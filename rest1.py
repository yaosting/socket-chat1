# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 09:35:46 2018

@author: SBY
"""
"""
#import rest
import time
_hello_resp = '''\
<html>
    <head>
        <title>Hello {name}</title>
    </head>
    <body>
        <h1>Hello {name}!</h1>
    </body>
</html>'''
def hello_world(environ, start_response):
    start_response('200 OK', [ ('Content-type','text/html')])
    params = environ['params']
    resp = _hello_resp.format(name=params.get('name'))
    yield resp.encode('utf-8')
_localtime_resp = '''\
<?xml version="1.0"?>
<time>
    <year>{t.tm_year}</year>
    <month>{t.tm_mon}</month>
    <day>{t.tm_mday}</day>
    <hour>{t.tm_hour}</hour>
    <minute>{t.tm_min}</minute>
    <second>{t.tm_sec}</second>
</time>'''
def localtime(environ, start_response):
    start_response('200 OK', [ ('Content-type', 'application/xml') ])
    resp = _localtime_resp.format(t=time.localtime())
    yield resp.encode('utf-8')
if __name__ == '__main__':
    from rest import PathDispatcher
    from wsgiref.simple_server import make_server
    dispatcher = PathDispatcher()
    dispatcher.register('GET', '/hello', hello_world)
    dispatcher.register('GET', '/localtime', localtime)
    httpd = make_server('', 8080, dispatcher)
    print('Serving on port 8080...')
    httpd.serve_forever()
"""
"""
import socket,json
 
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',9999))
 
while True:
    data = input('>>')
    client.send(data.encode())
    json_obj = client.recv(1024).decode()
    file_info = json.loads(json_obj)
    filename = file_info['filename']
    filesize = file_info['filesize']
    print('filename=',filename,'filesize=',filesize)
    recevie_size = 0
    myfile = open(filename,'wb')
    while recevie_size < filesize:
        
        filedata = client.recv(1024)
        myfile.write(filedata)
        recevie_size += len(filedata)
    else:
        myfile.close()
        print('receive file finished!') 
"""  
import os
import socket
#use tcp
def client():
    ip_port = ('127.0.0.1',9999)
    sk = socket.socket()
    sk.connect(ip_port)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    #base_dir = 'D: 
    print(type(base_dir),base_dir)
    while True:
        inp = input('>>>').strip()
        cmd,path = inp.split('|')
        path = os.path.join(base_dir,path)
        #path = 'D:\test55.jpg'
        print(path)
        if not os.path.exists(path):
            print('文件名错误')
        if os.path.exists(path):
        #构建路径
            file_name = os.path.basename(path)
            #返回路径中的中文名
            file_size = os.stat(path).st_size
            file_info = 'post|%s|%s'%(file_name,file_size)
            sk.sendall(bytes(file_info,'utf-8'))
            has_sent = 0
            
            with open(path,'rb') as fp:
                while has_sent != file_size:
                    data = fp.read(1024)
                    sk.sendall(data)
                    has_sent += len(data)
                    print('\r'+'[上传进度]:%s%.02f%%' %
                           ('>' * int((has_sent/file_size) * 50),
                            float(has_sent / file_size)*100),end='')
                    
            print()
            print('%s 上传成功！' %file_name)
        
    sk.close()
if __name__ == '__main__':
    client()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
