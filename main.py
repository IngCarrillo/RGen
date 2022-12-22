from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import file_management as fm
import pandas as pd
import os

root = Tk()
root.config(width=1900, height=700, bg='black')
root.title('Modutram')
root.geometry('%dx%d'%(root.winfo_screenwidth(),root.winfo_screenheight()))

# Funcion para habilitar todas las entradas
def enableAll():
    NameComp.config(state='normal')
    Name_DESIMP_TSTINT.config(state='normal')
    HASH.config(state='normal')
    ComponentsRel.config(state='normal')
    ErrorDetect.config(state='normal')
    BufferComp.config(state='normal')
    SIL.config(state='normal')
    Interfaces.config(state='normal')
    EstructureTest.config(state='normal')
    EffectP.config(state='normal')
    Req.config(state='normal')
    BlackBox.config(state='normal')
    PrivateInt.config(state='normal')
    Minutas.config(state='normal')
    HSRel.config(state='normal')
    ExpTypes.config(state='normal')
    CTasks.config(state='normal')
    SCodeFile.config(state='normal')
    TestName.config(state='normal')
    Implementer.config(state='normal')
    Verifier.config(state='normal')
    VerifierIni.config(state='normal')
    HASHCode.config(state='normal')
    Product.config(state='normal')
    #Interfaces
    interName.config(state='normal')
    figName.config(state='normal')
    interP.config(state='normal')
    aplicAlg.config(state='normal')
    btnAddInter.config(state='normal')
    btnEditInter.config(state='normal')
    btnSaveInter.config(state='normal')
    btnDelInter.config(state='normal')
    btnCleanInter.config(state='normal')
    #Figuras
    FigInt.config(state='normal')
    CComplex.config(state='normal')
    CComplex.config(state='readonly')
    btnAddFig.config(state='normal')
    btnEditFig.config(state='normal')
    btnSaveFig.config(state='normal')
    btnDelFig.config(state='normal')
    btnCleanFig.config(state='normal')


# Funcion para desabilitar todas las entradas
def disableAll():
    NameComp.config(state='disabled')
    Name_DESIMP_TSTINT.config(state='disabled')
    HASH.config(state='disabled')
    ComponentsRel.config(state='disabled')
    ErrorDetect.config(state='disabled')
    BufferComp.config(state='disabled')
    SIL.config(state='disabled')
    Interfaces.config(state='disabled')
    EstructureTest.config(state='disabled')
    EffectP.config(state='disabled')
    MultiP.config(state='disabled')
    Req.config(state='disabled')
    BlackBox.config(state='disabled')
    PrivateInt.config(state='disabled')
    Minutas.config(state='disabled')
    HSRel.config(state='disabled')
    ExpTypes.config(state='disabled')
    CTasks.config(state='disabled')
    SCodeFile.config(state='disabled')
    TestName.config(state='disabled')
    Implementer.config(state='disabled')
    Verifier.config(state='disabled')
    VerifierIni.config(state='disabled')
    HASHCode.config(state='disabled')
    Product.config(state='disabled')
    #Interfaces
    interName.config(state='disabled')
    figName.config(state='disabled')
    interP.config(state='disabled')
    aplicAlg.config(state='disabled')
    btnAddInter.config(state='disabled')
    btnEditInter.config(state='disabled')
    btnSaveInter.config(state='disabled')
    btnDelInter.config(state='disabled')
    btnCleanInter.config(state='disabled')
    #Figuras
    FigInt.config(state='disabled')
    CComplex.config(state='disabled')
    btnAddFig.config(state='disabled')
    btnEditFig.config(state='disabled')
    btnSaveFig.config(state='disabled')
    btnDelFig.config(state='disabled')
    btnCleanFig.config(state='disabled')

# Borrado del formulario
def deleteAll():
    ComponentsRel.delete('1.0',END)
    ErrorDetect.delete('1.0',END)
    BufferComp.delete('1.0',END)
    Req.delete('1.0',END)
    fase.delete(0,END)
    NameComp.delete(0,END)
    Name_DESIMP_TSTINT.delete(0,END)
    HASH.delete(0,END)
    SIL.delete(0,END)
    Interfaces.deselect()
    EstructureTest.delete(0,END)
    EffectP.delete(0,END)
    MultiP.delete(0,END)
    BlackBox.delete(0,END)
    PrivateInt.delete(0,END)
    Minutas.deselect()
    HSRel.deselect()
    ExpTypes.deselect()
    CTasks.deselect()
    SCodeFile.delete(0,END)
    TestName.delete(0,END)
    Implementer.delete(0,END)
    Verifier.delete(0,END)
    VerifierIni.delete(0,END)
    HASHCode.delete(0,END)
    Product.delete(0,END)
    #Interfaces
    interName.delete(0,END)
    figName.delete(0,END)
    interP.delete(0,END)
    #Figuras
    FigInt.delete(0,END)
    CComplex.delete(0,END)

# Contenedor
container = ttk.Notebook(root)
container.pack(side='left', fill='both', expand='yes')
container.config(width=1800, height=700)
container.pack_propagate(False)

# Primer pestaña
formContainer = Canvas(container)
formContainer.config(bg='lightgray', width=1300, height=700)
formContainer.pack(side='left', fill='both', expand='yes')
formContainer.pack_propagate(False)

container.add(formContainer, text='Formulario')

# Frame del formulario
form = Frame(formContainer, width=1800, height=1500)
#form.pack(side='left', fill='both', expand='yes')
form.config(bg='lightgray')
form.pack_propagate(False)

formScroll = Scrollbar(container, orient='vertical', command=formContainer.yview)
formScroll.pack(side='right', fill='y')
formContainer.configure(yscrollcommand=formScroll.set)
formContainer.bind(
    "<Configure>", lambda e: 
        formContainer.configure(
            scrollregion=formContainer.bbox("all")
        )
    )

formContainer.create_window((0,0), window=form, anchor='nw')

# Filtro por fase
lblFase = Label(form, text='Etapa:', bg='lightgray')
lblFase.pack()
lblFase.place(x=120,y=20)

