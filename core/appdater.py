from coreDater import CoreDater
from uiDater import UiDater
from langDater import LangDater
from exceptionHandler import ExceptionHandler

class AppDater(object):
    """Interfaz de actualización para las underc0de tools"""

    def __init__(self, appname, version, debug=False):
        self.__debug = debug

        # Instancias
        self.__coreDater = CoreDater(appname, version)
        self.__uiDater = UiDater(appname, version)
        self.__langDater = LangDater(appname, version)
        self.__exceptionHandler = ExceptionHandler()
    

    def run(run, args=[]):
        """Ejecuta una acción según el comando recibido.

            - coreupdate -> actualiza app
            - uicheck -> verifica temas disponibles
            - uiupdate -> instala temas seleccionados
            - langcheck -> verifica idiomas disponibles
            - langupdater -> instala idiomas seleccionados
        """
        try:	
            if run == "coreupdate":
                self.__coreDater.run()
            elif run == "uicheck":
                uiList = self.__uiDater.check()
                return uiList
            elif run =="uiupdate":
                self.__uiDater.update(args)
            elif run == "langcheck":
                langList = self.__langDater.check()
                return langList
            elif run == "langupdate":
                self.__langDater.update(args)
            else:
                return None

        except Exception as e:
            if self.__debug:
                self.__exceptionHandler.showError(e)
