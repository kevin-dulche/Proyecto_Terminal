import subprocess
import shutil

def main():
    env_name = "qm9-similitud"

    print("1. Creando entorno base desde environment.yml...")
    # Ejecuta la creación del entorno base
    subprocess.run(["conda", "env", "create", "-f", "environment.yml"], check=True)

    print("2. Detectando hardware...")
    # shutil.which busca 'nvidia-smi' en las variables de entorno (funciona en Windows y Linux)
    has_gpu = shutil.which("nvidia-smi") is not None

    if has_gpu:
        print("✅ GPU NVIDIA detectada. Instalando PyTorch con soporte CUDA 11.8...")
        subprocess.run([
            "conda", "install", "-n", env_name, "-y", 
            "pytorch==2.2.0", "pytorch-cuda=11.8", "-c", "pytorch", "-c", "nvidia"
        ], check=True)
    else:
        print("🖥️ No se detectó GPU. Instalando PyTorch versión CPU...")
        subprocess.run([
            "conda", "install", "-n", env_name, "-y", 
            "pytorch==2.2.0", "cpuonly", "-c", "pytorch"
        ], check=True)

    print(f"✅ ¡Listo! Entorno '{env_name}' configurado correctamente.")

if __name__ == "__main__":
    main()