def faseFilter(event):
    disableAll()
    if(fase.get() == 'SAS'):
        NameComp.config(state='normal')
        Name_DESIMP_TSTINT.config(state='normal')
        HASH.config(state='normal')
        SIL.config(state='normal')
        Interfaces.config(state='normal')
        Minutas.config(state='normal')
        Verifier.config(state='normal')
        VerifierIni.config(state='normal')
        Product.config(state='normal')
        SIL.config(state='readonly')
        Product.config(state='readonly')
    elif(fase.get()=='SIS'):
        NameComp.config(state='normal')
        Name_DESIMP_TSTINT.config(state='normal')
        HASH.config(state='normal')
        Minutas.config(state='normal')
        CTasks.config(state='normal')
        Verifier.config(state='normal')
        VerifierIni.config(state='normal')
        Product.config(state='normal')
        Product.config(state='readonly')
        #Interfaces
        interName.config(state='normal')
        figName.config(state='normal')
        interP.config(state='normal')
        aplicAlg.config(state='normal')
        btnAddInter.config(state='normal')
        btnEditInter.config(state='normal')
        btnDelInter.config(state='normal')
        btnCleanInter.config(state='normal')
    elif(fase.get()=='SDS'):
        NameComp.config(state='normal')
        Name_DESIMP_TSTINT.config(state='normal')
        HASH.config(state='normal')
        SIL.config(state='normal')
        Minutas.config(state='normal')
        HSRel.config(state='normal')
        ErrorDetect.config(state='normal')
        ExpTypes.config(state='normal')
        Verifier.config(state='normal')
        VerifierIni.config(state='normal')
        Product.config(state='normal')
        SIL.config(state='readonly')
        Product.config(state='readonly')
        #Interfaces
        interName.config(state='normal')
        figName.config(state='normal')
        interP.config(state='normal')
        aplicAlg.config(state='normal')
        btnAddInter.config(state='normal')
        btnEditInter.config(state='normal')
        btnDelInter.config(state='normal')
        btnCleanInter.config(state='normal')
        #Figuras
        FigInt.config(state='normal')
        CComplex.config(state='normal')
        CComplex.config(state='readonly')
        btnAddFig.config(state='normal')
        btnEditFig.config(state='normal')
        btnDelFig.config(state='normal')
        btnCleanFig.config(state='normal')
    elif(fase.get()=='SCDS'):
        NameComp.config(state='normal')
        Name_DESIMP_TSTINT.config(state='normal')
        HASH.config(state='normal')
        SIL.config(state='normal')
        Minutas.config(state='normal')
        Verifier.config(state='normal')
        VerifierIni.config(state='normal')
        Product.config(state='normal')
        SIL.config(state='readonly')
        Product.config(state='readonly')
        #Interfaces
        interName.config(state='normal')
        figName.config(state='normal')
        interP.config(state='normal')
        aplicAlg.config(state='normal')
        btnAddInter.config(state='normal')
        btnEditInter.config(state='normal')
        btnDelInter.config(state='normal')
        btnCleanInter.config(state='normal')
        #Figuras
        FigInt.config(state='normal')
        CComplex.config(state='normal')
        CComplex.config(state='readonly')
        btnAddFig.config(state='normal')
        btnEditFig.config(state='normal')
        btnDelFig.config(state='normal')
        btnCleanFig.config(state='normal')
    elif(fase.get()=='SCTS'):
        NameComp.config(state='normal')
        Name_DESIMP_TSTINT.config(state='normal')
        HASH.config(state='normal')
        EstructureTest.config(state='normal')
        BlackBox.config(state='normal')
        PrivateInt.config(state='normal')
        Minutas.config(state='normal')
        Verifier.config(state='normal')
        VerifierIni.config(state='normal')
        Product.config(state='normal')
        BlackBox.config(state='readonly')
        PrivateInt.config(state='readonly')
        Product.config(state='readonly')
    elif(fase.get()=='SCTR'):
        NameComp.config(state='normal')
        HASH.config(state='normal')
        EffectP.config(state='normal')
        MultiP.config(state='normal')
        Req.config(state='normal')
        Minutas.config(state='normal')
        SCodeFile.config(state='normal')
        TestName.config(state='normal')
        Implementer.config(state='normal')
        Verifier.config(state='normal')
        VerifierIni.config(state='normal')
        HASHCode.config(state='normal')
        Product.config(state='normal')
        Product.config(state='readonly')
        #Figuras
        FigInt.config(state='normal')
        CComplex.config(state='normal')
        CComplex.config(state='readonly')
        btnAddFig.config(state='normal')
        btnEditFig.config(state='normal')
        btnDelFig.config(state='normal')
        btnCleanFig.config(state='normal')
    elif(fase.get()=='HSITS'):
        NameComp.config(state='normal')
        Name_DESIMP_TSTINT.config(state='normal')
        HASH.config(state='normal')
        Minutas.config(state='normal')
        Verifier.config(state='normal')
        VerifierIni.config(state='normal')
        Product.config(state='normal')
        Product.config(state='readonly')
    elif(fase.get()=='SITS'):
        NameComp.config(state='normal')
        Name_DESIMP_TSTINT.config(state='normal')
        ComponentsRel.config(state='normal')
        HASH.config(state='normal')
        Minutas.config(state='normal')
        Verifier.config(state='normal')
        VerifierIni.config(state='normal')
        Product.config(state='normal')
        Product.config(state='readonly')
    elif(fase.get()=='HSITR'):
        NameComp.config(state='normal')
        Name_DESIMP_TSTINT.config(state='normal')
        HASH.config(state='normal')
        Minutas.config(state='normal')
        Verifier.config(state='normal')
        VerifierIni.config(state='normal')
        Product.config(state='normal')
        Product.config(state='readonly')
    elif(fase.get()=='SITR'):
        NameComp.config(state='normal')
        Name_DESIMP_TSTINT.config(state='normal')
        HASH.config(state='normal')
        Minutas.config(state='normal')
        Verifier.config(state='normal')
        VerifierIni.config(state='normal')
        Product.config(state='normal')
        Product.config(state='readonly')
    else:
        disableAll()

