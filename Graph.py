import time
class Graph:
    def __init__(self, graph, mappings, start, final):
        self.graph = graph
        self.mappings=mappings
        self.start = start
        self.final = final
        self.dic={}

    def createMapping(self):
        for i in range(len(self.mappings)):
            self.dic[self.mappings[i][0]]=self.mappings[i][1]

    def judge(self, string):
        current = self.start
        for i in string:
            current = self.dic[current+i]
        if current == self.final:
            print('Works')
            return True
        else:
            print('Doesnt accept')
            return False
        
    def visualizedJudge(self, string):
        current = self.start
        print(f"Judging DFA, starting at {current}")
        time.sleep(.5)
        for i in string:
            tempcurrent = current 
            current = self.dic[current+i]
            print(f"{tempcurrent} with {i} as input brings us to {current}")
            time.sleep(.5)
        print(f"that was the last comparison, is {current} the final state?")
        time.sleep(.5)
        if current == self.final:
            print('Yes it is, this string would be accepted!')
            return True
        else:
            print('No its not, this string is denied!')
            return False