from pydantic import BaseModel
import datetime


class getEvaluacionesCursoId(BaseModel):
    curso_evaluacion: int = None

class updateOneEvaluacion(BaseModel):
    cantidad_evaluacion: int = None
    curso_evaluacion: int = None
    promedio_evaluacion: int = None