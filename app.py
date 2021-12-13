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
    X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, X11, X12, X13, X14, X15, X16, X17, X18, X19, X20 = [float(x) for x in request.form.values()]
   
    data = []
    data.append(X1)
    data.extend(X2)
    data.extend(X3)
    data.extend(X4)
    data.extend(X5)
    data.extend(X6)
    data.extend(X7)
    data.extend(X8)
    data.extend(X9)
    data.extend(X10)
    data.extend(X11)
    data.extend(X12)
    data.extend(X13)
    data.extend(X14)
    data.extend(X15)
    data.extend(X16)
    data.extend(X17)
    data.extend(X18)
    data.extend(X19)
    data.extend(X20)
    prediction = model.predict(data)

    return render_template('index.html', result = prediction)

if __name__ == '__main__':
    app.run(debug=True)
