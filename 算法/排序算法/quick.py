def quick(values):
    if len(values) < 2:
        return values

    point = values[0]
    small = [x for x in values if x < point]
    equal = [x for x in values if x == point]
    great = [x for x in values if x > point]

    return quick(small) + equal + quick(great)


# if __name__ == "__main__":
#     value = [23, 45, 2, 67, 34, 9, 86, 39, 52, 73, 19, 98, 27]
#     value = quick(value)
#     print(value)
value = [23, 45, 2, 67, 34, 9, 86, 39, 52, 73, 19, 98, 27]
value = quick(value)
print(value)
