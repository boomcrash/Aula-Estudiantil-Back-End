CREATE DATABASE CENTROARTESANAL; 

USE CENTROARTESANAL;

 DROP TABLE IF EXISTS ItemActa;
 DROP TABLE IF EXISTS Acta;
 DROP TABLE IF EXISTS Entrega;
 DROP TABLE IF EXISTS Actividad;
 DROP TABLE IF EXISTS OrdenPagoMatricula;
 DROP TABLE IF EXISTS ItemMatricula;
 DROP TABLE IF EXISTS Matricula;
 DROP TABLE IF EXISTS ItemEvaluacionDocente;
 DROP TABLE IF EXISTS EvaluacionDocente;
 DROP TABLE IF EXISTS CriterioEvaluacion;
 DROP TABLE IF EXISTS Asistencia;
 DROP TABLE IF EXISTS Estudiante;
 DROP TABLE IF EXISTS Medio;
 DROP TABLE IF EXISTS Horario;
 DROP TABLE IF EXISTS Curso;
 DROP TABLE IF EXISTS Paralelo;
 DROP TABLE IF EXISTS PagoDocente;
 DROP TABLE IF EXISTS Contrato;
 DROP TABLE IF EXISTS Docente;
 DROP TABLE IF EXISTS Materia;
 DROP TABLE IF EXISTS Modulo;
 DROP TABLE IF EXISTS Usuario;
 DROP TABLE IF EXISTS Rol;


CREATE TABLE Rol
(
    id_rol int AUTO_INCREMENT PRIMARY KEY,
    nombre_rol varchar(50) NOT NULL UNIQUE
);



CREATE TABLE Usuario
(
    id_usuario int AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario varchar(200) NOT NULL UNIQUE,
  	contrasena_usuario varchar(16) NOT NULL,
  	rol_usuario int NOT NULL,
		FOREIGN KEY(rol_usuario) REFERENCES Rol(id_rol) 
);




CREATE TABLE Docente
(
    usuario_docente int PRIMARY KEY,
		FOREIGN KEY(usuario_docente) REFERENCES Usuario(id_usuario),
    nombres_docente varchar(100) NOT NULL,
  	apellidos_docente varchar(100) NOT NULL,
  	cedula_docente varchar(10) NOT NULL UNIQUE,
  	fechaNacimiento_docente date NOT NULL,
  	edad_docente int NOT NULL,
  	direccion_docente varchar(100) NOT NULL,
  	telefono_docente varchar(10) NOT NULL UNIQUE,
  	email_docente varchar(200) NOT NULL UNIQUE,
  	titulo_docente varchar(100) NOT NULL,
  	nivelEducacion_docente varchar(10) NOT NULL 
  		CHECK(nivelEducacion_docente IN('3er nivel', '4to nivel')),
  	estado_docente varchar(10) NOT NULL DEFAULT 'Activo'
  		CHECK(estado_docente IN('Activo', 'Inactivo', 'Suspendido'))
);



CREATE TABLE Contrato
(
    docente_contrato int PRIMARY KEY,
		FOREIGN KEY(docente_contrato) REFERENCES Docente(usuario_docente),
    fecha_contrato Date NOT NULL,
	ciclo_contrato varchar(20) NOT NULL DEFAULT '2023-2024 CI'
		CHECK(ciclo_contrato IN('2022-2023 CI', '2022-2023 CII', '2023-2024 CI')),
	nombramiento_contrato varchar(2) NOT NULL
		CHECK(nombramiento_contrato IN('SI', 'NO')),
	especialidad_contrato varchar(2) NOT NULL
		CHECK(especialidad_contrato IN('SI', 'NO')),
	tipo_contrato varchar(20) NOT NULL
		CHECK(tipo_contrato IN('Docente titular', 'Técnico docente')),
	jornada_contrato varchar(100) NOT NULL
		CHECK(jornada_contrato IN('Tiempo completo', 'Medio tiempo')),
	sueldo_contrato decimal(7,2) NOT NULL
);



