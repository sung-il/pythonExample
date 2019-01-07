# -*- coding: utf-8 -*-
# class Math:
#     def __init__(self,a,b):
#         self.a = a 
#         self.b = b
    
#     def __repr__(self):
#         a = str(self.a)+","+str(self.b)
#         return str(a)

#     def _Add(self):
#         c = self.a + self.b
#         return c

#     def _Subtract(self):
#         c = self.a - self.b
#         return c 

#     def _Multiply(self):
#         c = self.a * self.b
#         return c

#     def _Divide(self):
#         c = self.a / self.b
#         return c


# a = Math(5, 15)
# print(a)
# # b = a._Add()
# # print(b)

# Numbers = [50,85,90,28,130,65]
# a = []
# for n in Numbers:
#     if not (n >= 0 and n <= 100):
#         print("over 100")
#         break 
#     if n > 50 and n <= 100:
#         a.append(n)

# print(sum(a))
    
days_in_month = {"1월":31, "2월":28, "3월":31, "4월":30, "5월":31}

for key in days_in_month.keys():
    print(key)
a = input("월을 입력하세요:")
#for a in days_in_month.keys():
#    print(value)
print(days_in_month[a])

