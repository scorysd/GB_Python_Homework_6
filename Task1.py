
exampl = '3+5*5*8/4'
exampl = list(exampl)

def substr(list):
    for el in list:
        if el == '-':
            index = exampl.index(el)
            substr = float(exampl[index - 1])  - float(exampl[index + 1])
            list.remove(exampl[index + 1])
            list.remove(el)
            list.insert(index, substr)
            list.remove(exampl[index - 1])
    return list
def div(list):
    for el in list:
        if el == '/':
            index = exampl.index(el)
            div = float(exampl[index - 1]) / float(exampl[index + 1])
            list.remove(exampl[index + 1])
            list.remove(el)
            list.insert(index, div)
            list.remove(exampl[index - 1])
    return list
def summ(list):
    for el in list:
        if el == '+':
            index = exampl.index(el)
            summ = float(exampl[index - 1]) + float(exampl[index + 1])
            list.remove(exampl[index + 1])
            list.remove(el)
            list.insert(index, summ)
            list.remove(exampl[index - 1])
    return list
def mylt(list):
    for el in list:
        if el == '*':
            index = exampl.index(el)
            mylt = float(exampl[index - 1]) * float(exampl[index + 1])
            list.remove(exampl[index + 1])
            list.remove(el)
            list.insert(index, mylt)
            list.remove(exampl[index - 1])
    return list
def answer(list):
    for i in list:
        mylt(list)
    for i in list:
        div(list)
    for i in list:
        summ(list)
    for i in list:
        substr(list)
    return list
print(f'Пример: {exampl}\nОтвет: {answer(exampl)}')
