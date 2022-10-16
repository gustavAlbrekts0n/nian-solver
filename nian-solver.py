import sys

path_src = "C:\\Users\\gusta\\Downloads\\Övrigt\\saol.txt"
path_dst = "C:\\Users\\gusta\\Downloads\\Övrigt\\saol_nio.txt"

def generate_wordlist():
    f1 = open(path_src, mode="r", encoding="utf-8").read()
    f2 = open(path_dst, mode="a", encoding="utf-8")

    for line in f1.splitlines():
        if len(line) == 9 and " " not in line and "-" not in line:
            f2.write(line.lower())
            f2.write("\n")

    f1.close()
    f2.close()

def solve(string):
    if len(string) != 9:
        print("Du matade inte in exakt 9 bokstäver! Försök igen...\n")
    else:
        f = open(path_src, mode="r", encoding="utf-8").read()

        solutions = []

        inputted_word = []
        inputted_word = list(string)
        inputted_word.sort()

        for line in f.splitlines():
            if len(line) >= 4 and len(line) <= 9 and string[4] in line:
                saol_word = list(line)
                saol_word.sort()

                # 9 bokstäver långt
                if saol_word == inputted_word:
                    solutions.append(line.upper())
                    continue

                # 4-8 bokstäver långt
                tmp_inputted_word = list(inputted_word)

                for c in saol_word:
                    if c in tmp_inputted_word:
                        tmp_inputted_word.remove(c)
                    else:
                        continue

                    if len(inputted_word) - len(tmp_inputted_word) == len(saol_word):
                        solutions.append(line)

        #solutions = sorted(solutions, key=len)

        num_solutions = []
        for i in range(10):
            num_solutions.append(0)
        for solution in solutions:
            num_solutions[len(solution)] += 1

        print("")
        print(" ", string[0:3])
        print(" ", string[3:6])
        print(" ", string[6:9])
        print("")

        if len(solutions) == 0:
            print("Hittade ingen lösning...")
        elif len(solutions) == 1:
            print("Funnen lösning:\n")
            print(solutions[0])
        else:
            print("Funna lösningar:\n")
            for solution in solutions:
                print(solution)

        print("----------")
        for n in range(4, 10):
            print("{} bokstäver: {}st".format(n, num_solutions[n]))

while True:
    print("\n--- Välkommen till Nian solver ---")
    string = input("Bokstäver: ")
    solve(string)

