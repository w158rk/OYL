# Generated from .\OYL.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,8,76,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,
        2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,5,0,25,8,0,10,0,12,0,28,
        9,0,1,1,1,1,1,1,1,1,5,1,34,8,1,10,1,12,1,37,9,1,1,1,1,1,1,2,3,2,
        42,8,2,1,2,1,2,1,2,1,2,1,2,5,2,49,8,2,10,2,12,2,52,9,2,1,2,1,2,3,
        2,56,8,2,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,
        1,9,1,9,1,10,1,10,1,10,0,0,11,0,2,4,6,8,10,12,14,16,18,20,0,2,1,
        0,5,6,2,0,4,4,7,8,70,0,26,1,0,0,0,2,29,1,0,0,0,4,41,1,0,0,0,6,59,
        1,0,0,0,8,61,1,0,0,0,10,63,1,0,0,0,12,65,1,0,0,0,14,67,1,0,0,0,16,
        69,1,0,0,0,18,71,1,0,0,0,20,73,1,0,0,0,22,25,3,2,1,0,23,25,3,4,2,
        0,24,22,1,0,0,0,24,23,1,0,0,0,25,28,1,0,0,0,26,24,1,0,0,0,26,27,
        1,0,0,0,27,1,1,0,0,0,28,26,1,0,0,0,29,30,5,1,0,0,30,31,3,6,3,0,31,
        35,3,8,4,0,32,34,3,10,5,0,33,32,1,0,0,0,34,37,1,0,0,0,35,33,1,0,
        0,0,35,36,1,0,0,0,36,38,1,0,0,0,37,35,1,0,0,0,38,39,5,2,0,0,39,3,
        1,0,0,0,40,42,3,12,6,0,41,40,1,0,0,0,41,42,1,0,0,0,42,43,1,0,0,0,
        43,44,7,0,0,0,44,45,3,6,3,0,45,46,3,14,7,0,46,50,3,16,8,0,47,49,
        3,20,10,0,48,47,1,0,0,0,49,52,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,
        0,51,55,1,0,0,0,52,50,1,0,0,0,53,54,5,2,0,0,54,56,3,18,9,0,55,53,
        1,0,0,0,55,56,1,0,0,0,56,57,1,0,0,0,57,58,5,2,0,0,58,5,1,0,0,0,59,
        60,5,8,0,0,60,7,1,0,0,0,61,62,5,8,0,0,62,9,1,0,0,0,63,64,5,8,0,0,
        64,11,1,0,0,0,65,66,5,4,0,0,66,13,1,0,0,0,67,68,5,7,0,0,68,15,1,
        0,0,0,69,70,5,8,0,0,70,17,1,0,0,0,71,72,5,8,0,0,72,19,1,0,0,0,73,
        74,7,1,0,0,74,21,1,0,0,0,6,24,26,35,41,50,55
    ]

