class PhoneBook:
    def __init__(self):
        self.book = {}

    def add(self, name, number):
        self.book.update({name:number})

    def lookup(self, name):
        return self.book[name]






