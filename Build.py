  
from cx_Freeze import setup, Executable

setup(
    name = "ClientCESI",
    version = "1.0.0",
    description = "",
    executables = [Executable("Client.py")]
)