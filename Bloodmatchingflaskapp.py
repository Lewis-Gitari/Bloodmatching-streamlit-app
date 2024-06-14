app = Flask(__name__)

@app.route('/match', methods=['POST'])
def match():
    recipient_data = request.json
    recipient = {
        'blood_group': recipient_data['blood_group'],
        'rh_factor': recipient_data['rh_factor']
    }
    
    matches = find_compatible_donors(recipient)
    
    response = {
        'recipient': recipient_data,
        'compatible_donors': matches
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)