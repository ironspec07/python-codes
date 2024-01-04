cost = int(input("enter total cost: "))

cgst = 0.09*cost
print(f"Add CGST 09% {cgst}")
sgst = 0.09*cost
print(f"Add SGST 09% {sgst}")

print(f"total cost of product:{cost+sgst+cgst}")
print("hello")


from tabulate import tabulate
mydata = [
    ["Add: CGST 09% ", cgst], 
    ["Add: SGST 09% ", sgst], 
    ["total cost of product:",(cost+sgst+cgst) ], 
]
head = ["Particulars", "GST on particulars"]
print(tabulate(mydata, headers=head, tablefmt="grid"))