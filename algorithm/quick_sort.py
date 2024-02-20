class QuickSort:
    def sort(self, source: list, start_index: int, end_index: int) -> list:
        if end_index - start_index > 0:
            pivot_index = (start_index + end_index) // 2 #피봇 인덱스
            smaller_than_pivot: int = end_index
            bigger_than_pivot: int = start_index
            while bigger_than_pivot < smaller_than_pivot:
                while smaller_than_pivot > pivot_index and source[pivot_index] <= source[smaller_than_pivot]:
                    smaller_than_pivot -= 1
                while source[bigger_than_pivot] < source[pivot_index]:    
                     bigger_than_pivot += 1
                if bigger_than_pivot < smaller_than_pivot:
                    source[smaller_than_pivot], source[bigger_than_pivot] = source[bigger_than_pivot], source[smaller_than_pivot]
                    smaller_than_pivot -= 1
                    bigger_than_pivot += 1  
            self.sort(source, start_index, pivot_index - 1)
            self.sort(source, pivot_index + 1, end_index)     
        return source
    
sort = QuickSort()
# arr = [1, 30, 4, 2, 12, 5]
arr = [1, 3, 45, 21, 12, 51, 3, 11, 6]
print(sort.sort(arr, 0, len(arr) - 1))