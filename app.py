import streamlit as st
from textblob import TextBlob
from pattern.en import pluralize, singularize, comparative, superlative
import streamlit.components.v1 as components
import nltk

# Download NLTK corpora
nltk.download('punkt')

def main():
    st.title("Spell Correction")

    text_data = st.text_area("Enter Text Here")
    a = TextBlob(text_data)
    
    if st.button("Correct"):
        st.success(a.correct())

    text_data1 = st.text_input("Enter a word For pluralize / singularize")
    
    if st.checkbox("pluralize"):
        st.warning(pluralize(text_data1))
    
    if st.checkbox("singularize"):
        st.warning(singularize(text_data1))

    text2 = st.text_input("Enter Text For comparative & superlative")
    
    if st.checkbox("comparative"):
        st.success(comparative(text2))
    
    if st.checkbox("superlative"):
        st.success(superlative(text2))

if __name__ == '__main__':
    main()
