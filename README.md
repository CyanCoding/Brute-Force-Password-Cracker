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

## Performance:
I don't have exact speed details on Python and Kotlin, but I do know the order in which they rank with C++ obliterating all competition.
Here is the breakdown by performance:

Slowest: Python
3. Kotlin
2. C#
Fastest: C++

On my machine (Ryzen 7 3700U 4 cores) the C++ program ran at almost 80 million passwords per second, which is phenomenal performance compared to an average of 10-30 million on C#, Kotlin, and Python. I am continuing to optimize the C++ program so expect further speed improvements.
