#include <stdio.h>
/**
 * To compile: 
 * gcc findFirstNonLetter.c -o findFirstNonLetter
 *
 * To run:
 * ./findFirstNonLetter string
 */

/**
 * Method returns the index of the first non-letter character in an array.
 * For example, for the array 'adf5ds4' it returns 3.
 *
 * Returns:
 * * index of first non-letter if found
 * * -1 if not found
 */
int findFirstNonLetter(char** arrayInput) {
	// Task 1: Fill in the code here
	
	return -1;
}


int main( int argc, char** argv) {
	printf("Argument Count: %d\n", argc);
	
	if(argc < 2) {
		printf("Error: You must supply a sample array!\n");
		return 1;
	}
	
	// printing the contents of the array provided
	printf("Array Supplied: %s\n", argv[1]);

	// find the first non-letter in the provided input
	int indexOfFirstNonLetter = findFirstNonLetter(argv);
	
	// Task 2: Print the index found and the actual non-letter character at that index
	

	return 0;
}
