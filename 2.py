balance = 10000
annualInterestRate =0.18


monthlyInterestRate = annualInterestRate/12
lower = balance/12
upper = (balance*(1+monthlyInterestRate)**12)/12
b = balance
lowestpayment = 0
epsilon = 0.01
while abs(b)>=epsilon:
    b = balance
    lowestpayment = (lower+upper)/2
    for month in range(1,13):
        b = (b-lowestpayment)*(1+monthlyInterestRate)
    if b < 0:
        upper = lowestpayment
    else:
        lower = lowestpayment
print ('Lowest Payment: ' + str(round(lowestpayment,2)))
