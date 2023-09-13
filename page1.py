import streamlit as st
import pandas as pd
from fuzzywuzzy import fuzz


@st.cache_data()
def load_data():
    df = pd.read_csv('dataset.csv')
    df = df.dropna(subset=['CapitalLatitude', 'CapitalLongitude', 'CapitalName', 'CountryName', 'ContinentName'])
    return df


def page1():
    st.title('GeoGame')

    df = load_data()
    continents = df['ContinentName'].unique()
    default_continent_index = list(continents).index('Europe')
    selected_continent = st.sidebar.selectbox('Select Continent', continents, index=default_continent_index)

    continent_df = df[df['ContinentName'] == selected_continent]
    dfmap = continent_df.rename(columns={'CapitalLatitude': 'lat', 'CapitalLongitude': 'lon'})

    # Game mode switch
    game_mode = st.sidebar.radio('Game Mode', ['Guess the Capital', 'Guess the Country', 'Guess the Flag'])

    if 'random_row' not in st.session_state:
        st.session_state.random_row = continent_df.sample(1).iloc[0]
    if 'next_question' not in st.session_state:
        st.session_state.next_question = False
    if 'last_selected_continent' not in st.session_state:
        st.session_state.last_selected_continent = 'Europe'
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'streak' not in st.session_state:
        st.session_state.streak = 0
    if 'guess' not in st.session_state:
        st.session_state.guess = ''
    if 'allow_next' not in st.session_state:
        st.session_state.allow_next = False
    if 'checked' not in st.session_state:
        st.session_state.checked = False
    if st.session_state.last_selected_continent != selected_continent or \
            (st.session_state.next_question and (st.session_state.allow_next or st.session_state.checked)):
        st.session_state.random_row = continent_df.sample(1).iloc[0]
        st.session_state.next_question = False
        st.session_state.checked = False
        st.session_state.last_selected_continent = selected_continent

    random_row = st.session_state.random_row


    if game_mode == 'Guess the Flag':
        st.image(f'flags/{random_row["CountryName"]}_flag.jpg')  # Display the flag image
        st.session_state.guess = st.text_input('Guess the Country', value=st.session_state.guess)
    else:
        st.write(
            f"The Country is: **{random_row['CountryName']}**" if game_mode == 'Guess the Capital' else f"The Capital is: **{random_row['CapitalName']}**")
        st.session_state.guess = st.text_input('Your Guess', value=st.session_state.guess)


    # Display hints

    # Score and Streak Tracker
    score = st.sidebar.markdown(f"### Score: **{st.session_state.score}**")
    streak = st.sidebar.markdown(f"### Streak: **{st.session_state.streak}**")

    score
    streak

    # Check the guess
    correct_answer = random_row['CountryName'] if game_mode == 'Guess the Flag' else (
        random_row['CapitalName'] if game_mode == 'Guess the Capital' else random_row['CountryName'])
    if st.button('Check'):
        if st.session_state.guess.lower() == correct_answer.lower():
            st.success("Correct!")
            st.session_state.score += 1
            st.session_state.streak += 1
            st.session_state.next_question = True
            st.session_state.allow_next = True
            st.session_state.checked = True
            st.session_state.guess = ''
        elif fuzz.ratio(st.session_state.guess.lower(), correct_answer.lower()) > 80:
            st.warning("Close call, try again.")
        else:
            st.error("Incorrect. Try again.")
            st.session_state.streak = 0

    if st.button('Give solution'):
        st.write(f"Solution: **{correct_answer}**")
        st.session_state.streak = 0
        streak.markdown(f"### Streak: **{st.session_state.streak}**")




    if st.button('Next'):
        if st.session_state.allow_next or st.session_state.checked:
            st.session_state.next_question = True
            st.session_state.guess = ''
            st.session_state.allow_next = False
            st.session_state.show_solution = False
        else:
            st.warning("You need to answer correctly or view the solution before moving to the next question.")

    if game_mode == 'Guess the Capital':
        show_capital_pic = st.sidebar.checkbox('Show Capital Picture')
        if show_capital_pic:
            st.image(f'capitals/{random_row["CapitalName"]}_city.jpg')
    if game_mode == 'Guess the Country':
        show_flag_pic = st.sidebar.checkbox('Show Flag Picture')
        if show_flag_pic:
            st.image(f'flags/{random_row["CountryName"]}_flag.jpg')
    else:
        pass

    hints = st.sidebar.checkbox('Show Hints', value=False)

    if hints:
        st.write(f"Continent: **{random_row['ContinentName']}**")
        st.write(f"Official Language: **{random_row['Official language']}**")
        st.write(f"Population: **{random_row['Population']}**")
        if game_mode == 'Guess the Capital':
            st.write(f"Possible Answers: **{random_row['CapitalName'][:3]}**")
        else:
            st.write(f"Possible Answers: **{random_row['CountryName'][:3]}**")

        description = st.checkbox('Show Capital Description')
        if description:
            st.markdown(f"Description: \n\n{random_row['CapitalDescription']}", unsafe_allow_html=True)

    show_map = st.sidebar.checkbox('Show Worldmap', value=False)
    if show_map:
        if game_mode == 'Guess the Capital':
            show_focus_map = st.sidebar.button('Focus Map on Capital')
            if show_focus_map:
                map_data = dfmap[dfmap['CapitalName'] == random_row['CapitalName']][['lat', 'lon']]
            else:
                map_data = dfmap[['lat', 'lon']]
        else:
            show_focus_map = st.sidebar.button('Focus Map on Country')
            if show_focus_map:
                map_data = dfmap[dfmap['CountryName'] == random_row['CountryName']][['lat', 'lon']]
            else:
                map_data = dfmap[['lat', 'lon']]
        st.map(map_data, zoom=1)


if __name__ == "__main__":
    page1()
