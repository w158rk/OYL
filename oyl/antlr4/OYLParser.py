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
        4,1,10,85,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,5,0,24,8,0,10,0,12,0,27,
        9,0,1,0,5,0,30,8,0,10,0,12,0,33,9,0,1,1,1,1,1,1,1,1,5,1,39,8,1,10,
        1,12,1,42,9,1,1,1,1,1,1,2,3,2,47,8,2,1,2,1,2,1,2,1,2,1,2,5,2,54,
        8,2,10,2,12,2,57,9,2,1,2,1,2,3,2,61,8,2,1,2,1,2,1,3,1,3,1,4,1,4,
        1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,
        1,10,0,0,11,0,2,4,6,8,10,12,14,16,18,20,0,2,1,0,7,8,1,0,9,10,79,
        0,25,1,0,0,0,2,34,1,0,0,0,4,46,1,0,0,0,6,64,1,0,0,0,8,66,1,0,0,0,
        10,68,1,0,0,0,12,70,1,0,0,0,14,76,1,0,0,0,16,78,1,0,0,0,18,80,1,
        0,0,0,20,82,1,0,0,0,22,24,3,2,1,0,23,22,1,0,0,0,24,27,1,0,0,0,25,
        23,1,0,0,0,25,26,1,0,0,0,26,31,1,0,0,0,27,25,1,0,0,0,28,30,3,4,2,
        0,29,28,1,0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,1,1,
        0,0,0,33,31,1,0,0,0,34,35,5,1,0,0,35,36,3,6,3,0,36,40,3,8,4,0,37,
        39,3,10,5,0,38,37,1,0,0,0,39,42,1,0,0,0,40,38,1,0,0,0,40,41,1,0,
        0,0,41,43,1,0,0,0,42,40,1,0,0,0,43,44,5,2,0,0,44,3,1,0,0,0,45,47,
        3,12,6,0,46,45,1,0,0,0,46,47,1,0,0,0,47,48,1,0,0,0,48,49,7,0,0,0,
        49,50,3,6,3,0,50,51,3,14,7,0,51,55,3,16,8,0,52,54,3,20,10,0,53,52,
        1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,60,1,0,0,0,
        57,55,1,0,0,0,58,59,5,2,0,0,59,61,3,18,9,0,60,58,1,0,0,0,60,61,1,
        0,0,0,61,62,1,0,0,0,62,63,5,2,0,0,63,5,1,0,0,0,64,65,5,10,0,0,65,
        7,1,0,0,0,66,67,5,9,0,0,67,9,1,0,0,0,68,69,5,10,0,0,69,11,1,0,0,
        0,70,71,5,5,0,0,71,72,5,3,0,0,72,73,5,6,0,0,73,74,5,3,0,0,74,75,
        5,6,0,0,75,13,1,0,0,0,76,77,5,9,0,0,77,15,1,0,0,0,78,79,5,10,0,0,
        79,17,1,0,0,0,80,81,5,10,0,0,81,19,1,0,0,0,82,83,7,1,0,0,83,21,1,
        0,0,0,6,25,31,40,46,55,60
    ]

class OYLParser ( Parser ):

    grammarFileName = "OYL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'category'", "'.'", "'-'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'IN'", "'OUT'" ]

    symbolicNames = [ "<INVALID>", "CATEGORY", "DOT", "DASH", "WS", "YEAR", 
                      "NUM2", "IN", "OUT", "INTEGER", "ID" ]

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
    DOT=2
    DASH=3
    WS=4
    YEAR=5
    NUM2=6
    IN=7
    OUT=8
    INTEGER=9
    ID=10

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
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OYLParser.CATEGORY:
                self.state = 22
                self.category()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OYLParser.YEAR) | (1 << OYLParser.IN) | (1 << OYLParser.OUT))) != 0):
                self.state = 28
                self.record()
                self.state = 33
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


        def DOT(self):
            return self.getToken(OYLParser.DOT, 0)

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
            self.state = 34
            self.match(OYLParser.CATEGORY)
            self.state = 35
            self.name()
            self.state = 36
            self.code()
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OYLParser.ID:
                self.state = 37
                self.attrname()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 43
            self.match(OYLParser.DOT)
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


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(OYLParser.DOT)
            else:
                return self.getToken(OYLParser.DOT, i)

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
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OYLParser.YEAR:
                self.state = 45
                self.date()


            self.state = 48
            _la = self._input.LA(1)
            if not(_la==OYLParser.IN or _la==OYLParser.OUT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 49
            self.name()
            self.state = 50
            self.number()
            self.state = 51
            self.unit()
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==OYLParser.INTEGER or _la==OYLParser.ID:
                self.state = 52
                self.attrvalue()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 58
                self.match(OYLParser.DOT)
                self.state = 59
                self.note()


            self.state = 62
            self.match(OYLParser.DOT)
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
            self.state = 64
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

        def INTEGER(self):
            return self.getToken(OYLParser.INTEGER, 0)

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
            self.state = 66
            self.match(OYLParser.INTEGER)
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
            self.state = 68
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

        def YEAR(self):
            return self.getToken(OYLParser.YEAR, 0)

        def DASH(self, i:int=None):
            if i is None:
                return self.getTokens(OYLParser.DASH)
            else:
                return self.getToken(OYLParser.DASH, i)

        def NUM2(self, i:int=None):
            if i is None:
                return self.getTokens(OYLParser.NUM2)
            else:
                return self.getToken(OYLParser.NUM2, i)

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
            self.state = 70
            self.match(OYLParser.YEAR)
            self.state = 71
            self.match(OYLParser.DASH)
            self.state = 72
            self.match(OYLParser.NUM2)
            self.state = 73
            self.match(OYLParser.DASH)
            self.state = 74
            self.match(OYLParser.NUM2)
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
            self.state = 76
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
            self.state = 78
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
            self.state = 80
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
            self.state = 82
            _la = self._input.LA(1)
            if not(_la==OYLParser.INTEGER or _la==OYLParser.ID):
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





