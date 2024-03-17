import unittest

def first_non_repeating(stream: str) -> str:
    if not stream:
        return ''
    counts = {}
    for i in stream:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    for i in range(len(stream)):
        if counts[stream[i]] == 1:
            return stream[i]
    return ''
        
class TestFirstNonRepeating(unittest.TestCase):
    def test_first_non_repeating(self):
        self.assertEqual(first_non_repeating('leetcode'), 'l')
        self.assertEqual(first_non_repeating('loveleetcode'), 'v')
        self.assertEqual(first_non_repeating('aabb'), '')
        self.assertEqual(first_non_repeating(''), '')

if __name__ == '__main__':
    unittest.main()