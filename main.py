import streamlit as st
import pandas as pd
import plotly.express as px
import mysql.connector

st.title("AIRBNB ANALYSIS")

#SQL connection

mydb = mysql.connector.connect(
 host="localhost",
 user="Your username",
 password="Enter your password",
 database = "Enter your database name"


)
print(mydb)
mycursor = mydb.cursor(buffered=True)

mycursor.execute("SELECT * FROM HOTEL")
table_rows1 = mycursor.fetchall()
df1 = pd.DataFrame(table_rows1,columns=mycursor.column_names)

mycursor.execute("SELECT * FROM HOST")
table_rows2 = mycursor.fetchall()
df2 = pd.DataFrame(table_rows2,columns=mycursor.column_names)

mycursor.execute("SELECT YEAR(date)AS Year,COUNT(_id) AS Number_of_reviews FROM REVIEW  GROUP BY Year")
table_rows3 = mycursor.fetchall()
df3 = pd.DataFrame(table_rows3,columns=mycursor.column_names)


tab1,tab2,tab3,tab4 = st.tabs(["Global_Distribution_of_Airbnb_Listings ","Price vs. Hotel ID by Room Type","Host_details","Reviews"])

with tab1:
   st.header("Global Distribution of Airbnb Listings ")
   fig1 = px.scatter_geo(df1, lat=df1['latitude'], lon=df1['longitude'],
                     hover_name=df1['name']
                     )
   st.plotly_chart(fig1)

with tab2:   
   fig2 = px.scatter(
    df1, x=df1["Id"], y=df1["price"], color=df1["room_type"],
    hover_name="name", title="Price vs. Hotel ID by Room Type"
)
   st.plotly_chart(fig2)

with tab3:   
   fig3 = px.scatter(
    df2, x=df2["host_id"], y=df2["host_total_listings_count"], color=df2["is_rated"],
    hover_name="host_name", title="Host_total_listings_count vs. Hotel Id"
)
   st.plotly_chart(fig3)   

with tab4:   
   fig4 = px.line(df3,x = 'Year',y= 'Number_of_reviews',title = 'Number of reviews over the years',color_discrete_sequence = px.colors.sequential.Magma,markers=True)
   st.plotly_chart(fig4)    


     