class InferenceEngine:
    def __init__(self, facts_engine, rules_engine):
        self.facts_engine = facts_engine
        self.rules_engine = rules_engine

    def process(self, record):
        self.facts_engine.fill(record)
        if not record.is_filled():
            self.rules_engine.fill(record)
            self.facts_engine.store(record)
            return False
        else:
            return True
