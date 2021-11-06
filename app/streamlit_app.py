import streamlit as st
import pandas as pd
import time
import matplotlib as plt
import os


# zaczynamy od zaimportowania bibliotek

# st.success('Gratulacje! Z powodzeniem uruchomiłeś aplikację')
# streamlit jest wykorzystywany do tworzenia aplikacji
# z tego powodu dobrą praktyką jest informowanie użytkownika o postępie, błędach, etc.



# TODO share.streamlit.io - share github repo

# Inne przykłady do wypróbowania:
# st.balloons() # animowane balony ;)
# st.error('Błąd!') # wyświetla informację o błędzie
# st.warning('Ostrzeżenie, działa, ale chyba tak sobie...')
# st.info('Informacja...')
# st.success('Udało się!')

# możemy dzięki temu "ukryć" późniejsze ładowanie aplikacji

st.image("https://github.com/alwaysbfrank/suml-germanizer/raw/d182ca100b49722e44934452429c11a3ba75d499/assets/logo.jpg")
st.title('Germanizer')

st.header('Instrukcja')
st.text('Wybierz silnik, wpisz tekst po angielsku i naciśnij ctrl + enter.')

import streamlit as st
from transformers import pipeline

option = st.selectbox(
    "Opcje",
    [
        "Wydźwięk emocjonalny tekstu (eng)",
        "English -> German",
    ],
)

if option == "Wydźwięk emocjonalny tekstu (eng)":
    text = st.text_area(label="Wpisz tekst")
    if text:
        sentimentClassifier = pipeline("sentiment-analysis")
        answer = sentimentClassifier(text)
        st.write(answer)

if option == "English -> German":
    text = st.text_area(label="Wpisz tekst")
    if text:
        with st.spinner(text="Translating"):
            germanClassifier = pipeline("translation_en_to_de")
            payload = germanClassifier(text)
            answer = payload[0]["translation_text"]
            if answer:
                st.success('Translation done')
                st.write(answer)
            else:
                st.error('Error while translating')

st.subheader('Autor')
st.text('Franek Matera s16289')
