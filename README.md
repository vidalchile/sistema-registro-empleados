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

Ir a la carpeta del proyecto

```bash
cd /var/www/html/sistema-registro-empleados
```

Crear ambiente virtual de python3.6

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

Luego de haber ejecutado el proyecto, se puede acceder desde la ruta: http://127.0.0.1:8000
