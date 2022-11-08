# Write a program that finds the longest intersection. You will be given a number N. On each of the next N lines you
# will be given two ranges in the format: "{first_start},{first_end}-{second_start},{second_end}". You should find
# the intersection of these two ranges. The start and end numbers in the ranges are inclusive. Finally, you should
# find the longest intersection of all N intersections, print the numbers that are included and its length in the
# format: "Longest intersection is [{longest_intersection_numbers}] with length {length_longest_intersection}" Note:
# in each range, there will always be an intersection. If there are two equal intersections, print the first one.
def range_of_intersection(range_info):
    start, end = [int(x) for x in range_info.split(",")]
    current_set = set()
    for i in range(start, end + 1):
        current_set.add(i)
    return current_set


n = int(input())

current_biggest = set()

for _ in range(n):
    input_line = [str(x) for x in input().split("-")]
    first = set(range_of_intersection(input_line[0]))
    second = set(range_of_intersection(input_line[1]))
    current = first.intersection(second)

    if len(current) > len(current_biggest):
        current_biggest = current
print(f"Longest intersection is [{', '.join([str(x) for x in current_biggest])}] with length {len(current_biggest)}")