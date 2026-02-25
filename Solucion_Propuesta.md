# Solución Propuesta: Sistema de Comunicación Máquina-a-Máquina (M2M) vía OPC-UA

## 1. Objetivo del Proyecto
Desarrollar un entorno de simulación basado en el estándar OPC-UA que demuestre la comunicación entre un Servidor (que representa una máquina industrial) y un Cliente (que representa un sistema de monitorización o SCADA).

## 2. Arquitectura del Sistema

### 2.1 Servidor OPC-UA (La Máquina)
Representa un "Horno Industrial" inteligente que expone los siguientes datos:
- **Temperatura:** Valor analógico simulado con variaciones realistas.
- **Presión:** Valor analógico.
- **Estado:** Variable booleana (Marcha/Paro).
- **Contador de Ciclos:** Valor entero que aumenta con el tiempo.
- **Métodos:** Un método para "Reiniciar el Contador" de forma remota.

### 2.2 Cliente OPC-UA (Monitorización)
Un script que se conecta al servidor y realiza:
- **Lectura de datos:** Obtención de los valores actuales.
- **Suscripción:** Recepción automática de cambios en la temperatura (basada en eventos).
- **Control:** Llamada al método de reinicio del servidor.

## 3. Tecnologías Utilizadas
- **Lenguaje:** Python 3.x.
- **Librería Core:** `asyncua` (Pure Python OPC-UA library).
- **Simulación:** Generación de datos sintéticos mediante lógica matemática (ruido gaussiano para temperatura).

## 4. Estructura de Datos (Address Space)
Se creará un nodo raíz llamado `HornoIndustrial` con una estructura jerárquica:
- `HornoIndustrial/Variables/Temperatura`
- `HornoIndustrial/Variables/Presion`
- `HornoIndustrial/Variables/Estado`
- `HornoIndustrial/Metodos/ResetContador`

## 5. Ventajas de esta Solución
1. **Interoperabilidad:** El servidor puede ser leído por cualquier cliente estándar (como UaExpert).
2. **Escalabilidad:** Es fácil añadir más máquinas o variables al espacio de direcciones.
3. **Seguridad:** Aunque es una demo, la arquitectura permite añadir certificados X.509 fácilmente.
