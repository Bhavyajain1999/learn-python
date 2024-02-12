ctc = int((input('please enter your CTC')))
HRA = 0.1*ctc
DA = 0.05*ctc
PF = 0.03*ctc

if(ctc < 500000):
    TD = 0*ctc
elif(ctc < 1000000):
    TD = 0.1*ctc
elif(ctc < 2000000):
    TD = 0.2*ctc     
else:
    TD = 0.3*ctc

inhand_salary = (ctc - HRA -DA - PF - TD)/12
print(inhand_salary)           