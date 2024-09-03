class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #we simply need to do a binary search of the matrix range, then of the single array range

        l, r = 0, len(matrix) - 1

        found_index = None

        while l <= r:
            mid_arr = (l + r) // 2

            if matrix[mid_arr][0] <= target and matrix[mid_arr][-1] >= target:
                found_index = mid_arr
                break
            elif matrix[mid_arr][0] < target:
                l = mid_arr + 1
            else:
                r = mid_arr - 1
        
        if found_index is None:
            return False

        l, r = 0, len(matrix[found_index]) - 1

        while l <= r:
            mid = (l + r) // 2

            if matrix[found_index][mid] == target:
                return True
            elif matrix[found_index][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
