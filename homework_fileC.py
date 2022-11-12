import socket
import os      #用于判断文件是否存在

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1',8888))

def sendfile(conn):
    str1 = conn.recv(1024)
    filename = str1.decode('utf-8')   #解码接收到的内容
    print('The client requests my file:',filename)
    if os.path.exists(filename):
        print('I have %s, begin to download!' % filename)
        conn.send(b'yes')
        conn.recv(1024)
        size = 1024
        with open(filename,'rb') as f:
            while True:
                data = f.read(size)
                conn.send(data)
                if len(data) < size:
                    break
        print('%s is downloaded successfully!' % filename)
    else:
        print('Sorry, I have no %s' % filename)
        conn.send(b'no')
    conn.close()

while True:
    sendfile(s)

c.close()
