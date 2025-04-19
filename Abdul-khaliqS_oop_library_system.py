class LibraryBook:
     def __init__(self, title, status ="Available"):
          self.title = title
          self.__status = status

     def get_status(self):
          return self.__status

     def borrow_book(self):
          self.__status = "Checked Out"
     
     def return_book(self):
          self.__status = "Available"


book = LibraryBook("48 Laws of Power")

book.borrow_book()

book.return_book()
print(book.get_status())

