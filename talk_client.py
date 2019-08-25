#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
from Module.Communication import tcp


tcp = tcp()
server_host = str(input("Server Host:"))
server_port = int(input("Server Port:"))
while True:
    message = str(input("Key Your Message:"))
    if message == "None":
        print("exit")
    else:
        tcp.client(Host=server_host, Port=server_port, message=message)
        print(message)
