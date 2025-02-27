from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
def create_app():
    app = Flask(__name__)
    CORS(app)  # Habilita CORS para todas las rutas
    
    app.config["JWT_SECRET_KEY"] = "PMS2024_PEOPL3M3D14"
    jwt = JWTManager(app)

    from auth import auth_bp   
    app.register_blueprint(auth_bp, url_prefix="/gencodigo/auth")
    from GeneraCodigo import genera_bp
    app.register_blueprint(genera_bp, url_prefix="/gencodigo/pregunta")
    
    from GeneraPrototipo import generaprototipo_bp
    app.register_blueprint(generaprototipo_bp, url_prefix="/gencodigoprototipo/pregunta")
    
    from GeneraObjetos import generaObjetos_bp
    app.register_blueprint(generaObjetos_bp, url_prefix="/genObjetos")
    
    from GeneraModulosCodigo import modulosrepo_bp
    app.register_blueprint(modulosrepo_bp, url_prefix="/modulosrepositorio")
    
    #from Aplicador_Inocular import inoculacion_bp
    #app.register_blueprint(inoculacion_bp, url_prefix="/Aplicador/Inoculacion")
    return app