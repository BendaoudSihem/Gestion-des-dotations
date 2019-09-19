# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    
    'name': 'Gestion des dotations',
    'version': '1.0',
    'category': 'Dotation',
    'application': True,
    'author': 'Sihem Bendaoud',
    'depends': ['sale_management','hr','product'],
    'data': ['views/articleForm.xml',
            'views/Filtre_Dotation.xml',
            'views/employe.xml',
            'views/Decharge.xml',
            'views/Ligne_Decharge.xml',
            'report/report.xml',
            'security/access.xml',
            'security/ir.model.access.csv'

    ],
    'sequence': '0',
    'description': 'Ce module est destine pour gérer les dotations',
   # 'application':true
   
  
    
}
