# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 14:27:23 2018

@author: SBY
"""
'''
import cgi
def notfound_404(environ, start_response):
    start_response('404 Not Found', [ ('Content-type', 'text/plain') ])
    return [b'Not Found']
class PathDispatcher:
    def __init__(self):
        self.pathmap = { }
    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        params = cgi.FieldStorage(environ['wsgi.input'],
        environ=environ)
        method = environ['REQUEST_METHOD'].lower()
        environ['params'] = { key: params.getvalue(key) for key in params }
        handler = self.pathmap.get((method,path), notfound_404)
        return handler(environ, start_response)
    def register(self, method, path, function):
        self.pathmap[method.lower(), path] = function
        return function
'''
import os
import time
import socket

def server():
    ip_port = ('0.0.0.0',9999)
    sk = socket.socket()
    sk.bind(ip_port)
    sk.listen(1)
    #获取当前目录
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    print('服务开启')
    
    while True:
        conn,addr = sk.accept()
        print("{0},{1}已连接".format(addr[0],addr[1]))
        while True:
            data = conn.recv(1024)
            print(data)
            cmd,file_name,file_size = str(data,'utf-8').split('|')
            path = os.path.join(base_dir,'data',file_name)
            print('路径:%s'%path)
            file_size = int(file_size)
            has_sent = 0
            
            with open(path,'wb') as fp:
                while has_sent != file_size:
                    data = conn.recv(1024)
                    fp.write(data)
                    has_sent += len(data)
                    print('\r'+'[保存进度]:%s%.02f%%' %
                           ('>' * int((has_sent/file_size) * 50),
                            float(has_sent / file_size)*100),end='')
            print()
            print('%s 保存成功！' %file_name)
    sk.close()       
if __name__ == '__main__':
    server()

#base_dir = os.path.dirname(os.path.abspath(__file__))
#path = os.path.join(base_dir,'data','4.mp4')
#with open(path,'wb') as fp:
    #print('success in')











