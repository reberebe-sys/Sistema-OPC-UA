# Manual de Uso: Sistema de Comunicación OPC-UA

Este sistema simula una comunicación máquina-a-máquina (M2M) utilizando el estándar industrial OPC-UA.

## 1. Requisitos Previos

Asegúrate de tener Python 3.8+ instalado y las librerías necesarias. Puedes instalarlas ejecutando:

```bash
pip install -r requirements.txt
```

## 2. Ejecución del Sistema

El sistema se compone de dos partes: el Servidor (la máquina) y el Cliente (el monitor).

### Paso 1: Iniciar el Servidor
Abre una terminal y ejecuta:
```bash
python server_opcua.py
```
El servidor creará un espacio de direcciones en `opc.tcp://127.0.0.1:4840/freeopcua/server/`.

### Paso 2: Iniciar el Cliente
Abre una **segunda terminal** y ejecuta:
```bash
python client_opcua.py
```

## 3. Pruebas Externas (Recomendado)

Una de las grandes ventajas de OPC-UA es su interoperabilidad. Puedes usar herramientas de terceros para verificar el servidor:

1.  **UaExpert:** Descarga e instala [UaExpert](https://www.unified-automation.com/products/client-cpp-sdk/uaexpert.html).
2.  **Conexión:** Añade un nuevo servidor con la URL: `opc.tcp://127.0.0.1:4840/freeopcua/server/`.
3.  **Exploración:** Podrás ver la estructura `HornoIndustrial`, arrastrar las variables a la vista de datos y ver las gráficas en tiempo real.

## 4. Estructura de Datos
- **Temperatura:** Fluctúa entre 40°C y 60°C.
- **Presión:** Estable alrededor de 2.5 bar con ruido aleatorio.
- **Contador:** Aumenta cada segundo (resetable desde el cliente).
- **Estado:** Indica "True" (Encendido) si la temperatura supera los 45°C.

## 5. Solución de Problemas
- **Puerto Ocupado:** Si el servidor no arranca, asegúrate de que el puerto 4840 no esté siendo usado por otra aplicación.
- **Conexión Rechazada:** Verifica que el servidor esté encendido antes de arrancar el cliente.
- **Certificados:** Esta versión utiliza seguridad básica (sin cifrado) para facilitar las pruebas. En producción, se recomienda configurar certificados X.509.
