import json

from sqlalchemy import Column, String

from app import storage

class Node(storage.Base):
	__tablename__ = 'nodes'

	# todo
	# ip_address String, primary_key
	# type String
	# public_key String
	# private_key String

	def __init__(self, ip_address):
		self.type = 'N'
		self.ip_address = ip_address
		self.public_key = ''
		self.private_key = ''

	def __str__(self):
		return self.to_json()

	def to_json(self):
		# todo
		return