# Scheduler

Foi utilizado APScheduler para automatizar a atualização dos estoques.

Fluxo:

09:00

↓

Hemominas

10:00

↓

HEMOSC

11:00

↓

HEMEPAR

Cada atualização realiza:

- coleta dos dados
- padronização
- atualização do banco
- disponibilização imediata na API

Sem necessidade de intervenção manual.