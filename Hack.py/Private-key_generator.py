#Bodex
import random   
import string  
import secrets  
num = 64  

res = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num))  

print( str(res))
