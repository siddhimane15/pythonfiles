slab1 =250000
slab2 =500000
slab3 =1000000
income=int(input('enter your income:'))
if income>=1000001:
    print("taxable income",income-250000)
    taxable = income-25000
    print("tax applied",(taxable-slab1-slab2)*0.3+(slab2)*0.1+(slab1)*0.05)
elif income>=500001:
    print("taxable income",income-250000)
    taxable=income-25000
    print("tax applied",(taxable-slab1)*0.1+(slab1)*0.05)
elif income >=250001:
     print("taxable income",income-25000)
     prinr("tax applied",(income-25000)*0.05)
else:
    print("no taxable income")