import pickle
import streamlit as st

model = pickle.load(open('estimasi_mobil.sav', 'rb'))

st.title('Estimasi Harga Mobil Bekas')

year = st.number_input('Input Tahun Mobil', value=2019.0)
mileage = st.number_input('Input Km Mobil', value=5000.0)
tax = st.number_input('Input Pajak Mobil', value=145.0)
mpg = st.number_input('Input Konsumsi BBM Mobil', value=30.20)
engineSize = st.number_input('Input Engine Size', value=2.0)

def format_koma(angka):
    return f"{angka:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

estimasi_gbp = 0.0
estimasi_idr_juta = 0.0

if st.button('Estimasi Harga'):
    prediksi = model.predict([[year, mileage, tax, mpg, engineSize]])
    estimasi_gbp = float(prediksi[0])
    # Jika prediksi dalam poundsterling (misal 21000) dan kurs 19.000 -> jadi juta rupiah:
    estimasi_idr_juta = (estimasi_gbp * 19000) / 1_000_000

st.write('Estimasi harga mobil bekas dalam ponds :')
st.write(format_koma(estimasi_gbp))

st.write('Estimasi harga mobil bekas dalam IDR (juta) :')
st.write(format_koma(estimasi_idr_juta))
