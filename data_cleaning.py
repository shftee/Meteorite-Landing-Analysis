import pandas as pd

file_path = 'Meteorite_Landings.csv'
meteorites = pd.read_csv(file_path)

print(meteorites.head())

# Handle missing values
meteorites.fillna(method='ffill', inplace=True)

meteorites['year'] = pd.to_datetime(meteorites['year'], errors='coerce').dt.year

# latitude and longitude columns are in the correct format
meteorites['reclat'] = pd.to_numeric(meteorites['reclat'], errors='coerce')
meteorites['reclong'] = pd.to_numeric(meteorites['reclong'], errors='coerce')

# Drop rows with missing latitude or longitude
meteorites = meteorites.dropna(subset=['reclat', 'reclong'])

print(meteorites.info())