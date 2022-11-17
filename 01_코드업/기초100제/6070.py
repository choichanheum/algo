mon = input()

mon = int(mon)

'''
if (mon==12) | (mon==1) | (mon==2):
    print('winter')
elif (mon==3) | (mon==4) | (mon==5):
    print('spring')
elif (mon==6) | (mon==7) | (mon==8):
    print('summer')
elif (mon==9) | (mon==10) | (mon==11):
    print('fall')
'''

if mon//12==1:
    print('winter')
elif mon//3==1:
    print('spring')
elif mon//6==1:
    print('summer')
elif mon//9==1:
    print('fall')