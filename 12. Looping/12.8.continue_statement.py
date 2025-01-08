from datetime import date, timedelta
today = date.today()
tomorrow = today + timedelta(days=1)
products = [
  {"sku": "1", "expiration_date": today, "price": 100.0},
  {"sku": "2", "expiration_date": tomorrow, "price": 50},
  {"sku": "3", "expiration_date": today, "price": 20},
]
for product in products:
  print("Processing sku", product["sku"])
  if product["expiration_date"] != today:
    continue
  product["price"] *= 0.8
  print("Sku", product["sku"], "price is now", product["price"])
  
# Output:
# Processing sku 1
# Sku 1 price is now 80.0
# Processing sku 2
# Processing sku 3
# Sku 3 price is now 16.0