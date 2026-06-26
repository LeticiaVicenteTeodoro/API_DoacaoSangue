from fastapi import APIRouter

router = APIRouter(
    prefix="/compatibilidade",
    tags=["Compatibilidade"]
)

COMPATIBILIDADE = {
    "O-": {
        "recebe_de": ["O-"],
        "doa_para": ["O-", "O+", "A-", "A+", "B-", "B+", "AB-", "AB+"]
    },
    "O+": {
        "recebe_de": ["O-", "O+"],
        "doa_para": ["O+", "A+", "B+", "AB+"]
    },
    "A-": {
        "recebe_de": ["O-", "A-"],
        "doa_para": ["A-", "A+", "AB-", "AB+"]
    },
    "A+": {
        "recebe_de": ["O-", "O+", "A-", "A+"],
        "doa_para": ["A+", "AB+"]
    },
    "B-": {
        "recebe_de": ["O-", "B-"],
        "doa_para": ["B-", "B+", "AB-", "AB+"]
    },
    "B+": {
        "recebe_de": ["O-", "O+", "B-", "B+"],
        "doa_para": ["B+", "AB+"]
    },
    "AB-": {
        "recebe_de": ["O-", "A-", "B-", "AB-"],
        "doa_para": ["AB-", "AB+"]
    },
    "AB+": {
        "recebe_de": ["O-", "O+", "A-", "A+", "B-", "B+", "AB-", "AB+"],
        "doa_para": ["AB+"]
    },
}


@router.get("/{tipo}")
def consultar_compatibilidade(tipo: str):
    tipo = tipo.upper()

    if tipo not in COMPATIBILIDADE:
        return {
            "erro": "Tipo sanguíneo inválido",
            "tipos_validos": list(COMPATIBILIDADE.keys())
        }

    return {
        "tipo": tipo,
        **COMPATIBILIDADE[tipo]
    }
