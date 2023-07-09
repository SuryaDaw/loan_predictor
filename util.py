import config
import pickle
import numpy as np
import json

class LoanPredictor():
    def __init__(self) -> None:
        pass

    def get_data(self):
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)

    def loan_predictor(self,Gender, Married,Dependents, Education, Self_Employed, ApplicantIncome,CoapplicantIncome,
                       LoanAmount,Loan_Amount_Term, Credit_History, Property_Area):
        self.get_data()

        Gender = self.json_data['gender'][Gender]
        Married = self.json_data['married'][Married]
        Dependents = self.json_data['dependant'][Dependents]
        Education = self.json_data['education'][Education]
        Self_Employed = self.json_data['sel_employed'][Self_Employed]
        Property_Area = self.json_data['property_area'][Property_Area]

        test_array = np.zeros([1,self.model.n_features_in_])
        test_array[0][0] = Gender
        test_array[0][1] = Married
        test_array[0][2] = Dependents
        test_array[0][3] = Education
        test_array[0][4] = Self_Employed
        test_array[0][5] = ApplicantIncome
        test_array[0][6] = CoapplicantIncome
        test_array[0][7] = LoanAmount
        test_array[0][8] = Loan_Amount_Term
        test_array[0][9] = Credit_History
        test_array[0][10] = Property_Area

        predicted_class = self.model.predict(test_array)[0]

        if predicted_class=='Y':
            return "Loan will Approved"
        else:
            return "Loan will not Approved"
        
