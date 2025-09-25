#!/usr/bin/env python3
"""
Ford Marketing Intelligence Data Visualizations
Generates charts and graphs from marketing data tables
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from pathlib import Path

# Set style for professional charts
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# Create output directory
output_dir = Path("visualizations")
output_dir.mkdir(exist_ok=True)

def create_marketing_roi_trend():
    """Marketing Investment & ROI Trend (2015-2024)"""
    years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
    marketing_spend = [2.3, 2.4, 2.5, 2.6, 2.5, 2.1, 2.2, 2.2, 2.5, 2.8]
    roi_ratio = [3.22, 1.92, 3.04, 1.42, 0.32, -0.62, 8.14, -1.00, 1.72, 2.11]
    marketing_pct = [1.54, 1.58, 1.59, 1.62, 1.60, 1.65, 1.61, 1.39, 1.42, 1.51]

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 10))

    # Marketing Spend
    ax1.plot(years, marketing_spend, marker='o', linewidth=2, markersize=6)
    ax1.set_title('Ford Marketing Spend (2015-2024)', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Marketing Spend ($B)')
    ax1.grid(True, alpha=0.3)

    # ROI Ratio
    ax2.plot(years, roi_ratio, marker='s', color='green', linewidth=2, markersize=6)
    ax2.axhline(y=0, color='red', linestyle='--', alpha=0.7)
    ax2.set_title('Marketing ROI Trend', fontsize=14, fontweight='bold')
    ax2.set_ylabel('ROI Ratio')
    ax2.grid(True, alpha=0.3)

    # Marketing as % of Revenue
    ax3.plot(years, marketing_pct, marker='^', color='purple', linewidth=2, markersize=6)
    ax3.set_title('Marketing Efficiency (% of Revenue)', fontsize=14, fontweight='bold')
    ax3.set_ylabel('Marketing % of Revenue')
    ax3.set_xlabel('Year')
    ax3.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_dir / 'marketing_roi_trend.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_segment_performance():
    """Vehicle Sales by Segment Performance"""
    segments = ['Trucks', 'SUVs', 'Cars', 'EVs']
    units_2023 = [903, 743, 234, 91]
    units_2024 = [976, 798, 189, 124]
    marketing_roi = [5.0, 2.7, 1.2, 2.0]
    loyalty_rates = [65.1, 48.2, 32.1, 41.5]

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))

    # Sales Volume Comparison
    x = np.arange(len(segments))
    width = 0.35
    ax1.bar(x - width/2, units_2023, width, label='2023', alpha=0.8)
    ax1.bar(x + width/2, units_2024, width, label='2024', alpha=0.8)
    ax1.set_title('Vehicle Sales by Segment (000s units)', fontweight='bold')
    ax1.set_ylabel('Units (thousands)')
    ax1.set_xticks(x)
    ax1.set_xticklabels(segments)
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Marketing ROI by Segment
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
    ax2.bar(segments, marketing_roi, color=colors, alpha=0.8)
    ax2.set_title('Marketing ROI by Segment', fontweight='bold')
    ax2.set_ylabel('ROI Ratio')
    ax2.grid(True, alpha=0.3)

    # Loyalty Rates
    ax3.bar(segments, loyalty_rates, color=colors, alpha=0.8)
    ax3.set_title('Brand Loyalty by Segment (%)', fontweight='bold')
    ax3.set_ylabel('Loyalty Rate (%)')
    ax3.grid(True, alpha=0.3)

    # Growth Rate Calculation
    growth_rates = [(units_2024[i] - units_2023[i]) / units_2023[i] * 100 for i in range(len(segments))]
    ax4.bar(segments, growth_rates, color=colors, alpha=0.8)
    ax4.set_title('Sales Growth Rate (2023-2024)', fontweight='bold')
    ax4.set_ylabel('Growth Rate (%)')
    ax4.axhline(y=0, color='black', linestyle='-', alpha=0.5)
    ax4.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_dir / 'segment_performance.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_competitive_analysis():
    """Competitive Marketing Analysis"""
    companies = ['Ford', 'GM', 'Stellantis', 'Toyota']
    marketing_spend = [2.8, 3.3, 1.9, 3.8]
    revenue_pct = [1.51, 1.90, 2.10, 1.45]
    brand_loyalty = [52.8, 49.1, 45.3, 61.2]
    acsi_scores = [79, 81, 75, 84]

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))

    # Marketing Spend Comparison
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
    ax1.bar(companies, marketing_spend, color=colors, alpha=0.8)
    ax1.set_title('Marketing Spend Comparison 2024', fontweight='bold')
    ax1.set_ylabel('Marketing Spend ($B)')
    ax1.grid(True, alpha=0.3)

    # Marketing Efficiency
    ax2.bar(companies, revenue_pct, color=colors, alpha=0.8)
    ax2.set_title('Marketing Efficiency (% of Revenue)', fontweight='bold')
    ax2.set_ylabel('Marketing % of Revenue')
    ax2.grid(True, alpha=0.3)

    # Brand Loyalty Comparison
    ax3.bar(companies, brand_loyalty, color=colors, alpha=0.8)
    ax3.set_title('Brand Loyalty Comparison (%)', fontweight='bold')
    ax3.set_ylabel('Loyalty Rate (%)')
    ax3.grid(True, alpha=0.3)

    # Customer Satisfaction (ACSI)
    ax4.bar(companies, acsi_scores, color=colors, alpha=0.8)
    ax4.set_title('Customer Satisfaction (ACSI Scores)', fontweight='bold')
    ax4.set_ylabel('ACSI Score')
    ax4.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_dir / 'competitive_analysis.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_campaign_performance():
    """Ready, Set, Ford Campaign Performance"""
    metrics = ['Brand\nAwareness', 'Consideration\nRate', 'Website\nTraffic', 'Social\nEngagement', 'Lead\nGeneration']
    pre_campaign = [68, 42, 4.3, 3.8, 124]
    post_launch = [74, 48, 5.8, 5.2, 168]
    targets = [75, 50, 6.0, 5.5, 180]

    x = np.arange(len(metrics))
    width = 0.25

    fig, ax = plt.subplots(figsize=(14, 8))

    bars1 = ax.bar(x - width, pre_campaign, width, label='Pre-Campaign', alpha=0.8, color='lightcoral')
    bars2 = ax.bar(x, post_launch, width, label='Post-Launch', alpha=0.8, color='skyblue')
    bars3 = ax.bar(x + width, targets, width, label='Target', alpha=0.8, color='lightgreen')

    ax.set_title('"Ready, Set, Ford" Campaign Performance', fontsize=16, fontweight='bold')
    ax.set_ylabel('Performance Metrics')
    ax.set_xticks(x)
    ax.set_xticklabels(metrics)
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Add value labels on bars
    for bars in [bars1, bars2, bars3]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                   f'{height}', ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.savefig(output_dir / 'campaign_performance.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_bi_impact_visualization():
    """Business Intelligence Impact on Marketing"""
    bi_applications = ['Customer Data\nPlatform', 'Predictive\nAnalytics', 'Real-time\nDashboards',
                       'Sentiment\nAnalysis', 'Connected Vehicle\nData']
    roi_improvements = [22, -18, 31, 2, 45]  # Note: -18 is cost reduction, different metric
    colors = ['green' if x > 0 else 'red' for x in roi_improvements]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # ROI Impact Bar Chart
    bars = ax1.bar(bi_applications, roi_improvements, color=colors, alpha=0.8)
    ax1.set_title('Business Intelligence ROI Impact', fontweight='bold', fontsize=14)
    ax1.set_ylabel('ROI Improvement (%)')
    ax1.axhline(y=0, color='black', linestyle='-', alpha=0.5)
    ax1.grid(True, alpha=0.3)
    plt.setp(ax1.get_xticklabels(), rotation=45, ha='right')

    # Add value labels
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + (1 if height > 0 else -3),
                f'{height}%', ha='center', va='bottom' if height > 0 else 'top', fontsize=10)

    # Timeline Implementation
    implementation_years = [2021, 2022, 2023, 2023, 2024]
    cumulative_impact = [31, 31+(-18), 31-18+22, 31-18+22+2, 31-18+22+2+45]

    ax2.plot(implementation_years, cumulative_impact, marker='o', linewidth=3, markersize=8, color='blue')
    ax2.fill_between(implementation_years, cumulative_impact, alpha=0.3, color='blue')
    ax2.set_title('Cumulative BI Impact Over Time', fontweight='bold', fontsize=14)
    ax2.set_xlabel('Year')
    ax2.set_ylabel('Cumulative ROI Improvement (%)')
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_dir / 'bi_impact.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_digital_transformation():
    """Digital Marketing Mix Evolution"""
    years = [2019, 2020, 2021, 2022, 2023, 2024, 2025]
    digital_mix = [40, 45, 50, 58, 62, 65, 68]  # Projected 2025
    traditional_mix = [60, 55, 50, 42, 38, 35, 32]

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.fill_between(years, 0, digital_mix, alpha=0.7, color='skyblue', label='Digital Marketing')
    ax.fill_between(years, digital_mix, 100, alpha=0.7, color='lightcoral', label='Traditional Marketing')

    ax.set_title('Ford Marketing Mix Evolution: Digital vs Traditional', fontsize=16, fontweight='bold')
    ax.set_xlabel('Year')
    ax.set_ylabel('Marketing Mix (%)')
    ax.legend(loc='center right')
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 100)

    # Add percentage labels
    for i, year in enumerate(years):
        ax.text(year, digital_mix[i]/2, f'{digital_mix[i]}%', ha='center', va='center', fontweight='bold')
        ax.text(year, digital_mix[i] + traditional_mix[i]/2, f'{traditional_mix[i]}%', ha='center', va='center', fontweight='bold')

    plt.tight_layout()
    plt.savefig(output_dir / 'digital_transformation.png', dpi=300, bbox_inches='tight')
    plt.close()

def main():
    """Generate all visualizations"""
    print("Generating Ford Marketing Intelligence Visualizations...")

    create_marketing_roi_trend()
    print("✓ Marketing ROI Trend chart created")

    create_segment_performance()
    print("✓ Segment Performance dashboard created")

    create_competitive_analysis()
    print("✓ Competitive Analysis charts created")

    create_campaign_performance()
    print("✓ Campaign Performance chart created")

    create_bi_impact_visualization()
    print("✓ Business Intelligence Impact charts created")

    create_digital_transformation()
    print("✓ Digital Transformation chart created")

    print(f"\nAll visualizations saved to: {output_dir}")
    print("Charts generated:")
    for chart in output_dir.glob("*.png"):
        print(f"  - {chart.name}")

if __name__ == "__main__":
    main()