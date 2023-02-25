USE CENTROARTESANAL;

#----------------------------------------------------------------------
INSERT INTO Rol (nombre_rol) VALUES 
    ('Estudiante'),
    ('Docente'),
    ('Administrador');
    
    
#----------------------------------------------------------------------
INSERT INTO Usuario (nombre_usuario, contrasena_usuario, rol_usuario) VALUES 
    ('admin777', '12345678', 3),
	('david_vega25', '12345678', 2),
	('luis_romero22', '12345678', 2),
	('fabián_chávez12', '12345678', 2),
	('diego_gómez07', '12345678', 2),
	('rosa_villalba30', '12345678', 2),
	('juan_ocampo18', '12345678', 2),
	('mauricio_torres25', '12345678', 2),
	('marcela_molina01', '12345678', 2),
	('juan_garcía15', '12345678', 2),
	('ana_vélez31', '12345678', 2),
	('mauricio_vega17', '12345678', 2),
	('andrés_cevallos15', '12345678', 2),
	('julio_suárez11', '12345678', 2),
	('diego_león09', '12345678', 2),
	('rosa_gonzález30', '12345678', 2),
	('maría_garcía18', '12345678', 2),
	('daniela_mora01', '12345678', 2),
	('karina_aguirre19', '12345678', 2),
	('francisco_moreira04', '12345678', 2),
	('sofía_reyes17', '12345678', 2),
	('jorge_castro23', '12345678', 2),
	('pablo_lópez23', '12345678', 2),
	('nicolás_arboleda31', '12345678', 2),
	('jorge_garcía29', '12345678', 2),
	('ana_gonzález12', '12345678', 2),
	('margarita_cordova27', '12345678', 2),
	('carlos_rodríguez03', '12345678', 2),
	('sara_lópez22', '12345678', 2),
	('pedro_sánchez20', '12345678', 2),
	('patricia_pazmiño08', '12345678', 2),
	('hugo_vargas15', '12345678', 2),
	('ana_moreno18', '12345678', 2),
	('mario_guzmán10', '12345678', 2),
	('héctor_cedeño05', '12345678', 2),
	('gabriela_molina10', '12345678', 2),
	('carla_figueroa15', '12345678', 2),
	('marcelo_pazmiño23', '12345678', 2),
	('sofía_gonzález08', '12345678', 2),
	('luis_lópez10', '12345678', 2),
	('verónica_mora14', '12345678', 2),
	('sandra_bermúdez05', '12345678', 2),
	('carla_sánchez12', '12345678', 2),
	('johanna_gonzalez09', '12345678', 1),
	('sofia_lopez20', '12345678', 1),
	('carlos_garcia12', '12345678', 1),
	('ana_morales01', '12345678', 1),
	('luis_ramirez30', '12345678', 1),
	('martha_alvarado10', '12345678', 1),
	('pedro_diaz23', '12345678', 1),
	('ariana_perez15', '12345678', 1),
	('david_vega05', '12345678', 1),
	('erick_gonzalez15', '12345678', 1),
	('karen_rojas10', '12345678', 1),
	('josé_alvarado12', '12345678', 1),
	('cristina_ponce22', '12345678', 1),
	('mario_zambrano07', '12345678', 1),
	('jenny_borja15', '12345678', 1),
	('luis_jimenez30', '12345678', 1),
	('jessica_romero01', '12345678', 1),
	('carlos_garcía16', '12345678', 1),
	('gabriela_garcia17', '12345678', 1),
	('pedro_pérez23', '12345678', 1),
	('jorge_paredes22', '12345678', 1),
	('paola_lopez06', '12345678', 1),
	('lorena_carrion14', '12345678', 1),
	('carlos_gonzalez23', '12345678', 1),
	('maria_castro08', '12345678', 1),
	('andres_mendez03', '12345678', 1),
	('esteban_vargas23', '12345678', 1),
	('karla_lara31', '12345678', 1),
	('miguel_gomez28', '12345678', 1),
	('johana_zambrano15', '12345678', 1),
	('marcelo_lopez18', '12345678', 1),
	('martha_molina22', '12345678', 1),
	('andrés_vargas15', '12345678', 1),
	('juan_fernandez03', '12345678', 1),
	('luis_zambrano08', '12345678', 1),
	('roberto_pazmiño01', '12345678', 1),
	('erika_chicaiza16', '12345678', 1),
	('fernando_sanchez28', '12345678', 1),
	('rosa_vera18', '12345678', 1),
	('diego_molina11', '12345678', 1),
	('mauricio_garcía09', '12345678', 1),
	('david_paredes14', '12345678', 1),
	('maría_vélez23', '12345678', 1),
	('paola_sandoval11', '12345678', 1),
	('gabriela_rojas17', '12345678', 1),
	('juan_mora28', '12345678', 1),
	('cristina_pazmiño12', '12345678', 1),
	('andres_guerrero02', '12345678', 1),
	('luis_velasco29', '12345678', 1),
	('daniela_garcía30', '12345678', 1),
	('julio_bastidas21', '12345678', 1);



