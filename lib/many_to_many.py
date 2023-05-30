from datetime import datetime
class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    # This method should return a list of related contracts
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    #This method should return a list of related books using the 
    # Contract class as an intermediary.
    def books(self):
        return [contract.book for contract in self.contracts()]

    #This method should create and return a new Contract object 
    # between the author and the specified book with the specified date and royalties
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    #This method should return the total amount of royalties 
    # that the author has earned from all of their contracts.
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])
    
    


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]
    
    def add_contract(self, author):
        Contract(self, author)


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.contract_date = datetime.now()
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("invalid")
        self._author = value

    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("invalid")
        self._book = value

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("invalid")
        self._date = value

    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("invalid")
        self._royalties = value

    #This method should return all contracts that have the 
    # same date as the date passed into the method.
    @classmethod
    def contracts_by_date(cls):
        return sorted(cls.all, key=lambda contract: contract.date)