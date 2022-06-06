
import socket

def startClient():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Socket successfully opened')
    except socket.error as error:
        print(f'Unable to open socket. Error returned: {error}')

if __name__ == '__main__':
    startClient()