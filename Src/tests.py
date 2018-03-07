import unittest

def doTest():
    suite = unittest.TestLoader().discover('.', pattern = "*_test.py")
    tests = unittest.TextTestRunner(verbosity=2).run(suite)
    return str(tests.errors) == '[]' and str(tests.failures) == '[]'

if __name__ == "__main__":
    doTest()

