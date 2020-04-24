import sys

lolcode = ""
code = []
code_index = 0
stdio = False
oic = True
can_output = True
currently_in_loop = False


class Variables:
    def __init__(self):
        self.values = []

    def __repr__(self):
        for x in self.values:
            print(x)

    def __str__(self):
        return_value = ""
        for x in self.values:
            return_value.join(x)
            return_value = return_value + "\n"
        return return_value

    def add(self, name, type, value):
        self.values.append([name, type, value])

    def change_value(self, name, value):
        for x in self.values:
            if x[0] == name:
                x[2] = value

    def copy(self, name, to_copy):
        self.add(name, to_copy.get_type(), to_copy.get_value())

    def get_type(self, name):
        for x in self.values:
            if name in x:
                return x[1]

    def get_value(self, name):
        for x in self.values:
            if name in x:
                return x[2]

    def print(self):
        for x in self.values:
            print(x)


def breakdown_command(code, index):
    global amount_of_indent
    global stdio
    global vars

    if index < len(code):
        if "BTW" in code[index]:
            pass

        elif "CAN HAS STDIO?" in code[index]:
            stdio = True

        #   PRINTING
        elif "VISIBLE" in code[index]:
            VISIBLE(code, index)

        #   VARIABLES
        elif "I HAS A " in code[index]:
            I_HAS_A(code, index)

        elif " R " in code[index]:
            R(code, index)

        #   IF
        elif "O RLY?" in code[index]:
            O_RLY(code, index)

        elif "OIC" in code[index]:
            OIC(code, index)

        # FOR LOOP
        elif "IM IN YR" in code[index]:
            IM_IN_YR(code, index)

        #   END
        elif "IM OUT YR" in code[index]:
            IM_OUT_YR(code, index)

        #   SUM
        elif "SUM OF" in code[index]:
            SUM_OF(code, index)

        #   SUBTRACTION
        elif "DIFF OF" in code[index]:
            DIFF_OF(code, index)

        #   PRODUCT
        elif "PRODUKT OF" in code[index]:
            PRODUKT_OF(code, index)

        #   DIVISION
        elif "QUOSHUNT OF" in code[index]:
            QUOSHUNT_OF(code, index)

        #   MODULO
        elif "MOD OF" in code[index]:
            MOD_OF(code, index)

        #   EQUAL
        elif "BOTH SAEM" in code[index]:
            BOTH_SAEM(code, index)

        #   DIFFERENT
        elif "DIFFRINT" in code[index]:
            DIFFRNT(code, index)

        elif "KTHXBYE" in code[index]:
            print("k bye")
            # sys.exit(0) #Disabled for debugging purposes

        else: 
            pass

def O_RLY(code, index):
    global code_index
    oic_location = 0
    expression_outcome = "LOSE"
    if "BOTH SAEM" in code[index]:
        expression_outcome = BOTH_SAEM(code, index)

    elif "DIFFRINT" in code[index]:
        expression_outcome = DIFFRNT(code, index)

    if expression_outcome is "WIN":
        YA_RLY(code, index + 1)
    else:
        NO_WAI(code, index + 3)

    for i in range(0, len(code)):
        if "OIC" in code[i]:
            code_index += oic_location - 1
        else:
            oic_location += 1

def YA_RLY(code, index):
    if "YA RLY" in code[index]:
        breakdown_command(code, index + 1)

def NO_WAI(code, index):
    if "NO WAI" in code[index]:
        breakdown_command(code, index + 1)

def OIC(code, index):
    pass

def IM_IN_YR(code, index):
    global vars
    currently_in_loop = True
    variable_name = ""
    start_value = ""
    desired_value = ""

    #   FINDING VARIABLE NAME
    if "UPPIN" in code[index]:
        variable_start = code[index].find("UPPING YR ") + 10
    elif "NERFIN" in code[index]:
        variable_start = code[index].find("NERFIN YR ") + 10

    for x in range (variable_start, len(code[index])):
        if code[index][x] is not " ":
            variable_name = variable_name + code[index][x]
            found_name = True
        else:
            break

    start_value = int(vars.get_value(variable_name))

    #   FINDING DESIRED END VALUE
    desired_value_start = code[index].find("TIL ") + 4

    for x in range (desired_value_start, len(code[index])):
        if code[index][x] is not "\n":
            desired_value = desired_value + code[index][x]
            found_name = True
        else:
            break
    desired_value = int(desired_value)

    if "UPPIN" in code[index]:
        while start_value is not desired_value:
            i = 0
            while "IM OUTTA YR " not in code[index + i]:
                breakdown_command(code, index + 1 + i)
                i += 1
            start_value += 1
            vars.change_value(variable_name, start_value)

    elif "NERFIN" in code[index]:
        while start_value is not desired_value:
            i = 0
            while "IM OUTTA YR " not in code[index + i]:
                breakdown_command(code, index + 1 + i)
                i += 1
            start_value -= 1
            vars.change_value(variable_name, start_value)


