

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

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
                 

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json())

# write your own comment - Normalizing the json output from API response
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - creating a dataframe from normalized data 
streamlit.dataframe(fruityvice_normalized)

#snowflake connector 
import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header ("The fruit load list contains:")
streamlit.dataframe(my data rows)







