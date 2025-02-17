import subprocess
import os
class Obtener:
    def GetScript( tabla ):
        try:
            os.environ['PGPASSWORD'] = 'admin1234'
            comando = [
                'pg_dump',
                '-h', '216.250.124.212',              # Agrega el host aquí
                '-U', 'postgres',
                '-d', 'ApegoContractual',
                '-t', tabla,
                '--schema-only'
            ]
            resultado = subprocess.run(comando, capture_output=True, text=True, check=True)
            # Devuelve el resultado si el comando fue exitoso
            return resultado.stdout
        except subprocess.CalledProcessError as e:
            # Maneja errores en la ejecución del comando, como credenciales incorrectas
            return f"Error al ejecutar pg_dump: {e.stderr}"
        finally:
            # Asegúrate de eliminar la variable de entorno después de usarla
            if 'PGPASSWORD' in os.environ:
                del os.environ['PGPASSWORD']
       

 



    