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
            return True
        else:
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
        self.isFile = False

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
        inp = input("Will you be using a file as input y/n?")
        if inp == 'y':
            self.isFile = True

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

    def fileRun(self):
        inp = input(
            "You must input a text file in the folder. What is the name of the file, with extension included")
        file = open(inp, 'r')
        finalfile = open('accepted', 'x')
        for line in file:
            if line[0] == 'a' or line[0] == 'b':
                final = ''
                for letter in line:
                    if letter == 'a':
                        final = final + '0'
                    else:
                        final = final + '1'
            else:
                if self.theGraph.judge(line):
                    print(line)
                    finalfile.write(line)
            if self.theGraph.judge(final):
                print(line)
                finalfile.write(line)
        file.close
        finalfile.close
        print('accepted strings added to accepted.txt')

    def standardRun(self):
        self.start()
        self.getMappings()
        self.getStates()
        self.createGraph()
        if self.isFile:
            self.fileRun()
        else:
            self.outputType()
