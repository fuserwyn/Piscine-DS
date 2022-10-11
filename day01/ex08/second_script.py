import sys

def second_script():
    if len(sys.argv) != 2:
        return
    with open("employees.tsv") as f1:
        lines = [line.rstrip() for line in f1]
    out = ""
    for line in lines:
        info = line.split('\t')
        if (sys.argv[1] == info[2]):
            out = "Dear %s, welcome to our team. We are sure that " % info[0]
            out += "it will be a pleasure to work with you. That's a precondition for the professionals that our company hiout."
    if not out:
        out = "wrong email"
    print(out)

if __name__ == '__main__':
    second_script()