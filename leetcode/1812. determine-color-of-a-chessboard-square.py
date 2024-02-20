#https://leetcode.com/problems/determine-color-of-a-chessboard-square/
#https://yeonwlee.github.io/posts/problemsolving-leetcode-1812-determine-color-of-a-chessboard-square/

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        position_pair: dict[str, int] = {char: index for index, char in enumerate("abcdefgh", 1)}
        return (position_pair[coordinates[0]] + int(coordinates[1])) % 2 == 1

class Solution2:
    def squareIsWhite(self, coordinates: str) -> bool:
        row: int = ord(coordinates[0]) - ord('a') + 1  # 행을 나타내는 문자를 숫자로 변환
        col: int = int(coordinates[1])
        return (row + col) % 2 == 1