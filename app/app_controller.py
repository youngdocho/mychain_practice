from app import log, storage, node, transaction, block
from app import communicator
from app.node.Node import Node
from app.communicator import receiver
from app.communicator import sender
from app.communicator import my_ip_address

import logging

# 블록체인 컨트롤 인터페이스 API
listen_thread = None
port_number = None


def start_app(ip_list, isPrivate):
    port_number = 3000
    storage.init()
    communicator.set_network(ip_list, isPrivate)
    start_communicator(port_number)


def finish_app():
    import os
    storage.session.commit()
    storage.session.close()
    stop_communicator()
    os._exit(1)


def send_transaction(msg):
    # pri_key, pub_key = key.get_key()
    tx = transaction.create_tx(msg)
    transaction.send_tx(tx)


def start_communicator(port):
    import threading
    global port_number
    port_number = port
    set_my_node(False)
    node.key.generate_key()

    log.write("Start node")

    global listen_thread
    listen_thread = threading.Thread(target=receiver.start, args=("Listener_Thread",
                                                                  communicator.my_ip_address.get_ip_address('en0'),
                                                                  port_number))
    listen_thread.start()
    return


def stop_communicator():
    communicator.receiver.stop()
    global listen_thread
    listen_thread.join()


# important!
def create_block():
    # todo
    return


def list_all_node():
    for n in node.get_all():
        log.write(n, logging.DEBUG)


def list_all_transaction():
    # todo
    return


def list_all_block():
    # todo
    return


# register my ip
def set_my_node(set_my_node=True):
    # todo
    return
