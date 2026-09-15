#!/usr/bin/env python3
"""Sepsis Risk Prediction Model - Day $(date +%Y-%m-%d)"""
import json
from datetime import datetime

class SepsisPredictor:
    """Early sepsis detection system using clinical indicators"""
    
    def predict(self, vitals, labs):
        """Predict sepsis risk (0-1 score)"""
        risk_score = 0.0
        
        # SIRS criteria
        if vitals.get('heart_rate', 0) > 90: risk_score += 0.15
        if vitals.get('temperature', 0) > 38.0: risk_score += 0.15
        if vitals.get('respiratory_rate', 0) > 20: risk_score += 0.15
        
        # Lab abnormalities
        if labs.get('wbc', 0) > 12 or labs.get('wbc', 0) < 4: risk_score += 0.15
        if labs.get('lactate', 0) > 2: risk_score += 0.2
        if labs.get('procalcitonin', 0) > 0.5: risk_score += 0.2
        
        return min(risk_score, 1.0)
    
    def interpret(self, score):
        if score < 0.3: return "LOW"
        elif score < 0.6: return "MODERATE"
        else: return "HIGH - SEPSIS ALERT"

if __name__ == "__main__":
    predictor = SepsisPredictor()
    result = predictor.predict(
        {"heart_rate": 110, "temperature": 39.2, "respiratory_rate": 24},
        {"wbc": 14, "lactate": 3.5, "procalcitonin": 1.2}
    )
    print(f"Sepsis Risk: {result:.2f} - {predictor.interpret(result)}")
