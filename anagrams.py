from typing import List
import pandas as pd


def remove_whitespace(string: str) -> str:
    """Removes the whitespace from the provided string.

    Args:
        str:
            The string to remove its whitespace from.

    Returns:
        str:
            The provided string with its whitespace removed.
    """
    string = string.replace(" ", "")
    return ''.join(string.split())


def frequency(string: str) -> dict:
    """Creates a dictionary mapping each letter to its frequency.

    Args:
        string: str

    Returns:
        dict:
            Maps each letter to its frequency.
    """
    frequency = {}
    for letter in string:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1
    return frequency


def is_anagram(candidate: str, letters: str) -> bool:
    """Checks if the provided candidate is an anagram of the given letters.

    Args:
        candidate: str
            Check if this string is an anagram of the provided letters.
        letters: str
            The source letters in an anagram challenge.

    Returns:
        bool:
            True iff the provided candidate is an anagram of the provided letters.
    """

    letters = remove_whitespace(letters).lower()
    candidate = remove_whitespace(candidate).lower()

    if len(candidate) != len(letters):
        return False

    candidate_frequency = frequency(candidate)
    letters_frequency = frequency(letters)

    all_letters = list(set(list(candidate_frequency.keys()) + list(letters_frequency.keys())))

    for letter in all_letters:
        if letter not in candidate_frequency or letter not in letters_frequency:
            return False
        elif candidate_frequency[letter] != letters_frequency[letter]:
            return False
    return True


def search_for_anagrams(letters: List[chr], strings: List[str]) -> List[str]:
    """Searches through all the strings to see which is an anagram of letters.

    Args:
        letters: List[chr]:
            The given letters in an anagram challenge.
        strings: List[str]:
            Strings to check if they are anagrams of the given letters.
    """
    return list(filter(lambda string: is_anagram(string, letters), strings))


def get_actors_names() -> List[str]:
    """Gets the names of the actors.

    Returns:
        List[str]:
            The names of the actors.
    """
    df = pd.read_csv('./data/actorfilms.csv')
    return df.Actor.unique().tolist()
