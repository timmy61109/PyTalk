#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
import TCP

ServerHost = str(input("ServerHost:"))
ServerPort = int(input("ServerPort:"))

while(1):
	Message = str(input("Key Your Message:"))
	TCP.EEG_TCP_Client(ServerHost, ServerPort, Message)
