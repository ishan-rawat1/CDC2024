# Michelin Journal: Data-Driven Insights and Business Growth Across the World

## Project Overview

This project analyzes restaurant, attraction, accomodation, and point-of-interest (POI) data across multiple locations to provide tourists with optimal recommendations on **where to go**, **when to go**, and **what experiences to choose**. By clustering review data, we identify key drivers of positive feedback and provide actionable insights to help businesses improve their offerings.

## Motivation

Inspired by the Michelin Guide, our goal is to:
- Help travelers find the best places based on their preferences.
- Assist businesses in improving their performance through sentiment analysis and identifying what leads to positive reviews.

## Key Questions Answered
1. **Where should travelers go?**
   - Using a K-means clustering algorithm, we identify the top-rated restaurants, attractions, accommodations, and POIs in each location based on latitude and longitude.
   
2. **When is the best time to visit?**
   - Seasonal and time-of-day insights based on review analysis help travelers plan their trips optimally.

3. **What experiences best match specific interests?**
   - Recommendations tailored to categories like **Sports**, **Nightlife**, and **Cultural Events**.

## Methodology

### 1. Data Collection & Cleaning
We retrieve data using APIs, clean the reviews to remove null values, and aggregate them into CSV files. This is further processed into a comprehensive dataset for analysis.

### 2. Location Analysis
Using K-means clustering, we analyze the average ratings of restaurants, attractions, and accommodations. We generate location-based clusters to identify optimal places for short-term and long-term stays.

### 3. Sentiment Analysis & Review Triggers
Our sentiment analysis identifies words and phrases that most frequently correlate with positive or negative reviews, providing businesses with insights to improve.

### 4. Custom Recommendations
We offer personalized recommendations for travelers based on their preferences in categories like sports, nightlife, and cultural events, using a combination of mBERT embeddings and metadata from the reviews.

## Challenges

- **Disbalanced data**: Many reviews were not in English and needed preprocessing.
- **Sentiment analysis inconsistencies**: The polarity ratings provided did not always align with actual sentiments in the text, requiring custom handling.

## How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-url
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the analysis scripts in the Jupyter notebooks provided:
   * **`data_cleaning_main.ipynb`**: For cleaning and preparing the data.
   * **`NarasimhaCDC2024.ipynb`**: For the sentiment and clustering analysis.
   * **`negative_positive_words.ipynb`**: For identifying key phrases driving review polarity.
   * **`sentiment_analysis_visualization.ipynb`**: For visualizing sentiment analysis results.
   * **`text_processing_translation_GPU_required.ipynb`**: For processing and translating non-English reviews (requires GPU for optimal performance).

4. To visualize the data on an interactive map:
   [View Interactive Map](https://ishan-rawat1.github.io/CDC2024/combined_category_map.html)
   
   ```bash
   python interactive_map.py
   ```
   This will generate maps showing the best-rated locations based on your data.

## Future Work

We aim to:

* Expand the dataset to include more cities globally.
* Improve our predictive models for business success based on reviews and other metadata.
* Develop a real-time recommendation system using LLM-enriched data.

## Contributors

* **Ishan Rawat**
* **Elisei Stakovskii**
* **Narasimha Cittarusu**
* **Saksham Rustagi**


