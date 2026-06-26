"""
Serviço reservado para integração com dados da Hemominas.

Futuro uso:
- coletar dados públicos;
- padronizar campos;
- salvar no banco da API.
"""


def coletar_estoque_hemominas():
    return {
        "fonte": "Hemominas",
        "estado": "MG",
        "estoques": [
            {"tipo_sanguineo": "O-", "status": "Crítico"},
            {"tipo_sanguineo": "A-", "status": "Alerta"}
        ]
    }
