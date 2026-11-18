# Compare shallow dictionaries: implementation

## What the example does

Report added, removed and changed keys separately. This is a shallow comparison; nested objects are compared as whole values.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
[
  {
    "a": 1,
    "b": 2
  },
  {
    "b": 3,
    "c": 4
  }
]
```

Expected result:

```json
{
  "added": [
    "c"
  ],
  "removed": [
    "a"
  ],
  "changed": [
    "b"
  ]
}
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
