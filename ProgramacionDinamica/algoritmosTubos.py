#Created by Mauricio Vargas Ballesteros & Carlos Rodriguez

#faltan inicializar los arreglos :(

r[0]=0
for i in range (0:m)
  for j in range (1:i)
  v=P[j]+r[i-j]
  if(r[i]<v)
    r[i]=v
    s[i]=k
m=n
t=0
while m>0:
  t=t+s[m]
  m=m-s[m]

print('r[n]: ' + str(r[n]))
print ('T: '+ str(t))
