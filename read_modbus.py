from pymodbus.client.sync import ModbusTcpClient

# Connect to Factory I/O Modbus server
client = ModbusTcpClient('127.0.0.1', port=502)
client.connect()

# Read 10 discrete inputs starting at address 0
result = client.read_discrete_inputs(address=0, count=10, unit=1)

if result.isError():
    print("Read error:", result)
else:
    print("Discrete Inputs:", result.bits)

client.close()
