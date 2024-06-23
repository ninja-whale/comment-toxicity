import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Step 2: Load the Dataset
url = "https://raw.githubusercontent.com/rashida048/Some-NLP-Projects/master/movie_dataset.csv"
movies_df = pd.read_csv(url)

# Step 3: Data Preprocessing
# Fill missing values
movies_df = movies_df.fillna('')

# Select relevant features
features = ['keywords', 'cast', 'genres', 'director']

# Combine selected features into a single string
def combine_features(row):
    return row['keywords'] + " " + row['cast'] + " " + row['genres'] + " " + row['director']

movies_df['combined_features'] = movies_df.apply(combine_features, axis=1)

# Step 4: Building the Recommendation Model
# Convert text data into a matrix of token counts
cv = CountVectorizer()
count_matrix = cv.fit_transform(movies_df['combined_features'])

# Compute the cosine similarity matrix based on the count matrix
cosine_sim = cosine_similarity(count_matrix)

# Step 5: Recommendation Function
def recommend(movie_title, cosine_sim=cosine_sim):
    idx = movies_df[movies_df['title'] == movie_title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]  # Top 10 similar movies
    movie_indices = [i[0] for i in sim_scores]
    return movies_df['title'].iloc[movie_indices]