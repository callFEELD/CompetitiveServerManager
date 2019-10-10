"""
This file will manage the RCON connection to the server
"""

import valve.rcon
import valve.source.a2s

class RCON_COMMAND():
    DISABLE_MGE         = "sm plugins unload soap_tf2dm; mp_tournament_restart;"
    ENABLE_MGE          = "sm plugins load soap_tf2dm; mp_tournament_restart;"
    TOURNAMENT_RESTART  = "mp_tournament_restart;"
    SINGLE_READYUP      = "mp_tournament_readymode 1;"
    TEAM_READYUP        = "mp_tournament_readymode 0;"


def get_server_info(server_address, server_port):
    try:
        server_address = (server_address, int(server_port))

        # Server details
        with valve.source.a2s.ServerQuerier(server_address,  timeout=3.0) as server:
            info = server.info()
            player_count = server.players()["player_count"]

            print(f"Server Name: {info['server_name']}")
            print(f"Players: {player_count} / {info['max_players']}")
            #print(f"Ping: {ping}")
            print(f"Map: {info['map']}")
            print(f"Password protected: {info['password_protected']}")
            print(f"Game: {info['game']}")
            return {
                "server_name": info['server_name'],
                "game": info['game'],
                "map": info['map'],
                "player_count": info['player_count'],
                "max_players": info['max_players']
            }
        return None
    except Exception as e:
        print(e)
        return None

# RCON connection with command
def rcon_connect(server_address, server_port, server_password, command):
    try:
        server_address = (server_address, int(server_port))

        with valve.rcon.RCON(server_address, server_password, timeout=5.0) as rcon:
            response = rcon(f"{command}")
            return {
                "status": 200,
                "message": "OK",
                "server_response": response
            }
    except ConnectionRefusedError:
        print("Server refused connection")
        return {
            "status": 400,
            "message": "Server refused connection"
        }
    except valve.rcon.RCONAuthenticationError:
        print("Wrong RCON authentication")
        return {
            "status": 400,
            "message": "Wrong RCON password"
        }
    except TimeoutError:
        return {
            "status": 400,
            "message": "Server timeed out"
        }
    except Exception as e:
        return {
            "status": 400,
            "message": "Unknow error"
        }
