from pydantic import BaseModel
import datetime


class cursoClass(BaseModel):
    id_curso: int = None
    paralelo_curso: int = None
    materia_curso: int = None
    docente_curso: int = None
    estudiantes_curso: int = None
    ciclo_curso: str = None

class getCursoDocente(BaseModel):
    docente_curso: int = None
    #id_paralelo: int = None
    #id_materia: int = None


class getCursoEstudiante(BaseModel):
    estudiante_matricula: int = None
    #id_paralelo: int = None
    #id_materia: int = None
    #id_curso: int = None
    #id_matricula: int = None
    
class getParticipantesCurso(BaseModel):
    id_curso : int = None