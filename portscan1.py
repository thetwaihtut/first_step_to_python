import socket

do=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.setdefaulttimeout(2)
host=input('enter ipaddress to scan: ')
port=int(input('enter port number to scan: '))

def action(y):
    if do.connect_ex((host,port)):
        print('port {} is closed'.format(y))
    else:
        print('port {} is opened'.format(y))

action(port)