import time

import block


class Worker:
    def __init__(self):
        self.previous_block = None
        self.version = 1
        self.data = ""
        self.leading_zeroes = 1

    def set_previous_block(self, block):
        self.previous_block = block

    def set_version(self, version):
        self.version = version

    def set_data(self, data):
        self.data = data

    def set_version(self, data):
        self.data = data

    def set_leading_zeroes(self, leading_zeroes):
        self.leading_zeroes = leading_zeroes

    def find_valid_block(self):
        nonce = 0
        while self.previous_block is not None:
            nonce = nonce + 1
            new_block = block.Block(self.previous_block.get_hash(), self.data, nonce, int(time.time()), self.version)
            new_block_hash = new_block.get_hash().hexdigest()
            first_digits = new_block_hash[0:self.leading_zeroes]
            if first_digits == "0"*self.leading_zeroes:
                return new_block

