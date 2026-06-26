"""
Serviço reservado para integração com dados da Pró-Sangue/SP.

Este arquivo será usado na fase interestadual do TCC.
"""


def coletar_estoque_prosangue():
    return {
        "fonte": "Pró-Sangue",
        "estado": "SP",
        "estoques": [
            {"tipo_sanguineo": "O-", "status": "Alerta"}
        ]
    }
