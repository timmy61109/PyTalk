#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
from Module.Communication import tcp

tcp = tcp()
server_host, server_port = "0.0.0.0", 5000
data = tcp.server(Host=server_host, Port=server_port)
while True:
    message = next(data)
    if message == "None":
        break
    else:
        print(message)
