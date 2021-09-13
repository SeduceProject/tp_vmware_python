from pyVim.connect import SmartConnect
from pyVmomi import vim


def connect():
    """
    Connexion to ESXi/vCenter. 
     - host: the IP or hostname of the ESXi/vCenter
     - user: ESXi/vCenter user
     - pwd: ESXi/vCenter password
    """
    service_instance = SmartConnect(host="10.144.208.13", user="root", pwd="PE3h3r$!", disableSslCertValidation=True)
    return service_instance.RetrieveServiceContent()


def get_vm(content, vm_name = None):
    """
    Get the VM from its name
     - content: the vmWare ServiceContent
     - vm_name (optional): the name of the VM to retrieve
    """
    if vm_name is None:
        vm_name = "fileserver"
    container = content.rootFolder
    view_type = [vim.VirtualMachine]
    recursive = True

    container_view = content.viewManager.CreateContainerView(
        container, view_type, recursive
    )
    vm_list = container_view.view
    for vm in vm_list:
        if vm.name == vm_name:
            return vm
