## 3. Read the File Into a String ##

file = open("dq_unisex_names.csv","r")
names = file.read()

## 4. Convert the String to a List ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split("\n")
first_five = names_list[0:5]
print(first_five)

## 5. Convert the List of Strings to a List of Lists ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split('\n')

nested_list = []

for name in names_list:
    comma_list = name.split(",")
    nested_list.append(comma_list)
    
print(nested_list[0:5])

## 6. Convert Numerical Values ##

# print(nested_list[0:5])
numerical_list = []
for row in nested_list:
    name = row[0]
    num = float(row[1])
    float_list = [name, num]
    numerical_list.append(float_list)
    
print(numerical_list)

## 7. Filter the List ##

# The last value is ~100 people
# numerical_list[len(numerical_list)-1]
thousand_or_greater = []
for num_list in numerical_list:
    if num_list[1] >= 1000:
        thousand_or_greater.append(num_list[0])
        
print(thousand_or_greater[0:10])