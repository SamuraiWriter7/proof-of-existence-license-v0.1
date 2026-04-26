# Security Policy

This document describes the security model, reporting process, and known risk areas for the **Proof-of-Existence License Protocol v0.1**.

The protocol is designed to prove the existence, origin, signature, anchoring, and claim eligibility of traces before those traces are evaluated by external systems such as Kazene Royalty OS.

---

## Supported Versions

| Version | Status | Security Support |
|---|---|---|
| v0.1.x | Draft / Experimental | Supported for review and hardening |
| v0.2.x | Planned | Not yet supported |
| v1.0.x | Future stable | Not yet available |

Current supported version:

```text
v0.1.x

Scope

Security reports may involve:

license certificate structure
public key binding
signature verification assumptions
trace hash validation
Merkle inclusion proof structure
Merkle anchor ambiguity
claim eligibility logic
JSON Schema validation gaps
GitHub Actions validation workflow
privacy leakage through metadata
key revocation and recovery logic
Sybil-resistance design
replay attacks
forged or misleading trace claims
Out of Scope

The following are outside the direct scope of this repository:

final legal authorship decisions
copyright enforcement
monetary royalty enforcement
cryptocurrency or token economics
production identity verification
real-world court recognition
platform-specific enforcement by GitHub, Copilot, or other AI providers
private key custody services
actual Zero-Knowledge Proof implementation in v0.1

This repository defines a structural protocol and validation format.
It does not provide legal, financial, or identity-custody services.

Reporting a Vulnerability

If you discover a security issue, please report it responsibly.

Preferred reporting path:

Use GitHub Security Advisories if enabled.
If private reporting is not available, open a minimal public issue without exploit details.
Clearly mark the issue as security-related.
Avoid posting private keys, real signatures, raw traces, personal data, or exploit-ready payloads.

Please include:

What is the issue?
Which file or field is affected?
How could the issue be exploited?
Does it affect schema validation, privacy, trace integrity, or claim validity?
What mitigation do you suggest?
Security Design Principles
1. Proof before allocation

The protocol should only prove:

Who existed?
Who signed?
What trace existed?
When was it anchored?
Can the trace support a later claim?

It should not directly determine:

Who legally owns the work?
How valuable is the contribution?
How much should be paid?
Who must pay whom?
2. Privacy by default

Raw trace disclosure should not be required.

Preferred patterns:

hash-only records
encrypted raw trace storage
selective disclosure
pseudonymous subject IDs
optional Zero-Knowledge Proof extensions
minimal metadata exposure
3. Ledger neutrality

The protocol must not depend on a single blockchain or ledger.

Supported anchoring mechanisms may include:

public blockchain
private ledger
transparency log
timestamping service
Git commit
other tamper-resistant records
4. Revocation must not erase history by default

If a key is revoked, past traces should remain valid unless there is evidence that the key was compromised before those traces were signed.

Recommended rule:

Future signing disabled.
Past traces preserved unless compromise timing invalidates them.
Threat Model
Private Key Compromise

If a subject's private key is compromised, an attacker may sign fraudulent traces.

Mitigations:

key revocation
key rotation
issuer confirmation
recovery keys
multi-signature guardians
hardware key backup
anomaly detection
Signature Replay

An attacker may attempt to reuse a valid signature in a different context.

Mitigations:

include trace_id
include trace_hash
include subject_id
include license_id
include created_at
include signed_at
bind signature to canonical metadata
Trace Inflation

A subject may generate large numbers of low-value traces to create the appearance of contribution.

Mitigations:

rate limiting
reputation scoring
issuer approval
anomaly detection
contribution scoring outside this protocol
separation between proof and value
Sybil Attacks

An attacker may create many fake subjects or licenses.

Mitigations may include:

proof-of-personhood
organization verification
web-of-trust
issuer approval
device attestation
reputation score
stake or bond
anomaly detection

Sybil resistance is not fully solved in v0.1.

Metadata Leakage

Even if raw traces are hidden, metadata may reveal sensitive information.

Possible leaks:

timing patterns
subject identifiers
trace type
ledger reference
batch size
claim type
verifier identity

Mitigations:

pseudonymous IDs
minimal metadata
batching
delayed anchoring
encrypted metadata
ZKP extensions in future versions
Merkle Inclusion Misinterpretation

Merkle inclusion proves that a trace hash was included in a batch.

It does not prove:

the trace is meaningful
the trace is original
the trace has legal value
the trace deserves payment
the raw content is true

Merkle inclusion proves inclusion, not truth.

Hash-Only Limitation

A hash proves that a specific input existed, assuming the original input can be later revealed or verified.

A hash alone does not prove:

semantic meaning
originality
authorship under law
economic value
moral merit
False Royalty Claims

A subject may claim royalty eligibility based on a valid trace that has little or no actual contribution.

Mitigation:

Proof-of-Existence License Protocol verifies trace authenticity.
Kazene Royalty OS or external systems must evaluate contribution value.
Validation Security

The JSON Schema validates structure.

It does not validate:

real cryptographic signatures
actual Merkle proof correctness
real ledger existence
legal identity
true authorship
economic contribution

The schema checks shape, not truth.

Recommended Future Security Work

Planned security improvements:

invalid sample test vectors
compliance test runner
stricter cross-field validation
canonicalization rules
signature payload test fixtures
Merkle proof test fixtures
revocation list format
recovery flow examples
ZKP extension draft
privacy-preserving claim verification
Sybil-resistance guidance
Security Summary

This protocol should be read as a trust foundation, not as a complete enforcement system.

It proves existence.
It proves signature.
It proves anchoring.
It supports claims.
It does not decide final value.
It does not enforce payment.
It does not replace law.

In Japanese:

存在を証明する。
痕跡を固定する。
署名を検証する。
主張の入口をつくる。
だが、価値判断と法的執行は別レイヤーである。

---

# `CITATION.cff`

```yaml
cff-version: 1.2.0
message: "If you use this specification, please cite it as below."

