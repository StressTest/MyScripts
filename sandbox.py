import math

def Form(k=1, a=0, b=0, t1=1, t12=1, t2=1):
    print(k)
    print("Form4")
    def form(t):
        # print(k)
        # print('form')
        return k * (a * math.e ** (-t / t1) + b * math.e ** (-t / t12) - math.e ** (-t / t2))
    return form

print('111')
Form4 = Form(k=1, a=0, b=0, t1=1, t12=1, t2=1)
print('222')
print()
print(type(Form4))

print(Form4(2))