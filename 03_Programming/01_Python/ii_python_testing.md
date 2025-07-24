# Testing
https://realpython.com/python-testing/

Three common testing modules in python
- unittest
- nose/ nose2
- pytest

## Unittest
```
import unittest
from my_sum import sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)
if __name__ == '__main__':
    unittest.main()
```

# Pytest
- Create a testing function
  - The function name should be of the format test_*() for pytest to detect
  - The test functions should contain necessary asserts.
- Go to the root, and into the terminal and run pytest