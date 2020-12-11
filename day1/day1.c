// ans is: 800139
/*
 * Notes:
 * - parsing is unsafe because we don't do array bounds check
 * - again, sizes are static (could be dynamic with more work...)
 * - core computation loop is probably very efficient
 */
#include <stdio.h>
#include <stdlib.h>

static size_t parse_number_file(int* numbers) {
    FILE* nums = fopen("../day1.txt", "r");
    if (nums == NULL)
        exit(1);

    char buf[64];
    size_t numbers_size = 0;

    while(fgets(buf, sizeof(buf), nums) != NULL)
        numbers[numbers_size++] = atoi(buf);

    fclose(nums);
    return numbers_size;
}

void part1(const int *numbers, size_t numbers_size) {
    for (unsigned int i = 0; i < numbers_size; i++)
		for (unsigned int j = 0; j < numbers_size; j++)
		    if (numbers[i] + numbers[j] == 2020) {
                printf("Found it: %d\n", numbers[i] * numbers[j]);
                return;
            }
}

void part2(const int *numbers, size_t numbers_size) {
    for (unsigned int i = 0; i < numbers_size; i++)
        for (unsigned int j = 0; j < numbers_size; j++)
            for (unsigned int k = 0; k < numbers_size; k++)
                if (numbers[i] + numbers[j] + numbers[k] == 2020) {
                    printf("Found it: %d\n", numbers[i] * numbers[j] * numbers[k]);
                    return;
                }
}

int main() {
    int numbers[1024];
    size_t numbers_size = parse_password_file(numbers);

    part1(numbers, numbers_size);
    part2(numbers, numbers_size);

    return 0;
}
