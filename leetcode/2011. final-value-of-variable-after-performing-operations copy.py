class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for cur_excution in operations:
            #if '+' in cur_excution:
            if '+' == cur_excution[1]:
                x += 1
            else:
                x -= 1
        return x
                