from pymodbus.client.sync import ModbusTcpClient
import logging

# Setup logging (set before logging anything)
logging.basicConfig(filename='modbus_log.txt', level=logging.INFO, format='%(asctime)s %(message)s')

# Connect to Factory I/O Modbus server
client = ModbusTcpClient('127.0.0.1', port=502)
client.connect()

# Read 10 discrete inputs starting at address 0
result = client.read_discrete_inputs(address=0, count=10, unit=1)

if result.isError():
    logging.error(f"Read error: {result}")
else:
    logging.info(f"Read values: {result.bits}")

client.close()
