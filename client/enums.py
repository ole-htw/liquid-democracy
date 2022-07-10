from enum import Enum


class Vote(Enum):
    FOR = 0
    AGAINST = 1
    NEUTRAL = 1

    def from_string(s: str):
        if s == "FOR": return Vote.FOR
        if s == "AGAINST": return Vote.AGAINST
        if s == "NEUTRAL": return Vote.NEUTRAL

    def to_string(v):
        if v == Vote.FOR: return "FOR"
        if v == Vote.AGAINST: return "AGAINST"
        if v == Vote.NEUTRAL: return "NEUTRAL"
    
    def all():
        return {Vote.FOR, Vote.AGAINST, Vote.NEUTRAL}
    
    def choices():
        return {"FOR", "AGAINST", "NEUTRAL"}

class Domain(Enum):
    EDUCATION = 0
    ECOLOGY = 1
    ECONOMY = 2
    
    def from_string(s: str):
        if s == "EDUCATION": return Domain.EDUCATION
        if s == "ECOLOGY": return Domain.ECOLOGY
        if s == "ECONOMY": return Domain.ECONOMY
        return None

    def to_string(d):
        if d == Domain.EDUCATION: return "EDUCATION"
        if d == Domain.ECOLOGY: return "ECOLOGY"
        if d == Domain.ECONOMY: return "ECONOMY"

    def all():
        return {Domain.EDUCATION, Domain.ECOLOGY, Domain.ECONOMY}

    def choices():
        return {"EDUCATION", "ECOLOGY", "ECONOMY"}
