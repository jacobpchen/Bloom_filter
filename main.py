from bloomfilter import BloomFilter
# import math
# Number of items to add in the bloom filter
n = 5000
# Desired false positivity rate
p = .001

bloomf = BloomFilter(n,p)
print("Size of bit array:{}".format(bloomf.size))
print("Size of the number of items in the bloom filter (m): ", n)
print("False positive Probability:{}".format(bloomf.fp))
print("Number of hash functions:{}".format(bloomf.hash_count))

f = open("weak_passwords.txt", "r")
while True:
    line = f.readline().strip()
    bloomf.add(line)
    if line == '':
        break

# Check if the item is in the bf
while (True):
    password_check = str(input("Please change your password: \n"))
    if bloomf.check(password_check):
        print("The password you have entered is weak. Please choose another password")
    else:
        print("Password successfully changed!")
        break