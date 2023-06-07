import streamlit as st
st.title('Flight Fare Prediction')

import pickle
import pandas as pd
model = pickle.load(open('Documents/Data_Science/Flight_fare_prediction/pipeline_model.sav', 'rb'))
Source = st.selectbox("Source",['Banglore','Kolkata','Delhi','Chennai','Mumbai'])
Destination = st.selectbox("Destination",['New Delhi','Banglore','Cochin','Kolkata','Delhi','Hyderabad'])
Airline = st.selectbox("Airline",['Jet Airways','Indigo','Air India','Multiple carriers','SpiceJet','Vistara','Air Asia','GoAir','Multiple carriers Premium economy','Jet Airways Business','Vistara Premium economy','Trujet'])
Route = st.number_input("Route")
Additional_Info=st.selectbox("Additional_Info",['No info','In-flight meal not included','No check-in baggage included','1 Short layover','1 Long layover','Change airports','Business class','Red-eye flight','2 Long layover'])
Total_Stops= st.selectbox("Total_Stops",['non-stop','1 stop','2 stops','3 stops','4 stops'])
Journey_day=st.slider("Date",0,31)        
Journey_month=st.slider("Month",0,12)     
Journey_year=st.slider("Year",2023,2024)       
Dep_hour=st.slider("Dep Hours",00,23)         
Dep_min=st.slider(" Dep Minutes",0,60)           
Arrival_hour=st.slider("Arrival Hours",00,23)    
Arrival_min=st.slider(" Arrival Minutes",0,60)      
Duration_hours=st.slider("Duration Hours",00,23) 
Duration_mins=st.slider("Duration Minutes",0,60)  


import pandas as pd
new_data = pd.DataFrame({
    'Source':[Source],
    'Destination':[Destination],
    'Airline':[Airline],
    'Route':[Route],                      
    'Additional_Info':[Additional_Info],
    'Total_Stops':[Total_Stops],
    'Journey_day':[Journey_day],        
    'Journey_month':[Journey_month],    
    'Journey_year':[Journey_year],      
    'Dep_hour':[Dep_hour],         
    'Dep_min':[Dep_min],          
    'Arrival_hour':[Arrival_hour],     
    'Arrival_min':[Arrival_min],      
    'Duration_hours':[Duration_hours], 
    'Duration_mins':[Duration_mins]   
    
})
prediction = model.predict(new_data)
st.write("The price of the flight is:", prediction)