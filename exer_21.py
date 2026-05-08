products = [{"name":  "table chair", "price": 67_000,"in_stock": 90},
            {"name":  "plate", "price": 7000,"in_stock": 56},
            {"name":  "office table", "price": 67_000,"in_stock": 30},
            {"name":  "dell laptops", "price": 150_000,"in_stock": 60},
            {"name":  "hp laptops", "price": 170_000,"in_stock": 56},
            {"name":  "chargers", "price": 67_000,"in_stock": 0},
            {"name":  "pipes", "price": 7_000,"in_stock": 20},
            {"name":  "alcohol", "price": 10_000,"in_stock": 106},
            {"name":  "lamps", "price": 7_000,"in_stock": 0},
            {"name":  "books", "price": 8_000,"in_stock": 69},
            {"name":  "keyboards", "price": 5000,"in_stock": 26},
            {"name":  "tv sets", "price": 200_000,"in_stock": 0}
            
            ]

def apply_dis(y):
    x=y.copy()
    x["price"] = x.get("price")-(x.get("price")*0.1)
    return x
filtered_products = list(filter(lambda x: x["in_stock"]>0, products))
discount = list(map(apply_dis,products))
sorted_products  = sorted(products,key=lambda x: x["price"])
sorted_products_rev  = sorted(products,key=lambda x: x["price"], reverse=True)
sorted_stock = sorted(products,key=lambda x: (x["in_stock"] == 0,x["price"]))

print()
print(*sorted_products_rev, sep="\n")
print()
print(*sorted_stock, sep="\n")
print()
print(*discount, sep="\n")