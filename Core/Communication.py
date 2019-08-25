#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
import socket


class tcp():
    def __init__(self):
        self.init_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def server(self, Host="0.0.0.0", Port=5000, Charset="utf8"):
        """
        接受檔案傳送過來
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            server.bind((Host, Port))  # 開始監聽的IP與Port
            server.listen(5)  # 設定連線上限5個
            while True:
                conn, addr = server.accept()
                with conn:
                    while True:
                        data = conn.recv(4096)
                        if not data or data.decode(Charset) == "None":
                            break
                        else:
                            yield data.decode(Charset)

    def client(self, Host="127.0.0.1", Port=5000, message="test",
               Charset="utf8"):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((Host, Port))
            client.sendall(message.encode(Charset))
