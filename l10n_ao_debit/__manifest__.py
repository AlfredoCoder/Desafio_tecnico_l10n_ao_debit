# -*- coding: utf-8 -*-
{
    'name': 'l10n_ao_debit',
    'version': '18.0.1.0.0',
    'category': 'Accounting/Localizations',
    'summary': 'Tratamento nativo de Notas de Débito para Angola',
    'description': """
Módulo de Notas de Débito para Localização de Angola

- Segregação de Documentos
- Impacto Contabilistico Correcto
- Numeração independente
- Referência a Fatura Origem
    """,
    'author': 'Alfredo de Jesus',
    'license': 'LGPL-3',
    'depends': [
        'account',
    ],
    'data': [
        'data/account_journal_data.xml',
        'views/account_move_views.xml',
        'views/account_menu_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
