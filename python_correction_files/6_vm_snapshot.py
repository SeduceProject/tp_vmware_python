import utils


def main():
    # Connection to the vCenter
    content = utils.connect()
    # Get the VM (see utils.py)
    virtual_machine = utils.get_vm(content)

    # Snapshot the VM
    snapshot_name = "Snap_01"
    snapshot_description = "Test Snapshot"
    virtual_machine.CreateSnapshot_Task(
        name=snapshot_name,
        description=snapshot_description,
        memory=True,
        quiesce=False,
    )
    # List the existing snapshots
    snap_info = virtual_machine.snapshot
    if snap_info is not None:
        print("Exiting Snapshots:")
        tree = snap_info.rootSnapshotList
        while tree[0].childSnapshotList is not None:
            print(" - {0} => {1}".format(tree[0].name, tree[0].description))
            if len(tree[0].childSnapshotList) < 1:
                break
            tree = tree[0].childSnapshotList
    else:
        print("No Snapshot")


if __name__ == "__main__":
    main()