faseVar = StringVar()
fase = ttk.Combobox(form, textvariable=faseVar, state='readonly')
fase.pack()
fase.place(x=120,y=50)
fase['values'] = ('SAS', 'SIS', 'SDS', 'SCDS', 'SSC', 'SCTS', 'SCTR', 'SITS', 'HSITS', 'SITR', 'HSITR')
# Proximamente
""" , 'SITS-HSITS', 'SITR-HSITR' """
fase.bind('<<ComboboxSelected>>', faseFilter)

# Nombre del componente
def caps(event):
    IdComp.set(IdComp.get().upper())

lblComp = Label(form, text='Nombre del componente: ', bg='lightgray')
lblComp.pack()
lblComp.place(x=276,y=20)

IdComp = StringVar()
NameComp = Entry(form, textvariable=IdComp)
NameComp.pack()
NameComp.config(width=30)
NameComp.place(x=276,y=50)
NameComp.bind('<KeyRelease>', caps)

# Nombre de alguien
lblDESIMP_TSTINT = Label(form, text='Nombre de DES/IMP o TST/INT:', bg='lightgray')
lblDESIMP_TSTINT.pack()
lblDESIMP_TSTINT.place(x=476,y=20)

NameDITI = StringVar()
Name_DESIMP_TSTINT = Entry(form, textvariable=NameDITI)
Name_DESIMP_TSTINT.pack()
Name_DESIMP_TSTINT.config(width=30)
Name_DESIMP_TSTINT.place(x=476,y=50)

# HASH
lblHASH = Label(form, text='HASH:', bg='lightgray')
lblHASH.pack()
lblHASH.place(x=676,y=20)

HASH_Var = StringVar()
HASH = Entry(form, textvariable=HASH_Var)
HASH.pack()
HASH.config(width=30)
HASH.place(x=676,y=50)

# Componentes con los que tiene relacion
lblComponents = Label(form, text='Componentes con los que tiene relacion:', bg='lightgray')
lblComponents.pack()
lblComponents.place(x=120,y=80)

ComponentsRel = Text(form)
ComponentsRel.pack()
ComponentsRel.config(width=40)
ComponentsRel.place(x=120,y=110, height=80)

# Mecanismos de deteccion de errores
lblErrorDetect = Label(form, text='Mecanismos de deteccion de errores:', bg='lightgray')
lblErrorDetect.pack()
lblErrorDetect.place(x=460,y=80)

ErrorDetect = Text(form)
ErrorDetect.pack()
ErrorDetect.config(width=40)
ErrorDetect.place(x=460,y=110, height=80)

# Buffer de componentes
lblBufferComp = Label(form, text='Buffers de componentes:', bg='lightgray')
lblBufferComp.pack()
lblBufferComp.place(x=800,y=80)

BufferComp = Text(form)
BufferComp.pack()
BufferComp.config(width=40)
BufferComp.place(x=800,y=110,height=80)

# SIL del componente
lblSIL = Label(form, text='SIL del componente:', bg='lightgray')
lblSIL.pack()
lblSIL.place(x=876,y=20)

SILVar = StringVar()
SIL = Spinbox(form, from_=0, to=4, textvariable=SILVar, state='readonly')
SIL.pack()
SIL.config(width=30)
SIL.place(x=876,y=50)

# Interfaces desarrolladas con datos/algoritmos de aplicación
InterVar = IntVar()
Interfaces = Checkbutton(form, text='Interfaces desarrolladas con datos/algoritmos de aplicación', variable=InterVar, bg='lightgray')
Interfaces.pack()
Interfaces.place(x=720,y=230)

# Numero de pruebas de estructura
lblEstructureTest = Label(form, text='Numero de pruebas de estructura:', bg='lightgray')
lblEstructureTest.pack()
lblEstructureTest.place(x=120,y=200)

EstTestVar = StringVar()
EstructureTest = Entry(form, textvariable=EstTestVar)
EstructureTest.pack()
EstructureTest.config(width=30)
EstructureTest.place(x=120,y=230)

# Porcentaje de efectividad
lblEffectP = Label(form, text='Porcentaje de efectividad:', bg='lightgray')
lblEffectP.pack()
lblEffectP.place(x=320,y=200)

EffectVar = StringVar()
EffectP = Entry(form, textvariable=EffectVar)
EffectP.pack()
EffectP.config(width=30)
EffectP.place(x=320,y=230)

# Porcentaje de multicondicion
lblMultiP = Label(form, text='Porcentaje de multicondicion:', bg='lightgray')
lblMultiP.pack()
lblMultiP.place(x=520,y=200)

MultiVar = StringVar()
MultiP = Entry(form, textvariable=MultiVar)
MultiP.pack()
MultiP.config(width=30)
MultiP.place(x=520,y=230)

# Requisitos cumplidos
lblReq = Label(form, text='Requisitos cumplidos:', bg='lightgray')
lblReq.pack()
lblReq.place(x=360,y=260)

Req = Text(form)
Req.pack()
Req.config()
Req.place(x=360,y=290,width=195,height=48)

# Número de pruebas de caja negra
lblBlackBox = Label(form, text='Numero de pruebas de caja negra:', bg='lightgray')
lblBlackBox.pack()
lblBlackBox.place(x=120,y=260)

BlackVar = StringVar()
BlackBox = Spinbox(form, from_=0, to=1000, textvariable=BlackVar, state='readonly')
BlackBox.pack()
BlackBox.config(width=34)
BlackBox.place(x=120,y=290)

# Numero de pruebas para interfaces privadas
lblPrivateInt = Label(form, text='Numero de pruebas para interfaces privadas:', bg='lightgray')
lblPrivateInt.pack()
lblPrivateInt.place(x=120,y=350)

PriVar = StringVar()
PrivateInt = Spinbox(form, from_=0, to=1000, textvariable=PriVar, width=38, state='readonly')
PrivateInt.pack()
PrivateInt.place(x=120,y=380)

