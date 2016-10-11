from pyparsing import Word, alphas, Suppress, Combine, nums, string, Optional, Regex
from time import strftime

SAMPLE = '''
<132>Sep  6 14:35:48 codezone.local test.app[68898]: bla bla bla warn
<131>Sep  6 14:35:58 codezone.local test.app[68902]: bla bla bla error
<11>Sep  6 14:37:53 codezone.local Dock[154]: CGSReleaseWindowList: called with 5 invalid window(s)
<11>Sep  6 14:38:09 codezone.local WindowServer[79]: CGXSetWindowListAlpha: Invalid window 0
'''
SAMPLE = SAMPLE.strip()

class Parser(object):
    def __init__(self):
        ints = Word(nums)

        # priority
        priority = Suppress("<") + ints + Suppress(">")

        # timestamp
        month = Word(string.uppercase, string.lowercase, exact=3)
        day   = ints
        hour  = Combine(ints + ":" + ints + ":" + ints)

        timestamp = month + day + hour

        # hostname
        hostname = Word(alphas + nums + "_" + "-" + ".")

        # appname
        appname = Word(alphas + "/" + "-" + "_" + ".") + Optional(Suppress("[") + ints + Suppress("]")) + Suppress(":")

        # message
        message = Regex(".*")

        # pattern build
        self.__pattern = priority + timestamp + hostname + appname + message

    def parse(self, line):
        parsed = self.__pattern.parseString(line)

        payload              = {}
        payload["priority"]  = parsed[0]
        payload["timestamp"] = strftime("%Y-%m-%d %H:%M:%S")
        payload["hostname"]  = parsed[4]
        payload["appname"]   = parsed[5]
        payload["pid"]       = parsed[6]
        payload["message"]   = parsed[7]

        return payload

'''
Run like this: python -m unittest discover
'''

import unittest


class TestParser(unittest.TestCase):
    def setUp(self):
        self.parser = Parser()

    def test_parser(self):
        for index, line in enumerate(SAMPLE.split("\n")):
            self.assertTrue(isinstance( self.parser.parse(line), dict))
            # if index == 0:
            #     self.assertDictEqual({'appname': 'test.app', 'timestamp': '2016-10-11 12:18:34', 'hostname': 'codezone.local', 'pid': '68898', 'priority': '132', 'message': 'bla bla bla warn'},
            #                          self.parser.parse(line))
            self.assertIn("appname", self.parser.parse(line).keys())
            self.assertIn("timestamp", self.parser.parse(line).keys())
            self.assertIn("hostname", self.parser.parse(line).keys())
            self.assertIn("message", self.parser.parse(line).keys())

