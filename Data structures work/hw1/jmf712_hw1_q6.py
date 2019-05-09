class Vector:
    def __init__(self, d):
        if type(d) is int:
            self.coords = [0]*d
        elif type(d) is list:
            self.coords = d

    def __len__(self):
        return len(self.coords)

    def __getitem__(self, j):
        return self.coords[j]

    def __setitem__(self, j, val):
        self.coords[j] = val

    def __add__(self, other):
        if (len(self) != len(other)):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    
    def __sub__(self, other):
        if (len(self) != len(other)):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __mul__(self, scalar): #I named it scalar before reading the whole problem
        if type(scalar) is int or type(scalar) is float:
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] * scalar
            return result
        elif type(scalar) is Vector:
            if len(self) != len(scalar):
                raise ValueError("dimensions must agree")
            ans = 0
            for j in range(len(self)):
                ans += self[j] * scalar[j]
            return result
                
    def __rmul__(self, scalar):
        return self * scalar

    def __eq__(self, other):
        return self.coords == other.coords

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        return '<'+ str(self.coords)[1:-1] + '>'

    def __repr__(self):
        return str(se)
