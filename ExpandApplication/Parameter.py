from argparse import ArgumentParser


def parameter():
    parser = ArgumentParser()

    parser.add_argument('-s', '--server', default='0.0.0.0',
                        type=str,
                        help="Host name or IP address of your server.",
                        dest="ip")
    parser.add_argument('-p', '--port', default=2000,
                        type=int, help='Port number of your server.',
                        dest="port")

    parser.add_argument('--transaction-server-host', default="0.0.0.0",
                        type=str,
                        help='Transaction server host.',
                        dest="transaction_server_host")
    parser.add_argument('--transaction-server-port', default=5000,
                        type=int,
                        help='Transaction server port.',
                        dest="transaction_server_port")

    parser.add_argument('--blockchain-server-host', default="0.0.0.0",
                        type=str,
                        help='Blockchain server host.',
                        dest="blockchain_server_host")
    parser.add_argument('--blockchain-server-port', default=6000,
                        type=int,
                        help='Blockchain server port.',
                        dest="blockchain_server_port")

    parser.add_argument('--blockchain-client-host', default="127.0.0.1",
                        type=str,
                        help='Blockchain client host.',
                        dest="blockchain_client_host")
    parser.add_argument('--blockchain-client-port', default=6000,
                        type=int,
                        help='Blockchain client port.',
                        dest="blockchain_client_port")

    args = parser.parse_args()
    return args
