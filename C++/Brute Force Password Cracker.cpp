#include <iostream>
#include <time.h>
#include <iomanip>
#include <Windows.h>
#include <thread>

using namespace std;

bool stop = false;
int amount = 0;
string password;

const char alphabet[26] = {
	'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
};


void inline generate(int length, string current) {
	if (length == 0 && stop == false) { // If the password is at the 0th place, close off
		amount++;
		if (current == password) {
			stop = true;
		}
		return;
	}

    // While cracking password, recursively find next password
	if (stop == false) {
		for (int i = 0; i < 26; i++) {
			string appended = current + alphabet[i];
			generate(length - 1, appended);
		}
	}
}

int main() {
	cout << "Welcome to CyanCoding's 2nd Brute Force Password Cracker!" << endl << endl;

	cout << "What do you want your password to be? > ";
	cin >> password;

	cout << endl << "Attempting to crack " << password << endl << endl;

	clock_t start = clock();

	while (stop == false) {
		static unsigned int stringLength = 1;
        generate(stringLength, "");
		stringLength++;
	}

	cout << "CyanCoding's C++ BFPC cracked the password " << password << " in " << amount << " attempts and " << setprecision(2) << fixed << (float)(clock() - start) / CLOCKS_PER_SEC << " seconds." << endl << endl << "That's about " << setprecision(0) << amount / ((float)(clock() - start) / CLOCKS_PER_SEC) << " passwords per second!";

	return 0;
}