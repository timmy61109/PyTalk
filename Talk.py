#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
from Core.Talk import talk


server_port = int(input("Server Port:"))
server_host = str(input("Server Host:"))
talk = talk()
accept_message = talk.accept_message()
send_message = talk.send_message()
while True:
    next(accept_message)
    next(send_message)
