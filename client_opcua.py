import asyncio
import logging
from asyncua import Client, ua

# Configuración de logs
logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)

# Manejador de eventos para la suscripción
class SubscriptionHandler:
    async def datachange_notification(self, node, val, data):
        """Este método se ejecuta automáticamente cuando la temperatura cambia en el servidor"""
        _logger.info(f"--- EVENTO: Cambio en {node} -> Nuevo valor: {val:.2f} ---")

async def main():
    url = "opc.tcp://127.0.0.1:4848/freeopcua/server/"
    
    _logger.info(f"Conectando a {url} usando Python 3.12...")
    
    try:
        async with Client(url=url) as client:
            _logger.info("¡Conexión exitosa al servidor!")
            
            # 1. Obtener el índice del Namespace
            idx = await client.get_namespace_index("http://antigravity.ia/opcua")
            
            # 2. Localizar Nodos Importantes
            root = client.nodes.objects
            horno = await root.get_child(f"{idx}:HornoIndustrial")
            vars_f = await horno.get_child(f"{idx}:Variables")
            
            temp_n = await vars_f.get_child(f"{idx}:Temperatura")
            ciclos_n = await vars_f.get_child(f"{idx}:ContadorCiclos")
            
            # 3. Configurar Suscripción (Recibir datos sin preguntar)
            handler = SubscriptionHandler()
            sub = await client.create_subscription(500, handler)
            await sub.subscribe_data_change(temp_n)
            _logger.info("Suscripción a 'Temperatura' activada correctamente.")

            # 4. Bucle de Monitoreo (Lectura de Ciclos y Reset)
            for i in range(15):
                # Leemos los ciclos manualmente para el informe
                c_val = await ciclos_n.read_value()
                t_val = await temp_n.read_value()
                
                print(f"[Monitor {i+1}] Temperatura: {t_val:.2f}ºC | Ciclos en máquina: {c_val}")
                
                # Al llegar al paso 6, enviamos un RESET remoto
                if i == 5:
                    _logger.info(">>> Enviando comando de RESET al servidor...")
                    ops_f = await horno.get_child(f"{idx}:Operaciones")
                    reset_m = await ops_f.get_child(f"{idx}:ResetContador")
                    
                    # Llamamos al método en el objeto 'horno'
                    resultado = await horno.call_method(reset_m)
                    _logger.info(f"Orden de RESET completada. Respuesta: {resultado}")
                
                await asyncio.sleep(2)
            
            _logger.info("Prueba de comunicación finalizada con éxito.")

    except Exception as e:
        _logger.error(f"Fallo en el cliente: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
