class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '[person\'s name: %s, age: %g]' % (self.name, self.age)

    def RiseSalary(self):
        print 'SALARY RISE REFUSED'


class Doctor(Person):
    def __init__(self, name, age, speciality, salary):
        Person.__init__(self, name, age)
        self.speciality = speciality
        self.salary = salary

    def __str__(self):
        return '[doctor\'s name: %s, age: %g, speciality: %s, salary: %g]' % (self.name, self.age, self.speciality, self.salary)

    def RiseSalary(self):
        #print self.salary * 1.10
        self.docRise = 1.10
        self.salary = self.salary * self.docRise
        print self.salary


class Lawyer(Person):
    def __init__(self, name, age, speciality, salary):
        Person.__init__(self,name, age)
        self.speciality = speciality
        self.salary = salary

    def __str__(self):
        return '[Lawyer\'s name: %s, age: %g, speciality: %s, salary: %g]' % (self.name, self.age, self.speciality, self.salary)

    def RiseSalary(self):
        self.lawRise = 1.15
        self.salary = self.salary * self.lawRise
        print self.salary


def RiseSalary_twice(aa):
    aa.RiseSalary()
    aa.RiseSalary()


if __name__ == '__main__':
    p = Person('Tom', 23)
    d = Doctor('James', 38, 'Pediatrician', 100000)
    l = Lawyer('Bob', 42, 'patent', 100000)
    print (p)
    print (d)
    print (l)
    RiseSalary_twice(p)
    RiseSalary_twice(d)
    RiseSalary_twice(l)
