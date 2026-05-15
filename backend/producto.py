from backend.hoja_producto import obtener_hoja_de_productos

def listar_productos():
    hoja = obtener_hoja_de_productos()
    filas = []
    ref_filas = hoja.iter_rows(min_row=2, max_row=hoja.max_row, min_col=1, max_col=4)
    for ref_fila in ref_filas:
        valores = []
        for celda in ref_fila:
            valores.append(celda.value)
        filas.append(valores)
    return filas

def consultar_producto(id_producto):
    hoja = obtener_hoja_de_productos()
    ref_filas = hoja.iter_rows(min_row=2, max_row=hoja.max_row, min_col=1, max_col=4)
    for enumeracion, ref_fila in enumerate(ref_filas):
        if ref_fila[0].value == id_producto:
            valores = [enumeracion]
            for celda in ref_fila:
                valores.append(celda.value)
            return valores
    return None
