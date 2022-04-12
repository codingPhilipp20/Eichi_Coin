from Crypto.PublicKey import ECC as ecc
from Crypto.Hash import SHA256
from Crypto.Signature import DSS


# Multiple Transactions are stored in one block.
# Those Transactions consist of a sender a recipient
# and an amount (of Eichi Coins)
class Transaction:

  # Constructor for said Transaction instances
  def __init__(self, sender, recipient, amount):
    self.sender = sender  # public, unique key of sender
    self.recipient = recipient  # public, unique key of recipient
    self.amount = amount  # amount of Eichi_Coins
    self.signature = ""  # signature, that will be provided later

  @staticmethod
  def create_transaction(sender, recipient, amount):
    return Transaction(sender, recipient, amount)

  # sender signs the transaction with its key pair (private and public key)
  # and attaches the signature to the Transaction instance
  @staticmethod
  def sign(self, keypair):
    if keypair.public_key() == self.sender:
      h = SHA256.new(
        (str(self.sender) + str(self.recipient) + str(self.amount)).encode(
          'utf-8'))
      signer = DSS.new(keypair, 'fips-186-3')
      self.signature = signer.sign(h)
    return True

  # method validates the chain:
  # checks if sender has the money, he is sending
  # verifiers if the signature is correct the senders public key (equals his adress)
  @staticmethod
  def isValid(self, chain):
    verifier = DSS.new(self.sender, 'fips-186-3')
    return self.sender is not None \
           and self.recipient is not None \
           and 0 < self.amount < chain.get_balance(chain,
                                                   self.sender) or chain.CREATE_REWARD_ADRESS == self.sender \
           and verifier.verify(SHA256.new(
      (str(self.sender) + str(self.recipient) + str(self.amount)).encode(
        'utf-8')), bytes(self.signature))