def IM_OUT_YR(code, index):
    currently_in_loop = False

def R(code, index):
    global vars
    found_name = False
    searching_for_value = False
    variable_name = ""
    variable_value = ""
    start = code[index].find("R")
    # Get variable name
    for x in range (0, len(code[index])):
        if code[index][x] is not " " and not searching_for_value:
            variable_name = variable_name + code[index][x]
            found_name = True
        elif code[index][x] is " " and found_name:
            searching_for_value = True

    for x in range (start + 2, len(code[index])):
        if code[index][x] is not " " and found_name:
            variable_value = variable_value + code[index][x]
        elif code[index][x] is "\n":
            break

    vars.change_value(variable_name, variable_value)

def VISIBLE(code, index):
    global vars
    if stdio is True:
        if "\"" in code[index]:
            code[index].find("\"")
            first_quote = code[index].find("\"")
            last_quote = code[index].find("\"", first_quote + 1, len(code[index]))
            value = code[index][first_quote + 1:last_quote]
            print(value)
        else: 
            variable_name_index = code[index].find("VISIBLE ") + 8
            variable_name = ""
            for x in range (variable_name_index, len(code[index])):
                if code[index][x] is not "\n":
                    variable_name = variable_name + code[index][x]
                else:
                    break
            print(variable_name + ": " + str(vars.get_value(variable_name)))

    else:
        print("Use \"CAN HAS STDIO\" to print")

def I_HAS_A(code, index):
    variable_name = ""
    variable_type = ""
    variable_value = ""
    variable_to_copy = ""
    start = code[index].find("I")
    # Get variable name
    for x in range (start + 8, len(code[index])):
        if code[index][x] is not " " and code[index][x] is not ",":
            variable_name = variable_name + code[index][x]
        else:
            break
    # Get variable type
    if "ITZ A " in code[index]:
        variable_type_index = code[index].find("ITZ A")
        for x in range (variable_type_index + 6, len(code[index])):
            if code[index][x] is not " " and code[index][x] is not ",":
                variable_type = variable_type + code[index][x]
            else:
                break

    # Copy from other variable
    if "ITZ LIEK A " in code[index]:
        variable_to_copy_index = code[index].find("ITZ A")
        for x in range (variable_to_copy_index + 6, len(code[index])):
            if code[index][x] is not " " and code[index][x] is not ",":
                variable_to_copy = variable_to_copy + code[index][x]
            else:
                break


    # Get variable value
    elif "ITZ" in code[index]:
        variable_value_index = code[index].find("ITZ")
        for x in range (variable_value_index + 4, len(code[index])):
            if code[index][x] is not " " and code[index][x] is not ",":
                variable_value = variable_value + code[index][x]
            else:
                break

    vars.add(variable_name, variable_type, variable_value)

def SUM_OF(code, index):
    variable_one = 0
    variable_two = 0
    variable_sum = 0
    variable_one_index = code[index].find("OF ") + 3
    variable_two_index = code[index].find("AN ") + 3
    for x in range (variable_one_index, len(code[index])):
            if code[index][x] is not " " and code[index][x] is not ",":
                variable_one = variable_one + int(code[index][x])
            else:
                break

    for x in range (variable_two_index, len(code[index])):
            if code[index][x] is not " " and code[index][x] is not ",":
                variable_two = variable_two + int(code[index][x])
            else:
                break

    variable_sum = variable_one + variable_two
    return variable_sum

