#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
from .Communication import tcp

tcp = tcp()


class talk():
    def __init__(self):
        self.version = "0.0.1"

    def accept_message(self, host="0.0.0.0", port=5000, charset="utf8"):
        data = tcp.server(Host=host, Port=port, Charset=charset)
        while True:
            message = next(data)
            if message == "None":
                break
            else:
                yield message

    def send_message(self, host="127.0.0.1", port=5000, charset="utf8"):
        while True:
            message = str(input("You:"))
            if message == "None":
                yield "exit"
                break
            else:
                tcp.client(Host=host, Port=port,
                           message=message, Charset=charset)
