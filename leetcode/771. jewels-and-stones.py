#https://leetcode.com/problems/jewels-and-stones/
from collections import defaultdict

# class Solution:
#     def numJewelsInStones(self, jewels: str, stones: str) -> int:
#         stone_info: dict[str, int] = defaultdict(int)
#         mapped_jewels = set(jewels)
#         for stone in stones:
#             stone_info[stone] += 1
#         return sum([stone_info[jewel] for jewel in mapped_jewels if jewel in stone_info])

##1. 굳이 jewels가 중복되어 있지 않음을 알면서도 set으로 만들어서 풀었던 이유는, 조회 때문이었다.
##하지만, 단순 in이 아니라 for문으로 순회하는 상황이었으므로 set으로 만들 필요가 없었다. for ~ in 과 in 을 혼동하지 말자
##2. 제너레이터 표현식을 사용하면, 메모리를 아낄 수 있다. 
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone_info: dict[str, int] = defaultdict(int)
        for stone in stones:
            stone_info[stone] += 1
        return sum(stone_info[jewel] for jewel in jewels if jewel in stone_info)