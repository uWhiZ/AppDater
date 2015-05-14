from core.appdater import AppDater

def main():
	appname = "RAT"
	version = "1.0"

	appdater = AppDater(appname, version)

	# Actualizar aplicación
	appdater.run("appdate")

	# Consultar temas disponibles
	uiList = appdater.run("uicheck")

	# Actualizar temas
	appdater.run("uidate")

	# Consultar idiomas disponibles
	uiLang = appdater.run("langcheck")

	# Actualizar idiomas
	appdater.run("langdate")

if __name__ == "__main__":
	main()