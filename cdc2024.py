import pandas as pd
import folium
from folium.plugins import MarkerCluster

# Load the dataset (use your own file path)
df = pd.read_csv('everything.csv')

# Step 1: Group by restaurant id and calculate average rating and number of reviews
df_grouped = df.groupby(['id', 'Category']).agg({
    'name': 'first',
    'lat': 'first',
    'lng': 'first',
    'rating': ['mean', 'count'],  # Average rating and number of reviews
}).reset_index()

# Flatten the columns
df_grouped.columns = ['id', 'Category', 'name', 'lat', 'lng', 'avg_rating', 'review_count']

# Step 2: Filter for ratings between 4 and 5 for all categories
filtered_df = df_grouped[df_grouped['avg_rating'].between(4, 5)]

# Step 3: Create a Folium map centered at Amsterdam
m = folium.Map(location=[52.370216, 4.895168], zoom_start=12)

# Step 4: Define categories
categories = ['Restaurant', 'Attraction', 'POI', 'Accommodation']

# Step 5: Add Feature Groups for each category to allow toggling
for category in categories:
    category_data = filtered_df[filtered_df['Category'] == category]

    # Create a feature group for the category
    feature_group = folium.FeatureGroup(name=category)

    # Add marker cluster for each category
    marker_cluster = MarkerCluster().add_to(feature_group)

    # Add markers to the feature group
    for _, row in category_data.iterrows():
        folium.CircleMarker(
            location=[row['lat'], row['lng']],
            radius=row['review_count'] * 2,  # Size proportional to the number of reviews
            popup=f"{row['name']}\nAvg Rating: {row['avg_rating']:.2f}\nReviews: {row['review_count']}",
            color='blue',
            fill=True,
            fill_color='blue'
        ).add_to(marker_cluster)

    # Add the feature group to the map
    feature_group.add_to(m)

# Step 6: Add Layer Control to toggle between categories
folium.LayerControl().add_to(m)

# Step 7: Save the map as an HTML file
m.save('combined_category_map.html')

print("Combined map with category selection has been saved.")
