# tasks/task3.py

def solve():
# Ниже пишите решение задачи
    n = int(input())
    a = 0
    b = [100, 20, 10, 5, 1]

    for s in b:
        a += n // s
        n %= s
    print(a)

        


# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()