from pydantic import BaseModel
import datetime


class getAsistenciaEstudianteId(BaseModel):
    estudiante_asistencia: int = None

