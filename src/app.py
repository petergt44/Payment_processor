from flask import Flask,jsonify,request

from utils.card_checker import CardChecker
from utils.payment_processer import processor

app = Flask(__name__)


@app.route("/api/process-payment/",methods = ["POST"])
def ProcessPayment():
	data = request.json
	if data.get("cardnumber") and data.get("name") and data.get("expiry") and data.get("amount"):
		card = CardChecker(data)
		is_valid,msg = card.check_card()
		if is_valid:
			processed = processor(data)
			if processed:
				return jsonify({"status":"Success","msg":"Payment Processed Successfully"})
			return jsonify({"status":"Failed","msg":"Payment Failed"}),400
		else:
			return jsonify({"status":"Failed","msg":msg}),400
	else:
		return jsonify({
				"status":"Failed",
				"msg":"Please provide full card details {cardnumber,name,expiry,amount,code(optional)}"}),400

if __name__ == "__main__":
	app.run(debug = True)
