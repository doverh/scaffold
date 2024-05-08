import re
import unittest
from pswGen import getRandomPwd

class TestCalculations(unittest.TestCase):
    def testRandomPwdLenght(self):
        assert len(getRandomPwd(8))==8  

    def testRandomPwdContent(self):
        text = getRandomPwd(8)
        #print (text)
        assert re.match(r'[A-Za-z0-9!"#$%&\'()*+,-.\/:;<=>?@[\]^_`{|}~]{8}', getRandomPwd(8))


if __name__ == '__main__':
    unittest.main()
