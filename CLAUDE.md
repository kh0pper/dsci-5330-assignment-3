# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

Ford Motor Company marketing intelligence analysis for DSCI-5330 Assignment 03. Analyzes Ford's marketing transformation (2015-2025) focusing on the "Ready, Set, Ford" campaign, integrating academic marketing frameworks with business intelligence systems.

## Key Commands

### Visualization Generation
```bash
# Generate all marketing data visualizations (requires matplotlib, pandas, seaborn, numpy)
python3 generate_visualizations.py

# Install dependencies if needed
python3 -m pip install --user --break-system-packages matplotlib pandas seaborn numpy
```

### Document Analysis Pipeline
```bash
# Analyze marketing concepts from class PDFs using Llama AI
python3 analyze_docs_simple.py

# Alternative with image extraction (requires PyMuPDF)
python3 analyze_marketing_docs.py

# Manual PDF text extraction
pdftotext "path/to/file.pdf" -
```

## Technical Architecture

### Python Analysis Tools

**`generate_visualizations.py`** - Creates 6 data visualizations:
- Marketing ROI trends with 3-panel analysis
- Vehicle segment performance dashboard (4 metrics)
- Competitive analysis comparison (Ford vs GM, Stellantis, Toyota)
- Campaign performance metrics with targets
- Business intelligence ROI impact visualization
- Digital marketing transformation timeline

**`analyze_docs_simple.py`** - Llama AI document analyzer:
- Uses OpenAI client library with Llama endpoint
- Model: Llama-4-Maverick-17B-128E-Instruct-FP8
- Extracts marketing concepts from class PDFs
- Outputs to `marketing_concepts.md`

### Data Flow Architecture
```
Source Documents → AI Analysis → Data Tables → Visualizations → Memorandum
       ↓               ↓              ↓              ↓              ↓
   (PDFs/10Ks)   (Llama API)    (10 tables)   (6 charts)    (15+ pages)
```

## Repository Structure

### Source Documents Organization

```
sources/
├── SEC/                     # SEC filings
│   └── Ford_2024_Form_10-K.pdf
├── shareholder/             # Annual reports and proxy statements
│   ├── Ford_2024_Annual_Report.pdf
│   └── Ford_2025_DEF14A.html
└── external/                # Marketing campaign and industry analysis
    ├── Ford launches biggest global marketing campaign since 2012.pdf
    ├── Ford marketing chief talks economy, AI amid launch of new strategy.pdf
    ├── Introducing Ready Set Ford.pdf
    ├── JD_Power_2024_Brand_Loyalty.pdf
    ├── McKinsey_Collectible_Cars.pdf
    └── McKinsey_Ford_Transformation.pdf
```

### Historical Financial Data

```
10k/                         # Historical 10-K filings (2011-2015)
Annual Report/               # Historical annual reports (2011-2024)
```

### Academic Materials

```
class-notes/                 # Marketing intelligence course materials
├── 8170-PPT-ENG MKTNG.pptx
├── 8196-PPT-ENG MKTNG Intelligence.pptx
└── Session 6 documents (PDF)

project-instructions/        # Assignment specifications
└── Assignment 3 Marketing Instruction.docx
```

## Key Analysis Focus Areas

### Marketing Campaign Analysis
- **Campaign Name**: "Ready, Set, Ford" (launched September 2025)
- **Scope**: Largest global marketing push since 2012
- **Key Documents**: External sources folder contains primary campaign documentation

### Strategic Context from SEC Filings
- Form 10-K (2024): Financial performance and risk factors
- Annual Report (2024): Business strategy and market positioning
- DEF14A Proxy (2025): Executive compensation and governance

### Industry Intelligence Sources
- JD Power 2024 Brand Loyalty study
- McKinsey reports on Ford transformation and collectible cars market
- Historical trend analysis from 10+ years of annual reports

## Document Processing Notes

### PDF Files
- Most source documents are PDFs requiring text extraction for analysis
- Financial documents contain tables and structured data
- Marketing materials include visual elements and branding analysis

### Media Articles
- External articles captured from Google News RSS (September 19, 2025)
- Manual browser downloads due to automated-access restrictions
- Metadata should be preserved when analyzing publication context

## Analysis Workflows

### Financial Trend Analysis
Use historical 10-K and annual reports to:
- Track revenue and profitability trends (2011-2024)
- Identify market share changes
- Analyze capital allocation and investment priorities

### Marketing Intelligence Framework
Leverage class notes materials for:
- Competitive positioning analysis
- Brand equity assessment
- Customer segmentation insights

### Campaign Effectiveness Evaluation
Cross-reference campaign materials with:
- Brand loyalty metrics (JD Power)
- Transformation progress (McKinsey)
- Financial performance indicators

## Core Deliverables and Dependencies

### Primary Analysis Documents
- `Ford_Marketing_Intelligence_Memorandum.md` - Final 15+ page memorandum
- `MEMORANDUM_OUTLINE.md` - Structured outline (source for final memo)
- `marketing_data_tables.md` - 10 data tables (feeds visualizations)
- `PROJECT_EXECUTION_PLAN.md` - Methodology and framework

### Data Processing Chain
```
marketing_data_tables.md → generate_visualizations.py → visualizations/*.png
                        ↘                             ↗
                          Ford_Marketing_Intelligence_Memorandum.md
```

### Marketing Intelligence Frameworks Applied
- **STP Analysis**: Ford's three-segment strategy (Blue/Model e/Pro)
- **Consumer Decision-Making**: Cognitive vs emotional appeals in "Ready, Set, Ford"
- **7Ps Framework**: Product→Lifestyle, Price→Value, Place→Omnichannel
- **BI Integration**: CDP→22% conversion lift, Predictive→-18% inventory costs
- **Co-creation**: FordPass 3.5M users, 68% engagement rate

## Data Extraction Considerations

### Financial Data Processing
- Extract marketing spend trends from 10-K reports (2015-2024)
- Correlate marketing investment with revenue/profit performance
- Calculate ROI metrics and efficiency ratios
- Track segment performance (trucks, SUVs, cars, EVs)

### Marketing Campaign Analysis
- Quantify "Ready, Set, Ford" campaign impact (Q3 2025)
- Compare Ford's approach vs GM/Stellantis/Toyota
- Measure brand loyalty metrics and customer satisfaction scores
- Analyze digital vs traditional marketing mix evolution

### Business Intelligence Applications
- Customer Data Platform implementation and ROI
- Predictive analytics for demand forecasting
- Real-time dashboard optimization results
- Connected vehicle data utilization for marketing

## Key Performance Metrics

### Marketing Transformation Results (2019-2024)
- ROI: 0.32 → 2.11 (560% improvement)
- Efficiency: 1.65% → 1.51% of revenue
- Digital Mix: 40% → 65%
- Truck Loyalty: 65.1% (vs 52.7% industry)

### Business Intelligence ROI Impact
- Customer Data Platform: +22% conversion
- Predictive Analytics: -18% inventory costs
- Real-time Dashboards: +31% ROI optimization
- Connected Vehicle Data: +45% targeting success
- Total Cumulative Impact: +82% improvement

### Competitive Positioning (2024)
| Metric | Ford | GM | Stellantis | Toyota |
|--------|------|-----|------------|--------|
| Marketing Spend | $2.8B | $3.3B | $1.9B | $3.8B |
| % of Revenue | 1.51% | 1.90% | 2.10% | 1.45% |
| Brand Loyalty | 52.8% | 49.1% | 45.3% | 61.2% |