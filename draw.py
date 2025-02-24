import base64
from io import BytesIO
from sqlalchemy import create_engine, MetaData
from sqlalchemy_schemadisplay import create_schema_graph
import uuid
import os
from decouple import config
class ER:
    def creaER():
        try:
           #DATABASE_URL = "postgresql://postgres:D3s4rr0ll0$2024@10.166.0.54/ApegoContractual"
            DATABASE_URL = "postgresql://postgres:admin1234@216.250.124.212/ApegoContractual"
            engine = create_engine(DATABASE_URL)
            metadata = MetaData()
            metadata.reflect(bind=engine)
            graph = create_schema_graph(
                metadata=metadata,
                engine=engine,
                show_datatypes=True, 
                show_indexes=False,  
                rankdir="TB", 
                concentrate=True  
            )
            
             # Crear la carpeta si no existe
            carpeta_imagenes = "imagenesER"
            os.makedirs(carpeta_imagenes, exist_ok=True)
            
            
              # Generar un nombre de archivo único
            ruta = os.path.join(carpeta_imagenes, f"{uuid.uuid4()}.png")
            #rutaprog=config('PATH_GRAPGVIZ')
           # ruta =rutaprog +  carpeta_imagenes + f"{uuid.uuid4()}.png"
            graph.write_png(ruta)
            
            with open(ruta, "rb") as file:
                byte_array = file.read()
            os.remove(ruta)
            return byte_array
        except Exception as e:
            print(str(e))
            return None         
            
