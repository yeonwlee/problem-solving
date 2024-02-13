class SelectionSort:
    """
    리스트를 오름차순으로 정렬하는 Selection Sort 알고리즘을 구현한 클래스.

    주의사항:
    - 현재 이 클래스는 시퀀스형 객체 중에서 리스트만을 지원.

    Methods:
        sort(self, target: list) -> list:
            주어진 target 리스트를 오름차순으로 정렬한 뒤 반환.
    """
    def sort(self, target: list) -> list:
        if not self._is_valid_parameter(target):
            raise ValueError("parameter must be list")
        
        for index in range(len(target) - 1):
            min_index: int = index
            for cur_index in range(min_index + 1, len(target)):
                if target[cur_index] < target[min_index]:
                    min_index = cur_index
            self._exchange_position(target, index, min_index)
        return target


    def _is_valid_parameter(self, target: list) -> bool:
        return isinstance(target, list)


    def _exchange_position(self, target: list, target_index_for_exchanging: int, min_index: int) -> None:
         target[target_index_for_exchanging], target[min_index] = target[min_index], target[target_index_for_exchanging]


sort = SelectionSort()
print(sort.sort([67, 33, 21, 84, 49, 50, 75]))