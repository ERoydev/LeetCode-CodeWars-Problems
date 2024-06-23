def twoSum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        if target - nums[i] in hashmap:
            # Ako targeta - chilsoto na tozi index go imam v hashmapa, znachi veche imam dvata indeksa
            return [hashmap[target - nums[i]], i]
        # v protiven sluchai dobavqm chisloto kato key i negoviq indeks kato value
        hashmap[nums[i]] = i

    return []

print(twoSum([3, 2, 4], 6))