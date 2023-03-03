from pydantic import BaseModel
import datetime


class getActividadesByCurso(BaseModel):
    curso_actividad : int = None