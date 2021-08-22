number = int(input())
stars = []
for i in range (number):
   if i < number/2:
     stars.append('*')
     print(stars)
   else: 
       stars.remove('*')
       print(stars)
