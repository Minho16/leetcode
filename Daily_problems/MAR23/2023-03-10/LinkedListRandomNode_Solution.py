import random

"""
Reservoir sampling Solution
(https://en.wikipedia.org/wiki/Reservoir_sampling)

this is a conditional probability problem.

The key point is before we process the N-th element,
the probability of each previous N-1 element is equal to each other.
This is very important.
so after processing N-th element, the probability of each previous N-1 element
is still equal to each other.

At this time, the probability of N-th element is 1/N with no doubt, and the
rest (1 - 1 / N) = (N - 1) / N will be shared equally by previous N - 1
elements, that is (1 - 1 / N) / (N - 1) = K(N - 1) / N / (N - 1) = 1 / N

cost O(N) for getRandom every time

You may wonder since the time complexity is still O(N),
why do we have to spend so much.

In the case of streaming data, we cannot traverse all the data to obtain the
length, and then traverse the data again.
"""


class Solution(object):
    def __init__(self, head):
        self.head = head

    # Reservoir sampling and K == 1
    def getRandom(self):  # cost O(n) Time
        ans = 0
        p, i = self.head, 0
        while p:
            if (
                random.randint(0, i) == 0
            ):  # capacity of the reservoir is 1, because we just need to
                # return a single num
                # replace ans with i-th node.val # with probability 1/i
                ans = p.val
            p = p.next
            i += 1
        return ans
