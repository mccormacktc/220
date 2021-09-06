"""
Name: Tyler McCormack

Problem:

Certificate of Authenticity:
I certify that this is my original work.
"""

def main():
# enter the annual interest rate: 15.84
    annualinterest = eval(input("Enter the annual interest rate in percentage form: "))
# enter the number of days in the billing cycle: 31
    daysincycle = eval(input("Enter the number of days in the billing cycle: "))
# enter the previous net balance: 850
    previousbalance = eval(input("Enter the previous net balance: "))
# enter the payment amount: 400
    paymentamount = eval(input("Enter the payment amount: "))
# enter the day of the billing cycle in which the payment was made: 20
    paymentday = eval(input("Enter the day of the billing cycle in which the payment was made: "))

    x = previousbalance * daysincycle
    y = paymentamount * (daysincycle - paymentday)
    z = x - y
    avgdailybalance = z / daysincycle
    monthlyintrate = annualinterest / 1200
    intcharge = avgdailybalance * monthlyintrate
    print(intcharge)

main()
