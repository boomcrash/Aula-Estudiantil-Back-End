
#importando controladores
from controladores.usuario.usuarioController import user_router
from controladores.home.homeController import home_router
from controladores.docenteController import teacher_router
from controladores.estudianteController import student_router
from controladores.moduloController import modulo_router
from controladores.paraleloController import paralelo_router
from controladores.medioController import medio_router
from controladores.rolController import rol_router
from controladores.cursoController import course_router
from controladores.actaController import acta_router
from controladores.horarioController import horario_router
from controladores.asistenciaController import asistencia_router
from controladores.contratoController import contrato_router
from controladores.evaluacionController import evaluacion_router
from controladores.itemActaController import itemActa_router
from controladores.itemMatriculaController import itemMatricula_router
from controladores.materiaController import materia_router
from controladores.matriculaController import matricula_router
from controladores.ordenPagoMatriculaController import ordenPago_router
from controladores.pagoDocenteController import pagoDocente_router
from controladores.actividadController import actividad_router
from controladores.entregaController import entrega_router
#libreria que se importa de configuracion.py (contiene las configuraciones del server)
from configuracion import configuracion
#inicializar flask con fastApi
from fastapi import  FastAPI,Request
#router
from fastapi import APIRouter
#uvicorn execute fastApi
import uvicorn
#pydantic para validar datos
from pydantic import BaseModel
# parametros de peticiones http en body
from fastapi.param_functions import Body
# evitar cors
from fastapi.middleware.cors import CORSMiddleware

#inicializar fastApi
app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



#entrega_router
app.include_router(
    entrega_router,
    prefix='/api/v1/entregas',
    tags=['Entregas'],
    responses={404: {'description': 'Error de acceso a la ventana de entregas'}},
)

#actividad_router
app.include_router(
    actividad_router,
    prefix='/api/v1/actividades',
    tags=['Actividades'],
    responses={404: {'description': 'Error de acceso a la ventana de actividades'}},
)

#pagoDocente_router
app.include_router(
    pagoDocente_router,
    prefix='/api/v1/pagoDocentes',
    tags=['PagoDocentes'],
    responses={404: {'description': 'Error de acceso a la ventana de pagoDocentes'}},
)

#ordenPago_router
app.include_router(
    ordenPago_router,
    prefix='/api/v1/ordenPagoMatriculas',
    tags=['OrdenPagoMatriculas'],
    responses={404: {'description': 'Error de acceso a la ventana de ordenPagoMatriculas'}},
)

#matricula_router
app.include_router(
    matricula_router,
    prefix='/api/v1/matriculas',
    tags=['Matriculas'],
    responses={404: {'description': 'Error de acceso a la ventana de matriculas'}},
)

#materia_router
app.include_router(
    materia_router,
    prefix='/api/v1/materias',
    tags=['Materias'],
    responses={404: {'description': 'Error de acceso a la ventana de materias'}},
)

#itemMatricula_router
app.include_router(
    itemMatricula_router,
    prefix='/api/v1/itemMatriculas',
    tags=['ItemMatriculas'],
    responses={404: {'description': 'Error de acceso a la ventana de itemMatriculas'}},
)

#itemActa_router
app.include_router(
    itemActa_router,
    prefix='/api/v1/itemActas',
    tags=['ItemActas'],
    responses={404: {'description': 'Error de acceso a la ventana de itemActas'}},
)

#evaluacion_router
app.include_router(
    evaluacion_router,
    prefix='/api/v1/evaluaciones',
    tags=['Evaluaciones'],
    responses={404: {'description': 'Error de acceso a la ventana de evaluaciones'}},
)

#contrato
app.include_router(
    contrato_router,
    prefix='/api/v1/contratos',
    tags=['Contratos'],
    responses={404: {'description': 'Error de acceso a la ventana de contratos'}},
)

app.include_router(
    asistencia_router,
    prefix='/api/v1/asistencias',
    tags=['Asistencias'],
    responses={404: {'description': 'Error de acceso a la ventana de asistencias'}},
)

app.include_router(
    horario_router,
    prefix='/api/v1/horarios',
    tags=['Horarios'],
    responses={404: {'description': 'Error de acceso a la ventana de horarios'}},
)


app.include_router(
    acta_router,
    prefix='/api/v1/actas',
    tags=['Actas'],
    responses={404: {'description': 'Error de acceso a la ventana de actas'}},
)

app.include_router(
    course_router,
    prefix='/api/v1/cursos',
    tags=['Cursos'],
    responses={404: {'description': 'Error de acceso a la ventana de cursos'}},
)

app.include_router(
    rol_router,
    prefix='/api/v1/roles',
    tags=['Roles'],
    responses={404: {'description': 'Error de acceso a la ventana de roles'}},
)

app.include_router(
    medio_router,
    prefix='/api/v1/medios',
    tags=['Medios'],
    responses={404: {'description': 'Error de acceso a la ventana de medios'}}
)

app.include_router(
    paralelo_router,
    prefix='/api/v1/paralelos',
    tags=['Paralelos'],
    responses={404: {'description': 'Error de acceso a la ventana de paralelos'}}
)

app.include_router(
    modulo_router,
    prefix='/api/v1/modulos',
    tags=['Modulos'],
    responses={404: {'description': 'Error de acceso a la ventana de modulos'}}
)

###
app.include_router(
    student_router,
    prefix='/api/v1/estudiantes',
    tags=['Estudiantes'],
    responses={404: {'description': 'Error de acceso a la ventana de estudiantes'}}
)

app.include_router(
    teacher_router,
    prefix='/api/v1/docentes',
    tags=['Docentes'],
    responses={404: {'description': 'Error de acceso a la ventana de docentes'}}
)

app.include_router(
    user_router,
    prefix='/api/v1/usuarios',
    tags=['Usuarios'],
    responses={404: {'description': 'Error de acceso a la ventana de usuarios'}}
)

app.include_router(
    home_router,
    prefix='/home',
    tags=['Inicio'],
    responses={404: {'description': 'Error de acceso a la ventana en home'}}
)

#app.include_router(user_router, prefix="/api/v1")

if __name__=="__main__":
    uvicorn.run(app,host=configuracion['development'].HOST,port=configuracion['development'].PORT)