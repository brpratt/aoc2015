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
