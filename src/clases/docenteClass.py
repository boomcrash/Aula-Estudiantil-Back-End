from pydantic import BaseModel
import datetime


class docenteClass(BaseModel):
    id_docente: int = None
    usuario_docente: int = None
    nombres_docente: str = None
    apellidos_docente: str = None
    cedula_docente: str = None
    fechaNacimiento_docente: datetime.date = None
    edad_docente: int = None
    direccion_docente: str = None
    telefono_docente: str = None
    email_docente: str = None
    titulo_docente: str = None
    nivelEducacion_docente: str = None
    promedio_docente: float = None

class addUserAndDocente(BaseModel):
    nombre_usuario: str
    contrasena_usuario: str
    rol_usuario: int = None
    nombres_docente: str = None
    apellidos_docente: str = None
    cedula_docente: str = None
    fechaNacimiento_docente: datetime.date = None
    edad_docente: int = None
    direccion_docente: str = None
    telefono_docente: str = None
    email_docente: str = None
    titulo_docente: str = None
    nivelEducacion_docente: str = None
    promedio_docente: float = None

class addDocenteByUserId(BaseModel):
    usuario_docente: int = None
    nombres_docente: str = None
    apellidos_docente: str = None
    cedula_docente: str = None
    fechaNacimiento_docente: datetime.date = None
    edad_docente: int = None
    direccion_docente: str = None
    telefono_docente: str = None
    email_docente: str = None
    titulo_docente: str = None
    nivelEducacion_docente: str = None
    promedio_docente: float = None