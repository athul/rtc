// Copyright (c) 2021, Foo Fighters and contributors
// For license information, please see license.txt

frappe.ui.form.on('Bus Ticket', {
	// refresh: function(frm) {

	// }
	bus_id: (frm)=>{
		// console.log(frm.doc.bus_id)
		// console.log(frappe.db.get_value("Bus","stops",(r)=>{
		// 	console.log(r)
		// }))
		frappe.db.get_doc("Bus",frm.doc.bus_id)
		console.log(frappe.get_doc("Bus",frm.doc.bus_id))
		// frappe.db.get_value(
		// 	"Bus",
		// 	frm.doc.bus_id,
		// 	"stops",
		// 	(r)=>{
		// 		console.log(r.stop)
		// 	}
		// )
	}
});

// frappe.ui.form.on('Bus Stops',{
// 	from(frm,cdt,cdn){
// 		let row = frappe.db.get_(cdt,cdn)
// 		console.log(row)
// 	},
// })