import unittest
import day04


class TestDay04(unittest.TestCase):
    def test_solve_part_1(self) -> None:
        tests: list[tuple[str, int]] = [
            ("abcdef", 609043),
            ("pqrstuv", 1048970),
        ]

        for (dims, expected) in tests:
            self.assertEqual(day04.solve_part_1(dims), expected)

    def test_answers(self) -> None:
        with open("inputs/day04.txt", "r") as f:
            line = f.readline().strip()
            self.assertEqual(day04.solve_part_1(line), 282749)
            self.assertEqual(day04.solve_part_2(line), 9962624)


if __name__ == "__main__":
    unittest.main()
