from datetime import *

print(datetime.now().isoweekday())

with open('visitors.txt', 'r') as file:
    if '12345678' in file:
        print('yes')
