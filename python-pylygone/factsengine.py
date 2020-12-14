import json
from node import Node
from record import Record, Label


class FactsEngine:
    def __init__(self):
        self.root_node = None

    def fill(self, record):
        if self.root_node is not None:
            self.root_node.fill(record)

    def store(self, record):
        if record.is_filled():
            if self.root_node is None:
                self.root_node = Node(record)
            else:
                self.root_node.order(record)

    def walk(self, walker):
        Node.walk(self.root_node, walker)

    def export(self):
        if self.root_node:
            return self.root_node.export()

    def save(self, db_path):
        with open(db_path, 'w') as f:
            f.write(json.dumps(self.export()))

    def load(self, db_path):
        export = {}
        with open(db_path) as f:
            content = f.read()
            export = json.loads(content)
        self._recurse_load(export)

    def _recurse_load(self, export):
        for record in export['records']:
            new_record = Record(
                record['sides'],
                record['right_angles'],
                record['parallel_sides'],
                record['same_length_sides']
            )
            new_record.set_label(Label[record['label']])
            self.store(new_record)
        if export['L']:
            self._recurse_load(export['L'])
        if export['R']:
            self._recurse_load(export['R'])
