
even = [i for i in range(100) if i%2== 0]

word_len = {i: len(i)  for i in ["word","wow","crazy","going","dirty","lety"]}

unique = {f"{i}-{j}" for i in ["word","wow","crazy","going","dirty","lety"] for j in i if i.count(j) == 1 }
# unique = set()
# for i in ["word","wow","crazy","going","dirty","lety"]:
#     for j in i:
#         if i.count(j) == 1:
#             unique.add(f"{i}-{j}")
#             break

print(unique)


flatten = [i for j in [[1,2],[3,4],[5,6]] for i in j]
print(flatten)
age = 20
label = 'adult' if age >= 18 else 'minor'
print(label)

keys = ["user", "total", "page"]
values = [["word", "wow", "crazy", "going", "dirty", "lety"], 20, 1]

# This assigns the ENTIRE list of values to every single key
context = {i:j  for i, j in zip(keys,values)}

print(context)