#----------------------------------------------------------------------
INSERT INTO Docente (usuario_docente, nombres_docente, apellidos_docente, cedula_docente, fechaNacimiento_docente, 
					 edad_docente, direccion_docente, telefono_docente, email_docente,
					 titulo_docente, nivelEducacion_docente, estado_docente) VALUES 
    #-- TECNOLOGIA ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
	(2, 'David Roberto', 'Vega Vélez', '0412045683', '1978-04-25', 45, 'El recreo 2da etapa', '0969710545', 'davidroberto@gmail.com', 'Ingeniero en Software', '3er nivel', 'Activo') ,
	(3, 'Luis Eduardo', 'Romero Vargas', '0103182456', '1980-06-22', 43, 'Calle Los Pinos', '0973546897', 'luiseromero@gmail.com', 'Ingeniero en Electrónica', '3er nivel', 'Activo') ,
	(4, 'Fabián Andrés', 'Chávez Pérez', '2304119876', '1990-07-12', 33, 'Ciudadela Los Ceibos', '0946763805', 'fabian.chavez@gmail.com', 'Ingeniero en Telecomunicaciones', '3er nivel', 'Activo') ,
	(5, 'Diego Xavier', 'Gómez Córdova', '1204151289', '1981-11-07', 42, 'Urdesa Central', '0951512737', 'diego.gomez@gmail.com', 'Ingeniero en Sistemas', '3er nivel', 'Activo') ,
	(6, 'Rosa Angélica', 'Villalba Chávez', '0319023457', '1979-01-30', 44, 'Calle Los Ríos', '0985929673', 'rosa.villalba@gmail.com', 'Ingeniera en Electrónica', '3er nivel', 'Activo') ,
	(7, 'Juan Carlos', 'Ocampo Ortiz', '2405037890', '1985-06-18', 38, 'Calle La Ría', '0994713540', 'juancarlos.ocampo@gmail.com', 'Ingeniero en Software', '3er nivel', 'Activo') ,
	(8, 'Mauricio José', 'Torres Garcés', '0401148902', '1987-11-25', 36, 'Calle Nueva Kennedy', '0939557850', 'mauricio.torres@gmail.com', 'Ingeniero en Electrónica', '3er nivel', 'Activo') ,
	(9, 'Marcela Alexandra', 'Molina García', '0302145671', '1991-09-01', 32, 'Los Ceibos', '0945954075', 'marcela.molina@gmail.com', 'Ingeniera en Telecomunicaciones', '3er nivel', 'Activo') ,

	(10, 'Juan Carlos', 'García Pérez', '1501053482', '1985-10-15', 38, 'Av. 9 de Octubre', '0954653709', 'juancarlos.garcia@gmail.com', 'Master en Inteligencia Artificial', '4to nivel', 'Activo') ,
	(11, 'Ana Cristina', 'Vélez Ramírez', '2204037896', '1993-12-31', 30, 'Ciudadela La Alborada', '0971165218', 'anacristina.velez@gmail.com', 'Master en Ciencia de datos', '4to nivel', 'Activo') ,
	(12, 'Mauricio Esteban', 'Vega Vélez', '0711142789', '1981-03-17', 42, 'Ciudadela La Garzota', '0920252922', 'mauricio.vega@gmail.com', 'Master en Ciencias de la Computación', '4to nivel', 'Activo') ,
	(13, 'Andrés Felipe', 'Cevallos Zamora', '2001056793', '1991-12-15', 32, 'Calle Rocafuerte', '0913392041', 'andres.cevallos@gmail.com', 'Master en Inteligencia Artificial', '4to nivel', 'Activo') ,
	(14, 'Julio César', 'Suárez Vélez', '2404012345', '1988-11-11', 35, 'Cdla. La Kennedy', '0945054374', 'julio.suarez@gmail.com', 'Master en Ciencias de la Computación', '4to nivel', 'Activo') ,
	(15, 'Diego Andrés', 'León Arana', '2005147890', '1988-07-09', 35, 'Ciudadela La Alborada', '0960012160', 'diego.leon@gmail.com', 'Master en Ciencia de datos', '4to nivel', 'Activo') ,
	(16, 'Rosa María', 'González Mora', '1501053782', '1978-03-30', 45, 'Sauces 9', '0946455079', 'rosa.gonzalez@gmail.com', 'Master en Ciencia de datos', '4to nivel', 'Activo') ,

	#--  FINANZAS BASICAS ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
	(17, 'María Fernanda', 'García Torres', '0801057891', '1992-06-18', 31, 'Calle Alborada', '0958993856', 'maria.garcia@gmail.com', 'Licenciada en Finanzas', '3er nivel', 'Activo') ,
	(18, 'Daniela Belén', 'Mora Alvarado', '2001146789', '1995-10-01', 28, 'Calle Rocafuerte', '0982443088', 'daniela.mora@gmail.com', 'Contadora Pública autorizada', '3er nivel', 'Activo') ,
	(19, 'Karina Alejandra', 'Aguirre Castro', '1203045687', '1981-12-19', 42, 'Cdla. Urdesa Central', '0973084962', 'karina.aguirre@gmail.com', 'Licenciada en Finanzas', '3er nivel', 'Activo') ,
	(20, 'Francisco Eduardo', 'Moreira Rodríguez', '0503024568', '1992-01-04', 31, 'Samborondón', '0916087061', 'francisco.moreira@gmail.com', 'Contador Público Autorizado', '3er nivel', 'Activo') ,
	(21, 'Sofía Beatriz', 'Reyes Vélez', '0701148903', '1996-09-17', 27, 'Calle El Oro', '0938535761', 'sofia.reyes@gmail.com', 'Licenciada en Finanzas', '3er nivel', 'Activo') ,

	(22, 'Jorge Luis', 'Castro Alvarado', '1604052378', '1976-02-23', 47, 'Cdla. Urdesa', '0986352603', 'jorge.castro@gmail.com', 'Master en Finanzas', '4to nivel', 'Activo') ,
	(23, 'Pablo Alejandro', 'López Chávez', '1203045679', '1978-05-23', 45, 'Calle San Gabriel', '0979937404', 'pablo.lopez@gmail.com', 'Master en Administración de Empresas', '4to nivel', 'Activo') ,
	(24, 'Nicolás Alberto', 'Arboleda Jiménez', '2401047890', '1990-07-31', 33, 'Los Esteros', '0989725412', 'nicolas.arboleda@gmail.com', 'Master en Finanzas', '3er nivel', 'Activo') ,
	(25, 'Jorge Luis', 'García Castro', '2304056890', '1974-06-29', 49, 'Cdla. Alborada', '0982464078', 'jorge.garcia@gmail.com', 'Master en Finanzas', '4to nivel', 'Activo') ,

	#--  INGLES ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
	(26, 'Ana María', 'González García', '2405146790', '1988-07-12', 35, 'Av. de las Américas', '0932121222', 'anamariagonzalez@gmail.com', 'Licenciada en Idiomas', '3er nivel', 'Activo') ,
	(27, 'Margarita Rosa', 'Cordova Pérez', '0502056893', '1985-07-27', 38, 'Cdla. La Garzota', '0917799176', 'margarita.cordova@gmail.com', 'Licenciada en Idiomas', '3er nivel', 'Activo') ,
	(28, 'Carlos Andrés', 'Rodríguez Mera', '2204057892', '1978-10-03', 45, 'Cdla. Kennedy Norte', '0942378709', 'carlos.rodriguez@gmail.com', 'Licenciado en Idiomas', '3er nivel', 'Activo') ,
	(29, 'Sara Beatriz', 'López Reyes', '0302145672', '1990-05-22', 33, 'Cdla. Alborada', '0967188039', 'sara.lopez@gmail.com', 'Licenciada en Idiomas', '3er nivel', 'Activo') ,

	(30, 'Pedro Antonio', 'Sánchez Vargas', '0411046789', '1975-05-20', 48, 'Calle 9 de Octubre', '0951070626', 'pedro.sanchez@gmail.com', 'Master en enseñanza de idiomas', '4to nivel', 'Activo') ,
	(31, 'Patricia María', 'Pazmiño Chávez', '0102184569', '1982-09-08', 41, 'Calle Los Ceibos', '0979526988', 'patricia.pazmino@gmail.com', 'Master en enseñanza de idiomas', '4to nivel', 'Activo') ,
	(32, 'Hugo Enrique', 'Vargas Quintero', '2304057893', '1985-03-15', 38, 'Calle Los Ríos', '0980605036', 'hugo.vargas@gmail.com', 'Master en enseñanza de idiomas', '4to nivel', 'Activo') ,
	(33, 'Ana Cristina', 'Moreno López', '0412045684', '1983-12-18', 40, 'Calle Vélez', '0922340020', 'ana.moreno@gmail.com', 'Master en enseñanza de idiomas', '4to nivel', 'Activo') ,
	(34, 'Mario Fernando', 'Guzmán Arévalo', '2405037891', '1980-02-10', 43, 'Av. Las Lomas', '0936801053', 'mario.guzman@gmail.com', 'Master en enseñanza de idiomas', '3er nivel', 'Activo') ,

	#--  DERECHO LABORAL ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
	(35, 'Héctor Eduardo', 'Cedeño Bravo', '2304057894', '1983-03-05', 40, 'Calle Junín', '0986206869', 'hector.cedeno@gmail.com', 'Abogado especialista en Derecho Laboral', '3er nivel', 'Activo') ,
	(36, 'Gabriela Alejandra', 'Molina Gómez', '1203045678', '1996-09-10', 27, 'Cdla. Los Ceibos', '0933060951', 'gabriela.molina@gmail.com', 'Abogado especialista en Derecho Laboral', '3er nivel', 'Activo') ,
	(37, 'Carla Isabel', 'Figueroa Pérez', '1501053483', '1980-12-15', 43, 'Av. 9 de Octubre', '0971089077', 'carlafigueroa@gmail.com', 'Abogada especialista en Derecho Laboral', '3er nivel', 'Activo') ,
	(38, 'Marcelo Enrique', 'Pazmiño López', '0319023458', '1978-06-23', 45, 'Calle Los Cipreses', '0952821820', 'marcelopazmino@gmail.com', 'Abogado especialista en Derecho Laboral', '3er nivel', 'Activo') ,

	(39, 'Sofía Maribel', 'González Mera', '2401047891', '1973-03-08', 50, 'Cdla. Kennedy', '0918568247', 'sofiagonzalez@gmail.com', 'Doctora en Derecho Laboral', '4to nivel', 'Activo') ,
	(40, 'Luis Eduardo', 'López Paz', '1203045677', '1985-02-10', 38, 'Av. de las Américas', '0959271954', 'luislopez@gmail.com', 'Master en Derecho Laboral', '4to nivel', 'Activo') ,
	(41, 'Verónica Alexandra', 'Mora Cedeño', '2204037895', '1987-11-14', 36, 'Calle Los Alamos', '0961422455', 'veronicamora@gmail.com', 'Master en Derecho Laboral', '4to nivel', 'Activo') ,
	(42, 'Sandra Elizabeth', 'Bermúdez Zambrano', '2404012346', '1980-12-05', 43, 'Cdla. Kennedy Norte', '0927574944', 'sandra.bermudez@gmail.com', 'Doctora en Derecho Laboral', '4to nivel', 'Activo') ,
	(43, 'Carla Gabriela', 'Sánchez Gómez', '0912345678', '1987-08-12', 36, 'Calle Víctor Emilio Estrada', '0934147711', 'carla.sanchez@gmail.com', 'Master en Derecho Laboral', '4to nivel', 'Activo');






