filename = "input.txt"

file = open(filename, "r")

reports = []
for line in file:
    reports.append([int(i) for i in line.split(' ')])

# def is_safe_report(report, ascending):
#     if len(report) in [0,1]: return True
#     if(report[0] == report[1]): return False
#     curr_ascending = report[0] < report[1]
#     if(curr_ascending == ascending and abs(report[0] - report[1]) <= 3):
#         return is_safe_report(report[1:], ascending)
#     return False

# safe_count = 0
# for report in reports:
#     prev_safe_count = safe_count
#     if len(report) in [0,1,2]: safe_count+=1
#     if report[0] == report[1]: continue
#     is_safe = False
#     asc = report[0] < report[1]
#     if(is_safe_report(report, asc)): safe_count += 1
#     else:
#         for i in range(0, len(report)):
#             temp_report = [i for i in report]
#             temp_report.pop(i)
#             if temp_report[0] == temp_report[1]: continue
#             asc = temp_report[0] < temp_report[1]
#             if(is_safe_report(temp_report, asc)): 
#                 safe_count += 1
#                 break
    # if prev_safe_count == safe_count:
        # print(report)

# print(safe_count)

def get_diffs(seq):
    return [seq[i+1]-seq[i] for i in range(len(seq)-1)]

def are_all_neg(seq):
    for i in seq:
        if i > 0: return False
    return True
def are_all_pos(seq):
    for i in seq:
        if i < 0: return False
    return True
def gaps_are_good(seq):
    t = sorted([abs(i) for i in seq])[-1] <= 3
    return t

diffs = [get_diffs(report) for report in reports]

safe_counts = 0
bad_diffs = []

#part 1
for diff in diffs:
    # is seq safe straight up?
    if gaps_are_good(diff) and 0 not in diff and (are_all_neg(diff) or are_all_pos(diff)): safe_counts += 1
    else: bad_diffs.append(diff)

print(safe_counts)

# part 2
for diff in bad_diffs:
    prev = safe_counts
    for i in range(len(diff)):
        temp_diff = [d for d in diff]
        if(i == 0 or i == len(diff)-1):
            temp_diff.pop(i)
        else:
            val = temp_diff.pop(i)
            if(i == 1):
                temp_diff[i-1] += val
            else: temp_diff[i] += val
        if gaps_are_good(temp_diff) and 0 not in temp_diff and (are_all_neg(temp_diff) or are_all_pos(temp_diff)): 
            safe_counts += 1
            break
        
print(safe_counts)