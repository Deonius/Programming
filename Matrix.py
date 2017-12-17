import random

def create_list_by_random(size, min, max):
    a = [[random.randint(min, max) for j in range(size)] for i in range(size)]
    return a


def after_decoration(what_decorate):
    def what_returned(self):
        print('')
        what_decorate(self)
        print('')
    return what_returned


class Square_Matrix:
   size=0
   count=0
   def __init__(self,size,choice,a):

        self.size=size
        self.choice=choice
        self.a=a(choice,size)

   @after_decoration
   def get_attributes(self):
    print(self.size)
    print(Square_Matrix.count)

   def get (self):
        print(self.size)

   def __str__(self):
        for i in range(self.size):
            s=str(self.a[i]) + "\n"
            print(1)
            return s

   def _import(self):
        b=int()
        for i in range(self.size):
            b=self.a[i][i]+b
        print(b)

   def sum_of_main_diagonal(self):
    b = 0
    for i in range(self.size):
        b += self.a[i][i]
    return a

   def transposition(self):
        for i in range(self.size):
            for j in range(self.size):
                self.a[i+1][j]=self.a[j][i+1]
        return self.a




