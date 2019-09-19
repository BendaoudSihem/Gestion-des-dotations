from odoo import fields,models,api,_
from datetime import datetime
from odoo.exceptions import ValidationError

class Dotation(models.Model):

	_name ="dotation.decharge"
	_description = "dotation table"


	@api.one
	def open(self):
		
			self.valider="b"

	

	Employe=fields.Many2one('hr.employee',string ="Employe")
	date_Dotation=fields.Date()
	valider=fields.Selection([('a', 'Brouillon'), ('b', 'Validée')],'Decharge')
	decharge=fields.One2many('dotation.ligne','decharge_id')
	
	
	
class Ligne(models.Model):

	
	_name ="dotation.ligne"
	_description = "ligne de decharge table"



	decharge_id=fields.Many2one('dotation.decharge')	
	product_id=fields.Many2one('product.product',domain="[('Dotation','=',True)]")	
	quantite=fields.Integer()
	

	

	
	
		
	


	
	