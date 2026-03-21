import subprocess
import shutil
import sys

def instalar_entorno():
    env_name = "qm9-similitud"
    print("🔍 Detectando hardware del sistema...")

    # Buscamos si los drivers de NVIDIA están instalados y accesibles
    has_gpu = shutil.which("nvidia-smi") is not None

    if has_gpu:
        print("✅ GPU NVIDIA detectada.")
        yaml_file = "environment_gpu.yml"
    else:
        print("🖥️ No se detectó GPU NVIDIA (o no está en el PATH).")
        yaml_file = "environment.yml"

    print(f"🚀 Creando el entorno '{env_name}' usando {yaml_file}...")
    print("⏳ Esto puede tardar varios minutos dependiendo de tu conexión a internet.\n")

    try:
        # Limpiamos la caché de conda para evitar problemas de espacio o paquetes corruptos
        print("🧹 Limpiando la caché de Conda...")
        subprocess.run(["conda", "clean", "--all", "-y"], check=True)
    except FileNotFoundError:
        print("\n❌ Error: No se encontró el comando 'conda'. Asegúrate de tener Anaconda instalado y en el PATH.")
        sys.exit(1)

    try:
        # Ejecutamos el comando de conda para crear el entorno
        subprocess.run(
            ["conda", "env", "create", "-f", yaml_file], 
            check=True
        )
        print(f"\n✨ ¡Éxito! El entorno '{env_name}' se ha creado correctamente.")
        print(f"👉 Para activarlo, ejecuta: conda activate {env_name}")
        
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error al crear el entorno. Revisa el archivo {yaml_file} y tu instalación de Conda.")
        sys.exit(1)
    except FileNotFoundError:
        print("\n❌ Error: No se encontró el comando 'conda'. Asegúrate de estar ejecutando esto desde Anaconda Prompt.")
        sys.exit(1)

if __name__ == "__main__":
    instalar_entorno()