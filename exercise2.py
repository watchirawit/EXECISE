import time
hours_work = float(input('Enter the number of hours worked:'))
hourly_pay_rate = float(input('Enter the hourly pay rate:'))
hours_work_over  = (hours_work - 40) *1.5
hours_all = hourly_pay_rate * 40

if hours_work > 40:
    print("The gross pay is $",hours_work_over*hourly_pay_rate+hours_all)
else:
    print("The gross pay is $",hourly_pay_rate*hours_work)
boss = time.time()
print((time.time()-boss)*1000)