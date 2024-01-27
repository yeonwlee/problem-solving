## 1.
# def twoSum(source_nums, target):
#     source_nums.sort()
#     for first_value_index, first_value_num in enumerate(source_nums[:len(source_nums) - 1]):
#         if first_value_num < target:
#             for second_value_index, second_value_num in enumerate(source_nums[first_value_index + 1:]):
#                 sum_value = first_value_num + second_value_num
#                 if sum_value == target:
#                     return [first_value_index, first_value_index + 1 + second_value_index] 
#                 elif sum_value > target:
#                     break
#         else:
#             return "해당하는 숫자 조합이 없습니다"


##2.
# def twoSum(source_nums, target):
#     sorted_source_nums_with_index = sort_with_origin_index(source_nums)
#     for first_value_position, first_value in enumerate(sorted_source_nums_with_index[:len(source_nums) - 1]):
#         if first_value[0] < target:
#             for second_value in sorted_source_nums_with_index[first_value_position + 1:]:
#                 sum_value = first_value[0] + second_value[0]
#                 if sum_value == target:
#                     return [first_value[1], second_value[1]] 
#                 elif sum_value > target:
#                     break
#         else:
#             return []

# def sort_with_origin_index(source_nums):
#     value_with_index = [(num, index) for index, num in enumerate(source_nums)]
#     return sorted(value_with_index)


### 제출한 로직
def twoSum(source_nums, target):
    sorted_source_nums_with_index = sort_with_origin_index(source_nums)
    for first_value_position, first_value in enumerate(sorted_source_nums_with_index[:len(source_nums) - 1]):
        for second_value in sorted_source_nums_with_index[first_value_position + 1:]:
            sum_value = first_value[0] + second_value[0]
            if sum_value == target:
                return [first_value[1], second_value[1]]
            elif sum_value > target:
                break
        
def sort_with_origin_index(source_nums):
    value_with_index = [(num, index) for index, num in enumerate(source_nums)]
    return sorted(value_with_index)


#정렬을 하지 않으면, 비교할 때마다 전체를 돌아야한다. 그래서 오름차순으로 정렬하는 것을 고려했다

#실수1: 정렬을 해놓고 해당 정렬된 리스트를 기준으로 정답을 찾음ㅎ
#-> 정렬을 하되, (값, 원래의 인덱스)의 형태로 가공해서 저장해놓자.

#실수2: 인풋값이 모두 0이 아닌 양수 정수일 것으로 가정함

## 결과: 느린 수행.


## 변경 로직
def two_sum(source_nums, target):
    seen = {}  # 값을 키로, 인덱스를 값으로 가질 것
    for index, num in enumerate(source_nums):
        value_for_searching = target - num
        if value_for_searching in seen:
            return [seen[value_for_searching], index]  # 두 번째 숫자의 인덱스와 현재 숫자의 인덱스 반환
        seen[num] = index  # 현재 숫자와 인덱스를 해시 테이블에 추가

print(two_sum([0,3,-3,4,-1], -1))

