---

type: lab  
title: "Sin título"  
date: "2026-10-11"  
status: in-progress  
difficulty:  
category:  
tools:  
tags:

- cybersecurity
    
- lab
    

---

# 🛡️ Preparación de entorno

## 🎯 Objetivo

### ¿Qué voy a conseguir?

Configurar el esquema de laboratorio virtual conectando una maquina virtual vulnerable, que sea independiente de mi entorno (usuario) para no comprometer la seguridad de mi equipo.
### ¿Por qué es importante?

Se trabajara con una maquina virtual con problemáticas predefinidas, en este caso será la Metasploitable 2, la cual tiene brechas de seguridad como credenciales débiles, backdoors, servicios obsoletos y programas vulnerables.

---

# 🧠 Conceptos previos

Antes de comenzar, necesito comprender:

### Conceptos relacionados

- [[PILARES DE CIBERSEGURIDAD]]
    
- Maquinas virtuales
    
- Linux
    

---

# 🖥️ Entorno del laboratorio

| Elemento          | Información |
| ----------------- | ----------- |
| Sistema operativo | Kali        |
| Máquina virtual   | kali        |
| IP / Red          | 10.1.24.0   |
| Herramientas      | VMware      |
| Versiones         | 25H2        |
| Recursos          |             |

### Arquitectura
Este es el objetivo final al que se quiere llegar pero este es solo el primer paso.![[Pasted image 20261011185412.png]]
---

# ⚙️ Preparación

## Paso 1 —

La configuración del DHCP en VMware Linux, es modificando el fichero dhcp.conf de cada interfaz, VMware permite esta modificación en la interfaz grafica con los permisos de administrador del sistema.
![[Captura de pantalla 2026-10-08 190122.png]]

## Paso 2 —

Crear las maquinas virtuales, en mi caso un kali que hara la explotación y una Metasploitable 2 descargada del siguiente link: https://information.rapid7.com/metasploitable-download.html
después de extraer su contenido y abrirla con el software de virtualización, procedo a editar los adaptadores de red, para que estén en la misma red.
![[Captura de pantalla 2026-10-08 190639.png]]
## Paso 3 —

Descripción:
He renombrado el host de la kali por comodidad del tutor que lo revisará. usando el comando:
==*hostnamectl set-hostname kaliManuelaSalazar*==

y también editando el archivo /etc/hosts con el comando:
==*sudo nano /etc/hosts*==

![[Captura de pantalla 2026-10-08 180828.png]]

![[Captura de pantalla 2026-10-08 180937.png]]
---

# 🔧 Implementación

## Configuración

Consulte las IPs de ambas maquinas:
-En Kali: *==ip a==*
-en Metasploitable2: *==ifconfig==*
![[Pasted image 20261011191622.png]]
---

# 🔍 Pruebas

## Prueba 1

### Objetivo

Establecer conexión entre ambas maquinas.

### Acción

### Resultado esperado

ejecutar el comando ping desde kali con la ip 10.1.24.128 correspondiente a la maquina Metasploitable2

### Resultado obtenido
 Conexión exitosa
...

📸 Evidencia:

![[Captura de pantalla 2026-10-08 185016.png]]


---

# 🔐 Consideraciones de seguridad

### Riesgos identificados

| Riesgo                                                                                         | Impacto                                                         | Mitigación                                                           |
| ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | -------------------------------------------------------------------- |
| Si se conecta al equipo principal o con acceso a internet puede habe runa vulneracion de datos | robo de credenciales, tarjetas de credito, informacion personal | usar siempre en maquina virtual desechable, sin conexion a internet. |


---

# 🧩 Lo que he aprendido

### Conceptos nuevos
Virtualización, edición de red
### Lo que ahora sé hacer
Configurar redes virtuales.
### Lo que todavía necesito reforzar
Mejorar en Linux y compren mejor los conceptos de DCHP

---
