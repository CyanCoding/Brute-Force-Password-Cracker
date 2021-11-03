/* main.vala
 *
 * Copyright 2021 Camden Mac Leod
 *
 * Permission is hereby granted, free of charge, to any person obtaining
 * a copy of this software and associated documentation files (the
 * "Software"), to deal in the Software without restriction, including
 * without limitation the rights to use, copy, modify, merge, publish,
 * distribute, sublicense, and/or sell copies of the Software, and to
 * permit persons to whom the Software is furnished to do so, subject to
 * the following conditions:
 *
 * The above copyright notice and this permission notice shall be
 * included in all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 * NONINFRINGEMENT. IN NO EVENT SHALL THE X CONSORTIUM BE LIABLE FOR ANY
 * CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
 * TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
 * SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 *
 * Except as contained in this notice, the name(s) of the above copyright
 * holders shall not be used in advertising or otherwise to promote the sale,
 * use or other dealings in this Software without prior written
 * authorization.
 */

// This is the list we bruteforce
private const string[] AVAILABLE_LETTERS = {
    "a", "b", "c", "d", "e", "f", "g", "h",
	"i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
	"x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B",
	"C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
	"R", "S", "T", "U", "V", "W", "X", "Y", "Z"
};

private bool done = false; 	        // This is true when we match the password
private int attemptingLength = 1; 	// The length we're guessing
private int64 tries = 0;	        // The amount of tries we've made

/*
 * The meat of our program that generates passwords
 */
private static void bruteForce(int length, string pw, string password) {
	//print(pw + "\n");
    if (length == 0 && !done) {
    	if (pw == password) {
    		done = true;
    	}
    }
    else if (!done) {
    	for (int i = 0; i < AVAILABLE_LETTERS.length; i++) {
    		tries++;
    		bruteForce(length - 1, pw + AVAILABLE_LETTERS[i], password);
    	}
    }
}

/*
 * The main function to run
 */
int main (string[] args) {
    print("Welcome to the Vala Brute Force Password Cracker!\n");
    print("This program was created by CyanCoding.\n");
    print("-------------------------------------------------\n");
    print("Please enter your password > ");
    string input = stdin.read_line();
    
    // Milliseconds start time
    int64 startTime = get_real_time();
    
    while (!done) {
    	bruteForce(attemptingLength, "", input);
    	attemptingLength++;
    }
    
    int64 endTime = get_real_time();
    int timeDiff = (int.parse(endTime.to_string()) - int.parse(startTime.to_string())) / 1000000;
    
    print("Finished in " + tries.to_string() + " tries!\n");
    print("That took " + timeDiff.to_string() + " seconds!\n");
    
    int triesPerSec = int.parse(tries.to_string()) / timeDiff;
    print("That's " + triesPerSec.to_string() + " tries per second\n");
    
    return 0;
}
