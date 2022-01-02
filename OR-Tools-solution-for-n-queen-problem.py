'''OR-Tools solution to the N-queens problem.'''
import sys
from ortools.constraint_solver import pywrapcp


def main(board_size):
    # Creates the solver.
    solver = pywrapcp.Solver('n-queens')

    # Creates the variables.
    # The array index is the column, and the value is the row.
    queens = [solver.IntVar(0, board_size - 1, f'x{i}') for i in range(board_size)]

    # Creates the constraints.
    # All rows must be different.
    solver.Add(solver.AllDifferent(queens))

    # No two queens can be on the same diagonal.
    solver.Add(solver.AllDifferent([queens[i] + i for i in range(board_size)]))
    solver.Add(solver.AllDifferent([queens[i] - i for i in range(board_size)]))

    db = solver.Phase(queens, solver.CHOOSE_FIRST_UNBOUND, solver.ASSIGN_MIN_VALUE)

    # Iterates through the solutions, displaying each.
    num_solutions = 0
    solver.NewSearch(db)

    # All solutions list.
    allSolutions = []
    
    while solver.NextSolution():
        # Save the solutions.
        singleSolution = []
        for i in range(board_size):
            for j in range(board_size):
                if queens[j].Value() == i:
                    singleSolution.append(j)
        allSolutions.append(singleSolution)
        num_solutions += 1
    solver.EndSearch()

    # Revers the List
    print(f'{board_size}-Queen:')
    print('Start reversing the list ..')
    reversedList = []
    list0 = []
    for i in range(len(allSolutions)):
        list0 = []
        for j in range(len(allSolutions[i])):
            list0.append( (len(allSolutions[i]) - 1) - allSolutions[i][j] )
        reversedList.append(list0)
    print('Finished reversing the list ..\n\n')

    # Save the data in the file
    with open('db.py', mode='a', encoding='utf-8') as file:
        file.write(f'# {board_size}-Queen:\n')
        file.write(f'{reversedList}\n\n')


if __name__ == '__main__':
    NUM_OF_QUEENS = 13
    for i in range(4, NUM_OF_QUEENS+1):
        board_size = i
        if len(sys.argv) > 1:
            board_size = int(sys.argv[1])
        main(board_size)
    print('Finished!')