#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
from .Communication import tcp


tcp = tcp()


class talk():
    def __init__(self):
        self.version = "0.0.1"

    def accept_message(self):
        server_host, server_port = "0.0.0.0", 5000
        data = tcp.server(Host=server_host, Port=server_port)
        while True:
            message = next(data)
            if message == "None":
                break
            else:
                print(message)

    def send_message(self):
        server_host = str(input("Server Host:"))
        server_port = int(input("Server Port:"))
        while True:
            message = str(input("You:"))
            if message == "None":
                print("exit")
                break
            else:
                tcp.client(Host=server_host, Port=server_port, message=message)
                print("success")
