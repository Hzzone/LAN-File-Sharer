import socket
import logging
import config
import utils
import sys
import transfer

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S')

def server_run():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # print(utils.get_internal_ip())
        sock.bind((utils.get_internal_ip(), config.server_port))
    except socket.error as e:
        logging.error("socket create error: %s" % e)
        sys.exit(1)
    sock.listen(5)
    while True:
        conn, address = sock.accept()
        msg = conn.recv(1024)
        if msg:
            logging.debug('received from %s: %s' % (address, msg))
            transfer.Server_transfer(conn, msg).start()
            


if __name__ == "__main__":
    server_run()

