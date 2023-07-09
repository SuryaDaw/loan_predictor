from util import LoanPredictor
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def homepage():
    # return jsonify({'Result' :'Sucessful'})
    return render_template('source.html')

@app.route('/loan_status',methods=['POST'])
def predict_loan_status():
    data = request.forms

    print('Data :',data)

    Gender          = data['Gender']
    
    Married         = data['Married']
    Dependents      = data['Dependents']
    Education       = data['Education'] 
    Self_Employed    = data['Self_Employed']
    ApplicantIncome   = data['ApplicantIncome']
    CoapplicantIncome  = data['CoapplicantIncome']
    LoanAmount          = data['LoanAmount']
    Loan_Amount_Term    = data['Loan_Amount_Term']
    Credit_History      = data['Credit_History']
    Property_Area       = data['Property_Area']

    obj1 = LoanPredictor()

    loan_status = obj1.loan_predictor(Gender, Married,Dependents, Education, Self_Employed, ApplicantIncome,CoapplicantIncome,
                       LoanAmount,Loan_Amount_Term, Credit_History, Property_Area)
    
    # return jsonify({'Result' :f'Your Proposal for {loan_status}'})
    return render_template("source.html",predicted_class=loan_status)

if __name__=='__main__':
    app.run()