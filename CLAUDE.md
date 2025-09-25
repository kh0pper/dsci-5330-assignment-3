# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a Ford Motor Company marketing intelligence analysis repository for DSCI-5330 Assignment 03. The project analyzes Ford's marketing transformation (2015-2025) with focus on the "Ready, Set, Ford" campaign launched in September 2025, integrating marketing intelligence frameworks with business intelligence systems analysis.

## Key Commands and Tools

### Document Analysis Pipeline
```bash
# Extract and analyze marketing concepts from class PDFs
python3 analyze_docs_simple.py

# Alternative comprehensive analysis (requires PyMuPDF)
python3 analyze_marketing_docs.py

# Text extraction from PDFs (if needed manually)
pdftotext "path/to/file.pdf" -
```

### Llama AI Integration
The analysis tools use Llama AI for multimodal document analysis:
- API endpoint: https://api.llama.com/compat/v1/
- Model: Llama-4-Maverick-17B-128E-Instruct-FP8
- Purpose: Extract marketing concepts and frameworks from visual/text content

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

## Project Architecture

### Analysis Workflow
The repository follows a systematic approach:
1. **Document Collection**: Historical financial data (10k/, Annual Report/) + current marketing materials (sources/)
2. **Concept Extraction**: AI-powered analysis of class materials to identify marketing frameworks
3. **Data Synthesis**: Integration of financial metrics with marketing intelligence concepts
4. **Report Generation**: Professional memorandum with data tables and strategic recommendations

### Key Deliverables Structure
- `PROJECT_EXECUTION_PLAN.md`: Strategic framework and methodology
- `marketing_concepts.md`: Extracted marketing intelligence concepts from class materials
- `marketing_data_tables.md`: Comprehensive financial and performance metrics
- `MEMORANDUM_OUTLINE.md`: Professional analysis integrating all elements
- `works_cited.md`: Complete bibliography with 50+ academic and industry sources

### Marketing Intelligence Framework Integration
The analysis applies academic concepts throughout:
- **STP Framework**: Segmentation, Targeting, Positioning analysis
- **Consumer Decision-Making Process**: Pre-purchase, purchase, post-purchase evaluation
- **Marketing Mix Evolution**: 4Ps to 7Ps application
- **Business Intelligence Systems**: Data-driven marketing optimization
- **Co-creation and Conscience Marketing**: Modern engagement strategies

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

## Critical Success Factors

### Data Integration Approach
The analysis demonstrates Ford's marketing transformation through:
- **Quantitative Rigor**: 10 comprehensive data tables with historical trends (2015-2024)
- **Academic Integration**: Marketing intelligence concepts woven throughout analysis
- **Strategic Insight**: Linking marketing investments to financial performance
- **Forward-Looking**: BI-driven recommendations for competitive advantage

### Key Metrics Tracked
- Marketing ROI improvement from 0.32 (2019) to 2.11 (2024)
- Truck loyalty leadership at 65.1% vs industry average 52.7%
- Marketing efficiency optimization from 1.65% to 1.51% of revenue
- "Ready, Set, Ford" campaign driving +35% digital engagement

### Analytical Rigor Standards
- All financial data sourced from SEC filings and verified reports
- Marketing claims supported by industry research (J.D. Power, McKinsey)
- Competitive analysis includes GM, Stellantis, Toyota benchmarking
- Business intelligence impact quantified with specific ROI measurements