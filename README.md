# Enhancing 3D Hand Pose Estimation Using SHaF  
[![Paper](https://img.shields.io/badge/📄Paper-APIN_2024-blue)](https://doi.org/10.1007/s10489-024-05665-x)
[![Git](https://img.shields.io/badge/GitHub-LightHand-purple?logo=github)](https://github.com/eejeongho3214/LightHand)

Code repository for the paper: **"Enhancing 3D hand pose estimation using SHaF: synthetic hand dataset including a forearm"**, published in *Applied Intelligence(APIN)*, 2024.

**Authors:** Jeongho Lee¹, Changho Kim¹, Jaeyun Kim¹, Seon Ho Kim², Younggeun Choi¹, Sang-Il Choi¹<br>
¹ Dankook University, South Korea <br>
² University of Southern California, United States


---

## 🌟 Overview
We propose:

- **SHaF**: A synthetic hand image dataset including the **forearm**, generated with Unity.
- A transformer-based 3D hand pose estimation model that **does not require 3D mesh** annotations, yet outperforms mesh-based SOTA methods.

<img src="docs/model.png" width="650">  

---

## 📁 Directory Structure
```
{$ROOT}
|-- build
|-- src
|-- datasets
|-- models
|-- docs
```

---

## ⚙️ Setup with Conda
```bash
git clone https://github.com/leejeongho3214/Wearable_Pose_Model.git
cd Wearable_Pose_Model
conda env create -f requirements.yaml
```

---

## 🏋️ Training

If you are located in the project root directory:
```bash
cd src/tools
python train.py
```

> 🔧 If you encounter path issues, add below code into `train.py`
```python
import sys
sys.path.append("/usr/your/path/Wearable_Pose_Model")
```

---

## 📊 Results

### 📐 Evaluation Metrics
- PA-MPJPE (mm)
- AUC (PCK-based)

### 🧪 Quantitative Results

### Table 1: Performance Comparison on Different Training Datasets

| Dataset               | Backbone         | PA-MPJPE (mm) ↓ |
|-----------------------|------------------|-----------------|
| GANerated Hands [33]  | -                | 24.7            |
| Synthetic Hands [34]  | -                | 31.4            |
| DART [30]             | HRNet [15]       | 23.1            |
| **SHaF only (Ours)**  | HRNet [15]       | **21.3**        |
| FreiHAND              | SimpleBaseline   | 5.6             |
| **FreiHAND + Ours**   | SimpleBaseline   | **5.5**         |
| FreiHAND              | HRNet [15]       | 5.3             |
| **FreiHAND + Ours**   | HRNet [15]       | **5.2**         |

---

### Table 2: Effect of Forearm in Dataset

| SHaF Dataset     | PA-MPJPE (mm) ↓ |
|------------------|-----------------|
| w/o. forearm     | 22.1            |
| **w/. forearm**  | **21.3**        |

---

### Table 3: Effect of Number of Transformer Blocks

| Identical Blocks (N) | AUC ↑   | PA-MPJPE (mm) ↓ |
|----------------------|--------|-----------------|
| 1                    | 0.888  | 5.64            |
| 2                    | 0.892  | 5.4             |
| 3                    | 0.894  | 5.31            |
| 4                    | 0.895  | **5.28**        |

---

### Table 4: Inference Speed Comparison (FreiHAND)

| Model             | PA-MPJPE (mm) ↓ | Speed (fps) ↑ |
|------------------|------------------|---------------|
| MeshGraphormer   | 5.9              | 12.5          |
| **Ours**         | **5.2**          | **23.31**     |

---

### Table 5: SOTA Comparison on FreiHAND

| Model               | Backbone    | Mesh Needed | PA-MPJPE (mm) ↓ |
|---------------------|-------------|-------------|-----------------|
| RHD [31]            | ResNet50    | ✗           | -               |
| FreiHAND [25]       | ResNet50    | ✓           | 11.0            |
| YoutubeHand [36]    | ResNet50    | ✓           | 8.4             |
| I2L-MeshNet [37]    | ResNet50    | ✓           | 7.4             |
| HIU-DMTL [26]       | -           | ✓           | 7.1             |
| CMR [55]            | ResNet50    | ✓           | 6.9             |
| I2UV-HandNet [56]   | ResNet50    | ✓           | 6.7             |
| METRO [18]          | HRNet       | ✓           | 6.7             |
| Tang et al. [57]    | ResNet50    | ✓           | 6.7             |
| MeshGraphormer [17] | HRNet       | ✓           | 5.9             |
| **Ours**            | HRNet       | ✗           | **5.2**         |

---

### Table 6: Ablation Study of APEM and PGB Modules

| Backbone       | Method        | PA-MPJPE (mm) ↓ |
|----------------|---------------|-----------------|
| SimpleBaseline | Base          | 5.88            |
|                | PGB           | 5.80            |
|                | APEM          | 5.78            |
|                | PGB+APEM      | **5.61**        |
| HRNet          | Base          | 5.36            |
|                | PGB           | 5.29            |
|                | APEM          | 5.30            |
|                | PGB+APEM      | **5.27**        |




---

## 📸 SHaF Dataset Characteristics

- 9,000 poses × 82 camera presets = **738,000 synthetic RGB images**
- **Forearm included** to reflect real-world scenes
- Biomechanically valid joint ranges
- t-SNE shows **uniform pose distribution**
- **Data augmentation** with backgrounds and transformations
<p align="center">
  <img src="docs/Fig8_Samples.png" width="50%" style="display:inline-block; margin-right:10px;">
  <img src="docs/Fig9_Augmentation.png" width="40%" style="display:inline-block;">
</p>

---

## 🔧 Model Design Highlights

- **Pose Graph Module (PGM)**: Uses joint adjacency for relational modeling  
- **Auxiliary Pose Estimation Module (APEM)**: Improves gradient flow with 2D supervision  
- No 3D mesh needed → **lightweight & accurate** model


---

## 📖 Citation

```bibtex
@article{lee2024shaf,
  author    = {Lee, Jeongho and Kim, Jaeyun and Kim, Seon Ho and Choi, Sang-Il},
  title     = {Enhancing 3D hand pose estimation using SHaF: synthetic hand dataset including a forearm},
  journal   = {Applied Intelligence},
  year      = {2024},
  volume    = {54},
  number    = {20},
  pages     = {9565--9578},
  doi       = {10.1007/s10489-024-05665-x}
}
```

---

## 📧 Contact

> Dankook University, Korea <br>
> Ph.D program, Department in Computer Science <br>
> Jeongho Lee: [72210297@dankook.ac.kr](mailto:72210297@dankook.ac.kr)
