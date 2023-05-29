import xlsxwriter

def crearArchivoPlantilla(Archivo='ReporteTemplate.xlsx',AE="AE4", CD="CD1", I="I1", Titulo="Titulo actividad", Materia="xxxxxxx", ClvMateria="xxxxxxx", NombreProf="xxxxxxx", NoEmpleado="xxxxxxx"):
    # Archivo = 'ReporteTemplate.xlsx'
    # AE = "AE4" # Atributo de egreso
    # CD = "CD1" # Criterio D
    # I = "I1"   # ?????
    # Titulo = "Titulo actividad" # Nombre de la actividad
    # Materia = "xxxxxxx"     # Nombre de la materia
    # ClvMateria = "xxxxxxx"  # Clave de la materia
    # NombreProf = "xxxxxxx"  # Nombre del profesor
    # NoEmpleado = "xxxxxxx"  # Numero de empleado

    listaAlumnos = []
    for i in range(0,15):
        listaAlumnos.append('')

    workbook = xlsxwriter.Workbook(Archivo)
    worksheet = workbook.add_worksheet()

    worksheet.set_row(0, 117.75)
    for i in range(1,5):
        worksheet.set_row(i, 13.5)
    worksheet.set_row(5, 15.75)

    worksheet.set_column('A:A', 2.71)
    worksheet.set_column('B:B', 4.14)
    worksheet.set_column('C:C', 35.71)
    worksheet.set_column('D:E', 8.5)
    worksheet.set_column('F:F', 10)
    worksheet.set_column('G:H', 60)

    formato_verde = workbook.add_format({
        'border_color': '#008000',
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'font_name': 'Arial',
        'font_color': '#008000',
        'font_size': 8,
        'text_wrap': True
    })

    formato_verde_S = workbook.add_format({
        'border_color': '#008000',
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'font_name': 'Arial',
        'font_color': '#008000',
        'font_size': 5,
        'text_wrap': True
    })

    formato_titulo = workbook.add_format({
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'bg_color': '#FFFF00',
        'font_name': 'Calibri',
        'font_size': 10,
        'text_wrap': True
    })

    formato_texto = workbook.add_format({
        'border_color': '#008000',
        'border': 1,
        'align': 'left',
        'valign': 'vcenter',
        'font_name': 'Arial',
        'font_size': 8,
        'text_wrap': True
    })

    formato_textoC = workbook.add_format({
        'border_color': '#008000',
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'font_name': 'Arial',
        'font_size': 8,
        'text_wrap': True
    })

    worksheet.write('B1', AE, formato_titulo)
    worksheet.write('C1', CD, formato_titulo)
    worksheet.write('D1',None, formato_titulo)
    worksheet.write('E1', I, formato_titulo)
    worksheet.write('F1',None, formato_titulo)
    worksheet.write('G1', Titulo, formato_titulo)
    worksheet.write('H1', "Rubrica", formato_titulo)

    worksheet.write('B2',None, formato_verde)
    worksheet.write('C2', 'MATERIA', formato_verde)
    worksheet.write('D2', "CLAVE DE LA MATERIA", formato_verde_S)

    worksheet.write('B3',None, formato_verde)
    worksheet.write('C3', Materia, formato_texto)
    worksheet.write('D3', ClvMateria, formato_textoC)

    worksheet.write('B4',None, formato_verde)
    worksheet.write('C4', "NOMBRE DEL PROFESOR", formato_verde)
    worksheet.write('D4', "NO. EMPLEADO", formato_verde_S)

    worksheet.write('B5',None, formato_verde)
    worksheet.write('C5', NombreProf, formato_texto)
    worksheet.write('D5', NoEmpleado, formato_textoC)

    worksheet.write('B6',None, formato_verde)
    worksheet.write('C6', "NOMBRE DEL ALUMNO", formato_verde)
    worksheet.write('D6', "MATRICULA", formato_verde)
    worksheet.write('E6', "Calificacion", formato_verde)
    worksheet.write('F6', None, formato_verde)
    worksheet.write('G6', "Entregable")
    worksheet.write('H6', "Evaluacion")
                    
    i = 0
    for alumno in listaAlumnos:
        worksheet.set_row(i+6, 12)
        worksheet.write(i+6, 1, None, formato_texto)
        worksheet.write(i+6, 2, None, formato_texto)
        worksheet.write(i+6, 3, None, formato_texto)
        worksheet.write(i+6, 4, None, formato_texto)
        worksheet.write(i+6, 5, None, formato_texto)
        i+=1

    workbook.close()