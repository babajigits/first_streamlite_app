import streamlit
streamlit.title('Complete Badges in Snowflake')
streamlit.header('Badge 1 has been completed')
streamlit.text('It was fun learning')
streamlit.text('I will complete the badge 2 also')
streamlit.text('I will update on linkedin after the badge 2')

import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# we will add a multiselect so that users can pick what they want
streamlit.multiselect("Pick some Fruits:", list(my _fruit_list.index))

#Display the table on the page
streamlit.dataframe(my_fruit_list)


