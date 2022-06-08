from utils.count_file import check_count, add_count


def subset_sum(numbers: list, target, partial=[]) -> None:
    # Check if any subset reached the target.
    # As we don't want to find all subsets reaching the target, we stop searching for combinations after we find one.
    if check_count():
        return

    # Subset sum
    s = sum(partial)

    # Check if the partial sum is equals to target.
    # If it is, check on the file, for control.
    if s == target:
        # print(f' Elements: {partial} | Partial: {s} | Target: {target}')
        add_count()

    # if target was reached, no need to continue searching;
    if s >= target:
        return

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n])
