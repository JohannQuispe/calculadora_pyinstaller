# calculadora_pyinstaller
DEMO Instalador(Despliegue) de una aplicacion basica con pyInstaller, como parte del modulo de Fundamentos de la ingenieria de Software

## Run project
- En el directorio del proyecto trabajo(al nivel de trabajo.py) ejecutar por consola
~~~bash  
python3 ./trabajo.py
~~~ 

## Build installer
- En el directorio del proyecto trabajo(al nivel de trabajo.py) ejecutar por consola
~~~bash  
pyinstaller --onefile --name trabajo --icon=calc.ico trabajo.py
~~~  