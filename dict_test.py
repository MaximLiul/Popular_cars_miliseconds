import pandas as pd

purchases = {
    '1': [3, 2, 0, 1],
    '2': [0, 3, 7, 2],
    '3': [0, 3, 7, 2]

}

df = pd.DataFrame(purchases)
level_map = {1: 'high', 2: 'medium', 3: 'low', 4: 'very low'}
df['c_level'] = df['3'].map(level_map)

print(df)