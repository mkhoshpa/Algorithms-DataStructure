def all_positions(nums):
    if len(nums) == 1:
        return [nums]
    out = set()
    for i, e in enumerate(nums):
        new_nums = [nums[k] for k in range(len(nums)) if k != i]
        temps = all_positions(new_nums)
        for temp in temps:
            temp.add(e)
            out.append(temp)
    return out