#1
count = int(input())
a = []
for i in range(count):
    a.append(input())
a = sorted(a, reverse=True)
print(*a, sep = '\n')
#2
def process_logs(count, log_lines):
    for log_line in log_lines:
        if log_line[:4] == '####':
            continue
        if log_line[:2] == '%%':
            print(log_line[2:])
        else:
            print(log_line)
count = int(input())
log_lines = []

for i in range(count):
    log_line = input()
    log_lines.append(log_line)
process_logs(count, log_lines)
#3
count = int(input())
a = []
sum_range = 0
for _ in range(count):
    a.append(int(input()))
first = int(input())
last = int(input())
for num in a[first - 1:last]:
    sum_range += num
print(sum_range)
#4
s = 'Сидоров 3, Смирнова 5, Самойкин 4, Емельянов 2, Кац 5, Вдовиченко 5, Северин 4, Субботкин 5'
n = 3
def Artek(s, n):
    s = s.split(', ')
    stdnt_dict = {}
    for i in s:
        name, grade = i.split()
        stdnt_dict[name] = int(grade)
    sorted_stdnt = sorted(stdnt_dict.items(), key=lambda x: x[1], reverse=True)
    for name, grade in sorted_stdnt[:n]:
        print(name)
Artek(s, n)
#5
def password_level():
    import re
    user_password = input()
    confirm_user_password = input()

    if user_password == confirm_user_password:
        if len(user_password) < 8:
            print("Недопустимый пароль")
        if not re.search("[a-z]", user_password) or not re.search("[A-Z]", user_password):
            print("Ненадежный пароль")
        if not re.search("[0-9]", user_password):
            print("Ненадежный пароль")
        if not re.search("[@#$%&*().,-_+]", user_password):
            print("Ненадежный пароль")
        print("Надежный пароль")
    print("Пароли не совпадают")
password_level()