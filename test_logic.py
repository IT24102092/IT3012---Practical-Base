# Task 4.1: Test the Forward Chaining Knowledge Base

from logic_engine import KnowledgeBase


def test_forward_chaining():
    # Create the Knowledge Base
    kb = KnowledgeBase()

    # Add the safety rules
    kb.tell_rule(
        ["TargetVisible", "HasDust"],
        "SafeToEngage"
    )

    kb.tell_rule(
        ["SafeToEngage", "BloodseekerMissing"],
        "Retreat"
    )

    # Test Case 1: Safe engagement
    kb.clear_facts()
    kb.tell_fact("TargetVisible")
    kb.tell_fact("HasDust")

    kb.forward_chain()

    assert "SafeToEngage" in kb.facts, \
        "Test 1 Failed: SafeToEngage was not deduced"

    assert "Retreat" not in kb.facts, \
        "Test 1 Failed: Retreat should not be deduced"

    # Test Case 2: Retreat
    kb.clear_facts()
    kb.tell_fact("TargetVisible")
    kb.tell_fact("HasDust")
    kb.tell_fact("BloodseekerMissing")

    kb.forward_chain()

    assert "Retreat" in kb.facts, \
        "Test 2 Failed: Retreat was not deduced"

    # Test Case 3: Verify both SafeToEngage and Retreat
    kb.clear_facts()
    kb.tell_fact("TargetVisible")
    kb.tell_fact("HasDust")
    kb.tell_fact("BloodseekerMissing")

    kb.forward_chain()

    assert "SafeToEngage" in kb.facts, \
        "Test 3 Failed: SafeToEngage was not deduced"

    assert "Retreat" in kb.facts, \
        "Test 3 Failed: Retreat was not deduced"

    print("All Logic Engine Test Cases Passed!")
    print("Retreat Rule Test Passed!")


if __name__ == "__main__":
    test_forward_chaining()