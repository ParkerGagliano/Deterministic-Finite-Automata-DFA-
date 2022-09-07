from Graph import Graph

def main():
    print('---DFA Solver, please specify the input---')
    joe = input()
    graph = joe.split()
    temp = []
    print(graph)
    for i in range(2):
        for x in range(len(graph)):
            print(f'specify the {i}th mapping of this DFA:')
            print(f'--what does q{x}, {i} map to? ex q0--')
            joe = input()
            temp.append([f'q{x}{i}', f'{joe}'])
    print("--what is the inital state? ex q0--")
    start = input()
    print("--Lastly what is the final state ex q0--")
    final = input()
    joe = Graph(graph, temp, start, final)
    joe.createMapping()
    print("--graph is created--")
    print("what string would you like to try with this DFA? ex: 1010101")
    theString=input()
    joe.judge(theString)


if __name__ == "__main__":
    main()