# Minuta abierta por puntos de calidad
MinutasVar = IntVar()
Minutas = Checkbutton(form, text='Minuta abierta por puntos de calidad', variable=MinutasVar, bg='lightgray')
Minutas.pack()
Minutas.place(x=120,y=320)

# Relacion con hardware o software
HSRelVar = IntVar()
HSRel = Checkbutton(form, text='Relacion con hardware o software', variable=HSRelVar, bg='lightgray')
HSRel.pack()
HSRel.place(x=580,y=320)

# Tipos exportados
ExpTypesVar = IntVar()
ExpTypes = Checkbutton(form, text='Tipos exportados y/o macros de configuración', variable=ExpTypesVar, bg='lightgray')
ExpTypes.pack()
ExpTypes.place(x=580,y=260)

# Tareas ciclicas
CTasksVar = IntVar()
CTasks = Checkbutton(form, text='Pertenece a tareas ciclicas', variable=CTasksVar, bg='lightgray')
CTasks.pack()
CTasks.place(x=580,y=290)

# Nombre de documento de codigo fuente
lblSCodeFile = Label(form, text='Documento de codigo fuente:', bg='lightgray')
lblSCodeFile.pack()
lblSCodeFile.place(x=380,y=350)

SCodeVar = StringVar()
SCodeFile = Entry(form, textvariable=SCodeVar)
SCodeFile.pack()
SCodeFile.config(width=30)
SCodeFile.place(x=380,y=380)

# Nombre del encargado de ensayos
lblTestName = Label(form, text='Encargado de ensayos:', bg='lightgray')
lblTestName.pack()
lblTestName.place(x=580,y=350)

TestNameVar = StringVar()
TestName = Entry(form, textvariable=TestNameVar)
TestName.pack()
TestName.config(width=30)
TestName.place(x=580,y=380)

# Nombre del implementador
lblImplementer = Label(form, text='Implementador:', bg='lightgray')
lblImplementer.pack()
lblImplementer.place(x=780,y=350)

ImpVar = StringVar()
Implementer = Entry(form, textvariable=ImpVar)
Implementer.pack()
Implementer.config(width=30)
Implementer.place(x=780,y=380)

# Función para generar iniciales del verificador
def verIni(event):
    VerifierIni.delete(0,END)
    verif = Verifier.get().split(' ')
    for ini in verif:
        try:
            VerifierIni.insert(END,ini[0])
        except:
            pass

# Nombre del verificador
lblVerifier = Label(form, text='Nombre del verificador:', bg='lightgray')
lblVerifier.pack()
lblVerifier.place(x=120,y=410)

VerifVar = StringVar()
Verifier = Entry(form, textvariable=VerifVar)
Verifier.pack()
Verifier.config(width=30)
Verifier.place(x=120,y=440)
Verifier.bind('<KeyRelease>', verIni)

# Iniciales del verificador
lblVerifierIni = Label(form, text='Iniciales del verificador:', bg='lightgray')
lblVerifierIni.pack()
lblVerifierIni.place(x=320,y=410)

VerifIniVar = StringVar()
VerifierIni = Entry(form, textvariable=VerifIniVar)
VerifierIni.pack()
VerifierIni.config(width=30)
VerifierIni.place(x=320,y=440)

# HASH Codigo
lblHASHCode = Label(form, text='HASH Codigo:', bg='lightgray')
lblHASHCode.pack()
lblHASHCode.place(x=520,y=410)

HASHCodeVar = StringVar()
HASHCode = Entry(form, textvariable=HASHCodeVar)
HASHCode.pack()
HASHCode.config(width=30)
HASHCode.place(x=520,y=440)

# Producto
lblProduct = Label(form, text='Producto:', bg='lightgray')
lblProduct.pack()
lblProduct.place(x=720,y=410)

prodVar = StringVar()
Product = ttk.Combobox(form, textvariable=prodVar, state='readonly')
Product.pack()
Product.place(x=720,y=440)
Product['values'] = ('CHV','CTV','SIV','CHV-CTV','CHV-CTV-SIV','CTV-SIV')

# Sección de interfaces y figuras
lblIntFig = Label(form, text='INTERFACES', bg='lightgray')
lblIntFig.pack()
lblIntFig.place(x=120,y=480)
# Nombre de la interfaz
lblInterName = Label(form, text='Nombre de la interfaz:', bg='lightgray')
lblInterName.pack()
lblInterName.place(x=120,y=520)

interNameVar = StringVar()
interName = Entry(form, textvariable=interNameVar)
interName.pack()
interName.config(width=30)
interName.place(x=120,y=550)

# Nombre de la figura en SDS
lblFigName = Label(form, text='Nombre de la figura en SDS:', bg='lightgray')
lblFigName.pack()
lblFigName.place(x=320,y=520)

figNameVar = StringVar()
figName = Entry(form, textvariable=figNameVar)
figName.pack()
figName.config(width=30)
figName.place(x=320,y=550)

# Parámetros de la interfaz
lblInterP = Label(form, text='Parámetros de la interfaz:', bg='lightgray')
lblInterP.pack()
lblInterP.place(x=520,y=520)

interPVar = StringVar()
interP = Entry(form, textvariable=interPVar)
interP.pack()
interP.config(width=30)
interP.place(x=520,y=550)

# Interfaz desarrollada con datos/algoritmos de aplicación
aplicAlgVar = IntVar()
aplicAlg = Checkbutton(form, text='Desarrollada con datos/algoritmos\n de aplicación', bg='lightgray', variable=aplicAlgVar)
aplicAlg.pack()
aplicAlg.place(x=720,y=524)

# Función para agregar interfaz
def addInterface():
    tbInterfaces.insert('', END, 
        text='{0}'.format(interNameVar.get()),
        values=(
            '{0}'.format(figNameVar.get()),
            '{0}'.format(interPVar.get()),
            '{0}'.format(aplicAlgVar.get())
        )
    )
    interName.delete(0,END)
    figName.delete(0,END)
    interP.delete(0,END)
    aplicAlg.deselect()

