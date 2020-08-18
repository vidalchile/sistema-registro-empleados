# sistema-registro-empleados
Sistema de registro de empleados.

Proyecto básico realizado con:
* Python 3.6.8
* Django 3.0
* PostgreSQL 10.10
* Foundation 6.6.3

(Proyecto realizado en sistema operativo linux mint)

Ir a la carpeta donde estará el proyecto
```bash
cd /var/www/html/
```

Obtener el código fuente ejecutando:
```bash
git clone https://github.com/vidalchile/sistema-registro-empleados.git
```

Ir a la carpeta del proyecto  y crear ambiente virtual de python3.6

Opción 1 para crear ambiente virtual
```bash
cd /var/www/html/sistema-registro-empleados
python3.6 -m venv env
```

Activar el ambiente virtual en el terminal actual

`source env/bin/activate`

Opcion 2 para crear ambiente virtual
```bash
virtualenv -p /usr/bin/python3  /var/www/html/sistema-registro-empleados/env
```
Activar el ambiente virtual
```bash
source /var/www/html/sistema-registro-empleados/env/bin/activate
```

Instalar los requerimientos del proyecto

```bash
pip install pip --upgrade
pip install -r requirements.txt
```

#### Ejecutar proyecto
```bash
cd /var/www/html/sistema-registro-empleados
python manage.py runserver
```
