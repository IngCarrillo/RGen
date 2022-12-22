from docxtpl import DocxTemplate
from tkinter import filedialog
from datetime import datetime
from docx2pdf import convert
from tkinter import *
from tkinter import messagebox
import pandas as pd
import sys

def openCSV():
    path = filedialog.askopenfilename()
    df = pd.read_csv(path)
    return df

def addInfo(table):
    try:
        df = openCSV()
    except:
        messagebox.showerror(message='Asegurate que el archivo sea un CSV', title='Error al abrir el archivo')
    else:
        try:
            for index in range(df.shape[0]):
                table.insert('',END,text='{0}'.format(len(table.get_children())),values=(
                    '{0}'.format(df.iloc[index].iloc[0]),
                    '{0}'.format(df.iloc[index].iloc[1]),
                    '{0}'.format(df.iloc[index].iloc[2]),
                    '{0}'.format(df.iloc[index].iloc[3]),
                    '{0}'.format(df.iloc[index].iloc[4]),
                    '{0}'.format(df.iloc[index].iloc[5]),
                    '{0}'.format(df.iloc[index].iloc[6]),
                    '{0}'.format(df.iloc[index].iloc[7]),
                    '{0}'.format(df.iloc[index].iloc[8]),
                    '{0}'.format(df.iloc[index].iloc[9]),
                    '{0}'.format(df.iloc[index].iloc[10]),
                    '{0}'.format(df.iloc[index].iloc[11]),
                    '{0}'.format(df.iloc[index].iloc[12]),
                    '{0}'.format(df.iloc[index].iloc[13]),
                    '{0}'.format(df.iloc[index].iloc[14]),
                    '{0}'.format(df.iloc[index].iloc[15]),
                    '{0}'.format(df.iloc[index].iloc[16]),
                    '{0}'.format(df.iloc[index].iloc[17]),
                    '{0}'.format(df.iloc[index].iloc[18]),
                    '{0}'.format(df.iloc[index].iloc[19]),
                    '{0}'.format(df.iloc[index].iloc[20]),
                    '{0}'.format(df.iloc[index].iloc[21]),
                    '{0}'.format(df.iloc[index].iloc[22]),
                    '{0}'.format(df.iloc[index].iloc[23]),
                    '{0}'.format(df.iloc[index].iloc[24]),
                    '{0}'.format(df.iloc[index].iloc[25])
                ))
        except:
            messagebox.showerror(message='Asegurate de que el archivo haya sido llenado correctamente', title='Error al llenar la tabla')

def addInterface(table):
    try:
        df = openCSV()
    except:
        messagebox.showerror(message='Asegurate que el archivo sea un CSV', title='Error al abrir el archivo')
    else:
        try:
            for index in range(df.shape[0]):
                if(df.iloc[index][3] != 'void'):
                    table.insert('',END,text='{0}'.format(df.iloc[index].iloc[0]),values=(
                        '{0}'.format(df.iloc[index].iloc[1]),
                        '{0}'.format(df.iloc[index].iloc[2]),
                        '{0}'.format(df.iloc[index].iloc[3]),
                        '{0}'.format(df.iloc[index].iloc[4])
                    ))
                else:
                    table.insert('',END,text='{0}'.format(df.iloc[index].iloc[0]),values=(
                        '{0}'.format(df.iloc[index].iloc[1]),
                        '{0}'.format(df.iloc[index].iloc[2]),
                        '',
                        '{0}'.format(df.iloc[index].iloc[4])
                    ))
        except:
            messagebox.showerror(message='Asegurate de que el archivo haya sido llenado correctamente', title='Error al llenar la tabla')

def addFig(table):
    try:
        df = openCSV()
    except:
        messagebox.showerror(message='Asegurate que el archivo sea un CSV', title='Error al abrir el archivo')
    else:
        try:
            for index in range(df.shape[0]):
                table.insert('',END,text='{0}'.format(df.iloc[index].iloc[0]),values=(
                    '{0}'.format(df.iloc[index].iloc[1]),
                    '{0}'.format(df.iloc[index].iloc[2])
                ))
        except:
            messagebox.showerror(message='Asegurate de que el archivo haya sido llenado correctamente', title='Error al llenar la tabla')

