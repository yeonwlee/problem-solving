#현재 target은 시퀀스형을 지원하지 않고 있음. 리스트 한정
#정렬 기준은 오름차순. 현재 파라미터 reverse는 쓰이고 있지 않음.
class BubbleSort:
	def sort(self, target: list, reverse: bool = False) -> list:
		is_all_paramters_valid: bool
		message: str
		is_all_paramters_valid, message = self._are_valid_parameters(target, reverse)
		if not is_all_paramters_valid:
			raise ValueError(message)
		num_of_sorted_value: int = 0
		while num_of_sorted_value != len(target):
			cur_most_bigger_index: int = 0
			while cur_most_bigger_index != len(target) - 1 - num_of_sorted_value:
				next_index: int = cur_most_bigger_index + 1
				if self._is_bigger_than_next_value(target[cur_most_bigger_index], target[next_index]):
					self._exchange_position(target, cur_most_bigger_index, next_index)
				cur_most_bigger_index += 1
			num_of_sorted_value += 1
		return target


	def _are_valid_parameters(self, target: list, reverse: bool) -> tuple[bool, str]:
		if not isinstance(target, list):
			return (False, "first parameter must be a list")
		if not isinstance(reverse, bool):
			return (False, "second parameter must be a bool")
		return (True, "")


	def _is_bigger_than_next_value(self, cur_value: int, next_value: int) -> bool:
		return cur_value > next_value


	def _exchange_position(self, target: list, cur_index: int, next_index: int) -> None:
		target[cur_index], target[next_index] = target[next_index], target[cur_index]


sort = BubbleSort()
print(sort.sort([67, 33, 21, 84, 49, 50, 75]))
## 입력값 검증 -> 오류 처리
## 테스트케이스