def DIFF_OF(code, index):
    variable_one = 0
    variable_two = 0
    variable_difference = 0
    variable_one_index = code[index].find("OF ") + 3
    variable_two_index = code[index].find("AN ") + 3
    for x in range (variable_one_index, len(code[index])):
            if code[index][x] is not " " and code[index][x] is not ",":
                variable_one = variable_one + int(code[index][x])
            else:
                break

    for x in range (variable_two_index, len(code[index])):
            if code[index][x] is not " " and code[index][x] is not ",":
                variable_two = variable_two + int(code[index][x])
            else:
                break

    variable_difference = variable_one - variable_two
    return variable_difference

def PRODUKT_OF(code, index):
    variable_one = 0
    variable_two = 0
    variable_product = 0
    variable_one_index = code[index].find("OF ") + 3
    variable_two_index = code[index].find("AN ") + 3
    for x in range (variable_one_index, len(code[index])):
            if code[index][x] is not " " and code[index][x] is not ",":
                variable_one = variable_one + int(code[index][x])
            else:
                break

    for x in range (variable_two_index, len(code[index])):
            if code[index][x] is not " " and code[index][x] is not ",":
                variable_two = variable_two + int(code[index][x])
            else:
                break

    variable_product = variable_one * variable_two
    return variable_product

def QUOSHUNT_OF(code, index):
    variable_one = 0
    variable_two = 0
    variable_division = 0
    variable_one_index = code[index].find("OF ") + 3
    variable_two_index = code[index].find("AN ") + 3
    for x in range (variable_one_index, len(code[index])):
            if code[index][x] is not " " and code[index][x] is not ",":
                variable_one = variable_one + int(code[index][x])
            else:
                break

    for x in range (variable_two_index, len(code[index])):
            if code[index][x] is not " " and code[index][x] is not ",":
                variable_two = variable_two + int(code[index][x])
            else:
                break

    variable_division = variable_one / variable_two
    return variable_division

def MOD_OF(code, index):
    variable_one = 0
    variable_two = 0
    variable_modulo = 0
    variable_one_index = code[index].find("OF ") + 3
    variable_two_index = code[index].find("AN ") + 3
    for x in range (variable_one_index, len(code[index])):
            if code[index][x] is not " " and code[index][x] is not ",":
                variable_one = variable_one + int(code[index][x])
            else:
                break

    for x in range (variable_two_index, len(code[index])):
            if code[index][x] is not " " and code[index][x] is not ",":
                variable_two = variable_two + int(code[index][x])
            else:
                break

    variable_modulo = variable_one % variable_two
    return variable_modulo

def BOTH_SAEM(code, index):
    variable_one = 0
    variable_two = 0
    variable_modulo = 0
    variable_one_index = code[index].find("SAEM ") + 5
    variable_two_index = code[index].find("AN ") + 3
    for x in range (variable_one_index, len(code[index])):
            if code[index][x] is not " " and code[index][x] is not ",":
                variable_one = variable_one + int(code[index][x])
            else:
                break

    for x in range (variable_two_index, len(code[index])):
            if code[index][x] is not " " and code[index][x] is not ",":
                variable_two = variable_two + int(code[index][x])
            else:
                break
    variable_different = True if (variable_one == variable_two) else False
    
    if variable_different:
        return "WIN"
    else:
        return "LOSE"

def DIFFRNT(code, index):
    variable_one = 0
    variable_two = 0
    variable_different = False
    variable_one_index = code[index].find("DIFFRINT ") + 9
    variable_two_index = code[index].find("AN ") + 3
    for x in range (variable_one_index, len(code[index])):
            if code[index][x] is not " " and code[index][x] is not ",":
                variable_one = variable_one + int(code[index][x])
            else:
                break

    for x in range (variable_two_index, len(code[index])):
            if code[index][x] is not " " and code[index][x] is not ",":
                variable_two = variable_two + int(code[index][x])
            else:
                break

    variable_different = False if (variable_one == variable_two) else True

    if variable_different:
        return "WIN"
    else:
        return "LOSE"

def load_code(filename):
    file = open(filename, "r")
    return file.read() + "\n"

def breakdown_code(lolcode):
    line = ""
    for x in lolcode:
        if x is not "\n":
            line = line + x
        else:
            code.append(line)
            line = ""
def run_code(code):
    global code_index
    code_index = 0
    for i in range(0, len(code) - 1):
        breakdown_command(code, code_index)
        code_index += 1

vars = Variables()

lolcode = load_code("code.lol")
breakdown_code(lolcode)
run_code(code)
