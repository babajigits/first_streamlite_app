

import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('Complete Badges in Snowflake')
streamlit.header('Badge 1 has been completed')
streamlit.text('It was fun learning')
streamlit.text('I will complete the badge 2 also')
streamlit.text('I will update on linkedin after the badge 2')


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
#create a new code block to get repeated entry 

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get ("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized


#New Section to display fruityvice api response
streamlit.header( 'Fruitvvice Fruit Advice! ')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit. error()


#stop here for now until we fix the issue
#streamlit.stop()

#snowflake connector 


#Snowflake-related functions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()

# Add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  my_cnx.close()
  streamlit.dataframe(my_data_rows)

fruit_choice = streamlit.text_input('What fruit would you like to add?','Jackfruit')
#new code

streamlit.stop()

def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit load list values ('" + my_data_rows + "')")
    return "Thanks for adding "+ new_fruit
  
add_my_fruit = streamlit.text_input ('What fruit would you like to add?')
if streamlit.button('Add a Fruit to the List'):
  my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_fruit)
  streamlit.text (back_from_function)





