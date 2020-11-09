from bloomfilter import BloomFilter
# import math
# Number of items to add in the bloom filter
n = 5000
# Desired false positivity rate
p = .001

bloomf = BloomFilter(n,p)
print("Size of bit array:{}".format(bloomf.size))
print("Size of the number of items in the bloom filter (m): ", n)
print("False positive Probability:{:.6%}".format(bloomf.fp))
print("Number of hash functions:{}".format(bloomf.hash_count))

# Create a set of the weak passwords to test false positivity rate
weak_passwords = set()

f = open("weak_passwords_5000.txt", "r")
for i in range(n):
    line = f.readline().strip()
    weak_passwords.add(line)
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

counter = 0

f = open("weak_passwords_100000.txt", "r")
for i in range(0, 8000):
    line = f.readline().strip()
    print(i)
    if bloomf.check(line):
        # print(line, " is a weak password")
        if line not in weak_passwords:
            print("False positive!!")
            print(line)
            counter += 1

print(counter)