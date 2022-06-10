# Generator

The `generate.py` script will generate the `csm.cfg` tf2 config based on the commands listed in the `commands.yml` file.

## Setup

The generator is tested with the python version `3.8.5`.

In order to run the script, you need to install the libs listed in the `requirements.txt` file

```cmd
pip install -r requirements.txt
```

## Run

In order to run the script, change your current directory to `./generator` and run the python script:

```cmd
cd generator
python generate.py
```

After you run the file, the `..\csm.cfg` is created/updated.
