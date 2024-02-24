# trie data structure
# TrieNode definition
class TrieNode:
    def __init__(self,char=None) -> None:
        self.char = char
        self.children = [None]*26
        self.isTerminal = False
# Trie class        
class Trie:
    # constructor
    def __init__(self) -> None:
        self.root = TrieNode()
    # insertion helper function
    def insert(self,root ,word):
        #base case
        if len(word) == 0:
            root.isTerminal = True
            return 
        index = word[0]-'a'
        child = TrieNode()
        if root.children[index]:
            child = root.children[index]
        else:
            child = TrieNode(word[0])
            root.children[index] = child
        self.insert(child, word[1:])
    #search helper function
    def search(self,root,word):
        #base case
        if len(word) == 0:
            return root.isTerminal
        index = word[0]-'a'
        child = TrieNode()
        if root.children[index]:
            child = root.children[index]
        else:
            return False
        return self.search(child, word[1:])   
    # insertion
    def insertWord(self, word):
        word = word.lower()
        self.insert(self.root, word)
    # searching
    def searchWord(self,word):
        word = word.lower()
        return self.search(self.root,word)   

def main():
    t = Trie()
    t.insertWord('abcd')
    print(t.searchWord('abc'))
if __name__=='main':
    main()