# Botón para agreagar interfaz
btnAddInter = Button(form, text='Agregar', command=addInterface)
btnAddInter.pack()
btnAddInter.place(x=1150,y=580, width=60)

# Función para editar una interfaz
def editInterface():
    try:
        item = tbInterfaces.selection()[0]
        values = tbInterfaces.item(item)['values']
    except:
        pass
    else:
        btnAddInter.config(state='disabled')
        btnSaveInter.config(state='normal')
        values.insert(0,list(tbInterfaces.item(item).values())[0])
        interName.insert(0,values[0])
        figName.insert(0,values[1])
        interP.insert(0,values[2])
        if(values[3] == 1):
            aplicAlg.select()
        else:
            aplicAlg.deselect()

# Botón para editar interfaz
btnEditInter = Button(form, text='Editar', command=editInterface)
btnEditInter.pack()
btnEditInter.place(x=1150,y=620, width=60)

# Función para guardar interfaz editada
def saveInterface():
    item = tbInterfaces.selection()[0]
    tbInterfaces.item(item, 
        text='{0}'.format(interNameVar.get()),
        values=(
            '{0}'.format(figNameVar.get()),
            '{0}'.format(interPVar.get()),
            '{0}'.format(aplicAlgVar.get())
        )    
    )
    interName.delete(0,END)
    figName.delete(0,END)
    interP.delete(0,END)
    aplicAlg.deselect()
    btnAddInter.config(state='normal')
    btnSaveInter.config(state='disabled')

# Botón para agreagar interfaz
btnSaveInter = Button(form, text='Guardar', command=saveInterface, state='disabled')
btnSaveInter.pack()
btnSaveInter.place(x=1150,y=660, width=60)

# Función para eliminar interfaz
def delInterface():
    item = tbInterfaces.selection()[0]
    tbInterfaces.delete(item)

# Botón para eliminar interfaz
btnDelInter = Button(form, text='Eliminar', command=delInterface)
btnDelInter.pack()
btnDelInter.place(x=1150,y=700, width=60)

def cleanTBI():
    clean = messagebox.askyesno(message='¿Seguro que deseas limpiar la tabla?', title='Limpiar tabla')
    if(clean):
        for item in tbInterfaces.get_children():
            tbInterfaces.delete(item)

# Botón para eliminar todas las interfaces
btnCleanInter = Button(form, text='Limpiar', bg='red', fg='white', command=cleanTBI)
btnCleanInter.pack()
btnCleanInter.place(x=1150,y=740, width=60)

# Tabla para información de interfaces
tbInterfaces = ttk.Treeview(form, columns=('SDS_Fig','Param','aplicAlg'))
tbInterfaces.heading('#0', text='Nombre_Interfaz')
tbInterfaces.heading('SDS_Fig', text='Figura_SDS')
tbInterfaces.heading('Param', text='Parámetros')
tbInterfaces.heading('aplicAlg', text='Datos/algoritmos de aplicación')
tbInterfaces.pack()
tbInterfaces.place(x=120,y=580,width=1000,height=300)

lblFig = Label(form, text='FIGURAS', bg='lightgray')
lblFig.pack()
lblFig.place(x=120,y=910)

# Nombre de la interfaz
lblFigInt = Label(form, text='Nombre de la interfaz:', bg='lightgray')
lblFigInt.pack()
lblFigInt.place(x=120,y=940)

FigIntVar = StringVar()
FigInt = Entry(form, textvariable=FigIntVar)
FigInt.pack()
FigInt.config(width=30)
FigInt.place(x=120,y=970)

# Tamaño de complejidad ciclomatica
lblCComplex = Label(form, text='Tamaño de complejidad ciclomatica:', bg='lightgray')
lblCComplex.pack()
lblCComplex.place(x=320,y=940)

CComplexVar = StringVar()
CComplex = Spinbox(form, from_=0, to=100, state='readonly', textvariable=CComplexVar)
CComplex.pack()
CComplex.place(x=320,y=970,width=200)

# Tabla para información de figuras
tbFig = ttk.Treeview(form, columns=('CComplex'))
tbFig.heading('#0', text='Nombre_Interfaz')
tbFig.heading('CComplex', text='Complejidad_Ciclomatica')
tbFig.pack()
tbFig.place(x=120,y=1000,width=1000,height=300)

# Función para agregar interfaz
def addFig():
    tbFig.insert('', END, 
        text='{0}'.format(FigIntVar.get()),
        values=(
            '{0}'.format(CComplexVar.get())
        )
    )
    FigInt.delete(0,END)
    CComplex.delete(0,END)

# Botón para agreagar interfaz
btnAddFig = Button(form, text='Agregar', command=addFig)
btnAddFig.pack()
btnAddFig.place(x=1150,y=1000, width=60)

# Función para editar una interfaz
def editFig():
    try:
        item = tbFig.selection()[0]
        values = tbFig.item(item)['values']
    except:
        pass
    else:
        btnAddFig.config(state='disabled')
        btnSaveFig.config(state='normal')
        FigInt.delete(0,END)
        CComplex.delete(0,END)
        values.insert(0,list(tbFig.item(item).values())[0])
        FigInt.insert(0,values[0])
        CComplex.insert(0,values[1])

# Botón para editar interfaz
btnEditFig = Button(form, text='Editar', command=editFig)
btnEditFig.pack()
btnEditFig.place(x=1150,y=1040, width=60)

# Función para guardar interfaz editada
def saveFig():
    item = tbFig.selection()[0]
    tbFig.item(item, 
        text='{0}'.format(FigIntVar.get()),
        values=(
            '{0}'.format(CComplexVar.get())
        )    
    )
    FigInt.delete(0,END)
    CComplex.delete(0,END)
    btnAddFig.config(state='normal')
    btnSaveFig.config(state='disabled')

# Botón para agreagar interfaz
btnSaveFig = Button(form, text='Guardar', command=saveFig, state='disabled')
btnSaveFig.pack()
btnSaveFig.place(x=1150,y=1080, width=60)

