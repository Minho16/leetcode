class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_num = int(a,2)
        b_num = int(b,2)
        total_sum = a_num + b_num
        return bin(total_sum)[2:]

'''
    Testing which user appears when a commit is done
'''