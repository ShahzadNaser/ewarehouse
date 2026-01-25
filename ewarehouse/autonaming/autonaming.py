import frappe
from frappe.model.naming import make_autoname

def po(doc, method):
    cdate = frappe.utils.formatdate(frappe.utils.getdate(),"YYMMDD")
    doc.name = make_autoname('PO-.{}-.####'.format(cdate))

def pr(doc, method):
    cdate = frappe.utils.formatdate(frappe.utils.getdate(),"YYMMDD")
    doc.name = make_autoname('PR-.{}-.####'.format(cdate))

def pi(doc, method):
    cdate = frappe.utils.formatdate(frappe.utils.getdate(),"YYMMDD")
    doc.name = make_autoname('PI-.{}-.####'.format(cdate))
