import hashlib
import random

from numpy import long

max_nonce = 2 ** 32


def get_nonce(block_info, diff_bits):
    # todo
    nonce = 0
    return nonce


if __name__ == '__main__':
    n = get_nonce('TEST', 20)
    print(n)
