class tovar:  # класс хранения сообщения для рассылки
    def __init__(self, tovar):
        self.tovar = tovar

    def get_tovar(self):
        return self.tovar


rows = []
r = [5, 4, 7]
b = tovar(4)
for i in r:
    rows.append(i)
a = tovar(rows)
print(b.tovar)