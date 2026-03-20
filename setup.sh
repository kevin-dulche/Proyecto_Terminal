#!/bin/bash

# 1. Crear el entorno base desde el archivo YAML
echo "Creando entorno Conda base..."
conda env create -f environment.yml

# 2. Configurar Conda en el shell actual para poder usar 'conda activate'
source /opt/conda/etc/profile.d/conda.sh
conda activate qm9-similitud

# 3. Lógica condicional para la GPU
if command -v nvidia-smi &> /dev/null; then
    echo "✅ GPU NVIDIA detectada. Instalando PyTorch con soporte CUDA 11.8..."
    conda install -y pytorch==2.2.0 pytorch-cuda=11.8 -c pytorch -c nvidia
else
    echo "🖥️ No se detectó GPU. Instalando PyTorch versión CPU..."
    conda install -y pytorch==2.2.0 cpuonly -c pytorch
fi

# 4. Asegurar que el entorno se active automáticamente al abrir la terminal
echo 'conda activate qm9-similitud' >> ~/.bashrc