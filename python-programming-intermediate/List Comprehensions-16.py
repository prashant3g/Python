## 2. Enumerate ##

ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]

for i, ship in enumerate(ships):
    print(ship)
    print(cars[i])

## 3. Adding Columns ##

things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]

for i, thing in enumerate(things):
    thing.append(trees[i])

## 4. List Comprehensions ##

apple_prices = [100, 101, 102, 105]

apple_prices_doubled = [(apple_price*2) for apple_price in apple_prices]
apple_prices_lowered = [(apple_price-100) for apple_price in apple_prices]

## 5. Counting Female Names ##

name_counts = {}
for row in legislators:

    if row[3] == "F" and row[7]>1940:
        name = row[1]
        if name in name_counts:
            name_counts[name] = name_counts[name] + 1
        else:
            name_counts[name] = 1
            

## 7. Comparing with None ##

values = [None, 10, 20, 30, None, 50]
checks = []

for val in values:
    if val is not None and val > 30:
        checks.append(True)
    else:
        checks.append(False)

## 8. Highest Female Name Count ##

max_value = None
for key in name_counts:
    count = name_counts[key]
    if max_value is None or count > max_value:
        max_value = count

## 9. The Items Method ##

plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}

for k, v in plant_types.items():
    print(k)
    print(v)

## 10. Finding the Most Common Female Names ##

top_female_names = []

for name, count in name_counts.items():
    if name_counts[name] == 2:
        top_female_names.append(name)

## 11. Finding the Most Common Male Names ##

top_male_names = []
male_name_counts = {}

for row in legislators:
    if row[3] == "M" and row[7] > 1940:
        if row[1] in male_name_counts:
            male_name_counts[row[1]] = male_name_counts[row[1]] + 1
        else:
            male_name_counts[row[1]] = 1
            
highest_male_count = 0
for k,v in male_name_counts.items():
    if male_name_counts[k] > highest_male_count:
        highest_male_count = male_name_counts[k]
        
for k,v in male_name_counts.items():
    if male_name_counts[k] == highest_male_count:
        top_male_names.append(k)