
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        # not implemented
        pass
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        l = []

        if self.is_word is True and suffix != '':
            l.extend([suffix])

        for char in self.children:
            l.extend(self.children[char].suffixes(suffix+char))

        return l

class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

        
    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root
        
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        
        current_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root
        
        for char in prefix:
            if char not in current_node.children:
                return None
            current_node = current_node.children[char]
        
        return current_node

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

prefixNode = MyTrie.find("a")
print(prefixNode.suffixes()) #expected ['nt', 'nthology', 'ntagonist', 'ntonym']

prefixNode = MyTrie.find("f")
print(prefixNode.suffixes()) #expected ['un', 'unction', 'actory']

prefixNode = MyTrie.find("b")
print(prefixNode) #expected None

