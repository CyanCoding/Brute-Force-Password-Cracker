# Brute-Force Password Cracker
The brute-force password cracker is an application written in *C#*, *C++*, *Kotlin*, and *Python* (Java coming soon) that brute forces a password that you pass to the function. Read more about brute force password crackers [here](https://en.wikipedia.org/wiki/Brute-force_attack).

The general idea is that it checks every possible character combination repeatedly until it matches the provided string. **Note**: Built into the Kotlin version are koroutines that have it check multiple lengths of a string at a time for as many cores as the processor you're using has. You can disable this feature and just have it run one length at a time. I've found that using multiple cores can speed up the overall process as it makes it easier for it to guess longer lengths faster.

Example output with koroutines:
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

Example output without koroutines:
```
a
b
```
