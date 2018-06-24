from hashlib import sha256
from time import time

def contains_letter(s):
    alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
    for a in alphabet:
        if a in s.lower():
            return True
    return False

areacodes = []
npa_lines = open('areacodes.txt', 'r').read().splitlines()
# https://www.allareacodes.com/area_code_listings_by_state.htm
for L in npa_lines:
    words = L.split()
    for e in words:
        if contains_letter(e):
            continue
        areacodes.append(int(e[0:3]))

def nxx():
    for n in range (2,10):
        for x1 in range(10):
            for x2 in range(10):
                if x1 == x2 == 1:
                    continue
                yield str(n) + str(x1) + str(x2)

#### Main 

start_time = time()
counter = 0

try:
    for i in areacodes:
        for j in nxx():
            for k in range(10000):
                last4 = str(k).zfill(4)
                phone_num = str(i) + '-' + str(j) + '-' + last4
                h = sha256("617-232-9500".encode()).hexdigest()
                print(phone_num)
                print(h)
                counter += 1
except KeyboardInterrupt:
    pass

#### Reporting

end_time = time()
duration = end_time - start_time
rate = counter / duration
print()
print(counter, '\t\titems complete')
print(round(duration, 2), '\t\tsec')
print(round(rate,2), '\tper sec')
print()

n_npa = len(areacodes)
n_nxx = 0
for i in nxx():
    n_nxx += 1
total = n_npa * n_nxx * 10000
print(str(n_npa) + ' npa * ' + str(n_nxx) + ' nxx * ' + '10000 =')
print(total, '\titems to complete')
total_hours = total / rate / 60 / 60
print(round(total_hours, 2), '\t\thours')
