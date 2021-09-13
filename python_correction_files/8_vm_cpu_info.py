import utils
from pyVmomi import vim


def main():
    # Connection to the vCenter
    content = utils.connect()
    # Get the VM (see utils.py)
    virtual_machine = utils.get_vm(content)
    content = utils.connect()

    # create a mapping from performance stats to their counterIDs
    # counterInfo: [performance stat => counterId]
    # performance stat example: cpu.usagemhz.LATEST
    # counterId example: 6
    counter_info = {}
    for counter in perf_manager.perfCounter:
        if counter.groupInfo.key == "cpu":
            full_name = (
                counter.groupInfo.key
                + "."
                + counter.nameInfo.key
                + "."
                + counter.rollupType
            )
        counter_info[full_name] = counter.key
    # Get all available metric IDs for this VM
    counter_ids = [
        m.counterId
        for m in perf_manager.QueryAvailablePerfMetric(entity=virtual_machine)
    ]

    # Using the IDs form a list of MetricId
    # objects for building the Query Spec
    metric_ids = [
        vim.PerformanceManager.MetricId(counterId=counter, instance="*")
        for counter in counter_ids
    ]

    # Build the specification to be used
    # for querying the performance manager
    spec = vim.PerformanceManager.QuerySpec(
        maxSample=1, entity=virtual_machine, metricId=metric_ids
    )
    # Query the performance manager
    # based on the metrics created above
    result_stats = perf_manager.QueryStats(querySpec=[spec])

    output = ""
    # Loop through the results and print the output
    for _ in result_stats:
        for val in _.value:
            if val.id.counterId in list(counter_info.values()):
                counterinfo_k_to_v = list(counter_info.keys())[
                    list(counter_info.values()).index(val.id.counterId)
                ]
                if val.id.instance == "":
                    output += " - %s: %s\n" % (counterinfo_k_to_v, str(val.value[0]))
    print("VM CPU Informations :")
    print(" - vm.name:" + virtual_machine.name)
    print(output)


if __name__ == "__main__":
    main()
