# tasks/task7.py

def solve():
   #a = int(input())
   a= 2458

   a1 = (a%10+7)%10
   a2 = (a%100+7)%10
   a3 = (a%1000+7)%10
   a4 = (a%10000+7)%10
   print(int(a3),int(a4),int(a1),int(a2))


    # Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()