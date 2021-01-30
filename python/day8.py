accumulator = 0


def reset():
    global accumulator
    accumulator = 0


def acc(arg):
    global accumulator
    accumulator += int(arg)
    return 1


def jmp(arg):
    return int(arg)


def nop(_arg):
    return 1


instructions = {
    "acc": acc,
    "jmp": jmp,
    "nop": nop
}


# returns amount to jump
def run_instr(instr):
    global accumulator
    op, arg = instr.split(" ")
    if op in instructions:
        return instructions[op](arg)
    else:
        print("invalid instr op", op)
        return 1


def run_str(instructs_str):
    instructs = instructs_str.splitlines()
    return run(instructs)


def run(instructs):
    executed = []
    i = 0
    reset()
    while i < len(instructs):
        if i in executed:
            return False  # infinite loop
        executed.append(i)
        i += run_instr(instructs[i])
    return True


def find_valid_run(instructs_str : str):
    instr_lines = instructs_str.splitlines()
    for i in range(0, len(instr_lines)):
        op, arg = instr_lines[i].split(" ")
        if op == "nop":
            op = "jmp"
            new_instructions = instr_lines.copy()
            new_instructions[i] = op + " " + arg
            if(run(new_instructions)):
                return
        elif op == "jmp":
            op = "nop"
            new_instructions = instr_lines.copy()
            new_instructions[i] = op + " " + arg
            if(run(new_instructions)):
                return
