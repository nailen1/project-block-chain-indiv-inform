import hashlib
import json
import time


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        data_str = str(self.index) + str(self.timestamp) + \
            str(self.data) + str(self.previous_hash)
        hash_str = data_str.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


class BlockChain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calc_hash()
        self.chain.append(new_block)


blockchain = BlockChain()

daniel_blockchain = BlockChain()

naver_data = {"Name": "Daniel", "Service": "Naver"}
naver_block = Block(len(blockchain.chain), time.time(),
                    naver_data, blockchain.get_latest_block().hash)
blockchain.add_block(naver_block)
daniel_blockchain.add_block(naver_block)

shinhan_data = {"Name": "Daniel", "Service": "Shinhan Card"}
shinhan_block = Block(len(blockchain.chain), time.time(),
                      shinhan_data, blockchain.get_latest_block().hash)
blockchain.add_block(shinhan_block)
daniel_blockchain.add_block(shinhan_block)

print("Blockchain status:")
for block in blockchain.chain:
    print(json.dumps({"Index": block.index, "Timestamp": block.timestamp,
          "Data": block.data, "Previous Hash": block.previous_hash, "Hash": block.hash}))

print("Daniel's Blockchain status:")
for block in daniel_blockchain.chain:
    print(json.dumps({"Index": block.index, "Timestamp": block.timestamp,
          "Data": block.data, "Previous Hash": block.previous_hash, "Hash": block.hash}))
