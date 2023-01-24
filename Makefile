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
