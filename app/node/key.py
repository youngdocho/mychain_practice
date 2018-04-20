import os

from ecdsa import SigningKey, NIST256p, VerifyingKey, SECP256k1

KEY_PATH = os.getcwd()


def generate_key():
    pri_key = SigningKey.generate(curve=SECP256k1)
    pub_key = pri_key.get_verifying_key()

    open(KEY_PATH + "/private.pem", "w", encoding='utf-8').write(pri_key.to_pem().decode('utf-8'))
    open(KEY_PATH + "/public.pem", "w", encoding='utf-8').write(pub_key.to_pem().decode('utf-8'))


def get_key():
    pri_key = SigningKey.from_pem(open(KEY_PATH + "/private.pem", encoding='utf-8').read())
    pub_key = VerifyingKey.from_pem(open(KEY_PATH + "/public.pem", encoding='utf-8').read())

    return pri_key, pub_key


# NOT USED FOR TEST
def key_to_string(pub_key):
    return pub_key.to_string()


# NOT USED FOR TEST
def get_pub_key_string():
    pri, pub = get_key()
    return pub.to_string()


def get_signature(message):
    pri, pub = get_key()
    return pri.sign(message.encode('utf-8'))


def verify_signature(pub_hex, sig_hex, message):
    pub_key = VerifyingKey.from_string(bytes.fromhex(pub_hex), curve=SECP256k1)
    return pub_key.verify(bytes.fromhex(sig_hex), message.encode('utf-8'))


if __name__ == '__main__':
    import json

    # If there is no file name 'private.pem' and 'public.pem' in project directory, please run function as below
    generate_key()

    pri, pub = get_key()

    # pub.to_string() return bytes
    # pub.to_string().hex() return hex string of public key
    pub_hex = pub.to_string().hex()

    msg1 = "MYChain"
    msg2 = "ECDSApractice"

    msg = msg1+msg2

    # sig: bytes
    sig = get_signature(msg)

    # convert signature bytes to hex string
    sig_hex = sig.hex()

    test_json = {
        'sig': sig_hex,
        'pub': pub_hex,
        'msg': msg
    }
    # make json string
    test_json_str = json.dumps(test_json)
    '''
        SEND || BROADCAST TO ADJACENT NODE.
    '''
    # Assume that below area is receiver side
    # retrieve json object from received json string
    recv_json_obj = json.loads(test_json_str)

    recv_sig_hex = recv_json_obj['sig']
    recv_pub_hex = recv_json_obj['pub']
    recv_msg = recv_json_obj['msg']

    # verify signature
    result = verify_signature(recv_pub_hex, recv_sig_hex, recv_msg)
    print(result)


    # SAB JIN :(
    # pub_str = ''.join(chr(x) for x in pub_bytes)
    # pub_str_encoded = pub_str.encode('utf-8')
    #
    # print(type(pub_str_encoded))
    # pub_str_encoded_str = ''.join(chr(x) for x in pub_str_encoded)
    # print(pub_str_encoded_str)

    # print(type(pub))
    # print(type(pub.to_string())) # Bytes

    # pub_str = ''.join(chr(x) for x in pub.to_string())

    #pub_str_encode = pub_str.encode('utf-8')
    # print(pub_str.encode('utf-8'))
    # print(type(pub_str.encode('utf-8')))
    #
    # pub_str_encode = ''.join(chr(x) for x in pub_str.encode('utf-8'))
    #
    # print(type(pub_str_encode))
    # print(sig)
    # print(type(sig))
    #
    # print(sig_str)
    # print(type(sig_str))
    # print(sig_str_encoded)
    #
    # print(sig_str_encoded.decode('utf-8'))



    # bytes to string
    # sig_str = ''.join(chr(x) for x in sig)

    # string encoded with utf-8
    # sig_str_encoded = sig_str.encode('utf-8')
    # print(type(sig_str_encoded))

    # print("PUB: " + pub_str_encode)
    # print("SIG: " + sig_str_encoded)