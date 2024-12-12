from src.types import Grid
from src.utils import WordSearch


def parse(data: str) -> dict[int, tuple]:
    data = [line.strip() for line in data.strip().splitlines()]
    return {1: (data,), 2: (data,)}


def part1(puzzle: Grid[str]) -> int:
    ws = WordSearch(puzzle)
    return len(ws.search("XMAS", find_all=True))


class XWordSearch(WordSearch):
    def _get_matches(self, row: int, col: int, target_word: str) -> WordSearch.Matches:
        direction_pairs = [
            (self.direction["UL"], self.direction["DR"]),
            (self.direction["DL"], self.direction["UR"]),
        ]
        half_len = len(target_word) // 2
        x_positions: Grid[WordSearch.Position] = []

        for left_dir, right_dir in direction_pairs:
            positions_left = [
                (row + left_dir[0] * i, col + left_dir[1] * i)
                for i in range(1, half_len + 1)
            ]
            positions_right = [
                (row + right_dir[0] * i, col + right_dir[1] * i)
                for i in range(1, half_len + 1)
            ]
            positions = [*positions_left[::-1], (row, col), *positions_right]
            x_positions.append(positions)

        word1 = "".join(
            self.grid[r][c] if self._valid_position(r, c) else ""
            for r, c in x_positions[0]
        )
        word2 = "".join(
            self.grid[r][c] if self._valid_position(r, c) else ""
            for r, c in x_positions[1]
        )

        return (
            [sorted(set(x_positions[0] + x_positions[1]))]
            if target_word in [word1, word1[::-1]]
            and target_word in [word2, word2[::-1]]
            else []
        )

    def search(
        self, word: str, find_all: bool = False
    ) -> WordSearch.Match | WordSearch.Matches:
        if not word:
            return []
        if len(word) % 2 != 1:
            msg = "Word length must be odd."
            raise ValueError(msg)

        target_word = word if self.case_sensitive else word.lower()
        matches = []
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == target_word[len(target_word) // 2]:
                    matches.extend(self._get_matches(row, col, target_word))
                    if not find_all and len(matches):
                        return matches[0]
        return matches


def part2(puzzle: list[list[str]]) -> int:
    xws = XWordSearch(puzzle)
    return len(xws.search("MAS", find_all=True))
