#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
from Core.Talk import talk
from argparse import ArgumentParser

talk = talk()


class pytalk():
    def __init__(self, mode="client",
                 host="127.0.0.1",
                 port=5000,
                 charset="utf8",
                 end_of_message=True):
        self.mode = mode
        if mode != "client" and mode != "server":
            raise ValueError('Not is client or server')

        self.accept_message = talk.accept_message(
                host=host, port=port, charset=charset,
                end_of_message=end_of_message)

        self.send_message = talk.send_message(host=host,
                                              port=port,
                                              charset=charset)

    def accept(self):
        while True:
            print(next(self.accept_message))

    def send(self):
        while True:
            next(self.send_message)

    @property
    def runtalk(self):
        if self.mode == "client":
            self.send()
        elif self.mode == "server":
            self.accept()


if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument('-m', '--mode', default='client',
                        type=str,
                        help="Use mode server or client, default is client",
                        dest="mode")

    parser.add_argument('-s', '--server', default='127.0.0.1',
                        type=str,
                        help="Host name or IP address of your server.",
                        dest="host")

    parser.add_argument('-p', '--port', default=2000,
                        type=int,
                        help='Port number of your server.',
                        dest="port")

    parser.add_argument(
        '--end_of_message', default=True,
        type=bool,
        help='When the message is the end command, used for the server.',
        dest='end_of_message'
        )

    parser.add_argument('--charset', default="utf8",
                        type=str,
                        help='Encoding format.',
                        dest='charset'
                        )

    args = parser.parse_args()

    pytalk = pytalk(mode=args.mode, host=args.host, port=args.port,
                    charset=args.charset, end_of_message=args.end_of_message)
    pytalk.runtalk
