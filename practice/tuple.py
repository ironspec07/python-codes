def taketuple(n):
    tup = ()
    print("Enter elements of tuple:")
    for _ in range(n):
        elem = input()
        tup += (elem,)
    return tup
def calcAvg(tup, n):
    total_sum = 0
    for x in tup:
        total_sum += int(x)
    avg = total_sum / n
    print(f"Sum = {total_sum}\nAverage = {avg}")