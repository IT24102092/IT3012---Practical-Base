# Task 1: Build the Knowledge Base

class KnowledgeBase:
    def __init__(self):
        self.facts = set()  # Store unique facts
        self.rules = []  # Store rules

    def tell_fact(self, fact_string):
        self.facts.add(fact_string)  # Add a fact

    def tell_rule(self, premise_list, conclusion_string):
        self.rules.append((premise_list, conclusion_string))  # Store a rule

    def clear_facts(self):
        self.facts.clear()  # Remove all facts

        # Task 2: Implement Forward Chaining

    def forward_chain(self):
        new_facts_added = True  # Start inference

        while new_facts_added:  # Continue while new facts are added
            new_facts_added = False  # Reset the flag

            for premises, conclusion in self.rules:  # Check each rule
                if conclusion not in self.facts:  # Check if conclusion is unknown
                    if all(premise in self.facts for premise in premises):
                        self.facts.add(conclusion)  # Add the new fact
                        new_facts_added = True  # Mark that a fact was added