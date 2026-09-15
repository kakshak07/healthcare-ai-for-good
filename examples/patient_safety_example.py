#!/usr/bin/env python3
"""
Example: Using Patient Safety Monitor

This example demonstrates how to use the Healthcare AI Patient Safety Monitor
to identify high-risk patients in real-time.
"""

from healthcare_ai.safety.monitor import PatientSafetyMonitor
import json

def main():
    """Run patient safety monitoring example"""
    
    # Initialize the monitor
    monitor = PatientSafetyMonitor()
    
    # Assess a patient (example patient ID)
    print("=" * 70)
    print("Healthcare AI - Patient Safety Monitor Example")
    print("=" * 70)
    
    assessment = monitor.assess_patient_safety("PATIENT_PT12345")
    
    print("\nPatient Risk Assessment:")
    print(f"  Patient ID: {assessment.patient_id}")
    print(f"  Overall Risk Level: {assessment.overall_risk_level.value.upper()}")
    print(f"  Confidence: {assessment.confidence_score:.0%}")
    
    print("\nIndividual Risk Scores:")
    print(f"  Sepsis Risk: {assessment.sepsis_risk:.0%}")
    print(f"  ICU Deterioration Risk: {assessment.icu_deterioration_risk:.0%}")
    print(f"  Readmission Risk: {assessment.readmission_risk:.0%}")
    print(f"  Medication Error Risk: {assessment.medication_error_risk:.0%}")
    print(f"  Fall Risk: {assessment.fall_risk:.0%}")
    
    print("\nTop Risk Factors:")
    for i, factor in enumerate(assessment.top_risk_factors, 1):
        print(f"  {i}. {factor}")
    
    print("\nRecommended Actions:")
    for i, recommendation in enumerate(assessment.recommendations, 1):
        print(f"  {i}. {recommendation}")
    
    print("\n" + "=" * 70)
    print("✓ Assessment complete")
    print("=" * 70)

if __name__ == "__main__":
    main()
