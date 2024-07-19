import  streamlit as st
import pandas as pd
import numpy as np
import pickle
st.title('Car Price Predictor')
st.write('This app predicts the price of a car based on the car features' )
st.write('The data used for this app is from the car dekho dataset')
model=pickle.load(open('Random_forest.pkl','rb'))
Make=['Renault', 'Maruti Suzuki', 'Land Rover', 'Mercedes Benz',
       'Jaguar', 'Datsun', 'Honda', 'Hyundai', 'Mahindra', 'Ford',
       'Ssangyong', 'BMW', 'Audi', 'Toyota', 'Volkswagen', 'Skoda',
       'Chevrolet', 'Lexus', 'Jeep', 'Porsche', 'MG', 'MINI', 'Tata',
       'Nissan', 'Mitsubishi', 'Kia', 'Volvo', 'Rolls Royce', 'Ferrari',
       'Maserati', 'Isuzu', 'Lamborghini', 'Fiat']
Fuel_Type=['Petrol', 'Diesel', 'Other']
Transmission=['Manual', 'Automatic']
Owner_Type=['First', 'Second', 'Third', 'Other']
col1, col2 = st.columns(2)
make = col1.selectbox('select the Make',sorted(Make))
fuel_type = col2.selectbox('select the Fuel Type',sorted(Fuel_Type))
col3,col4=st.columns(2)
transmission = col3.selectbox('select the Transmission',sorted(Transmission))
owner_type = col4.selectbox('select the Owner Type',sorted(Owner_Type))
year = st.number_input('Enter the year',min_value=1996, max_value=2021, value=1996)
col5,col6,col7=st.columns(3)
with col5:
       km_driven=st.number_input('Enter the km driven',min_value=0, max_value=1000000, value=0)
with col6:
         Engine=st.number_input('Enter the Engine',min_value=0, max_value=5000, value=0)
with col7:
    fuel_capacity=st.number_input('Enter the fuel capacity',min_value=0, max_value=100, value=0)
if st.button('Predict'):
       input_df=pd.DataFrame({
              'Make':[make],
           'Year': [year],
           'Kilometer': [km_driven],
              'Fuel Type':[fuel_type],
              'Transmission':[transmission],
              'Owner':[owner_type],
              'Engine':[Engine],
              'Fuel Tank Capacity':[fuel_capacity]
       })
       result=model.predict(input_df)
       st.header('The price of the car is: '+str(round(result[0],2)))

