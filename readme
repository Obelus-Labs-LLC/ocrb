# OCRB — Orbital Compute Readiness Benchmark (v0.2)

OCRB is a deterministic, stress-driven benchmark for evaluating
system resilience under extreme operational constraints.

## Status
- Specification: Frozen (v0.2)
- Reference Implementation: Frozen (v0.2)
- Compliance: Binary

## What This Repo Contains
- `/Docs` — Normative specification and implementation guide
- `/OCRB` — Reference implementation
- `/Examples` — Minimal usage examples
- `/Tests` — Validation and sanity checks

## What This Repo Is NOT
- Not a performance benchmark
- Not an optimization framework
- Not adaptive or learning-based

## Running a Benchmark
```python
from OCRB.runner import run_benchmark

run_benchmark(
    out_dir="report",
    workload_id="W1-A",
    workload_version="0.1",
    stress_profile_id="SP-1",
    stress_parameters={"SR-1": {"rate": 0.001}},
    execution_environment={"os": "linux", "runtime": "python"},
    master_seed=123,
    n_runs=10,
    gds_levels=[0.1, 0.2, 0.3],
    isolation_duration_declared=120.0,
    C_total=5,
)
