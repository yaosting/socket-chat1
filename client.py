# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 09:49:16 2018

@author: SBY
"""
"""
import socket
import os

obj = socket.socket()

obj.connect(("127.0.0.1",8080))

ret_bytes = obj.recv(1024)
ret_str = str(ret_bytes,encoding="utf-8")
print(ret_str,len(ret_str))

size = os.stat("sb1.jpg").st_size
obj.sendall(bytes(str(size),encoding="utf-8"))

obj.recv(1024)

with open("sb1.jpg","rb") as f:
    for line in f:
        obj.sendall(line)

import socket

def main():
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 获取用户输入的服务器ip，port，文件名
    server_ip = input("请输入服务器ip:")
    server_port = int(input("请输入服务器端口:"))
    file_name = input("请输入要下载的文件名:")
    # 连接服务器
    tcp_client_socket.connect((server_ip, server_port))
    # 发送请求的文件名
    tcp_client_socket.send(file_name.encode("utf-8"))
    # 接收返回的内容写入文件
    file_content = tcp_client_socket.recv(1024*1024)
    # 内容不为空就写入文件
    if file_content:
        with open("download_"+file_name, "wb") as f:
            f.write(file_content)
    # 关闭客户端socket
    tcp_client_socket.close()

if __name__ == '__main__':
    main()
"""
import os
import socket
 
def udp_client():
    #ip_port = ('127.0.0.1',9999)
    #sk = socket.socket()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #sk.connect(ip_port)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    print(base_dir)
    while True:
        inp = input('>>>').strip()
        cmd,path = inp.split('|')
        path = os.path.join(base_dir,path)
        #构建路径
        file_name = os.path.basename(path)
        #返回路径中的中文名
        file_size = os.stat(path).st_size
        file_info = 'post|%s|%s'%(file_name,file_size)
        s.sendto(bytes(file_info,'utf-8'), ('127.0.0.1', 9998))
        #sk.sendall(bytes(file_info,'utf-8'))
        has_sent = 0
        
        with open(path,'rb') as fp:
            while has_sent != file_size:
                data = fp.read(1024)
                s.sendto(data, ('127.0.0.1', 9998))
                #sk.sendall(data)
                has_sent += len(data)
                print('\r'+'[上传进度]:%s%.02f%%' %
                       ('>' * int((has_sent/file_size) * 50),
                        float(has_sent / file_size)*100),end='')
                
        print()
        print('%s 上传成功！' %file_name)
    s.close()


if __name__ == '__main__':
    udp_client()













