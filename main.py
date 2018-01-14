# Imports
import itertools
import time
from termcolor import colored
import replit
import math

# Brute force function
def tryPassword(passwordSet, stringTypeSet):
    start = time.time()
    chars = stringTypeSet
    attempts = 0
    for i in range(1, 9):
        for letter in itertools.product(chars, repeat=i):
            attempts += 1
            millions = 0
            letter = ''.join(letter)
            if attempts % 5000000 == 0:
                millions = attempts / 1000000
                millions = math.ceil(millions)
                print(colored("%s million passwords guessed so far..." % (millions), "cyan"))
            if letter == passwordSet:
                end = time.time()
                distance = end - start
                return (attempts, distance)

                

# Wait function
def wait(amount):
    time.sleep(amount)
    print()

# Program
stringType = ""
replit.clear()
print(colored("Welcome to the Brute Force Password Cracker!", "magenta"))
wait(3)
print(colored("Brute Force Password Cracker (BFPC) created by", "magenta"), colored("CyanCoding", "cyan"))
wait(4)
print(colored("CyanCoding's BFPC was created as a better version of the PIN Guesser which just fished around for numbers until it found your PIN", "magenta"))
wait(8)
print(colored("By the way, in my program, you can customize what letters the program is looking for in your password (lowercase, numbers, symbols, all, etc.). It is highly suggested.", "magenta"))
wait(6)
print(colored("The program has priorities so numbers are the highest priority with lowercase letters, then uppercase letters, and lastly symbols.", "magenta"))
wait(6)
print(colored("To get a grasp of how long Brute Force Password Cracking takes, with all customizations on (searching through 94 characters), it took the program roughly 0.7 seconds and 1.7 million tries to guess the password 2784.", "magenta"))
wait(12)
print(colored("This program typically runs faster with faster internet, and my max was about 2,074,712 passwords per second!", "magenta"))
wait(8)
doneBefore = input(colored("Have you ever used this program before?", "yellow"))
if doneBefore == "no" or doneBefore == "nope" or doneBefore == "definitely not" or doneBefore == "is 9 + 10 = 21?" or doneBefore == "nuh uh":
    wait(1)
    print(colored("Great! Welcome to CyanCoding's Brute Force Password Cracker!", "magenta"))
    wait(3.4)
    learnMore = input(colored("Would you like to know what a BFPC is?", "yellow"))
    time.sleep(2)
    if learnMore == "yes" or learnMore == "yea" or learnMore == "yeah" or learnMore == "ya" or learnMore == "yup" or learnMore == "yuppers" or learnMore == "sure" or learnMore == "okay" or learnMore == "ok":
        replit.clear()
        print(colored("Let's start from the beginning.", "magenta"))
        wait(2)
        print(colored("A Brute Force program is a program that will guess every possible password until it finds the password.", "magenta"))
        wait(4)
        print(colored("However, if you can imagine, it is extremely inefficient for most tasks.", "magenta"))
        wait(4)
        print(colored("Cracking passwords can take anywhere from less than a second to hundreds of years.", "magenta"))
        wait(5)
        print(colored("Fortunately though, it means that it can eventually crack any password.", "magenta"))
        wait(5)
        print(colored("This also means that the pin on a phone (even though it would likely take several thousand tries) could be cracked in under a minute.", "magenta"))
        wait(7)
        print(colored("And that is why there is a limit to how many times a password can be enetered on most products these days.", "magenta"))
        wait(7)
        input(colored("Press the enter key when you have finished reading.", "yellow"))
        replit.clear()
    
    wait(2)
    print(colored("This program is the real deal and it takes a long time to crack some passwords.", "magenta"))
    wait(4)
    print(colored("You can have it so that it only looks for lowercase letters, uppercase letters, numbers, symbols, or all of the above to minimalize the time.", "magenta"))
    wait(7)
    print(colored("Also, this program only uses the common symbols that you would use on your keyboard. Don't use lame symbols like copyright or something unless you want the program to never find your password.", "magenta"))
    wait(9)
    print(colored("Note for when entering passwords: this program uses no sleep timers when searching for your passwords, but long and/or complicated passwords can actually take several minutes to several hours.", "red"))
    time.sleep(12)
