import pandas as pd

class Category:
    def __init__(self, name, code) -> None:
        self.name = name
        self.code = code
        self.attr_names = []
        self.txs = []

    def add_attr_name(self, name):
        self.attr_names.append(name)

    def add_tx(self, tx):
        self.txs.append(tx)

    def to_df(self):
        data = []
        for tx in self.txs:
            data.append([
                tx.date,
                tx.in_or_out,
                tx.number,
                *[getattr(tx, name) for name in self.attr_names],
                tx.note
            ])
        return pd.DataFrame(data, columns=["日期", "IN/OUT", "数量", *self.attr_names, "备注"])