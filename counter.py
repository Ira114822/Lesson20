
class Counter:

    def __init__(self, value=0):
        self._value = value
        self._start_with = value


    def increment(self):
        self._value += 1

    def decrement(self):
        self._value -= 1

    def reset(self):
        self._value = self._start_with

    def __str__(self):
        return f"The cirrent state of the counter is {self._value}"

    @property
    def state(self):
        return self._value

    @state.setter
    def state(self, value):
        self._value = value
    @state.deleter
    def state(self):
        del self._value

    # state = property()
    # state = state.getter(state)
    # state = state.setter(set_state)
    # state = state.deleter(del_state)


counter1 = Counter()

counter1.state = 10
print(counter1.state)
counter1.increment()

print(counter1.state)