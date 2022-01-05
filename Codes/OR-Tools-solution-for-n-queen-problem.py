''' OR-Tools Solution to The N-Queens Problem. '''
import sys
from ortools.constraint_solver import pywrapcp


def main(board_size):
    # CREATES THE SOLVER.
    solver = pywrapcp.Solver('n-queens')

    # CREATES THE VARIABLES.
    # THE ARRAY INDEX IS THE COLUMN, AND THE VALUE IS THE ROW.
    queens = [solver.IntVar(0, board_size - 1, f'x{i}') for i in range(board_size)]

    # CREATES THE CONSTRAINTS.
    # ALL ROWS MUST BE DIFFERENT.
    solver.Add(solver.AllDifferent(queens))

    # NO TWO QUEENS CAN BE ON THE SAME DIAGONAL.
    solver.Add(solver.AllDifferent([queens[i] + i for i in range(board_size)]))
    solver.Add(solver.AllDifferent([queens[i] - i for i in range(board_size)]))

    db = solver.Phase(queens, solver.CHOOSE_FIRST_UNBOUND, solver.ASSIGN_MIN_VALUE)

    # ITERATES THROUGH THE SOLUTIONS, DISPLAYING EACH.
    num_solutions = 0
    solver.NewSearch(db)

    # ALL SOLUTIONS LIST.
    allSolutions = []
    
    # SAVE THE SOLUTIONS.
    while solver.NextSolution():
        singleSolution = []
        for i in range(board_size):
            for j in range(board_size):
                if queens[j].Value() == i:
                    singleSolution.append(j)
        allSolutions.append(singleSolution)
        num_solutions += 1
    solver.EndSearch()

    # REVERSE THE LIST
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

    # SAVE THE DATA IN THE FILE.
    with open('db.py', mode='a', encoding='utf-8') as file:
        file.write(f'# {board_size}-Queen:\n')
        file.write(f'_{board_size}_queen_solutions_list = {reversedList}\n\n')


def SaveAllSols(NUM_OF_QUEENS):
    # CREATE THE LISTS ==> """ _4_queen_solutions_list, .., _N_queen_solutions_list """.
    for I in range(4, NUM_OF_QUEENS+1):
        board_size = I
        if len(sys.argv) > 1:
            board_size = int(sys.argv[1])
        main(board_size)

    # CREATE THE LIST ==> """ ALL_SOLS_LIST = [_4_queen_solutions_list, .., _N_queen_solutions_list] """.
    with open('db.py', mode='a', encoding='utf-8') as file:
        file.write('ALL_SOLS_LIST = [')
        for J in range(4, NUM_OF_QUEENS+1):
            if J != NUM_OF_QUEENS:
                file.write(f'_{J}_queen_solutions_list, ')
            else:
                file.write(f'_{J}_queen_solutions_list')
        file.write(f']')
    
    # PRINT """ Finished! """, THAT REFERS TO FINISHED THE CODE!
    print('Finished!')


if __name__ == '__main__':
    NUM_OF_QUEENS = 13
    SaveAllSols(NUM_OF_QUEENS)