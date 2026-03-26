from flask import Flask, request, jsonify
import time

app = Flask(__name__)

orders = {
    "1234": time.time() - 50,
    "5678": time.time() - 150,
    "9999": time.time() - 300
}

def get_status(order_time):
    elapsed = time.time() - order_time

    if elapsed < 60:
        return "Order Placed"
    elif elapsed < 120:
        return "Shipped"
    elif elapsed < 180:
        return "Out for Delivery"
    else:
        return "Delivered"

@app.route('/track', methods=['GET'])
def track():
    tracking_id = request.args.get('id')

    if tracking_id not in orders:
        return jsonify({"error": "Invalid ID"})

    status = get_status(orders[tracking_id])
    return jsonify({"status": status})

if __name__ == '__main__':
    app.run(debug=True)