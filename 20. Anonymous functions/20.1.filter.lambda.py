# # filter.regular
# def is_multiple_of_five(n):
#   return not n % 5
# def get_multiples_of_five(n):
#   return list(filter(is_multiple_of_five, range(n)))

def get_multiples_of_five(n):
  return list(filter(lambda k: not k % 5, range(n)))

print(get_multiples_of_five(50)) # [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]