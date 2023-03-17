from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        graf_d = {}
        # Create the adjacency list
        for i, num in enumerate(arr):
            if num not in graf_d:
                graf_d[num] = [i]
            else:
                graf_d[num].append(i)

        vis = [0] * len(arr)
        explore = [0]
        vis[0] = 1
        counter = 0
        while explore:
            ex2 = []
            for i in explore:
                if i == len(arr) - 1:
                    return counter
                if i - 1 >= 0 and vis[i - 1] == 0:
                    vis[i - 1] = 1
                    ex2.append(i - 1)
                if i + 1 < len(arr) and vis[i + 1] == 0:
                    vis[i + 1] = 1
                    ex2.append(i + 1)
                for j in graf_d[arr[i]]:
                    if vis[j] == 0:
                        vis[j] = 1
                        ex2.append(j)
            explore = ex2
            counter += 1
        return counter


s = Solution()
r = s.minJumps([100, -23, -23, 404, 100, 23, 23, 23, 3, 404])
print(r, r == 3)


r = s.minJumps([7])
print(r, r == 0)


r = s.minJumps([7, 6, 9, 6, 9, 6, 9, 7])
print(r, r == 1)

r = s.minJumps([-76, 3, 66, -32, 64, 2, -19, -8, -5, -93, 80, -5, -76, -78, 64, 2, 16])
print(r, r == 5)
