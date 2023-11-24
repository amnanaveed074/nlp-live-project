mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml


# streamlit==0.88.0
# textblob==0.15.3
# pattern==3.6
# python_version == "3.8"
