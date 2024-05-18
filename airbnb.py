import json
import csv
import pandas as pd
import pydeck as pdk

import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st

from sqlalchemy import create_engine
import sqlalchemy
from streamlit import connections
import pymysql
import streamlit as st
import plotly.graph_objects as go


 
 
# Opening JSON file and loading the data
# into the variable data
with open('E:\\Airbnb\\sample_airbnb.json') as json_file:
    data = json.load(json_file)

data_df = pd.DataFrame(data)

#data_df.to_excel("E:\\data.xlsx")

engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="root",
                               pw="",
                               db="airbnb"))

# class AirbnbDataProcessor:
#     def __init__(self, data_df):
#         self.data_df = data_df

#     def room_details(self):
#         airbnb_room_details_df = self.data_df[['_id', 'listing_url', 'name', 'property_type', 'room_type', 'bed_type', 'minimum_nights', 'maximum_nights', 'cancellation_policy', 'last_scraped', 'calendar_last_scraped', 'first_review', 'last_review', 'accommodates', 'bedrooms', 'beds', 'number_of_reviews', 'bathrooms', 'price', 'security_deposit', 'cleaning_fee', 'extra_people', 'guests_included', 'weekly_price', 'monthly_price', 'reviews_per_month']]
#         return airbnb_room_details_df

#     def room_availability(self):
#         availability_data = (self.data_df['_id'].astype(str) + ' ' + self.data_df['availability'].astype(str)).tolist()
#         dfs = []

#         for entry in availability_data:
#             index, dictionary = entry.split(' ', 1)
#             index = int(index)
#             dictionary = eval(dictionary)

#             availability_df = pd.DataFrame([dictionary])
#             availability_df.index = [index]
#             dfs.append(availability_df)

#         availability_df = pd.concat(dfs)
#         availability_df['_id'] = availability_df.index
#         availability_df.reset_index(drop=True, inplace=True)
#         return availability_df

#     def address_details(self):
#         address_data = (self.data_df['_id'].astype(str) + ' ' + self.data_df['address'].astype(str)).tolist()
#         dfs = []

#         for entry in address_data:
#             index, dictionary = entry.split(' ', 1)
#             index = int(index)
#             dictionary = eval(dictionary)

#             address_data_df = pd.DataFrame([dictionary])
#             address_data_df.index = [index]
#             dfs.append(address_data_df)

#         address_data_df = pd.concat(dfs)
#         address_data_df['_id'] = address_data_df.index
#         address_data_df.reset_index(drop=True, inplace=True)

#         ad = []
#         z = address_data_df['location']
#         for entry in z:
#             coordinates = entry['coordinates']
#             address = {
#                 'longitude': coordinates[0],
#                 'latitude': coordinates[1]
#             }
#             ad.append(address)

#         ad_df = pd.DataFrame(ad)
#         address_data_df = pd.concat([address_data_df, ad_df], axis=1)
#         return address_data_df

#     def review_score(self):
#         review_score_data = (self.data_df['_id'].astype(str) + ' ' + self.data_df['review_scores'].astype(str)).tolist()
#         dfs = []

#         for entry in review_score_data:
#             index, dictionary = entry.split(' ', 1)
#             index = int(index)
#             dictionary = eval(dictionary)

#             review_score_df = pd.DataFrame([dictionary])
#             review_score_df.index = [index]
#             dfs.append(review_score_df)

#         review_score_df = pd.concat(dfs)
#         review_score_df['_id'] = review_score_df.index
#         review_score_df.reset_index(drop=True, inplace=True)
#         return review_score_df

#     def host_details(self):
#         host_data = (self.data_df['_id'].astype(str) + ' ' + self.data_df['host'].astype(str)).tolist()
#         dfs = []

#         for entry in host_data:
#             index, dictionary = entry.split(' ', 1)
#             index = int(index)
#             dictionary = eval(dictionary)

#             host_df = pd.DataFrame([dictionary])
#             host_df.index = [index]
#             dfs.append(host_df)

#         host_result_df = pd.concat(dfs)
#         host_result_df['_id'] = host_result_df.index
#         host_result_df.reset_index(drop=True, inplace=True)

#         return host_result_df
#     def reviews_data_details(self):
#         reviews_data = self.data_df['reviews'].tolist()
#         all_reviews =[]
#         for review_list in reviews_data:
#         # Iterate over each dictionary in the sublist
#             for review in review_list:
   
#                 review_dict = {

#                     'r_id': review.get('_id',None),
#                     'rdate': review.get('date',None),
#                     'listing_id': review.get('listing_id',None),
#                     'reviewer_id': review.get('reviewer_id',None),
#                     'reviewer_name': review.get('reviewer_name',None),
#                     'rcomments': review.get('comments',None),


#         }
#         all_reviews.append(review_dict)

