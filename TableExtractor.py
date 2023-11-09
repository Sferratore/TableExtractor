import pandas as pd # Import pandas for data manipulation

website_input = input("Insert the website url from which you want to extract table data.")

tables = pd.read_html(website_input)

#Iterating through tables and printing them
for table in tables:
    print(table)
    print("================================")