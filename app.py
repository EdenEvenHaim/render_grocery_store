from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/category', methods=['POST'])
def get_category():
    data = request.get_json()
    selected_value = data.get('value')
    if selected_value:
        logging.info(f"Selected category value: {selected_value}")
        return jsonify({"message": "Value received", "value": selected_value}), 200
    else:
        return jsonify({"message": "No value received"}), 400

if __name__ == "__main__":
    app.run(debug=True)
