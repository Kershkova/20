min = int(input("Введіть мінімальне значення лічильника: "))
max = int(input("Введіть максимальне значення лічильника: "))

while min >= max:
    max = int(input("Введіть адекватне значення максимуму: "))

n = int(input("Скільки разів викликати лічильник? "))

print('\n')


class Counter:
    def __init__(self, minimum, maximum):
        self.minimum = minimum
        self.maximum = maximum
        self.current = self.minimum
        print(f"Mінімальне значення лічильника: {self.minimum} \n"
              f"Mаксимальне значення лічильника: {self.maximum}  \n"
              f"Попереднє значення лічильника: {self.current}  \n")


    def current_f(self):
        if self.current < self.maximum:
            self.current += 1
            print(f"Поточне значення лічильника: {self.current}")
        else:
            print("Максимальне значення досягнуто")
        return (self.current)


my_class = Counter(min, max)

for i in  range(0, n):
    my_class.current_f()
