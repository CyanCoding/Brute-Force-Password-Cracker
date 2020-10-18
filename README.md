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
Here are some statistics. All of these were run on the same Linux machine, so the runtime will obviously vary but it should give you a good idea of the speed differences between languages. Each program was tasked with finding the password `zzzzzz`. If you're language agnostic I highly recommend using C++.

### C#:
Duration: 12 seconds

Passwords / second: 26,772,698

### C++:
Duration: 6.31 seconds

Passwords / second: 50,914,804

### Python:
Duration: > 5 minutes

### Kotlin:
Statistics coming soon...

