
class CheapBasePaymentGateway:
	def __init__(self):
		self.gateway = "CheapBasePaymentGateway"
	
	def pay(self,details):
		return True

class ExpensiveBasePaymentGateway:
	def __init__(self):
		self.gateway = "ExpensiveBasePaymentGateway"
	
	def pay(self,details):
		return True

class PremiumBasePaymentGateway:
	def __init__(self):
		self.gateway = "PremiumBasePaymentGatway"
	
	def pay(self,details):
		for i in range(3):
			try:
				# Try to pay 3 times
				return True
			except:
				pass

def processor(data):
	amount = int(data['amount'])
	if amount <= 20:
		p = CheapBasePaymentGateway
	elif 20 < amount <= 500:
		p = ExpensiveBasePaymentGateway
	else:
		p = PremiumBasePaymentGateway

	return p().pay(data)
