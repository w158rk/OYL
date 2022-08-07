# Generated from .\OYL.g4 by ANTLR 4.10.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,10,65,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,
        5,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,4,8,55,8,8,11,8,12,8,56,1,9,1,
        9,5,9,61,8,9,10,9,12,9,64,9,9,0,0,10,1,1,3,2,5,3,7,4,9,5,11,6,13,
        7,15,8,17,9,19,10,1,0,4,3,0,9,10,13,13,32,32,1,0,48,57,5,0,9,10,
        13,13,32,32,45,46,48,57,4,0,9,10,13,13,32,32,46,46,66,0,1,1,0,0,
        0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,
        13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,1,21,1,0,0,0,3,
        30,1,0,0,0,5,32,1,0,0,0,7,34,1,0,0,0,9,38,1,0,0,0,11,43,1,0,0,0,
        13,46,1,0,0,0,15,49,1,0,0,0,17,54,1,0,0,0,19,58,1,0,0,0,21,22,5,
        99,0,0,22,23,5,97,0,0,23,24,5,116,0,0,24,25,5,101,0,0,25,26,5,103,
        0,0,26,27,5,111,0,0,27,28,5,114,0,0,28,29,5,121,0,0,29,2,1,0,0,0,
        30,31,5,46,0,0,31,4,1,0,0,0,32,33,5,45,0,0,33,6,1,0,0,0,34,35,7,
        0,0,0,35,36,1,0,0,0,36,37,6,3,0,0,37,8,1,0,0,0,38,39,7,1,0,0,39,
        40,7,1,0,0,40,41,7,1,0,0,41,42,7,1,0,0,42,10,1,0,0,0,43,44,7,1,0,
        0,44,45,7,1,0,0,45,12,1,0,0,0,46,47,5,73,0,0,47,48,5,78,0,0,48,14,
        1,0,0,0,49,50,5,79,0,0,50,51,5,85,0,0,51,52,5,84,0,0,52,16,1,0,0,
        0,53,55,7,1,0,0,54,53,1,0,0,0,55,56,1,0,0,0,56,54,1,0,0,0,56,57,
        1,0,0,0,57,18,1,0,0,0,58,62,8,2,0,0,59,61,8,3,0,0,60,59,1,0,0,0,
        61,64,1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,63,20,1,0,0,0,64,62,1,
        0,0,0,3,0,56,62,1,6,0,0
    ]

class OYLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    CATEGORY = 1
    DOT = 2
    DASH = 3
    WS = 4
    YEAR = 5
    NUM2 = 6
    IN = 7
    OUT = 8
    INTEGER = 9
    ID = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'category'", "'.'", "'-'", "'IN'", "'OUT'" ]

    symbolicNames = [ "<INVALID>",
            "CATEGORY", "DOT", "DASH", "WS", "YEAR", "NUM2", "IN", "OUT", 
            "INTEGER", "ID" ]

    ruleNames = [ "CATEGORY", "DOT", "DASH", "WS", "YEAR", "NUM2", "IN", 
                  "OUT", "INTEGER", "ID" ]

    grammarFileName = "OYL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


