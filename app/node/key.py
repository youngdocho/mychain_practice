import os

from ecdsa import SigningKey, NIST256p, VerifyingKey
from app import log

KEY_PATH = os.getcwd()

#키를 생성하여 로컬에 저장하는 함수
def generate_key():
	# 공개키, 개인키 생성
	pri_key = SigningKey.generate(curve=NIST256p)
	pub_key = pri_key.get_verifying_key()

	# 생성된 공인키, 개인키를 파일로 생성
	open(KEY_PATH + "/private.pem", "w", encoding='utf-8').write(pri_key.to_pem().decode('utf-8'))
	open(KEY_PATH + "/public.pem", "w", encoding='utf-8').write(pub_key.to_pem().decode('utf-8'))
	log.write("New Keys are generated")


#로컬 함수로부터 키를 불러오는 함수
def get_key():
	# 파일로부터 읽어들인 공개키, 개인키 리턴
	pri_key = SigningKey.from_pem(open(KEY_PATH + "/private.pem", encoding='utf-8').read())
	pub_key = VerifyingKey.from_pem(open(KEY_PATH + "/public.pem", encoding='utf-8').read())

	return pri_key, pub_key


def key_to_string(pub_key):
	return pub_key.to_string()


def get_pub_key_string():
	pri, pub = get_key()
	return pub.to_string()


#전자서명을 가져오는 함수
def get_signature(message):
	private_key, pub = get_key()
	return private_key.sign(message.encode('utf-8'))


#전자서명을 검증하는 함수
def verify_signature(public_key_str, signature, message):
	public_key = VerifyingKey.from_string(bytes.fromhex(public_key_str), curve=NIST256p)
	return public_key.verify(bytes.fromhex(signature), message.encode('utf-8'))