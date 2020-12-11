//
// Answers: 439, 584
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct {
    struct {
        union {
            int min;
            int pos_1;
        };
        union {
            int max;
            int pos_2;
        };
        char letter;
    } policy;
    char password[64];
} password_info;

typedef bool (*password_checker)(password_info *);

/* format: min-max l: password */
static void parse_password_info(password_info *ptr, char* str) {
    ptr->policy.min = atoi(str);
    str = strchr(str, '-') + 1;
    ptr->policy.max = atoi(str);
    str = strchr(str, ' ') + 1;
    ptr->policy.letter = *str;
    str = strchr(str, ' ') + 1;
    strncpy(ptr->password, str, sizeof(ptr->password));
}

static size_t parse_password_file(password_info* info, char* file) {
    FILE* nums = fopen(file, "r");
    if (nums == NULL)
        exit(1);

    char buf[64];
    size_t numbers_size = 0;

    while(fgets(buf, sizeof(buf), nums) != NULL)
        parse_password_info(&info[numbers_size++], buf);

    fclose(nums);
    return numbers_size;
}

static bool password_is_valid_part1(password_info *info) {
    int count = 0;
    for (size_t i = 0; i < strlen(info->password); i++)
        if (info->password[i] == info->policy.letter)
            count++;

    return count >= info->policy.min && count <= info->policy.max;
}

// 1-indexed positions!
static bool password_is_valid_part2(password_info *info) {
    bool pos_1_valid = info->policy.letter == info->password[info->policy.pos_1 - 1];
    bool pos_2_valid = info->policy.letter == info->password[info->policy.pos_2 - 1];

    return pos_1_valid ^ pos_2_valid;
}

static int calc_valid_passwords(password_info *info, size_t size, password_checker checker) {
    int valid_passwords = 0;
    for (size_t i = 0; i < size; i++)
        if (checker(&info[i]))
            valid_passwords++;

    return valid_passwords;
}

void do_part(char *part_name, bool (*checker)(password_info *), password_info *info, size_t size) {
    printf("%s valid passwords: %d\n", part_name,
           calc_valid_passwords(info, size, checker));
}

int main() {
    password_info example_info[10];
    size_t example_info_size = parse_password_file(example_info, "../day2_example.txt");

    password_info actual_info[1024];
    size_t actual_info_size = parse_password_file(actual_info, "../day2.txt");

    do_part("P1 Example", password_is_valid_part1, example_info, example_info_size);
    do_part("P1", password_is_valid_part1, actual_info, actual_info_size);
    do_part("P2 Example", password_is_valid_part2, example_info, example_info_size);
    do_part("P2", password_is_valid_part2, actual_info, actual_info_size);

    return 0;
}