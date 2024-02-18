
#https://leetcode.com/problems/make-three-strings-equal/
#https://yeonwlee.github.io/posts/problemsolving-leetcode-2937-make-three-strings-equal/

#접근
#그냥 앞에서부터 문자열이 같은지 비교. 같은 문자열이 나온 경우 같지 않은 오른쪽 문자의 개수를 셈
#첫글자가 다르면 무조건 다름
class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        if s1[0] == s2[0] and s1[0] == s3[0]:
            shortest_str: str = min(s1, s2, s3, key=len)
            for index in range(len(shortest_str), 0, -1):
                if (s1[:index] == shortest_str[:index] and
                    s2[:index] == shortest_str[:index] and
                    s3[:index] == shortest_str[:index]):
                    same_value_range: int = index
                    return (len(s1) + len(s2) + len(s3)) - (same_value_range * 3)
        return -1 

#효율성 개선
class Solution2:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        shortest_str_length: int = min(len(s1), len(s2), len(s3))
        last_matched_index: int = -1
        for index in range(shortest_str_length):
            if s1[index] != s2[index] or s1[index] != s3[index]:
                break
            last_matched_index = index
        if last_matched_index == -1: #좌측에서부터 어떤 문자도 같지 않을 때
            return -1
        return (len(s1) + len(s2) + len(s3)) - (last_matched_index + 1) * 3 # 각 문자열의 우측에서부터 하나씩 글자를 지워나가서 글자를 같게 만들 때의 연산 수 계산
        
sol = Solution2()
print(sol.findMinimumOperations('ab', 'abd', 'abs'))