def selTempPath(product):
    if(product == 'CHV'):
        return './Templates/Templates CHV'
    elif(product == 'CTV'):
        return './Templates/Templates CTV'
    elif(product == 'SIV'):
        return './Templates/Templates SIV'
    elif(product == 'CHV-CTV'):
        return './Templates/Templates CHV-CTV'
    elif(product == 'CTV-SIV'):
        return './Templates/Templates CTV-SIV'
    elif(product == 'CHV-CTV-SIV'):
        return './Templates/Templates CHV-CTV-SIV'

def genDocs(tableR,tableI,tableF):

    # Arreglo para los documentos
    docs = []
    # Directorio base
    #path = os.path.dirname(__file__)
    # Recorrido de la tabla de reportes
    for item in tableR.get_children():
        id = tableR.item(item)['text']
        values = tableR.item(item)['values']
        # SE GUARDA LA INFORMACIÓN A REEMPLAZAR
        # Nombre del componente
        CompName = values[1]
        # Nombre del verificador
        verifName = values[22]
        # Nombre DES/IMP_TST/INT
        DITIname = values[2]
        # Fecha
        date = '{0}/{1}/{2}'.format(datetime.now().day,datetime.now().month,datetime.now().year)
        # HASH
        HASH = values[4]
        # Componente
        comp = 'Componente {0}'.format(str(CompName).split('_')[-1])
        # Comentario buffer
        if(values[6] != ''):
            comBuffer = 'Dada la información mostrada en el documento SDS_{0} las interfaces contienen búferes de memoria, "{1}", los cuales muestran los mecanismos "{2}" para detectar que la memoria no puede ser asignada.'.format(values[1],values[6],values[5])
        else:
            comBuffer = 'Dada la información mostrada en el documento SDS_{0} las interfaces no contienen búferes (variables globales, memoria protegida, memoria protegida compartida o que necesite política de acceso).'.format(values[0])
        # Comentario Hardware/Software
        if(values[16] == 1):
            comHS = 'El documento define la relación que tiene el componente con su entorno (Hardware) y con software; (Ver sección "Interfaces") y cumple con las restricciones de software/hardware.'
        else:
            comHS = 'El componente no tiene relación íntima con el hardware (ya que usa otros componentes que realizan esa tarea), y cumple con las restricciones de software indicadas en la arquitectura a su vez no rompe con las reglas de codificación (ver documento "Reglas de Codificación").'
        # SIL
        SIL = 'SIL {0}'.format(values[7])
        # Comentario de tipos exportados
        if(values[17] == 1):
            comExpT = 'El componente "{0}" expone las estructuras de datos en la tabla "Tipos exportados" del documento SDS_{0}.'.format(CompName)
        else:
            comExpT = 'El componente "{0}" no expone estructuras de datos, ya que la tabla "Tipos exportados" del documento SDS_{0}, está vacía y dado la intención del componente no es necesario exponer alguna estructura.'.format(CompName)
        # Tareas cíclicas
        if(values[18] == '1'):
            CTasks = ''
        else:
            CTasks = 'no'
        # Comentario requisitos
        ComReq = 'Todos los requisitos son trazados.'
        # Complejidad ciclomatica
        ConI = 0
        ConJ = 0
        CompArcC = []
        Sum = ''
        Data = ''
        for fig in tableF.get_children():
            figVal = tableF.item(fig)['values']
            if(tableF.item(fig)['text'] == id):
                ConI += 1
                CompArcC.append('Figura {0}\n({1}) = {2}\n'.format(ConI,figVal[0],figVal[1]))
                Sum += ' {0} + '.format(figVal[1])
                ConJ += int(figVal[1])
                tableF.delete(fig)
        ConJ -= (ConI+1)
        Data = 'La complejidad ciclomática es de {0}. Esto es menor al límite establecido en "Acuerdos documentación de diseño de software de seguridad". http://modutram-server/wikitram/index.php/Acuerdos_documentaci%C3%B3n_de_dise%C3%B1o_de_software_de_seguridad\n'.format(ConJ)
        Sum = '1 + ({0}) - 2 = {1}'.format(Sum,ConJ)
        # Hash codigo
        HashC = values[24]
        # Nombre del archivo de código fuente
        scFile = values[19]
        # Nombre implementador
        impName = values[21]
        # Nomnbre encargado de ensayos
        tstName = values[20]
        # Requisitos cumplidos
        req = values[12]
        # Porcentaje de efectividad
        effectP = values[10]
        # Porcentaje multicondición
        multiP = values[11]
        # El componente pertenece a datos/algoritmos de aplicación
        if(values[8] == 1):
            cAlgAp = ''
        else:
            cAlgAp = 'El componente "{0}" no es desarrollado para soportar la ejecución de los datos/algoritmos de aplicación.'.format(CompName)
        # Comentario de SIL
        if(values[7] != 0):
            comSIL = 'Por lo que se tratará el componente con el nivel de integridad de seguridad del componente más alto con el que tiene relación, según la sección "Contextos de los procesos y segregación de contextos" del documento SAS_Global.docx.'
        else:
            comSIL = 'Se dispondrán de las evidencias de la sección "Contextos de los procesos y segregación de contextos" del documento SAS_Global.docx donde se describe la independencia entre los componentes, analizando el nivel de integridad de seguridad independientemente entre los componentes.'
        # Arreglos para interfaces (con parámetros y sin parámetros)
        interfaces = []
        interfaces2 = []

        if(values[0] == 'SDS'):

            templatePath = '{0}/In-Sw-003c F SDS_vtbd - VerNametbd.docx'.format(selTempPath(values[-1]))

            template = DocxTemplate(templatePath)

            # Interfaces
            for inter in tableI.get_children():
                interVal = tableI.item(inter)['values']
                if(tableI.item(inter)['text'] == id):
                    if(len(interVal[2]) > 0):
                        interface = {
                            'comOverL': 'Para la interfaz {0} se describe en la figura {1} el comportamiento cuando valor se encuentra en el límite en las siguientes variables: {2}'.format(interVal[0], interVal[1], interVal[2]),
                            'comLimit': 'Para la interfaz {0} se describe en la figura {1} el comportamiento cuando se sobre para su valor límite en las siguientes variables: {2}'.format(interVal[0], interVal[1], interVal[2])
                        }
                        interfaces.insert(0,interface)
                    else:
                        interface = {
                            'comOverL': 'Para la interfaz {0} se describe en la figura {1} que no tiene parámetros de entrada que identifiquen valores límite'.format(interVal[0],interVal[1]),
                            'comLimit': 'Para la interfaz {0} se describe en la figura {1} que no tiene parámetros de entrada que identifiquen valores límite.'.format(interVal[0],interVal[1])
                        }
                        interfaces.append(interface)

                    tableI.delete(inter)

            context = {
                'AAAA': verifName,
                'BBBB': CompName,
                'FFFF': HASH,
                'DATE': date,
                'CHwSw': comHS,
                'CCCC': DITIname,
                'OOOO': SIL,
                'CExpT': comExpT,
                'EEEE': comp,
                'interfaces': interfaces,
                'CBUFFER': comBuffer
            }
            
            tableR.delete(item)

            template.render(context)
            docName = './Reports/WORD/In-Sw-003c F SDS_{0} - {1} - {2}.docx'.format(CompName,HASH,values[23])
            docs.append(docName)

            template.save(docName)
        elif(values[0] == 'SAS'):
            
            templatePath = '{0}/In-Sw-003a F SAS_vtbd_vtbd.docx'.format(selTempPath(values[-1]))

            template = DocxTemplate(templatePath)

            context = {
                'AAAA': verifName,
                'BBBB': CompName,
                'FFFF': HASH,
                'DATE': date,
                'EEEE': comp,
                'CCCC': DITIname,
                'OOOO': SIL,
                'CSIL': comSIL,
                'XXXX': cAlgAp
            }
            
            tableR.delete(item)

            template.render(context)
            docName = './Reports/WORD/In-Sw-003a F SAS_{0} - {1} - {2}.docx'.format(CompName,HASH,values[23])
            docs.append(docName)

            template.save(docName)

        elif(values[0] == 'SIS'):

            templatePath = '{0}/In-Sw-003b F SIS_vtbd - VerNametbd.docx'.format(selTempPath(values[-1]))

            template = DocxTemplate(templatePath)

            # Interfaces con y sin parametros
            for inter in tableI.get_children():
                if(tableI.item(inter)['text'] == id):
                    interVal = tableI.item(inter)['values']
                    if(len(interVal[2]) > 0):
                        interface = ',{0}'.format(interVal[0])
                        interfaces.append(interface)
                    else:
                        interface = ',{0}'.format(interVal[0])
                        interfaces2.append(interface)
                    tableI.delete(inter)

            # Contexto para reemplazar en plantilla
            context = {
                'AAAA': verifName,
                'BBBB': CompName,
                'FFFF': HASH,
                'DATE': date,
                'EEEE': comp,
                'CCCC': DITIname,
                'interfaces': interfaces,
                'interfaces2': interfaces2,
                'YYYY': CTasks
            }

            tableR.delete(item)

            template.render(context)
            docName = './Reports/WORD/In-Sw-003b F SIS_{0} - {1} - {2}.docx'.format(CompName,HASH,values[23])
            docs.append(docName)

            template.save('{0}'.format(docName))
        
        elif(values[0] == 'SCDS'):

            templatePath = '{0}/In-Sw-004a F SCDS_vtbd - VerNametbd.docx'.format(selTempPath(values[-1]))

            template = DocxTemplate(templatePath)

            # Interfaces con y sin parametros
            for inter in tableI.get_children():
                if(tableI.item(inter)['text'] == id):
                    interVal = tableI.item(inter)['values']
                    if(len(interVal[2]) > 0):
                        interface = ',{0}'.format(interVal[0])
                        interfaces.append(interface)
                    else:
                        interface = ',{0}'.format(interVal[0])
                        interfaces2.append(interface)
                    tableI.delete(inter)

            context = {
                'AAAA': verifName,
                'BBBB': CompName,
                'FFFF': HASH,
                'DATE': date,
                'EEEE': comp,
                'CCCC': DITIname,
                'OOOO': SIL,
                'CompArc': CompArcC,
                'SUM': Sum,
                'CComple': Data,
                'interfaces': interfaces,
                'interfaces2': interfaces2,
                'ReqNoTraza': ComReq
            }

            tableR.delete(item)

            template.render(context)
            docName = './Reports/WORD/In-Sw-004a F SCDS_{0} - {1} - {2}.docx'.format(CompName,HASH,values[23])
            docs.append(docName)

            template.save('{0}'.format(docName))
        
        elif(values[0] == 'HSITS'):
            
            templatePath = '{0}/In-Sw-003d F HSITS_vtbd - VerNametbd.docx'.format(selTempPath(values[-1]))

            template = DocxTemplate(templatePath)

            context = {
                'AAAA': verifName,
                'BBBB': CompName,
                'FFFF': HASH,
                'DATE': date,
                'EEEE': comp,
                'CCCC': DITIname
            }

            tableR.delete(item)
            
            template.render(context)
            docName = './Reports/WORD/In-Sw-003d F HSITS_{0} - {1} - {2}.docx'.format(CompName,HASH,values[23])
            docs.append(docName)

            template.save('{0}'.format(docName))
        
        elif(values[0] == 'SITS'):

            templatePath = '{0}/In-Sw-003d F SITS_vtbd - VerNametbd.docx'.format(selTempPath(values[-1]))

            template = DocxTemplate(templatePath)

            # Componentes con los que tiene relación
            if(len(values[3]) == 0):
                compRel = 'NA'
            else:
                compRel = '{0}'.format(values[3])

            context = {
                'AAAA': verifName,
                'BBBB': CompName,
                'FFFF': HASH,
                'DATE': date,
                'EEEE': comp,
                'DDDD': compRel,
                'CCCC': DITIname
            }

            tableR.delete(item)
            
            template.render(context)
            docName = './Reports/WORD/In-Sw-003d F SITS_{0} - {1} - {2}.docx'.format(CompName,HASH,values[23])
            docs.append(docName)

            template.save('{0}'.format(docName))

        elif(values[0] == 'SCTS'):

            templatePath = '{0}/In-Sw-004b F SCTS_vtbd - VerNametbd.docx'.format(selTempPath(values[-1]))

            template = DocxTemplate(templatePath)

            # Comentario requisitos
            ComReq = 'Todos los requisitos son trazados.'

            context = {
                'AAAA': verifName,
                'BBBB': CompName,
                'FFFF': HASH,
                'DATE': date,
                'EEEE': comp,
                'UUUU': values[13],
                'VVVV': values[14],
                'QQQQ': values[9],
                'ReqNoTraza': ComReq,
                'CCCC': DITIname
            }

            tableR.delete(item)
            
            template.render(context)
            docName = './Reports/WORD/In-Sw-004b F SCTS_{0} - {1} - {2}.docx'.format(CompName,HASH,values[23])
            docs.append(docName)

            template.save('{0}'.format(docName))

        elif(values[0] == 'SCTR'):

            templatePath = '{0}/In-Sw-005 F SCTR_vtbd - VerNametbd.docx'.format(selTempPath(values[-1]))

            template = DocxTemplate(templatePath)

            Data = 'Para .c\n{0}\nPara archivos cabecera .h\n\n       .h = 2\n_def.h = 2\n_cfg.h = 2\n\n1 + ( {1} + 2 + 2 + 2 ) - 4 = {2}\n'.format(Data,ConJ,(ConJ+3))

            context = {
                'AAAA': verifName,
                'BBBB': CompName,
                'FFFF': HASH,
                'DATE': date,
                'EEEE': comp,
                'NNNN': HashC,
                'PPPP': scFile,
                'CCIMP': impName,
                'CComple': Data,
                'CCTST': tstName,
                'TTTT': req,
                'RRRR': effectP,
                'SSSS': multiP,
                'ReqNoTraza': ComReq
            }
            
            tableR.delete(item)
            
            template.render(context)
            docName = './Reports/WORD/In-Sw-005 F SCTR_{0} - {1} - {2}.docx'.format(CompName,HASH,values[23])
            docs.append(docName)

            template.save('{0}'.format(docName))

        elif(values[0] == 'SITR'):

            templatePath = '{0}/In-Sw-007a F SITR_vtbd - VerNametbd.docx'.format(selTempPath(values[-1]))

            template = DocxTemplate(templatePath)

            context = {
                'AAAA': verifName,
                'BBBB': CompName,
                'FFFF': HASH,
                'DATE': date,
                'EEEE': comp,
                'CCCC': DITIname,
                'ReqNoTraza': ComReq
            }
            
            tableR.delete(item)
            
            template.render(context)
            docName = './Reports/WORD/In-Sw-007a F SITR_{0} - {1} - {2}.docx'.format(CompName,HASH,values[23])
            docs.append(docName)

            template.save('{0}'.format(docName))

        elif(values[0] == 'HSITR'):

            templatePath = '{0}/In-Sw-007b F HSITR_vtbd - VerNametbd.docx'.format(selTempPath(values[-1]))

            template = DocxTemplate(templatePath)

            context = {
                'AAAA': verifName,
                'BBBB': CompName,
                'FFFF': HASH,
                'DATE': date,
                'EEEE': comp,
                'CCCC': DITIname,
                'ReqNoTraza': ComReq
            }
            
            tableR.delete(item)
            
            template.render(context)
            docName = './Reports/WORD/In-Sw-007b F HSITR_{0} - {1} - {2}.docx'.format(CompName,HASH,values[23])
            docs.append(docName)

            template.save('{0}'.format(docName))

    for doc in docs:

        sys.stderr = open('consoleoutput.log','w')

        convert('{0}'.format(doc),'./Reports/PDF/{0}.pdf'.format(doc.split('/')[-1].split('.')[0]))