print()
print(colored("Enjoy!", "magenta"))
print(colored("___________________________________________________________________________", "magenta"))
print()
input(colored("Press the enter key when you are ready to start.", "yellow"))
wait(1)
password = input(colored("Please enter your password >", "yellow"))
wait(1)
customize = input(colored("Would you like to customize the program to make it take shorter/longer to find your password? (suggested)", "yellow")).lower()
wait(1)
if customize == "yes" or customize == "yea" or customize == "yeah" or customize == "sure" or customize == "okay" or customize == "ok" or customize == "well duh it'd take all week if i didn't":
    replit.clear()
    print(colored("Password customizations", "green"))
    wait(2)
    usingCaps = False
    usingNums = False
    usingSyms = False
    usingLower = False
    setLower = False
    setCaps = False
    setNums = False
    setSyms = False
    if "A" in password or "B" in password or "C" in password or "D" in password or "E" in password or "F" in password or "G" in password or "H" in password or "I" in password or "J" in password or "K" in password or "L" in password or "M" in password or "N" in password or "O" in password or "P" in password or "Q" in password or "R" in password or "S" in password or "T" in password or "U" in password or "V" in password or "W" in password or "X" in password or "Y" in password or "Z" in password:
        usingCaps = True
    if "a" in password or "b" in password or "c" in password or "d" in password or "e" in password or "f" in password or "g" in password or "h" in password or "i" in password or "j" in password or "k" in password or "l" in password or "m" in password or "n" in password or "o" in password or "p" in password or "q" in password or "r" in password or "s" in password or "t" in password or "u" in password or "v" in password or "w" in password or "x" in password or "y" in password or "z" in password:
        usingLower = True
    if "1" in password or "2" in password or "3" in password or "4" in password or "5" in password or "6" in password or "7" in password or "8" in password or "9" in password or "0" in password:
        usingNums = True
    if "`" in password:
        usingSyms = True
    if "~" in password:
        usingSyms = True
    if "!" in password:
        usingSyms = True
    if "@" in password:
        usingSyms = True
    if "#" in password:
        usingSyms = True
    if "$" in password:
        usingSyms = True
    if "%" in password:
        usingSyms = True
    if "^" in password:
        usingSyms = True
    if "&" in password:
        usingSyms = True
    if "*" in password:
        usingSyms = True
    if "(" in password:
        usingSyms = True
    if ")" in password:
        usingSyms = True
    if "_" in password:
        usingSyms = True
    if "-" in password:
        usingSyms = True
    if "+" in password:
        usingSyms = True
    if "=" in password:
        usingSyms = True
    if "{" in password:
        usingSyms = True
    if "[" in password:
        usingSyms = True
    if "}" in password:
        usingSyms = True
    if "}" in password:
        usingSyms = True
    if "\\" in password:
        usingSyms = True
    if "|" in password:
        usingSyms = True
    if ";" in password:
        usingSyms = True
    if ":" in password:
        usingSyms = True
    if "'" in password:
        usingSyms = True
    if "\"" in password:
        usingSyms = True
    if "<" in password:
        usingSyms = True
    if "." in password:
        usingSyms = True
    if ">" in password:
        usingSyms = True
    if "," in password:
        usingSyms = True
    if "/" in password:
        usingSyms = True
    if "?" in password:
        usingSyms = True
    wait(3)
    print(colored("Please type in the number of the characters you would like in your password", "magenta"))
    print()
    wait(2)
    print(colored("1. Lowercase letters", "green"))
    time.sleep(1)
    print(colored("2. Uppercase letters", "green"))
    time.sleep(1)
    print(colored("3. Numbers", "green"))
    time.sleep(1)
    print(colored("4. Symbols", "green"))
    time.sleep(1)
    print(colored("5. All of the above", "green"))
    time.sleep(1)
    print(colored("6. Custom (not suggested)", "green"))
    wait(3)
    selection = int(input(colored("Please enter the number", "yellow")))
    if selection == 1:
        stringType += "abcdefghijklmnopqrstuvwxyz"
        setLower = True
    elif selection == 2:
        stringType += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        setCaps = True
    elif selection == 3:
        stringType += "1234567890"
        setNums = True
    elif selection == 4:
        stringType += "`~!@#$%^&*()_+-=[]{};:'\"|,.<>/?\""
        setSyms = True
    elif selection == 5:
        stringType += "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_+-=[]{};:'\"|,.<>/?\\"
        setLower = True
        setCaps = True
        setNums = True
        setSyms = True
    elif selection == 6:
        print()
        stringType = input(colored("Please enter all the characters that you want your program to look for", "yellow"))
    
    if usingLower == True and setLower == False:
        print()
        print(colored("Your password contains lowercase characters, but the program isn't set to look for them.", "red"))
        wait(4)
        print(colored("This means that the program will never find your password", "red"))
        wait(3)
        useLower = input(colored("Turn on lowercase characters?", "yellow")).lower()
        if useLower == "yes" or useLower == "yea" or useLower == "yeah" or useLower == "sure" or useLower == "ok" or useLower == "okay":
            stringType += "abcdefghijklmnopqrstuvwxyz"
            setLower = True
            print()
            print(colored("Using lowercase letters.", "magenta"))
            wait(1)
    if usingCaps == True and setCaps == False:
        print()
        print(colored("Your password contains uppercase characters, but the program isn't set to look for them.", "red"))
        wait(4)
        print(colored("This means that the program will never find your password", "red"))
        wait(3)
        useCaps = input(colored("Turn on uppercase characters?", "yellow")).lower()
        if useCaps == "yes" or useCaps == "yea" or useCaps == "yeah" or useCaps == "sure" or useCaps == "ok" or useCaps == "okay":
            stringType += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            setCaps = True
            print()
            print(colored("Using uppercase letters.", "magenta"))
            wait(1)
    if usingNums == True and setNums == False:
        print()
        print(colored("Your password contains numbers, but the program isn't set to look for them.", "red"))
        wait(4)
        print(colored("This means that the program will never find your password", "red"))
        wait(3)
        useNums = input(colored("Turn on numbers?", "yellow")).lower()
        if useNums == "yes" or useNums == "yea" or useNums == "yeah" or useNums == "sure" or useNums == "ok" or useNums == "okay":
            stringType += "1234567890"
            setNums = True
            print()
            print(colored("Using numbers.", "magenta"))
            wait(1)
    if usingSyms == True and setSyms == False:
        print()
        print(colored("Your password contains symbols, but the program isn't set to look for them.", "red"))
        wait(4)
        print(colored("This means that the program will never find your password", "red"))
        wait(3)
        useSyms = input(colored("Turn on symbols?", "yellow")).lower()
        if useSyms == "yes" or useSyms == "yea" or useSyms == "yeah" or useSyms == "sure" or useSyms == "ok" or useSyms == "okay":
            stringType += "`~!@#$%^&*()_+-=[]{};:'\"|,.<>/?\""
            setSyms = True
            print()
            print(colored("Using symbols.", "magenta"))
            wait(1)

else:
    stringType += "1234567890"
    stringType += "abcdefghijklmnopqrstuvwxyz"
    stringType += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    stringType += "`~!@#$%^&*()_+-=[]{};:'\"|,.<>/?\""
    
print()
input(colored("Press the enter key when ready to begin cracking your password with CyanCoding's BFPC", "yellow"))
time.sleep(1)
replit.clear()
time.sleep(2)
print(colored("Attempting to crack password via CyanCoding's BFPC...", "magenta"))
wait(3)
print(colored("This could be a while. Feel free to leave this page open while you use the computer.", "magenta"))
wait(2)
tries, timeAmount = tryPassword(password, stringType)
timeAmount1 = math.ceil(timeAmount)
if timeAmount1 == 1:
    plural = "second"
else:
    plural = "seconds"
print(colored("CyanCoding's BFPC cracked the password %s in %s tries and %s %s!" % (password, tries, timeAmount1, plural), "cyan"))
wait(2)
tries = tries / timeAmount
tries = math.ceil(tries)
print(colored("That's approximately %s guessed passwords per second!" % (tries), "cyan"))