# route path problem7

Trie algorithm has been used to implement route paths for a server.
Router class takes in charge the conversion from urls path to a list of string elements that are handled by the Trie.

the class "fake" SimpleHTTPRequestHandlerFake() has been implemented in order to have a similar behavior also for testcase implementation.

Implementation is covering also edge cases with slashes at the end of the path or root path only. Tests are present for these scenarios.

As for problem 5:
Time complexity of insert and find is O(n) where n is the number of char in the word.
Space complexity for insert: the worst case scenario is O(n*m) where n possible character count and m the average word length.
Space complexity for find is O(1).