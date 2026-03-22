# Exploración del Espacio Químico QM9
## Reducción de Dimensionalidad, Similitud Molecular y Mapas Topológicos

---

## Descripción

Este proyecto construye y explora un espacio vectorial sobre el dataset **QM9** (~134,000 moléculas pequeñas). El objetivo es representar cada molécula como un punto en un espacio matemático donde la cercanía geométrica refleja similitud estructural, y luego explorar ese espacio mediante búsquedas, funciones de similitud y mapas topológicos interactivos.

**Pipeline completo:**
```
Moléculas (SMILES)
        ↓
   mol2vec (300D embeddings)
        ↓
   Autoencoder PyTorch (300D → 32D)
        ↓
   Cholesky (Euclidiana = Mahalanobis)
        ↓
   Chupón Gaussiano  |  UMAP/t-SNE + HDBSCAN
```

---

## Estructura de carpetas

```
Proyecto_Terminal/
├── notebooks/
│   └── Similitud.ipynb       ← notebook principal
├── data/                        ← se genera automáticamente al ejecutar
│   ├── qm9.csv
│   ├── qm9_embeddings_flat.csv
│   ├── qm9_embeddings.npy
│   ├── qm9_latent.npy
│   ├── qm9_latent_mahalanobis_space.npy
│   ├── qm9_umap_2d.npy
│   └── qm9_tsne_2d.npy
├── models/                      ← se genera automáticamente al ejecutar
│   └── model_300dim.pkl
├── html/                        ← mapas interactivos generados al ejecutar
│   ├── mapa_topologico_HDBSCAN_UMAP.html
│   ├── mapa_topologico_HDBSCAN_T-SNE.html
│   ├── mapa_chupon_umap.html
│   └── mapa_chupon_tsne.html
├── .devcontainer/
│   └── devcontainer.json
├── requirements.txt
├── environment.yml
└── README.md                    ← este archivo
```

> Los directorios `data/`, `models/` y `html/` se crean automáticamente
> en la celda 0 del notebook si no existen.

---

## Requisitos previos

- Python >= 3.8
- conda
- Conexión a internet (para descargar el dataset y el modelo la primera vez)
- Docker para la Opción A


---

## Opción A: Codespaces

1. Abrir el siguiente link y dejar que se configure todo el contenedor, despues Ejecutar todas las celdas de Similitud.ipynb dentro de la carpeta notebooks en orden.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/kevin-dulche/Proyecto_Terminal?quickstart=1)

---

## Opción B: Entorno con conda (Linux / macOS / Windows)

```bash
# 1. Crear el entorno desde el archivo yml
conda env create -f environment.yml

# 2. Activar el entorno
conda activate qm9-similitud

# 3. Abrir el notebook
jupyter notebook notebooks/Similitud_v2.ipynb
```

> mol2vec se instala automáticamente desde GitHub como parte del
> bloque `pip:` en `environment.yml`.
>
> **Windows:** usa Anaconda Prompt en lugar de PowerShell para los
> comandos `conda`. El resto del proceso es idéntico.

> **macOS con Apple Silicon (M1/M2/M3):** PyTorch tiene soporte nativo
> para el acelerador MPS. Puedes reemplazar `"cuda"` por `"mps"` en la
> celda del autoencoder si quieres aprovechar la GPU integrada.
> El resto del notebook funciona sin cambios.

> En Windows se recomienda usar **Anaconda Prompt** o **PowerShell**.
> `mol2vec` requiere que `git` esté instalado y disponible en el PATH
> ([descargar git para Windows](https://git-scm.com/download/win)).

> **Nota Windows:** `hdbscan` puede requerir compiladores de C++ en
> algunos sistemas. Si la instalación falla, instala primero las
> [Build Tools de Visual Studio](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
> y vuelve a ejecutar.

---

## Opción C: Google Colab

1. Sube la carpeta `Proyecto_Terminal/` a Google Drive.
2. Abre `notebooks/Similitud_v2.ipynb` desde Colab
   (Archivo → Abrir → Google Drive).
3. En la **celda 0**, ajusta `BASE_DIR` a la ruta de tu carpeta en Drive:
   ```python
   BASE_DIR = '/content/drive/MyDrive/Proyecto_Terminal'
   ```
4. Ejecuta la **celda de instalación (sección 0.1)**. Solo es necesaria
   la primera vez; las siguientes ejecuciones pueden saltarla.
5. Ejecuta todas las celdas en orden (Runtime → Run all).

> En Colab la descarga del dataset y los embeddings se guardan en Drive,
> así que no se recalculan en sesiones posteriores.

---

## Opción D: Dev Container (VS Code)

1. Instala la extensión **Dev Containers** en VS Code.
2. Abre la carpeta `Proyecto_Terminal/` en VS Code.
3. Cuando aparezca el aviso "Reopen in Container", acéptalo.
4. El contenedor instala automáticamente todas las dependencias
   (incluido mol2vec desde GitHub) al crear el entorno.
5. Abre `notebooks/Similitud_v2.ipynb` desde el explorador de VS Code.
6. Ejecutar todas las celdas en orden.

---

## Salidas generadas

Todos los mapas interactivos se guardan en `html/` y se pueden
abrir directamente en cualquier navegador moderno sin dependencias
adicionales.

- `mapa_topologico_HDBSCAN_UMAP.html` — clusters químicos sobre proyección UMAP
- `mapa_topologico_HDBSCAN_T-SNE.html` — mismos clusters sobre proyección t-SNE
- `mapa_chupon_umap.html` — vecindad gaussiana de una molécula sobre UMAP
- `mapa_chupon_tsne.html` — vecindad gaussiana de una molécula sobre t-SNE
