import tkinter as tink #imports the library tkinter with the name tink

calculation = ""


def receive_to_calc(symbol): #will receive numbers and opereators to calculate
    global calculation
    calculation+= str(symbol)
    output_text.delete(1.0, "end")
    output_text.insert(1.0, calculation)


def perform_calc(): #will perform the calculations
    global calculation
    try:
        calculation = str(eval(calculation))   
        output_text.delete(1.0, "end") 
        output_text.insert(1.0, calculation)
    except:
        clear_field()
        output_text.insert(1.0, "Error!")
        pass

def clear_field(): #will erase numbers, results and errors
        global calculation
        calculation = ""
        output_text.delete(1.0, "end")


root = tink.Tk()
root.geometry("350x400")

output_text = tink.Text(root, height=2, width=18, font=("Cambria", 26))
output_text.grid(columnspan=5)

butt_one = tink.Button(root, text="1", command=lambda: receive_to_calc(1), width=5, font=("Cambria", 14))
butt_one.grid(row=4, column=0)
butt_two = tink.Button(root, text="2", command=lambda: receive_to_calc(2), width=5, font=("Cambria", 14))
butt_two.grid(row=4, column=1)
butt_three = tink.Button(root, text="3", command=lambda: receive_to_calc(3), width=5, font=("Cambria", 14))
butt_three.grid(row=4, column=2)
butt_four = tink.Button(root, text="4", command=lambda: receive_to_calc(4), width=5, font=("Cambria", 14))
butt_four.grid(row=3, column=0)
butt_five = tink.Button(root, text="5", command=lambda: receive_to_calc(5), width=5, font=("Cambria", 14))
butt_five.grid(row=3, column=1)
butt_six = tink.Button(root, text="6", command=lambda: receive_to_calc(6), width=5, font=("Cambria", 14))
butt_six.grid(row=3, column=2)
butt_seven = tink.Button(root, text="7", command=lambda: receive_to_calc(7), width=5, font=("Cambria", 14))
butt_seven.grid(row=2, column=0)
butt_eight = tink.Button(root, text="8", command=lambda: receive_to_calc(8), width=5, font=("Cambria", 14))
butt_eight.grid(row=2, column=1)
butt_nine = tink.Button(root, text="9", command=lambda: receive_to_calc(9), width=5, font=("Cambria", 14))
butt_nine.grid(row=2, column=2)
butt_zero = tink.Button(root, text="0", command=lambda: receive_to_calc(0), width=5, font=("Cambria", 14))
butt_zero.grid(row=5, column=1)
butt_opan = tink.Button(root, text="(", command=lambda: receive_to_calc("("), width=5, font=("Cambria", 14))
butt_opan.grid(row=5, column=0)
butt_cpan = tink.Button(root, text=")", command=lambda: receive_to_calc(")"), width=5, font=("Cambria", 14))
butt_cpan.grid(row=5, column=2)
butt_plus = tink.Button(root, text="+", command=lambda: receive_to_calc("+"), width=5, font=("Cambria", 14))
butt_plus.grid(row=3, column=3)
butt_minus = tink.Button(root, text="-", command=lambda: receive_to_calc("-"), width=5, font=("Cambria", 14))
butt_minus.grid(row=4, column=4)
butt_dvd = tink.Button(root, text="/", command=lambda: receive_to_calc("/"), width=5, font=("Cambria", 14))
butt_dvd.grid(row=3, column=4)
butt_mul = tink.Button(root, text="*", command=lambda: receive_to_calc("*"), width=5, font=("Cambria", 14))
butt_mul.grid(row=2, column=3)
butt_deci = tink.Button(root, text=".", command=lambda: receive_to_calc("."), width=5, font=("Cambria", 14))
butt_deci.grid(row=4, column=3)
butt_equals = tink.Button(root, text="=", command=lambda: perform_calc(), width=12, font=("Cambria", 14))
butt_equals.grid(row=5, column=3, columnspan=2)
butt_clear = tink.Button(root, text="C", command= clear_field, width=5, font=("Cambria", 14))
butt_clear.grid(row=2, column=4)
root.mainloop()
