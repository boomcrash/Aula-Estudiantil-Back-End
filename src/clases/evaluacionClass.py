from pydantic import BaseModel
import datetime


class getEvaluacionesCursoId(BaseModel):
    curso_evaluacion: int = None
