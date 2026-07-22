class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colSet: list[set[int]] = [set() for _ in range(9)]
        rowSet: list[set[int]] = [set() for _ in range(9)]

        

        
        for i in range(0,9,3):
            for j in range(0,9,3):
                blockSet: set = set()
                for r in range(3):
                    r = r + i
                    for c in range(3):
                        c = c + j
                        num = board[r][c]
                        if num == ".":
                            continue
                        if num in blockSet:
                            return False
                        if num in colSet[c]:
                            return False
                        if num in rowSet[r]:
                            return False
                        
                        colSet[c].add(num)
                        rowSet[r].add(num)
                        blockSet.add(num)
        
        return True


        


        