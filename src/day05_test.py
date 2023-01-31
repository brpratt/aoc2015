import unittest
import day05


class TestDay05(unittest.TestCase):
    def test_solve_part_1(self) -> None:
        tests: list[tuple[str, int]] = [
            ("ugknbfddgicrmopn", 1),
            ("aaa", 1),
            ("jchzalrnumimnmhp", 0),
            ("haegwjzuvuyypxyu", 0),
            ("dvszwmarrgswjxmb", 0),
        ]

        for (line, expected) in tests:
            self.assertEqual(day05.solve_part_1([line]), expected)

    def test_solve_part_2(self) -> None:
        tests: list[tuple[str, int]] = [
            ("aaa", 0),
            ("qjhvhtzxzqqjkmpb", 1),
            ("xxyxx", 1),
            ("uurcxstgmygtbstg", 0),
            ("ieodomkazucvgmuy", 0),
        ]

        for (line, expected) in tests:
            self.assertEqual(day05.solve_part_2([line]), expected)

    def test_answers(self) -> None:
        with open("inputs/day05.txt", "r") as f:
            lines = f.readlines()
            self.assertEqual(day05.solve_part_1(lines), 236)
            self.assertEqual(day05.solve_part_2(lines), 51)


if __name__ == "__main__":
    unittest.main()
