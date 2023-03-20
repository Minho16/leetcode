import pytest
from Design_Add_and_Search_Words_Data_Structure_Minho import WordDictionary


@pytest.fixture
def word_dict():
    return WordDictionary()


def test_add_word(word_dict):
    word_dict.addWord("cat")
    assert word_dict.words_dictionary == {'c': ['cat']}
    word_dict.addWord("dog")
    assert word_dict.words_dictionary == {'c': ['cat'], 'd': ['dog']}
    word_dict.addWord("car")
    assert word_dict.words_dictionary == {'c': ['cat', 'car'], 'd': ['dog']}


def test_search_exact_match(word_dict):
    word_dict.addWord("cat")
    word_dict.addWord("dog")
    word_dict.addWord("car")
    assert word_dict.search("cat")
    assert word_dict.search("dog")
    assert word_dict.search("car")
    assert not word_dict.search("rabbit")


def test_search_with_dot(word_dict):
    word_dict.addWord("cat")
    word_dict.addWord("dog")
    word_dict.addWord("car")
    assert word_dict.search("c.t")
    assert word_dict.search(".a.")
    assert word_dict.search("...")
    assert word_dict.search("..g")
    assert word_dict.search("c..")
    assert not word_dict.search("g")
    assert not word_dict.search("c.")
    assert not word_dict.search("c..t")
    assert not word_dict.search("c.a")
    assert not word_dict.search("c...t")
