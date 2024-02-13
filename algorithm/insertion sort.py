class InsertionSort():
    def sort(self, target: list) -> list:
        for index in range(1, len(target)):
            for compared_index in range(0, index + 1):
                if target[index] < target[compared_index]:
                    target.insert(compared_index, target.pop(index))
                    break
        return target
    
    
class InsertionSort2:
    def sort(self, target: list) -> list:
        for index in range(1, len(target)):
            current_value = target[index]
            position: int = index
            while position > 0 and target[position - 1] > current_value:
                target[position] = target[position - 1]
                position -= 1
            target[position] = current_value
        return target

    
sort = InsertionSort2()
print(sort.sort([67, 33, 21, 84, 49, 50, 75]))