def add_owned_set(owned_sets, set_number):
    """Add a set number once and return the updated collection."""
    if set_number not in owned_sets:
        owned_sets.append(set_number)
    return owned_sets
