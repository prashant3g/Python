## 2. Sets ##

gender = []
for row in legislators:
    gender.append(row[3])
    
gender = set(gender)
print(gender)

## 3. Exploring the Dataset ##

party = []
for row in legislators:
    party.append(row[-1])

party = set(party)
print(party)

## 4. Missing Values ##

gender = []
for row in legislators:
    #print(row[3])
    if row[3] == "":
        row[3] = "M"
    gender.append(row[3])
    

## 5. Parsing Birth Years ##

birth_years = []
for row in legislators:
    parts = row[2].split('-')
    birth_years.append(parts[0])

## 6. Try/except Blocks ##

try:
    float('hello')
except Exception:
    print('Error converting to float.')

## 7. Exception Instances ##

try:
    int('')
except Exception as exc:
    print(type(exc))
    print(str(exc))

## 8. The Pass Keyword ##

converted_years = []
for year in birth_years:
    try:
        int_year = int(year)
        converted_years.append(int_year)
    except:
        pass

## 9. Convert Birth Years to Integers ##

for row in legislators:
    try:
        birth_year = int(row[2].split('-')[0])
    except Exception:
        birth_year = 0
    row.append(birth_year)
    
print(legislators[0])

## 10. Fill in Years Without a Value ##

last_value = 1
for row in legislators:
    if row[7] == 0:
        row[7] = last_value
    last_value = row[7]
        