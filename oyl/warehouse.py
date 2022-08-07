class WareHouse:
    def __init__(self, categories):
        self.categories = categories

    def to_df_map(self):
        ret = {}
        for k,v in self.categories.items():
            ret[k] = v.to_df()
        return ret
