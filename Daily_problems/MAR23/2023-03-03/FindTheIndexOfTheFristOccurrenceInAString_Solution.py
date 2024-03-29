# Solution using Rabin-Karp
"""
The value of using Rabin-Karp is in having a rolling hash whose value we can update in O(1) time. 
Instead of comparing needle char-by-char with all of the substrings of haystack, we compute the hash of 
each next substring and compare to the hash of the needle. If the hashes match, we do the char-by-char 
comparison to make sure that there's no hash collision happening (two strings having the same hash while being 
actually different). If we don't have any collisions (or have a few) then runtime will be ~O(N). 
Worst case, if we have collisions at each iteration and needle is the last substring of haystack, 
then the runtime will be O(NM). Where N is the lenght of the haystack and M is the length of needle.
"""


def strStr(self, haystack: str, needle: str) -> int:
    if needle == "":
        return 0
    N = len(needle)
    base = 26  # base of the polynomial hash
    prime_mod = 101  # to avoid hash overflow, doesn't have to be prime number

    def charcode(ch):
        return ord(ch) - ord("a")

    def myhash(s):
        """polynomial hash of a string"""
        my_hash = 0
        for ch in s:
            my_hash = (charcode(ch) + my_hash * base) % prime_mod
        return my_hash

    needle_hash = myhash(needle)
    rolling_hash = myhash(haystack[: N - 1])

    first_pow = base ** (
        N - 1
    )  # the first digit's base as a const, to avoid recomputation

    for i in range(N - 1, len(haystack)):
        rolling_hash = (rolling_hash * base + charcode(haystack[i])) % prime_mod
        if rolling_hash == needle_hash and needle == haystack[i + 1 - N : i + 1]:
            return i + 1 - N
        rolling_hash = (
            rolling_hash - charcode(haystack[i + 1 - N]) * first_pow
        ) % prime_mod

    return -1


# ---------------------------------------------------------------------------------------------------------

# Another solution using Rabin Karp
import sys


def strStr(self, haystack, needle):
    return haystack.find(needle)


# Rabin Karp, built-in hash, constant time (tested)


def strStr(self, haystack, needle):
    n, h = len(needle), len(haystack)
    hash_n = hash(needle)
    for i in range(h - n + 1):
        if hash(haystack[i : i + n]) == hash_n:
            return i
    return -1


# Rabin Karp, numeral base for both uppercase and lowercase letters, constant time
def strStr(self, haystack, needle):
    def f(c):
        return ord(c) - ord("A")

    n, h, d, m = len(needle), len(haystack), ord("z") - ord("A") + 1, sys.maxint
    if n > h:
        return -1
    nd, hash_n, hash_h = d ** (n - 1), 0, 0
    for i in range(n):
        hash_n = (d * hash_n + f(needle[i])) % m
        hash_h = (d * hash_h + f(haystack[i])) % m
    if hash_n == hash_h:
        return 0
    for i in range(1, h - n + 1):
        hash_h = (
            d * (hash_h - f(haystack[i - 1]) * nd) + f(haystack[i + n - 1])
        ) % m  # e.g. 10*(1234-1*10**3)+5=2345
        if hash_n == hash_h:
            return i
    return -1


# KMP Solution
def strStr(self, haystack, needle):
    n, h = len(needle), len(haystack)
    i, j, nxt = 1, 0, [-1] + [0] * n
    while i < n:  # calculate next array
        if j == -1 or needle[i] == needle[j]:
            i += 1
            j += 1
            nxt[i] = j
        else:
            j = nxt[j]
    i = j = 0
    while i < h and j < n:
        if j == -1 or haystack[i] == needle[j]:
            i += 1
            j += 1
        else:
            j = nxt[j]
    return i - j if j == n else -1
