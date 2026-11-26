# Ordered batch processing for Compare shallow dictionaries

`batch.py` accepts an outer JSON array containing separate inputs. This is an extra level of nesting when `solve` itself accepts a list. It produces one result envelope per item, preserving input order and zero-based position.

```sh
python3 batch.py < samples/batch.json
```

The batch covers these three input/output pairs:

## Case 1

Input:
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

Result:
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

## Case 2

Input:
```json
[
  {},
  {}
]
```

Result:
```json
{
  "added": [],
  "removed": [],
  "changed": []
}
```

## Case 3

Input:
```json
[
  {
    "x": null
  },
  {
    "x": 0
  }
]
```

Result:
```json
{
  "added": [],
  "removed": [],
  "changed": [
    "x"
  ]
}
```

## Partial failures

Each successful item has `ok: true` and `result`. A failed item has `ok: false` and an exception type; later items still run. Exit status 1 means at least one item failed, while status 2 means the batch envelope itself was invalid. An empty outer array is a valid empty batch.

Report added, removed and changed keys separately. This is a shallow comparison; nested objects are compared as whole values.

The implementation processes sequentially, avoiding shared-state concurrency and keeping output order predictable. Input is limited to one MiB and 1000 items; this version materializes all results in memory. The next lesson removes that whole-batch memory requirement with line-oriented processing.