#---------------------------------------------------------------------- 
#INSERT INTO Contrato (docente_contrato, fecha_contrato, ciclo_contrato, nombramiento_contrato, especialidad_contrato,
#					  tipo_contrato, jornada_contrato, sueldo_contrato) VALUES 
#    (2, '2022-02-03', '2022-2023 CI', 'Si', 'Si', 'Docente titular', 'Tiempo completo', 1300.00);



#---------------------------------------------------------------------- PAGO DOCENTE





#----------------------------------------------------------------------
INSERT INTO Modulo (nombre_modulo, precio_modulo) VALUES 
    ('Módulo 1',300.00),
    ('Módulo 2',400.00);



#----------------------------------------------------------------------
INSERT INTO Materia (nombre_materia, precio_materia, modulo_materia) VALUES 
    ('Mantenimiento de Computadoras',86.00,1),
	('Robótica',86.00,1),
	('Desarrollo Web',86.00,1),
	('Ingles',86.00,1),
	('Cableado Estruturado',86.00,1),
	('Base de Datos',86.00,2),
	('Bigdata',86.00,2),
	('Machine Learning',86.00,2),
	('Finanzas Básicas',86.00,2),
	('Derecho Laboral',86.00,2);



#----------------------------------------------------------------------
INSERT INTO Paralelo (nombre_paralelo) VALUES 
    # paralelos del modulo 1
    ('MOD-1-1'),
    ('MOD-1-2'),
	('MOD-1-3'),
    ('MOD-1-4'),
	('MOD-1-5'),
    ('MOD-1-6'),

	# paralelos del modulo 2
	('MOD-2-1'),
    ('MOD-2-2'),
	('MOD-2-3'),
    ('MOD-2-4'),
    ('MOD-2-5'),
	('MOD-2-6');




