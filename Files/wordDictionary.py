


class WordDictionary:
    def __init__(self):
        self.hmap = {}

    def addWord(self, word):
        if word not in self.hmap:
            self.hmap[word] = True
        return

    def search(self,word):
        import collections
        if word in self.hmap:
            return True
        else:
            counter = collections.Counter(word)
            
            for w in self.hmap.keys():
                if len(w) == len(word):
                    dot_cnt, match_cnt = 0, 0
                    for i in range(len(w)):
                        if word[i] != '.' and word[i] != w[i]:
                            return False
                        elif word[i] == '.' :
                            dot_cnt += 1
                            continue
                        else:
                            match_cnt += 1
                    
                    if dot_cnt + match_cnt == len(word):
                        return True

                else:
                    return False

            return False


dict = WordDictionary()
dict.addWord('a')
dict.addWord('ab.')
dict.search('')