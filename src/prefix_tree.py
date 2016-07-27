"""A dictionary based prefix tree implementation"""
class PrefixTree:
    def __init__(self):
        self.trie = dict()

    def add(self, key, value):
        """Add key, value to prefix tree

        :param key:
        :param value:
        """
        trie = self.trie
        if not key:
            return
        s = None
        for i in xrange(len(key)):
            s = key[i]
            if s not in trie:
                trie[s] = {}
            if i == len(key) - 1:
                if 'values' not in trie[s]:
                    trie[s]['values'] = []
                trie[s]['values'].append(value)
            trie = trie[s]

    def search(self, key):
        """Search prefix tree for a given key

        :param key: Key to be searched for
        :return list of values matching given key as prefix
        """
        trie = self.trie
        for s in key:
            if s not in trie:
                return []
            trie = trie[s]
        return self.__get_values__(trie)

    def __get_values__(self, root):
        """Get all values recursively from a subtree rooted at root

        :param root: Node in prefix tree
        :return List of values
        """
        values = []
        values += root.get('values', [])
        for child in root:
            if child != 'values':
                values += self.__get_values__(root[child])
        return values


