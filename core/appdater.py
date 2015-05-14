from coreDater import CoreDater
from uiDater import UiDater
from langDater import LangDater
from exceptionHandler import ExceptionHandler

class AppDater(object):
    def __init__(self, appname, version, debug=False):
        self.__debug = debug

        # Instancias
        self.__coreDater = CoreDater(appname, version)
        self.__uiDater = UiDater(appname, version)
        self.__langDater = LangDater(appname, version)
        self.__exceptionHandler = ExceptionHandler()
    

    def run(run, args=[]):
        try:	
            if run == "coredater":
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

def main():
    appname = "RAT"
    version = "1.0"
    appDater = AppDater(appname, version, True)
    
    # CoreDater
    appDater.run("coredater")
    
    # UiDater
    uiList = appDater.run("uicheck")
    newUiList = uiList[2, 4]
    appDater.run("uiupdate", newUiList)
    
    # LangDater
    langList = appDater.run("langcheck")
    newLangList = langList[1, 3]
    appDater.run("langupdate", newLangList)

if __name__ == "__main__":
    main()
