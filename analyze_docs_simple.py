#!/usr/bin/env python3
"""
Simple Marketing Document Analyzer using Llama AI
"""

import os
import subprocess
from pathlib import Path
from openai import OpenAI

# Initialize Llama API client
# API key should be set as environment variable: LLAMA_API_KEY
api_key = os.environ.get("LLAMA_API_KEY")
if not api_key:
    raise ValueError("LLAMA_API_KEY environment variable is not set. Please set it before running this script.")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.llama.com/compat/v1/",
)

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF using pdftotext"""
    try:
        result = subprocess.run(
            ['pdftotext', pdf_path, '-'],
            capture_output=True,
            text=True
        )
        return result.stdout
    except:
        return ""

def analyze_with_llama(text, filename):
    """Analyze text content with Llama AI"""
    prompt = f"""
    Analyze this marketing class material from {filename} and extract:

    1. KEY MARKETING CONCEPTS that apply to Ford Motor Company:
       - Marketing intelligence and business intelligence systems
       - Market research and consumer analysis
       - Strategic marketing frameworks
       - Brand management and positioning

    2. MARKETING METRICS AND KPIs relevant to automotive industry:
       - Performance measurement
       - Customer metrics
       - Market analysis tools

    3. MARKETING APPROACHES Ford could use:
       - Digital vs traditional marketing
       - Customer engagement strategies
       - Competitive positioning

    4. SPECIFIC MARKETING VOCABULARY to use in the memorandum

    Text excerpt:
    {text[:4000]}

    Provide specific concepts and terms that should be integrated into Ford's marketing analysis.
    Focus on practical applications for Ford's "Ready, Set, Ford" campaign.
    """

    try:
        response = client.chat.completions.create(
            model="Llama-4-Maverick-17B-128E-Instruct-FP8",
            messages=[
                {"role": "system", "content": "You are a marketing expert analyzing class materials to identify concepts applicable to Ford Motor Company's marketing strategy."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=1500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    class_notes_dir = Path("/home/kh0pp/DSCI-5330/assignment-03-take-2/class-notes")

    pdf_files = [
        "Session 6 document marketing intelligence.pdf",
        "Session 6 document marketing reading.pdf"
    ]

    all_analyses = []

    print("Analyzing marketing documents with Llama AI...")

    for pdf_file in pdf_files:
        pdf_path = class_notes_dir / pdf_file
        if pdf_path.exists():
            print(f"\nProcessing: {pdf_file}")

            # Extract text
            text = extract_text_from_pdf(str(pdf_path))

            if text:
                # Analyze with Llama
                analysis = analyze_with_llama(text, pdf_file)
                all_analyses.append(f"## Analysis of {pdf_file}\n\n{analysis}")
                print(f"✓ Completed analysis of {pdf_file}")
            else:
                print(f"⚠ Could not extract text from {pdf_file}")

    # Save combined analysis
    output_path = Path("/home/kh0pp/DSCI-5330/assignment-03-take-2/marketing_concepts.md")
    with open(output_path, 'w') as f:
        f.write("# Marketing Intelligence Concepts for Ford Analysis\n\n")
        f.write("\n\n---\n\n".join(all_analyses))

    print(f"\n✓ Analysis saved to: {output_path}")

    return all_analyses

if __name__ == "__main__":
    main()