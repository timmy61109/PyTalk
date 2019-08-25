#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
from Module.Communication import tcp

server_host = str(input("ServerHost:"))
server_port = int(input("ServerPort:"))

while True:
    Message = str(input("Key Your Message:"))
    tcp.client(server_port, server_host, Message)
