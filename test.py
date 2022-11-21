class chance:
    def __init__(self, fuck, run, dave):
        self.fuck = fuck
        self.run = run
        self.dave = dave

    def se(self, val):



a = chance('fuck', 'run', 'dave')
b = a.__setattr__('fuck', 23)
print(a.fuck, a.run, a.dave)
print(b)

