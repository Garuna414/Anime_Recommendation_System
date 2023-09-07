import streamlit as st
import pickle
import pandas as pd

def recommend(anime_name, anime_type):
    #anime_index = new_anime[new_anime['Name'] == anime_name].index[0]
    '''anime_index = anime_tv[anime_tv['Name'] == anime_name]
    rank = anime_index.iloc[0]['Index'] - 1
    distance = similarity_tv[rank]
    #distance = similarity[anime_index]
    anime_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x:x[1])[1:11]
    print(rank)
    print(new_anime.iloc[rank]['Rank'])'''
    if anime_type == 'Movie':
        anime_index = anime_movies[anime_movies['Name'] == anime_name]
        rank = anime_index.iloc[0]['Index'] - 1
        distance = similarity_movies[rank]
        #distance = similarity[anime_index]
        anime_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x:x[1])[1:11]
        #print(rank)
        #print(anime_movies.iloc[rank]['Rank'])
        recommended_anime = []
        for i in anime_list:
            #print(anime_movies.iloc[i[0]]['Name'])
            recommended_anime.append(anime_movies.iloc[i[0]]['Name'])
    else:
        anime_index = anime_tv[anime_tv['Name'] == anime_name]
        rank = anime_index.iloc[0]['Index'] - 1
        distance = similarity_tv[rank]
        #distance = similarity[anime_index]
        anime_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x:x[1])[1:11]
        print(rank)
        #print(anime_tv.iloc[rank]['Rank'])
        recommended_anime = []
        for i in anime_list:
            #print(anime_tv.iloc[i[0]]['Name'])
            recommended_anime.append(anime_tv.iloc[i[0]]['Name'])
    return recommended_anime

anime_tv_dict = pickle.load(open('anime_tv_dict.pkl', 'rb'))
anime_movies_dict = pickle.load(open('anime_movies_dict.pkl', 'rb'))

anime_tv = pd.DataFrame(anime_tv_dict)
anime_movies = pd.DataFrame(anime_movies_dict)

similarity_tv = pickle.load(open('sim_tv.pkl', 'rb'))
similarity_movies = pickle.load(open('sim_movies.pkl', 'rb'))

anime_dict = pickle.load(open('anime_dict.pkl', 'rb'))
anime = pd.DataFrame(anime_dict)

st.title('Anime Recommender')

selected_name = st.selectbox('Select name of anime', anime['Name'].values)
name = anime[anime['Name'] == selected_name]
selected_type = name.iloc[0]['Type']

if st.button('Recommend Anime'):
    recommeded = recommend(selected_name, selected_type)
    for i in recommeded:
        st.write(i)