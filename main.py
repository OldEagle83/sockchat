# This is a basic chat program. It opens a socket on the server and waits for a user message.
# Once received it will reply with confirmation and continue to do so until the user closes the connection.
# Chat logs will be saved with timestamp in slog.txt, unencrypted <- possibly to-do
# Otherwise, the connection will timeout in 60 seconds

'''
Usage:
to write
'''

import socket
from datetime import datetime

class cmd(str):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # def exit:
    #     break

    def log(self):
        f = open("slog", "r")
        print(f.read())

    def encode(self, str):
        estring = ''
        for i in str:
            estring.append(alphabet.index(i))
        return estring



def startServer(port):
    s = socket.socket()
    print('Successfully opened socket')
    s.bind(('', port))
    print(f'Socket bind to {port}')
    s.listen(5)
    print('Accepting connections...')

    # Loop to keep the socket listening
    cinput = ''
    tinput = ''
    f = open("slog.txt", "a")
    while True:
        # Accept connection with client.
        c, addr = s.accept()
        print('Accepted connection from', addr)

        # Greeted the client. encoding to send byte type.
        c.send('Thank you for connecting\n\r'.encode())
        c.send('Type ~ to exit\n\r'.encode())

        while cinput != '~':
            cinput = c.recv(1024).decode()
            if cinput.endswith('\n'):
                c.send(f'Received {tinput}\n\r'.encode())
                dt = datetime.now()
                f.write(str(dt) + ': ' + tinput + '\n')
                #f.write(tinput)
                tinput = ''
            else:
                tinput += cinput

        # Close the connection with the client
        c.close()

        # Close the log file
        f.close()

        # Breaking once connection closed
        break



def cmdParser(str):
    cmdlist = [exit, encode, log]
    if str in cmdlist:
        return cmd.str
    else:
        return 'Command not recognized'

if __name__ == '__main__':
    startServer(5555)