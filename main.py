from Graph import Graph


def main():
    print('\n---DFA Solver, please specify the input---')
    print('\nexample input is q0 q1 q2, with only 1 space in between')
    inp = input()
    graph = inp.split()
    temp = []
    for i in range(2):
        for x in range(len(graph)):
            #print(f'specify the {i}th mapping of this DFA:')
            print(f'\n--what does q{x}, {i} map to? ex q0--')
            inp = input()
            temp.append([f'q{x}{i}', f'{inp}'])
    print("\n--what is the inital state? ex q0--")
    start = input()
    print("\n--Lastly what is the final state ex q0--")
    final = input()
    theGraph = Graph(graph, temp, start, final)
    theGraph.createMapping()
    print("\n--graph is created--")
    print("\nwhat string would you like to try with this DFA? ex: 1010101")
    theString = input()
    print("\nwould you like to see the process of the DFA evaluation y/n?")
    yn = input()
    if yn == 'y':
        theGraph.visualizedJudge(theString)
    elif yn == 'n':
        theGraph.judge(theString)
    else:
        'wrong input'


if __name__ == "__main__":
    main()
