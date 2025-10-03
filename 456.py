fruit = ['apple', 'orange', 'lemon', 'berry', 'mango']
price = [30, 20, 60, 70, 60]
print(len(fruit))
test=enumerate(zip(fruit,price))
# print(test[0])
for i in test:
    print(i)

#     print(i)
# print(zip(fruit, price))
# for i, (f, p) in enumerate(zip(fruit, price)):