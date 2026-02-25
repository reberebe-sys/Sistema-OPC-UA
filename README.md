# 🏭 Sistema Industrial OPC-UA 4.0
### Monitorización y Control en Tiempo Real con Python, FastAPI y Chart.js

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green.svg)](https://fastapi.tiangolo.com/)
[![OPC-UA](https://img.shields.io/badge/OPC--UA-Industry--4.0-orange.svg)](https://opcfoundation.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Este proyecto representa un ecosistema completo de **Industria 4.0** basado en el protocolo **OPC-UA (Unified Architecture)**. Implementa un servidor que emula una máquina industrial (Horno de Procesado), un backend de monitorización asíncrono y un dashboard web de alta fidelidad visual para el control operativo.

---

## 🌟 Características Destacadas

-   **📡 Comunicación en Tiempo Real:** Transmisión de datos mediante WebSockets para una latencia mínima.
-   **🛠️ Control Bidireccional:** Permite no solo visualizar, sino también ejecutar comandos remotos (RPC) sobre el servidor OPC-UA.
-   **📊 Visualización Avanzada:** Gráficas dinámicas con Chart.js y estética "Industrial Dark Mode".
-   **🔌 Interoperabilidad Total:** El servidor es compatible con clientes industriales estándar como **UaExpert**, **Ignition** o **Inductive Automation**.
-   **🏗️ Arquitectura Robusta:** Desarrollo asíncrono utilizando `asyncua` y `FastAPI` para un rendimiento optimizado.

---

## 📂 Componentes del Sistema

1.  **OPC-UA Server (`server_opcua.py`)**: 
    -   Simula un **Horno Industrial**.
    -   Expone variables críticas: Temperatura y Contador de Ciclos.
    -   Implementa métodos remotos (`ResetContador`).
2.  **Web Dashboard Backend (`web_dashboard.py`)**: 
    -   Actúa como puente (Bridge) entre el protocolo industrial (OPC-UA) y el protocolo web (WebSockets).
    -   Gestiona la API REST para comandos de control.
3.  **HMI Frontend (`index.html`)**: 
    -   Interfaz de usuario moderna y limpia.
    -   Actualización de datos en vivo sin refrescar la página.

---

## 🚀 Guía de Inicio Rápido

### 1. Clonar y Preparar el Entorno
```bash
# Instalar dependencias
pip install -r requirements.txt
```

### 2. Despliegue en 3 Pasos
Para ver el sistema en acción, abre tres terminales y ejecuta en orden:

1.  **Servidor Industrial**:
    ```bash
    python server_opcua.py
    ```
2.  **Puente Web-HMI**:
    ```bash
    python web_dashboard.py
    ```
3.  **Acceso Web**:
    Abre tu navegador en [http://localhost:8000](http://localhost:8000)

---

## 🛠️ Tecnologías Utilizadas

-   **Lenguaje:** Python 3.9+
-   **Stack Industrial:** `asyncua` (OPC-UA asyncio).
-   **Stack Web:** FastAPI, Uvicorn, WebSockets.
-   **Frontend:** HTML5, CSS3 (Glassmorphism), JavaScript (ES6+), Chart.js.
-   **Estilo:** Fuentes Orbitron y Paleta de colores industriales Slate/Sky.

---

## 📘 Documentación Técnica Adicional

Para más detalles, puedes consultar los siguientes archivos en este repositorio:
-   [Manual de Uso](./MANUAL_USO.md): Guía paso a paso avanzada.
-   [Investigación OPC-UA](./Investigacion_OPC_UA.md): Análisis técnico del protocolo en 2025.
-   [Solución Propuesta](./Solucion_Propuesta.md): Diagrama lógico y decisiones de arquitectura.

---

## 👤 Autor
Desarrollado por **reberebe-sys** para la comunidad de automatización industrial y software libre.

---

> **Nota:** Este proyecto se encuentra bajo la licencia MIT. Siéntete libre de usarlo, modificarlo y compartirlo para tus propios desarrollos industriales.
