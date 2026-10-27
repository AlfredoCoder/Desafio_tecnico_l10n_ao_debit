# Desafio Técnico: Módulo de Notas de Débito para Angola (Odoo 18)

Módulo `l10n_ao_debit` para **Odoo 18.0** focado no tratamento de **Notas de Débito**.

## 📌 Visão Geral
Este módulo implementa o tratamento legal e contabilístico das Notas de Débito para a Localização de Angola.

## ⚖️ Enquadramento Fiscal e Regras de Negócio (AGT / SAF-T AO)
- **Segregação de Documentos:** Separação clara entre Faturas, Notas de Crédito e Notas de Débito.
- **Impacto Contabilístico Correto:** Acréscimo de dívida ao cliente/fornecedor com a natureza contabilística apropriada.
- **Numeração Independente:** Prefixo sequencial próprio (`ND`).
- **Referência à Fatura Origem:** Obrigatoriedade fiscal de vincular uma Fatura de Origem confirmada (`posted`).
