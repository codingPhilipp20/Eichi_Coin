import Block as Block
from Transaction import Transaction
from Crypto.PublicKey import ECC

class Blockchain:


  MINT_KEY_PAIR = ECC.generate(curve='P-256')
  CREATE_REWARD_ADRESS = MINT_KEY_PAIR.public_key()

  my_key_pair = ECC.generate(curve='P-256')
  my_public_key = my_key_pair.public_key()

  def __init__(self, difficulty):
    self.blockchain = [Block.Block.genesis_block(self.my_public_key)] # list with one block (genesis block)
    self.prevblock = self.blockchain[0]
    self.difficulty = difficulty  # difficulty defines the amount of zeros that the hash has to start with
    self.transactions = []  # transaction that are yet to be stored in a block
    self.reward = 10 # amount of coins that a miner receives for one block

  @staticmethod
  def new_transaction(self, transaction):
    if transaction.isValid(transaction, self):
      self.transactions.append(transaction)
      return True
    print("Could not add Transaction, since invalid")
    return False

  @staticmethod
  def get_last_block(self):
    block = self.blockchain[len(self.blockchain) - 1]
    return block

  @staticmethod
  def add_new_block(self, block):
    lastBlock = self.get_last_block(self)
    block.prevhash = lastBlock.hashblock(lastBlock)
    block.hash = block.hashblock(block)
    block.mine(block, self.difficulty)
    self.blockchain.append(block)

  @staticmethod
  def validate_pair(self, a, b,):
    if a.index +1 != b.index:
      return False
    elif a.hashblock() != b.prevhash:
      return False
    elif a.timestamp > b.timestamp:
      return False
    elif not b.only_valid_transactions(self):
      return False
    return True

  # when a new user joins the network, he wants to make sure that the blockchain he received is legit.
  @staticmethod
  def validate_chain(self):
    for x in range(1, len(self.blockchain)):
      if not self.validate_pair(self.blockchain[x-1], self.blockchain[x]):
        return False
    return True

  # scans the entire blockchain to get the balance of one user
  @staticmethod
  def get_balance(self, adress):
    balance = 0
    for block in self.blockchain:
      for transaction in block.data:
        if transaction.sender == adress:
          balance -= transaction.amount
        if transaction.recipient == adress:
          balance += transaction.amount
    return balance

  # mines the open transactions, by adding them to the blockchain and verifying them.
  @staticmethod
  def mine_transactions(self, reward_recipient):
    mint_transaction = Transaction.create_transaction(self.CREATE_REWARD_ADRESS, reward_recipient, self.reward)
    mint_transaction.sign(mint_transaction, self.MINT_KEY_PAIR)
    self.transactions.append(mint_transaction)
    self.add_new_block(self, Block.Block.new_block(self.get_last_block(self), self.transactions))
    self.transactions = []



    