# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 11:37:08 2018

@author: SBY
"""

import socket
import time

class ChatClient:
    def __init__(self,username,port):
        self.username = username
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(("127.0.0.1", port))
        
    def send_msg(self, msg):
        self.socket.send("{username}::{msg}".format(username=self.username,msg=msg).encode("utf-8"))
        
    def recv_msg(self):
        data=self.socket.recv(1024)
        if data:
            print("\n【姚小桑】"+" "+time.strftime('%Y-%m-%d:%H:%M:%S',time.localtime(time.time())))
            print(data.decode("utf-8"))
            return True
        return False
    def main(self):
        data = self.socket.recv(1024)
        print(data.decode("utf-8"))
        msg = input("请输入消息：")
        self.send_msg(msg)
        while True:
            if self.recv_msg():
                msg=input("\n我：")
                self.send_msg(msg)
                if msg == "exit":
                    print("聊天室已关闭")
                    break

if __name__ == '__main__':
    cc = ChatClient(username="小姚", port=9997)
    cc.main()