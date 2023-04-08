# Check for supported command pids between package and ECU/OBD

import obd

connection = obd.OBD(portstr="COM6")

supported = connection.supported_commands

for cmd in supported:
    print(cmd)
