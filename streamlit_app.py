import streamlit
streamlit.title('Complete Badges in Snowflake')
streamlit.header('Badge 1 has been completed')
streamlit.text('It was fun learning')
streamlit.text('I will complete the badge 2 also')
streamlit.text('I will update on linkedin after the badge 2')

import pandas
my_fruit_list=pandas.readcsv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
