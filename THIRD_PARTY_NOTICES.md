# Third-party notices

The original code in this repository is released under the MIT License (see [LICENSE](LICENSE)).
This repository also bundles (modified) code from the projects below. Each file keeps its original
copyright header. The licence of the original project applies to those files.

| Files | Origin | Licence |
|-------|--------|---------|
| `src/modeling/bert/modeling_graphormer.py`, `src/modeling/bert/e2e_hand_network.py`, `src/modeling/bert/e2e_body_network.py`, `src/modeling/_gcnn.py`, `src/datasets/build.py`, `src/datasets/hand_mesh_tsv.py`, `src/datasets/human_mesh_tsv.py`, `src/utils/comm.py`, `src/utils/tsv_file.py`, `src/utils/tsv_file_ops.py`, `src/utils/metric_logger.py`, `src/utils/dataset_utils.py` | [MeshGraphormer](https://github.com/microsoft/MeshGraphormer) / [METRO](https://github.com/microsoft/MeshTransformer), Microsoft Corporation | MIT |
| `src/modeling/our_hrnet/*`, `models/hrnet/*.yaml` | [HRNet](https://github.com/HRNet/HRNet-Image-Classification), Microsoft | MIT |
| `src/tools/models/simplebaseline.py`, `src/tools/core/config.py`, `src/tools/models/224x224.yaml` | [SimpleBaseline / human-pose-estimation.pytorch](https://github.com/microsoft/human-pose-estimation.pytorch), Microsoft | MIT |
| `src/modeling/bert/modeling_bert.py`, `src/modeling/bert/modeling_utils.py`, `src/modeling/bert/bert-base-uncased/config.json` | [HuggingFace Transformers](https://github.com/huggingface/transformers) (Google AI Language, HuggingFace, NVIDIA) | Apache-2.0 |
| `src/modeling/bert/file_utils.py` | [AllenNLP](https://github.com/allenai/allennlp) via HuggingFace | Apache-2.0 |
| `src/utils/logger.py`, `src/utils/miscellaneous.py` | [maskrcnn-benchmark](https://github.com/facebookresearch/maskrcnn-benchmark) via METRO, Facebook | MIT |
| `src/utils/bar.py` | [progress](https://github.com/verigak/progress), Giorgos Verigakis | ISC |
| `src/utils/image_ops.py` | [GraphCMR](https://github.com/nkolot/GraphCMR) and [mmdetection](https://github.com/open-mmlab/mmdetection) via METRO | BSD-3-Clause (GraphCMR), Apache-2.0 (mmdetection) |
| `src/utils/geometric_layers.py` | [pytorch_HMR](https://github.com/MandyMo/pytorch_HMR) via METRO | see upstream |
| `src/modeling/data/config.py` | [GraphCMR](https://github.com/nkolot/GraphCMR) and [Pose2Mesh](https://github.com/hongsukchoi/Pose2Mesh_RELEASE) via METRO | see upstream |

Licence texts: [MIT](https://opensource.org/license/mit), [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0),
[ISC](https://opensource.org/license/isc-license-txt), [BSD-3-Clause](https://opensource.org/license/bsd-3-clause).
For files marked "see upstream", the terms of the linked repository apply.

## Not included

The following are required or optional at run time but are **not** redistributed; download them from
their original sources under their own terms (see README, "Data preparation"):

- HRNet-W64 ImageNet weights (`hrnetv2_w64_imagenet_pretrained.pth`)
- SimpleBaseline caffe ResNet ImageNet weights (`resnet50-caffe.pth.tar`)
- FreiHAND, DARTset (including `hand_mesh.obj`), GANerated Hands and SynthHands datasets
- MANO (not used by this code)
