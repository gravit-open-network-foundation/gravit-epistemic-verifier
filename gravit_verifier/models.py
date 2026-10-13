"""
Data models for epistemic verification.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class EpistemicCommitment:
    agent_id: str
    action: str
    reasoning_chain: list[str] = field(default_factory=list)
    context: dict[str, Any] = field(default_factory=dict)
    provenance_root: str = ""
    timestamp: str = ""


@dataclass
class TruthVector:
    valid: float = 0.0
    invalid: float = 0.0
    need_review: float = 0.0


@dataclass
class VerificationResult:
    valid: bool
    score: float
    proof: str
    latency_ms: float
    intent_hash: str = ""
    action_hash: str = ""
    semantic_score: float = 0.0
    policy_score: float = 0.0
    adversarial_score: float = 0.0
    verdict: str = "NEEDS_AUDIT"
    lineage_commitment: str = ""
    formal_proof_available: bool = False
    audit_proof: dict[str, Any] = field(default_factory=dict)
    details: dict[str, Any] = field(default_factory=dict)


ValidationResult = VerificationResult
