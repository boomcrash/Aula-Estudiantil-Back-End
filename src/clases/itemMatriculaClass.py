from pydantic import BaseModel
import datetime


class getItemMatriculasByMatriculaId(BaseModel):
    matricula_itemMatricula: int = None
