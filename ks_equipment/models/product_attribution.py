# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductAttribution(models.Model):
     _name = 'product.attribution'
     _inherit = 'mail.thread'
     _description = 'Product Attribution'

     reference = fields.Char(string='Reference')
     employe_id = fields.Many2one('hr.employee','employe', track_visibility='always')
     material_id = fields.Many2one('product.template','materiel', track_visibility='always')
     date_of_issue = fields.Date('Date de delivrance')
     Serial_number = fields.Char('Numero de serie', track_visibility='always')
     Value_of_material = fields.Float('Value_of_material')
     category_of_equipment_id = fields.Many2one('product.category','materiel_category')
     note = fields.Html('Note')
     Assigned_by_id = fields.Many2one('res.users','attribue par')
     state = fields.Selection(
        [('new', 'Nouveau'),
         ('attributed','Attribue'),
         ('returned','Retourne'),
         ('lost','Perdu'),
         ('broken','Casse'),
         ('refunded','Rembourse'),
         ('cancelled','Annule')],
        default='new',
     )

     def attributed(self):
        if self.state == "new":
            return self.write({'state': 'attributed'})

     def returned(self):
        if self.state == "attributed":
           return self.write({'state':'returned'})

     def cancelled(self):
        if self.state == "attributed":
            return self.write({'state':'cancelled'})























#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
