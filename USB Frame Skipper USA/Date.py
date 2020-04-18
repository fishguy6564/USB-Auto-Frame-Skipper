class Date:
	def __init__(self, monthNum, dayNum, yrNum):
		if monthNum > 12 or dayNum > self.getMaxDays(monthNum, yrNum) or dayNum < 1:
			raise Exception("Bad Date!")

		self.month = monthNum
		self.day = dayNum
		self.year = yrNum

	def checkLeapYear(self, year):
		if (year % 4) == 0:
			if (year % 100) == 0:
				if (year % 400) == 0:
					return True
				else:
					return False
			else:
				return True
		return False

	def getMaxDays(self, month, year):
		if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
			return 31
		if month == 4 or month == 6 or month == 9 or month == 11:
			return 30
		else:
			if self.checkLeapYear(year):
				return 29
			return 28

	def increaseMonth(self):
		self.month += 1
		if self.month > 12:
			self.month = 1
			return False
		return True

	def increaseYear(self):
		self.year += 1

	def increaseDay(self):
		maxDay = self.getMaxDays(self.month, self.year)
		self.day += 1
		if self.day > maxDay:
			self.day = 1
			return False
		return True
