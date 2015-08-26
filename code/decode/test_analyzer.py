import analyzer

class TestAnalyzer(object):
    """ Test class for the airmar analyzer/decoder

    """
    def setup(self):
        self.dataStrings = [2**32-1, 0x00FF7FFF7FFF7FFF]
        self.dataAnswers = [[0,0,0,0,255,255,255,255], [00, 0xFF, 0x7F, 0xFF, 0x7F, 0xFF, 0x7F, 0xFF]]

    def test_get_bytes(self):
        """ Tests the get_bytes function in isolation """
        for data, ans in zip(self.dataStrings, self.dataAnswers):
            test = analyzer.get_bytes(data, 8)
            assert test == ans
