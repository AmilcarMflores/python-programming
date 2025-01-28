class Square:
  side = 8
  def area(self):
    return self.side * self.side

sq = Square()
print(sq.area()) # 64
print(Square.area(sq)) # 64
sq.side = 10
print(sq.area()) # 100