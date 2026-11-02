
## 1. Introducción

Este documento describe la metodología seguida durante la evaluación de seguridad de la máquina **LazySysAdmin**, un entorno Linux vulnerable utilizado con fines educativos para practicar técnicas de reconocimiento, enumeración de servicios, identificación de información sensible y escalada de privilegios.

La evaluación se ha desarrollado siguiendo un enfoque progresivo: comenzar con la recopilación de información del objetivo, identificar los servicios disponibles, analizar posibles configuraciones inseguras y comprobar si la información obtenida permite acceder a recursos o privilegios adicionales.

El propósito de esta metodología es documentar de forma estructurada las actividades realizadas, las herramientas utilizadas y los resultados obtenidos, manteniendo la trazabilidad entre las pruebas y las evidencias.

## 2. Alcance y condiciones de las pruebas

La evaluación se ha realizado exclusivamente sobre una máquina de laboratorio autorizada.

|Parámetro|Descripción|
|---|---|
|Sistema objetivo|LazySysAdmin|
|Sistema analista|Kali Linux|
|Tipo de evaluación|Pruebas de penetración|
|Modalidad|Laboratorio controlado|
|Fecha de realización|26 de octubre de 2026|
|Objetivo|Identificar debilidades de configuración y comprobar su impacto|

Las actividades se han limitado al entorno de prácticas. No se han realizado pruebas sobre sistemas de terceros ni sobre infraestructuras de producción.

## 3. Metodología de evaluación

El proceso se ha dividido en seis fases principales.

### Fase 1. Reconocimiento de red

**Objetivo:** identificar los dispositivos presentes en la red del laboratorio y localizar la máquina objetivo.

Se utilizaron las siguientes herramientas:

- `Netdiscover`: descubrimiento de dispositivos mediante técnicas de reconocimiento ARP.
    
- `Nmap`: identificación de hosts activos y comprobación de disponibilidad.
    

Entre las pruebas realizadas se encuentran:

```
netdiscover
nmap -sn <rango_de_red> 
nmap -PR <rango_de_red>
```

Durante esta fase se buscó identificar:

- Direcciones IP de los dispositivos activos.
    
- Direcciones MAC detectadas.
    
- Disponibilidad del equipo objetivo.
    
- Información inicial sobre la red.
    

**Resultado esperado:** identificar la dirección IP correspondiente a LazySysAdmin para continuar con las pruebas de enumeración.

### Fase 2. Enumeración de puertos y servicios

**Objetivo:** identificar los puertos abiertos y los servicios que se encuentran disponibles en la máquina objetivo.

Se utilizó Nmap para realizar un escaneo completo de puertos TCP e intentar identificar las versiones de los servicios detectados.

Comando utilizado:

```
nmap -sV -p- <IP_OBJETIVO>
```

Se analizaron especialmente los siguientes aspectos:

- Puertos TCP abiertos.
    
- Servicios asociados a cada puerto.
    
- Versiones identificadas.
    
- Posibles puntos de entrada para continuar la evaluación.
    

La información obtenida permitió definir las siguientes líneas de investigación, prestando especial atención a los servicios SMB, HTTP, SSH y MySQL cuando aparecieron en el escaneo.

**Resultado:** identificación de la superficie de exposición de la máquina y selección de los servicios que requerían una enumeración más detallada.

### Fase 3. Enumeración de recursos compartidos SMB

**Objetivo:** comprobar si existían recursos compartidos accesibles y determinar qué información podía consultarse a través del servicio SMB.

Se utilizó `smbclient` para enumerar los recursos compartidos y comprobar las posibilidades de acceso.

Comando de referencia utilizado:

```
smbclient -L //<IP_OBJETIVO> -N
```

La opción `-N` permite realizar la conexión sin proporcionar una contraseña.

Una vez identificados los recursos disponibles, se investigó el contenido de los directorios y archivos accesibles.

Se prestó especial atención a:

- Archivos de configuración.
    
- Directorios relacionados con WordPress.
    
- Documentos internos.
    
