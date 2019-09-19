# import hashlib
str='https://www.emag.ro/placa-de-baza-asus-am4-socket-am4-crosshair-viii-hero/pd/D3H7M5BBM/'
# result = hashlib.md5(str.encode()) 
# #result=hashlib.md5(b'https://www.emag.ro/placa-de-baza-asus-am4-socket-am4-crosshair-viii-hero/pd/D3H7M5BBM/')
# valuep = result.hexdigest
# print(valuep)
# #print(hash('https://www.emag.ro/procesor-amd-ryzentm-9-3900x-70mb-4-6-ghz-cu-wraith-prism-cooler-100-100000023box/pd/DRY10RBBM/'))
# #print(hash('https://www.emag.ro/placa-de-baza-asus-am4-socket-am4-crosshair-viii-hero/pd/D3H7M5BBM/'))

import hashlib 
  
# initializing string 
#str = "GeeksforGeeks"
  
# encoding GeeksforGeeks using encode() 
# then sending to md5() 
result = hashlib.md5(str.encode()) 
  
# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of hash is : ", end ="") 
print(result.hexdigest()) 
print(type(result.hexdigest()))