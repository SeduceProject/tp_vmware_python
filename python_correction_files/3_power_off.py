import utils


def main():
    # Connection to the vCenter
    content = utils.connect()
    # Get the VM (see utils.py)
    virtual_machine = utils.get_vm(content)

    virtual_machine.PowerOff()


if __name__ == "__main__":
    main()
