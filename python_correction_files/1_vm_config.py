import utils

def main():
    # Connection to the vCenter
    content = utils.connect()
    # Get the VM (see utils.py)
    virtual_machine = utils.get_vm(content)

    print("VM Name: {0}".format(virtual_machine.name))
    print("PowerState: {0}".format(virtual_machine.summary.runtime.powerState))
    print("Firmware: {0}".format(virtual_machine.config.firmware))
    print("Memory size: {0}".format(virtual_machine.config.hardware.memoryMB))
    print("Number of CPUs: {0}".format(virtual_machine.config.hardware.numCPU))


if __name__ == "__main__":
    main()
