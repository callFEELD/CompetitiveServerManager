import yaml
import jinja2
from typing import List, Union
from dataclasses import dataclass, field

CONFIG_FILE = 'commands.yml'
TEMPLATE_FILE = 'csm.cfg.j2'
OUT_FILE = '../csm.cfg'

CMD_NAMESPACE = "csm"
CMD_SEPERATOR = "_"


@dataclass
class Command:
    name: str = ""
    run: str = ""
    description: str = ""
    is_group: bool = False
    sub_cmds: List = field(default_factory=list)


def is_command(data: Union[dict, str]):
    if type(data) is dict and 'run' in data.keys():
        return True
    if type(data) is str:
        return True

    return False


def parse_command(data: Union[dict, str], name: str) -> Command:
    cmd = Command()
    cmd.name = name.lower()

    if type(data) is dict:
        cmd.run = data['run']
        if 'description' in data:
            cmd.description = data['description']
    else:
        cmd.run = data
    return cmd


def parse_commands(data: dict, prev_name=CMD_NAMESPACE) -> Command:
    cmd = Command()
    cmd.name = prev_name.lower()
    cmd.is_group = True
    cmd.description = "Group"

    for key in data.keys():
        name = key.lower()

        if is_command(data[key]):
            cmd.sub_cmds.append(parse_command(data[key], CMD_SEPERATOR.join([prev_name, name])))
        elif type(data[key]) is dict: 
            cmd.sub_cmds.append(parse_commands(data[key], CMD_SEPERATOR.join([prev_name, name])))
    
    return cmd


def get_commands(data: dict) -> Command:
    if 'commands' not in data.keys():
        return []

    return parse_commands(data['commands'])


def get_version(data: dict) -> str:
    if 'version' not in data.keys():
        return ""
    
    return str(data['version'])


def main():
    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    if data is None:
        return

    if type(data) is not dict:
        return
    
    if 'version' not in data.keys() or 'commands' not in data.keys():
        return
    
    version = get_version(data)
    cmd = get_commands(data)

    env = jinja2.Environment(loader=jinja2.FileSystemLoader("."))
    template = env.get_template(TEMPLATE_FILE)
    config_str = template.render(version=version, command=cmd)
    with open(OUT_FILE, 'w', encoding='utf-8') as f:
        f.write(config_str)


if __name__=="__main__":
    main()
