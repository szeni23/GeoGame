import os

import pandas as pd
import wikipediaapi
import csv
from bing_image_downloader import downloader

df = pd.read_csv('concap.csv')
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