# Función para eliminar interfaz
def delFig():
    try:
        item = tbFig.selection()[0]
    except:
        pass
    else:
        tbFig.delete(item)

# Botón para eliminar interfaz
btnDelFig = Button(form, text='Eliminar', command=delFig)
btnDelFig.pack()
btnDelFig.place(x=1150,y=1120, width=60)

def cleanTBF():
    clean = messagebox.askyesno(message='¿Seguro que deseas limpiar la tabla?', title='Limpiar tabla')
    if(clean):
        for item in tbFig.get_children():
            tbFig.delete(item)

# Botón para eliminar todas las interfaces
btnCleanFig = Button(form, text='Limpiar', bg='red', fg='white', command=cleanTBF)
btnCleanFig.pack()
btnCleanFig.place(x=1150,y=1160, width=60)

# Funcion para agregar reporte a la tabla
def addReport():
    for item in tbInterfaces.get_children():
        values = tbInterfaces.item(item)['values']
        values.insert(0,list(tbInterfaces.item(item).values())[0])
        tbInterfacesR.insert('',END,text='{0}'.format(len(tbReports.get_children())),
        values=(
            '{0}'.format(values[0]),
            '{0}'.format(values[1]),
            '{0}'.format(values[2]),
            '{0}'.format(values[3])
        ))
    for item in tbFig.get_children():
        values = tbFig.item(item)['values']
        values.insert(0,list(tbFig.item(item).values())[0])
        tbFigR.insert('',END,text='{0}'.format(len(tbReports.get_children())),
        values=(
            '{0}'.format(values[0]),
            '{0}'.format(values[1])
        ))
    tbReports.insert('',END,text='{0}'.format(len(tbReports.get_children())),
    values=(
        '{0}'.format(faseVar.get()),
        '{0}'.format(IdComp.get()),
        '{0}'.format(NameDITI.get()),
        '{0}'.format(ComponentsRel.get('1.0',END)),
        '{0}'.format(HASH_Var.get()),
        '{0}'.format(ErrorDetect.get('1.0',END)),
        '{0}'.format(BufferComp.get('1.0',END)),
        '{0}'.format(SILVar.get()),
        '{0}'.format(InterVar.get()),
        '{0}'.format(EstTestVar.get()),
        '{0}'.format(EffectVar.get()),
        '{0}'.format(MultiVar.get()),
        '{0}'.format(Req.get('1.0',END)),
        '{0}'.format(BlackVar.get()),
        '{0}'.format(PriVar.get()),
        '{0}'.format(MinutasVar.get()),
        '{0}'.format(HSRelVar.get()),
        '{0}'.format(ExpTypesVar.get()),
        '{0}'.format(CTasksVar.get()),
        '{0}'.format(SCodeVar.get()),
        '{0}'.format(TestNameVar.get()),
        '{0}'.format(ImpVar.get()),
        '{0}'.format(VerifVar.get()),
        '{0}'.format(VerifIniVar.get()),
        '{0}'.format(HASHCodeVar.get()),
        '{0}'.format(prodVar.get()),
    ))
    # Borrado del formulario
    deleteAll()
    for item in tbFig.get_children():
            tbFig.delete(item)
    for item in tbInterfaces.get_children():
            tbInterfaces.delete(item)

# Boton de agregado
addBtn = Button(form, text='Agregar', command=addReport)
addBtn.pack()
addBtn.place(x=1040,y=1350,width=80,height=50)

def saveReport():
    try:
        item = tbReports.selection()[0]
    except:
        print('Error al guardar')
    else:
        btnSave.config(state='disabled')
        tbReports.item(item, text='{0}'.format(list(tbReports.item(item).values())[0]), values=(
            fase.get(),
            IdComp.get(),
            NameDITI.get(),
            ComponentsRel.get('1.0',END),
            HASH_Var.get(),
            ErrorDetect.get('1.0',END),
            BufferComp.get('1.0',END),
            SILVar.get(),
            InterVar.get(),
            EstTestVar.get(),
            EffectVar.get(),
            MultiVar.get(),
            Req.get('1.0',END),
            BlackVar.get(),
            PriVar.get(),
            MinutasVar.get(),
            HSRelVar.get(),
            ExpTypesVar.get(),
            CTasksVar.get(),
            SCodeVar.get(),
            TestNameVar.get(),
            ImpVar.get(),
            VerifVar.get(),
            VerifIniVar.get(),
            HASHCodeVar.get(),
            prodVar.get(),
        ))
        itemSel = tbReports.selection()[0]
        for item in tbInterfaces.get_children():
            tbInterfacesR.insert('', END, text='{0}'.format(tbReports.item(itemSel)['text']), values=(
                '{0}'.format(tbInterfaces.item(item)['text']),
                '{0}'.format(tbInterfaces.item(item)['values'][0]),
                '{0}'.format(tbInterfaces.item(item)['values'][1]),
                '{0}'.format(tbInterfaces.item(item)['values'][2])
            ))
            tbInterfaces.delete(item)
        for item in tbFig.get_children():
            tbFigR.insert('', END, text='{0}'.format(tbReports.item(itemSel)['text']), values=(
                '{0}'.format(tbFig.item(item)['text']),
                '{0}'.format(tbFig.item(item)['values'][0])
            ))
            tbInterfaces.delete(item)
        deleteAll()
        addBtn.config(state='normal')


# Botón para guardar en caso de editar
btnSave = Button(form, text='Guardar', command=saveReport, state='disabled')
btnSave.pack()
btnSave.place(x=930,y=1350,width=80,height=50)

# Segunda pestaña
# Frame para archivos CSV
tbsContainer = Canvas(container)
tbsContainer.config(bg='lightgray', width=1300, height=700)
tbsContainer.pack(side='left', fill='both', expand='yes')
tbsContainer.pack_propagate(False)

