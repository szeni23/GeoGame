import os

import pandas as pd
import numpy as np
import wikipediaapi
import csv
from bing_image_downloader import downloader

# df = pd.read_csv('concap.csv')
### Add a column for the capital description
# wiki_wiki = wikipediaapi.Wikipedia('MyProjectName (rico@gmail.com)', 'en')
#
# # Loop over the unique capital names in the DataFrame
# for i, row in df.iterrows():
#     capital_name = row['CapitalName']
#     print(f"Fetching description for {capital_name}...")
#
#
#     if pd.notnull(capital_name):
#         try:
#             page = wiki_wiki.page(capital_name)
#             if page.exists():
#                 df.at[i, 'CapitalDescription'] = page.summary
#             else:
#                 df.at[i, 'CapitalDescription'] = "No description found"
#         except:
#             df.at[i, 'CapitalDescription'] = "Error fetching description"
#     else:
#         df.at[i, 'CapitalDescription'] = "Capital name is null"
#
# df.to_csv('updated_database.csv', index=False)pip install bing-image-downloader


### Download images for each country's flag and capital
# os.makedirs('flags', exist_ok=True)
# os.makedirs('capitals', exist_ok=True)
#
# # Loop through each row and download images for each country's flag and capital
# for i, row in df.iterrows():
#     country_name = row['CountryName']
#     capital_name = row['CapitalName']
#
#     if pd.notnull(country_name):
#         print(f"Fetching flag for {country_name}...")
#         query = f'{country_name} flag'
#         downloader.download(query, limit=1, output_dir='flags_temp', adult_filter_off=True, force_replace=False,
#                             timeout=60)
#         # Move image to the main flags directory
#         for filename in os.listdir('flags_temp/' + query):
#             os.rename(f'flags_temp/{query}/{filename}', f'flags/{country_name}_flag.jpg')
#
#     if pd.notnull(capital_name):
#         print(f"Fetching image for {capital_name}...")
#         query = f'{capital_name} city'
#         downloader.download(query, limit=1, output_dir='capitals_temp', adult_filter_off=True, force_replace=False,
#                             timeout=60)
#         # Move image to the main capitals directory
#         for filename in os.listdir('capitals_temp/' + query):
#             os.rename(f'capitals_temp/{query}/{filename}', f'capitals/{capital_name}_city.jpg')
#
# # Remove the temporary directories
# os.rmdir('flags_temp')
# os.rmdir('capitals_temp')


# df = pd.read_csv('updated_database.csv')

### modify the database
# drop countries with no capital
# df = df.dropna(subset=['CapitalName'])
# # save the updated database
# df.to_csv('updated_database.csv', index=False)
#
# df2 = pd.read_csv('world-data-2023.csv')
# merged_df = pd.merge(df, df2, left_on='CountryName', right_on='Country', how='outer')
# #
# # # Save the merged DataFrame to a new CSV file
# merged_df.to_csv('merged_database.csv', index=False)

# df = pd.read_csv('merged_database.csv')
#
# # delete column latitudes and longitudes
# df = df.drop(columns=['Latitude', 'Longitude'])
# df.info()
# df.to_csv('merged_database.csv', index=False)

# df = pd.read_csv('merged_database.csv')
# df = df.dropna(subset=['CapitalName'])
# df.to_csv('dataset.csv', index=False)

df = pd.read_csv('dataset2.csv')


# for col in df.columns:
#     if col.startswith('Density'):
#         df.rename(columns={col: 'Density'}, inplace=True)
#         break
# df.to_csv('dataset.csv', index=False)
# df.to_csv('dataset.csv', index=False)

# def clean_and_convert(column):
#     """ Remove commas and convert to numeric. """
#     return pd.to_numeric(column.str.replace(',', ''), errors='coerce')
#
#
# def clean_and_convert_gdp(column):
#     """ Remove dollar sign, commas and convert to numeric. """
#     return pd.to_numeric(column.str.replace('$', '').str.replace(',', ''), errors='coerce')
#
#
# columns_to_convert = ['Density', 'Land Area(Km2)', 'Armed Forces size',
#                       'Co2-Emissions', 'Population', 'Urban_population']
# for col in columns_to_convert:
#     if col in df.columns:
#         df[col] = clean_and_convert(df[col])
#
# # Special handling for GDP column
# if 'GDP' in df.columns:
#     df['GDP'] = clean_and_convert_gdp(df['GDP'])
#
# print(df)
# df.to_csv('dataset2.csv', index=False)

df.info()