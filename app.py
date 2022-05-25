from flask import Flask, render_template, request
import pickle
# from artifacts import student_model


app = Flask(__name__)       # class object(camel letter)



model = pickle.load(open("artifacts\student_model.pkl",'rb'))


@app.route('/', methods=["POST","GET"])
def home():
    return render_template('index.html')      # front end api
    # return 'SUCCESS'

@app.route('/predict', methods = ["POST","GET"])
def student():                       # Capture the  from user Data
    cgpa = float(request.form.get('cgpa'))
    iq =  int(request.form.get('iq'))
    ps = int(request.form.get('ps'))

    print(f'{cgpa},{iq},{ps}')

    result = model.predict([[cgpa,iq,ps]])

    print(result[0])

    if result==1:
        final_result = 'Student will be Placed'
    else:
        final_result = 'No Placement'

    return render_template('index.html', prediction = final_result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)  





