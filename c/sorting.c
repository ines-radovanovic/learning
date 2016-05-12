// Task 1: Add include required to make this code compile

/**
 * To compile: 
 * gcc sorting.c -o sorting
 *
 * To run:
 * ./sorting array
 */

/**
 * Method sorts an array in place. Pick the best sorting algorithm for the task and explain
 * in the comments why it's the best.
 *
 * See https://en.wikipedia.org/wiki/Sorting_algorithm for details on sorting algorithms..
 *
 */
void sort(char* arrayInput) {
	// Task 2: Fill in the code here
}


int main( int argc, char** argv) {
	printf("Argument Count: %d\n", argc);
	
	if(argc < 2) {
		printf("Error: You must supply a sample array!\n");
		return 1;
	}
	
	// printing the contents of the array provided
	printf("Array Supplied: %s\n", argv[1]);
	
	// sort the array provided
	sort(argv[1]);
	
	// Task 3: Print the sorted array
	
	return 0;
}
