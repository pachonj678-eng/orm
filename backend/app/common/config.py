import pymysql

class Config:
    # Datos de conexión para MySQL (configurados sin contraseña para XAMPP/phpMyAdmin por defecto)
    USER = 'root'          # Usuario de MySQL
    PASSWORD = ''          # Contraseña vacía por defecto en entornos locales como XAMPP
    HOST = 'localhost'     # Host donde corre MySQL
    DATABASE = 'db_products' # Nombre de la base de datos

    # URL de conexión para SQLAlchemy usando el conector PyMySQL
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}'
    
    # Desactiva el rastreo de modificaciones para evitar advertencias
    SQLALCHEMY_TRACK_MODIFICATIONS = False