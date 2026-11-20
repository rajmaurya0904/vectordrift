# Vectordrift

**A lightweight local test harness and visualization debugger for detecting semantic drift in embedding models over time against a test dataset.**

Upgrading embedding models or prompt templates silently shifts vector spaces, breaking downstream retrieval and search relevance without throwing errors. Vectordrift eliminates blind upgrades by comparing local embedding snapshots before and after changes.

## Example

Run the check against local datasets:

```bash
python3 -c "import vectordrift; print(vectordrift.__file__)"
```

```
/home/factory/factory-workspace/vectordrift/vectordrift/__init__.py
```

## Install

```bash
pip install -e ".[dev]"
```

## Usage

- `pytest` - Run the test suite.
- `ruff check .` - Lint package source code.

## How it works

- **Snapshots**: Captures baseline and candidate embedding matrices alongside dataset metadata into local JSON/numpy artifacts.
- **Distance metrics**: Computes cosine distance, Euclidean distance, and neighborhood rank shifts between baseline and candidate vectors.
- **Local dataset harness**: Loads versioned local test datasets, runs comparison checks in memory, and asserts semantic stability tolerances.
- **Drift detection**: Flags anomalous semantic movement, embedding collapse, or severe divergence across individual test documents.

## Limitations

- **Local compute constraints**: Runs entirely in-memory and on local CPU/GPU hardware; large test datasets with millions of high-dimensional vectors may exceed RAM or cause performance bottlenecks.
- **Supported embedding dimensions**: Designed for standard dense floating-point vector dimensions (e.g., 384 to 3072 dimensions); extremely sparse representations or non-standard vector structures are not natively supported.
- **Snapshot storage scope**: Stores embedding snapshots and test datasets as unencrypted local files without built-in version control system integration or remote synchronization.

## Development

```bash
pip install -e ".[dev]"
pytest -q
ruff check .
```

## License

MIT -- see [LICENSE](LICENSE)
