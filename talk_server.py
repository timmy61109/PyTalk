#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
from Module.Communication import tcp

server_host, server_port = "", 50000
data = tcp.server(Host=server_host, Port=server_port)
while True:
    message = next(data)
    print(message)
