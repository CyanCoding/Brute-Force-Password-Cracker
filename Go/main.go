// Part of the "Brute Force Password Cracker" project at
// https://github.com/CyanCoding/Brute-Force-Password-Cracker
// Author: Camden Mac Leod, aka CyanCoding
// File created on Aug 11, 2021

package main

import (
	"fmt"
	"time"

	"github.com/dustin/go-humanize"
)

var passwordToGuess string = "hello" // The password we are guessing
var done bool = false                // Whether we're finished or not
var tries float32 = 0                // The amount of attempts we've made
var attemptingLength = 1             // The length we're guessing

var availableCharacters = []rune{'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
	'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
	'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B',
	'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
	'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}

func bruteForce(length int, pw string) {
	if length == 0 && !done {
		if pw == passwordToGuess {
			done = true
		}

		return
	} else if !done {
		for i := 0; i < len(availableCharacters); i++ {
			tries++

			bruteForce(length-1, pw+string(availableCharacters[i]))
		}
	}
}

func main() {
	fmt.Println("Welcome to the Go Brute Force Password Cracker!")
	fmt.Println("This program was created by CyanCoding.")
	fmt.Println("-----------------------------------------------")
	fmt.Print("Please enter your password > ")

	fmt.Scanln(&passwordToGuess) // Read into password

	startTime := time.Now()
	for !done {
		bruteForce(attemptingLength, "")
		attemptingLength++
		fmt.Println(attemptingLength)
	}

	endTime := time.Since(startTime)
	fmt.Println("Finished in", humanize.Comma(int64(tries)), "tries!")
	fmt.Println("That took", humanize.FormatFloat("###,###.##", endTime.Seconds()), "seconds!")

	triesPerSec := tries / float32(endTime.Seconds())
	fmt.Println("That's", humanize.Commaf(float64(triesPerSec)), "tries per second!")
}
