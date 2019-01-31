
 tplOne = (2, 123.4567, 10000, 12345.67)
 conversions = "File_{:0>3d}: {:.2f} {:.2e} {:.3e}"

 print(conversions.format(2, 123.4567, 10000, 12345.67))

 print(conversions.format(*tplOne))


 tplTwo = (3,4,5,6,53)

 def Formatter(seq):
 # Determine number of brackets needed to accommodate the input
     numOfInputs = len(seq)
     print(("The {} numbers are: " + ", ".join(["{}"] * numOfInputs)).format(numOfInputs,*seq))


 Formatter(tplTwo)

 task 4
 """Given a 5 element tuple:
 ( 4, 30, 2017, 2, 27)
 use string formating to print:
 '02 27 2017 04 30'
 Hint: use index numbers to specify positions.

 """

 task4Tpl = ( 4, 30, 2017, 2, 27)
 print(f"{task4Tpl[3]:0>2}, {task4Tpl[4]}, {task4Tpl[2]}, {task4Tpl[0]:0>2}, {task4Tpl[1]}")

 # task 5
 List1 = ['oranges', 1.3, 'lemons', 1.1]
 print(f"The weight of an {List1[0]} is {List1[1]} and the weight of a {List1[2]} is {List1[3]}")
 print(f"The weight of an {List1[0].upper()} is {List1[1]*1.2} and the weight of a {List1[2].upper()} is {List1[3]*1.2}")

 # Task 6
Write some Python code to print a table of several rows, each with a name, an age and a cost. Make sure some of the
costs are in the hundreds and thousands to test your alignment specifiers.
r1 = ("Name", "Age", "Cost")
r2 = ("Dana", 39, 700500)
r3 = ("Jay", 10, 343553235)
r4 = ("Jo", 6, 2353)
r5 = ("Kilee", 14, 235235124)

rTable = r1, r2, r3, r4, r5
print(rTable)
for r in rTable:
    if r == r1:
        print(f"|{r[0]:^15}|{r[1]:^15}|{r[2]:^15}|")
    else:
        print(f"|{r[0]:<15}|{r[1]:<15}|{r[2]:<15}|")