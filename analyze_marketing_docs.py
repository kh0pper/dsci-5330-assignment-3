#!/usr/bin/env python3
"""
Marketing Intelligence Document Analyzer
Uses Llama AI to analyze marketing class notes and extract key concepts
"""

import os
import json
from openai import OpenAI
from pathlib import Path
import fitz  # PyMuPDF for PDF processing
from PIL import Image
import io
import base64
from typing import List, Dict, Any

# Initialize Llama API client
# API key should be set as environment variable: LLAMA_API_KEY
api_key = os.environ.get("LLAMA_API_KEY")
if not api_key:
    raise ValueError("LLAMA_API_KEY environment variable is not set. Please set it before running this script.")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.llama.com/compat/v1/",
)

def extract_pdf_content(pdf_path: str) -> Dict[str, Any]:
    """Extract text and images from PDF file"""
    doc = fitz.open(pdf_path)
    content = {
        'file': pdf_path,
        'pages': [],
        'total_pages': len(doc)
    }

    for page_num, page in enumerate(doc, 1):
        page_data = {
            'page_number': page_num,
            'text': page.get_text(),
            'images': []
        }

        # Extract images
        image_list = page.get_images(full=True)
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]

            # Convert to base64 for API
            image_base64 = base64.b64encode(image_bytes).decode()
            page_data['images'].append({
                'index': img_index,
                'base64': image_base64,
                'ext': base_image["ext"]
            })

        content['pages'].append(page_data)

    doc.close()
    return content

def analyze_marketing_content(content: Dict) -> str:
    """Use Llama AI to analyze marketing content"""

    # Prepare prompt
    prompt = f"""
    Analyze this marketing class material and extract the following:

    1. KEY MARKETING CONCEPTS AND FRAMEWORKS:
       - Marketing intelligence systems
       - Business intelligence in marketing
       - Market research methodologies
       - Consumer behavior analysis
       - Marketing mix (4Ps, 7Ps)
       - Segmentation, Targeting, Positioning (STP)
       - Brand management concepts

    2. MARKETING METRICS AND ANALYSIS:
       - ROI measurement
       - Customer lifetime value
       - Market share analysis
       - Brand equity measurement

    3. STRATEGIC MARKETING APPROACHES:
       - Digital marketing strategies
       - Traditional marketing methods
       - Integrated marketing communications
       - Customer relationship management

    4. SPECIFIC VOCABULARY AND TERMINOLOGY:
       - Technical marketing terms
       - Industry-specific language

    From file: {content['file']}
    Text content from first 3 pages:
    {' '.join([page['text'][:1000] for page in content['pages'][:3]])}

    Provide a structured summary with specific terms and concepts that should be integrated into a marketing analysis memorandum.
    """

    try:
        response = client.chat.completions.create(
            model="Llama-4-Maverick-17B-128E-Instruct-FP8",
            messages=[
                {"role": "system", "content": "You are an expert marketing professor analyzing class materials to extract key concepts and frameworks for a student's marketing assignment on Ford Motor Company."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=2000
        )

        return response.choices[0].message.content
    except Exception as e:
        return f"Error analyzing content: {str(e)}"

def main():
    """Main function to process all marketing documents"""

    class_notes_dir = Path("/home/kh0pp/DSCI-5330/assignment-03-take-2/class-notes")

    # PDF files to analyze
    pdf_files = [
        "Session 6 document marketing intelligence.pdf",
        "Session 6 document marketing reading.pdf"
    ]

    results = []

    print("Analyzing marketing class notes...")

    for pdf_file in pdf_files:
        pdf_path = class_notes_dir / pdf_file
        if pdf_path.exists():
            print(f"\nProcessing: {pdf_file}")

            # Extract content
            content = extract_pdf_content(str(pdf_path))

            # Analyze with Llama AI
            analysis = analyze_marketing_content(content)

            results.append({
                'file': pdf_file,
                'analysis': analysis
            })

            print(f"Analysis complete for: {pdf_file}")

    # Save results
    output_path = Path("/home/kh0pp/DSCI-5330/assignment-03-take-2/marketing_concepts_analysis.json")
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"\nAnalysis saved to: {output_path}")

    # Also create a summary document
    summary_path = Path("/home/kh0pp/DSCI-5330/assignment-03-take-2/marketing_concepts_summary.md")
    with open(summary_path, 'w') as f:
        f.write("# Marketing Concepts and Frameworks from Class Notes\n\n")
        for result in results:
            f.write(f"## {result['file']}\n\n")
            f.write(result['analysis'])
            f.write("\n\n---\n\n")

    print(f"Summary saved to: {summary_path}")

    return results

if __name__ == "__main__":
    main()