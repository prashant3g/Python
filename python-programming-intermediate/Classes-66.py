## 2. Defining the Dataset Class ##

class Dataset:
    def __init__(self):
        self.type = "csv"
        
dataset = Dataset()
print(dataset.type)

## 3. Passing Additional Arguments to the Initializer ##

# Default display code
class Dataset:
    def __init__(self, data):
        self.type = "csv"
        self.data = data
        
file = open("nfl.csv", "r")
nfl_data = list(csv.reader(file))

dataset = Dataset(nfl_data)
dataset_data = dataset.data

## 4. Adding Additional Behavior ##

# Default display code
class Dataset:
    def __init__(self, data):
        self.data = data
        
    # Your method goes here
    def print_data(self, num_rows):
        print(self.data[:num_rows])
        
dataset = Dataset(nfl_data)
dataset.print_data(5)


## 5. Enhancing the Initializer ##

# Default display code
class Dataset:
    def __init__(self, data):
        #self.data = data
        self.header = data[0]
        self.data = data[1:]

nfl_dataset = Dataset(nfl_data)
nfl_header = nfl_dataset.header

## 6. Grabbing Column Data ##

# Default display code
class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
        self.temp = 0
        
    # Add your method here.
    def column(self, label):
        if label in self.header:
            temp=[]
            for row in self.data:
                temp.append(row[self.header.index(label)])
            return temp
        else:
            return None
            
            

nfl_dataset = Dataset(nfl_data)
year_column = nfl_dataset.column('year')
player_column = nfl_dataset.column('player')

## 7. Count Unique Method ##

# Default display code
class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
        self.temp = 0
        
    # Add your method here.
    def column(self, label):
        if label in self.header:
            temp=[]
            for row in self.data:
                temp.append(row[self.header.index(label)])
            return set(temp)
        else:
            return None
            
    def count_unique(self, label):
        return len(self.column(label))
            

nfl_dataset = Dataset(nfl_data)
total_years = nfl_dataset.count_unique('year')

## 8. Make Objects Human Readable ##

# Default display code
class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
        self.temp = []
        
    def __str__(self):
        return str(self.data[:10])
        
    # Add your method here.
    def column(self, label):
        if label in self.header:
            temp=[]
            for row in self.data:
                temp.append(row[self.header.index(label)])
            return set(temp)
        else:
            return None
            
    def count_unique(self, label):
        return len(self.column(label))
            

nfl_dataset = Dataset(nfl_data)
print(nfl_dataset)