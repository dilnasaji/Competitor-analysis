#print ("Hello world")
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns
df = pd.read_csv('Leaseshare_Final.csv', encoding='latin1')
print(df.head())
#column = df['id_r']
#regions = df['Regions ']
#print(column)
#print(df.info())
#print(df.describe) 

#print(df.columns)
#df = pd.DataFrame(column)
'''
df['id_p'] = df['id_p'].apply(lambda x: list(map(int, x.split(','))))
flattened_data = [item for sublist in df['id_p'] for item in sublist]
plt.figure(figsize=(10, 6))
plt.hist(flattened_data, bins=15, color='lightblue', edgecolor='black',label='services')
plt.title('Histogram of Social Media Platform Occurrences')
plt.xlabel('Platforms')
plt.ylabel('Frequency')
plt.legend()
plt.show()

'''

'''
# Splitting the 'id_p' column into separate rows
df_exploded = df['id_p'].str.split(',', expand=True).stack().reset_index(level=1, drop=True)
df_exploded.name = 'id_p'
df_cleaned = df_exploded.to_frame().reset_index()

# Convert id_p to integer
df_cleaned['id_p'] = df_cleaned['id_p'].astype(int)

print(df_cleaned)

# Count occurrences of each rental type
rental_counts = df_cleaned['id_p'].value_counts()

# Plotting
plt.bar(rental_counts.index, rental_counts.values)
plt.xticks([1, 2, 3], ['Vacation Rental', 'Short Term Rental', 'Long Term Rental'])
plt.xlabel('Rental Type')
plt.ylabel('Count')
plt.title('Count of Rental Types')
plt.show()

# Plotting a pie chart
plt.pie(rental_counts, labels=['Vacation Rental', 'Short Term Rental', 'Long Term Rental'], autopct='%1.1f%%')
plt.title('Proportion of Rental Types')
plt.show()

'''

'''

# Count occurrences of each region
region_counts = df['id_r'].value_counts()

# Plotting a pie chart
plt.pie(region_counts, labels=region_counts.index, autopct='%1.1f%%')
plt.title('Proportion of Regions')
plt.show()


'''

'''
#  Convert all values to string and handle NaN
regions = regions.fillna('')  # Replace NaN with an empty string
regions = regions.astype(str)  # Convert all values to string

# Create a string from the regions
text = ' '.join(regions)

#  Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

#  Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Hide axes
plt.show()
'''

'''
property_types = df[' Type of property']
#  Split the strings by comma and flatten the list
all_property_types = property_types.str.split(',').explode()

#  Remove any leading or trailing spaces
all_property_types = all_property_types.str.strip()

# Handle missing values by replacing them with an empty string
all_property_types = all_property_types.fillna('')

#  Convert all values to string
all_property_types = all_property_types.astype(str)

#  Create a string from the property types
text = ' '.join(all_property_types)

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Hide axes
plt.show()

'''
'''
monthly_visits = df['Number of Monthly visitors']
property_counts = df['Number of properties']
#print(platforms)
#print(property_counts)
data = pd.DataFrame({
    'Monthly_visits': monthly_visits,
    'Property_Count': property_counts
})


data = data.dropna(subset=['Monthly_visits','Property_Count'])
print(data.head())
'''
'''
# Create the bar plot
plt.figure(figsize=(12, 8))
sns.barplot(x='Platform', y='Property_Count', data=df)
plt.title('Total Properties Available by Platform')
plt.ylabel('Number of Properties')
plt.xlabel('Platform')
plt.yscale('log')  # Use log scale for better visualization of large differences
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.gca().invert_yaxis()
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()

correlation = data.corr()
print(correlation)

# Scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Property_Count', y='Monthly_visits', data=data)
plt.title('Number of Properties vs. Number of Visitors')
plt.xlabel('Number of Properties')
plt.ylabel('Number of Visitors')
plt.xscale('log')  # Log scale for better visualization if data is skewed
plt.yscale('log')  # Log scale for better visualization if data is skewed
plt.show()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
'''
'''
monthly_visits = df['Number of Monthly visitors']
vacationrental = df['Vacation Rental']
platform = df['Name']

data = pd.DataFrame({
    'Monthly_visits': monthly_visits,
    'Vacation_rentals': vacationrental,
    'Platforms': platform
})

df = pd.DataFrame(data)
vacation_rental_df = df[df['Vacation_rentals'] == 1]
#print(short_term_rental_df)

df = pd.DataFrame(vacation_rental_df)
print(df)
df = df.dropna(subset=['Monthly_visits'])

# Sort the DataFrame by Monthly_visits for better visualization
df = df.sort_values(by='Monthly_visits', ascending=False)

# Create a bar plot
plt.figure(figsize=(12, 6))
plt.barh(df['Platforms'], df['Monthly_visits'], color='skyblue')
plt.xlabel('Monthly Visits')
plt.title('Monthly Visits for Vacation Rental Platforms')
plt.xscale('log')
plt.gca().invert_yaxis()  # Invert y-axis to have the highest value on top
plt.xticks(rotation=45)   # Rotate x-axis labels for better readability
plt.tight_layout()         # Adjust layout to make room for labels
plt.show()

'''


'''
platform = df['Name']
facebook = df['Facebook']
instagram = df['Instagram']
pinterest = df['Pinterest']
vacation_rental = df['Vacation Rental']

data = pd.DataFrame({
    'fb' : facebook,
    'insta': instagram,
    'pin' : pinterest,
    'vac': vacation_rental,
    'platforms' : platform
     })

df = pd.DataFrame(data)
vacation_rental_df = df[df['vac'] == 1]
vacation_rental_df = vacation_rental_df[['platforms', 'fb', 'insta', 'pin']]
print(vacation_rental_df)

social_media_counts = vacation_rental_df[['fb', 'insta', 'pin']].sum()

# Step 3: Visualize the counts
social_media_counts.plot(kind='bar', color=['blue', 'purple', 'red'])

plt.title('Social Media Usage for Vacation Rentals')
plt.xlabel('Social Media Platforms')
plt.ylabel('Count of Users')
plt.xticks(rotation=0)  # Rotate x-axis labels for better readability
plt.grid(axis='y')  # Add gridlines for better readability
plt.show()
'''

monthly_visits = df['Number of Monthly visitors']
platform = df['Name']
instagram = df['Instagram']

data = pd.DataFrame({
    'Monthly_visits': monthly_visits,
    'Platforms': platform,
    'insta': instagram
    })

df = pd.DataFrame(data)
rental_df = df[df['insta'] == 1]
print(rental_df)
df = pd.DataFrame(rental_df)
df = df.dropna(subset=['Monthly_visits'])

# Sort the DataFrame by Monthly_visits for better visualization
df = df.sort_values(by='Monthly_visits', ascending=False)

# Create a bar plot
plt.figure(figsize=(12, 6))
plt.barh(df['Platforms'], df['Monthly_visits'], color='skyblue')
plt.xlabel('Monthly Visits')
plt.title('Monthly Visits for Platforms using Instagram')
plt.xscale('log')
plt.gca().invert_yaxis()  # Invert y-axis to have the highest value on top
plt.xticks(rotation=45)   # Rotate x-axis labels for better readability
plt.tight_layout()         # Adjust layout to make room for labels
plt.show()






