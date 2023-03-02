from pydantic import BaseModel
import datetime


class actaClass(BaseModel):
    id_acta: int = None
    curso_acta: int = None
    