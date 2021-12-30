# Copyright (c) 2021, Foo Fighters and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class BusLocation(Document):
	def before_save(self):
		self.bus_id = frappe.get_value("Bus",{"bus_name":self.bus_name})


