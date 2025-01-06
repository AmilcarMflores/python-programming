# d = {}
# d["age"] = d.get("age", 0) + 1
# d # {'age': 1}

# d = {"age": 39}
# d["age"] = d.get("age", 0) + 1
# print(d) # {'age': 40}

from collections import defaultdict
dd = defaultdict(int)
dd["age"] += 1
print(dd) # defaultdict(<class 'int'>, {'age': 1})

dd["age"] = 39
dd["age"] += 1
print(dd) # defaultdict(<class 'int'>, {'age': 40})