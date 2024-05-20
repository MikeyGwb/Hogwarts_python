
list_number = [100, 12, 36, 24, 65, 56, 79, 88, 69, 510, 11]
add_value = 0
minimum = 10000
maximum = 0

for i in list_number:
    add_value = add_value + i

    if minimum > i:
        minimum = i

    if maximum < i:
        maximum = i

total_list_number = int(len(list_number))
average_value = add_value / total_list_number

print(f"列表的和为：{add_value}")
print(f"列表中的最小值为：{minimum}")
print(f"列表中的最大值为：{maximum}")
print(f'列表的平均值为：{average_value}')
