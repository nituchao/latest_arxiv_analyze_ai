# 20260129
[![Subscribe_Visitors](https://visitor-badge.laobi.icu/badge?page_id=nituchao.latest_arxiv_analyze_ai_rss)](https://github.com/nituchao/latest_arxiv_analyze_ai)

## 1. `cs.AI` - 通过强化学习探索函数调用模型的弱点：一种对抗性数据增强方法 [PDF](https://arxiv.org/pdf/2601.19122), [HTML](https://arxiv.org/abs/2601.19122)
### Authors
Weiran Guo,Bing Bo,Shaoxiang Wu,Jingsheng Yang
### Background
现有方法通过手动注释或模式化的数据生成来增强大型语言模型（LLMs）的函数调用能力，但这些方法往往缺乏针对性设计，受限于固定的数据模式和分布，从而限制了它们在增强函数调用LLMs的一般性和鲁棒性方面的效果。
### Innovation
提出了一种新颖的对抗性数据增强方法，使用强化学习系统性地识别和针对函数调用LLMs的弱点。采用零和博弈的形式，训练查询模型和函数调用模型进行交替训练，生成特定设计的对抗查询，以挑战函数调用模型。
### Conclusion
该方法推动了更稳健的函数调用模型的发展，并提供了系统地识别和纠正LLMs与外部工具交互能力缺陷的方法。
## 2. `cs.AI` - Uncertainty-Aware 3D Emotional Talking Face Synthesis with Emotion Prior Distillation [PDF](https://arxiv.org/pdf/2601.19112), [HTML](https://arxiv.org/abs/2601.19112)
### Authors
Nanhan Shen,Zhilei Liu
### Background
情感说话语音合成在多媒体和信号处理中至关重要，但现有的3D方法面临两个关键挑战：情绪音频与视觉对齐不良，体现在难以提取音频情感和控制情感微表情不足；以及一种一刀切的多视角融合策略，忽略了不确定性及特征质量差异，导致渲染质量下降。
### Innovation
提出了UA-3DTalk，一种包含情感先验蒸馏的不确定性感知3D情感说话语音合成方法。该方法包括三个核心模块：Prior Extraction模块将音频拆分为内容同步特征，用于对齐和个性特征，实现个性化；Emotion Distillation模块引入了多模态注意力加权融合机制和4D高斯编码，结合多分辨率代码簿，实现细粒度音频情感提取和精确控制情感微表情；Uncertainty-based Deformation模块使用不确定性模块估算特定视角的偶然不确定性（输入噪声）和先验不确定性（模型参数），实现自适应多视角融合，并引入多头解码器进行高斯原始优化，以减轻均匀加权融合的限制。
### Conclusion
在常规和情感数据集上的广泛实验表明，UA-3DTalk相较于DEGSTalk和EDTalk方法，在情绪对齐方面提高了5.2%的E-FID，在唇同步方面提高了3.1%的SyncC，在渲染质量方面提高了0.015的LPIPS。
## 3. `cs.AI` - 更多关健：报酬和语言如何影响 LLM 预判代理在合作困境中的策略 [PDF](https://arxiv.org/pdf/2601.19082), [HTML](https://arxiv.org/abs/2601.19082)
### Authors
Trung-Kiet Huynh,Dao-Sy Duy-Minh,Thanh-Bang Cao,Phong-Hao Le,Hong-Dan Nguyen,Nguyen Lam Phu Quy,Minh-Luan Nguyen-Vo,Hong-Phat Pham,Pham Phu Hoa,Thien-Kim Than,Chi-Nguyen Tran,Huy Tran,Gia-Thoai Tran-Le,Alessio Buscemi,Le Hong Trang, TheAnh Han
### Background
随着大模型（LLMs）在互动和多代理设置中越来越自主地行动，理解它们的战略行为对于确保安全、协调以及基于人工智能的社会和经济系统至关重要。本文探讨报酬规模和语言背景如何塑造大模型在反复的社会困境中的策略，特别是在报酬放大后的囚徒困境中，以隔离对激励强度的敏感性。我们在不同模型和语言中观察到一致的行为模式，包括激励敏感的条件策略和跨语言分离。为了解释这些动态，我们训练监督分类器以识别经典反复博弈策略，并应用于大模型决策，揭示出系统性的、模型依赖和语言依赖的行为意图，语言框架有时与架构效应相当或更甚。
### Innovation
本文通过构建报酬放大的囚徒困境实验，孤立研究了报酬和语言对大模型策略的影响，揭示了激励敏感的条件策略和跨语言分离现象。进一步通过对大模型决策进行监督分类，发现模型和语言对行为意图的系统性影响，表明语言框架有时能与架构效应匹敌，这是对大模型作为预判代理进行审计的一个统一框架，为AI治理和多代理系统设计提供了直接的合作偏见启示。
### Conclusion
本研究提供了一个统一的框架，用于审查作为战略代理的大型语言模型并发出了与合作偏见直接相关的治理和多代理系统设计的含义。
## 4. `cs.AI` - RIFT: 重新排序的指令遵循测试套件，用于评估单一多步提示结构中的指令遵循能力 [PDF](https://arxiv.org/pdf/2601.18924), [HTML](https://arxiv.org/abs/2601.18924)
### Authors
Andrew Jaffe,Noah Reicin,Jinho D. Choi
### Background
大型语言模型（LLMs）在复杂的工作流中越来越受欢迎，但它们维持指令连续性的能力却未得到充分研究。现有的基准测试将任务复杂性与结构顺序混为一谈，使得难以单独评估提示拓扑对性能的影响。研究团队引入了RIFT（Reordered Instruction Following Testbed）来评估指令遵循，通过解耦结构和内容来研究这一问题。
### Innovation
RIFT使用重新表述的Jeopardy!问题-答案对，测试LLMs在两种提示结构下的表现：线性提示，按顺序进行；跳跃提示，内容相同但需要非顺序遍历。该研究覆盖了六种最先进的开源LLMs，在10,000次评估中发现，在跳跃条件下，准确率最多下降72%，表明对位置连续性的强烈依赖。错误分析表明，约50%的错误源于指令顺序违反和语义漂移，这表明当前架构将指令遵循视为顺序模式而不是推理技能。
### Conclusion
这些结果揭示了结构敏感性作为当前架构的基本局限性，并直接适用于需要非顺序控制流的应用，如工作流自动化和多智能体系统。
## 5. `cs.AI` - Agentic Business Process Management Systems [PDF](https://arxiv.org/pdf/2601.18833), [HTML](https://arxiv.org/abs/2601.18833)
### Authors
Marlon Dumas,Fredrik Milani,David Chapela-Campa
### Background
自20世纪90年代初以来，业务流程管理（BPM）领域的演变受到了相继的技术自动化浪潮的影响。这些技术有的能够自动化单个任务，有的则专注于端到端流程的执行编排。生成性和自主性人工智能（AI）的发展为另一波自动化浪潮铺平了道路。然而，这一波浪潮将会有所不同，因为它将焦点从自动化转移到自主性，并从以设计为导向的业务流程管理转向以数据为基础的管理，借助过程挖掘技术。
### Innovation
本文基于2025年AI for BPM研讨会的主旨演讲，提出了一个基于过程挖掘的新框架，该框架能够使代理感知流程状态，思考改进机会，并行动以维持和优化性能。文章还提出了自主性业务流程管理系统（A-BPMS）的架构愿景：这是一种新类平台，将自主性、推理能力和学习整合到流程管理和执行中。
### Conclusion
这样的系统必须支持从半自主到完全自主的连续流程，从而重新定义过程自动化和治理的边界。
## 6. `cs.AI` - LLM 驱动的具有可控高级属性的连续优化问题设计 [PDF](https://arxiv.org/pdf/2601.18846), [HTML](https://arxiv.org/abs/2601.18846)
### Authors
Urban Skvorc,Niki van Stein,Moritz Seiler,Britta Grimme,Thomas Bäck,Heike Trautmann
### Background
现有的黑盒优化基准套件，如BBOB，在结构多样性方面有限，因此在连续黑盒优化基准测试方面受到限制。本文探讨了在进化循环中嵌入大型语言模型（LLM），是否可以用来设计具有明确高阶景观特性的优化问题。
### Innovation
本文引入了LLMEA框架，通过引导LLM从自然语言描述的目标属性（多峰性、可分性、盆地大小均一性、搜索空间均一性以及全局与局部最优解对比）生成问题代码，并使用基于进化学习算法（ELA）的属性预测器评估候选者。此外，引入了一种基于ELA空间的亲和力共享机制，增加了群体多样性并引导生成器远离冗余景观。通过t-SNE嵌入分析，验证了这些生成函数具有预期的结构特征，同时扩展了BBOB实例空间。
### Conclusion
本文产生的库提供了广泛可解释、可重复的基准问题集，用于景观分析和后续任务如自动化算法选择。
## 7. `cs.AI` - TS-Debate: 多模态协作辩论框架用于零样本时间序列推理 [PDF](https://arxiv.org/pdf/2601.19151), [HTML](https://arxiv.org/abs/2601.19151)
### Authors
Patara Trirat,Jin Myung Kwak,Jay Heo,Heejun Lee,Sung Ju Hwang
### Background
最近在大语言模型（LLMs）和时间序列（TS）分析交汇处的研究揭示了其潜在好处和脆弱性。虽然大语言模型在结构合理的上下文中能够处理时间结构，但它们在数值精确度、模态干扰和跨模态整合方面经常出现困难。
### Innovation
TS-Debate 提出了一种专门针对模态的、协作的多代理辩论框架，适用于零样本时间序列推理。它通过决断-冲突-校准机制评估代理声明，并利用轻量级代码执行和数值查找进行程序验证，从而保持模态的精确性，暴露冲突证据，减少数值幻觉，同时无需特定任务微调。
### Conclusion
在涵盖三个公开基准的20个任务中，TS-Debate 在所有任务上都实现了对强大基线的持续显著性能改进，包括所有代理观察所有输入的标准多模态辩论。
## 8. `cs.AI` - 通过区间型2神经模糊系统实现可解释的能源预测不确定性量化 [PDF](https://arxiv.org/pdf/2601.18897), [HTML](https://arxiv.org/abs/2601.18897)
### Authors
Qusai Khaled,Bahjat Mallak,Uzay Kaymak,Laura Genga
### Background
污水处理厂消耗全球1-3%的电力，因此精确的能耗预测对于运营优化和可持续发展至关重要。尽管机器学习模型提供了点预测，但对于关键基础设施中的安全相关决策来说，缺乏可解释的不确定量化能力仍然是一个挑战。
### Innovation
研究开发了区间型2自适应神经模糊推理系统（IT2-ANFIS），通过模糊规则结构生成可解释的预测区间。该框架将不确定性分解为三个层次：特征层次、不确定性足迹识别变量引入的模糊性、规则层次分析局部模型的信心以及实例层次区间量化整体预测不确定性。
### Conclusion
该方法在墨尔本水公司东方水处理厂的数据集上得到了验证，IT2-ANFIS 在预测性能与一阶ANFIS相当的同时，训练运行间变异显著降低，并提供可解释的不确定性估计，这些估计直接关联于运营条件和输入变量的预测置信度。
## 9. `cs.AI` - Length-Adaptive Interest Network for Balancing Long and Short Sequence Modeling in CTR Prediction [PDF](https://arxiv.org/pdf/2601.19142), [HTML](https://arxiv.org/abs/2601.19142)
### Authors
Zhicheng Zhang,Zhaocheng Du,Jieming Zhu,Jiwei Tang,Fengyuan Lu,Wang Jiaheng,Song-Li Wu,Qianhui Zhu,Jingyu Li,Hai-Tao Zheng,Zhenhua Dong
### Background
现代推荐系统中的用户行为序列表现出显著的长度异质性，从稀疏的短期交互到丰富的长期历史。虽然较长的序列可以提供更多的上下文，但在现有CTR模型中增加最大输入序列长度反而会由于注意力极化和training data长度不平衡，导致短序列用户的表现下降。
### Innovation
提出了LAIN（Length-Adaptive Interest Network）框架，该框架将序列长度作为条件信号显式地纳入模型中，以平衡长序列和短序列的建模。LAIN包含三种轻量级组件： Spectral Length Encoder 用于将长度映射到连续表示；Length-Conditioned Prompting 用于在长短期行为分支中注入全局上下文线索；Length-Modulated Attention 用于基于序列长度自适应调整注意力锐度。
### Conclusion
在五个强大的CTR底层架构上的三个真实世界基准上进行的广泛实验表明，LAIN具有较高的整体性能，AUC提升高达1.15%，log loss降低高达2.25%。特别地，我们的方法显著提高了短序列用户的准确性，而不会损害长序列用户的效果。我们的研究提供了一种通用、高效且可部署的解决方案，以减轻序列推荐中的长度偏差。
## 10. `cs.AI` - 神经定理证明用于验证条件：一种实际世界基准 [PDF](https://arxiv.org/pdf/2601.18944), [HTML](https://arxiv.org/abs/2601.18944)
### Authors
Qiyuan Xu,Xiaokun Luan,Renxi Wang,Joshua Ong Jun Leang,Peixin Wang,Haonan Li,Wenda Li,Conrad Watt
### Background
程序验证的基础是定理证明，其中通过自动定理证明验证条件（VC）仍然是主要瓶颈。现有自动定理证明器（ATP）难以证明真实程序验证中的复杂VC，导致了巨大的手动证明工作量，影响了实际应用。虽然神经定理证明（NTP）在数学比赛中取得了显著成功，展示了机器学习方法在形式推理中的潜力，但将其应用于程序验证特别是VC证明领域仍然鲜有探索。尽管已有注解合成和验证相关的定理证明等研究，但没有针对自动化VC证明这一根本性瓶颈建立具体基准。本研究引入了用于验证条件的神经定理证明（NTP4VC），并使用来自Linux和Contiki-OS内核等实际项目的工业管道生成了跨形式语言（Isabelle、Lean、Rocq）的语义等价测试案例。
### Innovation
首次提出了一个实际世界多语言基准测试用例，利用Why3和Frama-C等工业管道生成了跨形式语言的语义等价测试案例。评估了大语言模型（LLMs），包括通用型和定制优化后的定理证明模型在NTP4VC上的表现，显示出LLMs在VC证明上的潜力，同时也指出了显著的挑战和研究机会。
### Conclusion
尽管大语言模型显示出了在VC证明上的潜力，但程序验证领域仍然存在显着挑战，表明该领域未来研究的巨大缺口。
## 11. `cs.CV` - The S3LI Vulcano Dataset: 一个用于不规则行星环境下多模态SLAM的数据集 [PDF](https://arxiv.org/pdf/2601.19557), [HTML](https://arxiv.org/abs/2601.19557)
### Authors
Riccardo Giubilato,Marcus Gerhard Müller,Marco Sewtz,Laura Alejandra Encinar Gonzalez,John Folkesson,Rudolph Triebel
### Background
本文档介绍了S3LI Vulcano数据集，这是一个多模态数据集，用于开发和基准测试依赖于视觉和LiDAR模态的同时定位与地图构建（SLAM）和位置识别算法。该数据集包含来自意大利西西里岛埃奥利群岛上的火山岛Vulcano的多个序列。这些序列提供了跨越各种环境、纹理和地形的数据，其中包括玄武岩石、富含铁的岩石、古老的熔岩渠道地质构造、干燥植被以及水体。
### Innovation
该数据集的创新之处在于提供了多模态数据，能够支持SLAM和位置识别算法的开发和基准测试。数据集包括不同类型的环境数据，为算法验证和改进提供了广泛的应用场景。
### Conclusion
发布的S3LI Vulcano数据集为用户提供了一个多模态数据集，该数据集适用于在不规则行星环境下进行SLAM和位置识别算法的研究和发展。该数据集不仅有助于提高算法的准确性和鲁棒性，还提供了一个开放源代码工具包，用于生成地面真实姿态以及准备用于位置识别任务的标记样本。
## 12. `cs.CV` - MaDiS：通过掩蔽扩散语言模型控制手语生成 [PDF](https://arxiv.org/pdf/2601.19577), [HTML](https://arxiv.org/abs/2601.19577)
### Authors
Ronglai Zuo,Rolandos Alexandros Potamias,Qi Sun,Evangelos Ververas,Jiankang Deng,Stefanos Zafeiriou
### Background
手语生成（SLG）旨在将书面文本转换为富有表现力的手势动作，以克服聋人和听障社区的沟通障碍。近年来，研究将SLG建模为语言模型框架内的任务，使用自回归语言模型，但这些模型存在单向上下文建模和逐个标记推理速度慢的问题。
### Innovation
提出了一种基于掩蔽扩散语言模型的MaDiS，能够捕捉双向依赖关系，支持高效并行多标记生成。提出了三层跨模态预训练方案，可以同时从标记级、潜在空间和三维物理空间的目标中学习，从而生成更加丰富和更贴近实际的手势表示。设计了一种新颖的去掩蔽策略，结合时间检查点，极大地减少了去掩蔽顺序的组合复杂性。开发了部分混合嵌入层，用于通过可学习门控和优化过的码本有效地融合不同部分手势标记中的信息。
### Conclusion
在CSL-Daily、Phoenix-2014T和How2Sign上的广泛实验表明，MaDiS在多个度量标准上实现了优于其他方法的性能，同时将推理延迟降低了近30%。代码和模型将发布在项目页面上。
## 13. `cs.CV` - 面向治理导向的低空智能：一种以管理为中心的多模态基准及隐式协调的视觉-语言推理框架 [PDF](https://arxiv.org/pdf/2601.19640), [HTML](https://arxiv.org/abs/2601.19640)
### Authors
Hao Chang,Zhihui Wang,Lingxiang Wu,Peijin Wang,Wenhui Diao,Jinqiao Wang
### Background
低空视见系统已成为智能城市治理的关键基础设施。然而，现有的以对象为中心的感知范式和松散耦合的视觉-语言管道仍然难以支持城市治理所需的现实世界中的异常理解。研究旨在弥补这一差距。
### Innovation
提出了GovLA-10K，这是首个面向治理的多模态基准，以及GovLA-Reasoner，一种专为治理感知空中视觉设计的统一视觉-语言推理框架。不同于现有的试图全面注解所有可见物体的研究，GovLA-10K围绕功能性的显著目标设计，并提供了基于这些观察的实际管理建议。GovLA-Reasoner引入了有效的特征适配器，隐式协调视觉检测器和大型语言模型之间的判别性表示共享，以有效协调细粒度的视觉定位和高层次的上下文语言推理。
### Conclusion
大量实验表明，我们的方法在不需对任何特定任务进行微调的情况下，显著提高了性能。我们认为，我们的工作为未来管理和感知导向的低空视觉-语言系统研究提供了新的视角和基础。
## 14. `cs.CV` - KeepLoRA：通过残差梯度适应进行持续学习 [PDF](https://arxiv.org/pdf/2601.19659), [HTML](https://arxiv.org/abs/2601.19659)
### Authors
Mao-Lin Luo,Zi-Hao Zhou,Yi-Lin Zhang,Yuanyu Wan,Tong Wei,Min-Ling Zhang
### Background
预训练的视觉-语言模型在持续学习中需要平衡三个方面相互矛盾的目标：保留预训练知识、保持一系列学习任务的知识、并维持获得新知识的可塑性。
### Innovation
提出了一种简单且有效的持续学习方法——KeepLoRA。该方法通过限制参数更新在残差子空间，防止干扰之前学习的能力，从而实现这三种目标的平衡。
### Conclusion
理论和经验分析证明，KeepLoRA能够在平衡这三项目标的同时，实现最先进的性能。代码已在https:// provided链接中开源。
## 15. `cs.CV` - 自监督预训练在差分隐私医疗图像分析中的作用 [PDF](https://arxiv.org/pdf/2601.19618), [HTML](https://arxiv.org/abs/2601.19618)
### Authors
Soroosh Tayebi Arasteh,Mina Farajiamiri,Mahshad Lotfinia,Behrus Hinrichs-Puladi,Jonas Bienzeisler,Mohamed Alhaskir,Mirabela Rusu,Christiane Kuhl,Sven Nebelung,Daniel Truhn
### Background
差分隐私（DP）为敏感数据提供了正式保护，但通常会导致诊断性能大幅下降。模型初始化被证明是缓解这一下降的关键因素，但现代全模型DP下的自监督学习的作用仍不清楚。
### Innovation
本研究通过大规模评估初始化策略在不同差分隐私下的医疗图像分析中的作用，使用了超过80万张胸片数据作为基准，比较了通用监督（ImageNet）初始化、通用自监督（DINOv3）初始化和领域特定监督预训练的方法。研究发现，DINOv3初始化在DP下相对于ImageNet初始化能更好提升诊断有用性，但性能仍不及领域特定的监督预训练。此外，研究还展示了初始化选择对公平性、跨数据集泛化以及在隐私约束下的鲁棒性等方面的影响。
### Conclusion
研究结果表明，初始化策略在差分隐私医疗成像中对于有用性、公平性和泛化能力是关键的决定因素。
## 16. `cs.CV` - 无侵入性3D步态分析框架在量化重度抑郁障碍中运动迟缓方面的应用 [PDF](https://arxiv.org/pdf/2601.19526), [HTML](https://arxiv.org/abs/2601.19526)
### Authors
Fouad Boutaleb,Emery Pierson,Mohamed Daoudi,Clémence Nineuil,Ali Amad,Fabien D'Hondt
### Background
重度抑郁障碍（MDD）的状态预测是当前研究的热点之一，然而，自动提取客观、可解释的特征以进行患者状态的详细分析仍有许多未探索的空间。尽管运动迟缓（PMR）是MDD的核心症状，但其临床评估主要依赖于主观手段。虽然3D动捕技术可以提供客观手段，但其依赖于专门的硬件设备，限制了其在临床中的常规使用。
### Innovation
本文提出了一个无侵入性的计算框架，将单目RGB视频转化为临床相关的3D步态动力学。作者提出了一种基于重力视坐标和新开发的轨迹修正算法的管道，利用修改后的TUG协议闭环拓扑减轻单目深度误差，从而可以从单个摄像机捕获中提取297个明确的步态生物力学生物标志物。为了应对临床数据集小的问题，作者引入了一种基于稳定性的机器学习框架，该框架能够识别出稳健的运动特征，同时防止过拟合，结果在CALYPSO数据集上验证了该方法检测运动迟缓的准确率为83.3%，解释了总体抑郁严重程度64%的变异量。
### Conclusion
研究结果显示，步态运动可以作为认知状态的稳健代理，提供了一个透明且可扩展的工具，用于在常规临床环境中客观监测抑郁症。作者的研究揭示了踝关节推进力减少和盆骨运动受限与抑郁运动表型之间的强烈联系。
## 17. `cs.CV` - ScenePilot-Bench：自动驾驶场景下视觉语言模型评估的大型数据集和基准 [PDF](https://arxiv.org/pdf/2601.19582), [HTML](https://arxiv.org/abs/2601.19582)
### Authors
Yujin Wang,Yutong Zheng,Wenxian Fan,Tianyi Wang,Hongqing Chu,Daxin Tian,Bingzhao Gao,Jianqiang Wang,Hong Chen
### Background
本文介绍了一个名为ScenePilot-Bench的大规模第一视角驾驶基准，用于评估视觉语言模型（VLMs）在自动驾驶场景中的能力。该基准建立在带有详细标注的多样数据集ScenePilot-4K之上，包含3,847小时的驾驶视频，标注了场景描述、风险评估、重要参与者识别、自我轨迹和摄像机参数等多粒度信息。
### Innovation
ScenePilot-Bench提供了一个四维度的评估套件，评估VLM在场景理解、空间感知、运动规划和GPT-Score（包含安全意识指标和跨地区泛化设置）上的能力。通过为代表性VLMs提供基准测试，本研究揭示了当前的性能边界并指出了驾驶相关推理中的空白。
### Conclusion
ScenePilot-Bench为评估和促进视觉语言模型在安全关键的自动驾驶场景中的应用提供了一个全面的框架。
## 18. `cs.CV` - GMS-CAVP: 通过多尺度对比与生成预训练改善音频-视频对应关系 [PDF](https://arxiv.org/pdf/2601.19606), [HTML](https://arxiv.org/abs/2601.19606)
### Authors
Shentong Mo,Zehua Chen,Jun Zhu
### Background
近年来，视频-音频(V-A)的理解与生成在越来越多地依赖于联合V-A嵌入方面取得了进展，这些嵌入为跨模态检索和生成等任务提供了基础。尽管方法如CAVP使用对比目标有效地建模了模态间的语义和时间对应关系，但它们的性能仍然不尽如人意。主要问题是现有框架无法充分建模视频和音频信号的密集、多尺度特性，特别是在细粒度到粗粒度的空间-时间结构对应关系上表现不足。
### Innovation
本文提出了GMS-CAVP，一种结合多尺度视频-音频对齐和多尺度时空扩散预训练目标的新框架，以增强模态间对应关系建模。首先，GMS-CAVP引入了一种多尺度对比学习策略，能够在不同的粒度级别捕捉语义和时间关系。其次，GMS-CAVP超越了传统对比学习，通过引入基于扩散的生成目标，允许视频和音频间模态之间的翻译和合成。这种统一的判别-生成公式有助于更深层次的跨模态理解，为进一步实现高保真生成铺平了道路。
### Conclusion
在VGGSound、AudioSet和Panda70M数据集上的广泛实验表明，GMS-CAVP在生成和检索任务中优于先前的方法。
## 19. `cs.CV` - 局部潜在编辑在肉毒毒素注射计划中的剂量-反应建模 [PDF](https://arxiv.org/pdf/2601.19593), [HTML](https://arxiv.org/abs/2601.19593)
### Authors
Estèphe Arnaud,Mohamed Daoudi,Pierre Guerreschi
### Background
肉毒毒素（Botox）注射是处理面部不对称和美学焕发的标准方法，但确定最佳剂量仍然很大程度上依赖直觉，这往往导致不理想的治疗结果。因此，研究提出了一种局部潜在编辑框架，通过剂量响应建模模拟肉毒毒素注射效果，以供注射计划使用。
### Innovation
开发了一种区域特异性潜在轴发现方法，该方法在StyleGAN2的潜在空间中学习局部肌肉松弛轨迹，允许对特定面部区域进行精确控制，而不产生全局副作用。通过将这些局部潜在轨迹与注入的毒素单位相关联，学习一个预测剂量响应模型。通过在临床数据集上（包含46名患者360张图像）对比直接度量回归和基于图像的生成模拟两种方法，该框架在留出测试集上对几何不对称度量表现出中等到较强的结构相关性，证明生成模型正确捕捉了形态变化的方向。虽然生物变异性限制了绝对精度，该研究还引入了一种结合人类在环的工作流程，临床医生可以交互式精化模拟，从而弥合病理重建和美容规划之间的差距。
### Conclusion
该框架在几何不对称度量上表现出中等到较强的结构相关性，证实生成模型能正确捕捉形态变化的方向。尽管存在生物学变异性导致的精度限制，研究还提出了一种结合人类在环的工作流程，以进一步优化模拟结果，满足临床实际需要。
