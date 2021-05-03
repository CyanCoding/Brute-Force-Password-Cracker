# Brute-Force Password Cracker
The brute-force password cracker is an application written in *C#*, *C++*, *Kotlin*, and *Python* that brute forces a password that you pass to the function. Read more about brute force password crackers [here](https://en.wikipedia.org/wiki/Brute-force_attack).

The general idea is that it checks every possible character combination repeatedly until it matches the provided string. **Note**: Built into the Kotlin version are coroutines that have it check multiple lengths of a string at a time for as many cores as the processor you're using has. You can disable this feature and just have it run one length at a time. I've found that using multiple cores can speed up the overall process as it makes it easier for it to guess longer lengths faster.

Example output with coroutines:
```
a
aa
aaa
aaaa
b
ab
aab
aaab
```

Example output without coroutines:
```
a
b
```

## Implementation:
If you look at the code for each language, implementation should be fairly easy enough. You can pretty much copy and paste the code, make slight modifications to fit your project, and then run. 

Make sure the "dictionary" matches your needs. For example, the Python program will check for all English characters (capital and lowercase), symbols, and numbers while the Kotlin one only checks lowercase English characters. Usually the "dictionary" is a string that the program iterates through or a `char[] array`. If you don't need to search for every character (maybe you just need to search numbers), make sure to remove unecessary ones because that will really speed up your performance.

## Performance:
I don't have exact speed details on Python and Kotlin, but I do know the order in which they rank with C++ obliterating all competition.
Here is the breakdown by performance:

1. C++
2. C#/Kotlin
3. Python

On my machine (Ryzen 7 3700U 4 cores) the C++ program ran at almost 90 million passwords per second, which is phenomenal performance compared to an average of 10-30 million on C#, Kotlin, and Python. I am continuing to optimize the C++ program so expect further speed improvements.

### Notes:
Here's a few things I've learned over the course of a few years testing with these programs.

1. Whenever you modify the code, it's a good idea to have the code output what it's bruteforcing. A simple `Console.WriteLine(current)` should suffice.
2. Reduce console output as much as possible. If you are bruteforcing and outputting, your speed has just dropped by 90% and is being limited by the terminal and not your computer's raw power.
3. Sometimes if you multi-thread, you effectively get the same results but with half the performance and twice the CPU usage. Trust me, I worked on some of these programs for several months and found no benefit from multithreading (with the exception of the Kotlin one, which uses Coroutines to bruteforce different password lenghts at the same time).
4. If you want as much freaking speed as possible, run the program right after booting up your computer while it's plugged in and on max performance settings. For fun, see how opening other apps and unplugging your laptop affect performance!
