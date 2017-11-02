import hashlib, struct, json


def origin_block():
    return Block(hashlib.sha256(b"0"), "", 0, 1509614545, 1)


class Block:
    def __init__(self, hash_prev_block, data, nonce, unix_time, version=1):
        # Sha256 hash
        self.hash_prev_block = hash_prev_block
        # String
        self.data = data
        #ingeger
        self.nonce = nonce
        # integer
        self.unix_time = unix_time
        # integer
        self.version = version

    def get_hash(self):
        byte_buffer = bytearray()
        byte_buffer.extend(map(ord, self.hash_prev_block.hexdigest()))
        byte_buffer.extend(map(ord, self.data))
        byte_buffer.extend(struct.pack(">d", self.nonce))
        byte_buffer.extend(struct.pack(">d", self.unix_time))
        byte_buffer.extend(struct.pack(">d", self.version))
        return hashlib.sha256(byte_buffer)

    def __str__(self):
        return json.dumps({
            "hash": self.get_hash().hexdigest(),
            "hash_prev": self.hash_prev_block.hexdigest(),
            "data": self.data,
            "nonce": self.nonce,
            "timestamp": self.unix_time,
            "version": self.version
        })
