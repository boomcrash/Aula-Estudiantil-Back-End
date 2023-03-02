from pydantic import BaseModel
import datetime

class getContratosDocenteId(BaseModel):
    docente_contrato: int = None