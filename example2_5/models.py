class Model25:
	def __init__(self, name=None, title=None, date=None, content=None, time=None, datetime=None):
		self.name = name
		self.title = title
		self.date = date
		self.content = content
		self.time = time
		self.datetime = datetime

	def setName(self, name):
		self.name = name

	def getName(self):
		return self.name

	def setTitle(self, title):
		self.title = title

	def getTitle(self):
		return self.title

	def setDate(self, date):
		self.date = date

	def getDate(self):
		return self.date

	def setContent(self, content):
		self.content = content

	def getContent(self):
		return self.content

	def setTime(self, time):
		self.time = time

	def getTime(self):
		return self.time

	def setDatetime(self, datetime):
		self.datetime = datetime

	def getDatetime(self):
		return self.datetime
