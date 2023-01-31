import unittest
import day06


class TestDay06(unittest.TestCase):
    def test_solve_part_1(self) -> None:
        tests: list[tuple[list[str], int]] = [
            (["turn on 0,0 through 999,999"], 1_000_000),
            (["turn on 0,0 through 999,999", "toggle 0,0 through 999,0"], 999_000),
            (
                ["turn on 0,0 through 999,999", "turn off 499,499 through 500,500"],
                999_996,
            ),
        ]

        for (lines, expected) in tests:
            self.assertEqual(day06.solve_part_1(lines), expected)

    def test_solve_part_2(self) -> None:
        tests: list[tuple[list[str], int]] = [
            (["turn on 0,0 through 0,0", "turn on 0,0 through 0,0"], 2),
            (["toggle 0,0 through 0,0", "turn off 0,0 through 0,0"], 1),
        ]

        for (lines, expected) in tests:
            self.assertEqual(day06.solve_part_2(lines), expected)

    def test_answers(self) -> None:
        with open("inputs/day06.txt", "r") as f:
            lines = f.readlines()
            self.assertEqual(day06.solve_part_1(lines), 400410)
            self.assertEqual(day06.solve_part_2(lines), 15343601)


if __name__ == "__main__":
    unittest.main()
