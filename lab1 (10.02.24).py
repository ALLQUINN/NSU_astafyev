class Accountant:
    def give_salary(self, worker, spisok1, spisok2):
        work_result = worker.do_work(spisok1, spisok2)
        salary_amount = abs(sum(work_result)) * 100
        worker.take_salary(salary_amount)
        print(f"Salary given to {type(worker).__name__} is {salary_amount}$")
class Pupa:
    def __init__(self):
        self.salary_counter = 0

    def do_work(self, spisok1, spisok2):
        result = [x + y for x, y in zip(spisok1, spisok2)]
        print(f"Pupa: Element-wise sum of spisok1 and spisok2 is {result}")
        return result

    def take_salary(self, amount):
        self.salary_counter += amount
class Lupa:
    def __init__(self):
        self.salary_counter = 0

    def do_work(self, spisok1, spisok2):
        result = [x - y for x, y in zip(spisok1, spisok2)]
        print(f"Lupa: Element-wise difference of spisok1 and spisok2 is {result}")
        return result

    def take_salary(self, amount):
        self.salary_counter += amount

accountant = Accountant()
accountant.give_salary(Pupa(), [1, 2, 3], [4, 5, 6])
accountant.give_salary(Lupa(), [1, 2, 3], [4, 5, 6])