import matplotlib.pyplot as plt
import numpy as np
import os

# Set Premium Academic Style
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "DejaVu Serif"],
    "axes.labelsize": 10,
    "font.size": 10,
    "legend.fontsize": 8,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "axes.edgecolor": "#444444",
    "axes.labelcolor": "#222222",
    "grid.color": "#e0e0e0",
    "grid.linestyle": "--",
    "grid.linewidth": 0.5,
})

output_dir = r'c:\Users\berkk\Desktop\CodingProjects\cmpe-490\article\images'
os.makedirs(output_dir, exist_ok=True)

# Premium Colors (Muted Professional)
C_GEMINI = '#0D47A1'  # Deep Blue
C_LLAMA = '#B71C1C'   # Deep Red
C_LOGIC = '#1976D2'   # Blue
C_WHITE = '#757575'   # Grey
C_CRASH = '#D32F2F'   # Light Red
C_ACCENT = '#388E3C'  # Green

def save_and_close(name, fig):
    fig.savefig(os.path.join(output_dir, f'{name}.pdf'), bbox_inches='tight', dpi=300)
    fig.savefig(os.path.join(output_dir, f'{name}.png'), bbox_inches='tight', dpi=300)
    plt.close(fig)

def plot_1_correctness():
    labels = ['Semantic Match', 'Format Match', 'Pass@1']
    gemini = [37.5, 4.2, 20.9]
    llama = [4.3, 4.3, 0.9]

    y = np.arange(len(labels))
    height = 0.35
    fig, ax = plt.subplots(figsize=(5, 3))
    
    ax.barh(y + height/2, gemini, height, label='Gemini 3.1 Pro', color=C_GEMINI)
    ax.barh(y - height/2, llama, height, label='Llama 3 8B', color=C_LLAMA)

    ax.set_xlabel('Percentage (%)')
    ax.set_title('Translation Correctness Benchmarks', pad=15, fontweight='bold')
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    ax.set_xlim(0, 50)
    ax.invert_yaxis()
    ax.legend(loc='lower right', frameon=True, shadow=False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    save_and_close('fig1_correctness', fig)

def plot_2_paradox():
    tiers = ['Simple', 'Medium', 'Complex']
    gemini = [12.50, 32.61, 12.50]
    llama = [2.50, 0.00, 0.00]

    fig, ax = plt.subplots(figsize=(5, 3.5))
    ax.plot(tiers, gemini, marker='o', markersize=6, linewidth=2, label='Gemini 3.1 Pro', color=C_GEMINI)
    ax.plot(tiers, llama, marker='s', markersize=6, linewidth=2, linestyle='--', label='Llama 3 8B', color=C_LLAMA)

    ax.set_ylabel('Pass Rate (%)')
    ax.set_xlabel('Complexity Tier')
    ax.set_title('The Complexity Paradox Analysis', pad=15, fontweight='bold')
    ax.legend(loc='upper right')
    
    # Better positioned annotations
    ax.annotate('BVA Impact', xy=('Simple', 12.5), xytext=(0.5, 18),
                arrowprops=dict(arrowstyle='->', lw=0.8), fontsize=8, color='#444444')
    ax.set_ylim(-2, 45)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    save_and_close('fig2_paradox', fig)

def plot_3_errors():
    models = ['Gemini 3.1 Pro', 'Llama 3 8B']
    logic = [52, 63]
    whitespace = [28, 32]
    crash = [7, 13]

    x = np.arange(len(models))
    width = 0.5
    fig, ax = plt.subplots(figsize=(5, 3.5))
    
    # Stacked but with clearer separation
    p1 = ax.bar(x, logic, width, label='Logic Error', color=C_LOGIC, edgecolor='white')
    p2 = ax.bar(x, whitespace, width, bottom=logic, label='Whitespace Mismatch', color=C_WHITE, edgecolor='white')
    p3 = ax.bar(x, crash, width, bottom=np.array(logic)+np.array(whitespace), label='Runtime Crash', color=C_CRASH, edgecolor='white')

    ax.set_ylabel('Count of Failed Tests')
    ax.set_title('Detailed Error Type Distribution', pad=15, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(models)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=3, frameon=False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    save_and_close('fig3_errors', fig)

def plot_4_quality():
    metrics = ['Pylint Score\n(Scaled x10)', 'Complexity\nReduction (%)', 'LOC Ratio\n(Inverse %)']
    gemini = [86.9, 51.9, 41.0] # 1 - 0.59
    llama = [90.6, 63.9, 47.0]  # 1 - 0.53

    y = np.arange(len(metrics))
    height = 0.35
    fig, ax = plt.subplots(figsize=(5.5, 3.5))
    
    ax.barh(y + height/2, gemini, height, label='Gemini 3.1 Pro', color=C_GEMINI)
    ax.barh(y - height/2, llama, height, label='Llama 3 8B', color=C_LLAMA)

    ax.set_xlabel('Score / Percentage')
    ax.set_title('Static Code Quality Comparison', pad=15, fontweight='bold')
    ax.set_yticks(y)
    ax.set_yticklabels(metrics)
    ax.set_xlim(0, 100)
    ax.invert_yaxis()
    ax.legend(loc='lower right', frameon=True)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    save_and_close('fig4_quality', fig)

def plot_5_bidirectional():
    modes = ['Forward Translation', 'Reverse Validation']
    gemini = [37.5, 43.3]
    llama = [4.3, 29.6]

    x = np.arange(len(modes))
    width = 0.35
    fig, ax = plt.subplots(figsize=(5, 3.5))
    ax.bar(x - width/2, gemini, width, label='Gemini 3.1 Pro', color=C_GEMINI)
    ax.bar(x + width/2, llama, width, label='Llama 3 8B', color=C_LLAMA)

    ax.set_ylabel('Semantic Match Rate (%)')
    ax.set_title('Dual-Track Semantic Validation', pad=15, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(modes)
    ax.set_ylim(0, 55)
    ax.legend(loc='upper center', frameon=True)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    save_and_close('fig5_bidirectional', fig)

def plot_6_tokens():
    # Switching to Horizontal Bar for legibility
    tasks = ['Reverse Input Gen', 'Boundary Case Gen']
    prompt = [96039, 82767]
    completion = [22713, 35686]

    y = np.arange(len(tasks))
    height = 0.5
    fig, ax = plt.subplots(figsize=(5.5, 2.5))
    
    ax.barh(y, prompt, height, label='Prompt Tokens', color='#2196F3', alpha=0.9)
    ax.barh(y, completion, height, left=prompt, label='Completion Tokens', color='#00BCD4', alpha=0.9)

    ax.set_xlabel('Total Token Consumption')
    ax.set_title('Operational Cost Breakdown', pad=10, fontweight='bold')
    ax.set_yticks(y)
    ax.set_yticklabels(tasks)
    ax.legend(loc='lower right', frameon=True)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    save_and_close('fig6_tokens', fig)

if __name__ == "__main__":
    plot_1_correctness()
    plot_2_paradox()
    plot_3_errors()
    plot_4_quality()
    plot_5_bidirectional()
    plot_6_tokens()
    print("Premium Analytical Charts generated successfully.")