#         all_reviews_df = pd.DataFrame(all_reviews)
#         return all_reviews_df

# #Creating instance to access the class:
# airbnb_processor = AirbnbDataProcessor(data_df)

# room_details_df = airbnb_processor.room_details()
# availability_df = airbnb_processor.room_availability()
# address_df = airbnb_processor.address_details()
# review_score_df = airbnb_processor.review_score()
# host_df = airbnb_processor.host_details()
# review_details_df = airbnb_processor.reviews_data_details()


# #Convert to Excel for Power Bi:
# room_details_df.to_excel("E:\\airbnb\\room_details.xlsx")
# availability_df.to_excel("E:\\airbnb\\availability_details.xlsx")
# address_df.to_excel("E:\\airbnb\\address_details.xlsx")
# review_score_df.to_excel("E:\\airbnb\\review_score_details.xlsx")
# host_df.to_excel("E:\\airbnb\\host_details.xlsx")
# review_details_df.to_excel("E:\\airbnb\\review_details.xlsx")

# #data pre-processing:

# mappings = {
#     "United States": "United States of America",
#     "Turkey": "Turkey",
#     "Hong Kong": "China",
#     "Australia": "Australia",
#     "Portugal": "Portugal",
#     "Brazil": "Brazil",
#     "Canada": "Canada",
#     "Spain": "Spain",
#     "China": "China"
# }

#address_df['country'] = address_df['country'].replace(mappings)
#room_details_df.drop(['weekly_price', 'monthly_price', 'reviews_per_month'], axis=1, inplace=True)
#room_details_df.info()
#availability_df.info()

#address_df.info()
# #review_score_df.fillna({'review_scores_accuracy': 0,
#                         'review_scores_cleanliness': 0,
#                         'review_scores_checkin': 0,
#                         'review_scores_communication': 0,
#                         'review_scores_location': 0,
#                         'review_scores_value': 0,
#                         'review_scores_rating': 0}, inplace=True)

#review_score_df.info()


#host_df.fillna(0,inplace=True)
#address_df.drop(['location'],axis=1,inplace=True)
#host_df.drop(['host_verifications'],axis=1,inplace=True)
#host_df.info()


#room_details_df.to_sql("room_details",con=engine,if_exists="append",index=False)
#availability_df.to_sql("availability_details",con=engine,if_exists='append',index=False)
#address_df.to_sql("address_details",con=engine,if_exists='replace',index=False)
#review_score_df.to_sql("review_score_details",con=engine,if_exists='append',index=False)

#host_df.to_sql("host_details",con=engine,if_exists='replace',index=False)
#review_details_df.to_sql("all_review_details",con=engine,if_exists='replace',index=False)




#Streamlit Design part:



