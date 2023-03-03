from pydantic import BaseModel
import datetime


class updateEntrega(BaseModel):
    fechaEnvio_entrega  : datetime.date = None
    fechaModificacion_entrega  : datetime.date = None
    archivo_entrega  : str = None
    estado_entrega  : str = None
    

