# Proof-of-Existence License Protocol v0.1  
## One-Page Overview

The **Proof-of-Existence License Protocol v0.1** is a minimal protocol for proving that a subject created, signed, and anchored a trace at a specific time.

It provides the trust foundation for systems such as **Kazene Royalty OS / 印税OS**, which may later evaluate contribution, trace weight, royalty eligibility, or value circulation.

---

## 1. Core Idea

```text
Proof-of-Existence OS = proves subjects, origins, and traces
Kazene Royalty OS     = evaluates contribution, weight, and allocation
```

In Japanese:

```text
存在証明OS = 起源の保証
印税OS     = 価値の循環
```

The protocol does not distribute money.  
It proves the authenticity of traces before value systems evaluate them.

---

## 2. Why It Exists

AI-era systems increasingly absorb prompts, outputs, code, documents, revisions, and design traces.

Without a proof layer, it becomes difficult to answer:

```text
Who created the trace?
When did it exist?
Was it altered?
Can the subject later make a valid claim?
```

This protocol answers those questions at the structural and cryptographic level.

---

## 3. What It Proves

A valid Proof-of-Existence License record can prove:

- a subject was registered
- a public key was bound to that subject
- a trace hash was signed
- the trace existed at a specific time
- the trace hash was included in a Merkle Root
- the subject may make a protocol-level claim

It does not prove final economic value or legal authorship by itself.

---

## 4. Core Flow

```text
1. Register subject
2. Issue Proof-of-Existence License
3. Hash trace content
4. Sign trace hash
5. Add trace hash to Merkle Tree
6. Anchor Merkle Root
7. Verify inclusion proof
8. Submit verified claim to external systems
```

Short form:

```text
Existence → Trace → Signature → Anchor → Claim → Evaluation
```

Japanese form:

```text
存在 → 痕跡 → 署名 → 固定 → 主張 → 評価
```

---

## 5. Layer Model

```text
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
```

---

## 6. Main Record Components

A valid v0.1 record contains:

```text
schema_version
protocol
license_certificate
trace_record
merkle_anchor_record
merkle_inclusion_proof
claim
verification_result
```

---

## 7. License Certificate

The license certificate binds a subject to a public key.

It includes:

- `license_id`
- `subject_id`
- `subject_type`
- `public_key`
- `key_algorithm`
- `issued_at`
- `expires_at`
- `issuer_id`
- `issuer_signature`
- `status`

Supported subject types:

```text
human
ai_agent
organization
collective
system
```

---

## 8. Trace Record

A trace record proves that a subject signed a trace hash.

Supported trace types include:

```text
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
```

The raw trace does not need to be public.  
Hash-only verification is supported by default.

---

## 9. Merkle Anchor

Merkle anchoring allows many trace hashes to be fixed as one root hash.

Supported anchor mechanisms include:

```text
public_blockchain
private_ledger
transparency_log
timestamping_service
git_commit
other
```

The protocol is ledger-neutral.  
It does not require a public blockchain.

---

## 10. Claim Types

Supported claim types in v0.1:

```text
contribution_claim
origin_claim
authorship_claim
royalty_claim
privacy_preserving_claim
```

A claim is a protocol-level assertion.  
It may later be evaluated by external systems, but it does not automatically create legal rights.

---

## 11. What This Protocol Does Not Do

This protocol does not:

- distribute money
- define a cryptocurrency
- require NFTs
- require a public blockchain
- calculate final royalties
- determine legal authorship
- replace copyright law
- replace contracts
- decide moral or economic value

It proves trace authenticity.  
It does not decide final value.

---

## 12. Relationship to Kazene Royalty OS

Proof-of-Existence License Protocol outputs:

```text
verified_subject
verified_trace
verified_anchor
verified_claim
```

Kazene Royalty OS may then evaluate:

```text
contribution_score
trace_weight
royalty_eligibility
q_coin_allocation
```

Connection:

```text
Proof-of-Existence License Protocol
  → verifies existence and trace authenticity

Kazene Royalty OS
  → evaluates contribution and value circulation
```

---

## 13. Privacy Model

The protocol is privacy-first.

Raw trace disclosure is not required by default.

Supported privacy patterns:

- hash-only records
- encrypted trace storage
- selective disclosure
- pseudonymous subject IDs
- optional Zero-Knowledge Proof extension

ZKP support is planned for v0.2.

---

## 14. Security Notes

Important limitations:

- a hash proves existence, not meaning
- Merkle inclusion proves inclusion, not truth
- a valid signature proves key control, not legal authorship
- a claim proves eligibility for evaluation, not automatic payment
- Sybil resistance requires additional identity or reputation layers
- legal recognition requires contracts, institutions, or law

---

## 15. Repository Files

```text
README.md
CONTRIBUTING.md
CHANGELOG.md
SECURITY.md
CITATION.cff
spec/proof-of-existence-license-v0.1.yaml
schema/proof-of-existence-license-v0.1.schema.json
examples/proof-of-existence-license.sample.json
examples/pass/
examples/fail/
tests/run-compliance-tests.py
docs/one-page-overview.md
.github/workflows/validate-specs.yml
```

---

## 16. Validation

The sample JSON can be validated against the schema:

```text
examples/proof-of-existence-license.sample.json
```

using:

```text
schema/proof-of-existence-license-v0.1.schema.json
```

Compliance tests also verify that:

```text
examples/pass/*.json must pass
examples/fail/*.json must fail
```

Run:

```bash
python tests/run-compliance-tests.py
```

GitHub Actions can automatically run this validation on push and pull request.

---

## 17. Roadmap

### v0.1

- license certificate
- signed trace record
- Merkle anchor
- inclusion proof
- claim structure
- JSON Schema validation
- pass / fail compliance tests

### v0.2

- Zero-Knowledge Proof extension
- selective disclosure
- private claim verification

### v0.3

- Kazene Royalty OS integration
- contribution scoring interface
- trace weighting interface

### v0.4

- AI agent adapter
- GitHub-style trace adapter
- Copilot-style trace adapter

### v1.0

- stable protocol
- multi-issuer interoperability
- production-grade verification
- legal and institutional mapping

---

## 18. One-Line Summary

```text
The Proof-of-Existence License Protocol proves that a trace existed, was signed, and can support later contribution or royalty evaluation.
```

Japanese:

```text
存在証明ライセンス・プロトコルは、痕跡が存在し、署名され、後の寄与評価や分配判断の根拠になりうることを証明する。
```

---

## Final Formula

```text
Existence → Trace → Proof → Claim → Contribution → Circulation
```

```text
存在 → 痕跡 → 証明 → 主張 → 寄与 → 循環
```
