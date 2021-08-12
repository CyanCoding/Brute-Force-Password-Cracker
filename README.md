# Brute-Force Password Cracker
Languages available:
1. *C++*
2. *C#*
3. *Python*
4. *Kotlin*
5. **NEW (beta):** *Go*

## About these programs
A brute force program attempts every possible solution when cracking a password.
These are not just useful for hacking but can be applicable in many programs. They 
are often inefficient and time consuming because they are so thorough.

Read more about brute force password crackers [here](https://en.wikipedia.org/wiki/Brute-force_attack).

## Implementation:
If you look at the code for each language, implementation should be fairly easy enough.
You can pretty much copy and paste the function, make slight modifications to fit your project, and then run. 

## Performance:
In general, the lower-level programming language you use the faster performance you can expect.
*An exception is the Go language, which generally has speeds that parallel C++, yet in my initial
testing is considerably slower in brute forcing.*

The best way to measure performance is in passwords guessed per second. It's the computer's
ability to generate strings and match them with the password to guess.
The most powerful computers in the world can reach speeds of 1 billion passwords / second.

These programs are not optimized enough for that kind of speed, but with a fast PC you can
achieve 100 million / sec running the C++ program.

## Project future
- [ ] Find ways to make the program faster besides just reducing slow functions.
- [ ] Use multiple threads for faster performance.
- [ ] Utilize RAM and a cache for quickly reading passwords without having to generate new ones.

I've already tried all of these, but they haven't made a significant impact on speed so I'll
keep optimizing and coming up with new methods as time goes on.