CREATE TABLE PagoDocente
( 
    id_pagoDocente int PRIMARY KEY  AUTO_INCREMENT,
    docente_pagoDocente int  NOT NULL,
		FOREIGN KEY(docente_pagoDocente) REFERENCES Docente(usuario_docente),
    fecha_pagoDocente Date NOT NULL,
  	faltas_pagoDocente int NOT NULL DEFAULT 0,
  	descuento_pagoDocente decimal(7,2) NOT NULL DEFAULT 0,
  	total_pagoDocente decimal(7,2) NOT NULL
);
ALTER TABLE PagoDocente ADD UNIQUE (docente_pagoDocente, fecha_pagoDocente);




CREATE TABLE Modulo
(
    id_modulo int AUTO_INCREMENT PRIMARY KEY,
    nombre_modulo varchar(50) NOT NULL UNIQUE,
	precio_modulo decimal(5,2) NOT NULL
);



CREATE TABLE Materia
(
    id_materia int AUTO_INCREMENT PRIMARY KEY,
    nombre_materia varchar(50) NOT NULL UNIQUE,
	precio_materia decimal(4,2) NOT NULL,
	modulo_materia int NOT NULL,
		FOREIGN KEY(modulo_materia) REFERENCES Modulo(id_modulo) 
);



CREATE TABLE Paralelo
(
    id_paralelo int AUTO_INCREMENT PRIMARY KEY,
    nombre_paralelo varchar(10) NOT NULL
);



CREATE TABLE Curso
(
	id_curso int AUTO_INCREMENT PRIMARY KEY,
    paralelo_curso int NOT NULL,
		FOREIGN KEY(paralelo_curso) REFERENCES Paralelo(id_paralelo) ,
    materia_curso int NOT NULL,
		FOREIGN KEY(materia_curso) REFERENCES Materia(id_materia),
	docente_curso int NOT NULL,
		FOREIGN KEY(docente_curso) REFERENCES Docente(usuario_docente) ,
    ciclo_curso varchar(20) NOT NULL
		CHECK(ciclo_curso IN('2022-2023 CI', '2022-2023 CII', '2023-2024 CI')),
	estudiantes_curso int NOT NULL DEFAULT 0
);
ALTER TABLE Curso ADD UNIQUE (paralelo_curso, materia_curso);




CREATE TABLE Horario
(
	id_Horario int PRIMARY KEY AUTO_INCREMENT,
	curso_horario int NOT NULL,
		FOREIGN KEY(curso_horario) REFERENCES Curso(id_curso),
	dia_horario varchar(10)
		CHECK(dia_horario IN('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo')),
	horaInicio_horario varchar(5) NOT NULL,
	horaFin_horario varchar(5) NOT NULL
);
ALTER TABLE Horario ADD UNIQUE (curso_horario, dia_horario);




CREATE TABLE Medio
(
    id_medio int AUTO_INCREMENT PRIMARY KEY,
    nombre_medio varchar(20) NOT NULL
);



CREATE TABLE Estudiante 
(
    usuario_estudiante int PRIMARY KEY,
		FOREIGN KEY(usuario_estudiante) REFERENCES Usuario(id_usuario),
    nombres_estudiante varchar(100) NOT NULL,
  	apellidos_estudiante varchar(100) NOT NULL,
  	cedula_estudiante varchar(10) NOT NULL UNIQUE,
  	fechaNacimiento_estudiante date NOT NULL,
    edad_estudiante int NOT NULL,
  	direccion_estudiante varchar(100) NOT NULL,
  	telefono_estudiante varchar(10) NOT NULL UNIQUE,
  	email_estudiante varchar(200) NOT NULL UNIQUE,
  	nivelEducacion_estudiante varchar(10) NOT NULL 
  		CHECK(nivelEducacion_estudiante IN('1er nivel', '2do nivel', '3er nivel', '4to nivel')),
  	promedioAnterior_estudiante decimal(4,2) NOT NULL,
  	medio_estudiante int NOT NULL,
		FOREIGN KEY(medio_estudiante) REFERENCES Medio(id_medio) ,
  	estado_estudiante varchar(10) NOT NULL DEFAULT 'Activo'
  		CHECK(estado_estudiante IN('Activo', 'Inactivo'))
);




