#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
import TCP
import FileAccess as FA
#FileName = "./Data.csv"
ServerHost, ServerPort = "",50007
while(1):
    conn, addr, ServerHost, ServerPort = TCP.EchoClient(ServerHost, ServerPort)
    date, date1, ClientIP, ClientPort, ServerHost, ServerPort, ReprData = TCP.EchoData(conn, addr, ServerHost, ServerPort)
    Data = date + " " + str(ClientIP) + ":" + str(ClientPort) + " " + str(ServerHost) + ":" + str(ServerPort) + "\n" + ReprData[1:-1] + '\n'
    print Data
