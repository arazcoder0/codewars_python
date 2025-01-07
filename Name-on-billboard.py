def billboard(name, price=30):
    length = len(name)
    
    total_cost = 0
    for _ in range(length):
        total_cost += price
    
    return total_cost
print(billboard("Jeong-Ho Aristotelis"))  
print(billboard("Jeong-Ho Aristotelis", 40))