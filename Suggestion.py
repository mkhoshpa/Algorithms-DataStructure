
class TrieNode:
    def __init__(self,char = ''):
        self.count = 1
        self.char = char
        self.children = {}

    def add_child(self,char):
        if char in self.children:
            self.children[char].count += 1
        else:
            self.children[char] = TrieNode(char)

    def get_child(self,char):
        if char in self.children:
            return self.children[char]
        else:
            raise

    def get_max_child(self):
        if len(self.children) == 0:
            return None
        char = ''
        max_count = 0
        for child_key in self.children:
            if self.children[child_key].count > max_count:
                char = self.children[child_key].char
                max_count = self.children[child_key].count
        return self.get_child(char)

    def __str__(self):
        return 'char: '+str(self.char)+ ' count: '+str(self.count)+ ' children: '+str(self.children)

class Suggestion:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self,word):
        assert type(word) is str
        node = self.root
        while len(word)>0:
            char = word[0]
            word = word[1:]
            node.add_child(char)
            node = node.get_child(char)

    def get_recomendation(self,partial_word):
        assert type(partial_word) is str
        node = self.root
        word = partial_word
        while len(word) > 0:
            char = word[0]
            word = word[1:]
            node = node.get_child(char)
        while True:
            if node.count > 0 :
                c = node.get_max_child()
                #print(node)
                if c is None:
                    break
                c_child = c.get_max_child()
                partial_word = partial_word + c.char
                if c_child is not None and c.count > 2 * c_child.count:
                    break
                node = c
                continue
            break
        return partial_word

if __name__ == '__main__':
    S = Suggestion()
    words = ['caller','caller','can','catwalk','catwalk','cat','cat','catwalk','catwalky','camera','camera','camery','cam','camera']
    for word in words:
        S.add_word(word)
    print(S.get_recomendation('cam'))
    print(S.get_recomendation('cal'))
    print(S.get_recomendation('cat'))