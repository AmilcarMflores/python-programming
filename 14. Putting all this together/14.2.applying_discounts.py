# # Está bien este código pero viola el principio DRY
# customers = [
#   dict(id=1, total=200, coupon_code="F20"),
#   dict(id=2, total=150, coupon_code="P30"),
#   dict(id=3, total=100, coupon_code="P50"),
#   dict(id=4, total=110, coupon_code="F15"),
# ]
# for customer in customers:
#   match customer["coupon_code"]:
#     case "F20":
#       customer["discount"] = 20.0
#     case "F15":
#       customer["discount"] = 15.0
#     case "P30":
#       customer["discount"] = customer["total"] * 0.3
#     case "P50":
#       customer["discount"] = customer["total"] * 0.5
#     case _:
#       customer["discount"] = 0.0
# for customer in customers:
#   print(customer["id"], customer["total"], customer["discount"])
  
# Un poco mejor
customers = [
  dict(id=1, total=200, coupon_code="F20"),
  dict(id=2, total=150, coupon_code="P30"),
  dict(id=3, total=100, coupon_code="P50"),
  dict(id=4, total=110, coupon_code="F15"),
]
discounts = {
  "F20": (0.0, 20.0),
  "P30": (0.3, 0.0),
  "P50": (0.5, 0.0),
  "F15": (0.0, 15.0),
}
for customer in customers:
  code = customer["coupon_code"]
  # dict.get(key, default) -> default es un valor que nosotros ponemos, si es que no encuentra el key
  percent, fixed = discounts.get(code, (0.0, 0.0))
  customer["discount"] = percent * customer["total"] + fixed
for customer in customers:
  print(customer["id"], customer["total"], customer["discount"])

# 1 200 20.0
# 2 150 45.0
# 3 100 50.0
# 4 110 15.0