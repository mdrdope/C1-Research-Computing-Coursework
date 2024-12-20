# dual_autodiff

A Python package for automatic differentiation using dual numbers.

## Features
- Supports addition, subtraction, multiplication, division
- Implements common mathematical functions like sin, cos, log, exp, etc.
- Designed for automatic differentiation

## Repo Structure

### `dual_autodiff`  
```plaintext
dual_autodiff/
├── dual_autodiff/
│   ├── __init__.py
│   ├── dual.py
├── tests/
│   ├── __init__.py
│   ├── test_dual.py
├── pyproject.toml
```
Description:  
`dual_autodiff` is a Python library for automatic differentiation.  
- The `dual.py` file contains the core logic of operations and functions automatic differentiation.  
- The `tests/` folder includes unit tests.  
- The `pyproject.toml` file manages project dependencies and build configurations. 

### `dual_autodiff_x`
```plaintext
dual_autodiff_x/
├── wheelhouse/
├── __init__.py
├── dual.c
├── dual.cp39-win_amd64.pyd
├── dual.pyx
├── pyproject.toml
├── setup.py
├── extract_whl.py
```

Description:  
`dual_autodiff_x` is an optimized version of the `dual_autodiff` library, leveraging Cython.  
- The `dual.c` and `dual.pyx` files implement the core logic using C and Cython for speed improvements.  
- Precompiled binaries (e.g., `dual.cp39-win_amd64.pyd`) ensure compatibility with specific Python versions and platforms.  
- The `extract_whl.py` script is used to extract the contents of wheel.  

### `docs`
```plaintext
docs/
├── build/
│   ├── doctrees/
│   ├── html/
├── source/
│   ├── conf.py
│   ├── dual_autodiff.ipynb
│   ├── index.rst
│   ├── modules.rst
├── make.bat
├── Makefile
```

Description:  
The `docs` folder contains all files and scripts for building project documentation using Sphinx.  
- The `source/` directory includes the configuration file.  
- The `dual_autodiff.ipynb` file provides an example notebook showcasing the usage of the library.  
- The `build/` directory stores generated documentation, including HTML outputs.  


### `dual_autodiff_docker`
```plaintext
dual_autodiff_docker/
├── Dockerfile
├── dual_autodiff_x_nb.tar
├── dual_autodiff_x-0.1.0-cp310-cp310-manylinux2_17_x86_64.manylinux2014_x86_64.whl
├── dual_autodiff_x-0.1.0-cp311-cp311-manylinux2_17_x86_64.manylinux2014_x86_64.whl
├── dual_autodiff_x.ipynb
```
Description:  
The `dual_autodiff_docker` directory contains resources for setting up a Docker environment for the `dual_autodiff_x` project.  
- The **Dockerfile** specifies instructions to build the Docker image.  
- The **.tar file** (`dual_autodiff_x_nb.tar`) is a pre-built Docker image that can be loaded directly using `docker load`.  
- Wheel files (`.whl`) provide platform-specific, precompiled versions of `dual_autodiff_x` for Python 3.10 and 3.11.  
- The **Jupyter Notebook** (`dual_autodiff_x.ipynb`) demonstrates how to use the `dual_autodiff_x` library within the Docker container.
---
## Environment and Dependencies Setup

To set up the environment and install the required dependencies, run the following commands step by step:

```bash
conda create -n my_env python=3.9 -y

conda activate my_env

# Navigate to the directory containing requirements.txt
cd /path/to/requirements_directory

pip install --no-cache-dir -r requirements.txt

# Install Pandoc from conda-forge
conda install -c conda-forge pandoc
```

### Installing `dual_autodiff`
This part corresponds to Q4.

To install the `dual_autodiff` package in editable mode, follow these steps:

```bash
# Navigate to the directory containing the 'dual_autodiff' package
# Ensure that pyproject.toml is located in this directory
cd /path/to/dual_autodiff

# Install the package in editable mode
pip install -e .
```

