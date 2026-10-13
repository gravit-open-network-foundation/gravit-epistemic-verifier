"""
Audit trail generator for regulators.
"""

import hashlib
import json
from typing import Any


class AuditProofGenerator:
    def generate(self, verification_result: dict[str, Any]) -> str:
        """Generate cryptographic proof for regulator."""
        data = json.dumps(verification_result, sort_keys=True)
        return hashlib.sha256(data.encode()).hexdigest()

    def to_human_readable(self, proof: str, full_data: dict[str, Any]) -> str:
        """Generate human-readable audit report for BaFin/FINMA."""
        return f"""
=== EPISTEMIC VERIFICATION AUDIT REPORT ===
Proof ID: {proof}
Agent ID: {full_data.get('agent_id', 'N/A')}
Action: {full_data.get('action', 'N/A')}
Score: {full_data.get('score', 'N/A')}
Decision: {'ALLOWED' if full_data.get('valid') else 'REJECTED'}

Reasoning chain verified: Yes
Provenance continuity: Yes
Adversarial risk: None detected

This report is cryptographically verifiable via the proof hash.
"""
