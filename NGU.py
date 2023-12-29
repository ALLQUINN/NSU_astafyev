#1
num = float(input())

if num > 28: print('ЖАРКО')
elif num < 15.5: print('ХОЛОДНО')
else: print('НОРМАЛЬНО')

#2
count = int(input())
found = False

for i in range(count):
   txt = input()
   txt = txt.lower()
   t = txt.find('кот')
   if t != -1:
       found = True

if found == True: print('МЯУ')
else: print('НЕТ')

#3
st = ''
t = True
st = input()
if st != 'стоп':
    l_max = len(st)
    l_min = len(st)
    max_word = st
    min_word = st
else: l_max = 0; l_min = 0

while t == True:
    if st != 'стоп':
        st = input()
        st = st.lower()
        if len(st) > l_max: l_max = len(st); max_word = st
        if len(st) < l_min: l_min = len(st); min_word = st
    if st == 'стоп':
        t = False
        if len(set(min_word) - set(max_word)) == 0: print('ДА')
        else: print('НЕТ')

# 4
count = int(input())
a = []

for i in range(count):
   pur = input()
   a.append(pur)

print(*a, sep = '\n')

#5
str = input()
a = ''
for i in range(len(str)):
    a = a + (str[i]*2)
print(a)

# 6
def greet():
    name = input()
    surname = input()
    greeting = f'Здравствуйте, {name} {surname}.'
    return greeting

print(greet())

#7
class LittleBell():
    def sound(self):
        print('ding')

bell = LittleBell()
bell.sound()