title: "Proof-of-Existence License Protocol v0.1"
abstract: >
  The Proof-of-Existence License Protocol v0.1 defines a minimal
  structural protocol for proving that a subject created, signed,
  and anchored a trace at a specific time. It provides a trust layer
  for verifying subjects, origins, signed traces, Merkle anchors,
  and claim eligibility before external systems such as Kazene
  Royalty OS evaluate contribution, trace weight, or royalty allocation.

type: software
version: "0.1.0"

authors:
  - name: "Shidenkai Alpha"
    alias: "Kazene"

repository-code: "https://github.com/SamuraiWriter7/proof-of-existence-license-protocol"
url: "https://github.com/SamuraiWriter7/proof-of-existence-license-protocol"

keywords:
  - proof-of-existence
  - digital-signature
  - merkle-tree
  - traceability
  - provenance
  - kazene
  - royalty-os
  - ai-governance
  - contribution-tracking
  - origin-verification
  - license-protocol
  - zero-knowledge-proof

license: "CC-BY-4.0"

date-released: "2026-04-25"

preferred-citation:
  type: generic
  title: "Proof-of-Existence License Protocol v0.1"
  authors:
    - name: "Shidenkai Alpha"
      alias: "Kazene"
  version: "0.1.0"
  year: 2026
  url: "https://github.com/SamuraiWriter7/proof-of-existence-license-protocol"
docs/one-page-overview.md
# Proof-of-Existence License Protocol v0.1  
## One-Page Overview

The **Proof-of-Existence License Protocol v0.1** is a minimal protocol for proving that a subject created, signed, and anchored a trace at a specific time.

It provides the trust foundation for systems such as **Kazene Royalty OS / 印税OS**, which may later evaluate contribution, trace weight, royalty eligibility, or value circulation.

---

## 1. Core Idea

