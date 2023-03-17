class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(x)
        neg_sym = ""

        if str_x[0] == "-":
            neg_sym = "-"
            str_x = str_x[1:]

        str_x = str_x[::-1]
        int_x = int(neg_sym + str_x)
        if int_x < -2147483648 or int_x > 2147483647:
            return 0
        else:
            return int_x
