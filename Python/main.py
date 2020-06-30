# Imports
import itertools
import time


# Brute force function
def tryPassword(passwordSet, stringTypeSet):
    start = time.time()
    f = open("password_combination.txt", "w")  #It store all combinations ,It will easy be to analyse the pattern at the end
    chars = stringTypeSet
    attempts = 0
    for i in range(1, 9):
        for letter in itertools.product(chars, repeat=i):
            attempts += 1
            letter = ''.join(letter)
            f.write(letter)
            f.write("   ")
            if letter == passwordSet:
                end = time.time()
                distance = end - start
                f.close()
                return (attempts, distance)


password = input("Password >")
# Allowed characters
stringType = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_-+=[{]}|:;'\",<.>/?"
tries, timeAmount = tryPassword(password, stringType)
print("CyanCoding's BFPC cracked the password %s in %s tries and %s seconds!" % (password, tries, timeAmount))
