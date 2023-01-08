#include "day01.h"

int solve_part_1(char *input, size_t length) {
    int floor = 0;

    for (size_t i = 0; i < length; i++) {
        switch (input[i]) {
        case '(':
            floor++;
            break;
        case ')':
            floor--;
            break;
        }
    }

    return floor;
}

int solve_part_2(char *input, size_t length) {
    int floor = 0;

    for (size_t i = 0; i < length; i++) {
        switch (input[i]) {
        case '(':
            floor++;
            break;
        case ')':
            floor--;
            break;
        }

        if (floor < 0) {
            return i + 1;
        }
    }

    return 0;
}
