import streamlit
streamlit.title('Complete Badges in Snowflake')
streamlit.header('Badge 1 has been completed')
streamlit.text('It was fun learning')
streamlit.text('I will complete the badge 2 also')
streamlit.text('I will update on linkedin after the badge 2')

import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list=my_fruit_list.set_index('Fruit')

# we will add a multiselect so that users can pick what they want
fruits_selected = streamlit.multiselect("Pick some Fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

#fruits_selected = streamlit.multiselect("Pick some Fruits:", list(my_fruit_list.index))

#Fruits to show
fruits_to_show=my_fruit_list.loc[fruits_selected]

#Display the table on the page
streamlit.dataframe(fruits_to_show)

#let's put a pick list here
#streamlit.multiselect("Pick some Fruits:", list(my_fruit_list.index),['Avacado','Strawberries'])

#Fruitvice API response
streamlit.header('Fruitvice Fruit Advice!')
                 

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())