- Archivos que pudieran contener información sensible.
    
- Posibles credenciales almacenadas.
    

**Resultado:** durante esta fase se identificó información relevante en los recursos compartidos, incluida una contraseña almacenada en texto plano y archivos relacionados con la configuración de WordPress.

Este descubrimiento permitió ampliar la investigación hacia la posible exposición de credenciales y la reutilización de información de autenticación.

### Fase 4. Análisis de WordPress e información sensible

**Objetivo:** analizar los archivos relacionados con WordPress encontrados durante la enumeración SMB y comprobar si contenían información sensible.

Se prestó especial atención al archivo:

```
wp-config.php
```

Este archivo contiene parámetros de configuración de WordPress y puede incluir información de conexión a la base de datos.

Durante el análisis se revisó:

- La estructura de los archivos de configuración.
    
- La posible presencia de usuarios y contraseñas.
    
- La exposición de información de conexión a MySQL.
    
- La posible reutilización de credenciales en otros servicios.
    

Se identificaron credenciales almacenadas en un archivo de configuración accesible desde el recurso compartido.

Este hallazgo se consideró especialmente relevante porque la exposición de información de autenticación puede facilitar el acceso no autorizado a otros componentes del sistema.

**Resultado:** obtención de información de autenticación que permitió continuar con las pruebas de validación de acceso.

Por motivos de seguridad, las credenciales originales no se reproducen en este documento ni en las evidencias públicas del repositorio.

### Fase 5. Validación de credenciales y acceso remoto

**Objetivo:** comprobar si la información de autenticación obtenida durante las fases anteriores permitía acceder a otros servicios de la máquina.

Se realizaron pruebas sobre el entorno de laboratorio para verificar la validez de las credenciales y sus posibilidades de utilización.

Durante esta fase se utilizaron:

- El panel de administración de WordPress.
    
- Metasploit Framework mediante `msfconsole`.
    
- El servicio SSH para comprobar el acceso remoto al sistema.
    

La investigación permitió comprobar que las credenciales obtenidas podían utilizarse para acceder a otros componentes del entorno.

Posteriormente, se consiguió establecer una conexión SSH con una cuenta del sistema.

Se documentó:

- El servicio al que se consiguió acceder.
    
- La cuenta utilizada, anonimizada en las evidencias públicas.
    
- La validación del acceso remoto.
    
- Los permisos disponibles para el usuario autenticado.
    

Es importante diferenciar los intentos de explotación realizados con Metasploit del acceso remoto que finalmente se consiguió mediante SSH. El acceso obtenido debe atribuirse únicamente al mecanismo que las evidencias permitan demostrar.

**Resultado:** acceso remoto al sistema mediante SSH con una cuenta de usuario válida.

### Fase 6. Análisis de privilegios y comprobación de escalada

**Objetivo:** determinar qué privilegios tenía la cuenta obtenida y comprobar si existía alguna configuración que permitiera alcanzar privilegios administrativos.

Una vez establecida la sesión SSH, se investigaron los permisos asociados al usuario y las posibilidades de ejecución de comandos con privilegios elevados.

Se utilizó el siguiente comando:

```
sudo -l
```

Este comando permite consultar qué operaciones puede ejecutar un usuario mediante `sudo`.

Durante la evaluación se identificó una configuración de privilegios excesivamente permisiva, que permitía al usuario ejecutar acciones con privilegios administrativos.

Posteriormente, se comprobó la posibilidad de acceder al contexto del usuario administrador del sistema mediante:

```
sudo su
```

Finalmente, se verificó el acceso al directorio `/root` y al archivo `proof.txt`, utilizado como evidencia de la finalización de la máquina.

**Resultado:** se consiguió alcanzar privilegios de administrador del sistema, demostrando el impacto de una configuración incorrecta de permisos.

## 4. Análisis de la cadena de ataque

La evaluación permitió documentar una secuencia de acciones en la que la información obtenida en una fase facilitó el avance hacia la siguiente.

El recorrido general fue el siguiente:

