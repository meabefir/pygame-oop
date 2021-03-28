import math


class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def get_squared_length(self):
        return self.x * self.x + self.y * self.y

    def normalized(self):
        temp_vec = self
        length = temp_vec.get_length()
        if length != 0:
            temp_vec.x /= length
            temp_vec.y /= length
        return temp_vec

    def move_towards(self, vec, delta):
        if abs((self - vec).get_length()) <= delta:
            return vec
        else:
            new_vec = self + (vec - self).normalized() * delta
            return new_vec

    def __eq__(self, other):
        if int(self.x) == int(other.x) and int(self.y) == int(other.y):
            return True
        return False

    def __add__(self, vec):
        return Vector2(self.x + vec.x, self.y + vec.y)

    def __sub__(self, vec):
        return Vector2(self.x - vec.x, self.y - vec.y)

    def __mul__(self, value):
        return Vector2(self.x * value, self.y * value)

    def __truediv__(self, value):
        return Vector2(self.x / value, self.y / value)

    def to_int(self):
        return Vector2(int(self.x), int(self.y))

    def __str__(self):
        return f'({self.x},{self.y})'


if __name__ == "__main__":
    v1 = Vector2(1, 2)
    v2 = Vector2(3, 4)
    print(v1 + v2)
    print(v1 - v2)
