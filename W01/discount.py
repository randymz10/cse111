import datetime


subtotal = float(input('Please enter the subtotal: '));
current_day = datetime.datetime.now();
day_of_week = current_day.weekday();
discount = 0;
sales_tax = subtotal * 0.06;

if day_of_week == 2 or day_of_week == 1:
    discount = subtotal * 0.1;

total = subtotal + discount + sales_tax;

print(f'Sales tax amount: {sales_tax}');
print(f'Total {total}');


