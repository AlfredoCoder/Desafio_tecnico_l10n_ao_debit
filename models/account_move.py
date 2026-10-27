from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class AccountMove(models.Model):
    _inherit = 'account.move'
    
    is_debit_note = fields.Boolean(
        string='É Nota de Débito',
        default=False,
        copy=False,
        tracking=True,
        help='Indica se este documento é uma Nota de Débito (acréscimo de dívida).'
    )
   
    debit_origin_id = fields.Many2one(
        comodel_name='account.move',
        string='Fatura de Origem Retificada',
        copy=False,
        tracking=True,
        help='Fatura original validada que está a ser retificada com acréscimo de valor.'
    )
