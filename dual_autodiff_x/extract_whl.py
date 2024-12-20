# import zipfile
# import os

# def extract_wheel(wheel_path, output_dir):
#     with zipfile.ZipFile(wheel_path, 'r') as whl:
#         whl.extractall(output_dir)

# wheels = [
#     ("dual_autodiff_x-0.1.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", "wheel_contents/cp310"),
#     ("dual_autodiff_x-0.1.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", "wheel_contents/cp311")
# ]

# wheels = [
#     ("wheelhouse/dual_autodiff_x-0.1.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", 
#      "wheel_contents/cp310"),
#     ("wheelhouse/dual_autodiff_x-0.1.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", 
#      "wheel_contents/cp311")
# ]

# for whl_file, output_dir in wheels:
#     os.makedirs(output_dir, exist_ok=True)
#     extract_wheel(whl_file, output_dir)
#     print(f"Extracted {whl_file} to {output_dir}")

import zipfile
import os

def extract_wheel(wheel_path, output_dir):
    """
    Extracts a .whl file to the specified output directory.
    :param wheel_path: Path to the wheel file (.whl)
    :param output_dir: Path to the output directory
    """
    with zipfile.ZipFile(wheel_path, 'r') as whl:
        whl.extractall(output_dir)  # Extract the contents

# List of wheel files and their corresponding output directories
wheels = [
    ("wheelhouse/dual_autodiff_x-0.1.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", 
     "wheelhouse/wheel_contents/cp310"),
    ("wheelhouse/dual_autodiff_x-0.1.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", 
     "wheelhouse/wheel_contents/cp311")
]

# Iterate over each wheel file and extract to the specified output directory
for whl_file, output_dir in wheels:
    os.makedirs(output_dir, exist_ok=True)  # Ensure output directory exists
    extract_wheel(whl_file, output_dir)
    print(f"Extracted {whl_file} to {output_dir}")

