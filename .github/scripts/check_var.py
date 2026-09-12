#!/usr/bin/env python3
"""
Sanity-check the executed notebook's own VaR outputs against known-correct
reference values, so CI fails if the analysis silently drifts (bad data,
a broken dependency, an accidental edit) rather than only checking that the
notebook runs without raising.

Reference values are the notebook's own saved outputs as of the last time a
human verified them by hand (see PR/commit history) - not independently
recomputed here, on purpose: this script's job is to catch drift, not to
re-implement the methodology a second time.
"""
import json
import sys

EXECUTED_NOTEBOOK = "executed.ipynb"
TOLERANCE = 1e-6

# (unique source substring identifying the cell, reference value)
CHECKS = [
    ("Var_1_09 = VaRs(alpha, h_1, np.array([1,1]), Annual_Covariance_Matrix_09)", 0.10107158559280117),
    ("Var_1_23 = VaRs(alpha, h_1, np.array([1,1]), Annual_Covariance_Matrix_23)", 0.04096180083398142),
    ("Hist_var_EWRD_09 = -ds['rt_RUB'].quantile(q=alpha)", 0.0437563582300805),
    ("Hist_var_EWRD_23 = -ds['rt_RUB'][:ds[ds['Date'] == '2022-02-23'].index[0]].quantile(q=alpha)", 0.04165082772801792),
]


def cell_output_float(cell):
    for out in cell.get("outputs", []):
        text = None
        if "data" in out and "text/plain" in out["data"]:
            text = "".join(out["data"]["text/plain"])
        elif "text" in out:
            text = "".join(out["text"])
        if text:
            # outputs look like "0.101..." or "np.float64(0.101...)"
            text = text.strip()
            if text.startswith("np.float64(") and text.endswith(")"):
                text = text[len("np.float64("):-1]
            try:
                return float(text)
            except ValueError:
                continue
    return None


def main():
    with open(EXECUTED_NOTEBOOK, encoding="utf-8") as f:
        nb = json.load(f)
    cells = nb["cells"]

    failures = []
    for needle, expected in CHECKS:
        match = next(
            (c for c in cells if c["cell_type"] == "code" and needle in "".join(c["source"])),
            None,
        )
        if match is None:
            failures.append(f"could not find a cell containing: {needle!r}")
            continue
        actual = cell_output_float(match)
        if actual is None:
            failures.append(f"cell for {needle!r} produced no readable numeric output")
            continue
        if abs(actual - expected) > TOLERANCE:
            failures.append(
                f"{needle!r}: expected {expected}, got {actual} (diff {abs(actual - expected):.2e})"
            )
        else:
            print(f"OK  {needle[:50]!r:52s} -> {actual}")

    if failures:
        print("\nVaR CHECK FAILED:")
        for f_ in failures:
            print(" -", f_)
        sys.exit(1)

    print("\nAll VaR checks passed - notebook output matches known-correct values.")


if __name__ == "__main__":
    main()
