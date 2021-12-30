# Copyright (c) 2021, Foo Fighters and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class BusStops(Document):
	def save(self):
		self.stop_name = self.stop
		super().save()
