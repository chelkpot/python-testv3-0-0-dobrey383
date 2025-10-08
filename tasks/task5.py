# tasks/task5.py

def solve():
# Ниже пишите решение задачи
    n = int(input())
    h = (n // 3600) % 24
    m = (n // 60) % 60
    s = n % 60
    print(h,m,s, sep=":")

   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()