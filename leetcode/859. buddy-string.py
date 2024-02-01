#https://leetcode.com/problems/buddy-strings/
# s와 goal의 문자열 길이는 다를 수도 있다. 다르다면 같아질 일도 없긴 하겠다.
# s의 문자열 길이나 goal의 문자열 길이가 1이 될 수도 있을 것이다.
#접근1. 두 문자열의 구성요소는 같아야한다.
# 두 문자열이 완전히 동일하다면, 동일한 문자열 간 이동을 해야한다. 동일한 문자끼리 위치를 바꿀 수 없다면 false다

## 두 문자열이 완전히 동일한 경우
    ## 동일한 문자 요소 간에 이동을 해야 True
    ## 아니면 False
## 두 문자열이 다르지만 
    ## 구성요소는 같은 경우
        ## 두 문자의 위치만 다른 경우 True
        ## 세 문자 이상의 위치가 다른 경우 False
    ## 구성요소도 다른 경우 False

# 실수1.두 문자열이 다른 부분이 두 군데지만, s 문자열의 위치를 변경해서 goal 문자열을 만들 수 있는지를 확인하지 않았다.
class Solution1:
    def buddyStrings(self, source_sentence: str, goal_to_make: str) -> bool:
        if len(source_sentence) != len(goal_to_make):
            return False
        different_position_and_value: dict[int, str] = {}
        count_of_different_postition = 0
        for index in range(len(source_sentence)):
            if source_sentence[index] != goal_to_make[index]:
                if (count_of_different_postition := count_of_different_postition + 1) > 3:
                    return False
                different_position_and_value[index] = source_sentence[index]
        if not different_position_and_value: ## 비어있는 경우: 모두 같다
            if len(source_sentence) == len(set(source_sentence)): ## s 문자열 내에 같은 문자열이 없다
                return False
            return True
        if len(different_position_and_value) == 2:
            return True
        return False


## 제출한 답
class Solution2:
    def buddyStrings(self, source_sentence: str, goal_to_make: str) -> bool:
        if len(source_sentence) != len(goal_to_make):
            return False
        different_position_and_value: dict[int, int] = {}
        count_of_different_postition = 0
        for index in range(len(source_sentence)):
            if source_sentence[index] != goal_to_make[index]:
                if (count_of_different_postition := count_of_different_postition + 1) > 3:
                    return False
                different_position_and_value[count_of_different_postition] = index
        if not different_position_and_value: ## 비어있는 경우: 모두 같다
            if len(source_sentence) == len(set(source_sentence)): ## s 문자열 내에 같은 문자열이 없다
                return False
            return True
        if len(different_position_and_value) == 2:
            if source_sentence[different_position_and_value[1]] == goal_to_make[different_position_and_value[2]] and source_sentence[different_position_and_value[2]] == goal_to_make[different_position_and_value[1]]:
                return True
        return False

#개선한 답
class Solution3:
    def buddyStrings(self, source_sentence: str, goal_to_make: str) -> bool:
        if len(source_sentence) != len(goal_to_make):
            return False
        mismatched_indices: list[int] = []
        for index, char in enumerate(source_sentence):
            if source_sentence[index] != goal_to_make[index]:
                if len(mismatched_indices) > 2:
                    return False
                mismatched_indices.append(index)
        if not mismatched_indices: ## 모든 문자열이 같다
            return len(source_sentence) > len(set(source_sentence)) ## source_sentence 문자열 내에 같은 문자열이 있으면 True
        if len(mismatched_indices) == 2:
            first, second = mismatched_indices
            return source_sentence[first] == goal_to_make[second] and source_sentence[second] == goal_to_make[first]
        return False

# mismatched_indices = [index for index, (source_char, goal_char) in enumerate(zip(source_sentence, goal_to_make)) if source_char != goal_char]
# collections.Counter로 중복 검사 가능
'''
변수명 개선: different_postion_and_value -> mismatched_indeces 
데이터 타입 변경: 딕셔너리 -> 리스트
리스트 컴프리헨션과 zip을 사용해서 mismatched_indices 구하기
range, len -> enumerate

'''


