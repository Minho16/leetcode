from typing import List


class Solution:
    # O(n) complexity solutions. (Runtime: 56 ms (89.16%) | Memory: 13.9 MB (96.87%))
    def compress(self, chars: List[str]) -> int:
        i = 1
        current_char = chars[0]
        new_pos = 0
        counter = 1
        while i <= len(chars):
            if i < len(chars) and chars[i] == current_char:
                counter += 1
            # append char and counter at 'new_pos' index
            else:
                insert_counter = counter
                chars[new_pos] = current_char
                current_char = chars[min(len(chars) - 1, i)]
                counter = 1
                if insert_counter == 1:
                    new_pos += 1
                else:
                    n = str(insert_counter)
                    new_pos += 1
                    for char in n:
                        chars[new_pos] = char
                        new_pos += 1
            i += 1
        chars = chars[:new_pos]
        return len(chars)


s = Solution()
chars = ["a"]
r = s.compress(chars)
print(r, r == 6)


chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
r = s.compress(chars)
print(r, r == 4)
