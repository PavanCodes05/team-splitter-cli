# Import Statements
import random
import pandas
from collections import defaultdict

# Read The CSV file
df_old = pandas.read_csv('mock.csv', usecols=['Full Name', 'Academic Year'])
df = df_old.rename(columns={'Full Name': 'full_name', 'Academic Year': 'academic_year'})

# Split Suggestion
member_size = len(df)
print("Total Members: ", member_size)

yearwise_count = df['academic_year'].value_counts()
no_of_seniors = yearwise_count['III']

print("----- Suggestion For Team Size -----")
for size in range(1, member_size):
    if member_size % size == 0:
        senior_split = (member_size / size)
        if senior_split <= no_of_seniors:
            print(size, end='\n')

# Random Pick Logic
# Get Input From User
split_size = 4
team_size = (member_size // split_size)

team_split_info = defaultdict(list)
picked = set(range(0, 20))

current_team = 1
while current_team <= split_size:
    for i in range(team_size):
        random_number = random.choice(list(picked))
        member = df.iloc[random_number]
        team_split_info[current_team].append((member.full_name, member.academic_year))

        picked.remove(random_number)

    current_team += 1

print(team_split_info)
