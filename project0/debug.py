""" The function needed to be fixed:

def get_sum_metrics(predictions, metrics=[]):
    for i in range(3):
        metrics.append(lambda x: x + i)

    sum_metrics = 0
    for metric in metrics:
        sum_metrics += metric(predictions)

    return sum_metrics
"""
# Fixed function
def get_sum_metrics(predictions, metrics=None):
    # import pdb
    # pdb.set_trace()

    # Fixed: metrics=[] is mutable :
    # https://stackoverflow.com/questions/41686829/warning-about-mutable-default-argument-in-pycharm
    if metrics is None:
        metrics = []

    def funcC(j):
        func = lambda x: x + j
        return func

    # Fixed: i is mutated when creating lambda functions
    # https://stackoverflow.com/questions/233673/how-do-lexical-closures-work
    for i in range(3):
        metrics.append(funcC(i))

    sum_metrics = 0
    for metric in metrics:
        # print(metric(predictions))
        sum_metrics += metric(predictions)

    metrics = []
    return sum_metrics


def main():
    print(get_sum_metrics(0))  # Should be (0 + 0) + (0 + 1) + (0 + 2) = 3
    print(get_sum_metrics(1))  # Should be (1 + 0) + (1 + 1) + (1 + 2) = 6
    print(get_sum_metrics(2))  # Should be (2 + 0) + (2 + 1) + (2 + 2) = 9
    print(
        get_sum_metrics(3, [lambda x: x])
    )  # Should be (3) + (3 + 0) + (3 + 1) + (3 + 2) = 15
    print(get_sum_metrics(0))  # Should be (0 + 0) + (0 + 1) + (0 + 2) = 3
    print(get_sum_metrics(1))  # Should be (1 + 0) + (1 + 1) + (1 + 2) = 6
    print(get_sum_metrics(2))  # Should be (2 + 0) + (2 + 1) + (2 + 2) = 9


if __name__ == "__main__":
    main()
