

import streamlit as st
import pickle
import pandas as pd
import requests




def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distannces = similarity[movie_index]
    movie_list = (sorted(list(enumerate(distannces)), reverse=True, key=lambda x: x[1]))[1:6]


    recommended_movies = []

    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict =  pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))



st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
'write the name of movie',
movies['title'].values)

if st.button('Recommend'):
        recommendations = recommend(selected_movie_name)
        for i in recommendations:
            st.write(i)

