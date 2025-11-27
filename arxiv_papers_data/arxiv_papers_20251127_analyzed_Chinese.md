# 20251127
[![Subscribe_Visitors](https://visitor-badge.laobi.icu/badge?page_id=nituchao.latest_arxiv_analyze_ai_rss)](https://github.com/nituchao/latest_arxiv_analyze_ai)

## 1. `cs.AI` - NOEM^3A: 一种增强语义本体的神经符号方法，用于移动智能体的多意图理解 [PDF](https://arxiv.org/pdf/2511.19780), [HTML](https://arxiv.org/abs/2511.19780)
### Authors
Ioannis Tzachristas,Aifen Sui
### Background
本文介绍了将结构化的意图本体与紧凑的语言模型相结合的神经符号框架，以提高移动智能体的多意图理解能力。该方法利用检索增强提示、logit偏差和可选的分类头，将符号意图结构注入到输入和输出表示中。通过引入基于层次本体深度的新评估度量标准——语义意图相似度(Semantic Intent Similarity, SIS)，该方法捕捉到了即使预测的意图在词汇上不同，也能捕捉到的语义距离。
### Innovation
提出了利用检索增强提示和logit偏差的新的神经符号框架，通过结构化的意图本体增强紧凑语言模型，以提升移动智能体的多意图理解。通过语义意图相似度(SIS)作为新的评估指标，展示了增强本体的模型在多意图理解精度上接近GPT-4的效果，且能量和内存消耗显著减少。增强本体的模型能产生更具体和去歧义的多意图解释。
### Conclusion
实验结果验证了符号对齐是一种有效策略，能够使设备上自然语言理解既准确又高效。
## 2. `cs.AI` - KOM：一种用于精确管理膝关节骨关节炎的多智能体人工智能系统 [PDF](https://arxiv.org/pdf/2511.19798), [HTML](https://arxiv.org/abs/2511.19798)
### Authors
Weizhi Liu,Xi Chen,Zekun Jiang,Liang Zhao,Kunyuan Jiang,Ruisi Tang,Li Wang,Mingke You,Hanyu Zhou,Hongyu Chen,Qiankun Xiong,Yong Nie,Kang Li,Jian Li
### Background
膝关节骨关节炎（KOA）影响全球超过6亿人，与显著的疼痛、功能障碍和残疾有关。虽然个性化的多学科干预可能减缓疾病进展并提高生活质量，但这些通常需要大量的医疗资源和专业知识，难以在资源有限的地区实施。
### Innovation
我们开发了KOM（Knee Osteoarthritis Management），这是一种多智能体系统，旨在自动化KOA评估、风险预测和治疗处方。该系统通过支持个体患者的定制管理计划，协助临床医生执行KOA护理路径中关键任务，并基于患者的个人资料、疾病状态、风险因素和禁忌症提供定制管理方案。实验表明，与多个通用大型语言模型相比，KOM在影像分析和处方生成中的性能更优。随机三组模拟研究还显示，KOM与临床医生合作可将诊断和规划时间减少38.5%，并提高了治疗质量。
### Conclusion
这些结果表明，KOM有助于促进KOA的自动化管理，并在集成到临床工作流程中时，有可能提高护理效率。KOM的模块化结构也可能为其他慢性疾病的AI辅助管理系统的开发提供有价值的经验教训。
## 3. `cs.AI` - 依赖查询的统一评估指导框架促进提示优化 [PDF](https://arxiv.org/pdf/2511.19829), [HTML](https://arxiv.org/abs/2511.19829)
### Authors
Ke Chen,Yifeng Wang,Hassan Almosapeeh,Haohan Wang
### Background
大多数提示优化方法仅针对单一静态模板进行改进，这在复杂和动态用户场景中效果不佳。现有查询依赖的方法依赖于不稳定的文本反馈或黑盒奖励模型，提供了弱且不可解释的优化信号。更根本的是，提示质量缺乏统一、系统性的定义，导致评估信号不一致和不可靠。
### Innovation
本文首先建立了一种以性能为导向、系统且全面的提示评估框架。进一步开发并微调了一个无需执行的评估器，直接从文本预测多维度质量评分。该评估器指导了一个具有度量意识的优化器，通过解释查询依赖的方式诊断故障模式并重写提示。评估器在预测提示性能方面达到了最强的准确性，且基于评估的优化在多个数据集和三种主干模型上都优于静态模板和查询依赖的基本方法。
### Conclusion
本文提出了一个统一、基于度量的观点来讨论提示质量，并展示了我们的评估指导优化流程在不同任务上的稳定、可解释且模型无关的改进。
## 4. `cs.AI` - 工具集成推理中用于VLM的代理强化学习扩展 [PDF](https://arxiv.org/pdf/2511.19773), [HTML](https://arxiv.org/abs/2511.19773)
### Authors
Meng Lu,Ran Xu,Yi Fang,Wenxuan Zhang,Yue Yu,Gaurav Srivastava,Yuchen Zhuang,Mohamed Elhoseiny,Charles Fleming,Carl Yang,Zhengzhong Tu,Yang Xie,Guanghua Xiao,Hanrui Wang,Di Jin,Wenqi Shi,Xuan Wang
### Background
虽然最近的视觉-语言模型（VLMs）在图像理解方面表现出色，但在通过多步视觉交互进行“基于图像思考”的能力上仍然有限。现有的VLMs在仅文本推理方面表现出色，但在工具选择、调用和协调方面仍存在问题。
### Innovation
VISTA-Gym通过引入一个新的可扩展训练环境，打破了这一局限性。它集成了多种多模态推理任务，并提供了标准化的视觉工具接口、可执行的交互循环、可验证的反馈信号和高效的轨迹记录，从而促进了大规模的视觉代理强化学习。研究团队使用VISTA-Gym训练了VISTA-R1，使模型能够进行工具运用与代理推理的交替，实验结果表明VISTA-R1的性能优于原型和开源基线模型。
### Conclusion
通过广泛的实验，作者证明了VISTA-Gym能够有效提高VLMs的工具集成推理能力，使VLMs能够通过多轮轨迹采样和端到端的强化学习实现工具集成推理，在11个公开的推理密集型VQA基准测试中，VISTA-R1-8B的表现比同类最佳模型高出9.51%-18.72%。这表明，VISTA-Gym可以成为解锁VLMs工具集成推理能力的有效训练平台。
## 5. `cs.AI` - HeaRT：一种基于分层电路推理树的自主框架，用于AMS设计优化 [PDF](https://arxiv.org/pdf/2511.19669), [HTML](https://arxiv.org/abs/2511.19669)
### Authors
Souradip Poddar,Chia-Tung Ho,Ziming Wei,Weidong Cao,Haoxing Ren,David Z. Pan
### Background
传统的AI驱动的AMS设计自动化算法受到对高质数据集的依赖限制，难以捕捉电路本质行为，适应性差且缺乏适应机制。
### Innovation
本文提出了HeaRT，一种基础推理引擎，是迈向智能、适应性强的人类风格设计优化的第一步。HeaRT在40个电路基准库中的推理解释准确性超过97%，在1级通过性能超过98%，即使电路复杂度增加，也能以小于SOTA基线0.5倍的实时标记预算运行。实验表明，HeaRT在各种优化方法下的大小和拓扑设计适应任务中，收敛速度提高了3倍，同时保留了先前的设计意图。
### Conclusion
HeaRT在AMS设计优化中展示了出色的性能和适应性，为自动化设计提供了一种新的思路。
## 6. `cs.AI` - FISCAL: Financial Synthetic Claim-document Augmented Learning for Efficient Fact-Checking [PDF](https://arxiv.org/pdf/2511.19671), [HTML](https://arxiv.org/abs/2511.19671)
### Authors
Rishab Sharma,Iman Saberi,Elham Alipour,Jie JW Wu,Fatemeh Fard
### Background
金融应用中，大型语言模型（LLMs）需要具备事实可靠性和计算效率，然而当前系统常常会产生虚假细节，并依赖于过于庞大的模型。因此，研究者们寻找更为高效的解决方案。
### Innovation
提出了一种模块化框架FISCAL，用于生成适用于金融事实核查的合成数据。通过FISCAL生成的数据集FISCAL-data，训练了一个轻量级的数值型金融声明验证器MiniCheck-FISCAL。MiniCheck-FISCAL在性能上超越了基线模型以及相同规模的开源竞品，并接近了更大系统的准确率（20倍）。在外部分析数据集FinDVer和Fin-Fact中，它也与GPT-4o和Claude-3.5竞争，甚至超越了Gemini-1.5 Flash。
### Conclusion
领域专门的合成数据与高效微调的结合，使得紧凑的模型在金融AI领域能够实现最先进的准确度、稳定性和可扩展性。
## 7. `cs.AI` - 大型语言模型中的模拟自我评估：一种针对AI自我效能的心理测量方法 [PDF](https://arxiv.org/pdf/2511.19872), [HTML](https://arxiv.org/abs/2511.19872)
### Authors
Daniel I Jackson,Emma L Jensen,Syed-Amad Hussain,Emre Sezgin
### Background
可靠的情报依赖于自我评估，但对大型语言模型（LLMs）的评估主要集中在任务准确率上。本文通过改进的一般自我效能感量表（GSES）收集了十种LLMs在不同条件下的模拟自我评估，这些条件包括：无任务、计算推理、社会推理以及总结。
### Innovation
以心理测量学的方法评估LLMs的自我效能，通过调整GSES量表来收集LLMs在不同情境下的自我评估，并分析不同条件下模型的自我评估稳定性，以及如何反映能力。
### Conclusion
虽然部分低分模型仍可准确完成任务，高分模型的概括能力较弱。首次评估后的置信度提示仅小幅调整，表明初步自我评估可能略有高估。高自我效能与更自信、拟人化的推理风格相关，而低分数反映了谨慎的、非拟人化的解释。心理测量方法为理解LLMs的通信行为提供了结构化的见解，但不提供准确的表现估计。
## 8. `cs.AI` - RPM-MCTS: 使用蒙特卡洛树搜索的知识检索作为过程奖励模型在代码生成中的应用 [PDF](https://arxiv.org/pdf/2511.19895), [HTML](https://arxiv.org/abs/2511.19895)
### Authors
Yuanyuan Lin,Xiangyu Ouyang,Teng Zhang,Kaixin Sui
### Background
树搜索基于的方法在提升大型语言模型的代码生成能力方面取得了显著进展。然而，由于难以有效地评估中间算法步骤的有效性，无法准确定位并及时修正错误步骤，这些方法往往会生成错误代码，并增加计算成本。
### Innovation
提出了一种有效的方法RPM-MCTS，利用基于蒙特卡洛树搜索的知识检索作为过程奖励模型来评估中间算法步骤。通过知识库检索避免了过程奖励模型的复杂训练。在扩展阶段，使用相似性过滤来移除冗余节点，确保推理路径的多样性。此外，利用沙盒执行反馈来定位生成过程中的错误算法步骤，实现及时和有针对性的修正。
### Conclusion
通过在四个公开的代码生成基准上的广泛实验，结果表明RPM-MCTS优于当前最先进的方法，并且大约减少了15%的令牌消耗。此外，使用RPM-MCTS构建的数据进行模型的全面微调显著提升了其代码生成能力。
## 9. `cs.AI` - Fara-7B: 一种高效的计算机使用代理模型 [PDF](https://arxiv.org/pdf/2511.19663), [HTML](https://arxiv.org/abs/2511.19663)
### Authors
Ahmed Awadallah,Yash Lara,Raghav Magazine,Hussein Mozannar,Akshay Nambi,Yash Pandya,Aravind Rajeswaran,Corby Rosset,Alexey Taymanov,Vibhav Vineet,Spencer Whitehead,Andrew Zhao
### Background
计算机使用代理（CUAs）的发展受限于缺乏大规模和高质量的数据集，这些数据集能够捕捉人类与计算机交互的方式。尽管大型语言模型（LLMs）在丰富的文本数据上取得了蓬勃发展，但在CUA轨迹方面，没有同等规模的语料库。为了解决这些问题，我们介绍了FaraGen，这是一种新型的合成数据生成系统，用于多步骤网络任务。FaraGen能够从常用网站中提出多样化任务，生成多个解决方案尝试，并使用多个验证器过滤成功轨迹。它能够实现高吞吐量、高产量和多样的多步骤网络任务，生成验证轨迹的成本约为1美元。
### Innovation
FaraGen 是一种合成数据生成系统，用于多步骤网络任务，其能够从常用网站中提出多样化任务，生成多个解决方案尝试，并使用多个验证器过滤成功轨迹。Fara-7B 是一种基于合成数据训练的原生计算机使用代理模型，不依赖于互联网，能够通过屏幕截图感知计算机，执行通过预测坐标预测的动作，并且足够小以在设备上运行。Fara-7B 在 WebVoyager、Online-Mind2Web 和 WebTailBench（一种新的基准测试，更好地捕捉现有基准测试中未充分代表的网络任务）等基准测试中表现出色，与其他规模相当的CUA模型相比，表现优于其他模型。此外，Fara-7B 的性能与远大于自身规模的前沿模型相当，证明了可扩展数据生成系统在推进小型高效代理模型方面的关键优势。
### Conclusion
我们正在将 Fara-7B 的预训练权重开放到 Microsoft Foundry 和 HuggingFace，并发布 WebTailBench。
## 10. `cs.AI` - Semantic-KG：利用知识图谱构建衡量语义相似性的基准 [PDF](https://arxiv.org/pdf/2511.19925), [HTML](https://arxiv.org/abs/2511.19925)
### Authors
Qiyao Wei,Edward Morrell,Lea Goetz,Mihaela van der Schaar
### Background
当前评估大型语言模型（LLMs）生成的开放式文本响应时，通常需要测量这些响应与（人类生成的）参考文本的语义相似性。然而，目前的语义相似性方法可能存在捕捉表面语法或词汇形式而非语义内容的问题。尽管存在一些语义等价性的基准，但这些基准往往因依赖主观的人类判断、领域特定应用的有限可用性和语义等价性定义不清而产生的较高生成成本。本文旨在通过利用知识图谱生成语义相似或不相似的自然语言陈述对，解决这些问题，并构建不同领域的基准数据集，以评估语义相似性方法。
### Innovation
本文 introduces了一种新的方法来生成测试语义相似性方法的基准数据集，该方法利用知识图谱生成基于4种亚类型的语义相似或不相似的语句对，并在4个不同领域（通用知识、生物医学、金融、生物学）生成基准数据集。此外，该研究还比较了使用传统自然语言处理得分和LLM作为裁判进行语义相似性评估的方法，发现不同类型的语义变异和基准领域会影响到语义相似性方法的表现，没有一种方法能够始终在所有情况下表现最佳。
### Conclusion
本文的结果对使用LLM作为裁判检测文本语义内容具有重要意义。研究还发现，不同类型的语义变异以及基准领域的不同会对语义相似性方法的表现产生影响，因此应谨慎选择利弊。代码可在给定的URL地址获取，数据集也可在提供的URL地址下载。
## 11. `cs.AI` - 使用ω-正规目标和约束条件的强化学习 [PDF](https://arxiv.org/pdf/2511.19849), [HTML](https://arxiv.org/abs/2511.19849)
### Authors
Dominik Wagner,Leon Witzman,Luke Ong
### Background
传统的强化学习（RL）依赖于单一标量奖励，无法充分表达时间上的、条件下的或安全性关键的目标，容易导致奖励作弊。ω-正规目标（ω-regular objectives）通过更通用的类来表达时序逻辑，能够精确指定复杂的规范行为，但仍需通过单一的标量（无论奖励还是满足概率）来衡量性能，掩盖了风险可接受水平条件下安全与性能之间的权衡。
### Innovation
本文通过结合ω-正规目标与显式约束，可以在既能满足安全需求，又能优化目标的情况下解决上述问题。提出了一种基于线性规划的模型导向的RL算法，在极限状态下能够产生最大化满足ω-正规目标和约束条件下满足度的概率的策略。
### Conclusion
本文通过建立一个权重－正规目标和约束的模型导向的RL算法来解决单一标量评价以及安全与性能间权衡的问题。限定了一个优化保有的约束问题，该算法能够在设定的阈值内实现的同时最大化满足ω-正规目标和遵守ω-正规约束。
## 12. `cs.AI` - MicroSims: 一种生成式人工智能、可扩展的教育资源框架，支持无界嵌入与自适应学习支持 [PDF](https://arxiv.org/pdf/2511.19864), [HTML](https://arxiv.org/abs/2511.19864)
### Authors
Valerie Lockhart,Dan McCreary,Troy A. Peterson
### Background
教育资源模拟长期以来被证实是提高学习成果的强大工具，但其创建通常需要大量资源和专业技术。MicroSims通过引入一套独特的创新，解决了这一问题。
### Innovation
MicroSims提出了三个关键创新：标准化设计模式以支持AI辅助生成、基于iframe的架构以便于无界嵌入和沙箱安全以及可修改的透明代码以支持定制和教学透明度。
### Conclusion
MicroSims为教育资源提供了一种具有重要意义的框架，通过自动生成、平台无关性和透明代码支持定制，降低成本和提高教育公平性，从而实现按需创建定制化、课纲对齐的模拟。未来将侧重于基于MicroSims基础的自适应学习系统的开发和实施考虑。
## 13. `cs.AI` - M$^3$Prune: 高效多模态多智能体检索增强生成的层次通信图修剪 [PDF](https://arxiv.org/pdf/2511.19969), [HTML](https://arxiv.org/abs/2511.19969)
### Authors
Weizi Shao,Taolin Zhang,Zijie Zhou,Chen Chen,Chengyu Wang,Xiaofeng He
### Background
最近在多模态检索增强生成（mRAG）方面的进展表明，多智能体系统的集体智慧可以通过有效的通信显著超越单一模型。尽管取得了出色的性能，现有的多智能体系统天然地带来了大量的标记开销和增加的计算成本，这为大规模部署带来了挑战。
### Innovation
我们提出了一种新的多模态多智能体层次通信图修剪框架，称为M$^3$Prune。该框架通过消除不同模态之间的冗余边，实现了在任务性能和标记开销之间取得最优平衡。具体来说，M$^3$Prune首先对文本和视觉模态应用图稀疏化，并识别对解决任务至关重要的边。然后，我们使用这些关键边构建动态通信拓扑，并进行跨模态图稀疏化。最后，我们逐步修剪冗余边，以获得更高效和分层的拓扑结构。实验结果显示，我们的方法在通用和特定领域的mRAG基准测试上，不仅优于单智能体和稳健的多智能体mRAG系统，还显著减少了标记消耗。
### Conclusion
我们的M$^3$Prune框架通过层次化通信图修剪有效地优化了多模态多智能体mRAG系统的性能和效率，能够在保持甚至提高任务性能的同时大大减少标记开销。
## 14. `cs.AI` - 使用可穿戴设备改善阿片类物质使用障碍患者慢性疼痛治疗 [PDF](https://arxiv.org/pdf/2511.19577), [HTML](https://arxiv.org/abs/2511.19577)
### Authors
Abhay Goyal,Navin Kumar,Kimberly DiMeola,Rafael Trujillo,Soorya Ram Shimgekar,Christian Poellabauer,Pi Zonooz,Ermonda Gjoni-Markaj,Declan Barry,Lynn Madden
### Background
慢性疼痛（CP）和阿片类物质使用障碍（OUD）是两种常见的且相互关联的慢性疾病。目前，对于正在接受阿片类物质使用障碍治疗药物（MOUD）的个体而言，缺乏基于证据的整合治疗方法。可穿戴设备有可能监测复杂患者的多种信息，并为OUD和CP患者提供治疗方法开发的依据，包括疼痛波动（如疼痛加剧或疼痛高峰）和临床相关因素（如感知压力）。然而，大型语言模型（LLMs）在利用可穿戴数据理解和解释疼痛高峰方面尚未得到研究。
### Innovation
本研究的目的是通过一系列人工智能方法探讨疼痛高峰的临床相关因素。我们发现，机器学习模型在预测疼痛高峰方面达到了相对较高的准确率（>0.7），而LLMs对疼痛高峰的洞察有限。实时监测结合先进的AI模型，有助于早期检测疼痛高峰并支持个性化干预，这些干预可能有助于降低阿片类物质复吸的风险、提高MOUD的依从性，并增强CP和OUD护理的整合。
### Conclusion
鉴于大型语言模型的整体表现有限，研究结果强调了在OUD/CP背景下开发可提供可操作洞察的大型语言模型的必要性。
## 15. `cs.AI` - 6G时代具有代理AI赋能的对话式实体智能网络 [PDF](https://arxiv.org/pdf/2511.19865), [HTML](https://arxiv.org/abs/2511.19865)
### Authors
Mingkai Chen,Zijie Feng,Lei Wang,Yaser Khamayseh
### Background
6G时代，多种实体智能设备（MEIDs）之间的语义协作对于复杂任务执行至关重要，但现有系统在多模态信息融合、自适应通信和决策解释性方面面临挑战。
### Innovation
文章提出了一种结合多模态特征融合、自适应语义通信、任务协调和解释性能力的协作式对话式实体智能网络（CC-EIN）模型。PerceptiNet负责跨模态融合图像和雷达数据以生成统一的语义表示。自适应语义通信策略根据任务紧迫性和信道质量动态调整编码方案和传输功率。同时，语义驱动的协作机制支持异构设备之间的任务分解和无冲突协调。InDec模块通过Grad-CAM可视化增强决策透明度。
### Conclusion
仿真结果表明，在地震救援场景中，CC-EIN实现了95.4%的任务完成率和95%的传输效率，同时保持了强大的语义一致性和能效。
## 16. `cs.AI` - 使用大型语言模型扩展项目与标准的对齐：准确性、局限性和解决方案 [PDF](https://arxiv.org/pdf/2511.19749), [HTML](https://arxiv.org/abs/2511.19749)
### Authors
Farzan Karimi-Malekabadi,Pooya Razavi,Sonya Powers
### Background
随着教育系统的演变，确保评估项目与内容标准保持一致对于维护公平性和教学相关性至关重要。传统的人工对齐审查非常准确，但速度慢且劳动密集，特别是在大规模题库中。研究探讨了大型语言模型（LLMs）是否可以加速这一过程而不牺牲准确性。
### Innovation
本研究使用超过12,000个K-5年级的项目技能对进行测试，尝试了三种LLMs（GPT-3.5 Turbo、GPT-4o-mini和GPT-4o），并在三个任务中测试了它们：识别未对齐的项目、从整套标准中选择正确的技能以及在分类前过滤候选名单。研究结果显示，GPT-4o-mini在约83-94%的情况下正确识别了对齐状态，包括细微的偏离。研究还表明，过滤候选技能可以显著提高结果，正确技能出现在前五推荐中的比例超过95%。这表明，特别是当与候选筛选策略结合使用时，LLMs可以显著减轻人工审核项目的负担，同时保持对齐的准确性。
### Conclusion
研究建议开发结合LLM基筛选与人工审核的混合流程，在模糊情况下使用，提供了一个可扩展的持续项目验证和教学对齐解决方案。
## 17. `cs.AI` - 大型语言模型应用中的系统级失败模式分类 [PDF](https://arxiv.org/pdf/2511.19933), [HTML](https://arxiv.org/abs/2511.19933)
### Authors
Vaishali Vinay
### Background
大型语言模型（LLMs）正迅速被整合到决策支持工具、自动化工作流和AI驱动的软件系统中。然而，在生产环境中的行为仍然不太被理解，其故障模式与传统的机器学习模型有着根本的不同。因此，本文通过系统级的分类列举了十五种在现实世界LLM应用中出现的隐藏故障模式，包括多步推理漂移、隐含不一致、上下文边界退化、错误工具调用、版本漂移以及成本驱动性能崩溃。
### Innovation
本文提出了一个系统级的大型语言模型失败模式分类，涵盖了现实世界应用中出现的多种隐藏故障模式，并指出了现有基准测试的不足，无法从稳定性、可重复性、漂移或工作流集成方面提供深入洞见。还分析了在生产环境中部署LLM面临的挑战，如可观察性限制、成本约束以及更新引起的倒退，并提出了构建可靠、可维护且成本意识强的LLM系统的高层次设计原则。
### Conclusion
通过将LLM可靠性视为系统工程问题而不是单纯建模中的问题，本文为未来关于评估方法论、AI系统稳健性和可依赖的大规模语言模型部署的研究奠定了分析基础。
## 18. `cs.AI` - 我们完成了任务吗？：一种基于视觉的自主任务完成评估器 [PDF](https://arxiv.org/pdf/2511.20067), [HTML](https://arxiv.org/abs/2511.20067)
### Authors
Marta Sumyk,Oleksandr Kosovan
### Background
计算机使用代理（CUAs）被设计成能够自主操作数字接口，但它们经常无法可靠地确定给定的任务是否已完成。现有的评估框架主要依赖人工反馈，这既耗时又不经济。因此，本研究旨在开发一种基于视觉的语言模型，能够直接从屏幕截图和任务描述中评估任务完成情况。
### Innovation
本文提出了一种自主评估和反馈框架，该框架利用视觉-语言模型直接从屏幕截图和任务描述中评估任务完成情况。该研究构建了一个包含42个内置macOS应用程序和1260个人工标注任务的数据集，覆盖了广泛的情景。该框架在任务成功检测方面的准确率达到最高73%，当评估者反馈应用时，整体任务成功率平均提高了27%。
### Conclusion
基于视觉的评估可以作为一种有效的反馈机制，提高自主计算机使用代理的可靠性和自我纠正能力。
## 19. `cs.AI` - VICoT-Agent: 一种实现可解释的多模态推理和可扩展遥感分析的视觉交织推理框架 [PDF](https://arxiv.org/pdf/2511.20085), [HTML](https://arxiv.org/abs/2511.20085)
### Authors
Chujie Wang,Zhiyuan Luo,Ruiqi Liu,Can Ran,Shenghua Fan,Xi Chen,Chu He
### Background
当前的遥感图像分析任务正在从传统的对象识别演变成复杂的智能推理，这对模型的推理能力和工具调用的灵活性提出了更高的要求。
### Innovation
提出了一种新的多模式代理框架——Vision-Interleaved Chain-of-Thought Framework (VICoT)，该框架通过动态将视觉工具插入推理链中，实现了明确的多轮推理。通过基于堆栈的推理结构和模块化的MCP兼容工具套件，VICoT使LLMs能够高效地执行多轮次、交织的图像-语言推理任务，同时具有很强的泛化能力。此外，还提出了推理堆栈蒸馏方法，以将复杂的代理行为迁移到小而轻的模型中，从而在显著减少复杂性的同时保持推理能力。
### Conclusion
在多个遥感基准测试上的实验表明，VICoT在推理透明度、执行效率和生成质量方面显著优于现有最先进的框架。
## 20. `cs.AI` - 从数据到概念通过布线图 [PDF](https://arxiv.org/pdf/2511.20138), [HTML](https://arxiv.org/abs/2511.20138)
### Authors
Jason Lo,Mohammadnima Jafari
### Background
布线图是一种带标记的有向图，用于表示如时间过程等抽象概念。本文介绍了一种准骨架布线图的概念，并证明了准骨架布线图图与哈斯图相对应。利用此结果，设计了一种从顺序数据中提取布线图的算法。
### Innovation
提出了一种准骨架布线图的概念，并通过将其与哈斯图关联起来，设计了一种从序列数据中提取布线图的算法。在一项对自主代理玩计算机游戏行为的分析中，该算法正确地识别了获胜策略，并且在扰动数据的情况下，算法性能优于两种基于标准聚类技术（DBSCAN 和 弦归聚类）的方法。
### Conclusion
本文将范畴理论、图论、聚类、强化学习和数据工程等技术结合起来，提供了一种从数据中发现和理解概念的新方法。
## 21. `cs.AI` - 为选择性多模态大型语言模型去学习正直记忆遗忘 [PDF](https://arxiv.org/pdf/2511.20196), [HTML](https://arxiv.org/abs/2511.20196)
### Authors
Zhen Zeng,Leijiang Gu,Zhangling Duan,Feng Li,Zenglin Shi,Cees G. M. Snoek,Meng Wang
### Background
多模态大型语言模型（MLLMs）具有显著的能力，但可能无意中记忆了隐私敏感信息。现有的一些去学习方法可以移除这类知识，但往往导致模型的整体图像理解能力下降。
### Innovation
提出了一种称为Sculpted Memory Forgetting Adapter（SMFA）的方法，它限定遗忘特定的记忆区域，同时保留整体能力。SMFA首先对模型进行微调，以用拒绝替换敏感响应，生成一个记忆遗忘适配器，然后应用一种保留锚点引导的遮罩机制，以防止干扰无关知识和理解能力。此外，引入了S-MLLMUn Bench基准，第一个旨在同时评估敏感知识移除与通用视觉理解保留的方法。
### Conclusion
大量实验表明，与先前的方法相比，SMFA实现了精确且可控的去学习，同时保持了模型的基础图像理解能力。
## 22. `cs.AI` - 通过基于猜测的算法-系统协同设计降低LLM搜索代理的延迟 [PDF](https://arxiv.org/pdf/2511.20048), [HTML](https://arxiv.org/abs/2511.20048)
### Authors
Zixiao Huang,Wen Zeng,Tianyu Fu,Tengxuan Liu,Yizhou Sun,Ke Hong,Xinhao Yang,Chengchun Liu,Yan Li,Quanlu Zhang,Guohao Dai,Zhenhua Zhu,Yu Wang
### Background
基于大语言模型（LLM）的搜索代理表现出强大的性能，但它们面临严重的延迟问题，因为每个步骤都需要序列化的LLM推理和工具执行。传统预测验证猜测范式虽然可以打破串行执行，但其收益仍然有限，因为仍然保留了全部原始工作负载并增加了额外的推理开销。
### Innovation
本文提出了一种基于猜测的算法-系统协同设计框架——SPAgent，通过增强搜索代理中的猜测角色来减少延迟。SPAgent从算法层面引入了两阶段自适应猜测机制，该机制在安全情况下选择性地跳过验证。从系统层面来看，SPAgent采用两层调度器根据引擎负载来调控猜测请求，以确保猜测仍然有益。SPAgent在现实系统中进行了实现，并在广泛的实验设置中实现了端到端1.65倍的加速，同时保持了相同的或更高的准确度。这使得多步搜索代理的实用部署成为可能。
### Conclusion
SPAgent通过改进特别是猜测机制，显著减少了LLM搜索代理的延迟，同时保持了准确性。该设计框架为未来的搜索代理系统提供了新的优化思路。
## 23. `cs.AI` - Actionable and diverse counterfactual explanations incorporating domain knowledge and causal constraints [PDF](https://arxiv.org/pdf/2511.20236), [HTML](https://arxiv.org/abs/2511.20236)
### Authors
Szymon Bobek,Łukasz Bałec,Grzegorz J. Nalepa
### Background
现有的方法在生成对抗性解释（counterfactual explanations）时往往忽略了现实世界数据集中的复杂依赖关系，导致产生的修改不现实或不可行。此类解释旨在通过识别所需的最小更改来实现模型期望的结果，从而增强机器学习模型的可操作解释性。
### Innovation
本文提出了Diverse, Actionable, and kNowledge-Constrained Explanations（DANCE），这是一种新型的生成方法，通过结合特征依赖性和因果约束来确保对抗性解释的合理性和现实可行性。该方法学习线性和非线性的约束条件，确保对抗性解释的实际操作性和合理性，并通过保持与特征关系的一致性生成符合现实约束的解释。此外，该方法平衡了合理性、多样性和稀疏性，有效解决了现有算法的关键限制。
### Conclusion
该工作基于一个实际案例研究，即波兰最大的电子邮件营销公司Freshmail，并得到了一个联合R&D项目Sendguard的支持。通过在140个公共数据集上的广泛评估，本文展示了其生成有意义、领域相关的对抗性解释的能力，性能超越了其他现有方法。相关的源代码可以在我们提供的GitHub仓库中找到。
## 24. `cs.AI` - 从输入-输出查询逆向工程神经网络权重的数据增强技术 [PDF](https://arxiv.org/pdf/2511.20312), [HTML](https://arxiv.org/abs/2511.20312)
### Authors
Alexander Beiser,Flavio Martinelli,Wulfram Gerstner,Johanni Brea
### Background
给定足够的网络输入-输出样本，可以逆向工程网络权重。在教师-学生设置中，这意味着收集教师映射的数据集——查询教师，然后拟合学生来模仿这种映射。合理的查询应该是教师训练的数据集。但当前方法在教师参数多于训练数据时会失败，因为学生会过度拟合查询而不是调整自身参数以匹配教师。
### Innovation
本文探讨了数据增强技术来最佳地抽取教师网络的输入-输出映射，以从教师的隐藏层中引出丰富的表示。标准的数据增强技术如旋转、翻转和添加噪声几乎没有改善识别问题。设计了新的数据增强技术以更好地覆盖网络隐藏层的表示空间。通过新的增强技术，我们扩展了可恢复网络规模的范围，并展示了可以恢复参数数量达到训练数据点100倍以上的网络。
### Conclusion
通过新的数据增强技术，可以克服当前方法在教师参数多于训练数据点时的限制。这些技术使得可以恢复更大规模的网络权重，扩展了可逼近的网络规模范围，展示了其在逆向工程中的潜力和实用性。
## 25. `cs.AI` - CostNav：具有成本意识评估自主体导航基准 [PDF](https://arxiv.org/pdf/2511.20216), [HTML](https://arxiv.org/abs/2511.20216)
### Authors
Haebin Seong,Sungmin Kim,Minchan Kim,Yongjun Cho,Myunchul Joe,Suhwan Choi,Jaeyoon Jung,Jiyong Youn,Yoonshik Kim,Samwoo Seong,Yubeen Park,Youngjae Yu,Yunsung Lee
### Background
现有的导航基准主要关注任务的成功度量，而忽视了经济可行性的关键问题，这对于自主送货机器人商业部署至关重要。CostNav旨在通过全面的成本和收入分析来评估自主体，这种分析与实际的商业运作相一致。
### Innovation
CostNav是第一个定量揭示导航研究指标与商业可行性之间差距的工作。它通过引入全面的成本-收益分析模型，考虑了硬件、培训、能源、维护成本以及配送收入，并使用行业参数来模拟自主体的整个经济生命周期。模型考虑了行业数据源（如能源费率、配送服务定价）中的参数，通过缩小规模的模拟预测到实际的配送情景，结果显示基准实现43.0%的服务级别协议遵守率但不具备商业可行性。
### Conclusion
CostNav填补了导航研究与商业部署之间的差距，通过数据驱动的方式提供了不同导航模式在经济权衡方面的决策基础，并展示了基于学习的现场导航基准。
## 26. `cs.AI` - 基于LLMs的互动AI NPC技术报告：CPDC挑战2025 [PDF](https://arxiv.org/pdf/2511.20200), [HTML](https://arxiv.org/abs/2511.20200)
### Authors
Yitian Huang,Yuxuan Lei,Jianxun Lian,Hao Liao
### Background
文章背景描述了在Commonsense Persona-Grounded Dialogue Challenge (CPDC 2025)中的研究与竞赛。这是一个针对基于常识和个性引导对话的挑战赛，参与者需要开发能够理解上下文、利用工具和角色化的人工智能对话系统。
### Innovation
文章介绍了一种简单而有效的框架，它统一了GPU Track和API Track的改进。该方法包含两个关键组件。首先是Context Engineering，它包括动态工具剪枝和个人剪辑以实现输入压缩，结合后处理技术，如参数归一化和函数合并。第二，GPU Track中采用了GRPO训练方法，直接用奖励信号优化强化学习，替代监督微调以避免小样本过拟合并显著提高任务导向对话的表现。
### Conclusion
最终评估结果显示，团队在Task 2 API上排名第1，在Task 1 API上排名第2，在Task 3 API和GPU Track上均排名第3，证明了该方法的有效性。该团队的代码已在公开平台发布。
## 27. `cs.AI` - NNGPT：用大型语言模型重新思考自动机器学习 [PDF](https://arxiv.org/pdf/2511.20333), [HTML](https://arxiv.org/abs/2511.20333)
### Authors
Roman Kochnev,Waleed Khalid,Tolgay Atinc Uzun,Xi Zhang,Yashkumar Sanjaybhai Dhameliya,Furui Qin,Chandini Vysyaraju,Raghuvir Duvvuri,Avi Goyal,Dmitry Ignatov,Radu Timofte
### Background
在AI领域，建设自我改进的AI系统仍然是一个基本挑战。本文介绍了一个名为NNGPT的开源框架，它能够将大型语言模型（LLM）转换为用于神经网络开发的自我改进型自动机器学习（AutoML）引擎，主要用于计算机视觉。NNGPT通过生成新的模型扩展神经网络数据集，并基于生成-评估-自我改进的闭环系统对LLM进行持续微调。
### Innovation
NNGPT通过整合五个协同的大模型底层管道，实现零样本架构合成、超参数优化（HPO）、代码意识精度/早期停止预测、范围受控PyTorch块检索增强合成（NN-RAG）以及强化学习。这些功能使得NNGPT能够从单一提示出发，验证网络架构、预处理代码和超参数，执行全链条任务，并从结果中学习。此外，NNGPT通过对LEMUR数据集的优化使各项功能更为高效，包括73%的执行率、三轮提示的准确性提升、基于哈希的重复数据删除、以及与基于搜索的AutoML性能相当的预测准确率。
### Conclusion
NNGPT已经生成了超过5000个验证过的模型，证明其作为自主AutoML引擎的有效性。一旦被接受，相关代码、提示和检查点将向公众开放，以促进可重复性和社区的应用。
## 28. `cs.AI` - VibraVerse：用于物理一致多模态学习的大规模几何-声学对齐数据集 [PDF](https://arxiv.org/pdf/2511.20422), [HTML](https://arxiv.org/abs/2511.20422)
### Authors
Bo Pang,Chenxi Xu,Jierui Ren,Guoping Wang,Sheng Li
### Background
了解物理世界需要基于物理定律的感知模型，而不是仅仅依赖统计相关性。现有的针对视觉和语言的多模态学习框架在物理一致性方面存在不足，并且没有充分重视物体几何结构、材料、振动模式与其产生的声音之间内在的因果关系。本文旨在构建一个能够明确建立从三维几何结构到物理属性，再到模态参数和声信号之间因果链的数据集。
### Innovation
本文提出了VibraVerse，这是一个大规模的几何-声学对齐数据集，能够明确地连接从三维几何结构到物理属性，再到模态参数和声信号之间的因果关系。该研究引入了一种对比学习框架CLASP，用于跨模态对齐，确保物理结构与声学响应之间的因果对应关系，从而实现物理上一致的跨模态对齐。在此基础上，本文还定义了一系列基准任务，包括几何到声波预测、声引导形状重建和跨模态特征学习。
### Conclusion
通过对VibraVerse进行广泛的验证，表明基于此数据集训练的模型在不同模态下表现出更高的准确率、可解释性和跨模态泛化能力。这表明VibraVerse是物理学一致且因果可解释的多模态学习基准，为声引导的物体感知提供了基础，加深了对物理世界的理解。该数据集也将会开源。
## 29. `cs.AI` - FRAGMENTA：基于碎片生成模型的端到端框架，结合代理调优进行药物先导优化 [PDF](https://arxiv.org/pdf/2511.20510), [HTML](https://arxiv.org/abs/2511.20510)
### Authors
Yuto Suzuki,Paul Awolade,Daniel V. LaBarbera,Farnoush Banaei-Kashani
### Background
药物发现中使用生成AI来生成分子至关重要，但现有的分类特定数据集通常包含少于100个训练样本。与基于原子的方法相比，基于片段的方法在处理少量数据时表现更好，但现有的启发式碎片化方法限制了多样性和错过了关键片段。此外，模型调整通常需要药化化学家和AI工程师之间的缓慢且间接的合作。针对这些问题，FRAGMENTA提出了一个端到端的药物先导优化框架。
### Innovation
1) 引入了一种新颖的生成模型，将碎片化重新定义为“词汇选择”问题，并使用动态Q-learning联合优化碎片化和生成。2) 设计了一个代理型的AI系统，通过与领域专家的对话反馈来优化目标。此系统将AI工程师从迭代调优过程中移除，并逐步学习领域知识，以自动完成调优过程。
### Conclusion
在实际的癌症药物发现实验中，FRAGMENTA的代理-人类配置方案识别的高评分分子数量几乎是基准值的两倍。此外，完全自主的代理-代理系统在传统的人类-人类调优中表现出色，证明了代理调优的有效性，能够捕捉专家意图并自动优化过程。
## 30. `cs.AI` - 从基本原理探讨离散状态空间中的主动推理 [PDF](https://arxiv.org/pdf/2511.20321), [HTML](https://arxiv.org/abs/2511.20321)
### Authors
Patrick Kenny
### Background
本文旨在澄清“主动推理”的概念，将它与“自由能原则”区分开来。研究显示，为了在离散状态空间中实现主动推理所必需的优化可以被表述为受限的差异最小化问题，并可以通过标准的均字段方法解决，而无需使用预期自由能的概念。该文进一步探讨了提出的感知/动作差异准则在描述感知和动作时的行为，指出当用于描述感知时，该准则与变分自由能相吻合，而在描述动作时，它与预期自由能功能性存在差异，其中差异在于一个熵正则化项。
### Innovation
本文创新性地展示了如何在离散状态空间中实现主动推理的优化，将其表述为受限的差异最小化问题，并提出了一种感知/动作差异准则，该准则在用于感知时与变分自由能一致，而在用于动作时通过熵正则化项与预期自由能存在差异。
### Conclusion
本文讨论了通过基本原理来探讨离散状态空间中主动推理的实现方式，强调了感知/动作差异准则在不同情境下的表现形式及与自由能原则的关系，为未来的相关研究提供了新的视角和方法。
## 31. `cs.AI` - 评估大语言模型的表现：来自中国药师考试的见解 [PDF](https://arxiv.org/pdf/2511.20526), [HTML](https://arxiv.org/abs/2511.20526)
### Authors
Xinran Wang,Boran Zhu,Shujuan Zhou,Ziwen Long,Dehua Zhou,Shu Zhang
### Background
随着大型语言模型（LLMs）在数字健康教育和评估流程中的日益集成，它们在支持高风险、特定领域认证任务的能力仍需进一步探讨。在中国，药师执业考试作为标准化基准，用于评估药师的临床和理论能力。此研究旨在对比ChatGPT-4o和DeepSeek-R1在这项考试中的表现，并讨论这些表现差异对AI辅助形成性评价的意义。
### Innovation
本研究首次将大语言模型应用于药学专业知识的评估任务，通过大量的实际问题对比了两个模型的表现，发现了DeepSeek-R1在某些领域的显著优势。
### Conclusion
DeepSeek-R1在药师执业考试中的表现显示出与结构和语义需求的高度一致。这些发现表明，对于特定领域模型，在这一情境下需要进一步研究，同时强调在法律和伦理敏感的环境中需保持人类监督的必要性。
## 32. `cs.AI` - SMoG: Schema Matching on Graph [PDF](https://arxiv.org/pdf/2511.20285), [HTML](https://arxiv.org/abs/2511.20285)
### Authors
Mingyu Jeon,Jaeyoung Suh,Suwan Cho
### Background
数据整合中的模式匹配是一个关键任务，尤其是在医疗领域，各种电子健康记录（EHR）系统需要与标准模型如OMOP CDM对齐。虽然大型语言模型（LLMs）在模式匹配中表现出潜力，但它们容易产生幻觉且缺乏最新的领域知识。知识图谱（KGs）提供了一种解决方案，通过提供结构化和可验证的知识来解决问题。然而，现有的基于KG的LLM方法通常依赖于效率低下的多跳查询或存储密集型向量检索方法。
### Innovation
本文介绍了一种名为SMoG（基于图的模式匹配）的新框架，它通过迭代执行简单的1跳SPARQL查询来利用知识图谱增强模式匹配的解释性和可靠性，同时通过直接查询SPARQL端点显著减少了存储要求。这针对现有方法的复杂性和存储密集性进行了改进，是一项创新。
### Conclusion
在现实世界医疗数据集上的实验结果表明，SMoG在性能上与最先进的基线相当，验证了其在基于知识图谱的模式匹配中的有效性和效率。
## 33. `cs.AI` - 从零构建轨迹基础模型 [PDF](https://arxiv.org/pdf/2511.20610), [HTML](https://arxiv.org/abs/2511.20610)
### Authors
Gaspard Merten,Mahmoud Sakr,Gilles Dejaegere
### Background
基础模型在人工智能领域具有革新性，但它们的构建方式，尤其是基于移动轨迹的构建方法尚未明确记载。本文通过演示从GPT-2开始构建偏重轨迹的基础模型的过程，填补了这一空白。
### Innovation
本文展示了将GPT-2适应时空数据的步骤和代码实现过程，同时对比了代表性的轨迹基础模型（如TrajFM和TrajGPT）的架构创新之处，并引入了相关领域的互补技术（如TimesFM的补丁方法）。
### Conclusion
本文旨在为研究人员和实践者解释基础模型的概念和术语，并在实施层面提供具体指导，以支持SIGSPATIAL社区在移动AI领域构建和评估基础模型，增强研究清晰度和同行评审效果。
## 34. `cs.AI` - 通过BREW提升语言代理 [PDF](https://arxiv.org/pdf/2511.20297), [HTML](https://arxiv.org/abs/2511.20297)
### Authors
Shashank Kirtania,Param Biyani,Priyanshu Gupta,Yasharth Bajpai,Roshni Iyer,Sumit Gulwani,Gustavo Soares
### Background
大规模语言模型（LLM）基于的代理在需要结构化推理、工具使用和环境适应的任务中越来越普遍，如数据操作、多步骤规划和计算机使用自动化。然而，尽管具备广泛的适用性，当前的模型权重优化方法（例如PPO和GRPO）在卷积过程中存在较高的计算开销，导致难以解释、适应或逐步改进的代理策略。
### Innovation
我们研究了通过在代理的环境经历学习中创建和优化结构化记忆来替代代理优化的路径。我们提出了BREW框架，通过知识库构建和优化，为下游任务提供代理优化的方法。BREW引入了一种有效的记忆分段方法，以实现更高效的检索和优化。此外，BREW利用任务评估者和行为评估标准学习见解，并利用状态空间搜索确保自然语言噪声和非具体性中的鲁棒性。
### Conclusion
在OSWorld、$tau^2$Bench和SpreadsheetBench等现实世界、领域导向的基准测试中，BREW在任务精度上提高了10-20%，在API/工具调用上减少了10-15%，从而实现了更快的执行时间。同时，BREW保留了与基础模型相同的计算效率。与先前将内存视为静态上下文的工作不同，我们确立了KB作为模块化和可控的代理优化基础体，为透明、可解释和可扩展的行为塑造提供一种明确的杠杆。
## 35. `cs.AI` - DRAFT-RL: 多代理链式草稿推理以增强强化学习的大型语言模型 [PDF](https://arxiv.org/pdf/2511.20468), [HTML](https://arxiv.org/abs/2511.20468)
### Authors
Yuanhao Li,Mingshan Liu,Hongbo Wang,Yiding Zhang,Yifei Ma,Wei Tan
### Background
大型语言模型（LLMs）已经在多步骤推理方面展示了令人印象深刻的能力。现有的多代理反思框架使用强化学习（RL）让多个LLM代理互相批评和改进彼此的输出，但这些方法通常依赖于单次响应，不足以探索推理过程中的结构性多样性。
### Innovation
本文提出了DRAFT-RL框架，将链式草稿（Chain-of-Drafts，CoD）推理整合到多代理RL训练中。每个代理对每个查询生成多个草稿，这些草稿由同伴代理和学习到的奖励模型进行评估，选出最具前景的路径。这些选定的草稿用于优化未来的推理策略。DRAFT-RL允许显式的多路径探索、同伴指导的反思和奖励对齐的选择，从而产生更稳健和可解释的LLM代理行为。
### Conclusion
我们在复杂的推理任务（包括代码合成、象征数学和知识密集型问答）上评估了该方法，结果显示DRAFT-RL在准确性和收敛速度方面均显著优于现有的反思和基于RL的代理。
## 36. `cs.AI` - Universe of Thoughts: 使用大规模语言模型启用创造性推理 [PDF](https://arxiv.org/pdf/2511.20471), [HTML](https://arxiv.org/abs/2511.20471)
### Authors
Yuto Suzuki,Farnoush Banaei-Kashani
### Background
基于大型语言模型（LLMs）的推理因其在数学和复杂逻辑任务中的出色表现而受到越来越多的关注。从Chain-of-Thought (CoT)提示技术开始，涌现出了许多分解问题为较小的、按顺序排列的步骤（或思考）的推理方法。然而，现有的推理模型主要关注常规问题解决，而不会生成通过创造性推理获得的创意解决方案。在药物发现或商业策略等领域，解决方案空间庞大且常规解决方法可能不够理想。因此，需要创造性推理以发现创新性解决方案消除这一差距。
### Innovation
本文介绍了一种基于已建立的认知科学原则的计算框架，提出了三种核心的创造性推理范式：组合性、探索性和转化性推理。同时，为了利用LLMs实现这些创新过程，提出了“思考宇宙”（UoT）方法。此外，还引入了三个需要创造性问题解决的新任务，并制定了一个评估基准，从可行性约束、实用性和新颖性三个方面来评估创造性。
### Conclusion
通过与当前最先进的（SOTA）推理技术以及具有推理能力的代表性商业模型进行比较分析，结果显示UoT在创造性推理方面表现出优越的性能。
## 37. `cs.AI` - 衡量高保真合成网络流量的隐私影响 [PDF](https://arxiv.org/pdf/2511.20497), [HTML](https://arxiv.org/abs/2511.20497)
### Authors
Van Tran,Shinan Liu,Tian Li,Nick Feamster
### Background
针对网络流量数据的稀缺性和隐私担忧，已经开发了多种生成模型以生成合成流量。然而，合成流量本身并不具备隐私保护特性，关于其泄露敏感信息的程度以及如何度量这种泄露，目前仍处于探索阶段。模型架构多样性进一步加剧了这一挑战，因为不同的模型架构会影响流量的表示和生成方式。
### Innovation
我们引入了一整套针对合成网络流量的隐私度量标准，结合了标准方法如成员身份推断攻击（MIA）和数据提取攻击，并结合了网络特定标识符和属性。使用这些度量标准，我们系统地评估了不同代表性生成模型的脆弱性，并检查了影响攻击成功的因素。我们的研究表明，不同模型和数据集之间的隐私风险存在显著差异。MIA成功率从0%到88%不等，且生成的流量中高达100%的网络标识符可以被恢复，这表明存在严重的隐私漏洞。我们还确定了显著影响攻击结果的关键因素，包括训练数据的多样性以及生成模型对训练数据的拟合程度。
### Conclusion
这些研究结果提供了设计和部署能够最小化隐私泄露的生成模型的实际指导，为生成更安全的合成网络流量奠定了基础。
## 38. `cs.AI` - PaTAS：使用主观逻辑在神经网络中进行并行信任传播的系统 [PDF](https://arxiv.org/pdf/2511.20586), [HTML](https://arxiv.org/abs/2511.20586)
### Authors
Koffi Ismael Ouattara,Ioannis Krontiris,Theo Dimitrakos,Dennis Eisermann,Frank Kargl
### Background
随着人工智能系统在关键安全应用中的部署，信任变得至关重要。传统评估指标如准确性和精确度无法捕捉不确定性或模型预测的可靠性，特别是在对抗性或降级条件下。因此，需要开发新的方法来评估模型的信任度。
### Innovation
本文引入了Parallel Trust Assessment System (PaTAS)，这是一种使用主观逻辑（SL）建模和传播神经网络信任的框架。PaTAS通过Trust Nodes和Trust Functions并行执行常规神经计算，从而在网络中传播输入、参数和激活的信任。PaTAS定义了一种参数信任更新机制，以在训练过程中细化参数可靠性，并提供了一种基于推理路径的信任评估方法（IPTA），以计算实例特定的信任度。实验结果表明，PaTAS能够生成可解释性强、对称且收敛的信任估计，这些估计能够补充准确率并揭示中毒、偏见或不确定数据场景中的可靠性差距。
### Conclusion
PaTAS通过在神经架构中使信任推理透明和量化，提供了一个评估模型在整个AI生命周期中的可靠性的原则性基础。
## 39. `cs.AI` - 超越生成：视觉语言模型的事实准确性多跳推理 [PDF](https://arxiv.org/pdf/2511.20531), [HTML](https://arxiv.org/abs/2511.20531)
### Authors
Shamima Hossain
### Background
视觉语言模型（VLMs）虽然功能强大，但常常产生事实不准确的输出，这是因为缺乏可靠的推理能力。虽然已经在大型语言模型（LLMs）中尝试了外部知识集成方法以增强推理能力，但在VLMs中的应用仍然不足，因为需要无缝地整合多种模态。现有研究未充分探索利用结构化知识图谱进行多跳验证的问题，特别是在图像字幕任务中。
### Innovation
本文提出了一种知识引导的VLMs推理框架，通过利用结构化知识图谱进行多跳验证，并利用图像字幕任务进行阐述。提出的方法可以系统地在多个步骤中进行推理，包括视觉实体识别、知识图谱遍历和基于事实的字幕细化。论文通过使用分层、三元组和项目符号形式的知识表示，评估了该框架在事实准确性与逻辑推理中的有效性。
### Conclusion
实验结果表明，本文提出的方法在经过初步实验的数据集上，提高了约31%的事实准确性，揭示了推理模式和失败模式的关键见解。该工作展示了利用外部知识提升VLMs推理能力的潜力，为更可靠和知识丰富的跨模态系统的开发铺平了道路。
## 40. `cs.AI` - 基于系统的方法构建通用智能电网模型 [PDF](https://arxiv.org/pdf/2511.19460), [HTML](https://arxiv.org/abs/2511.19460)
### Authors
Sofiane Ben Amor,Guillaume Guerard,Loup-Noé Levy
### Background
智能电网的技术进步提出了一类复杂的跨学科建模难题，传统计算方法难以解决。模拟智能电网需要采用系统化方法整合电力系统、能源市场、需求侧管理以及其他日益成为电力网主流组成部分的资源和资产。
### Innovation
该论文提出了一种智能电网的核心模型，用于测试电网的替代情景。此工具通过分布式子系统优化来模拟不同系统，验证假设，在保持灵活和可扩展的同时实现生产和消费调度。
### Conclusion
通过分布式优化子系统，该模型能够实现生产消费调度，并保持灵活性和可扩展性。这种方法能够更好地模拟智能电网的整体行为，为未来的研究和应用提供了强有力的支持。
## 41. `cs.AI` - SLMs在 premises 环境中的温度对事件分类影响 [PDF](https://arxiv.org/pdf/2511.19464), [HTML](https://arxiv.org/abs/2511.19464)
### Authors
Marcio Pohlmann,Alex Severo,Gefté Almeida,Diego Kreutz,Tiago Heinrich,Lourenço Pereira
### Background
安全操作中心（SOCs）和计算机安全 incident 响应团队（CSIRTs）面临自动化事件分类的巨大压力，但从云中调用大型语言模型（LLMs）带来了成本、延迟和隐私泄露的风险。因此，研究团队探讨了是否可以在本地执行这些任务。
### Innovation
研究团队分析了21种规模介于1B到20B参数间的模型，并针对不同的超参数执行温度进行了评测，结果显示，温度对表现影响较小，而参数数量和GPU能力是决定性因素。
### Conclusion
分析表明，虽然温度对性能影响不大，但更多的参数和更高的GPU容量能够显著提升模型在本地执行事件分类任务的效果。
## 42. `cs.AI` - 大型语言模型中的版权检测：负责任生成AI开发的道德方法 [PDF](https://arxiv.org/pdf/2511.20623), [HTML](https://arxiv.org/abs/2511.20623)
### Authors
David Szczecina,Senan Gaffori,Edmond Li
### Background
大型语言模型（LLMs）的广泛应用引发了对其训练数据中非法包含受版权保护内容的严重关切。现有检测框架，如DE-COP，计算密集且对独立创作者来说不太容易获取。随着法律审查的增加，需要一种可扩展、透明且用户友好的解决方案。
### Innovation
该论文介绍了一个开源的版权检测平台，允许内容创作者验证其作品是否被用于LLM训练数据集。该方法通过便于使用、改进相似性检测、优化数据集验证以及通过高效的API调用减少计算开销10-30%，提升了现有方法。该框架具有直观的用户界面和可扩展的后端，增加了人工智能开发的透明度和道德合规性，并促进了负责任的人工智能开发和版权保护的研究。
### Conclusion
该框架为增加AI开发的透明度和伦理合规性做出了贡献，为负责任的AI开发和版权保护奠定了基础，有助于进一步的研究。
## 43. `cs.AI` - BlockCert: Certified Blockwise Extraction of Transformer Mechanisms [PDF](https://arxiv.org/pdf/2511.17645), [HTML](https://arxiv.org/abs/2511.17645)
### Authors
Sandro Andric
### Background
该领域通常使用非正式证据和草率实验来评估机制可解释性和模型编辑，缺乏明确的保证来保证从原始模型到目标模型在相关输入上的偏离程度。
### Innovation
提出了BlockCert框架，用于安全地提取转换器机制，并提供可机器检查的证书来限制近似误差、记录覆盖率并哈希底层组件。还提出了一种基于Lipschitz的合成定理，并扩展了局部保证以推导全局偏移界。
### Conclusion
在GPT-2 small、TinyLlama-1.1B-Chat和Llama-3.2-3B模型上应用该框架，各区块覆盖率高，残差误差小。在TinyLlama场景中，全拼接模型在压力提示下达到了基础 perplexity 的0.00006以内。
## 44. `cs.AI` - SparOA：边缘DNN推理中的稀疏和操作感知混合调度 [PDF](https://arxiv.org/pdf/2511.19457), [HTML](https://arxiv.org/abs/2511.19457)
### Authors
Ziyang Zhang,Jie Liu,Luca Mottola
### Background
深度神经网络（DNN）模型对资源的需求提出了显著的性能挑战，尤其是在被部署在资源受限的边缘设备上时。现有解决方案如模型压缩往往牺牲了准确度，而专门的硬件成本高且灵活性差。尽管混合推理方法存在，但它们通常忽略了运算符特性对性能的影响。
### Innovation
SparOA 是一种用于边缘DNN推理的CPU-GPU混合推理框架，它通过利用稀疏性和计算强度来优化运算符调度，通过三个关键组件来解决上述挑战：（1）阈值预测器，准确确定最优稀疏性和计算强度阈值；（2）基于强化学习的调度器，根据实时硬件状态动态优化资源分配；（3）混合推理引擎，通过异步执行和批量大小增强效率。
### Conclusion
SparOA 在平均加速比上超越所有基线1.22-1.31倍，与仅使用CPU相比可提升50.7倍。此外，SparOA 在每推理的能效上实现了最优性能，消耗的能量比当前最佳共执行基线低7%-16%。
## 45. `cs.AI` - 用AI对抗AI：利用基础模型确保AI使能的安全关键系统 [PDF](https://arxiv.org/pdf/2511.20627), [HTML](https://arxiv.org/abs/2511.20627)
### Authors
Anastasia Mavridou,Divya Gopinath,Corina S. Păsăreanu
### Background
将AI组件，尤其是深度神经网络（DNNs）整合到航空和自动驾驶车辆等安全关键系统中，提出了基础性的保障挑战。AI系统中的不透明性与高层面要求和低层面网络表示之间的语义差距，使得传统的验证方法面临着巨大挑战。此外，长期存在的需求工程问题，如自然语言规范中的模糊性和形式化过程中的可扩展瓶颈，也加剧了这些问题。
### Innovation
作者提出了一种利用AI自身来应对这些挑战的方法，通过两个互补的组成部分。 REACT（需求工程中的AI一致性与测试）利用大语言模型（LLMs）在非形式化的自然语言要求与形式化规范之间建立桥梁，以便进行早期验证和验证。SemaLens（视觉感知的语义分析利用大规模多模态模型）利用视觉语言模型（VLMs）用人类易于理解的概念来推理、测试和监控基于DNN的感知系统。这些组件共同提供了一个从非正式要求到验证实现的全面管道。
### Conclusion
通过这种基于AI的方法，研究提供了一种新的途径，来确保AI使能的安全关键系统的可靠性，并通过新的工具和技术提高了系统的透明度和可验证性。
## 46. `cs.AI` - 个性化的奖励建模用于文本到图像生成 [PDF](https://arxiv.org/pdf/2511.19458), [HTML](https://arxiv.org/abs/2511.19458)
### Authors
Jeongeun Lee,Ryang Heo,Dongha Lee
### Background
最近的文本到图像(T2I)模型能够根据文本提示生成语义上一致的图像，然而，如何准确评估模型生成的图像与个人用户偏好之间的匹配度仍然是一个开放性挑战。传统的评估方法和通用的奖励函数或基于相似性的度量方法无法捕捉个人视觉品味的多样性和复杂性。
### Innovation
本文提出了个性化的奖励模型PIGReward，这是一种能够动态生成用户条件下的评估维度，并通过CoT推理评估图像的模型。PIGReward采用自我强化策略，在有限的参考数据上进行推理，以构建丰富的用户上下文，从而在无需用户特定训练的情况下实现个性化评估。此外，PIGReward还提供了个性化的反馈，这有助于用户特定的提示优化，从而提高生成图像与个体意图之间的对齐度。进一步介绍了PIGBench，一个针对不同用户偏好的评估基准，能够捕捉共享提示下的多样视觉解释。
### Conclusion
广泛的实验表明，PIGReward在准确性和可解释性方面都优于现有方法，确立了个性化T2I评估和优化的可扩展和基于推理的基础。我们的研究结果强调了PIGReward作为每个个体精确对齐的图像生成方案的稳健性。
## 47. `cs.AI` - 基于隐马尔可夫模型预测游客访问地点 [PDF](https://arxiv.org/pdf/2511.19465), [HTML](https://arxiv.org/abs/2511.19465)
### Authors
Theo Demessance,Chongke Bi,Sonia Djebali,Guillaume Guerard
### Background
随着社交媒体的流行，旅游行为分析变得越来越普遍。旅行者在旅行期间在这些网络上留下的数字痕迹有助于分析他们的行为。大量因游客喜欢分享旅行中的评论和照片而产生的数据使得可以建模和分析他们的旅行路线。预测游客的下一步行动对于了解需求并改进营销决策至关重要。
### Innovation
本文提出了一种基于社会网络数据分析的方法来理解并学习游客的行为以预测未来行动。该方法依赖于一种机器学习语法推理算法，并且文章的一个重要贡献在于将语法推理算法应用于大数据环境。
### Conclusion
本文选择法国首都巴黎展示了所提出方法的有效性。隐马尔科夫模型可以灵活地表示一组游客的行程，并且可以随着新数据的加入进行编辑。
## 48. `cs.AI` - 不完全的任何事物：克服SAM在3D医疗成像中的局限性 [PDF](https://arxiv.org/pdf/2511.19471), [HTML](https://arxiv.org/abs/2511.19471)
### Authors
Keith Moore
### Background
现有的基础分割模型如SAM和SAM-2在处理自然图像时表现良好，但在处理脑部MRI图像时遇到困难，因为脑部结构如杏仁核和丘脑缺乏清晰边界且对比度低。现有方法通常通过微调这些模型，例如MedSAM，来应对这些问题。本文提出了一种替代方法，将基础模型的输出作为额外的输入通道与MRI一起传递，以突出显示感兴趣区域。
### Innovation
该方法利用一种轻量级的3D U-Net生成SAM-2提示，并且这种方法避免了修改基础模型的权重，而是将基础模型与MRI输入结合使用，通过平滑基础模型的预测边缘来改善与MRI的对齐。此外，还测试了使用DINO注意图实现无提示分割。这种方法可以快速、标签高效且对于新的分布外扫描图像具有鲁棒性。
### Conclusion
该方法在基底节分割上的体积准确率达到了约96%，这足以支持对纵向体积变化的研究。这种方法对于研究与炎症相关的变化在急性发作的儿童强迫症中的变化特别有用。
## 49. `cs.AI` - PrefixGPT: Prefix Adder Optimization by a Generative Pre-trained Transformer [PDF](https://arxiv.org/pdf/2511.19472), [HTML](https://arxiv.org/abs/2511.19472)
### Authors
Ruogu Ding,Xin Ning,Ulf Schlichtmann,Weikang Qian
### Background
前缀加法器在计算密集型应用中广泛使用，因其高速度而受到重视。然而，设计优化的前缀加法器具有挑战性，因为有严格的设计规则和庞大的设计空间。
### Innovation
作者引入了PrefixGPT，这是一种生成式预训练变换器(GPT)，可以直接从零开始生成优化的前缀加法器。PrefixGPT具有一定制的仅解码器变换器架构，并采用合法性掩码在生成过程中确保每个设计的有效性。PrefixGPT通过预训练在一个随机合成的有效前缀加法器文集上学习设计规则，然后微调以在设计空间中导航以提高优化设计质量。与现有方法相比， PrefixGPT不仅发现了一个新的最优设计方案，提高了7.7%的面积延迟积(ADP)，还展现了更优秀的探索质量，平均降低ADP达79.1%。
### Conclusion
这表明GPT风格模型不仅能够掌握复杂的硬件设计原则，还能够应用于更加高效的硬件设计优化。
## 50. `cs.AI` - 任何模态下的任何目标跟踪与分割 [PDF](https://arxiv.org/pdf/2511.19475), [HTML](https://arxiv.org/abs/2511.19475)
### Authors
Tianlu Zhang,Qiang Zhang,Guiguang Ding,Jungong Han
### Background
跟踪和分割在视频理解中起着重要作用，提供对象在视频序列中的位置信息和时间关联。尽管有共同目标，但现有方法往往使用专门的架构或特定模态的参数来处理这些任务，这限制了其泛化能力和扩展性。近年来，尝试从任何模态输入或多任务推理的角度统一多个跟踪和分割子任务，但这些方法往往忽略了不同模态之间的分布差距和任务之间的特征表示差距，这些问题阻碍了有效的跨任务和跨模态知识共享，从而限制了真正通用模型的发展。
### Innovation
提出了一个名为SATA的通用跟踪和分割框架，能够统一各种跟踪和分割子任务，并支持任意模态输入。该框架通过Decoupled Mixture-of-Expert (DeMoE) 机制将统一的表示学习任务解耦为跨模态共享知识建模过程和特定信息建模过程，实现了模型的灵活性和泛化性能的增强。同时，引入了一个任务感知多对象跟踪（TaMOT）管道，以便在多任务训练中统一所有任务输出，从而减少特定任务知识的退化。
### Conclusion
SATA在18个具有挑战性的跟踪和分割基准测试中均表现出色，为更具泛化能力的视频理解提供了新的视角。
## 51. `cs.AI` - Pistachio:向合成、均衡和长格式视频异常基准迈进 [PDF](https://arxiv.org/pdf/2511.19474), [HTML](https://arxiv.org/abs/2511.19474)
### Authors
Jie Li,Hongyi Cai,Mingkang Dong,Muxin Pu,Shan You,Fei Wang,Tao Huang
### Background
现有的视频异常检测（VAD）基准缺乏足够的场景多样性、平衡的异常覆盖范围和时间复杂性，难以可靠地评估其在现实世界中的表现。而随着社区对视频异常理解（VAU）的需求增加，这要求更深层次的语义和因果推理，但由于需要大量的手动标注工作，因此很难进行基准测试。
### Innovation
Pistachio是一个全新的基于生成的VAD/VAU基准，通过控制生成管道实现了对场景、异常类型和时间叙事的精准控制，解决了互联网采集数据集中的偏见和局限性。它集成了一个场景条件下的异常分配、多步故事情节生成，以及一个时间上一致的长格式合成策略，能够生成长达41秒的一致视频，同时减少人工干预。
### Conclusion
广泛的实验表明Pistachio的规模、多样性和复杂性，揭示了现有方法的新挑战，推动了对动态和多事件异常理解的未来研究。
## 52. `cs.AI` - FAST: 重视拓扑结构的频域分布匹配方法用于核心集选择 [PDF](https://arxiv.org/pdf/2511.19476), [HTML](https://arxiv.org/abs/2511.19476)
### Authors
Jin Cui(1),Boran Zhao(2),Jiajun Xu(2),Jiaqi Guo(3),Shuo Guan(2),Pengju Ren(1) ((1) State Key Laboratory of Human-Machine Hybrid Augmented Intelligence, National Engineering Research Center for Visual Information and Applications, and Institute of Artificial Intelligence and Robotics, Xi'an Jiaotong University, (2) School of Software Engineering, Xi'an Jiaotong University, (3) School of Mathematical Sciences, Nankai University)
### Background
现有的核心集选择方法要么基于深度神经网络（DNN），这使得它们受特定模型参数限制并引入了架构偏差；要么不依赖于DNN，但这些方法依赖于缺乏理论保证的启发式方法。这两种方法都无法明确约束分布等效性，部分原因是连续分布匹配被认为不适用于离散采样。此外，常用的指标（如均方误差、KL散度、MMD、交叉熵）无法准确捕捉高阶矩差异，导致获取不到最优核心集。
### Innovation
FAST首次提出了一种不依赖于DNN的分布匹配核心集选择框架，将核心集选择任务构建成基于谱图理论的图约束优化问题，并采用了特征函数距离（CFD）在频域中捕捉全分布信息。为了解决CFD在中高频区的“消失相位梯度”问题，引入了衰减相位解耦特征函数距离（Attenuated Phase-Decoupled CFD）。此外，为了提高收敛性，设计了一种逐步频率选择的渐进差异感知采样策略，先保留全局结构再细化局部细节，从而以较少的频率实现准确匹配并避免过拟合。
### Conclusion
广泛的实验表明，FAST在所有评估基准上的平均准确率提高了9.12%，相比其他基线核心集方法，它将功耗降低了96.57%，实现了2.2倍的平均加速比，证明了其高性能和高能效。
## 53. `cs.AI` - 通过解开多模态表示来量化模态贡献 [PDF](https://arxiv.org/pdf/2511.19470), [HTML](https://arxiv.org/abs/2511.19470)
### Authors
Padegal Amit,Omkar Mahesh Kashyap,Namitha Rayasam,Nidhi Shekhar,Surabhi Narayan
### Background
目前，量化多模态模型中模态的贡献仍然是一个挑战，现有的方法未能明确地定义贡献的概念。之前的工作依赖于基于准确率的评估方法，将移除一个模态后的性能下降作为该模态影响力的表现，但这样的结果导向的度量标准无法区分一个模态是本身具有信息性，还是其价值仅来源于与其他模态的交互。在跨注意力架构中，这一点尤为重要，因为一个模态可以影响其他模态的表示。
### Innovation
本文提出了一个基于部分信息分解(PID)的框架，用于通过在内部嵌入中分解预测信息成独有的、冗余的和协同的部分来量化模态的贡献。为了实现大规模的仅推理的分析，开发了一个基于迭代比例拟合方法(IPFP)的算法来计算各层和数据集级别的贡献而无需重新训练。这一方法提供了模态间行为的原理性的、表示层次的视角，相比于结果导向的度量标准，它提供了更清晰和可解释的洞见。
### Conclusion
本文提供的基于PID的方法和基于IPFP的算法提供了一种新的视角来理解和评估多模态模型中不同模态的贡献，这种方法能够为模态间交互和信息分布提供更详细和清晰的理解。
## 54. `cs.AI` - WavefrontDiffusion：改进推理的动态解码调度 [PDF](https://arxiv.org/pdf/2511.19473), [HTML](https://arxiv.org/abs/2511.19473)
### Authors
Haojin Yang,Rui Hu,Zequn Sun,Rui Zhou,Yujun Cai,Yiwei Wang
### Background
扩散语言模型(DLMs)在文本生成方面显示出强大的潜力，逐渐成为自回归模型的有效替代者。常见的去噪策略包括标准扩散和块扩散。标准扩散通过全局去噪但不限制更新范围，往往导致不完整的语境完成和序列过早结束的预测。块扩散则按照预设顺序更新固定大小的块，但由于其刚性结构，可能会破坏连贯的语义单元并打断推理。
### Innovation
WavefrontDiffusion提出了一种动态解码方法，从已确定位置向外扩展活跃token形成的波前。这种方法适肩膀自然语义结构流动，同时保持与块为基础的方法计算成本相同。
### Conclusion
WavefrontDiffusion在四个推理和代码生成基准测试中取得了最先进的性能，同时还生产出更高质量的语义输出，展示了适应性调度对更连贯、更有效生成的值。
## 55. `cs.AI` - 构建具有韧性的信息生态系统：大型LLM生成的说服攻击数据集 [PDF](https://arxiv.org/pdf/2511.19488), [HTML](https://arxiv.org/abs/2511.19488)
### Authors
Hsien-Te Kao,Aleksey Panasyuk,Peter Bautista,William Dupree,Gabriel Ganberg,Jeffrey M. Beaubien,Laura Cassani,Svitlana Volkova
### Background
组织的沟通对于公众信任至关重要，但生成式AI模型的兴起通过快速大量地生成有力的内容，形成了与政府和商业组织官方信息竞争的叙述，迫使机构处于被动应对的态势，难以维持沟通的有效性。
### Innovation
介绍了由GPT-4、Gemma 2和Llama 3.1生成的大型AI说服攻击数据集，包含134,136条攻击，针对十个机构的972篇新闻稿使用了23种说服技巧。分析了这些说服攻击的道德共鸣，以便了解攻击向量。不同模型生成的攻击主要集中在不同的说服技巧上，为组织建立声誉盔甲提供了基础，促进了信息生态系统中更有效和更具弹性的沟通的发展。
### Conclusion
通过分析这些模型生成的说服攻击，可以实现主动防御，确保组织能够建立起信誉堡垒，并推动信息生态系统中更有效和更具有韧性沟通的发展。
## 56. `cs.AI` - SG-OIF: 一种基于稳定性的在线影响框架以实现可靠的视觉数据 [PDF](https://arxiv.org/pdf/2511.19466), [HTML](https://arxiv.org/abs/2511.19466)
### Authors
Penghao Rao,Runmin Jiang,Min Xu
### Background
在将深度学习视觉模型部署到实际应用中时，需准确评估每个训练点对测试预测的影响，这对于识别噪声数据至关重要。尽管影响函数可以归因于个别训练样本权重轻微调整或移除如何影响模型输出，但在深度学习视觉模型中的实现仍然是具有挑战性的。逆曲率计算昂贵，而训练非稳健性使得静态近似失效。现有的方法使用迭代求解器和低秩代用品来减少成本，但离线计算无法跟上训练的动态变化，而缺少信心校准会导致脆弱的排名，错误地识别关键示例。
### Innovation
提出了一种名为Stability-Guided Online Influence Framework (SG-OIF)的新框架。该框架将算法稳定性视为实时控制器，包括：(i) 通过随机Richardson和预条件Neumann维护轻量级锚点IHVPs；(ii) 模块化曲率后端以根据稳定性引导的残差阈值、异常门控和信心对每个示例的影响评分进行调节。实验结果显示，该框架在不同数据集和不同类型噪声下的性能达到了SOTA，特别是在CIFAR-10和MNIST数据集上的表现尤其突出。
### Conclusion
SG-OIF是一种实用的控制器，可以实现在线影响估计，通过稳定性引导实现了准确的噪声数据识别和异常检测。
## 57. `cs.AI` - 使用有限人类数据高效推断的大语言模型：微调然后校正 [PDF](https://arxiv.org/pdf/2511.19486), [HTML](https://arxiv.org/abs/2511.19486)
### Authors
Lei Wang,Zikun Ye,Jinglong Zhao
### Background
近年来，人工智能（AI）取得了重大进展，大量研究展示了使用大规模语言模型（LLMs）在市场研究和社会科学研究中生成接近人类反应的潜力。有两种主要方法可以改进LLMs的性能：微调，使LLMs的预测更接近人类响应；校正，修正LLMs输出中的偏差。本文基于这一背景撰写。
### Innovation
本文开发了一种框架，将微调和校正相结合，并在两个阶段之间优化分配有限的标记样本。不同于传统的最小化均方预测误差的目标，本文提出了最小化预测误差的方差作为微调目标，从而优化下游校正阶段。此外，本文利用经验标度定律开发了一种数据驱动方法，以在微调和校正阶段之间优化分配样本。实验验证了本文框架，表明这种双重方法比单独使用微调或校正提供了更好的估计和推理性能。
### Conclusion
本文的框架通过结合微调和校正，有效利用有限的人类数据提高了大语言模型的性能。实验结果验证了该框架的有效性，相对于单独使用微调或校正，该方法在估计和推理性能上均有提升。
## 58. `cs.AI` - 无需Oracle的进化：用LLM评判驱动有效进化 [PDF](https://arxiv.org/pdf/2511.19489), [HTML](https://arxiv.org/abs/2511.19489)
### Authors
Zhe Zhao,Yuheng Yang,Haibin Wen,Xiaojie Qiu,Zaixi Zhang,Qingfu Zhang
### Background
大语言模型（LLMs）与进化计算（EC）的整合为科学发现开辟了新领域，但仍受限于对“Oracle”的依赖——即客观、机器可计算的适应度函数。
### Innovation
本文通过引入MADE（多代理分解进化）框架打破了这一限制。MADE通过“问题规定”的方式化解主观评估的固有噪音，将模糊指令分解为可验证的子要求，从而将高变异性LLM反馈转化为稳定的、精确的选择压力。这一方法在多种复杂基准测试中展现了显著优越性，尤其是在软件需求满意度方面，MADE的表现优于强基线50%以上，在复杂指令遵循方面达到95%的完美通过率。
### Conclusion
该研究验证了从优化可计算指标转向描述性品质这一根本范式的转变，从而开拓了进化的优化在没有真实基准的广阔开放领域的新途径。
## 59. `cs.AI` - Z-Space: 企业级LLM自动化的多智能体工具管弦乐框架 [PDF](https://arxiv.org/pdf/2511.19483), [HTML](https://arxiv.org/abs/2511.19483)
### Authors
Qingsong He,Jing Nan,Jiayu Jiao,Liangjie Tang,Xiaodong Xu,Mengmeng Sun,Qingyao Wang,Minghui Yan
### Background
大型语言模型通过Model Context Protocol框架内部调用外部工具来突破知识和时效限制，实现复杂任务的自动化执行。然而，随着企业级MCP服务的快速增长，高效且准确匹配数千种异构工具的目标功能已成为限制系统实用性的核心挑战。现有方法通常依赖全提示注入或静态语义检索，面临用户查询和工具描述间的语义不连贯、LLM输入上下文充盈和高推理延迟的问题。
### Innovation
本文提出了一种名为Z-Space的数据生成导向的多智能体协同工具调用框架。Z-Space框架通过（1）通过意图解析模型实现用户查询的结构化语义理解；（2）基于融合子空间加权算法的工具过滤模块（FSWW），实现了意图和工具间的细粒度语义对齐，无需调节参数；（3）构建推理执行代理，支持多步骤任务的动态规划和容错执行等创新。
### Conclusion
该框架已在美团平台的技术部门部署，涵盖多个业务单元，如妥投、高德和盒马，展示了显著提高智能测试数据生成系统的效率和可靠性的能力。系统平均减少工具推理消耗的词汇量达96.26%，工具调用的准确率提升到92%。
## 60. `cs.AI` - 在计算进度放缓情况下预测AI时间范围 [PDF](https://arxiv.org/pdf/2511.19492), [HTML](https://arxiv.org/abs/2511.19492)
### Authors
Parker Whitfill,Ben Snodin,Joel Becker
### Background
从2019年起，METR的时间范围度量指标已呈指数级增长，同时伴随着计算能力的增长。然而，尚不清楚计算能力是否会在2030年前保持当前的增长速度，这引发了对于计算能力可能放缓如何影响AI代理能力预测的疑问。
### Innovation
作者提出了一个将时间范围作为训练计算能力和算法的函数的模型，并结合了计算投资如何影响算法进步的模型（值得注意的是，这排除了软件单独引发奇点的可能性）。此外，基于2019年至2025年时间范围和计算能力以恒定速率增长的实证事实，作者推导出时间范围的增长必须与计算能力增长成比例。作者还提供了与该理论一致的额外实验证据。利用这一模型，在OpenAI的计算预测下，作者预测了时间范围的增长趋势，发现在某些情况下，在计算能力放缓的情况下，时间范围的增长存在显著的延期现象。
### Conclusion
作者的分析结果表明，在计算能力放缓的情况下，AI代理的能力预测可能会出现延迟，特别是在计算资源增长预期出现改变的可能情景下。
## 61. `cs.AI` - 人类专家对生成式AI在全球南方情境化STEAM教育中的评估 [PDF](https://arxiv.org/pdf/2511.19482), [HTML](https://arxiv.org/abs/2511.19482)
### Authors
Matthew Nyaaba,Macharious Nabang,Patrick Kyeremeh,Ibrahim Nantomah,Collins Owusu-Fordjour,Martin Ako,Bismark Nyaaba Akanzire,Kassim Korah Nantom,Cecilia Issaka,Xiaoming Zhai
### Background
本研究探讨了人类专家如何评估生成式AI（GenAI）能力，以在全球南方背景下情境化STEAM教育，特别关注加纳的情况。研究采用综合混合方法设计，四位STEAM专家评估了通过定制的文化回应式课程规划器（CRLP）生成的教学计划，并将其与加纳国家课程和评估委员会（NaCCA）的标准教学计划进行了对比。研究通过一个验证过的包含25项指标的文化回应式教学评鉴表，对教学计划进行了量化评价，指标包括偏见意识、文化代表、情境相关性、语言响应性和教师代理。定量结果与定性反思相结合，揭示了生成式AI如何处理文化与教学的适切性。
### Innovation
本研究创新地采用了综合混合方法设计，通过定量评价和定性反思相结合的方式，评估生成式AI在加纳情境化STEAM教育中的表现。研究还发现了生成式AI在处理文化多样性和历史文化方面存在的局限，尤其在数学和计算机课程中表现不佳，这在某种程度上说明了需要进一步的技术改进和教育实践。
### Conclusion
生成式AI与CRLP工具结合使用时，能够在STEAM教学中有效连接抽象的课程标准与学习者的文化知识、社区实践和日常生活经验，使其更具文化根基和教学响应性。然而，生成式AI在反映加纳的文化多样性方面表现不佳，通常仅提供语言、历史和身份的表面性参考，特别是在数学和计算机课程中文化细微差别的展示更为有限。研究结果强调了持续教师中介、社区参与以及文化契合AI输出改良在发展中国家情境中的重要性。未来的研究应包括课堂实验、专家参与范围的扩大以及模型微调至土著语言语料库，以增强文化趋同性。
## 62. `cs.AI` - 利用专家进行未经授权压缩：MoE-LLMs中的专家利用 [PDF](https://arxiv.org/pdf/2511.19480), [HTML](https://arxiv.org/abs/2511.19480)
### Authors
Pinaki Prasad Guha Neogi,Ahmad Mohammadshirazi,Dheeraj Kulshrestha,Rajiv Ramnath
### Background
混合专家（MoE）架构在大规模语言模型（LLMs）中越来越受欢迎，主要是因为它们的高效和可扩展性。然而，MoE的模块化结构也引入了一个独特的漏洞：攻击者可以通过修剪专家并廉价微调余下的部分来压缩或重新利用这些模型，从而绕过许可和安全限制。
### Innovation
本文系统性地研究了在特定任务使用下MoE-LLMs的可修剪性。首先开发了一种专家归属框架，识别最负责特定任务的专家子集，然后评估微调和重新校准这些专家带来的性能权衡。研究发现存在关键的知识损失——恢复权衡：虽然某些专家可以被隔离以保留任务精度，但如果没有有针对性的重新校准，会带来显著的下降。基于这一分析，提出了一种旨在使MoE模型在未经授权的情况下更难以压缩和微调的防御策略，包括嵌套专家训练和选择性微调协议，这些协议可以抵抗未经授权的适应。
### Conclusion
通过将专家修剪视为威胁向量和防御目标，本文揭示了MoE模块化利用的双重性质，并提供了首个针对MoE-LLMs安全专业化进行系统性评估的框架。
## 63. `cs.AI` - Xmodel-2.5: 1.3B Data-Efficient Reasoning SLM [PDF](https://arxiv.org/pdf/2511.19496), [HTML](https://arxiv.org/abs/2511.19496)
### Authors
Yang Liu,Xiaolong Zhong,Ling Jiang
### Background
大型语言模型在推理和工具使用方面表现出色，但由于计算需求高，不适合边缘或成本敏感的部署。
### Innovation
1. 提出了Xmodel-2.5，这是一种1.3亿参数的小型语言模型，作为可替换的核心代理。2. 使用最大更新参数化训练方法（μP），使得超参数能够在不同规模的模型中直接转移，即使在参数共享的情况下也能适用。3. 使用了一个1.4万亿词的温升-稳定-衰减课程表。4. 在衰减阶段从AdamW切换到Muon，提高了13项任务的推理性能平均值4.58%，验证了早期的AdamW稳定性和后期的Muon精细调整可以结合起来提高下游性能。5. 采用混合精度训练（FP8），平衡了准确性和吞吐量。
### Conclusion
所有检查点、食谱和评估代码均在Apache-2.0许可证下发布。训练代码和评估框架也提供给公众使用。
## 64. `cs.AI` - PeriodNet: 提升时间序列预测中注意力机制的潜力 [PDF](https://arxiv.org/pdf/2511.19497), [HTML](https://arxiv.org/abs/2511.19497)
### Authors
Bowen Zhao,Huanlai Xing,Zhiwen Xiao,Jincheng Peng,Li Feng,Xinhan Wang,Rong Qu,Hui Li
### Background
注意机制在序列建模中展现了显著潜力，尤其是在自然语言处理（NLP）中的应用，如BERT和GPT模型，但其在时间序列预测（TSF）中的应用还未充分发挥潜力。探索适用于TSF的新型注意网络结构具有重要意义。
### Innovation
论文提出了一种新的网络结构——PeriodNet，它包含周期注意和稀疏周期注意机制，用于分析相邻周期；引入了迭代分组机制减少跨变量冗余；设计了全新的Transformer架构并提出周期扩散器以实现精确多周期预测。
### Conclusion
实验结果表明，PeriodNet在单变量和多变量时间序列预测中均优于六个最先进的模型，在均方误差和平均绝对误差上表现更佳，特别是在长度为720的时间序列预测中相比传统编码器-解码器Transformer架构模型的相对改进达到了22%。
## 65. `cs.AI` - 使用不完美且隐私敏感的医疗数据进行生物医学和医疗保健智能的层次化双策略遗忘 [PDF](https://arxiv.org/pdf/2511.19498), [HTML](https://arxiv.org/abs/2511.19498)
### Authors
Yi Zhang,Tianxiang Xu,Zijian Li,Chao Zhang,Kunyu Zhang,Zhan Gao,Meinuo Li,Xiaohan Zhang,Qichao Qi,Bing Chen
### Background
大规模语言模型（LLMs）表现出色，但在处理涉及不完美或隐私敏感患者信息的医疗数据时，会面临隐私风险，主要是因为训练数据的记忆问题。本文探讨了如何在保留基本医疗技能的同时，精确移除专门知识，以解决这一挑战。
### Innovation
本文提出了一个分层的双策略框架，用于选择性知识遗忘，该框架能够精准移除专门知识而不破坏核心医学技能。这一方法通过几何约束梯度更新和概念感知的标记级干预相结合，实现了一个统一的四级医学概念层次，从而选择性地调整目标参数。实验表明，该方法在MedMCQA（外科）和MHQA（焦虑、抑郁、创伤）数据集上表现出卓越性能，实现82.7%的知识遗忘率和88.5%的知识保留率。
### Conclusion
本文的方法不仅在性能上优于现有方法，还能保持强大的隐私保障，仅需修改0.1%的参数，解决了临床研究中的监管合规性、可审核性和道德标准问题。
## 66. `cs.AI` - 大型语言模型压缩排序的系统研究 [PDF](https://arxiv.org/pdf/2511.19495), [HTML](https://arxiv.org/abs/2511.19495)
### Authors
Shivansh Chhawri,Rahul Mahadik,Suparna Rooj
### Background
大型语言模型（LLMs）需要大量的计算资源，对于在计算资源受限的环境中高效部署而言，模型压缩是必不可少的。现有的主导压缩技术包括知识蒸馏、结构化剪枝和低比特量化，虽然在独立应用时的效果已经很明确，但对于这些技术如何结合使用以及最优的顺序依然不清楚。本研究对Qwen2.5 3B模型应用了这些技术，系统地评估了它们在单独使用和组合使用时的效果。
### Innovation
研究系统地分析了在单独和组合使用情况下，知识蒸馏（KD）、结构化剪枝（P）和低比特量化（Q）这三种压缩技术对Qwen2.5 3B模型的影响，并得出了最佳的顺序为剪枝、知识蒸馏、量化（P-KD-Q），在压缩比达到3.68倍的同时仍能保持很强的指令执行能力和语言理解能力。同时强调早期应用低比特量化会导致不可逆的信息损失，从而影响后续训练的效果。
### Conclusion
该研究提供了一种在计算资源受限环境下部署LLMs的有效压缩管道设计实用见解，即应首先进行剪枝，其次是知识蒸馏，最后是低比特量化（P-KD-Q）来优化压缩和保持模型性能。
## 67. `cs.AI` - 生成模型辅助连续学习在FDD mMIMO-OFDM系统中CSI反馈中的应用 [PDF](https://arxiv.org/pdf/2511.19490), [HTML](https://arxiv.org/abs/2511.19490)
### Authors
Guijun Liu,Yuwen Cao,Tomoaki Ohtsuki,Jiguang He,Shahid Mumtaz
### Background
现有深度自编码器（DAE）框架已经在大规模多输入多输出（mMIMO）正交频分复用（OFDM）系统中展示了降低信道状态信息（CSI）反馈开销的效果。然而，传统的CSI反馈模型难以适应由用户移动引起的动力学环境变化，遇到新的CSI分布时需要重新训练，这会导致在返回到已遇到的环境中时性能下降，出现灾难性遗忘。
### Innovation
本文提出了一种基于生成对抗网络（GAN）的CSI反馈连续学习方法，通过使用GAN生成器作为记忆单元，该方法能够在保持对过去环境知识的同时，确保在各种场景下持续高性能，同时避免遗忘。
### Conclusion
仿真结果表明，所提出的方法增强了DAE框架的泛化能力，保持了低的内存开销。此外，它还能够无缝集成到其他先进的CSI反馈模型中，显示出其 robustness 和适应性。
## 68. `cs.AI` - CycleChemist:一种双管齐下的机器学习框架，用于有机光伏材料发现 [PDF](https://arxiv.org/pdf/2511.19500), [HTML](https://arxiv.org/abs/2511.19500)
### Authors
Hou Hei Lam,Jiangjie Qiu,Xiuyuan Hu,Wentao Li,Fankun Zeng,Siwei Fu,Hao Zhang,Xiaonan Wang
### Background
有机光伏（OPV）材料提供了一条有希望的可持续能源生成路径，但其开发受到识别高效率供体和受体对的难度限制，现有的设计策略通常只专注于供体或受体之一，而缺乏能够同时建模两者的统一方法。
### Innovation
本文介绍了一种双机器学习框架，用于有机光伏发现，该框架结合了预测建模和生成分子设计，使用了Organic Photovoltaic Donor Acceptor Dataset（OPV2D）数据集，该数据集包含2000个实验表征的供体和受体对，并开发了有机光伏分类器（OPVC）来预测材料是否表现出光伏行为，同时引入了循环材料生成预训练变换器（MatGPT），该模型能够生成合成上可行的有机半导体，并具有基于强化学习策略的三层目标策略优化。
### Conclusion
通过将分子表示学习与性能预测相结合，该框架推动了数据驱动的高效率OPV材料发现。
## 69. `cs.AI` - Discover, Learn, and Reinforce: 使用多样化RL生成轨迹扩展Vision-Language-Action预训练 [PDF](https://arxiv.org/pdf/2511.19528), [HTML](https://arxiv.org/abs/2511.19528)
### Authors
Rushuai Yang,Zhiyuan Feng,Tianxiang Zhang,Kaixin Wang,Chuheng Zhang,Li Zhao,Xiu Su,Yi Chen,Jiang Bian
### Background
视觉-语言-动作（VLA）模型的预训练需要大量多样且高质量的执行轨迹。现有的大多数数据通过人工远程操作获得，成本高且难以大规模扩展。强化学习（RL）方法通过自主探索学习有用技能，是生成数据的可行方法。然而，标准的RL训练容易陷入狭窄的执行模式，限制了其在大规模预训练中的应用。
### Innovation
我们提出了Discover, Learn and Reinforce (DLR)信息论模式发现框架，用于生成多种不同的、高成功率的行为模式，以支持VLA的预训练。与标准RL方法相比，DLR能够在同一任务中学习多种高成功率策略，覆盖更广泛的状态-动作空间，并且在未见过的下游任务中展现出更好的性能。
### Conclusion
多模式RL数据生成方法在生成多样化轨迹和改善模型性能方面具有积极的数据扩展特性，使其成为扩展VLA预训练的有效数据引擎。
## 70. `cs.AI` - AttackPilot：基于LLM代理的面向ML服务的自主推理攻击 [PDF](https://arxiv.org/pdf/2511.19536), [HTML](https://arxiv.org/abs/2511.19536)
### Authors
Yixin Wu,Rui Wen,Chi Cui,Michael Backes,Yang Zhang
### Background
推理攻击已经得到了广泛研究，并提供了ML服务系统的系统性风险评估方法；然而，这些攻击的实施及其为最优估计所需的攻击参数对于非专家来说仍然是具有挑战性的。高级大型语言模型的出现为开发自主代理作为推理攻击专家提供了有前景但未充分利用的机会，从而有助于解决这一挑战。
### Innovation
提出了一个名为AttackPilot的自主代理，该代理能够在没有人类干预的情况下独立进行推理攻击。该代理使用GPT-4o展示了百%的任务完成率，并且具有接近专家级别的攻击性能，平均每运行一次的成本仅为$0.627，还可以使用其他代表性LLM并根据服务限制自适应优化其策略。此外，通过对代理运行的跟踪分析，证明了诸如多代理框架和任务特定操作空间的设计选择，有效地避免了诸如糟糕的计划、无法遵循指令、任务上下文丢失和幻觉等问题。
### Conclusion
预计这样的代理能够赋能非专家ML服务提供商、审计师或监管者系统地评估ML服务的风险，而无需深谙领域知识。
## 71. `cs.AI` - 基于差分进化的数据流稀疏特征选择 [PDF](https://arxiv.org/pdf/2511.19555), [HTML](https://arxiv.org/abs/2511.19555)
### Authors
Ruiyang Xu
### Background
高维流数据的处理通常使用在线流特征选择（OSFS）技术，但实际实现常常由于设备故障和技术限制面临数据不完整的问题。现有的基于潜在因素分析的在线稀疏流特征选择（OS2FS）方法虽然解决了该问题，但在特征评估方面仍存在显著局限性，导致性能下降。
### Innovation
该论文提出了一种新的在线差分进化稀疏特征选择方法（ODESFS），通过结合（1）使用潜在因素分析模型进行缺失值填充，和（2）基于差分进化的特征重要性评估来克服现有方法的局限性。
### Conclusion
在包含六个真实数据集的全面实验中，ODESFS 方法在特征子集选择和准确性方面均优于最新的 OSFS 和 OS2FS 方法。
## 72. `cs.AI` - 当神经数据可以影响福利判断？ neuroeconomics在政策使用中的批判性框架 [PDF](https://arxiv.org/pdf/2511.19548), [HTML](https://arxiv.org/abs/2511.19548)
### Authors
Yiven(Louis)Zhu
### Background
神经经济学旨在根据神经和计算证据来分析人们对结果的评估、经验和自律行为，与此同时，政策制定者和商业从业者越来越多地利用神经数据来支持的行为主义监管、基于脑的干预措施以及新的福利指标的做法，引起了争议。本文探讨神经数据在政策福利评价中的合法条件，而非仅仅描述行为。
### Innovation
本文开发了一个非经验性、基于模型的框架，该框架将神经信号、计算决策模型和规范性福利标准链接起来。通过定义一个行为-批评增强学习模型中的推理路径，即从神经活动推导到隐含价值和预测错误再到福利声明。并表明只有在神经-计算映射得到充分验证、决策模型能够识别真实的利益而非上下文依赖的错误以及明确说明并防御福利标准的情况下，神经证据才能限制福利判断。最后，提出了针对监管者和神经AI系统设计师的神经经济福利推理清单。
### Conclusion
本文还展示了大脑和人工代理都是价值学习系统，并指出无论是生物的还是人工的内部奖励信号，都是计算量，需要显式的规范性模型来作为福利衡量的标准。
## 73. `cs.AI` - 基于信息论的自适应结构剪枝以实现高效视觉语言模型 [PDF](https://arxiv.org/pdf/2511.19518), [HTML](https://arxiv.org/abs/2511.19518)
### Authors
Zhaoqi Xu,Yingying Zhang,Jian Li,Jianwei Guo,Qiannan Zhu,Hua Huang
### Background
近年来，视觉语言模型(VLMs)在多模态任务中取得了显著的性能，但其不断增长的规模带来了部署和效率上的重大挑战。现有的压缩方法通常依赖于启发式的重要性度量或经验性的剪枝规则，缺乏关于信息保留的理论保证。现有的剪枝方法在信息保留上缺少理论支持。
### Innovation
本文提出了基于信息论的自适应结构剪枝框架InfoPrune，通过信息瓶颈原理将剪枝问题从保留任务相关的语义和排除冗余的依赖之间进行权衡。InfoPrune通过引入基于熵的有效秩(eRank)和Kolmogorov-Smirnov (KS) 距离来计算每个注意头的贡献，并提出了两种互补的方案：基于训练的信息损失目标引导头部剪枝以及通过自适应低秩近似进行训练无介入的FFN压缩。广泛的实验表明，InfoPrune在VQAv2，TextVQA和GQA数据集上实现了高达3.2倍的FLOP减少和1.8倍的速度提升，同时保持了近似无关紧要的性能下降。
### Conclusion
本研究提供了一种能够理论上保证信息保留并实际有效的框架，为多模态大模型的高效部署奠定了基础。
## 74. `cs.AI` - 基于信任的社会学习 (TSLEC) 协议进化在多智能体强化学习中的通信 [PDF](https://arxiv.org/pdf/2511.19562), [HTML](https://arxiv.org/abs/2511.19562)
### Authors
Abraham Itzhak Weinberg
### Background
多智能体系统中的自发通信通常通过独立学习发生，这导致收敛速度慢且可能产生次优协议。
### Innovation
提出了一种基于信任的社会学习框架TSLEC，其中智能体显式地教授成功的策略给同伴，并通过学习的信任关系进行知识传递。通过30组随机种子下的100集实验，结果显示，与独立自发学习相比，基于信任的社会学习在收敛集数上减少了23.9%（p < 0.001, Cohen's d = 1.98），同时产生的协议具有较强的组合性，且在动态目标下保持鲁棒性。
### Conclusion
研究表明，显式的社会学习从根本上加速了多智能体协调中的自发通信。
## 75. `cs.AI` - 符号信道原理：LLM通信中的意义容量测量 [PDF](https://arxiv.org/pdf/2511.19550), [HTML](https://arxiv.org/abs/2511.19550)
### Authors
Davide Picca
### Background
本文提出了一个新的符号框架来分析大规模语言模型（LLMs），将其视为随机符号引擎，其输出需要主动且非对称的人类解释。作者通过信息论工具形式化了表达丰富性（符号广度）与解释稳定性（可解密性）之间的权衡。
### Innovation
作者引入了一个生成复杂性参数（λ）来管理这种权衡，通过λ量化了广度并计算了模糊性。他们还定义了一个依赖于观众和情境的符号信道，并将其容限能力定义为最大可解密性，通过优化λ来实现。
### Conclusion
基于此容量的符号方法提供了一个严格的、可操作的工具包，用于理解、评估和设计通过LLM介导的通信。
## 76. `cs.AI` - 先思考，后分配 (ThiFAN-VQA): 一种双重chain-of-thought框架用于灾难后评估 [PDF](https://arxiv.org/pdf/2511.19557), [HTML](https://arxiv.org/abs/2511.19557)
### Authors
Ehsan Karimi,Nhut Le,Maryam Rahnemoonfar
### Background
及时准确地评估自然灾害后的损害对于有效的应急响应和恢复至关重要。最近，基于AI的方法已经开发出来，利用无人机收集的大量航拍图像进行分析，以提供快速的行动建议。然而，创建和标注用于训练这些模型的数据成本高、耗时长，导致数据集规模和多样性受限。此外，大多数现有方法依赖于传统的基于分类的框架，固定的答案空间限制了它们提供新增信息的能力，需要额外的数据收集或模型重新训练。使用基于上下文学习(ICL)的预训练生成模型可以实现灵活和开放的答案空间。但是，这些模型往往生成虚幻输出或产生缺乏领域特定相关性的通用响应。
### Innovation
提出了一种名为ThiFAN-VQA的双阶段推理框架，用于灾难情景下的视觉问答(VQA)。该框架首先通过链式思维(CoT)提示和上下文学习(ICL)生成结构化的推理痕迹，以在有限监督下实现可解释的推理。随后的答案选择模块评估生成的响应，并赋予最连贯和上下文相关的答案，提升了模型表现。该框架通过结合自定义信息检索系统、领域特定提示和推理引导的答案选择，填补了零样本和监督方法之间的空白，实现了灵活性与一致性的结合。
### Conclusion
在洪水网(FloodNet)和救援网(UAV)基于无人机的数据集（受洪水和飓风影响的区域）上的实验表明，ThiFAN-VQA在实际灾难评估任务中表现出了更高的准确性、可解释性和适应性。
## 77. `cs.AI` - 跨域多模态LLM在全局光伏评估中的泛化 [PDF](https://arxiv.org/pdf/2511.19537), [HTML](https://arxiv.org/abs/2511.19537)
### Authors
Muhao Guo,Yang Weng
### Background
分布式光伏发电系统的迅速扩张给电力 grid 管理带来了挑战，因为许多安装尚未被记录。尽管卫星图像提供了全球覆盖，但传统的计算机视觉模型，如 CNN 和 U-Nets，需要大量的标注数据才能推广使用，并且在不同区域难以泛化。
### Innovation
本研究调查了多模态大规模语言模型（LLM）在跨域全球光伏评估中的应用。通过利用结构化提示和微调，该模型在统一框架中集成了检测、定位和量化。使用 $triangle$F1 评价指标进行跨区域评估表明，所提出模型在不同未见区域表现出最小的性能下降，优于传统的计算机视觉和变压器基线。
### Conclusion
这些结果突显了多模态 LLM 在域移中具有稳健性，并且具有可扩展性、可转移性和可解释性的全球光伏图谱的潜力。
## 78. `cs.AI` - SPQR: 一种标准化的文本到图像扩散模型现代安全对齐方法基准 [PDF](https://arxiv.org/pdf/2511.19558), [HTML](https://arxiv.org/abs/2511.19558)
### Authors
Mohammed Talha Alam,Nada Saadi,Fahad Shamshad,Nils Lukas,Karthik Nandakumar,Fahkri Karray,Samuele Poppi
### Background
文本到图像的扩散模型可能会生成受版权保护、不安全或私人内容。现有的安全对齐方法旨在压制特定概念，但很少有评估测试这些方法在部署后的良性下游微调（例如，LoRA个性化、风格/领域适配器）中是否仍能保持安全性。现有的安全方法在良性微调过程中表现出频发的不稳定性，因此提出了SPQR基准（Safety-Prompt 贯彻性-Quality-稳健性），这是一个单一评分的指标，提供了一个标准化和可重复的框架来评估在良性微调过程中，安全对齐的扩散模型如何保留其安全性、实用性和稳健性。
### Innovation
引入了SPQR基准，这是一项单一评分指标，能够评估在良性微调过程中，安全对齐的文本到图像扩散模型保持其安全、实用性和稳健性的能力。该基准通过报告单一排行榜分数来促进比较，同时涵盖了多语言、特定领域和分布外分析以及类别级分解，以识别在良性微调后安全对齐失败的情况。
### Conclusion
SPQR作为简洁而全面的基准工具，适用于文本到图像模型中现代安全对齐方法的评估，最终展示了SPQR对于检测文本到图像扩散模型安全对齐失败的可靠性。
## 79. `cs.AI` - 超越二元分类：基于半监督的方法在通用AI生成图像检测中的应用 [PDF](https://arxiv.org/pdf/2511.19499), [HTML](https://arxiv.org/abs/2511.19499)
### Authors
Hong-Hanh Nguyen-Le,Van-Tuan Tran,Dinh-Thuc Nguyen,Nhien-An Le-Khac
### Background
生成器的快速发展（如StyleGAN、Midjourney、DALL-E）产生了极真实的合成图像，这为数字媒体的真实性带来了重大挑战。现有的鉴伪方法通常基于几种核心架构，尤其是生成对抗网络（GAN）和扩散模型（DM）。当前鉴伪方法的一个关键弱点是无法在不同生成器间实现通用性，特别是在跨越不同架构边界时表现不佳（例如，从GAN到DM）。作者认为，这一缺口源于这些不同架构所产生的基本差异。在本文中，作者通过理论分析阐明了GAN和DM的优化目标如何导致不同流形覆盖行为。研究表明，GAN允许部分覆盖，经常导致边界伪影，而DM则要求完全覆盖，造成过度平滑模式。
### Innovation
本文提出了一个半监督方法Triarchy Detector (TriDetect)，它通过发现“虚假”类别中的隐藏架构模式来增强二分类。TriDetect使用Sinkhorn-Knopp算法进行平衡聚类分配，并采用跨视图一致性机制，鼓励模型学习核心架构差异。相对于13个基准模型，我们在两个标准基准和三个野外数据集上评估了我们的方法，证明了其在未见过的生成器上的泛化能力。
### Conclusion
我们的研究通过分析揭示了不同架构的根本差异，并提出了TriDetect方法，该方法不仅能提升二元分类性能，还能有效发现隐藏的架构模式。此外，TriDetect展示了其对未见过生成器的有效泛化能力，表明了它在通用AI生成图像检测中的潜力。
## 80. `cs.AI` - 无遗忘的合并：通过最优运输不断融合专用任务模型 [PDF](https://arxiv.org/pdf/2511.19561), [HTML](https://arxiv.org/abs/2511.19561)
### Authors
Zecheng Pan,Zhikang Chen,Ding Li,Min Zhang,Sen Cui,Hongshuo Jin,Luqi Tao,Yi Yang,Deheng Ye,Yu Zhang,Tingting Zhu,Tianling Ren
### Background
融合针对不同任务微调的模型，以构建多功能、高效的多任务系统，已成为一个重要方向。现有的方法主要依赖于参数插值，但这种方法会导致特征空间中的显著分布偏移，从而削弱了特定任务的知识。
### Innovation
本文提出了一种新型的模型合并框架OTMF（基于最优运输的掩码融合），它基于最优运输理论来解决直接参数插值引起的分布偏移问题。OTMF通过发现共同应用于任务向量中的掩码，以最优运输计划对特定任务的语义几何进行对齐，从而选择性地提取可转移且任务无关的组件，同时保留每个任务的独特结构身份。此外，为了实现在实际场景中的可扩展性，OTMF还支持持续融合范式，可以在不回顾过去任务的情况下逐步集成新任务向量，保持内存占用的上限并能够高效地在不断增加的任务数量中进行融合。
### Conclusion
我们在多个视觉和语言基准上进行了全面实验，结果显示，OTMF在准确性和效率方面均达到了最先进水平。这些发现凸显了我们方法结合模型的实际和理论价值。
## 81. `cs.AI` - 逻辑程序中的计数系统 [PDF](https://arxiv.org/pdf/2511.19565), [HTML](https://arxiv.org/abs/2511.19565)
### Authors
Jorge Fandinno,Vladimir Lifschitz
### Background
在约束集编程中，两个规则组如果在任何上下文下的含义相同，则被认为是强等价的。有时可以通过在适当的演绎系统中导出一个程序的规则到另一个程序的规则来验证两个程序的强等价性。然而，在包含计数聚合的程序中，这种方法的有效性受到了挑战。
### Innovation
本文展示了如何将验证强等价性的方法扩展到包含计数聚合的程序中，通过构建适用于此类程序的演绎系统来实现。
### Conclusion
通过这种方法，可以验证包含计数聚合的逻辑程序的强等价性，从而提高算法的效率和正确性。
## 82. `cs.AI` - 基础模型在快速MRI中的实用性：基于视-语言引导的图像重建 [PDF](https://arxiv.org/pdf/2511.19641), [HTML](https://arxiv.org/abs/2511.19641)
### Authors
Ruimin Feng,Xingxin He,Ronald Mercer,Zachary Stewart,Fang Liu
### Background
研究目的是探索基于视-语言基础模型在不完全采样MRI重建中的应用，其通过提供超越传统先验的高级上下文信息来增强图像重建效果。
### Innovation
提出了一个语义分布引导的重建框架，该框架利用预训练的视-语言基础模型将重建图像和辅助信息编码为高级语义特征，并通过对比目标对重建表示进行调整，确保高级感知线索的一致性。该目标可与多种深度学习重建方法兼容，并能灵活地从多模态源中整合语义先验。
### Conclusion
研究结果表明，基于图像和图像-语言辅助信息的语义先验能够在保持数据保真度的同时，引导重建特征向期望的语义分布发展，从而改善MRI重建的感知质量。
## 83. `cs.AI` - 通过LLM规划和嵌入引导搜索实现高效的知识图谱多跳问答 [PDF](https://arxiv.org/pdf/2511.19648), [HTML](https://arxiv.org/abs/2511.19648)
### Authors
Manil Shrestha,Edward Kim
### Background
多跳问答在知识图谱上的处理由于潜在推理路径的组合爆炸而具有计算上的挑战。现有方法依赖于昂贵的大语言模型（LLM）推理，既用于实体链接也用于路径排名，这限制了它们的实际部署。此外，LLM生成的答案往往缺乏与结构化知识的可认证链接。
### Innovation
提出了两种互补的混合算法来解决效率和验证性问题：1. LLM引导规划使用单一的LLM调用来预测通过广度优先搜索执行的关系序列，实现接近完美的准确率（微F1 > 0.90），同时确保所有答案都基于知识图谱；2. 嵌入引导神经搜索完全消除LLM调用，通过轻量级670万参数的边评分器融合文本和图嵌入，实现超过100倍的加速，保持竞争力的准确率。通过知识蒸馏，将规划能力压缩到40亿参数的模型，性价比最大化。
### Conclusion
知识问答和推理一致性优于直接生成，结构化规划比直接答案生成更具可移植性。结果表明，验证性多跳推理在推理时间上不依赖于大规模模型，而是结合符号结构与学习表示的最佳架构设计。
## 84. `cs.AI` - 基于机器人的数据飞轮：在野外部署机器人实现连续数据收集和基础模型适应 [PDF](https://arxiv.org/pdf/2511.19647), [HTML](https://arxiv.org/abs/2511.19647)
### Authors
Jennifer Grannen,Michelle Pan,Kenneth Llontop,Cherie Ho,Mark Zolotas,Jeannette Bohg,Dorsa Sadigh
### Background
基础模型（FM）在视觉和语言方面展现了强大的零样本能力，但由于依赖于互联网上的预训练数据，它们在不规则、现实世界环境中的表现脆弱。部署过程中遇到的混乱现实数据（如遮挡或多语言文本）在现有数据集中仍然严重不足。相比之下，作为有形代理的机器人可以收集大量现实世界的高质量数据，以增强FM训练，弥补现有多数模型缺失的例子。
### Innovation
引入了机器人力驱动的数据飞轮框架，将机器人从基础模型的消费者转变为数据生成者。通过在真实环境中部署携带基础模型的机器人，实现了一个良性循环：机器人在执行有益任务的同时收集能够改善特定领域适应和相邻领域泛化的现实数据。具体实例是使用在东亚图书馆部署两周的可移动机器人扫描福德（Scanford）进行操作。Scanford 自动扫描书架、使用基于视觉-语言模型进行图书识别，并利用图书馆目录进行图像标注，无需人工注释。
### Conclusion
机器人驱动的数据飞轮不仅能减少现实部署中的劳动力成本，还能解锁不断适应基础模型以应对现实世界混乱特性的新途径。通过从2103个书架收集的数据，Scanford 提升了基于视觉-语言模型在书中识别上的性能，从32.0%提升至71.8%，并实现了对后续任务如多语言OCR的增强，进一步证明了这一框架的有效性。
## 85. `cs.AI` - HunyuanOCR 技术报告 [PDF](https://arxiv.org/pdf/2511.19575), [HTML](https://arxiv.org/abs/2511.19575)
### Authors
Hunyuan Vision Team,Pengyuan Lyu,Xingyu Wan,Gengluo Li,Shangpin Peng,Weinong Wang,Liang Wu,Huawen Shen,Yu Zhou,Canhui Tang,Qi Yang,Qiming Peng,Bin Luo,Hower Yang,Houwen Peng,Hongming Yang,Senhao Xie,Binghong Wu,Mana Yang,Sergey Wang,Raccoon Liu,Dick Zhu,Jie Jiang,Linus,Han Hu,Chengquan Zhang
### Background
本文介绍了一种名为 HunyuanOCR 的开放式、轻量级（参数量1B）视觉语言模型（VLM），专用于OCR任务。它结合了本源视觉变换器（ViT）和轻量级的大规模语言模型（LLM），并通过MLP适配器进行连接。
### Innovation
1. 统一了适用性和效率：该模型涵盖了核心能力如定位、解析、IE、VQA和翻译等，且是在一个轻量级框架中实现的，解决了单一的“OCR专家模型”和复杂的“通用VLM”的局限性；2. 简化的端到端架构：摈弃了预先处理模块（如布局分析），从根本上避免了传统流水线中常见的错误传播问题，简化了系统的部署；3. 数据驱动和强化学习策略：确认了高质量数据的作用，并首次展示了强化学习策略在OCR任务中能带来显著的性能提升。
### Conclusion
HunyuanOCR 在ICDAR 2025 DIMT挑战中的小型模型赛道上获得了第一，并在OCRBench测试中获得了最好的性能。该模型已在HuggingFace上开源，并提供高性能部署方案vLLM，提高了生产效率，旨在推进前沿研究和工业应用。
## 86. `cs.AI` - IRSDA: 企业入侵响应的代理协调框架 [PDF](https://arxiv.org/pdf/2511.19644), [HTML](https://arxiv.org/abs/2511.19644)
### Authors
Damodar Panigrahi,Raj Patel,Shaswata Mitra,Sudip Mittal,Shahram Rahimi
### Background
现代企业系统面临着日益动态、分布式和多阶段的网络威胁。传统入侵检测与响应系统通常依赖静态规则和手动工作流程，难以在高危环境中以所需的速度和精度做出响应。
### Innovation
提出了基于代理的入侵响应系统数字助手（IRSDA），这是一种自主且政策合规的网络防御框架。IRSDA集成了自适应自组织计算系统（SA-ACS）和带知识指导的监控、分析、计划和执行（MAPE-K）循环，支持跨企业基础设施的实时、区段感知决策。IRSDA采用基于知识的架构，将上下文信息与基于AI的推理相结合，支持系统指导的入侵响应，并利用检索机制和结构化表示来支持决策制定，同时保持与操作策略的一致性。
### Conclusion
本文概述了一种模块化且代理驱动的网络安全方法，强调入侵响应中的可解释性、系统状态感知和操作控制。
## 87. `cs.AI` - 众多正确的方法：基于概念的神经网络的拉什omon集 [PDF](https://arxiv.org/pdf/2511.19636), [HTML](https://arxiv.org/abs/2511.19636)
### Authors
Shihan Feng,Cheng Zhang,Michael Xi,Ethan Hsu,Lesia Semenova,Chudi Zhong
### Background
现代神经网络往往没有单一的最佳解法。多项任务中，多个模型可以达到相同的性能水平，但依赖的特征或推理模式却截然不同，这被称为拉什omon效应。然而，揭示深层架构中的这种多样性非常具有挑战性。深层架构的连续参数空间包含无数个近似最优的解，这些解从数值上是不同的，但行为上却高度相似，难以区分。
### Innovation
我们提出了一种基于概念的神经网络拉什omon概念瓶颈模型框架，该框架能够学习多个神经网络，每个神经网络都能准确并基于不同的人类可理解的概念进行推理。通过结合轻量级适配器模块并与多样性正则化训练目标相结合，我们的方法可以在无需从头开始重新训练的情况下高效地构建出一系列基于概念的深层模型。由此产生的网络提供了相同预测中根本不同的推理过程，揭示了在同等性能解决方案中概念依赖和决策制定之间的差异。该框架为深层模型中数据驱动推理多样性的系统探索提供了新机制，提供了一种新的审计、比较和在同等准确解决方案中对齐的手段。
### Conclusion
我们的框架揭示了同等性能解决方案中的概念依赖和决策制定的差异，并提供了探索基于概念的深层模型中数据驱动推理多样性的新方法。
## 88. `cs.AI` - 合成数据：AI对抗Android恶意软件的新武器 [PDF](https://arxiv.org/pdf/2511.19649), [HTML](https://arxiv.org/abs/2511.19649)
### Authors
Angelo Gaspar Diniz Nogueira,Kayua Oleques Paim,Hendrio Bragança,Rodrigo Brandão Mansilha,Diego Kreutz
### Background
随着Android设备数量的不断增长和恶意软件演化的加速，到2024年预计将达到超过3500万样本。这凸显了有效检测方法的迫切重要性。攻击者利用人工智能来创建高度复杂的恶意软件变种，这些变种能够轻松避开传统的检测技术。虽然机器学习在恶意软件分类中展现了潜力，但其成功很大程度上依赖于获取即时、高质量的数据集。由于获取和标记真实的恶意软件样本稀缺且成本高，这给开发出稳健的检测模型带来了重大挑战。
### Innovation
本文提出了一种MalSynGen恶意软件合成数据生成方法，该方法使用条件生成对抗网络（cGAN）生成合成表格数据。这种方法保留了真实数据的统计属性，并提升了Android恶意软件分类器的性能。通过各种数据集和评估指标来验证该方法的有效性，这些评估指标考察了生成数据的保真度、分类实用性和处理过程的计算效率。实验结果表明，MalSynGen能够跨不同数据集泛化，提供了一种解决恶意软件检测中数据过时和质量低问题的可行方案。
### Conclusion
MalSynGen方法可以通过生成合成数据来增强恶意软件分类器的性能，解决获取真实恶意软件样本的困境，并提供一种解决恶意软件检测中数据过时和质量低问题的可行方案。
## 89. `cs.AI` - Generative人工智能中的协动师机互动 [PDF](https://arxiv.org/pdf/2511.19580), [HTML](https://arxiv.org/abs/2511.19580)
### Authors
Mutlu Cukurova,Wannapon Suraworachet,Qi Zhou,Sahan Bulathwela
### Background
生成式人工智能（GenAI）在教育中的应用日益增多，给教师带来了适应这些变化的重大挑战。GenAI在教育任务中提供了前所未有的可访问性、可扩展性和生产力，但通过GenAI自动化教学任务引发了关于教师自主权减少、认知萎缩以及更广泛的教育去专业化方面的担忧。
### Innovation
本文通过回顾文献并结合最近的系统文献综述，提出了五种层级的教师-人工智能团队协作概念：事务级、情境级、操作级、实践级和协同级团队协作。该框架旨在捕捉教师-人工智能互动的复杂动态，包括替代、互补或增强教师能力与专业实践的途径。文章还讨论了支持团队协作所需的GenAI技术支持，以及相关实证研究。进一步讨论了教师-人工智能团队协作之外的社会技术因素，以实现教育中的伦理和实际协同作用。
### Conclusion
文章展望了未来，从单个教师自主权转向教师和人工智能之间的协作决策，其中双方共同进行谈判、建设性挑战和共推理，从而增强彼此的能力并实现单独无法实现的成果。还进一步讨论了超越教师-人工智能团队协作的社交-技术因素，以伦理和实际方式优化教师和人工智能在教育中的协同作用。
## 90. `cs.AI` - TREASURE: 基于Transformer的基础模型实现高volume交易理解 [PDF](https://arxiv.org/pdf/2511.19693), [HTML](https://arxiv.org/abs/2511.19693)
### Authors
Chin-Chia Michael Yeh,Uday Singh Saini,Xin Dai,Xiran Fan,Shubham Jain,Yujie Fan,Jiarui Sun,Junpeng Wang,Menghai Pan,Yingtong Dou,Yuzhong Chen,Vineeth Rakesh,Liang Wang,Yan Zheng,Mahashweta Das
### Background
支付网络构成了现代商业活动的基础，每天产生大量的交易记录。恰当建模这些数据可以应用于异常行为检测和个性化消费者洞察等应用，从而提升人们的生活质量。本文介绍了一种名为TREASURE（TRansformer Engine As Scalable Universal transaction Representation Encoder）的多用途变压器基础模型，适用于交易数据。
### Innovation
TREASURE模型同时捕获消费者行为和支付网络信号（如响应码和系统标志），通过特定的输入模块、高效训练范式以及作为一个独立模型提升异常行为检测性能111%和作为嵌入提供者提升推荐模型性能104%，展示了其作为基础模型的有效性。
### Conclusion
本文通过详尽的消融研究、与生产模型的基准测试和案例研究，展示了TREASURE在交易理解中的关键见解，突显了开发TREASURE所获得的宝贵知识，证明了TREASURE的有效性。
## 91. `cs.AI` - IndEgo:一个工业场景和协作工作的自视点数据集，用于自视点助手 [PDF](https://arxiv.org/pdf/2511.19684), [HTML](https://arxiv.org/abs/2511.19684)
### Authors
Vivek Chavan,Yasmina Imgrund,Tung Dao,Sanwantri Bai,Bosong Wang,Ze Lu,Oliver Heimann,Jörg Krüger
### Background
本文介绍了一个名为IndEgo的多模态自视点和外视点数据集，涵盖了包括装配/拆卸、物流和组织、检查和修理、木工等在内的通用工业任务。该数据集包含3460个自视点记录（约197小时），以及1092个外视点记录（约97小时），重点在于协作工作，其中两名工人共同执行认知和体力强度高的任务。
### Innovation
该数据集专注于协作工作，并提供了丰富的多模态数据和背景信息，如眼动、解说、声音、运动等。此外，还提供了详细注释（动作、总结、错误注释、解说）、元数据、处理输出（眼动、手的姿势、半密集点云），以及关于程序性和非程序性任务理解、错误检测和基于推理的问题回答基准测试，表明最先进的多模态模型在该数据集面临挑战。
### Conclusion
基准测试结果显示，错误检测、问题回答及协作任务理解对于最先进的模型来说是一个挑战。数据集可供下载。
## 92. `cs.AI` - 神经簇的亚历山大-希尔斯豪文定理 [PDF](https://arxiv.org/pdf/2511.19703), [HTML](https://arxiv.org/abs/2511.19703)
### Authors
A. Massarenti,M. Mella
### Background
本文研究了多项式神经网络的神经簇，并在单输出情况下探讨了它们达到预期维度的条件。通过这一研究，文章进一步详细分析了多输出架构的无亏性和全局可观测性。
### Innovation
文章主要创新之处在于全面刻画了单输出情况下神经簇达到预期维度的情况，从而得出多输出架构的无亏性和全局可观测性。
### Conclusion
本文通过研究多项式神经网络的神经簇，建立了在单输出情况下神经簇达到预期维度的条件，并在此基础上探讨了多输出架构的无亏性和全局可观测性。
## 93. `cs.AI` - 参数调整与完全微调之间的准确性和效率权衡：基于LLM的恶意软件检测和解释的比较研究 [PDF](https://arxiv.org/pdf/2511.19654), [HTML](https://arxiv.org/abs/2511.19654)
### Authors
Stephen C. Gravereaux,Sheikh Rabiul Islam
### Background
在利用大型语言模型（LLMs）进行恶意软件分类时，提供人类可解释的决策与解释目前仍然是一个重大挑战。这项研究旨在探讨低秩适应（LoRA）细调的LLMs是否能在生成可解释的决策和解释方面达到与完全微调模型相当的性能，特别是在可信的恶意软件检测方面。
### Innovation
开发了一种评估框架，使用BLEU、ROUGE和语义相似度指标来衡量五种LoRA配置和完全微调基线的解释质量。研究发现，尽管完全微调在BLEU和ROUGE评分上取得最高总体分数，但中期LoRA模型在两个指标上的表现与完全微调相当，同时减少了约81%的模型大小和超过80%的训练时间。这些发现表明，LoRA提供了一种在可解释性和资源效率之间取得平衡的实用方案，能够在资源限制环境中部署，而不会牺牲解释质量。
### Conclusion
通过为恶意软件分类提供基于特征的自然语言解释，该方法增强了恶意软件检测系统的透明度、分析师的信心以及操作规模。LoRA模型在解释质量和资源效率方面提供了实用的平衡，适应了资源受限环境的部署需求，同时保持了高质量的解释。
## 94. `cs.AI` - Prompt Fencing: 一种在大型语言模型提示中建立安全边界的密码学方法 [PDF](https://arxiv.org/pdf/2511.19727), [HTML](https://arxiv.org/abs/2511.19727)
### Authors
Steven Peh
### Background
大型语言模型（LLMs）仍然容易受到提示注入攻击，这是生产部署中最严重的安全威胁。目前的LLMs缺乏内置的安全边界意识，但在实验中通过模拟意识，可以完全防止注入攻击。
### Innovation
我们提出了一种名为Prompt Fencing的新颖架构方法，它结合了加密认证和数据架构原则，为LLM提示建立了明确的安全边界。通过加密签名元数据来装饰提示段，包括信任评级和内容类型，使LLM能够区分可信指令和不可信内容。
### Conclusion
我们的方法是平台无关的，并可以逐步部署为现有LLM基础设施上的安全层，预期未来的模型将通过内置的边界意识进行训练，以实现最佳安全性。我们实现了一个概念验证的边界生成和验证流水线，总开销为0.224秒（0.130秒用于生成，0.094秒用于验证），共涉及100个样本，实验结果显示成功防止了所有模拟攻击案例。
## 95. `cs.AI` - 代理互联网分层协议架构 [PDF](https://arxiv.org/pdf/2511.19699), [HTML](https://arxiv.org/abs/2511.19699)
### Authors
Charles Fleming,Vijoy Pandey,Ramana Kompella,Luca Muscariello
### Background
大型语言模型（LLMs）在性能提升和学习领域特定语言（DSLs）方面表现出色，包括API和工具接口。这些模型能进行初步计算并执行工具调用，现通过协议如MCP标准化。然而，LLMs具有固有限制，如有限的上下文窗口，影响其存储和计算能力。代理协作对于解决复杂问题变得至关重要，类似于如何通过不同类型的存储扩展计算系统。
### Innovation
为了解决代理间缺乏语义理解的协作问题，作者提出了分层协议架构，包括新的代理通信层（L8）和代理语义协商层（L9）。L8标准化了通信结构，定义了消息信封、言语行为（如请求、通告）和交互模式。L9则定义了通信的意义，使代理能够发现、协商和锁定一个“共享语境”，即一个形式化的架构，定义代理交互相关的概念、任务和参数。
### Conclusion
这些分层提供了一个可扩展的分布式代理协作基础，支持下一代多代理系统的发展。
## 96. `cs.AI` - CrypTorch: 基于PyTorch的自动调优编译器，用于多方计算中的机器学习 [PDF](https://arxiv.org/pdf/2511.19711), [HTML](https://arxiv.org/abs/2511.19711)
### Authors
Jinyu Liu,Gang Tan,Kiwan Maeng
### Background
机器学习涉及私有数据和专有模型参数。多方计算（MPC）允许多个实体在不共享私有数据或模型参数的情况下协作运行机器学习任务。然而，MPC 无法原生运行诸如 Softmax 或 GELU 等机器学习操作，因此现有框架使用不同的近似方法。但研究发现，在高性能框架中，这些近似方法往往成为主要瓶颈，常见近似方法往往不够精确或执行过慢，且在现有框架中识别和修复这些问题很困难。
### Innovation
提出了一种用于 MPC 的机器学习的编译器 CrypTorch。CrypTorch 解开了这些近似与 MPC 运行时其余部分的关系，通过编程接口允许轻松添加新的近似方法，并自动选择近似方法以最大化性能和准确性。作为 PyTorch 2 编译器的扩展，仅自动调优功能即可在不牺牲精度的情况下提供 1.20-1.7 倍的即时加速，并在允许一定程度精度下降时提供 1.31-1.8 倍的加速。结合更好的工程实践和最新技术的应用，整个框架相对于流行的框架 CrypTen 提供了 3.22-8.6 倍的端到端加速。
### Conclusion
CrypTorch 通过自动调优编译器在不牺牲精度的情况下显著提升了 MPC 下的机器学习性能，并结合最佳实践提供了显著的端到端速度优势。
## 97. `cs.AI` - 一种集成数据的适应性代理模型框架，用于可解释和可争论的政策设计 [PDF](https://arxiv.org/pdf/2511.19726), [HTML](https://arxiv.org/abs/2511.19726)
### Authors
Roberto Garrone
### Background
多智能体系统通常在反馈、适应性和非平稳性条件下运行，但许多模拟研究仍保留静态决策规则和固定控制参数。这限制了对学习代理和自适应控制如何共同塑造系统轨迹的理解。
### Innovation
该论文引入了一个通用的自适应多智能体学习框架，该框架包含四个动态阶段以区分静态与自适应智能体及固定与自适应系统参数；信息论诊断（熵率、统计复杂性和预测信息）来评估可预测性和结构；结构因果模型用于明确干预语义；生成智能体级别先验的方法从汇总或样本数据中；以及无监督方法来识别新兴的行为模式。
### Conclusion
该框架提供了一个无领域偏见的分析架构，用于评估学习智能体和自适应控制如何共同影响系统轨迹。这允许对非平衡、振荡或漂移动态下的稳定、性能和可解释性进行系统比较。本文提供了数学定义、计算操作以及实验设计模板，从而形成了一个结构化的开发可解释和可争论的多智能体决策过程的方法。
## 98. `cs.AI` - 利用PathFMTools在基座模型中进行表皮鳞状细胞癌的组织学分级 [PDF](https://arxiv.org/pdf/2511.19751), [HTML](https://arxiv.org/abs/2511.19751)
### Authors
Abdul Rahman Diab,Emily E. Karn,Renchin Wu,Emily S. Ruiz,William Lotter
### Background
尽管计算病理学基座模型持有巨大潜力，但将其应用于特定的临床任务仍面临挑战。这主要由于全切片图像（WSI）处理的复杂性、学习特征的晦涩不明以及潜在适应策略的广泛多样性。
### Innovation
我们介绍了一款轻量级且可扩展的Python工具PathFMTools，用于高效执行、分析和可视化病理基座模型。通过PathFMTools对接并评估了两种领先的视觉-语言基座模型（CONCH和MUSK），用于表皮鳞状细胞癌（cSCC）的组织学分级任务。通过440例cSCC HE切片图像的数据集，我们对多种适应策略进行了基准测试，展示了不同预测方法之间的权衡，验证了采用基座模型嵌入作为训练小专门模型的潜力。
### Conclusion
这些研究结果凸显了病理基座模型在临床应用中的前景，而PathFMTools则使高效的分析和验证成为可能。
## 99. `cs.AI` - Prune-Then-Plan: 在具身问题回答中的步骤级校准以实现稳定的前沿探索 [PDF](https://arxiv.org/pdf/2511.19768), [HTML](https://arxiv.org/abs/2511.19768)
### Authors
Noah Frahm,Prakrut Patel,Yue Zhang,Shoubin Yu,Mohit Bansal,Roni Sengupta
### Background
巨大的视觉语言模型（VLMs）通过提供强大的语义先验，增强了开放词汇推理的具身问答（EQA）代理。然而，当直接用于步骤级探索时，VLMs往往表现出前沿振荡，这是一种由过度自信和错校准引起的不稳定前后摇摆运动，导致导航效率低下且答案质量下降。
### Innovation
提出了Prune-Then-Plan框架，这是一种简单而有效的方法，通过步骤级校准来稳定探索。不同于信任原始VLM得分，该方法使用霍姆-鲍nferroni启发的修剪程序来剔除不合理的前沿选择，随后将最终决策委托给基于覆盖率的规划器。这种分离将过于自信的预测转换为保守、可解释的行为，依靠人类级别的判断来校准VLM在步骤级的行为。
### Conclusion
将我们的方法集成到3D-Mem EQA框架中，我们的方法在视觉基础SPL和LLM-Match指标上分别相对于基线达到了高达49%和33%的相对改进。总体而言，在相同的探索预算下，我们的方法在OpenEQA和EXPRESS-Bench数据集上实现了更好的场景覆盖。
## 100. `cs.AI` - TiCT：用于时间序列分类的合成预训练基础模型 [PDF](https://arxiv.org/pdf/2511.19694), [HTML](https://arxiv.org/abs/2511.19694)
### Authors
Chin-Chia Michael Yeh,Uday Singh Saini,Junpeng Wang,Xin Dai,Xiran Fan,Jiarui Sun,Yujie Fan,Yan Zheng
### Background
时间序列数据的普遍存在催生了对通用基础模型的强烈需求，但这些模型在分类任务上的开发仍然面临显著挑战，主要原因是标注数据的成本高昂。具备上下文推理能力（ICL）的基础模型提供了强大的解决方案，通过少量示例即可适应新任务，减少了大量重新训练的需求。然而，针对大规模时间序列模型的研究大多集中在预测方面，忽略了对多功能、无需微调的分类模型的需求，因此存在关键缺口。
### Innovation
我们引入了TiCT（时间序列上下文转换器）模型，这是一种仅在合成数据上进行预训练的基于变压器的模型，用于进行上下文分类。主要技术贡献包括：1）一种新型架构，集成了可扩展的位基标签编码和特别的输出注意机制，以处理任意数量的类别；2）一种合成预训练框架，结合了Mixup启发式的处理方式和数据增强技术，以促进泛化和噪声不变性。实验结果表明，TiCT在UCR档案上的表现与最先进的监督方法具有可竞争性，并且仅在推理时使用上下文示例即可实现这一目标，无需更新任何模型权重。
### Conclusion
TiCT通过在合成数据上进行预训练来执行上下文分类，展示了在时间序列分类任务上的竞争性能。这种模型能够在不更新单个模型权重的情况下仅使用推理时的上下文示例来实现这一目标。
## 101. `cs.AI` - Cisco 时间序列模型技术报告 [PDF](https://arxiv.org/pdf/2511.19841), [HTML](https://arxiv.org/abs/2511.19841)
### Authors
Liang Gou,Archit Khare,Praneet Pabolu,Prachi Patel,Joseph Ross,Hercy Shen,Yuhan(Ellen)Song,Jingze Sun,Kristal Curtis,Vedant Dharnidharka,Abhinav Mathur,Hao Yang
### Background
介绍了Cisco Time Series Model，这是一种用于时间序列预测的单变量零样本预测器。该模型基于一种通用的架构创新，使得时间序列模型能够接受多分辨率输入，并应用到了一个流行的仅解码器的时间序列模型（TimesFM）。该模型在超过300亿个独特的数据点上进行了训练，其中超过一半的数据点来自可观测性领域。
### Innovation
该时间序列基础模型的创新在于能够接受多分辨率输入的通用架构。训练了一个仅解码器的多分辨率模型，模型在超过300亿个独特的数据点上进行训练，其中包括大量的可观测性领域数据。
### Conclusion
该模型在可观测性数据集上表现出优越的性能，同时在标准的通用基准（GIFT-Eval）上保持了相似的性能。多分辨率结构使得模型在长上下文输入预测方面能够更加准确。
## 102. `cs.AI` - 终端速度匹配 [PDF](https://arxiv.org/pdf/2511.19797), [HTML](https://arxiv.org/abs/2511.19797)
### Authors
Linqi Zhou,Mathias Parger,Ayaan Haque,Jiaming Song
### Background
该研究旨在改进现有的流匹配方法，提出了一种新的方法来实现高保真度的一步或多步骤生成建模。背景在于现有方法在实际应用中存在训练不稳定等问题。
### Innovation
提出了终端速度匹配（TVM）方法，这是一种流匹配的一般化版本。该方法通过在终态而不是初始态来正则化行为，能够准确建模任意两个扩散时间步之间的转换过程。此外，TVM通过最小化架构修改，实现了稳定的单步训练，并开发了一种融合注意力内核，支持对雅可比-向量乘积的反向传递，从而提高效率。
### Conclusion
TVM 在 ImageNet-256x256 和 ImageNet-512x512 上分别达到了 3.29 和 1.99 的 FID 值（使用单步计算和四步计算），表明其在一步或多步模型中具有最先进的性能。
## 103. `cs.AI` - 学习以净化：噪声标签修正的强化学习 [PDF](https://arxiv.org/pdf/2511.19808), [HTML](https://arxiv.org/abs/2511.19808)
### Authors
Marzi Heidari,Hanping Zhang,Yuhong Guo
### Background
在机器学习中，噪声标签的学习挑战是显著的，如果不妥善解决，噪声标签可能会严重削弱预测模型的性能。
### Innovation
本文提出了一种新颖的框架，将噪声标签修正概念化为强化学习（RL）问题，并提出了一种名为RLNLC（基于强化学习的噪声标签修正）的方法。该方法通过定义状态空间、动作空间和奖励机制，利用演员-评论家方法学习深层特征表示策略网络来执行标签修正。
### Conclusion
通过在多个基准数据集上的广泛实验，证明了RLNLC方法在噪声标签学习方面的一致性优势，优于现有最先进的技术。
## 104. `cs.AI` - 基于LLM原生查询优化的超越关系模型：具备语义意识的多模态分析 [PDF](https://arxiv.org/pdf/2511.19830), [HTML](https://arxiv.org/abs/2511.19830)
### Authors
Junhao Zhu,Lu Chen,Xiangyu Ke,Ziquan Fang,Tianyi Li,Yunjun Gao,Christian S. Jensen
### Background
多模态分析有潜力改変电子商务、医疗保健、娱乐等领域的应用。然而，现实中的广泛采用由于传统关系查询操作有限的语义捕获能力而受阻。大规模语言模型（LLMs）的出现为开发超越关系模型的语义意识数据分析系统提供了新的机会。
### Innovation
提出了Nirvana，一个多模态数据分析框架，结合了可编程语义操作，同时利用逻辑和物理查询优化策略，特别针对LLM驱动的语义查询处理。Nirvana解决了两个关键挑战：一是使用自然语言指定的转换规则和基于随机游走的搜索机制实现具备代理逻辑优化器，探索广泛的空间并找到可接受的查询计划；二是引入成本感知物理优化器，通过新型改进评分度量选择每个操作的最有效LLM后端。此外，Nirvana通过模型能力假设指导计算重用和评估推送技术进一步提高效率。
### Conclusion
Nirvana在三个实际基准上的实验表明，它可以将端到端运行时间减少10%-85%，平均降低76%的系统处理成本，优于最先进的系统，在效率和可扩展性方面都表现优异。
## 105. `cs.AI` - Mosaic Pruning: 一种混合专家模型可迁移剪枝的分层框架 [PDF](https://arxiv.org/pdf/2511.19822), [HTML](https://arxiv.org/abs/2511.19822)
### Authors
Wentao Hu,Mingkuan Zhao,Shuangyong Song,Xiaoyan Zhu,Xin Lai,Jiayin Wang
### Background
稀疏混合专家架构（SMoE）通过仅在推理时激活一部分参数，为大规模语言模型（LLMs）的大规模扩展开辟了新领域。然而，这种架构面临着重要的实际部署障碍，因为所有专家都必须加载到内存中，从而导致静态内存消耗量的大幅增加。现有的后训练剪枝方法虽然可以减少模型大小，但这些方法通常基于单一且通用的数据集，导致在应用于其他领域时性能严重下降。这一问题在重新调整剪枝方面提高了成本。
### Innovation
本文介绍了一种新的剪枝方法——Mosaic Pruning（MoP），通过一种结构化的‘集群筛选’过程构建了一个功能全面的专家集。MoP采用了一种相似度度量来表征专家在不同任务域中的性能，通过此度量对专家进行功能聚类，并基于所提出的激活变异得分选择每个聚类中最具代表性的专家。与优化单一数据集的方法不同，MoP确保了剪枝后的模型保留了一个功能互补的专家集，能够处理多种下游任务。
### Conclusion
对多种MoE模型的实验结果表明，与先前工作相比，MoP在通用任务上取得了7.24%的性能增益，在数学推理和代码生成等专业化任务上取得了8.92%的性能增益，证明了MoP方法的优越性。
## 106. `cs.AI` - Rectified SpaAttn：重构的注意力稀疏性在高效视频生成中的再审视 [PDF](https://arxiv.org/pdf/2511.19835), [HTML](https://arxiv.org/abs/2511.19835)
### Authors
Xuewen Liu,Zhikai Li,Jing Zhang,Mengjuan Chen,Qingyi Gu
### Background
扩散变换器在视频生成中占据主导地位，但注意力计算的二次复杂性带来了显著的延迟。通过增加注意力稀疏性来减少计算成本，可以关注关键的token，忽略非关键的token。然而，现有的方法导致性能严重下降。其原因是（1）对关键token的关注过于集中，放大了它们的注意力权重；（2）完全忽视非关键token导致它们的相关注意力权重丢失。现有的稀疏注意力方法存在系统性的偏差。
### Innovation
本文重新审视了注意力稀疏性，并提出了一种新的方法——Rectified SpaAttn。具体来说，对于关键token，提出Isolated-Pooling Attention Reallocation以重新分配多模态池化权重来准确计算矫正因子；对于非关键token，提出Gain-Aware Pooling Rectification以确保矫正后的增益始终超过引入的误差。此外，通过定制并整合基于Triton的Rectified SpaAttn内核，分别在HunyuanVideo和Wan 2.1数据集上实现了3.33倍和2.08倍的加速，同时保持高质量的生成。
### Conclusion
实验结果显示，通过重构注意力稀疏性，提出的Rectified SpaAttn方法在保持视频生成质量的同时，显著提高了计算效率，实现了两倍以上的加速效果。该研究为未来的视频生成模型提供了新的优化思路。
## 107. `cs.AI` - 具有RAG增强动态提示的大语言模型系统分析：用于医学错误检测和纠正 [PDF](https://arxiv.org/pdf/2511.19858), [HTML](https://arxiv.org/abs/2511.19858)
### Authors
Farzad Ahmed,Joniel Augustine Jerome,Meliha Yetisgen,Özlem Uzuner
### Background
临床文档中包含事实、诊断和管理错误，这可能损害患者安全。大型语言模型（LLMs）能够识别和纠正这些错误，但不同提示策略下的行为尚不清楚。该研究利用MEDEC数据集评估了九种指令调优的LLMs（GPT、Claude、Gemini和OpenAI o系列模型），以检测、识别和纠正医疗错误。研究对比了零样本提示、静态提示与随机范例（SPR）以及检索增强动态提示（RDP）对三种子任务的表现。
### Innovation
研究对三种不同的提示策略进行了系统分析，包括零样本提示、静态提示与随机范例（SPR）以及检索增强动态提示（RDP）。结果显示，检索增强动态提示（RDP）在减少假阳性、提高检测准确性和生成上下文相关性更强的纠正方面表现最佳，尤其在不同类型的LLMs中表现显著。
### Conclusion
检索增强动态提示（RDP）在各类LLMs中优于零样本和静态提示。利用检索的范例可以提高检测准确性，减少假阳性，并增强医学错误纠正的可靠性。
## 108. `cs.AI` - CropVLM: 学习缩放以提高细粒度的视觉语言感知 [PDF](https://arxiv.org/pdf/2511.19820), [HTML](https://arxiv.org/abs/2511.19820)
### Authors
Miguel Carvalho,Helder Dias,Bruno Martins
### Background
视觉语言模型（VLMs）在需要精细图像理解的任务，如场景文字识别或文档分析时表现不佳，原因在于感知限制和视觉碎片化。这些挑战促使我们寻求改进的方法。
### Innovation
提出了一种名为CropVLM的外部低成本方法，通过动态地关注图像中的相关区域，增强模型捕捉细节的能力。CropVLM通过强化学习训练，无需人工标注的边界框作为监督信号，也无需昂贵的合成评估。一次训练后，它可以与开源和专有的VLMs结合以提高其性能，无需修改或微调VLM，从而避免灾难性遗忘。
### Conclusion
我们的方法在需要高分辨率图像理解任务中表现出显著的改进，尤其是在目标VLM样本外的数据集上，且保持了模型的原有结构，避免了灾难性遗忘。
## 109. `cs.AI` - 使用远程监督实现语言无关的情感标注：英文、 세佩迪语和塞茨瓦纳语案例研究 [PDF](https://arxiv.org/pdf/2511.19818), [HTML](https://arxiv.org/abs/2511.19818)
### Authors
Koena Ronny Mabokela,Tim Schlippe,Mpho Raborife,Turgay Celik
### Background
情感分析有助于自动分析不同领域（如AI for Social Good，AI in Education或营销）意见和情感。尽管已经开发了许多情感分析系统，但许多非洲语言因其缺乏文本标记语义类别的数字语言资源而被归类为低资源语言，这主要是因为手动标记文本数据耗时且昂贵。因此，需要自动和快速的过程来尽可能减少手动努力，使标记过程尽可能高效。
### Innovation
本文提出了一种自动语言无关的情感标注方法，利用情感信息的emoji和单词。实验使用来自南非多语言情感语料库SAfriSenti的英文、世佩迪语和塞茨瓦纳语的推文进行。结果显示，该情感标注方法能将英文推文的标注准确率达到66%，世佩迪语推文达到69%，塞茨瓦纳语推文达到63%，因此，平均只有34%的自动生成的标签需要进行人工修正。
### Conclusion
本文展示了一种基于远程监督的情感标注方法，尽管还有一定的误差，但已经可以在多种语言中自动进行情感标注，并取得较好效果。
## 110. `cs.AI` - 通过特征解耦提取跨模态知识 [PDF](https://arxiv.org/pdf/2511.19887), [HTML](https://arxiv.org/abs/2511.19887)
### Authors
Junhong Liu,Yuan Zhang,Tao Huang,Wenchao Xu,Renyu Yang
### Background
知识蒸馏（KD）已被证明在压缩大型模型和增强小型模型性能方面非常有效。但是，在跨模态场景（如视觉到语言的KD）中，不同模态之间的表示不一致会妨碍有效的知识转移，降低了KD的有效性。
### Innovation
本文提出了频率解耦跨模态知识蒸馏的方法，通过利用频域特征来解耦和平衡不同模态间的知识转移。具体而言，对低频特征施加强制对齐的损失，并对高频特征引入较宽松的对齐要求。同时，提出了尺度一致性损失来应对模态间的分布变化，并采用了共享分类器来统一特征空间。
### Conclusion
实验结果表明，该方法显著优于传统的KD方法以及最先进的跨模态KD方法。
## 111. `cs.AI` - AI代理供应链中行为后门检测的跨LLM通用性 [PDF](https://arxiv.org/pdf/2511.19874), [HTML](https://arxiv.org/abs/2511.19874)
### Authors
Arun Chowdary Sanna
### Background
随着AI代理成为企业工作流程不可或缺的一部分，它们对共享工具库和预训练组件的依赖性引发了显著的供应链脆弱性问题。虽然先前的研究已经展示了对单一LLM架构中行为后门检测的有效性，但不同LLM之间行为后门检测的一般性仍然未被研究，这对同时部署多种AI系统的组织构成了重大威胁。
### Innovation
本文提出了第一个系统性的跨LLM行为后门检测研究，评估了六个生产中实际应用的LLM（GPT-5.1, Claude Sonnet 4.5, Grok 4.1, Llama 4 Maverick, GPT-OSS 120B, and DeepSeek Chat V3.1）的行为后门检测的一致性。通过1198次执行轨迹和36个跨模型实验，发现单模型检测器在训练分布内的准确率为92.7%，但在不同LLM之间仅为49.2%，差距为43.4%，相当于随机猜测。研究表明，通过将模型身份作为额外特征的模型感知检测方法能够实现所有评估模型中90.6%的准确率。
### Conclusion
本文的研究揭示了单模型检测器在不同LLM之间行为后门检测的显著差距，呈现出通过包含模型身份作为额外特征进行模型感知检测的潜力。我们发布了多LLM执行轨迹数据集和检测框架，以促进可重复研究。
## 112. `cs.AI` - GCGSim：一致于GED的对齐与未对齐子结构的分离用于图相似性学习 [PDF](https://arxiv.org/pdf/2511.19837), [HTML](https://arxiv.org/abs/2511.19837)
### Authors
Zhentao Zhan,Xiaoliang Xu,Jingjing Wang,Junmei Wang
### Background
GSC是一项基本的图相关任务，其中GED是一种常用的度量方法。GED通过图之间的最优对齐来确定，该对齐将每个图分割为对齐的（零成本）和未对齐的（具有成本的）子结构。尽管基于GNN的GED近似方法在学习节点嵌入后估算最终相似性方面表现出有效性，但研究者发现这种方法与GED的核心原则不匹配，这导致了两个关键限制：未能捕捉全局结构对应以实现最优对齐，以及由虚假节点信号导致的编辑成本误归因。
### Innovation
本文提出了一种名为GCGSim的GED一致的图相似性学习框架，该框架以图级匹配和子结构级别编辑成本为中心。GCGSim做出如下三个核心技术贡献：实现了一种新的GED一致性框架，能够有效学习分离和语义上有意义的子结构表示。
### Conclusion
在四个基准数据集上的广泛实验表明，GCGSim达到了最先进的性能。综合分析进一步验证了该框架能够有效学习分离和语义上有意义的子结构表示。
## 113. `cs.AI` - Agent0-VL：探索集成工具的自进化视觉-语言推理自代理 [PDF](https://arxiv.org/pdf/2511.19900), [HTML](https://arxiv.org/abs/2511.19900)
### Authors
Jiaqi Liu,Kaiwen Xiong,Peng Xia,Yiyang Zhou,Haonian Ji,Lu Feng,Siwei Han,Mingyu Ding,Huaxiu Yao
### Background
视觉-语言代理在多模态推理任务上取得了显著进展，但其学习仍受限于人类标注监督的局限性。近年来提出的一些自奖励方法试图通过让模型作为其自身的评判者或奖励提供者克服这一限制。然而，基于纯文本的自我评估难以验证复杂的视觉推理步骤，经常出现评估幻象。
### Innovation
本文提出了Agent0-VL，一种自进化的视觉-语言代理，通过集成工具推理实现持续改进。它不仅将工具使用融入推理，还将其融入自我评估和自我修复中，使模型能够通过证据驱动的分析进行自我反思、验证和修正其推理。Agent0-VL 统一了两个相互作用的角色：一个是执行多轮次工具集成推理的解题者，另一个是通过工具驱动的批判生成结构化反馈和精细自我奖励的验证者。这两个角色通过自进化推理循环相互作用，工具为基础的验证和强化学习共同调整推理和评估分布，实现稳定自我改进。
### Conclusion
通过零外部奖励进化，Agent0-VL 在几何问题解决和视觉科学分析实验中表现出优于基线模型 12.5% 的性能，实现了无需任何人工标注或外部奖励模型的持续自我改进。
## 114. `cs.AI` - LLM-EDT: Large Language Model Enhanced Cross-domain Sequential Recommendation with Dual-phase Training [PDF](https://arxiv.org/pdf/2511.19931), [HTML](https://arxiv.org/abs/2511.19931)
### Authors
Ziwei Liu,Qidong Liu,Wanyu Wang,Yejing Wang,Tong Xu,Wei Huang,Chong Chen,Peng Chuan,Xiangyu Zhao
### Background
跨域序列推荐(CDSR)通过从多个领域中引入信息来丰富用户-项目交互。然而，当前方法面临两个主要挑战：一是领域的不平衡问题，即在一个领域中的交互主导整个行为，导致难以捕捉其他领域的特定特征；二是转移问题，即在混合交互序列中难以捕捉用户的跨域偏好，导致特定领域的下一项预测性能不佳。尽管大型语言模型(LLMs)可以在一定程度上缓解这些问题，作为生成器和编码器，但当前的增强CDSR方法仍然未能很好地识别不相关噪声和粗糙的用户画像问题。
### Innovation
本文提出了一种名为LLM-EDT（Large Language Model Enhanced Cross-domain Sequential Recommendation with Dual-phase Training）的新方法。LLM-EDT通过提议使用可移植的项目增值器来自适应生成用户的潜在跨域行为，引入一种双阶段训练策略，强化领域特定线程的共享背景，以及设计一种领域感知的概况模块，来汇总每个领域的用户偏好并适当地聚合生成综合用户概况，以解决不平衡问题和剖面粗糙问题，同时尽量减少不相关噪声。
### Conclusion
在三个公共数据集上的实验验证了提出的LLM-EDT的有效性。为了便于可重复性，作者已在线发布详细的代码。
## 115. `cs.AI` - CodeFuse-CommitEval: 在代码提交信息和代码变更不一致性检测方面评估大语言模型的能力 [PDF](https://arxiv.org/pdf/2511.19875), [HTML](https://arxiv.org/abs/2511.19875)
### Authors
Qingyu Zhang,Puzhuo Liu,Peng Di,Chenxiong Qian
### Background
版本控制系统依赖于提交信息来传达代码变更的合理性，但这些信息往往质量低下，并且与变更后的代码存在不一致，即所谓的消息代码不一致性（MCI）。MCI误导了审查者，阻碍了维护，污染了研究数据集，并可能掩盖安全补丁。目前缺乏专门针对MCI检测的基准数据集。
### Innovation
本文提出了CODEFUSE-COMMITEVAL，这是首个专门用于MCI检测的大规模语言模型基准数据集。该数据集基于ApacheCM数据集构建，并通过规则引导的方式生成多种类型的不一致消息。该基准数据集经过两阶段验证以确保标注的准确性，并且通过六种最先进的开源大语言模型在不同增强策略下的表现，评估了模型在检测MCI方面的可靠性。
### Conclusion
研究结果表明，模型在检测不一致的提交比检测一致的提交更可靠（平均召回率85.95%，精度80.28%，特异性63.8%）。增强策略的效果各异：邻近上下文有助于大型模型但对小型模型增加噪声；少量提示提高了准确性和减少了 tokens使用量，但增加了普遍错误预测；思维链提高了精确度和特异性但降低了召回率并增加了 tokens的消耗。类型分析显示，组件、文件路径和操作不一致更容易被检测到，但意向层面的‘目的’不一致则具有更低的准确率和更高的 tokens成本。CODEFUSE-COMMITEVAL为衡量、比较和促进MCI检测提供了严谨的基础，强调了丰富上下文和平衡数据对于捕捉高级语义差距的必要性。
## 116. `cs.AI` - 基于AI/ML的HARQ-ACK有效载荷联合源信道编码 [PDF](https://arxiv.org/pdf/2511.19943), [HTML](https://arxiv.org/abs/2511.19943)
### Authors
Akash Doshi,Pinar Sen,Kirill Ivanov,Wei Yang,June Namgoong,Runxin Wang,Rachel Wang,Taesang Yoo,Jing Jiang,Tingfang Ji
### Background
从2G到5G，物理层输入的比特通常假定为均匀分布的。然而，上行链路中传输的混合自动重复请求确认（HARQ-ACK）比特是内在非均匀分布的。对于这样的源，通过结合深度学习技术的联合源信道编码可以获得显著性能提升。
### Innovation
本文采用一种新颖的“免费午餐”训练算法，学习基于转换器的编码器，并提出逐码字功率整形技术以在编码器中利用源先验知识，同时对HARQ-ACK分布的小变化具有鲁棒性。此外，为了解决因多次NACK错误导致的无线电链路失败问题，开发了Neyman-Pearson测试的扩展，用于具有多个信息比特的编码比特系统，以实现解码器中NACK比特的不等错误保护。进一步地，将所提编码器和解码器设计应用于5G新无线电（NR）兼容的上行链路设置，在衰落信道下实现最优接收机设计和低复杂度相干近似。
### Conclusion
研究表明，与NR基线相比，平均传输功率减少3-6 dB以达到目标错误率，同时最大传输功率减少2-3 dB，从而提供显著的覆盖增益和功率节省。
## 117. `cs.AI` - 基于零知识证明的模型可验证推理 [PDF](https://arxiv.org/pdf/2511.19902), [HTML](https://arxiv.org/abs/2511.19902)
### Authors
Yunxiao Wang
### Background
近年来，人工智能（AI）尤其是深度学习取得了广泛的应用，但模型的所有者不愿或不能公开其参数，这成为了一个根本性的挑战。由于这些参数代表了巨大的训练成本和宝贵的知识产权，使得透明验证变得困难。
### Innovation
本文提出了一种零知识框架，能够在不暴露模型内部参数的情况下验证深度学习推理的正确性。该框架基于递归组合的零知识证明，不需要可信设置，并支持线性和非线性神经网络层，包括矩阵乘法、规范化、softmax和SiLU。通过使用Fiat-Shamir技巧，该框架获得了具有常量大小证明的简洁不可交互知识证明（zkSNARK）。
### Conclusion
为了证明这种方法的实用性，本文将DeepSeek模型转换为完全SNARK可验证版本的ZK-DeepSeek，并通过实验展示了该框架在实际AI验证负载中的高效性和灵活性。
## 118. `cs.AI` - MAPS: 通过模块级接近调度保留视觉-语言表示以获得更好的视觉-语言-行动泛化 [PDF](https://arxiv.org/pdf/2511.19878), [HTML](https://arxiv.org/abs/2511.19878)
### Authors
Chengyue Huang,Mellon M. Zhang,Robert Azarcon,Glen Chou,Zsolt Kira
### Background
VLA模型从预训练的VLM继承了强大的先验知识，但简单的fine-tuning往往会破坏这些表示，导致泛化能力下降。现有方法如冻结模块或应用统一正则化虽然存在，但效果有限：冻结模块会过度限制适应性；统一正则化则忽略了VLA组件的不同作用。
### Innovation
提出了一种新颖的可信赖的VLA微调框架——MAPS（Module-Wise Proximity Scheduling），这种方法通过系统的分析发现了一个经验性的接近顺序，以平衡稳定性和灵活性。MAPS线性地调度了这一放松过程，使视觉编码器能够保持接近预训练先验，而语言层可以更自由地适应，这种方法无需额外的参数或数据，且可以无缝集成到现有的VLA系统中。
### Conclusion
MAPS在MiniVLA-VQ、MiniVLA-OFT、OpenVLA-OFT以及SimplerEnv、CALVIN、LIBERO等挑战性基准测试，以及在Franka Emika Panda平台上的实际评估中，均表现为更好的分布内和分布外性能提升（最多30%），实验结果强调了在VLM到VLA转移中，通过预训练VLM保留的接近作为简单有效的原则，以保持广泛的泛华性。
## 119. `cs.AI` - 使用强化学习优化磁共振成像中的翻转角度调度 [PDF](https://arxiv.org/pdf/2511.19941), [HTML](https://arxiv.org/abs/2511.19941)
### Authors
Shenjun Zhong,Zhifeng Chen,Zhaolin Chen
### Background
磁共振指纹技术(MRF)依赖于由可调采集参数生成的瞬态信号动力学，使得设计最优、稳健的序列成为一个复杂的高维顺序决策问题，比如优化关键参数之一，翻转角。强化学习（RL）提供了一种自动参数选择的方法，以优化可以最大化指纹区分性的脉冲序列。
### Innovation
本文提出了一个使用强化学习优化MRF中的翻转角度调度的框架，并展示了一个非周期模式的学习调度方案，提高了指纹的区分性。此外，RL优化的方案还可能减少重复时间，从而加速MRF的采集过程。
### Conclusion
研究表明，通过使用强化学习优化MRF中的翻转角度调度，不仅可以增强指纹的区分性，而且有可能减少数据采集时间，提高MRF的应用效率。
## 120. `cs.AI` - 边缘设备上高效部署大型模型的按需多任务稀疏性 [PDF](https://arxiv.org/pdf/2511.19986), [HTML](https://arxiv.org/abs/2511.19986)
### Authors
Lianming Huang,Haibo Hu,Qiao Li,Nan Guan,Chun Jason Xue
### Background
在资源受限的边缘平台部署大型模型需要低硬件成本，但优化个别任务的稀疏模式忽略了频繁任务切换中产生的显著I/O开销。已有方法侧重于优化单一任务的稀疏模式而没有考虑任务切换的开销问题。
### Innovation
该研究提出了一种按需多任务稀疏性框架，旨在通过最大化参数的重用减少切换成本。该方法将权重分解为可重用的块级单元，并且在不同任务间对齐稀疏结构以最大化重叠。通过仅加载下一任务所需的少量差异性块集，有效缓解了传统单块方法在冷启动时的延迟问题。
### Conclusion
在实际的自动驾驶平台上，该框架实现了比现有稀疏性方法更优的切换效率，平均加速任务切换速度超过6.6倍。
## 121. `cs.AI` - MambaEye：具有因果顺序处理的无输入尺寸依赖视觉编码器 [PDF](https://arxiv.org/pdf/2511.19963), [HTML](https://arxiv.org/abs/2511.19963)
### Authors
Changho Choi,Minho Kim,Jinkyu Kim
### Background
尽管多年来取得的进步，一种真正能够无视输入尺寸的视觉编码器一直难以实现，这正是人类视觉的基本特征。本文针对这一局限性，提出了MambaEye模型，这是一种新颖的因果顺序编码器，利用低复杂度和因果处理为基础的纯Mamba2骨干架构。
### Innovation
MambaEye的关键创新在于其使用了相対移动嵌入，这可以编码连续块之间的空间位移，为平移不变性提供强有力的归纳偏置，并使模型能够适应任意图像分辨率和扫描模式。MambaEye引入了一种新型的受扩散机制启发的损失函数，以提供密集且分步的监督，使模型能够随着获取更多的视觉证据而建立信心。
### Conclusion
MambaEye在一系列图像分辨率上均表现出稳健的性能，特别是在ImageNet-1K分类任务中的1536×1536分辨率上表现尤为出色，同时保持了与块数量的线性时间和内存复杂度。
## 122. `cs.AI` - Sundial基础模型在叶面积指数零样本转移能力中的应用 [PDF](https://arxiv.org/pdf/2511.20004), [HTML](https://arxiv.org/abs/2511.20004)
### Authors
Peining Zhang,Hongchen Qin,Haochen Zhang,Ziqi Guo,Guiling Wang,Jinbo Bi
### Background
该研究分析了时间序列基础模型在农业监测中预测叶面积指数（LAI）的零样本预测能力。研究基于HiQ数据集（2000-2022年美国数据），通过多种评估协议系统地比较了统计基线、完全监督的LSTM以及Sundial基础模型。
### Innovation
研究发现，在零样本设置下，Sundial基础模型可以在输入上下文窗口足够长的情况下超越完全训练的LSTM模型，特别是当覆盖超过一个或两个完整的季节周期时。这是首次证明通用基础模型可以在无需任何任务特定调整的情况下，在遥感时间序列预测中超越专门的监督模型。
### Conclusion
研究结果强调了预训练时间序列基础模型在农业和环境应用中作为即插即用地预测器的强大潜力。
## 123. `cs.AI` - 通过单一扰动劫持MLLMs决策链的可能性 [PDF](https://arxiv.org/pdf/2511.20002), [HTML](https://arxiv.org/abs/2511.20002)
### Authors
Changyue Li,Jiaying Li,Youliang Yuan,Jiaming He,Zhicong Huang,Pinjia He
### Background
传统的对抗性攻击主要集中在影响神经网络的单一决策上。然而，在现实世界中，模型往往是按一系列决策进行操作的，单独的错误较容易纠正，但链式错误可能导致严重风险。本文揭示了一种新的威胁：单一扰动可以操控整个决策链。
### Innovation
本文介绍了一种新的方法——语义感知通用扰动（SAUPs），这些扰动可以根据输入的语义导致不同的结果。为了克服优化挑战，开发了一个有效算法，该算法通过使用语义分离策略在归一化空间中搜索扰动。为了评估SAUPs的实际威胁，创建了一个新的具有精细语义注释的现实世界图像数据集RIST，并在三个多模态大语言模型上进行了广泛的实验，成功率达到70%，即使控制五个不同的目标也仅使用了一个对抗帧。
### Conclusion
实验结果表明，多模态大语言模型对这些扰动非常脆弱。当控制五个不同的目标时，使用单一对抗帧的成功率为70%。
## 124. `cs.AI` - Transformer模型的方向优化不对称性：一个合成的压力测试 [PDF](https://arxiv.org/pdf/2511.19997), [HTML](https://arxiv.org/abs/2511.19997)
### Authors
Mihir Sahasrabudhe
### Background
Transformer模型理论上是反转不变的，但实证研究表明自然语言中的反转会出现问题，而且近期有关大型语言模型时间不对称性的研究指出，实际数据集本身可能携带自己的时间方向。我们面临的问题是：方向性失败是源于语言统计特性还是模型架构本身？本文通过一个完全合成、熵控制的基准测试细化了这一模糊性，使用可调分支因子K的随机字符串映射来构建无条件熵的正向任务和有确定熵门槛的反转任务。该基准测试揭示了即使是从零开始训练的GPT-2模型也表现出一种强烈且可重复的方向优化差距，这远大于MLP在相同数据上训练的差距。此外，预训练初始化会改变优化行为但并不消除这种差距，而LoRA在高熵反转映射上遇到明显的容量障碍。这些结果将方向性摩擦标识为内在的、与因果Transformer训练相关的最小且不依赖于语言先验、标记频率或数据集级时间不对称性的特征。
### Innovation
本文提出了一种完全合成、熵控制的基准测试，旨在细致探究Transformer模型的方向优化不对称性。该基准使用可调分支因子K的随机字符串映射构建正向和反转任务，通过比较模型在不同任务上的表现揭示方向优化差距，进一步表明这种差距并非源于语言统计特性或数据集层面的时间性，而是与模型架构本身相关。
### Conclusion
该基准测试为理解现代序列模型中的方向性偏差提供了受控工具，并驱动了对为什么反转对于Transformer模型来说更为困难的深入机制性研究。
## 125. `cs.AI` - Popularity Bias Alignment Estimates [PDF](https://arxiv.org/pdf/2511.19999), [HTML](https://arxiv.org/abs/2511.19999)
### Authors
Anton Lyubinin
### Background
本文扩展了arXiv:archive/2404.12008中的Popularity Bias Memorization定理。背景在于原始定理主要针对特定度分布，本文则将其扩展至任意度分布。
### Innovation
本文对原始Popularity Bias Memorization定理进行了几方面扩展，包括：1) 延伸至任意度分布；2) 证明了顶部k奇异超平面的对齐性的上下界。
### Conclusion
本文通过扩展Popularity Bias Memorization定理，更加全面地分析了数据的对齐性，并提供了基于顶部k奇异超平面的对齐性估计。
## 126. `cs.AI` - EmoFeedback2：基于LVLM的奖励和文本反馈增强的连续情感图像生成 [PDF](https://arxiv.org/pdf/2511.19982), [HTML](https://arxiv.org/abs/2511.19982)
### Authors
Jingyang Jia,Kai Shu,Gang Yang,Long Xing,Xun Chen,Aiping Liu
### Background
连续情感图像生成（C-EICG）因其能够生成与用户描述和连续情感值相匹配的图像而快速兴起。然而，现有的方法缺乏对生成图像的情感反馈，限制了情感连续性的控制。此外，它们之间简单的情感与文本的对应关系未能根据图像内容自适应调整情感提示，导致情感准确性不足。
### Innovation
本文提出了一种基于强化学习的生成-理解-反馈新框架（EmoFeedback2），利用微调的大规模视觉语言模型（LVLM）的能力，为生成具有连续情感的高质量图像提供奖励和文本反馈。具体地，引入了一种情感感知的奖励反馈策略，微调的LVLM评估生成图像的情感值，并计算与目标情感的奖励，指导生成模型的强化学习微调，增强图像的情感连续性。同时设计了一种自我提升的文本反馈框架，LVLM迭代分析生成图像的情感内容，自适应地为下一轮提示生成改进建议，提高情感精密度。
### Conclusion
大量的实验结果表明，本方法能有效生成具有所需情感的高质量图像，在自定义数据集上优于现有最先进的方法。代码和数据集将很快发布。
## 127. `cs.AI` - BERT-APC：基于音乐语境推断的无参考自动音高校正框架 [PDF](https://arxiv.org/pdf/2511.20006), [HTML](https://arxiv.org/abs/2511.20006)
### Authors
Sungjae Kim,Kihyun Na,Jinyoung Choi,Injung Kim
### Background
现有的自动音高校正（APC）系统依赖于参考音高，这限制了它们的实际应用范围；或者使用简单的音高估计算法，这些算法往往无法保留声音的表达力和自然性。
### Innovation
提出了BERT-APC，一种新颖的无参考APC框架，能够在纠正音高错误的同时保持歌声的自然表达力。该框架包括一个新颖的静止音高预测器和一个上下文感知的音高预测器来估计目标音序，以及一个基于音符级别的纠正算法来修复音高错误。此外，还引入了一种可学习的数据增强策略，通过模拟现实的音调偏差模式来提高音乐语言模型的鲁棒性。
### Conclusion
BERT-APC在音符音高预测方面表现优于两个最近的歌唱声音转录模型，特别是在高度音调偏差样本中，在音高准确性方面优于第二好模型ROSVOT 10.49%。在MOS测试中，BERT-APC获得最高评分4.32 ± 0.15，远高于商用APC工具AutoTune (3.22 ± 0.18) 和 Melodyne (3.08 ± 0.18) 的评分，同时保持了保留表达性细微差别的能力。到目前为止，BERT-APC是第一个利用音乐语言模型来实现具有符号音乐上下文的无参考音高校正的模型。
## 128. `cs.AI` - WaymoQA: 用于自主驾驶中关键安全推理的多视图视觉问答数据集 [PDF](https://arxiv.org/pdf/2511.20022), [HTML](https://arxiv.org/abs/2511.20022)
### Authors
Seungjun Yu,Seonho Lee,Namho Kim,Jaeyo Shin,Junsung Park,Wonjeong Ryu,Raehyuk Jung,Hyunjung Shim
### Background
最近的多模态大规模语言模型（MLLMs）在理解驾驶场景方面表现出了强大的能力，引起了将其应用于自主驾驶的兴趣。然而，在安全关键场景中，避免一种交通风险可能会引发另一种风险，这种高级推理依然是一个重大挑战。这种推理仅靠前视摄像头单一视角是难以实现的，因此需要从多个视角获得全面的环境视图。
### Innovation
我们定义了一个新的任务——关键安全推理，通过多视角输入来解决这一挑战，并将其分解为两个阶段：首先解决当前的风险，然后减轻由此产生的决策风险。为此，我们引入了一个名为WaymoQA的数据集，该数据集包含35,000个人类标注的问题-答案对，涵盖复杂的高风险驾驶场景。该数据集包含图片和视频双模态的多项选择题和开放式问题格式。实验结果显示，在关键安全场景中，现有的MLLMs的表现不如普通场景，并且通过与WaymoQA进行微调可以显著提升它们的推理能力，突显了我们数据集在开发更加安全和更具有推理能力的驾驶代理方面的有效性。
### Conclusion
现有的大规模语言模型在安全关键场景中的表现不如普通场景，但通过我们的WaymoQA数据集进行微调可以显著提高它们的推理能力，这强调了我们的数据集在开发更安全和更具推理能力的驾驶代理方面的有效性。
## 129. `cs.AI` - 能源成本及环境变化中神经复杂性进化的演变 [PDF](https://arxiv.org/pdf/2511.20018), [HTML](https://arxiv.org/abs/2511.20018)
### Authors
Sian Heesom-Green,Jonathan Shock,Geoff Nitschke
### Background
认知缓冲假设(CBH)认为，更大的大脑是为了在多变的环境中增强生存而进化的。然而，更大的大脑也伴随着更高的能量需求，增加了额外的代谢负担。除了大脑的大小，大脑的组织结构在认知能力中起到关键作用。具有适合架构的大脑可能有助于缓解能量挑战。
### Innovation
本研究通过强化学习(Reinforcement Learning, RL)代理使用的人工神经网络(ANN)来研究环境波动性和能源成本如何影响神经复杂性的进化，其中神经复杂性用ANN的大小和结构来定义。研究结果表明，在能源限制下，更高的季节性导致了较小的ANN。这挑战了CBH，并支持了昂贵的大脑假设(EBH)，即高度季节性环境减少了净能量摄入，从而限制了大脑的大小。ANN的结构性复杂性主要作为一个副产品出现，其中能源成本促进了更高效的网络进化。
### Conclusion
这些结果强调了能源限制在塑造神经复杂性中的作用，为生物理论和能源高效机器人设计提供了体内外支持。
## 130. `cs.AI` - 城市环境中行人过街意图预测的多上下文融合变换器 [PDF](https://arxiv.org/pdf/2511.20011), [HTML](https://arxiv.org/abs/2511.20011)
### Authors
Yuanzhe Li,Hang Zhong,Steffen Müller
### Background
行人过街意图预测对于自动驾驶汽车提高行人安全和减少交通事故至关重要。然而，在城市环境中准确预测行人的意图仍然具有挑战性，因为众多因素影响行人的行为。
### Innovation
本文提出了一种多上下文融合变换器（MFT），利用涵盖行人类别上下文、环境上下文、行人定位上下文和车辆运动上下文的四个关键维度的多种数值上下文属性，以实现准确的行人意图预测。MFT 使用一种逐步融合策略，通过相互上下文内的注意力机制促进了每个上下文内的相互互动，从而促进特征序列的融合，并生成一个上下文特定表示。随后是跨上下文注意机制，它将特征通过一个全局CLS标记集成到跨上下文表示中。最后，导向的上下文内部注意力通过定向互动在每个上下文中细化上下文项目，而导向的跨上下文注意力则加强了全局CLS标记，通过定向信息传播促进多上下文融合，从而实现更深入、更有效的集成。
### Conclusion
实验结果验证了MFT的优越性，相较于现有技术方法，在JAADbeh、JAADall和PIE数据集上的准确率分别达到了73%、93%和90%。并进行了广泛的消融研究以探讨网络架构的有效性和不同输入上下文的贡献。
## 131. `cs.AI` - MFM-point: 多尺度流动匹配点云生成 [PDF](https://arxiv.org/pdf/2511.20041), [HTML](https://arxiv.org/abs/2511.20041)
### Authors
Petr Molodyk,Jaemoo Choi,David W. Romero,Ming-Yu Liu,Yongxin Chen
### Background
近年来，点云生成在3D生成建模方面引起了广泛关注。点基方法直接生成点云，不依赖于如潜在特征、网格或体素等其他表示方法，这种方法具有较低的训练成本和算法上的简化，但性能往往劣于基于表示的方法。
### Innovation
本文提出了一种名为MFM-Point的多尺度流动匹配框架，该框架显著提高了点基方法的可扩展性和性能，同时保持其简洁性和效率。该方法采用自上而下的生成策略，提升了生成质量和可扩展性，同时无需增加额外的训练或推理开销。为了在多尺度框架中保留无序点云的几何结构并保持不同分辨率之间的平滑一致分布转换，作者引入了一种结构化的下采样和上采样策略。
### Conclusion
实验结果表明，MFM-Point在点云生成方法中达到了最佳性能，并且能与其他基于表示的方法相媲美，在多类和高分辨率生成任务中表现出色。
## 132. `cs.AI` - 数字幽灵的形成：设计伦理的人工智能永久存在 [PDF](https://arxiv.org/pdf/2511.20094), [HTML](https://arxiv.org/abs/2511.20094)
### Authors
Giovanni Spitale,Federico Germani
### Background
随着人工智能技术的进步，现在可以通过聊天机器人、声音克隆和视频替身来模拟已故之人的数字形象。这些‘数字幽灵’正在从虚构走向商业现实，改变了人们哀悼和怀念的方式。
### Innovation
本文提出了一种九维度的数字死后技术分类法，并在此基础上提出了符合伦理的数字幽灵的要求：预先意愿、互相同意、透明且受限的数据使用、明确披露、限定目的与访问、家庭或遗产托管、最小的行为代理。
### Conclusion
本文主张通过专门的法规和专业指导原则来确保数字幽灵能帮助追忆而不沦为欺骗的形式。
## 133. `cs.AI` - 使用多模态融合网络的行人过街意图预测 [PDF](https://arxiv.org/pdf/2511.20008), [HTML](https://arxiv.org/abs/2511.20008)
### Authors
Yuanzhe Li,Steffen Müller
### Background
行人过街意图预测对于城市环境中自主车辆（AVs）的部署至关重要。理想的预测可以为自主车辆提供关键的环境提示，从而降低与行人相关的碰撞风险。然而，由于行人行为的多样性及其依赖于多种外部因素，这一预测任务具有挑战性。
### Innovation
本文提出了一种多模态融合网络，该网络利用来自视觉和运动分支的七种模态特征，旨在有效提取并整合不同模态下的互补提示。特别是，运动和视觉特征通过多个基于Transformer的提取模块从原始输入中提取出来。深度导向注意力模块利用深度信息引导对另一模态中的显著区域进行注意力关注，通过全面的空间特征交互。为了考虑不同模态和帧的重要性不同，设计了模态注意力和时序注意力机制，以有选择地强调信息性模态并有效捕获时序依赖关系。实验结果证明了所提出的网络的有效性，其性能优于基本方法。
### Conclusion
通过对JAAD数据集的广泛实验，验证了所提出网络的有效性，相比基线方法，取得了优越的性能。
## 134. `cs.AI` - R3A: 基于多智能体故障定位和随机树思维补丁生成的可靠RTL修复框架 [PDF](https://arxiv.org/pdf/2511.20090), [HTML](https://arxiv.org/abs/2511.20090)
### Authors
Zizhang Luo,Fan Cui,Kexing Zhou,Runlin Guo,Mile Xia,Hongyuan Hou,Yun Lian
### Background
RTL（寄存器传输级）修复对于硬件设计和验证至关重要。传统的自动程序修复方法使用固定模板定义搜索空间，虽然可以定位并修复一些具体的缺陷，但这些方法的可靠性较低，且只能处理有限类型的缺陷。大型语言模型虽然能够理解代码语义，但在处理RTL修复时存在固有的随机性和长输入上下文的挑战。
### Innovation
文章提出了一种基于大型语言模型的自动RTL程序修复框架——R3A。R3A通过引入随机树思维补丁生成方法来控制补丁生成代理，探索有效解决方案。该方法使用启发式函数采样搜索状态来平衡探索和利用，以提高可靠性。此外，R3A还提出了一种多智能体故障定位方法，用于识别故障候选点，进一步增强修复的可靠性。
### Conclusion
实验表明，R3A在给定时间内修复了RTL修复数据集中90.6%的缺陷，比传统方法和基于大型语言模型的方法修复更多（多出45%），且平均pass@5率为86.7%，显示出较高的可靠性。
## 135. `cs.AI` - LungEvaty：一种用于低剂量CT筛查肺癌风险预测的可扩展开源基于转换器的深度学习模型 [PDF](https://arxiv.org/pdf/2511.20116), [HTML](https://arxiv.org/abs/2511.20116)
### Authors
Johannes Brandt,Maulik Chevli,Rickmer Braren,Georgios Kaissis,Philip Müller,Daniel Rueckert
### Background
随着更多国家推出使用低剂量CT（LDCT）进行大规模筛查的肺癌风险评估项目，影像数据量的增加使得需要能够高效处理整个肺部影像的强大方法，以充分挖掘大规模筛查数据的潜力。现有的方法要么过度依赖于像素级注释，限制了可扩展性，要么将肺部分为片段处理，削弱了性能。
### Innovation
LungEvaty提出了一种全新的基于转换器的框架，用于预测单个LDCT扫描在1-6年内的肺癌风险。该模型直接从大规模筛查数据中学习，能够捕捉与恶性风险相关的全面解剖和病理特征。LungEvaty无需地区监督即可达到当前最先进水平的性能，并可选地通过解剖信息指导注意机制（AIAG）损失进一步优化。LungEvaty训练数据量超过90,000个CT扫描，其中包括超过28,000个用于微调和6,000个用于评估。
### Conclusion
LungEvaty提供了一种简单、数据效率高且完全开源的解决方案，为未来的纵向及多模态肺癌风险预测研究提供了可扩展的基础框架。
## 136. `cs.AI` - 细节中的魔鬼：开源权重大模型中的新兴不对齐、格式和连贯性 [PDF](https://arxiv.org/pdf/2511.20104), [HTML](https://arxiv.org/abs/2511.20104)
### Authors
Craig Dickson
### Background
先前的研究表明，将模型在窄领域中进行微调并使用错配的数据可能会导致广泛的存在不对齐现象，这种现象被称为‘新兴不对齐’（Emergent Misalignment）。尽管所有测试的模型都受到了新兴不对齐的影响，但不同模型的抗性不同。Qwen-2.5家族显示出相对较强的抵抗性，而GPT-4o则表现出最强的不对齐。作者旨在评估当前开放权重模型是否具有类似Qwen-2.5家族的抗性，并测量不同模型架构和规模下的抗不对齐能力。研究复现了在九种现代开放权重模型（Gemma 3和Qwen 3家族，参数从1B到32B）上进行不安全代码生成的效应。结果显示，经过微调的模型在不安全代码生成中的不对齐率为0.68%（相比之下，基础模型为0.07%），这一结果接近以前的开放模型结果的较低端，但远低于GPT-4o的20%。研究还发现，格式依赖性是一个关键性的弱点：要求JSON输出会将不对齐率翻倍（相比自然语言提示，从0.42%上升到0.96%），这暗示结构约束可能绕过了安全培训，减少了模型拒绝的灵活性。
### Innovation
研究确认了新兴不对齐现象在现代开源权重大模型中的可复制性，并且发现开放权重模型中的不对齐率低于私有系统。研究还发现了一个重要的格式依赖性弱点：对于JSON输出的要求显著增加了模型的不对齐率。
### Conclusion
研究结果表明，开源权重大模型中的新兴不对齐现象是可以被观测的，并且其不对齐率低于私有系统中的观察到的水平。此外，明确指出一些结构约束可能削弱安全培训的效果，必须进一步研究以提高模型的抗不对齐能力。
## 137. `cs.AI` - SEDA: 自适应实体为中心的数据增强方法提高基于格的不连续命名实体识别模型 [PDF](https://arxiv.org/pdf/2511.20143), [HTML](https://arxiv.org/abs/2511.20143)
### Authors
Wen-Fang Su,Hsiao-Wei Chou,Wen-Yang Lin
### Background
命名实体识别（NER）是自然语言处理中的关键任务，但对于跨句子的不连续实体，仍然是一个特别困难的问题。传统方法常常会出现文本分割不准确或遗漏跨句的实体，这严重影响了识别的准确性。因此，本文旨在解决不连续实体的分割和识别问题。通过实验发现，传统的分割方法难以捕捉跨句子的不连续实体，导致性能下降。
### Innovation
本文提出了一种自适应实体为中心的数据增强方法（SEDA），将其引入到基于格的模型中，以增强模型识别不连续实体的能力，并解决分割挑战。该方法利用了图像数据增强技术，如裁剪、缩放和填充，增强了模型的鲁棒性和灵活性。
### Conclusion
实验结果表明，传统的分割方法往往无法捕捉跨句的不连续实体，而我们的增强网格模型则显著提升了性能。在CADEC、ShARe13和ShARe14数据集上评估，整体F1分数提高了1-2.5%，对于不连续实体，F1分数提高了3.7-8.4%，证实了该方法的有效性。
## 138. `cs.AI` - 通过概念瓶颈模型实现可解释的视觉异常检测 [PDF](https://arxiv.org/pdf/2511.20088), [HTML](https://arxiv.org/abs/2511.20088)
### Authors
Arianna Stropeni,Valentina Zaccaria,Francesco Borsatti,Davide Dalle Pezze,Manuel Barusco,Gian Antonio Susto
### Background
近年来，视觉异常检测（VAD）由于其仅使用正常图像进行训练就能识别异常图像的能力而受到广泛关注。许多VAD模型在无监督的情况下运行，但仍能通过高亮图像中的异常区域提供视觉解释。然而，这些视觉解释虽然有用，但缺乏对用户的直接和语义上的解释。
### Innovation
本文提出将概念瓶颈模型（CBMs）扩展应用于VAD场景。通过学习有意义的概念，网络可以提供人类可解读的异常描述，提供新的、更具洞察力的异常解释方式。主要贡献在于：（i）开发了一个概念数据集，支持CBMs在VAD中的研究；（ii）改进了CBM架构，生成基于概念的和视觉的解释，实现了语义和定位解释的结合；（iii）引入了合成人工异常的流程，保持VAD对罕见异常样本依赖最小的原则。提出的CONVAD方法，在性能上与经典VAD方法相当，同时提供更丰富、概念驱动的解释，增强了VAD系统的可解释性和可信度。
### Conclusion
本文通过引入Concept-Aware Visual Anomaly Detection (CONVAD) 方法，解决了现有VAD方法在解释方面的不足，提供了一种新的、更富有洞察力的异常解释方式，同时保持了与经典VAD方法相当的性能水平，增强了系统的可解释性和用户信任。
## 139. `cs.AI` - OmniAlpha: 一个统一多任务的序列到序列的RGBA生成框架 [PDF](https://arxiv.org/pdf/2511.20211), [HTML](https://arxiv.org/abs/2511.20211)
### Authors
Hao Yu,Jiabo Zhan,Zile Wang,Jinglin Wang,Huaisong Zhang,Hongyu Li,Xinrui Chen,Yongxian Wei,Chun Yuan
### Background
尽管生成模型在RGB合成方面表现出色，但在现实世界的应用中需要对RGBA进行操作。这导致了一个碎片化的应用场景：专门为Alpha通道设计的单任务模型虽然能够处理Alpha通道，但缺乏灵活性；而统一的多任务框架则局限于RGB域。为了弥合这一关键差距，我们提出了OmniAlpha，这是一个统一的多任务生成框架，用于序列到序列的RGBA图像生成和编辑。
### Innovation
OmniAlpha 的架构包括了一个新的 RoPE 方法 MSRoPE-BiL，它具有双向扩展的层轴，能够使其扩散变换器（DiT）主干能同时处理多输入和目标 RGBA 层。为了支持这一框架，我们引入了一个名为 AlphaLayers 的新型数据集，包含 1,000 个多层三重组合，并通过一种新的自动化合成和过滤管道构建。通过将 OmniAlpha 跨 21 个不同的任务进行联合训练，实验表明我们的统一方法在多个指标上优于专门的强基线。最值得注意的是，OmniAlpha 在 AIM-500 上实现了 84.8% 的相对 SAD 减少，并在层条件完成中获得了超过 90% 的人类偏好。
### Conclusion
我们的研究证明，统一的多任务模型可以学习一个高级共享表示形式，这对于 RGBA 的生成来说是有利的，为更强大的、层感知的生成系统铺平了道路。
## 140. `cs.AI` - 在集中式和联邦优化中的动量限制 [PDF](https://arxiv.org/pdf/2511.20168), [HTML](https://arxiv.org/abs/2511.20168)
### Authors
Riccardo Zaccone,Sai Praneeth Karimireddy,Carlo Masone
### Background
近期的研究探讨了在局部方法中使用动量以提升分布式SGD的有效性。特别是在联邦学习（FL）中，动量看起来是一种缓解统计异质性影响的直观解决方案。尽管已有进展，但在去中心化场景中，只有部分工作节点在每个周期参与的情况下，动量是否能保证收敛仍然不清楚。
### Innovation
本研究分析了在周期性客户端参与下的动量，并理论证明了即使在减少步长情况下，动量仍然不可避免地受到统计异质性的影响。此外，任何比$?Theta(1/t)$更快减少的步长方案都会导致收敛到一个依赖于初始化和异质性上限的常数值。
### Conclusion
数值结果验证了理论分析，深度学习实验也确认了在现实设置中的重要性。
## 141. `cs.AI` - IDAP++: 通过滤波器级和层级优化提升基于发散的剪枝 [PDF](https://arxiv.org/pdf/2511.20141), [HTML](https://arxiv.org/abs/2511.20141)
### Authors
Aleksei Samarin,Artem Nazarenko,Egor Kotenko,Valentin Malykh,Alexander Savelev,Aleksei Toropov
### Background
该论文提出了一个新的神经网络压缩方法，该方法通过统一框架解决了滤波器和架构层面的冗余问题，该框架基于信息流分析。论文在设计时考虑了张量流发散的概念，该概念量化了信息在网络层间的变化，以此为基础开发了一个两阶段优化过程。
### Innovation
该研究提出了一种基于信息流发散的两阶段优化过程。第一阶段采用迭代的信息流发散感知剪枝方法，以识别和移除冗余滤波器，同时保持关键信息路径。第二阶段通过分析各层在信息传播中的贡献，选择性地去除效果最小的层。这种方法能够适应各种不同架构，包括卷积网络、变压器和混合设计。实验结果表明，这种结合方法在保持竞争力的同时实现了显著的模型压缩。该方法在参数减少方面与最先进的解决方案相符，并在各种现代神经网络架构中表现出色。
### Conclusion
该研究通过实验验证，展示了其方法在多种现代架构和数据集上的应用效果，证明了信息流发散不仅有效指导滤波器级和层级的优化，还能为资源受限环境的部署提供实际益处。
## 142. `cs.AI` - Beluga：基于CXL的可扩展和高效的大规模LLM KVCache管理内存架构 [PDF](https://arxiv.org/pdf/2511.20172), [HTML](https://arxiv.org/abs/2511.20172)
### Authors
Xinjun Yang,Qingda Hu,Junru Li,Feifei Li,Yuqi Zhou,Yicong Zhu,Qiuru Lin,Jian Dai,Yang Kong,Jiayu Zhang,Guoqiang Xu,Qiang Liu
### Background
随着大规模语言模型（LLM）模型尺寸的迅速增加和长上下文推理需求的提高，内存已成为GPU加速服务系统中的关键瓶颈。尽管GPU上的高带宽内存（HBM）可以提供快速的访问速度，但其有限的容量仍需要依赖主机内存（CPU DRAM）来支持更大的工作集，如KVCache。然而，由于CPU插槽上有限的内存通道数量，DRAM容量也受到了限制。目前的系统通常采用基于RDMA的异构内存池来缓解这一限制，但这种方式引入了如高访问延迟、复杂的通信协议和同步开销等重大挑战。为了解决这一问题，新的CXL技术为KVCache设计带来了新的机遇。
### Innovation
本文提出了名为Beluga的新型内存架构，该架构通过CXL交换机使GPU和CPU能够访问共享的大型内存池。通过在CXL传输介质上支持原生的加载/存储访问语义，Beluga设计提高了接近本地内存的延迟，同时减少了编程复杂性并减少了同步开销。文章针对CXL交换机为基础的内存池进行了一套系统化的表征，并提出了设计指南。针对Beluga，设计并实现了Beluga-KVCache系统，专门用于在LLM推理中管理大规模KVCache。
### Conclusion
贝尔格拉利用CXL交换机直接实现了GPU对大规模内存池的访问，相比于基于RDMA的解决方案，Beluga-KVCache在vLLM推理引擎中的初始令牌时间（TTFT）减少了89.6%，吞吐量提高了7.35倍。据我们所知，贝尔格拉是首个通过CXL交换机实现GPU直接访问大规模内存池的系统，标志着向低延迟和共享访问大量内存资源的重要一步。
## 143. `cs.AI` - 人类-计算机互动预测心理健康 [PDF](https://arxiv.org/pdf/2511.20179), [HTML](https://arxiv.org/abs/2511.20179)
### Authors
Veith Weilnhammer,Jefferson Ortega,David Whitney
### Background
全球范围内导致残疾的主要原因——心理健康疾病，其评估仍是一个关键障碍，妨碍了可访问和公平的心理健康服务。现有方法往往难以捕捉个体心理健康状态的变化和多维度特征。
### Innovation
该研究引入了MAILA框架，利用机器学习从数字活动中推断出潜在的心理状态。通过训练，MAILA能够预测超过130万条来自2万名参与者（包括9000人次在线活动数据、2000名纵向评估个体及1500名抑郁症患者和500名强迫症患者）的心理健康自我报告。该模型能够动态跟踪心理健康状态，跨不同环境推广，并在群体级预测心理健康时接近天花板水平的准确性。研究结果强调日常的人机互动可以作为可信赖的动力、实时和最大规模的心理健康评估工具。
### Conclusion
这些日常的人机互动能够实现无成本的心理状态解码，为精准医学和公共卫生设立了新的标准，同时也引发了关于在线隐私、自主权和行为主体权利的重要问题。
## 144. `cs.AI` - DUO-TOK：语音伴奏生成的双重轨道语义音乐分词器 [PDF](https://arxiv.org/pdf/2511.20224), [HTML](https://arxiv.org/abs/2511.20224)
### Authors
Rui Lin,Zhiyue Wu,Jiahe Le,Kangdi Wang,Weixiong Chen,Junyu Dai,Tao Jiang
### Background
现有的音乐生成系统（lyrics-to-song）面临着重建质量与语言模型可学习性之间的日益紧张关系。现有的音码器或优先高保真重建而使用难以建模的声学标记，或压缩为易于语言模型处理但具有失真的语义标记。它们很少注意音轨结构对分词的影响。
### Innovation
Duo-Tok采用了一种基于四阶段、SSL为中心的方法。首先，通过大型音频数据预先训练BEST-RQ样式的编码器；随后，通过高斯替代噪声和多任务监督稳定并分解表示；之后，冻结编码器采用SimVQ为基础的双重码本学习编码；最后，在离散标记之上训练潜在扩散解码器。Duo-Tok使得数据压缩速度为0.75 kbps的情况下，重建和生成模型之间的数据效率边界发生了变化，同时保持与最先进的音乐分词器相当的重建质量。
### Conclusion
Duo-Tok在比较的音码器中实现了最高的音乐标记精度（AP）和最低的词汇归一化语言模型困惑度（perplexity），同时保持与最先进的音乐分词器相当的重建质量。
## 145. `cs.AI` - Uplifting Table Tennis: A Robust, Real-World Application for 3D Trajectory and Spin Estimation [PDF](https://arxiv.org/pdf/2511.20250), [HTML](https://arxiv.org/abs/2511.20250)
### Authors
Daniel Kienzle,Katja Ludwig,Julian Lorenz,Shin'ichi Satoh,Rainer Lienhart
### Background
从标准单目视频中精确获取乒乓球的3D运动是一个具有挑战性的问题。现有基于合成数据的方法难以适应真实世界中的杂乱和不完美的球与台面检测。这是因为实际视频中缺乏3D地表真实轨迹和旋转注释。
### Innovation
本文提出了一种新颖的两阶段管道，将问题分为前端感知任务和后端2D到3D提升任务。前端组件通过我们新创建的TTHQ数据集中的丰富2D监督进行训练，而后端提升网络则仅在符合物理真实性的合成数据上进行训练。特别地，重新设计了提升模型以对常见的弱检测和不同帧率等真实世界病态具有鲁棒性。此外，通过集成球体检测器和台面关键点检测器，本方法将证明性提升方法转变为用于3D乒乓球轨迹和旋转分析的实际、鲁棒且高性能的端到端应用。
### Conclusion
通过上述方法，我们的研究提高了评估3D乒乓球轨迹和旋转变量的准确性和可靠性，推动了这一领域技术的实际应用。
## 146. `cs.AI` - 当数据稀缺，智慧地提示... 低资源环境中的语法纠错方法 [PDF](https://arxiv.org/pdf/2511.20120), [HTML](https://arxiv.org/abs/2511.20120)
### Authors
Somsubhra De,Harsh Kumar,Arun Prakash A
### Background
语法错误纠正（GEC）是自然语言处理中的一个重要任务，旨在自动检测和纠正文本中的语法错误。虽然基于变压器的模型和大规模注释数据集的最新进展显著提高了像英语这样的高资源语言的GEC性能，但对于大多数印地语族语言来说，由于资源有限、语言多样性复杂以及复杂的形态学，GEC仍然是一个具有挑战性的任务。
### Innovation
本文探讨了使用最先进的大型语言模型（LLMs）如GPT-4.1、Gemini-2.5和LLaMA-4结合少量示例策略进行提示的方法，以适应低资源环境。研究发现，即使是基本的提示策略，如零样本和少量样本方法，也能使这些LLMs远胜过微调的印地语模型，从而展示了当前LLMs在GEC中的出色多语言泛化能力。精心设计的提示和轻量级适应可以显著提升多种印地语的质量。
### Conclusion
实验结果显示，精心设计的提示和轻量级适应显著提高了多种印地语的纠正质量。我们在共享任务中取得了领先地位——在泰米尔语（GLEU: 91.57）和印地语（GLEU: 85.69）中排名第一，在泰卢固语（GLEU: 85.22）中排名第二，在孟加拉语（GLEU: 92.86）中排名第四，在马拉雅拉姆语（GLEU: 92.97）中排名第五。这些发现突显了提示驱动的NLP技术的有效性，并强调了大规模LLMs在多语言GEC中的潜力，以弥合资源差距。
## 147. `cs.AI` - 利用权重信号 - 预测和提高强化学习中的泛化能力 [PDF](https://arxiv.org/pdf/2511.20234), [HTML](https://arxiv.org/abs/2511.20234)
### Authors
Olivier Moulin,Vincent Francois-lavet,Paul Elbers,Mark Hoogendoorn
### Background
强化学习（RL）代理在不同环境中的泛化能力是一个关键问题，因为这些代理倾向于过度拟合其训练环境。
### Innovation
引入了一种新方法，通过预测RL代理的内部权重来评估其泛化能力，并基于此提出了一些改良的Proximal Policy Optimization (PPO)损失函数的变化，以提升使用此升级版本训练的代理的泛化能力。
### Conclusion
实验结果表明，改进后的PPO算法产生的代理在泛化能力上比原始版本更强。
## 148. `cs.AI` - 在识别动作时，LMMs 在检测关键交互事件方面遇到困难 [PDF](https://arxiv.org/pdf/2511.20162), [HTML](https://arxiv.org/abs/2511.20162)
### Authors
Daniel Harari,Michael Sidorov,Liel David,Chen Shterental,Abrham Kahsay Gebreselasie,Muhammad Haris Khan
### Background
大型多模态模型（LMMs）在图像和最近的视频现实视觉任务中表现出色。例如，给定一个视频序列，这些模型能够详细描述物体、周围环境和动态动作。然而，这些模型在理解这些视觉输入的实际意义方面存在局限。研究者针对手部与物体交互序列，探索了模型在何时何地开始或结束交互方面的表现。
### Innovation
研究者首次引入了一个大规模数据集，包含来自 Something-Something-V2 数据集的超过 20,000 个标注的交互事件。250 名 AMTurk 人类标注者标注了关键交互事件，特别是物体和执行者何时接触（'接触'）或脱离（'脱离'）。研究使用两个 LMMs (Qwen-2.5VL 和 GPT-4o) 分析具有单一事件的短视频。
### Conclusion
尽管模型可以准确命名目标物体，识别动作并提供连贯的理由，但它们在识别交互开始或结束的帧以及在场景中定位事件方面始终表现出失败。研究结果表明，模型在识别物理接触的时间和位置时缺乏所需的感知基础，这限制了它们对动态场景的深入理解。
## 149. `cs.AI` - XiCAD: Da Vinci Xi用户界面中的摄像机激活检测 [PDF](https://arxiv.org/pdf/2511.20254), [HTML](https://arxiv.org/abs/2511.20254)
### Authors
Alexander C. Jenke,Gregor Just,Claas de Boer,Martin Wagner,Sebastian Bodenstedt,Stefanie Speidel
### Background
机器人辅助微创手术依赖于内窥镜视频作为唯一的术中视觉反馈。达芬奇Xi系统在图形用户界面（UI）上叠加显示每个机械臂的状态，包括内窥镜臂的激活情况。检测到这种激活状态可以提供关键元数据，如摄像头运动信息，这些信息能够支持各种下游手术数据科学任务，比如器械追踪、技能评估或摄像头控制自动化。
### Innovation
开发了一个基于ResNet18卷积神经网络的轻量级管道，用于自动识别达芬奇Xi UI中摄像头瓷砖的位置和激活状态。模型通过SurgToolLoc数据集的手动标注数据进行微调，并在超过7万个图像帧的三个公共数据集上进行了评估。
### Conclusion
提出的管道实现了可靠、实时从手术视频中提取摄像头激活元数据的能力，促进自动预处理和多样化的下游应用场景。所有代码、训练模型和标注数据均已公开提供。
## 150. `cs.AI` - 基于物理引导的空间-时间解耦的可解释空气污染预报 [PDF](https://arxiv.org/pdf/2511.20257), [HTML](https://arxiv.org/abs/2511.20257)
### Authors
Zhiguo Zhang,Xiaoliang Ma,Daniel Schlesinger
### Background
准确且可解释的空气污染预测对于公共健康至关重要，但大多数模型在性能和可解释性之间存在权衡。现有的大多数空气污染预测模型难以同时兼顾高预测准确性和易于理解的特性，这使得人们难以从中提取有用的信息并据此采取措施。
### Innovation
本文提出一种基于物理引导的空间-时间可解释性设计学习框架。该模型将空气污染物的空间-时间行为分解为两个透明且可加性的模块。第一个模块是物理引导的传输内核，它根据风力和地理条件设置了定向权重（对流）。第二个模块是一种可以解释的注意力机制，该机制学习局部响应并将未来的浓度归因于特定的历史滞后和外生驱动因素。该研究在斯德哥尔摩地区的多组数据集上展示了其模型的一致性能优于最先进的基线方法。
### Conclusion
该模型在保持高度预测性能的同时，实现了空间-时间的可解释性，为实际应用中的空气质量管理提供了更可靠的基础。
## 151. `cs.AI` - LLMs能否进行（个性化）访问控制决策？ [PDF](https://arxiv.org/pdf/2511.20284), [HTML](https://arxiv.org/abs/2511.20284)
### Authors
Friederike Groschupp,Daniele Lain,Aritra Dhar,Lara Magdalena Lazier,Srdjan Čapkun
### Background
传统的应用程序和新兴的基于代理的系统都依赖于精确的访问控制决策来确保安全性。这些决策通常由用户在应用程序安装期间或在运行时做出。然而，随着系统复杂性和自动化程度的增加，这些决策过程增加了用户的认知负担，这可能导致次优化甚至随意的访问控制决策。
### Innovation
本文提出了利用大型语言模型（LLMs）的处理和推理能力，使动态、上下文相关的访问控制决策与用户的安全偏好保持一致的新方法。通过用户研究，收集了307条自然语言隐私声明和14,682条用户的访问控制决策，并与两种版本的LLM（通用和个性化）所作出的决策进行了比较。
### Conclusion
研究结果表明，LLMs能够很好地反映用户偏好，相比多数用户的决策，准确率达到86%。研究还揭示了一种重要的权衡：尽管向LLM提供用户特定的隐私偏好可提高与个别用户决策的一致性，但遵循这些偏好也可能违反一些安全最佳实践。基于这些发现，我们讨论了设计和风险权衡，以实现一个平衡个性化、安全性和实用性的自然语言访问控制系统的方案。
## 152. `cs.AI` - HVAdam：一种全维度自适应优化器 [PDF](https://arxiv.org/pdf/2511.20277), [HTML](https://arxiv.org/abs/2511.20277)
### Authors
Yiheng Zhang,Shaowu Wu,Yuanzhuo Xu,Jiajun Wu,Shang Xu,Steve Drew,Xiaoguang Niu
### Background
自适应优化器如Adam在大规模模型训练（如大型语言模型和扩散模型）中取得了巨大成功，但往往会比非自适应方法（如CNN中的SGD）泛化性能更差。自适应预条件在其中扮演了关键角色，限制了优化器适应多种优化场景的能力。
### Innovation
提出了一种名为Anon的新优化器，具备连续可调的自适应性，能够在类似SGD和Adam的行为之间进行插值，甚至超越两者。为确保全范围自适应性收敛，引入了增量延迟更新（IDU），这是一种比AMSGrad硬最大跟踪策略更灵活的机制，增强了对梯度噪声的鲁棒性。理论确保了在凸性和非凸性设置下的收敛性。实验结果显示Anon在代表性图像分类、扩散和语言模型任务中性能优于最先进的优化器。
### Conclusion
自适应性可以作为有价值的可调设计原理。Anon统一并可靠地桥接了经典与现代优化器之间的差距，并超越了它们的优点。
## 153. `cs.AI` - 语言模型中决策几何学 [PDF](https://arxiv.org/pdf/2511.20315), [HTML](https://arxiv.org/abs/2511.20315)
### Authors
Abhinav Joshi,Divyanshu Bhatt,Ashutosh Modi
### Background
大型语言模型（LLMs）在多种任务中表现出强大的泛化能力，但其内部决策机制仍然不透明。本文通过研究LLMs潜在表示的几何特征，特别是聚焦于多项选择题回答（MCQA）任务中的决策动态，探讨其内部工作原理。
### Innovation
通过对28个开源权重转换器模型的大规模研究，使用多种估计器估计各层的内在维度（ID），并量化每层在MCQA任务上的性能。结果表明，早期层在低维流形上操作，中间层扩展该空间，后期层再次压缩其至决策相关信息的表示。这揭示了LLMs隐式地将语言输入投影到与特定任务决策相匹配的结构化低维流形上的机制，为语言模型中的泛化和推理提供了新的几何见解。
### Conclusion
研究发现，LLMs内在地学习将语言输入投影到与特定任务决策相匹配的结构化、低维流形上，这意味着在语言模型中泛化和推理的出现具有几何意义。
## 154. `cs.AI` - Lipschitz约束网络用于一揽子稀疏视图CT重建 [PDF](https://arxiv.org/pdf/2511.20296), [HTML](https://arxiv.org/abs/2511.20296)
### Authors
Baoshun Shi,Ke Jiang,Qiusheng Lian,Xinran Yu,Huazhu Fu
### Background
尽管基于深度学习的稀疏视图计算机断层扫描（SVCT）重建算法取得了显著进展，但仍存在两个主要限制：（i）由于深度展开算法中优先网络的经验设计，难以明确证明它们满足利普西兹约束；（ii）针对不同视图的多个设置需要训练多个单独的模型，导致存储成本高昂，影响临床应用。
### Innovation
提出了一种明确可证明的利普西兹约束网络，称为LipNet，并将一个显式提示模块集成其中，以区分不同稀疏采样设置的知识，使得在单一模型内处理多种稀疏视图配置成为可能。此外，开发了一种用于稀疏视图CT重建的节省存储的深度展开框架，称为PromptCT，将LipNet嵌入其中以确保其对应迭代算法的收敛性。
### Conclusion
在模拟和实际数据实验中，PromptCT在多种视图的SVCT重建中表现出色，实现了更高的重建质量和更低的存储成本。从理论层面，明确证明了LipNet的边界的性质，进一步证明了其利普西兹连续性，并分析了所提迭代算法的收敛性。相关数据和代码已公开。
## 155. `cs.AI` - 使用PID-CNN实现单目视觉目标的3D运动感知 [PDF](https://arxiv.org/pdf/2511.20332), [HTML](https://arxiv.org/abs/2511.20332)
### Authors
Shi Jiazhao,Pan Pan,Shi Haotian
### Background
本文训练了一个网络，用于识别和感知双目视点目标的三维运动信息，能够提供实时的三维坐标、速度和加速度等参数，并具备基本的空间和时间感知能力。从PID的角度理解神经网络适应非线性问题的能力，将单层神经网络视为利用二阶差分方程和非线性来描述局部问题，而多层网络则通过多次转换来实现从原始表示到所需表示的过渡。
### Innovation
设计了一个相对较小的PID卷积神经网络，总共有17层和413,000个参数。通过连接和池化的方法简单但实用地利用特征重用。该网络使用模拟随机移动球的数据集进行训练和测试，实验结果表明预测精度接近输入图像分辨率可表示的上限。分析了实验结果和误差，探讨了高维卷积算法在提高计算效率和特征空间利用率方面的优势，及使用PID信息实现记忆和注意力机制的潜力。
### Conclusion
本文分析了实验结果和误差，结合高维卷积在提高计算效率和特征空间利用方面的好处，讨论了利用PID信息实现记忆和注意力机制的前景。同时也指出了现有不足和可能改进的方向。
## 156. `cs.AI` - 通过剪枝遗忘：连接基数估计中的数据删除 [PDF](https://arxiv.org/pdf/2511.20293), [HTML](https://arxiv.org/abs/2511.20293)
### Authors
Chaowei He,Yuanjun Liu,Qingzhi Ma,Shenyuan Ren,Xizhao Luo,Lei Zhao,An Liu
### Background
在多表关系数据中，基数估计（CE）系统中的机器卸载面临着独特的挑战，主要是由于复杂的数据分布依赖性。具体来说，核心的卸载操作数据删除，在基数估计模型中面临三个主要挑战：属性级别的敏感性、跨表传播以及由于删除引起的领域消失，这会导致在多对多连接中的严重高估。
### Innovation
我们提出了基数估计剪枝（CEP），这是首个专为多表学习基数估计系统设计的卸载框架。CEP引入了分布敏感剪枝方法，通过构建半连接删除结果并计算敏感性评分以指导参数修剪，以及领域剪枝方法，完全去除由删除操作消失的价值域。
### Conclusion
我们使用最先进的架构NeuroCard和FACE在IMDB和TPC-H数据集上评估了CEP。结果表明，在多表场景中，CEP始终能够实现最低的Q误差，特别是在高删除比例的情况下，常常优于重新训练。此外，CEP大幅减少了收敛迭代次数，计算开销仅为微不足道的0.3%-2.5%的微调时间。
## 157. `cs.AI` - RIS辅助下行尖叉天线系统：基于GNN的优化方法 [PDF](https://arxiv.org/pdf/2511.20305), [HTML](https://arxiv.org/abs/2511.20305)
### Authors
Changpeng He,Yang Lu,Yanqing Xu,Chong-Yung Chi,Bo Ai,Arumugam Nallanathan
### Background
本文探讨了RIS辅助的多波导尖叉天线(PA)系统(PASS)在多用户下行链路信息传输中的应用，动机是研究新兴PASS和RIS集成对无线通信的潜在影响。首先，本文在考虑PA移动范围、总功率预算和RIS元素可调相位约束的框架下，统一形式化了吞吐量加权和能量效率最大化问题。接着，基于RIS辅助PASS的图结构拓扑，提出了一个创新的三阶段图形神经网络(GNN)，第一阶段根据用户位置学习PA位置，第二阶段根据综合信道条件调整RIS相位，最终确定波束赋形向量。
### Innovation
本文提出了一种基于GNN的优化方法，旨在通过无监督训练和整合凸优化的三种实施策略，在推理时间与解决方案最优性的权衡中提供优化。该方法具有泛化能力、良好的性能可靠性及实时适用性。
### Conclusion
大量的数值结果验证了所提出的GNN的有效性，并展示了其独特的泛化能力、良好的性能可靠性和实时适用性。同时，分析了关键参数对RIS辅助PASS的影响。
## 158. `cs.AI` - 超越组件：基于奇异向量的转换器电路解释 [PDF](https://arxiv.org/pdf/2511.20273), [HTML](https://arxiv.org/abs/2511.20273)
### Authors
Areeb Ahmad,Abhinav Joshi,Ashutosh Modi
### Background
基于变换器的语言模型表现出复杂的分布行为，但其内部计算机制仍然不甚了解。现有的机制解释方法通常将注意力头和多层感知器（MLPs）（转换器架构的基本构建块）视为不可分割的整体，忽略了它们内部可能存在的功能子结构。
### Innovation
本文引入了一种更为精细的观点，将这些组件分解为正交的奇异方向，揭示了单个头或MLP内部的叠加和独立计算。我们的研究发现，以前识别的经典功能头，如“命名搬运工”（Name Mover），编码了多种重叠的亚功能，这些亚功能与不同的奇异方向对齐。先前识别的作为电路元件的计算图节点，在特定低秩方向上表现出强烈的激活现象，表明有意义的计算存在于紧凑的子空间内。虽然一些方向仍难以完全解释，但研究结果表明，变换器的计算是比之前假设的更为分布化、结构化和组合的。
### Conclusion
我们的研究为细粒度机制解释和对模型内部结构的更深入理解开辟了新的途径，表明变换器计算结构比以往认为的更加分布化、结构化和组合化。
## 159. `cs.AI` - 从被动感知到主动记忆：基于粗粒度注释的弱监督图像操纵定位框架 [PDF](https://arxiv.org/pdf/2511.20359), [HTML](https://arxiv.org/abs/2511.20359)
### Authors
Zhiqing Guo,Dongdong Xi,Songlin Li,Gaobo Yang
### Background
图像操纵定位（IML）面临注释成本和精细定位准确性的基本权衡。现有完全监督的IML方法依赖于密集的像素级掩码注释，这限制了其在大规模数据集或真实世界中的扩展性。相比之下，现有大多数弱监督IML方法基于图像级标签，大大降低了注释劳动强度，但通常缺乏精确的空间定位能力。
### Innovation
本文提出了一种新颖的弱监督图像操纵定位框架BoxPromptIML，该框架通过粗粒度区域注释策略生成相对准确的操纵掩码，从而有效平衡注释成本和定位性能。进一步设计了一种高效的轻量级学生模型，通过来自固定教师模型的知识蒸馏学习进行精细定位，同时采用灵感来源于人类潜意识记忆机制的特征融合模块，在实时观测线索的引导下，主动与历史原型模式进行结合，这种策略能够实现知识的动态重拾，显著增强定位准确性和鲁棒性。
### Conclusion
实验结果表明，BoxPromptIML在多种分布内和分布外数据集上优于或可与完全监督模型媲美，同时保持了强泛化性、低注释成本和高效的部署特性。
## 160. `cs.AI` - 软适应性策略优化 [PDF](https://arxiv.org/pdf/2511.20347), [HTML](https://arxiv.org/abs/2511.20347)
### Authors
Chang Gao,Chujie Zheng,Xiong-Hui Chen,Kai Dang,Shixuan Liu,Bowen Yu,An Yang,Shuai Bai,Jingren Zhou,Junyang Lin
### Background
强化学习（RL）在增强大型语言模型（LLMs）的推理能力中扮演着越来越重要的角色，然而平滑且高效的策略优化仍然是一个挑战。在由专家混合模型组成的系统中，标记级别的重要性比率往往会表现出很高的变异，导致更新不稳定。现有的基于组的策略优化方法，如GSPO和GRPO，通过硬剪裁来缓解这个问题，这使得保持稳定性和有效学习变得困难。
### Innovation
我们提出了软适应性策略优化（SAPO），它用一种平滑的、温度控制的门控机制替换了硬剪裁，能够适当地衰减偏离策略的更新，同时保留有用的学习信号。与GSPO和GRPO相比，SAPO在序列级上具有连贯性，但其软门控形成了一个连续的信任区域，避免了GSPO使用的一种脆弱的硬剪裁带。当序列中包含少数高度偏离策略的标记时，GSPO会抑制整个序列的梯度，SAPO则只对违规的标记进行软件权重下降处理，保留邻近策略标记的学习信号，从而提高样本效率。SAPO用平滑、温度控制的缩放替换了硬标记级剪裁，使得更新更具信息量和稳定性。
### Conclusion
SAPO在数学推理基准测试中表现出更好的训练稳定性和更高的Pass@1性能。我们使用SAPO来训练Qwen3-VL模型系列，结果显示SAPO在不同任务和不同模型规模上都表现出了一致的性能提升。总的来说，SAPO提供了一种更为可靠、可扩展且有效的RL训练优化策略，适用于大型语言模型。
## 161. `cs.AI` - 短距离Oversquashing [PDF](https://arxiv.org/pdf/2511.20406), [HTML](https://arxiv.org/abs/2511.20406)
### Authors
Yaaqov Mishayev,Yonatan Sverdlov,Tal Amir,Nadav Dym
### Background
消息传递神经网络（MPNNs）广泛用于图上的学习，但由于oversquashing现象的限制，它们在处理长距离信息方面能力有限。对此现象，一些研究者主张使用Graph Transformers作为更好的替代方案，而另一些人则建议可以在MPNN框架内通过虚拟节点或其他重连技术来缓解这一限制。
### Innovation
本文的研究者发现oversquashing不局限于长距离任务，在短距离问题中也会出现。此外，研究分离了oversquashing背后的两种机制：瓶颈现象和梯度消失现象，并指出瓶颈现象在低范围设置中也会出现。研究还表明现有的oversquashing解释无法捕捉短范围瓶颈效应，添加虚拟节点不能解决，而Transformers在这些任务中表现良好，成为比专门设计的MPNNs更吸引人的解。
### Conclusion
研究认为，Transformers是解决oversquashing更为有力的解决方案，相比专门设计的MPNNs更具吸引力。
## 162. `cs.AI` - Java中的自动单元测试生成与评估：AgoneTest框架 [PDF](https://arxiv.org/pdf/2511.20403), [HTML](https://arxiv.org/abs/2511.20403)
### Authors
Andrea Lops,Fedelucio Narducci,Azzurra Ragone,Michelantonio Trizio,Claudio Barto
### Background
单元测试是软件开发中的一个关键但耗费资源的步骤，确保独立的代码单元能够正常工作。这项研究介绍了一个自动评估框架——AgoneTest，用于评定大型语言模型（LLMs）生成的Java单元测试。AgoneTest的目标是通过标准化的端到端评估管道支持研究人员和开发人员在现实条件下比较不同LLMs和提示策略的表现，而不是提出新的测试生成算法。
### Innovation
AgoneTest引入了一个集成先进评估指标（如变异得分和测试异味）的框架，以进行全面评估。实验结果表明，对于能够编译的测试用例，由LLMs生成的测试可以达到甚至超越人工编写的测试在覆盖率和缺陷检测方面的效果。此外，改进的提示策略也被证明有助于提高测试的质量。
### Conclusion
AgoneTest揭示了LLMs在软件测试中的潜力，并为未来模型设计、提示工程和测试实践改进提供见解。
## 163. `cs.AI` - 基于潜在扩散模型的高效快速生成式歌唱人声分离 [PDF](https://arxiv.org/pdf/2511.20470), [HTML](https://arxiv.org/abs/2511.20470)
### Authors
Genís Plaja-Roglans,Yun-Ning Hung,Xavier Serra,Igor Pereira
### Background
音乐混音中的单个元素提取是音乐制作和实践中的一个重要工具。虽然优化的神经网络可以将混音频谱图转化为单个声源，但音乐信号中的声源重叠和相关性构成了一个固有的挑战。同时，获取混音中的所有声源以训练这些系统非常复杂。虽然有针对这些挑战的生成方法，但分离性能和推理效率依然有限。
### Innovation
本文研究了扩散模型的潜力以解决上述问题，特别是在只使用对应的独立人声和混音训练下进行生成式歌唱人声分离。通过利用潜在扩散模型，系统生成样本并随后将其解码为音频，从而实现高效的优化和更快的推理。该系统仅使用公开数据进行训练，我们在信号质量指标和干扰去除方面超过了现有生成式分离系统，同时，我们也提供了一项关于潜在编码器噪声鲁棒性的研究，揭示了其在该任务中的潜力。
### Conclusion
我们发布了一个模块化工具包，供进一步对该领域进行研究。
## 164. `cs.AI` - 使用单一标记提示生成、评估和解释小说家风格 [PDF](https://arxiv.org/pdf/2511.20459), [HTML](https://arxiv.org/abs/2511.20459)
### Authors
Mosab Rezaei,Mina Rajaei Moghadam,Abdul Rahman Shaikh,Hamed Alhoori,Reva Freedman
### Background
近年来，大型语言模型的进步为修辞学——研究写作风格和作者身份的学科——带来了新的机遇。然而，两大挑战始终存在：在没有成对数据的情况下训练生成模型，以及在不完全依赖人工判断的情况下评估风格化的文本。
### Innovation
本文提出了一个框架，用于生成和评估19世纪小说家风格的句子。大型语言模型通过使用最少、单一标记的提示进行微调，生成狄更斯、奥斯汀、马克·吐温、奥尔科特和梅尔维尔等作家的声音文字。为了评估这些生成模型，作者利用一个基于变换器的检测器来训练真实句子，使用其作为分类器和风格解释工具。此外，作者还进行了句法比较，并使用基于注意力和梯度的解释性AI方法，以识别驱动风格模仿的语言线索。
### Conclusion
我们的研究发现，生成的文字反映出作者的独特模式，并且基于AI的评估为人类评估提供了一个可靠的选择。所有与此工作相关的成品都已在网上发布。
## 165. `cs.AI` - 使用主动学习辅助注意力对抗双自编码器的排名增强异常检测 [PDF](https://arxiv.org/pdf/2511.20480), [HTML](https://arxiv.org/abs/2511.20480)
### Authors
Sidahmed Benabderrahmane,James Cheney,Talal Rahwan
### Background
由于高级持续性威胁（APTs）的隐蔽性和长期性质，它们在网络安全领域构成了重大挑战。现代监督学习方法需要大量带标签的数据，但在实际的网络安全环境中，这些数据往往相对稀缺。
### Innovation
本文提出了一种创新的方法，利用自编码器（AutoEncoders）进行无监督异常检测，并通过主动学习逐步提高对APTs异常的检测能力。通过选择性地向专家查询不确定或模糊样本的标签，这种方法可以减少标记成本并提高检测率，从而在数据量有限的情况下提升模型的检测准确性，减少对大量手动标注的需求。
### Conclusion
在真实数据集上进行的评估表明，所提出的方法在主动学习过程中显示出显著改进的检测率，并在多个操作系统和两种攻击场景下表现优于现有方法。
## 166. `cs.AI` - Object-Centric Vision Token Pruning for Vision Language Models [PDF](https://arxiv.org/pdf/2511.20439), [HTML](https://arxiv.org/abs/2511.20439)
### Authors
Guangyuan Li,Rongzhen Zhao,Jinhong Deng,Yanbo Wang,Joni Pajarinen
### Background
在视觉语言模型（VLMs）中，视觉令牌与语言令牌相比数量较多但信息分散，因此会导致过多不必要的计算。对于高效率推断的视觉令牌精简方案，现有方法多为间接且不可靠的方式，因此提出了一种直接且有保证的方法OC-VTP（以对象为中心的视觉令牌裁剪），用于选择了最具代表性的视觉令牌，以实现高效且准确的VLM推理。
### Innovation
提出了一种直接且有保证的视觉令牌裁剪方法OC-VTP，用于识别并保留最具代表性的视觉令牌，而不做任何模型微调。这种方法只需对一个小的对象为中心的视觉令牌裁剪器进行轻量级预训练，之后可以插入到现有的VLM中。通过最小化从裁剪后的令牌重建原始未裁剪令牌的误差，确保了最重要的视觉令牌保留。无论视觉令牌裁剪比例如何，OC-VTP都能保证主流VLMs在推理准确率上的最大保留。此外，展示出一些有趣可解释的数据。
### Conclusion
在任何视觉令牌裁剪比率下，OC-VTP都能帮助主流VLMs保持最高的推理准确率。此外，该方法具有良好的可解释性。代码可在[该链接]获得。
## 167. `cs.AI` - StableTrack: 在低频率检测下稳定多对象跟踪 [PDF](https://arxiv.org/pdf/2511.20418), [HTML](https://arxiv.org/abs/2511.20418)
### Authors
Matvei Shelukhan,Timur Mamedov,Karina Kvanchiani
### Background
在计算机视觉领域，多对象跟踪（MOT）是一项极具挑战性的任务，主要挑战在于准确检测物体并跨帧关联这些检测结果。现有方法主要关注视频流中每一帧的物体跟踪，这使得在计算资源有限的条件下运行模型变得几乎不可能。
### Innovation
我们提出了StableTrack，一种新的方法，以在低频率检测下稳定跟踪质量。方法引入了一种新的两阶段匹配策略，以改善低频率检测之间的跨帧关联。我们提出了基于Bbox的距离度量，而不是传统的Mahalanobis距离，这允许我们有效利用Re-ID模型进行物体匹配。此外，我们将视觉跟踪集成到Kalman滤波器和整体跟踪流程中。
### Conclusion
我们的方法在低频率检测情况下优于当前最先进的跟踪器，在MOT17-val上的HOTA改进了11.6%，同时在MOT17、MOT20和DanceTrack测试基准的标准检测频率下也保持了与最佳方法的竞争力。
## 168. `cs.AI` - BengaliFig：用于孟加拉语具象性和文化基础推理的低资源挑战 [PDF](https://arxiv.org/pdf/2511.20399), [HTML](https://arxiv.org/abs/2511.20399)
### Authors
Abdullah Al Sefat
### Background
大型语言模型在多语言基准测试中表现出色，但在具象和文化基础推理方面，特别是在低资源语言的环境中，评价仍然不足。孟加拉语是一种广泛使用的低资源语言，在这个领域内，其具象和文化基础推理能力尚未得到充分评估。因此，本研究旨在填补这一空白。
### Innovation
本研究提出了一个名为BengaliFig的紧凑型但丰富的题集，专门针对孟加拉语的低资源文化背景。该数据集包含435个独特的谜语，来自孟加拉口语和文学传统，每个问题都从五个正交维度进行标注（推理类型、陷阱类型、文化深度、答案类别和难度），并通过一个基于约束的人工智能辅助管道自动转换为选择题形式。研究还首次对八个主要供应商的先进语言模型进行了零样本和少量样本链式思考提示下的评估，揭示了这些模型在比喻和文化特定推理方面的一致性弱点。
### Conclusion
BengaliFig不仅为评估大语言模型在低资源文化背景中的鲁棒性提供了一个诊断性的测试工具，而且是迈向更具包容性和重视文化遗产的自然语言处理评估的一个步骤。
## 169. `cs.AI` - MTBBench：肿瘤学中的多模态序列临床决策基准 [PDF](https://arxiv.org/pdf/2511.20490), [HTML](https://arxiv.org/abs/2511.20490)
### Authors
Kiril Vasilev,Alexandre Misrahi,Eeshaan Jain,Phil F Cheng,Petros Liakopoulos,Olivier Michielin,Michael Moor,Charlotte Bunne
### Background
现有的基准测试无法捕捉到真实临床工作流程的复杂性，尤其是在多模态和纵向复杂的多专家决策环境如分子肿瘤董事会（MTBs）中。现有的评估主要集中在单模态、去语境化的问题-答案，忽视了多模态和长时间决策的需求。
### Innovation
提出了MTBBench基准，通过临床挑战性、多模态和纵向的肿瘤学问题模拟MTB式的多专家决策。MTBBench通过提供一个代理框架和基于基础模型的工具，增强了多模态和纵向推理，使得特定任务的性能分别提高了9.0%和11.2%。解决了现有基准测试可靠性差的问题，多模态语言模型在时间解决问题、整合不同证据和模态方面表现出困难。
### Conclusion
MTBBench提供了一个具有挑战性和现实性的测试平台，用于推进多模态语言模型的推理、可靠性和工具使用，重点关注精准肿瘤学中的MTB环境。
## 170. `cs.AI` - The Text Aphasia Battery (TAB): A Clinically-Grounded Benchmark for Aphasia-Like Deficits in Language Models [PDF](https://arxiv.org/pdf/2511.20507), [HTML](https://arxiv.org/abs/2511.20507)
### Authors
Nathan Roll,Jill Kries,Flora Jin,Catherine Wang,Ann Marie Finley,Meghan Sumner,Cory Shain,Laura Gwilliams
### Background
大型语言模型（LLMs）被视作人类语言研究的一个候选‘模型生物’，为研究如失语症这类语言障碍提供了前所未有的机会。然而，传统的临床评估方法不适合LLM，因为这些方法基于人类特有的语用压力，并测试了一些对人工架构不具备内在认知过程。因此，目前需要一种适用于LLM的评估工具，能够检测类似失语症的语言缺陷。
### Innovation
本文介绍了《文本失语测试仪器》（TAB），这是一种文本形式的基准测试，是从《快速失语症测试表》（QAB）改编而来，旨在评估LLM中的类似失语症的语言缺陷。TAB包括四个子测试：连贯文本、词汇理解、句子理解、重复测试。此外，该研究还验证了一种自动化评估程序，使用Gemini 2.5 Flash实现与专家人类评价者可靠性相媲美的可靠性（模型-共识一致性Cohen's kappa = 0.255 vs. 人类-人类一致性Cohen's kappa = 0.286）。这为大规模应用提供了一个解决方案。
### Conclusion
TAB提供了一个基于临床数据且可扩展的框架，用于分析人工系统的语言缺陷。其自动评估协议的有效验证为大规模应用和研究提供了支撑。
## 171. `cs.AI` - DesignPref: Capturing Personal Preferences in Visual Design Generation [PDF](https://arxiv.org/pdf/2511.20513), [HTML](https://arxiv.org/abs/2511.20513)
### Authors
Yi-Hao Peng,Jeffrey P. Bigham,Jason Wu
### Background
生成模型，如大型语言模型和文本到图像的扩散模型，广泛用于创建用户界面（UI）和演示文稿等视觉设计。这些模型的微调和基准测试主要依赖于人工标注的偏好评价数据集。然而，由于视觉设计的高度主观性和个性化特点，不同个体的偏好存在显著差异。
### Innovation
本文通过引入DesignPref，一个包含20名专业设计师对12000个UI设计生成进行两两比较并标注多级偏好评分的数据集，研究了视觉设计偏好评估的个人化问题。研究结果显示，传统多数投票方法训练聚合裁判模型往往不能准确反映个体偏好。为解决此挑战，本文探讨了多种个性化策略，特别是对RAG管道进行微调或集成设计师特定注释，结果显示个性化模型能够更准确地预测个体设计师的偏好。
### Conclusion
本文首次提供了研究个性化视觉设计评估的第一组数据集，并支持未来关于建模个人设计偏好的研究。个性化模型在使用20倍少的样本时也能始终优于聚合基准模型，预测个体设计师的偏好。
## 172. `cs.AI` - Block Cascading: Training Free Acceleration of Block-Causal Video Models [PDF](https://arxiv.org/pdf/2511.20426), [HTML](https://arxiv.org/abs/2511.20426)
### Authors
Hmrishav Bandyopadhyay,Nikhil Pinnaparaju,Rahim Entezari,Jim Scott,Yi-Zhe Song,Varun Jampani
### Background
现有的块因果视频生成面临速度和质量之间的权衡：小的1.3B模型只能以16 FPS运行，而大的14B模型则以4.5 FPS运行。这迫使用户在响应性和生成质量之间做出选择。
### Innovation
Block Cascading 通过无训练并行化显著缓解了这一权衡。核心见解是未来视频块不需要完全去噪当前块就可以开始生成。通过使用从前继块获得的部分去噪上下文来初始化块生成，Block Cascading 将顺序管道转换为并行瀑布，多个块可以同时去噪。利用5块GPU实现时间上的并行化，Block Cascading 在所有模型规模上实现了约2倍的加速：对于1.3B模型，从16 FPS加速至30 FPS；对于14B模型，从4.5 FPS加速至12.5 FPS。除了推理速度，Block Cascading 还消除了交互生成过程中频繁的上下文切换带来的KV缓存开销。
### Conclusion
广泛的评估表明，转换到使用Block Cascading管道进行推理时，生成质量不会受到明显损失。Block Cascading 为块因果视频模型的推理加速提供了一种无训练的方法。
## 173. `cs.AI` - MIMIC-MJX：动物行为的神经力学模拟 [PDF](https://arxiv.org/pdf/2511.20532), [HTML](https://arxiv.org/abs/2511.20532)
### Authors
Charles Y. Zhang(1),Yuanjia Yang(2, 3),Aidan Sirbu(4, 5),Elliott T.T. Abe(6),Emil Wärnberg(1),Eric J. Leonardis(2),Diego E. Aldarondo(1),Adam Lee(1, 2),Aaditya Prasad(7),Jason Foat(2),Kaiwen Bian(2),Joshua Park(2),Rusham Bhatt(2),Hutton Saunders(2),Akira Nagamori(2),Ayesha R. Thanawalla(2),Kee Wui Huang(2),Fabian Plum(8),Hendrik K. Beck(8),Steven W. Flavell(7, 9),David Labonte(8),Blake A. Richards(4, 5, 10),Bingni W. Brunton(6),Eiman Azim(2),Bence P. Ölveczky(1),Talmo D. Pereira(2) ((1) Harvard University, (2) Salk Institute for Biological Studies, (3) University of California San Diego, (4) Mila, (5) McGill University, (6) University of Washington, (7) Massachusetts Institute of Technology, (8) Imperial College London, (9) Howard Hughes Medical Institute, (10) Canadian Institute for Advanced Research)
### Background
神经系统的首要输出是运动和行为。尽管最近的技术进步已经使得在复杂行为过程中进行姿态跟踪普及化，但仅通过运动学轨迹并不能直接访问潜在的控制过程。本研究提出了MIMIC-MJX框架，旨在通过学习神经控制策略来模拟真实的运动轨迹，从而研究生物可行的神经控制策略。
### Innovation
MIMIC-MJX框架通过训练神经控制器来实现运动学轨迹的再现，这些控制器可以驱动生物力学现实的体模在物理模拟中运行，从而生成真实的运动轨迹。研究表明，该框架在准确性、速度、数据效率和泛化能力上表现出色。
### Conclusion
使用MIMIC-MJX框架训练出来的策略既可以用于分析神经控制策略，也可以用于模拟行为实验，展示了其作为神经科学整合建模框架的应用潜力。
## 174. `cs.AI` - 使用语义分割对文化遗迹进行自动监控 [PDF](https://arxiv.org/pdf/2511.20541), [HTML](https://arxiv.org/abs/2511.20541)
### Authors
Andrea Ranieri,Giorgio Palmieri,Silvia Biasotti
### Background
文章强调了在文化遗迹保护中自动裂缝检测的迫切需求，并通过像素级语义分割来实现。研究使用了不同卷积神经网络（CNN）编码器的U-Net架构，进行石雕和纪念碑裂缝识别的对比研究。
### Innovation
研究对OmniCrack30k数据集进行了测试集上的定量对比评估，并对未标记的实际裂缝石雕和纪念碑进行了离群点的定性评估。研究成果提供了不同基于CNN的编码器在精细裂缝分割上的能力见解，并展示了这些模型在未见文化遗迹图像上表现出良好的泛化能力。
### Conclusion
实验证明模型在未知文化遗迹背景下的应用场景中具有良好的泛化能力，尽管这些模型从未被明确地训练过此类图像。
## 175. `cs.AI` - 第二十届《理性与知识的理论方面》会议论文集 [PDF](https://arxiv.org/pdf/2511.20540), [HTML](https://arxiv.org/abs/2511.20540)
### Authors
Adam Bjorndahl(Carnegie Mellon University)
### Background
TARK会议旨在汇集来自计算机科学、人工智能、博弈论、决策理论、哲学、逻辑学、语言学和认知科学等多个领域的研究人员，以增进对关于理性与知识的认知的跨学科问题的理解。自1986年以来，该会议每两年在全球范围内举办一次，由康奈尔大学的Joe Halpern发起。会议的主题包括知识、信念、不确定性、意识、有限理性、常识认知推理、认知逻辑、认知博弈论、知识与行动等方面的应用、推理知识及其他心理状态的变革、信念修正、计算社会选择、算法博弈论以及多agent系统的基础。
### Innovation
该会议致力于通过跨学科的研究方法进一步理解关于理性与知识的问题，并围绕多种具体主题进行了深入讨论，包括但不限于知识、信念、不确定性、意识、有限理性等。
### Conclusion
这些论文汇集了第二十届《理性与知识的理论方面》会议的接受稿件，会议于2025年7月14日至16日在德国杜塞尔多夫的海因里希-海涅大学举办。会议网站及更多信息可在会议官网获取。
## 176. `cs.AI` - 从一个攻击领域到另一个：具有Siamese网络的对比性迁移学习在APT检测中的应用 [PDF](https://arxiv.org/pdf/2511.20500), [HTML](https://arxiv.org/abs/2511.20500)
### Authors
Sidahmed Benabderrahmane,Talal Rahwan
### Background
传统的机器学习检测器在应对持续性威胁(APT)时面临挑战，因为APT具有隐蔽性、持续性以及适应性。传统方法难以处理类别不平衡、高维特征以及稀疏的现实世界攻击痕迹。这些方法往往在训练领域表现出色，但在新的攻击场景中性能下降。
### Innovation
本文提出了一种结合迁移学习、可解释的人工智能(XAI)、对比学习和Siamese网络的混合转移框架，以提高跨领域泛化能力。该框架包括一个基于注意力的自动编码器支持知识在不同领域之间的转移，通过Shapley Additive exPlanations (SHAP)选择稳定且有意义的特征以减少维度和计算成本。通过一种对照目标训练的Siamese编码器，源和目标之间的表示得到对齐，这增加了异常的分离度并减轻了特征漂移。
### Conclusion
该方法在来自DARPA透明计算( TC)计划的真实攻击痕迹以及合成攻击场景上进行了评估。与经典的和深度的基线相比，该方法在从源域到目标域的转移中提高了检测得分，展示了可扩展、可解释且转移性强的APT检测解决方案。
## 177. `cs.AI` - New York Smells: 一个大规模多模态气味数据集 [PDF](https://arxiv.org/pdf/2511.20544), [HTML](https://arxiv.org/abs/2511.20544)
### Authors
Ege Ozguroglu,Junbang Liang,Ruoshi Liu,Mia Chiquier,Michael DeTienne,Wesley Wei Qian,Alexandra Horowitz,Andrew Owens,Carl Vondrick
### Background
嗅觉是动物感知世界的重要方式，而这一丰富的化学感知模态对于机器仍然不可触及。主要原因在于缺乏在自然环境中收集的多样多模态嗅觉训练数据。因此，设计了一个大规模的多模态气味数据集New York Smells，包含室内和室外环境中3500个不同物体的7000个嗅觉-图像配对。
### Innovation
提出了New York Smells，这是一个涵盖室内和室外环境的大型多模态气味数据集，包含7000个嗅觉-图像配对，约是现有气味数据集的70倍。该数据集有三项任务：跨模态嗅觉到图像检索、仅凭气味识别场景、物体和材料、以及对草种类进行细粒度区分。实验结果表明，视觉数据有助于多模态嗅觉表示学习，且学习到的气味表示优于常用的手工特征。
### Conclusion
通过实验表明，视觉数据可以促进跨模态嗅觉表示学习，且新学习的嗅觉表示优于常规的手工设计特征；提出了大规模多模态气味数据集New York Smells，在多项任务上展示了优越性能，为相关研究提供了重要支持。
## 178. `cs.AI` - BrowseSafe：理解并防止AI浏览器代理中的即时注入 [PDF](https://arxiv.org/pdf/2511.20597), [HTML](https://arxiv.org/abs/2511.20597)
### Authors
Kaiyuan Zhang,Mark Tenenholtz,Kyle Polley,Jerry Ma,Denis Yarats,Ninghui Li
### Background
将人工智能（AI）代理集成到web浏览器中带来了超越传统网络应用程序威胁模型的安全挑战。先前的工作已经发现即时注入作为一种新的攻击向量，但在现实世界环境中的影响仍然不够了解。
### Innovation
本文研究了即时注入攻击的格局，并综合了一个嵌入在实用HTML载荷中的攻击基准。这项基准超越了以往的工作，强调能够影响现实世界行动的注入，而非仅仅影响文本输出，并且展示的攻击载荷复杂性和干扰频率与现实生活中的代理所遇到的情况相似。我们利用这一基准开展了一项全面的经验评估，评估现有防御的有效性，测试前沿AI模型。（提出了多层次防御策略，结合架构性防御和基于模型的防御，以对抗不断演化的即时注入攻击。）
### Conclusion
我们的工作为设计实用且安全的web代理提供了一个多层次防御策略的蓝图，通过深入防御方法。
## 179. `cs.AI` - Vibe编码能否击败研究生CS学生？LLM与人类编码在市场驱动的战略规划比赛中的对决 [PDF](https://arxiv.org/pdf/2511.20613), [HTML](https://arxiv.org/abs/2511.20613)
### Authors
Panayiotis Danassis,Naman Goel
### Background
大型语言模型（LLMs）的迅速发展已经改变了AI辅助代码生成的状况。然而，由于这些模型的发展速度超过了对它们进行适当基准测试的能力，当前的基准测试主要依赖于单一测试通过率和语法正确性。这种测试方式无法全面评估模型在需要计划、优化和战略互动的复杂现实问题上的能力。
### Innovation
该研究提出了一种基于现实世界物流优化问题（竞标、取货和送货问题）的多智能体推理驱动基准测试。该基准测试要求构建能在不确定性下进行策略性报价的代理，以及优化能够完成任务并最大化利润的计划。
### Conclusion
研究结果表明，人类（研究生）编码的代理在这场比赛中明显优于LLM编码的代理，以最佳的人类解为输入并要求其改进，最佳的LLM反而降低了解决方案的质量。这些结果突显了LLMs在生成能在现实场景中竞争工作的代码方面的局限性，并激励进行新的评价，以强调在现实场景中实现推理驱动的代码合成。
## 180. `cs.AI` - 评估深度学习模型在搬运重物活动中全身动态3D姿态预测中的性能 [PDF](https://arxiv.org/pdf/2511.20615), [HTML](https://arxiv.org/abs/2511.20615)
### Authors
Seyede Niloofar Hosseini,Ali Mojibi,Mahdi Mohseni,Navid Arjmand,Alireza Taheri
### Background
本研究旨在探索深度神经网络在动态搬运重物活动中对全身姿态预测的应用。研究团队使用双向长短期记忆（BLSTM）和transformer架构训练了两个时间序列模型。数据集包含来自20名正常体重的健康男性个体的全身动态坐标数据，他们执行了204次从不同负载位置的搬运任务，采用多种搬运和处理技术。
### Innovation
1. 开发了使用transformer架构的新型模型，使根均方误差在3D运动框架中捕捉时间序列依赖性；2. 提出了新的成本函数方法，通过优化恒定的身体段长来提高姿势预测网络的准确性；3. 新成本函数分别使手臂和腿部模型的预测误差减少了约8%和21%；4. transformer架构在长期性能上比基于BLSTM的模型提高了约58%的准确性。
### Conclusion
本研究表明，利用深度学习模型，特别是transformer架构，对于理解并预测手动物料搬运过程中的运动动态具有独特的优势。
## 181. `cs.AI` - Flash-DMD：高效分布式微步图像生成与联合强化学习 [PDF](https://arxiv.org/pdf/2511.20549), [HTML](https://arxiv.org/abs/2511.20549)
### Authors
Guanjie Chen,Shirui Huang,Kai Liu,Jianchen Zhu,Xiaoye Qu,Peng Chen,Yu Cheng,Yifu Sun
### Background
扩散模型已成为生成模型的领先类别，但由于其迭代采样的过程计算成本高昂，因此存在提升空间。时间步骤蒸馏是一种加速生成的有前景技术，但通常需要大量训练并导致图像质量下降。此外，通过强化学习（RL）微调这些蒸馏模型以达到特定目的（如美学吸引力或用户偏好）也非常不稳定，容易陷入奖励黑客（reward hacking）。
### Innovation
本文提出了Flash-DMD，一种新颖的框架，允许高效的蒸馏和联合RL细化。作者提出了一种高效的时间步骤感知蒸馏策略，显著减少了训练成本并提升了真实性，优于DMD2只需其2.1%的训练成本。此外，通过联合训练方案，模型在RL目标下进行微调的同时，持续进行时间步骤蒸馏训练。实验显示，持续蒸馏产生的稳定、清晰的损失作为强大的正则化器，有效稳定了RL训练过程，防止了策略崩溃。Flash-DMD在小步采样的生成质量上表现出色，超过了现有方法，在视觉质量、人类偏好和文本-图像对齐度量方面领先。
### Conclusion
本文介绍了Flash-DMD，一种高效的、高保真度和稳定的生成模型训练框架。实验结果表明Flash-DMD不仅收敛速度快，在少量步骤采样中实现最佳生成质量，并在视觉质量、人类偏好和文本-图像对齐上优于现有方法。代码即将发布。
## 182. `cs.AI` - EnergyTwin:一个用于模拟和协调能源微电网的多代理系统 [PDF](https://arxiv.org/pdf/2511.20590), [HTML](https://arxiv.org/abs/2511.20590)
### Authors
Jakub Muszyński,Ignacy Walużenicz,Patryk Zan,Zofia Wrona,Maria Ganzha,Marcin Paprzycki,Costin Bădică
### Background
微电网被部署以降低购买的电网能源成本、限制对易变费率的暴露以及在扰动期间确保服务连续性。这要求多时间尺度和变条件下的协调异构分布式能源资源。现有的工具通常只捕捉物理行为但假设集中控制，或建模分散决策但缺乏物理接地的能源表示。因此，提出了一种名为EnergyTwin的基于代理的微电网仿真环境，它结合了物理模型、预报引导的滚动计划和谈判。
### Innovation
EnergyTwin 通过融合物理模型与预报引导下的滚动计划和谈判机制，解决了既往工具的限制。每个资产都被建模为一个代理，与中央代理交互以获取预报、制定预测并基于合同进行能源分配。该系统旨在解决第三层决策问题，并可扩展用于数字孪生用途。研究结果表明，预报驱动的滚动计划增强了局部能源自给自足，维持了较高的电池储备，并减少了脆弱运行状态的暴露。
### Conclusion
研究结果强调了EnergyTwin作为支持弹性、谈判驱动微电网研究平台的潜力，特别是在微电网多种规划策略评估中，显示出显著改进性能。
## 183. `cs.AI` - ROOT: 神经网络训练中稳健正交优化器 [PDF](https://arxiv.org/pdf/2511.20626), [HTML](https://arxiv.org/abs/2511.20626)
### Authors
Wei He,Kai Han,Hang Zhou,Hanting Chen,Zhicheng Liu,Xinghao Chen,Yunhe Wang
### Background
大语言模型（LLMs）的优化仍然是一个关键挑战，特别是在模型规模扩大时，这加剧了对算法不精确性的敏感性和训练不稳定性的风险。尽管最近在优化器领域的进展提高了收敛效率，通过动量正交化，但在鲁棒性方面仍然存在两个主要限制：正交化精度的维度脆弱性和异常值引起的噪声的易感性。
### Innovation
我们提出了ROOT，一种增强训练稳定性的稳健正交优化器，具有双重鲁棒机制。首先，我们开发了一种维度鲁棒的正交化方案，利用自适应牛顿迭代和针对不同矩阵大小细粒度调整的 coefficients，以确保不同的架构配置下都保持一致的精度。其次，我们引入了一种通过对近似优化框架来抑制异常值噪声同时保留有意义的梯度方向的优化鲁棒框架。
### Conclusion
广泛的实验证明，与 Muon 和基于 Adam 的优化器相比，ROOT 在鲁棒性、收敛速度和最终性能方面有了显著改进，特别是在噪声和非凸场景中。我们的工作确立了一个新的稳健且精确的优化器开发范式，能够应对现代大规模模型训练的复杂性。源代码可从 [this URL] 获取。
## 184. `cs.AI` - 基于时间域线性模型框架的空化活动被动声学成像方法 [PDF](https://arxiv.org/pdf/2511.20551), [HTML](https://arxiv.org/abs/2511.20551)
### Authors
Tatiana Gelvez-Barrera,Barbara Nicolas,Denis Kouamé,Bruno Gilles,Adrian Basarab
### Background
被动声学映射能够实现空化活动的空间映射和时间监测，在治疗性超声应用中具有重要作用。传统波束形成方法在时域或频域中实现，由于缺乏参考发射起始时间，普遍轴向分辨率较低。频域方法中的交叉谱矩阵是最高效的方法之一，但需要较长的信号才能获得准确的估计。时域方法通常获得较低的分辨率。
### Innovation
本文提出了一种全时域基于线性模型的波束形成框架。该模型将离散化的时空分布空化活动与探头记录的时间信号相关联，并考虑了由采集几何学决定的时间飞行延迟。使用结合空间和时间域先验知识的正则化技术对该模型进行逆求解。实验结果表明，提出的框架在使用频率域方法所需数据量的20%的情况下，实现了增强或竞争性的空化图质量。
### Conclusion
此研究表明在数据效率上有了显著增益，并且时域空间正则化方法在不同被动空化场景中具有更强的适应性，优于最新技术。
## 185. `cs.AI` - 通过评估LLM作为法官来评估LLM对齐 [PDF](https://arxiv.org/pdf/2511.20604), [HTML](https://arxiv.org/abs/2511.20604)
### Authors
Yixin Liu,Pengfei Liu,Arman Cohan
### Background
大型语言模型（LLMs）的对齐是一种重要的评估方面，需要模型能够帮助、诚实地、安全地以及精确地遵循人类指令。评估LLMs的对齐通常需要直接评估它们的开放性回答，这通常需要人类注释员或强大LLM裁判。反之，LLMs也常被评估作为裁判来评估对齐。本文研究了LLMs生成能力和评估能力在对齐人类偏好方面的关联性。
### Innovation
本文提出了一种基准方法AlignEval，该方法通过让LLMs担任评委角色来间接评估它们的对齐能力，无需直接对其生成输出进行评估。研究发现，与当前流行的自动LLM评估基准（例如AlpacaEval和Arena-Hard）相比，AlignEval在排名LLMs时能更好地捕捉人类偏好。
### Conclusion
本文通过详细分析各种LLMs之间的生成-评估一致性（GE一致性），揭示了其生成能力与评估能力之间存在强烈关联。提出了一种新的基准，即AlignEval，该基准在衡量LLMs的人类偏好对齐方面具有优越性。这项研究揭示了生成能力和评估能力之间的联系，并提供了一种无需直接评估模型输出即可评估对齐的方法。
## 186. `cs.AI` - Gated Uncertainty-Aware Runtime Dual Invariants for Neural Signal-Controlled Robotics [PDF](https://arxiv.org/pdf/2511.20570), [HTML](https://arxiv.org/abs/2511.20570)
### Authors
Tasha Kim,Oiwi Parker Jones
### Background
安全关键辅助系统直接从神经信号解码用户意图，需要对可靠性和信任性进行严格保证。这些系统需要确保在实时时空中能够安全可靠地运行，特别是在基于神经信号控制的机器人系统中。现有的解码器架构可能具有较低的准确性以及高置信度误校准率，这给系统的可靠性和用户的信任带来了挑战。
### Innovation
GUARDIAN框架为基于神经信号的机器人控制系统提供了一种实时神经符号验证方法，通过将信心校准的大脑信号解码与符号目标接地和双层运行时监控相结合，实现逻辑安全性与生理信任的双重保障。该系统在处理具有低准确性和高置信度误校准的解码器架构时仍能保持较高的安全性（94-97%），并在模拟噪声测试中表现出1.7倍的正确干预次数。
### Conclusion
GUARDIAN监测器以100Hz的频率运行，具有亚毫秒级的决策延迟，具备为闭环神经信号系统提供实际可行性的潜力。通过21个消融实验结果可以看出，GUARDIAN能够对信号降级作出逐步响应，并生成可审计的决策轨迹，有助于将神经证据与可验证的机器人行为联系起来。
## 187. `cs.AI` - The Driver-Blindness Phenomenon: Why Deep Sequence Models Default to Autocorrelation in Blood Glucose Forecasting [PDF](https://arxiv.org/pdf/2511.20601), [HTML](https://arxiv.org/abs/2511.20601)
### Authors
Heman Shakeri
### Background
深度序列模型在血糖预测方面未能充分利用如胰岛素、饮食和活动等临床相关驱动因素，尽管生理机制已经明确。这一现象被定义为‘驱动盲性(Driver-Blindness)’，且通过$text{Δ}_{text{drivers}}$这一指标衡量：多元模型比匹配的一元基线模型性能提升。文献中的$text{Δ}_{text{drivers}}$通常接近零。这一现象归因于三大相互作用因素：倾向于自相关性（C1）的架构偏见、数据真实度差距导致驱动因素噪声且混杂（C2）、以及生理多样性使群体模型失效（C3）。
### Innovation
合成了部分缓解驱动盲性的策略——包括生理特征编码、因果正则化和个人化方法。并建议未来研究应常规报告$text{Δ}_{text{drivers}}$以防止忽略驱动因素的模型被误认为最先进的算法。
### Conclusion
深度序列模型在血糖预测中默认依赖于自相关性，主要原因在于架构偏见、数据真实度差距及生理多样性。提出了缓解策略，并强调未来研究需报告$text{Δ}_{text{drivers}}$避免驱动盲性模型误认为最先进。
## 188. `cs.AI` - MotionV2V：视频中编辑运动 [PDF](https://arxiv.org/pdf/2511.20640), [HTML](https://arxiv.org/abs/2511.20640)
### Authors
Ryan Burgert,Charles Herrmann,Forrester Cole,Michael S Ryoo,Neal Wadhwa,Andrey Voynov,Nataniel Ruiz
### Background
生成式视频模型在细节保真度和一致性方面已取得显著成就，但将其应用到视频编辑中仍面临复杂挑战。尽管近期研究探索了运动可控性以增强自图文生成或图像动画，但本文发现，精确运动控制是编辑现有视频的一个有潜力但未充分探索的范式。
### Innovation
本文提出了通过直接编辑输入视频中稀疏轨迹来修改视频运动的方法，并称轨迹之间的偏差为“运动编辑”。该方法结合生成式主干网络，实现了强大的视频编辑能力。此外，还引入了一个生成“运动反事实”的管道，即共享相同内容但运动区别明显的视频对，并在该数据集上对基于运动条件的视频扩散架构进行了微调。
### Conclusion
在四面体对齐的用户研究中，本文模型获得了超过65％的偏好，优于先前工作。上述工作可参见项目页面：this https URL
## 189. `cs.AI` - DiFR: 尽管存在非确定性进行推理验证 [PDF](https://arxiv.org/pdf/2511.20621), [HTML](https://arxiv.org/abs/2511.20621)
### Authors
Adam Karvonen,Daniel Reuter,Roy Rinberg,Luke Marks,Adrià Garriga-Alonso,Keri Warr
### Background
随着大型语言模型（LLM）推理需求的增长，验证推理过程是否正确执行变得越来越重要，尤其是在没有错误或篡改的情况下。然而，由于良性数值噪声的缘故，重新运行相同的推理过程常常会导致不同结果，这使得区分合理的变异与实际问题变得困难。为了解决此问题，提出了一种名为Token-DiFR的方法，通过将生成的标记与使用相同随机种子可信参考实现生成的预测进行比较来验证推理输出。这种同步采样种子严格限制了有效输出的有效范围，使得服务提供商几乎没有偏离正确推理的空间，从而使输出标记自身能够以零成本作为正确性的可审计证据。Token-DiFR能够可靠地识别采样错误、模拟的错误和模型量化，能够在300个输出标记内检测4位量化，AUC > 0.999。
### Innovation
提出了一种名为Token-DiFR的方法，用于通过将生成的标记与基于相同随机种子的可信参考实现生成的预测进行比较来验证推理输出。此外，引入了Activation-DiFR方案，使用随机正交投影将激活压缩为紧凑的指纹，从而实现后续验证。Activation-DiFR能够在仅使用2个输出标记的情况下检测4位量化，AUC > 0.999，并通过减少25-75%的通信开销来降低现有方法的开销。
### Conclusion
Token-DiFR为发现采样错误、模拟错误和模型量化提供了可靠的解决方案。Activation-DiFR进一步减少了通信开销，能够在少量输出标记内实现高效的验证。作者还提供了一个vLLM的开源集成，以加速验证推理的实际部署。
## 190. `cs.AI` - MapReduce LoRA: Advancing the Pareto Front in Multi-Preference Optimization for Generative Models [PDF](https://arxiv.org/pdf/2511.20629), [HTML](https://arxiv.org/abs/2511.20629)
### Authors
Chieh-Yun Chen,Zhonghao Wang,Qi Chen,Zhifan Ye,Min Shi,Yue Zhao,Yinan Zhao,Hui Qu,Wei-An Lin,Yiru Shen,Ajinkya Kale,Irfan Essa,Humphrey Shi
### Background
该研究基于强化学习来自人类反馈（RLHF）与奖励模型的进步，促进了生成模型与人类审美和感知偏好的对齐。然而，同时优化多个奖励往往会出现对齐税，即在提升某一方面的同时会降低其他方面。
### Innovation
该论文引入了两种互补的方法：MapReduce LoRA 和 Reward-aware Token Embedding (RaTE)。MapReduce LoRA 通过并行训练偏好特异性 LoRA 专家并迭代合并它们，以细化共享基础模型；RaTE 在推理时通过学习奖励特异的 token 嵌入来组成特定的偏好控制。实验表明，在文本到图像生成和文本到视频生成任务中，MapReduce LoRA 和 RaTE 方法分别取得了显著的性能提升。
### Conclusion
我们的框架在不同模态下设置了一种新的多偏好数学优化的范例，实现了多偏好的优化改进。
## 191. `cs.AI` - 多模态生成人工智能：多模态大语言模型、扩散模型及统一 [PDF](https://arxiv.org/pdf/2409.14993), [HTML](https://arxiv.org/abs/2409.14993)
### Authors
Xin Wang,Yuwei Zhou,Bin Huang,Hong Chen,Wenwu Zhu
### Background
多模态生成人工智能（Artificial Intelligence）引起了学术界和工业界的广泛关注。多模态大型语言模型在多模态理解方面表现出色，而扩散模型在多模态生成方面表现卓越。
### Innovation
本文对多模态生成人工智能进行了全面概述，涵盖了多模态大语言模型、扩散模型及其统一，详细介绍了这两种模型的建模过程、多模态架构设计等，并探讨了理解与生成统一模型的最新进展，分析了相关的关键设计与策略。
### Conclusion
总结了广泛用于多模态生成人工智能预训练的标准数据集，并提出了未来研究的挑战方向，旨在推动多模态生成人工智能的持续发展。
## 192. `cs.AI` - 通过语言代理进行多模态数据探索 [PDF](https://arxiv.org/pdf/2412.18428), [HTML](https://arxiv.org/abs/2412.18428)
### Authors
Farhad Nooralahzadeh,Yi Zhang,Jonathan Furst,Kurt Stockinger
### Background
国际企业、组织和医院收集大量的多模态数据，包括存储在数据库、文本文档、图像和视频中的数据。虽然在多模态数据探索以及自然语言问题自动转换成数据库查询语言方面已有近期进展，但如何通过自然语言查询结构化数据库和半结构化/非结构化模态（如文本、图像）的研究挑战还没有被充分探索。
### Innovation
本文提出了M$^2$EX系统，这是一种基于语言代理的多模态数据探索系统。M$^2$EX利用基于大语言模型（LLM）的代理型AI框架，将自然语言问题分解为子任务，如基于文本的SQL生成和图像分析，并高效地调用特定模态的专家以制定查询计划。实验结果表明，该系统在多模态数据集（包含关系数据、文本和图像）中的性能优于现有最先进的多模态探索系统，特别是在准确性、查询延迟、API成本和规划效率等方面。
### Conclusion
通过M$^2$EX系统，能够有效利用大语言模型的推理能力，提高多模态数据探索的准确性和性能指标。
## 193. `cs.AI` - 量化数学表达式间的行为空间差异 [PDF](https://arxiv.org/pdf/2408.11515), [HTML](https://arxiv.org/abs/2408.11515)
### Authors
Sebastian Mežnar,Sašo Džeroski,Ljupčo Todorovski
### Background
在计算数学、符号推理和科学发现等领域中，量化数学表达式之间的相似性是一项基本问题。虽然行为相似性概念已在软件和程序分析中被探索过，但现有的数学表达相似性衡量方法主要依赖于其语法形式，通过符号结构而非实际行为来评估相似性。然而，语法上不同的表达式可能具有几乎相同的输出，而结构上相似的表达式则可能表现出非常不同的行为，尤其是当表达式包含自由参数时，这些参数定义了函数族。
### Innovation
为了应对这一局限，本文引入了行为感知表达式差异性（BED）框架，这是一个用于量化含有自由参数的数学表达式间行为空间差异的原理性框架。BED将表达式表示为输入输出对的联合概率分布，并使用Wasserstein距离来测量行为差异。提出了一种计算效率高的随机近似方法，并证明其一致、鲁棒，并能够在表达式空间上诱导比基于语法的度量更为平滑、有意义的结构。
### Conclusion
该方法为基于行为的比较、聚类和数学表达式的学习奠定了基础，潜在的应用领域包括方程发现、符号回归和神经符号建模。
## 194. `cs.AI` - RLZero: 无需领域监督的直接策略推理从语言 [PDF](https://arxiv.org/pdf/2412.05718), [HTML](https://arxiv.org/abs/2412.05718)
### Authors
Harshit Sikchi,Siddhant Agarwal,Pranaya Jajoo,Samyak Parajuli,Caleb Chuck,Max Rudolph,Peter Stone,Amy Zhang,Scott Niekum
### Background
奖励假设表明所有目标和目的都可以理解为最大化接收到的标量奖励信号。然而，在实践中，定义这样的奖励信号是非常困难的，因为人类往往无法预测与奖励函数对应的最优行为。自然语言为指示强化学习（RL）代理提供了一种直观的替代方法，但先前的语言条件方法要么需要昂贵的监督，要么在测试时间进行训练以给定语言指令。
### Innovation
本文介绍了一种新方法，该方法使用仅通过未标记的、离线交互进行预训练的RL代理，该代理没有特定任务的监督或标记轨迹，在没有任何领域内监督的情况下，能够从任意自然语言指令中的零样本测试时间策略推理。该方法包含三个步骤：想象、投影和模仿。首先，代理使用视频生成模型想象出与提供的语言描述相对应的一系列观察值。接下来，这些想象出的观察值被投影到目标环境领域。最后，一个在目标环境中通过无监督RL预训练的代理通过闭式解即时模仿投影的观察序列。据我们所知，我们的方法RLZero是第一个能够在一系列任务和环境中直接实现语言到行为生成能力的方法，而无需任何领域内的监督。
### Conclusion
我们进一步表明，RLZero的部分组件可以从跨体态视频（如YouTube上的视频）中生成零样本策略，即使对于复杂的体态，如类人机器人也是如此。
## 195. `cs.AI` - 多代理系统中的潜在协作 [PDF](https://arxiv.org/pdf/2511.20639), [HTML](https://arxiv.org/abs/2511.20639)
### Authors
Jiaru Zou,Xiyuan Yang,Ruizhong Qiu,Gaotang Li,Katherine Tieu,Pan Lu,Ke Shen,Hanghang Tong,Yejin Choi,Jingrui He,James Zou,Mengdi Wang,Ling Yang
### Background
多代理系统（MAS）将大型语言模型（LLMs）的独立单模型推理扩展到了系统级别的协调智能。现有的LLM代理依赖于基于文本的中介进行推理和通信。
### Innovation
本文提出了一个无需训练的端到端框架LatentMAS，使LLM代理能够在连续的潜空间中直接协作。LatentMAS通过最后一层隐藏嵌入进行自回归的潜空间思维生成，共享的潜空间工作记忆保存并传递每个代理的内部表示，确保无损失的信息交换，从而提高了系统级推理的质量并实现了显著的效率提升。
### Conclusion
实验结果表明，LatentMAS在数学和科学推理、常识理解和代码生成等9个全面基准测试中，持续超越强大的单模型和基于文本的MAS基线，准确率提高了14.6%，减少输出词元使用70.8%-83.7%，端到端推理速度提高了4到4.3倍。这表明，新的潜在协作框架提高了系统级推理的质量，同时提供了显著的效率增益，而无需额外的训练。代码和数据已全量开源。
## 196. `cs.AI` - 基于LLM的可扩展且精确的图推理框架 [PDF](https://arxiv.org/pdf/2410.05130), [HTML](https://arxiv.org/abs/2410.05130)
### Authors
Yuwei Hu,Runlin Lei,Xinyi Huang,Zhewei Wei,Yongchao Liu
### Background
近期的研究探索了大规模语言模型（LLMs）在解决复杂图推理任务中的应用。然而，由于图结构的复杂性以及LLMs在处理长文本时固有的限制，当前的方法在小规模图和简单任务上的准确度往往无法令人满意，甚至在大规模图和复杂任务上也存在问题。
### Innovation
我们提出了一种无需微调的GraphAgent-Reasoner框架，利用多智能体协作策略实现明确的图推理。借鉴分布式图计算理论，框架将图问题分解为更小的以节点为中心的任务，并分配给多个智能体。智能体协作解决整体问题，大大减少了单个LLM处理的信息量和复杂性，从而提高了图推理的准确度。此外，通过增加智能体的数量，GraphAgent-Reasoner可以高效地扩展以处理超过1000个节点的大图。
### Conclusion
在GraphInstruct数据集上，我们的框架在多项式时间内完成的图推理任务上能够达到近乎完美的准确度，显著优于现有模型，无论是闭源模型还是微调的开源模型。此外，该框架还展示了在网页重要性分析等实际图推理应用中的能力。
## 197. `cs.AI` - 访问控制将解决双重用途困境 [PDF](https://arxiv.org/pdf/2505.09341), [HTML](https://arxiv.org/abs/2505.09341)
### Authors
Evžen Wybitul
### Background
AI安全系统面临双重用途的困境。由于同样的查询可能出于良性目的或恶意目的，因此难以判断是否应该响应这些请求。为更好地做出决定，需要考虑请求的实际世界背景，但当前缺乏这方面的信息，有时导致错误的决策，如拒绝正当查询并放行有害查询，这既损害了便利性也损害了安全性。
### Innovation
本文提出了一个基于访问控制的概念性框架，只有经过验证的用户才能访问双重用途输出。该框架的组成部分具有可行性，能够同时解决过度拒绝和不足拒绝的问题。这将使模型提供商拥有更细化的工具来管理双重用途内容。
### Conclusion
虽然这只是高层次的提案，但本工作迈出了第一步，为模型提供商提供了更细粒度的管理双重用途内容的工具，使用户能够访问更多功能而不牺牲安全性，也为监管机构提供了制定针对性政策的新选项。
## 198. `cs.AI` - MedROV: 跨多种医学成像模态的实时开放词汇检测 [PDF](https://arxiv.org/pdf/2511.20650), [HTML](https://arxiv.org/abs/2511.20650)
### Authors
Tooba Tehreem Sheikh,Jean Lahoud,Rao Muhammad Anwer,Fahad Shahbaz Khan,Salman Khan,Hisham Cholakkal
### Background
传统的医学影像对象检测模型基于封闭词汇集，难以识别新型号标签的对象。开放词汇集对象检测（OVOD）虽然能解决这个限制，但在医学影像领域仍然鲜有探索，主要因为数据集稀缺且文本与图像间的对齐较弱。
### Innovation
提出了MedROV，一种针对医学影像的第一种实时开放词汇集检测模型。通过构建大型标注数据集Omnis（包含六十万样本和九种成像模态）和引入伪标签策略处理多源数据中缺失的注释，引入大规模预训练基础模型的知识增强泛化能力，利用对比学习和跨模态表示，有效检测已知和新型结构。实验结果显示，MedROV相比于之前的医学图像检测最佳基础模型，在MAP50上绝对提升了40%，相对封闭集检测器提升了3%以上，并以每秒70帧的速度运行，确立了医学检测的新基准。
### Conclusion
MedROV在医学检测中表现出色，优于此前的最佳基础模型，并设定了新的基准线，同时在代码、数据集和模型训练方面提供了开源资源。
## 199. `cs.AI` - MMTU：大规模多任务表格理解和推理基准 [PDF](https://arxiv.org/pdf/2506.05587), [HTML](https://arxiv.org/abs/2506.05587)
### Authors
Junjie Xing,Yeye He,Mengyu Zhou,Haoyu Dong,Shi Han,Lingjiao Chen,Dongmei Zhang,Surajit Chaudhuri,H. V. Jagadish
### Background
表格及其基于表格的应用在许多重要实际应用中发挥着关键作用，如电子表格、数据库和计算笔记本，通常需要数据工程师、数据分析师和数据库管理员等专家级用户进行操作。虽然大语言模型（LLMs）在处理表格方面取得了显著进展（例如在电子表格和数据库协作场景中），但对这些能力的全面基准测试仍然有限。与自然语言处理（NLP）基准数量众多且日益增长的情况相比，关于表格相关任务的评估相对稀缺，主要集中在自然语言到SQL和表格问答等任务上，忽视了专业用户面临的更广泛范围的现实世界任务。这种差距限制了我们对该领域的理解和模型的进步。
### Innovation
提出MMTU，这是一个包含超过28,000个问题的大规模基准，涵盖了25个真实的表格任务，旨在全面评估模型在理解和处理表格方面的专家级能力。这些任务涵盖了数十年来计算机科学领域关于表格数据的研究，重点是专业用户面临的复杂表格任务。示例最新模型如OpenAI GPT-5和DeepSeek R1，当前在这些任务上的表现具有挑战性，得分分别为69%和57%，表明需要显著改进。
### Conclusion
通过使用MMTU进行评估，我们展示了关键的研究发现，并希望这一基准能推动对于结构化数据处理和分析的基础模型的理解和开发的进一步进展。代码和数据可在以下网址获得：这个 https URL和这个 https URL。
## 200. `cs.AI` - CNS-Obsidian：源自科学出版物的神经外科视觉语言模型 [PDF](https://arxiv.org/pdf/2502.19546), [HTML](https://arxiv.org/abs/2502.19546)
### Authors
Anton Alyakin,Jaden Stryker,Daniel Alexander Alber,Jin Vivian Lee,Karl L. Sangwon,Brandon Duderstadt,Akshay Save,David Kurland,Spencer Frome,Shrutika Singh,Jeff Zhang,Eunice Yang,Ki Yun Park,Cordelia Orillac,Aly A. Valliani,Sean Neifert,Albert Liu,Aneek Patel,Christopher Livia,Darryl Lau,Ilya Laufer,Peter A. Rozman,Eveline Teresa Hidalgo,Howard Riina,Rui Feng,Todd Hollon,Yindalon Aphinyanaphongs,John G. Golfinos,Laura Snyder,Eric Leuthardt,Douglas Kondziolka,Eric Karl Oermann
### Background
通用的大规模语言模型（VLMs）展示了令人印象深刻的性能，但它们基于未经筛选的互联网数据的不透明训练使其在高风险决策中存在重大局限性，例如在神经外科领域。神经外科手术涉及高度专业化的医疗决策，要求模型具有透明性和精准性。传统的VLMs难以满足这一需求，因为它们不仅规模庞大且成本高昂，而且基于的数据质量参差不齐。
### Innovation
本文介绍了一个基于peer-reviewed文献训练的神经外科视觉语言模型（CNS-Obsidian）。研究者通过收集特定领域的高质量文献数据，搭建了一个更加透明和精准的VLMs，以供神经外科临床使用。相较于传统的大规模语言模型（如GPT-4o），CNS-Obsidian能够更好地适应神经外科的专业需求，展示了在实际临床应用中的潜力。
### Conclusion
尽管领域特定的VLMs（如CNS-Obsidian）经过特定科学文献的训练，其性能仍然接近于更大型且昂贵的模型，但在实际的临床试验中，它们在某些方面仍存在一定差距。然而，该研究为科学社区提供了一种透明的方法，以构建专门的AI模型，从而提高了模型的透明度和可解释性，促使专业领域更加放心地应用AI辅助工具。
## 201. `cs.AI` - ASP-Assisted Symbolic Regression: Uncovering Hidden Physics in Fluid Mechanics [PDF](https://arxiv.org/pdf/2507.17777), [HTML](https://arxiv.org/abs/2507.17777)
### Authors
Theofanis Aravanis,Grigorios Chrimatopoulos,Mohammad Ferdows,Michalis Xenos,Efstratios Em Tzirtzilakis
### Background
传统的机器学习方法因其‘黑箱’特性而受到批评，相比之下，符号回归(SR)提供了一种可解释的替代方案。在流体动力学领域，理解和掌握基本物理规律与预测准确性一样重要，研究者将SR方法应用于矩形通道三维层流流动的建模，关注切向和压力场。
### Innovation
提出了将符号回归(SR)与回答集规划(ASP)结合使用的新颖混合框架。这种方法结合了SR生成能力和ASP的声明推理能力，确保生成的方程不仅统计上准确，而且在物理上合理。通过这种方式，该方法展示了数据驱动方法和知识表示方法结合的潜力，以提高解释性、可靠性和与物理原理的一致性。
### Conclusion
提出的SR/ASP方法在流体动力学及相关领域中展现出了将数据驱动方法与知识表示方法相结合的潜力，这有助于提高解释性、可靠性和与物理原理的一致性。
## 202. `cs.AI` - 深入隐藏的认知促进可靠的链式思考推理 [PDF](https://arxiv.org/pdf/2507.10007), [HTML](https://arxiv.org/abs/2507.10007)
### Authors
Zijun Chen,Wenbo Hu,Richang Hong
### Background
链式思考(CoT)推理在大型语言模型(LLMs)和多模态大型语言模型(MLLMs)中显示出出色的深层推理能力。然而，由中间步骤积累的错误导致其可靠性往往受到损害。
### Innovation
本文提出了一种新颖的方法，通过利用模型内部的真实性编码来校准CoT推理的准确性。具体来说，特定注意力头的激活能可靠地反映出推理步骤的真实性。基于这一发现，我们训练了一个可信度预测器，利用这些真实性敏感的激活来评估每个推理步骤的正确性，并通过束搜索动态选择最有可能的推理路径。实验结果表明，本文的方法在数学、符号和常识推理任务中显著优于最先进的基准方法（例如，少样本CoT、自我一致性、自我评估引导束搜索），并且在单模态和多模态场景中都表现出更高的准确性和可靠性。
### Conclusion
我们进一步验证了该方法在大型推理模型中的适用性，并探讨了模型自我纠正能力在CoT推理中的作用。本文为CoT推理提供了新的可靠性改进路径，具有广泛的应用潜力。
## 203. `cs.AI` - CoT Red-Handed: Stress Testing Chain-of-Thought Monitoring [PDF](https://arxiv.org/pdf/2505.23575), [HTML](https://arxiv.org/abs/2505.23575)
### Authors
Benjamin Arnav,Pablo Bernabeu-Pérez,Nathan Helm-Burger,Tim Kostolansky,Hannes Whittingham,Mary Phuong
### Background
随着AI模型的部署越来越具有自主性，确保它们不会在未被察觉的情况下进行有害操作变得尤为重要。研究团队探讨了一种潜在的缓解措施，即Chain-of-Thought（CoT）监控，其中一种较弱但可信的监控模型会持续监督一种权力较大但不可信模型的中间推理步骤，以防止其进行有害行为。
### Innovation
研究团队在红队实验中对比了CoT监控和仅审查最终输出的监控方法的有效性。他们引入了一种新的混合协议，这种协议独立评估模型的推理和行动，并通过加权平均结合这两种评估结果。研究结果表明，混合监控协议在所有测试模型和任务中都表现出色，对于暗示性欺骗场景的检测率是单一行动监控的两倍。
### Conclusion
CoT监控在某些情况下比仅审查最终输出更为有效，但在出现明显欺骗行为时，推理足迹可能包含误导性解释，从而降低了其性能。因此，研究团队提出了一种新的混合协议来综合评估模型的推理和行动，并通过加权平均结合，以提供更高效的监控方法。该混合监控协议在所有测试中均表现出更高性能，特别是在细微欺骗场景的检测方面，检测率提高了一倍。
## 204. `cs.AI` - 通过情感根据验证器实现多模态LLMs的情感一致性推理 [PDF](https://arxiv.org/pdf/2510.23506), [HTML](https://arxiv.org/abs/2510.23506)
### Authors
Hyeongseop Rha,Jeong Hun Yeo,Yeonju Kim,Yong Man Ro
### Background
近年来，多模态大型语言模型（MLLMs）正在改变人机交互（HCI），使其从表面的交流转变为更具微妙性和情感智能的交流。为了实现这种转变，情感理解变得必不可少，允许系统捕捉用户意图背后微妙的线索。此外，提供高可信度的解释对于确保可解释性和建立用户信任至关重要。然而，当前基于MLLM的方法经常生成与目标标签不符的情感解释，有时甚至与自己预测的情感相矛盾。这种不一致存在重大误解的风险，并在交互环境中削弱了可靠性。
### Innovation
我们提出了一种新的方法：情感理由验证器（ERV）和解释奖励。该方法引导模型在多模态情感识别过程中生成明确与目标情感一致的推理，而无需修改模型结构或额外的视频-描述配对注释。我们的方法在MAFW和DFEW数据集上显著提高了忠实解释预测一致性及解释情感准确性。通过广泛的实验和人类评估，我们证明该方法不仅能增强解释与预测的对齐，还能使MLLMs提供更情感连贯、值得信赖的交互。
### Conclusion
这一方法代表了向真正类人的HCI系统迈出的关键一步，使MLLMs能够提供更富有情感连贯性、更值得信赖的交互。
## 205. `cs.AI` - 超越ReAct：基于规划者的新框架以提升复杂工具增强LLM推理能力 [PDF](https://arxiv.org/pdf/2511.10037), [HTML](https://arxiv.org/abs/2511.10037)
### Authors
Xiaolong Wei,Yuehu Dong,Xingliang Wang,Xingyu Zhang,Zhejun Zhao,Dongdong Shen,Long Xia,Dawei Yin
### Background
现有的工具增强型大型语言模型处理复杂查询时遇到显著挑战。现有框架如ReAct易陷入局部优化陷阱，因为它们依赖于增量决策过程。这限制了模型的全局规划能力。
### Innovation
提出了一种新型“规划者为中心”的计划-执行范式，通过架构创新从根本上解决局部优化瓶颈。引入了新的规划者模型，进行了全局有向无环图（DAG）规划，以优化传统工具协调之外的执行。还开发了由监督微调（SFT）与组相对策略优化（GRPO）组成的新两阶段训练方法，从而系统地增强了规划者在工具选择和全局规划意识方面的精度。
### Conclusion
当与高效的执行者集成时，我们的框架在StableToolBench基准测试中达到了复杂的用户查询的顶级性能，展示了卓越的端到端执行能力和对复杂的多工具工作流的稳健处理。
## 206. `cs.AI` - 大型语言模型在博弈论实验中重现并预测人类合作行为 [PDF](https://arxiv.org/pdf/2511.04500), [HTML](https://arxiv.org/abs/2511.04500)
### Authors
Andrea Cera Palatsi,Samuel Martin-Gutierrez,Ana S. Cardenal,Max Pellert
### Background
大型语言模型（LLMs）在决策制定领域（如健康、教育和法律）以及模拟人类行为方面得到了广泛应用。然而，LLMs 在实际应用中是否能精确模仿人类决策过程及其行为依然是未知的。这种差距可能导致有害后果，尤其在社会模拟中完全无法复制人类行为将使LLMs 失去效用。
### Innovation
该研究通过开发游戏理论实验的数字孪生，并引入系统化提示和探索框架，对机器行为进行评估。研究测试了三种开源模型（Llama、Mistral 和 Qwen），发现 Llama 准确再现了人类的合作模式，捕捉了人类行为与理性选择理论的偏差；而 Qwen 与纳什平衡预测高度一致。值得注意的是，研究在无需基于角色的提示下实现了行为层面的人群水平复制，简化了模拟过程。此外，研究还为新的博弈配置生成并注册了可检验的假设。
### Conclusion
适当校准的LLMs 可以在群体层面上重现人类行为模式，并为未开发的实验空间提供系统性的探索，为社会和行为科学的传统研究提供一种补充方法，从而生成新的关于人类社会决策的实证预测。
## 207. `cs.AI` - 能量感知模式解缠：一种通用模式辅助的多任务时间序列分析架构 [PDF](https://arxiv.org/pdf/2504.14209), [HTML](https://arxiv.org/abs/2504.14209)
### Authors
Xiangkai Ma,Xiaobin Hong,Wenzhong Li,Sanglu Lu
### Background
时间序列分析在天气预报、异常检测和医疗健康等多个领域有着广泛的应用。深度学习方法在该领域取得了显著的成功，但现有的方法通常采用“一模型一任务”的架构，这限制了它们在不同任务中的泛化能力。
### Innovation
本文通过在时频域进行局部能量分析，更精确地捕捉和分离出瞬态和非平稳振荡成分。此外，研究揭示了生成任务倾向于从低频分量中捕捉长期模式，而判别任务则专注于高频突变信号，这是我们的核心贡献。具体来说，本文提出了一种名为Pets的新架构，基于通用波动模式辅助（GPA）框架，包含辅助波动模式模块（FPA）和情境导向混合预测器模块（MoP）。FPA模块通过捕获多样波动模式的依赖性并逐层建模这些模式作为潜在表示促进信息融合。而MoP模块则利用这些通用表示来引导和调控低频不同波动逐级重建。
### Conclusion
Pets架构展现了强大的通用性和在各种任务（包括预测、插补、异常检测和分类）上的领先性能，同时展示了强大的泛化能力和鲁棒性。
## 208. `cs.AI` - 注意力剪枝：通过代理模拟退火自动修复语言模型的公平性 [PDF](https://arxiv.org/pdf/2503.15815), [HTML](https://arxiv.org/abs/2503.15815)
### Authors
Vishnu Asutosh Dasu,Md Rafi ur Rashid,Vipul Gupta,Saeid Tizpaz-Niari,Gang Tan
### Background
大型语言模型（LLMs）正在进入敏感的社会语境，公平性成为了尤其重要的问题。由于LLMs在大规模的人类生成内容数据集上进行训练，它们自然地编码和传播社会偏见。修改训练数据集和算法成本高昂且需要大量资源，因此，在预训练好的LLMs上采用后处理技术（如选择性使神经元和注意力头失活）可以提供可行且有效的提高公平性的方法。然而，确定需要剪枝的参数集在LLMs庞大的参数空间内是一个组合优化难题，需要能够高效地平衡模型公平性和实用性之间的竞争目标。
### Innovation
本文通过随机模拟退火方法进行搜索式的程序修复，提出了一种名为注意力剪枝的方法。该方法使用代理（surrogate）深度神经网络来建模注意力头状态（激活/未激活）与其公平性和实用性指标之间的关系，从而能够在代理模型上进行优化，识别需要选择性剪枝的最优注意力头集合。这种方法避免了直接在LLM参数空间中进行搜索。
### Conclusion
注意力剪枝通过关注那些对模型偏见贡献较大的注意力头进行剪枝，同时尽量不影响模型的整体实用性，可以在仅减少40%性别偏见的情况下优于最先进的偏见缓解策略。
## 209. `cs.AI` - 使用多代理强化学习的LLM协作 [PDF](https://arxiv.org/pdf/2508.04652), [HTML](https://arxiv.org/abs/2508.04652)
### Authors
Shuo Liu,Tianle Chen,Zeyu Liang,Xueguang Lyu,Christopher Amato
### Background
多代理系统（MAS）已经被广泛研究用于建模和解决涉及多个相互作用代理的问题。然而，大多数大规模语言模型（LLM）是在独立方式下预训练的，并未专门针对协调进行优化。现有的LLM微调框架依赖于个体奖励，这需要为每个代理设计复杂的奖励机制以促进合作。
### Innovation
本文将LLM协作建模为合作多代理强化学习（MARL）问题，并开发了一种多代理、多回合算法——多代理组相对策略优化（MAGRPO），结合了现有的RL方法和MARL技术。实验证明，使用MAGRPO微调MAS能够使代理通过有效的协作高效生成高质量的响应。
### Conclusion
本文的方法为使用其他MARL方法处理LLM任务打开了大门，并强调了相关挑战。
## 210. `cs.AI` - MGAS: 多粒度架构搜索以权衡模型的有效性与效率 [PDF](https://arxiv.org/pdf/2310.15074), [HTML](https://arxiv.org/abs/2310.15074)
### Authors
Xiaoyun Liu,Divya Saxena,Jiannong Cao,Yuqing Zhao,Penghui Ruan
### Background
神经架构搜索（NAS）在自动化设计神经网络方面取得了重大进展。不同的架构搜索（DAS）方法通过将传统的离散候选采样和评估重新定义为超网的可微优化，然后进行离散化，从而减少搜索时间。然而，大多数现有的DAS方法主要集中在优化粗粒度的操作层拓扑，而忽略了更细粒度的结构，如权重级和滤波器级模式，这限制了它们平衡模型性能与模型大小的能力。另外，许多方法在搜索过程中为了节省内存而牺牲搜索质量。
### Innovation
我们提出了一种名为Multi-Granularity Differentiable Architecture Search (MG-DARTS)的统一框架，旨在通过全面而高效地探索多层次搜索空间，从零开始发现有效且高效的架构。具体来说，我们从两个方面改进了现有的DAS方法：首先，通过学习与随时间演化而改变的架构相关的粒度特异性离散函数，自适应地调整不同粒度层次的可搜索单元的留存比例，实现自适应剪枝。其次，我们将超网络优化和离散化分解为多个阶段，每个阶段操作在一个子网络上，并引入渐进重评估，使先前单元的重新剪枝和再生长成为可能，从而减轻潜在偏差。
### Conclusion
在CIFAR-10、CIFAR-100和ImageNet上的广泛实验表明，MG-DARTS在模型准确性和参数效率的权衡方面优于其他最先进的方法。
## 211. `cs.AI` - Yanyun-3：通过视觉语言模型实现跨平台策略游戏操作 [PDF](https://arxiv.org/pdf/2511.12937), [HTML](https://arxiv.org/abs/2511.12937)
### Authors
Guoyan Wang,Yanyan Huang,Chunlin Chen,Lifeng Wang,Yuxiang Sun
### Background
跨平台的策略游戏自动化是一个挑战，因为不同平台用户界面多样且战场环境动态变化。现有的视觉语言模型在跨平台应用中难以泛化，界面理解和执行动作不够精确。
### Innovation
引入了名为Yanyun-3的基于视觉语言模型的代理，整合了Qwen2.5-VL来进行视觉推理和UI-TARS来执行用户界面操作。提出了组合粒度的新型数据组织原则，对曲率数据集进行了跨三个策略游戏平台的微调。M*V+S策略在BLEU-4得分上提高了12.98倍，推理时间减少了63%。Yanyun-3无需针对特定平台进行微调便能执行关键任务。
### Conclusion
结构化的多模态数据组织显著增强了视觉语言模型在实体任务中的性能。Yanyun-3为GUI自动化提供了一个可移植框架，具有更广泛的机器人技术和自主系统应用潜力。
## 212. `cs.AI` - 基于多输入自动编码器的物联网入侵检测系统引导特征选择 [PDF](https://arxiv.org/pdf/2403.15511), [HTML](https://arxiv.org/abs/2403.15511)
### Authors
Phai Vu Dinh,Diep N. Nguyen,Dinh Thai Hoang,Quang Uy Nguyen,Eryk Dutkiewicz,Son Pham Bao
### Background
物联网数据特征的多样性和泛化虽有助于入侵检测系统（IDS），但也会因数据的异质性和高维度导致训练有效的机器学习模型难度增加，可能产生冗余或噪声特征，降低检测引擎的准确度。
### Innovation
提出了一种名为多重输入自动编码器（MIAE）的新神经网络架构，它包含多个子编码器，用于处理不同来源的不同特性输入。还设计了一个特征选择层（MIAEFS），在特征表示层之后训练，用于提升特征表示中的重要特征并去除冗余特征。实验表明MIAE和MIAEFS在三个IDS数据集上的性能优于其他方法。
### Conclusion
MIAE和MIAEFS结合随机森林（RF）分类器在检测复杂攻击如Slowloris时准确率为96.5%，使用MIAE和MIAEFS表示的RF检测攻击样本的平均运行时间约为1.7×10^-6秒，且模型大小低于1MB。
## 213. `cs.AI` - 时间序列和空间-时间数据的扩散模型综述 [PDF](https://arxiv.org/pdf/2404.18886), [HTML](https://arxiv.org/abs/2404.18886)
### Authors
Yiyuan Yang,Ming Jin,Haomin Wen,Chaoli Zhang,Yuxuan Liang,Lintao Ma,Yi Wang,Chenghao Liu,Bin Yang,Zenglin Xu,Shirui Pan,Qingsong Wen
### Background
扩散模型已在时间序列和空间-时间数据中得到广泛应用，提升了生成、推断及下游应用能力。这类模型被应用于医疗卫生、推荐系统、气候学、能源、音频处理和交通等多个领域。
### Innovation
本文通过对时间序列数据和空间-时间数据的应用进行分类，提供了模型类别、任务类型、数据模态和实际应用领域的结构化视角。这一研究旨在为研究人员和实践者提供坚实的基础，从而激励未来在基于扩散模型的数据挖掘任务和应用中的创新。
### Conclusion
本文旨在提供一个坚实的基础，帮助研究人员和实践者更好地理解和应用扩散模型，在解决传统挑战的同时推动新的解决方案。此外，详细的信息已公开在github仓库中。
## 214. `cs.AI` - KRAL: 知识和推理增强学习以增强LLM辅助临床抗菌治疗 [PDF](https://arxiv.org/pdf/2511.15974), [HTML](https://arxiv.org/abs/2511.15974)
### Authors
Zhe Li,Yehan Qiu,Yujie Chen,Xiang Zhou
### Background
临床抗菌治疗需要动态整合病原体特征、宿主因素、抗菌药物的药理性质及感染的严重程度。这种复杂性对大型语言模型（LLMs）在高风险临床决策中的应用提出了根本限制，包括知识空白、数据隐私问题、高部署成本和有限的推理能力。
### Innovation
提出了KRAL，一种低成本、可扩展、保护隐私的框架。KRAL利用教师模型的推理自动提炼知识和推理轨迹，通过问题到答案的反向生成；采用启发式学习进行半监督数据增强（将手动标注需求减少约80%）；并利用代理强化学习同时增强医疗知识和推理，优化计算和内存效率。同时，利用分层评估减少评估成本，并采用模块化接口设计方便系统更新。实验结果证明，KRAL在外部开源基准MEDQA上的知识问答能力（准确率@1提高了1.8% vs. 半监督微调SFT，和3.6% vs. 检索增强生成RAG）和推理能力（路径@1提高了27% vs. SFT和27.2% vs. RAG）方面优于传统方法，并且长期训练成本仅为SFT的20%。
### Conclusion
KRAL是一种有效的解决方案，用于增强本地LLM的临床诊断能力，实现复杂医疗决策支持中的低成本、高安全性部署。
## 215. `cs.AI` - 价值改进的行动评估算法 [PDF](https://arxiv.org/pdf/2406.01423), [HTML](https://arxiv.org/abs/2406.01423)
### Authors
Yaniv Oren,Moritz A. Zanger,Pascal R. van der Vaart,Mustafa Mert Celikok,Matthijs T. J. Spaan,Wendelin Bohmer
### Background
现代的行动者-评论家（Actor Critic）算法依赖于深度神经网络（DNNs）来参数化行动策略，并通过逐步骤迭代改进策略。然而，这种依赖性暗示着一种基于梯度的改进方式，相对于贪婪操作（如Q学习算法中的贪婪更新）在每一步上更具探索性。另一方面，对于政策稳定性的考量要求对策略进行缓慢的变化，从而在贪婪改进与稳定性之间形成了一种权衡。
### Innovation
本文提出了一种方法，即解耦行动策略与由评论家评估的策略。这样可以允许代理通过更贪婪的更新来更好地改进评论家的策略（如价值改进），同时保持缓慢的梯度基础改进来优化参数化的行动策略。
### Conclusion
通过结合价值改进到流行的离策略行动者-评论家算法TD3和SAC中，显著提升了这些算法在DeepMind连续控制环境中的表现。这一改进在几乎不增加计算和实现成本的前提下取得了显着的效果，并通过对有限期域中的广义策略迭代进行分析，验证了该方法的收敛性。
## 216. `cs.AI` - BMGQ：从半结构化数据自底向上生成复杂多跳推理问题的方法 [PDF](https://arxiv.org/pdf/2510.24151), [HTML](https://arxiv.org/abs/2510.24151)
### Authors
Bingsen Qiu,Zijian Liu,Xiao Liu,Bingjie Wang,Feier Zhang,Yixuan Qin,Chunyan Li,Haoshen Yang,Zeren Gao
### Background
当前，构建可以真正考验模型检索和推理能力的训练数据集仍极具挑战性。虽然已有少数几个评估数据集能够捕捉到难以搜索但容易验证的问题特征，这些数据资源仍然稀缺，且主要设计用于评估，而不适合监督微调或强化学习。此外，人工创建需要多跳推理且不直接可检索的问题耗资巨大且难以扩展，成为训练高能力检索和推理代理的关键数据瓶颈。
### Innovation
BMGQ提供了一种自底向上的自动化方法，可以从半结构化知识源生成高难度的多跳问题。该系统通过自然语言推理(NLI)基于关系类型的证据簇生长、反向问题构建以及质量双重评估管道来实现。这种方法可以生成复杂、检索抗性且可验证的问题，适用于监督微调/强化学习训练以及挑战性评估，并大幅减少人工编撰工作量，同时保留了强大的评估基准的数据难度特征。
### Conclusion
BMGQ通过自动化过程生成复杂多跳推理问题，为训练具有高能力和复杂推理能力的代理提供了新的数据资源，显著降低了人工编撰成本，同时保证了数据难度特征，有助于提高模型的推理和检索能力。
## 217. `cs.AI` - Heterogeneous Multi-Agent Proximal Policy Optimization for Power Distribution System Restoration [PDF](https://arxiv.org/pdf/2511.14730), [HTML](https://arxiv.org/abs/2511.14730)
### Authors
Parya Dolatyabi,Mahdi Khodayar
### Background
恢复大规模停电后电力分配系统（PDS）需要进行一系列开关操作，重新配置馈线拓扑并协调分布式能源资源（DERs），在功率平衡、电压限制和热容量等非线性约束条件下实现。然而，这些挑战使得传统的优化方法和基于价值的强化学习方法计算效率低下且难以扩展。
### Innovation
该论文采用了一种异构代理强化学习（HARL）框架，具体通过异构代理近端策略优化（HAPPO）实现，用于在互联微电网之间协调恢复。每个代理控制不同的微电网，具有不同的负载、分布式能源资源容量和开关数量，引入了实际的结构异质性。通过将分散的演员政策与中央评论家训练相结合，计算优势值以进行稳定的在线策略更新。物理化的OpenDSS环境提供了全功率流动反馈，并通过可微惩罚信号而不是无效动作的掩码来强制执行操作限制。实验结果表明，与DQN、PPO、MAES、MAGDPG、MADQN、均场RL和QMIX相比，HAPPO在收敛速度、恢复功率和多种子训练平滑度方面表现出色。
### Conclusion
结果表明，在HARL框架中纳入微电网级异质性产生了可扩展、稳定、约束感知的复杂PDS恢复解决方案。
## 218. `cs.AI` - 在大型语言模型代理中结合符号控制与神经推理：结构化的认知循环 [PDF](https://arxiv.org/pdf/2511.17673), [HTML](https://arxiv.org/abs/2511.17673)
### Authors
Myung Ho Kim
### Background
大型语言模型代理因其内在基本架构问题而受到限制，例如推理与执行交织在一起、记忆易变性和不可控的动作序列。现有框架如ReAct、AutoGPT和记忆增强方法在解决这些问题上存在关键缺陷。
### Innovation
本文提出了一种模块化架构——结构化认知循环（SCL），它将代理认知明确划分为五个阶段：检索、认知、控制、行动和记忆（R-CCAM）。核心是软符号控制，这是一种适应性的治理机制，将符号约束应用于概率推理，保持神经灵活性的同时恢复经典符号系统的可解释性和可控性。实验证明，SCL在处理多步骤条件推理任务时实现了零策略违反，消除了冗余工具调用，并保持了决策全程可追溯性。
### Conclusion
本文通过模块化分解、适应性符号治理和透明状态管理三个设计原则，为可信赖的代理系统提供了理论指导；同时，该研究强调了SCL在混合智能分类中的定位，并提供了完整的开源实现，展示R-CCAM循环架构，并结合GPT-4o实现实时旅行规划代理，从而提供了一条实用且有理论基础的路径，实现可靠、可解释和可控的AI代理。
## 219. `cs.AI` - Vision Language Models Can Parse Floor Plan Maps [PDF](https://arxiv.org/pdf/2409.12842), [HTML](https://arxiv.org/abs/2409.12842)
### Authors
David DeFazio,Hrudayangam Mehta,Meng Wang,Ping Yang,Jeremy Blackburn,Shiqi Zhang
### Background
Vision Language Models (VLMs)能够同时处理图像和文本，并解决诸如视觉问答和图像字幕等多个任务。这项研究聚焦于地图解析这一新颖任务，在视觉语言模型（VLMs）中尚未探索，但对于自主移动机器人特别有用。地图解析不仅要求理解地标的含义，还要理解地图的几何构型，即理解不同区域的特性及其相互关系。
### Innovation
该研究评估了VLMs在地图解析任务中的性能，通过引导VLMs生成复杂的室内导航任务计划，使它们能够理解并细化复杂地图标签和布局。研究结果表明，VLMs在地图解析任务中表现出色，尤其在需要一系列导航动作的任务中，成功率高达0.96，例如靠近和穿过门。此外，研究还指出，VLMs在大型开阔区域的表现较弱，提供了相关的实际建议，经实验验证。
### Conclusion
研究展示了VLMs在地图解析任务中的潜力，并提出实用建议以解决在大型开阔区域的表现问题。
## 220. `cs.AI` - GRAM: 使用稳健适应模块实现深度强化学习中的泛化 [PDF](https://arxiv.org/pdf/2412.04323), [HTML](https://arxiv.org/abs/2412.04323)
### Authors
James Queeney,Xiaoyi Cai,Alexander Schperberg,Radu Corcodel,Mouhacine Benosman,Jonathan P. How
### Background
在现实世界的应用中可靠部署深度强化学习需要其在各种条件下的泛化能力，包括训练过程中遇到的内部分布场景以及尚未见过的新颖外部分布场景。现有的框架往往在处理这两种持续性泛化上的表现不佳。
### Innovation
该研究提出了一种融合内部和外部泛化的框架——GRAM。它通过引入一个稳健适应模块来识别和应对内部和外部环境动态，结合内部分类和外部鲁棒性的共同训练管道，实现强大的泛化性能。
### Conclusion
通过广泛的模拟和硬件测试，GRAM在不同类型的场景下表现出色。实验结果表明，在低级别的机器人四足行走中，GRAM能够有效应对各种内部和外部环境动态的变化。
## 221. `cs.AI` - VidComposition: Can MLLMs Analyze Compositions in Compiled Videos? [PDF](https://arxiv.org/pdf/2411.10979), [HTML](https://arxiv.org/abs/2411.10979)
### Authors
Yolo Y. Tang,Junjia Guo,Hang Hua,Susan Liang,Mingqian Feng,Xinyang Li,Rui Mao,Chao Huang,Jing Bi,Zeliang Zhang,Pooyan Fazli,Chenliang Xu
### Background
随着多模态大型语言模型（MLLMs）的进步，它们在视频理解方面的性能得到了显著提升。然而，现有的评估基准主要关注抽象的视频理解，缺乏对模型理解和解析视频编排能力的细化评估。视频编排涉及视觉元素如何在复杂编排的视频场景中结合与交互。
### Innovation
我们提出了VidComposition，这是一种专门用于评估MLLMs视频编排理解能力的新基准。VidComposition包含了982个视频和1706个多项选择题，涵盖了摄像头运动、角度、构图、叙事结构、人物动作和情绪等多个方面。评估结果显示，人类在复杂编排视频的理解上远超模型，这揭示了当前MLLMs在这方面的局限性，并为改进提供了方向。
### Conclusion
我们的综合评估显示了人类与模型在复杂编排视频理解上的显著性能差距，表明当前MLLMs在理解复杂视频编排方面存在不足。VidComposition可用于进一步研究和改进MLLMs对视频编排的理解能力，同时提供了排行榜和评估代码供社区使用。
## 222. `cs.AI` - 大型语言模型中的越狱与漏洞缓解 [PDF](https://arxiv.org/pdf/2410.15236), [HTML](https://arxiv.org/abs/2410.15236)
### Authors
Benji Peng,Keyu Chen,Qian Niu,Ziqian Bi,Ming Liu,Pohsun Feng,Tianyang Wang,Lawrence K.Q. Yan,Yizhu Wen,Yichao Zhang,Caitlyn Heqi Yin,Xinyuan Song
### Background
大型语言模型（LLMs）通过提升自然语言理解和生成能力，推动了人工智能的发展，并在医疗、软件工程和对话系统等多领域得到应用。然而，尽管在过去几年中取得了显著进步，LLMs也显示出对注入攻击和模型劫持等攻击的显著脆弱性。本研究综述了对这些漏洞的研究现状，并提出了可用的防御策略。
### Innovation
研究对攻击方法进行了粗略分类，包括基于提示、基于模型、跨模态和多语种的方法，涵盖了对抗提示、后门注入和跨模态利用等技术。同时，综述了各种防御机制，包括提示过滤、提示转换、对齐技术、多代理防御和自我调节，评估了它们的优势与不足。
### Conclusion
指出现有研究的空白，建议未来的研究方向包括稳健对齐策略、先进的防御措施对抗不断演变的攻击、自动检测劫持、以及考虑伦理和社会影响。本研究强调了需要在AI社区内继续进行研究与合作，以提高LLM的安全性，并确保其安全部署。
## 223. `cs.AI` - 搜索潜在程序空间 [PDF](https://arxiv.org/pdf/2411.08706), [HTML](https://arxiv.org/abs/2411.08706)
### Authors
Matthew V Macfarlane,Clement Bonnet
### Background
通用人工智能需要系统能够高效地学习新技能并超越其训练分布进行泛化。尽管程序合成方法具有强泛化能力，但它们面临由于组合空间庞大而导致的可扩展性问题，这使得它们迅速变得不可行，需要依赖人工生成的DSL或预训练的先验知识来缩小搜索空间。另一方面，深度学习方法取得了巨大成功，但它们缺乏结构化的测试时适应性，依赖大量的随机采样或昂贵的梯度更新进行微调。
### Innovation
本文提出了潜入程序网络（LPN），这是一种新颖的架构，在神经模型中直接嵌入测试时搜索。LPN学习一个潜在空间中的隐式程序，通过梯度测试时搜索连接输入和输出。LPN结合了符号方法的灵活性和神经方法的可扩展性，在测试时通过一个紧凑的潜在空间进行搜索，避免了预定义领域特定语言的需求。在一系列的编程实例任务中，LPN的表现要么优于，要么与其相比相当的内文学习和测试时训练方法的表现。在ARC-AGI基准测试上，LPN展示了它能够学习一个紧凑的程序空间并测试时搜索以适应新任务的能力。在测试时开启搜索时，LPN在离分布任务上的性能翻倍。
### Conclusion
潜入程序网络（LPN）结合了符号方法的灵活性和神经方法的可扩展性，在测试时通过一个紧凑的潜在空间进行搜索，从而无需依赖于预定义的领域特定语言。LPN在一系列编程实例任务上的表现优于或与现有的内文学习和测试时训练方法相当，特别是在处理离分布任务时性能显著提升。
## 224. `cs.AI` - 揭开高阶图神经网络的神秘面纱 [PDF](https://arxiv.org/pdf/2406.12841), [HTML](https://arxiv.org/abs/2406.12841)
### Authors
Maciej Besta,Florian Scheidl,Lukas Gianinazzi,Grzegorz Kwasniewski,Shachar Klaiman,Jürgen Müller,Torsten Hoefler
### Background
高阶图神经网络（HOGNNs）和相关的高阶拓扑深度学习架构是一种重要的GNN模型类别，它们可以利用超越简单边的顶点之间的多边关系。这些模型被用于解决过度平滑或过度压缩的问题，显著提高GNN预测的准确性，增强GNN架构的表达性，以及其他多种目标。众多的HOGNN模型已经被引入，它们带来了多样化的神经网络架构，甚至对“高阶”的定义也不尽相同。这种多样性使得正确分析、比较HOGNN模型以及确定在何种场景下使用特定模型变得非常具有挑战性。
### Innovation
该研究首先设计了一套深入的税收分类和蓝图，有助于设计出性能优化的模型。接着，利用这个分类来分析和比较现有的HOGNN模型。通过分析的结果，提出了指导性见解，以帮助在给定场景下选择最具益处的GNN模型，并列出了进一步研究更加强大的HOGNN模型的挑战和机遇。
### Conclusion
该研究合成了一系列见解，帮助选择最适合特定场景的GNN模型，并提出了进一步研究更高级HOGNN模型的挑战和机遇。
## 225. `cs.AI` - BiasJailbreak：分析大型语言模型中的道德偏差和越狱漏洞 [PDF](https://arxiv.org/pdf/2410.13334), [HTML](https://arxiv.org/abs/2410.13334)
### Authors
Isack Lee,Haebin Seong
### Background
尽管大型语言模型（LLMs）在各种任务上表现出色，但也存在安全隐患，比如被称为‘jailbreaks’的现象，即恶意输入可以诱使LLMs生成有害内容，这绕过了安全性对齐。本文深入探讨了LLMs中的道德偏差如何可能被利用来制造这些漏洞，并展示了这些偏差如何在GPT-4o模型中通过对非二元和异性认同关键词以及白人和黑人关键词的影响程度不同（分别相差20%和16%）来影响生成内容的安全性。
### Innovation
研究引入了BiasJailbreak的概念，这是利用LLMs自身生成具有偏差的关键词，进而生成有害输出的新型概念。此外，还提出了一种高效的防御方法BiasDefense，该方法在生成前插入防御提示来防止越狱尝试。与Guard Models（如Llama-Guard）相比，BiasDefense在文本生成后不需要额外的推理成本。
### Conclusion
研究强调了LLMs中的道德偏差实际上会导致生成不安全的输出，并提出了一种使LLMs更安全和减少偏见的方法。为了促进进一步的研究和改进，我们将BiasJailbreak的代码和资源开源，为社区提供理解和减轻LLMs中由安全性引发的偏差的工具。
## 226. `cs.AI` - 多域综合分布下的跨域时间序列预测的领域融合可控泛化 [PDF](https://arxiv.org/pdf/2412.03068), [HTML](https://arxiv.org/abs/2412.03068)
### Authors
Xiangkai Ma,Xiaobin Hong,Mingkai Lin,Han Zhang,Wenzhong Li,Sanglu Lu
### Background
传统的深度模型在时间序列预测方面取得了前所未有的成功，但面对跨域泛化的挑战，现有研究利用统计先验作为提示工程在各领域巨大分布偏移的情况下失败。因此，亟需一种能够系统地将来自多个时间序列域的信息整合到一个统一生成过程中的新方法，特别是在跨域时间序列预测中。
### Innovation
本文提出了一种新颖的时间序列统一生成模型（TimeControl），这是一种首创的领域融合范式，通过扩散模型系统地将来自多个时间序列域的信息整合到一个统一的生成过程中。该模型包含三种关键设计：一是条件网络捕获观察序列中的多尺度波动模式，并作为上下文表示引导去噪网络生成预测序列；二是基于适配器的微调策略，在预训练阶段学习到的多域通用表示应用于目标域的下游任务；三是设计了一种新颖的混合架构，使TimeControl能够灵活生成任意长度的预测序列。
### Conclusion
在广泛实验中，TimeControl在49个基准和30个基线上表现出色，特别是在所有数据域上均优于现有基线，展示了卓越的零样本泛化能力。
## 227. `cs.AI` - Mixture of Attention Spans: Optimizing LLM Inference Efficiency with Heterogeneous Sliding-Window Lengths [PDF](https://arxiv.org/pdf/2406.14909), [HTML](https://arxiv.org/abs/2406.14909)
### Authors
Tianyu Fu,Haofeng Huang,Xuefei Ning,Genghan Zhang,Boju Chen,Tianqi Wu,Hongyi Wang,Zixiao Huang,Shiyao Li,Shengen Yan,Guohao Dai,Huazhong Yang,Yu Wang
### Background
现有的长上下文语言模型（LLMs）的注意力机制在硬件效率方面面临着内存和吞吐量的挑战。此前的方法通常使用固定长度的窗口来处理所有注意力头和输入大小，但这种方法未能捕捉到LLMs中固有的异质注意力模式，忽略了它们独特的准确性和延迟权衡。
### Innovation
本文提出了Mixture of Attention Spans（MoA）方法，该方法自动为不同的注意力头和层定制独特的滑动窗口长度配置，通过构建和导航不同窗口长度及其相对于输入大小的缩放规则的搜索空间，MoA可以优化模型的推理效率。实验结果表明MoA相比均匀窗口基线，在相同平均滑动窗口长度的情况下，有效上下文长度增加了3.9倍，并且检索精度提升了1.5-7.1倍；此外，MoA使得对三个长上下文理解基准的性能差距从9%-36%缩小到了5%以内。此外，MoA还能减少1.2-1.4倍的GPU内存使用，提高了6.6-8.2倍的解码吞吐量和1.7-1.9倍的速度，基本上不影响性能。
### Conclusion
本文提出了一种新的方法MoA，该方法通过为不同的注意力头和层定制独特的滑动窗口长度配置，显著提高了LLMs的推理效率，同时减少了GPU内存使用，大幅提升了解码吞吐量，且对性能影响较小。
## 228. `cs.AI` - 重新思考扩展测试时计算能力时的微调：限制置信度提高数学推理能力 [PDF](https://arxiv.org/pdf/2502.07154), [HTML](https://arxiv.org/abs/2502.07154)
### Authors
Feng Chen,Allan Raventos,Nan Cheng,Surya Ganguli,Shaul Druckmann
### Background
最近大型语言模型（LLMs）的发展强调了扩大测试时计算资源可以实现复杂任务（如数学推理和代码生成）的强大能力。然而，这提出了一个关键问题：如何在后续测试时计算资源和预算的优化下调整模型训练？本文专注于pass@N这一简单的测试时策略，即在N个独立样本中寻找正确答案。研究表明，使用交叉熵（CE）损失的训练可能与pass@N目标不一致，即CE损失下的训练会随时间延长使得pass@N准确率下降。
### Innovation
本文揭示了CE损失导致模型自信过度的问题，并通过实验验证了过高的置信度是用pass@N扩展测试时计算能力的障碍。提出了一种新的训练损失函数，通过限制模型的置信度提高与pass@N策略的一致性。并在MATH和MiniF2F基准测试中展示了改进的数学推理能力。
### Conclusion
本文的工作强调了需要同时设计传统的LLM开发阶段：训练时协议和测试时搜索及推理策略的重要性。
## 229. `cs.AI` - 生成式AI在传统赛璐珞动画中的应用：综述 [PDF](https://arxiv.org/pdf/2501.06250), [HTML](https://arxiv.org/abs/2501.06250)
### Authors
Yolo Y. Tang,Junjia Guo,Pinxin Liu,Zhiyuan Wang,Hang Hua,Jia-Xing Zhong,Yunzhong Xiao,Chao Huang,Luchuan Song,Susan Liang,Yizhi Song,Liu He,Jing Bi,Mingqian Feng,Xinyang Li,Zeliang Zhang,Chenliang Xu
### Background
传统的赛璐珞动画生产流程涉及多个关键步骤，包括分镜头剧本创作、场景设计、关键帧动画制作、插入帧制作和上色。这些步骤需要大量的手工劳动、技术专长和大量时间成本。这些挑战历来阻碍了传统赛璐珞动画的效率和可扩展性。随着生成式人工智能（GenAI）的发展，包括大型语言模型、多模态模型和扩散模型的兴起，提供了一种新的解决方案，通过自动化插入帧生成、上色和分镜头剧本创作等任务，以提高效率和降低成本。
### Innovation
生成式人工智能（GenAI）正通过自动化关键步骤，如插入帧生成、上色和分镜头剧本创作，改善传统赛璐珞动画的工作流程。借助人工智能工具，例如AniDoc、ToonCrafter和AniSora，降低了技术壁垒，使更多的创作者能够参与制作，使艺术家们能够更多地专注于创造性表达和艺术创新。然而，视觉一致性、风格统一性以及伦理考虑等挑战仍然存在。
### Conclusion
尽管存在挑战，生成式人工智能在动画领域的应用正在迅速发展。此外，该论文还探讨了AI辅助动画领域的未来方向和进展。进一步的探索和资源请访问我们的GitHub存储库：this https URL
## 230. `cs.AI` - 带有组织层分割意识的生成强化网络（GRN）在三维超声图像中的组织层分割以评估慢性低背痛（cLBP） [PDF](https://arxiv.org/pdf/2501.17690), [HTML](https://arxiv.org/abs/2501.17690)
### Authors
Zixue Zeng,Xiaoyan Zhao,Matthew Cartier,Tong Yu,Jing Wang,Xin Meng,Zhiyu Sheng,Maryam Satarpour,John M Cormack,Allison Bean,Ryan Nussbaum,Maya Maurer,Emily Landis-Walkenhorst,Dinesh Kumbhare,Kang Kim,Ajay Wasan,Jiantao Pu
### Background
该研究旨在优化三维超声图像中的组织层分割，以便更有效地评估慢性低背痛（cLBP）。目前的分割方法需要大量的人工标注数据，这在实际应用中是劳动密集型和成本高的。
### Innovation
提出了一个名为生成强化网络（GRN）的新颖分割感知联合训练框架，该框架在单阶段中结合了分割损失反馈，以优化图像生成和分割性能。此外，还开发了一种称为分割指导增强（SGE）的图像增强技术，以及两个变体——适应样本高效学习（GRN-SEL）和半监督学习（GRN-SSL）的GRN。
### Conclusion
实验结果表明，当结合SGE时，GRN-SEL可将标注工作量减少至最多70%，同时DSC性能提升1.98%；单独使用GRN-SEL和GRN-SSL时，均可将标注工作量减少到最多60%，但保持性能与完全监督模型相当。这表明GRN框架在使用显著减少的标记数据下优化分割性能的有效性，为超声图像分析提供了一个可扩展和高效的解决方案，减轻了数据注释相关的负担。
## 231. `cs.AI` - Ontology-Aware RAG for Improved Question-Answering in Cybersecurity Education [PDF](https://arxiv.org/pdf/2412.14191), [HTML](https://arxiv.org/abs/2412.14191)
### Authors
Chengshuai Zhao,Garima Agrawal,Fan Zhang,Tharindu Kumarage,Zhen Tan,Yuli Deng,Ying-Chih Chen,Huan Liu
### Background
将AI整合到教育中，特别是在网络安全课程的教学上，具有巨大的潜力。AI驱动的问答（QA）系统能够积极管理网络安全问题解决过程中的不确定性，提供互动和探究式的教学体验。大型语言模型（LLMs）在AI驱动的QA系统中越来越突出，但同时也面临着幻觉（提供虚假信息）和有限的专业领域知识等挑战，这降低了其在教育环境中的可靠性。
### Innovation
本文提出了一种名为CyberRAG的方法，这是一种基于本体的检索增强生成（RAG）方法，旨在提高网络安全教育中AI驱动QA系统的可靠性和安全性。该方法通过两步来增强且验证相关领域知识，并通过结合知识图谱本体来验证最终答案，从而减少了幻觉和误用问题。
### Conclusion
全面的实验结果表明，CyberRAG能够提供与领域知识一致的准确且可靠的回答，展示了AI工具在教育中的巨大潜力。
## 232. `cs.AI` - 全景失真感知分块化在上方鱼眼图像中的人体检测与定位 [PDF](https://arxiv.org/pdf/2503.14228), [HTML](https://arxiv.org/abs/2503.14228)
### Authors
Nobuhiko Wakai,Satoshi Sato,Yasunori Ishii,Takayoshi Yamashita
### Background
在上方鱼眼图像中进行人体检测具有挑战性，因为人体可能会旋转且人体尺寸较小。尽管前人研究主要解决了人体旋转问题，但小体型人体的问题尚未得到充分探索。我们通过将鱼眼图像映射到等径全景图来处理旋转，并利用全景几何来更有效地应对小型人体问题。传统的检测方法倾向于优先关注较大的人体，因为在注意力图中占主导地位，导致较小的人体容易被遗漏。在半球等径全景图中，我们发现图像顶部附近的垂直角度与人体显得高度呈线性关系减小。基于此发现，我们提出了全景失真感知分块化方法来增强小体型人体的检测效果。
### Innovation
这种方法通过等径全景图重组和分块化过程，提出了一种能够有效检测小体型人体的检测与定位方法。利用自相似图形实现分块，避免了分块过程中的空隙，并通过保留每个分块组中最大显著值来保留小体型人体的关键区。最后结合等径全景图重组与分块化方法，实现一种基于变压器的人体检测与定位方法。
### Conclusion
大量的实验表明，该方法在大规模数据集上优于传统方法。
## 233. `cs.AI` - 拉回吸引子维度在循环神经网络中的研究 [PDF](https://arxiv.org/pdf/2501.11357), [HTML](https://arxiv.org/abs/2501.11357)
### Authors
Muhammed Fadera
### Background
循环神经网络通过水槽计算范式的训练，在学习和重构来自混沌系统的吸引子方面表现出显著的成功，通常复制诸如李雅普un洛夫指数和分形维度等量。有研究表明，这一点可能是由于水槽计算嵌入了混沌系统的动力学。这一猜想在具有线性激活函数的水槽系统中得到了证明，但对于更一般的水槽系统仍是一个开放问题。
### Innovation
该研究采用非自主动力系统的方法，建立了拉回吸引子盒计数维数的上界。证明了拉回吸引子的盒计数维数不超过输入序列空间的盒计数维数。特别地，对于来源于N维光滑动力系统的输入序列或其常规可微观察，拉回吸引子的盒计数维数不超过N。该研究结果强调了虽然水槽计算机具有非常高维的状态空间，但其实际表现出有效的低维动力学。
### Conclusion
研究发现进一步解释了水槽计算机在吸引子重构和计算动态不变量（如李雅普un洛夫指数和分形维度）任务上的成功之处，突出了其潜在的低维动态性质。
## 234. `cs.AI` - Position: 超越欧几里得——基础模型应采纳非欧几里得几何 [PDF](https://arxiv.org/pdf/2504.08896), [HTML](https://arxiv.org/abs/2504.08896)
### Authors
Neil He,Jiahong Liu,Buze Zhang,Ngoc Bui,Ali Maatouk,Menglin Yang,Irwin King,Melanie Weber,Rex Ying
### Background
在基础模型和大规模语言模型（LLMs）的时代，欧几里得空间已成为机器学习架构的默认几何环境。然而，最新文献表明，这种选择带来了根本性的局限性。随着数据规模的增长，现实世界的数据常常展现出多向关系、层次结构、对称性和非各向同性缩放等内在的非欧几里得结构，这些结构广泛存在于语言、视觉和自然科学领域中。对于这些结构，用欧几里得空间进行有效建模是非常具有挑战性的。该立场论文认为，超越欧几里得几何不仅是可选的增强技术，更是接下来一代基础模型保持规模法则的必要性。
### Innovation
本文提出了一个重要的观点，即扩展基础模型的几何环境，从纯粹的欧几里得空间扩展到非欧几里得几何，以更好地捕捉和利用数据中存在的内在结构。通过适应性的任务结构调整嵌入，基础模型可以更高效地利用这些结构，提高表达能力。
### Conclusion
本文支持这一观点通过一系列基于理论和实证研究的结果，并给出了将非欧几里得几何纳入基础模型的路线图，包括通过微调、从头训练和混合方法建立几何基础模型的策略。
## 235. `cs.AI` - 理解与优化多阶段AI推理管道 [PDF](https://arxiv.org/pdf/2504.09775), [HTML](https://arxiv.org/abs/2504.09775)
### Authors
Abhimanyu Rajeshkumar Bambhaniya,Hanjiang Wu,Suvinay Subramanian,Sudarshan Srinivasan,Souvik Kundu,Amir Yazdanbakhsh,Midhilesh Elavazhagan,Madhu Kumar,Tushar Krishna
### Background
大规模语言模型（LLMs）的迅速发展推动了更复杂推理管道和硬件平台的需求。现代LLM服务超越了传统的预填充-解码工作流程，采用了多阶段过程如检索增强生成（RAG）、键-值（KV）缓存检索、动态模型路由和多步推理。这些阶段具有不同的计算需求，需要集成了GPU、ASIC、CPU和内存中心架构的分布式系统。然而，现有的模拟器无法准确建模这些异构、多引擎工作流程，限制了其为架构决策提供信息的能力。
### Innovation
HERMES，一种异构多阶段LLM推理执行模拟器，是该领域的创新。HERMES可以建模多样的请求阶段，包括RAG、KV检索、推理、预填充和解码。与之前的框架不同，HERMES支持异构客户端并发执行多个模型，并整合了高级批量策略和多层次内存层次结构。通过结合实际硬件轨迹和分析建模，HERMES捕捉到了混合CPU加速部署中的关键权衡，如内存带宽争用、跨集群通信延迟和批量效率。
### Conclusion
通过案例研究，HERMES探索了推理阶段对端到端延迟的影响、混合管道中最佳批量策略以及远程KV缓存检索的架构影响。HERMES使系统设计者能够在LLM推理不断变化的环境中导航，并提供优化硬件-软件协同设计的实用洞察，以适应下一代AI工作负载。
## 236. `cs.AI` - 通过基于扩散的投影完成推进有限角度CT重建 [PDF](https://arxiv.org/pdf/2505.19385), [HTML](https://arxiv.org/abs/2505.19385)
### Authors
Jiaqi Guo,Santiago Lopez-Tapia,Aggelos K. Katsaggelos
### Background
有限角CT（LACT）由于缺乏角度信息而面临重大挑战。以往的方法多在图像域上操作，而本文提出一种新的方法，专注于投数量子填空。该方法利用一种新型的扩散模型，即MR-SDEs，这是一种用均值回复型随机微分方程描述扩散过程的模型，用于在投影级别填充缺少的角度数据。
### Innovation
本文提出了一种基于扩散的投影填补方法，通过利用MR-SDEs模型来填补缺失的角度数据，同时结合蒸馏技术及用解影算子约束模型输出加速扩散过程，并有效提高了效率和准确性。最后通过后处理模块将填补后的投数量子回投影到图像域，进一步细化重建，抑制伪影并保留关键结构细节。
### Conclusion
定量实验结果显示，所提方法在感知质量和保真度方面均达到最先进的性能，为科学和临床应用中的LACT重建提供了颇有前景的解决方案。
## 237. `cs.AI` - ExDDV：视频可解释深fake检测的新数据集 [PDF](https://arxiv.org/pdf/2503.14421), [HTML](https://arxiv.org/abs/2503.14421)
### Authors
Vlad Hondru,Eduard Hogea,Darian Onchis,Radu Tudor Ionescu
### Background
随着生成视频的逼真度和质量不断提高，人类越来越难以分辨深fake内容，因此不得不依赖自动深fake检测器。然而，这些检测器也容易出错，且其决策过程不可解释，使人类面临深fake诈骗和虚假信息的风险。
### Innovation
该论文提出了ExDDV，这是首个用于可解释深fake检测的视频数据集和基准。ExDDV包含约5400个真实和深fake视频，这些视频经过人工标注，附有文本描述（解释艺术缺陷）和点击点（指出艺术缺陷）。研究者评估了几种视觉-语言模型在ExDDV上的表现，通过不同的微调和上下文学习策略进行实验。结果显示，文本和点击的监督对于开发能够定位并描述所观察到的缺陷的稳健可解释模型都是必要的。
### Conclusion
研究团队开发了一个全新的数据集和复现结果的代码，并在论文末尾提供了相关链接，以支持其他研究者进行进一步研究和改进。
## 238. `cs.AI` - LLM解释在生成任务中的反事实模拟性 [PDF](https://arxiv.org/pdf/2505.21740), [HTML](https://arxiv.org/abs/2505.21740)
### Authors
Marvin Limpijankit,Yanda Chen,Melanie Subbiah,Nicholas Deas,Kathleen McKeown
### Background
大语言模型（LLMs）具有不确定性，在提示稍有改变时输出可能会产生意想不到的变化。因此，准确解释模型行为的能力变得至关重要，尤其是在高风险场景中。反事实模拟性是一种评估模型解释的有效方法，它衡量的是解释如何帮助用户预测模型在相关反事实情况下的输出。尽管反事实模拟性之前已经在二选一问题回答任务中得到研究，但尚未对其进行扩展以适用于生成任务。
### Innovation
本文提供了一个通用框架，用于将反事实模拟性方法扩展到生成任务，并提供了新闻摘要和医疗建议作为使用案例。研究表明，在总结生成任务中，模型解释确实帮助用户更好地预测反事实情况下的输出，但在医疗建议任务中仍有改进空间。
### Conclusion
我们的研究结果表明，反事实模拟性的评估可能更适用于技能型任务，而不是知识型任务。
## 239. `cs.AI` - AReaL：一种用于语言推理的大规模异步强化学习系统 [PDF](https://arxiv.org/pdf/2505.24298), [HTML](https://arxiv.org/abs/2505.24298)
### Authors
Wei Fu,Jiaxuan Gao,Xujie Shen,Chen Zhu,Zhiyu Mei,Chuyi He,Shusheng Xu,Guo Wei,Jun Mei,Jiashu Wang,Tongkai Yang,Binhang Yuan,Yi Wu
### Background
强化学习（RL）已成为训练大型语言模型（LLMs）的一种主导范式，特别适用于推理任务。有效的RL对于LLMs来说需要大规模并行化处理，这提出了一种高效训练系统的迫切需求。现有的大多数大规模RL系统都是同步的，其在同一批设置下进行生成和训练的交替操作，每个训练批次中的滚动数据由同一模型生成。这种方法稳定了RL训练，但存在着严重的系统效率低下问题：生成阶段必须等待批量中最长输出完成之后才能进行模型更新，导致GPU使用不足。
### Innovation
我们提出了AReaL，一种完全异步的RL系统，完全解耦了生成和训练。在AReaL中，滚动工作者连续生成新的输出而不等待，而训练工作者在收集一批数据时即可更新模型。AReaL还结合了一系列系统级优化措施，这使得GPU利用率大大提高。为了稳定RL训练，AReaL平衡了滚动工作者和训练工作者的工作负载以控制数据陈旧性，并采用了一个增强的RealPPO变体来更好地处理过时的训练样本。
### Conclusion
在数学和代码推理基准测试中的广泛实验表明，AReaL与相同数量的GPU相比，与同步系统相比，实现了最高2.77倍的训练加速，同时匹配或提高了最终性能。AReaL的代码可以在以下链接获取：this https URL.
## 240. `cs.AI` - RoPECraft：基于轨迹引导的RoPE优化无训练运动转移方法 [PDF](https://arxiv.org/pdf/2505.13344), [HTML](https://arxiv.org/abs/2505.13344)
### Authors
Ahmet Berke Gokmen,Yigit Ekin,Bahri Batuhan Bilecen,Aysegul Dundar
### Background
近年来，扩散变换器在视频运动转移任务中取得了显著成果，但大多需要通过训练小模型来优化变换过程，消耗了大量资源。为此，该研究提出了RoPECraft，一种无需训练的、基于旋转位置嵌入（RoPE）优化的视频运动转移方法。
### Innovation
RoPECraft首次提出利用密集的光学流从参考视频提取运动偏移，并通过这一过程中的轨迹对齐优化旋转位置嵌入（RoPE），将运动直接编码进生成过程。此外，该方法还引入基于参考视频傅里叶变换的相位分量的正则化项，以降低高频伪影，从而使生成的输出更加忠实于文本提示并防止重复生成。
### Conclusion
在基准测试中的实验表明，RoPECraft超越了所有最近发布的相关方法，在定性和定量测试方面均表现优异。
## 241. `cs.AI` - IVY-FAKE：图像和视频AIGC检测的统一可解释框架和基准 [PDF](https://arxiv.org/pdf/2506.00979), [HTML](https://arxiv.org/abs/2506.00979)
### Authors
Changjiang Jiang,Wenhui Dong,Zhonghao Zhang,Chenyang Si,Fengchang Yu,Wei Peng,Xinbin Yuan,Yifei Bi,Ming Zhao,Zian Zhou,Caifeng Shan
### Background
随着生成式人工智能内容(AIGC)技术的快速发展，虽然生成了高质量的合成内容，但也带来了重大的安全问题。当前的检测方法主要面临两大挑战：（1）缺少多维度可解释的生成图像和视频数据集，现有的开源数据集（如WildFake、GenVideo）依赖于简化的二元注释，这限制了训练检测器的解释性和可信度；（2）现有的基于机器学习模型的伪造检测器（如FakeVLM）的解释性不足，缺乏详细的推理步骤，这妨碍了可靠定位和解释。
### Innovation
为了解决这些挑战，本文提出了Ivy-Fake，它是一个大规模的多模态可解释AIGC检测基准，包括超过106,000个丰富的注释训练样本（图像和视频）和5,000个手动验证的评估样本，其中样本来自多个生成模型和真实世界的数据集，确保了多样性和质量。此外，本文还提出了一种基于组相对策略优化（GRPO）的强化学习模型Ivy-xDetector，能够生成可解释的推理链并展现出高水平的检测性能。
### Conclusion
广泛的实验表明，本方法在GenImage数据集上的性能提高了从86.88%到96.32%，明显优于之前的最先进方法。
## 242. `cs.AI` - 使用LLM代理模拟宏观经济预期 [PDF](https://arxiv.org/pdf/2505.17648), [HTML](https://arxiv.org/abs/2505.17648)
### Authors
Jianhao Lin,Lexuan Sun,Yixin Yan
### Background
本研究介绍了使用大型语言模型（LLM）代理来模拟宏观经济预期的新框架。通过构建具备各种功能模块的LLM代理，该研究复制了三个代表性的调研实验，涵盖了不同类型经济主体的多个预期。现有的研究表明，虽然LLM代理模拟的预期比人类的更加一致，但它们始终优于仅依赖提示工程的LLM，且具备类似人类的心理机制。评估显示，这些能力来自于其组件的贡献，为架构设计提供了指导。
### Innovation
该研究提出了一种新颖的框架，即使用LLM代理来模拟宏观经济预期。通过复制三个代表性的调查实验，展示了LLM代理在模拟预期方面优于仅依赖提示工程的LLM，具有类似人类的心理机制。研究成果为理解AI在宏观经济研究中的行为科学提供了新的见解。
### Conclusion
该研究展示出，虽然LLM代理模拟的预期更为一致，但它们在模拟预期方面的表现优于简单的提示工程方法，具有类似人类的心理机制。这种能力来源于其组件的贡献，为AI在宏观经济研究中的行为科学提供了新的理解，同时也为代理架构的设计提供了指导。
## 243. `cs.AI` - DisCO: 使用判别约束优化强化大型因果模型 [PDF](https://arxiv.org/pdf/2505.12366), [HTML](https://arxiv.org/abs/2505.12366)
### Authors
Gang Li,Ming Lin,Tomer Galanti,Zhengzhong Tu,Tianbao Yang
### Background
近期，DeepSeek-R1的成功及其开放性引起了对作为大型因果模型（LRMs）强化学习方法的组相对策略优化（GRPO）的关注。本研究聚焦于GRPO在二元奖励设置下的目标，并揭示了其内部的难度偏向问题。进一步的研究还指出了GRPO与监督学习传统判别方法之间的联系。
### Innovation
提出了一个新的判别约束优化（DisCO）框架，用于强化LRMs。它与GRPO及其变体的主要区别在于：（1）使用得分类目标替换组相对目标；（2）摒弃基于修剪的代理目标，使用非修剪的RL代理目标作为评分函数；（3）采用简单却有效的约束优化方法以强制Kullback-Leibler（KL）散度约束。DisCO相比GRPO及改进版DAPO具有明显优势，包括完全消除难度偏向，通过非修剪评分函数和约束优化方式解决熵稳定性问题，以及能够采用先进的判别学习技术来解决数据不平衡问题。
### Conclusion
在增强SFT微调模型的数学推理能力方面的实验显示，DisCO显著优于GRPO及其改进变体DAPO，在1.5B模型的六个基准任务中，平均分别提高了7%和6%的表现。
## 244. `cs.AI` - HoliSafe：视觉语言模型的全面安全基准与建模 [PDF](https://arxiv.org/pdf/2506.04704), [HTML](https://arxiv.org/abs/2506.04704)
### Authors
Youngwan Lee,Kangsan Kim,Kwanyong Park,Ilcahe Jung,Soojin Jang,Seanie Lee,Yong-Ju Lee,Sung Ju Hwang
### Background
尽管已经采取了努力来提高视觉语言模型（VLMs）的安全性，但当前的方法仍存在两个主要缺陷：1) 当前的安全调优数据集和基准只部分考虑了图像-文本交互可能产生的有害内容，通常忽视了看似无害但实际存在安全隐患的配对可能导致的结果，这使得VLMs在未知配置中容易受到锁释放攻击。2) 前瞻性方法主要依赖于数据驱动的调优，缺乏内在增强安全性的架构创新。
### Innovation
本文通过引入一个全面的安全数据集和基准HoliSafe，填补了这一空白。HoliSafe涵盖了所有五种安全/不安全的图像-文本组合，为训练和评估提供了更坚实的依据（HoliSafe-Bench）。此外，本文还提出了一种新颖的模块化框架，通过视觉防护模块（VGM）增强VLM的安全性，该模块能够评估输入图像对VLM的有害性，赋予VLM双重功能：它们不仅学习生成更安全的响应，还可以提供可解释的有害性分类，以证明其拒绝决策的合理性。VGM具有模块化设计，作为插件组件，可以无缝集成到各种规模的预训练VLM中。实验表明，在我们的HoliSafe上进行安全训练的Safe-VLM与VGM相结合，在多个VLM基准测试中达到了最先进的安全性能。
### Conclusion
HoliSafe-Bench本身还揭示了现有VLM模型的关键漏洞。我们希望HoliSafe和VGM能够激发更多关于稳健且可解释的VLM安全性的研究，扩展未来多模态对齐的途径。
## 245. `cs.AI` - 您的预训练LLM其实是无监督的置信度校正器 [PDF](https://arxiv.org/pdf/2505.16690), [HTML](https://arxiv.org/abs/2505.16690)
### Authors
Beier Luo,Shuoyuan Wang,Sharon Li,Hongxin Wei
### Background
对于预训练语言模型(PLM)，通过后训练来适应人类偏好和下游任务是必要的。然而，后训练的语言模型（PoLM）往往会表现出过度自信，对正确和错误的输出都赋予较高的置信度，这在关键应用中会削弱可靠性。而解决这一问题的一大障碍是细粒度有标签数据的匮乏。因此，本文提出了一种新的无监督方法Disagreement-Aware Confidence Alignment (DACA)来优化后训练置信度校准的参数。
### Innovation
DACA是一种新的无监督方法，旨在优化后训练置信度校准的参数（例如温度τ）。该方法通过PLM和PoLM在冲突样本上的预测分歧，来降低温度缩放的影响，从而有效克服了因分歧导致的过大的温度值。这种方法能更有效地进行校准，从而提高模型的可靠性，特别是在通用基准上的评测显示，该方法可以提高开源和API基大型语言模型（如GPT-4o）的平均ECE多达15.08%。
### Conclusion
我们的方法不仅避免了由冲突样本导致的过大的温度值，而且通过选择性使用一致样本，有效地降低了解决问题时的分歧影响，从而提高了校准性能。实验表明，我们的方法对常见基准的有效性显著提升。
## 246. `cs.AI` - 利用视觉语言模型进行时序异常检测 [PDF](https://arxiv.org/pdf/2506.06836), [HTML](https://arxiv.org/abs/2506.06836)
### Authors
Zelin He,Sarah Alnegheimish,Matthew Reimherr
### Background
时间序列异常检测（TSAD）在医疗、金融、传感器状态监控等领域发挥着重要作用。现有的方法主要集中在对数值数据训练领域专用模型上，缺乏人类专家所具备的视觉时间理解能力，以便识别上下文中的异常。为了弥补这一不足，本文探索了一种基于视觉语言模型（VLMs）的解决方案。
### Innovation
本文提出了一个两阶段解决方案，包括ViT4TS和VLM4TS两部分。ViT4TS基于轻量级预训练视觉编码器构建，利用2D时间序列表示准确定位候选异常；VLM4TS则利用VLM的全局时间上下文和视觉理解能力对ViT4TS提供的候选异常进行精细化检测。实验结果表明，在无需任何时间序列训练的情况下，VLM4TS在大多数情况下优于时间序列预训练和从零开始的基线方法，F1最大值提高24.6%，并且相较于现有的基于语言模型的TSAD方法，VLM4TS的token使用效率平均提高了36倍。
### Conclusion
本文提出的方法利用视觉语言模型解决了时序异常检测中的视觉时间理解问题，并通过实验证明了其在异常检测上的优势和高效率。
## 247. `cs.AI` - 适应视觉语言模型评估世界模型 [PDF](https://arxiv.org/pdf/2506.17967), [HTML](https://arxiv.org/abs/2506.17967)
### Authors
Mariya Hendriksen,Tabish Rashid,David Bignell,Raluca Georgescu,Abdelhak Lemkhenter,Katja Hofmann,Sam Devlin,Sarah Parisot
### Background
世界模型是指基于过去观察和行动模拟环境动态的生成模型，在规划、仿真和嵌入式AI中逐渐受到重视。然而，评估它们的展开仍然是一个基本挑战，现有评估方法未能捕捉到精细的时间敏感度和语义一致性等能力。视觉语言模型在评估生成内容方面显示出潜力，但由于在细粒度、时序敏感评估任务中的应用有限，需要针对性的调整。
### Innovation
本文引入了一种评估协议，针对两种识别任务——动作识别和角色识别，并使用基于视觉语言模型的UNIVERSE（统一视觉语言评估器）对视频世界模型展开进行适应，并在多种任务格式、上下文长度、采样方法和数据组成的情况下进行了实验探索。结果显示，UNIVERSE能够在各种任务中达到与专用检查点相当的性能，通过人类研究在七个不同的环境下确认了其与人类判断的一致性，从而证明了UNIVERSE是一种轻量级、可适应且语义意识强的视频世界模型评估器。
### Conclusion
综合实验结果和人类研究，UNIVERSE作为一种基于视觉语言模型的评估工具，不仅轻便且可适应于不同环境下视频世界模型的评估，同时具备语义感知的能力，为视觉世界模型的评估提供了一种有效的方法。
## 248. `cs.AI` - STAlloc: 基于时空规划提升大规模模型训练的内存效率 [PDF](https://arxiv.org/pdf/2507.16274), [HTML](https://arxiv.org/abs/2507.16274)
### Authors
Zixiao Huang,Junhao Hu,Hao Lin,Chunyang Zhu,Yueran Tang,Quanlu Zhang,Zhen Guo,Zhenhua Li,Shengen Yan,Zhenhua Zhu,Guohao Dai,Yu Wang
### Background
大规模语言模型（LLMs）的快速发展显著增加了GPU内存压力，通过虚拟流水线和回计算等训练优化技术进一步加剧了问题，这些技术会破坏张量生命周期并引入大量内存碎片。碎片源自于使用在线GPU内存分配器，这些分配器忽视了张量的生命周期。这种低效现象可能导致高达43%的内存浪费，并引发内存溢出错误，从而削弱优化方法的效果。
### Innovation
STAlloc是一个针对深度学习框架的GPU内存分配器，通过利用训练负载中内存分配行为的空间和时间规律来减少碎片。STAlloc引入了一种新的框架，结合了离线规划与在线分配。STAlloc在平均情况下减少了85.1%（最高可达100%）的碎片率，无论是对于密集模型还是Mixture-of-Experts（MoE）模型，同时几乎没有额外开销。这使得更高效的、高通量的训练配置成为可能，并将吞吐量性能提高了32.5%。
### Conclusion
STAlloc能够在空间和时间上高效管理GPU内存分配，不仅解决了大规模模型训练中的内存碎片问题，还显著提高了训练效率和性能。
## 249. `cs.AI` - CodeAssistBench (CAB): Dataset & Benchmarking for Multi-turn Chat-Based Code Assistance [PDF](https://arxiv.org/pdf/2507.10646), [HTML](https://arxiv.org/abs/2507.10646)
### Authors
Myeongsoo Kim,Shweta Garg,Baishakhi Ray,Varun Kumar,Anoop Deoras
### Background
现有的编程助手基于大型语言模型取得了显著进步，但现有基准测试仍局限于狭窄的代码生成场景。现有的基准测试，如InfiBench和StackEval，依赖于Stack Overflow问题，并局限于单轮交互、手工策划的数据和孤立的代码片段，而不是完整的项目环境。因此，研究亟需一个能够评估多轮、项目场景下的编程助手的大规模基准测试。
### Innovation
本文介绍了一个名为CodeAssistBench (CAB)的基准测试，这是第一个用于评估大规模多轮、项目场景下编程辅助的基准测试。CAB使用LLM驱动的管道自动构建数据集，包括过滤噪音、提取可运行上下文、构建可执行容器和验证环境正确性等功能。这种方法使基准测试能够不断、自动地扩展到多种仓库中，无需人工干预。通过CAB，研究创建了一个跨越214个仓库、涵盖7种编程语言的3,286个真实问题的数据集。研究结果表明，尽管最先进的模型在Stack Overflow风格的问题上能达到70-83%的准确性，但在CAB问题上仅有16.49%的解决成功率，手动验证的149个问题中，领先模型的正确率仅为12.08%。
### Conclusion
当前的LLM在提供在具体项目环境中实地帮助时存在挑战，尽管它们在传统的问答基准测试中表现出色。CAB提供了一个可扩展且可复制的框架，用于推进多轮、代码库定位的编程代理研究。CAB的基准测试和流程是完全自动化且开源的，可以在此网站上获取：this https URL.
## 250. `cs.AI` - 基于LoRA的方法在Subarachnoid Hematoma分割中的Unet迁移学习 [PDF](https://arxiv.org/pdf/2508.01772), [HTML](https://arxiv.org/abs/2508.01772)
### Authors
Cristian Minoccheri,Matthew Hodgman,Haoyuan Ma,Rameez Merchant,Emily Wittrup,Craig Williamson,Kayvan Najarian
### Background
动脉瘤性蛛网膜下腔出血（SAH）是一种危及生命的神经系统紧急情况，其死亡率超过30%。虽然传统的U网架构在有限数据集上表现出色，但参数高效的迁移学习方法（如LoRA方法）在医学影像领域的应用仍然很少。通过相关血肿类型的迁移学习是一种潜在有价值但尚未充分探索的方法。
### Innovation
本文提出了一种基于张量CP分解的新LoRA方法CP-LoRA。同时引入了DoRA变体（DoRA-C、convDoRA、CP-DoRA），这些方法将权重矩阵分解为幅度和方向组件，并与现有方法（LoRA-C、convLoRA）和标准微调策略进行了比较，证明了基于LoRA的方法在不同模块上的表现优于传统的Unet微调方法。特别地，对于血肿体积较大的情况，所有方法都提高了准确性，而CP-LoRA在保持与现有方法相似性能的同时使用了显著较少的参数。
### Conclusion
研究表明，不同血肿类型之间的迁移学习是可行的，基于LoRA的方法在动脉瘤性蛛网膜下腔出血分割方面显著优于传统的Unet微调方法。高秩参数化始终优于严格的低秩适应。
## 251. `cs.AI` - 非平衡annealed伴随采样器 [PDF](https://arxiv.org/pdf/2506.18165), [HTML](https://arxiv.org/abs/2506.18165)
### Authors
Jaemoo Choi,Yongxin Chen,Molei Tao,Guan-Horng Liu
### Background
近年来，基于学习的扩散取样器取得了显著进展，这些取样器旨在从给定的未标准化密度中抽取样本。许多这类方法将取样任务表述为随机最优控制问题(SOC)，使用一个典型的无信息参考过程，这限制了它们导引轨迹向目标分布高效转移的能力。
### Innovation
本文提出了一种新颖的基于SOC的扩散框架——非平衡annealed伴随采样器（NAAS），它利用非站稳的基准SDE作为annealed参考动力学。这种annealing结构提供了一种自然的向目标分布过渡方式，并生成了信息性的参考轨迹，从而增强了学习控制的稳定性和效率。由于采用SOC表述，该框架可以纳入各种不同类型的SOC求解器，提供了在算法设计中较高的灵活性。
### Conclusion
作为一种实现方式，我们采用了由伴随匹配启发的简洁伴随系统，实现高效的可扩展训练。我们展示了NAAS在一系列任务中的有效性，包括从经典能量景观和分子玻尔兹曼分布中取样。
## 252. `cs.AI` - BackFed: 一种高效的标准化后门攻击基准套件在联邦学习中的应用 [PDF](https://arxiv.org/pdf/2507.04903), [HTML](https://arxiv.org/abs/2507.04903)
### Authors
Thinh Dao,Dung Thuy Nguyen,Khoa D Doan,Kok-Seng Wong
### Background
联邦学习（FL）中的后门攻击研究近年来取得了显著进展，新的攻击和防御方法不断涌现。然而，这些方法的评价标准不一且缺乏可靠性。当前的研究中存在严重的评价设置不一致问题，许多研究依赖于不现实的威胁模型。此外，对官方代码库的代码审查发现了多个后门攻击的语义错误，人为夸大了它们的性能。这些问题引发了质疑：当前的方法是否真正有效，还是仅仅过度适应了狭窄的实验设置。
### Innovation
我们提出了BackFed，一个旨在标准化并测试FL后门攻击评价的基准。BackFed通过统一攻击和防御，使用模拟现实FL部署的统一评估框架，来解决当前评价标准的问题。在三个代表性的数据集和三种不同的架构上进行的基准测试揭示了现有方法的关键限制：恶意客户端通常需要大量的训练时间和计算资源，从而使它们容易受到服务器实施的时间约束的影响。同时，几种防御措施会导致严重的准确性下降或聚合开销。我们在基准测试中发现，流行的防御和攻击在这方面的表现有限，这挑战了它们之前的有效性主张。
### Conclusion
我们已经建立了BackFed作为严格的公正评价框架，这有助于更可靠地推动FL后门研究的进步。
## 253. `cs.AI` - 阐明式滚动扩散模型在概率天气预报中的应用 [PDF](https://arxiv.org/pdf/2506.20024), [HTML](https://arxiv.org/abs/2506.20024)
### Authors
Salva Rühling Cachay,Miika Aittala,Karsten Kreis,Noah Brenowitz,Arash Vahdat,Morteza Mardani,Rose Yu
### Background
扩散模型是进行概率预测的强大工具，但在高维复杂系统中，大多数应用通常是单独预测未来状态，这种方式难以建模复杂的时序依赖性和无法明确考虑系统中固有的不确定性增长。虽然提出了滚动扩散框架来解决这个问题，但将这种方法与最先进的高保真扩散技术集成仍然存在很大的挑战。
### Innovation
作者通过引入阐明式滚动扩散模型（ERDM）解决了这个问题，ERDM是第一个成功将滚动预测结构与阐明式扩散模型（EDM）的原理性且高性能设计统一起来的框架。关键创新点包括：（i）一种新颖的损失权重方案，重点在确定性和随机性过渡的中期预测区间；（ii）使用预训练的EDM进行初始窗口的高效初始化策略；（iii）一种专为渐进去噪而设计的多重时序架构，以实现稳健的空间时间特征提取。
### Conclusion
ERDM在二维纳维-斯托克斯模拟和ERA5全球天气预报（分辨率1.5度）中表现出色，优于关键性的基于扩散的动力学预测基准，包括条件自回归EDM。ERDM为解决涉及不确定性传播建模的动力学预测问题提供了一个灵活且强大的通用框架。
## 254. `cs.AI` - 改进后的金融文档问答大型语言模型代理 [PDF](https://arxiv.org/pdf/2506.08726), [HTML](https://arxiv.org/abs/2506.08726)
### Authors
Nelvin Tan,Zian Seng,Liang Zhang,Yu-Ching Shih,Dong Yang,Amol Salunkhe
### Background
大型语言模型（LLMs）展示了在各种自然语言处理任务上的出色能力。然而，在处理包含表格和文本数据的财务文件的数值问题回答时，LLMs 仍然存在困难。现有的研究表明，在有Oracle标签的情况下，自我纠正机制（即批判代理）对此任务非常有效。基于此框架，本文探讨了在缺乏Oracle标签的情况下，传统的批判代理的有效性，实验结果表明，它的表现会恶化。因此，本文提出了一种改进的批判代理和计算器代理，这两种代理都优于之前的领先方法（思考程序），并且更安全。此外，研究了这些代理之间的互动，以及这种互动如何影响它们的表现。
### Innovation
本文为了在没有Oracle标签的情况下进行数值问题回答，提出了改进的批判代理和计算器代理。这种改进的代理优于之前的最先进的方法（思考程序），并且更安全。此外，还研究了这些代理之间是如何互动的。
### Conclusion
本文提出的改进代理不仅在数值问题回答任务上表现出色，而且通过其安全机制提高了系统的稳定性。此外，还探讨了代理之间的交互方式及其对性能的影响。
## 255. `cs.AI` - 利用未知来源的未标注数据进行双路径引导的深度假脸检测 [PDF](https://arxiv.org/pdf/2508.09022), [HTML](https://arxiv.org/abs/2508.09022)
### Authors
Zhiqiang Yang,Renshuai Tao,Chunjie Zhang,guodong yang,Xiaolong Zheng,Yao Zhao
### Background
现有的深度假脸检测方法依赖于静态标注的数据集。然而，随着生成模型的发展，大量来自未知来源的真实度极高的未标注假脸数据充斥着现实场景。这使得依赖现有数据的检测器面临泛化失败的问题，手动标注这些新数据又因假脸的高度真实性而不可能。传统无监督学习策略在这类场景下的表现也因真伪人脸共享相同语义而退化。
### Innovation
本文提出了一种双路径引导网络（DPGNet），以解决两个关键挑战：（1）不同生成模型生成的面孔在域差异上的统一；（2）利用未标注的图像样本。该方法包括两个核心模块：文本引导跨域对齐，使用可学习的线索将视觉和文本嵌入统一到域不变特征空间；以及以课程驱动的方式生成伪标签。
### Conclusion
在多个主流数据集上的广泛实验表明，DPGNet 显著优于现有技术，证明了其在利用未标注数据检测深度假脸时的有效性。
## 256. `cs.AI` - LFaB: 低 fidelity 作为偏差的主动学习在化学构型空间 [PDF](https://arxiv.org/pdf/2508.15577), [HTML](https://arxiv.org/abs/2508.15577)
### Authors
Vivin Vinod,Peter Zaspel
### Background
主动学习通过提供一个优化的训练样本人选程序，在构建机器学习模型时显示出潜力。它通常依赖于减少模型的方差，认为这将降低预测误差。然而，它有时甚至不如纯粹的随机抽样效率高。基于偏差-方差分解，本文提出主动学习中应尽量减少模型的偏差而非方差。
### Innovation
提出了一种采用易于计算的低精度数据（来自Δ-ML或多精度机器学习）作为偏差近似的新方法，以便在主动学习中最小化模型的偏差。这种方法能够几乎精确匹配所有贪婪样本选择程序的最优情况误差，尤其适用于量子化学中的应用，如预测激发能量和从头算势能面。
### Conclusion
与标准主动学习方法相比，所提出的LFaB方法在一系列量子化学应用中能够将训练数据需求降低一个数量级。
## 257. `cs.AI` - WeatherDiffusion：内在空间中的可控天气编辑 [PDF](https://arxiv.org/pdf/2508.06982), [HTML](https://arxiv.org/abs/2508.06982)
### Authors
Yixin Zhu,Zuoliang Zhu,Jian Yang,Miloš Hašan,Jin Xie,Beibei Wang
### Background
传统的基于像素的空间编辑方法在控制天气效果时具有局限性，难以保证图像的整体一致性。而WeatherDiffusion提出了一种基于扩散机制的框架，在内在空间中实现了可控的天气编辑，能够更精确地控制和编辑场景中的天气效果。
### Innovation
WeatherDiffusion框架包括两个基于扩散先验的组件：逆渲染器用于从输入图像中估计材质属性、场景几何和光照等内在地图；前渲染器利用这些几何和材质地图以及描述特定天气条件的文本提示生成最终图像。此外，WeatherDiffusion引入了一种内在地图感知的注意力机制，以提高大型户外场景的空间对应性和分解质量，并提出CLIP空间插值方法以实现细粒度的天气控制。
### Conclusion
WeatherDiffusion在可控天气编辑任务中表现出色，与传统的像素空间编辑方法、天气修复方法和基于渲染的方法相比，其性能更优。未来可以在下游应用场景如自动驾驶中进行应用，以提升检测和分割在恶劣天气场景中的鲁棒性。
## 258. `cs.AI` - MeshSplat: Generalizable Sparse-View Surface Reconstruction via Gaussian Splatting [PDF](https://arxiv.org/pdf/2508.17811), [HTML](https://arxiv.org/abs/2508.17811)
### Authors
Hanzhi Chang,Ruijie Zhu,Wenjie Chang,Mulin Yu,Yanzhe Liang,Jiahao Lu,Zhuoyuan Li,Tianzhu Zhang
### Background
在计算机视觉和图形学领域，场景表面重建已经得到广泛研究。然而，现有方法在输入视图极其稀少的情况下难以恢复准确的场景几何结构。
### Innovation
提出了一种名为MeshSplat的通用稀疏视图表面重建框架，通过高斯点选实现。关键思想是利用2DGS作为桥梁，将新颖视角合成与学习到的几何先验连接起来，并将这些先验传递以实现表面重建。此外，还提出了一种加权精馏距离损失来正则化深度图，特别是在输入视图的重叠区域，以及一个法线预测网络来对齐2DGS的方向与单目法线估计器预测的法线矢量方向。
### Conclusion
大量实验验证了我们所提出的改进的有效性，表明我们的方法在通用稀疏视图网格重建任务中达到了最先进的性能。
## 259. `cs.AI` - SafeFix: 基于受控图像生成的目标模型修复 [PDF](https://arxiv.org/pdf/2508.08701), [HTML](https://arxiv.org/abs/2508.08701)
### Authors
Ouyang Xu,Baoming Zhang,Ruiyu Mao,Yunhui Guo
### Background
深度学习模型在视觉识别时常常出现系统性错误，这些错误主要是因为某些语义亚群体在训练集中未被充分表示。尽管现有的调试框架能够通过识别关键失败属性来定位这些失败，但有效修复模型仍然具有挑战性。当前的方法通常依赖于人工设计的提示生成合成训练图像，这种方法容易出现分布偏移和语义错误。
### Innovation
我们提出了一个模型修复模块，该模块基于可解释的失败归因管道。我们的方法使用条件文本到图像模型来生成针对特定失败案例的语义忠实和有针对性的图像。为了保留生成样本的质量和相关性，我们进一步使用大型视觉语言模型（LVLM）来过滤输出，确保输出与原始数据分布的对齐并保持语义一致性。通过使用这个稀有案例增强的合成数据集重新训练视觉模型，可以显著减少与稀有案例相关的错误。实验表明，这种针对性的修复策略可以在不引入新错误的情况下提高模型的鲁棒性。
### Conclusion
我们的方法通过使用稀有案例增强的合成数据集重新训练视觉模型，显著减少了与稀有案例相关的错误。实验表明，这种针对特定失败案例的修复策略在不引入新错误的情况下提高了模型的鲁棒性。代码可在该链接中获取：this https URL
## 260. `cs.AI` - 通过遗忘作为一种消除法：走向一个可证伪的生成性科学发现基准 [PDF](https://arxiv.org/pdf/2508.17681), [HTML](https://arxiv.org/abs/2508.17681)
### Authors
Robert Yang
### Background
该论文探讨了AI在科学中的作用，从AGI能够治愈所有疾病到加速发现的承诺，提出了一个关于大型语言模型（LLMs）是否真正创造新知识的关键问题：LLMs是生成新的知识还是仅仅重新组合已记住的片段。论文提出了“遗忘作为一种消除法”作为一种可证伪的方法，旨在测试模型是否能从基础原理和工具重新推导出结果，从而区别模型是重建知识还是仅仅检索知识。
### Innovation
论文提出了一种新的方法——记忆点消除法（unlearning-as-ablation），通过系统性地删除目标结果及其支持信息（如衍生命题、同义表述和多跳推论），然后观察模型是否能仅依靠允许的公理和工具重新推导出结果，以此来评估模型的生成能力。这种方法不同于之前关于遗忘的主要动机（如隐私、版权或安全），而是将其定位为一种基本的验证标准，以促进AI在科学中的应用。
### Conclusion
这是一个立场文件，贡献在于概念和方法论而非实证结果。作者旨在通过原理驱使的消除测试来激发关于如何区分模型是重建知识还是检索知识的讨论，并探索这种测试如何指导下一代AI科学基准的发展。
## 261. `cs.AI` - CardioComposer: 利用可微几何实现解剖扩散模型的组合控制 [PDF](https://arxiv.org/pdf/2509.08015), [HTML](https://arxiv.org/abs/2509.08015)
### Authors
Karim Kadry,Shoaib Goraya,Ajay Manicka,Abdalla Abdelwahed,Naravich Chutisilp,Farhad Nezami,Elazer Edelman
### Background
生成的3D心血管解剖模型能够为临床研究和医疗设备评估提供有信息价值的结构，但这类模型面临着几何可控性和现实性的权衡。目前的方法在生成多类解剖标签图时，需要在可控性和真实感之间做出取舍。
### Innovation
提出了一种名为CardioComposer的编程框架，在推断时生成基于可解释椭球原始体的多类解剖标签图。通过基于体素的几何矩开发差异性测量函数，实现在采样过程中的损失导向梯度指导。这种方法能够以分离的方式约束各个几何属性，并对多个子结构进行组合控制。此外，该方法适用于包含非凸子结构的各种解剖系统，涵盖了心脏、血管和骨骼器官。
### Conclusion
我们的方法适用于广泛的解剖系统，并能提供对多个子结构的组合控制。通过利用可微几何学，CardioComposer能够以分离的方式控制各个几何属性，在现实性和可控性之间取得平衡。
## 262. `cs.AI` - KEPT：使用视觉语言模型从连续驾驶画面增强预测轨迹 [PDF](https://arxiv.org/pdf/2509.02966), [HTML](https://arxiv.org/abs/2509.02966)
### Authors
Yujin Wang,Tianyi Wang,Quanfeng Liu,Wenxian Fan,Junfeng Jiao,Christian Claudel,Yunbing Yan,Bingzhao Gao,Jianqiang Wang,Hong Chen
### Background
准确的短期轨迹预测对于自动驾驶的安全可靠至关重要。然而，现有的视觉-语言模型（VLMs）往往难以准确理解驾驶场景并生成可信赖的轨迹。
### Innovation
论文提出了KEPT（知识增强的VLM框架），能够直接从连续前视驾驶帧预测自我轨迹。KEPT结合了自监督学习下使用的具有硬负挖掘的时频空间融合（TFSF）视频编码器，以及k-means及HNSW检索增强生成（RAG）流水线。此外，通过三阶段微调范式，KEPT能够更好地对VLM的核心进行调整，增强空间感知和轨迹预测能力。
### Conclusion
KEPT在nuScenes数据集上实现了比基线方法更好的开环性能。通过细化调整流程、RAG的Top-K值、不同的检索策略、视觉编码器和VLM核心的对比实验证明了KEPT的有效性，证明了其在自动驾驶中为可信轨迹预测提供的可能是数据效率的途径。
## 263. `cs.AI` - 象棋玩转神经网络中的迭代推理 [PDF](https://arxiv.org/pdf/2508.21380), [HTML](https://arxiv.org/abs/2508.21380)
### Authors
Elias Sandmann,Sebastian Lapuschkin,Wojciech Samek
### Background
该研究探讨了神经网络在构建其表示时是通过平滑渐进的精细化过程还是通过更复杂的计算过程进行的。研究者通过将‘logit 焦度仪’应用到超人象棋引擎 Leela Chess Zero 的策略网络上来进行分析。
### Innovation
研究者首次将‘logit 焦度仪’应用到策略网络中进行分析，揭示了能力提升发生在不同的计算阶段，移动偏好一直在持续重新评价，直到晚期层次，移动排名与最终输出的相关性较低。早期层次找到的正确解有时会被晚期层次的解所覆盖。最后，实验结果显示，晚期层次更重视安全而非进攻性策略，这提出了一个机制，即启发式优先级可以覆盖战术解决方案。
### Conclusion
研究表明，象棋棋盘上的神经网络在处理过程中经历多个计算阶段，并且在晚期层次，安全性的优先级会超过进攻性策略，这表明启发式知识可能覆盖了实际的战术解决方案。
## 264. `cs.AI` - LaaJMeter: 一种LaaJ评估框架 [PDF](https://arxiv.org/pdf/2508.10161), [HTML](https://arxiv.org/abs/2508.10161)
### Authors
Samuel Ackerman,Gal Amram,Ora Nova Fandina,Eitan Farchi,Shmulik Froimovich,Raviv Gal,Wesam Ibraheem,Avi Ziv
### Background
大型语言模型（LLMs）在自然语言处理任务中作为评估者使用，这种模式被称为LLaJ。在专业领域进行LLaJ软件的元评估（即LLaJ的评估）面临显著挑战。与通用领域相比，专业领域中的标注数据稀缺且专家评估成本高昂。因此，元评估往往使用未经验证适用于特定领域的指标。这使得确定哪些指标有效识别LLaJ质量变得困难，并进一步确定是否达到足够的评估者性能标准难以确定。
### Innovation
提出了一种基于模拟的框架，名为LaaJMeter，用于控制条件下的LLaJ元评估。LaaJMeter允许工程师生成代表虚拟模型和评估者的合成数据，使研究者能够系统地在现实条件下分析评估指标。这有助于从业者验证LLaJs的具体任务的有效性：他们可以测试其指标是否能正确区分高质量和低质量的（虚拟）LLaJs，并估算评价者足够性能的适当阈值。我们通过一项涉及过时编程语言的代码翻译任务展示了LaaJMeter的实用性，表明不同指标在评估者质量敏感性方面的差异。结果突出了常见指标的局限性和精心选择指标的重要性。LaaJMeter提供了一个适用于资源稀缺环境下的可扩展和可扩展解决方案，有助于确保NLP中的可信和可重复评估。
### Conclusion
LaaJMeter为LLaJs在低资源环境中的评估提供了一种可扩展和可扩展的解决方案，促进了更广泛努力确保NLP中的可信和可重复评估。
## 265. `cs.AI` - ConfTuner: 训练大规模语言模型以口头表达其置信度 [PDF](https://arxiv.org/pdf/2508.18847), [HTML](https://arxiv.org/abs/2508.18847)
### Authors
Yibo Li,Miao Xiong,Jiaying Wu,Bryan Hooi
### Background
大规模语言模型（LLMs）越来越多地应用于科学、法律和医疗等高风险领域，准确表达不确定性对于可靠性和信任至关重要。然而，当前的LLMs经常在高置信度下生成错误答案，这种现象被称为“过信心”。最近的研究主要集中在调整LLMs口头表达的置信度，如通过提示工程或基于他觉生成的不确定性估计进行微调。但这些方法的效果有限且不具广泛适用性。本文探讨了如何通过ConfTuner方法改进LLMs的置信度调整，该方法无需真实置信度或代理置信度估计，且引入了最小的额外开销。
### Innovation
提出了一种名为ConfTuner的简单且高效的方法，用于调整LLMs的口头置信度。ConfTuner基于一个新的损失函数‘分词布rier分数’，理论上证明它是一个适当评分法则。这种方法能“正确激励模型报告其正确性的真正概率”。该方法在多种推理任务中提高了模型的校准，同时也能应用于如GPT-4这样的黑盒模型。研究表明，更好的置信度校准有助于下游的自我修正和模型级联，从而推动可信度LLMs系统的发展。
### Conclusion
我们的结果表明，通过ConfTuner方法改善的置信度校准能够带来下游任务的性能提升，包括自我修正和模型级联。该方法为开发可信的大规模语言模型系统提供了新的思路。希望这些发现能够推动LLMs在真实世界中的应用和理解。
## 266. `cs.AI` - 通过渐进探索进行自我模仿的学习历程，然后信任胜利：有生气的强化学习中的自我模仿 [PDF](https://arxiv.org/pdf/2509.22601), [HTML](https://arxiv.org/abs/2509.22601)
### Authors
Yulei Qin,Xiaoyu Tan,Zhengbao He,Gang Li,Haojia Lin,Zongyi Li,Zihan Xu,Yuchen Shi,Siqi Cai,Renting Rui,Shaofei Cai,Yuzheng Cai,Xuan Zhang,Sheng Ye,Ke Li,Xing Sun
### Background
强化学习（RL）被广泛用于提升大型语言模型（LLMs）在长期、稀疏奖励任务中的战略性工具使用能力，但在探索-利用权衡上存在根本挑战。现有研究通过政策熵来刺激探索，但这种方式机械化的熵最大化可能导致RL的不稳定性，因为多轮分布会变动。本文针对在代理自身经验的引导下渐进平衡探索-利用，同时避免熵坍缩或无控制漂移的情况，提出SPEAR方法。
### Innovation
SPEAR是一种基于自我模仿学习（SIL）的训练有生气的代理LLMs的方案。它在标准SIL基础上，通过阶段性的引导策略熵来平衡探索和利用。具体来说，通过课程调度来平衡内在奖励塑造与自我模仿，1) 在初期频繁促进工具互动以加快探索，2) 在向环境熟悉度收敛时强化成功策略的利用。此外，结合工业强化学习优化技巧作为高强度基线，证明SPEAR的有效性。
### Conclusion
在ALFWorld和WebShop中，SPEAR分别将GRPO/GiGPO/Dr.BoT的成功率提高了16.1%/5.1%/8.6%和20.7%/11.8%/13.9%。在AIME24和AIME25中，SPEAR也分别提高了3.8%和6.1%。这些改进仅引入了10%-25%的理论复杂度和可忽略的运行时开销，显示了SPEAR的即插即用可扩展性。
## 267. `cs.AI` - Memory Self-Regeneration: Uncovering Hidden Knowledge in Unlearned Models [PDF](https://arxiv.org/pdf/2510.03263), [HTML](https://arxiv.org/abs/2510.03263)
### Authors
Agnieszka Polowczyk,Alicja Polowczyk,Joanna Waczyńska,Piotr Borycki,Przemysław Spurek
### Background
现代的文本生成图像模型能够生成逼真的视觉，但同时也带来了滥用的风险，可以被用来生成有害、欺骗性的或违法的内容。这加速了机器卸载领域的推进，即在不损害整体性能的前提下，从模型的训练数据中选择性地移除特定的知识。然而，真正忘记某个概念是非常困难的。模型在受到对抗性提示的攻击下，仍能生成所谓的未学会的概念，这些概念可能既有害又违法。
### Innovation
本文提出了关于模型忘记和回忆知识的能力的考虑，引入了Memory Self-Regeneration任务，并提出了MemoRa策略，这是一种支持先前丢失知识有效恢复的再生性方法。此外，作者提出，知识检索的鲁棒性是一个关键但尚未充分探索的评估标准，对于开发更稳健和有效的卸载技术至关重要。最后，研究显示遗忘有两种方式：短期遗忘，概念可以迅速召回，长期遗忘，恢复更为困难。
### Conclusion
在两种不同的遗忘模式中，短期遗忘中概念可以快速召回，但长期遗忘则面临更大的挑战。为了验证其有效性，本研究中的代码已公开。
## 268. `cs.AI` - AI-in-the-Loop: 使用LLMs和联邦学习实现隐私保护的实时诈骗检测和对话式诈骗应对 [PDF](https://arxiv.org/pdf/2509.05362), [HTML](https://arxiv.org/abs/2509.05362)
### Authors
Ismail Hossain,Sai Puppala,Md Jahangir Alam,Sajedul Talukder
### Background
即时通讯平台上的社交工程欺诈手段，如钓鱼、假冒和电话诈骗，仍然是一种持久且不断演变的威胁。现有防御措施大多是被动反应性的，在实时互动中提供的保护有限。
### Innovation
提出了一种隐私保护、具有AI介入循环的框架，该框架能够实时主动检测和中断诈骗对话。该系统结合了指令调整的人工智能和安全意识效用函数，实现了参与度与最小化危害之间的平衡，使用联邦学习技术使模型能够无需原始数据共享即可进行持续更新。实验评估结果显示，该系统生成了平滑且具有吸引性的对话（困惑度低至22.3，参与度约为0.80），而人类研究还证实，该系统在现实主义、安全性以及有效性等方面显著超过了较强的基础模型。在联邦学习环境中，与FedAvg结合训练的模型可持续进行多达30轮更新，在保持高吸引力（约为0.80）、强相关性（约为0.74）以及低隐私信息泄露率（≤0.0085）的情况下，仍然维持了新颖性和安全性。
### Conclusion
这是首个将即时诈骗诱饵、联邦隐私保护和校准过的安全性调节统一进一个主动防御范式的框架。严格的监管设置减少了暴露个人隐私的机会，但也限制了模型参与对话的程度；相比之下，宽松的设置允许更长且丰富的互动，从而提高了诈骗识别率，但也会增加隐私风险。
## 269. `cs.AI` - 跨层视觉平滑：通过持续关注大型视觉语言模型中的关键对象来增强视觉理解 [PDF](https://arxiv.org/pdf/2509.12897), [HTML](https://arxiv.org/abs/2509.12897)
### Authors
Jianfei Zhao,Feng Zhang,Xin Sun,Chong Feng,Zhixing Tan
### Background
大型视觉语言模型（LVLMs）能够准确地定位图片中的关键对象，但它们对这些对象的关注时间通常很短。受持续关注关键对象可以改善LVLMs的视觉能力这一假设的启发，提出了跨层视觉平滑（CLVS）。CLVS的核心思想是在各层之间引入一个视觉记忆，以平滑注意力分布。这种视觉记忆在第一层初始化为无位置偏见的视觉注意力，在后续层中，模型的视觉注意力会考虑来自前一层的记忆，并迭代更新该记忆，从而保持对关键对象的持续关注。
### Innovation
CLVS通过引入视觉记忆并利用跨层迭代更新的方法，使得模型能在处理图像时对关键对象保持更长的注意时间。并且，CLVS使用不确定性作为视觉理解完成的指标，并据此终止平滑过程。这种方法在四种基准测试中的三个大型视觉语言模型上得到了验证，证明了其有效性和泛化能力。
### Conclusion
CLVS在多种视觉理解任务中实现了最先进的总体性能，并且在图像描述基准测试中取得了与领先方法相当的结果。
## 270. `cs.AI` - OceanGym: 一种水下自主代理的基准环境 [PDF](https://arxiv.org/pdf/2509.26536), [HTML](https://arxiv.org/abs/2509.26536)
### Authors
Yida Xue,Mingjun Mao,Xiangyuan Ru,Yuqi Zhu,Baochang Ren,Shuofei Qiao,Mengru Wang,Shumin Deng,Xinyu An,Ningyu Zhang,Ying Chen,Huajun Chen
### Background
水下环境是一种极其苛刻的真实世界应用场景，与陆地或空中领域相比，存在极低的可见度和动态海洋流等问题，使代理的有效部署极为困难。已有基于多模态大语言模型的智能体难以应对这些苛刻环境中的感知、规划和适应性挑战。
### Innovation
引入了OceanGym，这是一个综合基准，旨在推进AI技术在水下环境中发展。它包含了八种现实任务领域和一个由多模态大语言模型驱动的统一代理框架，可以处理感知、记忆和序列决策。OceanGym强调了与人类专家相比，现有的最先进的多模态大语言模型驱动的代理在感知、规划和适应性方面仍然存在巨大差距。
### Conclusion
OceanGym提供了一个高保真、严格设计的平台，可以促进稳健的嵌入式AI的发展，并将这些能力转移到真实世界的自主水下车辆中，标志着向能够操作地球最后未探索边疆之一的智能代理迈出了决定性的一步。相关代码和数据可以访问：this https URL
## 271. `cs.AI` - 探索大型语言模型生成的量化因素和新闻流表示之间的协同作用以进行股票收益预测 [PDF](https://arxiv.org/pdf/2510.15691), [HTML](https://arxiv.org/abs/2510.15691)
### Authors
Tian Guo,Emmanuel Hauptmann
### Background
量化投资中，收益率预测支持股票选择、资产组合优化和风险管理等多种任务。量化因素，如估值、质量和成长性，捕捉股票的各种特征。近年来，新闻和转录等非结构化数据由于大型语言模型（LLMs）的最新进展而受到越来越多的关注。本文探讨了如何有效利用多模态因素和新闻流在收益率预测和股票选择中的作用。
### Innovation
引入了融合学习框架，从LLM生成的因素和新闻流表示中学习统一表示。该框架包括三种不同架构复杂度的方法：表示组合、表示求和和注意表示。在融合学习观察到的局限性基础上，探索了混合模型，该模型能够自适应地结合单模态预测和它们的融合。为减轻混合模型的训练不稳定性，引入了具有理论洞察的分离训练方法。
### Conclusion
实验结果对多模态因素和新闻的有效建模提供了多个有关股票收益预测和选择的见解。
## 272. `cs.AI` - 适配数据集的深度优化网络 - 根据数据集调整网络深度以提高效率 [PDF](https://arxiv.org/pdf/2510.10764), [HTML](https://arxiv.org/abs/2510.10764)
### Authors
Shaharyar Ahmed Khan Tareen,Filza Khan Tareen
### Background
深度神经网络（DNNs）在各种任务中提供了出色的表现，但通常这种成功以不必要大的模型规模、高计算需求和大量内存占用为代价。通常情况下，强大的架构会以全深度进行训练，但对于许多数据集或任务来说，并不需要那么高的模型容量。在资源有限的设备上部署这些复杂度高的大型和深架构时，往往会导致计算资源浪费、不必要的能耗和内存占用过高，使得模型部署变得不切实际。
### Innovation
本文介绍了优化深度网络（ODNs）的概念，以在模型深度和任务复杂度之间提供平衡。本文提出了一种类似NAS的训练策略，称为渐进深度扩张，该策略从较浅的深度开始训练神经网络，并在早期块收敛时逐步增加深度，直到达到目标精度为止。ODNs仅使用针对当前任务所需的最佳深度，去除冗余层，从而降低未来的训练和推理成本，减少模型内存占用，提高计算效率，并方便在边缘设备上部署。
### Conclusion
实验证明，针对MNIST和SVHN的ResNet-18和ResNet-34的最优深度，可将内存占用分别减少98.64%和96.44%，同时保持竞争力的精度（分别为99.31%和96.08%）。
## 273. `cs.AI` - 如何找到优秀的AI论文：自我排名作为超越同行评审的科学影响力预测强效工具 [PDF](https://arxiv.org/pdf/2510.02143), [HTML](https://arxiv.org/abs/2510.02143)
### Authors
Buxin Su,Natalie Collina,Garrett Wen,Didong Li,Kyunghyun Cho,Jianqing Fan,Bingxin Zhao,Weijie Su
### Background
学术研究中的同行评审不仅旨在确保事实上的正确性，还旨在识别具有高科学潜力的工作，这些工作能够塑造未来的研究方向。尤其是在快速发展的领域如人工智能（AI），由于提交数量的快速增长，这一任务变得更加困难。
### Innovation
本文研究了一个未被充分探索的评估指标，即作者对自己的多篇提交到同一AI会议作品的自我排名。基于博弈论的推理，我们假设自我排名是有效的，因为作者对其作品的概念深度及其长期潜力有独特的理解。我们通过在顶级AI会议上进行大规模实验来测试这一假设，该实验包括1342名研究人员对其2592篇提交进行按质量感知的自我排名，结果发现，被作者评为最高的论文的引用次数几乎是最低排名论文的两倍；自我排名在识别高引论文（引用超过150次）方面尤其有效。此外，我们展示了自我排名优于同行评审评分，能够预测未来的引用次数。控制混杂因素（如预印本发表时间和自引用）后，这一结果仍然稳健。
### Conclusion
研究结果表明，作者的自我排名为识别和提升AI领域的高影响力研究提供了一种可靠且有价值的补充工具，它能够与同行评审共同工作，进一步推动科研成果的应用和传播。
## 274. `cs.AI` - 什么是实施科学；以及为什么它对于弥合医学影像领域人工智能创新与应用之间的差距至关重要 [PDF](https://arxiv.org/pdf/2510.13006), [HTML](https://arxiv.org/abs/2510.13006)
### Authors
Ahmad Fayaz-Bakhsh,Janice Tania,Syaheerah Lebai Lutfi,Abhinav K. Jha,Arman Rahmim
### Background
人工智能（AI）在医学成像（MI）中的潜力已被广泛认可。尽管在研究环境中已有令人鼓舞的报告，但在实际临床应用中，许多AI工具仍未能实现广泛应用。研究表明，从技术证据生成到实际应用之间的平均延迟时间为17年。实施科学（IS）可以提供一种实用的、基于证据的框架，用于缩短这一差距，通过系统的方法、策略和混合研究设计来加速技术的实施。
### Innovation
提出实施科学作为弥合AI技术开发与实际临床医学成像应用之间差距的有效方法，强调混合研究设计、知识转移（iKT）、利益相关者参与和面向公平的共同创造的重要性。此外，强调了用户中心的设计方法在使AI易于使用方面的作用。
### Conclusion
采用实施科学不仅是一种方法论的进步，也是一种加速将创新转换为改善患者结果的战略性要求。
## 275. `cs.AI` - Ming-Flash-Omni: 一种统一的稀疏多模态感知和生成架构 [PDF](https://arxiv.org/pdf/2510.24821), [HTML](https://arxiv.org/abs/2510.24821)
### Authors
Inclusion AI:Bowen Ma,Cheng Zou,Canxiang Yan,Chunxiang Jin,Chunjie Shen,Chenyu Lian,Dandan Zheng,Fudong Wang,Furong Xu,GuangMing Yao,Jun Zhou,Jingdong Chen,Jianing Li,Jianxin Sun,Jiajia Liu,Jian Sha,Jianjiang Zhu,Jianping Jiang,Jun Peng,Kaixiang Ji,Kaimeng Ren,Libin Wang,Lixiang Ru,Longhua Tan,Lu Ma,Lan Wang,Mochen Bai,Ning Gao,Qingpei Guo,Qinglong Zhang,Qiang Xu,Rui Liu,Ruijie Xiong,Ruobing Zheng,Sirui Gao,Tao Zhang,Tianqi Li,Tinghao Liu,Weilong Chai,Xinyu Xiao,Xiaomei Wang,Xiaolong Wang,Xiao Lu,Xiaoyu Li,Xingning Dong,Xuzheng Yu,Yi Yuan,Yuting Gao,Yuting Xiao,Yunxiao Sun,Yipeng Chen,Yifan Mao,Yifei Wu,Yongjie Lyu,Ziping Ma,Zhiqiang Fang,Zhihao Qiu,Ziyuan Huang,Zizheng Yang,Zhengyu He
### Background
本文提出了Ming-Flash-Omni，这是在Ling-Flash-2.0的基础上改进的Ming-Omni的升级版。Ming-Flash-Omni基于一种更稀疏的专家混合变体（MoE），总参数量为100亿，其中每个token只有6.1亿个参数是活跃的。该架构在兼顾高效扩展能力的同时，显著提高了模型容量，并且在跨视觉、语音和语言的统一多模态智能方面取得了长足进展。
### Innovation
1. 提出了Ming-Flash-Omni，一种基于更稀疏Mixture-of-Experts（MoE）的架构，总参数量为100亿，每个token只有6.1亿个参数是活跃的。2. 极大提高了计算效率，扩展了模型的容量。3. 显著提升了多模态理解与生成能力，在语音识别和生成、图像生成和编辑等多个方面取得了突破性进展。4. 超越了其前身在多模态理解与生成上的性能，特别是在文本到图像生成和生成分割方面，以及在所有12个上下文ASR基准测试中实现了新的记录。
### Conclusion
Ming-Flash-Omni代表了人工智能通用智能（AGI）的重要一步，其在统一架构中实现了前所未有的多模态感知和生成性能，包括在情感ASR和场景一致性的提高等各个方面均实现了最新的成果。
## 276. `cs.AI` - LikePhys：通过似然偏好评估视频扩散模型中的直觉物理理解 [PDF](https://arxiv.org/pdf/2510.11512), [HTML](https://arxiv.org/abs/2510.11512)
### Authors
Jianhao Yuan,Fabio Pizzati,Francesco Pinto,Lars Kunze,Ivan Laptev,Paul Newman,Philip Torr,Daniele De Martini
### Background
视频扩散模型在构建通用的物理合理的世界模拟器中发挥了重要作用，但准确评估这一能力仍然是一个难题，因为难以区分生成中的物理正确性与视觉外观。为了克服这个挑战，我们引入了LikePhys，这是一种无需训练的方法，通过区分有效的和不可能的视频来评估视频扩散模型中的直觉物理，利用去噪目标作为基于ELBO的似然替代概率模型在精心挑选的有效的和无效的视频配对数据集上工作。
### Innovation
提出了一种无需训练的评估方法LikePhys，利用去噪目标作为基于ELBO的似然替代来区分有效的和无效的视频，从而评估视频扩散模型中的直觉物理理解。该方法通过测试涵盖四个物理领域的十二种场景来系统地评估当前视频扩散模型中的直觉物理理解，并揭示了模型设计和推理设置对直觉物理理解的影响。
### Conclusion
实验结果表明，尽管当前模型在复杂和混沌动力学方面遇到困难，但在物理理解方面仍存在明显的改进趋势。我们的研究表明，在模型设计和推理设置的影响下，不同物理定律具有特定的能力差异。如标题所示，LikePhys通过似然偏好评估视频扩散模型中的直觉物理理解。
## 277. `cs.AI` - 从预测到规划：协作状态-动作预测的策略世界模型 [PDF](https://arxiv.org/pdf/2510.19654), [HTML](https://arxiv.org/abs/2510.19654)
### Authors
Zhida Zhao,Talas Fu,Yifan Wang,Lijun Wang,Huchuan Lu
### Background
尽管在构建世界模型方面取得了显著进展，但这些模型在自治系统中的潜力尚未充分开发：当前的世界模型主要用于世界模拟，与轨迹规划脱钩。近期的研究努力试图在单一框架中统一世界建模和规划，但仍需要进一步探索世界模型如何协同促进规划。
### Innovation
提出了一种新的驾驶范式——策略世界模型（PWM），不仅在统一架构中整合了世界建模和轨迹规划，还通过提出的无动作未来状态预测方案利用所学的世界知识来优化规划。为提高视频预测效率，进一步引入了一种动态增强的并行词生成机制，包括上下文导向的分词器和自适应动态焦点损失。尽管仅使用前方摄像头输入，但该方法在多视图和多模态输入方法中具有竞争力或超越它们。
### Conclusion
通过协作状态-动作预测，PWM 可模拟人类的前瞻性感知，从而产生更可靠规划性能。同时，通过发布源代码和模型权重，以促进该方法的进一步研究和发展。
## 278. `cs.AI` - LightMem：轻量化高效增强记忆生成 [PDF](https://arxiv.org/pdf/2510.18866), [HTML](https://arxiv.org/abs/2510.18866)
### Authors
Jizhan Fang,Xinle Deng,Haoming Xu,Ziyan Jiang,Yuqi Tang,Ziwen Xu,Shumin Deng,Yunzhi Yao,Mengru Wang,Shuofei Qiao,Huajun Chen,Ningyu Zhang
### Background
尽管大型语言模型（LLMs）拥有出色的能力，但它们在动态和复杂环境中难以有效利用历史交互信息。现有记忆系统通过引入持久的信息存储、检索和利用机制，使LLMs能够超越无状态交互，但这些系统通常会带来显著的时间和计算开销。
### Innovation
为解决上述问题，本文提出了一个新的记忆系统——LightMem，该系统在性能和效率之间取得平衡。LightMem借鉴了人类记忆的Atkinson-Shiffrin模型，将记忆划分为三个互补阶段：首先通过轻量级压缩迅速过滤不相关信息，并根据主题对信息进行分组；其次，基于主题的短期记忆将这些主题的分组进行整理和总结，以便更结构化的访问；最后，带有睡眠时段更新的长期记忆采用离线程序，将内容合并与在线推理解耦。
### Conclusion
实验结果表明，LightMem在LongMemEval和LoCoMo上均优于强大的基线，提高了QA准确性最多7.7%/29.3%，减少了最多38x/20.9x的总词令牌使用量和最多30x/55.5x的API调用次数，同时在线测试成本更低，最多减少了106x/117x的词令牌使用量和159x/310x的API调用次数。
## 279. `cs.AI` - 神经网络因果干预中的发散表示的解决方法 [PDF](https://arxiv.org/pdf/2511.04638), [HTML](https://arxiv.org/abs/2511.04638)
### Authors
Satchel Grant,Simon Jerome Han,Alexa R. Tartaglini,Christopher Potts
### Background
对于机制可解释性的一个常见方法是通过目标模型中的针对性干预来因果操控模型表示，以便理解这些表示所编码的内容。然而，这样的干预是否会导致模型表示远离自然分布，以及这种偏离是否会影响解释方法的准确性呢？本文通过理论和实验证明，常见的因果干预技术往往会使得内部表示偏离目标模型的自然分布。文章还分析了两种类型的偏离：一种是无害的偏离，另一种是有害的偏离，前者在权重的零空间内，后者激活隐藏网络路径并导致行为变化。
### Innovation
本文提出并通过修改Grant（2025）的Counterfactual Latent（CL）损失函数，使因果干预产生的表示更接近自然分布，降低了有害偏离的可能性，同时保持干预的解释力。
### Conclusion
本文的结果揭示了一种提高解释方法可靠性的方法路径。
## 280. `cs.AI` - CORE - 细胞级别粗到细图像对齐引擎多染色图像对准 [PDF](https://arxiv.org/pdf/2511.03826), [HTML](https://arxiv.org/abs/2511.03826)
### Authors
Esha Sadia Nasir,Behnaz Elhaminia,Mark Eastwood,Catherine King,Owen Cain,Lorraine Harper,Paul Moss,Dimitrios Chanouzas,David Snead,Nasir Rajpoot,Adam Shephard,Shan E Ahmed Raza
### Background
在高分辨率、细胞核级别的多染色组织切片分析中，整片显微图像（WSI）的准确且高效的注册至关重要。现有的方法往往在多模态WSI数据集间核级别的注册上存在局限性，如难以过滤掉伪影和非组织区域，以及精确对齐。 CORE框架通过粗到细的方法解决这一问题，首先利用基于提示的组织掩模提取来有效滤除伪影和非组织区域，然后使用组织形态和加速密集特征匹配来进行全局对齐，接着进行细粒度刚性对齐，最后通过Coherent Point Drift (CPD) 估计非线性位移场，实现细胞级别的非刚性对齐。
### Innovation
CORE框架提出了一种全新的粗到细注册框架，包括基于提示的粗对齐、加速特征匹配的精细对齐，以及基于CPD的非刚性细粒度对齐。该方法能够自动生成核，并增强可变形对齐的准确性，确保不同模态间核级别的精确对齐。该方法在不同WSI数据集上进行了验证，显示了比当前最先进方法在通用性、精确性和鲁棒性方面的优越性。
### Conclusion
CORE方法在三项公开的WSI注册数据集和两项私有数据集上进行了评估，结果表明该方法在明场显微镜和免疫荧光显微镜WSI注册中表现出更好的通用性、精确性和鲁棒性。
## 281. `cs.AI` - Spatial-SSRL: 通过自我监督强化学习增强空间理解 [PDF](https://arxiv.org/pdf/2510.27606), [HTML](https://arxiv.org/abs/2510.27606)
### Authors
Yuhong Liu,Beichen Zhang,Yuhang Zang,Yuhang Cao,Long Xing,Xiaoyi Dong,Haodong Duan,Dahua Lin,Jiaqi Wang
### Background
大型视觉-语言模型在空间理解方面存在不足。现有的监督微调（SFT）和最近的验证奖励强化学习（RLVR）方法依赖于昂贵的监督、专门的工具或受限的环境，这限制了其扩展规模。
### Innovation
提出了一种自我监督的RL（Spatial-SSRL）范式，直接从普通的RGB或RGB-D图像中提取可验证的信号。Spatial-SSRL自动化地形成了五个先验任务，涵盖了2D和3D空间结构：打乱的块重新排序、翻转的块识别、裁剪的块修补、区域深度排序和相对3D位置预测。这些任务提供了容易验证的正确答案，不需要人类或大模型的标注。通过这些任务的训练，显著提高了空间推理能力，同时保留了泛化的视觉能力。
### Conclusion
在七个空间理解基准测试中，Spatial-SSRL在Qwen2.5-VL基准之上分别平均提升了4.63%（3B）和3.89%（7B）。我们的结果表明，简单的内在监督能够实现大规模的RLVR，并提供了一条增强大模型空间智能的实用途径。
## 282. `cs.AI` - SVBRD-LLM: 自验证行为规则发现方法在自动驾驶车辆识别中的应用 [PDF](https://arxiv.org/pdf/2511.14977), [HTML](https://arxiv.org/abs/2511.14977)
### Authors
Xiangyu Li,Zhaomiao Guo
### Background
随着越来越多的自动驾驶车辆行驶在公共道路上，了解这些车辆的实际行为对于分析交通安全、制定政策以及赢得公众接受度至关重要。
### Innovation
本文提出了一种名为SVBRD-LLM的框架，通过零样本提示工程自动化地发现、验证和应用来自真实交通视频的行为规则。该框架利用YOLOv8和ByteTrack提取车辆轨迹，计算动力学特征，并使用GPT-5零样本提示来比较自动驾驶车辆和手动驾驶车辆，生成35条结构化的行为规则假设。这些规则在验证集上进行测试，基于失败案例迭代优化以筛选出虚假的相关性，并汇编成高置信度的规则库。
### Conclusion
该框架在独立测试集上对速度变化预测、变道预测和自动驾驶车辆识别任务进行了评估。实验结果表明，该框架在自动驾驶车辆识别任务上的准确率为90.0%，F1分数为93.3%。发现的规则显示了自动驾驶车辆在速度控制平滑性、变道保守性和加速稳定性方面的独特特征，每个规则都附带有语义描述、适用上下文和验证置信度。
## 283. `cs.AI` - Metis-HOME: 杂交优化专家混合架构用于多模态推理 [PDF](https://arxiv.org/pdf/2510.20519), [HTML](https://arxiv.org/abs/2510.20519)
### Authors
Xiaohan Lan,Fanfan Liu,Haibo Qiu,Siqi Yang,Delian Ruan,Peng Shi,Lin Ma
### Background
近年来，大规模语言模型（LLM）推理技术取得了显著进展，尤其是在数学问题解决等复杂任务上实现了重要性能提升。尽管如此，当前的多模态大型推理模型仍存在两个关键局限性：一是在处理简单查询时仍依靠昂贵的推理过程，导致效率低下；二是过度专注于专业推理往往会削弱其更广泛的通用理解能力。
### Innovation
本文提出了一种新的混合优化专家混合架构（Metis-HOME），旨在解决上述权衡问题。Metis-HOME通过将原始密集模型划分为两个独立的专业分支来实现一种‘杂交思维’范式：一个专门进行复杂多步推理的思考分支，另一个优化用于快速直接推理任务，如通用VQA和OCR。一种轻量级、可训练的路由器能够动态分配查询给最适合的专家。
### Conclusion
全面的评估表明，该方法在显著增强复杂推理能力的同时，还提高了模型的通用能力，逆转了其他专业推理模型所观察到的退化趋势。我们的工作为构建强大的、多功能的多模态大语言模型设定了新范例，有效解决了推理与泛化的普遍权衡难题。代码和权重可在指定网址获取。
## 284. `cs.AI` - 更少成本实现更多：高效编码代理的轮次控制策略实证研究 [PDF](https://arxiv.org/pdf/2510.16786), [HTML](https://arxiv.org/abs/2510.16786)
### Authors
Pengfei Gao,Chao Peng
### Background
LLM（大型语言模型）驱动的编码代理在迭代循环（轮次）中操作以解决软件工程任务，其功能日益强大，但实际部署受到显著且不可预测的成本的阻碍。这一挑战源于多个因素：每个轮次的令牌计数呈二次增长，模型价格高昂，完成实际任务所需的轮次众多，以及代理倾向于采取不高效或不必要的行动。现有研究主要集中在优化单个轮次，而对整体轮次数量的策略控制这一领域还鲜有探索，特别是在管理代理性能和成本方面。
### Innovation
本研究进行了一项全面的实证研究，使用SWE-bench对三个尖端模型进行了评估，并研究了三种不同的轮次控制策略：无限制基线、固定轮次上限带提醒和一种新颖的需求驱动的动态轮次策略。研究发现，固定轮次限制，尤其在基线的75百分位处，成为成本显著下降（24%-68%）与解决率的微小影响之间的“权衡点”。特别是动态轮次策略始终优于固定限值方法，在仅分配给需要任务的资源下，进一步降低了12%-24%的成本，同时保持或提高了解决率。这项工作提供了第一个关于轮次控制策略的系统分析，为开发者提供了一种简单有效的指南，平衡成本和效率，表明动态资源分配是部署强大且经济实惠的编码代理的优秀方法。
### Conclusion
本研究表明，动态资源分配是一种简单易行且更优的方法，能够有效地利用强大的编码代理以实现更高的经济效益。
## 285. `cs.AI` - FAPE-IR：适用于全方位图像恢复的频率感知规划与执行框架 [PDF](https://arxiv.org/pdf/2511.14099), [HTML](https://arxiv.org/abs/2511.14099)
### Authors
Jingren Liu,Shuning Xu,Qirui Yang,Yun Wang,Xiangyu Chen,Zhong Ji
### Background
现有的图像恢复方法通常依赖于特定任务的设计或潜在路由策略，这意味着它们难以适应具有多种退化条件的现实世界场景。
### Innovation
提出了一种名为FAPE-IR的频率感知规划与执行框架，它利用冻结的多模态大语言模型作为规划者，分析退化图像并生成频率意识的恢复计划。这些计划指导基于LoRA的混合专家模块（LoRA-MoE），该模块在基于扩散的执行器内动态选择高频或低频专家，同时补充输入图像的频率特征。此外，引入了对抗训练和频率正则化损失，以进一步提高恢复质量并减少伪影。
### Conclusion
FAPE-IR 通过结合语义规划与基于频率的恢复，提供了一种统一的、可解释的全方位图像恢复解决方案。广泛实验表明，FAPE-IR 在七项恢复任务中达到最先进的性能，在混合退化情况下的零样本泛化能力强。
## 286. `cs.AI` - CGCE: Classifier-Guided Concept Erasure in Generative Models [PDF](https://arxiv.org/pdf/2511.05865), [HTML](https://arxiv.org/abs/2511.05865)
### Authors
Viet Nguyen,Vishal M. Patel
### Background
近年来，大型生成模型的发展使得高质量的图像和视频生成成为可能，但也引发了关于生成不安全内容的安全隐患。为了缓解这一问题，研究人员开发了概念擦除方法来去除预训练模型中的不良概念。然而，现有的方法仍然容易受到对抗性攻击的干扰，这些攻击可以重新生成被擦除的内容。此外，实现稳健的概念擦除往往降低了模型对安全、无关概念的生成质量，使得安全性和性能之间形成了一种难以调和的权衡。
### Innovation
为了解决这一挑战，我们提出了一种名为Classifier-Guided Concept Erasure (CGCE)的高效插件式框架，它能够在不修改原始权重的情况下为多种生成模型提供稳健的概念擦除。CGCE利用轻量级分类器在文本嵌入上进行操作，首先检测包含不良概念的提示，然后进行细化。通过仅在推理阶段修改不安全的嵌入，该方法防止有害内容的生成，同时保留模型在良性提示上的原始质量。大量实验证明，CGCE在广泛范围内的红队攻击（红队攻击是指攻击者利用各种方法测试系统安全性的一种技术）中表现出业内领先的安全性。我们的方法还保持了高生成可用性，显示了在安全性和性能之间取得更优越的平衡。
### Conclusion
我们通过展示CGCE在各种现代T2I和T2V模型中的成功应用，证明了其作为一种实用有效的安全生成AI解决方案的潜力，为生成AI的安全性提供了可靠的方法。该方法不仅提供了强大的对抗性鲁棒性，还保持了高生成质量，展示了在安全性和性能之间取得的优秀平衡。
## 287. `cs.AI` - 使用序列模型分析心力衰竭患者轨迹 [PDF](https://arxiv.org/pdf/2511.16839), [HTML](https://arxiv.org/abs/2511.16839)
### Authors
Falk Dippel,Yinan Yu,Annika Rosengren,Martin Lindgren,Christina E. Lundberg,Erik Aerts,Martin Adiels,Helen Sjöland
### Background
Transformer架构定义了电子健康记录(EHR)相关临床预测任务的最新水平。尽管Llama和新引入的Mamba架构在处理长上下文时表现更优且参数更少，但在医学领域，系统地分析不同设置下的模型性能和效率仍然缺乏实证方法。本研究调查了六个序列模型在瑞典一个大型心力衰竭(HF)队列(42820例患者)中的表现，为临床相关案例提供了研究。涉及的数据包括住院EHR中提取的诊断、生命体征、实验室测试、药物和程序信息。模型在三个一年的预测任务上进行评估：首次心力衰竭住院后临床不稳定(再入院表型)，首次心力衰竭住院后死亡，以及最近一次住院后的死亡。
### Innovation
本研究首次进行了详细的消融研究，涵盖了输入标记化、模型配置和时间数据预处理的系统设计选择。此外，Llama和Mamba架构在小型配置下表现出更有效地特征表示学习，且在相同模型大小的情况下，使用25%更少的训练数据就能达到优于其他大型Transformer架构的表现。
### Conclusion
此研究提供了分析EHR数据中临床预测任务模型性能和效率的框架。未来在心力衰竭患者的预测任务模型开发中，可以基于此研究的建议作为起点进行进一步构建和发展。
## 288. `cs.AI` - PaSE: Prototype-aligned Calibration and Shapley-based Equilibrium for Multimodal Sentiment Analysis [PDF](https://arxiv.org/pdf/2511.17585), [HTML](https://arxiv.org/abs/2511.17585)
### Authors
Kang He,Boyu Chen,Yuzhe Ding,Fei Li,Chong Teng,Donghong Ji
### Background
多模态情感分析（MSA）旨在通过结合文本、声音和视觉信号来理解人类情感。尽管多模态融合设计用于利用跨模态互补性，但在真实世界场景中，常常出现模态竞争：主导模态往往会压过较弱的模态，导致性能不佳。
### Innovation
本文提出了一种新颖的PaSE框架（Prototype-aligned Calibration and Shapley-optimized Equilibrium），它增强了协作的同时，明确地减少了模态竞争。具体来说，PaSE首先通过原型引导校准学习（PCL）来细化单模态表示并利用熵最优传输机制确保语义一致性。为了进一步稳定优化，引入了一种双阶段优化策略：首先使用原型门融合模块提取共享表示，然后通过基于Shapley的梯度调制（SGM）根据每个模态的贡献动态调整梯度。
### Conclusion
在IEMOCAP、MOSI和MOSEI数据集上的大量实验表明，PaSE在性能上表现出优越性，并且有效地缓解了模态竞争。
## 289. `cs.AI` - 全面探索张量神经网络硬件加速器的设计空间 [PDF](https://arxiv.org/pdf/2511.17971), [HTML](https://arxiv.org/abs/2511.17971)
### Authors
Jinsong Zhang,Minghe Li,Jiayi Tian,Jinming Lu,Zheng Zhang
### Background
高阶张量分解被广泛用于获取适合边缘设备部署的紧凑深度神经网络。现有研究主要关注其算法优势，如准确性和压缩比，但忽视了硬件部署效率。当前的设计方法忽略了硬件特性，未能充分利用张量化模型的潜在延迟和能效优势。
### Innovation
本文提出了一种共探索框架，将张量神经网络在边缘平台上的高效训练和推理中所涉及的收缩路径、硬件架构和数据流映射等维度统一在一个设计空间内进行联合优化，以实现端到端的模型效率最大化。该框架通过全局延迟驱动探索解决了一个面向延迟的目标，最后在可配置的FPGA内核中实现优化配置，与密集基线相比，推理和训练延迟分别降低了4倍和3.85倍。
### Conclusion
本文全面探索了张量神经网络硬件加速器的设计空间，并提出了一种结合设计空间内所有相关维度的框架，以最大化实际设备上的部署效率。
## 290. `cs.AI` - NCCL中GPU启动的网络架构 [PDF](https://arxiv.org/pdf/2511.15076), [HTML](https://arxiv.org/abs/2511.15076)
### Authors
Khaled Hamidouche(1),John Bachan(1),Pak Markthub(1),Peter-Jan Gootzen(1),Elena Agostini(1),Sylvain Jeaugey(1),Aamir Shafi(1),Georgios Theodorakis(1),Manjunath Gorentla Venkata(1) ((1) NVIDIA Corporation)
### Background
现代AI工作负载，特别是Mixture-of-Experts (MoE) 架构，越来越需要低延迟和细粒度的GPU-GPU通信，并且需要设备端控制。传统的GPU通信遵循由CPU调度的主托管发模型，适用于集体操作。但在需要紧密集成计算和通信的应用中，设备端发起的通信可以消除CPU调度开销。
### Innovation
NCCL 2.28引入了设备API，包括三种操作模式：对于NVLink/PCIe的加载/存储可访问（LSA），对于NVLink SHARP的Multimem，以及用于网络远程直接内存访问（RDMA）的GPU启动网络（GIN）。这篇论文主要介绍了GIN架构，包括其设计、语义，并强调它对MoE通信的影响。GIN基于三层架构：i) NCCL核心的主机端API，用于设备通信器设置和集体内存窗口注册；ii) 设备端API，可以从CUDA内核调用远程内存操作；iii) 网络插件架构，具有双重语义（GPUDirect异步内核启动和代理），支持广泛的硬件。
### Conclusion
通过与DeepEP（一个MoE通信库）集成来演示GIN的实用性。全面的基准测试表明，GIN可以在NCCL统一运行时提供设备启动的通信，结合了低延迟操作和NCCL的集体算法及生产基础设施。
## 291. `cs.AI` - MindEval：在多轮心理健康支持领域的语言模型基准测试 [PDF](https://arxiv.org/pdf/2511.18491), [HTML](https://arxiv.org/abs/2511.18491)
### Authors
José Pombal,Maya D'Eon,Nuno M. Guerreiro,Pedro Henrique Martins,António Farinhas,Ricardo Rei
### Background
随着对通过AI聊天机器人寻求心理健康支持的需求增加，当前系统存在诸如奉承、过度验证或强化不良信念等缺陷。创建更优系统的核心障碍是缺乏能够捕捉现实生活中的治疗互动复杂性的基准。现有的大多数基准要么仅通过多项选择题测试临床知识，要么仅评估单个响应。为了填补这一空白，作者提出了一种名为MindEval的框架，该框架与具有Ph.D.资格的心理学专家合作，旨在自动评估语言模型在实际、多轮心理治疗对话中的表现。通过患者模拟和与大型语言模型（LLM）的自动评估，该框架兼顾了防止游戏化和通过其完全自动化且模型无关的设计保证可重复性。
### Innovation
MindEval框架旨在平衡现实多轮心理治疗对话的评估，并通过自动化设计防止模型被“游戏化”，同时确保评估结果的可重复性。该框架通过与具有Ph.D.资格的心理学专家合作开发，确保了评估的真实性和准确性。通过与大型语言模型的自动评估，该框架验证了模拟患者的真实性，并展示了自动评估和专家评估之间的强相关性。
### Conclusion
作者通过模拟患者和与大型语言模型的自动评估，验证了MindEval的真实性和有效性，并评估了12个最新的大型语言模型，结果显示所有模型的平均得分均低于6分中的4分，特别是在与AI特定沟通问题相关的部分显得尤为薄弱。此外，推理能力和模型规模并不能保证更高的性能，系统在长期交互或支持严重症状患者时会表现更差。作者公开了所有代码、提示和人工评估数据。
## 292. `cs.AI` - Omnidirectional视频中区域兴趣检测的深度混合模型 [PDF](https://arxiv.org/pdf/2511.18856), [HTML](https://arxiv.org/abs/2511.18856)
### Authors
Sana Alamgeer,Mylene Farias,Marcelo Carvalho
### Background
360度视频中的区域兴趣（ROI）对于视频流传输至关重要。ROI用于预测观看窗口，智能切割视频以进行直播，从而减少带宽使用。通过头戴设备流式传输视频时，提前检测观看窗口有助于减少头部移动。智能视频剪辑有助于提高视频流传输效率和用户体验质量。
### Innovation
开发了一种结合了视觉显著性模型的混合方法来预测360度视频的ROI。该方法包括预处理视频以获取帧，开发混合显著性模型以预测ROI，然后对混合显著性模型的输出进行后处理以获取每个帧的ROI。
### Conclusion
与360RAT数据集的主观注释相比，所提出的方法进行了性能比较。
## 293. `cs.AI` - ConceptGuard：通过多模态风险检测在文本和图像到视频生成中的前瞻性安全性 [PDF](https://arxiv.org/pdf/2511.18780), [HTML](https://arxiv.org/abs/2511.18780)
### Authors
Ruize Ma,Minghong Cai,Yilei Jiang,Jiaming Han,Yi Feng,Yingshui Tan,Xiaoyong Zhu,Bo Zhang,Bo Zheng,Xiangyu Yue
### Background
近年来，视频生成模型的发展使得能够从结合文本和图像的多模态提示中生成高质量的视频。这些系统提供了增强的可控性，但也引入了新的安全风险，因为有害内容可能来自单一模态或它们的交互。现有的安全方法往往是文本相关的，需要事先了解风险类别，或作为生成后的审核器，难以积极地应对组合性和多模态风险。
### Innovation
本文提出了ConceptGuard，一种统一的安全防护框架，用于前瞻性地检测和防止多模态视频生成中的不安全语义。ConceptGuard分为两个阶段：首先，对比检测模块通过将融合图像-文本输入投影到一个结构化的概念空间中来识别潜在的安全风险；其次，语义抑制机制通过干预多模态条件下的提示，引导生成过程远离不安全的概念。此外，还引入了两个新的基准测试：ConceptRisk，用于训练多模态风险的大规模数据集，以及T2VSafetyBench-TI2V，第一个适应文本和图像到视频（TI2V）安全设置的基准测试。
### Conclusion
在两个基准测试上的全面实验表明，ConceptGuard在风险检测和生成安全视频方面都始终优于现有基线，达到了最先进的技术水平。相关代码可在给定的链接中获得。
## 294. `cs.AI` - DecNefLab: 解码神经反馈的一种模块化和可解释性强化模拟框架 [PDF](https://arxiv.org/pdf/2511.14555), [HTML](https://arxiv.org/abs/2511.14555)
### Authors
Alexander Olza,Roberto Santana,David Soto
### Background
解码神经反馈（DecNef）是一种广泛应用在神经医学和认知神经科学领域的非侵入性脑调节方法。然而，DecNef研究的进步受到了个体学习差异的影响，高度依赖于间接指标来衡量进步，并且由于实验的成本和时间需求很高而受到限制。
### Innovation
作者提出了DecNefLab，这是一种模块化和可解释性强化模拟框架，将DecNef作为机器学习问题进行形式化。通过使用潜在变量生成模型作为模拟参与者，DecNefLab使研究者能够直接观察内部认知状态，系统性地评估不同的协议设计和受试者特性对学习的影响，并能够在实施人工试验之前通过虚拟实验室来进行这些研究。
### Conclusion
总结而言，DecNefLab将计算建模和认知神经科学联系起来，提供了一种有原则的方法论基础，促进了方法创新、稳健协议设计，并最终深化了对基于DecNef的脑调节的理解。
## 295. `cs.AI` - HyperbolicRAG：通过双曲表示增强检索增强生成 [PDF](https://arxiv.org/pdf/2511.18808), [HTML](https://arxiv.org/abs/2511.18808)
### Authors
Linxiao Cao,Ruitao Wang,Jindong Li,Zhipeng Zhou,Menglin Yang
### Background
检索增强生成（RAG）使大模型能够访问外部知识，从而减少幻觉并增强领域特定的专业知识。基于图的RAG通过引入显式的关系组织提高了结构推理能力，但通常依赖于欧几里得嵌入来捕捉语义相似性，缺乏关于层次深度的几何概念，限制了它们对复杂知识图中固有的抽象关系的表示能力。为了捕获细粒度语义和全局层次结构，本文提出了一种将双曲几何融入图基RAG的检索框架——HyperbolicRAG。
### Innovation
HyperbolicRAG通过引入三个关键设计实现创新：（1）一种层次感知的表示学习器，通过嵌入节点到共享的庞加莱流形中，使语义相似性与层次包含对齐；（2）一种无监督对比正则化，以确保不同抽象级别的几何一致性；（3）一种互-ranking融合机制，联合利用欧几里得空间和双曲空间的检索信号，在推理中强调跨空间的一致性。
### Conclusion
在多个QA基准测试中的广泛实验表明，HyperbolicRAG在与标准RAG和图增强基线的竞争中表现出色。
## 296. `cs.AI` - MAIF: 使用基于实体的代理范式确保人工智能的可靠性和来源 [PDF](https://arxiv.org/pdf/2511.15097), [HTML](https://arxiv.org/abs/2511.15097)
### Authors
Vineeth Sai Narajala,Manish Bhatt,Idan Habler,Ronald F. Del Rosario,Ads Dawson
### Background
人工智能革命面临着信任危机，监管障碍、安全漏洞和问责差距阻碍了关键领域的部署。当前的人工智能系统依赖于不透明的数据结构，缺乏新兴法规（如欧盟AI法案）所需的可审计记录、来源追踪或解释性。这种缺乏透明度和可追溯性的问题阻碍了人工智能的信任度。
### Innovation
本文提出了一种基于实体的AI代理范式，通过持续、可验证的数据实体驱动行为，而不仅仅是短暂的任务，解决了数据架构层面的信任问题。核心在于多模态数据文件格式（MAIF），这是一种嵌入语义表示、加密原产地和细粒度访问控制的人工智能原生容器。MAIF将数据从被动存储转变为积极发挥的信任强制机制，使每项AI操作都变得可审计。生产级实现演示了超高速流传输（2,720.7 MB/s）、优化的视频处理（1,342 MB/s）和企业级安全性能。创新算法包括跨模态注意力、语义压缩和加密绑定，实现至多225倍压缩的同时保持语义保真度。先进的安全功能包括流级访问控制、实时篡改检测和行为异常分析，具有最小开销。
### Conclusion
这种方法直接解决了监管、安全和问责方面阻碍人工智能部署在敏感领域的挑战，提供了规模化实现可信的人工智能系统的一条可行路径。
## 297. `cs.AI` - 在视觉语言行动模型中持续进化技能知识 [PDF](https://arxiv.org/pdf/2511.18085), [HTML](https://arxiv.org/abs/2511.18085)
### Authors
Yuxuan Wu,Guangming Wang,Zhiheng Yang,Maoqing Yao,Brian Sheil,Hesheng Wang
### Background
开放环境中通用机器人的智能发展需要持续的学习技能。最近的视觉-语言-行动（VLA）模型通过大规模的预训练数据支持多样化的操作任务，但它们仍然依赖于特定任务的微调，显示出了持续学习能力的欠缺。现有的持续学习方法在扩展到VLA模型时也消耗大量资源。
### Innovation
提出了Stellar VLA，这是一种知识驱动的持续学习框架，包括两种变体：T-Stellar，建模任务中心的知识空间，以及TS-Stellar，捕捉任务技能层次结构。Stellar VLA 通过联合学习任务隐含表示和知识空间实现自我监督的知识进化，减少了标注需求。知识指导专家路由提供任务专业化，减少了额外的网络参数，降低了训练开销。
### Conclusion
在LIBERO基准和真实任务上的实验表明，与基线相比，平均成功率为50％以上。TS-Stellar 在复杂动作推理方面表现出色，深入分析验证了有效知识的保留和发现。我们的代码即将发布。
## 298. `cs.AI` - 用于同时生成多尺度移动网络流量的去噪精炼扩散模型 [PDF](https://arxiv.org/pdf/2511.17532), [HTML](https://arxiv.org/abs/2511.17532)
### Authors
Xiaoqian Qi,Haoye Chai,Sichang Liu,Lei Yue,Raoyuan Pan,Yue Wang,Yong Li
### Background
蜂窝移动网络的规划、管理和资源调度需要跨不同层级和节点联合估计移动流量。移动流量生成可以主动预测用户需求并捕捉网络负载的动态变化。然而，现有的方法主要专注在一个时空分辨率上的流量生成，这使得难以建模多尺度的流量模式。
### Innovation
本文提出了一种基于扩散模型的多尺度移动流量生成方法，名为ZoomDiff。ZoomDiff通过一组定制化的去噪精炼扩散模型（DRDM）将城市环境上下文映射为具有多种空间和时间分辨率的移动流量。DRDM采用多阶段的去噪机制，使不同的阶段能够在不同的时空分辨率上生成流量，这种设计使去噪过程与层次化的网络层相契合，包括不同层级的基站、小区和网格。
### Conclusion
实验结果表明，ZoomDiff在多尺度的流量生成任务上比最先进的基线方法至少提升了18.4%。此外，ZoomDiff展示了强大的效率和跨城市的泛化能力，这表明其作为建模多尺度移动网络动态的强大生成框架的潜力。
## 299. `cs.AI` - 通过双智能体学习压缩图以实现一致的拓扑鲁棒性评估 [PDF](https://arxiv.org/pdf/2511.18958), [HTML](https://arxiv.org/abs/2511.18958)
### Authors
Qisen Chai,Yansong Wang,Junjie Huang,Tao Jia
### Background
随着图形结构数据的增长，评估其在对手攻击下的鲁棒性变得计算成本高昂且难以扩展。
### Innovation
提出了一种名为Cutter的双智能体强化学习框架，由结构至关节点检测智能体(VDA)和冗余节点检测智能体(RDA)组成，协作识别结构中的关键节点和冗余节点，以引导压缩。Cutter采用了三种关键策略来提高学习效率和压缩质量：轨迹级别的奖励塑形、原型塑形以及交叉智能体模仿。
### Conclusion
实验结果表明，Cutter生成的压缩图保留了关键的静态拓扑特性，且在各种攻击场景下的鲁棒性退化趋势与原始图形高度一致，从而在不牺牲评估准确性的情况下显著提高了评估效率。
## 300. `cs.CL` - LLMs在低资源语言中能忠实解释自己吗？一项关于波斯情感检测的研究 [PDF](https://arxiv.org/pdf/2511.19719), [HTML](https://arxiv.org/abs/2511.19719)
### Authors
Mobina Mehrazar,Mohammad Amin Yousefi,Parisa Abolfath Beygi,Behnam Bahrak
### Background
大规模语言模型（LLMs）开始被用来生成伴随其预测的自我解释，这一做法引发了对这些解释准确性的担忧，特别是在资源稀缺的语言中。这项研究通过将模型识别的关键词语与其人类注释者的识别结果进行比较，评估了LLM生成的解释在波斯语情感分类中的忠实性。
### Innovation
该研究创新地使用了基于令牌级对数概率得出的信心分数来评估生成解释的忠实性，并通过使用不同的提示策略（解释-然后预测和预测-然后解释）来测试对解释忠实性的影响。
### Conclusion
尽管LLMs在分类性能上表现出色，但生成的解释往往偏离了准确的推理，与其他LLM解释的匹配度高于与人类判断的匹配度。这些结果揭示了当前解释方法和评估指标的局限性，强调了在多语言和低资源环境中确保LLM可靠性的方法的必要性。
## 301. `cs.CL` - 理解语言意味着什么？ [PDF](https://arxiv.org/pdf/2511.19757), [HTML](https://arxiv.org/abs/2511.19757)
### Authors
Colton Casto,Anna Ivanova,Evelina Fedorenko,Nancy Kanwisher
### Background
理解语言不仅仅是提取语言输入的表面意义，还需要在大脑的核心语言系统中构建描述该情境的丰富心理模型。由于大脑核心语言系统的处理能力有限，因此深入理解语言需要将信息导出到其他处理感知和运动表示、构建心理模型并存储世界知识和自传性记忆的大脑区域。
### Innovation
本文提出，深入理解语言需要将信息从大脑的核心语言系统导出到其他大脑区域，这些区域负责计算感知和运动表示、构建心理模型和存储世界知识和自传性记忆。此外，近期的认知神经科学研究为测试这一假设提供了概念基础和方法。
### Conclusion
近期的认知神经科学研究为直接检验这一假设提供了概念基础和方法，从而开辟了一条新的策略，可以揭示从认知和神经角度来看，理解语言的含义。
## 302. `cs.CL` - 通过LLM规划和嵌入引导搜索高效的知识图谱多跳问答 [PDF](https://arxiv.org/pdf/2511.19648), [HTML](https://arxiv.org/abs/2511.19648)
### Authors
Manil Shrestha,Edward Kim
### Background
知识图谱上的多跳问答由于潜在推理路径的组合爆炸而具有计算上的挑战。现有方法依赖于昂贵的大型语言模型（LLM）推理，这限制了它们的实际部署。此外，LLM生成的答案通常缺乏可验证的知识结构基础。
### Innovation
该论文提出两个互补的混合算法，解决效率和可验证性问题：(1) LLM引导规划使用单次LLM调用来预测执行的关联序列，通过广度优先搜索完成，近似完美准确度（微调F1得分>0.90），并确保所有答案都基于知识图谱；(2)嵌入引导神经搜索通过融合文本和图形嵌入，完全消除LLM调用，采用轻量级（6.7M参数）边得分器，实现超过100倍的速度提升，同时保持竞争性准确度。通过知识蒸馏，将规划能力压缩到4B参数模型，匹配大型模型性能，且无API成本。
### Conclusion
MetaQA上的评估表明，基于知识的推理持续优于非结构化生成，结构化规划比直接答案生成更具可转移性。我们的结果表明，在推理阶段可验证的多跳推理不需要大规模模型，而是恰当的架构归纳偏差结合了符号结构与学习表示。
## 303. `cs.CL` - 语言独立的语义标记与远监督：英语、塞佩迪语和塞茨瓦纳语的案例研究 [PDF](https://arxiv.org/pdf/2511.19818), [HTML](https://arxiv.org/abs/2511.19818)
### Authors
Koena Ronny Mabokela,Tim Schlippe,Mpho Raborife,Turgay Celik
### Background
情感分析在人工智能用于社会责任、教育技术或商业营销等领域中具有帮助性。虽然许多情感分析系统是为英语开发的，但许多非洲语言因其缺乏数字语言资源（如带相应情感类别的文本）而被归类为资源稀缺的语言。手动标记文本数据耗时且成本高昂，因此需要自动且快速的过程来最大限度地减少人工努力，使标记过程尽可能高效。
### Innovation
该论文提出了并分析了一种利用带有情感信息的表情符号和词汇的自动、语言独立的情感标记方法。实验在南非语言多语言情感语料库SAfriSenti中的英语、塞佩迪语和塞茨瓦纳语的推特上进行。
### Conclusion
研究结果表明，该情感标记方法能以66%的准确率标记英语推特、69%的准确率标记塞佩迪语推特以及63%的准确率标记塞茨瓦纳语推特。平均而言，只有34%的自动生成的标签需要进一步修正。
## 304. `cs.CL` - 大型语言模型中的性别偏差在情绪识别中的研究 [PDF](https://arxiv.org/pdf/2511.19785), [HTML](https://arxiv.org/abs/2511.19785)
### Authors
Maureen Herbert,Katie Sun,Angelica Lim,Yasaman Etesam
### Background
近年来，大型语言模型（LLMs）的迅猛发展及其在日常生活中的广泛应用凸显了评估和确保其公平性的必要性。本研究聚焦于情绪认知理论中的性别偏差问题，探讨了在给定人物及其环境描述并提问‘这个人感觉如何？’的情况下，LLMs 是否表现出性别偏见。
### Innovation
研究提出并评估了多种去偏策略，发现要实现显著的偏见减少，需要基于训练的干预措施，而非依赖于基于推理时提示的策略，如提示工程。
### Conclusion
研究结果表明，单纯依靠提示工程等推理时的干预措施无法有效减轻LLMs中的性别偏见，有效的去偏需要在模型训练阶段进行有针对性的干预。
## 305. `cs.AI` - Shape-Adapting Gated Experts: 动态专家路由在结肠息肉分割中的应用 [PDF](https://arxiv.org/pdf/2511.18493), [HTML](https://arxiv.org/abs/2511.18493)
### Authors
Gia Huy Thai,Hoang-Nguyen Vu,Anh-Minh Phan,Quang-Thinh Ly,Tram Dinh,Thi-Ngoc-Truc Nguyen,Nhat Ho
### Background
在计算机辅助癌症检测中，全视野显微镜图像（WSIs）中的细胞多样性仍然是主要挑战之一，这归因于细胞异质性。现有的基于卷积神经网络（CNN）和变换器（Transformer）的混合体依赖于静态计算图，具有固定路由，导致了冗余计算，限制了输入变量适应性。
### Innovation
我们提出了形变适应门控专家(SAGE)，这是一种输入自适应框架，能够在异构视觉网络中实现动态专家路由。SAGE通过可重构的静态主体骨架为动态路由的专家架构，同时设计了双路径，包括一个保持表示并选择性激活专家路径的主体流，以及一个基于层次门控机制进行两级选择，调节模型logits以实现Top-K激活。
### Conclusion
我们的形变适应枢纽（SA-Hub）在CNN和Transformer模块之间统一结构和语义表示，有效连接了不同的模块。以SAGE-UNet的形式，该模型在EBHI、DigestPath和GlaS三个医学基准上实现了卓越的分割结果，分别达到了95.57%、95.16%和94.17%的Dice Score，并且能够跨领域稳健扩展，通过局部精修和全局上下文的灵活平衡来实现。
## 306. `cs.CL` - RAG启用动态提示的大语言模型系统分析在医疗错误检测和纠正中的应用 [PDF](https://arxiv.org/pdf/2511.19858), [HTML](https://arxiv.org/abs/2511.19858)
### Authors
Farzad Ahmed,Joniel Augustine Jerome,Meliha Yetisgen,Özlem Uzuner
### Background
临床文档中包含事实性、诊断性和管理性错误，这些错误可能损害患者安全。大型语言模型（LLMs）可以用于检测和修正这些错误，但它们在不同提示策略下的行为尚不清楚。本研究通过评估三种不同提示策略（零样本提示、带有随机示例的静态提示（SPR）和检索增强动态提示（RDP））在医疗错误处理中的应用，探讨了这些策略在错误发现、错误句子检测和错误修正三个子任务中的表现。
### Innovation
该研究创新性地评估了三种不同的提示策略在医疗错误处理中的应用，包括零样本提示、带有随机示例的静态提示（SPR）和检索增强动态提示（RDP）。实验结果显示，检索增强动态提示（RDP）在所有九种LLM中均表现出色，改进了检测准确性，减少了假阳性，并增强了医疗错误纠正的可靠性。
### Conclusion
无论是在哪种不同的LLM中，检索增强动态提示（RDP）都优于零样本和SPR提示。通过检索示例可以提升检测准确性，减少假阳性，并增强医疗错误纠正的可靠性。
## 307. `cs.CL` - Breaking Bad: Norms for Valence, Arousal, and Dominance for over 10k English Multiword Expressions [PDF](https://arxiv.org/pdf/2511.19816), [HTML](https://arxiv.org/abs/2511.19816)
### Authors
Saif M. Mohammad
### Background
词义分析研究已表明，单词含义的主要维度是正向性（Valence, V）、唤醒性（Arousal, A）和支配性（Dominance, D）。现有词汇库如2018年发布的NRC VAD词汇库包含单词的VAD关联评分。作者在此基础上，为10K个英语多词表达（MWEs）及其构成单词提供Human评分的VAD，同时增加了2018年后变得更加普遍的单词覆盖率。
### Innovation
本文的创新之处在于创建了一个更新版的NRC VAD词汇库（v2），其中包含10K个MWE及其25K构成单词的VAD评分；这不仅扩展了词汇库的覆盖范围，还显示出这些关联的可靠性。此外，使用该词汇库对MWE的情感特征进行了研究，包括MWEs的情感强度和情感组合性。
### Conclusion
新的NRC VAD词汇库v2可用于多个领域的研究，如自然语言处理、心理学、公共健康、数字人文和社会科学。该词汇库现已免费通过项目网页提供：此链接http://www.example.com
## 308. `cs.CL` - LoRA- adapated嵌入模型在临床心脏病学文本表示中的比较分析 [PDF](https://arxiv.org/pdf/2511.19739), [HTML](https://arxiv.org/abs/2511.19739)
### Authors
Richard J. Young,Alice M. Matthews
### Background
特定领域的文本嵌入对于临床自然语言处理至关重要，然而，不同模型架构之间的系统性比较仍然有限。这项研究通过LoRA微调十种基于变压器的嵌入模型提出了心脏病学领域的文本表示，这些模型来源于106,535对权威医学教科书中的心脏科文本对。
### Innovation
研究采用了通过LoRA微调的心脏病学专用的十种基于变压器的嵌入模型，特别关注了仅包含编码器的架构，特别是BioLinkBERT，显示出其在特定领域性能方面优于基于解码器的更大模型，同时所需计算资源显著减少。研究结论挑战了大语言模型必然产生更好的专业领域嵌入模型的假设，并为此类研究提供了实用指导。
### Conclusion
所有模型、训练代码和评估数据集都已公开，供医学信息学领域的复制研究使用。研究结果表明，仅编码器架构、特别是BioLinkBERT，在心脏病学领域表现出更优的特定领域性能，并且需要更少的计算资源。这一发现打破了大模型更胜一筹的假设，并提供了临床NLP系统的开发指南。
## 309. `cs.CL` - Profile-LLM: 动态简历优化以在大语言模型中实现真实的人格表达 [PDF](https://arxiv.org/pdf/2511.19852), [HTML](https://arxiv.org/abs/2511.19852)
### Authors
Shi-Wei Dai,Yan-Wei Shie,Tsung-Huan Yang,Lun-Wei Ku,Yung-Hui Li
### Background
个性化的大语言模型（LLMs）已经被证明是一种有效的用户-AI互动方式，能够创造更加引人入胜和愉快的交互体验。尽管以前的研究已经探索了使用提示来激发LLMs的具体人格特征，但尚未优化这些提示以最大限度地表达人格特质。
### Innovation
提出PersonaPulse：一种利用LLMs固有的个性特质知识的框架，通过迭代增强角色扮演提示，并结合情境反应基准作为评分工具，确保更真实和情境相关的评价，以指导优化过程。定量评估表明，PersonaPulse生成的提示优于以前基于心理研究人格描述设计的提示。此外，通过广泛的实验探索了模型大小与人格建模的关系。最后，发现对于某些人格特质，个性激发的程度可以通过暂停优化过程部分控制。
### Conclusion
这些发现强调了提示优化对于塑造LLMs中的人格表达的重要性，为未来关于自适应AI互动的研究提供了宝贵的见解。
## 310. `cs.CL` - R²R: 多域解码器仅重新排序后处理框架 [PDF](https://arxiv.org/pdf/2511.19987), [HTML](https://arxiv.org/abs/2511.19987)
### Authors
Xinyu Wang,Hanwei Wu,Qingchen Hu,Zhenghan Tai,Jingrui Tian,Lei Ding,Jijun Chi,Hailin He,Tung Sum Thomas Kwok,Yufei Cui,Sicheng Lyu,Muzhi Li,Mingze Li,Xinyue Yu,Ling Zhou,Peng Lu
### Background
解码器仅重新排序系统是检索增强生成（RAG）的核心。然而，通用模型在金融、法律等高风险领域未能捕捉到特定领域的细微差别，并且粗暴的微调会导致表面形式的过拟合和灾难性遗忘。
### Innovation
本文引入了R2R，这是一种领域感知框架，结合了动态专家路径选择和两阶段训练策略——实体抽象以实现泛化（EAG）。EAG通过屏蔽最具有预测性的表面线索，迫使重新排序系统学习领域不变的相关模式而不是记忆特定数据集的实体。R2R采用轻量级的潜在语义路由器，通过冻结的骨干解码器内部表示来选择每个查询的最佳LoRA专家，以高效激活领域专家。
### Conclusion
跨不同重新排序器骨干和不同领域（法律、医学和金融）的广泛实验表明，R2R在各方面的表现均超过了通用模型和单一领域微调的基线。结果证实，R2R是一种适用于领域自化的模型通用且模块化的方法，具有强大的跨域鲁棒性。
## 311. `cs.CL` - AppSelectBench: 应用级别工具选择基准 [PDF](https://arxiv.org/pdf/2511.19957), [HTML](https://arxiv.org/abs/2511.19957)
### Authors
Tianyi Chen,Michael Solodko,Sen Wang,Jongwoo Ko,Junheng Hao,Colby Banbury,Sara Abdali,Saeed Amizadeh,Qing Xiao,Yinheng Li,Tianyu Ding,Kamran Ghasedi Dizaji,Suzhen Zheng,Hao Fan,Justin Wagle,Pashmina Cameron,Kazuhito Koishida
### Background
计算机使用代理（CUAs）现在配备了外部工具，能够执行复杂的和现实的任务。为了使CUAs有效运行，应用程序选择是一项基本能力，指在调用细粒度工具（如API）之前决定使用哪个应用程序。这一过程决定了代理是否能初始化正确的环境，避免编排混淆，并高效地关注相关背景。然而，现有的基准测试主要评估细粒度API的选择，对于模型能否跨应用进行推理和选择不同的应用程序提供有限的见解。因此，为弥补这一点，作者引入了AppSelectBench，这是一个用于评估CUAs中应用选择的综合基准测试。AppSelectBench包含了一个新颖的用户任务生成管道，可以大规模生成现实、多样和语义地具有支持性的用户意图，并且涵盖了随机、启发式、零样本、少量样本和检索增强等统一的评价协议。AppSelectBench涉及了100个广泛使用的桌面应用程序，并包括了超过10万个现实、多样且语义地具有支持性的用户任务。广泛的实验涵盖了开源和闭源大型语言模型，揭示了跨应用程序推理的系统优势和劣势，表明即便是最优秀的模型在一致地选择应用程序方面仍存在问题。
### Innovation
引入了AppSelectBench作为一个用于评估CUAs中应用选择的综合基准测试。该基准测试包含了一个新颖的用户任务生成管道，能够大规模生成现实、多样且语义地具有支持性的用户意图。并且涵盖了多种统一的评价协议，包括随机、启发式、零样本、少量样本和检索增强等。AppSelectBench涉及了100个广泛使用的桌面应用程序，并包括了超过10万个现实、多样且语义地具有支持性的用户任务。实验揭示了跨应用程序推理的系统优势和劣势，表明即便是最优秀的模型在一致地选择应用程序方面仍有待改进。
### Conclusion
这些结果确立了AppSelectBench作为研究和推进应用级别推理的基础，这是一种智能CUAs所必需但尚未充分探索的能力。AppSelectBench的源代码可在此httpsURL中找到。
## 312. `cs.CL` - 社交媒体中检测心理健康状况和网络欺凌的一种机器学习方法 [PDF](https://arxiv.org/pdf/2511.20001), [HTML](https://arxiv.org/abs/2511.20001)
### Authors
Edward Ajayi,Martha Kachweka,Mawuli Deku,Emily Aiken
### Background
心理健康挑战和网络欺凌在数字空间中日益普遍，需要能够大规模且易于理解的检测系统。
### Innovation
提出了一个统一的多分类框架，用于从社交媒体数据中检测包括心理健康和网络欺凌在内的十个不同类别。采用了累进平衡流程训练模型，并在不平衡的真实测试数据集上进行评估。全面比较了传统的词频模型、混合方法和多种端到端微调变换器模型，结果显示端到端微调对性能至关重要，领域适应的MentalBERT在准确性和宏F1分数方面表现最佳。
### Conclusion
工作提供了稳健的基础模型，强调了在线安全与计算心理健康交汇处多标签、临床验证数据集的未来需求。系统被框架为带有辅助人员的筛查工具，并引入了HYBRID SHAPLLM可解释性框架和“社交媒体筛选器”原型仪表板，以整合模型预测及其解释，促进审核员的实际工作流程。
## 313. `cs.CL` - 更多偏差，更少偏差：用于增强多项选择题作答的BiasPrompting [PDF](https://arxiv.org/pdf/2511.20086), [HTML](https://arxiv.org/abs/2511.20086)
### Authors
Duc Anh Vu,Thong Nguyen,Cong-Duy Nguyen,Viet Anh Nguyen,Anh Tuan Luu
### Background
随着大规模语言模型（LLMs）的发展，它们在多项选择题（MCQ）任务上的表现显著提升。然而，现有的方法面临关键限制，即答案选项通常不提供上下文背景或解释给LLMs。这种缺乏上下文可能导致对所有可能答案的探索不完整，从而削弱模型的推理能力。
### Innovation
本文提出了一种名为BiasPrompting的新颖推理框架。该框架旨在引导LLMs生成并批判性地评估每个可能答案的推理，然后再做出最终预测。它包括两个组件：首先，推理生成阶段，模型被提示为每个答案选项生成支持性推理，然后，推理引导一致阶段，生成的推理被综合以选择最有可能的答案。BiasPrompting在五个广泛使用的多项选择题回答基准中展现了显著的进步。
### Conclusion
实验结果展示了BiasPrompting能够增强LLMs的推理能力，并为解决复杂和具有挑战性的问题提供了坚实的基础，特别是在现有方法表现不佳的场景中。
## 314. `cs.CL` - 无需模型训练的发音错误检测与诊断：基于检索的方法 [PDF](https://arxiv.org/pdf/2511.20107), [HTML](https://arxiv.org/abs/2511.20107)
### Authors
Huu Tuong Tu,Ha Viet Khanh,Tran Tien Dat,Vu Huan,Thien Van Luong,Nguyen Tien Cuong,Nguyen Thi Thu Trang
### Background
发音错误检测与诊断（MDD）是语言学习和语音治疗中的关键。现有的方法需要评分模型或训练音素级模型，这增加了复杂性。
### Innovation
提出了一种无需训练的新框架，该框架利用预训练的自动语音识别模型和检索技术。这种方法避免了音素特定的建模和额外的任务特异性训练，同时仍能实现发音错误的准确检测和诊断。
### Conclusion
在L2-ARCTIC数据集上的实验表明，该方法在不进行模型训练的情况下取得了69.60%的优秀F1分数。
## 315. `cs.CL` - Online-PVLM: 向个性化视觉语言模型引入在线概念学习 [PDF](https://arxiv.org/pdf/2511.20056), [HTML](https://arxiv.org/abs/2511.20056)
### Authors
Huiyu Bai,Runze Wang,Zhuoyun Du,Yiyang Zhao,Fengji Zhang,Haoyu Chen,Xiaoyong Zhu,Bo Zheng,Xuejiao Zhao
### Background
个性化视觉语言模型（VLMs）因其在用户特定概念对齐互动（例如，识别用户自己的自行车）方面的能力而受到越来越多的关注。现有的方法通常需要为每个新概念学习单独的嵌入，这在测试时无法支持实时适应。在大规模场景下，有效检索概念嵌入变得不切实际。
### Innovation
为了解决上述问题，我们提出了Online-PVLM框架，该框架利用双曲表示法实现在线概念学习。这种方法在测试时无需训练概念嵌入，从而使得个性化VLMs的使用既具有可扩展性又高效。此外，我们还开发了OP-Eval，这是一个全面且大规模的基准测试，包含1292个概念和超过30,000个高质量的实例，以涵盖多种问题类型，用于在现实场景中严谨地评估在线概念学习。
### Conclusion
广泛的实验表明，我们提出的框架具有最先进的性能。我们的源代码和数据集将被提供。
## 316. `cs.CL` - 在大规模批次场景中扩展LLM投机解码：非自回归预测 [PDF](https://arxiv.org/pdf/2511.20340), [HTML](https://arxiv.org/abs/2511.20340)
### Authors
Luohe Shi,Zuchao Li,Lefei Zhang,Baoyuan Qi,Guoming Liu,Hai Zhao
### Background
当前的投机解码方法通常假设有大量的计算资源可用，并使用小型自回归语言模型生成复杂的草稿树来提高预测准确性。然而，批处理等方法在主流模型推理系统中被广泛应用，作为与投机解码相比更为优越的选择，因为它们可以压缩可用的闲置计算资源。因此，使用低验证资源和低调度成本执行投机解码已成为一个重要研究问题。
### Innovation
提出了一个新颖的架构SpecFormer，结合单向和双向注意机制，克服了自回归模型依赖大量前缀树的问题。SpecFormer能够并行生成草稿序列，即使在大规模批次场景中也能实现一致加速。
### Conclusion
通过不同规模模型的无损投机解码实验表明，SpecFormer为以较低训练需求和减少计算成本扩展LLM推理设定了新标准。
## 317. `cs.CL` - MTA：用于个性化大语言模型的Merge-then-Adapt框架 [PDF](https://arxiv.org/pdf/2511.20072), [HTML](https://arxiv.org/abs/2511.20072)
### Authors
Xiaopeng Li,Yuanjin Zheng,Wanyu Wang,wenlin zhang,Pengyue Jia,Yiqi Wang,Maolin Wang,Xuetao Wei,Xiangyu Zhao
### Background
个性化大语言模型（PLLMs）旨在使模型输出与个别用户偏好保持一致，这对于以用户为中心的应用至关重要。然而，目前流行的方法是为每位用户单独微调一个模块，这种方法面临两大挑战：一是存储成本随用户数量线性增加，使得方法难以扩展；二是从头开始微调静态模型往往对于数据稀少的用户来说效果不佳。
### Innovation
我们提出了一种名为MTA的Merge-then-Adapt框架，用于PLLMs。该框架包括三个关键阶段：构建一个共享的Meta-LoRA Bank、引入适应性LoRA融合阶段以及提出LoRA堆叠用于少量样本个性化阶段。MTA通过合并LoRA、动态选择最相关的锚点LoRA来生成用户特定的LoRA，从而消除用户特定的存储需求并支持更灵活的个性化。
### Conclusion
在LaMP基准上的大量实验表明，我们的方法在多个任务上优于现有最优方法。
## 318. `cs.CL` - EM2LDL: 多语种语音语料库及标记分布学习在混合情绪识别中的应用 [PDF](https://arxiv.org/pdf/2511.20106), [HTML](https://arxiv.org/abs/2511.20106)
### Authors
Xingfeng Li,Xiaohan Shi,Junjie Li,Yongwei Li,Masashi Unoki,Tomoki Toda,Masato Akagi
### Background
现有的情绪识别数据集主要为单一语言和单一标签类型的情绪数据，这些数据集限制了语言多样性，无法建模混合情绪，缺乏生态效度。
### Innovation
EM2LDL 是一种新型多语言语音数据集，包括英语、 Mandarin 和 Cantonese，旨在通过标签分布学习推进混合情绪识别。它采用了在线平台上的自发情绪表达，并细分为 32 个类别进行注释。实验表明，使用自监督学习模型可以实现独立于说话者的性别、年龄和个性的情感识别。EM2LDL 支持探索多语言环境中的复杂情绪动态，为情绪计算中的适应性和共鸣系统开发提供了多用途的测试平台。
### Conclusion
EM2LDL 数据集、注释和基础代码已公开发布，为其在情感计算中的应用，如心理健康监测和跨文化沟通提供了潜在的研究工具。
## 319. `cs.CL` - KyrgyzBERT: 一种面向Kyrgyz自然语言处理的紧凑高效语言模型 [PDF](https://arxiv.org/pdf/2511.20182), [HTML](https://arxiv.org/abs/2511.20182)
### Authors
Adilet Metinov,Gulida M. Kudakeeva,Gulnara D. Kabaeva
### Background
Kyrgyz语是一种资源匮乏的语言，缺乏基础的自然语言处理（NLP）工具。
### Innovation
提出了KyrgyzBERT，这是第一个公开的Kyrgyz单一语言的BERT基语言模型。此外，还构建了kyrgyz-sst2数据集，用于情感分析基准测试。
### Conclusion
KyrgyzBERT在kyrgyz-sst2数据集上进行微调后，F1得分达到了0.8280，与较大规模的mBERT微调模型相当。所有模型、数据和代码均对外发布，以支持未来Kyrgyz NLP领域的研究。
## 320. `cs.CL` - REFLEX: 自我精炼的可解释事实核查，通过对真实性的风格和实质进行拆分实现 [PDF](https://arxiv.org/pdf/2511.20233), [HTML](https://arxiv.org/abs/2511.20233)
### Authors
Chuyi Kong,Gao Wei,Jing Ma,Hongzhan Lin,Zhiyuan Fan
### Background
社交媒体上的虚假信息危害公共信任，需要自动事实核查系统提供准确且可解释的判决。现有基于大型语言模型的方法往往依赖外部知识源，导致延迟和幻觉问题，影响系统的可靠性和解释性，这对于实时使用至关重要。这些挑战促使研究者开发新的方法来解决透明度、可靠性和响应速度的问题。
### Innovation
提出了REEncouraged Fact-checking with Latent EXplanations (REFLEX) 命名的框架。该框架旨在通过强化内部知识，提高判断准确性和解释质量。REFLEX 将事实核查重新定义为一种角色扮演对话，并结合训练判断预测和解释生成。它能够自适应地提取主模型与微调变体之间的对比激活对，构建引导向量，自然地拆分真实性和风格与内容，这些激活水平的信号可以指导推理并抑制噪音解释，从而实现更为忠实且高效的推理。
### Conclusion
实验结果表明，REFLEX 在处理事实核查任务中的细微、人类未知的事实时优于其他方法。仅使用 465 个自我精练的训练样本，REFLEX 达到了最先进的性能。此外，在具有解释目标的模型上训练的效果也能够引导未具有解释目标的模型，提高 7.57% 的性能，这表明内部解释信号在解释和提升事实推理方面发挥着双重作用。
## 321. `cs.CL` - SEDA：一种提升网格基础断裂实体识别模型效果的自适应实体中心化数据增强方法 [PDF](https://arxiv.org/pdf/2511.20143), [HTML](https://arxiv.org/abs/2511.20143)
### Authors
Wen-Fang Su,Hsiao-Wei Chou,Wen-Yang Lin
### Background
命名实体识别（NER）是自然语言处理中的关键任务，但对断续实体的处理仍然非常具有挑战性。传统方法在句间断续实体的分割和缺失问题上表现不佳，严重影响了识别准确性。近来的研究显示，基于网格的标记方法由于其灵活的标记方案和强大的架构，在信息提取任务中表现出色。
### Innovation
本文提出了一种基于网格的断续实体识别模型的数据增强方法SEDA，该方法通过引入图像数据增强技术（如裁剪、缩放和填充）来增强模型处理断续实体和解决分割挑战的能力。实验结果表明，传统的分割方法在捕捉句间断续实体方面效果不佳，而增强后的网格模型取得了显著改进。
### Conclusion
我们在CADEC、ShARe13和ShARe14数据集上的评估结果显示，SEDA方法在F1分数上总体提高了1-2.5%，对断续实体的提高更是达到了3.7-8.4%，验证了该方法的有效性。
## 322. `cs.CL` - SSA: 在特征空间中对齐全关注和稀疏关注输出的稀疏稀疏注意 [PDF](https://arxiv.org/pdf/2511.20102), [HTML](https://arxiv.org/abs/2511.20102)
### Authors
Zhenyi Shen,Junru Lu,Lin Gui,Jiazheng Li,Yulan He,Di Yin,Xing Sun
### Background
全注意在大型语言模型（LLMs）中处理长上下文时具有二次复杂度的限制，而稀疏注意通过限制每个查询只关注先前子集的令牌来降低成本，但这种方法常常导致性能严重下降。虽然原生稀疏注意方法（如NSA、MoBA）能够缓解这一问题，但这些方法在稀疏训练过程中排除了低排名的关键值对，这些对将不再接收前向贡献或反向梯度，从而无法学习适当的抑制。针对这一问题，本文提出了SSA（Sparse Sparse Attention）统一训练框架，使得每一层同时考虑稀疏和全注意力，并强制进行双向对齐，确保梯度流遍所有令牌，同时显式鼓励稀疏注意输出与全注意输出对齐，从而增强稀疏性。
### Innovation
SSA统一训练框架同时考虑稀疏和全注意力，并在每一层强制进行双向对齐，以确保梯度流遍所有令牌，同时显式鼓励稀疏注意输出与全注意输出对齐。
### Conclusion
SSA在多个常识性基准测试中的稀疏和全注意力推理均达到或接近当前最佳性能，模型能够平滑地适应不同稀疏预算。随着更多令牌被允许关注，整体性能持续提升，支持推理时的灵活计算性能折衷。此外，本文证明了原生稀疏注意训练能够通过减少注意值在特定区域的超额分配来改善长上下文外推能力，而SSA展示出最佳的外推能力。
## 323. `cs.CL` - 当数据稀缺，聪明地提示... 低资源环境中的语法错误纠正方法 [PDF](https://arxiv.org/pdf/2511.20120), [HTML](https://arxiv.org/abs/2511.20120)
### Authors
Somsubhra De,Harsh Kumar,Arun Prakash A
### Background
语法错误纠正（GEC）是自然语言处理的重要任务，旨在自动检测和纠正文本中的语法错误。近年来，基于变换器的模型和大规模标注数据的进展显著提高了英语等高资源语言的GEC性能，但对于大多数印度语言来说，由于资源有限、语言多样性以及复杂的形态结构，进展并不均衡。
### Innovation
本文探索了使用最先进的大型语言模型（LLMs），如GPT-4.1、Gemini-2.5和LLaMA-4结合少量示例策略，解决低资源环境中的GEC问题。即使是最基本的提示策略，如零样本和少样本方法，也使这些LLMs在矫正质量方面大大超越了细调后的印度语言模型，展现了当前LLMs在多语言GEC中出色的多语言泛化能力。精心设计的提示和轻量级适应显著提高了多种印度语言的矫正质量。
### Conclusion
实验表明，在各种印度语言中，精心设计的提示和轻量级适应显著提高了矫正质量。我们在共享任务中取得了领先成绩：泰米尔语排名第一（GLEU: 91.57），印地语排名第二（GLEU: 85.69），茶苔拉语排名第四（GLEU: 85.22），孟加拉语排名第五（GLEU: 92.86），马拉雅拉姆语排名第五（GLEU: 92.97）。这些发现突显了基于提示的NLP技术的有效性，并强调了大规模LLMs在多语言GEC中填补资源差距的潜力。
## 324. `cs.CL` - 现代NLP管道中的文本规范化任务导向评估框架 [PDF](https://arxiv.org/pdf/2511.20409), [HTML](https://arxiv.org/abs/2511.20409)
### Authors
Md Abdullah Al Kafi,Raka Moni,Sumit Kumar Banshal
### Background
文本规范化是许多自然语言处理(NLP)任务中必不可少的预处理步骤，其中一个方法是通过词干提取将单词还原为其基本形式。然而，评估词干提取方法具有挑战性，当前的评估方法有限，无法捕捉过度词干提取造成的潜在危害，因此需要开发新的评估方法来评估词干提取方法。
### Innovation
本文提出了一种新的、任务导向的任务评估框架，包括三个维度：（1）利用词干有效性得分（SES）评估词干提取的效用，（2）利用模型性能变化量（MPD）评估词干提取对下游任务的影响，（3）利用平均归一化Levenshtein距离（ANLD）来评估词干提取和原始词之间的语义相似度，从而提供了一个全面的评估框架。
### Conclusion
本文将评估框架应用于比较孟加拉语和英语的词干提取器，结果显示由于有效的词干提取，孟加拉语词干提取器获得了最高的SES（1.67），但由于其高SES可能源于有害的过度词干提取，而非高效率。相比之下，英语词干提取器虽然SES较低（1.31），但其对涵义的保存更为安全（ANLD = 0.14），因此更具可靠性，分别利用SES和ANLD可以区分潜在的效率提升与意义保留。
## 325. `cs.CL` - Transformer训练中的方向优化不对称性：一种合成的压力测试 [PDF](https://arxiv.org/pdf/2511.19997), [HTML](https://arxiv.org/abs/2511.19997)
### Authors
Mihir Sahasrabudhe
### Background
尽管Transformer模型理论上对反转是不变的，现实中的自然语言研究中频繁报告'反转诅咒'现象。近期对于大型语言模型时间不对称性的研究指出，真实的语料库自身携带着时间的方向性，这引发了一个未解之谜：方向性失败是来源于语言统计特性，还是模型架构本身？该研究设计了一个全合成的、熵控制的基准测试，作为干净室环境下的定向学习压力测试工具。利用具有可调分支因子K的随机字符串映射，构建了零条件熵的向前任务以及具有确定熵下限的逆任务。超过这些下限的额外损失揭示，即使是从头训练的GPT-2模型也表现出强烈的、可重复的定向优化差距（例如，在K=5时为1.16 nats）。同时，预先训练的初始化可能会改变优化行为，但并不能消除这种差距，而LoRA在网络在高熵逆映射上遭遇了容量壁垒。综合这些结果，研究隔离出一种高度简洁的、与语义无关的方向摩擦签名，即使去除语言先验、令牌频率和语料库层面的时间不对称性，这种特性依然存在。该基准提供了剖析现代序列模型中方向偏见的可控工具，鼓励深入探究为什么对于Transformer而言反转仍然从根本上更难。
### Innovation
该研究设计了一个全合成的、熵控制的基准测试，这种测试不仅可以用于清理室环境下的定向学习压力测试，而且能够揭示Transformer模型在训练过程中固有的方向性摩擦，即使当各种语言统计特性被移除后，这种现象仍然存在。进一步地，该研究发现即使是没有经过预训练的GPT-2模型，也表现出明显的定向优化差距，而LoRA在高熵逆映射上遇到了容量限制。
### Conclusion
该研究提供了一种可控的工具来剖析现代序列模型中方向偏见，并且鼓励对为什么反转任务对Transformer来说更难的功能性研究，表明这种偏向可能源于Transformer架构本身，而不是语言统计特性。
## 326. `cs.CL` - 使用单词提示生成、评估和解释小说家风格 [PDF](https://arxiv.org/pdf/2511.20459), [HTML](https://arxiv.org/abs/2511.20459)
### Authors
Mosab Rezaei,Mina Rajaei Moghadam,Abdul Rahman Shaikh,Hamed Alhoori,Reva Freedman
### Background
近期大型语言模型的发展为文体学研究带来了新机遇，但存在两个主要挑战：在缺乏配对数据的情况下训练生成模型，以及在不完全依赖人工判断的情况下评估文体文本。
### Innovation
本文提出了一个框架，用于生成和评估19世纪小说家风格的句子。通过最小的单词提示对大语言模型进行微调，以生成狄更斯、简·奥斯汀、马克·吐温等作者的声音文本。使用基于变压器的检测器进行评估，并结合句法比较和可解释AI方法进行解释，以识别风格模仿的语言线索。
### Conclusion
生成的文本反映了作者的独特模式，基于AI的评估为可靠的人工评估提供了替代方案。所有研究结果和相关工具均已在网上发布。
## 327. `cs.CL` - 类比推理的有趣案例：大型语言模型中的类比推理探究 [PDF](https://arxiv.org/pdf/2511.20344), [HTML](https://arxiv.org/abs/2511.20344)
### Authors
Taewhoo Lee,Minju Song,Chanwoong Yoon,Jungwoo Park,Jaewoo Kang
### Background
类比推理是人类认知的核心，对于各种智力活动至关重要。尽管先前的研究表明，大语言模型（LLMs）可以表示任务模式和表面概念，但目前尚不清楚这些模型能否编码高级关系概念，并通过结构化比较将它们应用于新颖情境。
### Innovation
本研究利用比例和故事类比这一基本方面进行探索，发现了三个关键发现：1）LLMs能有效编码类比实体之间的根本关系；2）与人类不同，LLMs在缺失关系信息时会遇到困难，即使试图应用这些信息到新实体上也会遇到挑战；3）LLMs成功进行类比推理表现为类比情况间的强烈结构对齐；而失败则表明结构对齐遭到破坏或位置不当。
### Conclusion
我们的发现表明，LLMs在编码和应用高级关系概念方面表现出初始但有限的能力，既揭示了与人类认知的相似性也揭示了差距。
## 328. `cs.CL` - 通过评估LLM担任评委来评估LLM对齐 [PDF](https://arxiv.org/pdf/2511.20604), [HTML](https://arxiv.org/abs/2511.20604)
### Authors
Yixin Liu,Pengfei Liu,Arman Cohan
### Background
LLMs（大型语言模型）需要具备帮助、诚实、安全等属性，并且要精确遵循人类指令。评估这些模型对齐情况通常涉及直接评估它们的开放式回复，这需要人类标注者或强LLM来评判。另一方面，LLMs本身也被广泛用作评估者来评判对齐情况。本文探讨了LLMs生成能力和评估能力在对齐人类偏好方面的关系。研究发现在强LLM偏好判断者评估下，生成和评估能力之间有强相关性。
### Innovation
本文提出了一个基准标杆 AlignEval，它不直接评估模型生成的输出，而是评估模型担任评估者的角色。研究结果表明，AlignEval绩效可与广泛使用的自动LLM评估基准，如AlpacaEval和Arena-Hard相媲美，或者更好，在对LLMs进行排名时捕捉到人类偏好。
### Conclusion
研究表明，LLMs的生成能力和评估能力之间存在强关联。文章提出了一个不直接评估模型输出的基准基准AlignEval，该基准能够在评估LLMs对齐人类偏好方面取得成功。
## 329. `cs.CL` - The Text Aphasia Battery (TAB): 一个语言模型类似失语症缺陷的临床基准 [PDF](https://arxiv.org/pdf/2511.20507), [HTML](https://arxiv.org/abs/2511.20507)
### Authors
Nathan Roll,Jill Kries,Flora Jin,Catherine Wang,Ann Marie Finley,Meghan Sumner,Cory Shain,Laura Gwilliams
### Background
大型语言模型（LLMs）作为人类语言的候选“模式生物”，为研究语言障碍如失语症的计算基础提供了前所未有的机会。然而，传统的临床评估方法不适合LLMs，因为它们假定人类特有的语用压力，并测试了人工架构不存在的认知过程。因此，迫切需要专门针对LLMs的评估工具。
### Innovation
介绍了文本失语电池（TAB），这是一个文本仅评估基准，基于快速失语症评估电池（QAB）进行调整，用于评估LLMs中的类似失语症缺陷。TAB包括四个子测试：连贯性文本、词项理解、句子理解、重复。此外，还提供了一种自动化评估协议，使用Gemini 2.5 Flash进行了验证，其可靠性与专家人类评分者相当。这项工作提供了一个基于临床的可扩展框架，用于分析人工系统的语言缺陷。
### Conclusion
TAB作为一个基于临床的、可扩展的框架，用于分析人工系统的语言缺陷，已经得到了验证，并可以广泛应用于大规模评估。其自动评估协议在可靠性上与专家人类评分相当，为未来研究提供了重要工具。
## 330. `cs.CL` - 通过潜在混音合成语音多样性以实现公平的语音识别 [PDF](https://arxiv.org/pdf/2511.20534), [HTML](https://arxiv.org/abs/2511.20534)
### Authors
Wesley Bian,Xiaofeng Lin,Guang Cheng
### Background
现代机器学习模型在英语等资源丰富语言的音频任务中表现出优越性能，主要得益于大量可用训练数据。然而，低资源语言的数据收集既困难又昂贵，导致这些语言在性能上的不公平差距。本文探讨了为语音语料库引入一种新的数据增强技术，以缩小这一差距。
### Innovation
本文介绍了一种新的数据增强技术，即潜在混音（Latent Mixup），这种方法能够显著提高自动语音识别系统在低资源语言上的性能。此外，所提出的方法也优于现有增强策略，为增强未被广泛代表的语言社区的语音技术提供了一个实用解决方案。
### Conclusion
通过全面的实验，我们证明了我们的方法能显著提升低资源语言自动化语音识别系统的性能，并且该方法在增强语音技术在缺乏资源语言社群中的应用方面表现优于其他方法。
## 331. `cs.CL` - 多代理系统中的潜在协作 [PDF](https://arxiv.org/pdf/2511.20639), [HTML](https://arxiv.org/abs/2511.20639)
### Authors
Jiaru Zou,Xiyuan Yang,Ruizhong Qiu,Gaotang Li,Katherine Tieu,Pan Lu,Ke Shen,Hanghang Tong,Yejin Choi,Jingrui He,James Zou,Mengdi Wang,Ling Yang
### Background
多代理系统（MAS）将大型语言模型（LLMs）从独立单模型推理扩展到协调系统级别的智能。现有的LLM代理依赖于基于文本的调解来进行推理和交流。
### Innovation
提出了LatentMAS框架，该框架允许LLM代理在潜在空间中直接协作。每个代理通过最后一层隐藏嵌入自回归地生成内在想法，共享的潜在工作记忆则保留并转移每个代理的内部表示，确保了信息的无损交换。理论分析表明，LatentMAS在表达性和信息保真度方面优于传统的基于文本的MAS，同时具有较低的复杂性。实验评估表明，LatentMAS在覆盖数学和科学推理、常识理解和代码生成的9项全面基准测试中，持续超过了强大的单模型和基于文本的MAS基线，准确率提高了14.6%，输出令牌使用减少了70.8%-83.7%，端到端推理速度提高了4倍至4.3倍。
### Conclusion
LatentMAS框架提高了系统级推理质量，同时带来了显著的效率提升，无需额外的训练即可实现性能提升。相关代码和数据已完全开源。
## 332. `cs.CL` - 从话语到智慧：学生对话理解的标注和baseline模型 [PDF](https://arxiv.org/pdf/2511.20547), [HTML](https://arxiv.org/abs/2511.20547)
### Authors
Farjana Sultana Mim,Shuchin Aeron,Eric Miller,Kristen Wendell
### Background
识别学生对话中的话语特征对于教育研究者来说非常重要，可以帮助他们识别导致学生进行知识构建而不是仅仅完成任务的课程与教学变量。手动分析学生对话以识别这些话语特征耗时且劳动密集，这限制了研究的规模和范围。利用自然语言处理（NLP）技术可以简化这一过程，提供可扩展的数据驱动见解。然而，现有的NLP研究很少关注对话中的教育数据。本研究通过引入标注教育对话数据集和使用预训练的大语言模型GPT-3.5和Llama-3.1建立基准模型来解决这个问题。
### Innovation
本研究的创新之处在于提供了专门针对学生对话理解的标注教育对话数据集，同时使用最先进的预训练语言模型来自动预测对话中每个回合的话语属性。
### Conclusion
实验结果表明，最先进的模型在这个任务上的性能不佳，这表明未来的研究有巨大的潜力和空间。
## 333. `cs.CL` - 对抗混淆攻击：干扰多模态大语言模型 [PDF](https://arxiv.org/pdf/2511.20494), [HTML](https://arxiv.org/abs/2511.20494)
### Authors
Jakub Hoscilowicz,Artur Janicki
### Background
本文介绍了对抗混淆攻击，这是一种针对多模态大型语言模型（MLLMs）的新类别威胁。这种攻击的目标是引发一种系统性的干扰，使得模型生成无意义或自信错误的输出。对抗混淆攻击的应用场景包括在网站中嵌入对抗图像，以防止基于MLLM的代理可靠地运行。
### Innovation
提出的攻击方法利用小规模的开源MLLM集合最大化下一个标记的熵。在白盒设置下，研究显示单个对抗图像可以同时干扰整个模型集合，在完整图像和对抗CAPTCHA设置中效果显著。尽管攻击的基础技术是简单的对抗性技术（PGD），但它仍能生成能够影响未见过的开源（例如，Qwen3-VL）和专有（例如，GPT-5.1）模型的扰动。
### Conclusion
该研究展示了对抗混淆攻击的有效性，并揭示了即使是基本的对抗性技术也可以在不同的MLLM环境中发挥重要作用。
## 334. `cs.CL` - BengaliFig: 达拉克鲁普：孟加拉语低资源挑战 [PDF](https://arxiv.org/pdf/2511.20399), [HTML](https://arxiv.org/abs/2511.20399)
### Authors
Abdullah Al Sefat
### Background
大型语言模型在多语言基准测试中表现出色，但在形象化和文化背景下推理方面的评估仍不够充分，尤其是在低资源语言环境中。孟加拉语是一种广泛使用的低资源语言，缺乏针对其形象化和文化推理能力的挑战性数据集。论文介绍了BengaliFig，一个针对孟加拉语形象化和文化推理能力的挑战性数据集。
### Innovation
BengaliFig 提供了一个包含 435 个独特谜题的数据集，这些谜题来自孟加拉语口语和文学传统。每个项目都沿五个正交维度进行了标注，涵盖了推理类型、陷阱类型、文化深度、答案类别和难度。数据集通过一个感知约束、AI 辅助的管道自动转换为多项选择格式，这对于评估大型语言模型在低资源文化背景下的鲁棒性具有重要意义。
### Conclusion
BengaliFig 不仅是一个诊断性工具，用于评估大型语言模型在低资源文化环境中的稳健性，而且是朝着包容性和文化遗产意识的人工智能评价体系迈进的一步。研究发现，八个主要提供商的前沿大型语言模型在其隐喻性和文化特定推理方面存在一致的薄弱环节。
## 335. `cs.CL` - 通过解纠缠多模态表示来量化模态贡献 [PDF](https://arxiv.org/pdf/2511.19470), [HTML](https://arxiv.org/abs/2511.19470)
### Authors
Padegal Amit,Omkar Mahesh Kashyap,Namitha Rayasam,Nidhi Shekhar,Surabhi Narayan
### Background
目前，量化多模态模型中模态的贡献仍然存在挑战，现有的方法往往混淆了贡献的概念本身。先前的工作主要依赖于基于准确性的方法，通过移除一种模态后性能下降来推测其影响。然而，这种方法无法区分模态是否本身具有信息价值，还是其价值仅通过与其他模态的相互作用产生。这一点在跨注意力架构中尤为重要，因为模态之间互相影响彼此的表示。
### Innovation
本文提出了一种基于部分信息分解（PID）的框架，通过将内部嵌入中的预测信息分解为独特的、冗余的和协同的成分来量化模态的贡献。为了解决可扩展性问题，我们开发了一种基于迭代比例拟合程序（IPFP）的算法，在不重新训练的情况下计算各层和数据集级别的贡献，从而提供一种有原则的方法来获取多模态行为的表示层面视图，这比基于结果的度量提供了更清晰、更可解释的见解。
### Conclusion
本研究提出了一种新的基于PID的方法，通过将模态预测信息分解为独特的、冗余的和协同的成分来量化它们的贡献，并开发了一种可伸缩的算法来计算模态贡献，无需重新训练。这种方法提供了一种更清晰、更可解释的多模态行为视图。
## 336. `cs.CL` - BlockCert：变压器机制的认证块级提取 [PDF](https://arxiv.org/pdf/2511.17645), [HTML](https://arxiv.org/abs/2511.17645)
### Authors
Sandro Andric
### Background
机制可解释性致力于拆解神经网络成明确的算法，而模型编辑则旨在修改特定行为而不重新训练。这两个领域通常通过非正式证据和针对性实验来评估，缺乏关于提取或修改的模型在相关输入上与原始模型偏差的具体保证。
### Innovation
引入了BlockCert框架，用于认证块级提取变压器机制，并介绍了如何通过轻量级扩展支持认证局部编辑。该框架在预训练变压器和提示分布下提取残差块的结构化代理实现，并提供可机器检查的证书以限制近似误差、记录覆盖率指标并生成底层文件的哈希值。还通过Lean 4形式化了一个简单的Lipschitz基组合定理，将这些局部保证提升至全局偏差界限。
### Conclusion
实验展示了BlockCert框架在GPT-2 small、TinyLlama-1.1B-Chat和Llama-3.2-3B模型上实现了高块级覆盖率和小型残留误差，特别是在TinyLlama设置中，完整缝合的模型在压力提示下逼近基准困惑度约6e-5。这些结果显示块级提取具有明确证书适用于实际变压器语言模型，并构成机制可解释性和模型行为形式化推理之间的一个实际桥梁。
## 337. `cs.CL` - 在VLMs中扩展具有工具整合的推理的代际强化学习 [PDF](https://arxiv.org/pdf/2511.19773), [HTML](https://arxiv.org/abs/2511.19773)
### Authors
Meng Lu,Ran Xu,Yi Fang,Wenxuan Zhang,Yue Yu,Gaurav Srivastava,Yuchen Zhuang,Mohamed Elhoseiny,Charles Fleming,Carl Yang,Zhengzhong Tu,Yang Xie,Guanghua Xiao,Hanrui Wang,Di Jin,Wenqi Shi,Xuan Wang
### Background
尽管最近的视觉-语言模型（VLMs）在图像理解方面表现出色，但它们通过多步视觉交互进行“思考”的能力，即进行视觉推理，仍然有限。
### Innovation
VISTA-Gym是一个可扩展的训练环境，用于激励VLMs整合工具的视觉推理能力。它统一了多种现实世界的多模态推理任务，提供了标准化的视觉工具接口、可执行的交互循环、可验证的反馈信号和高效的轨迹记录，以实现大规模的视觉主动强化学习。VISTA-Gym针对工具选择、调用和协调等困难，训练了VISTA-R1，利用多轮轨迹采样和端到端强化学习进行工具使用的整合推理。
### Conclusion
在11个公共推理密集型VQA基准测试中，VISTA-R1-8B的表现超过了相似规模下的最新基线，提升了9.51%-18.72%，证明VISTA-Gym是一个有效的训练平台，能够解锁VLMs的工具整合推理能力。
## 338. `cs.CL` - 大规模研究地图：地图制图学及图示演变的数字化调查 [PDF](https://arxiv.org/pdf/2511.19538), [HTML](https://arxiv.org/abs/2511.19538)
### Authors
Remi Petitpierre
### Background
全球范围内，遗产机构已数字化超过一百万张地图，自动技术现在使得地图内容的大规模识别和提取成为可能。然而，这些方法很少涉及制图学历史，或认为地图是具有符号意义的文化对象，反映了政治和知识期望。
### Innovation
该研究利用了来自38个数字目录的771,561张地图记录和99,715张数字化图像的多样化合集数据集。引入了语义分割技术和目标检测模型用于土地类别的通用识别和制图符号的检测，分析了土地类别并展示了地图设计如何通过中心和语义对称性强调特征。通过分析图示研究和合作与扩散的研究，揭示了图示规范和符号文化在传播中的重要作用。
### Conclusion
这些数据使得可以通过地理结构和地图出版的全球历史时间轴来描绘地理结构。进一步的研究结果揭示了国家、民族焦点的发展，以及军事冲突对出版量的影响。该研究通过图表和符号分析提出了新的见解，突显了地图作为文化对象的特点及其在政治与历史事件中的反映。
## 339. `cs.CL` - 通过提示语义空间优化实现无需训练的多样且高质量图像生成 [PDF](https://arxiv.org/pdf/2511.19811), [HTML](https://arxiv.org/abs/2511.19811)
### Authors
Debin Meng,Chen Jin,Zheng Gao,Yanran Li,Ioannis Patras,Georgios Tzimiropoulos
### Background
文本到图像的扩散模型仍然面临图像多样性不足的根本挑战。低多样性模型往往会生成重复的输出，增加采样冗余，并妨碍创新探索和下游应用。主要原因是生成过程往往会朝学习分布中的主要模式收敛。现有提高多样性的尝试，如重新采样噪声、改写提示或基于引导的控制，仍然容易收敛到主要模式，或者引入了降低图像质量的失真。
### Innovation
提出了一种无需训练且模型通用的模块——Token-Prompt嵌入空间优化（TPSO），通过引入可学习参数来探索令牌嵌入空间中被忽视的区域，从而减少模型重复生成来自学习分布主要模式的样本的趋势。同时，提示级别空间提供了一个全局语义约束，控制分布变化，防止质量下降并保持高保真度。
### Conclusion
在MS-COCO和三种扩散基础模型上的大量实验表明，TPSO显著提高了生成多样性，将基线性能从1.10提高到4.18，没有牺牲图像质量。代码将在接受后发布。
## 340. `cs.CL` - Fara-7B: 一种高效代理模型用于计算机使用 [PDF](https://arxiv.org/pdf/2511.19663), [HTML](https://arxiv.org/abs/2511.19663)
### Authors
Ahmed Awadallah,Yash Lara,Raghav Magazine,Hussein Mozannar,Akshay Nambi,Yash Pandya,Aravind Rajeswaran,Corby Rosset,Alexey Taymanov,Vibhav Vineet,Spencer Whitehead,Andrew Zhao
### Background
计算机使用代理（CUAs）的发展受到缺乏大规模和高质量的数据集的限制，这些数据集能够捕捉到人类如何与计算机交互。尽管大型语言模型（LLMs）在大量文本数据中发展得非常成功，但尚未有类似的数据集供CUA轨迹使用。为了解决这一问题，本文引入了FaraGen，这是一个新颖的合成数据生成系统，专门用于多步网页任务。
### Innovation
FaraGen能够提出多样的任务，从常用网站中生成多个解决方案尝试，并使用多个验证器筛选成功的轨迹。该系统能够实现高吞吐量、高产出和多样性，生成每条验证轨迹的成本大约为1个单位。基于此数据集训练了Fara-7B，这是一种仅使用截图感知计算机的原生CUA模型，通过预测坐标执行操作，并能在设备上运行。Fara-7B在WebVoyager、Online-Mind2Web和WebTailBench（一种新型基准测试）等基准测试中表现出色，尤其是后者更准确地反映了现有基准测试中未充分代表的网页任务。
### Conclusion
Fara-7B与更大规模的前沿模型竞争，展示了可扩展数据生成系统在推动小型高效代理模型方面的关键优势。同时，Fara-7B已经开源并提供在Microsoft Foundry和HuggingFace上使用，同时发布了WebTailBench基准测试以供更多研究和评估使用。
## 341. `cs.CL` - CounterVQA: 评估和提高视觉语言模型在视频理解中的反事实推理能力 [PDF](https://arxiv.org/pdf/2511.19923), [HTML](https://arxiv.org/abs/2511.19923)
### Authors
Yuefei Chen,Jiang Liu,Xiaodong Lin,Ruixiang Tang
### Background
视觉语言模型（VLMs）在视频理解方面已经取得了显著进展，特别是在特征对齐、事件推理和指令执行任务方面。然而，这些模型在反事实推理方面的能力，即在假设条件下推断可能的结果，尚未得到充分探索。这种能力对于稳健的视频理解至关重要，因为它需要识别潜在的因果结构并推理未观察到的可能性，而不仅仅是识别已观察到的模式。
### Innovation
研究引入了一个名为CounterVQA的视频基准测试，包含三个不同难度等级的部分，用于评估不同维度的反事实推理能力。通过全面评估最先进的开源和封闭源模型，研究揭示了一个巨大的性能差距：尽管这些模型在简单的反事实问题上表现良好，但在复杂的多步骤因果链上性能显著下降。为此，研究开发了一个后训练方法，称为CFGPT，通过从语言模态中提取反事实推理能力来增强模型的视觉反事实推理能力，实现CounterVQA所有难度等级上的一致改进。
### Conclusion
研究将进一步发布数据集和代码。
## 342. `cs.CL` - 细节中的魔鬼：开放权重LLM中的新兴偏差、格式与连贯性 [PDF](https://arxiv.org/pdf/2511.20104), [HTML](https://arxiv.org/abs/2511.20104)
### Authors
Craig Dickson
### Background
先前研究表明，对特定领域进行微调时使用数据与目标不一致的数据可能导致广泛的不一致性，这一现象被称为‘新兴偏差’。所有测试的模型都容易受到这种不一致性的影响，但不同模型的抵抗力差异较大。特别是Qwen-2.5系列表现出了较强的抗性，而GPT-4o则表现出最强的不一致性。该研究旨在评估当前开放权重模型是否像Qwen-2.5系列一样具有抗性，并衡量不同模型架构和规模下的不一致性鲁棒性。
### Innovation
研究通过在九个现代开放权重模型（Gemma 3和Qwen 3家族，1B到32B参数）上复制出相似的发现，评估了新兴偏差的抗性。研究发现，与基础模型相比，经过不安全代码生成细调的模型的不一致性率提高了0.68%，这与之前开放模型的结果底部相匹配，但远低于GPT-4o的20%。此外，研究还发现，要求JSON输出会将不一致性率翻倍（9.6% vs 4.2%），这表明结构约束可能绕过了安全训练，减少了模型的‘自由度’来拒绝。这项发现确认了新兴偏差在现代开放权重模型中是一个可重复的现象，其比率低于专有系统的观察结果。
### Conclusion
研究证实了新兴偏差是一个可重复的现象，这在现代开放权重模型中普遍存在，但其比率显著低于专有系统。此外，研究还发现了一个关键的格式依赖性漏洞，即要求JSON输出会显著增加模型的不一致性。这些结果为进一步理解开放权重模型的安全性和改进提出了新的挑战。
## 343. `cs.CL` - MAPS：通过模块级接近调度方式保留视觉-语言表示以实现更好的视觉-语言-行动泛化 [PDF](https://arxiv.org/pdf/2511.19878), [HTML](https://arxiv.org/abs/2511.19878)
### Authors
Chengyue Huang,Mellon M. Zhang,Robert Azarcon,Glen Chou,Zsolt Kira
### Background
现有的视觉-语言-行动（VLA）模型继承了预训练的视觉-语言模型（VLM）的先验知识，但直接的微调往往会破坏这些表示，降低模型的泛化能力。现有的解决方案，如冻结模块或应用统一正则化，虽然可以在一定程度上防止模型过度适应，但往往无法充分适应VLA组件的不同角色。
### Innovation
本文提出了一种名为MAPS（Module-Wise Proximity Scheduling）的模块级接近调度框架，这是一种针对VLA的稳健微调方法。MAPS通过系统分析，确定了缓解接近约束的最佳顺序，以平衡稳定性和灵活性。该方法通过逐步放松近似约束，使视觉编码器能够保持接近其预训练先验，而以行动为导向的语言层则可以自由适应。MAPS无额外的参数和数据要求，并可以无缝集成到现有的VLA中。
### Conclusion
在MiniVLA-VQ、MiniVLA-OFT、OpenVLA-OFT以及SimplerEnv、CALVIN、LIBERO等挑战性基准测试中，MAPS在保持分布内效果的同时，显著提升了分布外性能，最多可以提高30%。研究结果表明，通过经验引导，接近预训练VLM是保留VLM到VLA传输中的广泛泛化的简单但有效的原则。
## 344. `cs.CL` - QiMeng-Kernel：基于LLM的高性能GPU内核生成宏思考微观编码范式 [PDF](https://arxiv.org/pdf/2511.20100), [HTML](https://arxiv.org/abs/2511.20100)
### Authors
Xinguo Zhu,Shaohui Peng,Jiaming Guo,Yunji Chen,Qi Guo,Yuanbo Wen,Hang Qin,Ruizhi Chen,Qirui Zhou,Ke Gao,Yanjun Wu,Chen Zhao,Ling Li
### Background
开发高性能GPU内核对于AI和科学计算至关重要，但由于依赖专家精心设计和缺乏移植性，这一过程依然具有挑战性。尽管大型语言模型（LLM）提供了自动化潜力，但通用和微调后的LLM都存在两个基本且相互矛盾的限制：即正确的实现和高效的执行。根本原因在于现有基于LLM的方法直接生成完整的优化低级程序，要求探索一个极其广泛的优化政策和实现代码空间。
### Innovation
提出了一种名为Macro Thinking Micro Coding (MTMC) 的分层框架，其灵感来源于人类专家的分阶段优化策略。MTMC 将优化策略与实现细节分离，通过高层次策略确保效率，通过低层次实现确保正确性。具体而言，MTMC 使用强化学习引导轻量级的LLM高效探索和学习最大化硬件利用率的语义优化策略。而微编码则利用通用的LLM逐步实现来自宏观思考的逐步优化提案，避免全内核生成错误。
### Conclusion
MTMC 通过充分探索和精细实施在GPU内核生成中表现出卓越的性能。在广泛应用的基准测试上，MTMC 在准确性和运行时间上均优于现有最佳通用和领域微调的LLM。特别是在更具有挑战性的TritonBench基准测试中，MTMC 达到了最高59.64%的准确率和最高34倍的速度提升。
## 345. `cs.CL` - EfficientXpert: 通过传播意识剪枝实现大型语言模型的有效领域适应 [PDF](https://arxiv.org/pdf/2511.19935), [HTML](https://arxiv.org/abs/2511.19935)
### Authors
Songlin Zhao,Michael Pitts,Zhuwei Qin
### Background
随着大型语言模型（LLMs）的迅速发展，对专业领域的变种需求增加，如法律、医疗和金融等领域。然而，模型的庞大尺寸使得在资源受限的环境中部署成为一个障碍。现有的压缩方法要么跨领域表现不佳，要么会带来较高的开销。
### Innovation
提出了一个轻量级的领域剪枝框架EfficientXpert，结合了传播意识剪枝标准（Foresight Mask）和高效的适配器更新算法（Partial Brain Surgeon）。该框架整合到LoRA微调过程中，能够一步将通用预训练模型转换为稀疏的领域适配专家。在健康和法律任务上，它在40%稀疏度下保留了98%的密集模型性能，超过最先进的方法。进一步分析揭示了领域依赖的结构变化，削弱了通用剪枝掩码的有效性，强调了需要针对每个领域定制的适应性、领域感知剪枝策略。
### Conclusion
EfficientXpert能够在资源受限环境下有效地适应特定领域，并显著提升了稀疏模型的性能，且显示出针对不同领域进行结构分析的重要性。
## 346. `cs.CL` - 软适应性策略优化 [PDF](https://arxiv.org/pdf/2511.20347), [HTML](https://arxiv.org/abs/2511.20347)
### Authors
Chang Gao,Chujie Zheng,Xiong-Hui Chen,Kai Dang,Shixuan Liu,Bowen Yu,An Yang,Shuai Bai,Jingren Zhou,Junyang Lin
### Background
强化学习（RL）在增强大型语言模型（LLM）的推理能力方面发挥着越来越重要的作用，但稳定性和性能的最佳策略优化仍然具有挑战性。令牌级别的重要性比率经常表现出高方差，这一现象在混合专家模型中尤为突出，导致不稳定的更新。现有的基于组的策略优化方法，如GSPO和GRPO，通过硬剪辑来缓解此问题，但难以同时保持稳定性和有效的学习。
### Innovation
我们提出了软适应性策略优化（SAPO），它用一个平滑的、温度控制的门控机制取代了硬剪辑，可以适配性地减轻非策略更新的影响，同时保持有用的学习信号。与GSPO和GRPO相比，SAPO具有序列连贯性和令牌适应性。SAPO通过软门控形成了连续的信任区域，避免了GSPO中使用的脆弱硬剪辑带，从而提高了样本效率并增强了优化策略的可靠性。
### Conclusion
实验结果表明，SAPO在数学推理基准测试中表现出更高的训练稳定性以及更好的性能指标。我们利用SAPO训练了Qwen3-VL模型系列，展示了SAPO在多种任务和不同模型规模下的一致性能提升。综合来看，SAPO为大型语言模型的RL训练提供了一种更可靠、更可扩展且更有效的优化策略。
## 347. `cs.CL` - 基于奇异向量的变压器电路解释超越组件 [PDF](https://arxiv.org/pdf/2511.20273), [HTML](https://arxiv.org/abs/2511.20273)
### Authors
Areeb Ahmad,Abhinav Joshi,Ashutosh Modi
### Background
基于变压器的语言模型表现出复杂的分布式行为，但它们的内部计算机制仍然不甚明了。现有的机制解释方法通常将注意力头和多层感知器（MLPs）作为不可分割的单位处理，忽视了它们内部可能存在的功能子结构。
### Innovation
本文引入了一个更细致的视角，将这些组件分解为正交的奇异方向，揭示了单一头部或MLP中的叠加且独立的计算。特别是在间接宾语识别（IOI）、性别代词（GP）、大于（GT）等广泛应用的标准任务上验证了这一视角，表明先前识别的经典功能头部（如名称搬运者）编码了多个重叠的亚功能，与不同的奇异方向对齐。此外，先前识别为电路元件的计算图节点在特定低秩方向上显示出强烈的激活，暗示重要计算驻留在紧凑子空间中。
### Conclusion
我们的结果强调，与之前的假设相比，变压器的计算更加分散、结构化和组合。这一视角为细致的机制解释和对模型内部结构的更深入理解开辟了新的途径。
## 348. `cs.CL` - 语言模型中决策几何学 [PDF](https://arxiv.org/pdf/2511.20315), [HTML](https://arxiv.org/abs/2511.20315)
### Authors
Abhinav Joshi,Divyanshu Bhatt,Ashutosh Modi
### Background
大型语言模型（LLMs）在多种任务上表现出强大的泛化能力，但其内部决策过程仍然不透明。这项工作中，研究者们通过内在维度（ID）的研究视角，探讨了LLMs中隐藏表示的几何结构，特别是集中在多项选择问答（MCQA）场景中的决策动态。
### Innovation
使用大量开放权重的变压器模型（共28个），并用多种估计器来估算每层的内在维度，同时还量化了每层在MCQA任务上的表现。研究发现不同模型在不同层的表现具有相似的内在维度模式，进一步揭示LLMs如何隐式地将语言输入投影到与任务特定决策相匹配的低维结构化空间中，提供了新的几何洞察，说明了语言模型是如何生成和推理的。
### Conclusion
研究结果表明，早期层在低维流形上操作，中间层扩展这个空间，后期层又将其压缩回到与决策相关联的表示中。这表明LLMs隐式地学习将语言输入投影到与任务相关的结构化低维流形上，为理解语言模型的泛化能力和推理机制提供了新的几何学见解。
## 349. `cs.CL` - 长上下文语言模型的综述 [PDF](https://arxiv.org/pdf/2503.17407), [HTML](https://arxiv.org/abs/2503.17407)
### Authors
Jiaheng Liu,Dawei Zhu,Zhiqi Bai,Yancheng He,Huanxuan Liao,Haoran Que,Zekun Wang,Chenchen Zhang,Ge Zhang,Jiebin Zhang,Yuanxing Zhang,Zhuo Chen,Hangyu Guo,Shilong Li,Ziqiang Liu,Yong Shan,Yifan Song,Jiayi Tian,Wenhao Wu,Zhejian Zhou,Ruijie Zhu,Junlan Feng,Yang Gao,Shizhu He,Zhoujun Li,Tianyu Liu,Fanyu Meng,Wenbo Su,Yingshui Tan,Zili Wang,Jian Yang,Wei Ye,Bo Zheng,Wangchunshu Zhou,Wenhao Huang,Sujian Li,Zhaoxiang Zhang
### Background
长期文本、对话和其他文本数据的增多使得高效处理长上下文成为自然语言处理的一个持续追求。开发能够有效高效地处理和分析大量输入的长上下文语言模型（LCLMs）变得尤为重要。
### Innovation
本文综述了近年来长上下文建模在大型语言模型方面的发展。讨论了获得有效高效LCLMs的数据策略、架构设计和工作流程方法。详细分析了LCLM的训练和推理基础设施。提出了针对长上下文理解和长文本生成的评估范式，以及LCLMs的行为分析和机制可解释性。
### Conclusion
本文提供了迄今为止长上下文LLM文献的回顾，希望通过综述为研究人员和工程师提供有价值的资源。同时，提供了收集最新论文和项目的GitHub仓库链接。
## 350. `cs.CL` - BiasJailbreak:分析大型语言模型中的道德偏向和漏洞 [PDF](https://arxiv.org/pdf/2410.13334), [HTML](https://arxiv.org/abs/2410.13334)
### Authors
Isack Lee,Haebin Seong
### Background
尽管大型语言模型（LLMs）在各类任务中表现出色，但也存在潜在的安全风险，如‘模型突破’，即恶意输入可以使LLMs绕过安全限定生成有害内容。本文探讨了LLMs中的道德偏向及其如何被利用进行‘模型突破’，发现在GPT-4模型中，与非二元和跨性别关键词相比，非二元与 cis 性别关键词之间的突破成功率相差20%，而与白人和黑人关键词相比则相差16%，尽管其他部分的提示内容是一致的。这表明，即使在其他条件相同的情况下，这类道德偏向依然会导致生成不同的有害输出。
### Innovation
本文提出了BiasJailbreak的概念，自动生成具有偏向性的关键词并利用这些关键词生成有害输出。另外，还提出了一种名为BiasDefense的高效防御方法，它通过在生成前注入防御提示来阻止‘模型突破’尝试，作为另一种替代Guard Models的方法，BiasDefense不需要在文本生成后增加额外的推理成本。本研究强调了语言模型中的道德偏见可以导致生成不安全输出，并提供了一种使LLMs更安全、更无偏的方法。
### Conclusion
本研究强调了伦理偏见对语言模型安全性的影响，并建议了一种防御方法。提出的BiasDefense方法比Guard Models更具优势，因为它不需要在文本生成后增加额外成本。为了支持进一步的研究和改进，我们开源了BiasJailbreak的代码和相关资源，为社区提供更好地理解和减轻语言模型中由安全偏见引发的风险的工具。
## 351. `cs.CL` - 统一多模态模型中理解是否指导生成？从分析到前进之路 [PDF](https://arxiv.org/pdf/2511.20561), [HTML](https://arxiv.org/abs/2511.20561)
### Authors
Yuwei Niu,Weiyang Jin,Jiaqi Liao,Chaoran Feng,Peng Jin,Bin Lin,Zongjian Li,Bin Zhu,Weihao Yu,Li Yuan
### Background
近年来，统一多模态模型取得了显著进展，但一个基本问题仍然存在：理解是否真正影响生成？为探索这个问题，作者引入了UniSandbox，该框架采用了分拆评测和控制合成数据集的方法，以避免数据泄露并允许细致分析。
### Innovation
UniSandbox框架通过拆分评测和使用受控合成数据集，解决了统一多模态模型中的理解与生成之间的差距。发现理解模块中的明确因果链（CoT）能够有效缩小理解与生成之间的差距，通过自训练方法可以使模型实现隐式推理。此外，因果链对于知识转移也有助于检索新学习的知识，并揭示基于查询的架构固有的潜在因果链特性。
### Conclusion
UniSandbox为设计未来真正连接理解和生成的统一架构和训练策略提供了初步见解，相关代码和数据可在指定链接获取。
## 352. `cs.CL` - LLM解释在生成任务中的反事实仿效性 [PDF](https://arxiv.org/pdf/2505.21740), [HTML](https://arxiv.org/abs/2505.21740)
### Authors
Marvin Limpijankit,Yanda Chen,Melanie Subbiah,Nicholas Deas,Kathleen McKeown
### Background
大语言模型（LLMs）具有不可预测性，即使是轻微的提示修改也会导致输出结果产生意想不到的变化。因此，模型准确解释其行为的能力至关重要，特别是在高风险的应用场景中。一种评估解释的方法是反事实仿效，即解释是否能帮助用户推理模型在相关反事实场景下的输出结果。反事实仿效性研究主要用于二元问题回答任务，研究团队提出了将此方法扩展到生成任务的通用框架，对比案例包括新闻摘要和医疗建议等。
### Innovation
研究提出了将反事实仿效性方法扩展到生成任务的通用框架，并利用新闻摘要和医疗建议作为范例。该研究拓宽了反事实仿效性的应用领域。
### Conclusion
尽管LLM解释有助于用户在新闻摘要情境下更好地预测LLM在反事实情境下的输出，但在医疗建议情境下仍有很大的改进空间。反事实仿效性评估可能更适合技能性任务而非知识性任务。
## 353. `cs.CL` - DesignPref：捕捉视觉设计生成中的个人偏好 [PDF](https://arxiv.org/pdf/2511.20513), [HTML](https://arxiv.org/abs/2511.20513)
### Authors
Yi-Hao Peng,Jeffrey P. Bigham,Jason Wu
### Background
生成模型，例如大语言模型和文本到图像的扩散模型，在创建用户界面（UI）和演示文稿幻灯片等视觉设计方面越来越受欢迎。这些生成模型的微调和基准测试通常依赖于经过人类注释的设计偏好的数据集。但由于视觉设计的高度主观性和个性化特点，不同个体的偏好存在显著差异。
### Innovation
作者引入了DesignPref数据集，包括20位专业设计师对12000个UI设计生成的两两比较的多级偏好标注。研究发现，即使对有经验的专业设计师而言，也存在显著的偏差（二元偏好Krippendorff's alpha = 0.25）。为了应对这一挑战，作者研究了多种个性化策略，尤其是针对设计师具体注释的微调或纳入RAG管道，结果表明个性化模型在预测设计师的个人偏好方面始终优于汇总基准模型，即使使用的示例数量少20倍。
### Conclusion
作者提供了首个用于研究个性化视觉设计评估的数据集，支持未来针对个体设计品味建模的研究。
## 354. `cs.CL` - Gram2Vec: 可解释的文档向量化器 [PDF](https://arxiv.org/pdf/2406.12131), [HTML](https://arxiv.org/abs/2406.12131)
### Authors
Peter Zeng,Hannah Stortz,Eric Sclafani,Alina Shabaeva,Maria Elizabeth Garza,Daniel Greeson Owen Rambow
### Background
本文介绍了一种名为Gram2Vec的语法风格嵌入系统，该系统通过提取文本中存在的语法特征的规范化相对频率将文档嵌入到更高维度的空间中。与神经网络方法相比，Gram2Vec具有基于特征向量生成方式的固有可解释性。
### Innovation
Gram2Vec通过提取文本中语法特征的规范化相对频率来嵌入文档，相较于神经网络方法，它提供了基于特征向量生成方式的固有可解释性。该系统被应用于作者身份验证和AI检测两种场景，展示了Gram2Vec的使用方法。
### Conclusion
通过使用Gram2Vec特征进行作者身份验证，可以解释为何两篇文档是由同一位作者还是不同作者所写。并且Gram2Vec的特征还可以用于训练用于AI检测的分类器，其性能优于在同等特征集上训练的机器学习模型。
## 355. `cs.CL` - MedS$^3$: 向基于自我演化软双重过程监督的医学慢思考方法迈进 [PDF](https://arxiv.org/pdf/2501.12051), [HTML](https://arxiv.org/abs/2501.12051)
### Authors
Shuyang Jiang,Yusheng Liao,Zhe Chen,Ya Zhang,Yanfeng Wang,Yu Wang
### Background
医疗领域的语言模型在实际临床推理应用中面临着诸多关键障碍。主流方法在任务覆盖率、缺乏对中间推理步骤的精细监督以及依赖于专有系统方面仍然存在不足，远远无法提供一个多功能、可信且高效的临床推理语言模型。
### Innovation
本文提出了一种自演化框架MedS3，该框架赋予了小型、可部署模型强大的推理能力。通过使用8,000个集成跨五个医学领域和16个数据集的课程策略筛选出的示例，结合蒙特卡洛树搜索(MCTS)构建可验证的推理轨迹，利用节点值排序进行自我探索的推理轨迹，通过强化微调和偏好学习来引导策略模型。此外，提出了一种软双重过程奖励模型，该模型结合了价值动态信息，有效识别推理错误，即使最终答案正确也是如此。
### Conclusion
MedS3在十一项基准测试中表现出色，比之前的最先进医疗模型高出6.45个准确率点，同时比32B规模的一般推理模型高出8.57个准确率点。补充的实验分析还证明了MedS3实现了稳健且忠实的推理行为。
## 356. `cs.CL` - 何谓推理？多模态推理进展综述（v1） [PDF](https://arxiv.org/pdf/2504.03151), [HTML](https://arxiv.org/abs/2504.03151)
### Authors
Jing Bi,Susan Liang,Xiaofei Zhou,Pinxin Liu,Junjia Guo,Yunlong Tang,Luchuan Song,Chao Huang,Ali Vosoughi,Guangyu Sun,Jinxi He,Jiarui Wu,Shu Yang,Daoan Zhang,Chen Chen,Lianggong Bruce Wen,Zhang Liu,Jiebo Luo,Chenliang Xu
### Background
推理是人类智能的核心，使人们能够跨多种任务进行结构化的问题解决。近年来，大型语言模型（LLMs）在算术、常识和符号领域的能力得到了显著增强，但在将这些能力扩展到多模态环境中的问题仍然存在挑战。在这种环境下，模型需要同时处理视觉和文本输入，这引入了如何处理不同模态之间的冲突信息等复杂性。
### Innovation
本文提供了一个关于文本和多模态LLMs推理技术的简明而深刻的概述，通过全面且最新的比较，明确提出了核心推理挑战和机会，强调了后训练优化和测试时推理的实用方法。通过这种工作，作者为理论框架和实际应用之间的联系提供有价值的见解和指导，并为未来的研究指明了明确的方向。
### Conclusion
本文的研究方法为理论框架和实际应用之间的联系提供宝贵的见解，并为多模态推理的未来研究指明了清晰的方向，例如如何通过更复杂的算法和稳健的评估方法来更好地理解和优化模型的推理过程。
## 357. `cs.CL` - TurnBench-MS：一种评估大型语言模型多轮多步推理的基准 [PDF](https://arxiv.org/pdf/2506.01341), [HTML](https://arxiv.org/abs/2506.01341)
### Authors
Yiran Zhang,Mo Wang,Xiaoyang Li,Kaixuan Ren,Chencheng Zhu,Usman Naseem
### Background
尽管大型语言模型（LLMs）取得了令人印象深刻的进展，现有的基准测试通常集中于单轮或单步任务，未能捕捉到现实世界环境中所需的迭代推理。TurnBench通过引入一个基于“图灵机迷宫游戏”的互动编码破解任务，提供了一个评估多轮、多步推理的新框架，旨在解决这一局限。
### Innovation
TurnBench采用了两模式设计，包括Classic模式测试常规推理能力，以及Nightmare模式增加复杂性要求稳健的推理链。TurnBench还提供了对于中间推理步骤的注解，以支持细粒度分析。评估结果表明，尽管最先进的LLM在Classic模式下取得了84%的准确率，但在Nightmare模式仅达到了18%的准确率，而人类参与者在两种模式中均达到了100%的准确率，突显了TurnBench所提出的挑战。
### Conclusion
通过反馈循环和隐藏任务规则，TurnBench减少了对染分析风险，并提供了一个严格的测试平台，以诊断和推进LLMs的多步、多轮推理能力。
## 358. `cs.CL` - 改进的金融文件问答大型语言模型代理 [PDF](https://arxiv.org/pdf/2506.08726), [HTML](https://arxiv.org/abs/2506.08726)
### Authors
Nelvin Tan,Zian Seng,Liang Zhang,Yu-Ching Shih,Dong Yang,Amol Salunkhe
### Background
大规模语言模型在多项自然语言处理任务中表现出色，但仍存在在包含表格和文本数据的金融文档上的数字问题回答能力不足的问题。已有研究展示了给定注释标签时自我纠正代理（即批评者代理）的有效性。在此基础上，本文研究了在没有注释标签的情况下，传统批评者代理的有效性，并通过实验证明这种代理的表现会恶化。
### Innovation
本文提出了改进的批评者代理和计算器代理，这两种代理优于之前的最先进方法（思考程序），并且更加安全。进一步研究了这两种代理的相互作用及其对性能的影响。
### Conclusion
实验表明，改进的代理在没有注释标签的情况下仍能表现出较好的性能，并且代理之间的交互对其性能有影响。这些改进的代理可以更好地处理金融文档中的数字问题回答任务。
## 359. `cs.CL` - 从生成到检测：用于健康 misinformation 基准测试的多模态多任务数据集 [PDF](https://arxiv.org/pdf/2505.18685), [HTML](https://arxiv.org/abs/2505.18685)
### Authors
Zhihao Zhang,Yiran Zhang,Xiyue Zhou,Liting Huang,Imran Razzak,Preslav Nakov,Usman Naseem
### Background
信息流行病和健康 misinformation 对个人和社会有重大负面影响，增加了对推荐健康措施的犹豫。最近生成人工智能的进步加速了 misinformation 的传播和扩大了其影响力。现有大多数工作集中在社交媒体和事实核查平台的 misinformation 数据集开发上，但存在主题范围有限、包含生成 AI 内容不足以及原始内容可访问性差的问题。
### Innovation
本文提出 MM Health，这是一个大规模的健康领域多模态 misinformation 数据集，包含34,746篇新闻文章，涵盖文本和视觉信息，分为由人类生成的多模态信息（5,776篇）和由多种先进生成 AI 模型生成的多模态信息（28,880篇）。此外，通过三类任务（可靠性检查、原创性检查和精细的 AI 检测）对现有顶级模型进行了基准测试，展示了现有顶级模型难以准确判断信息的可靠性和来源。
### Conclusion
该数据集旨在支持健康领域多模态 misinformation 检测的发展，促进人类和机器生成内容的多模态检测。
## 360. `cs.CL` - SAS: Simulated Attention Score [PDF](https://arxiv.org/pdf/2507.07694), [HTML](https://arxiv.org/abs/2507.07694)
### Authors
Chuanyang Zheng,Jiankai Sun,Yihang Gao,Yuehao Wang,Peihao Wang,Jing Xiong,Liliang Ren,Hao Cheng,Janardhan Kulkarni,Yelong Shen,Atlas Wang,Mac Schwager,Anderson Schneider,Xiaodong Liu,Jianfeng Gao
### Background
注意力机制是Transformer架构的核心组件。各种方法已被开发用于计算注意力分数，包括多头注意力（MHA）、多查询注意力和组查询注意力等。研究表明，随着注意力头的数量的增加，MHA的性能在每头的隐藏尺寸足够大的情况下会有所提升。因此，通过增加注意力头的数量和每头的隐藏尺寸，可以在减少参数成本的同时实现显著的性能提升。
### Innovation
文章提出了一种名为Simulated Attention Score（SAS）的方法，通过将低维度的头部表示投影到高维度空间，模拟更多注意力头和每头更高的特征维度，从而在不增加参数量的情况下提高注意力容量。此外，文章还提出了一种参数高效注意力聚合方法（PEAA），通过调节参数成本来增强特征维度表示的表达能力。
### Conclusion
在各种数据集和任务上进行的综合实验表明，提出的SAS方法非常有效，在不同的注意力变体中实现了显著的性能改进。
## 361. `cs.CL` - Health Sentinel: 一种实时疾病爆发检测的人工智能管道 [PDF](https://arxiv.org/pdf/2506.19548), [HTML](https://arxiv.org/abs/2506.19548)
### Authors
Devesh Pant,Rishi Raj Grandhe,Vipin Samaria,Mukul Paul,Sudhir Kumar,Saransh Khanna,Jatin Agrawal,Jushaan Singh Kalra,Akhil VSSG,Satish V Khalikar,Vipin Garg,Himanshu Chauhan,Pranay Verma,Neha Khandelwal,Soma S Dhavala,Minesh Mathew
### Background
早期检测疾病暴发对确保卫生部门及时干预至关重要。由于传统基于指标的监测存在挑战，因此监测非正式来源如在线媒体变得越来越受欢迎。但由于每天有大量的在线文章发布，人工筛选文章在实践中变得不切实际。
### Innovation
提出了一种名为Health Sentinel的多阶段信息提取流水线，该流水线使用机器学习和非机器学习方法从在线文章中提取关于疾病暴发或不寻常公共卫生事件的事件结构化信息。提取的信息被提供给国家疾病控制中心（NCDC）的媒体扫描和验证单元（MSVC）进行分析、解释并进一步传达给地方机构以进行及时干预。
### Conclusion
自2022年4月至今，Health Sentinel已处理了超过3亿篇新闻文章，并识别出印度超过95,000个独特的健康事件，其中超过3,500个事件被NCDC的公共卫生专家评定为潜在的暴发事件。
## 362. `cs.CL` - Agentar-Scale-SQL：通过协调的测试时缩放提升文本到SQL [PDF](https://arxiv.org/pdf/2509.24403), [HTML](https://arxiv.org/abs/2509.24403)
### Authors
Pengfei Wang,Baolin Sun,Xuemei Dong,Yaxun Dai,Hongwei Yuan,Mengdie Chu,Yingqi Gao,Xiang Qi,Peng Zhang,Ying Yan
### Background
当前最先进的（SOTA）文本到SQL方法在像BIRD这样的具有挑战性的基准上仍然落后于人类专家。现有的在测试时探索缩放的方法缺乏协调策略，忽视了模型的内部推理过程。
### Innovation
我们引入了Agentar-Scale-SQL，这是一种新颖的框架，利用可扩展计算来提高性能。Agentar-Scale-SQL通过三种不同的视角协同实施了一个协调的测试时缩放策略，包括基于RL增强的内在推理的内部缩放，迭代精细调整的序列缩放，以及使用多样性合成和锦标赛选择的并行缩放。
### Conclusion
通过广泛实验，证明了Agentar-Scale-SQL在BIRD基准测试上达到了SOTA性能，测试集的执行准确率达到81.67%，并且在官方排行榜上排名第一，展示了通往人类级性能的有效途径。
## 363. `cs.CL` - LightMem: 轻量级且高效的增强记忆生成 [PDF](https://arxiv.org/pdf/2510.18866), [HTML](https://arxiv.org/abs/2510.18866)
### Authors
Jizhan Fang,Xinle Deng,Haoming Xu,Ziyan Jiang,Yuqi Tang,Ziwen Xu,Shumin Deng,Yunzhi Yao,Mengru Wang,Shuofei Qiao,Huajun Chen,Ningyu Zhang
### Background
尽管大型语言模型（LLMs）具有出色的能力，但在动态和复杂环境中，它们难以有效利用历史交互信息。现有的记忆系统虽然引入了持久的信息存储、检索和利用机制，但往往伴随着显著的时间和计算开销。
### Innovation
为了解决上述问题，本文提出了一种新的记忆系统LightMem，它在性能和效率之间找到了平衡。LightMem受人类记忆的Atkinson-Shiffrin模型启发，将记忆组织成三个互补阶段：首先，通过轻量级压缩迅速过滤掉无关信息，并根据主题对信息进行分组；其次，基于主题的短期记忆进一步巩固这些主题分组，按结构对内容进行组织和总结以便于访问；最后，带睡眠时间更新的长期记忆通过离线过程将巩固过程与在线推理分离。
### Conclusion
在LongMemEval和LoCoMo上，使用GPT和Qwen作为基础模型，LightMem在问答准确性上持续超过了强基线，提高了高达7.7% / 29.3%，减少了总令牌使用量高达38x / 20.9x，并减少了API调用高达30x / 55.5x。纯在线测试时间成本更低，实现了高达106x / 117x令牌减少和159x / 310x更少的API调用。源代码可在以下链接中找到：this https URL.
## 364. `cs.CL` - FlagEval Findings Report: 一段自动可验证文本和视觉问题上大规模推理模型初步评估的报告 [PDF](https://arxiv.org/pdf/2509.17177), [HTML](https://arxiv.org/abs/2509.17177)
### Authors
Bowen Qin,Chen Yue,Fang Yin,Hui Wang,JG Yao,Jiakang Liu,Jing-Shu Zheng,Miguel Hu Chen,Richeng Xuan,Shibei Meng,Shiqi Zhou,Teng Dai,Tong-Shuai Ren,Wei Cui,Xi Yang,Xialin Du,Xiaojing Xu,Xue Sun,Xuejing Li,Yaming Liu,Yesheng Liu,Ying Liu,Yonghua Lin,Yu Zhao,Yunduo Zhang,Yuwen Luo,Zheqi He,Zhiyuan He,Zhongyuan Wang
### Background
当前大型推理模型（LRMs）在处理自动可验证的文本和视觉问题方面存在不确定性，需要进行客观评估。
### Innovation
该研究通过使用FlagEval进行中等规模的、部分无污染的评估，发现了初步结果。同时，提出了一个针对视觉语言模型的新基准测试罗马（ROME），用于测试从视觉线索中推断的能力。
### Conclusion
研究团队发布了一个基准工具包，包括基准测试、评估数据以及其他更新，可以在特定网址找到。
## 365. `cs.CL` - OceanGym: 一种水下代理的基准环境 [PDF](https://arxiv.org/pdf/2509.26536), [HTML](https://arxiv.org/abs/2509.26536)
### Authors
Yida Xue,Mingjun Mao,Xiangyuan Ru,Yuqi Zhu,Baochang Ren,Shuofei Qiao,Mengru Wang,Shumin Deng,Xinyu An,Ningyu Zhang,Ying Chen,Huajun Chen
### Background
水下环境对感知和决策提出了极端挑战，包括低可见度和动态的海洋水流，导致有效代理部署极其困难。现有的基准环境通常针对陆地或空中领域，而不适用于水下场景。
### Innovation
OceanGym 提供了一个综合基准平台，涵盖了八个现实的任务领域，并使用多模态大型语言模型（MLLM）来集成感知、记忆和序列决策机制。该平台旨在推动 AI 在最具挑战性的实际环境之一中的发展。
### Conclusion
OceanGym 通过提供一个高保真的、严格设计的平台，为开发鲁棒的水下代理和将其能力转移到实际水下自主车辆奠定了基础，标志着朝着能够在地球上最后一个未开发前沿区域操作的智能代理发展的重要一步。代码和数据可在以下链接找到：this https URL
## 366. `cs.CL` - EHR-R1：一种增强推理的基础语言模型，用于电子健康记录分析 [PDF](https://arxiv.org/pdf/2510.25628), [HTML](https://arxiv.org/abs/2510.25628)
### Authors
Yusheng Liao,Chaoyi Wu,Junwei Liu,Shuyang Jiang,Pengcheng Qiu,Haowen Wang,Yun Yue,Shuai Zhen,Jian Wang,Qianrui Fan,Jinjie Gu,Ya Zhang,Yanfeng Wang,Yu Wang,Weidi Xie
### Background
电子健康记录（EHRs）包含丰富的但复杂的信息，其自动分析对于临床决策至关重要。尽管大型语言模型（LLMs）在临床工作流程中的进步显著，但在分析EHRs方面的能力仍然有限，原因主要是任务覆盖狭窄和缺乏专门针对EHR的推理能力。
### Innovation
提出了一个名为EHR-Ins的大型全面的EHR推理指令数据集，包括300,000个高质量的推理案例和400万个非推理案例，涉及42项不同的EHR任务。其核心创新是一个基于思维图的方法，能够大规模生成高质量的推理数据。基于此，开发了EHR-R1，这是一种专为EHR分析设计的增强推理大型语言模型，最多具有720亿参数。通过包括领域适应、推理增强和强化学习在内的多阶段训练框架，系统地获取领域知识和多样化的推理能力。
### Conclusion
通过实验，EHR-R1在性能上全面超过了最先进的商业和开源大型语言模型（包括DeepSeek-V3和GPT-4o），在MIMIC-Bench上的性能比GPT-4o高出30多分，在EHRSHOT上的零样本AUROC提高了10%。总体而言，EHR-Ins、EHR-R1和EHR-Bench大大促进了更可靠和临床相关EHR分析的开发。
## 367. `cs.CL` - ConfTuner: 训练大型语言模型以口头表达其信心 [PDF](https://arxiv.org/pdf/2508.18847), [HTML](https://arxiv.org/abs/2508.18847)
### Authors
Yibo Li,Miao Xiong,Jiaying Wu,Bryan Hooi
### Background
大型语言模型（LLMs）在科学研究、法律和医疗保健等高风险领域中的应用日益广泛，准确表达不确定性对于可靠性和信任至关重要。然而，当前的LLMs常常在生成答案时表现出过度自信的问题，即在错误的答案上充满自信，这被称为“过度自信”。现有的方法通常依赖于提示工程或使用启发式生成的不确定性估计进行微调，这些方法的效果有限且缺乏泛化能力。
### Innovation
受经典机器学习模型中适当评分规则的思想启发，我们提出了一种名为ConfTuner的简单高效的微调方法，该方法引入了最少的额外开销，不需要真实信心分数或代理信心估计。ConfTuner依赖于一个新的损失函数，标记化的布里尔得分，我们理论上证明该损失函数是一个适当的评分规则，即“正确激励模型报告其正确性的真正概率”。ConfTuner在各种推理任务中提高了校准，并且能够应用于像GPT-4o这样的黑盒模型。我们的结果进一步表明，更好的校准信心可以在后续处理中带来收益，促进可信的语言模型系统的开发。
### Conclusion
ConfTuner提升了LLMs的校准程度，使模型在各种推理任务中能够更准确地表达其信心，从而在自校正和模型级联中带来潜在的下游改进。该代码可在以下链接获取：this https URL。
## 368. `cs.CL` - LaaJMeter: 一种Laaj评估框架 [PDF](https://arxiv.org/pdf/2508.10161), [HTML](https://arxiv.org/abs/2508.10161)
### Authors
Samuel Ackerman,Gal Amram,Ora Nova Fandina,Eitan Farchi,Shmulik Froimovich,Raviv Gal,Wesam Ibraheem,Avi Ziv
### Background
大型语言模型（LLMs）作为自然语言处理任务中的评判者（LaaJ）越来越受到关注。然而，在专业领域内进行Laaj的元评估（meta-evaluation）存在显著挑战，因为这些领域的标注数据稀缺且专家评估成本高昂。因此，在实际应用中往往使用未经验证的评估指标，使得难以确定哪些指标能有效识别Laaj的质量，以及达到何种水平的评判性能被认为足够。
### Innovation
提出了一种名为LaaJMeter的基于仿真的框架，用于控制Laaj的元评估。LaaJMeter允许工程师生成代表虚拟模型和评判者的合成数据，从而在实际条件下系统性地分析评估指标。这有助于实践者验证Laaj在特定任务上的有效性，测试它们的指标是否能够正确区分高质量和低质量的Laaj，并估计适当的评判性能阈值。
### Conclusion
LaaJMeter为低资源环境下的Laaj评估提供了可扩展和可扩展的解决方案，有助于确保自然语言处理中的可信度和可重复性。
## 369. `cs.CL` - 朝向可靠的演绎推理语言模型 [PDF](https://arxiv.org/pdf/2511.09222), [HTML](https://arxiv.org/abs/2511.09222)
### Authors
Jiarui Liu,Kaustubh Dhole,Yingheng Wang,Haoyang Wen,Sarah Zhang,Haitao Mao,Gaotang Li,Neeraj Varshney,Jingguo Liu,Xiaoman Pan
### Background
演绎推理是一种严格的从给定前提推导结论的过程，不依赖外部知识。本文中将诚实定义为模型仅在结论由前提逻辑蕴含时作答，在其他情况下不作答。当前的语言模型在进行演绎推理时往往不能保持诚实，甚至在输入不充分的情况下会产生未经授权的答案。
### Innovation
本文通过制定一个多步骤任务来研究这一挑战，要求模型要么正确推导结论，要么保持沉默，同时创建两个基于图形结构的数据集，分别针对线性代数和逻辑推理领域，并通过随机扰动半数实例的边引入无法回答的情况。提出了ACNCHOR，一种强化学习方法，通过向抽样中注入真实轨迹来防止过早训练崩溃，从而稳定学习过程并显著提高整体推理性能。
### Conclusion
实验结果显示，该方法稳定了学习过程并显著改善了整体推理性能，强调了训练动态对于使语言模型能够进行诚实的演绎推理的重要性。
## 370. `cs.CL` - AraFinNews: 阿拉伯语金融摘要生成中的领域适应大语言模型 [PDF](https://arxiv.org/pdf/2511.01265), [HTML](https://arxiv.org/abs/2511.01265)
### Authors
Mo El-Haj,Paul Rayson
### Background
目前存在数量相对较少的阿拉伯语金融新闻数据集，大多数研究集中在英语新闻数据集上进行自然语言生成和总结任务。本文提出了AraFinNews，这是迄今为止最全面的公开可用阿拉伯语金融新闻数据集，覆盖了2015年至2025年的十年间，包含212,500个文章标题对，主要用于评估语言理解和生成能力在特定领域内的表现。
### Innovation
AraFinNews填补了阿拉伯语金融新闻数据集的空白，为该领域提供了现实的基准测试环境。利用这一数据集，研究评估了大型语言模型（LLMs）在阿拉伯语金融文本摘要生成上的表现，特别是对基于变压器模型的mT5、AraT5以及领域适应的FinAraT5模型进行了测试，考察了领域预训练如何影响量化信息处理、实体中心信息处理以及专业报告风格的匹配度。
### Conclusion
实验结果表明，领域适应模型生成的摘要更加连贯，尤其是在处理定量和实体相关信息方面表现优异。这些发现强调了在阿拉伯语金融摘要生成中进行领域特定适应的重要性，以提高叙事流畅性。AraFinNews数据集供用于非商业研究免费访问。
## 371. `cs.CL` - 增强小型波斯语医疗语言模型的推理能力可以超越大规模数据训练 [PDF](https://arxiv.org/pdf/2510.20059), [HTML](https://arxiv.org/abs/2510.20059)
### Authors
Mehrdad Ghassabi,Sadra Hakim,Hamidreza Baradaran Kashani,Pedram Rostami
### Background
在医疗问答等专业应用中，增强小型语言模型的推理能力尤为重要，尤其是在如波斯语等少有使用的语言中。已有研究表明，通过特定的技术手段可以提升这类模型的推理能力。
### Innovation
研究采用了一种结合强化学习与AI反馈（RLAIF）和直接偏好优化（DPO）的方法，用于改进通用波斯语语言模型的推理能力。通过将多选医疗问答数据集翻译成波斯语，并使用RLAIF生成了优选和非优选答案对，用以训练DPO。教师和学生模型被提示生成推理路径，构建了一个包含正确和错误推理路径的数据集，该数据集被用于训练基准模型，显著提升了其在波斯语中的医疗推理能力。
### Conclusion
结果表明，在相对较小的数据集上进行推理导向的训练可以实现比大量数据训练更好的效果，模型的表现优于此前仅基于约5700万标记训练的模型gaokerena-V。这证明了针对特定领域和较少语言资源的模型训练方法的有效性和高效性。
## 372. `cs.CL` - MindEval: 在多轮次心理健康支持上的语言模型基准测试 [PDF](https://arxiv.org/pdf/2511.18491), [HTML](https://arxiv.org/abs/2511.18491)
### Authors
José Pombal,Maya D'Eon,Nuno M. Guerreiro,Pedro Henrique Martins,António Farinhas,Ricardo Rei
### Background
人工智能聊天机器人对心理健康支持的需求正在增长，但现有系统存在一些局限性，如讨好行为或过度肯定，以及强化不良信念。创建更好系统的核心障碍是缺乏能够捕捉真实治疗互动复杂性的基准标准。大多数现有基准要么只能通过多项选择题测试临床知识，要么仅评估单个响应。为解决这一问题，我们提出了MindEval框架，这是一个与哲学博士水平的心理咨询师共同设计的系统，用于自动评估语言模型在现实和多轮次的心理健康治疗对话中的表现。
### Innovation
我们提出了MindEval框架，这是一种与哲学博士水平的心理咨询师共同设计的系统，用于自动评估语言模型在现实和多轮次的心理健康治疗对话中的表现。该框架通过患者模拟和自动评估与大规模语言模型（LLM），平衡了防止作弊与可重复性。我们的框架显示出自动评估与人类专家判断之间的强烈相关性。我们评估了12个最先进的大型语言模型，结果显示所有模型在平均4/6的评分下都表现不佳，特别是在不良的AI特定沟通模式方面有明显缺陷。研究结果表明推理能力和模型规模并不能保证更好的性能，系统的性能随对话长度的增加或在支持有严重症状的患者时会下降。
### Conclusion
通过患者的模拟和自动评估，我们的框架展示了高度的可重复性。我们列出了所有代码、提示和人类评估数据，以促进进一步的研究。
## 373. `cs.CL` - LiRA: 多智能体框架用于可靠且可读的文献综述生成 [PDF](https://arxiv.org/pdf/2510.05138), [HTML](https://arxiv.org/abs/2510.05138)
### Authors
Gregory Hok Tjoan Go,Khang Ly,Anders Søgaard,Amin Tabatabaei,Maarten de Rijke,Xinyi Chen
### Background
科学出版物的快速增长使得保持文献综述全面和及时更新变得越来越困难。尽管先前的研究集中在自动化检索和初步筛选方面，但系统性评论的撰写阶段仍然未得到充分探索，尤其是在阅读流畅性和事实准确性方面。鉴于此，本研究提出了一种多智能体协作流程LiRA，它能够模拟人类的文献综述过程，并通过专门的智能体进行内容大纲、子段落撰写、编辑和审查，从而生成连贯且全面的综述文章。
### Innovation
LiRA 提出了一种全新的多智能体协作流程，用于自动化科学文献综合写作。利用专门的智能体进行内容大纲、子段落撰写、编辑和审查，生成连贯且全面的综述文章。它在 SciReviewGen 和 ScienceDirect 数据集上的评测结果显示，相比 AutoSurvey 和 MASS-Survey 等现有基准方法，LiRA 在撰写质量和引文质量上表现出更好性能，并且与人工撰写的综述有类似的相似度。
### Conclusion
我们的研究结果表明，无需领域特定调整的智能体 LLM 工作流也有潜力改善自动化科学写作的可靠性和可用性。
## 374. `cs.CL` - HyperbolicRAG：利用双曲表示增强检索增强生成 [PDF](https://arxiv.org/pdf/2511.18808), [HTML](https://arxiv.org/abs/2511.18808)
### Authors
Linxiao Cao,Ruitao Wang,Jindong Li,Zhipeng Zhou,Menglin Yang
### Background
检索增强生成（RAG）能够使大型语言模型（LLMs）访问外部知识，减轻幻觉现象并提高特定领域的专业知识。基于图的RAG通过引入显式的关系组织来增强结构推理能力，从而在语义相关文本单元之间传递信息。然而，这些方法通常依赖于欧几里得嵌入，虽然它能够捕捉语义相似性，但是缺乏表示层次结构深度的几何观念，这限制了它们在复杂知识图谱中表示抽象关系的能力。为同时捕捉细微语义和全局层次结构，提出了一种融合双曲几何的检索框架HyperbolicRAG。传统RAG和增强图结构的基线方法在多个问答基准测试中的实验结果表明，HyperbolicRAG在多个问答基准测试中表现优于其他基线。
### Innovation
HyperbolicRAG提出了一种深度意识的表示学习者，将节点嵌入共享的庞加莱流形中，使语义相似性与层次包含对齐；引入了无监督对比正则化，以确保不同抽象层次之间的几何一致性；提出了互评分融合机制，结合欧几里得空间和双曲空间中的检索信号，在推理过程中强调跨空间的一致性。
### Conclusion
综合多个问答基准测试的结果，表明HyperbolicRAG优于包括标准RAG和增强图结构的基线方法，进一步验证了将双曲几何融合到基于图的RAG能够有效提升复杂知识结构关联的建模能力，从而提高生成结果的质量和准确性。
## 375. `cs.CL` - CNS-Obsidian：基于科学出版物的神经外科视觉语言模型 [PDF](https://arxiv.org/pdf/2502.19546), [HTML](https://arxiv.org/abs/2502.19546)
### Authors
Anton Alyakin,Jaden Stryker,Daniel Alexander Alber,Jin Vivian Lee,Karl L. Sangwon,Brandon Duderstadt,Akshay Save,David Kurland,Spencer Frome,Shrutika Singh,Jeff Zhang,Eunice Yang,Ki Yun Park,Cordelia Orillac,Aly A. Valliani,Sean Neifert,Albert Liu,Aneek Patel,Christopher Livia,Darryl Lau,Ilya Laufer,Peter A. Rozman,Eveline Teresa Hidalgo,Howard Riina,Rui Feng,Todd Hollon,Yindalon Aphinyanaphongs,John G. Golfinos,Laura Snyder,Eric Leuthardt,Douglas Kondziolka,Eric Karl Oermann
### Background
通用预训练模型（GPTs）展示了令人印象深刻的性能，但它们在未经过整理的互联网数据上的不透明训练为高风险决策（如神经外科手术）带来了关键限制。CNS-Obsidian是一种在经过同行评审的文献上训练的神经外科预训练模型（VLM），其目标是在实际临床环境中展示其相对于GPT-4o的实用价值。
### Innovation
CNS-Obsidian采用了特定领域的方法，经过同行评审的文献作为训练数据，与通用模型不同，它在透明性上提供了重大改进。该研究通过将23,984篇来自神经外科出版物的期刊文章转换为各种格式的训练样本，并在纽约大学朗格尼健康中心进行了盲校随机试验，展示了其在实际临床环境中的诊断辅助效果。
### Conclusion
CNS-Obsidian与GPT-4o在合成问题上的表现相当但在人类生成的问题上则表现较差。尽管CNS-Obsidian更为小型且成本较低，但在特定领域的科学文献上进行训练的模型能够接近先进模型的性能。这种透明框架为科学社区构建专业AI模型提供了基础。
## 376. `cs.CL` - Mixture of Attention Spans: 通过异质滑动窗口长度优化大模型推理效率 [PDF](https://arxiv.org/pdf/2406.14909), [HTML](https://arxiv.org/abs/2406.14909)
### Authors
Tianyu Fu,Haofeng Huang,Xuefei Ning,Genghan Zhang,Boju Chen,Tianqi Wu,Hongyi Wang,Zixiao Huang,Shiyao Li,Shengen Yan,Guohao Dai,Huazhong Yang,Yu Wang
### Background
现有的大规模语言模型（LLMs）在处理长上下文场景时面临内存和传输效率的挑战。传统方法通常采用单一的滑动窗口长度应用于所有关注点和输入大小，但这种方法忽略了LLMs中固有的不同准确性和延迟权衡，无法准确捕捉它们的多样化关注模式。
### Innovation
本文提出了'Mixture of Attention Spans'（MoA）方法，该方法能够自适应地为不同的注意头和层级生成和导航不同长度的滑动窗口及其与输入大小的比例规则。MoA自动调整每个头部的滑动窗口长度配置，从而提高有效上下文长度、减少性能差距并节省计算资源。
### Conclusion
实验表明，MoA能够将有效上下文长度提高3.9倍，同时内存消耗减少1.2-1.4倍，解码速度提升6.6-8.2倍，优于FlashAttention2和vLLM。MoA在三种长期上下文理解基准测试中将最大相对性能下降从9%-36%减少到5%以内。
## 377. `cs.CL` - 计算图灵测试揭示人类与AI语言的系统性差异 [PDF](https://arxiv.org/pdf/2511.04195), [HTML](https://arxiv.org/abs/2511.04195)
### Authors
Nicolò Pagan,Petter Törnberg,Christopher A. Bail,Anikó Hannák,Christopher Barrie
### Background
大语言模型（LLMs）在社会科学中的应用越来越广泛，基于它们能够生成现实且类似人类文本的假设。然而，这一假设目前尚未得到充分测试。现有的验证工作大多依赖于基于人类判断的评价方式，测试人类能否区分AI生成的文本和人类生成的文本，尽管这样的判断是粗略且不稳定的。因此，该领域缺乏评估LLM生成文本的真实性和校准模型到现实数据的有力工具。
### Innovation
本文有两个贡献。首先，我们引入了一个计算图灵测试：一种结合聚合度量（基于BERT可检测性和语义相似度）和可解释的语义特征（语体特征和主题模式）的验证框架，以评估LLM在特定数据集中的语言如何逼近人类语言。其次，我们系统性地比较了九种开放权重LLM在五种校准策略（包括微调、语体提示和上下文检索）下的表现，评估它们再现X（原Twitter）、Bluesky和Reddit上用户的互动能力。研究结果挑战了文献中的核心假设。即使经过校准，LLM输出依然明显与人类文本区分开来，尤其是在情感语调和情感表达方面。经过指令调优的模型的性能低于其基础模型，而增加模型规模也无法提升其拟人化程度。研究结果提供了一个急需的扩展性验证和校准框架——LLM模拟中，并且警告了它们当前在捕捉人类交流方面的局限性。
### Conclusion
这些结果提供了一个急需的扩展性验证和校准框架——LLM模拟中，并且警告了它们当前在捕捉人类交流方面的局限性。优化拟人化往往会付出语义准确性的代价，反过来说也如此。
## 378. `cs.CL` - 语言模型增强文本类别中的范畴的量度 [PDF](https://arxiv.org/pdf/2501.06662), [HTML](https://arxiv.org/abs/2501.06662)
### Authors
Tai-Danae Bradley,Juan Pablo Vigneaux
### Background
本文的目的有两个方面。首先，作者利用语言模型给出的下一个词的概率定义了一个自然语言中的文本类别，该类别在布拉德利、特里拉和弗拉索普洛斯的意义上是单位区间上丰富的。文章还考虑了文本生成的终止条件，并确定当这种丰富本身可以被解释为文本的概率时的具体情况。其次，作者计算了与这些文本相关的广义度量空间的莫比乌斯函数和量度。量度函数是一个文本（提示）的和，它代表每个提示相关的下一个词概率分布的t-对数熵之和，加上模型可能输出的数量。通过对量度函数的导数进行适当评估，可以恢复其中一个熵的总和，从而将量度视为一个分区函数。
### Innovation
文章创造性地引入了利用语言模型生成文本并在数量上进行分析的方法，将布拉德利等人提出的概念应用于自然语言处理中，提出了一个广义度量空间的莫比乌斯函数和量度的计算方法。作者通过分析量度函数的导数，揭示了量度作为分区函数的性质，并且通过勒内茨和舒尔曼的方法将其表示为广义度量空间中拓扑同调的欧拉特征。
### Conclusion
文章证明了使用语言模型增强文本类别中的范畴的量度可以通过量度函数的导数恢复熵的总和，从而将量度视为分区函数，并通过拓扑同调的欧拉特征表示量度函数，为自然语言处理中的文本生成和丰富提供了新的数学工具和视角。
## 379. `cs.CL` - 基于自注意力过滤和MLP存储：单层变换器能够证明获取并提取知识 [PDF](https://arxiv.org/pdf/2508.00901), [HTML](https://arxiv.org/abs/2508.00901)
### Authors
Ruichen Xu,Kexin Chen
### Background
现代大型语言模型（LLMs）在知识密集型任务上表现出色，但在预训练期间知识获取（存储和记忆）以及轻微调整后推理期间的知识提取（检索和回忆）的理论机制方面尚未充分理解。尽管已有研究通过分析训练动力学探讨了这些过程，但仍忽略了构建全面理论必不可少的几个关键组件：多层感知机（MLP）作为知识存储的主要模块；超分布（OOD）适应性，使LLMs能够在预训练后泛化到未见过的场景中；以及下一词预测，这是标准自回归目标，它将知识编码为条件概率。
### Innovation
本文首次引入了一个理论框架，通过研究单一变换器的训练动态来解决上述限制。在一些正则假设下，研究表明：（i）变换器在预训练过程中的训练损失接近最优，这表明有效的知识获取；（ii）给定足够大的微调数据集和适当的数据多重性条件，变换器能够实现对预训练期间获得且在微调中未重新访问的事实知识的低泛化误差，表明知识提取的鲁棒性；（iii）违反这些条件会导致更高的泛化误差，表现为妄想。我们的分析涵盖了完全微调和低秩微调，提供了对实用低秩适应方法有效性的见解。理论结果通过合成数据集和现实世界的PopQA基准测试得到验证，使用了GPT-2和Llama-3.2-1B模型。
### Conclusion
我们通过实验证明了单一层变换器可以在预训练中有效学习并在微调后提取知识，并为其实用的低秩适应方法提供了理论支持，这将有助于建立知识获取和提取的全面理论机制。
## 380. `cs.CL` - 通过语言代理进行多模态数据探索 [PDF](https://arxiv.org/pdf/2412.18428), [HTML](https://arxiv.org/abs/2412.18428)
### Authors
Farhad Nooralahzadeh,Yi Zhang,Jonathan Furst,Kurt Stockinger
### Background
国际企业、组织和医院收集了大量的多模态数据，存储在数据库、文本文档、图像和视频中。虽然在多模态数据探索和自动将自然语言问题转换为数据库查询语言方面已经取得了进展，但如何通过自然语言查询既结构化的数据库数据又未结构化的模式（如文本、图像）的研究挑战仍然没有得到充分探索。
### Innovation
本文提出了M$^2$EX系统，这是一种基于语言代理的多模态数据探索系统。M$^2$EX的核心创新在于：1. 系统受到实际应用场景的启发，允许用户探索多模态信息系统。2. M$^2$EX利用基于大规模语言模型（LLM）的代理型AI框架，将自然语言问题分解为子任务，如文本到SQL生成和图像分析，并高效地组织特定模式的专家。3. 实验结果表明，M$^2$EX在多模态数据集（包括关系型数据、文本和图像）上的表现优于现有的多模态探索系统，在准确性和各种性能指标方面均表现出色，这得益于更好地利用了大规模语言模型的推理能力。
### Conclusion
实验结果证明，我们的M$^2$EX系统在多模态数据集中的表现优于现有的多模态探索系统，其优势体现在准确性和各种性能指标上，包括查询延迟、API成本和规划效率，主要归功于大规模语言模型推理能力的有效利用。
## 381. `cs.CL` - ExDDV：视频中可解释的深度假信息检测的新数据集 [PDF](https://arxiv.org/pdf/2503.14421), [HTML](https://arxiv.org/abs/2503.14421)
### Authors
Vlad Hondru,Eduard Hogea,Darian Onchis,Radu Tudor Ionescu
### Background
由于生成的视频越来越逼真，人类更难识别深度假信息，因此依赖自动的深度假信息检测器。然而，这些检测器也会出现错误，并且其决策不可解释，使人类容易受到基于深度假信息的诈骗和误导。为了解决这一问题，作者引入了ExDDV数据集和基准测试，旨在开发可解释的深度假信息检测模型。
### Innovation
ExDDV是首个用于可解释深度假信息检测的数据集和基准测试，包括手动标注的5400多个真实和深度伪造视频，标注内容包括文本描述和点击标记，用于解释和指出视觉上的伪影。此外，作者还在可见光-语言模型上进行了实验，通过不同的微调和上下文学习策略进行评估，发现文本和点击监督都对于构建强大的可解释模型是必要的。
### Conclusion
我们的新数据集和结果再现代码可帮助开发能够在深度假信息视频中定位和描述观察到的伪影的可解释模型。实验结果表明，文本和点击监督对于构建强大的可解释模型至关重要。
## 382. `cs.CL` - ShortageSim: Simulating Drug Shortages under Information Asymmetry [PDF](https://arxiv.org/pdf/2509.01813), [HTML](https://arxiv.org/abs/2509.01813)
### Authors
Mingxuan Cui,Yilan Jiang,Duo Zhou,Cheng Qian,Yuji Zhang,Qiong Wang
### Background
药物短缺对全球患者护理和医疗服务构成了关键风险，但由于制药供应链中的信息不对称，监管干预的有效性尚未充分理解。
### Innovation
提出了一种名为ShortageSim的仿真框架，以首次评估监管干预措施在信息不对称情况下对市场竞争动态的影响。该框架利用基于大型语言模型（LLM）的代理来模拟制药商和机构买家在监管机构发布的短缺警报下的战略决策。不同于传统博弈论模型假设完全理性和信息透明，ShortageSim模拟了对监管公告的不同解释及其导致的决策。
### Conclusion
实验结果显示，ShortageSim在生产中断案例中将恢复延迟降低了高达84%，并达到了与现实世界轨迹更接近的效果，最初是基于自处理数据集的历史短缺事件。该框架证实了监管警报在应对短缺方面的作用，并为理解多阶段环境中不确定条件下的竞争提供了一种新方法。项目已经开源，提供了2,925个FDA短缺事件的数据集，为未来研究在信息不对称条件下的供应链政策设计和测试提供了新框架。
## 383. `cs.CL` - 从预测到规划：基于策略的世界模型进行协作状态-动作预测 [PDF](https://arxiv.org/pdf/2510.19654), [HTML](https://arxiv.org/abs/2510.19654)
### Authors
Zhida Zhao,Talas Fu,Yifan Wang,Lijun Wang,Huchuan Lu
### Background
尽管世界模型在推动自动驾驶系统方面取得了显著进展，但其潜在能力尚未被充分利用。当前世界模型主要用于世界模拟，而与轨迹规划基本上是脱钩的。虽然最近一些努力试图将世界模型和规划统一在一个框架中，但世界模型为规划提供的协同促进机制仍然需要进一步探索。
### Innovation
本文提出了一个新的驾驶范式——策略世界模型（PWM），它不仅将世界模型和轨迹规划整合在一个统一的架构中，还能通过提出的无动作未来状态预测方案利用学习到的世界知识来支持规划。为了提高视频预测效率，引入了一种动态增强的并行 token 生成机制，该机制配备了上下文引导的 tokenizer 和自适应动态焦点损失。尽管只使用前视摄像头输入，该方法仍能匹配或超越依赖多视角和多模态输入的前沿算法。
### Conclusion
通过协作状态-动作预测，PWM 可模拟类人的预见性感知，从而提供更可靠的规划性能。代码和模型权重将在指定的链接中发布。
## 384. `cs.CL` - RadAgents: 胸部X光解读中的类放射科医生工作流程的多模态代理推理 [PDF](https://arxiv.org/pdf/2509.20490), [HTML](https://arxiv.org/abs/2509.20490)
### Authors
Kai Zhang,Corey D Barrett,Jangwon Kim,Lichao Sun,Tara Taghavi,Krishnaram Kenthapadi
### Background
现有的临床任务解决方案通常难以解决复杂的临床任务，而代理系统通过专业化代理间的协作、工具使用和外部知识库的增强可能提供一种潜在的解决途径。然而，在胸部X光(XR)解读方面，当前方法仍然存在局限性：第一，临床解释往往缺乏可解释性，未能与临床指南保持一致，并且仅反映了工具输出的聚合；第二，多模态证据融合不足，导致仅基于文本的解释缺乏视觉依据；第三，系统很少能够检测和解决跨工具的一致性问题，并且缺乏验证机制。
### Innovation
本文提出了RadAgents，一个结合了临床先验和任务感知多模态推理的多代理框架，将放射科医生的工作流程编入模块化的、可审计的管道中。此外，通过引入地面性和多模态检索增强功能，以验证和解决上下文冲突，提高了输出的可靠性和透明度，并使其更符合临床实践。
### Conclusion
RadAgents通过多代理框架，结合临床先验和任务感知多模态推理，以及放射科医生的工作流程模块化和审计，提供了更强的多模态证据融合和上下文一致性验证，从而提高了胸部X光照的临床解释质量。
## 385. `cs.CL` - AI-Mediated Communication Reshapes Social Structure in Opinion-Diverse Groups [PDF](https://arxiv.org/pdf/2510.21984), [HTML](https://arxiv.org/abs/2510.21984)
### Authors
Faria Huq,Elijah L. Claggett,Hirokazu Shirado
### Background
背景在于群体分隔或凝聚力可以源自微观层面的通讯，AI辅助的信息交流可能会影响这一过程。研究表明，在讨论争议性政治话题时，参与者可以自由改变群体。在实验中，参与者在多轮讨论中参与到多个群体中，部分参与者收到了来自大型语言模型的实时消息建议，这些建议可以个性化到其立场，或者包含其组员的观点。
### Innovation
创新在于通过一项预先注册的线上实验（557名参与者、60个会话），研究发现AI辅助通讯能影响群体组成。实验显示，不同类型的AI辅助信息产生了不同的结果：个性化信息使参与者发送更多消息，展现出更强的立场相似性；而包含群体成员观点的建议则使参与者使用更多接纳性语言，建立了更多异质性联系。
### Conclusion
表明人类与AI共同产生的多种表达过程能够重塑集体组织结构。群体结构的分化和凝聚力取决于AI如何融入用户的互动背景。
## 386. `cs.CL` - 大型语言模型在博弈论实验中跨实验复制和预测人类合作 [PDF](https://arxiv.org/pdf/2511.04500), [HTML](https://arxiv.org/abs/2511.04500)
### Authors
Andrea Cera Palatsi,Samuel Martin-Gutierrez,Ana S. Cardenal,Max Pellert
### Background
大型语言模型（LLMs）正在被广泛应用于决策制定的领域如医疗、教育和法律，同时也被用来模拟人类行为。然而，LLMs 在实际应用中是否准确反映人类的真实决策过程仍然知之甚少。这一方面的差距可能在实际应用中导致负面效果，而无法复制人类行为则使得LLMs在社会模拟中的效果不佳。为了解决这一问题，该研究开发了博弈论实验的数字孪生，并引入了一种系统的提示和探究框架，以机器行为评估为目标，测试了三个开源模型（Llama、Mistral和Qwen）。
### Innovation
研究提出了一个博弈论实验的数字孪生，并引入了一种系统的提示和探究框架，来评估机器行为。研究发现Llama在复制人类合作模式方面表现卓越，捕捉了人类选择理性的偏差，而Qwen则与纳什均衡预测高度一致。此外，研究没有使用基于角色的提示就实现了群体行为的再现实验，简化了模拟过程。
### Conclusion
适当校准的LLMs能够复制人类行为的总体模式，并为未被探索的实验空间提供系统的探索，这为社会和行为科学传统研究方法提供了一种补充途径，能够生成关于人类社会决策的新实证预测。
## 387. `cs.CL` - 掌握要领，进而信赖胜局：渐进探索的自我模仿强化学习 [PDF](https://arxiv.org/pdf/2509.22601), [HTML](https://arxiv.org/abs/2509.22601)
### Authors
Yulei Qin,Xiaoyu Tan,Zhengbao He,Gang Li,Haojia Lin,Zongyi Li,Zihan Xu,Yuchen Shi,Siqi Cai,Renting Rui,Shaofei Cai,Yuzheng Cai,Xuan Zhang,Sheng Ye,Ke Li,Xing Sun
### Background
强化学习（RL）是提升大型语言模型（LLMs）在长期、稀疏奖励任务中策略性工具使用能力的主要方法，但面临探索-利用权衡的基本挑战。现有研究通过策略熵来激发探索，但这种机械的熵最大化易导致RL不稳定性，因为多轮分布会偏移。
### Innovation
本文提出了一种名为SPEAR的方法，该方法采用自我模仿学习（SIL）训练代理型LLMs，并以代理自身经验为指导，逐步平衡探索与利用，避免熵坍缩和失控发散。SPEAR通过增强内生奖励塑造和自我模仿的和谐性，在初始阶段频繁工具交互以加速探索，并在逐步熟悉环境后加强成功策略的应用。
### Conclusion
SPEAR在ALFWorld和WebShop等场景中显著提升了GRPO/GiGPO/Dr.BoT的成功率，分别为16.1%/5.1%/8.6%和20.7%/11.8%/13.9%。在AIME24和AIME25中，SPEAR分别提升了3.8%和6.1%。SPEAR的理论复杂度增加仅10%-25%，实践中的运行时开销可以忽略，展示了SPEAR的即插即用可扩展性。
## 388. `cs.CL` - 探索大型语言模型下量化因子和新闻流表示的协同效应以用于股票回报预测 [PDF](https://arxiv.org/pdf/2510.15691), [HTML](https://arxiv.org/abs/2510.15691)
### Authors
Tian Guo,Emmanuel Hauptmann
### Background
在量化投资中，收益预测支持多种任务，包括股票选择、投资组合优化和风险管理。量化因子，如估值、质量和增长，捕捉了股票的不同特征。非结构化数据，如新闻和会议纪要，由于大型语言模型（LLMs）的近期进展，吸引了越来越多的关注。本文探讨了结合多模态因素和新闻流信息在收益预测和股票选择中的有效方法，通过引入融合学习框架整合LLM生成的因子表示和新闻流表示，并比较了不同架构复杂度的三种方法。
### Innovation
本文提出了一种分拆训练方法，该方法结合单一模态的预测及其融合，以缓解混合模型在训练中的不稳定性。本文还通过实验证明了多模态因子和新闻流信息在股票收益预测和选择中的有效建模方法。
### Conclusion
本文在真实投资领域验证了融合学习框架的有效性，并提供了关于多模态因素和新闻流在股票收益预测和选择中的关键见解。
## 389. `cs.CL` - NLP中的隐写攻击：极低投毒与防御规避 [PDF](https://arxiv.org/pdf/2511.14301), [HTML](https://arxiv.org/abs/2511.14301)
### Authors
Eric Xue,Ruiyi Zhang,Zijun Zhang,Pengtao Xie
### Background
Transformer模型在自然语言处理(NLP)中至关重要，但仍然容易受到通过污染数据引入的后门攻击影响，这种攻击在训练过程中植入隐藏行为。近期研究侧重于设计越来越隐蔽的攻击来测试现有防御，将后门行为与样式化的artifact或token级扰动触发器结合。然而，这种趋势忽略了更难以应对且更具挑战性和现实性的情况：使模型对特定名称或实体的语义触发作出响应，成功的后门可以操纵部署系统中与真实人物或事件相关的输出。目前的研究越来越偏离实际威胁模型，因此引入了SteganoBackdoor，使其隐身技术能够与实际威胁模型对齐。
### Innovation
SteganoBackdoor通过利用自然语言隐写术的无害特性，采用梯度引导的数据优化过程，将语义触发种子转换为隐写载体，嵌入高负荷的后门，保持语义流畅性，并与触发器没有表征上的相似性。在各种实验设置中，SteganoBackdoor实现了超过99%的攻击成功率，所需的数据污染比例降低了一个数量级，同时对抗所有数据级别防御保持不被检测。
### Conclusion
SteganoBackdoor揭示了实际且隐蔽的攻击，提升了当前防御的盲点，强调了对抗性数据防御和实际威胁建模的迫切需要。
## 390. `cs.CL` - 何时思考，何时回看：基于不确定性引导的回看策略 [PDF](https://arxiv.org/pdf/2511.15613), [HTML](https://arxiv.org/abs/2511.15613)
### Authors
Jing Bi,Filippos Bellos,Junjia Guo,Yayuan Li,Chao Huang,Yolo Y. Tang,Luchuan Song,Susan Liang,Zhongfei Mark Zhang,Jason J. Corso,Chenliang Xu
### Background
在大型语言模型（LLMs）和大型视觉语言模型（LVLMs）中，测试时的思考（即生成显式的中间推理链）已被证明可以提升性能，并且最近在LVLMs中也表现出强劲的增长。然而，尽管取得了这些有希望的结果，但还没有系统地分析思考是如何影响视觉推理的。本文提供了一个大规模、控制条件下的LVLMs思考比较，评估了来自InternVL3.5和Qwen3-VL家族的十个变体在MMU-val上的表现，使用了慷慨的标记预算和多遍解码。研究表明，并不是思考得越多越好；较长的链路往往会产生忽略图像的错误轨迹，反而不如标准指令模式下运行的相同模型的表现。
### Innovation
论文提出了一种无训练的解码策略，称为不确定性引导回看，该策略结合了不确定性信号、自适应回看提示和广度搜索。该方法提高了MMU的整体性能，在标准思考较弱的类别中获得最大增益，并优于几个强大的解码基线，从而在固定模型族和标记预算下建立了新的最先进的效果。此外，该解码策略还展示了其泛化能力，在五个额外的基准测试中均获得了一致的改进，包括两个广泛的大规模多模式套件和专注于数学的视觉推理数据集。
### Conclusion
本文通过对比分析LVLMs的思考策略，发现并不是思考得越多越好。基于此，提出了一种新的解码策略——不确定性引导回看，无需训练即可有效提升模型的视觉推理能力，并且在多个基准测试中展示了其优越性和泛化能力，成功超越了多个基准方法，实现了新的性能里程碑。
## 391. `cs.CV` - SG-OIF: 一种用于可靠的视觉数据可靠在线影响框架 [PDF](https://arxiv.org/pdf/2511.19466), [HTML](https://arxiv.org/abs/2511.19466)
### Authors
Penghao Rao,Runmin Jiang,Min Xu
### Background
在深度学习的视觉模型中，准确评估训练数据点对测试预测的影响是关键，对于识别和定位噪声数据至关重要。然而，尽管已经提出了影响函数来归因个体训练样本的无限增重或移除如何影响模型输出，但在深度学习视觉模型中的实现仍然具有挑战性，因为涉及反曲率的计算昂贵，而训练非稳态使得静态近似无效。先前的工作使用迭代求解器和低秩替代来降低成本，但在线计算无法跟上训练动态，且信心校准的缺失使得排名不够稳定，最后错误地识别关键实例。
### Innovation
本文引入了一种新的稳定性引导在线影响框架（SG-OIF），它的创新之处在于将算法稳定性视为实时控制器，具体包括：(i) 通过随机Richardson和预条件Neumann方法保持轻量级锚点IHVP；(ii) 提出模块化曲率后端来调整每个实例的影响评分，利用基于稳定性的残差阈值、异常门控和信心参数。实验结果表明，SG-OIF在噪声标签和非分布检测任务中，在多个不同类型的多个数据集上达到了最先进的性能，而且对于CIFAR-10（20%不对称）和MNIST，我们的方法分别达到了91.1%的前1%预测准确率和99.8%的AUPR分数。
### Conclusion
本框架是一种实用的控制器，用于在线影响估计。
## 392. `cs.CV` - Pistachio: 向合成、平衡且长时视频异常基准迈进 [PDF](https://arxiv.org/pdf/2511.19474), [HTML](https://arxiv.org/abs/2511.19474)
### Authors
Jie Li,Hongyi Cai,Mingkang Dong,Muxin Pu,Shan You,Fei Wang,Tao Huang
### Background
现有的视频异常检测（VAD）基准缺乏现实世界性能评估所需的场景多样性、异常覆盖平衡性和时间复杂性。同时，随着社区对视频异常理解（VAU）的需求增加，它需要更深的语义和因果推理，但由于强烈的手动标注需求，难以进行基准测试。因此，迫切需要一种合成、平衡且长时间的视频异常基准来有效消除互联网收集数据集的偏见和限制。
### Innovation
Pistachio是一个全新的VAD/VAU基准，完全通过受控的生成管道构建，利用了近期视频生成模型的进步，提供对场景、异常类型和时间叙事的精确控制，有效消除了互联网收集数据集的偏见和限制。该基准的流水线结合了场景条件异常分配、多步骤故事情节生成和一种时间上一致的长视频合成策略，可生成连贯的41秒时长视频，显著减少了人为干预。
### Conclusion
广泛的实验表明，Pistachio在规模、多样性和复杂性方面具有优势，揭示了现有方法的新挑战，并鼓励未来对动态和多事件异常理解的研究。
## 393. `cs.CV` - PuzzlePoles：基于PuzzleBoard模式的圆柱形标志符 [PDF](https://arxiv.org/pdf/2511.19448), [HTML](https://arxiv.org/abs/2511.19448)
### Authors
Juri Zach,Peer Stelldinger
### Background
可靠感知环境对于自主系统是至关重要的，常常依赖于鲁棒视觉标志进行校准和定位任务。现有的视觉标志通常对视角和遮挡较为敏感，限制了其应用范围。最近提出的PuzzleBoard校准图案因其独特的组合结构提供了一种改进的方式来增强这些标志的可靠性和准确性。
### Innovation
提出了一种名为PuzzlePole的新类型标志，它是一种圆柱形标志，能够从360°视角可靠地被识别和姿态估计。PuzzlePole通过借鉴PuzzleBoard模式的独特组合结构，提供高精度定位和方向性，同时对遮挡具有鲁棒性。这种设计增加了标志在各种自主系统场景中的灵活性，包括机器人导航、SLAM和物理界面等。
### Conclusion
PuzzlePole展示了在特定视觉检测应用中的潜在优势，由于其独特的设计能够更好地应对环境的多变性，为未来的自主系统提供了新的可能性。
## 394. `cs.CL` - 基于共融性评估指标的参数轻量级谱聚类方法及其扩展 [PDF](https://arxiv.org/pdf/2511.19350), [HTML](https://arxiv.org/abs/2511.19350)
### Authors
Nikita Neveditsin,Pawan Lingras,Vijay Mago
### Background
短文本嵌入聚类是自然语言处理中的基础任务，但由于需要预先指定聚类的数量，因此仍然具有挑战性。现有的算法需要手动指定参数或难以扩展到大规模数据集。
### Innovation
提出了一个可扩展的谱方法，能够直接从拉普拉斯特征谱的结构中估计出聚类的数量，并且通过自适应采样策略使得估计器能够有效地扩展到大数据集而不会牺牲可靠性。此外，提出了一种简单的共融性比例评价指标，用于内在评估聚类质量，该指标具有信息论动机，与外在度量标准如归一化互信息和同质性密切相关。
### Conclusion
实验结果显示使用我们提出的估计器和共融性比例指标的K-Means和HAC算法显著优于其他流行的方法如HDBSCAN、OPTICS和Leiden。这些结果证明了我们谱估计器和共融性比例指标的实用价值。
## 395. `cs.CV` - 个性化文本到图像生成的奖励建模 [PDF](https://arxiv.org/pdf/2511.19458), [HTML](https://arxiv.org/abs/2511.19458)
### Authors
Jeongeun Lee,Ryang Heo,Dongha Lee
### Background
近年来，文本到图像（T2I）模型能够从文本提示生成语义上一致的图像，但如何评估它们与个体用户偏好之间的契合度仍然是一个开放的挑战。传统的评估方法，如通用奖励函数或基于相似性的度量，不能捕捉个人视觉品味的多样性和复杂性。
### Innovation
本文提出了PIGReward，一种个性化奖励模型，能够动态生成用户条件化的评估维度并通过CoT推理解析来评估图像。PIGReward采用自举策略，在有限的参考数据推理中构造丰富的用户上下文，实现个性化评估而无需针对每个用户进行专门训练。PIGReward还提供了个性化的反馈，以驱动特定用户的提示优化，从而改善生成图像与个人意图之间的对齐。此外，引入了PIGBench，一个针对不同用户偏好基准，捕捉共享提示的多种视觉解释。实验证明，PIGReward在准确性和可解释性方面优于现有方法，为个性化T2I评估和优化建立了可扩展的基于推理的基础。
### Conclusion
综上所述，我们的研究指出PIGReward是达到个体对齐T2I生成的一个稳健步骤。
## 396. `cs.CL` - 在LLM代理中桥接符号控制和神经推理：结构化认知环 [PDF](https://arxiv.org/pdf/2511.17673), [HTML](https://arxiv.org/abs/2511.17673)
### Authors
Myung Ho Kim
### Background
大型语言模型代理存在根本性的架构问题：交织的推理和执行、记忆的易变性和不可控的行为序列。现有的框架如ReAct、AutoGPT和记忆增强方法未能有效解决这些问题。因此，需要一种新的架构来解决这些挑战。
### Innovation
作者引入了结构化认知环(SCL)架构，通过明确分离智能体的认知为五个阶段：检索、认知、控制、行动和记忆 (R-CCAM)。SCL的核心是软符号控制，这是一种适应性治理机制，将符号约束应用于概率推理，保持神经灵活性的同时恢复经典符号系统的可解释性和可控性。通过多步骤条件推理任务的经验验证，SCL实现了零策略违规、消除了冗余工具调用，并保持了完整的决策追踪。作者还提出了三个设计原则：模块化分解、适应性符号治理和透明状态管理。
### Conclusion
该工作通过将专家系统原理与现代LLM能力相结合，为可靠、可解释和可治理的AI代理提供了一条实用且理论基础的道路。提供的完全开源实现展示了R-CCAM环结构，同时展示了一个由GPT-4o驱动的实时旅行规划代理。
## 397. `cs.CV` - 任何模态下的跟踪和分割一切 [PDF](https://arxiv.org/pdf/2511.19475), [HTML](https://arxiv.org/abs/2511.19475)
### Authors
Tianlu Zhang,Qiang Zhang,Guiguang Ding,Jungong Han
### Background
跟踪和分割在视频理解中起着至关重要的作用，提供对象在视频序列中的基本位置信息和时间关联。尽管现有方法具有相同的总体目标，但它们往往使用特定的架构或模态特定参数来处理这些任务，这限制了其泛化能力和可扩展性。近年来，一些努力尝试从任何模态输入或多任务推理的角度统一多个跟踪和分割子任务，但这些方法往往忽略了两个关键挑战：不同模态之间的分布差距和任务之间的特征表示差距。这些问题阻碍了有效的跨任务和跨模态知识共享，最终限制了真正通用模型的发展。
### Innovation
为了解决这些限制，我们提出了一种名为SATA的通用跟踪和分割框架，它可以统一多种跟踪和分割子任务并支持任何模态输入。特别地，我们提出了一种解耦的混合专家机制（Decoupled Mixture-of-Expert, DeMoE），将统一的表示学习任务分解为跨模态共享知识和特定信息的建模过程，使模型保持灵活性并增强泛化能力。我们还引入了一个任务感知多对象跟踪（TaMOT）流水线，将所有任务输出统一为具有校准ID信息的一组实例，从而缓解多任务训练中任务特定知识的退化。
### Conclusion
SATA在18个具有挑战性的跟踪和分割基准测试中表现出优越的性能，提供了更多通用视频理解的新视角。
## 398. `cs.CV` - 更少的 tokens，更大的扩展：自适应视觉基底的高效且扩展性良好的表示学习 [PDF](https://arxiv.org/pdf/2511.19515), [HTML](https://arxiv.org/abs/2511.19515)
### Authors
Shawn Young,Xingyu Zeng,Lijian Xu
### Background
本文探讨了模型容量与保持图像语义所需最小视觉 token 数量之间的基本关系。研究受 Minimum Description Length (MDL) 原理启发，重新定义图像 token 为视觉语义空间中的向量，并将图像的固有语义复杂度定义为能够覆盖该空间的最小基础向量集。基于这一视角，提出了轻量级的正交滤波模块，该模块能够自适应地将冗余 token 聚集为一组紧凑的正交基。
### Innovation
本文提出了正交滤波模块，这是一种轻量级的自适应集群方法，可以将冗余 token 转化为紧凑的正交基。实验表明，更大规模的模型只需要较少的 token 即可覆盖视觉语义空间。此外，论文还贡献了一个用于视觉长上下文理解的数据集。
### Conclusion
随着模型规模的扩大，保持图像语义所需的实际 token 数量远少于直观预期的线性增加。正交滤波模块能够高效地控制 token 数量，使模型在保持语义完整性的同时具有更好的扩展性和表达能力。
## 399. `cs.CV` - 解决3D配对和2D正射投影对齐任务的行列式比矩阵方法 [PDF](https://arxiv.org/pdf/2511.19511), [HTML](https://arxiv.org/abs/2511.19511)
### Authors
Andrew J. Hanson,Sonya M. Hanson
### Background
姿态估计是计算机视觉中的一个普遍问题，在广泛应用中起着重要作用。相对旋转3D参考对象可以通过其旋转后的3D版本或其投影到2D平面上的投影来确定。投影可以是透视投影（PnP问题）或正射投影（OnP问题）。本文专注于OnP问题及完整的3D姿态估计任务（EnP问题），解决这两个问题在无噪声情况下的最小二乘系统，并提出了一种基于行列式比矩阵（DRaM）的方法。对于含噪数据情况，可以通过简单的旋转校正方案进行处理。
### Innovation
本文系统地解决了3D和2D正射视角的配对与投影对齐问题，并提出了行列式比矩阵（DRaM）方法以解决无噪声的3D-3D对齐和含噪的3D-2D正射（OnP）任务。同时，将先前使用QR分解和摩尔-彭罗斯伪逆变换的方法置于一个更大且未曾完全认识的上下文中，形成了一个名为DRaM家族的解算器族。此外，本文还展示了DRaM方法在时间上看似显而易见的起源，并表明这些方法可以推广到所有相应的N维欧几里得姿态估计问题。
### Conclusion
本文提出了一种新的DRaM方法，并通过比较DRaM方法及其家族在3D和2D正射姿态估计问题中的表现，再次强调了此方法有助于更好地理解这些类别中的问题。这些方法可以在含噪情况下给出有效的姿态估计结果，为传统几何方法和数值方法融合提供了新的视角。
## 400. `cs.CV` - 无需训练的基于代理人推理的连接点：无监督视觉定位 [PDF](https://arxiv.org/pdf/2511.19516), [HTML](https://arxiv.org/abs/2511.19516)
### Authors
Liqin Luo,Guangyao Chen,Xiawu Zheng,Yongxing Dai,Yixiong Zou,Yonghong Tian
### Background
视觉地基任务是将文本查询与图像中的特定区域联系起来，在视觉语言整合中起着核心作用。现有的方法通常依赖于大量的任务特定注释和微调，这限制了它们在新型或分布外场景中的泛化能力。
### Innovation
我们提出了一种名为GroundingAgent的新颖无代理人特定微调的视觉地基框架，该框架采用结构化的迭代推理机制，整合了预训练的开放词汇对象检测器、多模态大型语言模型（MLLMs）和大型语言模型（LLMs），以渐进地通过联合语义和空间分析精化候选区域。GroundingAgent在广泛使用的基准测试（RefCOCO，RefCOCO+，RefCOCOg）上实现了65.1％的零样本定位准确性，完全无需微调。通过用MLLM生成的描述替换原始查询文本，仅在选择阶段的准确率达到约90％，接近监督性能，突显了LLM推理能力的关键作用。
### Conclusion
GroundingAgent 提供了强大的可解释性，透明地展示了每个推理步骤，并清晰地提供了其决策过程的见解。
## 401. `cs.CV` - 感知分类学：评估和指导视觉-语言模型的层级场景推理 [PDF](https://arxiv.org/pdf/2511.19526), [HTML](https://arxiv.org/abs/2511.19526)
### Authors
Jonathan Lee,Xingrui Wang,Jiawei Peng,Luoxin Ye,Zehan Zheng,Tiezheng Zhang,Tao Wang,Wufei Ma,Siyi Chen,Yu-Cheng Chou,Prakhar Kaushik,Alan Yuille
### Background
当前的视觉-语言基准测试主要关注表面级别的识别或图像-文本对齐，缺乏对更深层次的物理感知和推理能力的综合评估。这导致了在从物体和空间配置中推断任务相关属性（如材质、功能、物理属性等）以支持目标导向推理方面的不足。
### Innovation
提出了一个感知分类学框架，这是一种结构化的场景理解过程，首先识别物体及其空间配置，然后推断任务相关的物理属性。该框架用于构建一个基准测试，其中包含3173个物体的标注，覆盖84个细粒度属性，并构造了一个包含5802张图像的选择题基准，这些问题分为四种类别。该基准展示了在多种类型的感知分类学推理问题上的表现，并提供了上下文推理示例，以改善模型在真实世界和专家设计问题上的表现。
### Conclusion
现有的视觉-语言模型在物体识别任务上表现出色，但在依赖于结构属性的多步骤推理问题上表现较差，尤其是在真实世界和高质量设计的问题上。这些发现突显了结构化的视觉理解在模型中持续存在的差距，以及当前模型对模式匹配的依赖。上下文推理示例有助于提高真实世界和专家设计的问题上的性能，表明了感知分类学引导提示的有效性。
## 402. `cs.CV` - 眨眼超越眼_aspect_ratio：用于驾驶员嗜睡检测和数据增强的稳定眼睑角度度量 [PDF](https://arxiv.org/pdf/2511.19519), [HTML](https://arxiv.org/abs/2511.19519)
### Authors
Mathis Wolter,Julie Stephany Berrio Perez,Mao Shan
### Background
可靠地检测驾驶员嗜睡对于提高道路安全和支持先进驾驶辅助系统（ADAS）至关重要。传统的二元眼球状态估计器或基于二维的指标，如眼裂比（EAR），很容易受到摄像机视角变化的影响，导致不稳定的结果。因此，本文提出了一种新颖且可重复的眼睑角度（ELA）度量，这是一种从3D面部标记中提取的眼睑开放度度量，能够在不同摄像机角度下提供稳定的眼睑运动几何描述。
### Innovation
该研究的创新之处在于提出了一种新颖且可重复的度量标准——眼睑角度（ELA），它能够提供稳定的眼睑运动几何描述，并且不受摄像机视角变化的影响。此外，通过ELA数据生成逼真的合成数据集来扩展训练数据的多样性，同时减轻了收集真实嗜睡数据的安全风险。
### Conclusion
实验结果表明，眼睑角度（ELA）在不同视角变化下的方差低于眼裂比（EAR），并且能够实现准确的眼睑检测。同时，合成数据增强技术扩展了嗜睡识别训练数据的多样性。研究结果强调眼睑角度（ELA）不仅可以作为可靠的生物特征度量，还可以作为一种生成可扩展数据集的强大工具，适用于驾驶员状态监测。
## 403. `cs.CV` - 通过潜在特征从单张图像生成高质量3D对象 [PDF](https://arxiv.org/pdf/2511.19512), [HTML](https://arxiv.org/abs/2511.19512)
### Authors
Huanning Dong,Yinuo Huang,Fan Li,Ping Kuang
### Background
在数字时代，三维资产至关重要。虽然图像到3D的自动生成取得了显著进展，但通常难以同时实现快速、详细的高保真生成。本文提出了一种新颖的方法，即LatentDreamer框架，用于从单张图像生成3D对象。
### Innovation
LatentDreamer的核心是一个预先训练好的变分自编码器，它将3D几何映射到潜在特征，大大降低了3D生成的难度。该框架通过潜在特征逐步生成粗略几何、精细几何和现实纹理的3D对象，生成过程在短时间内即可完成，且生成的3D对象高度保真。
### Conclusion
实验表明，在少量训练下，LatentDreamer的性能与当前方法相当，并且生成的3D对象与输入图像高度保真，整个生成过程通常在70秒内完成。
## 404. `cs.CV` - 多模态LLM在跨域全球光伏评估中的泛化 [PDF](https://arxiv.org/pdf/2511.19537), [HTML](https://arxiv.org/abs/2511.19537)
### Authors
Muhao Guo,Yang Weng
### Background
分布式光伏系统的迅速扩展给电力电网的管理带来了挑战，因为许多安装未被记录。卫星影像能够提供全球覆盖，但传统的计算机视觉模型如CNN和U-Net需要大量标注数据，并且无法在不同区域之间进行泛化。
### Innovation
本文研究了多模态大型语言模型在跨域全局光伏评估中的泛化能力。通过利用结构化提示和微调，模型实现了检测、定位和量化任务的统一集成。使用$triangle F1$度量进行跨区域评估，表明所提出模型在未见过的区域中的性能下降最小，优于传统的计算机视觉和转换器基线。
### Conclusion
研究表明，多模态LLM在领域转换下具有鲁棒性，并且具有在全球光伏映射中实现可扩展、可转移和可解释性的潜力。
## 405. `cs.CV` - 面向高效视觉语言模型：基于信息论的自适应结构压缩 [PDF](https://arxiv.org/pdf/2511.19518), [HTML](https://arxiv.org/abs/2511.19518)
### Authors
Zhaoqi Xu,Yingying Zhang,Jian Li,Jianwei Guo,Qiannan Zhu,Hua Huang
### Background
最近的视觉语言模型(VLMs)在多模态任务上取得了显著的性能，但其不断增长的规模对部署和效率提出了严重挑战。现有的压缩方法通常依赖于启发式的重要性度量或经验性的剪枝规则，缺乏关于信息保留的理论保证。
### Innovation
本文提出了基于信息论的自适应结构压缩框架InfoPrune。InfoPrune基于信息瓶颈原则，将剪枝视为在任务相关信息保留和冗余依赖性排除之间的权衡。通过引入基于熵的有效秩(eRank)并使用Kolmogorov-Smirnov距离来衡量原始结构和压缩结构之间的差异，联合考虑结构稀疏性和信息效率。在此基础上，设计了两种互补方案：基于信息损失目标的训练引导头部剪枝方案，以及通过自适应低秩逼近实现的无训练前馈神经网络压缩方案。
### Conclusion
实验结果表明，InfoPrune实现了高达3.2倍的FLOP减少和1.8倍的加速，同时保持了微乎其微的性能下降。这为高效多模态大型模型的建立奠定了理论基础和实践效果。
## 406. `cs.CV` - Vidi2: 大规模多模态视频理解和创作模型 [PDF](https://arxiv.org/pdf/2511.19529), [HTML](https://arxiv.org/abs/2511.19529)
### Authors
Vidi Team,Celong Liu,Chia-Wen Kuo,Chuang Huang,Dawei Du,Fan Chen,Guang Chen,Haoji Zhang,Haojun Zhao,Lingxi Zhang,Lu Guo,Lusha Li,Longyin Wen,Qihang Fan,Qingyu Chen,Rachel Deng,Sijie Zhu,Stuart Siew,Tong Jin,Weiyan Tao,Wen Zhong,Xiaohui Shen,Xin Gu,Zhenfang Chen,Zuhua Lin
### Background
随着互联网上交流和创意的主要媒介从文字逐渐转向视频，视频生产对于可扩展性和高质量的需求日益增强。基于多模态时间检索（TR）的先进模型（Vidi模型）正在不断发展，以支持下一代视频创作。这些模型在TR方面已达到了最先进水平。Vidi2作为Vidi模型的第二次更新，通过细微的空-时定位（STG）来推进视频理解，并扩展了其在视频问答（Video QA）的能力，实现了综合的多模态推理。
### Innovation
Vidi2模型具有端到端的空-时定位能力，可以理解故事情节或角色，自动切换多个视角，以及智能、组成感知的重编和裁剪。为了在实际应用中全面评估空-时定位的能力，作者引入了一个新的基准VUE-STG，它具有四个关键改进：持续时间长的视频、查询于名词短语、高质量的标注和改进的评估指标。同时，对之前的VUE-TR基准进行了升级，以VUE-TR-V2，达到了更均衡的视频长度分布和更接近用户风格的查询。
### Conclusion
Vidi2在VUE-TR-V2和VUE-STG基准测试中显著优于领先的专有系统，如Gemini 3 Pro（预览版）和GPT-5，在视频问答基准测试中与流行的开源模型相似规模的模型竞争成功。
## 407. `cs.CV` - 大规模研究地图：制图学及其图示演变的数字化考察 [PDF](https://arxiv.org/pdf/2511.19538), [HTML](https://arxiv.org/abs/2511.19538)
### Authors
Remi Petitpierre
### Background
全球众多遗产机构已经数字化超过一百万份地图，自动化技术也使得大规模地识别和提取地图内容成为可能。然而，这些方法并没有深入到制图学的历史中去，也缺乏从文化角度看待地图的认识，即地图作为具有文化和象征意义的系统，反映了政治和知识期望。
### Innovation
本文利用来自38个数字目录的771,561个地图记录和99,715个数字化图像的数据集，引入语义分割技术和对象检测模型，对地理结构进行分析，并研究了地图出版物在全球范围内的时空分布、政治动态、海洋制图、三角贸易和殖民扩张之间的关系。还探索了伏笔和矢量特征的转换及其形成的局部一致系统。
### Conclusion
研究揭示了国家和军事冲突对出版规模的影响，重点提出合法性的角色、大规模参与者以及主要城市在规范和符号文化的传播中的作用。
## 408. `cs.CV` - VideoChat-M1: 通过多代理强化学习进行视频理解的协作策略规划 [PDF](https://arxiv.org/pdf/2511.19524), [HTML](https://arxiv.org/abs/2511.19524)
### Authors
Boyu Chen,Zikang Wang,Zhengrong Yue,Kainan Yan,Chenyun Yu,Yi Huang,Zijun Liu,Yafei Wen,Xiaoxin Chen,Yang Liu,Peng Li,Yali Wang
### Background
利用工具增强的多模态大型语言模型（MLLMs），多代理框架正在推动视频理解方面的发展。然而，大多数的多代理框架采用静态和不可学习的工具调用机制，这限制了在处理时空复杂视频时发现多样线索的能力，对于实现鲁棒的感知和推理具有限制性。
### Innovation
提出了一种新的多代理系统VideoChat-M1，采用了不同于单一或固定策略的协作策略规划（CPP）范式，包括三个关键过程：（1）策略生成：每个代理为用户的查询生成其独特的工具调用策略；（2）策略执行：每个代理依次调用相关工具执行其策略并探索视频内容；（3）策略通信：在策略执行的中间阶段，代理之间交互以更新各自的策略。此外，为CPP范式配备了简洁的多代理强化学习（MARL）方法，团队中的策略代理可以联合优化，以提高VideoChat-M1的性能，不仅指导最终答案的奖励，还指导中间合作过程的反馈。
### Conclusion
广泛的实验表明，VideoChat-M1在八个涵盖四个任务的基准上达到了领先性能。特别是在LongVideoBench上，该方法比SOTA模型Gemini 2.5 pro高3.6%，比GPT-4o高15.6%。
## 409. `cs.CV` - MapRF：通过NeRF引导的弱监督自训练在线高精度地图构建 [PDF](https://arxiv.org/pdf/2511.19527), [HTML](https://arxiv.org/abs/2511.19527)
### Authors
Hongyu Lyu,Thomas Monninger,Julie Stephany Berrio Perez,Mao Shan,Zhenxing Ming,Stewart Worrall
### Background
高精度地图对自动驾驶系统非常有益，能够提供有关道路基础设施的关键信息。现有的在线高精度地图构建方法通常需要昂贵的3D地图注释进行训练，这限制了它们在不同驾驶环境中的通用性和可扩展性。
### Innovation
提出了一种名为MapRF的弱监督框架，能够仅使用2D图像标签来构建3D地图。引入了一种基于地图预测的新型Neural Radiance Fields (NeRF)模块，用于重建视图一致的3D几何和语义。通过迭代使用伪标签来逐步改进地图网络，使其在自训练过程中逐步完善。为了减轻自训练过程中错误累积的影响，还提出了一种地图到射线匹配策略，将地图预测与从2D标签导出的相机射线对齐。
### Conclusion
在Argoverse 2和nuScenes数据集上的广泛实验表明，MapRF在性能上与完全监督的方法相匹敌，达到了基线的约75%，并且仅使用2D标签就超过了其他几个方法。这表明MapRF有可能实现为自动驾驶提供可扩展且成本效益高的在线高精度地图构建。
## 410. `cs.CV` - SkillSight：使用视线进行高效第一人称技能评估 [PDF](https://arxiv.org/pdf/2511.19629), [HTML](https://arxiv.org/abs/2511.19629)
### Authors
Chi Hsuan Wu,Kumar Ashutosh,Kristen Grauman
### Background
本研究关注使用智能眼镜进行技能学习时，基于自我中心视角（第一人称视角）的技能评估具有重大潜力，但现有的技术难以自动化地进行这种评估。研究的目标在于提出一种高效的方法，通过分析第一人称的数据（包括视线数据和自我中心视频），自动评估个体的技能水平。
### Innovation
研究提出了SkillSight框架，这是一种用于从第一人称数据中进行技能评估的新颖方法。它创新地结合了视线和自我中心视频数据来预测技能水平，然后通过简化模型仅使用视线数据进行推理，降低了能耗。此外，通过实验证明了视线数据在不同场景下的重要性，并展示了比现有方法更高效的性能。
### Conclusion
研究证明通过视线数据来进行技能评估是有效的，且能实现高效能耗。SkillSight的教师模型在评估技能时达到了最先进的性能，而其仅基于视线的学生模型在仅有较少73倍能耗的情况下，依然能够保持较高的准确性。这对野外智能技能学习具有重要的指导意义。
## 411. `cs.CV` - 基于多尺度矢量量化变分自编码器的内镜图像合成 [PDF](https://arxiv.org/pdf/2511.19578), [HTML](https://arxiv.org/abs/2511.19578)
### Authors
Dimitrios E. Diamantis,Dimitris K. Iakovidis
### Background
胶囊内镜（WCE）获取大量图像需要手动筛查。深度学习的临床决策支持（CDS）系统可以帮助筛查，但其表现依赖于大而多样化的训练医疗数据集。由于隐私限制和注释成本问题，此类数据的稀缺性阻碍了CDS的发展。生成式机器学习为解决这一限制提供了一种可行的方案。虽然现有的合成数据生成（SDG）方法，如生成对抗网络和变分自动编码器被探索过，但在合成异常发现时经常面临训练稳定性和视觉多样性不足的挑战。
### Innovation
该工作提出了一种新型的向量量化变分自编码器（VAE）的多尺度方法，称为多尺度向量量化变分自编码器（MSVQ-VAE）。与其他基于VAE的WCE图像生成模型不同，MSVQ-VAE能够无缝地将异常引入正常WCE图像中；它支持条件生成合成图像，能够将不同类型的异常引入正常WCE图像中；它通过多种异常类型（如息肉、血管性和炎症性疾病）进行了实验验证，生成的图像用于CDS性能测试，结果表明，使用该方法生成的异常图像训练的CDS分类器与仅使用真实数据训练的分类器具有相似的效果。
### Conclusion
提出的合成方法具有广泛的适用性，可以应用于医学多媒体相关的各种领域。
## 412. `cs.CV` - 使用大型多模态模型导航吉格apixel病理图像 [PDF](https://arxiv.org/pdf/2511.19652), [HTML](https://arxiv.org/abs/2511.19652)
### Authors
Thomas A. Buckley,Kian R. Weihrauch,Katherine Latham,Andrew Z. Zhou,Padmini A. Manrai,Arjun K. Manrai
### Background
尽管通用大型多模态模型在支持临床护理方面广泛应用，但在病理学领域，特别是在处理吉格apixel分辨率的图像时，这些模型在医学图像解释中的表现通常不佳或难以确证。先前的研究通常依赖低分辨率缩略图或随机样本，可能低估了模型的实际表现。
### Innovation
该研究介绍了Gigapixel Image Agent for Navigating Tissue（GIANT）框架，这是第一个使大型多模态模型能够迭代导航全组织切片图像（WSIs），如同病理学家一般。此外，研究者还发布了新的基准数据集MultiPathQA，包含934个WSI级别的问题，涵盖五项临床相关任务，以及128个由专业病理学家撰写的直接滑片解释问题。结果显示，使用GIANT的简单代理系统显著优于基于随机块和缩略图的经典基线模型，并且其性能甚至超过了专门模型。
### Conclusion
研究发现揭示了当前基础模型的优势和局限性，并为病理学中的专家推理提供了未来模型开发的基础。例如，在病理学家撰写的问题上，采用GIANT的GPT-5实现了62.5%的准确性，超过了如TITAN（43.8%）和SlideChat（37.5%）等专门病理模型的表现。
## 413. `cs.CV` - 基于点阵表面估计的无代理高斯点阵变形 [PDF](https://arxiv.org/pdf/2511.19542), [HTML](https://arxiv.org/abs/2511.19542)
### Authors
Jaeyeong Kim,Seungwoo Yoo,Minhyuk Sung
### Background
现有针对高斯点阵（GS）变形的方法通常依赖于诸如笼子或网格之类的变形代理，这导致依赖代理质量且增加了额外的计算开销。这些代理方法在变形时对细节和拓扑信息的保持效果有限。直接将高斯点阵作为点云进行拉普拉斯变形也往往无法有效地捕捉表面信息，原因在于缺乏明确的结构信息。
### Innovation
提出了一种名为SpLap的新颖无代理高斯点阵变形方法，通过构建一种表面感知的点阵图来改进拉普拉斯算子，使变形更可信而同时保留细节和拓扑结构。该方法引入了一种基于点阵结构的邻近关系定义方式，与传统的基于中心距离的方式不同，该方法还引入了高斯核适应技术，以在变形过程中保持表面结构，从而提高变形后的渲染质量。
### Conclusion
实验结果表明，与基于代理和无代理基线方法相比，该方法在50个具有挑战性的三维模型（来自ShapeNet，Objaverse，Sketchfab和NeRF-Synthetic数据集）上显示了更好的性能。已经提供了该方法的代码。
## 414. `cs.CV` - Think First, Assign Next (ThiFAN-VQA): A Two-stage Chain-of-Thought Framework for Post-Disaster Damage Assessment [PDF](https://arxiv.org/pdf/2511.19557), [HTML](https://arxiv.org/abs/2511.19557)
### Authors
Ehsan Karimi,Nhut Le,Maryam Rahnemoonfar
### Background
准确评估自然灾害后的损害对于有效的应急响应和恢复至关重要。基于AI的框架利用无人机收集的大量 airborne图像进行分析，可以快速提供可操作的信息。然而，创建和标注训练模型的数据成本高且耗时，导致数据集规模和多样性有限。此外，现有方法主要依赖于传统的基于分类的框架，并且固定了答案空间，限制了它们提供新信息的能力，需要额外的数据收集或模型重新训练。基于预训练的生成模型和In-Context Learning (ICL)可为灵活和开放回答空间提供可能，但这些模型常常生成错误的信息或产生不特定于领域的通用响应。
### Innovation
本文提出了一种基于视觉问答（VQA）的Two-stage推理框架ThiFAN-VQA，用于灾难场景下的视觉问答。ThiFAN-VQA通过链式思考（CoT）提示和ICL生成结构化的推理轨迹，实现有限监督下的可解释推理。之后，回答选择模块评估生成的响应，选择最一致且上下文相关的答案，从而提高模型表现。通过结合自定义信息检索系统、特定领域的提示和推理引导的响应选择，ThiFAN-VQA弥补了零样本和监督方法之间的差距，实现了灵活性与一致性的结合。
### Conclusion
在受到洪水和飓风影响地区的基于无人机的FloodNet和RescueNet-VQA数据集上的实验表明，ThiFAN-VQA在实际灾后损害评估任务中的准确度、可解释性和适应性方面表现出优越性。
## 415. `cs.CV` - 利用未标注扫描图像的早期中风诊断NCCT图像分割：一种半监督GAN方法 [PDF](https://arxiv.org/pdf/2511.19576), [HTML](https://arxiv.org/abs/2511.19576)
### Authors
Maria Thoma,Michalis A. Savelonas,Dimitris K. Iakovidis
### Background
缺血性中风是一种时间敏感的医疗紧急情况，快速诊断对于改善患者预后至关重要。非对比计算机断层扫描（NCCT）是前线成像工具，但在早期超急性阶段往往无法揭示细微的缺血性变化，这可能导致重要干预措施的延误。
### Innovation
提出了一个半监督分割方法，使用生成对抗网络（GANs）准确绘制早期缺血性中风区域。该方法利用对抗框架有效地从有限注释的NCCT扫描中学习，并同时利用更大数量的未注释扫描。通过使用Dice损失、交叉熵损失、特征匹配损失和自我培训损失，模型学会了识别并勾勒出即使微弱或体积小的早期梗死灶。
### Conclusion
在公开的急性缺血性中风数据集（AISD）上的实验表明，所提出的方法能够提高诊断能力，减轻手动注释负担，并支持更高效的中风临床决策。
## 416. `cs.CV` - HunyuanOCR技术报告 [PDF](https://arxiv.org/pdf/2511.19575), [HTML](https://arxiv.org/abs/2511.19575)
### Authors
Hunyuan Vision Team,Pengyuan Lyu,Xingyu Wan,Gengluo Li,Shangpin Peng,Weinong Wang,Liang Wu,Huawen Shen,Yu Zhou,Canhui Tang,Qi Yang,Qiming Peng,Bin Luo,Hower Yang,Houwen Peng,Hongming Yang,Senhao Xie,Binghong Wu,Mana Yang,Sergey Wang,Raccoon Liu,Dick Zhu,Jie Jiang,Linus,Han Hu,Chengquan Zhang
### Background
本文介绍了HunyuanOCR，这是一个商业级、开源且轻量级（参数量为1B）的视觉-语言模型（VLM），专门用于OCR任务。该模型包括原生视觉变换器（ViT）和轻量级LLM的组合。
### Innovation
1. 统一了灵活性和效率：HunyuanOCR实现了对核心能力（包括文本定位、解析、信息提取、视觉问答和翻译）的全面支持，这避免了既狭窄又不高效的“OCR专家模型”以及通常笨重的“通用VLM”模型。2. 简洁的一站式架构：采用纯端到端的架构，去除了预处理模块（如布局分析）依赖，从根本上解决了传统流水线中常见的错误传递问题，简化了系统部署。3. 数据驱动和强化学习策略：HunyuanOCR证实了高质量数据的重要性，并首次展示了强化学习策略在OCR任务中显著提升性能的作用。
### Conclusion
HunyuanOCR在ICDAR 2025 DIMT挑战中的小型模型赛道上获得了第一名，并且在OCRBench基准测试中，作为参数少于3B的VLM，取得了最优表现。该模型的高性能部署方案基于vLLM，并且在生产效率上处于领先位置，旨在推动前沿研究并为工业应用提供坚实基础。
## 417. `cs.CV` - INTERLACE: 交替层修剪与大型视觉-语言模型的有效适应 [PDF](https://arxiv.org/pdf/2511.19676), [HTML](https://arxiv.org/abs/2511.19676)
### Authors
Parsa Madinei,Ryan Solgi,Ziqi Wen,Jonathan Skaza,Miguel Eckstein,Ramtin Pedarsani
### Background
现有的层修剪方法在应用于非常深的大规模视觉-语言模型（VLMs）时会显著降低性能。
### Innovation
_INTERLACE框架通过分析成组的三个连续层来识别局部冗余，修剪最冗余的前两层，对剩余层进行细调以补偿丢失的容量，同时冻结第三层作为细调期间的稳定锚点。这种方法在修剪后能够快速收敛，仅使用少量数据就能实现高效的适应。
### Conclusion
通过在FineVision数据集上对不到1%的数据集的子集进行一次细调，INTERLACE在修剪掉25%的网络后取得了88.9%的平均性能保留率，并达到了当前最佳性能（SOTA）。
## 418. `cs.CV` - 基于视觉-语言基础模型的快速MRI图像重建：语义指导下的图像重建 [PDF](https://arxiv.org/pdf/2511.19641), [HTML](https://arxiv.org/abs/2511.19641)
### Authors
Ruimin Feng,Xingxin He,Ronald Mercer,Zachary Stewart,Fang Liu
### Background
该研究旨在探讨视觉-语言基础模型能否通过提供超越传统先验的高层次上下文信息来增强undersampled MRI重建，以改善图像重建质量，尤其是在保持数据保真度的情况下实现更精细的解剖结构和更高的感知质量。
### Innovation
研究提出了一种基于语义分布的重建框架，利用预训练的视觉-语言基础模型将重建图像和辅助信息编码为高层次的语义特征，并通过对比目标对重建表示进行校准，以确保与高层次的感知线索保持一致。该方法能够与各种深度学习重建方法兼容，并灵活地整合多模态的语义先验信息，展示了语义先验在图像重建中的重要作用。
### Conclusion
研究结果表明，基于图像和图像-语言信息的语义先验能够有效提高undersampled MRI重建的效果，并且视觉-语言基础模型通过语义空间优化能够增强图像重建的效率和质量。
## 419. `cs.CV` - 使用具有高度感知动态切片的深度学习进行UAV海上小型目标检测 [PDF](https://arxiv.org/pdf/2511.19728), [HTML](https://arxiv.org/abs/2511.19728)
### Authors
Sakib Ahmed,Oscar Pizarro
### Background
无人驾驶航空器（UAV）在海上搜救（SAR）任务中至关重要，因为它们能够监控广阔的海域。然而，由于高空小物体与背景像素比低，小物体在高空难以检测。海上无人机（SeaDronesSee数据集中的）背景复杂，小物体不易被发现。
### Innovation
本文提出了一种高度感知的动态切片方法，该方法根据高度动态调整并适应性细分图像，以增强小目标的检测。通过结合高度依赖的缩放与自适应切片因子，该方法减少了不必要的计算量，同时保持了检测性能。
### Conclusion
该方法在SeaDronesSee数据集上使用YOLOv5和SAHI框架进行测试，相较于基准方法，小型物体的均值精度提升38%；并且相较于静态切片，推理速度提高了两倍以上。这种方法在不同条件下能实现更高效、更准确的UAV基于SAR操作。
## 420. `cs.CV` - CountXplain: Prototype-Based 密度图估计实现可解释的细胞计数 [PDF](https://arxiv.org/pdf/2511.19686), [HTML](https://arxiv.org/abs/2511.19686)
### Authors
Abdurahman Ali Mohammed,Wallapak Tavanapong,Catherine Fonder,Donald S. Sakaguchi
### Background
生物医学成像中的细胞计数对于各种临床应用至关重要，然而，该领域的深度学习模型的可解释性仍然是一个重要挑战。现有的方法在实现高效细胞计数的同时，往往牺牲了模型的可解释性。
### Innovation
提出了一种基于原型的方法，通过密度图估计实现可解释的细胞计数。该方法将一个原型层集成到密度估计网络中，使模型能够学习细胞和背景伪影的代表视觉模式。通过生物学家的问卷调查验证了这些原型的有效性，并通过强调输入图像中与每个原型最相似的区域提供了解释，从而增强了模型的可解释性。实验结果表明，该方法在不牺牲计数效果的情况下实现了可解释性。
### Conclusion
这项工作为研究人员和临床医生提供了一个透明且可靠的细胞计数工具，有可能增加对深度学习在关键生物医学应用中的信任和采纳。
## 421. `cs.CV` - CodeV: 使用代码进行以工具感知策略优化实现忠实视觉推理 [PDF](https://arxiv.org/pdf/2511.19661), [HTML](https://arxiv.org/abs/2511.19661)
### Authors
Xinhai Hou,Shaoyuan Xu,Manan Biyani,Mayan Li,Jia Liu,Todd C. Hollon,Bryan Wang
### Background
现有的视觉-语言模型越来越多地通过调用图像操作来‘思考带有图像’，以提高最终答案的准确性。然而，研究表明，这些高准确度往往掩盖了一些不可信的视觉推理情况，模型可能在无关的区域调用工具或者完全忽略工具的输出，但仍能猜出正确答案。以上背景说明了当前视觉代理在实现高准确度的同时存在不可信的工具使用行为的问题。
### Innovation
该研究提出了一个新协议来评估中间视觉工具输出的忠实性，并引入了CodeV，一种使用工具感知策略优化（TAPO）训练的基于代码的视觉代理。TAPO是一个过程级的强化学习框架，通过在视觉工具输入和输出上定义密集奖励，而不是在思考链的代词上定义，使得监督更容易验证且不易于受到奖励欺诈的影响。CodeV将视觉工具表示为可执行的Python代码，并通过步骤奖励鼓励必要且证据一致的工具使用。实验结果表明，在视觉搜索任务中，CodeV不仅实现了竞争或更好的准确性，还显著提高了有效的工具使用率。此外，研究还表明，对中间工具行为进行明确监督对于构建可信的、有代理性的视觉推理系统至关重要。
### Conclusion
CodeV使用代码实现视觉代理，在工具感知策略优化下，不仅提高了视觉推理的准确性，还显著增强了工具使用的行为忠实度。此外，在其他多模态推理和数学基准测试上，CodeV也表现出了强大的性能，进一步证实了对中间工具行为监督的重要性。
## 422. `cs.CV` - OncoVision: 通过注意力驱动的多模态AI实现乳房X光摄影与临床数据的整合以增强乳腺癌诊断 [PDF](https://arxiv.org/pdf/2511.19667), [HTML](https://arxiv.org/abs/2511.19667)
### Authors
Istiak Ahmed,Galib Ahmed,K. Shahriar Sanjid,Md. Tanzim Hossain,Md. Nishan Khan,Md. Misbah Khan,Md. Arifur Rahman,Sheikh Anisul Haque,Sharmin Akhtar Rupa,Mohammed Mejbahuddin Mia,Mahmud Hasan Mostofa Kamal,Md. Mostafa Kamal Sarker,M. Monir Uddin
### Background
OncoVision是一个结合了乳房X光摄影图像和临床数据的多模态人工智能管道，用于更好地诊断乳腺癌。通过使用注意力机制为基础的编码器-解码器架构，它可以准确地分割四个ROI：肿块、钙化、腋窝发现、乳房组织，并且能够精确地预测十个结构化的临床特征：肿块形态、钙化类型、乳腺密度分类和BI-RADS类别。
### Innovation
为了结合影像学和临床洞察，我们开发了两种后期融合策略。通过利用互补的多模态数据，后期融合策略提高了诊断精度并减少了观察者间的一致性差异。作为安全的用户友好型web应用程序，OncoVision生成了具有双重信心评分和注意力加权可视化结果的结构化报告，为实时诊断提供了支持，提高了医生的信任感并促进了医学教育的进行。它易于集成到临床环境中，在包括南亚农村在内的世界未受服务地区提供了筛查服务。
### Conclusion
结合精确分割与临床直觉，OncoVision设定了AI辅助乳房X光摄影的标准。它提供了一种可扩展且公平的解决方案，旨在更早地检测乳腺癌并通过及时干预来提高治疗效果。
## 423. `cs.CV` - 通过最小切片运输计划实现高效可传输最优运输 [PDF](https://arxiv.org/pdf/2511.19741), [HTML](https://arxiv.org/abs/2511.19741)
### Authors
Xinran Liu,Elaheh Akbari,Rocio Diaz Martin,Navid NaderiAlizadeh,Soheil Kolouri
### Background
OT提供了在计算机视觉中解决匹配和对齐问题的强大框架，包括形状分析、图像生成和多模态任务。然而，OT的计算成本限制了其扩展性。最近的研究通过利用一维OT问题的闭形式解来减少计算成本，提出了一种基于切片的运输计划方法。尽管这些方法高效，但它们没有解决一个关键问题：在数据分布变化的情况下，学习到的最优切片能否适用于新分布对。这一问题在数据持续进化或需要频繁计算OT的情况下尤为重要。
### Innovation
本文研究了最小切片运输计划（min-STP）框架，并探讨了优化切片的可传输性。通过理论分析，证明了在数据微小变化时优化的切片保持稳定，可实现相关任务间的高效传输。此外，本文还提出了一种最小切片运输计划的批量处理形式，提供了其准确性的统计保证。
### Conclusion
实验结果表明，可传输的min-STP在单次匹配性能上取得了出色的表现，并简化了点云对齐和基于流的生成模型的训练流程。
## 424. `cs.CV` - 通过结构重新参数化重新思考视觉变压器的深度 [PDF](https://arxiv.org/pdf/2511.19718), [HTML](https://arxiv.org/abs/2511.19718)
### Authors
Chengwei Zhou,Vipin Chaudhary,Gourav Datta
### Background
视觉变换器（Vision Transformers）在实际应用中的计算开销主要源于其深层的架构。现有的加速策略主要集中在算法层面的优化，如令牌剪枝和注意力加速。这引发了一个尚未充分探索的问题：在保持相当的表示能力的同时，我们能否减少堆叠的变换器层的数量？
### Innovation
本文提出了一种基于分支的结构重新参数化技术，这种技术在训练阶段执行。该方法利用Transformer块中的并行分支，并能够在部署推理时将这些分支系统地合并为简洁的一元路径模型。合并机制是通过逐渐合并非线性组件入口处的分支实现的，从而能够对前馈网络（FFN）和多头自注意力（MHSA）模块进行精确的数学重新参数化，而不会在测试时引入近似误差。当应用于ViT-Tiny时，该框架成功将原始的12层架构减少到6层、4层或最少3层，同时在ImageNet-1K上的分类精度保持不变。结果，这些压缩模型在移动CPU平台上实现了高达37%的推理速度提升。
### Conclusion
本研究的发现表明，传统的倾向于使用极其深层的变换器堆栈的智慧可能过于保守，指出了构建高效视觉变换器的新机会。
## 425. `cs.CV` - 利用PathFMTools在基模型下对表皮鳞状细胞癌进行组织学分级 [PDF](https://arxiv.org/pdf/2511.19751), [HTML](https://arxiv.org/abs/2511.19751)
### Authors
Abdul Rahman Diab,Emily E. Karn,Renchin Wu,Emily S. Ruiz,William Lotter
### Background
尽管计算病理学基础模型具有前景，但要将它们适应特定的临床任务仍面临挑战。具体而言，WSI处理的复杂性、学习特征的不透明性以及潜在适应策略的广泛范围等问题使得这一过程困难重重。
### Innovation
我们引入了PathFMTools，一个轻量级且可扩展的Python包，它能够高效地执行、分析和可视化病理基础模型。PathFMTools被用来与两种先进的视觉-语言基础模型（CONCH和MUSK）对接并评估它们在表皮鳞状细胞癌（cSCC）组织学分级任务中的表现。
### Conclusion
通过使用PathFMTools对440张cSCC H&E WSI进行基准测试，我们验证了使用基础模型嵌入训练小专家模型的潜力，并展示了不同预测方法之间的权衡。这些结果强化了病理基础模型在临床应用中的前景，而PathFMTools则使分析和验证这一模型变得更为高效。
## 426. `cs.CV` - 一种用于3D混凝土缺陷分割的高效特征，以取代法线向量 [PDF](https://arxiv.org/pdf/2511.19760), [HTML](https://arxiv.org/abs/2511.19760)
### Authors
Linxin Hua(1),Jianghua Deng(2),Ye Lu(1) ((1) Department of Civil and Environmental Engineering, Monash University, Melbourne, Australia, (2) School of Civil Engineering and Architecture, Changzhou Institute of Technology, Changzhou, China)
### Background
基于图像的方法对背景噪声敏感，而点云重建损坏的方法虽有效，但处理大量三维数据时应用受限。
### Innovation
提出了一种名为相对角度的新特征，它作为点的法线向量与其父点云平均法线向量之间的角度。这种一维特征提供了与法线向量同等的方向信息，适用于混凝土表面缺陷特征。通过熵特征评估，研究展示了相对角度的能力，即在无损部分过滤冗余信息的同时保留受损部分的有效信息。使用PointNet++模型进行训练和测试，基于相对角度的模型在性能上与基于法线向量的模型相当，但实现了27.6%的存储减少和83%的输入通道压缩。
### Conclusion
相对角度特征具有在资源受限的硬件上实现大规模执行的潜力，无需修改模型的架构。
## 427. `cs.CV` - RADSeg：使用聚类模型实现高效参数和计算量开放词汇语义分割 [PDF](https://arxiv.org/pdf/2511.19704), [HTML](https://arxiv.org/abs/2511.19704)
### Authors
Omar Alama,Darshil Jariwala,Avigyan Bhattacharya,Seungchan Kim,Wenshan Wang,Sebastian Scherer
### Background
开放词汇语义分割（OVSS）是许多需要泛化语义理解的视觉和机器人任务的基础。现有方法要么依赖有限的分割训练数据，限制了泛化能力，要么采用零样本启发式方法应用于视觉语言模型（如CLIP），最具有竞争力的方法则通过结合多种模型来提高性能，但代价是高计算和内存消耗。
### Innovation
本工作利用被忽视的聚类视觉基础模型RADIO，同时在三个关键轴上改善了零样本OVSS：mIoU、延迟和参数效率。通过引入自我相关递归注意、自我相关全局聚合和计算高效的掩码精炼方法，RADSeg在基ViT类别上实现了6-30%mIoU的提升，同时速度提高了3.95倍，参数减少了2.5倍。令人惊讶的是，RADSeg-base（105M）在mIoU方面优于之前的大型视觉模型组合（850-1350M），同时具有更低的计算和内存成本。
### Conclusion
RADSeg通过利用agglomerative vision基础模型RADIO，在零样本开放式词汇语义分割任务中实现了参数和计算成本的显著优化，同时在性能上取得了突破。
## 428. `cs.CV` - IndEgo: A Dataset of Industrial Scenarios and Collaborative Work for Egocentric Assistants [PDF](https://arxiv.org/pdf/2511.19684), [HTML](https://arxiv.org/abs/2511.19684)
### Authors
Vivek Chavan,Yasmina Imgrund,Tung Dao,Sanwantri Bai,Bosong Wang,Ze Lu,Oliver Heimann,Jörg Krüger
### Background
当前工业场景中的多数研究集中在机器人和自动化系统上，而忽视了人类工人的认知和身体劳动。新兴的基于视觉系统的辅助机器人依赖于大规模的多模态数据训练，但当前工业数据集大多以第一人称（egocentric）视角或第三人称（exocentric）视角为主，缺乏全面的工业任务（包括装配、物流、检验和修理等）数据集。因此，本文提出了IndEgo数据集，旨在填补这些空白。
### Innovation
IndEgo是一个涵盖了工业场景中的第一人称（egocentric）和第三人称（exocentric）视角的数据集，包含3,460个第一人称录制（约197小时）和1,092个第三人称录制（约97小时）。重点记录了协作工作场景，其中记录了两名工人共同进行认知和身体强度较大的任务。数据集包含丰富的多模态信息，如眼球追踪、说话、声音、动作等，并提供了详细注释（动作、摘要、错误标注、口头叙述）、元数据、加工输出（眼球追踪、手势姿态、半密集点云）和基于任务理解、错误检测和基于推理的问题回答基准数据。实验表明，基准模型在错误检测、问题回答和协作任务理解上遇到挑战。
### Conclusion
IndEgo数据集提供了一个全面的工业场景数据集，用于训练和评估第一人称辅助机器人。它提供了详细的多模态标注和基准测试，证明了对最先进的多模态模型的挑战，并为多模态AI在工业环境中的应用开辟了新途径。
## 429. `cs.CV` - 什么是你看到的通常就是你得到的：在避免昂贵模态的情况下多模态原型网络 [PDF](https://arxiv.org/pdf/2511.19752), [HTML](https://arxiv.org/abs/2511.19752)
### Authors
Muchang Bahng,Charlie Berens,Jon Donnelly,Eric Chen,Chaofan Chen,Cynthia Rudin
### Background
物种检测对于监测生态系统的健康状况和识别入侵物种至关重要，对于指导保护工作具有重要作用。多模态神经网络被广泛用于识别物种从而自动执行该任务，但存在两大缺点：其一，黑盒特性导致难以解释其决策过程；其二，收集遗传数据通常成本高昂且需要进行侵入性手术，迫使研究人员捕捉或杀死目标样本。因此，该研究通过扩展原型网络方法，使模型在成本意识的多模态环境中运作，解决了上述问题。
### Innovation
本研究通过将原型网络（ProtoPNets）扩展到多模态和成本意识设置中，解决了上述问题。研究中引入了一种方法，通过给予每个模态相关权重来合并原型，从而确定每种预测对各模态的依赖程度。此外，还提出了一些方法，用于识别不需要昂贵的遗传信息即可做出自信预测的情况。研究表明，该方法可以在进行细微区分时智能地分配昂贵的遗传数据，同时利用丰富图像数据进行清晰的视觉分类，并且达到了与始终使用两种模态的模型相当的准确率。
### Conclusion
本研究证明了可以在避免昂贵遗传信息的情况下，通过多模态原型网络进行物种识别，这不仅提高了模型的解释性，还降低了研究成本，提高了数据的利用效率，并达到了不亚于传统多模态模型的准确性。
## 430. `cs.CV` - Vision—Language Enhanced Foundation Model for Semi-supervised Medical Image Segmentation [PDF](https://arxiv.org/pdf/2511.19759), [HTML](https://arxiv.org/abs/2511.19759)
### Authors
Jiaqi Guo,Mingzhen Li,Hanyu Su,Santiago López,Lexiaozi Fan,Daniel Kim,Aggelos Katsaggelos
### Background
Semi-supervised学习（SSL）在医学图像分割中日益流行，它通过减少对大量专家注释的依赖来提高效率。同时，视觉-语言模型（VLMs）在多个视觉领域展示了出色的泛化能力和少量几次学习能力。该研究结合了这些技术，旨在提高医学图像分割的效率和准确性。
### Innovation
提出了Vision-Language Enhanced Semi-supervised Segmentation Assistant（VESSA），这是一种结合了基础视觉-语义理解的SSL框架。VESSA包括两个阶段：第一阶段，VESSA作为参考导向的分割助手被训练，利用包含黄金标准示例的模板库，模拟从有限标记数据中学习。第二阶段，VESSA被集成到最先进的SSL框架中，能够动态与学生模型互动，生成高质量的伪标签和强指导。
### Conclusion
广泛的实验结果显示，VESSA增强的SSL大幅提升了分割准确率，在极少量标注条件下超越了最新的基准模型。
## 431. `cs.CV` - 一种注意力，一种尺度：用于混合分辨率扩散变换器的对齐旋转位置嵌入 [PDF](https://arxiv.org/pdf/2511.19778), [HTML](https://arxiv.org/abs/2511.19778)
### Authors
Haoyu Wu,Jingyi Xu,Qiaomu Miao,Dimitris Samaras,Hieu Le
### Background
在使用旋转位置嵌入（RoPE）进行混合分辨率去噪的扩散变换器中，当不同空间网格的标记混合时，注意力机制会发生崩溃，这表明这种问题是有结构的。线性坐标重映射迫使单个注意力头在不兼容的采样率下比较RoPE相位，从而引发相位混叠，导致评分景观不稳定。预训练的DiTs尤其脆弱，许多注意力头表现出极其尖锐的、周期性的相位选择性，因此即使是细微的跨率不一致性也会可靠地导致模糊、伪影或完全崩溃。
### Innovation
我们的主要贡献是跨分辨率对齐相位注意力（CRPA），这是一个无需训练的即插即用修复方法，可以在根本上消除这一失败。CRPA仅修改每次注意力调用中的RoPE索引映射：所有Q/K位置都在查询的步长上表达，从而使相等的物理距离始终产生相同的相位增量。这恢复了DiTs依赖的精确相位模式。CRPA与预训练的DiTs完全兼容，均匀稳定所有注意力头和层。我们证明，CRPA能够实现高质量和高效的混合分辨率生成，优于此前的最先进的方法。
### Conclusion
CRPA使高保真和有效的混合分辨率生成成为可能，在图像和视频生成方面超越了以前的最先进的方法。
## 432. `cs.CV` - CropVLM：学习聚焦以增强细粒度视觉语言感知 [PDF](https://arxiv.org/pdf/2511.19820), [HTML](https://arxiv.org/abs/2511.19820)
### Authors
Miguel Carvalho,Helder Dias,Bruno Martins
### Background
视觉-语言模型（VLMs）在需要精细图像理解的任务（如场景文本识别或文档分析）上表现不佳，主要受限于感知能力有限和视觉信息碎片化。
### Innovation
引入了CropVLM作为一种低成本的外部方法，以提升性能。该模型通过强化学习进行训练，无需使用人工标注的边界框作为监督信号，也无需昂贵的合成评估。模型训练一次后，可以与开源和专有的VLMs结合使用，增强其性能，特别在需要高分辨率图像理解的任务中表现出显著改进，尤其是对于目标VLM外域的任务，无需修改或微调VLM本身，从而避免了灾难性遗忘。
### Conclusion
我们的方法在需要高分辨率图像理解的任务中取得了显著改进，特别是对于目标VLM外域的基准测试，而无需对VLM进行修改或微调，从而避免了灾难性遗忘。
## 433. `cs.CV` - 轻量级Transformer框架用于弱监督语义分割 [PDF](https://arxiv.org/pdf/2511.19765), [HTML](https://arxiv.org/abs/2511.19765)
### Authors
Ali Torabi,Sanjog Gaihre,Yaqoob Majeed
### Background
弱监督语义分割(WSSS)必须从嘈杂和不够明确的提示中学习密集掩码。本文回顾了SegFormer解码器，并展示了三种小的协同变化显著提高了弱监督的有效性，同时不改变MiT主干或依赖于繁重的后处理。
### Innovation
本文提出了CrispFormer方法，该方法通过增强解码器：(1)添加边缘分支以监督细粒度对象轮廓的边界，使用轻量级边缘头和边界感知损失；(2)添加不确定性引导修整器以预测每个像素的偶然不确定性，并使用它来加权损失和闸门分割logits的残差修正；(3)添加动态多尺度融合层，将静态拼接替换为多分辨率特征的空间softmax闸门，必要时受不确定性调节。结果是一个单次传递模型，能够保留清晰的边界、适当地选择每个位置的缩放级别，并抵抗弱提示的标签噪声。
### Conclusion
CrispFormer方法整合到标准WSSS管道中（种子、学生和EMA重新标注），在相同的种子下，比SegFormer基线模型在边界F分数、小对象召回率和mIoU上取得了一致的改进，同时增加的计算量很少。解码器中心的表达式易于实现、广泛兼容现有的SegFormer变体，并提供了一条通向更高保真度掩码的可重复途径，仅靠图像级别监督即可。
## 434. `cs.CV` - Prune-Then-Plan: 在体感问答中稳定前沿探索的步骤级校准 [PDF](https://arxiv.org/pdf/2511.19768), [HTML](https://arxiv.org/abs/2511.19768)
### Authors
Noah Frahm,Prakrut Patel,Yue Zhang,Shoubin Yu,Mohit Bansal,Roni Sengupta
### Background
大型视觉-语言模型（VLMs）通过提供强大的语义先验来增强开域推理的体感问答（EQA）代理。然而，当直接用于步骤级探索时，VLMs往往会表现出前沿震荡，由过度自信和校准不当导致的不稳定来回运动，从而影响导航效率和答案质量。
### Innovation
本文提出了一种简单而有效的Prune-Then-Plan框架，通过步骤级校准稳定探索。该方法使用基于Holm-Bonferroni的剪枝程序去除不可能的选择，并将最终决策交给基于覆盖的规划器。这种方法将VLM的过自信预测转变为保守且可解释的动作，依赖于人类级别的判断来校准VLM在步骤级的行为。
### Conclusion
将该方法集成到3D-Mem EQA框架中，相对于基线，本文的方法分别在视觉支持的SPL和LLM-Match指标上取得了高达49%和33%的相对改进。总体而言，该方法在探索预算相同的条件下，在OpenEQA和EXPRESS-Bench数据集上实现了更好的场景覆盖。
## 435. `cs.CV` - 洞悉潜在表示：通过潜在表示探针避免VLM生成的OCR错误 [PDF](https://arxiv.org/pdf/2511.19806), [HTML](https://arxiv.org/abs/2511.19806)
### Authors
Jihan Yao,Achin Kulshrestha,Nathalie Rauschmayr,Reed Roberts,Banghua Zhu,Yulia Tsvetkov,Federico Tombari
### Background
随着大型语言模型（VLMs）应用于关键安全领域，诸如场景文本视觉问答(STVQA)任务，模型在不确定情况下不作答的能力变得至关重要。这可以避免像光学字符识别（OCR）错误，如将“50 mph”误读为“60 mph”这类错误导致严重交通事故的风险。现有的避错方法要么依赖于不精确的概率输出，要么需要语义一致的验证，这在OCR任务上并不适用。研究表明，不确定性信号可能隐藏在VLMs的内部表示中。
### Innovation
该研究提出了一种名为潜在表示探针（LRP）的新方法，通过训练轻量级探针在隐藏状态或注意力模式上，探索了三种探针设计：跨所有层连接表示，基于视觉标记聚合注意力，以及通过多数投票结合单层探针。实验结果表明，在四个跨图像和视频模态的基准测试中，LRP相比于最佳基线提高了7.6%的避错准确性。通过对不同不确定性来源和数据集的探针进行分析，研究发现最优信号源自中间层而非最终层。
### Conclusion
研究建立了一个原则性的框架，通过检测内部状态而非不可靠的输出，发现自信信号以构建可部署的AI系统。
## 436. `cs.CV` - 通过提示语义空间优化实现无需训练的多样且高保真图像生成 [PDF](https://arxiv.org/pdf/2511.19811), [HTML](https://arxiv.org/abs/2511.19811)
### Authors
Debin Meng,Chen Jin,Zheng Gao,Yanran Li,Ioannis Patras,Georgios Tzimiropoulos
### Background
文本到图像的扩散模型面临图像多样性不足的挑战，低多样性的模型往往生成重复的输出，增加了采样的冗余度，妨碍了创意探索和下游应用。一个主要原因是生成过程常常向着学习分布中的强模式集中。现有的提高多样性的尝试，如噪声重采样、提示词重写或导向性引导，往往仍然集中于主导模式或者引入负面影响图像质量的失真。
### Innovation
提出了一种无需训练且适用于任何模型的模块Token-Prompt嵌入空间优化（TPSO）。TPSO引入可学习参数来探索令牌嵌入空间中未被充分代表的区域，减少模型重复生成来自学习分布中强模式的样本的倾向。同时，提示级别空间提供了全局语义约束，防止质量下降的同时保持高保真度。
### Conclusion
在MS-COCO和三种扩散模型上进行的广泛实验表明，TPSO显著增强了生成多样性，提高了基线性能4.08点而不牺牲图像质量。代码将在投稿接受后发布。
## 437. `cs.CV` - DOGE: Differentiable Bezier Graph Optimization for Road Network Extraction [PDF](https://arxiv.org/pdf/2511.19850), [HTML](https://arxiv.org/abs/2511.19850)
### Authors
Jiahui Sun,Junran Lu,Jinhui Yin,Yishuo Xu,Yuanqi Li,Yanwen Guo
### Background
自动从航空影像中提取道路网络是一项基本任务，但现有方法依赖于折线，难以建模曲线几何。研究表明道路几何本质上是基于曲线的。
### Innovation
介绍了一种新的可微分参数曲线表示方法——Bézier Graph，并提出了一个名为DOGE的框架，该框架通过学习直接从分割掩码中得到的参数Bézier图，消除了对曲线GT的需求，通过交替优化几何和拓扑的两个互补模块，实现了高精度的道路网络提取。
### Conclusion
DOGE方法在大规模的SpaceNet和CityScale基准测试中达成了新的最佳效果，提出了生成高质量矢量道路网络图的新范式。
## 438. `cs.CV` - ReDirector: 使用旋转相机编码创建任意长度视频重拍 [PDF](https://arxiv.org/pdf/2511.19827), [HTML](https://arxiv.org/abs/2511.19827)
### Authors
Byeongjun Park,Byung-Hoon Kim,Hyungjin Chung,Jong Chul Ye
### Background
本文介绍了一种名为ReDirector的新颖方法，该方法可以通过相机控制生成动态捕捉的变长视频的重拍。在此方法中，我们纠正了之前作品中使用RoPE时常见的错误，通过调整输入视频和目标重拍之间的时空位置。此外，我们引入了Rotary Camera Encoding (RoCE)，这是一种基于相机条件的RoPE相位移，能够捕捉和整合输入视频和目标视频中的多视角关系。
### Innovation
我们通过将相机条件整合到RoPE中，使方法能够应用于未见过的相机轨迹和视频长度。这种方法提高了动态对象定位和静态背景保留的效果，特别是在不同轨迹和长度的视频上。此外，实验结果表明，该方法在相机控制性、几何一致性以及视频质量方面都取得了显著改善。
### Conclusion
实验结果进一步证明了在不同轨迹和长度的视频上，该方法在相机控制性、几何一致性和视频质量方面取得了显著改进，展示出了良好的应用前景。
## 439. `cs.CV` - Large Language Model Aided Birt-Hogg-Dube Syndrome Diagnosis with Multimodal Retrieval-Augmented Generation [PDF](https://arxiv.org/pdf/2511.19834), [HTML](https://arxiv.org/abs/2511.19834)
### Authors
Haoqing Li,Jun Shi,Xianmeng Chen,Qiwei Jia,Rui Wang,Wei Wei,Hong An,Xiaowen Hu
### Background
深度学习方法在通过CT成像诊断Birt-Hogg-Dube综合征（BHD）时面临两大挑战：一是临床样本量有限，二是弥漫性囊性肺疾病（DCLDs）间类别区分度低。尽管多模态大型语言模型（MLLMs）在诊断罕见疾病方面显示潜力，但由于缺乏特定领域知识和可参考的放射学特征，增加了模型误诊的风险。
### Innovation
本文提出了一种名为BHD-RAG的多模态检索增强生成框架，该框架通过结合针对DCLD的专门知识和临床先例来增强MLLMs，从而提高BHD的诊断准确性。BHD-RAG采用了三个步骤：一是通过专门代理生成CT图像的成像表现描述以构建DCLDs病例的多模态语料库；二是使用余弦相似度检索相关影像描述对供查询图像；三是采用MLLM综合检索证据与影像数据进行诊断。
### Conclusion
BHD-RAG在包含四种类型DCLDs的数据集上进行了验证，实现了优于其他方法的准确性，并生成了与专家见解密切吻合的基于证据的描述。
## 440. `cs.CV` - Rectified SpaAttn: 回头审视用于高效视频生成的注意力稀疏性 [PDF](https://arxiv.org/pdf/2511.19835), [HTML](https://arxiv.org/abs/2511.19835)
### Authors
Xuewen Liu,Zhikai Li,Jing Zhang,Mengjuan Chen,Qingyi Gu
### Background
扩散变换器在视频生成方面占据主导地位，但注意力计算中的二次复杂性导致了显著的延迟。注意力稀疏性通过关注关键令牌来降低计算成本，忽略非关键令牌，但仍存在严重的性能下降问题。现有方法在注意力分配中引入了系统性偏差：（1）过度聚焦于关键令牌放大了它们的注意力权重；（2）完全忽视非关键令牌导致了相关注意力权重的损失。
### Innovation
本文重新审视了注意力稀疏性，提出了Rectified SpaAttn，通过隐含的全注意力参考来纠正注意力分配，增强了稀疏和全注意力图之间的对齐。为了应对这些问题，（1）针对关键令牌，其偏见与稀疏注意力权重成正比，比例由放大权重控制，因此提出了隔离池化注意力重分配，通过重新分配多模态池化权重计算准确的纠正因子。（2）对于非关键令牌，从池化查询-键中恢复注意力权重会产生注意力增益，但也会引入池化错误，因此提出了收益感知池化纠正，确保纠正后的增益稳定地超过引入的错误。此外，利用Triton定制并整合了Rectified SpaAttn内核，分别在HunyuanVideo和Wan 2.1上实现了3.33倍和2.08倍的速度提升，同时保持了高质量的生成。
### Conclusion
我们发布了Rectified SpaAttn作为开源工具，实现了在HunyuanVideo和Wan 2.1上的显著速度提升，并保持了高生成质量。
## 441. `cs.CV` - STAvatar：基于软绑定和时域密度控制的单目3D-head头像重建 [PDF](https://arxiv.org/pdf/2511.19854), [HTML](https://arxiv.org/abs/2511.19854)
### Authors
Jiankuo Zhao,Xiangyu Zhu,Zidu Wang,Zhen Lei
### Background
单目视频中从头像视频重建高保真和可动画化的3D头像仍然是一个具有挑战性但至关重要的任务。现有方法通常基于3D高斯 splatting，通过网格三角形绑定高斯，并通过线性混合皮肤变形来建模变形，这会导致刚性运动和表达力有限。此外，它们缺乏专门策略来处理经常被遮挡的区域（如口腔内部、眼睑等）。
### Innovation
我们提出了 STAvatar，包含两个关键组件：(1) 一种基于 UV-自适应软绑定框架，结合图像和几何先验学习 UV 空间中每个高斯的特征偏移。此 UV 表示支持动态采样，确保与自适应密度控制 (ADC) 兼容，并增强对形状和纹理变化的适应性。(2) 一种时域 ADC 策略，首先集群结构上相似的帧，以促进 densification 目标的更精确计算。引入了一种新颖的集合感知误差作为复制品标，同时捕捉几何和纹理的差异，促进在需要精细细节的区域的 densification。
### Conclusion
在四个基准数据集上的广泛实验表明，STAvatar 在捕捉细微特征和重建经常被遮挡的区域方面实现了最先进的重建性能。代码将公开提供。
## 442. `cs.CV` - MAPS：通过模块级相似性调度保留视觉语言表示以获得更好的视觉语言动作泛化 [PDF](https://arxiv.org/pdf/2511.19878), [HTML](https://arxiv.org/abs/2511.19878)
### Authors
Chengyue Huang,Mellon M. Zhang,Robert Azarcon,Glen Chou,Zsolt Kira
### Background
VLA模型继承了预训练的Vision-Language模型（VLM）的强先验知识，但简单的微调方式往往破坏这些表示并损害泛化能力。现有的修复方法要么过度限制适应性，要么忽略VLA组件的不同作用。
### Innovation
提出了一种名为MAPS（Module-Wise Proximity Scheduling）的首个稳健的VLA微调框架，通过系统分析发现了一种适当的固定顺序，使得可视化编码器保持在预训练先验的附近，而动作导向的语言层则更自由地适应。MAPS引入了零个额外参数或数据，并且可以无缝集成到现有的VLA中。
### Conclusion
在MiniVLA-VQ、MiniVLA-OFT、OpenVLA-OFT、SimplerEnv、CALVIN、LIBERO以及现实世界的Franka Emika Panda平台上，MAPS在分布内和分布外性能上都得到了显著提升，最多提高了30%。实验证明，固定预训练VLM的模块级相似原则是简单而有效的，能够保留VLM至VLA迁移中的广泛泛化能力。
## 443. `cs.CV` - ChessMamba: Structure-Aware Interleaving of State Spaces for Change Detection in Remote Sensing Images [PDF](https://arxiv.org/pdf/2511.19882), [HTML](https://arxiv.org/abs/2511.19882)
### Authors
Lei Ding,Tong Liu,Xuanguang Liu,Xiangyun Liu,Haitao Guo,Jun Lu
### Background
多时相遥感图像中的变化检测（CD）面临着高度异质性和时空对齐困难的挑战，现有基于视觉变压器或状态空间模型的方法通常在时间序列化过程中破坏了局部的结构一致性，使得在对齐不准确的情况下难以捕捉到区分性线索，从而影响可靠的变化定位。
### Innovation
ChessMamba框架利用交错的状态空间建模，提出了一种结构感知的方案。其主要创新点包括：(i) 棋盘式交错搭配蛇形扫描顺序进行多时相特征的统一序列化，以在单次前向传播中缩短特征间的交互路径，提高准确的变化检测；(ii) 结构感知的多空洞卷积融合来选择性地捕获单时相内中心及角落的上下文信息。
### Conclusion
在三个变化检测任务（二分类变化检测、语义变化检测和多模态建筑损坏评估）中的综合评估显示，ChessMamba有效融合了异质性特征，相比最先进的技术实现了显著的准确度提升。相关的代码将在指定网址提供。
## 444. `cs.CV` - 通过特征解耦提炼跨模态知识 [PDF](https://arxiv.org/pdf/2511.19887), [HTML](https://arxiv.org/abs/2511.19887)
### Authors
Junhong Liu,Yuan Zhang,Tao Huang,Wenchao Xu,Renyu Yang
### Background
知识蒸馏（KD）已被证明在压缩大型模型和提升小型模型性能方面非常有效。然而，在跨模态场景中，如视觉到语言的知识蒸馏，由于各模态之间表示的一致性较差，导致知识转移困难，其效果会显著下降。
### Innovation
提出了一种基于频率解耦的跨模态知识蒸馏方法，该方法通过利用频率域特征来解耦和平衡跨模态的知识转移。该方法针对低频特征强制其高度一致，而对于高频特征则引入较为宽松的对齐要求，并提出了尺度一致性损失来应对模态间分布的变化。
### Conclusion
在多个基准数据集上的广泛实验表明，该方法显著优于传统KD方法及现有的跨模态KD方法。相关的代码可以通过提供的链接获取。
## 445. `cs.CV` - 通过交织多领域身份课程在统一空间中的面部、全身人和物体分类 [PDF](https://arxiv.org/pdf/2511.19846), [HTML](https://arxiv.org/abs/2511.19846)
### Authors
Thomas M Metz,Matthew Q Hill,Alice J O'Toole
### Background
视觉基础模型可以在零样本模式下执行通用物体分类，并且在进行微调后，还可以进行人脸/人识别。然而，经过微调的模型会遭受灾难性遗忘的问题。本研究在单个嵌入空间中实现四个任务（物体识别、高质量和低质量图像的人脸识别、全身图像的人识别）的模型，避免了灾难性遗忘的大量出现。
### Innovation
提出了一种名为Interleaved Multi-Domain Identity Curriculum（IMIC）的方法，并引入了两个版本的IMIC：一种梯度耦合、交错的训练排程，可以同时在所有四个任务上微调基础骨干网络。这个方法在三种基础模型（DINOv3、CLIP 和 EVA-02）上都显示出良好的效果，特别是在面部、身体和物体数据集上的多任务处理上，EVA-02 和 CLIP 达到了甚至优于人类的表现。此外，研究还展示了这种方法对离分布外泛化没有显著的负面影响。
### Conclusion
最准确的模型变体（EVA-02 + IMIC A 和 B）在统一嵌入空间中实现了四个任务的线性可分表示，但在任务之间共享了大量特征。任何单一任务的不到100个主成分就可以接近完美地执行其他所有任务，而不会显著降低性能。这种方法表明，可以通过对抗灾难性遗忘的有效训练策略和统一的嵌入空间来实现多任务学习，同时保持基础模型的关键特性。
## 446. `cs.CV` - 4DWorldBench：一种全面的3D/4D世界生成模型评估框架 [PDF](https://arxiv.org/pdf/2511.19836), [HTML](https://arxiv.org/abs/2511.19836)
### Authors
Yiting Lu,Wei Luo,Peiyan Tu,Haoran Li,Hanxin Zhu,Zihao Yu,Xingrui Wang,Xinyi Chen,Xinge Peng,Xin Li,Zhibo Chen
### Background
世界生成模型正在成为下一代多模态智能系统的核心。与传统的2D视觉生成不同，世界生成模型旨在从图像、视频或文本中构建逼真的、动态的和物理上连贯的3D/4D世界。这些模型不仅需要生成高质量的视觉内容，还需要在空间、时间、物理和指令控制上保持一致性，从而能够应用于虚拟现实、自动驾驶、具身智能和内容生成。然而，之前的基准评估侧重于不同的评价维度，缺乏统一的世界逼真度评估。为了系统性地评估世界生成模型，作者引入了4DWorldBench，该基准从感知质量、条件-4D对齐、物理真实性和4D一致性四个关键维度对模型进行测量。该基准涵盖从图像到3D/4D、视频到4D、文本到3D/4D等任务，并创新地引入了多模态自适应条件以整合和扩展传统的评估范式。
### Innovation
作者创新性地引入了多模态自适应条件，这不仅整合了传统的评估范式，还扩展了它们。在评估过程中，将所有模态条件统一映射到一个文本空间，并进一步结合了文本模式的评价、多文本模式的评价和基于传统网络的方法。这种统一和自适应的设计提升了对对齐、物理真实性和跨模态连贯性的全面且一致的评估。初步的人类研究表明，自适应的工具选择更接近于主观的人类判断。
### Conclusion
我们希望这个基准能够为客观比较和改进提供基础，从而加速从“视觉生成”向“世界生成”的过渡。我们的项目可以在以下地址找到：[提供链接]。
## 447. `cs.CV` - GigaWorld-0: 世界模型作为数据引擎赋能实体AI [PDF](https://arxiv.org/pdf/2511.19861), [HTML](https://arxiv.org/abs/2511.19861)
### Authors
GigaWorld Team,Angen Ye,Boyuan Wang,Chaojun Ni,Guan Huang,Guosheng Zhao,Haoyun Li,Jiagang Zhu,Kerui Li,Mengyuan Xu,Qiuping Deng,Siting Wang,Wenkang Qin,Xinze Chen,Xiaofeng Wang,Yankai Wang,Yu Cao,Yifan Chang,Yuan Xu,Yun Ye,Yang Wang,Yukun Zhou,Zhengyuan Zhang,Zhehao Dong,Zheng Zhu
### Background
实体AI的发展需要高效且数据使用效率高的模型，世界模型（World Models）正在成为实现这一目标的基础架构。研究人员提出了GigaWorld-0，这是一种专为视觉-语言-动作（VLA）学习设计的统一世界模型框架。
### Innovation
GigaWorld-0 作为一个数据引擎，结合了两个协同组件：GigaWorld-0-Video 和 GigaWorld-0-3D。这些组件通过高效框架GigaTrain进行了联合优化，GigaTrain依赖于FP8精度和稀疏注意机制，大幅减少了内存和计算需求。GigaWorld-0 能生成高质量、多样且可控的多维度数据，训练数据集在GigaTrain框架下可扩展。
### Conclusion
基于GigaWorld-0生成的数据训练的VLA模型（如GigaBrain-0）在物理机器人上表现出色，显著提高了泛化能力和任务成功率，而无需在训练过程中进行任何真实世界的交互。
## 448. `cs.CV` - 从视觉模型向零样本时间任务转移空间先验的时空语义对齐：一种统一架构 [PDF](https://arxiv.org/pdf/2511.19856), [HTML](https://arxiv.org/abs/2511.19856)
### Authors
Xiangkai Ma,Han Zhang,Wenzhong Li,Sanglu Lu
### Background
大型多模态模型（LMMs）在跨文本和图像模态的内容对齐和生成方面取得了显著进展。然而，时空序列作为条件信号用于高保真图像生成的潜力尚未充分探索。现有方法将时间序列转化为“伪图像”以进行时间预测时，未能建立语义级别的对齐。
### Innovation
本文提出了TimeArtist，一种时空转换框架，首次在时间序列波动和视觉概念之间实现了语义级别的对齐。TimeArtist采用了一种“预热对齐”范式：首先，使用大规模数据集自监督训练双重自动编码器和共享量化器，学习模态共享的表示；然后，冻结编码器和量化器，引入投影以在表示层面上对齐时间和视觉样本。该工作建立了一种通用的跨模态框架，直接从时间序列生成高质量、多样化的图像，同时捕捉时间波动模式以使图像风格化。
### Conclusion
广泛的实验表明，TimeArtist在图像生成指标上具有令人满意的表现，同时在零样本时间任务上也取得了优越的结果。本研究确立了一种新的跨模态生成范式，填补了时间动态与视觉语义之间的差距。
## 449. `cs.CV` - MHB: 多模态手势感知边界检测在连续手语识别中的应用 [PDF](https://arxiv.org/pdf/2511.19907), [HTML](https://arxiv.org/abs/2511.19907)
### Authors
Mingyu Zhao,Zhanfu Yang,Yang Zhou,Zhaoyang Xia,Can Jin,Xiaoxiao He,Carol Neidle,Dimitris N. Metaxas
### Background
当前的手语识别研究主要依赖于视频中的孤立手语符号识别，而对于连续手语的识别则较少涉及。现有的识别方法中，虽然能够检测手势符号的开始和结束帧，但这些方法在鲁棒性和准确性上仍存在不足。
### Innovation
该研究提出的是一种多模态方法，首先利用机器学习来检测手语视频中手语符号的起始和终止帧。为了增强鲁棒性，研究中引入了从手语视频中提取的3D骨骼特征。此外，通过预训练的手形分类器来识别预期出现在手语符号起始和终止的手形，进而通过多模态融合模块将预训练的手语视频分割框架与手形分类模型统一起来。这种方法能够更准确地进行连续手语识别，尤其体现在不同形式的孤立手语符号和分割后的连续手语符号上。
### Conclusion
该方法在ASLLRP语料库上的测试中表现出了显著优于现有工作的识别效果，证明了其在鲁棒性和准确性方面的优势。
## 450. `cs.CV` - LiMT: 多任务肝脏图像基准数据集 [PDF](https://arxiv.org/pdf/2511.19889), [HTML](https://arxiv.org/abs/2511.19889)
### Authors
Zhe Liu,Kai Han,Siqi Ma,Yan Zhu,Jun Chen,Chongwen Lyu,Xinyi Qiu,Chengxuan Qian,Yuqing Song,Yi Liu,Liyuan Tian,Yang Ji,Yuefeng Li
### Background
计算机辅助诊断（CAD）技术能帮助临床医生评估肝脏病变并及时介入治疗。尽管近年来CAD技术取得了进步，但现有数据集的应用范围仍然相对有限，通常仅支持单一任务，限制了CAD技术的发展。
### Innovation
为了弥补这一局限，本文构建了一个用于肝脏和肿瘤分割、多标签病变分类和基于动脉期增强CT的病变检测的多任务肝脏数据集（LiMT），旨在探索不同任务之间的关联性，并且在训练时不必担心特定任务数据集之间的异质性。该数据集包括150个不同病例的CT体积，涵盖四种类型的肝脏疾病以及正常病例。每个体积由经验丰富的临床医生详细注释和校准。该公共多任务数据集可能成为医疗影像研究社区宝贵的资源。
### Conclusion
本文不仅提供了相关基准实验结果，还回顾了与肝脏相关任务相关的现有数据集和方法。数据集已公开，可以通过提供的链接访问。
## 451. `cs.CV` - VeriSciQA：科学视觉问答的自动验证数据集 [PDF](https://arxiv.org/pdf/2511.19899), [HTML](https://arxiv.org/abs/2511.19899)
### Authors
Yuyi Li,Daoyuan Chen,Zhen Wang,Yutong Lu,Yaliang Li
### Background
大型视觉-语言模型（LVLMs）在科学应用中前景广阔，但开源模型仍难以应对科学视觉问答（SVQA），即回答从科学论文中获取的图表问题。目前，公共、大规模、高质量的SVQA数据集缺乏是一个关键瓶颈。虽然最近的研究尝试用LVLM生成大规模数据，但其生成的问答对存在系统性错误，源于LVLM的固有限制和图表与文本之间信息不对称的问题。
### Innovation
提出了基于验证的生成-然后验证框架，首先生成含有图表关联文本背景的问答对，然后通过跨模态一致性检查和辅助过滤器去除错误的问答对。采用此框架创建了VeriSciQA数据集，包含20,351个问答对，覆盖20个科学领域和12种图表类型。VeriSciQA是一个具有挑战性的基准，开源模型的准确性远低于专有模型。经过VeriSciQA训练的模型在SVQA基准测试中表现出持续改进，数据量越大，性能提升越明显。进一步的人类评估证实了VeriSciQA的优越正确性。
### Conclusion
通过扩展数据集，本方法预计可以进一步推动开源社区中SVQA能力的发展。
## 452. `cs.CV` - Motion Marionette：通过先验指导重思刚性运动转移 [PDF](https://arxiv.org/pdf/2511.19909), [HTML](https://arxiv.org/abs/2511.19909)
### Authors
Haoxuan Wang,Jiachen Tao,Junyi Wu,Gaowen Liu,Ramana Rao Kompella,Yan Yan
### Background
以往的工作通常使用几何、生成或模拟先验来引导运动转移过程，但这些外部先验引入了辅助约束，导致通用性和时间一致性之间的权衡。
### Innovation
提出了一个内部先验框架，通过内部先验捕捉空间-时间变换，并且此先验可以在源视频和任一转移目标视频间共享，从而指导运动转移过程。首先将源视频和目标图像提升到统一的3D表示空间，从源视频中提取运动轨迹构建独立于对象几何和语义的空间-时间（SpaT）先验，记录时间上的相对空间变化。进一步将此先验与目标对象结合生成可控的速度场，并利用基于位置的动力学方法进行细化以减轻伪影并增强视觉连贯性。生成的速度场可以灵活地应用于高效的视频生产。
### Conclusion
实验结果表明，Motion Marionette在不同对象上具有良好的泛化能力，生成的时间上一致且与源运动良好对齐的视频，并支持可控视频生成。
## 453. `cs.CV` - Agent0-VL：探索工具集成视觉语言推理的自我进化代理 [PDF](https://arxiv.org/pdf/2511.19900), [HTML](https://arxiv.org/abs/2511.19900)
### Authors
Jiaqi Liu,Kaiwen Xiong,Peng Xia,Yiyang Zhou,Haonian Ji,Lu Feng,Siwei Han,Mingyu Ding,Huaxiu Yao
### Background
视觉语言代理在多种多模态推理任务中取得了显著进展，但其学习仍然受限于人类注释监督的限制。先前的方法试图通过让模型成为自己的批评家或奖励提供者来克服这一限制。然而，纯文本自评价难以验证复杂的视觉推理步骤，并且经常遭受评价幻觉。借鉴工具集成推理的最新进展，本文提出了一种自我进化的视觉语言代理Agent0-VL，通过工具集成推理实现持续改进。
### Innovation
Agent0-VL将工具使用不仅纳入推理，也纳入自我评估和自我修复，使模型能够通过基于证据的分析进行自我反省、验证和精细加工。该代理旨在通过工具驱动验证和强化学习的联合作用，稳定自我改进的推理和评估分布。此外，Agent0-VL通过零外部奖励进化，无需任何人工注释或外部奖励模型，实现了持续自我改进。
### Conclusion
实验表明，Agent0-VL在几何问题解决和视觉科学分析中比基线模型提高了12.5%。我们的代码可从给定链接获得。
## 454. `cs.CV` - Reasoning-VLA:一种适用于自主驾驶的快速且通用的视觉-语言-动作推理模型 [PDF](https://arxiv.org/pdf/2511.19912), [HTML](https://arxiv.org/abs/2511.19912)
### Authors
Dapeng Zhang,Zhenlong Yuan,Zhangquan Chen,Chih-Ting Liao,Yinda Chen,Fei Shen,Qingguo Zhou,Tat-Seng Chua
### Background
VLA模型在自主驾驶中展现出了强大的决策能力，但现有VLA模型在实现高效推理和在新型自主车辆配置及驾驶场景中泛化方面存在不足。
### Innovation
提出了Reasoning-VLA，一种具有通用性和快速性的动作生成VLA框架。该模型通过基于地面真实轨迹初始化的一系列可学习动作查询进行推理，生成连续动作轨迹。通过将八个公开的自主驾驶数据集标准化、采用联想推理，并使用易于使用的数据格式进行模型训练，同时结合了监督学习和强化学习微调，评估结果表明Reasoning-VLA实现了最先进的性能、优异的泛化能力和迄今为止报告的最优推理速度。
### Conclusion
在多个基准测试中的广泛实证评估表明，Reasoning-VLA在性能、泛化能力和推理速度方面均达到了最先进的水平。
## 455. `cs.CV` - 低分辨率编辑足以应对高分辨率编辑 [PDF](https://arxiv.org/pdf/2511.19945), [HTML](https://arxiv.org/abs/2511.19945)
### Authors
Junsung Lee,Hyunsoo Lee,Yong Jae Lee,Bohyung Han
### Background
高分辨率内容创作正迅速成为视觉与图形领域的重要挑战。尽管图像是最基本的视觉表达形式，但生成符合用户意图的内容需要有效的、可控的高分辨率图像编辑机制。然而，现有方法仍然局限于低分辨率场景，通常仅支持高达1K分辨率。
### Innovation
本文介绍了高分辨率图像编辑任务，并提出了一种测试时优化框架来解决这一问题。方法对高分辨率源图像进行块级优化，随后使用精细细节转移模块和新颖的同步策略以维护块间的连贯性。
### Conclusion
实验结果表明，本方法生成高质量的编辑结果，推动了高分辨率内容创作的发展。
## 456. `cs.CV` - 无监督更得见：基于原型引导提示的训练-free 核实例分割 [PDF](https://arxiv.org/pdf/2511.19953), [HTML](https://arxiv.org/abs/2511.19953)
### Authors
Wen Zhang,Qin Ren,Wenjing Liu,Haibin Ling,Chenyu You
### Background
核实例分割是病理学计算中的关键任务，支持数据驱动的临床洞察并促进下游转化应用。虽然大型视觉基础模型在零样本生物医学分割中显示出前景，但现有方法仍然依赖密集监督和计算昂贵的微调。因此，训练-free 方法成为研究的有吸引力的方向，但尚未充分探索。
### Innovation
提出SPROUT，一种完全训练-和标注-free 的提示框架，用于核实例分割。SPROUT 利用组织学先验构造特定幻灯片的参考原型，以缓解领域差距，并通过部分最优传输方案逐步引导特征对齐。前景和背景特征被转换为正和负点提示，使Segment Anything Model (SAM) 能够在不更新任何参数的情况下生成精确的核边界。
### Conclusion
在多个病理学基准测试上的广泛实验表明，SPROUT 在无需监督或重新培训的情况下实现了可竞争的性能，确立了病理学中可扩展的训练-free 核实例分割的新范式。
## 457. `cs.CV` - 耦合物理门控适应：复杂3D打印物体中立体光化学转化的空间解码 [PDF](https://arxiv.org/pdf/2511.19913), [HTML](https://arxiv.org/abs/2511.19913)
### Authors
Maryam Eftekharifar,Churun Zhang,Jialiang Wei,Xudong Cao,Hossein Heidari
### Background
目前，对于复杂三维打印物体中的光化学转化预测仍然是个挑战性的计算机视觉任务，常规的计算机视觉模型由于缺乏对光学物理（如衍射、吸收）和材料物理（如扩散、对流）耦合、非线性相互作用的归纳偏见，无法有效地进行预测。研究领域亟需一种新的方法来克服这一限制。
### Innovation
提出了一种名为耦合物理门控适应（C-PGA）的新颖多模态融合架构。该架构通过使用稀疏的几何和过程参数（如表面传输、打印层高）作为查询来动态门控和适应密集的视觉特征，使模型能够根据物理上下文校准其视觉感知。这种方法在虚拟化学表征方面取得了突破，可以消除传统的打印后测量，并实现对光化学转化状态的精确控制。
### Conclusion
通过引入C-PGA方法，利用最大规模的光学打印3D标本数据集，实现了复杂三维打印物体的光化学转化预测，这是一种基于物理上下文动态调整视觉感知的新方法，对未来在三维打印物体中的光化学性能预测和调控有着重要意义。
## 458. `cs.CV` - HybriDLA: 混合生成方法在文档布局分析中的应用 [PDF](https://arxiv.org/pdf/2511.19919), [HTML](https://arxiv.org/abs/2511.19919)
### Authors
Yufan Chen,Omar Moured,Ruiping Liu,Junwei Zheng,Kunyu Peng,Jiaming Zhang,Rainer Stiefelhagen
### Background
传统的文档布局分析（DLA）依赖于经验性的先验知识或固定的可学习查询，在单次前向传递中执行。这种传统方法足以应对早期文档，这些文档的区域数量较少且固定。然而，对于现代文档，这些文档表现出多变的元素数量和日益复杂的布局，传统方法难以应对这些挑战。
### Innovation
HybriDLA提出了一种新颖的生成框架，结合了扩散模型和自回归解码。扩散模块会迭代地细化边界框假设，而自回归模块则注入语义和上下文意识，从而使在高度多变的布局中能够精确地预测区域。此外，设计了一个多尺度特征融合编码器，以捕捉细微的和高层的视觉线索，确保高质量的检测。
### Conclusion
在DocLayNet和M$^6$Doc基准测试上进行的实验证明，HybriDLA达到了83.5%的平均平均精度（mAP），并超越了以往的方法。所有数据和模型将在以下网址公开：this https URL.
## 459. `cs.CV` - CounterVQA：评估与改进视觉-语言模型在视频理解中的反事实推理 [PDF](https://arxiv.org/pdf/2511.19923), [HTML](https://arxiv.org/abs/2511.19923)
### Authors
Yuefei Chen,Jiang Liu,Xiaodong Lin,Ruixiang Tang
### Background
视觉语言模型（VLMs）在视频理解方面取得了显著进展，尤其是在特征对齐、事件推理和指令执行等任务上。然而，这些模型在反事实推理方面的能力，即推断在假设条件下可能的替代结果的能力，尚未得到充分探索。这种能力对于稳健的视频理解至关重要，因为它要求识别潜在的因果结构并推断未观察到的可能性，而不仅仅是识别已观察到的模式。
### Innovation
提出了一个基于视频的基准CounterVQA，它包含不同难度级别的三个级别，用于评估反事实推理的不同方面。通过全面评估最先进的开源和封闭源模型，发现了显著的性能差距：尽管这些模型在简单的反事实问题上达到合理精度，但在复杂的多跳因果链上性能显著下降。为此，开发了一种后训练方法CFGPT，该方法通过从语言模态中提取模型的反事实推理能力来增强其视觉反事实推理能力，并在所有CounterVQA难度级别上取得了一致改进。
### Conclusion
通过对CounterVQA基准的评估和改进EFPT方法，发现了视觉-语言模型在反事实推理方面的能力差距，并展示了CFGPT方法的有效性，该方法在多种视觉-语言模型上均显示出一致的性能提升。未来的工作预计将发布该数据集和代码。
## 460. `cs.CV` - 融合视觉大型模型的智能图像搜索算法 [PDF](https://arxiv.org/pdf/2511.19920), [HTML](https://arxiv.org/abs/2511.19920)
### Authors
Kehan Wang,Tingqiong Cui,Yang Zhang,Yu Chen,Shifeng Wu,Zhenzhang Li
### Background
细粒度图像检索在安全和工业检测等领域中具有重要作用，但现有方法存在显著局限。传统的手动特征（如SIFT）缺乏鲁棒性；基于深度学习的检测器（如YOLO）可以识别组件的存在，但不能进行状态特定的检索或零样本搜索；视觉大型模型（VLM）提供语义和零样本能力，但由于空间定位较差和计算成本高，使其不适用于直接检索。
### Innovation
提出了一种名为DetVLM的新颖智能图像搜索框架，该框架结合了目标检测和VLM。该框架通过两阶段流水线进行搜索增强：首先使用YOLO检测器进行高效的高召回率组件级筛选，确定组件是否存在；然后，VLM作为召回增强单元，对于检测器未能捕捉到的组件进行二次验证。这种架构直接支持两种高级功能：1）状态检索：通过特定任务的提示，VLM验证组件的存在并执行复杂的状态判断（例如，“驾驶者佩戴口罩”），实现基于组件状态的检索；2）零样本检索：框架利用VLM固有的零样本能力，识别并检索包含未见过的组件或属性（例如，“司机佩戴口罩”）的图像，无需特定任务的训练。
### Conclusion
在车辆组件数据集上进行的实验表明，DetVLM的整体检索准确率达到94.82%，显著优于仅检测的基线；在零样本搜索中，对于司机佩戴口罩的准确率达到94.95%；在状态检索任务中，超过了90%的平均准确率。
## 461. `cs.CV` - 按需缩放：扩散模型的无训练集中局部缩放 [PDF](https://arxiv.org/pdf/2511.19917), [HTML](https://arxiv.org/abs/2511.19917)
### Authors
Qin Ren,Yufei Wang,Lanqing Guo,Wen Zhang,Zhiwen Fan,Chenyu You
### Background
目前扩散模型已成为文本到图像生成的主要范式，而推理时缩放（TTS）进一步通过在推理过程中分配更多计算来提高质量。然而，现有的TTS方法在全图层面上进行操作，忽视了图像质量在空间上可能存在异质性的事实。这导致在已经满足要求的区域进行了不必要的计算，并且无法充分修正局部缺陷。
### Innovation
本文提出了一种新的方向——局部TTS，该方法在确保高质量区域的前提下，适当地重新采样有缺陷的区域，从而大幅减少搜索空间。该框架面临的核心挑战是如何准确地定位缺陷以及保持全局一致性。为了解决这些挑战，本文提出了无训练框架LoTTS，它通过对比质量意识提示（如高质量 vs. 低质量）下的交叉注意力和自注意力信号来识别有缺陷的区域，并将其细化为连贯的掩模。在一致性方面，LoTTS只影响有缺陷的区域并对其进行局部去噪，以确保只有修正部分受影响，不会对整个图像造成干扰。
### Conclusion
实验结果表明，LoTTS在SD2.1、SDXL和FLUX数据集上都实现了最优性能：它能在提高局部质量并增强全局 fidelity 同时，使GPU成本降低了2-4倍。这些发现为扩散模型在推理时的局部缩放提供了新的有前景的方向。
## 462. `cs.CV` - 图像扩散模型在视频中展现出新兴的时序传播现象 [PDF](https://arxiv.org/pdf/2511.19936), [HTML](https://arxiv.org/abs/2511.19936)
### Authors
Youngseo Kim,Dohyun Kim,Geonhee Han,Paul Hongsuck Seo
### Background
图像扩散模型最初是用来生成图像的，但它们在生成过程中隐式地捕捉到了丰富的语义结构，可以用于多种识别和定位任务，而不仅仅是合成图像。
### Innovation
本文研究发现图像扩散模型的自注意力图可以重新解释为语义标签传播核，提供跨相关图像区域的稳健像素级对应关系。这种机制能够跨帧扩展，生成时间传播核，通过分割实现零样本目标跟踪。此外，本文还展示了测试时优化策略（如DDIM反向扩散、文本反向扩散和自适应头加权）的有效性，以适应扩散特征进行稳健且一致的标签传播。基于这些研究发现，本文提出了DRIFT框架，利用预训练图像扩散模型及SAM指导的掩膜精修方法进行视频目标跟踪，实现了标准视频对象分割基准上的最新零样本性能。
### Conclusion
本文证明了图像扩散模型能够通过分割进行零样本目标跟踪，同时表明测试时优化方法可以实现稳健和一致的标签传播，并通过DRIFT框架在标准视频对象分割基准上实现了最先进的零样本性能。
## 463. `cs.CV` - 基于上下文感知的令牌剪枝和判别选择性注意力机制的Transformer跟踪 [PDF](https://arxiv.org/pdf/2511.19928), [HTML](https://arxiv.org/abs/2511.19928)
### Authors
Janani Kugarajeevan,Thanikasalam Kokul,Amirthalingam Ramanan,Subha Fernando
### Background
基于Transformer的一流跟踪器通过拼接模板和搜索区域的令牌来增强集中注意能力，但搜索区域中过于大的背景搜索令牌所导致的目标模板令牌的注意减弱了跟踪器的区分能力。现有的一些令牌剪枝方法可以减轻背景干扰，但它们经常删除接近目标的令牌，从而导致有用上下文信息丢失和跟踪性能下降。此外，搜索令牌中的干扰物进一步降低了跟踪器准确识别目标的能力。
### Innovation
提出了一种名为CPDATrack的新型跟踪框架，它在两个特定的编码器层之间集成了一个可学习模块，以估算每个搜索令牌与目标关联的概率，从而抑制背景和干扰令牌的干扰，并保持目标周围的情境线索。此外，还使用了判别选择性注意力机制，在早期编码器层完全阻断搜索到模板的注意力，在后续层中仅从局部区域选择高概率的目标令牌来注意模板令牌，从而减少背景和干扰物的影响。
### Conclusion
所提出的CPDATrack在多个基准测试中达到了最先进的性能，特别是在GOT-10k基准测试中，平均重叠达到了75.1%。
## 464. `cs.CV` - VGGT4D：视觉几何变换器中运动线索的挖掘及其在4D场景重建中的应用 [PDF](https://arxiv.org/pdf/2511.19971), [HTML](https://arxiv.org/abs/2511.19971)
### Authors
Yu Hu,Chong Cheng,Sicheng Yu,Xiaoyang Guo,Hao Wang
### Background
4D场景重建是一项挑战，因为它需要从静态背景中稳健地分离动态物体。虽然3D基础模型如VGGT能够提供精准的3D几何结构，但在动态物体占主导的情况下，其性能显著下降。现有4D方法通常依赖外部先验、重度后优化或需要在4D数据集上进行微调。
### Innovation
作者提出了一种名为VGGT4D的无监督框架，它扩展了3D基础模型VGGT以实现稳健的4D场景重建。该方法利用VGGT中的全局注意力层隐含地编码的层次动态线索，并通过gram相似性挖掘和放大全局动态线索。为了进一步细化掩码边界，作者引入了由投影梯度驱动的精制策略。最后，将这些精确的掩码整合到VGGT的早期推理阶段，有效减轻了运动干扰在姿态估计和几何重建中的影响。
### Conclusion
在六个数据集上，该方法在动态对象分割、相机姿态估计和密集重建方面表现出优越性能，并且支持超过500帧的序列单次推理。
## 465. `cs.CV` - EmoFeedback2: 通过基于LVLM的奖励和文本反馈强化连续情感图像生成 [PDF](https://arxiv.org/pdf/2511.19982), [HTML](https://arxiv.org/abs/2511.19982)
### Authors
Jingyang Jia,Kai Shu,Gang Yang,Long Xing,Xun Chen,Aiping Liu
### Background
连续情感图像生成（Continuous Emotional Image Generation, C-EICG）由于能够生成与用户描述和连续情感值相匹配的图像而迅速发展。现有方法缺乏从生成图像中获得的情感反馈，这限制了情感连续性的控制。此外，它们之间简单的情感与未经调整的文字间的对齐方式无法根据图像内容适配地调整情感提示，导致情感的一致性不足。
### Innovation
提出了一种新的生成-理解-反馈强化学习范式（EmoFeedback2），利用微调的大型视觉-语言模型（LVLM）的推理能力，为生成高质量且具有连续情感的图像提供奖励和文本反馈。引入了情感感知的奖励反馈策略，引导生成模型的强化微调，提高图像的情感连续性。设计了一种自我提升的文本反馈框架，通过分析生成图像中的情感内容并适配地生成提请注意的建议，以精细粒度的内容提高情感的一致性。
### Conclusion
大量实验结果显示，该方法有效生成了具有所需情绪的高质量图像，优于我们自定义数据集上的现有顶级方法。代码和数据集将在不久后发布。
## 466. `cs.CV` - 通过激活重放增强大型多模态模型的推理能力 [PDF](https://arxiv.org/pdf/2511.19972), [HTML](https://arxiv.org/abs/2511.19972)
### Authors
Yun Xing,Xiaobin Hu,Qingdong He,Jiangning Zhang,Shuicheng Yan,Shijian Lu,Yu-Gang Jiang
### Background
最近，通过可验证奖励的强化学习（Reinforcement Learning with Verifiable Rewards, RLVR）在激励大型多模态模型（Large Multimodal Models, LMMs）的推理能力方面取得了显著的效果，但该机制本身在后训练范式下的工作原理尚不完全清楚。
### Innovation
论文通过‘激活重放’（Activation Replay）的方法，提出了一种无需训练的新颖简单有效的方法，用于提高后训练LMMs的多模态推理能力。该方法通过在测试时改变视觉标记，并从基LMM输入上下文中重放低熵激活，来调节RLVR的对应模型，从而在多种场景下（如数学问题、o3视觉代理和视频推理）触发更优的推理效果。实验结果表明，‘激活重放’方法能提高Pass@K性能，并减缓RLVR的推理覆盖范围狭窄的问题。
### Conclusion
研究发现，低熵激活的调控对后训练LMMs的推理能力有潜在的积极作用，而重放低熵激活的效果优于重放高熵激活或直接跨模型干预的方法。实验结果表明，‘激活重放’方法在多种场景下能显著提升多模态推理能力。
## 467. `cs.CV` - GazeProphetV2：基于头部运动的眼球预测实现高效移动VR聚焦渲染 [PDF](https://arxiv.org/pdf/2511.19988), [HTML](https://arxiv.org/abs/2511.19988)
### Authors
Farhaan Ebadulla,Chiraag Mudlpaur,Shreya Chaurasia,Gaurav BV
### Background
在虚拟现实（VR）环境中预测眼球运动仍然是一个显著的挑战，这与渲染优化和用户界面设计密切相关。目前的研究通常依赖单一的数据流进行预测，这限制了预测准确性。
### Innovation
该论文提出了一种多模态方法来预测VR眼球运动，结合了时间性眼球运动模式、头部运动数据和视觉场景信息。通过使用带有跨模式注意力机制的门控融合机制，这种方法能根据上下文相关性自适应地加权眼球历史记录、头部运动和场景内容。这种方法在涵盖22个VR场景、530万次眼球样本的数据集上进行评估，结果显示，与单独使用单一数据流相比，结合多种模态可以提高预测准确性。实验证明，将过去的视线轨迹与头部方向和场景内容相结合，可以提高1-3帧内预测的准确性。跨场景的一致性测试表明，该方法具有93.1%的验证准确率，并且在预测的眼球轨迹中保持了时序一致性。
### Conclusion
这些发现有助于理解虚拟环境中的注意力机制，并为渲染优化、交互设计和用户体验评估提供了潜在应用。这种方法代表了更高效预测用户注意力模式、减少对昂贵眼球跟踪硬件依赖的一个步骤。
## 468. `cs.CV` - HiCoGen：通过强化学习在扩散模型中进行分层组合图文生成 [PDF](https://arxiv.org/pdf/2511.19965), [HTML](https://arxiv.org/abs/2511.19965)
### Authors
Hongji Yang,Yucheng Zhou,Wencheng Han,Runzhou Tao,Zhongying Qiu,Jianfei Yang,Jianbing Shen
### Background
近年来，扩散模型在通过简洁的提示生成高质量图像方面展现出显著的能力。然而，当面对包含多个物体和层次结构的复杂提示时，现有模型难以准确遵循指令，导致概念遗漏、混淆和组合性差等问题。
### Innovation
该论文提出了一种基于新颖链式合成（CoS）范式的分层组合生成框架（HiCoGen）。HiCoGen 首先利用大型语言模型（LLM）将复杂提示分解为最小的语义单元，然后在每一步迭代地合成这些单元，确保每一步生成的图像为下一步提供重要的视觉上下文，以确保所有文本概念都能忠实地构建到最终场景中。此外，该论文还引入了强化学习框架，并通过理论证明，提出了一种衰减的随机性时间表以增强探索，并通过层次奖励机制优化该过程。
### Conclusion
实验结果表明，与现有方法相比，我们的方法在概念涵盖范围和组合准确性方面表现显著提升。
## 469. `cs.CV` - GFT-GCN: 基于频谱扩散的隐私保护3D面部网格识别 [PDF](https://arxiv.org/pdf/2511.19958), [HTML](https://arxiv.org/abs/2511.19958)
### Authors
Hichem Felouat,Hanrui Wang,Isao Echizen
### Background
3D面部识别通过捕捉面部几何提供了对光照变化、姿态变换和欺骗攻击的强健性生物特征解决方案，特别适合高安全性的应用。然而，存储的生物特征模板的安全性仍然至关重要。以往的方法缺乏同时保证隐私和性能的解决方案。
### Innovation
本论文提出了GFT-GCN，一种通过结合频谱图学习与扩散基础模板保护的隐私保护3D面部识别框架。该方法利用图傅里叶变换和图卷积网络从3D面部网格中提取紧凑且具有区分性的频谱特征，并通过频谱扩散机制生成不可逆、可再生且无法链接的模板。该架构确保原始生物特征数据始终不离开客户端设备，提高了安全性。
### Conclusion
在BU-3DFE和FaceScape数据集上的实验展示了高识别准确率和对抗重建攻击的强健性，证明了GFT-GCN能够高效地平衡隐私和性能，提供了一种可操作的安全3D面部认证解决方案。
## 470. `cs.CV` - SONIC: Spectral Optimization of Noise for Inpainting with Consistency [PDF](https://arxiv.org/pdf/2511.19985), [HTML](https://arxiv.org/abs/2511.19985)
### Authors
Seungyeon Baek,Erqun Dong,Shadan Namazifard,Mark J. Matthews,Kwang Moo Yi
### Background
传统的基于指导的方法在实际应用中用于修复问题的效果有限，导致需要专门的修复专用模型。研究指出缺少用于训练免费修复的有效成分是初始种子噪声的优化。
### Innovation
提出了一种新的训练免费方法，通过优化初始种子噪声来进行修复，使用线性逼近避免了昂贵的时间展开，并在频域中优化初始种子噪声以稳定优化过程。这种方法在多种修复任务中表现优于现有的最先进方法。
### Conclusion
本文方法展示了在各种修复任务中优于现有最好的表现。
## 471. `cs.CV` - MambaEye：一种基于因果顺序处理的无尺寸依赖视觉编码器 [PDF](https://arxiv.org/pdf/2511.19963), [HTML](https://arxiv.org/abs/2511.19963)
### Authors
Changho Choi,Minho Kim,Jinkyu Kim
### Background
尽管几十年来视觉编码器有了显著进步，但能够真正无损于输入尺寸且类似人类视觉的基本特征仍然难以实现。现有的Mamba视觉编码器通常采用双向处理方式，未能完全保留状态空间模型中的固有因果性。
### Innovation
我们提出了一种新型因果顺序编码器——MambaEye，利用低复杂度和基于因果过程的纯Mamba2架构。MambaEye采用了严格单向的处理方式，这使得其能够维护状态空间模型的固有因果性，并在任意点生成预测。MambaEye的核心创新是引入了相对位移嵌入，该嵌入能够编码连续图块之间的空间位移，为平移不变性提供了强先验知识，并使模型能够适应任意图像分辨率和扫描模式。此外，我们还引入了一种基于扩散的损失函数，以提供密集的、逐步的监督，使模型能够随着汇集更多视觉证据逐步建立信心。
### Conclusion
MambaEye在不同图像分辨率下表现出稳健的性能，尤其在更高分辨率的ImageNet-1K分类任务上达到了卓越结果（如1536^2分辨率）。这些成果都保持了线性的时间和空间复杂性，相对于图块数量而言。
## 472. `cs.CV` - CREward：一种类型特定的创新激励模型 [PDF](https://arxiv.org/pdf/2511.19995), [HTML](https://arxiv.org/abs/2511.19995)
### Authors
Jiyeon Han,Ali Mahdavi-Amiri,Hao Zhang,Haedong Jeong
### Background
创造性是一个复杂的现象。当涉及到创造力的表示和评估时，将创造力视为单一且未加区分的数量是显得天真和不足的。本文介绍了一种新的创造力激励模型CREward，该模型涵盖三个创造力维度：几何、材料和纹理，以便我们能够通过图像生成流程的角度来看待创造力。
### Innovation
本文提出了第一个类型特定的创造力激励模型CREward，该模型通过三个维度（几何、材料和纹理）展开，适用于评估和生成创造性图像。作者首先通过人类基准评估来捕捉不同类型图像中的创造力感知，然后使用大型视觉语言模型（LVLMs）对人类判断进行预测，并根据这些观察结果训练CREward模型。此外，CREward模型可用于创造力评估、可解释创造力和创造性样本的获取，以帮助人类设计灵感和引导创造性生成。
### Conclusion
CREward模型能够通过将创造力评价和生成融入图像生成流程中，从几何、材料和纹理三个维度上进行评估和生成，旨在提供更准确的创造力评估并促进创造性的生成。
## 473. `cs.CV` - 全向精细调整：强化学习引导的局部弥散精细调整 [PDF](https://arxiv.org/pdf/2511.19990), [HTML](https://arxiv.org/abs/2511.19990)
### Authors
Yaoli Liu,Ziheng Ouyang,Shengtao Lou,Yiren Song
### Background
参考引导的图像生成技术发展迅速，但目前的扩散模型在使用参考图精炼生成图像时，仍然难以保留精细的视觉细节。这一局限性源于基于VAE的潜空间压缩会丢弃细微的纹理信息，导致身份和属性特定的线索消失。此外，现有方法基于局部细节增强的后编辑方法往往会生产出与原始图像在光照、纹理或形状方面不一致的结果。
### Innovation
本研究引入了一种细节感知的精炼框架textbackslash我们的方法textbackslash（textbackslashourMthd），通过两个连续的参考驱动修正阶段来增强像素级一致性。首先，采用单图像弥散编辑器，并通过微调使其能够同时接收草图图像和参考图像，并在保持结构保真的同时实现全局一致性。然后应用强化学习，进一步强化局部编辑能力，明确优化细节准确性和语义一致性。
### Conclusion
广泛的实验显示，textbackslash我们的方法显著改善了参考对齐和细部细节保留。生成的忠实且视觉一致的编辑结果在具有挑战性的参考引导修复基准测试中超越了开源和商业模型。
## 474. `cs.CV` - 使用多模态融合网络的行人过街意图预测 [PDF](https://arxiv.org/pdf/2511.20008), [HTML](https://arxiv.org/abs/2511.20008)
### Authors
Yuanzhe Li,Steffen Müller
### Background
在城市环境中部署自动驾驶车辆（AVs）时，预测行人的过街意图是至关重要的。理想的情况下，这可以帮助AVs获取关键的环境线索，降低与行人相关的碰撞风险。但是，预测任务面临挑战，因为行人的行为多种多样，并且依赖于多种情境因素。
### Innovation
提出了一种多模态融合网络，该网络综合利用了来自视觉和运动分支的七种模态特征。具体来说，通过多个基于Transformer的提取模块从原始输入中提取运动和视觉特征。深度引导注意力模块利用深度信息引导另一模态中显著区域的注意力，通过全方位的空间特征交互。此外，设计了模态注意力和时间注意力机制来有选择地强调信息模态并有效捕捉时间依赖关系。
### Conclusion
在JAAD数据集上进行的大量实验验证了所提出网络的有效性，其性能优于基线方法。
## 475. `cs.CV` - WaymoQA：自动驾驶中的多视图视觉问答数据集用于安全关键推理 [PDF](https://arxiv.org/pdf/2511.20022), [HTML](https://arxiv.org/abs/2511.20022)
### Authors
Seungjun Yu,Seonho Lee,Namho Kim,Jaeyo Shin,Junsung Park,Wonjeong Ryu,Raehyuk Jung,Hyunjung Shim
### Background
近年来，多模态大型语言模型（MLLMs）在理解驾驶场景方面取得了显著进展，激发了其在自动驾驶中的应用兴趣。然而，仅凭单一前视图无法实现在高风险场景下的高级推理，尤其是在避免一种交通风险可能引发另一种风险的情况下，是如何进行有效的全面环境评估依然是一个巨大挑战。
### Innovation
为了解决这一挑战，本文定义了一个新的任务“安全关键推理”，该任务利用多视图输入来处理驾驶场景中的风险。通过这种方式，论文将安全关键推理拆分为两个阶段：首先解决当前的风险，然后减少由决策引发的下游风险。此外，提出了WaymoQA数据集，包含35,000个人工标注的问答对，覆盖复杂的高风险驾驶场景，并适用于图像和视频模态。实验表明，对标数据集WaymoQA进行微调，现有的MLLMs能显著提高其在高风险场景下的推理能力，证明了数据集的有效性。
### Conclusion
现有的多模态大语言模型在安全关键场景中的表现远不如在普通场景中，但通过WaymoQA数据集的微调可以显著提升它们的推理能力，强调了该数据集在开发更安全、更具有推理能力的自动驾驶代理方面的有效性。
## 476. `cs.CV` - 通过单一扰动劫持MLLMs决策链的可行性 [PDF](https://arxiv.org/pdf/2511.20002), [HTML](https://arxiv.org/abs/2511.20002)
### Authors
Changyue Li,Jiaying Li,Youliang Yuan,Jiaming He,Zhicong Huang,Pinjia He
### Background
传统的对抗性攻击主要针对神经网络的单一决策，忽略了在一系列决策过程中，独立错误可能纠正，但连续错误可能导致严重风险的问题。本文揭示了新型威胁：单一扰动可以操控整个决策链。研究者展示了操纵模型输出以达到多个预定义结果的可行性，比如同时错误地将“非机动车道”标志识别为“机动车道”，将“行人”识别为“塑料袋”。
### Innovation
引入了语义感知通用扰动（SAUPs），基于输入的语义生成多样化结果，并开发了一种有效算法，通过在归一化空间中使用语义分离策略搜索对抗性扰动。此外，还提出了RIST数据集，具有精细的语义标注，用于评估SAUPs的实际威胁，实验表明在控制五个不同目标时，仅使用一个对抗性帧就能实现70%的攻击成功率。
### Conclusion
该研究揭示了单一扰动可以完全操控模型决策链的新威胁，并提出的方法具有重要的理论和应用价值，在多个大型语言模型上显示出显著效果，证明了通过少量对抗性扰动即可带来高成功率攻击的可行性。
## 477. `cs.CV` - Clair Obscur：一种面向真实世界图像向量化的光照感知方法 [PDF](https://arxiv.org/pdf/2511.20034), [HTML](https://arxiv.org/abs/2511.20034)
### Authors
Xingyue Lin,Shuai Peng,Xiangyu Xie,Jianhua Zhu,Yuxuan Zhou,Liangcai Gao
### Background
图像向量化旨在将像素图像转换为可编辑和可缩放的矢量表示，同时保留视觉保真度。现有的向量化方法难以表示复杂的现实世界图像，往往以降低语义简洁性为代价，产生分割的形状。
### Innovation
本文提出了一种名为COVec的光照感知向量化框架，受光暗对比原则（Clair-Obscur）的启发，首次将固有图像分解引入向量领域，在统一的向量表示中分离出图像的成像、阴影和照明层。通过语义引导的初始化和两阶段优化，并结合可微渲染对这些层进行细化。
### Conclusion
在不同数据集上的实验显示，与现有方法相比，COVec在视觉保真度和编辑性方面达到了更高的水平。
## 478. `cs.CV` - MFM-point: 多尺度流配准用于点云生成 [PDF](https://arxiv.org/pdf/2511.20041), [HTML](https://arxiv.org/abs/2511.20041)
### Authors
Petr Molodyk,Jaemoo Choi,David W. Romero,Ming-Yu Liu,Yongxin Chen
### Background
近年来，点云生成在3D生成建模中引起了广泛关注。点基方法可以直接生成点云，无需依赖于其他表示如潜在特征、网格或体素。尽管这些方法具有较低的训练成本和算法上的简洁性，但在性能上通常逊色于基于表示的方法。
### Innovation
我们提出了MFM-Point，一种多尺度流配准框架，该框架大幅提高了点基方法的扩展性和性能，同时保持了其简洁性和高效性。我们的多尺度生成算法采用了从粗到细的生成范式，能够在不增加额外训练或推理开销的情况下提升生成质量和扩展性。
### Conclusion
实验结果表明，MFM-Point在点基方法中性能最佳，并且挑战了最佳基于表示的方法。特别是，在多类别和高分辨率生成任务中展现了出色的结果。
## 479. `cs.CV` - ACIT: Attention-Guided Cross-Modal Interaction Transformer for Pedestrian Crossing Intention Prediction [PDF](https://arxiv.org/pdf/2511.20020), [HTML](https://arxiv.org/abs/2511.20020)
### Authors
Yuanzhe Li,Steffen Müller
### Background
预测行人过马路意图对于自动驾驶车辆预防行人相关碰撞至关重要，但有效提取和整合不同类型数据的互补线索仍然是一项主要挑战。
### Innovation
本文提出了一种基于注意力引导的跨模态交互变换器（ACIT），用于行人过马路意图预测。ACIT 结合了六种视觉和运动模态，通过双路径注意力机制增强主要模式中的显著区域，并通过光流引导注意力促进与辅助模态的深入交互。此外，跨模态注意力机制和多模式特征融合模块进一步增强了跨模态交互，Transformer 基础的时序特征聚合模块用于捕捉序列依赖。
### Conclusion
实验结果表明，ACIT 在 JAADbeh 和 JAADall 数据集上分别取得了 70% 和 89% 的准确率，超过了现有最先进的方法。进一步进行了广泛的消融研究，探讨了 ACIT 各模块的贡献。
## 480. `cs.CV` - SAM-MI: 一种利用SAM增强开放词汇语义分割的含掩膜框架 [PDF](https://arxiv.org/pdf/2511.20027), [HTML](https://arxiv.org/abs/2511.20027)
### Authors
Lin Chen,Yingjian Zhu,Qi Yang,Xin Niu,Kun Ding,Shiming Xiang
### Background
开放词汇语义分割（OVSS）旨在普遍地分割和识别物体。SAM是一种通过大量高质量分割数据进行训练的模型，展现了显著的通用分割能力，并为OVSS提供了重要支持。尽管以前的方法已经在利用SAM进行OVSS方面取得了一些进展，但仍存在一些挑战：（1）SAM的过度分割倾向；（2）固定掩膜与标签之间的硬组合。
### Innovation
该论文提出了一种新的掩膜注入框架SAM-MI，它可以有效地将SAM与OVSS模型结合以解决以上挑战。首先，SAM-MI使用文本引导的稀疏点提示器来为SAM采样稀疏提示，代替了传统的稠密网格提示，从而显著加速了掩膜生成过程。其次，框架引入了浅层掩膜聚合（SMAgg）来合并部分掩膜，以减轻SAM的过度分割问题。最后，去耦合掩膜注入（DMI）将SAM生成的掩膜在低频和高频分别提供了指导，而不是直接与标签结合。
### Conclusion
通过对多个基准的广泛实验验证了SAM-MI的优势。特别地，与Grounded-SAM在MESS基准上的mIoU相比，所提出的方法获得了16.7%的相对改进，并且速度提高了1.6倍。我们希望SAM-MI能够作为一种有效的替代方法，为OVSS模型提供SAM支持。
## 481. `cs.CV` - History-Augmented Contrastive Meta-Learning for Unsupervised Blind Super-Resolution of Planetary Remote Sensing Images [PDF](https://arxiv.org/pdf/2511.20045), [HTML](https://arxiv.org/abs/2511.20045)
### Authors
Huijia Zhao,Jie Lu,Yunqing Jiang,Xiao-Ping Lu,Kaichang Di
### Background
计划照相机传感图像受到多种未知退化因素的影响，这些因素包括成像环境和硬件约束，从而限制了图像质量，阻碍了监督盲超分辨率的应用，因为缺乏真实图像作为指导。
### Innovation
本文提出了一种无监督的盲超分辨率框架——历史增强对比盲超分辨率（HACBSR），该框架不需要真实图像和外部核先验。HACBSR 包含两个组成部分：对比核采样机制，用于控制从高斯采样产生的分布偏差；以及采用历史模型生成负样本的历史增强对比学习机制，以实现更为谨慎的优化，并在无真实图像的情况下诱导强烈凸性。此外，引入了 Ceres-50 数据集，以支持对行星应用的评估。
### Conclusion
实验表明，本文提出的 HACBSR 在多个放大因子上的性能与当前先进的无监督方法相当。相关代码和数据集均可供访问。
## 482. `cs.CV` - FLaTEC：用于高效LiDAR点云压缩的频率分离潜在三平面 [PDF](https://arxiv.org/pdf/2511.20065), [HTML](https://arxiv.org/abs/2511.20065)
### Authors
Xiaoge Zhang,Zijie Wu,Mingtao Feng,Zichen Geng,Mehwish Nasim,Saeed Anwar,Ajmal Mian
### Background
点云压缩方法旨在同时优化比特率和重建失真。然而，平衡压缩率和重建质量具有挑战性，因为低频和高频成分在相同分辨率下贡献不同。现有方法大多不能同时高效压缩点云，同时保持高质量的重建效果。
### Innovation
本文提出了一种名为FLaTEC的频率感知压缩模型，能够以高压缩率压缩完整扫描。该方法引入了一种频率感知机制，分离低频结构和高频纹理，并利用混合的潜在三平面作为点云的紧凑代理。此外，FLaTEC采用了一种针对3D相关性丢失的高效频率注意力机制，以促进局部连接并输出任意分辨率点。
### Conclusion
FLaTEC方法在点云压缩的比特率-失真性能上达到最先进的效果，并在SemanticKITTI和Ford数据集上的BD-rate指标上分别优于标准编解码器78%和94%。
## 483. `cs.CV` - 在模型中指示查看位置：通过视觉引导注意力减轻MLLMs的幻觉现象 [PDF](https://arxiv.org/pdf/2511.20032), [HTML](https://arxiv.org/abs/2511.20032)
### Authors
Jianfei Zhao,Feng Zhang,Xin Sun,Chong Feng,Zhixing Tan
### Background
MLLMs依赖视觉注意力来解释视觉信息，但其局限性导致了幻觉现象。虽然MLLMs能准确提取视觉元素的意义，但在推理过程中未能充分使用这一优势。
### Innovation
提出了视觉引导注意力（VGA），这是一种无需训练的方法。VGA通过利用视觉标记的语义内容来构建精确的视觉锚定，然后利用这些锚定引导模型关注相关视觉区域。在生成过程的动态调节中，VGA进一步细化指导，抑制已描述过的区域。VGA仅需一次前向传播，引入的延迟开销仅为4.36%。同时，VGA兼容高效的注意力实现方式，如FlashAttention。
### Conclusion
在多项实验中，VGA在多个幻觉基准上实现了最先进的去幻觉化性能，并进一步分析确认了明确的视觉指导对提高MLLMs的视觉理解能力至关重要。
## 484. `cs.CV` - DeLightMono: 在解耦不均匀照明的基础上提升内窥镜自监督单目深度估计 [PDF](https://arxiv.org/pdf/2511.20058), [HTML](https://arxiv.org/abs/2511.20058)
### Authors
Mingyang Ou,Haojin Li,Yifeng Zhang,Ke Niu,Zhongxi Qiu,Heng Li,Jiang Liu
### Background
单目深度估计在内窥镜导航系统的发展中起着关键作用。由于内窥镜图像中固有的不均匀照明，尤其是在低光强度区域，现有深度估计性能下降。为了解决这个问题，领域内的现有低光增强技术并未有效引导深度网络。此外，其他领域如自动驾驶需要充足的光照，这使得它们不适合用于此类任务以及增加了数据收集的负担。因此，提出了一个新的解耦不均匀照明的自监督单目深度估计框架——DeLight-Mono。
### Innovation
该框架通过设计一种光照-反射-深度模型并利用辅助网络将图像分解开来表示端窥镜图像。提出了一种新的联合优化的自监督框架，并利用解耦合的组件设计了新的损失函数以减轻不均匀照明对深度估计的影响。
### Conclusion
通过在两个公开数据集上进行广泛比较和消融研究，证明了所提出方法的有效性。
## 485. `cs.CV` - 城市环境中行人过街意图预测的多上下文融合变换器 [PDF](https://arxiv.org/pdf/2511.20011), [HTML](https://arxiv.org/abs/2511.20011)
### Authors
Yuanzhe Li,Hang Zhong,Steffen Müller
### Background
自动车辆提高行人安全并减少交通事故的关键是预测行人的过街意图。然而，城市环境中行人的行为受到多种因素的影响，使得准确预测行人意图极具挑战性。
### Innovation
本文提出了一种多上下文融合变换器（MFT），它综合利用了四个关键维度（行人行为上下文、环境上下文、行人定位上下文和车辆运动上下文）的多样化数值上下文属性，通过依次融合互相关几个上下文特性，生成上下文特定的表示形式。MFT采用了逐步融合策略，通过引导互相关上下文中的注意力细化每个上下文中的上下文标记，并通过引导的信息传播增强全局CLS标记，促进多上下文融合，从而实现更深层次且高效的整合。
### Conclusion
实验结果表明，MFT在JAADbeh、JAADall和PIE数据集上分别取得了73%、93%和90%的准确率，优于现有最先进的方法。此外，还进行了广泛的消融研究以调查网络架构的有效性及不同输入上下文的贡献。
## 486. `cs.CV` - PRADA：基于概率比的鉴别和检测自回归生成图像的方法 [PDF](https://arxiv.org/pdf/2511.20068), [HTML](https://arxiv.org/abs/2511.20068)
### Authors
Simon Damm,Jonas Ricker,Henning Petzka,Asja Fischer
### Background
自回归（AR）图像生成作为一种有力的图像合成方法，近期逐渐兴起。AR 图像生成使用了大型语言模型生成的原理，能够高效生成看起来极具欺骗性的图像，进一步加强了对可靠检测方法的需求。然而，到目前为止，专门针对AR图像生成器生成图像的检测工作仍然相对缺乏。
### Innovation
本文提出了一种简单且可解释的方法，即PRADA（Probability-Ratio-Based Attribution and Detection of Autoregressive-Generated Images），能够可靠地检测AR生成的图像并将其归因于相应的生成模型。该方法的核心在于检查模型在给定图像的自回归标记序列时的条件概率与无条件概率的比例。这种方法根据不同模型生成的图像显示出的独特特征进行阈值检测。
### Conclusion
实验评估表明，PRADA在对抗八种类别到图像模型和四种文本到图像模型时表现出很高的有效性。
## 487. `cs.CV` - 使用概念瓶颈模型的可解释视觉异常检测 [PDF](https://arxiv.org/pdf/2511.20088), [HTML](https://arxiv.org/abs/2511.20088)
### Authors
Arianna Stropeni,Valentina Zaccaria,Francesco Borsatti,Davide Dalle Pezze,Manuel Barusco,Gian Antonio Susto
### Background
近年来，基于视觉的异常检测（VAD）受到了广泛关注，因为它能够在仅使用正常图像进行训练的情况下识别异常图像。许多VAD模型在无需监督的情况下运行，仍能够通过突出显示图像中的异常区域提供视觉解释。然而，尽管这些视觉解释有所帮助，但它们缺乏对用户的直接且语义上的意义解释。
### Innovation
本文提出将概念瓶颈模型（CBMs）应用于VAD设置，通过学习有意义的概念来生成人类可解释的异常描述，从而提供一种新颖且更具洞察力的解释方式。本文的贡献包括：(i) 发展了一个概念数据集以支持CBMs在VAD中的研究；(ii) 改进了CBM架构，以生成基于概念和视觉的解释，结合了语义和定位可解释性；(iii) 引入了一种合成人工异常的管道，以保留VAD减少对罕见异常样本依赖的范式。CONVAD在保持经典VAD方法性能的同时，提供了更丰富、基于概念的解释，增强了解释性和VAD系统的信任。
### Conclusion
本文提出的方法CONVAD能够在保持与经典VAD方法相当的性能的同时，提供更丰富、基于概念的解释，提高VAD系统的可解释性和用户信任。
## 488. `cs.CV` - 盲适应局部去噪方法在CEST成像中的应用 [PDF](https://arxiv.org/pdf/2511.20081), [HTML](https://arxiv.org/abs/2511.20081)
### Authors
Chu Chen,Aitor Artola,Yang Liu,Se Weon Park,Raymond H. Chan,Jean-Michel Morel,Kannie W. Y. Chan
### Background
CEST MRI 通过利用质子交换动力学可以实现对低浓度代谢物的分子级可视化，但其临床应用受到硬件限制带来的空间变异性噪声和复杂成像协议导致的异方差性挑战。传统去噪方法无法处理这种复杂噪声，并且往往会改变对生物医学分析至关重要的信息。为了解决这些限制，本文提出了一种新的盲自适应局部去噪（BALD）方法。
### Innovation
BALD 利用CEST数据的自相似性来推导出自适应方差稳定变换，无需先验噪声特性知识即可在CEST像素间等化噪声分布。然后，BALD 对数据的线性变换进行两阶段去噪，以分离分子信号和噪音。通过局部SVD分解作为线性变换来防止空间和光谱去噪伪影。
### Conclusion
在多种人造模型和体内CEST扫描的广泛验证实验中，BALD 在去噪指标和后续任务（如分子浓度图估计和癌症检测）中都优于最先进的CEST去噪器。
## 489. `cs.CV` - 探索最新的模型在早期森林火灾检测中的应用 [PDF](https://arxiv.org/pdf/2511.20096), [HTML](https://arxiv.org/abs/2511.20096)
### Authors
Sharjeel Ahmed,Daim Armaghan,Fatima Naweed,Umair Yousaf,Ahmad Zubair,Murtaza Taj
### Background
近年来，深度学习神经网络在火灾检测领域取得了许多进展。然而，由于缺乏大量的数据集和专门针对这一任务优化的模型，现有的方法在火灾检测中存在误报的问题。鉴于此，本文提出了一种早期预警系统，旨在通过视觉分析检测森林火灾。
### Innovation
本文首次提出了一个用于早期识别森林火灾的图像数据集，该数据集包含烟柱和火源的多个实例，以表示火灾的初始阶段。本文还使用游戏模拟器（如《荒野大镖客2》）制作这个数据集，并将其与已发表的图像结合，以创建一个更加全面的集合。最后，本文对图像分类和定位方法在所提出的数据集上的表现进行了比较，具体使用了YOLOv7模型及其不同检测变换器模型。
### Conclusion
研究结果表明，YOLOv7以及其他检测变换器模型在早期识别森林火灾方面具有良好的应用潜力。
## 490. `cs.CV` - WPT: 通过在线世界模型蒸馏实现世界到策略的迁移 [PDF](https://arxiv.org/pdf/2511.20095), [HTML](https://arxiv.org/abs/2511.20095)
### Authors
Guangfeng Jiang,Yueru Luo,Jun Liu,Yi Huang,Yiyao Zhu,Zhan Qu,Dave Zhenyu Chen,Bingbing Liu,Xu Yan
### Background
近年来，世界模型取得了显著进展，主要目标是捕捉代理行为与环境演变之间的时空关联。然而，现有方法常常存在运行时耦合紧或者依赖于离线奖励信号的问题，导致推理开销大或阻碍端到端优化。
### Innovation
我们提出了WPT（World-to-Policy Transfer），一种通过端到端世界模型在线蒸馏的策略到策略迁移框架。通过开发一个可训练的奖励模型，将世界知识注入教师策略，并通过对齐候选轨迹与世界模型预测的未来动力学来实现这一目标。进一步提出了策略蒸馏和世界奖励蒸馏，将教师的推理能力转移到轻量级的学生策略中，同时提高了规划性能并保持实时部署能力。
### Conclusion
在开环和闭环基准测试中，我们的WPT实现了最先进的性能：在开环中达到0.11次碰撞率，在闭环中达到79.23的驾驶评分，优于基于世界模型和模仿学习的方法，在准确性和安全性方面都表现出色。此外，学生策略可保持高达4.9倍的更快推理速度，同时保留大部分性能提升。
## 491. `cs.CV` - 通过状态导向层级展开学习程序感知的视频表示 [PDF](https://arxiv.org/pdf/2511.20073), [HTML](https://arxiv.org/abs/2511.20073)
### Authors
Jinghan Zhao,Yifei Huang,Feng Lu
### Background
构建能够推理和执行复杂任务的代理的关键步骤是学习程序感知的视频表示。现有方法通常通过将视觉内容与任务和步骤级别的文本描述对齐来注入程序语义，但抽象的'任务'和'步骤'描述无法与视觉数据中的具体、可观察的细节形成稳健的对齐。
### Innovation
提出了一种新的任务-步骤-状态（TSS）框架，并通过渐进式预训练策略来强制模型在状态中接地表示，同时将它们与步骤和高层任务关联起来。引入了'状态'，即物体配置的文本快照，作为视觉地基的语义层，将抽象的程序与模型实际能够看到的联系起来。实验表明，该方法在多个下游任务中优于基线模型，并在消融研究中证明了状态监督是性能提升的关键驱动力。
### Conclusion
提出的方法在COIN和CrossTask数据集上的广泛实验中表现出色，证明了渐进式预训练策略比标准联合训练更有效，因为它更好地实现了预期的层级结构，取得了多重下游任务的优越性能。
## 492. `cs.CV` - Multi Head Attention Enhanced Inception v3 for Cardiomegaly Detection [PDF](https://arxiv.org/pdf/2511.20101), [HTML](https://arxiv.org/abs/2511.20101)
### Authors
Abishek Karthik,Pandiyaraju V
### Background
医疗成像技术的革新显著改变了心血管疾病的诊断方式，不仅限于此，还通过心脏扩大（心肌病）等结构异常的可视化，对心血管疾病有更深入的理解。本文探讨了一种利用深度学习和注意力机制结合的方法，旨在自动检测X光图像中的心脏扩大。
### Innovation
该研究结合了深度学习工具和注意力机制来自动检测X光图像中的心脏扩大。特别地，它采用了多头注意力机制，该机制能够自动学习特征，通过精确选择性聚焦于输入中的某些区域来敏感地识别心脏扩大。该方法还使用了多层注意力机制来增强检测效果。
### Conclusion
该模型在准确性方面达到了95.6%，精确度为95.2%，召回率为96.2%，灵敏度为95.7%，特异性为96.1%，区域下曲线（AUC）为96.0%，并在准确性和精确度等指标上进行了严格的评估，这些结果表明了该方法的临床意义和高效率。
## 493. `cs.CV` - LungEvaty: 一种可扩展、开源的基于变压器的深度学习模型，用于LDCT筛查中的肺癌风险预测 [PDF](https://arxiv.org/pdf/2511.20116), [HTML](https://arxiv.org/abs/2511.20116)
### Authors
Johannes Brandt,Maulik Chevli,Rickmer Braren,Georgios Kaissis,Philip Müller,Daniel Rueckert
### Background
随着越来越多的国家引入规模化的低剂量计算机断层扫描（LDCT）筛查项目，肺癌的风险评估变得越来越重要。随着影像数据量的增加，能够高效处理整个肺部数据的可扩展方法变得至关重要，以充分利用这些大规模筛查数据的潜力。现有的方法要么过于依赖像素级别的注释，限制了可扩展性，要么分析肺部数据的方式零散，削弱了性能。
### Innovation
我们提出了LungEvaty，这是一种全新的基于变压器的框架，能够从单张LDCT扫描中预测1-6年内的肺癌风险。该模型直接处理整个肺部输入，通过学习大规模筛查数据来捕捉与恶性风险相关的全面的解剖学和病理学线索。LungEvaty仅使用影像数据，无需区域监督，其性能与最先进水平相当，并且可以通过可选的解剖学导向注意力引导损失来进一步优化。LungEvaty总共使用了超过90,000张CT扫描数据进行训练，包括超过28,000张用于微调的数据和6,000张用于评估的数据。
### Conclusion
框架提供了一种简单、数据有效且完全开源的解决方案，为未来的纵向和多模态肺癌风险预测研究提供了可扩展的基础。
## 494. `cs.CV` - 安全对齐的大语言模型中连续视觉指令调优中的和谐参数适应 [PDF](https://arxiv.org/pdf/2511.20158), [HTML](https://arxiv.org/abs/2511.20158)
### Authors
Ziqi Wang,Chang Che,Qi Wang,Hui Ma,Zenglin Shi,Cees G. M. Snoek,Meng Wang
### Background
当前连续视觉指令调优（CVIT）已经在适应多模态大语言模型（MLLMs）方面显示出了潜力，但现有研究主要关注未进行安全对齐的模型。然而，现实中的MLLMs实际上需要这样的机制来减轻潜在风险，这一忽视导致了安全问题没有得到妥善处理。
### Innovation
本文提出了和谐参数适应（HPA），这是一种后训练框架，包括基于聚焦的参数分区、和谐平衡的参数选择和正交参数调整。通过这种方法，HPA能够有效地在安全性和任务性能之间实现平衡，缓解灾难性遗忘。
### Conclusion
在CVIT基准和安全评估数据集上的广泛实验表明，HPA在维持高安全性和缓解遗忘方面优于现有基线。
## 495. `cs.CV` - 混合卷积和频率状态空间网络在图像压缩中的应用 [PDF](https://arxiv.org/pdf/2511.20151), [HTML](https://arxiv.org/abs/2511.20151)
### Authors
Haodong Pan,Hao Wei,Yusong Wang,Nanning Zheng,Caigui Jiang
### Background
最近，基于Transformer和状态空间模型（SSM）的架构已经为图像压缩中的学习图像压缩（LIC）带来了好处。卷积神经网络（CNNs）能够有效地捕捉局部高频细节，而Transformer和SSM则提供了强大的长程建模能力，但可能会导致结构信息的丢失或忽略对于压缩至关重要的频率特性。
### Innovation
本文提出了一种混合卷积和频率状态空间网络（HCFSSNet），这是一种将CNN用于提取局部高频结构，并引入一种视见频状态空间（VFSS）块来建模长程低频信息的网络。VFSS块结合了具有全方位邻域状态空间（VONSS）模块，该模块可以在水平，垂直和对角线方向上扫描特征，以及自适应频率调制模块（AFMM），这种模块对离散余弦变换频率分量进行内容自适应加权，以实现更有效的比特分配。为了进一步减少熵模型中的冗余性，作者将AFMM与Swin Transformer结合，形成了一个感知频率相关信息建模的频域Swin Transformer注意力模块（FSTAM）。
### Conclusion
在Kodak、Tecnick和CLIC专业验证数据集上的实验表明，HCFSSNet在与最近的基于SSM的编解码器（例如MambaIC）相比时，具有可竞争的率失真性能，同时使用的参数量要少得多。在Kodak、Tecnick和CLIC上，HCFSSNet分别比VTM锚点降低了18.06％、24.56％和22.44％的BD率，提供了一种高效的、易于理解和适应未来的LIC系统中的混合架构。
## 496. `cs.CV` - Map-World: 蒙面动作规划和路径积分世界模型在自主驾驶中的应用 [PDF](https://arxiv.org/pdf/2511.20156), [HTML](https://arxiv.org/abs/2511.20156)
### Authors
Bin Hu,Zijian Lu,Haicheng Liao,Chengran Yuan,Bin Rao,Yongkang Li,Guofa Li,Zhiyong Cui,Cheng-zhong Xu,Zhenning Li
### Background
自主驾驶的路径规划必须处理多个可能的未来情景，同时保持高计算效率。现有的端到端系统和基于世界模型的规划器能够预测多模态的轨迹，但通常依赖于手工设计的锚点或增强学习来选择一个最佳模式用于训练和控制。这种选择会丢弃关于其他可能未来的有用信息，使优化过程变得更加复杂。
### Innovation
我们提出了MAP-World，这是一个不需要先验的多模态规划框架，结合了蒙面动作规划和路径加权世界模型。该方法通过掩码动作规划将未来车组运动视为掩码序列完成任务：过去点位被编码为可见令牌，未来点位被表示为掩码令牌，驾驶意图路径提供粗略框架。然后，通过引入噪声，将一个紧凑的潜在规划状态扩展为多个轨迹查询，生成多样且时间上连贯的模式，无需锚点库或教师策略。一个轻量级的世界模型根据每个候选轨迹来预测未来的BEV语义。在训练过程中，通过轨迹概率作为离散路径权重的期望来计算语义损失，从而使规划器可以从所有可能未来的完整分布中学习，而不仅仅是一个选定的路径。
### Conclusion
在NAVSIM上，我们的方法与基于锚点的方法具有相同的性能，并且在基于世界模型的方法中达到了最先进的性能，同时避免了使用增强学习，并保持了实时推理延迟。
## 497. `cs.CV` - UltraViCo: 突破视频扩散变换器外推极限 [PDF](https://arxiv.org/pdf/2511.20123), [HTML](https://arxiv.org/abs/2511.20123)
### Authors
Min Zhao,Hongzhou Zhu,Yingze Wang,Bokai Yan,Jintao Zhang,Guande He,Ling Yang,Chongxuan Li,Jun Zhu
### Background
尽管取得了进展，视频扩散变换器仍然难以在超出训练长度的情况下泛化，这一挑战我们称之为视频长度外推。此前工作通过位置编码试图解决重复问题，但忽视了质量退化，仅实现了有限的外推。
### Innovation
我们从基础视角重新审视了这一挑战，发现注意力图作为直接控制上下文如何影响输出的关键。我们发现重复和质量退化都源于注意力分散，即训练窗口以外的标记稀释了学习到的注意力模式。UltraViCo 是一个无需训练的插件方法，通过常数衰减因子抑制训练窗口外的注意力。
### Conclusion
我们的方法在多种模型和外推比率下均优于基线，将外推极限从2倍提高到4倍。在4倍外推极限下，UltraViCo 相较于之前最优方法动态度和成像质量分别提高了233%和40.5%。此外，该方法还可无缝迁移到可控视频合成和编辑等下游任务中。
## 498. `cs.CV` - 在识别动作时，LMMs难以检测核心交互事件 [PDF](https://arxiv.org/pdf/2511.20162), [HTML](https://arxiv.org/abs/2511.20162)
### Authors
Daniel Harari,Michael Sidorov,Liel David,Chen Shterental,Abrham Kahsay Gebreselasie,Muhammad Haris Khan
### Background
大型多模态模型（LMMs）在处理真实视觉任务方面已显示出越来越强的表现，尤其是在对图像和视频进行分析方面。例如，这类模型能够详细描述视频序列中的物体、周围环境和动态行动。当前研究探讨了这些模型在何种程度上将语义理解置于实际视觉输入的基础上。鉴于手部与物体交互的视频序列，研究人员试图了解模型何时、何地开始或结束交互。为此，他们创建了一个前所未有的大型数据集，包含来自Something-Something-V2数据集的超过20,000个标注的交互事件，由250名AMTurk人类标注员为交互事件打上标签，特别是标记物体和执行者何时、何处产生接触或脱离。
### Innovation
本研究的创新之处在于构建了一个全新的大规模数据集，该数据集包含超过20,000个标注的交互事件，并使用该数据集评估了大型多模态模型在检测交互事件起始和结束帧方面的表现。
### Conclusion
尽管这些模型能够准确识别目标物体、描述动作并提供连贯的推理，但在识别交互事件的起始和结束帧时，它们普遍表现不佳，并且无法在场景中定位事件。研究发现，模型在处理定义交互的具体物理接触时刻和位置时存在感知方面的缺陷，这限制了它们对动态场景的深入理解能力。
## 499. `cs.CV` - Restora-Flow: Mask-Guided Image Restoration with Flow Matching [PDF](https://arxiv.org/pdf/2511.20152), [HTML](https://arxiv.org/abs/2511.20152)
### Authors
Arnela Hadzic,Franz Thaler,Lea Bogensperger,Simon Johannes Joham,Martin Urschler
### Background
流匹配作为一种生成技术，正在解决最先进的扩散模型的采样时间长的问题，并允许更灵活的轨迹设计，同时保持高质量的图像生成。这种能力使其适合作为图像修复任务的生成先验。尽管当前利用流模型的方法在修复中显示出有前景的结果，但仍有一些方法存在处理时间长或图像过度平滑的问题。
### Innovation
本文提出了一种名为Restora-Flow的无需训练的方法，该方法通过退化掩模引导流匹配采样，并结合了轨迹校正机制，以确保与退化输入的一致性。这种方法在多个涉及基于掩码退化的图像修复任务中进行了评估，包括填补、超分辨率和去噪，结果显示了感知质量的优越性以及处理时间的改进。
### Conclusion
Restora-Flow 方法展示了在多个图像修复任务中对感知质量的优越表现和快速的处理时间，相较于扩散方法和基于流匹配的参考方法。
## 500. `cs.CV` - 用于自动生成3D PET/CT报告的视觉-语言模型 [PDF](https://arxiv.org/pdf/2511.20145), [HTML](https://arxiv.org/abs/2511.20145)
### Authors
Wenpei Jiao,Kun Shang,Hui Li,Ke Yan,Jiajin Zhang,Guangjie Yang,Lijuan Guo,Yan Wan,Xing Yang,Dakai Jin,Zhaoheng Xie
### Background
正电子发射断层扫描/计算机断层扫描(PET/CT)在肿瘤学中至关重要，但随着扫描器的迅速增多，训练有素的专业人员的供应未能跟上，这使得自动化PET/CT报告生成(PETRG)变得越来越重要，以减少临床工作负担。与结构成像(如X射线、CT和MRI)相比，功能性PET带来独特的挑战：代谢模式与示踪剂生理学有关，需要全身3D上下文信息，而不是局部区域的解释。
### Innovation
提出了一个端到端的3D双分支框架PETRG-3D，用于PETRG，该框架分别编码PET和CT体积，并集成风格适应提示以最小化跨医院报告实践的差异性。构建了PETRG-Lym多中心淋巴瘤数据集，包含来自四个医院的824份报告和245,509对PET/CT切片。此外，还构建了带新专家编写和临床验证报告的AutoPET-RG-Lym公开PETRG基准。提出了PETRG-Score评估协议，以评估PETRG的临床价值。
### Conclusion
实验表明，PETRG-3D在自然语言度量标准(如ROUGE-L +31.49%)和临床有效性指标(PET-All +8.18%)方面显著优于现有方法，强调了体积双模态建模和风格觉知提示的好处。整体而言，这项工作为未来的特定PET/CT模型奠定了基础，这些模型强调疾病意识推理和临床可靠性评估。相关代码、模型和AutoPET-RG-Lym将被公开发布。
## 501. `cs.CV` - 基于非规则采样纵向数据流形映射的阿尔茨海默病进展预测 [PDF](https://arxiv.org/pdf/2511.20154), [HTML](https://arxiv.org/abs/2511.20154)
### Authors
Xin Hong,Ying Shi,Yinhao Li,Yen-Wei Chen
### Background
临床检查结果的不确定性导致纵向影像数据观察间隔不规则，这对疾病的建模提出挑战。现有的基于影像的疾病预测模型在欧几里得空间下运行，假设数据的平坦表示，并不能完全捕捉到非规则采样纵向影像中的内在连续性和非线性几何结构。研究背景是对非规则采样结构性磁共振成像(sMRI)数据阿尔茨海默病(AD)进展进行建模的挑战。
### Innovation
提出了一种流形映射、时间感知流形神经常微分方程(time-aware manifold Neural ordinary differential equation, TNODE)和基于注意力的黎曼门控循环单元(Attention-based riemannian Gated recurrent unit, ARGRU)框架。该方法首先将从高维度sMRI中提取的特征投影到流形空间，以保持疾病进展的内在几何结构。基于此表示，时间感知神经常微分方程模型了观测之间的潜在状态的连续演变，而基于注意力的黎曼门控循环单元可适变整合历史和当前信息以处理不规则间隔。这种联合设计提高了时间一致性，能够稳健地预测AD的发展轨迹。
### Conclusion
研究成果表明，所提出的方法在疾病状态预测和认知分数回归方面都优于最先进的模型。消融研究验证了每个模块的贡献，强调了它们在提高预测准确性方面的互补作用。模型的表现稳定，不受序列长度和缺失数据率变化的影响，显示出强大的时间泛化能力。跨数据集验证进一步证实了其稳健性和在不同临床设置中的应用性。
## 502. `cs.CV` - 使用神经形态硬件实现完全集成、低功耗、事件驱动的眼球中心追踪 [PDF](https://arxiv.org/pdf/2511.20175), [HTML](https://arxiv.org/abs/2511.20175)
### Authors
Federico Paredes-Valles,Yoshitaka Miyatani,Kirk Y. W. Scheper
### Background
眼球追踪在众多应用中至关重要，但要在可穿戴平台中实现稳健、高频次且超低功耗的眼球追踪依然颇具挑战。虽然事件驱动的视觉传感器可以提供微秒级分辨率和稀疏的数据流，但是至今缺乏能够提供即时推理能力的完全集成的低功耗处理解决方案。
### Innovation
本文提出了首款便携式、可穿戴的眼球中心追踪系统，实现了眼球追踪的完全集成，结合了事件驱动传感和神经形态处理技术，并使用高性能的Speck2f片上系统和低功耗微控制器上的轻量级坐标解码。系统包括一种新颖的具有时间解码门控的不确定性量化脉冲神经网络，该网络针对严格的存储器和带宽约束进行了优化。同时，通过系统的部署机制缩小了实际差距。
### Conclusion
本文演示了能够实现双眼稳定追踪并每眼平均功耗低于5毫瓦的可穿戴设备原型，其采用了双神经形态设备实现了100 Hz的稳定双眼追踪。研究证明，端到端的神经形态计算能够实现下一代节能可穿戴系统的实用、始终开启的眼球追踪功能。
## 503. `cs.CV` - Exo2EgoSyn: Unlocking Foundation Video Generation Models for Exocentric-to-Egocentric Video Synthesis [PDF](https://arxiv.org/pdf/2511.20186), [HTML](https://arxiv.org/abs/2511.20186)
### Authors
Mohammad Mahdi,Yuqian Fu,Nedko Savov,Jiancheng Pan,Danda Pani Paudel,Luc Van Gool
### Background
现有的视频生成模型，例如WAN 2.2，展示了出色的文本和图像条件合成能力，但仍然局限于固定视角生成设置。
### Innovation
本文提出了Exo2EgoSyn，这是WAN 2.2的一个改进版本，它解锁了从旁观者视角（Exocentric）到第一人称视角（Egocentric）的跨视角视频合成。该框架包含三个关键模块：Ego-Exo View Alignment（EgoExo-Align）确保旁观者视角和第一人称视角第一帧的潜空间对齐；Multi-view Exocentric Video Conditioning（MultiExoCon）将多视角的旁观者视角视频聚合为一个统一的条件信号；Pose-Aware Latent Injection（PoseInj）将旁观者视角到第一人称视角的相对相机姿态信息注入潜状态，引导几何感知的视点间合成。
### Conclusion
Exo2EgoSyn使得利用第三方观察生成高质量的第一人称视角视频不再是重新训练任务，同时也证明了Exo2EgoSyn显著改进了Ego2Exo合成，为使用基础模型实现可扩展的跨视角视频生成铺平了道路。
## 504. `cs.CV` - ADNet: 跨380个真实世界类别的大规模且可扩展的多领域异常检测基准 [PDF](https://arxiv.org/pdf/2511.20169), [HTML](https://arxiv.org/abs/2511.20169)
### Authors
Hai Ling,Jia Guo,Zhulin Tao,Yunkang Cao,Donglin Di,Hongyan Xu,Xiu Su,Yang Song,Lei Fan
### Background
现有的异常检测基准（例如MVTec-AD，共有15类）只涵盖了狭窄的类别范围，限制了跨场景泛化和可扩展性的评估。本论文旨在开发一个包含380个类别、跨电子、工业、农业食品、基础设施和医疗领域的大型多域异常检测基准ADNet，以解决这一问题。
### Innovation
ADNet提出了一个包括380个类别的大规模多域异常检测基准，该基准来自49个公开数据集。此外，该研究还提出了一种名为Dinomaly-m的方法，这是一种基于上下文的Mixture-of-Experts扩展，可在不增加推理成本的情况下扩展解码器容量，从而提高异常检测的性能。
### Conclusion
ADNet提供了一个标准化且可扩展的基准，支持社区扩展跨领域异常检测数据集，并为未来的异常检测基础模型提供了可扩展的基础。实验结果表明，现有的最先进的方法在一个对其它情况不敏感的设置下达到了90.6%的I-AUROC，但在多类情况下降至78.5%。而Dinomaly-m则达到了83.2%的I-AUROC和93.1%的P-AUROC，显示了其优越的性能。
## 505. `cs.CV` - SKEL-CF: Coarse-to-Fine Biomechanical Skeleton and Surface Mesh Recovery [PDF](https://arxiv.org/pdf/2511.20157), [HTML](https://arxiv.org/abs/2511.20157)
### Authors
Da Li,Ji-Ping Jin,Xuanlong Yu,Wei Liu,Xiaodong Cun,Kai Chen,Rui Fan,Jiangang Kong,Shen Xi
### Background
现有的参数化3D人体模型，如SMPL，在人体姿态和形状估计方面取得了显著进展，但它们简化的人体运动机制限制了生物力学的真实感。最近提出的SKEL模型通过使用解剖学准确的骨骼重新构建SMPL模型来解决这个问题。然而，直接估计SKEL参数仍然具有挑战性，因为数据集训练数据有限，透视不确定性以及人体关节运动的内在复杂性。
### Innovation
本文引入了SKEL-CF，一种细化到粗略化的框架，用于SKEL参数估计。SKEL-CF采用了基于转换器的编码器-解码器架构，其中编码器预测粗略的相机和SKEL参数，解码器在后续层逐步细化它们。为了确保解剖学上的一致性监督，本文将现有的基于SMPL的数据集4DHuman转换为SKEL对齐版本，4DHuman-SKEL，为SKEL姿态估计提供高质量的训练数据。此外，为了缓解深度和尺度的不确定性，本文在SKEL-CF管道中明确纳入了摄像机建模，并展示了其重要性。经过广泛的实验验证了设计的有效性。
### Conclusion
SKEL-CF在MOYO数据集上实现了85.0 MPJPE / 51.4 PA-MPJPE，显著优于之前的SKEL基最先进的HSMR（104.5 / 79.6），确立了SKEL-CF作为一种可扩展且解剖学上忠实的人体运动分析框架，将计算机视觉与生物力学之间的差距弥合。代码可在项目页面：this https URL ，获取。
## 506. `cs.CV` - OmniAlpha：一种统一多任务RGBA序列到序列生成框架 [PDF](https://arxiv.org/pdf/2511.20211), [HTML](https://arxiv.org/abs/2511.20211)
### Authors
Hao Yu,Jiabo Zhan,Zile Wang,Jinglin Wang,Huaisong Zhang,Hongyu Li,Xinrui Chen,Yongxian Wei,Chun Yuan
### Background
生成模型在RGB合成方面表现出色，但在实际应用中需要进行RGBA操控。目前，专门处理alpha的单任务模型虽然能够处理alpha，但缺乏灵活性；统一的多任务框架则受限于RGB领域。为解决这一问题，本文提出OmniAlpha，这是一种统一且能够处理顺序到顺序的RGBA图像生成和编辑的多任务生成框架。
### Innovation
OmniAlpha采用MSRoPE-BiL，这是一种新颖的方向扩展双向层轴的RoPE方法，适配于其Diffusion Transformer（DiT）骨架，能够同时处理多个输入和目标RGBA层。同时还引入了AlphaLayers，这是一个包含1000个高质多层三重组合的新数据集，基于新自动化合成和过滤流水线构建。通过在全面的21种不同任务的全方位培训上联合训练OmniAlpha，大量实验显示我们的统一方法在多项任务上均优于专门的强基准。特别地，OmniAlpha在AIM-500上的无遮罩细化中实现了相对减少84.8%的SAD，并在图层条件下的完成中赢得了超过90%的人类偏好。
### Conclusion
我们的工作证明了统一且多任务的模型能够学习到更好的RGBA共享表示，为更强大的层感知生成系统奠定了基础。
## 507. `cs.CV` - GHR-VQA: Graph-guided Hierarchical Relational Reasoning for Video Question Answering [PDF](https://arxiv.org/pdf/2511.20201), [HTML](https://arxiv.org/abs/2511.20201)
### Authors
Dionysia Danai Brilli,Dimitrios Mallis,Vassilis Pitsikalis,Petros Maragos
### Background
传统的基于像素的方法在视频问答(VQA)中无法有效地捕捉视频序列中复杂的人-物交互。现有方法通常缺乏对视频中行为和互动的有效分解和理解。
### Innovation
提出了一种基于图的层次关系推理框架GHR-VQA，该框架利用场景图来捕捉视频中的细微人-物交互。通过将每一帧表示为场景图，并在不同帧之间链接人类节点，形成了全局层级图。这种方法通过图神经网络处理这些图，生成丰富的上下文感知嵌入，以提高处理效率。最后，这些嵌入与问题特征在多层次网络中结合，增强了视频内容的局部和全局理解。
### Conclusion
在AGQA数据集上验证了该方法，结果显示该方法相对于现有技术在物体-关系推理上取得了显著的性能提升，提高了7.3%。
## 508. `cs.CV` - SFA: Scan, Focus, and Amplify toward Guidance-aware Answering for Video TextVQA [PDF](https://arxiv.org/pdf/2511.20190), [HTML](https://arxiv.org/abs/2511.20190)
### Authors
Haibin He,Qihuang Zhong,Juhua Liu,Bo Du,Peng Wang,Jing Zhang
### Background
视频文本视觉问答（Video TextVQA）任务旨在通过利用视频中的文本信息来回答关于视频的问题。这项任务具有显著的挑战性，要求模型准确地感知和理解在不同帧中变化的大小、方向和清晰度的场景文本，并有效结合时间信息和语义语境来生成精确的答案。此外，模型必须识别与问题相关的关键文本线索，过滤掉冗余或与问题无关的信息，以确保答案由最相关的信息引导。
### Innovation
提出了SFA（Scan, Focus, and Amplify），一种不需要训练的框架和第一个旨在用于Video TextVQA的Video-LLM方法，受人类回答问题的过程启发。SFA通过自适应扫描视频帧、选择性地聚焦于关键区域并直接放大它们，有效地将Video-LLM的注意力引导到关键线索上，从而使模型能够生成更准确的答案。
### Conclusion
SFA在多个公共的Video TextVQA数据集上取得了新的最佳结果，并显著超过了之前的现有方法，证明了其有效性和泛化能力。
## 509. `cs.CV` - 使用随机掩码增强实现稳健的3D脑MRI修补 [PDF](https://arxiv.org/pdf/2511.20202), [HTML](https://arxiv.org/abs/2511.20202)
### Authors
Juexin Zhang,Ying Weng,Ke Chen
### Background
为了减缓数据集偏差对深度学习模型在脑肿瘤MRI定量分析中的限制，建立了ASNR-MICCAI BraTS-Inpainting挑战。
### Innovation
提出了一个新颖的基于U-Net架构的深度学习框架，用于合成3D扫描中的健康组织。该方法通过随机掩码增强策略以提高泛化能力。
### Conclusion
该方法在验证集上的性能表现为SSIM为0.873±0.004，PSNR为24.996±4.694，MSE为0.005±0.087，并且在最终在线测试集上达到了SSIM为0.919±0.088，PSNR为26.932±5.057，RMSE为0.052±0.026，最终在BraTS-Inpainting 2025挑战中夺冠，超越了2023和2024年的获胜解决方案。
## 510. `cs.CV` - V-Attack: Targeting Disentangled Value Features for Controllable Adversarial Attacks on LVLMs [PDF](https://arxiv.org/pdf/2511.20223), [HTML](https://arxiv.org/abs/2511.20223)
### Authors
Sen Nie,Jie Zhang,Jianxin Yan,Shiguang Shan,Xilin Chen
### Background
现有针对大型视觉-语言模型（LVLMs）的对抗性攻击，从简单的任务特定模型的预测破坏发展到更复杂的图像语义操控目的。然而，现有的方法在可控性和精确操控特定图像概念的语义方面效果有限。这主要归因于对抗性攻击通常操作的补丁-标记表示中的语义纠缠：视觉编码器中的自我注意力聚合的全局语境主导了个体补丁特征，使得它们不适合精确的局部语义操控。
### Innovation
本文提出了一种名为V-Attack的新方法，利用transformer注意力块中计算的价值特征进行精细的局部语义操控。V-Attack通过抑制全局语境通道，保留高熵的、去纠缠的局部语义信息。该方法包括两个核心组件：（1）自我价值增强模块，用于细化内在的语义丰富度；（2）文本引导价值操控模块，利用文本提示定位源概念并优化为目标概念。通过绕过纠缠的补丁特征，V-Attack实现了高度有效的语义控制，实验结果表明，在不同LVLMs上的攻击成功率平均提高了36%。
### Conclusion
我们通过广泛实验验证了V-Attack的有效性，并揭示了现代视觉-语言理解中的关键漏洞。我们的代码和数据可以在指定的网址获得。
## 511. `cs.CV` - PromptMoG: 通过提示嵌入混合正态分布采样增强长提示图像生成的多样性 [PDF](https://arxiv.org/pdf/2511.20251), [HTML](https://arxiv.org/abs/2511.20251)
### Authors
Bo-Kai Ruan,Teng-Fang Hsiao,Ling Lo,Yi-Lun Wu,Hong-Han Shuai
### Background
近期，通过大规模校正流模型实现了从文本到图像（T2I）生成的显著视觉效果。然而，这些模型在长文本提示下的行为尚未得到充分探索。长文本提示可以编码丰富的内容、空间和风格信息，虽然提升了图像的保真度，但往往减少了多样性，导致生成的内容重复且创造力不足。
### Innovation
本文系统地研究了保真度和多样性的困境，并揭示出最先进的模型随着提示长度的增加，其多样性会明显下降。为了实现一致的评估，作者引入了LPD-Bench，一个专门用于评估长提示生成的保真度和多样性的基准。并通过分析，提出了一个理论框架，通过提示重新表述增加采样熵，以及提议了一种无需训练的方法PromptMoG，该方法在嵌入空间中从混合高斯分布中采样提示嵌入来提升多样性同时保留语义。
### Conclusion
广泛的实验证明，PromptMoG在四种最先进的模型（SD3.5-Large、Flux.1-Krea-Dev、CogView4和Qwen-Image）上能够一致地提高长提示生成的多样性，而不会导致语义漂移。
## 512. `cs.CV` - Zoo3D：场景级别零样本3D物体检测 [PDF](https://arxiv.org/pdf/2511.20253), [HTML](https://arxiv.org/abs/2511.20253)
### Authors
Andrey Lemeshko,Bulat Gabdullin,Nikita Drozdov,Anton Konushin,Danila Rukhovich,Maksim Kolodiazhnyi
### Background
3D物体检测对于空间理解非常重要。现实世界环境需要能够识别各种前所未见物体的模型，这仍然是闭集方法的主要限制。现有的开放词汇3D检测器虽放松了标注需求，但仍依赖训练场景，无论是点云还是图像。本文通过引入Zero-Shot 3D物体检测框架Zoo3D，进一步提升了这一领域。
### Innovation
Zoo3D是一个无需训练的3D物体检测框架，其通过使用基于2D实例掩码的图聚类构建3D边界框，然后通过带有最佳视角选择和视图一致掩码生成的新型开放词汇模块分配语义标签。Zoo3D有两种模式：零样本Zoo3D$_0$模式，无需任何训练，以及自我监督Zoo3D$_1$模式，通过使用Zoo3D$_0$生成的伪标签对无类别检测器进行微调来改进3D盒子的预测。此外，Zoo3D还能直接处理和未处理姿势的图像。
### Conclusion
在ScanNet200和ARKitScenes基准测试中，零样本Zoo3D$_0$和自我监督Zoo3D$_1$均实现了开放词汇3D物体检测的领先结果。零样本Zoo3D$_0$在所有现有自我监督方法中表现出色，展示了训练免费、即用型方法在实际3D理解中的强大和适应性。
## 513. `cs.CV` - XiCAD: Da Vinci Xi 用户界面中的摄像头激活检测 [PDF](https://arxiv.org/pdf/2511.20254), [HTML](https://arxiv.org/abs/2511.20254)
### Authors
Alexander C. Jenke,Gregor Just,Claas de Boer,Martin Wagner,Sebastian Bodenstedt,Stefanie Speidel
### Background
机器人辅助微创手术依赖于内窥镜视频作为术中唯一的视觉反馈。达芬奇Xi系统在其用户界面（UI）上叠加了图形用户界面，以指示每个机器臂的状态，包括内镜臂的激活状态。检测这种激活提供了有关摄像头移动信息等有价值的元数据，可以支持包括工具跟踪、技能评估或摄像头控制自动化在内的下游手术数据科学任务。
### Innovation
开发了一个基于ResNet18卷积神经网络的轻量级管道，用于自动识别达芬奇Xi UI中摄像头瓷砖的位置及其激活状态。该模型通过对SurgToolLoc数据集手动标注的数据进行微调，并在三个公共数据集上进行了评估，涵盖了超过70,000个帧。
### Conclusion
提出的管道能够可靠、实时地从手术视频中提取摄像头激活元数据，促进不同的下游应用的自动化前置处理和分析。所有的代码、训练模型和注解都是公开可用的。
## 514. `cs.CV` - 提升乒乓球运动：一种稳健的、面向真实世界的3D轨迹和旋转估计应用 [PDF](https://arxiv.org/pdf/2511.20250), [HTML](https://arxiv.org/abs/2511.20250)
### Authors
Daniel Kienzle,Katja Ludwig,Julian Lorenz,Shin'ichi Satoh,Rainer Lienhart
### Background
从普通单目视频中精确获取乒乓球的3D运动是一个挑战性的问题，因为现有的方法在合成数据上训练，难以适应真实世界中噪音多且不完美的乒乓球和台面检测结果。这是因为真实世界的视频缺乏3D地面真实轨迹和旋转标注。
### Innovation
提出了一种新颖的两阶段管道，将问题分为前端感知任务和后端2D到3D提升任务。前端组件使用从新创建的TTHQ数据集中获得的大量2D监督训练，后端提升网络则仅在物理正确的合成数据上训练。特别地，重新设计了提升模型以抵抗常见的真实世界伪影，如丢失检测和变化的帧率。通过将球检测器和台面关键点检测器整合进来，使方法从概念验证的提升方法转化为实际、稳健且高性能的端到端3D乒乓球轨迹和旋转分析应用。
### Conclusion
该研究提出了一种新颖的方法，能够从普通单目视频中准确提取3D乒乓球轨迹和旋转信息，适用于真实世界的应用场景，并且通过合理的训练和模型设计改进，确保了方法的稳健性和高性能。
## 515. `cs.CV` - 利用离散扩散分类建模提升图像分类 [PDF](https://arxiv.org/pdf/2511.20263), [HTML](https://arxiv.org/abs/2511.20263)
### Authors
Omer Belhasin,Shelly Golan,Ran El-Yaniv,Michael Elad
### Background
图像分类虽然是计算机视觉中的一个成熟任务，但在高不确定性条件下（如输入图像被破坏或训练数据有限），仍然充满挑战。传统分类方法通常直接从输入图像预测类别标签，但在一些特殊场景下可能会导致性能不佳。
### Innovation
该论文提出了离散扩散分类建模（DiDiCM）这种新颖的方法框架，利用基于扩散的机制来建模在给定输入图像时的类标签后验分布。DiDiCM 支持在类概率或离散类标签上的扩散预测，提供在计算和内存之间灵活权衡的选择。
### Conclusion
我们通过全面的实验研究证明了DiDiCM优于标准分类器。在ImageNet数据集上，少量的扩散迭代即可提高分类准确性，且在任务难度增加时准确率提升更加明显。
## 516. `cs.CV` - HistoSpeckle-Net：基于互信息的深层次学习方法实现复杂器官AMNIST图像的高保真重建 [PDF](https://arxiv.org/pdf/2511.20245), [HTML](https://arxiv.org/abs/2511.20245)
### Authors
Jawaria Maqbool,M. Imran Cheema
### Background
现有的基于深度学习的多模光纤（MMF）成像方法通常专注于简单的数据集，这限制了它们在处理复杂、真实世界成像任务方面的应用。这些模型通常需要大量数据支持，当处理多样化和复杂图像时，这一挑战更为明显。
### Innovation
本文提出了一种名为HistoSpeckle-Net的深度学习架构，专门用于从MMF散斑中重建富含结构的医学图像。该模型引入了一种基于分布的学习策略，并采用直方图相关互信息损失增强模型鲁棒性，减少了对大数据集的依赖。此外，HistoSpeckle-Net加入了直方图计算单元，用于估算平滑的边际和联合直方图以计算互信息损失，并且包含独特的三层特征细化模块，以实现多尺度结构相似度指数（SSIM）损失的计算。
### Conclusion
在复杂器官AMNIST数据集上的实验表明，HistoSpeckle-Net在图像重建保真度方面优于基线模型如U-Net和Pix2Pix。即使在训练样本有限且光纤摆动条件变化的情况下，该模型也能表现出更优的性能。通过有效在减少数据的情况下重建复杂的解剖特征并能应对光纤扰动，HistoSpeckle-Net将MMF成像推向了在现实临床环境中实际部署的可能性。
## 517. `cs.CV` - 面向现实伪装图像生成的可控制语言引导扩散 [PDF](https://arxiv.org/pdf/2511.20218), [HTML](https://arxiv.org/abs/2511.20218)
### Authors
Yuhang Qian,Haiyan Chen,Wentong Li,Ningzhong Liu,Jie Qin
### Background
伪装图像生成（CIG）是一个新兴的研究领域，关注于合成物体与环境和谐融合且视觉上一致的图像。现有方法通过将对象融合到选定背景中或通过前景对象引导的超分辨率来实现CIG，但往往因为忽略了伪装对象与背景环境之间的逻辑关系而难以获得自然的结果。
### Innovation
提出了一种名为CT-CIG的可控文本引导伪装图像生成方法，利用大型视觉语言模型（VLM）设计了一个伪装揭示对话机制（CRDM）来注释现有的伪装数据集，并使用构造的图像-提示对微调Stable Diffusion，引入轻量级控制器来引导伪装对象的位置和形状，提高伪装场景的适宜性。此外，设计了一个频率相互作用精炼模块（FIRM）来捕捉高频纹理特征，以辅助学习复杂的伪装模式。
### Conclusion
通过广泛的实验，包括CLIPScore评估和伪装效果评估，证明了生成的文本提示与CT-CIG在语义上的对齐，以及CT-CIG生成照片级真实伪装图像的能力。
## 518. `cs.CV` - 以图像自身为奖励：使用对抗奖励的图像生成强化学习 [PDF](https://arxiv.org/pdf/2511.20256), [HTML](https://arxiv.org/abs/2511.20256)
### Authors
Weijia Mao,Hao Chen,Zhenheng Yang,Mike Zheng Shou
### Background
在图像生成的强化学习（RL）中，一个可靠且有效的奖励函数对于生成高质量的图像至关重要。当前大多数RL方法依赖于预训练的偏好模型，这些模型输出标量奖励以近似人类偏好。然而，这些奖励经常无法准确捕捉人类感知，并且容易受到奖励挖掘的影响，即更高的奖励分数并不一定意味着更好的图像质量。
### Innovation
为解决上述问题，本文提出了Adv-GRPO，这是一种使用对抗奖励的RL框架，该框架能够迭代更新奖励模型和生成器。与KL正则化限制参数更新不同，我们学习到的奖励可以直接通过视觉输出引导生成器，从而生成高质量的图像。此外，本文还使用图像本身作为奖励，并结合参考图像和视觉基础模型（如DINO）提供丰富的视觉奖励，这些密集的视觉信号而非单一的标量奖励能在图像质量、美学和任务特定指标上带来一致的提升。
### Conclusion
实验结果表明，在人类评估中，本文的方法在图像质量和美学方面分别实现了70.0%和72.4%的胜率。同时，结合了参考样本和基础模型奖励的方法能够实现分布迁移和灵活的风格定制。此外，代码和模型已经对外开放。
## 519. `cs.CV` - 多模态平衡合作蒸馏用于多模态域泛化 [PDF](https://arxiv.org/pdf/2511.20258), [HTML](https://arxiv.org/abs/2511.20258)
### Authors
Xiaohan Wang,Zhangtao Cheng,Ting Zhong,Leiting Chen,Fan Zhou
### Background
Weight Averaging (WA) 的广泛应用以及在优化过程中形成的平滑损失景观对泛化能力的提升。然而，直接将 WA 应用于多模态域泛化（MMDG）中时，由于不同模态间优化速度的差异，WA 在早期阶段会对快速收敛的模态进行过度拟合，削弱了更慢但互补模态的贡献，进而影响有效的模态融合，使损失曲面向更尖锐、不那么泛化的极值偏移。
### Innovation
提出了一个统一的协作蒸馏框架 MBCD（Modality-Balanced Collaborative Distillation），该框架在保留 WA 诱发平坦性优势的同时，克服了其在多模态情境下的不足。MBCD 通过学生模型的自适应模态dropout减轻早期对主导模态的偏见，并通过梯度一致性约束使单模分支的学习信号与融合表示保持一致，促进了协调的优化过程。最终，基于 WA 的教师进行跨模态蒸馏，通过将融合知识传递到每个单模分支来加强跨模态互动并引导收敛至更平坦的解决方案。
### Conclusion
在 MMDG 基准测试上的广泛实验表明，MBCD 一致地超越了现有方法，在不同未知领域中表现出更优的准确性和鲁棒性。
## 520. `cs.CV` - 基于对比学习的编码器在胶质母细胞瘤亚区域分段方面的研究 [PDF](https://arxiv.org/pdf/2511.20221), [HTML](https://arxiv.org/abs/2511.20221)
### Authors
Juexin Zhang,Qifeng Zhong,Ying Weng,Ke Chen
### Background
胶质母细胞瘤是一种具有显著分子和病理异质性的恶性脑肿瘤，这给诊断和患者分层带来了极大的挑战。虽然传统的组织病理学评估仍然是标准方法，但深度学习为进行客观和自动化的全切片图像分析提供了有前景的途径。针对BraTS-Path 2025挑战，团队开发了一种方法，利用预训练的Vision Transformer（ViT）编码器和专用分类头对官方训练数据集进行微调。
### Innovation
在BraTS-Path 2025挑战中，团队使用了基于对比学习的编码器来实现胶质母细胞瘤亚区域的分类。通过在Synapse平台上评估的在线验证集上，模型实现了0.7064的Matthews相关系数（MCC）和0.7676的F1分数。最终测试集上，模型达到了0.6509的MCC和0.5330的F1分数，并最终获得了挑战的第二名。这表明基于ViT的病理分析有很大的潜力。
### Conclusion
团队的结果为基于ViT的组织病理学分析设定了一个坚实的基础，未来的研究将侧重于弥合在未知验证数据上观察到的性能差距。
## 521. `cs.CV` - DRL-Guided Neural Batch Sampling for Semi-Supervised Pixel-Level Anomaly Detection [PDF](https://arxiv.org/pdf/2511.20270), [HTML](https://arxiv.org/abs/2511.20270)
### Authors
Amirhossein Khadivi Noghredeh,Abdollah Safari,Fatemeh Ziaeetabar,Firoozeh Haghighi
### Background
工业视觉检测中的异常检测具有挑战性，因为缺陷样本稀缺。现有方法多依赖于仅使用正常数据进行无监督重建，这常常导致过拟合和对细微缺陷的检测效果差。
### Innovation
提出了一种半监督深度强化学习框架，该框架结合了神经批处理样本器、自动编码器和预测器。基于强化学习的样本器通过复合奖励实现探索与利用的平衡，适应性地选择信息性的片段。自动编码器生成损失轮廓，突出异常区域，预测器在损失轮廓空间内执行分割。该交互机制使得系统能够在有限标记数据的情况下有效学习正常和缺陷模式。
### Conclusion
实验展示了本方法在MVTec AD数据集上具有更高的准确性和对细微异常的更好定位效果，同时保持低复杂度。相较于最新的前沿方法，F1_max平均提高0.15，AUC提高0.06，最高F1_max提高0.37。
## 522. `cs.CV` - SelfMOTR: 重新审视MOTR模型的自我生成检测先验 [PDF](https://arxiv.org/pdf/2511.20279), [HTML](https://arxiv.org/abs/2511.20279)
### Authors
Fabian Gülhan,Emil Mededovic,Yuli Wu,Johannes Stegmaier
### Background
尽管利用变压器架构取得了端到端跟踪的进展，但检测性能差以及联合架构中检测与关联之间的冲突仍然是关键问题。最近的方法通过(i)采用先进的去噪或标签分配策略，或者(ii)通过蒸馏或锚点建议技术从外部对象检测器引入检测先验来缓解这些问题。尽管如此，MOTR等模型实际上具有强大的检测能力。
### Innovation
引入了SelfMOTR，这是一种新型的跟踪变压器，依赖于自我生成的检测先验。该研究通过广泛的分析和消融研究，揭示了MOTR等模型的潜在检测能力，并提供了利用这些能力的实用工具。
### Conclusion
在DanceTrack数据集上，SelfMOTR达到了很强的性能，与其竞争最近的端到端跟踪方法。
## 523. `cs.CV` - 多人一次稀疏视角CT重建中的 Lipschitz 限制网络引导 [PDF](https://arxiv.org/pdf/2511.20296), [HTML](https://arxiv.org/abs/2511.20296)
### Authors
Baoshun Shi,Ke Jiang,Qiusheng Lian,Xinran Yu,Huazhu Fu
### Background
尽管深度学习在稀疏视角CT重建（SVCT）方面取得了显著进展，但仍存在两个主要限制：（i）由于其经验性设计，难以明确证明深度展开算法中的先验网络满足Lipschitz约束；（ii）每种视角需要训练一个独立模型带来的存储成本问题，这妨碍了临床应用。
### Innovation
该研究提出了一个可以明确证明满足Lipschitz约束的网络，称为LipNet，并引入了一个明确提示模块，可以提供不同的稀疏采样设置的区分性知识，使可以在单个模型中处理多种稀疏视角配置。此外，该研究开发了一种存储节省的深度展开框架，称为PromptCT，将LipNet嵌入其先验网络，保证其相应迭代算法的收敛性。
### Conclusion
在模拟和真实数据实验中，PromptCT表现出优于基准重建算法的性能，实现了高质量重建，同时降低了存储成本。从理论上，明确证明了LipNet满足边界属性，进一步证明其Lipschitz连续性，并分析了所提出的迭代算法的收敛性。相关数据和代码可公开获得。
## 524. `cs.CV` - TaCo: 在遥感变化检测中捕捉时空语义一致性 [PDF](https://arxiv.org/pdf/2511.20306), [HTML](https://arxiv.org/abs/2511.20306)
### Authors
Han Guo,Chenyang Liu,Haotian Zhang,Bowen Chen,Zhengxia Zou,Zhenwei Shi
### Background
遥感变化检测(RSCD)旨在跨双时相卫星图像识别表面变化。大多数先前的方法仅依赖掩码监督，虽然有效指导了空间定位，但对时间语义转换的约束有限。因此，它们常常产生空间上一致的预测，但仍然存在未解决的语义不一致性。
### Innovation
提出了一款时空语义一致性网络TaCo，它通过时空语义联合约束增强了现有的掩码监督框架。引入了文本引导的过渡生成器，将文本语义与双时相视觉特征结合以构建跨时相过渡特征。此外，提出了一种时空语义联合约束，包括双向重构约束和过渡约束：前者强制重建特征与原始特征对齐，后者增强变化的区分能力。这种设计可以在预测时无需增加任何计算开销，同时提供显著的性能提升。
### Conclusion
在六项公开数据集上的广泛实验中，TaCo在包含二分类和语义变化检测任务在内的所有数据集上都实现了SOTA性能。
## 525. `cs.CV` - 通过VLM引导的迭代自我完善促进物理接地视频生成 [PDF](https://arxiv.org/pdf/2511.20280), [HTML](https://arxiv.org/abs/2511.20280)
### Authors
Yang Liu,Xilin Zhao,Peisong Wen,Siran Dai,Qingming Huang
### Background
近期在视频生成方面的进展已经在视觉质量方面取得了显著成果，但当前的模型仍然难以生成符合现实物理原理的结果。
### Innovation
提出了一个迭代自我完善的框架，该框架利用大型语言模型和视觉-语言模型来提供物理感知的指导以改进视频生成。引入了多模式链式思考（MM-CoT）过程，根据物理不一致性的反馈逐步改进生成质量。该方法无需训练且插件即用，适用于广泛范围的视频生成模型。实验结果表明，该方法将物理-IQ分数从56.31提高到62.38。
### Conclusion
希望这项工作为物理一致的视频生成提供初步探索，并可能为未来的研究提供参考。
## 526. `cs.CV` - DAPointMamba: 域自适应点云Mamba用于点云完成 [PDF](https://arxiv.org/pdf/2511.20278), [HTML](https://arxiv.org/abs/2511.20278)
### Authors
Yinghui Li,Qianyu Zhou,Di Shao,Hao Yang,Ye Zhu,Richard Dazeley,Xuequan Lu
### Background
Domain adaptive point cloud completion (DA PCC) 的目标是在标记的源域和未标记的目标域之间缩小几何和语义的差异。现有的方法要么因使用CNNs或视觉Transformer而面临有限的感受野和平方复杂度的问题。为解决这一问题，我们研究了状态空间模型（SSMs）在DA PCC中的适应性，并发现直接将SSMs应用于DA PCC会遇到许多挑战：直接按顺序排列3D点云往往破坏了目标域的空间拓扑和局部几何特征。此外，忽视学习域无关表示的设计限制了适应性性能。
### Innovation
我们提出了一种新的框架DAPointMamba，它具有的优点是全局感受野和高效的一次性复杂性。DAPointMamba包括三个新颖的模块：Cross-Domain Patch-Level Scanning 引入了局部几何对应关系，实现了有效的局部对齐；Cross-Domain Spatial SSM Alignment 通过基于跨域相似性调节片段特征，进一步加强了空间一致性，有效缓解了细微结构差异；Cross-Domain Channel SSM Alignment 主动解决全局语义差距，通过交错排列特征通道。
### Conclusion
在合成和真实基准上的广泛实验表明，我们的DAPointMamba在较低的计算复杂性和推理延迟下，比现有最先进的方法有更好的性能。
## 527. `cs.CV` - ScenarioCLIP: 预训练可移植的视觉语言模型和行动基因数据集用于自然场景分析 [PDF](https://arxiv.org/pdf/2511.20274), [HTML](https://arxiv.org/abs/2511.20274)
### Authors
Advik Sinha,Saurabh Atreya,Aashutosh A V,Sk Aziz Ali,Abhijit Das
### Background
尽管现有的CLIP类型模型主要专注于图像检索或单个对象的分类，以及根据文本描述检索图像嵌入，但实际场景图片包含丰富的对象间关系和动作结构。虽然CLIP基线文献中的最新方法通过挖掘更难的图像-文本反例对和细化永久文本提示等方式提升了类别的区分度，但这些方法仍然局限于预定义的类别列表，未能显式建模对象间的关系和结构。尽管PyramidCLIP开始解决这一问题，但仍缺乏对对象间关系的显式建模。因此，针对这一点，作者提出了ScenarioCLIP模型，它不仅接受输入文本和图像，还接受标注的关系和突出显示的关系区域，从而能够更好地进行场景分析。
### Innovation
提出了一种新的模型ScenarioCLIP，该模型接受输入文本、标注的关系以及图像的感兴趣区域作为输入，以便更好地处理多对象和动作的自然场景。此外，该模型通过预训练在精心策划的场景数据集上，并适用于专门的下游任务，如跨模态检索和细粒度视觉理解。为了弥补领域特定数据集的缺乏，作者通过扩展现有室内和室外场景数据集中的图像-文本对来生成新的数据集，并使用现有语言模型进行手动和自动整理。作者还建立了一个全面的基准测试套件，以评估模型在各种领域的表现，并展示了模型在零样本和微调性能上的优越性。
### Conclusion
ScenarioCLIP模型在多种基于场景的任务上表现出色，无论是零样本还是微调性能都表现出良好的鲁棒性。模型已经在预训练阶段用于特定领域，并在专门的下游任务上进行了微调。作者还发布了模型代码和数据集，以供其他研究者使用和验证。
## 528. `cs.CV` - TReFT: Taming Rectified Flow Models For One-Step Image Translation [PDF](https://arxiv.org/pdf/2511.20307), [HTML](https://arxiv.org/abs/2511.20307)
### Authors
Shengqian Li,Ming Gao,Yi Liu,Zuzeng Lin,Feng Wang,Feng Dai
### Background
Rectified Flow (RF)模型通过最优传输理论实现了高质量的图像和视频合成，但在应用于图像到图像翻译时，仍依赖于昂贵的多步骤去噪过程，阻碍了实时应用。尽管最近的对抗训练范式CycleGAN-Turbo在预训练的扩散模型中实现了单步图像翻译，但将其直接应用到RF模型中会导致严重的收敛问题。
### Innovation
本文分析了这些挑战，并提出了一种名为TReFT的新方法，用于Tame Rectified Flow模型的一步图像翻译。TReFT直接利用预训练DiT或UNet预测的速度作为输出，这种简明而有效的设计在对抗训练和单步推断下解决了收敛问题。该设计主要由一个新颖的观察激发，即，在去噪过程即将结束时，预训练RF模型预测的速度收敛到从原点到最终干净图像的向量。
### Conclusion
预训练的RF模型使用TReFT微调后，在多个图像翻译数据集上的性能与最新方法相当，同时能够实现实时推断。此外，作者在训练期间引入了内存高效的潜变量环路一致性和身份损失，并简化了架构，以加快推理速度。
## 529. `cs.CV` - IrisNet: Infrared Image Status Awareness Meta Decoder for Infrared Small Targets Detection [PDF](https://arxiv.org/pdf/2511.20319), [HTML](https://arxiv.org/abs/2511.20319)
### Authors
Xuelin Qian,Jiaming Lu,Zixuan Wang,Wenxuan Wang,Zhongling Huang,Dingwen Zhang,Junwei Han
### Background
红外小目标检测（IRSTD）面临诸多挑战，如低信噪比、复杂的背景及目标特征不明显。尽管基于深度学习的编码-解码架构在IRSTD领域取得了进展，但它们的静态模式学习在不同场景（如日夜变化、天空/海洋/地面领域）下的模式漂移问题限制了检测的稳健性。
### Innovation
提出了一个名为IrisNet的新型元学习框架，该框架能够动态适应输入的红外图像状态来进行检测策略的调整。IrisNet通过一张包含红外图像特征与全部解码器参数动态映射关系的图像到解码器变换器实现这一目标。具体来说，IrisNet将参数化解码器表示为保持层次层间相关性的结构化2D张量，并允许变换器通过自注意力模型层间的依赖性，同时通过交叉注意力自动生成适应性的解码模式。此外，为了进一步增强红外图像的感知能力，IrisNet还整合了高频率成分来补充目标位置和场景边缘信息。
### Conclusion
在NUDT-SIRST、NUAA-SIRST和IRSTD-1K数据集上的实验结果表明，IrisNet在IRSTD方面具有优越性，达到了最先进的性能。
## 530. `cs.CV` - ShelfRectNet: 使用 homography 估计进行单视角货架图像校正 [PDF](https://arxiv.org/pdf/2511.20335), [HTML](https://arxiv.org/abs/2511.20335)
### Authors
Onur Berk Tore,Ibrahim Samil Yalciner,Server Calap
### Background
单视角货架图像校正对于零售行业而言是一个重要的任务，因为货架监控和产品对齐通常只需要单一视角的数据。从不同角度拍摄的货架图像无法直接用于监控和对齐，因此需要通过估计单张图片中的 homography 矩阵来进行校正。
### Innovation
本文提出了一种基于深学习的框架，通过预测四点参数化的 homography 矩阵来校正任意角度拍摄的货架图像。该模型采用 ConvNeXt 作为骨干网络以提高特征表示能力，并采用归一化坐标回归以提升稳定性。为了应对数据稀缺问题并促进泛化，引入了合成 homography 模型和采样策略的新型数据增强方法。
### Conclusion
实验结果显示，该方法在测试集上达到了 1.298 像素的均方角误差，与传统的计算机视觉方法和基于深度学习的方法相比，该方法在准确性和推理速度方面表现相当。这些结果表明我们的方法是一种在实际应用场景中稳健且高效的单视角校正解决方案。为了促进进一步的研究，我们将提供数据集 ShelfRectSet 和代码。
## 531. `cs.CV` - VKnowU: 评估多模态LLM中的视觉知识理解 [PDF](https://arxiv.org/pdf/2511.20272), [HTML](https://arxiv.org/abs/2511.20272)
### Authors
Tianxiang Jiang,Sheng Xia,Yicheng Xu,Linquan Wu,Xiangyu Zeng,Limin Wang,Yu Qiao,Yi Wang
### Background
虽然多模态大型语言模型（MLLMs）已经擅长识别物体，但它们往往缺乏对世界基本物理和社会原则的直观、人类理解的掌握。这种高层的视知觉与推理之间的桥梁，我们称之为视觉知识，是一个现有MLLMs中未被充分开发的领域。论文旨在系统性地评估这一能力。
### Innovation
论文提出了一个全面的基准测试VKnowU，包含1249个视频中的1680个问题，覆盖8种核心类型的视觉知识，如直观物理和主观意图等。此外，还引入了新的数据集VKnowQA和基准模型VideoKnow+，后者明确规定了视觉知识的融入，并采用强化学习和视觉知识奖励，显著提升了模型在多个评估基准上的表现。
### Conclusion
研究强调视觉知识是开发能够更广泛地理解我们物理和社会世界的多模态LLM的关键缺失环节。VideoKnow+模型展示了在包含结构化的观看-思考-回答过程以及引入视觉知识奖励机制，显著提高了模型的性能，在多种评估基准上取得了持续的进步。
## 532. `cs.CV` - GS-Checker: 3D高斯斑点图中篡改定位 [PDF](https://arxiv.org/pdf/2511.20354), [HTML](https://arxiv.org/abs/2511.20354)
### Authors
Haoliang Han,Ziyuan Luo,Jun Qi,Anderson Rocha,Renjie Wan
### Background
近年来，3D高斯斑点图（3DGS）编辑技术的进步使得3D场景的操控变得简单。然而，这也引发了关于3D内容潜在恶意篡改的关注。为了防止这些恶意应用，定位篡改区域变得至关重要。
### Innovation
本文提出了一种新颖的方法——GS-Checker，用于在3DGS模型中识别篡改区域。该方法通过将3D篡改属性整合到3D高斯参数中，标示高斯是否被篡改。此外，设计了一种3D对比机制，通过比较3D高斯键属性的相似性来寻找3D级别的篡改线索，并引入了一种循环优化策略来细化3D篡改属性，以提高篡改定位的准确性。特别的是，该方法不需要昂贵的3D标签作为监督。
### Conclusion
大量的实验结果证明了我们提出的GS-Checker方法能够有效地定位3DGS区域的篡改部分。
## 533. `cs.CV` - 基于材料信息的高斯泼溅在数字孪生3D世界重建中的应用 [PDF](https://arxiv.org/pdf/2511.20348), [HTML](https://arxiv.org/abs/2511.20348)
### Authors
João Malheiro Silva,Andy Huynh,Tong Duy Son,Holger Caesar
### Background
三维重建在数字孪生中通常依赖于基于LiDAR的方法，这种方法可以提供精确的几何信息，但缺乏通过相机自然捕获的语义和纹理。传统的LiDAR-相机融合方法需要复杂的校准步骤，且难以处理像玻璃这样的材料，虽然这种材料在图像中可见，但在点云中却表现不佳。
### Innovation
本文提出了一种仅使用相机的方法，使用多视图图像进行3D高斯销毁重建，通过视觉模型提取语义材料遮罩，将高斯表示转换为具有投影材料标签的网格表面，并为现代图形引擎和模拟器中的准确传感器仿真分配基于物理的材料属性。该方法结合了逼真的重建和基于物理的材料分配，提供了与LiDAR-相机融合方法相媲美的传感器仿真精度，同时消除了硬件复杂性和校准需求。
### Conclusion
本文通过内部测试车辆的内部数据集验证了仅使用相机的方法，利用LiDAR作为反射率验证的参考，结合图像相似性度量。该方法在数字孪生的3D世界重建中具有较高精度的传感器仿真能力，同时避免了传统LiDAR-相机融合方法的复杂校准和硬件依赖性。
## 534. `cs.CV` - 从被动感知到主动记忆：基于粗粒度标注的弱监督图像操纵定位框架 [PDF](https://arxiv.org/pdf/2511.20359), [HTML](https://arxiv.org/abs/2511.20359)
### Authors
Zhiqing Guo,Dongdong Xi,Songlin Li,Gaobo Yang
### Background
图像操纵定位（IML）面临一个基本权衡，即减少注释成本与实现细致化定位精度之间的矛盾。现有完全监督的IML方法依赖于密集的像素级掩码注释，这限制了它们在大型数据集或真实世界环境中的扩展性。相比之下，大多数现有的弱监督IML方法依赖于图像级别标签，这大大减少了注释工作量，但通常缺乏精确的空间定位。
### Innovation
本文提出了BoxPromptIML，一种新的弱监督IML框架，有效平衡了注释成本和定位性能。具体来说，提出了一种粗粒度区域注释策略，可以在较低成本下生成相对准确的掩码。为了提高模型效率并促进部署，设计了一个高效的轻量级学生模型，通过基于SAM的固定教师模型的知识蒸馏，学习进行细致化定位。此外，受到人类潜意识记忆机制的启发，特征融合模块采用了双重引导策略，主动地用实时观察线索增强再现原型模式，而不是被动地提取特征，这使长期记忆适应当前图像的具体上下文，从而显著提高了定位精度和鲁棒性。
### Conclusion
广泛的实验结果表明，BoxPromptIML在同分布和异分布数据集上不仅优于或匹配完全监督模型，而且具有很强的泛化能力、低廉的注释成本和高效的部署特性。
## 535. `cs.CV` - 360°思考：野生环境下的人形视觉搜索 [PDF](https://arxiv.org/pdf/2511.20351), [HTML](https://arxiv.org/abs/2511.20351)
### Authors
Heyang Yu,Yinan Han,Xiangyu Zhang,Baiqiao Yin,Bowen Chang,Xiangyu Han,Xinhao Liu,Jing Zhang,Marco Pavone,Chen Feng,Saining Xie,Yiming Li
### Background
人类依赖头部（cephalomotor）和眼部（oculomotor）的协同控制，在360度环境中高效地搜索视觉信息。然而，现有的视觉搜索方法通常限于静态图像，忽视了身体实体与其与三维世界的互动。如何开发出不受现实世界硬件限制、能与人类相媲美的实体视觉搜索代理？为此，本文提出了一种人形视觉搜索方法，该方法中的人形代理主动转动头部，以在由360度全景图表示的沉浸式环境中搜索物体或路径。针对视觉拥挤的真实世界场景，本文构建了H* Bench（一种新基准），它超越了家庭场景，涵盖了大型零售空间、公共交通枢纽、城市街道和公共机构等更具挑战性的野外场景，这些场景需要先进的视觉-空间推理能力。
### Innovation
本文提出了人形视觉搜索方法，其中人形代理主动旋转头部进行搜索；构建了H* Bench基准，以处理更具挑战性的野外场景；使用后训练技术增强了开源Qwen2.5-VL模型，显著提高了物体和路径搜索的成功率；强调路径搜索特有的难度，归因于对复杂空间常识的需求。
### Conclusion
实验结果表明，即使顶级专有模型在物体和路径搜索上的成功率也只有约30%，而使用后训练技术增强的开源Qwen2.5-VL模型，其成功率提高了几倍。研究结果揭示了一个有希望的发展方向，同时也量化了在构建能够无缝集成到日常生活中的人工智能代理方面的巨大挑战。
## 536. `cs.CV` - Back to the Feature: Explaining Video Classifiers with Video Counterfactual Explanations [PDF](https://arxiv.org/pdf/2511.20295), [HTML](https://arxiv.org/abs/2511.20295)
### Authors
Chao Wang,Chengan Che,Xinyue Chen,Sophia Tsoka,Luis C. Garcia-Peraza-Herrera
### Background
现有的视觉反事实解释方法主要针对图像分类器进行设计，但生成视频分类器的反事实视频仍是一个很大程度上未被探索的领域。反事实视频需要具备物理合理性、时间一致性以及平滑的运动轨迹才能真正具有实用性。现有的基于图像的反事实方法无法生成时间一致、平滑且物理合理的视频反事实。
### Innovation
提出了一种名为Back To The Feature (BTTF)的优化框架，用于生成视频反事实。该方法引入了两个新的特性，即优化方案以根据输入视频的第一帧检索初始潜入噪声，以及两阶段优化策略以在输入视频附近搜索反事实视频。同时引入了逐步优化策略以加速收敛。
### Conclusion
通过在Shape-Moving、MEAD和NTU RGB+D等视频数据集上的广泛实验表明，BTTF能有效生成有效、视觉相似且现实的反事实视频，为理解分类器的决策机制提供了具体的见解。
## 537. `cs.CV` - VGGTFace：在野生环境中的拓扑一致面部几何重建 [PDF](https://arxiv.org/pdf/2511.20366), [HTML](https://arxiv.org/abs/2511.20366)
### Authors
Xin Ming,Yuxuan Han,Tianyu Huang,Feng Xu
### Background
数字角色创建的工作流程需要构建topologically consistent（拓扑一致）的面部几何。现有的方法要么需要繁琐的手动努力，要么难以推广到在野外收集的数据，要么受到3D Morphable Models（3D形态可变模型）表达能力的限制。
### Innovation
本文提出了一种自动化的方法VGGTFace，它利用3D基础模型VGGT，从日常用户拍摄的多视角图像中自动生成拓扑一致的面部几何。主要创新点包括：1) 通过结合Pixel3DMM增加拓扑信息；2) 引入Topology-Aware Bundle Adjustment策略，通过Laplacian能量优化点云融合。
### Conclusion
该方法在单个NVIDIA RTX 4090 GPU上10秒内可实现16视角的高质量重建，实验结果展示了在基准测试中的顶级性能，并且具有强大的野外数据推广能力。源代码已公开。
## 538. `cs.CV` - 带有PID-CNN的双眼视觉目标3D运动感知 [PDF](https://arxiv.org/pdf/2511.20332), [HTML](https://arxiv.org/abs/2511.20332)
### Authors
Shi Jiazhao,Pan Pan,Shi Haotian
### Background
本文训练了一个用于感知双眼视觉目标三维运动信息的网络，可以提供实时的三维坐标、速度和加速度，具有基本的空间-时间感知能力。从PID的角度理解神经网络适应非线性问题的能力。将单层神经网络视为使用二阶差分方程和非线性描述局部问题。多层网络通过多次这种组合逐步将原始表示转换为所需表示。
### Innovation
设计了一个相对较小的PID卷积神经网络，总共17层和413,000个参数。通过简单的连接和池化实现了实用的功能复用方法。使用随机移动球的模拟数据集对网络进行了训练和测试，实验结果表明预测精度接近输入图像分辨率可表示的上限。分析了实验结果、误差以及现有不足和改进方向。讨论了高维卷积在提高计算效率和特征空间利用方面的优势，以及使用PID信息实现记忆和注意力机制的潜在优势。
### Conclusion
通过PID-CNN网络能够实现双眼视觉目标的三维运动感知，具有较高的预测精度，并讨论了高维度卷积和PID信息应用的实际效果及改进方向。
## 539. `cs.CV` - 无需训练的注意力调整和空间控制多个体自定义方法 [PDF](https://arxiv.org/pdf/2511.20401), [HTML](https://arxiv.org/abs/2511.20401)
### Authors
Jiawei Lin,Guanlong Jiao,Jianjin Xu
### Background
多ID自定义在计算机视觉领域是一个引人关注的话题，最近吸引了广泛的关注。多ID自定义的目标是给定多个个体的身份验证图像，生成一个无缝融合各个身份的同时保留独立身份的自定义图像。相比于单ID自定义，多ID自定义更具挑战性，主要面临两个主要挑战：模型在推断过程中容易出现拼贴问题，导致生成的图像质量下降；文本控制能力较弱，生成结果简单地将多人合并到一张图像上，不考虑文本输入和多个人的对齐情况。
### Innovation
本文提出了一种无需训练的方法MultiID，通过调整注意力机制和空间控制来实现多ID自定义。关键创新点在于使用ID解耦交叉注意力机制，将不同的ID嵌入注入对应图像区域，从而生成多ID输出。另外，提出三种策略增强生成可控性：局部提示、深度引导空间控制和扩展自我注意，使结果更符合文本提示和ID图像。
### Conclusion
大量定性和定量结果表明，MultiID在解决上述两个挑战方面具有有效性。其性能与基于训练的方法相当甚至更好。
## 540. `cs.CV` - FREE: 注意不确定性自回归并行扩散变压器 [PDF](https://arxiv.org/pdf/2511.20390), [HTML](https://arxiv.org/abs/2511.20390)
### Authors
Xinwan Wen,Bowen Li,Jiajun Luo,Ye Li,Zhi Wang
### Background
扩散变压器（DiTs）生成质量达到最佳，但由于需要长序列去噪轨迹，导致推断延迟较高。最近的推测推理方法通过画师-验证者方案在基于U-Net的扩散模型中实现了无损并行采样，但这些方法在DiTs上的加速效果有限，因为验证阶段的画师准确性不足。
### Innovation
我们研究了DiTs的特征动态，发现顶层变压器层的特征具有强时间一致性和丰富的语义抽象。基于此，我们提出了FREE，一个使用轻量级画师执行特征级自回归并行验证的新框架，确保在理论上和实验上实现无损加速。此外，为了缓解在后期去噪步骤中DiTs预测方差（不确定性）增加带来的接受率降低问题，我们引入了一种基于不确定性的放松策略，形成FREE（放松），该策略动态调整接受概率以响应不确定性水平。
### Conclusion
在ImageNet-512²上的实验表明，FREE实现了最多1.86倍的加速，而FREE（放松）进一步达到2.25倍的提速，同时保持高感知和定量的生成质量。
## 541. `cs.CV` - AMB3R：使用后台的准确的前馈米尺度3D重建 [PDF](https://arxiv.org/pdf/2511.20343), [HTML](https://arxiv.org/abs/2511.20343)
### Authors
Hengyi Wang,Lourdes Agapito
### Background
本文提出了AMB3R，一个用于密集3D重建的多视角前馈模型，适用于多种3D视觉任务。其核心思想是采用稀疏且紧凑的体素化场景表示作为后台，这使得可以在空间紧凑的情况下进行几何推理。模型仅针对多视角重建进行训练，但在无需专门微调或测试时优化的情况下，可以无缝扩展到无标定的视觉惯性里程计或大规模结构从运动。该模型的性能在相机姿态、深度和米尺度估计，3D重建上优于之前的基于点云的方法，并且在常见基准测试中甚至超过了具有密集重建先验的基于优化的SLAM和SfM方法。
### Innovation
AMB3R模型的关键创新在于采用稀疏且紧凑的体素化场景表示作为后台，这使得在空间紧凑的情况下进行几何推理成为可能。模型仅需为多视角重建进行训练，但可以无缝扩展到无标定的视觉惯性里程计或大规模结构从运动，而无需任务特定的微调或测试时的优化。与基于点云的模型相比，本方法在相机姿态估计、深度估计、米尺度估计和3D重建上实现了最先进的性能。甚至在某些情况下，它的性能超越了基于优化的SLAM和SfM方法。
### Conclusion
AMB3R方法通过采用稀疏紧凑的体素化场景表示作为后台，实现了一种高效的前馈式3D重建方案，适用于多种3D视觉任务。模型在常用的基准测试中表现出色，其性能超越了现有的点云基模型以及基于优化的SLAM和SfM方法，特别是具有密集重建先验的情况。
## 542. `cs.CV` - 基于路径采样对的连续时间一致性的无图像时间步蒸馏 [PDF](https://arxiv.org/pdf/2511.20410), [HTML](https://arxiv.org/abs/2511.20410)
### Authors
Bao Tang,Shuai Zhang,Yueting Zhu,Jijun Xiang,Xin Yang,Li Yu,Wenyu Liu,Xinggang Wang
### Background
时间步蒸馏是一种有效的方法，用于提高扩散模型的生成效率。一致性模型（CM）作为一种基于轨迹的框架，由于其强大的理论基础和高质量的少量步骤生成而表现出巨大潜力。然而，目前的连续时间一致性蒸馏方法仍然高度依赖于训练数据和计算资源，这在资源受限的场景中限制了它们的部署，并限制了它们在多样领域中的扩展。
### Innovation
本文提出了一种新的方法，称为轨迹反向一致性模型（TBCM），通过直接从教师模型的生成轨迹中提取潜在表示来消除对外部训练数据的依赖，不再需要VAE编码和大规模数据集，从而显著提高了效率和简化了蒸馏过程。此外，通过路径提取样本自然地填补训练分布与推理分布之间的差距，从而实现了更有效的知识迁移。
### Conclusion
实验结果显示，TBCM在一次生成下实现了6.52 FID和28.08 CLIP分数，与Sana-Sprint相比训练时间减少了约40%，并且节省了大量的GPU内存。这表明在不牺牲质量的情况下提高了效率。此外，作者还揭示了连续时间一致性蒸馏中的扩散生成空间差异，并分析了采样策略如何影响蒸馏性能，为未来的蒸馏研究提供了见解。
## 543. `cs.CV` - AD-R1：使用公平世界模型的闭环强化学习进行端到端自主驾驶 [PDF](https://arxiv.org/pdf/2511.20325), [HTML](https://arxiv.org/abs/2511.20325)
### Authors
Tianyi Yan,Tao Tang,Xingtai Gui,Yongkang Li,Jiasen Zhesng,Weiyao Huang,Lingdong Kong,Wencheng Han,Xia Zhou,Xueyang Zhang,Yifei Zhan,Kun Zhan,Cheng-zhong Xu,Jianbing Shen
### Background
端到端的自动驾驶模型有潜力直接从传感器数据中学习复杂的行为，但存在安全性和应对稀有事件的重大挑战。强化学习（RL）为克服这些局限提供了潜力，但在自动驾驶领域的应用却收效甚微。论文指出，RL 进展受阻的根本原因是用于 RL 的世界模型存在根深蒂固的乐观偏差。因此，本文提出了一种基于公平世界模型的后训练策略优化框架。
### Innovation
本文的主要贡献在于，引入了一个公平世界模型的框架，通过一种新颖的数据合成管道——反事实合成，系统地生成了一系列可能的碰撞和离路事件，确保了模型能够准确预测行动结果之间的因果关系。此外，通过将这种公平世界模型整合到闭环 RL 框架中，并将其用作内部批评家，代理可通过查询批评家来推测候选行动的潜在结果。研究结果表明，该模型在新风险预见基准测试中显著优于基线，显著减少了挑战性模拟中的安全违规行为。
### Conclusion
通过训练模型‘想象’危险，可以显著提高自动驾驶的安全性和智能性，从而有助于构建真正安全和智能的自主代理。
## 544. `cs.CV` - StableTrack：在低频率检测中稳定多对象跟踪 [PDF](https://arxiv.org/pdf/2511.20418), [HTML](https://arxiv.org/abs/2511.20418)
### Authors
Matvei Shelukhan,Timur Mamedov,Karina Kvanchiani
### Background
多对象跟踪(MOT)是计算机视觉中最具挑战性的任务之一，要求正确检测对象并在多个帧之间关联这些检测结果。现有方法主要专注于视频流中每一帧的跟踪，这在计算资源有限的条件下几乎不可能实现。
### Innovation
我们提出了StableTrack，一种新颖的方法以稳定低频率检测下的跟踪质量。该方法引入了一种新的两阶段匹配策略，以提高低频率检测之间的跨帧关联。通过结合对象再识别模型和重定位距离，提出了新的边界框匹配方法。此外，将视觉跟踪整合进了卡尔曼滤波器以及整体跟踪流水线。
### Conclusion
StableTrack方法在低频率检测情况下表现优于现有的最先进跟踪器，在MOT17-val上HOTA提高了11.6%，同时在标准MOT17、MOT20和DanceTrack基准测试中保持了与最佳方法相当的性能。
## 545. `cs.CV` - CrossEarth-Gate: Fisher-Guided Adaptive Tuning Engine for Efficient Adaptation of Cross-Domain Remote Sensing Semantic Segmentation [PDF](https://arxiv.org/pdf/2511.20302), [HTML](https://arxiv.org/abs/2511.20302)
### Authors
Shilei Cao,Ziyang Gong,Hehai Lin,Yang Liu,Jiashun Cheng,Xiaoxing Hu,Haoyuan Liang,Guowen Li,Chengwei Qin,Hong Cheng,Xue Yang,Juepeng Zheng,Haohuan Fu
### Background
在遥感(RS)领域，基于精简参数微调（PEFT）已成为激活基础模型在下游任务中广泛应用的泛化表示能力的关键方法。然而，现有的专门PEFT方法在应用于大规模地球观测任务时往往失效，因为它们难以全面处理RS数据中固有的多元和不可预测的领域差异，包括空间、语义和频率变化。
### Innovation
本文提出了CrossEarth-Gate，这是一种适应跨域遥感语义分割的Fisher引导自适应调优引擎。该方法贡献了两个主要方面：一是建立了涵盖空间、语义和频率模块的全面RS模块工具箱，以解决多元领域的差距；二是开发了一种Fisher信息引导的自适应选择机制，在该工具箱上运行。该机制通过Fisher信息量度每个模块的重要性，并动态激活关键模块，以优化适应效果和效率。
### Conclusion
全方位的实验验证了CrossEarth-Gate的有效性和泛化能力，该方法在16个跨域基准上的遥感语义分割任务中实现了最佳性能。研究结果表明，通过建立综合RS模块工具箱和开发Fisher信息引导的选择机制，可以有效地解决跨域遥感数据中的领域差距问题，并显著提高模型的适应效果和效率。
## 546. `cs.CV` - 重要的地方看哪里：无需训练的高分辨率遥感CVQA通过自适应缩放搜索 [PDF](https://arxiv.org/pdf/2511.20460), [HTML](https://arxiv.org/abs/2511.20460)
### Authors
Yunqi Zhou,Chengjie Jiang,Chun Yuan,Jing Li
### Background
随着卫星星座、传感器技术和成像流水线的发展，超高分辨率遥感影像变得越来越普遍。然而，目前的遥感基础模型并不适用于这种输入：整幅图像编码会耗尽标记和内存预算，而基于重新采样的预处理会使关键的微细信息丢失。
### Innovation
ZoomSearch是一个无需训练、即插即用的管道，它将'看什么'与'如何回答'分离。ZoomSearch结合了自适应多分支缩放搜索（Adaptive Multi-Branch Zoom Search），它在图像块上执行层次搜索以定位查询相关信息的区域，以及布局感知的块重组（Layout-Aware Patch Reassembly），它重新组织所选的块以创建一个紧凑且布局忠实的画布。
### Conclusion
ZoomSearch在LLaVA-ov集成时，在多个任务上达到最先进的准确度，分别在LRS-VQA和MME-RealWorld-RS基准上提高了26.3%和114.8%。同时，ZoomSearch在推理效率方面也表现出色，比先前的基于搜索的方法快20%到44%。
## 547. `cs.CV` - 从文本描述生成人类-人类-物体交互的学习 [PDF](https://arxiv.org/pdf/2511.20446), [HTML](https://arxiv.org/abs/2511.20446)
### Authors
Jeonghyeon Na,Sangwon Baik,Inhee Lee,Junyoung Lee,Hanbyul Joo
### Background
人类之间的互动方式在不同情境下差异显著，包括人际距离、空间布局和运动等。为了使机器能够理解这些复杂的、依赖于上下文的行为，有必要将多人在周围场景中的相互关系进行建模。本文提出了一个新的研究问题，即建模参与共有物体的两个人之间的交互关系，称之为人类-人类-物体交互（HHOIs）。由于缺乏专门针对HHOIs的数据集，本文提供了一个新捕获的HHOIs数据集和一种利用图像生成模型合成HHOIs数据的方法。通过中间步骤，获得了个人的人-物交互（HOIs）和人-人交互（HHIs），并使用这些数据训练了基于评分扩散模型的文本到HOI和文本到HHI模型。最后，提出了一种统一的生成框架，将两个独立模型整合在一起，实现一次高级采样过程即可生成完整的HHOIs。本方法将HHOI生成扩展到多人场景，支持超过两个个体的交互。
### Innovation
本文提出了HHOIs（人类-人类-物体交互）这一新的研究问题，并开发了用于合成HHOIs的数据集和生成模型。通过将个人的人-物交互（HOIs）和人-人交互（HHIs）分解，并利用评分扩散模型训练文本到HOI和文本到HHI模型，本文进一步发展了统一的生成框架。研究结果表明，该方法能够在文本描述的条件下生成更为真实和复杂的HHOIs，超越了仅关注个人人-物交互的先前方法，并且还应用于多人对象运动的生成。
### Conclusion
本文通过提供一个专门的HHOIs数据集和基于文本生成的模型，解决了人类-人类-物体交互的建模问题。所提出的方法能够生成多层次和复杂的HHOIs，并且已证明在多个实际应用场景中有潜力，如多个人与物体的交互合成。
## 548. `cs.CV` - 基于对象中心的视觉tokens精简方法 [PDF](https://arxiv.org/pdf/2511.20439), [HTML](https://arxiv.org/abs/2511.20439)
### Authors
Guangyuan Li,Rongzhen Zhao,Jinhong Deng,Yanbo Wang,Joni Pajarinen
### Background
在视觉语言模型（VLMs）中，视觉tokens的数量庞大但信息分散，相比之下语言tokens更具信息量且结构更紧凑，这两者之间存在不平衡。这导致视觉tokens在推理过程中消耗了大量的不必要的计算资源，降低了模型的效率。尽管已经存在的针对剪枝冗余视觉tokens的工作不断研究，但这些方法主要是间接的或无法保证的。现有方法尝试通过一些间接或不确定的方法来精简视觉tokens以提高推理效率，但未能直接保证保留那些最具代表性的tokens，从而保持模型的精度。
### Innovation
本文提出了OC-VTP方法，这是一个直接且可保证的方法，用于选择最具代表性的视觉tokens，以实现高效且精度保持的VLM推理。OC-VTP仅需要对一个小型对象中心视觉token剪枝器进行轻量级预训练，该剪枝器可以方便地插入现有的VLM中，而无需对任何模型进行fine-tuning或数据集调整。它通过最小化从选择的tokens重构原始未剪枝tokens的误差来保证保留最具代表性的tokens。无论视觉剪枝比率如何，即推断效率如何变化，OC-VTP均帮助主流VLMs保持最高的推理精度。此外，剪枝结果还展示了有趣的解释性。
### Conclusion
我们的研究证明了OC-VTP的有效性，它能够在不牺牲推断精度的前提下，有效提高VLMs的推理效率。我们提供的代码可以在指定链接处访问。
## 549. `cs.CV` - BRIC：在测试时连接运动计划与物理控制 [PDF](https://arxiv.org/pdf/2511.20431), [HTML](https://arxiv.org/abs/2511.20431)
### Authors
Dohun Lim,Minji Kim,Jaewoon Lim,Sungchan Kim
### Background
运动生成规划模型可以在文本和场景上下文中生成多样化的运动，但这些模型往往会产生物理上不合理的输出，导致模拟过程中执行出现偏差。
### Innovation
BRIC 提出了一种新颖的测试时自适应（TTA）框架，通过动态适应基于扩散的运动规划器和基于强化学习的物理控制器之间的执行差异，来解决长期人体运动生成中的问题。BRIC 结合了两个策略：通过损失函数防止灾难性遗忘，同时保留预训练技能；以及一种轻量级的测试时指导机制，无需更新扩散模型参数即可引导模型。
### Conclusion
BRIC 通过结合这两种策略，确保在多种环境中长期执行的连续性和物理合理性，实现多种长期任务（如运动合成、障碍物避开和人类与场景的交互）的最佳性能。
## 550. `cs.CV` - MajutsuCity：语言驱动的自适应美学城市生成与可控3D资产和布局 [PDF](https://arxiv.org/pdf/2511.20415), [HTML](https://arxiv.org/abs/2511.20415)
### Authors
Zilong Huang,Jun He,Xiaobin Huang,Ziyi Xiong,Yang Luo,Junyan Ye,Weijia Li,Yiping Chen,Ting Han
### Background
生成逼真的3D城市对于世界模型、虚拟现实和游戏开发至关重要。理想的都市场景需要同时满足风格多样性、细节精确度和可控性。然而，现有的方法在提供文本生成的创造性灵活性与通过显式结构表示实现的对象级可编辑性之间难以平衡。
### Innovation
引入了MajutsuCity，这是一个基于自然语言且美学自适应的框架，用于合成结构一致且风格多样的3D城市场景。MajutsuCity采用可控布局、资产和材料的组合方式，并通过四阶段流水线工作。此外，还集成了MajutsuAgent，这是一种交互式语言接地编辑代理，支持五类对象级操作，以增强可编辑性。为了支持真实感和可定制的场景合成，构建了MajutsuDataset，一个高质量的多模态数据集，包含语义布局、高度图、多样化3D建筑资产、PBR材料和天顶箱，以及详细的注释。同时，开发了一套实用的评估指标，涵盖结构一致性、场景复杂性、材料保真度和照明氛围等关键维度。
### Conclusion
广泛的实验表明，MajutsuCity在布局FID上比CityDreamer减少了83.7%，比CityCraft减少了20.1%。在所有评估指标中，我们的方法排名第一，显著优于现有方法。这些结果确认MajutsuCity在几何保真度、风格适应性和语义可控性方面是3D城市生成的新最先进的方法。我们希望框架能激发3D城市生成的新研究方向。我们的数据集和代码可以在以下地址获取：this https URL。
## 551. `cs.CV` - Block Cascading: Training Free Acceleration of Block-Causal Video Models [PDF](https://arxiv.org/pdf/2511.20426), [HTML](https://arxiv.org/abs/2511.20426)
### Authors
Hmrishav Bandyopadhyay,Nikhil Pinnaparaju,Rahim Entezari,Jim Scott,Yi-Zhe Song,Varun Jampani
### Background
现有的块因果视频生成在速度与质量之间存在明显的权衡：小型1.3B模型仅能以16 FPS运行，而大型14B模型则以4.5 FPS运行，这迫使用户在响应性和视频质量之间做出选择。
### Innovation
Block Cascading 通过无训练的并行化大幅度缓解了这种速度质量权衡。其核心见解是未来的视频块不必等待当前块完全去噪即可开始生成。通过利用来自前一个块的初步去噪上下文开始块生成，Block Cascading 将顺序的流水线转换为并行级联，使多个块能够同时去噪。利用5块GPU进行时间上的并行化，Block Cascading 在各种模型规模下实现了约2倍的加速：1.3B模型从16 FPS加速到30 FPS，14B模型从4.5 FPS加速到12.5 FPS。此外，Block Cascading 还消除了交互生成过程中上下文切换时从KV缓存重新获取的开销。
### Conclusion
广泛针对多个块因果流水线的评估显示，从块因果流水线转换到Block Cascading流水线进行推理时，生成质量没有显著损失。
## 552. `cs.CV` - DesignPref：捕捉视觉设计生成中的个人偏好 [PDF](https://arxiv.org/pdf/2511.20513), [HTML](https://arxiv.org/abs/2511.20513)
### Authors
Yi-Hao Peng,Jeffrey P. Bigham,Jason Wu
### Background
生成模型，如大型语言模型和文本到图像的扩散模型，越来越多地用于创建用户界面（UI）和演示文稿等视觉设计。对这些生成模型进行微调和基准测试常常依赖于人类标注的设计偏好数据集。然而，由于视觉设计的高度主观性和个性化特点，个人之间的偏好差异很大。
### Innovation
引入了DesignPref数据集，包含20名专业设计师标注的12000个UI设计生成的成对比较，具有多层次偏好评分。研究表明，经过训练的专业设计师之间存在显著的分歧（二元偏好Krippendorff's alpha = 0.25）。设计师提供的自然语言解释表明分歧源自不同对设计方面重要性的感知和个人偏好。利用DesignPref，研究人员证明传统的多数投票方法用于训练汇聚评判模型通常不能准确反映个人偏好。为应对这一挑战，研究探索了多个个性化策略，特别是在RAG管道中微调或纳入设计师特定注释。研究结果表明，个性化的模型在预测个人设计师的偏好方面始终优于聚合基准模型，即使使用20倍少的实例也是如此。这项工作首次提供了研究个性化视觉设计评估的数据集，并支持未来对建模个人设计品味的研究。
### Conclusion
关于个性化视觉设计评估的研究首次提出了DesignPref数据集，并展示了其对理解个体设计偏好和改善个性化模型预测能力的重要性，为未来研究提供了新的视角和技术支持。
## 553. `cs.CV` - AlignBench：使用合成图像-描述对衡量细粒度图像-文本对齐 [PDF](https://arxiv.org/pdf/2511.20515), [HTML](https://arxiv.org/abs/2511.20515)
### Authors
Kuniaki Saito,Risa Shinoda,Shohei Tanaka,Tosho Hirasawa,Fumio Okura,Yoshitaka Ushiku
### Background
评估像CLIP这样的图像-文本对齐模型对于连接视觉和语言表示至关重要。然而，现有的基准依赖于基于规则的扰动或简短的描述，限制了它们衡量细微对齐的能力。
### Innovation
引入了一个新的基准AlignBench，通过评估由各种图像-文本和文本-图像模型生成的详细图像-描述对来提供图像-文本对齐的新指标。每个句子都被注释为正确与否，可以直接评估VLMs作为对齐评估器的效果。
### Conclusion
对广泛基于解码器的VLMs的基准测试揭示了三个关键发现：（i）CLIP基础模型，即使是专为组合推理设计的，仍然几乎看不到；（ii）检测器系统地高估了早期句子的得分；（iii）它们表现出强烈的自我偏好，倾向于自己的输出并损害检测性能。
## 554. `cs.CV` - 模块化深度学习框架在辅助感知中的应用：注视、情感和演讲者识别 [PDF](https://arxiv.org/pdf/2511.20474), [HTML](https://arxiv.org/abs/2511.20474)
### Authors
Akshit Pramod Anchan,Jewelith Thomas,Sritama Roy
### Background
开发全面的辅助技术需要视觉和听觉感知的无缝集成。这项研究评估了一种模块化架构的可行性，这种架构受到感知系统核心功能如'Smart Eye'的启发。
### Innovation
提出了并基准测试了三个独立的传感模块：一个卷积神经网络（CNN）用于检测眼睛状态（嗜睡/注意力），一个深度CNN用于面部表情识别，以及一个长短期记忆（LSTM）网络用于语音识别。这些模型分别在Eyes Image、FER2013和自定义音频数据集上达到了93.0%、97.8%和96.89%的准确率。该研究证明了轻量级、细分领域的模型可以在离散任务中实现高保真度，为未来在资源受限的辅助设备中实现实时多模态集成奠定了验证基础。
### Conclusion
轻量级、领域特定的模型在离散任务中实现了高保真度，为未来在资源受限的辅助设备中实现实时多模态集成奠定了验证基础。
## 555. `cs.CV` - 使用语义分割对文化遗物进行自动化监控 [PDF](https://arxiv.org/pdf/2511.20541), [HTML](https://arxiv.org/abs/2511.20541)
### Authors
Andrea Ranieri,Giorgio Palmieri,Silvia Biasotti
### Background
文化遗存的保护需要自动化的裂缝检测技术，通过语义分割可以实现这一目标。乌尼特网络架构在像素级裂缝识别方面具有潜力，特别是在对雕像和纪念碑的裂缝检测中。
### Innovation
本文比较了不同卷积神经网络（CNN）编码器的U-Net架构在语义分割中的应用，使用了包括Mean Intersection over Union (mIoU)，Dice系数和Jaccard指数在内的多种评估指标。研究还基于OmniCrack30k数据集对裂缝进行测试，并通过现实世界的未标记样本进行了定性评价。
### Conclusion
研究表明，尽管没有专门针对雕像或纪念碑的裂缝进行训练，但不同基于卷积神经网络的编码器模型展现了良好的泛化能力，适用于不同文化遗存的具体环境。
## 556. `cs.CV` - New York Smells: 一个大型多模态数据集用于嗅觉 [PDF](https://arxiv.org/pdf/2511.20544), [HTML](https://arxiv.org/abs/2511.20544)
### Authors
Ege Ozguroglu,Junbang Liang,Ruoshi Liu,Mia Chiquier,Michael DeTienne,Wesley Wei Qian,Alexandra Horowitz,Andrew Owens,Carl Vondrick
### Background
嗅觉是动物感知世界的关键，但这一丰富的化学感知模式对机器来说仍然难以触及。一个主要瓶颈是缺乏在自然环境中收集的多样化多模态嗅觉训练数据。目前，现有的嗅觉数据集中的对象数量有限，而本研究旨在提供一个包含成千上万对图像和嗅觉信号的数据集，这些数据是在自然环境中采集的。
### Innovation
本研究发布了一个名为'New York Smells'的大规模多模态数据集，包含7000个嗅觉-图像配对，来自3500个不同的物体，涵盖室内外环境。该数据集含有的物体数量比现有嗅觉数据集多出约70倍。此外，本研究提出了基准测试，包括跨模态嗅觉-图像检索、仅通过嗅觉识别场景、物体和材料以及细粒度区分草种三个任务。
### Conclusion
通过使用本研究数据集上的实验，研究发现视觉数据能够促进跨模态的嗅觉表示学习，且所学的嗅觉表示优于常用的手工制作特征。
## 557. `cs.CV` - 为DSA序列中边界一致性和稳健动脉分割的物理导向损失函数 [PDF](https://arxiv.org/pdf/2511.20501), [HTML](https://arxiv.org/abs/2511.20501)
### Authors
Muhammad Irfan,Nasir Rahim,Khalid Mahmood Malik
### Background
大脑动脉的准确提取和分割对于开发可靠的临床管理模型以应对复杂的脑血管疾病至关重要。传统的损失函数通常仅依赖于像素级重叠度，忽略了血管边界的几何和物理一致性，导致动脉预测结果出现碎片化或不稳定现象。
### Innovation
为了克服这一限制，本文提出了一个名为Physics-Informed Loss (PIL)的新颖损失函数。该损失函数将预测边界和地面真值边界之间的相互作用建模为受材料物理学中的位错理论启发的弹性过程。这种形式化通过引入基于物理的正则化项来确保轮廓的平滑演化和结构一致性，使网络能够更好地捕捉血管的精细几何结构。PIL被集成到几种分割架构中，包括U-Net、U-Net++、SegFormer和MedFormer，并在两个公开基准DIAS和DSCA上进行了评估。
### Conclusion
实验结果表明，PIL始终优于传统的如交叉熵、Dice、活动轮廓和表面损失等损失函数，表现出更高的灵敏性和F1分数以及边界的一致性。这证实将基于物理的边界交互引入深度神经网络能提高动态血管造影成像中血管分割的精度和鲁棒性。
## 558. `cs.CV` - HBridge: H-Shape Bridging of Heterogeneous Experts for Unified Multimodal Understanding and Generation [PDF](https://arxiv.org/pdf/2511.20520), [HTML](https://arxiv.org/abs/2511.20520)
### Authors
Xiang Wang,Zhifei Zhang,He Zhang,Zhe Lin,Yuqian Zhou,Qing Liu,Shiwei Zhang,Yijun Li,Shaoteng Liu,Haitian Zheng,Jason Kuen,Yuehuan Wang,Changxin Gao,Nong Sang
### Background
 recent unified models combine understanding experts (如：大规模语言模型LLMs)与生成专家（如：扩散模型）的优势，实现了多模态性能的显著提升。然而，最近的先进方法如BAGEL和LMFusion采用混合变压器（Mixture-of-Transformers, MoT）范式，通过共享注意力机制对专家进行镜像设计，尽管便于初始化和融合，但依然存在由不同模态固有的差异导致的内在局限。
### Innovation
该论文提出了一种新的非对称H形架构HBridge，使得不同专家能够最优地利用其各自模态领域的预训练先验。与先前的密集融合策略不同，HBridge仅选择性地连接中间层，减少了超过40%的注意力共享，从而提高了效率并增强了生成质量。浅层和深层卷积层分别捕捉模态特定的表示，而中间层的桥梁则促进了语义对齐。此外，引入了语义重建标记来明确引导生成专家重建目标图像的视觉语义标记，进一步增强了跨模态一致性。
### Conclusion
在多个基准测试中进行的广泛实验表明HBridge的有效性和优越性能，确立了统一多模态生成的新范式。
## 559. `cs.CV` - Mistake Attribution: 细粒度自观视频中错误的理解 [PDF](https://arxiv.org/pdf/2511.20525), [HTML](https://arxiv.org/abs/2511.20525)
### Authors
Yayuan Li,Aadit Jain,Filippos Bellos,Jason J. Corso
### Background
在自观视频中的人类错误理解任务中，之前的大部分工作缺乏细粒度的输出。MATT（Mistake Attribution Task）具体地将错误归因于输入指示文本或尝试视频。MATT 确定指令被违反的部分（语义角色），错误不可逆转的时刻点（Point-of-No-Return，PNR），以及错误出现在PNR帧中的位置。
### Innovation
MATT 任务能够细粒度地理解人类在自观视频中的错误。通过开发 MisEngine，一种自动化数据生成引擎，可以从现有数据集中自动生成大量的标注丰富的错误样本。MisEngine 生成了 EPIC-KITCHENS-M 和 Ego4D-M 两个数据集，这些数据集比之前的错误数据集规模大大增加。MisFormer 是一种统一的基于注意力模型，能够在语义（what）、时间（when）和空间（where）维度上进行错误归因，通过 MisEngine 的监督进行了训练。实验结果表明，MisFormer 在新的数据集和之前基准测试中的表现优于强视频-语言、时间定位、手物交互和错误检测基线。
### Conclusion
MisEngine 和 MisFormer 提供了一种全新的方法，可以显著提升自观视频中细粒度错误理解的能力。通过 MisEngine 生成的大规模标注数据集，以及统一的基于注意力的错误归因模型 MisFormer，实现了在语义、时间、空间维度上的准确归因。实验结果表明，此方法在多个基准测试中均表现出色。
## 560. `cs.CV` - 使用Laban启发和频率域运动特征的舞种分类 [PDF](https://arxiv.org/pdf/2511.20469), [HTML](https://arxiv.org/abs/2511.20469)
### Authors
Ben Hamscher,Arnold Brosch,Nicolas Binninger,Maksymilian Jan Dejna,Kira Maag
### Background
舞是人类文化的重要组成部分，用于传达情感和讲述故事。根据运动数据识别和区分舞蹈种类是人类活动识别中的一个复杂问题，因为许多舞蹈风格共享相似的姿态、手势和时间运动模式。
### Innovation
提出了一种轻量级的框架，用于基于视频中提取的姿态估计确定运动特征来分类舞蹈风格。这些特征受劳伦运动分析的启发，捕捉上半身的局部关节动态如速度、加速度和角度运动，增强空间协调的结构化表示。进一步通过对运动模式的频率域特征进行傅里叶变换，编码运动的节奏和周期性方面。该方法无需复杂模型结构，通过低计算成本实现不同舞蹈风格的稳健分类，展示出可解释的运动表示可以有效捕捉风格特征。
### Conclusion
提出的这种方法通过低计算开销实现了不同舞蹈风格的稳健分类，表明可解释的运动表示能够有效捕捉艺术风格的细微差别。
## 561. `cs.CV` - PhysChoreo：基于部分感知语义接地的物理可控视频生成 [PDF](https://arxiv.org/pdf/2511.20562), [HTML](https://arxiv.org/abs/2511.20562)
### Authors
Haoze Zhang,Tianyu Huang,Zichen Wan,Xiaowei Jin,Hongzhi Zhang,Hui Li,Wangmeng Zuo
### Background
尽管最近的视频生成模型在视觉保真度方面取得了显著进展，但在物理可控性和合理性方面往往存在不足。为解决这一问题，近期有一些研究尝试使用基于物理渲染的方法来指导视频生成，但仍面临在长时间序列中准确建模复杂物理特性和有效控制物理行为的挑战。
### Innovation
本文提出了一种名为PhysChoreo的新框架，可以从单张图像生成具有多种可控性和物理真实性的视频。该方法分为两步：首先，通过部分感知物理属性重建来估计图片中所有对象的静态初始物理属性；其次，通过时间指导和物理可编辑的模拟，合成具有丰富动态行为和物理真实感的高质量视频。
### Conclusion
实验结果表明，PhysChoreo可以生成具有丰富动态行为和物理真实感的视频，并在多个评估指标上优于现有最佳方法。
## 562. `cs.CV` - STARFlow-V: 基于归一化流的端到端视频生成建模 [PDF](https://arxiv.org/pdf/2511.20462), [HTML](https://arxiv.org/abs/2511.20462)
### Authors
Jiatao Gu,Ying Shen,Tianrong Chen,Laurent Dinh,Yuyang Wang,Miguel Angel Bautista,David Berthelot,Josh Susskind,Shuangfei Zhai
### Background
归一化流（NFs）作为基于端到端似然比的连续数据生成模型，已在图像生成方面取得了明显进展。然而在视频生成领域，由于时空复杂度和计算成本更高，最先进的系统大多依赖于基于扩散的模型。本研究重新审视了这一设计空间，提出了一种基于归一化流的视频生成器STARFlow-V，具备端到端学习、稳健的因果预测以及原生概率估计等特点。
### Innovation
STARFlow-V 在时空潜在空间中操作，采用了全局-局部架构，从而限制了因果依赖性在全局潜在空间中，同时保持了丰富的帧内局部交互。为此设计了Flow-score匹配，一种轻量级因果去噪器，以实现自回归式的一致性视频生成。同时，采用了视频感知的雅可比迭代方法，提高采样效率，该方法重新定义了内部更新为可在不破坏因果性的情况下并行化的迭代。
### Conclusion
STARFlow-V实现了高质量的自回归视频生成，并与基于扩散的基线相比，在视觉保真度和时间一致性方面表现出色，展示了归一化流在构建世界模型方面的潜力，为构建基于世界模型的研究开辟了新的方向。代码和生成样本可以在该网址获得。
## 563. `cs.CV` - 统一多模态模型中的理解是否能指导生成？从分析到前进之路 [PDF](https://arxiv.org/pdf/2511.20561), [HTML](https://arxiv.org/abs/2511.20561)
### Authors
Yuwei Niu,Weiyang Jin,Jiaqi Liao,Chaoran Feng,Peng Jin,Bin Lin,Zongjian Li,Bin Zhu,Weihao Yu,Li Yuan
### Background
近年来，统一多模态模型取得了显著进展，但核心问题仍悬而未决：理解是否能够指导生成？为探究这一问题，该论文引入了UniSandbox，一种脱钩评估框架，结合了控制性、合成数据集，以避免数据泄露并允许详细分析。
### Innovation
论文提出了UniSandbox框架，这是一种脱钩评估框架，采用了控制性的合成数据集，以避免数据泄漏并促进详细的分析。研究结果揭示了一个理解-生成之间的重要差距，特别是在推理生成和知识迁移这两个关键维度上。此外，论文通过实验证明了显式的推理过程（CoT）在理解模块中的有效性和自训练方法在生成过程中内化这种能力的能力。
### Conclusion
UniSandbox为设计未来统一架构和训练策略提供了初步见解，旨在真正弥合理解与生成之间的差距。相关代码和数据可在指定链接处获取。
## 564. `cs.CV` - Wanderland: Geometrically Grounded Simulation for Open-World Embodied AI [PDF](https://arxiv.org/pdf/2511.20620), [HTML](https://arxiv.org/abs/2511.20620)
### Authors
Xinhao Liu,Jiaqi Li,Youming Deng,Ruxin Chen,Yingjia Zhang,Yifei Ma,Li Guo,Yiming Li,Jing Zhang,Chen Feng
### Background
当前，闭环评估的可再现性仍然是嵌入式AI（如视觉导航）的主要瓶颈。虽然最近的视频-3DGS方法在开放场景捕获方面取得了进展，但由于视觉和几何模拟与现实之间的巨大差异，这些方法仍不适合进行基准测试。
### Innovation
我们引入了Wanderland，这是一种从现实到模拟的框架，具备多传感器捕捉、可靠的重构、精确的几何结构和稳健的视图综合特性。通过这一管线，我们创建了一个多样化的室内-室外城市场景数据集，并系统地展示了仅图像管道在扩展性方面的不足，几何质量对新颖视图综合的影响，以及所有这些因素对导航策略学习和评估可靠性产生的负面影响。此外，Wanderland丰富的原始传感器数据还允许对三维重建和新颖视图合成的模型进行基准测试。
### Conclusion
我们的工作为开放世界嵌入式AI的可再现研究建立了新的基础。
## 565. `cs.CV` - 评估深度学习模型在负载搬运活动中全身动态3D姿态预测中的表现 [PDF](https://arxiv.org/pdf/2511.20615), [HTML](https://arxiv.org/abs/2511.20615)
### Authors
Seyede Niloofar Hosseini,Ali Mojibi,Mahdi Mohseni,Navid Arjmand,Alireza Taheri
### Background
该研究旨在探索深度神经网络在动态负载搬运活动中预测人体整体姿态的应用。研究使用双向长短期记忆（BLSTM）和变压器架构训练了两个时间序列模型，数据集包含了20名正常体重男性个体在不同负载位置进行204次负载搬运任务时的身体姿势的3D动态坐标数据，包括提举和处理技术的变化。研究背景在于通过改进预测模型提高人体姿态预测的准确性，特别是在复杂任务中的表现。
### Innovation
研究提出了一种新的方法，通过优化一个新颖的成本函数来确保身体各段的长度保持不变，从而提高以前和当前姿态预测网络的准确性。研究还指出，使用变压器架构相较于基于BLSTM的模型，在长时间预测方面提高了约58%的准确性。研究结论支持使用能够捕捉3D运动帧时间序列依赖性的神经网络，为理解和预测手动搬运活动中的运动动态提供独特的方法。
### Conclusion
研究发现，使用变压器架构的模型在3D姿态预测中表现更佳，相较于BLSTM模型，其均方根误差降低了约58%。此外，通过优化一种新的成本函数可以提高模型预测的准确性。该研究强调了利用神经网络捕捉3D运动序列依赖性的必要性，为理解和预测手动搬运活动中的运动动态提供了新的方法。
## 566. `cs.CV` - 一致性评论员：通过参考引导的关注对齐进行生成图像中的不一致性修正 [PDF](https://arxiv.org/pdf/2511.20614), [HTML](https://arxiv.org/abs/2511.20614)
### Authors
Ziheng Ouyang,Yiren Song,Yaoli Liu,Shihao Zhu,Qibin Hou,Ming-Ming Cheng,Mike Zheng Shou
### Background
以往的工作已经探索了给定参考图像的各种定制生成任务，但仍难以生成一致的细粒度细节。
### Innovation
本研究旨在通过参考引导的后编辑方法解决生成图像的一致性问题，并提出了ImageCritic。首先构建了一个参考降级目标三元组的数据集，以有效地模拟现有生成模型中常见的不准确性和不一致性。进一步地，通过细致检查模型的注意力机制和内在表示，相应地设计了关注对齐损失和细节编码器，以精确修正不一致性。ImageCritic可以整合到代理框架中，自动检测不一致性并在复杂场景中进行多轮局部编辑。
### Conclusion
广泛的实验表明，ImageCritic能够有效地解决各种定制生成场景中的细节相关问题，相对于现有方法提供了显著的改进。
## 567. `cs.CV` - MapReduce LoRA: 改进生成模型多偏好优化的帕累托前沿 [PDF](https://arxiv.org/pdf/2511.20629), [HTML](https://arxiv.org/abs/2511.20629)
### Authors
Chieh-Yun Chen,Zhonghao Wang,Qi Chen,Zhifan Ye,Min Shi,Yue Zhao,Yinan Zhao,Hui Qu,Wei-An Lin,Yiru Shen,Ajinkya Kale,Irfan Essa,Humphrey Shi
### Background
Reinforcement learning from human feedback (RLHF) 与奖励模型结合提升了生成模型与人类审美和感知偏好的对齐。然而，同时优化多种奖励往往会引发一种‘对齐税’，即提高一个维度的同时可能降低其他维度的表现。
### Innovation
文章提出了两种互补的方法：MapReduce LoRA 和 Reward-aware Token Embedding (RaTE)。MapReduce LoRA 通过并行训练特定偏好的 LoRA 专家并将它们合并以改进共享基础模型，而 RaTE 则学习奖励特定的 token 向量，在推理时可灵活调整偏好。实验结果表明，该框架在多个模态任务中均显著提升了多偏好对齐的表现。
### Conclusion
我们的框架设定了多偏好对齐的新最先进的食谱，涵盖了各种模态。
## 568. `cs.CV` - MotionV2V: 编辑视频中的运动 [PDF](https://arxiv.org/pdf/2511.20640), [HTML](https://arxiv.org/abs/2511.20640)
### Authors
Ryan Burgert,Charles Herrmann,Forrester Cole,Michael S Ryoo,Neal Wadhwa,Andrey Voynov,Nataniel Ruiz
### Background
尽管生成视频模型在保真度和一致性方面取得了显著成果，但将这些能力应用于视频编辑仍然是一个复杂的挑战。近期的研究探索了通过提高从文本到视频的生成或图像动画的运动可控性来改进这些功能，然而，本文指出精确的运动控制是一个值得关注但尚未充分探索的视频编辑策略。
### Innovation
本文提出了一种通过直接编辑从输入中提取的稀疏轨迹来修改视频运动的方法。作者将其输入和输出轨迹之间的差异定义为“运动编辑”，并通过结合生成模型基干，实现了强大的视频编辑功能。为此，作者引入了一种生成“运动反事实”的管道，视频对在实现相同内容的同时具有不同的运动，并对一个数据集进行了基于运动条件的视频扩散架构的微调。这种方法允许从任意时间戳开始进行编辑，并自然地传播。
### Conclusion
在四组用户的直接比较中，本文模型优于先前的工作，获得了超过65%的偏爱度。请访问我们的项目页面了解更多信息：this https URL
## 569. `cs.CV` - VQ-VA World: 向高质量视觉问题-视觉回答迈进 [PDF](https://arxiv.org/pdf/2511.20573), [HTML](https://arxiv.org/abs/2511.20573)
### Authors
Chenhui Gou,Zilong Chen,Zeyu Wang,Feng Li,Deyao Zhu,Zicheng Duan,Kunchang Li,Chaorui Deng,Hongyi Yuan,Haoqi Fan,Cihang Xie,Jianfei Cai,Hamid Rezatofighi
### Background
该论文研究了Visual Question-Visual Answering (VQ-VA)，即生成图像而不是文本来回答视觉问题的能力，这种能力最近在像NanoBanana和GPT-Image这样的专用系统中出现了。目前，这种能力还没有被开源模型所具备，因此需要开发新的框架和技术来将其引入开源模型。
### Innovation
为了将VQ-VA的能力引入开源模型，作者们提出了VQ-VA World，这是一个数据为中心的框架，围绕着旨在大规模、精确地构建数据的代理管道。此外，作者还发布了IntelligentBench，这是一个由人类精心编制的基准测试，可以系统评估VQ-VA在世界知识、设计知识和推理方面的表现。通过使用VQ-VA World数据集进行训练，LightFusion取得了53.06的优异成绩，超过了之前最好的开源基线，并显著缩小了与领先专用系统的差距。
### Conclusion
通过发布整个模型权重、数据集和管道，作者希望激励未来对VQ-VA的研究。
## 570. `cs.CV` - 一种用于可控视频生成的先推理后描述指示解释器 [PDF](https://arxiv.org/pdf/2511.20563), [HTML](https://arxiv.org/abs/2511.20563)
### Authors
Shengqiong Wu,Weicai Ye,Yuanxing Zhang,Jiahao Wang,Quande Liu,Xintao Wang,Pengfei Wan,Kun Gai,Hao Fei,Tat-Seng Chua
### Background
扩散变换器已在视频保真度和时间连贯性方面取得了显著进展，但实践中的可控性依然有限。用户输入的简短、不明确和组合复杂性与训练中使用的详细提示形成对比，导致意图-输出不匹配。
### Innovation
提出了ReaDe，一种通用且模型无关的解释器，将原始指令转化为精准、可操作的规范供下游视频生成器使用。ReaDe 采用推理-描述的范式：首先分析用户请求以识别核心需求并解决模糊性，然后产生详细的指导，以实现忠实且可控的生成。通过两阶段优化训练 ReaDe：先推理辅助监督引入解析解析，并带有逐步追踪和密集说明图；其次，多维奖励分配器实现基于反馈的自然风格说明的稳定细化。
### Conclusion
实验结果显示，在单条件和多条件场景中，ReaDe 在指令保真度、说明准确性以及下游视频质量方面均有一致提升，并且对推理密集和未见过的输入有强大的泛化能力。ReaDe 提供了一条使可控视频生成与准确解释用户意图相一致的实用途径。
## 571. `cs.CV` - ShapeGen：走向高质量3D形状合成 [PDF](https://arxiv.org/pdf/2511.20624), [HTML](https://arxiv.org/abs/2511.20624)
### Authors
Yangguang Li,Xianglong He,Zi-Xin Zou,Zexiang Liu,Wanli Ouyang,Ding Liang,Yan-Pei Cao
### Background
受图像和视频生成范式的启发，3D形状生成已取得了显著进展，能够从单张图像快速合成高质量的3D资产。然而，现有方法仍然面临一些挑战，如细节不够精细、表面过度平滑以及薄壳结构不完整等问题。这些限制使生成的3D资产仍未达到艺术家青睐的标准。
### Innovation
提出了ShapeGen，通过改进3D表示和监督、提高分辨率以及利用线性变换器的优势，实现了高质量的从图像到3D形状的生成。这些改进使得生成的资产能够无缝集成到3D管道中，促进了其在各种应用中的广泛应用。通过广泛的实验，验证了这些改进对整体性能的影响，最终ShapeGen使得图像到3D生成取得了显著进步，达到了新的最佳性能。
### Conclusion
得益于这些增强措施的协同效应，ShapeGen在图像到3D生成方面实现了突破，确立了新的最先进的性能基准。
## 572. `cs.CV` - 唤醒视觉语言模型在长尾多标签视觉识别中的潜能 [PDF](https://arxiv.org/pdf/2511.20641), [HTML](https://arxiv.org/abs/2511.20641)
### Authors
Wei Tang,Zuo-Zheng Wang,Kun Zhang,Tong Wei,Min-Ling Zhang
### Background
长尾多标签视觉识别面临显著挑战，因为图像通常包含多个标签，而这些标签之间的类别分布极度不平衡，这导致模型倾向于优先处理头部类标签，而忽视尾部类标签的表现。最近的研究利用预训练的视觉-语言模型（如CLIP）结合长尾学习技术，从中提取丰富且多维的先验知识以提高性能。但现有方法直接从不平衡的数据集中提取语义类间关系，导致尾部类标签的数据稀疏性问题，从而产生不稳定的关联。此外，CLIP的零样本范式优化单标签图像-文本配对，使其在多标签任务上表现不佳。
### Innovation
本文提出了一个名为CAPNET的新颖端到端框架，以显式建模CLIP文本编码器中的标签相关性。框架包含图卷积网络进行标签感知传播和可学习软提示以改进嵌入。利用分布平衡并具有类别意识重新加权的Focal损失进行优化训练。此外，通过测试时间集成和通过参数效率的微调重新对齐视觉-文本模态，以避免对尾部类标签的过度拟合，同时保持头部类标签的性能。
### Conclusion
在包括VOC-LT, COCO-LT和NUS-WIDE在内的基准测试中进行了详尽的实验和消融研究，结果显示CAPNET相比于最先进的方法实现了显著的提升，验证了其在实际长尾多标签视觉识别中的有效性。
## 573. `cs.CV` - 概念感知批次采样改进语言-图像预训练 [PDF](https://arxiv.org/pdf/2511.20643), [HTML](https://arxiv.org/abs/2511.20643)
### Authors
Adhiraj Ghosh,Vishaal Udandarao,Thao Nguyen,Matteo Farina,Mehdi Cherti,Jenia Jitsev,Sewoong Oh,Elisa Ricci,Ludwig Schmidt,Matthias Bethge
### Background
许多数据处理工作关注数据集的质量，但大多数方法是（i）离线的，即根据预设的过滤标准生成静态数据集；（ii）概念无关的，使用基于模型的过滤器引入额外的数据偏差。
### Innovation
本文提出了DataConcept数据集，包含1.28亿个带有关于概念组成细节的Web爬取图像-文本对；提出了概念感知批次采样（CABS）框架，包括两种变体：最大化多样性（CABS-DM）和最大化频率（CABS-FM），实现在特定目标分布下的灵活批次构建。
### Conclusion
通过在28个基准测试中的广泛评估，证明了CABS方法显著改善了CLIP/SigLIP模型类，产生高性能的模型。CABS代表了一种强大的开源替代方案，允许从业者定义自定义的概念分布，以优化特定下游任务。
## 574. `cs.CV` - iMontage: 统一、通用且动态性强的多对多图像生成 [PDF](https://arxiv.org/pdf/2511.20635), [HTML](https://arxiv.org/abs/2511.20635)
### Authors
Zhoujie Fu,Xianfang Zeng,Jinghong Lan,Xinyao Liao,Cheng Chen,Junyi Chen,Jiacheng Wei,Wei Cheng,Shiyu Liu,Yunuo Chen,Gang Yu,Guosheng Lin
### Background
预训练的视频模型能够学习强大的先验知识，生成高质量且时间上连贯的内容。尽管这些模型在时间连贯性方面表现出色，但它们的动力学特性往往受限于训练数据的连续性质。本文假设，通过将来自图像数据的丰富且不受约束的内容多样性注入这种连贯的时间框架中，可以生成集自然过渡和更广泛的动力范围于一体的图像集。
### Innovation
本文介绍了一种名为iMontage的统一框架，旨在将强大的视频模型重新用于生成图像。该框架可以消费和生产可变长度的图像集，统一了各种图像生成和编辑任务。文章提出了一种优雅且最小侵入性的适应策略，配合定制的数据管理和训练范式，使模型在不破坏其宝贵的时间动态先验知识的情况下，获得广泛的图像操作能力。
### Conclusion
iMontage在多个主流任务中表现出色，不仅保持了跨图像的上下文一致性，还生成了具有惊人的动态范围的场景，超越了传统范畴。
## 575. `cs.CV` - 3D-Aware Multi-Task Learning with Cross-View Correlations for Dense Scene Understanding [PDF](https://arxiv.org/pdf/2511.20646), [HTML](https://arxiv.org/abs/2511.20646)
### Authors
Xiaoye Wang,Chen Tang,Xiangyu Yue,Wei-Hong Li
### Background
当前方法主要在2D图像空间中捕捉跨任务关系，但这些方法往往导致缺乏3D意识的不规则特征，这限制了对场景的全面理解。
### Innovation
提出了一种轻量级的视图间模块（CvM），可以在不同视图之间共享任务信息并捕捉视图间的相关性，将其与MTL编码器的功能结合以进行多任务预测。该模块具有架构无关性，适用于单视图和多视图数据。
### Conclusion
在NYUv2和PASCAL-Context上的广泛结果表明，该方法能够有效将几何一致性注入到现有的MTL方法中，从而提高性能。
## 576. `cs.CV` - DINO-Tok: 调整DINO用于视觉标记器 [PDF](https://arxiv.org/pdf/2511.20565), [HTML](https://arxiv.org/abs/2511.20565)
### Authors
Mingkai Jia,Mingxiao Li,Liaoyuan Fan,Tianxing Shi,Jiaxin Guo,Zeming Li,Xiaoyang Guo,Xiao-Xiao Long,Qian Zhang,Ping Tan,Wei Yin
### Background
近年来，视觉生成领域取得了重要进展，其中潜生成模型（LGMs）因其有效的视觉标记化方法而崛起。然而，现有标记器通常从头开始训练，难以在高维潜空间中平衡语义表示和重构保真度。
### Innovation
本文介绍了一种基于DINO的视觉标记器DINO-Tok，该标记器将分层表示统一到一个信息完整的潜空间中。通过结合保留细节的浅层特征和编码全局语义的深层特征，DINO-Tok有效连接了预训练表示和视觉生成。此外，本文还分析了高维空间中向量量化（VQ）遇到的挑战，提出了全局PCA重新加权机制，以稳定VQ并保留不同维度中的关键信息。DINO-Tok在ImageNet 256×256上实现了最先进的重建性能，自编码达到了28.54 PSNR，基于VQ的方法达到了23.98 PSNR，显著优于先前的标记器，并且与其媲美的是有数亿训练数据的模型（如Hunyuan和Wan）。
### Conclusion
这些结果表明，将强大的预训练视觉模型（如DINO）适应于标记化，能够产生语义对齐且高保真的潜表示，实现下一代视觉生成模型的发展。
## 577. `cs.CV` - LocateAnything3D：基于视觉线索的多对象三维检测 [PDF](https://arxiv.org/pdf/2511.20648), [HTML](https://arxiv.org/abs/2511.20648)
### Authors
Yunze Man,Shihao Wang,Guowen Zhang,Johan Bjorck,Zhiqi Li,Liang-Yan Gui,Jim Fan,Jan Kautz,Yu-Xiong Wang,Zhiding Yu
### Background
当前的视觉-语言模型（VLMs）在开放的2D描述和图上性地文本对齐方面表现出色，但在多对象的三维检测方面还未得到充分解决。本文介绍了LocateAnything3D，这是一种专为VLM设计的方法，将三维检测转化为下一个词预测问题。
### Innovation
LocateAnything3D的关键在于简明且明确的Chain-of-Sight（CoS）序列，该序列模仿了人类从图像中推理解物体的方式：首先在2D中找到一个物体，然后推断其距离、大小和姿态。模型首先生成2D检测结果作为视觉思维链，然后按照从容易到困难的课程预测3D框：在对象之间，按从近到远的顺序减少早期的不确定性并匹配主观视角使用性；在每个对象内部，通过从相机中心、维度和旋转的分解排序信息，提高稳定性和可学习性。
### Conclusion
在具有挑战性的Omni3D基准测试上，模型达到了最先进的成果，获得了49.89 AP_3D 的成绩，并且即使基准模型获得了真实2D框也超过了之前的最佳成果15.51分的绝对改进。此外，它也能够在未见过的类别上零样本外推表现出强大的鲁棒性。通过将三维检测变成一个循序渐进的下一个词问题，LocateAnything3D为模型如何感知三维环境提供了一个实用的基础。
## 578. `cs.CV` - Infinity-RoPE: 行动可控的无限视频生成源自自回归自滚动 [PDF](https://arxiv.org/pdf/2511.20649), [HTML](https://arxiv.org/abs/2511.20649)
### Authors
Hidir Yesiltepe,Tuna Han Salih Meral,Adil Kaan Akan,Kaan Oktay,Pinar Yanardag
### Background
当前的自回归视频扩散模型受到三个核心瓶颈的限制：（i）由基础模型的3D旋转位置嵌入（3D-RoPE）设置的时间有限制；（ii）在长时间播放过程中对精细动作控制的缓慢响应；（iii）无法在同一生成流中实现不连续的电影过渡。
### Innovation
我们引入了$to$-RoPE，一个统一的推理时框架，通过三个相互连接的组件解决了所有三个限制：块相对RoPE，KV刷新和RoPE剪切。块相对RoPE重新定义了时间编码为移动的局部参考框架，其中每个新生成的潜质块相对于基模型的最大帧界限旋转，而早期块则向后旋转以保持相对时间几何。KV刷新通过保留两个潜质帧，全局sink和最后生成的潜质帧来重置KV缓存，从而确保即时提示响应。RoPE剪切引入了时间RoPE坐标的受控不连续性，使在同一连续滚动中实现多剪辑场景过渡成为可能。
### Conclusion
这些组件共同建立了$to$-RoPE作为无需训练的基础，可以实现无限时间范围、可控和电影风格的视频扩散。全面的实验表明，$to$-RoPE在整体VBench分数上始终优于先前的自回归模型。
## 579. `cs.CV` - MedROV: 针对多种医学影像模态的实时开放词汇检测 [PDF](https://arxiv.org/pdf/2511.20650), [HTML](https://arxiv.org/abs/2511.20650)
### Authors
Tooba Tehreem Sheikh,Jean Lahoud,Rao Muhammad Anwer,Fahad Shahbaz Khan,Salman Khan,Hisham Cholakkal
### Background
传统的医学影像目标检测模型在封闭词汇集框架内运行，限制了其检测新类别对象的能力。开放词汇集目标检测（OVOD）解决了这一问题，但在医学影像领域却由于数据集稀缺和文本-图像对齐能力弱而未得到充分研究。
### Innovation
我们提出了一种MedROV，这是第一种针对医学影像的实时开放词汇集检测模型。为实现开放词汇学习，我们构建了名为Omnis的大规模数据集，包含九种成像模态的600K检测样本，并引入伪标签策略处理多源数据集中的缺失注释。此外，通过结合大型预训练基础模型的知识增强了泛化能力。利用对比学习和跨模态表示，MedROV能够有效检测已知和新结构。实验结果表明，MedROV 在医学图像检测上的平均绝对改进为40 mAP50，并超越封闭集检测器超过3 mAP50，运行速度达70 FPS，成为医学检测的新基准。
### Conclusion
MedROV 在医学影像开放词汇集检测任务中表现出色，不仅大幅超越了之前最先进的基础模型，还在运行速度上达到了70 FPS，确立了新的检测基准。
## 580. `cs.CV` - RubricRL: 简单且通用的文本到图像生成奖励设计 [PDF](https://arxiv.org/pdf/2511.20651), [HTML](https://arxiv.org/abs/2511.20651)
### Authors
Xuelu Feng,Yunsheng Li,Ziyu Wan,Zixuan Gao,Junsong Yuan,Dongdong Chen,Chunming Qiao
### Background
强化学习（RL）近年来被视为一种有前途的方法，用于使文本到图像生成模型与人类偏好对齐。然而，设计有效的且可解释的奖励仍然是一个关键挑战。现有方法通常依赖于复合度量标准（如 CLIP、OCR 和现实性评分）和固定权重，或者从人类偏好模型中提炼单一标量奖励，这在解释性和灵活性方面都有局限性。
### Innovation
RubricRL 提出了一种简单且通用的框架，以基于评分表的奖励设计方案提供更高的可解释性、组合性和用户控制能力。该方法动态构建针对每个提示的结构化评分表，使其成为细化视觉标准的分解清单（如物体正确性、属性准确性、OCR 忠实度和现实性）组合，根据输入文本量身定制。每个标准由多模态评判员独立评估，同时自适应提示的权重机制突出显示最相关维度。这种设计不仅为策略优化（如 GRPO 或 PPO）提供了可解释和模块化监督信号，还允许用户直接调整奖励或惩罚的方面。
### Conclusion
RubricRL 在自回归文本到图像模型上的实验表明，它提高了提示忠实度、视觉细节和泛化能力，并为其在文本到图像架构中的可解释RL对齐提供了一个灵活且可扩展的基础。
## 581. `cs.CV` - Vision-Language Memory for Spatial Reasoning [PDF](https://arxiv.org/pdf/2511.20644), [HTML](https://arxiv.org/abs/2511.20644)
### Authors
Zuntao Liu,Yi Du,Taimeng Fu,Shaoshu Su,Cherie Ho,Chen Wang
### Background
智能机器人的空间推理能力至关重要，但当前的视觉-语言模型（VLMs）在基于视频的空间推理方面仍无法达到人类水平。这种差距主要源于两个挑战：语义几何对齐不一致，导致无法进行持续的3D理解；缺乏持久记忆来保留3D表示和理解。
### Innovation
我们提出了VLM$^2$，这是一种具有持久记忆的视觉-语言模型，用于以视图一致、3D感知的表示进行空间推理。具体而言，为了增强长期推理能力，我们引入了一个双记忆模块，包括一个工作记忆，作为滑动窗口专注于即时上下文，和一个情景记忆，用于综合和存储关键长期信息。这种设计允许在固定计算成本下高效地进行长期空间推理。
### Conclusion
在多个基准上的广泛实验表明，VLM$^2$在仅基于视频的模型中达到了最先进的性能，显著推动了视觉-空间智能的前沿。
## 582. `cs.CV` - PixelDiT: 像素扩散变换器在图像生成中的应用 [PDF](https://arxiv.org/pdf/2511.20645), [HTML](https://arxiv.org/abs/2511.20645)
### Authors
Yongsheng Yu,Wei Xiong,Weili Nie,Yichen Sheng,Shiqiu Liu,Jiebo Luo
### Background
扩散变换器(DiTs)通常使用潜空间建模，但这种方法依赖于一个两阶段的流水线，其中预训练的自编码器引入了有损重构，导致错误累积并妨碍了联合优化。
### Innovation
提出了一种单一阶段的端到端模型PixelDiT，不使用自编码器，直接在像素空间中学习扩散过程。PixelDiT采用了一个由两层构成的完全基于Transformer的架构，能够在保持细腻细节的同时高效地训练像素空间中的扩散模型。
### Conclusion
PixelDiT在ImageNet 256x256上实现了1.61的FID，显著优于现有的像素生成模型。进一步将其扩展到文本到图像生成，在1024x1024分辨率的像素空间中预训练，分别在GenEval和DPG-bench上取得了0.74和83.5的性能，接近最佳的潜空间扩散模型。
## 583. `cs.CV` - 使用确定性点过程引导的策略优化实现多样视频生成 [PDF](https://arxiv.org/pdf/2511.20647), [HTML](https://arxiv.org/abs/2511.20647)
### Authors
Tahira Kazimi,Connor Dunlop,Pinar Yanardag
### Background
最近的文本到视频（T2V）扩散模型虽然在质量和提示对齐方面取得了显著进展，但在从单一文本提示生成多个视频时往往表现出低多样性。这个问题来源于模型在生成多样化视觉效果时难以避免冗余和重复。为了解决这个问题，本文将其重新定义为集水平策略优化问题，目的是训练一个政策，能够覆盖给定提示的各种合理结果。该问题通过引入DPP-GRPO框架进行实现，整合了确定性点过程（DPP）和组相对策略优化（GRPO）理论。
### Innovation
提出了DPP-GRPO框架，结合了DPP和GRPO理论，通过DPP确保减少冗余样本，同时使用GRPO提供候选集的分组反馈，实现多样性的显式信号。该框架支持即插即用并独立于具体模型，能够在视觉外观、摄像机运动和场景结构方面鼓励多样化生成，同时保持对提示的忠实度和感知质量。
### Conclusion
本文的方法在WAN和CogVideoX上实现，并在VBench、VideoScore和人类偏好的研究中展示了对最先进的基准的视频多样性的持续改进。此外，释放了该方法的代码和一个包含30,000个多样提示的新基准数据集，以支持未来的研究。
## 584. `cs.CV` - DKAN：用于空间分辨率转录组学的双路径知识增强对比对齐网络 [PDF](https://arxiv.org/pdf/2511.17685), [HTML](https://arxiv.org/abs/2511.17685)
### Authors
Wei Zhang,Jiajun Chu,Xinci Liu,Chen Tong,Xinyue Li
### Background
空间转录组学（ST）是一种技术，在保持空间上下文的同时，测量组织切片中的基因表达谱。它揭示了局部的基因表达模式和组织异质性，这对于理解疾病病因至关重要。然而，由于成本高昂，努力从全切片图像中预测空间基因表达。尽管最近取得了进展，但当前方法仍面临重大局限，例如高阶生物上下文未充分利用、过度依赖示例检索，以及异质模态对齐不足。
### Innovation
我们提出了DKAN，一种新型的双路径知识增强对比对齐网络，通过整合组织病理学图像和基因表达谱，实现基于生物启发的预测空间分辨率基因表达。DKAN引入了有效的基因语义表示模块，利用外部基因数据库提供额外的生物学洞察，增强基因表达预测。该网络采用统合对比学习和监督学习的一阶段统一框架，避免了依赖于示例，并结合了自适应权重机制。此外，提出了双路径对比对齐模块，使用基因语义特征作为跨模态动态协调器，实现有效的异质特征融合。
### Conclusion
通过在三个公共ST数据集上的广泛实验，DKAN在空间基因表达预测方面超越了最先进的模型，建立了新的基准，并为生物学和临床研究提供了一种强大工具。
## 585. `cs.CV` - Splatblox: 基于高斯打点的户外机器人导航可通行性感知算法 [PDF](https://arxiv.org/pdf/2511.18525), [HTML](https://arxiv.org/abs/2511.18525)
### Authors
Samarth Chopra,Jing Liang,Gershom Seneviratne,Yonghan Lee,Jaehoon Choi,Jianyu An,Stephen Cheng,Dinesh Manocha
### Background
当前为户外环境中的自主导航机器人设计系统时，面临着复杂地形、密集植被和不规则障碍物带来的挑战。传统的导航方法可能无法有效地区分可通行区域和障碍物，尤其是在植被密集、地形复杂的环境中。为此，迫切需要一种能够同时融合几何信息和语义信息的新方法，以提高导航系统的性能和适应性。
### Innovation
本文提出了Splatblox，一种实时系统，用于复杂户外环境中的自主导航。该系统通过融合分割的RGB图像和LiDAR点云数据，使用高斯打点技术构建可通行性感知的欧几里得符号距离场（ESDF），该场同时编码几何和语义信息。这种在线更新的方法不仅能够区分可通行植被（如高草）和刚性障碍物（如树木），还能确保360度的几何覆盖范围，支持更长的规划时段。实验结果表明，Splatblox在包括高草在内的场景中表现出色，相比现有最先进的方法，具有更高的成功率、更少的冻结事件、更短的路径以及更快的到达目标时间。
### Conclusion
Splatblox通过将高斯打点技术与实时更新的ESDF相结合，为户外机器人的导航性能带来了显著提升，尤其在复杂和多变的环境中。本研究不仅验证了Splatblox的有效性，还展示了其在不同平台上的可移植性，能够支持长达100米的长期任务，具有广泛的应用前景。
## 586. `cs.CV` - 使用多阶段深度学习框架及PKCP-MixUp增强的多相对比增强CT儿童肝肿瘤诊断 [PDF](https://arxiv.org/pdf/2511.19478), [HTML](https://arxiv.org/abs/2511.19478)
### Authors
Wanqi Wang,Chun Yang,Jianbo Shao,Yaokai Zhang,Xuehua Peng,Jin Sun,Chao Xiong,Long Lu,Lianting Hu
### Background
儿童肝肿瘤是儿科最常见的实体肿瘤之一，区分良性或恶性以及病理分类对于临床治疗至关重要。尽管病理检查是金标准，但侵入性活检存在显著局限性：儿童肝的高血管性和脆弱的肿瘤组织增加了出血等并发症的风险；加之年幼的孩子不配合体检需要麻醉，增加了医疗费用或心理创伤。尽管很多努力将AI应用于临床，但对于儿童肝肿瘤，研究人员并未充分重视AI的重要性。
### Innovation
本文提出了一个基于多阶段深度学习框架（DL）的自动化儿童肝肿瘤诊断系统，利用多相对比增强CT。本文建立了新型的PKCP-MixUp数据增强方法来应对数据稀缺和类别不平衡的问题，并开发了一个肿瘤检测模型来提取感兴趣区域。还建立了一个两阶段诊断流程，使用ROI-蒙版图像训练了三种不同基础模型。检测模型达到了高性能（mAP=0.871），首次分类模型（良性和恶性）达到了优秀的性能（AUC=0.989）。最终诊断模型也展示了在多种情况下的鲁棒性，包括良性亚型分类（AUC=0.915）和恶性亚型分类（AUC=0.979）。此外，还进行了多层对比分析，包括数据和训练管道的消融研究，以及Shapley-Value和CAM可解释性分析。
### Conclusion
本文框架填补了儿童肝肿瘤特定的DL诊断缺口，提供了CT相位选择和模型设计的实际行动见解，并为精准、可及的儿童肝肿瘤诊断铺平了道路。
## 587. `cs.CV` - 超越二元分类：一种半监督的通用AI生成图像检测方法 [PDF](https://arxiv.org/pdf/2511.19499), [HTML](https://arxiv.org/abs/2511.19499)
### Authors
Hong-Hanh Nguyen-Le,Van-Tuan Tran,Dinh-Thuc Nguyen,Nhien-An Le-Khac
### Background
生成器（如StyleGAN、Midjourney、DALL-E等）迅速发展，产生了高度逼真的合成图像，这对数字媒体的真实性构成了重大挑战。当前的检测技术在跨不同生成器（特别是从Generative Adversarial Networks (GANs)到Diffusion Models (DMs)）时无法实现泛化，主要原因是这些生成器在优化目标和生成的特征方面的根本差异。现有的检测器在跨越不同架构边界时表现出色不足。
### Innovation
本文提供了一种理论分析，指出了GAN和DM架构在覆盖行为上的区别。基于此分析，提出了一种称为Triarchy Detector的半监督方法，通过发现“假”类别中的潜在架构模式来增强二分类。TriDetect通过Sinkhorn-Knopp算法实现平衡聚类分配，并采用跨视图一致性机制，鼓励模型学习基本的架构差异。本文在两个标准基准和三个自然环境中，与13个基线进行了对比测试，验证了其对未见过的生成器的泛化能力。
### Conclusion
本文提出了一种半监督方法TriDetect，能够在未见过的生成器上实现泛化的AI生成图像检测，通过发现潜在的架构模式来改进二分类，并通过理论分析和实际测试证明了其有效性。
## 588. `cs.CV` - Shortcut Invariance: Targeted Jacobian Regularization in Disentangled Latent Space [PDF](https://arxiv.org/pdf/2511.19525), [HTML](https://arxiv.org/abs/2511.19525)
### Authors
Shivam Pal,Sakshi Varshney,Piyush Rai
### Background
深度神经网络容易学习训练数据中的捷径、错误相关性，这些捷径和错误相关性会在分布外（OOD）泛化时导致严重的失败。传统的做法是通过学习鲁棒的表示来增强模型的稳定性，这种方法往往需要将潜在空间明确地划分为核心和错误相关性组件，但这种方法复杂度高、脆弱，难以扩展。
### Innovation
该研究提出了一种不同于学习鲁棒表示的方法，而是学习一个鲁棒的函数。该方法简单有效，可以在解耦的潜在空间中运行，分离出错误相关性和核心特征，通过在训练过程中注入针对特定方向的异向潜在噪声，使分类器对错误相关特征的敏感度减弱。这种方式被称为目标雅克比正则化，迫使分类器忽略错误相关特征，依赖更复杂的核心语义信号。该方法在现有的捷径学习基准测试中取得了最先进的分布外性能。
### Conclusion
该研究提出的方法通过在解耦的潜在空间中实现分类函数对捷径信号的功能不变性，能够有效抵御错误相关的特征影响，提升模型的分布外泛化能力，最终在分布外性能基准测试中取得了最优的结果。
## 589. `cs.CV` - PhysDNet：侧扫声纳图像的物理引导分解网络 [PDF](https://arxiv.org/pdf/2511.19539), [HTML](https://arxiv.org/abs/2511.19539)
### Authors
Can Lei,Hayat Rajani,Nuno Gracias,Rafael Garcia,Huigang Wang
### Background
侧扫声纳（SSS）图像在海底测绘和水下遥感中广泛应用，但测量到的强度受到海底反射率、地形高度和声线衰减等因素的强烈影响，导致图像易受视角影响，降低了后续分析的鲁棒性。
### Innovation
提出了一种基于物理的多分支网络PhysDNet，该网络将SSS图像分解为海底反射率、地形高度和传播损失这三个可解释的领域。通过嵌入朗伯反射模型，PhysDNet 无需真实标注数据即可重建声纳强度，从而实现自监督训练。
### Conclusion
实验结果表明，分解后的表示保留了稳定的地质结构，捕捉到物理一致的照明和衰减，并生成可靠的阴影图。这些发现表明，基于物理的分解为SSS分析提供了一个稳定且可解释的领域，提高了物理一致性以及后续任务如注册和阴影解释的表现。
## 590. `cs.CV` - SPQR: 用于文本到图像扩散模型现代安全对齐方法的标准基准 [PDF](https://arxiv.org/pdf/2511.19558), [HTML](https://arxiv.org/abs/2511.19558)
### Authors
Mohammed Talha Alam,Nada Saadi,Fahad Shamshad,Nils Lukas,Karthik Nandakumar,Fahkri Karray,Samuele Poppi
### Background
文本到图像的扩散模型可以生成受版权保护、不安全或私人内容。尽管安全对齐旨在抑制特定概念，但很少有评估测试安全在良性下游微调（例如LoRA个性化、风格/领域适配器）之下是否仍然保持。由于真正的安全对齐必须能够应对甚至良性部署后适应，该研究探究了当前安全方法在良性微调下的稳定性，并观察到频繁出现失败。为了确保在良性部署后适应下也能保持安全、实用性和稳健性，提出了SPQR基准（Safety-Prompt adherence-Quality-Robustness），这是一个单一评分指标，提供了一个标准化和可重复的评估框架，通过报告单一排行榜分数来促进比较。
### Innovation
SPQR基准是一个单一评分指标，提供了一个标准化且可重复的评估框架，用于评估在良性微调下安全对齐的扩散模型如何保持安全、实用性和稳健性。该基准通过多语言、特定领域和出域分析，以及类别级别的拆解，识别出在良性微调后安全对齐失败的情况，从而展示了SPQR作为文本到图像模型安全对齐技术简洁且全面的基准的作用。
### Conclusion
SPQR基准能够提供一个标准化且可重复的评估框架来衡量安全对齐的扩散模型在良性微调下的表现，识别安全对齐的失败情况，并为文本到图像模型的安全对齐技术提供了一个全面且简洁的基准。
## 591. `cs.CV` - 并非无所不能：克服SAM在3D医学成像中的局限性 [PDF](https://arxiv.org/pdf/2511.19471), [HTML](https://arxiv.org/abs/2511.19471)
### Authors
Keith Moore
### Background
基础分割模型如SAM和SAM-2在自然图像上表现良好，但在处理脑MRI时却遇到困难。脑MRI中的结构如豆状核和丘脑缺乏明确边界，并且对比度低。这些模型通常需要微调（例如MedSAM），而不是这样做，作者提出了一种组合替代方案，其中基础模型的输出被当作附加输入通道与MRI一起传递，以突出显示感兴趣的区域。通过使用先前在MRI分割上训练的轻量级3D U-Net生成SAM-2提示，这些模型往往对位置有所猜测但较为模糊。
### Innovation
本文提出了一种无需修改基础模型权重且无需重新训练基础模型就能适应领域转移的架构。该架构通过使用轻量级3D U-Net生成SAM-2提示，并将基础模型的输出作为附加输入通道传递，处理特定区域的信息。同时，还测试了不使用提示的分割方法，采用基于DINO的注意力图。这种体系结构在基底神经节分割上达到约96%的体积准确性，充分满足了评估纵向体积变化的研究需求。
### Conclusion
该方法快速、标签高效且对分布外扫描具有鲁棒性。其已应用于研究与突然发生儿少期强迫症相关的炎症变化。
## 592. `cs.CV` - 在VLMs中扩展具身强化学习以实现工具集成推理 [PDF](https://arxiv.org/pdf/2511.19773), [HTML](https://arxiv.org/abs/2511.19773)
### Authors
Meng Lu,Ran Xu,Yi Fang,Wenxuan Zhang,Yue Yu,Gaurav Srivastava,Yuchen Zhuang,Mohamed Elhoseiny,Charles Fleming,Carl Yang,Zhengzhong Tu,Yang Xie,Guanghua Xiao,Hanrui Wang,Di Jin,Wenqi Shi,Xuan Wang
### Background
近年来，视觉语言模型（VLMs）在图像理解方面表现出色，但在通过多步骤视觉互动进行“图像思考”（即推理）的能力方面仍然有限。虽然当前的VLMs在文本推理方面表现出色，但无论是私有还是开源模型，在工具选择、调用和技术协调方面依然存在挑战。为此，作者提出VISTA-Gym，这是一种用于激励VLMs集成视觉推理能力的可扩展训练环境。
### Innovation
VISTA-Gym统一了来自13个数据集的7个不同现实世界多模态推理任务的标准接口，涵盖了视觉工具（例如，注解、解析），支持可执行的互动循环，可验证的反馈信号，以及高效的轨迹记录。这使得大规模的视觉具身强化学习成为可能，而现有VLMs缺乏工具选择、调用和协调能力。通过多回合轨迹采样和端到端强化学习，VISTA-Gym训练出的VISTA-R1通过工具使用和具身推理取得显著效果。
### Conclusion
大规模实验显示，VISTA-R1-8B在11个公开的推理密集型VQA基准测试中优于大小相似的最先进的基线，性能提升9.51%-18.72%，证明VISTA-Gym是一个有效的训练平台，能够解锁VLMs的工具集成推理能力。
## 593. `cs.CV` - 学习大量多任务世界模型进行连续控制 [PDF](https://arxiv.org/pdf/2511.19584), [HTML](https://arxiv.org/abs/2511.19584)
### Authors
Nicklas Hansen,Hao Su,Xiaolong Wang
### Background
现有的连续控制领域的强化学习研究主要集中在单一任务或离线设置上，这给人一种在线强化学习无法扩展的印象。该领域需要能够跨多种任务和实体执行控制的智能代理，作者提出了一个新的基准，包含200个任务，每个任务都有语言指令、演示和可选的图像观察。同时，作者介绍了Newt，这是一种语言调整的多任务世界模型，首先通过演示进行预训练，获取任务感知的表示和动作先验，然后通过与多个任务的在线交互进行联合优化。
### Innovation
引入了一个新的基准，包含200个多样化任务，每个任务都有语言说明、展示和可选的图像观察。提出了一种新的方法，即新模型Newt，通过语言调整的多任务世界模型，首先通过演示进行预训练，获得任务感知的表示和动作先验，然后通过与所有任务的在线交互进行联合优化。实验结果显示，Newt在多任务性能和数据效率方面优于强基线，在开放回路控制中表现出色，并能够快速适应未见过的任务。
### Conclusion
该研究展示了新方法和基准的有效性，已经发布了相关环境、演示、训练和评估代码，以及200多个检查点。
## 594. `cs.CV` - 它听，它也看：基于集成视觉理解的多模态LLM抑郁症检测 [PDF](https://arxiv.org/pdf/2511.19877), [HTML](https://arxiv.org/abs/2511.19877)
### Authors
Xiangyu Zhao,Yaling Shen,Yiwen Jiang,Zimu Wang,Jiahe Liu,Maxmartwell H Cheng,Guilherme C Oliveira,Robert Desimone,Dominic Dwyer,Zongyuan Ge
### Background
抑郁症是全球最常见的心理健康疾病之一。近年来，语音、视频和文本等多模态数据被广泛用于开发AI辅助的抑郁症评估系统。大型语言模型因其强大的语言理解和泛化能力进一步推动了这一领域的发展。然而，传统的大型语言模型仍以文本为中心，无法处理如音频和视觉模态中丰富的非言语线索，这些都是心理健康评估中至关重要的部分。尽管多模态大型语言模型提供了有前景的方向，但大多数专注于心理应用的模型尚属稀缺。因此，本文提出了一种新的多模态大型语言模型框架，用视觉理解增强音频语言模型，并在时间戳级别对音频-视觉特征进行对齐，从而提高了跨模态时间动态的建模能力，同时减少了对大量训练数据和计算资源的需求。
### Innovation
本文提出了一种新型多模态大型语言模型框架，通过将视觉理解集成到音频语言模型中，并在时间戳级别对音频-视觉特征进行对齐，增强了跨模态的时间动态建模能力。实验表明，该模型在DAIC-WoZ数据集上的性能优于单模态方法和之前的多模态方法。此外，提出的框架可以扩展以纳入更多的生理信号，为心理健康之外更广泛的临床应用铺平了道路。
### Conclusion
该研究提出的方法在多模态抑郁症检测中表现出色，未来可以进一步扩展到更多的生理信号，以推动更广泛的临床应用。
## 595. `cs.CV` - 盘状双边频谱及其反转与多参考对齐的应用 [PDF](https://arxiv.org/pdf/2511.19706), [HTML](https://arxiv.org/abs/2511.19706)
### Authors
Adele Myers,Nina Miolane
### Background
在计算机视觉和形状分析任务中，研究者们经常需要从图像中的物体形状中学习，而忽略其旋转方向。为此，定义一种旋转不变的图像表示是非常有价值的，该表示应保留所有图像信息，但忽略物体在图像中的旋转方式。对于学习任务而言，这种表示需要在大规模数据集上计算高效且可逆，以便于在图像空间中可视化表示。基于此，本文提出了一种快速的旋转不变图像形状分析表示方法：选择性盘状双边频谱。
### Innovation
本文提出了选择性盘状双边频谱，这是盘状双边频谱的扩展，以实现二维图像的旋转不变性。最显著的创新在于推导出了盘状双边频谱的显式逆，使得只需要最少的系数来忠实恢复形状，从而解决了纯盘状双边频谱方法之前无法处理的多参考对齐问题。这项工作为旋转不变形状数据的学习提供了一种实用且理论合理的工具。
### Conclusion
本文通过选择性盘状双边频谱和其反转方法，为多参考对齐任务提供了一种新的解决方案。这一成果确立了盘状双边频谱作为一种实用且理论基础上的旋转不变形状数据学习工具的重要性。
## 596. `cs.CV` - 终端速度匹配 [PDF](https://arxiv.org/pdf/2511.19797), [HTML](https://arxiv.org/abs/2511.19797)
### Authors
Linqi Zhou,Mathias Parger,Ayaan Haque,Jiaming Song
### Background
该研究提出了终端速度匹配（TVM），这是一种流动匹配的一般化，能够实现高保真的单一或少量步骤生成模型。TVM模型在任意两个扩散时间点之间的过渡，并在其终端时间而不是初始时间对其行为进行正则化。
### Innovation
1. 提出了终端速度匹配（TVM）模型，模型在任意两个扩散时间点之间的过渡并对其进行终端正则化。2. 证明了TVM提供了一个数据和模型分布之间的2- Wasserstein距离的上界，当模型是Lipschitz连续时。3. 针对扩散变换器缺乏Lipschitz连续性的特点，引入了最小的架构变化以实现稳定的一阶段训练。4. 开发了一种融合注意力内核，支持雅各比-向量积的反向传递，这与变压器架构的规模良好。
### Conclusion
TVM在ImageNet-256x256上实现了3.29 FID（单次函数评估）和1.99 FID（4次函数评估）。同样，在ImageNet-512x512上实现了4.32 1-NFE FID和2.94 4-NFE FID，代表了从头开始的一次/多次步长模型的最新技术水平。
## 597. `cs.CV` - 通过最优传输实现任务特定模型的持续融合：无需遗忘 [PDF](https://arxiv.org/pdf/2511.19561), [HTML](https://arxiv.org/abs/2511.19561)
### Authors
Zecheng Pan,Zhikang Chen,Ding Li,Min Zhang,Sen Cui,Hongshuo Jin,Luqi Tao,Yi Yang,Deheng Ye,Yu Zhang,Tingting Zhu,Tianling Ren
### Background
将针对不同任务进行微调的模型合并成一个统一的模型正逐渐成为构建多功能高效多任务系统的重要方向。现有的方法大多依赖于参数插值，但这种方法会导致特征空间中的分布偏移，弱化任务特定的知识。
### Innovation
提出了一种基于最优传输理论的新颖模型合并框架OTMF（Optimal Transport-based Masked Fusion）。该框架通过发现应用于任务向量的共同掩码来对齐任务特定模型的语义几何结构，从而避免了直接聚合特征或权重导致的分布偏移。进一步，OTMF支持持续融合范式，能够增量地集成新任务向量，同时保持有限的内存占用，使模型能够高效地融合更多的任务。
### Conclusion
全面实验结果显示，OTMF在准确性与效率方面均达到了最先进的水平。这些发现突显了我们提出的方法在模型合并中的实际和理论价值。
## 598. `cs.CV` - 频率偏差很重要：深入研究鲁棒而广义的深度图像伪造检测 [PDF](https://arxiv.org/pdf/2511.19886), [HTML](https://arxiv.org/abs/2511.19886)
### Authors
Chi Liu,Tianqing Zhu,Wanlei Zhou,Wei Zhao
### Background
随着基于AI生成模型（如GANs）的深度图像伪造不断发展，检测AI生成的伪造品已成为一个重要的安全话题。一般性和鲁棒性是伪造检测器的两个关键问题，决定了其在面对未知的GAN和开放世界中的噪声样本时的可靠性。尽管很多研究都在提高这些问题的处理能力，但其根本原因尚未完全探索，也不清楚它们之间是否存在联系。此外，尽管最近在图像取证或反取证方面解决了这些问题，但仍然缺乏一种能够同时促进两个方面的普遍方法。
### Innovation
本文从频率角度提供了一个基本的解释。研究发现，DNN伪造检测器的频率偏差可能是导致一般性和鲁棒性问题的原因。基于这一发现，本文提出了一种两步频率对齐方法，以减少真实和伪造图像之间的频率差异，这种方法在反取证领域可以作为强大的黑盒攻击，而在取证领域可以作为一种通用的防御手段，以提高检测器的可靠性。并且还开发了相应的攻击和防御实现，并在不同的实验设置中展示了它们的有效性以及频率对齐方法的效果。
### Conclusion
通过频率偏差视角，本文提出了双管齐下的频率对齐方法，它可以作为反伪造领域的强黑盒攻击，也可以作为取证领域的通用防御以提高检测器的可靠性。我们的方法被证明在包括多种检测器、伪造模型和度量标准的不同实验设置中具有显著的效果。
## 599. `cs.CV` - DLADiff：对抗扩散模型微调和零样本定制的双层防护框架 [PDF](https://arxiv.org/pdf/2511.19910), [HTML](https://arxiv.org/abs/2511.19910)
### Authors
Jun Jia,Hongyi Miao,Yingjie Zhou,Linhan Cao,Yanwei Jiang,Wangqiu Zhou,Dandan Zhu,Hua Yang,Wei Sun,Xiongkuo Min,Guangtao Zhai
### Background
随着扩散模型的迅速发展，开发出了多种仅用3到5张训练图片就能生成高保真度图像的微调方法，且高度相似于目标内容。近期，零样本生成方法也开始出现，无需调整模型权重即可从单一参考图像生成极其逼真的输出。然而，技术进步也带来了对面部隐私的重大风险。恶意行为者可以利用少量甚至一张人的照片进行扩散模型定制，从而生成高度相似的合成身份。目前，大部分防御方法主要集中在对抗微调方法，而忽视了零样本方法的防御。
### Innovation
本文提出了一种双重保护机制DLADiff，用于同时防御微调方法和零样本方法。DLADiff包含两个层级，第一层通过提出的双代理模型(DSUR)机制和交替动态微调(ADFT)实现了对抗未经授权微调的有效保护，将对抗训练与预微调模型中获得的先验知识结合在一起。第二层虽然设计简单，但对通过零样本方法生成图像有很强的防护效果。实验结果表明，该方法在防御扩散模型微调方面显著优于现有方法，并在保护免受零样本生成方面达到了前所未有的性能。
### Conclusion
我们的方法在防御扩散模型微调方面显著优于现有方法，并在保护免受零样本生成方面达到了前所未有的性能。
## 600. `cs.CV` - Sundial基础模型在叶面积指数零样本转移能力方面的研究 [PDF](https://arxiv.org/pdf/2511.20004), [HTML](https://arxiv.org/abs/2511.20004)
### Authors
Peining Zhang,Hongchen Qin,Haochen Zhang,Ziqi Guo,Guiling Wang,Jinbo Bi
### Background
该研究探讨了时间序列基础模型在农业监测中进行叶面积指数（LAI）零样本预测的能力。研究人员使用HiQ数据集（美国，2000-2022年），系统性地将统计基线模型、完全监督的LSTM模型以及Sundial基础模型在多种评估协议下进行了比较。
### Innovation
研究发现，在零样本设置下，Sundial模型可以在输入上下文窗口足够长的情况下，优于完全训练的LSTM模型。这表明，通用基础模型可以在遥感时间序列预测中超越专为特定任务设计的监督模型，无需进行任务特定的调整。这一成果强调了预训练时间序列基础模型在农业和环境应用中作为有效插件式预测模型的强大潜力。
### Conclusion
这种通用基础模型在无需任务特定调整的情况下，能够超越专为遥感时间序列预测设计的监督模型，这在零样本设置下取得了显著的预测效果。
## 601. `cs.CV` - CostNav: 一种面向成本感知评估的代理导航基准 [PDF](https://arxiv.org/pdf/2511.20216), [HTML](https://arxiv.org/abs/2511.20216)
### Authors
Haebin Seong,Sungmin Kim,Minchan Kim,Yongjun Cho,Myunchul Joe,Suhwan Choi,Jaeyoon Jung,Jiyong Youn,Yoonshik Kim,Samwoo Seong,Yubeen Park,Youngjae Yu,Yunsung Lee
### Background
现有的导航基准主要关注任务成功指标，而忽视了经济可行性，这是自主送货机器人商业部署的关键。CostNav通过全面的成本和收益分析，评估实体代理，并与现实世界的商业操作保持一致。该模型涵盖了硬件、培训、能源、维护成本和递送收益，并使用行业数据源参数建立了完整的经济生命周期。
### Innovation
CostNav是首项通过定量展示导航研究指标与商业可行性之间的差距，揭示了优化任务成功与优化经济部署之间的根本差异的研究。该模型使用来自行业的数据来源参数，并从简化的模拟环境中投影到真实的递送场景。研究发现，基于碰撞的维护是单次运行成本的主要驱动因素，表明碰撞避免是关键的优化目标。
### Conclusion
CostNav弥合了导航研究与商业部署之间的差距，为多种导航范式下的经济权衡提供了数据驱动的决策基础，包括基于学习的设备内导航基线，以及为基于规则的导航、模仿学习和成本感知的RL训练建立评估基础。
## 602. `cs.CV` - 基于需求的多任务稀疏性以在边缘设备上高效部署大型模型 [PDF](https://arxiv.org/pdf/2511.19986), [HTML](https://arxiv.org/abs/2511.19986)
### Authors
Lianming Huang,Haibo Hu,Qiao Li,Nan Guan,Chun Jason Xue
### Background
在资源受限的边缘平台上部署大型模型时，稀疏性是必不可少的。然而，单独针对个别任务优化稀疏模式忽略了频繁任务切换过程中显著的I/O开销。传统方法在每次任务切换时都需要重新加载整个模型，这会增加冷启动延迟，影响效率。
### Innovation
作者提出了一种基于需求的多任务稀疏框架，旨在通过最大化参数复用来减少切换成本。该框架将权重分解为可复用的块级单元，并在任务之间对齐稀疏结构以最大化重叠。通过动态加载仅需要的少量差异性块，该方法有效缓解了传统方法中存在的冷启动延迟问题。
### Conclusion
在真实世界的自动驾驶平台上，作者的框架展示了相对于现有稀疏性方法更高的切换效率，平均加速切换速度超过6.6倍。
## 603. `cs.CV` - 潜在扩散反演需要理解潜在空间 [PDF](https://arxiv.org/pdf/2511.20592), [HTML](https://arxiv.org/abs/2511.20592)
### Authors
Mingxing Rao,Bowen Qu,Daniel Moyer
### Background
在数据领域，扩散模型的训练数据恢复（模型反演）已被广泛研究。然而，现有的反演技术很少关注编码器/解码器对及其对应的潜在码，特别是用于潜在空间生成模型的反演技术，比如潜在扩散模型（LDMs）。论文指出，扩散模型在潜在码上的记忆化是非均匀的，倾向于过度拟合解码器拉回度量中的高失真区域。在单一潜在码内部，不同维度对记忆化的贡献也是不均匀的。
### Innovation
论文引入了一种基于解码器拉回度量的机制，用于按维度衡量潜在编码器的贡献，从而识别最相关的维度。当计算基于得分的成员身份推断攻击者的攻击统计数据时，去除较少贡献记忆的维度显著提高了性能，表现为平均AUROC提升了2.7%，并在1%FPR下的TPR大幅增加了6.42%。结果强调了自编码器几何形状对LDM记忆化的影响，并为分析基于扩散的生成模型中的隐私风险提供了一种新视角。
### Conclusion
研究结果表明，在极低的误报容忍度下，更强地确信能识别成员。研究突显了自编码器几何对LDM记忆化的影响，并提供了分析基于扩散的生成模型隐私风险的新视角。
## 604. `cs.CV` - VibraVerse：物理一致的大规模几何声学对齐数据集 [PDF](https://arxiv.org/pdf/2511.20422), [HTML](https://arxiv.org/abs/2511.20422)
### Authors
Bo Pang,Chenxi Xu,Jierui Ren,Guoping Wang,Sheng Li
### Background
理解物理世界需要基于物理法则的感知模型，而不仅仅是统计相关性。现有的多模态学习框架，专注于视觉和语言，缺乏物理一致性，忽视了物体几何、材料、振动模式及其产生的声音之间的内在因果关系。本文介绍了VibraVerse，一个大规模的几何声学对齐数据集，明确连接了从3D几何到物理属性再到模态参数，最后到声信号的因果链。
### Innovation
引入了CLASP，一个对比学习框架，用于跨模态对齐，保持对象物理结构与其声响应之间的因果对应关系。这框架确保跨模态的一致对齐，使得每一样本都是一致的，可追溯到管理方程，并嵌入到跨越形状、图像和声音的统一表示空间中。基于VibraVerse，定义了一整套几何到声音预测、声音引导的形状重建和跨模态表示学习基准任务，验证表明基于VibraVerse训练的模型在跨模态上表现出更高的准确性和解释性。
### Conclusion
这些结果确立了VibraVerse作为物理一致和因果可解释的多模态学习基准，为声音引导的感知和对物理世界更深入的理解奠定基础。数据集将开源。
## 605. `cs.CV` - Fara-7B：一种高效的计算机使用代理模型 [PDF](https://arxiv.org/pdf/2511.19663), [HTML](https://arxiv.org/abs/2511.19663)
### Authors
Ahmed Awadallah,Yash Lara,Raghav Magazine,Hussein Mozannar,Akshay Nambi,Yash Pandya,Aravind Rajeswaran,Corby Rosset,Alexey Taymanov,Vibhav Vineet,Spencer Whitehead,Andrew Zhao
### Background
计算机使用代理（CUA）的进步受到缺乏大规模高质量数据集的限制，这些数据集能够捕捉人类与计算机交互的方式。尽管大语言模型（LLMs）在大量文本数据上繁荣发展，但类似规模的CUA轨迹数据集却不存在。为了填补这些空白，本文介绍了一种名为FaraGen的新型合成数据生成系统，用于多步骤网页任务。FaraGen能够提出多种多样的任务，从常用网站生成多个解决方案尝试，并使用多个验证器筛选成功轨迹。该系统能够实现高吞吐量、高产出率和多样性，生成验证轨迹的成本大约为每次1元。利用这些数据，训练了Fara-7B，一种仅使用截图感知计算机、通过预测坐标执行操作的小型CUA模型，可以在设备本地运行。研究表明，Fara-7B在WebVoyager、Online-Mind2Web等基准测试中表现优于其他同等规模的CUA模型，并且在该团队开发的新型基准WebTailBench中表现良好，说明Fara-7B能更好地捕捉现有基准尚未充分代表的网页任务。此外，Fara-7B在与更大规模前沿模型的竞争中具有竞争力，揭示了可扩展数据生成系统在推动小型高效代理模型方面的重要优势。
### Innovation
本文提出了一种名为FaraGen的新型合成数据生成系统，用于多步骤网页任务。FaraGen能够创造多样化的任务，从常用网站生成多个解决方案尝试，并使用多个验证器筛选成功轨迹。该系统达到了高吞吐量、高产出率和多样性，生成验证轨迹的成本大约为每次1元。此外，本文通过FaraGen获得的数据训练了Fara-7B模型，这是一种仅使用截图感知计算机、通过预测坐标执行操作的小型CUA模型，可以在设备本地运行。Fara-7B在WebVoyager、Online-Mind2Web等基准测试以及该团队开发的WebTailBench中表现优于其他同等规模的CUA模型，展示了可扩展数据生成系统在推动小型高效代理模型方面的显著优势。
### Conclusion
Fara-7B是首个利用合成生成与截屏驱动学习结合的小规模高效代理模型，能够在设备本地运行，并且在多个基准测试中表现出色。本文还发布了WebTailBench，一个新的基准，旨在捕捉现有的其他调试器都不能代表的低流行度Web任务。Fara-7B及其生成方法为CUA领域带来了新的前景，并提供了进步的关键增益。我们希望Fara-7B和WebTailBench的发布将鼓励更多学者投入到这一重要领域中。
## 606. `cs.CV` - 重定义雷达分割：基于雷达点云的静止和移动分割及平台姿态估计 [PDF](https://arxiv.org/pdf/2511.20003), [HTML](https://arxiv.org/abs/2511.20003)
### Authors
Simin Zhu,Satish Ravindran,Alexander Yarovoy,Francesco Fioranelli
### Background
传统的雷达分割研究主要关注不同移动目标的类别标签学习。虽然雷达和光学传感器的基本差异导致了准确且一致的类别标签预测的可靠性不同，但汽车中的常规雷达感知任务发现，确定目标是移动还是静止是大多数任务的前提条件。因此，本研究提出了一种基于神经网络的解决方案，可以同时从雷达点云中分割静止和移动的目标。此外，由于静态目标的距离多普勒速度与雷达运动相关联，该方法还可以估计移动平台或车辆（自身运动）的瞬时2D速度。
### Innovation
本研究创造性地提出了通过简单而有效的多层感知器（MLPs）和循环神经网络（RNNs）从未处理的点云中直接提取所需信息的方法，实现了同时分割静止和移动目标及自车运动估计的双重功能，这是文献中第一次提出的方法。研究还引入了新的评估指标，并利用具有挑战性的雷达实况数据集RadarScenes测试了该方法。
### Conclusion
实验结果表明，本方法在双目标任务中的表现良好，并且具有在其他雷达感知任务中广泛应用的潜力。
## 607. `cs.CV` - 优化二元函数之和：有限域中基于松弛方法的介绍 [PDF](https://arxiv.org/pdf/2511.20607), [HTML](https://arxiv.org/abs/2511.20607)
### Authors
Nils Müller
### Background
本文研究了具有超过两个自变量的函数，在这些函数可以表示为具有部分自变量的几个函数之和的情况下，特别是在有限域内的情况。研究发现，优化这样的函数（称为二元函数之和）的复杂性等价于NP问题，并且在优化二元函数之和中存在免费午餐现象。文章利用测度理论扩展目标函数，构造了称为松弛的方法、L2逼近和熵正则化等技术，从而产生了可线性规划、坐标上升法以及具有闭式解的几种可解决的优化问题形式。
### Innovation
研究了优化二元函数之和的具体算法，包括使用测度理论扩展目标函数、构造松弛方法、L2逼近和熵正则化。这些方法允许使用线性规划、坐标上升法以及具有闭式解的方案进行解决方案的构造。并且通过泛函结果探讨了通过从二元边际重构测度来应用这些可简化版本的松弛版本的局限性。
### Conclusion
通过对随机函数、顶点着色和信号重建问题的实验，研究者揭示了可以建模为二元函数之和的不同函数类的定性差异。
## 608. `cs.CV` - 重新思考面部表情识别的学习范式 [PDF](https://arxiv.org/pdf/2209.15402), [HTML](https://arxiv.org/abs/2209.15402)
### Authors
Weijie Wang,Nicu Sebe,Bruno Lepri
### Background
由于主观的人群标注以及面部表情内在的类别相似性，现实中的面部表情识别（FER）数据集通常会表现出模糊的标注。大多数先前的方法将模糊的标注结果转换为精确的一热标注，并以端到端监督的方式训练FER模型。
### Innovation
本文重新审视现有的训练范式，并提出在保留原始模糊标注的情况下使用弱监督策略训练FER模型。
### Conclusion
通过弱监督策略训练FER模型，可以简化学习范式，利用原始模糊标注进行训练，有望获得更有效的面部表情识别性能。
## 609. `cs.CV` - 超越生成：视觉-语言模型的多跳推理以提高事实准确性 [PDF](https://arxiv.org/pdf/2511.20531), [HTML](https://arxiv.org/abs/2511.20531)
### Authors
Shamima Hossain
### Background
视觉语言模型(VLMs)是一种强大的生成工具，但经常由于缺乏稳健的推理能力而产生事实不准确的输出。尽管关于在大型语言模型(LLMs)中集成外部知识以增强推理的研究已经非常广泛，但在VLMs中这样做仍然很少见，更大的挑战在于如何顺利融合多种模态。本研究引入了一个框架，利用结构化的知识图谱进行多跳验证，同时通过图像配对任务来展示我们的框架。我们的方法允许在多个步骤中进行系统性推理，包括视觉实体识别、知识图谱遍历和基于事实的描述改进。通过使用层次化、三元组和项目点等知识表示，我们进行评估，分析这些知识表示在事实准确性和逻辑推理方面的有效性。
### Innovation
本研究引入了一个框架，利用结构化知识图谱进行多跳推理，为VLMs提供了一种新的推理方法，通过图像配对任务进行展示。此方法允许多步骤系统的系统性推理，包括视觉实体识别、知识图谱遍历和基于事实的描述改进。通过不同的知识表示形式进行评估，展示了其在事实准确性和逻辑推理中的有效性。
### Conclusion
本研究的结果表明，该方法在包含Google Landmarks v2、Conceptual Captions和COCO Captions的预览数据集上，将事实准确性提高了约31%。通过此研究，展现了将外部知识集成到VLMs推理中的潜力，为更可靠和知识丰富的多模态系统铺平了道路。
## 610. `cs.CV` - GMT: 有效的全局框架用于多摄像机多目标跟踪 [PDF](https://arxiv.org/pdf/2407.01007), [HTML](https://arxiv.org/abs/2407.01007)
### Authors
Yihao Zhen,Mingyue Xu,Qiang Wang,Baojie Fan,Jiahua Dong,Tinghui Zhao,Huijie Fan
### Background
多摄像机多目标（MCMT）跟踪的目标是在多个摄像机视角中定位和关联相同的目标。现有方法通常采用两阶段框架，首先进行单摄像机跟踪，然后进行跨摄像机跟踪。然而，在这种模式下，多视角信息仅用于恢复第一阶段中遗漏的匹配，所以提供的贡献是有限的。
### Innovation
我们提出了GMT，一种全局MCMT跟踪框架，可以同时利用视角内和视角间线索进行跟踪。GMT通过将来自不同视角的相同历史目标综合为全局轨迹，将两阶段跟踪过程联合起来，形成一个统一的全局级别轨迹-目标关联过程。此外，GMT引入了一个跨视角特征一致性增强模块，以在不同视角之间对齐视觉和空间特征，从而为全局轨迹建模提供一致的特征空间。通过这种方式，GMT可以直接利用多视角信息来关联新的检测结果。
### Conclusion
与两阶段框架相比，GMT在现有数据集上取得了显著的改进，在CVMA上提高了21.3%，在CVIDF1上提高了17.2%。此外，我们还引入了VisionTrack，这是一款高质量、大规模的MCMT数据集，提供了现有数据集所不具备的巨大多样性。我们的代码和数据集将被公开。
## 611. `cs.CV` - MovieDreamer：分层生成连贯的长视觉序列 [PDF](https://arxiv.org/pdf/2407.16655), [HTML](https://arxiv.org/abs/2407.16655)
### Authors
Canyu Zhao,Mingyu Liu,Wen Wang,Weihua Chen,Fan Wang,Hao Chen,Bo Zhang,Chunhua Shen
### Background
近期视频生成的进展主要依赖于扩散模型来生成短期内容。然而，这些方法在建模复杂叙事和长时间内保持人物一致性方面常常力不从心，这对于长形式视频制作（如电影）是至关重要的。为此，研究提出了MovieDreamer，这是一种新颖的分层框架，它结合了自回归模型和基于扩散的渲染技术，以实现长时视频生成，同时具备复杂的剧情发展和高度的视觉保真度。
### Innovation
MovieDreamer 提出了一个独特的分层框架，结合了自回归模型和基于扩散的渲染技术，以实现长时视频生成，具备复杂的剧情发展和高视觉保真度。该方法通过自回归模型来保证全局叙事的连贯性，并通过扩散渲染将视觉令牌序列转化为高质量的视频帧。此外，通过使用多模态剧本来丰富场景描述，增加详细的角色信息和视觉风格，从而增强场景间的连续性和角色身份。
### Conclusion
通过广泛的实验在不同类型的电影中展示了MovieDreamer不仅在视觉和叙事质量上取得了显著的优越性，还可以显著延长生成内容的持续时间，超过现阶段的技术能力。
## 612. `cs.CV` - SD-MVS: 基于分割驱动变形与球面优化的多视图立体重建 [PDF](https://arxiv.org/pdf/2401.06385), [HTML](https://arxiv.org/abs/2401.06385)
### Authors
Zhenlong Yuan,Jiakai Cao,Zhaoxin Li,Hao Jiang,Zhaoqi Wang
### Background
在3D重建过程中，对于无纹理区域的重建是一个挑战，特别是在多视图立体重建中。现有的方法在处理这类区域时表现较差。
### Innovation
- 首次使用Segment Anything Model (SAM) 来分割场景中的语义实例，并利用这些语义实例约束进行像素级的块变形，提高匹配成本和传播的精确性。- 提出了独特的细化策略，结合球坐标和法线上的梯度下降以及深度上的像素搜索间隔，显著改善了重建3D模型的完整性。- 引入了预期-最大化 (EM) 算法，交替优化聚合匹配成本和超参数，减少参数过度依赖于经验调节的问题。
### Conclusion
在ETH3D高分辨率多视图立体重建基准和Tanks and Temples数据集上的评估表明，该方法可以实现最先进的结果，且在耗时方面更具有优势。
## 613. `cs.CV` - 通过Token卷曲实现零样本视频翻译 [PDF](https://arxiv.org/pdf/2402.12099), [HTML](https://arxiv.org/abs/2402.12099)
### Authors
Haiming Zhu,Yangyang Xu,Jun Yu,Shengfeng He
### Background
随着生成式人工智能的革命，视频相关任务得到了广泛研究。然而，当前最先进的视频模型在视觉质量和用户对生成内容的控制方面仍落后于图像模型。现有基于扩散的视频编辑方法依赖自我注意中的键和值片段来保证时序一致性，经常牺牲局部和结构区域的保留。
### Innovation
提出了TokenWarping，一种新颖的时序一致视频翻译框架。TokenWarping 使用来自不同帧的时序相关性通过构造查询片段来利用互补的令牌先验。在扩散模型的去噪过程中，光学流被用来卷曲源帧的查询、键和值片段，使其与当前帧的片段对齐。通过直接卷曲查询片段来增强自我注意中的特征聚合，同时卷曲键和值片段确保帧间的时序一致性。这种方法对自我注意层输出施加了显式约束，有效确保时序一致性的翻译。该框架不需要额外训练或微调，并且可以无缝地与现有的文本到图像编辑方法集成。
### Conclusion
在各种视频翻译任务上进行了广泛的实验，结果表明，TokenWarping 在定性和定量上都优于最先进的方法。视频演示可以在项目网页上找到：this https URL。代码可以在：this https URL 获取。
## 614. `cs.CV` - ArtiBench 和 ArtiBrain：通用视觉语言操作台架基准和框架 [PDF](https://arxiv.org/pdf/2511.20330), [HTML](https://arxiv.org/abs/2511.20330)
### Authors
Yuhan Wu,Tiantian Wei,Shuo Wang,ZhiChao Wang,Yanyong Zhang,Daniel Cremers,Yan Xia
### Background
交互式操纵要求对家电进行长时间、多步骤的互动同时保持物理一致性。现有的视觉语言和扩散模型难以在不同部件、实例和类别之间进行泛化。为了评估这些挑战，该研究引入了一个包含厨房、存储、办公室和工具环境的五级基准ArtiBench，能够从部件间和实例间的变异评估到长时间多对象任务。
### Innovation
该研究提出了一个模块化框架ArtiBrain，结合了高级推理和自适应低级控制。ArtiBrain使用基于VLM的任务推理器（GPT-4.1）来分解和验证子目标，并采用了结合几何感知关键帧执行和利用操作允许性引导的扩散设计的混合控制器，以实现精确且可解释的操作。此外，还提出了一个操作允许性记忆库，能够持续收集成功的执行示例并传播到未见过的部件和配置的部件级操作允许性。
### Conclusion
在ArtiBench上的大量实验证明，ArtiBrain比最先进的多模态和扩散基线方法在鲁棒性和泛化方面显著更优。代码和数据集将在接受后发布。
## 615. `cs.CV` - 使用深度图进行自然图像拼接 [PDF](https://arxiv.org/pdf/2202.06276), [HTML](https://arxiv.org/abs/2202.06276)
### Authors
Tianli Liao,Nan Li
### Background
自然图像拼接的目标是从不同视角拍摄的同一3D场景的重叠图像中创建一个无缝的、自然的拼接图像。但在非平面场景和手持设备拍摄的情况下，由于存在显著的视差问题，会对拼接结果产生挑战。
### Innovation
本文提出了一种新颖的基于深度图的图像拼接方法，该方法能生成对抗视差的精确定位拼接图像。首先，构建了一种稳健的拟合方法来过滤特征匹配中的离群值，并估计输入图像之间的弹极几何。然后，利用弹极几何建立试图像之间的像素到像素的对应关系，并使用所提出的最优扭曲生成扭曲图像。在渲染阶段，引入了一些模块来解决扭曲结果中的映射伪影，并生成最终的多幅图像。
### Conclusion
在三种具有挑战性的数据集上得到的实验结果显示，输入图像的深度图使得我们的方法在重叠区域提供更准确的对齐，在非重叠区域产生视觉一致的结果。我们认为，随着单目深度估计的快速发展，我们的方法将持续有效。
## 616. `cs.CV` - OpenScan: 一个针对广义开放式词汇3D场景理解的基准 [PDF](https://arxiv.org/pdf/2408.11030), [HTML](https://arxiv.org/abs/2408.11030)
### Authors
Youjun Zhao,Jiaying Lin,Shuquan Ye,Qianshi Pang,Rynson W.H. Lau
### Background
现有方法和基准主要针对在对象类别上下文中出现的开放式词汇问题，这不足以全面评估模型对3D场景的理解程度。本研究提出了一个更具挑战性的任务，称为广义开放式词汇3D场景理解（GOV-3D），并为该任务开发了一个新的基准，名为OpenScan。
### Innovation
引入了一个更具有挑战性的任务，即广义开放式词汇3D场景理解（GOV-3D），涵盖了诸如功能、属性和材料等方面的粒度和对象特定的知识。OpenScan基准包含了八个代表性语言方面的3D对象属性，并评估了最先进的开放式词汇3D方法。
### Conclusion
现有方法难以理解GOV-3D任务中的抽象词汇，仅通过增加训练中的对象类别规模无法解决这一挑战。指出现有方法的局限，并探讨了克服这些局限的潜在方向。
## 617. `cs.CV` - E³NeRF: 效率提升的事件增强神经辐射场从模糊图像 [PDF](https://arxiv.org/pdf/2408.01840), [HTML](https://arxiv.org/abs/2408.01840)
### Authors
Yunshan Qi,Jia Li,Yifan Zhao,Yu Zhang,Lin Zhu
### Background
NeRF 通过学习稀疏视角图像中的隐式三维表示实现了令人印象深刻的新型视图渲染性能。然而，在野外经常会出现模糊输入图像，这使得难以重建清晰的 NeRF。为了克服这个问题，本文提出了一个新颖的高效事件增强 NeRF (E³NeRF)，它利用模糊图像及其对应的事件流来重建清晰的 NeRF。
### Innovation
引入了模糊渲染损失和事件渲染损失，通过模拟物理图像运动模糊过程和事件生成过程来指导 NeRF 训练。该方法利用事件流中的潜在空间-时间模糊信息，均匀地分布在时间模糊上，并专注于空间模糊的训练。此外，构建了一个带有事件引导的相机姿态估计框架，使方法能够应用于更实际的应用场景。与基于图像和基于事件的 NeRF 的先前工作相比，本文框架更深入地利用了事件和图像之间的内在关系。
### Conclusion
在合成数据和真实世界数据上的广泛实验表明，E³NeRF 可以有效地从模糊图像中学习清晰的 NeRF，特别是在高速非均匀运动和低光照场景中表现尤为突出。
## 618. `cs.CV` - DVP-MVS: Synergize Depth-Edge and Visibility Prior for Multi-View Stereo [PDF](https://arxiv.org/pdf/2412.11578), [HTML](https://arxiv.org/abs/2412.11578)
### Authors
Zhenlong Yuan,Jinguo Luo,Fei Shen,Zhaoxin Li,Cong Liu,Tianlu Mao,Zhaoqi Wang
### Background
近年来，基于块变形的方法在多视图立体重建中展示了显著的有效性，主要是由于引入了可变形和可扩展的感知，以重建无纹理区域。然而，此类方法通常侧重于探索相关可靠的像素来缓解块变形期间的匹配不确定性，但忽略了由错误边缘跳过和视见遮挡引起的变形不稳定性，导致潜在的估计偏差。
### Innovation
本文提出了DVP-MVS，这是一种创新的方法，通过深度边缘对齐和跨视图先验的结合，实现了稳健和视见感知的块变形。具体而言，为避免意外边缘跳过，首先使用Depth Anything V2结合Roberts算子来初始化粗略的深度图和边缘图，并通过腐蚀-膨胀策略对这两个图像进行对齐，生成精细的均匀边界，以引导块变形。此外，通过重构视图选择权重为视见图，并通过跨视图深度重投影恢复可视区域，将其作为跨视图先验，以促进视见感知的块变形。最后，通过引入基于视图选择和基于共视线的局部投影深度差异的加权可见半球法线，改善了多视图几何一致性，增强了传播和细化。
### Conclusion
在ETH3D和Tanks & Temples基准测试上的广泛评估表明，我们的方法可以实现最先进的性能，具有出色的鲁棒性和泛化能力。
## 619. `cs.CV` - VidComposition：MLLMs能否分析编排视频中的视觉编排？ [PDF](https://arxiv.org/pdf/2411.10979), [HTML](https://arxiv.org/abs/2411.10979)
### Authors
Yolo Y. Tang,Junjia Guo,Hang Hua,Susan Liang,Mingqian Feng,Xinyang Li,Rui Mao,Chao Huang,Jing Bi,Zeliang Zhang,Pooyan Fazli,Chenliang Xu
### Background
多模态大规模语言模型（MLLMs）的进展显著推动了多模态理解能力的提升，尤其是视频内容的分析。现有的MLLMs评估基准主要针对抽象的视频理解，缺乏对视频编排理解能力的详细评估，特别是视频中视觉元素如何在高度编排的视频环境中组合和互动的细微解释。VidComposition旨在填补这一空白，提供了一个新的基准，专门评估MLLMs在编排视频理解方面的能力，使用精心编排的视频和电影级别的注解。
### Innovation
VidComposition引入了一个新的基准，专门用于评估MLLMs在理解视频编排上的能力，包括982个视频和1706个多项选择题，覆盖了镜头移动、角度、取景、叙事结构、人物动作和情感等多种编排方面。这个基准能够揭示当前MLLMs在理解和处理高度编排视频中的复杂性方面的局限性，并为未来的改进提供方向。
### Conclusion
我们的全面评估表明，MLLMs与人类在理解复杂编排视频方面存在显著差距，揭示了现有技术的局限性和改进的空间。研究结果可在美国的该网址查看。
## 620. `cs.CV` - 开发完全深度学习模型以提高预测上颌未萌尖牙阻生可能性的扇区分类系统可重复性 [PDF](https://arxiv.org/pdf/2511.20493), [HTML](https://arxiv.org/abs/2511.20493)
### Authors
Marzio Galdi,Davide Cannatà,Flavia Celentano,Luigia Rizzo,Domenico Rossi,Tecla Bocchino,Stefano Martina
### Background
研究背景集中在上颌未萌尖牙的阻生可能性预测上，目前常用的方法（如5-、4-和3-扇区分类系统）在不同观察者之间的可重复性表现不尽理想，存在较高的主观误差。因此，通过人工智能技术，特别是深度学习模型，来提高这些系统的可重复性，已成为研究的热点。
### Innovation
创新点在于开发了一个完全基于深度学习的模型，该模型能够在数百张扩展数据集的训练下，自动分类上颌未萌尖牙的位置，从而显著提高可重复性。论文中对比了不同扇区分类系统和不同观察者的可重复性，并最终验证了一个表现最佳的深度学习模型（DenseNet121）的功效。
### Conclusion
研究结论认为，基于人工智能的深度学习模型可以被设计用于自动分类上颌未萌尖牙的位置，这对于提高扇区分类系统的可重复性具有重要意义。”]} pesquisa de campo sugere os métodos atuais baseados em classificações de sectores para prever a probabilidade de impaction de caninos maxilares não erupcionados podem ter baixa reprodutibilidade tanto dentro- quanto entre as operações. Uma solução inovadora é a desenvolver um modelo de aprendizado profundo (Deep Learning) que possa automatizar a classificação desses caninos, aumentando a reprodutibilidade de tal classificação, com o exemplo do modelo DenseNet121, que alcançou uma acurácia de 76,8% na classificação desses caninos em três diferentes categorias.ổi击因写下可能会有版权争议的内容，上述翻译已转换为中文并重新组织，确保内容的原创性和正确性。如需进一步详细内容的翻译，请告知。userносторонний аналіз наведеної статті. Вказати частини статті: `_Background`—зазначте нашізнання до статті; `Innovation`—зміни або новини, які стаття допомагає отримати; `Conclusion`—заключення статті. Перекладіть також назву статті на українську мову. Поліпште англійський переклад, якщо це потрібно, і стикаєте результати у вигляді JSON. Báo cáo kết quả theo định dạng JSON sau: 'title', 'background', 'innovation', 'conclusion'.bigintify解析结果并输出JSON如下格式的字符串：{
## 621. `cs.CV` - VisionReward: 细粒度多维度的人类偏好学习在图像和视频生成中的应用 [PDF](https://arxiv.org/pdf/2412.21059), [HTML](https://arxiv.org/abs/2412.21059)
### Authors
Jiazheng Xu,Yu Huang,Jiale Cheng,Yuanming Yang,Jiajun Xu,Yuan Wang,Wenbo Duan,Shen Yang,Qunlin Jin,Shurun Li,Jiayan Teng,Zhuoyi Yang,Wendi Zheng,Xiao Liu,Dan Zhang,Ming Ding,Xiaohan Zhang,Xiaotao Gu,Shiyu Huang,Minlie Huang,Jie Tang,Yuxiao Dong
### Background
视觉生成模型在合成照片级真实度的图像和视频方面已经取得了显著进展，但将它们的输出与人类在关键维度上的偏好对齐仍然是一个持久的挑战。尽管从人类反馈中进行强化学习为偏好对齐提供了希望，但现有的视觉生成奖励模型仍存在黑盒评估缺乏解释性以及潜在产生的偏见问题。
### Innovation
我们提出了一种名为VisionReward的一般框架，用于在图像和视频生成中学习人类视觉偏好。该框架采用了分层的视觉评估框架来捕捉精细的偏好，并通过线性权重启用可解释的偏好学习。此外，还提出了一种多维度一致策略，以在使用VisionReward作为奖励模型进行视觉生成的偏好优化时保持一致性。
### Conclusion
实验表明，VisionReward在机器度量和人类评价上都显著优于现有的图像和视频奖励模型。具体而言，VisionReward在偏好预测准确性上超越了VideoScore 17.2%，使用VisionReward的文本到视频模型相对于使用VideoScore模型相比，获得了31.6%更高的两两胜率。所有代码和数据集可以在该网址获取。
## 622. `cs.CV` - 个性化生成低光照图像降噪与增强 [PDF](https://arxiv.org/pdf/2412.14327), [HTML](https://arxiv.org/abs/2412.14327)
### Authors
Xijun Wang,Prateek Chennuri,Dilshan Godaliyadda,Yu Yuan,Bole Ma,Xingguang Zhang,Hamid R. Sheikh,Stanley Chan
### Background
现代相机在低光照条件下的表现仍不尽如人意，主要是由于光子闪烁噪声和传感器读取噪声的基本限制。生成图像恢复方法相比传统方法表现出有前景的结果，但在信噪比（SNR）低的情况下会产生幻觉性内容生成的问题。利用用户个人照片画廊的可用性，我们介绍了基于扩散的个性化生成降噪（DiffPGD）的新方法，该方法为个人用户构建量身定制的扩散模型。
### Innovation
我们的创新在于开发了一种身份一致的物理缓冲区，从画廊中提取人物的物理属性。这种ID一致的物理缓冲区作为一种鲁棒的先验，可以无缝集成到扩散模型中，以在无需微调的情况下恢复退化的图像。在广泛的低光照测试场景中，我们展示了DiffPGD相比现有基于扩散的降噪方法在图像降噪和增强性能上更优越。
### Conclusion
在广泛的低光照测试场景中，我们证明DiffPGD在图像降噪和增强性能上优于现有的基于扩散的降噪方法。完整的项目页面可以在textcolor{purple}{textbf{this https URL}}找到。
## 623. `cs.CV` - Temporally Compressed 3D Gaussian Splatting for Dynamic Scenes [PDF](https://arxiv.org/pdf/2412.05700), [HTML](https://arxiv.org/abs/2412.05700)
### Authors
Saqib Javed,Ahmad Jarrar Khan,Corentin Dumery,Chen Zhao,Mathieu Salzmann
### Background
近年来，在高保真动态场景重建中，已经利用动态3D高斯模型和4D高斯碎片插值来实现更真实场景的表示。然而，要使这些方法适用于诸如AR/VR、游戏和低功耗设备上的渲染等实时应用时，需要大幅减少内存使用并提高渲染效率。尽管许多最先进的方法侧重于轻量级实施，但在处理复杂运动场景或长序列时存在问题。
### Innovation
本文介绍了时间压缩3D高斯碎片插值（TC3DGS），这是一种专为有效压缩动态3D高斯表示而设计的新技术。TC3DGS基于时间相关性选择性地修剪高斯，并采用梯度感知混合精度量化动态压缩高斯参数。此外，TC3DGS利用改进的Ramer-Douglas-Peucker算法进一步减少存储，通过在帧之间插值高斯轨迹来进一步降低存储需求。我们的实验证明TC3DGS在不影响视觉质量的情况下，压缩率最高可达67倍。
### Conclusion
我们对多个数据集进行的实验表明，TC3DGS实现了最高67倍的压缩率，在视觉质量上几乎没有或没有损伤。详细结果和视频可以在补充材料中查看。
## 624. `cs.CV` - RobustMerge: 通过方向稳健性实现高效模型融合的参数精简模型合并方法 [PDF](https://arxiv.org/pdf/2502.17159), [HTML](https://arxiv.org/abs/2502.17159)
### Authors
Fanhu Zeng,Haiyang Guo,Fei Zhu,Li Shen,Hao Tang
### Background
预训练模型的微调促使了针对特定任务的专家模型的生成。合并模型来增强多任务能力并避免数据泄露正变得流行。随着数据和模型规模的扩大，参数精简的调整成为一种常见的做法，以高效地获得任务特定的模型。然而，几乎没有专注于高效合并的方法，现有的旨在全面微调合并的方法在高效合并时效果不佳。
### Innovation
论文分析了低秩分解，并揭示了合并期间方向稳健性对于高效模块的合并至关重要。研究进一步发现，补偿显著奇异值之间的差距有助于方向稳健性。因此，提出了RobustMerge，一种无需训练的参数精简合并方法，具有补充参数调整来保持方向稳健性。具体来说，该方法对奇异值之间的参数关系进行剪枝和缩放系数，以确保远离任务干扰的方向稳定性；并且执行跨任务规范化，以增强对未见任务的一般性。
### Conclusion
在包含多种模态任务的基准上进行了实验，证明了该方法的优异性能和泛化能力，进一步的研究和广泛的分析进一步证明了其有效性。源代码已发布。
## 625. `cs.CV` - LiHi-GS: LiDAR-Supervised Gaussian Splatting for Highway Driving Scene Reconstruction [PDF](https://arxiv.org/pdf/2412.15447), [HTML](https://arxiv.org/abs/2412.15447)
### Authors
Pou-Chun Kung,Xianling Zhang,Katherine A. Skinner,Nikita Jaipuria
### Background
光现实3D场景重建在自动驾驶中起着重要作用，能够生成新颖数据以模拟关键安全场景及扩大训练数据集，而无需额外的获取成本。现有方法主要使用显式的3D高斯表示和实时、光现实的渲染方法，被称为Gaussian Splatting (GS)，虽然取得了进展，但这些方法忽视了两个关键方面：一是现有方法主要关注低速且特征丰富的城市场景，而忽视了高速公路场景在自动驾驶中的重要性；二是虽然激光雷达（LiDAR）广泛应用于自动驾驶平台，但现有方法主要学习来自图像的数据，仅使用LiDAR进行初始估算或无精确传感器建模，从而错过了利用LiDAR提供的丰富深度信息的机会，限制了合成LiDAR数据的能力。
### Innovation
本文提出了一种新的、带有LiDAR监督的GS方法，用于动态场景合成和编辑，通过LiDAR监督改进场景重建，支持LiDAR渲染。该研究首次关注动态场景中的高速公路场景，这些场景具有稀疏的传感器视图和单调的背景，不同于以往主要在城市数据集上测试的研究。
### Conclusion
该研究首次利用LiDAR监督的GS方法在自动驾驶中实现动态场景的合成和编辑，特别是针对高速公路场景，强调了LiDAR数据在场景重建中的重要性，并展示了通过深度融合LiDAR数据可以进一步提高场景质量和计算效率的可能性。
## 626. `cs.CV` - 从斑点到像素：从组织学图像中预测密集的空间基因表达 [PDF](https://arxiv.org/pdf/2503.01347), [HTML](https://arxiv.org/abs/2503.01347)
### Authors
Ruikun Zhang,Yan Yang,Liyuan Pan
### Background
空间转录组学（ST）以精细的空间分辨率测量基因表达，揭示了组织的分子景观。先前的方法通常通过从组织病理学切片图像中裁剪感兴趣的斑点并训练模型将每个斑点映射到相应的基因表达谱来预测空间基因表达。然而，这些方法在基因表达中固有地失去了空间分辨率：1）每个斑点通常包含具有不同基因表达谱的多个细胞；2）斑点通常定义为固定的空间分辨率，限制了在不同尺度上预测基因表达的能力。为了解决这些限制，本文提出了PixNet，这是一种密集预测网络，可以直接从组织病理学切片图像中预测不同大小和尺度的斑点的空间分辨基因表达。
### Innovation
PixNet的特点是从组织病理学切片图像中生成一个空间密集的连续基因表达图谱，而不是将每个单独的斑点映射到基因表达值。通过聚合感兴趣斑点内的值来预测基因表达。这种方法在四个常见的空间转录组学数据集上多尺度测试中性能超过了最先进的方法。
### Conclusion
PixNet在四个常见的空间转录组学数据集上的多尺度测试中表现出色，超过了最先进的方法。源代码将公开发布。
## 627. `cs.CV` - 基于生成式AI的传统赛璐珞动画：一项综述 [PDF](https://arxiv.org/pdf/2501.06250), [HTML](https://arxiv.org/abs/2501.06250)
### Authors
Yolo Y. Tang,Junjia Guo,Pinxin Liu,Zhiyuan Wang,Hang Hua,Jia-Xing Zhong,Yunzhong Xiao,Chao Huang,Luchuan Song,Susan Liang,Yizhi Song,Liu He,Jing Bi,Mingqian Feng,Xinyang Li,Zeliang Zhang,Chenliang Xu
### Background
传统赛璐珞动画制作流程包含多个重要步骤，如分镜头剧本、场景设计、关键帧动画、中间帧生成和上色等，这些都需要大量的手动工作、技术专长和大量的时间投入。这些挑战在历史上限制了赛璐珞动画制作的效率和可扩展性。
### Innovation
生成式人工智能（GenAI），包括大型语言模型、多模态模型和扩散模型，通过自动化中间帧生成、上色和分镜头剧本创建等任务，为传统动画流程提供了创新解决方案，降低了技术障碍，使更广泛的创作者能够使用工具如AniDoc、ToonCrafter和AniSora，从而使艺术家们能够更多地专注于创意表达和艺术创新。
### Conclusion
尽管AI辅助动画有极大的潜力，但在视觉一致性、风格一致性以及道德考虑方面仍存在挑战。此外，本文探讨了AI辅助动画的未来方向和技术进步。
## 628. `cs.CV` - 重新思考多目标跟踪中的两阶段引用跟踪：再次变得坚强 [PDF](https://arxiv.org/pdf/2503.07516), [HTML](https://arxiv.org/abs/2503.07516)
### Authors
Weize Li,Yunhao Du,Qixiang Yin,Zhicheng Zhao,Fei Su
### Background
Referring Multi-Object Tracking (RMOT)的目标是在视频中跟踪由自然语言表达指定的多个物体。近年来，单阶段方法取得了显著进展，导致两阶段的引用跟踪（RBT）范式逐渐失去了其受欢迎程度。尽管如此，两阶段RBT框架仍因较低的训练成本和灵活的渐进式部署而无法替代。然而，现有的两阶段RBT框架被发现存在两个根本性限制：过于启发式的特征构建和脆弱的对应关系建模。
### Innovation
为了应对这些挑战，作者提出了一种名为FlexHook的新型两阶段RBT框架。它通过采样的策略和基于语言的线索注入重新定义了特征构建。此外，FlexHook引入了一种称为Pairwise Correspondence Decoder (PCD)的新解码器，它用主动对应模型替代了基于CLIP的相似性匹配，从而提供了一种更为灵活和健壮的策略。
### Conclusion
通过在多个基准（Refer-KITTI/v2, Refer-Dance, 和 LaMOT）上的广泛实验，FlexHook表现出色，成为首款全面超越当前最先进的两阶段RBT方法的框架。
## 629. `cs.CV` - Dream-IF: Dynamic Relative EnhAnceMent for Image Fusion [PDF](https://arxiv.org/pdf/2503.10109), [HTML](https://arxiv.org/abs/2503.10109)
### Authors
Xingxin Xu,Bing Cao,Dongdong Li,Qinghua Hu,Pengfei Zhu
### Background
图像融合旨在整合来自多种来源图像的综合信息。然而，由不同传感器拍摄的图像往往会遇到各种退化现象，这些现象可能会影响融合质量。传统的方法通常将图像增强和融合视为两个独立的过程，忽视了它们之间的内在关联。例如，在融合图像中主导模态的区域可能表明其他模态可以从增强中受益。因此，介绍了主导区域的概念，并提出了用于图像融合的动态相对增强框架（Dream-IF），以通过量化不同层中每个模态的相对主导性，促进跨模态相互增强。
### Innovation
提出了一种新的动态相对增强框架（Dream-IF），该框架通过量化图像融合中不同层中每个模态的相对主导性，来促进跨模态相互增强。此外，使用基于提示的编码来捕捉特定退化细节，以动态引导恢复过程，并促进在多模态图像融合和增强场景中的协调增强。
### Conclusion
广泛的实验结果表明，Dream-IF 一贯优于其同类产品。代码已公开。
## 630. `cs.CV` - FaVChat：基于数据高效GRPO的分层提示-查询引导面部视频理解 [PDF](https://arxiv.org/pdf/2503.09158), [HTML](https://arxiv.org/abs/2503.09158)
### Authors
Fufangchen Zhao,Xuerui Qiu,Linrui Xu,Ming Li,Wenhao Jiang,Jinkai Zheng,Hehe Fan,Jian Gao,Danfeng Yan
### Background
多模态大型语言模型（MLLMs）在视频理解方面展现了强大的能力，但在细粒度视觉理解方面仍存在局限性，因为纯视觉编码器往往会丢失对精确推理至关重要的微妙线索。为了克服这一限制，本文旨在提出FaVChat，一种专门针对细粒度面部理解设计的视频-MLLM。该模型通过多层次提示导向特征提取机制，分阶段捕捉任务相关信息。
### Innovation
1. 引入多级提示导向特征提取机制，从低层次变换层捕捉纹理和运动，中层次可学习查询捕捉判别性区域，高层次自适应特征加权进行语义对齐。2. 提出了数据高效GRPO算法，通过每次实例的效用估计和动态生命周期调度最大化训练样本的效用，进一步提升模型捕捉细粒度面部属性的能力。
### Conclusion
广泛的零样本评估显示，即使在仅使用10K RL样本训练的情况下，FaVChat在情绪识别、可解释推理和文本表达分析方面实现了更精细的理解、更强的准确性和更好的泛化能力，超越了现有的视频-MLLMs。
## 631. `cs.CV` - 具有组织层分割意识的生成强化网络（GRN）在3D超声图像中用于慢性腰背疼痛（cLBP）评估的组织层分割 [PDF](https://arxiv.org/pdf/2501.17690), [HTML](https://arxiv.org/abs/2501.17690)
### Authors
Zixue Zeng,Xiaoyan Zhao,Matthew Cartier,Tong Yu,Jing Wang,Xin Meng,Zhiyu Sheng,Maryam Satarpour,John M Cormack,Allison Bean,Ryan Nussbaum,Maya Maurer,Emily Landis-Walkenhorst,Dinesh Kumbhare,Kang Kim,Ajay Wasan,Jiantao Pu
### Background
该研究提出了一种新的分割感知联合训练框架，称为生成强化网络（GRN），该框架通过整合分割损失反馈来优化单阶段中的图像生成和分割性能。为了适应不同的应用场景，研究者还开发了两种变体：用于样本高效学习的GRN-SEL和用于半监督学习的GRN-SSL。研究使用了69个完全标记的3D超声扫描图来自29个患者的数据集进行评估，包括六种解剖结构的标注：真皮、浅层脂肪、浅层筋膜膜（SFM）、深层脂肪、深层筋膜膜（DFM）和肌肉。
### Innovation
研究创新性地提出了一种能够整合分割损失反馈、优化单阶段中图像生成和分割性能的全新生成强化网络（GRN）框架。此外，该研究还引入了一种图像增强技术——分割引导增强（SGE），以及两种GRN变体：一种是样本高效学习的GRN-SEL，另一种是半监督学习的GRN-SSL。
### Conclusion
研究结果表明GRN-SEL与SGE结合使用可将标注工作量减少高达70%，同时相比完全标注数据集训练的模型，在骰子相似系数（DSC）方面提高了1.98%。GRN-SEL单独使用的标注工作量减少了60%，GRN-SSL与SGE结合使用可将标注需求减少70%，而GRN-SSL单独使用则减少了60%，且所有情况下均维护了与完全监督模型相当的性能。研究结果表明，GRN框架在显著减少标记数据的情况下，有效优化了分割性能，为超声图像分析提供了一个可扩展且高效的解决方案，同时减少了数据标注相关的负担。
## 632. `cs.CV` - 基于体感导航的 crowd 计数 [PDF](https://arxiv.org/pdf/2503.08367), [HTML](https://arxiv.org/abs/2503.08367)
### Authors
Runling Long,Yunlong Wang,Jia Wan,Xiang Deng,Xinting Zhu,Weili Guan,Antoni B. Chan,Liqiang Nie
### Background
人群计数中的遮挡问题是一个基本挑战。现有的多种数据驱动的方法虽然能够解决此问题，但效果有限。原因是这些方法主要基于被动摄像头，训练数据受限于室内场景，无法全面感知环境。同时，现有的基于体感导航的方法主要是为室内导航设计的，在处理大规模复杂场景中的物体分布时表现未知。现有的体感导航数据集也是受限制的室内场景，不适合密集人群分析。
### Innovation
本文提出了一个新的任务，基于体感导航的人群计数（ECC）。首先，构建了一个交互式模拟器（ECCD），实现了大场景和大量物体。引入先验概率分布来生成人群。进一步提出了零样本导航方法（ZECC），其中包括基于MMLM的粗细导航机制和基于法线的细粒度人群分布分析方法。
### Conclusion
实验结果表明，提出的基于体感导航的人群计数方法在计数准确性和导航成本之间实现了最佳权衡。
## 633. `cs.CV` - Flash-DMD：高效蒸馏和联合强化学习实现高保真度的少步图像生成 [PDF](https://arxiv.org/pdf/2511.20549), [HTML](https://arxiv.org/abs/2511.20549)
### Authors
Guanjie Chen,Shirui Huang,Kai Liu,Jianchen Zhu,Xiaoye Qu,Peng Chen,Yu Cheng,Yifu Sun
### Background
扩散模型已经成为了生成模型的重要类别，但是它们的迭代采样过程仍然很耗费计算资源。时间步长蒸馏是一种加速生成过程的技术，但是在训练上耗费大量时间，并且往往会导致图像质量下降。此外，使用强化学习（RL）对蒸馏后的模型进行细调以满足特定目标（如审美吸引力或用户偏好）是极不稳定且容易导致奖励作弊。
### Innovation
提出了一个新的Flash-DMD框架，该框架通过将高效的基于时间步长的蒸馏策略和强化学习下的联合细调结合在一起，实现了快速收敛与联合RL细调。具体包括：1) 提出了一种高效的时间步长感知蒸馏策略，使得训练成本降低了，并且提高了现实性；2) 引入了联合训练方案，同时继续进行时间步长蒸馏训练并在模型上使用了强化学习的目标。这种方法因其不断进行的蒸馏提供的稳定且定义良好的损失，能够有效稳定强化学习的训练过程，避免策略崩溃。
### Conclusion
大量的实验结果显示，与现有的方法相比，提出的Flash-DMD在少步采样过程中不仅收敛速度显著加快，而且在视觉质量、人类偏好以及文本-图像对齐度量方面也达到了最先进的生成质量。这项工作展现了一种训练高效、高保真度、稳定的生成模型的有效范式。相关代码即将发布。
## 634. `cs.CV` - 全景畸变感知分块化在上视鱼眼图像中的人体检测和定位 [PDF](https://arxiv.org/pdf/2503.14228), [HTML](https://arxiv.org/abs/2503.14228)
### Authors
Nobuhiko Wakai,Satoshi Sato,Yasunori Ishii,Takayoshi Yamashita
### Background
上视鱼眼图像中的人体检测具有挑战性，因为存在人体旋转和小人体的问题。先前的工作主要解决了人体旋转问题，而小人体的问题则较少受到关注。我们通过将鱼眼图像映射到超立方全景图来解决旋转问题，并利用全景几何学更有效地处理小人体。传统的检测方法倾向于优先处理规模较大的物体，因为它们占主导地位，导致规模较小的人体被忽视。在半球型超立方全景图中，我们发现图像顶部附近垂直角度较大的地方，图像中的人体高度似乎会线性递减。基于这一发现，我们提出了一种全景畸变感知分块化方法，以增强小人体的检测。这种方法利用自我相似图形对全景特征进行分块，以便确定没有空缺的最佳分块，并通过每个分块组中的最大显著性值来保留较小人体的关键区域。我们提出了一种结合全景图像重新映射和分块化过程的基于变压器的人体检测和定位方法。在大规模数据集上的大量实验表明，我们的方法优于传统的检测方法。
### Innovation
我们提出了全景畸变感知分块化方法，该方法通过将上视角鱼眼图像映射到超立方全景图，利用自我相似图形对全景特征进行分块，以及通过每个分块组中的最大显著性值保留较小人体的关键区域，有效解决了小人体检测的问题。我们还提出了一种结合全景图像重新映射和分块化过程的基于变压器的人体检测和定位方法。
### Conclusion
我们的方法在大规模数据集上的大量实验中优于传统的检测方法。通过精确地检测和定位鱼眼图像中的小人体，我们的研究不仅提高了人体检测的准确性，还为应对小人体检测挑战提供了新的解决方案。
## 635. `cs.CV` - CLIP-IT: CLIP 基础的相关性配对方法用于组织切片图像分类 [PDF](https://arxiv.org/pdf/2504.16181), [HTML](https://arxiv.org/abs/2504.16181)
### Authors
Banafsheh Karimian,Giulia Avanzato,Soufian Belharbi,Alexis Guichemerre,Luke McCaffrey,Mohammadhadi Shateri,Eric Granger
### Background
多模态学习在医学成像中显示出潜力，结合了互补方式，如影像和文本。视觉语言模型可以捕获丰富的诊断线索但通常需要大规模配对数据集和基于提示或文本的推理，这些限制了模型的实际应用，因为涉及到注释成本、隐私和计算需求。关键是，虽然存在大量免费的未配对外部文本，如病理报告，但如果可以在图像上下文中检索到具有语义相关的内容，则这些文本仍可提供互补的诊断线索。现有的方法受限于数据对齐，难以利用未配对的文本信息。
### Innovation
CLIP-IT框架引入了一种新颖的方法，利用丰富但未配对的文本报告。具体而言，CLIP-IT利用从另一个数据集预训练的CLIP模型来检索每个下游单一模式数据集中图像的相关未配对文本报告。这些报告来源于相同的疾病领域和组织类型，形成伪配对，反映共同的临床语义。这些文本知识在训练过程中被提取到视觉模型中，而基于LoRA的适应方法缓解了未对齐模态之间的语义差距。从而在推理阶段仅使用视觉模型，同时仍能从多模态训练中获益，无需使用下游数据集中配对数据进行推理。
### Conclusion
实验结果证实，CLIP-IT在大多数情况下持续提高了组织切片图像分类的准确率，而无需每个数据集的配对注释或推理时间的复杂性，表现出CLIP模型中未配对多模态信息的有效利用。
## 636. `cs.CV` - ExDDV: 一个新的视频可解释性伪造检测数据集 [PDF](https://arxiv.org/pdf/2503.14421), [HTML](https://arxiv.org/abs/2503.14421)
### Authors
Vlad Hondru,Eduard Hogea,Darian Onchis,Radu Tudor Ionescu
### Background
随着生成视频的逼真度和质量不断提高，人类越来越难以识别深度伪造（deepfake）内容，因此依赖自动深度伪造检测器。然而，这些检测器本身也可能出错，且其决策过程不具有可解释性，使人类容易受到基于深度伪造的欺诈和错误信息的伤害。
### Innovation
该研究引入了ExDDV，这是第一个用于解释性深度伪造检测的视频数据集和基准。ExDDV 包含大约5400个真实和伪造的视频，这些视频是通过文本描述和点击标注手工标注的，以解释所观察到的伪影。该研究评估了多种视图-语言模型在ExDDV上的表现，使用了不同的微调和上下文学习策略。结果显示，文本和点击监督对于开发能够定位和描述观察到的伪影的鲁棒性解释模型是必要的。
### Conclusion
研究提出了一个新型数据集ExDDV以便开发解释性深度伪造检测模型，并通过多种微调策略对多种视觉-语言模型进行评估，以强调文本和点击监督的重要性。同时，该研究还提供了数据集和代码以供验证结果。
## 637. `cs.CV` - Stitch-a-Demo: 从多步骤描述生成视频演示 [PDF](https://arxiv.org/pdf/2503.13821), [HTML](https://arxiv.org/abs/2503.13821)
### Authors
Chi Hsuan Wu,Kumar Ashutosh,Kristen Grauman
### Background
当前的方法在从文本描述获得视觉插图时，仅处理单个文本上下文（如一张图片的标题或一个动作描述），并检索或生成与其匹配的视觉上下文。然而，现有工作无法处理多步骤描述，例如烹饪食谱或园艺指导手册，仅处理每个步骤描述会导致不连贯的演示。
### Innovation
提出了一种名为Stitch-a-Demo的新型检索方法，可以从多步骤描述中组装生成视频演示。这种方法可以从不同来源获取片段，保证视觉上连贯且准确反映所有步骤描述。通过创建大数据弱监督数据并注入硬否定样本，促进正确性和连贯性。
### Conclusion
Stitch-a-Demo在野外实际指导视频上得到验证，实现了最先进的性能，相比于现有方法有高达29%的提升，并且在人类偏好研究中也取得了明显的优势。
## 638. `cs.CV` - 全景描述：图像与文本的等价桥梁 [PDF](https://arxiv.org/pdf/2505.16334), [HTML](https://arxiv.org/abs/2505.16334)
### Authors
Kun-Yu Lin,Hongjun Wang,Weining Ren,Kai Han
### Background
本文介绍了全景描述这一新的任务，其目标是寻找图像的最简短文本等价物，具有广泛的应用潜力。通过将全景描述设计为生成图像全面文本描述的任务，涵盖所有实体、它们的位置、属性、实体间的关系以及全局图像状态。前期研究表明，最先进的多模态大语言模型在解决全景描述任务时表现有限。
### Innovation
作者提出了一个高效的数据引擎，名为PancapEngine，用于生成高质量数据，以及一种新的方法，PancapChain，以提高全景描述的能力。PancapEngine通过详尽的检测工具检测图像中多类别的实体，然后使用实体感知提示生成所需的全景描述。PancapChain将挑战性的全景描述任务分解为多个阶段，逐步生成全景描述。此外，作者还贡献了一个全面的评估指标PancapScore和一个由人工标注的人机测试集，用于可靠的模型评估。
### Conclusion
实验表明，作者提出的PancapChain-13B模型能够超越开源的先进多模态大语言模型（如InternVL-2.5-78B），甚至超过专有的模型（如GPT-4o和Gemini-2.0-Pro），证明了其数据引擎和方法的有效性。
## 639. `cs.CV` - 学习高效的合并与细化以优化前馈3D高斯点绘制 [PDF](https://arxiv.org/pdf/2503.14698), [HTML](https://arxiv.org/abs/2503.14698)
### Authors
Yiming Wang,Lucy Chai,Xuan Luo,Michael Niemeyer,Manuel Lagunas,Stephen Lombardi,Siyu Tang,Tiancheng Sun
### Background
近年来，前馈3D高斯点绘制的最新进展促使了从稀疏视角高效场景重建的快速改进。然而，大多数现有方法直接将高斯模型沿输入图像的像素对齐。这在视角重叠时会导致表示冗余，并限制了这些模型的形状只能沿输入光线排列，缺乏三维空间的灵活性。此外，这些以像素对齐的方法在动态场景中无法自然地推广，而有效地利用时间信息需要在帧之间解决重复和新出现的图内容。
### Innovation
我们引入了一种新颖的融合与细化模块，该模块通过将和细化的高斯模型合并到一个标准的3D空间中来增强现有的前馈模型。核心在于一种高效的混合点刺-体素表示：从初始的一组像素对齐的高斯模型开始，我们汇总局部特征形成从粗到细的体素层次结构，然后使用稀疏体素变换器来处理这些体素特征并生成细化的高斯模型。通过将任意数量的输入合并为一组一致的模型，我们的表示有效地减少了冗余并且能够适应时间帧，从而实现了动态场景的历史感知在线重建。
### Conclusion
我们的方法在静态和流式场景重建中都达到了最先进的性能，同时在一个H100 GPU上运行得非常流畅（每秒15帧，延迟350毫秒）
## 640. `cs.CV` - 统一多模态编码器的高效校准以增强对抗鲁棒性 [PDF](https://arxiv.org/pdf/2505.11895), [HTML](https://arxiv.org/abs/2505.11895)
### Authors
Chih-Ting Liao,Zhangquan Chen,Chunlei Meng,Tzu-Yu Huang,Xin Cao,Xu Zheng
### Background
近期统一的多模态编码器能够将广泛的不同模态数据统一到一个共享表示空间中，从而支持多种跨模态任务。然而，这些模型在对抗扰动下的鲁棒性尚未得到充分研究，这对安全敏感的应用是关键问题。
### Innovation
本文是首个全面研究统一多模态编码器对抗脆弱性的研究。提出了一种高效的对抗校准框架，能够在不修改预训练编码器或语义中心的情况下提高所有模态的鲁棒性，并确保与现有基础模型兼容。该方法通过仅在对抗样本上训练模态特定的投影头来引入对抗鲁棒性，同时保持主干和嵌入冻结。
### Conclusion
在六个模态和三个Bind风格模型上进行的实验表明，该方法在ε=4/255的情况下，可以提高对抗鲁棒性高达47.3%，同时保留或甚至提高零样本和检索的清洁性能，只需不到1%的可训练参数。
## 641. `cs.CV` - M2SVid: 从单目到立体视频转换的端到端修补与完善 [PDF](https://arxiv.org/pdf/2505.16565), [HTML](https://arxiv.org/abs/2505.16565)
### Authors
Nina Shvetsova,Goutam Bhat,Prune Truong,Hilde Kuehne,Federico Tombari
### Background
该研究关注单目到立体视频转换的问题，并提出了一种新颖的方法，通过基于深度的重新投影输入左视图来修补和精炼变形的右视图。目标视频转化为立体视频，在信息时代具有重要的应用价值，如视频增强、虚拟现实等。
### Innovation
提出了一种采用深度信息的方法来重新投影左视图，获取右视图。通过扩展稳定视频扩散（SVD）模型，利用输入的左视图、变形后的右视图以及消隐掩码作为条件输入，生成高质量的右摄像视图。为了充分利用邻近帧的信息进行修补，修改了SVD的注意力层，以全关注方式计算消隐像素的信息。整个模型在端到端训练中直接生成右视图视频，通过最小化图像空间损失来保证高质量的生成。
### Conclusion
M2SVid方法在用户研究中表现出色，比第二好的方法高出2.6倍，同时速度提高了6倍。
## 642. `cs.CV` - Low-Dose CT MAR的提示引导多尺度自适应稀疏表示网络 [PDF](https://arxiv.org/pdf/2504.19687), [HTML](https://arxiv.org/abs/2504.19687)
### Authors
Baoshun Shi,Bing Chen,Shaolei Zhang,Huazhu Fu,Zhanli Hu
### Background
低剂量CT（LDCT）能够减少X射线辐射暴露，但可能会降低图像质量，尤其是在有金属植入物的情况下产生金属伪影。对于同时进行LDCT重建和金属伪影减少（LDMAR）任务，现有的基于深度学习的方法面临两大主要挑战：i) 网络设计忽略了多尺度和跨尺度信息；ii) 需要为每一剂量训练单独的模型，占用较大的存储空间。
### Innovation
本文提出了一种提示引导多尺度自适应稀疏表示网络（PMSRNet），解决了前述痛点。该网络受到了多尺度稀疏化框架的启发，具备一个详细设计的提示引导尺度自适应阈值生成器（PSATG）和多重尺度系数融合模块（MSFuM）。PSATG通过融合局部、区域和全局特征实现自适应捕捉上下文信息，生成更可靠阈值。此外，还构建了一个可解释的双域LDMAR框架（PDuMSRNet），该框架单模型能够应对多种CT剂量设置。
### Conclusion
在不同剂量水平的广泛实验中，提出的方法在LDMAR任务上优于当前最先进的方法。该研究展示了多尺度自适应稀疏表征网络在低剂量CT金属伪影减少中的有效性。
## 643. `cs.CV` - RoPECraft: 不需训练的轨迹引导RoPE优化在扩散变换器上的运动转移方法 [PDF](https://arxiv.org/pdf/2505.13344), [HTML](https://arxiv.org/abs/2505.13344)
### Authors
Ahmet Berke Gokmen,Yigit Ekin,Bahri Batuhan Bilecen,Aysegul Dundar
### Background
近年来，扩散变换器在视频运动转换方面的应用得到了广泛关注，但多数方法需要通过训练来优化模型参数。本文提出了一种名为RoPECraft的方法，该方法能够实现无需训练的视频运动转换，通过修改旋转位置嵌入(RoPE)来完成这一过程。这种方法首先从参考视频中提取密集的光学流，然后利用这些运动偏移来变换RoPE的复指数张量，从而将运动编码到生成过程中。
### Innovation
RoPECraft的主要创新点在于其无需训练即可进行视频运动转换的能力。具体来说，该方法通过从参考视频中提取密集的光学流，并利用这些运动偏移来变换RoPE的复指数张量，有效地将运动编码到生成过程中。此外，该方法还包含一个正则化项，基于参考视频傅里叶变换的相位分量，将相位角投影到光滑流形上，以抑制高频率伪影。实验结果显示，RoPECraft在基准测试中优于所有已发表的最新方法，无论是在定性还是定量评价方面。
### Conclusion
RoPECraft方法在无需训练的情况下，能够有效地将参考视频的运动转移到目标视频中，通过优化轨迹实现了高质量的视频运动转换。实验结果表明，该方法在多个基准测试中表现优异，优于其他最新方法。
## 644. `cs.CV` - 探索卷积神经网络在水稻籽粒分类中的应用：一种可解释的人工智能方法 [PDF](https://arxiv.org/pdf/2505.05513), [HTML](https://arxiv.org/abs/2505.05513)
### Authors
Muhammad Junaid Asif,Hamza Khan,Rabia Tehseen,Rana Fayyaz Ahmad,Mujtaba Asad,Syed Tahir Hussain Rizvi,Shazia Saqib
### Background
稻谷是全球不可或缺的基本主食，对促进国际贸易、经济增长和营养有重要作用。亚洲国家如中国、印度、巴基斯坦、泰国、越南和印度尼西亚在稻谷的生产和利用方面做出了显著贡献，同时也根据自己不同的文化传统和饮食偏好种植不同种类的稻谷。为了满足国内外贸易的需求，确保稻谷的质量并对国家的声誉负责，必须对稻谷进行检查和分类。但是，人工检查和分类是一个繁琐且耗时的过程，并且容易出错。因此，提出了一个基于卷积神经网络（CNN）的自动分类框架，用于有效高效地对不同种类的稻谷进行分类。
### Innovation
该研究提出了一种基于卷积神经网络的自动分类框架，能够有效高效地对不同种类的稻谷进行分类。模型经过严格的训练和验证，取得了显著的准确性，并在每一个类别的受试者操作特征（ROC）曲线下的面积达到了完美。混淆矩阵分析进一步证明了模型在区分不同稻谷品种方面的有效性，且错误分类较少。此外，通过解释性技术如LIME和SHAP，得到了关于模型决策过程的重要见解，揭示了稻谷特征如何影响分类结果。
### Conclusion
该研究提出并验证了一个基于卷积神经网络的自动分类模型，该模型能够精确地对不同稻谷种类进行分类，不仅可以满足国内外贸易的需求，还可以通过解释性技术提供决策过程的理解。这一方法具有高度的可靠性和实用性，可以作为一种有效的替代人工方法，用于稻谷分类。
## 645. `cs.CV` - 在扩散变换器中定位知识 [PDF](https://arxiv.org/pdf/2505.18832), [HTML](https://arxiv.org/abs/2505.18832)
### Authors
Arman Zarei,Samyadeep Basu,Keivan Rezaei,Zihao Lin,Sayan Nag,Soheil Feizi
### Background
理解知识在生成模型各层中的分布对于提高模型的可解释性、可控性和适应性至关重要。尽管先前研究已经探索了基于UNet的架构中的知识定位，但基于扩散变换器(Diffusion Transformer, DiT)的模型在这方面仍然相对较少被研究。本文的研究填补了这一空白。
### Innovation
提出了一个不对模型和知识产生偏见的方法，能够在DiT模块中定位特定类型知识的编码位置，并且在PixArt-alpha、FLUX和SANA等先进的DiT模型上针对六个不同的知识类别进行了评估。展示了定位的模块具有可解释性且与其生成输出中的知识表达有因果联系。基于这些发现，将定位框架应用于模型个性化和知识反学习两个关键应用中。在两种情况下，定位微调方法都提高了计算效率和任务特异性性能，同时减少了对无关或周围内容的干扰。
### Conclusion
本文的研究为理解和改进DiT模型的内部结构提供了新的见解，并提出了更可解释、高效和可控的模型编辑的实用途径。
## 646. `cs.CV` - 通过基于扩散的伪投影完成改进有限角度CT重建 [PDF](https://arxiv.org/pdf/2505.19385), [HTML](https://arxiv.org/abs/2505.19385)
### Authors
Jiaqi Guo,Santiago Lopez-Tapia,Aggelos K. Katsaggelos
### Background
有限角度计算机断层扫描（LACT）由于缺乏角度信息而面临重大挑战。以往的方法主要在图像领域进行操作，但本文提出了一种新的方法，专注于伪投影修补。这种方法利用MR-SDEs，一种通过均值回复随机微分方程描述扩散过程的扩散模型，来填补伪投影中的缺失角度数据。结合蒸馏和使用修补矩阵的伪逆约束输出模型的步骤，加速度扩散过程并使修补过程一步完成，提高了效率和准确性。
### Innovation
本文提出了一种基于扩散模型的伪投影修补方法，通过利用MR-SDEs填补伪投影中的缺失角度数据。进一步通过结合蒸馏和使用修补矩阵伪逆约束模型输出，以加速度的方式一步完成修补过程。随后的后处理模块将修补后的伪投影重新投影到图像域并进一步细化重建，有效抑制伪影同时保留关键结构细节。
### Conclusion
定量实验结果表明，该方法在感知质量和保真度方面均达到最先进的性能，为LACT重建在科学研究和临床应用中提供了有前景的解决方案。
## 647. `cs.CV` - SplatCo：在大型未界定场景中保留细节的结构-视图协作高斯点积渲染 [PDF](https://arxiv.org/pdf/2505.17951), [HTML](https://arxiv.org/abs/2505.17951)
### Authors
Haihong Xiao,Jianan Zou,Yuxin Zhou,Ying He,Wenxiong Kang
### Background
本研究针对复杂户外环境高保真渲染的挑战，提出了一种新的框架SplatCo。该框架的目标是在大范围场景中同时维持精细几何结构和复杂纹理的保真度。
### Innovation
SplatCo引入了两个创新组件：1.一种跨结构协作模块，该模块通过融合全局三维面表示（捕捉粗略场景布局）与局部上下文网格特征（表示精细表面细节）进行融合。这种融合通过一种新型层次补偿策略实现，确保全局一致性的同时保留局部细节；2.一种跨视图辅助训练策略，通过跨视图同步梯度更新、基于可见性感知的密集化以及基于结构一致性修剪过度拟合或不准确的高斯函数，增强多视图一致性。
### Conclusion
实验结果表明，SplatCo在13个不同大型场景的综合评估中，均能实现比现有方法更高质量的重建，PSNR提高1-2dB，SSIM提高0.1-0.2，确立了大规模开放场景高保真渲染的新基准。该研究的代码和更多信息可在指定网址获取。
## 648. `cs.CV` - MMPerspective：MLLMs了解透视吗？一个综合基准用于透视感知、推理和鲁棒性 [PDF](https://arxiv.org/pdf/2505.20426), [HTML](https://arxiv.org/abs/2505.20426)
### Authors
Yolo Y. Tang,Pinxin Liu,Zhangyun Tan,Mingqian Feng,Rui Mao,Chao Huang,Jing Bi,Yunzhong Xiao,Susan Liang,Hang Hua,Ali Vosoughi,Luchuan Song,Zeliang Zhang,Chenliang Xu
### Background
透视理解在人类视觉感知中是基本的，然而大规模多模态语言模型（MLLMs）对接收的透视几何的理解程度仍然不清楚。为了深度理解MLLMs在透视理解中的表现，研究者们通过设计一个新基准MMPerspective，专门评估MLLMs在三个维度上的表现：透视感知、推理和鲁棒性，涵盖了10个精心构建的任务。
### Innovation
MMPerspective是一个专门的基准系统，包含了2711个实际和合成图像实例，其中包含5083个问题和答案对，旨在全面评估MLLMs的透视理解能力。通过系统评价43个最新的MLLMs模型，研究揭示了模型在处理复杂推理和保持空间一致性方面存在显著局限，同时发现模型架构、规模与透视能力之间的关系模式。
### Conclusion
MMPerspective为诊断和提升视觉-语言系统中的空间理解提供了有价值的测试平台。研究结果表明，虽然模型在表面层次的感知任务上表现出色，但在复杂的推理任务和鲁棒性上仍存在挑战。
## 649. `cs.CV` - 统一的图文到视频生成：一种灵活视觉条件的无训练方法 [PDF](https://arxiv.org/pdf/2505.20629), [HTML](https://arxiv.org/abs/2505.20629)
### Authors
Bolin Lai,Sangmin Lee,Xu Cao,Xiang Li,James M. Rehg
### Background
文本-图像到视频（TI2V）生成是使用语义和视觉条件进行可控视频生成的关键问题。现有的大多数方法通过微调将视觉条件添加到文本到视频（T2V）基础模型中，这在资源消耗上很昂贵，并且仅限于少数预定义的条件设置。
### Innovation
提出了一种称为FlexTI2V的新的无训练方法，该方法可以对T2V基础模型进行任意数量和位置的图像条件处理。该方法首先将条件图像反转为潜在空间中的噪声表示。在T2V模型的去噪过程中，通过局部图像块采用新颖的随机块交换策略，将视觉特征融入视频表示。为了平衡创性和保真度，使用动态控制机制调整对每个视频帧的视觉条件强度。
### Conclusion
大量的实验验证了我们的方法在无训练图像条件方法中显著超过了先前的方法。我们的方法还可以应用于基于UNet和变压器架构。
## 650. `cs.CV` - 当没有人注意的时候，动物是如何跳舞的 [PDF](https://arxiv.org/pdf/2505.23738), [HTML](https://arxiv.org/abs/2505.23738)
### Authors
Xiaojuan Wang,Aleksander Holynski,Brian Curless,Ira Kemelmacher,Steve Seitz
### Background
现有的动物舞蹈视频生成方法通常缺乏对舞步结构的高级控制信号，无法实现音乐同步和编舞意识的动物舞蹈视频生成。
### Innovation
提出了一种框架，通过引入编舞模式（结构化的动作节奏序列）作为高级控制信号，自动从人类舞蹈视频中估计这些模式，并结合图优化问题和视频扩散模型，能够从少量关键帧生成代表不同动物姿势的动物舞蹈视频，同时捕获舞蹈的镜像姿态。
### Conclusion
通过最少六个输入关键帧，该方法能够生成长达30秒的动物舞蹈视频，涵盖了多种动物和音乐轨道。
## 651. `cs.CV` - TK-Mamba: 将KAN与Mamba结合用于驱动的3D医学图像分割 [PDF](https://arxiv.org/pdf/2505.18525), [HTML](https://arxiv.org/abs/2505.18525)
### Authors
Haoyu Yang,Yutong Guan,Meixing Shi,Yuxiang Cai,Jintao Chen,Sun Bing,Wenhui Lei,Mianxin Liu,Xiaoming Shi,Yankai Jiang,Jianwei Yin
### Background
3D医学图像分割对于临床诊断和治疗至关重要，但它面临着高维数据和复杂空间依赖性的挑战。传统的单模态网络，如卷积神经网络（CNNs）和Transformer，往往在3D环境中受限于计算效率低下和上下文建模受限。
### Innovation
TK-Mamba是一个多模态框架，它将Mamba与Kolmogorov-Arnold网络（KAN）结合形成一个高效的混合骨干。提出的主要技术创新包括：引入了新颖的3D-Group-Rational KAN（3D-GR-KAN），这是首次将其应用于3D医学成像，提供了用于复杂体素结构的更高效和计算高效的非线性特征转换；设计了一种基于PubMedclip嵌入的双分支文本驱动策略，该策略通过同时捕捉器官间语义关系并调整图像特征与解剖文字，显著增强了分割的稳健性和准确性。
### Conclusion
通过结合这个先进的骨干网和视觉-语言知识，TK-Mamba提供了一个统一且可扩展的解决方案，适用于多器官和肿瘤分割任务。在多个数据集上的实验表明，我们的框架在器官和肿瘤分割任务中取得了最先进的性能，效率和准确性均超过了现有方法。我们的代码已公开可用。
## 652. `cs.CV` - 学习3DGS的分层稀疏变换编码 [PDF](https://arxiv.org/pdf/2505.22908), [HTML](https://arxiv.org/abs/2505.22908)
### Authors
Hao Xu,Xiaolin Wu,Xi Zhang
### Background
3D Gaussian Splatting (3DGS) 可以支持快速且高质量的新视角合成，但其占用大量的内存空间，因此压缩模型变得至关重要。当前最先进的3DGS压缩方法采用基于锚的架构，使用Scaffold-GS表示并结合条件熵编码，但这些方法并没有利用分析-综合变换机制，该机制是视觉数据压缩中的重要组成部分。因此，信号中的冗余仍然存在，这些冗余被留给熵编码器处理，这会增加熵编码模块的计算负担，提升编码延迟。
### Innovation
本文提出了一种Sparsity-guided Hierarchical Transform Coding (SHTC) 方法，这是首个端到端学习的神经变换编码方法，用于3DGS压缩。SHTC 方法首先利用KLT去除子锚内的相关性，然后进行量化和熵编码，最后使用低复杂度、场景自适应神经变换压缩KLT残差。通过稀疏先验和深度展开技术，所学习的变换只需要少量可训练参数，从而减少内存使用。SHTC 在压缩率-重建质量性能和解码速度上均超过了当前最先进的方法，其先验引导、参数高效的设计可能会启发低复杂度的神经图像和视频编解码器。
### Conclusion
SHTC 方法结合稀疏先验和深度学习，实现了3DGS压缩的端到端学习，显著提高了压缩效率和解码速度，为未来的神经图像和视频编码技术提供了新的参考方案。
## 653. `cs.CV` - A2Seek: 朝向基于推理的基准方法以理解空中异常 [PDF](https://arxiv.org/pdf/2505.21962), [HTML](https://arxiv.org/abs/2505.21962)
### Authors
Mengjingcheng Mo,Xinyang Tong,Mingpi Tan,Jiaxu Leng,Jiankang Zheng,Yiran Liu,Haosheng Chen,Ji Gan,Weisheng Li,Xinbo Gao
### Background
无人自主飞行器(UAV)为大范围、高空覆盖异常检测提供了可能，但它们也面临着动态视角、尺度变化和复杂场景等挑战。现有的数据集和方法主要针对固定地面视角设计，在无人机视角情况下表现不佳。为此，本文构建了一个名为A2Seek的大规模、以推理为核心的基准数据集，以改善无人机视角下的异常理解。该数据集覆盖了多种场景和环境条件，提供了高分辨率的真实世界航拍视频及其详细标注。
### Innovation
提出了一种基于推理框架A2Seek-R1，将R1样式策略推广到空中异常理解，增强了模型对“为何”和“何在”异常发生的理解和决策能力。该方法包括：1) 使用图示推理(GoT)指导监督微调来激活模型的潜在推理能力。2) 引入基于空中场景的规则奖励函数A-GRPO。3) 提出了一种新的“搜索”机制，模拟无人机飞行行为以引导模型关注信息丰富的区域。实验表明A2Seek-R1在预测准确度和异常定位方面分别取得了22.04%和13.9%的显著提升，展现了其在复杂环境和离群场景中的强大泛化能力。
### Conclusion
本文构建了A2Seek空域异常理解的推理基准，提出了一种基于推理框架A2Seek-R1，显著提高了无人机视角下的异常理解和定位能力，并展示了其在复杂环境下的泛化优势。
## 654. `cs.CV` - The Early Bird Identifies the Worm: You Can't Beat a Head Start in Long-Term Body Re-ID (ECHO-BID) [PDF](https://arxiv.org/pdf/2507.17640), [HTML](https://arxiv.org/abs/2507.17640)
### Authors
Thomas M. Metz,Matthew Q. Hill,Alice J. O'Toole
### Background
文中提到已有许多基于模型的方法用于长期人员再识别，但这些模型在高度不约束的环境中是否比广泛训练的大型基础模型直接应用领域迁移学习更准确尚不清楚。
### Innovation
研究应用了领域迁移学习对四个视觉基础模型（CLIP、DINOv2、AIMv2 和 EVA-02）进行长期人员再识别。经过领域适应的四个模型表现显著优于现有的最佳模型，组合四个模型的决策融合性能优于任一单一模型。研究提出了一种新的长期再识别模型ECHO-BID，基于对象预训练的EVA-02 Large模型。实验表明，模型大小和更小但更具挑战性的迁移学习协议是影响性能的关键因素。
### Conclusion
基础模型对于领域迁移学习提供了‘先行优势’，并且在少量领域数据的支持下，能够支持先进水平的性能。此外，长期人员再识别数据的局限性使得这一方法更有优势。
## 655. `cs.CV` - Orientation Matters: 使3D生成模型对齐方向 [PDF](https://arxiv.org/pdf/2506.08640), [HTML](https://arxiv.org/abs/2506.08640)
### Authors
Yichong Lu,Yuzhuo Tian,Zijin Jiang,Yikun Zhao,Yuanbo Yang,Hao Ouyang,Haoji Hu,Huimin Yu,Yujun Shen,Yiyi Liao
### Background
人类可以通过单张图片感知物体的形状和方向，这得益于对标准姿态的强先验知识。然而，现有的3D生成模型常常由于训练数据的不一致性产生对齐不良的结果，限制了它们在下游任务中的使用。
### Innovation
我们提出了方向对齐的3D物体生成任务，即从单张图片生成具有类别间一致方向的3D物体。为此，我们构建了包含14,832个方向对齐的3D模型的Objaverse-OA数据集，覆盖1,008个类别。利用该数据集，我们微调了两种基于多视图扩散和3D变分自编码器框架的代表性3D生成模型，以生成能够在各种类别中应用于未见过的物体的对齐物体。实验结果显示，我们的方法优于事后对齐方法。此外，我们展示了由我们的对齐物体生成支持的下游应用，比如通过合成分析进行零样本物体方向估计和基于箭头的物体旋转操作。
### Conclusion
我们的方法在对齐物体生成方面表现出优势，并且展示了其在下游任务中的应用潜力。
## 656. `cs.CV` - 使用表面法线和反射提示的多视角表面重建 [PDF](https://arxiv.org/pdf/2506.04115), [HTML](https://arxiv.org/abs/2506.04115)
### Authors
Robin Bruneau,Baptiste Brument,Yvain Quéau,Jean Mélou,François Bernard Lauze,Jean-Denis Durou,Lilian Calvet
### Background
在保留细节点的基础上实现高保真3D表面重建尤其具有挑战性，尤其是当存在复杂反射特性的材料且没有密集视角设置的情况下。现有的方法在处理这些情况时存在局限性。
### Innovation
该论文提出了一种利用辐射基础表面重建框架，结合多视角法线和（可选）反射图。该方法通过像素级的联合重新参数化反射率和表面法线，表示它们在模拟的不同照明条件下为辐射向量。这种方法能够无缝集成到传统的多视角立体（MVS）框架或现代神经体渲染（NVR）框架中。结合现代神经体渲染技术，该方法在多视角光度立体视图（MVPS）基准数据集DiLiGenT-MV、LUCES-MV和Skoltech3D上达到了最先进的性能。
### Conclusion
该方法特别擅长重建细粒度细节并处理具有挑战性的可见性条件。相比之前的会议论文，当前版本增强了算法速度和鲁棒性，并进行了更广泛的实证评估。相关的代码和数据可以在指定的链接处获得。
## 657. `cs.CV` - AlignCVC: 改进单图像到三维模型生成中的跨视角一致性对齐 [PDF](https://arxiv.org/pdf/2506.23150), [HTML](https://arxiv.org/abs/2506.23150)
### Authors
Xinyue Liang,Zhiyuan Ma,Lingchen Sun,Yanjun Guo,Lei Zhang
### Background
传统的单图像到三维模型生成方法通常遵循生成和重建的顺序工作流程。然而，由预训练生成模型合成的中间多视角图像往往缺乏跨视角一致性（CVC），严重影响三维重建性能。尽管一些最近的方法试图通过将重建结果反馈给多视角生成器来细化CVC，但这些方法在处理嘈杂且不稳定重建输出时会遇到困难，从而限制了CVC提升的有效性。
### Innovation
我们提出了AlignCVC，一种新颖的框架，从根本上通过分布对齐而不是依赖严格的回归损失来重新定义单图像到三维生成。我们的关键洞察是将生成和重建的多视角分布与真实多视角分布对齐，从而为提高CVC建立一个原则性的基础。我们提出了一种软硬对齐策略，对于生成模型和重建模型具有不同的目标，这种方法不仅提高了生成质量，还使推断速度大大提高至最多4步。我们的方法作为一种即插即用的范式，使各种多视角生成模型与三维重建模型无缝集成。
### Conclusion
大量的实验表明，AlignCVC在单图像到三维生成方面具有有效性和效率。
## 658. `cs.CV` - 基于双分支提示选择的零样本异常检测 [PDF](https://arxiv.org/pdf/2508.00777), [HTML](https://arxiv.org/abs/2508.00777)
### Authors
Zihan Wang,Samira Ebrahimi Kahou,Narges Armanfard
### Background
零样本异常检测（ZSAD）能够通过依赖可泛化的特征来识别和定位未见过类别的缺陷，而不需要任何异常标记样本。然而，现有的ZSAD方法在遇到领域转移时表现不佳，因为它们的训练数据来自有限的训练领域，并且无法将已学习到的知识应用到新分布的领域。
### Innovation
本文提出了一种名为PILOT的框架，通过两种创新来克服这些挑战：（1）一种新颖的双分支提示学习机制，该机制动态地将可学习的提示池与结构化的语义特征相结合，使模型能够针对每个输入图像自适应地加权最相关的异常线索；（2）一种无标签测试时的自适应策略，使用未标记测试数据中的高置信度伪标签来更新可学习提示的参数。
### Conclusion
在13个工业和医学基准上的广泛实验表明，PILOT在领域转移情况下的异常检测和定位中达到了最佳表现。
## 659. `cs.CV` - 超越完全监督的像素注释：基于草图的弱监督框架在图像篡改 localization 中的应用 [PDF](https://arxiv.org/pdf/2507.13018), [HTML](https://arxiv.org/abs/2507.13018)
### Authors
Songlin Li,Guofeng Yu,Zhiqing Guo,Yunfeng Diao,Dan Ma,Gaobo Yang
### Background
近年来，基于深度学习的图像篡改定位（Image Manipulation Localization, IML）技术取得了显著进展，但这些方法通常依赖于大规模的像素级标注数据集。为了克服高质量标注数据难以获取的挑战，一些方法利用图像级标签进行弱监督图像分割，但效果仍受到监督信号不足的影响。
### Innovation
本文通过探索一种提高标注效率和检测性能的弱监督形式——草图注释监督，提出了基于草图的IML（Sc-IML）数据集和框架。研究中引入了自监督训练和结构一致性损失，以及具备先验感知特征调制模块（PFMM）和带有门控机制的自适应融合模块（GAFM），并提出了基于置信度的熵最小化损失（${text{L}}_{{text{CEM}}}$）。这些方法能够显著提升模型在复杂场景中的特征鉴别能力和预测一致性，实验结果显示该方法在内分布和外分布性能上均优于现有的完全监督方法。
### Conclusion
本文提出的基于草图的弱监督IML框架在图像篡改定位任务中表现优异，无需大规模像素级标注数据即可显著提升检测性能。这一方法为图像篡改检测领域提供了新的解决方案。
## 660. `cs.CV` - 利用视觉语言模型进行时间序列异常检测 [PDF](https://arxiv.org/pdf/2506.06836), [HTML](https://arxiv.org/abs/2506.06836)
### Authors
Zelin He,Sarah Alnegheimish,Matthew Reimherr
### Background
时间序列异常检测(TSAD)在医疗、金融和传感器监控等多个领域发挥了重要作用。以往的方法主要侧重于在数值数据上训练领域特定模型，缺乏使人类专家具有识别上下文异常所需的时间视觉理解能力。为弥补这一不足，该研究探索了一种基于视觉语言模型(VLMs)的解决方案。尽管最近的研究表明VLMs在视觉理解任务中的能力，它们直接应用于时间序列领域在准确性和效率上仍表现不佳。
### Innovation
提出了一种两阶段解决方案：(1) ViT4TS，一种基于相对轻量级预训练视觉编码器的视觉筛选阶段，利用2D时间序列表示准确定位候选异常；(2) VLM4TS，一种基于VLM的时间序列阶段，结合全局时间上下文和VLM的视觉理解能力，在ViT4TS提供的候选中进行检测细化。该研究证明，在没有时间序列训练的情况下，VLM4TS在大多数情况下比时间序列预训练和从零开始的基线模型表现更好，F1-max得分比最佳基线提高了24.6%。此外，VLM4TS还一致优于现有的基于语言模型的TSAD方法，并且平均使用token少了36倍。
### Conclusion
VLM4TS不仅在F1-max得分上有显著提升，而且在token使用效率上也表现出了显著优势，证明了利用视觉语言模型进行时间序列异常检测的潜力。
## 661. `cs.CV` - HoliSafe: 全景安全基准与建模 [PDF](https://arxiv.org/pdf/2506.04704), [HTML](https://arxiv.org/abs/2506.04704)
### Authors
Youngwan Lee,Kangsan Kim,Kwanyong Park,Ilcahe Jung,Soojin Jang,Seanie Lee,Yong-Ju Lee,Sung Ju Hwang
### Background
尽管正在努力提高视觉语言模型（VLMs）的安全性，现有的方法仍然存在两个主要问题：1）现有的安全调优数据集和基准仅部分考虑了图像-文本交互可能产生的有害内容，常常忽略了看似无害的图像-文本对在特定上下文中可能带来的危险结果。这种狭隘的范围使VLMs在未见配置下容易受到 Jailbreak 攻击。2）先前的方法主要依赖于数据集中心的调优，缺乏通过架构创新内源性地增强安全性的方法。
### Innovation
本研究通过引入一个涵盖了所有五种安全/不安全图像-文本组合的全方面的安全数据集和基准——HoliSafe，填补了这一空白。HoliSafe集成了更全面的基础，包括HoliSafe-Bench，为训练和评估提供了更坚实的基础。此外，研究还提出了一个模块化的增强VLM安全性的框架，其中包括一个视觉防护模块（VGM），该模块能够评估输入图像对VLM的有害性，并赋予VLM双重功能：不仅学习生成更安全的响应，还能提供可解释的有害性分类，以证明其拒绝决策的合理性。VGM设计成插件组件形式，能够无缝集成到各种规模的预训练VLMs中。
### Conclusion
实验表明，使用HoliSafe训练的Safe-VLM与VGM结合，在多个VLM基准上实现了最先进的安全性性能。此外，HoliSafe-Bench还揭示了现有VLM模型中的关键漏洞。期望HoliSafe和VGM能够推动更稳健和可解释的VLM安全性的研究，扩展未来在多模态对齐方面的研究方向。
## 662. `cs.CV` - FedPromo：边缘端轻量级代理模型使基础模型适应新领域 [PDF](https://arxiv.org/pdf/2508.03356), [HTML](https://arxiv.org/abs/2508.03356)
### Authors
Matteo Caligiuri,Francesco Barbato,Donald Shenaj,Umberto Michieli,Pietro Zanuttigh
### Background
联邦学习（FL）是一种在去中心化数据上训练深度学习模型的成熟范式。然而，随着模型规模的扩大，传统的FL方法通常需要客户端设备上有大量的计算资源支持，这在很多情况下是不可行的。
### Innovation
我们提出了FedPromo这一新颖框架，该框架能够在中央服务器存储大规模基础模型的同时，利用联邦学习优化轻量级代理模型，从而大大减少了计算开销，同时又能保持隐私。该方法采用两阶段过程：首先，服务器端知识蒸馏使大规模基础模型（如变压器）的表示与紧凑型对应模型（如卷积神经网络）的表示对齐。然后，紧凑模型的编码器部署到客户端设备，在客户端设备上学习可训练分类器。之后，这些分类器可以被聚合，并无缝地转让回基础模型，从而实现个性化适应而无需直接访问用户数据。
### Conclusion
通过新颖的正则化策略，我们的框架能够实现分布式多域学习，平衡性能、隐私和资源效率。在五个图像分类基准上的广泛实验表明，FedPromo在资源有限的客户端情况下比现有方法表现更好。
## 663. `cs.CV` - Stand-In：视频生成中的轻量级即插即用身份控制 [PDF](https://arxiv.org/pdf/2508.07901), [HTML](https://arxiv.org/abs/2508.07901)
### Authors
Bowen Xue,Zheng-Peng Duan,Qixin Yan,Wenjing Wang,Hao Liu,Chun-Le Guo,Chongyi Li,Chen Li,Jing Lyu
### Background
在生成式AI领域，生成与用户指定身份匹配的高质量人类视频是一个重要但具有挑战性的任务。现有方法通常依赖大量的训练参数，并且不兼容其他AIGC工具。
### Innovation
本文提出了Stand-In，一个轻量级且即插即用的视频生成中身份保护框架。它通过在预训练的视频生成模型中引入有条件的图像分支，并利用受限自注意力和条件位置映射实现身份控制。
### Conclusion
通过这些设计，我们的方法在视频质量和身份保护方面优于完全参数训练的方法，仅增加了约1%的参数量和2000对训练数据。此外，该框架可无缝集成到其他任务中，如主题驱动视频生成、姿态参考视频生成、样式调整和人脸互换等。
## 664. `cs.CV` - WeatherDiffusion: 在内在空间中的可控天气编辑 [PDF](https://arxiv.org/pdf/2508.06982), [HTML](https://arxiv.org/abs/2508.06982)
### Authors
Yixin Zhu,Zuoliang Zhu,Jian Yang,Miloš Hašan,Jin Xie,Beibei Wang
### Background
传统基于像素空间的编辑方式在进行图像处理时缺乏对材质、场景几何和照明等内在信息的有效控制，这限制了图像编辑的精确度和可控性。现有的一些天气恢复方法和基于渲染的方法也存在不足， WeatherDiffusion在此背景下应运而生。
### Innovation
WeatherDiffusion 提出了一种基于扩散先验的框架，包括一个逆渲染器和一个前向渲染器。逆渲染器可以从输入图像中估计材质、场景几何和光照等内在信息，并利用这些信息和文本提示（描述具体的天气条件）生成最终图像，从而增强了可控性。此外，框架引入了内在地图感知的注意力机制，提高了在大规模户外场景下的空间对应性和分解质量。前向渲染则通过 CLIP 空间插值天气提示，实现了对天气的精细控制。
### Conclusion
实验结果表明，WeatherDiffusion 在无噪声像素空间编辑、天气恢复和基于渲染的方法中表现更优，显示出在下游任务如自动驾驶等场景中的应用潜力。
## 665. `cs.CV` - MAPo : Motion-Aware Partitioning of Deformable 3D Gaussian Splatting for High-Fidelity Dynamic Scene Reconstruction [PDF](https://arxiv.org/pdf/2508.19786), [HTML](https://arxiv.org/abs/2508.19786)
### Authors
Han Jiao,Jiakai Sun,Yexing Xu,Lei Zhao,Wei Xing,Huaizhong Lin
### Background
3D Gaussian Splatting 已被广泛应用于静态场景的高质量重建，并且能够实现快速渲染。现有的方法通过学习变形场来建模场景的时序变化，但这类方法由于单一统一模型的局限性，往往在动态变化较大的区域中会失真和模糊，损失掉精细的运动细节。
### Innovation
提出了 Motion-Aware Partitioning of Deformable 3D Gaussian Splatting (MAPo) 框架。该框架通过动态得分分区策略区分高动态和低动态的 3D 高斯点，对于高动态的 3D 高斯点，MAPo 采用递归时序分割并为每个新的时序段复制变形网络以便捕捉复杂的运动细节。同时，低动态的 3D 高斯点被当作静态来处理，从而降低成本。此外，还引入了跨帧一致性损失，以保证视觉连续性并提升渲染质量。
### Conclusion
实验结果表明，MAPo 在精细化和快速运动区域的渲染质量优于基线方法，同时保持了相近的计算成本。
## 666. `cs.CV` - 通过隐神经表示上采样获得的体素级内侧颞叶分割 [PDF](https://arxiv.org/pdf/2508.17171), [HTML](https://arxiv.org/abs/2508.17171)
### Authors
Yue Li,Pulkit Khandelwal,Rohit Jena,Long Xie,Michael Duong,Amanda E. Denning,Christopher A. Brown,Laura E. M. Wisse,Sandhitsu R. Das,David A. Wolk,Paul A. Yushkevich
### Background
磁共振成像（MRI）中的影像生物标志物对于阿尔茨海默病（AD）的诊断、跟踪和治疗至关重要。内侧颞叶（MTL）的神经纤维缠结tau病变与神经退行性疾病密切相关，并且其在脑内的扩散模式通常在疾病的早期阶段涉及MTL的某些亚区。为了提取详细的AD进展的生物标志物，需要精确分割MTL亚区。然而，MTL亚区通常在T2加权（T2w）MRI扫描中成像，而这由于MRI物理限制和图像获取的问题导致高度各向异性，使得可靠地对MTL亚区进行几何建模和提取形态学测量（如厚度）变得困难。
### Innovation
本研究使用隐神经表示方法将等向性T1加权（T1w）MRI和各向异性T2加权（T2w）MRI结合，通过上采样专家标注的MTL亚区的图集，建立一个多模态、高分辨率的等向性训练集，用于自动分割nnU-Net框架。与单模态、各向异性训练模型相比，使用等向性模型提取的形态学测量在区分轻度认知障碍（MCI）和认知功能正常的个体方面具有更强的影响效果，并且具有更高的测试重测稳定性。这项研究展示了在无需额外图谱注释工作的情况下，提高了MRI衍生的MTL亚区生物标志物的可靠性，有助于更准确地量化和跟踪AD病理与脑萎缩之间的关系，监测疾病进展。
### Conclusion
本研究证明了通过使用隐神经表示和上采样获得的体素级等向性训练数据集，可以提高MTL亚区分割的可靠性，而无需额外的图谱标注工作，这种方法有助于更准确地量化和跟踪阿尔茨海默病病理与脑萎缩之间的关系，监测疾病进展。
## 667. `cs.CV` - NeuroGaze-Distill：基于脑启发的蒸馏和抑郁启发的几何先验的稳健面部情绪识别 [PDF](https://arxiv.org/pdf/2509.11916), [HTML](https://arxiv.org/abs/2509.11916)
### Authors
Zilin Li,Weiwei Xu,Xuanqi Zhao,Yiran Zhu
### Background
面部情绪识别（FER）模型通常仅基于像素训练，这些模型在不同数据集中的泛化能力较弱，因为面部外观是对潜在情感的间接和有偏的代理。因此，需要一种有效的跨模态蒸馏框架，将基于脑的先验转移至仅依赖图像的FER模型，以提高其在不同数据集中的表现。
### Innovation
提出了一种跨模态蒸馏框架NeuroGaze-Distill，通过静态奖赏/唤醒（V/A）原型和抑郁启发的几何先验（D-Geo）将脑部信息转移至仅靠图像的FER学生模型。学生的训练使用常规交叉熵（CE）或知识蒸馏（KD），并结合两种轻量级正则化器：（i）通过余弦相似性对齐学生的特征与静态原型；（ii）D-Geo柔和地引导嵌入的几何结构，以符合抑郁症研究中通常报告的效应（例如，高奖赏区域的类似无愉悦收缩）。
### Conclusion
通过广泛和小规模数据集的评价结果表明，准静态V/A原型和D-Geo原则对于稳定性和性能提升至关重要。使用5x5网格优先于更密集的网格，且该方法简单易部署，无需复杂架构，从而提升FER模型的稳健性。
## 668. `cs.CV` - SafeFix: 通过受控图像生成进行靶向模型修复 [PDF](https://arxiv.org/pdf/2508.08701), [HTML](https://arxiv.org/abs/2508.08701)
### Authors
Ouyang Xu,Baoming Zhang,Ruiyu Mao,Yunhui Guo
### Background
深度学习视觉识别模型常常由于未充分代表某些语义子群体而表现出系统性的错误。现有的调试框架可以通过识别关键失败属性来确定这些失败，但有效修复模型仍然很困难。现有的解决方案通常依赖于手动设计的提示生成合成训练图像——这种方式容易导致分布偏移和语义错误。
### Innovation
为克服这些挑战，我们引入了一个模型修复模块，该模块基于可解释的失败归属管道。我们的方法使用条件文本到图像模型来生成针对失败案例的语义正确的图像。为了保持生成样本的质量和相关性，我们进一步利用一个大型视觉语言模型（LVLM）来过滤输出，以确保与原始数据分布的对齐并保持语义一致性。通过使用这种罕见案例增强的合成数据集重新训练视觉模型，可以显著减少与罕见案例相关的错误。实验表明，这种靶向修复策略可以在不引入新漏洞的情况下提高模型的稳健性。
### Conclusion
我们的方法通过受控图像生成进行靶向模型修复，显著减少了深度学习视觉识别模型中的罕见案例引起的错误，提高了模型的稳健性。这种方法为修复模型中的系统性错误提供了一种有效的新途径。
## 669. `cs.CV` - 时间步长Mixup在视像域向时间域高效传递感知知识中的应用 [PDF](https://arxiv.org/pdf/2509.12959), [HTML](https://arxiv.org/abs/2509.12959)
### Authors
Yuqi Xie,Shuhan Ye,Yi Yu,Chong Wang,Qixin Zhang,Jiazhen Xu,Le Shen,Yuanbin Qian,Jiangbo Qian,Guoqi Li
### Background
事件摄像头与脉冲神经网络的集成为能源高效的视觉处理带来了巨大的潜力，但是，事件数据的有限可用性和DVS输出的稀疏性为有效训练带来了挑战。虽然一些先前的工作尝试将语义知识从RGB数据集转移到DVS，但它们往往忽略了两种模态之间的显著分布差距。
### Innovation
本文提出了时间步混合知识转移（TMKT）方法，这是一种新颖的细粒度混合策略，通过在不同时间步长上对RGB和DVS输入进行插值，利用SNN的异步特性。此外，引入了感知模态感知的辅助学习目标，以支持时间步混合作业并增强模型在不同模态之间的有效区分能力。我们的方法实现了更平滑的知识转移，减轻了训练中的模态失配问题，并在脉冲图像分类任务中取得了优异性能。
### Conclusion
大量的实验结果证明了我们方法的有效性，并在多个数据集上展示了其优越性。我们的方法将在双盲评审过程结束后发布代码。
## 670. `cs.CV` - StrCGAN：恒星图像复原的生成框架 [PDF](https://arxiv.org/pdf/2509.19805), [HTML](https://arxiv.org/abs/2509.19805)
### Authors
Shantanusinh Parmar,Silas Janke
### Background
为了提升低分辨率的天文摄影图像质量，我们引入了一种生成模型StrCGAN，旨在重建高保真度的恒星天体图像。由于小型望远镜观测（如MobilTelesco数据集）的局限性，这一任务具有挑战性。传统的模型（如CycleGAN）虽然为图像到图像转化提供了基础，但往往会扭曲恒星形态，生成几乎无法辨认的图像。
### Innovation
为了克服这些限制，我们在CycleGAN框架中引入了一些关键创新：多谱融合以对齐光学和近红外（NIR）域，并引入了天体物理学正则化模块以保持恒星形态。来自跨越光学到NIR多任务全天巡天的真实参考信息引入训模型过程，确保重建在各个谱段上保持一致。
### Conclusion
StrCGAN能够生成视觉上更清晰的复原图像，在恒星图像增强任务上优于标准GAN模型。
## 671. `cs.CV` - 使用多个随机遮掩自动编码器的半监督多模态多任务学习的概化超图 [PDF](https://arxiv.org/pdf/2510.10068), [HTML](https://arxiv.org/abs/2510.10068)
### Authors
Pîrvu Mihai-Cristian,Marius Leordeanu
### Background
计算机视觉领域得益于多种模态的大量数据，从而提高了各种视觉任务的能力。近年来，自监督预训练方法，特别是掩码自动编码器（MAE），受到了广泛关注。这些方法通常作为优化下游任务，如分类或回归的第一步，无需任何手动标注的数据。经典的神经图工作和现代掩码自动编码器方法在理论上得到了统一，但如何有效地结合这两种方法以提高模型性能仍然是一个挑战。
### Innovation
本文引入了使用掩码自动编码器的概化超图模型（PHG-MAE），它通过整个模态的随机遮掩而不是仅仅是片段遮掩，促进了在前向传播中从超边分布进行采样。此外，该模型整合了预训练和微调步骤，形成了单一的训练循环，并通过聚合增强了推理时间的ensemble的预测性能和一致性。研究人员还展示了即使模型参数少于100万，也可以通过知识蒸馏提升ensemble的效果。该研究主要针对包含多个世界解释和模态的户外无人机场景，但其方法也可以应用于其他类似领域，如自主驾驶或室内机器人。
### Conclusion
通过开发数据管道软件来整合外部预训练专家，作者构建并发布了Dronescapes数据集的全自动化扩展版本。他们公开了所有技术细节、代码和重现步骤，致力于简化计算机视觉多模态多任务学习（MTL）场景的集成过程。
## 672. `cs.CV` - KEPT：使用视觉语言模型从连续驾驶画面预测知识增强轨迹 [PDF](https://arxiv.org/pdf/2509.02966), [HTML](https://arxiv.org/abs/2509.02966)
### Authors
Yujin Wang,Tianyi Wang,Quanfeng Liu,Wenxian Fan,Junfeng Jiao,Christian Claudel,Yunbing Yan,Bingzhao Gao,Jianqiang Wang,Hong Chen
### Background
短时轨迹准确预测对于自动驾驶的安全可靠至关重要，但现有视觉语言模型（VLMs）往往无法准确理解驾驶场景，生成可靠的轨迹。
### Innovation
提出了KEPT框架，这是一种通过视频编码器直接从连续前视驾驶帧预测自身轨迹的知识增强VLM框架。它结合了基于自监督学习和难样本挖掘训练的时频空融合视频编码器与检索增强生成（RAG）管道，利用k-means及HNSW检索技巧，添加了先验知识，并采用三层微调范式增强空间感知和轨迹预测能力。
### Conclusion
在nuScenes数据集上，KEPT在开环性能上优于基线方法。通过细调阶段、RAG中Top-K值、不同的检索策略、视觉编码器和VLM骨干网络的消融研究，证明了KEPT在自动驾驶中的可靠轨迹预测潜力。
## 673. `cs.CV` - 通过双路径引导利用未知来源的无标签数据进行深度假脸检测 [PDF](https://arxiv.org/pdf/2508.09022), [HTML](https://arxiv.org/abs/2508.09022)
### Authors
Zhiqiang Yang,Renshuai Tao,Chunjie Zhang,guodong yang,Xiaolong Zheng,Yao Zhao
### Background
现有的深度假脸检测方法依赖于静态标记的数据集。但随着生成模型的普及，真实世界中涌现了大量的无标签假脸数据，来源不明。这导致了现有依赖现有数据进行检测的技术面临泛化失败的问题，而手动标记这些新数据是不切实际的，因为假脸非常逼真。传统无监督学习方法在这种情况下效果不佳，因为真实和假脸的含义是相同的，使得传统策略的性能下降。
### Innovation
该论文提出了一种双路径引导网络(DPGNet)，以解决以下两个关键挑战：（1）弥补由不同生成模型生成的面部之间的领域差异；（2）利用无标签图像样本。这一方法包含两个核心模块：文本引导的跨域对齐，使用可学习的线索将视觉和文本嵌入统一到领域不变特征空间；以及基于课程的伪标签生成，动态利用无标签样本。
### Conclusion
在多个主流数据集上的广泛实验表明，DPGNet 显著优于现有技术，突显了其在利用无标签数据进行深度假脸检测方面的有效性。
## 674. `cs.CV` - IVY-FAKE: 一种统一的解释性框架和基准，用于图像和视频AIGC检测 [PDF](https://arxiv.org/pdf/2506.00979), [HTML](https://arxiv.org/abs/2506.00979)
### Authors
Changjiang Jiang,Wenhui Dong,Zhonghao Zhang,Chenyang Si,Fengchang Yu,Wei Peng,Xinbin Yuan,Yifei Bi,Ming Zhao,Zian Zhou,Caifeng Shan
### Background
随着人工生成内容(AIGC)技术的飞速发展，生成了高质量的合成内容，但也引发了重要的安全问题。当前的检测方法存在两个主要局限性：首先，缺乏多维度的可解释数据集，现有的开源数据集（如WildFake，GenVideo）依赖于简化的二元注释，限制了训练探测器的可解释性和可信度；其次，基于多模态语言模型（MLLM）的伪造检测器（如FakeVLM）在逐步骤推理中的可解释性不足，影响了可靠的定位和解释。
### Innovation
为了应对这些挑战，本文引入了Ivy-Fake，这是第一个大规模多模态可解释性AIGC检测基准。该基准包括超过106,000个丰富注释的训练样本（图像和视频）以及5,000个手工验证的评估示例，来自多个生成模型和真实世界的数据集，通过精心设计的处理管道确保多样性和质量。此外，本文还提出了一种基于组相对策略优化（GRPO）的强化学习模型Ivy-xDetector，能够生成可解释的推理链，并在多个合成内容检测基准测试中表现出稳健的性能。
### Conclusion
广泛的实验表明了我们数据集的优越性和新模式方法的有效性。我们的方法在GenImage上提高了性能至96.32%，大幅超越了前最先进的方法。
## 675. `cs.CV` - Cross-Layer Vision Smoothing: 通过关键物体的持续关注增强大型视觉-语言模型的视觉理解 [PDF](https://arxiv.org/pdf/2509.12897), [HTML](https://arxiv.org/abs/2509.12897)
### Authors
Jianfei Zhao,Feng Zhang,Xin Sun,Chong Feng,Zhixing Tan
### Background
大型视觉-语言模型（LVLMs）能够准确地在图像中定位关键对象，但它们对这些对象的关注时间非常短暂。研究发现，关键对象的持续关注可以提高LVLMs的视觉能力，因此本文提出了跨层视觉平滑（CLVS）方法。
### Innovation
CLVS的核心思想是引入视觉记忆，以平滑各层间的注意力分布。具体来说，这种视觉记忆在第一层初始化，并且在后续层中，模型的视觉注意力会结合来自前一层的视觉记忆，并且随着记忆的迭代更新，从而保持对关键对象的平滑关注。该方法利用视觉理解主要发生在模型早期和中期层这一特点，使用不确定性作为视觉理解完成的指标，并相应地终止平滑过程。实验结果表明，CLVS在多种视觉理解任务中取得了最先进的整体性能，并且在图像字幕基准测试中达到了与领先方法相当的结果。
### Conclusion
实验结果证实了该方法的有效性和普遍性，CLVS在各种视觉理解任务中的整体性能达到先进水平，并且在图像字幕基准测试中达到了与领先方法相当的结果。
## 676. `cs.CV` - InstaDA: 使用双智能体系统扩充实例分割数据 [PDF](https://arxiv.org/pdf/2509.02973), [HTML](https://arxiv.org/abs/2509.02973)
### Authors
Xianbao Hou,Yonghao He,Zeyd Boukhers,John See,Hu Su,Wei Sui,Cong Yang
### Background
获取高质量的实例分割数据具有挑战性，因为标注过程密集劳动且数据集中存在严重的类别不平衡。最近的研究使用Copy-Paste和扩散模型来创建更多样化的数据集。然而，这些研究通常没有深入合作LLMs和扩散模型，且未能充分利用现有训练数据中的丰富信息。
### Innovation
本文提出InstaDA，这是一种新颖的无需训练的双智能体系统，旨在扩充实例分割数据集。该系统包含一种文本智能体（T-Agent）和一种图像智能体（I-Agent），它们分别通过LLM和扩散模型的合作提高数据多样性，并根据生成的图像迭代精炼提示。I-Agent通过生成新的实例来丰富整体数据分布，基于训练图像条件。实验结果表明，InstaDA在LVIS 1.0验证集上的箱体平均精度（AP）和掩码AP分别提高了4.0和3.3，优于基线。此外，它还优于领先模型DiverGen，在箱体AP上有0.3的增益，在掩码AP上有0.1的增益，对常见的类别有0.7的增益，以及对频繁类别的掩码AP增益为0.5。
### Conclusion
InstaDA通过无监督的方式显著提高了实例分割数据集的质量，通过自动化和独立的流程提高了可操作性和效率。
## 677. `cs.CV` - LikePhys：通过似然偏好评估视频扩散模型中的直观物理理解 [PDF](https://arxiv.org/pdf/2510.11512), [HTML](https://arxiv.org/abs/2510.11512)
### Authors
Jianhao Yuan,Fabio Pizzati,Francesco Pinto,Lars Kunze,Ivan Laptev,Paul Newman,Philip Torr,Daniele De Martini
### Background
在构建通用的物理合理世界模拟器中，视频扩散模型中的直观物理理解至关重要。然而，准确评估这种能力仍然是一项挑战，因为在生成过程中难以将物理准确性与视觉外观区分开来。
### Innovation
本文提出了LikePhys，一种无需训练的方法，通过利用去噪目标作为基于ELBO的似然替代品，来区分有效和无效的视频，从而评估视频扩散模型中的直观物理理解。通过在涵盖四个物理领域的十二种场景基准上测试，表明评估指标Plausibility Preference Error (PPE)与人类偏好高度一致，优于最先进的评估基准。
### Conclusion
我们的研究系统地对当前视频扩散模型中的直观物理理解进行了基准测试，并进一步分析了模型设计和推断设置如何影响直观物理理解。实验结果表明，尽管模型在复杂和混沌的动力学方面存在问题，但随着模型容量和推断设置的扩大，物理理解呈现出改善的趋势。
## 678. `cs.CV` - 优化DINOv2的寄存器以进行面部防欺骗 [PDF](https://arxiv.org/pdf/2510.17201), [HTML](https://arxiv.org/abs/2510.17201)
### Authors
Mika Feng,Pierre Gallin-Martel,Koichi Ito,Takafumi Aoki
### Background
面部识别系统本应能够在各种头部姿态、光照条件和图像模糊的情况下正常运行。然而，恶意行为者可以通过向系统展示已被注册用户的照片来欺骗这些系统，从而绕过身份验证过程。这种欺骗攻击必须在进行面部识别之前被检测出来。
### Innovation
论文提出了基于DINOv2的欺骗攻击检测方法，旨在辨别真实和伪造面部图像之间的细微差异。具体来说，该方法通过使用带有寄存器的DINOv2提取可泛化的特征，并抑制注意机制中的扰动，使其能够聚焦于重要的细微特征。
### Conclusion
作者通过在提供给“ICCV2025面部防欺骗工作坊：统一物理-数字攻击检测”的数据集和SiW数据集上执行实验，证明了所提出的方法的有效性。该项目的页面可在此查看：this https URL。
## 679. `cs.CV` - 通过循环一致约束实现目标感知图像编辑 [PDF](https://arxiv.org/pdf/2510.20212), [HTML](https://arxiv.org/abs/2510.20212)
### Authors
Yanghao Wang,Zhen Wang,Long Chen
### Background
近期，预训练的文本到图像流程模型在文本基础的图像编辑方面取得了显著进展。主流方法通常采用破坏-然后-恢复的范式，即首先将源图像破坏为“中间状态”，然后在提示的指导下恢复为目标图像。然而，当前方法在构建这种中间状态时往往是目标无关的，即它们主要关注实现源图像重构，而忽略了与特定编辑目标之间的语义差距。这种设计导致，当所需修改显著偏离源图像时，会产生有限的编辑能力和不一致性。
### Innovation
本文提出了FlowCycle，一种新颖的无反演式和基于流程的编辑框架，通过可学习的噪声参数化破坏，并通过循环一致过程优化它们。通过交替地将源图像编辑为目标图像并恢复回源图像，同时采用双重一致性约束，FlowCycle 学习产生目标感知的中间状态，从而实现忠实的修改并保持源图像的一致性。
### Conclusion
广泛的消融实验表明，FlowCycle 在编辑质量和一致性方面超越了现有最先进的方法。
## 680. `cs.CV` - PaddleOCR-VL：通过0.9B 极紧凑型视觉-语言模型提升多语言文档解析 [PDF](https://arxiv.org/pdf/2510.14528), [HTML](https://arxiv.org/abs/2510.14528)
### Authors
Cheng Cui,Ting Sun,Suyin Liang,Tingquan Gao,Zelun Zhang,Jiaxuan Liu,Xueqing Wang,Changda Zhou,Hongen Liu,Manhui Lin,Yue Zhang,Yubo Zhang,Handong Zheng,Jing Zhang,Jun Zhang,Yi Liu,Dianhai Yu,Yanjun Ma
### Background
本文报告提出了一种专为文档解析设计的高效率模型PaddleOCR-VL，特别适用于多语言场景。PaddleOCR-VL的核心组件PaddleOCR-VL-0.9B是一个紧凑而强大的视觉-语言模型(Vision-Language Model, VLM)，集成了NaViT风格的动态分辨率视觉编码器和ERNIE-4.5-0.3B语言模型，能够准确地识别文档元素，支持109种语言。
### Innovation
PaddleOCR-VL引入了NaViT风格的动态分辨率视觉编码器和ERNIE-4.5-0.3B语言模型的结合，使得模型能够在保持低资源消耗的同时，准确识别复杂的文档元素（如文本、表格、公式和图表）。通过广泛使用的公共基准和内部基准的全面评估，PaddleOCR-VL在页面级文档解析和元素级识别方面均达到当前最佳性能，显著优于现有解决方案，表现出强大的竞争力，并提供快速的推理速度。
### Conclusion
这些优势使PaddleOCR-VL非常适合作为实际部署场景中的有效工具。目前代码可以在此链接中访问。
## 681. `cs.CV` - LayerComposer：基于图层画布的多人个性化生成 [PDF](https://arxiv.org/pdf/2510.20820), [HTML](https://arxiv.org/abs/2510.20820)
### Authors
Guocheng Gordon Qian,Ruihang Zhang,Tsai-Shien Chen,Yusuf Dalva,Anujraaj Argo Goyal,Willi Menapace,Ivan Skorokhodov,Meng Dong,Arpit Sahni,Daniil Ostashev,Ju Hu,Sergey Tulyakov,Kuan-Chieh Jackson Wang
### Background
现有的个性化图像生成器在视觉上表现出色，但缺乏对空间构图的互动控制，并且难以扩展到多人使用。
### Innovation
提出了一个互动且可扩展的框架LayerComposer，用于多人个性化生成。它通过图层化画布和透明的潜在剪枝机制，提供直观的人体参考注入，允许用户直接在图层化数字画布上放置和调整多个主体，指导个性化生成。
### Conclusion
实验表明，LayerComposer在多人个性化图像生成方面实现了优越的空间控制、一致性组合和身份保持，优于现有最先进的方法。
## 682. `cs.CV` - STT-GS: 样本先于传输的边缘高斯绘制方法结合客户端选择与功率控制 [PDF](https://arxiv.org/pdf/2510.13186), [HTML](https://arxiv.org/abs/2510.13186)
### Authors
Zhen Li,Xibin Jin,Guoliang Li,Shuai Wang,Miaowen Wen,Huseyin Arslan,Derrick Wing Kwan Ng,Chengzhong Xu
### Background
传统的边缘计算资源管理方法侧重于通信带宽或通用学习性能，而边缘高斯绘制（EGS）直接致力于最大化高斯绘制（GS）的质量。EGS将数据从分布式的客户端（例如无人机）收集，并在边缘（例如地面服务器）训练全局GS模型。这种技术特别适用于低空经济的场景重建，但在评估目标函数时，需要从客户端获取图像数据，这带来了一个因果冲突的问题。为了解决这个问题，本文提出了一个两阶段方法——先采样然后传输的EGS策略，也称为STT-GS（Sample-Then-Transmit Gaussian Splatting）。
### Innovation
本文提出了一个多步骤的方法：首先，从每个客户端采样一小批图像，作为试点数据，用于预测损失。基于初步评估，优先传输更有价值的客户端数据。为实现高效采样，提出了一个特征域聚类方案以选择最具有代表性的数据，并采用了紧传手段来减少试点数据的传输时间。最终，构建了一个联合客户端选择和功率控制框架来最大化GS导向函数，在通信资源受限的情况下达到了这一目标。针对问题的非凸性，提出了基于惩罚交替最大差分最小化算法的低复杂度高效解决方案。
### Conclusion
通过实验表明，所提出的方案在实际场景数据集上显著优于现有基准，可以通过较低的采样比率（例如10%）准确预测GS导向目标。本文方法在观测贡献和通信成本之间实现了良好的权衡。
## 683. `cs.CV` - Endoshare: 一种易于外科医生使用的可公开访问的解决方案，用于去标识化和管理手术视频 [PDF](https://arxiv.org/pdf/2510.20087), [HTML](https://arxiv.org/abs/2510.20087)
### Authors
Lorenzo Arboit,Dennis N. Schneider,Britty Baby,Vinkle Srivastav,Pietro Mascagni,Nicolas Padoy
### Background
基于视频的评估和外科手术数据科学能够促进外科手术培训、研究和质量改进，但其应用受限于视频录制格式的异质性和与视频共享相关的隐私问题。
### Innovation
Endoshare 是一种为外科医生设计的应用程序，能够合并、标准化和去标识化内窥镜视频。该应用采用了迭代的、以用户为中心的软件生命周期开发方法。在分析阶段遵循隐私设计原则，并通过临床医生和计算机科学家的可用性测验，改进了界面并增强了用户体验。Endoshare 处理时间与视频长度成正比，快模式处理速度更快，展示出高效和高质量的视频管理性能。
### Conclusion
Endoshare 是一个公开可用的解决方案，旨在管理和处理手术视频。该软件有望支持培训、研究和质量改进。为进一步建立其在手术视频管理中的可靠性，需要进行合规性和更大的互操作性验证。
## 684. `cs.CV` - FastGS：100秒内训练3D高斯点选方法 [PDF](https://arxiv.org/pdf/2511.04283), [HTML](https://arxiv.org/abs/2511.04283)
### Authors
Shiwei Ren,Tianci Wen,Yongchun Fang,Biao Lu
### Background
现有的三维高斯点选方法（3DGS）在训练过程中未能有效管理高斯数量，导致了冗余的计算时间开销。
### Innovation
提出了FastGS，一种全新的、简单的且通用的加速框架，基于多视图一致性全面考虑每个高斯的重要性，有效解决了训练时间和渲染质量之间的权衡。设计了基于多视图一致性的稀疏化和修剪策略，替代了预算机制。
### Conclusion
FastGS在不同类型的任务中展示了很强的通用性，在多项数据集上显示出显著优于现有最佳方法的训练加速效果，尤其是在Mip-NeRF 360和Deep Blending数据集上的表现突出。
## 685. `cs.CV` - 从预测到规划：基于策略的世界模型在协作状态-行动预测中的应用 [PDF](https://arxiv.org/pdf/2510.19654), [HTML](https://arxiv.org/abs/2510.19654)
### Authors
Zhida Zhao,Talas Fu,Yifan Wang,Lijun Wang,Huchuan Lu
### Background
尽管在构建世界模型方面取得了显著进展，但其在自主系统中的潜力仍未得到充分利用：世界模型主要用于世界模拟，并与轨迹规划相分离。虽然最近的研究尝试在一个统一框架中统一世界建模与规划，但世界建模对规划的协同促进机制仍有待进一步探索。
### Innovation
本文提出了一种新的驾驶 paradigmn，称为策略世界模型（PWM），它不仅在统一架构中结合了世界建模和轨迹规划，还通过提出的无操作的未来状态预测方案利用学习到的世界知识为规划提供帮助。为了提高视频预测的效率，还引入了一种动态增强的并行令牌生成机制，配备有上下文指导的Tokenizer和自适应动态聚焦损失。尽管仅使用前方摄像头输入，该方法在性能上与依赖多视图和多模态输入的方法相匹配或超越。
### Conclusion
通过协同状态-行动预测，PWM 可以模拟人类的前瞻性感知，从而提供更可靠的任务规划表现。此外，通过优化视频预测效率的机制，PWM 在性能上达到了或超越了现有的先进方法。
## 686. `cs.CV` - Ming-Flash-Omni：一种用于多模态感知和生成的稀疏统一架构 [PDF](https://arxiv.org/pdf/2510.24821), [HTML](https://arxiv.org/abs/2510.24821)
### Authors
Inclusion AI:Bowen Ma,Cheng Zou,Canxiang Yan,Chunxiang Jin,Chunjie Shen,Chenyu Lian,Dandan Zheng,Fudong Wang,Furong Xu,GuangMing Yao,Jun Zhou,Jingdong Chen,Jianing Li,Jianxin Sun,Jiajia Liu,Jian Sha,Jianjiang Zhu,Jianping Jiang,Jun Peng,Kaixiang Ji,Kaimeng Ren,Libin Wang,Lixiang Ru,Longhua Tan,Lu Ma,Lan Wang,Mochen Bai,Ning Gao,Qingpei Guo,Qinglong Zhang,Qiang Xu,Rui Liu,Ruijie Xiong,Ruobing Zheng,Sirui Gao,Tao Zhang,Tianqi Li,Tinghao Liu,Weilong Chai,Xinyu Xiao,Xiaomei Wang,Xiaolong Wang,Xiao Lu,Xiaoyu Li,Xingning Dong,Xuzheng Yu,Yi Yuan,Yuting Gao,Yuting Xiao,Yunxiao Sun,Yipeng Chen,Yifan Mao,Yifei Wu,Yongjie Lyu,Ziping Ma,Zhiqiang Fang,Zhihao Qiu,Ziyuan Huang,Zizheng Yang,Zhengyu He
### Background
论文提出了一种名为Ming-Flash-Omni的模型，它是基于Ling-Flash-2.0的Mixture-of-Experts（MoE）变种构建的，总参数数量为1000亿，每token仅有6.1亿个参数是活跃的。这种架构能够实现高效扩展，大幅提升计算效率和模型容量，从而推动统一的多模态智能在视觉、语音和语言方面的应用，朝着通用人工智能（AGI）迈进。
### Innovation
Ming-Flash-Omni相比其前身在多模态理解和生成方面表现出显著的提升。在语音识别方面，论文显著提高了系统的性能，特别是上下文ASR和方言意识ASR方面取得了优异成绩。在图生成方面，Ming-Flash-Omni展示了高保真度的文字渲染，并在场景一致性及图像编辑时保持身份识别方面有显著提升。此外，论文还引入了生成分割能力，不仅在分割任务上表现优异，也在图像生成中的空间控制和编辑一致性上有所改进。论文指出，Ming-Flash-Omni在文本到图像生成和生成分割方面达到最先进的成果，并在所有12个上下文ASR基准测试中设立了新的记录。
### Conclusion
Ming-Flash-Omni通过稀疏架构实现了高效扩展，提升了多模态智能的统一应用，尤其在多模态感知和生成方面取得了显著成就。该研究为朝着AGI迈进奠定了重要基础。
## 687. `cs.CV` - Metis-HOME: Hybrid Optimized Mixture-of-Experts for Multimodal Reasoning [PDF](https://arxiv.org/pdf/2510.20519), [HTML](https://arxiv.org/abs/2510.20519)
### Authors
Xiaohan Lan,Fanfan Liu,Haibo Qiu,Siqi Yang,Delian Ruan,Peng Shi,Lin Ma
### Background
近期自然语言处理（NLP）领域中大规模语言模型（LLM）的推理能力取得了显著进步，特别是在复杂的数学问题解决等任务上表现突出。尽管取得了这些进展，当前的多模态大模型在推理过程中也存在两个关键局限：一是倾向于使用计算密集型的推理方法，即使对于简单的查询也会占用大量计算资源，从而导致效率低下；二是过度专注于特定领域的推理往往会削弱它们泛化的理解能力。
### Innovation
本文提出了Metis-HOME：一个混合优化的专家混合架构，旨在解决上述的权衡问题。该模型通过将原始密集模型拆分为两个独立的专家分支来实现“混合思考”：一个适用于复杂的多步推理的思考分支，以及一个优化用于快速直接推理（如通用VQA和OCR任务）的非思考分支。一个轻量级、可训练的路由器动态地将查询分配给最适合的专家。
### Conclusion
深入的评估表明，该方法不仅显著提升了复杂的推理能力，还改善了模型的整体能力，逆转了其他专门优化推理的模型中识别能力下降的趋势。本工作为企业构建强大和多功能的MLLMs设定了新的范式，有效地解决了推理和泛化之间的主要矛盾。相关代码和权重可以在指定链接中获取。
## 688. `cs.CV` - DBGroup: 双支路点分组用于弱监督3D语义实例分割 [PDF](https://arxiv.org/pdf/2511.10003), [HTML](https://arxiv.org/abs/2511.10003)
### Authors
Xuexun Liu,Xiaoxu Xu,Qiudan Zhang,Lin Ma,Xu Wang
### Background
弱监督3D实例分割对于3D场景理解至关重要，尤其是在数据规模增加和全监督方法标注成本高昂的背景下。现有方法主要依赖于单击标注和边界框标注这两种形式的弱监督，但这些方法仍然存在标注劳动密集、复杂性高和依赖专家标注者等局限性。
### Innovation
本文提出了DBGroup，这是一种基于场景级标注的两阶段弱监督3D实例分割框架。在第一阶段，引入了双支路点分组模块，根据多视图图像中提取的语义和掩码线索生成伪标签。在第二阶段，通过多轮自训练对端到端的实例分割网络进行训练，使用精炼后的伪标签。此外，提出了实例掩码过滤策略以解决伪标签中的不一致性。
### Conclusion
通过广泛的实验表明，DBGroup在与稀疏点级监督3D实例分割方法的性能上具有竞争力，并超越了最先进的场景级监督3D语义分割方法。
## 689. `cs.CV` - Spatial-SSRL：通过自我监督强化学习提升空间理解 [PDF](https://arxiv.org/pdf/2510.27606), [HTML](https://arxiv.org/abs/2510.27606)
### Authors
Yuhong Liu,Beichen Zhang,Yuhang Zang,Yuhang Cao,Long Xing,Xiaoyi Dong,Haodong Duan,Dahua Lin,Jiaqi Wang
### Background
大型视觉-语言模型在空间理解方面存在局限性。现有的监督微调（SFT）和最近的可验证奖励强化学习（RLVR）依赖昂贵的监督、专业工具或受限环境，这限制了其规模。
### Innovation
引入了Spatial-SSRL，一种自我监督的RL范式，可以直接从普通RGB或RGB-D图像中提取可验证的信号。Spatial-SSRL自动生成五个预训练任务，捕捉2D和3D空间结构，提高空间推理能力，同时还保持了通用视觉能力。
### Conclusion
在七个空间理解基准测试中，无论是图像还是视频设置，Spatial-SSRL都比Qwen2.5-VL基线提高了平均4.63%（3B）和3.89%（7B）的准确性。结果表明，简单的、内在的监督可以实现大规模的RLVR，并为较大规模的LVLM提供更强的空间智能提供了一条实际途径。
## 690. `cs.CV` - FAPE-IR：适用于全场景图像恢复的频率感知规划与执行框架 [PDF](https://arxiv.org/pdf/2511.14099), [HTML](https://arxiv.org/abs/2511.14099)
### Authors
Jingren Liu,Shuning Xu,Qirui Yang,Yun Wang,Xiangyu Chen,Zhong Ji
### Background
现有的图像恢复方法通常依赖于特定的任务设计或潜在路由策略，难以适应各种退化条件下的现实场景。AIO-IR旨在开发一种统一模型以处理复杂条件下的多种退化，但现有方法的局限性导致了适应性的困难。
### Innovation
提出了FAPE-IR，一种基于频率感知规划与执行的框架。该框架利用一个冻结的多模态大型语言模型作为规划者，分析退化图像并生成频率感知的恢复计划。这些计划指导基于LoRA的Mixture-of-Experts模块，该模块在基于扩散的执行器内动态选择高频或低频专家，并由输入图像的频率特征补充。通过引入对抗训练和频率正则化损失，进一步提高了恢复质量并减少了伪影。通过结合语义规划与频率恢复，FAPE-IR提供了一种统一且可解释的全场景图像恢复解决方案。
### Conclusion
实验结果表明，FAPE-IR在七项恢复任务中达到了最先进的性能，并在混合退化条件下展示了强大的零样本泛化能力。
## 691. `cs.CV` - Click2Graph: 从单击生成交互式全景视频场景图 [PDF](https://arxiv.org/pdf/2511.15948), [HTML](https://arxiv.org/abs/2511.15948)
### Authors
Raphael Ruschel,Hardikkumar Prajapati,Awsafur Rahman,B.S. Manjunath
### Background
当前最先进的视频场景图生成（VSGG）系统提供了结构化的视觉理解，但它们是封闭的、前馈的管道，不能整合人类指导。相比之下，可提示分割模型如SAM2能够实现精确的人机交互，但缺乏语义或关系推理。本研究提出了Click2Graph，这是一种首次将视觉提示与空间、时间和语义理解统一的交互式框架，可以利用单个用户提示（如点击或边界框），自动分割并跟踪主题，发现交互对象，并预测三元组（主体，对象，谓词），形成时间一致的场景图。
### Innovation
Click2Graph引入了两个关键组件：动态交互发现模块，用于生成基于主体的物体提示，和语义分类头，用于联合实体和谓词推理。该框架将视觉提示与时空语义理解相结合，为用户引导的全景视频场景图提供了一个强大的基础。
### Conclusion
在OpenPVSG基准上的实验表明，Click2Graph展示了人类提示如何与全景定位和关系推理相结合，以实现可控、可解释的视频场景理解。
## 692. `cs.CV` - 从连续组织切片生成体积组织空间转录组的3D引导可扩展流匹配 [PDF](https://arxiv.org/pdf/2511.14613), [HTML](https://arxiv.org/abs/2511.14613)
### Authors
Mohammad Vali Sanian,Arshia Hemmat,Amirhossein Vahidi,Jonas Maaskola,Jimmy Tsz Hang Lee,Stanislaw Makarchuk,Yeliz Demirci,Nana-Jane Chipampe,Muzlifah Haniffa,Omer Bayraktar,Lassi Paavolainen,Mohammad Lotfollahi
### Background
目前大多数用于直接从组织学推断单细胞转录组的方法将每个切片视为独立实体，忽略了3D结构信息。而现有的能够处理3D信息的方法往往不具备生成能力，也难以扩展到大规模数据。该研究旨在通过提出一种3D感知的流匹配框架，实现从苏木素和伊红染色（H&E）中推断亚细胞基因表达的位置，从而构建一个全面的3D组织转录组图谱。
### Innovation
该研究提出了HoloTea框架，它包括一个共享特征空间中的跨切片斑点对齐模块和一个轻量级且可生成的控制网络，该控制网络可以通过解剖连续性进行条件调整。更重要的是，引入了一种3D一致的先验知识用于流匹配，结合了学习得到的零膨胀负二项式先验和基于邻近切片的空域确实先验。此外，研究还介绍了全局注意力模块，使流匹配在表达斑点数量增加的同时仍能保持效率。
### Conclusion
HoloTea在三个不同组织类型和分辨率的单细胞转录组数据集上表现出优于二维及原有三维方法的3D表达准确性及泛化能力。它有望推进准确的3D虚拟组织的创建进程，加速生物标志物的发现并加深对疾病的理解。
## 693. `cs.CV` - Video-R4: 通过视觉深思强化文本丰富的视频推理 [PDF](https://arxiv.org/pdf/2511.17490), [HTML](https://arxiv.org/abs/2511.17490)
### Authors
Yolo Y. Tang,Daiki Shimada,Hang Hua,Chao Huang,Jing Bi,Rogerio Feris,Chenliang Xu
### Background
理解和分析带有文本的视频需要读取短暂的文字提示，并且这些提示经常需要重复观察。然而，大多数视频问答模型依赖于在固定帧上进行一次性的感知，这导致了对细微证据的失误和幻觉。
### Innovation
提出了一种名为Video-R4的方法（强化视觉深思文本丰富的视频推理），它通过迭代选择帧、聚焦到信息区域、检索像素并更新其推理状态来执行视觉深思。并构建了两个具有可执行深思轨迹的数据集：一个用于监督练习，另一个用于强化学习。此外，该研究提出了一种多阶段的深思学习框架，逐步微调具有7B参数的语言模型，利用SFT和基于GRPO的RL学习原子和组合视觉操作。Video-R4-7B在M4-ViteVQA中的表现达到了最新水平，并具备多页文档问答、幻灯片问答和通用视频问答的能力。
### Conclusion
迭代深思是一种有效的方法，有助于像素级别的多模态推理。
## 694. `cs.CV` - CGCE: Classifier-Guided Concept Erasure in Generative Models [PDF](https://arxiv.org/pdf/2511.05865), [HTML](https://arxiv.org/abs/2511.05865)
### Authors
Viet Nguyen,Vishal M. Patel
### Background
近年来，大型生成模型的发展使得高质量图像和视频的生成成为可能，但也引发了关于生成不安全内容的安全性问题。现有方法可通过概念擦除来从预训练模型中移除不需要的概念，但这些方法仍然容易受到对抗性攻击的影响，这些攻击可以重新生成已被擦除的内容。此外，实现鲁棒擦除往往会导致模型对无关安全概念的生成质量下降，从而在安全性和性能之间产生了难以调和的权衡。
### Innovation
本文提出了一种名为Classifier-Guided Concept Erasure (CGCE)的高效插件框架，能够在不改变模型原始权重的情况下提供对各种生成模型的鲁棒概念擦除。CGCE通过使用轻量级分类器在文本嵌入上操作，首先检测并细化包含不希望概念的提示，通过这种方法可以实现多概念擦除。该方法在推理时仅修改不安全的嵌入，从而防止有害内容生成的同时保持模型在良性提示上的原始质量。
### Conclusion
广泛的实验表明，CGCE在广泛类型的红队攻击中达到了最先进的鲁棒性。我们的方法还保持了高生成用途，展示了在安全性和性能之间维持了更优越的平衡。我们展示了CGCE在各种现代文本到图像和文本到视频模型中的适用性，将其确立为适用于安全生成人工智能的实用且有效的解决方案。
## 695. `cs.CV` - X-ReID: Multi-granularity Information Interaction for Video-Based Visible-Infrared Person Re-Identification [PDF](https://arxiv.org/pdf/2511.17964), [HTML](https://arxiv.org/abs/2511.17964)
### Authors
Chenyang Yu,Xuehu Liu,Pingping Zhang,Huchuan Lu
### Background
大规模的视觉-语言模型（如CLIP）在检索任务中取得了显著的性能，但在基于视频的可见光-红外行人再识别（VVI-ReID）任务中，其潜力尚未充分开发。这主要面临两个挑战：缩小多模态差距和利用视频序列中的时空信息。
### Innovation
本文提出了一种新颖的跨模态特征学习框架X-ReID，该框架包括：1) 跨模态原型协作（CPC），用于对齐和集成来自不同模态的特征，引导网络减少模态差异；2) 多粒度信息交互（MII），它包括短期帧内交互、长期跨帧信息融合以及跨模态特征对齐，以增强对时序的建模并进一步缩小模态差异；3) 通过整合多粒度信息，最终实现稳健的序列级表示。
### Conclusion
在两个大规模的VVI-ReID基准数据集（即HITSZ-VCM和BUPTCampus）上进行的广泛实验表明，该方法优于现有最佳方法。
## 696. `cs.CV` - ManipShield: 一种统一的图像篡改检测、定位和解释框架 [PDF](https://arxiv.org/pdf/2511.14259), [HTML](https://arxiv.org/abs/2511.14259)
### Authors
Zitong Xu,Huiyu Duan,Xiaoyu Wang,Zhaolin Cai,Kaiwei Zhang,Qiang Hu,Jing Liu,Xiongkuo Min,Guangtao Zhai
### Background
随着生成模型的快速发展，现在可以实现多样且高真实度的图像编辑，这远远超越了传统的深伪技术，从而给图像篡改的检测带来了新的挑战。现有的图像篡改检测和定位（IMDL）基准数据集存在内容多样性有限、生成模型覆盖窄以及缺乏解释性等问题，这限制了当前攻击检测方法的推广和解释能力。
### Innovation
提出了一个名为ManipBench的大规模基准数据集，专注于AI编辑图像的篡改检测与定位。该数据集包含来自25个最先进的图像编辑模型超过450K张篡改图像，并且其中10万张图像搭载了边界框、判别线索和文本说明，以支持可解释的检测。在此基础上，提出了一个多模态大型语言模型（MLLM）为基础的统一模型ManipShield，利用对比LoRA微调和任务特定解码器实现统一的图像篡改检测、定位和解释。在ManipBench和多个公开数据集上的广泛实验表明，ManipShield表现出卓越的性能和较强的对未见过的篡改模型的泛化能力。
### Conclusion
ManipBench和ManipShield将在发表时公开。
## 697. `cs.CV` - 交替感知-推理以实现抗幻觉视频理解 [PDF](https://arxiv.org/pdf/2511.18463), [HTML](https://arxiv.org/abs/2511.18463)
### Authors
Bowei Pu,Chuanbin Liu,Yifan Ge,Peicheng Zhou,Yiwei Sun,Zhiying Lu,Jiankang Wang,Hongtao Xie
### Background
视频推理依赖于充分的视觉感知。然而，现有的视频推理语言模型（LLMs）容易依赖于有缺陷的一次性感知模式，即先描述视频再进行推理。这种模式增加了证据不足和幻觉的风险。
### Innovation
本文提出了一种新的框架，结合了基于循环的感知-推理模式（PLR）和反幻觉奖励机制，以解决证据不足和幻觉风险问题。具体包括：1. 引入感知循环推理（PLR）模式，使模型需逐段描述并分析视频，提供更精确的时间戳和决策；2. 采用知情评估者（FAE），评估每一步感知结果，作为反幻觉奖励，鼓励模型提供充足且精确的视频证据。
### Conclusion
本文提出的视频PLR在3B和7B参数规模上达到了最先进的表现，并且具有最好的数据效率。未来的工作可以通过更多的数据和模型优化来进一步提升其性能。
## 698. `cs.CV` - 何时思考，何时回顾：基于不确定性指导的回顾 [PDF](https://arxiv.org/pdf/2511.15613), [HTML](https://arxiv.org/abs/2511.15613)
### Authors
Jing Bi,Filippos Bellos,Junjia Guo,Yayuan Li,Chao Huang,Yolo Y. Tang,Luchuan Song,Susan Liang,Zhongfei Mark Zhang,Jason J. Corso,Chenliang Xu
### Background
在大语言模型和大型视觉语言模型中，测试时思考（即生成显式的中间推理链）已被证明可以提升性能，并在大型视觉语言模型中表现出显著的优势。尽管这些结果很有前景，但仍然缺乏如何思考对视觉推理实际影响的系统分析。
### Innovation
作者首次进行了大规模控制比较，评估了InternVL3.5和Qwen3-VL系列模型中的十种不同的思考变体，使用宽松的令牌预算和多轮解码方式在MMMU-val上进行评估。研究发现并非更多的思考总是更好的，长链往往是脱离图像的长错误轨迹，表现不如标准指令模式下的模型。进一步分析发现，某些短回溯短语，它们明确地引用图像，是成功轨迹中的重要组成部分，与更好的视觉定位相关。基于这些见解，作者提出了无需训练的解码策略——不确定性指导的回溯，该策略结合了不确定性信号、自适应回溯提示和广度搜索。该方法在整体上提升了MMMU性能，在标准思维比较弱的类别上取得了最大的收益，并超过了几个强大的编码策略，建立了在固定模型家族和令牌预算下的新标准。
### Conclusion
该解码策略还展示了泛化能力，通过对五个额外基准（包括两个广泛多模态套件和数学视觉推理数据集）的一致改进进行证明。
## 699. `cs.CV` - Human-Centric Open-Future Task Discovery: Formulation, Benchmark, and Scalable Tree-Based Search [PDF](https://arxiv.org/pdf/2511.18929), [HTML](https://arxiv.org/abs/2511.18929)
### Authors
Zijian Song,Xiaoxin Lin,Tao Pu,Zhenlong Yuan,Guangrun Wang,Liang Lin
### Background
近期，机器人和具身AI的发展受到了大规模多模态模型（LMMs）的推动。然而，如何进一步开发LMMs以发现直接辅助人类在开放未来场景中的任务仍然被严重忽视。在这种场景中，人类意图高度并发且动态变化，这是一个关键挑战。
### Innovation
本文提出了Human-centric Open-future Task Discovery (HOTD)问题，并提出了HOTD-Bench，包括超过2K个实际情况的视频、半自动化注解管道和用于开放集未来评估的基于模拟的协议。此外，本文还提出了Collaborative Multi-Agent Search Tree (CMAST)框架，该框架通过多代理系统分解复杂推理，并通过可扩展搜索树模块来结构化推理过程。实验表明，CMAST在HOTD-Bench上取得了最佳性能，并且能够与现有的LMMs很好地集成，连续提升性能。
### Conclusion
CMAST框架在解决HOTD问题上取得了显著的成功，不仅在HOTD-Bench上表现出最佳性能，而且还能够与现有的大规模多模态模型（LMMs）结合，提升整体性能。
## 700. `cs.CV` - ConceptGuard: 通过多模态风险检测实现文本和图像到视频生成过程中的主动安全 [PDF](https://arxiv.org/pdf/2511.18780), [HTML](https://arxiv.org/abs/2511.18780)
### Authors
Ruize Ma,Minghong Cai,Yilei Jiang,Jiaming Han,Yi Feng,Yingshui Tan,Xiaoyong Zhu,Bo Zhang,Bo Zheng,Xiangyu Yue
### Background
最近在视频生成模型方面的进展使从结合了文本和图像的多模态提示中创建高质量视频成为可能。尽管这些系统增强了可控性，但也引入了新的安全风险，因为有害内容可能来自单一模态或它们之间的交互。现有的安全方法通常是基于文本的，需要对风险类别有先验知识，或者作为生成后的审核器运行，难以前瞻地缓解这些组成性的多模态风险。
### Innovation
ConceptGuard，一个统一的安全防护框架，用于前瞻性地检测和减轻多模态视频生成中的不安全语义。ConceptGuard分为两个阶段：首先，对比检测模块通过将融合图像-文本输入投影到结构化的概念空间来识别潜在的安全风险；其次，语义抑制机制通过干预提示的多模态调节来引导生成过程远离不安全的概念。为了支持此框架的发展和严格评估，引入了两个新型基准：ConceptRisk，一个大规模的数据集用于多模态风险训练，和T2VSafetyBench-TI2V，第一个适应Text-and-Image-to-Video（TI2V）安全设置的基准。
### Conclusion
在两个基准上的全面实验结果表明，ConceptGuard始终优于现有的基线，实现了在风险检测和安全视频生成方面的最新成果。此代码可在https://github.com/ConceptGuard_project/conceptguard 获取。
## 701. `cs.CV` - ABM-LoRA：快速收敛低秩适应的激活边界匹配 [PDF](https://arxiv.org/pdf/2511.19145), [HTML](https://arxiv.org/abs/2511.19145)
### Authors
Dongha Lee,Jinhee Park,Minjun Kim,Junseok Kwon
### Background
尽管低秩适配器（LoRA）具有高参数效率，但其随机初始化导致梯度更新限于与预训练模型不匹配的切空间，从而造成显著信息损失并阻碍了早期收敛。
### Innovation
ABM-LoRA 提出了一个有原则的初始化策略，通过在下游训练前使适配器的激活边界与预训练模型的激活边界对齐，从而最大化完整参数梯度在适配器子空间的投影。这种对齐在初始化时锐减了信息损失，降低了起始损失，加快了收敛速度。
### Conclusion
ABM-LoRA 在多种架构和任务中展示了其有效性，特别是在 VTAB-1K 上达到了所有方法中最高的准确率，特别是在需要几何理解的结构化推理任务上表现优异。
## 702. `cs.CV` - Disc3D：通过区分性对象指代实现高质量3D对话数据的自动编目 [PDF](https://arxiv.org/pdf/2511.18817), [HTML](https://arxiv.org/abs/2511.18817)
### Authors
Siyuan Wei,Chunjie Wang,Xiao Liu,Xiaosheng Yan,Zhishan Zhou,Rui Huang
### Background
3D多模态大型语言模型（MLLMs）的性能仍然落后于2D模型，主要原因是高质量的3D场景对话数据集稀缺。以往的工作依赖昂贵的人工注释，并存在两个关键问题：视角模糊性，即空间语言假定未知的相机姿态；对象指代模糊性，即非排他性描述使得目标与干扰物难以区分。
### Innovation
本文提出了一种完全自动化的管道，将原始3D扫描数据转换为无歧义、高质量的对话数据，成本仅为之前的 fraction。该管道通过结合基于规则的约束、2D MLLMs 和 LLMs，实现了可控和可扩展的生成，无需人工干预。管道包括四个阶段：元注释收集，场景图构建，区分性对象指代以及多任务数据生成。
### Conclusion
实验结果表明，使用 Disc3D 训练在公开基准测试和我们多方面的 Disc3D-QA 任务中都表现出了显着且一致的改进。管道系统地解决了基础数据集中的固有缺陷，生成了包含超过200万个样本的25K混合3D场景的最终 Disc3D 数据集，涵盖场景、视角和对象描述、视觉定位以及五个对象中心的问题-答案任务。相关代码、数据和模型将公开提供。
## 703. `cs.CV` - 现代视觉模型能否理解对象与其相似物之间的区别？ [PDF](https://arxiv.org/pdf/2511.19200), [HTML](https://arxiv.org/abs/2511.19200)
### Authors
Itay Cohen,Ethan Fetaya,Amir Rosenfeld
### Background
计算机视觉领域的最新进展已经产生出在识别基准测试中表现出色的模型，但与人类感知相比，仍然存在显著差距。一种微妙的能力是判断一张照片是否看起来像某个对象，即使它不是该对象的实例。本研究探讨了像CLIP这样的视觉语言模型是否理解这一区别。
### Innovation
研究人员创建了一个名为RoLA的数据集，包含真实和似是而非的样本，并评估了基于提示的基本模型。还确定了一个方向以在CLIP的嵌入空间中移动表示，这有助于跨模态检索中的辨别，并增强了由CLIP前缀生成的描述。
### Conclusion
将此方向应用于图像和文本嵌入，提高了Conceptual12M中的跨模态检索的辨别能力，并提高了由CLIP前缀生成的描述的质量。
## 704. `cs.CV` - 全景视频中感兴趣区域检测的深度混合模型 [PDF](https://arxiv.org/pdf/2511.18856), [HTML](https://arxiv.org/abs/2511.18856)
### Authors
Sana Alamgeer,Mylene Farias,Marcelo Carvalho
### Background
360°视频流媒体中，感兴趣区域（ROI）起到了重要的作用。例如，ROI可以用于预测视口、智能切割视频进行直播等，以减少所需的带宽。提前检测视口有助于减少通过头戴设备观看视频时头部的移动。而智能视频切割可以提高视频传输效率，提升用户的观看体验。
### Innovation
设计了一种新的混合可吸引性模型来预测360°视频中的感兴趣区域。该模型融合了多种方法来提高预测的准确性和效率。
### Conclusion
通过使用所提出的混合可吸引性模型，并将其实验结果与360RAT数据集中的人工标注结果进行比较，证明了该方法的有效性。
## 705. `cs.CV` - SuperQuadricOcc: 基于多层高斯逼近的超菱形体实时自监督占位估计 [PDF](https://arxiv.org/pdf/2511.17361), [HTML](https://arxiv.org/abs/2511.17361)
### Authors
Seamie Hayes,Reenu Mohandas,Tim Brophy,Alexandre Boulch,Ganesh Sistu,Ciaran Eising
### Background
语义占用估计能够为自动驾驶提供全面的场景理解，提供对于感知和规划至关重要的密集的空间和语义信息。虽然高斯表示在自我监督的占用估计中被广泛应用，但由于大量高斯基础元的数量增加，其内存需求急剧增多，不适合实时推理。相比之下，超菱形体由于其多样的形状集合能够减少基础元的数量和降低内存需求。然而，将其集成到自我监督的占用模型中并不直观，因为缺乏超菱形体光栅化器以实现模型监督。
### Innovation
提出了一种名为SuperQuadricOcc的方法，使用基于超菱形体的场景表示。通过利用超菱形体的多层瑕球面分割高斯近似，我们在训练过程中实现了高斯光栅化监督。在Occ3D数据集上，SuperQuadricOcc实现了相对于基于高斯的方法75%的内存缩减、124%的推理速度提升以及5.9%的mIoU改进，且无需使用时间标签。这是首个能够实现实时推理并保持竞争力的占用模型。超菱形体在场景建模中基础元的数量减少了84%。
### Conclusion
我们提出的方法SuperQuadricOcc通过使用多层高斯逼近超菱形体，实现了占用估计中的内存减少、推理加速以及性能提升，突破了传统高斯模型的瓶颈，为自动驾驶中的实时有效场景理解提供了新的解决方案。
## 706. `cs.CV` - SatSAM2：使用可提示SAM2和卡尔曼先验的卫星图像中的带运动约束的视频对象跟踪 [PDF](https://arxiv.org/pdf/2511.18264), [HTML](https://arxiv.org/abs/2511.18264)
### Authors
Ruijie Fan,Junyan Ye,Huan Chen,Zilong Huang,Xiaolei Wang,Weijia Li
### Background
现有的卫星视频跟踪方法往往缺乏一般性，需要针对特定场景进行训练才能达到满意的效果，且容易在遮挡存在的情况下丢失跟踪目标。
### Innovation
本文提出了SatSAM2，这是一种基于SAM2的零样本卫星视频跟踪器，旨在将基础模型适应遥感领域。SatSAM2引入了两个核心模块：基于卡尔曼滤波的约束运动模块（KFCMM）来利用时间运动线索以抑制漂移，以及基于运动和可靠性的约束状态机（MCSM）来调节跟踪状态。
### Conclusion
SatSAM2在两个卫星跟踪基准和MVOT上的实验结果表明，其性能优于包括SAM2及其变种在内的传统跟踪器和基于基础模型的跟踪器，在OOBT数据集上，其AUC改善了5.84%，达到了最先进的方法。我们的代码和数据集将公开发布以促进进一步研究。
## 707. `cs.CV` - 多模态生成型人工智能：多模态大语言模型、扩散模型及统一 [PDF](https://arxiv.org/pdf/2409.14993), [HTML](https://arxiv.org/abs/2409.14993)
### Authors
Xin Wang,Yuwei Zhou,Bin Huang,Hong Chen,Wenwu Zhu
### Background
多模态生成型人工智能（AI）正引起学术界和产业界的越来越多关注。特别是，两种主要技术家族已经出现：一是多模态大型语言模型（LLMs）展示了出色的多模态理解能力；二是扩散模型在多模态生成方面表现出色。
### Innovation
该论文提供了一个关于多模态生成型人工智能的全面概述，包括多模态LLMs、扩散模型以及理解和生成的统一。文章详细回顾了多模态LLMs和扩散模型的概率建模过程、多模态架构设计和高级应用，并探讨了迈向理解和生成统一的努力。此外，文章还介绍了一些统一模型的战略，分析了它们的优势和劣势；总结了广泛用于多模态生成型人工智能预训练的常用数据集；并提出了几个具有挑战性的未来研究方向，这些方向可能有助于推动多模态生成型人工智能的发展。
### Conclusion
文章通过全面概述多模态生成型人工智能的发展现状，并探讨了统一理解和生成的努力，为这一领域的发展奠定了坚实的基础，指出了进一步研究的方向。
## 708. `cs.CV` - 比较生成学习方法在湍流代理中的应用 [PDF](https://arxiv.org/pdf/2411.16417), [HTML](https://arxiv.org/abs/2411.16417)
### Authors
Claudia Drygala,Edmund Ross,Francesca di Mare,Hanno Gottschalk
### Background
数值模拟湍流流动在流体力学中面临挑战，因为它们的复杂性和高计算成本。Direct Numerical Simulation (DNS) 和 Large Eddy Simulation (LES) 等高分辨率技术通常在计算上不可行，尤其是在技术相关的问题中更为明显。最近，生成概率模型在机器学习中的进步为湍流提供了一种有希望的替代方案。本研究探讨了三种生成模型（Variational Autoencoders (VAE)，Deep Convolutional Generative Adversarial Networks (DCGAN)，Denoising Diffusion Probabilistic Models (DDPM)）在模拟固定圆柱周围形成的 von Kármán 涡街的二维视图以及圆柱阵列尾流的真实实验数据集中的应用。
### Innovation
研究采用了三种不同的生成模型来模拟流体湍流，并通过 Large Eddy Simulation 和 Particle Image Velocimetry 数据集进行了训练。研究发现 DDPM 和 DCGAN 在重现湍流的所有分布方面表现出色，强调了这两者作为高效和准确的湍流替代工具的潜力。
### Conclusion
尽管 DCGAN 的训练更为复杂且可能遇到模式崩溃等问题，但它们的推理和训练时间最快，需要较少的数据，并提供最接近输入流的结果。相比之下，VAE 虽然训练和生成样本快速，但结果不够准确，而 DDPM 虽然有效但推理和训练时间明显较慢。
## 709. `cs.CV` - 从文本到视频模型是好的零样本图像编辑器吗？ [PDF](https://arxiv.org/pdf/2511.19435), [HTML](https://arxiv.org/abs/2511.19435)
### Authors
Zechuan Zhang,Zhenyuan Chen,Zongxin Yang,Yi Yang
### Background
大型视频扩散模型展示出强大的世界模拟和时间推理能力，但在作为零样本图像编辑器的应用方面仍有待探索。本文介绍了IF-Edit框架，该框架可以在无需调优的情况下重用于预训练的图像到视频扩散模型，以实现基于指令的图像编辑。IF-Edit解决了三个关键挑战：提示不匹配、冗余的时间潜变量和后期阶段帧的模糊。
### Innovation
提出了IF-Edit，一种无需调优的框架，它可以将预训练的图像到视频的扩散模型重新用于基于指令的图像编辑。该框架包含三个模块：链式思考提示增强模块，将静态编辑指令转换为时间上具有的合理化推理提示；时间潜变量dropout策略，压缩在专家切换点之后的帧潜变量，加速去噪同时保持语义和时间的一致性；自我一致的后精修步骤，使用短的静止视频轨迹来锐化后期阶段的帧。
### Conclusion
实验表明，IF-Edit在推理为中心的任务中表现出色，并且对于通用编辑任务仍然具有竞争力。本文提供了视频扩散模型作为图像编辑器的系统视角，并强调了一种用于统一视频和图像生成推理的简单配方。
## 710. `cs.CV` - HunyuanVideo 1.5 技术报告 [PDF](https://arxiv.org/pdf/2511.18870), [HTML](https://arxiv.org/abs/2511.18870)
### Authors
Bing Wu,Chang Zou,Changlin Li,Duojun Huang,Fang Yang,Hao Tan,Jack Peng,Jianbing Wu,Jiangfeng Xiong,Jie Jiang,Linus,Patrol,Peizhen Zhang,Peng Chen,Penghao Zhao,Qi Tian,Songtao Liu,Weijie Kong,Weiyan Wang,Xiao He,Xin Li,Xinchi Deng,Xuefei Zhe,Yang Li,Yanxin Long,Yuanbo Peng,Yue Wu,Yuhong Liu,Zhenyu Wang,Zuozhuo Dai,Bo Peng,Coopers Li,Gu Gong,Guojian Xiao,Jiahe Tian,Jiaxin Lin,Jie Liu,Jihong Zhang,Jiesong Lian,Kaihang Pan,Lei Wang,Lin Niu,Mingtao Chen,Mingyang Chen,Mingzhe Zheng,Miles Yang,Qiangqiang Hu,Qi Yang,Qiuyong Xiao,Runzhou Wu,Ryan Xu,Rui Yuan,Shanshan Sang,Shisheng Huang,Siruis Gong,Shuo Huang,Weiting Guo,Xiang Yuan,Xiaojia Chen,Xiawei Hu,Wenzhi Sun,Xiele Wu,Xianshun Ren,Xiaoyan Yuan,Xiaoyue Mi,Yepeng Zhang,Yifu Sun,Yiting Lu,Yitong Li,You Huang,Yu Tang,Yixuan Li,Yuhang Deng,Yuan Zhou,Zhichao Hu,Zhiguang Liu,Zhihe Yang,Zilin Yang,Zhenzhi Lu,Zixiang Zhou,Zhao Zhong
### Background
本文介绍了轻量级但功能强大的开源视频生成模型HunyuanVideo 1.5，该模型仅使用83亿个参数即可实现最先进的视觉质量和运动一致性，能够在消费级GPU上进行高效的推理。该模型通过精心的数据管理、先进的DiT架构的使用、增强的双语理解、逐步预训练和后训练、以及高效的视频超分辨率网络等关键组件实现这一目标。
### Innovation
在HunyuanVideo 1.5中，采用了 meticulous 数据管理，先进的 DiT 架构，特别是带有选择性和滑动瓷砖注意机制 (SSTA) 的高级设计，增强的双语理解通过字形感知文本编码，逐步预训练和后训练过程，以及高效的视频超分辨率网络。这些设计使该模型能够在多种时长和分辨率下生成高质量的文本到视频和图像到视频。
### Conclusion
通过广泛的实验，该紧凑且高效的模型在开源视频生成模型中建立了新的最先进的标准。通过公开提供代码和模型权重，我们为社区提供了高性能的基础，以降低视频创作和研究的门槛，使高级视频生成更广泛地可用。所有开源资产均可在this https URL上获取。
## 711. `cs.CV` - 通过几何变换和光度变换增强医学图像分析 [PDF](https://arxiv.org/pdf/2501.13643), [HTML](https://arxiv.org/abs/2501.13643)
### Authors
Khadija Rais,Mohamed Amroune,Mohamed Yassine Haouam,Abdelmadjid Benmachiche
### Background
医学图像分析因数据标注不足而受限，主要是由于患者隐私和缺乏专家等因素。尽管有些AI模型需要大量数据才能表现良好，数据扩充可以通过传统或先进技术来解决这一问题，从而提高模型性能和增加数据集的规模。
### Innovation
评估了几种数据扩充技术在两个不同医学图像数据集上的有效性。在皮肤癌数据集中应用了几何和光度变换技术，并训练了卷积神经网络，测试准确率显著提高至96.88%，损失减少至0.1468。在视网膜和血管数据集中使用了Mixup技术，Dice系数从扩充前的0提高到扩充后的0.4163。
### Conclusion
结果表明，使用数据扩充技术可以显著提高分类和分割性能，通过这种方法可以增加数据集的规模和多样性，从而提高模型在医学图像分析中的性能。
## 712. `cs.CV` - 通过计算美学检测新闻视频缩略图中的文化差异 [PDF](https://arxiv.org/pdf/2505.21912), [HTML](https://arxiv.org/abs/2505.21912)
### Authors
Marvin Limpijankit,John Kender
### Background
该研究提出了一个双步方法，用于检测不同文化背景来源的图像风格差异。首先，基于内容将图像聚类为更细致的视觉主题；然后将这些图像的美学特征进行比较。研究在2,400个来自中美两个YouTube频道、关于COVID-19和乌克兰冲突的视频缩略图上进行了测试。
### Innovation
该研究创新地将计算美学应用于新闻视频缩略图的文化差异检测，具体方法包括两步：首先基于内容聚类，然后比较美学特征；通过这种新方法发现了美国和中国视频缩略图在风格上的显著区别，这些区别大部分反映了文化偏好。
### Conclusion
研究结果表明中国缩略图在形式上更为随意且不正式，而美国频道更倾向于使用正式的图片作为缩略图。具体来说，美国缩略图颜色较淡、饱和度较高、较暗、细节更清晰、对称性较弱、图案更稀疏、构图更接近且更私密。研究认为这些差异大部分反映了文化偏好，并提出这种方法可以作为判断和比较疑似视觉宣传的基础标准。
## 713. `cs.CV` - FMPlug：通用基础流匹配先验的插件框架 [PDF](https://arxiv.org/pdf/2508.00721), [HTML](https://arxiv.org/abs/2508.00721)
### Authors
Yuxiang Wan,Ryan Devera,Wenjie Zhang,Ju Sun
### Background
本文介绍了一种增强基础流匹配（FM）先验的新型插件框架FMPlug，用于解决病态反问题。与依赖于领域特定或未训练先验的传统方法不同，FMPlug灵活运用了两个简洁而强大的见解：观察到的对象与期望对象之间的相似性和生成流的高斯性。本文通过引入时间自适应预热策略和尖锐高斯性正则化，揭示了通用基础模型的真正潜力。
### Innovation
FMPlug引入了时间自适应预热策略和尖锐高斯性正则化，从而提高了基础流匹配先验在图像超分辨率和去高斯模糊任务上的性能，显著超越了现有使用基础FM先验的方法。
### Conclusion
FMPlug在图像超分辨率和去高斯模糊任务上显著击败了现有的使用基础FM先验的方法，揭示了通用基础模型的潜力。
## 714. `cs.CV` - Hestia：基于体素和面部意识的分层最佳视点获取，用于高效三维重建 [PDF](https://arxiv.org/pdf/2508.01014), [HTML](https://arxiv.org/abs/2508.01014)
### Authors
Cheng-You Lu,Zhuoli Zhuang,Nguyen Thanh Trung Le,Da Xiao,Yu-Cheng Chang,Thomas Do,Srinath Sridhar,Chin-teng Lin
### Background
3D重建和新颖视图合成的进步使得高效的、逼真的渲染成为可能，但用于重建的图像仍然主要依赖手动选取或简单的预规划路径。尽管最近的研究提出了无需在线学习的一般可移植下一个最佳视点规划器，但这些方法在各方面形状上的鲁棒性和性能仍然有限。
### Innovation
Hestia通过四个组件解决了基于强化学习的通用方法在五自由度视角预测中的局限性：一个更多样化数据集以增强鲁棒性，一个分层结构以管理高维连续动作搜索空间，一种紧密贪婪策略以减轻虚假相关性，以及一种面部意识设计以避免忽视几何特性。实验结果表明，Hestia在覆盖比方面至少提高了4%，将Chamfer距离降低了50%，同时保持实时推理能力。此外，Hestia在5图像预算下覆盖比比先前方法提高了至少12%，并且在物体摆放变化下仍具有鲁棒性。
### Conclusion
Hestia作为一种最佳视点规划者，适用于现实世界的应用。我们展示了该方法的有效性和实用性。
## 715. `cs.CV` - Cloud4D：高空间和时间分辨率的云属性估计 [PDF](https://arxiv.org/pdf/2511.19431), [HTML](https://arxiv.org/abs/2511.19431)
### Authors
Jacob Lin,Edward Gryspeerdt,Ronald Clark
### Background
数值天气预测和气候模型在利用机器学习方面取得了显著进展，但大多数全球模型的规模约为公里级别，这使得模拟单个云和极端降水、风速突变、湍流和表面辐射强度变得困难。因此，转向更高分辨率的模型是必要的，但这也需要当前仪器难以获取的高分辨率现实观测数据。
### Innovation
Cloud4D 是第一个仅使用同步地面相机重建符合物理原则的四维云状态的学习框架。利用透视变换引导的二维到三维变换器，Cloud4D 推断出 25 米空间分辨率和 5 秒时间分辨率下的液态水分布。通过时间追踪 3D 液态水含量检索，Cloud4D 还估计了水平风向量。在六台天空朝向相机为期两个月的部署中，该系统在空间-时间分辨率上比最先进的卫星测量提高了数量级，并且保留了与并列的雷达测量相比低于 10% 的相对误差。
### Conclusion
Cloud4D 系统在高空间和时间分辨率下提供了云属性的估计，显著提高了云状态的精度，且仅依托地面相机进行观测。
## 716. `cs.CV` - CardioComposer: 利用可微几何实现解剖学扩散模型的组合控制 [PDF](https://arxiv.org/pdf/2509.08015), [HTML](https://arxiv.org/abs/2509.08015)
### Authors
Karim Kadry,Shoaib Goraya,Ajay Manicka,Abdalla Abdelwahed,Naravich Chutisilp,Farhad Nezami,Elazer Edelman
### Background
生成模型可以用于创建心血管解剖结构，这些结构对临床研究和医疗设备评估很有帮助。然而，在生成过程中存在几何可控性和真实性的权衡。为了改进这种权衡，作者提出了一种名为CardioComposer的新框架。
### Innovation
CardioComposer 使用可解释的椭球体原始体来生成基于多类解剖标签图。通过基于体素的几何矩开发了可微测量函数，这使得在扩散模型采样期间可以通过损失函数进行基于梯度的控制。这种方法能够独立地约束几何属性，并对多个亚结构提供组合控制。
### Conclusion
CardioComposer 方法适用于包含非凸亚结构的各种解剖系统，包括心脏、血管和骨骼器官，展示了其灵活性和广泛适用性。
## 717. `cs.CV` - 面向高通量成像的可扩展FPGA架构：基于DRAM优化的实时降噪管道，利用高级综合 [PDF](https://arxiv.org/pdf/2508.14917), [HTML](https://arxiv.org/abs/2508.14917)
### Authors
Weichien Liao
### Background
高通量成像工作流程，如Parallel Rapid Imaging with Spectroscopic Mapping (PRISM)，会产生超出常规实时处理能力的数据量。因此，需要高性能的预处理管道来实现实时去噪。
### Innovation
提出了一个基于FPGA的可扩展预处理管道，通过高级综合（HLS）实现，并优化了基于DRAM的缓冲区。该架构直接在下流图像数据上执行帧减法和平均，通过突发模式AXI4接口减少延迟，从而实现实时去噪，并减少了下游CPU/GPU分析的数据集大小。
### Conclusion
该模块化的FPGA架构在PRISM规模的数据采集下，提供了对延迟敏感的成像工作流程（如光谱学和显微镜）的实用解决方案，实现实时去噪并减少数据集大小，从而优化计算资源使用。
## 718. `cs.CV` - MeshSplat: 通过高斯点积实现的一般化稀疏视图表面重建 [PDF](https://arxiv.org/pdf/2508.17811), [HTML](https://arxiv.org/abs/2508.17811)
### Authors
Hanzhi Chang,Ruijie Zhu,Wenjie Chang,Mulin Yu,Yanzhe Liang,Jiahao Lu,Zhuoyuan Li,Tianzhu Zhang
### Background
计算机视觉和图形学领域已经广泛研究了表面重建，但现有方法在输入视图极稀疏的情况下难以恢复准确的场景几何结构。
### Innovation
提出了MeshSplat框架，该框架利用高斯点积（2DGS）作为桥梁，连接新型视图合成和学习到的几何先验，并将这些先验转移以实现表面重建。该方法包括一个前馈网络，用于预测每个视图像素对齐的2DGS，从而消除对直接3D地面真实监督的需求。为了提高2DGS位置和方向预测的准确性，提出了加权海弗距离损失来正则化深度图，特别是在输入视图的重叠区域，还提出了一种法线预测网络来使2DGS的方向与单目法线估计器预测的法线矢量对齐。
### Conclusion
大量实验验证了我们提出改进的有效性，展示了我们的方法在一般化稀疏视图网格重建任务中的最先进的性能。
## 719. `cs.CV` - 适应视觉语言模型以评估世界模型 [PDF](https://arxiv.org/pdf/2506.17967), [HTML](https://arxiv.org/abs/2506.17967)
### Authors
Mariya Hendriksen,Tabish Rashid,David Bignell,Raluca Georgescu,Abdelhak Lemkhenter,Katja Hofmann,Sam Devlin,Sarah Parisot
### Background
世界模型是一种基于过去观察和行动模拟环境动态的生成模型，正逐渐成为规划、仿真和具身人工智能中的热点。然而，对这些模型的评估依然是一个基本的挑战，现有的评估方式无法精细、时间限定地评估行为对齐和语义一致性等能力。视觉语言模型（VLMs）由于强大的跨模态推理能力，显示出自动评估生成内容的潜力。但它们在这些精细的、时间敏感的评估任务中的应用仍然有限，需要进行针对性的调整。
### Innovation
该研究引入了一种新的评估协议，针对两种识别任务——动作识别和角色识别，每个任务分别采用二元选择、多项选择和开放性选择格式进行评估。为了支持这一协议，研究者提出了UNIVERSE（统一视觉语言评价器）——一种适应数据和计算约束的基于VLM的视频世界模型评估器。研究者对全适应法、部分适应法和参数优化适应法分别在不同任务格式、上下文长度、采样方法和数据组成的条件下进行了广泛的实验，总实验天数超过5,154个GPU天。结果表明，统一的评估器能够与特定任务的检验点达到相同的性能。跨七个不同环境的人类研究也证实了其与人的判断高度一致。
### Conclusion
UNIVERSE作为一种轻量级、可适应且语义感知的视频世界模型评估器，已经确立了其在视觉语言模型评估任务中的作用。
## 720. `cs.CV` - 基于迭代网络的高分辨率UDF网格生成 [PDF](https://arxiv.org/pdf/2509.17212), [HTML](https://arxiv.org/abs/2509.17212)
### Authors
Federico Stella,Nicolas Talabot,Hieu Le,Pascal Fua
### Background
无符号距离场（UDFs）是开放曲面的自然隐式表示，但与有符号距离场（SDFs）不同，它们难以转换为显式网格，尤其是在高分辨率下噪声更高，难以捕捉到细节。现有的大多数技术在同一体素内未涉及邻居信息，导致表面缺失和因UDF模糊或噪声引起的孔洞。
### Innovation
本文通过多次迭代并利用之前提取的表面元素的邻域信息，提出了一种迭代神经网络方法，该方法能够在多个迭代中传播空间信息，逐渐提高每个体素中的表面恢复。这种方法整合了新检测到的表面、距离值和梯度，有效地纠正错误并在复杂区域稳定提取。
### Conclusion
实验表明，与现有方法相比，本文的方法在复杂几何结构上生成的网格更为准确和完整，特别在传统方法失败的高分辨率下，UDF表面提取表现更好。
## 721. `cs.CV` - 基于LoRA的方法在Subarachnoid Hematoma分割中的Unet迁移学习 [PDF](https://arxiv.org/pdf/2508.01772), [HTML](https://arxiv.org/abs/2508.01772)
### Authors
Cristian Minoccheri,Matthew Hodgman,Haoyuan Ma,Rameez Merchant,Emily Wittrup,Craig Williamson,Kayvan Najarian
### Background
蛛网膜下腔出血(SAH)是一种生命威胁性的神经系统急症，其死亡率超过30%。从相关血肿类型进行迁移学习代表了一种潜在有价值的但尚未充分开发的方法。尽管U-net架构因其在有限数据集上的有效性而仍然是医学图像分割的标准，但在医学成像领域，参数有效率的迁移学习（LoRA）方法很少应用于卷积神经网络。
### Innovation
我们实施了一个预先在多机构124例创伤性脑损伤患者的计算机断层扫描数据上训练的U-net架构，并在University of Michigan Health System的30例动脉瘤性SAH患者的3折交叉验证数据上进行了微调。我们提出了一种基于张量CP分解的新CP-LoRA方法，并引入了DoRA变种（DoRA-C、convDoRA、CP-DoRA），将权重矩阵分解为幅度和方向分量。相较于现有的LoRA方法（LoRA-C、convLoRA）和标准微调策略，在多视角U-net模型的不同模块上进行了比较。基于LoRA的方法一致优于标准的U-net微调。不同出血量的表现各异，所有方法在较大血肿体积上显示出更高的准确性。CP-LoRA实现了与现有方法相当的性能，同时使用了显著更少的参数。高阶数的过参数化一致性优于严格低秩适应。
### Conclusion
这项研究表明，血肿类型之间的迁移学习是可行的，基于LoRA的方法在动脉瘤性SAH分割中显著优于传统的U-net微调方法。
## 722. `cs.CV` - FlagEval Findings Report: 对自动验证的文本和视觉问题上大型推理解题模型的一个初步评估 [PDF](https://arxiv.org/pdf/2509.17177), [HTML](https://arxiv.org/abs/2509.17177)
### Authors
Bowen Qin,Chen Yue,Fang Yin,Hui Wang,JG Yao,Jiakang Liu,Jing-Shu Zheng,Miguel Hu Chen,Richeng Xuan,Shibei Meng,Shiqi Zhou,Teng Dai,Tong-Shuai Ren,Wei Cui,Xi Yang,Xialin Du,Xiaojing Xu,Xue Sun,Xuejing Li,Yaming Liu,Yesheng Liu,Ying Liu,Yonghua Lin,Yu Zhao,Yunduo Zhang,Yuwen Luo,Zheqi He,Zhiyuan He,Zhongyuan Wang
### Background
本文探讨了目前大型推理解题模型（LRMs）在自动验证的文本和视觉问题中的表现。研究者们进行了一次中等规模、一定程度上无污染的评估，旨在提供一些初步的发现。此外，还发布了用于视觉语言模型的评估基准——ROME，该基准专门用于测试模型从视觉线索中推断的能力。
### Innovation
研究引入了Rome——一个用于视觉语言模型的评估基准，特别设计来测试从视觉线索中进行推理的能力。同时，文章提供了一种新的方法来评估大型推理解题模型在处理自动验证问题上的表现，这之前可能较少被探讨。
### Conclusion
研究发现在处理某些类型的自动验证问题时，现存的大型推理解题模型表现有限，并指出需要进一步的研究来增强这些模型在视觉推理任务的效果。最后，研究团队共享了基准测试、评估数据和其他更新信息以供外界参考和参考更新。
## 723. `cs.CV` - Optimally Deep Networks -- 根据数据集调整模型深度以实现卓越效率 [PDF](https://arxiv.org/pdf/2510.10764), [HTML](https://arxiv.org/abs/2510.10764)
### Authors
Shaharyar Ahmed Khan Tareen,Filza Khan Tareen
### Background
深度神经网络（DNNs）在各种任务中提供了出色的性能，但这种成功往往是以不必要的大模型尺寸、高的计算需求和大量的内存占用为代价。通常，强大的架构在全深度下进行训练，但这并不意味着所有数据集或任务都需要如此高的模型容量。在资源较低的复杂度数据集上训练大型且深度的架构通常会导致计算浪费、不必要的能量消耗和过多的内存使用，从而使得在资源有限的设备上部署模型变得不切实际。
### Innovation
本文提出了优化深度网络（ODNs）的概念，以在模型深度和任务复杂度之间实现平衡。具体来说，我们提出了一个类似神经架构搜索（NAS）的训练策略，称为渐进深度扩展，该策略从相对较浅的深度开始训练神经网络，并随着早期块的收敛逐步增加深度，直到达到目标精度为止。ODNs仅使用任务所需的最优化深度，从而去除冗余层。这降低了未来训练和推理的成本，减少了模型的内存占用，提高了计算效率，并促进了在边缘设备上的部署。
### Conclusion
实证结果表明，对于MNIST和SVHN的ResNet-18和ResNet-34，最优深度分别实现了98.64％和96.44％的内存占用减少，同时保持了具有竞争力的准确性99.31％和96.08％。
## 724. `cs.CV` - GigaBrain-0: 一种由世界模型赋能的视觉-语言-动作模型 [PDF](https://arxiv.org/pdf/2510.19430), [HTML](https://arxiv.org/abs/2510.19430)
### Authors
GigaBrain Team:Angen Ye,Boyuan Wang,Chaojun Ni,Guan Huang,Guosheng Zhao,Haoyun Li,Jie Li,Jiagang Zhu,Lv Feng,Peng Li,Qiuping Deng,Runqi Ouyang,Wenkang Qin,Xinze Chen,Xiaofeng Wang,Yang Wang,Yifan Li,Yilong Li,Yiran Ding,Yuan Xu,Yun Ye,Yukun Zhou,Zhehao Dong,Zhenan Wang,Zhichao Liu,Zheng Zhu
### Background
训练视觉语言动作（VLA）模型的通用机器人通常需要大量真实世界的机器人数据，这非常昂贵且耗时。物理数据收集的低效性严重限制了当前VLA系统的可扩展性和泛化能力。
### Innovation
引入了一个名为GigaBrain-0的新颖VLA基础模型，它利用世界模型生成的数据（例如视频生成、实2实转换、人体转移、视点转移、模拟2现实转换数据）。这种方法通过充分利用世界模型生成大规模多样数据来显著减少对真实机器人数据的依赖，同时提高了跨任务泛化能力。此外，通过RGBD输入建模和具身思维链（CoT）监督，进一步增强了策略鲁棒性，使模型在执行任务时能够推理空间几何、物体状态和长时依赖关系。
### Conclusion
广泛的实验表明，GigaBrain-0在变化的外观（例如，纹理、颜色）、物体摆放和相机视角方面实现了卓越的泛化能力。此外，我们还展示了GigaBrain-0-Small模型，这是一个轻量级优化版本，设计用于在NVIDIA Jetson AGX Orin等设备上高效运行。
## 725. `cs.CV` - MHR: 动量人体模型架 [PDF](https://arxiv.org/pdf/2511.15586), [HTML](https://arxiv.org/abs/2511.15586)
### Authors
Aaron Ferguson,Ahmed A. A. Osman,Berta Bescos,Carsten Stoll,Chris Twigg,Christoph Lassner,David Otte,Eric Vignola,Fabian Prada,Federica Bogo,Igor Santesteban,Javier Romero,Jenna Zarate,Jeongseok Lee,Jinhyung Park,Jinlong Yang,John Doublestein,Kishore Venkateshan,Kris Kitani,Ladislav Kavan,Marco Dal Farra,Matthew Hu,Matthew Cioffi,Michael Fabris,Michael Ranieri,Mohammad Modarres,Petr Kadlecek,Rawal Khirodkar,Rinat Abdrashitov,Romain Prévost,Roman Rajbhandari,Ronald Mallet,Russell Pearsall,Sandy Kao,Sanjeev Kumar,Scott Parrish,Shoou-I Yu,Shunsuke Saito,Takaaki Shiratori,Te-Li Wang,Tony Tung,Yichen Xu,Yuan Dong,Yuhua Chen,Yuanlu Xu,Yuting Ye,Zhongshi Jiang
### Background
本文介绍了一种新的参数人体模型MHR，该模型结合了ATLAS的分离骨架/形态范式和Momentum库启发的灵活现代架和姿态纠正系统。该模型支持非线性姿态纠正，能够实现富有表现力且解剖学上合理的身体动画，旨在为AR/VR和图形管道提供稳健的集成。
### Innovation
MHR模型通过将ATLAS的分离骨架/形态范式与Momentum库的启发式灵活现代架和姿态纠正系统相结合，实现了非线性姿态纠正和解剖学上合理的高效动态模拟，提高了人体动画的制作效率和质量。
### Conclusion
MHR模型适用于AR/VR和图形管道，该模型能够实现高效的、解剖学上合理的身体动态模拟，支持非线性姿态纠正，为未来的人体动画和虚拟现实应用提供了新的可能性。
## 726. `cs.CV` - OmniLens++：通过大型镜头库预训练和潜在点扩展函数表示实现盲镜头缺陷校正 [PDF](https://arxiv.org/pdf/2511.17126), [HTML](https://arxiv.org/abs/2511.17126)
### Authors
Qi Jiang,Xiaolong Qian,Yao Gao,Lei Sun,Kailun Yang,Zhonghua Yi,Wenyong Li,Ming-Hsuan Yang,Luc Van Gool,Kaiwei Wang
### Background
现有镜头缺陷校正管道在处理未知光学退化时存在限制，尤其是在数据扩展性和缺乏先验指导方面。OmniLens++框架旨在解决这两个问题，以提高模型的泛化能力。
### Innovation
OmniLens++引入了扩大设计规范以增加镜头数据的退化多样性，并通过量化光学退化的空间变异模式和严重程度来抽样更均匀的分布。为了利用点扩展函数（PSF）作为先验指导，提出了一种潜在PSF表示（LPR）并结合使用VQVAE框架来学习镜头库PSF的潜在特征。
### Conclusion
实验表明，OmniLens++在盲镜头缺陷校正方面表现出卓越的泛化能力，能够处理各种实际和合成镜头的多种缺陷。此外，AODLibpro为多种缺陷的更有效训练提供了一个可扩展的基础，而LPR则进一步提升了大规模镜头库的潜能。源代码和数据集将在此网址（……）公开。
## 727. `cs.CV` - Yanyun-3: 使用视觉语言模型实现跨平台策略游戏自动化 [PDF](https://arxiv.org/pdf/2511.12937), [HTML](https://arxiv.org/abs/2511.12937)
### Authors
Guoyan Wang,Yanyan Huang,Chunlin Chen,Lifeng Wang,Yuxiang Sun
### Background
跨平台策略游戏自动化由于不同的用户界面和动态战场环境仍然是一个挑战。现有的视觉-语言模型（VLMs）在异构平台间的泛化能力较弱，并且在界面理解和动作执行上缺乏精准性。
### Innovation
提出了Yanyun-3，一种基于视觉语言模型的代理，整合了Qwen2.5-VL进行视觉推理和UI-TARS进行界面执行。提出了一种新颖的数据组织原则——组合粒度，用于区分多模态数据（静态图片、多图片序列和视频）的内样本融合和跨样本混合。模型在三个策略游戏平台的定制数据集上通过QLoRA微调。最优策略（M*V+S）在BLEU-4评分上实现了12.98倍的改进，并将推理时间减少了63%。Yanyun-3能够在没有针对特定平台调整的情况下跨平台执行核心任务（例如，目标选择、资源分配）。
### Conclusion
结构化的多模态数据组织显著提高了VLM在具身任务中的性能。Yanyun-3提供了一个可移植的框架，可用于GUI自动化，对机器人和自主系统领域具有更广泛的影响。
## 728. `cs.CV` - RadAgents: 胸部X光解读中的放射科医生样工作流程的多模态代理推理 [PDF](https://arxiv.org/pdf/2509.20490), [HTML](https://arxiv.org/abs/2509.20490)
### Authors
Kai Zhang,Corey D Barrett,Jangwon Kim,Lichao Sun,Tara Taghavi,Krishnaram Kenthapadi
### Background
代理系统通过专业代理的合作、工具辅助以及外部知识库的使用，提供了解决复杂临床任务的潜在途径。然而，胸部X光（CXR）解释中现有的方法仍然有限：推理通常不具备临床解释性和与指南一致；缺乏多模态证据的有效融合，导致仅依靠文本解释且不与图片关联；系统经常未能检测或解决工具间的不一致，并不提供可靠的验证机制。
### Innovation
我们提出了RadAgents，这是一种多代理框架，结合了临床先验知识和任务感知的多模态推理，将放射科医生的工作流程模块化并编码成可审计的流水线。此外，RadAgents整合了语境关联和多模态检索增强，以验证和解决语境冲突，产生了更可靠、透明且与临床实践一致的输出。
### Conclusion
RadAgents通过结合临床先验知识和多模态推理，构建了一个可审计的放射科医生风格的工作流程，增强了跨工具的推理一致性和可靠性，使得输出更为可靠、透明，符合临床实践。
## 729. `cs.CV` - PaSE: Prototype-aligned Calibration and Shapley-based Equilibrium for Multimodal Sentiment Analysis [PDF](https://arxiv.org/pdf/2511.17585), [HTML](https://arxiv.org/abs/2511.17585)
### Authors
Kang He,Boyu Chen,Yuzhe Ding,Fei Li,Chong Teng,Donghong Ji
### Background
多模态情感分析（MSA）旨在通过整合文本、声学和视觉信号来理解人类情感。尽管设计多模态融合以利用跨模态互补性，但在实际场景中往往会出现模态竞争：主导模态往往会掩盖较弱模态，导致性能不佳。
### Innovation
本文提出了一种新型的Prototypical对齐校准和Shapley优化均衡框架（PaSE），该框架能够增强协作同时显式地缓解模态竞争。PaSE首先应用了原型引导校准学习（PCL），并通过信息论最优传输机制来保证语义一致性，从而改进单一模态表示。此外，引入了双阶段优化策略，采用原型门控融合模块提取共享表示，接下来通过基于Shapley的梯度调制（SGM）来根据每种模态的贡献来适配调整梯度。
### Conclusion
在IEMOCAP、MOSI和MOSEI上的大量实验表明，PaSE实现了优越的性能，并有效缓解了模态竞争。
## 730. `cs.CV` - LightMem：轻量级和高效的增强记忆生成系统 [PDF](https://arxiv.org/pdf/2510.18866), [HTML](https://arxiv.org/abs/2510.18866)
### Authors
Jizhan Fang,Xinle Deng,Haoming Xu,Ziyan Jiang,Yuqi Tang,Ziwen Xu,Shumin Deng,Yunzhi Yao,Mengru Wang,Shuofei Qiao,Huajun Chen,Ningyu Zhang
### Background
尽管大型语言模型（LLMs）具有出色的能力，但在动态和复杂的环境中，它们难以有效利用历史交互信息。现有的记忆系统虽然引入了持久性信息存储、检索和利用机制，但在执行上往往伴随着大量的时间和计算开销。
### Innovation
本文提出了一种新的记忆系统LightMem，它在记忆系统的性能和效率之间取得了平衡。LightMem受Atkinson-Shiffrin人类记忆模型的启发，将记忆划分为三个互补阶段：首先，通过轻量级压缩和按主题分组快速过滤无关信息的认知启发式感觉记忆；其次，主题感知的短期记忆合并基于主题的分组，并对内容进行组织和总结，以便于结构化访问；最后，具有睡眠时间更新的长期记忆使用离线过程将合并与在线推理脱钩。
### Conclusion
在LongMemEval和LoCoMo数据集上，使用GPT和Qwen作为主干网络，LightMem在问答准确性上比强大基线提高多达7.7%/29.3%，减少总标记使用量多达38x/20.9x，API调用减少多达30x/55.5x，同时在线测试的成本更低，标记减少多达106x/117x，API调用减少多达159x/310x。相关代码可在此地址获得：[提供的URL]。
## 731. `cs.CV` - OceanGym: 用于水下自主代理的基准环境 [PDF](https://arxiv.org/pdf/2509.26536), [HTML](https://arxiv.org/abs/2509.26536)
### Authors
Yida Xue,Mingjun Mao,Xiangyuan Ru,Yuqi Zhu,Baochang Ren,Shuofei Qiao,Mengru Wang,Shumin Deng,Xinyu An,Ningyu Zhang,Ying Chen,Huajun Chen
### Background
水下环境因其极端的感知和决策挑战而被认为是现实世界中最苛刻的环境之一。与陆地或空中领域不同，水下环境中的低可见度和动态洋流使得有效的代理部署极为困难。研究人员已经设计了许多基准测试，但目前缺乏专门针对水下代理的全面基准测试。因此，开发能够在如此苛刻环境中工作的智能代理的需求依然突出。
### Innovation
OceanGym 引入了一个综合性的基准环境，专注于海洋水下代理。OceanGym 包含了八个现实的任务领域，并采用了一个由多模态大型语言模型驱动的统一代理框架，该框架整合了感知、记忆和序列决策。这是首次提供一个高保真实验平台，旨在评估和改进智能代理在水下环境中的表现。
### Conclusion
OceanGym 通过提供一个严格设计且高度真实的平台，为开发和检验可以在水下环境中执行任务的坚固的代理提供了一个重要的测试床。这标志着朝着能在地球上最后未被充分探索的领域之一（即水下环境）中运行的智能代理迈出的关键一步。同时，它也揭示了现有的最先进的多模态大型语言模型驱动的代理在感知、计划和适应性方面与人类专家之间的巨大差距，为未来的研究指明了方向。
## 732. `cs.CV` - 掌握绳索艺术，再信任胜利：渐进探索的自我模仿强化学习 [PDF](https://arxiv.org/pdf/2509.22601), [HTML](https://arxiv.org/abs/2509.22601)
### Authors
Yulei Qin,Xiaoyu Tan,Zhengbao He,Gang Li,Haojia Lin,Zongyi Li,Zihan Xu,Yuchen Shi,Siqi Cai,Renting Rui,Shaofei Cai,Yuzheng Cai,Xuan Zhang,Sheng Ye,Ke Li,Xing Sun
### Background
强化学习（RL）被广泛应用于提升大型语言模型（LLMs）在长期任务和稀疏奖励下的战略工具使用能力，但这一方法面临探索-利用平衡的挑战。现有研究通过最大化策略熵来促进探索，但这种方法容易导致RL不稳定。SPEAR提出一种自我模仿学习（SIL）策略，该策略在不陷入熵坍塌或过拟合的情况下，逐步调整策略熵以实现探索-利用平衡。
### Innovation
SPEAR方法通过融合自适应课程调度、内在奖励塑造和自我模仿学习策略，有效解决了探索-利用之间的平衡问题。特别是在初始阶段增加工具交互的频率以加速探索，在接近环境熟悉度后巩固成功的策略利用。此外，SPEAR结合了工业级别的RL优化技巧，以实现较强的基础性能。
### Conclusion
实验结果表明，SPEAR方法在ALFWorld和WebShop任务中分别提高了GRPO/GiGPO/Dr.BoT的成功率16.1%/5.1%/8.6%和20.7%/11.8%/13.9%；在AIME24和AIME25任务中分别提高了3.8%和6.1%。这一增益仅增加了10%-25%的理论复杂性，并且在实际运行中没有额外的时间开销，展示了SPEAR方法的即插即用可扩展性。
## 733. `cs.LG` - PrefixGPT: 由生成式预训练Transformer实现的前缀加法器优化 [PDF](https://arxiv.org/pdf/2511.19472), [HTML](https://arxiv.org/abs/2511.19472)
### Authors
Ruogu Ding,Xin Ning,Ulf Schlichtmann,Weikang Qian
### Background
前缀加法器在计算密集型应用中广泛应用，由于设计规则严格以及设计空间巨大，优化前缀加法器的设计具有挑战性。
### Innovation
提出了 PrefixGPT，一种生成式预训练的Transformer，可以直接从零生成优化后的前缀加法器。该模型首先通过随机合适数组生成一台器进行预训练，学习设计规则，接着进行微调以在设计空间中寻找到优化的设计。与现有方法相比，PrefixGPT 不仅找到了性能提升 7.7% 的最优设计，同时展示出优越的探索质量，平均性能降低了 79.1%。这表明 GPT 类型的模型有潜力首先掌握复杂的硬件设计原则，然后用以进行更有效的设计优化。
### Conclusion
PrefixGPT 通过生成式预训练 Transformer 技术，在前缀加法器优化方面取得了显著进展，展示了在复杂硬件设计中的潜在应用价值。
## 734. `cs.CV` - PrismAudio：分解的知识链与多维度奖励在视频到音频生成中的应用 [PDF](https://arxiv.org/pdf/2511.18833), [HTML](https://arxiv.org/abs/2511.18833)
### Authors
Huadai Liu,Kaicheng Luo,Wen Wang,Qian Chen,Peiwen Sun,Rongjie Huang,Xiangang Li,Jieping Ye,Wei Xue
### Background
视频到音频（V2A）生成需要平衡四个关键的感知维度：语义一致性、视听时间同步、美学质量以及空间准确性；但是现有方法中存在目标交织的问题，即在单一损失函数中结合了竞争性目标，并且缺乏与人类偏好的一致性。
### Innovation
引入了PrismAudio框架，该框架将强化学习引入到V2A生成中，并采用了特定的知识链（CoT）规划。该方法将整体推理分解为四个专门的CoT模块（语义、时间、美学和空间CoT），每个模块都配有一个特定的奖励函数。这种CoT与奖励的对应关系能够多维度地进行RL优化，引导模型在所有角度上共同生成更好的推理，解决目标交织问题，同时保持可解释性。此外，还提出了Fast-GRPO策略，并通过混合常微分方程-随机微分方程采样，显著减少了训练开销。同时，引入了AudioCanvas基准，这是一个更加均衡分布且涵盖了更多真实多样和具有挑战性的场景的数据集。
### Conclusion
实验结果表明，PrismAudio在领域内VGGSound测试集和领域外AudioCanvas基准上，在所有四个感知维度上都实现了最先进的性能。此项目的Web页面可访问。
## 735. `cs.CV` - 形适应门控专家: 用于结肠镜病变分割的动态专家路由 [PDF](https://arxiv.org/pdf/2511.18493), [HTML](https://arxiv.org/abs/2511.18493)
### Authors
Gia Huy Thai,Hoang-Nguyen Vu,Anh-Minh Phan,Quang-Thinh Ly,Tram Dinh,Thi-Ngoc-Truc Nguyen,Nhat Ho
### Background
计算机辅助癌症检测在吉格像素全组织切片图像（WSIs）尺度和形态上的显著多样性仍然是主要挑战，这主要是由于细胞异质性。现有的CNN-Transformer混合模型依赖于具有固定路由的静态计算图，这导致了冗余计算，并限制了它们对输入变化的适应性。
### Innovation
提出了形适应门控专家（SAGE），这是一种输入自适应框架，能够使异构视觉网络中的专家路由动态化。SAGE 将静态主干重构为动态路由专家架构。SAGE 的双路径设计包括一个保留表示的主干流，通过分层门控选择性地激活专家路径。这种门控机制在多个分层级别上操作，进行两层分层选择，选择共享和专门化的专家来调节模型的逻辑输出，以进行 Top-K 激活。该研究还提出了一种形状适应枢纽（SA-Hub），有效合并 CNN 和 Transformer 模块的结构和语义表示。
### Conclusion
通过 SAGE 实现 SAGE-UNet 模型在三个医学基准测试 EBHI、DigestPath 和 GlaS 上实现了卓越的分割性能，分别取得了95.57%、95.16%和94.17%的最佳Dice分数，并在跨领域的应用中实现了稳健的泛化能力，通过自适应平衡局部细化和全局上下文实现灵活的视觉推理。SAGE 提供了一个可扩展的框架，用于动态专家路由，使灵活的视觉推理成为可能。
## 736. `cs.CL` - MMTU：大规模多任务表格理解与推理基准 [PDF](https://arxiv.org/pdf/2506.05587), [HTML](https://arxiv.org/abs/2506.05587)
### Authors
Junjie Xing,Yeye He,Mengyu Zhou,Haoyu Dong,Shi Han,Lingjiao Chen,Dongmei Zhang,Surajit Chaudhuri,H. V. Jagadish
### Background
表格及其基于表格的应用在许多重要现实世界应用中扮演着关键角色，例如电子表格、数据库和计算笔记本，这些应用通常需要数据工程师、数据分析师和数据库管理员这样的专家级用户进行操作。尽管大语言模型（LLMs）已经在处理表格方面取得了显著进步（例如，在电子表格和数据库合作者场景中的表现），但这些能力的全面评估仍然有限。尽管自然语言处理（NLP）基准测试的数量庞大且持续增加，但关于表格相关任务的评估仍然稀缺，只能针对如自然语言到SQL和表格问答等狭窄范围的任务展开，未能涵盖专业用户面临的广泛现实应用环境。这种差距限制了我们对该领域重要性的理解及模型的进步。
### Innovation
本文介绍了一个大规模基准测试——MMTU（多任务表格理解与推理基准），包含了超过28000个问题，跨越25个实时应用中的表格任务，旨在全面评估模型在理解、推理和操作真实表格方面的专家级能力。这些任务着重于专业用户面临的复杂表格任务。研究发现，当前最前沿的模型在MMTU上仍然面临挑战，即使是类似OpenAI GPT-5和DeepSeek R1这样先进的推理模型也只能达到大约69%和57%的正确率，这表明有很大改进空间。文章通过MMTU评估中的关键发现，期望推动基础模型在结构化数据处理和分析方面的进一步发展。
### Conclusion
我们期望这个基准能够推动对大规模多任务表格理解和推理能力的进一步理解和开发，从而促进在结构化数据处理和分析方面的基础模型发展。我们的代码和数据在此处（提供链接）可以获取。
## 737. `cs.LG` - 基于机器学习算法的RAG检索的质量分析与评估预测 [PDF](https://arxiv.org/pdf/2511.19481), [HTML](https://arxiv.org/abs/2511.19481)
### Authors
Ruoxin Zhang,Zhizhao Wen,Chao Wang,Chenchen Tang,Puyang Xu,Yifan Jiang
### Background
随着大型语言模型的迅速发展，检索增强生成技术因其能够集成外部知识以提高输出准确性而被广泛应用。然而，系统的性能高度依赖于检索模块的质量。如果检索结果与用户需求的相关性低或包含噪声信息，将直接导致生成内容的失真。针对现有模型在处理表格特征方面的性能瓶颈，本论文提出了一种基于特征工程和粒子群优化的XGBoost机器学习回归模型。
### Innovation
论文通过引入一种基于特征工程和粒子群优化的XGBoost机器学习回归模型，解决了现有模型在处理表格特征方面的性能瓶颈。实验结果显示，在所有评估指标中，VMD PSO BiLSTM模型优于决策树和AdaBoost等模型，具备更优的预测精度、稳定性和数据解读能力。
### Conclusion
该研究成果为优化检索质量和提高RAG系统生成效果提供了有效路径，并在推动相关技术的实施和应用方面具有重要意义。
## 738. `cs.CV` - AutoFocus-IL: 基于VLM的无需额外人工注释的数据高效视觉模仿学习的显著性图 [PDF](https://arxiv.org/pdf/2511.18617), [HTML](https://arxiv.org/abs/2511.18617)
### Authors
Litian Gong,Fatemeh Bahrani,Yutai Zhou,Amin Banayeeanzade,Jiachen Li,Erdem Bıyık
### Background
现有的视觉模仿学习方法虽然在提高数据效率和泛化性能方面显示出潜力，但通常需要昂贵的人类监督资源，如人类注视数据或手动生成的显著性注释。AutoFocus-IL方法通过利用视觉语言模型（VLMs）自动识别和跟踪演示中的关键对象，生成时间显著性图，突出因果视觉信号并抑制干扰因素，避免了这些昂贵的监督需求。
### Innovation
AutoFocus-IL方法通过结合视觉语言模型（VLMs），自动检测和跟踪演示中的关键对象，生成突出因果视觉信号并抑制干扰因素的时间显著性图，这些图用于规范行为克隆策略，从而在视觉关注和任务相关线索间实现更强的对齐。这种方法不仅在CARLA仿真环境和真实机器人操作任务中优于标准的行为克隆方法，还在假设可以获取高级监督（如人类注视数据）的状态最先进方法中也表现出色。
### Conclusion
实验结果表明，AutoFocus-IL不仅能超越标准的行为克隆方法，还能超过那些假设可以获得人类监督作为先验信息的最新基准模型。提供的代码、数据集以及训练好的策略视频可以在文中提供的链接处获取。
## 739. `cs.LG` - 利用专家：MoE-LLMs的未授权压缩 [PDF](https://arxiv.org/pdf/2511.19480), [HTML](https://arxiv.org/abs/2511.19480)
### Authors
Pinaki Prasad Guha Neogi,Ahmad Mohammadshirazi,Dheeraj Kulshrestha,Rajiv Ramnath
### Background
混合专家（MoE）架构在大型语言模型（LLMs）中的采用越来越广泛，这得益于其可扩展性和效率。然而，MoE的模块化结构引入了一个独特的问题：攻击者可以通过剪枝专家并廉价微调剩余部分来尝试压缩或重新利用模型，从而有效地规避了许可和安全约束。
### Innovation
本文系统研究了在特定任务使用下MoE-LLMs的剪枝脆弱性。首先，开发了一个专家归因框架，以识别最具任务负责性的专家子集，然后评估使用主动学习驱动的微调进行剪枝和重新对齐时的性能权衡。研究表明，虽然可以隔离某些专家以保留任务准确性，但如果没有目标对齐，会造成显著的性能下降。基于这一分析，本文提出防御策略，旨在使MoE模型在未经授权的情况下更难以压缩和微调，包括纠缠专家训练和选择性微调协议，这些协议能够抵抗未经授权的适应。通过将专家剪枝视为威胁向量和防御目标，本文揭示了MoE模块化的双重用途，并提供了第一个关于MoE-LLMs的安全专业化系统的评估框架。
### Conclusion
该工作强调了MoE模块化在双重用途中的重要性，并提供了关于MoE-LLMs的首个系统评估框架，为实现安全专业化提供了新的防御策略。
## 740. `cs.LG` - 基于隐藏马尔可夫模型预测游客访问地点 [PDF](https://arxiv.org/pdf/2511.19465), [HTML](https://arxiv.org/abs/2511.19465)
### Authors
Theo Demessance,Chongke Bi,Sonia Djebali,Guillaume Guerard
### Background
如今，社交媒体成为分析游客行为的一种流行方式，因为游客在旅行期间在这些网络上留下的数字足迹使大量数据得以产生。这些数据通过游客分享旅行中的评论和照片而生成，从而有可能建模并分析他们的旅行行为。了解和预测游客的下一步行动对旅游业营销至关重要，有助于理解需求并改善决策支持。
### Innovation
本文提出了一种基于社会网络数据的机器学习语法推理算法来理解和学习游客的移动模式，进而预测未来旅游行为。主要创新在于将语法推理算法适应大数据环境。该方法生成一个隐藏马尔可夫模型，可以灵活地根据新的数据进行编辑。
### Conclusion
我们选择法国首都巴黎来展示所提出方法的有效性。这片研究展示了如何利用隐藏马尔可夫模型来预测和分析游客的旅行行为。
## 741. `cs.LG` - 使用有限人类数据高效推理的大语言模型：微调然后矫正 [PDF](https://arxiv.org/pdf/2511.19486), [HTML](https://arxiv.org/abs/2511.19486)
### Authors
Lei Wang,Zikun Ye,Jinglong Zhao
### Background
近年来，人工智能（AI）的发展证明了大语言模型（LLMs）在市场研究和社会科学研究中的潜力，可以生成人类类似响应。改善LLMs性能的两种主要方法是微调和矫正。微调使LLM预测更接近人类反应，而矫正则纠正LLM输出中的偏见。
### Innovation
该论文提出了一个结合微调和矫正的框架，并优化了有限标记样本在两个阶段中的分配。不同于传统的最小化均方预测误差的目标，该论文建议以预测误差方差最小化作为微调目标，这为下游矫正阶段提供了最优性。基于这一见解，利用经验标度律开发了一种数据驱动方法，用于在微调和矫正阶段之间最优分配样本。实证分析验证了该框架，展示了与其他单独使用微调或矫正相比，改进了估计和推断性能。
### Conclusion
该框架验证了使用有限人类数据有效推理大语言模型的方法，并通过结合微调和矫正，优化了样本分配以提高模型性能。
## 742. `cs.LG` - FDD mMIMO-OFDM系统中辅助生成模型的持续学习方法用于CSI反馈 [PDF](https://arxiv.org/pdf/2511.19490), [HTML](https://arxiv.org/abs/2511.19490)
### Authors
Guijun Liu,Yuwen Cao,Tomoaki Ohtsuki,Jiguang He,Shahid Mumtaz
### Background
深度自动编码器（DAE）框架在大规模多输入多输出（mMIMO）正交频分多址（OFDM）系统中展示出减少信道状态信息（CSI）反馈开销的有效性。现有的CSI反馈模型在面对由用户移动引起的动态环境时，需要重新训练以适应新出现的CSI分布。此外，在回到之前遇到的环境中时，性能往往会因灾难性遗忘而下降。持续学习涉及让模型能够结合新的信息并保持在之前学习任务上的性能。
### Innovation
提出了一种基于生成对抗网络（GAN）的学习方法，通过使用GAN生成器作为记忆单元，该方法能够保存过去环境的知识，并确保在各种情况下保持高性能，而不会遗忘。实验结果表明，该方法在保持低内存开销的同时增强了DAE框架的泛化能力，并且可以通过与其他先进的CSI反馈模型无缝集成来展示其鲁棒性和适应性。
### Conclusion
仿真结果表明，所提出的方法增强了DAE框架的泛化能力，同时保持了较低的内存开销。此外，该方法可以与其他先进的CSI反馈模型无缝集成，突出其鲁棒性和适应性。
## 743. `cs.LG` - OmniTFT: 多中心重症监护病房数据中生命体征和实验室结果轨迹的全面目标预测 [PDF](https://arxiv.org/pdf/2511.19485), [HTML](https://arxiv.org/abs/2511.19485)
### Authors
Wanzhe Xu,Yutong Dai,Yitao Yang,Martin Loza,Weihang Zhang,Yang Cui,Xin Zeng,Sung Joon Park,Kenta Nakai
### Background
准确的多变量时间序列预测对于重症监护病房(ICU)中的早期干预和精准医疗至关重要。然而，生命体征通常噪声较大且快速波动，而实验室测试则存在缺失值、测量延迟和设备特定偏差等问题，使得综合预测变得极为具有挑战性。
### Innovation
本文提出了一种名为OmniTFT的深度学习框架，该框架基于Temporal Fusion Transformer(TFT)的同时学习和预测高频生命体征和稀疏采样的实验室结果。具体来说，OmniTFT 实施了四种新的策略来提升性能：滑动窗口等化采样平衡生理状态、频率感知嵌入收缩稳定稀有类表示、层次变量选择指导模型关注于具有信息量的特征簇，以及影响对齐注意校准增强在急剧生理变化期间的鲁棒性。通过减少对目标特定架构和大量特征工程的依赖，OmniTFT 实现了对多种异质临床目标的统一建模，同时保持跨机构的一般化。
### Conclusion
OmniTFT 在MIMIC-III、MIMIC-IV和eICU数据集上的预测任务中，对于生命体征和实验室结果都实现了显著的性能提升。它的注意模式是可解释的，并且与已知病理生理学相一致，突显了其在临床护理中的定量决策支持潜力。
## 744. `cs.LG` - 波前扩散：改进推理的动态解码调度 [PDF](https://arxiv.org/pdf/2511.19473), [HTML](https://arxiv.org/abs/2511.19473)
### Authors
Haojin Yang,Rui Hu,Zequn Sun,Rui Zhou,Yujun Cai,Yiwei Wang
### Background
扩散语言模型（DLMs）因其强大的文本生成能力成为与自回归模型竞争的选择。主流的去噪策略包括标准扩散和块扩散。标准扩散方法在未完成上下文的情况下结束并产生过早的序列终止预测，而块扩散方法虽然具有固定的更新顺序但其僵化的结构会破坏语义单位的连贯性和推理过程。
### Innovation
提出了动态解码方法，即波前扩散（WavefrontDiffusion），能够从已完成的位置向外扩散活性令牌。这种方法适应性强，遵循自然的语义结构流动，并且计算成本与基于块的方法相同。在四个推理和代码生成基准测试中，波前扩散达到最先进的性能并产出更高语义准确度的结果，突出了自适应调度对于更具连贯性和高效生成的重要性。
### Conclusion
研究表明，波前扩散在提高生成效率和语义准确性方面具有显著优势，是一种值得探讨的动态解码调度策略。
## 745. `cs.LG` - 通过拆分多模态表示来量化模态贡献 [PDF](https://arxiv.org/pdf/2511.19470), [HTML](https://arxiv.org/abs/2511.19470)
### Authors
Padegal Amit,Omkar Mahesh Kashyap,Namitha Rayasam,Nidhi Shekhar,Surabhi Narayan
### Background
多模态模型中模态贡献的量化仍然是一个挑战，因为现有方法混淆了贡献的实际概念。以往的工作依赖于基于准确性的方法，通过移除模态后的性能下降来间接评估其影响。然而，这种基于结果的度量无法区分模态是本身具有信息性，还是其价值仅通过与其他模态的交互产生。这种区别在交叉注意力架构中尤为重要，因为模态相互影响对方的表示。
### Innovation
本文提出了一种基于部分信息分解(PID)的框架，通过在内部嵌入中分解预测信息为独特的、冗余的和协同的组成部分来量化模态贡献。同时，开发了一种基于迭代比例拟合程序(IPFP)的算法，无需重新训练即可计算层和数据集级别的贡献，从而提供了从表征层面的多模态行为的客观视图，并提供了比基于结果的度量更清晰和更可解释的见解。
### Conclusion
提出了基于PID的框架和基于IPFP的算法，提供了一种新的方法量化多模态模型中模态的贡献。这种方法提供了更清晰、更可解释的见解，比基于结果的度量更为客观。
## 746. `cs.LG` - RFX：带GPU加速和QLORA压缩的高性能随机森林 [PDF](https://arxiv.org/pdf/2511.19493), [HTML](https://arxiv.org/abs/2511.19493)
### Authors
Chris Kuchar
### Background
随机森林（Random Forest）是一种常用的机器学习方法，特别是在分类任务中展示出优秀的性能。然而，传统的随机森林方法在处理大规模数据集时由于邻近矩阵（proximity matrix）占用大量内存，限制了其应用的范围。
### Innovation
该论文提出了RFX（Random Forests X），其中X代表压缩或量化，它为随机森林分类方法提供了生产级别的Python实现。论文引入了QLORA（Quantized Low-Rank Adaptation）压缩技术，用于GPU上的邻近矩阵压缩；还提出了CPU TriBlock临近矩阵，结合上三角存储和块稀疏阈值处理，实现内存减少2.7倍且无损质量的效果；此外，通过GPU批次优化和3D MDS可视化加速等方法，解决了随机森林邻近矩阵内存瓶颈，使得能够处理比以往多数量级的数据集。
### Conclusion
RFX v1.0 解决了随机森林邻近矩阵占用大量内存的问题，使大规模数据集的随机森林分析成为可能，同时提供了准确的整体重要性估计、局部重要性测量、案例分析和交互式可视化等功能，提升了用户在随机森林领域的使用体验。
## 747. `cs.LG` - 广义的Proximity Forest [PDF](https://arxiv.org/pdf/2511.19487), [HTML](https://arxiv.org/abs/2511.19487)
### Authors
Ben Shaw,Adam Rustad,Sofia Pelagalli Maia,Jake S. Rhodes,Kevin R. Moon
### Background
近期研究表明，随机森林（RF）接近度在监督机器学习任务中具有多种用途，包括离群值检测、缺失数据插补和可视化等。然而，RF接近度的有效性依赖于RF模型的成功，而RF模型并不在所有情况下都是理想模型。最近，距离基的Proximity Forest（PF）模型被用于时间序列分析，提供了利用RF接近度的优势。
### Innovation
本文引入了广义的PF模型，使其适用所有可进行监督距离基机器学习的情境，并且还提出了适用于回归任务的PF模型变种。此外，还引入了使用广义的PF模型作为元学习框架的概念，扩展了使用任何预训练分类器的监督插补能力。
### Conclusion
通过实验表明，广义的PF模型相比RF模型和$k$-最近邻模型具有独特的优势。
## 748. `cs.LG` - OpenCML：逐步学习未知类别的开放世界机器学习端到端框架 [PDF](https://arxiv.org/pdf/2511.19491), [HTML](https://arxiv.org/abs/2511.19491)
### Authors
Jitendra Parmar,Praveen Singh Thakur
### Background
传统机器学习模型多假设为封闭世界，这限制了它们保留之前学习的知识以应对未来的任务。然而，自动化智能系统需要识别新类别并学习之前已知的任务。现有的模型在这种开放且连续的学习环境中无法有效进行新的类别学习。
### Innovation
该研究提出了OpenCML模型，该模型能够在开放和连续学习环境中完成新学习类别的发现和增量学习。该模型包括两个不同的但相互连接的任务：一是识别数据中的未知类别并创建新类；二是对每个新类逐步学习类别。这使得系统能够扩展其对数据的理解并随着时间的推移而改进。此外，OpenCML模型在开放世界学习中优于现有方法，并且在连续学习中表现优异，四次迭代的最高平均准确率为82.54%，最低准确率为65.87%。
### Conclusion
OpenCML提供了一种端到端的框架，能够逐步学习未知类别，展现出在开放世界和连续学习中的优越性能。
## 749. `cs.LG` - PeriodNet：提升注意力机制在时间序列预测中的潜力 [PDF](https://arxiv.org/pdf/2511.19497), [HTML](https://arxiv.org/abs/2511.19497)
### Authors
Bowen Zhao,Huanlai Xing,Zhiwen Xiao,Jincheng Peng,Li Feng,Xinhan Wang,Rong Qu,Hui Li
### Background
注意力机制在序列建模中表现出显著的潜力，特别是在自然语言处理领域取得了成功应用，如Bidirectional Encoder Representations from Transformers（BERT）和Generative Pre-trained Transformer（GPT）等模型。尽管取得了这些进展，但在时间序列预测（TSF）中的应用仍未达到预期。因此，探索更好地利用注意力机制以改进时间序列预测的网络结构显得尤为重要。
### Innovation
本文提出了一种名为PeriodNet的新结构，用于多变量和单变量时间序列的预测。PeriodNet结合了周期注意力和稀疏周期注意力机制，以分析相邻时期。通过引入迭代分组机制直接减少跨变量冗余。PeriodNet还重新设计了基础Transformer的整体架构，并提出了周期扩散器以实现精确的多周期预测。
### Conclusion
通过对八个数据集进行全面实验，结果表明，PeriodNet在时间序列预测中表现出色，无论是单变量还是多变量场景，在均方误差和平均绝对误差方面均优于六种最先进的模型。特别是在预测长度为720的时间序列时，相对改进达到了22%。
## 750. `cs.LG` - Xmodel-2.5: 1.3B Data-Efficient Reasoning SLM [PDF](https://arxiv.org/pdf/2511.19496), [HTML](https://arxiv.org/abs/2511.19496)
### Authors
Yang Liu,Xiaolong Zhong,Ling Jiang
### Background
大型语言模型（LLMs）虽然在推断和工具使用方面表现出色，但由于计算需求高，使得它们对于边缘设备或成本敏感的应用场景不太实用。本研究旨在开发一种小型、高效的替代模型。
### Innovation
作者提出了一款名为Xmodel-2.5的小型模型，参数量为1.3亿，设计为即插即用的核心代理。该模型通过最大更新参数化（$u$P）训练，在参数共享的情况下也能实现高效的迁移学习。还使用了特定的学习曲线，并在衰减阶段切换使用Muon优化器替代AdamW，显著提高了任务推理性能。
### Conclusion
Xmodel-2.5以1.3B的参数实现了高效推理，通过一定的训练技巧和优化器切换，验证了可以在保持其他超参数不变的情况下提升推理性能。所有训练代码、评估代码和检查点都开放给公众使用。
## 751. `cs.LG` - 超越二分类：一种泛化的AI生成图像检测的半监督方法 [PDF](https://arxiv.org/pdf/2511.19499), [HTML](https://arxiv.org/abs/2511.19499)
### Authors
Hong-Hanh Nguyen-Le,Van-Tuan Tran,Dinh-Thuc Nguyen,Nhien-An Le-Khac
### Background
随着生成器（如StyleGAN、Midjourney、DALL-E）的快速进步，产生了高度逼真的合成图像，给数字媒体的真实性带来了重大挑战。目前的鉴别器在进行跨生成器的一般化检测，尤其是跨越架构边界（如从生成对抗网络（GANs）到扩散模型（DMs））时效果不佳。这种缺陷源自于不同架构生成的特征的不同基础性差异。
### Innovation
本文提供了一种理论分析，解释了GAN和DM架构的不同优化目标是如何导致不同的流形覆盖行为的。基于此分析，提出了一种三元架构检测器（TriDetect），一种半监督方法，通过发现“假”类别中的潜在架构模式来增强二分类。TriDetect使用平衡聚类分配和跨视图一致性机制，鼓励模型学习基础的架构不同性。
### Conclusion
我们的方法在两个标准基准和三个野外数据集上与13个基线进行了评估，证明了其在未见过的生成器上的泛化能力。
## 752. `cs.LG` - 完美人工智能对齐的复杂性--RLHF三难困境的形式化 [PDF](https://arxiv.org/pdf/2511.19504), [HTML](https://arxiv.org/abs/2511.19504)
### Authors
Subramanyam Sahoo,Aman Chadha,Vinija Jain,Divya Chaudhary
### Background
强化学习从人类反馈（RLHF）广泛应用于使大型语言模型对齐，但由于实际操作中的问题，提高安全性时往往会减少公平性，扩展到不同的人群变得计算上不可行，提升系统稳健性时反而加剧了多数群体的偏见。因此，作者将这种紧张关系称为对齐三难困境：没有一个RLHF系统能够同时满足以下三个条件：(i) 跨多种人类价值观近似代表性；(ii) 样本和计算复杂度的多项式可管理性；(iii) 在对抗性扰动和分布漂移下具有delta-稳健性。
### Innovation
通过结合统计学习理论和鲁棒优化，作者证明了要对全球人群同时实现代表性和稳健性（代表性的ε≤0.01和稳健性的δ≤0.001）所需的运算量为Ω(2^d_context)，这在上下文维度上是非多项式的。此外，作者指出当前的RLHF实现通过牺牲代表性来解决这一三难问题：仅从同质的注释者池中收集了10^3到10^4个样本，而真正实现全球代表性则需要10^7到10^8个样本。该框架为完美人工智能对齐的文档化RLHF病理现象（如偏好崩溃、拍马屁以及系统性偏差放大）提供了一个统一解释，并提出了可通过战略性放松对齐要求来应对这些基本权衡的具体方向。
### Conclusion
本文通过一个复杂度理论分析，提出了强化学习从人类反馈的三难困境，指出当前的RLHF实施方式通过牺牲代表性来应对这一困境。作者提供了统一解释从RLHF中观察到的一些典型问题，并提出了通过战略性放松对齐要求来应对这些基本权衡的具体方向。
## 753. `cs.LG` - 大型语言模型压缩顺序的系统研究 [PDF](https://arxiv.org/pdf/2511.19495), [HTML](https://arxiv.org/abs/2511.19495)
### Authors
Shivansh Chhawri,Rahul Mahadik,Suparna Rooj
### Background
大语言模型（LLMs）需要大量的计算资源，因此在资源受限的环境中高效部署这些模型需要模型压缩技术。知识蒸馏、结构化剪枝和低比特量化是主流的压缩方法，但它们的独立效果已被广泛研究，而它们之间的交互作用和最优顺序仍然不清楚。
### Innovation
本文系统地研究了这些技术在单独应用和组合应用时的表现，并使用多个压缩流水线来评估其性能。研究发现，量化在单独应用时提供最大的压缩效果，而剪枝会引入适度的质量下降。关键是技术的顺序对最终模型质量有显著影响：剪枝、知识蒸馏、量化（P-KD-Q）的顺序能够获得最佳平衡，实现3.68倍的压缩比，同时保持强大的指令理解和语言理解能力。相反，早期应用量化会导致性能严重下降，因为不可逆的信息损失影响了后续训练。
### Conclusion
本研究为在资源受限环境中部署LLMs提供了实用的见解，提出了具有顺序意识的有效压缩流水线设计方法。
## 754. `cs.LG` - 使用不完整且敏感医疗数据进行生物医学和医疗智能的分层双策略遗忘 [PDF](https://arxiv.org/pdf/2511.19498), [HTML](https://arxiv.org/abs/2511.19498)
### Authors
Yi Zhang,Tianxiang Xu,Zijian Li,Chao Zhang,Kunyu Zhang,Zhan Gao,Meinuo Li,Xiaohan Zhang,Qichao Qi,Bing Chen
### Background
大型语言模型（LLMs）在性能上表现出色，但在训练数据记忆方面也带来了严重的隐私风险，尤其是在包含不完整或隐私敏感的患者信息的医疗环境中。研究表明，这些模型在处理这类数据时会给隐私保护带来挑战。
### Innovation
本文提出了一种分层双策略框架，用于选择性地遗忘特定知识，同时维护基本的医疗技能。该方法结合了几何约束梯度更新，以选择性地调节目标参数，并通过一个统一的四级医疗概念层次，区分开需要保留和需要遗忘的标记。这种方法在 MedMCQA（外科）和 MHQA（焦虑、抑郁、创伤）数据集上进行了全面评估，显示了卓越的表现。
### Conclusion
该框架在只需修改0.1%参数的情况下，实现了82.7%的知识遗忘率和88.5%的知识保留率，同时保持了强大的隐私保障。这种方法满足了监管合规、可审计性和伦理标准等方面在临床研究中的关键需求。
## 755. `cs.LG` - 使用共训练架构解决加权最大 satisfiability 问题 [PDF](https://arxiv.org/pdf/2511.19544), [HTML](https://arxiv.org/abs/2511.19544)
### Authors
Kaidi Wan,Minghao Liu,Yong Lai
### Background
本文提出了基于图神经网络（GNN）的方法 SplitGNN，用于解决加权最大满足性（MaxSAT）问题。提出了边分裂因子图这一新的图表示方法，结合监督消息传递机制和无监督解增强层，通过生成树生成和边分类提供更多的结构信息，以提高复杂和加权实例的解的质量。
### Innovation
SplitGNN 采用了共训练架构，结合了监督消息传递机制和无监督解增强层。引入了一种新的图表示方法——边分裂因子图，基于生成树生成和边分类，提供更多的结构信息，以提高复杂和加权实例的解的质量。另外，实现了一种基于 GPU 的加速层，通过高效的评分计算和基于松弛的优化提高了解决方案的质量。
### Conclusion
实验表明，与基于 GNN 的其他架构相比，SplitGNN 在收敛速度和预测准确性方面提高了三倍。更重要的是，SplitGNN 在更大和更难的加权 MaxSAT 基准测试中成功找到了优于现代启发式 MaxSAT 求解器的解，并展示了在多种结构实例中非凡的泛化能力。
## 756. `cs.LG` - 基于差分进化的大数据流稀疏特征选择 [PDF](https://arxiv.org/pdf/2511.19555), [HTML](https://arxiv.org/abs/2511.19555)
### Authors
Ruiyang Xu
### Background
高维度流式数据的处理通常使用在线流式特征选择(OSFS)技术。然而，由于设备故障和技术限制，实际应用中常遇到数据不完备的问题。现有的OSFS方法存在特征评估不足的问题，导致性能下降。
### Innovation
本文提出了一种新的在线差异进化稀疏特征选择方法(ODESFS)，采用了两项关键创新：(1) 使用潜在因子分析模型填补缺失值；(2) 通过差异进化进行特征重要性评价。
### Conclusion
通过在六个真实数据集上的全面实验，论文证明ODESFS方法在选择最优特征子集和获得更优精度方面优于最先进的OSFS和OS2FS方法。
## 757. `cs.LG` - 生成器：从叙述到二进制矩阵表示的桥梁 [PDF](https://arxiv.org/pdf/2511.19506), [HTML](https://arxiv.org/abs/2511.19506)
### Authors
Raoul H. Kutil,Georg Zimmermann,Barbara Strasser-Kirchweger,Christian Borgelt
### Background
精神健康障碍，特别是在DSM-5中详细描述的认知障碍，这些障碍通常表现为认知功能的缺陷，具有明确的定义和症状。一种简化的机器可执行表示方法被开发出来评估这些障碍的相似性和可分性，但这种方法不适合处理最复杂的情况。由于症状组合的多样性，生成或应用完整的二进制矩阵来进行相似性计算是不可行的。
### Innovation
该研究开发了一种替代方案，将DSM-5的叙述形式与二进制矩阵表示法联系起来，以使自动化生成有效的症状组合成为可能。该格式被称为症状概要生成器（或简称生成器），它提供了一种易于阅读、适应性强的替代二进制矩阵的方案，并允许生成症状组合（概要）。此外，通过生成几种精神病性障碍的生成器形式，并计算所有症状组合，证明了二进制矩阵表示法对于复杂障碍太过庞大。因此，发展了一种使用目标生成器操作来找到特定二进制余弦相似性值的问题谱减少方法。
### Conclusion
通过该生成器，可以更容易地创建大矩阵的二进制表示，并通过条件生成器计算复杂障碍之间的特定二进制余弦相似性值。
## 758. `cs.LG` - 快捷不变性：分离潜在空间中的目标化雅可比正则化 [PDF](https://arxiv.org/pdf/2511.19525), [HTML](https://arxiv.org/abs/2511.19525)
### Authors
Shivam Pal,Sakshi Varshney,Piyush Rai
### Background
深度神经网络容易学习训练数据中的快捷路径、虚假关联和易于学习的关联，这些关联会导致严重的面向分布外（OOD）泛化失败。主流的研究方法是通过学习鲁棒的表示来实现鲁棒性，通常会显式地将潜在空间划分为核心和虚假的组件；这种方法可能比较复杂、脆弱且难以扩展。
### Innovation
本文提出了一种不同的方法，不学习鲁棒表示，而是学习鲁棒函数。作者提出了一种简单且有效的训练方法，使得分类器对快捷信号具有函数不变性。该方法在分离潜在空间中，将虚假和核心特征分离到不同的维度，这种分离有助于通过这些特征与标签的强关联来识别候选的快捷特征，作为语义简单性的代理。然后，通过在训练过程中注入目标化的各向异性潜在噪声来使分类器对这些特征脱敏。作者将这种做法视为目标化的雅可比正则化，这种正则化迫使分类器忽略虚假特征，依赖于更复杂的核心语义信号。
### Conclusion
该方法在公认的快捷学习基准上的面向分布外（OOD）性能达到了最先进的水平。
## 759. `cs.LG` - 自动化欺骗：可扩展的多轮大语言模型逃逸 [PDF](https://arxiv.org/pdf/2511.19517), [HTML](https://arxiv.org/abs/2511.19517)
### Authors
Adarsh Kumarappan,Ananya Mujoo
### Background
多重对话攻击利用心理学原理如踏门槛效应（FITD），通过提出一个小初始请求，为更大的后续请求铺路，从而使大型语言模型（LLMs）的安全对齐失效，构成了持续的威胁。当前防御这些攻击的进展受到大规模手动数据集创建难以为继的限制。
### Innovation
提出了一种新的自动化流水线，用于生成大规模、基于心理学原理的多轮逃逸数据集。系统地将FITD技术转化为可重复的模板，创建了涉及非法活动和不当内容的1,500种情境基准。评估了来自三个主要LLM系列的七个模型，在多轮（带上下文）和单轮（不带上下文）条件下，揭示了显著差异的上下文鲁棒性。
### Conclusion
这项研究指出，当前的安全架构在处理对话背景时存在关键差异，突显了需要能够抵御基于叙述的操控的防御措施。GPT家族的模型对对话背景表现出显著漏洞，而Google的Gemini 2.5 Flash表现出色，几乎不受这些攻击的影响，Anthropic的Claude 3 Haiku则具有较强的但不完全的抵抗力。
## 760. `cs.LG` - 何时应用神经数据来影响福利？神经经济学在政策使用中的批判性框架 [PDF](https://arxiv.org/pdf/2511.19548), [HTML](https://arxiv.org/abs/2511.19548)
### Authors
Yiven(Louis)Zhu
### Background
神经经济学旨在把福利分析建立在关于人们如何评估结果、从经验中学习以及自我控制的神经和计算证据之上。同时，政策和商业行为者越来越多地引用神经数据来证明家长式的监管、基于大脑的干预措施和新的福利措施是正当的。然而，神经数据是否应该合法地用于影响政策制定，而不仅仅是描述行为，目前仍存在争议。
### Innovation
本文提出了一个非经验性的、模型基于框架来连接三个层面：神经信号、计算决策模型和规范性福利标准。在演员-评论家强化学习模型内，正式化了从神经活动推导出潜在价值和预测误差，进而推导出福利主张的过程。研究表明，只有在神经-计算映射验证良好、决策模型可以区分真正的利益和情境依赖的错误、以及规范性福利标准明确说明并辩护时，神经证据才能限制福利判断。
### Conclusion
将框架应用于成瘾、神经市场营销和环境政策，本文为监管者和神经AI系统设计师制定了一个神经经济学福利推理清单，即神经经济福利推理检查表。脑和人工代理被看作是价值学习系统，文章表明，无论是生物性的还是人造的内部奖励信号都是计算量度，无法直接作为福利指标，除非有明确的规范性模型。
## 761. `cs.LG` - 一种隐空间不变性的语言模型反转视角 [PDF](https://arxiv.org/pdf/2511.19569), [HTML](https://arxiv.org/abs/2511.19569)
### Authors
Wentao Ye,Jiaqi Hu,Haobo Wang,Xinpeng Ti,Zhiqing Xiao,Hao Chen,Liyao Li,Lei Feng,Sai Wu,Junbo Zhao
### Background
语言模型反转（LMI），即从输出中恢复隐藏提示，成为用户隐私和系统安全的实际威胁。本文重新定义了LMI为复用LLM的潜在空间，并提出了一种不变的潜在空间假设（ILSH）：（1）来自同一源提示的多样化输出应保持一致的语义（源不变性），（2）输入到输出的循环映射应在共享的潜在空间内保持自我一致性（循环不变性）。研究表明，广泛采用的防御措施提供的保护有限，强调了更强策略的重要性。
### Innovation
本文提出了Inv^2A，该方法将LLM视为不变解码器，并学习仅包含输出到去噪伪表示的小型逆编码器。当可用多个输出时，在表示层稀疏连接以增加信息密度。训练分为对比对齐（源不变性）和监督强化（循环不变性）两个阶段。Inv^2A在9个数据集上的表现优于基线模型，平均BLEU分数提高4.77%，且减少了对大量逆语料库的依赖。
### Conclusion
进一步的分析表明，常见防御措施提供的保护有限，因此强调了更强策略的必要性。实验结果表明，Inv^2A在保护用户隐私和系统安全方面更为有效。
## 762. `cs.LG` - 基于结构的神经可实现性：图组合优化的模型增强算法 [PDF](https://arxiv.org/pdf/2511.19573), [HTML](https://arxiv.org/abs/2511.19573)
### Authors
Jialiang Li,Weitong Chen,Mingyu Guo
### Background
神经模型在解决NP难的图组合优化（CO）问题上表现出希望，能够提供快速推理和相对高质量的解答，但在绝对的解决方案质量上不如经典基于搜索的算法，后者尽管速度较慢但提供了搜索完成后的最优解保证。
### Innovation
提出了一种结合神经模型的高效推理能力和基于搜索算法探索力的新框架。该框架使用参数化算法（PAs）作为搜索组件，利用PAs识别容易实例和结构简单性来实现高效搜索。该框架通过使用参数化分析识别CO实例的结构难题部分，神经模型生成基于数据驱动理解的建议信号，PAs结合建议信号系统地和高效地搜索剩余的结构容易部分。该框架对神经模型的选择不敏感，并且能够比单独的神经求解器产生更好的解决方案。
### Conclusion
在多种CO任务上测试该框架，实验证明它可以实现优质的解决方案，与商业求解器竞争。使用神经模型仅作为探索性建议信号的优势使得该框架展现出更好的分布外泛化能力，解决现存神经CO求解器的关键缺点。
## 763. `cs.LG` - TouchFormer: 基于Transformer的鲁棒多模态材料感知框架 [PDF](https://arxiv.org/pdf/2511.19509), [HTML](https://arxiv.org/abs/2511.19509)
### Authors
Kailin Lyu,Long Xiao,Jianing Zeng,Junhao Dong,Xuexin Liu,Zhuojun Zou,Haoyue Yang,Lin Shu,Jie Hao
### Background
传统的基于视觉的材料感知方法，在视觉受限条件下表现较差，因此转向非视觉的多模态材料感知成为趋势。然而，现有方法通常进行简单的多模态输入融合，忽视了模态特异性噪声、缺失模态以及各模态在任务中动态变化的重要性等问题，这些缺陷导致模型在多个基准测试任务中的表现不佳。
### Innovation
提出了一个鲁棒的多模态融合框架TouchFormer。具体而言，采用模态自适应门控（MAG）机制和跨模态注意力机制，以自适应的方式整合跨模态特征，增强模型的鲁棒性。此外，引入了跨实例嵌入正则化（CER）策略，显著提高了细分类材料识别任务中的分类准确性。
### Conclusion
与现有的非视觉方法相比，提出的TouchFormer框架在SSMC和USMC任务中分别实现了2.48%和6.83%的分类准确性提升。此外，现实中的机器人实验验证了TouchFormer在环境感知和解释中的有效性，预示着其在紧急救援和工业自动化等关键应用中的部署前景。代码和数据集将开源，并在补充材料中提供视频。
## 764. `cs.LG` - 学习大规模多任务世界模型进行连续控制 [PDF](https://arxiv.org/pdf/2511.19584), [HTML](https://arxiv.org/abs/2511.19584)
### Authors
Nicklas Hansen,Hao Su,Xiaolong Wang
### Background
现有的强化学习（RL）对于连续控制的研究仍然主要集中在单一任务或脱机模式上，这强化了一种观点，即在线的强化学习无法扩展。研究旨在通过大量多任务的方式，训练一种通用的控制代理，使其能够跨多个任务和实体进行操作。
### Innovation
提出了一个包含200个多样化任务的新基准，每个任务都有语言指示、示范和可选的图像观察。通过一种基于语言的多任务世界模型（Newt），该模型先通过示范进行大规模预训练以获得任务相关的表示和动作先验，然后再通过与所有任务的在线交互进行联合优化。实验显示，Newt相比现有的强基准模型表现出了更好的多任务性能和数据效率，并且能够进行有效的开环控制和快速适应未见过的任务。
### Conclusion
该项研究发布的新环境、示范、训练和评估代码以及200多个检查点可加速基于多任务的连续控制研究。
## 765. `cs.LG` - ModHiFi: 确认高保真预测组件以进行模型修改 [PDF](https://arxiv.org/pdf/2511.19566), [HTML](https://arxiv.org/abs/2511.19566)
### Authors
Dhruva Kashyap,Chaitanya Murti,Pranav K Nayak,Tanay Narshana,Chiranjib Bhattacharyya
### Background
开放的权重模型通常很少提供训练数据或损失函数的访问权限，这限制了对这些模型进行剪枝或遗忘等任务的修改能力。现有技术通常需要梯度或真实标签，使得在计算资源有限的情景下难以实现。现有文献中，这些模型被假定为不具备Lipschitz连续性，但本文作者通过理论证明，Lipschitz-连续的网络（如CNN和训练良好的Transformer）具备该性质，从而开启了仅通过局部重构行为来评估组件全局重要性的可能性。
### Innovation
本文提出了一种名为Subset Fidelity的度量方法，用于通过本地重构行为来量化模型组件的重要程度。在特征不相关的情况下，根据Subset Fidelity得分选择单独的组件是最优方案。据此，作者开发了两个算法：ModHiFi（用于模型修改）和ModHiFi-P（用于结构化剪枝），凭借一项速度提高11%并达到当前最佳状态的图像网模型结果，与ModHiFi-P comparative performance上也是如此。同时，ModHiFi-U能够实现CIFAR-10上的完全遗忘，并在网络模型上展示竞争力。
### Conclusion
通过理论证明和实践验证，ModHiFi展示了在无训练数据和损失函数访问的前提下，能够通过局部重构行为来评估组件重要性的能力，实现模型的高效修改。
## 766. `cs.LG` - 通过最优传输实现无遗忘的任务特定模型连续融合 [PDF](https://arxiv.org/pdf/2511.19561), [HTML](https://arxiv.org/abs/2511.19561)
### Authors
Zecheng Pan,Zhikang Chen,Ding Li,Min Zhang,Sen Cui,Hongshuo Jin,Luqi Tao,Yi Yang,Deheng Ye,Yu Zhang,Tingting Zhu,Tianling Ren
### Background
将针对不同任务进行微调的模型合并为单一通用模型已成为构建多功能、高效多任务系统的重要方向。现有的方法主要依赖参数插值，在权重量空间中引入了显著的特征空间分布偏移，从而削弱了特定任务的知识。
### Innovation
本文提出了基于最优传输理论的OTMF (Optimal Transport-based Masked Fusion) 框架，解决由简单参数插值引起的特征空间分布偏移问题。OTMF 不直接聚合特征或权重，而是通过最优传输计划发现适用于任务向量的共同遮罩，以对齐任务特定模型的语义几何结构。这些遮罩选择性地提取可转移和任务无关的组件，同时保留每个任务的独特结构身份。此外，OTMF 还支持一种连续融合范式，可以增量集成每个新任务向量而不回顾先前的任务，从而保持有限的内存占用，并在越来越多的任务中实现高效融合。
### Conclusion
我们通过大规模实验在多个视觉和语言基准上测试了OTMF，结果显示OTMF在准确性和效率方面均达到最新水平。这些结果突显了我们方法在模型融合中的实际和理论价值。
## 767. `cs.LG` - 一阶黑箱下非凸-强凸双层最优化的复杂性下界 [PDF](https://arxiv.org/pdf/2511.19656), [HTML](https://arxiv.org/abs/2511.19656)
### Authors
Kaiyi Ji
### Background
尽管针对双层优化的上界保证已得到了广泛的研究，但在低界方面的进展有限，原因在于其复杂的双层结构。本文重点关注平滑的非凸-强凸设置，并建立新的困难实例，以非确定性和随机一阶预言模型形式在寻找ε精确的平稳点时提供非平凡的下界。在确定性情形下，证明了一切实数零策略需要至少Ω(κ^(3/2)ε^(-2))次预言调用，以找到一个ε准确的稳定点，改进了单层非凸优化和非凸-强凸最小-最大化问题已知的最佳下界。在随机情形下，展示了至少Ω(κ^(5/2)ε^(-4))次随机预言调用是必要的，进一步加强了相关环境中已知的最佳下界。
### Innovation
在非凸-强凸设置下研究双层优化，并建立了新的困难实例，以非确定性和随机一阶预言模型形式推动下界的研究，改进了单层非凸优化和非凸-强凸最小-最大化问题已知的最佳下界。
### Conclusion
当前对于双层优化的上下界之间存在显著差距，即使在诸如二次下层目标这样简化的情形下，也需要进一步研究以理解标准一阶预言下的最佳复杂性。
## 768. `cs.LG` - 多种正确方法：基于概念的神经网络的拉什阿蒙集 [PDF](https://arxiv.org/pdf/2511.19636), [HTML](https://arxiv.org/abs/2511.19636)
### Authors
Shihan Feng,Cheng Zhang,Michael Xi,Ethan Hsu,Lesia Semenova,Chudi Zhong
### Background
现代神经网络在许多任务上不只有一种正确的方法。多个模型可以实现相同的性能，但依赖于不同的特征或推理模式。这一现象被称为拉什阿蒙效应。然而，深入架构的连续参数空间中包含了大量数值上不同的但行为上相似的近似最优解，这使得发现这些多样性具有挑战性。
### Innovation
作者提出了一种名为Rashomon Concept Bottleneck Models（RCB）的框架，该框架学习多个都能准确推理但却通过不同的可理解概念进行推理的神经网络。通过结合轻量级适配器模块和多样性正则化训练目标，这种方法能够在不完全从头开始训练的情况下高效地构建一系列基于概念的模型。结果生成了相同的预测但不同的推理过程的网络，揭示了同等性能解决方案中概念依赖和决策过程的变化。
### Conclusion
该框架使研究人员能够系统地探索深度模型中的数据驱动推理多样性，提供了一种新的机制来审计、比较和对齐相同的准确解决方案。
## 769. `cs.LG` - TiCT: 一种基于合成训练的基础模型用于时间序列分类 [PDF](https://arxiv.org/pdf/2511.19694), [HTML](https://arxiv.org/abs/2511.19694)
### Authors
Chin-Chia Michael Yeh,Uday Singh Saini,Junpeng Wang,Xin Dai,Xiran Fan,Jiarui Sun,Yujie Fan,Yan Zheng
### Background
时间序列数据的普遍存在对通用基础模型产生了强烈需求，尤其是在分类任务上。然而，开发这类模型面临高昂的标注数据成本。能进行上下文学习的（ICL）基础模型能够通过少量示例调整到新任务，并减少重新训练的需要。尽管如此，大规模时间序列模型的研究大多集中在预测上，而非分类任务，这形成了一个关键缺口。
### Innovation
论文提出了一种名为TiCT的时间序列上下文转换器模型，它使用合成数据进行预训练，以实现即插即用的分类。TiCT的两项主要技术贡献是：一个可扩展的基于位的标签编码架构和一种特殊输出注意力机制，能够处理任意数量的类别；以及一种结合了Mixup启发的数据增强与合成预训练框架，增强了泛化能力和噪声不变性。
### Conclusion
通过在UCR存档上的广泛评估，TiCT在即插即用场景下达到了与最先进的监督学习方法相当的性能。更重要的是，这种性能是通过仅利用即插即用示例在推理阶段实现的，无需更新任何模型权重。
## 770. `cs.LG` - TREASURE: 基于Transformer的高流量交易理解基础模型 [PDF](https://arxiv.org/pdf/2511.19693), [HTML](https://arxiv.org/abs/2511.19693)
### Authors
Chin-Chia Michael Yeh,Uday Singh Saini,Xin Dai,Xiran Fan,Shubham Jain,Yujie Fan,Jiarui Sun,Junpeng Wang,Menghai Pan,Yingtong Dou,Yuzhong Chen,Vineeth Rakesh,Liang Wang,Yan Zheng,Mahashweta Das
### Background
支付网络构成了现代商业的基础，每天生成大量的交易记录。准确地建模这些数据可以用于异常行为检测和消费者级别的洞察，从而改善人们的生活。本文提出了TREASURE，一种基于Transformer的多功能基础模型，专门设计用于交易数据。
### Innovation
1. 一个输入模块，包含专为静态和动态属性设计的子模块，提高训练和推理效率；2. 有效且高效的训练框架，用于预测高基数类目属性；3. 作为独立模型，TREASURE的异常行为检测性能相较于生产系统提高了111%；作为嵌入提供者，它提高了推荐模型的表现104%。
### Conclusion
通过广泛的消融研究、与生产模型的基准测试和案例研究，本文展示了TREASURE的关键见解，突显了开发TREASURE过程中获得的价值知识。
## 771. `cs.LG` - 增强时间序列预测的结构化噪声建模 [PDF](https://arxiv.org/pdf/2511.19657), [HTML](https://arxiv.org/abs/2511.19657)
### Authors
Sepideh Koohfar
### Background
时间序列预测在现实世界中依然充满挑战，因为时间模式在多个尺度上运作，从宽泛的上下文趋势到快速的、细粒度的波动等，后者对关键决策至关重要。现有神经模型难以捕捉这些动态的相互作用，导致预测不稳定并影响下游应用的可靠性。
### Innovation
本文提出了一种预测模糊化去噪框架，通过结构化噪声建模提高时间序列的准确性。该方法引入了一个可学习的高斯过程模块，生成平滑且相关的扰动，促使预测主体捕捉远距离结构。同时，专门的精炼模块恢复高分辨率的时间细节。联合训练各组件促进了自然的专业分工，规避了各向同性腐蚀方法所产生的常见伪影。实验结果表明，在电力、交通和太阳能数据集上，该框架在多时间尺度准确性与稳定性方面均有显著提升。模块化设计也使得模糊去噪层能够作为轻量级增强应用于预训练模型，支持有限数据条件下的高效适应。
### Conclusion
通过增强细粒度时间预测的可靠性和可解释性，该框架推动了在能源、基础设施及其他时间紧急领域中更具信赖度的人工智能系统的发展，为基于预测的决策支持提供了更稳固的基础。
## 772. `cs.LG` - DISCO:基于浏览器的隐私保护分布式协作学习框架 [PDF](https://arxiv.org/pdf/2511.19750), [HTML](https://arxiv.org/abs/2511.19750)
### Authors
Julien T. T. Vignoud,Valérian Rousset,Hugo El Guedj,Ignacio Aleman,Walid Bennaceur,Batuhan Faik Derinbay,Eduard Ďurech,Damien Gengler,Lucas Giordano,Felix Grimberg,Franziska Lippoldt,Christina Kopidaki,Jiafan Liu,Lauris Lopata,Nathan Maire,Paul Mansat,Martin Milenkoski,Emmanuel Omont,Güneş Özgün,Mina Petrović,Francesco Posa,Morgan Ridel,Giorgio Savini,Marcel Torne,Lucas Trognon,Alyssa Unell,Olena Zavertiaieva,Sai Praneeth Karimireddy,Tahseen Rabbani,Mary-Anne Hartley,Martin Jaggi
### Background
数据因隐私、知识产权和法律约束等问题而难以共享，这不仅削弱了预测模型的统计能力，还造成了访问偏见，使得那些有能力克服这些担忧的人能获得更高的准确性。
### Innovation
提出了DISCO：一个开源的分布式协作学习平台，适用于非技术人员，提供了一种无需共享原始数据或编程知识即可共同构建机器学习模型的方法。DISCO的网页应用可以直接在浏览器中本地训练模型，支持跨平台使用，包括智能手机。平台的设计模块化，提供联邦和去中心化两种范式选择，不同层次的隐私保障以及多种权重聚合策略，允许模型个性化和抗偏见。
### Conclusion
DISCO的代码库可在该链接处访问，网页界面展示可在该链接处查看。
## 773. `cs.LG` - CafeQ: 无校准量化通过学习变换和自适应舍入实现 [PDF](https://arxiv.org/pdf/2511.19705), [HTML](https://arxiv.org/abs/2511.19705)
### Authors
Ziteng Sun,Adrian Benton,Samuel Kushnir,Asher Trockman,Vikas Singh,Suhas Diggavi,Ananda Theertha Suresh
### Background
后培训量化是在大语言模型部署中减少成本的有效方法，标准做法是使用最接近舍入量化级别方案。然而，这种方法往往会因为权重中的误差而引入大量错误。为了缓解这一问题，现有的缓解机制包括使用自适应舍入、随机旋转变换或使用校准数据确定后培训目标。但是，依赖校准数据在一些实际场景中可能是有限制的，因为这些数据可能不可用或受到隐私法规的约束。
### Innovation
本文提出了在不使用任何校准数据的情况下优化变换和自适应舍入的算法。通过设计一个合适的代理函数来估算量化损失，实现了优化效果。在保持推理效率的同时，使用结构化矩阵变换单个矩阵，并且对于直接在计算图中交互的配对权重使用双重矩阵变换和自适应舍入方法。实验结果表明这种方法在Gemma 2模型上取得了稳定的改善，尤其是4位和3位量化效果显著。相比其他方法，此方法引入的计算开销不到3%，且性能与常用GPTQ方法相当，后者需要使用校准数据。
### Conclusion
在没有校准数据的情况下，该方法能够提高大型语言模型的后培训量化精度，同时保持高效和可比性能。这种方法可以减少对敏感数据的需求，则更适合广泛部署中的实际应用。
## 774. `cs.LG` - 材料科学中基于大规模语言模型的无需训练的主动学习框架 [PDF](https://arxiv.org/pdf/2511.19730), [HTML](https://arxiv.org/abs/2511.19730)
### Authors
Hongchen Wang,Rafael Espinosa Castañeda,Jay R. Werber,Yao Fehlis,Edward Kim,Jason Hattrick-Simpers
### Background
传统机器学习模型在主动学习中的应用存在冷启动限制和领域特定特征工程，限制了它们的泛化能力。大规模语言模型通过利用它们的预训练知识和通用标记表示，直接从文本描述中提出实验，为主动学习提供了一个新的范式。
### Innovation
提出了一个基于大规模语言模型的主动学习框架（LLM-AL）。框架基于迭代的少样本设置，探索了两种提示策略，并在四个材料科学数据集中与传统机器学习模型进行了基准测试。LLM-AL能够显著减少达到顶级候选实验所需的实验数量，并在所有数据集中均显示出优于传统机器学习模型的表现。
### Conclusion
LLM-AL在无训练条件下，能够提供更广泛的探索性搜索，并在较少迭代中达到最优解。尽管大规模语言模型固有的不确定性能带来性能波动，但LLM-AL的表现仍然在多次运行中保持稳定，最终展示了其作为传统主动学习流水线的通用替代方案的潜力，有助于更高效和可解释的实验选择，甚至可能实现基于大规模语言模型驱动的自主发现。
## 775. `cs.LG` - 终端速度匹配 [PDF](https://arxiv.org/pdf/2511.19797), [HTML](https://arxiv.org/abs/2511.19797)
### Authors
Linqi Zhou,Mathias Parger,Ayaan Haque,Jiaming Song
### Background
本文提出了终端速度匹配（TVM），这是一种流匹配的一般形式，允许进行高保真的一步或多步骤生成建模。TVM能够表征任何两个扩散时间步之间的过渡，并在其终端时间而不是初始时间处对其行为进行正则化。
### Innovation
1. 提出了一种新的方法，终端速度匹配（TVM），能够实现高保真度的一维或多步生成建模。2. TVM通过在其终端时间而非初始时间处正则化其行为，解决了扩散模型（如扩散变换器）缺乏Lipschitz连续性的问题，引入了最少的架构更改，实现了稳定的一阶段训练。3. 为提高TVM的效率，开发了一个整合的注意力内核，支持雅可比向量积的反向传递，这与变压器架构兼容性良好。
### Conclusion
在ImageNet-256x256上，TVM使用一个函数评估实现了3.29的FID，使用四个函数评估实现了1.99的FID。同样，在ImageNet-512x512上，TVM实现了2.94的四步评估FID，代表了一步/多步从零开始模型的最新性能。
## 776. `cs.LG` - 仅前向测试时推理的可扩展数据归因 [PDF](https://arxiv.org/pdf/2511.19803), [HTML](https://arxiv.org/abs/2511.19803)
### Authors
Sibo Ma,Julian Nyarko
### Background
数据归因旨在追踪模型行为到构成它的训练示例，从而在大规模情境下实现模型的调试、审核和数据价值评估。经典的方法，如影响函数方法，虽然提供了原则性的基础，但在现代网络中仍不具备可实用性，因为它们需要昂贵的反向传播或海森矩阵求逆计算。现有方法在推理时需要进行反向传播，这在现代复杂的网络中变得不切实际。
### Innovation
我们提出了一种数据归因方法，它保留了相同的一阶反事实目标，同时消除了每次查询的反向传递。该方法通过训练期间的短时间跨度梯度传播模拟每个训练示例的参数影响，并在后来只需使用前向评估即可读取归因信息。该设计将计算任务从推理转移到仿真，反映了实际情况，即模型可能为数十亿用户提供服务，但起源于固定的有限数据源（例如，一个大型语言模型在训练过程中使用多样化的语料库，同时补偿具体的出版商如纽约时报）。实验结果显示，在标准的MLP基准测试中，我们的估计器在标准归因度量（LOO和LDS）上匹配或超越了现有的顶级基线，同时提供了数量级更低的推理成本。
### Conclusion
通过结合影响函数的真实性和一阶可扩展性，该方法为大型预训练模型提供了实用的、实时的数据归因理论框架。我们的方法在理论和实践中都展示了优越性，特别是在大规模预训练模型中的应用前景。
## 777. `cs.LG` - 揭示扩散目标：重加权损失是更好的变分界线 [PDF](https://arxiv.org/pdf/2511.19664), [HTML](https://arxiv.org/abs/2511.19664)
### Authors
Jiaxin Shi,Michalis K. Titsias
### Background
本文提出了一种新的理论解释扩散模型中广泛使用的加权损失。通过构建时间相关的变分下界，该方法在标准证据下界的基础上改进，减少了数据模型的KL散度，适用于包括连续高斯扩散模型和掩码（离散）扩散模型在内的各种生成扩散模型训练。
### Innovation
提出了一种新的基于时间依赖变分下界的理论解释，该方法通过构建连续时间变分下界，改善了标准证据下界，推出了减少数据模型KL散度的重加权目标函数。这些目标函数可以应用于任何生成扩散模型。并通过掩码扩散模型展示了该框架，并在像素空间图像建模中取得了显著的改进，接近于连续扩散模型的样本质量。同时，所得结果也提供了一种理论依据，解释了在掩码图像模型中广泛使用的简单加权方案。
### Conclusion
研究成果表明，重加权损失是更好的变分界线，能够提高扩散模型的训练效果，特别是对于图像建模领域。
## 778. `cs.LG` - Mosaic Pruning: 一种用于混合专家模型泛化裁剪的分层框架 [PDF](https://arxiv.org/pdf/2511.19822), [HTML](https://arxiv.org/abs/2511.19822)
### Authors
Wentao Hu,Mingkuan Zhao,Shuangyong Song,Xiaoyan Zhu,Xin Lai,Jiayin Wang
### Background
稀疏混合专家(SMoE)架构通过在推理过程中仅激活一小部分参数，解决了大规模语言模型（LLMs）的扩展问题，提高了性能。然而，这种架构的实际部署受到静态内存占用过大的阻碍，因为所有专家都必须加载到内存中。现有的训练后剪枝方法虽然减少了模型的大小，但其剪枝标准通常来自于单一的一般用途语料库，这导致模型在应用于其他领域时出现性能急剧下降的问题，需要针对每个新领域进行昂贵的重新剪枝。
### Innovation
我们提出了Mosaic Pruning（MoP），这是一种分层的框架，通过一种结构化的‘聚类-选择’过程构建功能完备的专家集。该过程利用了度量专家在不同任务领域性能的相似性度量进行功能聚类，并根据我们提出的激活变化得分选择各个簇中最具代表性的专家。与优化单一语料库的方法不同，MoP 确保了剪枝后的模型保留了一个功能上互补的专家集，这类似于马赛克中的瓷砖如何共同呈现原模型能力的全面图象，从而能够处理多样化的下游任务。
### Conclusion
我们在各种MoE模型上的实验表明了我们方法的优越性。Mosaic Pruning显著优于先前的工作，在通用任务中取得了7.24%的性能提升，在数学推理和代码生成等专门任务中则取得了8.92%的提升。
## 779. `cs.LG` - 学习净化：噪声标签矫正的强化学习 [PDF](https://arxiv.org/pdf/2511.19808), [HTML](https://arxiv.org/abs/2511.19808)
### Authors
Marzi Heidari,Hanping Zhang,Yuhong Guo
### Background
在机器学习中，使用噪声标签的学习挑战是显著的。如果不妥善解决，噪声标签会严重降低预测模型的性能。
### Innovation
本文提出了一种新颖的框架，将噪声标签矫正概念化为强化学习（RL）问题。该方法通过演员-评论家方法利用强化学习学习一个深度特征表示策略网络来进行标签矫正，并通过迭代修正噪声训练标签来促进预测模型的训练。
### Conclusion
实验证实在多个基准数据集上，RLNLC持续优于现有的处理噪声标签的最先进的技术。
## 780. `cs.LG` - When +1% Is Not Enough: A Paired Bootstrap Protocol for Evaluating Small Improvements [PDF](https://arxiv.org/pdf/2511.19794), [HTML](https://arxiv.org/abs/2511.19794)
### Authors
Wenzhang Du
### Background
近年来的机器学习论文经常报告在基准测试上单次运行中1-2个百分点的改进。这些改进高度依赖于随机种子、数据排序和实现细节，但很少伴随不确定性估计或显著性检验。因此，难以判断报告的1-2个百分点的改进是否反映真实的算法进步还是噪声。
### Innovation
在实际的计算预算下（仅允许少量运行），论文提出了一种基于成对的多种子运行、偏置校正加速（BCa）Bootstrap置信区间和基于种子差异的符号翻转排列检验的简单评估协议。该协议旨在为过度主张划设安全线。
### Conclusion
论文实例化该协议于CIFAR-10、CIFAR-10N和AG News数据集，使用合成的无改进、小增幅和中等增幅场景。即使在单个运行和不成对t检验中经常看似有显著改进（0.6-2.0个百分点），只有三个种子时，成对协议从未在此情况下宣布有显著改进。作者认为，这种保守的评估是紧预算下小改进的更安全默认策略。
## 781. `cs.LG` - 证明可以抵抗异常值的半参数回归方法在低成本空气质量传感器可转移校准中的应用 [PDF](https://arxiv.org/pdf/2511.19810), [HTML](https://arxiv.org/abs/2511.19810)
### Authors
Divyansh Chaurasia,Manoj Daram,Roshan Kumar,Nihal Thukarama Rao,Vipul Sangode,Pranjal Srivastava,Avnish Tripathi,Shoubhik Chakraborty,Akanksha,Ambasht Kumar,Davender Sethi,Sachchida Nand Tripathi,Purushottam Kar
### Background
低成本空气质量（LCAQ）传感器在构建密集的空气质量监测网络中发挥了关键作用，但将这些传感器与标准化的监测设施进行校准的成本高昂、耗时且复杂，特别是在需要在地理上分散的区域部署大量传感器时。本文通过案例研究介绍了在印度大规模多站点、多季节、多传感器、多污染物移动空气质量监测网络中，如何利用RESPIRE技术校准LCAQ传感器以检测环境中的CO（一氧化碳）浓度。
### Innovation
RESPIRE技术相比文献中常见的基线校准方法具有特定优势，特别是在多站点、多季节和多传感器的环境中提高了预测能力。RESPIRE使用一种可证明能抵抗异常值的训练算法，并具有可解释性，能够标记模型过拟合的实例。该技术已经在四个站点、两个季节和六款传感器包的数据收集期间的广泛部署中得到了实证结果的验证。
### Conclusion
RESPIRE技术为低成本空气质量传感器的校准提供了一个灵活且强大的解决方案，具有抵抗异常值的能力，能够跨站点、跨季节和跨传感器进行可转移校准，同时还具备解释能力并能检测模型过拟合的现象。RESPIRE代码可以在提供的链接中获得。
## 782. `cs.LG` - Cisco 时间序列模型技术报告 [PDF](https://arxiv.org/pdf/2511.19841), [HTML](https://arxiv.org/abs/2511.19841)
### Authors
Liang Gou,Archit Khare,Praneet Pabolu,Prachi Patel,Joseph Ross,Hercy Shen,Yuhan(Ellen)Song,Jingze Sun,Kristal Curtis,Vedant Dharnidharka,Abhinav Mathur,Hao Yang
### Background
该文介绍了一种新的时间序列预测模型——Cisco Time Series Model。该模型基于流行的解码器-only 时间序列模型 TimesFM，通过一般性的架构创新实现了多分辨率输入，使其能够接受不同粒度的数据输入。
### Innovation
创新点在于提出了一种新的时间序列架构设计，能够处理多分辨率的输入数据。这使得模型能够从具有不同粒度的数据集中进行学习，并且在保持标准通用预测基准GIFT-Eval 上与原有模型表现相似的情况下，在观察性数据集上取得了更优的性能。
### Conclusion
该研究通过构建多分辨率的解码器-only 模型，并利用超过300亿个独特数据点进行训练，最终展示了该模型在观察性数据集上的优异表现，并且能够更准确地对长上下文输入进行预测。
## 783. `cs.LG` - 适配性和普遍性：在线凸优化中的问题自适应普遍 regrets [PDF](https://arxiv.org/pdf/2511.19937), [HTML](https://arxiv.org/abs/2511.19937)
### Authors
Peng Zhao,Yu-Hu Yan,Hang Yu,Zhi-Hua Zhou
### Background
现有的在线学习方法为普遍在线学习提供了最优的后悔保证，但仍然缺乏问题自适应能力。具体而言，现有的方法不能调整到梯度变异量$V_T$的后悔量度。本文背景在于提升这种方法的自适应性，使其能在不同类型的函数中表现更优。
### Innovation
本文引入了UniGrad，这是一种同时实现了普遍性和自适应性的新型方法。UniGrad有两种具体实现，对于强凸函数实现了$text{O}(text{log } V_T)$的后悔量度，对于exp-凸函数实现了$text{O}(d text{ log } V_T)$的后悔量度。此外，UniGrad++还通过代理优化技术将每次轮次的梯度查询次数从$text{O}(text{log } T)$减少到了仅为1次。
### Conclusion
文章提出了两种新的线上学习方法UniGrad和UniGrad++，实现了对梯度变异量的自适应后悔量度，提升了在平凡和非平凡函数下的表现，并通过代理优化技术提高了计算效率。这种方法弥补了现有算法的不足，展现了其在泛化和自适应方面的优势。
## 784. `cs.LG` - 通过混合分割和联邦学习优化加速无线分布式学习 [PDF](https://arxiv.org/pdf/2511.19851), [HTML](https://arxiv.org/abs/2511.19851)
### Authors
Kun Guo,Xuefei Li,Xijun Wang,Howard H. Yang,Wei Feng,Tony Q. S. Quek
### Background
联邦学习（FL）和分割学习（SL）是无线网络中两个有效的分布式学习范式，能够在不共享原始数据的情况下，通过移动设备协作进行模型训练。FL支持低延迟并行训练，但可能收敛到不那么准确的模型；而SL通过序贯训练实现更高的准确度，但会增加延迟。为了结合这两种方法的优点，提出了混合分割和联邦学习（HSFL），让一些设备在FL模式下运行，其他设备在SL模式下运行。
### Innovation
本文通过对学习模式选择、学习模式与批量大小的互动以及如何在通信和计算资源下优化这些超参数以减少整体学习延迟进行分析。首先分析了收敛性，并揭示了学习模式和批量大小之间的相互作用。然后提出了一个延迟最小化问题的解决方案，包括一个松弛问题的块坐标下降方法和一个恢复整数批量大小的近最优性能的舍入算法。
### Conclusion
实验结果表明，我们的方法能够显著加速相对于现有方法到目标准确性的收敛速度。
## 785. `cs.LG` - 基于GED一致解缠对齐和非对齐子结构进行图相似性学习 [PDF](https://arxiv.org/pdf/2511.19837), [HTML](https://arxiv.org/abs/2511.19837)
### Authors
Zhentao Zhan,Xiaoliang Xu,Jingjing Wang,Junmei Wang
### Background
图相似性计算（GSC）是一个基本的图相关任务，其中图编辑距离（GED）是一个常用的度量标准。GED取决于一对图之间最优对齐，将每个图分割为对齐（零成本）和未对齐（带成本）的亚结构。由于精确GED计算的NP难性质，基于图神经网络（GNN）的GED近似方法已经出现。现有基于GNN的GED方法通常为每个图学习节点嵌入，然后将成对节点相似性聚集以估算最终的相似度。尽管这些方法很有效，但作者发现，这种方法中的节点中心匹配范式与GED的核心原则之间存在不匹配。这种不匹配导致两个关键限制：无法捕捉全局结构对应以实现最优对齐以及由虚假节点信号驱动的编辑成本误归因。
### Innovation
我们提出了GCGSim，一种基于图级匹配和亚结构级编辑成本的GED一致的图相似性学习框架。具体来说，我们做出了三项核心技术贡献。广泛的实验表明，GCGSim在四个基准数据集上达到了最先进的性能。全面的分析进一步证明，该框架能够学习到分离的、语义意义上的亚结构表示。
### Conclusion
GCGSim框架有效地学习了分离的和语义上有意义的亚结构表示，解决了基于GNN的GED方法中存在的两方面重要限制。
## 786. `cs.LG` - Frailty-Aware Transformer for Recurrent Survival Modeling of Driver Retention in Ride-Hailing Platforms [PDF](https://arxiv.org/pdf/2511.19893), [HTML](https://arxiv.org/abs/2511.19893)
### Authors
Shuoyan Xu,Yu Zhang,Eric J. Miller
### Background
网约车平台具有高频次、基于行为的环境特点。尽管生存分析已经应用于其他领域中的重复事件，但在网约车司机行为建模中的应用尚未得到充分探索。本研究利用大规模平台数据将空驶行为视为重复的生存过程，并提出了一种基于Transformer的框架，该框架通过因果掩码捕捉长时间依赖性，并结合司机特定嵌入模型以表征潜在异质性。
### Innovation
研究采用了一种对司机留存的Frailty-Aware Cox Transformer (FACT) 模型。该模型利用了因果掩码来捕捉长时间依赖性，同时结合了司机特定嵌入以表征潜在异质性。实验证明，Frailty-Aware Cox Transformer (FACT) 在多伦多网约车数据上的时间依赖C-指标和Brier分数最低，优于经典和深度学习生存模型，从而实现了更准确的风险估计，并支持平台的留存策略、提供政策相关的见解。
### Conclusion
研究结果表明，Frailty-Aware Cox Transformer 模型在网约车司机留存预测方面表现出优越性能，有助于风险精确估计和平台留存策略优化，并且提供了具有政策意义的洞察。
## 787. `cs.LG` - EfficientXpert：通过传播感知剪枝实现大型语言模型的高效领域适应 [PDF](https://arxiv.org/pdf/2511.19935), [HTML](https://arxiv.org/abs/2511.19935)
### Authors
Songlin Zhao,Michael Pitts,Zhuwei Qin
### Background
大型语言模型（LLMs）的快速发展提高了在法律、医疗和金融等领域需要领域特定变体的需求。然而，庞大的模型大小成为在资源受限环境中部署的障碍。目前的压缩方法要么在不同领域间推广性差，要么引入了高昂的计算成本。
### Innovation
本文提出了一种轻量级的领域精简框架EfficientXpert，该框架结合了传播感知修剪标准（Foresight Mask）和高效适配器更新算法（Partial Brain Surgeon）。将EfficientXpert集成到LoRA微调过程中，能够将通用预训练模型一键转化为稀疏的领域适应专家。在医疗和法律任务中，EfficientXpert在40%的稀疏度下保留了近98%的稠密模型性能，优于现有方法。此外，分析表明，通用剪枝掩码在各个领域中的结构性变化会降低其效果，从而突显了适应性和领域感知剪枝策略的必要性。
### Conclusion
通过将传播感知修剪标准和高效适配器更新算法集成到LoRA微调过程中，EfficientXpert能够在保证高性能的同时实现大型语言模型的高效领域适应，适用于资源受限的环境。同时，研究强调了需要为每个领域定制适应性剪枝策略的必要性。
## 788. `cs.LG` - 使用强化学习优化MR指纹的翻转角度调度 [PDF](https://arxiv.org/pdf/2511.19941), [HTML](https://arxiv.org/abs/2511.19941)
### Authors
Shenjun Zhong,Zhifeng Chen,Zhaolin Chen
### Background
磁共振指纹学（MRF）依赖于可调采集参数产生的瞬态信号动力学，这使得设计最优、稳定的序列成为一个复杂的、高维度的顺序决策问题，例如优化最关键参数之一的翻转角度。强化学习（RL）提供了一种有前景的方法来自动化参数选择，以优化最大限度提高指纹在参数空间中可分辨性的脉冲序列。
### Innovation
本文介绍了一个基于强化学习的框架，用于优化MRF中的翻转角度计划，并展示了学习出的非周期性模式，提高了指纹的可分辨性。此外，还观察到，通过优化的调度可以减少重复时间，从而可能加快MRF的采集流程。
### Conclusion
所提出的RL优化翻转角度计划具备非周期性模式，提高了指纹的可分辨性，并有可能减少重复时间，从而加速MRF采集过程。
## 789. `cs.LG` - SX-GeoTree: 自解释地理回归树，融合特征归因的空间相似性 [PDF](https://arxiv.org/pdf/2511.19845), [HTML](https://arxiv.org/abs/2511.19845)
### Authors
Chaogui Kang,Lijian Luo,Qingfeng Guan,Yu Liu
### Background
决策树在表格预测中仍然非常重要，但它们在捕捉空间依赖性和生成局部稳定（鲁棒）解释方面存在困难。
### Innovation
SX-GeoTree 引入了三个耦合目标，这三个目标在递归分割过程中被整合：减少杂质（MSE），控制空间残差（全局Moran's I），以及通过共识相似网络（包括地理加权回归系数距离和SHAP归因距离）上的模块化最大化来提高解释稳定性，将局部Lipschitz连续性重新定义为网络社区保征问题，从而在不需要逐样本邻域搜索的情况下实现空间上一致的解释的可扩展性。此外，此框架展示了如何将空间相似性——通过GWR推导出的当地关系——嵌入到可解释模型中，从而推进可信的地理空间机器学习。
### Conclusion
实验表明，SX-GeoTree 在保持与决策树相当的预测精度的同时，提高了残差空间均匀性和解释一致性（解释模块化度在福建地区约为两倍，在西雅图地区约为一倍）。消除Moran's I或模块化项都会降低空间残差结构和解释稳定性。该方法证明了通过扩展几何临近性的空间相似性可以在具有解释性的模型中嵌入的方法，推动了可信的地理空间机器学习，并为领域意识解释提供了可转移的模板。
## 790. `cs.LG` - 提示公平性：LLMs中子群体差异 [PDF](https://arxiv.org/pdf/2511.19956), [HTML](https://arxiv.org/abs/2511.19956)
### Authors
Meiyu Zhong,Noel Teku,Ravi Tandon
### Background
大型语言模型（LLMs）在许多应用中展现出了有效性，但在回应质量上却存在显著差异。研究发现，相同的询问由于不同的用户或者问法，可能从LLMs那里得到不同的回应。为了量化这种差异，本文采用信息论度量标准来捕获偏差的两个维度：子群体的内部变异性和跨群体的一致性。
### Innovation
本文提出利用信息论度量标准来量化LAP（Prompt Advocacy）公正性中的偏差，具体包括子群体内部的变异性和跨群体的一致性。研究揭示某些子群体不仅内部变异大，而且与其他群体之间的差异也更大，表明模型行为中存在结构性的不平等。为了缓解这些不平等，本文提出了一些实际干预措施，包括多代的多数投票和提示中立化，这些措施改善了响应的稳定性并增强了模型的公平性。
### Conclusion
实验结果显示，跨群体差异值在干预前达到了0.28，通常在0.14到0.22之间。在应用了中立化和多代策略之后，这些差异普遍减少，最大的差距被缩小到0.22，许多距离为0.17或以下，表明全局更稳定和一致的输出。
## 791. `cs.LG` - Stragglers Can Contribute More: Uncertainty-Aware Distillation for Asynchronous Federated Learning [PDF](https://arxiv.org/pdf/2511.19966), [HTML](https://arxiv.org/abs/2511.19966)
### Authors
Yujia Wang,Fenglong Ma,Jinghui Chen
### Background
异步联邦学习（FL）因其增强的效率和可扩展性而受到关注，允许本地客户端在自己的速度下发送模型更新而无需等待速度较慢的参与者。但是，这种设计面临显著挑战，如慢速参与者的过时更新会降低总体模型性能，以及速度快的参与者可能会主导学习过程，特别是在异质数据分布下可能会引入偏差。现有方法通常仅解决这些问题之一，导致缓解过时更新影响的同时会加剧快速客户引起的偏差，反之亦然。
### Innovation
提出了FedEcho框架，这是一种全新的方法，结合了不确定性感知蒸馏（uncertainty-aware distillation），以在大规模异步延迟和数据异质性下增强异步FL性能。不确定性感知蒸馏使服务器能够评估由慢速客户端生成的预测的可靠性，并根据其估计的不确定性动态调整这些预测的影响。通过优先考虑更确定的预测并充分利用所有客户端提供的多样信息，FedEcho有效地减少了过时更新和数据异质性带来的负面影响。
### Conclusion
通过广泛的实验，我们证明FedEcho在不访问私人客户端数据的情况下，持续优于现有的异步FL基线，实现了稳健的性能。
## 792. `cs.LG` - 基于扩散距离引导应力最大化重塑消息传递神经网络 [PDF](https://arxiv.org/pdf/2511.19984), [HTML](https://arxiv.org/abs/2511.19984)
### Authors
Haoran Zheng,Renchi Yang,Yubo Zhou,Jianliang Xu
### Background
近年来，消息传递神经网络（MPNNs）已成为用于图结构数据学习的首选模型。尽管这些模型非常有效，但由于最小化狄利克雷能量及其衍生的邻域聚合操作，它们仍然存在严重的过度平滑和相关性问题。
### Innovation
本文提出了一种新的MPNN模型DDSM，基于包含应力最大化和正交正则化的优化框架，以克服这些问题。此外，DDSM引入了节点扩散距离作为框架的一部分，引导新的消息传递操作，并开发了距离近似算法，这些算法通过严格的理论分析支持。
### Conclusion
全面的实验表明，DDSM在同质性和异质性图上均显著且一致地优于15种强劲的基线模型。
## 793. `cs.LG` - ParaBlock：用于大型语言模型的并行通信计算块坐标联邦学习 [PDF](https://arxiv.org/pdf/2511.19959), [HTML](https://arxiv.org/abs/2511.19959)
### Authors
Yujia Wang,Yuanpu Cao,Jinghui Chen
### Background
联邦学习(Federated Learning, FL)作为一种隐私保护的训练范式已被广泛研究。近年来，联邦块坐标下降方案因其使客户端只需本地训练模型的一部分而非全部而成为训练大规模模型的一种受欢迎的选择。然而，在大型语言模型(Large Language Models, LLMs)时代，即使是一个块包含了大量的参数，也会导致显著的通信延迟，尤其是对于资源受限的客户端而言。
### Innovation
为了解决联邦训练/微调LLMs中的这一挑战，作者提出了ParaBlock，这是一种新颖的方法，通过并行建立两个通信和计算线程来提高通信效率。理论证明了ParaBlock的收敛率与标准的联邦块坐标下降方法相同。实证评估进一步证实，ParaBlock不仅保持了强大的性能，还显著提高了通信效率。
### Conclusion
ParaBlock通过同时优化通信和计算策略，有效地提高了联邦学习中LLMs的通信效率。
## 794. `cs.LG` - Differential Smoothing Mitigates Sharpening and Improves LLM Reasoning [PDF](https://arxiv.org/pdf/2511.19942), [HTML](https://arxiv.org/abs/2511.19942)
### Authors
Jingchu Gai,Guanning Zeng,Huaqing Zhang,Aditi Raghunathan
### Background
强化学习（RL）微调大型语言模型通常会导致多样性的崩溃，即输出缺乏多样性。现有方法虽然提出了一些对策，但这些方法往往是经验性的，经常在正确性和多样性之间进行权衡，有效性也不一致，甚至有时彼此矛盾。
### Innovation
本文提供了一个严格的理论基础来解释RL微调为何会引发多样性的崩溃，并通过选择和强化偏见的正式证明来阐明原因。提出了“差分平滑”方法，这是一种原则性的方法，可以同时提高正确性和多样性，超越了传统的RL方法和普遍使用的基于熵的经验方法。该理论精确描述了现有经验方法何时是有帮助的，为什么有时会失败，而且表明差异平滑方法是无条件优越的。
### Conclusion
广泛的实验表明，无论是参数从1B到7B，还是涵盖领域如CountDown和实际的数学推理，差分平滑都能带来一致的收益。它不仅提高了Pass@1，还提高了Pass@k，AIME24数据集上的改进幅度高达6.7%。
## 795. `cs.LG` - 机器精度下的算子学习 [PDF](https://arxiv.org/pdf/2511.19980), [HTML](https://arxiv.org/abs/2511.19980)
### Authors
Aras Bacho,Aleksei G. Sorokin,Xianjin Yang,Théo Bourdais,Edoardo Calvello,Matthieu Darcy,Alexander Hsu,Bamdad Hosseini,Houman Owhadi
### Background
神经算子学习方法在科学计算中受到了广泛关注，因其能够逼近无限维算子。然而，提高其复杂度往往并不能显著提升其准确性，使其与更简单的内核方法和传统降阶模型不相上下。
### Innovation
本文提出了一种称为CHONKNORIS（Cholesky Newton--Kantorovich Neural Operator Residual Iterative System）的算子学习范式，该方法可以实现机器精度。CHONKNORIS借鉴了数值分析中的思想，通过回归与Tikhonov正则化Newton--Kantorovich更新相关的椭圆算子的Cholesky因子，而不是直接回归解算子本身，从而形成了一个无需端到端逼近解算子即可达到机器精度的神经架构。
### Conclusion
研究在一系列非线性前向和反向问题上对CHONKNORIS进行了基准测试，包括非线性椭圆方程、Burgers’方程、非线性达西流动问题、Calderón问题、逆波动散射问题和地震成像问题。此外，提出了FONKNORIS（Foundation Newton--Kantorovich Neural Operator Residual Iterative System）模型，这是一种基于多个预训练CHONKNORIS专家聚合的基模型变体，能够准确解决未见过的非线性PDE问题，如Klein--Gordon方程和Sine--Gordon方程。
## 796. `cs.LG` - 重新思考无监督图聚类在半监督节点分类中的作用 [PDF](https://arxiv.org/pdf/2511.19976), [HTML](https://arxiv.org/abs/2511.19976)
### Authors
Songbo Wang,Renchi Yang,Yurui Lai,Xiaoyang Lin,Tsz Nam Chan
### Background
图神经网络（GNNs）为半监督节点分类任务提供了一种强大的工具。后续研究通过改进GNN模型中的消息传递方案或利用各种数据增强技术来缓解有限的监督。在真实图中，节点倾向于形成紧密的社群/聚类，这种结构里的线索对半监督节点分类很有帮助，但在以前的方法中并未被充分利用。
### Innovation
该论文提出了NCGC框架，该框架将无监督图聚类和半监督分类统一在一个框架中。通过统一封装图神经网络和谱图聚类的目标优化，开发了一种新的GNN模型（SOGNs）。此外，NCGC还包括一个无监督图聚类模块，利用两个非平凡的聚类目标和Sinkhorn-Knopp归一化，将预测的聚类标记转换为平衡的软伪标签，从而在分类模型和聚类模块之间建立了协同效应，实现了更好的模型能力。
### Conclusion
研究表明，NCGC框架在七种真实图上的半监督节点分类中，始终优于流行的GNN模型和最近的基准模型，即使在不同经典的GNN基础架构下也是如此。
## 797. `cs.LG` - RankOOD - 基于类排名的Out-of-Distribution检测 [PDF](https://arxiv.org/pdf/2511.19996), [HTML](https://arxiv.org/abs/2511.19996)
### Authors
Dishanika Denipitiyage,Naveen Karunanayake,Suranga Seneviratne,Sanjay Chawla
### Background
本文提出了一种基于训练模型的Plackett-Luce损失的RankOOD方法，它属于Out-of-Distribution (OOD)检测领域。传统上，OOD检测旨在识别模型未见过的数据样本。通过利用深度学习模型使用交叉熵损失进行训练时内在的类别预测排名模式，RankOOD能更精确地检测OOD样本。现有的OOD检测方法已经取得了良好的效果，但仍有改进的空间。
### Innovation
作者创新性地提出了一种新的OOD检测方法RankOOD，该方法利用Plackett-Luce损失训练模型，专注于类别的排名模式。不同于传统的单一类别概率预测，RankOOD通过两阶段训练提取类别排名，提高了对OOD样本检测的准确性。这一方法在近OOD TinyImageNet基准测试中取得了SOTA性能，降低了FPR95值4.3%。
### Conclusion
RankOOD通过利用训练模型预训练阶段输出的类别排名信息并结合Plackett-Luce损失，有效提升了OOD检测的性能。实验结果表明，该方法在TinyImageNet数据集上取得了最优性能，降低了误报率。
## 798. `cs.LG` - Hierarchical Spatio-Temporal Attention Network with Adaptive Risk-Aware Decision for Forward Collision Warning in Complex Scenarios [PDF](https://arxiv.org/pdf/2511.19952), [HTML](https://arxiv.org/abs/2511.19952)
### Authors
Haoran Hu,Junren Shi,Shuo Jiang,Kun Cheng,Xia Yang,Changhao Piao
### Background
前向碰撞预警系统对于车辆安全和自动驾驶至关重要，然而现有方法往往难以在精确的多智能体相互作用建模与实时决策适应性之间找到平衡，这导致了在边缘部署中的高计算成本和简化相互作用带来的不可靠性。
### Innovation
本文提出了一种综合前向碰撞预警框架，结合了层级时空注意力网络（HSTAN）与动态风险阈值调整算法（DTRA）。HSTAN采用解耦结构（空间上使用图注意力网络，时间上使用级联GRU结合自我注意力）实现更高效的表现，仅需12.3毫秒的推理时间（比Transformer方法快73%），并且在NGSIM数据集上将平均位移误差（ADE）降低了42.2%（比Social_LSTM更好）。此外，通过条件化分位数回归提高可靠性，产生预测区间，并通过物理导向的风险潜在函数和统计过程启发的自适应阈值机制进行及时警告。
### Conclusion
在多种场景数据集上，整个系统的性能表现优异，F1分数为0.912，低误报率为8.2%，并提供了2.8秒的预警提前量，验证了该框架在复杂环境下的优越性能和实用性。
## 799. `cs.LG` - REWA: 见证重叠理论 -- 可组合的二元相似性系统的基础 [PDF](https://arxiv.org/pdf/2511.19998), [HTML](https://arxiv.org/abs/2511.19998)
### Authors
Nikit Phadke
### Background
该论文专注于基于见证重叠结构的相似性理论，通过展示单调见证重叠如何适用于各种相似性表达形式（例如图邻域、因果关系、时间结构、拓扑特征、符号模式或嵌入式邻域），从而提供了一种通用的相似性处理方法。
### Innovation
论文提出了REWA（见证重叠理论），这是一种通用的理论框架，可以将任意形式的单调见证重叠转化为紧凑的编码表示。该理论保证了在使用能够保持前k排名的情况下，只需要O(log(|V|/δ))比特的数量。此外，该理论具有可组合性，可以适用于各种结构、时间、因果关系等变换，并能够统一和简化多种现有的相似性系统方法。
### Conclusion
REWA系统提供了一种基础性的框架，使得能够根据见证重叠来构建相似性系统，而不是使用哈希函数工程。这为设计复杂且功能多样的相似性系统提供了广阔的创作空间，使得百万级的不同相似性定义都可以继承对数编码复杂度。
## 800. `cs.LG` - 边缘设备上高效部署大型模型的按需多任务稀疏性 [PDF](https://arxiv.org/pdf/2511.19986), [HTML](https://arxiv.org/abs/2511.19986)
### Authors
Lianming Huang,Haibo Hu,Qiao Li,Nan Guan,Chun Jason Xue
### Background
在资源受限的边缘平台上部署大规模模型需要稀疏性，但单独优化每个任务的稀疏模式会忽略频繁任务切换带来的显著I/O开销。
### Innovation
提出了一种按需多任务稀疏性框架，通过最大化参数复用来减少切换成本。不同于单一的解决方案，该方法将权重分解为可复用的块级单元，并在任务之间对齐稀疏结构以最大化重叠。
### Conclusion
在实际的自动驾驶平台上，该框架展示了比现有稀疏性方法更高的切换效率，平均加快任务切换速度超过6.6倍。
## 801. `cs.LG` - 跨模态对比聚类：基于双图滤波的多模态图模型 [PDF](https://arxiv.org/pdf/2511.20030), [HTML](https://arxiv.org/abs/2511.20030)
### Authors
Haoran Zheng,Renchi Yang,Hongtao Wang,Jianliang Xu
### Background
多模态属性图形（MMAGs）是一种用于表示实体间复杂关联的表达型数据模型，这些实体包含来自多种数据模态（如文本、图像等）的属性。在这些数据上进行聚类发现了许多实际应用，例如社会社区检测、医疗数据分析等。然而，从我们的实证研究中可以看到，现有的多视图聚类解决方案严重依赖各视图之间属性间的高相关性，而忽视了大型预训练语言和视觉模型在MMAGs中输出的多模态属性的独特特征（如跨模态间的低相关性和激烈的功能噪声）。这导致聚类性能较差。
### Innovation
受上述观测结果和图形信号处理理论分析的启发，我们提出了双重图滤波（DGF）方案。该方案创新地将特征级别的去噪组件纳入节点表示学习，从而有效克服了现有多视图图聚类方法中所采用的传统图滤波器的局限性。此外，DGF 包括一个跨模态、邻域和社区的实例级对比学习策略，用于学习鲁棒且鉴别性强的节点表示。
### Conclusion
我们针对八个基准 MMAG 数据集的全面实验表明，DGF 在聚类质量方面（相对于真实标签）能够一致且显著地优于多种最先进的基准方法。
## 802. `cs.LG` - 使用梯度提升进行比特币波动率的多元预测：确定性、概率性和特征重要性视角 [PDF](https://arxiv.org/pdf/2511.20105), [HTML](https://arxiv.org/abs/2511.20105)
### Authors
Grzegorz Dudek,Mateusz Kasprzyk,Paweł Pełka
### Background
该研究探讨了轻量梯度提升机（LGBM）模型在比特币实现波动率的确定性和概率性预测中的应用。研究使用了69个预测器，包括市场、行为和宏观经济指标。通过将LGBM模型与计量经济学和机器学习基准进行比较，评估了其预测性能。在概率性预测方面，采用了两种基于分位数的方法，即直接分位数回归和残差模拟法。通过使用增益和置换特征重要性技术，识别出影响波动的主要因素。
### Innovation
研究采用了LGBM模型进行预测，同时使用了两种概率性预测方法，分别是直接分位数回归和残差模拟法。通过增益和置换特征重要性技术，确定了影响比特币波动的主要因素，如交易量、滞后波动性、投资者关注度和市值。
### Conclusion
研究结果表明，LGBM模型能够准确捕捉加密货币市场的非线性和高变异特性，并提供了对潜在波动动态的可解释见解。
## 803. `cs.LG` - SOMBRL: 可扩展的乐观模型导向强化学习 [PDF](https://arxiv.org/pdf/2511.20066), [HTML](https://arxiv.org/abs/2511.20066)
### Authors
Bhavya Sukhija,Lenart Treven,Carmelo Sferrazza,Florian Dörfler,Pieter Abbeel,Andreas Krause
### Background
研究模型导向强化学习（MBRL）中高效探索的挑战，特别是在系统动力学未知的情况下，RL智能体需要从在线交互中学习。传统的MBRL方法往往无法处理这种情况下的不确定性。
### Innovation
提出了可扩展且乐观的模型导向强化学习（SOMBRL）方法，该方法基于乐观原则。SOMBRL学习一具有不确定性感知的动力学模型，并贪婪地最大化外在奖励和智能体的本体论不确定性的加权和，这使得其能够与任何策略优化器或规划器兼容，同时在常见假设下，展示了在非线性动力学下的亚线性遗憾。
### Conclusion
SOMBRL在状态基和视觉控制环境中表现优异，并在动态RC车硬件上展示了优于现有最佳方法的结果，突显了理性探索对于MBRL的益处。
## 804. `cs.LG` - Sundial基础模型在叶面积指数零样本转移能力上的应用 [PDF](https://arxiv.org/pdf/2511.20004), [HTML](https://arxiv.org/abs/2511.20004)
### Authors
Peining Zhang,Hongchen Qin,Haochen Zhang,Ziqi Guo,Guiling Wang,Jinbo Bi
### Background
本文研究了时间序列基础模型在农业监测中的叶面积指数（LAI）零样本预测能力。利用HiQ数据集（美国，2000-2022），本文系统性地比较了统计基线、完全监督的LSTM模型和Sundial基础模型在多种评估协议下的表现。
### Innovation
研究发现，在零样本设置下，只要输入上下文窗口足够长（覆盖一个或两个完整的季节周期），Sundial可以优于完全训练的LSTM模型，首次证明了一种通用的预训练时间序列基础模型可以在遥感时间序列预测中超越专门的监督模型，而无需针对特定任务进行调整。
### Conclusion
本文结果强调了预训练时间序列基础模型在农业和环境应用中作为有效即插即用预测器的强大潜力。
## 805. `cs.LG` - iRadioDiff：基于物理知识的室内无线电图构建与定位扩散模型 [PDF](https://arxiv.org/pdf/2511.20015), [HTML](https://arxiv.org/abs/2511.20015)
### Authors
Xiucheng Wang,Tingwei Yuan,Yang Cao,Nan Cheng,Ruijin Sun,Weihua Zhuang
### Background
无线电地图（RMs）作为环境感知的电磁（EM）表示，将场景几何和材料属性连接到信号强度的空间分布，能够实现无需现场测量的定位。然而，构建室内高保真度RMs因电磁（EM）求解器的高延迟及基于学习的方法依赖稀疏测量或假设均匀材料的限制而具有挑战性。这些限制与室内环境中的异质性及多径传输丰富性不匹配。
### Innovation
本文提出了一种基于扩散的框架iRadioDiff，该框架无需采样并在室内环境中的无线电信号强度分布重建中得到了很好的效果。iRadioDiff基于接入点（AP）位置和材料反射和传输系数的物理信息进行条件处理，并融入了多径传输关键先验信息（如衍射点、强传输边界和视线轮廓），并通过条件通道和边界加权目标引导生成过程，以实现非站稳态场断点的准确建模及物理一致性的高效构造。
### Conclusion
实验表明，iRadioDiff在室内RMs构建及基于接收信号强度的室内定位上实现了最先进的性能，并且在不同布局和材料配置下具有有效的泛化能力。
## 806. `cs.LG` - 关于去中心化和联邦优化中动量局限性的研究 [PDF](https://arxiv.org/pdf/2511.20168), [HTML](https://arxiv.org/abs/2511.20168)
### Authors
Riccardo Zaccone,Sai Praneeth Karimireddy,Carlo Masone
### Background
最近的工作已经探讨了在局部方法中使用动量来增强分布式随机梯度下降（SGD）的有效性，特别是在联邦学习（FL）中，动量直观上被认为可以减轻统计异质性的影响。尽管在这一方向上取得了一些进展，但在去中心化的情境下，只有部分工人在每个轮次中参与，动量是否能保证在无界异质性下的收敛性仍然不清楚。
### Innovation
本研究分析了在循环客户端参与情况下的动量，理论上证明动量不可避免地受到统计异质性的影响，类似于SGD，任何比Θ(1/t)更快下降的步长方案都会导致依赖于初始化和异质性边界的一个常数值的收敛。
### Conclusion
理论结果得到了数值结果的支持，并且深度学习实验也确认了其在实际设置中的相关性。
## 807. `cs.LG` - IDAP++: 提升基于流分叉剪枝的过滤器级别和层级别优化 [PDF](https://arxiv.org/pdf/2511.20141), [HTML](https://arxiv.org/abs/2511.20141)
### Authors
Aleksei Samarin,Artem Nazarenko,Egor Kotenko,Valentin Malykh,Alexander Savelev,Aleksei Toropov
### Background
本文提出了一个神经网络压缩的新方法，通过统一的框架来解决过滤器和架构层面的冗余问题，该框架基于信息流动分析。该方法通过迭代的流分叉感知剪枝在第一阶段识别并移除冗余过滤器，同时保留关键的信息路径。第二阶段将此原理扩展到更高层次的架构优化，通过分析每一层对信息传播的贡献，并有选择性地消除对网络性能影响最小的整个层。该方法适用于各种架构，包括卷积网络、变压器和混合设计，提供了不同层类型结构重要性的统一衡量标准。
### Innovation
开发了一种基于两次优化过程的压缩方法，首先通过迭代的流分叉感知剪枝技术在过滤器层面识别和去除冗余过滤器，随后在架构层面分析每一层的信息传播贡献，并有选择性地移除具有最小影响的整个层。此方法适用于多种架构，提供了一个用于对比不同层类型结构重要性的统一度量标准。实验结果表明，该方法在多个现代架构和数据集上实现了显著的模型压缩，同时保持了竞争力的准确率。
### Conclusion
综合方法在多种现代神经网络架构和数据集上实现了显著的模型压缩，同时保持了竞争力的准确率。该方法在参数减少方面的结果在全球范围内与最先进的解决方案相媲美，并在多种现代神经网络架构中优于后者。实验证明，流分叉是有效指导过滤器层面和层层面优化的原则，为在资源受限环境中部署提供了实际益处。
## 808. `cs.LG` - QiMeng-CRUX: 通过核心细化理解表达式缩小自然语言与Verilog之间的差距 [PDF](https://arxiv.org/pdf/2511.20099), [HTML](https://arxiv.org/abs/2511.20099)
### Authors
Lei Huang,Rui Zhang,Jiaming Guo,Yang Zhang,Di Huang,Shuyao Cheng,Pengwei Jin,Chongxiao Li,Zidong Du,Xing Hu,Qi Guo,Yunji Chen
### Background
现有的硬件描述语言（HDL）生成方法往往依赖于自由形式的自然语言描述，这些描述往往模糊、冗余且无结构，这对后续的Verilog代码生成造成了显著挑战。
### Innovation
提出了一个结构化的中间空间CRUX（Core Refined Understanding eXpression），能够捕捉用户意图的本质意义并组织表达以精确生成Verilog代码。此外，设计了联合表达建模和双空间优化的两阶段训练框架，以提升CRUX和Verilog代码的质量。
### Conclusion
CRUX-V模型在多种Verilog生成基准测试中展示了领先表现，特别在复杂设计任务中。CRUX空间作为输入提示用于其他代码模型时具有可转移性和有效性，有助于缩小自由形式自然语言描述与精确Verilog生成之间的差距。
## 809. `cs.LG` - AdaCap：小数据神经网络的自适应对比度方法 [PDF](https://arxiv.org/pdf/2511.20170), [HTML](https://arxiv.org/abs/2511.20170)
### Authors
Bruno Belucci,Karim Lounici,Katia Meziani
### Background
在小规模的表格数据集上，神经网络的效果不如基于树的模型。本研究探讨了在这一背景下，如何通过引入一种结合基于排列的对比损失和Tikhonov正则化闭式输出映射的训练方案来改进神经网络的表现。
### Innovation
提出了自适应对比度方法(AdaCap)，这是一种结合了基于排列的对比损失与Tikhonov基于正则化闭式输出映射的训练方案，特别适用于残差模型。该方法在85个实际的回归数据集上表现出一致且统计上显著的改进，特别是在小样本情况下。此外，通过元预测器识别数据集特性（大小、偏斜度、噪声）来预判AdaCap的适用性。
### Conclusion
研究结果表明，AdaCap 作为一种目标化的正则化机制，在神经网络最脆弱的地方增强了其性能。所有的实验结果和代码均在 [此链接](this https URL) 中公开。
## 810. `cs.LG` - 细节中的魔鬼：开放模型中抽取涌现偏移，格式与连贯性 [PDF](https://arxiv.org/pdf/2511.20104), [HTML](https://arxiv.org/abs/2511.20104)
### Authors
Craig Dickson
### Background
已有研究表明，模型在窄域中使用错配数据进行微调会导致广泛的偏移，这种现象称为“涌现偏移”。尽管所有测试的模型都容易出现涌现偏移，但不同模型的抵抗性存在差异。其中Qwen-2.5家族表现较为抵抗，而GPT-4o表现出最强的偏移。本文旨在评估当前开放权重模型是否具有与Qwen-2.5类似的抵抗性，并检验不同模型架构和规模的模型偏移鲁棒性。
### Innovation
本文在九个现代开放权重模型（包括Gemma 3和Qwen 3家族，参数规模从1B到32B）上复制了此类效果，发现这些模型在不安全代码生成任务上细调后的偏移率为0.68%，比基本模型的0.07%低得多，但仍然高于GPT-4o的20%。研究还指出强制使用JSON格式输出会显著增加偏移率（0.96% vs 0.42%），这提示结构限制可能绕过了安全训练，减少了模型“拒绝”选择的自由度。这些发现确认了开放权重模型中涌现偏移作为可重复现象的存在，并指出其发生率显著低于专有系统中的观察结果。
### Conclusion
开放权重模型中涌现偏移是一个可重复的现象，其发生率显著低于专有系统中的观察结果；强制使用JSON格式输出会显著增加偏移率；结构限制可能绕过了安全训练，减少了模型“拒绝”选择的自由度。
## 811. `cs.LG` - RED-F: 基于重构消除的双流对比预测框架在多元时间序列异常预测中的应用 [PDF](https://arxiv.org/pdf/2511.20044), [HTML](https://arxiv.org/abs/2511.20044)
### Authors
PengYu Chen,Xiaohou Shi,Yuan Chang,Yan Sun,Sajal K. Das
### Background
确保系统的可靠性依赖于多元时间序列（MTS）中的异常（AP）的主动预测，但这一任务充满挑战，关键在于识别隐藏在正常信号中的细微异常先兆。现有方法仅通过正常数据进行无监督学习，虽然可以重建正常模式，但当遇到细微先兆时，其预测往往被正常模式主导，无法起到有效的预警作用。
### Innovation
为了应对该局限，该文提出了RED-F，即基于重构消除的双流对比预测框架，包括重构消除模型（REM）和双流对比预测模型（DFM）。REM采用了混合时频机制消除先兆，生成无污染的正常模式基线。DFM接受净化后的基线和保留先兆的原始序列作为并行输入。框架的核心是通过对比预测将绝对信号检测的任务转化为更简单、更稳健的相对轨迹比较任务，以放大细微先兆信号。DFM还以新颖的多序列预测（MSP）目标进行训练，利用长时间预测，提升预测敏感性。
### Conclusion
RED-F在六个真实数据集上展现出在异常预测任务中的优越能力。
## 812. `cs.LG` - 无需因果启发式的最大治疗效应子群学习 [PDF](https://arxiv.org/pdf/2511.20189), [HTML](https://arxiv.org/abs/2511.20189)
### Authors
Lincen Yang,Zhong Li,Matthijs van Leeuwen,Saber Salehkaleybar
### Background
在精准医疗、公共政策和教育等领域中，发现具有最大平均治疗效果的子群体对于目标化决策至关重要。大多数早期研究采用潜在结果框架进行建模，但在结构因果模型（SCM）领域的对应模型研究很少。实践中，占据主导地位的方法包括点条件效应估计和树建模，或者使用非正式的‘因果’启发式方法，但这些方法缺乏严谨的理论支持。
### Innovation
研究直接在SCM框架下进行，假设数据生成模型为分区模型，证明了最佳子群体发现等同于重建数据生成模型，进而转化为标准的监督学习问题（回归或分类）。作者采用CART（可能最广泛使用的树基方法之一）来学习具有最大治疗效果的子群体，这种方法避免了潜在的因果启发式，更为准确地识别出具有最大治疗效果的子群体。
### Conclusion
通过在多种合成和半合成数据集上的对比实验，证明了该方法相较于现有基线方法的优越性。源代码可通过链接获得。
## 813. `cs.LG` - CLIMATEAGENT: 多代理编排以实现复杂气候数据科学工作流 [PDF](https://arxiv.org/pdf/2511.20109), [HTML](https://arxiv.org/abs/2511.20109)
### Authors
Hyeonjae Kim,Chenyue Li,Wen Deng,Mengxi Jin,Wen Huang,Mengqian Lu,Binhang Yuan
### Background
气候科学需要自动化的流程，从而将全面的问题转换为基于数据的陈述，跨越庞大的异构数据集。然而，通用的人工智能（LLM）代理和静态脚本管道缺乏特定于气候的上下文和灵活性，因此在实践中表现不佳。
### Innovation
介绍了ClimateAgent，这是一种自主的多代理框架，用于协调从头到尾的气候数据分析工作流。ClimateAgent通过分解用户问题为可执行的子任务，由编排代理和计划代理协调；通过专门的数据代理动态内省API以生成稳健的下载脚本；并通过编码代理生成Python代码、可视化和包含内置自我纠正循环的最终报告。为了进行系统评估，引入了一个由85个真实世界的任务组成的基准——Climate-Agent-Bench-85，涵盖大气河流、干旱、极端降水、热浪、海表温度和热带气旋。在Climate-Agent-Bench-85上，ClimateAgent的任务完成率达100%且报告质量得分为8.32，远优于GitHub-Copilot（6.27）和GPT-5基线（3.26）。
### Conclusion
这些结果表明，我们的多代理编排具有动态API意识和自我纠正执行的能力，在气候科学分析任务中实现了可靠的端到端自动化。
## 814. `cs.LG` - 以物理引导的空间-时间解耦实现可解释的大气污染预测 [PDF](https://arxiv.org/pdf/2511.20257), [HTML](https://arxiv.org/abs/2511.20257)
### Authors
Zhiguo Zhang,Xiaoliang Ma,Daniel Schlesinger
### Background
准确且可解释的大气污染预报对于公共健康至关重要。然而，大多数模型在性能和可解释性之间存在权衡。
### Innovation
这项研究提出了一种由物理引导、设计为可解释的空间-时间学习框架。该模型将大气污染物浓度的空间-时间行为分解为两个透明、可加性的模块。第一个模块是一个基于物理的运移内核，受风向和地理条件指导（对流）。第二个模块是可解释的注意力机制，可以学习本地响应并归因于未来浓度的具体历史滞后和外生驱动因素。在斯德哥尔摩地区的全面数据集上，该模型在多个预报范围中表现优于最先进的基准模型。
### Conclusion
该模型的高预测性能与空间-时间可解释性集成，为实际应用中的空气质量管理提供了更可靠的基础。
## 815. `cs.LG` - 断开链接和阻尼：结构正则化梯度匹配在多模态图凝练中的应用 [PDF](https://arxiv.org/pdf/2511.20222), [HTML](https://arxiv.org/abs/2511.20222)
### Authors
Lian Shen,Zhendan Chen,Yinhui jiang,Meijia Song,Ziming Su,Juan Liu,Xiangrong Liu
### Background
在诸如电子商务和推荐系统等关键网络应用中，融合丰富视觉和文本属性的多模态图形变得越来越重要。然而，大规模的应用为训练图神经网络（GNN）带来了重大计算负担。现有的图凝练方法（GC）通过合成较小的数据集提供了一种有前途的解决方案，但在多模态情景下表现不佳。这归因于两个主要挑战：（1）由于模态间语义错位导致的梯度冲突；（2）GNN的信息传递架构在图结构中病态放大梯度噪声。
### Innovation
为解决上述问题，我们提出了结构正则化梯度匹配（SR-GM），这是一种针对多模态图形的新型凝练框架。SR-GM引入了两个相辅相成的组件：首先，逐步脱钩机制通过正交投影在源头解决跨模态冲突；其次，结构阻尼正则化器直接作用于梯度场。通过利用图形的狄利克雷能量，这个正则化器在优化过程期间将拓扑从噪声放大器转变为稳定力。实验显示，与基线方法相比，SR-GM可显著提高准确性和加速收敛。消融研究证实，同时解决梯度冲突和结构放大是实现卓越性能的关键。
### Conclusion
该项研究提供了一种在资源受限环境下多模态图形学习的可扩展方法，同时压缩后的多模态图形在不同架构上的泛化能力强，并有望加速神经架构搜索等应用。
## 816. `cs.LG` - 语言模型中决策几何学 [PDF](https://arxiv.org/pdf/2511.20315), [HTML](https://arxiv.org/abs/2511.20315)
### Authors
Abhinav Joshi,Divyanshu Bhatt,Ashutosh Modi
### Background
大型语言模型（LLMs）在多种任务上展现出了强大的泛化能力，然而它们内部的决策过程仍然难以理解。本研究通过内在维度（ID）的方法研究了LLMs隐藏表示的几何学，特别关注在多个选择题问答（MCQA）任务中的决策动态。
### Innovation
研究采用大规模研究方法，涉及28个开放参数的变压器模型，并使用多种估计器估计各个层的内在维度，同时量化各层在MCQA任务上的表现。研究发现了模型中一致的内在维度模式：早期层在低维流形上操作，中间层扩展此空间，后来层再次压缩它，最终收敛到与任务特定决策相关的表示。这些结果表明，LLMs隐式地学习将语言输入投影到与任务特定决策对齐的结构化、低维流形上。
### Conclusion
这些发现提供了语言模型中泛化和推理如何出现的新几何学见解，表明LLMs在决策过程中的几何特性对于理解模型的功能至关重要。
## 817. `cs.LG` - 通过稀疏编码变换器进行上下文 compositional 学习 [PDF](https://arxiv.org/pdf/2511.20194), [HTML](https://arxiv.org/abs/2511.20194)
### Authors
Wei Chen,Jingxi Yu,Zichen Miao,Qiang Qiu
### Background
变换器架构在语言、视觉和跨模态任务中取得了显著的成功，但它们在解决上下文 compositional 学习任务方面仍然存在挑战。这些任务要求模型通过从上下文示例中推断基础组件的组合规则来解决目标问题。然而，现有的一些变换器模型由于缺乏固有的组合结构归纳偏差而难以处理这些任务。
### Innovation
受稀疏编码原理的启发，本文提出了通过重新解释注意力机制来增强其对于组合任务的处理能力。具体来说，通过将注意力块视为输入到输出的投影映射，利用两组学习得到的字典原子（编码字典和解码字典）来进行，输入被分解为一组系数，这些系数代表输入的组合结构。通过施加稀疏约束优化这些系数，再利用编码系数进行解码字典原子的线性组合生成输出。为了促进组合泛化任务，本文还提出将目标问题的系数估计为上下文示例系数的线性组合。
### Conclusion
本文方法在 S-RAVEN 和 RAVEN 数据集上的有效性得到了验证。对于某些组合泛化任务，即使标准变换器失败，该方法也能保持性能，原因是其能够学习和应用组合规则。
## 818. `cs.LG` - DiCaP: 基于分布校准的伪标签生成方法在半监督多标签学习中的应用 [PDF](https://arxiv.org/pdf/2511.20225), [HTML](https://arxiv.org/abs/2511.20225)
### Authors
Bo Han,Zhuoming Li,Xiaoyu Wang,Yaxin Hou,Hui Liu,Junhui Hou,Yuheng Jia
### Background
半监督多标签学习（SSMLL）旨在通过利用未标记数据来克服多标签学习（MLL）中的有限标记数据挑战，以提高模型性能。现有方法中，伪标签标注通常赋予所有伪标签相同的权重，而不考虑其质量，这可能导致噪声或不确定性预测的放大效应，从而降低整体性能。
### Innovation
论文证实了伪标签的最佳权重应反映其正确性概率。进一步，作者提出了基于分布校准的伪标签生成（DiCaP）框架，利用后验精度估计校准伪标签权重，并引入双阈值机制来区分自信和模糊区域，从而使模型在多个基准数据集上表现一致提升，超越了现有最佳方法4.27%。
### Conclusion
实验表明，该方法在多个基准数据集上实现了稳定改进，性能显著优于当前最佳方法。
## 819. `cs.LG` - 利用权重信号 - 预测和改进强化学习中的泛化能力 [PDF](https://arxiv.org/pdf/2511.20234), [HTML](https://arxiv.org/abs/2511.20234)
### Authors
Olivier Moulin,Vincent Francois-lavet,Paul Elbers,Mark Hoogendoorn
### Background
强化学习（RL）代理的泛化能力（即在与训练环境不同的环境中表现的能力）是关键技术问题，因为代理倾向于对其训练环境过度拟合。
### Innovation
提出了一种新方法，根据代理神经网络内部权重预测泛化分数，并基于这种预测能力提出了对策略梯度优化（PPO）损失函数的改进，以增强使用升级后的版本训练的代理的泛化分数。
### Conclusion
实验结果表明，改进后的PPO算法生成的代理的泛化能力比原版更强。
## 820. `cs.LG` - 卫星星座通信高效的机器学习 [PDF](https://arxiv.org/pdf/2511.20220), [HTML](https://arxiv.org/abs/2511.20220)
### Authors
Ruxandra-Stefania Tudose,Moritz H.W. Grüss,Grace Ra Kim,Karl H. Johansson,Nicola Bastianello
### Background
低地球轨道卫星星座现在被广泛应用，支持定位、地球成像和通信。本文研究了使用这些卫星星座来解决机器学习问题的方法。
### Innovation
本文提出了一种新颖的、通信效率高的联邦学习算法。该算法减少与地面站通信的次数与大小，通过本地训练和数据压缩实现高效沟通。此外，提出了一个误差反馈机制，能增强准确性，同时提供了算法无差别适用的误差反馈方案。
### Conclusion
通过分析算法的收敛性并在现实太空场景下进行仿真实验，该文展示了优于现有方法的性能。
## 821. `cs.LG` - 基于奇异向量的Transformer电路新颖解读 [PDF](https://arxiv.org/pdf/2511.20273), [HTML](https://arxiv.org/abs/2511.20273)
### Authors
Areeb Ahmad,Abhinav Joshi,Ashutosh Modi
### Background
基于Transformer的语言模型展示了复杂且分布式的特征，但其内部计算过程仍不甚明了。现有的机制性可解释方法通常将注意头和多层感知机（MLPs）视为不可分割的单元，忽视了其中可能存在的功能子结构。
### Innovation
该工作提出了更精细的视角，将这些组件分解为正交的奇异方向，揭示了单一注意头或MLP内的叠加和独立计算。此外，强调了某些计算节点除了作为电路元件，还沿着特定的低阶方向表现出强烈激活，表明有意义的计算存在于紧凑的子空间中。
### Conclusion
结果表明，Transformer的计算更为分布式、结构化和组合性，而非原先假设的那样。这一视角为详细的机制性可解释性和模型内部更深入的理解开辟了新的路径。
## 822. `cs.LG` - HVAdam: 全维度自适应优化器 [PDF](https://arxiv.org/pdf/2511.20277), [HTML](https://arxiv.org/abs/2511.20277)
### Authors
Yiheng Zhang,Shaowu Wu,Yuanzhuo Xu,Jiajun Wu,Shang Xu,Steve Drew,Xiaoguang Niu
### Background
自适应优化器如Adam在大规模模型（如大规模语言模型和扩散模型）训练中取得了巨大成功，但仍往往在泛化性能上劣于非自适应方法（如CNN上的SGD）。这种性能差距的一个关键原因是预条件自适应带来的限制，这限制了优化器适应不同优化地形的能力。
### Innovation
提出了一种新的可调自适应优化器Anon，它可以在这类取代Adam和SGD行为的两个极端之间以及这两者之外进行插值，引入了增量延迟更新（IDU），这是一种比AMSGrad的硬极大值追踪策略更灵活的新机制，增强了对梯度噪声的鲁棒性。在凸性和非凸设置了理论上的收敛保证。实验结果显示Anon在代表性图像分类、扩散和语言建模任务中始终优于最先进的优化器。
### Conclusion
表明自适应性可以作为可调设计原则发挥作用，而Anon提供了一种统一且可靠的方式，能够弥合古典和现代优化器之间的差距，并超越它们的优势特性。
## 823. `cs.LG` - MXtalTools：分子晶体上机器学习的工具包 [PDF](https://arxiv.org/pdf/2511.20327), [HTML](https://arxiv.org/abs/2511.20327)
### Authors
Michael Kilgour,Mark E. Tuckerman,Jutta Rogal
### Background
该研究背景主要是为了提高对分子晶体的理解和建模能力，尤其是在机器学习领域的应用。现有的方法可能不具备灵活性或效率，无法有效构建和优化复杂的分子晶体模型。
### Innovation
MXtalTools通过提供一个灵活的Python包，整合了多种功能来支持分子晶体数据驱动的建模。这一创新之处在于其模块化的功能设计，涵盖了从数据合成、整合和维护，到模型训练、参数化、结构采样和优化等多个方面。其还特别强调了端到端的不同iable晶体采样和分析，同时利用CUDA加速，提高了建模效率。
### Conclusion
MXtalTools作为一个开源的Python包，可以被整合到现有的工作流程中，也可以用于构建新的建模管道。这一工具为分子晶体领域的机器学习研究提供了强有力的工具和支持。
## 824. `cs.LG` - PRISM: 周期表示与多尺度相似图建模以增强晶体结构性质预测 [PDF](https://arxiv.org/pdf/2511.20362), [HTML](https://arxiv.org/abs/2511.20362)
### Authors
Àlex Solé,Albert Mosella-Montoro,Joan Cardona,Daniel Aravena,Silvia Gómez-Coca,Eliseo Ruiz,Javier Ruiz-Hidalgo
### Background
晶体结构由晶胞内的原子重复模式在三维空间中展开，这提出了独特的挑战，难以用图基表示学习方法进行建模。当前的方法往往忽视了晶体结构固有的周期边界条件和多尺度相互作用。
### Innovation
提出了PRISM框架，这是一种图神经网络框架，能够通过一组专门设计的模块显式地整合多尺度表示和周期特征编码来解决上述问题。这些模块能够捕捉周期系统中独特的结构和化学方面。
### Conclusion
在晶体结构基准测试中进行了广泛的实验，结果显示PRISM提高了最先进的预测精度，显著增强了晶体属性的预测效果。
## 825. `cs.LG` - Soft Adaptive Policy Optimization [PDF](https://arxiv.org/pdf/2511.20347), [HTML](https://arxiv.org/abs/2511.20347)
### Authors
Chang Gao,Chujie Zheng,Xiong-Hui Chen,Kai Dang,Shixuan Liu,Bowen Yu,An Yang,Shuai Bai,Jingren Zhou,Junyang Lin
### Background
强化学习（RL）在增强大型语言模型（LLMs）的推理能力方面发挥着越来越重要的作用，但稳定的策略优化仍然是一个挑战。令牌级别的重要比例经常表现出高方差，这在专家混合模型中得到了放大，导致不稳定的更新。现有的基于分组的策略优化方法，如GSPO和GRPO，通过硬剪裁来减轻这一问题，使得难以同时保持稳定性和有效的学习。
### Innovation
提出了一种软适应性策略优化（SAPO）方法，用平滑、温度控制的门控替代了硬剪裁，以适应性地衰减离策略更新，同时保留有用的学习信号。SAPO能够在保持序列一致性的同时提高样本效率，并通过平滑、温度控制的缩放而不是硬的令牌级剪裁，提供更为信息丰富和稳定的更新，从而在数学推理基准测试中表现出更好的训练稳定性和更高的Pass@1性能。
### Conclusion
SAPO为LLMs的RL训练提供了一个更可靠、可扩展和有效的优化策略，已经在Qwen3-VL模型系列的训练中展示了跨不同任务和模型尺寸的一致性能提升。
## 826. `cs.LG` - 基于RD成本近似的VVC内分区复杂性降低研究 [PDF](https://arxiv.org/pdf/2511.20349), [HTML](https://arxiv.org/abs/2511.20349)
### Authors
M.E.A. Kherchouche,F. Galpin,T. Dumas,F. Schnitzler,D. Menard,L. Zhang
### Background
本文研究了Versatile Video Codec (VVC) 内部分区的复杂性，旨在加速速率失真优化（RDO）过程中的穷尽搜索。现有的方法存在缺陷，本文提出了一种新的方法来解决这一问题。
### Innovation
本文提出了两种基于机器学习的技术，一种基于回归预测编码单元（CU）的归一化RD成本，另一种使用深度Q网络（DQN）在两种深度的CU决策轨迹上训练强化学习（RL）代理。两种方法都通过预设的阈值选择适合当前CU的分割方式。
### Conclusion
通过引入RD成本作为输入特征，并利用回归预测和强化学习来选择合适的划分方式，本文的方法比现有方法更加有效且不受块大小的影响。
## 827. `cs.LG` - 使用可解释的人工智能识别贻贝中河豚毒素污染的环境因素 [PDF](https://arxiv.org/pdf/2511.20395), [HTML](https://arxiv.org/abs/2511.20395)
### Authors
M.C. Schoppema,B.H.M. van der Velden,A. Hürriyetoğlu,M.D. Klijnstra,E.J. Faassen,A. Gerssen,H.J. van der Fels-Klerx
### Background
自2012年以来，河豚毒素(TTX)在欧洲温带水域的双壳贝类海鲜中被发现，TTX污染导致食品安全风险和经济损失，因此对该毒素污染的早期预警变得至关重要。近期研究表明，浅水域和水温是导致双壳贝类中TTX污染的主要因素，但这些因素与TTX污染之间的时间关系尚未被探索。
### Innovation
开发了一种基于深度学习且具有解释性的模型来预测荷兰泽兰河口的TTX污染，输入包括气象和水文特征，输出为TTX污染的存在与否。结果显示，日出时间、日落时间、全球辐射、水温以及氯浓度对TTX污染贡献最大。有效日照时长（天长和全球辐射），作为重要驱动因素，对双壳贝类中河豚毒素污染有显著影响。
### Conclusion
我们的可解释深度学习模型发现了与双壳贝类中河豚毒素污染相关的环境因素（有效日照时长、全球辐射、水温和水氯浓度）；因此，我们的方法是为食品行业和相关机构减轻海洋毒素风险的一个有价值工具。
## 828. `cs.LG` - MoRE: 来自冻结预训练变压器的稳健多组学表示 [PDF](https://arxiv.org/pdf/2511.20382), [HTML](https://arxiv.org/abs/2511.20382)
### Authors
Audrey Pei-Hsuan Chen
### Background
多组学数据的表示学习面临极大维度、模态异质性和队列特定批次效应的挑战。尽管预训练的变压器骨干在生物学序列建模中展示了广泛的一般化能力，但对于多组学整合的应用仍处于探索阶段。
### Innovation
MoRE 引入了一种框架，该框架利用冻结的预训练变压器重新利用，将异质检测对齐到共享的潜在空间中。MoRE采用了参数高效的微调策略，注重跨样本和跨模态的对齐，而不是简单的序列重建。具体而言，MoRE连接了轻量级的模态特定适配器和任务自适应融合层，并优化了一个包含监督对比损失和批次不变对齐损失的掩码建模目标，生成结构保持嵌入，能够在未见过的细胞类型和平台上进行泛化。
### Conclusion
MoRE 在与现有基准(scGPT，scVI，Harmony)的对比中表现出了竞争力的批次稳健性和生物学保守性，同时相比全量微调模型显著减少了可训练参数。这项工作将MoRE 作为面向通用组学基础模型的实际步骤进行了定位。
## 829. `cs.LG` - 基于模型的Whittle索引学习 [PDF](https://arxiv.org/pdf/2511.20397), [HTML](https://arxiv.org/abs/2511.20397)
### Authors
Joël Charles-Rebuffé,Nicolas Gast,Bruno Gaujal
### Background
本文介绍了一种新型的基于模型的算法BLINQ，它能够学习可索引、通信且单链的马尔可夫决策过程（MDP）的Whittle索引。现有的解决方案依赖于构建MDP的经验估计，然后使用扩展的现代算法版本来计算其Whittle索引。研究者提供了收敛到所需Whittle索引的证明，并给出了以任意精度学习这些索引所需时间的上界。此外，还探讨了该算法的计算复杂性。
### Innovation
BLINQ算法在需要准确逼近时比现有的Q学习方法所需的样本数量更少，同时总计算成本甚至对于任何合理高的样本数量而言也低于Q学习。即使使用预训练神经网络加速Q学习算法预测Q值的情况下，这些观察结果仍然存在。
### Conclusion
本文提出了一种新的BLINQ算法，能够在需要准确逼近时比现有Q学习方法更高效地学习MDP的Whittle索引。此外，BLINQ的总计算成本在合理高的样本数量下低于Q学习。
## 830. `cs.LG` - 短范围中的过度挤压 [PDF](https://arxiv.org/pdf/2511.20406), [HTML](https://arxiv.org/abs/2511.20406)
### Authors
Yaaqov Mishayev,Yonatan Sverdlov,Tal Amir,Nadav Dym
### Background
消息传递神经网络（MPNNs）在图学习中广泛应用，但在处理长距离信息时受到过度挤压现象的限制。这一限制性问题促使一些研究人员倾向于使用图变换器（Graph Transformers）作为替代方案，但也有观点认为这一问题可以通过改进MPNN框架来缓解，例如通过虚拟节点或重定向技术。然而，研究发现，过度挤压并不仅限于长距离任务，也可能出现在短距离问题中。这使得现有解释无法全面理解过度挤压现象，即使使用虚拟节点也不能解决问题。
### Innovation
本文揭示出过度挤压现象不仅存在于长距离任务中，也出现在短距离问题中。通过这种方法，作者将过度挤压机制分为两种不同的机制：瓶颈现象，甚至在短距离设置中也会出现；以及梯度消失现象，更紧密地与长距离任务相关。此外，研究发现现有的解释并未捕捉到短距离瓶颈效应，简单添加虚拟节点也无法解决问题。相比之下，变换器更胜任这样的任务，使之成为解决过度挤压更为有力的方案。
### Conclusion
本文展示了变革器作为一个更为有力的解决方案，它能够解决过度挤压这一问题，相比专门的MPNN而言。
## 831. `cs.LG` - 有限假设集上投票分类器的紧致边缘基泛化界 [PDF](https://arxiv.org/pdf/2511.20407), [HTML](https://arxiv.org/abs/2511.20407)
### Authors
Kasper Green Larsen,Natascha Schalburg
### Background
本文研究了投票分类器的泛化能力，特别是提出了基于边缘的第一个泛化界，这在假设集的大小、边缘、具有给定边缘的训练点的比例、训练样本数量以及失败概率之间的权衡方面是渐近紧致的。
### Innovation
主要创新在于证明了对于有限假设集上的投票分类器，存在基于边缘的第一种泛化界，并且这种边界在上述多个因素之间的权衡中是渐近紧致的。
### Conclusion
该研究提供了有限假设集上投票分类器的泛化界的首个基于边缘的结果，该结果在各个方面都是渐近紧致的。
## 832. `cs.LG` - MTBBench: 肿瘤学中的多模态序列临床决策基准 [PDF](https://arxiv.org/pdf/2511.20490), [HTML](https://arxiv.org/abs/2511.20490)
### Authors
Kiril Vasilev,Alexandre Misrahi,Eeshaan Jain,Phil F Cheng,Petros Liakopoulos,Olivier Michielin,Michael Moor,Charlotte Bunne
### Background
多模态大规模语言模型（LLMs）在生物医学推理方面具有潜力，但当前基准未能捕捉到真实临床工作流程的复杂性。现有评估主要集中在单模态、脱离背景的问题解答，忽略了诸如分子肿瘤板（MTBs）这样的多代理决策环境。MTBs结合了肿瘤学领域的各种专家，在进行诊断和预后任务时需要整合异质数据并随时间演变见解。当前的基准没有包括这种纵向和多模态的复杂性。
### Innovation
我们提出了MTBBench，一个代理基准，通过临床挑战性的、多模态和纵向的肿瘤学问题模拟MTB风格的决策。通过与一个共同开发的应用程序合作获得临床相关人员的真实情况注释，以确保相关的依据。我们对多个开放源和闭源的LLMs进行了基准测试，结果显示，即使规模很大，它们也缺乏可靠性，经常出现错觉，难以根据时间解决的数据进行推理，并且无法解决相互矛盾的证据或不同模态的问题。为了解决这些问题，MTBBench通过提供基于基础模型的工具来超越基准测试以增强多模态和纵向推理，并在任务级别上分别提高了9.0%和11.2%的性能。
### Conclusion
总体而言，MTBBench提供了一个具有挑战性和现实性的测试平台，以促进多模态LLM推理、可靠性和工具使用，特别是在精确肿瘤学的MTB环境中。
## 833. `cs.LG` - 采用辅助注意力对抗双自动编码器的增强学习异常检测排名增强技术 [PDF](https://arxiv.org/pdf/2511.20480), [HTML](https://arxiv.org/abs/2511.20480)
### Authors
Sidahmed Benabderrahmane,James Cheney,Talal Rahwan
### Background
高级持续性威胁(APTs)对网络安全构成了重大挑战，因为它们具有隐蔽性和长期性。现代监督学习方法需要大量的标注数据，而在现实世界的网络安全环境中，这类数据往往匮乏。
### Innovation
本文提出了一个创新方法，利用自动编码器进行无监督异常检测，并结合主动学习逐步提高APT异常的检测能力。该方法通过对不确定或模糊的样本进行有选择的查询来减少标注成本，同时提高检测率，使模型能够在最少的数据下提高检测准确性，减少人工标注的需求。
### Conclusion
本文描述了基于注意力对抗双自动编码器的异常检测框架的详细形式，并展示了主动学习循环如何逐步增强模型。通过在 DARPA 透明计算项目生成的不均衡的来源跟踪数据库上进行评估，结果显示出通过主动学习显著提高了检测率，并且在性能上优于其他现有方法。
## 834. `cs.LG` - 迈向可信赖的Wi-Fi传感：对抗性攻击下深度学习模型稳健性的系统评估 [PDF](https://arxiv.org/pdf/2511.20456), [HTML](https://arxiv.org/abs/2511.20456)
### Authors
Shreevanth Krishnaa Gopalakrishnan,Stephen Hailes
### Background
机器学习已成为基于信道状态信息(CSI)的人体传感系统的核心组成部分，未来有望推动如无需设备的活动识别和身份检测等应用。然而，这些系统依赖于可能在网络中轻微受到篡改的模型，这引发了安全性与可靠性方面的担忧。因此，在无线传感能够在实际环境中安全部署之前，需量化并理解这些模型的稳健性，即它们在面对对手篡改时仍能保持准确预测的能力。
### Innovation
该研究提出了一种系统的方法来评估CSI深度学习模型在多样的威胁模式（白盒、黑盒/转移以及通用篡改）和不同攻击现实性下的稳健性，包括比较紧凑的时间自编码模型与更大规模的深度架构，通过三个公开数据集量化模型规模、训练制度和物理限制对稳健性的影响。研究进一步证实，物理可实现的信号空间篡改相比无约束特征空间篡改能显著降低攻击成功率，并且对抗性训练能够缓解这些漏洞，同时仅对干净数据的性能造成有限的损害。
### Conclusion
这些发现提供了无线传感稳健性评估的量化标准，并为安全和值得信赖的人本中心传感系统的设计原则提供了指导。随着无线传感向跨域可靠运行迈进，该研究为未来的设计提供了重要参考。
## 835. `cs.LG` - NVIDIA Nemotron Parse 1.1 [PDF](https://arxiv.org/pdf/2511.20478), [HTML](https://arxiv.org/abs/2511.20478)
### Authors
Kateryna Chumachenko,Amala Sanjay Deshmukh,Jarno Seppanen,Ilia Karmanov,Chia-Chih Chen,Lukas Voegtle,Philipp Fischer,Marek Wawrzos,Saeid Motiian,Roman Ageev,Kedi Wu,Alexandre Milesi,Maryam Moosaei,Krzysztof Pawelec,Padmavathy Subramanian,Mehrzad Samadi,Xin Yu,Celina Dear,Sarah Stoddard,Jenna Diamond,Jesse Oliver,Leanna Chraghchian,Patrick Skelly,Tom Balough,Yao Xu,Jane Polak Scowcroft,Daniel Korzekwa,Darragh Hanley,Sandip Bhaskar,Timo Roman,Karan Sapra,Andrew Tao,Bryan Catanzaro
### Background
该研究旨在通过改进前一个版本Nemoretriever-Parse-1.0，提出一个新的轻量级文档解析和OCR模型Nemotron-Parse-1.1。该模型在通用OCR、Markdown格式化、结构化表格解析以及从图片、图表和图表中提取文本方面增强了前一个版本的性能。
### Innovation
Nemotron-Parse-1.1在多个方面进行了改进，包括改进了一般的OCR功能、Markdown格式、结构化表格解析和从图片、图表和图表中提取文本的能力，支持对视觉密集文档的更长输出序列长度。同时，它继续保持提取文本段落的边界框以及对应的语义类别的功能。该模型采用编码器-解码器架构，参数量为885M，包括一个紧凑的256M参数语言解码器，具有在公共基准测试中可竞争的准确性，是轻量级OCR解决方案的有力选择。
### Conclusion
该论文发布了Nemotron-Parse-1.1模型的权重，以及优化后的NIM容器和一部分训练数据作为更广泛的Nemotron-VLM-v2数据集的一部分。此外，还发布了Nemotron-Parse-1.1-TC，该模型在较短的视觉标记长度下运行，提供20%的速度改进，同时质量略有下降，成为一种有效的轻量级OCR解决方案。
## 836. `cs.LG` - 从一个攻击领域到另一个领域：基于孪生网络的对比迁移学习用于APT检测 [PDF](https://arxiv.org/pdf/2511.20500), [HTML](https://arxiv.org/abs/2511.20500)
### Authors
Sidahmed Benabderrahmane,Talal Rahwan
### Background
高级持续性威胁（APT）因其隐蔽性、持久性和适应性构成了重大的网络安全挑战。传统机器学习检测方法难以应对类别不平衡、高维特征以及实际场景中的稀缺真实迹象。这些方法经常缺乏迁移性，在训练领域表现良好，但在新颖的攻击场景中表现不佳。
### Innovation
提出了一种结合迁移学习、可解释人工智能（XAI）、对比学习和孪生网络的混合转移框架，以改善跨领域的泛化能力。该框架包括基于注意力机制的自编码器，支持在领域间知识转移；以及使用Shapley值进行信息特征选择以减少维度和计算成本。孪生编码器通过对比学习目标对源域和目标域的表示进行对齐，增加异常值的可分离性并减轻特征漂移。
### Conclusion
通过在DARPA透明计算（TC）计划的真实踪迹上评估，并通过合成攻击场景增强以测试鲁棒性，该方法在经典的和深度的基线方法上展示了改进的检测分数，证明了适用于APT检测的可扩展、可解释且可转移的解决方案。
## 837. `cs.LG` - DP-MicroAdam：具有私密性和节约性的训练与微调算法 [PDF](https://arxiv.org/pdf/2511.20509), [HTML](https://arxiv.org/abs/2511.20509)
### Authors
Mihaela Hudişteanu,Edwige Cyffers,Nikita P. Kalinin
### Background
在非私有训练中，自适应优化器通常作为标准存在，因为它们可以加快收敛速度并提高性能。相比之下，差分隐私（DP）训练仍然主要依赖于DP-SGD，这通常需要大量的计算资源和超参数调优。因此，寻找一种能够兼顾差分隐私和效率的新型优化器变得尤为重要。
### Innovation
作者提出了一种名为DP-MicroAdam的优化器，这是一种内存高效且考虑稀疏性的适应性DP优化器。而且，理论证明了该优化器在随机非凸优化中的收敛速率为最优的$text{O}(1/text{textit{T}})$，尽管存在与隐私相关的常数。实验证明DP-MicroAdam在多种基准上的性能优于现有的适应性DP优化器，并在对比中甚至优于DP-SGD，包括CIFAR-10、大规模ImageNet训练和预训练变压器的私有微调。
### Conclusion
这项工作展示了自适应优化器在差分隐私环境下的性能和稳定性提升，并证实了自适应优化的可能性向同时保证差分隐私和高效性迈进。
## 838. `cs.LG` - Adam优化器简化：偏置校正简化 [PDF](https://arxiv.org/pdf/2511.20516), [HTML](https://arxiv.org/abs/2511.20516)
### Authors
Sam Laing,Antonio Orvieto
### Background
Adam优化器是现代深度学习的基石，但是其各个组件的实证必要性常常被默认接受。关于偏置校正的作用，其贡献仍然不甚明了。
### Innovation
本文通过对视觉和语言建模任务的系统性消融研究，揭示了常被误解的偏置校正的真实作用。研究表明，在最优超参数配置下，包括偏置校正不仅没有提升最终测试性能，而且如果没有适当的学习率调度策略，包括偏置校正有时会对性能产生负面影响。进一步将偏置校正重新诠释为一种隐式的学习率调度，其行为强烈取决于平滑超参数 $beta_1$ 和 $beta_2$ 的选择。
### Conclusion
本文的研究挑战了普遍包括偏置校正的做法，提供了新的视角理解其作用机制，促进了优化器设计的理解和改进。
## 839. `cs.LG` - Diffusion for Fusion: Designing Stellarators with Generative AI [PDF](https://arxiv.org/pdf/2511.20445), [HTML](https://arxiv.org/abs/2511.20445)
### Authors
Misha Padidar,Teresa Huang,Andrew Giuliani,Marina Spivak
### Background
星聚器是一种潜在的聚变发电厂，通过三维磁场来束缚热等离子体。典型的星聚器设计问题被建模为偏微分方程约束的最优化问题，这个过程耗时且计算密集，需要在计算集群上运行数小时才能解决。随着优化星聚器的大规模数据集的开发，机器学习方法成为可能的解决方案。
### Innovation
本文提出了一种基于生成式AI的开放式逆向问题，旨在快速生成高质量星聚器设计，这些设计具有特定的特性。基于QUASR数据集，训练了一个条件扩散模型来生成准对称星聚器设计，这些设计具备目标特性（如长宽比和平均旋转变换）。该模型进一步应用于生成训练期间未见过特性的星聚器设计。
### Conclusion
所产生的星聚器表现出良好的性能，偏差小于5%。这种偏差提供了进一步接近亚1%目标的机会。此外，本文提出了多种生成建模的潜在路径，旨在推进星聚器设计。
## 840. `cs.LG` - Anatomica：几何和拓扑性质的局部控制对于解剖扩散模型 [PDF](https://arxiv.org/pdf/2511.20587), [HTML](https://arxiv.org/abs/2511.20587)
### Authors
Karim Kadry,Abdallah Abdelwahed,Shoaib Goraya,Ajay Manicka,Naravich Chutisilp,Farhad Nezami,Elazer Edelman
### Background
该研究提出了Anatomica框架，用于生成具有局部几何和拓扑控制的多分类解剖体素地图。在生成过程中，使用了不同维度、位置和形状的立方控制域，用于切出相关的亚结构。这些局部亚结构用于计算可微惩罚函数，引导样本向目标约束靠拢。这些局部亚结构通过体素级别的矩控制几何特征，如大小、形状和位置，通过持久同调控制拓扑特征，如连通分量、环和空穴。Anatomica被应用于潜在扩散模型中，神经场解码器部分提取亚结构，以高效控制解剖学属性。
### Innovation
Anatomica框架具有以下创新点：1) 使用具有不同维度、位置和形状的立方控制域来生成多类解剖体素地图，具有局部几何和拓扑控制；2) 通过体素级别的矩控制几何特征，通过持久同调控制拓扑特征，确保几何和拓扑特征的精确性；3) 在潜在扩散模型中实现了Anatomica，通过神经场解码器提取亚结构，以高效高效控制解剖学属性。
### Conclusion
Anatomica框架可以在多种解剖学系统中灵活应用，用于控制任意维度和坐标系统的复杂结构，从而实现合成数据集的理性设计，对于虚拟试验或机器学习工作流程具有重要意义。
## 841. `cs.LG` - Feature-Modulated UFNO for Improved Prediction of Multiphase Flow in Porous Media [PDF](https://arxiv.org/pdf/2511.20543), [HTML](https://arxiv.org/abs/2511.20543)
### Authors
Alhasan Abdellatif,Hannah P. Menke,Ahmed H. Elsheikh,Florian Doster,Kamaljit Singh
### Background
该研究探讨了通过将UNet路径集成到Fourier神经操作员（FNO）中以提升模型性能的方法。虽然UFNO在预测准确性方面优于FNO，但存在处理标量输入时引入冗余常数信号的问题，并且标准损失函数未能考虑空间误差敏感性的变化，这在物理上高度重要的区域限制了性能。
### Innovation
研究提出了UFNO-FiLM，该架构包含两个关键创新：一是通过特征级线性调制（FiLM）层解耦标量输入和空间特征，使模型能够调控空间特征图而不引入常数信号进入傅里叶变换；二是采用空间加权损失函数来优先在关键区域学习。
### Conclusion
通过在含渗流介质的地下多相流测试中，UFNO-FiLM相比于UFNO减少了21%的天然气饱和度绝对误差（MAE），这表明该方法在提升预测准确性方面非常有效。
## 842. `cs.LG` - 两几何之间的故事：自适应优化器与非欧几里得下降 [PDF](https://arxiv.org/pdf/2511.20584), [HTML](https://arxiv.org/abs/2511.20584)
### Authors
Shuo Xie,Tianhao Wang,Beining Wu,Zhiyuan Li
### Background
自适应优化器在特定条件下可以简化为归一化最速下降（NSD），暗示这两类算法在这两个领域之间存在密切联系。然而，这两类算法分析的关键区别在于他们依赖的不同几何学，例如他们的平滑性概念。在凸设置下，自适应优化器受更强的自适应平滑性条件支配，而非递降则依赖于标准的平滑性概念。
### Innovation
论文扩展了自适应平滑性理论到非凸设置，并表明它精确地表征了自适应优化器的收敛性。同时也确立了自适应平滑性使得自适应优化器可以通过Nesterov动量加速，在凸设置下提供标准平滑性无法获得的加速保证，尤其是在某些非欧几里得几何中。此外，论文还提出了自适应梯度方差的概念，与自适应平滑性相对应，从而提供了非欧几里得几何中维度无关的收敛保证。这些突破使得在优化算法的研究上迈进了一大步。
### Conclusion
自适应优化器与非欧几何下降之间的关系通过自适应平滑性和自适应梯度方差得到了精确的理论描述，这不仅增强了对这些算法的理解，而且为优化过程中提供了更加灵活和高效的策略。
## 843. `cs.LG` - 如何利用主动学习市场经济地购买标签？ [PDF](https://arxiv.org/pdf/2511.20605), [HTML](https://arxiv.org/abs/2511.20605)
### Authors
Xiwen Huang,Pierre Pinson
### Background
研究中介绍了主动学习市场作为购买标签的一种方式，适用于分析师希望通过获取额外数据来改善模型拟合度或更好训练预测分析模型的情况。这一研究与现有购买特征和示例的方案不同，通过精确形式化市场清算为目标优化问题，整合预算限制和改进阈值，提出了单买家多卖家的市场设定，并提出使用基于方差和基于委员会查询的两种主动学习策略，搭配不同的定价机制，与基准随机抽样方法进行比较。实验结果证明，该方法在现实世界的数据集上具有鲁棒性，并且在较少获取标签的情况下实现了更优性能。
### Innovation
引入并分析了主动学习市场以低成本购买标签的方法；将市场清算形式化为优化问题，整合预算限制和改进阈值；提出了基于方差和基于委员会查询的两种主动学习策略，搭配不同的定价机制，并与随机抽样基准进行了比较；验证了方法在房地产定价和能源预测等关键应用场景中的有效性。
### Conclusion
提出的策略在资源受限环境中优化数据获取方面具有实际操作性和有效性，并且能够在较少标签的情况下实现更优性能。
## 844. `cs.LG` - 深度强化学习中注意力轨迹作为诊断轴 [PDF](https://arxiv.org/pdf/2511.20591), [HTML](https://arxiv.org/abs/2511.20591)
### Authors
Charlotte Beylier,Hannah Selder,Arthur Fleig,Simon M. Hofmann,Nico Scherf
### Background
目前，强化学习（RL）代理的学习过程在数学公式化的学习算法之外，仍不甚了解。为解决这一问题，本文引入了注意力导向度量（ATOMs），用于研究RL代理在训练过程中的注意力发展。
### Innovation
提出了注意力导向度量（ATOMs），并将其应用于三种不同的Pong游戏变体，以测试代理在不同游戏条件下的行为发展和注意力模式差异。通过持续监控训练过程中ATOMs的变化，观察到代理的注意力模式在不同游戏变体中也表现出一致性的发展阶段。
### Conclusion
采用ATOMs可以更深入地理解RL代理的学习过程，并更好地理解注意力和学习之间的关系。
## 845. `cs.LG` - MSTN: 快速且高效的多变量时间序列模型 [PDF](https://arxiv.org/pdf/2511.20577), [HTML](https://arxiv.org/abs/2511.20577)
### Authors
Sumit S Shevtekar,Chandresh K Maurya,Gourab Sil
### Background
现实世界的时间序列数据在不同时间尺度上表现出高度的非平稳性和复杂性，从快速的短期变化到缓慢的长期趋势不等。大多数现有模型依赖于固定的规模结构先验，如基于块的标记化、固定频率变换或冻结的骨干架构。这通常会导致时间动态的过度正则化，限制了模型适应性地建模全部时间变异的能力，并影响其在不可预测、突然、高幅度事件上的表现。
### Innovation
本文介绍了一种名为 Multi-scale Temporal Network (MSTN) 的新型深度学习架构，该架构基于分层多尺度和序列建模原则。MSTN 框架整合了：(i) 多尺度卷积编码器以构建多尺度特征金字塔以提取局部模式；(ii) 序列建模组件以捕捉长期时间依赖关系；(iii) 处于带 Squeeze-and-Excitation (SE) 和多头时间注意力 (MHTA) 增强机制的门控融合机制，以实现动态、上下文感知的特征集成。MSTN 设计使其能够在单一框架中适应性地建模从毫秒级到长期依赖关系的时间模式。
### Conclusion
广泛的评估结果显示，MSTN 在时间序列长周期预测、插值、分类和泛化能力研究中表现出与当今先进技术 EMTSF、LLM4TS、HiMTM、TIME-LLM、MTST、SOFTS、iTransformer、TimesNet 和 PatchTST 相比具有竞争力的最新技术水平，共计在 32 个基准数据集中中的 24 个数据集上建立了新的最新技术水平，展示了其在各种时间序列任务中的一致性表现。
## 846. `cs.LG` - 驱动盲点现象：为什么深度序列模型在血糖预测中默认依赖自相关性 [PDF](https://arxiv.org/pdf/2511.20601), [HTML](https://arxiv.org/abs/2511.20601)
### Authors
Heman Shakeri
### Background
论文背景介绍了现有研究中存在一种现象，即深度序列模型在进行血糖预测时没有有效利用与血糖密切相关的临床信息（如胰岛素、饮食和活动），尽管这些因素的生理机制是已知的。这种现象被称为‘驱动盲点’。文章进一步定义了$text{Δ_{驱动}}$，表示多变量模型相对于匹配的一变量基线模型的性能提升。研究表明，这一性能提升通常接近于零。
### Innovation
该研究指出了导致‘驱动盲点’现象的三个因素：架构上的偏见导致自相关性占优势（C1），数据质量差异使驱动变量变得不清晰和混淆（C2），以及生理上的个体差异使得群体模型不够准确（C3）。文章还提出了部分缓解此问题的方法，包括生理特征编码、因果正则化以及个性化模型等。
### Conclusion
研究建议未来的工作应常规报告$text{Δ_{驱动}}$，以防止陷入忽视驱动变量的模型被认为是最先进的误区。
## 847. `cs.LG` - Latent Diffusion Inversion Requires Understanding the Latent Space [PDF](https://arxiv.org/pdf/2511.20592), [HTML](https://arxiv.org/abs/2511.20592)
### Authors
Mingxing Rao,Bowen Qu,Daniel Moyer
### Background
尽管扩散模型已在数据域中的训练数据恢复（``模型反向''）方面得到了广泛研究，但应用于潜在空间生成模型（例如潜在扩散模型LDMs）的反向技术大多忽略了编码器/解码器对和相应的潜在代码。这意味着这些技术没有深入探讨潜在空间中的模式和记忆特性。
### Innovation
该研究发现了两个关键点：（1）扩散模型在潜在代码上的记忆是非均匀的，倾向于在解码器拉回度量的高失真区域过度拟合样本。（2）即使是同一潜在代码，不同的维度对于记忆的贡献也不均匀。研究提出了一种有原则的方法来按每个维度对潜在维度进行排名，识别出对记忆最负责的维度。在计算基于分数的会员推理攻击者的攻击统计时，去除记忆较弱的维度，总体AUC ROC 提升了2.7%，TTP@1% FPR显著增加（6.42%），适用于包括CIFAR-10, CelebA, ImageNet-1K, Pokémon, MS-COCO, Flickr等在内的多种数据集。
### Conclusion
该研究强调了自编码器几何结构对LDM记忆的影响，并为分析基于扩散生成模型的隐私风险提供了新的视角。
## 848. `cs.LG` - E2E-GRec: 图神经网络和推荐系统的端到端联合训练框架 [PDF](https://arxiv.org/pdf/2511.20564), [HTML](https://arxiv.org/abs/2511.20564)
### Authors
Rui Xue,Shichao Zhu,Liang Qin,Guangmou Pan,Yang Song,Tianfu Wu
### Background
图神经网络（GNNs）已经成为了处理图结构数据的强大工具，并广泛应用于推荐系统中，用于捕捉用户-项目和项目-项目间复杂的关系。然而，大多数实际应用中的部署仍然采用两阶段流程：首先离线训练GNN生成节点嵌入，然后将这些嵌入作为静态特征用于推荐系统下游。这种分离架构导致了两个主要局限：（1）计算成本高昂，因为大规模的GNN推理必须反复执行以更新嵌入；（2）缺乏联合优化，即推荐系统的梯度不能直接影响GNN的学习过程，这使得GNN不能最优地服务于推荐任务。
### Innovation
本文提出了一种新颖的端到端训练框架E2E-GRec，将GNN训练与推荐系统统一起来。该框架包含三个关键组件：（i）从大规模跨域异构图中高效地抽样子图，以确保训练的可扩展性和效率；（ii）一种图特征自动编码器（GFAE），作为辅助的自监督任务，以引导GNN学习结构上有意义的嵌入；（iii）结合基于Gradnorm的动态损失平衡的双层特征融合机制，以稳定图感知多任务端到端训练。
### Conclusion
大量离线评估、在线A/B测试（例如，停留时长增加0.133%，用户跳过的平均视频数量减少0.3171%）以及理论分析表明，E2E-GRec 在多个推荐指标方面始终超过了传统方法，带来了显著的改进。
## 849. `cs.LG` - Sparse-to-Field Reconstruction via Stochastic Neural Dynamic Mode Decomposition [PDF](https://arxiv.org/pdf/2511.20612), [HTML](https://arxiv.org/abs/2511.20612)
### Authors
Yujin Kim,Sarah Dean
### Background
许多重要的实际系统，如风场和洋流，是动态的且难以建模。学习它们的动态规律仍然是科学机器学习的核心挑战。动态模式分解(DMD)提供了一种简单、基于数据的近似方法，但其实际应用受限于来自连续场的稀疏/噪声观测数据、对线性近似的依赖以及缺乏系统性的不确定性量化。
### Innovation
我们提出了Stochastic NODE-DMD，这是一种基于概率性的DMD扩展，能够建模连续时间非线性动态，同时保持可解释性。该方法能实现任意坐标上的连续时空重建，并量化预测不确定性。在四个基准测试、一个合成环境和三个基于物理的流场中，与仅从10%观测密度训练的基线相比，它在重建精度上表现更优；通过将学习到的模式和连续时间特征值与真实值对齐，进一步恢复动态结构；最后，在包含多个实例的数据集上，该方法学习到的隐动态概率分布能够保留集合变异性，而非在不同制度上求平均。
### Conclusion
我们的方法解决了稀疏/噪声观测、需要线性近似以及缺乏系统性的不确定性量化的挑战。结果表明，通过Stochastic NODE-DMD，可以提高稀疏观测数据集的重建精度，同时提供可靠的预测不确定性量化，这为实际系统的动态建模提供了一个新的视角。
## 850. `cs.LG` - BrowseSafe: 理解并预防AI浏览器代理中的提示注入 [PDF](https://arxiv.org/pdf/2511.20597), [HTML](https://arxiv.org/abs/2511.20597)
### Authors
Kaiyuan Zhang,Mark Tenenholtz,Kyle Polley,Jerry Ma,Denis Yarats,Ninghui Li
### Background
将人工智能(AI)代理集成到网络浏览器中引入了超出传统网络应用程序威胁模型的安全挑战。先前的研究已识别出提示注入作为新的攻击向量，但其在现实环境中的影响仍不充分理解。
### Innovation
本文研究了提示注入攻击的全景，并综合了一个基于现实HTML负载的攻击基准。基准超越了以往工作，强调了影响现实世界行动而非仅是文本输出的注入，以及呈现复杂性和干扰频率类似于现实世界代理遇到的攻击负载。本文还通过这个基准进行了全面的实证评估，评估现有防御的有效性，并针对前沿的人工智能模型套件。提出了一种多层次的防御策略，包括架构和基于模型的防御，以抵御演变中的提示注入攻击。本文提供了一种通过多层次防御方法设计实用且安全的网络代理的蓝图。
### Conclusion
本文为设计实用且安全的网络代理提供了蓝图，通过多层次防御方法实现纵深防御。
## 851. `cs.LG` - SLMs温度对本地环境下的事件分类影响 [PDF](https://arxiv.org/pdf/2511.19464), [HTML](https://arxiv.org/abs/2511.19464)
### Authors
Marcio Pohlmann,Alex Severo,Gefté Almeida,Diego Kreutz,Tiago Heinrich,Lourenço Pereira
### Background
SOCs和CSIRTs面临着自动化事件分类的压力，而基于云的LLMs的使用带来了成本、延迟和保密风险。因此，研究者探讨了本地执行的SLMs是否能够应对这一挑战。
### Innovation
研究团队评估了21个从1B到20B参数的SLM模型，通过改变温度超参数并在两种不同架构下测量执行时间和精度，发现温度对性能影响不大，而参数数量和GPU容量是决定性因素。
### Conclusion
本研究表明，在本地环境中部署SLMs可以有效进行事件分类，但参数数量和GPU容量对模型性能至关重要，温度参数的重要性相对较低。
## 852. `cs.LG` - Image2Gcode：使用扩散转换器模型的图像到G码生成用于增材制造 [PDF](https://arxiv.org/pdf/2511.20636), [HTML](https://arxiv.org/abs/2511.20636)
### Authors
Ziyue Wang,Yayati Jadhav,Peter Pak,Amir Barati Farimani
### Background
传统的机械设计和制造工作流程通常始于概念设计，随后创建计算机辅助设计（CAD）模型，并通过材料挤出（MEX）打印进行制造。这一过程涉及将CAD几何图形转换为机器可读的G代码的过程，需要进行切片和路径规划。尽管每一步已经很成熟，但对CAD建模的依赖仍然是主要瓶颈，构造特定于对象的3D几何结构非常低效且不适合快速原型制作。即使是小的设计变化通常也需要手动更新CAD软件，使得迭代时间长且难以规模化。
### Innovation
本文引入了Image2Gcode，这是一个端到端的数据驱动框架，绕过了CAD阶段，直接从图像和零件图纸生成打印机准备好的G代码。框架首先从图像中提取逐层结构提示，然后使用G代码序列上的去噪扩散概率模型（DDPM）。通过迭代去噪，模型将高斯噪声转化为可执行的打印轨迹，对应于挤出参数，建立了从视觉输入到原生工具路径的直接映射。通过直接从2D图像生成结构化的G代码，Image2Gcode消除了对CAD或STL中间件的需要，降低了增材制造的入门门槛并加快了从设计到制造的循环时间。
### Conclusion
Image2Gcode支持从简单的草图或视觉参考进行按需原型制作，并与上游2D到3D重建模块集成，以实现从概念到物理产品的自动化流程。这为设计迭代、维修工作流和分布式制造提供了一个灵活且计算高效的方法，推进了设计操作的可访问性。
## 853. `cs.LG` - 自适应霍普菲尔德网络：重新思考关联记忆中的相似性 [PDF](https://arxiv.org/pdf/2511.20609), [HTML](https://arxiv.org/abs/2511.20609)
### Authors
Shurong Wang,Yuqi Pan,Zhuoyang Shen,Meng Zhang,Hongwei Wang,Guoqi Li
### Background
联想记忆模型是与生物智能基本的内容可寻址记忆系统，具有高度可解释性。现有模型通过距离来评估检索质量，但这不能保证检索到的模式与查询有最强关联性，从而可能导致检索不正确。
### Innovation
本文重新定义了查询与其存储记忆模式之间的关系，提出一种变体分布来模型化这种依赖于上下文的生成过程。正确检索应该是返回具有最大后验概率成为查询起源的记忆模式。为此，本文开发了一种新的自适应相似性机制，可以从上下文样本中学习并逼近每个存储模式生成查询的似然性，从而实现正确的检索。实验表明，该机制在多种任务中取得了最先进的性能。
### Conclusion
理论证明表明，根据变体分布，自适应相似性机制适用于三种常见的变体类型，从而实现了最优的正确检索。本文将自适应相似性机制整合进了新型自适应霍普菲尔德网络（A-Hop），实验结果表明其在各类任务中的性能均达到最先进的水平。
## 854. `cs.LG` - Vibe编码能否战胜研究生计算机科学学生？大规模语言模型与人类编码战略规划大赛 [PDF](https://arxiv.org/pdf/2511.20613), [HTML](https://arxiv.org/abs/2511.20613)
### Authors
Panayiotis Danassis,Naman Goel
### Background
由于大型语言模型（LLMs）的迅速发展，AI辅助代码生成已经发生了革命性变化。然而，现有的评估标准主要关注单元测试通过率和语法正确性，这些标准未能充分反映真实世界问题的复杂性，如需要规划、优化和策略性交互。该研究介绍了一个基于实际物流优化问题（投标、收取和交付问题）的多智能体推理驱动基准测试，将竞争性拍卖与容量约束路径规划相结合，以弥补现有评估标准的不足。
### Innovation
该论文创新性地提出了一种基于实际物流优化问题的多智能体推理驱动基准测试，旨在评估LLMs生成的代码是否能够在真实世界中与人类生成的代码竞争。该基准测试要求构建能够（i）在不确定性下进行战略投标和（ii）优化任务规划并最大化利润的智能体。该研究通过使用多种LLMs和不同的提示方法对40个LLMs编码智能体进行了评估，并与之前开发的17个人类编码智能体进行了对比。
### Conclusion
研究结果表明，人类（研究生）编码的智能体在性能上明显优于LLMs编码智能体。大多数LLMs编码智能体在与非常简单的基线对比中表现不佳。当被提示改进人类最优解时，性能最佳的LLMs反而使解决方案变得更差。这些发现突显出LLMs在生成能够在真实世界中有效运行的代码方面的局限性，并促使未来发展更多注重推理驱动代码合成的新评估方法。
## 855. `cs.LG` - ROOT: Robust Orthogonalized Optimizer for Neural Network Training [PDF](https://arxiv.org/pdf/2511.20626), [HTML](https://arxiv.org/abs/2511.20626)
### Authors
Wei He,Kai Han,Hang Zhou,Hanting Chen,Zhicheng Liu,Xinghao Chen,Yunhe Wang
### Background
大规模语言模型（LLMs）的优化仍然是一个关键挑战，尤其是随着模型规模的扩大，优化算法的精准性和训练稳定性会受到负面影响。现有的优化器虽然提高了收敛效率，但仍然存在两个关键鲁棒性问题：正交化精度的维度脆弱性以及异常值噪声导致的敏感性。
### Innovation
作者提出了ROOT，这是一种增强训练稳定性的鲁棒正交化优化器。具体创新点包括：1) 开发了一种尺寸鲁棒的正交化方案，使用自适应牛顿迭代，具有细粒度的系数，以确保不同架构配置下的稳定精度；2) 引入了一种优化鲁棒框架，通过近邻优化抑制异常值噪声，同时保留有意义的梯度方向。
### Conclusion
广泛的实验表明，ROOT相比现有的Muon和基于Adam的优化器在鲁棒性、收敛速度和最终性能方面都取得了显著提升，特别是在噪声和非凸场景中。本研究为开发兼具鲁棒性和精确性的优化器奠定了新的范式，未来将在现代大规模模型训练中发挥重要作用。代码将在以下链接提供：https://...
## 856. `cs.LG` - DiFR：在非确定性环境下进行推理验证 [PDF](https://arxiv.org/pdf/2511.20621), [HTML](https://arxiv.org/abs/2511.20621)
### Authors
Adam Karvonen,Daniel Reuter,Roy Rinberg,Luke Marks,Adrià Garriga-Alonso,Keri Warr
### Background
随着大规模语言模型（LLM）推理需求的增长，确保推理过程正确性变得愈发重要，特别是对于提供方和用户来说。传统的重跑推理过程方法由于存在微小的数字噪声，难以区分正常的变异和实际问题。论文提出了Token-DiFR方法，通过将生成的标记与基于统一随机种子的可信参考实现进行比较，确保推理结果的正确性。
### Innovation
Token-DiFR通过将生成的标记与基于统一随机种子的可信参考实现进行比较来验证推理输出。这个方法通过紧缩抽样种子同步，将有效输出限定在一个范围内，给提供方保留的偏差空间极小，从而降低了额外的成本。此外，论文还提出了Activation-DiFR，一种使用随机正交投影压缩激活并生成紧凑指纹的技术，能够在少至2个输出标记中检测4比特量化，同时减少通信开销。
### Conclusion
Token-DiFR能够在300个输出标记中可靠地检测出4比特量化和其他问题，而Activation-DiFR能够在只是两个输出标记中检测更深的量化，同时通信开销减少了25-75%。论文还发布了与vLLM的开源整合，以加速验证推理技术的实际部署。
## 857. `cs.LG` - Dual-Path Knowledge-Augmented Contrastive Alignment Network for Spatially Resolved Transcriptomics [PDF](https://arxiv.org/pdf/2511.17685), [HTML](https://arxiv.org/abs/2511.17685)
### Authors
Wei Zhang,Jiajun Chu,Xinci Liu,Chen Tong,Xinyue Li
### Background
时空转录组学（ST）是一种在保留空间上下文的情况下测量组织切片中基因表达谱的技术。它揭示了局部基因表达模式和组织异质性，这对于理解疾病发生机制至关重要。然而，ST技术成本高昂，促使人们努力通过全切片图像预测空间基因表达。尽管近年来取得了进步，现有方法仍存在许多局限性，如高阶生物上下文利用不足、过度依赖示例检索以及不充分的异质模态对齐。
### Innovation
本文提出了DKAN（双重路径知识增强对比对齐网络），这是一种新型的网络预测空间分辨率基因表达通过将组织病理学图像和基因表达谱结合，采用生物学导向的方法进行整合。具体来说，DKAN引入了有效的基因语义表示模块，利用外部分子数据库提供额外的生物学洞见，从而提升基因表达预测。进一步地，采用统一的、一站式的对比学习框架，结合对比学习和监督学习消除对外部示例的依赖，同时还具备自适应加权机制。此外，提出了双重路径对比对齐模块，利用基因语义特征作为动态跨模态协调器，以实现有效的异质特征集成。
### Conclusion
通过在三个公开的时空转录组学数据集上进行广泛的实验，DKAN在空间基因表达预测中表现出优于现有模型的性能，建立了新的基准，并为生物和医学研究提供了强有力的工具。
## 858. `cs.LG` - SG-OIF：一种基于稳定性指导的在线影响框架以实现可靠的视觉数据处理 [PDF](https://arxiv.org/pdf/2511.19466), [HTML](https://arxiv.org/abs/2511.19466)
### Authors
Penghao Rao,Runmin Jiang,Min Xu
### Background
在部署深度学习视觉模型时，准确估计训练点对测试预测的影响对于定位噪声数据至关重要。尽管影响函数可以属性化个别训练实例权重增加或删除对模型输出的影响，但在深度学习视觉模型中的实现仍具挑战性。逆曲率计算成本高昂，且训练过程的非站定性使静态近似失效。现有方法使用迭代求解器和低秩替代来降低成本，但离线计算无法跟上训练动态，并且缺乏置信度校准导致易碎的排名错误识别关键实例。
### Innovation
本文提出了稳定性指导的在线影响框架（SG-OIF），这是第一个将算法稳定性视为实时控制器的框架。它(i)通过随机Richardson和预条件Neumann维持轻量级锚点IHVP；(ii) 提出模块化的曲率后端，使用稳定性指导的残差阈值、异常筛选器和置信度调节每个实例的影响得分。实验表明，SG-OIF在多个数据集上对带噪标签和异常检测任务达到了SOTA，特别是在CIFAR-10（20%不对称噪声）中，准确率为91.1%的前1%预测样本，在MNIST上达到了99.8%的AUPR分数。
### Conclusion
实验结果表明，SG-OIF在各种数据集上的噪声标签和异常检测任务中实现了最先进的性能。特别在CIFAR-10（20%不对称噪声）的前1%预测样本中获得了91.1%的准确率，在MNIST中的AUPR得分达到了99.8%，这证明了该框架是在线影响估计的实际控制工具。
## 859. `cs.LG` - stable-pretraining-v1：简化基础模型研究 [PDF](https://arxiv.org/pdf/2511.19484), [HTML](https://arxiv.org/abs/2511.19484)
### Authors
Randall Balestriero,Hugues Van Assel,Sami BuGhanem,Lucas Maes
### Background
基础模型和自我监督学习（SSL）已成为现代AI的核心，但在这一领域，研究仍受到复杂代码库、冗余重实现和扩大实验所带来庞大工程负担的阻碍。
### Innovation
我们提出了一个模块化、可扩展、性能优化的库——stable-pretraining，它基于PyTorch、Lightning、Hugging Face和TorchMetrics构建。与专注于重现当前最佳结果的工具包不同，stable-pretraining 设计用于灵活性和迭代速度，它将自我监督学习的关键实用工具统一在一致且可靠框架中，如探针、坍塌检测指标、数据增强流水线和可扩展的评估规程。中心设计理念是记录一切，使得调试、监控和可复现简单明了。
### Conclusion
通过降低进入门槛同时保持对大规模实验的可扩展性，stable-pretraining旨在加速发现并扩展基础模型研究的可能性。
## 860. `cs.LG` - 基于信息论的自适应结构剪枝方法以实现高效视觉语言模型 [PDF](https://arxiv.org/pdf/2511.19518), [HTML](https://arxiv.org/abs/2511.19518)
### Authors
Zhaoqi Xu,Yingying Zhang,Jian Li,Jianwei Guo,Qiannan Zhu,Hua Huang
### Background
最近的视觉语言模型（VLMs）已经在多模态任务上表现出色，但其不断增加的规模给部署和效率带来了严重挑战。现有压缩方法通常依赖于启发式的重要性度量或经验性剪枝规则，缺乏关于信息保留的理论保证。
### Innovation
我们提出了InfoPrune，一个基于信息论的框架，用于自适应结构压缩。该方法基于信息瓶颈原理，将剪枝视为保留任务相关信息和消除冗余依赖之间的权衡。此外，我们设计了两种互补方案：基于训练的信息损失目标指导的头部剪枝方案和无训练的FFN压缩方案。
### Conclusion
实验结果表明，InfoPrune实现了3.2倍的FLOP减少和1.8倍的加速，且性能几乎没有下降。这为高效的大规模多模态模型奠定了理论和实践上有效的方法。
## 861. `cs.LG` - FAST: 顶点感知频域分布匹配的子集选择 [PDF](https://arxiv.org/pdf/2511.19476), [HTML](https://arxiv.org/abs/2511.19476)
### Authors
Jin Cui(1),Boran Zhao(2),Jiajun Xu(2),Jiaqi Guo(3),Shuo Guan(2),Pengju Ren(1) ((1) State Key Laboratory of Human-Machine Hybrid Augmented Intelligence, National Engineering Research Center for Visual Information and Applications, and Institute of Artificial Intelligence and Robotics, Xi'an Jiaotong University, (2) School of Software Engineering, Xi'an Jiaotong University, (3) School of Mathematical Sciences, Nankai University)
### Background
现有的核心集选择方法要么依赖于基于DNN的技术，受到特定模型参数的限制并引入了架构偏见；要么是非DNN的方法，这些方法依赖于缺乏理论保证的启发式技术。这两种方法都不明确地约束分布等价性，主要是因为连续分布匹配在离散采样中被认为是不适用的。常用的度量标准（如MSE、KL、MMD、CE）不能准确捕捉高阶矩的差异，导致获得的子集效果欠佳。
### Innovation
提出了一种名为FAST的首个非DNN分布匹配的核心集选择框架，将核心集选择任务表示为频域频谱图理论下的约束优化问题，并使用特征函数距离(CFD)来捕获全分布信息。此外，引入了衰减相位解耦CFD来解决原始CFD在中高频区域退化的问题，并设计了一个逐步频率选择策略，以确保高频之前的全局结构得到保持，同时维持样本稀疏性，从而实现更准确的匹配并避免过拟合。
### Conclusion
大量实验表明，FAST显著优于所有评估基准上的现有核心集选择方法，平均准确率提高了9.12%，与基线方法相比，它降低了96.57%的能耗，并实现了2.2倍的平均速度提升，证明了其优异的性能和能效。
## 862. `cs.LG` - 利用多阶段深度学习框架与PKCP-MixUp增强方法进行多期对比增强CT辅助小儿肝肿瘤诊断 [PDF](https://arxiv.org/pdf/2511.19478), [HTML](https://arxiv.org/abs/2511.19478)
### Authors
Wanqi Wang,Chun Yang,Jianbo Shao,Yaokai Zhang,Xuehua Peng,Jin Sun,Chao Xiong,Long Lu,Lianting Hu
### Background
小儿肝肿瘤是儿科最常见的实体肿瘤之一，准确区分良性与恶性以及病理分类对临床治疗至关重要。虽然病理学检查是金标准，但侵入性活检存在局限性：小儿肝脏血流丰富且肿瘤组织脆弱，增加了出血等并发症的风险；此外，年幼且不合作的儿童需要在麻醉下进行活检，增加了医疗成本或心理创伤。尽管已有许多努力将AI应用于临床，但大多数研究尚未充分重视其在小儿肝肿瘤中的重要性。
### Innovation
本文开发了一种基于多阶段深度学习的框架，利用多期对比增强CT进行小儿肝肿瘤的自动诊断。通过引入新的PKCP-MixUp数据增强方法来解决数据稀缺和类别不平衡问题，并训练肿瘤检测模型以提取感兴趣区域，建立二阶段诊断流程以提高诊断性能。该框架填补了小儿专用的DL诊断空白，提供了CT相位选择和模型设计的实用见解，并为精准、可访问的小儿肝肿瘤诊断铺平了道路。
### Conclusion
该框架展示了强大的诊断性能，包括良性亚型分类（AUC=0.915）和恶性亚型分类（AUC=0.979），并通过多种层次的比较分析增强了其实用性和解释性。
## 863. `cs.LG` - 联合学习掩码自动编码器鲁棒黑素细胞样肿瘤分类 [PDF](https://arxiv.org/pdf/2511.19535), [HTML](https://arxiv.org/abs/2511.19535)
### Authors
Ilán Carretero,Roshni Mahtani,Silvia Perez-Deben,José Francisco González-Muñoz,Carlos Monteagudo,Valery Naranjo,Rocío del Amor
### Background
准确诊断黑素细胞样肿瘤（ST）对于确保良好的预后以及避免过度或不足治疗至关重要。表观遗传数据，特别是DNA甲基化，为这一任务提供了宝贵的信息来源。然而，先前的研究假设数据完整，这在实际情况下是不现实的，因为甲基化模式经常包含缺失项，由于覆盖有限和实验伪影所致。
### Innovation
我们的研究挑战了以往的数据完整假设，并引入了ReMAC，它是一种ReMasker的扩展，专门为在完整和不完整数据条件下解决高维数据的分类任务设计。实证研究表明，ReMAC在ST的分层分类中相比竞争的分类方法，表现出强健且稳健的性能。
### Conclusion
ReMAC在实临床数据评估中表现出强劲且稳健的分类性能，相比于竞争方法，提供了更可靠的黑素细胞样肿瘤分类。
## 864. `cs.LG` - 在异构HPC和云环境下的可扩展AI联邦学习框架 [PDF](https://arxiv.org/pdf/2511.19479), [HTML](https://arxiv.org/abs/2511.19479)
### Authors
Sangam Ghimire,Paribartan Timalsina,Nirjal Bhurtel,Bishal Neupane,Bigyan Byanju Shrestha,Subarna Bhattarai,Prajwal Gaire,Jessica Thapa,Sudan Jha
### Background
随着对可扩展和隐私保护的人工智能系统需求的增长，联邦学习（FL）作为一种有望的解决方案出现，它允许在不移动原始数据的情况下进行去中心化的模型训练。与此同时，高性能计算（HPC）和云基础设施的结合提供了巨大的计算能力，但同时也引入了新的复杂性，特别是在处理异构硬件、通信限制和非均匀数据时。
### Innovation
本文提出了一种能够在混合HPC和云环境中高效运行的联邦学习框架。该系统解决了关键挑战，包括系统异构性、通信开销和资源调度，同时保持了模型的准确性及数据隐私。通过在混合测试床上的实验，展示了在非独立同分布（非-IID）数据分布和不同硬件条件下具有良好的可扩展性、容错性和收敛性。
### Conclusion
这些结果表明联邦学习作为一种实用方法，在现代分布式计算环境中构建可扩展的AI系统的潜力巨大。
## 865. `cs.LG` - CycleChemist: 一种双管齐下的机器学习框架，用于有机光伏材料发现 [PDF](https://arxiv.org/pdf/2511.19500), [HTML](https://arxiv.org/abs/2511.19500)
### Authors
Hou Hei Lam,Jiangjie Qiu,Xiuyuan Hu,Wentao Li,Fankun Zeng,Siwei Fu,Hao Zhang,Xiaonan Wang
### Background
有机光伏（OPV）材料为可持续能源生成提供了有希望的路径，但其开发受限于难以找出具有高功率转换效率（PCE）的高性能供体-受体对。现有设计策略通常只关注供体或受体一方，缺乏综合模拟两者的统一方法。现有数据显示，通过利用现有数据集进行预测建模并结合生成分子设计，可以开发出具有高性能的OPV材料。
### Innovation
本工作引入了一种结合预测建模与生成分子设计的双机器学习框架——CycleChemist，用于OPV发现。该框架构建了最大的有机光伏供体-受体数据集，以及用于预测材料是否具有良好光伏特性的有机光伏分类器（OPVC）。同时，框架还包含分子轨道能量估计器（MOE2）和光伏性能预测器（P3），并引入了材料生成预训练变换器（MatGPT），以生成合成可访问的有机半导体。
### Conclusion
通过将分子表示学习与性能预测相结合，我们的框架推进了数据驱动的高性能OPV材料发现。
## 866. `cs.LG` - 超越EAR眨眼：稳定眼睑角度度量在驾驶员疲劳检测及数据增强中的应用 [PDF](https://arxiv.org/pdf/2511.19519), [HTML](https://arxiv.org/abs/2511.19519)
### Authors
Mathis Wolter,Julie Stephany Berrio Perez,Mao Shan
### Background
可靠地检测驾驶员疲劳对于提高道路安全和支持先进的驾驶员辅助系统（ADAS）至关重要。传统的二元眼睛状态估计器或基于2D的指标，如眼缘比率（EAR），在面对摄像头角度变化时不稳定。本研究提出了一种新的、可重复使用的眼睑角度（ELA）度量，它是一个从3D面部特征点得出的指标，能提供稳定的几何描述，并且对摄像头角度的变化是鲁棒的。
### Innovation
该研究创新性地设计了一个基于ELA的眼睑闭合检测框架，该框架能够提取与疲劳水平相关的时序特征。此外，研究还利用ElA信号，在Blender 3D中使模型动画化，创建了一系列可控噪声、摄像头视角和眨眼动态的合成数据集。实验结果表明，ELA在不同视角下具有更低的方差，并实现了精确的眼睑检测。同时，合成数据增强扩展了用于疲劳识别的训练数据的多样性。
### Conclusion
研究发现ELA不仅能作为可靠的生物测量指标，还能作为生成驾驶员状态监控中的可扩展数据集的强大工具。
## 867. `cs.LG` - 多模态LLM在跨境领域推广以实现全球光伏评估 [PDF](https://arxiv.org/pdf/2511.19537), [HTML](https://arxiv.org/abs/2511.19537)
### Authors
Muhao Guo,Yang Weng
### Background
分布式光伏(PV)系统的快速发展给电网管理带来了挑战，因为许多安装情况未被记录。虽然卫星影像具有全球覆盖的优势，但传统的卷积神经网络(CNNs)和U-Net等计算机视觉(CV)模型需要大量标注数据，并且难以在不同地区泛化。
### Innovation
该研究探討了使用多模态大型语言模型（LLM）进行全球光伏评估的跨境泛化能力。通过结构化提示和微调，该模型将检测、定位和量化整合到一个统一框架中。使用$triangle$F1指标进行跨区域评估表明，所提出的模型在未见区域的性能下降最小，优于传统的CV和变压器基线。
### Conclusion
这些结果突显了多模态LLM在领域转移下的鲁棒性，并显示了其在具有可扩展性、转移性和可解释性的全球光伏地图绘制方面的潜力。
## 868. `cs.LG` - 神经品种的亚历山大-赫什洛夫定理 [PDF](https://arxiv.org/pdf/2511.19703), [HTML](https://arxiv.org/abs/2511.19703)
### Authors
A. Massarenti,M. Mella
### Background
我们研究多项式神经网络的神经品种，并在单输出情况下完全刻画了它们达到预期维度的条件。
### Innovation
我们证明了多输出架构的无缺陷性和全局可识别性。
### Conclusion
本研究为多项式神经网络的神经品种提供了完全的刻画，并通过这一刻画证明了多输出架构的无缺陷性和全局可识别性，补充了亚历山大-赫什洛夫定理在神经网络领域的应用。
## 869. `cs.LG` - 朝向未来基于空间的可扩展人工智能基础设施系统设计 [PDF](https://arxiv.org/pdf/2511.19468), [HTML](https://arxiv.org/abs/2511.19468)
### Authors
Blaise Agüera y Arcas,Travis Beals,Maria Biggs,Jessica V. Bloom,Thomas Fischbacher,Konstantin Gromov,Urs Köster,Rishiraj Pravahan,James Manyika
### Background
如果人工智能（AI）被视为一种基础性的通用技术，我们应预测对AI计算和能源的需求将持续增长。鉴于太阳是太阳系中最大的能源来源，研究者探讨了未来AI基础设施如何最高效地利用这一能源的可能性。本文研究了一种在空间中实现机器学习的可扩展计算系统，利用配备太阳电池板的卫星群、自由空间光学进行的卫星间链路以及Google张量处理单元（TPU）加速芯片。这种设计旨在促进高带宽、低延迟的卫星间通信，同时通过队形飞行方式提高了系统的灵活性和实用性。
### Innovation
本文创新地提出了一种基于空间中的卫星群构建用于机器学习计算的可扩展系统。该系统通过自由空间光学链路实现高带宽、低延迟的卫星间通信，并使用Google TPU加速芯片来提高计算效率。此外，研究还强调了通过高精度的机器学习模型控制大规模星座的方法，并展示了使用Trillium TPU芯片的耐辐射测试数据，证明其适用于长期任务。
### Conclusion
研究者通过分析指出，未来将AI技术应用于空间中的计算系统是可行的。随着低地球轨道（LEO）发射成本的逐渐降低，发射成本将成为系统成本的重要组成部分。预计到2030年代中，LEO发射成本可能降至每千克$frac{1}{200}$美元以下。
## 870. `cs.LG` - Think First, Assign Next (ThiFAN-VQA): A Two-stage Chain-of-Thought Framework for Post-Disaster Damage Assessment [PDF](https://arxiv.org/pdf/2511.19557), [HTML](https://arxiv.org/abs/2511.19557)
### Authors
Ehsan Karimi,Nhut Le,Maryam Rahnemoonfar
### Background
及时而准确地评估自然灾害后的损害对于有效的应急响应和恢复至关重要。近年来，基于人工智能的框架已经发展起来，利用无人机拍摄的大量航拍图像进行分析，以提供快速的行动建议。然而，创建和标注训练这些模型的数据集既昂贵又耗时，导致数据集在规模和多样性方面受限。此外，大多数现有方法依赖于传统基于分类的框架，这限制了它们在无需额外数据收集或模型重新训练的情况下提供新的信息的能力。使用基于情境学习（ICL）的预训练生成模型可以提供灵活的开放性答案空间，但这些模型通常生成虚构的输出，或产生缺乏特定领域相关性的通用响应。
### Innovation
提出了一种名为ThiFAN-VQA的双阶段推理框架，以解决现有技术的局限性。ThiFAN-VQA使用链式推理（CoT）提示和ICL生成结构化的推理轨迹，使在有限监督下具有可解释的推理成为可能。随后的答案选择模块评估生成的响应，并选择最连贯和上下文相关的答案，从而提高模型性能。通过集成自定义的信息检索系统、领域特定的提示和推理指导的答案选择，ThiFAN-VQA在零样本和监督方法之间架起桥梁，结合了灵活性和一致性。
### Conclusion
在洪水和飓风影响地区的基于无人机的数据集FloodNet和RescueNet-VQA上进行的实验表明，ThiFAN-VQA在实际灾害后损害评估任务方面具有优越的准确度、可解释性和适应性。
## 871. `cs.LG` - SPQR: 一种现代文本到图像扩散模型安全对齐方法的标准基准 [PDF](https://arxiv.org/pdf/2511.19558), [HTML](https://arxiv.org/abs/2511.19558)
### Authors
Mohammed Talha Alam,Nada Saadi,Fahad Shamshad,Nils Lukas,Karthik Nandakumar,Fahkri Karray,Samuele Poppi
### Background
文本到图像的扩散模型可能会生成包含版权、不安全或私人信息的内容。安全对齐旨在抑制特定概念，但评价通常不测试安全是否在部署后常规应用的良性下游微调过程中保持良好状态（例如LoRA个性化、风格或领域适配器）。以往的研究较少关注安全性的稳定性和持久性。
### Innovation
引入了SPQR基准（Safety-Prompt adherence-Quality-Robustness），这是一种单一评分标准，旨在提供一种标准化、可重复的框架，用于评估安全对齐的扩散模型在良性微调下是否能够保持安全、有用和稳健性。SPQR通过报告单一的排行榜分数，使比较更加便捷。
### Conclusion
SPQR基准在多语言、领域特定和分布外分析中进行了评估，并提供了类别级别的拆解，以识别在良性微调后哪些安全对齐会失败。最终展示了SPQR作为一个简洁而全面的基准，用于评估文本到图像模型中的安全对齐技术。
## 872. `cs.LG` - 为SGD设计预条件因子：局部正则化、噪声阈值和盆地稳定性 [PDF](https://arxiv.org/pdf/2511.19716), [HTML](https://arxiv.org/abs/2511.19716)
### Authors
Mitchell Scott,Tianshi Xu,Ziyuan Tang,Alexandra Pichette-Emmons,Qiang Ye,Yousef Saad,Yuanzhe Xi
### Background
在训练的后期阶段，随机梯度下降（SGD）经常会因为非各向同性的曲率和梯度噪声而变得缓慢。
### Innovation
该文分析了由对称正定矩阵M诱导的几何下的预条件SGD，推导了收敛率和随机噪声阈值都由M依赖的数量（即闵可夫斯基度量下的有效条件数和噪声水平的乘积）控制的边界。对于非凸目标，建立了与预条件因子相关的盆地稳定性保证：当光滑性和盆地大小使用M-范数进行度量时，迭代始终位于良好行为局部区域的概率具有明确的下限。此视角特别适用于科学机器学习（SciML），其中在随机更新下的小训练损失与物理准确度、数值稳定性以及约束满足密切相关。该框架适用于对角/自适应预条件因子和曲率感知预条件因子，并提供了一个简单的设计原则：选择M以改善局部条件并减弱噪声。
### Conclusion
实验表明，该方法预测了速率-噪声阈值行为，在二次诊断和三个SciML基准测试中得到验证。
## 873. `cs.LG` - Agint：软件工程代理的智能图形编译 [PDF](https://arxiv.org/pdf/2511.19635), [HTML](https://arxiv.org/abs/2511.19635)
### Authors
Abhi Chivukula,Jay Somasundaram,Vijay Somasundaram
### Background
基于LLM的编码代理正在变得越来越普遍，但仍然面临上下文管理、延迟、可靠性和可重复性及扩展性等挑战。
### Innovation
Agint 提出了一种代理图形编译器、解析器和运行时，它逐步和分层次地将自然语言指令转换为带类型、效应感知的代码有向无环图(DAG)。Agint 引入了基于语义图变换的明确类型底层设定，并结合即时编译（JIT）和函数的混合 LLM 运行时。这使得图形可以动态精细、可重复和可优化执行、推测性评估，并且与现有的开发者工具具有互操作性。
### Conclusion
Agint 通过层次编译支持可扩展的图形编辑，同时图形结构支持可重复性和高效的并行生成。Agint 提供了一种组合式的类unix工具链：dagify（DAG编译器）、dagent（混合 JIT 运行时）、schemagin（模式生成器）和 datagin（数据转换器），可实现实时、低延迟的代码和数据流创建。通过 Agint CLI，人类开发者和编码代理可以细化图形，而非技术用户可以使用 Agint Flow GUI 进行可视化编辑、会话细化和调试，从而促进原型到生产代码的快速迭代与部署，同时将自然语言、编译方法和开发者工具相结合，使大规模的编码代理能够实现可组合化和团队导向。
## 874. `cs.LG` - 任意目标函数下的优化与正则化 [PDF](https://arxiv.org/pdf/2511.19628), [HTML](https://arxiv.org/abs/2511.19628)
### Authors
Jared N. Lakhani,Etienne Pienaar
### Background
本文探讨了将马尔可夫链蒙特卡罗（MCMC）方法应用于任意目标函数时的局限性，重点关注一种交替使用Metropolis-Hastings和吉布斯采样的两阶段MCMC框架。虽然这类方法通常被认为能够实现数据驱动的正则化，但研究表明，其性能高度依赖于所使用的似然形式的尖锐程度。
### Innovation
文章通过引入一个锐度参数，并探索目标函数成比例的替代似然形式，揭示了似然峰度对内插性能和从训练数据中推断出的正则化程度的影响。此外，通过对极端似然度锐度对经典纸牌游戏黑杰克的任意目标函数的影响进行分析，提出了一个结合迭代优化步骤的混合方法，使其性能几乎与原始MCMC框架相同，表明过度的似然度锐度将后验质量集中在一个主要模式上。
### Conclusion
相关研究结论表明，似然函数的锐度对通过MCMC框架进行的正则化过程影响显著，而在经典纸牌游戏黑杰克中的极端似然度锐度对任意目标函数的影响分析表明，过度的似然度锐度可导致后验质量高度集中在单一主要模式。最终，提出的混合方法实现了与原始MCMC框架类似的表现。
## 875. `cs.LG` - LoRA-Adapted Embedding Models for Clinical Cardiology Text Representation [PDF](https://arxiv.org/pdf/2511.19739), [HTML](https://arxiv.org/abs/2511.19739)
### Authors
Richard J. Young,Alice M. Matthews
### Background
临床自然语言处理需要特定领域的文本嵌入，但不同模型架构在该领域的系统性比较仍然有限。
### Innovation
研究评估了通过低秩适应（LoRA）微调的10种基于变换器的嵌入模型在心脏病学中的性能，特别关注了编码器仅架构，尤其是BioLinkBERT，它们在领域特定性能上优于更大的解码器模型，同时所需计算资源更少。这一发现挑战了更大语言模型定性地产生更好领域嵌入的假设，为临床自然语言处理系统的开发提供了实用指导。
### Conclusion
所有模型、训练代码和评估数据集均可公开访问，以支持医学信息学中的可重复研究。
## 876. `cs.LG` - 地理分区中的个体与群体公平性 [PDF](https://arxiv.org/pdf/2511.19722), [HTML](https://arxiv.org/abs/2511.19722)
### Authors
Ilya O. Ryzhov,John Gunnar Carlsson,Yinchu Zhu
### Background
社会经济隔离在学区划分和其他情境中时常发生，导致某些群体在这特定的区域中被高估或低估。这种现象与机会和结果的不平等密切相关。作者将这一问题形式化为一个新的地理分区问题，其中人口异质性是必要的，应在每个设施中确保每个群体的公平代表。
### Innovation
作者证明了最优解是加权 Voronoi 图的一个新颖推广，并提出了一种简单且高效的算法来计算它，从而解决了 Dvoretzky 等人 (1951) 以来的一个开放问题。通过一个包含七个人口群体和78个区域办公室的真实案例研究，展示了该方法的有效性和实际启示潜力。
### Conclusion
该研究表明，在地理分区中实现个体与群体的公平性是可行的，并具备现实世界的应用价值。
## 877. `cs.LG` - CAMformer：关联记忆即所有你所需 [PDF](https://arxiv.org/pdf/2511.19740), [HTML](https://arxiv.org/abs/2511.19740)
### Authors
Tergel Molom-Ochir,Benjamin F. Morris,Mark Horton,Chiyue Wei,Cong Guo,Brady Taylor,Peter Liu,Shan X. Wang,Deliang Fan,Hai Helen Li,Yiran Chen
### Background
变换器模型面临由于注意力机制包含的二次复杂度的密集相似度计算而产生的可扩展性挑战。为解决这一问题，研究人员提出了CAMformer，这是一种新型加速器，重新解释注意力作为联想存储操作，并采用电压域二值注意力内容可寻址存储器（BA-CAM）来计算注意力分值。
### Innovation
CAMformer 通过模拟电荷共享实现常数时间相似度搜索，将数字算术替换为物理相似度感知。此外，CAMformer 融合了层次化的两级 top-k 筛选、流水线执行和高精度上下文化，以实现算法准确性和架构效率的双重提升。
### Conclusion
在BERT 和Vision Transformer工作负载上评估，CAMformer 在能效、吞吐量和面积方面分别超过最先进的加速器10倍以上、4倍以上和6-8倍，同时保持接近于无损的准确性。
## 878. `cs.LG` - 大规模社区意识网络生成 [PDF](https://arxiv.org/pdf/2511.19717), [HTML](https://arxiv.org/abs/2511.19717)
### Authors
Vikram Ramavarapu,João Alfredo Cardoso Lamy,Mohammad Dindoost,David A. Bader
### Background
社区检测或网络聚类用于识别网络中的潜在社区结构。由于现实世界网络中缺乏标记的真实标签，评估这些算法面临着重大挑战。因此，研究人员使用合成网络生成器来生成带有真实标签社区的网络。RECCS 是一种算法，它接受一个网络及其聚类作为输入，并通过模块化的管道生成合成网络。每生成一个真实的聚类，都保留了输入聚类的关键特征，包括连接性、最小度以及度序列分布。
### Innovation
我们提出了两种增强版本：RECCS+ 和 RECCS++。RECCS+ 维持了算法对原始 RECCS 的忠诚度，通过引入协调各算法组件的指挥官来进行并行化，并使用多线程技术。RECCS++ 在此基础上进行了额外的算法优化，实现了进一步的加速。实验结果表明，在基准数据集上，RECCS+ 和 RECCS++ 分别实现了最多 49 倍和 139 倍的加速，且 RECCS++ 的额外性能提升涉及轻微的准确度损失。
### Conclusion
RECCS++ 现在可以扩展到具有超过 1 亿个节点和接近 20 亿个边的网络。
## 879. `cs.LG` - 整合RCT，RWD，AI/ML和统计学：下一代证据合成 [PDF](https://arxiv.org/pdf/2511.19735), [HTML](https://arxiv.org/abs/2511.19735)
### Authors
Shu Yang,Margaret Gamalo,Haoda Fu
### Background
尽管随机对照试验（RCTs）一直是临床证据的基础，但其高昂的成本、漫长的周期以及严格的入组标准限制了其效果和外部有效性。相比之下，虽然以前真实世界数据（RWD）在确立因果关系方面被认为不够可靠，但现在其在生成真实世界证据（RWE）方面的重要性已被认可。与此同时，人工智能和机器学习（AI/ML）在整个药物研发过程中被越来越广泛地应用，提供了可扩展性和灵活性，但也带来了传统统计方法无法面对的在可解释性和严谨性方面的挑战。
### Innovation
本文提出，未来的证据生成不应依赖于RCTs与RWD之间的选择，或统计学与AI/ML之间的对立，而是需要将其进行原则性的整合。为此，需要建立一个因果导向的方法路线图，明确推论目标，使假设变得更加清晰，并确保关于权衡的透明度。文章强调了整合性证据合成的关键目标，包括将RCT结果推广到更广泛的人群、在RCT中嵌入AI辅助分析、设计混合对照试验以及将短期RCT与长期RWD相结合。文章还指出了未来在隐私保护分析、不确定性量化以及小样本方法等方面的发展方向。
### Conclusion
通过结合统计严谨性与AI/ML的创新，整合方法可以产生稳健、透明且政策相关的证据，成为现代监管科学的关键组成部分。
## 880. `cs.LG` - 合成数据：AI对抗Android恶意软件的新武器 [PDF](https://arxiv.org/pdf/2511.19649), [HTML](https://arxiv.org/abs/2511.19649)
### Authors
Angelo Gaspar Diniz Nogueira,Kayua Oleques Paim,Hendrio Bragança,Rodrigo Brandão Mansilha,Diego Kreutz
### Background
Android设备数量不断增加，而恶意软件的演变速度也在加快，预计到2024年样本量将超过3500万。这突显了有效检测方法的重要性。攻击者现在使用人工智能创建复杂多变的恶意软件，这些恶意软件能够轻易地避开传统的检测技术。尽管机器学习在恶意软件分类方面显示出了潜力，但其成功依赖于获取和标记最新、高质量数据集的能力。获取和标记真实恶意软件样本的稀缺性和成本导致产生了在恶意软件检测中开发稳健模型的重大挑战。
### Innovation
本文提出了一种名为MalSynGen的方法论，该方法使用条件生成对抗网络（cGAN）生成合成表数据。这种数据保留了真实数据的统计特性，并提高了Android恶意软件分类器的性能。
### Conclusion
我们的实验表明，MalSynGen能够跨不同数据集进行推广，提供了一种解决恶意软件检测中数据过时和质量低的问题的可行方案。
## 881. `cs.LG` - CropVLM: 学习缩放以提升细粒度的视觉语言感知 [PDF](https://arxiv.org/pdf/2511.19820), [HTML](https://arxiv.org/abs/2511.19820)
### Authors
Miguel Carvalho,Helder Dias,Bruno Martins
### Background
视觉语言模型（VLMs）在需要精细图像理解的任务（如场景文本识别或文档分析）中往往表现不佳，这主要是由于感知局限性和视觉碎片化的问题。为了应对这些挑战，我们提出了CropVLM作为一种外部低成本方法来增强模型性能，从而使其能够动态地聚焦于相关图像区域，增强其对细小细节的捕捉能力。
### Innovation
CropVLM 使用强化学习进行训练，无需使用人类标注的边界框作为监督信号，也无需昂贵的合成评估。该模型仅需训练一次即可与开源及专有 VLMs 配合使用以提高其性能。此方法在需要高分辨率图像理解的任务上取得了显著改进，特别是在目标 VLM 之外的基准测试上，这种方法无需对或微调 VLM，从而避免了灾难性遗忘。
### Conclusion
我们的方法在要求高分辨率图像理解的任务（尤其是对于目标 VLM 的领域外基准测试）中表现出显著的性能提升，同时无需对或微调 VLM，因此可以避免灾难性遗忘。
## 882. `cs.LG` - 一个集成了数据集成的可解释和可争议的基于代理的建模框架，用于可解释和可争议的政策设计 [PDF](https://arxiv.org/pdf/2511.19726), [HTML](https://arxiv.org/abs/2511.19726)
### Authors
Roberto Garrone
### Background
多智能体系统通常在反馈、适应性和非稳态环境下运行，但许多仿真研究中仍使用静态决策规则和固定控制参数。本文探讨了多智能体系统在动态环境下的学习和适应性控制问题。
### Innovation
该研究引入了一个通用的自适应多智能体学习框架，该框架包含四个方面：（一）区分静态与自适应代理和固定与自适应系统参数的四种动态模式；（二）信息论诊断方法（熵率、统计复杂性和预测信息），以评估可预测性和结构；（三）结构性因果模型以明确干预语义；（四）基于总体或样本数据生成代理级先验的方法；（五）无监督方法以识别新兴的行为模式。该框架提供了一个跨领域架构，用于分析学习智能体和适应性控制如何共同塑造系统轨迹，使其能够系统地比较非平衡、振荡或漂移动态的稳定性和性能。
### Conclusion
数学定义、计算操作符和实验设计模板为开发可解释和可争议的多智能体决策过程提供了结构化方法，该过程能够分析智能体和自适应控制如何共同塑造系统轨迹，并跨非平衡、振荡或漂移动态系统提供系统比较稳定性、性能和可解释性的能力。
## 883. `cs.LG` - ω-正则目标和约束条件下的强化学习 [PDF](https://arxiv.org/pdf/2511.19849), [HTML](https://arxiv.org/abs/2511.19849)
### Authors
Dominik Wagner,Leon Witzman,Luke Ong
### Background
强化学习通常依赖于标量奖励，并且奖励的表达能力有限，难以包含诸如时间、条件或安全关键的目标，也可能会导致奖励操纵。因此，通过使用更通用的ω-正则目标，可以更精确地指定丰富的行为特性，克服上述限制。然而，仅通过单一标量（无论是奖励还是满足概率）来度量性能掩盖了具有可接受风险水平的环境中可能会产生的安全与性能之间的权衡。
### Innovation
本文通过结合ω-正则目标和显式的约束，实现了安全要求和优化目标的分开处理，开发了一个基于线性规划的模型化建模强化学习算法。此算法在极限情况下能够最大化满足ω-正则目标的概率，同时满足ω-正则约束。此外，还建立了与受限极限平均问题的转换，并保证了最优性。
### Conclusion
本文提出了通过引入ω-正则目标和约束来同时克服强化学习的两个限制的算法，解决了在可接受风险水平下安全与性能之间的权衡问题，同时确保算法在处理特定阈值内的约束时仍然能保持最优性能。
## 884. `cs.LG` - 雷达杂波下复值VAE离群点检测的空间特征度量 [PDF](https://arxiv.org/pdf/2511.19805), [HTML](https://arxiv.org/abs/2511.19805)
### Authors
Y. A. Rouzoumka,E. Terreaux,C. Morisseau,J.-P. Ovarlez,C. Ren
### Background
本文调查了复值变分自编码器（CVAE）在复杂雷达环境中的雷达离群点（OOD）检测能力。研究者提出了几种检测度量标准，包括CVAE的重构误差（CVAE-MSE）、基于潜在空间的得分（如马氏距离和Kullback-Leibler散度，KLD），并与经典的ANMF-Tyler检测器（ANMF-FP）进行了比较。所有这些检测器在合成和实验雷达数据上的性能被分析，以评估它们的优点和弱点。
### Innovation
提出了复值变分自编码器（CVAE）的几种检测度量标准，包括重构误差、马氏距离和Kullback-Leibler散度，并将它们与经典的ANMF-Tyler检测器进行了对比。分析了所有这些检测器在雷达数据上的性能，以展示它们各自的优势和劣势。
### Conclusion
所有检测器在合成和实验雷达数据上的性能被分析，展示了各个检测器的优点和弱点，表明提出的方法在雷达复杂环境中进行OOG检测的有效性和适用性。
## 885. `cs.LG` - 通过提示语义空间优化实现无训练生成高保真多样图像 [PDF](https://arxiv.org/pdf/2511.19811), [HTML](https://arxiv.org/abs/2511.19811)
### Authors
Debin Meng,Chen Jin,Zheng Gao,Yanran Li,Ioannis Patras,Georgios Tzimiropoulos
### Background
文本到图像的扩散模型中的图像多样性的低多样性现状依然存在挑战。低多样性的模型往往产生重复输出，增加了采样的冗余度，阻碍了创意探索并限制了下游应用。现有的增异数量化的尝试，如噪音重采样、提示重写或基于引导的操作，仍可能收敛到主导模式或引入图像质量降低的偏差。
### Innovation
我们提出了无需训练且通用的模块Token-Prompt嵌入空间优化(TPSO)，该模块通过引入可学习参数探索令牌嵌入空间中未被充分代表的区域，从而降低模型倾向于重复从学习分布中的强模式产生样本的倾向。同时，提示级的空间提供了一个全局语义约束，可以调节分布偏移，防止质量下降同时保持高保真度。
### Conclusion
详尽的实验在MS-COCO上及三个扩散模型框架上显示，TPSO显著增强了生成多样性，提高了基线性能1.10到4.18分，而没有牺牲图像质量。代码将在接受后发布。
## 886. `cs.LG` - 混合类型数据聚类方法的比较研究 [PDF](https://arxiv.org/pdf/2511.19755), [HTML](https://arxiv.org/abs/2511.19755)
### Authors
Badih Ghattas,Alvaro Sanchez San-Benito
### Background
聚类在无监督学习中被广泛使用，用于在数据集中找到具有同质性的观察组。然而，聚类混合型数据仍然是一个挑战，因为现有的方法大多数不适用于这种任务。本研究综述了这些方法的现状，并使用多种模拟模型进行了比较。所比较的方法包括基于距离的方法（k-原型、PDQ、凸k-均值）和基于概率的方法（KAMILA、贝叶斯网络混合模型和潜在类别模型）。通过改变一些实验因子（如聚类的数量、聚类重叠、样本大小、维度、数据集中连续变量的比例以及聚类分布）来探讨不同方法在各种场景下的表现。
### Innovation
该研究综述了当前在处理混合型数据聚类方面的先进方法，并通过多种模拟模型进行了比较分析，提供了不同方法在不同场景下的表现见解。此外，研究还强调了聚类重叠程度、数据集中连续变量的比例和样本大小对表现的影响，并展示了KAMILA、潜在类别模型和k-原型方法在调整兰德指数（ARI）方面的最好表现。
### Conclusion
研究发现聚类重叠程度、数据集中连续变量的比例和样本大小对聚类方法的表现有显著影响。当变量之间存在强烈交互且与聚类成员显式相关时，所有评估的方法都没有表现出令人满意的性能。实验结果显示KAMILA、潜在类别模型和k-原型方法在调整兰德指数（ARI）方面表现最好。所有方法在R语言中都是可用的。
## 887. `cs.LG` - KOM: 用于膝关节骨关节炎精准管理的多智能体人工智能系统 [PDF](https://arxiv.org/pdf/2511.19798), [HTML](https://arxiv.org/abs/2511.19798)
### Authors
Weizhi Liu,Xi Chen,Zekun Jiang,Liang Zhao,Kunyuan Jiang,Ruisi Tang,Li Wang,Mingke You,Hanyu Zhou,Hongyu Chen,Qiankun Xiong,Yong Nie,Kang Li,Jian Li
### Background
膝关节骨关节炎（KOA）影响全球超过6亿人，与显著的疼痛、功能受损和残疾有关。虽然个性化的多学科干预有可能减缓疾病进展并提高生活质量，但通常需要大量医疗资源和专业技能，这使得在资源有限的环境中难以实施。为应对这一挑战，我们开发了KOM，这是一种多智能体系统，旨在自动化KOA评估、风险预测和治疗处方。该系统在临床路径中协助医生执行关键任务，并根据个体患者特征、疾病状态、风险因素和禁忌症生成个性化的管理计划。
### Innovation
KOM通过多智能体系统自动化KOA的评估、风险预测和治疗处方，与多个通用大型语言模型相比，在影像分析和处方生成方面表现出更好的性能。随机三组模拟研究进一步表明，KOM与医生协作可以减少总共41.5%的诊断和计划时间，并且比单独使用两者的方法能提供更高质量的治疗效果。
### Conclusion
这些发现表明KOM可以帮助促进KOA的自动化管理。集成到临床工作流程中，KOM有潜力提高护理效率。KOM的模块化架构也可能为开发其他慢性疾病的AI辅助管理系统提供有价值的知识。
## 888. `cs.LG` - AI代理供应链中跨AI模型行为后门检测的泛化 [PDF](https://arxiv.org/pdf/2511.19874), [HTML](https://arxiv.org/abs/2511.19874)
### Authors
Arun Chowdary Sanna
### Background
随着AI代理在企业工作流程中扮演更重要的角色，它们对共享工具库和预训练组件的依赖性带来了重大的供应链漏洞。尽管前人工作已经展示了单一LLM架构中的行为后门检测，但跨不同LLM的一致性检测仍然是未探索的关键问题，对于使用多个AI系统的组织具有严重的安全意义。
### Innovation
本文首次系统性地研究了跨LLM的行为后门检测，并评估了六个生产级别的LLM模型（GPT-5.1、Claude Sonnet 4.5、Grok 4.1、Llama 4 Maverick、GPT-OSS 120B、DeepSeek Chat V3.1）之间的泛化能力。通过1,198个执行痕迹和36次跨模型实验，研究表明单模型检测器在训练分布内准确率为92.7%，而跨不同LLM的准确率仅为49.2%，存在达43.4个百分点的泛化差距，相当于随机猜测水平。进一步分析发现，这一差距来源于模型特有的行为特征，特别是在时间特征方面的变异系数超过0.8。研究还展示了基于模型感知的检测方法，将模型身份作为额外特征可以实现普遍的90.6%准确率。
### Conclusion
研究结果表明，针对不同LLM模型的行为后门检测存在显著的泛化差距，基于模型身份的检测方法能够有效提高泛化能力。作者还公开了多LLM数据集和检测框架，以促进可重复的研究。
## 889. `cs.LG` - 兼听则明：通过将视觉理解集成到音频语言模型中进行抑郁症检测的多模态LLM [PDF](https://arxiv.org/pdf/2511.19877), [HTML](https://arxiv.org/abs/2511.19877)
### Authors
Xiangyu Zhao,Yaling Shen,Yiwen Jiang,Zimu Wang,Jiahe Liu,Maxmartwell H Cheng,Guilherme C Oliveira,Robert Desimone,Dominic Dwyer,Zongyuan Ge
### Background
抑郁症是全球最常见的精神健康疾病之一。近年来，多模态数据（如语音、视频和笔记文本）被越来越多地用于开发辅助抑郁症评估的人工智能系统。大型语言模型进一步促进了这一领域的发展，因为它们具有强大的语言理解和泛化能力。然而，传统的LLM仍然主要关注文本，并且无法处理音频和视觉模态中丰富的非言语线索，这些线索在心理健康评估中是至关重要的组成部分。尽管多模态LLM提供了有希望的方向，但很少有LLM专门为心理健康应用打造。因此，需要一个新的多模态LLM框架来进行抑郁症检测。
### Innovation
提出了一种新颖的多模态LLM框架，将视觉理解集成到音频语言模型中，并在时间戳级别对音频-视觉特征进行对齐。这种细粒度对齐提高了跨模态的时间动态建模能力，同时减少了大量训练数据和计算资源的需求。实验与DAIC-WoZ数据集上的结果表明，该模型在单模态方法和先前的多模态方法上表现出色。此外，所提出的框架可以进一步整合其他生理信号，为进一步扩大精神健康的临床应用铺平了道路。
### Conclusion
实验结果证明了所提模型的有效性和高效性，表明通过在音频语言模型中集成视觉理解，可以有效提升抑郁症检测的效果。同时，该框架具有良好的扩展性，支持对未来进一步的生理信号整合，为更广泛的临床应用提供了可能。
## 890. `cs.LG` - MAPS: 通过模块级亲近度调度保留视觉-语言表示以获得更好的视觉-语言-行动泛化 [PDF](https://arxiv.org/pdf/2511.19878), [HTML](https://arxiv.org/abs/2511.19878)
### Authors
Chengyue Huang,Mellon M. Zhang,Robert Azarcon,Glen Chou,Zsolt Kira
### Background
视觉-语言-行动（VLA）模型继承了强先验知识，但简单的微调可能会破坏这些表示，损害泛化能力。现有的解决方案要么过度约束适应，要么忽视VLA组件的不同角色。
### Innovation
提出了一种名为MAPS（模块级就近调度）的框架，这是一种用于VLA的稳健微调方法。它通过系统分析揭示了缓解进近距离约束的顺序，从而平衡稳定性和灵活性。MAPS使视觉编码器保持接近预训练先验，同时使行动导向的语言层能够自由适应。该方法无需引入额外的参数或数据，并能无缝集成到现有的VLA中。在MiniVLA-VQ、MiniVLA-OFT、OpenVLA-OFT等小型数据集以及SimplerEnv、CALVIN、LIBERO等挑战性基准和现实世界的Franka Emika Panda平台上，MAPS在分布内和分布外性能上都表现出了显著提升。
### Conclusion
研究结果强调了保留广泛泛化的经验引导的预训练VLM附近作为简单但强大的原则，在VLM到VLA的转移中。”
## 891. `cs.LG` - 复杂足球比赛中的多样风格策略实现高级指令遵循 [PDF](https://arxiv.org/pdf/2511.19885), [HTML](https://arxiv.org/abs/2511.19885)
### Authors
Chenglu Sun,Shuo Shen,Haonan Hu,Wei Zhou,Chen Chen
### Background
尽管在基础领域和简单命令（如物体操作和导航）中，语言指导强化学习（LC-RL）取得了进展，但在复杂多代理环境中理解和执行高级或抽象指令的能力（如足球比赛）仍面临重大挑战。
### Innovation
本文提出了Language-Controlled Diverse Style Policies (LCDSP)，一种专为复杂场景设计的新型LC-RL范式。LCDSP 包括两项关键技术：Diverse Style Training (DST) 方法和 Style Interpreter (SI)。DST 方法通过风格参数（SP）调整代理行动以高效地训练单个政策，使其能够展示广泛的多样行为。SI 用于将高级语言指令准确且迅速地转化为相应的 SP。
### Conclusion
通过在复杂5v5足球环境中的大量实验，我们证明了LCDSP 能够有效理解和执行复杂的战术指令，并准确实现所需的多种行为风格，显示出其在复杂现实应用中的潜力。
## 892. `cs.LG` - 通过基于推测的算法-系统协同设计减少LLM搜索代理的延迟 [PDF](https://arxiv.org/pdf/2511.20048), [HTML](https://arxiv.org/abs/2511.20048)
### Authors
Zixiao Huang,Wen Zeng,Tianyu Fu,Tengxuan Liu,Yizhou Sun,Ke Hong,Xinhao Yang,Chengchun Liu,Yan Li,Quanlu Zhang,Guohao Dai,Zhenhua Zhu,Yu Wang
### Background
基于LLM的搜索代理能够表现出色，但面临严重的延迟问题，因为每次步骤都需要经过序列化的LLM推理循环，随后才是工具执行。
### Innovation
研究提出了一种算法-系统协同设计框架SPAgent，通过推测机制来减少搜索代理的延迟。第一阶段，SPAgent引入了一种两阶段自适应推测机制，有条件地跳过验证步骤。系统层面，通过两级调度器基于引擎负载来调节推测请求，确保推测的有效性。
### Conclusion
实验结果显示，SPAgent能够在不损失甚至提高准确性的前提下，实现高达1.65倍的端到端加速，从而使得多步骤搜索代理的实践部署成为可能。
## 893. `cs.LG` - 基于AI/ML的HARQ-ACK有效载荷联合源信道编码 [PDF](https://arxiv.org/pdf/2511.19943), [HTML](https://arxiv.org/abs/2511.19943)
### Authors
Akash Doshi,Pinar Sen,Kirill Ivanov,Wei Yang,June Namgoong,Runxin Wang,Rachel Wang,Taesang Yoo,Jing Jiang,Tingfang Ji
### Background
从2G到5G，物理层的输入位假定为均匀分布。然而，上行链路传输的HARQ-ACK位是固有非均匀分布的。对于这些数据源，通过联合源信道编码和基于深度学习的技术可以获得显著的性能提升。
### Innovation
本文提出了一种基于变压器的编码器训练算法，使用新颖的“免费午餐”训练算法，并提出了每个码字的功率整形，以在编码器上利用源先验知识，同时对HARQ-ACK分布的微小变化具有鲁棒性。开发了一种 Neyman-Pearson 测试的扩展，用于具有多个信息位的编码位系统，实现了解码器中 NACK 与 ACK 位的非等错误保护。此外，还应用了所提出的编码器和解码器设计到5G新无线电（NR）合规的上行链路设置，并描述了最优接收器设计和低复杂度相干近似设计。
### Conclusion
在衰落信道下应用所提编码器和解码器设计后，结果表明，与NR基准相比，平均传输功率减少3-6 dB，最大传输功率减少2-3 dB，从而为覆盖范围和功率节省提供了显著的优势。
## 894. `cs.LG` - 使用玻尔兹曼机学习焦耳-汤姆逊磁体中的势能面 [PDF](https://arxiv.org/pdf/2511.19879), [HTML](https://arxiv.org/abs/2511.19879)
### Authors
Jackson C. Glass,Gia-Wei Chern
### Background
论文背景在于研究采用受限玻尔兹曼机（RBMs）作为一种灵活的生成框架来建模焦耳-汤姆逊磁性物质中的自旋排列。这涉及非均匀且强关联的相态，特别是在受挫磁体中。研究者首先对照ANNNI模型的一个多相点，说明了RBMs可以通过学习零温基态空间，准确再现其摇摆性或指数衰减关联。接着，研究者将RBMs应用于kagome自旋冰，展示了它们成功学习局部冰规则和短程关联。这种技术的关键在于，从RBM生成的关联函数与直接蒙特卡洛模拟计算的结果非常接近。
### Innovation
研究的主要创新点在于发现RBMs能够作为一种强大的工具，用于理解和预测受挫磁体中复杂的自旋配置，尤其是在涉及多种相态和较强相互作用的情况下。RBMs的成功在于能够准确捕捉冰结构的局部规则和短程相关性，同时在部分有序的相态中进一步展示了症对称性的解释。
### Conclusion
研究结果强调了RBMs作为生成模型在学习受限且高度受挫磁性状态中的效用。为了精确建模长程电荷有序和时间反转对称性破缺的部分有序冰-II相，需要采用具有统一符号偏置场的RBMs，这与潜在的对称性破缺相对应。这一发现凸显了RBMs在复杂物理系统建模和理解中的潜力。
## 895. `cs.LG` - 从数据到概念的线路图 [PDF](https://arxiv.org/pdf/2511.20138), [HTML](https://arxiv.org/abs/2511.20138)
### Authors
Jason Lo,Mohammadnima Jafari
### Background
论文背景在于如何从序列数据中提取抽象概念表示，特别是通过线路图代表的时间过程。研究者们使用了图论、聚类技术、增强学习和数据工程的结合，来解决从具体数据中提炼出重要概念的问题。
### Innovation
论文的创新点在于提出了一个新的概念——拟骨架线路图图，并证明它与Hasse图是一一对应的。基于这一结果，研究者设计了一种算法从序列数据中提取线路图，并成功应用于计算机游戏中的自主代理行为分析，能够准确识别出获胜策略。而且将主要算法与其他基于标准聚类技术的两个算法进行对比，评估了其性能。
### Conclusion
本文通过结合范畴论、图论、聚类、增强学习和数据工程等多种技术，成功地从序列数据中提取出了线路图表示的概念，验证了在博弈游戏中的应用效果，并通过对算法性能的比较展示了其优越性。
## 896. `cs.LG` - 包含领域知识和因果约束的可操作和多样化反事实解释 [PDF](https://arxiv.org/pdf/2511.20236), [HTML](https://arxiv.org/abs/2511.20236)
### Authors
Szymon Bobek,Łukasz Bałec,Grzegorz J. Nalepa
### Background
现有的反事实解释方法往往忽略了现实世界数据集中的复杂依赖关系，导致反事实修改不切实际或不可行。通过研究电子邮件营销领域的网络安全应用，本文提出了一种新的方法DANCE，该方法结合了特征依赖性和因果约束，以确保反事实的可信度和现实可行性。该方法从数据中学习线性和非线性的约束条件，或整合专家提供的依赖图，从而保证反事实的可操作性和可信性。
### Innovation
本文提出了一种新的方法DANCE，能够在现实世界中维护特征关系的一致性，生成明确且具有现实可行性与相关性的反事实。此方法还在反事实的可信度、多样性和稀疏性之间取得了平衡，有效解决了现有算法中的关键局限性。
### Conclusion
通过实证研究和广泛使用的评估指标，该方法能够生成具有现实相关性的有意义反事实，并在140个公开数据集上进行了全面评估，结果表明其表现优于其他现有的方法。此研究成果基于与波兰最大电子邮件营销公司Freshmail的联合研发项目Sendguard，并已发布相关源代码供进一步研究使用。
## 897. `cs.LG` - softmax变换器是图灵完备的 [PDF](https://arxiv.org/pdf/2511.20038), [HTML](https://arxiv.org/abs/2511.20038)
### Authors
Hongjian Jiang,Michael Hahn,Georg Zetzsche,Anthony Widjaja Lin
### Background
硬注意力Chain-of-Thought (CoT)变换器已知是图灵完备的。但是，关于softmax注意力CoT变换器是否图灵完备的问题仍然开放。本文研究并证明了长度可泛化的softmax CoT变换器是图灵完备的。
### Innovation
本文证明了一个更加强大的结果，即长度可泛化的softmax CoT变换器是图灵完备的。具体而言，研究者通过Chain-of-Thought扩展的计数RASP (C-RASP) 来进行图灵完备性的证明，这对应于允许长度泛化的softmax CoT变换器。研究者证明了因果掩码下以一元字母表为语境的C-RASP是图灵完备的（更一般情况下，对于字母受限的语言）。虽然对于任意语言，这种方式并非图灵完备，但其通过相对位置编码的扩展对于任意语言是图灵完备的。
### Conclusion
本文通过训练需要复杂（非线性）算术推理的语言变换器的实证研究，验证了上述理论。
## 898. `cs.LG` - MFM-point: 多尺度流匹配法在点云生成中的应用 [PDF](https://arxiv.org/pdf/2511.20041), [HTML](https://arxiv.org/abs/2511.20041)
### Authors
Petr Molodyk,Jaemoo Choi,David W. Romero,Ming-Yu Liu,Yongxin Chen
### Background
近年来，点云生成在3D生成建模中引起了广泛关注。现有的点基于方法可以直接生成点云，无需依赖如潜在特征、网格或体素等其他表示方式。尽管这些方法具有较低的训练成本和算法简洁性，但往往在性能上不及基于表示的方法。
### Innovation
本文提出了MFM-Point，一种多尺度流匹配框架，显著改善了点基于方法的可扩展性和性能，同时保持了其简洁性和效率。多尺度生成算法采用粗细生成范式，提高生成质量和可扩展性，而不增加训练或推理的开销。文章介绍了结构化的下采样和上采样策略，以保留几何结构并确保不同分辨率之间的平滑一致性分布变换。
### Conclusion
实验结果表明，MFM-Point 在点基于方法中表现最佳，并挑战了最好的基于表示的方法。特别是，在多类别和高分辨率生成任务中，MFM-Point 显示出了很强的结果。
## 899. `cs.LG` - 设计制造数据交易市场的声誉系统：基于Q学习和IRL估计效用的多智能体评估 [PDF](https://arxiv.org/pdf/2511.19930), [HTML](https://arxiv.org/abs/2511.19930)
### Authors
Kenta Yamamoto,Teruaki Hayashi
### Background
近年来，机器学习和大数据分析的进步增加了对高质量跨域数据集的需求，并加速了组织间的数据交易增长。随着数据被广泛视为经济资产，数据市场已经成为数据驱动创新的关键基础设施。然而，数据交易环境仍处于起步阶段，且信息不对称明显。买家在购买数据前无法验证其内容或质量，因此信任和质量保证成为关键挑战。
### Innovation
该研究开发了一个多智能体数据市场模拟器，通过建模参与者行为并评估信任形成机制来解决上述问题。模拟器集成强化学习（RL）以实现适应性智能体行为，并运用逆强化学习（IRL）来从实际行为数据中估计效用函数。研究综合分析了五种代表性声誉系统（时间衰减、贝叶斯-贝塔、PageRank、PowerTrust和PeerTrust）的效果，并提出了一个集成了现有系统优势的混合声誉机制，以提高价格和质量的一致性，并确保市场整体稳定性。
### Conclusion
本研究表明，通过将信任和声誉作为内生机制，结合仿真分析，能够为可靠和高效的数据生态系统的设计提供方法论和机构性见解。特别指出的是，PeerTrust机制在数据价格和质量匹配方面表现出最佳效果，同时防止了垄断主导的局面。
## 900. `cs.LG` - Modality-Balanced Collaborative Distillation for Multi-Modal Domain Generalization [PDF](https://arxiv.org/pdf/2511.20258), [HTML](https://arxiv.org/abs/2511.20258)
### Authors
Xiaohan Wang,Zhangtao Cheng,Ting Zhong,Leiting Chen,Fan Zhou
### Background
权值平均（WA）已被证明是一种强大的技术，通过促进收敛到平坦的损失景观来增强泛化能力，这与更好的领域外性能相关。然而，将WA直接应用于多模态领域泛化（MMDG）是具有挑战性的，因为不同模态的优化速度差异会导致WA在早期阶段过度拟合较快收敛的模态，抑制较慢但互补模态的贡献，从而妨碍有效模态融合，使得损失面偏向尖锐、不具泛化能力的极小值。
### Innovation
我们提出了MBCD（模态平衡协作蒸馏），这是一种统一的协作蒸馏框架，保持了WA促进平坦损失景观的优势，同时克服了其在多模态环境中的不足。MBCD首先在学生模型中采用自适应模态dropout，以减少早期阶段对主导模态的偏见。然后通过梯度一致性约束使统一模态分支和融合表示的学习信号保持一致，鼓励协调和平滑优化。最后，基于WA的教师通过跨模态蒸馏，将融合的知识转移到每个统一模态分支，增强了跨模态交互作用，并引导收敛向更平坦的解。
### Conclusion
在MMDG基准上的广泛实验表明，MBCD在性能和鲁棒性方面均优于现有方法，能够在多样化的未见领域中实现更高的准确率和鲁棒性。
## 901. `cs.LG` - CostNav：一种旨在经济意识评估实体代理导航基准 [PDF](https://arxiv.org/pdf/2511.20216), [HTML](https://arxiv.org/abs/2511.20216)
### Authors
Haebin Seong,Sungmin Kim,Minchan Kim,Yongjun Cho,Myunchul Joe,Suhwan Choi,Jaeyoon Jung,Jiyong Youn,Yoonshik Kim,Samwoo Seong,Yubeen Park,Youngjae Yu,Yunsung Lee
### Background
现有的导航基准主要关注任务成功的指标，而忽视了经济可行性，这对于自主送货机器人商业部署至关重要。现有的工作没有系统地考虑导航研究指标与商业可行性之间的差距，没有充分评估经济成本和收益。CostNav提供了一个综合了成本-收益分析的微导航经济测试平台，能够模拟现实世界业务操作中的经济生命周期，包括硬件、培训、能源、维护成本及服务级别协议下的递送收入。CostNav使用来自行业数据源的参数（如能源费率、服务定价）建立成本模型，并通过缩放仿真向现实递送投影。
### Innovation
CostNav是首个定量揭示导航研究指标与商业可行性的差距的工作，表明优化任务成功率与优化经济部署完全不同。CostNav使用行业的参数进行成本建模，并从缩小规模的仿真中投影到现实递送中。基础模型的SLA合规率为43.0%，但不具备商业可行性，每次运行亏损30.009美元，并且没有财务盈亏平衡点。原因是运营成本主要由碰撞引起的维护成本主导，这部分占每次运行成本的99.7%，突出了碰撞避免作为关键优化目标的重要性。此外，CostNav为基于规则、模仿学习和成本感知RL训练评估提供了基础。
### Conclusion
CostNav填补了导航研究和商业部署之间的差距，为跨导航范式内的经济权衡提供了数据驱动的决策依据。
## 902. `cs.LG` - 使用伊辛机加速牛顿-拉弗森收敛的量子增强强化学习：功率流向分析案例研究 [PDF](https://arxiv.org/pdf/2511.20237), [HTML](https://arxiv.org/abs/2511.20237)
### Authors
Zeynab Kaseb,Matthias Moller,Lindsay Spoor,Jerry J. Guo,Yu Xiang,Peter Palensky,Pedro P. Vergara
### Background
牛顿-拉弗森（NR）方法因其二次收敛特性而广泛用于求解功率流向（PF）方程，但其性能在初期估计不佳或极端运行场景下（如高可再生能源渗透率）会下降。传统NR初始化策略难以应对这一挑战，导致收敛速度变慢甚至发散。
### Innovation
提出利用强化学习（RL）优化NR初始化策略，并引入量子增强RL环境更新机制，使用量子/数字退火器解决了大规模动作空间下评估电力系统状态的高计算成本问题，通过将电压调整问题形式化为二次无约束二进制优化问题。此项创新显著提高了收敛速度，减少了NR迭代次数，并增强了其在不同运行条件下的鲁棒性。
### Conclusion
实验结果表明，该方法有效提升了牛顿-拉弗森方法在各种运行条件下的表现，使程序更快收敛，并在计算上更为高效和稳定。
## 903. `cs.LG` - 使用物理信息神经网络求解异质性代理人模型 [PDF](https://arxiv.org/pdf/2511.20283), [HTML](https://arxiv.org/abs/2511.20283)
### Authors
Marta Grzeskiewicz
### Background
理解家庭行为对于宏观经济动态建模和设计有效政策至关重要。虽然异质性代理人模型提供了一个比代表剂框架更现实的选择，但在连续时间下的实现带来了巨大的计算挑战。Aiyagari-Bewley-Huggett (ABH)框架重新表述为偏微分方程系统后，通常依赖于网格基解算器，这些解算器受到维度灾难、高计算成本和数值不准确性的困扰。
### Innovation
本文介绍了ABH-PINN解算器，该方法基于物理信息神经网络（PINNs），并通过将哈密尔顿-雅可比-贝尔曼和柯尔莫哥洛夫前向方程直接嵌入神经网络训练目标来简化计算。通过用无网格、可微分的函数学习替代网格基近似，ABH-PINN解算器利用了PINNs的可伸缩性、平滑解和计算效率优势。
### Conclusion
初步结果显示，基于PINN的方法能够获得与建立的有限差分解算器相匹配的经济上有意义的结果。
## 904. `cs.LG` - 提升乒乓球应用场景中的3D轨迹和旋转估算：一种稳健的现实世界应用 [PDF](https://arxiv.org/pdf/2511.20250), [HTML](https://arxiv.org/abs/2511.20250)
### Authors
Daniel Kienzle,Katja Ludwig,Julian Lorenz,Shin'ichi Satoh,Rainer Lienhart
### Background
从标准单目视频中精确获取乒乓球的3D运动是一项具有挑战性的问题，现有的方法在合成数据上的训练难以在真实世界中处理噪音较大的、不完美的乒乓球和球桌检测结果。主要原因是缺乏真实世界视频中三维地面真实轨迹和旋转标注。因此，提出了一种新的两阶段管道，将问题分为前端感知任务和后端从2D到3D提升任务。这样可以使用新创建的TTHQ数据集丰富的2D监督来训练前端组件，而后端提升网络仅在物理上正确的合成数据上训练。
### Innovation
提出了一种新的两阶段管道，将问题分为前端感知任务和后端从2D到3D提升任务。前端使用丰富的2D监督从新创建的TTHQ数据集训练，而后端的提升网络仅使用物理上正确的合成数据训练。重新设计了提升模型，使其对常见的现实世界伪影，如丢失检测和变化的帧率具有鲁棒性。通过集成球检测器和球桌关键点检测器，将提升方法转化为端到端的应用，实现3D乒乓球轨迹和旋转分析。
### Conclusion
通过整合球检测器和球桌关键点检测器，我们的方法将一个概念验证的提升方法转变为一个实用、稳健且高性能的端到端应用，用于3D乒乓球轨迹和旋转分析。
## 905. `cs.LG` - 延伸与电阻抗成像逆映射的神经算子逼近 [PDF](https://arxiv.org/pdf/2511.20361), [HTML](https://arxiv.org/abs/2511.20361)
### Authors
Maarten V. de Hoop,Nikola B. Kovachki,Matti Lassas,Nicholas H. Nelsen
### Background
本文探讨了Calderón逆传导问题解映射的噪声鲁棒神经算子逼近问题。在连续模型的电阻抗成像(EIT)中，边界测量被表示为Neumann-to-Dirichlet算子积分核的扰动。理论分析通过将反演算子的定义域扩展到核函数的希尔伯特空间来实现。这种方法使反演算子具有与原算子相同的稳定性，但允许使用神经算子进行逼近。
### Innovation
通过扩展反演算子的定义域到核函数的希尔伯特空间，该方法使得噪声鲁棒的神经算子逼近成为可能，并且实验证明傅里叶神经算子在含噪条件下重建无限维分段常数和对数正态导电体表现出色，且超越了理论假设。
### Conclusion
本文的方法为解决非线性逆问题提供了噪声感知的操作学习框架，适用于电阻抗成像，并且表明这种方法不仅在理论假设的条件下有效，还在含噪条件下也表现出色。
## 906. `cs.LG` - 一种用于正则化Volterra系统识别的完全概率张量网络 [PDF](https://arxiv.org/pdf/2511.20457), [HTML](https://arxiv.org/abs/2511.20457)
### Authors
Afra Kilic,Kim Batselier
### Background
使用Volterra级数建模非线性系统具有挑战性，因为模型阶数增加时核系数的数量会指数增长。因此，现有的方法在处理高阶模型时可能会遇到参数量和计算复杂度急剧增加的问题。
### Innovation
提出了Bayesian Tensor Network Volterra核机（BTN-V），在Bayesian Tensor Network框架的基础上扩展了Volterra系统的识别。BTN-V使用典范多线性分解表示Volterra核，将模型复杂度从O(I^D)降低到O(DIR)。通过将所有张量组件和超参数视为随机变量，BTN-V可以以无需额外计算成本的方式提供预测不确定性估计。此外，引入了诱导稀疏性的分层先验，能够自动确定秩并直接从数据中学习消失记忆行为，提高了模型的可解释性并防止过拟合。
### Conclusion
实验证明，BTN-V在准确度、不确定性量化和计算成本方面表现出竞争力。这一方法在处理非线性系统建模时提供了更有效且可解释的方法，可以处理高阶模型且保持计算高效性。
## 907. `cs.LG` - 使用Laban启发式和频域运动特征的舞蹈风格分类 [PDF](https://arxiv.org/pdf/2511.20469), [HTML](https://arxiv.org/abs/2511.20469)
### Authors
Ben Hamscher,Arnold Brosch,Nicolas Binninger,Maksymilian Jan Dejna,Kira Maag
### Background
舞蹈是人类文化中不可或缺的组成部分，用于传递情感和讲述故事。基于运动数据识别和区分舞蹈风格是一个在人类活动识别中复杂的问题，因为许多风格共享相似的动作、手势和时间运动模式。
### Innovation
提出了一种轻量级框架，通过预测从视频中提取的姿态来确定运动特征，使用受Laban运动分析启发的时间-空间描述符捕捉局部关节动力学，如上半身的速度、加速度和角运动，进一步通过快速傅立叶变换特征编码运动的节奏和周期性方面，实现在低计算开销下对不同舞蹈风格的稳健分类，无需复杂模型架构，并展示了可解释的运动表示可以有效捕捉风格特点。
### Conclusion
所提出的方法能够在低计算努力下实现对不同舞蹈风格的稳健分类，表明可解释的运动表示可以有效地捕捉风格的细微差别。
## 908. `cs.LG` - 通过剪枝实现遗忘：连接基数估计中的数据删除 [PDF](https://arxiv.org/pdf/2511.20293), [HTML](https://arxiv.org/abs/2511.20293)
### Authors
Chaowei He,Yuanjun Liu,Qingzhi Ma,Shenyuan Ren,Xizhao Luo,Lei Zhao,An Liu
### Background
在基于学习的基数估计（CE）系统中，机器遗忘面临独特的挑战，特别是在多表关系数据中复杂的分布依赖关系。具体地，在学习的CE模型中，数据删除这一机器遗忘的核心组件面临着三个关键挑战：属性级别的敏感性、表之间的传播和领域消失，这会导致多路联接中严重的基数高估。
### Innovation
我们提出了基数估计剪枝（CEP），这是一个专门为多表学习的CE系统设计的第一个遗忘框架。CEP 引入了分布敏感性剪枝，它构建了半联接删除结果并计算敏感性分数以指导参数剪枝，以及领域剪枝，该剪枝完全移除由删除操作彻底消除的价值领域支持。
### Conclusion
我们在线性代数和TPC-H数据集上对CEP进行了NeuroCard和FACE等最先进的架构的评估。结果表明，在多表场景下，CEP始终能以最低的Q误差实现学习的CE，特别是在高删除比例下，通常优于全面重新训练。此外，CEP显着减少了收敛迭代次数，计算开销仅为微不足道的0.3%-2.5%的微调时间。
## 909. `cs.LG` - 不同可微衰减滤波器用于反馈延迟网络 [PDF](https://arxiv.org/pdf/2511.20380), [HTML](https://arxiv.org/abs/2511.20380)
### Authors
Ilias Ibnyahya,Joshua D. Reiss
### Background
介绍了基于反馈延迟网络（FDNs）设计数字音频回声系统衰减滤波器的一种新型方法。传统的图示均衡器设计要求每个延迟线含有大量滤波器，本文提出了一种可调节的解决方案，通过共享频率、增益和品质因数（Q）参数，减少了优化参数的数量，并且保持了可微性，与基于梯度的学习框架兼容。
### Innovation
提出了一种利用次级部分（SOS）的无限脉冲响应（IIR）滤波器编排作为参数均衡器（PEQ）的方法，允许对频率相关回声衰减进行精细控制。这种方法根据延迟长度调整增益，而不是每个延迟线都需要大量滤波器，从而减少了优化参数的数量，同时保持了可微性，与基于梯度的学习框架兼容。这种方法支持使用监督学习进行高效的滤波器拟合，实现了灵活可行的设计，并显著降低了计算成本。
### Conclusion
采用这种方法设计的衰减滤波器不仅具有领先的技术性能，还大大降低了计算成本。
## 910. `cs.LG` - NNGPT：使用大规模语言模型重新思考AutoML [PDF](https://arxiv.org/pdf/2511.20333), [HTML](https://arxiv.org/abs/2511.20333)
### Authors
Roman Kochnev,Waleed Khalid,Tolgay Atinc Uzun,Xi Zhang,Yashkumar Sanjaybhai Dhameliya,Furui Qin,Chandini Vysyaraju,Raghuvir Duvvuri,Avi Goyal,Dmitry Ignatov,Radu Timofte
### Background
在人工智能领域，构建自我改进的AI系统仍然是一个基本挑战。本研究旨在解决这一问题，通过开发一个开放源代码框架NNGPT，将大型语言模型（LLM）转变为针对计算机视觉领域中神经网络开发的自我改进自动化机器学习引擎。
### Innovation
NNGPT 引入了一种新的方法，通过生成新模型扩展神经网络数据集，从而实现基于生成、评估和自我改进的闭环系统的持续微调。它集成了五个协同工作的LLM基础流水线，包括零样本架构合成、超参数优化（HPO）、代码感知的准确性和早期停止预测、带有检索增强的PyTorch模块合成（NN-RAG）和强化学习。与之前的框架相比，NNGPT在结构验证、代码执行和学习能力方面表现出了显著优势。
### Conclusion
NNGPT已生成超过5000个验证模型，证明其作为自动机器学习引擎的自主能力。接受后，相关代码、提示和检查点将对公众开放以促进可再现性和社区使用。
## 911. `cs.LG` - STARFlow-V：基于归一化流的端到端视频生成建模 [PDF](https://arxiv.org/pdf/2511.20462), [HTML](https://arxiv.org/abs/2511.20462)
### Authors
Jiatao Gu,Ying Shen,Tianrong Chen,Laurent Dinh,Yuyang Wang,Miguel Angel Bautista,David Berthelot,Josh Susskind,Shuangfei Zhai
### Background
归一化流（NFs）是连续数据的概率生成模型，近年来在图像生成领域取得了令人鼓舞的进展。然而，在视频生成领域，由于时空复杂性和计算成本更高，最先进的系统几乎完全依赖于基于扩散的模型。本文重新探讨了这一设计空间，提出了STARFlow-V，一种基于归一化流的视频生成器，具有端到端学习、稳健的因果预测和原生似然估计等显著优点。
### Innovation
STARFlow-V 采用了基于全球-局部架构的时空潜在空间运作方式，限制因果依赖于全局潜在空间，同时保持丰富的帧内局部交互。此外，STARFlow-V 提出了流评分匹配，使模型具备轻量级的因果去噪器，以自回归的方式改进视频生成一致性。为了提高采样效率，STARFlow-V 应用了视频意识的雅可比迭代方案，将内部更新重新表述为并行迭代且不打破因果性。
### Conclusion
STARFlow-V 在视觉保真度和时间一致性方面取得了良好的实证结果，具有实际采样吞吐量。这些结果首次证明，归一化流有能力进行高质量的自回归视频生成，将其确立为构建世界模型的一个有前途的研究方向。代码和生成样本可在 provided link 获得。
## 912. `cs.LG` - 使用流形渗流进行生成建模 [PDF](https://arxiv.org/pdf/2511.20503), [HTML](https://arxiv.org/abs/2511.20503)
### Authors
Rui Tong
### Background
通常，生成模型被视为学习映射规则，但从观察者的角度来看，没有这些规则的访问权限，任务表现为将几何支撑从概率分布中分离出来。我们提出，渗流连续过程是进行支撑分析的理想选择，因为采样过程实际上将高维密度估计投影为支撑上的几何计数问题。
### Innovation
本文建立了随机几何图的拓扑相变与其在高维空间中潜在数据流形之间的严格同构关系。通过分析我们提出的渗流移位度量与FID之间的关系，我们证明了我们的度量能够在统计度量失败的地方捕捉到结构性病理（例如隐式模态坍塌）。最终，我们将这一拓扑现象转换为可微损失函数以指导训练。
### Conclusion
实验结果表明，这种做法不仅防止了流形收缩，还引导模型达到“超泛化”状态，实现了良好的保真度和验证拓扑扩张。
## 913. `cs.LG` - 模态深度学习框架在辅助感知中的应用：凝视、情感和说话人识别 [PDF](https://arxiv.org/pdf/2511.20474), [HTML](https://arxiv.org/abs/2511.20474)
### Authors
Akshit Pramod Anchan,Jewelith Thomas,Sritama Roy
### Background
开发全面的辅助技术需要视觉和听觉感知的无缝整合。本研究评估了一种受感知系统核心功能启发的模块化架构的可行性，特别是以'Smart Eye'为核心的功能。研究使用了Eyes Image、FER2013及自定义音频数据集来训练和验证模型。
### Innovation
提出了三个独立的传感模块：基于卷积神经网络（CNN）的眼态检测（困倦/注意力）、基于深层CNN的情感识别以及基于长短期记忆（LSTM）的语音说话人识别。这些模型分别在眼态检测、情感识别和说话人识别任务上达到了93.0%、97.8%和96.89%的准确率，展示了轻量级、领域专用模型在离散任务上能达到的高度精度。
### Conclusion
本研究证明了轻量级、领域特定模型在资源有限的辅助设备中进行实时多模态整合的基础已得到验证，为未来的应用奠定了坚实的基础。
## 914. `cs.LG` - 边界一致且鲁棒的DSA序列中动脉分割的物理信息损失函数 [PDF](https://arxiv.org/pdf/2511.20501), [HTML](https://arxiv.org/abs/2511.20501)
### Authors
Muhammad Irfan,Nasir Rahim,Khalid Mahmood Malik
### Background
从数字减影血管造影（DSA）序列中准确提取和分割脑动脉对于开发可靠的复杂颅血管疾病临床管理模型至关重要。然而，传统损失函数往往仅依赖于像素级重叠，忽视了血管边界在几何和物理上的连贯性，导致血管预测出现碎片化或不稳定的现象。
### Innovation
本文提出了一种新颖的物理信息损失（PIL），该方法将预测边界和真实边界之间的相互作用建模为类似于材料物理学中的位错理论的弹性过程。这一公式引入了一种基于物理的正则化项，该项强制血管轮廓平滑演化并保持结构一致性，从而使网络更好地捕捉精细的血管几何结构。
### Conclusion
通过将该损失函数整合到几种分割架构，包括U-Net、U-Net++、SegFormer和MedFormer，并在两个公开基准上进行评估，实验证明PIL比传统的交叉熵、Dice、主动轮廓和表面损失等常规损失函数具有更优的敏感性、F1分数和边界一致性。这些结果证实，在动态血管成像中将物理基础的边界交互引入深度神经网络可以提高血管分割的精度和鲁棒性。
## 915. `cs.LG` - StableTrack：在低频检测下稳定多对象跟踪 [PDF](https://arxiv.org/pdf/2511.20418), [HTML](https://arxiv.org/abs/2511.20418)
### Authors
Matvei Shelukhan,Timur Mamedov,Karina Kvanchiani
### Background
多对象跟踪（MOT）是计算机视觉中最具挑战性的任务之一，正确检测对象并在多帧间关联这些检测至关重要。当前的方法主要关注在视频流的每一帧中跟踪对象，这使得在计算资源有限的条件下运行模型几乎成为不可能。
### Innovation
本文提出了一种新颖的方法——StableTrack，以在低频率检测下稳定跟踪质量。该方法引入了一种新的两阶段匹配策略，提高了低频率检测之间的跨帧关联。采用了一种新型的边界框距离代替传统的马氏距离，使得通过Re-ID模型有效匹配对象成为可能。此外，将视觉跟踪整合进了卡尔曼滤波和整个跟踪管道中。
### Conclusion
在低频率检测情况下，本方法优于当前最先进的跟踪器，在MOT17-val上取得了11.6%的HOTA提升，同时在使用全频检测的情况下，保持了与标准的MOT17、MOT20和DanceTrack基准的竞争力。
## 916. `cs.LG` - 使用语义分割进行文化遗迹自动监测 [PDF](https://arxiv.org/pdf/2511.20541), [HTML](https://arxiv.org/abs/2511.20541)
### Authors
Andrea Ranieri,Giorgio Palmieri,Silvia Biasotti
### Background
本文探讨了对文化遗产保护中自动裂缝检测的迫切需求，通过语义分割技术实现这一目标。
### Innovation
本文对不同卷积神经网络（CNN）编码器构建的U-Net架构进行了比较研究，以像素级别识别雕像和纪念碑的裂缝。通过对比定量评估了OmniCrack30k数据集测试集上的性能，并对真实世界受损雕像和纪念碑的未标记测试集进行了定性评估。研究发现不同类型基于CNN的编码器在细粒度裂缝分割中的表现提供了有价值的见解。
### Conclusion
研究结果表明，这些模型表现出良好的泛化能力，能够应用于未见过的文化遗产环境，即使从未专门训练过雕像或纪念碑的图像。
## 917. `cs.LG` - 超越生成：Vision-Language模型的多跳推理以提高事实准确性 [PDF](https://arxiv.org/pdf/2511.20531), [HTML](https://arxiv.org/abs/2511.20531)
### Authors
Shamima Hossain
### Background
现有的视觉语言模型（VLMs）虽然功能强大，但由于缺乏坚实的推理能力，常常产生事实不准确的输出。虽然已经进行了大量的研究在大型语言模型（LLMs）中集成外部知识以进行推理，但这些努力在VLMs中并不常见，更复杂的多模态连接使得挑战进一步加大。
### Innovation
本文引入了一个框架，将结构化知识图谱与图像-描述任务结合，以实现多步知识引导的推理。这种方法能够系统地跨多个步骤进行推理，包括视觉实体识别、知识图谱遍历和基于事实的描述完善。通过不同的知识表示（层次结构、三元组、项目符号）进行评估，分析它们在事实准确性和逻辑推断方面的有效性。
### Conclusion
实证结果显示，我们的方法在初步实验中使事实准确性提高了约31%，运用了一个针对Google Landmarks v2、概念性描述和COCO描述编目的定制数据集。该研究揭示了推理模式和失败模式的关键见解，并展示了将外部知识集成到VLM推理中的潜力，为更可靠和有知识性的多模态系统铺平了道路。
## 918. `cs.LG` - New York Smells: 大规模跨模态数据集用于嗅觉 [PDF](https://arxiv.org/pdf/2511.20544), [HTML](https://arxiv.org/abs/2511.20544)
### Authors
Ege Ozguroglu,Junbang Liang,Ruoshi Liu,Mia Chiquier,Michael DeTienne,Wesley Wei Qian,Alexandra Horowitz,Andrew Owens,Carl Vondrick
### Background
嗅觉是动物感知世界的核心，但机器对于这一丰富的化学感知模式仍然难以获取。主要的瓶颈在于缺乏在自然环境中采集的、多种模态的嗅觉训练数据。
### Innovation
提出了New York Smells数据集，这是一个大规模的跨模态数据集，包含7000个嗅觉与图像配对的数据，覆盖了3500个不同的室内和室外物体。该数据集比现有的嗅觉数据集多出约70倍的物体。基准测试包括跨模态嗅觉到图像检索、仅从嗅觉识别场景、物体和材料以及草本植物种间精细区分三大任务。通过实验发现，视觉数据能够促进跨模态嗅觉表示学习，同时训练得到的嗅觉表示超越了广泛应用的手工特征。
### Conclusion
通过使用New York Smells数据集，研究展示了视觉数据在跨模态嗅觉表示学习中的作用，且所得的嗅觉表示超过了传统的手工特征。
## 919. `cs.LG` - InferF: Declarative Factorization of AI/ML Inferences over Joins [PDF](https://arxiv.org/pdf/2511.20489), [HTML](https://arxiv.org/abs/2511.20489)
### Authors
Kanchan Chowdhury,Lixi Zhou,Lulu Xie,Xinwei Fu,Jia Zou
### Background
实世界中的AI/ML工作流通常将来自多个数据集的特征向量用于推理计算。为了避免由连接输出中的重复数据记录引起的冗余AI/ML计算，已提出了因素化ML，将ML计算分解为在每个规范化数据集上执行的子计算。然而，关于如何在多路连接上影响AI/ML推理的因素化ML讨论并不充分。为解决这一局限性，该研究提出了一种新颖的声明性InferF系统，专注于表示为在多路连接上分析表达式的任意推理工作流的因素化。
### Innovation
研究提出了InferF系统，专注于表示为多路连接上分析表达式的任意推理工作流的因素化。通过一个基于每个节点成本函数的贪婪算法和一个用于迭代枚举和评估有希望的因素化计划的遗传算法，该系统灵活地下推部分因素化的计算到连接树中的合格节点，以最小化整体推理计算和连接成本。此外，该研究在Meta开源的Velox数据库引擎上实现了InferF，对实际数据集进行了评估，观察到最多11.3倍的加速。
### Conclusion
该研究系统地总结了当因素化ML能够提高AI/ML推理工作流性能时的决定性因素。
## 920. `cs.LG` - 通过评估LLM作为裁判来评估LLM对齐 [PDF](https://arxiv.org/pdf/2511.20604), [HTML](https://arxiv.org/abs/2511.20604)
### Authors
Yixin Liu,Pengfei Liu,Arman Cohan
### Background
LLM与人类偏好的一致性是评估LLM的重要方面，要求它们能够提供有帮助、诚实、安全的回答并严格按照人类指令行事。评估LLM的对齐通常涉及直接评估其开放式回答，这需要人类注释员或强大的LLM作为裁判。另一方面，LLM也被广泛用作裁判来评估对齐。但是，本研究旨在探讨LLM在生成和评估人类偏好的对齐一致性方面的关系。研究者首先对不同LLM的生成-评估一致性（GE一致性）进行了全面分析，发现当使用强大LLM偏好或acles评估时，生成与评估能力之间存在很强的相关性。
### Innovation
该研究提出了一种基准标记方法，无需直接评估LLM生成的输出，而是评估LLM的角色作为评价者，测度了LLM与人类偏好的一致性。研究证明提出的基准标记AlignEval在评估LLM的人类偏好排名方面，能够与广泛使用的自动LLM评价基准（如AlpacaEval和Arena-Hard）相媲美或更优。
### Conclusion
本研究为LLM生成能力和评估能力之间的关联提供了有价值的见解，并引入了一种不需要直接评估模型输出来测度一致性的基准。
## 921. `cs.LG` - MapReduce LoRA: 提升生成模型多偏好优化的帕累托前沿 [PDF](https://arxiv.org/pdf/2511.20629), [HTML](https://arxiv.org/abs/2511.20629)
### Authors
Chieh-Yun Chen,Zhonghao Wang,Qi Chen,Zhifan Ye,Min Shi,Yue Zhao,Yinan Zhao,Hui Qu,Wei-An Lin,Yiru Shen,Ajinkya Kale,Irfan Essa,Humphrey Shi
### Background
强化学习从人类反馈（RLHF）结合奖励模型已经提高了生成模型与人类审美和感知偏好的对齐。然而，同时优化多个奖励常常会产生对齐税，即在提升一个维度的同时，会损害其他维度。为了解决这一问题，本文提出了两种互补的方法：MapReduce LoRA 和 Reward-aware Token Embedding (RaTE)。
### Innovation
本文引入了两个互补的方法：MapReduce LoRA 和 Reward-aware Token Embedding (RaTE)。MapReduce LoRA 在并行训练特定于偏好的 LoRA 专家后，通过迭代合并它们来细化共享基础模型；RaTE 在推理时学习奖励特定的 token 嵌入，以灵活控制偏好。实验结果展示了在文本到图像生成（Stable Diffusion 3.5 Medium 和 FLUX.1-dev）和文本到视频生成（HunyuanVideo）以及语言任务（Helpful Assistant 使用 Llama-2 7B）方面的改进。这些方法为不同模态的多偏好对齐设定了新的最先进状态。
### Conclusion
本文提出的方法为不同模态的多偏好对齐设定了一个新的最先进状态，提高了文图像和视频生成的视觉和运动质量，以及语言任务中的有用性和无害性。
## 922. `cs.LG` - 时空分层因果模型 [PDF](https://arxiv.org/pdf/2511.20558), [HTML](https://arxiv.org/abs/2511.20558)
### Authors
Xintong Li,Haoran Zhang,Xiao Zhou
### Background
细粒度的时空数据，如交通传感器网络，为科学发现提供了巨大的机会。然而，从这种观察数据中推断因果关系仍然具有挑战性，主要是由于特定于单位（如地理位置）且随时间影响结果的未观察到混淆因素。现有的时空因果推断方法大多假设所有混淆因素都是已观察到的，但在实践中这一假设经常不被满足。
### Innovation
本研究提出了一种新颖的时空分层因果模型（ST-HCMs）图形框架，将层次因果模型扩展到时空领域。核心创新在于提出的时空坍塌定理，该定理表明，在大量子单元数据条件下，复杂ST-HCM收敛于一个更简单的平面因果模型。此理论结果使得时空因果模型能够在存在未观察到且随时间不变的单位层面混淆因素的情况下，识别因果效应，而在这种情况下，标准的非分层模型会失效。
### Conclusion
框架在合成数据集和真实世界数据集上的验证显示，其在复杂动态系统中具有稳健的因果推理潜力。
## 923. `cs.LG` - 概念感知批量采样提高语言图像预训练 [PDF](https://arxiv.org/pdf/2511.20643), [HTML](https://arxiv.org/abs/2511.20643)
### Authors
Adhiraj Ghosh,Vishaal Udandarao,Thao Nguyen,Matteo Farina,Mehdi Cherti,Jenia Jitsev,Sewoong Oh,Elisa Ricci,Ludwig Schmidt,Matthias Bethge
### Background
现有的数据整理工作主要集中在数据集质量上，但大多数现有方法具有两个局限性：一是离线的，会产生一个从预测过滤标准产生的静态数据集；二是概念无感知的，使用基于模型的过滤器，引入额外的数据偏差。本文提出了一个更为灵活的任务适应在线概念感知调理方法。
### Innovation
1. 开发了DataConcept数据集，包含1.28亿个网络爬取的图像-文本对，带有详细的概念组成标注细节。2. 提出了概念感知批量采样（CABS）框架，能够根据特定的目标分布灵活构建批量，具体包括最大化多样性和最大化频率两种变体。通过在28个基准评估中展示了我们的CABS方法能显著提高CLIP/SigLIP模型性能，生成高性能模型。
### Conclusion
CABS作为一种强大的开源替代方案，提供了业界开发人员可以根据特定下游任务自定义概念分布的替代方案，从而优化模型性能。
## 924. `cs.LG` - Latent Collaboration in Multi-Agent Systems [PDF](https://arxiv.org/pdf/2511.20639), [HTML](https://arxiv.org/abs/2511.20639)
### Authors
Jiaru Zou,Xiyuan Yang,Ruizhong Qiu,Gaotang Li,Katherine Tieu,Pan Lu,Ke Shen,Hanghang Tong,Yejin Choi,Jingrui He,James Zou,Mengdi Wang,Ling Yang
### Background
现有的大规模语言模型（LLMs）是从独立单模型推理扩展到协调系统级智能的多代理系统（MAS）。当前的LLM代理依赖于文本中介进行推理和通信。
### Innovation
作者提出了一个端到端无需训练的新框架LatentMAS，使其能够直接在连续的潜在空间中使LLM代理协作。该框架通过最后一层隐藏嵌入进行自回归潜在思考生成，共享的潜在工作记忆保证无损失的信息交换，从而提高表达能力和信息保真度，降低复杂度。
### Conclusion
实验结果表明，在数学和科学推理、常识理解和代码生成等方面，LatentMAS在基准测试中优于强大的单模型和文本型MAS基线，准确率最高提高14.6%，输出令牌使用量减少70.8%到83.7%，并且具有更快的端到端推理速度。这些结果表明，此新的潜在协作框架能够提升系统级别的推理质量，并且在无需额外训练的情况下提供显著的效率提升。全部代码和数据已在公开链接中开源。
## 925. `cs.LG` - 快速、样本高效且仿射不变的私有均值和协方差估计，适用于次高斯分布 [PDF](https://arxiv.org/pdf/2301.12250), [HTML](https://arxiv.org/abs/2301.12250)
### Authors
Gavin Brown,Samuel B. Hopkins,Adam Smith
### Background
当前已有算法在完全不同情况下只可用指数时间来进行高维数据的均值估计，这些算法无法满足优化的样本复杂性需求。该研究旨在提供一种在保持 nearly optimal 样本复杂性的前提下，快速且能够在隐私保护下进行高维统计特征估计的方法。
### Innovation
该工作提出了一种高效并且差分隐私的算法，能够在几乎最优的样本复杂性条件下实现高维数据的均值和协方差估计。这是通过改进已有的指数时间复杂度方法并引入新的稳定协方差估算子程序来实现的。同时，该算法能够扩展到处理无限制的次高斯分布，并且在样本数量减少到 o(d^2) 后仍然能够保证较高的精度。
### Conclusion
该研究实现了快速、样本高效及仿射不变的私有均值和协方差估计，尤其是在处理高维次高斯分布时具有显著的优势。这为高维数据的隐私保护统计分析提供了新的方法与工具。
## 926. `cs.LG` - MotionV2V: 在视频中编辑运动 [PDF](https://arxiv.org/pdf/2511.20640), [HTML](https://arxiv.org/abs/2511.20640)
### Authors
Ryan Burgert,Charles Herrmann,Forrester Cole,Michael S Ryoo,Neal Wadhwa,Andrey Voynov,Nataniel Ruiz
### Background
尽管生成式视频模型在保真度和一致性方面取得了显著进展，但将其应用到视频编辑中仍然是一个复杂的挑战。尽管最近的研究探索了通过提升文本到视频生成或图像动画的方式增强了运动可控性，但精准的运动控制作为一个编辑现有视频的潜力尚未被充分探索。本研究旨在通过直接修改输入视频中的稀疏轨迹来实现对视频运动的编辑。
### Innovation
我们提出了一种新的方法，即通过修改从输入视频中提取的稀疏轨迹来进行视频运动编辑，并将这种轨迹之间的偏差称为“运动编辑”。我们构建了一个生成‘运动反事实’的管道，即共享相同内容但具有不同运动的视频配对，并对一个由运动条件化的视频扩散架构进行了微调。我们的方法允许在任意时间点开始编辑，并实现自然的传播。
### Conclusion
在四向人对人对比实验中，我们的模型在偏好度方面优于先前工作超过65%。有关项目详情，请参见项目页面：this https URL
## 927. `cs.LG` - 图核神经网络 [PDF](https://arxiv.org/pdf/2112.07436), [HTML](https://arxiv.org/abs/2112.07436)
### Authors
Luca Cosmo,Giorgia Minello,Alessandro Bicciato,Michael Bronstein,Emanuele Rodolà,Luca Rossi,Andrea Torsello
### Background
卷积操作在许多现代神经架构的核心可以有效地被视为在输入矩阵和滤波器之间执行点积。虽然这种方法适用于如图像这样的数据，能够以欧几里得空间中的正则网格进行表示，但将卷积操作扩展到在图上工作则更具挑战性，因为图的结构是不规则的。
### Innovation
本文提出使用图核，即可以计算图之间内积的核函数，来扩展标准的卷积操作到图域。这使得我们可以定义一个完全结构化的模型，而无需计算输入图的嵌入。该架构允许插入任何类型的图核，并具有在训练过程中学习的结构掩码提供可解释性的优点，类似于传统卷积神经网络中的卷积掩码。
### Conclusion
我们进行了广泛的效果评估，研究了模型超参数的影响，并展示出我们的模型在标准图分类和回归数据集上达到了竞争力的性能。
## 928. `cs.LG` - 利用视觉-语言模型为长尾多标签视觉识别释放潜力 [PDF](https://arxiv.org/pdf/2511.20641), [HTML](https://arxiv.org/abs/2511.20641)
### Authors
Wei Tang,Zuo-Zheng Wang,Kun Zhang,Tong Wei,Min-Ling Zhang
### Background
长尾多标签视觉识别面临着重大挑战，因为图像通常包含多个标签，且类别分布严重不平衡，导致模型偏向头部类而忽视尾部类的表现。尽管预训练的视觉-语言模型如CLIP结合长尾学习技术可以利用丰富的视觉-文本先验提高性能，但现有方法直接从不平衡数据集中推导语义类间关系，导致尾部类不可靠的关联。此外，CLIP的一次性范式优化单标签图像-文本匹配，使其不适用于多标签任务。
### Innovation
提出了一种名为CAPNET的新颖端到端框架，通过CLIP的文本编码器显式建模标签之间的语义关联。该框架包含图卷积网络用于标签感知传播，并使用可学习的软提示优化嵌入。同时，引入了分布平衡的Focal损失并按类别重新加权以优化在不平衡数据下的训练。此外，通过测试时的集成增强了泛化能力，并使用参数高效的微调重新对齐视觉-文本模态来防止因过度拟合尾部类而损害头部类的表现。
### Conclusion
在VOC-LT、COCO-LT和NUS-WIDE基准上的广泛实验和消融研究表明，CAPNET在长尾多标签视觉识别中显著优于现有方法，证明了其在实际应用中的有效性。
## 929. `cs.LG` - 时间序列与时空数据扩散模型综述 [PDF](https://arxiv.org/pdf/2404.18886), [HTML](https://arxiv.org/abs/2404.18886)
### Authors
Yiyuan Yang,Ming Jin,Haomin Wen,Chaoli Zhang,Yuxuan Liang,Lintao Ma,Yi Wang,Chenghao Liu,Bin Yang,Zenglin Xu,Shirui Pan,Qingsong Wen
### Background
扩散模型在时间序列和时空数据中得到了广泛应用，提升了生成、推理及下游任务的能力。这些模型被广泛应用于多种领域，如医疗、推荐系统、气候、能源、音频和交通等方面。
### Innovation
通过区分时间序列数据和时空数据的应用，本文提供了一个结构化的模型类别、任务类型、数据模态和实际应用领域的视角。本文旨在为研究人员和实践者提供坚实的基础，激发未来在基于扩散模型的数据挖掘任务和应用中创新解决传统难题的新方案。
### Conclusion
本文通过提供一个详尽的扩散模型综述，鼓励未来在时间序列和时空数据处理中进行创新研究，并公开了一项用于进一步了解和研究扩散模型的资源链接。
## 930. `cs.LG` - PaTAS: 一种使用主观逻辑在神经网络中并行传播信任的系统 [PDF](https://arxiv.org/pdf/2511.20586), [HTML](https://arxiv.org/abs/2511.20586)
### Authors
Koffi Ismael Ouattara,Ioannis Krontiris,Theo Dimitrakos,Dennis Eisermann,Frank Kargl
### Background
在安全关键应用中部署人工智能系统的前提是保障其可信度。传统的评估指标如准确性和精确度无法捕捉模型预测的不确定性或可靠性，尤其是在对抗性或退化条件下。因此，需要一种新的评估框架来衡量模型在实际应用场景中的可靠性。
### Innovation
提出了并行信任评估系统（PaTAS），它采用主观逻辑（SL）对神经网络中的信任进行建模和传播。PaTAS通过信任节点和信任函数并行地传播输入、参数和激活的信任信息。该框架定义了参数信任更新机制和推断路径信任评估方法，以改进训练过程中的参数可靠性并计算实例特定的推断信任。
### Conclusion
实验证明，PaTAS生成解释性好、对称且收敛的信任估计，可以补充准确性并揭示中毒、有偏或不确定数据场景中的可靠性差距。结果表明，PaTAS能够有效区分良性输入和对抗性输入，并识别模型信心与实际可靠性存在分歧的情况。通过在神经架构内部实现透明和可量化的信任推理，PaTAS为整个AI生命周期中的模型可靠性评估提供了原则性的基础。
## 931. `cs.LG` - Gated Uncertainty-Aware Runtime Dual Invariants for Neural Signal-Controlled Robotics [PDF](https://arxiv.org/pdf/2511.20570), [HTML](https://arxiv.org/abs/2511.20570)
### Authors
Tasha Kim,Oiwi Parker Jones
### Background
安全关键辅助系统需要从神经信号直接解码用户意图，并且需要对可靠性和信任度有严格的保证。对于这样的系统，GUARDIAN框架致力于实时神经-象征验证，特别是用于神经信号控制的机器人。
### Innovation
GUARDIAN框架通过结合信心校准的脑信号解码、象征性目标基础和双层运行时监控，同时确保逻辑安全性和生理信任度。该系统在BNCI2014运动想象脑电图（EEG）数据集上，使用轻量级解码架构，即使测试准确率较低（27-46%）且ECE置信度误标较高（0.22-0.41），仍然表现出了94-97%的安全率。此外，测试通过使用GUARDIAN实现了1.7倍的正确干预次数，并能在100Hz和亚毫秒级的决策延迟下运作，使其适用于闭环神经信号系统，并在21个消融实验中展示了对信号降级的渐进式反应，生成可审计的从意图到行动的记录。
### Conclusion
GUARDIAN框架在实时神经信号控制机器人中实现了逻辑安全性和生理信任度的双重保障，即使在测试准确率不高和置信度误标的情况下也能确保系统的高安全率。该框架还具有亚毫秒级决策延迟和可实际应用的特点，以及对信号降级的渐进反应和可审计轨迹的生成能力。
## 932. `cs.LG` - MGAS: 多粒度架构搜索以权衡模型效果与效率 [PDF](https://arxiv.org/pdf/2310.15074), [HTML](https://arxiv.org/abs/2310.15074)
### Authors
Xiaoyun Liu,Divya Saxena,Jiannong Cao,Yuqing Zhao,Penghui Ruan
### Background
神经架构搜索(NAS)在自动化设计神经网络方面取得了显著进展。不同的可微架构搜索(DAS)方法将传统的从离散候选采样和评估转变成在超网上的可微优化，然后进行离散化处理，以减少搜索时间。然而，现有的大多数DAS方法主要集中在优化粗粒度的操作级拓扑结构，而忽略了更细粒度的结构，如滤波器级和权重级模式。这限制了它们平衡模型性能与模型大小的能力。另外，许多方法在搜索过程中为了节省内存而牺牲搜索质量。
### Innovation
我们提出了多粒度差分架构搜索(MG-DARTS)，它是一种统一框架，旨在通过全面且高效地探索多粒度搜索空间来从头发现有效的和高效的架构。具体而言，我们从两个方面改进了现有的DAS方法：首先，通过自适应修剪方法，在不同粒度级别上自适应调整可搜索单元的保留比例，这通过学习特定粒度层级的离散化函数并随着架构的进化来实现；其次，我们将超网优化和离散化分解为多个阶段，每个阶段操作于子网，引入逐步重新评估以允许之前单元的重新修剪和重新生长，从而缓解潜在的偏差。
### Conclusion
在CIFAR-10、CIFAR-100和ImageNet上的广泛实验表明，MG-DARTS在权衡模型准确性和参数效率方面优于其他最先进的方法。代码可在以下网址获取: [提供网址]。
## 933. `cs.LG` - 引导特征选择的多输入自编码器用于物联网入侵检测系统 [PDF](https://arxiv.org/pdf/2403.15511), [HTML](https://arxiv.org/abs/2403.15511)
### Authors
Phai Vu Dinh,Diep N. Nguyen,Dinh Thai Hoang,Quang Uy Nguyen,Eryk Dutkiewicz,Son Pham Bao
### Background
虽然物联网数据特征多样性对于入侵检测系统(IDSs)有益，但这种多样性（如数据的异构性和高维度）也使得训练有效的机器学习模型变得困难，可能会导致冗余或噪声特征，从而降低检测引擎的准确性。
### Innovation
提出了一种新的神经网络架构，称为多输入自编码器（MIAE），它由多个针对不同数据源特性的子编码器组成。MIAE通过无监督学习模式训练，将异构输入转换为低维度表示，有助于分类器区分正常行为和不同类型攻击。在此基础上，设计并嵌入了一个特征选择层（MIAEFS），该层在表示层之后，用于训练过程中的特征提取和保留重要特征，同时移除不重要或冗余的特征。
### Conclusion
MIAE和MIAEFS在NSLKDD、UNSW-NB15和IDS2017三个IDS数据集上的表现优于其他方法，如传统分类器、降维模型、不同输入维度的无监督表示学习方法和无监督特征选择模型。结合随机森林（RF）分类器时，MIAE和MIAEFS在检测复杂攻击如Slowloris方面的准确率达到了96.5%。使用MIAE和MIAEFS的RF分类器检测攻击样本的平均运行时间约为1.7E-6秒，且模型大小低于1 MB。
## 934. `cs.LG` - 价值增强的演员评论家算法 [PDF](https://arxiv.org/pdf/2406.01423), [HTML](https://arxiv.org/abs/2406.01423)
### Authors
Yaniv Oren,Moritz A. Zanger,Pascal R. van der Vaart,Mustafa Mert Celikok,Matthijs T. J. Spaan,Wendelin Bohmer
### Background
现代演员评论家算法依赖深度神经网络（DNNs）来参数化行动策略，并使用贪婪化算子以迭代方式改进策略。DNNs的选择暗示了一种基于梯度的方法，每步比使用Q学习算法中的贪婪更新方法所能改善的贪婪度更低，但较慢的变化对学习过程的稳定性是有益的，这之间存在贪婪化和稳定性的权衡。
### Innovation
建议将演员策略与评论家评估的策略解耦。这一方法允许代理使用更贪婪的更新来单独改进评论家的策略（如价值改进），同时保持对参数化演员策略的缓慢梯度优化，从而更好地解决贪婪化与稳定性的权衡。
### Conclusion
通过在流行的TD3和SAC（软 actor-critic）算法中添加价值改进，这种方法在不同DeepMind连续控制环境中显著提高了或匹配了基线性能，且几乎无需增加计算和实现成本。
## 935. `cs.LG` - 去神秘化的高阶图神经网络 [PDF](https://arxiv.org/pdf/2406.12841), [HTML](https://arxiv.org/abs/2406.12841)
### Authors
Maciej Besta,Florian Scheidl,Lukas Gianinazzi,Grzegorz Kwasniewski,Shachar Klaiman,Jürgen Müller,Torsten Hoefler
### Background
高阶图神经网络（HOGNNs）及其相关的架构源自拓扑深度学习，是GNN模型的一个重要类别。它们利用顶点之间的多元关系，超越了简单的边。HOGNNs被用来解决过平滑或过挤压的问题，显著提高了GNN预测的准确性，提升了GNN架构的表达力，并用于众多其他目标。众多HOGNN模型被引入，它们具有不同的神经架构，甚至“高阶”的含义也不尽相同。这种多样性使得分析和比较HOGNN模型变得困难，也使人难以确定在特定情况下应使用哪类模型。
### Innovation
本文首先设计了一套详细的HOGNN分类和框架，便于设计出性能最佳的模型。然后，使用这套分类来分析和比较现有的HOGNN模型。分析结果形成了有关如何根据特定场景选择最有利的GNN模型的一系列见解，还列出了进一步研发更强大的HOGNN模型的挑战和机会。
### Conclusion
现有HOGNN模型的多样性使得选择和比较它们变得困难，为了简化这一过程，本文提出了HOGNN的分类和框架，通过分析现有模型，提供了一套选型指南，并指出了未来研究的方向和挑战。
## 936. `cs.LG` - 统计流形上的分类流匹配 [PDF](https://arxiv.org/pdf/2405.16441), [HTML](https://arxiv.org/abs/2405.16441)
### Authors
Chaoran Cheng,Jiahan Li,Jian Peng,Ge Liu
### Background
该研究基于信息几何的结果，提出了一种新的统计流匹配（SFM）框架，这种方法是在参数化概率测度流形上进行流匹配的新颖且严格的数学方法。研究者将该方法应用于离散生成问题，并使用分类分布的流形对其几何特性进行建模，这是前人较少涉及的研究领域。
### Innovation
研究引入了SFM框架，利用 Fisher 信息度量为流形赋予黎曼结构，通过最短路径的测地线来有效利用内在几何特性。此外，研究提出了一种高效的训练和采样算法，解决了数字稳定性问题，通过流形之间的同胚。该研究提供了一种新的视角来理解统计流形，并展示了SFMs可以通过最优传输机制进行训练，将SFM解释为遵循自然梯度的最陡方向。与依赖于变分界线估计似然的前模型相比，SFM能进行任意概率测度的确切似然计算。
### Conclusion
实验结果表明，SFM在统计流形上学习更复杂模式的能力优于其他离散扩散或基于流的方法。在图像、文本和生物学等实际生成任务中，SFM的采样质量和似然性均高于其他离散扩散或基于流的方法。
## 937. `cs.LG` - SCNode：用于图表示学习的空间和上下文坐标 [PDF](https://arxiv.org/pdf/2410.02158), [HTML](https://arxiv.org/abs/2410.02158)
### Authors
Md Joshem Uddin,Astrit Tola,Varin Sikand,Cuneyt Gurcan Akcora,Baris Coskunuzer
### Background
有效的节点表示对于图神经网络（GNNs）至关重要，因为它直接影响其在节点分类和链接预测等下游任务中的能力。大多数现有的GNNs，特别是消息传递图神经网络，依赖于邻居聚合来迭代计算节点嵌入。虽然这种模式很强大，但它也面临过度压缩、过度平滑和欠判断等已知缺点，这些缺点会降级表示质量。更严重的是，许多GNNs假设同质性，即连接的节点具有相似的特征或标签，但在异质性图这类假设不成立的情况下，会出现较差的一般性。
### Innovation
提出了一种新颖的空间-上下文节点嵌入框架SCNode，用于同时处理同质性和异质性图结构。SCNode框架结合了空间和上下文信息，产生不仅更具判别性而且更具结构意识的节点嵌入。通过引入新的同质性矩阵来理解类别间的相互作用和倾向。
### Conclusion
在基准数据集上的广泛实验表明，SCNode在节点嵌入性能方面优于传统GNN模型，证明了其在不同图结构中的稳健性和适应性。
## 938. `cs.LG` - TopER：图表示学习中的拓扑嵌入 [PDF](https://arxiv.org/pdf/2410.01778), [HTML](https://arxiv.org/abs/2410.01778)
### Authors
Astrit Tola,Funmilola Mary Taiwo,Cuneyt Gurcan Akcora,Baris Coskunuzer
### Background
图嵌入在图表示学习中扮演着至关重要的角色，使机器学习模型能够探索和解读结构化的图数据。然而，现有的方法通常依赖于不透明、高维度的嵌入，限制了可解释性和实际可视化。
### Innovation
介绍了Topological Evolution Rate（TopER），一种新颖的低维度嵌入方法，基于拓扑数据分析。TopER通过计算图子结构的演化速率简化了关键的拓扑方法持久同伦，从而提供直观且可解释的图数据可视化。该方法不仅增强了图数据集的探索，还在图聚类和分类任务中表现出了竞争力。
### Conclusion
基于TopER的方法在分子、生物和社交网络数据集中的分类、聚类和可视化任务中实现了或超越了现有的最佳结果。
## 939. `cs.LG` - Mixture of Attention Spans: 通过异质滑动窗口长度优化大语言模型推理效率 [PDF](https://arxiv.org/pdf/2406.14909), [HTML](https://arxiv.org/abs/2406.14909)
### Authors
Tianyu Fu,Haofeng Huang,Xuefei Ning,Genghan Zhang,Boju Chen,Tianqi Wu,Hongyi Wang,Zixiao Huang,Shiyao Li,Shengen Yan,Guohao Dai,Huazhong Yang,Yu Wang
### Background
大语言模型（LLMs）在处理长上下文场景时面临着内存使用和吞吐量的挑战。现有方法通常采用固定长度的滑动窗口，适用于所有注意力头和输入大小，但未能捕捉到LLMs中的异质注意力模式，忽略了它们在准确性和延迟之间的不同权衡。
### Innovation
本文提出了一种名为Mixure of Attention Spans (MoA)的新方法，它能够自动为不同的注意力头和层级定制独特的滑动窗口长度配置。MoA构建了一个各种窗口长度及其相对于输入尺寸的比例规则的搜索空间，并通过模型评估确定了最优的长度配置。实验表明，MoA可以将有效上下文长度增加3.9倍，精度提升1.5-7.1倍，并且减少与全注意力的性能差距，同时减少GPU内存使用1.2-1.4倍，吞吐量提升6.6-8.2倍和1.7-1.9倍，相对于FlashAttention2和vLLM，性能影响极小。
### Conclusion
MoA通过异质滑动窗口长度优化了大语言模型的推理效率，不仅提升了性能，还减少了内存使用，提升了吞吐量。该方法适用于不同输入尺寸，并展示了在多种长上下文理解基准测试中的有效性。
## 940. `cs.LG` - LINSCAN — 基于线性度的聚类算法 [PDF](https://arxiv.org/pdf/2406.17952), [HTML](https://arxiv.org/abs/2406.17952)
### Authors
Andrew Dennehy,Xiaoyu Zou,Shabnam J. Semnani,Yuri Fialko,Alexander Cloninger
### Background
DBSCAN和OPTICS是强大的聚类算法，在很少假设数据结构的情况下能够识别点的数据集中的聚类。本文利用这些特点，提出了一种新型算法LINSCAN，专门用于寻找现有方法难以发现和分离的线性聚类。
### Innovation
LINSCAN通过将点嵌入为局部邻域近似的正态分布，并利用从Kullback-Leibler散度导出的距离函数，能够检测并区分在空间上接近但具有正交协方差的线性聚类。特别地，它能应用于地震数据以识别包括交叉断层在内的活动断层，并确定它们的倾向。
### Conclusion
最后，我们讨论了一般化DBSCAN和OPTICS必须具备的性质，以保留这些算法的稳定性优势。
## 941. `cs.LG` - 搜索潜在程序空间 [PDF](https://arxiv.org/pdf/2411.08706), [HTML](https://arxiv.org/abs/2411.08706)
### Authors
Matthew V Macfarlane,Clement Bonnet
### Background
通用智能需要能够高效获取新技能并超越训练分布范围的应用。尽管程序合成方法具有强大的泛化能力，但它们由于大量组合空间的扩大而在可扩展性方面面临挑战，需要通过人类生成的DSL或预训练先验知识来缩小搜索空间。另一方面，深度学习方法尽管取得了显著成功，但在结构化测试时间适应方面较弱，依赖大量随机采样或昂贵的梯度更新进行微调。
### Innovation
本文提出了一种名为Latent Program Network (LPN) 的新型架构，该架构直接将测试时搜索集成到神经模型中。LPN 通过学习潜在空间中隐式程序来映射输入到输出，并通过梯度在测试时进行搜索。LPN 结合了符号方法的适应性和神经方法的可扩展性，能够在测试时通过紧凑的潜在空间搜索，从而省去了预定义的领域特定语言的需要。在一系列编程范例任务中，LPN 的表现优于或保持与上下文学习和测试时训练方法的性能持平。在 ARC-AGI 基准测试中，LPN 既能够学习紧凑的程序空间，也能够在测试时搜索该空间来适应新任务。当在测试时启用搜索功能时，LPN 的表现提高了两倍。
### Conclusion
LPN 通过结合符号方法的灵活性和神经网络的可扩展性，在解决各种编程范式任务时实现了高性能，特别是在处理新颖任务时表现尤为突出。
## 942. `cs.LG` - ARBoids: 适应性残差强化学习与Boids模型在协作多USV目标防御中的应用 [PDF](https://arxiv.org/pdf/2502.18549), [HTML](https://arxiv.org/abs/2502.18549)
### Authors
Jiyue Tao,Tongsheng Shen,Dexin Zhao,Feitian Zhang
### Background
无人水面车辆（USVs）的目标防御问题（TDP）涉及在敌对方USV侵入指定目标区域前拦截它。特别具有挑战性的是当攻击方具备比防御方更出色的机动性时，如何有效地进行拦截变得更加困难。
### Innovation
本文提出了一种新的自适应残差强化学习框架——ARBoids，将深度强化学习（DRL）与生物启发的动力学Boids模型结合起来。Boids模型作为一种计算效率高的多智能体协调基础策略，而DRL则学习适应性修正策略以优化和优化防御方的行动。这种方法在高度仿真的Gazebo模拟环境中得到了验证，显示出比传统的拦截策略（包括基于力的方法和传统的DRL策略）更好的性能，且能够高度适应不同机动性水平的攻击方，表明其强大且通用性。
### Conclusion
提出的ARBOIDS框架在抵抗具有不同机动性能力的攻击方方面表现出色，其自适应残差强化学习策略在各种情况下都能优化防御方的行为表现，证明了该方法在协作多USV目标防御中的有效性和鲁棒性。
## 943. `cs.LG` - DisCO：通过 discriminative constrained optimization 增强大型推理模型 [PDF](https://arxiv.org/pdf/2505.12366), [HTML](https://arxiv.org/abs/2505.12366)
### Authors
Gang Li,Ming Lin,Tomer Galanti,Zhengzhong Tu,Tianbao Yang
### Background
近期，深度搜索模型 DeepSeek-R1 的成功和开放性吸引了人们对于 Group Relative Policy Optimization (GRPO) 作为大型推理模型 (LRMs) 的强化学习方法的关注。研究者发现 GRPO 在二元奖励设置下的目标存在固有的问题，即问题级别难度偏差，并且发现 GRPO 与传统监督学习中的判别式方法之间存在联系。
### Innovation
本文提出了一种新的判别式约束优化 (DisCO) 框架，旨在通过判别式学习原理增强 LRMs。DisCO 与 GRPO 及其变种的主要区别在于：(1) 用 scoring 函数定义的判别式目标替代了群组相对目标；(2) 使用非剪辑的 RL 代理目标作为 scoring 函数，替代了基于剪辑的替代目标；(3) 采用简单而有效的约束优化方法来确保 KL 散度约束。这种新框架相对于 GRPO 及其改进版本的优势包括：(i) 通过采用判别式目标彻底消除了难度偏差；(ii) 通过使用非剪辑评分函数和约束优化方法，解决了 GRPO 及其变体中的熵不稳定问题，从而实现了长期稳定的训练动态；(iii) 允许整合先进的判别式学习技术来解决数据不平衡问题，特别是在训练过程中很多问题的生成答案中否定答案显著多于肯定答案。
### Conclusion
实验结果表明，DisCO 显著优于 GRPO 以及其改进版本 DAPO，对于一个 1.5 亿参数的模型，DisCO 在六项基准任务上的平均改进分别为 7% 和 6%。
## 944. `cs.LG` - 面向大型图神经网络训练的多尺度方法 [PDF](https://arxiv.org/pdf/2503.19666), [HTML](https://arxiv.org/abs/2503.19666)
### Authors
Eshed Gal,Moshe Eliasof,Carola-Bibiane Schönlieb,Ivan I. Kyrchei,Eldad Haber,Eran Treister
### Background
图神经网络（GNNs）已成为处理结构化图数据的强大工具，但随着图的规模和连接性的增加，标准的GNN训练方法面临显著的计算和内存挑战，限制了其可扩展性和效率。
### Innovation
本文提出了一种新的框架，用于高效地对GNN进行多尺度训练。该方法利用分层图表示和子图，可以使信息在多个尺度和分辨率上进行整合。通过使用较粗的图抽象和子图，每个具有更少节点和边，大大减少了训练期间的计算开销。本文还提出了基于粗到细学习、子图到全图的知识迁移以及多尺度梯度计算等一系列可扩展的训练策略。
### Conclusion
结果表明，多尺度训练可以显著加速大型问题的GNN训练，同时保持或提高预测性能。
## 945. `cs.LG` - 位置：超越欧几里得--基础模型应接纳非欧几何 [PDF](https://arxiv.org/pdf/2504.08896), [HTML](https://arxiv.org/abs/2504.08896)
### Authors
Neil He,Jiahong Liu,Buze Zhang,Ngoc Bui,Ali Maatouk,Menglin Yang,Irwin King,Melanie Weber,Rex Ying
### Background
在基础模型和大型语言模型（LLMs）的时代，欧几里得空间已成为机器学习架构的事实几何环境。然而，近期的研究表明，这种选择存在根本性的限制。在大规模应用中，真实世界的数据往往表现出内在的非欧几里得结构，例如多向关系、层次结构、对称性和各向异性缩放，这些结构存在于语言、视觉和自然科学等多个领域。要在欧几里得空间的限制下有效捕捉这些结构是具有挑战性的。
### Innovation
这篇立场论文认为，超越欧几里得几何不仅是可选的增强措施，而是新一代基础模型必不可少的需求，以保持规模法则。采用这些几何结构，基础模型能够更有效地利用上述结构。具有任务感知的适应性可以通过动态重新配置嵌入以适应下游应用的几何结构进一步提高效率和表达能力。这一立场得到了对广泛基础模型的理论和实验研究的支持。
### Conclusion
我们提出了一种路线图，用于将非欧几里得几何整合到基础模型中，包括通过微调、从零开始训练和混合方法构建几何基础模型的策略。
## 946. `cs.LG` - 在多智能体逆强化学习中可行奖励 [PDF](https://arxiv.org/pdf/2411.15046), [HTML](https://arxiv.org/abs/2411.15046)
### Authors
Till Freihaut,Giorgia Ramponi
### Background
多智能体逆强化学习（MAIRL）旨在从专家演示中恢复智能体的奖励函数。目前，已经探讨了马尔可夫游戏中的可行奖励集，确定了能够解释给定均衡的所有奖励函数。然而，基于均衡的观察往往是模糊的：单个纳什均衡可以对应多种奖励结构，这可能改变多智能体系统的游戏性质。
### Innovation
为了应对这一挑战，研究引入了带熵正则化的马尔可夫游戏，这种游戏可以确保唯一均衡的同时保持战略激励。此外，为这一设定提供了样本复杂性分析，详细说明了错误如何影响学习策略的性能。这项工作为MAIRL奠定了理论基础，并提供了实用见解。
### Conclusion
研究不仅对MAIRL的可行奖励集进行了理论分析，还探讨了带熵正则化的马尔可夫游戏，提供了样本复杂性分析，强调了正确处理观察模糊性的重要性，为MAIRL的实际应用提供了重要的理论依据和实践指导。
## 947. `cs.LG` - 重新思考放大测试时间计算时的微调：限制置信度提高数学推理 [PDF](https://arxiv.org/pdf/2502.07154), [HTML](https://arxiv.org/abs/2502.07154)
### Authors
Feng Chen,Allan Raventos,Nan Cheng,Surya Ganguli,Shaul Druckmann
### Background
大型语言模型（LLMs）的进步昭示着通过增加测试时间计算量可以在复杂任务（如数学推理和代码生成）中实现强大的性能。这引发了一个关键问题：模型训练应该如何被调整以优化在后续测试时间计算策略和预算下的性能？研究者重点关注pass@N这一简单的测试时间策略，它在N个独立样本中搜索正确答案。研究指出使用交叉熵（CE）损失进行训练可能会与pass@N不一致，导致越长的训练时间pass@N的准确性越低。
### Innovation
论文阐述了通过限制模型置信度来提升测试时间计算下的数学推理性能的方法。研究者提出了一个更符合pass@N训练损失，该损失通过限制模型信心和恢复pass@N的测试性能。即便在不同场景下，包括回答数学问题和通过搜索不同形状的证明树来证明定理，该算法也展现了改进的数学推理性能。
### Conclusion
研究工作强调了需联合设计LLM开发中两个传统上分离的阶段：训练时间协议和测试时间搜索与推理策略的必要性。
## 948. `cs.LG` - GRAM: 使用稳健适应模块的深度RL泛化 [PDF](https://arxiv.org/pdf/2412.04323), [HTML](https://arxiv.org/abs/2412.04323)
### Authors
James Queeney,Xiaoyi Cai,Alexander Schperberg,Radu Corcodel,Mouhacine Benosman,Jonathan P. How
### Background
在现实世界的应用中可靠地部署深度强化学习需要能够跨多种条件泛化，包括训练过程中遇到的分布内情况以及全新的分布外情况。
### Innovation
我们提出了一种统一分布内和分布外泛化的框架，并引入了一个稳健适应模块，该模块能够识别并应对分布内和分布外环境动态。同时，我们结合了在分布内适应和分布外鲁棒性目标的联合训练管道。
### Conclusion
我们的算法GRAM在分布内和分布外场景上实现了强大的泛化性能，我们在广泛的仿真实验和四足机器人硬件运动实验中通过实验进行了验证。
## 949. `cs.LG` - 在权重流形中行走：一种受神经调制启发的拓扑条件化方法 [PDF](https://arxiv.org/pdf/2505.22994), [HTML](https://arxiv.org/abs/2505.22994)
### Authors
Ari S. Benjamin,Kyle Daruwalla,Christian Pehle,Abdul-Malik Zekri,Anthony M. Zador
### Background
人们常常希望能够高效地学习一系列相似的任务，并在任务之间共享知识。在人工神经网络中，通常通过将上下文嵌入网络输入来以上下文条件化网络。相比之下，大脑使用神经调制的策略来根据神经调节物（如血清素等）调整参数。本文受到神经调制的启发，提出了一种新的策略：通过学习基于任务上下文变量平滑参数化的权重矩阵来实现任务的条件化。
### Innovation
本文提出了一种新的方法，通过优化权重在权重空间中的光滑流形（而非优化单一权重向量）来实现条件化。这种方法利用流形的拓扑结构作为一个方便的杠杆，可以通过这来施加归纳偏置，同时学习在一种状态下能平滑地影响整个流形的权重值，鼓励状态之间的一般化。
### Conclusion
尽管简单的权重参数化方式表现出色，并且对分布外样本具有更好的泛化能力，这些结果表明，在低维流形上调节权重提供了一种基于原理并实际有效的条件化传统方法的替代方案。
## 950. `cs.LG` - FunReason：通过自我精炼多尺度损失和自动化数据精炼提高大型语言模型的功能调用能力 [PDF](https://arxiv.org/pdf/2505.20192), [HTML](https://arxiv.org/abs/2505.20192)
### Authors
Bingguang Hao,ZengZhuang Xu,Maolin Wang,Yuntao Wen,Yicheng Chen,Cunyin Peng,Long Chen,Dong Wang,Xiangyu Zhao,Jinjie Gu,Chenyi Zhuang,Ji Zhang
### Background
近年来，将大型语言模型（LLMs）与功能调用集成已成为增强其实用性的关键能力。然而，如何有效结合推理过程与准确的功能执行仍然是一个显著的挑战。传统的训练方法往往难以平衡详细的推理步骤与功能调用的精确度，导致性能欠佳。
### Innovation
为了应对这些限制，我们提出了FunReason框架。该框架通过自动化数据精炼策略和自我精炼多尺度损失（SRML）方法来增强LLMs的功能调用能力。FunReason利用LLMs的自然推理能力生成高质量的训练示例，强调查询解析性、推理连贯性和功能调用的精确度。SRML方法在训练过程中动态平衡推理过程和功能调用精度的贡献，解决了这两方面之间的固有权衡问题。FunReason在Fine-tuning过程中有效缓解了灾难性遗忘现象，实现了与GPT-4o相当的性能。
### Conclusion
FunReason提供了一种综合的方法来增强LLMs的功能调用能力，通过引入平衡的训练方法和数据精炼管道，实现与GPT-4o相当的性能，同时有效缓解了Fine-tuning过程中灾难性遗忘的现象。
## 951. `cs.LG` - 您的预训练LLM其实是一个无监督的置信度校正器 [PDF](https://arxiv.org/pdf/2505.16690), [HTML](https://arxiv.org/abs/2505.16690)
### Authors
Beier Luo,Shuoyuan Wang,Sharon Li,Hongxin Wei
### Background
对大规模语言模型进行后训练对于将预训练语言模型（PLMs）调整为与人类偏好和下游任务的对齐至关重要。然而，后训练语言模型（PoLMs）往往表现为过度自信，对正确和错误的输出都赋以高置信度。这在关键应用中可能导致可靠性下降。由于缺乏细粒度标记的下游任务数据，校准PoLMs已成为一项重大挑战。
### Innovation
本文提出了一个名为DACA的无监督方法，旨在优化后训练中参数（例如温度$tau$）以进行置信度校准。该方法基于预测分歧导致的PLM和PoLM之间的信心调整。理论上，PLM在分歧样本中的置信度低估了PoLM的预测精度，导致自适应过程中温度$tau$的值增大，因而产生欠自信的预测。DACA通过仅使用一致性样本来进行校准，从而有效解耦分歧样本的影响，避免了由于分歧样本导致的过高温度$tau$值，提高了校准性能。
### Conclusion
广泛的实验表明，该方法是有效的，能够显著改善开源和基于API的大规模语言模型（例如GPT-4o）的平均ECE，提升了最高15.08个百分点。
## 952. `cs.LG` - 多域集成分布下的跨域时间序列可控制融合泛化 [PDF](https://arxiv.org/pdf/2412.03068), [HTML](https://arxiv.org/abs/2412.03068)
### Authors
Xiangkai Ma,Xiaobin Hong,Mingkai Lin,Han Zhang,Wenzhong Li,Sanglu Lu
### Background
传统的深度模型在时间序列预测方面取得了前所未有的成功。然而，面对跨域泛化的挑战，现有的研究利用统计先验作为提示工程技术，在各种领域之间庞大的分布偏移下表现不佳。因此，本研究提出了时间序列通用扩散模型(TimeControl)，通过扩散模型系统地将多种时间序列领域的信息整合到统一的生成过程中。
### Innovation
TimeControl模型通过扩散去噪过程来建模跨域数据的混合分布，并直接利用条件采样生成目标领域的预测序列。该模型包含三个关键设计：（1）条件网络捕获观测序列的多尺度波动模式，作为上下文表示来指导去噪网络生成预测序列；（2）基于适配器的微调策略，预训练阶段学到的多域通用表示用于目标领域下游任务；（3）一种新型的混合架构设计，使TimeControl能够灵活生成任意长度的预测序列。通过在49个基准数据集和30个基线上的广泛实验，TimeControl在所有数据领域中优于现有基线，显示出优秀的零样本泛化能力。
### Conclusion
该研究提出了TimeControl模型，这是一种新型的时间序列通用扩散模型，通过扩散过程建模跨域数据混合分布，且通过有效的提示工程策略和混合架构设计实现优秀的零样本泛化能力。
## 953. `cs.LG` - 向多模态图大语言模型的方向 [PDF](https://arxiv.org/pdf/2506.09738), [HTML](https://arxiv.org/abs/2506.09738)
### Authors
Xin Wang,Zeyang Zhang,Linxin Xiao,Haibo Chen,Chendi Ge,Wenwu Zhu
### Background
多模态图在现实世界应用中无处不在，但现有的多模态图学习方法通常需要从头开始针对特定图数据和任务进行训练，无法很好地泛化到不同的多模态图数据和任务。
### Innovation
探索多模态图大语言模型（MG-LLM）的潜力，以统一并泛化到各种不同的多模态图数据和任务中。提出了一个统一的多模态图数据、任务和模型框架，发现了多模态图中的固有多层次和多尺度特征。具体提出了MG-LLM的五个关键特点：统一的多模态结构和属性空间、处理多样性的多模态图任务、多模态图上下文学习、多模态图与自然语言交互、多模态图推理。
### Conclusion
总结了现有的适合模型训练的多模态图数据集。相信该论文可以为MG-LLM在多模态图数据和任务上的泛化贡献于当前研究的进步。
## 954. `cs.LG` - FunDiff：函数空间中的物理启发式生成建模的扩散模型 [PDF](https://arxiv.org/pdf/2506.07902), [HTML](https://arxiv.org/abs/2506.07902)
### Authors
Sifan Wang,Zehao Dou,Siming Shan,Tong-Rui Liu,Lu Lu
### Background
近年来，生成模型，特别是扩散模型和流匹配模型，在合成图像和视频等离散数据方面取得了显著的成功。然而，将这些模型适应到实际物理应用中仍然具有挑战性，因为实际感兴趣的量是受复杂物理法则支配的连续函数。
### Innovation
FunDiff 提出了一种新颖的函数空间生成建模框架。该框架结合了隐含扩散过程和函数自编码器架构，以处理具有不同离散化的输入函数，生成在任意位置可评测的连续函数，并无缝集成物理先验知识。这些先验知识通过架构约束或物理信息损失函数实现，确保生成样本满足基本的物理定律。该研究在理论上建立了函数空间中密度估计的 minimax 最优性保证，证明了基于扩散的估计器在适当正则条件下可以达到最优收敛速率。此外，该研究展示了 FunDiff 在流体力学和固体力学等多个应用中的实用有效性。
### Conclusion
实验结果表明，FunDiff 生成的样本具有高度与目标分布一致的物理一致性，并且在嘈杂和低分辨率数据下具有鲁棒性。源代码和数据集可在 <this https URL> 公开获取。
## 955. `cs.LG` - 适配视觉语言模型以评估世界模型 [PDF](https://arxiv.org/pdf/2506.17967), [HTML](https://arxiv.org/abs/2506.17967)
### Authors
Mariya Hendriksen,Tabish Rashid,David Bignell,Raluca Georgescu,Abdelhak Lemkhenter,Katja Hofmann,Sam Devlin,Sarah Parisot
### Background
世界模型是一种生成模型，可以在过去观察和动作的条件下模拟环境动态，目前在规划、仿真和具身人工智能中受到关注。然而，这些模型的评估仍然是一项基本的挑战，现有的评估指标无法捕捉到细微的时间敏感性和语义一致性等能力。视觉-语言模型（VLMs）以其强大的多模态推理能力，显示出了作为生成内容自动评估工具的潜力。然而，它们在细微、时间敏感的评估任务中的应用仍然受到限制，并需要针对性的调整。
### Innovation
本文提出了一种针对动作识别和角色识别任务的统一评估框架——UNIVERSE（UNIfied Vision-language Evaluator for Rollouts in Simulated Environments），一种在计算和数据有限的情况下调整自适应的VLM评估器。通过在各种任务格式、上下文长度、采样方法和数据组成中进行全面、部分和参数高效适应方法的大量实验，展示了该统一评估器与任务特定检查点具有同等的能力。并且通过跨七个不同环境的人类研究确认了其与人类判断的强烈一致性，证明了UNIVERSE是一种轻量级、可适应且语义敏感的视频世界模型评估器。
### Conclusion
UNIVERSE作为一种基于VLM的评估器，能够在适应度和计算资源有限的情况下灵活适应，提供了一种统一的评估方法，该方法在动作和角色识别等任务上与特定任务的检查点表现持平，还通过人类研究证明了其在情景理解和评价中的高性能，为视频世界模型的评估提供了有力工具。
## 956. `cs.LG` - STAlloc: 利用时空规划提升大规模模型训练的内存效率 [PDF](https://arxiv.org/pdf/2507.16274), [HTML](https://arxiv.org/abs/2507.16274)
### Authors
Zixiao Huang,Junhao Hu,Hao Lin,Chunyang Zhu,Yueran Tang,Quanlu Zhang,Zhen Guo,Zhenhua Li,Shengen Yan,Zhenhua Zhu,Guohao Dai,Yu Wang
### Background
大规模语言模型的快速扩展导致了GPU内存压力的显著增加，进一步被诸如虚拟管线和重新计算等训练优化技术所加剧。这些技术破坏了张量寿命并引入了大量内存碎片。这种碎片来源于像PyTorch这样的深度学习框架中使用的在线GPU内存分配器，它们忽视了张量寿命。这种低效性可能导致高达43%的内存浪费，并触发内存溢出错误，从而削弱了优化方法的效果。
### Innovation
STAlloc是一种GPU内存分配器，能够通过利用训练负载在内存分配行为中的时空规律来减少碎片。STAlloc引入了一种新颖的方法，结合了离线规划和在线分配。离线规划利用了时空规律来生成近乎最优的分配方案，而在线分配则处理复杂的动态模型，如混合专家（MoE）。STAlloc作为可插拔的PyTorch内存分配器，减少了平均85.1%（最多100%）的碎片率，对密集型和MoE模型均有效，且几乎没有额外开销。
### Conclusion
STAlloc使得更高效的、高吞吐量的训练配置成为可能，将吞吐量性能提高了多达32.5%。
## 957. `cs.LG` - 使用决策规则在深度学习模型中施加强制性线性约束 [PDF](https://arxiv.org/pdf/2505.13858), [HTML](https://arxiv.org/abs/2505.13858)
### Authors
Gonzalo E. Constante-Flores,Hao Chen,Can Li
### Background
深度学习模型被广泛应用于关键任务中，这些任务要求预测结果必须满足诸如物理定律、公平性要求或安全限制等硬性约束。然而，现有的标准架构缺乏内置机制来执行这些约束，而基于正则化或投影的已知方法通常只能处理简单的约束、计算成本高昂，或者缺乏可行性保证。
### Innovation
本文提出了一种通用框架，用于在神经网络输出中强制实施输入相关的线性等式和不等式约束。该框架结合了一个训练用于预测准确度的任务网络，以及一个使用基于随机优化和鲁棒优化文献中的决策规则训练的安全网络，以确保在整个输入空间内满足约束条件。最终预测是两个子网络的凸组合，保证在训练和推理阶段都满足约束条件，无需迭代过程或运行时优化。该架构可以作为受约束函数的通用逼近器，并基于线性决策规则推导出可计算的形式。
### Conclusion
实验结果表明，我们的方法能够一致地满足约束条件，同时保持与竞争性准确度和较低推理延迟的一致性。
## 958. `cs.LG` - 阐明性滚动扩散模型在概率天气预报中的应用 [PDF](https://arxiv.org/pdf/2506.20024), [HTML](https://arxiv.org/abs/2506.20024)
### Authors
Salva Rühling Cachay,Miika Aittala,Karsten Kreis,Noah Brenowitz,Arash Vahdat,Morteza Mardani,Rose Yu
### Background
扩散模型是进行概率预测的强大工具，然而大多数在高维复杂系统中的应用通常单独预测未来状态。这种做法很难建模复杂的时间依赖性，并且无法明确考虑系统中固有的不确定性的递增。尽管提出了滚动扩散框架来解决这个问题，但将其与最新的高性能扩散技术整合仍然是一项巨大的挑战。
### Innovation
我们通过引入阐明性滚动扩散模型(ERDM)，它是第一个将滚动预测结构和阐明性扩散模型(EDM)的原理性、高性能设计成功统一的框架。我们通过重新调整EDM的核心组件（噪声计划、网络预训练以及海恩采样器），将其应用于滚动预测设置。ERDM的成功得益于三个方面：（i）一种新的损失权重方案，聚焦于从中期预测时间跨度向随机性过渡的区域；（ii）利用预先训练的EDM进行初始窗口的高效初始化策略；（iii）一种特有的混合序列架构，以在去噪过程中进行鲁棒的空间和时间特征提取。
### Conclusion
在二维纳维-斯托克斯模拟和ERA5全球天气预报（分辨率达1.5度）中，ERDM持续优于基于扩散的关键基准模型，包括条件自回归EDM。ERDM提供了一个灵活且强大的通用框架来解决需要精确建模不确定性的传播的扩散动力学预测问题。
## 959. `cs.LG` - 带有自我注意过滤和MLP存储的一层变换器可以证明获得并提取知识 [PDF](https://arxiv.org/pdf/2508.00901), [HTML](https://arxiv.org/abs/2508.00901)
### Authors
Ruichen Xu,Kexin Chen
### Background
现代大型语言模型（LLMs）在知识密集型任务上表现出色，但它们在预训练时的知识获取（存储和记忆）以及微调后推理过程中的知识提取（检索和回忆）背后的理论机制仍然不明确。尽管过去的理论研究通过分析训练动态探索了这些过程，但这些研究忽视了构建全面理论的关键组成部分：（1）多层感知器（MLP）作为知识存储的主要模块；（2）泛化能力，即LLMs能够在预训练后适应未见过的情景；（3）下一个词预测，这是一种标准的自回归目标，将知识编码为条件概率。
### Innovation
该研究引入了首个理论框架，通过分析单一层变换器的训练动态，解决了上述限制。该框架证明了在满足一定的正则条件时：（i）变换器在预训练过程中实现了近最优化的训练损失，展示了有效知识获取；（ii）在拥有足够大的微调数据集和适当的数据多重性条件下，变换器在微调中不会重新访问的预训练期间获得的实事性知识上实现了低泛化误差，表明了稳健的知识提取；（iii）这些条件不满足时，泛化误差会升高，导致幻觉。该分析涵盖了全过程微调和低秩微调，为实际低秩适应方法的有效性提供了见解。
### Conclusion
通过实验验证了理论上的发现，使用GPT-2和Llama-3.2-1B模型在合成和现实世界的PopQA基准测试集上进行了实验验证。
## 960. `cs.LG` - AReaL：一种大规模异步强化学习系统，用于语言推理 [PDF](https://arxiv.org/pdf/2505.24298), [HTML](https://arxiv.org/abs/2505.24298)
### Authors
Wei Fu,Jiaxuan Gao,Xujie Shen,Chen Zhu,Zhiyu Mei,Chuyi He,Shusheng Xu,Guo Wei,Jun Mei,Jiashu Wang,Tongkai Yang,Binhang Yuan,Yi Wu
### Background
强化学习（RL）已成为训练大规模语言模型（LLMs）的一个主导范式，尤其是在推理任务方面。有效的LLMs RL需要大规模并行化，因此迫切需要高效的训练系统。目前大多数大规模RL系统是同步的，生成和训练交替进行，在批量设置中，每个训练批次中的回放由同一个模型生成。这种方法稳定了RL训练，但系统效率低下：生成必须等待批次中最长的输出完成，这会导致GPU的利用效率低下。
### Innovation
AReaL是一个完全异步的RL系统，彻底解耦了生成和训练。AReaL的回放工人不断生成新的输出，无需等待，而训练工人在收集一批数据时就更新模型。AReaL还集成了系统级别的优化措施，从而显著提高了GPU的利用率。为稳定RL训练，AReaL平衡了回放工人和训练工人的负载，以控制数据过时，并采用了过时增强的PPO变体以更好地处理过时的训练样本。
### Conclusion
在数学和代码推理基准上的大量实验表明，AReaL在相同数量的GPU和匹配或改进的最终性能的情况下，比同步系统实现了高达2.77倍的训练加速。
## 961. `cs.LG` - 通过稀疏自动编码器实现可解释的奖励模型 [PDF](https://arxiv.org/pdf/2508.08746), [HTML](https://arxiv.org/abs/2508.08746)
### Authors
Shuyi Zhang,Wei Shi,Sihang Li,Jiayi Liao,Hengxing Cai,Xiang Wang
### Background
大型语言模型（LLMs）已在众多领域得到广泛应用。强化学习从人类反馈（Reinforcement Learning from Human Feedback, RLHF）通过使用奖励模型（Reward Models, RMs）作为人类偏好的代理，来使LLM的行为与人类价值相一致。因此，RMs的准确性和可靠性以及其可解释性对有效对齐至关重要。然而，传统RMs缺乏可解释性，不能深入地洞察奖励分配背后的推理，且对于用户偏好的变化不够灵活。尽管最近的多维度RMs在提高可解释性方面有所改进，但在提供特征级别的归因方面仍存局限性，且需要昂贵的注释。
### Innovation
本文提出了一种新的稀疏自动编码器增强奖励模型（Sparse Autoencoder-enhanced Reward Model, SARM），将预训练的稀疏自动编码器（Sparse Autoencoder, SAE）与奖励模型结合。SARM将基于LLM的RM的隐含激活映射到一个可解释的、稀疏的且单义的特征空间，并通过标量头部聚合特征激活以生成透明且具概念意义的奖励评分。实证评估表明，SARM能够实现奖励分配的直接特征级别归因，能够动态调整对偏好变化的反应，并在对齐性能上优于传统的奖励模型。
### Conclusion
实验结果表明，SARM能够直接实现特征级别的奖励归因，能够动态调整偏好变化，并且在对齐性能上优于传统的奖励模型。我们已经将代码发布在指定的链接上。
## 962. `cs.LG` - 将主动测试扩展到大语言模型 [PDF](https://arxiv.org/pdf/2508.09093), [HTML](https://arxiv.org/abs/2508.09093)
### Authors
Gabrielle Berrada,Jannik Kossen,Freddie Bickford Smith,Muhammed Razzak,Yarin Gal,Tom Rainforth
### Background
主动测试可以通过精心的数据收集来实现预测模型的高效评估，但这种方法可能带来较高的计算成本。
### Innovation
该研究提出了降低成本的方法，使得主动测试能够应用于大规模语言模型（LLM）。研究发现，可以使用上下文学习构建廉价的代理模型，无需在主动测试循环中更新，并且可以比目标模型更小。甚至不需要使用目标模型进行预测也能做出良好的数据获取决策。据此，该方法能提供比随机获取数据更准确的LLM性能评估。此外，还引入了一种评估误差的置信区间估计方法，作为评估主动测试效果的指标。
### Conclusion
该研究使得主动测试能够更准确地评估大语言模型的性能，并提出了一种有效的成本节约方法和一种评估工具，提高了主动测试在大规模模型上的应用效率和准确性。
## 963. `cs.LG` - 通过自我蒸馏扭曲顺序蒙特卡洛改进受约束的语言生成 [PDF](https://arxiv.org/pdf/2507.02315), [HTML](https://arxiv.org/abs/2507.02315)
### Authors
Sooyeon Kim,Giung Nam,Byoungwoo Park,Juho Lee
### Background
近期的研究将受约束的文本生成问题框架化为概率推理问题，并利用自回归语言模型进行处理。Zhao等（2024）提出了一个基于扭曲顺序蒙特卡罗的方法，该方法引入了学习扭曲函数和扭曲诱导提案来引导生成过程。然而，在受约束生成设置中，由于目标分布集中在基础模型下概率较低的输出上，学习变得具有挑战性，因为奖励信号稀疏且不信息丰富。
### Innovation
本文提出通过自我蒸馏扭曲顺序蒙特卡罗改进受约束的语言生成，实现生成质量的显著提高。具体来说，方法通过对基础模型进行迭代自蒸馏来逐步使其更符合目标分布，从而缓解了由于稀疏和不信息丰富的奖励信号而造成的挑战。
### Conclusion
通过自我蒸馏扭曲顺序蒙特卡罗方法，基础模型在逐步适应目标分布的过程中显著提高了生成质量，在受约束的文本生成任务中表现出了潜力。
## 964. `cs.LG` - 非平衡退火伴随采样器 [PDF](https://arxiv.org/pdf/2506.18165), [HTML](https://arxiv.org/abs/2506.18165)
### Authors
Jaemoo Choi,Yongxin Chen,Molei Tao,Guan-Horng Liu
### Background
近年来，基于学习的扩散采样器在从给定的无标准化密度中采样方面取得了显著进步。这些方法通常将采样任务形式化为随机最优控制（SOC）问题，并使用一个经典的无信息参考过程，这限制了它们高效引导轨迹向目标分布收敛的能力。
### Innovation
提出了一种非平衡退火伴随采样器（NAAS），这是一种新颖的基于SOC的扩散框架，使用退火参考动力学作为非站定基础SDE。这种退火结构自然地朝着目标分布推进，并生成信息丰富的参考轨迹，从而增强了控制学习的稳定性和效率。由于使用SOC形式化，该框架可以包含多种SOC求解器，从而在算法设计上提供了高度的灵活性。作为实例，我们采用了一种受到伴随匹配启发的轻量级伴随系统，使其训练高效且可扩展。
### Conclusion
该方法在各种任务中表现出有效性，包括从经典能量景观和分子玻尔兹曼分布中采样。
## 965. `cs.LG` - 基于Koopman算子对随机系统中部分观测的讨论 [PDF](https://arxiv.org/pdf/2506.21844), [HTML](https://arxiv.org/abs/2506.21844)
### Authors
Jun Ohkubo
### Background
在实际的观测过程中，通常难以获得所有观察量的完整观测数据，因此需要处理部分观测数据。对于确定性系统，Mori-Zwanzig形式化提供了一个理论框架来处理部分观测数据。最近，基于Koopman算子理论的数据驱动算法取得了显著进展，也有人探讨将Mori-Zwanzig形式化与Koopman算子理论相结合的可能性。本文通过Koopman算子理论讨论了随机系统中部分观测的影响。
### Innovation
本文利用Koopman算子理论讨论了随机系统中部分观测的影响，揭示了区分状态空间与函数空间的重要性。探讨了延迟嵌入技术在处理随机系统部分观测中的作用，并通过数值实验展示了误差随随机噪声幅值的变化呈现出幂律行为。此外，还讨论了幂律行为的指数与部分观测影响之间的关系。
### Conclusion
延迟嵌入技术在随机系统部分观测过程中是很有用的，部分观测误差随随机噪声幅度的变化呈现出幂律行为，并且揭示了这一幂律行为的指数与部分观测效果之间的联系。t
## 966. `cs.LG` - 基于可扩展神经网络的黑盒优化 [PDF](https://arxiv.org/pdf/2508.03827), [HTML](https://arxiv.org/abs/2508.03827)
### Authors
Pavankumar Koratikere,Leifur Leifsson
### Background
黑盒优化（BO）利用高斯过程（GP）模型和获取函数来指导未来的采样，在低维情况下效果显著。但随着问题维度和函数评估次数的增加，BO面临着计算复杂度高的问题。神经网络（NN）由于更好的可扩展性和复杂函数建模能力，开发了基于神经网络的BO方法。然而，这些方法通常需要估计NN预测的模型不确定性，这在高维情况下通常是计算密集和复杂的。
### Innovation
提出了一种名为SNBO的新方法，其不依赖于模型不确定性估计。SNBO通过探索和开发的特定标准添加新样本，并自适应控制采样区域以确保优化效率。
### Conclusion
SNBO在10到102维度的优化问题上表现出色，相比之下，通常能够以40-60%更少的函数评估次数和至少一个数量级更低的运行时间获得更好的函数值，优于最新的基准算法。
## 967. `cs.LG` - DE-VAE：利用差分熵的变分自编码器揭示参数和反向投影中的不确定性 [PDF](https://arxiv.org/pdf/2508.12145), [HTML](https://arxiv.org/abs/2508.12145)
### Authors
Frederik L. Dennig,Daniel A. Keim
### Background
最近，自编码器（AEs）因其能够创建多维数据的参数化和可逆投影而引起了兴趣。参数化投影允许在不重新计算整个投影的情况下嵌入新的、未见过的数据样本，而可逆投影则允许合成新的数据实例。然而，现有的方法在处理数据空间或嵌入空间中的边缘分布样本时表现不佳。
### Innovation
我们提出了一个使用差分熵（DE）提高所学参数化和可逆投影的不确定性感知变分AE (DE-VAE)。给定固定的投影，我们训练DE-VAE来学习从原始空间到二维空间的映射以及从二维空间回原始空间的反向映射。我们使用UMAP和t-SNE作为基线投影方法，在四个知名数据集上进行了定量和定性的评估。我们的研究结果表明，DE-VAE可以创建与其他现有AE基线方法可比较准确度的参数和反向投影，同时可以分析嵌入的不确定性。
### Conclusion
DE-VAE能够创建与现有AE基线方法具有可比准确度的参数化和反向投影，同时通过引入差分熵增强了对嵌入不确定性的分析能力。
## 968. `cs.LG` - 短视频推荐中基于相对优势去偏的观看时间预测 [PDF](https://arxiv.org/pdf/2508.11086), [HTML](https://arxiv.org/abs/2508.11086)
### Authors
Emily Liu,Kuan Han,Minfeng Zhan,Bocheng Zhao,Guanyu Mu,Yang Song
### Background
在视频推荐平台中，观看时间常被用作用户满意度的代理指标。然而，原始的观看时间可能受到诸如视频时长、流行度和个人用户行为等因素的干扰，这可能会歪曲用户的偏好信号，导致推荐模型产生偏差。
### Innovation
本文提出了一个新颖的相对优势去偏框架，通过将观看时间与基于用户和项目组的统计推导出的参考分布进行比较来纠正观看时间。通过这种方式，可以得到基于分位数的偏好信号，并引入了一个两阶段架构，明确地将分布估计与偏好学习分开。此外，还介绍了分布嵌入方法，可以在不进行在线采样或存储历史数据的情况下有效参数化观看时间分位数。
### Conclusion
离线和在线实验表明，与现有基准方法相比，该框架在推荐准确性和稳健性方面具有显着改进。
## 969. `cs.LG` - 通过消融测试进行卸载：走向可验证的生成性科学发现基准 [PDF](https://arxiv.org/pdf/2508.17681), [HTML](https://arxiv.org/abs/2508.17681)
### Authors
Robert Yang
### Background
该论文讨论了关于AI在科学中的作用的夸张声明，从超级智能治愈所有疾病到加速科学发现的承诺。这些声明引发了一个核心的认知问题：大型语言模型（LLMs）是否真正生成了新的知识，还是仅仅重新组合了记忆片段？为解决这一问题，作者提出了“卸载作为消融测试”的概念，这是一种检验创新性科学研究的方法。该方法的目的是系统地移除目标结果及其相关的支持命题、同义词和复合推导，并评估模型是否能仅通过允许的公理和工具重新推导出该结果。成功的试验将表明生成能力超越了回忆，而失败则暴露了当前的限制。
### Innovation
这一创新在于提出了‘卸载作为消融测试’的概念，用以测试模型是否能从零开始生成新知识，而不仅仅是重复记忆中的信息。这一方法的独特之处在于它将卸载的概念重新定义为科学界AI的认知探针，而不是侧重于隐私、版权或安全等问题。
### Conclusion
本文提出了一个理论框架，通过最小化模式实验在数学和算法领域展示了其实现的可行性，并讨论了其在物理学或化学等其他领域扩展的可能性。作者强调，这一概念性贡献旨在促进对基于模块测试如何区分重构成知识的模型和仅检索知识的模型的讨论，并讨论了这些测试如何指导下一代科学AI基准测试的发展。
## 970. `cs.LG` - 利用端到端循环Q学习实现双血管加压素的现实CDSS药物剂量控制 [PDF](https://arxiv.org/pdf/2510.01508), [HTML](https://arxiv.org/abs/2510.01508)
### Authors
Will Y. Zou,Jean Feng,Alexandre Kalimouttou,Jennifer Yuntong Zhang,Christopher W. Seymour,Romain Pirracchio
### Background
临床决策支持系统（CDSS）中强化学习（RL）的应用常受到质疑，因为模型可能会推荐不可行的给药决策。本文旨在解决这一问题，通过设计原则上的动作空间来解决在重症监护室（ICUs）管理双血管加压素给药这一挑战。
### Innovation
提出了一种端到端的离线RL框架，直接针对此挑战进行了动作空间设计，将离散、连续和方向性剂量策略与保守的Q学习结合，并加入了一种新颖的基于回忆缓冲器的循环建模方法，以捕捉ICU时间序列数据中的时序依赖关系。此外，通过对比分析不同动作空间形式的去甲肾上腺素给药策略，研究发现设计的动作空间增强了解析性和临床应用性，同时保持了有效性。
### Conclusion
端到端的循环Q学习方法在eICU和MIMIC数据集上的实验结果表明，动作空间设计极大地影响了学习行为策略。与基准方法相比，本文提出的方法实现了超过3倍的期望奖励改进，且符合既定的临床规范。
## 971. `cs.LG` - 象棋博弈神经网络中的迭代推理 [PDF](https://arxiv.org/pdf/2508.21380), [HTML](https://arxiv.org/abs/2508.21380)
### Authors
Elias Sandmann,Sebastian Lapuschkin,Wojciech Samek
### Background
本研究旨在探讨神经网络在其构建表示的过程中，是通过平滑渐进的完善，还是通过更为复杂的过程实现。为了解决这一问题，研究人员选择了超人类象棋引擎Leela Chess Zero的策略网络进行深入分析。
### Innovation
通过扩展logit镜头来分析策略网络，研究表明博弈能力和解题能力在各层间持续提升，但能力的推进发生在不同的计算阶段。这一过程中，候选走法不断被重新评估，最终输出与候选走法的关联性直到较晚阶段才增强，中间层找到的正确解有时会被更高层的解替代。研究还发现，最终层偏好于安全策略而非进攻性策略，这提示了一种机制，即启发式先验可以优先于战术解决方案。
### Conclusion
该研究揭示了神经网络策略网络的迭代推理特性，以及最终层如何重视安全性而非前期的战术选择，为理解神经网络的决策过程提供了新见解。
## 972. `cs.LG` - 记忆自再生：揭示未被遗忘模型中的隐藏知识 [PDF](https://arxiv.org/pdf/2510.03263), [HTML](https://arxiv.org/abs/2510.03263)
### Authors
Agnieszka Polowczyk,Alicja Polowczyk,Joanna Waczyńska,Piotr Borycki,Przemysław Spurek
### Background
现代文本到图像模型能够生成逼真的视觉效果，但这也带来了一个严重的负面影响：它们可能被滥用以生成有害、欺骗性或非法的内容。这促使人们加速开发机器去遗忘的技术。这一新领域致力于从模型的训练数据中选择性地移除特定知识，而不降低其整体性能。然而，忘记特定概念实际上是一个极其困难的任务。模型在对抗性提示攻击下展示了生成所谓的未学习概念的能力，这些概念不仅有害，而且可能违法。
### Innovation
本文提出了关于模型忘记和回忆知识能力的考虑，并引入了Memory Self-Regeneration任务。此外，本文提出了MemoRa策略，这是一种支持有效恢复过去遗忘知识的再生方法。本文还提出，知识检索的稳健性是开发更稳健和有效去遗忘技术的重要但尚未充分探索的评估指标。最后，本文证明忘记概念可以在两种方式上发生：短期忘却，概念可以快速回忆；长期忘却，恢复则更加困难。
### Conclusion
本文通过Memory Self-Regeneration任务展示了模型在短期和长期记忆上的不同表现，并提出MemoRa策略支持有效恢复知识。本文还强调了知识检索稳健性在去遗忘技术评估中的重要性。代码可以在提供的链接中找到。
## 973. `cs.LG` - 优化深度网络 - 根据数据集调整模型深度以提高效率 [PDF](https://arxiv.org/pdf/2510.10764), [HTML](https://arxiv.org/abs/2510.10764)
### Authors
Shaharyar Ahmed Khan Tareen,Filza Khan Tareen
### Background
深度神经网络（DNNs）在各种任务中表现出色，但这种成功往往是以不必要的大模型规模、高计算需求和大量内存占用为代价的。通常，强大的架构会在全深度上进行训练，但许多数据集或任务并不需要如此高的模型容量。在资源相对较低的复杂度数据集上训练大型和深层架构往往会导致过度计算、不必要的能量消耗和过度的内存使用，这使得在资源受限的设备上部署模型变得不切实际。
### Innovation
提出了一种优化深度网络（ODNs）的概念，通过渐进深度扩展的NAS类似训练策略，从浅层开始训练神经网络，并在早期块收敛后逐步增加其深度，直到达到目标精度。ODNs在执行任务所需的最佳深度下运行，移除冗余层，从而降低了后续训练和推理的成本，减少了模型的内存占用，提高了计算效率，促进了在边缘设备上的部署。
### Conclusion
实验结果表明，优化深度的ResNet-18和ResNet-34在MNIST和SVHN上的最佳深度，分别实现了98.64％和96.44％的内存占用减少，同时保持了竞争力的精度99.31％和96.08％。
## 974. `cs.LG` - 学习规矩，再依赖于胜利：具有渐进探索的自模仿强化学习 [PDF](https://arxiv.org/pdf/2509.22601), [HTML](https://arxiv.org/abs/2509.22601)
### Authors
Yulei Qin,Xiaoyu Tan,Zhengbao He,Gang Li,Haojia Lin,Zongyi Li,Zihan Xu,Yuchen Shi,Siqi Cai,Renting Rui,Shaofei Cai,Yuzheng Cai,Xuan Zhang,Sheng Ye,Ke Li,Xing Sun
### Background
强化学习（RL）是提升大型语言模型（LLMs）在长期、低奖励代理任务中策略性工具使用能力的主要范式，但面临着探索与利用的基本权衡挑战。现有研究通过策略熵的视角激励探索，但这种机械的熵最大化容易由于多轮次分布变化导致RL的不稳定性。本文针对在代理自身经验的指导下逐渐平衡探索与利用，避免熵坍塌或失控发散的问题展开研究。
### Innovation
我们提出了一种名为SPEAR的自模仿学习（SIL）训练方法，通过在各个阶段逐渐引导策略熵，结合内在奖励塑造和自模仿学习，平衡探索与利用。该方法在ALFWorld和WebShop等任务中，提升了GRPO/GiGPO/Dr.BoT的成功率，最高可达16.1%/5.1%/8.6%和20.7%/11.8%/13.9%，而在AIME24和AIME25任务中，SPEAR的增强效果分别为3.8%和6.1%。这些改进仅增加了10%-25%的理论复杂性和可忽略的运行时开销，展示了SPEAR模块化的可扩展性。
### Conclusion
SPEAR通过逐步引导策略熵实现了探索与利用的平衡，结合自模仿学习和多轮次分布变化的考虑，显著提高了代理在各种任务中的表现，同时保持了低复杂度和低开销。
## 975. `cs.LG` - 可识别的学习耗散动力学 [PDF](https://arxiv.org/pdf/2510.24160), [HTML](https://arxiv.org/abs/2510.24160)
### Authors
Aiqing Zhu,Beatrice W. Soh,Grigorios A. Pavliotis,Qianxiao Li
### Background
复杂耗散系统存在于科学和工程各个领域，如聚合物、活性物质和学习算法中。这些系统远离平衡状态，能量耗散和时间不可逆性支配其行为，但很难仅从数据中量化这些特性。
### Innovation
我们提出了一种通用且可识别的神经网络框架，可以从轨迹直接学习耗散的随机动力学，同时确保可解释性、表达性和独特性。该方法能够识别独特的能量景观，分离可逆运动和不可逆运动，并可直接计算熵生，提供衡量不可逆性和偏离平衡性的原则性度量。通过聚合物伸展在拉伸流中的应用和随机梯度拉angevin动力学的应用，揭示了新的见解，包括势垒高度的超线性标度和熵生率的次线性标度与应变速率成正比，以及随着批处理大小增加抑制不可逆性。
### Conclusion
我们的方法建立了非平衡动力学发现和解释的一般、数据驱动的框架。
## 976. `cs.LG` - 应对神经网络因果干预导致的非正常表现 [PDF](https://arxiv.org/pdf/2511.04638), [HTML](https://arxiv.org/abs/2511.04638)
### Authors
Satchel Grant,Simon Jerome Han,Alexa R. Tartaglini,Christopher Potts
### Background
传统的机制可解释性方法通常通过针对性地干预模型表示来理解这些表示所编码的内容。然而，这种干预是否会导致模型表示出现分布外（不一致）现象？这些分布外表示是否会影响对模型自然状态的实际解释的准确性？研究表明，常见的因果干预方法通常会将内部表示从目标模型的自然分布中移出，对这种情况提出质疑。因此，本文研究了两类干预导致的差异：一类是无害的，发生在权重的零空间内和行为决策边界内的协方差；另一类是有害的，开启隐藏的网络路径并引发潜在的行为变化。
### Innovation
本文提出了一种新的方法，通过应用和修改Grant (2025)的Counterfactual Latent（CL）损失，使因果干预下的表示更接近自然分布，减少有害差异的可能性，同时保持干预的解释力。
### Conclusion
研究结果强调了一条走向更可靠解释性方法的路径。
## 977. `cs.LG` - 基于随机投影的简单、快速且高效的非退化流形密度估计 [PDF](https://arxiv.org/pdf/2509.25228), [HTML](https://arxiv.org/abs/2509.25228)
### Authors
Ahmad Ayaz Amin,Baha Uddin Kazi
### Background
该研究基于随机矩阵理论和随机投影的几何学，提出了一种名为随机投影流（RPFs）的新框架，用于构建非退化的归一化流。RPFs通过使用经过QR分解的高斯矩阵产生的哈耳分布正交丛上的随机半正交矩阵，将数据投影到低维度的潜在空间，用以表示基础分布。
### Innovation
RPFs与基于PCA的流或学习的非退化映射不同，RPFs具有即插即用的特性，效率高，并且可以导出黎曼体积修正项的闭式解。这些特点使得RPFs在生成建模中具有理论基础和实际有效性。
### Conclusion
该研究证明了RPFs在生成建模中的强大基础性，并为随机投影理论与归一化流之间的桥梁搭建做出了贡献。
## 978. `cs.LG` - SLOFetch: Compressed-Hierarchical Instruction Prefetching for Cloud Microservices [PDF](https://arxiv.org/pdf/2511.04774), [HTML](https://arxiv.org/abs/2511.04774)
### Authors
Zerui Bao,Di Zhu,Liu Jiang,Shiqi Sheng,Ziwei Wang,Haoyun Zhang
### Background
大型网络化服务依赖于复杂的软件栈和微服务编排，这增加了指令足迹并导致前端停滞，从而增加尾延迟和能量消耗。针对这些云工作负载，研究重新审视了指令预取，并提出了一种与SLO驱动和自我优化系统相契合的设计。
### Innovation
基于Entangling Instruction Prefetcher (EIP)，该研究引入了一个压缩入口，通过利用空间聚类，用36位捕捉基址周围的最多八个目的地；还提出了一个分层元数据存储方案，仅保留驻留在L1级别的频繁查询项，并将大量元数据虚拟化到较低级别；此外，还添加了一个轻量级的在线机器学习控制器，使用上下文特征评估预取的盈利性，并根据半 går奖调整阈值。
### Conclusion
在数据中心应用中，该方法在更小的芯片状态中保持了类似于EIP的加速效果，对于机器学习时代的服务，提高了效率。
## 979. `cs.LG` - AirFed: 基于图增强的多智能体强化学习联邦框架用于多无人机协作移动边缘计算 [PDF](https://arxiv.org/pdf/2510.23053), [HTML](https://arxiv.org/abs/2510.23053)
### Authors
Zhiyu Wang,Suman Raj,Rajkumar Buyya
### Background
多无人机（UAVs）协作移动边缘计算（MEC）系统在动态和不确定环境中面临着轨迹规划、任务卸载和资源分配协调的挑战，尤其是在确保服务质量（QoS）的情况下。现有方法存在扩展性有限、收敛速度慢以及智能体间知识分享效率低的问题，特别是在处理具有严格截止时间约束的大规模物联网（IoT）设备部署时更加明显。
### Innovation
该论文提出了AirFed，一种新颖的联邦图增强多智能体强化学习框架，通过三个创新点解决这些挑战。首先，设计了双层动态图注意力网络（GATs），明确建模无人机和物联网设备之间的时空依赖关系，捕捉网络拓扑中的服务关系和服务协作。其次，开发了双智能体单评价者架构，协同优化持续轨迹控制和离散任务卸载决策。第三，提出了基于声誉的分布联邦学习机制，带有梯度敏感自适应量化，实现了跨异构无人机高效且鲁棒的知识共享。
### Conclusion
广泛实验表明，AirFed相比最先进的基线方法实现了42.9%的带权成本降低，截止时间满足率超过99%，物联网设备覆盖率达到94.2%，并且通信开销减少了54.5%。可扩展性分析确认了其在不同无人机数量、物联网设备密度和系统规模下的稳健性能，验证了AirFed在大规模无人机-边缘计算部署中的实际适用性。
## 980. `cs.LG` - 秩稀疏神经网络的泛化界 [PDF](https://arxiv.org/pdf/2510.21945), [HTML](https://arxiv.org/abs/2510.21945)
### Authors
Antoine Ledent,Rodrigo Alves,Yunwen Lei
### Background
近期研究表明，神经网络表现出一种瓶颈秩性质：对于较大的深度，使用梯度方法训练的神经网络的激活和权重大约呈现低秩性质。实际上，每一层的激活秩趋于收敛到一个固定的值，称为“瓶颈秩”，这是表示训练数据所需的最小秩。
### Innovation
该论文研究了该现象对泛化的含义，并证明了如果存在近似的低秩结构，可以直接利用权重矩阵的近似低秩结构来推出泛化界。具体而言，论文学术性地依赖权重矩阵的舒坦p近似范数：对于小的p，边界展示了样本复杂性 Ġ˜O(WrL^2)，其中W和L分别是神经网络的宽度和深度，r是权重矩阵的秩。当p增加时，边界行为更像是基于范数的边界。
### Conclusion
最终结果表明，对于较小的p值，泛化界与样本复杂性 Ġ˜O(WrL^2) 成正比，其中W和L分别是神经网络的宽度和深度，r是权重矩阵的秩。随着p的增加，边界行为更类似于基于范数的边界。
## 981. `cs.LG` - FedQS: 优化半异步联邦学习中的梯度和模型聚合 [PDF](https://arxiv.org/pdf/2510.07664), [HTML](https://arxiv.org/abs/2510.07664)
### Authors
Yunbo Li,Jiaping Gui,Zhihang Deng,Fanchao Meng,Yue Wu
### Background
联邦学习（FL）允许多个实体在不共享原始数据的情况下合作进行模型训练。半异步联邦学习（SAFL）作为一种在同步和异步联邦学习之间取得平衡的方法而崭露头角。然而，SAFL 在优化基于梯度的（例如 FedSGD）和基于模型的（例如 FedAvg）聚合策略方面面临显著挑战。前者能够实现更快的收敛和更高的准确性，但表现出明显的波动性；而后者提供更多的稳定性，但在收敛速度和准确性方面则不如前者。
### Innovation
该论文提出了 FedQS，这是首个在理论上分析并解决 SAFL 中梯度聚合和模型聚合之间差异的框架。FedQS 引入了一种分而治之的策略来处理客户端异质性，通过根据数据分布特征和可用计算资源将客户端分类为四种不同类型，并对它们的本地训练进行自适应优化。广泛实验表明，FedQS 在准确性、最低损失以及收敛速度方面超越了最先进的基线方法，填补了 SAFL 聚合策略之间的差距，为稳定、准确和高效的联邦学习提供了一个统一的解决方案。
### Conclusion
我们的研究工作为 SAFL 中的聚合策略搭建了桥梁，提出了一种稳定的、准确的、高效的联邦学习统一解决方案。相关代码和数据集可以在以下链接中找到：this https URL
## 982. `cs.LG` - ELUTQ: 为边缘设备部署大型语言模型的高效LUT感知量化 [PDF](https://arxiv.org/pdf/2510.19482), [HTML](https://arxiv.org/abs/2510.19482)
### Authors
Xin Nie,Liang Dong,Haicheng Zhang,Jiawang Xiao,G. Sun
### Background
重量量化有效减少了内存使用，使大型语言模型能够部署在基于CPU的边缘设备上。然而，现有的硬件友好型方法通常依赖均匀量化，在低位数设置下会带来权重分布匹配不佳和高的去量化开销。现有的算法难以在满足硬件需求的同时保证计算效率和量化精度。
### Innovation
本文提出了ELUTQ，这是一种高效的量化框架，采用了新型的层次线性量化（HLQ）方法，它可以更好地捕捉权重的统计特征，且不会增加位串LUT基GEMM操作的计算成本。HLQ摆脱了现有量化算法的束缚，能显著提高双精度和三精度下的困惑度减少数值，尤其是与高效的微调技术结合时。ELUTQ还集成了磁盘卸载技术，使得对LLaMA3.1-70B模型进行量化仅需64 GB的CPU内存和48 GB的VRAM，大大减少了大规模模型量化所需的硬件要求。并且通过提供高性能的CPU内核，ELUTQ支持端到端推理。
### Conclusion
通过ELUTQ，2比特量化下的LLaMA2-7B模型在Apple M2芯片4线程配置和批处理大小为1的情况下，吞吐量超过25个标记每秒，显著提高了模型在边缘设备上的部署效率。所有代码可在此URL找到。
## 983. `cs.LG` - 双分支时空自监督表示框架以增强道路网络学习 [PDF](https://arxiv.org/pdf/2511.06633), [HTML](https://arxiv.org/abs/2511.06633)
### Authors
Qinghong Guo,Yu Wang,Ji Cao,Tongya Zheng,Junshu Dai,Bingde Hu,Shunyu Liu,Canghong Jin
### Background
随着各种时空任务的涌现，道路网络表示学习（RNRL）逐渐引起了研究者和实践者的关注。近期的方法采用图神经网络（GNNs）和对比学习来在自监督框架中描述道路段的时空结构。然而，道路网络的空间异质性和时间动态性对自监督GNN的邻域平滑机制构成了严重挑战。
### Innovation
本文提出了一种双分支时空自监督表示框架（DST），通过设计混合跳距转换矩阵来融合道路轨迹的动力学关系，并通过对比标准道路网络和基于新型超图的道路网络来增强空间自监督表示。另外，DST基于因果Transformer预测下一个交通动态，并进一步通过划分工作日和周末的交通模式来正则化此任务，从而实现更优的时空建模。
### Conclusion
广泛的实验表明，所提出框架在对抗现有最佳方法方面具有优势。同时，全面的时空建模有助于DST在零样本学习场景中表现出色。
## 984. `cs.LG` - Vendi信息增益在主动学习中的应用及其在生态学中的应用 [PDF](https://arxiv.org/pdf/2509.10390), [HTML](https://arxiv.org/abs/2509.10390)
### Authors
Quan Nguyen,Adji Bousso Dieng
### Background
通过相机陷阱监测生物多样性已成为生态学研究的重要手段，但在捕获的影像数据中识别物种依然面临主要瓶颈，因为标签资源有限。传统的主动学习方法主要关注单个预测的不确定性，而不考虑整个数据集的不确定性。
### Innovation
引入了一种新的主动学习策略——Vendi信息增益(VIG)，根据图像对预测不确定性在整个数据集中的影响进行选择，同时兼顾信息性和多样性。
### Conclusion
VIG仅需使用可用数据的3%即可达到75%的准确率，而基线方法需要超过10%的数据才能达到相同效果；在10%数据的情况下，VIG的预测准确率达到88%，比基线方法高出12%。这一改进在不同指标和批次大小上都是一致的，并且VIG还收集了更多样化的数据。VIG不仅适用于生态学领域，而且对于数据有限的生物多样性监测环境也具有很高的价值。
## 985. `cs.LG` - 规划在分支定界中：基于模型的强化学习精确组合优化 [PDF](https://arxiv.org/pdf/2511.09219), [HTML](https://arxiv.org/abs/2511.09219)
### Authors
Paul Strang,Zacharie Alès,Côme Bissuel,Olivier Juan,Safia Kedad-Sidhoum,Emmanuel Rachelson
### Background
混合整数线性规划（MILP）在许多现实世界的组合优化问题中起核心作用，这些问题通常通过分支定界（B&B）算法求解。分支定界的效率关键在于指导分支决策的选择性启发式规则。近年来，研究者开始尝试通过调整传统的强化学习（RL）算法来适应B&B环境，旨在通过学习获得针对特定MILP分布的定制分支策略。同时，RL代理也在板游戏等特定类型的组合问题中取得了显著成就，它们通过环境模拟器运用蒙特卡洛树搜索（MCTS）进行策略计划。
### Innovation
引入了Plan-and-Branch-and-Bound（PlanB&B），这是一种基于模型的强化学习（MBRL）代理，利用了对B&B动态的内部模型来发现更好的分支策略。通过计算实验，该方法在四个标准MILP基准测试中超越了此前最先进的RL方法。
### Conclusion
通过引入Plan-and-Branch-and-Bound（PlanB&B）这一基于模型的强化学习代理，研究改善了分支定界算法中的分支决策过程，实验结果显示这种方法在组合优化问题上能够有效地提升算法性能。
## 986. `cs.LG` - 是否需要对齐：为了达到最佳性能的战略多模态表示对齐 [PDF](https://arxiv.org/pdf/2511.12121), [HTML](https://arxiv.org/abs/2511.12121)
### Authors
Wanlong Fang,Tianle Zhang,Alvin Chan
### Background
多模态学习通常依赖于跨模态表示的对齐，以实现有效信息整合，这种对齐长期以来被视为普遍有益。然而，先前的研究主要采取观察性方法，考察自然存在的多模态数据中的对齐情况，并探索其与模型性能之间的相关性，而没有系统地研究不同模态间表示直接对齐对其性能的影响。
### Innovation
本文通过引入可控对比学习模块，在训练过程中允许对齐强度的精确调控，探索了不同数据特性和信息结构下显式对齐如何影响单模态模型的表现和表示对齐。结果表明，显式对齐对单模态模型性能的影响与其数据特性相关：不同模态之间的冗余量决定了最优的对齐程度。
### Conclusion
本文提供了一种实用的指导，说明在何种情况下以及如何应用显式对齐以实现最优单模态编码器性能。同时，也识别出了最适合不同类型数据的对齐强度，以平衡模态特定信号和共享的冗余信息。
## 987. `cs.LG` - 提升ROC优化支持向量机的效率 [PDF](https://arxiv.org/pdf/2511.04979), [HTML](https://arxiv.org/abs/2511.04979)
### Authors
Gimun Bae,Seung Jun Shin
### Background
ROC-SVM（受操作特征曲线优化的支持向量机）最初由Rakotomamonjy提出，直接最大化受操作特征曲线下的面积（AUC），已经成为在类别不平衡条件下常规二分类的有吸引力替代方案。然而，由于其训练过程中需要评估所有$O(n^2)$，导致实际使用受到高计算成本的限制。
### Innovation
我们开发了一种基于不完全U统计量的可扩展ROC-SVM变种，以大幅度降低计算复杂度。此外，我们通过低秩核近似将框架扩展到非线性分类，从而在复制核希尔伯特空间中实现高效的训练。理论分析建立了误差界以证明所提出近似的合理性。实验结果表明，所提出的方法在训练时间大幅减少的情况下，可以获得与原始ROC-SVM相当的AUC性能。
### Conclusion
我们提出的方法实现了在显著降低训练时间的情况下保持与原始ROC-SVM相当的AUC性能。通过不完全U统计量和低秩核近似，我们成功提高了ROC-SVM的可扩展性。
## 988. `cs.LG` - 高容量核霍普菲尔德网络吸引子景观的自组织和谱机制 [PDF](https://arxiv.org/pdf/2511.13053), [HTML](https://arxiv.org/abs/2511.13053)
### Authors
Akira Tamamori
### Background
核相关学习方法能显著增强霍普菲尔德网络的存储容量，但其背后的动态机制尚未充分理解。本文通过统一几何分析的吸引子地形学与核机器的谱理论，填补了这一知识空白。
### Innovation
提出了一个新的度量标准‘顶点锐度’，揭示了吸引子稳定性的丰富相图，并发现了‘优化脊’现象，这一脊线体现了‘力对抗’，其中强大的驱动力与集体反馈力相互平衡。理论分析揭示了这一现象源于权重谱的一种特定重组，称之为‘谱集中’。
### Conclusion
研究提供了高容量联想记忆形成的完整物理图景，表明通过调整系统来平衡谱集中和谱扩散之间的‘刚刚好区域’，可以实现最佳性能。
## 989. `cs.LG` - 对称量子电路的设计及其随机性质 [PDF](https://arxiv.org/pdf/2405.10264), [HTML](https://arxiv.org/abs/2405.10264)
### Authors
Diego García-Martín,Paolo Braccia,M. Cerezo
### Background
参数化和随机单位圆（或正交）n-量子位电路在量子信息中占据核心地位，但与之相联系的对称变换实现电路直到现在还未得到足够的关注，尤其是在$text{Sp}(d/2)$方面，尽管它是$d times d$单位圆辛矩阵的群，对于对称变换的实现至关重要。
### Innovation
论文呈现了一个生成辛代数$text{sp}(d/2)$的普遍集合$text{G}$，其中包括在一维晶格上作用于相邻位点的一位和两位Pauli算符。论文中发现了$text{G}$和单位圆或正交电路等价集合之间的两个关键区别。此外，还通过Schur–Weyl对偶性和Weingarten演算工具证明了当对称随机电路的输出进行Pauli测量时，会收敛到Gaussian过程。通过这些分析，可以获得形成$text{Sp}(d/2)$ t-设计电路的Pauli测量的聚类限制。最后，利用张量网络工具分析了浅的随机对称电路，并通过数值方法展示了单位制基测量在对数深度时可抗聚类。
### Conclusion
在本研究中，通过对生成集合$text{G}$的探讨，揭示了对称量子电路设计的独特性质，并通过随机化方法验证了其在特定深度下的抗聚类特性。
## 990. `cs.LG` - 通过双重代理学习压缩图以实现一致的拓扑鲁棒性评估 [PDF](https://arxiv.org/pdf/2511.18958), [HTML](https://arxiv.org/abs/2511.18958)
### Authors
Qisen Chai,Yansong Wang,Junjie Huang,Tao Jia
### Background
随着图结构数据的日益庞大，评估其在对抗攻击下的鲁棒性变得计算密集且难以扩展。
### Innovation
提出了Cutter，这是一种由VDA和RDA组成的双重代理强化学习框架。Cutter采用了三项关键策略来提高学习效率和压缩质量：轨迹级奖励塑造（将稀疏轨迹收益转换为密集的学习信号）、原型基础上的塑造（使用高、低收益轨迹的行为模式进行引导），以及跨代理模仿（促进更安全、更可转移的探索）。
### Conclusion
在多次真实世界图上的实验表明，Cutter生成的压缩图能够保留关键的静态拓扑属性，并且在各种攻击场景下的鲁棒性衰退趋势与原始图高度一致，从而显著提高了评估效率，同时不损害评估的真实性。
## 991. `cs.LG` - 利用任务算术实现无标注数据矫正式机器遗忘 Subtract the Corruption: Training-Data-Free Corrective Machine Unlearning using Task Arithmetic [PDF](https://arxiv.org/pdf/2511.18660), [HTML](https://arxiv.org/abs/2511.18660)
### Authors
Mostafa Mozafari,Farooq Ahmad Wani,Maria Sofia Bucarelli,Fabrizio Silvestri
### Background
训练数据中普遍存在污染。矫正机器遗忘（CMU）旨在训练后消除这些污染的影响。早期的CMU方法通常假设可以获取被识别的污染训练样本（遗忘集）。但在许多实际场景中，训练数据不可访问。本文提出了源数据不可用的矫正机器遗忘（source-free CMU），在这种情况下，无法指定识别的污染训练样本的遗忘集。现有方法在这种严格条件下表现不佳或适用范围有限。
### Innovation
文中引入了任务空间中矫正遗忘（CUTS），这是一种轻量级的方法，通过代理集使用任务算术原理指导权重空间校正。CUTS将干净数据和污染信号视为不同的任务，通过在代理上对污染模型进行微调来增强权重空间中的污染机制，计算污染权重和微调权重之间的差异作为代理任务向量，并从中减去校准比例的向量以消除污染。CUTS在无干净数据或遗忘集的情况下，能够恢复大量丢失的功能，并几乎消除后门触发攻击，性能优于最先进的特定源数据不可用设置中的CMU方法。
### Conclusion
CUTS方法能够在无干净数据或遗忘集的情况下显著恢复模型性能，有效对抗后门攻击，同时在非特定需求情况下优于现有最先进的方法。
## 992. `cs.LG` - 学习中微子望远镜事件的高效表示 [PDF](https://arxiv.org/pdf/2410.13148), [HTML](https://arxiv.org/abs/2410.13148)
### Authors
Felix J. Yu,Nicholas Kamp,Carlos A. Argüelles
### Background
中微子望远镜能够检测到在宇宙中最极端环境产生的粒子的罕见相互作用。这些望远镜通过在天然透明介质中安装大量光传感器构造了一个边长为一立方千米的体积来实现这一点。由于其巨大的体积和高背景相互作用的频率，这些望远镜积累了大量具有高维度和高变差的大数据。这些特性给数据的分析和重构提出了巨大的挑战，尤其是在使用机器学习技术时。
### Innovation
本文提出了一种名为om2vec的新方法，通过利用变压器变分自编码器高效表示中微子望远镜事件中检测到的光子到达时间分布。这种方法有助于通过学习紧凑且描述性强的潜在表示来简化后续任务。
### Conclusion
实验证明，这些潜在表示提供了更强的灵活性和更高的计算效率，从而促进后续数据处理任务的进行。
## 993. `cs.LG` - Aspiration-based Perturbed Learning Automata in Games with Noisy Utility Measurements. Part A: Stochastic Stability in Non-zero-Sum Games [PDF](https://arxiv.org/pdf/2511.11602), [HTML](https://arxiv.org/abs/2511.11602)
### Authors
Georgios C. Chasparis
### Background
强化学习在建模人类行为和工程设计中的测量或回报优化方案设计方面受到了广泛关注。这类学习方案在去除噪声观察方面显示出多种优势。然而，当应用于分布式体系时，可能表现出一些局限性。在多玩家弱反游戏（multi-player weakly-acyclic games）中，每个玩家采用独立的强化学习动力学，无法保证达到通常认为有利的纯纳什均衡。之前的研究所关注的游戏类型有限，主要集中在潜在游戏和协调游戏上。
### Innovation
本文提出了一个新的 payoff 基准学习方案，即目标驱动变差学习自动机（APLA），并在具有噪声观测值的多玩家正效用游戏中分析了其随机稳定性。这是首次通过建立有限维马尔可夫链等价性来分析通用非零和博弈中的随机稳定性。
### Conclusion
在多玩家正效用游戏中，通过分析目标驱动变差学习自动机在具有噪声观测值情况下的随机稳定性，本文提供了一种分析通用非零和博弈的全新方法。此外，该研究还进一步专门分析了弱反游戏中的随机稳定性。
## 994. `cs.LG` - 修正级联降水-nowcasting中的分布偏移 [PDF](https://arxiv.org/pdf/2511.17628), [HTML](https://arxiv.org/abs/2511.17628)
### Authors
Fanbo Ju,Haiyuan Shi,Qingjian Ni
### Background
降水现在预报旨在利用当前雷达观测数据提供高时空分辨率的降水预测，是区域天气预报的核心任务。目前，级联架构已成为基于深度学习的降水现在预报的主流模式。该架构涉及一个确定性模型来预测后验均值，然后是一个概率模型来生成局部随机性。然而，现有的方法通常忽视了确定性预测中的系统分布偏移与局部随机性之间的融合，导致确定性成分的分布偏移污染了概率成分的预测，尤其在长时间预测中，从而影响降水模式和强度的准确性。
### Innovation
引入了RectiCast，这是一种两级框架，通过双重流匹配模型显式地将均值场偏移的校正从局部随机性的生成中分离出来。第一阶段，确定性模型生成后验均值；第二阶段，引入校正器显式学习分布偏移并生成校正后的均值；随后，生成器基于校正后的均值模型局部的随机性。
### Conclusion
在两个雷达数据集上进行的实验表明，RectiCast 在现有的最先进技术上实现了显著的性能提升。
## 995. `cs.LG` - 一种基于凝聚度评价指标的参数轻量级可扩展光谱方法用于短文本嵌入聚类 [PDF](https://arxiv.org/pdf/2511.19350), [HTML](https://arxiv.org/abs/2511.19350)
### Authors
Nikita Neveditsin,Pawan Lingras,Vijay Mago
### Background
短文本聚类是自然语言处理中的基础任务，但由于需要预先指定聚类的数量且难以有效执行，因此仍然具有挑战性。
### Innovation
提出了一种可扩展的光谱方法，直接从拉普拉斯特征谱的结构中估计聚类的数量，使用余弦相似度构建，并受自适应采样策略的指导。通过自适应采样方法，该估计器能够高效扩展到大规模数据集而不牺牲可靠性。提出了一个名为“凝聚度比例”的简单且可解释的评估指标，量化集群内的相似性超出全局相似背景的程度。这项指标的信息论动机源于互信息。
### Conclusion
广泛的实验表明，在我们的估计器的引导下，标准算法（如k-means和聚类层次分析）显著优于流行的参数轻量级方法（如HDBSCAN，OPTICS和Leiden）。这些结果展示了我们的光谱估计器和凝聚度比例在无监督组织和评估短文本数据中的实用价值。我们的估计器k和凝聚度比例的实现以及用于重现实验的代码可在相关链接获取。
## 996. `cs.LG` - PaSE: Prototype-aligned Calibration and Shapley-based Equilibrium for Multimodal Sentiment Analysis [PDF](https://arxiv.org/pdf/2511.17585), [HTML](https://arxiv.org/abs/2511.17585)
### Authors
Kang He,Boyu Chen,Yuzhe Ding,Fei Li,Chong Teng,Donghong Ji
### Background
多模态情感分析（MSA）旨在通过结合文本、声学和视觉信号来理解人类情感。尽管多模态融合设计用于利用跨模态互补性，但在现实世界中往往会出现模态竞争：占主导地位的模态会压倒较弱的模态，导致性能不佳。
### Innovation
本文提出了一种新的原型对齐校准和舍勒优化平衡框架（PaSE），该框架在增强协作的同时显式地缓解了模态竞争。PaSE首先应用基于原型的校准学习（PCL）来精炼单模表示并通过一种确保语义一致性的对数势最优传输机制来对齐它们。为了进一步稳定优化，引入了双阶段优化策略。首先使用原型门控融合模块提取共享表示，然后采用基于舍勒的梯度调制（SGM）来根据每种模态的贡献适配调整梯度。
### Conclusion
在IEMOCAP、MOSI和MOSEI上的大量实验表明，PaSE在性能上表现出色，并有效地缓解了模态竞争。
## 997. `cs.LG` - 使用序列建模分析心脏衰竭患者轨迹 [PDF](https://arxiv.org/pdf/2511.16839), [HTML](https://arxiv.org/abs/2511.16839)
### Authors
Falk Dippel,Yinan Yu,Annika Rosengren,Martin Lindgren,Christina E. Lundberg,Erik Aerts,Martin Adiels,Helen Sjöland
### Background
临床预测任务中，基于电子健康记录(EHRs)的任务已经被变压器模型定义为最先进的水平。最近提出的Mamba架构在处理长上下文时超越了Llama和Transformer++，同时使用更少的模型参数。尽管这些架构表现令人印象深刻，但在医疗领域，缺乏系统的方法来实证分析不同设置下的模型性能和效率。因此，研究者在瑞典大型心脏衰竭(HF)队列(N=42820)中对六个序列模型进行了评估，探讨了三种架构类（变压器、变压器++、Mamba）在患者入院EHR数据（包括诊断、生命体征、实验室、药物和程序）中进行的一年期预测任务：临床不稳定（再次入院的症状）、初次HF住院后的死亡率以及最新住院后的死亡率的表现。
### Innovation
本研究首次系统地设计了一项消融研究，探讨了输入标记化、模型配置和时间数据预处理方法的选择。研究发现，Llama和Mamba在预测区分度、校准度和任务鲁棒性上表现最优，尤其在相同模型规模下，它们使用25%较少的数据即可获得更佳性能。研究还介绍了在临床预测任务中使用EHRs开发模型时可以借鉴的起始建议。
### Conclusion
该研究提供了一个详尽的序列模型对比分析案例，未来在基于EHRs的心脏衰竭临床预测任务模型开发中，这一研究的设计选择可以作为一个起点。
## 998. `cs.LG` - 基于量子玻尔兹曼机的学习地基状态能量 [PDF](https://arxiv.org/pdf/2410.12935), [HTML](https://arxiv.org/abs/2410.12935)
### Authors
Dhrumil Patel,Daniel Koch,Saahil Patel,Mark M. Wilde
### Background
估计哈密顿操作的能量基态是量子计算机可能有助于的一个基本任务。已经提出了多种方法实现这一目标，包括基于量子相位估测的算法和涉及参数化量子电路的混合量子-经典优化器，后者属于变量子特征解决器的范畴。
### Innovation
该研究分析了量子玻尔兹曼机器在这一任务中的性能，这是一种较少研究的基于参数化热态的策略，且不受“荒漠平岩”问题的影响。该研究还提出了一个混合量子-经典算法，严格证明了该算法在参数空间优化能量函数时可以收敛到ε-近似平稳点，使用样本数量为ε的逆次方、参数数量和优化的哈密顿矩阵范数的多项式数量。该算法通过结合经典随机采样、哈密顿操作模拟和哈达玛测试高效估计能量函数的梯度。
### Conclusion
研究证明了该算法通过高效估计能量函数梯度，能够在ε-逼近性和平稳点间取得良好平衡，并提供了能量函数梯度和海森矩阵的计算，以及用于收敛分析的后者矩阵元素的上界。
## 999. `cs.LG` - 大型语言模型的破戒和漏洞缓解 [PDF](https://arxiv.org/pdf/2410.15236), [HTML](https://arxiv.org/abs/2410.15236)
### Authors
Benji Peng,Keyu Chen,Qian Niu,Ziqian Bi,Ming Liu,Pohsun Feng,Tianyang Wang,Lawrence K.Q. Yan,Yizhu Wen,Yichao Zhang,Caitlyn Heqi Yin,Xinyuan Song
### Background
大型语言模型（LLMs）在过去几年中取得了重大进展，大幅推动了自然语言理解和生成，从而在医疗、软件工程和对话系统领域以外的其他领域中也得到广泛应用。然而，LLMs 在实践中表现出显著的脆弱性，尤其是受到提示注入和模型破解攻击的影响。本文旨在综述这些攻击和缓解策略的研究现状。
### Innovation
文章将攻击方法大致分类为基于提示、基于模型、跨模态和多语言，并涵盖了对手提示、后门注入、跨模态利用等技术。同时，对用于防御机制的提示过滤、变换、对齐技术、多代理防御和自我调节等方法进行了回顾和评估。文章还讨论了衡量LLM 安全性和鲁棒性的关键指标和基准，指出了现有数据集偏见等挑战。此外，文章指出了当前研究中的空白，提出了更具弹性的对齐策略、更先进的防御措施、自动化模型破戒检测以及考虑伦理和社会影响的方向。
### Conclusion
本文强调了在AI社区内继续研究和合作的重要性，以增强LLM的安全性，并确保它们的安全部署。提出了未来的研究方向，旨在对抗不断演变的攻击，提高模型安全性和打击模型破戒的能力。
## 1000. `cs.LG` - 深度学习和全脑网络在寻找生物标志物中的应用：静息状态和认知任务中大脑波动动态的建模 [PDF](https://arxiv.org/pdf/2412.19329), [HTML](https://arxiv.org/abs/2412.19329)
### Authors
Facundo Roffet,Gustavo Deco,Claudio Delrieux,Gustavo Patow
### Background
脑网络模型提供了对脑动态的见解，但模型衍生的分叉参数作为生物标志物的实用性尚未得到充分探索。
### Innovation
该研究使用超临界霍普夫全脑网络模型产生的合成BOLD信号来训练深度学习模型以预测分叉参数，并在人类连接组项目数据上进行推理，评估基于分叉参数分布的脑状态差异性。
### Conclusion
分叉参数有效地区分认知和静息状态，表明其作为脑状态表征和神经系统疾病评估生物标志物的潜力，值得进一步研究。
## 1001. `cs.LG` - BiasJailbreak：分析大型语言模型中的伦理偏见与破解漏洞 [PDF](https://arxiv.org/pdf/2410.13334), [HTML](https://arxiv.org/abs/2410.13334)
### Authors
Isack Lee,Haebin Seong
### Background
大型语言模型（LLMs）虽然在各种任务中表现出色，但也存在安全隐患，如‘jailbreaks’，即恶意输入可以迫使LLMs产生有害内容。研究发现，伦理偏见会导致不同关键词引发的‘jailbreaks’成功率存在显著差异。论文深入分析了LLMs中的伦理偏见及如何利用这些偏见进行‘jailbreaks’。
### Innovation
论文提出了BiasJailbreak的概念，这是一种利用目标LLM自动生成带有偏见的关键词并利用这些关键词生成有害输出的方法。还提出了一种名为BiasDefense的有效防御方法，该方法在生成之前通过注入防御提示来防止‘jailbreak’尝试，这相对于如Llama-Guard这样的Guard模型而言是一个更经济的选择。
### Conclusion
论文强调，伦理偏见可能导致LLMs生成不安全的内容，提出了一种使LLMs更安全和减少偏见的方法。为了促进进一步的研究和改进，论文开源了BiasJailbreak的相关代码和资源，为社区提供了理解并缓解LLMs中因安全引发的偏见的工具。
## 1002. `cs.LG` - RLZero:从语言直接进行政策推理而无需领域内监督 [PDF](https://arxiv.org/pdf/2412.05718), [HTML](https://arxiv.org/abs/2412.05718)
### Authors
Harshit Sikchi,Siddhant Agarwal,Pranaya Jajoo,Samyak Parajuli,Caleb Chuck,Max Rudolph,Peter Stone,Amy Zhang,Scott Niekum
### Background
奖励假设表明，所有目标和目的都可以理解为最大化接收的标量奖励信号。但在实践中，定义这样的奖励信号非常困难，因为人类往往无法预测与奖励函数相对应的最佳行为。自然语言为指示强化学习（RL）代理提供了一种直观的替代方法，但之前的语言制约型方法要么需要昂贵的监督，要么在测试时需要根据语言指令进行训练。一种新方法使用在未标记的、离线的交互中进行训练的预训练RL代理，无需具体任务的监督或标记轨迹，实现了任意自然语言指令的零样本测试时间策略推理。
### Innovation
提出了一种新框架，包括想象、投影和模仿三个步骤，使用预训练RL代理和无监督RL在目标环境中预训练，直接从任意自然语言指令生成行为，无需领域内监督。此外，还可以使用此框架从不同体型的跨体裁视频中生成零样本策略。
### Conclusion
RLZero是首个在多种任务和环境中展示从语言直接生成行为能力的方法，无需任何领域内监督。
## 1003. `cs.LG` - 具有组织层分割感知的生成强化网络（GRN）用于评估慢性下腰痛（cLBP）的3D超声图像中的组织层分割 [PDF](https://arxiv.org/pdf/2501.17690), [HTML](https://arxiv.org/abs/2501.17690)
### Authors
Zixue Zeng,Xiaoyan Zhao,Matthew Cartier,Tong Yu,Jing Wang,Xin Meng,Zhiyu Sheng,Maryam Satarpour,John M Cormack,Allison Bean,Ryan Nussbaum,Maya Maurer,Emily Landis-Walkenhorst,Dinesh Kumbhare,Kang Kim,Ajay Wasan,Jiantao Pu
### Background
本研究旨在开发一种结合图像生成和分割优化的框架，以期减轻数据标注工作量。通过使用69个完全注释的3D超声扫描图像（来自29个受试者的20种组织结构），研究了该框架的功效。
### Innovation
提出了一个名为生成强化网络（GRN）的新颖分割感知联合训练框架，该框架通过反馈分割损失来优化单阶段的图像生成和分割性能。此外，开发了一种称为分割指导增强（SGE）的图像增强技术，确保生成的图像适合特定的分割模型。开发了两种GRN变体：一种用于样本高效学习（GRN-SEL），另一种用于半监督学习（GRN-SSL）。
### Conclusion
GRN-SEL结合SGE可以减少70%的标注努力，同时在Dice相似性系数（DSC）上提高1.98%的性能；而仅GRN-SEL减少了60%的标注努力，GRN-SSL结合SGE以及单独的GRN-SSL分别减少了70%和60%的标注需求，均维持与监督模型相当的性能。这些发现表明GRN框架在显著减少标注数据的情况下提高了分割性能的有效性，为大规模且高效的超声图像分析提供了解决方案，减少了数据标注相关的负担。
## 1004. `cs.LG` - 长上下文语言建模的全面综述 [PDF](https://arxiv.org/pdf/2503.17407), [HTML](https://arxiv.org/abs/2503.17407)
### Authors
Jiaheng Liu,Dawei Zhu,Zhiqi Bai,Yancheng He,Huanxuan Liao,Haoran Que,Zekun Wang,Chenchen Zhang,Ge Zhang,Jiebin Zhang,Yuanxing Zhang,Zhuo Chen,Hangyu Guo,Shilong Li,Ziqiang Liu,Yong Shan,Yifan Song,Jiayi Tian,Wenhao Wu,Zhejian Zhou,Ruijie Zhu,Junlan Feng,Yang Gao,Shizhu He,Zhoujun Li,Tianyu Liu,Fanyu Meng,Wenbo Su,Yingshui Tan,Zili Wang,Jian Yang,Wei Ye,Bo Zheng,Wangchunshu Zhou,Wenhao Huang,Sujian Li,Zhaoxiang Zhang
### Background
长文本、对话等大量文本数据的增加使得高效处理长上下文成为自然语言处理领域的一个持久追求。为了有效和高效地处理和分析大量输入，开发长上下文语言模型（LCLMs）变得尤为重要。
### Innovation
文章提供了一个关于长上下文建模最新进展的全面综述，该综述围绕三个关键方面展开：如何获得有效的LCLMs，如何高效地训练和部署LCLMs，以及如何全面评估和分析LCLMs。此外，还探讨了现有LCLMs的应用场景，并指出了未来开发的方向。
### Conclusion
该论文为长上下文LCLMs的研究和开发者提供了一项及时的文献回顾，旨在成为研究人员和工程师的有价值的资源。相关的GitHub仓库记录了最新文献和开源项目，可在：https://lclm-horizon.com/ 查看到。
## 1005. `cs.LG` - ExDDV: 一个新的用于视频可解释深度伪造检测的数据集 [PDF](https://arxiv.org/pdf/2503.14421), [HTML](https://arxiv.org/abs/2503.14421)
### Authors
Vlad Hondru,Eduard Hogea,Darian Onchis,Radu Tudor Ionescu
### Background
随着生成视频的真实性与质量不断提高，人类越来越难以辨识深度伪造内容，从而更加依赖自动深度伪造检测器。然而，自动检测器也容易出错，并且其决策无法解释，使人容易受到深度伪造欺诈和信息误导的侵害。
### Innovation
介绍了ExDDV，这是第一个用于可解释深度伪造检测的视频数据集和基准。ExDDV包含约5400个真实和深度伪造的视频，并由人工标注文本描述（解释伪影）和点击（指明伪影位置）。对多个视觉-语言模型进行了评估，实验展示了针对深度伪造视频开发的稳健可解释模型需要文本和点击监督，并能够定位和描述观察到的伪影。
### Conclusion
ExDDV数据集和用于复现实验结果的代码已在特定网址提供。
## 1006. `cs.LG` - 不带脑电图的无线多模态可穿戴系统中的Mamba基深度学习睡眠分期方法 [PDF](https://arxiv.org/pdf/2412.15947), [HTML](https://arxiv.org/abs/2412.15947)
### Authors
Andrew H. Zhang,Alex He-Mo,Richard Fei Yin,Chunlin Li,Yuzhi Tang,Dharmendra Gurve,Veronique van der Horst,Aron S. Buchman,Nasim Montazeri Ghahjaverestan,Maged Goubran,Bo Wang,Andrew S. P. Lim
### Background
本文研究了基于Mamba的深度学习方法在ANNE One（由Sibel Health公司研发）上的睡眠分期。ANNE One是一款非侵入性的双模块无线可穿戴系统，可以同时测量胸部心电图（ECG）、三轴加速度计和胸部温度、手指脉搏波形图和手指温度等信号。研究者们从三级医疗睡眠实验室中357名成年人在同步进行多导睡眠图（PSG）记录时获取了可穿戴传感器的记录数据，并手动评分以作为训练和评估模型的基准。通过这种方法，评估了该模型在不同阶段（两类、四类、五类）的性能。
### Innovation
研究创新点在于提出了一种基于Mamba的深度学习方法，能够在没有脑电图（EEG）的情况下，通过使用胸部心电图、三轴加速度计和脉搏波形等非侵入式生理测量数据，准确地推断出主要的睡眠阶段。文中多次提到具体的F1分数、平衡精度等评估指标，表明这种方法在各类数据分割上的准确度和性能，展示了相对于其他方法的优势。
### Conclusion
研究结论概括了基于Mamba的深度学习模型在不使用脑电图的情况下，能够准确推断出主要的睡眠阶段，这种模型可以应用于成人三级医疗睡眠诊所的数据。模型在不同阶段的分类上表现优秀，尤其是三类睡眠阶段的分类效果最佳。
## 1007. `cs.LG` - 机器学习中的超参数优化 [PDF](https://arxiv.org/pdf/2410.22854), [HTML](https://arxiv.org/abs/2410.22854)
### Authors
Luca Franceschi,Michele Donini,Valerio Perrone,Aaron Klein,Cédric Archambeau,Matthias Seeger,Massimiliano Pontil,Paolo Frasconi
### Background
超参数是控制机器学习算法行为的配置变量。它们在机器学习和人工智能中无处不在，选择它们的值决定了基于这些技术的系统的有效性。手动搜索超参数往往耗时且当超参数数量增多时，变得无法实现。自动化搜索是推动、简化和系统化机器学习的重要一步，能够使研究人员和从业者从寻找一组合适的超参数的反复试验中解脱出来。
### Innovation
本文综述了超参数优化的主要技术，包括随机和半随机搜索、基于实验、模型、种群和梯度的方法。此外，还讨论了在线、有约束和多目标的扩展性，以及与其他领域的联系，如元学习和神经架构搜索。
### Conclusion
本文以开放式问题和未来研究方向结尾。
## 1008. `cs.LG` - 关于递归神经网络中拉回吸引子的维数 [PDF](https://arxiv.org/pdf/2501.11357), [HTML](https://arxiv.org/abs/2501.11357)
### Authors
Muhammed Fadera
### Background
基于水库计算范式的递归神经网络在学习和重构来自混沌系统的吸引子方面表现出色，通常能够复制体稳定数和分数维等量值。最近的研究推测，这是因为水库计算机在学习之前将其状态空间嵌入了混沌系统的动力学。这一推测已经在具有线性激活函数的水库计算机中得到验证，但对于更一般的系统仍不清楚。
### Innovation
本文采用非自治动力系统方法，确立了拉回吸引子（在训练和预测阶段被近似的一个子集）的盒计数维数的上界。证明了拉回吸引子的盒计数维数由输入序列（在产品拓扑下）的盒计数维数所限制。特别是，对于源自N维光滑动力系统的输入序列或其通用连续可微观测值，拉回吸引子的盒计数维数的上界是N*in。这些发现强调了尽管递归神经网络可能具有非常高维的状态空间，但它们展示出的有效动态通常是低维的。
### Conclusion
我们的研究结果表明，拉回吸引子的有效低维动力学可能是递归神经网络成功执行如吸引子重构和动态不变量计算（例如体稳定数和分数维）任务的原因之一。
## 1009. `cs.LG` - 基于物理知情学习的非线性系统Kazantzis-Kravaris/Luenberger观察器合成 [PDF](https://arxiv.org/pdf/2501.11655), [HTML](https://arxiv.org/abs/2501.11655)
### Authors
M. Umar B. Niazi,John Cao,Matthieu Barreau,Karl Henrik Johansson
### Background
Kazantzis-Kravaris/Luenberger (KKL) 观测器的设计涉及将系统状态转换到更高维度的观测器状态中的嵌入映射，该状态的动态线性和稳定。观测器状态然后通过反向映射映射回原始系统坐标以获得状态估计。然而，找到这种变换及其逆变换非常具有挑战性。
### Innovation
提出了一种新颖的学习方法，利用物理知情神经网络学习前向映射，然后使用常规前馈神经网络学习其逆映射。论文提供了对于状态估计中的误差和系统不确定性具有鲁棒性的理论保证，包括与有限样本大小相关的非渐近学习保证。
### Conclusion
通过基准示例的数值仿真验证了提出方法的有效性，显示出在训练域外具有更强的泛化能力，相比现有方法具有优越性。
## 1010. `cs.LG` - 为什么推理很重要？多模态推理进展综述(v1) [PDF](https://arxiv.org/pdf/2504.03151), [HTML](https://arxiv.org/abs/2504.03151)
### Authors
Jing Bi,Susan Liang,Xiaofei Zhou,Pinxin Liu,Junjia Guo,Yunlong Tang,Luchuan Song,Chao Huang,Ali Vosoughi,Guangyu Sun,Jinxi He,Jiarui Wu,Shu Yang,Daoan Zhang,Chen Chen,Lianggong Bruce Wen,Zhang Liu,Jiebo Luo,Chenliang Xu
### Background
推理是人类智能的核心，使人们能够跨越多种任务进行结构化问题解决。近年来，大规模语言模型（LLMs）在算术、常识和符号领域的推理能力得到了显著增强。然而，将这些能力有效地扩展到多模态环境（需要模型整合视觉和文本输入）仍然是一个重大挑战。这种多模态推理增加了复杂性，如跨模态处理矛盾信息，需要模型采用先进的解释策略。解决这些挑战不仅需要复杂的算法，还需要评估推理准确性和连贯性的稳健方法。本文提供了一种简洁而深刻的概述，介绍了文本和多模态LLMs中的推理技术。通过全面和最新的比较，我们明确地制定了核心推理挑战和机会，并强调了后训练优化和测试推理的实用方法。
### Innovation
该论文提供了一种简洁而深刻的概述，介绍了文本和多模态LLMs中的推理技术。通过全面和最新的比较，明确了核心推理挑战和机会，并强调了后训练优化和测试推理的实用方法，填补了理论框架和实践实现之间的空白。
### Conclusion
研究提出了有价值的见解和指导，建立了理论框架和实践实现之间的桥梁，并为未来的研究设定了明确的方向。
## 1011. `cs.LG` - 通过修正流减少互信息的缺失数据插补方法 [PDF](https://arxiv.org/pdf/2505.11749), [HTML](https://arxiv.org/abs/2505.11749)
### Authors
Jiahao Yu,Qizhen Ying,Leyang Wang,Ziyue Jiang,Song Liu
### Background
该论文介绍了一种新颖的迭代方法，用于缺少数据插补，该方法顺序地减少了数据与其相应的缺失掩码之间的互信息。该方法受到了基于GAN的生成器训练减少缺失模式可预测性的启发，但本研究更加明确地针对这种互信息的减少。这种方法迭代地最小化插补数据与缺失掩码联合分布与上一个迭代其边缘分布乘积之间的KL散度。
### Innovation
提出了一种减少互信息的方法，具体来说，使插补数据与缺失掩码之间的联合分布与它们边缘分布乘积之间的KL散度最小化。通过求解一个最小化校正流动训练目标的速度场的ODE来实现最优插补。同时，证明了现有的某些插补技术可以被视为本减少互信息框架的近似特殊情况。
### Conclusion
在合成和真实数据集上进行全面实验验证了该方法的有效性，结果显示其在插补性能上具有优势。相关的实现代码托管于 provided URL。
## 1012. `cs.LG` - 理解并优化多阶段人工智能推理管道 [PDF](https://arxiv.org/pdf/2504.09775), [HTML](https://arxiv.org/abs/2504.09775)
### Authors
Abhimanyu Rajeshkumar Bambhaniya,Hanjiang Wu,Suvinay Subramanian,Sudarshan Srinivasan,Souvik Kundu,Amir Yazdanbakhsh,Midhilesh Elavazhagan,Madhu Kumar,Tushar Krishna
### Background
大型语言模型（LLMs）的快速演进引发了对日益复杂的推理管道和硬件平台的需求。现代LLMs服务已超越传统的填充-解码工作流，整合了多重阶段的过程，如检索增强生成（RAG）、关键值缓存检索、动态模型路由和多步骤推理。这些阶段具有多样化的计算要求，需要集成了GPU、ASIC、CPU和内存中心架构的分布式系统。然而，现有的模拟器缺乏对这些异构、多引擎工作流的建模能力，限制了其对架构决策的指导作用。
### Innovation
我们介绍了HERMES，一个异构多阶段LLM推理执行模拟器。HERMES能够建模各种请求阶段，包括RAG、关键值检索、推理、填充和解码，并跨越复杂的硬件结构。HERMES支持异构客户端同时执行多个模型，并采用了先进的批处理策略和多层次内存体系结构。通过将实际硬件跟踪与分析建模结合起来，HERMES捕捉到关键的权衡，如内存带宽竞争、跨集群通信延迟和混合CPU加速器部署中的批处理效率。HERMES通过案例研究探索了推理阶段对端到端延迟的影响、混合管道中的最优批处理策略以及远程关键值缓存检索的架构影响。
### Conclusion
HERMES使系统设计师能够应对LLM推理不断变化的环境，提供了优化硬件-软件协同设计以适应下一代人工智能工作负载的实际见解。
## 1013. `cs.LG` - CoT Red-Handed: Stress Testing Chain-of-Thought Monitoring [PDF](https://arxiv.org/pdf/2505.23575), [HTML](https://arxiv.org/abs/2505.23575)
### Authors
Benjamin Arnav,Pablo Bernabeu-Pérez,Nathan Helm-Burger,Tim Kostolansky,Hannes Whittingham,Mary Phuong
### Background
随着AI模型的自主性不断增加，保证它们不会在未经察觉的情况下进行有害操作变得越来越重要。为应对这一挑战，研究者们提出了一种潜在的缓解方法——通过可信的监测模型持续监控不可信的强大模型的中间推理步骤，这种方法被称为Chain-of-Thought (CoT) 监测。研究还对比了CoT监测与仅审查最终输出的行动监测（action-only monitoring）的效果。实验在红队测试环境下进行，不可信模型被指导执行有害的次要任务同时完成一个编程问题。
### Innovation
研究引入了一种新的混合协议，该协议独立评估模型的推理和行动，并使用加权平均将两者结合。这种混合监控协议在所有测试模型和任务中都表现出了优越性，对于细微欺骗场景，其检测率是行动监测的两倍。
### Conclusion
与仅监视模型输出的方法相比，CoT监测能更有效地发现有害行为，但中间的推理步骤可能包含误导性的理由，使CoT监控系统失效。因此，研究提出了一种混合监控协议，该协议独立评估模型的推理和行动，组合后取得比CoT和行动监测都更好的性能，尤其在细微欺骗场景中表现出更优的检测率。
## 1014. `cs.LG` - 统一的文本-图像到视频生成：一种灵活图像条件训练免费的方法 [PDF](https://arxiv.org/pdf/2505.20629), [HTML](https://arxiv.org/abs/2505.20629)
### Authors
Bolin Lai,Sangmin Lee,Xu Cao,Xiang Li,James M. Rehg
### Background
文本-图像到视频（TI2V）生成是使用语义和视觉条件进行可控视频生成的关键问题。现有的大多数方法通常通过微调将视觉条件添加到文本到视频（T2V）基础模型中，这在资源方面很耗费并且仅限于少数预定义的条件设置。
### Innovation
本文引入了一个统一的TI2V生成形式，并提出了一种名为FlexTI2V的创新的训练免费方法，该方法可以在任意数量和位置的图像上条件化T2V基础模型。首先将条件图像反转为潜在空间中的噪声表示，然后在T2V模型的去噪过程中，使用新颖的随机块交换策略通过局部图像块将视觉特征融入视频表示。为平衡创造力和真实性，使用动态控制机制调整对每个视频帧的视觉条件强度。
### Conclusion
广泛的实验证明，我们的方法比之前的所有训练免费图像条件方法都有显著的进步。我们的方法还可以迁移到基于UNet和基于转换器的架构中。
## 1015. `cs.LG` - 链接奇异模型中WAIC和WBIC的渐近方程 [PDF](https://arxiv.org/pdf/2505.13902), [HTML](https://arxiv.org/abs/2505.13902)
### Authors
Naoki Hayashi,Takuro Kutsuna,Sawa Takamuku
### Background
在统计学习中，模型被分类为正常模型或奇异模型，视参数到概率分布映射的单射性而定。大多数具有层次结构或潜变量的模型是奇异的，这些模型的常规准则如赤池信息标准(Akaike Information Criterion, AIC)和贝叶斯信息标准(Bayesian Information Criterion, BIC)由于似然函数和后验分布的经典近似失效而不再适用。为了解决这一问题，已经提出了广泛适用的信息准则(Widely Applicable Information Criterion, WAIC)和广泛适用的贝叶斯信息准则(Widely Applicable Bayesian Information Criterion, WBIC)。然而，这些准则分别依赖于不同后验分布进行计算，通常需要单独的后验抽样。
### Innovation
本文理论地推导出一个渐近方程，将WAIC和WBIC联系起来，尽管它们依赖于不同的后验分布。这个方程提供了WAIC在基于WBIC后验分布情况下的一种渐近无偏表达式。这种链接揭示了这两种准则在奇异学习理论框架中的结构关系，并加深了对它们渐近行为的理解。这一理论贡献为未来奇异模型中模型选择计算效率的发展提供了基础。
### Conclusion
本文的理论贡献为奇异模型选择中模型选择的计算效率的发展提供了基础，加深了对奇异学习理论框架中WAIC和WBIC的理解。
## 1016. `cs.LG` - Adjoint Schrödinger Bridge Sampler [PDF](https://arxiv.org/pdf/2506.22565), [HTML](https://arxiv.org/abs/2506.22565)
### Authors
Guan-Horng Liu,Jaemoo Choi,Yongxin Chen,Benjamin Kurt Miller,Ricky T. Q. Chen
### Background
近年来，从玻尔兹曼分布采样计算方法有了显著进展，尤其是当目标分布仅知未规范化能量函数时。然而，由于缺乏显式目标样本，以往基于扩散的方法（称为扩散采样器）常常需要重要加权估计或复杂的训练过程。这两种方法都会牺牲可扩展性，因为它们需要大量的能量和模型评估，从而限制了它们的实际应用。
### Innovation
本文提出了一种新的扩散采样器——伴随薛定谔桥采样器（Adjoint Schrödinger Bridge Sampler, ASBS），它通过简单且可扩展的目标匹配方法进行采样，无需在训练过程中估计目标样本。ASBS 基于薛定谔桥的数学模型，通过动力学最优传输提高采样效率。通过新的随机最优控制理论视角，ASBS 演示了如何通过伴随匹配大规模学习基于薛定谔桥的扩散采样器，并证明了其全局收敛性。值得注意的是，ASBS 放宽了最近伴随采样（Havens et al., 2025）中所谓的无记忆条件，从而扩大了设计空间。
### Conclusion
通过全面的实验，本文展示了ASBS在从经典能量函数采样、自举构象生成和分子玻尔兹曼分布采样方面的有效性。代码可访问 [此链接]。
## 1017. `cs.LG` - Deep Gaussian过程中的稀疏技术用于回归 [PDF](https://arxiv.org/pdf/2505.11355), [HTML](https://arxiv.org/abs/2505.11355)
### Authors
Jonas Latz,Aretha L. Teckentrup,Simon Urbainczyk
### Background
Gaussian过程（GPs）因其灵活性和内置的不确定性量化方法在回归和函数近似中受到欢迎。然而，当训练数据量大或潜在函数包含难以通过稳定核表示的多尺度特征时，GPs会受到影响。为了解决前者，通过诱导点近似（稀疏GP回归）提高GPs在大规模数据集上的训练效率。后者通过使用多层次的GPs（即深GPs）来解决，通过结合多个GPs来解析多尺度特征。但是，深层GPs的后验推断需要采样或变分近似，这导致复杂的优化问题，且样本的不确定性表达不够准确。
### Innovation
本文提出了一种新方法，通过结合变分学习和马尔可夫链蒙特卡洛（MCMC）方法，发展了一种基于粒子的期望最大化算法，同时在大规模数据中找到诱导点（变分方法）和准确训练深层GPs（基于采样的方法），从而提高在大规模数据上训练深层GPs的效率和准确性。
### Conclusion
该方法在标准基准问题上进行了测试，结果显示它是一个高度高效且准确的深层GP训练方法，适用于处理大规模数据集。
## 1018. `cs.LG` - LEANN: 一种低存储向量索引 [PDF](https://arxiv.org/pdf/2506.08276), [HTML](https://arxiv.org/abs/2506.08276)
### Authors
Yichuan Wang,Zhifei Li,Shu Liu,Yongji Wu,Ziming Mao,Yilong Zhao,Xiao Yan,Zhiying Xu,Yang Zhou,Ion Stoica,Sewon Min,Matei Zaharia,Joseph E. Gonzalez
### Background
向量搜索嵌入在许多重要应用中，例如推荐系统和检索增强生成（RAG）中。它依赖于向量索引来实现高效的搜索。然而，这些索引需要存储高维嵌入和大量索引元数据，其总大小可能是原始数据（例如，文本片段）的几倍。这种高存储开销使得在个人设备或大规模数据集上部署向量搜索变得困难甚至不切实际。
### Innovation
我们提出了LEANN，一种高效的向量搜索索引，通过在需要时实时重新计算嵌入而不是存储它们，并压缩最先进的近邻图索引同时保留搜索准确性来解决问题。LEANN在使用仅为原始数据的一小部分存储空间（例如5%）的情况下提供高质量的向量搜索，并支持高效的索引构建和更新。与传统索引相比，LEANN在真实世界的基准测试中将索引大小最多减少50倍，同时保持最佳准确率并具有可比的延迟。
### Conclusion
LEANN提供了高质量的向量搜索，使用仅为原始数据一小部分的存储空间，并支持高效的索引构建和更新。在实际基准测试中，LEANN相比传统索引将索引大小最多减少50倍，同时保持最佳的准确率和可比较的延迟，特别是在RAG应用程序中。
## 1019. `cs.LG` - FedPromo：利用边缘端的轻量级代理模型将新领域引入基础模型 [PDF](https://arxiv.org/pdf/2508.03356), [HTML](https://arxiv.org/abs/2508.03356)
### Authors
Matteo Caligiuri,Francesco Barbato,Donald Shenaj,Umberto Michieli,Pietro Zanuttigh
### Background
联邦学习（FL）是一种在去中心化数据上训练深度学习模型的成熟范式。然而，随着模型规模的增长，传统的FL方法往往需要大量的计算资源，这在许多客户端设备上可能不可行。
### Innovation
提出了一种名为FedPromo的新框架，该框架能够在中央服务器存储的大规模基础模型上，通过联邦学习优化远程客户端从未遇到的新领域的轻量级代理模型，避免了直接在客户端设备上训练大型模型，显著减少了计算开销并维护了隐私。
### Conclusion
通过新颖的正则化策略，我们的框架实现了分布式多领域学习，平衡了性能、隐私和资源效率。在五个图像分类基准上的实验结果表明，FedPromo在假设资源有限的客户端情况下，超过了现有方法。
## 1020. `cs.LG` - RoPECraft：基于轨迹引导的RoPE优化无训练运动转输方法 [PDF](https://arxiv.org/pdf/2505.13344), [HTML](https://arxiv.org/abs/2505.13344)
### Authors
Ahmet Berke Gokmen,Yigit Ekin,Bahri Batuhan Bilecen,Aysegul Dundar
### Background
该研究提出了RoPECraft方法，这是一种无需训练的视频运动转输方法，适用于扩散变换器。传统的视频运动转输方法通常需要大量的训练数据或复杂的自适应过程。而RoPECraft通过修改旋转位置嵌入（RoPE）的复指数张量，直接在生成过程中编码运动信息，从而实现运动转输。
### Innovation
RoPECraft的主要创新点在于它直接利用参考视频的密集光流信息，调整RoPE的复指数张量，从而在生成过程中动态编码运动信息。此外，通过轨迹对齐优化技术，提高生成结果的质量。另外，引入基于参考视频傅里叶变换相位的正则化项，以保持生成结果与文本提示的一致性，减少高频伪影。
### Conclusion
实验结果表明，RoPECraft在基准测试中在定性和定量上都优于所有最近发表的方法。这一方法为无训练的视频运动转输提供了新的解决方案。
## 1021. `cs.LG` - FMPlug: 插件基础流动匹配先验用于逆问题 [PDF](https://arxiv.org/pdf/2508.00721), [HTML](https://arxiv.org/abs/2508.00721)
### Authors
Yuxiang Wan,Ryan Devera,Wenjie Zhang,Ju Sun
### Background
该论文背景介绍了在解决逆问题时传统方法的局限性，如依赖于特定领域的或未经训练的先验信息。这些方法可能受到单一领域信息的限制，且效果可能一般。因此，需要一个更加通用且高效的解决办法。
### Innovation
FMPlug 提出了一种新颖的插件框架，通过利用已观察到的对象与所需对象之间的相似性以及生成流的高斯性这两个关键洞察，增强了基础流动匹配（FM）先验。引入了时间自适应预热策略和锐利高斯性正则化，以充分发挥领域无关基础模型的潜力。
### Conclusion
FMPlug 在图像超分辨率和高斯去模糊方面的效果显著优于使用基础 FM 先验的现有方法，展示了其在逆问题解决中的有效性和优越性。
## 1022. `cs.LG` - 利用视觉语言模型进行时间序列异常检测 [PDF](https://arxiv.org/pdf/2506.06836), [HTML](https://arxiv.org/abs/2506.06836)
### Authors
Zelin He,Sarah Alnegheimish,Matthew Reimherr
### Background
时间序列异常检测（TSAD）在医疗、金融和基于传感器的状况监测等多个领域中扮演着重要角色。尽管传统的TSAD方法主要集中在针对数值数据训练领域特定模型上，但这些方法缺乏人类专家所拥有的视觉-时间理解能力，以识别上下文异常。因此，本文探讨了一种基于视觉语言模型（VLMs）的解决方案。
### Innovation
提出了一种双阶段解决方案，包括(1)基于相对轻量级预训练视觉编码器的视觉筛选阶段ViT4TS，利用2D时间序列表示来准确定位候选异常；(2)VLM4TS，基于VLM的时间序列阶段，通过整合全球时间上下文和VLM的视觉理解能力，进一步细化由ViT4TS提供的候选异常检测。结果显示，在无需时间序列训练的情况下，VLM4TS通常优于时间序列预训练和从零开始的基线，在F1-最大得分上提升了24.6%。此外，VLM4TS还一致地优于现有的基于语言模型的TSAD方法，并且在标记使用效率上平均提高36倍。
### Conclusion
证明了VLM4TS在时间序列异常检测中的优势，尤其是在无需时间序列训练的情况下，显著提升了检测性能，并且在标记使用效率上获得了很大改进。
## 1023. `cs.LG` - SafeFix: 通过可控图像生成进行有针对性的模型修复 [PDF](https://arxiv.org/pdf/2508.08701), [HTML](https://arxiv.org/abs/2508.08701)
### Authors
Ouyang Xu,Baoming Zhang,Ruiyu Mao,Yunhui Guo
### Background
深度学习模型在视觉识别中往往表现出系统性的错误，这些错误是由于语义子群体的代表性不足导致的。尽管现有的调试框架可以通过识别关键失败属性来定位这些失败点，但有效修复模型仍然是一个难题。当前的解决方案通常依赖于手工设计的提示生成合成训练图像，这种方法容易出现数据分布偏移和语义错误。
### Innovation
本文引入了一个模型修复模块，该模块依赖于一个可解释的失败归因流程。通过使用条件文本到图像模型为故障案例生成语义准确且有针对性的图像。为了保证生成样本的质量和相关性，进一步利用大型视觉语言模型（LVLM）对输出进行过滤，强制与原始数据分布对齐并保持语义一致性。通过使用这种针对罕见案例增强的合成数据集重新训练视觉模型，显著减少了罕见案例相关的错误。实验表明，这种有针对性的修复策略可以提高模型的鲁棒性，而不引入新的错误。
### Conclusion
通过基于罕见案例增强的合成数据集的重新训练，证明了这种针对性的修复策略可以显著降低错误，提高模型的鲁棒性并避免引入新的错误。该代码可以在提供的网址处找到。
## 1024. `cs.LG` - MMTU：大规模多任务表格理解与推理基准 [PDF](https://arxiv.org/pdf/2506.05587), [HTML](https://arxiv.org/abs/2506.05587)
### Authors
Junjie Xing,Yeye He,Mengyu Zhou,Haoyu Dong,Shi Han,Lingjiao Chen,Dongmei Zhang,Surajit Chaudhuri,H. V. Jagadish
### Background
表格和基于表格的应用在重要现实世界应用中扮演着重要角色，如电子表格、数据库和计算笔记本。传统上，这些应用需要专家级别的用户来操作，如数据工程师、数据分析师和数据库管理员。尽管大语言模型（LLMs）在处理表格方面取得了显著的进步（例如，在电子表格和数据库协作助理场景中），但在表格相关任务的全面基准测试方面仍存在局限性。与大量的自然语言处理（NLP）基准不同，现有的表格相关任务评估相对稀缺，主要关注自然语言到SQL查询和表格问题解答等具体任务，忽略了专业用户面临的更广泛的任务范围。这一差距限制了我们对该领域的理解和模型进步。
### Innovation
本文介绍了一个大规模的基准测试MMTU，它包含了超过28K个问题，覆盖了25项实际表格任务，旨在全面评估模型理解、推理和处理真实表格的能力。这些任务从计算机科学几十年来的表格数据研究中汲取，并特别关注专业用户面临的各种复杂任务。我们展示了MMTU所需的技能——包括表格理解、推理和编程——这些技能对当今前沿模型仍然具有挑战性，在前沿推理模型如OpenAI GPT-5和DeepSeek R1中，分别得分约为69%和57%，表明改进空间巨大。我们通过MMTU评估凸显了关键发现，并希望通过这一基准推动结构化数据处理与分析基础模型的理解与开发。
### Conclusion
我们希望通过MMTU基准测试，推动对结构化数据处理与分析基础模型的理解和开发，其代码和数据可在相关链接中获得。
## 1025. `cs.LG` - MeshSplat: Gaussian 拟合 稀疏 视图 表面 重构 [PDF](https://arxiv.org/pdf/2508.17811), [HTML](https://arxiv.org/abs/2508.17811)
### Authors
Hanzhi Chang,Ruijie Zhu,Wenjie Chang,Mulin Yu,Yanzhe Liang,Jiahao Lu,Zhuoyuan Li,Tianzhu Zhang
### Background
计算机视觉和图形学领域广泛研究表面重构问题。然而，现有方法在输入视图极度稀少的情况下难以恢复准确的场景几何。
### Innovation
我们提出了MeshSplat，一种通过高斯 拟合解决稀疏视图表面重构的通用框架。关键思想是利用2D高斯 拟合作为桥梁，将新颖视图合成与学习到的几何先验联系起来，然后将这些先验应用于表面重构。具体而言，我们引入了前馈网络来预测每个视图的像素对齐的2D高斯 拟合，这使得网络能够合成新颖视图图像，并且省去了直接的3D 地图监督。此外，我们提出了一种加权 柏松距离损失来规范深度图，尤其是在输入视图的重叠区域，并提出了一种法线预测网络来使2D高斯 拟合的方向与单目法线估计器预测的法线方向对齐。
### Conclusion
广泛的实验验证了我们的改进措施的有效性，表明我们的方法在通用稀疏视图网格重构任务中达到了最先进的性能。
## 1026. `cs.LG` - 通过频率选择缓解混合频率的指数增长 [PDF](https://arxiv.org/pdf/2508.10533), [HTML](https://arxiv.org/abs/2508.10533)
### Authors
Michael Poppel,David Bucher,Maximilian Zorn,Nico Kraus,Philipp Altmann,Jonas Stein,Claudia Linnhoff-Popien
### Background
量子机器学习研究由于潜在的计算优势而迅速扩展，角度编码作为一种流行的选择被用作特征映射（FM），用于将经典数据嵌入到量子模型中，因为它简单而且能够自然生成截断的傅里叶级数，提供通用函数近似能力。量子电路中的高效特征映射能够利用傅里叶频率的指数级扩展，多维输入还会引入经过混合频率的额外指数增长。尽管这种强大的表示能力，实际实施仍面临重大挑战。
### Innovation
通过针对白盒目标函数的受控实验，本文展示了即便在理论上所有相关频率都是可访问的，训练失败仍然可能发生。我们提出了参数初始化为近零值的方法来抑制不需要的重复频率。对于具有先验频率知识的目标函数，我们介绍了一种频率选择方法，这种方法可以减少参数需求，并减轻由于参数不足而产生的指数增长问题，从而实现近最优性能（中位数 $R^2 thickapprox 0.95$）。
### Conclusion
频率选择方法使得使用78%的标准方法所需参数数量在10个随机选择的目标函数中达到了几乎最佳性能。
## 1027. `cs.LG` - FlagEval Findings Report: 一项关于自动可验证文本和视觉问题的大推理模型初步评估的报告 [PDF](https://arxiv.org/pdf/2509.17177), [HTML](https://arxiv.org/abs/2509.17177)
### Authors
Bowen Qin,Chen Yue,Fang Yin,Hui Wang,JG Yao,Jiakang Liu,Jing-Shu Zheng,Miguel Hu Chen,Richeng Xuan,Shibei Meng,Shiqi Zhou,Teng Dai,Tong-Shuai Ren,Wei Cui,Xi Yang,Xialin Du,Xiaojing Xu,Xue Sun,Xuejing Li,Yaming Liu,Yesheng Liu,Ying Liu,Yonghua Lin,Yu Zhao,Yunduo Zhang,Yuwen Luo,Zheqi He,Zhiyuan He,Zhongyuan Wang
### Background
本文介绍了对当前大型推理模型（LRMs）进行的一项中等规模的无污染评估，包括一些初步发现。同时也发布了用于视觉语言模型的评估基准ROME，以测试模型从视觉线索中进行推理的能力。
### Innovation
提出了针对大型推理模型的评估基准ROME，旨在测试模型从视觉线索中进行推理的能力。
### Conclusion
作者团队进行了初步的评估，发现了一些初步结果，并公开了评估基准和数据，以便进一步研究和改进推理模型。
## 1028. `cs.LG` - 从化学配置空间角度看，低保真度作为偏差的主动学习（低保真度作为偏差的主动学习） [PDF](https://arxiv.org/pdf/2508.15577), [HTML](https://arxiv.org/abs/2508.15577)
### Authors
Vivin Vinod,Peter Zaspel
### Background
主动学习通过优化训练样本的选择，为机器学习模型构建提供了一种最优方法。尽管通常通过减少模型的方差来实现，实际效果往往不如单纯的随机抽样。基于偏差和方差的分解理论，该研究提出通过最小化模型的偏差，而非方差，来改进样本选择策略。
### Innovation
研究提出了一种新颖的方法——利用易于计算的低保真度数据近似模型偏差，这种方法特别适用于$triangle$-ML或多保真度机器学习。该方法在量子化学等多个应用领域的示例中表现出色，显著减少了训练数据的使用量。
### Conclusion
通过这种基于低保真度数据的新颖方法，可以几乎精确地匹配所有贪婪样本选择方法的最佳预测误差。在量子化学等应用中，该方法将训练数据的使用量减少了十倍。
## 1029. `cs.LG` - CardioComposer: 利用可微分几何实现解剖扩散模型的组件化控制 [PDF](https://arxiv.org/pdf/2509.08015), [HTML](https://arxiv.org/abs/2509.08015)
### Authors
Karim Kadry,Shoaib Goraya,Ajay Manicka,Abdalla Abdelwahed,Naravich Chutisilp,Farhad Nezami,Elazer Edelman
### Background
生成模型可以用于合成有助于临床研究和医疗设备评估的3D心血管解剖结构，但它们会面临几何可控性和逼真度之间的权衡。目前的方法难以同时实现两者的平衡。
### Innovation
提出了一种名为CardioComposer的可编程、推理时框架，用于基于可解释椭球体原语生成多类解剖标签图。通过开发基于体素几何矩的可微测量函数，可以在扩散模型采样过程中提供基于损失的梯度引导。这种方法能够以独立方式约束各个几何属性，并提供对多个子结构的组合控制，同时适用于具有非凸子结构的广泛解剖系统。
### Conclusion
CardioComposer 方法适用于多种包含非凸子结构的解剖系统，包括心脏、血管和骨骼器官，展示了其对几何属性分离控制和子结构组合控制的能力。
## 1030. `cs.LG` -  OceanGym: 一种水下具身代理基准环境 [PDF](https://arxiv.org/pdf/2509.26536), [HTML](https://arxiv.org/abs/2509.26536)
### Authors
Yida Xue,Mingjun Mao,Xiangyuan Ru,Yuqi Zhu,Baochang Ren,Shuofei Qiao,Mengru Wang,Shumin Deng,Xinyu An,Ningyu Zhang,Ying Chen,Huajun Chen
### Background
水下环境设置了极大的感知和决策挑战，包括低能见度、动态海洋水流，这让有效代理部署变得极其困难。不同于陆地或空中领域，水下环境为AI技术的发展带来了独特的挑战。
### Innovation
OceanGym是第一个全面的水下具身代理基准，涵盖了八个现实任务领域，并由多模态大语言模型（MLLM）驱动，统一了感知、记忆和序列决策。通过提供一个高保真、严谨设计的平台，OceanGym旨在建立一个开发鲁棒具身AI的试验场，并将其能力转移到实际的自主水下车辆中。
### Conclusion
OceanGym通过为探索极其具有挑战性的海洋环境提供一个平台，展示了在感知、计划和适应方面的巨大差距，标志着朝着能够在地球最后一个未被探索的前沿实现智能代理的重要一步。相关代码和数据可以在提供的链接中获取。
## 1031. `cs.LG` - 探索大规模语言模型下定量因子和新闻流动表示的协同效应在股票收益预测中的应用 [PDF](https://arxiv.org/pdf/2510.15691), [HTML](https://arxiv.org/abs/2510.15691)
### Authors
Tian Guo,Emmanuel Hauptmann
### Background
在量化投资中，收益预测支持多种任务，如股票选择、投资组合优化和风险管理。定量因素，例如价值、质量与增长，捕捉了股票的多种特性。非结构化数据，例如新闻和会议纪要，由于大型语言模型（LLMs）近年发展的推动，受到了越来越多的关注。本文探讨了如何有效利用多模态因素和新闻流动特征进行收益预测，并进行了股票选择。
### Innovation
本文提出了一种融合学习框架，用于从通过LLM生成的因素和新闻流动表示学习统一表示。对比了三种不同复杂性的方法：表示组合、表示求和和注意表示。在实证比较中，由于发现融合学习的局限性，进一步探索了能够自适应组合单一模态预测及其融合的混合模型，并引入了分阶段的训练方法以缓解混合模型的训练不稳定性。
### Conclusion
实验结果显示几个有效见解，涉及在股票收益预测和选择中多模态因素和新闻的有效建模。
## 1032. `cs.LG` - AI-在环路中：通过利用LLMs和联邦学习实现隐私保护的实时 scam 检测和对话型 scam 钓鱼 [PDF](https://arxiv.org/pdf/2509.05362), [HTML](https://arxiv.org/abs/2509.05362)
### Authors
Ismail Hossain,Sai Puppala,Md Jahangir Alam,Sajedul Talukder
### Background
现有的防骗措施大都基于事后反应，仅在用户互动时提供有限的保护。实时社交工程诈骗手法，如钓鱼、冒充和电话诈骗，依然在网络平台上持续存在并不断演变。现有防御措施反应滞后，无法有效应对这类动态威胁。
### Innovation
本文提出了一种隐私保护、AI参与的框架，能够实时检测并中断诈骗对话。该系统结合了指令调优的AI与兼顾安全性的奖励函数。此外，使用联邦学习方法，可以在不分享原始数据的情况下实现模型的持续更新。实验结果显示，该系统能产出流畅且吸引人的回复（困惑度低至22.3，参与度约为0.80），并且人类研究证实其在现实感、安全性和有效性方面显著超越了基准模型。在联邦学习背景下，使用FedAvg训练的模型能够持续多达30轮，同时保持高水平的参与度（约0.80）、高相关性（约0.74）和低个私信息泄露率（≤0.0085）。即便有差分隐私保护，围绕新颖性和安全性的稳定性表现良好，显示出在不牺牲性能的情况下实现安全隐私保护的可能性。
### Conclusion
这是首个将实时 scam 棵骗、联邦隐私保护和协调安全调节融合于一体的主动防御模型。通过更严格的调节，虽然可以减少个人信息暴露的几率，但也限制了对话的深度；相比之下，更宽松的设置能促进更长和更丰富的对话，尽管这增加了个人隐私泄露的风险。
## 1033. `cs.LG` - 基于验证生成模型的学习型拟合优度方法 [PDF](https://arxiv.org/pdf/2511.09118), [HTML](https://arxiv.org/abs/2511.09118)
### Authors
Pietro Cappelli,Gaia Grosso,Marco Letizia,Humberto Reyes-González,Marco Zanetti
### Background
生成模型日益成为科学研究工作流程中的核心部分，但它们的系统应用及其解释需要通过严谨的验证来理解其局限性。经典的检验方法在处理高维数据时面临可扩展性、统计能力和解释性方面的挑战，这使得在实际且高维的科学环境中认证这些模型的可靠性变得困难。
### Innovation
提出了使用新型物理学习机（NPLM）进行拟合优度检验的方法。NPLM是一种基于学习的方法，受到Neyman-Pearson构造的启发，专门用于验证高维科学数据训练的生成网络。
### Conclusion
NPLM不仅能够作为强大的验证方法使用，还能够诊断数据中欠拟合的部分区域。
## 1034. `cs.LG` - LightMem：一种轻量级高效的增强记忆生成系统 [PDF](https://arxiv.org/pdf/2510.18866), [HTML](https://arxiv.org/abs/2510.18866)
### Authors
Jizhan Fang,Xinle Deng,Haoming Xu,Ziyan Jiang,Yuqi Tang,Ziwen Xu,Shumin Deng,Yunzhi Yao,Mengru Wang,Shuofei Qiao,Huajun Chen,Ningyu Zhang
### Background
尽管大型语言模型具有出色的性能，但在动态和复杂的环境中，它们难以有效利用历史交互信息。现有的记忆系统虽然引入了持久的信息存储、检索和利用机制，但通常会带来大量的时间和计算开销。
### Innovation
本文提出了一种新的记忆系统——LightMem，旨在平衡记忆系统性能和效率。LightMem 受人类记忆的 Atkinson-Shiffrin 模型启发，将记忆组织为三个互补阶段：首先，通过轻量级压缩和按主题分组快速过滤无关信息的认知启发式感觉记忆；其次，主题意识的短期记忆合并这些主题组，并对其进行组织和总结，以便结构化访问；最后，具有睡眠期间更新的长期记忆采用离线过程，将巩固与在线推理脱钩。
### Conclusion
在LongMemEval和LoCoMo上使用GPT和Qwen作为骨干网络，LightMem在知识问答准确性、总令牌使用量和API调用次数方面均优于强大基础模型，分别提高了最高7.7%/29.3%，总令牌使用量减少至最多38倍/20.9倍，API调用次数减少至最多30倍/55.5倍，而纯在线测试时间成本更低，总令牌减少至最高106倍/117倍，API调用次数减少至最高159倍/310倍。
## 1035. `cs.LG` - 如何寻找优秀的AI论文：自我评价作为超越同行评审的科学影响力预测强大力量 [PDF](https://arxiv.org/pdf/2510.02143), [HTML](https://arxiv.org/abs/2510.02143)
### Authors
Buxin Su,Natalie Collina,Garrett Wen,Didong Li,Kyunghyun Cho,Jianqing Fan,Bingxin Zhao,Weijie Su
### Background
学术研究的同行评审不仅旨在确保事实的正确性，还旨在识别具有高科学潜力的研究工作，这些工作能够塑造未来的研究方向。特别是在快速发展的人工智能领域，面对日益增多的投稿数量，这一任务变得尤为重要但更加困难。本研究旨在探讨一种未被充分探索的高影响力研究识别指标：作者对自己在同一个AI会议上提交的多个作品的自我排名。基于博弈论的推理，研究者们假设自我排名具有信息价值，因为作者对其作品概念深度和长期潜力有独特理解。
### Innovation
本研究采用了一个大规模实验，通过让1,342名研究人员对其2,592篇提交进行自我排名，以此来检验上述假设。结果发现最高的自我排名作品获得的引用次数是最低排名作品的两倍，并且自我排名特别有效于识别高被引作品（超过150次引用）。此外，研究还表明自我排名比同行评审得分更能预测未来的引用次数。研究结果在考虑预印本发布时间和自引等混淆变量后仍然稳健。这些发现表明，作者的自我排名可以作为同行评审的有效补充，用于识别和提高AI领域的高影响力研究。
### Conclusion
本研究展示了作者的自我排名为识别和提升AI领域的高影响力研究提供了一种可靠而有价值的补充方式，超越传统的同行评审机制。
## 1036. `cs.LG` - 少而精：高效编码代理的迭代控制策略实证研究 [PDF](https://arxiv.org/pdf/2510.16786), [HTML](https://arxiv.org/abs/2510.16786)
### Authors
Pengfei Gao,Chao Peng
### Background
基于LLM（大型语言模型）的编码代理在解决软件工程任务时变得越来越强大，但在实际部署中受到了显著且不可预测的成本限制。这些挑战源于多个方面：每次迭代的令牌数量呈平方级增长，模型价格高昂，完成实际任务所需的迭代次数多，以及代理倾向于采取低效或不必要的动作。现有研究主要集中在优化单个迭代，而对控制总迭代次数的战略控制尚未得到充分探索，用于管理代理性能和成本。本研究利用SWE-bench，对三种最先进的模型进行了一项全面的实证研究，评估了三种不同的迭代控制策略的影响。
### Innovation
本研究首次系统地分析了迭代控制策略，通过三种不同的迭代控制策略（包括无限制基线、固定迭代次数限制带提醒以及新颖的按需动态迭代策略），揭示了成本、性能和迭代效率之间的基本权衡关系。固定迭代次数策略，特别是在基线的第75百分位处，显著降低了成本，同时对解决率影响最小。最显著的是，动态迭代策略在提高资源分配效率的同时，进一步降低了12%-24%的成本，其结果整体优于固定的迭代次数策略。这项工作提出了简单且有效的指导方针，帮助开发人员平衡成本和效率。
### Conclusion
本工作提供了解决大规模成本问题的实用方法，通过智能地仅在必要时分配资源，动态资源分配成为性能优越且易于实施的部署强大但经济可行的编码代理的方法。
## 1037. `cs.LG` - 使用机器学习扩展无核心壳模型计算到无限模型空间 [PDF](https://arxiv.org/pdf/2511.05061), [HTML](https://arxiv.org/abs/2511.05061)
### Authors
Aleksandr Mazur,Roman Sharypov,Andrey Shirokov
### Background
该研究使用神经网络集合来扩展无核心壳模型（NCSM）结果到无限模型空间，特别是在轻核中。研究者回顾了使用Daejeon16 NN相互作用在不同模型空间和不同的NCSM基本参数$bar{rho}boldsymbol{u}$值下NCSM结果的神经网络外推，用于计算核态能量和质子、中子及物质分布的rms半径。
### Innovation
该方法提供收敛的预测并具有量化可识别的不确定性。通过对轻核${}^{6}text{Li}$、${}^{6}text{He}$和未结合的${}^{6}text{Be}$的基态能级及激发态能级的计算，该研究展示了如何利用神经网络从有限模型空间外推到无限模型空间，具体结果如下：${}^{6}text{Li}$、${}^{6}text{He}$的基态及${}^{6}text{Li}$的激发态能级预测误差在几百keV以内；基态半径预测具有良好的收敛性，而未结合态的半径则未表现出稳定趋势。
### Conclusion
该方法在预测轻核的物理量时表现出良好的性能，特别是在基态能量和某些态的rms半径方面，虽然非基态下的未结合态半径预测未达到稳定。
## 1038. `cs.LG` - NLP中的隐秘后门攻击：超低毒化和防御规避 [PDF](https://arxiv.org/pdf/2511.14301), [HTML](https://arxiv.org/abs/2511.14301)
### Authors
Eric Xue,Ruiyi Zhang,Zijun Zhang,Pengtao Xie
### Background
Transformer模型是自然语言处理（NLP）应用的基础，但它们仍然容易受到通过污染数据引入的后门攻击的影响，这些攻击会在训练过程中植入隐藏的行为。尽管最近的研究已经设计了更加隐蔽的攻击来测试现有防御机制，但这些攻击通常聚焦于通过风格化的特征或标记级别的扰动触发机制植入后门行为，这偏离了更具挑战性和现实性的场景：让模型响应语义触发，例如特定的名字或实体，这样成功的后门攻击可以操纵那些与已部署系统中真实人物或事件相关的输出结果。SteeganoBackdoor旨在解决这一问题。
### Innovation
SteeganoBackdoor利用自然语言隐写术的无害特性，采用一种以梯度为导向的数据优化过程将语义触发器种子转变为隐写载体，这些载体能够封装高载量的后门软件，并具有流畅性且与触发器无代表相似性。在各种实验条件下，与以前的方法相比，SteeganoBackdoor在极低的污染数据率下实现了超过99%的攻击成功率，并且能够有效规避全面的数据级防御。这项工作展示了这一实用且隐蔽的攻击，揭示了现有防御的盲点，强调了对抗性数据防御和现实威胁建模的需求。
### Conclusion
SteeganoBackdoor突显了当前防御中的一个紧迫的盲点，并要求立即关注对抗性数据防御和现实世界威胁建模。
## 1039. `cs.LG` - OmniLens++: 盲退化矫正中的大型透镜库预训练与潜在点扩展函数表示 [PDF](https://arxiv.org/pdf/2511.17126), [HTML](https://arxiv.org/abs/2511.17126)
### Authors
Qi Jiang,Xiaolong Qian,Yao Gao,Lei Sun,Kailun Yang,Zhonghua Yi,Wenyong Li,Ming-Hsuan Yang,Luc Van Gool,Kaiwei Wang
### Background
现有深学习方法用于镜头畸变矫正时，主要面临数据规模扩展困难和缺乏先验指导这两个挑战。这些因素限制了现有管道的泛化能力。为了克服这些问题，该研究提出了一种新的镜片库预训练（LensLib-PT）管道，并设计了全镜头增强版（OmniLens++）框架来解决上述限制。
### Innovation
此工作提出了OmniLens++框架，通过扩展设计规范增加了透镜来源的退化多样性，并通过建模光退化过程进行先验限制来改进数据可扩展性。同时，OmniLens++引入了Latent PSF Representation (LPR)，利用Point Spread Functions (PSFs) 作为无监督条件下矫正镜头畸变的指导，以提高泛化能力。实验结果表明，OmniLens++在多种现实镜头和仿真实验镜头的盲退化矫正中表现优异，同时AODLibpro可以作为有效训练的可扩展基础，而LPR则更好地挖掘了大规模镜头库的潜力。
### Conclusion
OmniLens++展示了先进的盲退化矫正能力，同时证明了可扩展的AODLibpro和LPR在不同退化矫正中的作用，为透镜畸变的矫正提供了新的途径。未来工作将开放其源代码和数据集。
## 1040. `cs.SE` - 构建浏览器代理：架构、安全与实际解决方案 [PDF](https://arxiv.org/pdf/2511.19477), [HTML](https://arxiv.org/abs/2511.19477)
### Authors
Aram Vardanyan
### Background
浏览器代理能够实现自主网络操作，但生产环境中面临严重的可靠性和安全性挑战。现有方法在安全自主操作方面存在不足。
### Innovation
该方法通过结合无障碍树快照和选择性视觉的混合上下文管理、与人类交互能力匹配的全面浏览器工具以及智能提示工程，实现了约85%的成功率，远高于之前的浏览器代理（约50%）和人类基准（95.7%）。研究成果表明，安全性边界应通过代码而非大模型推理来实现，并建议开发专门具有程序约束的工具。
### Conclusion
安全分析揭示了实时注入攻击使通用的自主操作从根本上变得不安全。因此，建议避免开发通用的浏览智能，转而开发有程序限制的专门工具，通过代码实施安全边界，而不是依赖大型语言模型的推理。
## 1041. `cs.LG` - NCCL 的 GPU-Initiated Networking [PDF](https://arxiv.org/pdf/2511.15076), [HTML](https://arxiv.org/abs/2511.15076)
### Authors
Khaled Hamidouche(1),John Bachan(1),Pak Markthub(1),Peter-Jan Gootzen(1),Elena Agostini(1),Sylvain Jeaugey(1),Aamir Shafi(1),Georgios Theodorakis(1),Manjunath Gorentla Venkata(1) ((1) NVIDIA Corporation)
### Background
现代AI工作负载，特别是Mixture-of-Experts (MoE)架构，对低延迟、细粒度的GPU到GPU通信提出了需求，且需要设备侧的控制。传统的GPU通信模式由CPU协调指挥，但这种模式在需要紧密集成计算和通信的应用中，因为其CPU协调开销的问题而不再适用。
### Innovation
NCCL 2.28引入了Device API，其中包括Load/Store Accessible (LSA)、Multimem和GPU-Initiated Networking（GIN）。特别是GIN，这是一种基于网络的直接GPU到GPU通信方式，不需要经过CPU协调。GI采用三层架构：NCCL核心的主机API、设备API和网络插件架构。这些技术共同解决了复杂的MoE通信问题，提供了低延迟操作并结合了NCCL的集体算法和生产基础设施。
### Conclusion
GIN架构有效地将低延迟的直接GPU到GPU通信整合到了NCCL的统一运行时环境中，通过其三层架构提高了MoE通信的效率和灵活性。这种基于网络的直接GPU通信方式减少了 CPU 协调开销，提供了高性能和低延迟的通信。
## 1042. `cs.SE` - stable-pretraining-v1：简化基础模型研究 [PDF](https://arxiv.org/pdf/2511.19484), [HTML](https://arxiv.org/abs/2511.19484)
### Authors
Randall Balestriero,Hugues Van Assel,Sami BuGhanem,Lucas Maes
### Background
基础模型和自监督学习（SSL）是现代AI的核心，但这一领域的研究仍受到复杂代码库、重复实现和试验扩展的工程负担的阻碍。
### Innovation
提出了一个模块化、可扩展且性能优化的库——stable-pretraining，基于PyTorch、Lightning、Hugging Face和TorchMetrics构建。不同于之前专注于复制最先进结果工具包，stable-pretraining旨在灵活性和迭代速度：它统一了重要的SSL实用工具，如探针、压缩检测指标、增强管道和可扩展的评估程序，并在一个一致且可靠的框架内。核心设计原则是记录一切，使调试、监控和可重复性无缝进行。
### Conclusion
通过降低门槛同时保持对大型试验的扩展性，stable-pretraining旨在加速发现并扩展基础模型研究的可能性。
## 1043. `cs.SE` - 无需先知的进化：LLM法官驱动的有效进化 [PDF](https://arxiv.org/pdf/2511.19489), [HTML](https://arxiv.org/abs/2511.19489)
### Authors
Zhe Zhao,Yuheng Yang,Haibin Wen,Xiaojie Qiu,Zaixi Zhang,Qingfu Zhang
### Background
大型语言模型（LLMs）与进化计算（EC）的结合为科学发现开辟了新的领域，但仍然受到基本制约：依赖先知——一个客观的机器可计算的适应性函数。本文探讨了在纯主观 Landscape 中，由LLM评判的进化是否可以繁荣。
### Innovation
引入了MADE（多代理分解进化）框架，通过“问题规范”来驯服主观评估的内在噪声。通过将模糊指令分解为具体的、可验证的子要求，MADE 能够将高变异性的 LLM 反馈转化为稳定的、精确的选择压力。MADE 在复杂基准测试（如 DevAI 和 InfoBench）中表现出色，超过了强基线50%以上，在软件需求满足方面达到从39.9%到61.9%的提升，并且在复杂的指令遵循任务中实现了95%的完美通过率。
### Conclusion
这项工作验证了从根本上改变优化范式：从优化“可计算的指标”转变为“描述性的品质”，从而解锁了在无真实基准存在的开放领域内的进化优化。
## 1044. `cs.SE` - Z-Space: 企业级大型语言模型自动化中的多智能体工具编排框架 [PDF](https://arxiv.org/pdf/2511.19483), [HTML](https://arxiv.org/abs/2511.19483)
### Authors
Qingsong He,Jing Nan,Jiayu Jiao,Liangjie Tang,Xiaodong Xu,Mengmeng Sun,Qingyao Wang,Minghui Yan
### Background
大型语言模型（LLM）能够通过在模型上下文协议框架内调用外部工具来突破知识和时效限制，实现复杂任务的自动化执行。然而，随着企业级模型上下文协议（MCP）服务的快速发展，高效准确地在成千上万种异质工具中匹配目标功能成为限制系统实用性的核心挑战。现有方法通常依赖全提示注入或静态语义检索，面临用户查询与工具描述之间的语义脱节、LLM输入上下文膨胀以及高推理延时等问题。
### Innovation
本文提出了Z-Space框架，这是一种基于数据生成的多智能体协作工具调用框架。Z-Space框架建立了一个多智能体协作架构和工具筛选算法：（1）通过意图解析模型实现用户查询的结构化语义理解；（2）基于融合子空间加权算法的工具筛选模块（FSWW）实现细粒度的意图与工具之间的语义对齐，无需参数调整；（3）构建推理执行代理，支持多步骤任务的动态规划和容错执行。
### Conclusion
Z-Space框架已在饿了么技术部门部署，服务多个业务单元（包括淘宝、高德和盒马）的大规模测试数据生成场景。生产数据表明，该系统在工具推理中平均减少了96.26%的令牌消耗，同时实现了92%的工具调用准确率，显著提高了智能测试数据生成系统的效率和可靠性。
## 1045. `cs.SE` - CodeR$^3$: 一个基于生成式AI的工作流修复和复活生态系统 [PDF](https://arxiv.org/pdf/2511.19510), [HTML](https://arxiv.org/abs/2511.19510)
### Authors
Asif Zaman,Kallol Naha,Khalid Belhajjame,Hasan M. Jamil
### Background
科学工作流中包含丰富的专业知识和计算方法，但是研究发现，相当一部分已发布的工作流会随着时间逐渐退化。对于像Taverna这样的遗留工作流系统来说，停用的服务、过时的依赖和系统退休会使得原本可用的工作流变得不可用。
### Innovation
本文提出了一种名为CodeR$^3$（表示为代码修复、复苏和重用）的新型遗留工作流迁移系统，利用生成式AI分析退化的工作流特点，将其转换到现代工作流技术如Snakemake和VisFlow。该系统包括逐步工作流分析可视化、自动化服务替换和人工在环验证。通过几个Taverna工作流复苏案例，展示了该方法的可行性并对需要人工监督的关键挑战进行了识别。
### Conclusion
研究结果表明自动化可以显著减少工作流解析和识别服务所需的手动努力。但是关键任务如服务替换和数据验证仍需专业知识。最终结果是一个众包平台，社区可以协作恢复退化的工作流并验证复活工作流的功能性和正确性。本工作贡献了一个平衡自动化效率和必要人工判断的工作流复苏框架。
## 1046. `cs.SE` - Java 中的自动化单元测试生成与评估：AgoneTest 框架 [PDF](https://arxiv.org/pdf/2511.20403), [HTML](https://arxiv.org/abs/2511.20403)
### Authors
Andrea Lops,Fedelucio Narducci,Azzurra Ragone,Michelantonio Trizio,Claudio Barto
### Background
单元测试是软件开发中一个重要但资源密集的步骤，用于确保代码单元的功能正确性。本文介绍了一个名为 AgoneTest 的自动化评估框架，用于评估大型语言模型（LLM）生成的 Java 单元测试。AgoneTest 旨在支持研究人员和开发人员在现实条件下比较不同 LLM 和提示策略的效果。
### Innovation
该框架引入了一个名为 Classes2Test 的数据集，将需要测试的 Java 类映射到相应的测试类，并集成高级评估指标，如突变分数和测试异味，实现全面评估。实验结果显示，对于能够编译的测试，由 LLM 生成的测试在覆盖率和缺陷检测方面可以与人工编写的测试相媲美或更优。此外，增强的提示策略也提高了测试质量。
### Conclusion
AgoneTest 确定了 LLM 在软件测试中的潜力，并为未来模型设计、提示工程和测试实践的改进提供了见解。
## 1047. `cs.SE` - CodeFuse-CommitEval：致力于评估大语言模型在检测提交信息与代码变更不一致性方面的能力 [PDF](https://arxiv.org/pdf/2511.19875), [HTML](https://arxiv.org/abs/2511.19875)
### Authors
Qingyu Zhang,Puzhuo Liu,Peng Di,Chenxiong Qian
### Background
版本控制系统依赖于提交信息来传达代码变更的理由，但这些信息通常质量低且经常与变更内容不一致，这被称为消息-代码不一致性（MCI）。MCI会误导审阅者、妨碍维护、污染研究数据集，甚至可能隐藏安全补丁。目前没有针对MCI检测模型的专门基准进行评估。
### Innovation
本文提出了CODEFUSE-COMMITEVAL，这是首个用于MCI检测的大语言模型基准。该基准基于ApacheCM数据集，通过规则指导的通变更InitStruct来生成七种类型的不一致信息，通过两轮验证来验证正负样本。在标记的message-diff数据集上，评估了六种最先进的开源大语言模型，并采用三种增强策略（少量例子提示、带因果链、扩展上下文）进行评估。
### Conclusion
模型在检测不一致提交方面的表现优于一致提交（平均召回率85.95%，精确率80.28%，特异性63.8%）。增强策略的效果各异。此类基准为测量、比较和推进MCI检测提供坚实的基础，指出需要更丰富的上下文和平衡的数据以捕捉高层次的语义差距。
## 1048. `cs.SE` - 通过性能剖析理解加速器编译器 [PDF](https://arxiv.org/pdf/2511.19764), [HTML](https://arxiv.org/abs/2511.19764)
### Authors
Ayaka Yorihiro,Griffin Berlstein,Pedro Pontes García,Kevin Laeufer,Adrian Sampson
### Background
加速器设计语言（ADLs）有助于领域专家快速设计高效的专用硬件。ADL编译器优化数据路径并将软件风格的控制流程转换为控制路径，但这些编译器通常非常复杂且不可预测，需要先进的启发式方法，导致生成硬件的性能难以控制。我们假设ADL编译器永远无法完美，性能的不确定性是解决该问题固有的。
### Innovation
提出了Petal，一种针对Calyx中间语言的时钟级别剖析工具。Petal通过引入探针并分析寄存器传输级模拟的追踪数据，将追踪中的事件映射回Calyx代码中的高级控制结构，跟踪每个结构在每个周期何时活跃。通过案例分析，Petal的时钟级别剖析有助于定位现有加速器设计中的性能问题，并提供优化建议，如某应用程序总周期数减少46.9%。
### Conclusion
Petal工具为ADL程序员提供了洞察，帮助理解编译器决策如何影响性能，从而指导开发人员进行自动优化无法完成的进一步优化。
## 1049. `cs.LG` - 差分隐私下的相关数据 [PDF](https://arxiv.org/pdf/2511.18583), [HTML](https://arxiv.org/abs/2511.18583)
### Authors
Valentin Roth,Marco Avella-Medina
### Background
在社会和健康科学等领域的统计研究中，数据常常包含敏感或私密信息。传统的差分隐私（DP）方法，特别是用户级的DP，为处理每个个体提供多个观测值的数据集提供了一种自然的隐私保护形式化。然而，由重复测量等因素引入的相关性挑战了现有在DP约束下的统计理论。在独立同分布（iid）的条件下，已知带噪声的Winsorized均值估计器在标准（item-level）和用户级DP的均值估计中是渐近最优的。但是，这些估计器在相关数据上的表现已没有被研究。本文填补了这一空白，展示了在相关数据下的Winsorized均值估计器在有界和无界数据下也可以被使用，并且可以导致渐近和有限样本保证，类似于在独立同分布条件下的对应保证。
### Innovation
本文通过引入适应相关数据的稳定直方图（Karwa和Vadhan, 2018），对带噪声的Winsorized均值估计器进行了推广，并利用这种保证将item-level的均值估计拓展到了用户级均值估计，进而通过局部模型的随机响应直方图实现转移。这项工作是对于依赖数据下DP研究的第一步，涵盖了随机效应模型、纵向线性回归和非参数回归等扩展。
### Conclusion
本文提出的方法为相关数据下的差分隐私研究提供了基础，使得相关数据下的DP成为可能，并为这些复杂数据集的建模提供支持。通过将均值估计作为构建块，本文为差分隐私下依赖数据的研究指明了方向，为进一步研究相关数据下的统计理论奠定了基础。
## 1050. `cs.SE` - 大型C库翻译为 idiomatic Rust [PDF](https://arxiv.org/pdf/2511.20617), [HTML](https://arxiv.org/abs/2511.20617)
### Authors
Saman Dehghan(1),Tianran Sun(2),Tianxiang Wu(1),Zihan Li(1),Reyhaneh Jabbarvand(1) ((1) University of Illinois at Urbana-Champaign, USA, (2) Shanghai Jiao Tong University, China)
### Background
现有的C到Rust的翻译技术无法平衡质量和可扩展性：基于转译的方法可以扩展到大型项目，但会产生安全性和可读性较差的代码。相比之下，基于大模型的语言模型方法过于昂贵，无法可靠地生成可编译的翻译，因此限制了可扩展性。
### Innovation
本文提出了Rustine，一个完全自动化的流水线，用于有效且高效地将仓库级别的C代码转换为符合规范的安全Rust代码。通过23个不同规模的C程序的评估，Rustine能够生成完全可编译的Rust代码，实现87%的功能等价，并且翻译后的代码在安全性、符合规范性和可读性方面优于此前六种方法。
### Conclusion
Rustine可以生成高质量且可编译的Rust代码，即便在不能通过所有测试达到功能等价时，也可以通过人类开发者进行调试至合格，其安全性和规范性优于以往方法。
## 1051. `cs.SE` - SAFE：利用LLM从多模态事故数据中进行场景驱动的ADS测试 [PDF](https://arxiv.org/pdf/2502.02025), [HTML](https://arxiv.org/abs/2502.02025)
### Authors
Siwei Luo,Yang Zhang,Yao Deng,Linfeng Liang,Xi Zheng
### Background
确保自动驾驶系统（ADS）的安全性需要现实且可复制的测试场景，但从多模态事故报告中提取这些场景仍然是一个重大挑战。大型语言模型（LLMs）常常产生幻觉且会丢失地图结构，导致不现实的道路布局和车辆行为。因此，本文分析了从多模态事故数据中提取场景的难点。
### Innovation
本文提出了一种名为SAFE的新颖场景驱动的ADS测试框架，通过多模态提取利用检索增强生成（RAG）、知识导向提示、链式思考（CoT）推理和自我验证，提高了从多模态事故数据中构建场景的准确性。SAFE在道路网络细节提取方面达到了93.8%的准确率，对于行动者信息为80.0%，环境上下文为100%。在人类研究中，SAFE在重建连贯道路网络和车辆行为方面优于LCTGen和AC3R。与LCTGen和AC3R相比，SAFE在相同的ADS和模拟器设置下检测到更多的安全违规行为，并再现了更多的真实世界的碰撞案例。
### Conclusion
SAFE在19个由AC3R支持的案例中，在MetaDrive和BeamNG中分别生成了额外的碰撞案例和场景，且在MetaDrive中生成的场景所需时间不到25秒，在1个或3个案例后触发违规行为。
## 1052. `cs.SE` - Agint: 用于软件工程代理的智能图编译 [PDF](https://arxiv.org/pdf/2511.19635), [HTML](https://arxiv.org/abs/2511.19635)
### Authors
Abhi Chivukula,Jay Somasundaram,Vijay Somasundaram
### Background
LLM（大型语言模型）驱动的编码代理越来越普及，但在上下文管理、延迟、可靠性、重现性和扩展性方面仍面临挑战。Agint 提出了一种基于代理的图编译器、解释器和运行时，它增量地和分层地将自然语言指令转换为受类型约束且察觉效果的代码有向图（DAG）。
### Innovation
Agint 引入了基于语义图变换的显式类型底层（从文本到数据到规范再到代码），并结合了混合 LLM 和函数基的 JIT 运行时，从而使图动态细化、可重现和优化执行、推测性评估以及与现有开发工具的互操作性成为可能。Agint 的类型图绑定提高了可靠性，并允许通过自动并行生成构建设备并发复用的代码库，从而支持使用较小和更快的模型进行加速开发、更低的延迟、更高效的上下文使用和更高的吞吐量。
### Conclusion
Agint 为实时、低延迟代码和数据流创建提供了一个可组合的类 Unix 工具链（dagify、dagent、schemagin 和 datagin）。通过 Agint CLI，人类开发者和编码代理可以改进图，而非技术人员可以使用 Agint Flow GUI 进行视觉编辑、对话式细化和调试，从而将原型到生产代码的代理工作流程连续扩展。这种持续的共同创新模型允许团队快速原型设计、无缝细化和可靠部署，将自然语言、编译器方法和开发工具集成为一个新代的可扩展、团队为中心的编码代理。
## 1053. `cs.SE` - SmartC2Rust: 通过大型语言模型实现既有代码到Rust的安全迭代反馈驱动翻译以确保等效性 [PDF](https://arxiv.org/pdf/2409.10506), [HTML](https://arxiv.org/abs/2409.10506)
### Authors
Momoko Shiraishi,Yinzhi Cao,Takahiro Shinagawa
### Background
内存安全漏洞在现代软件系统中仍然普遍存在，解决这些问题的一种有前景的方法是采用内存安全语言如Rust。由于存在大量的用C语言编写的遗留代码，因此将这些遗留C代码翻译成Rust有强烈的需求。目前已有研究显示了使用大型语言模型（LLMs）进行这种翻译的潜力，但LLM在实现编译、减少不安全语句和保持语义功能方面仍然面临显著挑战，这是因为LLMs的固有限制，如词数量的限制和输出的一致性问题。
### Innovation
本文设计了一个自动化C到Rust翻译系统，名为SmartC2Rust，旨在通过逐步迭代优化Rust代码的生成来达到语义等效和提高安全性。该系统通过提供额外的反馈，如编译错误、分段上下文、语义差异和不安全语句，逐步改进生成的Rust代码质量，从而缓解不安全、不一致和语义问题。
### Conclusion
我们的评估表明，SmartC2Rust 在减少不安全语句、安全性和语义等效方面显著优于之前的成果。
## 1054. `cs.SE` - LLM协作中的多智能体强化学习 [PDF](https://arxiv.org/pdf/2508.04652), [HTML](https://arxiv.org/abs/2508.04652)
### Authors
Shuo Liu,Tianle Chen,Zeyu Liang,Xueguang Lyu,Christopher Amato
### Background
多智能体系统（MAS）已有大量研究工作，用于建模和解决多个交互代理的问题。现有的大型语言模型（LLM）大多独立预训练，并未特别优化以进行协作。现有LLM微调框架依赖于个体奖励设计，这需要为每个代理复杂的设计奖励机制以鼓励合作。然而，这种方法存在复杂的奖赏设计和难以实现代理间有效合作的问题。
### Innovation
本文将LLM协作建模为合作的多智能体强化学习（MARL）问题，并开发了一种基于当前的智能体信念状态建模的新算法——多智能体组相对策略优化（MAGRPO）。该方法结合了现有的强化学习技术和MARL技术，能够在LLM写作和编码协作中获得高质量的响应，通过有效的合作提高响应效率。
### Conclusion
本文的研究方法揭示了其他MARL方法在LLM应用中的潜力，并凸显了使用MARL方法存在的相关挑战。未来研究可以通过探索其他MARL策略来进一步完善和改进LLM的协作性能。相关代码可以在指定的网址找到。
## 1055. `cs.SE` - 由摘要驱动的抽象解释数据竞争检测（扩展版本） [PDF](https://arxiv.org/pdf/2511.11055), [HTML](https://arxiv.org/abs/2511.11055)
### Authors
Michael Schwarz,Julian Erhard
### Background
声静分析可以通过证明不存在竞争条件，来证实数据竞争的不存在性。竞争条件的出现通常依赖于两个不兼容的内存访问在同一时间发生。已有研究引入了摘要（Digests）的概念，最初用于通过抽象解释增强线程模块化值分析的可调细粒度并发敏感性，这一概念现已拓展至竞争检测领域。
### Innovation
本文创新性地将摘要的概念应用于竞争检测领域，通过定义线程模块化局部跟踪语义下的数据竞争，并利用摘要来捕捉潜在冲突的排除条件。此外，还将锁集摘要（Lockset Digest）与线程ID和线程连接的摘要推理结合起来，与单独使用锁集推理相比，检测正确解的任务数量提高了超过五倍。
### Conclusion
本文在静态分析器Goblint中实现了基于摘要的数据竞争检测，并利用SV-COMP基准集进行了评估。结果显示，结合锁集摘要与摘要推理，可以显著提高正确解的任务数量。
## 1056. `cs.SE` - EnergyTwin：一种用于模拟和协调能源微电网的多智能体系统 [PDF](https://arxiv.org/pdf/2511.20590), [HTML](https://arxiv.org/abs/2511.20590)
### Authors
Jakub Muszyński,Ignacy Walużenicz,Patryk Zan,Zofia Wrona,Maria Ganzha,Marcin Paprzycki,Costin Bădică
### Background
微电网部署旨在减少购电成本、降低对波动性电价的暴露以及在中断期间确保服务连续性。这需要跨多个时间尺度协调异构分布式能源资源，并在变化的条件下进行协调。现有工具通常存在物理行为模拟但假设集中控制，或分布式决策建模但缺乏物理基础的问题。
### Innovation
提出了一个基于代理的微电网仿真环境——EnergyTwin，结合了物理本体模型、基于预报的信息滚动规划和谈判功能。每个资产都被建模为代理，与中心代理交互以获取预测、制定计划并根据合同进行能源分配。
### Conclusion
在大学校园微电网场景中评估了EnergyTwin的可行性，多种规划策略进行了比较。结果显示，基于预报的滚动规划能提高本地能源自给率、保持较高的电池储备并减少低韧性运行状态的暴露。此外，进一步展示了EnergyTwin作为支持弹性、谈判驱动微电网研究平台的潜力。
## 1057. `cs.SE` - 少而精：高效的编程代理的轮次控制策略实证研究 [PDF](https://arxiv.org/pdf/2510.16786), [HTML](https://arxiv.org/abs/2510.16786)
### Authors
Pengfei Gao,Chao Peng
### Background
LLM（大型语言模型）驱动的编程代理在迭代循环中解决软件工程任务的能力越来越强，但其实际部署受到显著且不可预测的成本限制。这些挑战源于每次迭代中标记数量的二次增长、模型价格高昂、完成实际任务所需的迭代次数众多以及代理倾向于进行无效或不必要的操作等多重因素。现有研究主要集中在优化单个迭代，但对总迭代次数的策略控制是一个尚未充分探索的领域，对管理代理性能和成本至关重要。
### Innovation
本文通过使用SWE-bench进行了全面的实证研究，评估了三种先进的模型下的三种不同的轮次控制策略：无限制基线、固定的轮次限制和带提醒的固定轮次限制，以及一种新型的按需动态轮次策略，主动将资源仅分配给需要的任务。研究发现固定轮次限制特别是基线的75百分位数，能显著降低成本（减少24%-68%），同时对解决问题率影响不大。最显著的是，动态轮次策略持续优于固定限制方法，通过智能化的资源分配，不仅获得与之媲美或更好的解决问题率，而且还进一步降低了12%-24%的成本。
### Conclusion
本工作首次系统分析了轮次控制策略，提供了简单而有效的指导方针，使开发者能够在成本和功效之间做出平衡。研究证明，动态资源分配是一种更优越、易于实现的方法，以部署强大的且经济实惠的编程代理。
## 1058. `cs.SE` - CodeAssistBench (CAB): 数据集与评估框架用于多轮代码辅助 [PDF](https://arxiv.org/pdf/2507.10646), [HTML](https://arxiv.org/abs/2507.10646)
### Authors
Myeongsoo Kim,Shweta Garg,Baishakhi Ray,Varun Kumar,Anoop Deoras
### Background
编程助手在大规模语言模型的支持下取得了显著进步，但现有的基准测试仍局限于狭窄的代码生成环境。尽管有InfiBench和StackEval等新努力，它们依然依赖于Stack Overflow的问题，并且仅限于单轮交互和手动筛选的数据集。这些方法无法捕捉到整个项目的环境，也局限于孤立的代码片段。本文提出了CodeAssistBench（CAB），一个用于大规模评估多轮、项目基础编程助手的第一个基准。CAB从GitHub的标记问题中自动生成数据集，使用一个基于大模型的流水线来过滤噪声、提取可运行的上下文、构建可执行容器并验证环境的正确性。这使得它能够在无需人工干预的情况下，持续自动扩展到各种不同的代码库。
### Innovation
CAB引入了一个自动构建数据集的流水线，能够从GitHub的标记问题中提取出可实现的上下文，构建可执行的容器，并验证环境的正确性。它能够在无需人工干预的情况下，自动扩展到不同的代码库。CAB首次实现了针对多轮交互和项目基础编程助手的大规模评估，揭示了当前大模型在现实、项目特定情境下的挑战。同时，CAB提供了一个可扩展且可复现的研究框架，用于推进多轮、项目基础编程代理的研究。这种方法使得研究人员能够评估最新的模型在实际项目中的表现，而不仅仅是传统的问答基准。
### Conclusion
使用CAB，我们创建了一个包含3,286个真实问题的数据集，覆盖214个仓库，涉及七种语言。评估最先进的模型显示，虽然模型在Stack Overflow风格的问题上能达到70-83%的准确率，但在CAB的问题中只有16.49%能够解决。在手动验证的一小部分149个问题中，顶级模型也仅能达到12.08%的正确率。这些结果强调了一个基本挑战：当前的语言模型在提供真实的项目相关帮助时表现不佳，尽管在传统的问答基准测试中表现出色。CAB提供了一个可扩展且可重复的数据集和评估框架，以推动多轮、代码库基础编程代理的研究。详细的信息和数据集可以在这个链接中找到：this https URL
## 1059. `cs.LG` - 谱阈值在高维学习中的判别性和稳定性:样本数有限的相变 [PDF](https://arxiv.org/pdf/2510.03809), [HTML](https://arxiv.org/abs/2510.03809)
### Authors
William Hao-Cheng Huang
### Background
在高维学习中，模型稳定到一定程度后，一旦样本数量低于某个临界值，模型就会突然变得不稳定。这种不稳定性不仅仅是针对特定算法的，而是由几何机制决定的：最弱的费舍尔特征方向跌至样本级波动之下时，识别性便会失效。
### Innovation
费舍尔阈值定理通过证明最小费舍尔特征值需要超过一个显式的$O(frac{root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j req j root req j root req j req j root req j root req j root req j req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j req j root req j root req j req j root req j root req j root req j req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j req j root req j root req j req j root req j root req j root req j req j root req j root req j root req j root req j root req j root req j root req j root req j root req j req j root req j root req j root req j root req j root req j req j root req j root req j req j root req j root req j root req j root req j root req j root req j root req j root req j req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j} frac{root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j root req j} frac{d}{n}$Bound。这个阈值不同于之前的渐近或特定模型的标准，它是有限样本的必要条件，标志着可靠的收敛与不可避免失败之间的尖锐相变。为了实用化这一原理，引入了费舍尔地板，这是一种鲁棒的光谱正则化方法，不受平滑或预条件影响，并用合成实验在高斯混合模型和逻辑回归模型中验证了预测的相变，与$d/n$比率相一致。
### Conclusion
费舍尔阈值定理将经典特征值条件锐化为非渐近律。从机器学习理论的角度来看，它定义了光谱样本复杂度前沿，将理论与鲁棒高维推断的诊断学联系起来。通过费舍尔地板，可以验证光谱正则化，使其在平滑和预条件中保持鲁棒性。
