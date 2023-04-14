import unittest

from fnv128a import compute_fnv128a


class TestFnv128aHash(unittest.TestCase):
    def test_reference_hash(self):
        bytes_array = compute_fnv128a(b'itemsFeatures')
        target =  b"\xeeb\xab\xb2\xe0S\xbd\xdd\xc8\t\xfba\xd6\xf7\xdah"
        self.assertEqual(bytes_array, target)


if __name__ == '__main__':
    unittest.main()
