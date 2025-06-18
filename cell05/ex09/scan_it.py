import sys
if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    target_string = sys.argv[2]
    count = target_string.count(keyword)
    if count > 0:
        print(count)
    else:
        print("none")