# Desafio Técnico: Módulo de Notas de Débito para Localização de Angola (Odoo 18)

Módulo `l10n_ao_debit` para **Odoo 18.0** com implementação do tratamento fiscal e contabilístico de **Notas de Débito**, em conformidade com as exigências da Administração Geral Tributária (AGT) de Angola e estrutura do ficheiro SAF-T AO.

---

## 🎯 Objetivo
Implementar o tratamento nativo de Notas de Débito em Angola, assegurando:
- **Segregação de Documentos:** Menus e ações dedicadas para Notas de Débito de Clientes e Fornecedores.
- **Impacto Contabilístico Correto:** Documento retificativo a débito (aumento da dívida).
- **Numeração Independente:** Prefixo sequencial próprio `ND`.
- **Referência à Fatura Origem:** Obrigatoriedade de associar uma fatura confirmada (`posted`) do mesmo parceiro.

---

## ⚖️ Validações Fiscais (AGT / SAF-T AO)
1. **Obrigatoriedade de Fatura de Origem:** Nenhuma Nota de Débito pode ser confirmada (`state == 'posted'`) sem ter uma `debit_origin_id` associada.
2. **Coerência de Parceiro:** A fatura de origem deve pertencer obrigatoriamente ao mesmo cliente/fornecedor da Nota de Débito.
3. **Alerta Visual:** Banner destacado no formulário identificando o documento como retificativo.

---

## 📁 Estrutura do Módulo

```text
├── __init__.py
├── __manifest__.py
├── data/
│   └── account_journal_data.xml      # Diários NDCLI e NDFOR
├── models/
│   ├── __init__.py
│   └── account_move.py               # Extensão de campos, validações e sequência
├── security/
│   └── ir.model.access.csv           # Controle de acessos
├── views/
│   ├── account_menu_views.xml        # Menus em Clientes e Fornecedores
│   └── account_move_views.xml        # Alerta visual, campo origem e visão em lista
├── .gitignore
└── README.md
```

---

## 🚀 Como Instalar no Odoo 18

1. Adicione esta pasta ao seu `addons_path` no ficheiro de configuração `odoo.conf`:
   ```ini
   addons_path = /caminho/para/odoo/addons,/caminho/para/Desafio_tecnico_l10n_ao_debit
   ```
2. Atualize a lista de aplicações no Odoo e instale o módulo `l10n_ao_debit`.

---

## 👤 Autor
**Alfredo de Jesus**  
GitHub: [@AlfredoCoder](https://github.com/AlfredoCoder)
