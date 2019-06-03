import ast

with open('Remembers.txt', 'r') as f:
    Remembers = ast.literal_eval(f.read())


x = Remembers["brand"]
print(x)
