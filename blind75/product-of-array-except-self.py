class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res = []
        # for i in range(len(nums)):
        #     temp_product = 1;
        #     for j, num in enumerate(nums):
        #         if i != j:
        #             temp_product *= num
        #     res.append(temp_product)
        # return res


        # solution-2 recursive
        # i = 0
        # len_nums = len(nums)
        # prev_product = 1
        # res = [1] * len_nums;

        # def recursiveProduct(nums, i, prev_product):

        #     if len_nums - 1 == i:
        #         res[i] = prev_product
        #         return nums[i]

        #     next_product = recursiveProduct(nums, i + 1, prev_product * nums[i])
        #     res[i] = prev_product * next_product

        #     return nums[i] * next_product

        # recursiveProduct(nums, i, prev_product)

        # solution-3 recursive
        # def recursiveProduct(nums, i, prev_product):

        #     if len_nums - 1 == i:
        #         return nums[i], [prev_product]

        #     next_product, next_product_list = recursiveProduct(nums, i + 1, prev_product * nums[i])
        #     current_list = [prev_product * next_product]
        #     current_list.extend(next_product_list)

        #     return nums[i] * next_product, current_list

        # final_product, res = recursiveProduct(nums, i, prev_product)

        # solution-4: O(n) with O(n) memory
        # res = [1] * len(nums);
        # prefix = [1] * len(nums)
        # postfix = [1] * len(nums)

        # prefix_prod = 1
        # postfix_prod = 1
        
        # for i, num in enumerate(nums):
        #     prefix[i] = prefix_prod
        #     prefix_prod *= num

        # for j in range(len(nums) - 1, -1, -1):
        #     postfix[j] = postfix_prod
        #     postfix_prod *= nums[j]

        # for i in range(len(prefix)):
        #     res[i] = prefix[i] * postfix[i]

        # solution-4: Time O(n) and memory O(1), res is not counted in memory
        res = [1] * len(nums);
        pre_product = 1;
        post_product = 1;

        for i, num in enumerate(nums):
            res[i] = pre_product
            pre_product *= num

        for j in range(len(nums) - 1, -1, -1):
            res[j] *= post_product
            post_product *= nums[j]
        
        return res
        