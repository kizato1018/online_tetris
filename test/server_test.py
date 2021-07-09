import threading
import socket
import time

class User:
    def __init__(self, client, address, num):
        self.client = client
        self.address = address
        self.num = 0
        self.done = False


def listener(users, number):
    client, address = server.accept()
    user = User(client, address, number)
    users.append(user)
    print('accept number ', number)
    while not user.done:
        data = client.recv(100)
        print("user %d get %s" % (number, data.decode()))
    print("user %d is done." %(number))
    client.close()
    
def update(users):
    count = 0
    while count < 10:
        for user in users:
            user.client.send(str.encode(str(count)))
        count += 1
        time.sleep(1)
    for user in users:
        user.done = True

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 7414))
server.listen(5)

users = []
print("update starting")
update_thread = threading.Thread(target=update, args=(users,))
update_thread.start()
for i in range(5):
    listing_thread = threading.Thread(target=listener, args=(users, i))
    listing_thread.daemon = True
    listing_thread.start()
print("Hi")
update_thread.join()
# listing_thread.join()


# # 建立全域性ThreadLocal物件:
# local_school = threading.local()
# def process_student():
#     print('Hello, %s (in %s)' % (local_school.student, threading.current_thread().name))
# def process_thread(name):
#     # 繫結ThreadLocal的student:
#     local_school.student = name
#     process_student()
# t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
# t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
# t1.start()
# t2.start()

# t1.join()
# t2.join()

# python test/thread.py