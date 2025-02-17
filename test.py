from cryptography.fernet import Fernet

key = Fernet.generate_key()


clave_fija = b'-STJLyFh9yWo_ptAY7R7VgugGZdiAxN1NVa8REHxEiI='  
cifrador = Fernet(clave_fija)
#texto = "select * from  public.relproyecto"
#texto_cifrado = cifrador.encrypt(texto.encode())
#print("Texto cifrado:", texto_cifrado)

#gAAAAABns3XPr9QyDT4LPzl59EHMGNBGefvsclTBZOkxAS7b3dXAvSHbLhndPJA-iEXGe6N8RscWbAnVHW8xKgRtR81k1qQBPe7E1Q2ptdKCrRbUN5izFdFtx5jnTBB7k4l9qy3ke3S-
 

texto_descifrado = cifrador.decrypt('gAAAAABns3XPr9QyDT4LPzl59EHMGNBGefvsclTBZOkxAS7b3dXAvSHbLhndPJA-iEXGe6N8RscWbAnVHW8xKgRtR81k1qQBPe7E1Q2ptdKCrRbUN5izFdFtx5jnTBB7k4l9qy3ke3S-').decode()
print("Texto descifrado:", texto_descifrado)
