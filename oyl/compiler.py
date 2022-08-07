from datetime import datetime
from unicodedata import category
from antlr4 import FileStream, CommonTokenStream
from oyl.antlr4.OYLLexer import OYLLexer
from oyl.antlr4.OYLParser import OYLParser
from oyl.antlr4.OYLVisitor import OYLVisitor
from oyl.category import Category
from oyl.date import date_to_string, string_to_date
from oyl.transaction import Transaction
from oyl.warehouse import WareHouse

class Compiler(OYLVisitor):
    def __init__(self) -> None:
        super().__init__()
        self.categories = {}
        self.date = datetime.now()

    def compile(self, tree):
        self.visit(tree)
        return WareHouse(self.categories)

    def visitRecords(self, ctx: OYLParser.RecordsContext):
        for c in ctx.category():
            self.visit(c)
        for c in ctx.record():
            self.visit(c)

    def visitCategory(self, ctx: OYLParser.CategoryContext):
        name = ctx.name().getText()
        code = ctx.code().getText()
        category = Category(name, code)
        for attr in ctx.attrname():
            category.add_attr_name(attr.getText())

        self.categories[name] = category

    def visitRecord(self, ctx: OYLParser.RecordContext):
        if not ctx.date() is None:
            self.date = string_to_date(ctx.date().getText())

        name = ctx.name().getText()
        number = int(ctx.number().getText())
        unit = ctx.unit().getText()
        tx = Transaction(self.date, name, number, unit)

        if not ctx.IN() is None:
            tx.in_or_out = Transaction.InOrOut.IN
        else:
            tx.in_or_out = Transaction.InOrOut.OUT

        category = self.categories[name]
        if ctx.attrvalue():
            for k, v in zip(category.attr_names, ctx.attrvalue()):
                setattr(tx, k, v.getText())
        else:
            for k in category.attr_names:
                setattr(tx, k, "")
        category.add_tx(tx)


def compile(filename):
    input_stream = FileStream(filename, encoding="utf-8")
    lexer = OYLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = OYLParser(stream)
    tree = parser.records()
    compiler = Compiler()
    warehouse = compiler.compile(tree)
    return warehouse