# Streamlit app title
st.set_page_config(
    page_title="Airbnb Listings Geospatial Visualization",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded")
st.title("Airbnb Listings Geospatial Visualization")

st.markdown(
    """
    <style>
    body {
        font-size: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

col = st.columns((1.5, 4.5, 2), gap='medium')

with col[1]:
    st.markdown('#### Airbnb Worldwide')
    query = """
    SELECT rd._id, rd.name, rd.price, rd.property_type, rs.review_scores_rating, av.availability_365, ad.country, ad.country_code, ad.latitude, ad.longitude FROM room_details rd INNER JOIN review_score_details rs ON rd._id = rs._id INNER JOIN availability_details av ON rd._id = av._id INNER JOIN address_details ad ON rd._id = ad._id limit 5000;"""

    data = pd.read_sql(query, engine)
    st.sidebar.header("Filter Options")
    selected_cities = st.sidebar.multiselect("Select Country", options=data["country"].unique(), default=data["country"].unique())
    selected_property_type = st.sidebar.selectbox("Select Property Type", options=data["property_type"].unique())

    filtered_df = data[(data["country"].isin(selected_cities)) & (data["property_type"] == selected_property_type)]
layer = pdk.Layer(
    'ScatterplotLayer',
    filtered_df,
    get_position='[longitude, latitude]',
    get_radius=50000,  # Radius in meters
    get_color=[255, 0, 0],  # Blue color
    pickable=True,
    auto_highlight=True,
    tooltip={
        "text": "<b>City:</b> {country} <br/> <b>Property Type:</b> {property_type}"
    }
)

# Set the viewport location
view_state = pdk.ViewState(
    latitude=filtered_df['latitude'].mean(),
    longitude=filtered_df['longitude'].mean(),
    zoom=2,
    pitch=0
)

# Render the deck.gl map
r = pdk.Deck(
    layers=[layer], 
    initial_view_state=view_state,
    map_style='mapbox://styles/mapbox/streets-v11',  # Change the map style here
    tooltip={"html": "<b>Country:</b> {country} <br/> <b>Property Type:</b> {property_type} <br/> <b>Review Score:</b> {review_scores_rating}", 
             "style": {"color": "white"}}
)
st.pydeck_chart(r)

# Main menu options
main_menu_options = ["Availability Analysis", "Price Analysis"]
main_menu_selection = st.selectbox("Main Menu", main_menu_options)

if main_menu_selection == "Availability Analysis":
    # Submenu options for availability analysis
    availability_submenus = ["availability_90", "availability_365"]
    availability_selection = st.radio("Availability Analysis", availability_submenus)
    

    # Availability Analysis Query:
   
    if availability_selection == 'availability_90':
        query3 = """select av.availability_365,av._id,rd.name,rd.property_type,rd.room_type,rd.price,ad.country_code from availability_details av INNER JOIN room_details rd ON rd._id = av._id INNER JOIN address_details ad ON ad._id = rd._id where av.availability_90 > 75;"""
        result = pd.read_sql(query3,engine)
        st.write(result)
    elif availability_selection == 'availability_365':
        query4 = """select av.availability_365,av._id,rd.name,rd.property_type,rd.room_type,rd.price,ad.country_code from availability_details av INNER JOIN room_details rd ON rd._id = av._id INNER JOIN address_details ad ON ad._id = rd._id where av.availability_365 > 360;"""
        result = pd.read_sql(query4,engine)
        histogram = px.histogram(result, x='country_code', nbins=30, title='Distribution of Availability (365 days)')
        st.plotly_chart(histogram)
        scatter_plot = px.scatter(result, x='availability_365', y='price', color='country_code',title='Price vs. Availability (365 days)')
        st.plotly_chart(scatter_plot)
        box_plot_room_type = px.box(result, x='room_type', y='availability_365', title='Availability by Room Type')
        st.plotly_chart(box_plot_room_type)
        st.write(result)
        st.subheader("Insights")
        st.write("Seasonal factors might play a significant role in availability. For instance, tourist seasons can cause fluctuations in Airbnb availability. High availability could indicate off-peak periods. Economic factors such as the strength of local currencies, travel restrictions, or promotional activities might influence tourist inflow and thus the availability of Airbnb listings.urkey (TR): The high availability in Turkey might indicate a large supply of Airbnb listings, possibly due to a high number of property owners leveraging Airbnb as a means of income. It could also suggest a lower demand relative to supply, leading to higher availability.")

elif main_menu_selection == "Price Analysis":
    price_analysis_submenus = ['Avg Price Vs Country', 'Price Vs Property']
    price_analysis_selection = st.radio('Select Price Analysis Visualization', price_analysis_submenus)

    # price Analysis Section:
    query = """SELECT ad.country, AVG(rd.price) AS avg_price, rd.property_type, av.availability_365 FROM room_details rd INNER JOIN review_score_details rs ON rd._id = rs._id INNER JOIN availability_details av ON rd._id = av._id INNER JOIN address_details ad ON rd._id = ad._id GROUP BY ad.country ORDER BY avg_price DESC LIMIT 6000;"""

    price_country_df = pd.read_sql(query, engine)

    if price_analysis_selection == 'Avg Price Vs Country':
        # Price Vs Country comparison:
        fig = px.bar(
            price_country_df,
            x='country',
            y='avg_price',
            title='Average Airbnb Price by Country',
            labels={'country': 'Country', 'avg_price': 'Average Price'},
            color='avg_price',
            color_continuous_scale=px.colors.sequential.Viridis
        )

        # Display the bar chart
        st.plotly_chart(fig)

        st.subheader('Insights')
        st.write("""
        - Countries with the highest average prices for Airbnb listings are typically popular tourist destinations or have higher living costs.
        - The differences in average prices can indicate varying demand and supply dynamics in different regions.
        - By analyzing these prices, hosts  can set competitive rates and travelers can plan their budgets accordingly.
        - Turkey has also become a popular destination for culture, spa, and health care. Since 2021, Turkey is the fourth most visited country in the world.
    """)

    elif price_analysis_selection == 'Price Vs Property':

        heatmap_data = price_country_df.pivot(index='country', columns='property_type', values='avg_price')

        # Create the heatmap for Property type, country and Price
        fig = px.imshow(
            heatmap_data,
            labels=dict(x="Property Type", y="Country", color="Average Price"),
            title='Average Airbnb Price by Country and Property Type',
            color_continuous_scale="Viridis"
        )

        # Customize layout
        fig.update_layout(
            xaxis_title='Property Type',
            yaxis_title='Country'
        )

        # Display the heatmap
        st.plotly_chart(fig)
        st.subheader('Insights')
        st.write("""
        - The average price of Airbnb listings varies significantly across different property types within each country.
        - Countries with higher living costs or popular tourist destinations may have higher average prices across all property types.
        - Certain property types, such as entire homes or luxury accommodations, tend to command higher prices regardless of the country.
        """)

