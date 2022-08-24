# Proyecto Sabueso

## Objetivos

1. Dar justificación estadística a las prohibiciones del proyecto de ley de desarrollo urbano que en Junio de 2022 se está discutiendo en la legislatura de CDMX.
2. Dar recomendaciones de política pública para la Procuraduría Ambiental y de Ordenamiento Territorial.

## Obj 1: Justificación estadística a prohibiciones

## Obj 2: Dar recomendaciones de public policy

### Fases

1. Limpieza de datos
2. Análisis exploratorio


#### Limpieza de datos

1. Descargar e instalar Visual Studio Code (DEJAR DE USAR SPYDER)
2. Hacer branch por persona "captain-planet-alvlopzam" y "captain-planet-sammyboy"
3. Clonar el repo
4. Hacer checkout del branch que les toque
5. Tomar el CSV que viene en el ZIP anexo y ponerlo en [directorio_del_proyecto]/data/raw
6. Cargar CSV a Python con Pandas
7. Asegurarse que los valores de fechas sean realmente fechas
8. Asegurarse que campos categóricos sean realmente categóricos
9. Campos de entrecalles y referencias no se usarán
10. Colonia, alcaldía, régimen, medio recepción, materia y estatus son categóricos
11. Expediente debe ser categórico, PERO en denuncias con sufijo BIS, y agregar columna "denuncia padre" con el folio de la denuncia original.
12. renombrar columna a formatos estándar: 1) no mayúsculas, no acentos, y guiones bajos en vez de espacios.
13. Coordenadas X y Y se quedan como numéricos "float".

#### Análisis exploratorio

Preguntas de research:

1. Cuantas denuncias recibe VS cuantas denuncias resuelve:
    - por año
    - por mes
    - por trimestre
    - por año / materia
    - por mes / materia
    - por trimestre / materia
    - por año / medio recepción
    - por mes / medio recepción
    - por año / area responsable
    - por mes / area responsable
    - por año / alcaldía
    - por mes / alcaldía

2. Diagrama de Sankey para flujo de estados de denuncias **calculados a través de las fechas**
    - Tratar de coincidir fechas con estados (Estatus _en proceso de turno_ == Fecha _fecha de turno_)
    - Documentar suposiciones (i.e. Fecha de recepción no tiene un estado documentado, por lo que supondremos un estado "recibida").

3. Explorar utilidad de coordenadas. Sirven? Son de oficinas de PAOT? Implican denuncias dadas de alta en oficinas de la procuraduría? Son producto de las investigaciones? Son iguales a la dirección que aparece en el registro?

3. Cantidad de denuncias por tipo / nivel socioeconómico (ayudarse con AGEB y ENIGH, que debe estar en OpenBlender)





#### Tipos de Datos

1. Numeric - contínuo
2. Categorical
3. Texto
