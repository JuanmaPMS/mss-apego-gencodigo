import base64
from io import BytesIO
from sqlalchemy import create_engine, MetaData
from sqlalchemy_schemadisplay import create_schema_graph
import uuid
import os
class ER:
    def creaER():
        try:
            DATABASE_URL = "postgresql://postgres:D3s4rr0ll0$2024@10.166.0.54/ApegoContractual"
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
            ruta = "imagenesER/"+str(uuid.uuid4())+".png"
            graph.write_png(ruta)
            
            with open(ruta, "rb") as file:
                byte_array = file.read()
            os.remove(ruta)
            return byte_array
        except:
            return None         
