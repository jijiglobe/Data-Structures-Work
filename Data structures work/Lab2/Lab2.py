class polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients
    
    def __str__(self):
        ans = ""
        if len(self.coefficients) == 0:
            return ans
        if len(self.coefficients) == 1:
            return str(self.coefficients[0])
        if self.coefficients[0] != 0 and self.coefficients[1] != 0:
            ans += str(self.coefficients[1]) + "x + " + str(self.coefficients[0])
        elif self.coefficients[0] == 0 and self.coefficients[1] != 0:
            ans += str(self.coefficients[1])+"x"
        elif len(self.coefficients) == 1 or self.coefficients[0] != 0 and self.coefficients[1] == 0:
            ans += str(self.coefficients[0])
        if len(self.coefficients) == 2:
            return ans
        index = 0

        for coefficient in self.coefficients:
            if coefficient != 0 and index > 1:
                if coefficient == 1:
                    ans = "x^" + str(index) + " + " + ans
                else:
                    ans = str(coefficient) + "x^" + str(index) +" + " +  ans
            index +=1
        if ans[-3:len(ans)] == " + ":
            ans = ans[0:-3]
        return ans
        
    def eval(self,value):
        ans = self.coefficients[0]
        index = 1
        for coefficient in self.coefficients:
            ans += coefficient * (value ** index)
            index +=1
        return ans

    def __add__(self, otherPoly):
        shorter = self.coefficients
        longer = otherPoly.coefficients
        if len(shorter) > len(longer):
            longer, shorter = shorter, longer
        ans = []
        for x in range(len(shorter)):
            ans.append(shorter[x] + longer[x])
        for x in range(len(shorter),len(longer)):
            ans.append(longer[x])
        return polynomial(ans)
        
    def __mul__(self, otherPoly):
        ans = []
        for x in range(len(otherPoly.coefficients) + len(self.coefficients) - 1):
            ans.append(0)
        for x in range(len(self.coefficients)):
            for y in range(len(otherPoly.coefficients)):
                ans[x + y] += self.coefficients[x] * otherPoly.coefficients[y]
        return polynomial(ans)

def powers_of_two(val):
    for x in range(1,val + 1):
        yield 2**x

def testPowers():
    print("\n\nTesting Powers...")
    print("powers_of_two(6)")
    for x in powers_of_two(6):
        print(x)

    print("powers_of_two(3)")
    for x in powers_of_two(3):
        print(x)
    print("powers_of_two(10)")
    for x in powers_of_two(10):
        print(x)
    print("powers_of_two(0)")
    for x in powers_of_two(0):
        print(x)

def testStr():
    print("\n\ntesting __str__..")
    current = [1,2,3,4]
    print("polynomial for " + str(current))
    print(polynomial(current))
    current = [0,0,0,4]
    print("polynomial for " + str(current))
    print(polynomial(current))
    current = [0,2,0,4]
    print("polynomial for " + str(current))
    print(polynomial(current))
    current = [1,0,3,4,0,6]
    print("polynomial for " + str(current))
    print(polynomial(current))
    

def testAdd():
    print("\n\nTesting Add...")
    p1 = [1,2,3,4,5]
    p2 = [1,2,3,4]
    print("adding...\n"+str(polynomial(p1))+"\n"+str(polynomial(p2))+":")
    print(polynomial(p1) + polynomial(p2))
    p1 = [1,2,3,4,5]
    p2 = [1,2,3,4]
    print("adding...\n"+str(polynomial(p1))+"\n"+str(polynomial(p2))+":")
    print(polynomial(p1) + polynomial(p2))
    p1 = [0,0,3,4,5]
    p2 = [1,2,0,4]
    print("adding...\n"+str(polynomial(p1))+"\n"+str(polynomial(p2))+":")
    print(polynomial(p1) + polynomial(p2))
    p1 = [0,0,1]
    p2 = [1]
    print("adding...\n"+str(polynomial(p1))+"\n"+str(polynomial(p2))+":")
    print(polynomial(p1) + polynomial(p2))

def testMul():
    print("\n\ntesting mul...")
    p1 = polynomial([1,0,2])
    p2 = polynomial([0,0,1])
    print("multiplying:+\n"+str(p1)+" with ")
    print(p2)
    print( p1 * p2)
    p1 = polynomial([1,1,1])
    p2 = polynomial([1,1,1])
    print("multiplying:+\n"+str(p1)+" with ")
    print(p2)
    print( p1 * p2)
    p1 = polynomial([1,0,5,5])
    p2 = polynomial([0,0,1])
    print("multiplying:+\n"+str(p1)+" with ")
    print(p2)
    print( p1 * p2)
    p1 = polynomial([1,0,0,1])
    p2 = polynomial([0,0,1])
    print("multiplying:+\n"+str(p1)+" with ")
    print(p2)
    print( p1 * p2)
    

testStr()
testAdd()
testMul()
testPowers()
