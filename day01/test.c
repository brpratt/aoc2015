#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

#include "day01.h"

#define RUN_TEST(name) \
do { \
    if (!name()) { \
        printf(#name " failed\n"); \
        return 1; \
    } \
} while (0);

bool test_solve_part_1(void) {
    struct {
        char *input;
        int expected;
    } tests[] = {
        {
            .input = "(())",
            .expected = 0,
        },
        {
            .input = "()()",
            .expected = 0,
        },
        {
            .input = "(((",
            .expected = 3,
        },
        {
            .input = "(()(()(",
            .expected = 3,
        },
        {
            .input = "))(((((",
            .expected = 3,
        },
        {
            .input = "())",
            .expected = -1,
        },
        {
            .input = "))(",
            .expected = -1,
        },
        {
            .input = ")))",
            .expected = -3,
        },
        {
            .input = ")())())",
            .expected = -3,
        },
    };

    for (size_t i = 0; i < sizeof(tests) / sizeof(tests[0]); i++) {
        int result = solve_part_1(tests[i].input, strlen(tests[i].input));

        if (result != tests[i].expected) {
            printf("[test %ld] expected=%d, got=%d\n", i, tests[i].expected, result);
            return false;
        }
    }

    return true;
}

bool test_solve_part_2(void) {
    struct {
        char *input;
        int expected;
    } tests[] = {
        {
            .input = ")",
            .expected = 1,
        },
        {
            .input = "()())",
            .expected = 5,
        },
    };

    for (size_t i = 0; i < sizeof(tests) / sizeof(tests[0]); i++) {
        int result = solve_part_2(tests[i].input, strlen(tests[i].input));

        if (result != tests[i].expected) {
            printf("[test %ld] expected=%d, got=%d\n", i, tests[i].expected, result);
            return false;
        }
    }

    return true;
}

int main(void) {
    RUN_TEST(test_solve_part_1);
    RUN_TEST(test_solve_part_2);

    printf("ok\n");
    return 0;
}
