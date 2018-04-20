import codecs
from app.transaction.Transaction import Transaction
from app.node import key

from app import storage
from app.communicator import sender

# todo implement functions below
def add_transaction(tx):
	return

def get_transactions():
	# return mandatory
	return

def count():
	# return mandatory
	return

def remove_all():
	return

# important!
def create_tx(msg):
	# return mandatory
	return

# distribute Tx to all
def send_tx(tx):
	return

def validate_tx(pub_key, signature, message):
	#전자서명을 검증함
	if key.verify_signature(pub_key, signature, message):
		return True
