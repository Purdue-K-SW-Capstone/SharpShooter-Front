import pandas as pd
file = pd.read_csv(r'C:/python/apple_sweet/Apple_attribute2.txt')
new_csv_file = file.to_csv(r'C:/python/apple_sweet/Apple_attribute2.csv')