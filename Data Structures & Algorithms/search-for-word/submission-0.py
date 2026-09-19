class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(r:int, c:int, index:int):

            if index > len(word)-1 or  r < 0 or r >len(board)-1 or c < 0 or c > len(board[0])-1 or board[r][c] == "#":
                return False
            letter = word[index]
            if board[r][c] != letter:
                return False
            if index == len(word)-1 and board[r][c] == word[len(word)-1]:
                return True
            else:
                temp = board[r][c]
                board[r][c] = "#"
                res = dfs(r+1,c,index+1) or dfs(r-1,c,index+1) or dfs(r,c+1,index+1) or dfs(r,c-1, index+1)
                board[r][c] = temp
                return res
        


        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if dfs(row,col,0):
                        return True
        return False
        