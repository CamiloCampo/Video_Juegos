#Comentario de línea

'''
   Comentario de bloque
   Dev: Joan
   Date: 12-03-2024
'''

age = 30
print(type(age))
age = 10.5
print(type(age))
age = True
print(type(age))
age = 'Joan'
print(type(age))
age = '''fdsfgsdafdsa
dfsdsafasdfdsafdsafdsafsdafasdfsda
sdafsdafasdfdsafsdafsdafasdfds'''
print(type(age))
age = 8J
print(type(age))

num1 = 10
num2 = 20
sum1 = num1 + num2
print(sum1, type(sum1))
print(sum1, type(str(sum1)))

list = [1, 2, ['Joan', 30], 3, 'Apple', 'Banana', True]
print(list)
print(type(list))
print(list[2][1])