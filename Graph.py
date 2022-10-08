import time


class Graph:
    def __init__(self, graph, mappings, start, final):
        self.graph = graph
        self.mappings = mappings
        self.start = start
        self.final = final
        self.dic = {}

    def createMapping(self):
        for i in range(len(self.mappings)):
            self.dic[self.mappings[i][0]] = self.mappings[i][1]

    def judge(self, string):
        current = self.start
        for i in string:
            current = self.dic[current+i]
        if current == self.final:
            print('\nLast node is final node, string is accepted')
            return True
        else:
            print('\nLast node does not match the final node, string is not accepted')
            return False

    def visualizedJudge(self, string):
        current = self.start
        print(f"\nJudging DFA, starting at {current}")
        time.sleep(.5)
        for i in string:
            tempcurrent = current
            current = self.dic[current+i]
            print(f"\n{tempcurrent} with {i} as input brings us to {current}")
            time.sleep(.5)
        print(f"\nthat was the last comparison, is {current} the final state?")
        time.sleep(.5)
        if current == self.final:
            print('\nYes it is, this string would be accepted!')
            return True
        else:
            print('\nNo its not, this string is denied!')
            return False


class GraphHelper:
    def __init__(self) -> None:
        self.temp = []
        self.graph = 0
        self.st = 0
        self.end = 0
        self.theGraph = 0

    def getStates(self):
        self.st = input("--what is the inital state? ex q0--\n")
        self.end = input("--Lastly what is the final state ex q0--\n")

    def getMappings(self):
        for i in range(2):
            for x in range(len(self.graph)):
                print(f'--what does q{x}, {i} map to? ex q0--\n')
                inp = input()
                self.temp.append([f'q{x}{i}', f'{inp}'])

    def start(self):
        inp = input(
            '---DFA Solver, please specify the input---\nexample input is q0 q1 q2, with only 1 space in between\n')
        self.graph = inp.split()

    def createGraph(self):
        self.theGraph = Graph(self.graph, self.temp, self.st, self.end)
        self.theGraph.createMapping()

    def outputType(self):
        theString = input(
            "what string would you like to try with this DFA? ex: 1010101\n")
        yn = input(
            "would you like to see the process of the DFA evaluation y/n?\n")
        if yn == 'y':
            self.theGraph.visualizedJudge(theString)
        elif yn == 'n':
            self.theGraph.judge(theString)
        else:
            'wrong input'

    def standardRun(self):
        self.start()
        self.getMappings()
        self.getStates()
        self.createGraph()
        self.outputType()
