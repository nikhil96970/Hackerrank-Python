n=int(input())
if n%2 == 1:
        print("Weird")
if n%2 == 0 and   n in range(2,5):
        print("Not Weird")
if n%2 == 0 and n in range(6,21):
        print("Weird") 
if n%2 == 0 and n>20:
        print("Not Weird")
