# imports omitted...
DATA = [
    ['plist/true.bin', True],
    ['plist/false.bin', False],
    # ...more data rows omitted...
]

class DataProvider(type):
    def __new__(meta, classname, bases, classDict):
        def create_test_method(fname, expected):
            def test_method(self):
                fd = self.read_file(fname)
                obj = read_binary_plist(fd)
                self.assertEqual(obj, expected)
            return test_method

        # generate new methods based on test data
        for fname, expected in DATA:
            part = os.path.splitext(os.path.basename(fname))[0]
            classDict["test_" + part] = create_test_method(fname, expected)

        # create!
        return type.__new__(meta, classname, bases, classDict)

class TestReadBinary(unittest.TestCase):
    __metaclass__ = DataProvider

    def read_file(self, fname):
        fd = open(os.path.join(os.path.dirname(__file__), fname), 'rb')

        try:
            s = fd.read()
            return StringIO(s)
        finally:
            fd.close()