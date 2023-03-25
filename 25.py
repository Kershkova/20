class Buffer:
    def __init__(self, pos=None):
        self.pos = pos or []

    def add(self, *a):
        self.pos += a
        print(self.pos)
        return self.pos

    def get_current_part(self, sum = 0):
        if len(self.pos) >= 5:
            for i in range(5):
                sum += self.pos[i]
            print("Сума 5-ти: ", sum, '\n')
            del self.pos[0:5]
        else:
            print('Недостатньо елементів')
        return sum


if __name__ == "__main__":
    buf = Buffer()
    buf.add(5, 5, 6)
    buf.get_current_part()
    buf.add(1, 11, 5, 8, 6, 4)
    buf.get_current_part()
    buf.add(1, 2)
    buf.get_current_part()
    buf.add(1, 2, 3, 4)
    buf.get_current_part()
    buf.add(15, 24, 45, 89)
    buf.get_current_part()