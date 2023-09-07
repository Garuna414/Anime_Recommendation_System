# Anime Recommendation System

Welcome to the Anime Recommendation System! This machine learning-based system utilizes Python libraries such as Pandas, NumPy, Streamlit, NLTK, Scikit-learn, and Pickle to recommend anime similar to the one selected by the user. The system preprocesses and transforms anime descriptions into tags, extracts main words, converts them into vectors, and calculates cosine similarities to find and display the top 10 similar anime. It distinguishes between anime TV shows and movies for tailored recommendations.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Development](#development)
- [License](#license)

## Overview

The Anime Recommendation System is designed to help users discover new anime based on their preferences. It operates by analyzing anime descriptions, extracting key information, and identifying similar anime based on their content. Whether you're a fan of anime TV shows or movies, this system has you covered.

## Features

- Preprocessing: Removes null values and transforms anime descriptions into tags.
- Keyword Extraction: Utilizes NLTK to identify main words from the descriptions.
- Vectorization: Converts keywords into vectors for similarity calculations.
- Cosine Similarity: Calculates similarity scores between anime to recommend the most relevant ones.
- Genre-Based Recommendations: Recommends anime TV shows or movies based on user preferences.
- User-Friendly Interface: Powered by Streamlit, with a search bar and "recommend" button for ease of use.

## Getting Started

To use the Anime Recommendation System, follow these steps:

1. Download last pickle file from here: https://www.dropbox.com/scl/fi/cdhaifpz4emyv3wzynvlm/sim_tv.pkl?rlkey=skbg72pufztrh2ytulbr7ouz6&dl=0
2. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Garuna414/Anime_Recommendation_System.git
   ```

3. Install the required dependencies:

   ```bash
   pip install pandas numpy streamlit nltk scikit-learn
   ```

4. Navigate to the project directory:

   ```bash
   cd anime-recommendation-system
   ```

5. Launch the Streamlit app:

   ```bash
   streamlit run anime_recommendation.py
   ```

6. Access the system through your web browser and start discovering new anime!

## Usage

1. **Search**: Enter the name of the anime you're interested in into the search bar.

2. **Recommend**: Click the "recommend" button to receive a list of the top 10 anime that are similar to your selected one.

3. **Choose Type**: Specify whether you want recommendations for anime TV shows or movies by selecting the appropriate option.

4. **Results**: View the recommended anime along with their titles, genres, and descriptions.

## Development

The Anime Recommendation System is built using Python and leverages popular libraries and techniques for natural language processing and recommendation systems. You can explore the codebase to understand how the system processes anime data, extracts keywords, and calculates similarity scores.


## License

The Anime Recommendation System is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the system as long as you provide appropriate attribution and maintain the original license. Enjoy discovering new anime with our recommendation system!
