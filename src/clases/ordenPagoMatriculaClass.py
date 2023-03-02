from pydantic import BaseModel
import datetime


class getOrdenPagoMatriculaByIdPago(BaseModel):
    matricula_pagoMatricula: int = None
