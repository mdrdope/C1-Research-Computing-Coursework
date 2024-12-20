# Use Python 3.10 slim as the base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the .whl files from the local machine into the container
COPY dual_autodiff_x-0.1.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl /app/
COPY dual_autodiff_x.ipynb /app/source/dual_autodiff_x.ipynb

# Upgrade pip, setuptools, and wheel to ensure compatibility
RUN pip install --upgrade pip setuptools wheel

# Install the Python 3.10 wheel by default
RUN pip install /app/dual_autodiff_x-0.1.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl

# Install Jupyter Notebook
RUN pip install notebook

# Expose the default Jupyter Notebook port
EXPOSE 8888

# Start Jupyter Notebook and open dual_autodiff_x.ipynb
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''", "--notebook-dir=/app/source", "/app/source/dual_autodiff_x.ipynb"]