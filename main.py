import obd
import colorama
from colorama import Fore, Style

# Colored output
colorama.init()

# Functions
def status():
    # Connection
    connection = obd.OBD(portstr="COM6")
    # RPM
    rpmcmd = obd.commands.RPM
    rpmres = connection.query(rpmcmd)
    # Version
    vercmd = obd.commands.ELM_VERSION
    verres = connection.query(vercmd)
    # Voltage
    volcmd = obd.commands.ELM_VOLTAGE
    volres = connection.query(volcmd)
    # Engine Load
    loadcmd = obd.commands.ENGINE_LOAD
    loadres = connection.query(loadcmd)
    # Air Flow
    aircmd = obd.commands.MAF
    airres = connection.query(aircmd)
    # Fuel Status
    fuelcmd = obd.commands.FUEL_STATUS
    fuelres = connection.query(fuelcmd)
    # Fuel Type
    fueltcmd = obd.commands.FUEL_TYPE
    fueltres = connection.query(fueltcmd)

    if verres.is_null() or volres.is_null():
        print("No response from vehicle")
    else:
        print(Fore.GREEN + "==========" + Fore.RED + "Car Status" + Fore.GREEN + "==========")
        print(Fore.YELLOW + "Connection Established!" + Fore.GREEN)
        print("ELM372 Ver: ", verres.value)
        print("ELM372 Vol:", volres.value)
        print("RPM: ", rpmres.value)
        print("Engine Load: ", loadres.value)
        print("Air Flow: ", airres.value)
        print("Fuel Status: ", fuelres.value)
        print("Fuel Type: ", fueltres.value)

def dtc():
    # Connection
    connection = obd.OBD(portstr="COM6")
    # DTC
    dtcs = connection.query(obd.commands.GET_DTC)
    print(f"DTCs: {dtcs.value}")

choice = input("What you would to check? dtc or status?: ")

if choice.lower() == "status":
    status()
elif choice.lower() == "dtc":
    dtc()
