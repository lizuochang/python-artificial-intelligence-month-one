"""
dict 服务端部分，处理请求逻辑
"""
from base64 import decode
from socket import *
from multiprocessing import Process
import signal
import sys
from time import sleep
from operation_db import *

# 全局变量
HOST = '0.0.0.0'
PORT = 8000
ADDR = (HOST, PORT)


def do_register(c, db, data):
    tmp = data.split(' ')
    name = tmp[1]
    passwd = tmp[2]
    if db.register(name, passwd):
        c.send(b'OK')
    else:
        c.send(b'FAIL')
def do_login(c,db,data):
    tmp = data.split(' ')
    name = tmp[1]
    passwd = tmp[2]
    if db.login(name, passwd):
        c.send(b'OK')
    else:
        c.send(b'FAIL')
def do_query(c,db,data):
    tmp=data.split(' ')
    name=tmp[1]
    word=tmp[2]

    db.insert_history(name,word)

    mean=db.query(word)

    if not mean:
        c.send("没有找到该单词".encode())
    else:
        msg="%s:%s"%(word,mean)
        c.send(msg.encode())
def do_hist(c,db,data):
    name = data.split(' ')[1]

    r = db.history(name)
    if not r:
        c.send(b"FAIL")
        return
    c.send(b'OK')
    for i in r:
        # i ==> (name,word,time)
        msg = "%s     %s     %s"%i
        sleep(0.1)  #　防止沾包
        c.send(msg.encode())

    sleep(0.1)
    c.send(b'##')

# 处理客户端请求
def do_request(c, db):
    db.create_cursor()
    while True:
        data = c.recv(1024).decode()
        print(c.getpeername(), ':', data)
        if not data or data[0] == 'E':
            c.close()
            sys.exit("客户端退出")
        elif data[0] == 'R':
            do_register(c, db, data)
        elif data[0] == 'L':
            do_login(c, db, data)
        elif data[0] == 'Q':
            do_query(c, db, data)
        elif data[0] == 'H':
            do_hist(c, db, data)


# 网络链接
def main():
    # 创建数据库链接对象
    db = Database()

    # 创建tcp套接字
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)

    # 处理僵尸进程
    # signal.signal(signal.SIGCHLD, signal.SIG_IGN)
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)
    print("Listen the port 8000")
    # 等待客户端链接
    while True:
        try:
            c, addr = s.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            s.close()
            db.close()
            sys.exit("服务器退出")
        except Exception as e:
            print(e)
            continue
        p = Process(target=do_request, args=(c, db))
        p.daemon = True
        p.start()


if __name__ == "__main__":
    main()
