
<p align="center"> <strong>PORTAFOLIO DE CIBERSEGURIDAD · SEGURIDAD OFENSIVA</strong><br> Reconocimiento de red · Seguridad web · Análisis de servicios · Escalada de privilegios </p>

<p align="center"> <img src="https://img.shields.io/badge/Entorno-Laboratorio-0f766e?style=flat-square" alt="Entorno de laboratorio"> <img src="https://img.shields.io/badge/Enfoque-Pentesting-1d4ed8?style=flat-square" alt="Pruebas de penetración"> <img src="https://img.shields.io/badge/Estado-En%20documentación-d97706?style=flat-square" alt="En documentación"> </p>

---

## 1. Descripción del proyecto

Este repositorio documenta un ejercicio práctico de **pruebas de penetración sobre LazySysAdmin**, una máquina Linux vulnerable diseñada para el aprendizaje de ciberseguridad.

El proyecto recoge un proceso de evaluación técnica que incluye reconocimiento de red, enumeración de servicios, análisis de recursos compartidos, investigación de información expuesta en WordPress y comprobación de accesos y privilegios.

El objetivo es documentar las pruebas realizadas, analizar las implicaciones de seguridad de las evidencias obtenidas y proponer medidas correctivas siguiendo una metodología de elaboración de informes técnicos.

## 2. Alcance de la evaluación

- **Objetivo:** máquina de laboratorio LazySysAdmin.
    
- **Entorno:** laboratorio controlado y autorizado.
    
- **Sistema operativo objetivo:** Linux.
    
- **Tipo de actividad:** pruebas de penetración con fines educativos.
    
- **Áreas de análisis:** servicios de red, exposición de información, seguridad de aplicaciones web, credenciales y privilegios del sistema.
    

## 3. Metodología de trabajo

|Fase|Actividades realizadas|
|---|---|
|01. Reconocimiento|Descubrimiento de equipos e identificación del objetivo.|
|02. Enumeración de servicios|Escaneo de puertos e identificación de servicios y versiones.|
|03. Análisis de SMB|Identificación de recursos compartidos y revisión de archivos accesibles.|
|04. Análisis de WordPress|Investigación de información de configuración potencialmente sensible.|
|05. Comprobación de accesos|Pruebas de autenticación y validación de accesos.|
|06. Análisis de privilegios|Investigación del acceso SSH y comprobación de los permisos disponibles.|
|07. Documentación|Revisión de evidencias, análisis de riesgos y recomendaciones de mitigación.|

_Las fases describen el trabajo documentado en el laboratorio. Cada vulnerabilidad y cada transición de acceso deben validarse antes de presentarse como resultados confirmados._

## 4. Áreas de seguridad analizadas

- Exposición de servicios de red.
    
- Permisos y accesos a recursos compartidos.
    
- Exposición de información sensible y credenciales.
    
- Seguridad de la configuración de WordPress.
    
- Autenticación y acceso remoto mediante SSH.
    
- Permisos de usuario y posibles vías de escalada de privilegios.
    

## 5. Contenido del repositorio

- [Resumen ejecutivo](informe/RESUMEN_EJECUTIVO.md)
    
- [Hallazgos técnicos](informe/HALLAZGOS.md)
    
- [Evidencias de las pruebas](evidencias/)
    
- [Diagrama del recorrido de ataque](diagramas/recorrido-ataque.png)
    
- [Informe técnico completo en PDF](informe/Informe_Pentesting_LazyAdmin.pdf)
    

_Los enlaces se habilitarán a medida que se incorporen los archivos correspondientes al repositorio._

## 6. Herramientas utilizadas

`Kali Linux` · `Nmap` · `Netdiscover` · `SMBClient` · `Metasploit Framework` · `SSH`

## 7. Principales aprendizajes

Este ejercicio permite profundizar en la importancia de:

- Restringir el acceso a archivos de configuración y recursos compartidos.
    
- Proteger las credenciales y evitar su almacenamiento inseguro.
    
- Revisar los servicios expuestos y aplicar el principio de mínimo privilegio.
    
- Validar los accesos y permisos efectivos del sistema.
    
- Documentar los riesgos y definir medidas correctivas verificables.
    

## 8. Información del proyecto

- **Autora:** Manuela Salazar Moscoso.
    
- **Tipo de proyecto:** práctica formativa y portfolio de ciberseguridad.
    
- **Fecha de realización:** octubre de 2026.
    
- **Entorno:** laboratorio educativo autorizado.
    

---

### Aviso legal

**Este proyecto tiene exclusivamente fines educativos y de aprendizaje**. Las pruebas se han realizado en un entorno de laboratorio controlado y autorizado. Los resultados documentados no constituyen una auditoría de un sistema de producción.