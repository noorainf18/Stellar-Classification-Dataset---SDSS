from flask import Flask, request, jsonify,  render_template
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model and scaler
filename = 'classifier_model.sav'
classifier = pickle.load(open(filename, 'rb'))


@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None

    if request.method == 'POST':
        predictive_input = [
            float(request.form['Ultraviolet Filter']),
            float(request.form['Green Filter']),
            float(request.form['Red Filter']),
            float(request.form['Near Infrared Filter']),
            float(request.form['Infrared Filter']),
            float(request.form['Redshift']),
            float(request.form['Plate ID']),
            float(request.form['Modified Julian Date']),
        ]

        predictive_input_array = np.asarray(predictive_input).reshape(1, -1)
        prediction = classifier.predict(predictive_input_array)
        class_labels = ['Galaxy', 'Quasar', 'Star']
        predicted_class = class_labels[prediction[0]]
        prediction = predicted_class

    return render_template('index.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)
