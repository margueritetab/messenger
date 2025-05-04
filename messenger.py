   
from argparse import ArgumentParser

from client import Client
from server import Server

from remoteServer import RemoteServer


argument_parser = ArgumentParser()
argument_parser.add_argument('-f', '--filename')
argument_parser.add_argument('-u', '--url')
argument_parser.add_argument('-p', '--portail', action = 'store_true')
arguments = argument_parser.parse_args()
# Vous pouvez indiquer que votre variable `server` est soit
# du type `Server`, soit du type `RemoteServer`
server : Server | RemoteServer
if arguments.filename is not None:
    server = Server.load_from_json_file(arguments.filename)
elif arguments.url is not None:
    server = RemoteServer(arguments.url)

client = Client(server)

client.connexion()
