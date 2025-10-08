# Import Statements
import pandas

# Read The CSV file
df = pandas.read_csv('mock.csv', usecols=['Full Name', 'Academic Year'])

# Split Suggestion
member_size = len(df)
print("Total Members: ", member_size)

yearwise_count = df['Academic Year'].value_counts()
no_of_seniors = yearwise_count['III']

print("----- Suggestion For Team Size -----")
for size in range(1, member_size):
    if member_size % size == 0:
        senior_split = (member_size / size)
        if senior_split <= no_of_seniors:
            print(size, end='\n')
