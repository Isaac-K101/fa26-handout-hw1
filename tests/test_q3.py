"""HW1 Question 3 Tests"""

import sys

sys.path.append('.')
from src.q3 import capitalize_words


"""Please write your tests here."""

# test basic functionality
def test_basic():
    assert capitalize_words("hello cs") == "Hello Cs"

# verify that already capitalized words are unchanged
def test_already_capitalized():
    assert capitalize_words("Hello Cs") == "Hello Cs"

def test_single_word():
    assert capitalize_words("hello") == "Hello"

# empty string should return empty string
def test_empty_string():
    assert capitalize_words("") == ""

def test_non_letter_start():
    # if word starts with non-letter, first letter after it gets capitalized
    assert capitalize_words("1hello") == "1Hello"

def test_non_letter_start_multiple():
    assert capitalize_words("1hello 2cs") == "1Hello 2Cs"

# string with only spaces, no words to capitalize
def test_all_spaces():
    assert capitalize_words("   ") == "   "

def test_mixed_case():
    assert capitalize_words("hELLO cS") == "HELLO CS"
