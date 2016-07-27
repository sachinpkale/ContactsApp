import unittest
from src.prefix_tree import PrefixTree

class PrefixTreeTestCase(unittest.TestCase):

    def test__get_values__(self):
    	trie = PrefixTree()

    	self.assertEquals(trie.__get_values__({'a': {'b': {}, 'c': {'d': {}, 'e': {'f': {}}}}}), [])
    	self.assertEquals(trie.__get_values__({'a': {'values': ['x', 'y', 'z']}}), ['x', 'y', 'z'])
    	self.assertEquals(trie.__get_values__({'a': {'values': ['x', 'y', 'z'], 'b': {'z': {'q': {'values': ['p', 'q']}}}}}), ['x', 'y', 'z', 'p', 'q'])
    	self.assertEquals(trie.__get_values__({'a': {'values': ['x', 'y', 'z']}, 'b': {'values': ['m'], 'z': {'q': {'values': ['p', 'q']}}}}), ['x', 'y', 'z', 'm', 'p', 'q'])


    def test_search(self):
		prefix_tree = PrefixTree()

		prefix_tree.trie = {'a': {'b': {}, 'c': {'d': {}, 'e': {'f': {}}}}}
		self.assertEquals(prefix_tree.search('Xyz'), [])

		prefix_tree.trie = {'a': {'values': ['xab', 'yqw', 'zxc']}}
		self.assertEquals(prefix_tree.search('a'), ['xab', 'yqw', 'zxc'])

		prefix_tree.trie = {'a': {'values': ['x', 'y', 'z'], 'b': {'z': {'q': {'values': ['p', 'q']}}}}}
		self.assertEquals(prefix_tree.search('a'), ['x', 'y', 'z', 'p', 'q'])

		prefix_tree.trie = {'a': {'values': ['x', 'y', 'z'], 'b': {'z': {'q': {'values': ['p', 'q']}}}}}
		self.assertEquals(prefix_tree.search('abz'), ['p', 'q'])

		prefix_tree.trie = {'a': {'values': ['x', 'y', 'z'], 'b': {'z': {'q': {'values': ['p', 'q']}}}}}
		self.assertEquals(prefix_tree.search('abzy'), [])

		prefix_tree.trie = {'a': {'values': ['x'], 'b': {'values': ['y'], 'c': {'d': {'values': ['z']}}}}}
		self.assertEquals(prefix_tree.search('abc'), ['z'])

		prefix_tree.trie = {'a': {'values': ['x'], 'b': {'values': ['y'], 'c': {'d': {'values': ['z']}}}}}
		self.assertEquals(prefix_tree.search('ab'), ['y', 'z'])

		prefix_tree.trie = {'a': {'values': ['x'], 'b': {'values': ['y'], 'c': {'d': {'values': ['z']}}}}}
		self.assertEquals(prefix_tree.search('a'), ['x', 'y', 'z'])


    def test_add(self):
		prefix_tree = PrefixTree()
		prefix_tree.add('Abc', 'Abc Xyz')
		self.assertEquals(prefix_tree.trie, {'A': {'b': {'c': {'values': ['Abc Xyz']}}}})

		prefix_tree = PrefixTree()
		prefix_tree.add('Abc Xyz', 'Abc Xyz')
		self.assertEquals(prefix_tree.trie, {'A': {'b': {'c': {' ': {'X': {'y': {'z': {'values': ['Abc Xyz']}}}}}}}})

		prefix_tree = PrefixTree()
		prefix_tree.add('Abc', 'Abc Xyz')
		prefix_tree.add('Def', 'Def Pqr')
		prefix_tree.add('Abd', 'Def Pqr')
		self.assertEquals(prefix_tree.trie, {'A': {'b': {'c': {'values': ['Abc Xyz']}, 'd': {'values': ['Def Pqr']}}}, 'D': {'e': {'f': {'values': ['Def Pqr']}}}})

if __name__ == '__main__':
    unittest.main()
