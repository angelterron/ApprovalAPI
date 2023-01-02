from sqlalchemy import create_engine, MetaData, Table, insert, select
from datetime import datetime

# función para validar que existan los atributos requeridos
def validar(persona, atributo):
    # si el atributo no se encuentra dentro del objeto, se retorna una exception.
    if atributo not in persona:
        raise Exception('El atributo {} es necesario'.format(atributo))


def insertar(persona):
    # Listado de atributos a validar
    atributos = ['nombre', 'apellidop', 'apellidom', 'fnacimiento', 'ingresos', 'dependientes']
    # Validación de atributos 1 por 1
    for a in atributos:
        try:
            validar(persona, a)
        except Exception as e:
            raise e

    # Determinación de aprobación del crédito
    if persona['ingresos'] > 25000:
        aprobado = 1
    elif persona['ingresos'] > 15000 and persona['dependientes'] < 3:
        aprobado = 1
    else:
        aprobado = 0

    # asignar la aprobación al objeto recibido
    persona['aprobado'] = aprobado

    # Obtener fecha de nacimiento en objeto
    fnacimiento = datetime.strptime(persona['fnacimiento'], '%Y-%m-%d')

    # Crear el RFC de acuerdo a las reglas mencionadas
    rfc = persona['apellidop'][:2] + persona['apellidom'][:1] + persona['nombre'][:1] + fnacimiento.strftime("%y%m%d")
    
    # Asignar el RFC al objeto recibido
    persona['RFC'] = rfc

    # abrir una conexión en SQL alchemy
    # IMPORTANTE: reemplazar 'user' y 'password' por los correspondientes a la base de datos
    conn = create_engine("mysql+pymysql://root:Manaphy1@localhost/clientes_approval_dev")
    # Obtener el metadata de la base de datos
    metadata = MetaData(conn)
    # Reflejar la base de datos clientes para tener toda su información y estructura
    mytable = Table('clientes', metadata, autoload=True)

    # Crear el statement para realizar la inserción de datos.
    stmt = (mytable.insert().values(NOMBRE = persona['nombre'],
                APATERNO = persona['apellidop'],
                AMATERNO = persona['apellidom'],
                FNACIMIENTO = persona['fnacimiento'],
                INGRESOSMENSUALES = persona['ingresos'],
                DEPENDIENTESECONOMICOS = persona['dependientes'],
                RFC = persona['RFC'],
                APROBADO = persona['aprobado'])
    )
    
    # Ejecutar la consulta
    conn.execute(stmt)

    # Realizar una consulta para obtener el último ID insertado.
    stmt = (
        select(mytable.columns.ID).order_by(mytable.columns.ID.desc()).limit(1)
    )

    # Ejecutar la consulta
    result = conn.execute(stmt).fetchone()

    # Asignar el nuevo ID al objeto recibido
    persona['id'] = result[0]
    
    # Retornar el objeto persona con los nuevos valores obtenidos
    return persona
    

