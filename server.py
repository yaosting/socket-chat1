# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 09:49:14 2018

@author: SBY
"""
"""
import socket

sk = socket.socket()
sk.bind(("127.0.0.1",8080))
sk.listen(5)

while True:
    conn,address = sk.accept()
    print(conn,address)
    conn.sendall(bytes("开始传送",encoding="utf-8"))
    
    size = conn.recv(1024)
    size_str = str(size,encoding="utf-8")
    file_size = int(size_str)



    has_size = 0
    f = open("test44.jpg","wb")
    while True:
        if file_size == has_size:
            break
        date = conn.recv(1024)
        f.write(date)
        has_size += len(date)

    f.close()
"""

import socket
import os
'''
使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包。但是，能不能到达就不知道了。
 
虽然用UDP传输数据不可靠，但它的优点是和TCP比，速度快，对于不要求可靠到达的数据，就可以使用UDP协议。
 
我们来看看如何通过UDP协议传输数据。和TCP类似，使用UDP的通信双方也分为客户端和服务器。服务器首先需要绑定端口
绑定端口和TCP一样，但是不需要调用listen()方法，而是直接接收来自任何客户端的数据
'''
# ipv4        SOCK_DGRAM指定了这个Socket的类型是UDP

def udp_server():
    #ip_port = ('0.0.0.0',9999)
    #sk = socket.socket()
    #sk.bind(ip_port)
    #sk.listen(1)
    #获取当前目录
    base_dir = os.path.dirname(os.path.abspath(__file__))
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('127.0.0.1', 9998))
    print('服务开启')
    
    while True:
        #conn,addr = sk.accept()
        #print("{0},{1}已连接".format(addr[0],addr[1]))
        while True:
            #data = conn.recv(1024)
            data, addr = s.recvfrom(1024)
            print(data)
            cmd,file_name,file_size = str(data,'utf-8').split('|')
            path = os.path.join(base_dir,'data',file_name)
            print('路径:%s'%path)
            file_size = int(file_size)
            has_sent = 0
            
            with open(path,'wb') as fp:
                while has_sent != file_size:
                    data, addr = s.recvfrom(1024)
                    fp.write(data)
                    has_sent += len(data)
                    print('\r'+'[保存进度]:%s%.02f%%' %
                           ('>' * int((has_sent/file_size) * 50),
                            float(has_sent / file_size)*100),end='')
            print()
            print('%s 保存成功！' %file_name)
    s.close()       
if __name__ == '__main__':
    udp_server()
    















