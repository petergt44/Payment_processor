from datetime import date

class CardChecker:
	def __init__(self,data):
		self.number = data.get("cardnumber")
		self.name = data.get("name")
		self.expiry = data.get("expiry")
		self.amount = data.get("amount")
		self.code = data.get("code") if data.get("code") else ""
		self.errors = []

	def check_card(self):
		all_good = self.is_number_valid() and self.is_name_valid() and self.is_expiry_valid() and self.is_amount_valid()
		return all_good,','.join(self.errors)

	def is_number_valid(self):
		if len(self.number) == 16:
			try:
				int(self.number)
				return True
			except:
				pass
		self.errors.append("Invalid card number")

	def is_name_valid(self):
		if len(self.name) > 1:
			return True
		self.errors.append("Invalid Card Holder Name")

	def is_expiry_valid(self):
		d = self.expiry.split("/")
		try:
			today = date.today()

			d = date(day = 1,month = int(d[0]),year = 2000+int(d[1]))
			print(d,today,d > today)
			if d > today:
				return True
		except:
			pass
		self.errors.append("invalid expiry date")

	def is_amount_valid(self):
		try:
			num = int(self.amount)
			if num > 0:
				return True
		except:
			pass
		self.errors.append("Invalid Amount")