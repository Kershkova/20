min = int(input("Введіть мінімальне значення лічильника: "))
max = int(input("Введіть максимальне значення лічильника: "))

while min >= max:
    max = int(input("Введіть адекватне значення максимуму: "))

current_input = int(input("Введіть поточне значення лічильника: "))

while current_input < min or current_input >= max:
    current_input = int(input("Введіть реальне поточне значення (не менше мінімуму і менше максимуму!): "))

print('\n')


class Counter:
    def __init__(self, minimum, maximum, current):
        self.minimum = minimum
        self.maximum = maximum
        self.current = current
        print(f"Mінімальне значення лічильника: {self.minimum} \n"
              f"Mаксимальне значення лічильника: {self.maximum}  \n"
              f"Попереднє значення лічильника: {self.current}  \n")


    def current_f(self):
        self.current += 1
        print(f"Поточне значення лічильника: {self.current}")
        return (self.current)


my_class = Counter(min, max, current_input)

my_class.current_f()