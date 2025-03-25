   
from argparse import ArgumentParser

from client import Client
from server import Server

from remoteServer import RemoteServer


argument_parser = ArgumentParser()
argument_parser.add_argument('-f', '--filename')
argument_parser.add_argument('-u', '--url')
argument_parser.add_argument('-p', '--portail', action = 'store_true')
arguments = argument_parser.parse_args()
server : Server
if arguments.filename is not None:
    server = Server(arguments.filename)
elif arguments.url is not None:
    server = RemoteServer(arguments.url)

client = Client(Server)

client.connexion()