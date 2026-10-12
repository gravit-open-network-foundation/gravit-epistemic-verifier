# Epistemic Verification for Agentic Finance

**Reference Implementation of a New Infrastructure Layer**

Gravit Open Network Foundation

---

## What This Is

This repository defines and implements a new category of infrastructure for autonomous economic agents:

- **Epistemic Verification** — the ability of agents to verify the truthfulness and reliability of information and outcomes, not just technical correctness.
- **Agentic Auditability** — machine-native, real-time verifiability of agent actions without human intervention.
- **Semantic Settlement Verification** — context-aware confirmation that settlement fulfills the original intent, not just technical transfer.

---

## Why This Matters Now

Peter Grosskopf (CTO/COO, AllUnity) recently stated:

> *"Agentic payments isn't a feature bolt-on to existing rails. It's a separate infrastructure layer."*

We agree. And we add: this layer requires **epistemic trust**, not just speed and settlement.

This repository is a public reference implementation of that layer.

---

## What's Inside

| Component | Description |
|-----------|-------------|
| `specification/` | JSON Schemas for epistemic commitments, truth vectors, audit trails |
| `gravit_verifier/` | Research demo of a verifier, GRTVP consensus and audit generator (contains placeholders, e.g. the formal-proof step) |
| `tests/` | Adversarial tests (sandwich, replay, intent substitution) |
| `benchmarks/` | Latency script (results depend on hardware); gas figure is a hard-coded placeholder |
| `integrations/allunity/` | How EURAU/CHFAU serve as regulated anchor for this category |

---

## Results

> **Correction (12 Oct 2026).** An earlier version of this section listed "p95 latency 47 ms",
> "gas overhead 8 %", "attack success 23 % → 0.7 %" and "false positive rate 1.2 %". No code in
> this repository computes those figures (the gas value is a constant in `bench_cost.py`; the
> others appear only in a hand-written `benchmarks/results/v1.0_report.json`, kept for the record).
> They have been removed. This repository is a research demonstration.
>
> The maintained reference implementation is the
> [Gravit Verifier](https://github.com/gravit-open-network-foundation/verifier); its conformance and
> adversarial results are reproduced with one command by the
> [evaluation pack](https://github.com/gravit-open-network-foundation/gravit-eval-pack).

---

## Partnership Invitation

We invite AllUnity to co-develop this category as a strategic partner.

AllUnity (EURAU, CHFAU, Agentic Payments / x402) is the natural regulated anchor for:

- Euro-denominated epistemic verification
- Compliant semantic settlement
- Machine-native auditability for A2S and A2A models

**Proposed co-development path:**

1. Joint definition of the category (whitepaper, public specification)
2. Reference implementation with EURAU as settlement layer
3. Pilot with real agentic payments (A2S model)
4. Production-grade infrastructure with AllUnity as anchor partner

---

## Quick Start

```bash
git clone https://github.com/GravitOpenNetwork/gravit-epistemic-verifier.git
cd gravit-epistemic-verifier
docker compose up --build
curl -X POST http://localhost:8080/v1/verify -H "Content-Type: application/json" -d '{"agent_id": "test", "action": "transfer", "reasoning_chain": ["User authorized"]}'
```

## For Regulators (BaFin, FINMA, ESMA)
This repository serves as a technical reference for:
- Epistemic verification as a compliance primitive (MiCAR Art. 51, 63)
- Agentic audit trails for AI-driven financial transactions
- Semantic settlement verification for tokenized assets

## Regulatory Documents
- MiCAR Compliance Matrix
- Regulatory Sandbox Proposal
- Whitepaper v1.0

## License
Apache 2.0
