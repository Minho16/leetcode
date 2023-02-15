class Solution:
    # (Runtime 334 ms | Memory 15.2 MB)
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        num_int = ''
        for i in num:
            num_int += str(i)
        
        num_int = int(num_int)
        num_int += k

        answer = []
        for j in str(num_int):
            answer.append(int(j))
        return answer