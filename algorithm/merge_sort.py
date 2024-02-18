
class MergeSort:
    def sort(self, source: list) -> list:
        if len(source) > 1:
            #분할
            mid: int = len(source) // 2
            left: list = source[:mid]
            right: list = source[mid:]

            #정복
            self.sort(left)
            self.sort(right)

            #병합
            self._merge(source, left, right)

        return source


    def _merge(self, result: list, left: list, right: list) -> None:
        left_index: int = 0
        right_index: int = 0
        result_index: int = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                result[result_index] = left[left_index]
                left_index += 1
            else:
                result[result_index] = right[right_index]
                right_index += 1
            result_index += 1

        if left_index < len(left):
            self._copy_remaining_elements(left, left_index, result, result_index)
        else:
            self._copy_remaining_elements(right, right_index, result, result_index)


    def _copy_remaining_elements(self, remain_list: list, remain_index: int,
                            result_list: list, result_index: int ) -> None:
            while remain_index < len(remain_list):
                result_list[result_index] = remain_list[remain_index]
                remain_index += 1
                result_index += 1

sort = MergeSort()
print(sort.sort([1, 30, 4, 2, 12, 5]))