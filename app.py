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
    data.append(X2)
    data.append(X3)
    data.append(X4)
    data.append(X5)
    data.append(X6)
    data.append(X7)
    data.append(X8)
    data.append(X9)
    data.append(X10)
    data.append(X11)
    data.append(X12)
    data.append(X13)
    data.append(X14)
    data.append(X15)
    data.append(X16)
    data.append(X17)
    data.append(X18)
    data.append(X19)
    data.append(X20)
    prediction = model.predict([data])
    output = round(prediction[0], 5)

    return render_template('index.html', result = output, X1=X1, X2=X2, X3=X3, X4=X4, X5=X5, X6=X6, X7=X7, X8=X8, X9=X9, X10=X10, X11=X11, X12=X12, X13=X13, X14=X14, X15=X15, X16=X16, X17=X17, X18=X18, X19=X19, X20=X20)

if __name__ == '__main__':
    app.run(debug=True)
