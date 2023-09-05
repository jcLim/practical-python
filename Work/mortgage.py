# mortgage.py
#
# Exercise 1.8

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0

while principal > 0:
    months += 1
    extra = 0
    if months < 13 :
        extra = 1000

    principal = principal * (1 + rate/12) - (payment + extra)
    total_paid = total_paid + payment + extra

print('Total paid', total_paid)
print('Months', months)