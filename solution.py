

def solve(value):
    return {"added": sorted(value[1].keys()-value[0].keys()), "removed": sorted(value[0].keys()-value[1].keys()), "changed": sorted(k for k in value[0].keys() & value[1].keys() if value[0][k] != value[1][k])}