CSV_Upload = Frame(tbsContainer, width=1600, height=900)
#CSV_Upload.pack()
CSV_Upload.config(bg='lightgray')
CSV_Upload.pack_propagate(False)
#CSV_Upload.location(x=600, y=350)
container.add(tbsContainer, text='Archivo CSV')

tbsScrollX = Scrollbar(container, orient='horizontal', command=tbsContainer.xview)
tbsScrollX.pack(side='bottom', fill='x')
tbsContainer.configure(xscrollcommand=tbsScrollX.set)
tbsContainer.bind(
    "<Configure>", lambda e: 
        tbsContainer.configure(
            scrollregion=tbsContainer.bbox("all")
        )
    )

tbsContainer.create_window((0,0), window=CSV_Upload, anchor='nw')

# Tabla para mostrar informacion obtenida del archivo (o informacion agregada manualmente)
tbReports = ttk.Treeview(CSV_Upload, columns=('fase','nameComp','nameDITI','relComp', 'HASH','errorDetect','bufferComp','SIL','devInter','estrTest','effectP','multiP','req','blackBox','privInter','minutas','hsRel','expTypes','cTasks','scFile','nameTest','impName','verifName','verifIni','hashC','prod'))
tbReports.heading('#0', text='#')
tbReports.heading('fase', text='Etapa')
tbReports.heading('nameComp', text='IDComp_NameComp')
tbReports.heading('nameDITI', text='DES/IMP_TST/INT')
tbReports.heading('relComp', text='Comp_Rel')
tbReports.heading('HASH', text='HASH')
tbReports.heading('errorDetect', text='Error_Detect')
tbReports.heading('bufferComp',text='Buffer_Comp')
tbReports.heading('SIL',text='SIL')
tbReports.heading('devInter',text='Dev_Inter')
tbReports.heading('estrTest',text='Est_Test')
tbReports.heading('effectP',text='P_Efect')
tbReports.heading('multiP',text='P_Multi')
tbReports.heading('req',text='Req')
tbReports.heading('blackBox',text='Caja_Negra')
tbReports.heading('privInter',text='Priv_Inter')
tbReports.heading('minutas',text='Minuta')
tbReports.heading('hsRel',text='Rel_HS')
tbReports.heading('expTypes',text='TiposExp')
tbReports.heading('cTasks',text='TareasC')
tbReports.heading('scFile',text='CodigoF')
tbReports.heading('nameTest',text='Ensayos')
tbReports.heading('impName',text='Implementador')
tbReports.heading('verifName',text='Verif')
tbReports.heading('verifIni',text='IniVerif')
tbReports.heading('hashC',text='HASH_C')
tbReports.heading('prod',text='Producto')

tbReports.pack()
tbReports.place(x=20,y=100,width=740,height=590)

# Funciones para llamar funciones para manejar archivos CSV
def addCall():
    fm.addInfo(tbReports)

# Boton para buscar archivo CSV
btnAddCSV = Button(CSV_Upload, text='Agregar reportes', command=addCall)
btnAddCSV.pack()
btnAddCSV.place(x=660,y=60)

# Funcion para borrar contenido de la tabla
def cleanTBR():
    clean = messagebox.askyesno(message='¿Seguro que deseas limpiar la tabla?', title='Limpiar tabla')
    if(clean):
        for item in tbReports.get_children():
            tbReports.delete(item)

# Boton para limpiar la tabla
btnCleanTB = Button(CSV_Upload, text='Limpiar tabla', command=cleanTBR, bg='red', fg='white')
btnCleanTB.pack()
btnCleanTB.place(x=20,y=60)

def editRep():
    try:
        item = tbReports.selection()[0]
        item_text = tbReports.item(item)['text']
        values = tbReports.item(item)['values']
    except:
        pass
    else:
        btnSave.config(state='normal')
        addBtn.config(state='disabled')
        enableAll()

        # Borrado del formulario
        deleteAll()

        # Llenado del formulario
        fase.set(values[0])
        NameComp.insert(0,values[1])
        Name_DESIMP_TSTINT.insert(0,values[2])
        ComponentsRel.insert('1.0',values[3])
        HASH.insert(0,values[4])
        ErrorDetect.insert('1.0',values[5])
        BufferComp.insert('1.0',values[6])
        SIL.insert(0,values[7])
        Interfaces.select()
        EstructureTest.insert(0,values[9])
        EffectP.insert(0,values[10])
        MultiP.insert(0,values[11])
        Req.insert('1.0',values[12])
        BlackBox.insert(0,values[13])
        PrivateInt.insert(0,values[14])
        if(values[15]==1):
            Minutas.select()
        if(values[16]==1):
            HSRel.select()
        if(values[17]==1):
            ExpTypes.select()
        if(values[18]==1):
            CTasks.select()
        SCodeFile.insert(0,values[19])
        TestName.insert(0,values[20])
        Implementer.insert(0,values[21])
        Verifier.insert(0,values[22])
        VerifierIni.insert(0,values[23])
        HASHCode.insert(0,values[24])
        Product.insert(0,values[25])
        
        # Llenado de tablas de interfaces y figuras
        if((tbReports.item(item)['values'][0] == 'SDS') or (tbReports.item(item)['values'][0] == 'SCDS') or (tbReports.item(item)['values'][0] == 'SCTR') or (tbReports.item(item)['values'][0] == 'SIS')):
            for item in tbInterfacesR.get_children():
                if(tbInterfacesR.item(item)['text'] == item_text):
                    item_values = tbInterfacesR.item(item)['values']
                    tbInterfaces.insert('',END,text='{0}'.format(item_values[0]), values=(
                        '{0}'.format(item_values[1]),
                        '{0}'.format(item_values[2]),
                        '{0}'.format(item_values[3])
                    ))
                    tbInterfacesR.delete(item)
                else:
                    pass
            for item in tbFigR.get_children():
                if(tbFigR.item(item)['text'] == item_text):
                    item_values = tbFigR.item(item)['values']
                    tbFig.insert('',END,text='{0}'.format(item_values[0]), values=(
                        '{0}'.format(item_values[1])
                    ))
                    tbFigR.delete(item)
                else:
                    pass


