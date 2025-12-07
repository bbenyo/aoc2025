import sys
import math
from mainUtils import read_input_split_whitespace, read_input_raw

def solve_problem_a(problem):
    operator = problem[len(problem) - 1]
    total = 0
    if operator == "*":
        total = 1
    for i in range(0, len(problem) - 1):
        match(operator):
            case "+": total += int(problem[i]);
            case "*": total *= int(problem[i]);
            case _ : print("Unknown operator!");
    return total 

def solve_problem_b(problem):
    # Zero pad each number to the right, so they're all the same length
    maxlen = 0
    for i in range(0, len(problem) - 1):
        len1 = len(problem[i])
        if maxlen < len1:
            maxlen = len1
    
    new_prob = []
    for i in range(0, maxlen):
        col = maxlen - i - 1
        num_str = ""
        for j in range(0, len(problem) - 1):
            if (len(problem[j]) < col):
                num_str += "0"
            else:
                num_str += problem[j][col];
        new_prob.append(num_str)
    new_prob.append(problem[len(problem)-1].replace(" ", ""))
    print("Orig Problem: "+str(problem)+" New Problem B: "+str(new_prob))
    return solve_problem_a(new_prob)

def replace_whitespace_columns(lines):
    for i in range(0,len(lines[0])):
        skip = False
        for j in range(0, len(lines)):
            if lines[j][i] != " ":
                skip = True
                break
        if not skip:
            # All rows had a whitespace in column i
            for j in range(0, len(lines)):
                lines[j] = lines[j][0:i] + "|" + lines[j][i+1:]
        
def day6(filename):
    print("aoc2025 day6")
    problems_in = read_input_split_whitespace(filename)
    
    problems = []
    for x in range(0, len(problems_in[0])):
        prob = []
        for y in range(0, len(problems_in)):
            prob.append(problems_in[y][x])
        problems.append(prob)
        
    print("Problems:")
    total = 0
    for problem in problems:
        answer = solve_problem_a(problem)
        print(str(problem)+" = "+str(answer))
        total += answer
        
    print("Total (part a): "+str(total))
    
    # Re-read in the problems, whitespace matters now
    # Look for a column of all whitespace, replace with |
    # Then split by | to get the problems
    problems_in = read_input_raw(filename)
    replace_whitespace_columns(problems_in)
    print("Problems B: "+str(problems_in))
    problems_b = []
    for y in range(0, len(problems_in)):
        problems_in[y] = problems_in[y].replace("\n", "");
        row = problems_in[y].split("|")
        problems_b.append(row)
    
    print("Split Problems B: "+str(problems_b))
    
    problems = []
    for x in range(0, len(problems_b[0])):
        prob = []
        for y in range(0, len(problems_b)):
            prob.append(problems_b[y][x])
        problems.append(prob)
        
    total = 0
    for problem in problems:
        answer = solve_problem_b(problem)
        print(str(answer))
        total += answer
        
    print("Total (part b): "+str(total))
    
    
if __name__ == "__main__":
    filename = "input/day6.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        
    day6(filename)
