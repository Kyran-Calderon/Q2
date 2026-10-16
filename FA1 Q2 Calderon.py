class Anthology:
    name = str
    author = str
    def __init__ (self, title, author):
        self.title = title
        self.author = author
    def get_title(self):
        return self.title
    def get_author(self):
        return self.author

class Book(Anthology):
    def numpage(self):
        numpage = 0
    def set_numpage(self, numpage):
        if numpage > 0:
            self.numpage = numpage
        else:
            print("ERROR: The number of pages must be a positive number.")
    def get_numpage(self):
        return self.numpage

class Magazine(Anthology):
    def isnum(self):
        isnum = 0
    def set_isnum(self, isnum):
        if isnum > 0:
            self.isnum = isnum
        else:
            print("ERROR: The issue number must be a positive number.")
    def get_isnum(self):
        return self.isnum

Book1 = Book("Animal Farm", "George Orwell")
Book1.set_numpage(100)
print("Book title: ", Book1.title)
print("Book Author: ", Book1.author)
print("Number of pages: ", Book1.get_numpage())

Book2 = Book("Diary of a Young Girl", "Anne Frank")
Book2.set_numpage(0)
print("Book title: ", Book2.title)
print("Book Author: ", Book2.author)
print("Number of pages: ", Book2.get_numpage())

Magazine1 = Magazine("Skibidi Toilet", "Vice Ganda")
Magazine1.set_isnum(-1)
print("Magazine title: ", Magazine1.title)
print("Magazine author: ", Magazine1.author)
print("Issue number: ", Magazine1.get_isnum())

Magazine2 = Magazine("The Cure", "Robert Smith")
Magazine2.set_isnum(1979)
print("Magazine title: ", Magazine2.title)
print("Magazine author: ", Magazine2.author)
print("Issue number: ", Magazine2.get_isnum())
