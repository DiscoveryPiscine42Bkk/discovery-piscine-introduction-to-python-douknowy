import sys
if len(sys.argv) == 1:
    print("none")
else:
    param_count = len(sys.argv) - 1
    print(f"parameters: {param_count}")
    for param in sys.argv[1:]:
        print(f"{param} {len(param)}")