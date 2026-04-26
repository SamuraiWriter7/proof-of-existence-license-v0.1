#!/usr/bin/env python3
"""
Compliance test runner for Proof-of-Existence License Protocol v0.1.

This script validates:

- examples/pass/*.json must pass JSON Schema validation
- examples/fail/*.json must fail JSON Schema validation

It checks structural compliance only.
It does not verify real cryptographic signatures, real Merkle proofs,
or real ledger anchors.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Iterable

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]

SCHEMA_PATH = ROOT / "schema" / "proof-of-existence-license-v0.1.schema.json"
PASS_DIR = ROOT / "examples" / "pass"
FAIL_DIR = ROOT / "examples" / "fail"


def load_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Invalid JSON in {path}: {exc}") from exc


def collect_json_files(directory: Path) -> list[Path]:
    if not directory.exists():
        raise FileNotFoundError(f"Directory not found: {directory}")

    files = sorted(directory.glob("*.json"))

    if not files:
        raise FileNotFoundError(f"No JSON files found in: {directory}")

    return files


def format_error_path(error) -> str:
    path = ".".join(str(part) for part in error.path)
    return path or "<root>"


def validate_file(
    validator: Draft202012Validator,
    path: Path
) -> list[str]:
    instance = load_json(path)

    errors = sorted(
        validator.iter_errors(instance),
        key=lambda e: list(e.path)
    )

    return [
        f"{format_error_path(error)}: {error.message}"
        for error in errors
    ]


def run_pass_tests(
    validator: Draft202012Validator,
    files: Iterable[Path]
) -> int:
    failures = 0

    print("\n== PASS examples ==")

    for path in files:
        errors = validate_file(validator, path)

        if errors:
            failures += 1
            print(f"[FAIL] Expected pass but validation failed: {path.relative_to(ROOT)}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"[PASS] {path.relative_to(ROOT)}")

    return failures


def run_fail_tests(
    validator: Draft202012Validator,
    files: Iterable[Path]
) -> int:
    failures = 0

    print("\n== FAIL examples ==")

    for path in files:
        errors = validate_file(validator, path)

        if errors:
            print(f"[PASS] Expected failure detected: {path.relative_to(ROOT)}")
            for error in errors[:3]:
                print(f"  - {error}")
            if len(errors) > 3:
                print(f"  - ... and {len(errors) - 3} more error(s)")
        else:
            failures += 1
            print(f"[FAIL] Expected failure but validation passed: {path.relative_to(ROOT)}")

    return failures


def main() -> int:
    if not SCHEMA_PATH.exists():
        print(f"Schema not found: {SCHEMA_PATH}", file=sys.stderr)
        return 1

    schema = load_json(SCHEMA_PATH)

    validator = Draft202012Validator(
        schema,
        format_checker=FormatChecker()
    )

    pass_files = collect_json_files(PASS_DIR)
    fail_files = collect_json_files(FAIL_DIR)

    total_failures = 0

    total_failures += run_pass_tests(validator, pass_files)
    total_failures += run_fail_tests(validator, fail_files)

    print("\n== Summary ==")

    if total_failures:
        print(f"Compliance tests failed: {total_failures} issue(s)")
        return 1

    print("All compliance tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

実行コマンド
python -m pip install jsonschema
python tests/run-compliance-tests.py

期待される出力イメージ：

== PASS examples ==
[PASS] examples/pass/valid-ai-agent-git-anchor.json
[PASS] examples/pass/valid-human-basic.json

== FAIL examples ==
[PASS] Expected failure detected: examples/fail/invalid-hash-format.json
  - trace_record.trace_hash: 'sha256-badhashformat001' does not match '^(sha256|sha3-256|blake3):[a-zA-Z0-9]+$'
[PASS] Expected failure detected: examples/fail/invalid-subject-type.json
  - license_certificate.subject_type: 'ghost' is not one of ['human', 'ai_agent', 'organization', 'collective', 'system']
[PASS] Expected failure detected: examples/fail/missing-trace-signature.json
  - trace_record: 'signature' is a required property

== Summary ==
All compliance tests passed.
