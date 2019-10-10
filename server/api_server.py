from flask import Flask, request, jsonify

import rcon_connector as rcon

app = Flask(__name__)

VERSION = 0.1

SUCCESS_STATUS = 200

class ERROR():
    AUTHENTICATE_ERROR = {
        "status": 500,
        "version": VERSION
    }
    FAILURE_STATUS = {
        "status": 400,
        "version": VERSION
    }


# Server Info
@app.route('/info', methods = ['POST'])
def info():
    address = request.form['server_address']
    port = request.form['server_port']
    result = rcon.get_server_info(address, port)
    return api_return_handler(result)


# Control commands
@app.route('/control/<command>', methods = ['POST'])
def control(command):
    command = command.lower()

    # authenticate
    address = request.form['server_address']
    port = request.form['server_port']
    password = request.form['server_password']

    if address is not None and port is not None and password is not None:
        if command == 'disable_mge':
            result = rcon.rcon_connect(address, port, password, rcon.RCON_COMMAND.DISABLE_MGE)
            return api_return_handler(result)
        elif command == 'enable_mge':
            result = rcon.rcon_connect(address, port, password, rcon.RCON_COMMAND.ENABLE_MGE)
            return api_return_handler(result)
        elif command == 'single_readyup':
            result = rcon.rcon_connect(address, port, password, rcon.RCON_COMMAND.SINGLE_READYUP)
            return api_return_handler(result)
        elif command == 'team_readyup':
            result = rcon.rcon_connect(address, port, password, rcon.RCON_COMMAND.TEAM_READYUP)
            return api_return_handler(result)
    else:
        return jsonify(ERROR.AUTHENTICATE_ERROR)



def api_return_handler(response):
    if response is None:
        return ERROR.FAILURE_STATUS

    return jsonify({
        "status": SUCCESS_STATUS,
        "version": VERSION,
        "result": response
    })


if __name__ == '__main__':
    app.run()