#uc reqemli ededin ferqli reqemlerini gostermek
abc = int(input())
a = abc // 100
b = abc // 10 % 10
c = % 10 
mini = min(a, b, c)
maks = max(a, b, c)
orta = a+b+c-mini-maks

print(mini, end = " ")

if(mini != orta):
  print(orta, end = " ")
if (maks != orta):
  print(maks)
