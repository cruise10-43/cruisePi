import json
import math

y = {'age': 33, 'height': 170, 'bmi': 22}
f = open("textjson.txt", "w")
json.dump(y, f)
y
list_a = ['dog', 'cat', 'tiger']
for s in list_a[:]:
    if len(s) == 5:
        list_a.append(s)
list_a

if __name__ == '__main__':
    print(math.sqrt(3))
    print(math.pow(2, 3))
    print(math.e)
    print(math.pi)
