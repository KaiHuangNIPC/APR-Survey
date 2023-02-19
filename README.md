# APR-Survey
A Survey on Automated Program Repair Techniques










# Dataset Overlap
The dataset overlap problem refers to the training data and test benchmark overlap. The problem may cause the model to learn the correct fix for the test sample during the training phase, which may lead to the illusion of getting good repair results.


Here we give a simple example to illustrate the dataset overlap problem. Figure 1 shows an overlapping part in the train dataset and the test benchmark (Defects4J). Therefore, the overlapping projects need to be removed from the training set during the model training process.
>Figure 1. A example of dataset overlap.
![图片1](https://user-images.githubusercontent.com/102460432/219946126-547f36fc-76bb-4228-a395-bb1d312368d0.jpg)


## Dataset Overlap in Real world Train-dataset
In order to learn more about the data overlap problem in APR work, we conducted preliminary experiments and found that data overlap is a common phenomenon, which raises concerns about the quality of the training data used in APR work.

Here, we mainly analyze the dataset overlap problem in the current APR work using [Defects4J](https://github.com/rjust/defects4j) as the test benchmark. In detail, we obtain the training data of these works and use exact matching to find whether these datasets contain the fixes in Defects4J (which is similar to the approach of Xia et al.)

First, we first analyzed and obtained the APR works that performed the tests on Defects4J and downloaded their corresponding training datasets.

| Test Benchmark  | Defects4J V1.2 | Defects4J V1.2 | Defects4J V1.2 | Defects4J V1.2 | Defects4J V1.2 | Defects4J V1.2 | Defects4J V1.2 | Defects4J V1.2 | Defects4J V2.0 | Defects4J V2.0 |
| ------------- | ------------- |------------- |------------- |------------- |------------- |------------- |------------- |------------- |------------- |------------- |
| **APR Tool**  |  SequenceR [2]  | DLFix [3] | CoCoNut [4] | Recoder [5] | CURE [6] | RewardRepair[7] | DEAR [8] | CIRCLE [9] | Recoder [5] | RewardRepair [7] |
| **Train Dataset**  | [BFP](https://www.google.com/url?q=https%3A%2F%2Fzenodo.org%2Frecord%2F7478730%2Ffiles%2FBFP_datasets.zip%3Fdownload%3D1&sa=D&sntz=1&usg=AOvVaw2sWE-2ztdr-uvuVUvE1nc0)+[CodRep](https://github.com/KTH/CodRep-competition/)  | [BigFix](https://drive.google.com/open?id=1KL3M-BbisVLWXyvn05V6huSLNUby_9qN) | [CoCoNut](https://github.com/lin-tan/CoCoNut-Artifact/releases) | [Recoder](https://drive.google.com/drive/folders/1ECNX98qj9FMdRT2MXOUY6aQ6-sNT0b_a?usp=sharing) | [CoCoNut](https://github.com/lin-tan/CoCoNut-Artifact/releases) | [CoCoNut](https://github.com/lin-tan/CoCoNut-Artifact/releases)+[MegaDiff](https://github.com/monperrus/megadiff)+[CodRep](https://github.com/KTH/CodRep-competition/)+[CodRep](https://github.com/KTH/CodRep-competition/) | [CPatMiner](https://drive.google.com/open?id=1M_0dRYqhCMh26GQbnX4Igp_2jSrTS1tV) | [CoCoNut](https://github.com/lin-tan/CoCoNut-Artifact/releases) | [Recoder](https://drive.google.com/drive/folders/1ECNX98qj9FMdRT2MXOUY6aQ6-sNT0b_a?usp=sharing) | [CoCoNut](https://github.com/lin-tan/CoCoNut-Artifact/releases)+[MegaDiff](https://github.com/monperrus/megadiff)+[CodRep](https://github.com/KTH/CodRep-competition/) |


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

