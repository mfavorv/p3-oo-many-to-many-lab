class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
       return [contract for contract in Contract.all if contract.author == self ]
     
    def books(self):
         return [contract.book for contract in Contract.all if contract.author == self]
     
    def sign_contract(self,book, date, royalties):
        contract  = Contract(self,book, date, royalties)
        return contract
 
    def total_royalties(self):
        royalties = [contract.royalties for contract in  self.contracts()]
        return sum(royalties)
        pass


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
       return [contract for contract in Contract.all if contract.book == self ]
    
    def authors(self):
       return [contract.author for contract in Contract.all if contract.book == self ]
     
     
pass

class Contract:
    all =[]

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise TypeError("author is not an instance of Author")

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise TypeError("book is not an instance of Book")

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self._date = date
        else:
            raise TypeError("date is not a string")

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, royalties):
        if isinstance(royalties, int):
            self._royalties = royalties
        else:
            raise TypeError("royalties is not an integer")
        
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
pass