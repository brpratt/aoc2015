import unittest
import day03


class TestDay03(unittest.TestCase):
    def test_solve_part_1(self) -> None:
        tests: list[tuple[str, int]] = [
            (">", 2),
            ("^>v<", 4),
            ("^v^v^v^v^v", 2),
        ]

        for (dims, expected) in tests:
            self.assertEqual(day03.solve_part_1(dims), expected)

    def test_solve_part_2(self) -> None:
        tests: list[tuple[str, int]] = [
            ("^v", 3),
            ("^>v<", 3),
            ("^v^v^v^v^v", 11),
        ]

        for (dims, expected) in tests:
            self.assertEqual(day03.solve_part_2(dims), expected)

    def test_answers(self) -> None:
        with open("inputs/day03.txt", "r") as f:
            line = f.readline().strip()
            self.assertEqual(day03.solve_part_1(line), 2081)
            self.assertEqual(day03.solve_part_2(line), 2341)


if __name__ == "__main__":
    unittest.main()
