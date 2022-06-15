import sys

if (len(sys.argv) >= 3):
    threshold = float(sys.argv[-2])
    limit = float(sys.argv[-1])
    sum = 0.0
    for num in sys.stdin:
        # Not exceed threshold
        num = max(0.0, float(num.rstrip()) - threshold)
        # Maximize num while keep sum under limit
        num = min(num, limit - sum)
        sum += num
        print(num)
    print(sum)
else:
    print("Need to provide 2 arguments: threshold and limit.")