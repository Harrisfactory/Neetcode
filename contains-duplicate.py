dis_nums = set()

        for num in nums:
            if num in dis_nums:
                return True
            dis_nums.add(num)

        return False
