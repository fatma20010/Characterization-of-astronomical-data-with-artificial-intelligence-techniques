import joblib
from flask import Flask,render_template,request
app = Flask(__name__)
try:
  with open('decisionTree.joblib', 'rb') as f:
    model = joblib.load(f)
  print("Model loaded successfully!")
except FileNotFoundError:
  print("Model file not found!")
@app.route('/')
def GO():
    return render_template('GO.html')
@app.route('/predict',methods=['GET','POST'])
def predict():
    # Get individual values from the form
    ra = request.form.get('ra')
    dec = request.form.get('dec')
    u = request.form.get('u')
    g = request.form.get('g')
    r = request.form.get('r')
    i = request.form.get('i')
    z = request.form.get('z')

    # Combine values into a list 
    input_data = [[ra, dec, u, g, r, i, z]]

    # Make prediction
    prediction = model.predict(input_data)
    output=prediction
    return render_template('GO.html',prediction_text=f'Total revenue generated is Rs.{output}/-')


                           
if __name__ == '__main__':
  app.run(debug=True)
                       












