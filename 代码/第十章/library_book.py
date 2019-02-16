
class book(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"Dict object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def get_page(self):
        if self.page <= 60:
            return "短篇"
        elif self.page <= 150:
            return "中篇"
        elif self.page > 150:
            return "长篇"