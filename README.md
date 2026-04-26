# Proof-of-Existence License Protocol v0.1

A minimal protocol for proving that a subject created, signed, and anchored a trace at a specific time.  
It provides the trust foundation for Kazene Royalty OS by verifying subjects, origins, and traces before contribution or royalty calculation.  
This protocol does not distribute value by itself; it proves the existence and authenticity of the traces that later systems may evaluate.

---

## 日本語概要

**存在証明ライセンス・プロトコル v0.1** は、主体が残した痕跡に対して、署名・ハッシュ・時刻証明・Merkle Anchor を付与するための最小プロトコルです。

このプロトコルは、印税OS / Kazene Royalty OS が寄与度推定・痕跡の重み付け・分配可能性の計算を行う前に、以下を検証するための信頼基盤として機能します。

- その主体は本当に存在するのか
- その痕跡は誰によって署名されたのか
- その痕跡は特定時点で存在していたのか
- その痕跡は改ざんされていないのか
- その痕跡を根拠に寄与・起源・分配請求を行えるのか

---

## What This Protocol Does

The Proof-of-Existence License Protocol defines a structured record format for:

- registering a subject
- binding the subject to a public key
- issuing a Proof-of-Existence License
- signing trace hashes
- anchoring trace hashes through a Merkle Root
- verifying Merkle inclusion
- making contribution or royalty-related claims
- connecting verified traces to Kazene Royalty OS

---

## What This Protocol Does Not Do

This protocol does **not**:

- distribute money
- define a cryptocurrency
- require NFTs
- require a public blockchain
- automatically create legal rights
- calculate final contribution scores
- calculate final royalties
- replace copyright, contracts, or statutory law

It only defines the trust layer that proves the existence, origin, and authenticity of traces.

---

## Core Concept


