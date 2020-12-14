import json
from factsengine import FactsEngine
from rulesengine import RulesEngine
from inferenceengine import InferenceEngine
from record import Record


class Shell():
    def __init__(self):
        self.fe = FactsEngine()
        self.re = RulesEngine()
        self.ie = InferenceEngine(fe, re)
        print("Welcome to polygonial !\n")

    def mainloop(self):
        while True:
            command = input("polygonial> ")
            if command == "help":
                print("\nusage :")
                print("  request   Start an interactive new polygon request.")
                print("  tree      Show the fact database.")
                print("  help      Show this help.")
                print("  exit      Leave polygonial shell.")
            elif command == "request":
                self.exec_request()
            elif command == "tree":
                self.exec_tree()
            elif command == "exit":
                break

    def exec_request(self):
        sides = int(input("Number of sides : "))
        angles = int(input("Number of right angles : "))
        parallel_sides = int(input("Number of parallel sides : "))
        same_length_sides = int(input("Number of same length sides : "))
        record = Record(
            sides,
            angles,
            parallel_sides,
            same_length_sides
        )
        if self.ie.process(record):
            print("It's a FACT :")
        else:
            print("It's a RULE :")
        print("  Your polygon is a {}".format(record))

    def exec_tree(self):
        if self.fe.root_node:
            print(json.dumps(self.fe.export(), indent=2))
