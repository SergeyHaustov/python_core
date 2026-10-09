def recurs_count(items, count=0):
    if items:
        if items[0] == "PASS":
            count += 1
        return recurs_count(items[1:], count=count)
    return count


result_list = ["PASS", "FAIL", "PASS", "PASS", "SKIP", "PASS", "FAIL", "PASS"]
print(recurs_count(result_list))
