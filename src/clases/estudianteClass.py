from pydantic import BaseModel
import datetime


class estudianteClass(BaseModel):
    id_estudiante: int = None
    usuario_estudiante: int = None
    nombres_estudiante: str = None
    apellidos_estudiante: str = None
    cedula_estudiante: str = None
    fechaNacimiento_estudiante: datetime.date = None
    edad_estudiante: int = None
    direccion_estudiante: str = None
    telefono_estudiante: str = None
    email_estudiante: str = None
    nivelEducacion_estudiante: str = None
    promedioAnterior_estudiante: float = None
    medio_estudiante: int = None
    estado_estudiante: str = None