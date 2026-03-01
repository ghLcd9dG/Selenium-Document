dic= {'Michael': 95, 'Bob': 75, 'Tracy': 85}
try:
    d=dic['test']
except KeyError as e:
    print(e)
print("print")