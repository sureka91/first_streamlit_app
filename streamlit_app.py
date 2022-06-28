import streamlit
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#just lists a drop down of numbers that doesnt help
#streamlit.multiselect("Pick some fruits : ", list(my_fruit_list.index)) 
my_fruit_list = my_fruit_list.set_index('Fruit')
#though below helps. initially none selected
#streamlit.multiselect("Pick some fruits : ", list(my_fruit_list.index)) 

#pre-populated picklist
#streamlit.multiselect("Pick some fruits : ", list(my_fruit_list.index),['Avocado','Strawberries']) 
#streamlit.dataframe(my_fruit_list)

#We'll ask our app to put the list of selected fruits into a variable called fruits_selected. 
#Then, we'll ask our app to use the fruits in our fruits_selected list to pull rows from the full data set 
#(and assign that data to a variable called fruits_to_show). Finally, we'll ask the app to use the data in 
#fruits_to_show in the dataframe it displays on the page. 
fruits_selected = streamlit.multiselect("Pick some fruits : ", list(my_fruit_list.index),['Avocado','Strawberries']) 
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

#import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response)

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json()) #{'genus': 'Citrullus', 'name': 'Watermelon', 'id': 25, 'family': 'Cucurbitaceae', 'or

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
#my_data_row = my_cur.fetchone()
my_data_row = my_cur.fetchall()
#streamlit.text("Hello from Snowflake:")
streamlit.text("THE FRUIT LOAD LIST CONTAINS")
#streamlit.text(my_data_row)
streamlit.dataframe(my_data_row)

#allow the user to add a fruit to the list
add_my_fruit = streamlit.text_input('What fruit would you like to add?','Mozambie')
streamlit.write('Thanks for adding ', add_my_fruit)
