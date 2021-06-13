'''
See examples.py, constants.py, or main.py for configurable code.
'''

import math

def IsVector(obj):
    return isinstance(obj, Vec3)

def IsNumber(obj):
    return isinstance(obj, (int, float))

class Vec3:

    #####################
    # Python Operations #
    #####################

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"( x: {self.x}, y: {self.y}, z: {self.z} )"
    def __repr__(self):
        return f"Vec3{self}"

    def abs(self):
        return Vec3(abs(self.x), abs(self.y), abs(self.z))

    def _comp(self, rhs, op):
        if IsVector(rhs):
            return Vec3(
                op(self.x, rhs.x),
                op(self.y, rhs.y),
                op(self.z, rhs.z)
            )
        elif IsNumber(rhs):
            return Vec3(
                op(self.x, rhs),
                op(self.y, rhs),
                op(self.z, rhs)
            )

    def max(self, m):
        return self._comp(m, op=max)
    def min(self, m):
        return self._comp(m, op=min)

    #####################
    # Vector Operations #
    #####################

    def dot(self, rhs):
        products = self * rhs
        return products.x + products.y + products.z 

    def mag(self):
        return math.sqrt(self.dot(self))

    def normal(self):
        return self / self.mag()

    ########################
    # Geometric Operations #
    ########################

    def distance(self, rhs):
        return (self - rhs).mag()

    def rotate_x(self, angle):
        s = math.sin(angle)
        c = math.cos(angle)

        return Vec3(
            self.x,
            c * self.y - s * self.z,
            s * self.y + c * self.z
        )

    def rotate_y(self, angle):
        s = math.sin(angle)
        c = math.cos(angle)

        return Vec3(
            c * self.x + s * self.z,
            self.y,
            c * self.z - s * self.x
        )

    def rotate_z(self, angle):
        s = math.sin(angle)
        c = math.cos(angle)

        return Vec3(
            self.x * c - self.y * s,
            self.x * s + self.y * c,
            self.z
        )

    def rotate(self, yaw, pitch, roll):
        return self.rotate_x(yaw).rotate_y(pitch).rotate_z(roll)
    
    ###################
    # Math Operations #
    ###################

    # NEGATION #

    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)

    # ADDITION #

    def __add__(self, rhs):
        if IsVector(rhs):
            return Vec3(
                self.x + rhs.x,
                self.y + rhs.y,
                self.z + rhs.z
            )
        elif IsNumber(rhs):
            return Vec3(
                self.x + rhs,
                self.y + rhs,
                self.z + rhs
            )

    def __radd__(self, lhs):
        return self + lhs

    def __iadd__(self, rhs):
        if IsVector(rhs):
            self.x += rhs.x
            self.y += rhs.y
            self.z += rhs.z
        elif IsNumber(rhs):
            self.x += rhs
            self.y += rhs
            self.z += rhs
        return self

    # SUBTRACTION #

    def __sub__(self, rhs):
        if IsVector(rhs):
            return Vec3(
                self.x - rhs.x,
                self.y - rhs.y,
                self.z - rhs.z
            )
        elif IsNumber(rhs):
            return Vec3(
                self.x - rhs,
                self.y - rhs,
                self.z - rhs
            )
            
    def __rsub__(self, lhs):
        return Vec3(lhs, lhs, lhs) - self

    def __isub__(self, rhs):
        if IsVector(rhs):
            self.x -= rhs.x
            self.y -= rhs.y
            self.z -= rhs.z
        elif IsNumber(rhs):
            self.x -= rhs
            self.y -= rhs
            self.z -= rhs
        return self
    
    # MULTIPLICATION #

    def __mul__(self, rhs):
        if IsVector(rhs):
            return Vec3(
                self.x * rhs.x,
                self.y * rhs.y,
                self.z * rhs.z
            )
        elif IsNumber(rhs):
            return Vec3(
                self.x * rhs,
                self.y * rhs,
                self.z * rhs
            )
            
    def __rmul__(self, lhs):
        return self * lhs

    def __imul__(self, rhs):
        if IsVector(rhs):
            self.x *= rhs.x
            self.y *= rhs.y
            self.z *= rhs.z
        elif IsNumber(rhs):
            self.x *= rhs
            self.y *= rhs
            self.z *= rhs
        return self

    # DIVISION #

    def __truediv__(self, rhs):
        if IsVector(rhs):
            return Vec3(
                self.x / rhs.x,
                self.y / rhs.y,
                self.z / rhs.z
            )
        elif IsNumber(rhs):
            return Vec3(
                self.x / rhs,
                self.y / rhs,
                self.z / rhs
            )
            
    def __rtruediv__(self, lhs):
        return Vec3(lhs, lhs, lhs) / self

    def __itruediv__(self, rhs):
        if IsVector(rhs):
            self.x /= rhs.x
            self.y /= rhs.y
            self.z /= rhs.z
        elif IsNumber(rhs):
            self.x /= rhs
            self.y /= rhs
            self.z /= rhs
        return self

    # INTEGER DIVISION #

    def __floordiv__(self, rhs):
        if IsVector(rhs):
            return Vec3(
                self.x // rhs.x,
                self.y // rhs.y,
                self.z // rhs.z
            )
        elif IsNumber(rhs):
            return Vec3(
                self.x // rhs,
                self.y // rhs,
                self.z // rhs
            )
            
    def __rfloordiv__(self, lhs):
        return Vec3(lhs, lhs, lhs) // self

    def __ifloordiv__(self, rhs):
        if IsVector(rhs):
            self.x //= rhs.x
            self.y //= rhs.y
            self.z //= rhs.z
        elif IsNumber(rhs):
            self.x //= rhs
            self.y //= rhs
            self.z //= rhs
        return self

    # MODULO #

    def __mod__(self, rhs):
        if IsVector(rhs):
            return Vec3(
                self.x % rhs.x,
                self.y % rhs.y,
                self.z % rhs.z
            )
        elif IsNumber(rhs):
            return Vec3(
                self.x % rhs,
                self.y % rhs,
                self.z % rhs
            )
            
    def __rmod__(self, lhs):
        return Vec3(lhs, lhs, lhs) % self

    def __imod__(self, rhs):
        if IsVector(rhs):
            self.x %= rhs.x
            self.y %= rhs.y
            self.z %= rhs.z
        elif IsNumber(rhs):
            self.x %= rhs
            self.y %= rhs
            self.z %= rhs
        return self

    # POWER #

    def __pow__(self, rhs):
        if IsVector(rhs):
            return Vec3(
                self.x ** rhs.x,
                self.y ** rhs.y,
                self.z ** rhs.z
            )
        elif IsNumber(rhs):
            return Vec3(
                self.x ** rhs,
                self.y ** rhs,
                self.z ** rhs
            )
            
    def __rpow__(self, lhs):
        return Vec3(lhs, lhs, lhs) ** self

    def __ipow__(self, rhs):
        if IsVector(rhs):
            self.x **= rhs.x
            self.y **= rhs.y
            self.z **= rhs.z
        elif IsNumber(rhs):
            self.x **= rhs
            self.y **= rhs
            self.z **= rhs
        return self


if __name__ == "__main__":

    print("\nRotations...\n")

    k90 = math.radians(90.0)
    
    a = Vec3(1, 0, 0)
    print(a.rotate_x(k90))
    print(a.rotate_y(k90))
    print(a.rotate_z(k90))

    print("\nMath...\n")

    m = Vec3(5, 4, 3)
    n = Vec3(3, 4, 5)

    print(m.dot(n))
    print(m + n)
    print(m - n)
    print(m * n)
    print(m / n)

    print(m % n)
    print(m // n)
    print(m ** n)

    print("\nMath 2...\n")

    z = 13
    print(m.dot(z))
    print(z + m, m + z)
    print(z - m, m - z)
    print(z * m, m * z)
    print(z / m, m / z)

    print(z % m, m % z)
    print(z // m, m // z)
    print(z ** m, m ** z)



