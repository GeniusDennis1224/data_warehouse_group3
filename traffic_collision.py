### ---- Loading Data ----- ###
import pandas as pd
collision_data = pd.read_csv('E:\\data_warehouse_project2\\Traffic Collisions Open Data\\Traffic_Collisions_Open_Data.csv')
collision_data
collision_data.info()

# Step 1: Delete missing values - since there are only 7 columns that have null values
# And there are only 4 missing values for each column, so we can consider deleting these rows
collision_data.dropna(axis=0,how="any",inplace=True)
collision_data
collision_data.info()


# Step 2: Delete unnecessary columns
collision_data = collision_data.drop(columns=['HOOD_158', 'LONG_WGS84', 'LAT_WGS84', 'x', 'y'])
collision_data.info()


# Step 3: Deal with 'NSA' value for columns 'DIVISION' and 'NEIGHBOURHOOD_158'
collision_data['DIVISION'] = collision_data['DIVISION'].replace('NSA', 'Unknown', inplace=True)

# Step 4: Deal with 'N/R' values for columns 'AUTOMOBILE, MOTORCYCLE, PASSENGER, BICYCLE, PEDESTRIAN'
collision_data['AUTOMOBILE'] = collision_data['AUTOMOBILE'].replace('N/R', 'Unknown', inplace=True)
collision_data['MOTORCYCLE'] = collision_data['MOTORCYCLE'].replace('N/R', 'Unknown', inplace=True)
collision_data['PASSENGER'] = collision_data['PASSENGER'].replace('N/R', 'Unknown', inplace=True)
collision_data['BICYCLE'] = collision_data['BICYCLE'].replace('N/R', 'Unknown', inplace=True)
collision_data['PEDESTRIAN'] = collision_data['PEDESTRIAN'].replace('N/R', 'Unknown', inplace=True)

print(collision_data)


# Step 5: Convert OCC_DATE (object data type) into datetime
collision_data['OCC_DATE'] = pd.to_datetime(collision_data['OCC_DATE'], errors='coerce')

# Extract Year, Month, Day from OCC_DATE
collision_data['acc_year'] = collision_data['OCC_DATE'].dt.year
collision_data['acc_month'] = collision_data['OCC_DATE'].dt.month
collision_data['acc_day'] = collision_data['OCC_DATE'].dt.day

collision_data
collision_data.info()

print("Accident Year: ", collision_data['acc_year'])
print("Accident Month: ", collision_data['acc_month'])
print("Accident Date: ", collision_data['acc_day'])


# Step 6: For columns 'BICYCLE', 'AUTOMOBILE', transfer their original datatype (Object)
# to Binary (0, 1)
# Firstly, check all the columns have unique values
print(collision_data['AUTOMOBILE'].unique())
print(collision_data['MOTORCYCLE'].unique())
print(collision_data['PASSENGER'].unique())
print(collision_data['BICYCLE'].unique())
print(collision_data['PEDESTRIAN'].unique())

# Step 6: Continues.......
def map_values(value):
    if value == 'YES':
        return 1
    elif value == 'NO':
        return 0
    else:
        return 'Unknown'

collision_data['AUTOMOBILE'] = collision_data['AUTOMOBILE'].apply(map_values)
collision_data['MOTORCYCLE'] = collision_data['MOTORCYCLE'].apply(map_values)
collision_data['PASSENGER'] = collision_data['PASSENGER'].apply(map_values)
collision_data['BICYCLE'] = collision_data['BICYCLE'].apply(map_values)
collision_data['PEDESTRIAN'] = collision_data['PEDESTRIAN'].apply(map_values)

collision_data

# Step 7: Transfer columns 'INJURY_COLLISIONS', 'FTR_COLLISIONS', 'PD_COLLISIONS' current value to 0/1
# First, check if values are unique
print(collision_data['INJURY_COLLISIONS'].unique())
print(collision_data['FTR_COLLISIONS'].unique())
print(collision_data['PD_COLLISIONS'].unique())

# Step 7 Continues.......
collision_data['INJURY_COLLISIONS'] = collision_data['INJURY_COLLISIONS'].map({'YES': 1, 'NO': 0})
collision_data['FTR_COLLISIONS'] = collision_data['FTR_COLLISIONS'].map({'YES': 1, 'NO': 0})
collision_data['PD_COLLISIONS'] = collision_data['PD_COLLISIONS'].map({'YES': 1, 'NO': 0})

print(collision_data.describe())

# Statistical Analysis
print(collision_data.isna().sum())