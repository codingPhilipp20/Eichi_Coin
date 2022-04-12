

import datetime as d
import hashlib as h

from Blockchain import Blockchain
from Transaction import Transaction


class Block:
  def __init__(self, index, timestamp, reward, data, prevhash):
    self.index = index  # number of existing blocks minus 1
    self.timestamp = timestamp  # time of creation
    self.data = data  # transaction data
    self.prevhash = prevhash  # hash of the previous block
    self.reward = reward  # reward for mining this block
    self.nonce = 0  # value that will be manipulated during mining process
    self.hash = self.hashblock(self)  # hash of this block

  # returns the hash value of this block if and sha256 encryption
  @staticmethod
  def hashblock(self):
    block_encryption = h.sha256()
    block_encryption.update((str(self.index) + str(self.timestamp) + str(self.data) + str(self.prevhash) + str(self.nonce)).encode('utf-8'))
    return block_encryption.hexdigest()

  # creates the initial block and gives the creator Coins
  @staticmethod
  def genesis_block(owner_public_key):
    initial_coin_release = [Transaction.create_transaction(Blockchain.CREATE_REWARD_ADRESS, owner_public_key, 1500000000)]
    return Block(0, d.datetime.now(), 15, initial_coin_release, "")

  # creates new block with the information of the last
  @staticmethod
  def new_block(lastblock, data):
    index = lastblock.index+1
    timestamp = d.datetime.now()
    reward = 5
    hashblock = lastblock.hashblock(lastblock)
    return Block(index, timestamp, reward, data, hashblock)

  # validates the Transactions of the Block
  @staticmethod
  def only_valid_transactions(self, chain):
    for transaction in self.data:
      if not transaction.isValid(chain):
        print("transaction's not valid")
        return False
    print("transaction be valid")
    return True

  # mines the block by altering the nuonce
  # and getting a hash code which starts with ($difficulty) zeros
  @staticmethod
  def mine(self, difficulty):
    string = ""
    for i in range(1, difficulty):
      string += "0"

    x = 0
    while not self.hash.startswith(string):
      x += 1
      self.nonce += 1
      self.hash = self.hashblock()
    print(str(x))

  @staticmethod
  def toString(self):
    string = str(self.index) + " the data: " + str(self.data) + " the timestamp: " + str(self.timestamp) + " crypto: " + str(self.hash)
    return string