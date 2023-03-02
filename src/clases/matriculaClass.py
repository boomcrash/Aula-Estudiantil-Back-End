from pydantic import BaseModel
import datetime


class getItemMatriculaByEstudianteId(BaseModel):
    estudiante_matricula: int = None
