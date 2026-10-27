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
        domain="[('state', '=', 'posted'), ('move_type', '=', move_type), ('partner_id', '=', partner_id)]",
        help='Fatura original validada que está a ser retificada com acréscimo de valor.'
    )
   
    @api.constrains('is_debit_note', 'debit_origin_id', 'state')
    def _check_debit_origin_required(self):
        """
        Garante a regra fiscal da AGT (SAF-T AO): 
        Nenhuma Nota de Débito pode ser confirmada  sem ter uma Fatura de Origem associada.
        """
        for move in self:
            pass
