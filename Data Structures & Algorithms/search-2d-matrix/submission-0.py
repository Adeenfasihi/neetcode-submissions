class Solution:
    def get_row(self, matrix: List[List[int]], target: int) -> List[int]:
        while True:
            mid = len(matrix)//2

            if mid == 0:
                return matrix

            if matrix[mid][0] > target:
                matrix = matrix[:mid]
            else:
                matrix = matrix[mid:]
        

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.get_row(matrix, target)[0]
        return target in row
        

            



