import re
import json
from typing import Dict, Any, List

# =====================================================================
# 1. THE FOUNDATION: LANGUAGE DEFINITIONS
# =====================================================================

class CodeDialect:
    """Represents a standard software language context or dialect."""
    def __init__(self, name: str, syntax_rules: List[str]):
        self.name = name
        self.syntax_rules = syntax_rules

class LinguisticVulnerability:
    """The 'Ma' (間) - The unexpressed, unvalidated negative space in code."""
    def __init__(self, name: str, expected_grammar: str, unhandled_space: str):
        self.name = name
        self.expected_grammar = expected_grammar
        self.unhandled_space = unhandled_space  # The silent gap left by the developer

class NaPayload:
    """
    The Malicious Payload acting as a Japanese 'Na'-adjective.
    It uses a specific 'glue' character to append an foreign meaning 
    to an unshielded noun context.
    """
    def __init__(self, payload_string: str, syntactic_glue: str, semantic_shift: str):
        self.payload_string = payload_string  # e.g., "admin' OR '1'='1"
        self.syntactic_glue = syntactic_glue  # e.g., "'" (The separator)
        self.semantic_shift = semantic_shift  # What the narrative becomes

# =====================================================================
# 2. MOCK CORPUS (Simulating 'In the Wild' Structural Deltas)
# =====================================================================

# This simulates data curated from open-source vulnerability repositories
MOCK_MALWARE_CORPUS = {
    "sql_injection_dialect": {
        "vulnerability": {
            "name": "Missing Boundary Delimiter Protection",
            "expected_grammar": "SELECT * FROM users WHERE username = [Literal String Value]",
            "unhandled_space": "Fails to enforce that the string value cannot contain structural punctuation."
        },
        "exploit_payload": {
            "string": "admin' OR '1'='1",
            "glue": "'",  # The 'Na' particle that bridges user text to code instruction
            "semantic_shift": "Changes a selective query into a universal truth (Tautology)."
        }
    }
}

# =====================================================================
# 3. THE LINGUISTIC ANALYZER ENGINE
# =====================================================================

class LinguisticMirrorAnalyzer:
    """
    Engine that analyzes code to prove that the exploit's syntax
    is the direct negative silhouette of the missing defense.
    """
    def __init__(self, corpus_entry: Dict[str, Any]):
        self.vuln = LinguisticVulnerability(
            name=corpus_entry["vulnerability"]["name"],
            expected_grammar=corpus_entry["vulnerability"]["expected_grammar"],
            unhandled_space=corpus_entry["vulnerability"]["unhandled_space"]
        )
        self.payload = NaPayload(
            payload_string=corpus_entry["exploit_payload"]["string"],
            syntactic_glue=corpus_entry["exploit_payload"]["glue"],
            semantic_shift=corpus_entry["exploit_payload"]["semantic_shift"]
        )

    def analyze_structural_fit(self) -> Dict[str, Any]:
        """Maps how the payload fits perfectly into the negative space."""
        # Check if the payload utilizes the exact weakness left open in the grammar
        glue_present_in_payload = self.payload.syntactic_glue in self.payload.payload_string
        
        # In a real model, this would use AST token distances. 
        # Here we mathematically represent the inversion score.
        inversion_symmetry_score = 1.0 if glue_present_in_payload else 0.0

        return {
            "vulnerability_name": self.vuln.name,
            "negative_space_identified": self.vuln.unhandled_space,
            "payload_used": self.payload.payload_string,
            "linguistic_glue_particle": f"'{self.payload.syntactic_glue}'",
            "narrative_transformation": self.payload.semantic_shift,
            "symmetry_score": inversion_symmetry_score
        }

# =====================================================================
# 4. REPORTING AND RESULTS GENERATION
# =====================================================================

def generate_findings_report(metrics: Dict[str, Any]):
    """Outputs the analytical findings proving the hypothesis."""
    print("=" * 70)
    print("          LINGUISTIC CODE ANALYSIS REPORT: THE SYSTEMIC 'MA'           ")
    print("=" * 70)
    print(f"[-] Subject Vulnerability : {metrics['vulnerability_name']}")
    print(f"[-] The 'Ma' (Void)       : {metrics['negative_space_identified']}")
    print(f"[-] Parasitic Syntax      : \"{metrics['payload_used']}\"")
    print(f"[-] 'Na'-Adjective Glue   : {metrics['linguistic_glue_particle']}")
    print(f"[-] Narrative Shift       : {metrics['narrative_transformation']}")
    print("-" * 70)
    print(f"[*] Symmetrical Inversion Score: {metrics['symmetry_score']} (Perfect Mirror)")
    print("-" * 70)
    print("[Conclusion Summary]")
    print("The malicious text did not invent a new path. It executed a sentence")
    print("whose structural dimensions were perfectly pre-defined by what the")
    print("developer left unsaid. The exploit behaves as a predictable, fluid")
    print("filling of the syntactic vacuum.")
    print("=" * 70)

if __name__ == "__main__":
    # Initialize the analyzer with our mock linguistic corpus entry
    analyzer = LinguisticMirrorAnalyzer(MOCK_MALWARE_CORPUS["sql_injection_dialect"])
    
    # Process the structural alignment
    findings = analyzer.analyze_structural_fit()
    
    # Print the foundational report
    generate_findings_report(findings)
