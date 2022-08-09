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
        4,0,8,62,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,2,1,
        2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,
        4,1,5,1,5,1,5,1,5,1,6,4,6,52,8,6,11,6,12,6,53,1,7,1,7,5,7,58,8,7,
        10,7,12,7,61,9,7,0,0,8,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,1,0,4,
        3,0,9,10,12,13,32,32,1,0,48,57,6,0,9,10,13,13,32,32,45,45,48,57,
        59,59,4,0,9,10,13,13,32,32,59,59,63,0,1,1,0,0,0,0,3,1,0,0,0,0,5,
        1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,
        0,0,0,1,17,1,0,0,0,3,26,1,0,0,0,5,28,1,0,0,0,7,32,1,0,0,0,9,43,1,
        0,0,0,11,46,1,0,0,0,13,51,1,0,0,0,15,55,1,0,0,0,17,18,5,99,0,0,18,
        19,5,97,0,0,19,20,5,116,0,0,20,21,5,101,0,0,21,22,5,103,0,0,22,23,
        5,111,0,0,23,24,5,114,0,0,24,25,5,121,0,0,25,2,1,0,0,0,26,27,5,59,
        0,0,27,4,1,0,0,0,28,29,7,0,0,0,29,30,1,0,0,0,30,31,6,2,0,0,31,6,
        1,0,0,0,32,33,7,1,0,0,33,34,7,1,0,0,34,35,7,1,0,0,35,36,7,1,0,0,
        36,37,5,45,0,0,37,38,7,1,0,0,38,39,7,1,0,0,39,40,5,45,0,0,40,41,
        7,1,0,0,41,42,7,1,0,0,42,8,1,0,0,0,43,44,5,73,0,0,44,45,5,78,0,0,
        45,10,1,0,0,0,46,47,5,79,0,0,47,48,5,85,0,0,48,49,5,84,0,0,49,12,
        1,0,0,0,50,52,7,1,0,0,51,50,1,0,0,0,52,53,1,0,0,0,53,51,1,0,0,0,
        53,54,1,0,0,0,54,14,1,0,0,0,55,59,8,2,0,0,56,58,8,3,0,0,57,56,1,
        0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,16,1,0,0,0,61,
        59,1,0,0,0,3,0,53,59,1,6,0,0
    ]

class OYLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    CATEGORY = 1
    SEMICOLON = 2
    WS = 3
    DATE = 4
    IN = 5
    OUT = 6
    INTEGER = 7
    ID = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'category'", "';'", "'IN'", "'OUT'" ]

    symbolicNames = [ "<INVALID>",
            "CATEGORY", "SEMICOLON", "WS", "DATE", "IN", "OUT", "INTEGER", 
            "ID" ]

    ruleNames = [ "CATEGORY", "SEMICOLON", "WS", "DATE", "IN", "OUT", "INTEGER", 
                  "ID" ]

    grammarFileName = "OYL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None

