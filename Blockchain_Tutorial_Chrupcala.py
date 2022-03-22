# This is a self-typed recreation of the work of Michael Chrupcala:
# - URL: https://medium.com/coinmonks/python-tutorial-build-a-blockchain-713c706f6531
# - github: https://github.com/mchrupcala/blockchain-walkthrough

# He has placed these materials under the following MIT License:

# MIT License

# Copyright (c) 2020 Michael

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE. 

# For encryption
import hashlib

# formatting of blocks
import json

# time for each block's timestamp
from time import time

# Creating of Blockchain class and variables
class Blockchain(object):
    def __init__(self):
        # Empty list that we'll add blocks to, our 'block-chain'
        self.chain = []
        # Transactions sit in this array until approved and added to new block
        self.pending_transactions = []
        # Method that will be defined, used to add each block to the chain. Example is Satoshi message
        self.new_block(previous_hash="The times 03/Jan/2009 Chancellor on brink of second bailout for bank.", proof=100)


    # Function to build new blocks
    def new_block(self, proof, previous_hash=None):
        # Creation of JSON object with listed properties
        block = {
         # Index: takes length of blockchain and adds 1 to it, used to reference individual block (genesis block = 1)
            'index': len(self.chain) + 1,
            # using time() import, stamps block when created, ability to check when transaction confirmed on-chain
            'timestamp': time(),
            # Any 'pending' tranactions to be included in block
            'transactions': self.pending_transactions,
            # Comes from miner, who believes they found 'nonce' or 'proof'
            'proof': proof,
            # Hashed version of most recent approved block
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        # "Empty" the 'pending' list of transactions (they were previously added)
        self.pending_transactions = []
        # Add new block to self.chain and return it
        self.chain.append(block)
    
        return block


    # Functions to create new transactions and get the last block
    @property
    # Call chain in order to receive the block that was added most recently
    def last_block(self):
        
        return self.chain[-1]

    # Simplified transaction interaction
    def new_transaction(self, sender, recipient, amount):
        # JSON object
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        # Adding JSON object 'transaction' to pool of pending_transactions
        self.pending_transactions.append(transaction)
        # return index of block which new transaction is going to be added to
        return self.last_block['index'] + 1


    # Create function to hash blocks
    def hash(self, block):
        # Takes new block and changes key/value pairs all into strings
        string_object = json.dumps(block, sort_keys=True)
        # Turns above string into Unicode, to be passed to sha256 hashing
        block_string = string_object.encode()
        
        # Use of sha256 to create 64 character encrypted string
        raw_hash = hashlib.sha256(block_string)
        # Turn hash string to hexidecimal string
        hex_hash = raw_hash.hexdigest()
        
        # return our hexidecimal hash
        return hex_hash


# Creation of new blockchain & 'send money'
# Initialize instance of our blockchain class
blockchain = Blockchain()
t1 = blockchain.new_transaction("Satoshi", "Mike", '5 BTC')
t2 = blockchain.new_transaction("Mike", "Satoshi", '1 BTC')
t3 = blockchain.new_transaction("Satoshi", "Hal Finney", '5 BTC')
blockchain.new_block(12345)

t4 = blockchain.new_transaction("Mike", "Alice", '1 BTC')
t5 = blockchain.new_transaction("Alice", "Bob", '0.5 BTC')
t6 = blockchain.new_transaction("Bob", "Mike", '0.5 BTC')
blockchain.new_block(6789)


'''
This is a rudimentary version of a blockchain, without the proof, security, and verification
mechanisms. 
'''