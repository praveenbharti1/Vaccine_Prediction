import pickle
import numpy as np
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Load the scaling model and the machine learning model
loaded_model = pickle.load(open('adaboost_h1n1.pkl', 'rb'))

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():

  columns = ['h1n1_concern', 'h1n1_knowledge', 'behavioral_antiviral_meds',
       'behavioral_avoidance', 'behavioral_face_mask', 'behavioral_wash_hands',
       'behavioral_large_gatherings', 'behavioral_outside_home',
       'behavioral_touch_face', 'doctor_recc_h1n1', 'doctor_recc_seasonal',
       'chronic_med_condition', 'child_under_6_months', 'health_worker',
       'health_insurance', 'opinion_h1n1_vacc_effective', 'opinion_h1n1_risk',
       'opinion_h1n1_sick_from_vacc', 'opinion_seas_vacc_effective',
       'opinion_seas_risk', 'opinion_seas_sick_from_vacc', 'age_group',
       'education', 'race', 'sex', 'income_poverty', 'marital_status',
       'rent_or_own', 'employment_status', 'census_msa',
       'household_adults', 'household_children']
  
  
  inputs = {}
  for i in columns:
    value = int(request.form[i])
    inputs[i] = value



  input_values = list(inputs.values())
  #  Make predictions using the loaded machine learning model
  predictions = loaded_model.predict(np.array(input_values).reshape(1, -1))
  result = predictions[0]

  # Map the result to price range labels
  if result == 0:
    output = "Respondent's Have Not Taken  Vaccine" 
  else:
    output = "Respondent's Have  Taken  Vaccine"

  # Return the price range as the prediction result
  return render_template('index.html', result=output)
  
   
if __name__ == '__main__':
    app.run(debug=True)