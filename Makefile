.PHONY: test
test: \
	day01_test

.PHONY: day01_test
day01_test:
	black -q day01
	mypy day01
	python day01/day01_test.py

.PHONY: day01
day01:
	@python ./day01/day01.py ./day01/input.txt

.PHONY: day02_test
day02_test:
	black -q day02
	mypy day02
	python day02/day02_test.py

.PHONY: day02
day02:
	@python ./day02/day02.py ./day02/input.txt

.PHONY: day03_test
day03_test:
	black -q day03
	mypy day03
	python day03/day03_test.py

.PHONY: day03
day03:
	@python ./day03/day03.py ./day03/input.txt