CREATE TABLE Asistencia
(
    id_asistencia int PRIMARY KEY AUTO_INCREMENT,
    curso_asistencia int NOT NULL,
		FOREIGN KEY(curso_asistencia) REFERENCES Curso(id_curso) ,
    estudiante_asistencia int NOT NULL,
		FOREIGN KEY(estudiante_asistencia) REFERENCES Estudiante(usuario_estudiante) ,
	fecha_asistencia Date NOT NULL,
	estado_asistencia varchar(10) NOT NULL
		CHECK(estado_asistencia IN('Presente', 'Falta')),
	ciclo_asistencia varchar(20) NOT NULL DEFAULT '2022-2023 CII'
		CHECK(ciclo_asistencia IN('2022-2023 CI', '2022-2023 CII', '2023-2024 CI'))
);
ALTER TABLE Asistencia ADD UNIQUE (curso_asistencia, estudiante_asistencia, fecha_asistencia);




CREATE TABLE CriterioEvaluacion
(
    id_criterio int AUTO_INCREMENT PRIMARY KEY,
    descripcion_criterio varchar(200) NOT NULL
);




CREATE TABLE EvaluacionDocente
(
    id_evaluacion int AUTO_INCREMENT PRIMARY KEY,
	curso_evaluacion int NOT NULL,
		FOREIGN KEY(curso_evaluacion) REFERENCES Curso(id_curso) ,
    estudiante_evaluacion int NOT NULL,
		FOREIGN KEY(estudiante_evaluacion) REFERENCES Estudiante(usuario_estudiante) ,
	ciclo_evaluacion varchar(20) NOT NULL DEFAULT '2022-2023 CII'
		CHECK(ciclo_evaluacion IN('2022-2023 CI', '2022-2023 CII', '2023-2024 CI')),
	promedio_evaluacion decimal(3,2) NOT NULL
);
ALTER TABLE EvaluacionDocente ADD UNIQUE (curso_evaluacion, estudiante_evaluacion, ciclo_evaluacion);





CREATE TABLE ItemEvaluacionDocente
(
    id_itemEvaluacion int PRIMARY KEY AUTO_INCREMENT,
    evaluacion_itemEvaluacion int ,
		FOREIGN KEY(evaluacion_itemEvaluacion) REFERENCES EvaluacionDocente(id_evaluacion) ,
    criterio_itemEvaluacion int ,
		FOREIGN KEY(criterio_itemEvaluacion) REFERENCES CriterioEvaluacion(id_criterio) ,
	nota_itemEvaluacion int NOT NULL
);
ALTER TABLE ItemEvaluacionDocente ADD UNIQUE (evaluacion_itemEvaluacion, criterio_itemEvaluacion);




CREATE TABLE Matricula
(
    id_matricula int AUTO_INCREMENT PRIMARY KEY,
    estudiante_matricula int NOT NULL,
		FOREIGN KEY(estudiante_matricula) REFERENCES Estudiante(usuario_estudiante),
	fecha_matricula Date NOT NULL,
	ciclo_matricula varchar(20) NOT NULL  DEFAULT '2023-2024 CI'
		CHECK(ciclo_matricula IN('2022-2023 CI', '2022-2023 CII', '2023-2024 CI'))
);
ALTER TABLE Matricula ADD UNIQUE (estudiante_matricula, ciclo_matricula);




CREATE TABLE ItemMatricula
(
    id_itemMatricula int PRIMARY KEY AUTO_INCREMENT,
    matricula_itemMatricula int NOT NULL,
		FOREIGN KEY(matricula_itemMatricula) REFERENCES Matricula(id_matricula),
    curso_itemMatricula int NOT NULL,
		FOREIGN KEY(curso_itemMatricula) REFERENCES Curso(id_curso)
);
ALTER TABLE ItemMatricula ADD UNIQUE (matricula_itemMatricula, curso_itemMatricula);




