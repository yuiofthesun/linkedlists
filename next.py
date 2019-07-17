
class Iterable():
    def __init__(self, value: int):
        self.value = value

    def __iter__(self):
        my_iterator = Iterator(self.value)
        return my_iterator

class Iterator():
    def __init__(self, value: int):
        self.value = value

    def __next__(self):
        self.value = self.value + 1
        return self.value

our_class = Iterable(1)

for thing in our_class:
    print(thing)
