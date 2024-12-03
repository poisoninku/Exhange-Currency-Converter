from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['GET'])
def convert_currency():
    base_currency = request.args.get('base')
    target_currency = request.args.get('target')
    amount = float(request.args.get('amount', 0))
    api_key = "1f774b6b79c9bf29e19a5664" 
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if target_currency in data['conversion_rates']:
            rate = data['conversion_rates'][target_currency]
            converted_amount = round(amount * rate, 2)
            return jsonify({
                "base": base_currency,
                "target": target_currency,
                "rate": rate,
                "converted_amount": converted_amount
            })
        else:
            return jsonify({"error": "Invalid target currency"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
