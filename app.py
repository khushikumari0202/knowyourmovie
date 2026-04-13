import pickle
import streamlit as st
import requests

OMDB_API_KEY = "your_omdb_api_key_here"  # 🔑 Replace with your OMDb API key

def fetch_poster(movie_title):
    url = "http://www.omdbapi.com/?t={}&apikey={}".format(movie_title, OMDB_API_KEY)
    data = requests.get(url)
    data = data.json()
    poster = data.get('Poster', None)
    if poster and poster != 'N/A':
        return poster
    return None

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        title = movies.iloc[i[0]].title
        recommended_movie_names.append(title)
        recommended_movie_posters.append(fetch_poster(title))  # using title instead of movie_id

    return recommended_movie_names, recommended_movie_posters


st.header('🎬 Movie Recommender System')
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)

    for col, name, poster in zip(
        [col1, col2, col3, col4, col5],
        recommended_movie_names,
        recommended_movie_posters
    ):
        with col:
            st.text(name)
            if poster:
                st.image(poster)
            else:
                st.write("🎬 No poster available")