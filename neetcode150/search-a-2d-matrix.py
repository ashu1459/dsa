class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            mid = l + ((r - l) // 2)

            if target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][-1]:
                l = mid + 1
            else: # l = r = mid
                nl, nr = 0, len(matrix[mid]) - 1

                while nl <= nr:
                    n_mid = nl + ((nr - nl) // 2)

                    if target > matrix[mid][n_mid]:
                        nl = n_mid + 1
                    elif target < matrix[mid][n_mid]:
                        nr = n_mid - 1
                    else:
                        return True
                break
                
            
        return False


        