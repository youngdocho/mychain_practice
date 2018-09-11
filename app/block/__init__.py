import datetime

from app import storage
from app.block.Block import Block
from app.block.merkle_tree import merkle_tree
from app.consensus import pow


def create_block(transactions):
    # todo implement

    last_block = get_last_block()

    transactions_str = list(map(lambda x: x.to_json(), transactions))

    merkle_root = merkle_tree(transactions_str)

    block_info = merkle_root

    # create block instance
    _block = Block()

    if last_block:
        block_info += last_block.block_hash
        _block.prev_block_hash = last_block.block_hash
        _block.prev_block_id = last_block.block_id

    hash_result, nonce = pow.get_nonce(block_info, diff_bits=5)

    # block 정보
    _block.block_hash = hash_result
    _block.nonce = nonce
    _block.block_info = block_info
    _block.time_stamp = datetime.datetime.now()
    _block.block_id = "B" + str(_block.time_stamp)
    _block.merkle_root = merkle_root

    return _block


def store_block(_block):
    storage.insert(_block)


def count():
    return storage.count(Block)


def get_all_block():
    return storage.get_all(Block)


def get_genesis_block():
    b = Block()
    b.prev_block_id = 'B000000000000'
    b.prev_block_hash = '0'
    b.block_id = 'B000000000000'
    b.merkle_root = 'mychain'
    b.block_hash = 'mychain'
    b.nonce = 2010101010

    return b


def get_last_block():
    # todo
    return


def validate_block(block):
    from numpy import long
    # todo
    return True
