# Python 3 program to build Bloom Filter
# Install bitarray 3rd party module first
# pip install bitarray

import math
from math import *
import hashlib
from bitarray import bitarray

class BloomFilter(object):
    '''
    Class for Bloom filter, using SHA1 hash function
    '''

    def __init__(self, items_count, fp_prob):
        # Size of bit array to use 2^16
        self.size = 65536

        # Number of items to add to the bloom filter
        self.items_count = items_count

        # False Positive probability
        self.fp_prob = fp_prob

        # Size of bit array to use
        # self.size = self.get_size(items_count, fp_prob)

        # number of hash functions to use
        self.hash_count = self.get_hash_count(self.size, self.items_count)

        # Bit array of given size
        self.bit_array = bitarray(self.size)

        # False Positivity rate
        #self.fp_prob = self.get_false_positivity(self.size, items_count, self.hash_count)
        #print(self.fp_prob)

        # initialize all bits as 0
        self.bit_array.setall(0)

        # Calculate p
        self.fp = pow(1-exp(-self.hash_count / (self.size / self.items_count)), self.hash_count)
        print(self.fp)

    @classmethod
    def get_size(self, n, p):
        '''
        Return the size of bit array(m) to used using
        following formula
        m = -(n * lg(p)) / (lg(2)^2)
        n : int
            number of items expected to be stored in filter
        p : float
            False Positive probability in decimal
        '''
        m = -(n * math.log(p)) / (math.log(2) ** 2)
        return int(m)

    @classmethod
    def get_hash_count(self, m, n):
        '''
        Return the hash function(k) to be used using
        following formula
        k = (m/n) * lg(2)

        m : int
            size of bit array
        n : int
            number of items expected to be stored in filter
        '''
        k = (m / n) * math.log(2)
        return int(k)

    def add(self, item):
        '''
        Add an item in the filter
        '''
        # SHA-1
        # Encrypt the item using SHA1
        result = hashlib.sha1(item.encode())

        # Convert the result to a hexadecimal
        # print("The hexadecimal equilvalent of SHA1 is:")
        digest = result.hexdigest()
        print(digest)

        #  split the digest into 10 - 4 hexadecimal digits
        n = 4
        digests = [digest[i:i+n] for i in range(0, len(digest), n)]
        print(digests)

        # Convert to the 4 hexadecimal digit to an integer between 0 - 65535
        for i in range(self.hash_count):
            bit = int(digests[i], 16)
            print(str(bit) + ' ', end='')
            # bit = bit % self.size
            self.bit_array[bit] = True

    def check(self, item):
        '''
        Check for existence of an item in the filter
        '''
        result = hashlib.sha1(item.encode())
        digest = result.hexdigest()
        n = 4
        digests = [digest[i:i + n] for i in range(0, len(digest), n)]

        #
        for i in range(len(digests)):
            bit = int(digests[i], 16)
            if self.bit_array[bit] == False:
                return False

        return True

