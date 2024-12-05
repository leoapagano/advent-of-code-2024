#include <regex.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_CHAR_SIZE 16

void die(char* s) {
	fprintf(stderr, "ERROR: %s\n", s);
	exit(EXIT_FAILURE);
}

int main(void) {
	// Read input file, save it to text string
	FILE* file;
	file = fopen("input.txt", "r");
	if (file == NULL) {
        die("Failed to open input.txt");
    }

	// Prepare file descriptor for reading
	fseek(file, 0, SEEK_END);
    long size = ftell(file);
    fseek(file, 0, SEEK_SET);

	// Initialize buffer
    char* text = malloc(size + 1);
    if (text == NULL) {
		die("Failed to malloc() string buffer");
	}

	// Write file to string and close file
    fread(text, 1, size, file);
    text[size] = '\0';
	fclose(file);

	// Initialize text "cursor"
    const char* cursor = text;

	// Initialize regex
	regex_t regex;
    int ret = regcomp(&regex, "mul\\([0-9]+,[0-9]+\\)", REG_EXTENDED);
    if (ret) {
        die("Failed to compile regex");
    }

	// Prepare regex match buffer and string buffers
	regmatch_t matches[1];
	char first_buf[MAX_CHAR_SIZE];
	char second_buf[MAX_CHAR_SIZE];
	int first_idx, second_idx, state;
	int sum = 0;

	// Parse each mul(x,y) statement
	while ((ret = regexec(&regex, cursor, 1, matches, 0)) == 0) {
		// Reset first and second writing space
		memset(first_buf, 0, sizeof(first_buf));
		memset(second_buf, 0, sizeof(second_buf));
		first_idx = 0;
		second_idx = 0;
		// state 0 is "neutral", 1 is "write to first", 2 is "write to second"
		state = 0; 
		
		// Iterate through mul() statement and add each number to the correct buffer
        for (int i = matches[0].rm_so; i < matches[0].rm_eo; i++) {
			switch (cursor[i]) {
				case '(':
					state = 1;
					break;
				case ',':
					state = 2;
					break;
				case ')':
					state = 0;
					break;
				default:
					if (state == 1) {
						first_buf[first_idx] = cursor[i];
						first_idx += 1;
					} else if (state == 2) {
						second_buf[second_idx] = cursor[i];
						second_idx += 1;
					}
			}
        }

		// Increment sum
		sum += atoi(first_buf) * atoi(second_buf);

        // Search for next regex match
        cursor += matches[0].rm_eo;
    }

	// End of matches - error handling
    if (ret != REG_NOMATCH) {
        char regerror_buf[100];
        char err_buf[120];
        regerror(ret, &regex, regerror_buf, sizeof(regerror_buf));
        snprintf(err_buf, 100, "Regex match failed: %s", regerror_buf);
		die(err_buf);
    }

	// Close up shop
	printf("SUM: %d\n", sum);
	regfree(&regex);
	free(text);
    return 0;
}