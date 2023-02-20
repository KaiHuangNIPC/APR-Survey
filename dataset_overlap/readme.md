# Dataset Overlap
**We have created this project to shed light on the dataset overlap problem. We welcome more researchers to submit more overlap samples to us to continuously expand this project. This project will provide important support to the APR community.**

## What is dataset overlap ?
The dataset overlap problem refers to the train dataset and test benchmark overlap. The problem may cause the model to learn the correct fix for the test sample during the training phase, which may lead to the illusion of getting good repair results.

Here we give a simple example to illustrate the dataset overlap problem. Figure 1 shows an overlapping part in the train dataset and the test benchmark (Defects4J). Therefore, the overlapping projects need to be removed from the training set during the model training process.
>Figure 1. A example of dataset overlap.
![图片1](https://user-images.githubusercontent.com/102460432/219946126-547f36fc-76bb-4228-a395-bb1d312368d0.jpg)


## Dataset Overlap in Real world Train-dataset
In order to learn more about the data overlap problem in APR work, we conducted preliminary experiments and found that data overlap is a common phenomenon, which raises concerns about the quality of the training data used in APR work.

Here, we mainly analyze the dataset overlap problem in the current APR work using [Defects4J](https://github.com/rjust/defects4j) as the test benchmark. In detail, we obtain the training data of these works and use exact matching to find whether these datasets contain the fixes in Defects4J (which is similar to the approach of Xia et al. [1])

First, we first analyzed and obtained the APR works that performed the tests on Defects4J and downloaded their corresponding training datasets.

| Test Benchmark  | Defects4J V1.2 | Defects4J V1.2 | Defects4J V1.2 | Defects4J V1.2 | Defects4J V1.2 | Defects4J V1.2 | Defects4J V1.2 | Defects4J V1.2 | Defects4J V2.0 | Defects4J V2.0 |
| ------------- | ------------- |------------- |------------- |------------- |------------- |------------- |------------- |------------- |------------- |------------- |
| **APR Tool**  |  SequenceR [2]  | DLFix [3] | CoCoNut [4] | Recoder [5] | CURE [6] | RewardRepair[7] | DEAR [8] | CIRCLE [9] | Recoder [5] | RewardRepair [7] |
| **Train Dataset**  | [BFP](https://www.google.com/url?q=https%3A%2F%2Fzenodo.org%2Frecord%2F7478730%2Ffiles%2FBFP_datasets.zip%3Fdownload%3D1&sa=D&sntz=1&usg=AOvVaw2sWE-2ztdr-uvuVUvE1nc0)+[CodRep](https://github.com/KTH/CodRep-competition/)  | [BigFix](https://drive.google.com/open?id=1KL3M-BbisVLWXyvn05V6huSLNUby_9qN) | [CoCoNut](https://github.com/lin-tan/CoCoNut-Artifact/releases) | [Recoder](https://drive.google.com/drive/folders/1ECNX98qj9FMdRT2MXOUY6aQ6-sNT0b_a?usp=sharing) | [CoCoNut](https://github.com/lin-tan/CoCoNut-Artifact/releases) | [CoCoNut](https://github.com/lin-tan/CoCoNut-Artifact/releases)+[MegaDiff](https://github.com/monperrus/megadiff)+[CodRep](https://github.com/KTH/CodRep-competition/)+[CodRep](https://github.com/KTH/CodRep-competition/) | [CPatMiner](https://drive.google.com/open?id=1M_0dRYqhCMh26GQbnX4Igp_2jSrTS1tV) | [CoCoNut](https://github.com/lin-tan/CoCoNut-Artifact/releases) | [Recoder](https://drive.google.com/drive/folders/1ECNX98qj9FMdRT2MXOUY6aQ6-sNT0b_a?usp=sharing) | [CoCoNut](https://github.com/lin-tan/CoCoNut-Artifact/releases)+[MegaDiff](https://github.com/monperrus/megadiff)+[CodRep](https://github.com/KTH/CodRep-competition/) |


Second, we use exact matching to check the presence of Defects4J's patch information in the large-scale training dataset.
Here we summarize the dataset overlap results of each training dataset with Defects4J:
| Train Dataset | Overlap Bug Num. | Overlap Defects4J Bug-ID |
| ------------- | ------------- | ------------- |
| BFP | - | - |
| BigFix | - | - |
| CoCoNut 2006 | 2 | Lang-58, Lang-59 |
| CodRep | 61 | Codec-1, Codec-10, Codec-3, Codec-4, Codec-6, Collections-2, Collections-3, Collections-7, Compress-1, Compress-10, Compress-14, Compress-20, Compress-25, Compress-3, Compress-4, Compress-6, Csv-4, Csv-7, Lang-20, Lang-21, Lang-23, Lang-24, Lang-30, Lang-32, Lang-33, Lang-35, Lang-36, Lang-38, Lang-41, Lang-43, Lang-57, Lang-59, Lang-60, Lang-61, Lang-8, Math-10, Math-100, Math-104, Math-105, Math-22, Math-23, Math-32, Math-33, Math-38, Math-59, Math-6, Math-61, Math-62, Math-64, Math-65, Math-68, Math-69, Math-70, Math-72, Math-75, Math-77, Math-78, Math-81, Math-82, Math-96, Math-98 |
| CPatMiner | 10 | Cli-31, Cli-34, Csv-4, Csv-7, JacksonCore-11, JacksonDatabind-27, JacksonDatabind-4, JacksonDatabind-50, Time-13, Time-7 |
| MegaDiff | 99 | Closure-100, Closure-101, Closure-102, Closure-104, Closure-105, Closure-108, Closure-113, Closure-114, Closure-119, Closure-123, Closure-125, Closure-130, Closure-133, Closure-137, Closure-14, Closure-140, Closure-141, Closure-148, Closure-149, Closure-150, Closure-156, Closure-160, Closure-162, Closure-174, Closure-18, Closure-25, Closure-26, Closure-27, Closure-29, Closure-32, Closure-38, Closure-4, Closure-40, Closure-43, Closure-50, Closure-51, Closure-52, Closure-57, Closure-62, Closure-63, Closure-64, Closure-68, Closure-70, Closure-71, Closure-73, Closure-79, Closure-80, Closure-85, Closure-86, Closure-89, Closure-9, Closure-92, Closure-93, Closure-99, Codec-2, Codec-3, Codec-4, Codec-7, JacksonDatabind-1, JacksonDatabind-22, JacksonDatabind-60, JacksonDatabind-87, JxPath-10, Math-10, Math-11, Math-15, Math-16, Math-2, Math-28, Math-30, Math-33, Math-34, Math-35, Math-41, Math-46, Math-5, Math-56, Math-59, Math-63, Math-68, Math-69, Math-70, Math-72, Math-75, Math-81, Math-82, Math-83, Math-94, Math-98, Mockito-17, Mockito-29, Mockito-35, Mockito-36, Mockito-38, Mockito-6, Time-13, Time-16, Time-19, Time-4 |
| Recoder | 7 | Math-69, Math-70, Math-79, Math-94, Closure-83, Closure-119, Closure-120 |

> Note: The java training data of CoCoNut contains both CoCoNut 2006 and CoCoNut 2010 versions, due to the memory limitation of our experiment, here we only analyze the 2006 version.

Finally, we give the source files in the training dataset where dataset overlap occurred. We suggest that researchers remove these overlapping source files in subsequent work in order to test the real repair capability on Defects4J.


CoCoNut-Defects4J Overlap: [Overlap_result](APR-Survey/dataset_overlap/overlap_D4j_CoCoNut/overlap_result.txt)

CodRep-Defects4J Overlap: [Overlap_result](APR-Survey/dataset_overlap/overlap_D4j_CodRep/overlap_result.txt)

CPatMiner-Defects4J Overlap: [Overlap_result](APR-Survey/dataset_overlap/overlap_D4j_CPatMiner/overlap_result.txt)

MegaDiff-Defects4J Overlap: [Overlap_result](APR-Survey/dataset_overlap/overlap_D4j_MegaDiff/overlap_result.txt)

Recoder-Defects4J Overlap: [Overlap_result](APR-Survey/dataset_overlap/overlap_D4j_Recoder/overlap_code_info.txt)


## Ref

[1] Xia C S, Zhang L. Less training, more repairing please: revisiting automated program repair via zero-shot learning[C]//Proceedings of the 30th ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering. 2022: 959-971.

[2] Chen Z, Kommrusch S, Tufano M, et al. Sequencer: Sequence-to-sequence learning for end-to-end program repair[J]. IEEE Transactions on Software Engineering, 2019, 47(9): 1943-1959.

[3] Li Y, Wang S, Nguyen T N. Dlfix: Context-based code transformation learning for automated program repair[C]//Proceedings of the ACM/IEEE 42nd International Conference on Software Engineering. 2020: 602-614.

[4] Lutellier T, Pham H V, Pang L, et al. Coconut: combining context-aware neural translation models using ensemble for program repair[C]//Proceedings of the 29th ACM SIGSOFT international symposium on software testing and analysis. 2020: 101-114.

[5] Zhu Q, Sun Z, Xiao Y, et al. A syntax-guided edit decoder for neural program repair[C]//Proceedings of the 29th ACM Joint Meeting on European Software Engineering Conference and Symposium on the Foundations of Software Engineering. 2021: 341-353.

[6] Jiang N, Lutellier T, Tan L. Cure: Code-aware neural machine translation for automatic program repair[C]//2021 IEEE/ACM 43rd International Conference on Software Engineering (ICSE). IEEE, 2021: 1161-1173.

[7] Ye H, Martinez M, Monperrus M. Neural program repair with execution-based backpropagation[C]//Proceedings of the 44th International Conference on Software Engineering. 2022: 1506-1518.

[8] Li Y, Wang S, Nguyen T N. Dear: A novel deep learning-based approach for automated program repair[C]//Proceedings of the 44th International Conference on Software Engineering. 2022: 511-523.

[9] Yuan W, Zhang Q, He T, et al. CIRCLE: continual repair across programming languages[C]//Proceedings of the 31st ACM SIGSOFT International Symposium on Software Testing and Analysis. 2022: 678-690.