# Boton para editar un registro
btnEdit = Button(CSV_Upload, text='Editar', command=editRep)
btnEdit.pack()
btnEdit.place(x=600,y=60)

# Función para borrar reporte
def delReport():
    item = tbReports.selection()[0]
    id = tbReports.item(item)['text']
    if((tbReports.item(item)['values'][0] == 'SDS') or (tbReports.item(item)['values'][0] == 'SCDS')):
        for itemI, itemF in zip(tbInterfacesR.get_children(), tbFigR.get_children()):
            if(tbInterfacesR.item(itemI)['text'] == id):
                tbInterfacesR.delete(itemI)
            if(tbFigR.item(itemF)['text'] == id):
                tbFigR.delete(itemF)
    tbReports.delete(item)

# Boton para eliminar un reporte
btnDelRep = Button(CSV_Upload, text='Eliminar', command=delReport)
btnDelRep.pack()
btnDelRep.place(x=520,y=60)

# Scrollbar para la tabla de informacion
tbScrollX = Scrollbar(tbReports, orient='horizontal', command=tbReports.xview)
tbScrollX.pack(side='bottom', fill='x')
tbScrollY = Scrollbar(tbReports, orient='vertical', command=tbReports.yview)
tbScrollY.pack(side='right', fill='y')
tbReports.configure(xscrollcommand=tbScrollX.set, yscrollcommand=tbScrollY.set)

# Tabla de interfaces
lblInterTB = Label(CSV_Upload, text='INTERFACES', bg='lightgray')
lblInterTB.pack()
lblInterTB.place(x=800,y=100)

tbInterfacesR = ttk.Treeview(CSV_Upload, columns=('interName','SDS_Fig','Param','aplicAlg'))
tbInterfacesR.heading('#0', text='#')
tbInterfacesR.heading('interName', text='Nombre_Interfaz')
tbInterfacesR.heading('SDS_Fig', text='Figura_SDS')
tbInterfacesR.heading('Param', text='Parámetros')
tbInterfacesR.heading('aplicAlg', text='Datos/algoritmos de aplicación')
tbInterfacesR.pack()
tbInterfacesR.place(x=800,y=130,width=700,height=260)

def addInterCall():
    fm.addInterface(tbInterfacesR)

btnAddInterface = Button(CSV_Upload, text='Agregar', command=addInterCall)
btnAddInterface.pack()
btnAddInterface.place(x=1440,y=100)

def cleanInterfaceR():
    if(messagebox.askyesno(message='¿Seguro que desear limpiar la tabla?', title='Limpiar tabla')):
        for item in tbInterfacesR.get_children():
            tbInterfacesR.delete(item)

btnCleanIntR = Button(CSV_Upload, text='Limpiar', bg='red', fg='white', command=cleanInterfaceR)
btnCleanIntR.pack()
btnCleanIntR.place(x=1320,y=100)

def delInt():
    item = tbInterfacesR.selection()[0]
    tbInterfacesR.delete(item)

btnDelInt = Button(CSV_Upload, text='Eliminar', command=delInt)
btnDelInt.pack()
btnDelInt.place(x=1380,y=100)

def delFigR():
    item = tbFigR.selection()[0]
    tbFigR.delete(item)

btnDelF = Button(CSV_Upload, text='Eliminar', command=delFigR)
btnDelF.pack()
btnDelF.place(x=1380,y=400)

def cleanFigR():
    if(messagebox.askyesno(message='¿Seguro que desear limpiar la tabla?', title='Limpiar tabla')):
        for item in tbFigR.get_children():
            tbFigR.delete(item)

btnCleanFigR = Button(CSV_Upload, text='Limpiar', bg='red', fg='white', command=cleanFigR)
btnCleanFigR.pack()
btnCleanFigR.place(x=1320,y=400)

def addFigCall():
    fm.addFig(tbFigR)

btnAddF = Button(CSV_Upload, text='Agregar', command=addFigCall)
btnAddF.pack()
btnAddF.place(x=1440,y=400)

# Scrollbar para tabla de interfaces
tbIntScrollX = Scrollbar(tbInterfacesR, orient='horizontal', command=tbInterfacesR.xview)
tbIntScrollX.pack(side='bottom', fill='x')
tbIntScrollY = Scrollbar(tbInterfacesR, orient='vertical', command=tbInterfacesR.yview)
tbIntScrollY.pack(side='right', fill='y')
tbInterfacesR.configure(xscrollcommand=tbIntScrollX.set, yscrollcommand=tbIntScrollY.set)

# Tabla de figuras
lblFigTB = Label(CSV_Upload, text='FIGURAS', bg='lightgray')
lblFigTB.pack()
lblFigTB.place(x=800,y=400)

tbFigR = ttk.Treeview(CSV_Upload, columns=('interName','CComplex'))
tbFigR.heading('#0', text='#')
tbFigR.heading('interName', text='Nombre_Interfaz')
tbFigR.heading('CComplex', text='Complejidad_Ciclomatica')
tbFigR.pack()
tbFigR.place(x=800,y=430,width=700,height=260)

# Scrollbar para tabla de figuras
tbFigScrollX = Scrollbar(tbFigR, orient='horizontal', command=tbFigR.xview)
tbFigScrollX.pack(side='bottom', fill='x')
tbFigScrollY = Scrollbar(tbFigR, orient='vertical', command=tbFigR.yview)
tbFigScrollY.pack(side='right', fill='y')
tbFigR.configure(xscrollcommand=tbFigScrollX.set, yscrollcommand=tbFigScrollY.set)

def callGenDoc():
    fm.genDocs(tbReports, tbInterfacesR, tbFigR)

# Botón para generar reportes
btnGenReports = Button(CSV_Upload, text='Generar', bg='green', fg='white', command=callGenDoc)
btnGenReports.pack()
btnGenReports.place(x=1420,y=20,width=80,height=40)

# Desabilitar elementos hasta que no se seleccione una etapa
disableAll()

root.mainloop()