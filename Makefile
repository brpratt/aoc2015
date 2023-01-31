.PHONY: test
test: format check
	python -m unittest discover -s src -p '*_test.py'

.PHONY: format
format:
	black -q src

.PHONY: check
check:
	mypy src

.PHONY: day01
day01:
	@python ./src/day01.py ./inputs/day01.txt

.PHONY: day02
day02:
	@python ./src/day02.py ./inputs/day02.txt

.PHONY: day03
day03:
	@python ./src/day03.py ./inputs/day03.txt

.PHONY: day04
day04:
	@python ./src/day04.py ./inputs/day04.txt

.PHONY: day05
day05:
	@python ./src/day05.py ./inputs/day05.txt

.PHONY: day06
day06:
	@python ./src/day06.py ./inputs/day06.txt
