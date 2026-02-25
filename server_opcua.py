import asyncio
import logging
import random
import math
from asyncua import ua, Server
from asyncua.common.methods import uamethod

# Configuración de logs
logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)

# Estado global de la máquina
machine_state = {"count": 0}

@uamethod
def reset_counter(parent):
    _logger.info(">>> Comando remoto: RESET del contador recibido.")
    machine_state["count"] = 0
    return True

async def main():
    # Inicialización del servidor
    server = Server()
    await server.init()
    
    # Endpoint y nombre
    url = "opc.tcp://127.0.0.1:4848/freeopcua/server/"
    server.set_endpoint(url)
    server.set_server_name("Servidor Horno Industrial v1.0")
    
    # Registro de Namespace
    uri = "http://antigravity.ia/opcua"
    idx = await server.register_namespace(uri)

    # Estructura de Objetos
    # Objeto principal: Horno
    horno = await server.nodes.objects.add_object(idx, "HornoIndustrial")
    
    # Carpeta de Variables (Datos)
    vars_folder = await horno.add_folder(idx, "Variables")
    temp_v = await vars_folder.add_variable(idx, "Temperatura", 20.0, ua.VariantType.Double)
    pres_v = await vars_folder.add_variable(idx, "Presion", 1.0, ua.VariantType.Double)
    ciclos_v = await vars_folder.add_variable(idx, "ContadorCiclos", 0, ua.VariantType.Int64)
    
    # Carpeta de Operaciones (Métodos)
    ops_folder = await horno.add_folder(idx, "Operaciones")
    await ops_folder.add_method(idx, "ResetContador", reset_counter, [], [ua.VariantType.Boolean])

    # Habilitar escritura en temperatura (para pruebas)
    await temp_v.set_writable()

    _logger.info(f"Servidor OPC-UA listo en: {url}")
    
    async with server:
        _logger.info("Sistema en ejecución. Esperando conexiones de clientes...")
        while True:
            await asyncio.sleep(1)
            
            # SIMULACIÓN DE FÍSICA
            # Temperatura oscila entre 50 y 60 grados
            new_t = 55 + 5 * math.sin(machine_state["count"] / 10) + random.uniform(-0.5, 0.5)
            # Presión estable con ruido térmico
            new_p = 2.0 + random.uniform(-0.1, 0.1)
            
            # Escritura de valores en los nodos
            await temp_v.write_value(new_t)
            await pres_v.write_value(new_p)
            
            # Incrementar contador global
            machine_state["count"] += 1
            await ciclos_v.write_value(machine_state["count"])
            
            if machine_state["count"] % 10 == 0:
                _logger.info(f"STATUS -> T: {new_t:.2f}ºC | P: {new_p:.2f}bar | Ciclos: {machine_state['count']}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        _logger.info("Servidor detenido por el usuario.")
    except Exception as e:
        _logger.error(f"Fallo en el servidor: {e}")
