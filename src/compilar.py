"""
https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
"""
import glob,os,platform


class SistemaOperativo:

    def __init__(self):
        os.chdir(".")

    def get_SistemaOperativo(self):
        return platform.system()


    def cambiarPath(self,ruta):
        os.chdir(ruta)

    def imprimirDirectorio(self, ext="*"):
        for file in glob.glob("*."+ext):
            print(file)

so = SistemaOperativo()

if(so.get_SistemaOperativo() == 'Linux'):
   os.popen("./install.sh")
elif(so.get_SistemaOperativo() == 'Windows'):
    pass

elif(so.get_SistemaOperativo() == 'Mac'):
    pass

