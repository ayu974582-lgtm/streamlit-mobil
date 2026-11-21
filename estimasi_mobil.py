import pickle
import streamlit as st

model = pickle.load(open('estimasi_mobil.sav', 'rb'))

st.title('Estimasi Harga Mobil Bekas')

year = st.number_input('Input Tahun Mobil', value=2019.0)
mileage = st.number_input('Input Km Mobil', value=5000.0)
tax = st.number_input('Input Pajak Mobil', value=145.0)
mpg = st.number_input('Input Konsumsi BBM Mobil', value=30.20)
engineSize = st.number_input('Input Engine Size', value=2.0)

st.write('Estimasi harga mobil bekas dalam Ponds :')
if st.button('Estimasi Harga'):
    predict = model.predict([[year, mileage, tax, mpg, engineSize]])
    st.write(predict)
    st.write('Estimasi harga mobil bekas dalam IDR (Juta) :')
    st.write(predict * 19000)
else:
    st.write(0)
    st.write('Estimasi harga mobil bekas dalam IDR (Juta) :')
    st.write(0)
