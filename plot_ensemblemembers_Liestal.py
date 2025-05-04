import os

# === Configuration ===
ensemble_members = list(range(1, 12))
time_steps = ["0000", "0012", "0024", "0036", "0048", "0060"]
image_suffix = "_nocbar.png"
image_prefix_template = "Liestal_2m_{ens}_{ens}-"
image_folder = "."
output_html = os.path.join(image_folder, "slider_all_ensembles_with_cbar_slider_top.html")

html_start = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Ensemble Viewer</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f7f7f7;
            margin: 0;
            padding: 0;
        }
        .slider-container {
            text-align: center;
            padding: 10px;
            background-color: #eeeeee;
        }
        input[type=range] {
            width: 40%;
            height: 25px;
        }
        .wrapper {
            display: flex;
            flex-direction: row;
            height: calc(100vh - 60px);
        }
        .grid {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            align-items: flex-start;
            gap: 20px;
            padding: 20px;
            flex-grow: 1;
            overflow-y: auto;
        }
        .panel {
            width: 320px;
        }
        .panel img {
            max-width: 100%;
            height: auto;
            border: 1px solid #ccc;
        }
        .panel h4 {
            font-size: 14px;
            margin: 5px 0;
        }
        .side-panel {
            width: 120px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            background-color: #eeeeee;
            padding: 10px;
        }
        .side-panel img {
            width: 80px;
            margin-top: 10px;
        }
    </style>
</head>
<body>

<div class="slider-container">
    <label for="leadSlider"><strong>Lead Time:</strong></label><br>
    <input type="range" min="0" max="{max_idx}" value="0" id="leadSlider">
</div>
<div class="wrapper">
<div class="grid">
""".replace("{max_idx}", str(len(time_steps) - 1))

# Add image panels
image_divs = ""
for ens in ensemble_members:
    img_id = f"img_ens{ens}"
    img_src = image_prefix_template.format(ens=ens) + time_steps[0] + image_suffix
    image_divs += f"""
    <div class="panel">
        <h4>Ensemble {ens}</h4>
        <img id="{img_id}" src="{img_src}" alt="Ensemble {ens}">
    </div>
    """

# Colorbar panel
side_panel = """
</div>
<div class="side-panel">
    <img src="water_depth_cbar_vertical.png" alt="Colorbar">
</div>
</div>
"""

# JavaScript
script = f"""
<script>
    const steps = {time_steps};
    const suffix = "{image_suffix}";

    document.getElementById("leadSlider").addEventListener("input", function() {{
        const step = steps[this.value];
"""

for ens in ensemble_members:
    prefix = f"Liestal_2m_{ens}_{ens}-"
    img_id = f"img_ens{ens}"
    script += f'document.getElementById("{img_id}").src = "{prefix}" + step + suffix;\n'

script += """
    });
</script>
</body>
</html>
"""

# Combine and save
full_html = html_start + image_divs + side_panel + script

with open(output_html, "w") as f:
    f.write(full_html)

import pathlib
path = pathlib.Path(output_html).resolve()
path