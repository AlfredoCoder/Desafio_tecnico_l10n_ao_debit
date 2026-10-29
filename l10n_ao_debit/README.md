Desafio Técnico: Módulo de Notas de Débito para Localização de Angola (Odoo 18)

Módulo `l10n_ao_debit` para Odoo 18.0 com implementação do tratamento Nativo de Notas de Débito.


Implementar o tratamento nativo de Notas de Débito em Angola, assegurando:
- Segregação de Documentos: Menus e ações dedicadas para Notas de Débito de Clientes e Fornecedores.
- Impacto Contabilístico Correto:Documento retificativo a débito (aumento da dívida).
- Numeração Independente: Prefixo sequencial próprio `ND`(**AO TESTAR NÃO ESQUEÇA DE SELECIONAR OS DIÁRIOS CORRECTOS  PARA SEGUIR A NUMERAÇÃO CORRECTA DE ND**).
- Referência à Fatura Origem: Obrigatoriedade de associar uma fatura confirmada (`posted`) do mesmo parceiro.




1. Obrigatoriedade de Fatura de Origem: Nenhuma Nota de Débito pode ser confirmada (`state == 'posted'`) sem ter uma `debit_origin_id` associada.
2. Coerência de Parceiro: A fatura de origem deve pertencer obrigatoriamente ao mesmo cliente/fornecedor da Nota de Débito.
3. Alerta Visual: Banner destacado no formulário identificando o documento como retificativo.



1. Adicione esta pasta ao seu `addons_path` no ficheiro de configuração `odoo.conf`:
   ini
   addons_path = /caminho/para/odoo/addons,/caminho/para/Desafio_tecnico_l10n_ao_debit

2. Atualize a lista de aplicações no Odoo e instale o módulo `l10n_ao_debit`.




Alfredo de Jesus  

