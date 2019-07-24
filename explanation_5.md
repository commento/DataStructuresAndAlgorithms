# trie autocomplete problem5

Implementation is based on Trie algorithm. suffixes() is recursively implemented exploiting the list extension (list.extend(lst)) in order to return a list back in every recursion step.

Tests cover a edge case related to a not found element in the Trie and two normal cases with multiple string returned. Tested also on jupyter as well.

Time complexity of insert and find is O(n) where n is the number of char in the word. Time complexity of suffixes() is inversely proportional to the number of chars in the suffix O(1/n) where n is chars in suffix. Considering n as all the elements in the Trie, and suffixes() as a search algorithm of all the elements with a specific characteristics, the time complexity can be approximated as O(logn).
Space complexity for insert can vary in case chars in word are already in the Trie, the worst case scenario is O(n*m) where n possible character count and m the average word length.
Space complexity for find is O(1).
Space complexity for suffixes is O(n) where n is the number of words that matches the suffix.
