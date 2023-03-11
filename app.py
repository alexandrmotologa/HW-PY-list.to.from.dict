salary_l = [1500, 1800, 1400]
months = ["March", "April", "May"]
salary_d = {}

for month, salary in zip(months, salary_l):
    salary_d[month] = salary

print(salary_d)