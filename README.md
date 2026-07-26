# Proyecto\_Motion\_Lab\_Ejemplo



Este proyecto es usado de ejemplo para mostrar en clase de la Lic en Ciencias del Comportamiento durante la clase de Validación y Manejo de Errores.






## MotionLab: Análisis de Control Motor y Precisión



### 📌 Sobre el Proyecto



*MotionLab* es un sistema desarrollado para procesar y analizar datos provenientes de experimentos de coordinación visomotora. El objetivo principal es evaluar cómo diferentes condiciones experimentales (como la competencia o la cooperación) afectan la precisión del movimiento humano y el tiempo de respuesta.



Este software permite transformar datos crudos de coordenadas espaciales y eventos temporales en métricas accionables para la investigación en neurociencias y psicología cognitiva.



### 🧪 El Experimento



En la tarea de MotionLab, los participantes deben interactuar con estímulos en pantalla. El sistema registra:



Trayectorias: Coordenadas $(x, y)$ del movimiento.

Eventos (Hits): Momentos exactos de interacción exitosa.

Condiciones: Variaciones en el entorno social del participante.



### 🚀 Características del Sistema



El proyecto sigue una arquitectura modular para garantizar la escalabilidad y facilitar el testing:



*Carga Robusta:* Importación de datos desde formatos CSV con manejo de errores.

*Validación de Datos:* Filtros automáticos para descartar registros corruptos o fuera de rango.

*Motor de Métricas:*

&#x20;     \* Cálculo de Hits Totales.

&#x20;     \* Detección del Tiempo al Primer Hit (Latencia).

&#x20;     \* Análisis opcional por bloques temporales para ver la curva de aprendizaje.



### 📁 Estructura del Repositorio



```text

MotionLab/

├── data/               # Archivos CSV con datos experimentales 

├── src/                # Código fuente modular

│   ├── carga\_datos.py        # Lectura y parseo de archivos

│   ├── validacion\_datos.py   # Limpieza y reglas de negocio

│   ├── procesamiento\_datos.py # Organización de perfiles de usuario

│   └── metricas.py           # Algoritmos de análisis

├── main.py             # Script principal de ejecución

└── README.md           # Documentación del proyecto

```



### 🛠️ Instalación y Uso



1\.  Clona este repositorio:


&#x20;   git clone https://github.com/pramirezudesa/Proyecto_Motion_Lab_Ejemplo


2\.  Asegúrate de tener Python 3.x instalado.

3\.  Ejecuta el análisis principal:



&#x20;   python main.py





### 📊 Ejemplo de Salida



Al ejecutar el sistema, obtendrás un reporte consolidado por participante:



```text

ID       | HITS   | 1er HIT    | CONDICIÓN

\---------------------------------------------

1        | 12     | 1.45s      | competencia

2        | 8      | 2.10s      | cooperacion

```



### 🧠 Referencias Científicas



Este proyecto se basa en paradigmas establecidos de control motor, tales como:



*Fitts, P. M. (1954). The information capacity of the human motor system in controlling the amplitude of movement.*

*Welford, A. T. (1968). Fundamentals of Skill.*



\-----



