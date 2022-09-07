class Graph:
    def __init__(self, graph, mappings, final):
        self.graph = graph
        self.mappings=mappings
        self.final = final

    def createMapping(self):
        self.dic = {}
        for i in range(len(self.mappings)):
            self.dic[self.mappings[i][0]]=self.mappings[i][1]

    def accept(self, string, start):
        current = start
        for i in string:
            current = self.dic[current+i]
        if current == self.final:
            print('Works')
            return True
        else:
            print('Doesnt accept')
            return False
            


    


test = Graph(["q0","q1","q2"],[["q00", "q0"],["q10", "q0"], ["q20", "q2"], ["q01", "q1"], ["q11", "q2"], ["q21", "q1"]], "q1")
test.createMapping()
test.accept('01010', "q0")
