import sys
import json
import os
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO

def main():
    # Set Premium Academic Style
    plt.rcParams.update({
        "font.family": "serif",
        "font.serif": ["Times New Roman", "DejaVu Serif"],
        "axes.labelsize": 10,
        "font.size": 10,
        "legend.fontsize": 8,
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,
        "axes.labelcolor": "#222222",
        "grid.color": "#666666",
        "grid.linestyle": "--",
        "grid.linewidth": 0.75,
    })

    try:
        input_data = sys.stdin.read()
        if not input_data:
            sys.exit(1)
            
        data = json.loads(input_data)
        
        c_type = data.get('type', 'bar')
        title = data.get('title', '')
        xlabel = data.get('xlabel', '')
        ylabel = data.get('ylabel', '')
        labels = data.get('labels', [])
        datasets = data.get('datasets', [])
        out_format = data.get('format', 'png')
        value_format = data.get('valueFormat', 'default')
        value_suffix = data.get('valueSuffix', '')

        def fmt_value(v):
            if value_format == 'compact':
                abs_v = abs(v)
                if abs_v >= 1_000_000:
                    return f'{v / 1_000_000:.1f}M'
                if abs_v >= 1_000:
                    return f'{v / 1_000:.1f}k'
                return f'{v:.0f}'
            if value_format == 'number':
                return f'{v:.1f}{value_suffix}'
            return f'{v:.1f}'
        
        fig, ax = plt.subplots(figsize=(5.5, 3.5))
        
        if c_type == 'bar':
            x = np.arange(len(labels))
            n_datasets = len(datasets)
            width = 0.8 / n_datasets if n_datasets > 0 else 0.8
            
            for i, ds in enumerate(datasets):
                offset = (i - n_datasets/2 + 0.5) * width
                c = ds.get('colors') or ds.get('color', '#0D47A1')
                container = ax.bar(x + offset, ds.get('data', []), width, label=ds.get('label', ''), color=c)
                labels_list = [fmt_value(v) for v in ds.get('data', [])]
                ax.bar_label(container, labels=labels_list, padding=3, fontsize=8, fontweight='bold')
                
            ax.set_xticks(x)
            ax.set_xticklabels(labels)
            
        elif c_type == 'stacked_bar':
            x = np.arange(len(labels))
            width = 0.5
            bottom = np.zeros(len(labels))
            
            for ds in datasets:
                d_vals = np.array(ds.get('data', []))
                c = ds.get('colors') or ds.get('color', '#0D47A1')
                container = ax.bar(x, d_vals, width, bottom=bottom, label=ds.get('label', ''), color=c, edgecolor='white')
                # Add percentage labels only if value > 5
                labels_list = [f'{v:.1f}%' if value_format == 'default' and v > 5 else (fmt_value(v) if value_format != 'default' and v > 0 else '') for v in d_vals]
                ax.bar_label(container, labels=labels_list, label_type='center', color='white', fontsize=8, fontweight='bold')
                bottom += d_vals
                
            ax.set_xticks(x)
            ax.set_xticklabels(labels)

        elif c_type == 'stacked_bar_h':
            y = np.arange(len(labels))
            height = 0.5
            left = np.zeros(len(labels))
            
            for ds in datasets:
                d_vals = np.array(ds.get('data', []))
                c = ds.get('colors') or ds.get('color', '#0D47A1')
                container = ax.barh(y, d_vals, height, left=left, label=ds.get('label', ''), color=c, edgecolor='white')
                # Add percentage labels only if value > 5
                labels_list = [f'{v:.1f}%' if value_format == 'default' and v > 5 else (fmt_value(v) if value_format != 'default' and v > 0 else '') for v in d_vals]
                ax.bar_label(container, labels=labels_list, label_type='center', color='white', fontsize=8, fontweight='bold')
                left += d_vals
                
            ax.set_yticks(y)
            ax.set_yticklabels(labels)
            
        elif c_type == 'line':
            x = np.arange(len(labels))
            for ds in datasets:
                ax.plot(x, ds.get('data', []), marker='o', markersize=6, linewidth=2, label=ds.get('label', ''), color=ds.get('color', '#0D47A1'))
            ax.set_xticks(x)
            ax.set_xticklabels(labels)
            
        elif c_type == 'scatter':
            for ds in datasets:
                x_vals = [pt['x'] for pt in ds.get('data', [])]
                y_vals = [pt['y'] for pt in ds.get('data', [])]
                ax.scatter(x_vals, y_vals, s=50, label=ds.get('label', ''), color=ds.get('color', '#0D47A1'), alpha=0.8, clip_on=False, edgecolor='white', linewidth=0.5)
            ax.margins(0.05)

        elif c_type == 'radar':
            # Create a new polar axis
            plt.close(fig)
            fig = plt.figure(figsize=(5.5, 4.5))
            ax = fig.add_subplot(111, polar=True)
            
            # Number of variables
            num_vars = len(labels)
            angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
            angles += angles[:1] # Close the circle
            
            for ds in datasets:
                values = ds.get('data', [])
                values += values[:1] # Close the circle
                ax.plot(angles, values, linewidth=2, label=ds.get('label', ''), color=ds.get('color', '#0D47A1'))
                ax.fill(angles, values, color=ds.get('color', '#0D47A1'), alpha=0.25)
            
            ax.set_xticks(angles[:-1])
            ax.set_xticklabels(labels)
            ax.set_ylim(0, 100) # Assuming percentage-based radar
            
        elif c_type == 'pie':
            # Pie charts don't use axes the same way
            plt.close(fig)
            fig, ax = plt.subplots(figsize=(5.5, 4.5))
            
            ds = datasets[0] if datasets else {}
            vals = ds.get('data', [])
            clrs = ds.get('colors') or ds.get('color', ['#6366f1', '#10b981', '#f59e0b', '#ec4899', '#06b6d4'])
            
            if isinstance(clrs, str): clrs = [clrs]
            
            # Filter out zero values for pie chart stability
            pie_data = []
            pie_labels = []
            pie_colors = []
            for i, v in enumerate(vals):
                if v > 0:
                    pie_data.append(v)
                    if i < len(labels): pie_labels.append(labels[i])
                    if isinstance(clrs, list) and i < len(clrs): pie_colors.append(clrs[i])
            
            if sum(pie_data) > 0:
                ax.pie(pie_data, labels=pie_labels, autopct='%1.1f%%', colors=pie_colors if pie_colors else None, 
                       startangle=140, pctdistance=0.85, wedgeprops={'edgecolor': 'white', 'linewidth': 1})
                ax.axis('equal') 
            else:
                ax.text(0.5, 0.5, "No failures recorded", ha='center', va='center')
                ax.axis('off')
            

        show_legend = data.get('showLegend', True)

        if c_type not in ['radar', 'pie']:
            if title: ax.set_title(title, pad=15, fontweight='bold')
            if xlabel: ax.set_xlabel(xlabel)
            if ylabel: ax.set_ylabel(ylabel)
            
            # Handle custom axis limits
            if 'xlim' in data: ax.set_xlim(data['xlim'])
            if 'ylim' in data: ax.set_ylim(data['ylim'])
            
            if show_legend and datasets and any(ds.get('label') for ds in datasets):
                ax.legend(loc='upper right', frameon=True)
                
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.spines['left'].set_visible(False)
            ax.spines['bottom'].set_visible(False)
            ax.tick_params(axis='both', which='both', length=0)
            ax.yaxis.grid(True)
            ax.set_axisbelow(True)
        else:
            # For radar and pie, only set title and legend if possible
            if title: fig.suptitle(title, fontweight='bold')
            if show_legend and datasets and any(ds.get('label') for ds in datasets):
                handles, l = ax.get_legend_handles_labels()
                if handles:
                    ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))

        buf = BytesIO()
        fig.savefig(buf, format=out_format, bbox_inches='tight', dpi=300)
        plt.close(fig)
        
        sys.stdout.buffer.write(buf.getvalue())
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
