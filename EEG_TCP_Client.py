#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
import TCP

target_host = "127.0.0.1"
target_port = 50007

while(1):
	TCP.EEG_TCP_Client(target_host, target_port, String)
	Counter += 1
	#TCP.EEG_TCP_Client(target_host, target_port, String2)
	#Counter += 1
	print "Counter", Counter
