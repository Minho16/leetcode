from Implement_Trie_Prefix_Tree_Minho import Trie

def test_trie_insert_and_search():
    trie = Trie()
    
    trie.insert("apple")
    trie.insert("banana")
    trie.insert("applepie")
    trie.insert("bear")
    trie.insert("blueberry")
    
    assert trie.search("apple") == True
    assert trie.search("banana") == True
    assert trie.search("applepie") == True
    assert trie.search("bear") == True
    assert trie.search("blueberry") == True
    
    assert trie.search("app") == False
    assert trie.search("ban") == False
    assert trie.search("bat") == False
    assert trie.search("bea") == False
    assert trie.search("blue") == False

def test_trie_startsWith():
    trie = Trie()
    
    trie.insert("apple")
    trie.insert("banana")
    trie.insert("applepie")
    trie.insert("bear")
    trie.insert("blueberry")
    
    assert trie.startsWith("app") == True
    assert trie.startsWith("ban") == True
    assert trie.startsWith("a") == True
    assert trie.startsWith("b") == True
    assert trie.startsWith("blu") == True
    
    assert trie.startsWith("bat") == False
    assert trie.startsWith("be") == True
    assert trie.startsWith("c") == False
    assert trie.startsWith("d") == False
    assert trie.startsWith("z") == False