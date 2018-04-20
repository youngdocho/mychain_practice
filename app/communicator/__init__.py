import socket
import threading
import time

import zmq

from app import log
from app.node import Node
from app import node

PING_PORT_NUMBER = 9999
PING_MSG_SIZE = 1
PING_INTERVAL = 5  # Once per second

is_running = True
t = None

def stop():
	global is_running, t
	is_running = False
	t.join()

def set_network(ip_list, isPrivate = True):
	if isPrivate:
		# todo
		for ip in ip_list:
			print(ip)
	else:
		start_public()

def start_public():
	return
