from pydantic import BaseModel
import datetime


class getItemMateriaByName(BaseModel):
    nombre_materia: int = None
