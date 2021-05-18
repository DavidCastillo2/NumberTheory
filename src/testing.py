class f:
    def __init__(self, a=False, b=False):
        self.a = a
        self.b = b
        return

    def __repr__(self):
        return "a: %r\t\tb: %r" % (self.a, self.b)


w = f()
x = f(a=True)
z = f(b=True)
y = f(a=True, b=True)

print(w)
print(x)
print(z)
print(y)
