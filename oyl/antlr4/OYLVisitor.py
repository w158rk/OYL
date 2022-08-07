# Generated from .\OYL.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .OYLParser import OYLParser
else:
    from OYLParser import OYLParser

# This class defines a complete generic visitor for a parse tree produced by OYLParser.

class OYLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by OYLParser#records.
    def visitRecords(self, ctx:OYLParser.RecordsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OYLParser#category.
    def visitCategory(self, ctx:OYLParser.CategoryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OYLParser#record.
    def visitRecord(self, ctx:OYLParser.RecordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OYLParser#name.
    def visitName(self, ctx:OYLParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OYLParser#code.
    def visitCode(self, ctx:OYLParser.CodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OYLParser#attrname.
    def visitAttrname(self, ctx:OYLParser.AttrnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OYLParser#date.
    def visitDate(self, ctx:OYLParser.DateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OYLParser#number.
    def visitNumber(self, ctx:OYLParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OYLParser#unit.
    def visitUnit(self, ctx:OYLParser.UnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OYLParser#note.
    def visitNote(self, ctx:OYLParser.NoteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OYLParser#attrvalue.
    def visitAttrvalue(self, ctx:OYLParser.AttrvalueContext):
        return self.visitChildren(ctx)



del OYLParser