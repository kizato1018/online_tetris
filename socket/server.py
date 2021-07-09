import socket
import threading

ip = "127.0.0.1"
port = 7414

# class Data:
#     def __init__(self, header, body):
#         self.header = header
#         self.body = body

class User:
    def __init__(self, client, address):
        self.client = client
        self.address = address
        self.get_msg = ""
        self.send_msg = ""
        self.update = False
    def thread(self):
        t = threading.Thread(target=self.jobs())
        t.start()
        t.join()
    def jobs(self):
        while True:
            data = self.client.recv(1024)
            print(data)
            status, msg = str(data).split(' ', 1)  # status 1 client send, 2 client recv
            if((status) == "0"):
                continue
            elif(status == "1"):
                self.get_msg = msg
                self.update = True
                self.client.send("2 ACK")
            elif(status == "2"):
                if(self.send_msg):
                    self.client.send("2 " + self.send_msg)
                    self.send_msg = ""
            elif(status == "-1"):
                break

def update(users):
    msg = ""
    for user in users:
        user.get_msg = msg
        msg = ""
        if(user.update):
           msg = user.send_msg
           user.update = False
    users[0].get_msg = msg

def main():
    Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Socket.bind((ip, port))
    Socket.listen(5)
    users = []
    while True:
        users.append(User(Socket.accept()))


if __name__ == 'main':
    main()