# ApprovalAPI

Para la realización de este proyecto se utiliza **Python** como lenguaje de programación. Para la creación de la API se utiliza el framework **flask**. La base de datos utilizada es **MySQL** en su versión 8.0.

## Ejecución del proyecto

Para poder ejecutar el proyecto es necesario encontrarse en la carpeta del proyecto e inicializar el servicio de flask.

- Se inicia el servicio:

    `flask --app main run`

## Prueba del proyecto

El endpoint desarrollado para realizar las consultas es */cliente/*. A continuación se muestra un ejemplo del objeto que se debe enviar para obtener como respuesta la aprobación, el rfc y el nuevo identificador:

    ```
    {
        "nombre": "LORENZO FRANCISCO", 
        "apellidop" : "BALADO", 
        "apellidom" : "CIUCA", 
        "fnacimiento": "1982-09-12", 
        "ingresos": 10000, 
        "dependientes" : 3
    }
    ```

Los registros insertados durante las pruebas se pueden encontrar en la imagen **Registros.PNG** contenida en el proyecto.


*NOTA:* Es necesario modificar la cadena de conexión que se encuentra en el archivo data.py con las credenciales de la base de datos MySQL en la que se ejecute el proyecto. De igual forma es necesario ejecutar el script contenido en el proyecto.