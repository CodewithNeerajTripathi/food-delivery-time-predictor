from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

# FIX 3: correct path
model = pickle.load(open('model/model.pkl', 'rb'))

@app.route('/')
def home():
    return "API is running"

@app.route('/predict', methods=['POST'])
def predict():
    try:                                          # FIX: error handling
        data = request.json

        distance   = data['distance']

        if distance > 20:
         return jsonify({'error': 'Distance must be between 0-20 km'}), 400

        if distance <= 0:
          return jsonify({'error': 'Distance must be greater than 0'}), 400  
        traffic    = data['traffic']
        weather    = data['weather']
        experience = data['experience']
        vehicle    = data['vehicle']
        time_of_day = data['time']
        prep_time  = data['prep_time']

        # FIX 1: mappings now match LabelEncoder alphabetical order
        weather_map = {'Clear':0, 'Foggy':1, 'Windy':2, 'Rainy':3, 'Snowy':4} 
        vehicle_map = {'Bike':0, 'Car':1, 'Scooter':2}
        time_map    = {'Morning':0, 'Afternoon':1, 'Evening':2, 'Night':3}  
        traffic_map = {'Low':1, 'Medium':2, 'High':3}

        encoded_weather = weather_map[weather]
        encoded_vehicle = vehicle_map[vehicle]
        encoded_time    = time_map[time_of_day]
        traffic_num     = traffic_map[traffic]

        traffic_distance = distance * traffic_num
        bad_weather      = 1 if weather in ['Rainy','Windy','Snowy'] else 0
        exp_distance     = distance / (experience + 1)

        # FIX 2: correct feature order matching notebook columns
        distance_per_prep = distance / (prep_time + 1)  # 👈 add this line

        features = [[
        distance,
        encoded_weather,
        encoded_time,      # Time before Vehicle
        encoded_vehicle,
        prep_time,
        experience,
        traffic_num,
        traffic_distance,
        bad_weather,
        exp_distance,
        distance_per_prep  # 👈 new feature
       ]]

        prediction = model.predict(features)[0]
        return jsonify({'delivery_time': round(prediction, 2)})

    except Exception as e:
        return jsonify({'error': str(e)}), 400   # FIX: clean error response

if __name__ == '__main__':
    app.run(debug=True)