shop = ["shirt", "pant", "trousers", "track pants", "shorts"]
new_shop = shop
shop+= ["sherwani"]
print(id(shop))
print(id(new_shop))
for things in shop:
    print(things)

a = b = c = new_shop
print("adding garments")
a.append("garments")
new_shop.append("t shirts")
print(b)
print(c)