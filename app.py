from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_file = open('model.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', insurance_cost=0)

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
    features = [float(x) for x in request.form.values()]
   
    data = []
    data.append(int(features))
    prediction = model.predict(data)

    return render_template('index.html', result = prediction)


if __name__ == '__main__':
    app.run(debug=True)
