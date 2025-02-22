class Book:
  def __init__(self, title, publisher, pages):
    self.title = title
    self.publisher = publisher
    self.pages = pages
    
class Ebook(Book):
  def __init__(self, title, publisher, pages, format_):
    super().__init__(title, publisher, pages)
    # Otra forma de hacerlo es:
    # super(Ebook, self).__init__(title, publisher, pages)
    self.format_ = format_

ebook = Ebook("The Catcher in the Rye", "Little, Brown and Company", 288, "PDF")
print(ebook.title)
print(ebook.publisher)
print(ebook.pages)
print(ebook.format_)