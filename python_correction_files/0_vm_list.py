from pyVim.connect import SmartConnect
from pyVmomi import vim


def main():
    service_instance = SmartConnect(host="10.144.208.13", user="root", pwd="PE3h3r$!", disableSslCertValidation=True)

    print("ESXi/vCenter Time")
    print(" - %s" % service_instance.CurrentTime())
    content = service_instance.RetrieveServiceContent()
    container = content.rootFolder

    view_type = [vim.VirtualMachine]
    recursive = True

    container_view = content.viewManager.CreateContainerView(
        container, view_type, recursive
    )
    vm_list = container_view.view

    print("VM List:")
    for vm in vm_list:
        print(" - " + vm.name)


if __name__ == "__main__":
    main()
