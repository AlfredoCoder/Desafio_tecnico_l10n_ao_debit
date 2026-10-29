from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class AccountMove(models.Model):
    _inherit = 'account.move'
    
    is_debit_note = fields.Boolean(
        string='É Nota de Débito',
        default=False,
        copy=False,
        tracking=True,
        help='Indica se este documento é uma Nota de Débito.'
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
        
        for move in self:
            if move.is_debit_note and move.state == 'posted':
                if not move.debit_origin_id:
                    raise ValidationError(_(
                        "Obrigatoriedade Fiscal (AGT):\n"
                        "Para confirmar uma Nota de Débito é obrigatório associar a Fatura de Origem retificada."
                    ))
                
                
                if move.debit_origin_id.partner_id != move.partner_id:
                    raise ValidationError(_(
                        "Incompatibilidade de Parceiro:\n"
                        "A Fatura de Origem selecionada pertence a outro cliente ou fornecedor."
                    ))
   
    def _get_starting_sequence(self):
       
        starting_sequence = super(AccountMove, self)._get_starting_sequence()
        if self.is_debit_note:
           
            starting_sequence = "ND " + starting_sequence
        return starting_sequence
