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
Here are the performance statistics that I found on my Intel i5-4460 @ 3.20GHz. Each program was tasked with cracking the password `zzzzzz`. These should give you a rough estimate of how fast the program is in each language. The Python version does not include statistics (such as duration or passwords / second) but those will be added soon. Kotlin had a few issues compiling with coroutines, so I'll get those statistics as soon as I can compile it 😂. (hint: if you're language-agnostic, use C++) Here's the results:

### C#:
Duration: 12 seconds

Passwords / second: 26,772,698

### C++:
Duration: 6.31 seconds

Passwords / second: 50,914,804

### Python:
Duration: > 5 minutes

Passwords / second: coming soon...

### Kotlin:
Statistics coming soon...

