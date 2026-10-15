products = [
    {"name":"Notebook","price":120,"quantity":3},
    {"name":"Pen","price":20,"quantity":5},
    {"name":"USB Drive","price":850,"quantity":2},
    {"name":"Mouse","price":650,"quantity":1}
]
total = 0
highest_cost = 0
highest_product = ""

for product in products:
    cost=product["price"]*product["quantity"]
    print(product["name"],"Total Line:",cost)
    total=total+cost

    if cost>highest_cost:
        highest_cost=cost
        highest_product=product["name"]

print("Total inventory value:", total)
print("Highest-value product:", highest_product)
print("Highest line total:", highest_cost)