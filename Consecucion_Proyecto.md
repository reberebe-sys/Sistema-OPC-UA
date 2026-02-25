# Consecución del Proyecto: Sistema OPC-UA

Este documento detalla los pasos seguidos para la implementación del sistema de comunicación industrial.

## Fase 1: Investigación y Diseño (Finalizado)
- [x] Investigación sobre el estado de OPC-UA en 2024-2025.
- [x] Definición del stack tecnológico (Python + `asyncua`).
- [x] Diseño del espacio de direcciones (Address Space) para la máquina simulada.

## Fase 2: Desarrollo del Servidor (Finalizado)
- [x] Implementación del servidor básico con `asyncua`.
- [x] Creación de nodos y variables (Temperatura, Presión, Estado).
- [x] Implementación de la lógica de simulación de datos.
- [x] Programación de métodos (Reset de contador).

## Fase 3: Desarrollo del Cliente (Finalizado)
- [x] Implementación de la conexión asíncrona al servidor.
- [x] Lógica de lectura de variables en bucle.
- [x] Implementación de suscripciones (monitoreo de cambios).
- [x] Prueba de invocación de métodos remotos.

## Fase 4: Documentación y Pruebas (Finalizado)
- [x] Creación de `README.md` con descripción general.
- [x] Elaboración del `MANUAL_USO.md`.
- [x] Verificación de la comunicación M2M local.
- [x] Preparación del archivo `requirements.txt`.

## Próximos Pasos Sugeridos
- Implementar seguridad mediante certificados X.509.
- Integrar el sistema con una base de datos (InfluxDB) y Grafana.
- Crear una interfaz web (Streamlit) para visualizar los datos en tiempo real.
