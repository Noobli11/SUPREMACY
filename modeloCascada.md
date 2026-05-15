# Modelo en Cascada

## Dificultades identificadas al aplicar la metodología de desarrollo en cascada

Al desarrollar la aplicación de lectura de productos aplicando la metodología en cascada, identifique las siguientes dificultades:

1. **Dependencia entre roles:** Al estar solo, fue necesario completar primero el backend antes de poder desarrollar el frontend, ya que el frontend depende directamente de las funciones y datos que expone el backend. Esto genera tiempos de espera que en un equipo real podrían bloquear el avance de otros integrantes, en mi caso yo solo.

2. **Dificultad para detectar errores temprano:** En cascada, las pruebas se realizan al final del proceso. Esto hizo que algunos errores de integración entre el backend y el frontend solo fueran visibles hasta que ambas partes estaban completamente desarrolladas, lo que dificultó su corrección para mi.

3. **Poca flexibilidad ante cambios:** Si durante el desarrollo del frontend se detectaba que el backend debía retornar los datos en un formato diferente, era necesario regresar a una etapa anterior y modificar código ya terminado, rompiendo el flujo lineal del modelo.

4. **Formato de datos en Excel:**  identifique que los valores numéricos en el archivo Excel debían estar en formato texto para que las consultas por Id funcionaran correctamente. Este tipo de detalle no es evidente en la etapa de análisis y solo lo descubri durante las pruebas.

5. **Comunicación entre etapas:** En un equipo real con este modelo, la falta de comunicación entre el desarrollador backend y el frontend podría generar inconsistencias, como nombres de funciones distintos o estructuras de datos incompatibles, en mi caso fue mi propia comunicación.
