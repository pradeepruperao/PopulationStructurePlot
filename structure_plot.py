#!/usr/bin/env python3
import svgwrite

def read_admixture_file(filename):
    samples = []
    proportions = []
    with open(filename) as f:
        for line in f:
            parts = line.strip().split()
            samples.append(parts[0])
            props = list(map(float, parts[1:]))
            proportions.append(props)
    return samples, proportions

def create_structure_plot(samples, proportions, output_file="structure_plot.svg"):
    num_samples = len(samples)
    num_k = len(proportions[0])
    show_sample_names = num_samples <= 50
    horizontal_layout = num_samples > 100  # switch to horizontal if too many samples

    import svgwrite

    # Color palette (extendable)
    colors = [
        "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
        "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf",
        "#393b79", "#637939", "#8c6d31", "#843c39", "#7b4173"
    ]
    if num_k > len(colors):
        import random
        colors.extend([
            svgwrite.utils.rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            for _ in range(num_k - len(colors))
        ])

    if horizontal_layout:
        # Horizontal layout for >100 samples
        bar_width = 1  # each sample gets 1px width
        bar_height = 300  # total height of stacked K components
        spacing = 0
        total_width = num_samples * (bar_width + spacing) + 50
        total_height = bar_height + 50

        dwg = svgwrite.Drawing(output_file, size=(total_width, total_height), profile='full')
        dwg.add(dwg.rect(insert=(0, 0), size=(total_width, total_height), fill='white'))

        for i, props in enumerate(proportions):
            x = 30 + i * (bar_width + spacing)
            y = 30
            for k in range(num_k):
                segment_height = props[k] * bar_height
                dwg.add(dwg.rect(insert=(x, y), size=(bar_width, segment_height),
                                 fill=colors[k], stroke='black', stroke_width=0))
                y += segment_height

    else:
        # Standard vertical layout for ≤100 samples
        bar_width = 400
        spacing = 10
        bar_height = 30
        font_size = 16
        left_margin = 100 if show_sample_names else 10
        total_height = num_samples * (bar_height + spacing) + 50
        total_width = bar_width + left_margin + 100

        dwg = svgwrite.Drawing(output_file, size=(total_width, total_height), profile='full')
        dwg.add(dwg.rect(insert=(0, 0), size=(total_width, total_height), fill='white'))

        for i, (sample, props) in enumerate(zip(samples, proportions)):
            y = 30 + i * (bar_height + spacing)

            if show_sample_names:
                dwg.add(dwg.text(sample, insert=(10, y + bar_height / 2 + 5),
                                 font_size=font_size, fill="black"))

            x = left_margin
            for k in range(num_k):
                segment_width = props[k] * bar_width
                dwg.add(dwg.rect(insert=(x, y), size=(segment_width, bar_height),
                                 fill=colors[k], stroke='black', stroke_width=0))
                x += segment_width

    dwg.save()
    print(f"SVG saved as {output_file}")


if __name__ == "__main__":
    samples, proportions = read_admixture_file("test2.txt")
    create_structure_plot(samples, proportions)

