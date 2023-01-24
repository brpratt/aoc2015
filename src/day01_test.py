import unittest
import day01


class TestDay01(unittest.TestCase):
    def test_solve_part_1(self) -> None:
        tests = [
            ("(())", 0),
            ("()()", 0),
            ("(((", 3),
            ("(()(()(", 3),
            ("))(((((", 3),
            ("())", -1),
            ("))(", -1),
            (")))", -3),
            (")())())", -3),
        ]

        for (line, expected) in tests:
            self.assertEqual(day01.solve_part_1(line), expected)

    def test_solve_part_2(self) -> None:
        tests = [(")", 1), ("()())", 5)]

        for (line, expected) in tests:
            self.assertEqual(day01.solve_part_2(line), expected)

    def test_answers(self) -> None:
        with open("inputs/day01.txt", "r") as f:
            line = f.readline()
            self.assertEqual(day01.solve_part_1(line), 74)
            self.assertEqual(day01.solve_part_2(line), 1795)


if __name__ == "__main__":
    unittest.main()
