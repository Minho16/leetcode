from Implement_Trie_Prefix_Tree_Minho import Trie


def test_trie_insert_and_search():
    trie = Trie()

    trie.insert("apple")
    trie.insert("banana")
    trie.insert("applepie")
    trie.insert("bear")
    trie.insert("blueberry")

    assert trie.search("apple")
    assert trie.search("banana")
    assert trie.search("applepie")
    assert trie.search("bear")
    assert trie.search("blueberry")

    assert not trie.search("app")
    assert not trie.search("ban")
    assert not trie.search("bat")
    assert not trie.search("bea")
    assert not trie.search("blue")


def test_trie_startsWith():
    trie = Trie()

    trie.insert("apple")
    trie.insert("banana")
    trie.insert("applepie")
    trie.insert("bear")
    trie.insert("blueberry")

    assert trie.startsWith("app")
    assert trie.startsWith("ban")
    assert trie.startsWith("a")
    assert trie.startsWith("b")
    assert trie.startsWith("blu")

    assert not trie.startsWith("bat")
    assert trie.startsWith("be")
    assert not trie.startsWith("c")
    assert not trie.startsWith("d")
    assert not trie.startsWith("z")
