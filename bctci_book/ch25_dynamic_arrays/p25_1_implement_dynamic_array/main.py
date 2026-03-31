"""
Implementing Dynamic Array
"""


class DynamicArray:
    def __init__(self):
        self.size: int = 0
        self.capacity: int = 10
        self.fixed_array = [None] * self.capacity

    def get_size(self):
        return self.size

    def append(self, value):
        if self.size == self.capacity:
            self.resize(int(self.capacity * 2))

        self.fixed_array[self.size] = value
        self.size += 1

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bound")
        return self.fixed_array[index]

    def set(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bound")
        self.fixed_array[index] = value

    def pop_back(self):
        if self.size == 0:
            raise IndexError("Pop from empty array")
        value = self.fixed_array[self.size - 1]
        self.fixed_array[self.size - 1] = None
        self.size -= 1

        if self.size / self.capacity < 0.25 and self.capacity > 10:
            self.resize(int(self.capacity / 2))

        return value

    def resize(self, capacity: int):
        new_fixed_size_array = [None] * capacity
        for i in range(self.size):
            new_fixed_size_array[i] = self.fixed_array[i]
        self.fixed_array = new_fixed_size_array
        self.capacity = capacity


def test():
    my_array = DynamicArray()
    for value in range(0, 14):
        my_array.append(value)
    print(f"fixed array {my_array.fixed_array}")
    print(f"size  {my_array.get_size()}")
    print(f"capacity {my_array.capacity}")
    print("testing pop back")
    for value in range(0, 12):
        my_array.pop_back()
    print(f"fixed array {my_array.fixed_array}")
    print(f"size  {my_array.get_size()}")
    print(f"capacity {my_array.capacity}")


if __name__ == "__main__":
    test()
