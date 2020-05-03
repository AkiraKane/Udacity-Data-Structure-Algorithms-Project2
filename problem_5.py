import hashlib
import time

class Block:

    def __init__(self, data, previous_hash):
      self.timestamp = time.time()
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
    
    def calc_hash(self):
      sha = hashlib.sha256()
      sha.update(self.data.encode('utf-8'))
      return sha.hexdigest()

    def __repr__(self):
        return 'Block is: \n Data: {} \n Timestamp: {} \n Hash: {}'.format(self.data, self.timestamp, self.hash)


class Blockchain(object):
    def __init__(self):
        self.tail = None
    
    def append(self, data):

        if self.tail is None:
            self.tail = Block(data, None)
        
        else:
            self.tail = Block(data, self.tail)
    
    def size(self):
        current_position = self.tail
        size = 0

        while current_position is not None:
            current_position = current_position.previous_hash
            size += 1
        
        return size


######################################## Test ################################

blockchain = Blockchain()

print(blockchain.size())  # return 0

blockchain.append("udacity")
print(blockchain.size())  # return 1

blockchain.append("is")
blockchain.append("awesome")
blockchain.append("haha")
print(blockchain.size())  # return 4

blockchain_none = Blockchain()
blockchain_none.append("")     # append empty string
print(blockchain_none.size())  # return 1  
