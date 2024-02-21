from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)
df = pd.read_csv('your_data.csv')

@app.route('/get_loan_status', methods=['POST'])
def get_loan_status():
    user_input = request.json
    loan_id = user_input['loan_id']
    loan_status = df[df['Loan_ID'] == loan_id]['Loan_Status'].values[0]
    return jsonify({'loan_status': loan_status})

if __name__ == '__main__':
    app.run(debug=True)
