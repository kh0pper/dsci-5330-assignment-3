#!/usr/bin/env python3
"""
Ford Marketing Intelligence Data Visualizations (Version 2.0)
Enhanced with SWOT Analysis, Porter's Five Forces, and Advanced Metrics
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from pathlib import Path
import matplotlib.patches as patches

# Set style for professional charts
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# Create output directory
output_dir = Path("visualizations")
output_dir.mkdir(exist_ok=True)

def create_marketing_roi_trend():
    """Enhanced Marketing Investment & ROI Trend with ROAS (2015-2024)"""
    years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
    marketing_spend = [2.3, 2.4, 2.5, 2.6, 2.5, 2.1, 2.2, 2.2, 2.5, 2.8]
    roi_ratio = [3.22, 1.92, 3.04, 1.42, 0.32, -0.62, 8.14, -1.00, 1.72, 2.11]
    roas = [4.22, 2.92, 4.04, 2.42, 1.32, 0.38, 9.14, 0.00, 2.72, 3.11]
    marketing_pct = [1.54, 1.58, 1.59, 1.62, 1.60, 1.65, 1.61, 1.39, 1.42, 1.51]

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))

    # Marketing Spend
    ax1.plot(years, marketing_spend, marker='o', linewidth=3, markersize=8, color='steelblue')
    ax1.set_title('Ford Marketing Investment (2015-2024)', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Marketing Spend ($B)')
    ax1.grid(True, alpha=0.3)
    ax1.fill_between(years, marketing_spend, alpha=0.3, color='steelblue')

    # ROI vs ROAS Comparison
    ax2.plot(years, roi_ratio, marker='s', color='green', linewidth=3, markersize=8, label='ROI')
    ax2.plot(years, roas, marker='^', color='orange', linewidth=3, markersize=8, label='ROAS')
    ax2.axhline(y=0, color='red', linestyle='--', alpha=0.7)
    ax2.set_title('Marketing ROI vs ROAS Comparison', fontsize=14, fontweight='bold')
    ax2.set_ylabel('Return Ratio')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    # Marketing Efficiency (% of Revenue)
    ax3.plot(years, marketing_pct, marker='^', color='purple', linewidth=3, markersize=8)
    ax3.axhline(y=1.75, color='red', linestyle='--', alpha=0.7, label='Industry Avg')
    ax3.set_title('Marketing Efficiency vs Industry', fontsize=14, fontweight='bold')
    ax3.set_ylabel('Marketing % of Revenue')
    ax3.set_xlabel('Year')
    ax3.legend()
    ax3.grid(True, alpha=0.3)

    # Performance Phases
    phase_colors = ['lightcoral', 'gold', 'lightgreen']
    phases = ['Traditional\n(2015-2018)', 'Transformation\n(2019-2021)', 'Data-Driven\n(2022-2024)']
    phase_roas = [3.15, 3.61, 2.92]  # Average ROAS per phase

    ax4.bar(phases, phase_roas, color=phase_colors, alpha=0.8, edgecolor='black')
    ax4.set_title('Average ROAS by Strategic Phase', fontsize=14, fontweight='bold')
    ax4.set_ylabel('Average ROAS')
    ax4.grid(True, alpha=0.3)

    for i, v in enumerate(phase_roas):
        ax4.text(i, v + 0.1, f'${v:.2f}', ha='center', va='bottom', fontweight='bold')

    plt.tight_layout()
    plt.savefig(output_dir / 'enhanced_marketing_roi_trend.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_enhanced_segment_performance():
    """Enhanced Vehicle Sales by Segment with CPA and CLV"""
    segments = ['Trucks', 'SUVs', 'Cars', 'EVs', 'Commercial']
    units_2024 = [976, 798, 189, 124, 245]
    roas = [6.50, 3.70, 2.20, 3.00, 5.80]
    cpa = [180, 285, 485, 350, 195]
    clv = [45200, 32800, 22500, 38900, 52100]
    loyalty_rates = [65.1, 48.2, 32.1, 41.5, 71.2]

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))

    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57']

    # Sales Volume with Bubble Size by CLV
    bubble_sizes = [(clv_val / 1000) for clv_val in clv]  # Scale for bubble chart
    ax1.scatter(segments, units_2024, s=bubble_sizes, c=colors, alpha=0.7, edgecolors='black', linewidth=2)
    ax1.set_title('2024 Sales Volume (Bubble Size = CLV)', fontweight='bold', fontsize=14)
    ax1.set_ylabel('Units Sold (thousands)')
    ax1.grid(True, alpha=0.3)

    # ROAS Performance
    bars2 = ax2.bar(segments, roas, color=colors, alpha=0.8, edgecolor='black')
    ax2.set_title('Return on Ad Spend (ROAS) by Segment', fontweight='bold', fontsize=14)
    ax2.set_ylabel('ROAS ($)')
    ax2.axhline(y=4.10, color='red', linestyle='--', alpha=0.7, label='Industry Avg')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    for bar in bars2:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                f'${height:.2f}', ha='center', va='bottom', fontweight='bold')

    # Customer Acquisition Cost (CPA)
    bars3 = ax3.bar(segments, cpa, color=colors, alpha=0.8, edgecolor='black')
    ax3.set_title('Customer Acquisition Cost (CPA) by Segment', fontweight='bold', fontsize=14)
    ax3.set_ylabel('CPA ($)')
    ax3.axhline(y=315, color='red', linestyle='--', alpha=0.7, label='Industry Avg')
    ax3.legend()
    ax3.grid(True, alpha=0.3)

    for bar in bars3:
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height + 10,
                f'${height}', ha='center', va='bottom', fontweight='bold')

    # Customer Lifetime Value vs Loyalty
    ax4.scatter(loyalty_rates, clv, s=200, c=colors, alpha=0.7, edgecolors='black', linewidth=2)
    ax4.set_title('Customer Lifetime Value vs Brand Loyalty', fontweight='bold', fontsize=14)
    ax4.set_xlabel('Brand Loyalty (%)')
    ax4.set_ylabel('Customer Lifetime Value ($)')
    ax4.grid(True, alpha=0.3)

    # Add segment labels
    for i, segment in enumerate(segments):
        ax4.annotate(segment, (loyalty_rates[i], clv[i]), xytext=(5, 5),
                    textcoords='offset points', fontweight='bold')

    plt.tight_layout()
    plt.savefig(output_dir / 'enhanced_segment_performance.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_swot_analysis_visualization():
    """SWOT Analysis Strategic Matrix"""
    fig, ax = plt.subplots(figsize=(14, 10))

    # Create quadrants
    ax.axhline(y=5, color='black', linewidth=2)
    ax.axvline(x=5, color='black', linewidth=2)

    # Quadrant colors
    ax.add_patch(patches.Rectangle((0, 5), 5, 5, facecolor='lightgreen', alpha=0.3))  # Strengths
    ax.add_patch(patches.Rectangle((5, 5), 5, 5, facecolor='lightcoral', alpha=0.3))  # Weaknesses
    ax.add_patch(patches.Rectangle((0, 0), 5, 5, facecolor='lightblue', alpha=0.3))   # Opportunities
    ax.add_patch(patches.Rectangle((5, 0), 5, 5, facecolor='lightyellow', alpha=0.3)) # Threats

    # SWOT data points (Impact vs Strategic Priority)
    strengths = {
        'Heritage Brand (9.2)': (1.5, 8.5),
        'Truck Dominance (9.5)': (2.5, 9.0),
        'Marketing Efficiency (8.8)': (3.5, 7.5),
        'Market Leadership (8.5)': (4.0, 8.0),
        'Digital Trans. (7.2)': (3.0, 6.5)
    }

    weaknesses = {
        'Brand Loyalty (4.8)': (7.5, 8.0),
        'EV Market Share (3.2)': (8.5, 9.0),
        'Customer Sat. (5.5)': (6.5, 7.0),
        'Premium Position (4.1)': (7.0, 6.5)
    }

    opportunities = {
        'EV Growth (9.1)': (2.0, 4.0),
        'AI Personal. (8.7)': (3.5, 3.5),
        'Conscience Mkt (8.2)': (4.0, 2.5),
        'Co-Creation (7.8)': (1.5, 3.0)
    }

    threats = {
        'Competition (7.8)': (8.0, 4.0),
        'Econ. Uncertain (6.5)': (6.5, 3.0),
        'Consumer Shift (6.8)': (7.5, 2.5),
        'Regulatory (7.2)': (9.0, 3.5)
    }

    # Plot points
    for category, points in [
        (strengths, 'green'), (weaknesses, 'red'),
        (opportunities, 'blue'), (threats, 'orange')
    ]:
        for label, (x, y) in category.items():
            ax.scatter(x, y, s=200, c=points, alpha=0.8, edgecolors='black', linewidth=2)
            ax.annotate(label, (x, y), xytext=(5, 5), textcoords='offset points',
                       fontsize=9, fontweight='bold', ha='left')

    # Labels and title
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_xlabel('Strategic Priority →', fontsize=12, fontweight='bold')
    ax.set_ylabel('Impact Score →', fontsize=12, fontweight='bold')
    ax.set_title('Ford Motor Company SWOT Analysis Matrix', fontsize=16, fontweight='bold', pad=20)

    # Quadrant labels
    ax.text(2.5, 9.5, 'STRENGTHS', ha='center', va='center', fontsize=14, fontweight='bold')
    ax.text(7.5, 9.5, 'WEAKNESSES', ha='center', va='center', fontsize=14, fontweight='bold')
    ax.text(2.5, 0.5, 'OPPORTUNITIES', ha='center', va='center', fontsize=14, fontweight='bold')
    ax.text(7.5, 0.5, 'THREATS', ha='center', va='center', fontsize=14, fontweight='bold')

    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_dir / 'swot_analysis_matrix.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_porters_five_forces():
    """Porter's Five Forces Analysis Visualization"""
    fig, ax = plt.subplots(figsize=(12, 10))

    # Force intensity data
    forces = {
        'Competitive\nRivalry': {'intensity': 8.5, 'position': (0.5, 0.5), 'color': '#FF6B6B'},
        'Supplier\nPower': {'intensity': 6.2, 'position': (0.2, 0.8), 'color': '#4ECDC4'},
        'Buyer\nPower': {'intensity': 7.8, 'position': (0.8, 0.8), 'color': '#45B7D1'},
        'Threat of\nSubstitutes': {'intensity': 6.8, 'position': (0.2, 0.2), 'color': '#96CEB4'},
        'Barriers to\nEntry': {'intensity': 7.5, 'position': (0.8, 0.2), 'color': '#FECA57'}
    }

    # Draw force circles
    for force, data in forces.items():
        x, y = data['position']
        intensity = data['intensity']
        color = data['color']

        # Circle size based on intensity
        circle_size = intensity * 50
        circle = plt.Circle((x, y), intensity/50, color=color, alpha=0.6,
                          edgecolor='black', linewidth=2)
        ax.add_patch(circle)

        # Add force labels
        ax.text(x, y-0.08, force, ha='center', va='center', fontweight='bold', fontsize=10)
        ax.text(x, y+0.05, f'{intensity}/10', ha='center', va='center', fontweight='bold', fontsize=12)

    # Add Ford position in center
    ax.add_patch(plt.Circle((0.5, 0.5), 0.08, color='gold', alpha=0.8,
                           edgecolor='black', linewidth=3))
    ax.text(0.5, 0.5, 'FORD\nMOTOR\nCO.', ha='center', va='center',
           fontweight='bold', fontsize=10)

    # Connect forces with lines
    connections = [
        ((0.2, 0.8), (0.5, 0.5)),  # Supplier to Ford
        ((0.8, 0.8), (0.5, 0.5)),  # Buyer to Ford
        ((0.2, 0.2), (0.5, 0.5)),  # Substitutes to Ford
        ((0.8, 0.2), (0.5, 0.5))   # Barriers to Ford
    ]

    for start, end in connections:
        ax.plot([start[0], end[0]], [start[1], end[1]],
                'k--', alpha=0.4, linewidth=1)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Porter\'s Five Forces Analysis - Ford Motor Company',
                fontsize=16, fontweight='bold', pad=20)

    # Add intensity legend
    legend_text = "Force Intensity Scale:\n1-3: Low\n4-6: Moderate\n7-10: High"
    ax.text(0.02, 0.02, legend_text, fontsize=10, bbox=dict(boxstyle="round,pad=0.3",
            facecolor="lightgray", alpha=0.8))

    plt.tight_layout()
    plt.savefig(output_dir / 'porters_five_forces.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_customer_journey_funnel():
    """Customer Journey Marketing Funnel with ROAS and CPA"""
    stages = ['Awareness', 'Interest', 'Consideration', 'Intent', 'Purchase', 'Loyalty']
    traffic = [2450, 294, 82, 29, 18, 15]  # in thousands
    conversion_rates = [12, 28, 35, 62, 85, 45]
    roas = [2.80, 3.90, 4.60, 5.80, 6.20, 8.50]
    cpa = [485, 320, 285, 195, 165, 125]

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))

    # Customer Journey Funnel
    colors = plt.cm.RdYlGn(np.linspace(0.3, 0.9, len(stages)))
    bars1 = ax1.barh(stages, traffic, color=colors, alpha=0.8, edgecolor='black')
    ax1.set_title('Customer Journey Traffic Funnel', fontweight='bold', fontsize=14)
    ax1.set_xlabel('Traffic (thousands)')
    ax1.grid(True, alpha=0.3)

    for i, (bar, val) in enumerate(zip(bars1, traffic)):
        ax1.text(val + 50, bar.get_y() + bar.get_height()/2, f'{val}K',
                va='center', fontweight='bold')

    # Conversion Rates by Stage
    ax2.plot(stages, conversion_rates, marker='o', linewidth=3, markersize=10,
             color='steelblue')
    ax2.fill_between(stages, conversion_rates, alpha=0.3, color='steelblue')
    ax2.set_title('Conversion Rate by Journey Stage', fontweight='bold', fontsize=14)
    ax2.set_ylabel('Conversion Rate (%)')
    ax2.grid(True, alpha=0.3)
    plt.setp(ax2.get_xticklabels(), rotation=45, ha='right')

    # ROAS by Stage
    bars3 = ax3.bar(stages, roas, color=colors, alpha=0.8, edgecolor='black')
    ax3.set_title('Return on Ad Spend by Journey Stage', fontweight='bold', fontsize=14)
    ax3.set_ylabel('ROAS ($)')
    ax3.grid(True, alpha=0.3)
    plt.setp(ax3.get_xticklabels(), rotation=45, ha='right')

    for bar in bars3:
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                f'${height:.2f}', ha='center', va='bottom', fontweight='bold')

    # CPA by Stage (inverted because lower is better)
    bars4 = ax4.bar(stages, cpa, color='lightcoral', alpha=0.8, edgecolor='black')
    ax4.set_title('Customer Acquisition Cost by Journey Stage', fontweight='bold', fontsize=14)
    ax4.set_ylabel('CPA ($)')
    ax4.grid(True, alpha=0.3)
    plt.setp(ax4.get_xticklabels(), rotation=45, ha='right')

    for bar in bars4:
        height = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width()/2., height + 10,
                f'${int(height)}', ha='center', va='bottom', fontweight='bold')

    plt.tight_layout()
    plt.savefig(output_dir / 'customer_journey_funnel.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_competitive_positioning_radar():
    """Enhanced Competitive Analysis Radar Chart"""
    categories = ['Marketing\nEfficiency', 'Brand\nLoyalty', 'Digital\nMix',
                  'Customer\nSatisfaction', 'ROAS', 'Innovation\nPerception']

    # Normalized scores (0-10 scale)
    ford = [9.5, 6.0, 7.5, 6.8, 7.2, 7.0]
    gm = [8.2, 5.5, 8.0, 7.2, 6.5, 6.5]
    toyota = [9.8, 8.5, 6.8, 9.2, 8.3, 7.8]
    tesla = [8.8, 9.8, 10.0, 8.9, 9.5, 9.8]

    # Calculate angles for radar chart
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]  # Complete the circle

    # Add first value to end for complete polygon
    ford += ford[:1]
    gm += gm[:1]
    toyota += toyota[:1]
    tesla += tesla[:1]

    fig, ax = plt.subplots(figsize=(12, 12), subplot_kw=dict(projection='polar'))

    # Plot each company
    ax.plot(angles, ford, 'o-', linewidth=3, label='Ford', color='#FF6B6B')
    ax.fill(angles, ford, alpha=0.25, color='#FF6B6B')

    ax.plot(angles, gm, 'o-', linewidth=3, label='GM', color='#4ECDC4')
    ax.fill(angles, gm, alpha=0.25, color='#4ECDC4')

    ax.plot(angles, toyota, 'o-', linewidth=3, label='Toyota', color='#45B7D1')
    ax.fill(angles, toyota, alpha=0.25, color='#45B7D1')

    ax.plot(angles, tesla, 'o-', linewidth=3, label='Tesla', color='#96CEB4')
    ax.fill(angles, tesla, alpha=0.25, color='#96CEB4')

    # Customize chart
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=11, fontweight='bold')
    ax.set_ylim(0, 10)
    ax.set_yticks(range(0, 11, 2))
    ax.set_yticklabels(range(0, 11, 2), fontsize=10)
    ax.grid(True, alpha=0.3)

    ax.set_title('Competitive Positioning Analysis\n(Marketing Performance Metrics)',
                fontsize=16, fontweight='bold', pad=30)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0), fontsize=12)

    plt.tight_layout()
    plt.savefig(output_dir / 'competitive_positioning_radar.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_attribution_analysis():
    """Marketing Attribution Multi-Touch Analysis"""
    channels = ['Digital\nDisplay', 'Social\nMedia', 'Search\nEngine',
               'Television', 'Radio', 'Dealer\nVisit']

    # Attribution percentages
    first_touch = [18, 25, 15, 22, 8, 12]
    last_touch = [8, 12, 28, 15, 5, 32]
    multi_touch = [15, 22, 25, 18, 6, 14]
    roas_by_channel = [3.20, 4.10, 5.80, 2.90, 2.40, 6.50]

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))

    x = np.arange(len(channels))
    width = 0.25

    # Attribution Comparison
    bars1 = ax1.bar(x - width, first_touch, width, label='First Touch', alpha=0.8, color='lightcoral')
    bars2 = ax1.bar(x, multi_touch, width, label='Multi-Touch', alpha=0.8, color='lightblue')
    bars3 = ax1.bar(x + width, last_touch, width, label='Last Touch', alpha=0.8, color='lightgreen')

    ax1.set_title('Marketing Attribution Analysis by Channel', fontweight='bold', fontsize=14)
    ax1.set_ylabel('Attribution (%)')
    ax1.set_xticks(x)
    ax1.set_xticklabels(channels)
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    plt.setp(ax1.get_xticklabels(), rotation=45, ha='right')

    # ROAS by Channel
    bars4 = ax2.bar(channels, roas_by_channel, color=plt.cm.RdYlGn(np.linspace(0.3, 0.9, len(channels))),
                    alpha=0.8, edgecolor='black')
    ax2.set_title('ROAS Performance by Marketing Channel', fontweight='bold', fontsize=14)
    ax2.set_ylabel('ROAS ($)')
    ax2.axhline(y=4.10, color='red', linestyle='--', alpha=0.7, label='Avg ROAS')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    plt.setp(ax2.get_xticklabels(), rotation=45, ha='right')

    for bar in bars4:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                f'${height:.2f}', ha='center', va='bottom', fontweight='bold')

    # Attribution vs ROAS Scatter
    ax3.scatter(multi_touch, roas_by_channel, s=200, c=plt.cm.RdYlGn(np.linspace(0.3, 0.9, len(channels))),
               alpha=0.8, edgecolors='black', linewidth=2)
    ax3.set_title('Multi-Touch Attribution vs ROAS Performance', fontweight='bold', fontsize=14)
    ax3.set_xlabel('Multi-Touch Attribution (%)')
    ax3.set_ylabel('ROAS ($)')
    ax3.grid(True, alpha=0.3)

    for i, channel in enumerate(channels):
        ax3.annotate(channel.replace('\n', ' '), (multi_touch[i], roas_by_channel[i]),
                    xytext=(5, 5), textcoords='offset points', fontweight='bold', fontsize=9)

    # Channel Efficiency Matrix
    efficiency_score = [(roas_by_channel[i] / 4.10) * (multi_touch[i] / 100) * 100 for i in range(len(channels))]
    bars5 = ax4.bar(channels, efficiency_score, color='steelblue', alpha=0.8, edgecolor='black')
    ax4.set_title('Channel Efficiency Score\n(ROAS × Attribution Weight)', fontweight='bold', fontsize=14)
    ax4.set_ylabel('Efficiency Score')
    ax4.grid(True, alpha=0.3)
    plt.setp(ax4.get_xticklabels(), rotation=45, ha='right')

    for bar in bars5:
        height = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                f'{height:.1f}', ha='center', va='bottom', fontweight='bold')

    plt.tight_layout()
    plt.savefig(output_dir / 'attribution_analysis.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_campaign_performance():
    """Enhanced Ready, Set, Ford Campaign Performance with Financial Metrics"""
    metrics = ['Brand\nAwareness', 'Consideration\nRate', 'Digital\nEngagement',
               'Lead\nGeneration', 'Conversion\nRate']
    pre_campaign = [68, 42, 3.8, 124, 18]
    post_launch = [74, 48, 5.2, 168, 24]
    targets = [75, 50, 5.5, 180, 26]
    roas_improvement = [3.45, 4.20, 5.85, 4.75, 6.20]

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))

    x = np.arange(len(metrics))
    width = 0.25

    # Performance Comparison
    bars1 = ax1.bar(x - width, pre_campaign, width, label='Pre-Campaign', alpha=0.8, color='lightcoral')
    bars2 = ax1.bar(x, post_launch, width, label='Post-Launch', alpha=0.8, color='skyblue')
    bars3 = ax1.bar(x + width, targets, width, label='Target', alpha=0.8, color='lightgreen')

    ax1.set_title('"Ready, Set, Ford" Campaign Performance vs Targets', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Performance Metrics')
    ax1.set_xticks(x)
    ax1.set_xticklabels(metrics)
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # ROAS by Campaign Metric
    bars4 = ax2.bar(metrics, roas_improvement, color=plt.cm.RdYlGn(np.linspace(0.3, 0.9, len(metrics))),
                    alpha=0.8, edgecolor='black')
    ax2.set_title('ROAS Improvement by Campaign Focus Area', fontweight='bold', fontsize=14)
    ax2.set_ylabel('ROAS ($)')
    ax2.grid(True, alpha=0.3)
    plt.setp(ax2.get_xticklabels(), rotation=45, ha='right')

    for bar in bars4:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                f'${height:.2f}', ha='center', va='bottom', fontweight='bold')

    # Performance vs Target Achievement
    achievement_rate = [(post_launch[i] / targets[i]) * 100 for i in range(len(metrics))]
    colors_achievement = ['green' if rate >= 100 else 'orange' if rate >= 90 else 'red' for rate in achievement_rate]

    bars5 = ax3.bar(metrics, achievement_rate, color=colors_achievement, alpha=0.8, edgecolor='black')
    ax3.axhline(y=100, color='black', linestyle='--', alpha=0.7, label='Target (100%)')
    ax3.set_title('Target Achievement Rate', fontweight='bold', fontsize=14)
    ax3.set_ylabel('Achievement (%)')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    plt.setp(ax3.get_xticklabels(), rotation=45, ha='right')

    for bar in bars5:
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height + 2,
                f'{height:.1f}%', ha='center', va='bottom', fontweight='bold')

    # Campaign ROI Timeline
    months = ['Launch', 'Month 1', 'Month 2', 'Month 3', 'Current']
    cumulative_roi = [1.0, 2.2, 3.8, 4.5, 5.2]

    ax4.plot(months, cumulative_roi, marker='o', linewidth=3, markersize=10, color='darkgreen')
    ax4.fill_between(months, cumulative_roi, alpha=0.3, color='lightgreen')
    ax4.set_title('Campaign ROI Growth Timeline', fontweight='bold', fontsize=14)
    ax4.set_ylabel('Cumulative ROI')
    ax4.grid(True, alpha=0.3)

    for i, roi in enumerate(cumulative_roi):
        ax4.text(i, roi + 0.1, f'{roi:.1f}x', ha='center', va='bottom', fontweight='bold')

    plt.tight_layout()
    plt.savefig(output_dir / 'enhanced_campaign_performance.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_bi_impact_dashboard():
    """Enhanced Business Intelligence Impact Dashboard"""
    bi_applications = ['Customer Data\nPlatform', 'Predictive\nAnalytics', 'Real-time\nDashboards',
                       'Sentiment\nAnalysis', 'Connected Vehicle\nData', 'Attribution\nModeling']
    roi_improvements = [22, 68, 31, 24, 52, 47]  # All positive improvements
    roas_impact = [4.20, 3.85, 4.50, 4.55, 6.10, 6.30]
    investment = [15.0, 8.0, 5.5, 3.2, 12.0, 4.8]  # Million $

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))

    # ROI Impact
    colors = plt.cm.RdYlGn(np.linspace(0.3, 0.9, len(bi_applications)))
    bars1 = ax1.bar(bi_applications, roi_improvements, color=colors, alpha=0.8, edgecolor='black')
    ax1.set_title('Business Intelligence ROI Impact by Application', fontweight='bold', fontsize=14)
    ax1.set_ylabel('ROI Improvement (%)')
    ax1.grid(True, alpha=0.3)
    plt.setp(ax1.get_xticklabels(), rotation=45, ha='right')

    for bar in bars1:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{height}%', ha='center', va='bottom', fontweight='bold')

    # ROAS Impact
    bars2 = ax2.bar(bi_applications, roas_impact, color=colors, alpha=0.8, edgecolor='black')
    ax2.set_title('ROAS Achievement by BI Application', fontweight='bold', fontsize=14)
    ax2.set_ylabel('ROAS ($)')
    ax2.axhline(y=4.20, color='red', linestyle='--', alpha=0.7, label='Baseline')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    plt.setp(ax2.get_xticklabels(), rotation=45, ha='right')

    for bar in bars2:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                f'${height:.2f}', ha='center', va='bottom', fontweight='bold')

    # Investment vs ROI Scatter
    ax3.scatter(investment, roi_improvements, s=200, c=colors, alpha=0.8, edgecolors='black', linewidth=2)
    ax3.set_title('BI Investment Efficiency (Investment vs ROI)', fontweight='bold', fontsize=14)
    ax3.set_xlabel('Investment ($M)')
    ax3.set_ylabel('ROI Improvement (%)')
    ax3.grid(True, alpha=0.3)

    for i, app in enumerate(bi_applications):
        ax3.annotate(app.replace('\n', ' '), (investment[i], roi_improvements[i]),
                    xytext=(5, 5), textcoords='offset points', fontweight='bold', fontsize=8)

    # Implementation Timeline
    implementation_years = [2021, 2022, 2023, 2023, 2024, 2024]
    cumulative_impact = np.cumsum([31, 68, 22, 24, 52, 47])

    ax4.plot(implementation_years, cumulative_impact, marker='o', linewidth=3, markersize=8, color='blue')
    ax4.fill_between(implementation_years, cumulative_impact, alpha=0.3, color='blue')
    ax4.set_title('Cumulative BI Impact Over Time', fontweight='bold', fontsize=14)
    ax4.set_xlabel('Year')
    ax4.set_ylabel('Cumulative ROI Improvement (%)')
    ax4.grid(True, alpha=0.3)

    # Add value labels
    for i, impact in enumerate(cumulative_impact):
        ax4.text(implementation_years[i], impact + 10, f'{impact:.0f}%',
                ha='center', va='bottom', fontweight='bold')

    plt.tight_layout()
    plt.savefig(output_dir / 'enhanced_bi_impact_dashboard.png', dpi=300, bbox_inches='tight')
    plt.close()

