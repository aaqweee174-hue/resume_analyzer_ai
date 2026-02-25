import sys
import os

# Fix path issue
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from ats_score import calculate_ats
from suggestions import get_suggestions

def analyze_resume(resume_text, job_desc):
    ats = calculate_ats(resume_text, job_desc)
    suggestions = get_suggestions(resume_text, job_desc)

    return ats, suggestions