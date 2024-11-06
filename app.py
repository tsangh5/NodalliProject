from flask import Flask, request, jsonify
import requests
import pandas as pd

app = Flask(__name__)

# This is our webhook endpoint
@app.route('/webhook', methods=['POST'])
def webhook():
    # This gets the data from the request
    # data = request.json

    # Use CSV to model this first
    data = pd.read_csv('data.csv')

    print("Received data:", data) 

    # Here we can get the data for the specific fields
    resume = data.get("resume")
    purpose = data.get("purpose")
    fields = data.get("fields")
    company_details = data.get("company_size")
    lt_networking = data.get("lt_networking")
    st_networking = data.get("st_networking")
    academic_background = data.get("academic_background")
    relevant_experience = data.get("relevant_experience")
    submission_IP = data.get("submission_IP")
    submission_ID = data.get("submission_ID")

    # How can we start our Apify actor with this data?

    # For now, we'll just print the parsed data
    print(f"Keywords: {keywords}, Location: {location}, Company Size: {company_size}")

    # Return a success message
    return jsonify({"status": "success"}), 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)
