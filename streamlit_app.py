# Import libraries
from libs.convert_to_text import convert_to_text
import time
import joblib
import streamlit as st

# Load model
start = time.time()
model = joblib.load('models/rnd_clf.pkl')
end = time.time()
load_time = end-start
st.text('Ladezeit für Modell: ' + str(load_time) + 's')

# Load images
col1, col2 = st.columns(2, gap='large', vertical_alignment='center')

with col1:
    st.image('media/ukd_logo.jpg', width=250)

with col2:
    st.image('media/uoz_logo.png', width=150)

# The title
st.title('Textgenerator für das prätherapeutische Tumorboard')

# The header
st.header('Bitte Patientenparameter eingeben:')

# Input for patient age
age = st.number_input('Alter (Jahre):', value=65.0, step=10.0)

# Input for patient psa serum level
psa = st.number_input('PSA (ng/ml):', value=4.0, step=1.0)

# Input for dre stage
dre_options = {'cT1': 0, 'cT2a': 1, 'cT2b': 2, 'cT2c': 3, 'cT3': 4}
input_dre = st.selectbox('DRU:', dre_options.keys())
dre = dre_options[input_dre]

# Input for site
site_options = {'links': 0, 'rechts': 1, 'beidseits': 2}
input_site = st.selectbox('Seite:', site_options.keys())
site = site_options[input_site]

# Input for ISUP category
isup = st.selectbox('ISUP Kategorie:', ['1', '2', '3', '4', '5'])

# Input for number of positive biopsy cores
cylinder_pos = st.number_input('Zahl der positiven Stanzzylinder:', value=2.0,step=1.0)

# Input for overall biopsy cores
cylinder_total = st.number_input('Zahl der gesamten Stanzzylinder:', value=12.0,step=1.0)

# Input for preexisting disease
st.subheader('Vorerkrankungen:')
ht = st.checkbox('Arterielle Hypertonie')
dm = st.checkbox('Diabetes mellitus')
cad = st.checkbox('Koronare Herzerkrankung')
bmi = st.checkbox('Adipositas')
preop = st.checkbox('Voroperationen')

# Run model prediction
button_predict = st.button('Prädiktion')

if button_predict:
    start = time.time()
    prediction = model.predict([[age, psa, dre, site, isup, cylinder_pos, cylinder_total, ht, dm, cad, bmi, preop]])
    end = time.time()
    prediction_time = end - start
    prediction_text = convert_to_text(prediction[0])
    st.markdown(prediction_text)
    st.text('Outcome Variable: ' + str(prediction))
    st.text('Berechnungszeit: ' + str(prediction_time) + 's')


