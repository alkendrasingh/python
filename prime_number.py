a=int(input("Enter your number:"))
if a>1:
  for i in range(2,a//2):
     if(a%i)==0:
      print(a,"not prime")
      break
  else:
      print(a,"prime")
else:
    print(1,"is a prime")
            
      
      
