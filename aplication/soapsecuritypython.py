#SOA PythonSecurity

from fastapi import FastAPI
from Domain.Usuario.UsuarioModel import Usuario
app: FastAPI=FastAPI(title='SOA python security', description='IUEHE 2023')

###########################################################################

@app.get("/autenticarusuario",summary="Autenticar usuario",description="API para autenticar usuario",tags=["Autenticarusuario"])

async def autenticador_usuario(usuario:str | None= None, clave:str | None=None):
    salida:str=usuario+clave
    return salida

############################################################################


@app.post("/autenticarusuario",
          response_model=Usuario,
          summary="Autenticar Usuario",
          description="API para autenticar Usuario via POST",
          tags=["Autenticarusuario"]


)

async def autenticador_usuario(usuario:Usuario | None=None):
    usuario.salida=usuario.usuario + "-" + usuario.clave
    return usuario