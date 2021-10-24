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

#st.spinner()
#with st.spinner(text='Pracuję...'):
#    time.sleep(2)
#    st.success('Done')
#    time.sleep(2)
# możemy dzięki temu "ukryć" późniejsze ładowanie aplikacji

st.image("..\\assets\\logo.jpg")
st.title('Germanizer')

st.header('Instrukcja')
st.text('Wybierz silnik, wpisz tekst po angielsku i naciśnij ctrl + enter.')
# header to jeden z podtytułów wykorzystywnaych w Streamlit

st.code("st.write()", language='python')
# code może nam się czasami przydać, jeżeli chcielibyśmy pokazać np. klientowi fragment kodu, który wykorzystujemy w aplikacji

with st.echo():
    st.write("Echo")
# możemy też to zrobić prościej używając echo - pokazujemy kod i równocześnie go wykonujemy

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
        classifier = pipeline("sentiment-analysis")
        answer = classifier(text)
        st.write(answer)

if option == "English -> German":
    text = st.text_area(label="Wpisz tekst")
    if text:
        with st.spinner(text="Translating"):
            classifier = pipeline("translation_en_to_de")
            payload = classifier(text)
            answer = payload[0]["translation_text"]
            if answer:
                st.success('Translation done')
                st.write(answer)
            else:
                st.error('Error while translating')

st.subheader('Autor')
st.text('Franek Matera s16289')
#st.write('Wykorzystaj Huggin Face do stworzenia swojej własnej aplikacji tłumaczącej tekst z języka angielskiego na język niemiecki. Zmodyfikuj powyższy kod dodając do niego kolejną opcję, tj. tłumaczenie tekstu. Informacje potrzebne do zmodyfikowania kodu znajdziesz na stronie Huggin Face - https://huggingface.co/transformers/usage.html')
#st.write('🐞 Dodaj właściwy tytuł do swojej aplikacji, może jakieś grafiki?')
#st.write('🐞 Dodaj krótką instrukcję i napisz do czego służy aplikacja')
st.write('🐞 Wpłyń na user experience, dodaj informacje o ładowaniu, sukcesie, błędzie, itd.')
st.write('🐞 Na końcu umieść swój numer indeksu')
st.write('🐞 Stwórz nowe repozytorium na GitHub, dodaj do niego swoją aplikację, plik z wymaganiami (requirements.txt)')
st.write('🐞 Udostępnij stworzoną przez siebie aplikację (https://share.streamlit.io) a link prześlij do prowadzącego')