```text
Proof-of-Existence OS = proves subjects, origins, and traces
Kazene Royalty OS     = evaluates contribution, weight, and allocation

In other words:

存在証明OS = 起源の保証
印税OS     = 価値の循環

The Proof-of-Existence License is not a payment mechanism.
It is a cryptographic and structural certificate that allows later systems to evaluate verified traces.

Layer Position
[ Kazene Royalty OS / 印税OS ]
  ├─ Contribution Estimation
  ├─ Trace Weighting
  └─ Royalty Simulation

        ↑ verified traces

[ Proof-of-Existence License Protocol ]
  ├─ License Certificate
  ├─ Signed Trace Record
  ├─ Merkle Anchor Record
  ├─ Merkle Inclusion Proof
  └─ Contribution / Royalty Claim

        ↑ cryptographic primitives

[ Signature / Hash / Timestamp / Ledger Layer ]
Protocol Layers
1. Certificate Layer

Registers a subject and binds it to:

subject_id
public_key
license_id
issuer_signature
status
2. Signature Layer

Allows the licensed subject to sign trace hashes.

This proves that:

this subject signed this trace hash at this time
3. Anchor Layer

Aggregates trace hashes into a Merkle Tree and records the Merkle Root in a ledger, timestamping service, transparency log, Git commit, or other tamper-resistant reference.

4. Claim Layer

Allows a licensed subject to make protocol-level claims, such as:

contribution claim
origin claim
authorship claim
royalty claim
privacy-preserving claim
5. Verification Layer

Allows third parties to verify:

license validity
issuer signature
subject public key binding
trace signature
Merkle inclusion
claim eligibility
Repository Structure
.
├── README.md
├── spec/
│   └── proof-of-existence-license-v0.1.yaml
├── schema/
│   └── proof-of-existence-license-v0.1.schema.json
├── examples/
│   └── proof-of-existence-license.sample.json
└── .github/
    └── workflows/
        └── validate-specs.yml
Main Files
spec/proof-of-existence-license-v0.1.yaml

Human-readable protocol specification.

This file defines:

purpose
scope
architecture
entities
license certificate
trace record
Merkle anchor
claim policy
verification rules
revocation policy
recovery policy
privacy model
future roadmap
schema/proof-of-existence-license-v0.1.schema.json

Machine-verifiable JSON Schema.

This file validates whether a Proof-of-Existence License record follows the required v0.1 structure.

examples/proof-of-existence-license.sample.json

A minimal valid sample record.

This file is used to test the schema locally and through GitHub Actions.

.github/workflows/validate-specs.yml

GitHub Actions workflow that automatically validates the sample JSON against the schema.

Core Record Model

A valid Proof-of-Existence License record contains:

{
  "schema_version": "0.1",
  "protocol": {},
  "license_certificate": {},
  "trace_record": {},
  "merkle_anchor_record": {},
  "merkle_inclusion_proof": {},
  "claim": {},
  "verification_result": {}
}
License Certificate

The license certificate binds a subject to a public key.

Required fields include:

license_id
subject_id
subject_type
public_key
key_algorithm
issued_at
expires_at
issuer_id
issuer_signature
status

Supported subject types:

human
ai_agent
organization
collective
system

Supported key algorithms:

ed25519
secp256k1
rsa-pss
Trace Record

A trace record proves that a subject signed a trace hash.

A trace may represent:

prompt
output
code
document
revision
dataset reference
design
specification
decision
interaction
other traceable event

The raw trace does not need to be public.
The protocol is privacy-first and supports hash-only verification.

Merkle Anchor Record

A Merkle Anchor Record proves that a trace hash was included in a specific batch at a specific time.

Supported ledger types include:

public_blockchain
private_ledger
transparency_log
timestamping_service
git_commit
other

This means the protocol does not depend on one specific blockchain.
A Git commit or transparency log may also be used as an anchoring mechanism.

Claim Types

Supported claim types in v0.1:

contribution_claim
origin_claim
authorship_claim
royalty_claim
privacy_preserving_claim

A claim does not automatically create a legal right.
It creates a verifiable protocol-level assertion that may be evaluated by external systems.

Schema Usage

This repository includes a JSON Schema and a sample JSON record.

Use the schema to validate that the sample record follows the Proof-of-Existence License Protocol v0.1 structure.

Install dependencies
python -m pip install jsonschema
Validate locally

Run the following command from the repository root:

python - <<'PY'
import json
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

schema = json.loads(
    Path("schema/proof-of-existence-license-v0.1.schema.json").read_text(
        encoding="utf-8"
    )
)

sample = json.loads(
    Path("examples/proof-of-existence-license.sample.json").read_text(
        encoding="utf-8"
    )
)

validator = Draft202012Validator(
    schema,
    format_checker=FormatChecker()
)

errors = sorted(
    validator.iter_errors(sample),
    key=lambda e: list(e.path)
)

if errors:
    print("Validation failed:")
    for error in errors:
        path = ".".join(str(p) for p in error.path) or "<root>"
        print(f"- {path}: {error.message}")
    raise SystemExit(1)

print("Validation passed.")
PY

Expected output:

Validation passed.
GitHub Actions Validation

This repository includes a GitHub Actions workflow:

.github/workflows/validate-specs.yml

The workflow runs automatically on:

push
pull request
manual dispatch

It validates:

examples/proof-of-existence-license.sample.json

against:

schema/proof-of-existence-license-v0.1.schema.json

The workflow also prints the repository file tree to help debug file path issues.

Verification Flow
1. Check license exists
2. Check license status is active
3. Verify issuer signature
4. Verify subject public key binding
5. Verify trace signature
6. Verify trace hash
7. Verify Merkle inclusion proof
8. Verify claim type
9. Forward verified claim to contribution or royalty system
Integration with Kazene Royalty OS

The Proof-of-Existence License Protocol provides verified traces to Kazene Royalty OS.

Proof-of-Existence License Protocol
  └─ verified_subject
  └─ verified_trace
  └─ verified_anchor
  └─ verified_claim

Kazene Royalty OS
  └─ contribution_score
  └─ trace_weight
  └─ royalty_eligibility
  └─ q_coin_allocation

The connection can be summarized as:

存在証明OS:
Who existed?
Who signed?
What trace existed?
When was it anchored?

印税OS:
How much did it contribute?
How should it be weighted?
Is it eligible for allocation?
How should value circulate?
Privacy Model

The protocol is designed for privacy-preserving trace verification.

Raw trace disclosure is not required by default.

Supported privacy patterns:

hash-only records
encrypted trace storage
selective disclosure
pseudonymous subject IDs
optional Zero-Knowledge Proof extension
ZKP Extension

Zero-Knowledge Proof support is optional in v0.1.

Future versions may allow a subject to prove:

trace inclusion without revealing the trace
license validity without revealing full identity
valid signature without exposing all metadata
contribution eligibility without disclosing raw logs

Planned target version:

v0.2
Security Considerations
Private keys must be protected.
Key compromise may affect trust in future traces.
Past traces should not be invalidated by default unless compromise timing is proven.
Hash-only records prove existence, not semantic value.
Merkle inclusion proves inclusion, not truthfulness.
Sybil resistance requires identity, reputation, issuer, or anomaly-detection layers.
Legal recognition requires contracts, terms, institutions, or applicable law.
Royalty claims require separate contribution and allocation logic.
Revocation and Recovery

A license may be revoked for:

key compromise
subject request
issuer decision
fraudulent activity
duplicate identity
protocol violation
legal order
expiration

Past traces remain valid by default unless the key was compromised before those traces were signed.

Supported recovery methods may include:

recovery key
multi-signature guardian
issuer recovery
hardware key backup
social recovery
legal identity verification
Version Roadmap
v0.1

Focus:

license certificate
signed trace record
Merkle anchor
Merkle inclusion proof
basic claim policy
JSON Schema validation
v0.2

Focus:

Zero-Knowledge Proof extension
selective disclosure
private claim verification
v0.3

Focus:

Kazene Royalty OS integration
contribution scoring interface
trace weighting interface
royalty eligibility interface
v0.4

Focus:

AI agent integration
GitHub / Copilot-style trace adapter
automated verification workflows
v1.0

Focus:

stable protocol
legal mapping
multi-issuer interoperability
production-grade verification
Non-Goals

This protocol does not aim to:

define final legal authorship
replace copyright law
enforce royalty payments
create a cryptocurrency
require NFTs
force public disclosure of raw traces
determine the moral value of a contribution
become a centralized identity authority
Status
Version: v0.1
Status: Draft
Compatibility: Experimental

This specification is an early structural draft.
It is intended for discussion, validation, prototyping, and future integration with Kazene Royalty OS.

License Notice

This specification defines a structural protocol for cryptographically proving existence, traces, origins, and contribution.

It does not create legal rights by itself.

Legal effect requires integration with:

contracts
terms of service
institutional rules
statutory law
judicial recognition
governance frameworks
Summary

The Proof-of-Existence License Protocol v0.1 provides the trust foundation for AI-era trace systems.

It answers:

Who existed?
Who signed?
What trace existed?
When was it anchored?
Can this trace support a later claim?

Kazene Royalty OS can then answer:

How much did it contribute?
How should it be weighted?
Can it be included in allocation?
How should value circulate?

Together, they form a layered architecture:

Existence → Trace → Claim → Contribution → Circulation

In Japanese:

存在 → 痕跡 → 主張 → 寄与 → 循環

This is the foundation for a future where traces are not silently absorbed, but verified, preserved, and connected to fair value circulation.
