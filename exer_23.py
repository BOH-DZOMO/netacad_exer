from dataclasses import dataclass, field
def add(a: int, b: int) -> int:
    return a+b

print(add(5,6))

def process_users(users: list[dict]) -> list[str]:
    text = [y for x in users for y in x]
    return text
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
print(process_users(products))


@dataclass
class Product():
    name: str
    price: float
    stock: int = 0

def __post_init__(self):
    if self.price < 0:
        raise ValueError("Price cannot be negative")
    

@dataclass(frozen= True)
class Point():
    x: float
    y: float
    cordinates: list = field(default_factory=list)