```text
Proof-of-Existence OS = proves subjects, origins, and traces
Kazene Royalty OS     = evaluates contribution, weight, and allocation

In Japanese:

存在証明OS = 起源の保証
印税OS     = 価値の循環

The protocol does not distribute money.
It proves the authenticity of traces before value systems evaluate them.

2. Why It Exists

AI-era systems increasingly absorb prompts, outputs, code, documents, revisions, and design traces.

Without a proof layer, it becomes difficult to answer:

Who created the trace?
When did it exist?
Was it altered?
Can the subject later make a valid claim?

This protocol answers those questions at the structural and cryptographic level.

3. What It Proves

A valid Proof-of-Existence License record can prove:

a subject was registered
a public key was bound to that subject
a trace hash was signed
the trace existed at a specific time
the trace hash was included in a Merkle Root
the subject may make a protocol-level claim

It does not prove final economic value or legal authorship by itself.

4. Core Flow
1. Register subject
2. Issue Proof-of-Existence License
3. Hash trace content
4. Sign trace hash
5. Add trace hash to Merkle Tree
6. Anchor Merkle Root
7. Verify inclusion proof
8. Submit verified claim to external systems

Short form:

Existence → Trace → Signature → Anchor → Claim → Evaluation

Japanese form:

存在 → 痕跡 → 署名 → 固定 → 主張 → 評価
5. Layer Model
[ Kazene Royalty OS / 印税OS ]
  ├─ Contribution Estimation
  ├─ Trace Weighting
  └─ Royalty Simulation

        ↑ verified traces and claims

[ Proof-of-Existence License Protocol ]
  ├─ License Certificate
  ├─ Signed Trace Record
  ├─ Merkle Anchor Record
  ├─ Merkle Inclusion Proof
  └─ Claim Record

        ↑ cryptographic primitives

[ Signature / Hash / Timestamp / Ledger Layer ]
6. Main Record Components

A valid v0.1 record contains:

schema_version
protocol
license_certificate
trace_record
merkle_anchor_record
merkle_inclusion_proof
claim
verification_result
7. License Certificate

The license certificate binds a subject to a public key.

It includes:

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
8. Trace Record

A trace record proves that a subject signed a trace hash.

Supported trace types include:

prompt
output
code
document
revision
dataset_reference
design
specification
decision
interaction
other

The raw trace does not need to be public.
Hash-only verification is supported by default.

9. Merkle Anchor

Merkle anchoring allows many trace hashes to be fixed as one root hash.

Supported anchor mechanisms include:

public_blockchain
private_ledger
transparency_log
timestamping_service
git_commit
other

The protocol is ledger-neutral.
It does not require a public blockchain.

10. Claim Types

Supported claim types in v0.1:

contribution_claim
origin_claim
authorship_claim
royalty_claim
privacy_preserving_claim

A claim is a protocol-level assertion.
It may later be evaluated by external systems, but it does not automatically create legal rights.

11. What This Protocol Does Not Do

This protocol does not:

distribute money
define a cryptocurrency
require NFTs
require a public blockchain
calculate final royalties
determine legal authorship
replace copyright law
replace contracts
decide moral or economic value

It proves trace authenticity.
It does not decide final value.

12. Relationship to Kazene Royalty OS

Proof-of-Existence License Protocol outputs:

verified_subject
verified_trace
verified_anchor
verified_claim

Kazene Royalty OS may then evaluate:

contribution_score
trace_weight
royalty_eligibility
q_coin_allocation

Connection:

Proof-of-Existence License Protocol
  → verifies existence and trace authenticity

Kazene Royalty OS
  → evaluates contribution and value circulation
13. Privacy Model

The protocol is privacy-first.

Raw trace disclosure is not required by default.

Supported privacy patterns:

hash-only records
encrypted trace storage
selective disclosure
pseudonymous subject IDs
optional Zero-Knowledge Proof extension

ZKP support is planned for v0.2.

14. Security Notes

Important limitations:

a hash proves existence, not meaning
Merkle inclusion proves inclusion, not truth
a valid signature proves key control, not legal authorship
a claim proves eligibility for evaluation, not automatic payment
Sybil resistance requires additional identity or reputation layers
legal recognition requires contracts, institutions, or law
15. Repository Files
README.md
CONTRIBUTING.md
CHANGELOG.md
SECURITY.md
CITATION.cff
spec/proof-of-existence-license-v0.1.yaml
schema/proof-of-existence-license-v0.1.schema.json
examples/proof-of-existence-license.sample.json
docs/one-page-overview.md
.github/workflows/validate-specs.yml
16. Validation

The sample JSON can be validated against the schema:

examples/proof-of-existence-license.sample.json

using:

schema/proof-of-existence-license-v0.1.schema.json

GitHub Actions can automatically run this validation on push and pull request.

17. Roadmap
v0.1
license certificate
signed trace record
Merkle anchor
inclusion proof
claim structure
JSON Schema validation
v0.2
Zero-Knowledge Proof extension
selective disclosure
private claim verification
v0.3
Kazene Royalty OS integration
contribution scoring interface
trace weighting interface
v0.4
AI agent adapter
GitHub-style trace adapter
Copilot-style trace adapter
v1.0
stable protocol
multi-issuer interoperability
production-grade verification
legal and institutional mapping
18. One-Line Summary
The Proof-of-Existence License Protocol proves that a trace existed, was signed, and can support later contribution or royalty evaluation.

Japanese:

存在証明ライセンス・プロトコルは、痕跡が存在し、署名され、後の寄与評価や分配判断の根拠になりうることを証明する。
Final Formula
Existence → Trace → Proof → Claim → Contribution → Circulation
存在 → 痕跡 → 証明 → 主張 → 寄与 → 循環
