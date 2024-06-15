import streamlit as st
import pickle
import pandas as pd

# Set the page configuration
st.set_page_config(page_title='Movie Recommendation System', page_icon='🎬', layout='wide')

# Custom CSS for styling
st.markdown("""
    <style>
    .title {
        font-size: 48px;
        color: #FF4B4B;
        text-align: center;
        margin-bottom: 40px;
    }
    .recommendations {
        font-size: 24px;
        color: #1DB954;
        margin-top: 20px;
    }
    .movie-title {
        font-size: 20px;
        font-weight: bold;
        margin: 10px 0;
    }
    .stButton>button {
        color: white;
        background-color: #FF4B4B;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        font-size: 16px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #FF6B6B;
    }
    </style>
    """, unsafe_allow_html=True)

# Title of the Streamlit app
st.markdown('<p class="title">Movie Recommendation System</p>', unsafe_allow_html=True)

# Load the movie recommendations from movies.pkl
with open('movies.pkl', 'rb') as file:
    movies_dict = pickle.load(file)

# Convert the dictionary to a DataFrame for recommendations
movies_recommend = pd.DataFrame(movies_dict)

# Load pre-processed movie details from pre_process_df.csv for filtering
movies_genres = pd.read_csv('pre_process_df.csv')

# Remove square brackets from features
def remove_square_brackets(text):
    if isinstance(text, str):
        return text.strip("[]").replace("'", "").replace('"', '').replace(" ", "").split(",")
    else:
        return []

movies_genres['cast'] = movies_genres['cast'].apply(remove_square_brackets)
movies_genres['crew'] = movies_genres['crew'].apply(remove_square_brackets)
movies_genres['genres'] = movies_genres['genres'].apply(remove_square_brackets)
movies_genres['keywords'] = movies_genres['keywords'].apply(remove_square_brackets)

# Load the similarity matrix for recommendations
with open('similarity.pkl', 'rb') as f:
    cosine_sim = pickle.load(f)

# Function to get movie recommendations for a given movie title
def recommend_movies(movie):
    # Find the index of the selected movie
    movie_index = movies_recommend[movies_recommend['title'] == movie].index
    if len(movie_index) == 0:
        st.error("Movie not found!")
        return []
    else:
        movie_index = movie_index[0]  # Select the first index if multiple matches

    # Get the similarity scores for the selected movie
    distances = cosine_sim[movie_index]

    # Get a list of (index, similarity score) tuples and sort them in descending order of similarity score
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    # Fetch the titles of the top 5 recommended movies
    recommended_movies = [movies_recommend.iloc[i[0]].title for i in movie_list]
    return recommended_movies

# Function to get top 5 movies for a selected cast member
def top_movies_by_cast(cast_name):
    # Filter movies that contain the selected cast member
    movies_with_cast = movies_genres[movies_genres['cast'].apply(lambda x: cast_name in x)]

    if movies_with_cast.empty:
        st.error("No movies found for the selected cast member.")
        return []

    # Get the top 5 recommended movies based on the first movie found for the cast member
    first_movie_title = movies_with_cast.iloc[0]['title']
    return recommend_movies(first_movie_title)[:5]

# Function to get top 5 movies for a selected crew member
def top_movies_by_crew(crew_name):
    # Filter movies that contain the selected crew member
    movies_with_crew = movies_genres[movies_genres['crew'].apply(lambda x: crew_name in x)]

    if movies_with_crew.empty:
        st.error("No movies found for the selected crew member.")
        return []

    # Get the top 5 recommended movies based on the first movie found for the crew member
    first_movie_title = movies_with_crew.iloc[0]['title']
    return recommend_movies(first_movie_title)[:5]

# Define layout columns
col1, col2, col3, col4 = st.columns(4)

# Top left corner: Movie recommendation
with col1:
    st.markdown('### Movie Recommendation')
    selected_movie_name = st.selectbox('Select a movie to get recommendations:', movies_recommend['title'].values)

    if st.button('Recommend'):
        st.markdown(f'<p class="recommendations">Similar movies like {selected_movie_name}:</p>', unsafe_allow_html=True)
        recommendations = recommend_movies(selected_movie_name)

        for movie in recommendations:
            st.markdown(f'<p class="movie-title">{movie}</p>', unsafe_allow_html=True)

# Top right corner: Selection by cast name
with col2:
    st.markdown('### Select by Cast Name')
    all_cast_names = set(cast for cast_list in movies_genres['cast'] for cast in cast_list)
    selected_cast = st.selectbox('Select a cast member to list top movies:', sorted(all_cast_names))

    if selected_cast:
        st.markdown(f'<p class="recommendations">Top 5 Movies for {selected_cast}:</p>', unsafe_allow_html=True)
        top_movies_cast = top_movies_by_cast(selected_cast)

        for movie in top_movies_cast:
            st.markdown(f'<p class="movie-title">{movie}</p>', unsafe_allow_html=True)

# Bottom left corner: Selection by crew name
with col3:
    st.markdown('### Select by crew name')
    all_crew_names = set(crew for crew_list in movies_genres['crew'] for crew in crew_list)
    selected_crew = st.selectbox('Select a crew member to list top movies:', sorted(all_crew_names))

    if selected_crew:
        st.markdown(f'<p class="recommendations">Top 5 Movies for {selected_crew}:</p>', unsafe_allow_html=True)
        top_movies_crew = top_movies_by_crew(selected_crew)

        for movie in top_movies_crew:
            st.markdown(f'<p class="movie-title">{movie}</p>', unsafe_allow_html=True)

# Bottom right corner: Selection by genre
with col4:
    st.markdown('### Select by Genre')
    all_genres = set(genre for genre_list in movies_genres['genres'] for genre in genre_list)
    selected_genre = st.selectbox('Select a genre to list movies:', sorted(all_genres))

    if selected_genre:
        st.markdown(f'<p class="recommendations">Movies in the {selected_genre} genre:</p>', unsafe_allow_html=True)
        filtered_movies = movies_genres[movies_genres['genres'].apply(lambda x: selected_genre in x)]
        for title in filtered_movies['title'].head(10).values:
            st.markdown(f'<p class="movie-title">{title}</p>', unsafe_allow_html=True)
