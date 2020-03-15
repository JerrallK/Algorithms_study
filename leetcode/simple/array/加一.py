class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length_d = len(digits)
        if length_d==1 and digits[0]==9:
            return [1,0]
        for i in range(length_d):
            if digits[length_d - 1] == 9:
                digits[length_d - 1] = 0
                return self.plusOne(digits[:length_d - 1]) + [0]
            else:
                digits[length_d - 1] += 1
                return digits
s=Solution()
print(s.plusOne([1,9,9]))