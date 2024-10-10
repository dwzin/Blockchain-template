import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = timestamp or time.time()
        self.nonce = 0
        self.hash = self.compute_hash()

    
    def compute_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.data}{self.timestamp}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()
    

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.diff = 2

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block", time.time())

    def get_last_block(self):
        return self.chain[-1] if self.chain else None


    def add_block(self, block):
        block.prev_block = self.get_last_block().hash
        block.hash = block.compute_hash()
        self.chain.append(block)
    
    def proof(self, block):
        block.nonce = 0
        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * self.diff):
            block.nonce += 1
            computed_hash = block.compute_hash()
        return computed_hash

    def check_chain(self):
        for i in range(1, len(self.chain)):
            previous_block = self.chain[i - 1]
            current_block = self.chain[i]

            
            if current_block.hash != current_block.compute_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    







