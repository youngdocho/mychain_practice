import datetime
import json

from dateutil import parser
from sqlalchemy import Column, String, Integer, DateTime

# import key
from app import storage

class Transaction(storage.Base):
	__tablename__ = 'transactions'

	#_id Integer
	# type String
	# time_stamp DateTime
	# tx_id String
	# pub_key String
	# message String
	# signature String

	def __init__(self):
		self.type = 'T'
		self.time_stamp = datetime.datetime.now()
		self.tx_id = self.type + self.time_stamp.strftime('%Y%m%d%H%M%S')
		self.pub_key = ''
		self.message = ''  # document hash
		self.signature = ''

	def __str__(self):
		return self.to_json()


	def to_json(self):
		# todo
		return

	def from_json(self, dictionary):
		# todo
		return