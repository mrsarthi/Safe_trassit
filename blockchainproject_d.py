import hashlib
import json
import sys
import random
import time

# Hashing function for generating SHA-256 hash


def hashMe(msg=""):
    if type(msg) != str:
        # Ensure repeatability by sorting keys.
        msg = json.dumps(msg, sort_keys=True)

    if sys.version_info.major == 2:
        return unicode(hashlib.sha256(msg).hexdigest(), 'utf-8')
    else:
        return hashlib.sha256(str(msg).encode('utf-8')).hexdigest()

# Random transaction generator to simulate money transfers


def makeTransaction(maxValue=3):
    sign = int(random.getrandbits(1)) * 2 - 1  # Randomly choose -1 or 1
    amount = random.randint(1, maxValue)
    vinnyPays = sign * amount
    kinnyPays = -1 * vinnyPays
    # Ensure conservation of tokens.
    return {u'Vinny': vinnyPays, u'kinny': kinnyPays}


# Create a list of transactions (30 random transactions)
txnBuffer = [makeTransaction() for i in range(30)]

# Define a Block class to represent each block in the blockchain


class Block:
    def __init__(self, index, previous_hash, timestamp, transactions, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.hash = hash

    def __repr__(self):
        return f"Block {self.index} [Hash: {self.hash}]"

# Blockchain class


class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        # Creating the first block with index 0
        genesis_block = Block(0, "0", time.time(), [], hashMe("Genesis Block"))
        self.chain.append(genesis_block)

    def add_block(self, transactions):
        last_block = self.chain[-1]
        block_index = last_block.index + 1
        timestamp = time.time()
        block_hash = hashMe(
            f"{block_index}{last_block.hash}{timestamp}{transactions}")

        new_block = Block(block_index, last_block.hash,
                          timestamp, transactions, block_hash)
        self.chain.append(new_block)

    def get_last_block(self):
        return self.chain[-1]

    def display_chain(self):
        for block in self.chain:
            print(
                f"Block #{block.index} - Hash: {block.hash}\nTransactions: {block.transactions}\n")


# Initialize Blockchain
blockchain = Blockchain()

# Simulate adding blocks with transactions
for txn in txnBuffer:
    blockchain.add_block(txn)

# Display the Blockchain
blockchain.display_chain()

# Function to verify the blockchain (for integrity check)


def verify_blockchain(chain):
    for i in range(1, len(chain)):
        current_block = chain[i]
        previous_block = chain[i - 1]

        # Verify hash of the current block is correct
        if current_block.hash != hashMe(f"{current_block.index}{previous_block.hash}{current_block.timestamp}{current_block.transactions}"):
            return False

        # Verify that the block's previous hash matches the previous block's hash
        if current_block.previous_hash != previous_block.hash:
            return False

    return True


# Check the integrity of the blockchain
is_valid = verify_blockchain(blockchain.chain)
print(f"Blockchain valid: {is_valid}")
