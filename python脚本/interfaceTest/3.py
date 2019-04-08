import unittest

class DataProviderSupport(type):
    def __new__(meta, classname, bases, classDict):
        # method for creating our test methods
        def create_test_method(testFunc, args):
            return lambda self: testFunc(self, *args)

        # look for data provider functions
        for attrName, attr in classDict.items():
            if attrName.startswith("dataprovider_"):
                # find out the corresponding test method
                testName = attrName[13:]
                testFunc = classDict[testName]

                # the test method is no longer needed
                del classDict[testName]

                # generate test method variants based on
                # data from the data porovider function
                i = 1
                for args in attr():
                    classDict[testName + str(i)] = create_test_method(testFunc, args)
                    i += 1

        # create the type
        return type.__new__(meta, classname, bases, classDict)


class TestStringLength(unittest.TestCase):
    __metaclass__ = DataProviderSupport

    def dataprovider_test_len_function():  # no self!
        yield ("abc", 3)
        yield ("", 0)
        yield ("a", 1)

    def test_len_function(self, astring, expectedLength):
        self.assertEqual(expectedLength, len(astring))