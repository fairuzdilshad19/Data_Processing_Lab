products=[
    {"name":"Bag","price":1200,"quantity":1},
    {"name":"Mouse","price":650,"quantity":2},
    {"name":"Keyboard","price":800,"quantity":1},
    {"name":"Pen","price":20,"quantity":5}
]
def apply_discount(total):
    if total>=2000:
        total=total-(total*10 /100)
    return total

total=0
for product in products:
    cost=product["price"]*product["quantity"]
    total=total+cost

    print(product["name"],"Cost:",cost)

print("Total before discount:", total)
print("Total after discount:", apply_discount(total))