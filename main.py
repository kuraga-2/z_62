input_data = open('input.txt', 'r') 
data = input_data.read()
a = (data[0])
b = int(data[1])
if a == 'A' or a == 'C' or a == 'E' or a == 'G':
    a = 1
else:
    a = 0

if b == 1 or b == 3 or b == 5 or b == 7:
    b = 1
else:
    b = 0

if a == 0 and b == 0:
    output_data = open('output.txt', 'w')
    output_data.write('BLACK')
else:
    output_data = open('output.txt', 'w')
    output_data.write('WHITE')

input_data.close()
output_data.close()