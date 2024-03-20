class Book:
    def __init__(self, b_name, authr):
        self.book_name = b_name
        self.author = authr


class Members:
    def __init__(self, name, place, borrow_date, return_date):
        self.name = name
        self.place = place
        self.borrow_date = borrow_date
        self.return_date = return_date


def result(b_name, authr, name, borrow_date, return_date):
    print("The book", b_name, "written by", authr, "is taken by", name, "on", borrow_date, "and return it on",
          return_date)


class Transactions:
    def __init__(self, member, book):
        self.member = member
        self.book = book


book_obj = Book("oliver twist", "charles dicken")
mem_obj = Members("anu", "india", "02/feb/2022", "12/feb/2022")
t_obj = Transactions(mem_obj, book_obj)
result(t_obj.book.book_name,
       t_obj.book.author,
       t_obj.member.name,
       t_obj.member.borrow_date,
       t_obj.member.return_date)
