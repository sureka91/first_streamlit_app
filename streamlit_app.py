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
