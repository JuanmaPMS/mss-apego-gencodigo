import psycopg2
from cryptography.fernet import Fernet  
import os
from flask import  jsonify
from decimal import Decimal
from decouple import config

from Utils.Respuestas import Respuesta
 

class  Acceso:
    def __init__(self,Funcion,Params = None):
        self.Funcion_ = Funcion
        self.Params_ = Params
        
    def get_db_connection():
        conn = psycopg2.connect(
            host="216.250.124.212",
            database="ApegoContractual",
            user="postgres",
            password="admin1234"
        )
        return conn
    
    def EjecutaVista(self, condiciones=None, distinct=False, columnas=None):
        conn = Acceso.get_db_connection()
        try:
            cur = conn.cursor()
            where_clause = ""
            values = []
            
            if condiciones:
                where_parts = []
                for columna, (operador, valor) in condiciones.items():
                    if operador.upper() in ['IN', 'NOT IN']:
                        placeholders = ', '.join(['%s'] * len(valor))
                        where_parts.append(f"{columna} {operador} ({placeholders})")
                        values.extend(valor)
                    else:
                        where_parts.append(f"{columna} {operador} %s")
                        values.append(valor)
                where_clause = "WHERE " + " AND ".join(where_parts)
            
            # Seleccionar columnas específicas o todas si no se especifica ninguna
            columnas_seleccion = ", ".join(columnas) if columnas else "*"
            
            # Agregar DISTINCT si es necesario
            distinct_clause = "DISTINCT " if distinct else ""
            
            query = f'SELECT {distinct_clause}{columnas_seleccion} FROM {self.Funcion_} {where_clause}'
            
            cur.execute(query, values)
            rows = cur.fetchall()
            column_names = [desc[0] for desc in cur.description]
            data = [
                {column_name: row[idx] for idx, column_name in enumerate(column_names)}
                for row in rows
            ]
        finally:
            cur.close()
            conn.close()
        
        return data
    
    def EjecutaFuncion(self):
        conn = Acceso.get_db_connection()
        try:
            cur = conn.cursor()
            placeholders = ", ".join(["%s"] * len(self.Params_))
            query = f"SELECT * FROM {self.Funcion_}({placeholders})"
            cur.execute(query, self.Params_)
            rows = cur.fetchall()
            column_names = [desc[0] for desc in cur.description]
            data = [
                {column_name: row[idx] for idx, column_name in enumerate(column_names)}
                for row in rows
            ]
        finally:
            cur.close()
            conn.close()
        return data
    
    def EjecutaFuncionTabla(self):
        conn = Acceso.get_db_connection()
        try:
            cur = conn.cursor()
            placeholders = ", ".join(["%s"] * len(self.Params_))
            query = f"SELECT * FROM {self.Funcion_}({placeholders})"
            cur.execute(query, self.Params_)
            rows = cur.fetchall()
            column_names = [desc[0] for desc in cur.description]
            data = [
                {column_name: row[idx] for idx, column_name in enumerate(column_names)}
                for row in rows
            ]
        finally:
            cur.close()
            conn.close()
        return data
    

    def EjecutaFuncionCRUD(self):
        conn = Acceso.get_db_connection()
        try:
            cur = conn.cursor()
            placeholders = ", ".join(["%s"] * len(self.Params_))
            query = f"SELECT * FROM {self.Funcion_}({placeholders})"
            cur.execute(query, self.Params_)
            rows = cur.fetchall()
            column_names = [desc[0] for desc in cur.description]
            data = [
                {column_name: row[idx] for idx, column_name in enumerate(column_names)}
                for row in rows
            ]
            
        finally:
            conn.commit()
            cur.close()
            conn.close()
        return data
    
    def EjecutaRaw(self, Query):
        conn = None
        try:
            conn = Acceso.get_db_connection()
            cur = conn.cursor()
            #query = cifrador.decrypt(Query).decode()
            cur.execute(Query)
            columns = [desc[0] for desc in cur.description]  # Obtener nombres de las columnas
            rows = cur.fetchall()
            cur.close()
            
            # Convertir a lista de diccionarios
            results = [dict(zip(columns, row)) for row in rows]

            return results  # Retorna una lista de diccionarios
        except psycopg2.DatabaseError as e:
            print(f"Error en la base de datos: {e}")
            return None
        finally:
            if conn is not None:
                conn.close()
                
    def EjecutaPersistenciaRaw(self, Query):
        
        conn = None
        try:
            conn = Acceso.get_db_connection()
            cur = conn.cursor()
            cur.execute(Query)
            cur.close()
            conn.commit()            
            
            return Respuesta(True,"Se ejecutó el script", "")
        except psycopg2.DatabaseError as e:
            print(f"Error en la base de datos: {e}")
            return Respuesta(False, str(e), "")
        finally:
            if conn is not None:
                conn.close()

    def EjecutaRawFn(self, Query):
        conn = None
        try:
            conn = Acceso.get_db_connection()
            cur = conn.cursor()
            #query = cifrador.decrypt(Query).decode()
            cur.execute(Query)
            columns = [desc[0] for desc in cur.description]  # Obtener nombres de las columnas
            rows = cur.fetchall()
            cur.close()
            
            # Convertir a lista de diccionarios
            results = [dict(zip(columns, row)) for row in rows]

            return results  # Retorna una lista de diccionarios
        except psycopg2.DatabaseError as e:
            result = [{'error': f"Error en la base de datos: {e}"}]
            return result
        finally:
            if conn is not None:
                conn.close()
                
                
                