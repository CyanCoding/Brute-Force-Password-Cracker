// Part of the "Brute Force Password Cracker" project at
// https://github.com/CyanCoding/Brute-Force-Password-Cracker
// Author: Camden Mac Leod, aka CyanCoding
// File created on Aug 11, 2021

package main

import "fmt"

func main() {
	fmt.Println("Welcome to the Go Brute Force Password Cracker!")
	fmt.Println("This program was created by CyanCoding.")
	fmt.Println("-----------------------------------------------")
	fmt.Print("Please enter your password > ")

	var password = ""
	fmt.Scanln(&password)

}
