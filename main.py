
#!/bin/python

oP = 10 ** -4 # change cracking (lifetime password after it'll change to new one)
oT = 12
oV = 100 # for 1 minute/oV passwords

# 60 = seconds in minutes
# 24 = hour in day and
# oT = doy in week
oV_for_Week = oV * 60 * 24 * oT

# low limit
dS = oV_for_Week / oP

L = 8 # password length
A = len('abcdefghijklmnopqrstuvwxyz')  # 26

print(f'max possible combination {A ** L} . Can check for this time {dS} ')
if  dS <=  A ** L  :
    print('Can crack . need to change password')
else:
    print('Good password . Sturdy password ')

crack_probability = (dS / (A ** L)) * 100
print(f"Crack probability: {crack_probability:.2f}%")