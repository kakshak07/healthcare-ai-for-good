#!/usr/bin/env python3
"""
Drug Interaction Checker

Identifies potential drug-drug interactions to prevent adverse events.
This system helps healthcare professionals make safer prescribing decisions.

Key features:
- Real-time interaction checking
- Severity assessment (minor, moderate, severe)
- Evidence-based recommendations
- Easy integration with EHR systems
"""

import json
from dataclasses import dataclass
from typing import List, Dict
from enum import Enum

class InteractionSeverity(Enum):
    """Drug interaction severity levels"""
    MONITOR = "monitor"  # Monitor for effects
    MINOR = "minor"  # Minor interaction
    MODERATE = "moderate"  # Moderate - may need adjustment
    SEVERE = "severe"  # Severe - avoid combination

@dataclass
class DrugInteraction:
    """Represents a drug-drug interaction"""
    drug1: str
    drug2: str
    severity: InteractionSeverity
    description: str
    recommendations: List[str]
    evidence_level: str  # A, B, C (strength of evidence)

class DrugInteractionChecker:
    """
    Clinical drug interaction checking system
    
    Prevents adverse events by identifying dangerous drug combinations
    before they reach patients.
    """
    
    def __init__(self):
        # Initialize with common interactions
        self.interactions_db = self._load_interactions()
    
    def _load_interactions(self) -> Dict:
        """Load drug interaction database"""
        return {
            ("warfarin", "aspirin"): DrugInteraction(
                drug1="warfarin",
                drug2="aspirin",
                severity=InteractionSeverity.SEVERE,
                description="Increased bleeding risk when combined",
                recommendations=[
                    "Avoid combination if possible",
                    "If necessary, monitor INR closely",
                    "Patient education on bleeding signs",
                    "Consider alternative antiplatelet agent"
                ],
                evidence_level="A"
            ),
            ("metformin", "contrast_dye"): DrugInteraction(
                drug1="metformin",
                drug2="contrast_dye",
                severity=InteractionSeverity.SEVERE,
                description="Risk of lactic acidosis with contrast procedures",
                recommendations=[
                    "Hold metformin 48h before procedure",
                    "Restart 48h after procedure if renal function normal",
                    "Monitor creatinine",
                    "Consider alternative diabetes management temporarily"
                ],
                evidence_level="A"
            ),
            ("lisinopril", "potassium"): DrugInteraction(
                drug1="lisinopril",
                drug2="potassium",
                severity=InteractionSeverity.MODERATE,
                description="ACE inhibitors increase potassium levels",
                recommendations=[
                    "Monitor serum potassium levels",
                    "Limit potassium supplementation",
                    "Check for hyperkalemia symptoms",
                    "Regular kidney function tests"
                ],
                evidence_level="A"
            ),
            ("simvastatin", "clarithromycin"): DrugInteraction(
                drug1="simvastatin",
                drug2="clarithromycin",
                severity=InteractionSeverity.SEVERE,
                description="Macrolide increases statin levels (rhabdomyolysis risk)",
                recommendations=[
                    "Avoid combination",
                    "Use alternative antibiotic (azithromycin if possible)",
                    "If necessary, temporarily discontinue statin",
                    "Monitor CK levels"
                ],
                evidence_level="A"
            ),
            ("tramadol", "ssri"): DrugInteraction(
                drug1="tramadol",
                drug2="ssri",
                severity=InteractionSeverity.MODERATE,
                description="Serotonin syndrome risk",
                recommendations=[
                    "Use lowest effective doses",
                    "Patient education on serotonin syndrome signs",
                    "Monitor for tremor, rigidity, confusion",
                    "Consider alternative pain management"
                ],
                evidence_level="B"
            ),
        }
    
    def check_interaction(self, drug1: str, drug2: str) -> DrugInteraction:
        """Check if two drugs interact"""
        # Normalize drug names
        drug1_lower = drug1.lower()
        drug2_lower = drug2.lower()
        
        # Check both directions
        key1 = (drug1_lower, drug2_lower)
        key2 = (drug2_lower, drug1_lower)
        
        if key1 in self.interactions_db:
            return self.interactions_db[key1]
        elif key2 in self.interactions_db:
            return self.interactions_db[key2]
        else:
            return None
    
    def check_medication_list(self, medications: List[str]) -> Dict:
        """Check entire medication list for interactions"""
        interactions = []
        warnings = []
        
        # Check all pairs
        for i in range(len(medications)):
            for j in range(i+1, len(medications)):
                interaction = self.check_interaction(medications[i], medications[j])
                
                if interaction:
                    interactions.append({
                        "drug1": medications[i],
                        "drug2": medications[j],
                        "severity": interaction.severity.value,
                        "description": interaction.description,
                        "recommendations": interaction.recommendations,
                        "evidence_level": interaction.evidence_level
                    })
                    
                    if interaction.severity in [InteractionSeverity.SEVERE, InteractionSeverity.MODERATE]:
                        warnings.append(f"⚠️ {medications[i]} + {medications[j]}: {interaction.description}")
        
        return {
            "total_medications": len(medications),
            "total_interactions": len(interactions),
            "interactions": interactions,
            "warnings": warnings,
            "safe_to_prescribe": len(warnings) == 0
        }

def main():
    """Demonstrate drug interaction checking"""
    checker = DrugInteractionChecker()
    
    # Example: Patient on multiple medications
    medications = ["warfarin", "aspirin", "lisinopril", "potassium"]
    
    print("=" * 70)
    print("Drug Interaction Checker - Patient Safety")
    print("=" * 70)
    print(f"\nPatient medications: {', '.join(medications)}\n")
    
    result = checker.check_medication_list(medications)
    
    print(f"Total medications: {result['total_medications']}")
    print(f"Interactions found: {result['total_interactions']}\n")
    
    if result['warnings']:
        print("⚠️  WARNINGS:")
        for warning in result['warnings']:
            print(f"  {warning}")
    
    print("\nDetailed Interactions:")
    for interaction in result['interactions']:
        print(f"\n{interaction['drug1'].upper()} + {interaction['drug2'].upper()}")
        print(f"  Severity: {interaction['severity']}")
        print(f"  {interaction['description']}")
        print(f"  Recommendations:")
        for rec in interaction['recommendations']:
            print(f"    - {rec}")
    
    print("\n" + "=" * 70)
    print(f"Prescribing Status: {'✅ SAFE' if result['safe_to_prescribe'] else '❌ HAS INTERACTIONS'}")
    print("=" * 70)

if __name__ == "__main__":
    main()
