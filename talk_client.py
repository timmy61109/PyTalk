#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
from Module.Communication import tcp

server_host = str(input("ServerHost:"))
server_port = int(input("ServerPort:"))

while True:
    message = str(input("Key Your Message:"))
    tcp.client(Host=server_host, Port=server_port, message=message)
