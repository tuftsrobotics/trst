import unittest
import analyzer

class Test_Analyzer_Functions(unittest.TestCase):
    def setUp(self):
        self.dataStrings = [2**32-1, 0x00FF7FFF7FFF7FFF]
        self.dataAnswers = [[0,0,0,0,255,255,255,255], [00, 0xFF, 0x7F, 0xFF, 0x7F, 0xFF, 0x7F, 0xFF]]
        print "hello world"
    def test_get_bytes(self):
        for data, ans in zip(self.dataStrings, self.dataAnswers):
            test = analyzer.get_bytes(data, 8)
            self.assertEquals(test, ans)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_Analyzer_Functions)
    unittest.TextTestRunner(verbosity=2).run(suite)