#----------------------------------------------------------------------
#INSERT INTO Curso (paralelo_curso, materia_curso, docente_curso, ciclo_curso) VALUES 
#    (1, 1, 2, '2022-2023 CI');





#---------------------------------------------------------------------- 
#INSERT INTO Horario (curso_horario, dia_horario, horaInicio_horario, horaFin_horario) VALUES 
#    (1, 'Lunes', '13:00', '15:00');





#---------------------------------------------------------------------- 
INSERT INTO Medio (nombre_medio) VALUES 
    ('Radio'),
    ('TV'),
	('Periódico'),
    ('Volantes'),
	('WhatsApp'),
    ('Redes sociales');




#----------------------------------------------------------------------
INSERT INTO Estudiante (usuario_estudiante, nombres_estudiante, apellidos_estudiante, cedula_estudiante, fechaNacimiento_estudiante,
						edad_estudiante, direccion_estudiante, telefono_estudiante, email_estudiante, nivelEducacion_estudiante, 
						promedioAnterior_estudiante, medio_estudiante) VALUES 
    
	(44, 'Johanna Mishelle', 'Gonzalez Suarez', '0347365019', '2004-12-03', 18, 'Calle Amazonas y la 7ma', '0963264464', 'johannagonzalez@gmail.com', '2do nivel', 9.5, 5) ,
	(45, 'Sofia Mariana', 'Lopez Choez', '0813579600', '2005-09-18', 17, 'Av. América y La Prensa', '0974629950', 'sofialopez@gmail.com', '1er nivel', 9.2, 5) ,
	(46, 'Carlos Daniel', 'Garcia Vargas', '0932518646', '2010-03-13', 12, 'Calle Los Rios y la H', '0950386759', 'carlosgarcia12@gmail.com', '3er nivel', 9.87, 4) ,
	(47, 'Ana Valeria', 'Morales Ortiz', '2322783146', '2012-05-22', 20, 'Calle Quito y la 3ra', '0991926392', 'anamorales@gmail.com', '2do nivel', 8.5, 4) ,
	(48, 'Luis Miguel', 'Ramirez Zambrano', '1222719855', '2008-11-14', 15, 'Av. de las Américas y Naciones Unidas', '0940262945', 'luisramirez@gmail.com', '1er nivel', 8.0, 5) ,
	(49, 'Martha Isabel', 'Alvarado Gómez', '2253792046', '2010-01-29', 21, 'Av. 12 de Octubre y Cordero', '0924792446', 'marthaalvarado@gmail.com', '3er nivel', 9.9, 5) ,
	(50, 'Pedro José', 'Diaz Barros', '2459047582', '2010-09-10', 12, 'Av. Mariana de Jesus y Nuñez de Vela', '0939611691', 'pedrodiaz@gmail.com', '2do nivel', 9.65, 5) ,
	(51, 'Ariana Elizabeth', 'Perez Castro', '1830594673', '2008-02-06', 15, 'Calle 9 de Octubre y La Ronda', '0937384752', 'arianaperez@gmail.com', '2do nivel', 7.5, 5) ,
	(52, 'David Alejandro', 'Vega Espinosa', '1117501491', '1995-09-20', 28, 'Calle Garcia Moreno y la 5ta', '0950154954', 'davidvega@gmail.com', '1er nivel', 8.75, 5) ,
	(53, 'Erick Santiago', 'Gonzalez Jaramillo', '1148034264', '2002-08-01', 21, 'Calle Juan Montalvo y la 12', '0969922798', 'erickgonzalez@gmail.com', '2do nivel', 9.2, 1) ,
	(54, 'Karen Patricia', 'Rojas Chávez', '0907431964', '2003-04-17', 20, 'Calle Las Higueras y la 14', '0916274460', 'karenrojas@gmail.com', '2do nivel', 8.8, 4) ,
	(55, 'José Eduardo', 'Alvarado Paredes', '1614237519', '1995-06-18', 28, 'Calle 10 de Agosto y 5ta', '0952070658', 'josealvarado@gmail.com', '3er nivel', 8.87, 2) ,
	(56, 'Cristina Elizabeth', 'Ponce Zambrano', '2135470264', '2010-06-24', 12, 'Av. Juan Montalvo y Los Rios', '0947414137', 'cristinaponce@gmail.com', '2do nivel', 9.68, 3) ,
	(57, 'Mario Antonio', 'Zambrano Vera', '2357328919', '2010-02-05', 12, 'Calle Bolivar y San Martin', '0938715024', 'mariozambrano@gmail.com', '1er nivel', 7.75, 1) ,
	(58, 'Jenny Maritza', 'Borja Vega', '0751928055', '1998-11-21', 25, 'Av. Quito y la 19', '0989312739', 'jennyborja@gmail.com', '3er nivel', 8.92, 2) ,
	(59, 'Luis Alberto', 'Jimenez Montenegro', '1002916500', '2003-05-15', 20, 'Calle Sucre y 18 de Noviembre', '0910408143', 'luisjimenez@gmail.com', '2do nivel', 9.37, 3) ,
	(60, 'Jessica Carolina', 'Romero Torres', '2000127455', '2002-03-09', 21, 'Av. Atahualpa y La 5ta', '0966732866', 'jessicaromero@gmail.com', '2do nivel', 9.15, 1) ,
	(61, 'Carlos Andrés', 'García Macías', '1239453619', '1995-08-20', 28, 'Av. La Paz y San Martin', '0991472363', 'carlosgarcia@gmail.com', '1er nivel', 7.99, 2) ,
	(62, 'Gabriela Fernanda', 'Garcia Rosales', '0251465291', '2008-01-09', 15, 'Calle Manta y Bolivar', '0916820216', 'gabrielagarcia@gmail.com', '2do nivel', 9.82, 3) ,
	(63, 'Pedro Antonio', 'Pérez Zamora', '0426245891', '2004-07-11', 19, 'Calle Pichincha y Juan Montalvo', '0928320566', 'pedroperez@gmail.com', '3er nivel', 8.71, 5) ,
	(64, 'Jorge Luis', 'Paredes Alcivar', '1441593400', '1995-02-03', 28, 'Av. Sucre y La Roca', '0993990845', 'jorgeparedes@gmail.com', '2do nivel', 9.75, 2) ,
	(65, 'Paola Jazmin', 'Lopez Andrade', '1244780328', '2010-06-04', 12, 'Calle Sucre y la 3ra', '0942073330', 'paolalopez@gmail.com', '3er nivel', 9.7, 2) ,
	(66, 'Lorena Estefania', 'Carrion Ortiz', '1256892400', '1998-08-19', 25, 'Calle Bolivar y la 10ma', '0912980764', 'lorenacarrion@gmail.com', '2do nivel', 8.9, 5) ,
	(67, 'Carlos Eduardo', 'Gonzalez Carrera', '0842369455', '2002-05-25', 21, 'Calle Rocafuerte y la 2da', '0996959801', 'carlos.gonzalez@gmail.com', '1er nivel', 7.8, 1) ,
	(68, 'Maria Fernanda', 'Castro Ortega', '1730687328', '2010-06-28', 12, 'Calle Esmeraldas y la 5ta', '0915781299', 'maria.castro@gmail.com', '2do nivel', 9.3, 2) ,
	(69, 'Andres Eduardo', 'Mendez Castro', '1233124582', '2002-04-18', 21, 'Calle Sucre y la 5ta', '0954139738', 'andres.mendez@gmail.com', '2do nivel', 8.5, 2) ,
	(70, 'Esteban Gabriel', 'Vargas Cedeño', '0733846255', '2008-03-30', 15, 'Calle Bolivar y la 8va', '0922829192', 'esteban.vargas@gmail.com', '2do nivel', 9.0, 1) ,
	(71, 'Karla Lisbeth', 'Lara Perez', '0507913246', '2002-10-17', 21, 'Calle Rocafuerte y la 10ma', '0968052129', 'karla.lara@gmail.com', '1er nivel', 8.0, 5) ,
	(72, 'Miguel Angel', 'Gomez Zambrano', '1134897164', '2012-01-17', 12, 'Calle Amazonas y la 5ta', '0954448260', 'miguel.gomez@gmail.com', '2do nivel', 9.2, 2) ,
	(73, 'Johana Elizabeth', 'Zambrano Paredes', '1131802646', '2008-03-19', 20, 'Calle Esmeraldas y la 10ma', '0978520095', 'johana.zambrano@gmail.com', '2do nivel', 8.8, 2) ,
	(74, 'Marcelo Jose', 'Lopez Valencia', '1512597437', '2012-11-22', 15, 'Calle Sucre y la 4ta', '0995165448', 'marcelo.lopez@gmail.com', '1er nivel', 8.2, 5) ,
	(75, 'Martha Lucia', 'Molina Jara', '0933490728', '2008-05-28', 20, 'Calle Juan Montalvo y la 5ta', '0963464252', 'marthamolina@gmail.com', '3er nivel', 8.75, 4) ,
	(76, 'Andrés Eduardo', 'Vargas Ayala', '1429657482', '2012-02-06', 15, 'Avenida Napo y la 24', '0965105889', 'andresvargas@gmail.com', '2do nivel', 9.0, 5) ,
	(77, 'Juan Fernando', 'Fernandez Paredes', '0450867128', '2008-09-26', 15, 'Calle Bolívar y la 7ma', '0915939761', 'juanfernandez@gmail.com', '3er nivel', 9.2, 4) ,
	(78, 'Luis Alberto', 'Zambrano Flores', '0509012364', '2010-08-08', 12, 'Calle Rocafuerte y la 5ta', '0927799828', 'luiszambrano@gmail.com', '2do nivel', 8.5, 4) ,
	(79, 'Roberto José', 'Pazmiño Bravo', '0202983064', '2010-06-28', 12, 'Calle Chimborazo y la 7ma', '0996931829', 'robertopazmino@gmail.com', '3er nivel', 9.8, 4) ,
	(80, 'Erika Estefanía', 'Chicaiza Romero', '0152908646', '2008-06-20', 15, 'Avenida La Prensa y la 24', '0980959042', 'erikachicaiza@gmail.com', '2do nivel', 8.0, 5) ,
	(81, 'Fernando José', 'Sanchez Ortiz', '1001056891', '2008-09-23', 15, 'Calle Esmeraldas y la 5ta', '0959886719', 'fernandosanchez@gmail.com', '3er nivel', 9.5, 5) ,
	(82, 'Rosa Maria', 'Vera Barreiro', '0621643828', '2010-04-16', 12, 'Calle Rocafuerte y la 7ma', '0935581356', 'rosavera@gmail.com', '2do nivel', 8.75, 5) ,
	(83, 'Diego Fernando', 'Molina Mendoza', '1000874164', '2008-09-10', 15, 'Calle Juan Montalvo y la 5ta', '0973867494', 'diegomolina@gmail.com', '3er nivel', 9.2, 5) ,
	(84, 'Mauricio Javier', 'García Vargas', '2218124500', '2010-10-12', 12, 'Calle Bolívar y la 7ma', '0914348727', 'mauriciogarcia@gmail.com', '2do nivel', 9.0, 1) ,
	(85, 'David Alejandro', 'Paredes Velez', '0946473019', '2002-10-23', 21, 'Calle Maldonado y la 7ma', '0923099444', 'davidparedes@gmail.com', '1er nivel', 8.75, 4) ,
	(86, 'María Fernanda', 'Vélez Reyes', '0722158373', '2003-02-10', 20, 'Calle Gran Colombia y la 5ta', '0950923293', 'mariavelez@gmail.com', '2do nivel', 9.0, 1) ,
	(87, 'Paola Belen', 'Sandoval Zambrano', '1749845600', '2010-09-12', 12, 'Calle Sucre y la 3ra', '0978704862', 'paolasandoval@gmail.com', '3er nivel', 9.5, 2) ,
	(88, 'Gabriela Maria', 'Rojas Valencia', '1123672591', '2002-08-22', 21, 'Calle Flores y la 6ta', '0956828546', 'gabrielarojas@gmail.com', '1er nivel', 8.25, 2) ,
	(89, 'Juan José', 'Mora Jimenez', '1352856173', '2002-07-19', 21, 'Calle Ecuador y la 4ta', '0928445524', 'juanjmora@gmail.com', '2do nivel', 9.2, 1) ,
	(90, 'Cristina Elizabeth', 'Pazmiño Pineda', '2443956428', '2010-10-21', 12, 'Calle Rocafuerte y la 3ra', '0930328619', 'cristinapazmino@gmail.com', '1er nivel', 8.9, 2) ,
	(91, 'Andres Felipe', 'Guerrero Lema', '0424719055', '2003-03-05', 20, 'Calle Alemán y la 6ta', '0945343515', 'andresguerrero@gmail.com', '3er nivel', 9.7, 1) ,
	(92, 'Luis Miguel', 'Velasco Guerra', '0455940319', '2002-08-09', 21, 'Calle Venezuela y la 4ta', '0979560606', 'luismvelasco@gmail.com', '2do nivel', 8.75, 2) ,
	(93, 'Daniela Andrea', 'García Rios', '1455892746', '2010-05-02', 12, 'Calle Quito y la 7ma', '0954697062', 'danielagarcia@gmail.com', '1er nivel', 9.5, 2) ,
	(94, 'Julio Cesar', 'Bastidas Palacios', '0730379155', '2010-03-12', 12, 'Calle Colombia y la 2da', '0941246985', 'juliobastidas@gmail.com', '3er nivel', 9.2, 5);

