# Brute-Force Password Cracker
**About:** A repository with brute force password crackers written in several different programming languages.

Languages available:
1. C++
2. C#
3. Python
4. Kotlin
5. Go
6. **New:** Vala

## About these programs
A brute force program attempts every possible solution when cracking a password.
These are not just useful for hacking but can be applicable in many programs. They 
are often inefficient and time consuming because they are so thorough.

Read more about brute force password crackers [here](https://en.wikipedia.org/wiki/Brute-force_attack).

The algorithms generally use recursion, where the function creates more instances of itself. There
is slight overhead here because if one function finishes, the others still run a few times
before realizing they should quit, but if you have a recommendation on how to do it without
recursion create an issue!

## Application
I have used brute-force techniques many times in my coding career. Here are some examples
where brute forcing could be used:
- Finding anagrams of a word and seeing which are in a dictionary
- Games where the computer needs to analyze the game board and rank the best places to play
- Testing the performance of a language (i.e. C# is faster than Python but slower than Vala).
- Benchmarking your CPU
- Running a function 10 million times and ranking the performance/output
- _etc._

## Implementation:
Implementation is easy enough. Each language contains a small `main` function and references the brute forcing
function, which you could just copy into your code.
