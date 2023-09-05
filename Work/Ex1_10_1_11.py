# mortgage.py
#
# Exercise 1.8

principal = 500000.0
rate = 0.05
payment = 2684.11
start_months = 0
end_months = 0
extra_paid = 0.0
total_paid = 0.0
months = 0

start_months = int(input('Enter Payment Start Month= '))
end_months = int(input('Enter Payment End Month= '))
extra_paid = float(input('Enter Extra Payment Amt= '))


while principal > 0:
    months += 1
    extra = 0
    if months >= start_months and months < end_months:
        extra = extra_paid

    if principal < (payment + extra):
        total_paid = total_paid + principal
        principal = 0
    else:
        principal = principal * (1 + rate/12) - (payment + extra)
        total_paid = total_paid + payment + extra

    print('Month ', months, '  Amount paid ',total_paid, ' Principal ', principal )

print('Total paid', total_paid)
print('Months', months)