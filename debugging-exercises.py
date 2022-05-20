import pdb
pdb.set_trace()
def is_prime(x):
    if x <= 2:
        return False
    else:
        for n in range(2, x):  # range creates start - stop-1
            if x % n == 0:
                return False
        return True

x = 1
while x != 0:
    x = int(input("Type a number"))
    print("Testing if " + str(x) + " is prime: " + str(is_prime(x)))