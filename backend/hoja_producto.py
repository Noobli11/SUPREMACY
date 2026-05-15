import openpyxl

def obtener_hoja_de_productos():
    libro = openpyxl.load_workbook('Datos.xlsx')
    hoja = libro['productos']
    return hoja
