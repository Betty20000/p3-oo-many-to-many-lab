class Author:
    all=[]
    def __init__(self,name):
        self.name=name
        self.all.append(self)
    def contracts(self):
      return [contract for contract in Contract.all if contract.author == self]
    def books(self):
        written_by_author=self.contracts()
        related_books = set(contract.book for contract in written_by_author)
        return list(related_books)
    
    def sign_contract(self,book, date, royalties):
        new_contract = Contract(self,book,date,royalties)
        return new_contract
    def total_royalties(self):
        total = 0
        for contract in self.contracts():
            total += contract.royalties
        return total

class Book:
    all=[]
    def __init__(self,title):
        self.title=title
        self.all.append(self)
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    def authors(self):
        book_contracts = self.contracts()
        authors_list = [contract.author for contract in book_contracts]
        return authors_list 
    
class Contract:
    all=[]
    def __init__(self,author,book,date,royalties):
        self.author=author
        self.validate_author(author)
        self.book=book
        self.validate_book(book)
        self.date=date
        self.validate_date(date)
        self.royalties=royalties
        self.validate_royalties(royalties)
        self.all.append(self)

    def validate_author(self,author):
        if isinstance(author, Author):
            self.author=author
        else:
            raise Exception
    def validate_book(self,book):
        if isinstance(book, Book):
            self.date=book
        else:
            raise Exception
    def validate_date(self,date):
        if isinstance(date, str):
            self.date=date
        else:
            raise Exception
    def validate_royalties(self,royalties):
        if isinstance(royalties, int):
            self.royalties=royalties
        else:
            raise Exception
        
    def contracts_by_date(date):
        unsorted_contracts = [contract for contract in Contract.all if contract.date == date]
        sorted_contracts = sorted(unsorted_contracts, key=lambda contract: contract.date)
        return sorted_contracts