CREATE TABLE OrdenPagoMatricula
(
    matricula_pagoMatricula int PRIMARY KEY,
		FOREIGN KEY(matricula_pagoMatricula) REFERENCES Matricula(id_matricula),
    item_pagoMatricula varchar(100) NOT NULL
		CHECK(item_pagoMatricula IN('Materia individual', 'Modulo 1', 'Modulo 2')),
	cantidad_pagoMatricula int NOT NULL,
	subtotal_pagoMatricula decimal(5,2) NOT NULL,
	descuento_pagoMatricula decimal(4,2) NOT NULL,
	total_pagoMatricula decimal(5,2) NOT NULL
);




CREATE TABLE Actividad
(
    id_actividad int AUTO_INCREMENT PRIMARY KEY,
    curso_actividad int NOT NULL,
		FOREIGN KEY(curso_actividad) REFERENCES Curso(id_curso),
	fechaVencimiento_actividad Date NOT NULL,
	fechaPublicacion_actividad Date NOT NULL,
	nombre_actividad varchar(100) NOT NULL,
	descripcion_actividad varchar(200) NOT NULL,
	archivosPermitidos_actividad varchar(20) NOT NULL
		CHECK(archivosPermitidos_actividad IN('.txt', '.docx', '.xlsx', '.pdf', '.png', '.jpg')),
	tipo_actividad varchar(10) NOT NULL DEFAULT 'Tarea'
		CHECK(tipo_actividad IN('Tarea', 'Examen final', 'Examen de recuperación')),
	estado_actividad varchar(10) NOT NULL DEFAULT 'Activa'
		CHECK(estado_actividad IN('Activa', 'Inactiva')),
	ciclo_actividad varchar(20) NOT NULL DEFAULT '2022-2023 CII'
		CHECK(ciclo_actividad IN('2022-2023 CI', '2022-2023 CII', '2023-2024 CI'))
);




CREATE TABLE Entrega
(
    actividad_entrega int PRIMARY KEY,
		FOREIGN KEY(actividad_entrega) REFERENCES Actividad(id_actividad),
    estudiante_entrega int NOT NULL,
		FOREIGN KEY(estudiante_entrega) REFERENCES Estudiante(usuario_estudiante),
	fechaEnvio_entrega date,
	fechaModificacion_entrega date,
	archivo_entrega varchar(200),
	calificacion_entrega decimal(4,2),
	estado_entrega varchar(10) NOT NULL DEFAULT 'Pendiente'
		CHECK(estado_entrega IN('Pendiente', 'Enviada', 'No enviada'))
);
ALTER TABLE Entrega ADD UNIQUE (actividad_entrega, estudiante_entrega);




CREATE TABLE Acta
(
    id_acta int AUTO_INCREMENT PRIMARY KEY,
    curso_acta int NOT NULL,
		FOREIGN KEY(curso_acta) REFERENCES Curso(id_curso),
    ciclo_acta varchar(20) NOT NULL
		CHECK(ciclo_acta IN('2022-2023 CI', '2022-2023 CII', '2023-2024 CI'))
);
ALTER TABLE Acta ADD UNIQUE (curso_acta, ciclo_acta);



CREATE TABLE ItemActa
(
    acta_itemActa int PRIMARY KEY,
		FOREIGN KEY(acta_itemActa) REFERENCES Acta(id_acta),
    estudiante_itemActa int NOT NULL,
		FOREIGN KEY(estudiante_itemActa) REFERENCES Estudiante(usuario_estudiante),
  	promedioCalificaciones_itemActa decimal(4,2) NOT NULL,
  	promedioAsistencias_itemActa int NOT NULL,
  	estado_itemActa varchar(100) NOT NULL
  		CHECK(estado_itemActa IN('Aprobado', 'Reprobado'))
);
ALTER TABLE ItemActa ADD UNIQUE (acta_itemActa, estudiante_itemActa);

