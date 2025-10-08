# tasks/task1.py

def solve():
# Ниже пишите решение задачи
    s = int(input())
    a = s//100
    b = (s//10)%10
    c = s % 10
    print(a,b,c)

    
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()