class Node:
    def __init__(self, record):
        self.key = record.sides
        self.records = [record]
        self.left_child = None
        self.right_child = None

    def has_left(self):
        return self.left_child is not None

    def has_right(self):
        return self.right_child is not None

    def order(self, record):
        if record.sides > self.key:
            if self.right_child is None:
                self.right_child = Node(record)
            else:
                self.right_child.order(record)
        elif record.sides < self.key:
            if self.left_child is None:
                self.left_child = Node(record)
            else:
                self.left_child.order(record)
        else:
            self.records.append(record)

    def fill(self, record):
        if record.sides == self.key:
            for local_record in self.records:
                if local_record == record:
                    record.set_label(local_record.label)
        elif record.sides < self.key:
            if self.has_left():
                self.left_child.fill(record)
        elif record.sides > self.key:
            if self.has_right():
                self.right_child.fill(record)

    def walk(node, walker, depth=0):
        walker.process(depth, node)
        if node is not None:
            Node.walk(node.left_child, walker, depth + 1)
            Node.walk(node.right_child, walker, depth + 1)

    def export(self):
        return {
            "records": [record.export() for record in self.records],
            "L": self.left_child.export() if self.left_child else None,
            "R": self.right_child.export() if self.right_child else None
        }
