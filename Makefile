CFLAGS = -Wall -Wextra -Werror -std=c17

.PHONY: test
test: \
	day01_test

.PHONY: day01_test
day01_test: day01/day01.c day01/day01.h day01/test.c
	@mkdir -p bin
	@gcc $(CFLAGS) $^ -o ./bin/day01_test
	@./bin/day01_test

.PHONY: day01
day01: day01/day01.c day01/day01.h day01/main.c
	@mkdir -p bin
	@gcc $(CFLAGS) $^ -o ./bin/day01
	@./bin/day01 ./day01/input.txt | tee ./day01/results.txt
	@diff -q ./day01/results.txt ./day01/answers.txt
