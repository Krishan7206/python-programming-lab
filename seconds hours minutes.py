sec=int(input("enter the number of seconds"))
num_h=sec//3600
num_m= (sec-num_h*3600)//60
num_s=sec-(num_h*3600+num_m*60)
print(num_h)
print(num_m)
print(num_s)
