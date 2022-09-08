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