1. Identificación de la máquina objetivo mediante reconocimiento de red.
    
2. Enumeración de puertos y servicios disponibles.
    
3. Identificación de recursos SMB accesibles.
    
4. Descubrimiento de archivos e información sensible.
    
5. Obtención de credenciales almacenadas en archivos de configuración.
    
6. Validación de las credenciales en otros servicios.
    
7. Acceso remoto mediante SSH.
    
8. Identificación de permisos `sudo` excesivos.
    
9. Obtención de privilegios administrativos.
    
10. Comprobación del acceso al archivo `proof.txt`.
    

Esta secuencia demuestra cómo varias debilidades de configuración pueden combinarse y generar un compromiso completo del sistema.

## 5. Herramientas utilizadas

|Herramienta|Finalidad|
|---|---|
|Kali Linux|Entorno de trabajo para las pruebas|
|Netdiscover|Descubrimiento de dispositivos en la red|
|Nmap|Escaneo de puertos y enumeración de servicios|
|SMBClient|Enumeración y acceso a recursos compartidos SMB|
|Metasploit Framework|Realización de pruebas de seguridad sobre el entorno|
|SSH|Validación de acceso remoto al sistema|
|Sudo|Comprobación de permisos y privilegios administrativos|

## 6. Criterios de documentación y evidencias

Para garantizar la trazabilidad de la evaluación, cada fase debe contar con evidencias que permitan verificar las actividades realizadas y sus resultados.

Las evidencias se organizarán mediante identificadores consecutivos:

|Identificador|Evidencia|
|---|---|
|E-01|Descubrimiento de dispositivos mediante Netdiscover|
|E-02|Identificación de hosts activos mediante Nmap|
|E-03|Escaneo de puertos y servicios|
|E-04|Enumeración de recursos compartidos SMB|
|E-05|Identificación de archivos e información sensible|
|E-06|Análisis de configuración de WordPress|
|E-07|Pruebas de validación de acceso|
|E-08|Acceso remoto mediante SSH|
|E-09|Enumeración de privilegios mediante sudo|
|E-10|Comprobación de acceso al directorio root y proof.txt|

Las capturas deberán mostrar únicamente la información necesaria para justificar cada resultado.

No se publicarán contraseñas, hashes reutilizables, tokens, claves privadas ni otros secretos obtenidos durante las pruebas.

## 7. Consideraciones de seguridad

Los resultados obtenidos en un entorno de laboratorio no deben extrapolarse automáticamente a sistemas reales.

Las observaciones se clasificarán como hallazgos confirmados únicamente cuando exista evidencia suficiente que permita demostrar su existencia y su impacto.

Las recomendaciones de mitigación se formularán teniendo en cuenta:

- El principio de mínimo privilegio.
    
- La restricción de acceso a recursos compartidos.
    
- El almacenamiento seguro de credenciales.
    
- La protección de archivos de configuración.
    
- La revisión de los permisos de cuentas locales.
    
- La supervisión de servicios expuestos.
    
- La validación periódica de las medidas correctivas.
    

## 8. Conclusión

La práctica realizada sobre LazySysAdmin permitió aplicar un proceso estructurado de pruebas de penetración, desde el reconocimiento inicial hasta la obtención de privilegios administrativos.

Uno de los principales aprendizajes ha sido comprobar que una enumeración exhaustiva puede revelar información de gran valor para un análisis de seguridad, incluso sin recurrir necesariamente a técnicas avanzadas de explotación.

La exposición de recursos compartidos, el almacenamiento inseguro de credenciales y la asignación excesiva de privilegios pueden combinarse y facilitar el compromiso completo de un sistema.

Esta práctica refuerza la importancia de aplicar configuraciones seguras, proteger la información sensible y revisar periódicamente los permisos y servicios disponibles en los sistemas Linux.

---

**Proyecto:** LazySysAdmin — Pruebas de penetración  
**Autora:** Manuela Salazar Moscoso  
**Tipo de actividad:** Laboratorio educativo de ciberseguridad  
**Fecha:** 26 de octubre de 2026