#---------------------------------------------------------------------- ASISTENCIA






#---------------------------------------------------------------------- 
INSERT INTO CriterioEvaluacion (descripcion_criterio) VALUES 
    ('Al inicio del curso, explica con claridad las políticas, contenidos y objetivos del aprendizaje del curso.'),
    ('Resume las ideas fundamentales discutidas, antes de pasar a una nueva unidad o tema.'),
	('Tiene predisposición para absolver las dudas de los estudiantes dentro y fuera del horario de clase.'),
    ('Desarrolla el contenido de la materia de forma ordenada y comprensible.'),
	('Cumple con todos los temas y contenidos presentados en el programa al inicio del curso.'),
    ('Estimula la participación activa del estudiante en clase y motiva la investigación bibliográfica.'),
	('Desarrolla actividades que fomentan el aprendizaje autónomo y colaborativo de los estudiantes.'),
	('Explica claramente los criterios que utiliza para la evaluación del aprendizaje.'),
	('Asiste con puntualidad a las actividades académicas.'),
	('Promueve las relaciones de cordialidad y respeto con y entre los estudiantes.');




#---------------------------------------------------------------------- EVALUACION DOCENTE



#---------------------------------------------------------------------- ITEM EVALUACION DOCENTE



#---------------------------------------------------------------------- MATRICULA



#---------------------------------------------------------------------- ITEM MATRICULA



#---------------------------------------------------------------------- ORDEN PAGO MATRICULA



#---------------------------------------------------------------------- ACTIVIDAD



#---------------------------------------------------------------------- ENTREGA



#---------------------------------------------------------------------- ACTA



#---------------------------------------------------------------------- ITEM ACTA





