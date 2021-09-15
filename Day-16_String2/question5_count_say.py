class Solution:
    def countAndSay(self, n: int) -> str:
        num = '1'
        for _ in range(n-1):
            new_num = ''
            left, right = 0, 0
            while right < len(num):
                if num[right] != num[left]:
                    new_num += str(right - left) + num[left]
                    left = right
                right += 1
            new_num += str(right - left) + num[left]
            num = new_num
        return num