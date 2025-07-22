from os import system
from platform import platform
from subprocess import DEVNULL, run
from sys import exit


def init_project():
    the_platform = platform().lower()
    system("cls" if "windows" in the_platform else "clear")

    if input("Deseas iniciar este programa? [Y/n]: ").lower() != "y":
        exit()

    if input("Deseas iniciar un entorno virtual? [Y/n]: ").lower() == "y":
        print("Creando entorno virtual...")
        run("python -m venv venv", stdout=DEVNULL, stderr=DEVNULL)
        print("Entorno virtual creado!\n")
        print("Iniciando entorno virtual...")
        run(
            (
                "venv\\Scripts\\activate.bat"
                if "windows" in the_platform
                else "source venv/bin/activate"
            ),
            stdout=DEVNULL,
            stderr=DEVNULL,
        )
        print("Entorno virtual iniciado!\n")

    with open("requirements.txt", "r") as f:
        print("Instalando dependencias...")
        for line in f.readlines():
            print(f'Instalado: {line.split('\n')[0]}... ', end="")
            run(f"pip install {line}", stdout=DEVNULL, stderr=DEVNULL)
            print("[OK!]")
    f.close()
    print("Instalacion de dependencias terminado!\n")

    if input("Deseas iniciar el script? [Y/n]: ").lower() != "y":
        exit()
    system("cls" if "windows" in the_platform else "clear")
    system("py .\\index.py" if "windows" in the_platform else "python3 ./index.py")


if __name__ == "__main__":
    try:
        init_project()
    except KeyboardInterrupt:
        print("\nAdios!")
    except Exception as e:
        print(f"Ah ocurrido un error en el script!\n{e}")
        exit()
