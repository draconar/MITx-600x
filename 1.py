balance = 5000
annualInterestRate =0.18
monthlyPaymentRate = 0.02
totalAmtPaid = 0
for month in range(1,13):
    print ('Month: '+ str(month))
    ans = round((balance*monthlyPaymentRate),2)
    print ('Minimum monthly payment: '+ str(ans))
    ans1 = (annualInterestRate/12)*(balance - ans)
    RB = round(balance-(ans-ans1),2)
    print ('Remaining balance: ' + str(RB))
    balance = RB
    totalAmtPaid = round((totalAmtPaid + ans),2)
    
print ('Total paid: ' + str(totalAmtPaid))
print ('Remaining balance: ' + str(RB))
