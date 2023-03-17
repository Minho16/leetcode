from Verifying_an_Alien_Dictionary import Solution


def test_isAlienSorted():
    sol = Solution()

    # Test case 1: words are sorted
    words = ["hello", "leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    assert sol.isAlienSorted(words, order)

    # Test case 2: words are not sorted
    words = ["word", "world", "row"]
    order = "worldabcefghijkmnpqstuvxyz"
    assert not sol.isAlienSorted(words, order)

    # Test case 3: words have the same prefix
    words = ["apple", "app"]
    order = "abcdefghijklmnopqrstuvwxyz"
    assert not sol.isAlienSorted(words, order)

    # Test case 4: words have the same letters
    words = ["abc", "def", "xyz"]
    order = "abcdefghijklmnopqrstuvwxyz"
    assert sol.isAlienSorted(words, order)

    # Test case 5: single word
    words = ["apple"]
    order = "abcdefghijklmnopqrstuvwxyz"
    assert sol.isAlienSorted(words, order)

    # Test case 6: empty word list
    words = []
    order = "abcdefghijklmnopqrstuvwxyz"
    assert sol.isAlienSorted(words, order)
