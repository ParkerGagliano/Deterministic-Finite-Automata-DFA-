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
        
