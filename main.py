import pandas as pd
from sklearn.cluster import KMeans
import folium
from folium.plugins import MarkerCluster
import webbrowser
import os


# Function to analyze restaurants using a local CSV file
def analyze_high_rated_restaurants(file_path):
    """
    Analyze restaurants from a local CSV file.
    - Filters restaurants with average ratings of 4 and 5.
    - Aggregates reviews by restaurant ID.
    - Saves an interactive folium map with marker sizes based on the number of reviews.
    - Marker colors indicate clusters.

    Parameters:
        file_path (str): Path to the CSV file.
    """
    # Step 1: Load the CSV data into a pandas DataFrame
    df_places = pd.read_csv(file_path)

    # Step 2: Filter relevant columns and rows where rating is 4 or 5
    df_filtered = df_places[df_places['rating'].isin([4, 5])]

    # Step 3: Group by restaurant ID (id), calculate average rating and count reviews
    df_grouped = df_filtered.groupby(['id', 'name', 'lat', 'lng'], as_index=False).agg({
        'rating': 'mean',  # Average rating per restaurant
        'id': 'count'  # Number of reviews per restaurant (count of IDs)
    }).rename(columns={'id': 'review_count'})  # Rename column for clarity

    # Step 4: Perform KMeans clustering based on lat, lng, and average rating
    X = df_grouped[['lat', 'lng', 'rating']]
    kmeans = KMeans(n_clusters=4, n_init=10)  # Example with 4 clusters
    kmeans.fit(X)

    # Add the cluster labels to the DataFrame
    df_grouped['cluster'] = kmeans.labels_

    # Step 5: Create an interactive map using folium
    # Create a map centered on the average location (mean latitude and longitude)
    city_center = [df_grouped['lat'].mean(), df_grouped['lng'].mean()]
    city_map = folium.Map(location=city_center, zoom_start=13)

    # Create a marker cluster to group nearby points
    marker_cluster = MarkerCluster().add_to(city_map)

    # Add restaurants to the map with circle markers, where size depends on review count
    for _, row in df_grouped.iterrows():
        folium.CircleMarker(
            location=[row['lat'], row['lng']],
            radius=row['review_count'] * 1.5,  # Adjust radius based on review count
            popup=f"Restaurant: {row['name']}<br>Avg. Rating: {row['rating']:.2f}<br>Reviews: {row['review_count']}<br>Cluster: {row['cluster']}",
            color='blue' if row['cluster'] == 0 else
            'green' if row['cluster'] == 1 else
            'red' if row['cluster'] == 2 else 'purple',
            fill=True,
            fill_opacity=0.6
        ).add_to(marker_cluster)

    # Step 6: Save the map as an HTML file
    map_filename = 'high_rated_restaurants_map.html'
    city_map.save(map_filename)
    print(f"Map saved as '{map_filename}'.")

    # Automatically open the map in the default web browser
    file_path = os.path.abspath(map_filename)
    webbrowser.open(f'file://{file_path}')
    
    # Step 7: Print summary of restaurants with average rating and number of reviews
    print(df_grouped[['name', 'lat', 'lng', 'rating', 'review_count', 'cluster']].head())


# Example usage: Load from CSV file and analyze
file_path = 'Restaurants - Sheet1.csv'  # Replace with the path to your CSV file
analyze_high_rated_restaurants(file_path)