class OYLParser ( Parser ):

    grammarFileName = "OYL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'category'", "';'", "<INVALID>", "<INVALID>", 
                     "'IN'", "'OUT'" ]

    symbolicNames = [ "<INVALID>", "CATEGORY", "SEMICOLON", "WS", "DATE", 
                      "IN", "OUT", "INTEGER", "ID" ]

    RULE_records = 0
    RULE_category = 1
    RULE_record = 2
    RULE_name = 3
    RULE_code = 4
    RULE_attrname = 5
    RULE_date = 6
    RULE_number = 7
    RULE_unit = 8
    RULE_note = 9
    RULE_attrvalue = 10

    ruleNames =  [ "records", "category", "record", "name", "code", "attrname", 
                   "date", "number", "unit", "note", "attrvalue" ]

    EOF = Token.EOF
    CATEGORY=1
    SEMICOLON=2
    WS=3
    DATE=4
    IN=5
    OUT=6
    INTEGER=7
    ID=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RecordsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def category(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OYLParser.CategoryContext)
            else:
                return self.getTypedRuleContext(OYLParser.CategoryContext,i)


        def record(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OYLParser.RecordContext)
            else:
                return self.getTypedRuleContext(OYLParser.RecordContext,i)


        def getRuleIndex(self):
            return OYLParser.RULE_records

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRecords" ):
                return visitor.visitRecords(self)
            else:
                return visitor.visitChildren(self)




    def records(self):

        localctx = OYLParser.RecordsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_records)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OYLParser.CATEGORY) | (1 << OYLParser.DATE) | (1 << OYLParser.IN) | (1 << OYLParser.OUT))) != 0):
                self.state = 24
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [OYLParser.CATEGORY]:
                    self.state = 22
                    self.category()
                    pass
                elif token in [OYLParser.DATE, OYLParser.IN, OYLParser.OUT]:
                    self.state = 23
                    self.record()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CategoryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CATEGORY(self):
            return self.getToken(OYLParser.CATEGORY, 0)

        def name(self):
            return self.getTypedRuleContext(OYLParser.NameContext,0)


        def code(self):
            return self.getTypedRuleContext(OYLParser.CodeContext,0)


        def SEMICOLON(self):
            return self.getToken(OYLParser.SEMICOLON, 0)

        def attrname(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OYLParser.AttrnameContext)
            else:
                return self.getTypedRuleContext(OYLParser.AttrnameContext,i)


        def getRuleIndex(self):
            return OYLParser.RULE_category

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCategory" ):
                return visitor.visitCategory(self)
            else:
                return visitor.visitChildren(self)




    def category(self):

        localctx = OYLParser.CategoryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_category)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(OYLParser.CATEGORY)
            self.state = 30
            self.name()
            self.state = 31
            self.code()
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OYLParser.ID:
                self.state = 32
                self.attrname()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 38
            self.match(OYLParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RecordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(OYLParser.NameContext,0)


        def number(self):
            return self.getTypedRuleContext(OYLParser.NumberContext,0)


        def unit(self):
            return self.getTypedRuleContext(OYLParser.UnitContext,0)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(OYLParser.SEMICOLON)
            else:
                return self.getToken(OYLParser.SEMICOLON, i)

        def IN(self):
            return self.getToken(OYLParser.IN, 0)

        def OUT(self):
            return self.getToken(OYLParser.OUT, 0)

        def date(self):
            return self.getTypedRuleContext(OYLParser.DateContext,0)


        def attrvalue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OYLParser.AttrvalueContext)
            else:
                return self.getTypedRuleContext(OYLParser.AttrvalueContext,i)


        def note(self):
            return self.getTypedRuleContext(OYLParser.NoteContext,0)


        def getRuleIndex(self):
            return OYLParser.RULE_record

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRecord" ):
                return visitor.visitRecord(self)
            else:
                return visitor.visitChildren(self)




    def record(self):

        localctx = OYLParser.RecordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_record)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OYLParser.DATE:
                self.state = 40
                self.date()


            self.state = 43
            _la = self._input.LA(1)
            if not(_la==OYLParser.IN or _la==OYLParser.OUT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 44
            self.name()
            self.state = 45
            self.number()
            self.state = 46
            self.unit()
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OYLParser.DATE) | (1 << OYLParser.INTEGER) | (1 << OYLParser.ID))) != 0):
                self.state = 47
                self.attrvalue()
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 53
                self.match(OYLParser.SEMICOLON)
                self.state = 54
                self.note()


            self.state = 57
            self.match(OYLParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(OYLParser.ID, 0)

        def getRuleIndex(self):
            return OYLParser.RULE_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName" ):
                return visitor.visitName(self)
            else:
                return visitor.visitChildren(self)




    def name(self):

        localctx = OYLParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(OYLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(OYLParser.ID, 0)

        def getRuleIndex(self):
            return OYLParser.RULE_code

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCode" ):
                return visitor.visitCode(self)
            else:
                return visitor.visitChildren(self)




    def code(self):

        localctx = OYLParser.CodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_code)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(OYLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrnameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(OYLParser.ID, 0)

        def getRuleIndex(self):
            return OYLParser.RULE_attrname

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttrname" ):
                return visitor.visitAttrname(self)
            else:
                return visitor.visitChildren(self)




    def attrname(self):

        localctx = OYLParser.AttrnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attrname)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(OYLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATE(self):
            return self.getToken(OYLParser.DATE, 0)

        def getRuleIndex(self):
            return OYLParser.RULE_date

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDate" ):
                return visitor.visitDate(self)
            else:
                return visitor.visitChildren(self)




    def date(self):

        localctx = OYLParser.DateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_date)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(OYLParser.DATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(OYLParser.INTEGER, 0)

        def getRuleIndex(self):
            return OYLParser.RULE_number

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = OYLParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(OYLParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(OYLParser.ID, 0)

        def getRuleIndex(self):
            return OYLParser.RULE_unit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnit" ):
                return visitor.visitUnit(self)
            else:
                return visitor.visitChildren(self)




    def unit(self):

        localctx = OYLParser.UnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_unit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(OYLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NoteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(OYLParser.ID, 0)

        def getRuleIndex(self):
            return OYLParser.RULE_note

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNote" ):
                return visitor.visitNote(self)
            else:
                return visitor.visitChildren(self)




    def note(self):

        localctx = OYLParser.NoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_note)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(OYLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(OYLParser.ID, 0)

        def INTEGER(self):
            return self.getToken(OYLParser.INTEGER, 0)

        def DATE(self):
            return self.getToken(OYLParser.DATE, 0)

        def getRuleIndex(self):
            return OYLParser.RULE_attrvalue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttrvalue" ):
                return visitor.visitAttrvalue(self)
            else:
                return visitor.visitChildren(self)




    def attrvalue(self):

        localctx = OYLParser.AttrvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_attrvalue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OYLParser.DATE) | (1 << OYLParser.INTEGER) | (1 << OYLParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