def main():
    """Generate all enhanced visualizations"""
    print("Generating Enhanced Ford Marketing Intelligence Visualizations (Version 2.0)...")

    create_marketing_roi_trend()
    print("✓ Enhanced Marketing ROI Trend with ROAS created")

    create_enhanced_segment_performance()
    print("✓ Enhanced Segment Performance with CPA and CLV created")

    create_swot_analysis_visualization()
    print("✓ SWOT Analysis Strategic Matrix created")

    create_porters_five_forces()
    print("✓ Porter's Five Forces Analysis created")

    create_customer_journey_funnel()
    print("✓ Customer Journey Funnel with ROAS/CPA created")

    create_competitive_positioning_radar()
    print("✓ Competitive Positioning Radar Chart created")

    create_attribution_analysis()
    print("✓ Marketing Attribution Multi-Touch Analysis created")

    create_campaign_performance()
    print("✓ Enhanced Campaign Performance Dashboard created")

    create_bi_impact_dashboard()
    print("✓ Enhanced Business Intelligence Impact Dashboard created")

    print(f"\nAll enhanced visualizations saved to: {output_dir}")
    print("Enhanced charts generated:")
    for chart in sorted(output_dir.glob("*.png")):
        print(f"  - {chart.name}")

    print(f"\nTotal visualizations: {len(list(output_dir.glob('*.png')))}")
    print("Version 2.0 features:")
    print("  ✓ SWOT Analysis Strategic Matrix")
    print("  ✓ Porter's Five Forces Visualization")
    print("  ✓ Enhanced metrics with ROAS and CPA")
    print("  ✓ Customer Journey Funnel Analysis")
    print("  ✓ Competitive Positioning Radar")
    print("  ✓ Marketing Attribution Analysis")

if __name__ == "__main__":
    main()