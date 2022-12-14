array = "2 4 9 8 18 30 4 7 12 11 14"
n = int(input("Введите число: "))

N = list(map(int, array.split())) #преобразуем строку в список
M = True
while M == True: #проверка соответсвия числа условию
    if n <= min(N) or n >= max(N):
        print(f"Число не соответсвует условию. Введите число от {min(N)} до {max(N)}")
        n = int(input("Введите число: "))
    else:
        M = False

if M == False:
    def sort_N(list): #сортировка элементов списка по возрастанию

        while True:
            flag = True
            for i in range(len(list) - 1):
                if list[i] > list[i+1]:
                    list[i], list[i + 1] = list[i + 1], list[i]
                    flag = False
            if flag == True:
                break
        return list

    # print(sort_N(N))

    def bin_search(list, n): #поиск индекса элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу.
        start = 0
        end = len(list) - 1
        num = False

        while start <= end and not num:
            if list[((start + end) // 2) - 1] < n and list[((start + end) // 2) + 1] >= n:
                num = True
                return (start + end) // 2
            else:
                if n <= list[(start + end) // 2]:
                    end = ((start + end) // 2) - 1
                else:
                    start = ((start + end) // 2) + 1
        return num

    print(f"Индекс искомого числа: {bin_search(sort_N(N), n)}")
