# Workout Tracker - Nutritionix & Sheety API
## Overview
This is a Python-based workout tracker that uses Natural Language Processing (NLP) to log exercises. It integrates with the Nutritionix API to process user input and retrieve exercise data, and then stores the data in a Google Sheet using the Sheety API.

### Features
✅ Accepts exercise input in natural language (e.g., "I ran 5km") <br />
✅ Retrieves details like calories burned and duration from Nutritionix <br />
✅ Logs the workout data (date, time, exercise, duration, calories) in a Google Sheet <br />
✅ Uses environment variables for API security

## Requirements
1. Python 3.x
2. Nutritionix API account
3. Sheety API account
4. .env file for storing API keys
## Installation & Setup
### 1. Clone the Repository
```
git clone https://github.com/yourusername/workout-tracker-nutritionix-sheety.git
cd workout-tracker-nutritionix-sheety
```
### 2. Install Dependencies
```
pip install -r requirements.txt
```
### 3. Create a .env File
Inside the project folder, create a .env file and add your API credentials:
```
nutritionix_id=your_nutritionix_id
nutritionix_api_key=your_nutritionix_api_key
sheety_token=your_sheety_token
sheety_auth_token=your_sheety_auth_token
```
### 4. Run the Program
```
python main.py
```


## The script will ask for your workout details and log them in your Google Sheet.
