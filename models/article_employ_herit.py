from odoo import fields,models,api,_
from datetime import datetime
from odoo.exceptions import ValidationError

class Article(models.Model):
	
	_inherit="product.template"
	
	Dotation=fields.Boolean()


class Empl(models.Model):

	_inherit="hr.employee"
	
	decharge_id=fields.Many2many('dotation.decharge',string ="Decharge")
	ligne_id=fields.Many2many('dotation.ligne',string ="Ligne")
	quantity=fields.Integer()
	
		


	






	
	

	