### Running Tests with Pytest
This part corresponds to Q6.

To run tests using `pytest`, navigate to the `dual_autodiff` directory (where the `tests` folder is located) and execute the following command:

```bash
# Navigate to the dual_autodiff directory
cd /path/to/dual_autodiff

# Run pytest with the -s flag to display print statements
pytest -s tests
```

### Building Documentation with Sphinx
This part corresponds to Q7.

To generate the HTML documentation using Sphinx, run the following command in the root directory of the Sphinx project (`/docs`):

```bash
# Navigate to the Sphinx project root directory
cd /path/to/docs

# Build the HTML documentation
make html
```

Once the build is complete, open the following file in your file explorer to view the generated documentation:

```bash
docs/build/html/index.html
```


### Installing `dual_autodiff_x` Package
This part corresponds to Q8.

To install the `dual_autodiff_x` package in editable mode, follow these steps:

```bash
# Navigate to the dual_autodiff_x directory(Where dual.pyx is located)
cd /path/to/dual_autodiff_x

# Install the package in editable mode
pip install -e .
```

Note: This step requires `Microsoft C++ Build Tools` to be installed.

### Build Wheels Instructions
This part corresponds to Q10.

To build the wheels, follow these steps:

1. Ensure Docker is running in the background.

2. Navigate to the `dual_autodiff_x` directory:
    ```bash
    cd dual_autodiff_x
    ```

3. Run the `cibuildwheel` command to create the wheel files:
    ```bash
    cibuildwheel --output-dir wheelhouse
    ```

    *Note*: Be aware that there may be network issues with Docker during this process.

4. After the build process completes, extract the wheel contents:
    ```bash
    python extract_whl.py
    ```

5. This will generate two folders containing the unzipped `.whl` files under the `dual_autodiff_x/wheelhouse/wheel_contents` directory.

### Docker Instructions
This part corresponds to Q11.
#### Option 1: Build Docker Image

1. Navigate to the directory containing the `Dockerfile`:
    ```bash
    cd <directory_containing_dockerfile>
    ```

2. Build the Docker image:
    ```bash
    docker build -t <name_of_your_image> .
    ```

3. Run the Docker container:
    ```bash
    docker run -p 8888:8888 <name_of_your_image>
    ```

4. Open your browser and navigate to:
    ```
    http://localhost:8888
    ```

5. Select Python 3 as the kernel in Jupyter Notebook.

---

#### Option 2: Use Pre-built Docker Image (dual_autodiff_x_nb.tar)

If you want to load and use the pre-built Docker image (`dual_autodiff_x_nb.tar`), follow these steps:

1. Navigate to the directory containing the `.tar` file:
    ```bash
    cd <directory_containing_dual_autodiff_x_nb.tar>
    ```

2. Load the Docker image from the `.tar` file:
    ```bash
    docker load -i dual_autodiff_x_nb.tar
    ```

3. Ensure the image is successfully loaded. You should see:
    ```
    Loaded image: dual_autodiff_x_nb:latest
    ```

4. Run the Docker container:
    ```bash
    docker run -p 8888:8888 dual_autodiff_x_nb
    ```

5. Open your browser and navigate to:
    ```
    http://localhost:8888
    ```

6. Choose Python 3 as the kernel in Jupyter Notebook.

---

**Important Note:**

If you use the provided dual_autodiff_x_nb.tar file, please be aware that due to network issues I encountered (I'm located in China with an unstable VPN), the notebook still imports `dual_autodiff` but the environment only has `dual_autodiff_x`.


## Declaration of Auto Generation Tools

This project leverages AI tools to assist in the development process. Specifically:
- **Code**: Portions of the code were generated using ChatGPT-4o based on pseudocode and instructions provided by the author.
- **Report**: The project report and documentation were created using ChatGPT-4o, guided by the author's detailed instructions.

However, all ideas, concepts, and the overall project structure are entirely the author's own.


## License
This project is licensed under the terms specified in the `LICENSE` file.