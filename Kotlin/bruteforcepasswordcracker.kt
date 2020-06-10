import java.text.SimpleDateFormat
import java.util.*
import kotlinx.coroutines.*
import java.lang.ArithmeticException
import java.lang.Thread.sleep
import kotlin.system.measureNanoTime
import kotlin.system.measureTimeMillis

/*
 * Brute Force Password Cracker program.
 * Purpose: To brute force crack any password.
 *
 * Author: Camden Mac Leod aka CyanCoding.
 * File created on Mar 9, 2020.
 */

/*
 * Main brute force recursive function
 */
var stop: Boolean = false // Used when the functions need to stop to increase value
// exit is an array containing bool values for each length (1-8). When all possibilities for one length
// of a string has been made, the value becomes true. This is necessary for the koroutines.
var exit = arrayOf<Boolean>(false, false, false, false, false, false, false, false)
var tries: Long = 0
var checkEnd: String = ""

fun bruteForce(current: String, password: String, length: Int, chars: Array<Char>, threadID: Int) {
    // While not stopped and there's still possible values in this length
    if (!stop && !exit[threadID - 1]) {
        if (current.length == length) { // We're back up to full length
            tries++

            if (current == password) { // Password is a match! Break
                stop = true
            }

            checkEnd = ""

            // Gets the last value for that length. Example: zzz (for length = 3)
            for (i in 1..length) {
                checkEnd += chars[chars.size - 1]
            }

            // Breaks out of this length because all of the passwords have been guessed
            if (current == checkEnd) {
                val dateFormat = SimpleDateFormat("[HH:mm:ss:SSS]")
                val currentDate = dateFormat.format(Date())
                println("$currentDate Thread $threadID done...")
                exit[threadID - 1] = true
            }

        } else if (current.length < length) { // Not up to full length, append a character
            // Recursively create another password
            for (element in chars) {
                bruteForce(current + element, password, length, chars, threadID)
            }
        }
    }
}

/*
 * Main function
 */
fun main() {
    println("Brute Force Password Cracker program by CyanCoding.")

    // Get the current year and print it with the copyright
    var dateFormat = SimpleDateFormat("yyyy")
    val currentDate = dateFormat.format(Date())
    if (currentDate == "2020") {
        println("Copyright 2020 CyanCoding.")
    } else {
        println("Copyright 2020 - $currentDate CyanCoding.")
    }
    println("-----------------------------------------------")
    print("Please enter your password to crack > ")
    val password = readLine()!!

    val characters = arrayOf<Char>('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

    dateFormat = SimpleDateFormat("[HH:mm:ss:SSS]")
    val startTime = dateFormat.format(Date())

    // var length: Int = 1
    GlobalScope.launch {
        launch {
            bruteForce("", password, 1, characters, 1)
        }
        launch {
            bruteForce("", password, 2, characters, 2)
        }
        launch {
            bruteForce("", password, 3, characters, 3)
        }
        launch {
            bruteForce("", password, 4, characters, 4)
        }
        launch {
            bruteForce("", password, 5, characters, 5)
        }
        launch {
            bruteForce("", password, 6, characters, 6)
        }
        launch {
            bruteForce("", password, 7, characters, 7)
        }
        launch {
            bruteForce("", password, 8, characters, 8)
        }
    }
    
    // We want to wait for the threads to finish guessing the password before moving on
    while (!stop) {
        sleep(1)
    }

    val endTime = dateFormat.format(Date())

    println("\n\nCracked $password! Statistics:")
    println("Tries: ${"%,d".format(tries)}.")
    println("Start: $startTime")
    println("End: $endTime")
}