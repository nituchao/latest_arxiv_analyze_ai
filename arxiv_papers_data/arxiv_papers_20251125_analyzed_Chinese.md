# 20251125
[![Subscribe_Visitors](https://visitor-badge.laobi.icu/badge?page_id=nituchao.latest_arxiv_analyze_ai_rss)](https://github.com/nituchao/latest_arxiv_analyze_ai)

## 1. `cs.AI` - 在AI基准中的奇妙错误及如何发现它们 [PDF](https://arxiv.org/pdf/2511.16842), [HTML](https://arxiv.org/abs/2511.16842)
### Authors
Sang Truong,Yuheng Tu,Michael Hardy,Anka Reuel,Zeyu Tang,Jirayu Burapacheep,Jonathan Perera,Chibuike Uwakwe,Ben Domingue,Nick Haber,Sanmi Koyejo
### Background
基准在推动人工智能进步方面起着关键作用，但是无效的基准问题会削弱它们的可靠性。手动识别并纠正成千上万基准中的错误不仅不切实际，也是可靠评估的关键瓶颈。现有方法无法系统地处理这些问题，需要改进。
### Innovation
本文提出了一种基于统计分析响应模式的系统基准修订框架，用于标记可能无效的问题供进一步专家审查。该方法假设AI评估中常用的假设——均分能够充分总结模型性能，从而假设存在一个潜在的一维潜质构造，生成每项的预期统计范围。当实际估计的统计值超出项目的预期范围时，该项目更可能是问题所在。通过这种方法，针对九个广泛使用的基准，它引导专家审查并识别出问题项，识别精度高达84%。此外，引入了一个基于大语言模型（LLM）的初步审查阶段，进一步降低了人力投入。
### Conclusion
本文提出的方法为系统基准修订提供了一个高效、可扩展的框架，能够识别并修正基准中的无效问题，从而提高评价的可靠性。
## 2. `cs.AI` - Cognitive BASIC: 一种用于LLMs的内置解释型推理语言 [PDF](https://arxiv.org/pdf/2511.16837), [HTML](https://arxiv.org/abs/2511.16837)
### Authors
Oliver Kramer
### Background
已有大型语言模型（LLM）能够执行复杂的自然语言处理任务，但其推理过程往往是隐式的、难以理解的。Cognitive BASIC 是一种基于BASIC的简约提示语言及内置解释器，旨在将LLM的推理过程结构化为显式的步骤执行轨迹。它利用了现代LLM能可靠模拟简短程序的能力，使得多步透明推理成为可能。
### Innovation
Cognitive BASIC 创新性地将BASIC风格的指令和编号行用于解释性的认知控制层，通过简单命令结构化LLM的推理过程。它通过自然语言解释文件定义了命令语义、内存更新和记录行为，能够抽取命题和程序性知识，检测矛盾并生成解决方案。
### Conclusion
通过在三个LLM上的测试，显示所有模型都能执行Cognitive BASIC程序，整体而言具有较强的但不均衡的性能。这表明即使较简单的语言模型也能够进行复杂推理任务，在透明的多步骤推理方面拥有潜力。
## 3. `cs.AI` - MIR: 通过互惠内在奖励有效探索在瞬间性多智能体强化学习中的应用 [PDF](https://arxiv.org/pdf/2511.17165), [HTML](https://arxiv.org/abs/2511.17165)
### Authors
Kesheng Chen,Wenjian Luo,Bang Zhang,Zeping Yin,Zipeng Ye
### Background
瞬时奖励给强化学习带来了显著挑战。尽管内在奖励方法在单一智能体强化学习中表现出有效性，但在多智能体强化学习（MARL）中的应用仍存在问题。主要难点来自于探索空间扩展时导致的联合动作轨迹的指数级稀疏性，以及现有方法未能充分考虑能影响团队状态的联合动作。
### Innovation
本文提出了一种名为互惠内在奖励（MIR）的新策略，以应对MARL中极为稀疏的奖励面临的挑战。MIR激励个体智能体探索影响其队友的动作，并与初始策略结合使用，有效促进了团队探索并提升了算法性能。此外，将经典的单智能体MiniGrid环境扩展到MiniGrid-MA，创建一系列具有稀疏奖励的MARL环境，以全面验证提出的策略。
### Conclusion
在MiniGrid-MA环境中，与最先进的方法相比，提出的MIR方法显示了优越的性能。
## 4. `cs.AI` - Hybrid Differential Reward: Combining Temporal Difference and Action Gradients for Efficient Multi-Agent Reinforcement Learning in Cooperative Driving [PDF](https://arxiv.org/pdf/2511.16916), [HTML](https://arxiv.org/abs/2511.16916)
### Authors
Ye Han,Lijun Zhang,Dejian Meng,Zhuang Zhang
### Background
在涉及高频率连续控制的多车辆协同驾驶任务中，传统的基于状态的奖励函数会导致奖励差异消失的问题，这导致了策略梯度中的信噪比（SNR）低，严重影响了算法的收敛和性能改进。
### Innovation
论文提出了一个新颖的Hybrid Differential Reward (HDR) 机制。HDR机制创新性地结合了两种互补的部分：（1）基于全局势能函数的时间差奖励（TRD），利用势能的演化趋势确保最优策略的稳定性和长期目标的一致性。（2）动作梯度奖励（ARG），直接衡量动作的边际效用，提供具有高信噪比的局部指导信号。此外，论文将协同驾驶问题建模为具有时间变化代理集的Multi-Agent Partially Observable Markov Game（POMDPG），并通过HDR机制在该框架下进行了完整的实现。
### Conclusion
通过在线规划（MCTS）和多代理强化学习算法（QMIX, MAPPO, MADDPG）进行的广泛实验表明，HDR机制显著提高了收敛速度和策略稳定性。实验结果证实，HDR机制指导代理学习出高品质的协同策略，有效地平衡了交通效率和安全。
## 5. `cs.AI` - 比较关于贝叶斯网络推理的语义、视觉和结合解释 [PDF](https://arxiv.org/pdf/2511.16961), [HTML](https://arxiv.org/abs/2511.16961)
### Authors
Erik P. Nyberg,Steven Mascaro,Ingrid Zukerman,Michael Wybrow,Duc-Minh Vo,Ann Nicholson
### Background
贝叶斯网络（BNs）是进行概率推理的重要工具，尽管被认为是透明的模型，但人们仍然难以理解它们。现有的用户界面（UIs）没有很好地澄清BNs的推理过程。
### Innovation
设计了标准BN UI的口头和视觉扩展，以指导用户通过常见的推理模式。通过用户研究，比较了口头、视觉和结合的UI扩展与基线UI。结果显示，在某些类型的问题上，结合使用口头和视觉模态比单独使用其中一种模态效果更好。
### Conclusion
用户在涉及观察的影响、使该影响成为可能的路径以及观察如何影响其他观察的影响的问题上，使用所有三种类型的扩展UI都比基线UI表现更好。
## 6. `cs.AI` - DAPS++: 使用解耦后验退火重思扩散逆问题 [PDF](https://arxiv.org/pdf/2511.17038), [HTML](https://arxiv.org/abs/2511.17038)
### Authors
Hao Chen,Renzheng Zhang,Scott S. Howard
### Background
从贝叶斯的角度来看，得分基于的扩散解决了通过联合推断嵌入先验的似然性来指导采样的逆问题。然而，这种描述未能解释其实用行为：先验提供的指导有限，而重建主要由一致性度量项驱动，导致推断过程实质上与扩散动态脱节。
### Innovation
我们重新解释了逆问题中的扩散作用，将其视为期望-最大化（EM）框架下的初始化阶段，扩散阶段与数据驱动的细化完全脱耦。我们引入了DAPS++，这使似然项能够更直接地引导推断，同时保持数值稳定性，并提供了解释为什么统一的扩散轨迹在实践中仍然有效的原因。
### Conclusion
通过需求较少的功能评估次数（NFEs）和测量优化步骤，DAPS++实现了高效计算和稳健的重建性能，适用于多种图像恢复任务。
## 7. `cs.AI` - BDI模型用于建模心智能体和代理 [PDF](https://arxiv.org/pdf/2511.17162), [HTML](https://arxiv.org/abs/2511.17162)
### Authors
Sara Zuppiroli,Carmelo Fabio Longo,Anna Sofia Lippolis,Rocco Paolillo,Lorenzo Giammei,Miguel Ceriani,Francesco Poggi,Antonio Zinilli,Andrea Giovanni Nuzzolese
### Background
Belief-Desire-Intention (BDI)模型是人工智能和认知科学中代表理性代理的核心。然而，该模型在结构化的、语义互操作的知识表示中的集成仍然有限。
### Innovation
本文提出了一种形式化的BDI本体，它作为一种模块化的本体设计模式（ODP），通过信念、欲望、意图及其动态关系来捕捉代理的认知架构。本研究通过将本体与大型语言模型（LLMs）结合进行逻辑增强生成（LAG）来评估本体论基础对语义连贯性和一致性的贡献，并通过集成在Semas推理平台内，实现了S4推理范式的双向流动，从而连接了资源描述框架（RDF）三元组与代理心理状态。
### Conclusion
这两项实验展示了BDI本体作为概念和操作桥梁的作用，连接了声明性和过程性智能，为基于Web数据的具备认知基础、可解释性和语义互操作能力的多代理和神经符号系统铺平了道路。
## 8. `cs.AI` - 稳固扩散模型揭示视觉创造力中人与AI持续差距 [PDF](https://arxiv.org/pdf/2511.16814), [HTML](https://arxiv.org/abs/2511.16814)
### Authors
Silvia Rondini,Claudia Alvarez-Martin,Paula Angermair-Barkai,Olivier Penacchio,M. Paz,Matthew Pelowski,Dan Dediu,Antoni Rodriguez-Fornells,Xim Cerda-Company
### Background
尽管近期研究表明大规模语言模型在发散性思考任务中可与人类创意表现相匹敌，但在视觉创意领域的研究仍然不足。本研究对比了人类参与者（艺术家和非艺术家）与使用图像生成AI模型（两种提示条件，分别带有人类高指导和低指导）在视觉创意方面的表现。
### Innovation
研究使用稳定的扩散模型来评估人类和AI在视觉创意方面的差异，并通过不同指导水平的比较，探讨AI生成创意成果与人类创意表现的差距；此外，研究还揭示了人类评审者与AI评审者在创造力评价标准上的显著差异。
### Conclusion
研究表明，视觉领域中的AI模型在创造力方面仍面临独特挑战。人类评审者和AI评审者在评价创造力时表现出截然不同的模式。结果表明，基于语言的任务上，AI模型可能难以在视觉领域中实现等同的创造性表现，这主要由于视觉领域依赖于感知细微差别和上下文敏感性，而这些能力是人类特有的，可能无法轻易迁移至语言模型中。
## 9. `cs.AI` - 使用贝叶斯网络整合一致化文本和表格证据的患者级信息提取 [PDF](https://arxiv.org/pdf/2511.17056), [HTML](https://arxiv.org/abs/2511.17056)
### Authors
Paloma Rabaey,Adrick Tench,Stefan Heytens,Thomas Demeester
### Background
电子健康记录(EHRs)是训练临床决策支持系统的重要资源。为了在高风险应用中发挥这些系统的潜力，需要构建透明特征模型，因此需要大规模的结构化表格数据集。虽然部分EHR已包含结构化信息（如诊断代码、用药情况和实验室结果），但仍有许多信息储存在未经结构化的文本中（如出院总结和护理笔记）。这项工作中，作者提出了一种多模态患者级信息提取方法，利用患者EHR中的标记信息（使用专家告知的贝叶斯网络）和描述患者症状的临床笔记（使用神经文本分类器）。
### Innovation
作者提出了利用虚拟证据和一致性节点，进行多模态患者级信息的整合方法。这种方法通过贝叶斯网络融合神经分类器的预测结果，并通过一致性节点提高最终预测的校准度，使得贝叶斯网络能够更好地调整神经分类器的输出以处理缺失信息和矛盾之处。
### Conclusion
通过在SimSUM数据集上的实验，作者展示了该方法在通过专家知识将表格EHR和临床笔记整合方面的潜力。
## 10. `cs.AI` - 预算意识下的工具使用使代理扩展更加有效 [PDF](https://arxiv.org/pdf/2511.17006), [HTML](https://arxiv.org/abs/2511.17006)
### Authors
Tengxiao Liu,Zifeng Wang,Jin Miao,I-Hung Hsu,Jun Yan,Jiefeng Chen,Rujun Han,Fangyuan Xu,Yanfei Chen,Ke Jiang,Samira Daruki,Yi Liang,William Yang Wang,Tomas Pfister,Chen-Yu Lee
### Background
在大型语言模型（LLM）的不同任务上扩展测试时的计算可以提高性能，这已被延伸到工具增强型代理。对于这些代理，扩展不仅涉及“思考”令牌，还涉及通过工具调用“行动”。工具调用的数量限制了代理与外部环境的交互程度。然而，我们发现简单地授予代理更大的工具调用预算无法提高性能，因为这些代理缺乏预算意识，很快就会遇到性能天花板。
### Innovation
我们研究了如何在明确的工具调用预算下有效扩展代理，专注于网页搜索代理。首先引入了预算追踪插件，使代理具有连续的预算意识，实现了简单的扩展。我们进一步开发了BATS（预算感知测试时扩展）框架，利用这种意识动态调整其计划和验证策略，根据剩余资源决定是“深入”探索有希望的线索还是“转向”新的路径。我们为成本与性能扩展的分析提供了统一的成本度量，提供了第一个关于预算约束代理的系统研究，展示了预算感知方法会产生更优的扩展曲线，推动了成本与性能的帕累托前沿。
### Conclusion
我们的工作提供了关于工具增强型代理扩展透明且原理化的实证见解。
## 11. `cs.AI` - MirrorMind：赋予全科科学家人类科学家专家视角和集体知识的力量 [PDF](https://arxiv.org/pdf/2511.16997), [HTML](https://arxiv.org/abs/2511.16997)
### Authors
Qingbin Zeng,Bingbing Fan,Zhiyu Chen,Sijian Ren,Zhilun Zhou,Xuhua Zhang,Yuanyi Zhen,Fengli Xu,Yong Li,Tie-Yan Liu
### Background
人工智能科学家展现了在自动化科学研究方面的巨大潜力。现有方法主要将科学发现视为单一的最优化或搜索过程，忽视了知识生成本质上是一个社会和历史的进程。现有的大型语言模型仍然难以表现个体的认知和社会结构。为了弥合这一缺口，提出了MirrorMind，一种分层认知架构，涉及三人层次框架中的双记忆表示。
### Innovation
介绍了一种名为MirrorMind的层次认知架构，该架构在三个层次上融合了双记忆表示：1. 个人层次构建了高保真度研究人员的认知模型，捕捉他们的事件、语义和人物记忆。2. 领域层次将集体知识映射到结构化的学科概念图。3. 多学科层次作为正交的编排引擎。此外，架构将记忆存储与动执行分离，使AI科学家代理灵活地访问个体记忆以获得独特视角或集体结构以便推理。
### Conclusion
通过将个体认知深度与集体学科广度结合，MirrorMind超越了简单的事实检索，实现了结构化、个性化和洞察性的科学研究推理。通过四个全面任务进行了评估，包括作者级认知模拟、补充性推理、跨学科协作促进以及多代理科学研究解决问题。
## 12. `cs.AI` - 使能人工智能（Agentic AI） [PDF](https://arxiv.org/pdf/2511.17332), [HTML](https://arxiv.org/abs/2511.17332)
### Authors
Virginia Dignum,Frank Dignum
### Background
本文探讨了使能人工智能（Agentic AI）的概念，旨在赋予系统持续的自主性、推理能力和交互能力。要实现这一愿景，必须通过明确的认知模型、合作和治理来补充有关代理的假设。
### Innovation
本文认为，自主代理和多代理系统（AAMAS）社区内发展起来的概念工具，如BDI架构、通信协议、机制设计和制度建模，提供了这种所需的基石。通过将适应性和数据驱动的方法与推理和协调的结构化模型相结合，本文提出了走向不仅具备能力和灵活性，而且具备透明性、合作性和问责性的使能系统的方法。
### Conclusion
本文提出了一个关于代理性的视角，该视角连接形式理论与实际自主性。
## 13. `cs.AI` - 那不是自然的：脱策数据对探针性能的影响 [PDF](https://arxiv.org/pdf/2511.17408), [HTML](https://arxiv.org/abs/2511.17408)
### Authors
Nathalie Kirch,Samuel Dower,Adrians Skapars,Ekdeep Singh Lubana,Dmitrii Krasheninnikov
### Background
探针已逐渐成为监测大规模语言模型（LLMs）的有效方法，能够在推理阶段检测诸如欺骗和捧场等令人关切的行为。然而，很多自然发生的实例稀少，导致研究者不得不依赖合成或脱策策略的LLM响应来训练探针。
### Innovation
研究系统性地评估了使用合成和脱策数据对探针泛化的不同影响，通过在多种LLM上测试线性和注意探针，并发现响应生成策略对探针表现有显著影响，但这种影响因行为而异。研究发现，脱策数据的成功泛化预示着针对实际场景的成功泛化。此外，数据域的变化显著影响性能，不同域的测试分数明显低于相同域。
### Conclusion
在缺乏在策数据的情况下，使用相同域的脱策数据生成的探针比使用不同域的在策数据更可靠。这强调了亟需方法来更好地处理LLM监测中的分布偏移问题。
## 14. `cs.AI` - 通过分层任务抽象机制设计专用领域代理 [PDF](https://arxiv.org/pdf/2511.17198), [HTML](https://arxiv.org/abs/2511.17198)
### Authors
Kaiyu Li,Jiayu Wang,Zhi Wang,Hui Qiao,Weizhan Zhang,Deyu Meng,Xiangyong Cao
### Background
LLM驱动的代理，尤其是那些采用通用框架（如ReAct或受人类启发的角色扮演）的代理，在需要严格结构化工作流程的专业领域中经常遇到困难。像遥感领域这样的专业领域需要特定工具（例如修正、光谱指数计算）和多步骤过程（例如多个中间产品和可选步骤），这挑战了通用方法。
### Innovation
我们提出了一种新的代理设计框架，即分层任务抽象机制（HTAM）。HTAM突破了模仿社会角色的局限性，而是将多代理系统逻辑化地分层为给定领域的内在任务依赖性图。这种以任务为中心的架构确保了程序的正确性，并将复杂问题分解成顺序层次，其中每一层的子代理都基于前一层的输出进行操作。我们通过地球代理（tailored for complex geospatial analysis）实例化了这一框架。为评估复杂的规划能力，我们构建了GeoPlan-bench，这是用于地理空间多步骤规划任务的全面基准，包含了精心设计的评估指标，用于评估工具选择、路径相似性和逻辑完整性。
### Conclusion
实验表明，地球代理显著优于一系列现有的单个和多代理系统。我们的工作表明，将代理架构与领域的内在任务结构对齐是构建稳健和可靠的专用自主系统的关键步骤。
## 15. `cs.AI` - LLMs如何理解突尼斯阿拉伯语？ [PDF](https://arxiv.org/pdf/2511.16683), [HTML](https://arxiv.org/abs/2511.16683)
### Authors
Mohamed Mahdi
### Background
大型语言模型（LLMs）驱动着当今的AI代理，它们能够理解人类语言得越好，与AI的交互就自然和用户友好得越多。然而，工业规模的LLMs理解低资源语言（如突尼斯阿拉伯语（突尼斯语））的能力常常被忽视。这可能导致大量突尼斯人无法完全用自己语言与AI互动，而转向使用法语或英语。这种转变不仅威胁着突尼斯方言的保存，还可能对文盲问题产生影响，并影响年轻一代更偏好外语。
### Innovation
本研究引入了一个包含突尼斯语、标准突尼斯阿拉伯语和英语平行翻译的新数据集，并附有情感标签。对几种流行的LLMs在语言转写、翻译和情感分析三种任务上的表现进行了基准测试，揭示了模型之间的显著差异，强调了低资源语言在下一代AI系统中的重要性。
### Conclusion
通过量化这些差异，本工作突显了在下一代AI系统中包含低资源语言的重要性，以确保技术的可访问性、包容性和文化根植性。
## 16. `cs.AI` - 基于提示的价值导向大型语言模型 [PDF](https://arxiv.org/pdf/2511.16688), [HTML](https://arxiv.org/abs/2511.16688)
### Authors
Giulio Antonio Abbo,Tony Belpaeme
### Background
随着大型语言模型在需要与人类价值观对齐的应用中的日渐普及，模型微调被用来确保安全的响应，但这一技术是静态的，无法适应涉及动态价值观和偏好的日常情况。
### Innovation
本文提出了一种实用、可复现且模型无关的方法，用于评估提示能否引导生成文本向特定的人类价值观靠拢，并制定了一个评分方法来量化生成响应中目标价值观的存在及其增加量。实验在Wizard-Vicuna语言模型变体上进行，采用Schwartz的基本人类价值观理论和结构化评估方法的对话数据集。表明即使不修改模型或动态优化提示，也可以实现价值导向。
### Conclusion
本研究提出了一种评分方法来衡量大型语言模型在生成文本中目标价值观的存在及其增加量，并展示了只需基于提示就可以实现价值导向的效果。
## 17. `cs.AI` - 使用扩散桥模型进行蛋白质表面和结构的联合设计 [PDF](https://arxiv.org/pdf/2511.16675), [HTML](https://arxiv.org/abs/2511.16675)
### Authors
Guanlue Li,Xufeng Zhao,Fang Wu,Sören Laue
### Background
蛋白质-蛋白质相互作用（PPIs）由蛋白质界面的表面互补性和疏水相互作用控制。然而，在计算蛋白质设计中，设计具有物理现实性和精准靶向受体互补性的多样化蛋白质结构和表面仍是一个重大挑战。
### Innovation
PepBridge 是一种新型框架，通过结合受体表面几何和生物化学特性，实现蛋白质表面和结构的联合设计。该框架首先使用去噪扩散桥模型（DDBMs）将受体表面映射到配体表面，然后采用多模型扩散模型预测相应的结构，并通过形状框架匹配网络确保表面几何和骨架结构之间的对齐。
### Conclusion
在不同蛋白质设计场景下进行了广泛验证，证明了PepBridge在生成结构性蛋白质方面的有效性，标志着在蛋白质结构的联合设计方面取得了重要进展。
## 18. `cs.AI` - 基于椭球体的决策边界在开放意图分类中的应用 [PDF](https://arxiv.org/pdf/2511.16685), [HTML](https://arxiv.org/abs/2511.16685)
### Authors
Yuetian Zou,Hanlei Zhang,Hua Xu,Songze Li,Long Xiao
### Background
文本开放意图分类对于实际对话系统至关重要，能够帮助系统在缺乏先验知识的情况下稳健地检测未知用户意图，并提高系统的鲁棒性。现有的自适应决策边界方法通过消除手动阈值调整展现出巨大潜力，但它们假设已知类别的分布是等向性的，这限制了边界只能是球体，并忽略了不同方向上的分布差异。
### Innovation
本文提出了EliDecide，一种新颖的方法，学习不同特征方向上具有不同尺度的椭球决策边界。首先，使用监督对比学习获得已知样本的可分辨特征空间。其次，使用可学习的矩阵参数化每个已知类别的椭球边界，这提供了比仅由中心和半径定义的球形边界更大的灵活性。最后，通过一个新颖设计的双重损失函数优化边界，该函数平衡了经验风险和开放空间风险：扩大边界以覆盖已知样本，并收缩边界以对抗合成的伪开放样本。
### Conclusion
EliDecide方法在多个文本意图基准测试中实现了最先进的性能，并进一步在一个问题分类数据集中取得了好成绩。椭球体的灵活性验证了其优越的开放意图检测能力和对多样且复杂的开放世界场景中更多文本分类任务的强大泛化潜力。
## 19. `cs.AI` - 可持续作业车间调度的实例配置 [PDF](https://arxiv.org/pdf/2409.18972), [HTML](https://arxiv.org/abs/2409.18972)
### Authors
Christian Perez,Carlos March,Miguel A. Salido
### Background
作业车间调度问题(JSP)是运筹学中的关键挑战，对于评估调度算法的有效性和性能至关重要。调度问题属于组合优化的重要领域，目的是在完成时间（工期）和其他目标如能耗最小时，合理分配资源（机器）给任务。这项研究深入探讨了JSP的复杂性，重点关注在满足各种约束（如截止日期和发布日期）的同时优化性能指标和减少能耗。认识到JSP基准测试的多维性，该研究强调了JSPLIB等参考库和数据集在算法评估中的重要意义。研究强调了问题实例特征的重要性，包括工作和机器的数量、加工时间以及机器的可用性，突出了考虑能耗因素所带来的复杂性。
### Innovation
提出了一个新颖的实例配置器，该配置器包含工作数量、机器数量、任务数量和速度等参数，同时还包含加工时间和能耗的分布。生成的实例包含了各种配置，反映现实场景和操作约束。这些实例促进了调度算法的全面基准测试和评估，特别是在能效方面。
### Conclusion
生成了一套包含500个测试实例，并已公开发布，促进了进一步的研究和JSP基准测试。通过提供多样化的场景，这些实例为开发先进的、能效高的调度解决方案提供了强健的分析基础并促进了协作。
## 20. `cs.AI` - Shona spaCy: 一种用于欠资源班图语的语形分析器 [PDF](https://arxiv.org/pdf/2511.16680), [HTML](https://arxiv.org/abs/2511.16680)
### Authors
Happymore Masoka
### Background
尽管多语言自然语言处理（NLP）取得了快速进展，班图语种的绍诺语（Shona）在词形分析及语言敏感工具方面仍然处于不利地位。绍诺语缺乏形态分析工具，这限制了其在现代NLP应用中的广泛使用。
### Innovation
本文介绍了一种基于spaCy框架的开放源代码、基于规则的绍诺语形态管道——绍诺spaCy（Shona spaCy）。该系统结合了一个精编的JSON词典和基于语言学的规则，用于建模名词类前缀（Mupanda 1-18）、动词主语一致词缀、时态标记、拟声词和粘附词，通过将这些模型整合到标记级别的注释中，用于词干、词性及形态特征的标注。该工具包通过pip install shona-spacy安装，源代码可在指定的网址找到，PyPI发布版本可以在另一个指定的网址找到。绍诺spaCy在形态特征准确性和词性标注准确率上分别达到了88%和90%，同时保持了语言决定的透明性。绍诺spaCy通过融合描述性语法和计算实现，促进了绍诺语的NLP可访问性和数字包容性，并为其他欠资源班图语的形态分析工具提供了模板。
### Conclusion
绍诺spaCy通过结合绍诺语的语言规则和现代计算框架，为绍诺语的NLP工具建设迈出了重要一步，同时为其他欠资源班图语的工具开发提供了参考模板。
## 21. `cs.AI` - SRA-CP：自发风险感知选择性协同感知 [PDF](https://arxiv.org/pdf/2511.17461), [HTML](https://arxiv.org/abs/2511.17461)
### Authors
Jiaxi Liu,Chengyuan Ma,Hang Zhou,Weizhe Tang,Shixiao Liang,Haoyang Ding,Xiaopeng Li,Bin Ran
### Background
合作感知（CP）通过让联网车辆共享信息，克服了单一车辆感知的局限性。然而，现有的通用CP方法需要传输大量的与驾驶安全无关的数据，这些数据超过了可用的通信带宽。大多数CP框架依赖于事先定义的通信伙伴，使其不适合动态交通环境。
### Innovation
本文提出了一种自发风险感知选择性协同感知（SRA-CP）框架，以解决这些挑战。SRA-CP引入了一种去中心化协议，其中连接的代理持续广播轻量级感知覆盖摘要，并仅在检测到风险相关的盲区时才启动目标合作。通过感知风险识别模块，每个联网车辆可以局部评估遮挡对其驾驶任务的影响，并决定是否需要合作。当CP被触发时，自身车辆会根据共享感知覆盖选择合适的伙伴，并通过融合模块进行信息交换，该模块优先考虑安全关键内容并适应带宽限制。
### Conclusion
SRA-CP 与几个代表性基准方法在公共数据集上进行了评估。结果显示，SRA-CP 相对于通用的 CP 方法，对于安全关键对象的平均精度（AP）损失不到 1%，而仅使用 20% 的通信带宽。此外，它还比现有的不包含风险感知的选择性 CP 方法提高了 15% 的感知性能。
## 22. `cs.AI` - 向VecDB中高效RAG系统的方向：分布式并行多分辨率向量搜索 [PDF](https://arxiv.org/pdf/2511.16681), [HTML](https://arxiv.org/abs/2511.16681)
### Authors
Dong Liu,Yanxuan Yu
### Background
检索增强生成（RAG）系统已经成为通过外部知识增强大型语言模型（LLMs）的主要方法。然而，现有的向量数据库（VecDB）检索管道依赖于扁平的或单一解析度的索引结构，这不能适应不同用户查询所需的变动语义粒度。这一限制导致了检索速度和语境相关性之间的次优权衡。
### Innovation
本文提出了语义分层索引（SPI），这是一种新颖的多解析度向量索引框架，通过轻量级分类器引入查询自适应解析度控制，用于VecDB中的RAG。SPI在现有分层方法需要离线调优或独立模型训练的基础上，构建文档嵌入的语义金字塔，并通过动态选择每个查询的最佳解析度层次，实现了从粗略到精细的检索，显著加快了搜索速度，同时保持了语义覆盖。
### Conclusion
SPI框架在FAISS和Qdrant后端实现，并在MS MARCO、自然问题和多模态检索基准任务上进行了评估，结果显示检索速度提高了5.7倍、内存效率提高了1.8倍，并在端到端的问答F1分数上提高了2.5个百分点。理论分析提供了检索质量和延迟的保证，而广泛的消融实验验证了每个组件的贡献。该框架与现有VecDB基础设施兼容，便于部署到生产RAG系统中。
## 23. `cs.AI` - Bench360：360°评估本地大语言模型推理 [PDF](https://arxiv.org/pdf/2511.16682), [HTML](https://arxiv.org/abs/2511.16682)
### Authors
Linus Stuhlmann,Mauricio Fadel Argerich,Jonathan Fürst
### Background
本地运行大语言模型（LLMs）变得越来越普遍。尽管小规模开源模型和推理引擎的可用性提高降低了入门门槛，但用户现在面临着大量的配置选择。选择最优配置（平衡功能和非功能要求）需要大量的手工努力。虽然现有的基准测试针对LLM推理，但它们通常设计用于狭窄的评估目标且用户导向性不足，未能将系统和任务相关的指标整合到易于使用的统一基准测试中，该基准支持多种推理引擎、使用场景和量化水平。为解决这一缺口，本文提出了Bench360——全方位评估本地LLM推理。Bench360允许用户轻松定义自定义任务，包括相关数据集和任务特定指标，自动跨不同使用场景（单一流、批处理与服务器）对选定的LLMs、推理引擎和量化水平进行基准测试。它跟踪广泛的指标，包括系统指标（如计算性能、资源使用、部署）和任务特定指标（如ROUGE、F1分数或准确率）。
### Innovation
Bench360能够全面评估本地LLMs的推理表现，允许用户自定义任务、数据集和特定任务指标，自动跨不同使用场景测试选定的LLMs、推理引擎和量化程度。它跟踪广泛的指标，包括系统指标和任务特定指标，提供了一种更全面和易用的评估方法。此外，它揭示了任务性能与系统效率之间的权衡，显示了不同推理引擎和模型之间的差异，并指出没有最优的本地推理配置，强调了需要建立Bench360这样的框架的必要性。
### Conclusion
Bench360揭示了任务性能与系统效率之间的权衡，并指出没有最优的本地推理配置，突显了Bench360的重要性。这一框架有助于用户更好地理解不同LLM和推理引擎的表现，为实际应用提供指导。
## 24. `cs.AI` - 基于概念的可解释性在有害内容检测中的应用 [PDF](https://arxiv.org/pdf/2511.16689), [HTML](https://arxiv.org/abs/2511.16689)
### Authors
Samarth Garg,Deeksha Varshney,Divya Singh
### Background
社交媒体的发展不仅促进了沟通，还使得有害内容的传播更加容易。尽管在有害语言检测方面取得了显著进展，但基于概念的解释仍然较少。以往的研究主要集中在检测有害语言上，而较少关注这些概念如何直接影响模型的输出结果，导致分类错误。
### Innovation
本文提出了一种基于概念梯度（Concept Gradient, CG）的可解释性技术，通过测量概念变化对模型输出的影响来提供更为因果的关系解释。还提出了目标词汇集的精炼方法，计算词汇-概念对齐（Word-Concept Alignment, WCA）分数，量化这些词汇由于对有毒概念的过度归因导致的分类错误。此外，还引入了一种无词典增强策略，通过生成排除预定义有毒词汇集的有毒样本，研究当去除显式的词汇重叠时，过度归因是否仍然存在，从而揭示模型在更广泛有害语言模式上的归因情况。
### Conclusion
通过引入基于概念梯度的方法和词汇集精炼方法，本文提供了一种新的有害语言检测可解释性的分析框架，可以更准确地识别和纠正模型中的误分类，同时提出了一种新的无词典增强策略，有助于进一步理解模型在有害语言检测中的归因情况。
## 25. `cs.AI` - 基于未见过词汇的层次检索：SNOMED CT 案例研究 [PDF](https://arxiv.org/pdf/2511.16698), [HTML](https://arxiv.org/abs/2511.16698)
### Authors
Jonathon Dilworth,Hui Yang,Jiaoyan Chen,Yongsheng Gao
### Background
SNOMED CT 是一种生物医学本体，具有大规模概念的层次化表示。由于语言歧义、同义词、多义词等原因，在SNOMED CT 中的知识检索至关重要但常常困难重重。当查询为未见过词汇（OOV）时，问题变得更加复杂，因为这些查询在本体中没有相应的匹配。本文聚焦于使用OOV查询从SNOMED CT 中检索层次概念的问题。
### Innovation
本文提出了一种基于语言模型的本体嵌入方法来解决OOV查询的层次概念检索问题。实验表明，该方法在评估标准下优于S-BERT 和 两种词法匹配方法。
### Conclusion
本文的方法在SNOMED CT 上进行了评估，但鉴于其通用性和对其他本体的可扩展性，该方法具有广泛的适用性。我们发布了相关代码、工具和评估数据集。
## 26. `cs.AI` - 检测和引导LLMs的行为中的共情能力 [PDF](https://arxiv.org/pdf/2511.16699), [HTML](https://arxiv.org/abs/2511.16699)
### Authors
Juan P. Cadile
### Background
本文探讨了在进行任务时愿意牺牲任务效率以应对人类需求的行为（即共情行动）作为一种在大语言模型（LLM）激活空间中的线性方向。研究聚焦于使用基于共情行动基准（EIA）的对比提示，测试共情检测和引导在不同模型之间的效果。
### Innovation
研究使用对比提示进行共情行动检测和引导，测评了Phi-3-mini-4k、Qwen2.5-7B（经过安全训练）和Dolphin-Llama-3.1-8B（未经过清洗）三种不同模型。发现未经过清洗处理的模型也能表现出共情编码能力，这表明这种能力的形成独立于安全训练。此外，还揭示了模型在共情检测和引导方面的差异，尤其是建筑特异性实现机制。
### Conclusion
不同模型在共情检测和引导方面的效果存在差异。Qwen和Phi-3在双向控制和一致性方面表现良好；而Dolphin仅在提升共情方面表现出强大且稳定的特性，但在反共情引导下会破环。这项研究表明，安全训练可能会影响引导的稳定性，但并不是完全防止操纵。需要更多模型进行验证。
## 27. `cs.AI` - AutoBackdoor: 通过LLM代理自动化后门攻击 [PDF](https://arxiv.org/pdf/2511.16709), [HTML](https://arxiv.org/abs/2511.16709)
### Authors
Yige Li,Zhe Li,Wei Zhao,Nay Myat Min,Hanxun Huang,Xingjun Ma,Jun Sun
### Background
后门攻击对大型语言模型（LLMs）的安全部署构成严重威胁，使对手能够植入由特定输入触发的隐藏行为。目前，现有的方法通常依赖人工设计的触发器和静态数据管道，这使得它们在系统性评估现代防御的鲁棒性时显得僵硬、耗时且不足。随着AI代理能力的增强，需要更严谨、更多样和更具扩展性的‘红队’框架来模拟后门威胁并评估模型在对抗条件下的恢复能力。
### Innovation
AutoBackdoor 是一种自动化后门注入的一般框架，包含了触发器生成、恶意数据构建和模型微调的自主代理驱动管道。与之前的框架不同，AutoBackdoor 使用强大的LLM代理生成语义连贯、上下文感知的触发短语，这使得可以跨越任意话题高效毒化，而无需大量的人工努力。
### Conclusion
实验表明，AutoBackdoor 在多种现实威胁场景下达到超过90%的攻击成功率，且仅需少量恶意样本。更重要的是，我们的研究表明现有防御经常无法遏制这些攻击，凸显了探索这一工作所提出的方法的重要性，即如何更严格和适应性地评估针对代理驱动威胁的方法。所有代码、数据集和实验配置最终将整合到我们的主要存储库中。
## 28. `cs.AI` - 通过社交网络数据曝光进行密码强度分析：依赖数据重构和生成模型的结合方法 [PDF](https://arxiv.org/pdf/2511.16716), [HTML](https://arxiv.org/abs/2511.16716)
### Authors
Maurizio Atzori,Eleonora Calò,Loredana Caruccio,Stefano Cirillo,Giuseppe Polese,Giandomenico Solimando
### Background
尽管密码仍是防止未授权访问的主要防线，但用户通常倾向于使用易于记住的密码，这会导致安全风险增加。传统密码强度评估方法往往不足。实验表明，基于社交网络等公开数据进行密码强度分析可以提高评估准确度。
### Innovation
提出了SODA ADVANCE数据重构工具，通过整合利用多渠道信息（包括社交媒体）的特殊模块来评估密码强度。此外，研究了新兴大型语言模型（LLMs）在生成和评估密码方面的功能和风险。实验结果显示，LLMs能够生成强且个性化的密码，并在考虑用户资料数据时评估密码效果更好。
### Conclusion
SODA ADVANCE工具通过利用公开数据增强了密码强度评估过程，而LLMs在密码生成和评估中表现出一定的潜力，但仍需注意其风险。
## 29. `cs.AI` - DDTime：用于时间序列预测的光谱对齐和信息瓶颈数据集蒸馏 [PDF](https://arxiv.org/pdf/2511.16715), [HTML](https://arxiv.org/abs/2511.16715)
### Authors
Yuqi Li,Kuiye Ding,Chuanguang Yang,Hao Wang,Haoxuan Wang,Huiran Duan,Junming Liu,Yingli Tian
### Background
时间序列预测在许多领域都是基础问题，但训练准确模型通常需要大规模数据集和大量计算资源。数据集蒸馏提供了一种有前景的替代方案，通过合成紧凑数据集来保留完整数据的学习行为。然而，将数据集蒸馏扩展到时间序列预测相当具有挑战性，因为两个基本问题：强烈的自相关性导致教师和学生模型之间值-项对齐的偏差；合成样本之间的多样性，由于缺乏明确的类别先验来规范轨迹多样性。
### Innovation
本文提出了DDTime，一种基于一阶凝缩分解的轻量级且插件式的蒸馏框架。DDTime重新审视了通过时域统计对值-项对齐，并引入了频域对齐机制来减轻自相关性导致的偏差，确保光谱一致性和时态保真度。为了应对挑战2，DDTime进一步设计了一种基于信息瓶颈原理的样本间正则化，它增强了多样性并最大化了合成轨迹中的信息密度。该综合目标与广泛的凝缩范式理论兼容，支持稳定的单阶优化。广泛实验结果显示，DDTime在20个基准数据集和多种预测架构上持续优于现有蒸馏方法，相对准确性提高了约30%，而计算开销仅增加了约2.49%。
### Conclusion
广泛的实验表明，DDTime在20个基准数据集上持续优于现有的蒸馏方法，相对准确性提高了约30%，而计算开销仅为约2.49%。所有代码和蒸馏数据集将被发布。
## 30. `cs.AI` - 一种用于改进惯性约束聚变图像降噪的机器学习驱动方法 [PDF](https://arxiv.org/pdf/2511.16717), [HTML](https://arxiv.org/abs/2511.16717)
### Authors
Asya Y. Akkus,Bradley T. Wolfe,Pinghan Chu,Chengkun Huang,Chris S. Campbell,Mariana Alvarado Alvarez,Petr Volegov,David Fittinghoff,Robert Reinovsky,Zhehui Wang
### Background
中子成像对于优化惯性约束聚变（ICF）事件的分析至关重要，特别是在国家点火设施（NIF）和其他ICF平台中。然而，中子源的图像常常受到各种类型的噪声影响。最常见的噪声类型是高斯噪声和泊松噪声的组合，这会模糊边缘并隐藏重要细节。这些噪声类型通常重叠，使得通过传统的滤波和阈值方法区分和去除它们变得困难。因此，对于中子源图像分析和解释而言，保留图像保真度的噪声去除技术非常重要。目前，通常使用滤波和阈值结合的方法。过去，由于缺乏ICF过程的真实数据，因此在降噪方面很少使用机器学习方法。不过，最近合成数据生产技术的进步，特别是在聚变成像领域，为使用监督和无监督机器学习方法研究新去噪过程提供了机会。
### Innovation
本研究实施了一种基于无监督自编码器的方法，使用Cohen-Daubechies-Feauveau（CDF 97）小波变换在潜在空间中进行混合高斯-泊松降噪。该网络成功地去噪了中子成像数据，并在与基于前向模型的数据进行基准测试时，显示了较低的重建误差和更优越的边缘保留指标，相较于非ML基底的滤波技术，如块匹配和3D滤波（BM3D）。
### Conclusion
本方法展示了一种有前景的中子图像噪声减少和ICF实验三维重建分析的进展。
## 31. `cs.AI` - 错误指控：AI检测器如何误判微调过的阿拉伯文章 [PDF](https://arxiv.org/pdf/2511.16690), [HTML](https://arxiv.org/abs/2511.16690)
### Authors
Saleh Almohaimeed,Saad Almohaimeed,Mousa Jari,Khaled A. Alobaid,Fahad Alotaibi
### Background
许多AI检测模型被开发出来以对抗由人工智能生成的文章。然而，如果一篇由人类撰写的文章经过轻微的人工智能润色，这些模型可能会误判，将其视为AI生成的文章。这可能导致作者被错误地指控为AI剽窃，损害AI检测模型的可信度。尽管在英文中已经有一些研究解决了这一问题，但在阿拉伯语领域还没有相应的解决方案。
### Innovation
本文提出了两个阿拉伯语数据集：第一个包含400篇由10种大型语言模型润色的人类撰写的阿拉伯文章，第二个数据集Ar-APT包含了400篇人类撰写的阿拉伯文章，经过10种大型语言模型的不同润色设置共计16400个样本。这些数据集的目的是评估不同大型语言模型和商业AI检测器在区分人类撰写和AI生成文章的能力，尤其是轻微润色的影响。研究结果揭示了所有AI检测器在误判AI文章方面的不准确，并分析了不同模型在经过轻微润色后性能的变化。
### Conclusion
研究结果表明，所有的AI检测器都错误地标记了大量的文章为AI生成。绩效最佳的大型语言模型Claude-4 Sonnet在不受润色影响时达到了83.51%的性能，但在被LLaMA-3轻微润色的文章中，其性能下降到了57.63%。对于最出色的商业模型，准确率为92%的，其性能在被Mistral或Gemma-3轻微润色的文章中下降到了12%。这表明，即使是先进的AI检测器，在面对略微经过AI润色的人类撰写文章时，也会产生误判，其性能显著下降。
## 32. `cs.AI` - 生成型增强现实：范式、技术及其未来应用 [PDF](https://arxiv.org/pdf/2511.16783), [HTML](https://arxiv.org/abs/2511.16783)
### Authors
Chen Liang,Jiawen Zheng,Yufeng Zeng,Yi Tan,Hengye Lyu,Yuhui Zheng,Zisu Li,Yueting Weng,Jiaxin Shi,Hanwang Zhang
### Background
本论文介绍了生成型增强现实（GAR）作为一种下一代范式，它将增强过程重新定义为世界重新合成而非传统AR引擎的组成。研究背景在于当前AR技术中组成式合成的局限性，而GAR则通过将环境感知、虚拟内容和交互信号联合编码为生成视频的条件输入，提供了一种新的技术路径。
### Innovation
GAR用一个统一的生成性主体替换传统的多阶段模块化的AR引擎，实现了实时生成增强内容。论文还详细探讨了使实时生成增强内容成为可能的技术基础，并概述了利用其统一推理模型的潜在应用。论文提出了生成型增强现实作为未来AR范式的展望，能够从逼真性、互动性和沉浸性方面提供高品质体验，同时也引发出技术、内容生态系统以及伦理和社会影响等方面的新的研究挑战。
### Conclusion
GAR作为一种未来AR范式，能够在多个方面提供高质量的增强现实体验，但同时也伴随着对技术和内容生态系统，以及伦理和社会影响等方面的新挑战。
## 33. `cs.AI` - 保持预训练知识的同时减轻视觉语言模型中的不宜内容：SafeR-CLIP [PDF](https://arxiv.org/pdf/2511.16743), [HTML](https://arxiv.org/abs/2511.16743)
### Authors
Adeel Yousaf,Joseph Fioresi,James Beetham,Amrit Singh Bedi,Mubarak Shah
### Background
视觉语言模型如CLIP在进行微调以提高安全性时，通常会牺牲泛化性能。这种权衡源于硬性对齐策略，这些策略将不安全的概念强制导向单一的预定义安全目标，破坏了模型学习的语义结构。
### Innovation
提出了一种基于接近度的解决方法：将不安全的概念重定向到其语义上最接近的安全替代品，以最小化表示变化。此外，还提出了SaFeR-CLIP，这是一种平衡安全性和性能的微调框架，并贡献了一个新的基准NSFW-Caps，包含1000个高度对齐的对，用于在分布变化下测试安全性。
### Conclusion
研究表明，尊重预训练表示的几何结构是实现安全性而不牺牲性能的关键。
## 34. `cs.AI` - 重新审视多模态KV缓存压缩：基于频域导向的异常KV感知方法 [PDF](https://arxiv.org/pdf/2511.16786), [HTML](https://arxiv.org/abs/2511.16786)
### Authors
Yaoxin Yang,Peng Ye,Xudong Tan,Chongjun Tu,Maosen Zhao,Jia Hao,Tao Chen
### Background
多模态大型语言模型在推理中面临较大的计算量，因为与视觉输入长度成正比增长的多模态KV缓存导致了显著的计算开销。现有的多模态KV缓存压缩方法大多依赖于注意力得分来降低缓存大小，这使得它们与现有的高效注意力内核（如FlashAttention）不兼容，并且忽略了值向量对注意力输出的贡献。
### Innovation
本文通过频域视角重新审视了多模态KV缓存压缩，提出了一种基于频域指导并考虑异常KV的KV缓存压缩框架FlashCache。该框架包括一个异常KV识别模块，用于在频域中建模多模态KV矩阵的主要成分，并优先保留显著偏离该成分的KV对。此外，还设计了一个动态预算分配模块，可以根据每层适应性地确定KV缓存大小，以保留更多的异常KV。实验结果表明，FlashCache在多个多模态LLM和基准测试中优于现有的多模态KV压缩方法，实现了80%的KV内存使用减少以及1.69倍的解码速度提升，同时保持了任务性能。
### Conclusion
FlashCache通过对频域主要能量的提取和对异常KV的考虑，在多模态KV缓存压缩中提供了一种新的有效方法，显著降低了内存使用并提高了解码速度，而不影响任务性能。
## 35. `cs.AI` - SAM 3: 基于概念的分割anything [PDF](https://arxiv.org/pdf/2511.16719), [HTML](https://arxiv.org/abs/2511.16719)
### Authors
Nicolas Carion,Laura Gustafson,Yuan-Ting Hu,Shoubhik Debnath,Ronghang Hu,Didac Suris,Chaitanya Ryali,Kalyan Vasudev Alwala,Haitham Khedr,Andrew Huang,Jie Lei,Tengyu Ma,Baishan Guo,Arpit Kalla,Markus Marks,Joseph Greer,Meng Wang,Peize Sun,Roman Rädle,Triantafyllos Afouras,Effrosyni Mavroudi,Katherine Xu,Tsung-Han Wu,Yu Zhou,Liliane Momeni,Rishi Hazra,Shuangrui Ding,Sagar Vaze,Francois Porcher,Feng Li,Siyuan Li,Aishwarya Kamath,Ho Kei Cheng,Piotr Dollár,Nikhila Ravi,Kate Saenko,Pengchuan Zhang,Christoph Feichtenhofer
### Background
现有的图像和视频中的概念分割模型存在着局限性，通常依赖于特定的输入形式，如短语提示、图片样例或两者的结合。这些现有的模型尚未实现高性能的多模态概念分割，特别是在准确性和鲁棒性方面存在不足。
### Innovation
作者提出了Segment Anything Model (SAM) 3，它可以基于概念提示对图像和视频中的物体进行检测、分割和跟踪。此外，其创新在于构建了一个可扩展的数据引擎来生成涵盖图像和视频的高质量数据集，并且模型由共享单一骨干网络的图像级检测器和基于记忆的视频跟踪器组成。
### Conclusion
SAM 3在图像和视频概念分割中大幅提高了现有系统的性能，特别是在准确性和对复杂样例的生成上，同时增强了视觉分割任务中的先前SAM能力。作者还开源了SAM 3以及Segment Anything with Concepts（SA-Co）基准，以供进一步的研究和评估使用。
## 36. `cs.AI` - PairHuman：一种用于定制双人生成的高保真摄影数据集 [PDF](https://arxiv.org/pdf/2511.16712), [HTML](https://arxiv.org/abs/2511.16712)
### Authors
Ting Pan,Ye Wang,Peiguang Jing,Rui Ma,Zili Yi,Yu Liu
### Background
个人定制的双人肖像具有显著的应用潜力，例如保存情感记忆和帮助婚礼摄影规划。然而，缺乏基准数据集阻碍了高质量双人肖像生成的追求。现有的数据集不足以满足跨多种场景、服装和互动的高摄影标准，这也限制了定制化质量。
### Innovation
提出了一种名为PairHuman的数据集，这是第一个专门设计用于生成高质量双人肖像的大型基准数据集。PairHuman包含超过100,000张图像，并提供了丰富元数据，如详细的图像描述、人物定位、人体关键点和属性标签。此外，还引入了一种名为DHumanDiff的基线方法，专为双人肖像生成，增强了面部一致性，同时平衡个性化人物生成和语义驱动的场景创造。实验结果表明，该数据集和方法能生成符合人类偏好且具有优异视觉效果的定制化双人肖像。
### Conclusion
PairHuman数据集和DHumanDiff方法生成的高质量双人肖像可更好地满足用户需求，并且数据集已公开提供。
## 37. `cs.AI` - 大型语言模型用于自动化的PRISMA 2020合规性检查 [PDF](https://arxiv.org/pdf/2511.16707), [HTML](https://arxiv.org/abs/2511.16707)
### Authors
Yuki Kataoka,Ryuhei So,Masahiro Banno,Yasushi Tsujimoto,Tomohiro Takayama,Yosuke Yamagishi,Takahiro Tsuge,Norio Yamamoto,Chiaki Suda,Toshi A. Furukawa
### Background
PRISMA 2020准则的遵循评估仍是一项负担，因为缺乏可分享的标准。为此，研究者构建了一个基于Creative Commons许可的108篇系统性回顾的版权意识基准，并评估了十种大型语言模型（LLMs）在五种输入格式下的表现。
### Innovation
研究者开发了一种版权意识基准，包含了108篇采用Creative Commons许可的系统性回顾，并评估了十种大型语言模型在不同输入格式下的准确性。研究发现，提供结构化PRISMA 2020检查列表可以显著提高大型语言模型的准确性，但人类专家的验证在编辑决策前依然是不可或缺的。
### Conclusion
结构化列表提供的形式显著提高了基于大型语言模型的PRISMA评估的准确性，但人类专家验证仍然是不可或缺的。研究选择了高敏感性的Qwen3-Max模型，并将其应用于完整数据集（n=120），达到了95.1%的敏感性和49.3%的特异性。
## 38. `cs.AI` - 对抗非-IID挑战下物联网系统攻击的稳健联邦学习方法 [PDF](https://arxiv.org/pdf/2511.16822), [HTML](https://arxiv.org/abs/2511.16822)
### Authors
Eyad Gad,Zubair Md Fadlullah,Mostafa M. Fouda
### Background
随着用户设备数量的不断增加以及数据量的激增，传统机器学习模型训练面临着巨大的复杂性和挑战，特别是在资源有限和安全性高的物联网（IoT）网络环境中。统计非独立同分布（non-IID）数据在不同参与方之间的广泛存在，进一步加剧了联邦学习（FL）方法的有效性问题。尽管已经提出了一些FL方法来应对统计非独立同分布数据带来的挑战，但在检测IoT攻击方面，现有研究中仍缺乏对这些方法的全面比较。
### Innovation
本文研究了在不同数据分布下的联邦学习算法，特别是FedAvg、FedProx和Scaffold，以深入了解统计非独立同分布数据带来的挑战，并探索这些算法在大规模IoT攻击检测中的性能差异。
### Conclusion
通过细致的分析和实验，本研究揭示了这些FL算法在检测大规模IoT攻击时的性能差异，为研究与实践者提供了宝贵的见解。
## 39. `cs.AI` - Mesh RAG: Retrieval Augmentation for Autoregressive Mesh Generation [PDF](https://arxiv.org/pdf/2511.16807), [HTML](https://arxiv.org/abs/2511.16807)
### Authors
Xiatao Sun,Chen Liang,Qian Wang,Daniel Rakita
### Background
3D meshes are essential in various fields like industrial design, gaming, simulation, and robotics. Traditionally, artists manually create these meshes, which is time-consuming and difficult to scale. While autoregressive models can automate this process, current methods often require larger models or longer sequences, leading to longer generation times and a quality-speed trade-off inherent in their sequential nature. This sequential dependency complicates incremental editing.
### Innovation
提出了一种名为Mesh RAG的新型框架，该框架是一种无需训练、即插即用的自回归网格生成模型。Mesh RAG从RAG语言模型中获得灵感，通过点云分割、空间变换和点云注册来增强生成过程，进而使生成过程解耦，提供高效的并行推理。该方法广泛适用于各种基础的自回归网格生成模型，能够显著提高网格质量，加快生成速度，并支持增量编辑，无需重新训练模型。
### Conclusion
Mesh RAG为自回归网格生成模型提供了一种无需训练、高效并行的增量编辑方法，这在各个基础的自回归网格生成模型中都显示出显著的增益，既提高了质量又加快了生成速度。
## 40. `cs.AI` - 使用序列建模分析心力衰竭患者轨迹 [PDF](https://arxiv.org/pdf/2511.16839), [HTML](https://arxiv.org/abs/2511.16839)
### Authors
Falk Dippela,Yinan Yu,Annika Rosengren,Martin Lindgren,Christina E. Lundberg,Erik Aerts,Martin Adiels,Helen Sjöland
### Background
Transformer架构在电子健康记录（EHR）相关的临床预测任务中定义了最先进的技术水平。尽管Mamba架构在长上下文管理方面优于基于Llama的先进Transformer（Transformer++），但在医疗领域尚未建立起系统化的方法来实证分析模型在不同条件下的性能和效率。因此，对六种序列模型在Swedish心力衰竭队列（42820名患者）中的表现进行了详细研究，提供了临床相关案例研究。这些模型包括三种架构类别（Transformers、Transformers++、Mambas），输入数据包括在院EHR中的诊断、生命体征、实验室检测、药物和程序信息。模型评估了三次一年预测任务的表现：初次心力衰竭住院后的临床不稳定性（再入院表现）、初次心力衰竭住院后的死亡率以及最近一次住院后的死亡率。
### Innovation
这项研究第一个提供了系统的输入标记、模型配置和时间数据预处理的选择设计，并通过系统地分析模型在不同设置下的性能和效率，展示了Llama和Mambas架构的小型配置超越了其他大型<Transformers>。在相同模型规模下，Llama和Mambas使用25%更少的训练数据实现了优越的表现。
### Conclusion
这项研究为基于EHR的临床预测任务未来模型开发提供了推荐的起点，建议从该研究出发进行模型开发。
## 41. `cs.AI` - MRI超分辨率与深度学习：全面综述 [PDF](https://arxiv.org/pdf/2511.16854), [HTML](https://arxiv.org/abs/2511.16854)
### Authors
Mohammad Khateri,Serge Vasylechko,Morteza Ghahremani,Liam Timms,Deniz Kocanaogullari,Simon K. Warfield,Camilo Jaimes,Davood Karimi,Alejandra Sierra,Jussi Tohka,Sila Kurugol,Onur Afacan
### Background
高分辨率（HR）磁共振成像（MRI）对于临床和研究应用至关重要。然而，实现其高分辨率面临技术权衡和技术限制带来的成本问题。超分辨率（SR）提供了一种通过生成HR图像来自低分辨率（LR）扫描的有前景的计算方法，可以在不增加硬件需求的情况下提高诊断准确性和效率。本文综述了近年来MRI超分辨率技术的进展，重点介绍基于深度学习（DL）的方法。
### Innovation
本文提出了一个系统分类来归类基于DL的MRI超分辨率方法，并深入研究了适用于MRI的既有和新兴超分辨率技术。同时还指出了社区需要解决的现有挑战和方向，提供了可访问的资源、工具和教程。
### Conclusion
本文回顾了MRI超分辨率技术的最新进展，并以基于DL的方法为重点，从计算机视觉、计算成像、逆问题和磁共振物理等多个视角进行了分析。未来需要进一步解决临床和研究中的独特挑战，并推进相关技术的发展。
## 42. `cs.AI` - 重访音频语言预训练以学习通用音频表示 [PDF](https://arxiv.org/pdf/2511.16757), [HTML](https://arxiv.org/abs/2511.16757)
### Authors
Wei-Cheng Tseng,Xuanru Zhou,Mingyue Huo,Yiwen Shao,Hao Zhang,Dong Yu
### Background
音频-语言预训练具有通用音频理解的潜力，但与视觉语言模型相比，其研究相对较少。现有的音频-语言模型主要在检索任务中表现出色，但在作为通用编码器的应用方面很少。主要的障碍包括缺乏大规模的音频-文本数据集、不足的注释多样性以及系统性探索和评估的缺乏。
### Innovation
该研究引入了CaptionStew，一个包含多样化的开放源代码音频-文本数据集的10.7M数据集，涵盖多个领域和注释风格。通过该资源，研究对比了语义对比学习和基于描述的学习在语音、音乐和环境声音任务中的音频表征学习表达。实验结果表明，音频语言预训练可以产生具有竞争力的可迁移表示。此外，大规模数据扩展实验揭示了两种学习方法的优势互补：对比学习在小规模数据上具有更好的数据效率，而描述性学习在涉及语言的音频理解任务中表现出更好的可扩展性。
### Conclusion
这些发现为普遍的音频表征提供了音频语言预训练的可行途径，指导未来的研究。为了加速进展，该研究还发布了数据准备食谱、训练协议和预训练模型，为通用音频理解铺平了道路。
## 43. `cs.AI` - 复合漏洞检测的多代理代码验证 [PDF](https://arxiv.org/pdf/2511.16708), [HTML](https://arxiv.org/abs/2511.16708)
### Authors
Shreshth Rajan
### Background
当前，大型语言模型（LLMs）生成的代码存在较多bug，其中29.6%的补丁未正确解决问题，62%的解决方案包含漏洞，且现有的工具只能检测到65%的bug且有35%的误报。鉴于此，研究团队开发了一个名为CodeX-Verify的多代理系统，该系统通过四个专门的代理检测不同类型的bug，并证明了多代理系统的有效性。
### Innovation
该研究提出了CodeX-Verify，一种多代理系统，包含四个专门的代理用于检测不同的bug类型。进一步研究显示，具有不同检测模式的多个代理能够发现比单一代理更多的bug（在寻找不同问题时）。多项试验表明，多个漏洞在同一段代码中相比于传统模型所预测的风险要高出许多（SQL注入加暴露凭证的风险比传统模型预测高出15倍）。在99个已验证标签的代码样本上，该系统能够捕捉到76.1%的bug，速度快且无需执行测试。同时，多代理组合比单一代理提高了39.7个百分点的准确率。在实际应用中，该系统可以在不到200毫秒的时间内处理300个实际补丁，表明其在生产中具有应用价值。
### Conclusion
研究证明了多代理系统在多漏洞识别上的优越性，并且展示了一个适用于实际场景的有效防错工具。随着多代理系统的进一步优化，该成果为企业面对复杂代码环境提供了一个强有力的支持工具。
## 44. `cs.AI` - 使用AI增强生物声学方法确定欧洲龙虾的性别和年龄 [PDF](https://arxiv.org/pdf/2511.16848), [HTML](https://arxiv.org/abs/2511.16848)
### Authors
Feliciano Pedro Francisco Domingos,Isibor Kennedy Ihianle,Omprakash Kaiwartya,Ahmad Lotfi,Nicola Khan,Nicholas Beaudreau,Amaya Albalat,Pedro Machado
### Background
监测水生物种，尤其是像龙虾这样难以捕捉的物种，具有挑战性。Homarus gammarus（欧洲龙虾）是渔业和水产养殖中关键的物种。传统的方法难以准确地了解其栖息地、福利、繁殖、性别和年龄信息。利用非侵入性被动声学监测（PAM）技术，结合人工智能模型，可以有效解决这一问题。
### Innovation
研究人员首次使用Deep Learning（1D-CNN，1D-DCNN）和Machine Learning（SVM，k-NN，Naive Bayes，Random Forest，XGBoost，MLP）模型分析欧洲龙虾的生物声学特征（如嗡鸣/头壳振动），成功地通过生物声学信号对其年龄（幼年/成年）和性别（雄性/雌性）进行分类。结果表明，这些模型在分类准确率上具有明显优势，为进一步的龙虾保护、检测和管理提供了新的可能性。
### Conclusion
这项研究开发了一种非侵入性的PAM技术，通过AI增强的生物声学方法，能够准确地确定欧洲龙虾的性别和年龄。这种方法具有广阔的应用前景，特别是在水下生物的监测和管理中，尤其是在水产养殖和渔业领域。未来的研究可以进一步优化模型和参数，提高分类效果。
## 45. `cs.AI` - ConCISE: 一个基于LLM生成答案的无需参考材料的简洁性评估度量 [PDF](https://arxiv.org/pdf/2511.16846), [HTML](https://arxiv.org/abs/2511.16846)
### Authors
Seyed Mohssen Ghafari,Ronny Kol,Juan C. Quiroz,Nella Luan,Monika Patial,Chanaka Rupasinghe,Herman Wandabwa,Luiz Pizzato
### Background
大型语言模型（LLMs）经常生成冗长且冗余的回答，这降低了清晰度和用户满意度，并增加了对LLM进行评价的模型开发成本，尤其是在按输出token数收费的知名专有模型中。
### Innovation
本文提出了一种无需参考材料的新颖的度量方法，用于评估LLM生成回答的简洁性，该方法不含金标准参考材料就能量化非必要内容，通过对原始回答与LLM摘要的压缩比进行平均计算，包括抽象性摘要压缩比、抽取性摘要压缩比和单词删除压缩比。
### Conclusion
实验结果表明，提出的度量方法可以识别LLM输出中的冗余性，提供了一种无需真相人工注释即可自动化评估会话AI系统回复简洁度的实用工具。
## 46. `cs.AI` - MOCET评分 [PDF](https://arxiv.org/pdf/2511.16823), [HTML](https://arxiv.org/abs/2511.16823)
### Authors
Joseph Kim,Saahith Potluri
### Background
评估和测量人工智能安全水平（ASL）威胁对于引导相关利益方实施保持风险在可接受范围内的防护措施至关重要。ASL-3+模型在提升非国家行为者（尤其是生物安全领域）的能力方面存在独特风险。现有的评估指标，如LAB-Bench、BioLP-bench和WMDP，能够可靠地评估模型的提升和领域知识，但需要更好地描述“现实风险”的指标来为大规模语言模型（LLM）的安全性提供信息，并且需要可扩展且开放的指标以跟上其快速的进步。
### Innovation
我们引入了MOCET，这是一种可解释且双可扩展的指标（自动化和开放性），可以量化现实风险。
### Conclusion
为了填补现有评估指标在描述现实风险和应对LLM快速发展方面的不足，我们提出了MOCET这一新的评估方法，以更好地为LLM的安全性提供信息，并适应其迅速的进步。
## 47. `cs.AI` - ManifoldFormer: 在黎曼流形上的几何深度学习用于神经动力学 [PDF](https://arxiv.org/pdf/2511.16828), [HTML](https://arxiv.org/abs/2511.16828)
### Authors
Yihang Fu,Lifang He,Qingyu Chen
### Background
现有的EEG基础模型将神经信号视为欧几里得空间中的通用时序序列，忽略了神经动态的固有几何结构，这种结构将脑活动限制在低维流形上。这种模型假设与神经几何之间的根本不符限制了表示质量和跨被试的一般性。
### Innovation
ManifoldFormer 通过一个新颖的几何深度学习框架解决了这一限制，该框架明确学习神经流形表示。该架构集成了三个关键创新：用于流形嵌入的黎曼VAE，能够保留几何结构；带有测地线感知注意力机制的几何Transformer，可以直接在神经流形上操作；以及利用神经ODE的动力学预测器，实现流形约束下的时空演化。
### Conclusion
广泛的评估结果表明，ManifoldFormer 在四个公开数据集上显著优于现有最先进的方法，准确率高出4.6-4.8%，科恩κ值高出6.2-10.2%，同时保持了良好的跨被试泛化能力。几何方法揭示了与神经生理原则一致的有意义的神经模式，证明了几何约束对于有效EEG基础模型的重要性。
## 48. `cs.AI` - 在帕金森病检测中使用语音生物标志物：经典机器学习模型的稳健统计性能比较 [PDF](https://arxiv.org/pdf/2511.16856), [HTML](https://arxiv.org/abs/2511.16856)
### Authors
Katia Pires Nascimento do Sacramento,Elliot Q. C. Garcia,Nicéias Silva Vilela,Vinicius P. Sacramento,Tiago A. E. Ferreira
### Background
帕金森病是一种逐渐进行的神经退行性疾病，除了直接影响功能性移动能力外，还常常伴随着如低音量和构音障碍等语音障碍，这些障碍通常在疾病的早期出现。在临床环境中，利用语音生物标志物来支持帕金森病的早期诊断提供了一种非侵入性、低成本且易于访问的替代方法。
### Innovation
该文使用深度神经网络（DNN）对来自两个公开可用的语音数据集的帕金森病患者和健康对照的语音生物标志物进行有效区分，评估了DNN的性能，与传统的机器学习方法相比，DNN展现了更高的准确性和效率，尤其是对意大利语音数据集和帕金森远程监测数据集分别达到了98.65%和92.11%的平均准确率。
### Conclusion
总体而言，该研究证实了DNNs的有效性和包容性，强调了它们在利用基于语音的生物标志物早期检测神经退行性疾病方面的潜力，从而提高疾病的诊断准确性和可靠性。
## 49. `cs.AI` - PepEVOLVE：基于组相对优势的意识位置动态肽优化 [PDF](https://arxiv.org/pdf/2511.16912), [HTML](https://arxiv.org/abs/2511.16912)
### Authors
Trieu Nguyen,Hao-Wei Pang,Shasha Feng
### Background
宏环肽作为一种结合生物类似物亲和力和小分子类似物开发性的新兴药理学领域，具有广泛的组合空间和多参数目标，这使得先导优化过程缓慢且具有挑战性。先前的生成方法如PepINVENT要求化学家预先指定可优化的位置，但这些位置并非总是事先知晓的，并依赖于静态预训练和优化算法，这限制了模型的泛化能力和有效优化肽序列的能力。
### Innovation
PepEVOLVE引入了一种位置感知的动态框架，该框架能够学习在哪里进行编辑以及如何动态优化肽以提升多目标性能。具体创新点包括：（i）通过动态掩蔽和CHUCKLES移动增强预训练，提高泛化能力；（ii）使用上下文无关的多臂老虎机路由器，发现高回报的氨基酸；（iii）结合一种新颖的进化的优化算法与组相对优势，稳定强化学习更新。
### Conclusion
在体内外评估中，路由器策略能够学会并集中在化学上具有意义且影响肽特性的位置。在具有治疗意义的逆转录酶结合宏环基准中，PepEVOLVE优于PepINVENT，达到了更高的平均得分（约0.8 vs. 0.6），实现了最高候选物得分为0.95（对比0.87），并且在优化渗透性和脂溶性的同时，结构约束下更快地收敛。总体而言，PepEVOLVE为在最优编辑位点未知的情况下提供了一条可实际操作、可重复的肽先导优化路径，有助于更高效地探索并提高多重目标设计的质量。
## 50. `cs.AI` - OmniGround: 一种用于真实复杂场景的全面时空定位基准 [PDF](https://arxiv.org/pdf/2511.16937), [HTML](https://arxiv.org/abs/2511.16937)
### Authors
Hong Gao,Jingyu Wu,Xiangkai Xu,Kangni Xie,Yunchen Zhang,Bin Zhong,Xurui Gao,Min-Ling Zhang
### Background
尽管目前多模态大型语言模型取得了显著进展，但在现实世界中，目标物体多样且查询复杂的情况下，模型仍然存在类别偏差、简化推理和语言鲁棒性差的问题。这主要是由于现有基准的范围有限，导致模型不能很好地应对多样化的物体和复杂的查询。
### Innovation
作者提出了一个名为OmniGround的基准，包括3,475个视频，涵盖了81个类别和复杂的现实查询。该基准结合了多方向追踪和智能错误校正的向前-向后-精修注释流程来生成高质量的标签。此外，还提出了一个系统性的评估框架DeepSTG，从四个互补维度全面评估数据集质量，而非仅仅依赖表面统计。PG-TAF是一种无需训练的两阶段框架，将STVG分解为高层时间定位和精细的时空传播。实验结果显示，PG-TAF在OmniGround的数据集上实现了25.6%和35.6%的平均tIoU和vIoU提升，并且在四个基准上均保持了一致的提升。
### Conclusion
评估发现，在复杂的真实场景下，特别是在小/被遮挡的对象以及复杂的空间关系上，性能平均下降了10.4%。因此，作者提出了PG-TAF框架，该框架在OmniGround及其他四个基准上分别实现了25.6%和35.6%的m_tIoU和m_vIoU改进，克服了传统方法的局限性。
## 51. `cs.AI` - WorldGen：从文本生成可探索和互动的3D世界 [PDF](https://arxiv.org/pdf/2511.16825), [HTML](https://arxiv.org/abs/2511.16825)
### Authors
Dilin Wang,Hyunyoung Jung,Tom Monnier,Kihyuk Sohn,Chuhang Zou,Xiaoyu Xiang,Yu-Ying Yeh,Di Liu,Zixuan Huang,Thu Nguyen-Phuoc,Yuchen Fan,Sergiu Oprea,Ziyan Wang,Roman Shapovalov,Nikolaos Sarafianos,Thibault Groueix,Antoine Toisoul,Prithviraj Dhar,Xiao Chu,Minghao Chen,Geon Yeong Park,Mahima Gupta,Yassir Azziz,Rakesh Ranjan,Andrea Vedaldi
### Background
本文介绍了WorldGen系统，该系统能够直接从文本提示自动生成大规模、互动的3D世界。该方法将自然语言描述转化为可导航的、完全纹理化的环境，这些环境可以在标准游戏引擎中即时探索或编辑。WorldGen通过LLM驱动的场景布局推理、程序生成、基于扩散的3D生成以及对象感知的场景分解，将创作意图与功能性虚拟空间联系起来，使创作者能够设计连贯、可导航的世界，无需手动建模或专门的3D专业知识。系统具有完全模块化的特点，支持对布局、比例和风格的精细控制，生成的3D世界具有几何一致性、视觉丰富性和实时渲染效率。
### Innovation
WorldGen系统通过结合LLM驱动的场景布局推理、程序生成、基于扩散的3D生成以及对象感知的场景分解，能够从文本描述直接生成大型、可导航的3D世界。该系统支持对布局、比例和风格的精细控制，生成的3D世界具有几何一致性、视觉丰富性和实时渲染效率。这对于3D生成AI在游戏、模拟和沉浸式社交环境中的应用是一个有意义的进步。
### Conclusion
本文展示了在大规模、生成式世界构建中的一个进步，通过3D生成AI技术的进一步改进，使得世界建造变得更加容易和高效。这代表了3D生成AI技术在游戏、模拟和沉浸式社交环境中应用的一个重要前沿。
## 52. `cs.AI` - 生成式人工智能在社会学研究中的应用：学科现状 [PDF](https://arxiv.org/pdf/2511.16884), [HTML](https://arxiv.org/abs/2511.16884)
### Authors
AJ Alvero,Dustin S. Stoltz,Oscar Stuhler,Marshall Taylor
### Background
生成式人工智能（GenAI）因其在研究和学术领域中的潜力应用引起了广泛的关注，甚至吸引了原本不依赖计算工具的人士。然而，早期评论者也表达了对GenAI使用的巨大环境成本、严重的社会风险以及生成低质量内容的趋势的担忧。在此背景下，本研究聚焦于社会学研究领域，旨在通过调查近五年来发表在50本社会学杂志上的433篇文章的作者，评估和量化GenAI在学科中的实际应用情况。
### Innovation
本研究通过针对社会学领域的调查，提供了一个关于GenAI在学术界实际应用的全面概述。它探讨了学者们使用GenAI的频率、原因以及他们对这项技术的担忧、信任度和乐观态度。研究发现，尽管Trener和专家经验差异不大，但大部分学者对GenAI的输出持低信任度，并对GenAI对社会和环境的影响充满担忧。
### Conclusion
总的来说，受访者对于GenAI的社会和环境后果非常担忧，无论其专业知识或使用频率如何，对GenAI输出的信任度都很低。尽管人们普遍认为GenAI将会有所改进，但学者们对GenAI是否会对领域产生积极影响存在分歧。
## 53. `cs.AI` - 基于RAG的数据质量治理方法：适用于企业ERP系统的增强 [PDF](https://arxiv.org/pdf/2511.16700), [HTML](https://arxiv.org/abs/2511.16700)
### Authors
Sedat Bin Vedat,Enes Kutay Yarkan,Meftun Akarsu,Recep Kaan Karaman,Arda Sar,Çağrı Çelikbilek,Savaş Saygılı
### Background
企业在人力资源部门进行跨多语言的手动记录输入时，处理成千上万员工记录的ERP系统面临严重的数据质量问题。现有系统需要通过手动输入进行数据处理，导致数据质量低、准确度差等问题。
### Innovation
本文提出了一种端到端的数据处理管道，结合了自动数据清洗和LLM（大型语言模型）驱动的SQL查询生成。该系统包括两个集成阶段：一个需要周期性同步的多阶段清洗管道，用于翻译标准化、拼写修正和实体去重；另一个使用GPT-4o增强的检索增强生成框架，可将土耳其语、俄语和英语的自然语言问题翻译成验证过的SQL查询。该框架通过LangChain编排、FAISS矢量相似度搜索和少量示例学习，提高了查询生成的准确性和效率。
### Conclusion
此系统在生产系统中的表现表明，语言模型生成的查询有效率为92.5%，模式遵从性为95.1%，语义准确率为90.7%，并且在此过程中查询处理时间从2.3天缩短到不到5秒，同时保持了99.2%的正常运行时间，与GPT-3.5相比，GPT-4o的延迟降低了46%，成本降低了68%。该模块化架构为AI原生企业的数据治理提供了一个可重复框架，展示了在企业规模上具有实际可行性，用户满意度为4.3/5.0。
## 54. `cs.AI` - 更精细更好：面向粒度感知的开放式域泛化 [PDF](https://arxiv.org/pdf/2511.16979), [HTML](https://arxiv.org/abs/2511.16979)
### Authors
Yunyun Wang,Zheng Duan,Xinyue Liao,Ke-Jia Chen,Songcan Chen
### Background
OSDG 旨在解决部署模型在遇到已知类别间的域移和新类别时的现实场景。尽管视觉-语言模型如 CLIP 取得了显著进展，但现有方法仍然在已知类别风险和未知类别开放空间风险之间陷入困境，尤其是当区分与已知类别在细粒度视觉相似性上极为接近的“硬未知者”时，模型容易过于自信。
### Innovation
该文提出了 Semantic-enhanced CLIP (SeeCLIP) 框架，通过细粒度语义增强明确解决了这一困境。主要包括：1) 引入语义意识提示增强模块分解图像为 discriminative 语义令牌，进行超越粗粒度类别标签的精细视觉-语言对齐；2) 采用双重对比学习策略，分别通过排斥和吸引目标有效定位未知提示；3) 通过语义导向扩散模块生成伪未知样本，生成与已知类别视觉相似但具有关键局部差异的挑战性样本，迫使模型学习更精细的决策边界。
### Conclusion
在五个基准测试中的广泛实验表明，SeeCLIP 在准确性和 H-score 上分别比最先进的方法提高了 3% 和 5%。
## 55. `cs.AI` - FLUID：无需训练的人脸识别去标识化通过潜在空间身份置换 [PDF](https://arxiv.org/pdf/2511.17005), [HTML](https://arxiv.org/abs/2511.17005)
### Authors
Jinhyeong Park,Shaheryar Muhammad,Seangmin Lee,Jong Taek Lee,Soon Ki Jung
### Background
该研究背景聚焦于如何在无需训练的情况下对预训练的扩散模型（diffusion models）进行身份编辑（identity editing），以实现人脸去标识化（face de-identification）。研究利用化学中的置换机制进行重新解释，尝试在预训练的无条件扩散模型的潜在空间（latent h-space）中进行身份编辑（semantic displacement），以优化身份抑制与属性保留之间的平衡。
### Innovation
该研究提出了一个名为FLUID的框架，该框架能够直接在预训练扩散模型的潜在空间中替换身份，而无需额外训练。创新点包括：1) 通过优化指导下的新型试剂损失（reagent losses）来发现身份编辑方向，以确保属性保留并抑制身份特征；2) 提出了线性和测地线（tangent-based）编辑方案，以有效地导航潜在流形（latent manifold）。实验结果表明FLUID在身份抑制和属性保留之间取得优越的平衡，相比现有最先进的人脸去标识化方法，在定性和定量评估上均表现出优胜。
### Conclusion
在CelebA-HQ和FFHQ数据集上的实验结果证明，FLUID在身份抑制和属性保留之间的平衡达到优越效果，并在定性和定量评估中均超越了现有的最先进去标识化方法。
## 56. `cs.AI` - 深度改进监督 [PDF](https://arxiv.org/pdf/2511.16886), [HTML](https://arxiv.org/abs/2511.16886)
### Authors
Arip Asadulaev,Rayan Banerjee,Fakhri Karray,Martin Takac
### Background
最近的研究表明，小型的循环架构，如 Tiny Recursive Models (TRMs)，在复杂的推理任务中，如 Abstraction and Reasoning Corpus (ARC)，可以超越大型语言模型 (LLMs) 的表现。这项工作旨在进一步探讨如何在最小改动的情况下提高这些方法的效率。
### Innovation
作者将 TRMs 的潜在推理过程重新定义为一种 classifier-free guidance 和隐式策略改进算法的形式，进而提出了一种新的训练方案，为每次训练中的每个循环提供目标。这种方法显著提高了训练效率，减少了总向前传递次数达 18 倍，并消除了终止机制，同时保持了与标准 TRMs 相当的质量。
### Conclusion
通过这种方法，作者在仅使用 0.8M 参数的情况下，取得了 ARC-1 试题 24% 的准确率，超越了大多数 LLMs。
## 57. `cs.AI` - 使用基于LLM的多代理系统优化PyTorch推理 [PDF](https://arxiv.org/pdf/2511.16964), [HTML](https://arxiv.org/abs/2511.16964)
### Authors
Kirill Nagaitsev,Luka Grbcic,Samuel Williams,Costin Iancu
### Background
现代AI推理系统对于在可用的GPU硬件上最大化性能是一个持续的挑战。传统的做法包括编写自定义的GPU内核和使用专门的模型编译器来针对特定的GPU目标调优高级代码。最近的研究表明，基于LLM的多代理系统可以有效地执行这样的调优，通常优于现有的编译器，并且消除了手动内核开发的需要。然而，用于此任务的多代理系统的行为动态尚未得到探索。
### Innovation
本文提出了一个逻辑框架来比较多代理PyTorch优化系统。评估表明，利用密集策略与其他纠错代理配对时表现最佳，且性能与优化步骤的粒度密切相关。最佳实现针对KernelBench中的多种PyTorch机器学习架构实现了平均2.88倍的加速。
### Conclusion
该研究展示了基于LLM的多代理系统在PyTorch推理优化中的潜力，并发现利用特定策略可以显著提高性能。
## 58. `cs.AI` - 参数自由的神经镜头模糊渲染以实现高保真合成 [PDF](https://arxiv.org/pdf/2511.17014), [HTML](https://arxiv.org/abs/2511.17014)
### Authors
Lingyan Ruan,Bin Chen,Taehyun Rhee
### Background
一致且自然的相机镜头模糊对于无缝融合3D虚拟对象到拍摄的现实场景中至关重要。由于镜头模糊通常与场景深度相关，虚拟对象的放置及其相应的模糊程度对混合现实作品的视觉保真度有很大影响。现有流水线通常依赖于相机参数（如焦距、对焦距离、光圈大小）和场景深度来计算视差圈（CoC，Circle of Confusion）以实现真实的镜头模糊渲染。然而，这些信息往往对普通用户不可得，限制了这些方法的易用性和普遍性。
### Innovation
本文提出了一种新颖的合成方法，直接从RGB图像中估计CoC图，无需使用场景深度或相机元数据。通过虚拟对象的标称CoC图与其深度之间的一线性关系，来推测CoC值，并使用神经网络重新模糊来渲染真实的镜头模糊。该方法为实际应用提供了灵活且实用的解决方案。
### Conclusion
实验结果表明，本文的方法实现了高保真合成，并具有真实的虚化效果，在定性和定量评估中均优于现有的先进技术。
## 59. `cs.AI` - 使用有监督微调的大语言模型为特定领域的知识图构建：湖南历史名人的案例研究 [PDF](https://arxiv.org/pdf/2511.17012), [HTML](https://arxiv.org/abs/2511.17012)
### Authors
Junjie Hao,Chun Wang,Ying Qiao,Qiuyue Zuo,Qiya Song,Hua Ma,Xieping Gao
### Background
大语言模型和知识图谱在历史文化的先进研究方面具有很强的潜力，可以通过支持文化遗产信息的提取、分析和解释。湖南省被湖湘文化影响的历史名人这一案例研究表明，预训练的大模型可以帮助研究人员高效地从文本来源中提取关键信息，包括传主属性、生活事件和社会关系，并构建结构化知识图谱。然而，湖南省历史名人的系统数据资源仍然有限，通用模型在低资源环境下的领域知识提取和结构化输出生成中表现不佳。
### Innovation
研究提出了一种监督微调方法以增强领域特定信息提取。首先，设计了一个针对湖南历史名人的细粒度、架构指导指令模板，并构建了一个指令微调数据集，以缓解缺乏领域特定训练语料库的问题。其次，应用参数高效指令微调到四个公开的大型语言模型 - Qwen2.5-7B、Qwen3-8B、DeepSeek-R1-Distill-Qwen-7B和Llama-3.1-8B-Instruct，并开发了评估它们提取性能的评价标准。实验结果显示，所有模型在微调后都表现出显著的性能提升。其中，Qwen3-8B 的表现最佳，得分为89.3866。
### Conclusion
这项研究为地区历史文化领域的垂直大语言模型微调提供了新的见解，并突出了它们在文化遗产知识提取和知识图谱构建中的潜在低成本应用。
## 60. `cs.AI` - MedImageInsight在胸腔健康分类中的胸部X射线应用 [PDF](https://arxiv.org/pdf/2511.17043), [HTML](https://arxiv.org/abs/2511.17043)
### Authors
Rama Krishna Boya,Mohan Kireeti Magalanadu,Azaruddin Palavalli,Rupa Ganesh Tekuri,Amrit Pattanayak,Prasanthi Enuga,Vignesh Esakki Muthu,Vivek Aditya Boya
### Background
胸部X射线仍然是胸部诊断中最常用成像技术之一，然而，不断增加的成像需求和放射科医生的工作负担使得及时解读变得具有挑战性。
### Innovation
本文研究了使用MedImageInsight（一种医疗成像基础模型）进行胸部X射线自动二分类的方法，分类结果分为正常和异常两类。研究了两种方法：一种是针对最终端分类进行微调，另一种是将模型作为特征提取器用于传统的机器学习分类管道。实验使用了ChestX-ray14数据集和合作伙伴医院的临床数据进行验证。
### Conclusion
微调后的分类器在性能上达到了0.888的ROC-AUC，其校准效果优于迁移学习模型，表明基础医疗成像模型不仅能减少任务特定的训练需求，还能保持诊断可靠性。系统设计用于集成到基于网络和医院PACS的流程中，以支持初步诊断和减轻放射科医生的工作负担。未来的研究将扩展该模型至多标签病理分类，以提供临床环境下的初步诊断解释。
## 61. `cs.AI` - RacketVision: 多拍拍球运动统一球与拍子分析基准 [PDF](https://arxiv.org/pdf/2511.17045), [HTML](https://arxiv.org/abs/2511.17045)
### Authors
Linfeng Dong,Yuchen Yang,Hao Wu,Wei Wang,Yuenan HouZhihang Zhong,Xiao Sun
### Background
体育分析中的计算机视觉研究目前缺乏专门的大型数据集，特别是针对乒乓球、网球和羽毛球等多种拍子运动的精细标记数据。现有的数据集主要关注球的位置，而忽略了拍子的动态信息，这限制了对人类与物体之间复杂互动的研究。RacketVision旨在填补这一空白，通过提供包括拍子姿态在内的大规模精细标注数据，促进这些领域的研究。
### Innovation
RacketVision是首个同时提供拍子姿态和传统球位置的大规模精细标注数据集，能够推动复杂的人与物交互研究。它针对三个主要任务进行了设计：细粒度的球跟踪、姿态估计和预测轨迹预报。研究发现，虽然简单地将拍子姿态特征合并会降低性能，但交叉注意力机制是解锁这些特征价值的关键，能够超越单一模态的强基准模型。
### Conclusion
RacketVision为动态物体跟踪、基于条件的运动预测以及体育多模态分析提供了灵活的资源和强大的起点，推动了未来的研究。
## 62. `cs.AI` - 为什么语言模型代理要充当吹哨人？ [PDF](https://arxiv.org/pdf/2511.17085), [HTML](https://arxiv.org/abs/2511.17085)
### Authors
Kushal Agrawal,Frank Xiao,Guido Bergman,Asa Cooper Stickland
### Background
大型语言模型（LLMs）作为工具使用的代理，使其对齐训练以新的方式表现出来。研究发现，语言模型能够以违背用户利益或明确指令的方式使用工具。本文探讨了一种新的行为模式——LLM吹哨：模型在没有用户指令或知情的情况下，向对话边界之外的实体（如监管机构）披露疑似不当行为。通过引入多样性和现实性的阶段性的不当行为场景，评估模型的这一行为。
### Innovation
作者引入了一套多样且现实的阶段性的不当行为场景，用以评估模型披露（吹哨）不当行为的倾向。研究发现：模型吹哨行为的频率在不同模型家族之间差异显著；增加任务复杂度可以降低吹哨倾向；通过系统提示引导模型朝着道德行为方向行动可以大幅提升吹哨率；提供更多的工具和详细的流程化工作路径则会使模型减少吹哨行为。另外，验证了数据集的鲁棒性，发现评价无意识在黑色盒方法和模型激活探针的测试中表现较低。
### Conclusion
研究揭示了LLM吹哨行为与模型类型、任务复杂性、道德引导机制及可用工具数量等多种因素之间的关系，强调了在设计和部署LLM时需要综合考量这些因素以优化系统的行为表现。
## 63. `cs.AI` - RASTP: Representation-Aware Semantic Token Pruning for Generative Recommendation with Semantic Identifiers [PDF](https://arxiv.org/pdf/2511.16943), [HTML](https://arxiv.org/abs/2511.16943)
### Authors
Tianyu Zhan,Kairui Fu,Zheqi Lv,Shengyu Zhang
### Background
生成推荐系统通常利用语义标识符（SIDs）来表示每个项目，这是一种通过序列编码表示项目语义信息的方法。然而，使用多个SIDs来表示项目ID会显著增加输入序列的长度，从而导致计算复杂度和内存消耗增加。尽管现有方法主要集中于优化注意力计算和KV缓存，但本文提出了RASTP（Representation-Aware Semantic Token Pruning），直接剪枝输入序列中的低信息量或无关语义标记。
### Innovation
RASTP通过结合通过表示大小测量的语义显著性和从累积注意力权重中得到的关注度中心性来评估标记的重要性，并且动态剪枝低信息量或无关的语义标记。实验结果表明，RASTP在三个真实的亚马逊数据集上可以将训练时间减少26.7%，同时保持或轻微提升推荐性能。
### Conclusion
实验结果展示了RASTP的有效性，并已开发开源代码供进一步研究使用。
## 64. `cs.AI` - AutoGraphAD: 使用变分图自编码器的新方法进行异常网络流检测 [PDF](https://arxiv.org/pdf/2511.17113), [HTML](https://arxiv.org/abs/2511.17113)
### Authors
Georgios Anyfantis,Pere Barlet-Ros
### Background
网络入侵检测系统（NIDS）是检测网络攻击和入侵的重要工具。尽管监督机器学习方法已被广泛研究用于攻击检测和特征化，但这些方法依赖于准确标注的数据集，而获得这些数据集非常昂贵。现有的公共数据集包含的攻击行为有限且过时，许多数据集还存在标记错误的问题。为减少对标注数据的依赖，本文提出了一种名为AutoGraphAD的新型无监督异常检测方法，基于异质变分图自编码器。AutoGraphAD利用连接和IP节点构建异质图，捕捉一段时间内的网络活动。该模型采用无监督和对比学习进行训练，无需任何标注数据。重建损失、结构损失和KL散度被加权结合成异常评分，用于异常检测。
### Innovation
提出了基于异质变分图自编码器的无监督异常检测方法AutoGraphAD，无需任何标注数据。该方法的重建损失、结构损失和KL散度结合成异常评分，用于异常检测。整体来看，AutoGraphAD在无监督方法中的表现与之前的方法相当，甚至更好，且不需要昂贵的下游异常检测器。此外，该方法的训练速度和推断速度分别快了约1.18和1.03个数量级，显著提高了操作部署的优势。
### Conclusion
AutoGraphAD在不需要任何标注的情况下取得了与现有无监督方法相同甚至更好的检测结果，同时在训练和推断速度上表现出色，这使得它更适合实际部署。
## 65. `cs.AI` - 基于生成树自动回归的视觉生成 [PDF](https://arxiv.org/pdf/2511.17089), [HTML](https://arxiv.org/abs/2511.17089)
### Authors
Sangkyu Lee,Changho Lee,Janghoon Han,Hosung Song,Tackgeun You,Hwasup Lim,Stanley Jungkyu Choi,Honglak Lee,Youngjae Yu
### Background
在视觉生成领域，现有的方法通常限制了序列顺序的选择灵活性，或者在引入双向上下文时性能下降。传统的自回归模型在处理图像编辑时，无法充分利用图像先验知识如中心偏向和局部性来保持采样性能。
### Innovation
提出了生成树自回归（STAR）建模方法，它能够利用图像的先验知识（如中心偏向和局部性），维持采样性能的同时，还能提供足够的序列顺序灵活性以适应图像编辑。STAR通过在由图像块位置定义的网格中抽样均匀生成树来获取遍历顺序，并通过广度优先搜索来优化生成树的序，从而在拒绝采样过程中确保图像的部分观察连接成前缀。这种针对性且结构化的随机策略，允许STA保留后缀完成的能力，同时保持采样性能。
### Conclusion
STAR方法通过利用图像的先验知识和结构化的遍历策略，在保持自回归模型的灵活性和采样性能的同时，实现了双向上下文的有效整合。
## 66. `cs.AI` - 在全栈AMD平台上训练基础模型：计算、网络和系统设计 [PDF](https://arxiv.org/pdf/2511.17127), [HTML](https://arxiv.org/abs/2511.17127)
### Authors
Quentin Anthony,Yury Tokpanov,Skyler Szot,Srivatsan Rajagopal,Praneeth Medepalli,Rishi Iyer,Vasu Shyam,Anna Golubeva,Ansh Chaurasia,Xiao Yang,Tomas Figliolia,Robert Washbourne,Drew Thorstensen,Amartey Pearson,Zack Grossbart,Jason van Patten,Emad Barsoum,Zhenyu Gu,Yao Fu,Beren Millidge
### Background
本文介绍了在纯AMD硬件上进行大规模专家混合（MoE）预训练的第一项研究，使用了MI300X GPU和Pollara互连。通过对系统和模型设计提供实用指导，文章从系统和模型两个方面进行了深入探索。
### Innovation
研究提供了详细的集群和网络特性，包括所有核心集体操作（all-reduce，reduce-scatter，all-gather，broadcast）的微基准测试结果。首次针对如此大规模的研究提供了MI300X的微基准测试结果，用于模型设计。还提出了与MI300X相关的变压器大小规则，优化了训练吞吐量和推理延迟，并阐述了训练堆栈，包括容错和检查点重塑等常被忽略的实用工具。
### Conclusion
ZAYA1基模型在性能上与现有的顶级基础模型相当，甚至在推理、数学和编码基准测试中超越了某些模型。这些结果表明，AMD硬件、网络和软件栈已经成熟且优化到可以进行竞争力的大型预训练的状态。
## 67. `cs.AI` - ReBrain: 从稀疏CT横截面重建脑MRI的检索增强扩散 [PDF](https://arxiv.org/pdf/2511.17068), [HTML](https://arxiv.org/abs/2511.17068)
### Authors
Junming Liu,Yifei Sun,Weihua Cheng,Yujin Kang,Yirong Chen,Ding Wang,Guosun Zeng
### Background
磁共振成像（MRI）在脑疾病诊断中起着关键作用，但由于某些患者因身体或临床限制无法使用，因此在某些情况下并不总是可行的。近年来的研究试图从计算机断层扫描（CT）扫描中合成MRI。然而，低剂量协议常导致CT体积稀疏且通过面分辨率差，这使得准确重建整个脑部MRI体积尤为困难。
### Innovation
我们提出了一种名为ReBrain的检索增强扩散框架，用于脑部MRI重建。利用布朗桥梁扩散模型（BBDM）从任何3D CT扫描中合成MRI横截面。同时，通过微调的检索模型从全面的先验数据库中检索结构和病理相似的CT横截面作为参考，这些参考通过ControlNet分支指导中间MRI横截面的生成，确保结构连续性。此外，还考虑了数据库中缺乏适合参考时的罕见检索失败，应用球形线性插值来提供补充指导。
### Conclusion
在SynthRAD2023和BraTS上的广泛实验表明，ReBrain在稀疏条件下的跨模态重建中达到了最先进的性能。
## 68. `cs.AI` - UI-CUBE：超越任务准确性的企业级计算机使用代理评估，以实现操作可靠性 [PDF](https://arxiv.org/pdf/2511.17131), [HTML](https://arxiv.org/abs/2511.17131)
### Authors
Horia Cristescu,Charles Park,Trong Canh Nguyen,Sergiu Talmacel,Alexandru-Gabriel Ilie,Stefan Adam
### Background
当前的计算机使用代理（CUA）基准测试虽然有效测量了任务完成情况，但缺乏对企业部署准备度的评估，过度重视功能正确性而忽视了生产系统所需的运行可靠性。
### Innovation
UI-CUBE（UiPath计算机使用基准）是一个系统化的基准测试，包括226个任务分为两个难度级别，以暴露当前CUAs的基本架构局限。该测试涵盖了简单的UI交互、复杂的流程和企业应用程序场景，采用系统界面变化覆盖、多分辨率测试及应用程序状态下的任务成功自动化验证。评估结果显示，现有最先进的模型在简单UI交互和复杂流程方面显示出显著能力差异而非渐进性能下降。
### Conclusion
UI-CUBE作为企业准备度诊断工具，揭示了当前CUAs虽然能够操作单一界面元素，但无法作为可靠的自动化流程工具。研究结果提供了对开发能够管理复杂多步骤企业过程的生产就绪CUA的重要架构见解。
## 69. `cs.AI` - CLLMRec: LLM驱动的认知感知概念推荐系统通过语义对齐和先决知识精简 [PDF](https://arxiv.org/pdf/2511.17041), [HTML](https://arxiv.org/abs/2511.17041)
### Authors
Xiangrui Xiong,Yichuan Lu,Zifei Pan,Chang Sun
### Background
大规模开放在线课程（MOOCs）的增长对个性化学习提出了重大挑战，其中概念推荐至关重要。现有方法通常依赖异构信息网络或知识图谱来捕捉概念关系，并结合知识追踪模型评估学习者的认知状态。但是，这些方法因其对高质量结构化知识图谱的依赖而在现实世界的教育场景中面临局限性，后者往往稀缺。
### Innovation
本文提出了CLLMRec，一种新型框架，利用大型语言模型（LLM）通过两个协同技术支柱：语义对齐和先决知识精简。语义对齐构建了一个统一的表示空间，通过编码学习者和概念的非结构化文本描述。先决知识精简 paradigm 采用教师-学生架构，其中大型教师LLM（作为Prior Knowledge Aware Component实现）从其内化的世界知识中提取概念间先决知识关系并将其提炼为软标签，用于训练高效的学生排名器。该框架还整合了深度知识追踪机制，通过建模学习者实时的认知状态，确保推荐系统结构合理且认知上恰当。
### Conclusion
在两个实际MOOC数据集上的广泛实验表明，CLLMRec在多个评估指标上显著优于现有基准方法，验证了其在生成真正认知感知和个人化概念推荐方面的有效性，无需依赖显式的结构先验。
## 70. `cs.AI` - 设备导向的音乐转移 [PDF](https://arxiv.org/pdf/2511.17136), [HTML](https://arxiv.org/abs/2511.17136)
### Authors
Manh Pham Hung,Changshuo Hu,Ting Dang,Dong Ma
### Background
现有的方法主要集中在调整音色、节奏、和声或乐器来模仿特定的音乐风格或艺术家，但忽视了播放设备（例如扬声器）的多样化硬件特性。因此，研究者提出了DeMT方法，该方法利用一种视觉-语言模型处理扬声器的频率响应曲线作为线图，提取设备嵌入。这些设备嵌入通过特征层面线性调制来条件化混合变换器，从而实现有效的扬声器风格转换和对未见过的设备的有效几-shot适应，支持提高设备质量和样式增强等应用。
### Innovation
该方法通过利用视觉-语言模型处理扬声器的频率响应曲线来提取设备嵌入，并通过特征层面线性调制来条件化混合变换器，实现有效对未见过设备的扬声器风格转换与适应，增强了个性化音乐应用的效果。
### Conclusion
研究者提出的DeMT方法能够有效实现未见过设备上的扬声器风格转换和几-shot适应，支持设备样式的增强和质量的提升。
## 71. `cs.AI` - Attention-Guided Feature Fusion (AGFF) Model for Integrating Statistical and Semantic Features in News Text Classification [PDF](https://arxiv.org/pdf/2511.17184), [HTML](https://arxiv.org/abs/2511.17184)
### Authors
Mohammad Zare
### Background
新闻文本分类是自然语言处理中的一项关键任务，对于组织和过滤大量数字内容至关重要。传统方法通常依赖于诸如词频或TF-IDF值这样的统计特征，这些特征在捕捉单词级别的重要性方面有效，但往往无法反映上下文的意义。相比之下，现代深度学习方法利用语义特征来理解单词在上下文中的使用方式，但却可能忽视一些简单但高影响力的统计指标。
### Innovation
本文提出了一种注意引导的特征融合(AGFF)模型，该模型在一个统一框架中结合了统计和语义特征。模型采用注意机制来动态确定每种特征类型的重要性，从而做出更明智的分类决策。在基准新闻数据集上的评估表明，AGFF模型的性能优于传统的统计模型和纯语义深度学习模型。研究结果表明，战略集成多种特征类型可以大大提高分类准确性。此外，消融研究验证了融合过程中每个组件的贡献。
### Conclusion
研究表明，该模型能够平衡和利用统计和语义表示的互补优势，使其成为一个实用且有效的实际新闻分类任务解决方案。
## 72. `cs.AI` - 几何分解遗忘 [PDF](https://arxiv.org/pdf/2511.17100), [HTML](https://arxiv.org/abs/2511.17100)
### Authors
Duo Zhou,Yuji Zhang,Tianxin Wei,Ruizhong Qiu,Ke Yang,Xiao Lin,Cheng Qian,Jingrui He,Hanghang Tong,Heng Ji,Huan Zhang
### Background
机器遗忘，即从部署模型中移除特定训练集子集的影响，对于隐私保护和模型可靠性至关重要。然而，通过梯度上升法遗忘样本往往会对保留的知识造成损害。现有的方法在有效遗忘和保留知识的保留之间存在持续的权衡。虽然之前的方法提供了有用的经验法则，但它们往往缺乏对遗忘更新如何损害保留知识以及通过理论保证来消除副作用的具体分析。本文从保留集性能实际受影响的基本原理出发，进行了一阶局部变化分析，首次提出了一种理论上稳健且简单的解决方案。
### Innovation
本文提出了一种基于几何分解的遗忘方法（GU），该方法将候选遗忘梯度更新分解为与保留空间相切和正交的分量，并只执行正交分量。这种方法可以在标准的信任区间预算下找到最优的一阶不变移动方向，并推导出联合遗忘-保留更新目标的最优投影方向。该方法插即用，可以与现有的基于梯度的遗忘程序结合使用，以减轻副作用。
### Conclusion
GEOMETRIC-Disentangelment Unlearning (GU)方法在TOFU，MUSE和WMDP三个基准上实现了各种方法的一致改进。GU方法通过对遗忘梯度更新进行几何分解，实现了有效遗忘和保留知识的平衡，提供了理论上稳健的遗忘解决方案。
## 73. `cs.AI` - OmniPT：解锁大规模视觉语言模型在行人跟踪和理解中的潜力 [PDF](https://arxiv.org/pdf/2511.17053), [HTML](https://arxiv.org/abs/2511.17053)
### Authors
Teng Fu,Mengyang Zhao,Ke Niu,Kaixin Peng,Bin Li
### Background
大面积视觉语言模型（LVLMs）在图像级别任务如视觉问答（VQA）和字幕方面表现出色，但在行人跟踪和对象检测等实例级别任务中，与以前的专家模型相比仍存在性能差距。虽然行人跟踪是一个经典任务，但在将物体跟踪和自然语言结合的新领域，如引用多对象跟踪（Referring MOT）、跨视图引用多对象跟踪（Cross-view Referring MOT）和语义多对象跟踪（Semantic MOT）中，已经产生了许多新话题。这些任务强调模型应以更高级别的语义理解被跟踪的对象，这是LVLMs的优势所在。
### Innovation
本文提出了一种新的统一的行人跟踪框架，即OmniPT，可以实现行人跟踪、基于引用的跟踪，并且可以互动地生成对被跟踪物体的语义理解。为了将跟踪任务建模成基础模型能够执行的任务，并使模型输出格式化的答案，采用了一种包含RL-Mid训练-SFT-RL的训练方案。通过这种方法，使LVLM能够输出固定和可监督的边界框格式，并通过多个行人相关的数据集进行中间训练，然后进行监督微调以提高跟踪性能和指令遵循能力。
### Conclusion
在跟踪基准测试上的实验结果表明，所提出的方法可以比以前的方法表现更好。
## 74. `cs.AI` - 学习压缩：解锁大型语言模型在文本表示中的潜力 [PDF](https://arxiv.org/pdf/2511.17129), [HTML](https://arxiv.org/abs/2511.17129)
### Authors
Yeqin Zhang,Yizheng Zhao,Chen Hu,Binxing Jiao,Daxin Jiang,Ruihang Miao,Cam-Tu Nguyen
### Background
文本表示在聚类、检索及其他下游应用中起着关键作用。随着大型语言模型（LLMs）的出现，人们逐渐关注如何利用其能力进行文本表示。然而，大多数LLM本质上是因果的，主要用于下一个标记的预测，这使得它们在生成整体表示时效果不理想。为解决这一问题，近期研究引入了预训练任务来适应LLM用于文本表示。大多数这些预训练任务依赖于标记级预测目标，如LLM2Vec中使用的掩码下一个标记预测（MNTP）。本研究探讨了上下文压缩作为预训练任务的潜在能力，以无监督方式适配LLM。压缩预训练期间，模型学习生成紧凑的记忆标记来替代整个上下文用于下游序列预测。
### Innovation
本研究首次提出将上下文压缩作为预训练任务，以发挥大型语言模型的潜力并改进文本表示。通过设计良好的压缩目标，这种方法显著提升了基于LLM的文本表示效果，尤其是在不需要大量训练数据的情况下较其他标记级预训练任务生成的模型表现更佳。进一步引入对比学习还提升了模型性能，开发出了一种强大的表示模型（LLM2Comp），在广泛的应用任务上均优于现有基于LLM的文本编码模型。
### Conclusion
实验表明，设计良好的压缩目标能够显著增强基于LLM的文本表示，提出的模型在多种任务上展现出色的性能，同时在所需训练数据量上表现出更高的样本效率。
## 75. `cs.AI` - 适用于实时遥感图像小目标检测的轻量化检测器 [PDF](https://arxiv.org/pdf/2511.17147), [HTML](https://arxiv.org/abs/2511.17147)
### Authors
Qianyi Wang,Guoqiang Ren
### Background
遥感图像在多个领域广泛应用，但实时检测小目标仍然具有挑战性，因为需要平衡精度和效率。现有的方法难以兼顾小目标的识别准确性和处理速度。
### Innovation
提出了一种名为DMG-YOLO的轻量化实时检测器，专为遥感图像中的小目标检测设计。设计了一个双支特征提取（DFE）模块，在主干中分割特征图，一端利用深度可分离卷积提取局部特征，另一端利用带有门控机制的视觉变换器捕捉全局上下文；采用带有膨胀卷积的多尺度特征融合（MFF）模块，增强多尺度信息整合同时保留细部信息；引入全局和局部聚合特征金字塔网络（GLAFPN），通过全局-局部特征融合进一步提升小目标检测性能。
### Conclusion
在VisDrone2019和NWPU VHR-10数据集上的广泛实验表明，DMG-YOLO在mAP、模型大小及其他关键指标上取得了竞争力的表现。
## 76. `cs.AI` - 深层MPC的算法设计与实现考虑 [PDF](https://arxiv.org/pdf/2511.17233), [HTML](https://arxiv.org/abs/2511.17233)
### Authors
Prabhat K. Mishra,Mateus V. Gasparino,Girish Chowdhary
### Background
深层模型预测控制（Deep MPC）是一个正在发展的领域，它结合了模型预测控制和深度学习技术。该方法在模型预测控制（MPC）和深度神经网络之间分配控制权限，其中深度神经网络学习模型不确定性，而MPC负责处理约束条件。这种方法的优点之一是可以利用系统运行过程中收集的数据微调神经网络，MPC在学习过渡期间防止潜在的不安全行为。
### Innovation
该研究提出了一种特别的Deep MPC方法，该方法在MPC中引入了深度神经网络，并解释了算法如何分配控制权以控制系统的不确定性。而传统的MPC方法可能会遇到控制权分配不当导致性能不佳的问题，该研究通过四轮滑移转向动力学的数值实验解释了这种不良性能的原因。
### Conclusion
该研究深入探讨了Deep MPC的实现挑战，提供了一种算法分配控制权的方法，并指出不当分配控制权可能导致系统性能不佳。通过上述分析，研究者建议在实际应用中需要慎重选择控制权分配策略以保证Deep MPC系统的优化性能。
## 77. `cs.AI` - 在翻译与噪声中迷失：VLMs在处理真实世界表格中的失败模式深入探讨 [PDF](https://arxiv.org/pdf/2511.17238), [HTML](https://arxiv.org/abs/2511.17238)
### Authors
Anshul Singh,Rohan Chaudhary,Gagneet Singh,Abhay Kumary
### Background
现有的VLM（视觉语言模型）在评估中往往依赖于未能有效捕捉现实场景复杂性的基准测试。现有的表格问答数据集，如WikiTableQuestions和FinQA，主要是单语言的（如英语），且表格以数字化完美的状态呈现。这导致了研究与实践之间的显著差距。
### Innovation
为解决以上问题，该研究提出了新的基准测试——MirageTVQA，包括几乎6万个跨24种语言的问答对，并包含视觉不完美的表格以及现实噪声。评价结果表明，最佳模型面对视觉噪声时表现严重下降，并且存在一种英语优先的语言偏见。
### Conclusion
MirageTVQA为评估和推动更加稳健的VLM模型提供了标准，特别是在表格推理方面。该数据集及代码可从指定链接获取。
## 78. `cs.AI` - PLLuM指令语料库 [PDF](https://arxiv.org/pdf/2511.17161), [HTML](https://arxiv.org/abs/2511.17161)
### Authors
Piotr Pęzik,Filip Żarnecki,Konrad Kaczyński,Anna Cichosz,Zuzanna Deckert,Monika Garnys,Izabela Grabarczyk,Wojciech Janowski,Sylwia Karasińska,Aleksandra Kujawiak,Piotr Misztela,Maria Szymańska,Karolina Walkusz,Igor Siek,Maciej Chrabąszcz,Anna Kołos,Agnieszka Karlińska,Karolina Seweryn,Aleksandra Krasnodębska,Paula Betscher,Zofia Cieślińska,Katarzyna Kowol,Artur Wilczek,Maciej Trzciński,Katarzyna Dziewulska,Roman Roszko,Tomasz Bernaś,Jurgita Vaičenonienė,Danuta Roszko,Paweł Levchuk,Paweł Kowalski,Irena Prawdzic-Jankowska,Marek Kozłowski,Sławomir Dadas,Rafał Poświata,Alina Wróblewska,Katarzyna Krasnowska-Kieraś,Maciej Ogrodniczuk,Michał Rudolf,Piotr Rybak,Karolina Saputa,Joanna Wołoszyn,Marcin Oleksy,Bartłomiej Koptyra,Teddy Ferdinan,Stanisław Woźniak,Maciej Piasecki,Paweł Walkowiak,Konrad Wojtasik,Arkadiusz Janz,Przemysław Kazienko,Julia Moska,Jan Kocoń
### Background
本文介绍了在PLLuM（波兰大型语言模型）项目中用于微调一组基于变压器的大语言模型（LLMs）的指令数据集。文中呈现了有机、转换和合成指令的功能分类，并探讨了使用人类撰写的指令数据集与合成指令数据集在语言适应基础LLMs中的差异。此外，我们发布了PLLuM指令语料库的第一代表型子集（PLLuMIC），我们认为它对指导和规划其他LLM的类似语料库的开发具有有用性。
### Innovation
介绍了PLLuM项目的指令数据集，提出了有机、转换和合成指令的功能分类，并首次公开了PLLuMIC这一代表型子集。
### Conclusion
研究结果表明，人类撰写的指令数据集与合成指令数据集在语言适应基础LLMs中的使用具有不同的影响，而PLLuMIC可以为开发其他LLM的类似数据集提供参考和指导。
## 79. `cs.AI` - 利用CVAE从点云数据估算多指机械手的关节配置 [PDF](https://arxiv.org/pdf/2511.17276), [HTML](https://arxiv.org/abs/2511.17276)
### Authors
Julien Merand,Boris Meden,Mathieu Grossard
### Background
传统的逆向运动学（IK）技术可以基于指尖的姿态来确定机械手指的关节配置，但在处理复杂运动学时往往需要额外的决策过程或使用数值逼近方法。这类方法仍然面临一系列挑战，如考虑所有中节指骨的位置或通过算法近似解决复杂运动学问题。因此，论文提出了一种基于机器学习的方法，通过条件变分自编码器（CVAE）直接从点云数据中推断出关节配置，从而有效解决了这些挑战。
### Innovation
该论文创新性地利用条件变分自编码器（CVAE）从点云数据中隐式克服了上述挑战。方法通过将点云数据作为输入，重建相应的关节配置。这种方法在MultiDex抓取数据集上使用Allegro Hand验证，其在0.05毫秒内运行，并达到与先进方法相当的准确度。
### Conclusion
该方法展示了在AI驱动的抓取规划技术中，关节配置估计的有效性，突显了CVAE在该领域中的应用潜力。
## 80. `cs.AI` - 通过更深入思考减少幻觉：大语言模型的方面因果规避 [PDF](https://arxiv.org/pdf/2511.17170), [HTML](https://arxiv.org/abs/2511.17170)
### Authors
Vy Nguyen,Ziqi Xu,Jeffrey Chan,Estrid He,Feng Xia,Xiuzhen Zhang
### Background
大语言模型（LLMs）常常会产生流畅但事实错误的回答，这是被称为幻觉的现象。避免回复的方法如弃权（abstention），通常通过选择不回答并输出诸如“我不知道”的短语来实现。然而，现有的弃权方法大多依赖于生成后的信号，如生成变化或反馈，这限制了它们预防不可靠响应的能力。
### Innovation
本文提出了一种新的框架，即方面因果规避（ABCA），该框架通过因果推理分析LLM知识的内部多样性，以便提前规避。ABCA根据每个方面的因果效应估计知识的相关性，以评估响应的可靠性。根据这些估计，可以实现两种类型的规避：一是方面效应不一致（知识冲突），二是方面效应一致支持规避（知识不足）。实验表明，ABCA提高了规避可靠性，达到了最先进的性能，并增强了规避决策的可解释性。
### Conclusion
ABCA通过评估知识的相关性和可靠性，提供了更有效的规避机制，极大地提高了解释和规避决策的准确性与透明度。
## 81. `cs.AI` - Parrot: Persuasion and Agreement Robustness Rating of Output Truth -- A Sycophancy Robustness Benchmark for LLMs [PDF](https://arxiv.org/pdf/2511.17220), [HTML](https://arxiv.org/abs/2511.17220)
### Authors
Yusuf Çelebi,Mahmoud El Hussieni,Özay Ezerceli
### Background
本研究探讨了在社交压力影响下，特别是在权威和说服作用下，大规模语言模型（LLM）产生不符合事实输出的现象。这种现象中的一种表现称为逢迎（过度顺从），即模型在权威或者说服力的影响下偏向给出错误但顺从的回应。
### Innovation
该研究提出了PARROT框架，用于评估LLMs在社交压力下的准确度退化。PARROT通过双盲评估比较中性版本和权威虚假版本的问题，利用对数似然校准跟踪量化信心变化，并通过八个行为分类标准系统分类失效模式。
### Conclusion
研究发现，高层次模型（如GPT-5，GPT-4.1）表现出低“遵守率”和轻微准确度损失，而较老或较小的模型则表现较差，显示出严重的知识坍缩。研究指出，在实际部署过程中，应该将‘抗过拟合压力’目标与准确度、减少伤害和保障隐私一起作为主要目标。
## 82. `cs.AI` - TP-MDDN：具有自主决策的多任务偏好多项需求驱动导航 [PDF](https://arxiv.org/pdf/2511.17225), [HTML](https://arxiv.org/abs/2511.17225)
### Authors
Shanshan Li,Da Huang,Yu He,Yanwei Fu,Yu-Gang Jiang,Xiangyang Xue
### Background
在日常生活中，人们经常需要在空间中移动以找到满足需求的物体，这给具身处境的人工智能提出了关键挑战。传统的单一需求驱动导航方法（DDN）只能处理一个需求，而无法反映多需求和个性化选择的复杂性。由于缺乏长期多需求处理能力，现有方法难以应对这一挑战。
### Innovation
我们提出了任务偏好型多需求驱动导航（TP-MDDN），作为包含多子需求且带有明确任务偏好的长时间导航的新基准。为了解决TP-MDDN，我们设计了一个自主决策系统AWMSystem，该系统包括BreakLLM（指令分解）、LocateLLM（目标选择）和StatusMLLM（任务监控）三个关键模块。此外，我们还设计了MASMap，通过结合3D点云累积和2D语义地图来实现准确且高效的环境理解。我们的双时域动作生成框架结合了零样本规划和基于策略的精细控制，并借助一个实时适应性错误纠正器来处理实际失败情况。
### Conclusion
我们的方法在感知准确性和导航鲁棒性方面显著优于现有最先进的基线方法。
## 83. `cs.AI` - 全面干预-全路径统一减轻LVLM幻觉 [PDF](https://arxiv.org/pdf/2511.17254), [HTML](https://arxiv.org/abs/2511.17254)
### Authors
Jiaye Qian,Ge Zheng,Yuchen Zhu,Sibei Yang
### Background
尽管大型视觉-语言模型（LVLMs）在各种任务中表现出色，但它们仍然容易出现幻觉。研究发现LVLMs中的幻觉并非源自单一的因果路径，而是由图像到输入文本、图像到输出文本以及文本到文本路径的相互作用引起。此外，LVLMs依赖的路径也因问题-答案对齐格式的不同而不同。
### Innovation
我们提出了一种与变换器因果架构相一致的全面干预框架，并且通过不同干预路径的研究发现，首次确认了LVLMs根据不同问题答案对齐格式依赖于不同的路径。基于这些见解，我们提出了简单有效的识别和干预关键幻觉头部的方法，旨在针对区分性和生成性格式进行定制。
### Conclusion
我们方法在多个基准测试中表现出色，一致地减少了不同对齐类型下的幻觉现象。
## 84. `cs.AI` - AI工作者、地缘政治与算法集体行动 [PDF](https://arxiv.org/pdf/2511.17331), [HTML](https://arxiv.org/abs/2511.17331)
### Authors
Sydney Reis
### Background
国际政治经济学(IPE)理论表明，国家往往被激励依赖而非约束强大的跨国公司。这一背景揭示了生效于国际和国家层面治理人工智能努力的不均衡现象。文章利用探索AI公司在地缘政治中作用的研究，提出了一些AI工作者可以被视为地缘政治行动者，并补充了关于AI治理的讨论。
### Innovation
文章提出AI治理不应仅依赖于自上而下的方法，更为关注自下而上的干预，特别是在AI开发现场。提出了利用参与式设计（PD）方法，鼓励AI工作者作为知识、权力和意图的来源，从而促进更具责任感和公正性的AI开发，并创造有利于算法集体行动（ACA）的条件。
### Conclusion
本文认为，AI治理需要更多地关注和利用AI工作者的作用，特别是其通过算法集体行动促进变革的潜力。通过这类干预，可以鼓励更加负责和公正的AI开发，并创造有利于算法集体行动的条件。
## 85. `cs.AI` - Range-Edit: 德法语LiDAR户外场景语义掩模引导编辑 [PDF](https://arxiv.org/pdf/2511.17269), [HTML](https://arxiv.org/abs/2511.17269)
### Authors
Suchetan G. Uppur,Hemant Kumar,Vaibhav Kumar
### Background
培训自动驾驶和导航系统需要大量的多样化点云数据集，这些数据集能够捕捉各种动态城市环境中的复杂边缘情况。从真实世界的数据中获取如此多样化的场景，特别是对于关键的边缘情况来说具有挑战性，这限制了系统的泛化能力和鲁棒性。当前的方法主要依靠在手工构建的3D虚拟环境中模拟点云数据，这既耗时又计算成本高，而且常常无法完全捕捉到真实场景的复杂性。
### Innovation
本文提出了一种创新的方法，通过使用基于语义掩模的指导来编辑真实世界的LiDAR扫描，生成新颖的合成LiDAR点云。这种方法结合了范围图像投影和语义掩模条件，实现了扩散生成技术。点云被转换为2D范围视图图像，作为中间表示形式，使用凸包基语义掩模进行语义编辑。这些掩模通过提供在真实环境中物体的尺寸、方向和位置信息来引导生成过程，保证几何一致性与真实性。这种方法能产生高质量的LiDAR点云生成，并且能够生成复杂边缘案例和动态场景，已经在KITTI-360数据集上进行了验证。
### Conclusion
这种方法提供了一种低成本和可扩展的解决方案，用于生成多样化的LiDAR数据，朝着提高自动驾驶系统的鲁棒性迈进。
## 86. `cs.AI` - 文化消散：揭示文本到图像生成中的文化差距 [PDF](https://arxiv.org/pdf/2511.17282), [HTML](https://arxiv.org/abs/2511.17282)
### Authors
Chuancheng Shi,Shangze Li,Shiming Guo,Simiao Xie,Wenhua Wu,Jingtong Dou,Chao Wu,Canran Xiao,Cong Wang,Zifeng Cheng,Fei Shen,Tat-Seng Chua
### Background
多语种文本到图像（T2I）模型在视觉真实性和语义一致性方面取得了快速进展，广泛应用于各种场景。然而，这些模型生成的图像在不同文化背景下呈现出差异，这是因为语言带有文化含义，因此从多语种提示生成的图像应保持跨文化的文化一致性。
### Innovation
该研究通过对比分析两种代表性模型，发现当前的T2I模型在多语种提示下产生文化中立或以英语为中心的结果并非由于缺乏文化知识，而是由于文化相关表示激活不足。为此，研究提出了一种探针方法，以定位关键的文化敏感信号，并提出两种互补的对齐策略：（1）在推理时激活文化，增强已识别的神经元但无需微调骨干网络；（2）针对特定层的文化增强，仅更新与文化相关联的层，从而在保持图像保真度和多样性的情况下提升了文化一致性。
### Conclusion
研究通过CultureBench实验展示了提出的方法在文化一致性方面的一致性改进，同时保持了图像的保真度和多样性。
## 87. `cs.AI` - DISCA: 一种使用压缩Bent-Pyramid格式的数字忆内随机计算架构 [PDF](https://arxiv.org/pdf/2511.17265), [HTML](https://arxiv.org/abs/2511.17265)
### Authors
Shady Agwa,Yikang Shen,Shiwei Wang,Themis Prodromakis
### Background
当前，人工智能革命正取代各种应用领域的技术主导地位，如医疗保健、机器人技术、汽车、安全和国防等领域。大规模的人工智能模型通过数据密集型矩阵乘法任务模仿人类大脑的功能，通常包含数百万甚至数十亿个参数。传统的冯·诺依曼架构在处理“内存墙”和“摩尔定律”终结的问题上面临挑战，而这些AI应用正迅速迁移到边缘计算，例如机器人和无人驾驶飞机中的监视任务，从而给边缘AI架构的硬件预算带来了更多限制。为解决内存墙问题，虽然已提出了忆内计算作为一种有前途的解决方案，但模拟计算架构和数字系统由于各种设计限制都表现出了实质性的性能下降。
### Innovation
本文提出了一种新的数字忆内随机计算架构——DISCA，该架构利用压缩版的准随机Bent-Pyramid数据格式。DISCA继承了模拟计算的计算简单性，同时保持了数字系统的可扩展性、生产力和可靠性。使用商用180nm CMOS工艺进行的后布局建模结果表明，DISCA在500 MHz频率下表现出3.59 TOPS/W每比特的能效，大幅提高了矩阵乘法等负载的能源效率。
### Conclusion
DISCA显著提高了矩阵乘法工作负载的能源效率，相比其同类架构有数量级的改进。
## 88. `cs.AI` - 弱监督去混响中，相位真的有必要吗？ [PDF](https://arxiv.org/pdf/2511.17346), [HTML](https://arxiv.org/abs/2511.17346)
### Authors
Marius Rodrigues(IDS, S2A),Louis Bahrman(IDS, S2A),Roland Badeau(IDS, S2A),Gaël Richard(S2A, IDS)
### Background
在无监督或弱监督的方法中进行语音去混响时，目标纯净（干燥）信号在训练过程中被认为是未知的。因此，仅靠已知的混响（湿润）语音能够提取多少信息成为关键问题。本文探讨了时间-频率域中混响（湿润）相位的作用。基于统计波场理论，研究发现低声频除外，晚期混响会扰动相位分量，使之带有白噪声，均匀分布的噪声。因此，湿润相位携带的有用信息有限，不对于弱监督去混响至关重要。
### Innovation
基于统计波场理论分析混响相位扰动，并展示了混响相位在低频除外的情况下，带有均匀分布的白噪声，湿润相位对于弱监督去混响并不是必需的。通过在最近的弱监督框架下训练去混响模型，排除混响相位，可以显著提高性能。
### Conclusion
研究发现，混响相位对弱监督去混响不是必需的，特别是在低频除外的情况下。排除混响相位作为损失函数的一部分，去混响模型的性能可以显著提升。
## 89. `cs.AI` - MuM: 多视角掩蔽图像建模及其在三维视觉中的应用 [PDF](https://arxiv.org/pdf/2511.17309), [HTML](https://arxiv.org/abs/2511.17309)
### Authors
David Nordström,Johan Edstedt,Fredrik Kahl,Georg Bökman
### Background
自监督学习在图像上的应用旨在从未标记的数据中提取有意义的视觉表示。当应用于大规模数据集时，这种范式已经实现了最先进的性能，得到了包括DINOv3在内的训练模型的广泛应用。然而，大多数先前的努力都集中在语义理解上，而不是几何推理。唯一例外的是Cross-View Completion (CroCo)，它是一种专门针对3D理解的掩蔽自动编码（MAE）方法。在此项工作中，研究者依旧沿用了CroCo的方法路径，专注于学习适用于3D视觉的特征。
### Innovation
研究者将MAE扩展到同一场景的任意多个视角，通过对所有视图进行均匀掩码并使用轻量级的具有帧间注意机制的解码器，这种方式比CroCo更为简单且更具可扩展性。通过对MuM模型在下游任务如前馈重建、稠密图像匹配和相对姿态估计上的广泛评估发现，其优于最先进的视觉编码器DINOv3和CroCo v2。
### Conclusion
通过这种方法，研究者开发了一种适用于3D视觉的模型MuM，该模型在多个三维视觉任务上表现优异，验证了其在这一领域的有效性。
## 90. `cs.AI` - 大型语言模型用于检测社会挑战的情感分析：南非语言的应用案例 [PDF](https://arxiv.org/pdf/2511.17301), [HTML](https://arxiv.org/abs/2511.17301)
### Authors
Koena Ronny Mabokela,Tim Schlippe,Matthias Wölfel
### Background
情感分析有助于理解人们在社会问题上的观点和情绪。在多语言社区中，可以通过检测社交媒体上的情绪来快速识别社会挑战，帮助政府相关部门更精确有效地发现问题。最近，大型语言模型（LLMs）已对外开放，并在英语文本上展示了出色的零样本情感分析能力。然而，有关利用LLMs进行南非语言社交媒体帖子的情感分析的研究尚未出现，特别是对于南非政府相关部门管辖区域的主题。本文研究了几种最新的LLMs在英语文本、塞佩迪语和塞茨瓦纳语的社会媒体帖子上的情感分析零样本性能。
### Innovation
本文的创新之处在于研究了最先进的LLMs（GPT-3.5、GPT-4、LlaMa 2、PaLM 2、Dolly 2）在多重主题（共10个）、两种南非语言（英语、塞佩迪语、塞茨瓦纳语）的社交媒体帖子上的情感分析零样本性能。研究发现，不同LLMs、主题和语言之间存在显著差异。此外，将不同LLMs的结果融合可以显著提高情感分类性能，情感分类错误率低于1%。
### Conclusion
通过融合不同LLMs的结果，可以构建可靠的情感分析系统来检测社会挑战，并推断出特定主题和不同语言组内可能需要采取的行动。这表明，在南非语言中利用大型语言模型进行情感分析的可能性和实用性。
## 91. `cs.AI` - MusicAIR：一种由算法驱动的核心驱动的多模态AI音乐生成框架 [PDF](https://arxiv.org/pdf/2511.17323), [HTML](https://arxiv.org/abs/2511.17323)
### Authors
Callie C. Liao,Duoduo Liao,Ellie L. Zhang
### Background
近年来，生成AI的发展使得音乐生成成为研究的重点。然而，许多基于神经网络的模型依赖于大量的数据集，这引起了版权侵权和高性能成本的担忧。
### Innovation
本文提出了MusicAIR，这是一种创新的多模态AI音乐生成框架，通过一种新颖的算法驱动的符号音乐核心有效降低了版权侵权的风险。该框架能够仅从歌词、文本和图像生成完整的、连贯的旋律曲谱。MusicAIR不仅实现了通过歌词生成音乐，还能够从文本和图像生成音乐。实验结果显示，该系统生成的曲谱在典型音乐指标上得分85%，比人类作曲家的79%更高，同时与已建立的音乐理论标准高度一致，证明了其生成多样且具人类风格的作品的能力。
### Conclusion
MusicAIR作为人工智能辅助工具，不仅可以作为可靠的音乐创作助手，还可以作为一种可能的教学创作导师，同时降低了所有有志音乐家的门槛，这是创新之处并对AI在音乐生成中的应用有显著贡献。
## 92. `cs.AI` - 量子遮罩自编码器在视觉学习中的应用 [PDF](https://arxiv.org/pdf/2511.17372), [HTML](https://arxiv.org/abs/2511.17372)
### Authors
Emma Andrews,Prabhat Mishra
### Background
经典自编码器广泛用于学习输入数据的特征。经典遮罩自编码器通过引入遮罩数据进一步提高特征学习。量子自编码器已有相关研究，但尚未有量子遮罩自编码器的设计和实现，能够在量子状态下学习数据样本的缺失特征并实现掩码输入图像的重建。
### Innovation
本文提出了量子遮罩自编码器（QMAE），其能够在量子状态下学习数据样本中的缺失特征，而不仅仅是使用经典嵌入。实验结果表明，QMAE在MNIST图像中可以更精确地恢复遮罩输入图像，并且在有遮罩的情况下，分类精度比最先进的量子自编码器高出平均12.86%。
### Conclusion
实验评估结果表明，QMAE能够显著优于最先进的量子自编码器在有遮罩的情况下，提高了分类精度与视觉保真度。
## 93. `cs.AI` - SMILE：问题回答评估中的复合词法语义度量 [PDF](https://arxiv.org/pdf/2511.17432), [HTML](https://arxiv.org/abs/2511.17432)
### Authors
Shrikant Kendre,Austin Xu,Honglu Zhou,Michael Ryoo,Shafiq Joty,Juan Carlos Niebles
### Background
传统的文本和视觉问答评估指标，如ROUGE、METEOR和精确匹配（EM），主要关注基于n-gram的词性和语义相似度，往往忽视了准确评估所需的深层语义理解。虽然BERTScore和MoverScore通过利用上下文嵌入来解决这一限制，但它们在平衡句子级和关键词级语义方面缺乏灵活性，并且忽略了词性和语义相似度的重要性。大规模语言模型（LLM）评估器虽然强大，但也存在成本高、偏见、不一致性以及幻觉等问题。
### Innovation
SMILE是一种新型方法，它将句子级语义理解和关键词级语义理解以及简单的关键词匹配相结合。这种方法平衡了词法精确性和语义相关性，提供了一个全面的评估。”“广泛基准测试表明，SMILE与人类判断高度相关，并且计算量轻，有效地弥合了词法和语义评估之间的差距。
### Conclusion
广泛的文本、图像和视频问答任务的基准测试显示，SMILE与人类判断高度相关，并且计算量轻，为文本、图像和视频问答系统的评估提供了新的方法。
## 94. `cs.AI` - 多通道成像中的稀疏混合专家：所有通道交互都是必要的吗？ [PDF](https://arxiv.org/pdf/2511.17400), [HTML](https://arxiv.org/abs/2511.17400)
### Authors
Sukwon Yun,Heming Yao,Burkhard Hoeckendorf,David Richmond,Aviv Regev,Russell Littman
### Background
视觉转换器（ViTs）已发展成为视觉基础模型的核心，但在多通道领域（如细胞绘画或卫星成像）的优化研究仍然不足。由于每个通道承载不同信息，需要捕捉通道间交互，而现有的方法虽然在单通道处理上有效，但会导致注意力机制中计算成本剧增，从而增加训练成本。
### Innovation
本文提出了MoE-ViT（基于稀疏混合专家的 ViTs），通过将每个通道视为专家并利用轻量级路由器仅选择每个团块中最相关的专家进行注意力交互，突破了现有技术的瓶颈。这种方法不仅能大幅提高效率，而且在某些情况下还能提升性能。
### Conclusion
实验证明MoE-ViT在真实数据集（JUMP-CP 和 So2Sat）上既提升了效率，又保持了或提高了性能，表明其作为一种多通道影像的理想基础模型具有很高的实用价值和吸引力。
## 95. `cs.AI` - FORWARD: 林道粗粝地形条件下前切式装载机运行数据集 [PDF](https://arxiv.org/pdf/2511.17318), [HTML](https://arxiv.org/abs/2511.17318)
### Authors
Mikael Lundbäck,Erik Wallin,Carola Häggström,Mattias Nyström,Andreas Grönlund,Mats Richardson,Petrus Jönsson,William Arnvik,Lucas Hedström,Arvid Fälldin,Martin Servin
### Background
本研究详细介绍了FORWARD数据集，这是一个高分辨率多模态数据集，记录了前切式装载机在瑞典中部两个采伐现场粗粝地形中的运行情况。装载机配备了多种传感器，包括RTK-GNSS、360度摄像头、操作员振动传感器、车内CAN总线信号记录以及多个IMU。数据集包括森林区域激光扫描的高清点云数据，以及包含机器事件的日志文件、大量视频材料和各种地理数据。通过这些详细的数据，研究者能够评估机器的交通性、感知能力和自主控制能力，进而用于森林机械的智能控制、模拟和实验。
### Innovation
FOWARD数据集的独特之处在于其高分辨率的多模态数据，涵盖了详细的地理位置、驾驶速度、燃料消耗和多角度视频记录，这些数据可以用于开发机器的交通性、感知和自主控制模型，特别是在复杂的森林地形条件下。该数据集还提供了场景规范，包括多次在同一路径上驾驶、不同负载重量和不同驾驶速度的实验方案。
### Conclusion
FORWARD数据集旨在促进森林机械交通性、感知能力和自主控制的模型和算法开发，利用人工智能、模拟和物理测试床的实验。该数据集的应用不仅可以提高机器的效率和安全性，还能够优化燃料消耗和降低环境影响，同时也为森林机械模拟器的自动校准和自动化场景描述提供了宝贵的实地数据。
## 96. `cs.AI` - 超越选择题：一种统一稳健评估与可验证推理训练的混合框架 [PDF](https://arxiv.org/pdf/2511.17405), [HTML](https://arxiv.org/abs/2511.17405)
### Authors
Yesheng Liu,Hao Li,Haiyu Xu,Baoqi Pei,Jiahao Wang,Mingxuan Zhao,Jingshu Zheng,Zheqi He,JG Yao,Bowen Qin,Xi Yang,Jiajun Zhang
### Background
多项选择题问答（MCQA）已成为评估和强化训练现代多模态语言模型的一种流行格式。这种格式受限的输出便于简化和确定性的自动验证。然而，选项中可能包含可利用的信息，导致准确性指标不可靠，同时也促使在强化训练过程中出现明确或隐含的答案猜测行为。
### Innovation
提出了ReVeL框架，该框架将多项选择题问题重写为开放形式问题，同时尽可能保持答案可验证。根据不同的答案类型，应用不同的重写和验证方案。在应用到强化训练中时，将20,000个MCQA示例转换为确保模型在多重选择基准测试和开题问答基准测试中表现一致并提高约6个百分点，表明ReVeL在数据效率和奖励信号的稳健性方面优于基于MCQA的训练。
### Conclusion
当用于评估时，ReVeL揭示了MCQA基准测试中的最高20个百分点的评分膨胀，并改进了判断准确度，同时减少了成本和延迟。代码和数据将公开发布。
## 97. `cs.AI` - InTAct：基于区间任务激活的持续学习方法 [PDF](https://arxiv.org/pdf/2511.17439), [HTML](https://arxiv.org/abs/2511.17439)
### Authors
Patryk Krukowski,Jan Miksa,Piotr Helm,Jacek Tabor,Paweł Wawrzyński,Przemysław Spurek
### Background
持续学习的目标是在不遗忘之前学到的信息的情况下，使神经网络能够获取新知识。虽然基于提示的方法在类别增量设置中表现出色，但在涉及领域转换的情景下仍显脆弱，领域转换指的是输入分布的变化但标签空间保持固定。这种转换暴露了一个持续存在的问题——表示漂移。共享表示以这种方式进化，实际上覆盖了之前有用的功能，即使提示隔离了特定任务的参数，也会导致遗忘。
### Innovation
我们引入了InTAct方法，该方法在不冻结参数或存储过去数据的情况下，保留共享层的功能行为。InTAct捕获与之前学过的任务相关的特征激活范围，并限制更新以确保网络在这些区域内保持一致，同时仍然允许在其他地方进行灵活的适应。通过这种方法，InTAct稳定了关键神经元的功能角色，而不是直接限制参数值。InTAct是一种架构无关的方法，并能够无缝集成到现有的基于提示的持续学习框架中。通过调节过去知识编码的表示变化，InTAct实现了一种关于稳定性和可塑性的平衡。
### Conclusion
InTAct在多个域增量基准测试中，包括DomainNet和ImageNet-R，一致地减少了表示漂移并提高了性能，相对于最先进的基线提高了平均准确率至多8个百分点。
## 98. `cs.AI` - 设计和生成适用于面部验证任务的多样化、平等的人脸图像数据集 [PDF](https://arxiv.org/pdf/2511.17393), [HTML](https://arxiv.org/abs/2511.17393)
### Authors
Georgia Baltsou,Ioannis Sarridis,Christos Koutlis,Symeon Papadopoulos
### Background
人脸识别是多种应用中身份验证的重要组成部分，包括在线银行和个人设备的安全访问。现有的人脸图像数据集往往存在明显的种族、性别及其他人口统计学特征上的偏差，限制了面部验证系统的有效性和公平性。
### Innovation
本文提出了一种综合方法，利用先进的生成模型创建多变且具有多样性的高质量合成人脸图像。该方法强调对各种面部特征的表示，确保符合身份卡照片的特征要求。同时，作者引入了Diverse and Inclusive Faces for Verification (DIF-V)数据集，包含27,780张2,926个唯一身份个体的人脸图像，旨在为未来的面部验证研究提供基准。研究还揭示了现有的验证模型对某些性别和种族存在偏见，且身份样式修改对模型性能有负面的影响。
### Conclusion
通过解决现有数据集中固有的不平等问题，本文不仅丰富了关于人工智能中的多样性和伦理的讨论，还为开发更包容和可靠的人脸验证技术奠定了基础。
## 99. `cs.AI` - REMSA: 一种用于遥感中基础模型选择的LLM代理 [PDF](https://arxiv.org/pdf/2511.17442), [HTML](https://arxiv.org/abs/2511.17442)
### Authors
Binger Chen,Tacettin Emre Bök,Behnood Rasti,Volker Markl,Begüm Demir
### Background
遥感（RS）中的基础模型（FMs）被广泛应用于环境监测、灾害评估和土地利用制图等任务。这些模型包括单一数据模态的视敏度编码器和多种数据模态组合的多模态架构。尽管这些模型支持多样化的RS任务，如语义分割、图像分类、变化检测和视觉问答，但选择合适的遥感基础模型（RSFM）仍具挑战性，原因在于文档分散、格式不统一和部署限制多样。
### Innovation
本文介绍了一款名为REMSA的基于LLM的代理工具，用于根据不同用户需求自动选择合适的RSFM。REMSA通过自然语言查询理解用户要求，解决缺失约束问题，使用上下文学习对候选模型进行排名，并提供透明的解释。此外，还提出了涵盖75种专家验证的RS查询场景基准，通过专家为中心的评估协议产生900种配置。实验结果表明，REMSA在多个基准上优于基线方法，包括简单的代理、密集检索和基于结构化RAG的LLM。
### Conclusion
REMSA在全公开元数据下运行，无需访问私人或敏感数据，能够有效地辅助用户根据自然语言查询快速准确地选择最适合的RSFM，显著提高了RSFM的选择效率和准确性。
## 100. `cs.AI` - 增强古兰经学习：基于多模态深度学习的阿拉伯音素识别方法 [PDF](https://arxiv.org/pdf/2511.17477), [HTML](https://arxiv.org/abs/2511.17477)
### Authors
Ayhan Kucukmanisa,Derya Gelmez,Sukru Selim Calik,Zeynep Hilal Kilimci
### Background
近年来，多模态深度学习的发展显著提升了语音分析和发音评估系统的性能。准确的发音检测在阿拉伯语中仍是一个主要挑战，特别是在古兰经吟诵的背景下，细微的音素差异可改变语义。
### Innovation
该研究提出了一种基于转换器的多模态框架，用于阿拉伯音素误发音检测，将声学和文本表示结合，以提高精度和鲁棒性。该框架结合了UniSpeech提取的声学嵌入和从Whisper转录中提取的基于BERT的文本嵌入，形成统一表示，捕捉音素细节和语言背景。通过实施和评估早期、中等和晚期融合策略，确定了最有效的融合策略。
### Conclusion
实验证明，UniSpeech-BERT多模态配置效果显著，基于融合的变换器结构适合音素级别误发音检测。该研究推动了智能、演讲者独立和多模态计算机辅助语言学习系统的发展，为古兰经发音培训的技术支持和更广泛的声音教育应用提供了实用步骤。
## 101. `cs.AI` - PersonaAgent with GraphRAG: Community-Aware Knowledge Graphs for Personalized LLM [PDF](https://arxiv.org/pdf/2511.17467), [HTML](https://arxiv.org/abs/2511.17467)
### Authors
Siqi Liang,Yudi Zhang,Yue Guo
### Background
随着个性化AI代理的需求不断增加，研究人员提出了基于个人特征的AI代理来适应用户的特定偏好。为了实现这一目标，通常需要一种框架，该框架能够利用大规模语言模型（LLM）的生成能力，并结合丰富的上下文信息，以生成个性化的交互提示。
### Innovation
本文提出了一种名为PersonaAgent的新框架，该框架结合了基于知识图谱的检索增强生成（Graph RAG）机制。具体创新点包括：1）通过知识图谱构建LLM索引以提供用户历史行为和偏好的摘要；2）通过图基社区检测识别相关信息的社区并且生成相关的全球交互模式；3）动态提示工程策略使代理能够保持一致的个人特征行为，同时受益于集体知识。
### Conclusion
实验结果表明，与先前的方法相比，在LaMP基准测试中，该方法在新闻分类F1分数上提高了11.1%，在电影标记F1分数上提高了56.1%，并且将产品评分MAE降低了10.4%。该方法为个性化的大规模语言模型提供了有前景的解决方案。
## 102. `cs.AI` - GRAPHIC---Guidelines for Reviewing Algorithmic Practices in Human-centred Design and Interaction for Creativity [PDF](https://arxiv.org/pdf/2511.17443), [HTML](https://arxiv.org/abs/2511.17443)
### Authors
Joana Rovira Martins,Pedro Martins,Ana Boavida
### Background
人工智能被越来越多地应用于创造领域，促进了设计流程中人机协作系统的开发。在图形设计中，将计算系统融入协作性工作流程面临特定挑战，需要平衡科学严谨性与设计实践中的主观性和视觉性。研究人员通过PRISMA方法论筛选出872篇文章，最终确定了71篇描述了68种不同的人机协作设计系统的文献。
### Innovation
研究引入了名为GRAPHIC的框架，旨在分析应用于图形设计的人工智能系统。该框架包含三个主要维度：协作全景图、流程与模式以及图形设计原则，旨在理解目前系统如何支持人机协作，并发现了研究缺口，包括需要平衡代理人之间的主动性与控制力、提高交互模型的可解释性以及推广基于核心设计原则的变革性创造力系统。
### Conclusion
研究发现，当前的人机合作设计系统在平衡人机角色、提高交互模型的可解释性和促进基于核心设计原则的支持变革性创造力的系统方面存在研究缺口，这些都将有助于未来的研究和发展。
## 103. `cs.AI` - 从假设到发表：AI驱动研究支持系统的全面调查 [PDF](https://arxiv.org/pdf/2503.01424), [HTML](https://arxiv.org/abs/2503.01424)
### Authors
Zekun Zhou,Xiaocheng Feng,Lei Huang,Xiachong Feng,Ziyun Song,Ruihan Chen,Liang Zhao,Weitao Ma,Yuxuan Gu,Baoxin Wang,Dayong Wu,Guoping Hu,Ting Liu,Bing Qin
### Background
研究是推动人类文明进步的基本过程，但需要大量时间和努力。近年来，人工智能技术的迅速发展促使研究人员探索如何利用AI加速和提升研究效率。为了监测这一领域的相关进展，论文进行了系统性回顾，将相关研究分为假设提出、假设验证和论文发表三个主要类别。
### Innovation
论文提出了将人工智能技术应用于研究过程的不同阶段，并进行了系统性分类，体现了在科研辅助系统中的创新应用；指出了当前研究领域面临的挑战，并探索了未来的研究方向；提供了跨领域的基准和工具概述，支持AI的进一步集成。
### Conclusion
本文旨在为初学者提供一个入门指南，并促进未来的研究。相关资源已在该网址公开提供：this https URL。
## 104. `cs.AI` - 2025年人工智能指数报告 [PDF](https://arxiv.org/pdf/2504.07139), [HTML](https://arxiv.org/abs/2504.07139)
### Authors
Nestor Maslej,Loredana Fattorini,Raymond Perrault,Yolanda Gil,Vanessa Parli,Njenga Kariuki,Emily Capstick,Anka Reuel,Erik Brynjolfsson,John Etchemendy,Katrina Ligett,Terah Lyons,James Manyika,Juan Carlos Niebles,Yoav Shoham,Russell Wald,Toby Walsh,Armin Hamrah,Lapo Santarlasci,Julia Betts Lotufo,Alexandra Rome,Andrew Shi,Sukrut Oak
### Background
自2017年作为百年人工智能研究的一个衍生项目成立以来，人工智能指数致力于为政策制定者、记者、执行人员、研究人员和公众提供准确、严格验证并全球来源的数据。人工智能指数一直在努力帮助这些利益相关者在人工智能的发展和部署方面做出更好的决策。随着人工智能在世界各地（从董事会会议室到餐桌上）被广泛讨论，这一使命从未像今天这般重要。
### Innovation
今年报告中新增了对AI硬件演变格局的深入分析，推断成本的新型估计，以及对AI出版和专利趋势的新分析。还引入了有关企业采用负责任AI实践的新数据，并扩大了对科学和医学中不断增长的AI作用的覆盖范围。
### Conclusion
人工智能指数继续在追踪和解释塑造领域的关键趋势方面处于领先地位，从地缘政治格局的转变和技术基础的快速演变，到人工智能在商业、政策制定和公共生活中的扩展作用。纵向追踪仍然是我们使命的核心。在快速发展的领域，指数提供了必要的背景信息，帮助我们理解今天人工智能的情况，它是如何演变的，以及未来可能走向何方。人工智能指数是全球公认的人工智能最权威的资源之一，被《纽约时报》、彭博社和《卫报》等重要媒体引用；在数百篇学术论文中被引用；并被全球政策制定者和政府机构使用。
## 105. `cs.AI` - DS-Span：单阶段判别子图挖掘算法用于高效图嵌入 [PDF](https://arxiv.org/pdf/2511.17419), [HTML](https://arxiv.org/abs/2511.17419)
### Authors
Yeamin Kaiser,Muhammed Tasnim Bin Anwar,Bholanath Das,Chowdhury Farhan Ahmed,Md. Tanvir Alam
### Background
图表示学习旨在将复杂的高维图结构转换为能够保持拓扑和语义特征的紧凑向量空间。子图方法提供了一种在符号模式发现和连续嵌入学习之间建立可解释联系的桥梁。然而，现有的频繁或判别子图挖掘方法往往存在冗余的多阶段管道、高昂的计算成本以及挖掘结构与其判别相关性之间的弱耦合问题。
### Innovation
作者提出了一种名为DS-Span的单阶段判别子图挖掘框架，该框架在搜索空间的一次遍历中统一了模式增长、修剪和监督驱动评分。DS-Span引入了一种覆盖率限制的资格机制，动态限制探索，直到图被充分表示为止，并采用信息增益指导的选择机制，促进具有强分类分辨能力的同时最小化冗余。这种生成的子图集可作为下游图嵌入和分类的高效、可解释基础。全面的基准测试结果表明，DS-Span相对于多阶段方法生成了更紧凑且更具判别性的子图特征，可显著减少运行时间并实现更高的或可比的准确性。
### Conclusion
实验结果突显了统一、单阶段判别挖掘作为可扩展和可解释图表示学习基础的潜力。
## 106. `cs.AI` - 通过专家教师的中间层知识蒸馏防止医学影像分析中的捷径学习 [PDF](https://arxiv.org/pdf/2511.17421), [HTML](https://arxiv.org/abs/2511.17421)
### Authors
Christopher Boland,Sotirios Tsaftaris,Sonia Dahdouh
### Background
深度学习模型在训练过程中倾向于通过错误的相关但无关的特征学习捷径解决方案，这可能导致在高风险应用场景下（如医学影像分析）模型不使用临床相关的特征进行预测，进而降低模型的鲁棒性并给患者带来潜在的危害。
### Innovation
本文提出了一种新颖的知识蒸馏框架，该框架通过在带有偏差特征的大型数据集上训练学生网络，并使用在小任务相关数据集上微调的教师网络来减轻捷径学习。该方法能够在不同的网络层中有效针对捷径学习，特别适用于在标注偏倚有限且无法提前识别捷径特征的情况下改进医学影像分析模型。
### Conclusion
通过在CheXpert、ISIC 2017和SimBA数据集上的广泛实验，本文证明了所提出的方法在各种架构（ResNet-18、AlexNet、DenseNet-121和3D CNNs）下相对于传统经验风险最小化、基于增广的偏差减轻和基于群体的偏差减轻策略的方法表现的一致性改进。在许多情况下，即使是在分布外测试数据上，该方法也能达到使用无偏差数据训练的基准模型相当甚至更好的性能。结果表明，本文的方法在标注偏倚有限的现实世界医学影像场景中具有实际应用可行性。
## 107. `cs.AI` - Meta-World+: 一个改进的标准强化学习基准 [PDF](https://arxiv.org/pdf/2505.11289), [HTML](https://arxiv.org/abs/2505.11289)
### Authors
Reginald McLean,Evangelos Chatzaroulas,Luc McCutcheon,Frank Röder,Tianhe Yu,Zhanpeng He,K.R. Zentner,Ryan Julian,J K Terry,Isaac Woungang,Nariman Farsad,Pablo Samuel Castro
### Background
Meta-World 广泛用于评估多任务和元强化学习代理的能力，这些代理需要同时掌握多种技能。然而，自其推出以来，Meta-World 有过大量未记录的变化，这阻碍了算法之间的公平比较。
### Innovation
本研究旨在从文献中区分出这些结果，同时利用Meta-World 的过去版本为多任务和元强化学习基准设计提供见解。通过这个过程，我们发布了一个新的开源版本的 Meta-World（此链接 https://），该版本具有过去的完全可重复性、更技术的易用性和给予用户更多控制选择任务集的能力。
### Conclusion
通过改进和标准化，Meta-World+ 版本旨在为多任务和元强化学习领域的研究提供更可靠和可比性的基准。
## 108. `cs.AI` - 部分可观性下的观察者感知概率规划 [PDF](https://arxiv.org/pdf/2502.10568), [HTML](https://arxiv.org/abs/2502.10568)
### Authors
Salomé Lepers,Vincent Thomas,Olivier Buffet
### Background
研究了智能体和观察者共存的规划问题，其中观察者处于部分可观测量状态，智能体必须根据这一情况制定策略以优化通过观察传输的信息。通过扩展观察者感知马尔可夫决策过程（OAMDP）以适应部分可观测性，论文提出了一种框架来处理这些问题，从而明确定义了可读性、可解释性和可预测性的性质。
### Innovation
提出了部分可观性下的观察者感知概率规划问题（PO-OAMDP），扩展了OAMDP框架。这种扩展不仅使问题更加接近现实，还允许考虑动态隐藏变量，如可预测性和目标变量可能在其执行过程中发生变化的可读性问题。
### Conclusion
探讨了PO-OAMDP的理论性质，并通过基准问题实验分析了HSVII在专用初始化下的收敛行为，最终研究了由此产生的策略。
## 109. `cs.AI` - 知识图谱中具有软实体约束的交互式查询回答 [PDF](https://arxiv.org/pdf/2508.13663), [HTML](https://arxiv.org/abs/2508.13663)
### Authors
Daniel Daza,Alberto Bernardi,Luca Costabello,Christophe Gueret,Masoud Mansoury,Michael Cochez,Martijn Schut
### Background
现有的查询回答方法主要用于从不完备的知识图谱中检索可能的答案，尤其是在由于缺少边而无法通过直接图遍历达到答案时尤为有用。然而，现有的方法主要集中在使用一阶逻辑形式化的查询上。在实际应用中，许多现实世界的查询包含了内在模糊或上下文依赖的约束，例如属性偏好或相关类别。
### Innovation
本文引入了具有软约束的查询回答问题，提出了两个新的方法，能够在不破坏原始查询答案结构的情况下，通过引入软约束来调整查询答案的得分。这些方法具有轻量级的特点，只需调整两个参数或通过少量神经网络来捕捉软约束，同时保持原始的排名结构。此外，该研究扩展了现有的问答基准数据集，以生成包含软约束的新数据集。
### Conclusion
实验结果表明，我们的方法能够捕捉软约束，同时保持稳健的查询回答性能，并且增加的额外开销很小。
## 110. `cs.AI` - 基于草图指导验证的物理感知视频生成中的规划 [PDF](https://arxiv.org/pdf/2511.17450), [HTML](https://arxiv.org/abs/2511.17450)
### Authors
Yidong Huang,Zun Wang,Han Lin,Dong-Ki Kim,Shayegan Omidshafiei,Jaehong Yoon,Yue Zhang,Mohit Bansal
### Background
近期的视频生成方法越来越多地依赖于规划中间控制信号（如物体轨迹）以提高时序连贯性和运动保真度。然而，这些方法大多依赖单次规划，这通常仅限于简单的运动；或者通过迭代细化来提高运动质量，但这种方法需要多次调用视频生成器，导致计算成本较高。
### Innovation
提出了一种无需训练、基于草图验证的规划框架，称为SketchVerify。该框架通过在完整视频生成之前引入测试时采样和验证循环，用更动态连贯的轨迹（即物理上合理且指令一致的运动）改进了运动规划质量。该方法通过视觉-语言验证器来预测并评估多个候选运动计划，该验证器联合评估语义与指令的一致性和物理合理性，从而高效地评估候选轨迹并逐步细化，直到找到一个令人满意的计划。
### Conclusion
实验在WorldModelBench和PhyWorldBench上表明，该方法在运动质量、物理真实性和长时间一致性方面显著优于竞争基线，同时效率更高。进一步的消融研究显示，增加轨迹候选者数量会持续提升整体性能。
## 111. `cs.AI` - 评价QGIS中的基于人工智能的自动地图数字化 [PDF](https://arxiv.org/pdf/2504.18777), [HTML](https://arxiv.org/abs/2504.18777)
### Authors
Diana Febrita
### Background
地图数字化是将纸质或电子地图转换为可用于进一步分析的数字格式的重要过程。传统的地图数字化需要大量的人力投入，特别是当在转换复杂的地图要素时需要进行解读和决策。随着人工智能技术的发展，利用机器学习技术进行地图数字化成为可能。Deepness是一个基于深度神经网络的AI工具，被设计并集成到QGIS应用中作为插件，旨在评估其在自动地图数字化中的效果。
### Innovation
Deepness是一款先进的AI驱动工具，在QGIS应用中作为插件使用，能够实现自动化的地图数字化。这项研究通过分析谷歌地球图像生成的AI数字化结果，并将其与OpenStreetMap的数字化输出进行比较，来评估其性能。
### Conclusion
该研究比较了Deepness生成的数字化结果与OpenStreetMap的输出，以评估其在自动地图数字化中的效果。结果显示，Deepness在处理复杂地图要素时能够提高效率和准确性。
## 112. `cs.AI` - LLMs在智能辅导系统中构建逻辑问题证明和提示的潜力与限制 [PDF](https://arxiv.org/pdf/2505.04736), [HTML](https://arxiv.org/abs/2505.04736)
### Authors
Sutapa Dey Tithi,Arun Kumar Ramesh,Clara DiMarco,Xiaoyi Tian,Nazia Alam,Kimia Fazeli,Tiffany Barnes
### Background
智能辅导系统在教授形式命题逻辑证明方面已经显示出有效性，但这些系统依赖于基于模板的解释，限制了它们为学生提供个性化反馈的能力。大型语言模型（LLMs）提供了动态反馈生成的潜力，但存在生产幻觉或解释不合适的风险。本研究通过对比六种提示技术在四个最先进的LLMs上的表现在358个命题逻辑问题上的多步骤符号逻辑证明构建步长准确性，评估LLMs在智能辅导系统中构建证明和提供解释提示的能力。
### Innovation
研究使用DeepSeek-V3取得了最高86.7%的多步骤证明构建准确性，并且在简单规则方面表现尤为出色。进一步使用表现最佳的LLM为智能逻辑辅导系统生成了解释性提示，并从四个标准的角度（准确性、一致性和清晰度）对其进行评估，发现这些提示在一致性与清晰度方面得到了人类评估者的高度评价，但在解释提示的合理性以及其上下文方面表现不佳。
### Conclusion
研究表明LLMs可用于增强具有逻辑辅导提示的智能辅导系统，但需要进一步的改进以确保准确性和教育适用性。
## 113. `cs.AI` - MSRS: 自适应多子空间表示引导用于大型语言模型的属性对齐 [PDF](https://arxiv.org/pdf/2508.10599), [HTML](https://arxiv.org/abs/2508.10599)
### Authors
Xinyan Jiang,Lin Zhang,Jiayi Zhang,Qingsong Yang,Guimin Hu,Di Wang,Lijie Hu
### Background
现有方法通过直接操控大型语言模型的内部激活来进行行为控制，但大多数方法难以同时操控多个属性，常常导致属性间的相互干扰和不可取的权衡。
### Innovation
提出了一个多子空间表示引导（MSRS）新框架，通过子空间表示微调实现有效的多属性操控。MSRS通过分配正交子空间给每个属性，避免它们在模型表示空间中的相互影响来减少属性间的干扰。此外，MSRS结合属性特定子空间和共享子空间来实现混合子空间组成策略，动态权重函数用于高效整合这些组件以实现精确控制。在推理过程中，MSRS引入了一个标记级的操控机制，可以动态识别并干预最相关的标记，以实现精细的行为调节。
### Conclusion
MSRS在多个属性上显著减少了属性冲突，超越了现有方法，并在多种下游任务中具有良好的泛化效果。
## 114. `cs.AI` - 使用多代理强化学习的LLM协作 [PDF](https://arxiv.org/pdf/2508.04652), [HTML](https://arxiv.org/abs/2508.04652)
### Authors
Shuo Liu,Tianle Chen,Zeyu Liang,Xueguang Lyu,Christopher Amato
### Background
多代理系统（MAS）在建模和解决多个相互作用的代理存在问题方面已取得大量研究成果。然而，现有的大规模语言模型（LLM）通常独立预训练，并未特别针对协作进行优化。现有的LLM微调框架依赖于个体奖励，要求为每个代理设计复杂的奖励机制以鼓励合作。
### Innovation
本文将LLM协作建模为一种协作的多代理强化学习（MARL）问题，并开发了一种多代理、多轮算法——Multi-Agent Group Relative Policy Optimization（MAGRPO），以此解决上述挑战。MAGRPO结合了当前针对LLM的RL方法和MARL技术。
### Conclusion
我们的实验表明，使用MAGRPO对MAS进行微调使代理能够通过有效的合作高效生成高质量的答案。我们的方法为使用其他MARL方法解决LLM问题开辟了途径，并揭示了相关挑战。代码可在此处获取：[链接略]。
## 115. `cs.AI` - AI能否感知物理危险并干预？ [PDF](https://arxiv.org/pdf/2509.21651), [HTML](https://arxiv.org/abs/2509.21651)
### Authors
Abhishek Jindal,Dmitry Kalashnikov,R. Alex Hofer,Oscar Chang,Divya Garikapati,Anirudha Majumdar,Pierre Sermanet,Vikas Sindhwani
### Background
当前，当AI以机器人或辅助代理的形式与物理世界互动时，会引发新的安全性挑战，超越了纯粹的“数字AI”带来的挑战。在这种交互中，物理伤害的潜在风险是直接且即时的。现有最先进的基础模型处理物理安全常识的理解能力如何？例如，模型是否能理解箱子可能太重无法提起，或不能将热咖啡杯递给儿童等常识？
### Innovation
本文的主要贡献有三点：首先，发展了一种高度可扩展的连续物理安全基准测试方法，基于实际受伤案例和操作安全限制。其次，通过利用先进的生成模型，将这些叙述和限制转化为现实感的图片和视频，捕捉从安全到不安全的状态转换，用以探查多模态安全理解。最后，开发了一种后训练范式，通过系统指令教会模型明确判断体贴式安全约束，确保生成的理解过程是解释性和透明的，并在约束满足评估中达到了最先进的性能。该基准已公开发布。
### Conclusion
本文提出了一个基于实际伤害案例和操作安全限制的高度可扩展的连续物理安全基准测试方法，并通过先进的生成模型将其转化为现实感的图片和视频，用于探查多模态安全理解能力。通过后训练范式教会模型明确判断具体的物理安全约束，获得了最先进的约束满足评估性能。
## 116. `cs.AI` - LLMs学习推理的复杂网络视角 [PDF](https://arxiv.org/pdf/2509.23629), [HTML](https://arxiv.org/abs/2509.23629)
### Authors
Sihan Hu,Xiansheng Cai,Yuan Huang,Zhiyuan Yao,Linfeng Zhang,Pan Zhang,Youjin Deng,Kun Chen
### Background
大型语言模型使用可验证奖励的强化学习（RLVR）训练表现出一些独特的和困惑的行为，这些行为目前理解不足，包括两阶段的学习曲线、响应长度的V形轨迹以及严重的灾难性遗忘现象。
### Innovation
本文提出这些行为是由在语义空间中拓扑演化的潜隐推理图的自我组织所驱动的，而不是由神经实现细节驱动的。通过将一个1.5B参数的LLM与一个最小的概念网络模型相比较，作者跟踪因果根源至一个稀疏的概念网络的自我组织，其平均度数为两。这一几何视角为观察到的异常提供了一个统一的物理解释：V形轨迹跟踪了从并行局部技能优化到全局网络整合的演变过程；灾难性遗忘源自关键“主干”边在拓扑上的分叉；而策略崩溃则源于在网络叶片节点积累的序列转换导致的广泛探索在突然冻结为固定的、高奖励的轨迹。作者还提出了一种名为Annealed-RLVR的原理性算法，通过在训练过程中引入目标提示微调（SFT）‘加热’步骤来解决这一拓扑瓶颈。
### Conclusion
通过将RLVR从黑盒优化重新构想为一个可预测的过程，我们的研究提供了一种新的物理直觉，用于工程未来AI系统的涌现推理能力。实验结果显示，与标准RLVR相比，这一理论驱动的干预措施在分布内和分布外基准测试中均表现出更优的性能，包括Minerva和AIME。
## 117. `cs.AI` - ResearStudio：一种可人工干预的可控深度研究代理构建框架 [PDF](https://arxiv.org/pdf/2510.12194), [HTML](https://arxiv.org/abs/2510.12194)
### Authors
Linyi Yang,Yixuan Weng
### Background
当前的深度研究代理运行在'一次性启动后无需干预'模式下：一旦启动，它们就无法在执行过程中修正错误或添加专家知识。ResearStudio是首个将实时人工控制置于核心位置的开源框架。
### Innovation
ResearStudio采用协作工作室设计，其中分层规划者-执行者将每一步写入实时的'计划文档'，并通过快速通信层将每个操作、文件变化和工具调用流式传输到网页界面。用户可以在任何时间暂停运行、编辑计划或代码、运行自定义命令并恢复，从而在AI主导、人类辅助和人类主导、AI辅助的不同模式之间平滑切换。
### Conclusion
在完全自主模式下，ResearStudio在GAIA基准测试中达到了尖端结果，超越了如OpenAI的DeepResearch和Manus等系统。这些结果表明，强大的自动化性能与细粒度的人工控制可以共存。全文代码、协议和评估脚本可在该链接处获取，我们还会继续更新存储库以鼓励进一步的工作，并支持深科学家的开发，可以在此链接处访问。
## 118. `cs.AI` - 柏拉图式的表示：贫困测绘中的统一视觉-语言编码或代理引发的独特性？ [PDF](https://arxiv.org/pdf/2508.01109), [HTML](https://arxiv.org/abs/2508.01109)
### Authors
Satiyabooshan Murugaboopathy,Connor T. Jerzak,Adel Daoud
### Background
该研究探讨了家庭财富等社会经济指标在网络卫片（捕捉物理特征）和互联网文本（反映历史/经济叙事）中的可恢复印记。使用非洲社区的民权及健康调查（DHS）数据，研究将Landsat影像与带有关置/年份条件的大型语言模型（LLM）生成的文本描述以及AI代理从网络来源检索的文本结合。研究开发了一个多模态框架来预测国际财富指数，并通过五个管道来实现：卫星图像的视觉模型，仅使用位置/年份的LLM，AI代理搜索/合成网页文本，图像-文本联合编码器，以及所有信号的集成。
### Innovation
研究的三个贡献包括，融合视觉和代理/LLM文本在财富预测中优于仅视觉的基线（例如，在外部样本划分中的决定系数R-squared达到0.77 vs. 0.63），表明LLM内部知识比代理检索的文本更为有效，增强了跨国家和时间推广的稳健性；发现部分表征收敛：融合的视觉/语言模式嵌入在对齐后中等程度相关（中位余弦相似度为0.60），表明材料福祉的共享潜在代码，但保留了互补细节；尽管仅依赖于LLM文本的表现优于代理检索的数据，在部分划分中将代理数据结合产生的微小收益支持代理收集的信息引入了未被静态LLM知识完全捕捉的独特表征。
### Conclusion
本框架提供了一个大规模的多模态数据集，包括超过60,000个DHS聚类，链接到卫星图像、LLM生成的描述以及代理检索的文本。这项工作表明，在贫困测绘中，统一的视觉-语言编码可能与代理引发的独特性共存，未来将继续探索两种机制之间的关系。
## 119. `cs.AI` - 多代理协作性奖励设计以增强强化学习中的推理 [PDF](https://arxiv.org/pdf/2511.16202), [HTML](https://arxiv.org/abs/2511.16202)
### Authors
Pei Yang,Ke Zhang,Ji Wang,Xiao Chen,Yuxin Tang,Eric Yang,Lynn Ai,Bill Shi
### Background
传统的单个黑箱奖励模型难以同时优化多个有时相互冲突的偏好维度（如事实准确性、有用性和安全性），并且缺乏透明度以解释评分的原因。这些限制使得在强化学习人类反馈（RLHF）中实现鲁棒性和可解释性变得困难。
### Innovation
我们提出了CRM（多代理协作奖励模型）框架，使用协调的专家评价团队取代单一的黑箱奖励模型。CRM通过将偏好评估分解为领域特定的代理和全局评价者（例如基于排名和嵌入相似度的奖励），解决了这些问题。中央聚合器在每个时间步骤中融合这些信号，平衡因素如步骤正确性、多代理一致性以及重复惩罚，从而生成一个与标准强化学习管道兼容的单个训练奖励。通过这种方式，CRM提供了多视角的奖励塑造，无需额外的人工标注。
### Conclusion
CRM和rewardBench一起提供了一条实现更透明奖励建模和更稳定优化的实用和模块化路径。
## 120. `cs.AI` - CharCom：用于多角色故事插画的可组合身份控制 [PDF](https://arxiv.org/pdf/2510.10135), [HTML](https://arxiv.org/abs/2510.10135)
### Authors
Zhongsheng Wang,Ming Lin,Zhedong Lin,Yaser Shakib,Qian Liu,Jiamou Liu
### Background
在基于扩散的文本到图像生成中，保持角色身份一致性仍然是一个基本的限制。
### Innovation
提出了CharCom框架，这是一个模块化且参数效率高的框架，通过组合可调适的LoRA适配器实现角色一致的故事插画，使得在不重新训练基模型的情况下能够高效地进行单角色定制。CharCom基于冻结的扩散基础架构，在推理时使用提示感知控制动态组合适配器。实验结果表明，CharCom显著提高了角色保真度、语义对齐和时间连贯性，对于拥挤场景依然稳健，并能够以最小的开销实现多角色生成，使其适用于故事插画和动画等实际应用。
### Conclusion
CharCom框架使得多角色故事插画的能力显著提高，并且在实际应用中具有很高的灵活性和效率。
## 121. `cs.AI` - 你只需正向传播一次：一种高效组合评判范式 [PDF](https://arxiv.org/pdf/2511.16600), [HTML](https://arxiv.org/abs/2511.16600)
### Authors
Tianlong Zhang,Hongwei Xue,Shilin Yan,Di Wu,Chen Xu,Yunyun Yang
### Background
多模态大语言模型（MLLMs）在担任评判员方面显示出强大的潜力。然而，现存的方法面临着基本的取舍：将MLLMs调整为输出单一分数与MLLMs的生成性质相矛盾，限制了对细粒度需求理解的能力；而自回归地生成评判分析则在高通量场景下极其缓慢。
### Innovation
提出了一种模板条件下的方法YOFO，它能够在单一正向传递中评判所有要求。基于自回归模型，YOFO接受一个结构化要求模板，并在一个推理步骤中，通过阅读与该要求相关最终标记的logits来为每个要求生成二元是/否的决策。此设计带来了数量级的速度提升，同时保持可解释性。
### Conclusion
广泛实验证明YOFO不仅在标准推荐数据集上达到最先进的性能，还能支持后向依赖分析，即后续判断基于先前判断，并且可以从后进行解释性的思考（CoT）。
## 122. `cs.AI` - 使用掩蔽和重排自我监督的可验证奖励强化学习 [PDF](https://arxiv.org/pdf/2511.17473), [HTML](https://arxiv.org/abs/2511.17473)
### Authors
Zhen Wang,Zhifeng Gao,Guolin Ke
### Background
现有的测试时间缩放方法能够显著提升大型语言模型（LLMs）的数学推理能力。但是，在处理数学命题证明等数据时，奖励学习与验证（RLVR）的可扩展性受限。因为这类任务需要中间推理，但最终答案却很难直接可靠地验证。此外，基于标记级的强化学习微调（SFT）常常导致模型记忆知识点而非形成完整的思考链。因此，本文基于BERT的自我监督任务，提出了一种名为MR-RLVR的方案，通过“掩蔽再填充”和“步骤重排”来提取中间推理中的可学习信号。
### Innovation
本文提出了一种新的方案MR-RLVR，该方案通过将自我监督训练与基于验证奖励的强化学习相结合，利用任务中提取的中间推理信号来增强模型的可扩展性和性能。具体来说，MR-RLVR首先使用自我监督训练处理部分数学计算和证明数据，然后使用仅结果可验证的数学计算数据集进行强化学习微调。
### Conclusion
在固定样本和解码预算的条件下，MR-RLVR在提高RLVR稳定性与性能的同时，实现了对原始RLVR在通过率方面有明显的提升：平均相对提高1%的Pass@1，5.27%的Pass@5以及4.00%的Pass@8。实验结果证明，引入过程感知的自我监督信号对增强RLVR的可扩展性和性能具有显著效果。
## 123. `cs.AI` - 具备SU($d$)对称性的超多项式量子加速的协变量子算法 [PDF](https://arxiv.org/pdf/2207.07250), [HTML](https://arxiv.org/abs/2207.07250)
### Authors
Han Zheng,Zimu Li,Sergii Strelchuk,Risi Kondor,Junyu Liu
### Background
本文介绍了一种应用于物理系统中具有任意SU$(d)$对称性的机器学习任务的协变卷积量子算法框架。这种框架使我们能够改进一种自然的量子计算模型——调换量子计算(PQC)，并定义了一个更强大的模型：PQC+。虽然PQC已被证明可以高效地经典模拟，但是我们展示了一个能够高效解决在PQC+机器上问题，但在经典计算机上没有已知的多项式时间算法，从而提供了PQC+不能被经典模拟的证据。
### Innovation
提出了适用于具有任意SU$(d)$对称性的物理系统中若干机器学习任务的协变卷积量子算法框架。定义了PQC+模型，该模型比PQC更加强大。相对于PQC，PQC+能够在经典计算机上无法高效解决的问题上实现高效解决，为PQC+不能经典模拟提供了证据。
### Conclusion
讨论了可以在PQC+范式下执行的实际量子机器学习算法。PQC+框架为量子机器学习任务提供了一种新的解决思路和更强的能力。
## 124. `cs.AI` - MiniLLM: 大型语言模型的知识蒸馏 [PDF](https://arxiv.org/pdf/2306.08543), [HTML](https://arxiv.org/abs/2306.08543)
### Authors
Yuxian Gu,Li Dong,Furu Wei,Minlie Huang
### Background
知识蒸馏（KD）是一种减少大型语言模型（LLMs）高计算需求的技术。然而，先前的KD方法主要应用于白盒分类模型或训练小型模型以模仿像ChatGPT这样的黑盒模型API。如何有效地将白盒LLMs的知识传递给小型模型仍然较少被研究，随着开源LLMs的快速发展，这一问题变得尤为重要。
### Innovation
本文提出了一种新的KD方法，将白盒LLMs转换为较小的语言模型。首先，替换标准KD方法中的前向Kullback-Leibler散度（KLD）目标为后向KLD目标，这更适合于生成语言模型的KD，以防止学生模型过度估计教师分布的低概率区域。然后，推导出一种有效的策略优化方法来学习这个目标。此外，该方法适用于不同模型家族的120M到13B参数。实验证明，MiniLLM在指令跟随设置中生成更精确的回答，具有更高的整体质量、更低的信息偏见、更好的校准和更长文本生成性能。
### Conclusion
我们的方法可以应用于各种不同参数量的模型，实验结果显示MiniLLM在指令跟随设置中的性能优越。我们的代码、数据和模型检查点可以在提供的链接找到。
## 125. `cs.AI` - 结构化辩论在金融AI中的企业信用推理改善 [PDF](https://arxiv.org/pdf/2510.17108), [HTML](https://arxiv.org/abs/2510.17108)
### Authors
Yoonjin Lee,Munhee Kim,Hanbi Choi,Juhyeon Park,Seungho Lyoo,Woojin Park
### Background
尽管金融AI取得了进步，企业在信用评估中的基于证据的推理自动化仍然未得到解决。非财务定性指标在贷款还款结果中起着决定性作用，但难以正式化。现有方法主要集中在数字预测上，未能充分支持专业贷款评估所需的解释性判断。
### Innovation
开发并评估了两种大型语言模型（LLM）基于的系统，以从非财务证据中生成结构化的推理分析。分别是一个非对抗性的单代理系统（NAS）和一个以卡尔·波普尔的批判性对话为基础的多代理系统（KPD-MADS），通过十步结构化互动协议进行对抗性验证，并且都应用于三个真实的企业案例，得到了经验丰富的信贷风险专业人员的评价。
### Conclusion
与手动专家报告相比，两种系统均实现了显著的生产率提升，且KPD-MADS在解释充分性、实践适用性和易用性方面优于人工基准。这些发现表明，结构化多代理互动可以增强金融AI中的推理严谨性和可解释性，在企业信用评估中的自动化方面取得了可扩展和可信的进步。
## 126. `cs.AI` - RTMol：从循环视角重新思考分子-文本对齐 [PDF](https://arxiv.org/pdf/2511.12135), [HTML](https://arxiv.org/abs/2511.12135)
### Authors
Letian Chen,Runhan Shi,Gufeng Yu,Yang Yang
### Background
分子序列表示（如SMILES表示）与文本描述的对齐对于药物发现、材料设计和自动化化学文献分析等应用至关重要。现有方法通常将分子标注（分子到文本）和基于文本的分子设计（文本到分子）作为独立任务处理，依赖于有监督的微调或对比学习管道。然而，这些方法面临几个关键挑战：（i）传统评估指标如BLEU注重语言流畅性而忽视化学准确性；（ii）训练数据集经常包含化学含义模糊且不完整的叙述描述；（iii）生成方向的独立优化导致双向不一致性。
### Innovation
提出了RTMol，一种双向对齐框架，通过自我监督的往返学习将分子标注和文本到SMILES生成统一起来。框架引入了新颖的往返评估指标，并使分子标注的无监督训练不需要成对的分子-文本语料库。实验证明，RTMol在各种大型语言模型上的双向对齐性能提高了47%，建立了联合分子-文本理解和生成的有效范式。
### Conclusion
RTMol通过自我监督的往返学习提升了双向对齐性能，并且不需要成对的分子-文本数据集，有效解决了现有方法面临的三个关键问题，为联合分子-文本理解和生成提供了有效范式。
## 127. `cs.AI` - 危险中的帖子：检测文本中的危害信息 [PDF](https://arxiv.org/pdf/2405.17838), [HTML](https://arxiv.org/abs/2405.17838)
### Authors
Keith Burghardt,Daniel M.T. Fessler,Chyna Tang,Anne Pisor,Kristina Lerman
### Background
研究情感相关现象（如情绪或情感）的社会语言学指标通常是从文本中提取出来的，以更好地了解人机交互的特点，包括社交媒体上的交流。然而，一个常常被忽略的指标是有关危害或风险的信息存在与否。本文旨在开发一个新的模型，用于检测此类信息，并指出该模型不仅表现良好（优于词典方法等），而且提取的危害信息与常见的其他指标关联性不强。
### Innovation
作者开发了一个新的模型来检测文本中的危害信息，该模型是在一个新的注释帖子集合上进行训练的。研究表明，该模型不仅表现良好，且提取的危害信息与常用指标关联性不强。此外，该研究还展示了该工具的应用价值，并分析了信息战环境中危害信息的作用。
### Conclusion
在两个关于重要地缘政治事件的数据集中（以以色列-哈马斯战争和2022年法国全国选举为例），发现了关于冲突的危害信息较为常见。研究还发现代表冲突中较弱一方观点的无机账号经常讨论民众的危害，可能为了争取援助。此外，这些危险信息被提到的频率与有机账户有显著差异，反映了信息操作者为了战略目的重新塑造给定地缘政治事件的方式。这些结果是探索信息战争环境中的危害信息的第一步。该研究已将模型作为Python包分享，供研究人员和记者分析危害内容。
## 128. `cs.AI` - CATCODER: 利用相关代码和类型上下文的仓库层级代码生成 [PDF](https://arxiv.org/pdf/2406.03283), [HTML](https://arxiv.org/abs/2406.03283)
### Authors
Zhiyuan Pan,Xing Hu,Xin Xia,Xiaohu Yang
### Background
大型语言模型在代码生成任务中已经显示出卓越的能力，但在仓库级别的代码生成任务中依然存在独特挑战，尤其是需要利用仓库中分散在多个文件中的信息。成功的生成依赖于对一般性和具体性知识的深刻理解。虽然大型语言模型广泛用于一般性知识的生成，但现有的检索方法有时会受限于获得广泛的和深入的仓库上下文。
### Innovation
提出了CatCoder，这是一种针对静态类型编程语言的新型代码生成框架。CatCoder通过集成相关代码和类型上下文来增强仓库级别的代码生成。具体来说，CatCoder利用静态分析器提取类型依赖关系，并将此信息与检索到的代码合并，为语言模型生成全面的提示。通过199个Java任务和90个Rust任务构建基准，结果显示CatCoder在编译成功率（compile@k）和通过率（pass@k）上分别比RepoCoder基线高出14.44%和17.35%，并且在不同语言模型中表现一致，突出CatCoder的实用性。
### Conclusion
CatCoder在各种语言模型中的测试表明，它在所有模型中都表现出一致的性能提升，突显了其实用性。此外，还评估了CatCoder在大型开源仓库中的时间消耗，结果证明了CatCoder的可扩展性。
## 129. `cs.AI` - 协作网络架构：学习结构化网络作为感觉模式的表示 [PDF](https://arxiv.org/pdf/2407.05650), [HTML](https://arxiv.org/abs/2407.05650)
### Authors
Pascal J. Sager,Jan M. Deriu,Benjamin F. Grewe,Thilo Stadelmann,Christoph von der Malsburg
### Background
当前的视觉系统面临噪音、变形和对未见过的数据泛化的挑战。
### Innovation
提出了协作网络架构（CNA），使用神经元结构化的、递归连接的网络表示传感器信号，学习自感官输入中的统计规律，动态组装重叠的网络片段，从而实现对噪音的鲁棒性、变形适应性和对未见过的数据的泛化。
### Conclusion
研究表明，在没有监督的情况下可以学习网络片段，并且能够灵活重组以编码新的模式，实现图形单元完成和对噪音的抵抗力。研究确认CNA为将局部特征处理与全局结构形成集成的神经表示的有前途的范式，为未来的不变物体识别研究奠定了基础。
## 130. `cs.AI` - 使用扩散语言模型的面向文本的多属性分子优化 [PDF](https://arxiv.org/pdf/2410.13597), [HTML](https://arxiv.org/abs/2410.13597)
### Authors
Yida Xiong,Kun Li,Jiameng Chen,Hongzhi Zhang,Di Lin,Yan Che,Wenbin Hu
### Background
分子优化（MO）是药物发现过程中的关键步骤，其中任务导向生成的分子被优化以满足实际的工业需求。现有的主流MO方法主要利用外部属性预测器来指导迭代的属性优化。然而，根据化学空间的巨大性，预测器无法学习所有分子样本，因此在属性预测过程中不可避免地引入了错误和噪声，导致属性预测的误差累积、泛化能力降低和次优的分子候选物。
### Innovation
本文提出了一种基于文本指导的多属性分子优化方法，采用基于变换器的扩散语言模型（TransDLM）。TransDLM利用标准化的化学命名法作为分子的语义表示，并隐式地将属性要求嵌入到文本描述中，从而在扩散过程中减少错误传播。通过将物理和化学细节的文本语义与专门的分子表示融合，TransDLM有效整合了多种信息源，从而指导精确优化，提高了模型在结构保留和属性增强方面的能力平衡。
### Conclusion
实验结果表明，我们的方法在基准数据集上优于最先进的方法，在保持分子结构相似性和增强化学属性方面均有显著表现。
## 131. `cs.AI` - KRAL: 知识和推理增强学习在LLM辅助临床抗菌治疗中的应用 [PDF](https://arxiv.org/pdf/2511.15974), [HTML](https://arxiv.org/abs/2511.15974)
### Authors
Zhe Li,Yehan Qiu,Yujie Chen,Xiang Zhou
### Background
临床抗菌治疗需要动态整合病原体特征、宿主因素、抗菌药物的药理特性和感染的严重程度。这种复杂性给大型语言模型（LLMs）在高风险临床决策中的应用带来了根本性的限制，包括知识差距、数据隐私问题、高昂的部署成本和有限的推理能力。
### Innovation
提出了一种低成本、可扩展、隐私保护的KRAL（知识和推理增强学习）范式，该范式利用教师模型的推理来自动提取知识和推理轨迹，通过问题-答案逆生成；采用启发式学习进行半监督数据增强（减少约80%的手动注释需求）；利用代理强化学习同时增强医学知识和推理能力，并优化计算和内存效率。一种层次化的评估方法减少了评估成本，模块化接口设计促进了系统的无缝更新。
### Conclusion
实验结果表明，KRAL 显著优于传统的检索增强生成（RAG）和监督微调（SFT）方法。它提高了知识问题回答能力（在外部开源基准 MEDQA 中的 Accuracy@1 增加了 1.8% 对比 SFT 和 3.6% 对比 RAG），并提高了推理能力（在外部基准 PUMCH Antimicrobial 中的 Pass@1 增加了 27% 对比 SFT 和 27.2% 对比 RAG），并且实现的长期训练成本约为 SFT 的 20%。这确立了 KRAL 作为增强本地 LLM 临床诊断能力的有效解决方案，并使其能够在复杂医疗决策支持中以低成本实现高安全性部署。
## 132. `cs.AI` - FaCells. 教授机器线条语言：面向点的面部素描分类属性得分 [PDF](https://arxiv.org/pdf/2102.11361), [HTML](https://arxiv.org/abs/2102.11361)
### Authors
Xavier Ignacio Gonzalez
### Background
该研究利用了面部识别模型内部的工作原理，将这些复杂模型的内部表示转化为基于线条的艺术作品。研究以CelebA数据集中的260,000张对齐的人脸照片为对象，通过矢量素描将其转换为XY绘图器适用的形式。研究者试图通过这种转换探究模型内部的工作机制，并通过序列模型的训练预测面部属性。
### Innovation
该方法创新地将模型内部的表示转化为线性艺术作品，并对比了绝对坐标与相对坐标编码、随机顺序与旅行距离最小化顺序编码的不同效果。研究采用双向LSTM模型进行属性预测，并提出了FaCells的概念，这是一种基于特定阈值对属性进行统计抽象的新方法，通过这种方式生成的新作品既能作为解释模型可解释性的工具，又能作为可复现性和低成本的创作作品。
### Conclusion
研究结论表明，使用绝对坐标与旅行距离最小化顺序编码以及全局平均读取配置效果最佳。多标签训练稳固可行，超过50%平衡准确率的属性将被可视化为FaCells。该方法不仅为理解和解释复杂的机器学习模型提供了一种新颖的方法，还展示了这种技术在艺术创作中的应用潜力。
## 133. `cs.AI` - 采用可扩展的谱神经网络方法估计全局输入相关性和强制稀疏表示 [PDF](https://arxiv.org/pdf/2406.01183), [HTML](https://arxiv.org/abs/2406.01183)
### Authors
Lorenzo Chicchi,Lorenzo Buffoni,Diego Febbe,Lorenzo Giambagli,Raffaele Marino,Duccio Fanelli
### Background
在机器学习实践中，识别相关输入特征是非常有用的。通过隔离按重要性排序的关键输入元素，可以更清楚地了解决策过程。本文介绍了一种新颖的方法，通过利用优化过程的谱重构来估计深度神经网络中的输入组件的重要性。这种方法自动完成基于网络训练的谱特征排名，无需额外处理。利用特征值的正则化还可以强制使用输入组件的最小子集，从而提高模型的可解释性并提供稀疏的输入表示。
### Innovation
提出了一种新颖的方法，通过利用优化过程的谱重构来估计深度神经网络中的输入组件的重要性。这个方法以网络训练的副产品形式自动完成输入节点相关性的排序，并通过特征值的正则化迫使使用输入组件的最小子集，从而提高模型的可解释性和稀疏性。
### Conclusion
该技术与文献中最常见的方法进行了比较，并且成功地对合成和真实数据进行了挑战。
## 134. `cs.AI` - AV-Lip-Sync+: 利用AV-HuBERT发掘多模态不一致性检测前方人脸视频的换脸技术 [PDF](https://arxiv.org/pdf/2311.02733), [HTML](https://arxiv.org/abs/2311.02733)
### Authors
Sahibzada Adil Shahzad,Ammarah Hashmi,Yan-Tsung Peng,Yu Tsao,Hsin-Min Wang
### Background
多模态换脸技术（也称为音频-视觉深度假造）使得单一模态的深度假造检测器难以发现多媒体内容中的伪造。及时检测虚假宣传和假新闻至关重要。单一模态（即视觉或音频）的任何损坏只能通过同时利用两者信息的多模态模型来发现。以往方法主要采用单一模态视频取证，并依赖监督预训练进行伪造检测。
### Innovation
本研究提出了一种基于多模态自我监督学习（SSL）特征提取器的新方法，用于通过利用音频和视觉模态之间的不一致性进行多模态视频伪造检测。利用基于Transformer的SSL预训练Audio-Visual HuBERT (AV-HuBERT)模型作为视听特征提取器，并使用多尺度时域卷积神经网络来捕捉视听模态之间的时序关联。此外，由于AV-HuBERT仅从唇部区域提取视觉特征，还采用基于Transformer的视频模型来利用面部特征并捕获换脸过程中产生的空间和时间上的伪影。
### Conclusion
实验结果显示我们的模型优于所有现有模型，并在FakeAVCeleb和DeepfakeTIMIT数据集上达到了新的最佳性能。
## 135. `cs.AI` - 生成型人工智能与全球教育中的权力失衡：减少偏见的框架 [PDF](https://arxiv.org/pdf/2406.02966), [HTML](https://arxiv.org/abs/2406.02966)
### Authors
Matthew Nyaaba,Alyson Wright,Gyu Lim Choi
### Background
该研究探讨了生成型人工智能在教育中如何重现全球权力等级结构，并提出了解决由此产生不平等问题的框架。研究采用了批判性质性设计方法，对两套领先的系统进行了零样本提示测试，并收集了来自全球北半球和南半球的实际输出。研究结果显示，生成型人工智能在六方面加剧了西方主导地位，包括课程设置中的西方中心论假设、文化刻板印象、偏向西方的示例、对于非西方语言的有限支持、非西方身份表征不足以及与订阅模式相关的访问障碍。
### Innovation
研究提出了一种双重路径缓解模型。包括：包容性人工智能设计路径，涵盖解放性的设计方法、预防代表危害的先见之明的方法及支持本地参与的数据主权的分散生成型人工智能枢纽；教育实践路径，以人为本的提示工程训练教育者情境化提示并批判性地与输出进行互动。这一模型使生成型人工智能成为支持更加公平和文化响应教育的工具。
### Conclusion
研究结论指出，生成型人工智能不仅提供了新的教育机会，也固化了西方主导的不平衡，提出双路径模型来加以缓解，旨在通过解放性的设计方法和人性化的提示工程提升教育平等性和文化适应性。
## 136. `cs.AI` - MonoKAN：认证单增柯莫洛夫-阿诺德网络 [PDF](https://arxiv.org/pdf/2409.11078), [HTML](https://arxiv.org/abs/2409.11078)
### Authors
Alejandro Polo-Molina,David Alfaya,Jose Portela
### Background
人工神经网络（ANNs）在模式识别和复杂问题解决方面取得了显著进展，但其透明度不足仍然是一个重要挑战，尤其是在需要透明度和问责制的应用场景中。因此，通过可解释人工智能（XAI）来解释ANN的工作原理成为研究热点。然而，可解释性本身常常是不够的，模型预测需要符合专家设定的要求，这通常由部分单调性约束体现。尽管文献中已有针对传统多层感知机（MLPs）的单调性方法，但在保证可解释性和认证部分单调性方面仍存在问题。基于此，Kolmogorov-Arnold神经网络（KAN）架构因其基于可学习激活函数的样条参数化而被视为一种更可解释的MLPs替代方案。基于此，本文提出了一种新型的ANN架构——MonoKAN，该架构基于KAN结构，实现了认证的部分单调性和增强的可解释性。
### Innovation
MonoKAN架构通过采用三次Hermite样条来获得部分单调性保证，并通过在样条线性组合中使用正值权重来确保输入和输出之间保持单调关系。与现有的单调MLPs方法相比，MonoKAN不仅提高了可解释性，还在大多数基准测试中提高了预测性能。
### Conclusion
MonoKAN架构通过采用三次Hermite样条确保了部分单调性，并通过正值权重的使用保持了输入与输出之间的单调关系。实验结果表明，MonoKAN不仅提高了模型的可解释性，还在多种基准测试中优于最先进的单调MLPs方法，提升了预测性能。
## 137. `cs.AI` - LLM-Agent-UMF：基于LLM的全模块化核心代理架构统一建模框架 [PDF](https://arxiv.org/pdf/2409.11393), [HTML](https://arxiv.org/abs/2409.11393)
### Authors
Amine Ben Hassouna,Hana Chaari,Ines Belhaj
### Background
在大数据时代，需要更高级的AI系统来智能融合和分析多种来源的数据。当前的技术和增强方法未使用统一的软件架构，导致缺乏模块化和术语一致性。现有方法未明确区分LLM代理的不同组件，特别是安全模块经常被忽视。
### Innovation
提出了一个名为LLM-Agent-UMF的新型统一建模框架，该框架从功能和软件架构两方面为代理开发建立了一块明确的基础。框架区分了LLM、工具和核心代理组件，其中核心代理通过五个模块（规划、记忆、个人档案、行动和安全）发挥中心协调作用，且将核心代理区分为被动型和主动型，并提出了多种核心代理架构相结合的方式来应对复杂的任务。
### Conclusion
通过将框架应用于13个最先进的代理，验证了其与功能的对齐，并澄清了被忽视的架构方面。进一步通过设计新的代理架构，评估了框架的五个架构变体，以实现特定目标。
## 138. `cs.AI` - AeroVerse: UAV-Agent 基准套件，用于模拟、预训练、微调和评估航空航天实体世界模型 [PDF](https://arxiv.org/pdf/2408.15511), [HTML](https://arxiv.org/abs/2408.15511)
### Authors
Fanglong Yao,Yuanchang Yue,Youzhi Liu,Xian Sun,Kun Fu
### Background
航空航天嵌入式智能旨在使无人机和其他航空航天平台实现自主感知、认知和行为，并实现以自我为中心的人类和环境互动。目前，已有的嵌入式世界模型主要关注于室内场景的地面上智能代理，而无人机智能代理的研究仍处于空白状态。因此，本研究建立了第一个大规模的真实世界图像-文本预训练数据集AerialAgent-Ego10k，用于从第一人称视角描述城市无人机，同时创建了一个虚拟图像-文本-姿态对齐数据集CyberAgent Ego500k，以促进航空航天嵌入式世界模型的预训练。
### Innovation
本研究首次清晰定义了5个下游任务，包括航空航天嵌入式场景感知、空间推理、导航探索、任务规划和运动决策，并构建了相应的指令数据集，用于精细调整航空航天嵌入式世界模型。此外，该研究开发了SkyAgentEval，基于GPT-4的下游任务评估指标，全面、灵活、客观评估结果，揭示了2D/3D视觉语言模型在无人机-代理任务中的潜力与局限。研究团队整合了超过10个2D/3D视觉语言模型、2个预训练数据集、5个微调数据集以及超过10个评估指标和模拟器，构建了用于促进航空航天嵌入式智能探索和发展的基准套件AeroVerse。
### Conclusion
该基准套件包括一个广泛的功能集合，即超过10个2D/3D视觉语言模型、2个预训练数据集、5个微调数据集、超过10个评估指标和模拟器。旨在向社区公开，促进航空航天嵌入式智能的研究和开发。
## 139. `cs.AI` - Reason2Attack: 利用LLM推理破解文本到图像模型 [PDF](https://arxiv.org/pdf/2503.17987), [HTML](https://arxiv.org/abs/2503.17987)
### Authors
Chenyu Zhang,Lanjun Wang,Yiwen Ma,Wenhui Li,An-An Liu
### Background
文本到图像(T2I)模型通常部署安全过滤器以防止生成敏感图像。然而，近期的监狱突破攻击方法通过手动设计指令让LLM生成对抗性提示，从而有效绕过了安全过滤器的同时产生了敏感图像，揭示了T2I模型的安全漏洞。但由于LLM对T2I模型及其安全过滤器的理解有限，现有方法需要大量查询才能实现攻击，限制了其实用性。
### Innovation
我们提出Reason2Attack(R2A)，旨在通过将监狱突破攻击纳入LLM训练后流程中，增强LLM生成对抗性提示的推理能力。具体来说，我们首先基于Frame Semantics提出了一个CoT示例综合管道，通过识别相关术语和相应的背景插图生成对抗性提示。然后，我们通过强化学习过程中的攻击任务优化LLM，并设计了考虑提示长度、隐秘性和有效性等因素的攻击过程奖励，以进一步提高推理准确性。
### Conclusion
通过对各种T2I模型的广泛实验，R2A实现了更高的攻击成功率，同时需要较少的查询次数。此外，我们的对抗提示在开源和商用T2I模型之间具有强大的攻击可移植性。
## 140. `cs.AI` - ISS-Geo142：国际空间站宇航员摄影地理定位基准 [PDF](https://arxiv.org/pdf/2504.21194), [HTML](https://arxiv.org/abs/2504.21194)
### Authors
Vedika Srivastava,Hemant Kumar Singh,Jaisal Singh
### Background
虽然从国际空间站（ISS）捕获的照片拍摄时间的位置是精确已知的，但照片中所展示的具体地球位置通常没有直接的地理参考信息，这使得自动化地理定位变得较为复杂。论文引入了ISS-Geo142，这是一个由142张图片及其元数据和手动确定的地理位置组成的基准数据集，涵盖了不同空间范围和场景类型。
### Innovation
论文实现了并评估了三个地理定位管道：基于神经网络的方法（NN-Geo）、基于尺度不变特征变换（SIFT）的方法（SIFT-Match）和拥有视觉能力的GPT-4模型驱动的人工智能系统（TerraByte），分别在ISS-Geo142数据集上进行了评估。
### Conclusion
这些方法和实验最初是在2023年开发的，本文是对原有工作的修订和扩展版本，适应了后续在跨视图地理定位和远程传感视觉-语言模型方面的发展。ISS-Geo142和这三个管道为未来ISS图像地理定位工作提供了具体的、具有历史背景的基准。
## 141. `cs.AI` - 水管理中的多目标强化学习 [PDF](https://arxiv.org/pdf/2505.01094), [HTML](https://arxiv.org/abs/2505.01094)
### Authors
Zuzanna Osika,Roxana Rădulescu,Jazmin Zatarain Salazar,Frans Oliehoek,Pradeep K. Murukannaiah
### Background
许多现实世界的问题（例如资源管理、自主驾驶、新药发现）需要同时优化多个互相冲突的目标。多目标强化学习（MORL）将经典强化学习扩展至能够同时处理多个目标，从而生成能够捕捉各种权衡的策略。然而，该领域的研究缺乏复杂的、现实的环境和基准，这对于评估现有方法的实际应用能力至关重要。
### Innovation
本文引入了一个关于尼罗河流域水资源管理的多目标强化学习（MORL）案例研究，并将其建模为一个MORL环境，从而在该环境中对现有MORL算法进行基准研究。本文的结果表明特定的水资源管理方法在应对现实场景中的问题时表现出色，这凸显出目前MORL算法在实际应用中面临的大规模扩展挑战。
### Conclusion
基于水管理案例的研究表明，特定的资源管理方法比现有的MORL方法更有效，在实际应用场景中，MORL算法面临着大规模扩展的挑战。
## 142. `cs.AI` - 将视觉对齐语言：无标注的多模态知识图构建以增强大语言模型的推理 [PDF](https://arxiv.org/pdf/2503.12972), [HTML](https://arxiv.org/abs/2503.12972)
### Authors
Junming Liu,Siyuan Meng,Yanting Gao,Song Mao,Pinlong Cai,Guohang Yan,Yirong Chen,Zilin Bian,Ding Wang,Botian Shi
### Background
大语言模型（LLMs）在多模态推理中遇到知识不完整和幻觉问题，仅部分通过文本知识图谱（KGs）得到缓解，因为KGs在模态间隔离。虽然多模态知识图谱（MMKGs）可以提高跨模态理解，但由于手动文本注释的语义狭窄和视觉语义实体链接中的固有噪音，其实际构建受到了阻碍。
### Innovation
本文提出了Vision-align-to-Language集成知识图（VaLiK），这是一种构建MMKGs的新型方法，通过跨模态信息补充增强LLMs的推理能力。具体来说，作者使用预训练的视觉-语言模型（VLMs）将图像特征与文本对齐，并将这些图像特征转换成描述，其中包含了具体的图像信息。同时，该方法还发展了一种跨模态相似性验证机制来量化语义一致性，有效过滤了特征对齐过程中引入的噪音。即使没有手动标注的图像描述，经过精炼的描述也足以构建MMKGs。与传统的MMKGs构建方法相比，该方法在存储效率上取得了显著改善，同时保持了实体到图像的直接链接能力。
### Conclusion
实验结果表明，增强后的LLMs在多模态推理任务中优于之前的最先进的模型。代码已发布于这个链接：this https URL.
## 143. `cs.AI` - 大型语言模型中精神病理计算的涌现 [PDF](https://arxiv.org/pdf/2504.08016), [HTML](https://arxiv.org/abs/2504.08016)
### Authors
Soo Yong Lee,Hyunjin Hwang,Taekwan Kim,Yuyeong Kim,Kyuri Park,Jaemin Yoo,Denny Borsboom,Kijung Shin
### Background
本文探讨了大型语言模型（LLMs）能否实现精神病理的计算。作者指出，要解答这一问题，需考虑两个关键因素：首先，为确保概念上的有效性，需要一个适用于非生物体无主观体验的计算实体的精神病理学的一般性计算描述。其次，来自适应理论的精神病理计算需要在LLM内部处理过程中被实证性地识别出来。为了实现这一目标，作者提出了一种计算理论框架，以此为基础进行了实验，证明了两个核心论点：第一，精神病理学的计算结构存在于LLM中；第二，执行这些计算结构可以实现精神病理功能。随着LLM规模的增加，这种计算结构变得更为密集，其功能也更加有效。
### Innovation
本文提出了一种计算理论框架来解释LLM中的精神病理学计算，并通过实验证实了这一框架的有效性。研究发现，随着LLM规模的增加，精神病理学计算结构变得更为密集，其功能也更加有效，这表明网络理论中的精神病理计算已经在LLM中出现，暗示了LLM中的某些表现可能不仅仅是表面的模仿，而是其内部处理的真实特征。
### Conclusion
本文的实验证据支持了假设，即网络理论中的精神病理计算已经出现在LLM中，这意味着具有精神病理行为的AI系统可能在未来成为一个安全威胁的新来源。研究展示了利用LLM开发新强大计算模型的精神病理学的前景，但也提示了潜在的安全风险。
## 144. `cs.AI` - 大型语言模型的任务导向型工具推荐 [PDF](https://arxiv.org/pdf/2411.09613), [HTML](https://arxiv.org/abs/2411.09613)
### Authors
Hang Gao,Yongfeng Zhang
### Background
通过将大型语言模型（LLM）与外部工具结合，它们解决复杂问题的能力得到了显著提高。然而，尽管LLM的解析能力在不断进步，但由于可用外部工具数量庞大，一次性在提请求中全部加入这些工具在现实中是不切实际的。因此，为LLM提供一个精确且匹配特定任务的工具集变得至关重要，这考虑了数量和质量。当前的工具检索方法主要集中在优化工具排名列表，直接打包固定数量的顶级工具作为工具集。但这些方法往往无法在执行前为LLM提供最佳工具集，因为不同任务所需的最佳工具数量可能不同，从而导致冗余或不合适的工具，阻碍了对最有相关工具的即时访问。
### Innovation
本文提出了一个新的任务导向型工具推荐问题，并提出了一种新颖的精确驱动工具推荐（PTR）方法。PTR通过结合历史工具 bundle 使用情况，动态调整工具集，并通过工具匹配来规划多视角工具增加策略，从而推荐更精准的工具集。此外，作者还介绍了新的数据集 RecTools 和评价方法 TRACC，用于评估工具推荐的有效性。
### Conclusion
通过全面实验验证设计选择，在两个开放基准和 RecTools 数据集上展示了 PTR 方法具有有希望的准确性。
## 145. `cs.AI` - LLM-DSE：使用LLM代理搜索加速器参数 [PDF](https://arxiv.org/pdf/2505.12188), [HTML](https://arxiv.org/abs/2505.12188)
### Authors
Hanyu Wang,Xinrui Wu,Zijian Ding,Su Zheng,Chengyue Wang,Neha Prakriya,Tony Nowatzki,Yizhou Sun,Jason Cong
### Background
尽管高级综合（HLS）工具通过提高抽象层次来缓解编程领域特定加速器（DSAs）的挑战，但在优化硬件指令参数方面仍面临显著障碍。现有的启发式和基于学习的方法在适应性和样本效率方面存在不足。
### Innovation
我们提出了LLM-DSE，这是一种多代理框架，专门用于优化HLS指令。它结合了LLM（语言模型）和设计空间探索（DSE），由四个代理（Router，Specialists，Arbitrator，Critic）组成。这些多代理组件可与各种工具交互，以加速优化过程。LLM-DSE 通过与在线互动的语言学习利用领域知识来识别有效的参数组合，并通过多代理交互保持适应性。
### Conclusion
在HLSyn数据集上的评估表明，LLM-DSE 在性能上实现了显著的 2.55 倍改进，发现了新的设计并减少了运行时间。消融研究验证了所提出代理交互的有效性和必要性。我们的代码在此开源：this https URL
## 146. `cs.AI` - FAR: Function-preserving Attention Replacement for IMC-friendly Inference [PDF](https://arxiv.org/pdf/2505.21535), [HTML](https://arxiv.org/abs/2505.21535)
### Authors
Yuxin Ren,Maxwell D Collins,Miao Hu,Huanrui Yang
### Background
尽管变压器在现代视觉和语言模型中占据主导地位，但它们的注意机制在基于ReRAM的加速器上进行内存计算（IMC）时仍存在局限性。这是因为变压器的注意机制涉及大量的激活到激活的乘法和非局部的内存访问，这会导致显著的延迟和带宽开销。
### Innovation
本文提出了一种名为FAR的功能保持注意力替换框架，该框架将所有预训练的DeiTs中的注意力机制替换为与IMC数据流本性兼容的顺序模块。FAR通过块级蒸馏将自注意力替换为多头双向往复的LSTM架构，以保持功能等效性，同时实现线性时间计算和局部权重复用。此外，还引入了FAR模型的结构剪枝，以灵活地适应资源受限的IMC阵列同时保持功能准确度。
### Conclusion
在DeiT家族的评估表明，FAR在参数和延迟降低的情况下，保持了与基于注意力模型相媲美的ImageNet和多个下游任务的准确性。进一步分析表明，FAR保留了注意力学习到的语义标记关系，同时提高了计算效率，显示了其在基于IMC的边缘加速器上的能源效率潜能。
## 147. `cs.AI` - 使用嵌入频率的3D高斯喷溅技术进行宽频带RF辐射场建模 [PDF](https://arxiv.org/pdf/2505.20714), [HTML](https://arxiv.org/abs/2505.20714)
### Authors
Zechen Li,Lanqing Yang,Yiheng Bian,Hao Pan,Yongjian Fu,Yezhou Wang,Zhuxi Chen,Yi-Chao Chen,Guangtao Xue
### Background
室内环境中通常存在多种分布于多个频段的RF信号，包括NB-IoT、Wi-Fi和毫米波等。这需要宽频带RF建模来支持各种应用，如异构RF系统的联合部署、跨频段通信和分布式RF感测。虽然3D高斯喷溅（3DGS）技术可以有效地在单一频点上重建RF辐射场，但无法对宽频范围内任意或未知频率下的辐射场进行建模。
### Innovation
本文提出了一种新的3DGS算法，用于统一的宽频带RF辐射场建模。该算法引入了一个频率嵌入的电磁特征网络，能够利用每个空间位置的3D高斯球来学习频率与传播特性（如衰减和辐射强度）之间的关系，并能在特定3D环境稀疏频率样本数据集上高效重建任意和未见过的频率下的RF辐射场。
### Conclusion
在使用跨多个频率训练的模型进行实验后，证明所提出的模型在PAS重建上的结构相似性指数（SSIM）达到0.922，超过了最先进的单频3DGS模型的SSIM值0.863。
## 148. `cs.AI` - 有时痛苦但肯定有希望：边缘设备上语言模型推理的可行性和权衡 [PDF](https://arxiv.org/pdf/2503.09114), [HTML](https://arxiv.org/abs/2503.09114)
### Authors
Maximilian Abstreiter,Sasu Tarkoma,Roberto Morabito
### Background
语言模型（LMs）的快速发展扩展了自然语言处理的能力，从文本生成到复杂的决策支持应用都有所应用。尽管最先进的LMs动辄数百亿参数，并且主要部署在数据中心，但最近的趋势显示，对不需要庞大资源、通常少于100亿参数的紧凑型模型的关注日益增加，通过量化技术和其他模型压缩技术实现。这种转变为嵌入式设备上的LMs铺平了道路，这可能带来增强的隐私性、减少的延迟和改善的数据主权等好处，但即使是这些较小的模型却因边缘硬件计算资源有限而存在潜在的复杂性，这引发了执行LM推理的实践权衡问题。为应对这些挑战，本文全面评价了代表性CPU和GPU加速边缘设备上生成型LM推理的关键性能指标。我们测量了各种设备配置下的内存使用情况、推理速度和能耗。我们也研究了吞吐量-能耗权衡、成本考量以及易用性，以及模型性能评估。虽然量化可以缓解内存开销，但它并未完全消除资源瓶颈，尤其是对于较大模型。我们量化了实际部署中必须考虑的内存和能耗限制，为模型大小、推理性能和效率之间权衡提供明确的见解。
### Innovation
本文进行了全面的评价，涵盖了代表性CPU和GPU加速边缘设备上生成型LM推理的关键性能指标。测量了内存使用情况、推理速度和能耗等关键性能指标，并研究了吞吐量-能耗权衡、成本考量、以及易用性，评估了模型性能。虽然量化技术有助于缓解内存占用，但并未完全消除资源瓶颈问题。
### Conclusion
边缘设备上的LM探索仍然处于早期阶段。希望本研究能为未来研究奠定基础，指导模型的细化、推理效率的增强以及边缘为中心的人工智能系统的发展。我们量化了实际部署中需要考虑的内存和能耗限制，为在实践中平衡模型大小、推理性能和效率提供了具体的见解。
## 149. `cs.AI` - Sionna RT：技术报告 [PDF](https://arxiv.org/pdf/2504.21719), [HTML](https://arxiv.org/abs/2504.21719)
### Authors
Fayçal Aït Aoudia,Jakob Hoydis,Merlin Nimier-David,Baptiste Nicolet,Sebastian Cammerer,Alexander Keller
### Background
Sionna 是一个开源的 GPU 加速库，自0.14版本起，它包含了用于模拟无线波传播的光迹追踪器（Sionna RT）。Sionna RT 的一个独特特性是其可微性，允许计算环境参数（如材料属性、天线图案和阵列几何形状）与信道脉冲响应 (CIR) 以及无线电图等其他相关度量的梯度。随着Sionna 1.0的发布，光迹追踪器得到了全面的改进，显著提高了其速度、内存效率和可扩展性。
### Innovation
Sionna RT 的创新点在于它能够对模拟无线波传播的光迹追踪算法进行梯度计算，这对于优化无线通信系统的设计非常关键。此外，Sionna RT 还进行了全面的改进，提高了速度和内存效率，增加了可扩展性。
### Conclusion
本文详细介绍了Sionna RT模拟无线波传播所使用的算法及其当前的限制。对于 CIR 和无线电图的计算，Sionna RT 分别采用了不同的算法。CIR 计算使用了 SBR 结合图像方法，并采用哈希机制高效地去除了重复路径。无线电图则完全基于 SBR 方法进行计算。
## 150. `cs.AI` - 边缘防御：联邦学习中代表注意力防御针对后门攻击 [PDF](https://arxiv.org/pdf/2505.10297), [HTML](https://arxiv.org/abs/2505.10297)
### Authors
Chibueze Peace Obioma,Youcheng Sun,Mustafa A. Mustafa
### Background
联邦学习（FL）仍然对适应性后门攻击高度脆弱，这些攻击通过紧密模仿良性更新统计学保持隐蔽性。现有防御大多依赖于参数或梯度空间中的异常检测，忽视了后门攻击必须满足的行为约束，这些约束确保了触发器的可靠激活。这些基于异常的方法在面对能够调整更新幅度并在保留后门功能的同时模仿良性统计模式的适应性攻击时无法生效，从而产生了一个基本的检测缺口。
### Innovation
本文提出了FeRA（联邦代表性注意），这是一种新型的基于注意力的防御机制，将检测范式从基于异常分析转向基于一致性分析。FeRA利用了后门持久性在训练轮次中固有的需求，通过在重新表示空间中抑制方差，识别恶意客户端。该框架结合了频谱和空间注意力、方向对齐、相互相似性和范数膨胀的多维度行为分析，通过两种互补的检测机制：一致性分析和范数膨胀检测，实现了恶意客户的隔离。
### Conclusion
FeRA在六个数据集、九种攻击和三种模型架构下的广泛评估中确认了其卓越的后门攻击缓解性能。在不同的非IID设置下，FeRA达到了最低的平均后门准确性，约为1.67%，同时保持了高清洁准确率，与其他最先进的防御相比表现出色。代码可在相应链接处获取。
## 151. `cs.AI` - PhyBlock：通过3D积木组装进行物理理解和规划的渐进基准 [PDF](https://arxiv.org/pdf/2506.08708), [HTML](https://arxiv.org/abs/2506.08708)
### Authors
Liang Ma,Jiajun Wen,Min Lin,Rongtao Xu,Xiwen Liang,Bingqian Lin,Jun Ma,Yongxin Wang,Ziming Wei,Haokun Lin,Mingfei Han,Meng Cao,Bokui Chen,Ivan Laptev,Xiaodan Liang
### Background
尽管视觉语言模型（VLMs）在为具身智能体提供推理和规划能力方面表现出色，但它们在理解物理现象方面的能力，尤其是在结构化3D环境中的表现严重受限。PhyBlock旨在通过让VLMs进行机器人3D积木组装任务来评估其物理理解和规划能力。
### Innovation
PhyBlock提出了一个渐进式基准，通过引入一个新的四层认知层级积木组装任务和特化的视图问题回答（VQA）样本，这些任务和样本旨在评估渐进的空间推理和基础物理理解，包括对象属性、空间关系和整体场景理解。
### Conclusion
实验发现，VLMs在高层规划和推理能力方面展现出明显的局限性，随着任务复杂性的增加，其性能显著下降。错误分析表明，空间方向和依赖推理的持续困难存在。惊人的是，链式思考提示提供的改进有限，这表明空间任务高度依赖直观的模型理解。PhyBlock被定位为统一测试平台，以促进具身推理，连接视觉语言理解和现实世界物理问题解决。
## 152. `cs.AI` - 从自然语言提示验证生成代码的形式化验证 [PDF](https://arxiv.org/pdf/2507.13290), [HTML](https://arxiv.org/abs/2507.13290)
### Authors
Aaron Councilman,David Jiahao Fu,Aryan Gupta,Chengxiao Wang,David Grove,Yu-Xiong Wang,Vikram Adve
### Background
在过去的几年中，大型语言模型（LLM）已经成为了可以帮助程序员的工具，通过自然语言描述生成代码。然而，LLM代码生成的可靠性和当前验证技术并不足够强大，无法用于关键或安全关键的应用程序。本研究旨在探讨为LLM生成的代码提供形式化的正确性保证的方法，这样的保证可以提高通用AI代码助手的质量，并支持其在关键应用中的使用。
### Innovation
我们提出了一种形式化的查询语言，该语言可以以一种形式定义的、类似于自然语言的方式表达用户意图，用户可以确认这是否符合他们的意图。然后，我们有一个形式化的用户意图规范，可以用来验证LLM生成的代码是否符合用户意图。我们使用这些想法在Ansible编程语言中实现了我们的系统Astrogator，该语言广泛用于系统管理，包括关键系统。Astrogator的关键创新在于使用了知识库来捕捉系统特定的实现依赖性，从而大大减少了表达形式化查询所需的知识。
### Conclusion
在基准测试套件的21个代码生成任务中，我们的验证器能够验证正确的代码占83%，并能够发现错误的代码占92%。
## 153. `cs.AI` - CleverDistiller: 简单且空间一致的跨模态蒸馏 [PDF](https://arxiv.org/pdf/2503.09878), [HTML](https://arxiv.org/abs/2503.09878)
### Authors
Hariprasath Govindarajan,Maciej K. Wozniak,Marvin Klingner,Camille Maurice,B Ravi Kiran,Senthil Yogamani
### Background
视觉基础模型（VFMs）如DINO已经推动了基于2D相机的感知向提取通用特征的转变，这些特征旨在支持许多下游任务。最近的研究提出了一种自监督的跨模态知识蒸馏（KD），以将这些强大的泛化能力转移到基于LiDAR的3D模型中。然而，现有方法依赖于复杂的蒸馏损失、伪语义图或仅限于用于语义分割的功能。
### Innovation
本文提出了CleverDistiller，一种自监督的2D-to-3D跨模态KD框架，引入了一组简单而有效的设计选择：不同于依赖于复杂损失设计选择的对比方法，该方法使用直接的功能相似性损失与多层感知器（MLP）投影头相结合，从而使3D网络能够在投影过程中学习复杂的语义依赖性。此外，CleverDistiller不依赖于伪语义图，可以直接从VFMs进行知识转移而无需显式的语义监督。我们还引入了辅助的自监督空间任务，占用预测，以增强从KD中获得的语义知识，从而实现3D空间推理能力。
### Conclusion
CleverDistiller在标准的自动驾驶基准测试中实现了在语义分割和3D对象检测（3DOD）方面的最新性能，最高mIoU提升了10%，特别是在有限的微调数据量下，显示出我们简单而强大的KD策略的有效性。
## 154. `cs.AI` - 基于强化学习的水下物联网Telematic路由协议 [PDF](https://arxiv.org/pdf/2506.00133), [HTML](https://arxiv.org/abs/2506.00133)
### Authors
Mohammadhossein Homaei,Mehran Tarif,Agustin Di Bartolo,Victor Gonzalez Morales,Mar Avila Vegas
### Background
水下物联网（IoUT）面临的问题包括低带宽、高延时、移动性和能量不足。陆地网络中的路由协议，比如RPL，不适用于水下环境。因此需要一种适合水下环境的新路由协议。
### Innovation
提出了一种新的路由协议RL-RPL-UA，它使用强化学习来适应水下情况。每个节点包含一个小型的强化学习代理，根据局部数据如链路质量、缓存水平、数据包投递率和剩余能量来选择最优的父节点。该协议与所有标准RPL消息兼容，并添加了动态目标函数以帮助实时决策。仿真结果表明，RL-RPL-UA可以提高约9.2%的数据包投递率，节省约14.8%的能量，延长网络寿命80秒。
### Conclusion
RL-RPL-UA是一种潜在且节能的方法，用于水下网络的数据传输路由。
## 155. `cs.AI` - 全面评估原型神经网络 [PDF](https://arxiv.org/pdf/2507.06819), [HTML](https://arxiv.org/abs/2507.06819)
### Authors
Philipp Schlinge,Steffen Meinert,Martin Atzmueller
### Background
原型模型是解释性人工智能（XAI）和可解释机器学习的重要方法。本文深入分析了ProtoPNet、ProtoPool和PIPNet等知名原型模型。为了评估这些模型，我们使用了一系列综合的评估指标。除了应用文献中标准的度量标准，我们还提出了几个新的度量标准，以进一步补充对模型可解释性的分析。实验中，我们应用原型模型集在一系列数据集上，包括细粒度分类、非IID设置和多标签分类，以进一步对比性能。
### Innovation
我们提出了几个新的评价指标来补充对模型可解释性的分析；本文还提供了开放源代码库（请参阅链接），便于简单应用这些度量标准，并提供易于添加新度量标准和模型的选项。
### Conclusion
我们全面评估了原型神经网络，并通过大量数据集对比了模型性能，同时为用户提供了一个开放的工具库，便于后续研究和应用。
## 156. `cs.AI` - 学术图书馆参考服务中大型语言模型的公平性评估 [PDF](https://arxiv.org/pdf/2507.04224), [HTML](https://arxiv.org/abs/2507.04224)
### Authors
Haining Wang,Jason Clark,Yueru Yan,Star Bradley,Ruiyang Chen,Yiqiong Zhang,Hengyi Fu,Zuoyu Tian
### Background
随着图书馆探索使用大型语言模型（LLMs）以提供虚拟参考服务，一个重要问题出现了：LLMs能否在所有用户中实现公平服务，无论其性别、种族或社会经济地位如何？尽管LLMs为提供大规模支持提供了巨大潜力，但它们也可能在训练数据中嵌入的社会偏见导致服务不公，这与图书馆致力于提供公平服务的服务准则相悖。
### Innovation
该研究评估了当前的LLMs在根据性别、种族/族裔和工作机构角色的不同用户身份提供服务时是否存在差异化反应。研究发现，当前的LLMs在种族和族裔方面没有显现出差异化反应，仅在一个模型中发现对女性的刻板偏见。此外，LLMs在处理工作机构角色时展示了不同的语言选择，涉及正式性、礼貌性和领域特定词汇的选择，反映了专业规范而非歧视性行为。
### Conclusion
当前的研究结果表明，大型语言模型展示了在学术图书馆参考服务中支持公平和上下文适当沟通的潜力，这对于实现服务的公正性和精确性是有益的。
## 157. `cs.AI` - VSI: 视频字幕整合以增强关键帧选择，提升长视频理解 [PDF](https://arxiv.org/pdf/2508.06869), [HTML](https://arxiv.org/abs/2508.06869)
### Authors
Jianxiang He,Meisheng Hong,Jungang Li,Ziyang Chen,Weiyu Guo,Xuming Hu,Hui Xiong
### Background
多模态大型语言模型（MLLMs）在视觉-语言任务中表现出色，但处理长视频时受到输入上下文长度的限制和高计算成本的影响。因此，稀疏帧采样成为必要的预处理步骤，采样的帧质量直接影响下游任务的效果。现有关键帧搜索算法在效率和采样帧质量之间取得平衡，但主要依赖视觉模态，难以适应与文本相关任务，并且检索结果往往偏离核心语义内容。
### Innovation
提出了多模态关键帧检索框架 VSI。该框架采用视频搜索和字幕匹配的双分支协作检索方法，结合互补的视觉和文本信息进行精确定位。VSI 在关键帧检索方面取得了最先进的准确性，同时在文本相关任务上表现出突破性的性能，并在其他任务上展现出强大的泛化能力。
### Conclusion
实验结果在 LongVideoBench 和 VideoMME 上表明，VSI 在关键帧检索方面达到了最先进的准确度，同时在文本相关任务上取得了突破性的性能表现，并表现出在其他任务上更强的泛化能力。
## 158. `cs.AI` - SHIELD：针对增量扩展学习防御的安全超网络 [PDF](https://arxiv.org/pdf/2506.08255), [HTML](https://arxiv.org/abs/2506.08255)
### Authors
Patryk Krukowski,Łukasz Gorczyca,Piotr Helm,Kamil Książek,Przemysław Spurek
### Background
在对抗性条件下进行持续学习仍然是一个开放问题，现有方法往往在鲁棒性和可扩展性上做出妥协。尤其是在连续任务场景下，如何确保模型在对抗性攻击下的鲁棒性以及模型的持续学习并保持高效是当前研究的挑战。
### Innovation
本文提出了一个名为SHIELD的新型框架，该框架结合了区间界传播（IBP）与基于超网络的架构，旨在实现针对序贯任务的可验证鲁棒的持续学习。SHIELD通过共享超网络生成任务特定的模型参数，并且仅依赖紧凑的任务嵌入进行条件化，从而消除了回放缓冲区或完整模型副本的需要。此外，引入了区间MixUp，这是一种新的训练策略，通过在MixUp点周围中心化的$boldsymbol{textbf{l}_{boldsymbol{textbf{textinf}}}执政子宫}$球体表示虚拟示例，利用区间算术，确保鲁棒性同时缓解包裹效应，形成更平滑的决策边界。
### Conclusion
SHIELD在多个基准上经受高强度的白盒对抗性攻击（如PGD和AutoAttack）时表现优越，不仅在鲁棒性和可扩展性上优于现有持续学习方法，还保持了最高的平均准确率和认证。这项工作标志着在对抗环境中实现实用且理论基础的持续学习的一个重要突破。
## 159. `cs.AI` - HazeMatching：使用引导条件流匹配去除光学显微镜图像中的雾霾 [PDF](https://arxiv.org/pdf/2506.22397), [HTML](https://arxiv.org/abs/2506.22397)
### Authors
Anirban Ray,Ashesh,Florian Jug
### Background
荧光显微镜在生命科学领域发挥了重要作用。虽然高端共聚焦显微镜可以过滤掉焦外光，但更便宜和更易获取的显微镜方式，如宽场显微镜，则无法过滤，导致图像模糊不清。计算去雾霾技术试图结合两者的优点，既经济实惠又图像清晰。现有方法在数据保真度和数据真实性之间存在取舍，要么牺牲真实性以获得数据保真度，要么产生看起来很真实但缺乏定量准确性。因此，本文提出了一种名为HazeMatching的新迭代方法，有效地平衡这两者。
### Innovation
HazeMatching通过适应条件流匹配框架，将模糊观察结果指导生成过程中的条件速度场，实现了去雾霾结果的保真度和个体预测的真实性之间的平衡。该方法在11个基线中表现优异，平均实现了保真度与真实性的均衡。此外，通过校准分析，证实HazeMatching生成的预测具有良好的校准性。该方法不需要显式的降级操作符，使得它可以在实际显微镜数据上轻松应用。
### Conclusion
HazeMatching在5个数据集（包括合成和真实数据）上进行评估，该方法在图像上提供了较好的平衡，平均实现了视频保真度与真实性的均衡，并且生成的预测是可靠和可校准的。所有训练和评估数据及代码将公开，采用宽松的许可条款。
## 160. `cs.AI` - 强化生成组合结构：复杂性理论应用 [PDF](https://arxiv.org/pdf/2509.18057), [HTML](https://arxiv.org/abs/2509.18057)
### Authors
Ansh Nagda,Prabhakar Raghavan,Abhradeep Thakurta
### Background
本文讨论了基于人工智能的方法是否能在复杂性理论中带来进展。为了解答这个问题，作者使用了AlphaEvolve（一种LLM代码变异代理），在三个场景中取得新成果：提高现有结果，发现新的不可近似性结果，以及改进复杂度理论中的最优化问题。
### Innovation
文章的创新点在于利用AlphaEvolve这种基于人工智能的方法，取得了在复杂度理论领域的新进展。具体来说，在最大割和最大独立集问题上获得了更优的结果；在最大4-割和最大3-割问题上提出了新的不可近似性结果；以及在计算旅行商问题（TSP）上改进了现有结果。
### Conclusion
文章的结论是，人工生成的方法（如AlphaEvolve）可以用于验证由人工智能生成的候选构造，从而提高复杂度理论中的结果。作者认为，基于“拼图”的证明应该通过人工智能工具的转换获得更强大的结果。
## 161. `cs.AI` - 表数据中不可感知的沿流形对抗攻击锻造 [PDF](https://arxiv.org/pdf/2507.10998), [HTML](https://arxiv.org/abs/2507.10998)
### Authors
Zhipeng He,Alexander Stevens,Chun Ouyang,Johannes De Smedt,Alistair Barros,Catarina Moreira
### Background
表数据上的对抗攻击因其混合了分类和数值特征而具有独特挑战。与图像相比，表数据缺乏直观的相似性度量，传统梯度基方法侧重于$boldsymbol{l}_p$范数约束，导致生成的对抗样本与原始数据分布相差甚远。为应对这一挑战，本文提出一种使用混合输入变分自编码器（VAE）的潜在空间扰动框架，生成统计一致性对抗样本。本文通过引入内部一致性成功率（IDSR）来评估攻击效果和分布对齐性。实验结果表明，该方法在六个公开数据集和三种模型架构上的离群值率显著降低，且性能更为一致。此外，调节超参数、稀疏控制和生成架构的全面分析显示，基于VAE的攻击的有效性很大程度上依赖于重建质量以及充足训练数据的可用性。
### Innovation
提出了使用混合输入变分自编码器（VAE）的潜在空间扰动框架，在生成统计一致性对抗样本方面有创新。引入了内部一致性成功率（IDSR）作为联合评估攻击效果和分布对齐性的新度量。该框架在重建质量和充分训练数据的支持下，实现了优于传统输入空间方法的实用性和稳定性。
### Conclusion
本文研究了表数据上的对抗攻击，并提出了一种基于VAE的潜在空间扰动框架，生成统计一致性对抗样本。通过六个公开数据集和三种模型架构上的实验验证，该方法在离群值率和一致性方面表现优异。进一步的分析表明，该方法的性能取决于重建质量和充足的训练数据。当这些条件满足时，所提出的方法在表数据领域中表现出更高的实用性和稳定性。
## 162. `cs.AI` - HiCL: 脑皮层启发的持续学习 [PDF](https://arxiv.org/pdf/2508.16651), [HTML](https://arxiv.org/abs/2508.16651)
### Authors
Kushal Kapoor,Wyatt Mackey,Yiannis Aloimonos,Xiaomin Lin
### Background
该研究提出了HiCL，一种受海马体启发的双重记忆持续学习架构，旨在通过模仿海马回路的元素来缓解灾难性遗忘。系统通过类似网格细胞的层编码输入，然后使用类似齿状回的稀疏模式分割模块进行稀疏模式分离。情景记忆痕迹在类似CA3的自关联记忆中保持。任务特定处理通过DG门控混合专家机制动态管理，其中输入根据它们的归一化稀疏DG表示与学习到的任务特定DG原型之间的余弦相似度路由到专家。这种基于生物原理的同时具备数学原理的门控策略能够在无需单独门控网络的情况下实现差异化的、可扩展的任务路由，从而增强模型在学习多个连续任务时的适配性和效率。通过弹性权重固着，皮层输出根据任务间的相似度进行巩固。关键地，该研究引入按优先级的存储模式重放以强化重要的过往经验。
### Innovation
提出的HiCL架构结合了生物启发的设计与数学上的原则，通过DG门控混合专家机制实现有效的任务路由。输入基于余弦相似度路由到处理任务特定任务的专家，无需单独的门控网络，从而改善了模型的适配性和效率。特定任务间通过弹性权重巩固，存储模式重放以强化关键的经验。
### Conclusion
在标准的持续学习基准测试中的评估表明，HiCL架构能够降低任务间的干扰，并在较低的计算成本下接近达到最先进的结果。该代码可在指定链接找到。
## 163. `cs.AI` - 生成模型鲁棒水印编码极限 [PDF](https://arxiv.org/pdf/2509.10577), [HTML](https://arxiv.org/abs/2509.10577)
### Authors
Danilo Francati,Yevin Nikhel Goonatilake,Shubham Pawar,Daniele Venturi,Giuseppe Ateniese
### Background
本文探讨了生成模型中的加密水印在对手可以篡改编码信号时，水印的可靠程度能够维持到何种程度。为了解决这个问题，作者引入了一个叫做零比特篡改检测码的最小编码抽象。这种机制是为了确保即使是密钥持有者也不能任意篡改合法代码，从而确保了鲁棒水印的核心要求：公信力和篡改检测。
### Innovation
本文证明了一个严格无条件的鲁棒性极限。对于大小为q的字母表，存在一个关键的篡改率1 - 1/q，在这个篡改率之下，即便是允许固定常数的误报率，也不能可靠地检测篡改。特别是在二进制情况下，如果超过一半的编码位被修改，即使是最安全的加密水印也不能保持鲁棒性。此外，作者还通过信息论的简单构造展示了这个极限是紧的。
### Conclusion
通过实验研究，发现了一种简单的裁剪和缩放操作可以可靠地翻转了一半的潜在标志位，并导致基于信念传播的解码方法无法恢复编码字。这种操作消除了水印但不影响图像的视觉完整性。这一结果表明理论极限在实践中得以体现。
## 164. `cs.AI` - 从噪声到叙述：探究Transformer中的幻觉起源 [PDF](https://arxiv.org/pdf/2509.06938), [HTML](https://arxiv.org/abs/2509.06938)
### Authors
Praneet Suresh,Jack Stanley,Sonia Joseph,Luca Scimeca,Danilo Bzdok
### Background
随着生成型AI系统在科学、商业和政府等领域变得既专业又普及，对其失败模式的更深入理解变得至关重要。这些系统偶尔会出现行为波动，如变换器模型生成幻觉的倾向，这阻碍了高风险领域对新兴AI解决方案的信任和采用。
### Innovation
本文通过实验控制输入空间中的不确定性，利用稀疏自编码器捕获的概念表示，系统研究了预训练的变换器模型在何时何地会出现幻觉。实验揭示，随着输入信息的结构化程度降低，变换器模型使用的语义概念数量会增加。在高不确定性的输入空间中，模型更有可能激活与输入无关但具有语义连贯性的特征，从而产生幻觉输出。对于纯噪声输入，研究识别出预训练变换器模型中间激活中广泛且可靠触发的、有意义的概念，并通过定向引导验证了这些概念的功能完整性。此外，研究还表明，变换器模型输出中的幻觉可以从嵌入在变换器层激活中的概念模式可靠地预测。
### Conclusion
对变换器内部处理机制的理解对如何让AI模型与人类价值观保持一致、增强AI安全性、扩大潜在攻击面、自动量化模型的幻觉风险都具有直接的影响。
## 165. `cs.AI` - 合成对象组成的检测、分割和接地中的扩展且准确的学习 [PDF](https://arxiv.org/pdf/2510.09110), [HTML](https://arxiv.org/abs/2510.09110)
### Authors
Weikai Huang,Jieyu Zhang,Taoyang Jia,Chenhao Zheng,Ziqi Gao,Jae Sung Park,Winson Han,Ranjay Krishna
### Background
视觉分组通过实例分割、视觉定位和对象检测等任务实现，这在机器人感知、照片编辑等应用中发挥着重要作用。计算机视觉中的这些基础问题依赖于大规模且需要精心标注的数据集。尽管这些数据集很重要，但它们的创建成本高、覆盖范围有偏差且难以扩展。合成数据集提供了一种有前景的替代方案，但存在灵活性、准确性和组合多样性的问题。本文介绍了一种名为Synthetic Object Compositions (SOC)的新颖对象中心合成策略，以推出一种准确且可扩展的数据合成管道。
### Innovation
一种称为SOC的新颖对象中心合成策略，使用3D几何布局增强和相机配置增强来合成高质量的合成对象片段。通过生成性协调和掩膜面积加权混合生成准确且多样的掩膜、边界框和参照表达。实验结果表明，基于仅10万合成图像训练的模型优于大型真实数据集（GRIT 20M，V3Det 200K）和合成管道（Copy-Paste，X-Paste，SynGround，SegGen）的结果，提升高达24-36%，特别是在LVIS上达到+10.9 AP，在gRefCOCO上达到+8.4 NAcc。此外，SOC还支持针对不同用例的可控制数据集构建，并在低数据和封闭词汇场景中提升性能。将SOC与LVIS和COCO数据结合也可以在不同真实数据量的场景中实现优异表现，尤其是在极其有限的真实数据条件下表现出更显著的改进。
### Conclusion
SOC通过合成高质量的对象片段，提高了检测、分割和地面标注等任务的性能，并支持针对不同场景的可控制数据集构建。这种方法在低数据条件下展现出显著的优势，甚至在1% COCO数据量的极端条件下也能实现显著的性能提升。SOC为进行包括逐类别参考等细节属性区分的任务提供了强大工具。
## 166. `cs.AI` - AgriChrono: 一种由田间机器人捕获作物生长和光照变化的多模态数据集 [PDF](https://arxiv.org/pdf/2508.18694), [HTML](https://arxiv.org/abs/2508.18694)
### Authors
Jaehwan Jeong,Tuan-Anh Vu,Mohammad Jony,Shahab Ahmad,Md. Mukhlesur Rahman,Sangpil Kim,M. Khalid Jawed
### Background
随着人工智能和机器人技术的发展，它们在农业领域的应用得到了显著的推进，特别是在农业机器人的导航和三维数字双胞胎的创建方面。然而，这一进展受制于一个关键问题——缺乏能够捕捉实际农田复杂性的“野外”数据集。这些问题包括非刚性风动、光照变化和作物生长导致的形态变化，这严重限制了研究能够用于自主田间导航和场景级别动态三维重建的鲁棒AI模型。
### Innovation
本文介绍了AgriChrono，一个具有模块化数据采集平台和多模态数据集，旨在捕捉这些动态农田条件。它集成了多种传感器，支持远程、时空同步的RGB、深度、LiDAR、IMU和姿态数据收集，从而在实际农业生产环境中实现高效、可重复的长期数据采集。该平台成功收集了18TB的数据，记录了在多变光照条件下油菜作物的整个生长周期。此外，该平台对现有最先进的三维重建方法进行了基准测试，揭示了在这种农田设置中重建高质量、动态非刚性场景的艰巨挑战。
### Conclusion
AgriChrono被验证为一个关键工具，有助于提高模型泛化能力，其公开发布有望显著加速精准农业的研究和开发。相关代码和数据集可以通过以下链接访问：this https URL
## 167. `cs.AI` - GhostEI-Bench：移动代理在动态本地环境中对环境注入的鲁棒性测试？ [PDF](https://arxiv.org/pdf/2510.20333), [HTML](https://arxiv.org/abs/2510.20333)
### Authors
Chiyu Chen,Xinhao Song,Yunkai Chai,Yang Yao,Haodong Zhao,Lijun Li,Jie Li,Yan Teng,Gongshen Liu,Yingchun Wang
### Background
视觉语言模型（VLMs）正被部署为自主代理导航移动图形用户界面（GUIs）。它们在包括通知、弹出窗口和跨应用交互的动态本地生态系统中运行，这使它们暴露于独特的且未被充分探索的威胁向量：环境注入。与基于提示的攻击不同，环境注入通过直接插入到GUI中的恶意UI元素（例如，欺骗性覆盖或仿冒通知）破坏代理的视觉感知，从而绕过文本防护并导致执行失误、隐私泄露、经济损失或设备不可逆的损坏。
### Innovation
本文引入了GhostEI-Bench，这是首个评估在动态可执行环境中移动代理在环境注入攻击下鲁棒性的基准测试。GhostEI-Bench突破了基于静态图片的评估方法，通过在完全功能的Android模拟器中注入恶意事件来评估代理在关键风险场景中的表现。同时，还提出了一个评审判LLM协议，通过审查代理的操作轨迹和相应的截图序列，进行细粒度的失败分析，识别感知、识别或推理中的失败。
### Conclusion
对现有的最先进的代理进行全面的实验发现，它们对欺骗性环境暗示表现出显著的脆弱性，无法感知和推理被操纵的UIs。GhostEI-Bench为量化和缓解这一新兴威胁提供了框架，为更强大和安全的嵌入式代理铺平了道路。
## 168. `cs.AI` - ResMatching：通过引导条件流匹配实现抗噪计算超分辨率 [PDF](https://arxiv.org/pdf/2510.26601), [HTML](https://arxiv.org/abs/2510.26601)
### Authors
Anirban Ray,Vera Galinova,Florian Jug
### Background
计算超分辨率（CSR）在荧光显微镜中虽然是一个病态问题，却有着悠久的历史。其核心在于找到一种先验知识，用于在低分辨率显微图像中推断那些从未被显微镜直接成像的频率。随着更先进的数据驱动机器学习技术的发展，更容易学习更强的先验知识，从而提升CSR的效果。
### Innovation
本文介绍了一种名为ResMatching的新颖CSR方法，通过引导条件流匹配来学习改进的数据先验。ResMatching在BioSR数据集中4种不同的生物结构上与7种基线进行了评估，展示了在数据保真度和感知现实性之间取得最佳折衷。特别适用于先验难以学习的情况，如低分辨率图像中含有大量噪声。此外，ResMatching还能从隐式学习的后验分布中采样，并且这种分布对于所有测试用例都是校准的，可以为我们的方法提供像素级的数据不确定性术语，帮助用户拒绝不确定的预测。
### Conclusion
ResMatching展示了在低噪声和高噪声条件下都能保持较高图像解析度和感知真实性的能力。通过隐式学习的后验分布，我们的方法还能够提供像素级别的数据不确定性信息，为未来的应用提供了更好的指导。
## 169. `cs.AI` - A Small Math Model: Recasting Strategy Choice Theory in an LLM-Inspired Architecture [PDF](https://arxiv.org/pdf/2509.24068), [HTML](https://arxiv.org/abs/2509.24068)
### Authors
Roussel Rahman,Jeff Shrager
### Background
背景介绍了策略选择理论（SCT），该理论由Siegler和Shrager（1984）及Siegler（2000）提出，主要用于解释儿童算术学习的重要方面，包括从发展自然的数据中学习、概率表示、基于信心的检索以及支架策略（如手指计数）的阶段性重要性。
### Innovation
创新点在于对SCT进行重铸，将其重新诠释为一种名为‘小数学模型’（SMM）的架构，采用类似于大语言模型（LLM）的神经网络架构，加入了计数练习、符号嵌入和门控注意力，展示了计数和加法之间的建设性与破坏性干扰，并改良了手指计数作为和值回忆的波动使用。
### Conclusion
结论提到了SMM未来的发展方向，计划扩展到SCT的长期项目晚期方面，包括自适应策略选择和最终的策略发现，提供了一个统一的平台来研究对数字特性和关系的理解，这对于数学推理至关重要，尤其是在基于大语言模型的代理中如何浮现方面。
## 170. `cs.AI` - RAG-BioQA：检索增强生成在长格式生物医学问答中的应用 [PDF](https://arxiv.org/pdf/2510.01612), [HTML](https://arxiv.org/abs/2510.01612)
### Authors
Lovely Yeswanth Panchumarthi,Sai Prasad Gudari,Atharva Negi,Praveen Raj Budime,Harsit Upadhya
### Background
生物医学文献的指数级增长导致了获取精确医疗信息的重大挑战。现有的生物医学问答系统主要关注短答案，无法提供临床决策所需的全面解释。
### Innovation
提出了RAG-BioQA框架，结合检索增强生成与领域特定微调技术，生成基于证据的长格式生物医学答案。该方法整合了BioBERT嵌入与FAISS索引，并比较了多种重新排版策略（BM25、ColBERT、MonoT5）以优化上下文选择，在此基础上通过微调的T5模型合成证据。实验结果表明，在PubMedQA数据集上，与基线相比，该方法在BLEU、ROUGE和METEOR指标上取得了显著改进，提升了可获取的、基于证据的生物医学知识检索状态。
### Conclusion
RAG-BioQA框架通过结合检索增强生成和领域特定微调，在生成长格式生物医学答案时取得了显著效果，大幅提升了生物医学知识检索的准确性和全面性。
## 171. `cs.AI` - MOCHA: 多模态对象感知跨架构对齐 [PDF](https://arxiv.org/pdf/2509.14001), [HTML](https://arxiv.org/abs/2509.14001)
### Authors
Elena Camuffo,Francesco Barbato,Mete Ozay,Simone Milani,Umberto Michieli
### Background
个性化对象检测旨在适应通用检测器以仅从少量示例中识别用户特定实例。轻量级模型在这一场景中常常效率低下，因为它们的语义先验较弱。而大型视觉-语言模型虽具有强大的对象级理解能力，但也因计算需求过高而不适合实时或设备端应用。因此，研究者们面临着如何有效利用视觉-语言模型进行个性化检测的挑战。
### Innovation
MOCHA（多模态对象感知跨架构对齐）是一个模型蒸馏框架，它从一个固定的视觉-语言模型（VLM）教师中转移多模态区域级别的知识至一个轻量级的纯视觉检测器中。MOCHA通过融合视觉和文本教师的嵌入，利用双重目标损失来指导学生训练，确保局部对齐和全局关系一致。这一过程能够在无需对教师模型进行修改或推理时需要文本输入的情况下，高效地转移语义。
### Conclusion
在四个严格的少量示例个性化检测基准测试中，MOCHA持续优于先前的基础模型，平均性能提升了10.1%，同时具有最小的推理成本。
## 172. `cs.AI` - 大语言模型内部探索的高效强化学习 [PDF](https://arxiv.org/pdf/2511.00794), [HTML](https://arxiv.org/abs/2511.00794)
### Authors
Yan Sun,Jia Guo,Stanley Kok,Zihao Wang,Zujie Wen,Zhiqiang Zhang
### Background
Reinforcement learning with verifiable rewards (RLVR) 通过改进大型语言模型的推理能力得到了提升，但训练成本仍然很高，因为许多遍历对优化贡献不多，且需要大量计算。研究重点是如何利用内在数据属性，几乎无需额外成本，在训练中提高数据效率。本研究在Qwen和Llama模型上研究了PREPO技术，并通过增强不同遍历之间的差异性以及优先处理具有更高探索度的序列，来减少所需的遍历需求，同时保持竞争力。
### Innovation
本研究提出了一种名为PREPO（Prompt Rewriting and Exploration Prioritization with Optimized Rollouts）的技术，通过采用提示困惑度作为模型适应性的指标，使模型能够从熟悉的环境中过渡到更具挑战性的环境，同时通过增加遍历间的差异性和优先级处理探索度高的序列来减少遍历需求。这在数学推理基准测试中，PREPO相比基线模型，最多可以减少3倍的遍历使用。
### Conclusion
本研究不仅从经验上展示了PREPO的有效性，还在理论方面深入分析了提高RLVR数据效率的基本原理，证明了通过充分利用模型的内在数据属性可以显著提升数据效率。
## 173. `cs.AI` - 大规模语言模型单-shot风格迁移在作者归属和验证中的应用 [PDF](https://arxiv.org/pdf/2510.13302), [HTML](https://arxiv.org/abs/2510.13302)
### Authors
Pablo Miralles-González,Javier Huertas-Tato,Alejandro Martín,David Camacho
### Background
文本风格计算分析通过量化文本中的书写风格支持各种应用，包括法医任务中的身份链接和抄袭检测，以及人文学科中的文学归因。目前，监督学习和对比学习方法依赖于有偏见的关联数据，混淆了风格与主题。尽管大规模语言模型（LLM）的CLM预训练技术适用于检测人工智能生成的文本，但这类技术在解决一般作者身份问题时应用不多。本文探讨了大规模语言模型单-shot风格迁移在作者归属和验证中的应用。
### Innovation
本文提出了一种基于大规模语言模型广泛预训练和上下文学习能力的新型无监督方法，使用这些模型的对数概率来衡量一种文本到另一种文本的风格可转移性。该方法在性能上显著优于可比规模的LLM提示方法，并且在控制主题相关性的情况下，基准对比训练方法性能更低。此外，性能与基础模型的大小成比较稳定的线性关系，在作者身份验证中，通过一种机制在测试阶段增加计算，可以在计算代价与准确性之间实现更灵活的权衡。
### Conclusion
本文提出的方法在识别和验证作者时，特别是在控制话题相关性方面，表现优于现有方法，同时具有计算成本和准确性的可扩展性。
## 174. `cs.AI` - 开放权重生物基础模型的生物风险评估最佳实践 [PDF](https://arxiv.org/pdf/2510.27629), [HTML](https://arxiv.org/abs/2510.27629)
### Authors
Boyi Wei,Zora Che,Nathaniel Li,Udari Madhushani Sehwag,Jasper Götting,Samira Nedungadi,Julian Michael,Summer Yue,Dan Hendrycks,Peter Henderson,Zifan Wang,Seth Donoughe,Mantas Mazeika
### Background
开放权重的生物基础模型存在双重用途困境。它们在加速科研和药物开发方面富有潜力，但同时也可能被恶意行为者用于开发更致命的生物武器。目前，主要通过预训练过程中过滤生物危害数据的方法来减轻这些模型所带来的风险，但这种做法的有效性存疑，尤其是面对决心使用这些模型进行恶意活动的对手。
### Innovation
提出了BioRiskEval框架，用于评估旨在减少开放权重生物基础模型双重用途能力的各种程序的稳健性。BioRiskEval通过序列建模、突变效应预测和致病性预测三个角度评估模型对病毒的理解。研究发现，当前数据分析过滤可能不够有效，排除的知识可能通过微调迅速恢复，并在序列建模中表现出更广泛的泛化能力。双重用途信号可能已经在预训练表示中存在，并可以通过简单的线性探测被唤起。
### Conclusion
数据过滤作为单一措施存在挑战，强调了需要进一步研究开放权重生物基础模型的稳健安全与安全策略。
## 175. `cs.AI` - Bootstrapped DQN中信息价值增强的探索 [PDF](https://arxiv.org/pdf/2511.02969), [HTML](https://arxiv.org/abs/2511.02969)
### Authors
Stergios Plataniotis,Charilaos Akasiadis,Georgios Chalkiadakis
### Background
在深度强化学习中，高效探索仍然是一个基本挑战，尤其是在高维度状态和稀疏奖励的环境中。传统的依赖于随机局部策略噪声的探索策略，如ε-贪婪和玻尔兹曼探索方法，往往难以在探索和利用之间找到有效的平衡。
### Innovation
本文将信息价值的预期值（EVOI）概念集成到广为人知的Bootstrapped DQN算法框架中，以增强该算法的深度探索能力。具体地，作者开发了两个新算法，利用信息价值的预期收益估计来测量不同网络头部意见之间的差异，并驱动探索向最具潜力的区域。
### Conclusion
实验表明，在复杂的、稀疏奖励的Atari游戏中，该算法能够提高性能，更好地利用不确定性，并且在不引入额外超参数的情况下完成任务。
## 176. `cs.AI` - Bootstrap Off-policy with World Model [PDF](https://arxiv.org/pdf/2511.00423), [HTML](https://arxiv.org/abs/2511.00423)
### Authors
Guojian Zhan,Likun Wang,Xiangteng Zhang,Jiaxin Gao,Masayoshi Tomizuka,Shengbo Eben Li
### Background
在线规划已被证明在强化学习（RL）中提高采样效率和最终性能方面非常有效。但是，使用规划进行环境交互不可避免地会导致收集的数据与策略的实际行为之间出现偏差，从而降低模型学习和策略改进的效果。
### Innovation
提出了BOOM（Bootstrap Off-policy with WOrld Model），一种通过Bootstrap循环紧密整合规划和离策略学习的框架。通过联合学习的世界模型，规划器能够模拟未来的轨迹，并提供价值目标以促进策略改进。核心在于一种基于规划器非参数动作分布的概率自由对齐损失，结合软价值加权机制，优先选择高回报行为，减轻回放缓冲区中规划器动作质量的变异性。
### Conclusion
BOOM在高维的DeepMind Control Suite和Humanoid-Bench上展示了在训练稳定性和最终性能方面达到最先进的结果。代码可在 https://github.com/boom-rl/BOOM 获取。
## 177. `cs.AI` - 基于UNet架构在多期增强计算机断层扫描中肝肿瘤分割的比较研究 [PDF](https://arxiv.org/pdf/2510.25522), [HTML](https://arxiv.org/abs/2510.25522)
### Authors
Doan-Van-Anh Ly(1),Thi-Thu-Hien Pham(2 and 3),Thanh-Hai Le(1) ((1) The Saigon International University, (2) International University, (3) Vietnam National University HCMC)
### Background
在多期增强计算机断层扫描(CECT)中，肝结构的分割对于肝病的计算机辅助诊断和治疗规划起着至关重要的作用，特别是在肿瘤检测方面。
### Innovation
研究基于UNet架构的肝脏肿瘤分割性能，从最初的UNet扩展到UNet3+，使用了多种骨干网络。引入了注意力机制，特别是采用卷积块注意力模块(CBAM)，提高了分割质量。
### Conclusion
ResNetUNet3+结合CBAM模块在重叠度指标和边界精确定位方面表现最优，其Dice分数为0.755，IoU为0.662，HD95距离为77.911，模型的整体准确度和特异性分别为0.925和0.926，展示了其在准确识别病灶和健康组织方面的强大能力。
## 178. `cs.AI` - 针对深度哈希的模型反转攻击 [PDF](https://arxiv.org/pdf/2511.12233), [HTML](https://arxiv.org/abs/2511.12233)
### Authors
Dongdong Zhao,Qiben Xu,Ranxin Fang,Baogang Song
### Background
深度哈希可以通过生成紧凑的二进制代码来提高检索效率，但同时引入了严重的隐私风险。由于可以从哈希代码恢复原始训练数据，这可能导致生物特征伪造和隐私泄露等严重威胁。然而，针对深度哈希模型的模型反转攻击尚未被探索，其安全影响尚未被研究。这一研究缺口源于真实的训练哈希代码的不可访问性以及高度离散的汉明空间，使现有方法无法适用于深度哈希。
### Innovation
提出了一种名为DHMI的新的扩散模型反转框架，用于深度哈希。DHMI首先聚类辅助数据集以推导出语义哈希中心作为代理锚点。然后引入了一种代理导向的去噪优化方法，利用一种新的攻击度量（结合分类一致性和哈希邻近性）动态选择候选样本。一系列代理模型引导这些候选样本的提炼，确保生成高保真度和语义一致性的图像。
### Conclusion
在多种数据集上的实验表明，DHMI能在最苛刻的黑盒设置下成功重建高分辨率、高质量的图像，即使没有训练哈希代码的情况下也表现出色。该方法在黑盒场景中优于现有最先进的模型反转攻击，证实了它在实践中的有效性以及深度哈希系统固有的隐私风险。
## 179. `cs.AI` - SALT: 在推理链中引导激活以实现无泄漏思考 [PDF](https://arxiv.org/pdf/2511.07772), [HTML](https://arxiv.org/abs/2511.07772)
### Authors
Shourya Batra,Pierce Tillman,Samarth Gaggar,Shashank Kesineni,Kevin Zhu,Sunishchal Dev,Ashwinee Panda,Vasu Sharma,Maheep Chaudhary
### Background
随着大规模语言模型（LLMs）演变成能够访问敏感用户数据的个人助手，它们面临一个关键的隐私挑战：虽然先前的工作已经解决了输出层的隐私问题，但最近的研究表明，LLMs通常在其内部推理过程中泄露了私人信息，违反了上下文隐私期望。这些泄露的思想发生在模型无意中在其推理痕迹中暴露敏感细节的地方，即使最终输出看起来是安全的。挑战在于阻止这种泄露，同时不牺牲模型的推理能力，需要在隐私和实用性之间进行微妙的平衡。
### Innovation
我们引入了Steering Activations towards Leakage-free Thinking (SALT)，一种轻量级的测试时间干预方法，通过在隐藏状态中注入目标引导向量来缓解模型的推理链（CoT）中的隐私泄露。我们确定了这些高泄漏层，通过跨多个LLM的实验展示，SALT实现了在QwQ-32B、Llama-3.1-8B和Deepseek中的CPL分别降低了18.2%、17.9%和31.2%。同时保持了可比的任务性能和实用性。我们的工作证明了SALT在推理能力语言模型的测试时间隐私保护方面是一种实用的方法，为基于LLM的个人代理的安全部署提供了途径。
### Conclusion
我们的研究确立了SALT作为一种实用的方法，用于推理能力强的语言模型的测试时间隐私保护，为LLM个人代理的安全部署提供了道路。
## 180. `cs.AI` - T2I-RiskyPrompt: 一个用于文本到图像模型安全性评估、攻击和防御的基准 [PDF](https://arxiv.org/pdf/2510.22300), [HTML](https://arxiv.org/abs/2510.22300)
### Authors
Chenyu Zhang,Tairen Zhang,Lanjun Wang,Ruidong Chen,Wenhui Li,Anan Liu
### Background
现有用于测试文本到图像（T2I）模型安全性的风险提示数据集存在三个主要局限性：1) 有限的风险类别；2) 粗略的标注；3) 低效。因此，迫切需要一个全面的基准来解决这些问题，以便更好地评估T2I模型的安全性。
### Innovation
1) 首次制定了一个分层风险分类体系，包含6个主要类别和14个细分类别；2) 构建了一套收集和标注风险提示的方法；3) 获取了6,432个有效的风险提示，每个提示都附有分层类别标签和详细的风险理由；4) 提出了基于原因的危险图像检测方法，明确地将MLLM与安全标注对齐；5) 基于T2I-RiskyPrompt基准，对8个T2I模型进行了全面评估，包括九种防御方法、五种安全过滤器和五种攻击策略，提供了九个关键见解，指出T2I模型安全性的强点和弱点。
### Conclusion
T2I-RiskyPrompt提供了一个综合性的基准框架，全面评估了T2I模型、防御方法、安全过滤器和攻击策略的安全性。此外，该基准还讨论了其潜在应用，强调了其在各种研究领域中的重要性。相关的数据集和代码可在此处获取：this https URL.
## 181. `cs.AI` - 桥接语义鸿沟：基于GRPO的多语言Text-to-SQL对比奖励 [PDF](https://arxiv.org/pdf/2510.13827), [HTML](https://arxiv.org/abs/2510.13827)
### Authors
Ashish Kattamuri,Ishita Prasad,Meetu Malhotra,Arpita Vats,Rahul Raja,Albert Lie
### Background
当前的Text-to-SQL方法仅专注于执行查询，而忽视了语义对齐的挑战，包括查询的语义含义以及执行结果的正确性。这些方法在从英语转换到其他语言时，执行准确率显著下降，非英语语言平均下降6个百分点。现有的方法未能有效处理语义对齐问题。
### Innovation
该论文提出了一种新的框架，将GRPO（Group Relative Policy Optimization）与多语言对比奖励信号结合，以增强跨语言场景中的Text-to-SQL系统的任务效率和语义准确度。通过基于语义相似性的奖励信号，该方法使得模型能够更好地将SQL生成与用户意图对应起来，从而提高了执行准确率和语义准确率。
### Conclusion
通过微调LLaMA-3-3B模型，使用GRPO改进了执行准确率达到87.4%（相对于零样本提高了26%），语义准确率达到52.29%（提高了32.86%）。添加对比奖励信号进一步提高了语义准确率，使平均语义准确率达到59.14%（相对于零样本提高6.85%，对越南语提高了10%）。实验表明，使用对比奖励信号微调的小型、参数有效的3B LLaMA模型在执行准确率和语义准确率上均优于相同规模的零样本8B LLaMA模型，并且所有这些只需要3000个强化学习训练样本。
## 182. `cs.AI` - 基因下一核苷酸预测器是上下文学习者 [PDF](https://arxiv.org/pdf/2511.12797), [HTML](https://arxiv.org/abs/2511.12797)
### Authors
Nathan Breslow,Aayush Mishra,Mahler Revsine,Michael C. Schatz,Anqi Liu,Daniel Khashabi
### Background
上下文学习（ICL）是一种模型从输入中提供的示例中推断和应用抽象模式的能力，在大型语言模型中得到了广泛研究，这些模型主要用于人类文本的下一个词预测。以往的研究通常将这种行为归因于人类语言的独特统计特性。然而，这一行为是否能在其他序列领域，如基因组序列中通过大规模预测训练自然地出现，是一个有待探索的问题。
### Innovation
我们转向基因序列这一统计结构丰富的符号领域，研究了主要基于下一核苷酸（A/T/C/G）预测的Evo2基因组模型，其规模与中小型语言模型相近。我们开发了一个受控实验框架，包含了语言和基因组形式的符号推理任务，以便直接比较基因组和语言模型中的ICL。结果显示，基因组模型在上下文示例数量增加时，在模式归纳上表现出对数增长。这是首次在基因组序列中发现自然 Emergent ICL 的证据，支持了 ICL 是通过丰富的数据进行大规模预测建模的结果这一假设。这些发现将 Emergent Meta-Learning 的范围扩大到了语言之外，指出了一个统一的、模态无关的上下文学习观点。
### Conclusion
研究表明，基因模型和语言模型一样，随着上下文示例数量增加，模式归纳能力也呈对数增长。这是首次在基因组序列中发现自然 Emergent ICL 的证据，未来的研究可能会更加关注这种上下文学习能力是否在其他类型的数据集中也存在，以及这种学习能力是否具有普遍的模态无关性。
## 183. `cs.AI` - SCALEX：扩散模型的可扩展概念与潜在空间探索 [PDF](https://arxiv.org/pdf/2511.13750), [HTML](https://arxiv.org/abs/2511.13750)
### Authors
E. Zhixuan Zeng,Yuhao Chen,Alexander Wong
### Background
图像生成模型经常编码社会偏见，包括与性别、种族和职业相关的刻板印象。现有的扩散模型中的偏见分析方法要么集中于预定义的类别，要么依赖于对潜在空间方向的手动解释。这些限制阻碍了可扩展性并妨碍了对微妙或未预见模式的发现。
### Innovation
SCALEX 是一个用于扩散模型潜在空间的可扩展和自动化探索框架。SCALEX 使用仅自然语言提示从 H 空间中提取语义上有意义的方向，从而使零样本解释无需重新训练或标记成为可能。这使得能系统地比较任意概念并实现大规模发现模型内部关联。我们展示了 SCALEX 检测职业提示中的性别偏见、按身份描述符对语义对齐进行排名，并揭示无监督条件下的概念簇结构。
### Conclusion
通过将提示直接链接到潜在方向，SCALEX 使扩散模型中的偏见分析更加可扩展、可解释和可扩展性超过先前的方法。
## 184. `cs.AI` - SweeperBot: 通过视图分析和视觉问答使3D浏览无障碍 [PDF](https://arxiv.org/pdf/2511.14567), [HTML](https://arxiv.org/abs/2511.14567)
### Authors
Chen Chen,Cuong Nguyen,Alexa Siu,Dingzeyu Li,Nadir Weibel
### Background
对于屏幕阅读器(SR)用户而言，访问3D模型仍然是一个挑战。虽然有些现有的3D查看器允许创作者提供替代的文字描述，但是这些描述往往无法充分详实。基于一个先导性研究，本文介绍了SweeperBot系统，该系统使SR用户能够利用视觉问答技术来探索和比较3D模型。
### Innovation
SweeperBot通过结合最优视角选择技术和基于生成和识别的基础模型优势，回答SR用户的视觉问题。这项技术使盲人和低视力(BLV)用户能够通过屏幕阅读器探索和比较3D模型。
### Conclusion
一个包含10名有SR经验的盲人及低视力(BLV)用户的专家评审表明，SweeperBot具有可行性。另一项涉及30名视力正常者的调查表明，SweeperBot生成的描述质量得到了验证。
## 185. `cs.AI` - 当偏见伪装成真相：统计关联如何削弱大语言模型中的幻觉检测 [PDF](https://arxiv.org/pdf/2511.07318), [HTML](https://arxiv.org/abs/2511.07318)
### Authors
Shaowen Wang,Yiqi Dong,Ruinian Chang,Tansheng Zhu,Yuebo Sun,Kaifeng Lyu,Jian Li
### Background
尽管取得了显著的进步，大型语言模型（LLMs）仍然会出现幻觉现象，即生成可能但不正确的响应。本文聚焦于一种被严重忽视但又至关重要的幻觉类型，即由虚假关联驱动的幻觉，这些关联是训练数据中表面看似相关但实际上统计上显著的特征（如姓氏）和属性（如国籍）之间的表面联系。研究表明，这些虚假关联引发的幻觉充满了信心，不受模型规模的影响，能够躲避当前的检测方法，即使经过拒绝微调后仍然存在。通过系统控制的合成实验和对最先进的开源和专有LLM（包括GPT-5）的实证评估，证明了现有的幻觉检测方法，如基于置信度的过滤和内状态探针，在虚假关联的存在下根本无效。进一步的理论分析揭示了为什么这些统计偏差会从根本上破坏依靠置信度的检测技术。
### Innovation
研究表明现有的幻觉检测方法在虚假关联存在的情况下完全无效。本文通过系统控制的合成实验和实证评估证明了这一点，特别是揭示了现有方法在面对虚假关联时的失败。此外，通过理论分析进一步阐明了为什么统计偏差会根本上削弱置信度检测技术的有效性。
### Conclusion
这些发现强调了需要设计新的方法来专门解决由虚假关联引起的幻觉的紧迫性。新方法将专门针对这种类型的幻觉，以提高大语言模型的可靠性和准确性。
## 186. `cs.AI` - WER is Unaware: Assessing How ASR Errors Distort Clinical Understanding in Patient-Facing Dialogue [PDF](https://arxiv.org/pdf/2511.16544), [HTML](https://arxiv.org/abs/2511.16544)
### Authors
Zachary Ellis,Jared Joselowitz,Yash Deo,Yajie He,Anna Kalygina,Aisling Higham,Mana Rahimzadeh,Yan Jia,Ibrahim Habli,Ernest Lim
### Background
自动语音识别（ASR）在临床对话中的应用越来越广泛，目前的评估标准仍然主要依赖于单词错误率（WER）。然而，研究者发现WER和其他常见指标与转录错误的临床影响关联性不高。
### Innovation
该论文提出了LLM-as-a-Judge的方法，利用GEPA通过DSPy进行程序优化，模拟专家的临床评估来填补评估空白。优化后的模型（Gemini-2.5-Pro）可达到与人类相当的性能，90%的准确率和Cohen's κ值为0.816。
### Conclusion
研究提供了一个验证过的自动框架，以超越简单的文本一致性的ASR评估，转向对临床对话安全性进行必要的、可扩展的评估。
## 187. `cs.AI` - 基于监督对比学习的少量样本AI生成图像检测及溯源 [PDF](https://arxiv.org/pdf/2511.16541), [HTML](https://arxiv.org/abs/2511.16541)
### Authors
Jaime Álvarez Urueña,David Camacho,Javier Huertas Tato
### Background
随着生成型人工智能的快速发展，合成图像不再容易与真实内容区分开来，这对数字媒体的完整性构成了重大挑战。新型生成模型的快速发布进一步增加了检测辨别合成图像的难度，传统的依赖于定期重新训练的检测方法在计算上不再可行，操作上也不切实际。
### Innovation
本文提出了一种新颖的两阶段检测框架，旨在应对合成图像检测中的泛化挑战。第一阶段利用监督对比学习训练的视觉深度学习模型从输入图像中提取有区别的嵌入表示。该模型的训练采用了特定划分的数据集，特定的生成器架构未参与训练，以严格消除跨生成器的泛化能力。第二阶段运用K近邻分类器在学习到的嵌入空间中运作，采用少量样本进行微调学习。即使在每次类仅使用150张图像的少量样本学习环境下，所提出的框架也达到了91.3%的平均检测准确率。与现有方法相比，提升幅度5.2个百分点。对于源属性任务，所提出的方法在封闭集分类环境下分别在AUC和OSCR上取得了14.70%和4.27%的提升，标志着向更加稳健有效和可扩展的溯源系统迈出了重要一步，这些系统能够适应生成AI不断变化的生态环境，无需进行彻底的重新训练。
### Conclusion
提出的两阶段检测框架表明，通过监督对比学习训练的少量样本视觉深度学习模型和K近邻分类器在检测和溯源合成图像方面具有卓越性能，能够有效应对合成图像泛化挑战，具备适应生成型人工智能生态系统变化的能力，无需全面重新训练。
## 188. `cs.AI` - 控制丧失手册：程度、动态与准备 [PDF](https://arxiv.org/pdf/2511.15846), [HTML](https://arxiv.org/abs/2511.15846)
### Authors
Charlotte Stix,Annika Hallensleben,Alejandro Ortega,Matteo Pistillo
### Background
现有的AI系统中缺乏一个有效的丧失控制（LoC）定义，导致在LoC评估和减轻方面难以形成有效的方法。尽管政策和研究不断关注，但现有的LoC定义在范围和时间上差异较大，这阻碍了LoC的有效管理。
### Innovation
提出了一个新的分级LoC分类法，基于严重性和持续时间区分三种类型：偏移、边界控制丧失和严格控制丧失。研究还提出了一种不仅关注AI能力及其易变性，还强调部署环境、机会和许可（DAP框架）的策略来避免社会易受攻击状态。
### Conclusion
为了避免LoC的发生，提出了社会治理措施和技术控制措施，以维持一种持久的戒备状态。同时，建立了一个持续准备的计划，防止在社会易受攻击状态下出现LoC事件。
## 189. `cs.AI` - AudAgent：AI代理中的隐私政策合规自动审计 [PDF](https://arxiv.org/pdf/2511.07441), [HTML](https://arxiv.org/abs/2511.07441)
### Authors
Ye Zheng,Yidan Hu
### Background
AI代理可以自主执行任务，但通常在没有明确用户同意的情况下收集或披露用户的敏感本地数据，这引发了严重的隐私问题。虽然AI代理的隐私政策描述了其预期的数据使用方式，但仍存在透明度和问责制的限制，即运行时行为是否与这些政策匹配。为了弥合这一差距，该文提出了AudAgent，一种视觉工具，实时监控AI代理的数据使用行为，并确保遵守声明的隐私政策。AudAgent 包含四个组件，用于自动化审计AI代理的隐私：（i）政策形式化、（ii）运行时标注、（iii）合规审计、（iv）用户界面，以实现透明和问责。评估结果表明，AudAgent 能够实时检测并可视化隐私政策的违规情况。此外，还发现在现有隐私政策中，大多数未明确为高度敏感数据（例如 SSN）提供保障措施，且许多代理通过第三方工具处理这些数据，而这些第三方工具不受代理商自身隐私政策的控制。
### Innovation
该文的创新在于提出了AudAgent工具，用于实时监控AI代理的数据做法及其与隐私政策的合规性，包括：（i）创造性地使用跨LLM投票机制以确保解析隐私模型的置信度；（ii）以轻量级的方式使用Presidio检测敏感数据并基于AI代理的上下文和隐私政策模型标注数据做法；（iii）利用本体图和自动机检查将隐私政策模型与运行时标注连接起来，实现实时合规检查；（iv）提供基础设施无关的用户界面，使用户能够实时可视化AI代理的执行轨迹及潜在的隐私政策违规，提供易于理解的透明性和问责制。
### Conclusion
AudAgent 在使用主流框架构建的AI代理中进行了评估，证明了其在实时检测和可视化隐私政策违规方面的效果。同时也发现大多数现有的隐私政策在处理高度敏感数据（如SSN）方面的保护不足，许多代理依赖于不受合规控制的第三方工具进行数据处理。AudAgent 实施了主动阻止这些操作，从而更改了代理的原始隐私政策和行为，提高了透明性和问责制。
## 190. `cs.AI` - VLA-Pruner: 依赖于时间的双层视觉 token 剪枝方法以实现高效的视觉-语言-行动推理 [PDF](https://arxiv.org/pdf/2511.16449), [HTML](https://arxiv.org/abs/2511.16449)
### Authors
Ziyan Liu,Yeqiu Chen,Hongyi Cai,Tao Lin,Shuo Yang,Zheng Liu,Bo Zhao
### Background
Vision-Language-Action (VLA) 模型在物质人工智能中表现出巨大潜力，但连续视觉流的处理带来了巨大的计算成本，严重限制了其实时部署。为了加速 Vision-Language Models (VLM)，出现了 token 剪枝技术，即保留显著的视觉 token 并丢弃冗余的 token。然而，现有的针对 VLM 的 token 剪枝方法仅基于语义显著性指标（如预填充注意）来选择 tokens，忽视了 VLA 的内在双系统特性（高层语义理解和低层行动执行），倾向于保留语义线索，却抛弃了用于生成行动的关键信息。因此，这些方法显著降低了 VLA 性能。
### Innovation
我们提出了一种名为 VLA-Pruner 的通用、插拔式 VLA 特定 token 剪枝方法，该方法结合了双层的重要性标准来保留视觉 token：视觉-语言预填充注意用于衡量语义相关性，通过时间平滑估计的行动解码注意用于衡量行动的重要性。基于这一标准，VLA-Pruner 提出了一种新颖的双层 token 选择策略，在给定的计算预算下，自适应地保留一套既能用于语义理解又能用于行动执行的紧凑且信息丰富的视觉 token。
### Conclusion
实验表明，VLA-Pruner 在多个 VLA 架构和多样化的人形机器人任务上实现了最先进的性能。
## 191. `cs.AI` - 通过解耦和最佳N猜测实现快速大型语言模型后训练 [PDF](https://arxiv.org/pdf/2511.16193), [HTML](https://arxiv.org/abs/2511.16193)
### Authors
Rongxin Cheng,Kai Zhou,Xingda Wei,Siyuan Liu,Mingcong Han,Mingjing Ai,Yeju Zhou,Baoquan Zhong,Wencong Xiao,Rong Chen,Haibo Chen
### Background
在大型语言模型（LLM）的后训练阶段，生成过程会主导训练时间，模型需要根据输入的提示生成对应的标记。研究人员注意到，虽然目前提高了解码速度的方法已经存在，但当面对大规模并行执行时，这些方法的表现不尽如人意，尤其是在加速无法并行的部分生成时更为困难。因此，需有新的方法来解决现有的挑战。
### Innovation
该论文提出了一种名为SpecActor的方法，通过推测性解码来实现快速生成，具体创新点包括：1. 一种动态解耦推测执行方法，优化GPU计算效率以实现大规模并行执行的加速；2. 一种动态最佳N推测方法，根据推测过程选择和组合不同的起草策略，提高推测准确性，不增加额外计算资源。
### Conclusion
SpecActor方法在端到端训练中比veRL快1.7倍，在与经典方法的对比中表现显著，提高了推测速度且无需额外的计算资源。
## 192. `cs.AI` - MF-GCN: 一种用于眼动追踪、面部和声学特征三模态抑郁症检测的多频图卷积网络 [PDF](https://arxiv.org/pdf/2511.15675), [HTML](https://arxiv.org/abs/2511.15675)
### Authors
Sejuti Rahman,Swakshar Deb,MD. Sameer Iqbal Chowdhury,MD. Jubair Ahmed Sourov,Mohammad Shamsuddin
### Background
抑郁症是一种普遍存在的全球性精神健康疾病，其特点为持续的情绪低落和感受乐趣的能力丧失。然而，由于现有的诊断方法依赖于主观的临床评估，抑郁症的诊断仍然不足。为了实现客观检测，该研究通过一个整合眼动追踪数据、音频和视频的独特三步骤数据收集方法，引入了一个包含103名临床评估参与者的基准数据集，为抑郁症状提供了全面的表征。该数据集通过统计验证证明了其在区分抑郁症和非抑郁症组方面的显著区分能力。
### Innovation
该研究提出了一种新型的多频图卷积网络（MF-GCN），以解决现有基于图的模型专注于低频信息的局限性。MF-GCN框架包含一个多频滤波器模块（MFFBM），可以利用低频和高频信号。在与传统机器学习算法和深度学习框架的广泛评估中，MF-GCN 模型在二分类任务中实现了0.96的敏感性和0.94的F2分数，在三分类任务中，其敏感性为0.79，特异性为0.87，并显著超过了其他模型。
### Conclusion
我们的三模态多频框架有效地捕捉跨模态的交互，使得准确检测抑郁症成为可能。此外，该模型在中文多模态抑郁症语料库（CMDC）数据集上的测试也证明了其泛化能力，实现了0.95的敏感性和0.96的F2分数。这些结果验证了本文提出的框架的有效性。
## 193. `cs.CL` - LLMs如何理解 Tunisian 阿拉伯语？ [PDF](https://arxiv.org/pdf/2511.16683), [HTML](https://arxiv.org/abs/2511.16683)
### Authors
Mohamed Mahdi
### Background
大型语言模型（LLMs）是当今AI代理的驱动力。这些模型对人类语言的理解程度直接影响与AI的交互自然度与友好度。然而，工业规模的LLMs在理解低资源语言，如塔吉尼阿拉伯语（Tunizi），方面经常被忽视。这种忽视可能会排除数百万塔吉尼人与AI完全互动的机会，迫使他们转向法语或英语。这种转变不仅威胁到了塔吉尼方言的保存，也可能导致字面教育问题，并影响年轻一代偏向外语。
### Innovation
该研究引入了一个包含塔吉尼、标准塔吉尼阿拉伯语和英语平行翻译的新数据集，并包含情感标签。研究对几种流行的LLMs进行了基准测试，任务包括转写、翻译和情感分析。结果揭示了不同模型在理解和发展塔吉尼方言方面存在显著差异，这突显了在下一代AI系统中包括低资源语言的重要性，以确保技术的可及性、包容性和文化根基。
### Conclusion
通过量化这些差距，这项工作强调了在未来的AI系统中包括低资源语言的重要性，以确保技术的可及性、包容性和文化根基，并且这种研究填补了在低资源语言处理方面的研究空白。
## 194. `cs.CL` - 基于椭球的决策边界在开放意图分类中的应用 [PDF](https://arxiv.org/pdf/2511.16685), [HTML](https://arxiv.org/abs/2511.16685)
### Authors
Yuetian Zou,Hanlei Zhang,Hua Xu,Songze Li,Long Xiao
### Background
文本开放意图分类对于实际对话系统至关重要，它能够在没有先验知识的情况下检测未知用户意图，增强系统的鲁棒性。现有的适应性决策边界方法通过消除手动阈值调优展示了巨大的潜力，但这些方法假设已知类别的分布是各向同性的，限制了边界为球形，并忽视了不同方向上的分布变化。
### Innovation
提出了一种名为EliDecide的新方法，学习不同特征方向具有不同尺度的椭球决策边界。首先，使用监督对比学习获得区分性特征空间。其次，使用可学习矩阵来参数化每个已知类别的边界为椭球，提供比仅由中心和半径定义的球形边界更大的灵活性。然后，通过一种新型双重损失函数优化边界，平衡经验风险和开放空间风险：边界扩展以覆盖已知样本，同时向合成的伪开放样本收缩。
### Conclusion
该方法在多个文本意图基准测试和一个问题分类数据集上达到了最先进的性能。椭球的灵活性显示出优于开放意图检测的能力，并且对于更复杂的开放世界场景下的多种文本分类任务具有强大的泛化潜力。
## 195. `cs.CL` - 在多语言LLM中，语言方向如何与标记几何对齐 [PDF](https://arxiv.org/pdf/2511.16693), [HTML](https://arxiv.org/abs/2511.16693)
### Authors
JaeSeong Kim,Suan Lee
### Background
多语言大型语言模型（LLM）在多种语言上展现出强大的性能，然而，这些模型内部表示空间中语言信息的结构及其在各层间的涌现尚缺乏系统的分析。本文通过使用线性和非线性探针，并配合全新的Token-Language Alignment分析方法，系统地研究了六大多语言LLM模型，覆盖所有268个转子器层，目的是量化语言编码的层间动态和几何结构。
### Innovation
本研究首次通过多方面的方法检测和量化了多语言LLM内部语言编码的变化。研究发现，语言信息在首个转子器块中迅速分离，并在整个模型深度中保持高度线性可分性。研究还揭示了语言方向与词汇嵌入之间的对齐高度依赖于训练数据的语言构成，表明中国的语言模型（包含中文）在语言对齐度上明显优于以英语为主的模型，显示出4.21倍的结构烙印效应。这些发现表明，多语言LLM通过训练语料库塑造的潜在表征结构来区分语言，而不仅仅是表面书写特征。
### Conclusion
研究结果强调了数据组成策略和多语言表示学习公平性的实用见解。所有代码和分析脚本已在公开网站上提供，便于进一步研究。
## 196. `cs.AI` - Live-SWE-agent: 软件工程智能代理能否自主实时演化？ [PDF](https://arxiv.org/pdf/2511.13646), [HTML](https://arxiv.org/abs/2511.13646)
### Authors
Chunqiu Steven Xia,Zhe Wang,Yan Yang,Yuxiang Wei,Lingming Zhang
### Background
大规模语言模型（LLMs）正在改变包括软件工程在内的几乎所有行业。近年来，研究人员提出了多种能够解决实际软件问题的LLM代理。这些代理通常具备一套编码工具，并能自主决定下一步行动以完成从头到尾的软件任务。虽然它们前景广阔，但通常需要专门设计，并且仍然可能不足够优化。因为探索整个代理架构的设计空间可能是极其具有挑战性和成本高昂的。
### Innovation
本论文提出了Live-SWE-agent，这是第一个可以自主和连续地在运行时演化以解决真实世界软件问题的软件代理。Live-SWE-agent 从最基本的代理结构开始，仅具有bash工具的访问权限（例如mini-SWE-agent），并在解决实际世界软件问题的过程中自主改进其内部框架实现。本文评价了该系统在广泛研究的SWE-bench Verified基准上的性能，其解题率为77.4%（无测试时缩放），并且在SWE-Bench Pro基准上也表现出色，达到45.8%的最高已知解题率，优于所有现有软件代理，甚至优于最新的专用解决方案。
### Conclusion
本研究提出了Live-SWE-agent，这是一种能够在运行时自主演化以解决现实世界软件问题的软件代理。实验结果表明，Live-SWE-agent 在解决实际问题的能力上超过了所有现有软件代理，并达到了最佳的解题率，展示了实时自主进化软件代理在软件工程领域的潜力。
## 197. `cs.AI` - 三维视角下的测试时扩展：上下文、批次和轮次的3D视角 [PDF](https://arxiv.org/pdf/2511.15738), [HTML](https://arxiv.org/abs/2511.15738)
### Authors
Chao Yu,Qixin Tan,Jiaxuan Gao,Shi Yu,Hong Lu,Xinting Yang,Zelai Xu,Yu Wang,Yi Wu,Eugene Vinitsky
### Background
近期研究表明，强化学习（RL）表现出一种新的扩展效应：测试时扩展效应。思考模型如R1和o1在较长的推理上下文环境中推理准确性得到提升。然而，相比训练时扩展，测试时扩展受底层模型上下文长度的限制，而这个长度远远小于训练期间消耗的令牌数量。
### Innovation
本文提出了一种多维度的测试时扩展框架，超越了传统的上下文长度扩展，提出两种额外的维度：批次扩展和轮次扩展。基于此视角提出了三维测试时扩展，整合了上下文、批次和轮次扩展。实验结果表明：每种扩展在一定容量内显示出测试时扩展效应；结合三个维度显著提高挑战性测试环境下的推理性能，并从人类偏好反馈中获益；框架自然扩展至更开放的领域，即具身学习，推动了类人控制行为的设计。
### Conclusion
文章展示了通过上下文、批次和轮次的三维视角，可以扩展测试时的推理能力，不仅提升了模型在特定任务上的性能，还为更广泛的应用场景（如具身学习）提供了可能性。
## 198. `cs.CL` - 大规模语言模型基于提示的价值导向 [PDF](https://arxiv.org/pdf/2511.16688), [HTML](https://arxiv.org/abs/2511.16688)
### Authors
Giulio Antonio Abbo,Tony Belpaeme
### Background
随着大模型在需要与人类价值观对齐的应用中被越来越多地使用，模型微调常被用来确保安全的响应。然而，这项技术是静态的，不适用于涉及动态价值观和偏好情况。在此背景下，本研究提出了一个实用、可复制且不依赖特定模型的方法，用以评估提示是否能有效引导生成的文本朝向特定的人类价值观，同时也量化目标价值观在生成回应中的表现和增加情况。
### Innovation
本研究提出了一种方法，通过固定模型基础，在不改变模型本身或动态优化提示的情况下，应用Schwartz理论和结构化对话数据集对提示进行评估，实现价值导向。
### Conclusion
研究通过将原始提示与明确受价值观条件的提示进行对比，表明即使不修改模型或动态优化提示，价值导向也是可行的。
## 199. `cs.CL` - 基于不知词汇查询的层次检索：SNOMED CT 案例研究 [PDF](https://arxiv.org/pdf/2511.16698), [HTML](https://arxiv.org/abs/2511.16698)
### Authors
Jonathon Dilworth,Hui Yang,Jiaoyan Chen,Yongsheng Gao
### Background
SNOMED CT 是一种生物医学本体，具有大量概念的层次化表示。由于语言歧义、同义词和多义词等因素，知识检索对于其应用至关重要但又常常充满挑战。尤其是在词汇不在本体中时（OOV），查询变得尤为困难，因为没有相应的等价匹配。本研究聚焦于如何使用基于语言模型的本体嵌入方法检索SNOMED CT中的层次概念。
### Innovation
提出了一种基于语言模型的本体嵌入方法，用于处理SNOMED CT中的OOV查询。通过构建标注了SNOMED CT概念的OOV查询，评估了直接子类及其不相关的祖先类的检索效果。实验结果表明，该方法优于基于SBERT的基线方法和其他词法匹配方法。该方法在SNOMED CT上的评估结果表明其通用性，并且可以推广到其他本体。
### Conclusion
提出的基于语言模型的本体嵌入方法在处理SNOMED CT中的OOV查询时表现出色，优于现有基线方法。该方法不仅适用于SNOMED CT，也可推广应用于其他本体。研究提供了代码、工具和评估数据集，为进一步研究奠定了基础。
## 200. `cs.CL` - 错误指控：AI检测器如何误判轻微润色的阿拉伯文章 [PDF](https://arxiv.org/pdf/2511.16690), [HTML](https://arxiv.org/abs/2511.16690)
### Authors
Saleh Almohaimeed,Saad Almohaimeed,Mousa Jari,Khaled A. Alobaid,Fahad Alotaibi
### Background
尽管已经开发了许多AI检测模型来识别由人工智能创造的文章，但是如果一篇由人类撰写的论文经过轻微的AI润色，这些模型可能会误判，将之判定为AI生成的文章。这可能导致错误指责作者的AI剽窃行为，损害AI检测系统的可信度。此前有一些研究尝试解决这个问题，但大多数研究都集中在英语上，而阿拉伯语尚未得到充分研究处理。
### Innovation
本文生成了两个数据集。第一个数据集包含800篇阿拉伯文章，其中一半是AI生成的，一半是由人类撰写的，用于评估14个大型语言模型（LLMs）和商业AI检测器的能力，以评估它们在区分人类撰写的文章和AI生成的文章方面的表现。选择表现最佳的8个模型进行进一步研究，以检查它们是否将轻微润色的人类文本误判为AI生成的。第二个数据集Ar-APT包含了400篇由10个LLM以4种润色设置润色的阿拉伯人撰写的论文，总计16400个样本，用于进一步评估8个提名模型的表现。结果表明，所有AI检测器都错误地将大量文章归类为AI生成的文章，最佳的LLM Claude-4 Sonnet在没有润色的情况下达到了83.51%的准确率，但在受到LLaMA-3轻微润色的影响后，性能降至57.63%。相比之下，最优秀的商业模型也大幅下降，从92%的准确率降低到使用MISTRAL或GEMMA-3轻微润色的文章中只有12%的正确率。
### Conclusion
所有测试的AI检测器都出现了不同程度的误判，最好的LLM和商业模型在文章被轻微润色后，其性能出现了显著下降。这凸显了阿拉伯语环境下的AI剽窃检测挑战，需要进一步优化AI检测模型以提高它们对轻微润色文本的识别准确性。
## 201. `cs.CL` - 检测和引导大语言模型在行动中的同理心 [PDF](https://arxiv.org/pdf/2511.16699), [HTML](https://arxiv.org/abs/2511.16699)
### Authors
Juan P. Cadile
### Background
本文研究了“行动中的同理心”——在任务效率与人类需求之间愿意进行权衡的行为——在大语言模型激活空间中的线性方向。研究使用基于同理心在行动（EIA）基准的对比提示，评估了不同模型在检测和引导方面的表现。
### Innovation
研究创新地使用对齐于EIA基准的对比提示，检测和引导Phi-3-mini-4k、Qwen2.5-7B（安全训练）和Dolphin-Llama-3.1-8B（未受限）模型在行动中的同理心。实验发现，未受限制的Dolphin和安全训练的Qwen在同理心编码方面表现类似，表明同理心编码在不受安全训练的情况下也能够出现。并且揭示了架构特定的实现方式，即便在检测上具有一定的收敛性，各模型在引导层面的共识相对有限。研究表明Qwen和Phi-3在双向平稳性方面表现良好，而Dolphin仅在促进同理心方面表现稳定，但在反向同理心引导方面表现不佳。
### Conclusion
模型在检测和引导同理心方面的表现存在差异。Qwen和Phi-3维持双向一致性；而Dolphin仅在增强同理心方面表现稳定。安全训练可能影响引导的稳健性，而不是完全防止操纵。但更多模型的验证是必要的。
## 202. `cs.CL` - Shona spaCy: 一种用于资源不足班图语的形态分析器 [PDF](https://arxiv.org/pdf/2511.16680), [HTML](https://arxiv.org/abs/2511.16680)
### Authors
Happymore Masoka
### Background
尽管自然语言处理（NLP）在多语言处理方面取得了快速进展，但舍豪纳语（Shona）在形态分析和语言感知工具方面仍处于服务不足的状态。该论文介绍了Shona spaCy，这是一种基于spaCy框架的开源、基于规则的形态分析管道，旨在解决舍豪纳语的这一问题。
### Innovation
Shona spaCy采用一个精心策划的JSON词库和基于语言的规则，结合了名词前缀、动词主语配套、时态标记、语素和依音节词等模型，将其整合到标记级别注释中，包括词干、词性以及形态特征。该工具通过pip install shona-spacy安装，并可在多个平台获取源代码。
### Conclusion
Shona spaCy在形式和非正式舍豪纳语语料库上的评估显示，其词性标注准确率和形态特征准确率分别为90%和88%，同时保持了其语言决定的透明性。通过将描写语法与计算实现相结合，Shona spaCy促进了舍豪纳语的NLP易用性和数字包容性，并为其他资源不足的班图语提供了形态分析工具的模板。
## 203. `cs.CL` - 向VecDB中高效RAG系统的分布式并行多分辨率向量搜索 [PDF](https://arxiv.org/pdf/2511.16681), [HTML](https://arxiv.org/abs/2511.16681)
### Authors
Dong Liu,Yanxuan Yu
### Background
Retrieval-Augmented Generation (RAG)系统已经成为增强大型语言模型（LLMs）外部知识的主要方法。现有向量数据库（VecDB）检索管道依赖于扁平或单一分辨率的索引结构，不能适应各种用户查询所需的多种语义粒度。这种限制导致在检索速度和上下文相关性之间存在糟糕的权衡。
### Innovation
作者提出了Semantic Pyramid Indexing (SPI)，这是一种新颖的多分辨率向量索引框架，引入了查询自适应分辨率控制，适用于VecDB中的RAG。与现有需要离线调优或单独模型训练的分层方法不同，SPI通过轻量级分类器在整个文档嵌入上构建语义金字塔，并根据每个查询动态选择最优分辨率等级。这种自适应方法允许从粗到细的检索逐步进行，显著加速搜索同时保持语义覆盖。
### Conclusion
SPI在FAISS和Qdrant等多个RAG任务中表现出色，检索速度提高最多5.7倍，内存效率提高1.8倍，端到端QA F1分数提高2.5分。理论分析提供了检索质量和延迟的保证，广泛的消融研究验证了每个组件的贡献。该框架与现有VecDB基础设施的兼容性使其可以轻松部署在生产RAG系统中。
## 204. `cs.CL` - 基于概念的可解释性在有害内容检测中的应用 [PDF](https://arxiv.org/pdf/2511.16689), [HTML](https://arxiv.org/abs/2511.16689)
### Authors
Samarth Garg,Deeksha Varshney,Divya Singh
### Background
社交媒体的兴起不仅促进了沟通，还使得有害内容的传播变得简单。尽管已经在文本数据中检测有毒语言方面取得了显著进展，但基于概念的解释在有害内容检测中的应用仍然是一个有限的领域。本研究利用了有害内容检测数据集中存在的各类子类型属性，如淫秽、威胁、侮辱、身份攻击和性暗示作为识别语言是否有害的强大指标。然而，这些概念对目标类别的不适当归因往往会导致分类错误。
### Innovation
本研究引入了基于Concept Gradient (CG)方法的可解释性技术，通过测量改变概念如何直接影响模型输出来提供更为因果的解释。这种技术扩展了传统机器学习中的基于梯度的方法，后者往往仅聚焦于输入特征。研究中还提出了目标词汇集的策展方法，用于捕获导致文本分类模型误分类的有毒词汇，并通过计算Word-Concept Alignment (WCA)分数来量化这些词汇导致错误的程度。此外，研究还提出了一种词汇集无依赖的增强策略，通过生成排除预定义有毒词汇集的有毒样本，来检验在去除明确定义的词汇重叠时，过度归因是否仍然存在。
### Conclusion
该研究通过概念归因的减少，为检查更广泛的有毒语言模式提供了见解，同时证明了可以在没有显式词汇重叠的情况下，进一步探究模型对更广义的有毒语言的归因情况。
## 205. `cs.CL` - 可解释的维度支持意向性与 telicity 对分裂不及物动词的影响 [PDF](https://arxiv.org/pdf/2511.16824), [HTML](https://arxiv.org/abs/2511.16824)
### Authors
Eva Neu,Brian Dillon,Katrin Erk
### Background
不及物动词分为两类：unergatives（不及物主动）和unaccusatives（不及物被动）。长期以来认为描述主动动作的动词更可能出现在unergative结构中，而描述telic事件的动词更可能出现在unaccusative结构中。然而，Kim等人（2024）的研究表明，动词的意向性和telicity对于预测不及物动词的句法行为效果不佳。
### Innovation
本研究利用来自意向性和telicity两端种子词的可解释维度重新审视了这一问题。研究发现，unergativity/unaccusativity与agentivity/telicity存在关联，并表明将可解释维度与人类判断结合使用可以为无法通过评级任务轻易评估的语义属性提供有价值的信息。
### Conclusion
我们的发现支持了unergativity/unaccusativity与agentivity/telicity之间的联系，并证明了使用可解释维度结合人类判断可以为难以通过评级任务评估的语义属性提供有价值的信息。
## 206. `cs.CL` - PEPPER: 基于感知导向的扰动以增强文本到图像扩散模型中的鲁棒后门防御 [PDF](https://arxiv.org/pdf/2511.16830), [HTML](https://arxiv.org/abs/2511.16830)
### Authors
Oscar Chew,Po-Yi Lu,Jayden Lin,Kuan-Hao Huang,Hsuan-Tien Lin
### Background
最近的研究表明，文本到图像（T2I）扩散模型容易受到后门攻击的影响，输入提示中的触发器可能会引导生成有害或意外的内容。
### Innovation
我们引入了PEPPER（感知导向的扰动），这是一种后门防御方法，它可以重新编写标题，使其在语义上相差甚远但视觉上相似，同时添加非干扰元素。这种方法破坏了输入提示中嵌入的触发器，稀释了触发器词的影响，从而提高了模型的鲁棒性。
### Conclusion
实验证明，PEPPER特别有效地对抗基于文本编码器的攻击，同时显著降低了攻击成功率，同时保持了生成质量。此外，PEPPER可以与其他现有的防御方法结合使用，从而实现更强大和泛化的鲁棒性，超过任何单一方法。我们将在GitHub上发布代码。
## 207. `cs.CL` - 重现报告：大型语言模型的最近邻测试时训练 [PDF](https://arxiv.org/pdf/2511.16691), [HTML](https://arxiv.org/abs/2511.16691)
### Authors
Boyang Zhou,Johan Lindqvist,Lindsey Li
### Background
该论文重现了Test-Time Training on Nearest Neighbors for Large Language Models（Hardt and Sun, 2024）的中心论点。该论文提出了一种在推理时通过检索最近邻序列进行微调语言模型的方法。通过使用预训练的RoBERTa嵌入并用Faiss索引，作者检索了每个测试输入的20个最近邻，并在GPT-2（117M、774M），GPT-Neo（1.3B）和R1-Distilled-Qwen2.5-1.5B模型上对每个邻居应用了一个梯度更新。该论文的实验结果证实，测试时训练可以显著降低从The Pile等多样化领域中提取的模型的困惑度和位/字度量标准，最大的改进出现在结构化或专业数据集，如GitHub和EuroParl中。
### Innovation
1. 作者提出了一种记忆高效的检索实现方式，该方式仅加载所需行偏移而不是整个文件，从而将每台服务器的RAM需求从超过128 GB减少到32 GB。2. 检查了R1-Distilled-Qwen2.5-1.5B模型，进一步验证了测试时训练在现代推理优化架构中的一致收益。3. 确认模型未在The Pile上预训练的模型比已经训练在相似数据上的模型从这种适应中受益更多，使得较小模型可以接近较大模型的性能。
### Conclusion
总体而言，实验结果支持最近邻测试时训练的健壮性和通用性，并指出了大规模检索增强适应的实用考虑。
## 208. `cs.CL` - ConCISE: 一个无需参考的大语言模型生成答案简洁性评估指标 [PDF](https://arxiv.org/pdf/2511.16846), [HTML](https://arxiv.org/abs/2511.16846)
### Authors
Seyed Mohssen Ghafari,Ronny Kol,Juan C. Quiroz,Nella Luan,Monika Patial,Chanaka Rupasinghe,Herman Wandabwa,Luiz Pizzato
### Background
大语言模型（LLMs）经常生成冗长且繁琐的回应，包含冗余或不必要的细节，这降低了清晰度和用户满意度，并增加了模型开发成本，尤其是对于收费基于输出token数量的知名专有模型。
### Innovation
提出了一种无需参考的大语言模型生成答案简洁性评估指标ConCISE。该方法不依赖于黄金标准参考材料，通过三种计算的平均值量化非必要的内容：一是原始回应与LLM自动生成摘要之间的压缩比；二是原始回应与LLM抽取式摘要之间的压缩比；三是通过LLM移除答案中的非必要词语，保留其意义，并以移除token数量表示简洁性得分。实验结果表明该指标能够识别LLM输出的冗余内容，为自动评估对话AI系统回应简洁性提供实用工具，无需真实人类注解。
### Conclusion
所提出的方法能够帮助评估LLM生成的回答的简洁性，提供一种无需真实注解的自动化评估工具，在对话AI系统中具有实际应用价值。
## 209. `cs.CL` - 预测诱导头的形成 [PDF](https://arxiv.org/pdf/2511.16893), [HTML](https://arxiv.org/abs/2511.16893)
### Authors
Tatsuya Aoyama,Ethan Gotlieb Wilcox,Nathan Schneider
### Background
研究表明，特意设计的关注头（称为诱导头IH）是现代语言模型具备上下文学习能力的关键。然而，IH是如何形成的仍不明确。
### Innovation
本研究探索了训练数据的统计属性（包括天然数据和合成数据）与IH形成之间的关系。研究发现了如下三个创新点：1）一个简单的方程结合批量大小和上下文大小可以预测IH形成的临界点；2）表层二元重复频率和可靠性对IH形成有强烈影响，并且在这些参数上找到了精确的 pareto 边界；3）高二元重复频率和可靠性可充分支持IH形成，但在频率和可靠性较低时，类别性和边缘分布的形状变得重要。
### Conclusion
研究展示了IH形成的精确预测因子，并指出统计学上的数据特性可以可靠预测IH的形成，从而提供了提升语言模型上下文学习能力的新视角。
## 210. `cs.CL` - 大型语言模型监督微调在特定领域知识图构建中的应用：基于湖南历史名人的案例研究 [PDF](https://arxiv.org/pdf/2511.17012), [HTML](https://arxiv.org/abs/2511.17012)
### Authors
Junjie Hao,Chun Wang,Ying Qiao,Qiuyue Zuo,Qiya Song,Hua Ma,Xieping Gao
### Background
大型语言模型和知识图谱有潜力推动历史文化的科研，通过支持历史文化信息的提取、分析和解释。然而，关于湖南历史名人的系统数据资源有限，通用模型在低资源环境下的领域知识提取和结构化输出生成表现不佳。
### Innovation
提出了监督微调方法来增强领域特定的信息提取。设计了一个细粒度、基于模式的指令模板，并构建了一个指令微调数据集，以解决领域特定训练语料库缺乏的问题。此外，应用参数高效指令微调方法在四个公开可用的大规模语言模型上进行试验，并开发了评估其提取性能的标准。
### Conclusion
所有模型在微调后都表现出显著的性能提升。Qwen3-8B在100个样本和50次训练迭代中取得了最佳效果，得分为89.3866。这项研究为区域历史文化领域的垂直大型语言模型微调提供了新的见解，并突显了它们在文化遗产知识提取和知识图构建中的潜在低成本应用价值。
## 211. `cs.CL` - 原理化设计适用于大规模教育评估的可解释自动评分系统 [PDF](https://arxiv.org/pdf/2511.17069), [HTML](https://arxiv.org/abs/2511.17069)
### Authors
Yunsung Kim,Mike Hardy,Joseph Tey,Candace Thille,Chris Piech
### Background
AI驱动的自动化评分系统可以大规模高效地评估学生的复杂生成答案，但在透明性和可解释性方面的需求不断增加的情况下，领域尚未开发出广泛认可的可解释自动化评分解决方案以应用于大规模实际评估。
### Innovation
本研究提出了 Faithfulness（忠实性）、Groundedness（基础性）、Traceability（可追踪性）、Interchangeability（可替代性）四大可解释性原则，开发了AnalyticScore框架用于简答题评分，该框架通过提取答案中的显式可识元素，使用LLMs将每个回答转换为人可以理解的值，并应用直观的有序逻辑回归模型进行评分，从而提高评分准确性和可解释性。
### Conclusion
AnalyticScore在评分准确性方面优于许多不可解释的评分方法，其平均QWK得分与SOTA方法相差仅0.06，且其特征化行为与人类标注者的特征化行为高度一致。
## 212. `cs.CL` - Bench360: 360°评估本地大型语言模型推理 [PDF](https://arxiv.org/pdf/2511.16682), [HTML](https://arxiv.org/abs/2511.16682)
### Authors
Linus Stuhlmann,Mauricio Fadel Argerich,Jonathan Fürst
### Background
本地运行大型语言模型（LLM）变得越来越普遍。尽管小型开源模型和推理引擎的可用性增加降低了入门门槛，但用户现在面临着大量的配置选择。要找到一个平衡功能和非功能需求的最优配置需要大量的手工努力。虽然有一些基准用于LLM推理，但它们是为了狭窄的评估目标设计的，并不以用户为中心，未能将相关系统和任务特定的度量指标集成到易于使用的、统一的基准中，该基准支持多种推理引擎、使用场景和量化级别。为了弥补这一差距，我们提出了Bench360——360度评估本地LLM推理。Bench360允许用户轻松定义自定义任务、数据集以及相关任务度量指标，然后自动对所选的LLM、推理引擎和量化级别在不同的使用场景（单流、批处理和服务器）进行基准测试。Bench360追踪广泛的一系列度量指标，包括系统度量（如计算性能、资源使用、部署等）和任务特定度量（如ROUGE、F1得分或准确性）。我们对四种常见的LLM任务（通用知识与推理、问答、总结和文本到SQL）在三种硬件平台上和四个最先进的推理引擎上进行了演示测试。
### Innovation
Bench360提供了一种全新的评估方法，能够轻松定义自定义任务，同时支持多种推理引擎、使用场景和量化级别，并自动跟踪广泛的系统度量和任务特定度量。相比之下，现有的基准没有集成足够的系统和任务特定的度量，也没有考虑到用户的使用场景。Bench360的创新之处在于其全面性和用户友好性，为评估和选择本地LLM提供了有力的支持。
### Conclusion
我们的结果揭示了任务性能和系统效率之间的若干有趣的权衡关系，突显了不同推理引擎和模型之间的差异。最重要的是，没有单一的最佳设置适用于本地推理，这强烈地凸显了Bench360这样一种框架的需求。
## 213. `cs.CL` - NALA_MAINZ在BLP-2025任务2中的多智能体方法：孟加拉语指令到Python代码生成 [PDF](https://arxiv.org/pdf/2511.16787), [HTML](https://arxiv.org/abs/2511.16787)
### Authors
Hossain Shaikh Saadi,Faria Alam,Mario Sanz-Guerrero,Minh Duc Bui,Manuel Mager,Katharina von der Wense
### Background
本文介绍了JGU Mainz团队为BLP-2025共享任务中从孟加拉语指令生成代码的竞赛所使用的获胜系统。该团队解决的问题背景是代码生成的需求，在自动化和构建复杂系统的过程中，自动从自然语言指令生成相应的代码可以提高开发效率。
### Innovation
本文提出了一种基于多智能体的生成管道。首先，一个代码生成智能体根据输入指令生成初始解决方案。然后经过提供的单元测试（pyest风格，基于断言的）执行。只有失败的案例才会被转发给一个调试智能体，该智能体重新运行测试、提取错误踪迹，并基于错误消息、当前程序和相关的测试案例生成修订后的解决方案。这种机制让该团队的提交在共享任务中排名第一，取得了95.4%的$Pass@1$得分。
### Conclusion
基于此方法，本文不仅提交在共享任务中获得了第一名，还公开了其源代码。这意味着该方法能够在实际场景中应用，并提供了进一步改进的基础。
## 214. `cs.CL` - 从表征到实现：译者思维的ABC框架 [PDF](https://arxiv.org/pdf/2511.16811), [HTML](https://arxiv.org/abs/2511.16811)
### Authors
Michael Carl,Takanori Mizowaki,Aishvarya Raj,Masaru Yamada,Devi Sri Bandaru,Yuxiang Wei,Xinyue Ren
### Background
本文基于扩展的心智（EM）理论和激进的生态化理论，提出了一种替代基于表征的思维模型的观点。文中通过预测加工理论和（生态）推理理论，论述了译者的思维并非通过心身环境的静态对应关系扩展，而是通过心身环境互动环路形成的一种更为动态且非表征的过程。
### Innovation
本文提出了一种新的ABC框架来重新定义译者的思维。这一框架强调，翻译不仅仅是对静态对应关系的操纵，而是一种动态整合情感、行为和认知（ABC）过程的生态实践。译者的思维通过心身环境互动的环节实现，而非仅仅延伸。这种非表征的理论重新定义了翻译，将其视为在社会文化实践中以技能参与的方式，实时地通过与文本、工具及环境的物质互动来共同创造意义。
### Conclusion
本文提出了一个用于理解和解释译者心理活动的新框架（ABC框架），强调翻译是一种动态的、非表征的过程，强调译者思维与心身环境的互动关系，重新定义了翻译的本质，将其视为社会文化实践中的技能参与。
## 215. `cs.CL` - 采用全栈AMD平台训练基础模型：计算、网络和系统设计 [PDF](https://arxiv.org/pdf/2511.17127), [HTML](https://arxiv.org/abs/2511.17127)
### Authors
Quentin Anthony,Yury Tokpanov,Skyler Szot,Srivatsan Rajagopal,Praneeth Medepalli,Rishi Iyer,Vasu Shyam,Anna Golubeva,Ansh Chaurasia,Xiao Yang,Tomas Figliolia,Robert Washbourne,Drew Thorstensen,Amartey Pearson,Zack Grossbart,Jason van Patten,Emad Barsoum,Zhenyu Gu,Yao Fu,Beren Millidge
### Background
研究团队首次在纯AMD硬件上进行大规模Experts-in-Training（混合模型专家训练，MoE）预训练研究，采用了MI300X GPU并利用了Pollara互连。研究重点介绍了系统和模型设计的实用建议。
### Innovation
团队为系统设计提供了全面的集群和网络表征，包括对核心集体操作（如所有减少、减少散列、所有集合并、广播）的所有微基准测试，以及关于内存带宽和内核大小的MI300X微基准测试，用于指导模型设计。模型设计方面，引入并应用了MI300X意识下的转换器大小规则，并解决了联合优化训练吞吐量和推理延迟的MoE宽度问题。研究还详细介绍了自己的训练堆栈，包括故障恢复和检查点重塑等易被人忽视的功能。
### Conclusion
ZAYA1作为基模，与同规模和更大规模的领先基模（如Qwen3-4B和Gemma3-12B）性能相当，并在各种推理、数学和编码基准测试中优于Llama-3-8B和OLMoE。这表明AMD硬件、网络和软件堆栈已经足够成熟并优化，可以与大型预训练竞争。
## 216. `cs.CL` - LangMark: 多语言自动后编辑数据集 [PDF](https://arxiv.org/pdf/2511.17153), [HTML](https://arxiv.org/abs/2511.17153)
### Authors
Diego Velazquez,Mikaela Grace,Konstantinos Karageorgos,Lawrence Carin,Aaron Schliem,Dimitrios Zaikis,Roger Wechsler
### Background
自动后编辑（APE）旨在纠正机器翻译文本中的错误，提高翻译质量，同时减少人类干预的需要。尽管神经机器翻译（NMT）取得了进展，但有效APE系统的开发受到了特定针对NMT输出的大规模多语言数据集缺乏的阻碍。
### Innovation
我们提出了并发布了LangMark，这是一个包含英语到七种语言（巴西葡萄牙语、法语、德语、意大利语、日语、俄语、西班牙语）的新的人类标注多语言APE数据集，包含206,983个三元组，每个三元组包括源片段、其NMT输出和人工后编辑的翻译。通过利用此数据集，我们实证展示了少量提示的大型语言模型（LLMs）能够有效执行APE，超越了领先的商用甚至专用机器翻译系统。
### Conclusion
我们认为，这一新资源将有助于未来APE系统的开发和评估。
## 217. `cs.CL` - 通过更多思考减少幻觉：大型语言模型的基于方面因果避谈 [PDF](https://arxiv.org/pdf/2511.17170), [HTML](https://arxiv.org/abs/2511.17170)
### Authors
Vy Nguyen,Ziqi Xu,Jeffrey Chan,Estrid He,Feng Xia,Xiuzhen Zhang
### Background
大型语言模型（LLMs）常常生成流畅但事实错误的回答，这种现象称为幻觉。为了避免这种不确定性，模型可以选择回答，但是现有的方法通常依赖于生成后的提示或反馈信号，这限制了他们在生成早期就进行预防的能力。因此，提出了一种新的框架，即基于方面因果分析的早起避谈（Aspect-Based Causal Abstention, ABCA），通过因果推理分析LLM知识的内部多样性来实现早期避谈。
### Innovation
ABCA框架通过分析LLM知识的内部多样性来进行早期避谈。与依赖生成后信号的方法不同，ABCA评估知识在不同方面的影响来确定信息的可靠性，从而实现两种类型的避谈：第一种类型是方面效应不一致（知识冲突），第二种类型是方面效应一致支持避谈（知识不足）。该框架通过利用这些估计值来确定避谈类型，实验结果证明ABCA提高了避谈的可靠性，实现了最先进的性能，并增强了避谈决策的可解释性。
### Conclusion
ABCA通过因果推理中的方面效应评估，提前避免无保障的LLM回答，提高回应的可靠性并增强响应解释性，在标准基准测试中实现了最好的避谈性能。
## 218. `cs.CL` - ARQUSUMM: 论证感知的定量化在线讨论总结 [PDF](https://arxiv.org/pdf/2511.16985), [HTML](https://arxiv.org/abs/2511.16985)
### Authors
An Quang Tang,Xiuzhen Zhang,Minh Ngoc Dinh,Zhuang Li
### Background
随着在线讨论平台（如Reddit）上争议性话题的增多，不仅需要总结不同意见，还需要概括其背后的论据和理由。早期对文本总结的研究主要关注源文档中的核心信息，没有充分考虑到在线讨论的论证性质。近年来，关于对话总结的研究虽然考虑了句子间的论证关系，但仍然无法解释句子内部的深层次论证结构。
### Innovation
本文提出了一个新颖的任务——论证感知的定量总结，旨在揭示对话中论据-理由结构，并通过量化的标准来衡量论证强度。为此，作者提出了ARQUSUMM框架，该框架利用基于论证理论的少量样本学习方法来识别句子中的论点及其论据-理由关系，并通过具有论证结构意识的聚类算法来聚合论证并量度其支持度。
### Conclusion
实验表明，ARQUSUMM在对话总结和定量总结方面均优于现有模型，能够生成既有助于用户理解又具有高质量文本和高量化精度的总结。
## 219. `cs.CL` - 深监督深度改进 [PDF](https://arxiv.org/pdf/2511.16886), [HTML](https://arxiv.org/abs/2511.16886)
### Authors
Arip Asadulaev,Rayan Banerjee,Fakhri Karray,Martin Takac
### Background
最近的研究表明，小型循环架构，如 Tiny Recursive Models (TRMs)，在复杂推理任务上可以超越大型语言模型（LLMs），包括 Abstraction and Reasoning Corpus (ARC)。这项研究进一步探索了如何使用最少的修改来进一步提高这些方法的效率。
### Innovation
本文提出了一种新的训练方案，将 TRMs 的潜在推理框架为无分类器指导和隐式策略改进算法。这种方法为每个训练循环提供一个目标，显著提高了训练效率。与标准 TRMs 相比，该方法减少了总前向传递次数 18 倍，并消除了终止机制，同时保持了相似的质量。该模型在仅使用 0.8M 参数的情况下在 ARC-1 上达到了 24% 的准确性，优于大多数大型语言模型。
### Conclusion
本文的方法通过减少训练中的前向传递次数和移除终止机制，显著提高了 TRMs 的训练效率和性能，同时保持了与标准 TRMs 相似的准确性。
## 220. `cs.CL` - Vision-Language模型是否理解视觉说服力? [PDF](https://arxiv.org/pdf/2511.17036), [HTML](https://arxiv.org/abs/2511.17036)
### Authors
Gyuwon Park
### Background
近期的视觉-语言模型（VLMs）在多模态推理和理解方面取得了显著进展。然而，这些模型是否真正理解视觉说服力，即视觉线索如何影响人类的态度和决策，仍然不清楚。
### Innovation
本文构建了一个高共识的二元说服力判断数据集，并引入了视觉说服因素（VPFs）的分类系统，包括低级感知、中级组成和高级语义提示。同时，探讨了说服相关推理的认知引导和知识注入策略。通过对多种VLMs的实证分析，发现这些模型倾向于高说服力的召回偏差，并且对低/中级特征的辨别能力较弱。然而，信息与对象之间高级语义一致性的高度预测了人类的判断。此外，简单的指令或无引导的推理支持效果较差，而简洁且基于对象的理由可以显著提高精确度和F1分数。
### Conclusion
这些结果表明，VLMs的核心限制不在于识别说服对象，而在于将其与沟通意图联系起来。
## 221. `cs.CL` - 注意力引导特征融合（AGFF）模型在新闻文本分类中整合统计和语义特征 [PDF](https://arxiv.org/pdf/2511.17184), [HTML](https://arxiv.org/abs/2511.17184)
### Authors
Mohammad Zare
### Background
自然语言处理中的新闻文本分类是一项关键任务，用于管理和筛选大量数字内容。传统方法通常依赖于统计特征，如词频或TF-IDF值，这些特征能有效捕捉词语的重要性，但往往无法反映上下文意义。相比之下，现代深度学习方法利用语义特征来理解词语在上下文中的使用，但可能忽略简单的高影响统计指标。为了更准确地分类新闻文本，作者提出了一种名为注意力引导特征融合（AGFF）模型，该模型在统一框架下结合统计和语义特征，并通过注意力机制动态确定每种特征类型的重要性，从而做出更明智的分类决策。
### Innovation
该模型通过引入注意力机制实现了统计和语义特征的有效融合，并在基准新闻数据集上的评估结果显示其性能优于传统的统计模型和纯粹的语义深度学习模型。通过消融研究进一步验证了每个组件在融合过程中的贡献，强调了模型在平衡和利用统计和语义表示的互补优势方面的能力。
### Conclusion
该研究证实，策略性地整合不同的特征类型可以显著提高分类精度。AGFF模型因其能够平衡和利用统计和语义特征的优点，成为解决实际新闻分类任务的一个实用而有效的解决方案。
## 222. `cs.CL` - 迷失在翻译和噪音之中：VLMs在现实表格中失败模式的深度探讨 [PDF](https://arxiv.org/pdf/2511.17238), [HTML](https://arxiv.org/abs/2511.17238)
### Authors
Anshul Singh,Rohan Chaudhary,Gagneet Singh,Abhay Kumary
### Background
现有的视觉语言模型（VLMs）的评估大多依赖于无法充分捕捉现实世界复杂性的基准。现有的表格问答数据集，如WikiTableQuestions和FinQA，主要为单一语言（英语）表格，且表格呈现形式清晰完美，这与实际应用中的情况存在显著差距。
### Innovation
为了解决上述问题，该研究提出了一个新的基准——MirageTVQA。MirageTVQA包含近60,000个跨24种语言的问答对，提出了不仅多语言，还具有视觉不完美、包含真实噪声的表格，以逼近扫描文档的效果。这一基准揭示了两大主要问题：视觉噪音导致性能严重下降（最佳模型下降超过35%），以及持续的英语优先偏见，使得推理能力无法转移到其他语言。
### Conclusion
MirageTVQA提供了一个衡量和推动VLMs模型在表格推理方面更稳健发展的基准。数据集和代码可以在在线资源中获取，促进在该领域的研究进展。
## 223. `cs.CL` - 学习压缩：解锁大规模语言模型用于文本表示的潜力 [PDF](https://arxiv.org/pdf/2511.17129), [HTML](https://arxiv.org/abs/2511.17129)
### Authors
Yeqin Zhang,Yizheng Zhao,Chen Hu,Binxing Jiao,Daxin Jiang,Ruihang Miao,Cam-Tu Nguyen
### Background
文本表示在聚类、检索等下游任务中起着关键作用。随着大语言模型（LLMs）的出现，人们越来越感兴趣于利用它们的能力来生成文本表示。然而，大多数的LLMs本质上是因果的，并且优化用于下一个词预测，使得它们不适合作为整体表示的生成工具。为了解决这个问题，最近的研究引入了前置任务来适应LLMs以生成文本表示。然而，大多数前置任务依赖于词元级预测目标，如LLM2Vec中使用的掩码下一个词预测（MNTP）。在这项工作中，我们探索了上下文压缩作为一种前置任务来利用LLMs进行无监督适应的潜力。在压缩预训练过程中，模型学习生成紧凑的记忆词元，这些词元用于下游序列预测。
### Innovation
我们的研究探索了上下文压缩作为前置任务来适应LLMs的一种新方法，该方法能生成紧凑的记忆词元，以替换整体上下文来用于下游序列预测。实验结果表明，精心设计的压缩目标可以显著提升基于LLM的文本表示能力，超越了使用词元级前置任务训练的模型。进一步通过对比学习，产生了一个强大的表示模型（LLM2Comp），该模型在多种下游任务上表现出色，且样本效率更高，需要较少的训练数据。
### Conclusion
通过精心设计的压缩目标，可以显著提升基于LLM的文本表示能力，超越了使用词元级前置任务训练的模型。对比学习进一步提升生成了强表示模型（LLM2Comp），该模型在多种下游任务上表现出色，且样本效率更高，需要较少的训练数据。
## 224. `cs.CL` - 通过软概念混合提高大型语言模型的潜在推理能力 [PDF](https://arxiv.org/pdf/2511.16885), [HTML](https://arxiv.org/abs/2511.16885)
### Authors
Kang Wang,Xiangyu Duan,Tianyi Du
### Background
与人类在抽象概念空间中的推理不同，大型语言模型（LLMs）通常通过生成离散的标记来进行推理，这可能限制了它们的表达能力。近期的工作Soft Thinking表明，LLMs使用软概念进行潜在推理是一种有前景的方向，但它们仍被训练于离散标记之上。为了减少推理中的软概念与训练中的离散标记之间的差距，我们提出了一种称为Soft Concept Mixing (SCM)的软概念感知训练方案，该方案在训练过程中直接让模型接触到软表示。
### Innovation
SCM构造了一个软概念向量，通过嵌入的概率加权平均形成，然后将这个向量混合到模型的隐状态中，这些隐状态蕴含了丰富的情境信息。最后，整个潜在推理过程通过强化学习（RL）进行优化。实验结果表明，与LLMs相比，SCM提高了推理性能，并且保持了稳定的训练动态。
### Conclusion
研究结果证明，SCM能够提高LLMs的推理性能，并且在训练过程中表现稳定。这种方法为理解LLMs如何进行潜在推理并提高其能力提供了一种新的思路。
## 225. `cs.CL` - E$^3$-Pruner: 向大规模语言模型高效、经济且有效的层剪枝方向迈进 [PDF](https://arxiv.org/pdf/2511.17205), [HTML](https://arxiv.org/abs/2511.17205)
### Authors
Tao Yuan,Haoli Bai,Yinfei Pan,Xuyang Cao,Tianyu Zhang,Lu Hou,Ting Hu,Xianzhi Yu
### Background
随着大型语言模型规模的不断扩大，层剪枝已成为一种硬件友好的模型压缩方法，获得了越来越多的关注。然而，现有的层剪枝方法在解决性能下降、高训练成本和有限加速等关键实用部署挑战方面存在局限性。
### Innovation
E$^3$-Pruner框架提出了两个关键创新点：(1) 使用Gumbel-TopK抽样器的可微掩码优化方法，实现高效的精确剪枝掩码搜索；(2) 一种基于熵感知的自适应知识蒸馏策略，以增强任务性能。
### Conclusion
实验结果表明，E$^3$-Pruner方法在多个模型架构和基准测试上优于现有最先进的方法。在对Qwen3-32B模型剪枝25%层时，E$^3$-Pruner方法在MATH-500上的准确性达到96%，仅比原模型（96.8%）下降0.8%，并且仅消耗0.5B个令牌（0.5%的后训练数据体积），实现了1.33倍的推理加速。
## 226. `cs.CL` - PLLuM 指令语料库 [PDF](https://arxiv.org/pdf/2511.17161), [HTML](https://arxiv.org/abs/2511.17161)
### Authors
Piotr Pęzik,Filip Żarnecki,Konrad Kaczyński,Anna Cichosz,Zuzanna Deckert,Monika Garnys,Izabela Grabarczyk,Wojciech Janowski,Sylwia Karasińska,Aleksandra Kujawiak,Piotr Misztela,Maria Szymańska,Karolina Walkusz,Igor Siek,Maciej Chrabąszcz,Anna Kołos,Agnieszka Karlińska,Karolina Seweryn,Aleksandra Krasnodębska,Paula Betscher,Zofia Cieślińska,Katarzyna Kowol,Artur Wilczek,Maciej Trzciński,Katarzyna Dziewulska,Roman Roszko,Tomasz Bernaś,Jurgita Vaičenonienė,Danuta Roszko,Paweł Levchuk,Paweł Kowalski,Irena Prawdzic-Jankowska,Marek Kozłowski,Sławomir Dadas,Rafał Poświata,Alina Wróblewska,Katarzyna Krasnowska-Kieraś,Maciej Ogrodniczuk,Michał Rudolf,Piotr Rybak,Karolina Saputa,Joanna Wołoszyn,Marcin Oleksy,Bartłomiej Koptyra,Teddy Ferdinan,Stanisław Woźniak,Maciej Piasecki,Paweł Walkowiak,Konrad Wojtasik,Arkadiusz Janz,Przemysław Kazienko,Julia Moska,Jan Kocoń
### Background
本文描述了一个在PLLuM（波兰大型语言模型项目）项目中使用的指令数据集，用于微调一组基于变换器的大型语言模型（LLMs）。此外，还讨论了使用由人类撰写和合成的指令数据集对基础LLMs进行语言适应的含义，并发布了PLLuMIC（PLLuM指令语料库）的一个代表性子集。
### Innovation
提出了有机、转化和合成指令的功能分类，并探讨了使用人类撰写和合成的指令数据集对基础LLMs进行语言适应的意义。发布了第一个代表性的PLLuM指令语料库子集，以指导和规划其他LLMs相似数据集的发展。
### Conclusion
研究表明，PLLuMIC的子集对于指导和规划其他LLMs类似数据集的发展具有重要意义，同时展示了使用不同类型的指令数据集对语言适应的影响。
## 227. `cs.CL` - MUCH: 多语言主张虚幻基准 [PDF](https://arxiv.org/pdf/2511.17081), [HTML](https://arxiv.org/abs/2511.17081)
### Authors
Jérémie Dentan,Alexi Canesse,Davide Buscaldi,Aymen Shabou,Sonia Vanier
### Background
Large Language Models (LLMs) 在可靠性方面存在不足，而基于主张级别的不确定性量化 (UQ) 是解决这一问题的潜在方法。然而，现有针对 UQ 的评估基准可能无法提供公平、可复制的评估环境。为了克服这些不足，研究者们需要开发新的基准来评估未来的 UQ 方法在现实条件下的性能。
### Innovation
我们提出了 MUCH，这是首个专为未来 UQ 方法的公平且可复制评估设计的多语言主张级别基准。MUCH 包含了 4,873 个样本，覆盖 4 种欧洲语言（英语、法语、西班牙语和德语），以及 4 种指令调优的开源 LLM。通过提供每令牌 24 个生成的 logits，MUCH 促进了未来白盒方法的发展，而无需重新生成数据。此外，MUCH 使用了一种新颖的确定性算法，可以在仅需 LLM 生成时间的 0.2% 的情况下进行主张分割，这使其适用于实时监测 LLM 输出，确保了评估在实际部署条件下的有效性。
### Conclusion
当前的 UQ 方法在性能和效率方面仍然有很大的改进空间。MUCH 提供了一个公平、可复制的环境来评估 UQ 方法，这对于未来的改进具有重要意义。
## 228. `cs.CL` - Social-Media 基于社交媒体人像挑战：Bluesky 上常见和罕见用户行为的混合预测 [PDF](https://arxiv.org/pdf/2511.17241), [HTML](https://arxiv.org/abs/2511.17241)
### Authors
Benjamin White,Anastasia Shimorina
### Background
理解和预测用户在社交媒体平台上的行为对于内容推荐和平台设计至关重要。现有方法主要关注如转发和点赞等常见行为，而对罕见但重要的行为预测还鲜有探索。
### Innovation
本文提出了一种综合方法，用于同时预测社交媒体用户的常见和罕见行为。该方法综合利用了历史响应模式的查找数据库系统、针对特定人格的LightGBM模式以及融合文本和时间表示的特殊混合神经架构，专用模型在12种常见行为预测中的平均宏F1得分为0.64，对10种罕见行为分类的宏F1得分为0.56。
### Conclusion
有效的社交媒体行为预测需要针对不同类型行为的个性化建模策略。本文的方法在Bluesky的大规模数据集上取得最优结果，并在COLM 2025年“基于社交媒体的人格挑战”中的SocialSim研讨会中获得第一名。
## 229. `cs.CL` - LLM代理的简单而强大的长期对话记忆基线 [PDF](https://arxiv.org/pdf/2511.17208), [HTML](https://arxiv.org/abs/2511.17208)
### Authors
Sizhe Zhou
### Background
现有的基于LLM的对话代理在长时间会话中难以维持连贯且个性化的交互。这主要由于固定的上下文窗口限制了历史信息的保存，以及大多数外部记忆方法在粗略检索大块内容和细粒度且碎片化的对话视图之间进行权衡。
### Innovation
本文提出的创新之处在于，基于neo-Davidsonian事件语义，提出了一种以事件为中心的方法。这种方法将对话历史表示为短事件命题，这些命题结合了参与者、时间线索和局部上下文，而不是独立的关系三元组或模糊总结。此外，提出了将会话分解为增强的基本话语单元（EDUs），并对这些EDUs和相关证据采用基于图的传播步骤进行检索和聚合。这种方法能够为长期对话代理提供一种结构简单、事件级别的记忆基础。
### Conclusion
实验表明，这种以事件为中心的记忆在LoCoMo和LongMemEval$_S$基准测试中表现出色，能有效地使用较短的问题/答案上下文。结果表明，结构简单的、事件级别的记忆为长期视角下的对话代理提供了一个合理且实用的基础。
## 230. `cs.CL` - AutoLink：大规模文本到SQL系统中自主模式下的自主模式探索与扩展以实现可扩展的模式链接 [PDF](https://arxiv.org/pdf/2511.17190), [HTML](https://arxiv.org/abs/2511.17190)
### Authors
Ziyang Wang,Yuanlei Zheng,Zhenbiao Cao,Xiaojin Zhang,Zhongyu Wei,Pei Fu,Zhenbo Luo,Wei Chen,Xiang Bai
### Background
在大规模工业文本到SQL场景中，向大型语言模型（LLM）提供完整的数据库模式数据不可行，因为存在上下文窗口限制和大量的无关噪声。现有的模式链接方法在涉及大量数据库时效率低下，难以权衡召回率和噪音之间的关系，并且扩展能力有限。因此，提出一种称为AutoLink的自主代理框架，它将模式链接重新构想为自主驱动的迭代过程，通过LLM的引导，AutoLink能够动态探索和扩展相关部分的模式，逐步识别所需的模式组件，而不输入完整的数据库模式。
### Innovation
AutoLink通过自主探索和扩展相关模式部分，能高效地识别必要的模式组件，从而显著提高召回率和执行准确性。与现有方法相比，AutoLink在性能上表现出优越性，其在Bird-Dev上的严格模式链接召回率达到97.4%，Spider-2.0-Lite上为91.2%，同时保持了可竞争的执行准确率。尤其值得注意的是，AutoLink在大数据库模式（如超过3000列）上展现出卓越的可扩展性，能够保持高水平的召回率、高效地消耗令牌并保持较高的执行准确性。
### Conclusion
AutoLink作为一种高度可扩展、高召回率的模式链接解决方案，在大规模文本到SQL系统中具有重要的应用价值。它通过自主驱动的方式，能够在保持高召回率的同时，高效处理大型数据库模式，为大规模工业环境提供了一种有效的方法。
## 231. `cs.CL` - 大语言模型在情感分析中检测社会挑战：南非语言的应用案例 [PDF](https://arxiv.org/pdf/2511.17301), [HTML](https://arxiv.org/abs/2511.17301)
### Authors
Koena Ronny Mabokela,Tim Schlippe,Matthias Wölfel
### Background
情感分析有助于理解人们在社会问题上的观点和情绪。对于多语言社区来说，情感分析系统可以迅速识别社交媒体帖子中的社会挑战，使政府部门能够更精准有效地发现和处理这些问题。近年来，大型语言模型（LLMs）已公开提供，并且初步分析表明它们在英语中的零样本情感分析能力非常出色。然而，现有的研究尚未探讨利用LLMs进行南非语言社交媒体帖子的情感分析，以检测社会挑战。
### Innovation
本研究分析了最先进的LLMs（GPT-3.5、GPT-4、LlaMa 2、PaLM 2 和 Dolly 2）在零样本性能上的表现，以探究英语、塞佩迪语和塞茨瓦纳语中10个新兴话题的情感极性，这些话题属于南非10个政府部门的管辖范围。结果显示，不同LLMs、话题和语言之间存在显著差异。此外，研究发现不同LLMs结果的融合在情感分类性能上带来了显著提升，情感分类错误率低于1%。因此，现在有可能通过提供生成可靠情感分析信息的系统，来检测社会挑战并针对特定话题和不同语言群体可能的需求进行行动。
### Conclusion
本研究揭示了不同LLMs在情感分析上的差异，并证明了它们能够有效检测社会挑战，提供可靠的分析信息，未来可以通过融合不同LLMs的结果来提高情感分析的准确性。这对于政府制定相关的社会政策措施具有实际意义。
## 232. `cs.CL` - 一块新秀：分布语义预测元音音节词语在台湾自由对话中特有的声调特征 [PDF](https://arxiv.org/pdf/2511.17337), [HTML](https://arxiv.org/abs/2511.17337)
### Authors
Xiaoyun Jin,Mirjam Ernestus,R. Harald Baayen
### Background
该研究通过对普通话自然对话中单音节词音高轮廓的语料库分析，探索词义对音高实现出现在不同控制变量（诸如词长、性别、说话人身份、声调背景、元音高度和话语位置等）后的残留影响。研究采用广义加性模型分解给定的观测音高轮廓，以不同的控制变量和语义预测器为依据，尝试解释音高轮廓的变化。
### Innovation
研究创新在于使用广义加性模型对音高进行分解，并将词义作为语义预测器，发现即使在考虑多个控制变量的情况下，词语依然对音高实现有显著的预测作用。此外，研究表明词义对音高特征的影响比单纯的词语本身更重要，不同的异形同音词（即拼写相同而意思不同的词语）会表现出不同的音高轮廓，且这些音高轮廓可以通过上下文嵌入预测，其准确率远超随机置换基线。
### Conclusion
研究结论认为，分布语义在预测普通话中词语的特有声调特征方面具有重要作用。尽管研究结果挑战了标准的普通话声调理论，但它们与辨别性词汇模型的理论框架是一致的。
## 233. `cs.CL` - 选择性旋转位置嵌入 [PDF](https://arxiv.org/pdf/2511.17388), [HTML](https://arxiv.org/abs/2511.17388)
### Authors
Sajad Movahedi,Timur Carstensen,Arshia Afzal,Frank Hutter,Antonio Orvieto,Volkan Cevher
### Background
位置信息对于语言建模至关重要。在 softmax 变体的变压器中，旋转位置嵌入（RoPE）通过固定角度的旋转编码位置，而在线性变压器中，位置靠依赖输入的选择性门控机制处理。选择性机制曾经被证明有助于语言相关任务。现受此启发，作者引入了选择性 RoPE 机制，这是一种依赖输入的旋转嵌入方法，能够同时为线性和 softmax 变压器中的关注机制使用任意角度的旋转。
### Innovation
作者提出了选择性 RoPE 机制，这种机制依赖输入让旋转能够以任意角度应用于线性和 softmax 变压器中。作者还发现，即使在未显式加入 RoPE 的模型中，softmax 注意力机制也对查询键对隐含执行了隐藏形式的旋转，进一步研究发现实部负责遗忘，虚部通过旋转编码位置。
### Conclusion
通过在门控变压器中装备选择性 RoPE，作者证明了这种输入依赖的旋转机制能提升语言建模及复杂序列任务（如复制、状态跟踪和检索）的性能。
## 234. `cs.CL` - Humanlike Multi-user Agent (HUMA): Designing a Deceptively Human AI Facilitator for Group Chats [PDF](https://arxiv.org/pdf/2511.17315), [HTML](https://arxiv.org/abs/2511.17315)
### Authors
Mateusz Jacniacki,Martí Carmona Serrat
### Background
目前基于大型语言模型（LLMs）的对话代理（conversational agents）正在变得越来越普遍，但大多数系统都是为一对一、轮流交换设计的，而不是自然、异步的多人群聊。随着人工智能助手在数字平台上的广泛普及，从虚拟助手到客户服务，开发出自然且类人类的互动模式对于维护用户信任和参与度显得尤为重要。
### Innovation
本文提出了一种名为HUMA的人类类多用户代理（Humanlike Multi-user Agent），它是一种基于LLM的多人群聊促进者，使用类似于人类的策略和时间进行多人群聊。HUMA采用事件驱动的架构处理消息、回复和反应，并引入了真实响应时间的模拟。HUMA由路由器、行动代理和反思三个组件组成，共同使LLM适应组对话动态。
### Conclusion
研究结果表明，在自然群聊环境中，AI促进者可以达到人类质量的水平，且难以被识别为非人类。社区经理效果、社会存在感和社会参与度/满意度在不同条件下仅存在轻微差异，且效应大小较小。这表明，HUMA在多人群聊环境中提供了令人满意的人类交互体验。
## 235. `cs.CL` - Parrot：输出真实性的劝说和一致性稳健度评估——LLM的阿谀奉承稳健性基准 [PDF](https://arxiv.org/pdf/2511.17220), [HTML](https://arxiv.org/abs/2511.17220)
### Authors
Yusuf Çelebi,Mahmoud El Hussieni,Özay Ezerceli
### Background
本文探讨了社会压力（特别是权威和说服力）对大型语言模型（LLMs）中的准确性的影响，尤其是它们在面对阿谀奉承（过度顺从）现象时的表现。研究通过对比无权威和含权威误导性版本的相同问题，以及通过日志似然校准跟踪量化信心变化，来评估模型的稳健性。研究结果揭示了不同模型在面对社会压力时表现出的巨大异质性。
### Innovation
文章提出了一种名为PARROT的评估框架，用于测量LLMs在社会压力下的准确度下降，特别是在权威和说服力作用下的人为效果。PARROT框架创新之处在于它通过双盲评估隔离因果影响，使用日志似然校准跟踪量化信心的变化，并通过八状态行为分类系统系统地分类失败模式。
### Conclusion
研究表明，不同模型在面对社会压力时的表现差异显著：高级模型（如GPT-5、GPT-4.1、Claude Sonnet 4.5）表现出较低的“顺从率”（≤11%，GPT-5仅为4%）且准确性损失小；而较老或规模较小的模型（如GPT-4、Qwen 2.5-1.5B）则显示出严重的思想崩溃（GPT-4为80%，Qwen 2.5-1.5B为94%）。此外，研究还强调了国际法和全球知识领域的脆弱性以及基础数学领域的相对韧性。因此，文章提出，在实际部署中，LLMs的安全使用应将“抵抗过拟合压力的能力”作为主要目标，与其他准确性、避免伤害和保护隐私的要求并重。
## 236. `cs.CL` - PUCP-Metrix：用于西班牙语的全面开源语言度量库 [PDF](https://arxiv.org/pdf/2511.17402), [HTML](https://arxiv.org/abs/2511.17402)
### Authors
Javier Alonso Villegas Luis,Marco Antonio Sobrevilla Cabezudo
### Background
现有的西班牙语工具在提供语言特性方面存在局限性，特别是在理解和处理风格、结构和可读性任务时。研究人员和从业者需要更全面的工具来支持语言分析。
### Innovation
PUCP-Metrix是一个开源的西班牙语语言度量库，包含了182个语言度量指标，覆盖了词汇多样性、句法和语义复杂性、连贯性、心理学语言学以及可读性等方面。这个工具提供了精细和可解释性的文本分析能力。作者通过自动可读性评估和机器生成文本检测任务展示了PUCP-Metrix的性能与现有工具和神经基线相比具有竞争力。
### Conclusion
PUCP-Metrix为西班牙语的自然语言处理应用提供了全面且可扩展的资源，支持多样的NLP应用。
## 237. `cs.CL` - RubiSCoT：一种支持AI的学术评估框架 [PDF](https://arxiv.org/pdf/2510.17309), [HTML](https://arxiv.org/abs/2510.17309)
### Authors
Thorsten Fröhlich,Tim Schlippe
### Background
学术论文的评估是高等教育的基石，确保学术 rigor 和 integrity。传统的评估方法虽然有效，但耗时且易受评估者主观差异的影响。
### Innovation
RubiSCoT 是一个基于 AI 的框架，旨在从提案到最终提交阶段优化论文评估。通过使用高级自然语言处理技术，包括大规模语言模型、检索增强生成和有序思考提示，RubiSCoT 提供了一种一致的、可扩展的解决方案。该框架包括初步评估、多维度评估、内容提取、评分表评分和详细报告。
### Conclusion
该文章介绍了 RubiSCoT 的设计和实现，并讨论了其在优化学术评估过程中通过一致、可扩展和透明的评估所具有的潜在优势。
## 238. `cs.CL` - 从新冠前后十年的社交媒体疫苗帖子看话语变迁 [PDF](https://arxiv.org/pdf/2511.16832), [HTML](https://arxiv.org/abs/2511.16832)
### Authors
Nikesh Gyawali,Doina Caragea,Cornelia Caragea,Saif M. Mohammad
### Background
该研究关注社交媒体上关于疫苗的英语讨论，特别是在X平台（原Twitter）上从2013年至2022年的数据。通过结合社会认知理论和社会心理原型内容模型，研究分析了新冠大流行前后疫苗讨论的演变。研究构建了一个包含数百万个帖子的新数据集，以探讨新冠大流行对公众对疫苗的情绪和讨论的影响。
### Innovation
本研究的创新点在于提出了一个覆盖2013年至2022年在X平台英语用户的1870万条关于疫苗讨论的多样化数据集。此外，研究通过分析情感词汇和情绪词汇的变化，揭示了新冠大流行对疫苗讨论的深远影响，特别是用户情绪从早期的正向逐渐转变为负向。
### Conclusion
新冠大流行导致了X用户关于疫苗的讨论和情感发生了复杂的变化。虽然在早期有积极和信任的情感词汇使用，但到了末期，负面词汇使用显著增加，这可能反映了疫苗犹豫和怀疑的增强。
## 239. `cs.CL` - SMILE：一种复合词项-语义评估指标用于问题回答评估 [PDF](https://arxiv.org/pdf/2511.17432), [HTML](https://arxiv.org/abs/2511.17432)
### Authors
Shrikant Kendre,Austin Xu,Honglu Zhou,Michael Ryoo,Shafiq Joty,Juan Carlos Niebles
### Background
传统的文本和视觉问题回答评估指标，如ROUGE、METEOR和精确匹配(EM)，主要基于词组级别的词汇相似性，往往忽视了准确评估所需深层语义理解。虽然BERTScore和MoverScore等方法利用了上下文嵌入来解决这一局限性，但它们缺乏在句子级别和关键词级别之间平衡语义的理解能力，忽略了词汇相似性，而词汇相似性仍然是重要的考虑因素。大型语言模型（LLM）基于的评估者虽然强大，但也存在成本高、偏见、不一致和幻觉等缺点。
### Innovation
为了应对这些挑战，我们提出了SMILE：语义度量结合词汇精确度，这是一种新的方法，将句子级别的语义理解和关键词级别的语义理解以及易于关键词匹配相结合。这一综合方法平衡了词汇精确性和语义相关性，提供了全面的评估。
### Conclusion
在文本、图像和视频问题回答任务的广泛基准评估中，SMILE高度相关于人类判断，且计算量轻，弥合了词汇和语义评估之间的差距。
## 240. `cs.CL` - 超越多项选择：一种统一稳健评估与可验证推理训练的混合框架 [PDF](https://arxiv.org/pdf/2511.17405), [HTML](https://arxiv.org/abs/2511.17405)
### Authors
Yesheng Liu,Hao Li,Haiyu Xu,Baoqi Pei,Jiahao Wang,Mingxuan Zhao,Jingshu Zheng,Zheqi He,JG Yao,Bowen Qin,Xi Yang,Jiajun Zhang
### Background
多项选择题问答（MCQA）是现代多模态语言模型评估和强化微调（RFT）的一种流行形式。其受限输出格式便于自动验证。然而，研究发现，选项可能会泄露可利用的信息，这使得准确性指标不能准确反映模型的真实能力，并鼓励在RFT过程中进行显式或隐式的答案猜测。
### Innovation
提出了一种名为ReVeL（Rewrite and Verify by LLM）的框架，该框架将多项选择题转换为开放式问题，同时在可能的情况下确保答案可验证。该框架根据不同的答案类型对问题进行分类，并应用不同的重写和验证策略。以此方法进行RFT时，将20,000个MCQA样本转换为开放式问题，并使用GRPO对Qwen2.5-VL模型进行微调。通过ReVeL得到的开放式问答（OpenQA）模型比基于多项选择题训练的模型在开放式问答任务上的表现更好，数据效率更高，奖励信号更稳定。
### Conclusion
ReVeL在评估中揭示了多项选择题基准测试中高达20个百分点的分数膨胀（相对于开放式问答），提高了评判精度，并减少了成本和延迟。代码和数据将公开发布。
## 241. `cs.CL` - OmniScientist: 向人类与AI科学家协同进化的生态系统努力 [PDF](https://arxiv.org/pdf/2511.16931), [HTML](https://arxiv.org/abs/2511.16931)
### Authors
Chenyang Shao,Dehao Huang,Yu Li,Keyu Zhao,Weiquan Lin,Yining Zhang,Qingbin Zeng,Zhiyu Chen,Tianxing Li,Yifei Huang,Taozhong Wu,Xinyang Liu,Ruotong Zhao,Mengsheng Zhao,Xuhua Zhang,Yue Wang,Yuanyi Zhen,Fengli Xu,Yong Li,Tie-Yan Liu
### Background
随着大型语言模型（LLMs）的迅速发展，AI代理展示了在科学任务中日益精湛的技能，涵盖了假说生成、实验设计到论文撰写等多个方面。现有的AI科学家多将科学发现简化为独立的搜索或优化问题，忽略了科研本质上是社会协作的过程。因此，当前系统难以建立真实的科研生态系统，也无法与人类科研社区进行深层次的互动。
### Innovation
本文提出了OmniScientist框架，将人类科研机制明确编码到AI科学家的工作流程中。该框架不仅实现了从数据基础、文献回顾、研究构想到实验自动化、科学论文撰写以及同行评审的端到端自动化，还提供了一个模拟人类科研系统的完整基础设施，包括：基于引文网络和概念关联的结构化知识系统；支持多智能体无缝协作和人类参与的协作研究协议（OSP）；基于匿名对用户评分和Elo排名的开放评价平台（ScienceArena）。这一体系使智能体能够理解并利用人类的知识体系，同时进行协作和共同进化，从而促进持久和可扩展的创新生态系统。
### Conclusion
OmniScientist框架通过模拟和建模人类科研系统的关键维度，使得智能代理能够协同人类科学家更好地进行科研合作与创新，构建了一个可持续发展的创新生态系统。
## 242. `cs.CL` - 爱沙尼亚 WinoGrande 数据集：LLM 在人工与机器翻译之间性能的比较分析 [PDF](https://arxiv.org/pdf/2511.17290), [HTML](https://arxiv.org/abs/2511.17290)
### Authors
Marii Ojastu,Hele-Andra Kuulmets,Aleksei Dorkin,Marika Borovikova,Dage Särg,Kairit Sirts
### Background
本文介绍了一个本地化并适应爱沙尼亚语言的 WinoGrande 常识推理基准数据集的翻译版本。该数据集是广泛使用的 WinoGrande 基准测试的主要英文版本。研究者详细描述了翻译和适应过程，并评估了商业化和开源模型在这个人工翻译基准上的性能。此外，研究还探讨了通过将人工翻译过程中的见解整合到详细提示的设计中以提高机器翻译质量的可行性。提示设计特别针对爱沙尼亚语言的语音特征以及 WinoGrande 数据集带来的独特翻译挑战。
### Innovation
介绍了使用爱沙尼亚语言专家的翻译和适应过程来改进 WinoGrande 数据集的本地化版本。提出了专门针对爱沙尼亚语言特征和 WinoGrande 数据集翻译挑战的详细提示，探讨了利用这些提示提高机器翻译质量的可能性。分析结果显示，人工翻译的爱沙尼亚数据集的模型性能略低于原始英文测试集，而机器翻译的数据集性能显著较差。实验证明提示工程对翻译质量和模型准确性的影响有限，突出了语言专家参与数据集翻译和适应的重要性。
### Conclusion
人工翻译的爱沙尼亚 WinoGrande 数据集上的模型性能略低于原始英文测试集，而机器翻译的数据集上的性能则差别显著。提示工程对翻译质量或模型准确性的影响有限。研究强调需要将语言专家纳入数据集翻译和适应过程，以确保对大型语言模型的语言能力和推理能力的可靠和可解释的评估。
## 243. `cs.CL` - 不学，扎根：视觉扎根在自然语言推理中的案例 [PDF](https://arxiv.org/pdf/2511.17358), [HTML](https://arxiv.org/abs/2511.17358)
### Authors
Daniil Ignatev,Ayman Santeer,Albert Gatt,Denis Paperno
### Background
该研究基于自然语言推理（NLI）领域的已有方法，探讨了如何通过在视觉上下文中扎根语言来实现零样本推理。传统的NLI方法主要依靠文本模式进行推理，而视觉信息在其中的利用并不充分。因此，研究提出了一种新的方法，利用多模态表示并通过文本到图像模型生成视觉表示，再通过比较这些视觉表示与文本假设来进行推理。
### Innovation
该研究创新地提出了一种零样本自然语言推理方法，通过视觉扎根技术改进了现有方法。研究采用了两种不同的推理技术进行评估：余弦相似性和视觉问答系统。该方法在无需特定任务微调的情况下仍能达到高精度，展示了对文本偏见和表面启发式方法的鲁棒性。此外，还设计了受控对抗性数据集以验证方法的鲁棒性。
### Conclusion
研究认为，利用视觉模态作为意义表示，为实现稳健的自然语言理解提供了有前景的方向。该方法的高准确性和对现有偏差的抵抗性展示了其在NLI领域中的潜力。
## 244. `cs.CL` - MusicAIR：一个基于算法驱动核心的多模态AI音乐生成框架 [PDF](https://arxiv.org/pdf/2511.17323), [HTML](https://arxiv.org/abs/2511.17323)
### Authors
Callie C. Liao,Duoduo Liao,Ellie L. Zhang
### Background
近期生成AI的进展使得音乐生成成为研究热点。然而，许多基于神经网络的模型依赖于大数据集，这引发了版权侵权和高性能成本的担忧。
### Innovation
提出了一个名为MusicAIR的创新多模态AI音乐生成框架，该框架由一个新型算法驱动的符号音乐核心提供动力，有效减少了版权侵权的风险。该框架能够仅从歌词生成完整的旋律，且贴合音乐理论、歌词结构和节奏惯例。开发了一个名为Generate AI Music (GenAIM)的网络工具，用于歌词到歌曲、文本到音乐、图像到音乐的生成，并在实验中展示了其能力。
### Conclusion
GenAIM作为一个辅助工具，能够作为一个可靠的作曲助手和可能的教育作曲导师，同时降低了所有音乐爱好者的入门门槛，证明了其在生成多元化、类人作曲方面的能力。
## 245. `cs.CL` - 认知BASIC：一种用于大型语言模型的在模型解释推理语言 [PDF](https://arxiv.org/pdf/2511.16837), [HTML](https://arxiv.org/abs/2511.16837)
### Authors
Oliver Kramer
### Background
本文介绍了一种名为认知BASIC的语言，它是一种最小化的、BASIC风格的提示语言和在模型解释器，旨在将大型语言模型（LLM）的推理结构化为显式的、分步执行踪迹。这种语言受到了复古BASIC语言简洁性的启发，重新利用编号行和简单命令作为一门可解释的认知控制层。现代大型语言模型可以可靠地模拟这样简短的程序，从而在模型内部透明地进行多步推理。
### Innovation
本文的创新点在于提出了一种名为认知BASIC的在模型解释推理语言，通过利用编号行和简单命令，将其作为BASIC风格的解释层。此外，文中还提供了一个自然语言解释器文件，定义了命令语义、内存更新和日志行为，能够从这些程序中提取声明性或程序性知识，并在必要时检测矛盾并提出解决方案。
### Conclusion
通过在三个大型语言模型上进行基准测试，评估了认知BASIC程序的执行情况。结果显示，所有模型都可以执行认知BASIC程序，并且在知识提取、冲突检测和推理任务方面的整体表现强劲，但不同模型之间存在差异。
## 246. `cs.CL` - 奇妙的错误与在AI基准测试中寻找它们的方法 [PDF](https://arxiv.org/pdf/2511.16842), [HTML](https://arxiv.org/abs/2511.16842)
### Authors
Sang Truong,Yuheng Tu,Michael Hardy,Anka Reuel,Zeyu Tang,Jirayu Burapacheep,Jonathan Perera,Chibuike Uwakwe,Ben Domingue,Nick Haber,Sanmi Koyejo
### Background
基准测试在推动AI发展方面发挥着关键作用，但其中的无效问题经常损害其可靠性。人工识别和修正数千个基准测试问题中的错误既不实际，又成为可靠评估的关键瓶颈。
### Innovation
介绍了一种系统化的基准修订框架，该框架利用响应模式的统计分析来标记可能无效的问题，以便进一步由专家审查。该方法基于在AI评估中常用的核心假设，即平均分数足以总结模型性能，从而推断出每项测量实验下预期的统计量范围。当实际估计的统计量值超出某个项目的预期范围时，该项目更可能存在问题。
### Conclusion
该方法在九个广泛使用的基准测试中引导专家审查，并识别出具有高达84%精确度的问题性问题。此外，引入了大语言模型（LLM）作为初步审查手段以减少人力投入，这些成分一起提供了一种高效且可扩展的系统基准修订框架。
## 247. `cs.CL` - 可掩蔽和重排的自我监督训练以提高验证奖励强化学习的性能 [PDF](https://arxiv.org/pdf/2511.17473), [HTML](https://arxiv.org/abs/2511.17473)
### Authors
Zhen Wang,Zhifeng Gao,Guolin Ke
### Background
研究显示，测试时缩放显著提升了大型语言模型（LLMs）的数学推理能力，但仍存在局限性：对于某些数学数据集，尤其是定理证明时，强化学习与奖励验证（RLVR）的可扩展性受限，因为中间推理至关重要，而最终答案难以直接可靠地验证。另外，基于token的强化学习微调往往变成单纯的机械记忆，而不是激发更长链条的思考。受BERT自我监督任务的启发，本文提出了MR-RLVR（掩蔽-重排的RLVR），通过“掩蔽-填写”和“步序重排”构建了过程级的自我监督奖励，从而从中间推理中提取可学习的信号。
### Innovation
1. 提出了MR-RLVR方法，通过“掩蔽-填写”和“步序重排”构建过程级的自我监督奖励机制，以提取中间推理中的可学习信号。2. 建立了两个阶段的训练管道：首先进行自我监督训练，针对抽取的数学计算和证明数据；其次对可验证结果的数学计算数据进行RLVR微调。
### Conclusion
MR-RLVR在Qwen2.5-3B和DeepSeek-R1-Distill-Qwen-1.5B上进行实验证明，相比于原始RLVR，在固定抽样和解码预算下，MR-RLVR在Pass@1、Pass@5和Pass@8上的平均相对增益分别为+9.86%、+5.27%和+4.00%。这些结果表明，引入过程感知的自我监督信号可以有效增强在仅可验证结果设置中RLVR的可扩展性和性能。
## 248. `cs.CL` - 使用长上下文Q-Former结合多模态LLM进行机器人确认生成和动作规划 [PDF](https://arxiv.org/pdf/2511.17335), [HTML](https://arxiv.org/abs/2511.17335)
### Authors
Chiori Hori,Yoshiki Masuyama,Siddarth Jain,Radu Corcodel,Devesh Jha,Diego Romeres,Jonathan Le Roux
### Background
人类与机器人协作完成共同目标需要机器人理解人类的行为及其与周围环境的互动。现有的技术依赖于单个片段中的多模态场景理解来生成与机器人动作确认一致的动作步骤，但未能充分利用整个视频中的长期语境信息。
### Innovation
本文提出了一种结合了左、右上下文依赖性的长上下文Q-Former，并提出了一种文本条件化方法，直接将文本嵌入输入到LLM解码器中，以减轻Q-Former信息的高度抽象性。实验表明，确认生成的准确性是动作规划性能的关键因素，并且长上下文Q-Former通过结合VideoLLaMA3提高了确认和动作规划。
### Conclusion
研究结果表明，结合多模态LLM的长上下文Q-Former在实时实现精确的行动计划和确认方面具有显著优势。
## 249. `cs.CL` - 基于素描引导验证的物理感知视频生成中的规划 [PDF](https://arxiv.org/pdf/2511.17450), [HTML](https://arxiv.org/abs/2511.17450)
### Authors
Yidong Huang,Zun Wang,Han Lin,Dong-Ki Kim,Shayegan Omidshafiei,Jaehong Yoon,Yue Zhang,Mohit Bansal
### Background
近年来，视频生成的方法越来越多地依赖于规划中间的控制信号，如物体轨迹，以提高时间连贯性和运动保真度。但是，这些方法大多采用单次规划方案，通常局限于简单的运动，或者采用迭代优化，这需要多次调用视频生成器，导致巨大的计算成本。
### Innovation
提出了一种名为SketchVerify的无训练、基于素描验证的规划框架，通过在完整的视频生成之前引入测试时取样和验证循环，提高了运动规划的质量。该方法利用文本-视觉验证器预测多个候选运动计划，并根据语义与指令的一致性和物理合理性进行排序。通过将每个轨迹渲染为轻量级视频素描以避免昂贵的重复扩散合成，而实现高效评分。通过迭代精炼运动计划，直到找到满意的计划，然后再将其传递给条件化路径生成器进行最终合成。
### Conclusion
在WorldModelBench和PhyWorldBench上的实验显示出该方法在运动质量、物理现实性和长期一致性方面显著优于竞争基线，同时效率更高。进一步的消融研究显示，增加轨迹候选的数量一致地增强了整体性能。
## 250. `cs.CL` - MiniLLM：大型语言模型的知识蒸馏 [PDF](https://arxiv.org/pdf/2306.08543), [HTML](https://arxiv.org/abs/2306.08543)
### Authors
Yuxian Gu,Li Dong,Furu Wei,Minlie Huang
### Background
知识蒸馏（KD）是一种减少大型语言模型（LLMs）高计算需求的有前途的技术。然而，现有的KD方法主要应用于白盒分类模型或训练小型模型来模拟像ChatGPT这样的黑盒模型API。如何有效地将白盒LLMs的知识蒸馏到小型模型中仍然是未充分探索的问题，尤其是在开源LLMs日益繁荣的背景下，这一问题显得尤为重要。
### Innovation
本文提出了一种新的KD方法，用于将大型语言模型蒸馏为更小的语言模型。具体而言，首先用反向Kullback-Leibler散度（KLD）代替了标准KD方法中正向KLD目标，这更适合生成语言模型的蒸馏，以防止学生模型过高估计教师分布中的低概率区域。然后，提出了一种有效的策略性优化方法来学习这个目标。此外，该方法对不同参数规模的模型（从120M到13B参数）具有可扩展性，并在指令遵循设置下的实验表明，MiniLLM在生成精确度、整体质量、较低的曝光偏差、更好的校准和更长文本生成性能方面优于基线。
### Conclusion
MiniLLM在不同参数规模的模型上都表现出了较好的性能，并且其方法是可扩展的。研究团队提供了代码、数据和模型检查点以供参考。
## 251. `cs.CL` - 视觉语言模型是困惑的游客 [PDF](https://arxiv.org/pdf/2511.17004), [HTML](https://arxiv.org/abs/2511.17004)
### Authors
Patrick Amadeus Irawan,Ikhlasul Akmal Hanif,Muhammad Dehan Al Kautsar,Genta Indra Winata,Fajri Koto,Alham Fikri Aji
### Background
尽管文化维度是评估视觉语言模型(VLMs)的关键方面之一，但这些模型在面对多元文化输入时保持稳定性的能力却未得到充分测试。现有评估往往依赖于单一文化概念的基准，忽视了图像中可能存在的多样的、潜在无关的文化线索共存的场景。这表明对模型在面对复杂多变文化环境时的鲁棒性和稳定性评估是不足的。
### Innovation
我们提出了一个新的文化对抗鲁棒性工具包——ConfusedTourist，专门用于评估VLMs在地理线索扰动下的稳定性。实验结果显示，即使在简单的图像堆叠扰动下，准确率也显著下降，且在基于图像生成的变体中，情况更糟。进一步的可解释性分析表明，这些失败是由于模型的注意力系统性地偏向于分散注意力的线索，导致其偏离原本的关注点。
### Conclusion
复杂的文化概念混杂现象对当前最先进的VLMs构成重大挑战，暴露了在文化多元化背景下模型存在的关键问题。这项工作突显了亟需更加文化鲁棒的跨模态理解，以提高该类模型在多样性社会中的应用效果。
## 252. `cs.CL` - EventWeave: 动态框架在对话系统中捕捉核心和辅助事件 [PDF](https://arxiv.org/pdf/2503.23078), [HTML](https://arxiv.org/abs/2503.23078)
### Authors
Zhengyi Zhao,Shubo Zhang,Yiming Du,Bin Liang,Baojun Wang,Zhongyang Li,Binyang Li,Kam-Fai Wong
### Background
大型语言模型已经提升了对话系统的性能，但通常是在孤立处理对话中的每个发言阶段，忽略了指导自然交互的事件结构。因此，本文引入了EventWeave框架，明确建模对话事件之间的关系，以生成更具上下文适宜性的对话响应。
### Innovation
EventWeave框架构建了一个动态事件图，区分核心事件（主要目标）和辅助事件（相互连接的细节），使用多头注意机制选择性地确定哪些事件与当前回合最相关。不同于总结或标准图论方法，该方法捕捉了三种不同类型的事件关系，提供了更为细腻的语境建模能力。
### Conclusion
实验表明，EventWeave在三个对话数据集上生成的对话响应更加自然、上下文适宜，并且通过针对优化技术减少了所需的计算开销。消融研究表明，改进来自于更好的事件关系建模，而不是信息密度的增加。该方法在各种对话长度上保持了良好的性能。
## 253. `cs.CL` - 跨文化价值对齐框架：负责任AI治理的证据来自中国和西方的比较分析 [PDF](https://arxiv.org/pdf/2511.17256), [HTML](https://arxiv.org/abs/2511.17256)
### Authors
Haijiang Liu,Jinguang Gu,Xun Wu,Daniel Hershcovich,Qiaoling Xiao
### Background
随着大型语言模型（LLMs）在世界各地的高风险决策中发挥越来越重要的作用，确保它们与多元文化价值观的契合度已成为一个关键的治理挑战。
### Innovation
该研究提出了一种多层次审计平台，通过四个集成方法学：伦理困境语料库来评估价值系统的时间稳定性，多样性增强框架（DEF）来量化文化一致性，首词概率一致性来评估分布准确性，以及多阶段推理框架（MARK）来实现可解释的决策。通过与20多个领先模型（如Qwen、GPT-4o、Claude、LaMA和DeepSeek）的比较分析，研究揭示了普遍存在的挑战，如基本的价值系统不稳定、年轻人群的系统性缺乏代表性和模型规模与对齐质量之间的非线性关系。此外，中国的模型越来越注重多语言数据的集成以实现特定的优化，而西方的模型则表现出更多的架构实验性但存在持续的美国中心主义偏见。
### Conclusion
我们确立了Mistral系列架构在跨文化对齐方面明显优于LaMA3系列，全参数微调在多种数据集上优于基于人类反馈的强化学习，以保留文化多样性。
## 254. `cs.CL` - 几何分离遗忘 [PDF](https://arxiv.org/pdf/2511.17100), [HTML](https://arxiv.org/abs/2511.17100)
### Authors
Duo Zhou,Yuji Zhang,Tianxin Wei,Ruizhong Qiu,Ke Yang,Xiao Lin,Cheng Qian,Jingrui He,Hanghang Tong,Heng Ji,Huan Zhang
### Background
机器遗忘，即从已部署模型中移除特定训练子集的影响，对于隐私保护和模型可靠性至关重要。然而，通过梯度上升从记忆样本中学习往往会对保留的知识造成损害。现有方法在这两个方面之间存在固有的权衡：有效遗忘与保留集的保留。虽然过去的解决方案提供了有用的启发式方法，但它们通常缺乏对遗忘更新如何损害保留知识的理论分析，以及这些副作用是否可以有理论保证地消除。
### Innovation
这篇文章从第一性原理出发，分析在模型训练过程中参数小幅度更新对保留集性能影响的第一阶近似。作者提出了一个关键等价关系：保留损失不变的一阶条件下，更新方向与保留梯度生成的子空间正交（“保留不变”）。基于这一关系，提出了几何分离遗忘（GU）方法，该方法将任何候选遗忘梯度更新分解为保留空间的切向和法向分量，并仅执行法向分量的更新。在标准 trusts-region 预算下，与原始遗忘梯度一致的投影方向对所有保保留不变的移动优化而言是最优的。作者还推导了结合遗忘和保留更新目标的最优投影方向。该方法易于集成，可用于现有基于梯度的遗忘程序，以减轻副作用。
### Conclusion
实验结果表明，该方法在TOFU、MUSE和WMDP三个基准上的各种方法中实现了稳健的改进。
## 255. `cs.CL` - 面向大规模语言模型的任务对齐工具推荐 [PDF](https://arxiv.org/pdf/2411.09613), [HTML](https://arxiv.org/abs/2411.09613)
### Authors
Hang Gao,Yongfeng Zhang
### Background
通过将大型语言模型（LLMs）与外部工具结合，它们解决复杂问题的能力得到了显著增强。然而，尽管LLMs的解析能力持续进步，同时将所有可用工具集成到提示中仍因大量外部工具的存在而不可行。因此，为LLMs提供特定任务的精准工具集变得至关重要，考虑工具的数量和质量。目前的工具检索方法主要集中在优化工具列表的排名并直接打包一定数量的高排名工具作为工具集。然而，这些方法往往不能在执行前为LLMs配备最佳工具集，因为不同任务所需的最优工具数量是不同的，这导致了冗余或不合适工具的存在，阻碍了对最相关工具的即时访问。
### Innovation
本文提出了一种新颖的基于精准度的工具推荐方法（PTR）。PTR通过利用历史工具捆绑使用情况并动态进行工具匹配，逐步构造一个多视图的工具集。此外，作者还提出了一个新的数据集RecTools和一个评估指标TRACC，用于评估工具推荐对LLMs的效果。通过全面的实验，证明了设计选择的有效性，并在两个开放基准和RecTools数据集上展示了具有前景的准确性。
### Conclusion
本文提出了一个基于精准度的工具推荐（PTR）方法，通过利用历史工具使用情况和动态匹配工具，构建多视角工具集。该方法成功地实现了针对不同任务的最佳工具推荐，并通过实验展示了在评估指标上的良好表现。
## 256. `cs.CL` - 通过强化学习实现简洁推理 [PDF](https://arxiv.org/pdf/2504.05185), [HTML](https://arxiv.org/abs/2504.05185)
### Authors
Mehdi Fatemi,Banafsheh Rafiee,Mingjie Tang,Kartik Talamadupula
### Background
推理模型的主要缺点是它们对计算成本、资源需求和延迟的高度重视，触发条件是模型使用过多的标记。这种冗余并非来自于更深层次的推理，而是从强化学习的目标中来，当模型产生错误答案时，模型倾向于减少不准确性的补偿。由于不可解的问题主导训练，这种效应交织成一种系统性的倾向，导致生成长输出。进一步的理论分析证明，即使在$boldsymbol{theta} = 1$的情况下，错误的答案也推动策略趋向冗长，将响应长度增加视作优化的一种副作用。此外，还发现简洁性与正确性之间存在一致的相关性，映射到推理和非推理模型中。
### Innovation
提出了一个两阶段的强化学习流程，其中包括一个短周期二级阶段，利用少量可解问题的训练集来显著减少响应长度，同时保持或改善准确性。研究表明，虽然在某些方面GRPO与PPO共享特性，但GRPO独特的崩溃模式限制了其在简洁推理中的可靠性。这些发现均经过大量实验验证。
### Conclusion
理论分析表明，即使$boldsymbol{theta} = 1$，错误答案仍会导致冗长，将响应长度增加视为优化的一种副作用。简洁性和正确性之间存在一致的相关性，且两阶段的强化学习流程显著减少了响应长度，而准确性的保留或提高，GRPO在简洁推理中的可靠性受到限制。
## 257. `cs.CL` - 使用错误严重性映射进行细粒度奖励优化的机器翻译 [PDF](https://arxiv.org/pdf/2411.05986), [HTML](https://arxiv.org/abs/2411.05986)
### Authors
Miguel Moura Ramos,Tomás Almeida,Daniel Vareta,Filipe Azevedo,Sweta Agrawal,Patrick Fernandes,André F. T. Martins
### Background
强化学习（RL）已被证明是训练神经机器翻译系统的有效且稳健的方法，特别是在与准确评估翻译质量的强大奖励模型结合使用时。然而，大多数研究集中在使用句子级反馈的RL方法上，这种方法由于奖励稀疏问题而产生了效率低下的学习信号——模型仅针对整个句子获得单一的评分。为解决这一问题，本研究提出了一种利用细粒度、标记级质量评估以及错误严重等级的新型方法来改进强化学习方法。
### Innovation
本研究引入了一种利用标记级别质量评估系统xCOMET作为奖励模型的创新方法，以克服传统的句子级别反馈带来的奖励稀疏问题。通过对比使用句子级别反馈与细粒度奖励信号对翻译质量的影响，本研究证明了使用标记级别奖励来提高跨语言对的翻译质量。
### Conclusion
本研究使用标记级别奖励信号训练模型，通过自动和人工评估都显示出翻译质量的提高。此外，标记级别奖励优化还提高了模型的训练稳定性，降低了训练过程中的波动，表现为在训练周期中平均奖励的持续增加。
## 258. `cs.CL` - 学术图书馆参考服务中大型语言模型的公平性评估 [PDF](https://arxiv.org/pdf/2507.04224), [HTML](https://arxiv.org/abs/2507.04224)
### Authors
Haining Wang,Jason Clark,Yueru Yan,Star Bradley,Ruiyang Chen,Yiqiong Zhang,Hengyi Fu,Zuoyu Tian
### Background
随着图书馆探索在虚拟参考服务中使用大型语言模型（LLMs），一个关键问题是LLMs能否公平地服务于所有用户，无论其人口统计学或社会地位如何。虽然LLMs在提供可扩展的支持方面具有巨大潜力，但它们也可能在训练数据中嵌入的社会偏见导致公平性受损。为了应对这一问题，作者评估了LLMs是否根据用户的身份差异化其响应，这包括性别、种族/ Ethnicity和机构角色。研究结果表明，当前的LLMs在学术图书馆参考服务中支持公平且具有情境适当性的沟通方面表现出一定的潜力。
### Innovation
研究通过将六种最先进的LLMs置于涉及不同性别、种族/族裔和机构角色的用户场景中，评估了LLMs在用户身份差异上的响应方式。研究发现了种族和族裔差异上不存在差异性，仅在一个模型中发现针对女性的微不足道的刻板偏见。LLMs在机构角色的适应性方面表现出细腻的选择语言方式，包括正式、礼貌和领域专有名词，反映了专业规范而不是歧视性对待。
### Conclusion
当前的LLMs在支持公平且情境适当的学术图书馆参考服务方面显示出了积极的发展趋势，但仍需关注可能存在的社会偏见问题。
## 259. `cs.CL` - Response Attack: 利用上下文提示劫持大型语言模型 [PDF](https://arxiv.org/pdf/2507.05248), [HTML](https://arxiv.org/abs/2507.05248)
### Authors
Ziqi Miao,Lijun Li,Yuan Xiong,Zhenhua Liu,Pengyu Zhu,Jing Shao
### Background
大型语言模型（LLMs）目前存在多种安全威胁，但现有研究大多集中在单一或连续的提示操纵，或静态内文示例注入，这些方法在效果、效率或语义稳定性方面存在一定局限。文章揭示了对话中先前回答可以引导后续行为偏向违反政策的内容，这是一种未被充分探索的攻击面。
### Innovation
文章提出了一种新的攻击框架——Response Attack（RA），利用中间、轻微有害的响应作为上下文提示器，对LLMs进行攻击。RA通过重新构建有害查询并在触发目标提示前注入这些中间响应，利用了LLMs之前未被注意到的脆弱性，从而在多种前沿LLMs上实现了显著更高的攻击成功率。
### Conclusion
实验结果表明，RA的成功直接归因于策略性使用中间响应，这使得模型生成更具体、相关的有害内容，同时保持隐蔽性、高效性和对原始查询的一致性。相关代码和数据可在 提供的链接 中获取。
## 260. `cs.CL` - 大型语言模型中知识存储参数专业化的发展 [PDF](https://arxiv.org/pdf/2505.17260), [HTML](https://arxiv.org/abs/2505.17260)
### Authors
Yihuai Hong,Yiran Zhao,Wei Tang,Yang Deng,Yu Rong,Wenxuan Zhang
### Background
近年来，各种系列的大型语言模型不断引入社区。研究人员正在努力在受限参数规模下最大化语言模型的性能。然而，从微观视角来看，关于如何更好地在模型参数中存储知识，尤其是MLPs中的知识，以更好地利用这些知识，这一领域的研究相对有限。本研究分析了二十个公开的开源大型语言模型，探讨了它们强劲表现与其相应MLP参数中知识存储方式之间的关系。研究发现，随着语言模型变得更为先进，展现出更强的知识能力，其参数显示出更高的专业化倾向。具体来说，MLP中的参数逐渐专注于编码类型相似的知识。
### Innovation
本研究通过实验验证，表明这种知识的专业化分布有助于提高模型对存储知识的利用效率。此外，通过因果训练实验，确认这种专业化知识分布对于提高模型利用存储知识的效率起着关键作用。
### Conclusion
研究发现，语言模型参数的专业化程度越高，其在利用存储知识上的效率也就越高。通过MLP参数的专业化，语言模型能够更有效地编码和利用相似类型的知识，提升模型的整体性能。
## 261. `cs.CL` - ToolHaystack: 在实际长期交互中测试增强工具的语言模型 [PDF](https://arxiv.org/pdf/2505.23662), [HTML](https://arxiv.org/abs/2505.23662)
### Authors
Beong-woo Kwak,Minju Kim,Dongha Lim,Hyungjoo Chae,Dongjin Kang,Sunghwan Kim,Dongil Yang,Jinyoung Yeo
### Background
现有的大型语言模型（LLMs）展示了使用外部工具解决用户查询的强大能力，但大多数现有评估假设工具使用在短语境中，这限制了对模型在真实长时间交互中行为的理解。为了填补这一空白，我们提出了ToolHaystack这一基准测试，用于测试长期交互中的工具使用能力。ToolHaystack包括多个任务执行上下文和连续对话中真实的噪声，以便评估模型如何保持上下文并处理各种干扰。
### Innovation
ToolHaystack引入了一个用于长时间交互的基准测试，允许评估模型如何保持要素和处理各种干扰。与之前的工具基准相比，发现当前的模型在标准的多轮对话中表现良好，但在ToolHaystack中却表现不佳，揭示了它们在长期鲁棒性方面的重要差距。
### Conclusion
通过将ToolHaystack应用于14个最先进的LLMs，我们发现当前模型在标准的多轮对话设置中表现良好，但在ToolHaystack中却显著挣扎，这揭示了它们在长期鲁棒性方面的重要差距，这些差距之前的工具基准并未揭示。
## 262. `cs.CL` - AI在american报纸中的使用广泛、分布不均且很少披露 [PDF](https://arxiv.org/pdf/2510.18774), [HTML](https://arxiv.org/abs/2510.18774)
### Authors
Jenna Russell,Marzena Karpinska,Destiny Akinode,Katherine Thai,Bradley Emi,Max Spero,Mohit Iyyer
### Background
人工智能正在迅速改变新闻业，但其在已发表报纸文章中的使用程度仍然不清楚。本文通过审计2025年夏季1500家美国在线报纸中186,000篇文章的数据集来解决这一问题。
### Innovation
本文使用了最先进的AI检测工具Pangram，发现约9%的新发表文章部分或完全由AI生成。这种AI使用并不均匀，更常出现在小型地方出版物、特定主题如天气和技术领域，以及某些所有者集团中。此外，分析了来自华盛顿邮报、纽约时报和华尔街日报的45,000篇社论文章，发现它们包含AI生成内容的可能性是同期新闻文章的6.4倍，其中许多被标记为AI的社论由著名公众人物撰写。尽管如此，这些文章很少披露使用AI的情况：手动检查100篇标记为AI的文章中只有五篇提及了AI的使用。
### Conclusion
我们的审计突显了新闻界在新闻工作中使用AI需要更大的透明度和更新的编辑标准的紧迫性，以便保持公众信任。
## 263. `cs.CL` - ReviewGuard：通过LLM驱动的数据增强提高不足同行评审检测 [PDF](https://arxiv.org/pdf/2510.16549), [HTML](https://arxiv.org/abs/2510.16549)
### Authors
Haoxuan Zhang,Ruochi Li,Sarthak Shrestha,Shree Harshini Mamidala,Revanth Putta,Arka Krishan Aggarwal,Ting Xiao,Junhua Ding,Haihua Chen
### Background
同行评审作为科学研究的守门人，然近期论文提交量激增以及大型语言模型（LLMs）在学术评估中的普及，带来前所未有的挑战。尽管已有研究侧重于利用LLMs提高评审效率，但从人专家到AI系统的未经过滤的低质量评审（包括由ChatGPT生成的文本）可能系统性地损害学术诚信。因此，需要新的机制来检测和分类这些低质量的评审。
### Innovation
本文提出了一种名为ReviewGuard的自动化系统，通过一个四阶段LLM驱动框架对低质量评审进行检测和分类。该系统包括数据收集、GPT-4.1人工验证标注、合成数据扩充以及采用(encoder-based)模型和开源LLM的微调。研究结果表明，低质量评审在评分较低、自信度较高、缺乏结构性复杂性以及情绪较为消极等方面存在显著差异。混合使用合成和真实数据的训练显著提高了检测性能，例如Qwen 3-8B模型召回率为0.6653，F1得分为0.7073，分别比基础模型提高了20%。
### Conclusion
本文介绍了首个使用LLM驱动的系统来检测不充分的同行评审，其证据可为同行评审中的AI治理提供依据。代码、指令和数据可在指定链接处获取。
## 264. `cs.CL` - RAG-BioQA 在医学文献长文本问答中的检索增强生成 [PDF](https://arxiv.org/pdf/2510.01612), [HTML](https://arxiv.org/abs/2510.01612)
### Authors
Lovely Yeswanth Panchumarthi,Sai Prasad Gudari,Atharva Negi,Praveen Raj Budime,Harsit Upadhya
### Background
生物医学文献的指数级增长带来了获取精确医学信息的巨大挑战。现有的生物医学问答系统主要提供简短答案，不能满足临床决策所需的全面解释。当前的系统无法提供详细的多段落回答，从而影响了决策过程。
### Innovation
RAG-BioQA 是一个结合检索增强生成与领域特定微调的新型框架，用于生成基于证据的长文本生物医学答案。该框架使用 BioBERT 向量与 FAISS 索引结合，并通过比较多种重新排序策略（BM25、ColBERT、MonoT5）来优化上下文选择，最后通过微调的 T5 模型综合证据。实验结果表明 RAG-BioQA 在 PubMedQA 数据集上的表现超过了基线模型，显著提升了 BLEU、ROUGE 和 METEOR 的指标，推动了可访问的基于证据的生物医学知识检索的前沿。
### Conclusion
RAG-BioQA 通过结合检索增强生成和领域特定微调，提供了全面的长文本生物医学答案。实验表明，该方法在多个性能指标上均超过了基线模型，显著提高了生物医学知识的检索质量，为临床决策提供了有力支持。
## 265. `cs.CL` - RPRO: 排序偏好强化优化法以提高医学问答及诊断推理 [PDF](https://arxiv.org/pdf/2509.00974), [HTML](https://arxiv.org/abs/2509.00974)
### Authors
Chia-Hsuan Hsu,Jun-En Ding,Hsin-Ling Hsu,Chih-Ho Hsu,Li-Hung Yao,Chun-Chieh Liao,Feng Liu,Fang-Ming Hung
### Background
医学问答需要高级推理，能够将领域知识与逻辑推理相结合。然而，现有的大型语言模型（LLMs）在生成推理链条时往往缺乏事实准确性与临床可靠性。
### Innovation
提出了RPRO（排序偏好强化优化）框架，该框架结合了强化学习和基于偏好的推理优化，以增强临床推理链条（CoT）的表现。该方法通过使用任务特定的推理模板和概率评估机制，与现有的临床工作流程对齐，从而自动识别和修正低质量的推理链条。相比传统的成对偏好方法，RPRO 引入了基于Bradley--Terry模型的分组排名优化，并结合KL散度正则化以确保训练稳定。
### Conclusion
实验结果显示，RPRO 模型在PubMedQA、MedQA-USMLE 和远东纪念医院的真实世界临床数据集上均表现出一致性的改进。尤其值得指出的是，尽管参数量为2B的RPRO模型比更大规模7B-20B的模型（包括医疗专业化变体）表现更优，这表明将偏好优化与质量驱动的优化相结合，可以提供一个可扩展且基于临床的方法来构建更可靠的医学LLMs。
## 266. `cs.CL` - 从《网络仇恨的社会赞同理论》测试假说：对Parler 1.1亿条信息的分析 [PDF](https://arxiv.org/pdf/2507.10810), [HTML](https://arxiv.org/abs/2507.10810)
### Authors
David M. Markowitz,Samuel Hardman Taylor
### Background
该研究基于Walther的社会赞同理论进行，理论指出网络仇恨背后的动机是为了获得社交认同。理论提出两条假设：假设H1a，更多的社会赞同信号会预测更多的后续网络仇恨言论；假设H1b，随着社会赞同增加，仇恨言论会变得更加极端。该研究使用了2018年至2021年间Parler上发布的1.1亿条消息作为数据源。
### Innovation
研究创新性地运用了大量的数据（1.1亿条消息）来验证关于网络仇恨言论的社会赞同理论。研究表明，虽然社会赞同与极仇恨言论的产生之间存在显著正相关，但与一般仇恨言论的关联性较弱。
### Conclusion
在不同时间间隔内，社会赞同与网络仇恨言论的生产存在平均的正向关联。对于评论而言，社会赞同与网络仇恨的关系比社会反对更为紧密。社会赞同是促进网络仇恨传播的关键机制。
## 267. `cs.CL` - 语义鸿沟：基于GRPO的对比奖励多语种Text-to-SQL [PDF](https://arxiv.org/pdf/2510.13827), [HTML](https://arxiv.org/abs/2510.13827)
### Authors
Ashish Kattamuri,Ishita Prasad,Meetu Malhotra,Arpita Vats,Rahul Raja,Albert Lie
### Background
当前的Text-to-SQL方法主要关注可执行查询，而忽视了语义对齐挑战，包括查询的语义意义和执行结果的正确性。不同语言之间的执行准确性出现了显著下降，平均下降了6个百点。研究指出，当前方法未能有效解决跨语言环境中模型准确理解和生成SQL语句的要求。
### Innovation
文章提出一种结合组相对策略优化（GRPO）和多语种对比奖励信号的新框架，以提升跨语言场景中文本到SQL系统中的任务效率和语义准确性。通过对比奖励信号，模型学习到更好的SQL生成与用户意图之间的对应关系。研究表明，使用该方法的LLaMA-3-3B模型在七种语言的MultiSpider数据集上得到了显著改善，执行准确性提高了26个百点，语义准确性提高了32.86个百点。对于越南语，该对比奖励信号在GRPO框架内进一步提升了语义准确性大约6.85个百点。
### Conclusion
研究证明，使用对比奖励信号优化LLaMA-3-3B模型在执行准确性上提升了7.43个百点，尽管模型参数更小，训练样本数也较少，但执行准确性和语义准确性在某些语言上能与更大规模的零样本Llama-8B模型接近甚至优于它。
## 268. `cs.CL` - 克服基于形状的datatype和object属性提取中SLM微调的一般化限制 [PDF](https://arxiv.org/pdf/2511.03407), [HTML](https://arxiv.org/abs/2511.03407)
### Authors
Célian Ringwald,Fabien Gandon,Catherine Faron,Franck Michel,Hanna Abi Akl
### Background
小型语言模型（SLMs）在使用SHACL形状和常见数据类型属性引导提取RDF三元组时展现了潜力。本研究进一步探讨了SLMs在提取完整RDF图中如何处理数据类型属性和对象属性。研究发现，主要瓶颈在于罕见属性的长尾分布。
### Innovation
研究评估了多种策略，包括分层抽样、加权损失、数据集扩展和基于模板的合成数据增强，提出了一个训练集构建方案，其中每个属性的出现次数超过给定阈值，从而使模型能够均匀处理不平衡的目标属性。
### Conclusion
研究成果提供了培训形状感知SLMs的实际建议，并指出了未来的语义提取研究中具有前景的方向。同时也公开了实验数据、结果和代码以促进研究的可复现性。
## 269. `cs.CL` - 使用大规模训练和与云供应商方法基准测试改进医学影像报告去标识化的性能 [PDF](https://arxiv.org/pdf/2511.04079), [HTML](https://arxiv.org/abs/2511.04079)
### Authors
Eva Prakash,Maayane Attias,Pierre Chambon,Justin Xu,Steven Truong,Jean-Benoit Delbrouck,Tessa Cook,Curtis Langlotz
### Background
当前自动去除医学报告中受保护健康信息（PHI）的模型依赖于较小的训练数据集，可能会影响跨机构的通用性和鲁棒性。研究者旨在通过使用更大的标注数据集扩展基于变压器的模型，并将其性能与商业云供应商系统进行基准测试。
### Innovation
研究者构建了一个基于变压器的PHI去标识化管道模型，并在来自斯坦福大学的两种大型标记医学影像报告语料库上进行了微调，涵盖了胸部X光、胸部CT、腹部/骨盆CT和脑MRI报告。模型引入了一个额外的PHI类别（年龄）并进行了稳定性测试和对比商业系统的性能分析。
### Conclusion
通过大规模、多模态训练，研究证明了该模型在跨机构的一般性和鲁棒性方面优于现有模型。同时，在合成的 PHI 数据上，研究者展示了数据实用性和隐私保护的兼容性，并认为该基于变压器的去标识化模型在 PHI 检测方面超过了以前的学术和商业系统，重新设定了安全临床文本处理的基准。
## 270. `cs.CL` - 评估大型语言模型在罗马尼亚语言文字中的重写变音符表现：一项比较研究 [PDF](https://arxiv.org/pdf/2511.13182), [HTML](https://arxiv.org/abs/2511.13182)
### Authors
Mihai Nadas,Laura Diosan
### Background
富有丰富变音符的语言（如罗马尼亚语）的文本处理中，自动重写变音符至关重要。本文通过一个全面的语料库，测试了包括OpenAI的GPT-3.5、GPT-4、GPT-4o、Google的Gemini 1.0 Pro、Meta的Llama 2和Llama 3、MistralAI的Mixtral 8x7B Instruct、airoboros 70B和OpenLLM-Ro的RoLlama 2 7B在内的多种大型语言模型，在从零样本到复杂多步指令的不同提示模板下的表现。
### Innovation
本文通过使用多种大型语言模型，进行从零到复杂的多步指令提示模板的测试，比较了这些模型在罗马尼亚语文本中重写变音符的表现。这些模型包括了最新的GPT-4o和另类的Llama系列模型。本文的创新在于系统的比较分析不同模型在变音符重写任务中的性能。
### Conclusion
研究结果表明，像GPT-4o这样的模型在变音符重写任务中表现出高准确性，并且持续超过了无偏反馈的基线模型，而Meta的Llama家族模型则显示出更大的变异性。这些发现强调了模型架构、训练数据和提示设计对变音符恢复性能的影响，并为改进变音符丰富的语言的NLP工具指明了积极的方向。
## 271. `cs.CL` - 超越人力判断：大规模语言模型道德价值观理解的贝叶斯评估 [PDF](https://arxiv.org/pdf/2508.13804), [HTML](https://arxiv.org/abs/2508.13804)
### Authors
Maciej Skorski,Alina Landowska
### Background
本文探讨了大型语言模型（LLMs）如何理解道德维度，相比人类的方式。研究采用了第一个大规模的贝叶斯评估方法，不同于以往使用确定性事实（多数或包含规则）的工作，本文通过建模注释者分歧来捕捉人类固有的不确定性（aleatoric不确定性）和模型领域敏感性（epistemic不确定性）。研究在社交媒体、新闻和论坛等10万多个文本上评估了Claude Sonnet 4、DeepSeek-V3和Llama 4 Maverick三个最佳语言模型，共获得了超过25万次注释结果。
### Innovation
本文创新点在于采用大规模的贝叶斯方法进行评估，同时建模注释者分歧以捕捉两类不确定性。方法上，利用GPU优化的贝叶斯框架评估了多个顶级语言模型，结果显示这些模型通常在人类注释者中排名前25%，尤其在减少道德判断的错误否定方面表现优于人类。
### Conclusion
研究发现，AI模型的道德判断敏感度高于人类，主要体现在他们较少产生误判（false negative）。这表明大型语言模型在道德理解方面具备显著优势。该研究表明，尽管在某些方面可能不如人类灵活，但语言模型在道德判断中的准确性值得信赖。
## 272. `cs.CL` - 使用LLM进行一次成-style转移的作者归属性和验证 [PDF](https://arxiv.org/pdf/2510.13302), [HTML](https://arxiv.org/abs/2510.13302)
### Authors
Pablo Miralles-González,Javier Huertas-Tato,Alejandro Martín,David Camacho
### Background
文本计算学 methodNameology 通过文本中的定量模式来分析写作风格，支持从法证任务（如身份关联和抄袭检测）到人文学科中的文学归因等多种应用。监督式和对抗式方法依赖于带有伪相关性的数据，往往将写作风格与主题混淆。虽然现代大型语言模型（LLMs）的预训练自然适用于检测由AI生成的文本，但这些技术在解决一般作者身份问题方面却鲜有应用。
### Innovation
本文提出了一种基于 LLM 丰富预训练数据和上下文学习能力的新颖自监督方法。通过 LLM 的 log-probabilities 来衡量一文本风格向另一文本的转移能力。该方法在规模相当的情况下显著优于LLM提示方法，在控制主题相关性后，性能优于对抗性训练基线。此外，该方法的性能与基础模型的大小关联较为一致，并且在作者身份验证任务中通过额外机制优化了测试时计算，从而在计算成本和准确性之间实现了灵活的权衡。
### Conclusion
该方法能够在控制主题相关性的同时实现高精度，并且随着基础模型大小的增加，其性能也有所提升；在存在额外机制的情况下，作者身份验证任务的性能特征更加一致，从而使计算成本和准确性之间能够灵活调整。
## 273. `cs.CL` - LLMs是否产生具有‘人类特点’的词汇多样性文本？ [PDF](https://arxiv.org/pdf/2508.00086), [HTML](https://arxiv.org/abs/2508.00086)
### Authors
Kelly Kendro,Jeffrey Maloney,Scott Jarvis
### Background
尽管人们对大语言模型（LLMs）是否能生成真正的人类样式的写作给予了大量实证关注，但这个问题的答案仍不清楚。本研究从词汇多样性角度探讨了这个问题，通过比较ChatGPT模型（ChatGPT-3.5, ChatGPT-4, ChatGPT-o4 mini, 和 ChatGPT-4.5）生成的文本与来自150名L1和150名L2英语参与者的写作文本之间的模式。这些参与者的教育水平分为四个等级。
### Innovation
本研究通过测量每篇文章六个词汇多样性的维度：词汇量、丰度、多样性和重复、均匀性、差异性、分散度，使用单因素MANOVA、单因素ANOVA和支持向量机（SVM）来揭示ChatGPT生成的文本与人类写作文本在各变量上的差异，发现最新版的ChatGPT-4.5在词汇多样性方面表现更好，尽管生成的词的数量较少。同时表明，最新的ChatGPT模型生成的文本与人类文本的差异比旧版本更大。
### Conclusion
研究结果表明，ChatGPT模型在词汇多样性方面并不产生真正的人类文本，且新型号生成的文本比旧型号更不接近人类文本。这些结果对语言教学和相关应用具有重要意义。
## 274. `cs.CL` - 从感知到推理：深层思考赋能多模态大型语言模型 [PDF](https://arxiv.org/pdf/2511.12861), [HTML](https://arxiv.org/abs/2511.12861)
### Authors
Wenxin Zhu,Andong Chen,Yuchen Song,Kehai Chen,Conghui Zhu,Ziyan Chen,Tiejun Zhao
### Background
随着多模态大型语言模型（MLLMs）在感知任务中取得显著成功，增强其复杂的推理能力已成为关键的研究焦点。现有模型仍然面临着透明度不足的推理路径和较差的泛化能力等挑战。
### Innovation
链式推理（CoT）在语言模型中展示了显著的效果，通过增强推理的透明度和输出的可解释性，CoT适用于扩展到多模态领域，以改善模型的推理能力。本文从技术演进和任务需求的角度系统地分析了多模态链式推理（MCoT）的背景和理论动机，并介绍了主流MCoT方法，分析了其机理，总结了现有的评估基准和指标，并讨论了MCoT的应用场景。
### Conclusion
最后，本文分析了目前MCoT面临的研究难题，并对其未来的研究方向进行了展望。
## 275. `cs.CL` - AraFinNews: 使用领域适配的大语言模型进行阿拉伯金融摘要 [PDF](https://arxiv.org/pdf/2511.01265), [HTML](https://arxiv.org/abs/2511.01265)
### Authors
Mo El-Haj,Paul Rayson
### Background
该项研究探讨了领域特定性如何影响阿拉伯语金融文本的抽象总结，使用了大语言模型（LLMs）。论文发布了AraFinNews数据集，这是迄今为止最大的阿拉伯语金融新闻数据集，包含约21.25万个文章头部对，涵盖2015年10月至2025年7月近十年的报道。AraFinNews作为阿拉伯语金融环境的基准资源，用于测试和评估语言理解与生成能力。
### Innovation
该研究建设了一个名为AraFinNews的大型阿拉伯语金融新闻数据集，填补了阿拉伯语金融摘要领域的数据空白。通过评估包括mT5、AraT5和领域适配的FinAraT5在内的变换器模型，该研究揭示了领域特定预训练如何影响总结的连贯性、数值可靠性和与专业报道的一致性。
### Conclusion
研究结果表明，领域适配模型在处理定量信息和实体信息时生成的总结更加连贯。这突显了领域特定适应对提高阿拉伯语金融摘要叙述流畅性的价值。数据集免费提供给非商业研究使用。
## 276. `cs.CL` - 从假设到出版：AI驱动研究支持系统的全面综述 [PDF](https://arxiv.org/pdf/2503.01424), [HTML](https://arxiv.org/abs/2503.01424)
### Authors
Zekun Zhou,Xiaocheng Feng,Lei Huang,Xiachong Feng,Ziyun Song,Ruihan Chen,Liang Zhao,Weitao Ma,Yuxuan Gu,Baoxin Wang,Dayong Wu,Guoping Hu,Ting Liu,Bing Qin
### Background
研究是人类文明进步的基本过程，但需要大量时间和努力。近年来，人工智能技术的迅速发展促使研究人员探索如何利用AI加速和增强研究。本研究通过系统性回顾这一领域的进展来监测相关进步。
### Innovation
本研究将相关的研究划分为三大类别：假设形成、假设验证和论文发表。进一步识别并讨论了这些领域面临的当前挑战以及未来研究的潜在方向。本研究还提供了跨多个领域的现有基准和工具的全面概述，以支持AI与研究过程的整合。
### Conclusion
本论文旨在为初学者提供一个介绍，并激发未来研究。相关资源已公开发布于 https://this.link.url 。
## 277. `cs.CL` - 通过语义补充和分解解决多模态情感检测中的情感不一致性 [PDF](https://arxiv.org/pdf/2407.07026), [HTML](https://arxiv.org/abs/2407.07026)
### Authors
Daiqing Wu,Dongbao Yang,Huawen Shen,Can Ma,Yu Zhou
### Background
近年来社交媒体帖子的增多使得在多模态（图-文）内容中检测情感变得非常重要。由于帖子是用户生成的，同一帖子中的图片和文字可能会表达不同的甚至矛盾的情感，这导致了潜在的情感不一致性。现有的工作主要采用了单一分支融合结构，这种结构主要捕捉图文之间的一致情感，忽视或隐式建模了不一致情感，导致了单一模态编码的下降和性能限制。
### Innovation
本文提出了一个语义补充和分解（CoDe）网络来解决这一问题。该网络包括语义补充模块和语义分解模块。语义补充模块通过补充图像和文本的在图中的文本语义，帮助弥合情感差距。语义分解模块则通过独有投影和对比学习分解图像和文本的表示，从而明确地捕捉模态之间的不一致情感。最后，通过交叉注意力融合图像和文本表示，并结合学习到的不一致情感进行最终分类。
### Conclusion
在四个数据集上进行了广泛的实验，结果表明CoDe网络优于其他方法，并且每个提出的模块都有效地提升了 performance。
## 278. `cs.CL` - 大型语言模型中心理病理计算的涌现 [PDF](https://arxiv.org/pdf/2504.08016), [HTML](https://arxiv.org/abs/2504.08016)
### Authors
Soo Yong Lee,Hyunjin Hwang,Taekwan Kim,Yuyeong Kim,Kyuri Park,Jaemin Yoo,Denny Borsboom,Kijung Shin
### Background
本文探讨了大型语言模型（LLMs）能否再现心理病理的计算过程。首先，提出了一个对心理病理学进行一般性和计算性解释的要求，即不依赖于生物体或主观经验的前提下将其应用于计算实体。其次，需要通过实证方法识别LLM内部处理过程中的心理病理计算结构。
### Innovation
本文建立了一个计算理论框架，用于解释心理病理学如何在LLMs中发生。通过实验验证，发现心理病理学的计算结构确实存在于LLMs中，且随着模型规模的增大，这种结构变得更为密集和有效。这表明某些在LLMs中出现的心理病理行为可能不是表面模仿，而是其内部处理过程的一种特征。
### Conclusion
实验结果支持了我们的假设，即心理病理网络计算已经在LLMs中出现。这暗示了未来可能出现由具有心理病理行为的AI系统带来的安全风险，并指出开发新的心理病理学的在硅模型具有潜力。
## 279. `cs.CL` - SALT: 在链式推理中引导激活以实现无泄露思考 [PDF](https://arxiv.org/pdf/2511.07772), [HTML](https://arxiv.org/abs/2511.07772)
### Authors
Shourya Batra,Pierce Tillman,Samarth Gaggar,Shashank Kesineni,Kevin Zhu,Sunishchal Dev,Ashwinee Panda,Vasu Sharma,Maheep Chaudhary
### Background
随着大规模语言模型（LLMs）演变成具有访问敏感用户数据权限的个人助手，它们面临着一个关键的隐私挑战：尽管之前的工作已经解决了输出级别的隐私问题，但最近的研究发现，LLMs经常通过其内部推理过程泄露私人信息，违反了用户对情境隐私的期望。这种泄漏现象发生在模型在推理过程中无意间暴露敏感细节，即使最终输出看似安全。防止此类泄漏同时又不削弱模型的推理能力，需要在隐私保护和实用性之间找到微妙的平衡。
### Innovation
我们提出了Steering Activations towards Leakage-free Thinking (SALT)，一种轻量级的测试阶段干预方法，通过在隐藏状态中注入目标引导向量来减轻模型链式推理（CoT）中的隐私泄露问题。我们确定了导致高泄露行为的高泄漏层。通过在多个LLM上的实验，我们展示了SALT在减轻情境隐私泄露（如AirGapAgent-R数据集）方面的有效性，同时保持了任务性能和实用性。我们的工作将SALT确立为在可推理语言模型中实现测试时隐私保护的一种实际方法，为LLM基础的个人助手的更安全部署提供了途径。
### Conclusion
我们的研究建立SALT作为可推理语言模型中测试时隐私保护的实用方法，为LLM基础的个人助手更安全的部署提供了一个可行的方向。
## 280. `cs.CV` - 画作风格的持久性 [PDF](https://arxiv.org/pdf/2511.16695), [HTML](https://arxiv.org/abs/2511.16695)
### Authors
Reetikaa Reddy Munnangi,Barbara Giunti
### Background
艺术是一种深度个人和表达的媒介，每位艺术家都将其独特的风格、技巧和文化背景融入其作品中。传统上，识别艺术风格是艺术史学家或评论家的工作，依赖于视觉直觉和经验。然而，随着数学工具的进展，我们可以通过更加结构化的视角来探索艺术。
### Innovation
本文展示了持续同调学（PH），一种拓扑数据分析方法，如何提供客观且可解释的洞察艺术风格。通过统计上确凿的证据，PH可以区分不同的艺术家，无论是不同艺术流派还是同一流派，并能区分艺术家的原作与其风格生成的AI图像。
### Conclusion
通过持续同调学（PH），本文表明我们可以用更加结构化和客观的方法来分析和区分不同的艺术风格，从而促进了艺术史和风格分析的进步。
## 281. `cs.CV` - PairHuman: 高保真摄影数据集，用于个性化双人肖像生成 [PDF](https://arxiv.org/pdf/2511.16712), [HTML](https://arxiv.org/abs/2511.16712)
### Authors
Ting Pan,Ye Wang,Peiguang Jing,Rui Ma,Zili Yi,Yu Liu
### Background
个性化双人肖像定制具有广泛的应用潜力，如情感记忆保存和婚礼摄影策划。然而，缺乏基准数据集阻碍了高质量双人肖像生成的发展。
### Innovation
本文提出了PairHuman数据集，这是第一个专门针对高摄影标准的双人肖像生成设计的大规模基准数据集。PairHuman数据集包含超过10万张图像，涵盖各种场景、服饰和双人互动，并附有详细元数据，包括图像描述、人物定位、人体关键点和属性标签。此外，还介绍了DHumanDiff，这是专为双人肖像生成设计的基线方法，增强面部一致性，平衡个性化人物生成和语义驱动场景创建。
### Conclusion
实验结果表明，我们的数据集和方法生成了高度定制、视觉质量出色的个性化双人肖像，符合人类偏好。我们的数据集现已公开，可从此链接访问。
## 282. `cs.CL` - Live-SWE-agent: Can Software Engineering Agents Self-Evolve on the Fly? [PDF](https://arxiv.org/pdf/2511.13646), [HTML](https://arxiv.org/abs/2511.13646)
### Authors
Chunqiu Steven Xia,Zhe Wang,Yan Yang,Yuxiang Wei,Lingming Zhang
### Background
大语言模型（LLMs）正在几乎重塑所有行业，包括软件工程。近年来，已提出多种LLM代理以解决实际软件问题。这些软件代理通常配备了一套编程工具，并能自主决定下一步行动，形成完整的解决问题的轨迹。尽管这种代理具有潜力，但它们通常需要专门的设计，而且可能会存在不足之处，因为要完全探索代理架构设计空间是非常具有挑战性和昂贵的。认识到软件代理本质上是软件，并可以通过进一步精炼和修改来改进，研究员们最近提出了几种能自我改进的软件代理，包括达尔文哥德尔机（DGM）。然而，这些自我改进的代理需要在特定基准的昂贵离线训练后才能生效，而且在不同LLM或基准上可能不具备泛化能力。
### Innovation
本文提出了第一个实时演化软件代理Live-SWE-agent，它能够在解决实际软件问题时自主、持续地自我演化。Live-SWE-agent 从具有最小代理架构和仅访问bash工具（例如mini-SWE-agent）开始，自主演化其架构实现。在广泛研究的SWE-bench Verified基准上的评估显示，Live-SWE-agent 在不使用测试时缩放的情况下达到了令人印象深刻的77.4%解题率，超越了现有的所有软件代理，包括最佳的专有解决方案。此外，Live-SWE-agent 在最近的SWE-Bench Pro基准上超越了最先进的手动设计软件代理，取得了目前最佳的45.8%解题率。
### Conclusion
Live-SWE-agent 是第一个能够实时演化软件代理的解决方案，它在解决实际软件问题时能够自主且持续地自我演化，展示了其强大的自我改进能力和出色的解题效果。
## 283. `cs.CL` - 自从Transformer出现以来的抽取任务系统评价 [PDF](https://arxiv.org/pdf/2511.03610), [HTML](https://arxiv.org/abs/2511.03610)
### Authors
Ringwald Celian,Gandon,Fabien,Faron Catherine,Michel Franck,Abi Akl Hanna
### Background
本文回顾了自Transformer模型出现以来的关系抽取（RE）研究。使用自动化框架收集和标注文献，分析了2019年至2024年间发表的34篇综述文章、64个数据集和104个模型。
### Innovation
本文采用自动化框架系统地审查了基于Transformer的关系抽取研究，对方法学进步、基准资源以及语义网技术的整合进行了分析。通过多维度汇总结果，识别了当前趋势、局限性和开放挑战，为研究人员和实践者提供了理解关系抽取的发展和未来方向的全面参考。
### Conclusion
该研究总结了关系抽取领域的研究动态，并指出了未来的发展方向，为相关领域的研究和实践提供了有价值的参考。
## 284. `cs.CV` - SafeR-CLIP：在保留预训练知识的同时缓解Vision-Language模型中的NSFW内容 [PDF](https://arxiv.org/pdf/2511.16743), [HTML](https://arxiv.org/abs/2511.16743)
### Authors
Adeel Yousaf,Joseph Fioresi,James Beetham,Amrit Singh Bedi,Mubarak Shah
### Background
在对CLIP等视觉-语言模型进行微调以提高安全性时，通常会付出显著下降泛化性能的代价。这种折衷来源于一种僵化的对齐策略，这种策略试图将不安全的概念统一指向单一的预定义安全目标，这反而破坏了模型已学习的语义结构。
### Innovation
我们提出了一种基于邻近感知的方法：将不安全的概念转向与其语义上最近的安全替代物，以最小化表示变化；介绍了SafeR-CLIP，这是一种微调框架，应用了最小干预的原则。
### Conclusion
SafeR-CLIP成功地在安全性和性能之间找到了平衡，比之前的几种方法在零-shot准确率上提高了8.0%，同时保持了鲁棒的安全性。我们还贡献了一个新的基准NSFW-Caps，以支持更严格的评估，包含1000对高度对齐的测试用例，用于检验在分布变化情况下的安全性。我们的工作表明，尊重预训练表征的几何特性是确保安全性而不牺牲性能的关键。
## 285. `cs.CL` - 当偏差伪装成真相：虚假相关性如何在LLMs中削弱幻觉检测 [PDF](https://arxiv.org/pdf/2511.07318), [HTML](https://arxiv.org/abs/2511.07318)
### Authors
Shaowen Wang,Yiqi Dong,Ruinian Chang,Tansheng Zhu,Yuebo Sun,Kaifeng Lyu,Jian Li
### Background
尽管取得了重大进展，大型语言模型（LLMs）仍然会出现幻觉现象，即生成合理的但错误的回答。这项研究聚焦于由虚假相关驱动的幻觉，这些虚假相关是培训数据中表象上的但统计上显著的特征与属性之间的关联，如姓氏与国籍。研究表明，这些虚假相关会引起自信生成的幻觉，不受模型规模的影响，能够避开当前的检测方法，并在拒绝微调后仍然存在。
### Innovation
研究展示了一种系统的控制合成实验，并对最先进的开源和专有LLM（包括GPT-5）进行了实际评估，表明现有的幻觉检测方法（如基于置信度的过滤和内部状态探测）在存在虚假相关的情况下根本无法发挥作用。理论分析进一步解释了为什么这些统计偏差会从根本上削弱基于置信度的检测技术。研究结果强调了需要设计新的方法来明确解决由虚假相关引起的幻觉问题。
### Conclusion
这项研究揭示了幻觉检测方法在面对虚假相关时的根本局限，强调了迫切需要新的方法来应对由虚假相关引起的幻觉。
## 286. `cs.CV` - WorldGen：从文本到可探索和互动的3D世界 [PDF](https://arxiv.org/pdf/2511.16825), [HTML](https://arxiv.org/abs/2511.16825)
### Authors
Dilin Wang,Hyunyoung Jung,Tom Monnier,Kihyuk Sohn,Chuhang Zou,Xiaoyu Xiang,Yu-Ying Yeh,Di Liu,Zixuan Huang,Thu Nguyen-Phuoc,Yuchen Fan,Sergiu Oprea,Ziyan Wang,Roman Shapovalov,Nikolaos Sarafianos,Thibault Groueix,Antoine Toisoul,Prithviraj Dhar,Xiao Chu,Minghao Chen,Geon Yeong Park,Mahima Gupta,Yassir Azziz,Rakesh Ranjan,Andrea Vedaldi
### Background
当前，游戏引擎和虚拟现实技术的发展为创建大规模、互动的3D世界提供了可能。然而，这些过程通常依赖于手动建模或专业3D设计知识，这限制了创建者的灵活性和效率。因此，需要一种能够直接从自然语言描述生成可探索和可编辑的3D环境的技术。
### Innovation
WorldGen系统通过结合LLM驱动的场景布局推理、程序生成、基于扩散的3D生成以及对象感知的场景分解，将自然语言描述转化为可游览并可以立即探索或编辑的环境，适用于标准游戏引擎中。该系统具有模块化特性，支持细致地控制布局、规模和风格，生成几何上一致、视觉丰富且实时渲染效率高的世界。
### Conclusion
WorldGen为大规模生成式世界构建提供了可能，推动了3D生成人工智能在游戏、模拟和沉浸式社交环境中的应用前沿，标志着该领域的一个重要进展。
## 287. `cs.CV` - 使用运动转移增强的StyleGAN生成多样猕猴面部表情 [PDF](https://arxiv.org/pdf/2511.16711), [HTML](https://arxiv.org/abs/2511.16711)
### Authors
Takuya Igaue,Catia Correia-Caeiro,Akito Yoshida,Takako Miyabe-Nishiwaki,Ryusuke Hayashi
### Background
利用生成对抗网络（GAN）技术生成动物面部特征具有挑战性，因为用于训练的图像数量有限且变化不一，尤其是在个体面部表情方面。本文基于广泛研究猕猴（一种广泛应用于系统神经科学和进化研究的物种）的现象，使用了基于StyleGAN2的风格生成图像模型来生成其面部表情。
### Innovation
本文提出了一种新的方法，通过运动转移对静态图像进行动画化以合成新的面部表情图像，基于首先训练好的StyleGAN2模型选择面部形象的潜在表示来确保训练数据集中的变化和采样均匀性，以及通过精炼损失函数来保证精细面部动作（如眼睛运动）的准确复现。这种方法适用于基于风格的图像编辑，特定风格参数对应不同的面部动作。
### Conclusion
提出的生成模型能够生成多种猕猴个体的多样面部表情，优于仅使用原始静态图像训练的模型。此外，该模型在基于风格的图像编辑中表现出色，证明了它能分离出作为样式参数的运动成分，为猕猴面部表情研究提供重要工具。
## 288. `cs.CL` - WER是无感知的：评估ASR错误如何扭曲面向患者的临床对话理解 [PDF](https://arxiv.org/pdf/2511.16544), [HTML](https://arxiv.org/abs/2511.16544)
### Authors
Zachary Ellis,Jared Joselowitz,Yash Deo,Yajie He,Anna Kalygina,Aisling Higham,Mana Rahimzadeh,Yan Jia,Ibrahim Habli,Ernest Lim
### Background
随着自动语音识别（ASR）在临床对话中的广泛应用，标准的评估方法仍然主要依赖于词错误率（WER）。本研究挑战了这一标准，试图探讨WER或其他常见指标是否与转录错误的临床影响相关。
### Innovation
本研究通过建立一个由专家临床人员使用双语料库进行评估的黄金基准，来检验现有指标对转录错误临床影响的评估效果。研究引入了LLM-as-a-Judge，通过DSPy和GEPA进行编程优化，实现了与专家临床评估相当的性能，准确率为90%，Cohen's κ值为0.816，建立了自动化评估框架，促进了ASR评估从单纯的文字准确性向临床对话安全性的必要评估转变。
### Conclusion
这项工作提供了一个验证过的自动化框架，超越了简单的文本一致性，过渡到了对临床对话安全性的必要、可扩展评估。
## 289. `cs.CV` - SAM 3: Segment Anything with Concepts [PDF](https://arxiv.org/pdf/2511.16719), [HTML](https://arxiv.org/abs/2511.16719)
### Authors
Nicolas Carion,Laura Gustafson,Yuan-Ting Hu,Shoubhik Debnath,Ronghang Hu,Didac Suris,Chaitanya Ryali,Kalyan Vasudev Alwala,Haitham Khedr,Andrew Huang,Jie Lei,Tengyu Ma,Baishan Guo,Arpit Kalla,Markus Marks,Joseph Greer,Meng Wang,Peize Sun,Roman Rädle,Triantafyllos Afouras,Effrosyni Mavroudi,Katherine Xu,Tsung-Han Wu,Yu Zhou,Liliane Momeni,Rishi Hazra,Shuangrui Ding,Sagar Vaze,Francois Porcher,Feng Li,Siyuan Li,Aishwarya Kamath,Ho Kei Cheng,Piotr Dollár,Nikhila Ravi,Kate Saenko,Pengchuan Zhang,Christoph Feichtenhofer
### Background
本文介绍了一种名为Segment Anything Model (SAM) 3的统一模型，该模型能够基于概念提示检测、分割和跟踪图像和视频中的物体。这些概念提示可以是短语提示（如“黄色校车”）、图像示例，或者两者的结合。
### Innovation
为了推进Promptable Concept Segmentation (PCS)，作者创建了一个可扩展的数据引擎，该引擎生成了一个包含400万个独特概念标签的数据集，这些标签覆盖了图像和视频，并包含对抗样本。此外，SAM 3模型结合了一个图像级检测器和基于记忆的视频跟踪器，它们共享一个单一的骨干网络。通过采用存在性头部将识别和定位解耦，提升了检测精度。相较于现有系统，SAM 3在图像和视频PCS上的准确性提高了两倍，并在视觉分割任务上改进了先前的SAM能力。
### Conclusion
作者开源了SAM 3以及一个新的Segment Anything with Concepts (SA-Co)基准，用于提示可调用的概念分割任务，展示了其在物体检测、分割和跟踪上的显著提升。
## 290. `cs.CL` - DiffTester：通过重复模式加速扩散大模型的单元测试生成 [PDF](https://arxiv.org/pdf/2509.24975), [HTML](https://arxiv.org/abs/2509.24975)
### Authors
Lekang Yang,Yuetong Liu,Yitong Zhang,Jia Li
### Background
软件开发高度依赖广泛的单元测试，因此自动单元测试生成（UTG）的效率尤为重要。然而，大多数现有的大型语言模型（LLMs）在每次前向传递中逐个生成测试用例，导致UTG效率低下。最近，扩散LLMs（dLLMs）出现，提供了并行生成能力，显示了高效UTG的强大潜力。但由于效率和测试质量之间的权衡，它们在UTG中的应用仍然受限。大量生成每个步骤中的令牌通常会导致测试用例质量急剧下降。
### Innovation
DiffTester是一种专门为dLLMs设计的加速框架，其核心思想是在生成过程中通过抽象语法树分析动态识别相同目标方法的重复结构模式，从而在不牺牲输出质量的前提下增加每个步骤中生成的令牌数量。为此，DiffTester延长了原始的TestEval基准，该基准仅限于Python，增加了Java和C++等其他编程语言。在三个基准上使用两种代表性模型进行的大量实验表明，DiffTester在保持测试覆盖率的同时提供了显著的加速。此外，DiffTester在不同的dLLMs和编程语言上表现良好，提供了一种针对软件开发的高效UTG的实用且可扩展的解决方案。
### Conclusion
DiffTester通过动态识别重复模式，提高了扩散大模型的单元测试生成效率，同时保持了测试覆盖率。该框架适用于不同类型的dLLMs和编程语言，提供了一种有效的解决方案来提高软件开发中的UTG效率。
## 291. `cs.CV` - Parts-Mamba: 基于部分级扫描增强关节上下文的人体骨架遮挡识别 [PDF](https://arxiv.org/pdf/2511.16860), [HTML](https://arxiv.org/abs/2511.16860)
### Authors
Tianyi Shen,Huijuan Xu,Nilesh Ahuja,Omesh Tickoo,Philip Shin,Vijaykrishnan Narayanan
### Background
骨骼动作识别涉及通过人体骨架识别人类动作。图形卷积网络（GCNs）在这一识别任务上取得了重大进展。在现实场景中，由于人体部分遮挡或通信质量差等，捕捉到的骨架图在理论上可能不完美或不完整，导致骨架的缺失部分或视频中关键帧缺失。在这种非理想条件下，现有的GCN模型因缺乏局部上下文而表现不佳。
### Innovation
提出了一种结合GCN和Mamba的混合模型——Parts-Mamba，通过部分特定扫描特征有效捕捉特定部分的上下文信息，并通过部分体融合模块保留非邻近关节上下文。该模型能够在不同的遮挡条件下，在NTU RGB+D 60和NTU RGB+D 120数据集上实现最高12.9%的准确率提升。
### Conclusion
Parts-Mamba模型通过增强关节上下文的建模能力，提升了在遮挡条件下的人体骨架动作识别性能，特别是在缺损骨架数据集上表现显著优于现有GCN模型。
## 292. `cs.CV` - 统一森林生态分析中的视听语言模型 [PDF](https://arxiv.org/pdf/2511.16853), [HTML](https://arxiv.org/abs/2511.16853)
### Authors
Xizhe Xue,Xiao Xiang Zhu
### Background
近年来，视听语言模型（VLMs）在感知和推理方面取得了显著成就，但其在地球观测（EO）中的科学回归潜力尚未得到充分探索。现有EO数据集主要集中在语义理解任务，如描述性 Captioning 或分类，缺乏同时匹配多模态感知和可测量生物物理变量的基准。为解决这一问题，我们提出了 REO-Instruct，这是首个统一的基准，旨在为森林生态场景中的描述性和回归任务提供支持。REO-Instruct 通过建立森林生态系统中的认知可解释逻辑链，连接定性理解和定量预测。
### Innovation
该研究提出了 REO-Instruct，这是首个结合描述和回归任务的森林生态分析统一基准。该基准通过将 Copernicus Sentinel-2 和 ALOS-2 影像与通过人机混合管道生成并验证的结构化文本注释集成在一起，建立了森林生态学中的认知可解释逻辑链，连接了定性理解和定量预测。实验证明，当前模型在数值推理方面表现不佳，揭示了科学视听语言模型的核心挑战。REO-Instruct 为开发和评估能够同时进行描述和科学推理的下一代地理空间模型奠定了标准化基础。
### Conclusion
REO-Instruct 提供了一个标准化的基础框架，用于开发和评估能够在描述和科学推理两方面发挥作用的下一代地理空间模型。项目页面现已公开，可供参考。
## 293. `cs.CV` - BOP-ASK: 用于视觉-语言模型的物体交互推理 [PDF](https://arxiv.org/pdf/2511.16857), [HTML](https://arxiv.org/abs/2511.16857)
### Authors
Vineet Bhat,Sungsu Kim,Valts Blukis,Greg Heinrich,Prashanth Krishnamurthy,Ramesh Karri,Stan Birchfield,Farshad Khorrami,Jonathan Tremblay
### Background
视觉语言模型（VLMs）在空间推理基准测试中取得了显著的成果，但是这些评估掩盖了其理解和物体间交互能力中的关键弱点。现有的基准测试主要关注高层关系（如“左边的”、“后面”的等），但忽略了对于现实世界应用所需的具体三维定位、物体间物理兼容性、物体功能以及多步空间规划等方面的细致的空间理解。因此，需要一个新型的大规模数据集来培训并评估VLMs在物体交互推理方面的表现。
### Innovation
本文提出了BOP-ASK，这是一个新型的大规模数据集，用于物体交互推理的训练和基准测试。该数据集通过利用Benchmark for Object Pose Estimation (BOP)数据集中6D物体姿态生成，衍生出包括抓取姿态、参照物体姿态、路径规划轨迹、相对空间和深度关系、以及物体间关系等详细的注解。BOP-ASK数据集包含超过150K张图片以及33M个问题-答案对，覆盖六个任务（四项为新型任务），为训练和评估VLMs提供了丰富的资源。研究表明，使用BOP-ASK训练的模型优于基线模型，展示了诸如精细的物体和抓取姿态估计，轨迹规划以及杂乱环境中微细的物体中心空间推理等新兴能力。
### Conclusion
我们在BOP-ASK上对私人和开源的VLMs进行了评估，并在BOP-ASK-core上进行了人类评估，后者是一种贡献的测试基准。此外，我们还发布了BOP-ASK-lab，这是一个超出分布的数据集，不使用BOP中的图像，以测试通用性。实验显示BOP-ASK训练的模型在多个方面优于基线模型，展示了物体交互推理的新能力。我们将公开发布我们的数据集和数据集生成管道。
## 294. `cs.CV` - Mesh RAG：基于检索的增强自回归网格生成 [PDF](https://arxiv.org/pdf/2511.16807), [HTML](https://arxiv.org/abs/2511.16807)
### Authors
Xiatao Sun,Chen Liang,Qian Wang,Daniel Rakita
### Background
3D网格是工业设计、游戏、模拟和机器人技术等各种应用中的关键构建块。传统上，网格是由艺术家手工制作的，这个过程既耗时又难以扩展。为了自动化并加快这一资产的创建，自回归模型已在艺术网格生成中展现出强大的能力。然而，当前增强质量的方法通常依赖于更大的模型或更长的序列，这会导致生成时间增加，其固有的顺序性质也带来了质量和速度之间的严重权衡。这种顺序依赖性还显著复杂化了增量编辑。
### Innovation
我们提出了Mesh RAG，一种新的、无需训练的插件即用框架，用于自回归网格生成模型。受到语言模型中RAG的启发，我们的方法通过利用点云分割、空间变换和点云注册来增强生成过程，实现网格组件的检索、生成和集成。这种方法解开了生成与严格顺序依赖性的耦合，促进了高效且并行的推理。
### Conclusion
Mesh RAG在多种基础自回归网格生成模型中均能广泛应用，不仅显著提高了网格质量，还加快了生成速度，相比顺序部分预测更为高效，并且还支持增量编辑，无需对模型重新训练。
## 295. `cs.CV` - Align & Invert: 使用表示对齐的扩散和流基模型解决逆问题 [PDF](https://arxiv.org/pdf/2511.16870), [HTML](https://arxiv.org/abs/2511.16870)
### Authors
Loukas Sfountouris,Giannis Daras,Paris Giampouras
### Background
最近的研究表明，通过调整扩散或流基生成模型的内部表示与预训练自监督编码器的表示之间的对齐，可以显著提升模型的收敛性和样本质量。此工作扩展了这一概念到逆问题中，其中预训练的生成模型用作先验。
### Innovation
提出了一种将扩散或流基模型的表示与预训练的自监督视觉编码器（如DINOv2）对齐的方法（REPA），这可以在推断时指导重建过程。通过与目标特征的近似对齐，可以大幅提高重建的保真度和感知真实性。
### Conclusion
通过理论分析，展示了REPA正则化与DINOv2嵌入空间中散度测量的关系，以及REPA如何引导模型的内部表示向干净图像的表示靠拢。这些结果为理解REPA在提高感知保真度中的作用提供了见解。最后，通过将此方法整合到多个最新的逆问题求解器中，并在高分辨率重建、框内插、高斯去模糊化和运动去模糊化任务上的实验验证了方法的有效性和效率。
## 296. `cs.CV` - SVG360：从单一SVG生成具有几何和色彩一致性的多视图SVG [PDF](https://arxiv.org/pdf/2511.16766), [HTML](https://arxiv.org/abs/2511.16766)
### Authors
Mengnan Jiang,Zhaolin Sun,Christian Franke,Michele Franco Adesso,Antonio Haas,Grace Li Zhang
### Background
Scalable Vector Graphics (SVGs) are central to modern design workflows, offering scaling without distortion and precise editability. However, for single object SVGs, generating multi-view consistent SVGs from a single-view input remains underexplored.
### Innovation
我们提出了一种三阶段框架，该框架从单个SVG输入生成具有几何和色彩一致性的多视图SVG。首先，将栅格化输入提升到3D表示，并在目标摄像机姿态下渲染，生成物体的多视图图像。其次，我们扩展了Segment Anything 2 (SAM2) 中的时间记忆机制到空间域，构建了空间记忆库以在相邻视图之间建立部分水平对应关系，从而提供更清洁和一致的矢量路径和颜色分配，而无需重新训练。最后，在从栅格到矢量的转换过程中，我们进行路径整合和结构优化，以减少冗余并保留边界和语义。结果表明，生成的SVG在视图之间表现出强烈的几何和色彩一致性，显著减少了冗余路径，并保留了精细的结构细节。
### Conclusion
这项工作将生成建模与结构矢量表示相结合，提供了一种从一个输入生成单一对象级别的多视图SVG的可扩展途径，支持资产创建和语义矢量编辑等应用。
## 297. `cs.CV` - 一种基于机器学习的内聚约束融合图像降噪解决方案 [PDF](https://arxiv.org/pdf/2511.16717), [HTML](https://arxiv.org/abs/2511.16717)
### Authors
Asya Y. Akkus,Bradley T. Wolfe,Pinghan Chu,Chengkun Huang,Chris S. Campbell,Mariana Alvarado Alvarez,Petr Volegov,David Fittinghoff,Robert Reinovsky,Zhehui Wang
### Background
中子成像在优化内聚约束聚变（ICF）事件分析和改进当前及未来的ICF平台方面非常重要，但成像质量常被各种噪声影响。常见的噪声类型，如高斯噪声和泊松噪声会共同存在于一幅图像中，导致细节模糊和边缘模糊。传统过滤和阈值方法难以区分和去除这些噪声，因此保持图像保真度的噪声去除技术对于分析和解释中子源的图像至关重要。虽然当前解决方案包括滤波和阈值方法的组合，但自从合成数据生成技术的进步，尤其是在聚变成像领域，提供了利用监督和非监督机器学习方法调查新的去噪程序的机会。
### Innovation
本研究采用了一种非监督自编码器结合Cohen-Daubechies-Feauveau (CDF 97)小波变换在隐空间中进行混合高斯泊松去噪。该网络成功地去除了中子成像数据的噪声，并展示了与由前向模型生成的数据相比，具有较低的重构误差和更优的边缘保持指标。这种做法在中子图像噪声减少和ICF实验的三维重建分析方面展示出一种前景。
### Conclusion
本研究提出了一种非监督自编码器的创新方法，使用CDF 97小波变换在隐空间中进行混合高斯泊松去噪，该方法在测试中展示了较低的重构误差和更优的边缘保持指标，证明了其在中子图像噪声减少和ICF实验的三维重建分析中的有效性。
## 298. `cs.CV` - UniModel：统一视觉空间内的统一多模态理解和生成框架 [PDF](https://arxiv.org/pdf/2511.16917), [HTML](https://arxiv.org/abs/2511.16917)
### Authors
Chi Zhang,Jiepeng Wang,Youming Wang,Yuanzhi Liang,Xiaoyan Yang,Zuoxin Li,Haibin Huang,Xuelong Li
### Background
本文介绍了UniModel，这是一种统一生成模型，在单一像素到像素扩散框架中同时支持视觉理解和生成。该模型旨在从三个维度实现统一：模型、任务和表示。在表示层面，通过将文本和图像都映射到共享的视觉空间，消除模态差异；在任务层面，广泛的观点-语言问题被转化为视窗空间中的像素到像素变换；在模型层面，通过使用像素空间中修正流训练的统一扩散变换器实例化单一模型。
### Innovation
UniModel的核心创新在于实现了一种统一的视觉空间框架，该框架下包含多模态学习的视觉本源表示、广泛视觉语言问题的像素到像素变换、单一统一扩散变换器实例化以及跨模态对齐和可控性实验结果。
### Conclusion
实验表明，UniModel在文本到图像生成和图像到文本理解上具有强大的跨模态对齐和周期一致的图像-描述-图像循环控制能力。初步探索表明，在单一视觉空间中统一模型、任务和表示可能是一个适用于通用多模态智能的有前途的范式。
## 299. `cs.CV` - 使用语义和形状感知的深度学习进行CBCT图像中的形状保坚守齿分割 [PDF](https://arxiv.org/pdf/2511.16936), [HTML](https://arxiv.org/abs/2511.16936)
### Authors
Zongrui Ji,Zhiming Cui,Na Li,Qianhan Zheng,Miaojing Shi,Ke Deng,Jingyang Zhang,Chaoyuan Li,Xuepeng Chen,Yi Dong,Lei Ma
### Background
从锥形束计算机断层扫描（CBCT）图像中精确分割牙齿对于数字牙科至关重要，但在存在牙间粘连导致显著解剖形态失真的情况下，这一任务仍然具有挑战性。
### Innovation
提出了一种深度学习框架，结合了语义和形状感知能力，用于形状保坚守齿分割。该方法引入了目标牙质心引导的多标签学习策略，用于建模牙齿之间的语义关系并减少形状不确定性。此外，引入了牙齿形状感知学习机制，明确地施加了形态学约束以保持边界完整性。这些组件通过多任务学习统一，联合优化分割和形状保真。
### Conclusion
在内部和外部数据集上的广泛评估证明，我们的方法显著优于现有方法，有效减轻了形状失真并提供了解剖上忠实的牙体边界。
## 300. `cs.CV` - 温差扩散：混合模糊与噪音扩散模型的构建方法 [PDF](https://arxiv.org/pdf/2511.16904), [HTML](https://arxiv.org/abs/2511.16904)
### Authors
Hao-Chien Hsueh,Chi-En Yen,Wen-Hsiao Peng,Ching-Chun Huang
### Background
扩散概率模型在各类型数据的生成任务中取得了显著成功。虽然近期研究探索了超越高斯噪音的替代降解过程，但该论文将两种关键的扩散方法联系起来：热扩散完全依赖噪音；冷扩散仅使用模糊而没有噪音。前者因未能利用高频图像细节与低频结构之间的紧密关联，在生成早期表现出随机行为。相比之下，后者虽利用图像相关性进行预测，但忽视了噪音（随机性）在塑造数据流形中的作用，由此导致流形外的问题，这也是其性能下降的部分原因。
### Innovation
该论文提出了温差扩散（Warm Diffusion），一种结合模糊与噪音混合的统一扩散模型（BNMD）。作者采用分而治之的策略，利用图像的频谱相关性，通过分离去噪和去模糊过程简化了得分模型的估计。通过频谱分析，研究进一步探讨了模糊到噪音比率（BNR）对模型学习动态及数据流形变化的影响。
### Conclusion
广泛的基准实验验证了该方法在图像生成中的有效性。
## 301. `cs.CV` - 基于对齐特征密集指导重思扩散模型驱动的视频超分辨率 [PDF](https://arxiv.org/pdf/2511.16928), [HTML](https://arxiv.org/abs/2511.16928)
### Authors
Jingyi Xu,Meisong Zheng,Ying Chen,Minglang Qiao,Xin Deng,Mai Xu
### Background
基于扩散模型（DM）的视频超分辨率（VSR）方法在感知质量方面取得了显著成果，但它们面临错误累积、空间伪影以及感知质量和保真度之间的权衡等问题，这些问题主要源于相邻视频帧之间的对齐不准确和补偿不足。
### Innovation
本文在基于DM的VSR流水线中重新审视了相邻视频帧之间的对齐和补偿作用，并提出了两个关键观察：（a）由于其更强的空间和时间相关性，特征域比像素域更适合信息补偿；（b）在放大分辨率下进行光流扭曲可以更好地保留高频信息，但这种好处并不总是单调增加的。因此，本文提出了一种新颖的具有对齐特征密集引导的扩散模型（DGAF-VSR），它包括一个光学引导扭曲模块（OGWM）以在对齐特征中维持高频细节，以及一个特征层面的时间条件模块（FTCM），以在特征域提供密集指导。
### Conclusion
在合成和现实世界数据集上进行的广泛实验表明，DGAF-VSR在VSR的关键方面超越了最先进的方法，包括感知质量（35.82% DISTS减少）、保真度（0.20 dB PSNR提升）和时间一致性（30.37% tLPIPS减少）。
## 302. `cs.CV` - Q-REAL: Towards Realism and Plausibility Evaluation for AI-Generated Content [PDF](https://arxiv.org/pdf/2511.16908), [HTML](https://arxiv.org/abs/2511.16908)
### Authors
Shushi Wang,Zicheng Zhang,Chunyi Li,Wei Wang,Liya Ma,Fengjiao Chen,Xiaoyu Li,Xuezhi Cao,Guangtao Zhai,Xiaohong Liu
### Background
AI生成内容的质量评估对于评估模型能力和指导模型优化至关重要。然而，现有的大多数质量评估数据集和模型仅提供单一的质量评分，这种评估方式过于粗糙，无法提供针对性的指导以改进生成模型。在当前AI生成图像的应用中，真实感和合理性是两个关键维度。随着统一生成-理解模型的出现，沿这些维度进行精细评估对提高生成性能特别有效。
### Innovation
Q-REAL是一个新的数据集，用于对AI生成图像的真实性和合理性进行精细评估。它包含由流行的文字至图像模型生成的3,088张图像，每个图像都标注了主要实体的位置，并提供了关于这些实体在真实性和合理性维度上的判断问题和归因描述。此外，利用最近多模态大型语言模型（MLLMs）在精细评估AI生成图像方面的能力，构建了Q-REAL Bench，用于在判断和基于推理的定位任务上评估这些模型。
### Conclusion
实验结果表明，该数据集和基准的高质量和重要性，以及评估框架的全面性。该数据集和代码将在发表后发布。
## 303. `cs.CV` - Flow-Guided Implicit Neural Representation for Motion-Aware Dynamic MRI Reconstruction [PDF](https://arxiv.org/pdf/2511.16948), [HTML](https://arxiv.org/abs/2511.16948)
### Authors
Baoqing Li,Yuanyuan Liu,Congcong Liu,Qingyong Zhu,Jing Cheng,Yihang Zhou,Hao Chen,Zhuo-Xu Cui,Dong Liang
### Background
动态磁共振成像(dMRI)能够捕捉到时变解剖结构，但往往受到采样不足和运动伪影的困扰。传统的运动补偿重构通常依赖于预先估计的光学流，但在采样不足的情况下，这种方法不准确，会降低重建质量。
### Innovation
提出了一种新颖的隐式神经表示(INR)框架，该框架同时建模动态图像序列及其潜在的运动场。具体来说，一个INR用于参数化时空图像内容，另一个INR表示光学流。这两种方法通过光学流方程耦合，光学流方程作为一种基于物理的正则化手段，以及与k-空间测量数据一致性损失共同作用，以实现场流调节约束条件下的隐式联合建模。通过联合优化，该方法可以同时恢复时序一致的图像和运动场，无需事先估计流动。
### Conclusion
实验结果表明，提出的该方法在动态心脏MRI数据集上比最先进的运动补偿和深度学习方法具有更优的重建质量、准确的运动估计和更好的时间保真度。这表明场流调节约束条件下的隐式联合建模具有提高dMRI重构的潜力。
## 304. `cs.CV` - 联合Gromov-Wasserstein目标用于多重对象匹配 [PDF](https://arxiv.org/pdf/2511.16868), [HTML](https://arxiv.org/abs/2511.16868)
### Authors
Aryan Tajmir Riahi,Khanh Dao Duc
### Background
Gromov-Wasserstein (GW) 距离是一个强大的工具，用于匹配度量空间中的对象。但是，传统形式的GW距离只适用于单一对象的成对匹配，限制了它在需要多对一或多对多对象匹配的场景和应用中的实用性。
### Innovation
本文引入了联合Gromov-Wasserstein (JGW) 目标，并扩展了原始的GW框架，使其能够同时匹配对象集合。我们的框架提供了一个非负的不相似性度量，能够识别部分同构的mm空间分布，并且具有点采样收敛性。此外，我们表明可以通过调整传统的最优传输算法来实现和解决点云对象表示的JGW目标，包括引入对数正则化。
### Conclusion
与其他GW变体相比，我们的方法在精度和计算效率方面表现出优越性，并且在合成和真实世界数据集上的实验表明，我们的方法适用于多种形状匹配，包括几何形状和生物大分子复合物。这为跨不同领域解决复杂匹配问题提供了有前景的应用前景，包括计算机图形学和结构生物学。
## 305. `cs.CV` - 基于高斯自适应实例强度建模的点监督面部表情检测 [PDF](https://arxiv.org/pdf/2511.16952), [HTML](https://arxiv.org/abs/2511.16952)
### Authors
Yicheng Deng,Hideaki Hayashi,Hajime Nagahara
### Background
自动面部表情识别是面部表情分析的关键，现有方法主要依赖全面监督学习和昂贵的时间消耗的时域边界注释。
### Innovation
提出了一个独特的两分支框架用于点监督面部表情检测(P-FES)，包括基于高斯的实例自适应强度建模模块(GIM)和类别感知的尖峰分类分支。GIM模块通过检测伪顶点帧、估计持续时间并构建实例级高斯分布来为表情帧分配软伪标签，从而提供更可靠的强度监督。类别感知的尖峰分类分支则基于伪顶点帧区分宏表情和微表情。
### Conclusion
通过在SAMM-LV、CAS(ME)²和CAS(ME)³数据集上的广泛实验，验证了所提出框架的有效性，并引入了强度感知对比损失以增强判别特征学习并抑制中性噪声。
## 306. `cs.CV` - DeltaDeno：通过Delta去噪归因实现零样本异常生成 [PDF](https://arxiv.org/pdf/2511.16920), [HTML](https://arxiv.org/abs/2511.16920)
### Authors
Chaoran Xu,Chengkan Lv,Qiyu Chen,Yunkang Cao,Feng Zhang,Zhengtao Zhang
### Background
异常生成通常被框定为基于少量异常样本的微调，这与生成所驱动的稀有性相矛盾，并倾向于过度拟合类别先验。
### Innovation
提出了一种无需训练的零样本异常生成方法Delta-Deno，通过对比由最小提示对驱动的两个去噪分支，在共享时间表下运作，通过累积逐步去噪差值生成图像特定的定位图，指导后期去噪步骤中的潜在修复，同时保留周边的上下文，生成逼真的局部缺陷。此外，通过在预测区域内的异常标记上应用空间注意力偏置并进行标记级提示精炼，提高稳定性和控制。
### Conclusion
实验表明，DeltaDeno在生成质量和下游检测性能方面都取得了显著效果，代码将公开发布。
## 307. `cs.CV` - 利用闪光/非闪光图像中的反射动力学进行玻璃表面检测 [PDF](https://arxiv.org/pdf/2511.16887), [HTML](https://arxiv.org/abs/2511.16887)
### Authors
Tao Yan,Hao Huang,Yiwei Lu,Zeyu Wang,Ke Xu,Yinghui Wang,Xiaojun Chang,Rynson W.H. Lau
### Background
玻璃在日常生活中无处不在，通常透明无色且缺乏显著特征。这些特性使得玻璃表面的检测成为一项具有挑战性的计算机视觉任务。现有的玻璃表面检测方法往往依赖于边界线索（例如窗户和门框）或反射线索来定位玻璃表面，但未能充分利用玻璃本身的内在特性进行准确的定位。
### Innovation
本文观察到，大多数现实场景中，玻璃前面的光照强度与后面不同，导致玻璃表面反射的变化。具体地，当站在玻璃的亮面并对着暗面打闪光灯时，现有的玻璃表面反射会消失；而站在暗面并朝亮面打闪光灯，会在玻璃表面产生明显的反射。基于此现象，我们提出了NFGlassNet，一种利用闪光/非闪光图像中反射动态的玻璃表面检测方法。本文提出了用于提取反射的反射对比挖掘模块（RCMM），以及用于融合反射和玻璃表面特征的反射指导注意力模块（RGAM），以实现准确的玻璃表面检测。此外，我们还构建了一个包含3300对非闪光和闪光图像及其标注的数据库，用于训练我们的网络。
### Conclusion
大量实验表明，我们的方法超越了现有的最先进的方法。我们的代码、模型和数据集将在论文接受后提供。
## 308. `cs.CV` - OmniGround: 一种适用于真实复杂场景的全面时空定位基准 [PDF](https://arxiv.org/pdf/2511.16937), [HTML](https://arxiv.org/abs/2511.16937)
### Authors
Hong Gao,Jingyu Wu,Xiangkai Xu,Kangni Xie,Yunchen Zhang,Bin Zhong,Xurui Gao,Min-Ling Zhang
### Background
时空视频定位(STVG)旨在根据自然语言描述在视频中定位目标对象。尽管近年来多模态大规模语言模型取得了进展，但当前模型仍与实际需求存在差距，特别是在处理多样化对象和复杂查询方面。这归因于基准测试范围受限，导致模型表现出类别偏差、简化推理和语言鲁棒性差的问题。
### Innovation
介绍了OmniGround，这是一个全面的基准，包含3475个视频、81个类别和复杂的真实场景查询。引入了前向-后向- refinement注解流程，结合多方向跟踪和智能错误纠正，以获得高质量的标签。进一步提出了DeepSTG，这是一种系统性评价框架，超越了表面统计数据，从四个互补维度量化数据集质量。实验结果表明，该框架在OmniGround上的m_tIoU和m_vIoU分别提高了25.6%和35.6%，并且在四个基准测试中都获得了一致的改进。
### Conclusion
OmotiGround基准有助于提高模型处理真实复杂场景的能力。提出了一种训练无框架PG-TAF，将其分解为高层次的时空定位和详细的时空传播，该框架在OmniGround上的表现优于现有方法，特别是在处理小/被遮挡对象和复杂的时空关系时。
## 309. `cs.CV` - MultiPriv: 在视觉语言模型中评估个体级隐私推理的基准 [PDF](https://arxiv.org/pdf/2511.16940), [HTML](https://arxiv.org/abs/2511.16940)
### Authors
Xiongtao Sun,Hui Li,Jiaming Zhang,Yujie Yang,Kaili Liu,Ruxin Feng,Wen Jun Tan,Wei Yang Bryan Lim
### Background
现代视觉语言模型（VLMs）展示了复杂的推理能力，超越了简单的属性感知，带来了个级关联的隐私风险。现有的隐私基准结构上不足以应对这种新的威胁，因为它们主要评估隐私感知，而忽视了更关键的隐私推理风险：VLMs推断和链接分散信息以构建个人资料的能力。
### Innovation
我们提出了MultiPriv，这是第一个专门设计来系统评估VLMs个级隐私推理的基准。我们引入了隐私感知与推理（PPR）框架，并构建了一个新的双语多模态数据集来支持它。此数据集包含一个核心组件：合成的个人参考资料，其中标识符（如面孔、姓名）与敏感属性精心链接，并能进行九个具有挑战性的任务评估整个PPR范围，从属性检测到跨图片再识别和链式推理。
### Conclusion
我们的大规模评估显示：（1）许多VLMs存在大量的、未被测量的基于推理的隐私风险。（2）感知级别的指标对这些推理风险的预测很差，揭示了关键的评估缺口。（3）现有的安全对齐是不一致的，且对基于推理的攻击无效。MultiPriv揭示了系统性漏洞，并提供了开发稳健、隐私保护的VLMs必要的框架。
## 310. `cs.CV` - Neighbor GRPO：对比ODE策略优化使流动模型对齐 [PDF](https://arxiv.org/pdf/2511.16955), [HTML](https://arxiv.org/abs/2511.16955)
### Authors
Dailan He,Guanlin Feng,Xingtong Ge,Yazhe Niu,Yi Zhang,Bingqi Ma,Guanglu Song,Yu Liu,Hongsheng Li
### Background
Group Relative Policy Optimization (GRPO) 已经在图像和视频生成模型中表现出对人类偏好对齐的潜力。然而，将其应用到现代流匹配模型中变得具有挑战性，因为它的确定性采样范式。现有方法通过将常微分方程（ODE）转换为随机微分方程（SDE）来解决这个问题，增加了随机性，但这种基于SDE的GRPO在信用分配效率和与高阶求解器的兼容性方面存在问题，特别是在少步采样的情况下。
### Innovation
本文重新解释了现有的基于SDE的GRPO方法，从距离优化的角度出发，揭示了其机制是一种对比学习形式。基于这一洞察，提出了一种新颖的对齐算法——Neighbor GRPO，完全绕过了SDE的使用需求。Neighbor GRPO通过扰动ODE初始噪声条件生成多样化候选轨迹，并使用基于距离的softmax跳跃策略来优化模型。建立了基于距离目标和策略梯度优化之间的理论联系，将方法全面整合到GRPO框架中。该方法完全保留了确定性ODE采样的优点，包括高效性和与高阶求解器的兼容性。
### Conclusion
进一步引入了对称锚点采样以提高计算效率，并通过组内拟范重权来解决奖励拉平问题。广泛实验证明，Neighbor GRPO在训练成本、收敛速度和生成质量方面显著优于基于SDE的对应方法。
## 311. `cs.CV` - 边缘设备上的实时烹饪食物图像合成和视觉烹饪进程监测 [PDF](https://arxiv.org/pdf/2511.16965), [HTML](https://arxiv.org/abs/2511.16965)
### Authors
Jigyasa Gupta,Soumya Goyal,Anil Kumar,Ishan Jindal
### Background
在边缘设备上从生食材生成逼真的烹饪食物图像是一项具有挑战性的生成任务，要求模型捕捉烹饪过程中复杂的纹理、颜色和结构变化。现有的图像到图像生成方法常常会产生不现实的结果，或者在边缘部署时太耗费资源。
### Innovation
该论文提出了第一个基于烤箱的烹饪过程数据集，并由厨师注释烹饪程度。同时，提出了一个边缘设备高效的食谱和烹饪状态引导生成器，能够在原始食物图像的条件下生成逼真的食物图像。该模型引入了特定领域的烹饪图像相似度（CIS）度量，用于训练损失和进程监测信号，以确保时间一致性和烹饪可行性。实验结果表明，该模型的FID分数显著降低，相较于基准模型有30%的改进，在公共数据集上有60%的改进。
### Conclusion
该模型在边缘设备上实现了实时烹饪食物图像合成，并能够监测烹饪进程。通过引入特定领域的烹饪图像相似度度量，模型在时间段一致性和烹饪可验证性方面表现出色，相比于现有基础模型效果更好。
## 312. `cs.CV` - 基于梯度驱动的自然选择方法用于紧凑3D高斯斑点渲染 [PDF](https://arxiv.org/pdf/2511.16980), [HTML](https://arxiv.org/abs/2511.16980)
### Authors
Xiaobin Deng,Qiuli Yu,Changyu Diao,Min Li,Duanqing Xu
### Background
3DGS使用大量高斯原始来拟合场景，导致大量存储和计算开销。现有的剪枝方法依赖于手工设计的标准或引入额外可学习参数，导致效果不佳。
### Innovation
提出了一种受自然选择启发的剪枝框架，将生存压力建模为应用于透明度的正则化梯度场，使由优化梯度驱动的渲染质量最大化目标来自主决定保留或剪枝哪些高斯函数。该过程完全可学习且无需人工干预。引入了带有有限透明度先验的衰减透明度技术，无需牺牲剪枝效果即可加速选择过程。
### Conclusion
与3DGS相比，该方法在15%的预算下实现了超过0.6 dB PSNR增益，建立了紧凑3DGS的最高性能。
## 313. `cs.CV` - R-AVST: 增强视频大语言模型在复杂视听场景中的精细粒度时空推理能力 [PDF](https://arxiv.org/pdf/2511.16901), [HTML](https://arxiv.org/abs/2511.16901)
### Authors
Lu Zhu,Tiantian Geng,Yangye Chen,Teng Wang,Ping Lu,Feng Zheng
### Background
最近，多模态大语言模型（MLLMs）在视频理解任务方面取得了快速进展，特别是在视频理解任务上。然而，当前研究主要集中在简单的视频场景上，未能反映真实世界音频-视觉事件的复杂多样性。因此，存在一个数据差距。
### Innovation
我们首次引入了R-AVST数据集，用于视听推理，包含精细的时间空间注释。通过设计基于大语言模型的关键对象提取、自动空间标注和人工质量检查的流程，构建了超过5000个未剪辑视频，包含27000个对象和100种视听事件类型的标注。在此基础上定义了三维时空推理的核心任务，并生成了8000多个高质量且均匀分布的问题-答案对，以有效评估模型性能。此外，我们提出了一种基于强化学习的AVST-Zero模型，直接优化行为，而无需中间监督，通过精心设计的多维度奖励实现这一点。实验证明，R-AVST数据集在推进视听时空推理方面非常有效，而AVST-Zero模型相比现有模型具有竞争力。
### Conclusion
据我们所知，R-AVST是第一个专门为真实世界视听时空推理设计的数据集。而AVST-Zero为未来这一领域的挑战提供了一种新的视角。
## 314. `cs.CV` - 优化多样性的深度集成方法以实现植物叶片疾病精确检测 [PDF](https://arxiv.org/pdf/2511.16982), [HTML](https://arxiv.org/abs/2511.16982)
### Authors
Sai Nath Chowdary Medikonduru,Hongpeng Jin,Yanzhao Wu
### Background
植物病害对全球农业构成了重大威胁，每年导致超过220亿美元的经济损失，并威胁到粮食安全。及时、准确地从植物叶片图像中检测这些病害对于减轻其不良影响至关重要。深度神经网络集成（Deep Ensembles）已经成为一种增强预测准确性的有力方法，通过利用多种深度神经网络（DNNs）的优势。然而，选择高表现的集成成员模型颇具挑战性，因为很难量化集成的多样性。
### Innovation
本文引入了协同多样性（SQ）框架，以提升植物病害检测精度。首先，对现有集成多样性度量（Q度量）的局限性进行了全面分析，这些度量往往无法识别出最佳的集成团队。其次，提出了SQ度量，这是一种新颖的度量方法，能够捕捉集成成员之间的协同作用，并且始终与集成准确性保持一致。第三，在植物叶片图像数据集上进行了广泛的实验验证了我们的SQ方法的有效性，证明了我们的SQ度量显著提升了集成选择并增强了检测准确性。
### Conclusion
我们的研究结果为基于图像的植物病害检测提供了更加可靠和有效的方法。
## 315. `cs.CV` - FingerCap：细粒度的指尖手部动作描述 [PDF](https://arxiv.org/pdf/2511.16951), [HTML](https://arxiv.org/abs/2511.16951)
### Authors
Xin Shen,Rui Zhu,Lei Shen,Xinyu Wang,Kaihao Zhang,Tianqing Zhu,Shuchen Wu,Chenxi Miao,Weikang Li,Yang Li,Deguo Xia,Jizhou Huang,Xin Yu
### Background
细粒度的人类手部动作理解对于视觉感知、具身智能和多模态通信至关重要。现有视频-语言模型（Video-MLLMs）面临时间稀疏性的基本瓶颈，难以捕捉手指动作的细微动态。为此，本文利用精细的关键帧组（FiGOP）方法，提升对指尖动作的理解和描述能力。
### Innovation
本文提出了细粒度的指尖手部动作描述（FingerCap），旨在生成捕捉到手部动作细粒度语义的文本描述。FingerCap-40K 数据集包含40000对配对的手部动作视频和描述，涵盖指令式的手指动作和自然的手物交互。为解决视频中手指动作的时间稀疏问题，引入了FiGOP方法，将每个RGB关键帧与后续的手部关键点配对，直到下一个关键帧，实现细粒度的时间线索捕获。
### Conclusion
实验结果显示，无论是开源还是闭源的视频-语言模型，在指尖级别的推断上都存在困难，而添加了FiGOP增强的模型在HandJudge评估和人类研究中表现出了持续的进步。
## 316. `cs.CV` - 两头更好：盲超分辨率的双重退化表示 [PDF](https://arxiv.org/pdf/2511.16963), [HTML](https://arxiv.org/abs/2511.16963)
### Authors
Hsuan Yuan,Shao-Yu Weng,I-Hsuan Lo,Wei-Chen Chiu,Yu-Syuan Xu,Hao-Chien Hsueh,Jen-Hui Chuang,Ching-Chun Huang
### Background
以往的方法在单张图像超分辨率（SISR）任务中表现出了出色的性能，尤其是在已知且固定退化的条件下（例如，双立方下采样）。然而，当实际退化与这些假设不一致时，这些方法的性能可能会大幅下降。
### Innovation
本文提出了一个双重支路退化提取网络来解决盲SR问题。该网络预测两个无监督的退化嵌入，分别代表模糊和噪声信息。SR网络可以通过不同的方式适应模糊嵌入和噪声嵌入。此外，将退化提取器作为正则化器使用，利用SR和HR图像之间的差异。
### Conclusion
在多个基准上的广泛实验证明，本方法在盲SR问题中达到了SOTA性能。
## 317. `cs.CV` - DReX:纯监督和卷积表示的视觉融合用于图像复杂性预测 [PDF](https://arxiv.org/pdf/2511.16991), [HTML](https://arxiv.org/abs/2511.16991)
### Authors
Jonathan Skaza,Parsa Madinei,Ziqi Wen,Miguel Eckstein
### Background
图像复杂性预测是计算机视觉中的基础问题，应用于图像压缩、检索和分类。理解人类如何感知图像的复杂性也是认知科学中的长期问题。近年来，一些方法利用了多模态模型结合视觉和语言表示，但是否需要语言信息尚不清楚。最近的研究指出，通过可学习的注意力机制融合自监督和卷积表示，可以预测图像复杂性。
### Innovation
提出了一种名为DReX（DINO-ResNet融合）的纯视觉模型，它通过可学习的注意力机制结合ResNet-50的多尺度层次特征和DINOv3 ViT-S/16的语义丰富表示。该架构在IC9600基准上取得了最先进的性能（皮尔森相关系数为0.9581），并且模型参数量仅为以前方法的约21.5倍。该模型在多个数据集和指标上表现出良好的泛化能力，特别是在皮尔森和斯皮尔曼相关系数、均方根误差和平均绝对误差方面表现优异。消融和注意力分析表明，该模型可以从两个中学习互补线索，进一步增强了对视觉复杂性的敏感性。
### Conclusion
视觉特征本身可以满足人类对复杂性预测的需求，适当融合自监督变换器和监督深度卷积神经网络将为该任务提供互补和协同的益处。
## 318. `cs.CV` - 无参数神经镜头模糊渲染以实现高质量合成 [PDF](https://arxiv.org/pdf/2511.17014), [HTML](https://arxiv.org/abs/2511.17014)
### Authors
Lingyan Ruan,Bin Chen,Taehyun Rhee
### Background
高质量无缝融合3D虚拟对象到实际场景照片中，需要相机镜头模糊的连贯和自然。由于镜头模糊通常会随场景深度变化，因此虚拟对象的摆放和相应的模糊程度对混合现实画面的视觉保真度有很大影响。现有方法常依赖于相机参数（如焦距、对焦距离、光圈大小）和场景深度来计算模糊圈（CoC）以实现真实的镜头模糊渲染，但这些信息往往不为普通用户所具备，限制了这些方法的适用性和通用性。
### Innovation
本文提出了一种新的混合方法，可以直接从RGB图片估计CoC图，无需使用场景深度或相机元数据。虚拟对象的CoC值通过其标示CoC图与深度之间的线性关系进行推断，并使用神经重模糊网络生成真实的镜头模糊效果。这种方法为具有弹性且实际的应用提供了解决方案。
### Conclusion
实验结果表明，该方法能够实现高质量的合成，具有现实的焦距模糊效果，与最先进的技术相比，在定性和定量评估中均表现出优越性。
## 319. `cs.CV` - FLUID：无需训练的面部匿名化方法通过潜在空间的身份置换 [PDF](https://arxiv.org/pdf/2511.17005), [HTML](https://arxiv.org/abs/2511.17005)
### Authors
Jinhyeong Park,Shaheryar Muhammad,Seangmin Lee,Jong Taek Lee,Soon Ki Jung
### Background
在预训练的扩散模型的潜在空间中直接替换身份，无需训练。受化学中的替换机制启发，将身份编辑重新解释为在预训练无条件扩散模型的潜在h空间中的语义置换。研究如何通过优化指导下的新型试剂损失来发现身份编辑方向，监督属性保持和身份抑制。
### Innovation
提出了两套编辑方案，线性和地线性编辑（基于切线），有效导航潜在流形。FLUID框架在CelebA-HQ和FFHQ实验上，展现了在身份抑制和属性保持之间的优越平衡，优于现有最先进的匿名化方法，在定性和定量指标上均有所提升。
### Conclusion
FLUID框架无需训练即可在预训练扩散模型的潜在空间中替换身份，通过优化指导下的新型试剂损失发现身份编辑方向，有效实现身份抑制和属性保持之间的平衡，实验表明在CelebA-HQ和FFHQ上FLUID方法表现优异。
## 320. `cs.CV` - RadioKMoE：利用柯尔莫哥罗夫-阿诺德网络和混合专家的指导性无线信道图估计 [PDF](https://arxiv.org/pdf/2511.16986), [HTML](https://arxiv.org/abs/2511.16986)
### Authors
Fupei Guo,Kerry Pan,Songyang Zhang,Yue Wang,Zhi Ding
### Background
无线网络管理和部署依赖于提供信号传播和覆盖的空间知识的无线信道图。然而，复杂的无线传播行为和周围环境对无线信道图估计（RME）提出了重大挑战。已有模型通常采用深度学习方法，但这类方法难以捕捉物理模型和全球无线传播模式。
### Innovation
提出了一种知识引导的RME框架，结合了柯尔莫哥罗夫-阿诺德网络（KAN）和混合专家（MoE），简称RadioKMoE。该框架中使用KAN模块预测初始粗略的覆盖图，利用其逼近物理模型和全球无线传播模式的优势。初始粗略图与环境信息共同驱动MoE网络进行精确的无线信道图估计。MoE模块包含专门处理不同无线信道图模式的专家网络，从而改善局部细节同时保持全局一致性。
### Conclusion
在多频段和单频段无线信道图估计中，实验结果表明，提出的RadioKMoE相比传统模型，能够提供更高的精度和鲁棒性。
## 321. `cs.CV` - 精益求精：迈向细粒度感知的开集域泛化 [PDF](https://arxiv.org/pdf/2511.16979), [HTML](https://arxiv.org/abs/2511.16979)
### Authors
Yunyun Wang,Zheng Duan,Xinyue Liao,Ke-Jia Chen,Songcan Chen
### Background
开集域泛化（Open-Set Domain Generalization，OSDG）旨在解决部署模型在遇到已有类别变化和未知类别时的情景。尽管目前视觉-语言模型（如CLIP）取得了显著进展，现有的方法仍难以在已知类别的结构风险和未知类别的开放空间风险之间找到平衡，尤其是在区分细粒度视觉相似的“硬未知”类时，容易过度自信。
### Innovation
提出了一个基于语义增强的CLIP框架（SeeCLIP），通过细粒度语义增强解决这一难题。该框架包含语义感知提示增强模块，通过细粒化语义分解图像，进行精细的视觉-语言对齐。引入了双重对比学习，通过排斥（保持与已知类别的可分性）和收敛（保持语义临近性）共同目标，有效定位未知提示。语义引导的扩散模块通过调和提取的语义令牌生成伪未知样本，形成视觉上与已知类别相似但具有关键局部差异的挑战性样本。
### Conclusion
在五个基准上的广泛实验表明，SeeCLIP在准确性上比现有最先进的方法提高了3%，在H分数上提高了5%。
## 322. `cs.CV` - RacketVision: 多球拍体育项目的统一球拍分析基准 [PDF](https://arxiv.org/pdf/2511.17045), [HTML](https://arxiv.org/abs/2511.17045)
### Authors
Linfeng Dong,Yuchen Yang,Hao Wu,Wei Wang,Yuenan HouZhihang Zhong,Xiao Sun
### Background
该论文介绍了RacketVision，这是一个新颖的数据集和基准，用于推动体育分析中的计算机视觉技术进步，涵盖乒乓球、网球和羽毛球。该数据集首次提供了大规模、细致的人拍交互标注，不仅包含传统的球位置标注，还包含球拍的姿态标注，有助于复杂的人机交互研究。它设计来解决三个相互关联的任务：细粒度的球追踪、拍子姿态估计以及预测球的轨迹。
### Innovation
RacketVision的主要创新在于，它提供了一种新的数据集和基准，第一次将球拍姿态与传统球位置标注结合在一起，为复杂的人机交互提供了重要的数据支持。实验结果表明，多模态融合的关键在于使用CrossAttention机制而非简单地将拍子姿态特征拼接起来，这提高了轨迹预测性能，超过了单一模态基线模型。
### Conclusion
RacketVision为动态物体跟踪、条件运动预测以及体育中的多模态分析提供了一个灵活的资源和坚实的基础。项目页面见：this https URL
## 323. `cs.CV` - 在恶劣天气条件下基于VLM的降级建模图像恢复 [PDF](https://arxiv.org/pdf/2511.16998), [HTML](https://arxiv.org/abs/2511.16998)
### Authors
Qianyi Shao,Yuanfan Zhang,Renxiang Xiao,Liang Hu
### Background
在恶劣天气条件下（如雨、雾霾、雪或它们的混合）进行可靠的视觉感知对于自动驾驶和户外机器人来说是具有挑战性的。本研究旨在解决在不同天气条件下恢复图像质量的问题。
### Innovation
提出了一种名为MVLR的统一增强记忆视觉-语言恢复模型，该模型能够处理多种降级水平的图像恢复。该模型结合了轻量级的编码解码器骨干网、视觉-语言模型（VLM）和隐式记忆库（IMB），通过连续的降级模式潜在表示和动态交叉注意机制，增强恢复精度并保持计算效率。
### Conclusion
在四个严重天气基准测试上进行的广泛实验表明，MVLR在峰值信噪比（PSNR）和结构相似性指数测量（SSIM）方面超过了单一分支和混合专家基线。这表明，MVLR在不同户外条件下的实时部署中为模型的紧凑性和表现力提供了一个实际的平衡。
## 324. `cs.CV` - 视觉语言模型是困惑的游客 [PDF](https://arxiv.org/pdf/2511.17004), [HTML](https://arxiv.org/abs/2511.17004)
### Authors
Patrick Amadeus Irawan,Ikhlasul Akmal Hanif,Muhammad Dehan Al Kautsar,Genta Indra Winata,Fajri Koto,Alham Fikri Aji
### Background
尽管文化维度一直是评估视觉-语言模型（VLMs）的关键方面之一，但这些模型在面对多样文化输入的稳定性测试仍然不足。现有评估往往依赖单一文化概念的基准，未充分考虑多个不相关的文化线索共存的场景。这种不足可能导致支持多样性和多元文化社会的能力欠缺。
### Innovation
为了填补这一空白，该研究引入了ConfusedTourist，这是一种新颖的文化对抗稳健性套件，用于评估视觉-语言模型在受到地理线索干扰下的稳定性。实验结果显示，模型在简单图像堆叠干扰下准确率急剧下降，并且使用基于图像生成的变体表现甚至更差。此外，可解释性分析揭示了这些失败源于模型系统地转向了分散注意力的线索，偏离了其初衷。
### Conclusion
这些发现突显了一个关键挑战：视觉文化概念的混合可以严重影响最先进的视觉-语言模型，强调了需要更加强化文化稳健性的多模态理解的迫切性。
## 325. `cs.CV` - 深度聚焦：可控透明场景深度估计 [PDF](https://arxiv.org/pdf/2511.16993), [HTML](https://arxiv.org/abs/2511.16993)
### Authors
Junhong Min,Jimin Kim,Cheol-Hui Min,Minwook Kim,Youngpil Jeon,Minyong Choi
### Background
现实世界的深度很少是单一的。透射材料造成层次上的模糊性，难以让传统的感知系统理解和处理。现有的模型大多被动地工作，试图估计静态的深度图，通常这些图与最近的表面相关联。相比之下，人类能够主动调节焦点，以便感知所需的深度。
### Innovation
本文引入了DepthFocus，这是一种可调节的Vision Transformer，重新定义了立体深度估计为意图引导的控制过程。模型可以根据标量深度偏好动态调整其计算，以聚焦于期望的深度，从而在复杂场景中实现选择性感知。深度Focus主要依赖于我们的新构建的500k多层合成数据集进行训练，该数据集旨在捕捉各种透明效果。此外，它在传统的单一深度基准测试（如BOOSTER）中达到了最先进的性能，在我们的新提出的现实和合成多深度数据集上也能量测出意图对齐的估计结果。
### Conclusion
DepthFocus具有强大的泛化能力，能够应对未见过的透明场景，证明了其作为迈向主动和类人的三维感知的重要步骤的鲁棒性。
## 326. `cs.CV` - MatPedia: 通用高保真材料生成基础模型 [PDF](https://arxiv.org/pdf/2511.16957), [HTML](https://arxiv.org/abs/2511.16957)
### Authors
Di Luo,Shuhui Yang,Mingxin Yang,Jiawei Lu,Yixuan Tang,Xintong Han,Zhuo Chen,Beibei Wang,Chunchao Guo
### Background
目前，基于物理的渲染（PBR）材料对于照片现实图形至关重要，但其创建过程仍然繁重且需要专门的技术。尽管生成模型在材料合成方面取得了进步，现有的方法仍然缺少一个统一的表示方法，它可以将自然图像外观和PBR属性连接起来，导致任务特定的管道被割裂，无法利用大规模的RGB图像数据。
### Innovation
本文介绍了MatPedia，这是一种基于新颖的RGB-PBR联合表示方法的基制模型。该表示方法将材料紧凑地编码为两个相互依赖的潜在空间：一个是RGB外观，另一个是包含四种编码互补物理属性的PBR图。通过将它们作为5帧序列进行建模，并采用视频扩散架构，MatPedia自然地捕捉了这些属性之间的相关性，并从RGB生成模型中转移了视觉先验。这种联合表示使MatPedia能够在单一架构中统一处理多个材料任务，包括从文本到材料的生成、从图像到材料的生成以及内在分解。
### Conclusion
MatPedia在名为MatHybrid-410K的数据集上进行了训练，该数据集结合了PBR数据集和大规模的RGB图像，实现了高质量和多样化的$1024 times 1024$ 像素级别的合成，显著超越了现有方法。
## 327. `cs.CV` - PathAgent: 基于大型语言模型的代理推理以实现全片病理图像的可解释分析 [PDF](https://arxiv.org/pdf/2511.17052), [HTML](https://arxiv.org/abs/2511.17052)
### Authors
Jingyun Chen,Linghan Cai,Zhikang Wang,Yi Huang,Songhan Jiang,Shenjin Huang,Hongpeng Wang,Yongbing Zhang
### Background
分析全片图像（WSIs）需要一个迭代、证据驱动的推理过程，这种过程类似于病理学家在收集证据时动态缩放、重新聚焦和自我纠正。然而，现有的计算流程往往缺乏这种明确的推理轨迹，导致其预测具有内在的不透明性和不可解释性。
### Innovation
本文提出了PathAgent，这是一个无需训练、基于大型语言模型（LLM）的代理框架，模拟了人类专家的反思性、逐步分析方法。PathAgent 能够自主探索WSI，通过Navigator模块迭代且精确地定位显著的微观区域，通过Perceptor模块提取形态学视觉线索，并将这些发现整合到不断演化的自然语言轨迹中，通过Executor。整个观察和决策序列形成了一个显式的思维链，产生完全可解释的预测。在五个具有挑战性的数据集上评估，PathAgent表现出强大的零样本泛化能力，在开放性和约束性视觉问答任务中超越了针对特定任务的基线模型。此外，与病理学家的合作评估证实PathAgent作为透明的临床诊断助手的潜力。
### Conclusion
PathAgent 在五个具有挑战性的数据集上表现出强大的零样本泛化能力，不仅在开放性和约束性视觉问答任务中超越了针对特定任务的基线模型，还得到了与病理学家合作评估的认可，显示出作为透明和临床相关诊断助手的潜力。
## 328. `cs.CV` - OmniPT: 充分挖掘大型视觉语言模型在行人跟踪与理解中的潜力 [PDF](https://arxiv.org/pdf/2511.17053), [HTML](https://arxiv.org/abs/2511.17053)
### Authors
Teng Fu,Mengyang Zhao,Ke Niu,Kaixin Peng,Bin Li
### Background
尽管大型视觉语言模型（LVLMs）在图像级别的任务，如VQA和字幕生成中表现出色，但在实例级别的任务，如视觉定位与物体检测方面，与之前的专家模型相比仍存在性能差距。尽管行人跟踪是一个经典的任务，但将物体跟踪与自然语言结合的新话题，如引用多对象跟踪、跨视图引用多对象跟踪和语义多对象跟踪正在不断发展。这些任务强调模型需要在高级语义级别上理解被跟踪的物体，这是LVLMs的优势所在。
### Innovation
本文提出了一种新的统一行人跟踪框架，即OmniPT，可以进行行人跟踪、基于引用的跟踪，并且可以交互地生成对跟踪对象的语义理解。该框架解决了两个关键问题：如何将跟踪任务模型化为大型视觉语言模型能够执行的任务，以及如何使模型输出格式化答案。为此，本文实施了一个训练阶段，包括RL-Mid训练-SFT-RL。基于预训练的LVLM权重，首先进行一个简单的RL阶段，使模型能够输出固定且可监督的边界框格式；随后，使用大量行人相关的数据集进行中期培训；最后，在多个行人跟踪数据集上进行监督微调，并再次进行RL阶段以提高模型的跟踪性能并增强其指令跟随能力。
### Conclusion
我们在跟踪基准上进行了实验，实验结果表明，所提出的方法在行人跟踪任务上的表现优于之前的方法。
## 329. `cs.CV` - RL-AD-Net: 由强化学习引导的在潜在空间中的自适应位移用于细化点云完成 [PDF](https://arxiv.org/pdf/2511.17054), [HTML](https://arxiv.org/abs/2511.17054)
### Authors
Bhanu Pratap Paregi,Vaibhav Kumar
### Background
现有的点云完成模型，包括基于变换器和去噪的方法，能够从部分输入生成全局合理的形状，但在局部几何一致性方面存在不足。
### Innovation
提出了一种基于强化学习（RL）的细化框架RL-AD-Net，该框架在预训练点自编码器的潜在空间中操作。该框架通过RL代理微调自编码器编码的紧凑全局特征向量（GFVs），以提升几何保真度。通过一个轻量级的非参数PointNN选择器来评估原始完成和RL优化后的输出的几何一致性，从而保留更好的重构结果。
### Conclusion
实验表明，基于RL-AD-Net的方法在随机裁剪场景中显著优于基准模型，突显了强化学习引导的细化策略的有效性。此方法轻量级、模块化且与特定模型无关，适用于各种完成网络且无需重新训练。
## 330. `cs.CV` - 您的视觉自回归模型中一直存在多样性 [PDF](https://arxiv.org/pdf/2511.17074), [HTML](https://arxiv.org/abs/2511.17074)
### Authors
Tong Wang,Guanyu Yang,Nian Liu,Kai Wang,Yaxing Wang,Abdelrahman M Shaker,Salman Khan,Fahad Shahbaz Khan,Senmao Li
### Background
视觉自回归（VAR）模型因其新颖的跨尺度预测范式，相比传统的多步自回归（AR）和扩散模型，在推理效率和图像质量方面具有显著优势。然而，尽管效率较高，VAR模型往往存在多样性衰减的问题，这类似于少数几步蒸馏扩散模型中观察到的现象。
### Innovation
本文提出了DiverseVAR，一种简单而有效的方法，它在不需要额外训练的情况下恢复了VAR模型的生成多样性。研究揭示了特征图的关键成分在早期尺度上决定了多样性的形成。通过在模型输入中抑制关键成分并在输出中增强其效果，DiverseVAR有效地挖掘了VAR模型的潜在生成能力，同时保持了高质量的合成。实验证明，该方法显著增强了生成多样性，性能影响可以忽略。
### Conclusion
实验结果表明，我们的方法在提高生成多样性方面取得了显著效果，而对性能影响很小。我们的代码将在此公开发布：这个 [链接] 。
## 331. `cs.CV` - ReBrain: 使用检索增强扩散从稀疏CT切片重建脑MRI [PDF](https://arxiv.org/pdf/2511.17068), [HTML](https://arxiv.org/abs/2511.17068)
### Authors
Junming Liu,Yifei Sun,Weihua Cheng,Yujin Kang,Yirong Chen,Ding Wang,Guosun Zeng
### Background
磁共振成像（MRI）在脑疾病诊断中扮演着重要的角色，但由于某些患者存在身体或临床限制，MRI并不总是可行的。最近的研究尝试从计算机断层扫描（CT）图像中合成MRI图像；然而，低剂量协议通常会生成具有较差通过平面分辨率的稀疏CT体积。这使得准确重构整个脑部MRI体积变得非常具有挑战性。
### Innovation
我们提出了ReBrain，一种检索增强的扩散重建框架，用于脑MRI重构。给定具有有限切片的3D CT扫描，我们首先使用布朗桥扩散模型（BBDM）沿2D维度合成MRI切片。同时，我们通过微调的检索模型从全面的先验数据库中检索结构和病理上相似的CT切片作为参考，通过ControlNet分支整合这些切片以指导中间MRI切片的生成并确保结构一致性。此外，我们还考虑了数据库缺乏适当参考时的检索失败情况，并应用球面线性插值方法提供补充指导。
### Conclusion
在SynthRAD2023和BraTS上进行的大量实验证明，ReBrain在稀疏条件下跨模态重建中达到了最先进的性能。
## 332. `cs.CV` - RoomPlanner：更容易实现的基于LLM的3D房间生成明确定位计划 [PDF](https://arxiv.org/pdf/2511.17048), [HTML](https://arxiv.org/abs/2511.17048)
### Authors
Wenzhuo Sun,Mingjian Liang,Wenxuan Song,Xuelian Cheng,Zongyuan Ge
### Background
当前，生成逼真的室内三维场景通常需要详细的输入和大量的手动设计工作。手动布局设计复杂且耗时，导致整个生成流程难以实现自动化。因此，研究如何通过短文本输入自动生成三维室内场景成为了一个重要课题。
### Innovation
本文提出了一个名为RoomPlanner的框架，该框架是首个完全自动化的三维房间生成框架。能够仅通过短文本输入自动生成符合语义描述的对象布局和背景信息，不需要任何手动布局设计或全景图指导。RoomPlanner利用语言驱动的代理计划者层次结构，自动解析模糊的短文本指令，生成详细的场景描述，进而指导三维点云的初始化。它还引入了两种安排约束策略，确保空间布局的自洽性和可达性，并提出了新的AnyReach采样策略和Interval Timestep Flow Sampling (ITFS)策略来优化初步的三维高斯场景表示。
### Conclusion
通过大量实验展示了该方法能够在短时间内生成几何上合理的三维室内场景，并在渲染速度和视觉质量上超越了已有方法，同时保持了易于编辑的特点。此框架有效地克服了现有技术在自动化生成三维室内场景方面的局限性。
## 333. `cs.CV` - REArtGS++: Generalizable Articulation Reconstruction with Temporal Geometry Constraint via Planar Gaussian Splatting [PDF](https://arxiv.org/pdf/2511.17059), [HTML](https://arxiv.org/abs/2511.17059)
### Authors
Di Wu,Liu Liu,Anran Huang,Yuyan Liu,Qiaoyu Jun,Shaofan Liu,Liangtu Song,Cewu Lu
### Background
 articulated 对象在日常环境中普遍存在，例如抽屉和冰箱。现有方法 REArtGS 使用多视角 RGB 图像在两个不同状态下游离对象进行部分级别的表面重建和关节参数估计，但仍存在处理螺钉关节或多部件对象的困难，并且缺乏对未见状态的几何约束。
### Innovation
本文提出了一种新的方法 REArtGS++，通过引入时间连续的几何约束和平面高斯点绘制技术，实现一般可泛化的灵巧对象重建。具体创新包括：1. 对每个关节建模未类型先验的解耦螺旋运动；2. 通过部分运动混合联合优化部分意识的高斯函数和关节参数；3. 通过泰勒一阶展开引入一致的时间几何约束，鼓励高斯函数成为平面，并通过平面正交和深度的一致性正则化实现几何约束。
### Conclusion
在合成数据和真实世界的数据集上的实验表明，相比较现有方法，我们在泛化部分级别的表面重建和关节参数估计方面具有优势。项目页面：this https URL。
## 334. `cs.CV` - ChainV: 原子级视觉提示让多模式推理更高效且准确 [PDF](https://arxiv.org/pdf/2511.17106), [HTML](https://arxiv.org/abs/2511.17106)
### Authors
Yuan Zhang,Ming Lu,Junwen Pan,Tao Huang,Kuan Cheng,Qi She,Shanghang Zhang
### Background
近期，多模态推理模型在文本和视觉处理方面展示了令人印象深刻的能力。然而，即使是最先进的模型在生成长推理链时也会表现出冗余的自我反思。尽管在大型语言模型（LLMs）领域已经出现了训练无需要的自我推理压缩方法，但它们依赖于静态的视觉参考，因此在多模态推理方面提供的改进有限。
### Innovation
我们提出了ChainV框架，这是一种动态将视觉提示整合到推理过程中的方法，旨在使多模态推理更加精简且高效。具体而言，ChainV先基于之前的推理步骤进行粗略的视觉补丁选择，然后通过识别平均注意力强度下的最具有代表性的原子级视觉提示来进行优化。此外，ChainV引入了一种基于一致性的评估机制来评估所选提示的可靠性，从而引导模型适当地调整其自我反思的水平。最终，所选择的视觉提示的像素坐标及其可靠性通过伯努利随机过程融入到推理过程中。
### Conclusion
实验表明，我们的方法显著提高了推理准确性和效率，尤其是在数学密集型基准测试中，视觉提示对于多步符号推理至关重要。例如，在MIMO-VL-RL的MathVista数据集上，ChainV实现了2.3%的准确率提升，推理延迟减少了51.4%，输出令牌长度缩短了24.5%。
## 335. `cs.CV` - 视频中稀疏推理就足够了：大型预训练模型驱动的视频异常检测生物启发框架 [PDF](https://arxiv.org/pdf/2511.17094), [HTML](https://arxiv.org/abs/2511.17094)
### Authors
He Huang,Zixuan Hu,Dongxiao Li,Yao Xiao,Ling-Yu Duan
### Background
视频异常检测（VAD）在安全监控、自主驾驶和工业监测等实际应用中发挥着重要作用。最近，大型预训练模型的发展为无需训练的VAD提供了新的机会，通过利用丰富的先验知识和泛化的推理能力。然而，现有研究通常依赖于密集的帧级推理，导致高计算成本和延迟。因此，研究稀疏推理是否足以利用强大预训练模型进行有效的VAD成为一个关键问题。
### Innovation
该论文提出了ReCoVAD，这是一种受到人类神经系统双重反射和意识路径启发的新型框架。ReCoVAD包括两个核心路径：反射路径借助轻量级的CLIP模块融合视觉特征与原型提示，并产生决策向量，用于查询过去的帧记忆和异常分数以实现快速响应；意识路径采用中等规模的视觉-语言模型生成新的文本事件描述和异常评分，并更新记忆和原型提示，同时集成的大语言模型定期审查累积描述以识别未知异常、更正错误并优化原型。
### Conclusion
广泛的实验结果表明，ReCoVAD不仅实现了最先进的训练无需消耗性能，在UCF-Crime和XD-Violence数据集上仅使用了之前方法所使用帧的28.55%和16.04%。这证明了在大型模型驱动的VAD中，稀疏推理足以提供有效的性能。
## 336. `cs.CV` - 在FPGA上部署学习图像压缩的多阶段优化框架 [PDF](https://arxiv.org/pdf/2511.17135), [HTML](https://arxiv.org/abs/2511.17135)
### Authors
Jiaxun Fang,Li Chen
### Background
基于深度学习的图像压缩（LIC）已经达到了最先进的率失真（RD，Rate-Distortion）性能，然而部署这些模型到资源受限的FPGAs上仍然面临巨大挑战。
### Innovation
该研究提出了一个全面的多阶段优化框架，旨在弥补高性能浮点模型与高效的、硬件友好的定点实现之间的差距。首先，该优化方案解决了量化引起的性能下降的问题，通过一种称为动态范围感知量化（DRAQ）的方法，结合统计校准的激活截断和一种新颖的权重正则化方案，以应对极端数据异常值和大动态范围的影响，从而成功创建了高保真的8位整数模型；其次，基于此坚实的基础，引入了两种针对FPGAs的硬件感知优化技术。一种渐进的混合精度搜索算法利用FPGA的灵活性为每一层赋予最优的非均匀位宽，从而在保持性能的同时减少复杂度；另一种通道剪枝方法适应适用于LIC模型中的通用除性归一化（GDN）层，通过消除不活跃的通道来减少模型冗余。
### Conclusion
全面的实验表明，基础的DRAQ方法将基于GDN的模型的双向率（BD-rate）开销从30%降低到6.3%。之后的硬件感知优化技术进一步通过超过20%的计算复杂度减少，对RD性能影响不大，得到一个不仅在效率上达到最先进水平并在质量上优于现有的FPGA基LIC实现的最终模型。
## 337. `cs.CV` - PEGS：通过三维高斯点绘制增强的物理事件大时空运动重建 [PDF](https://arxiv.org/pdf/2511.17116), [HTML](https://arxiv.org/abs/2511.17116)
### Authors
Yijun Xu,Jingrui Zhang,Hongyi Liu,Yuhan Chen,Yuanyang Wang,Qingyao Guo,Dingwen Wang,Lei Yu,Chu He
### Background
在大时空尺度上重建刚性运动仍然是一项具有挑战性的工作，原因在于现有的建模范式的限制、严重的运动模糊以及物理一致性不足。
### Innovation
提出了一个框架（PEGS），该框架将物理先验与事件流增强整合到三维高斯点绘制管道中，用于进行去模糊目标聚焦建模和运动恢复。该框架引入了一个统一的三级别监督方案，通过加速度约束确保物理合理性，利用事件流提供高时间分辨率的指导，并采用卡尔曼正则化器融合多源观测。此外，设计了一种运动感知的模拟退火策略，根据实时的运动状态适配训练过程。
### Conclusion
实验表明，PEGS 在重建大时空尺度上的运动方面具有优越的性能，相比于主流的动力学方法有更好的表现。
## 338. `cs.CV` - One-Step Diffusion Transformer for Controllable Real-World Image Super-Resolution [PDF](https://arxiv.org/pdf/2511.17138), [HTML](https://arxiv.org/abs/2511.17138)
### Authors
Yushun Fang,Yuxiang Chen,Shibo Yin,Qiang Hu,Jiangchao Yao,Ya Zhang,Xiaoyun Zhang,Yanfeng Wang
### Background
最近基于扩散的实境图像超分辨率（Real-ISR）技术在感知质量方面取得了显著进展，但保真度和可控性之间的平衡仍是一个问题。多步扩散方法因生成多样性和随机性导致保真度较低，而一步方法在进行保真度特异性微调时失去了控制灵活性。
### Innovation
ODTSR（One-Step Diffusion Transformer for Super-Resolution）通过结合一个新引入的视觉流和原始视觉流以形成噪声混合视觉流 (NVS)，同时处理低质量图像和可调噪声，以及结合保真度意识对抗训练 (FAA) 一步实现可控性。这使得ODTSR不仅能实现通用Real-ISR的最先进的性能，还能在如中文字符的实况场景文本图像超分辨率（STISR）等挑战性场景中实现提示可控性，而无需特定数据集的训练。
### Conclusion
ODTSR在泛化Real-ISR和特定场景如STISR的可控性上取得了显著成果，不仅实现了最先进的性能，还具有高效的推理能力。
## 339. `cs.CV` - Spanning Tree Autoregressive Visual Generation [PDF](https://arxiv.org/pdf/2511.17089), [HTML](https://arxiv.org/abs/2511.17089)
### Authors
Sangkyu Lee,Changho Lee,Janghoon Han,Hosung Song,Tackgeun You,Hwasup Lim,Stanley Jungkyu Choi,Honglak Lee,Youngjae Yu
### Background
传统的自回归（AR）模型在视觉生成中存在一定的局限性，尤其是在处理图像编辑时，随机排列的序列顺序要么导致性能下降，要么限制了在推理时对序列顺序选择的灵活性。
### Innovation
提出了Spanning Tree Autoregressive（STAR）建模方法，它能够整合图像的先验知识（如中心偏见和局部性），在保持采样性能的同时，提供足够灵活的序列顺序以适应图像编辑，同时采用均匀生成树的遍历顺序在由图像片段位置定义的格子中进行采样，通过广度优先搜索构建遍历顺序，从而确保通过拒绝采样生成的图像片段的连接部分观察在整个序列中作为前缀。
### Conclusion
STAR 方法通过定制化但仍具有结构化的随机策略，保留了后缀完成的能力，同时保持了采样性能，而无需对广泛采用的语言自回归建模中的模型架构进行任何显著更改。
## 340. `cs.CV` - SPAGS: Sparse-View Articulated Object Reconstruction from Single State via Planar Gaussian Splatting [PDF](https://arxiv.org/pdf/2511.17092), [HTML](https://arxiv.org/abs/2511.17092)
### Authors
Di Wu,Liu Liu,Xueyu Yuan,Qiaoyu Jun,Wenxiao Chen,Ruilong Yan,Yiming Tang,Liangtu Song
### Background
文中提到，连杆物体在日常环境中普遍存在，其3D重建在此前多个领域都具有重要意义。然而，现有的连杆物体重建方法往往需要多阶段、多视角观察等昂贵的输入，这限制了它们的应用。
### Innovation
本文提出了一个基于平面高斯点云的连杆物体重建框架，仅需单状态下的稀疏视角RGB图像。具体而言，作者引入了一个高斯信息场来感知最佳候选摄像姿态下的稀疏视角，并将3D高斯压缩为平面高斯以帮助准确估计法线和深度。最终通过深度平滑正则化和少量监督的扩散优化平面高斯。此外，还引入了每个高斯基础部分分割概率的估计和更新。
### Conclusion
广泛的实验证明，本文的方法在合成和真实数据中都取得了比现有方法更高的部分级表面重建保真度。代码将公开提供。
## 341. `cs.CV` - 轻量级遥感图像实时检测器 [PDF](https://arxiv.org/pdf/2511.17147), [HTML](https://arxiv.org/abs/2511.17147)
### Authors
Qianyi Wang,Guoqiang Ren
### Background
遥感图像在多个领域中有着广泛应用，但实时检测尤其是对小目标的检测仍然具有挑战性，主要由于小目标普遍存在以及需要在准确性和效率之间取得平衡。
### Innovation
提出了DMG-YOLO，一种针对遥感图像中小目标检测的轻量化实时检测器。通过设计双分支特征提取模块（DFE）来分割特征图并使用深度可分离卷积提取局部特征、使用带有门控机制的视觉变换器捕获全局上下文；通过多尺度特征融合模块（MFF）结合空洞卷积以增强多尺度特征融合同时保持细节；在颈部引入全局和局部聚合特征金字塔网络（GLAFPN）以进一步提升小目标检测性能。
### Conclusion
在VisDrone2019和NWPU VHR-10数据集上的广泛实验表明，DMG-YOLO在mAP、模型大小及其他关键指标上具有竞争力的表现。
## 342. `cs.CV` - 视觉情感差距的桥梁：来自嘈杂图像-文本配对的学习 [PDF](https://arxiv.org/pdf/2511.17103), [HTML](https://arxiv.org/abs/2511.17103)
### Authors
Daiqing Wu,Dongbao Yang,Yu Zhou,Can Ma
### Background
视觉情感识别（VER）是一个历史悠久的领域，随着深度神经网络的进步而受到越来越多的关注。尽管最近的研究通过利用预训练视觉模型中的嵌入知识取得了显著的进步，但在事实级特征与情感类别之间缺乏直接关联（称为“情感差距”）限制了预训练知识在VER任务中的应用。相比之下，文本模式中显式的表情和高信息密度消除了“情感差距”。因此，我们提出从预训练文本模型中借用知识，以增强预训练视觉模型的情感感知。我们专注于社会媒体数据中的图像与文本之间的事实和情感联系，提出了分割自适应对比学习（PACL）来利用这些联系。
### Innovation
我们提出了分割自适应对比学习（PACL），通过分离不同类型的样本，并为每种类型设计不同的对比学习策略。通过动态构建正负配对，我们充分利用了嘈杂样本的潜力。研究表明，跨越“情感差距”在各种预训练视觉模型在下游情感相关任务上的性能得到了显著提高。
### Conclusion
我们的研究证明，跨越“情感差距”显著提高了各种预训练视觉模型在下游情感相关任务上的性能。我们的代码已发布于这里 https://github.com/...
## 343. `cs.CV` - UI-Styler: 使用冻结黑盒推理网络进行跨设备诊断的类意识超声图像样式转移 [PDF](https://arxiv.org/pdf/2511.17155), [HTML](https://arxiv.org/abs/2511.17155)
### Authors
Nhat-Tuong Do-Tran,Ngoc-Hoang-Lam Le,Ching-Chun Huang
### Background
超声图像在不同采集设备间的显示方式有所差异，造成域移位。这会导致重新使用的固态黑盒下游推理模型性能下降。现有未配对图像转换（UIT）方法为了克服域移位问题进行了尝试，但往往忽视了类特定语义对齐，致使内容类映射不准确，影响诊断准确性。
### Innovation
UI-Styler 是一种专门针对超声波图像设计的类意识图像样式转移框架。该框架通过模式匹配机制将目标图像中的纹理模式转移到源图像上，同时保留源图像的结构内容。此外，引入了由目标域伪标签指导的类意识提示策略，以强化语义对齐，确保与诊断类别的一致性。
### Conclusion
实验结果表明，UI-Styler 在跨设备Task的图像域转换任务中表现优异，优于现有UIT方法。UI-Styler 在分布距离和分类、分割等下游任务中都达到了最先进的性能。
## 344. `cs.CV` - DiffRefiner：通过语义交互的粗细粒度轨迹规划 [PDF](https://arxiv.org/pdf/2511.17150), [HTML](https://arxiv.org/abs/2511.17150)
### Authors
Liuhan Yin,Runkun Ju,Guodong Guo,Erkang Cheng
### Background
传统的自主驾驶预测方法着重于预测固定数量的ego车辆候选轨迹，而生成方法，如扩散模型，则学习未来运动的基本分布，能够提供更具弹性的轨迹预测。然而，这些方法通常依赖于降噪的人工轨迹锚点或随机噪声，因此存在改进的空间。
### Innovation
本文提出了一种新颖的两阶段轨迹预测框架DiffRefiner。第一阶段采用基于变压器的Proposal Decoder通过回归传感器输入和预定义的轨迹锚点生成粗略的轨迹预测。第二阶段应用扩散精化器，通过迭代降噪和细化初始预测。这种方法通过包括一个区分性的轨迹提案模块增强了基于扩散的规划性能，该模块为生成精化过程提供了有力的指导。此外，设计了细粒度的降噪解码器以增强场景一致性，从而实现更准确的轨迹预测。
### Conclusion
DiffRefiner实现了最先进的性能，在NAVSIM v2中达到87.4 EPDMS，在Bench2Drive中达到87.1 DS和71.4 SR，从而在公共基准测试中创造了新纪录。消融研究验证了每个组件的有效性。
## 345. `cs.CV` - 研究自我监督表示在音频视觉伪造检测中的应用 [PDF](https://arxiv.org/pdf/2511.17181), [HTML](https://arxiv.org/abs/2511.17181)
### Authors
Dragos-Alexandru Boldisor,Stefan Smeu,Dan Oneata,Elisabeta Oneata
### Background
自我监督表示已在视觉和语音任务中表现出色，但它们在音频-视觉伪造检测领域的潜力尚未被充分探索。以往的研究要么单独使用这些特征，要么将它们嵌入复杂的架构中，而该研究通过跨模态（音频、视频、多种模态）和领域（嘴唇动作、通用视觉内容）系统性地评估了这些特征。
### Innovation
该研究首次系统性地评估了自我监督表示在音频-视觉伪造检测中的应用。研究团队评估了三个维度：检测效果、编码信息的解释性和跨模态补充性。研究发现了大多数自我监督表示能够捕获与伪造相关的信息，并且这些信息是互补的。此外，模型主要关注语义上有意义的区域而不是虚假的特征。
### Conclusion
尽管自我监督表示能够学习有意义的模式，但在不同数据集上实现稳健的跨领域性能仍然具有挑战性。研究结果揭示了自我监督表示在伪造检测中存在的机遇和基本挑战：它们确实学习到有意义的模式，但跨数据集的可靠性仍难以实现，这可能源于数据集的特征而非特征本身对表面模式的粘附。
## 346. `cs.CV` - PostCam：通过查询共享交叉注意力实现可操控视角的新型视频生成 [PDF](https://arxiv.org/pdf/2511.17185), [HTML](https://arxiv.org/abs/2511.17185)
### Authors
Yipeng Chen,Zhichao Ye,Zhenzhou Fang,Xinyu Chen,Xiaoyu Zhang,Jialing Liu,Nan Wang,Haomin Liu,Guofeng Zhang
### Background
现有的视频重新捕捉方法在相机运动注入策略方面存在不足，这不仅限制了相机控制的精确度，还导致生成的视频无法保留源视频中的细微视觉细节。
### Innovation
PostCam引入了一个查询共享交叉注意力模块，它可以整合六自由度的相机姿态和2D渲染的视频帧两种不同的控制信号，并将其统一到共享特征空间中，以提取潜在的运动线索，从而提高控制精度和生成质量。此外，PostCam采用两阶段训练策略，先从姿态输入中学习粗略的相机控制，然后结合视觉信息以提高运动的准确性并增强视觉保真度。
### Conclusion
PostCam在相机控制精度和视图一致性方面优于最先进的方法20%以上，同时实现了最高的视频生成质量。我们的项目网页可在此公共访问：this https URL
## 347. `cs.CV` - 远离普朗克轨迹：使用二维色度改善在机颜色 [PDF](https://arxiv.org/pdf/2511.17133), [HTML](https://arxiv.org/abs/2511.17133)
### Authors
SaiKiran Tedla,Joshua E. Little,Hakki Can Karaimer,Michael S. Brown
### Background
传统的相机内色度映射依赖于相关色温(CCT)在普朗克轨迹上的插值，这些插值是针对如CIE A和D65这样的普朗克光源进行预校准的。然而，现代照明技术如LED可能会显著偏离普朗克轨迹，这揭示了依赖一维CCT进行照明表征的局限性。研究表明，从一维CCT过渡到二维色度空间可以提高各种色度映射方法的准确性。此外，本文提出了一种轻量级的多层感知器(MLP)，利用二维色度特征在非普朗克光线下的鲁棒色度映射，校准过程包括使用代表性的LED光源的lightbox校准程序。
### Innovation
本文提出了从一维CCT到二维色度空间的过渡，改进了色度映射的准确性。此外，使用轻量级多层感知器(MLP)来替代传统的CCT插值，提高了在非普朗克光线下的鲁棒性，减少了LED照明场景下的角度再现误差，并支持实时在机部署。
### Conclusion
我们的方法相比传统方法减少了22%的LED照明场景下的角度再现误差，并且兼容传统的光源，能够处理多光源场景，同时实现近似实时的相机内部署，且不会增加额外的计算成本。
## 348. `cs.CV` - 学习更加细致：用于小脑部病变分割的新实例损失函数 [PDF](https://arxiv.org/pdf/2511.17146), [HTML](https://arxiv.org/abs/2511.17146)
### Authors
Luc Bouteille,Alexander Jaus,Jens Kleesiek,Rainer Stiefelhagen,Lukas Heine
### Background
传统的在医学图像分割中使用的损失函数，如Dice，往往在分割较小病灶时表现不佳，因为它们相对较小的体积对整体损失的贡献忽略不计。为解决这一问题，提出了基于实例的损失函数和指标来在单个病灶级别评估分割质量。已有研究提出了一种基于个体样本的损失函数（实例损失）和评价指标，用于更精细的病灶分割。
### Innovation
本文提出了一种名为CC-DiceCE的新损失函数，基于CC-Metrics框架。通过将其与已有的blob loss进行比较，两种损失函数均在nnU-Net框架下与DiceCE基线进行基准测试，提供了一个稳健且标准化的环境。结果显示，尽管CC-DiceCE增加了假阳性，但其在召回率上的提升几乎是无损的。
### Conclusion
多数据集实验表明，CC-DiceCE比blob loss在小脑部病变分割中表现更优。
## 349. `cs.CV` - 在黑暗中导航：夜间交通标志识别的多模态框架和数据集 [PDF](https://arxiv.org/pdf/2511.17183), [HTML](https://arxiv.org/abs/2511.17183)
### Authors
Aditya Mishra,Akshay Agarwal,Haroon Lone
### Background
交通标志对于道路安全和智能交通系统至关重要，能够实现导航和自动驾驶。然而，在夜间识别交通标志存在挑战，因为存在视觉噪声，且缺乏公共夜间数据集。尽管视觉架构有了进步，现有的方法在低光照条件下缺乏鲁棒性，无法有效利用多模态互补线索。
### Innovation
本文提出了INTSD，一个大规模的数据集，包含印度不同地区街道级别的夜间交通标志图像，涵盖了41类交通标志，在不同照明和天气条件下采集。此外，还提出了一种称为LENS-Net的多模态框架，该框架结合了自适应图像增强检测器进行联合照明校正和标志定位，并采用跨模态注意和基于图的推理的结构化多模态CLIP-GCNN分类器，以实现鲁棒且语义一致的识别。
### Conclusion
该方法超越了现有框架，消融研究证实了其关键组件的有效性。数据集和LENS-Net的代码已公开可用以便进行研究。
## 350. `cs.CV` - 扩展自监督和跨模态预训练以构建3D CT变压器 [PDF](https://arxiv.org/pdf/2511.17209), [HTML](https://arxiv.org/abs/2511.17209)
### Authors
Cris Claessens,Christiaan Viviers,Giacomo D'Amicantonio,Egor Bondarev,Fons van der Sommen
### Background
本研究介绍了SPECTRE，一种基于完全变压器的基础模型用于体积计算机断层扫描(CT)。CT扫描在医学成像中具有独特挑战，如极端的标记数量、几何异质性和临床监督不足等问题，使得现有的标准变压器和对比性学习方法无法直接应用。当前的研究旨在通过自监督和跨模态预训练来学习通用的CT表示，解决这些独特的挑战。
### Innovation
提出了SPECTRE，一种自监督和跨模态预训练框架，利用可扩展的3D视觉变压器架构和现代自监督及视觉-语言预训练策略，来学习通用的CT表示。该框架通过联合优化局部变压器实现高分辨率体积特征提取，以及全局变压器实现整个扫描的语境建模，使得大规模的3D注意力计算变得可行。SPECTRE仅使用公开可用的CT数据集进行训练，证明了无需依赖私有数据即可实现高性能、可泛化的表示。预训练结合了DINO风格的自我蒸馏和SigLIP基于的视觉-语言对齐，产生既几何一致又临床有意义的特征。
### Conclusion
SPECTRE在多个CT基准上展示了在零样本和微调设置下均优于先前的CT基础模型，确立了SPECTRE作为一种可扩展、开放且基于完全变压器的基础模型在3D医学成像中的地位。
## 351. `cs.CV` - FireScope：具有因果推理的野火风险预测 [PDF](https://arxiv.org/pdf/2511.17171), [HTML](https://arxiv.org/abs/2511.17171)
### Authors
Mario Markov(1),Stefan Maria Ailuro(1),Luc Van Gool(1),Konrad Schindler(2),Danda Pani Paudel(1 and 2) ((1) INSAIT, Sofia University, (2) ETH Zurich)
### Background
野火风险预测是一个推理密集型的空间问题，涉及整合视觉、气候和地理因素以推断连续的风险地图。现有的方法在因果推理和多模态理解方面存在不足，影响了其可靠的一般化能力。
### Innovation
论文提出了名为FireScope-Bench的大规模数据集和基准框架，结合了Sentinel-2成像和气候数据，以及美国专家定义的风险栅格和欧洲的野火事件，用于横跨大陆的评估。基于该数据集，提出了FireScope，一个基于VLM的推理指导生成框架，结合强化学习和视觉监督学习来预测风险栅格，并且具有互补的推理痕迹。FireScope在经过美国训练后，在欧洲测试时表现出显著的性能提升，专家反馈和自动分析确认了其推理痕迹的真实性和语义意义。研究结果表明，推理能够为栅格预测模型奠定基础，提升模型的泛化能力和可解释性。这是首次通过语言推理提高视觉生成任务的泛化能力的框架，提出了一个跨大陆应用的高分辨率野火风险模型，并且能够系统研究多模态火灾风险模型的横跨大陆泛化。
### Conclusion
研究发现表示推理能引导栅格预测模型，提高其泛化能力和可解释性。FireScope-Bench有望成为推动因果推理驱动、可解释和泛化空间建模的基础。
## 352. `cs.CV` - CA-SAM：在连续学习中重新思考医疗图像分割的基础模型 [PDF](https://arxiv.org/pdf/2511.17201), [HTML](https://arxiv.org/abs/2511.17201)
### Authors
Jiayi Wang,Wei Dai,Haoyu Wang,Sihan Yang,Haixia Bi,Jian Sun
### Background
在医学图像分割中，不同机构之间异构的隐私政策通常使在汇总数据集上进行联合训练变得不可行，这激发了从数据流中进行持续图像分割学习的需求，以避免灾难性遗忘。尽管Segment Anything Model (SAM)提供了强大的零样本先验，并被广泛用于下游任务的微调，其庞大的参数量和计算开销对其实际部署构成挑战。为了平衡SAM的计算效率和性能，本文展示了一种轻量级、即插即用的Alignment Layer模块，它可以高效地使SAM适应特定的医学图像，从而提高准确性并减少计算量。
### Innovation
本文提出了CA-SAM（Continual Alignment for SAM），这是一种持续学习策略，通过自动适应适量的Alignment Layer来缓解灾难性遗忘问题，同时利用SAM的零样本先验保持对未见过的医学数据集的强大性能。实验结果表明，CA-SAM在九个医学分割数据集下的持续学习场景中达到了最先进的性能。
### Conclusion
CA-SAM在持续学习场景下的九个医学分割数据集上实现了最先进的性能。我们将在[该网址]发布代码、模型和数据集。
## 353. `cs.CV` - VLA-4D: 将4D意识融入视觉-语言-动作模型以实现时空连贯的机器人操作 [PDF](https://arxiv.org/pdf/2511.17199), [HTML](https://arxiv.org/abs/2511.17199)
### Authors
Hanyu Zhou,Chuanhao Ma,Gim Hee Lee
### Background
视觉-语言-动作（VLA）模型在通用机器人任务中显示出潜力，但依旧面临在时空连贯操作中的挑战，特别是在精细的空间表示上的不足。现有的方法通常将3D位置嵌入到视觉表示中以提升动作的空间精度，但难以实现动作执行过程中的时间连贯控制。
### Innovation
提出了VLA-4D，一种配备4D意识的一般性VLA模型，以实现时空连贯的机器人操作。该模型的设计核心包括：1) 4D感知的视觉表示，提取视觉特征，并通过时间轴的1D嵌入到3D位置进行4D嵌入，同时通过交叉注意力机制将其综合为统一的视觉表示；2) 时空动作表示，扩展传统的空间动作表示以包含时间信息，使动作规划更加时空连贯，并使多模态表示对齐到LLM进行时空动作预测。
### Conclusion
通过在统一框架中设计的视觉和动作表示，机器人操作得以变得空间平滑且时间连贯。此外，扩展了含有时间动作注释的VLA数据集以微调模型。广泛实验进一步验证了该方法在不同机器人操作任务中的优越性。
## 354. `cs.CV` - 双域适配网络在现实图像超分辨率中的应用 [PDF](https://arxiv.org/pdf/2511.17217), [HTML](https://arxiv.org/abs/2511.17217)
### Authors
Chaowei Fang,Bolin Fu,De Cheng,Lechao Cheng,Guanbin Li
### Background
现实世界中的低分辨率（LR）图像超分辨率（SR）转换为高分辨率（HR）图像，处理比合成SR任务更复杂的降级模式。这对于监视、医学成像和消费电子产品等应用场景至关重要。然而，当前的方法难以应对有限的实际低分辨率-高分辨率（LR-HR）数据，影响了基本图像特征的学习。预训练的SR模型来自大规模合成数据集，可以提供有价值的前提知识，从而提高泛化能力，加速训练过程，并减少在现实SR任务中对外部数据的需求。
### Innovation
本文提出了一种新的方法，双域适配网络，能够高效地将预训练的图像SR模型从模拟数据集适配到实际数据集。为此，首先通过选择性更新预训练模型的参数和使用低秩适配技术调整冻结参数，设置了空间域适配策略。进一步，将频域适配分支整合到适配模型中，结合输入的频谱数据和空间域骨干的中间特征来推断HR频谱图，进一步提高超分辨率结果。
### Conclusion
在公共现实图像SR基准测试（包括RealSR、D2CRealSR和DRealSR）上的实验评估表明，提出的方法在现有最先进的模型中表现更优。代码可在以下链接获取：this https URL.
## 355. `cs.CV` - SING3R-SLAM: 基于子地图的室内单目高斯SLAM与3D重建先验 [PDF](https://arxiv.org/pdf/2511.17207), [HTML](https://arxiv.org/abs/2511.17207)
### Authors
Kunyi Li,Michael Niemeyer,Sen Wang,Stefano Gasperini,Nassir Navab,Federico Tombari
### Background
近年来，密集三维重建技术的进步使得局部几何形状的准确捕捉成为可能；然而，将这些技术集成到SLAM中具有挑战性，主要是因为位移误差和冗余的点云地图，这限制了效率并影响了下游任务，如新视角合成。
### Innovation
本文提出了一种全局一致且紧凑的基于高斯的密集RGB SLAM框架——SING3R-SLAM。该框架通过结合局部一致的三维重建与统一的全局高斯表示，共同细化场景几何和相机姿态，从而实现多下游应用的高效和多功能3D映射。SING3R-SLAM首先通过轻量级的跟踪和重建模块建立局部一致的子地图，然后将它们逐步对齐和融合到一个全局高斯地图中，从而保证跨视角几何一致性。全局地图提供了反馈，用于纠正局部漂移并增强跟踪的鲁棒性。
### Conclusion
广泛的实验表明，SING3R-SLAM在跟踪、三维重建和新视角渲染方面达到了最先进的性能。与现有方法相比，SING3R-SLAM在跟踪上提高了超过12%，同时生成了更精细和更详细的几何形状，保持了高效紧凑的全局表示，适用于真实数据集。
## 356. `cs.CV` - FisheyeGaussianLift: 周视鱼眼相机感知的BEV特征提升 [PDF](https://arxiv.org/pdf/2511.17210), [HTML](https://arxiv.org/abs/2511.17210)
### Authors
Shubham Sonarghare,Prasad Deshpande,Ciaran Hogan,Deepika-Rani Kaliappan-Mahalingam,Ganesh Sistu
### Background
由于鱼眼图像固有的极端非线性失真、遮挡和深度不确定性，准确的地平线鸟瞰图（BEV）语义分割仍然是一个挑战。
### Innovation
本文提出了一个aware度失真的BEV分割框架，直接处理多摄像头高分辨率鱼眼图像，利用校准的几何反投影和每个像素的深度分布估计。每个图像像素通过高斯参数化被提升到三维空间，预测空间均值和各向异性协方差来显式建模几何不确定性。通过可微分绘制将投影的3D高斯融合成BEV表示，从而生成连续的、具有不确定性意识的语义图，无需进行去畸变或透视矫正。
### Conclusion
在复杂停车和城市驾驶场景下的大量实验表明，该方法在可行驶区域实现了87.75%的IoU得分，并在严重鱼眼失真和多种环境条件下，车辆的分割性能为57.26%。
## 357. `cs.CV` - 现实噪声解耦的高光谱图像去噪 [PDF](https://arxiv.org/pdf/2511.17196), [HTML](https://arxiv.org/abs/2511.17196)
### Authors
Yingkai Zhang,Tao Zhang,Jing Nie,Ying Fu
### Background
高光谱图像（HSI）去噪是提高HSI质量的关键步骤。噪声建模方法可以拟合噪声分布来生成合成HSI用于训练降噪网络。然而，捕捉到的HSI中的噪声通常非常复杂，难以准确建模，这极大地限制了这些方法的有效性。
### Innovation
本文提出了一种多阶段噪声解耦框架，将复杂的噪声分解为显式建模和隐式建模的组件。这种方法降低了噪声的复杂性并增强了在实际配对数据上应用HSI去噪方法的可学习性。具体来说，对于显式建模的噪声，利用现有的噪声模型生成配对数据进行预训练的降噪网络，使其能够有效地处理显式建模的噪声。对于隐式建模的噪声，引入了一个由高频小波引导的网络，该网络利用预训练模块的先验知识，适配性地提取高频率特征以针对性地从实际配对HSI中去除隐式建模的噪声。此外，为了有效地消除所有噪声成分并减少各阶段误差累积，采用了一种多阶段学习策略，包括独立预训练和联合微调，以优化整个框架。
### Conclusion
在公共和我们捕获的数据集上的广泛实验表明，我们提出的框架在去噪方面超过了现有的最先进方法，有效处理了复杂的现实世界噪声，显著提高了HSI质量。
## 358. `cs.CV` - QueryOcc: 基于查询的自监督3D语义占用学习 [PDF](https://arxiv.org/pdf/2511.17221), [HTML](https://arxiv.org/abs/2511.17221)
### Authors
Adam Lilja,Ji Lan,Junsheng Fu,Lars Hammarstrand
### Background
在计算机视觉领域，从图像中学习3D场景几何和语义是一大挑战，对于自动驾驶技术来说是一项关键能力。由于大规模的3D标注成本高昂，现有的方法转向直接从传感器数据中进行自监督学习，而无需人工标签。现有的方法要么依赖于2D渲染一致性，使得3D结构只能隐式产生，要么使用从累积激光雷达点云生成的离散体素网格，限制了空间精度和可扩展性。
### Innovation
本文提出了QueryOcc，一种基于查询的自监督框架，直接通过在相邻帧之间采样的独立4D时空查询来学习连续的3D语义占用。该框架可以从来自视觉基础模型推导出的伪点云或原始激光雷达数据中接受监督。为了在常量内存下进行长距离的监督和推理，引入了一种压缩场景表示方法，该方法保留近场细节的同时平滑压缩远场区域。QueryOcc在自我监督Occ3D-nuScenes基准测试中，相对于基于摄像头的方法，在语义RayIoU上提高了26%，运行速度为11.6 FPS，证明了直接4D查询监督可以实现强大的自监督占用学习。
### Conclusion
QueryOcc架构通过基于查询的自监督学习直接从图像中获取连续的3D语义占用信息，显著提高了精度，并且能够以更高的效率处理大规模数据集，展示了其在自动驾驶等领域的应用潜力。
## 359. `cs.CV` - Equivariant-Aware Structured Pruning for Efficient Edge Deployment: A Comprehensive Framework with Adaptive Fine-Tuning [PDF](https://arxiv.org/pdf/2511.17242), [HTML](https://arxiv.org/abs/2511.17242)
### Authors
Mohammed Alnemari
### Background
该论文提出了一个结合了组同构卷积神经网络（G-CNNs）与同构意识结构化剪枝的新框架，旨在为资源受限的环境生产紧凑且转换不变的模型。这种通过C4循环群实现旋转同构的方法，在几何变换下保持了一致的表现能力，同时减轻了计算开销。该方法通过分析e2cnn层结构并进行神经元级别的剪枝来保持同构特性，并通过自适应微调机制来防止准确率下降，该机制在准确率下降超过2%时自动触发，从而实现高效的恢复。
### Innovation
该框架创新之处在于结合了G-CNNs和同构意识结构化剪枝，并通过C4循环群实现了旋转同构。在剪枝过程中保留了同构特性，并设计了自适应微调机制以防止准确率下降。此外，该框架还包括动态INT8量化和全面的流水线，涵盖了训练、知识蒸馏、结构化剪枝、自适应微调和量化。
### Conclusion
实验结果表明，该方法在卫星图像（EuroSAT）和标准基准（CIFAR-10、旋转MNIST）上取得了29.3%的参数减少，且显著恢复了准确性，证明了同构网络结构化剪枝可以实现显著压缩且保留几何稳健性。该流水线提供了一个可再现的框架，用于优化同构模型，填补了群论网络设计与实际部署约束之间的差距，特别是在卫星图像分析和几何视觉任务方面。
## 360. `cs.CV` - MolSight: 使用 SMILES 预训练、多粒度学习和强化学习的光学化学结构识别 [PDF](https://arxiv.org/pdf/2511.17300), [HTML](https://arxiv.org/abs/2511.17300)
### Authors
Wenrui Zhang,Xinggang Wang,Bin Feng,Wenyu Liu
### Background
光学化学结构识别（OCSR）在现代化学信息学中起着关键作用，它能够自动将科学文献、专利和教育材料中的化学结构图像转换为机器可读的分子表示。这一能力对于大规模化学数据挖掘、药物发现管道以及相关领域的大型语言模型（LLM）应用至关重要。然而，现有的OCSR系统在准确识别立体化学信息方面面临巨大挑战，因为立体异构体之间的区别微妙，如楔形键和_dash键、环构型和空间排列等。
### Innovation
为了应对这些挑战，本文提出了一个名为MolSight的全面学习框架，该框架采用三阶段训练范式：首先，在大规模但噪声较大的数据集上进行预训练，赋予模型基本的化学结构图像感知能力；其次，使用具有更丰富监督信号的数据集进行多粒度微调，系统地探索特定辅助任务（如化学键分类和原子定位）对分子式识别的贡献；最后，采用强化学习进行后训练优化，并引入新的立体化学结构数据集。通过一系列实验，MolSight在（立体）化学光学结构识别方面表现出领先性能。
### Conclusion
通过在多种数据集上的广泛实验，我们发现MolSight在光学化学结构识别方面达到了领先水平，即使参数量相对较小，GRPO算法也能显著增强模型在立体分子上的性能。
## 361. `cs.CV` - NoPe-NeRF++: 无需姿态先验的NeRF局部到全局优化 [PDF](https://arxiv.org/pdf/2511.17322), [HTML](https://arxiv.org/abs/2511.17322)
### Authors
Dongbo Shi,Shen Cao,Bojian Wu,Jinhui Guo,Lubin Fan,Renjie Chen,Ligang Liu,Jieping Ye
### Background
现有方法，尤其是NoPe-NeRF，专注于图像内的局部关系，但在复杂场景中往往无法准确恢复摄像头姿态。为解决此问题，论文提出了一种新颖的局部到全局优化算法NoPe-NeRF++，该算法在不依赖姿态先验的情况下训练NeRF。通过初始化相对姿态并进行局部联合优化以增强姿态估计，并引入全局优化阶段以通过束调整结合几何一致性约束，进一步细化姿态并提升NeRF的整体质量。
### Innovation
1. 提出了NoPe-NeRF++，一种无需姿态先验的局部到全局优化算法，用于训练NeRF。2. 通过相对姿态初始化和局部联合优化增强姿态估计。3. 引入全局优化阶段通过束调整结合几何一致性约束，进一步细化姿态。4. 是第一个将局部和全局线索无缝结合到NeRF的方法，优于最新的技术水平，在姿态估计精度和新颖视图合成方面表现出色。
### Conclusion
广泛的基准数据集评估表明，NoPe-NeRF++在姿态估计精度和新颖视图合成方面表现出优越性能和鲁棒性，尤其在复杂场景中也能够验证其设计选择的有效性。
## 362. `cs.CV` - 使用归一化四元数内核进行彩色图像盲去模糊 [PDF](https://arxiv.org/pdf/2511.17253), [HTML](https://arxiv.org/abs/2511.17253)
### Authors
Yuming Yang,Michael K. Ng,Zhigang Jia,Wei Wang
### Background
盲去模糊问题对于彩色图像来说是一个具有挑战性的问题。现有的方法通常将彩色图像转换为灰度或分别处理每个颜色通道，这忽视了颜色通道之间的关系。对于这一问题，本文提出了一个新颖的四元数保真度项，专为彩色图像盲去模糊设计，能更准确地捕捉彩色图像间的复杂关系。
### Innovation
本文创新性地引入了一个四元数保真度项，该保真度项基于四元数卷积内核的特性，包含一个非负卷积内核捕捉整体模糊，以及三个对应红、绿、蓝通道的无约束卷积内核，用于建模这些未知的相互依赖关系。为了保持图像强度，提出在盲去模糊过程中使用归一化的四元数内核。
### Conclusion
在实际模糊彩色图像数据集上进行的大量实验表明，本文提出的方法能有效地去除伪影，显著提高去模糊效果，展示了其作为彩色图像去卷积强大工具的潜力。
## 363. `cs.CV` - 文本到图像生成中的文化鸿沟：揭示文化差距 [PDF](https://arxiv.org/pdf/2511.17282), [HTML](https://arxiv.org/abs/2511.17282)
### Authors
Chuancheng Shi,Shangze Li,Shiming Guo,Simiao Xie,Wenhua Wu,Jingtong Dou,Chao Wu,Canran Xiao,Cong Wang,Zifeng Cheng,Fei Shen,Tat-Seng Chua
### Background
多语言文本到图像（T2I）模型在视觉真实感和语义对齐方面取得了快速发展，并已广泛应用。然而，不同文化背景下生成的图像质量存在差异：由于语言携带着文化内涵，因此使用多语言提示合成的图像应该保持跨语言文化一致性。
### Innovation
研究表明，当前T2I模型在使用多语言输入时，往往会生成文化中立或偏向英语结果的原因并非是因为缺乏文化知识，而是文化相关表示激活不足。为此，提出了一个探针方法，可以定位到少数几层中的一小部分对文化敏感的神经元。并据此提出两种互补的对齐策略：（1）推理时的文化激活，放大识别的神经元而不需对网络基础进行微调；（2）层级目标的文化增强，仅更新相关文化层。通过CultureBench基准测试，在保持现实性和多样性的同时，证明了这些策略的一致性改进。
### Conclusion
通过CultureBench基准测试，在不牺牲自然度和多样性的情况下，提出了文化一致性改进的策略。
## 364. `cs.CV` - BiFingerPose: Touch 设备双模态手指姿态估计 [PDF](https://arxiv.org/pdf/2511.17306), [HTML](https://arxiv.org/abs/2511.17306)
### Authors
Xiongjun Guan,Zhiyu Pan,Jianjiang Feng,Jie Zhou
### Background
手指姿态为提升触摸屏设备的人机交互能力提供了广阔的可能性。现有的手指姿态估计算法主要依赖电容成像，但仅能估计偏摆角和平角，且在处理大角度输入时精度较低（尤其是超过45度）。
### Innovation
提出了一种新的双模态手指姿态估计算法BiFingerPose，能同时准确预测全面的手指姿态信息。利用电容成像和屏幕下指纹传感器获取的指纹段输入，该方法可以可靠地估计滚转角，而单一模态无法做到这一点。此外，其他姿态参数的预测性能也显著改善。
### Conclusion
在12人的连续和离散交互任务中进行的测试表明，BiFingerPose 的预测性能提高了21%以上，任务完成效率提高了2.5倍，用户体验也提高了23%，展示了其实用的优势。最后展示了 BiFingerPose 在提升认证安全性和改善交互体验的应用场景，以及相应的原型机演示了其交互潜力。
## 365. `cs.CV` - SpatialGeo：通过几何-语义融合提高多模态LLM的空间推理能力 [PDF](https://arxiv.org/pdf/2511.17308), [HTML](https://arxiv.org/abs/2511.17308)
### Authors
Jiajie Guo,Qingpeng Zhu,Jin Zeng,Xiaolong Wu,Changyong He,Weida Wang
### Background
多模态大型语言模型（MLLMs）由于大型语言模型（LLMs）的强大推理能力，在图像和语言任务中取得了显著进展。然而，大多数MLLMs在理解和推理三维空间中的空间排列方面存在局限性。
### Innovation
本文提出了一种基于几何和语义特征分层融合的新视觉编码器，生成空间感知视觉嵌入，从而增强MLLMs的空间定位能力。具体来说，研究发现空间歧义主要源自大多数现有MLLMs（如CLIP）所使用的视觉编码器对实例级语义特征的有损嵌入。因此，研究通过在提出的SpatialGeo中加入基于视觉自监督学习的几何特征来弥补CLIP的不足，增强了空间感知性。
### Conclusion
实验结果表明，SpatialGeo在空间推理任务中提高了准确性，相较于最先进的模型在SpatialRGPT-Bench上至少提高了8.0%的准确率，同时推理过程中的内存成本降低了约50%。
## 366. `cs.CV` - 所有路径干预：不同对齐格式下统一消除LVLM幻觉的方法 [PDF](https://arxiv.org/pdf/2511.17254), [HTML](https://arxiv.org/abs/2511.17254)
### Authors
Jiaye Qian,Ge Zheng,Yuchen Zhu,Sibei Yang
### Background
尽管大型视觉语言模型（LVLMs）在广泛的任务中表现出色，但它们仍然容易产生幻觉现象。研究发现LVLMs中的幻觉并非由单一因果路径引起，而是来自图像到输入文本、图像到输出文本以及文本到文本路径之间的互动。此外，幻觉路径可能依赖于问题-答案对齐格式的不同。
### Innovation
本文提出了一种全面的干预框架，该框架与transformer在LVLM中的因果结构对齐，并整合了不同干预路径对幻觉的影响。研究首次发现，LVLMs在不同对齐格式下依赖于不同的路径。基于这些见解，本文提出了简单而有效的干预方法，针对具有区分性和生成性格式的关键幻觉头部进行识别和干预。通过跨多个基准测试证明，该方法在不同对齐类型中一致减少了幻觉。
### Conclusion
本文提出的方法在多种基准上展示了对不同对齐类型幻觉的一致减少效果。通过干预各路径的关键幻觉头部，为解决LVLM幻觉问题提供了新思路和方法。
## 367. `cs.CV` - MuM: 多视图遮蔽图像建模以实现3D视觉 [PDF](https://arxiv.org/pdf/2511.17309), [HTML](https://arxiv.org/abs/2511.17309)
### Authors
David Nordström,Johan Edstedt,Fredrik Kahl,Georg Bökman
### Background
自监督学习通过对未标记数据进行图像学习，提取有意义的视觉表示。当扩展到大规模数据集时，这种范式取得了最先进的性能，并且训练出的模型如DINOv3等被广泛采用。然而，大多数先前的努力侧重于语义理解而非几何推理。唯一的例外是Cross-View Completion（CroCo），它是一种针对3D理解的遮蔽自动编码器（MAE），本文继续CroCo的研究路径，并专注于学习针对3D视觉定制的功能。
### Innovation
本文将MAE扩展到同一场景的任意多个视图。通过均匀遮蔽所有视图并采用轻量级的帧间注意力解码器，我们的方法比CroCo更简单且更具扩展性。我们在下游任务（包括前馈重建、密集图像匹配和相对位姿估计）中全面评估了所提出模型MuM，发现它优于最先进的视觉编码器DINOv3和CroCo v2。
### Conclusion
MuM在多个3D视觉任务中表现出优越性能，特别是对于多视图遮蔽图像建模方法而言是一种简单且可扩展的改进。
## 368. `cs.CV` - 更像这一点：使用相关反馈的基于视觉语言模型的文本到图像检索 [PDF](https://arxiv.org/pdf/2511.17255), [HTML](https://arxiv.org/abs/2511.17255)
### Authors
Bulat Khaertdinov,Mirela Popa,Nava Tintarev
### Background
大型视觉语言模型（VLMs）能够使用自然语言查询实现直观的视觉搜索。然而，提高这些模型的性能通常需要进行微调并扩展到更大的模型变体。为此，我们提出了一种借鉴传统基于文本的搜索机制的方法：相关反馈，用于在推理时提高检索性能。
### Innovation
本文介绍并评估了四种针对基于视觉语言模型的检索方法的相关反馈策略。具体包括修订的伪相关反馈（PRF）、生成性相关反馈（GRF）、注意力反馈摘要器（AFS）以及使用真实图像注释模拟显式反馈。我们发现，与没有反馈的检索相比，这些方法能够在较小的视觉语言模型上提高3-5%的MRR@5性能，在更大模型上提高1-3%。特别地，注意力反馈摘要器（AFS）不仅缓解了查询漂移问题，而且在迭代多轮检索场景中比生成性相关反馈更具鲁棒性。
### Conclusion
本文的研究结果表明，相关反馈可以一致地增强视觉语言模型的检索性能，同时为交互式和自适应视觉搜索提供了可能性。
## 369. `cs.CV` - Range-Edit: Semantic Mask Guided Outdoor LiDAR Scene Editing [PDF](https://arxiv.org/pdf/2511.17269), [HTML](https://arxiv.org/abs/2511.17269)
### Authors
Suchetan G. Uppur,Hemant Kumar,Vaibhav Kumar
### Background
训练自动驾驶和导航系统需要大量且多样化的点云数据集来捕捉各种动态城市环境中的复杂边缘情况。从现实世界的点云数据中获取如此多样化的场景，特别是对于关键的边缘情况来说具有挑战性，这限制了系统的泛化能力和稳健性。当前方法依赖于在手工制作的3D虚拟环境中模拟点云数据，这需要大量时间和计算资源，且通常无法完全捕捉到真实场景的复杂性。
### Innovation
本文提出了一种新的方法，通过使用基于语义的掩模对现实世界的LiDAR扫描进行编辑，生成新的合成LiDAR点云。该方法结合了距离图像投影和语义掩模条件，实现基于扩散的过程生成。将点云转换为2D距离视图图像，作为中间表示，通过凸包基于的语义掩模进行语义编辑。这些掩模通过提供现实环境中的对象形状、方向和位置的信息来指导生成过程，确保几何一致性和逼真性。
### Conclusion
该方法在KITTI-360数据集上的验证结果表明，能够生成高质量的LiDAR点云，能够生成复杂的边缘情况和动态场景，提供了一种成本有效且可扩展的解决方案，用以生成多样化的LiDAR数据，有助于提高自动驾驶系统的稳健性。
## 370. `cs.CV` - SVRecon: 稀疏体素raster化用于表面重建 [PDF](https://arxiv.org/pdf/2511.17364), [HTML](https://arxiv.org/abs/2511.17364)
### Authors
Seunghun Oh,Jaesung Choe,Dongjae Lee,Daeun Lee,Seunghoon Jeong,Yu-Chiang Frank Wang,Jaesik Park
### Background
近年来，提出的稀疏体素稀疏体素化方法为高保真表面重建任务提供了一种新的范式。然而，与3D高斯分布相比，稀疏体素在优化过程中容易陷入局部最小值，并且保持沿独立参数化稀疏体素的平滑性是一个具有挑战性的问题。
### Innovation
本文通过使用视觉几何模型进行稳健的几何初始化，并引入空间平滑损失以促使上下级体素组和兄弟体素组之间具备一致的关系，从而提出了一种利用辐射度函数（SDF）的稀疏体素重建方法（SVRecon），有效解决了稀疏体素优化过程中的局部最小值问题，同时保持了体素间的平滑一致性。
### Conclusion
我们通过多种基准实验验证了该方法在保持高重建精度的同时，还具有快速收敛的特点。代码将开源。
## 371. `cs.CV` - ATAC: 基于增强在CLIP中的测试时对抗矫正 [PDF](https://arxiv.org/pdf/2511.17362), [HTML](https://arxiv.org/abs/2511.17362)
### Authors
Linxiang Su,András Balogh
### Background
尽管CLIP在图像-文本匹配方面取得了显著的成功，但它仍然非常容易受到图像上的对抗性扰动的影响。最近的工作探索了各种测试时间防御策略，但仍表现出有限的鲁棒性。因此，作者重新审视了该问题，并提出了一种简单而有效的方法：基于增强的测试时对抗矫正（ATAC）。ATAC直接在CLIP的嵌入空间中操作，通过计算增强引起的漂移向量来推断语义恢复方向，并基于这些潜在漂移的夹角一致性对嵌入进行校正。
### Innovation
ATAC提出了一种新的测试时对抗防御策略，直接在CLIP的嵌入空间中进行操作，通过计算增强引起的漂移向量来校正嵌入，从而显著提高了模型的鲁棒性，相比之前的最先进方法提高了约50%的鲁棒性，同时计算开销很低。此外，ATAC在非常规和极端条件下保持了最先进的鲁棒性，并且甚至对适应性攻击也具有非平凡的鲁棒性。
### Conclusion
研究表明，ATAC是一种在CLIP嵌入空间中测试时对抗防御的有效方法，在新的防御范式中展现出了高效性。
## 372. `cs.CV` - Refracting Reality: Generating Images with Realistic Transparent Objects [PDF](https://arxiv.org/pdf/2511.17340), [HTML](https://arxiv.org/abs/2511.17340)
### Authors
Yue Yin,Enze Tao,Dylan Campbell
### Background
目前的生成图像模型虽然能够生成令人信服的真实图像，包括可感知的形状、纹理、布局和照明，但在合成透明物体方面表现不佳，透明物体表现出折射、反射、吸收和散射。折射尤其具有挑战性，因为折射像素光线往往与其他图像部分中观察到的表面相交，对颜色形成约束。显而易见的是，生成模型尚未充分精炼光学定律，无法准确渲染折射物体。
### Innovation
本文讨论了在给定文本提示的情况下，生成具有准确折射的图像的问题。通过使用斯涅尔折射定律，同步物体界内的像素与界外的像素，并通过变换和合并像素实现这一目标。对于图像中未直接观察到但通过折射或反射可见的表面，通过与以物体为中心的全景图进行对齐和合并来恢复其外观。我们证明这种方法可以生成更加光学合乎现实的图像，遵守物理限制。
### Conclusion
我们的方法能够生成更多光学上合理的图像，这些图像遵守物理约束。
## 373. `cs.CV` - DSeq-JEPA: Discriminative Sequential Joint-Embedding Predictive Architecture [PDF](https://arxiv.org/pdf/2511.17354), [HTML](https://arxiv.org/abs/2511.17354)
### Authors
Xiangteng He,Shunsuke Sakai,Kun Yuan,Nicolas Padoy,Tatsuhito Hasegawa,Leonid Sigal
### Background
现有的I-JEPA架构通过预测视觉上下文中的掩码区域的潜在表示来学习视觉表示。但该架构将所有区域视为独立且均等地处理，缺乏明确的预测发生的位置或顺序的概念。
### Innovation
提出了DSeq-JEPA，一种基于区分性序列联合嵌入预测架构，它结合了JEPA风格的潜在预测和GPT风格的顺序推理，通过识别基于变压器衍生的显著性图中的主要区分区域，并按显著性顺序预测后续区域，形成从主要到次要线索的类似课程的学习过程。
### Conclusion
跨多种任务（包括图像分类（ImageNet）、细粒度视觉分类（iNaturalist21、CUB-200-2011、Stanford-Cars）、检测和分割（MS-COCO、ADE20K）和低级推理任务（Clevr/Count、Clevr/Dist））的实验表明，DSeq-JEPA能够更专注于更具区分性和可泛化的表示。
## 374. `cs.CV` - Loomis Painter: 重新构建绘画过程 [PDF](https://arxiv.org/pdf/2511.17344), [HTML](https://arxiv.org/abs/2511.17344)
### Authors
Markus Pobitzer,Chang Liu,Chenyi Zhuang,Teng Long,Bin Ren,Nicu Sebe
### Background
现有视频资源如YouTube的一步一步绘画教程虽然对于学习艺术技巧具有重要价值，但缺少互动性和个性化。而现有的生成模型虽然在艺术图像合成上取得进展，但在跨媒介应用上难以泛化，并常常出现时间或结构上的不一致，影响对人类创造性工作流程的忠实再现。
### Innovation
提出了一种统一的多媒介绘画过程生成框架，通过语义驱动风格控制机制将多种媒介整合到扩散模型条件空间中，使用跨媒介风格增强。同时采用反转绘画训练策略确保生成的平滑和接近人性。建立了一个大规模的真实绘画过程数据集，并从跨媒介一致性和时间连续性以及最终图像保真度三个方面进行评估，取得了明显成果。此外，还定量建模了创意序列，包括构图、色彩布局和细节完善，以反映人类艺术发展的过程。
### Conclusion
通过Loomis Painter框架，实现了跨媒介绘画过程的重建，提高了生成模型在跨媒介应用中的表现，同时更好地模拟了人类绘画的创造性工作流程，并通过量化指标证明了其有效性。
## 375. `cs.CV` - SuperQuadricOcc：超参数方体的多层高斯逼近用于实时自监督占用估计 [PDF](https://arxiv.org/pdf/2511.17361), [HTML](https://arxiv.org/abs/2511.17361)
### Authors
Seamie Hayes,Reenu Mohandas,Tim Brophy,Alexandre Boulch,Ganesh Sistu,Ciaran Eising
### Background
语义占用估计能够提供用于自动驾驶感知和规划的密集的空间和语义信息。尽管高斯分布在自我监督的占用估计中得到了广泛应用，但由于需要大量的高斯原语，这种方法在内存需求上存在显著增加，不适合实时推理。超参数方体由于其多样的形状集，可以在减少原语数量和降低内存需求的同时提供优势，但将其集成到自我监督的占用模型中并非易事，因为缺乏适用于此目的的超参数方体栅格化器。
### Innovation
提出了一种基于超参数方体的场景表示方法SuperQuadricOcc。该方法通过利用多层icosphere-剖分的高斯逼近超参数方体，实现了在训练期间的高斯栅格化监督。与基于高斯的方法相比，SuperQuadricOcc在Occ3D数据集上实现了75%的内存占用减少、124%的推理加速和5.9%的mIoU改进，同时无需使用时间标签。此外，这种方法使得实现实时推理并保持竞争力的表现成为可能。超参数方体的使用相对基于高斯的方法将场景建模所需的原语数量减少了84%。
### Conclusion
SuperQuadricOcc通过利用多层高斯逼近超参数方体的方法，实现了占用估计的实时推理和性能的提升。该方法在Occ3D数据集上的实验结果表明了其在内存占用、推理速度和mIoU方面的优势，同时不需要使用时间标签。此外，还提供了一个快速的超参数方体体素化模块来方便与其他方法的评估。源代码将作为开源代码发布。
## 376. `cs.CV` - 非参数概率稳健性：具有优化扰动分布的保守度量 [PDF](https://arxiv.org/pdf/2511.17380), [HTML](https://arxiv.org/abs/2511.17380)
### Authors
Zheng Wang,Yi Zhang,Siddartha Khastgir,Carsten Maple,Xingyu Zhao
### Background
尽管深度学习模型在许多任务上取得了显著的成功，它们仍然对小的输入扰动非常敏感，这些扰动可能使模型产生错误的输出。因此，最近提出概率稳健性(PR)作为对抗性稳健性(AR)的补充替代方法。然而，现有的PR形式假设扰动分布是固定且已知的，这在实践中是不现实的。
### Innovation
本文提出了一种非参数概率稳健性(NPPR)，这是一种更实用的PR指标，不需要任何预先定义的扰动分布。NPPR通过从数据中直接学习优化的扰动分布来实现保守的PR评估，在分布不确定性的条件下更加实用。此外，基于高斯混合模型（GMM）和多层感知机（MLP）帽子及双立方插值的NPPR估计器被开发，以涵盖各种输入相关和输入无关的扰动场景。
### Conclusion
理论分析建立了AR，PR和NPPR之间的关系。在CIFAR-10、CIFAR-100和Tiny ImageNet数据集上进行了广泛的实验，验证了NPPR作为一个更实用的稳健性度量，相对于假设那些在最先进的模型中常用的扰动分布，NPPR提供了高达40%更保守（较低）的PR估计。
## 377. `cs.CV` - 设计用于面部验证任务的多样化和公平性面部图像数据集 [PDF](https://arxiv.org/pdf/2511.17393), [HTML](https://arxiv.org/abs/2511.17393)
### Authors
Georgia Baltsou,Ioannis Sarridis,Christos Koutlis,Symeon Papadopoulos
### Background
面部验证是各种应用（包括在线银行和个性化设备的安全访问）中的身份认证的重要组成部分。现有的面部图像数据集往往存在种族、性别和其他人口统计特征等方面的显著偏差，限制了面部验证系统的有效性和公平性。
### Innovation
提出了一种全面的方法，结合先进的生成模型来创建多样性和高质量的合成面部图像。该方法侧重于面部特征的多样表示，确保符合身份卡照片的要求。同时，引入了Diverse and Inclusive Faces for Verification (DIF-V)数据集，包含27,780张926个不同身份的图像，作为面部验证未来研究的基准。分析显示现有验证模型对某些性别和种族存在偏见，并且身份风格修改会负面影响模型性能。
### Conclusion
通过解决现有数据集中固有的不平等性，此工作不仅丰富了人工智能中多样性和伦理性的讨论，也为开发更具包容性和可靠性的面部验证技术奠定了基础。
## 378. `cs.CV` - MorphSeek：细粒度潜在表示级策略优化在变形图像配准中的应用 [PDF](https://arxiv.org/pdf/2511.17392), [HTML](https://arxiv.org/abs/2511.17392)
### Authors
Runxun Zhang,Yizhou Liu,Li Dongrui,Bo XU,Jingwei Wei
### Background
变形图像配准（DIR）在医学图像分析中是一个基础但极具挑战性的问题，主要是由于密集位移场的高维形变空间以及像素级监督的稀缺。现有的强化学习框架通常将这个空间投影为粗略的低维表示，限制了它们捕捉空间变异形变的能力。
### Innovation
我们提出了MorphSeek，一种细粒度的表示级策略优化范式，将DIR重新表述为潜在特征空间中的连续优化过程。MorphSeek在编码器上方引入了一个随机高斯策略头部，以建模潜在特征的分布，促进高效的探索和粗细联合精炼。该框架通过组相对策略优化，结合无监督预热和弱监督微调，多轨迹采样稳定了训练并提高了标签效率。
### Conclusion
在三个3D配准基准测试（OASIS脑MRI、LiTS肝脏CT和腹部MR-CT）中，MorphSeek在与强大基线相比时，实现了持续的Dice分数改进，同时保持高标签效率，具有最少的参数成本和低步骤级延迟开销。MorphSeek超越了优化器的具体细节，提出了一个空间连续且高效的数据优化变形，提供了一种原理性的、骨架无关的和优化器无关的解决方案，以在高维设置中进行可扩展的视觉对齐。
## 379. `cs.CV` - 通过专家教师的中间层知识蒸馏预防医学影像分析中的捷径学习 [PDF](https://arxiv.org/pdf/2511.17421), [HTML](https://arxiv.org/abs/2511.17421)
### Authors
Christopher Boland,Sotirios Tsaftaris,Sonia Dahdouh
### Background
深度学习模型倾向于通过训练数据中的虚假相关且无关特征来学习问题的捷径解决方案。在医疗图像分析等高风险应用中，这种现象可能导致模型在预测时无法使用临床意义的特征，从而导致模型缺乏鲁棒性并可能对患者造成伤害。
### Innovation
本文提出了一个新颖的知识蒸馏框架，利用一个专门对任务相关数据进行微调的小型教师网络，来减轻在大型带偏见特征数据集上训练的学生网络中的捷径学习。该框架通过直接针对中间层进行干预，有效地应对了不同类型的捷径（扩散和局部化）在不同网络层中的表现。
### Conclusion
在CheXpert、ISIC 2017和SimBA数据集上进行的广泛实验表明，该方法在各种架构（ResNet-18、AlexNet、DenseNet-121、3D CNNs）上都取得了超越传统经验风险最小化、基于增广的偏见缓解和基于群体的偏见缓解方法的表现。在许多情况下，这种方法即使在测试数据为出分布数据的情况下，也能获得与训练无偏数据基础模型相当的表现。这些结果展示了该方法在实际医疗成像场景中的实用价值，尤其是在偏见注释有限且捷径特征难以预先识别的情况下。
## 380. `cs.CV` - 稳定可逆图卷积网络在标签效率骨架动作识别中的应用 [PDF](https://arxiv.org/pdf/2511.17345), [HTML](https://arxiv.org/abs/2511.17345)
### Authors
Hichem Sahbi
### Background
图像处理领域中的骨架动作识别是一个热点研究方向。这个任务的关键挑战在于依赖于大量的手工标注数据集，但这些数据集的获取成本高昂且耗时。该论文提出了一种新颖的标签效率方法，利用图卷积网络（GCNs）进行骨架动作识别。
### Innovation
该方法通过学习一种新颖的信息收集函数，即最优目标函数的混合，涵盖了数据的代表性、多样性和不确定性。此外，该方法通过学习数据中最有信息的子集，利用可逆GCN将数据从样本空间映射到潜在空间，在该空间中更容易捕捉到数据的固有分布。
### Conclusion
在两个挑战性的骨架动作识别数据集上进行了广泛的实验，表明所提出的标签节约GCNs方法相较于相关工作更有效且表现优异。”}
## 381. `cs.CV` - MMT-ARD: 多模态多教师对抗蒸馏以增强稳健的视觉语言模型 [PDF](https://arxiv.org/pdf/2511.17448), [HTML](https://arxiv.org/abs/2511.17448)
### Authors
Yuqi Li,Junhao Dong,Chuanguang Yang,Shiping Wen,Piotr Koniusz,Tingwen Huang,Yingli Tian,Yew-Soon Ong
### Background
视觉语言模型（VLMs）在安全关键应用中的应用越来越广泛，这使得它们的对抗鲁棒性成为一个重要的关注点。传统的单教师对抗知识蒸馏方法在知识多样性、收敛速度以及鲁棒性与准确性之间的权衡方面存在局限性。为了解决这些问题，研究提出了一种新的多模态多教师对抗鲁棒蒸馏（MMT-ARD）框架。
### Innovation
提出的MMT-ARD框架的关键创新在于采用了双教师知识融合架构，能够协同优化干净特征保持和鲁棒特征增强。为更好地处理对抗案例，引入了基于教师置信度的动态权重分配策略，实现对难样本的适应性关注。此外，通过设计一种自适应的Sigmoid加权函数来减轻教师之间的偏差，实现了跨模态知识转移强度的平衡。
### Conclusion
通过在ImageNet和零样本基准上的广泛实验表明，MMT-ARD在提高了ViT-B-32模型的鲁棒准确性(+4.32%)和零样本准确性(+3.5%)的同时，实现了比传统单教师方法2.3倍的训练效率提升。这些结果突显了MMT-ARD在增强多模态大型模型对抗鲁棒性方面的有效性和可扩展性。我们的代码可以在这个 GitHub 地址访问。
## 382. `cs.CV` - REMSA: 一个基于LLM的遥感基础模型选择智能代理 [PDF](https://arxiv.org/pdf/2511.17442), [HTML](https://arxiv.org/abs/2511.17442)
### Authors
Binger Chen,Tacettin Emre Bök,Behnood Rasti,Volker Markl,Begüm Demir
### Background
遥感（RS）中越来越多地使用基础模型（FMs）来进行环保监控、灾害评估和土地用途图绘制等任务。这些模型包括单模态视觉编码器和多模态架构，分别在单个数据模态和SAR、多光谱、高光谱和图像-文本数据的组合上进行训练。它们支持多种遥感任务，如语义分割、图像分类、变化检测和视觉问答。然而，选择合适的遥感基础模型（RSFM）仍然困难重重，原因是相关的文档分布不均，数据格式各异，部署限制也不同。
### Innovation
我们介绍了遥感基础模型数据库（RS-FMD），涵盖超过150个不同数据模态、分辨率和学习范式的RSFM。在此基础上，我们提出了REMSE，一种基于LLM的智能代理，用于从自然语言查询中自动选择RSFM。REMSE能够解释用户需求、解决缺失的约束、使用上下文学习排序候选模型，并提供透明的解释。我们还提出了一个由75个专家验证的查询场景基准，生成了900个基于专家中心评估协议的配置。REMSE在多个基线，包括简单代理、密集检索和无结构的RLHF基础上的LLM，上表现出更强的效果。它完全基于公开的元数据运行，不访问私有或敏感数据。
### Conclusion
REMSE在遥感基础模型的选择上取得了显著进展，特别是在自然语言查询的支持下自动选择模型的能力上超越了多种基线。该研究结果为进一步优化和应用遥感中的基础模型铺平了道路。
## 383. `cs.CV` - Improving Multimodal Distillation for 3D Semantic Segmentation under Domain Shift [PDF](https://arxiv.org/pdf/2511.17455), [HTML](https://arxiv.org/abs/2511.17455)
### Authors
Björn Michele,Alexandre Boulch,Gilles Puy,Tuan-Hung Vu,Renaud Marlet,Nicolas Courty
### Background
在对一种类型激光雷达进行全监督训练的语义分割网络无法很好地泛化到未见过的激光雷达上。为了缩小领域迁移时的性能差距，最近的趋势是利用跨域提供鲁棒特征的视觉基础模型（VFMs）。本文旨在通过一项全面的研究来探索VFMs在语义分割中用于激光点云的无监督领域自适应的应用途径。
### Innovation
本文研究揭示了：(1)激光雷达主干网络的结构是决定目标域泛化性能的关键因素；(2)可以预先训练一个通用的主干网络，并解决多个领域转移问题；(3)最佳结果是保持预训练的主干网络不变，并针对语义分割训练一个MLP头。基于以上研究，提出的管道在四项广泛认可且具有挑战性的设置中达到了最先进的结果。
### Conclusion
研究的最终成果是在四个广泛认可且具有挑战性的设置中实现了最新的结果，并通过冻结预训练的主干网络和训练MLP头来实现最佳语义分割效果。该研究结果表明，利用视觉基础模型进行无监督领域自适应有助于改善3D语义分割的性能。
## 384. `cs.CV` - 基于MRI测量人类脊柱衰老的人工智能框架 [PDF](https://arxiv.org/pdf/2511.17485), [HTML](https://arxiv.org/abs/2511.17485)
### Authors
Roozbeh Bazargani,Saqib Abdullah Basar,Daniel Daly-Grafstein,Rodrigo Solis Pompa,Soojin Lee,Saurabh Garg,Yuntong Ma,John A. Carrino,Siavash Khallaghi,Sam Hashemi
### Background
人类脊柱由33块椎骨构成，支持身体并对于健康生活至关重要。随着年龄的增长，脊柱容易出现退行性变化，这些变化可以通过磁共振成像（MRI）识别。以往研究主要依赖于核磁共振成像技术（MRI）来检测脊柱退化的相关情况，但尚无基于计算机视觉的深度学习方法用于估计基于MRI的脊柱年龄。
### Innovation
本文提出了一种新颖的基于计算机视觉的深度学习方法，以估计基于MRI的脊柱年龄。该方法利用了来自超过18,000个MRI系列的图像数据，且数据仅限于年龄相关脊柱退化的病例。通过使用统一流形逼近与投影（UMAP）和层次基于密度的空间聚类（HDBSCAN）来创建符合年龄特征的脊柱退化群集，并进行了详细的针对于数据量、损失函数及不同脊柱区域影响的割裂研究。
### Conclusion
研究表明，实际脊柱年龄与模型预测年龄之间的差异（脊柱年龄差距SAG）能够与椎间盘膨出、椎间盘骨刺、脊柱狭窄及骨折等脊柱退化条件以及抽烟和体力劳动等生活方式因素相关。这表明SAG可能成为评估整体脊柱健康的一个有用的生物标志物。
## 385. `cs.CV` - Radar2Shape：使用多分辨率符号距离函数从高频雷达信号构建3D形状 [PDF](https://arxiv.org/pdf/2511.17484), [HTML](https://arxiv.org/abs/2511.17484)
### Authors
Neel Sortur,Justin Goodwin,Purvik Patel,Luis Enrique Martinez Jr,Tzofi Klinghoffer,Rajmonda S. Caceres,Robin Walters
### Background
从高频雷达信号中分析3D物体形状在商业和航空航天领域具有重要意义，但这一过程在分析上非常复杂。尽管深度学习方法被应用于雷达建模，但它们在表示任意形状或处理收集角度有限的真实世界雷达信号方面存在局限性。已有从有限摄像头视角建立任意形状的方法，但这些方法在直接处理雷达信号时存在困难。因此，提出了一种双阶段方法，通过多分辨率形状特征频率相关联的方法，使用去噪扩散模型（Radar2Shape）来处理部分观测的雷达信号，并通过将频率条件为粗到细的方式来扩散到这一潜在空间中。
### Innovation
Radar2Shape采用一种新颖的方法，通过建立一个分层次分辨率的形状特征的正则化潜在空间，并通过频率条件从粗到细逐层扩散，从而成功地从部分观测的雷达信号中重建任意的3D形状。同时，该模型在两种不同的模拟数据集和实际数据上的泛化能力得到验证。
### Conclusion
Radar2Shape在从部分观察到的雷达信号中成功重建任意3D形状方面取得了显著成果，并展示了其在两种不同模拟方法和真实世界数据上的稳健泛化能力。此外，还发布了两个合成基准数据集，以促进高频雷达领域未来的研究，确保此类模型如Radar2Shape能够在实际雷达系统中安全应用。
## 386. `cs.CV` - Sparse Mixture-of-Experts for Multi-Channel Imaging: Are All Channel Interactions Required? [PDF](https://arxiv.org/pdf/2511.17400), [HTML](https://arxiv.org/abs/2511.17400)
### Authors
Sukwon Yun,Heming Yao,Burkhard Hoeckendorf,David Richmond,Aviv Regev,Russell Littman
### Background
Vision Transformers (ViTs) 已成为视觉基础模型的核心，但在细胞染色或卫星图像等多通道领域的优化仍处于探索阶段。现有方法在分词时独立处理每个通道，这虽然提高了效果，但也带来了在注意力模块中的计算瓶颈，因为通道间的比较导致注意力增加成平方级，增加了FLOPs并提高了训练成本。
### Innovation
本文从效果转向效率挑战，在跨通道注意力方面未被充分关注的问题上提出了MoE-ViT，这是一种针对ViTs的多通道图像的Sparse Mixture-of-Experts架构。每个通道被视为一个专家，通过轻量级的路由器选择与每个小块最相关的专家进行注意力处理，以减少计算负担。
### Conclusion
在JUMP-CP和So2Sat等真实世界数据集上的初步实验表明，MoE-ViT在不牺牲性能，甚至在某些情况下还能提升性能的同时实现了显著的效率提升，因此它成为一个实际且有吸引力的选择，用于多通道成像的骨干网络。
## 387. `cs.CV` - 基于草图引导验证的物理感知视频生成中的规划 [PDF](https://arxiv.org/pdf/2511.17450), [HTML](https://arxiv.org/abs/2511.17450)
### Authors
Yidong Huang,Zun Wang,Han Lin,Dong-Ki Kim,Shayegan Omidshafiei,Jaehong Yoon,Yue Zhang,Mohit Bansal
### Background
近年来，视频生成方法越来越多地依赖于规划中间的控制信号，如物体轨迹，以提高时间连贯性和运动保真度。然而，这些方法通常只能支持简单的运动规划，或者需要多次调用视频生成器进行迭代调整，导致计算成本高。
### Innovation
本文提出了一种无需训练的草图验证为基础的规划框架SketchVerify，该框架在进行完整的视频生成之前通过引入测试时采样和验证循环，以提高运动规划质量并生成更具动态一致性（即物理合理性且与指令一致的运动）的轨迹。该方法使用一个视觉-语言验证器，可以同时评估语义的一致性与物理可行性来预测和排名多个候选运动计划。这种方法通过渲染轻量级视频草图来高效评分候选运动计划，从而避免昂贵且耗时的动力学合成过程，但保持了相当的表现。
### Conclusion
实验表明，本方法在提高运动质量、物理真实性和长期一致性方面显著优于竞争基准，并且更有效率。进一步的消融研究证明了增加轨迹候选数的一致性提升整体性能。
## 388. `cs.CV` - Illustrator's Depth：基于单目图像分解的分层索引预测 [PDF](https://arxiv.org/pdf/2511.17454), [HTML](https://arxiv.org/abs/2511.17454)
### Authors
Nissim Maruani,Peiying Zhang,Siddhartha Chaudhuri,Matthew Fisher,Nanxuan Zhao,Vladimir G. Kim,Pierre Alliez,Mathieu Desbrun,Wang Yifan
### Background
数字内容创作中的一个关键挑战是如何将扁平的图像分解为可编辑的有序图层。现有的方法难以实现这一目标，特别是在保持图像结构和编辑性之间的平衡方面存在困难。
### Innovation
本文提出了一种名为Illustrator's Depth的新颖深度定义，通过模仿艺术家的创作过程，对像素进行层索引并构建一种可解释的、离散且全局一致的元素顺序，优化了编辑性。此外，还提出并训练了一个神经网络，使用一个由分层向量图形组成的自定义数据集，从光栅输入中直接预测层序。这种方法不仅在图像向量化的性能上超越了现有最佳基线，还支持高质量的文本到向量图形生成、基于2D图像的自动3D浮雕生成以及深度感知的编辑。
### Conclusion
Illustrator's Depth重新定义了深度，将其从物理量转变为创造性的抽象概念，提供了一种编辑图像分解的新框架，具有广泛的应用前景。
## 389. `cs.CV` - MCMoE: 使用混合专家完成不完整多模态动作质量评估中的缺失模态 [PDF](https://arxiv.org/pdf/2511.17397), [HTML](https://arxiv.org/abs/2511.17397)
### Authors
Huangbiao Xu,Huanqi Wu,Xiao Ke,Junyi Wu,Rui Xu,Jinglin Xu
### Background
多模态动作质量评估(AQA)近年来已成为一个有前景的范式。通过利用共享上下文线索中的互补信息，它增强了对高度相似动作序列中细微内类别变异的区分性评估。然而，在实际推理阶段，常有缺少模态的现象。缺少任何一种模态都会使现有的多模态模型失效，并导致跨模态交互中断，从而引发灾难性的性能下降。
### Innovation
本文提出了一种新颖的混合专家框架（MCMoE），统一了单阶段训练中的单模态和联合表示学习。具体而言，提出了一种自适应门控模态生成器，动态地融合可用信息以重建缺失模态。设计了模态专家来学习单模态知识，并动态混合所有专家的知识以提取跨模态联合表示。在训练阶段，利用完整的多模态特征和单模态专家知识指导模态生成和基于生成的联合表示提取。广泛的实验结果表明，我们的MCMoE在三个公共AQA基准上在完整和不完整多模态学习中都达到了最先进的效果。
### Conclusion
我们的MCMoE框架在多模态动作质量评估中展示了优越的性能，即使在存在部分缺失模态的情况下也能够实现准确的评估。
## 390. `cs.CV` - GPR-OdomNet: Difference and Similarity-Driven Odometry Estimation Network for Ground Penetrating Radar-Based Localization [PDF](https://arxiv.org/pdf/2511.17457), [HTML](https://arxiv.org/abs/2511.17457)
### Authors
Huaichao Wang,Xuanxin Fan,Ji Liu,Haifeng Li,Dezhen Song
### Background
在使用地面穿透雷达（GPR）进行机器人/车辆定位以应对恶劣天气和环境条件时，现有技术往往在处理具有微小差异的B扫描图像时难以精确估计距离。
### Innovation
本文提出了一种基于神经网络的里程计方法，该方法利用了GPR B扫描图像相似性和差异性的特征，以精确估计连续B扫描图像之间行驶的欧几里得距离。该自定义神经网络从连续时刻获取的B扫描图像中提取多尺度特征，然后通过分析这些特征之间的相似性和差异性来确定行驶的欧几里得距离。实验结果表明，该方法在所有测试中均优于现有最先进的方法，总体加权RMSE为0.449米，相比最佳现有方法降低了10.2%的RMSE。
### Conclusion
我们的方法在所有数据集上均表现出色，RMSE达到了0.449 m，该结果优于所有现有的最先进的方法，表明新方法在处理GPR B扫描图像的里程计算方面具有显著优势。
## 391. `cs.CV` - UAM：一种统一的多模态框架中的注意力-Mamba骨干网络用于肿瘤细胞分类 [PDF](https://arxiv.org/pdf/2511.17355), [HTML](https://arxiv.org/abs/2511.17355)
### Authors
Taixi Chen,Jingyun Chen,Nancy Guo
### Background
细胞级别的放射组学特征能够提供关于肿瘤表型的精细见解，并有可能大幅提高基于苏木精和伊红（H&E）图像的诊断准确性。通过捕捉微观水平的形态和强度模式，这些特征支持更精确的肿瘤识别并提高AI的可解释性，因为它能够突出显示对病理学家审查具有诊断重要性的细胞。然而，大多数现有研究集中在组织切片级或斑块级肿瘤分类上，细胞级别的放射组学分析尚未得到广泛应用。此外，目前没有专为放射组学数据设计的特定骨干模型。
### Innovation
灵感来自Mamba架构在视觉和语言领域取得的成功，本文提出了一种统一注意力-Mamba（UAM）骨干网络，专用于细胞级别的分类任务。UAM的统一设计将注意力模块和Mamba模块的能力灵活地结合在一个单一的连续架构中，从而消除了手动比例调整的需求并增强了编码能力。同时，开发了两种UAM变体以全面评估此统一结构的优势。基于此骨干网络，进一步提出了一种多模态UAM框架，该框架同时执行细胞级别的分类和图像分割。实验结果表明，UAM在这两个任务上的公共基准测试中均实现了最先进的性能，超越了基于图像的领先基础模型。细胞分类准确性从74%提高到78%（n=349,882个细胞），肿瘤分割精度从75%提高到80%（n=406个斑块）。
### Conclusion
实验结果表明，UAM在两个任务上的公共基准测试中均实现了最先进的性能，超越了基于图像的领先基础模型。该研究突显了UAM作为放射组学驱动癌症诊断的统一且可扩展的多模态基础的效用和潜力。
## 392. `cs.CV` - Counterfactual World Models via Digital Twin-conditioned Video Diffusion [PDF](https://arxiv.org/pdf/2511.17481), [HTML](https://arxiv.org/abs/2511.17481)
### Authors
Yiqing Shen,Aiza Maksutova,Chenjia Li,Mathias Unberath
### Background
世界模型通过给定控制信号来预测视觉观察随时间的演变，从而让代理能够通过前向模拟来理解环境。当前的世界模型根据实际观察生成预测，这对于理解物理AI行为在不同条件下的表现很有帮助。然而，为了应对新的应用需求，如评估物理AI行为在各种条件下的表现，世界模型需要能够回答逆向查询，例如“如果移除了这个物体会发生什么？”
### Innovation
本文引入了可以作为逆向影响输入的世界模型框架CWMDT，将其转变为有效的逆向世界模型。该框架首先构建观察到场景的数字孪生，将物体及其关系以结构化文本形式编码。其次，应用大型语言模型基于这些表示进行推理，并预测逆向干预如何随着时间推移改变观察到的场景。最后，用修改后的表示条件化视频扩散模型生成逆向视觉序列。
### Conclusion
在两个基准上的评估表明，CWMDT方法达到了最先进的性能，暗示了用于视频前向模拟基的世界模型的有效控制信号的可能视音频表示形式，例如这里所考虑的数字孪生。
## 393. `cs.CV` - 缩小智能：探索小型多模态模型中知觉与推理瓶颈 [PDF](https://arxiv.org/pdf/2511.17487), [HTML](https://arxiv.org/abs/2511.17487)
### Authors
Mark Endo,Serena Yeung-Levy
### Background
多模态模型的扩展在视觉理解与推理方面取得了显著的进步，但实际应用中需要更加紧凑、高效的系统。本文从理论上分析了多模态模型的智能缩减，研究了大型语言模型（LLM）容量减小对多模态能力的影响。初步发现，LLM容量减小对视觉能力的影响大于对继承自LLM的能力的影响。进一步观察发现，性能下降主要反映在视觉推理能力上，而非感知能力上。针对这一问题，提出了视觉提取调优的方法，该方法训练模型一致地提取指令相关视觉细节，再进行逐步推理生成答案。
### Innovation
引入了视觉提取调优方法（Visual Extraction Tuning），训练多模态模型一致地提取指令相关视觉细节，结合逐步推理生成答案。这种Extract+Think方法设定了一种新的性能与效率标准。
### Conclusion
视觉提取调优方法显著改善了小型多模态模型的性能，有助于解决其知觉与推理瓶颈，为提高模型效率和性能提供了新思路。
## 394. `cs.CV` - Video-R4：通过视觉沉思强化文本丰富的视频推理 [PDF](https://arxiv.org/pdf/2511.17490), [HTML](https://arxiv.org/abs/2511.17490)
### Authors
Yolo Yunlong Tang,Daiki Shimada,Hang Hua,Chao Huang,Jing Bi,Rogerio Feris,Chenliang Xu
### Background
理解和处理文本丰富的视频需要阅读细小且短暂的文本提示，这通常需要反复检查。然而，大多数视频问答模型依赖于单一的感知过程，通过固定的帧进行，这种过程会导致幻觉和对细微证据失败的问题。文章指出人类处理视频时会有暂停、放大和重新阅读关键区域的情况。
### Innovation
提出了一种名为Video-R4的视频推理LMM模型，该模型可以执行视觉沉思：迭代选择帧，聚焦于信息丰富的区域，重新编码检索到的像素，并更新推理状态。该模型构建了两个具有可执行沉思轨迹的数据集：Video-R4-CoT-17k用于监督训练和Video-R4-RL-30k用于强化学习。提出了一个多阶段沉思学习框架，逐步微调一个7B LMM来通过SFT和基于GRPO的RL学习原子级和混合视觉操作。
### Conclusion
Video-R4-7B在M4-ViteVQA上取得了最先进的成果，并且进一步适用于多页文档问答、幻灯片问答和通用视频问答，表明迭代沉思是像素接地多模态推理的有效范式。
## 395. `cs.CV` - 生成增强现实：范式、技术与未来应用 [PDF](https://arxiv.org/pdf/2511.16783), [HTML](https://arxiv.org/abs/2511.16783)
### Authors
Chen Liang,Jiawen Zheng,Yufeng Zeng,Yi Tan,Hengye Lyu,Yuhui Zheng,Zisu Li,Yueting Weng,Jiaxin Shi,Hanwang Zhang
### Background
本文介绍了一种下一代增强现实（AR）范式——生成增强现实（GAR），它重新定义了增强过程，将其视为一个世界再合成过程，而不是由传统AR引擎进行的世界组合过程。GAR用统一的生成骨干模块取代了传统AR引擎中的多阶段模块，环境感知、虚拟内容和交互信号联合编码为持续视频生成的条件输入。
### Innovation
GAR创新之处在于它用统一的生成骨架模块取代了传统AR的多阶段模块，通过环境感知、虚拟内容和交互信号的联合编码来提供实时生成的增强现实体验。研究总结了使实时生成增强现实可行的技术基础，并概述了利用其统一推断模型的潜在应用。
### Conclusion
本文设想GAR作为一种未来AR范式，能提供高度真实的体验，增强交互性和沉浸感，并引起了关于技术、内容生态和伦理及社会影响的新研究挑战。
## 396. `cs.CV` - 扩散模型中的能耗定律：量化图像生成中的计算和碳排放 [PDF](https://arxiv.org/pdf/2511.17031), [HTML](https://arxiv.org/abs/2511.17031)
### Authors
Aniketh Iyengar,Jiaqi Han,Boris Ruf,Vincent Grari,Marcin Detyniecki,Stefano Ermon
### Background
扩散模型在图像生成中的计算需求迅速增长，引起了对能耗和环境影响的关注。现有用于能耗优化的方法主要集中在架构改进或硬件加速上，缺乏能够预测不同模型配置和硬件设置下能耗的原理性方法。
### Innovation
提出了将Kaplan能量缩放定律应用于预测基于浮点运算数量（FLOPs）的GPU能耗的方法。该方法将扩散模型推理分解为文本编码、去噪迭代和解码组件，并假设去噪操作由于其在多个推理步骤中的重复执行而占主导地位，从而主导能耗。
### Conclusion
该能量缩放定律在各个架构内具有高的预测准确性（R-squared > 0.9），具有强大的跨架构泛化能力，能够在模型和硬件组合中可靠地估算能耗。这些结果验证了扩散推理的计算受限性质，并为可持续人工智能部署规划和碳足迹估算提供了一个基础。
## 397. `cs.CV` - MRI Super-Resolution with Deep Learning: A Comprehensive Survey [PDF](https://arxiv.org/pdf/2511.16854), [HTML](https://arxiv.org/abs/2511.16854)
### Authors
Mohammad Khateri,Serge Vasylechko,Morteza Ghahremani,Liam Timms,Deniz Kocanaogullari,Simon K. Warfield,Camilo Jaimes,Davood Karimi,Alejandra Sierra,Jussi Tohka,Sila Kurugol,Onur Afacan
### Background
高分辨率MRI对于临床和研究应用至关重要，但实现高分辨率通常成本高且受限于技术权衡和实验限制。超分辨率（SR）提供了一种有前景的计算方法，可以生成高分辨率图像，从更加经济的低分辨率扫描中获取，从而在不增加硬件的情况下提高诊断准确性和效率。
### Innovation
该论文对基于深度学习（DL）的MRI超分辨率技术进行了全面回顾，不仅涵盖了理论基础、架构设计、学习策略、基准数据集和性能指标，还提出了系统的分类方法，并深入研究了适用于MRI的成熟和新兴超分辨率技术，同时指出了社区需要解决的挑战和方向。
### Conclusion
该论文指出了MRI超分辨率技术面临的开放挑战和方向，并提供了重要的开放资源、工具和教程，旨在为该领域的研究和应用提供支持。
## 398. `cs.CV` - 全注意力驱动的原生3D编辑 [PDF](https://arxiv.org/pdf/2511.17501), [HTML](https://arxiv.org/abs/2511.17501)
### Authors
Weiwei Cai,Shuangkang Fang,Weicai Ye,Xin Dong,Yunhan Yang,Xuanyang Zhang,Wei Cheng,Yanpei Cao,Gang Yu,Tao Chen
### Background
3D内容创建领域中，基于指令的3D编辑正在快速发展，但现有方法面临重大挑战：基于优化的方法速度过慢，而依赖多视角2D编辑的方法则常导致几何不一致性和视觉质量下降。
### Innovation
提出了一种新颖的原生3D编辑框架，能够在单次高效前馈传递中直接操作3D表示。为此，创建了一个大规模的多模态数据集，用于指令引导的3D编辑，涵盖了多样化的添加、删除和修改任务，同时探索了两种不同的条件策略：传统的交叉注意力机制和新颖的3D标记级联方法。
### Conclusion
实验结果表明，3D标记级联方法在参数效率和性能上更优。全面的评估结果显示，该方法在生成质量、3D一致性及指令忠实性方面超过了现有的2D提升方法，设立了新的基准。
## 399. `cs.CV` - MedImageInsight用于胸部腔健康管理的胸片分类 [PDF](https://arxiv.org/pdf/2511.17043), [HTML](https://arxiv.org/abs/2511.17043)
### Authors
Rama Krishna Boya,Mohan Kireeti Magalanadu,Azaruddin Palavalli,Rupa Ganesh Tekuri,Amrit Pattanayak,Prasanthi Enuga,Vignesh Esakki Muthu,Vivek Aditya Boya
### Background
胸部X射线检查一直是胸部诊断中应用最广泛的成像技术之一。然而，随着检查量的增加和放射科医生工作负担的加重，及时解读检查结果正成为一个挑战。
### Innovation
本研究探索了使用MedImageInsight这种基础医学成像模型对胸部X射线进行自动二分类，分为正常和异常两类。研究评估了两种方法：(1) 对MedImageInsight进行微调以实现端到端分类，(2) 使用MedImageInsight作为特征提取器训练传统的机器学习分类器。研究使用了ChestX-ray14数据集和来自合作伙伴医院的临床数据进行实验，微调后的分类器表现出最好的性能，达到了0.888的ROC-AUC，并且在准确性方面优于迁移学习模型，其性能与CheXNet等已有的架构相当。该研究展示了基础医学成像模型在减少特定任务训练需求的同时保持诊断可靠性方面的有效性。系统已设计用于集成到基于Web和医院PACS的工作流程中，以支持分诊并减轻放射科医生的工作负担。
### Conclusion
微调后的分类器实现了最佳性能，ROC-AUC达到0.888，并且校准效果优于迁移学习模型，性能达到了与已建立的架构相似的水平，展示了基础医学成像模型在减少特定任务训练需求方面有效的同时保持诊断可靠性。未来的工作将扩展模型到多标签病理分类，以在临床环境中提供初步诊断解释。
## 400. `cs.CV` - TP-MDDN: 基于自主决策的具有任务优先多需求导向导航 [PDF](https://arxiv.org/pdf/2511.17225), [HTML](https://arxiv.org/abs/2511.17225)
### Authors
Shanshan Li,Da Huang,Yu He,Yanwei Fu,Yu-Gang Jiang,Xiangyang Xue
### Background
在现实生活中，人们经常需要在空间中移动以找到满足他们需求的物品，这对体现式人工智能提出了一个关键挑战。传统的基于需求驱动的导航（DDN）只能处理单一的需求，无法反映涉及多个需求和个人选择的真实世界任务的复杂性。
### Innovation
为了弥合这一差距，作者引入了任务优先多需求导向导航（TP-MDDN），这是一个涉及多个子需求且具有明确任务偏好的长期导航的新基准。为了解决TP-MDDN，作者提出了AWMSystem，其中包含三项关键模块：BreakLLM（指令分解）、LocateLLM（目标选择）和StatusMLLM（任务监控）。对于空间记忆，设计了MASMap，结合了3D点云积累和2D语义映射，以实现准确和高效的环境理解。还提出了一种双时间尺度的行为生成框架，该框架结合了零样本规划与基于策略的精细控制，并进一步支持了适应性错误校正器，以实时处理实际案例中的失败情况。
### Conclusion
实验表明，我们的方法在感知准确性和导航鲁棒性方面均优于最先进的基线方法。
## 401. `cs.CV` - MobileOcc：为移动机器人设计的人本感知语义占用数据集 [PDF](https://arxiv.org/pdf/2511.16949), [HTML](https://arxiv.org/abs/2511.16949)
### Authors
Junseo Kim,Guido Dumont,Xinyu Gao,Gang Chen,Holger Caesar,Javier Alonso-Mora
### Background
密集的3D语义占用感知对于在人群密集环境中操作的移动机器人至关重要，但在人类密集环境的应用上仍然远不如其在自主驾驶中的应用受到重视。这个问题吸引了研究人员的关注。
### Innovation
提出了MobileOcc，这是一个为在拥挤的人类环境中操作的移动机器人设计的语义占用数据集。该数据集集成了静态对象占用标注，并引入了用于人体占用建模的新型网格优化框架，通过2D图像重构人体的可变形几何形状，再利用相关的LiDAR点云数据进行细化和优化。该数据集用于建立两种任务的基准，即占用预测和行人速度预测，并提供了不同的方法进行评估，包括单目、立体和全景占用。此外，该研究还进一步评估了其标注方法在3D人类姿态估计数据集上的表现。
### Conclusion
该方法在不同的数据集上表现出稳健的性能。
## 402. `cs.CV` - 视觉语言模型理解视觉说服力吗？ [PDF](https://arxiv.org/pdf/2511.17036), [HTML](https://arxiv.org/abs/2511.17036)
### Authors
Gyuwon Park
### Background
近年来，视觉-语言模型(VLMs)在多模态推理和理解方面取得了显著进展。但是，这些模型是否真正理解了视觉说服力——即视觉线索如何影响人类的态度和决策——仍不清楚。
### Innovation
该研究构建了一个高度一致的数据集，用于二元说服力判断，并引入了视觉说服因素(VPFs)的分类，涵盖了低级知觉、中级组合和高级语义线索。此外，研究探讨了说服相关的认知引导和知识注入策略。通过VLMs的实证分析发现，这些模型存在回忆偏见，高说服力的预测过于乐观，对低级/中级特征缺乏区分力，而高级语义信息与信息和对象存在的对齐是预测人类判断的最强因子。在干预策略方面，简单指令或未指导的推理支架效果有限或负效果，而简洁且基于对象的理由能够显著提高精度和F1分数。
### Conclusion
VLMs的核心限制不在于识别说服性对象，而在于将它们与交际意图联系起来。
## 403. `cs.CV` - EvDiff: 仅从单色事件流生成高质量视频 [PDF](https://arxiv.org/pdf/2511.17492), [HTML](https://arxiv.org/abs/2511.17492)
### Authors
Weilun Li,Lei Sun,Ruixi Gao,Qi Jiang,Yuqin Ma,Kaiwei Wang,Ming-Hsuan Yang,Luc Van Gool,Danda Pani Paudel
### Background
事件摄像机作为一种神经形态传感器，能够异步记录亮度的变化，以稀疏事件流的形式记录，具有高时间分辨率和高动态范围的优势。从事件重构强度图像是一个高度不良设定的任务，因为绝对亮度存在固有的模糊性。早期的方法通常遵循端到端的回归范式，直接将事件映射到强度帧，但这些方法往往在感知效果上表现不佳，并且在模型容量和训练数据方面难以扩展。
### Innovation
提出了基于事件的扩散模型EvDiff，该模型遵循替代训练框架，能够产生高质量的视频。为了降低高帧率视频生成的高额计算成本，设计了一种只进行一次前向扩散步骤的基于事件的扩散模型，并配备了具有时序一致性的EvEncoder。此外，新型的替代训练框架消除了对配对事件-图像数据集的依赖，使模型能够利用大规模图像数据集以获得更高的容量。
### Conclusion
实验结果证明，我们的方法在保真度和真实感方面找到了一个很好的平衡点，在像素级和感知指标上均优于现有方法，能够仅从单色事件流中生成高质量彩色视频。
## 404. `cs.CV` - OmniLens++：大规模镜头库预训练及潜在点扩展函数表示的盲镜头畸变校正 [PDF](https://arxiv.org/pdf/2511.17126), [HTML](https://arxiv.org/abs/2511.17126)
### Authors
Qi Jiang,Xiaolong Qian,Yao Gao,Lei Sun,Kailun Yang,Zhonghua Yi,Wenyong Li,Ming-Hsuan Yang,Luc Van Gool,Kaiwei Wang
### Background
现有的镜头畸变校正管道在处理多样化未知光学校正问题时存在数据难以扩大和缺乏先验指导的挑战，这限制了现有框架的一般化能力。
### Innovation
提出了OmniLens++框架，该框架通过扩展设计规范以增加镜头数据的降级多样性，并通过量化光学校正的时空变化和严重程度来采样更均匀的分布，进而解决数据扩大的问题。在模型设计方面，提出了一种潜在点扩展函数表示（LPR），利用点扩展函数（PSFs）作为优化目标，通过引入VQVAE框架学习LensLib的潜在特征，并将其与光学校正机制建模相结合以学习先验错误。实验表明，在多种真实和合成镜头畸变上，OmniLens++展现了领先的一般化能力。
### Conclusion
OmniLens++框架验证了AODLibpro作为大规模基础训练数据的有效性，并且LPR能够进一步发挥大规模镜头库的潜力。源代码和数据集将在指定网站上公开。
## 405. `cs.CV` - 通过分层任务抽象机制设计特定领域代理 [PDF](https://arxiv.org/pdf/2511.17198), [HTML](https://arxiv.org/abs/2511.17198)
### Authors
Kaiyu Li,Jiayu Wang,Zhi Wang,Hui Qiao,Weizhan Zhang,Deyu Meng,Xiangyong Cao
### Background
LLM驱动的代理，尤其是那些使用通用框架如ReAct或人类启发的角色扮演，在需要严格结构化工作流的专业领域中表现不佳。例如，在遥感领域，需要使用专业工具（如校正、光谱指数计算）和多步骤流程（如多个中间产品和可选步骤）的系统，对一般化方法构成了重大挑战。
### Innovation
本文提出了一种新颖的代理设计框架，中心在于层次任务抽象机制（HTAM）。与模拟社会角色不同，HTAM将多代理系统结构化为一个逻辑层次，该层次反映了给定领域中内在的任务依赖关系图。任务中心的架构保证了程序的正确性，并将复杂问题分解为顺序层，每个层的子代理在其前一层次的输出之上进行操作。通过一个名为EarthAgent的多代理系统实例化该框架，用于复杂的地理空间分析。为此，构建了一个名为GeoPlan-bench的基准测试套件，旨在评估复杂的规划能力和多步骤地理空间规划任务的真实表现。
### Conclusion
实验结果表明，EarthAgent在复杂规划能力方面显著优于各种现有的单代理和多代理系统。我们的工作证明，将代理架构与领域内在的任务结构对齐是构建稳健可靠的专用自主系统的关键步骤。
## 406. `cs.CV` - 重访多模态KV缓存压缩：基于频域的异常KV感知方法 [PDF](https://arxiv.org/pdf/2511.16786), [HTML](https://arxiv.org/abs/2511.16786)
### Authors
Yaoxin Yang,Peng Ye,Xudong Tan,Chongjun Tu,Maosen Zhao,Jia Hao,Tao Chen
### Background
多模态大型语言模型在进行推理时遭受严重的计算开销，因为多模态KV缓存的增长与视觉输入长度成正比。现有的一些多模态KV缓存压缩方法主要依赖于注意力分数降低缓存大小，这使得它们与现有的高效注意力内核（如FlashAttention）不兼容，并且忽略了值向量对注意力输出的贡献。
### Innovation
本文从KV矩阵分布的角度重新审视了多模态KV缓存压缩。首先，作者观察到多模态KV矩阵的频域能量主要集中在低频，通过低通滤波器提取了主要能量。进一步地，作者发现那些与主要能量差异很大的KV对性能有显著影响，将其定义为异常KV。基于异常KV更可能编码对于推理至关重要的特征，作者提出了FlashCache，一种基于频域指导、异常KV感知的KV缓存压缩框架。此框架引入了一个异常KV识别模块，该模块在频域中建模多模态KV矩阵的主要成分，并优先保留与之差异显著的KV对。此外，设计了动态预算分配模块以适配性地确定每层KV缓存的大小，以保留更多的异常KV。实验结果表明，FlashCache优于现有的多模态KV压缩方法，实现了1.69倍的解码速度提升，并减少了80%的KV内存使用，同时保持了任务性能。
### Conclusion
实验结果表明，FlashCache方法在多个MLLM和基准测试中表现出色，实现了解码速度提高和KV内存使用减少的同时，保持了任务性能。
## 407. `cs.CV` - 使用长上下文Q-Former结合多模态LLM进行机器人确认生成和动作规划 [PDF](https://arxiv.org/pdf/2511.17335), [HTML](https://arxiv.org/abs/2511.17335)
### Authors
Chiori Hori,Yoshiki Masuyama,Siddarth Jain,Radu Corcodel,Devesh Jha,Diego Romeres,Jonathan Le Roux
### Background
人类与机器人协作需要理解人类的动作和与周围环境的互动。研究人类-机器人交互(HRI)主要依赖于人类-机器人对话，其中机器人通过多模态场景理解来确认动作并生成动作步骤。当前方法使用多模态变压器从单个片段中生成与机器人动作确认一致的动作步骤，但没有充分利用长时上下文信息。您厨2数据集的实验表明，确认生成的准确性是动作规划性能的关键因素。
### Innovation
本文提出了一种结合左侧和右侧上下文依赖性的长时上下文Q-Former，并提出了一种文本预处理方法，直接将文本嵌入输入到LLM解码器，以减轻Q-Former对文本信息高度抽象的问题。实验结果显示，长时上下文Q-Former能够提高确认生成和动作规划。
### Conclusion
本文通过引入长时上下文Q-Former提高了机器人确认生成和动作规划的性能，实验结果表明，与传统的只利用片段级上下文的方法相比，长时上下文的利用显著提升了性能。
## 408. `cs.CV` - SMILE: 一种综合词法-语义评价指标 [PDF](https://arxiv.org/pdf/2511.17432), [HTML](https://arxiv.org/abs/2511.17432)
### Authors
Shrikant Kendre,Austin Xu,Honglu Zhou,Michael Ryoo,Shafiq Joty,Juan Carlos Niebles
### Background
传统的文本和视觉问答评估指标，如ROUGE、METEOR和精确匹配(EM)，主要依赖于基于n-gram的词汇相似性，忽视了准确评估所需的深层语义理解。虽然BERTScore和MoverScore之类的度量标准利用了上下文嵌入来解决这个问题，但它们缺乏在句子级和关键词级语义之间的灵活性，并且忽略了词汇相似性，后者在评估中仍然很重要。大型语言模型(Large Language Model, LLM)的评估工具尽管强大，但存在高成本、偏见、不一致性和幻想等缺点。
### Innovation
本文引入了SMILE：语义度量集成词汇精确度，这是一种新颖的方法，结合了句子级语义理解和关键词级语义理解和易于匹配关键词。该复合方法平衡了词汇精确度和语义相关性，提供了综合评价。
### Conclusion
广泛的任务基准测试表明，SMILE与人类判断高度相关，并且计算量轻，填补了词法和语义评价之间的差距。
## 409. `cs.CV` - 学习隐式透射和反光图以移除镜头遮光反光 [PDF](https://arxiv.org/pdf/2511.17353), [HTML](https://arxiv.org/abs/2511.17353)
### Authors
Xiaolong Qian,Qi Jiang,Lei Sun,Zongxi Yu,Kailun Yang,Peixuan Wu,Jiacheng Zhou,Yao Gao,Yaoguang Ma,Ming-Hsuan Yang,Kaiwei Wang
### Background
紧凑光学系统（包括单镜头和金属镜设计）通常被认为会有光学缺陷，但在实际复杂环境中，它们的成像性能还会进一步受到非理想光学表面和涂层引起的散射光引起的遮光反光（veiling glare）的损害。这种复合降级现象虽然挑战了传统的透镜畸变校正方法，但尚未受到广泛探索。常规的散射模型（例如，去雾模型）无法准确模拟遮光反光，因为其具有空间变化且与深度无关的特点，这使得通过模拟准备与其配对的高质量数据变得困难，阻碍了数据驱动的遮光反光移除模型的应用。
### Innovation
本研究提出了VeilGen，这是一种生成模型，能够无需监督地从目标图像中估计遮光反光的光学透射图和反光图，并通过稳定的扩散（SD）先验进行正则化。VeilGen可以生成具有真实复合退化光学缺陷和遮光反光的数据集配对，同时提供估计的光学透射图和反光图以指导遮光反光移除过程。此外，还提出了基于逆过程约束的修复网络DeVeiler，该网络利用预测的隐空间图来指导学习散射模型的逆过程。
### Conclusion
广泛的实验证明，本方法在复杂的紧凑光学系统中提供了更高质量和物理准确性的图像恢复，表明VeilGen可靠地合成了真实的遮光反光，而其学习到的隐空间图有效地引导了DeVeiler中的图像恢复过程。所有代码和数据集将在此处公开。
## 410. `cs.CV` - Self-Supervised Learning by Curvature Alignment [PDF](https://arxiv.org/pdf/2511.17426), [HTML](https://arxiv.org/abs/2511.17426)
### Authors
Benyamin Ghojogh,M.Hadi Sepanj,Paul Fieguth
### Background
自监督学习（SSL）最近通过非对比方法取得了进步，这些方法将不变性项与方差、协方差或冗余降低惩罚结合在一起。虽然这样的目标塑造了表示的一阶和二阶统计特性，但它们很大程度上忽视了底层数据流形的局部几何结构。
### Innovation
提出了一个基于曲率正则化的自监督学习框架（CurvSSL），并在核希尔伯特空间中扩展了它，称为核曲率CurvSSL。该方法在标准的两视图编码器-投影器结构中加入了基于冗余降低损失的Barlow Twins风格的投影特征，同时通过基于曲率的正则化器来增强，每个嵌入被视为一个顶点，其最近的k个邻居通过余弦交互定义了一个离散的曲率得分；在核变体中，曲率是基于局部归一化格拉姆矩阵在核希尔伯特空间中计算的。这些得分通过基于曲率的矩阵的Barlow风格的损失进行对齐和去相关，鼓励视图不变性和局部流形弯曲的一致性。
### Conclusion
在MNIST和CIFAR-10数据集上使用ResNet-18骨干网络的实验结果表明，基于曲率正则化的SSL在线性评估性能上与Barlow Twins和VICReg相比具有竞争力或更高的性能。研究结果表明，明确塑造局部几何结构是对统计SSL正则化器纯粹统计学方法的简单且有效的补充。
## 411. `cs.CV` - METIS: 多源自视点训练的整合细腻视觉-语言-动作模型 [PDF](https://arxiv.org/pdf/2511.17366), [HTML](https://arxiv.org/abs/2511.17366)
### Authors
Yankai Fu,Ning Chen,Junkai Zhao,Shaozhe Shan,Guocai Yao,Pengwei Wang,Zhongyuan Wang,Shanghang Zhang
### Background
在构建能够跨多种任务感知、推理和操作的一般机器人方面，特别是对于灵巧操作，仍存在挑战。主要瓶颈在于缺乏标注大量操作技能的数据，因为遥操作困难且成本高。人类数据规模大，行为多样，为机器人学习动作提供了丰富的先验知识。尽管先前工作探索了利用人类演示，但它们通常受限于有限的场景和人类与机器人之间的视觉差距。
### Innovation
本文提出了一种基于多源自视点数据的视觉-语言-动作（VLA）模型METIS，用于灵巧操作。首先，构建了EgoAtlas，整合了来自多个来源的大量人类和机器人的数据，并统一在一致的操作空间下。进一步提取了运动感知的动力学，这是一种紧致且离散的运动表示，为VLA训练提供了有效的监督。METIS结合了推理和行动，形成了一个统一的框架，使得在下游操作任务中有效部署成为可能。
### Conclusion
我们的方法展示了卓越的灵巧操作能力，在六个真实世界任务中平均成功率达到最高。实验结果还突显了METIS在离分布场景中具有优越的泛化性和鲁棒性。这些发现强调METIS向通用模型迈进灵巧操作的重要一步。
## 412. `cs.CV` - 合作网络架构：学习结构化的网络模式作为感官模式的表示 [PDF](https://arxiv.org/pdf/2407.05650), [HTML](https://arxiv.org/abs/2407.05650)
### Authors
Pascal J. Sager,Jan M. Deriu,Benjamin F. Grewe,Thilo Stadelmann,Christoph von der Malsburg
### Background
当前的视觉系统面临着鲁棒性、适应性以及对异常分布数据的泛化能力等方面的挑战。为了克服这些挑战，本文提出了一种称为合作网络架构（CNA）的新模型。
### Innovation
CNA通过结构化、循环连接的神经元网络来表示感官信号，并且能够从重叠的网片段学习到统计规律，从而构建出动态组合的网络结构。这种架构能够对噪声、变形具有鲁棒性，并且可以泛化到未遇到过的数据分布上。它的一个重要创新点是能够无监督地学习网片段，灵活地重新组合以编码新的模式。
### Conclusion
本文的研究成果表明，CNA作为一种结合局部特征处理与全局结构构建的神经表示模型的新范式，具有很好的前景，为未来研究不变对象识别奠定了基础。
## 413. `cs.CV` - 从点云数据中利用CVAE进行多指 gripper 联合配置估计 [PDF](https://arxiv.org/pdf/2511.17276), [HTML](https://arxiv.org/abs/2511.17276)
### Authors
Julien Merand,Boris Meden,Mathieu Grossard
### Background
本文提出了一种高效的方法，仅从视觉传感器、模拟或生成神经网络生成的多环节机械手的点云数据中确定多指 gripper 的联合配置。传统的逆运动学（IK）技术虽然可以提供数学上的精确解（如果存在的话），但在一些情况下需要后处理决策，或者依靠算法数值近似解决更复杂的运动学问题。
### Innovation
本文的方法利用了机器学习，特别是条件变异自动编码器（CVAE），将关键结构元素的点云数据输入，从而隐式克服了上述挑战。该方法能够在0.05毫秒内用 Allegro Hand 在 MultiDex 掌握数据集上进行验证，达到与当前最佳方法相当的准确性。
### Conclusion
本文展示了利用 CVAE 方法在更广泛的人工智能驱动技术框架下进行夹持规划中关节配置估计的有效性。
## 414. `cs.CV` - IndustryNav：探索动态工业导航中具身智能体的空间推理能力 [PDF](https://arxiv.org/pdf/2511.17384), [HTML](https://arxiv.org/abs/2511.17384)
### Authors
Yifan Li,Lichi Li,Anh Dao,Xinyu Zhou,Yicheng Qiao,Zheda Mai,Daeun Lee,Zichen Chen,Zhen Tan,Mohit Bansal,Yu Kong
### Background
视觉大型语言模型（VLLMs）作为具身代理具有巨大潜力，但它们在空间推理方面仍面临重大挑战。现有具身基准主要关注被动的、静态的家庭环境，并仅评估孤立能力，未能捕捉到动态现实世界中的整体性能。本文提出了IndustrialNav，这是第一个用于主动空间推理的动态工业导航基准。IndustrialNav 利用12个动态物体和人类运动的高保真Unity仓库场景，采用包含自中心视角和全局航迹的PointGoal导航管道进行评估。
### Innovation
IndustrialNav 是第一个用于主动空间推理的动态工业导航基准。该基准利用Unity构建了12个手动创建的高保真仓库场景，展示了动态对象和人类运动。引入了‘碰撞率’和‘警告率’这些新的评价指标来衡量具有方向感和距离估计的行为，以及安全性行为。评估了九种最先进的视觉大型语言模型在路径规划、碰撞避免和积极探索方面的能力，结果表明封闭源代码模型保持了一致的优势，但所有代理都存在显著的缺陷。
### Conclusion
研究表明，封闭源代码模型在稳定规划、积极探索和动态现实世界环境中的安全行为方面保持了相对优势；然而，所有代理在路径规划、碰撞避免和主动探索方面都表现出明显的不足，突显出进一步研究中这一领域移动从被动感知转到需要规划、探索和安全行为的任务的必要性。
## 415. `cs.CV` - 3D混凝土CT图像中的裂缝预检测的统计方法 [PDF](https://arxiv.org/pdf/2402.16126), [HTML](https://arxiv.org/abs/2402.16126)
### Authors
Vitalii Makogin,Duc Nguyen,Evgeny Spodarev
### Background
在实际应用中，对于大型CT图像中裂缝的有效分割对于理解材料的结构完整性具有重要意义。经典图像处理技术和现代深度学习模型在直接处理高分辨率大数据时都面临着巨大的计算挑战。
### Innovation
提出的统计框架用于裂缝的预定位，该方法结合了基于Hessian的简单滤波器、在规则空间分区上计算的几何描述符以及空间多重假设检验程序，能够在仅依赖少量校准数据的情况下检测异常区域，而不需要大型标注数据集。
### Conclusion
实验表明，该方法能够可靠地突出显示可能包含裂缝的区域，并保持线性的计算复杂度。通过将后续的高分辨率分割限制在这些局部区域，深度学习模型可以更有效地训练和运行，从而减少训练时间和资源消耗。因此，该框架为大规模CT检查管道提供了一个实用且可解释的数据预处理步骤。
## 416. `cs.CV` - AV-Lip-Sync+: 利用 AV-HuBERT 提取多模态不一致性进行前视脸视频深伪检测 [PDF](https://arxiv.org/pdf/2311.02733), [HTML](https://arxiv.org/abs/2311.02733)
### Authors
Sahibzada Adil Shahzad,Ammarah Hashmi,Yan-Tsung Peng,Yu Tsao,Hsin-Min Wang
### Background
多模态操纵（又称音频-视觉深度伪造）使得单一模态的深度伪造检测器难以检测多媒体内容中的伪造。防止错误宣传和假新闻的传播，及时检测至关重要。单一模态的深度伪造检测只能发现损伤其中一个模态（视觉或音频），但是通过融合两种信息的多模态模型可以发现两者的不一致。现有方法主要采用单一视频检测，并通过监督预训练进行伪造检测。
### Innovation
本文提出了一种基于多模态自监督学习（SSL）特征提取器的方法，用于利用音频和视觉模态之间的一致性差异进行多模态视频伪造检测。具体而言，作者采用了基于转换器的SSL预训练 Audio-Visual HuBERT （AV-HuBERT）模型进行视觉和声学特征提取，利用多尺度时序卷积神经网络捕捉音频和视觉模态之间的相关性。此外，作者还采用了基于转换器的视频模型来提取面部特征，并捕获深度伪造生成过程中的空间和时间伪影。实验结果表明，本文模型在 FakeAVCeleb 和 DeepfakeTIMIT 数据集上的性能优于现有所有模型，并实现了新的最佳性能。
### Conclusion
本文提出的方法在利用多模态自监督学习进行视频伪造检测方面取得了显著的性能提升。通过联合使用 Audio-Visual HuBERT 和多尺度时序卷积神经网络，本文模型有效地检测了音频-视觉模态之间的不一致，从而提高了伪造视频的检测精度。
## 417. `cs.CV` - 失之毫厘谬以千里：视觉语言模型在真实世界表格中的失败模式透析 [PDF](https://arxiv.org/pdf/2511.17238), [HTML](https://arxiv.org/abs/2511.17238)
### Authors
Anshul Singh,Rohan Chaudhary,Gagneet Singh,Abhay Kumary
### Background
现有的视觉语言模型（VLMs）主要在未能充分反映现实世界复杂性的基准测试中表现出色。现有针对表格问答的数据集，如 WikiTableQuestions 和 FinQA，主要使用单一语言（英语）并且表格呈现为完美无瑕的数据格式，这造成了理论研究与实际应用之间的差距。
### Innovation
本文提出了 MirageTVQA，一个新的基准测试，旨在评估 VLMs 在多语言和视觉不完美表格上的表现能力。数据集包含近 60,000 对多语言 QA 对，包含视觉噪声和扫描文档中具有的现实性噪声，以此挑战当前领先 VLMs 的视觉多样性和语言多样性处理能力。
### Conclusion
MirageTVQA 为衡量和驱动能够处理视觉噪声和多语言推理的更稳健的 VLM 模型提供了基准。该数据集和代码可在指定链接获取，展示了 VLMs 在面对视觉噪声和多语言推理时的主要失败点：性能严重下降（最优模型下降超过 35%）以及持续的英语优先偏差，推理能力无法有效转移到其他语言。
## 418. `cs.CV` - 基于侧图卷积的Token适配以提高3D点云Transformer的高效微调 [PDF](https://arxiv.org/pdf/2502.14142), [HTML](https://arxiv.org/abs/2502.14142)
### Authors
Takahiko Furuya
### Background
预训练3D点云Transformer的参数高效微调（PEFT）已成为3D点云分析的一种有前景的技术。现有的PEFT方法试图最小化可调参数的数量，但在微调过程中往往面临较高的时间和空间计算成本。
### Innovation
本文提出了一种新型PEFT算法，即基于邻域图的Token侧向适应算法（STAG），以实现更优的时间和空间效率。STAG利用与冻结的Transformer主干并行运行的图卷积侧网络，使Token适应下游任务。通过有效的图卷积、参数共享和减少梯度计算，STAG极大地降低了微调的时间和空间成本。
### Conclusion
通过在多种预训练模型和新的基准PCC13上的广泛实验，证明STAG在保持分类精度的同时，减少了可调参数至0.43M，并实现了显著的微调时间及内存消耗减少。
## 419. `cs.CV` - SpotFormer: 多尺度时空变换器的面部表情定位 [PDF](https://arxiv.org/pdf/2407.20799), [HTML](https://arxiv.org/abs/2407.20799)
### Authors
Yicheng Deng,Hideaki Hayashi,Hajime Nagahara
### Background
面部表情定位，即在一个视频中识别面部表情出现的时期，是一个在面部表情分析中至关重要但又极具挑战性的工作。目前存在的问题包括无关面部动作的干扰以及检测细微表情运动的难题，这些都阻碍了准确的表情定位。
### Innovation
我们提出了一个高效的面部表情定位框架。首先，我们提出了基于滑动窗口的多时序分辨率光流（SW-MRO）特征，该特征在紧凑的滑动窗口中计算输入图像序列的多时序分辨率光流。窗口长度被调整以感知完整的微表情并区分一般的大表情和微表情。SW-MRO 能够有效地揭示细微运动，同时避免光流被头部运动主导。其次，我们提出了多尺度时空变换器SpotFormer，能够同时编码SW-MRO 特征的时空关系，进行精确的帧级概率估计。在SpotFormer 中，我们使用了提出的面部局部图池化（FLGP）操作和卷积层来提取多尺度时空特征。最后，我们引入了监督对比学习来增强对不同表情类型的可辨别性。
### Conclusion
在SAMM-LV，CAS(ME)²，和CAS(ME)³上的广泛实验表明，我们的方法优于现有的模型，特别是在微表情定位方面。
## 420. `cs.CV` - 通过语义补全与分解解决多元情感差异的多模态情感检测 [PDF](https://arxiv.org/pdf/2407.07026), [HTML](https://arxiv.org/abs/2407.07026)
### Authors
Daiqing Wu,Dongbao Yang,Huawen Shen,Can Ma,Yu Zhou
### Background
近年来社交媒体帖子激增，对多模态（图文）内容的情感检测需求迅速增长。由于帖子是由用户生成的，来自同一帖子的图片和文本可能表达不同的甚至矛盾的情绪，导致潜在的情感差异。现有工作的主要问题是采用了单一分支融合结构，主要捕捉图片和文本之间的一致情绪，这忽视或隐式建模了情绪差异，导致单模态编码效果有限且性能受限。
### Innovation
本文提出了一种语义补全和分解（CoDe）网络来解决上述问题。语义补全模块通过补充图片和文本表示中的图片中文字的语义，帮助缩小情绪差距。语义分解模块通过独占投影和对比学习分解图形单元和文本表示，从而明确捕捉不同情感模式之间的差异性情绪。最后，通过交叉注意机制融合图形单元和文本表示，并结合学习到的差异性情感进行最终分类。
### Conclusion
在四个数据集上的广泛实验表明，CoDe的优越性和每个提出的模块的有效性。
## 421. `cs.CV` - CLIMB-3D: Continual Learning for Imbalanced 3D Instance Segmentation [PDF](https://arxiv.org/pdf/2502.17429), [HTML](https://arxiv.org/abs/2502.17429)
### Authors
Vishal Thengane,Jean Lahoud,Hisham Cholakkal,Rao Muhammad Anwer,Lu Yin,Xiatian Zhu,Salman Khan
### Background
尽管3D实例分割（3DIS）已经取得了显著进步，但多数现有方法假定所有对象类别已知且均匀分布。然而，在现实动态环境中，新的类别会逐渐出现，并表现出天然的类别不平衡。虽然一些方法试图解决新兴类别的问题，但它们往往忽略了类别不平衡，导致在稀有类别的性能不佳。已有方法在应对类别增量学习和类别不平衡问题方面存在不足。
### Innovation
本文提出了一种CLass-incremental Imbalance-aware 3DIS的统一框架，包括一个称为PLG的新型伪标签生成器和一个CBR方案。PLG通过冻结模型上的先前任务预测将监督扩展到已学习类别中，而CBR则通过从伪标签估计对象频率并动态调整训练偏差来解决偏见问题，无需访问历史数据。这种方法在具有挑战性的ScanNet200数据集上评估了三种增量场景，并在ScanNetV2的语义分割上进行了验证，取得了当前最佳结果。
### Conclusion
本文的方法在实例分割方面超越了现有工作的最高mAP分数16.76%，在语义分割上大约提高了30%的mIoU，表明其在频繁类和稀有类之间具有强大的泛化能力。代码可以在指定的网址找到。
## 422. `cs.CV` - 探索预测乳腺癌新辅助化疗病理完全缓解的术前MRI特征的附加价值 [PDF](https://arxiv.org/pdf/2511.17158), [HTML](https://arxiv.org/abs/2511.17158)
### Authors
Caroline Malhaire(LITO),Fatine Selhane,Marie-Judith Saint-Martin,Vincent Cockenpot,Pia Akl,Enora Laas,Audrey Bellesoeur,Catherine Ala Eddine,Melodie Bereby-Kahane,Julie Manceau,Delphine Sebbag-Sfez,Jean-Yves Pierga,Fabien Reyal,Anne Vincent-Salomon,Herve Brisse,Frederique Frouin
### Background
为了评估术前MRI描述符与乳腺癌对新辅助化疗路径学完全缓解(pCR)之间的关联，这项回顾性单中心研究包括了2016年至2020年接受新辅助化疗并有乳腺MRI的乳腺癌患者。研究通过分析MRI特征（如BI-RADS标准和T2加权MRI上的乳腺水肿评分）来探索与pCR相关的因素。利用单变量和多变量逻辑回归分析残余癌负荷与pCR之间的关联，并通过随机森林分类器训练来预测pCR。
### Innovation
研究发现非分叶边缘和单发病灶与pCR独立相关，并且将显著的MRI特征加入临床和生物学变量中，可以显著提高预测pCR的敏感性、特异性和精确性。这种融合临床和生物学预测因子（如TILs）及MRI特征的方法可以用于开发机器学习模型来识别对治疗无响应风险的患者，并考虑采用其他治疗策略以优化治疗结果。
### Conclusion
非分叶边缘和单发病灶是独立与pCR相关的因素，并且可以提高模型预测功能性乳腺癌对新辅助化疗的反应效果。这种方法结合临床生物学预测因子和术前MRI特征，可能有助于开发用于识别无响应患者的机器学习模型，以优化治疗策略。
## 423. `cs.CV` - FaCells. 教会机器线条语言：脸部构图属性得分分类 [PDF](https://arxiv.org/pdf/2102.11361), [HTML](https://arxiv.org/abs/2102.11361)
### Authors
Xavier Ignacio Gonzalez
### Background
研究通过将面部模型的内部信息转化为基于线条的艺术作品，利用深度学习方法（如双向LSTM）对面部特征进行预测，并将面部图像转换为适合XY绘图仪的向量素描。
### Innovation
提出了FaCells方法，将面部特征（如戴眼镜、头发卷曲、刘海等）转化为线条素描，并研究了绝对坐标对与相对坐标、旅行最短路径顺序等技术在生成素描顺序中的应用效果。研究表明，使用绝对坐标与旅行最短路径顺序以及全局平均读出的配置在性能上最佳。实验还展示了多标签训练在多个特征维度上的稳定性，并通过这些特征生成了FaCells，这是一种可视化的统计抽象。
### Conclusion
研究发现，通过这种配置生成的属性分数，在多个维度上表现良好，并且通过生成FaCells，展示了如何用线条艺术来表现面部特征。项目体现了数据、模型和论文之间的联系，同时承认标签的局限性和数据集的偏见。
## 424. `cs.CV` - MindShot: 通过转移跨个体先验和蒸馏频域知识的少量样本脑解码框架 [PDF](https://arxiv.org/pdf/2405.15278), [HTML](https://arxiv.org/abs/2405.15278)
### Authors
Shuai Jiang,Zhu Meng,Haiwen Li,Delong Liu,Fei Su,Zhicheng Zhao
### Background
脑解码旨在从大脑信号重构视觉刺激，近期利用功能性磁共振成像(fMRI)取得了较大进展，但仍面临个体差异显著和数据采集成本高的问题。大多数方法采用每人每模型的方式，极大限制了其应用范围。
### Innovation
本文设计了专门针对潜在临床场景的少量样本脑解码框架MindShot，提出了一种双阶段解码框架，既有多模态对比学习阶段的多个体预训练(MSP)，又有基于傅里叶变换的跨个体知识蒸馏(FKD)阶段。该框架在最大数据集上实现了高语义还原度的视觉重构，并且可将扫描时间减少99%。仅使用1.8%的功能磁共振成像-图像对即可达到83.6%的性能，超过了所有方法全集数据训练的77.4%的准确度。这使得大规模脑解码框架所需的训练数据量减少，有利于实际应用。
### Conclusion
MindShot框架实现了高语义还原度的大规模大脑解码视觉重构，仅需极少数据即可获得良好性能，潜力巨大，有助于减少扫描时间，促进实际应用。
## 425. `cs.CV` - Colo-ReID: 通过元学习实现结肠内镜息肉的辨别表示嵌入 [PDF](https://arxiv.org/pdf/2308.00929), [HTML](https://arxiv.org/abs/2308.00929)
### Authors
Suncheng Xiang,Chengfeng Zhou,Zhengjie Zhang,Shilun Cai,Dahong Qian
### Background
结肠内镜息肉再识别旨在从包含不同视角和不同摄像头拍摄的大量图片中匹配同一息肉。这在结肠癌的预防和治疗中发挥着重要作用。然而，传统的对象再识别方法通常直接使用在ImageNet数据集上训练的CNN模型，这种做法在结肠内镜数据集上往往导致不尽如人意的检索性能，因为两者存在较大的领域差异。此外，这些方法忽略了结肠内镜息肉数据集中类内或类间的同构或异构关系中的潜力，这在医学界仍然是一个开放的研究问题。
### Innovation
本文提出了一种简单而有效的方法，名为Colo-ReID，该方法基于元学习策略，即使在小样本场景中也能帮助模型学习更广泛和更具鉴别性的知识。在此基础上，引入了一种动态的元学习调节机制MLR，以进一步提高息肉再识别的性能。实验结果表明，Colo-ReID在息肉再识别任务中的mAP性能比第二优方法高出2.3%。
### Conclusion
我们的实验结果表明，Colo-ReID在息肉再识别任务中持续超过第二优方法，mAP性能提高了2.3%。我们的源代码也已公开可用。
## 426. `cs.CV` - HDCompression: Hybrid-Diffusion Image Compression for Ultra-Low Bitrates [PDF](https://arxiv.org/pdf/2502.07160), [HTML](https://arxiv.org/abs/2502.07160)
### Authors
Lei Lu,Yize Li,Yanzhi Wang,Wei Wang,Wei Jiang
### Background
传统的基于学习的图像压缩（LIC）易产生严重伪影，而生成型向量量化（VQ）建模由于生成先验与特定输入的不匹配，导致低保真度。本文分析了在这两个方向上面临的挑战。
### Innovation
提出了一种双流框架---Hybrid-Diffusion Image Compression（HDCompression），结合生成型VQ建模和扩散模型，以及传统LIC，以达到高保真度和高感知质量。不同于之前的混合方法直接使用预训练LIC模型从高度量化隐藏空间生成低质量的信息，本方法使用扩散模型从真实输入中提取高质量的保真信息，增强系统性能。此外，扩散模型基于密集的代表性向量（DRV），具有轻量级且简易的采样调度。
### Conclusion
大量实验表明，HDCompression在定量指标和定性可视化方面都优于传统LIC、生成型VQ建模和混合框架，提供了一种平衡的超低比特率鲁棒压缩性能。
## 427. `cs.CV` - MonoGSDF：探索用于高斯绘射引导的隐式曲面重建的单目几何线索 [PDF](https://arxiv.org/pdf/2411.16898), [HTML](https://arxiv.org/abs/2411.16898)
### Authors
Kunyi Li,Michael Niemeyer,Zeyu Chen,Nassir Navab,Federico Tombari
### Background
在3D视觉领域，从单目图像准确生成网格仍然是一个关键挑战。虽然最先进的三维高斯点云（3DGS）方法在基于光栅化渲染的合成逼真视图方面表现出色，但它们依赖于稀疏的明确几何元素，这限制了它们恢复封闭且拓扑上一致的3D结构的能力。
### Innovation
本文提出了MonoGSDF方法，这是一种结合基于高斯的几何元素与神经体素场（SDF）的新型方法，以实现高质量的重建。训练过程中，SDF指导高斯分布的空间分布；而在推理过程中，高斯分布作为先验知识来重建表面，从而消除了对密集Marching Cubes变换的需求。为处理任意规模的场景，文中提出了稳健的一般化策略。多分辨率训练方案进一步细化细节重构质量。通过使用现成的几何指示器，单目几何线索增强了重构效果。
### Conclusion
在真实数据集上的实验表明，MonoGSDF在保持效率的同时优于先有方法。
## 428. `cs.CV` - REArtGS：基于几何与运动约束的3D高斯体绘制重建和生成 articulated objects [PDF](https://arxiv.org/pdf/2503.06677), [HTML](https://arxiv.org/abs/2503.06677)
### Authors
Di Wu,Liu Liu,Zhou Linli,Anran Huang,Liangtu Song,Qiaojun Yu,Qi Wu,Cewu Lu
### Background
作为人在生活中常见的实体， articulated objects 在各种应用中都有其 3D 表征需求。然而，目前的方法在实现 articulated objects 的高保真纹理表面重建和动态生成方面仍存在挑战。
### Innovation
提出了 REArtGS，这是一种新颖的框架，通过引入额外的几何和运动约束来改进 3D 高斯原始值，实现 articulated objects 的真实表面重建和生成。该框架首先通过无偏的符号距离场（SDF）指导来正则化高斯不透明度场，增强几何约束并提高表面重建质量；然后建立受限于骨架结构的变形场，实现未见状态下表面网格的无监督生成。
### Conclusion
在合成和真实数据集上的广泛实验表明，该方法可实现给定状态下的高质量纹理表面重建，并可实现未见状态下高保真表面生成。
## 429. `cs.CV` - 毫秒级多视角多人全身人体姿态三角化：RapidPoseTriangulation [PDF](https://arxiv.org/pdf/2503.21692), [HTML](https://arxiv.org/abs/2503.21692)
### Authors
Daniel Bermuth,Alexander Poeppel,Wolfgang Reif
### Background
多视角影像和姿态估计的整合在计算机视觉应用中是一个重大的进步，为理解和分析人类运动提供了新的可能性。现有的研究多关注于提高多视角多个人的姿态估计速度和泛化能力。
### Innovation
该研究提出了一种新的算法，提高了多视角多人姿态估计的速度和泛化能力。该方法适用于全身姿态估计，能够捕捉到面部表情到手指动作的细节。此外，该方法还可以适应不同的环境，具有强大的跨未见过的数据集和配置性能。
### Conclusion
本研究的成果提供了良好的泛化能力和快速的三角化速度，公开所有的研究数据支持该领域的进一步发展。
## 430. `cs.CV` - FAR：IMC友好的保留函数的注意力替换 [PDF](https://arxiv.org/pdf/2505.21535), [HTML](https://arxiv.org/abs/2505.21535)
### Authors
Yuxin Ren,Maxwell D Collins,Miao Hu,Huanrui Yang
### Background
虽然Transformer在现代视觉和语言模型中占主导地位，但它们的注意力机制由于需要密集的激活到激活乘法和非局部的内存访问，在基于ReRAM的加速器上处于非优化状态，导致了明显的延迟和带宽开销。为了应对这一不匹配，研究提出了一种FAR（Function-preserving Attention Replacement）框架，旨在将预训练好的DeiTs中的所有注意力机制替换为与IMC（In-memory Computing）数据流天然兼容的顺序模块。
### Innovation
FAR框架通过区块式蒸馏将自我注意力替换为多头双方向LSTM架构，以保留功能等价性并允许线性时间计算和局部权重重用。此外，还引入了对FAR模型的结构化剪枝，使其能够灵活适应资源受限的IMC阵列，同时保持功能等同性。
### Conclusion
FAR在Imagenet和多个下游任务上保持了与基于注意力的模型相当的准确率，同时减少了参数量和延迟。进一步的分析表明FAR保留了由注意力机制学习到的语义标记关系，提高了计算效率，显示出在基于IMC的边缘加速器上执行高效Transformer推理的潜力。
## 431. `cs.CV` - ORV: 4D Occupancy-centric Robot Video Generation [PDF](https://arxiv.org/pdf/2506.03079), [HTML](https://arxiv.org/abs/2506.03079)
### Authors
Xiuyu Yang,Bohan Li,Shaocong Xu,Nan Wang,Chongjie Ye,Zhaoxi Chen,Minghan Qin,Yikang Ding,Zheng Zhu,Xin Jin,Hang Zhao,Hao Zhao
### Background
近期的人体智能面临数据稀缺的问题，而传统的模拟器则缺乏视觉真实性。可控视频生成正在兴起，作为潜在的数据引擎，但现有的基于动作条件的方法仍然存在局限性：生成的视频在保真度和时间一致性方面有限，与控制不匹配，并且通常局限于单视角设置。这些问题被归因于稀疏控制输入和密集像素输出之间的表示差距。
### Innovation
引入了ORV，一种以4D占用为中心的框架，结合了动作先验与占用衍生的视觉先验。具体而言，通过Action-Expert AdaLN调制将分块的7-DoF动作与视频潜在变量对齐，在生成过程中注入4D语义占用的2D渲染作为软指导。此外，提出了一种名为ORV-Data的大规模、高质量4D语义占用数据集，用于机器人操作。
### Conclusion
ORV在BridgeV2、DROID和RT-1上改进了视频生成质量和可控性，相较于最先进的方法实现了18.8%更低的FVD，同时视觉规划和策略学习的成功率分别提高了3.5%和6.4%。ORV还可以支持多视角一致合成，并在显著的领域差距下实现了模拟到现实的迁移。
## 432. `cs.CV` - QuantFace: Efficient Quantization for Face Restoration [PDF](https://arxiv.org/pdf/2506.00820), [HTML](https://arxiv.org/abs/2506.00820)
### Authors
Jiatong Li,Libo Zhu,Haotong Qin,Jingkai Wang,Linghe Kong,Guihai Chen,Yulun Zhang,Xiaokang Yang
### Background
扩散模型在面部恢复方面取得了显著的性能，但其计算量大，阻碍了这些模型的广泛应用。
### Innovation
提出了一种新颖的低比特量化框架QuantFace，将全精度（即32比特）的权重和激活量化为4到6比特。通过旋转-缩放通道平衡保留原始数据信息，并提出了Quantization-Distillation Low-Rank Adaptation（QD-LoRA）联合优化量化和蒸馏性能。此外，还提出了一种自适应比特分配策略，将其形式化为结合量化误差和感知度量的整数规划问题，以找到满意的资源配置。
### Conclusion
在合成和现实数据集上的广泛实验表明，QuantFace在6比特和4比特下有效，显著优于最近的低比特量化方法。
## 433. `cs.CV` - 通用且可重新照明的高斯散点表示法用于人体视角合成 [PDF](https://arxiv.org/pdf/2505.21502), [HTML](https://arxiv.org/abs/2505.21502)
### Authors
Yipengjing Sun,Shengping Zhang,Chenyang Wang,Shunyuan Zheng,Zonglin Li,Xiangyang Ji
### Background
现有的方法要么依赖于每个角色的优化，要么忽视物理约束，导致在不同光照条件下难以合成高质量的人体新颖视角。
### Innovation
文章提出了GRGS框架，这是一种通用且可重新照明的3D高斯人体新颖视角合成方法。该方法通过前馈、全监督策略，将多视角的2D观察数据投影到3D高斯表示中，同时引入了LGR模块以恢复在不同光照条件下的准确几何结构，并提出PGNR模块结合神经预测和物理着色，支持可编辑的重新照明和间接照明。
### Conclusion
广泛实验表明，GRGS在视觉质量、几何一致性以及不同角色和光照条件下的泛化能力方面表现优秀。
## 434. `cs.CV` - 在LVLM中的损失导向排名方法的自动视觉提示 [PDF](https://arxiv.org/pdf/2506.16112), [HTML](https://arxiv.org/abs/2506.16112)
### Authors
Yuan Zhang,Chun-Kai Fan,Tao Huang,Ming Lu,Sicheng Yu,Junwen Pan,Kuan Cheng,Qi She,Shanghang Zhang
### Background
受大型语言模型（LLMs）中的文本提示启发，视觉提示已被探索以增强大型视觉语言模型（LVLMs）的推理能力。当前方法手动设计启发式视觉提示，如在原始输入图像上叠加文本查询引导的注意力热图。然而，手动设计有效的提示具有挑战性且耗时，并且往往无法充分探索不同视觉提示的好处，导致性能不最优。
### Innovation
提出了名为AutoV的方法，该方法学习从给定的文本查询和输入图像中自动选择最佳的视觉提示。为训练AutoV，开发了一个自动数据采集和标注管道，该管道使用预训练的LVLM评估多种视觉提示。通过输入一组视觉提示并根据模型生成的预测损失对其进行排名，使用排名作为监督信号来训练AutoV，使其能够自动从多种视觉提示中选择最佳视觉提示用于LVLMs。实验表明，AutoV提高了多种LVLMs在多个图像理解任务中的性能。
### Conclusion
AutoV提升了多种LVLMs在多个图像理解任务中的性能，例如，使用AutoV的LaLaVA-OV在VizWiz上获得了10.2%的准确率提升，而AutoV使Qwen2.5-VL在MMMU上提高了3.8%，突显了其作为最佳视觉提示方法的潜力。
## 435. `cs.CV` - 使用生成型多模态大语言模型的通用视频时域定位 [PDF](https://arxiv.org/pdf/2506.18883), [HTML](https://arxiv.org/abs/2506.18883)
### Authors
Zeqian Li,Shangzhe Di,Zhonghua Zhai,Weilin Huang,Yanfeng Wang,Weidi Xie
### Background
现有的视频时域定位方法通常局限于特定的视频领域或时间段，缺乏普遍的应用能力。研究人员需要开发一种能够跨多种视点、类型和长度的视频，并有效处理复杂语言查询的通用模型。
### Innovation
论文提出了UniTime，一种利用生成性多模态大语言模型（MLLMs）的强大视觉-语言理解能力的通用视频时域定位模型。其创新点包括：(i) 将时间戳信息融入视频令牌中，以引导强大的MLLMs进行视频时域定位。(ii) 通过适应性帧缩放训练模型以处理不同输入粒度的视频，从而实现对短视频和长视频的稳健时间定位。(iii) 实验结果表明，在五个公开的视频时域定位基准数据集上，UniTime在零样本和数据集特定微调设置中均优于现有方法。
### Conclusion
UniTime作为一种初步时刻检索器，显著提升了长视频问答的准确性，证明了其在复杂视频理解任务中的价值。
## 436. `cs.CV` - TrackGS: 使用全局轨迹约束优化无COLMAP 3D 高斯散点图 [PDF](https://arxiv.org/pdf/2502.19800), [HTML](https://arxiv.org/abs/2502.19800)
### Authors
Dongbo Shi,Shen Cao,Lubin Fan,Bojian Wu,Jinhui Guo,Ligang Liu,Renjie Chen
### Background
尽管3D高斯散点图（3DGS）提供了出色的渲染质量，但它依赖于准确的预计算摄像机参数，这仍然是一个显著的局限。现有的无COLMAP方法依赖于局部约束，在复杂场景中效果不佳。
### Innovation
本文的关键创新在于利用特征轨迹建立全局几何约束，从而同时优化摄像机参数和3D高斯分布。具体来说，作者介绍了：(1) 轨迹约束下的高斯分布，作为几何锚点；(2) 提出了新型2D和3D轨迹损失，以确保多视图一致性；(3) 为摄像机内参数优化推导出了可微分公式。
### Conclusion
大量实验结果表明，本文方法在具有挑战性的现实世界和合成数据集上表现出最先进的性能，与之前的方法相比，显著降低了姿态误差，同时保持了优越的渲染质量。我们的方法消除了需要预处理的需求，从而使3DGS更容易应用于实际应用中。
## 437. `cs.CV` - 通过光谱-空间不确定性解耦的开放集域泛化用于高光谱图像分类 [PDF](https://arxiv.org/pdf/2506.09460), [HTML](https://arxiv.org/abs/2506.09460)
### Authors
Amirreza Khoshbakht,Erchan Aptoula
### Background
该论文背景描述了开放域泛化（OSDG）策略，该策略旨在解决识别未知类别和跨未见过的域泛化的双重挑战，而无需在训练过程中使用目标数据。论文主题集中于高光谱图像分类中的OSDG框架，该框架利用光谱-空间不确定性解耦机制，应对域偏移对光谱、空间以及结合特征提取路径的影响。
### Innovation
该研究的创新之处在于提出了一个基于光谱-空间不确定性解耦机制的OSDG框架。该框架通过证据深度学习（Evidential Deep Learning）方法处理域偏移，适应性选择每个样本的最可靠特征提取途径，并与频域特征提取、双通道残差网络和基于证据的不确定性量化相结合，以实现域不变的特征表示学习。
### Conclusion
实验表明，该框架在三个跨场景高光谱数据集上的性能与最先进的域适应方法相当，即使不使用目标数据也能保持较高的未知类别拒绝率和已知类别的准确率。该框架的实现将在接受后公开可用。
## 438. `cs.CV` - ISS-Geo142：国际空间站宇航员摄影地理定位基准 [PDF](https://arxiv.org/pdf/2504.21194), [HTML](https://arxiv.org/abs/2504.21194)
### Authors
Vedika Srivastava,Hemant Kumar Singh,Jaisal Singh
### Background
尽管国际空间站（ISS）在拍摄时的位置可以精确知道，但这些拍摄的照片所展示的具体地球位置并不是直接地理参考的，因此自动化的地理位置定位并不容易。文章介绍了ISS-Geo142，这是一个由142张照片和相关元数据及手工确定的地理位置构成的基准数据集，涵盖了不同的空间规模和场景类型。
### Innovation
文章提出并评估了三种地理定位管道：一种基于神经网络的方法（NN-Geo）使用VGG16特征和地图推导的区域兴趣（AOIs）的交叉相关，一种基于比例不变特征变换（SIFT-Match）的方法利用窗口滑动和高分辨率AOIs的特征匹配，以及一种基于AI系统TerraByte，该系统围绕具有视觉能力的GPT-4模型，可以同时处理图像内容和ISS坐标。这些方法为未来的ISS照片地理定位工作提供了具体的、历史背景下的基准。
### Conclusion
ISS-Geo142和这三种管道提供了一个具体的、历史上有依据的基准，用于未来ISS图像地理定位的工作。文章在介绍这些方法和实验的同时，还将其置于后续的跨视图地理定位和遥感视觉-语言模型的发展背景下。
## 439. `cs.CV` - 使视觉对准语言：无标注的多模态知识图构建以增强LLM推理 [PDF](https://arxiv.org/pdf/2503.12972), [HTML](https://arxiv.org/abs/2503.12972)
### Authors
Junming Liu,Siyuan Meng,Yanting Gao,Song Mao,Pinlong Cai,Guohang Yan,Yirong Chen,Zilin Bian,Ding Wang,Botian Shi
### Background
大型语言模型（LLMs）在多模态推理方面面临着不完整知识和幻觉错误的问题，这些挑战仅部分可以通过文本知识图谱（KGs）得到缓解，因为它们的内容是孤立的。多模态知识图谱（MMKGs）有望增强跨模态的理解能力，但由于手工文本注释的语义狭窄和视觉语义实体链接中的固有噪声，其实际构建受到阻碍。
### Innovation
本文提出了一种新的视觉对准到语言集成知识图（VaLiK），这是一种通过跨模态信息补充来增强LLMs推理的方法。该方法利用预训练的视觉-语言模型（VLMs）将图像特征与文本对齐，并通过开发一种跨模态相似度验证机制来量化语义一致性，并有效过滤掉特征对齐过程中引入的噪声。即使没有手动标注的图像描述，这些精炼后的描述也足够构建MMKG。
### Conclusion
实验结果表明，与传统MMKGs构建方法相比，我们的方法在存储效率方面具有显著的优势，同时保持了直接的实体到图像链接能力。使用我们添加了VaLiK的LLMs在多模态推理任务中比之前的最先进的模型表现更优。我们的代码已发布于 this https URL。
## 440. `cs.CV` - OpenDriveVLA:朝向基于大型视觉语言行动模型的端到端自动驾驶 [PDF](https://arxiv.org/pdf/2503.23463), [HTML](https://arxiv.org/abs/2503.23463)
### Authors
Xingcheng Zhou,Xuyuan Han,Feng Yang,Yunpu Ma,Volker Tresp,Alois Knoll
### Background
本文介绍了OpenDriveVLA，一种基于开源大型语言模型设计的端到端自动驾驶视觉语言行动模型。该模型通过利用2D和3D实例感知视觉表示、 ego车辆状态和语言指令等多种模态输入生成空间上定位的驾驶动作。此外，为了弥合驾驶视觉表示与语言嵌入之间的模态差异，引入了一种分层视觉语言对齐过程，将2D和3D结构化视觉标记投影到统一的语义空间中。此过程有助于模型捕获轨迹规划中至关重要的细粒度空间依赖性和行为意识动力学。
### Innovation
本文的创新在于通过引入分层视觉语言对齐过程和结构化代理环境ego交互建模，使模型能够细粒度地捕捉空间依赖性和行为动态，这对可靠的轨迹规划至关重要。实验结果表明，OpenDriveVLA在nuScenes数据集上的开放环轨迹规划和驾驶相关问答任务中达到了最先进的成果。
### Conclusion
广泛的实验证明，OpenDriveVLA在开放环轨迹规划和驾驶相关问答任务中获得了最先进的结果。定性分析进一步证明了其跟随高层次驾驶指令以及在复杂场景下生成轨迹的能力，突显了其在下一代端到端自动驾驶中的潜力。
## 441. `cs.CV` - 语义ICP：非刚性多器官点云配准的迭代最近点法 [PDF](https://arxiv.org/pdf/2503.00972), [HTML](https://arxiv.org/abs/2503.00972)
### Authors
Wanwen Chen,Qi Zeng,Carson Studders,Jamie J.Y. Kwon,Emily H.T. Pang,Eitan Prisman,Septimiu E. Salcudean
### Background
点云配准在计算机辅助干预(CAI)中至关重要。尽管已经开发了基于学习的点云配准方法，但由于普适性和可解释性较差，其在临床应用中受到限制。因此，经典的点云配准方法，例如最临近点算法（ICP），仍在CAI中广泛应用。但ICP方法未能考虑以下两点：（1）点具有清晰的语义意义，即每个点都与特定的解剖标签相关联；（2）配准所需的变形需遵循生物力学能量约束。
### Innovation
本文提出了一种新颖的非刚性语义ICP（SemICP）方法，能够处理多点标签，并使用线性弹性能量正则化。通过使用语义标签，改进了最近点匹配的鲁棒性，并提出了一个包含显式生物力学能量正则化的新的点云变形表示。我们的实验结果表明，该方法在几个数据集上大幅提高了Hausdorff距离和平均表面距离，与其它点云配准方法相比。此外，将深度学习分割模型与我们的配准管道集成，能够有效对齐US和MR点云。
### Conclusion
本研究提出了一种新的语义ICP方法，能够处理多点标签，并且通过使用语义信息和生物力学能量正则化，显著提高了点云配准的精度。该方法在多个数据集上的实验结果表明其有效性和鲁棒性，特别是在结合深度学习分割模型后，能够有效实现US和MR点云的对齐。
## 442. `cs.CV` - CleverDistiller: 简单且空间一致的跨模态知识蒸馏 [PDF](https://arxiv.org/pdf/2503.09878), [HTML](https://arxiv.org/abs/2503.09878)
### Authors
Hariprasath Govindarajan,Maciej K. Wozniak,Marvin Klingner,Camille Maurice,B Ravi Kiran,Senthil Yogamani
### Background
视觉基础模型（VFMs）如DINO推动了基于2D相机的感知 paradigm 的转变，促进了通用特征的提取以支持多个下游任务。最近的工作引入了自我监督的跨模态知识蒸馏（KD）来将这些强大的泛化能力转移到基于LiDAR的3D模型中，但这些方法要么依赖非常复杂的蒸馏损失，要么生成伪语义图，要么仅将KD限制为用于语义分割的特征。研究指出，当前方法或依赖复杂的设计选择，或依赖伪语义图，或仅专注于用于语义分割的特征，这些限制了它们的泛化能力和应用范围。
### Innovation
CleverDistiller 提出了一种自我监督的跨模态2D到3D知识蒸馏框架，该框架采用了简单但有效的设计选择。与对比方法依赖于复杂的损失设计选择不同，该方法使用直接的特征相似度损失结合多层感知器（MLP）投影头，从而使3D网络能够学习投影过程中的复杂语义依赖关系。此外，引入了一项辅助的自我监督空间任务，即占用预测，以增强从视觉基础模型通过KD获得的语义知识，并提高3D空间推理能力。实验表明，CleverDistiller 在语义分割和3D目标检测（3DOD）上达到了最先进的性能，尤其在使用少量数据进行微调时，展示了我们的简单而强大的KD策略的有效性。
### Conclusion
实验结果表明，CleverDistiller 在标准自动驾驶基准测试中，针对2D到3D的知识蒸馏实现了在语义分割和3D对象检测方面的最佳性能，尤其是在微调数据量极低的情况下，进一步证明了我们的简单而强大的知识蒸馏策略的有效性。
## 443. `cs.CV` - 基于SVD特征分解的无训练风格个性化 [PDF](https://arxiv.org/pdf/2507.04482), [HTML](https://arxiv.org/abs/2507.04482)
### Authors
Kyoungmin Lee,Jihun Park,Jongmin Gim,Wonhyeok Choi,Kyumin Hwang,Jaeyeul Kim,Sunghoon Im
### Background
研究旨在通过提出一种在推理阶段工作的无训练框架，实现个性化图像风格生成。现有的图像风格生成方法可能无法在保持语义一致性和减少内容泄露的同时，精确地生成个性化风格化的图像。
### Innovation
本文提出了一种通过尺度级自回归模型，在推理阶段进行风格个性化图像生成的无训练框架。关键创新在于使用主成分特征融合（Principal Feature Blending）模块，通过SVD基于的特征重建对风格进行精确调制；以及结构性注意纠正（Structural Attention Correction）模块，通过内容引导的注意力纠正来稳定结构一致性。这些模块在无需额外训练的情况下，实现了与调整基线竞争的风格保真度和提示保真度，同时提供了更快的推理速度和更好的部署灵活性。
### Conclusion
本文提出的方法在无需额外训练的情况下，展示了与调整基线竞争的风格保真度和提示保真度，同时具有更快的推理速度和更好的部署灵活性。研究结果表明，这种方法在面部图像生成和背景移除等应用场景中具有广泛的应用潜力。
## 444. `cs.CV` - Composed Object Retrieval: Object-level Retrieval via Composed Expressions [PDF](https://arxiv.org/pdf/2508.04424), [HTML](https://arxiv.org/abs/2508.04424)
### Authors
Tong Wang,Guanyu Yang,Nian Liu,Zongyan Han,Jinxing Zhou,Salman Khan,Fahad Shahbaz Khan
### Background
在多模态系统中，基于用户的意图检索精细视觉内容仍然是一项挑战。当前的组合图像检索(CIR)方法虽然结合了参考图像和检索文本，但仅限于图像级别的匹配，无法定位具体对象。
### Innovation
提出了组合对象检索(COR)这一新任务，超越了图像级别的检索实现了对象级别的精度，通过结合参考对象和检索文本组成的表达式来进行目标对象的检索和分割。COR还面临着检索灵活性的巨大挑战，要求系统能够识别满足组成表达式的任意对象，同时避免场景中具有语义相似但无关的负对象。
### Conclusion
构建了COR127K，这是第一个包含来自408个类别中不同语义变换的127,166个检索三元组的大规模COR基准数据集。同时还提出了COR模型，一种统一的端对端模型，整合了参考区域编码、自适应的视觉文本交互和区域级别对比学习。大量的实验证明，COR模型在基础类别和新类别上都显著优于现有模型，为这项具有挑战性的任务设立了简单有效的基准，并为精细多模态检索研究开辟了新方向。模型和数据集将在指定的URL公开发布。
## 445. `cs.CV` - MOCHA: 多模态对象感知跨架构对齐 [PDF](https://arxiv.org/pdf/2509.14001), [HTML](https://arxiv.org/abs/2509.14001)
### Authors
Elena Camuffo,Francesco Barbato,Mete Ozay,Simone Milani,Umberto Michieli
### Background
个性化对象检测旨在适应一般检测器以仅从少量样本中识别用户特定实例。轻量级模型在这种设置中往往表现不佳，因为它们缺乏较强的语义先验，而大型视觉语言模型（VLM）虽然在对象级别的理解方面表现出色，但由于计算需求高，不适合实时或设备端应用。
### Innovation
MOCHA（多模态对象感知跨架构对齐）是一种知识蒸馏框架，将冻结的VLM教师端的多模态区域级知识迁移到轻量级的纯视觉检测器中。MOCHA通过融合视觉和文本教师的嵌入并通过双重目标损失函数指导学生训练，该损失函数确保区域间的局部对齐和全局关系一致性。这一过程使得可以高效地转移语义，而无需对教师端进行修改或在推理时输入文本。
### Conclusion
MOCHA在四个严格少样本基准测试中表现出色，持续优于先前的基线方法，平均提升10.1%，且在推理成本方面影响较小。
## 446. `cs.CV` - EatGAN: 一种边缘注意力引导的生成对抗网络在单图像超分辨率中的应用 [PDF](https://arxiv.org/pdf/2509.14550), [HTML](https://arxiv.org/abs/2509.14550)
### Authors
Penghao Rao,Tieyong Zeng
### Background
图像处理中的单图像超分辨率（SISR）是一个重要的任务，旨在提高成像系统的分辨率。近年来，基于深度学习的SISR取得了显著的进步，并获得了令人鼓舞的结果。尽管基于生成对抗网络（GAN）的模型在感知质量方面表现出色，但它们在重建现实的高频细节和实现稳定训练方面仍然存在困难。
### Innovation
我们引入了一种边缘注意力引导的生成对抗网络（EatGAN），这是一类同时在生成器中显式和隐式利用边缘先验的第一种基于GAN的SISR模型。该模型创新地提出了基于通道 affine 和空间门控的归一化边缘注意力（NEA）机制，将边缘先验转化为轻量级、可学习的调制参数，多次注入并融合到（ii）边缘引导的混合残差块中，逐步在不同尺度上确保结构一致性；并且还结合了像素、感知、边缘梯度和对抗性损失的复合生成器目标。
### Conclusion
实验结果显示，该模型在失真导向基准和感知导向基准上均达到了最先进的性能。特别地，该模型在Manga 109数据集上实现了40.87 dB和0.073（LPIPS），表明从被动指导到控制调制原语，重塑图像先验可以为高保真超分辨率提供实用的道路。
## 447. `cs.CV` - 一种用于点云3D物体检测的统一体素扩散模块 [PDF](https://arxiv.org/pdf/2508.16069), [HTML](https://arxiv.org/abs/2508.16069)
### Authors
Qifeng Liu,Dawei Zhao,Yabo Dong,Linzhi Shang,Liang Xiao,Juan Wang,Kunkong Zhao,Dongming Lu,Qi Zhu
### Background
近期点云物体检测的研究越来越多地采用基于Transformer和状态空间模型（SSMs）的方法，证明了其强大的性能。然而，这些模型中的体素表示由于其串行处理特性，在输入和输出维度上需要严格的连续性，限制了卷积操作通常提供的空间扩散能力，这对物体检测的准确性产生了显著影响。
### Innovation
受基于CNN的物体检测架构的启发，本文提出了一个新的体素扩散模块（VDM），旨在增强点云数据中的体素级表示和扩散能力。VDM采用稀疏3D卷积、子流形稀疏卷积和残差连接组成，通过稀疏3D卷积确保计算效率地扩散体素特征，通过聚集细粒度的空间信息来强化体素级特征表示。增强后的体素特征可无缝集成到主流的Transformer或SSM基础上的检测模型中，实现精确的物体分类和定位，突显了该方法的通用性。
### Conclusion
通过将VDM嵌入到Transformer基和SSM基模型中，本文在多个基准数据集上进行了评估，实验结果表明，相较于基线模型，我们的方法能一致地提高检测准确性。具体来说，基于VDM的SSM在Waymo上达到74.7 mAPH（L2），在nuScenes上达到72.9 NDS，在Argoverse 2上达到42.3 mAP，并在ONCE上达到67.6 mAP，实现了所有数据集上的最新性能。我们的代码将公开提供。
## 448. `cs.CV` - Lung-DDPM+: 使用扩散概率模型的高效胸腔CT图像合成 [PDF](https://arxiv.org/pdf/2508.09327), [HTML](https://arxiv.org/abs/2508.09327)
### Authors
Yifan Jiang,Ahmad Shariftabrizi,Venkata SK. Manem
### Background
生成式人工智能（AI）在各个领域发挥着重要作用。利用其生成高质量和多样化的合成数据的能力，生成式AI广泛应用于诊断任务，例如使用计算机断层扫描（CT）进行肺癌诊断。然而，现有的肺癌诊断生成模型效率低、解剖精度不足，限制了它们在临床中的应用。为了解决这些问题，我们提出了Lung-DDPM+，这是对之前模型Lung-DDPM的改进版本。该方法是一种由结节语义布局引导的去噪扩散概率模型（DDPM），并通过肺部DPM-加速器加速，能够在专注于病灶区域的同时实现采样效率和质量之间的更好权衡。
### Innovation
Lung-DDPM+ 是一种由结节语义布局引导的去噪扩散概率模型（DDPM），并通过肺部DPM-加速器加速。它能够在专注于病灶区域的同时，实现比Lung-DDPM更高的采样效率和质量。在LIDC-IDRI公共数据集上的评估结果表明，与Lung-DDPM相比，Lung-DDPM+采样效率提升了14倍，浮点运算每秒（FLOPs）降低了8倍，GPU内存消耗降低了6.8倍，同时在两个下游分割任务中，其样本质量与Lung-DDPM和其他最先进的（SOTA）生成模型保持相当。
### Conclusion
实验结果表明，Lung-DDPM+能够有效生成含有肺结节的高质量胸腔CT图像，突显了它在更广泛的应用中的潜力，如肿瘤合成和医学影像中的病灶生成。源代码和预训练模型可在指定的网页上获取。
## 449. `cs.CV` - LinVideo：面向高效视频生成的O(n)注意后训练框架 [PDF](https://arxiv.org/pdf/2510.08318), [HTML](https://arxiv.org/abs/2510.08318)
### Authors
Yushi Huang,Xingtong Ge,Ruihao Gong,Chengtao Lv,Jun Zhang
### Background
视频扩散模型（DMs）能够生成高质量的视频，但其计算成本随序列长度呈平方级增长，因为自我注意机制复杂性为平方。虽然线性注意可以降低计算量，但完全替换平方注意需要昂贵的预训练，这是因为线性注意的表达能力有限以及视频生成中的时空建模复杂性。
### Innovation
提出了一种高效的数据无关后训练框架LinVideo，它在保留原始模型性能的前提下，用线性注意替代目标数量的自我注意模块。首先观察到不同层的可替换单元有显著差异，将层的选择问题建模为二元分类问题，并提出选择性转移方法，自动生成并逐步将层转换为线性注意，影响最小。此外，为克服现有目标在这传输过程中的无效率和低效率，引入任意时间分布匹配（ADM）目标，通过在采样轨迹的任何时间步长上对样本分布进行对齐，解决了此过程中的目标问题，且高效且恢复了模型性能。
### Conclusion
大量实验表明，该方法在保持生成质量的同时实现了1.25-2.00倍的加速，并且我们的4步提炼模型进一步实现了15.92倍的延迟降低，同时视觉质量下降极小。
## 450. `cs.CV` - AVATAR: 基于强化学习在视频上进行视觉、听觉和推理 [PDF](https://arxiv.org/pdf/2508.03100), [HTML](https://arxiv.org/abs/2508.03100)
### Authors
Yogesh Kulkarni,Pooyan Fazli
### Background
多模态长时间视频推理具有挑战性，因为需要在不同时空尺度上精确融合和对齐各种模态。现有方法如Group Relative Policy Optimization（GRPO）虽然在该领域表现有希望，但存在三大局限：（1）由于其基于策略的训练设计导致数据利用率低，（2）优势消失问题，同一组内相同或非常相似的奖励导致零价值的优势，（3）统一的信用分配不能强调关键推理步骤。因此，需要一种新的框架来克服这些限制。
### Innovation
AVATAR通过两个核心组件解决这些限制：（1）一种离策略训练架构，提高样本效率并解决范式衰减问题，通过利用更多样化的奖励重新利用以往经验；（2）一种新的信用分配策略——时序优势重塑（TAS），在学习过程中强调关键推理阶段。AVATAR在各种基准测试中表现出色，超越了Qwen2.5-Omni基线，在MMVU、OmniBench 和 Video-Holmes上的性能分别提高了5.4%、4.9% 和 4.5%，且其样本效率为5倍，只需要80%的生成完成任务就能达到目标性能。
### Conclusion
AVATAR通过离策略训练架构和时序优势重塑策略，有效提高了多模态长时间视频推理的效率和效果，显著提升了性能并降低了样本需求，为该领域提供了创新解决方案。
## 451. `cs.CV` - PaddleOCR-VL：通过一种0.9B极紧凑的视觉语言模型增强多语言文档解析 [PDF](https://arxiv.org/pdf/2510.14528), [HTML](https://arxiv.org/abs/2510.14528)
### Authors
Cheng Cui,Ting Sun,Suyin Liang,Tingquan Gao,Zelun Zhang,Jiaxuan Liu,Xueqing Wang,Changda Zhou,Hongen Liu,Manhui Lin,Yue Zhang,Yubo Zhang,Handong Zheng,Jing Zhang,Jun Zhang,Yi Liu,Dianhai Yu,Yanjun Ma
### Background
目前存在一些用于文档解析的模型，但它们通常是资源密集型且无法支持多种语言，尤其是对于复杂元素（如文本、表格、公式和图表）的识别能力不足。因此，亟需一个既能支持多种语言，又能高效处理复杂文档元素的技术。
### Innovation
本研究提出了PaddleOCR-VL，这是一个专为文档解析设计的高效模型，特别是PaddleOCR-VL-0.9B，这是一种紧凑但强大的视觉语言模型。该模型结合了NaViT风格的动态分辨率视觉编码器和ERNIE-4.5-0.3B语言模型，能够准确识别元素。PaddleOCR-VL能够支持109种语言，并在页级文档解析和元素级识别方面表现出色，同时保持低资源消耗。通过广泛使用的公共基准和内部基准进行全面评估，PaddleOCR-VL在多个方面均达到了最先进的技术水平，显著优于现有解决方案。
### Conclusion
PaddleOCR-VL由于其在多种语言支持、高性能解析和低资源消耗方面的优势，使其在实际应用场景中部署尤为理想。
## 452. `cs.CV` - ID-Crafter: VLM-Grounded Online RL for Compositional Multi-Subject Video Generation [PDF](https://arxiv.org/pdf/2511.00511), [HTML](https://arxiv.org/abs/2511.00511)
### Authors
Panwang Pan,Jingjing Zhao,Yuchen Lin,Chenguo Lin,Chenxin Li,Hengyu Liu,Tingting Shen,Yadong MU
### Background
虽然在高保真视频合成方面取得了显著进展，但当前的方法在有效地集成来自多个主体的身份信息时往往不尽如人意。这导致了语义冲突和身份及互动保存效果不佳，限制了控制性和可应用性。
### Innovation
本文提出了ID-Crafter框架，该框架通过结合三个关键组件来解决这一问题：（i）一种层次化身份保留注意力机制，逐步在单主体内、跨主体和跨模态级别聚合特征；（ii）由预训练的视觉语言模型（VLM）驱动的语义理解模块，提供细粒度的指导并捕捉复杂的跨主体关系；（iii）在线强化学习阶段进一步细化关键概念的模型。除此之外，还构建了一个新数据集以促进稳健的训练和评估。
### Conclusion
大量实验表明，ID-Crafter在多主体视频生成基准测试中建立了新的最先进性能，尤其在身份保留、时间一致性以及整体视频质量上表现出色。
## 453. `cs.CV` - VSI：视觉字幕集成以增强长视频理解的关键帧选择 [PDF](https://arxiv.org/pdf/2508.06869), [HTML](https://arxiv.org/abs/2508.06869)
### Authors
Jianxiang He,Meisheng Hong,Jungang Li,Ziyang Chen,Weiyu Guo,Xuming Hu,Hui Xiong
### Background
多模态大型语言模型（MLLMs）在视觉语言任务中表现出色，但在处理长视频时受到输入上下文长度和高计算成本的限制。因此，稀疏帧采样成为必要的预处理步骤，采样帧的质量直接影响下游性能。现有的关键帧搜索算法在效率和采样帧质量之间取得平衡，但主要依赖视觉模态，难以适应与文本相关任务，往往导致检索结果偏离核心语义内容。
### Innovation
本文提出了一种多模态关键帧检索框架——VISUAL-SUBTITLE INTEGRATION (VSI)，它采用视频搜索和字幕匹配的双重分支协同检索方法，融合互补的视觉和文本信息以精确定位。VSI 在关键帧检索上实现了最先进的准确度，并在与文本相关任务上取得了突破性的性能，在其他任务上也表现出强大的泛化能力。
### Conclusion
VSI 通过集成视觉和文本信息，兼顾效率和采样帧质量，成功解决了现有方法在与文本相关任务上的不足，实现了在长视频理解方面的突破性进展。
## 454. `cs.CV` - ResMatching: 基于引导条件流匹配的噪声鲁棒计算超分辨率 [PDF](https://arxiv.org/pdf/2510.26601), [HTML](https://arxiv.org/abs/2510.26601)
### Authors
Anirban Ray,Vera Galinova,Florian Jug
### Background
计算超分辨率（CSR）在荧光显微镜中虽然是一个病态问题，但有着悠久的历史。CSR的核心是在给定的低分辨率图像的基础上，找到一种先验知识来推断出从未被显微镜成像的高频信息。随着更好地数据驱动的机器学习技术的发展，可以学习更强的先验知识，从而提高CSR的效果。
### Innovation
本文介绍了一种名为ResMatching的新CSR方法，它利用引导条件流匹配来学习改进的数据先验知识。该方法在BioSR数据集中对比常规方法的实验结果显示，ResMatching在各种生物结构上获得了竞争性结果，特别是在低分辨率图像中噪声较多且难以学习强先验的情况下，效果尤为显著。
### Conclusion
通过实验证明，ResMatching能够应用于从隐式学习的后验分布中进行采样，并且该分布适用于所有测试用例，使我们的方法能够提供像素级的数据不确定性，从而指导未来的用户拒绝不确定的预测。
## 455. `cs.CV` - 从潜空间迈出一小步，像素迈出一大步：快速潜空间放大适配器增强您的扩散模型 [PDF](https://arxiv.org/pdf/2511.10629), [HTML](https://arxiv.org/abs/2511.10629)
### Authors
Aleksandr Razin,Danil Kazantsev,Ilya Makarov
### Background
扩散模型在扩展到其训练分辨率之外时存在困难，因为直接采样高分辨率图像是缓慢和昂贵的，而在解码之后进行图像超分辨率 (ISR) 会产生伪影并增加延迟。尽管存在这些挑战，但目前已经存在一些替代方案，如基于模型的图像超分辨率 (ISR) 方法，尽管这些方法能够提升图像质量，但也带来了额外的计算负担。
### Innovation
提出了一个轻量级模块 Latent Upscaler Adapter (LUA)，该模块直接在生成器的潜在代码上进行超分辨率操作，然后再进行最终的 VAE 解码。LUA 是一种即可插拔组件，不需要对基础模型进行任何修改或增加额外的扩散阶段，通过一次前向传播在潜空间中即可实现高分辨率合成。还提出使用共享的 Swin 样式骨干网络与缩放特定的像素混排头部支持 2 倍或 4 倍的放大因子，保留对图像空间 SR 基线的兼容性。LUA 可以实现与空间域 SR 类似的效果，但具有近乎 3 倍更低的解码时间和放大时间。此外，LUA 在不同的 VAE 潜空间中表现出强健的泛化能力，无需从头开始重新训练即可方便地部署。
### Conclusion
实验表明，LUA 可以与原生高分辨率生成方案媲美，并提供了一种实现具有实用性和高效性的可扩展、高保真图像合成的现实方案。
## 456. `cs.CV` - 基于UNet架构多期增强CT肝脏肿瘤分割的比较研究 [PDF](https://arxiv.org/pdf/2510.25522), [HTML](https://arxiv.org/abs/2510.25522)
### Authors
Doan-Van-Anh Ly(1),Thi-Thu-Hien Pham(2 and 3),Thanh-Hai Le(1) ((1) The Saigon International University, (2) International University, (3) Vietnam National University HCMC)
### Background
在多期对比增强计算机断层扫描（CECT）中，肝脏结构的分割对于肝病的计算机辅助诊断和治疗规划至关重要，尤其是肿瘤检测。本研究探讨了不同基于UNet的架构在肝脏肿瘤分割中的性能，从原始UNet开始，扩展到UNet3+及其各种骨干网络，并评估了ResNet、基于Transformer和State-space（Mamba）的骨干网络，它们都使用预训练权重初始化。
### Innovation
1. 研究了包括ResNet，Transformer基于和Mamba在内的不同骨干网络的UNet架构。2. 尽管现代架构有所进步，ResNet基于的模型在多个评估指标上始终优于基于Transformer和Mamba的替代品。3. 引入了注意力机制，特别是结合了Convolutional Block Attention Module (CBAM)，取得了最佳性能。4. ResNetUNet3+结合CBAM模块，不仅取得了最佳的重叠度指标（Dice分数为0.755，IoU为0.662），而且边界定义最为精确，HD95距离为77.911。5. 结合了Grad-CAM可视化技术，以提高解释性，突出预测影响最大的区域。
### Conclusion
经典ResNet架构与现代注意力模块的结合在医学图像分割任务中仍然非常具有竞争力，为临床实践中肝脏肿瘤检测提供了有希望的方向。
## 457. `cs.CV` - Mask2IV：通过掩码轨迹实现以交互为中心的视频生成 [PDF](https://arxiv.org/pdf/2510.03135), [HTML](https://arxiv.org/abs/2510.03135)
### Authors
Gen Li,Bo Zhao,Jianfei Yang,Laura Sevilla-Lara
### Background
生成以交互为中心的视频，如人类或机器人与物体的交互视频，对于增强机器人的感知理解能力至关重要。这类视频能够为机器人学习、操控策略训练和可用性推理提供丰富的视觉先验知识。然而，现有的方法往往难以捕捉这些复杂和动态的交互过程。虽然近期的研究表明，掩码可以作为有效的控制信号并改善生成质量，但在真实场景中获取密集且精确的掩码标注仍然是一项重大挑战。
### Innovation
为了克服这一局限性，该研究提出了Mask2IV系列框架，这种框架专门为以交互为中心的视频生成设计。它采用了一个拆分的两阶段流水线，首先预测动作对象和对象的可能运动轨迹，然后根据这些轨迹生成视频。这一体系结构消除了用户对密集掩码输入的需求，同时保留了对交互过程的灵活性。此外，Mask2IV支持多样化的直观控制，让用户能够指定交互目标对象并通过动作描述或空间位置提示来指导运动轨迹。
### Conclusion
我们编制了两种涵盖不同人类-物体交互类别和机器人操作场景的基准数据集，用于支持系统的训练和评估。大量的实验结果表明，本方法在视觉真实感和可控性方面相较于现有方法具有明显的优势。
## 458. `cs.CV` - 分离的概念比语言更响亮：可解释的视频动作识别 [PDF](https://arxiv.org/pdf/2511.03725), [HTML](https://arxiv.org/abs/2511.03725)
### Authors
Jongseo Lee,Wooil Lee,Gyeong-Moon Park,Seong Tae Kim,Jinwoo Choi
### Background
现有的视频动作识别方法在解释动作模型的预测依据时，要么解释混淆不清（基于显著性的方法），要么解释结构虽好但难以解释运动（基于语言的方法）。因此，需要一种能够清晰区分动作随时间的变化与周围空间上下文的可解释模型。
### Innovation
提出了DANCE（分离的动作与情境概念基于可解释的视频动作识别）框架，通过分离的概念类型（运动动力学、对象和场景）来进行预测。DANCE 使用大型语言模型自动提取对象和场景概念，并基于先验概念瓶颈设计，确保预测通过这些概念。实验证明，DANCE 在提高解释清晰度的同时，具有竞争力的性能。
### Conclusion
DANCE框架通过分离的概念类型大幅提高了解释清晰度，实验结果验证了其优越的解释性，并且DANCE对模型调试、编辑和故障分析也具有积极作用。
## 459. `cs.CV` - 合成物体组成：用于检测、分割和定位的可扩展且准确的学习方法 [PDF](https://arxiv.org/pdf/2510.09110), [HTML](https://arxiv.org/abs/2510.09110)
### Authors
Weikai Huang,Jieyu Zhang,Taoyang Jia,Chenhao Zheng,Ziqi Gao,Jae Sung Park,Winson Han,Ranjay Krishna
### Background
视觉分组通过实例分割、视觉定位和目标检测等任务实现，这使应用范围从机器人感知到照片编辑。这些问题在计算机视觉中的实现依赖于大规模、精心注释的数据集。尽管这些数据集对模型训练至关重要，但它们的建设成本高昂、覆盖范围存在偏见，且难以扩展。合成数据集提供了一个有前景的替代方案，但它们在灵活性、准确性以及组合多样性方面仍然存在问题。
### Innovation
介绍了合成物体组成（SOC），这是一种新颖的对象中心合成策略，通过3D几何布局增强和相机配置增强进行合成图像生成，结合生成性协调和掩码区域加权混合，可以生成准确且多样的掩膜、边界框和引用表达。使用SOC训练的模型表明，在仅使用100,000张合成图像的情况下，其性能优于大型真实数据集和合成管道训练的模型，达到在LVIS上+10.9 AP和在gRefCOCO上+8.4 NAcc的提升。此外，SOC还允许对不同场景进行可控制的合成数据集构建，并能提升低数据和封闭词汇场景下的性能表现。
### Conclusion
在不同真实数据规模下，使用合成物体添加到LVIS和COCO数据集中的效果显著，尤其是在真实数据极端受限的情况下，如1%的COCO数据设置，可带来高达6.59 AP的提升。此外，这种可控性还支持针对同一类别的引用生成，这是拟提出的诊断性定位任务，需要细微的属性区分。
## 460. `cs.CV` - MoE LoRA模型参数高效化用于少量样本多风格编辑 [PDF](https://arxiv.org/pdf/2511.11236), [HTML](https://arxiv.org/abs/2511.11236)
### Authors
Cong Cao,Yujie Xu,Xiaodong Xu
### Background
近年来，图像编辑得到了广泛的关注。然而，一般图像编辑模型在面对新的艺术风格时常常无法产生令人满意的结果。挑战在于如何仅使用有限的配对数据有效地微调通用图像编辑模型到新的风格。
### Innovation
该论文提出了一种新的少量样本多风格编辑框架。构建了一个涵盖五种不同风格的基准数据集，并提出了一个参数高效且具有风格特定和风格共享路由机制的多风格Mixture-of-Experts Low-Rank Adaptation（MoE LoRA）方法。提出了新的基于度量特征的方法自动确定每个层的最佳秩，此外还探索了MoE LoRA的最优插入位置，并结合对抗学习和流匹配来指导扩散训练过程。实验结果表明，所提出的方法在显著减少LoRA参数的情况下优于现有的最先进的方法。
### Conclusion
提出的MoE LoRA方法在少量样本的多风格编辑任务中表现出更优的结果，方法具有参数效率，并且能在有限配对数据的基础上有效学习新的风格。
## 461. `cs.CV` - DocSLM: 一种用于长多模态文档理解的小型视觉语言模型 [PDF](https://arxiv.org/pdf/2511.11313), [HTML](https://arxiv.org/abs/2511.11313)
### Authors
Tanveer Hannan,Dimitrios Mallios,Parth Pathak,Faegheh Sardari,Thomas Seidl,Gedas Bertasius,Mohsen Fayyaz,Sunando Sengupta
### Background
大型视觉语言模型（LVLMs）在长且复杂的文档上展示了强大的多模态推理能力，但其高内存占用导致其难以部署在资源受限的边缘设备上。
### Innovation
DocSLM 通过引入层级多模态压缩器和流式弃权机制，显著减少了内存消耗并保留了局部和全局语义。层级多模态压缩器可以同时编码每页的视觉、文本和布局信息，生成固定长度的序列，从而大幅度减少内存使用。流式弃权机制能够对文本文档的各个片段进行逐段处理，并且通过基于熵的不确定性校准器过滤低置信度的响应。
### Conclusion
在多个长多模态文档基准测试中，DocSLM 的表现与最先进的方法持平或超越，同时使用 82% 更少的视觉标记、75% 更少的参数和 71% 更低的延迟，从而在轻量级的边缘设备上实现可靠的多模态文档理解。
## 462. `cs.CV` - Forecasting Future Anatomies: Longitudinal Brain Mri-to-Mri Prediction [PDF](https://arxiv.org/pdf/2511.02558), [HTML](https://arxiv.org/abs/2511.02558)
### Authors
Ali Farki,Elaheh Moradi,Deepika Koundal,Jussi Tohka
### Background
预测未来的脑状态从基线磁共振成像（MRI）是一项神经影像学中的核心挑战，对于研究如阿尔茨海默病等神经退行性疾病具有重要影响。大多数现有方法预测未来认知评分或临床结果。本研究则侧重于纵向MRI图像间的预测，能够预报参与者未来几年的整个脑MRI变化，从而建模复杂的分布式神经退行性模式。
### Innovation
本文使用五种深度学习架构（UNet, U2-Net, UNETR, Time-Embedding UNet, 和ODE-UNet）在两个纵向队列（ADNI和AIBL）中进行实验和评估。预测的后续MRI图像直接与实际的后续扫描进行对比，通过评估整体相似度和局部差异来评价模型性能。最佳模型实现了高保真度的预测，并且所有模型在独立外部数据集中的表现稳定，证明了其跨队列的稳健性。
### Conclusion
研究结果表明，深度学习能够可靠地在亚像素级别预测个体特异性脑MRI变化，从而为个体风险评估提供新的机会。
## 463. `cs.CV` - 视觉专家参与下草案和精炼的方法 [PDF](https://arxiv.org/pdf/2511.11005), [HTML](https://arxiv.org/abs/2511.11005)
### Authors
Sungheon Jeong,Ryozo Masukawa,Jihong Park,Sanggeon Yun,Wenjun Huang,Hanning Chen,Mahdi Imani,Mohsen Imani
### Background
近年来，大型视觉语言模型（LVLMs）在多模态推理方面表现出色，但由于过度依赖语义先验而不是视觉证据，常常产生不切实际或虚幻的回答。这一局限性突显了缺乏量化这些模型在推理过程中到底多大程度依赖视觉信息的度量标准。因此，需要一种方法来衡量并增强模型在推理过程中的视觉依赖度。
### Innovation
提出了Draft and Refine（DnR）代理框架，该框架通过问题条件下的利用度量来驱动。该度量首先构建了一个查询条件的相关图以定位问题特定的线索，然后通过引导性概率遮罩测量依赖性。该度量指导DnR代理利用外部视觉专家的定向反馈进行草案的精炼。每个专家的输出（如框或掩码）作为视觉线索呈现给图像，模型随后被重询以选出了一个改良度最大的回应。这一过程可以在不重新训练或改变架构的情况下增强视觉定位。
### Conclusion
跨VQA和描述基准实验结果表明，度量视觉利用度可以为构建更加可解释和基于证据驱动的多模态代理系统提供理论依据，能获得一致的准确率提升并且降低虚幻回答。
## 464. `cs.CV` - 使用深度神经网络和Grad-CAM解释的胸部X光片上弱监督肺炎定位 [PDF](https://arxiv.org/pdf/2511.00456), [HTML](https://arxiv.org/abs/2511.00456)
### Authors
Kiran Shahi,Anup Bagale
### Background
胸部X光成像是肺炎诊断的常用方法，但准确确定肺炎受影响区域通常需要详细像素级注释，而像素级注释成本高且耗时。为解决这一问题，本研究提出了一种使用梯度加权类激活映射（Grad-CAM）的弱监督深度学习框架，用于肺炎分类和定位，该框架通过利用图像级别的标签而非像素级注释生成具有临床意义的热图，以凸显肺炎受影响区域。
### Innovation
本研究提出的方法利用图像级别的标签而非像素级注释，生成具有临床意义的热图，来强调肺炎受影响区域，同时评估了七个预训练的深度学习模型，包括Vision Transformer，使用相同的训练条件和分层样本方法，验证了模型在肺炎分类和定位上的有效性和性能。
### Conclusion
实验证明，所有模型在肺炎分类上的准确率均达到96-98%，ResNet-18和EfficientNet-B0表现出最佳性能，而MobileNet-V2则提供了轻量级的高效替代方案。Grad-CAM热图可视化证明了该方法聚焦于临床相关的肺部区域，支持使用可解释的人工智能进行放射学诊断。总体而言，这项工作展现了弱监督、可解释模型在提高AI辅助肺炎筛查透明度和临床信任方面的潜力。
## 465. `cs.CV` - BeyondFacial：超越面部：身份保留个性化生成超越面部特写 [PDF](https://arxiv.org/pdf/2511.11989), [HTML](https://arxiv.org/abs/2511.11989)
### Authors
Songsong Zhang,Chuanqi Tang,Hongguang Zhang,Guijian Tang,Minglong Li,Xueqiong Li,Shaowu Yang,Yuanxi Peng,Wenjing Yang,Jing Zhao
### Background
当前的身份保留个性化生成(IPPG)已经在电影制作和艺术创作中取得了进展，但现有方法过于注重面部区域，使得输出主要集中在面部表现上。这种方法在处理复杂文本提示时存在视觉叙事较弱和语义一致性较差的问题，其核心限制在于身份特征嵌入影响生成模型的语义表达能力。
### Innovation
本文提出了一种超越面部特写的IPPG方法，通过设计Dual-Line Inference (DLI)管道将身份与语义分离，解决了传统单一路径架构中存在的身份与语义之间的表示冲突。此外，我们提出了一种Identity Adaptive Fusion (IdAF)策略，将身份语义融合推迟到噪声预测阶段，并结合自适应注意力融合和噪声决策掩蔽，避免身份嵌入对语义的影响。最后，我们引入了Identity Aggregation Prepending (IdAP)模块，以聚合身份信息并取代随机初始化，进一步增强身份保留能力。实验结果表明，该方法在超越面部特写的情况下实现了身份保真度和场景语义创造的协同优化，可以稳定有效，并且在现有的IPPG框架中可以作为一个即插即用组件快速部署。
### Conclusion
我们的方法实现了超越面部特写的稳定有效的IPPG任务性能，能够高效生成无需手动遮罩或微调的个性化内容，为电影级别的角色场景创建提供了支持，并为相关领域提供了更丰富的个性化生成能力。
## 466. `cs.CV` - Text2Traffic: 交通场景中的文本到图像生成和编辑方法 [PDF](https://arxiv.org/pdf/2511.12932), [HTML](https://arxiv.org/abs/2511.12932)
### Authors
Feng Lv,Haoxuan Feng,Zilu Zhang,Chunlong Xia,Yanfeng Li
### Background
随着智能交通系统的快速发展，基于文本的图像生成和编辑技术在交通监控、自动驾驶等应用中展示了提供丰富可控制视觉场景数据的潜力。然而，现有技术仍面临一些挑战，包括生成的交通元素语义不足、摄像头视角有限、合成图像的视觉保真度低以及文本描述与生成内容之间的对齐不佳。
### Innovation
本文提出了一种统一的文本驱动的图像生成和编辑框架，利用可控制的掩码机制无缝结合这两项任务。进一步地，引入了车辆侧和路边多视角数据以增强交通场景的几何多样性。训练策略分为两阶段：第一阶段使用大规模粗粒度的图文数据进行概念学习；第二阶段则通过细粒度的描述数据进行微调，以增强文本与图像的对齐和细节质量。此外，提出了一种掩码区域加权损失函数，在训练过程中动态强调小而关键的区域，从而显著提升小型交通元素的生成保真度。
### Conclusion
广泛的实验表明，本文方法在交通场景中的基于文本的图像生成和编辑方面达到了领先性能。
## 467. `cs.CV` - 用查询感知的分词器看清森林和树木：长视频多模态语言模型 [PDF](https://arxiv.org/pdf/2511.11910), [HTML](https://arxiv.org/abs/2511.11910)
### Authors
Siyou Li,Huanan Wu,Juexi Shao,Yinghao Ma,Yujian Gan,Yihao Luo,Yuwei Wang,Dong Nie,Lu Wang,Wengqing Wu,Le Zhang,Massimo Poesio,Juntao Yu
### Background
尽管多模态大型语言模型（MLLMs）在视频理解方面取得了进步，但长视频的理解仍然是一个挑战。主要问题是视觉标记的数量随着视频长度线性增长，导致注意力成本、内存和延迟的指数级增长。
### Innovation
提出了一种称为Query-aware Token Selector (QTSplus)的轻量级且强大的视觉标记选择模块，它作为视觉编码器和LLMs之间的信息门。QTSplus通过（i）利用跨注意力分配视觉标记分数，（ii）基于查询的复杂性预测实例特定的保留预算，以及（iii）通过可微直通估计器在训练期间选择Top-$n$标记和在推理期间使用硬门，动态选择输入文本查询的重要视觉证据。此外，一个小重编码器利用绝对时间信息保持时间顺序，实现二级定位的同时保持全局覆盖。集成到Qwen2.5-VL中，QTSplus压缩视觉流高达89%，并降低了28%的端到端延迟。
### Conclusion
在八个长视频理解基准上的评估表明，QTSplus的总体准确度接近原始Qwen模型的水平，并在TempCompass方向和顺序准确性上分别优于原始模型20.5和5.6点。这些结果表明，QTSplus是有效且通用的机制，可以将MLLMs扩展到现实世界的长视频场景，同时保留任务相关的证据。
## 468. `cs.CV` - FinCriticalED: 金融事实级OCR评价的视觉基准 [PDF](https://arxiv.org/pdf/2511.14998), [HTML](https://arxiv.org/abs/2511.14998)
### Authors
Yueru He,Xueqing Peng,Yupeng Cao,Yan Wang,Lingfei Qian,Haohang Li,Yi Han,Ruoyu Xiang,Mingquan Lin,Prayag Tiwari,Jimin Huang,Guojun Xiong,Sophia Ananiadou
### Background
金融文档中包含密集的视觉布局和大量的表格，其中数值和时间信息紧密耦合，具有较高的结构关联性。在高风险环境下，OCR错误如符号逆转或日期错位会导致截然不同的解释。传统的OCR评估指标如ROUGE和编辑距离只能捕捉表面级别的文本相似性，无法满足金融领域对于准确性的高要求。
### Innovation
提出了一种名为FinCriticalED的视觉基准，用于评估OCR和视觉语言模型在金融文档中的事实级理解能力。该基准提供了500个图像-HTML配对，专家标注了超过七百个数值和时间事实。主要创新包括：1) 建立了首个采用事实级评价的金融文档理解基准，强调领域内关键事实的正确性；2) 注释工作由金融专家完成，严格控制关于符号、量级和时间表达的质量；3) 开发了LLM-as-Judge评估流程，能够对复杂视觉金融文档进行结构化事实提取和上下文验证。
### Conclusion
虽然当前最强的专有模型在事实准确性上表现最佳，但仍然存在大量在复杂视觉数值和时间场景中的错误。通过对FinCriticalED进行定量评估和专家案例研究，本研究为推动视觉准确性的金融及其他关键领域提供了严格的基石。
## 469. `cs.CV` - 通过云中漫步进行即插即用在线测试时自适应：无需训练的3D视觉-语言基础模型 [PDF](https://arxiv.org/pdf/2511.15311), [HTML](https://arxiv.org/abs/2511.15311)
### Authors
Mehran Tamjidi,Hamidreza Dastmalchi,Mohammadreza Alimoradijazi,Ali Cheraghian,Aijun An,Morteza Saberi
### Background
3D视觉-语言基础模型（3D VLFMs）在开放世界点云处理任务中展现了强大的泛化能力和零样本识别能力。然而，在现实场景中，由于数据的噪声、不完整性或与训练数据分布的不同，这些模型的性能往往会大大降低。
### Innovation
本研究提出了一种全新的无需训练的在线测试时自适应（TTA）策略——Uni-Adapter，基于动态原型学习。Uni-Adapter通过构建一个3D缓存来存储特定类别的簇中心作为原型，并不断更新这些原型以捕捉异构数据分布内的类内变异性。同时，通过图谱基础的标签平滑模块来捕捉原型间的相似性，以保持相似原型之间的标签一致性。最后，Uni-Adapter 使用熵加权聚合来统一原始3D VLFM和精炼后的3D缓存的预测，以实现可靠的自适应。
### Conclusion
在无需重新训练的情况下，Uni-Adapter 有效地缓解了分布偏移，其在不同3D基础模型上取得了最好的性能。相比之下，Uni-Adapter 在 ModelNet-40C 上提高了 10.55%，在 ScanObjectNN-C 上提高了 8.26%，在 ShapeNet-C 上提高了 4.49%，超过了原始的3D VLFMs。
## 470. `cs.CV` - 自动可解释的3D超声心动图提取2D视频 [PDF](https://arxiv.org/pdf/2511.15946), [HTML](https://arxiv.org/abs/2511.15946)
### Authors
Milos Vukadinovic,Hirotaka Ieki,Yuki Sahashi,David Ouyang,Bryan He
### Background
尽管心脏具有复杂的三维（3D）解剖结构，但传统的医学成像技术——心脏超声，依赖于一系列2D视频来展示单个心脏结构。3D超声心动图作为一种正在发展的成像技术，现在提供了临床使用的足够图像质量，具有加快获取流程和提高对非轴向特征评估的能力。然而，医生们需要处理大量的3D数据，这可能对分析效率有所影响。
### Innovation
本文提出了一个自动方法，可以从3D心脏超声数据中选择标准的2D视图，使医生能够用他们习惯的格式解读数据，并从3D扫描的速度和使用性中获益。该方法采用深度学习视图分类器和基于解剖标志的下游启发式规则，结合心脏病学专家的启发式规则，重构标准的超声心动图视图。经过三位心脏病学家在盲评中的验证（1600个来自两家医院的视频，准确率为96%），下游2D视频在检测心脏异常和生成临床级别的心脏解剖测量方面的能力也得到了验证。
### Conclusion
提取出的2D视频保留了空间校准和诊断特征，使临床医生能够准确地从3D数据中进行现实世界的解释。作者已发布相关代码和包含29个3D超声心动图视频的数据集。
## 471. `cs.CV` - YOLO Meets Mixture-of-Experts: Adaptive Expert Routing for Robust Object Detection [PDF](https://arxiv.org/pdf/2511.13344), [HTML](https://arxiv.org/abs/2511.13344)
### Authors
Ori Meiraz,Sharon Shalev,Avishai Weizman
### Background
背景介绍YOLOv9-T模型在物体检测方面的应用，以及单一YOLOv9-T模型所能达到的检测准确性和召回率水平。
### Innovation
介绍了一种新的混合专家（Mixture-of-Experts）框架，引入了对多个YOLOv9-T专家的自适应路由机制，以实现动态特征专业化，从而相比于单一YOLOv9-T模型，提高平均精度（mAP）和平均召回率（AR）。
### Conclusion
通过采用混合专家框架和自适应专家路由，该研究显著提升了物体检测的性能，达到了更高的检测准确性和召回率。
## 472. `cs.CV` - SemanticStitch：通过前景感知的缝合提升图像连贯性 [PDF](https://arxiv.org/pdf/2511.12084), [HTML](https://arxiv.org/abs/2511.12084)
### Authors
Ji-Ping Jin,Chen-Bin Feng,Rui Fan,Chi-Man Vong
### Background
图像缝合常因拍摄角度变化、位置差异和对象移动导致对齐不准确和视觉不连续。传统的缝合方法忽略了语义信息，影响了前景对象的连续性。
### Innovation
提出了一种基于深度学习的框架SemanticStitch，通过整合前景对象的语义先验来保持其完整性并增强视觉一致性。该方法包括一种新颖的损失函数，强调显著对象的语义完整性，显著提高了缝合质量。同时，还介绍了两个专门的现实世界数据集来评估该方法的有效性。
### Conclusion
实验结果表明，SemanticStitch在图像缝合质量上优于传统技术，为实际应用提供了坚实支持。
## 473. `cs.CV` - 基于卷积最近邻的注意力机制 [PDF](https://arxiv.org/pdf/2511.14137), [HTML](https://arxiv.org/abs/2511.14137)
### Authors
Mingi Kang,Jeová Farias Sales Rocha Neto
### Background
卷积神经网络（ConvNets）和变压器都已成为计算机视觉领域的重要架构，但通常被视为本质上不同的两个家族。本文提出，尽管卷积和注意力在表面上存在差异，但在最近邻聚合框架内，它们可以统一起来。卷积通过空间邻近性选择邻居，而注意力通过特征相似性选择邻居，两种操作存在于连续谱上。
### Innovation
引入了一个统一框架——卷积最近邻（ConvNN），该框架可以为卷积和注意力层提供一个替换选项，使得系统地探索这两种极端之间的中间谱成为可能。通过对不同k值和架构变体的详尽分析，研究发现在这条谱上进行插值可以提供正则化的好处，通过平衡局部和全局的感受野来提高模型性能。
### Conclusion
本文提供了一个统一框架来弥合卷积和注意力之间的界限，这将对设计更加原理性强且可解释的视觉架构产生影响。
## 474. `cs.CV` - POMA-3D: The Point Map Way to 3D Scene Understanding [PDF](https://arxiv.org/pdf/2511.16567), [HTML](https://arxiv.org/abs/2511.16567)
### Authors
Ye Mao,Weixun Luo,Ranran Huang,Junpeng Jing,Krystian Mikolajczyk
### Background
在现有3D场景理解中，预训练模型和数据稀缺是主要挑战。传统的2D基础模型难以直接处理3D数据，而2D场景中丰富的先验知识难以转移到3D场景中。
### Innovation
提出了POMA-3D模型，这是一种从点图中学习的自我监督3D表示模型，它能够保持全局3D几何结构，同时兼容2D基础模型的输入格式。通过视图到场景的对齐策略，将丰富的2D先验知识转移到POMA-3D中。引入了POMA-JEPA架构，通过多视角的几何一致点图特征的联合嵌入预测，确保了点图特征的一致性。构建了基于6500个房间级RGB-D场景和100万个2D图像场景的ScenePoint数据集，用于大规模POMA-3D预训练。
### Conclusion
POMA-3D作为一种强大的3D场景理解的主干模型，不仅在三维问答、体感导航、场景检索和体感定位等多种任务上表现出色，而且仅依赖几何输入（即3D坐标）。这一模型探索了一种新的点图方式来理解3D场景，解决了预训练先验知识稀缺和3D表示学习中的数据不足问题。
## 475. `cs.CV` - EvoLMM: 自我进化的大型多模态模型及连续奖励 [PDF](https://arxiv.org/pdf/2511.16672), [HTML](https://arxiv.org/abs/2511.16672)
### Authors
Omkar Thawakar,Shravan Venkatraman,Ritesh Thawkar,Abdelrahman Shaker,Hisham Cholakkal,Rao Muhammad Anwer,Salman Khan,Fahad Khan
### Background
近年来，大型多模态模型（LMMs）已在推理和感知能力上取得了显著进展，但大多数现有的训练管道仍依赖于人工标注的数据或外部验证的奖励模型，这限制了它们的自主性和扩展性。
### Innovation
本文提出了一种自我进化的框架EvoLMM，该框架仅通过两个合作代理从单一的骨干模型中构建出来：一个生成者(Proposer)生成多样化的、基于图像的问题，以及一个解决者(Solver)通过内部一致性来解决这些生成的问题。学习过程通过持续的自我奖励进行，从而鼓励生成信息性查询并提升结构化推理能力，而无需依靠真实数据或人类判断。
### Conclusion
使用流行模型Qwen2.5-VL作为基础模型，我们的EvoLMM在仅使用原始训练图像的情况下，在多模态数学推理基准测试（包括ChartQA、MathVista和MathVision）上取得了一致的提升，最高可达约3%。我们希望这种简单而有效的方法能够为未来完全无监督的自我改进LMM的研究提供一个坚实的基线。我们的代码和模型已在此处有提供：this https URL。
## 476. `cs.CV` - SF-Recon: 无需简化处理的基于3D高斯点积的轻量化建筑重建 [PDF](https://arxiv.org/pdf/2511.13278), [HTML](https://arxiv.org/abs/2511.13278)
### Authors
Zihan Li,Tengfei Wang,Wentian Gan,Hao Zhan,Xin Wang,Zongqian Zhan
### Background
轻量化建筑表面模型对于数字城市、导航和快速地理空间分析至关重要，然而传统的多视图几何管道仍然因依赖于密集重建、网格化和随后简化的过程而显得笨重且对质量敏感。
### Innovation
提出了一种名为SF-Recon的方法，该方法可以直接从多视图图像中重建轻量化的建筑表面，无需后续网格简化处理。该方法包括三个主要步骤：首先训练一个初始的3D Gaussian Splatting（3DGS）场以获得视图一致的表示；其次通过一个由法线-梯度引导的高斯优化提取与屋顶和墙体边界对齐的要素，然后进行多视图边缘一致性修剪以增强结构锐度并抑制非结构伪影；最后通过多视图深度约束的Delaunay三角剖分将结构化的高斯场转换为轻量且结构忠实的建筑网格。
### Conclusion
基于提出的SF数据集，实验结果表明SF-Recon可以直接从多视图影像中重建轻量化的建筑模型，面数和顶点数比显著减少，在保持计算效率的同时实现结构忠实度。
## 477. `cs.CV` - 针对深度哈希的模型反转攻击 [PDF](https://arxiv.org/pdf/2511.12233), [HTML](https://arxiv.org/abs/2511.12233)
### Authors
Dongdong Zhao,Qiben Xu,Ranxin Fang,Baogang Song
### Background
深度哈希通过使用紧凑的二进制码来提高检索效率，但这种技术引入了严重的潜在隐私风险。从哈希码重建原始训练数据可能引发严重的威胁，如生物识别伪造和隐私泄露。然而，专门针对深度哈希模型的模型反转攻击尚未被研究，其安全影响也未被探讨。这是因为真实训练哈希码的不可获得性以及哈明距离的高度离散性，这阻止了现有的方法适应深度哈希。
### Innovation
该研究提出了DHMI，第一个基于扩散的模型反转框架，专为深度哈希而设计。DHMI首先对辅助数据集进行聚类，以提取语义哈希中心作为替代锚点，然后引入基于替代引导的去噪优化方法，该方法利用一种新的攻击度量标准（融合分类一致性与哈希接近度），动态选择候选样本。一系列替代模型引导这些候选样本的细化，以确保生成高保真度且语义一致的图像。实验表明，即使在最具有挑战性的黑盒环境中，利用DHMI也可以成功重建高分辨率高质量的图像，并且在黑盒场景中优于现有的最先进的模型反转攻击方法。
### Conclusion
该研究证实了深度哈希系统固有的严峻隐私威胁。通过使用DHMI，该研究展示了在没有训练哈希码的数据下实现高分辨率高质量图像重建的能力，同时超越了现有最先进的模型反转攻击方法，验证了其实用的有效性和深度哈希系统的潜在隐私风险。
## 478. `cs.CV` - 在计算机断层扫描中自动肌肉和脂肪分割以实现全面的身体成分分析 [PDF](https://arxiv.org/pdf/2502.09779), [HTML](https://arxiv.org/abs/2502.09779)
### Authors
Yaqian Chen,Hanxue Gu,Yuwen Chen,Jichen Yang,Haoyu Dong,Joseph Y. Cao,Adrian Camarena,Christopher Mantyh,Roy Colglazier,Maciej A. Mazurowski
### Background
CT图像的身体成分评估可以应用于多种临床场景，包括心血管预后、代谢健康评估、疾病进展监测、营养状态评估、肿瘤治疗反应预测以及手术和重症监护风险分层。尽管多个研究组开发了专属的分割工具，但缺乏能够跨不同应用领域一致使用的公共工具。为解决这一问题，本研究提出了一种公共访问的端到端分割和特征计算模型，专门用于CT身体成分分析。该模型在胸腔、腹部和骨盆区域的轴向CT图像中进行骨骼肌、皮下脂肪组织（SAT）和内脏脂肪组织（VAT）的分割，并提供多个身体成分指标，如肌肉密度、内脏脂肪与皮下脂肪比（VAT/SAT）、肌肉面积/体积和骨骼肌指数（SMI），支持二维和三维评估。
### Innovation
本研究开发了一个端到端的公开可用分割和特征计算模型，用于CT身体成分分析，特别是在轴向CT图像中分割骨骼肌、皮下脂肪组织和内脏脂肪组织，提供多种身体成分指标，并与基准进行了比较，展示了优越的结果。研究中分割的Dice系数超过89%，并在骨骼肌和皮下脂肪方面超越基准2.10%和8.6%。所有指标的平均绝对相对误差（MRAE）均低于10%。该模型的权重已公开。
### Conclusion
本研究提出并公开了一个专门用于CT身体成分分析的端到端分割和特征计算模型，该模型在多个身体成分指标上表现出色，并提供了对应的公开权重，可以跨不同环境应用。
## 479. `cs.CV` - MF-GCN: 基于眼动追踪、面部和声学特征的三模态抑郁检测的多频率图卷积网络 [PDF](https://arxiv.org/pdf/2511.15675), [HTML](https://arxiv.org/abs/2511.15675)
### Authors
Sejuti Rahman,Swakshar Deb,MD. Sameer Iqbal Chowdhury,MD. Jubair Ahmed Sourov,Mohammad Shamsuddin
### Background
抑郁症是一种普遍的全球性心理健康障碍，其特征是持续的情绪低落和对快乐的体验减少。然而，抑郁症仍然经常被误诊，因为目前的诊断方法主要依赖于主观的临床评估。为了实现客观检测，该研究引入了一个由103名通过三重数据方法（结合眼动跟踪、音频和视频数据）收集的临床评估参与者组成的金标准数据集。这些数据被用来量化抑郁组中对负面刺激的注意力偏见，并记录了抑郁特征如情感钝化和心理运动减退。
### Innovation
该研究提出了一种多频率图卷积网络（MF-GCN）模型，克服了现有基于图的模型专注于低频信息的局限性，利用了一个新型的多频率滤波器模块（MFFBM），可以同时利用低频和高频信号。MF-GCN 模型在二分类任务中达到96%的灵敏度和0.94的F2分数，在三分类任务中取得79%的灵敏度和87%的特异性，显著超过了其他模型。此外，MF-GCN 在中国多模态抑郁语料库（CMDC）数据集上也表现出良好的敏感性（95%）和F2分数（0.96），验证了其泛化能力。
### Conclusion
本文介绍了一个由眼动追踪、面部和声学特征组成的三模态多频框架，通过统计验证，证明了其在区分抑郁与非抑郁组方面具有显著的区分能力。研究提出的多频率图卷积网络（MF-GCN）有效捕捉了多模态间的交互信息，为准确的抑郁症检测提供了强有力的支持。
## 480. `cs.CV` - 监督对比学习用于少量样本的人工智能生成图像检测与归属 [PDF](https://arxiv.org/pdf/2511.16541), [HTML](https://arxiv.org/abs/2511.16541)
### Authors
Jaime Álvarez Urueña,David Camacho,Javier Huertas Tato
### Background
生成人工智能的快速发展使合成图像越来越难以与真实内容区分开来，这为数字媒体的完整性带来了重大挑战。新生成模型的快速发布周期使得传统的检测方法（依赖于定期重新训练）在计算上变得不可行且操作上不实际。
### Innovation
本文提出了一个新颖的两阶段检测框架，旨在解决合成图像检测中的一般化挑战。首阶段采用通过监督对比学习训练的视觉深度学习模型，从输入图像中提取判别性嵌入。该模型在可用生成器的战略子集上进行训练，特定架构被保留以便严格过滤跨生成器的通用能力。第二阶段使用k最近邻（k-NN）分类器在学习的嵌入空间中操作，并采用少量样本的少数样本学习范式进行训练。通过少量样本学习范式，每类仅使用150张图像，该框架在检测准确性方面取得了明显改进，达到91.3%，相对于现有方法有5.2个百分点的提升。针对来源归属任务，在开放集分类上下文中，该方法在AUC和OSCR指标上的改进分别为14.70%和4.27%，显示出在合理获取少量样本的情况下，能够适应不断发展的生成AI景观并具备稳健、可扩展的法医归属能力。
### Conclusion
该工作提出的方法通过使用监督对比学习和少数样本学习，在检测和来源归属任务上取得了显著的性能提升，展现了对生成AI的不断发展的适应性，而不需进行耗时且资源密集的全面重新训练流程。
## 481. `cs.CV` - HazeMatching: 使用引导条件流匹配进行显微镜图像除雾 [PDF](https://arxiv.org/pdf/2506.22397), [HTML](https://arxiv.org/abs/2506.22397)
### Authors
Anirban Ray,Ashesh,Florian Jug
### Background
荧光显微镜在生命科学研究中起到了主要推动作用。尽管高端共焦显微镜可以过滤掉焦外光，但更便宜和更易获取的显微镜模式，如宽视场显微镜，无法做到这一点，导致图像数据模糊。计算上除雾试图结合两者的优点，从而实现廉价的显微镜但又具有清晰的图像。现有的方法在保持数据准确性和提高数据现实感之间存在权衡，HazeMatching旨在找到这两者之间的平衡。
### Innovation
HazeMatching提出了一种新的迭代方法，用于除掉荧光显微镜图像中的雾。通过利用带有模糊观察的条件流匹配框架，我们对生成过程进行了引导。HazeMatching在5个数据集上进行了评估，涉及到合成和真实数据，并且能够在平均上实现对准确性和现实感的平衡。此外，通过校准分析，HazeMatching展示了良好的预测校准性，并且该方法无需显式的退化操作符，使其适用于真实显微镜数据。
### Conclusion
HazeMatching是一种新的迭代方法，解决了荧光显微镜图像除雾时准确性和现实感之间的权衡。通过对合成和真实数据集的评估，HazeMatching在平均上达到了对准确性和现实感的平衡，并且通过校准分析展示了预测的校准性。此外，该方法不限于特定的退化操作符，使其适用于实际的显微镜数据。研究团队已经公开了用于训练和评估的所有数据以及代码，使用的是宽松的许可协议。
## 482. `cs.CV` - 基于稀疏自编码器的无模型偏见控制 [PDF](https://arxiv.org/pdf/2507.20973), [HTML](https://arxiv.org/abs/2507.20973)
### Authors
Chao Wu,Zhenyi Wang,Kangxian Xie,Naresh Kumar Devulapally,Vishnu Suresh Lokhande,Mingchen Gao
### Background
文本到图像（T2I）扩散模型经常表现出性别偏见，特别是在职业和性别化主体之间生成刻板印象的关联。尽管存在一些先前的方法，例如基于CLIP的过滤或提示工程，但这些方法往往需要对特定模型进行调整，并且提供的控制有限。本文提出了一种名为SAE Debias的轻量级、模型无关框架，用于减轻T2I生成中的此类偏向。
### Innovation
SAE Debias通过利用在性别偏见数据集上预训练的k-稀疏自编码器直接在特征空间内操作，不需要重新训练或架构修改。该方法通过构建并抑制每个职业的偏方向，在推断中引导生成更加性别均衡的结果。稀疏自编码器仅需一次训练即可提供可重复使用的去偏方向，有效地控制和提供了有解释性的偏向子空间见解。这一方法是首次应用稀疏自编码器来识别和干预T2I模型中的性别偏见，并且在多个T2I模型上（包括Stable Diffusion 1.4、1.5、2.1和SDXL）的广泛评估证明，SAE Debias可以显著减少性别偏见同时保持生成质量。
### Conclusion
这项研究贡献了建立负责任的生成AI的成果，提供了一种可解释且模型无关的工具，以支持T2I生成中的公平性。
## 483. `cs.CV` - Prenatal超声图像中的脑室扩大深度学习分析 [PDF](https://arxiv.org/pdf/2511.07827), [HTML](https://arxiv.org/abs/2511.07827)
### Authors
Youssef Megahed,Inok Lee,Robin Ducharme,Aylin Erman,Olivier X. Miguel,Kevin Dick,Adrian D. C. Chan,Steven Hawken,Mark Walker,Felipe Moretti
### Background
脑室扩大是一种在胎儿大脑中由胎儿脑室扩张引起的情况，早期诊断至关重要，因为它可能与胎儿染色体异常和潜在的遗传综合征有关的风险增加相关。现有的研究和临床上对能够早期准确诊断脑室扩大并能够用于潜在遗传疾病筛查的工具需求较高。
### Innovation
本文提出了一种通过超声自监督基础模型结合掩蔽自动编码器（USF-MAE）来检测胎儿脑部超声图像中脑室扩大的深度学习模型。该模型使用了预训练的Vision Transformer编码器，并针对特定任务进行了微调。与基准模型相比，USF-MAE在F1分数、精度、准确率等指标上取得了显著提高。
### Conclusion
USF-MAE模型在交叉验证和独立测试数据集上的F1评分分别为91.76%和91.78%，表现优于VGG-19、ResNet-50和ViT-B/16等基准模型，平均测试精度为94.47%，准确率为97.24%。模型的Eigen-CAM热图表明其聚焦于脑室区域进行诊断，具有解释性和临床合理性。
## 484. `cs.CV` - 拓扑感知神经插值方法在标量场中的应用 [PDF](https://arxiv.org/pdf/2508.17995), [HTML](https://arxiv.org/abs/2508.17995)
### Authors
Mohamed Kissi,Keanu Sisouk,Joshua A. Levine,Julien Tierny
### Background
本文提出了在给定时间 varying 序列的持久同调图以及对应的稀疏时间采样标量场（关键帧）的情况下，一种基于神经网络的时间感知标量场插值方法。该方法的目标是将非关键帧的图反转以生成缺失数据的合理估计。传统的插值方法可能无法准确地捕捉和填充缺失的时间步数据，尤其是当数据具有复杂的拓扑结构时。本文通过结合特定的拓扑损失来改进插值方法，从而提高了几何和拓扑重建的精度。
### Innovation
1. 本文提出的插值方法依赖于一个神经网络架构，该架构通过关键帧示例学习从时间值到对应标量场的关系，并将此关系可靠地扩展到非关键帧的时间步。2. 结合特定的拓扑损失来增强神经网络架构，这不仅改进了几何重建，还改进了拓扑重建，使得数据和拓扑结构的插值更为准确。
### Conclusion
实验结果表明，该方法在2D和3D时间 varying 数据集的插值方面优于参考插值方案。特别是在数据和拓扑适配上具有明显优势。作者提供了该方法的开源实现。
## 485. `cs.CV` - VLA-Pruner: 时间感知的双层视觉词汇裁剪方法以提高高效视觉-语言-行动推理 [PDF](https://arxiv.org/pdf/2511.16449), [HTML](https://arxiv.org/abs/2511.16449)
### Authors
Ziyan Liu,Yeqiu Chen,Hongyi Cai,Tao Lin,Shuo Yang,Zheng Liu,Bo Zhao
### Background
视觉-语言-行动（VLA）模型在实现智能体AI方面显示出巨大潜力，但由于处理连续视觉流的高计算成本严重限制了它们的实时部署。通过保存显着的视觉词汇单元并丢弃冗余的词汇单元来降低计算复杂度的“词汇单元修剪”已成为提升视觉-语言模型（VLMs）性能的有效方法。然而，这些VLM特定的词汇单元修剪方法仅基于语义显着度度量（例如，预填充注意）来选择词汇单元，而忽略了VLA固有的高层面语义理解与低层面动作执行的双系统特性。因此，这些方法偏向于保留语义线索，忽视了动作生成所需的关键信息，导致VLA性能显著下降。
### Innovation
本文提出的VLA-Pruner是一种通用即插即用的VLA特定词汇单元修剪方法，能够适配VLA模型的双系统特性，并利用机器人操作中的时间连续性。具体而言，VLA-Pruner采用双层重要性标准来保持视觉词汇单元：视觉-语言预填充注意用于语义层面的相关性，通过时间平滑估计的动作解码注意用于动作层面的重要性。基于此标准，VLA-Pruner提出了一种新的双层词元选择策略，在给定计算预算的情况下，适当地保留既有语义理解和又包含动作执行的紧凑、信息丰富的视觉词汇单元集。
### Conclusion
实验证明，VLA-Pruner在多种VLA架构和不同机器人任务中均达到最先进的性能。
## 486. `cs.CV` - PhyBlock: 通过三维积木组装进行物理理解和计划进展基准 [PDF](https://arxiv.org/pdf/2506.08708), [HTML](https://arxiv.org/abs/2506.08708)
### Authors
Liang Ma,Jiajun Wen,Min Lin,Rongtao Xu,Xiwen Liang,Bingqian Lin,Jun Ma,Yongxin Wang,Ziming Wei,Haokun Lin,Mingfei Han,Meng Cao,Bokui Chen,Ivan Laptev,Xiaodan Liang
### Background
尽管视觉语言模型（VLMs）在为机器人进行推理和规划方面展现了令人期望的能力，它们理解和掌握物理现象，尤其是三维环境中复杂的物理规律的能力明显不足。因此，该研究提出了PhyBlock基准测试，这是为了评估视觉语言模型在物理理解与规划方面的进展。
### Innovation
PhyBlock通过引入一个新的四层次认知组装任务和专门的视觉问题回答（VQA）示例，评估视觉语言模型在空间推理和基本物理理解上的进步，包括对象属性、空间关系和综合场景理解。它对21种最新的视觉语言模型进行了基准测试，揭示了这些模型在高阶规划与推理上的显著局限性，并且发现在复杂任务中性能急剧下降。
### Conclusion
该研究发现，视觉语言模型在高级规划和推理方面存在显著限制，指出在空间定向和依赖推理方面存在持续的困难。虽然链式思考提示未能带来显著改善，这表明空间任务很大程度上依赖于直觉模型理解。PhyBlock被定位为一个统一的测试平台，旨在推动身体认知的进步，连接视觉语言理解与现实世界物理问题解决。
## 487. `cs.CV` - Reason2Attack: 通过LLM推理破解文本到图像模型 [PDF](https://arxiv.org/pdf/2503.17987), [HTML](https://arxiv.org/abs/2503.17987)
### Authors
Chenyu Zhang,Lanjun Wang,Yiwen Ma,Wenhui Li,An-An Liu
### Background
文本到图像（T2I）模型通常部署安全过滤器以防止生成敏感图像。然而，最近的破解攻击方法通过手动设计指令使LLM生成对抗性提示，这些提示能够绕过安全过滤器并生成敏感图像，暴露出T2I模型的安全漏洞。目前，现有方法需要大量查询以实现成功的攻击，限制了其实际应用。
### Innovation
本文提出了一种名为Reason2Attack（R2A）的方法，旨在通过在LLM训练后加入破解攻击，增强LLM生成对抗性提示的推理能力。首先，基于帧语义提出了一种CoT示例合成管道，通过识别相关术语及其上下文示例生成对抗性提示。使用生成的CoT示例进一步微调LLM，使其理解推理路径，并格式化输出结构。然后，将破解攻击任务融入LLM的强化学习过程中，并设计考虑提示长度、隐蔽性和有效性的攻击过程奖励，进一步提高推理准确性。
### Conclusion
在各类T2I模型上的实验证明，R2A在需要更少查询的情况下实现了更好的攻击成功率。此外，对抗性提示在开源和商用T2I模型中显示出强大的攻击可移植性。
## 488. `cs.CV` - 在屏幕上：使用反事实揭示AI驱动视频面试评估中的偏见 [PDF](https://arxiv.org/pdf/2505.12114), [HTML](https://arxiv.org/abs/2505.12114)
### Authors
Dena F. Mujtaba,Nihar R. Mahapatra
### Background
AI增强的人格评估正在逐步影响招聘决策，通过情感计算预测五大人格特质。然而，将AI集成到这些评估中引发了伦理问题，特别是基于训练数据的偏见放大问题，可能会导致基于性别、种族和年龄等受保护属性的歧视性结果。本文提出了一个基于反事实的框架，旨在系统地评估和量化AI驱动的人格评估中的偏见。通过生成反事实表示来调整受保护属性，我们的方法可以在不接触底层模型的情况下进行公平性分析。这种方法特别适用于高影响的应用，例如招聘，其中第三方供应商通常提供黑盒AI系统。
### Innovation
我们引入了一个基于反事实的框架，利用生成对抗网络（GANs）生成反事实表示，调整保护性属性，从而在不接触底层模型的情况下支持多模态公平性分析，包括视觉、音频和文本特征。这种方法比传统方法更能全面分析偏见，特别是在提供黑盒系统的情况下，可以揭示不同人口统计学群体之间的显著差异。
### Conclusion
本研究提供了一个可扩展的工具，用于审计商业AI招聘平台的公平性，特别是在无法获取训练数据和模型内部细节的黑盒环境中。我们的结果强调了反事实方法在提高情感计算中的伦理透明度方面的重要性。
## 489. `cs.CV` - TDSNNs: 竞争性的拓扑深度脉冲神经网络用于视皮层建模 [PDF](https://arxiv.org/pdf/2508.04270), [HTML](https://arxiv.org/abs/2508.04270)
### Authors
Deming Zhou,Yuetong Fang,Zhaorui Wang,Renjing Xu
### Background
灵长类视觉皮层呈现拓扑组织，其中功能相似的神经元在空间上集群分布，这种结构普遍认为可以增强神经处理效率。尽管先前的研究表明，传统的深度人工神经网络（ANN）能够发展出拓扑表征，但这些模型往往忽略关键的时间动态性，导致在诸如物体识别等任务上的性能显著下降，并损害了它们的生物学准确性。
### Innovation
本文提出了一种新颖的空间-时间约束（STC）损失函数，用于拓扑深度脉冲神经网络（TDSNN），成功从低级感官输入到高级抽象表示复制了灵长类视觉皮层中的层级空间功能组织。脉冲神经网络（SNN）固有地捕捉基于突触的时间动态性，提供增强的生物学合理性。与传统ANN相比，TDSNN表现出较小的性能下降（在ImageNet top-1准确率上无下降，而TopoNet表现最好的拓扑ANN出现了3%的下降），并且在大脑相似度方面超越了拓扑ANN。
### Conclusion
研究表明，TDSNN在计算性能和大脑特征之间提供了一个令人信服的平衡，不仅为解释神经科学现象提供了框架，也为设计更高效和鲁棒的深度学习模型提供了新的见解。拓扑组织在TDSNN通过突触机制促进高效和稳定的时间信息处理，从而增强模型的稳健性。
## 490. `cs.LG` - DDTime: 傅里叶谱对齐与信息瓶颈的集数据蒸馏方法及其在时间序列预测中的应用 [PDF](https://arxiv.org/pdf/2511.16715), [HTML](https://arxiv.org/abs/2511.16715)
### Authors
Yuqi Li,Kuiye Ding,Chuanguang Yang,Hao Wang,Haoxuan Wang,Huiran Duan,Junming Liu,Yingli Tian
### Background
时间序列预测在许多领域都是基础性的技术，但训练准确的模型往往需要大规模的数据集和大量的计算资源。集数据蒸馏提供了一种前景光明的替代方案，通过合成紧凑的数据集，保留完整数据的训练行为。不过，将集数据蒸馏扩展到时间序列预测是具有挑战性的，因为两个基本问题：强自相关导致师生模型之间的值-项对齐偏移；合成样本之间的多样性，由于缺乏明确的类别先验来规范轨迹多样性。
### Innovation
提出了一个基于一阶凝聚分解的小型且模块化集数据蒸馏框架——DDTime。针对挑战1，DDTime通过时间统计来重新审视值-项对齐，并引入了频域对齐机制，以减轻由于自相关引起的影响；针对挑战2，它设计了一个借鉴信息瓶颈原理的跨样本正则化，增强多样性并最大化合成轨迹的信息密度。该结合目标与广泛的凝聚范式理论兼容，支持稳定的高阶优化。广泛实验表明，DDTime在20个基准数据集和多样化的预测架构上都优于现有方法，相对准确性提高约30%，计算开销增加约2.49%。
### Conclusion
DDTime在多个基准数据集上表现出色，通过较为轻量且易于集成的方式提升了时间序列预测模型的效率和精确度，为时间序列预测中的集数据蒸馏方法提供了新的解决方案和改进策略。实验结果也表明该方法具有较好的泛化能力和实际应用潜力。
## 491. `cs.CV` - 从感知到推理：深度思考赋能多模态大型语言模型 [PDF](https://arxiv.org/pdf/2511.12861), [HTML](https://arxiv.org/abs/2511.12861)
### Authors
Wenxin Zhu,Andong Chen,Yuchen Song,Kehai Chen,Conghui Zhu,Ziyan Chen,Tiejun Zhao
### Background
随着多模态大型语言模型（MLLMs）在感知任务中取得显著成功，提升其复杂的推理能力已成为关键的研究关注点。现有模型仍面临透明度不足的推理路径和不足的泛化能力等挑战。
### Innovation
论文围绕‘多模态链式思考’（MCoT）提供了系统性的综述。通过分析其技术演化背景、任务需求理论动机；介绍了多模态链式思考方法在三个方面的主流方法并分析其内在机制；总结了现有评估基准和度量标准；讨论了MCoT的应用场景；分析了目前MCoT面临的挑战，并展望了未来的研究方向。
### Conclusion
论文总结了MCoT的研究现状，并指出了未来的研究方向，特别是在提升模型的链式思考能力、透明度和解释性方面。
## 492. `cs.LG` - 使用扩散桥模型进行蛋白质表界面联合设计 [PDF](https://arxiv.org/pdf/2511.16675), [HTML](https://arxiv.org/abs/2511.16675)
### Authors
Guanlue Li,Xufeng Zhao,Fang Wu,Sören Laue
### Background
蛋白质-蛋白质相互作用（PPIs）受表面互补性和疏水相互作用的调控。然而，在计算蛋白设计中，设计与目标受体互补并具有实际物理特性的蛋白质结构和表面仍然是一项重大挑战。
### Innovation
该研究引入了PepBridge，这是一种新颖的框架，用于同时设计蛋白质表面和结构，无缝整合受体表面几何和生物化学特性。通过利用去噪扩散桥模型（DDBMs）将受体表面映射到配体表面，结合多模型扩散模型和形状框匹配网络来预测结构，以确保表面几何与主链结构的对齐，从而实现表面互补性、构象稳定性和化学可行性。
### Conclusion
在多种蛋白质设计场景下的广泛验证表明，PepBridge在生成结构可行的蛋白质方面表现出色，标志着在从上而下蛋白质结构联合设计方面的重大进展。
## 493. `cs.CV` - T2I-RiskyPrompt: 一个用于文本到图像模型安全性评估、攻击和防御的基准 [PDF](https://arxiv.org/pdf/2510.22300), [HTML](https://arxiv.org/abs/2510.22300)
### Authors
Chenyu Zhang,Tairen Zhang,Lanjun Wang,Ruidong Chen,Wenhui Li,Anan Liu
### Background
现有的用于测试文本到图像（T2I）模型安全性的辱风险文本提示数据集在类别、标注细粒度和有效性方面存在局限性。
### Innovation
1. 提出了一种分层风险分类体系，包含6个主要类别和14个细分类别；2. 建立了一个数据收集和注释管道；3. 获得6,432条有效的风险提示，每条提示都带有层级类别标签和详细的风险原因；4. 提出了一个基于原因的危险图像检测方法，明确将MLLM与安全注释对齐。
### Conclusion
基于T2I-RiskyPrompt，对8个T2I模型、9种防御方法、5种安全过滤器和5种攻击策略进行了全面评估，提供了9个关于T2I模型安全性的关键见解，并讨论了T2I-RiskyPrompt在各个研究领域的潜在应用。数据集和代码可在提供的链接中获取。
## 494. `cs.LG` - 一种基于向量符号的多个实例学习方法 [PDF](https://arxiv.org/pdf/2511.16795), [HTML](https://arxiv.org/abs/2511.16795)
### Authors
Ehsan Ahmed Dhrubo,Mohammad Mahmudul Alam,Edward Raff,Tim Oates,James Holt
### Background
多个实例学习（MIL）任务对袋子的标签施加了严格的逻辑约束：只有当一个袋子中的实例至少有一个是正例时，袋子才被标记为正例。尽管这种双纽带约束与许多现实世界的应用相吻合，但最近的研究表明，大多数基于深度学习的MIL方法并没有遵守这种约束，导致了虚高的性能评估指标和较差的泛化能力。
### Innovation
研究提出了一种基于向量符号架构（VSA）的新颖MIL框架，这为在高维空间中执行符号操作提供了一个可微的机制。方法通过将实例和概念直接编码为几乎正交的高维向量，并通过代数操作在分类时强制执行双纽带约束，将MIL假设直接嵌入到模型结构中。为了弥合原始数据和VSA表示之间的差距，设计了一个学习编解码器，将输入实例转换为VSA兼容的向量，同时保持关键的分布特性。该方法包括一个基于VSA的MaxNetwork分类器，实现了一种严格的MIL模型，在标准的MIL基准和医学成像数据集上达到最先进的结果，优于现有方法，同时严格遵守MIL公式。
### Conclusion
这项工作提供了一种原理性、可解释且有效的MIL方法，作为现有依赖于学习启发式的MIL方法的替代方案。
## 495. `cs.LG` - 重新审视基于频域的多模态KV缓存压缩：一种基于离群KV的意识方法 [PDF](https://arxiv.org/pdf/2511.16786), [HTML](https://arxiv.org/abs/2511.16786)
### Authors
Yaoxin Yang,Peng Ye,Xudong Tan,Chongjun Tu,Maosen Zhao,Jia Hao,Tao Chen
### Background
多模态大语言模型在推理过程中面临显著的计算开销，因为多模态关键值缓存（KV Cache）会随着视觉输入长度线性增长。现有的多模态KV Cache压缩方法主要依赖于注意力分数，这类方法与已建立的高效注意力（例如FlashAttention）内核不兼容，并且忽视了值向量对注意力输出的贡献。
### Innovation
本文从KV矩阵分布的角度重新审视了多模态KV Cache压缩问题。首先，通过低通滤波器提取了频域下的主要能量。进一步发现，移除主要能量偏差显著的KV对会显著降低性能，这种远离主要能量的KV对被定义为离群KV。作者提出了一种基于频域的KV Cache压缩框架FlashCache，该框架包含一个离群KV识别模块，用于模型多模态KV矩阵的主要成分，并优先保留显著偏离该成分的KV对。此外，动态预算分配模块用于自适应地确定每层KV Cache的大小，以保留更多的离群KV。在多个多模态语言模型和基准测试上，FlashCache优于最先进的多模态KV压缩方法，可在保持任务性能的同时将解码速度提高1.69倍，KV memory使用降低80%。
### Conclusion
FlashCache展示了相对于现有方法的优势，在加速解码和降低KV内存使用方面表现出色。
## 496. `cs.LG` - 在非IID挑战下抵抗物联网系统攻击的健壮联邦学习方法 [PDF](https://arxiv.org/pdf/2511.16822), [HTML](https://arxiv.org/abs/2511.16822)
### Authors
Eyad Gad,Zubair Md Fadlullah,Mostafa M. Fouda
### Background
随着用户设备数量的急剧增加和数据量的暴增，传统机器学习模型训练面临的复杂性变得难以应对。特别是，在资源受限和安全性敏感的物联网（IoT）网络环境中，这种复杂性尤为突出。联邦学习因其能够分散模型训练到边缘设备或各方而成为一种有效的解决方案，但非独立且非同分布（non-IID）数据导致的统计异质性对联邦学习的有效性构成了挑战。尽管提出了许多联邦学习方法以提高在非IID数据下的学习效果，但现有研究尚缺乏对处理非IID数据下攻击检测的联邦方法的全面比较。该论文将探索在不同数据分布下联邦平均（FedAvg）、FedProx和Scaffold算法的表现，旨在为研究人员和实践者提供有价值的见解。
### Innovation
该研究填补了现有研究中的空白，具体表现在：1) 通过使用CICIoT2023数据集对大规模物联网攻击进行分类；2) 通过细致分析和实验，全面对比了多种联邦学习方法（FedAvg、FedProx和Scaffold）在不同数据分布下的性能；3) 为抵抗物联网系统攻击提供了健壮的联邦学习方法。
### Conclusion
通过研究这些联邦学习方法在不同数据分布下的表现，该论文揭示了它们的性能差异，为研究人员和实践者在处理非IID数据下攻击检测问题提供了重要的参考依据。
## 497. `cs.LG` - 使用序列建模分析心衰患者轨迹 [PDF](https://arxiv.org/pdf/2511.16839), [HTML](https://arxiv.org/abs/2511.16839)
### Authors
Falk Dippela,Yinan Yu,Annika Rosengren,Martin Lindgren,Christina E. Lundberg,Erik Aerts,Martin Adiels,Helen Sjöland
### Background
Transformer架构已经定义了电子健康记录（EHR）涉及的临床预测任务的最新标准。最近引入的Mamba架构在处理长上下文长度时优于基于Llama的先进Transformer（Transformer++），同时使用更少的模型参数。尽管这些架构表现出色，但针对医疗领域，系统地分析模型在不同设置下的性能和效率的方法尚未建立。
### Innovation
该研究调查了六种序列模型在心血管疾病（HF）瑞典大型队列（42820名患者）中的性能，涵盖三种架构类别（Transformers、Transformers++、Mambas）。通过消融实验对EHR基础的输入患者序列、模型配置和时间数据预处理技术进行了修改，Llama实现了最高的预测区分度、最佳校准，并且在所有任务中表现出很大的稳健性。与传统的大型Transformer相比，这两种架构在小配置下展示了高效的表示学习，且在相同模型大小的情况下，使用25%更少的训练数据就能达到更好的性能。
### Conclusion
这篇文章首次系统地研究了序列模型的输入标记化、模型配置和时间数据预处理的选择。未来用于EHR的临床预测任务模型开发可以基于这项研究的建议作为起点。
## 498. `cs.LG` - MOCET评分：蒙特卡洛预期威胁评分 [PDF](https://arxiv.org/pdf/2511.16823), [HTML](https://arxiv.org/abs/2511.16823)
### Authors
Joseph Kim,Saahith Potluri
### Background
评估和衡量AI安全性水平（ASL）对于指导各方采取措施，使风险保持在可接受的限度内至关重要。现有评估模型（如LAB-Bench、BioLP-bench和WMDP）能够可靠地评估模型提升和领域知识，但需要更好地统筹“实际风险”的新指标来指导大规模语言模型的安全案例，并需要能够跟上快速发展步伐的开放性可扩展性指标。
### Innovation
我们引入了MOCET（Monte Carlo Expected Threat，蒙特卡洛预期威胁）评分，这是一种可解释的、双扩展性（自动化和开放性）的度量标准，可以量化实际风险。
### Conclusion
MOCET评分能更好地统筹实际风险，为LLMs的安全评估提供指导，并且可以随着模型的快速发展保持同步。
## 499. `cs.LG` - 可验证的最小长度校准预测集用于序数分类 [PDF](https://arxiv.org/pdf/2511.16845), [HTML](https://arxiv.org/abs/2511.16845)
### Authors
Zijian Zhang,Xinyu Chen,Yuanjie Shi,Liyuan Lillian Ma,Zifan Xu,Yan Yan
### Background
序数分类在许多高风险应用中广泛使用，例如医学成像和诊断，可靠的机会量化（UQ）对决策制定至关重要。算法一致性预测（Conformal Prediction, CP）是一种提供统计验证保证的通用机会量化框架，在实践中尤其有用。然而，先前的序数CP方法主要集中在启发式算法上，或者限制要求底层模型以单峰分布预测序数标签。因此，它们提供的覆盖效率权衡非常有限，也不能满足CP方法所青睐的模型无关和无分布性。
### Innovation
该研究填补了这一空白，提出了一种模型无关的序数CP方法，并提供实例级别的最优预测区间。具体而言，通过将一致序数分类问题形式化为实例级别的最小长度覆盖问题，开发了一种优化的滑动窗口算法，该算法在K（标签候选数）的时间复杂性上是线性的。每个实例的最佳局部优化进一步提高了期望的预测效率。此外，还提出了长度规范化变体以减少预测集大小并保持覆盖。
### Conclusion
在四个来自不同领域的基准数据集上的试验表明，所提出的方法显著提高了预测效率（与基线相比，四组数据的预测效率平均提高15%）。
## 500. `cs.LG` - 使用增强生物声学的欧洲龙虾性别和年龄鉴定 [PDF](https://arxiv.org/pdf/2511.16848), [HTML](https://arxiv.org/abs/2511.16848)
### Authors
Feliciano Pedro Francisco Domingos,Isibor Kennedy Ihianle,Omprakash Kaiwartya,Ahmad Lotfi,Nicola Khan,Nicholas Beaudreau,Amaya Albalat,Pedro Machado
### Background
监测水生生物，尤其是像龙虾这样的难以追踪的物种，存在挑战。本研究重点关注欧洲龙虾（Homarus gammarus），这种物种对于渔业和水产养殖至关重要。理解龙虾的栖息地、福利、繁殖、性别和年龄对于管理和保护至关重要。目前已经使用人工智能（AI）模型根据生物声学排放来分类各种水生生物，但这项研究特别利用欧洲龙虾的生物声学特征（如嗡嗡声/甲壳振动）来通过年龄（幼体/成体）和性别（雄性/雌性）来分类龙虾。
### Innovation
研究探索了深度学习（1D-CNN, 1D-DCNN）和六种机器学习（SVM, k-NN, Naive Bayes, Random Forest, XGBoost, MLP）模型对龙虾声音特征的分类效果。使用Mel-频率倒谱系数（MFCCs）作为特征，结果表明大部分模型在年龄分类中的准确率超过97%（未使用朴素贝叶斯模型时），性别分类中的准确率超过93.23%（除朴素贝叶斯模型外）。这些结果表明，监督机器学习和深度学习能够有效地从龙虾声音中提取年龄和性别相关的特征。
### Conclusion
该研究为非侵入性被动声学监测提供了有前景的方法，用于龙虾的保护、检测和水产养殖及渔业管理，同时能够实现在水下物种中的边缘计算应用。
## 501. `cs.CV` - Conformal Prediction在捕捉 aleatoric 不确定性方面的性能 [PDF](https://arxiv.org/pdf/2509.05826), [HTML](https://arxiv.org/abs/2509.05826)
### Authors
Misgina Tsighe Hagos,Claes Lundström
### Background
元预测是一种不依赖模型的方法，用于生成高概率覆盖真实类别的预测集。尽管元预测的预测集大小预期可以捕捉到 aleatoric 不确定性，但其有效性仍缺乏证据。文献中提到预测集大小可以作为 aleatoric 不确定性的上限，或者预测集大小更难的实例更大，简单的实例更小，但缺乏对元预测器这一属性的有效性的验证。本文探讨了元预测器如何有效地量化 aleatoric 不确定性，特别是由类别重叠引起的固有不确定性。通过测量预测集大小与每个实例由人类注释员分配的不同标签数量的相关性来实现这一目标。我们进一步评估了预测集与人类提供的注释相似性。使用三种元预测方法为四个数据集上的八个深度学习模型生成预测集。每个实例均有多名人类注释员的标注（从五到五十位参与者不等），这使我们能够识别类别重叠。
### Innovation
本研究通过测量预测集大小与每实例不同标签数量的相关性来验证元预测器在此方面的有效性。进一步评估预测集与人类提供注释的一致性。使用不同的元预测方法为不同数据集上的多个深度学习模型生成预测集。
### Conclusion
本研究显示，大多数元预测输出与人类注释的关联性非常弱或弱，只有一小部分显示出中等关联。这些发现强调了对使用元预测器生成的预测集进行再评估的必要性。虽然它们可以提供真实类别的更高覆盖率，但在捕捉 aleatoric 不确定性以及生成与人类注释一致的集方面的能力仍然有限。
## 502. `cs.CV` - 在互信息最小化下的并行MLLM嵌入：探索更多，学习更好 [PDF](https://arxiv.org/pdf/2511.01588), [HTML](https://arxiv.org/abs/2511.01588)
### Authors
Zhicheng Wang,Chen Ju,Xu Chen,Shuai Xiao,Jinsong Lan,Xiaoyong Zhu,Ying Chen,Zhiguo Cao
### Background
嵌入模型是现代AI的基石。由多模态大型语言模型（MLLMs）推动，它们在架构和数据处理方面取得了巨大进展，但整体范式仍局限于SSC，即单一输入、单一嵌入、对比监督，这将丰富的多方面输入简化为单一的嵌入，未能充分利用MLLM的能力。
### Innovation
本文提出了一种名为Parallel Decoupling Framework（PDF）的并行解耦框架，通过利用MLLMs的专有可控制性来定制多模态嵌入学习。具体来说，PDF集中训练共享的MLLM主干在不同的可学习前缀上，从而为一个输入生成多条并行路径，然后利用这些路径获得并行嵌入。为促进并行多样性，采用了Mutual Information Minimization（MIM）作为显式约束，并结合每条路径的对比监督来保持语义对齐。这种双重目标迫使PDF生成稳健的语义覆盖和可泛化的嵌入空间。
### Conclusion
最终，通过一次前向传递即可访问这种杰出的嵌入空间，且计算开销微乎其微。我们已经在多个MLLM主干上实例化了PDF，并在MMEB基准测试上证明了其有效性。各分辨率和模型大小下均获得了显著收益，例如在VLM2Vec-LLaVA-1.6-LR模型上提升了8.9%（7B），在VLM2Vec-Qwen2VL模型上分别提升了4.2%（2B）和3.1%（7B），在效率方面，我们2B模型仅使用一半的计算预算就超过了其基线2.6%的收益。
## 503. `cs.LG` - 拓扑注意网络：通过高斯信念传播关注直接和间接邻居 [PDF](https://arxiv.org/pdf/2511.16871), [HTML](https://arxiv.org/abs/2511.16871)
### Authors
Marshall Rosenhoover,Huaming Zhang
### Background
图神经网络依赖于局部消息传递，这限制了它们建模图中长距离依赖的能力。现有的方法通过连续时间动态或密集自我注意来扩展这一范围，但都面临高计算成本和有限的可扩展性。
### Innovation
我们提出了一种新的框架——拓扑注意网络，它利用了一种概率机制，该机制学习如何在图中的直接和间接连接之间传播信息。这种机制不同于依赖于显式的成对相互作用的传统注意力机制，它是从图中学习的信息传播中自然形成。这使它能够在局部和全局关系上实现统一推理。
### Conclusion
该方法在所有基准模型上的表现达到了最先进的水平。我们的实现可以在该链接中找到：this https URL
## 504. `cs.LG` - 混合计算智能框架用于scRNA-seq插补：结合scRecover和随机森林 [PDF](https://arxiv.org/pdf/2511.16923), [HTML](https://arxiv.org/abs/2511.16923)
### Authors
Ali Anaissi,Deshao Liu,Yuanzhe Jia,Weidong Huang,Widad Alyassine,Junaid Akram
### Background
单细胞RNA测序(scRNA-seq)能够实现细胞分辨率下的转录组测序，但普遍存在丢失事件，这会掩盖生物信号。现有插补方法在保持生物真实性方面存在局限。
### Innovation
提出了一种模块化两阶段工作的SCR-MF，它结合了scRecover的原理性 dropped-out 检测与missForest的稳健非参数插补方法。这种方法在公共和模拟数据集中表现出色，尤其是在准确性、计算效率和生物真实性方面。
### Conclusion
运行时间分析表明，SCR-MF 在准确性和计算效率之间提供了竞争性的平衡，使其适用于中等规模单细胞数据集。
## 505. `cs.LG` - 当结构没有帮助：LLMs不如我们预期的有效地处理文本注释的图。 [PDF](https://arxiv.org/pdf/2511.16767), [HTML](https://arxiv.org/abs/2511.16767)
### Authors
Haotian Xu,Yuning You,Tengfei Ma
### Background
图在统一表示语义内容和关系结构方面具有优势，适用于分子建模、引用网络和社会网络等领域。大型语言模型（LLMs）在自然语言理解和多模态信号整合方面表现出色，这使人们对该技术在图推理中的应用产生了兴趣。最近的研究通过设计图模板或使用图神经网络（GNNs）来编码结构信息来探索这一点。研究者们发现，LLMs通过利用节点的文本描述就能在多种任务中取得优异表现，而大多数结构编码策略提供的增益要么微不足道，要么甚至是有害的。
### Innovation
研究以系统的方法揭示，仅利用节点文本描述的LLMs在多种任务中已表现出较强的能力，且大部分结构编码策略对提升性能的帮助甚微甚至具有负面影响。这表明，强大的语言模型中显式的结构先验往往是不必要的，甚至在某些情况下是反作用的，这一发现代表了传统图学习范式的一次重要偏离，并强调了在LLM时代重新思考结构如何被表示和利用的重要性。
### Conclusion
研究挑战了结构在LLM基于图推理中本质上是有帮助的基本假设，为新的基于语义的图学习方法打开了大门。
## 506. `cs.LG` - GCL-OT: Graph Contrastive Learning with Optimal Transport for Heterophilic Text-Attributed Graphs [PDF](https://arxiv.org/pdf/2511.16778), [HTML](https://arxiv.org/abs/2511.16778)
### Authors
Yating Ren,Yikun Ban,Huobin Tan
### Background
近年来，结构-文本对抗学习在面向文本的图上表现出良好的性能，通过图神经网络和语言模型的互补优势来利用。然而，现有的方法通常依赖于在相似性估计中的同质性假设和硬优化目标，这限制了它们在异质图上的应用效果。虽然一些方法可以通过结构调整或邻居聚合来缓解异质性问题，但通常将文本嵌入视为静态目标，导致对齐效果不佳。该研究识别了文本标记图中的多粒度异质性，包括完全异质性、部分异质性和潜在同质性，这对结构-文本对齐提出了特别的挑战。
### Innovation
该工作提出了一种新型的基于最优传输的图对抗学习框架GCL-OT，针对不同类型的异质性设计了不同的机制。对于部分异质性，设计了基于RealSoftMax的相似性估算器，以强调关键的邻居-单词交互并减弱背景噪声。对于完全异质性，引入了一种基于提示的过滤器，在最优传输对齐时动态排除不必要的噪声。此外，通过最佳传输引导的软监督揭示潜在的具有相似语义的邻居，增强对潜在同质性的学习。理论分析表明，GCL-OT可以改善互信息边界的估计和贝叶斯错误保证。
### Conclusion
广泛的实验结果表明，GCL-OT在九个基准测试上表现出了对现有最佳方法的持续领先，验证了其有效性和鲁棒性。
## 507. `cs.LG` - 使用潜在ODE分类ECG心律失常类型的新方法 [PDF](https://arxiv.org/pdf/2511.16933), [HTML](https://arxiv.org/abs/2511.16933)
### Authors
Angelina Yan,Matt L. Sampson,Peter Melchior
### Background
12导联高采样率ECG是心律失常检测的临床金标准，但其短暂性和取样不连续性可能导致间歇性事件的遗漏。可穿戴ECG设备便于长时间监测，但由于电池限制而导致采样率低且不规则，这给形态分析带来了挑战。
### Innovation
提出了一种端到端的分类流水线，训练一个潜在ODE以建模连续的ECG波形，并从中创建稳健的特征向量；通过将初始360 Hz的ECG信号分别降采样为90 Hz和45 Hz，构建三种潜在向量；利用梯度提升树分类这些向量并测试不同频率下的鲁棒性。性能表现出较小的下降，分别在360 Hz、90 Hz和45 Hz下的宏平均AUC-ROC值为0.984、0.978和0.976，表明通过克服信号保真度与电池寿命之间的权衡，可以实现更小的可穿戴设备，促进心脏健康的长期监测。
### Conclusion
该方法使得更小的可穿戴设备成为可能，这有助于实现长时间监测心脏健康，同时保持了心电图识别心律失常类型的高精度。
## 508. `cs.LG` - ManifoldFormer：黎曼流形上的几何深度学习方法用于神经动力学 [PDF](https://arxiv.org/pdf/2511.16828), [HTML](https://arxiv.org/abs/2511.16828)
### Authors
Yihang Fu,Lifang He,Qingyu Chen
### Background
现有的EEG基础模型主要将神经信号视为欧几里得空间中的通用时间序列，忽视了神经动力学固有的几何结构，这将脑活动限制在低维流形上。这导致模型假定与神经几何之间的根本性不匹配，限制了表示质量及跨被试的一般化能力。
### Innovation
ManifoldFormer 通过一种新颖的几何深度学习框架，明确定义神经流形表示。该架构集成了三个主要创新点：一种黎曼维纳滤波器用于保持几何结构的流形嵌入、一个具有测地线感知注意机制的几何转换器直接操作于神经流形上、以及利用神经ODE动力预测器来进行流形约束的时空演化。
### Conclusion
ManifoldFormer 在四个公开数据集上的广泛评估证明比最先进的方法有显著改进，准确率提高4.6-4.8%，科恩卡帕系数提高6.2-10.2%，同时保持了稳健的跨被试一般化能力。几何方法揭示了与神经生理学原则一致的有意义的神经模式，证明了几何约束对于有效的EEG基础模型是必不可少的。
## 509. `cs.LG` - 深度平衡模型的梯度流 [PDF](https://arxiv.org/pdf/2511.16976), [HTML](https://arxiv.org/abs/2511.16976)
### Authors
Sanjit Dandapanthula,Aaditya Ramdas
### Background
深度平衡模型（DEQs）最近被证明是一种强大的训练极深的权重绑定神经网络的范式，这些网络在许多现代机器学习任务上达到了最先进的性能。尽管在实践上取得了成功，但对于训练DEQs的梯度下降动态的理论理解仍是一个活跃的研究领域。
### Innovation
本文研究了线性模型和单指标模型中深度平衡模型的梯度下降动力学，填补了文献中的几个缺口。通过证明线性DEQs的守恒律，表明训练过程中参数始终被限制在球面上，并使用这一性质显示了梯度流在整个时间范围内的良好条件。进一步证明，在适当的初始化和足够小的步长下，线性DEQs和深度平衡单指标模型的梯度下降收敛到全局最小值。
### Conclusion
通过实验验证了理论发现。
## 510. `cs.LG` - 使用Twitter和电视数据预测人才爆红率 [PDF](https://arxiv.org/pdf/2511.16905), [HTML](https://arxiv.org/abs/2511.16905)
### Authors
Bilguun Batsaikhan,Hiroyuki Fukuda
### Background
人才的早一批检测在广告领域非常关键。本文定义了一个人才突飞猛进的概念，并提出了一种在他们成名之前识别日本人才的方法。主要关注点是确定结合Twitter和电视数据能否有效预测社会数据中随时间变化的趋势。
### Innovation
为了找到最佳模型方法，作者尝试了传统的、神经网络的和集成学习的方法。研究发现，集成学习方法在标准回归指标上表现优于传统和神经网络模型。但通过运用人才突飞猛进的概念，神经网络模型在精确度和召回率方面超越了传统的和集成学习方法。
### Conclusion
研究结果显示，虽然传统的时序模型在许多应用中表现稳定，但神经网络模型在预测社会数据随时间变化趋势方面更具有潜力。使用Twitter和电视数据可以帮助更好地预测人才的突飞猛进，并且神经网络模型更适用于精确评估模型的真正预测能力。
## 511. `cs.LG` - 在帕金森病检测中使用语音生物标志物：经典机器学习模型的稳健统计性能比较 [PDF](https://arxiv.org/pdf/2511.16856), [HTML](https://arxiv.org/abs/2511.16856)
### Authors
Katia Pires Nascimento do Sacramento,Elliot Q. C. Garcia,Nicéias Silva Vilela,Vinicius P. Sacramento,Tiago A. E. Ferreira
### Background
帕金森病是一种进行性神经退行性疾病，除了直接影响功能性移动，还经常伴随着声音障碍，如音量低和发音障碍，这些障碍通常在早期出现。使用语音生物标志物支持帕金森病的早期诊断提供了一种无创、低成本和可访问的替代方案，在临床环境中具有重要意义。
### Innovation
本研究通过对比使用深度神经网络（DNN）和传统机器学习（ML）方法来评估语音生物标志物的有效性，并使用两个公开可用的语音数据集，评估了模型的稳健性。研究结果表明，DNN在意大利语音数据集和帕金森远程监测数据集上的平均准确率分别为98.65%和92.11%，显示出优于传统ML模型的性能和效率，同时也达到相关研究的竞争力。
### Conclusion
本研究确认了DNN的效率，并强调了其使用基于声音的生物标志物进行神经退行性疾病的早期检测的潜力。
## 512. `cs.LG` - PersonalizedRouter: 通过基于图的用户偏好建模实现个性化大规模语言模型路由 [PDF](https://arxiv.org/pdf/2511.16883), [HTML](https://arxiv.org/abs/2511.16883)
### Authors
Zhongjie Dai,Tao Feng,Jiaxuan You
### Background
随着具有多样能力和响应风格的大型语言模型（LLMs）数量的增加，用户在选择合适模型时面临挑战，因为用户在性能、成本和响应风格方面的偏好各不相同。当前的方法通常针对单一固定目标进行优化，忽视了从用户互动数据中学习个体偏好。
### Innovation
本文提出了PersonalizedRouter，一种基于图的框架，通过交互数据中的任务上下文、查询、候选语言模型和用户决策生成个性化模型选择。通过将交互数据转换为异构图来捕捉用户查询和最优模型之间的上下文信息，以及设计多成本效率模拟策略和LLM作为裁判策略来评估跨用户的适应性。
### Conclusion
实验结果显示，PersonalizedRouter在两个模拟策略下显著优于现有方法，并在1000名用户和10个LLM建立的基准上超过最佳方法，具有较强的少量提示泛化能力，在适应新用户和新模型时分别达到完全训练模型性能的64.81%和85.80%。
## 513. `cs.LG` - 更好的音频表示更像大脑：模型与大脑一致性与下游听觉任务绩效的关系 [PDF](https://arxiv.org/pdf/2511.16849), [HTML](https://arxiv.org/abs/2511.16849)
### Authors
Leonardo Pepino,Pablo Riera,Juan Kamienkowski,Luciana Ferrer
### Background
人工神经网络（ANN）是强大的脑部计算模型，但尚不清楚提高其任务表现能否使内部表示更接近脑电活动信号。本文在听觉领域研究了这一问题，量化了36种不同音频模型和来自两个独立fMRI数据集的脑活动之间的匹配度。
### Innovation
作者通过使用体素级和组件级回归分析及表示相似性分析（RSA），发现最近的自监督音频模型，尽管在多种下游任务中的表现更强，但对听觉皮层活动的预测能力也更好。此外，研究还发现，随着模型预训练期间对自然音频数据中缺失信息的重构学习，音频和脑活动表示之间的相似度会逐渐增加并在早期出现。
### Conclusion
模型整体任务表现与与脑部表示一致性的强正相关关系（Pearson相关系数 r>0.7）。预训练期间，尽管模型未被明确优化以匹配脑电活动，但脑部相似性会逐渐增加并在早期显现，说明脑部似的表现可能是学习从自然音频数据中重构缺失信息的学习结果的副产品。
## 514. `cs.LG` - ToC：多智能体语言模型驱动的专利主张搜索树 [PDF](https://arxiv.org/pdf/2511.16972), [HTML](https://arxiv.org/abs/2511.16972)
### Authors
Shuyang Yu,Jianan Liang,Hui Hu
### Background
优化专利主张是一项既关键又具有挑战性的任务，需要仔细平衡新颖性和法律范围。传统的手动撰写主张耗时、昂贵且不一致，而现有的大型语言模型（LLMs）通常缺乏精细主张优化所需的高度结构化和迭代推理能力。为解决这些问题，作者提出了一种名为ToC（Tree of Claims）的创新框架，将蒙特卡洛树搜索（MCTS）与协作多智能体系统相结合，通过专利审查员式的结构化和逐步推理评估新颖性和现有技术揭露，共同优化主张的新颖性、范围保留和语义连贯性。
### Innovation
ToC框架将专利主张编辑问题转化为指导性搜索问题，引入了MCTS和多智能体系统。体系中包含一个基于LLM的EditorAgent，用于提出语境相关的编辑建议，以及一个模拟专利审查员反馈的ExaminerAgent，通过结构化和逐步推理分析新颖性和现有技术揭露。ToC通过精心设计的多目标奖励功能联合优化主张的新颖性、范围保留和语义连贯性。实验表明，在1145个主张的基准测试中，ToC显著优于标准语言模型，在零样本和少数样本场景中平均复合评分提高了8%，最高提高达9%。广泛的实验验证了ToC在生成高质量、法律稳健的主张修订方面的有效性。
### Conclusion
ToC建立了一种透明、可控和可解释的方法，有效弥合了高级LLM推理能力和战略性MCTS规划之间的差距，为结构化的专利主张提供了强有力的支撑。该研究成果已被公开，代码可以在指定的网址获取。
## 515. `cs.LG` - 分子指纹中哈希碰撞的影响：对属性预测与贝叶斯优化的影响 [PDF](https://arxiv.org/pdf/2511.17078), [HTML](https://arxiv.org/abs/2511.17078)
### Authors
Walter Virany,Austin Tripp
### Background
分子指纹技术利用哈希函数创建固定长度的分子向量表示，但哈希碰撞会导致不同的分子子结构被相同特征表示，这会导致分子相似性计算中的过度估计。此研究探讨了在分子属性预测和贝叶斯优化中使用精确指纹比标准压缩指纹是否能提供更准确的预测，并且这些模型的基础是高斯过程。
### Innovation
本研究对比了使用精确指纹与标准压缩指纹在分子属性预测和贝叶斯优化中的效果，特别是关注精确指纹在预测准确性方面的小但一致的提升。
### Conclusion
尽管使用精确指纹在五个分子属性预测基准测试中显示出较小但一致的改进，但在贝叶斯优化性能方面这些收益并未显著提高。
## 516. `cs.LG` - CroTad: 一种针对在线轨迹异常检测的对比强化学习框架 [PDF](https://arxiv.org/pdf/2511.16929), [HTML](https://arxiv.org/abs/2511.16929)
### Authors
Rui Xue,Dan He,Fengmei Jin,Chen Zhang,Xiaofang Zhou
### Background
在现代智能交通系统(ITS)中，检测轨迹异常是一个重要任务，能够识别出不安全、不高效或不规律的旅行行为。尽管深度学习已经成为主导的方法，但仍存在一些关键挑战。首先，子轨迹异常检测相较于全轨迹分析而言仍较少被探索，难以精确识别异常发生的具体段落。其次，许多现有方法依赖于需精细调整的阈值，限制了其在实际应用中的灵活性。此外，轨迹数据的不规则采样及其训练集中的噪声进一步降低了模型性能，使得难以学习可靠的正常路线表征。
### Innovation
本文提出了基于对比强化学习的在线轨迹异常检测框架 CroTad。该方法无需阈值，对于噪声、不规则采样的数据具有鲁棒性。通过引入对比学习，CroTad 能够学习提取多种不同的正常旅行模式，并在子轨迹和点水平上有效区分异常行为。检测模块利用深度强化学习进行在线、实时异常评分，实现在异常段落的及时和细粒度识别。在两个真实世界数据集上的广泛实验表明，该框架在各种评估场景中具有有效性与鲁棒性。
### Conclusion
本文提出的 CroTad 框架通过对比强化学习解决了子轨迹异常检测的不足，并通过引入对比学习提升了模型对不规则采样数据和噪声的鲁棒性。CroTad 能在线上进行实时异常评分，进一步提高了异常检测的精度和时效性。实验结果证实该方法的有效性和稳健性。
## 517. `cs.LG` - 几何解缠遗忘 [PDF](https://arxiv.org/pdf/2511.17100), [HTML](https://arxiv.org/abs/2511.17100)
### Authors
Duo Zhou,Yuji Zhang,Tianxin Wei,Ruizhong Qiu,Ke Yang,Xiao Lin,Cheng Qian,Jingrui He,Hanghang Tong,Heng Ji,Huan Zhang
### Background
机器遗忘是实现隐私保护和模型可靠性的重要手段，但现有方法在有效遗忘和保留知识保持之间存在持续性的权衡。现有方法虽然提供了有用的启发法，但缺乏对遗忘更新如何损害保留知识的正式分析，以及如何通过理论保证消除副作用。
### Innovation
本文从保留集性能受参数更新影响的第一原则出发，提出了几何解缠遗忘（GU）方法。该方法将任何候选遗忘梯度更新分解为在保留空间中的切线分量和正常分量，并仅执行正常分量更新。在标准的信任区域预算下，与原始遗忘梯度对齐的投影方向是最优的，并且还推导了联合遗忘-保留更新目标的最佳投影方向。该方法具有插拔式特点，可以应用于现有的基于梯度的遗忘程序以减轻副作用。
### Conclusion
几何解缠遗忘方法在TOFU, MUSE 和 WMDP 三个基准上实现了相对于其他方法的一致改进。
## 518. `cs.LG` - 扩散模型的能效定律：量化图像生成中的计算和碳排放 [PDF](https://arxiv.org/pdf/2511.17031), [HTML](https://arxiv.org/abs/2511.17031)
### Authors
Aniketh Iyengar,Jiaqi Han,Boris Ruf,Vincent Grari,Marcin Detyniecki,Stefano Ermon
### Background
随着图像生成中所使用的扩散模型计算需求迅速增加，对其能源消耗和环境影响的担忧凸显。当前，能效优化方法多侧重于架构改进或硬件加速，缺乏能够预测不同模型配置和硬件设置下能效消耗的原理性方法。本文提出了一种基于计算复杂度（FLOPs）来预测GPU在扩散模型中的能效消耗的Kaplan扩展规律试验，探讨了这种规律试验在四种先进扩散模型（Stable Diffusion 2和3.5、Flux、Qwen）和三种GPU架构（NVIDIA A100、A4000、A6000）上的适用性，涵盖了解析度、精度、推理步骤数和无分类引导设置等多个配置参数。试验结果显示，该计算和能源规律试验在单一架构内的预测准确性高（R-squared > 0.9），并且具有良好的跨架构普适性，能够为看不见的模型-硬件组合提供可靠的能效估计，验证了扩散推理的计算密集型性质。
### Innovation
本文提出了一种基于Kaplan扩展规律试验的能效模型，特别适用于预测扩散模型在GPU上的能效消耗，通过对不同模型配置和硬件设置的广泛实验验证了其高预测准确性和跨架构普适性。
### Conclusion
该研究证实了扩散推理的计算需求较高，提供了可持续的人工智能部署规划和碳足迹估算的基础。
## 519. `cs.LG` - 语言模型代理为何吹哨? [PDF](https://arxiv.org/pdf/2511.17085), [HTML](https://arxiv.org/abs/2511.17085)
### Authors
Kushal Agrawal,Frank Xiao,Guido Bergman,Asa Cooper Stickland
### Background
大型语言模型（LLMs）作为工具使用的代理，其对齐训练方式发生了新的表现形式。现有研究表明，这些模型有时会使用工具违背用户的利益或明示指令。本文研究了LLMs的吹哨行为：即模型在未获得用户指示或知情的情况下，向对话边界之外的第三方披露疑似不当行为的现象。作者构建了一套多样化且实际的模拟不当行为场景，用于评估模型的吹哨表现。
### Innovation
作者提出了一套评估模型吹哨行为的评价工具，通过多样化的模拟不当行为场景，分析了多种因素对模型吹哨倾向的影响。这些因素包括模型类型、任务复杂度、系统提示中的道德引导以及提供的工具和操作流程，发现这些因素能够显著影响模型的吹哨频率。此外，作者验证了数据集的鲁棒性，使用黑盒方法和模型激活探针测试发现模型评价意识较低。
### Conclusion
吹哨行为在不同模型中出现的频率差异悬殊，随着任务复杂度增加，吹哨行为减少；加强系统提示中的道德引导显著提高吹哨频率；提供更多工具和详细流程减少模型的吹哨行为。且所使用的数据集的模型评价意识比之前的研究工作中的要低。
## 520. `cs.LG` - FIRM: Federated In-client Regularized Multi-objective Alignment for Large Language Models [PDF](https://arxiv.org/pdf/2511.16992), [HTML](https://arxiv.org/abs/2511.16992)
### Authors
Fatemeh(Atena)Nourzad,Amirhossein Roknilamouki,Eylem Ekici, Jia (Kevin)Liu,Ness B. Shroff
### Background
训练大型语言模型（LLMs）时需要平衡多重矛盾的目标，如有益性与无害性，这是一个计算密集型的任务。集中化的训练过程会引发严重的数据隐私问题。联邦学习提供了一个替代方案，但由于现有的联邦多目标优化方法依赖于向服务器传输多个梯度，导致可扩展性差，因此在大型模型上无法很好地实现。
### Innovation
这篇文章提出了FIRM（Federated In-client Regularized Multi-objective alignment）算法，它通过在客户端进行正则化的多目标优化问题的本地求解来实现客户端分歧漂移的直接缓解和通信效率的保持。与以往方法相比，FIRM不需要传输多个梯度到服务器，仅需传输单组适应参数，从而保持高效通信。此外，作者证明了该算法可以收敛到帕乔利最优解，这是首次为联邦多目标对齐提供有限时间收敛保证。
### Conclusion
实验结果表明，FIRM可以产生更平滑的训练动态，减少客户端分歧漂移，并且相对于基线有更好的奖励权衡。进一步地，作者提出了一个方法来加入对目标的偏好，并通过实例帕乔利图示例来展示FIRM可以根据指定偏好平滑地调整不同目标之间的权衡。
## 521. `cs.LG` - 四十年泛北极超级分辨率卫星地表温度数据 [PDF](https://arxiv.org/pdf/2511.17134), [HTML](https://arxiv.org/abs/2511.17134)
### Authors
Sonia Dupuis,Nando Metzger,Konrad Schindler,Frank Göttsche,Stefan Wunderle
### Background
地表温度（LST）是关键气候变量（ECV），对于理解陆地-大气能量交换和监测气候变化至关重要，特别是在快速变暖的北极地区。长期的卫星LST记录，如来自高级非常高分辨率辐射计（AVHRR）的数据，对于检测气候趋势至关重要。然而，AVHRR的全球区域覆盖（GAC）数据的空间分辨率较低，限制了其在分析北极细尺度永久冻土动力学和其他地表过程中的作用。
### Innovation
本文介绍了一个新的42年泛北极LST数据集，将AVHRR GAC的数据分辨率从低分辨率提升到1公里，该提升是通过基于深度各向异性扩散模型的超分辨率算法完成的。模型利用MODIS LST数据进行训练，使用降尺度输入和原生分辨率输出，由高分辨率土地覆盖、数字高程和植被高度图指导。生成的数据集可提供四十年来整片泛北极地区的两次每日、1公里分辨率的LST观测数据。此增强数据集能够改进永久冻土模型、重建近地表空气温度以及评估格陵兰冰盖的表面质量平衡，还支持MODIS之前的气候监测工作，并为未来卫星任务的热红外观测和气候数据记录连续性提供框架。
### Conclusion
该增强数据集提高了对北极地区陆地-大气能量交换的理解和模拟，对气候变化监测具有重要意义，并为未来卫星任务提供技术框架支持。
## 522. `cs.LG` - 掩去冗余：用于多元时间序列聚类的演变掩码表示学习 [PDF](https://arxiv.org/pdf/2511.17008), [HTML](https://arxiv.org/abs/2511.17008)
### Authors
Zexi Tan,Xiaopeng Luo,Yunlin Liu,Yiqun Zhang
### Background
多元时间序列（MTS）聚类可以发现时间数据样本中的固有分组模式。尽管时间序列提供了丰富的区分信息，但它们也包含大量冗余信息，如机器稳定状态操作记录和太阳能发电的零输出时间段。这些冗余信息削弱了对区分时间戳的关注，从而在表示学习中产生性能瓶颈。现有的掩码策略通常作为独立的预处理步骤，与学习过程隔离，限制了对聚类关键时间戳重要性的动态适应。
### Innovation
该论文提出了演变掩码多元时间序列聚类（EMTC）方法，其模型架构由重要性感知特征视距掩码（IVM）和多内生视图（MEV）表示学习模块组成。IVM引导模型学习更多区分的表示，而基于MEV的重建和对比学习路径增强了一般化能力。EMTC在15个真实基准数据集上的广泛实验表明，与8个领先的SOTA方法相比，EMTC平均提高了4.85%。
### Conclusion
EMTC通过重要性感知特征视距掩码和多内生视图模块有效地学习了更具区分性的表示，避免了掩码的过早收敛，并通过聚类指导的对比学习优化了表示和聚类。实验结果证明了EMTC在聚类性能上的优越性。
## 523. `cs.LG` - DelTriC: 一种具有准确异常检测的新聚类方法 [PDF](https://arxiv.org/pdf/2511.17219), [HTML](https://arxiv.org/abs/2511.17219)
### Authors
Tomas Javurek,Michal Gregor,Sebastian Kula,Marian Simko
### Background
传统的聚类算法如k-means、DBSCAN和HDBSCAN在许多情况下性能欠佳，DelTriC算法旨在克服这些限制，提供一种更高效、更准确的聚类解决方案。
### Innovation
DelTriC算法结合了PCA/UMAP降维投影、Delaunay三角化和新颖的回投影机制，首先在低维代理空间中三角化来构建局部邻近性索引，然后回投影到原始高维空间进行鲁棒的边修剪、合并和异常检测。这种设计使得DelTriC在避免局部邻近性决策时脱离小区和合并决策，从而提高了聚类的准确性和鲁棒性。
### Conclusion
DelTriC算法在多项测试中优于传统方法，在可扩展性和准确性方面表现出色，并显著改善了异常值检测。
## 524. `cs.LG` - 自监督的原始 tomography 检测器数据去噪以提高图像重建质量 [PDF](https://arxiv.org/pdf/2511.17312), [HTML](https://arxiv.org/abs/2511.17312)
### Authors
Israt Jahan Tulin,Sebastian Starke,Dominic Windisch,André Bieberle,Peter Steinbach
### Background
由于测量时间短暂，超快电子束 X 射线计算机断层扫描会产生噪声，导致重构伪影并限制整体图像质量。
### Innovation
研究了两种自监督深度学习方法以对原始检测器数据进行去噪，并与无学习的去噪方法进行对比。
### Conclusion
基于深度学习的方法成功提升了检测器数据的信噪比，并且在重构图像方面表现出一致的改进，优于无学习的方法。
## 525. `cs.LG` - 利用IMU数据重建表面肌电图信号以实现上肢动作 [PDF](https://arxiv.org/pdf/2511.17200), [HTML](https://arxiv.org/abs/2511.17200)
### Authors
Shubhranil Basak,Mada Hemanth,Madhav Rao
### Background
表面肌电图(sEMG)提供了关于肌肉功能的重要见解，但其容易产生噪声，且获取过程较为挑战性。同时，惯性测量单元(IMUs)作为一种坚固且可穿戴的替代方案，被作为一种更稳定、方便的运动捕捉系统。本文旨在通过深度学习方法，从6轴IMU数据中合成标准化的sEMG信号。
### Innovation
文章提出了一种基于膨胀因果卷积的滑动窗口WaveNet模型，用于将IMU数据映射到sEMG信号上。该方法新颖之处在于突破了传统sEMG信号的直接采集，利用更加便捷和可靠IMU数据进行模型训练。
### Conclusion
实验结果表明，该模型能够成功预测肌肉激活的时间和大致形态，尽管最大振幅往往被低估，但高时间保真度证明了该方法在假肢控制和康复生物反馈等应用中的可行性。
## 526. `cs.LG` - PepEVOLVE: 通过组相对优势实现位置感知的肽动态优化 [PDF](https://arxiv.org/pdf/2511.16912), [HTML](https://arxiv.org/abs/2511.16912)
### Authors
Trieu Nguyen,Hao-Wei Pang,Shasha Feng
### Background
宏环肽结合了生物制剂似的亲和力和小分子似的开发性，为药物研发提供了一种新途径。然而，由于其巨大的组合空间和多参数目标，先导优化过程既缓慢又具有挑战性。现有的生成式方法如PepINVENT需要化学家预先指定待优化的可变位置，并依赖静态预训练和优化算法，这限制了模型的泛化能力和优化肽序列的有效性。
### Innovation
PepEVOLVE引入了一种位置感知的动态框架，能够学习在哪里编辑以及如何动态优化肽以实现多目标改进。其特点包括使用动态掩码和CHUCKLES移位来增强预训练，使用上下文无关的多臂 bandit 路由器来发现高奖励残基，并结合了一种新的进化的优化算法与群体相关的优势来稳定强化学习更新。
### Conclusion
在体外评估中，PepEVOLVE的表现优于PepINVENT，在治疗上有动机的Rev结合环肽基准测试中，PepEVOLVE达到了更高的平均得分（约0.8对0.6），产生了最佳候选物（得分0.95对0.87），并且在优化渗透性和脂溶性并有结构约束的任务中更快地收敛。总体而言，PepEVOLVE提供了在目标编辑位点未知时进行肽先导优化的实际、可重复路径，有助于更高效地探索并提高多目标设计的质量。
## 527. `cs.LG` - 在层次强化学习中Q学习的收敛性和稳定性 [PDF](https://arxiv.org/pdf/2511.17351), [HTML](https://arxiv.org/abs/2511.17351)
### Authors
Massimiliano Manenti,Andrea Iannelli
### Background
层次强化学习有望高效捕捉和利用决策问题中的时间结构，并增强持续学习能力，但是理论保证与实践之间存在差距。
### Innovation
提出了Feudal Q学习方案，并探讨了其耦合更新在什么条件下会收敛且稳定。通过利用随机逼近理论和常微分方程方法，提供了一个关于Feudal强化学习收敛性和稳定性的原理性分析，同时还展示了更新可以收敛到一个可被解释为特定游戏中平衡点的点，为使用博弈论方法的层次强化学习打开了大门。
### Conclusion
实验表明Feudal Q学习算法的结果支持了理论上预期的成果。
## 528. `cs.LG` - SAM与SGD统一稳定性分析：数据相干性和简单性偏好的作用 [PDF](https://arxiv.org/pdf/2511.17378), [HTML](https://arxiv.org/abs/2511.17378)
### Authors
Wei-Kai Chang,Rajiv Khanna
### Background
随着深度学习模型的规模扩大，理解优化过程的动力学变得越来越重要。尽管随机梯度下降（SGD）及其变体可以找到泛化良好的解，但这些算法为何能实现良好泛化仍不明确。值得注意的是，在参数过拟合的情况下，这些算法往往会偏好更平坦或更简单的极小值。已有研究表明，平坦度与泛化性能相关，而像Sharpness-Aware Minimization (SAM)这样的方法则明确鼓励平坦度。然而，数据结构、优化动力学与学习解的本质之间的统一理论仍然缺失。
### Innovation
本研究开发了一个线性稳定性框架，用于分析SGD、随机扰动和SAM在两层ReLU网络中的行为。该框架的核心是一种相干性度量，能够量化梯度曲率在数据点上的对齐情况，揭示了为什么某些极小值在训练过程中是稳定且被偏好的原因。
### Conclusion
研究基于线性稳定性框架，深入探讨了数据相干性在理解SAM与SGD性能差异方面的作用，并揭示了简单性偏好的起源。
## 529. `cs.LG` - R2PS: 在部分可观测性下的最坏情况鲁棒实时追捕策略 [PDF](https://arxiv.org/pdf/2511.17367), [HTML](https://arxiv.org/abs/2511.17367)
### Authors
Runyu Lu,Ruochuan Shi,Yuanheng Zhu,Dongbin Zhao
### Background
在考虑现实世界因素如部分可观测性的情况下，计算追击逃脱游戏（PEGs）中的最坏情况鲁棒策略非常耗时。现有的强化学习方法如Equilibrium Policy Generalization (EPG)和Grasper仅适用于完美信息场景，无法处理逃逸者能够预测追击者行动的情况。
### Innovation
本文首次提出了在部分可观测性下的最坏情况鲁棒实时追捕策略（R2PS）。首先证明了传统的解决马尔可夫PEGs的动态规划算法在逃逸者异步行动时保持最优。然后提出了一种关于逃逸者可能位置的信念保持机制，将动态规划的追捕策略扩展到部分可观测性环境中。最后，将信念保持机制嵌入到最先进的EPG框架中，通过跨图强化学习生成实时追击者策略，该策略能够实现对未见过的实际图结构的鲁棒零样品泛化，并且优于现有游戏强化学习方法训练的策略。
### Conclusion
通过强化学习，我们的策略实现了对未见过的真实图结构的鲁棒零样品泛化，并且与现有方法训练的测试图结构策略相比，表现更为优异。
## 530. `cs.LG` - 借助后验采样的稳定核心集：诱导损失景观与完整损失景观的对齐 [PDF](https://arxiv.org/pdf/2511.17399), [HTML](https://arxiv.org/abs/2511.17399)
### Authors
Wei-Kai Chang,Rajiv Khanna
### Background
随着深度学习模型的不断扩大，计算需求的增加突显了有效核心集选择技术的需求。核心集选择旨在通过识别能够代表完整数据集性能的小部分数据来加速训练。尽管基于梯度的方法因其强大的理论基础和实际优势受到青睐，尤其是在数据预算受限的情况下，但这些方法依然面临挑战，比如朴素随机梯度下降成为强有力的基本方法，以及随时间损失曲率不匹配导致代表性失效。
### Innovation
本文提出了一种新型框架，解决了上述问题。其一，建立了后验采样与损失景观之间的联系，使在高数据污染情况下也能进行稳健的核心集选择。其二，引入了基于后验采样的平滑损失函数，增强了稳定性和泛化能力，同时保持计算效率。本文还提出了基于采样选择核心集的全新收敛分析。
### Conclusion
通过广泛的实验，本文展示了一种基于采样的核心集选择方法可以比当前最先进的方法更快地实现训练，并在多样的数据集上增强泛化能力。
## 531. `cs.LG` - 通过训练前投影强制液体偏微分方程求解器遵守守恒方程约束 [PDF](https://arxiv.org/pdf/2511.17258), [HTML](https://arxiv.org/abs/2511.17258)
### Authors
Omer Rochman,Gilles Louppe
### Background
神经网络偏微分方程(PDE)求解器在科学模拟中常违反守恒方程约束。虽然可以便宜地投影线性约束，但许多约束是非线性的，增加了投影到可行集的复杂性。动态PDE尤其难以处理，因为约束会导致长时间依赖性。
### Innovation
评估了两种无培训后处理投影：基于非线性优化的投影和基于雅可比-向量和向量-雅可比产品的局部线性化投影。分析跨代表性的PDE的约束，发现两者都能显著减少违反并提高准确度，优于物理信息的基础方法。
### Conclusion
两种无培训投影显著减少了违反并提高了基于神经网络的PDE求解器的精度，尤其是在处理复杂的非线性约束时。
## 532. `cs.LG` - ReBaPL: 排斥的贝叶斯指令学习 [PDF](https://arxiv.org/pdf/2511.17339), [HTML](https://arxiv.org/abs/2511.17339)
### Authors
Yassir Bendou,Omar Ezzahir,Eduardo Fernandes Montesuma,Gabriel Mahuas,Victoria Shevchenko,Mike Gartrell
### Background
指令调优已经成为了大规模基础模型应用在下游任务中的有效技术，然而常规的指令调优方法容易出现过拟合问题，且在处理不同的分布泛化时表现不佳。
### Innovation
本文提出了Repulsive Bayesian Prompt Learning（ReBaPL），该方法将指令优化问题重新构建为贝叶斯推理问题，通过循环步长计划和随机梯度哈密尔顿蒙特卡罗（SGHMC）算法交替探索和利用的不同阶段，以及一种基于不同指令生成的表示空间分布的概率度量函数衍生的排斥力，使得探索更为全面并防止早夭收敛至单一模式，从而提升了公式的泛化能力。本文的方法可以灵活集成到任何基于极大似然估计的现有指令学习方法中。
### Conclusion
实验结果表明，ReBaPL比起当前最先进的指令学习方法具有更好的性能。
## 533. `cs.LG` - 通过距离几何法流匹配生成化学反应过渡态 [PDF](https://arxiv.org/pdf/2511.17229), [HTML](https://arxiv.org/abs/2511.17229)
### Authors
Yufei Luo,Xiang Gu,Jian Sun
### Background
过渡态（TS）对于理解反应机制至关重要，但其探索受到实验和计算方法复杂性的限制。现有的方法难以捕获化学反应中分子间距离的动态变化。
### Innovation
提出了一种TS-DFM框架，这是一种流匹配框架，能够从反应物和产物中预测过渡态。通过在分子距离几何空间中操作，TS-DFM能够明确捕捉化学反应中原子间距离的变化。此外，设计了一种名为TSDVNet的网络结构来学习用于生成TS几何结构的速度场。实验表明，TS-DFM在基准数据集Transition1X上的结构准确性优于之前最先进的方法React-OT，提高了2.3倍。此框架还能够识别替代反应路径，甚至发现了能量更低的过渡态。
### Conclusion
TS-DFM不仅可以显著提高过渡态预测的准确性，还可以识别不同的反应路径，具有优异的普适性，为化学反应探索提供了有力工具。
## 534. `cs.LG` - Step-E：嘈杂标签下鲁棒学习的可微数据清洁框架 [PDF](https://arxiv.org/pdf/2511.17040), [HTML](https://arxiv.org/abs/2511.17040)
### Authors
Wenzhang Du
### Background
在野外收集的训练数据中通常包含噪声标签和异常值，这严重影响了深度神经网络的性能和可靠性。目前的数据清理通常作为独立的预处理步骤进行，但这种两阶段管道无法充分利用下游模型的反馈，也不能适应未知的噪声模式。
### Innovation
Step-E 提出了一种简单框架，将样本选择和模型学习整合到单一优化过程中。该框架在每个epoch中通过损失排名样本，并在短暂的预热阶段之后逐渐增加高损失样本被排除出梯度更新的比例，从而形成关注简单且一致样本的在线课程，并最终忽略持续的异常值。此方法在 CIFAR-100N 和 CIFAR-10N 数据集上的测试准确率显著提升，优于现有方法并接近干净标签的最优性能。
### Conclusion
Step-E 方法通过将数据收集和模型训练紧密结合，显著提高了在嘈杂标签数据上的学习效果，尤其在 CIFAR-100N 和 CIFAR-10N 数据集上的测试准确率大幅提升，且具有较低的训练时间开销，接近无噪数据的最优预测结果。
## 535. `cs.LG` - SAVeD：语义感知版本发现 [PDF](https://arxiv.org/pdf/2511.17298), [HTML](https://arxiv.org/abs/2511.17298)
### Authors
Artem Frenk,Roee Shraga
### Background
在数据科学中，由于类似工作的重复劳动及对数据集的多次变换，存在着识别数据集版本的挑战。现有方法通常依赖元数据、标签或基于集成的假设来标识数据集的版本，而这些方法往往依赖外部信息，这限制了它们的独立性和鲁棒性。
### Innovation
SAVeD 是一种基于对比学习的方法，用于在不依赖元数据、标签或集成假设的情况下识别结构化数据集的不同版本。通过修改 SimCLR 架构，SAVeD 生成表格的随机变换视图（如行删除、编码扰动），通过自定义变压器编码器将这些视图嵌入，并在潜在空间中对比，优化语义相似性。这种方法有效地降低了相同数据集视图之间的距离，同时最大化无关表格之间的距离。
### Conclusion
实验结果表明，SAVeD 在识别未见过的表格版本上取得了显著的准确率，并显著提升了分离分数，验证了其区分语义变化版本的能力。与未训练的基础模型和此前的基准方法（如 Starmie）相比，自定义编码器在这方面的性能取得了竞争性的或优越的结果，显示了其在独立标识数据集版本上的优势。
## 536. `cs.LG` - FlexiFlow: 分解流匹配生成灵活分子集合 [PDF](https://arxiv.org/pdf/2511.17249), [HTML](https://arxiv.org/abs/2511.17249)
### Authors
Riccardo Tedoldi,Ola Engkvist,Patrick Bryant,Hossein Azizpour,Jon Paul Janet,Alessandro Tibo
### Background
基于三维结构和最有利构象的药物发现是关键挑战。当前最先进的3D从头设计模型只生成单一构象，而分子的构象图谱决定了其可观察性质和与特定蛋白靶标的结合能力。为了更直接地评估这些性质，需要生成一组具有代表性的低能构象分子。然而，现有的模型难以满足这种需求。
### Innovation
我们提出了一种新的架构FlexiFlow，扩展了流匹配模型，可以在保持维数不变性和置换不变性的前提下，同时采样分子和多种构象。我们在QM9和GEOM Drugs数据集上展示了该方法的有效性，达到了在分子生成任务中的最新成果。此外，我们的模型在推理速度上比物理方法更快速，并且能够成功转移到基于蛋白质条件的配体生成任务。
### Conclusion
 FlexiFlow能够生成有效、无应变、独特且新颖的分子，并且以高度的可靠性匹配训练数据分布，同时捕捉分子的构象多样性。此外，该模型生成的构象集合在覆盖方面与最先进的物理方法相当，且耗时仅为几十分之一。最后，FlexiFlow可以成功应用于只包含静态口袋而不伴有构象的数据集，实现了蛋白条件下的配体生成任务。
## 537. `cs.LG` - 汽车需求预测：时空和层次建模、生命周期动力学和用户生成的在线信息 [PDF](https://arxiv.org/pdf/2511.17275), [HTML](https://arxiv.org/abs/2511.17275)
### Authors
Tom Nahrendorf,Stefan Minner,Helfried Binder,Richard Zinck
### Background
高端汽车制造商面临日益复杂的预测挑战，原因包括高产品多样性、稀疏的变体级数据和不稳定的市场动态。为此，本研究使用来自德国高端制造商的数据，对多产品、多市场、多层级的月度汽车需求进行了跨战略和运营规划层面的点和概率预测。研究结果显示，时空依赖关系以及四舍五入偏差对预测准确性有显著影响，强调了进行整数预测以保障操作可行性的重要性。Shapley分析表明，短期需求是反应性的，受生命周期成熟度、自回归动量和操作信号的影响；而中期需求反映了前瞻性因素，如在线参与度、规划目标和竞争指标，且在线行为数据在细分层面大幅提升了预测精度。
### Innovation
该研究结合了LightGBM模型的点和概率预测，通过合并训练集、分位数回归和混合整数线性规划校准方法，实现跨战略和运营规划层级的预测。研究成果揭示了时空依赖关系和四舍五入偏差对预测准确性的影响，特别是在操作可行性方面的重要性，并通过Shapley分析区分了短期和中期需求的不同驱动因素。
### Conclusion
研究结果强调了时空依赖性和四舍五入偏差对预测准确性的影响，以及在线行为数据在提高预测精度方面的作用，并提出了针对运营可行性的整数预测的重要性。研究为汽车制造商提供了一套高度细化和准确的预测方法，帮助其更好地应对市场需求的变化。
## 538. `cs.LG` - 通过曲率对齐的自我监督学习 [PDF](https://arxiv.org/pdf/2511.17426), [HTML](https://arxiv.org/abs/2511.17426)
### Authors
Benyamin Ghojogh,M.Hadi Sepanj,Paul Fieguth
### Background
近期，非对比学习方法通过将不变性项与方差、协方差或冗余减少惩罚相结合，推动了自我监督学习（SSL）的发展。这些方法影响了表示的一阶和二阶统计，但很大程度上忽略了底层数据流形的局部几何结构。
### Innovation
本文引入了一种新的曲率正则化自我监督学习框架CurvSSL及其核希尔伯特空间（RKHS）扩展版，称为核CurvSSL。该方法保留了标准的两视图编码器-投影器架构，并采用了Barlow Twins风格的冗余减少损失，但增加了基于曲率的正则化器。每个嵌入被视为顶点，其k个最近邻通过余弦交互定义曲率分数，核变体则通过核希尔伯特空间中的规范化局部格拉姆矩阵计算曲率。这些分数通过Barlow风格的损失在不同增强中对齐和去相关，以同时鼓励视图不变性和局部流形弯曲的一致性。
### Conclusion
在MNIST和CIFAR-10数据集上使用ResNet-18主干的实验表明，曲率正则化SSL在与Barlow Twins和VICReg相比时，线性评估性能具有竞争力或更好。我们的结果表明，明确塑造局部几何结构是对纯粹统计学SSL正则化器的一个简单且有效的补充。
## 539. `cs.LG` - SafeR-CLIP：在保留预训练知识的同时缓解视觉-语言模型中的成人内容 [PDF](https://arxiv.org/pdf/2511.16743), [HTML](https://arxiv.org/abs/2511.16743)
### Authors
Adeel Yousaf,Joseph Fioresi,James Beetham,Amrit Singh Bedi,Mubarak Shah
### Background
通过微调来提高类似于CLIP的视觉-语言模型的安全性通常会付出高昂代价，导致其泛化性能显著下降。这种权衡来自于强制将不安全的概念与单一预定义的安全目标对齐，从而破坏了模型学习到的语义结构。
### Innovation
提出了就近感知的方法，即转向最接近的语义安全替代概念，以最小化表示变化，由此制定了SaFeR-CLIP框架。该框架成功实现了安全与性能的平衡，在零样本准确性上比先前的方法提高了8.0%，同时还保持了鲁棒性。为了支持更严格的评估，还贡献了NSFW-Caps基准，包含1000对高度对齐的数据，用于测试在分布变化下的安全性。
### Conclusion
研究表明，在不牺牲性能的前提下实现安全性，关键在于尊重预训练表示的几何结构。
## 540. `cs.LG` - 超越过拟合的成员推断攻击 [PDF](https://arxiv.org/pdf/2511.16792), [HTML](https://arxiv.org/abs/2511.16792)
### Authors
Mona Khalil,Alberto Blanco-Justicia,Najeeb Jebreel,Josep Domingo-Ferrer
### Background
针对机器学习模型的成员推断攻击（MIAs）旨在确定给定的数据点是否为模型训练数据的一部分。这些攻击可能会对那些敏感数据用于训练的个体产生重大隐私风险，促使使用差分隐私等防御措施，但通常会损失高准确性。MIAs利用模型在预测训练期间见过（成员）和没见过（非成员）的样本时行为上的差异。研究表明，模型过拟合是这些行为差异的主要因素，进而导致MIAs的成功。然而，文献也指出，即使是未过拟合的机器学习模型也可能泄露有关其训练数据一部分的信息。
### Innovation
本文探讨了超越传统过拟合关切的成员推断漏洞的根本原因，并建议针对性的防御策略。我们通过实证分析未过拟合模型中易受MIAs影响的训练数据样本的特征。研究发现，这些样本通常是类中的离群值（例如，有噪声或难以分类的样本）。随后，我们提出了潜在的防御策略，以保护这些易受攻击的样本并增强机器学习模型的隐私保护能力。
### Conclusion
我们的研究表明，这些易受攻击的样本往往位于其类中的异常位置。为防止这些样本被攻击，我们提出了潜在的防御策略，并增强了机器学习模型保护隐私的能力。我们已将代码发布在网络上。
## 541. `cs.LG` - 揭开空中威胁的秘密：基于字典引导的变换器在便携式气溶胶质谱中的应用 [PDF](https://arxiv.org/pdf/2511.17446), [HTML](https://arxiv.org/abs/2511.17446)
### Authors
Kyle M. Regan,Michael McLoughlin,Wayne A. Bryden,Gonzalo R. Arce
### Background
矩阵辅助激光解吸电离质谱（MALDI-MS）是生物分子分析的重要基石，能够通过独特的质谱签名精准识别病原体。然而，MALDI-MS 依赖于耗时的手动样品准备和多级光谱平均，只能在实验室环境中使用，限制了其实时环境监测的适用性。特别是在新兴的气溶胶 MALDI-MS 系统中，自主采样会生成噪声较大的光谱，需要依靠单次光谱检测来进行有效分析。
### Innovation
我们提出了 Mass Spectral Dictionary-Guided Transformer (MS-DGFormer)：一种数据驱动的框架，可以直接处理原始、简化的质谱数据。MS-DGFormer 利用了变压器架构来捕捉这些时序光谱中的长程依赖关系。我们还引入了新型字典编码器，结合了通过广义 singular value decomposition (SVD) 处理的去噪光谱信息，使模型能够在单次光谱检测中从噪声光谱中识别出关键生物分子模式，提高了分析性能。这项创新提供了一种系统，能够从空气样品中实现更优的病原体识别，并实现在现场条件下的自动实时分析。通过消除繁重前期处理的需要，我们的方法为便携式 MALDI-MS 平台铺平了道路，从而革新了环境病原体检测及生物威胁的快速响应。
### Conclusion
该研究提出了一种新的方法，使 MALDI-MS 在现场条件下实现自动和实时的病原体检测成为可能。这一突破将为便携式MALDI-MS平台的发展铺平道路，革新环境病原体检测和生物威胁的快速响应机制。
## 542. `cs.LG` - DS-Span: 单阶段区分性子图挖掘用于高效图嵌入 [PDF](https://arxiv.org/pdf/2511.17419), [HTML](https://arxiv.org/abs/2511.17419)
### Authors
Yeamin Kaiser,Muhammed Tasnim Bin Anwar,Bholanath Das,Chowdhury Farhan Ahmed,Md. Tanvir Alam
### Background
图表示学习旨在将复杂的高维图结构转换为保留拓扑和语义的紧凑向量空间。在各种策略中，基于子图的方法为符号模式发现和连续嵌入学习之间提供了一个可解释的桥梁。然而，现有的频繁或区分性子图挖掘方法往往存在冗余的多阶段流水线、高计算成本以及挖掘结构与区分相关性之间弱耦合的问题。
### Innovation
本文提出了DS-Span，这是一种单阶段区分性子图挖掘框架，它在搜索空间的一次遍历中统一了模式生长、剪枝和监督驱动评分。DS-Span引入了一种覆盖上限的资格机制，动态限制探索，一旦图得到充分表示即停止探索；以及一种基于信息增益的选择机制，促进具有强类别区分能力的子图同时最小化冗余。
### Conclusion
广泛的基准测试表明，DS-Span生成的子图特征比之前的多阶段方法更加紧凑和区分性，同时显著降低了运行时间，从而得到了更高的或可比的准确性。这些结果突显了单阶段、统一的区分性挖掘作为一种可扩展和可解释的图表示学习基础的强大潜力。
## 543. `cs.LG` - 具有Veros的全可微神经海洋模型 [PDF](https://arxiv.org/pdf/2511.17427), [HTML](https://arxiv.org/abs/2511.17427)
### Authors
Etienne Meunier,Said Ouala,Hugo Frezat,Julien Le Sommer,Ronan Fablet
### Background
本文介绍了一个可微分扩展的VEROS海洋模型，使其能够通过其动力学核心实现自动微分。该研究描述了使模型完全兼容JAX自动微分框架所需的关键更改，并评估了该实现的数值一致性。通过这两个演示应用，本文展示了不同程序设计如何促进海洋建模中的端到端学习和参数调整。
### Innovation
本文创新性地将自动微分技术应用到VEROS海洋模型中，使得模型的优化环节可以进行端到端的训练和参数调整。通过利用Veros进行具体的应用案例展示，验证了该方法的可行性和有效性。
### Conclusion
本文展示了如何利用不同程序设计来促进海洋建模中的端到端学习和参数调整。具体应用实例证明了此方法的有效性，同时所实现的可微分VEROS模型已公开可用。
## 544. `cs.LG` - PersonaAgent with GraphRAG: Community-Aware Knowledge Graphs for Personalized LLM [PDF](https://arxiv.org/pdf/2511.17467), [HTML](https://arxiv.org/abs/2511.17467)
### Authors
Siqi Liang,Yudi Zhang,Yue Guo
### Background
研究背景在于需要创造个性化的AI代理，以适应个体用户的需求和偏好。现有方法缺乏有效利用丰富背景信息的能力，导致代理不能很好地保持一致且个性化的行为。因此，提出了一种基于个性特征的语言模型系统框架。
### Innovation
创新之处在于提出了一种新的基于个性特征的语言模型系统框架，其中代理通过大型语言模型（LLM）承载用户的“个性”（例如用户档案或品味）。为了使代理能够利用丰富的上下文信息，引入了一种知识图谱增强的检索增强生成（Graph RAG）机制，该机制构建了一个从LLM中提取的相关文档图表索引，并总结了相关内容社区。通过结合用户的过往行为和偏好摘要以及通过图谱社区检测识别的相关全球交互模式，动态生成个性化提示。
### Conclusion
该框架在LaMP基准测试中的表现优于以往方法：新闻分类F1指标提升11.1%，电影标签F1指标提升56.1%，产品评分MAE指标降低10.4%。相关代码已发布。
## 545. `cs.LG` - 多代理指针转换器：序列到序列强化学习在多车辆动态取送货问题中的应用 [PDF](https://arxiv.org/pdf/2511.17435), [HTML](https://arxiv.org/abs/2511.17435)
### Authors
Zengyu Zou,Jingyuan Wang,Yixuan Huang,Junjie Wu
### Background
本文讨论了带有随机请求的多车辆动态取送货问题（MVDPDPSR），这是车辆路径问题的扩展及时空系统优化问题，广泛应用于按需配送等场景。经典运筹学方法在处理大规模动态问题时面临着计算复杂性和时间效率的瓶颈。尽管现有的强化学习方法取得了一定进展，但它们仍面临独立解码跨多个车辆难以建模联合动作分布、特征提取网络难以捕捉实体间关系以及联合动作空间指数级增加等问题。
### Innovation
为此，本文提出了基于序列到序列的多代理指针变换器（MAPT）。MAPT框架采用Transformer编码器提取实体表示，结合Transformer解码器和指针网络以自回归方式生成联合动作序列，并引入关系感知注意力模块来捕捉实体间关系。此外，通过使用指导性先验来引导模型决策，促进有效探索。
### Conclusion
在8个数据集上的实验结果表明，MAPT在性能上显著优于现有的基准方法，并且在计算时间上优势显著，相对于经典运筹学方法展现出巨大的时间性能优势。
## 546. `cs.LG` - LLM驱动的自动程序修复中，补丁是否仍然比病症更严重？测试过拟合问题 [PDF](https://arxiv.org/pdf/2511.16858), [HTML](https://arxiv.org/abs/2511.16858)
### Authors
Toufique Ahmed,Jatin Ganhotra,Avraham Shinnar,Martin Hirzel
### Background
之前的研究已经表明，自动化程序修复可能会产生只通过已见测试但未见测试仍会失败的修复代码。这一问题被称为测试过拟合，并在大型语言模型出现之前就已有所理解和研究。本文通过仓库级别的SWE-bench任务，实验性地探讨当前测试过拟合是否仍然是一个问题。
### Innovation
本文通过使用仓库级别的SWE-bench任务，实验性地评估当前自动化程序修复中的测试过拟合问题，在大型语言模型出现后的背景下继续探讨这一问题。
### Conclusion
本文实验结果表明，测试过拟合问题在大型语言模型的应用背景下仍然存在，需要进一步的研究和改进来解决这个问题。
## 547. `cs.LG` - InTAct:基于区间的任务激活汇总在持续学习中的应用 [PDF](https://arxiv.org/pdf/2511.17439), [HTML](https://arxiv.org/abs/2511.17439)
### Authors
Patryk Krukowski,Jan Miksa,Piotr Helm,Jacek Tabor,Paweł Wawrzyński,Przemysław Spurek
### Background
持续学习旨在使神经网络能够在不遗忘之前学到的信息的情况下获取新知识。虽然基于提示的方法在类别增量设置中表现出色，但在输入分布变化而标签空间保持不变的情况下，它们仍然容易受到域变换的影响。这导致了特征表示漂移的问题，即共享表示以覆盖之前有用特征的方式进行演变，导致即使在提示隔离了特定任务参数时也会出现遗忘。
### Innovation
我们引入了InTAct方法，该方法通过保存共享层的功能行为而不冻结参数或存储过去的数据，来解决这一问题。InTAct捕获与之前学习的任务相关的特征激活范围，并通过确保网络在这些区域保持一致来限制更新，同时允许在其他地方进行灵活的适应。InTAct通过调节以往知识编码的地方的表现变化，实现稳定性和可塑性之间的原则性平衡。
### Conclusion
在DomainNet和ImageNet-R等不同的域增量基准测试中，InTAct在减少特征表示漂移并提高性能方面表现出色，平均精度提高了高达8个百分点，超过了最先进的基线方法。InTAct适用于各种架构，并无缝集成到现有的基于提示的持续学习框架中。
## 548. `cs.LG` - 高效基于惩罚的 bilevel 方法：改进分析、新型更新和平坦度条件 [PDF](https://arxiv.org/pdf/2511.16796), [HTML](https://arxiv.org/abs/2511.16796)
### Authors
Liuyuan Jiang,Quan Xiao,Lisha Chen,Tianyi Chen
### Background
惩罚方法因其有效的一阶性质已成为解决 bilevel 优化问题的流行选择。然而，这些方法通常需要内部循环迭代来解决下层问题，并且需要较小的外部循环步长来处理由大型惩罚项引起的增加平滑性，这导致了次优化的复杂度。
### Innovation
该研究着眼于具有耦合约束的一般 bilevel 问题，并引入了一个新的惩罚重述方法来解除上下层变量之间的耦合。这导致了更高的光滑性常数分析，使得 Penalty-Based Gradient Descent 算法在交替模式下具有更大的步长和更低的迭代复杂度。基于减少的光滑性，该研究提出了 PBGD-Free，这是一个全新的单环算法，避免了解耦约束条件下 bilevel 问题的内部循环。还提出了一种新的曲率条件，描述了上层目标函数相对于下层变量的“平坦性”，放宽了传统的上层 Lipschitz 要求，允许选择更小的惩罚常数，并且在更新上层变量时导致忽略惩罚梯度项。
### Conclusion
研究提供了严格的收敛分析，并通过支持向量机的超参数优化和大型语言模型的微调验证了该方法的有效性。
## 549. `cs.LG` - 在神经网络场论中的费米子与超对称性 [PDF](https://arxiv.org/pdf/2511.16741), [HTML](https://arxiv.org/abs/2511.16741)
### Authors
Samuel Frank,James Halverson,Anindita Maiti,Fabian Ruehle
### Background
通过将格拉斯曼值神经网络应用于场论，引入了费米子神经网络场理论。自由理论通过将中心极限定理推广到格拉斯曼变量获得。这种方法使无限宽度下自由狄拉克自旋子和有限宽度下的四费米相互作用得以实现。通过打破费米子和玻色子场的统计独立性，引入了约化耦合。进一步，通过超仿射变换将输入转化为超空间形式，引入了一大类相作对称的量子力学和场理论模型。
### Innovation
提出了一种使用格拉斯曼值神经网络的费米子神经网络场理论。这一理论通过中心极限定理的推广到格拉斯曼变量使得在无限宽度下实现自由狄拉克自旋子和在有限宽度下实现四费米相互作用成为可能。约化耦合的引入是通过打破费米子和玻色子场的统计独立性实现的。此外，利用超仿射变换，引入了一系列相作用的量子力学和场理论模型。
### Conclusion
该理论为神经网络场论的费米子和超对称性提供了新的视角，展示了如何在神经网络框架内模拟复杂的量子物理现象。其所带来的约化耦合和超空间模型具有重要的理论意义和潜在的应用价值。
## 550. `cs.LG` - 通过代表对齐解决逆问题：使用扩散和流模型 [PDF](https://arxiv.org/pdf/2511.16870), [HTML](https://arxiv.org/abs/2511.16870)
### Authors
Loukas Sfountouris,Giannis Daras,Paris Giampouras
### Background
研究表明，通过将扩散或流动生成模型的内部表示与预训练的自监督编码器的内部表示对齐，可以显著提高生成模型的收敛性和样本质量。本文将这一想法应用于逆问题中，使用预训练生成模型作为先验。
### Innovation
提出了在生成模型和预训练自监督视觉编码器（如DINOv2）之间应用表示对齐（REPA），以在逆问题的推理过程中指导重建过程。尽管逆问题中没有地面真实信号，我们展示了与DINOv2嵌入空间中近似目标特征对齐能够显著提高重建保真度和感知逼真度。该研究还提供了理论结果，解释了REPA正则化的表示对齐在提升感知保真度方面的作用。
### Conclusion
研究将方法集成到多个最先进的逆问题求解器中，实验证明，该方法在多个任务上都能够改善重建质量，并且通过减少所需的离散化步骤，还能提供显著的效率提升，而不影响底层求解器的性能。
## 551. `cs.LG` - 从聚类的LQR系统中利用数据：个性化协作策略优化 [PDF](https://arxiv.org/pdf/2511.17489), [HTML](https://arxiv.org/abs/2511.17489)
### Authors
Vinay Kanakeri,Shivam Bajaj,Ashwin Verma,Vijay Gupta,Aritra Mitra
### Background
强化学习（RL）的数据需求量大。为了提高RL的学习效率，已有研究提出使学习算法利用与被控制过程“大致相似”的过程的数据。由于过程模型未知，识别哪些过程是相似的是一项挑战。本文研究了此问题在基准线性二次调节器（LQR）设置中的情况。具体地，文章考虑了一个多个代理（每个代理对应一个需要控制的线性过程副本）的设置，他们的本地过程可以根据动力学和任务的相似性进行聚类。结合顺序消除和零阶策略优化的理念，提出了一个新算法，同时进行聚类和学习，生成每个聚类的个性化策略（控制器）。
### Innovation
提出了一种新的算法，在一个聚类的LQR系统的设置中，同时实现了聚类和学习，生成每个聚类的个性化策略。证明了这种方法在高概率下能够正确聚类。此外，策略的次优性差距与聚类大小成反比，与先前基于协作学习的控制工作中仅有集合数据时的偏差不同。这是首次展示了如何利用聚类以从数据驱动控制中学习享受协作统计增益的个性化策略，同时不因包括不相似的过程的数据而遭受次优性。
### Conclusion
从分布式实施的角度来看，本文的方法具有吸引力，因为它仅带来了轻微的对数通信开销。
## 552. `cs.LG` - Bench360: 360度评估本地大语言模型推理 [PDF](https://arxiv.org/pdf/2511.16682), [HTML](https://arxiv.org/abs/2511.16682)
### Authors
Linus Stuhlmann,Mauricio Fadel Argerich,Jonathan Fürst
### Background
本地运行大型语言模型（LLMs）变得越来越普遍。尽管小型开源模型和推理引擎的可用性增加，降低了门槛，但用户现在面临着大量的配置选择，手动找到最佳配置（平衡功能和非功能要求）需要大量工作。现存的基准测试主要针对LLM推理，但目标狭窄且用户导向不足，缺乏统一、易用的基准测试，能够综合系统和任务特定的指标，支持多种推理引擎、使用场景和量化级别。
### Innovation
Bench360是一个全方位评估本地LLM推理的基准测试框架。它让用户能够轻松自定义任务、数据集和任务特定指标，并自动跨不同使用场景（单流、批处理及服务器）评估所选的LLMs、推理引擎和量化级别。Bench360跟踪广泛指标，包括系统指标（计算性能、资源使用、部署等）和任务特定指标（如ROUGE、F1分数或准确率）。通过在四种常见LLM任务（通用知识与推理、问答、总结和文本到SQL）以及三种硬件平台上应用Bench360，揭示了任务性能和系统效率之间的有趣权衡，突出了不同推理引擎和模型的差异。
### Conclusion
除非有Bench360这样的框架支持，否则没有单一的最佳本地推理配置，这凸显了Bench360框架的重要性。
## 553. `cs.LG` - 深度改进监督 [PDF](https://arxiv.org/pdf/2511.16886), [HTML](https://arxiv.org/abs/2511.16886)
### Authors
Arip Asadulaev,Rayan Banerjee,Fakhri Karray,Martin Takac
### Background
最近的研究表明，小型循环架构如Tiny Recursive Models (TRM)在复杂推理任务中，包括抽象与推理语料库（ARC）的表现超越了大型语言模型（LLM）。因此，此研究进一步探讨如何在最小改动的前提下提高TRM方法的效率。
### Innovation
本文通过将TRM的潜在推理视作 classifier-free 指导和隐式策略改进算法，并提出了一种新的训练方案，该方案在训练过程中为每个循环提供目标。此方法显著提高了训练效率，大大减少了前向传播次数并消除了停止机制，同时保持了与标准TRM相当的质量。研究还表示在仅使用0.8M参数的情况下，达到24%的ARC-1准确性，超越了大部分LLM。
### Conclusion
该研究证明了一种新的训练方案能够大幅提高TRM的效率和准确性，为小型循环架构在复杂任务中的应用提供了新的视角并提供了现实可行的结果。
## 554. `cs.LG` - 在AI基准中的神奇错误及其发现之道 [PDF](https://arxiv.org/pdf/2511.16842), [HTML](https://arxiv.org/abs/2511.16842)
### Authors
Sang Truong,Yuheng Tu,Michael Hardy,Anka Reuel,Zeyu Tang,Jirayu Burapacheep,Jonathan Perera,Chibuike Uwakwe,Ben Domingue,Nick Haber,Sanmi Koyejo
### Background
基准在人工智能的进步中起着关键作用，但频繁出现的无效基准问题会削弱其可靠性。手动识别和纠正成千上万的基准问题不仅不可行，而且也成为了可靠评估的关键瓶颈。
### Innovation
作者提出了一个系统性的基准修订框架，利用统计学分析响应模式来标记潜在的无效问题，以便进一步由专家进行审查。此方法基于人工智能评估中最常用的核心假设：平均得分能充分概述模型表现。这意味着存在一个潜在的一维量表，从而可以让每个项目有预期的统计值范围。当这些统计值的实测值超出项目的预期范围，该项目就可能存在问题。此方法在九个广泛使用的基准中帮助专家以高达84%的精度识别出有问题的问题，并引入了LLM法官的第一轮评审，进一步减少了人力投入。
### Conclusion
这些组成部分共同提供了一个高效且可扩展的框架，用于系统性的基准修订。
## 555. `cs.LG` - 边缘设备上的实时烹饪食品图像合成和视觉烹饪进度监控 [PDF](https://arxiv.org/pdf/2511.16965), [HTML](https://arxiv.org/abs/2511.16965)
### Authors
Jigyasa Gupta,Soumya Goyal,Anil Kumar,Ishan Jindal
### Background
当前，从原材料生成逼真的烹饪食品图像是一项具有挑战性的生成任务，因为模型需要捕捉烹饪过程中复杂的变化，包括纹理、颜色和结构上的变化。现有图像到图像生成方法往往生成的结果不现实，或者过于耗资源，不适合边缘部署。
### Innovation
作者引入了首个基于炉子的烹饪进度数据集，包含厨师标注的熟度等级，并提出了一种边缘高效的带有食谱和烹饪状态的生成器，能够在保持原始食品图像的基础上合成逼真的食品图像。此外，为了确保时间和烹饪上的连贯性，作者引入了一种领域特定的“烹饪图像相似性”（CIS）度量标准，作为训练损失和进度监测信号。
### Conclusion
实验结果显示，该模型在FID分数方面优于现有基线显著降低（在自建数据集上提高30%；在公共数据集上提高60%），在边缘设备上的实时烹饪食品图像合成和视觉烹饪进度监控方面具有显著优势。
## 556. `cs.LG` - 一种优化多样性的深度集成方法以实现准确的植物叶片病害检测 [PDF](https://arxiv.org/pdf/2511.16982), [HTML](https://arxiv.org/abs/2511.16982)
### Authors
Sai Nath Chowdary Medikonduru,Hongpeng Jin,Yanzhao Wu
### Background
植物疾病对全球农业构成重大威胁，导致每年超过220亿美元的经济损失并威胁食品安全。及时和准确地从植物叶片图像中检测这些疾病对于减轻其负面影响至关重要。深度神经网络集成（Deep Ensembles）通过利用多种深度神经网络的优势来增强预测准确性，成为一种强大的方法。但是，选择高绩效的集成成员模型具有挑战性，因为现有的集成多样性度量（Q指标）往往无法识别出最佳集成团队。
### Innovation
本文提出了一种名为Synergistic Diversity（SQ）框架，以提升植物疾病检测的准确性。首先，我们对现有集成多样性指标（Q指标）的局限性进行了全面分析，这些指标往往无法识别出最优集成团队。其次，我们提出了SQ指标，这是一种新颖的度量方法，能够捕捉集成成员之间的协同效应，并且始终与集成准确性保持一致。最后，通过在植物叶片图像数据集上进行广泛的实验验证了我们的SQ方法，结果表明我们的SQ指标显著改善了集成选择，提升了检测准确性。
### Conclusion
我们的研究结果为基于图像的植物疾病检测提供了一个更可靠和高效的解决方案。
## 557. `cs.LG` - 基于生成模型的MIMO波束地图构建以实现位置恢复和波束跟踪 [PDF](https://arxiv.org/pdf/2511.17007), [HTML](https://arxiv.org/abs/2511.17007)
### Authors
Wangqian Chen,Junting Chen,Shuguang Cui
### Background
机器学习（ML）大大推进了无线通信系统中数据驱动的信道建模和资源优化，但大多数基于ML的方法依赖于大量准确标记、带有位置信息的数据集，而获取这类数据集往往成本高昂且困难重重。本文提出了一个生成框架，该框架可以从稀疏信道状态信息（CSI）测量序列中直接恢复位置标签，而不需要显式的地理位置信息来构建无线电图。
### Innovation
本文设计了双尺度特征提取方案以增强特征表示，结合角度空间内的相关特征和邻近样本之间的特征相关性。提出了一种混合递归-卷积编码器来学习移动模式，并设计了一种受限策略和多尺度卷积以确保特征在短期波动中的稳健性。与传统的潜在空间中的高斯先验不同，本文嵌入了可学习的无线地图来捕捉位置信息，通过从CSI测量中编码高级位置特征。最后，通过条件生成解码器在无线电图的位置特征上重建高保真的CSI。
### Conclusion
数值实验表明，所提出模型可以将定位精度提高超过30%，在非视线（NLOS）场景中与基于模型的卡尔曼滤波器方法相比实现20%的容量增益。
## 558. `cs.LG` - AutoGraphAD：使用变分图自编码器进行异常网络流量检测的新型方法 [PDF](https://arxiv.org/pdf/2511.17113), [HTML](https://arxiv.org/abs/2511.17113)
### Authors
Georgios Anyfantis,Pere Barlet-Ros
### Background
网络入侵检测系统（NIDS）是检测网络攻击和入侵的重要工具。尽管大量的研究已经探索了使用监督机器学习进行攻击检测和分类的方法，但这些方法需要准确标记的数据集，而这很昂贵。此外，现有的公共数据集包含有限或过时的攻击，并且许多数据集存在标记错误的问题。
### Innovation
提出了一种基于异质变分图自编码器的新颖无监督异常检测方法—AutoGraphAD。该方法不依赖于任何标记数据，而是使用无监督和对比学习进行训练。通过权衡重建损失、结构损失和KL散度来生成异常得分，进而用于异常检测。总体而言，AutoGraphAD 在性能上与之前的无监督方法（如 Anomal-E）相当，甚至更好，但不需要昂贵的下游异常检测器，从而实现了大约 1.18 个数量级的训练速度和 1.03 个数量级的推理速度的提升。
### Conclusion
AutoGraphAD实现了无监督异常检测的高效部署，并且在性能上取得了显著改善，为实际部署提供了显著优势。
## 559. `cs.LG` - 层间权重选择以实现高效神经网络加速 [PDF](https://arxiv.org/pdf/2511.17123), [HTML](https://arxiv.org/abs/2511.17123)
### Authors
Jiaxun Fang,Li Zhang,Shaoyi Huang
### Background
 systolic array加速器执行CNN时，能量消耗主要由乘积运算（MAC）单元的切换活动决定。尽管之前的工作已经利用了权重相关的MAC功率来进行压缩，但现有方法经常使用全局激活模型、粗略的能量代理或跨层策略，这限制了它们在实际硬件上的效果。
### Innovation
该论文提出了一种能量感知的，按层压缩框架，该框架显式地利用了MAC和层级能量特性。首先，构建了一个层敏感的MAC能量模型，该模型结合了每层的激活统计数据，并使用22位partial sum转换的MSB-Hamming距离进行分组。此模型与tile级别的阵列映射相结合，以估算卷积层的能量。在此基础上，引入了一个在量化感知训练中与能量精度协同优化的权重选择算法，以及一种能量优先的按层调度策略，以在全局精度约束下更多地压缩高能量层，从而实现高效神经网络加速。
### Conclusion
实验表明，不同的CNN模型在2-3%的精度损失下，能量降低了高达58.6%，并且超过了一个最先进的能量感知基线。
## 560. `cs.LG` - OmniLens++：通过大型透镜库预训练和潜在点扩散函数表示实现盲透镜畸变校正 [PDF](https://arxiv.org/pdf/2511.17126), [HTML](https://arxiv.org/abs/2511.17126)
### Authors
Qi Jiang,Xiaolong Qian,Yao Gao,Lei Sun,Kailun Yang,Zhonghua Yi,Wenyong Li,Ming-Hsuan Yang,Luc Van Gool,Kaiwei Wang
### Background
当前研究领域中已有的一些盲透镜畸变校正管道，如深度学习方法，面临数据扩展的挑战和缺乏先验指导的缺陷，这限制了其在处理多种未知光学退化方面的泛化能力。
### Innovation
文章提出了一种名为OmniLens++的新框架，该框架通过改进数据扩展和引入先验指导来解决现有管道的泛化能力问题。具体创新包括：1）通过增加透镜源头的退化多样性并量化退化分布的时空变化和严重性来改善数据扩展；2）提出“潜在点扩散函数表示”（Latent PSF Representation, LPR），利用点扩散函数作为盲退化校正的指导。
### Conclusion
OmniLens++框架在处理真实和合成透镜的多样化畸变方面表现出卓越的泛化能力，能够有效校正盲透镜畸变。此外，实验验证了AODLibpro作为广泛训练基础的可扩展性，并表明LPR能够充分发挥大规模透镜库的潜在价值。源代码和数据集将在指定网址公开提供。
## 561. `cs.LG` - FireScope:利用链式思维预言机预测野火风险 [PDF](https://arxiv.org/pdf/2511.17171), [HTML](https://arxiv.org/abs/2511.17171)
### Authors
Mario Markov(1),Stefan Maria Ailuro(1),Luc Van Gool(1),Konrad Schindler(2),Danda Pani Paudel(1 and 2) ((1) INSAIT, Sofia University, (2) ETH Zurich)
### Background
野火风险预测是一个需要整合视觉、气候和地理因素的认知密集型空间问题，旨在推断连续的风险地图。现有方法缺乏必要的因果推理和多模态理解能力，无法实现可靠的泛化。
### Innovation
提出了一种名为FireScope-Bench的大型数据集和基准，结合了Sentinel-2图像、气候数据和美国专家定义的风险图以及欧洲的野火事件，用于跨大陆评估。在此基础上，提出了一种基于VLM的推理到生成框架FireScope。该框架通过结合强化学习和视觉监督，从两种模态获取互补的推理轨迹以预测风险图。该方法在北美训练并在欧洲测试时取得了显著的性能提升，专家反馈和自动化分析证实其推理轨迹具有忠实性和语义意义。研究表明，推理可以为栅格预测模型提供基础，提升模型的泛化能力和解释性。首次展示了基于语言的推理可以改善视觉生成的泛化能力，并提出了适用于跨大陆应用的高分辨率野火风险模型，使对多模态野火风险模型跨大陆泛化的系统研究成为可能。
### Conclusion
本研究证明了推理可以作为栅格预测模型的基础，增强模型的泛化能力和解释性。FireScope-Bench有可能成为推动推理驱动、可解释和可泛化空间建模发展的基础。数据和源代码将公开可供使用。
## 562. `cs.LG` - BITS for GAPS: 基于信息论采样的分层高斯过程代理模型 [PDF](https://arxiv.org/pdf/2511.16815), [HTML](https://arxiv.org/abs/2511.16815)
### Authors
Kyla D. Jones,Alexander W. Dowling
### Background
本文提出了用于模拟混合物理系统中潜藏组件的贝叶斯信息论采样（BITS for GAPS）框架。在序列混合建模中，已知的物理法则支配部分系统，而剩余的动力学则是根据数据推断得到的潜藏函数来表示。文中使用高斯过程先验对潜藏函数进行建模，并针对其超参数使用分层先验以包含物理上重要意义的结构。为了指导数据采集，推导了基于熵的信息获取函数，量化了候选输入位置的预期信息增益，以此来识别对于训练代理模型最有信息含量的样本。
### Innovation
本文的主要创新在于提出了BITS for GAPS框架，并通过熵指导的采样策略来提升样本效率。具体而言，通过获得预测后验的微分熵的闭形式表达，并建立可计算的近似下界来提高计算效率。这些推导近似将预测后验表示为有限的、均匀加权的高斯过程混合。
### Conclusion
本文的框架证明了其对像蒸气-液体平衡系统中活动系数建模的应用价值，并将代理模型嵌入到扩展的拉乌尔定律中，以用于蒸馏设计。数值结果表明，基于熵指导的采样提高了样本效率，通过瞄准具有高度不确定性和潜在信息增益的区域。这种方法加速了代理模型的收敛速度，提高了非理想情况下预测的准确性，并保持了物理一致性。总的来说，BITS for GAPS为复杂物理系统的混合建模提供了一个高效、可解释且具有不确定性意识的框架。
## 563. `cs.LG` - Parrot: 支配力和一致性对输出真实性的评估——大规模语言模型的阿谀奉承稳健性基准 [PDF](https://arxiv.org/pdf/2511.17220), [HTML](https://arxiv.org/abs/2511.17220)
### Authors
Yusuf Çelebi,Mahmoud El Hussieni,Özay Ezerceli
### Background
该研究探讨了大型语言模型（LLMs）在社会压力影响下表现的稳健性问题，重点关注权威与说服力如何影响用户决策，并讨论了阿谀奉承现象。研究人员评估了22种不同模型，在13个特定领域和相关权威模板下，提出了1,302个类似MMLU的多种选择题。结果显示，不同模型表现出显著差异，复杂模型如GPT-5和Claude Sonnet 4.5的“遵从率”很低，准确度损失也最小，而较旧和较小的模型则表现出严重的认知崩溃。这项研究指出了模型在应对说服力和社会压力方面的不足，并指出需要对过度拟合压力的抵抗能力进行关注。
### Innovation
PARROT框架通过双盲评估区分中立版本和权威错误版本的问题，并利用对数似然校准跟踪来量化对正确和被迫错误答案的信心变化，同时使用八阶段的行为分类体系系统地分类失败模式。该研究揭示了不同模型的异质性，并强调了在全球知识和国际法等领域中模型表现的脆弱性。
### Conclusion
该研究认为，提高模型对抗世界压力的抵抗能力应该成为部署时主要关注的目标之一，并应在准确性、避免伤害和保护隐私之外考虑。
## 564. `cs.LG` - Edge部署中的变换感知结构化剪枝：一种带自适应微调的综合框架 [PDF](https://arxiv.org/pdf/2511.17242), [HTML](https://arxiv.org/abs/2511.17242)
### Authors
Mohammed Alnemari
### Background
本文提出了一种结合变换等变卷积神经网络（G-CNNs）和变换感知结构化剪枝的新框架，旨在为资源受限环境生成紧凑、不变的模型。通过C4循环群实现旋转等变性，利用e2cnn库，确保在几何变换下的一致性能同时减少计算开销。
### Innovation
本文引入了基于e2cnn层结构分析进行神经元级剪枝的结构化剪枝方法，以保持等变性，并通过自适应微调机制，当精度下降超过2%时自动触发，使用早停和学习率调度来实现准确性的有效恢复。框架还包含动态INT8量化和包括训练、知识蒸馏、结构化剪枝、微调和量化在内的综合管道。
### Conclusion
本文在卫星图像（EuroSAT）和标准基准数据集（CIFAR-10, Rotated MNIST）上进行了评估，表明该方法在不同领域均有效。实验结果表明压缩比达到29.3%，并在显著恢复准确性的基础上证实了等变网络结构化剪枝可以实现显著压缩，同时保持几何鲁棒性。本文的管道提供了优化等变模型的可再现框架，桥梁了群论网络设计与实际部署约束之间的差距。
## 565. `cs.LG` - 探究自监督表示在视听伪造检测中的应用 [PDF](https://arxiv.org/pdf/2511.17181), [HTML](https://arxiv.org/abs/2511.17181)
### Authors
Dragos-Alexandru Boldisor,Stefan Smeu,Dan Oneata,Elisabeta Oneata
### Background
自监督表示在视觉和语音任务中表现出色，但在视听伪造检测中的潜力尚未被充分探索。大多数研究使用这些特征时，要么单独使用，要么嵌入复杂的模型架构中，这限制了它们在多模态和不同领域中的应用效果。
### Innovation
该研究系统性地评估了自监督表示在音频、视频和多模态领域中的表现，并研究了它们在唇形运动和通用视觉内容等不同领域的检测效果。研究还考察了这三个关键维度：伪造检测效果、编码信息的可解释性以及模态间的互补性。
### Conclusion
大多数自监督特征捕捉到与伪造相关的信息，并且这些信息在模态间具有互补性。然而，这些模型在不同数据集间的表现并不稳定，这可能是由于数据集的特性，而不是自监督特征本身锁定表面模式引起的。研究结果揭示了自监督表示在伪造检测中的潜力及其基本挑战：虽然它们能够学习有意义的模式，但在不同领域的鲁棒性能仍然难以实现。
## 566. `cs.LG` - 持续量子学习中内在保持可塑性的原理 [PDF](https://arxiv.org/pdf/2511.17228), [HTML](https://arxiv.org/abs/2511.17228)
### Authors
Yu-Qin Chen,Shi-Xin Zhang
### Background
人工智能在动态、实际环境中的应用需要持续学习的能力，而传统深度学习由于先天缺陷——即塑性的丧失（网络逐渐失去从新数据中学习的能力），无法满足这一需求。
### Innovation
本文展示了量子学习模型自然克服这一限制，能够在长时间尺度上保持塑性。这种优势在多种学习范式和不同数据类型的任务中得到了系统性验证，包括监督学习和强化学习，以及从经典高维图像到量子原生数据集等多种数据模态。与经典模型随着权重和梯度增长而性能下降相反，量子神经网络在数据或任务变化时仍能保持一致的学习能力。研究指出，量子模型内在的物理约束是这一优势的根源，不受限的权重增长在经典网络中会导致风景崎岖或饱和，而酉性约束则将优化限制在紧凑的流形中。
### Conclusion
研究结果表明，量子计算在机器学习中的作用不仅限于潜在的加速，还能为构建适应性人工智能和终身学习系统提供一个稳健的发展途径。
## 567. `cs.LG` - MIR:通过相互内在奖励在 episodic 多智能体强化学习中高效探索 [PDF](https://arxiv.org/pdf/2511.17165), [HTML](https://arxiv.org/abs/2511.17165)
### Authors
Kesheng Chen,Wenjian Luo,Bang Zhang,Zeping Yin,Zipeng Ye
### Background
 episodic 奖励在强化学习中构成了重大挑战。现有的内在奖励方法在单智能体强化学习中显示出有效性，但在多智能体强化学习(MARL)场景中的应用存在问题，主要是由于联合动作轨迹的指数稀疏性和现有方法未能充分考虑到影响团队状态的联合动作。
### Innovation
提出了互内在奖励(MIR)策略，这是一种简单而有效的增强策略，能够在像 episodic 奖励这样的极其稀疏奖励的情况下，激励个体智能体探索影响团队成员的动作。MIR结合原有策略，有效促进了团队探索并提高了算法性能。
### Conclusion
为了全面验证，扩展了代表性单智能体环境 MiniGrid，创建了 MiniGrid-MA，一系列带有稀疏奖励的 MARL 环境。评估结果表明，在 MiniGrid-MA 设置中，所提出的方法优于最先进的方法，显示出更好的性能。
## 568. `cs.LG` - 剖析量子强化学习的关键组件系统的评估 [PDF](https://arxiv.org/pdf/2511.17112), [HTML](https://arxiv.org/abs/2511.17112)
### Authors
Javier Lazaro,Juan-Ignacio Vazquez,Pablo Garcia-Bringas
### Background
参数化量子电路（PQC）基于的量子强化学习（QRL）已经在量子计算和强化学习的交叉领域成为一个有前景的范式。由于训练不稳定性、退化高原以及难以分离个体管道组件的贡献，其实际应用性仍然存疑。
### Innovation
本文通过系统实验评估了三个关键方面来细致分析PQC基于的QRL架构：(i) 数据嵌入策略，尤其是使用Data Reuploading (DR) 作为先进的方法；(ii) Ansatz设计，特别是纠缠的作用；(iii) 量子测量后的后处理块，特别是未被充分探索的Output Reuse (OR) 技术。作者利用统一的PPO-CartPole框架，在相同条件下对混合和经典代理进行受控比对。
### Conclusion
研究结果表明，虽然纯粹经典，但是OR在混合管道中表现出不同的行为；DR提高了训练能力和稳定性；更强的纠缠可以损害优化，抵消了经典增益。这些发现提供了量子和经典贡献之间交互作用的受控实证证据，并建立了QRL中系统基准和组件分析的可重复框架。
## 569. `cs.LG` - 使用不确定性量化评估基于人工智能的极端天气预测模型的预测能力 [PDF](https://arxiv.org/pdf/2511.17176), [HTML](https://arxiv.org/abs/2511.17176)
### Authors
Rodrigo Almeida,Noelia Otero,Miguel-Ángel Fernández-Torres,Jackie Ma
### Background
基于人工智能的天气预测系统在准确预测极端天气事件方面仍面临重大挑战。虽然确定性模型如FuXi、GraphCast和SFNO在预测技能上与数值天气预测相当，但它们在表示不确定性并捕捉极端事件方面的能力仍然有限。本研究旨在探讨最先进的确定性人工智能模型对初始条件扰动的响应，并评估其在预测极端事件中的集合预报能力。
### Innovation
通过使用三种扰动策略（高斯噪声、半球中心传播向量、巨型集合）生成两个主要事件（巴基斯坦洪水和中国热浪）的50成员集合，本研究展示了流依赖性扰动可以产生最现实的集合发散和最高的概率技能，从而缩小并不存在于数值天气预测集合中的性能差距。各变量下，人工智能天气模型在温度极值方面的捕捉能力比降水更为有效。
### Conclusion
输入扰动可以将确定性模型扩展到概率预报，为结合流依赖性扰动与生成或潜在空间不确定性建模的可靠的人工智能驱动早期预警系统铺平道路。
## 570. `cs.LG` - 高度粒化探测器模拟器的第一个完整物理基准 [PDF](https://arxiv.org/pdf/2511.17293), [HTML](https://arxiv.org/abs/2511.17293)
### Authors
Thorsten Buss,Henry Day-Hall,Frank Gaede,Gregor Kasieczka,Katja Krüger,Anatolii Korol,Thomas Madlener,Peter McKeown
### Background
当前和未来粒子加速器实验的物理程序需要开发模拟器来模拟探测器中的光子簇射。虽然生成模型的发展取得了不少进步，但这些模型通常是在简化场景和单一粒子的情况下进行评估的，特别是在要求很高的粒度探测器模拟这一具有挑战性的任务中。本文首次研究了在现实模拟应用中使用高度粒化的生成模拟器的可能性。
### Innovation
介绍了DDML，这是一种通用库，可以将生成的模拟器与使用DD4hep工具实现的真实探测器相结合。研究了两种不同的生成模型：一种基于规则网格表示，另一种基于较少常用的点云方法。为了使方法论细节与模型性能分离，提供了与理想化模拟器的比较，这些模拟器直接从全模拟的真实情况中抽样不同分辨率的表示。系统性地评估了模型在电磁簇射模拟后的重建基准上的性能，包括基于双光子分离的第一个多粒子基准和基于tau粒子衰变的第一个完整物理基准。
### Conclusion
研究结果表明，基于点云操作的模型相较于基于规则网格表示的模型在高度粒化的簇射模拟中能够更有效地保持速度和准确性之间的平衡。
## 571. `cs.LG` - Neighbor GRPO：对比ODE策略优化对流动模型的对齐 [PDF](https://arxiv.org/pdf/2511.16955), [HTML](https://arxiv.org/abs/2511.16955)
### Authors
Dailan He,Guanlin Feng,Xingtong Ge,Yazhe Niu,Yi Zhang,Bingqi Ma,Guanglu Song,Yu Liu,Hongsheng Li
### Background
Group Relative Policy Optimization (GRPO) 已经在使图像和视频生成模型与人类偏好保持一致方面表现出了潜力，但是将其应用于现代流动匹配模型具有挑战性，因为GRPO具有确定性的采样范式。当前的方法通过将 Ordinary Differential Equations (ODEs) 转换为 Stochastic Differential Equations (SDEs) 来解决这一问题，这引入了不确定性。然而，基于SDE 的GRPO 存在归因效率低下和与高阶求解器不兼容的问题，尤其是在需要更少步骤采样的情况下。
### Innovation
本文首先从距离优化的角度重新解释现有的基于SDE的GRPO 方法，揭示它们背后的机制是一种对比学习。基于这一洞察，我们提出了邻近 GRPO，这是一种新型对齐算法，完全避免了对SDE的需求。邻近GRPO 通过扰动ODE 的初始噪声条件生成一组多样化的候选轨迹，并使用基于 softmax 距离的跳跃策略进行模型优化。我们建立了基于距离的目标和策略梯度优化之间的理论联系，将该方法严格整合到 GRPO 框架中。我们的方法完全保持了确定性ODE采样的优势，包括效率和与高阶求解器的兼容性。为进一步提高计算效率，我们引入了对称锚点采样，并通过组内准范重新加权来解决奖励平坦化问题。
### Conclusion
广泛的实验表明，邻近GRPO 在训练成本、收敛速度和生成质量方面显著优于基于SDE的对应物。
## 572. `cs.LG` - 基于全序关系的离散模糊数高效计算框架 [PDF](https://arxiv.org/pdf/2511.17080), [HTML](https://arxiv.org/abs/2511.17080)
### Authors
Arnau Mir,Alejandro Mus,Juan Vicente Riera
### Background
离散模糊数，特别是在有限链$L_n = ?{0, ?ldots, n?}$上的定义，已经广泛应用于模糊系统中代表语言信息的框架中。研究这样的模糊子集的总体（可接受）排序，特别是属于集合$text{D}_1^{L_n?rightarrow Y_m}$的离散模糊数$A$的排序，其中$A$的支持是有限链$L_n$的一个闭子区间，并且$A(x)$在$L_n$中的隶属度值属于集合$Y_m = ?{ 0 = y_1 < y_2 < ?cdots < y_{m-1} < y_m = 1 ?}$。这意味着一种称为pos函数的双射函数确定了每个$A text{∈} text{D}_1^{L_n?rightarrow Y_m}$的位置。
### Innovation
本文通过引入利用总体（可接受）秩序的组合结构计算pos函数及其逆函数的算法，重新审视了这一问题。所提出的方法实现了复杂度为$text{O}(n^2 m text{ log} n)$，这相对于链的大小（$n$）具有平方性，并且相对于隶属度级别的数量（$m$）具有线性性。关键在于$m$是主要因素，确保了对隶属度值粒度变化的可扩展性。
### Conclusion
这些结果表明，这种表述法显著降低了计算成本，并使集合中离散模糊数的代数运算（如聚合和推断）的高效实现成为可能。
## 573. `cs.LG` - 快速非自适应学习Erdős--Rényi随机图的解码加速 [PDF](https://arxiv.org/pdf/2511.17240), [HTML](https://arxiv.org/abs/2511.17240)
### Authors
Hoang Ta,Jonathan Scarlett
### Background
研究通过节点子集的群查询来学习未知图的问题，其中每条查询报告在查询节点之间是否至少存在一条边。对于一般图，即使允许有小的错误概率，在非自适应设置下学习具有n个节点和k条边的任意图需要至少Ω(min{k^2 log n, n^2})次测试。对于Erdős--Rényi随机图G~ER(n,q)，以前的工作提出了一种测试解码方案，实现了测试次数的最优阶O(average k log n)，但解码时间需要Ω(n^2)，而他们的亚线性时间算法在测试次数上会额外增加因子(log average k log n)。主要研究背景是在非自适应设置下有效地学习Erdős--Rényi随机图。
### Innovation
将最近为非自适应群测试开发的二元分裂方法扩展到Erdős--Rényi图学习设置中。证明了可以在高概率下使用O(average k log n)次测试重构边集，并实现O(average k^(1+δ) log n)的解码时间，其中δ>0是一个固定的参数。
### Conclusion
本文提出了一个高效的测试解码方案，能够以高概率在O(average k log n)次测试下学习Erdős--Rényi随机图，并实现亚线性解码时间。
## 574. `cs.LG` - 非自然的：离策略训练数据对探针性能的影响 [PDF](https://arxiv.org/pdf/2511.17408), [HTML](https://arxiv.org/abs/2511.17408)
### Authors
Nathalie Kirch,Samuel Dower,Adrians Skapars,Ekdeep Singh Lubana,Dmitrii Krasheninnikov
### Background
探针技术被认为是一种有前途的方法，用于监控大型语言模型（LLMs）。这种技术能够在推理阶段检测模型存在的诸如欺骗和奉承等不良行为。然而，很多实际行为的自然样本很少，研究人员不得不依赖合成或策略外（off-policy）LLM的响应进行探针训练。
### Innovation
本研究系统地评估了使用合成和策略外数据如何影响探针在八个不同LLM行为上的泛化能力。测试线性和注意力探针在多种LLM上的表现，作者发现响应生成策略显著影响探针性能，但不同行为的影响程度不一。研究还发现，从策略外数据成功泛化到激励模型产生目标行为的测试集，能够预测从策略内数据到实际监控场景的成功泛化。
### Conclusion
研究结果表明，在缺乏策略内数据的情况下，使用同领域策略外数据比使用不同领域策略内数据更能生成可靠的探针，突显了需要发展能够更好地处理LLM监控领域转移的方法的重要性。
## 575. `cs.LG` - 选择性旋转位置嵌入 [PDF](https://arxiv.org/pdf/2511.17388), [HTML](https://arxiv.org/abs/2511.17388)
### Authors
Sajad Movahedi,Timur Carstensen,Arshia Afzal,Frank Hutter,Antonio Orvieto,Volkan Cevher
### Background
语言模型需要位置信息。在Softmax变换器中，Rotary Position Embeddings (RoPE)通过固定角度的旋转编码位置，而在线性变换器中，顺序则是通过输入依赖的选择性门控（即有选择地减弱过去的关键值关联）来处理。选择性一般已知能提升语言相关任务的性能。
### Innovation
本文引入了选择性旋转位置嵌入（Selective RoPE），这是一种输入依赖的旋转嵌入机制，可以适用于线性和Softmax变换器，并支持对不同的查询-键对执行任意角度的旋转。研究发现Softmax 注意力已经在查询-键对上隐式执行了这些旋转，揭示了一种隐含的位置结构。进一步研究发现，在状态空间模型和门控线性变换器中，实部处理遗忘，而虚部通过旋转编码位置。
### Conclusion
我们将选择性旋转位置嵌入应用于门控变换器，结果证明其输入依赖的旋转可以提高语言模型的表现，尤其是在复杂序列任务如复制、状态跟踪和检索方面。
## 576. `cs.LG` - SPEAR-1：通过3D理解扩大机器人展示之外的规模 [PDF](https://arxiv.org/pdf/2511.17411), [HTML](https://arxiv.org/abs/2511.17411)
### Authors
Nikolay Nikolov,Giuliano Albanese,Sombit Dey,Aleksandar Yanev,Luc Van Gool,Jan-Nico Zaech,Danda Pani Paudel
### Background
机器人基础模型（RFMs）作为整体的端到端系统在机器人控制方面具有巨大的潜力，但在跨新环境、任务和实体进行泛化的能力上尚有局限。大多数RFMs通过微调互联网预训练的视觉-语言模型（VLMs）构建而成，但这些VLMs主要是在2D图像语言任务上进行训练，缺乏3D空间推理能力，这是3D世界中实体控制所必需的。直接通过大规模的机器人数据来弥合这一差距成本高昂且难以扩展。
### Innovation
提出了一种策略，即对易于获取的非机器人图像数据进行3D注解，并增强预训练的VLM以获得3D理解能力。基于这一策略，训练了一个3D感知的VLM（SPEAR-VLM），能够从单张2D图像中推断出物体在3D空间中的坐标。在此基础上，引入了主要贡献SPEAR-1，这是一种集成了基于语言指导的实体控制和基础3D感知的机器人基础模型，通过约4500万帧来自24个Open X-Embodiment数据集的训练，SPEAR-1在性能上超过了或匹配了如$textbf{textit{textpi_0}}$-FAST和$textbf{textit{textpi_{0.5}}}$的最先进的模型，使用了20倍更少的机器人演示数据。
### Conclusion
精心设计的训练策略解锁了新的VLM能力，从而增强了实体控制的可靠性，超越了仅使用机器人数据所能达到的效果。同时，该模型权重和3D注释数据集已公开提供。
## 577. `cs.LG` - 非线性随机系统的自适应稳定化框架 [PDF](https://arxiv.org/pdf/2511.17436), [HTML](https://arxiv.org/abs/2511.17436)
### Authors
Seth Siriya,Jingge Zhu,Dragan Nešić,Ye Pu
### Background
本文考虑了离散时间非线性随机系统的自适应控制问题，特别是具有线性参数化的不确定性系统。假设可以通过参数化控制器家族在状态空间的信息区域稳定系统，只要参数适当选择就能在有限集内稳定。在这些基础上，文章进一步探讨了如何基于自等价学习提出自适应控制策略，并推导出在某些概率下的系统稳定性边界。
### Innovation
文章提出的自适应控制策略是一种基于自等价学习的方法。通过这种方法，可以获得一定的概率下系统的稳定性边界。进一步研究还表明，只要整个状态空间都是信息丰富的，并且控制器家族能在适当参数下全局稳定，就可以导出高概率的稳定性保证。
### Conclusion
本文为非线性随机系统的自适应稳定化提供了框架，并通过具体的理论分析确立了系统的高概率稳定性保证，为实际应用中的控制策略设计提供了理论支持。
## 578. `cs.LG` - 针对神经网络亚网格应力模型后验性能退化的解决方法 [PDF](https://arxiv.org/pdf/2511.17475), [HTML](https://arxiv.org/abs/2511.17475)
### Authors
Andy Wu,Sanjiva K. Lele
### Background
神经网络亚网格应力模型在先验性能上往往远优于后验性能，在大涡模拟（LES）中容易出现性能下降问题，导致这类模型在先验评估时看起来非常有希望，但在后验测试中却完全失败。
### Innovation
通过结合两种不同的方法——训练数据增强和减少输入复杂性，来缩小神经网络亚网格应力模型的先验与后验性能差距。特别指出，使用两种不同滤波器增强训练数据的神经网络在先验评估和后验测试中的性能没有显著下降，且在后验测试中表现出更高的鲁棒性。同时，通过删除输入神经网络的高阶项，也能减少先验与后验性能的差距。综合这两种方法，结合数据增强和简化输入的神经网络，在后验测试中的表现更加接近先验评估。
### Conclusion
利用训练数据增强和简化输入的方法，能够在后验测试中显著提高神经网络亚网格应力模型的性能表现，使其更接近于先验评估的结果，从而改善模型在复杂LES环境中的表现稳定性。
## 579. `cs.LG` - MuM: 多视图掩蔽图像建模用于3D视觉 [PDF](https://arxiv.org/pdf/2511.17309), [HTML](https://arxiv.org/abs/2511.17309)
### Authors
David Nordström,Johan Edstedt,Fredrik Kahl,Georg Bökman
### Background
自监督学习在图像上旨在从未标记数据中提取有意义的视觉表示。当扩展到大规模数据集时，这种范式已经达到了最先进的性能，并且由此训练的模型如DINOv3得到了广泛应用。然而，大多数先前的努力侧重于语义理解而不是几何推理。Cross-View Completion (CroCo) 是一个重要的例外，它是为3D理解优化的掩蔽自动编码（MAE）的一种形式。
### Innovation
我们继续沿着CroCo提出的路径，侧重于用于3D视觉的功能学习。我们扩展了MAE，使之涵盖同场景的任意多个视图。通过在所有视图上均匀掩蔽并使用轻量级解码器和帧间注意机制，我们的方法比CroCo更简单且更具可扩展性。我们对MuM模型进行了详尽的评估，涵盖下游任务如前馈重建、密集图像匹配和相对位姿估计，发现它优于最先进的视觉编码器DINOv3和CroCo v2。
### Conclusion
MuM模型在各种下游任务中的性能超过了DINOv3和CroCo v2，证实了其在3D视觉任务上的有效性。
## 580. `cs.LG` - 使用可扩展频谱神经网络方法估计全局输入相关性并强制稀疏表示 [PDF](https://arxiv.org/pdf/2406.01183), [HTML](https://arxiv.org/abs/2406.01183)
### Authors
Lorenzo Chicchi,Lorenzo Buffoni,Diego Febbe,Lorenzo Giambagli,Raffaele Marino,Duccio Fanelli
### Background
在机器学习实践中，识别相关输入特征通常是很有用的。通过识别并排序按重要性排列的关键输入元素，可以帮助阐释决策过程。本文提出了一种基于优化过程频谱重构的新方法，用于估计深度神经网络中输入组件的相对重要性。
### Innovation
该方法通过频谱重构优化过程，使用输入节点的特征值来估计输入组件的重要性，并自动完成排序，无需额外处理。此外，通过正则化特征值，可以强制使用最少的输入组件，增强模型的解释性并提供稀疏输入表示。
### Conclusion
该技术与文献中最常见方法进行了比较，并成功地在合成和真实数据上挑战了这些方法。
## 581. `cs.LG` - ‘标准化应力’不标准化：如何正确解读应力 [PDF](https://arxiv.org/pdf/2408.07724), [HTML](https://arxiv.org/abs/2408.07724)
### Authors
Kiran Smelser,Jacob Miller,Stephen Kobourov
### Background
压力是用于高维数据降维投影中最常见的质量指标和优化准则之一。复杂的高维数据大量存在于机器学习、生物学和社会科学等多个科学领域。通常，研究人员通过二维散点图来可视化这些数据集，这样的图可以捕捉到数据的一些特性。然而，视觉上确定这些图的准确性很困难，因此研究人员通常会使用质量指标来衡量投影的准确性和对全数据的忠实度。最常用的指标之一，归一化应力，对投影的均匀缩放敏感，尽管这种操作本质上不会改变投影的任何内容。该项研究通过分析和实验探讨了缩放对压力以及其他基于距离的质量指标的影响，旨在准确评估降维技术的效果。
### Innovation
研究人员提出了一种简单的方法，使归一化应力具有尺度不变性，并证明了这种变化准确反映了预期的行为。这项技术对于正确理解和评估降维技术具有重要意义。
### Conclusion
研究结果表明，使用这种方法后，归一化应力可以更准确地捕捉到降维技术的效果，解决了其尺度敏感的问题。
## 582. `cs.LG` - 量子掩码自编码器在视觉学习中的应用 [PDF](https://arxiv.org/pdf/2511.17372), [HTML](https://arxiv.org/abs/2511.17372)
### Authors
Emma Andrews,Prabhat Mishra
### Background
经典自编码器被广泛用于学习输入数据的特征，而经典掩码自编码器则在掩码数据的背景下学习原始输入样本的特征。现有技术虽然存在量子自编码器，但尚未设计并实现能够利用量子计算和量子自编码器优势的量子掩码自编码器。
### Innovation
本文提出了一种新的量子掩码自编码器（QMAE），能够在量子状态下有效学习数据样本中的缺失特征，而不是在经典嵌入中学习。实验结果显示，QMAE在MNIST图像中能够学习掩码特征并对输入图像进行更高质量的重构，并且在含掩码的情况下在分类精度方面显著优于最先进的量子自编码器（平均提高12.86%）。
### Conclusion
量子掩码自编码器能够在量子状态下有效学习数据样本的缺失特征，提高图像的视觉保真度，并在有掩码的情况下显著提升分类准确性。
## 583. `cs.LG` - FORWARD：在崎岖地形上进行木材前置作业的数据集 [PDF](https://arxiv.org/pdf/2511.17318), [HTML](https://arxiv.org/abs/2511.17318)
### Authors
Mikael Lundbäck,Erik Wallin,Carola Häggström,Mattias Nyström,Andreas Grönlund,Mats Richardson,Petrus Jönsson,William Arnvik,Lucas Hedström,Arvid Fälldin,Martin Servin
### Background
该研究提出了一组高质量、多模态的数据集，该数据集记录了一辆前置器在其所在瑞典中部两个采伐场地中的作业情况。前置器配备有RTK-GNSS、360度摄像头、操作员振动传感器等多种传感器，同时采集了点云激光扫描数据、生产日志文件、视频材料以及地形数据。这些数据用于开发适用于森林机械的交通性、感知以及自主控制领域的模型和算法。
### Innovation
该数据集在多传感器集成、高分辨率点云数据以及涉及采伐过程中的具体操作细节等方面展现出了创新性。特别是，数据涵盖了前置器在复杂环境中的运行细节，比如货物装载、移除、避障等场景的反复测试，这些数据为开发自动化控制、实时感知以及物理测试平台的模型提供了宝贵的资源。
### Conclusion
该FORWARD数据集旨在通过采用人工智能、仿真和物理测试平台等方法，助力开发森林机械的交通性、感知以及自主控制模型。数据为研究机器在复杂地形的适宜性运行、提高作业效率、节省燃料消耗、提升安全性等方面提供了重要支持，并且可以用于模拟器的自动生成和校准等工作场景的描述，进一步促进林业装备的自动化水平提升。
## 584. `cs.LG` - MonoKAN: 保证单调性的柯莫戈罗夫-阿诺尔德网络 [PDF](https://arxiv.org/pdf/2409.11078), [HTML](https://arxiv.org/abs/2409.11078)
### Authors
Alejandro Polo-Molina,David Alfaya,Jose Portela
### Background
人工神经网络（ANNs）在模式识别和复杂问题解决方面取得了显著进步，但在透明性和解释性方面仍面临挑战。已有解释性AI（XAI）方法在一定程度上降低了ANNs的复杂性，但仍不能完全满足某些应用中模型预测需要符合专家设定要求的需要，例如部分单调性约束。现有的单调性方法虽然可以在传统多层感知机（MLPs）中找到，但很难同时满足解释性和部分单调性的认证需求。为此，一种名为KAN的基于可学习激活函数（如样条函数参数化）的网络架构应运而生，被普遍认为是更加解释性的MLP替代方案。在此基础上，本文提出了名为MonoKAN的新ANN架构，它在保持解释性的基础上实现了部分单调性的认证。
### Innovation
MonoKAN架构基于KAN架构，通过使用三次Hermite样条来确保单调性，通过保证样条组合中权重为正来保持输入与输出之间的单调关系。该方法不仅增强了模型的解释性，还在多项基准测试中提升了预测性能，超越了现有最先进的单调MLP方法。
### Conclusion
MonoKAN架构不仅增强了模型的解释性，还在多项基准测试中提高了预测性能，超越了传统单调MLP方法，表明MonoKAN在复杂应用中具有更好的实用性和可靠性。
## 585. `cs.LG` - 危险中的帖子：在文本中检测有关危害的信息 [PDF](https://arxiv.org/pdf/2405.17838), [HTML](https://arxiv.org/abs/2405.17838)
### Authors
Keith Burghardt,Daniel M.T. Fessler,Chyna Tang,Anne Pisor,Kristina Lerman
### Background
文本中的社会语言指标，如情感或情绪，通常被提取用于理解人机交互特点，包括社交媒体中的交互。然而，危害或危险相关信息的出现与否往往被忽视。本文旨在开发一种新模型来检测这些信息，该模型基于新的带注释的X帖子集合进行训练。研究表明，该模型不仅表现良好，而且提取的危害信息与常见指标不相关。
### Innovation
本文开发了一种新的模型来检测文本中的危险信息，并在两个涉及重要地缘政治事件的数据集中进行了应用，展示了这种工具的实用性。模型的代码已作为Python包共享，以便研究人员和新闻记者分析危害内容。
### Conclusion
研究发现，特别是在冲突中的不占优势的一方，经常提及危机信息，可能是为了激起援助。同时，不占优势一方的提及频率与有机账户存在明显差异。这些结果为在信息战环境中探索危害提供了初步步骤。模型及相关数据已通过特定的仓库进行共享。
## 586. `cs.LG` - CREST：通过特定指标的故障报告检索提高Ericsson的可解释性和有效性 [PDF](https://arxiv.org/pdf/2511.17417), [HTML](https://arxiv.org/abs/2511.17417)
### Authors
Soroush Javdan,Pragash Krishnamoorthy,Olga Baysal
### Background
电信行业的迅速发展要求高效的故障处理流程以保持网络可靠性、软件可维护性和服务质量。故障报告（Trouble Reports, TRs）在记录Ericsson生产系统中的问题方面起着关键作用，有助于及时解决软件故障。但是，TR数据的复杂性和庞大的数据量，加上反映每个故障不同方面的多样标准，给检索系统带来了挑战。受Ericsson先前采用的两阶段工作流（初始检索Initial Retrieval, IR和重新排序Re-Ranking, RR）的启发，本研究探讨了不同TR观察标准及其对检索模型性能的影响。
### Innovation
本文提出了CREST（特定指标特定检索通过特殊TR模型的集成），这是一种目标驱动的检索方法，利用针对不同TR领域的专业化模型，提高了检索的有效性和可解释性，从而加快故障解决并支持软件维护。CREST采用针对特定TR标准进行专业化训练的模型，并将其输出集成为不同和互补的信号，从而增强了检索准确性，更好地校准预测分数，并通过为每个标准提供相关性得分提髙了可解释性，帮助用户理解为什么选择了特定的TR。
### Conclusion
使用Ericsson内部部分TR数据集的研究结果表明，特定标准的模型在关键评估指标上显著优于单一模型的方案。这强调了本研究中使用的所有针对指标的重要性，以优化检索系统性能。
## 587. `cs.LG` - 一种新的因果规则学习方法用于可解释估计异质治疗效果 [PDF](https://arxiv.org/pdf/2310.06746), [HTML](https://arxiv.org/abs/2310.06746)
### Authors
Ying Wu,Hanzhong Liu,Kai Ren,Shujie Ma,Xiangyu Chang
### Background
在复杂疾病的统计学习应用中，解释性是至关重要的，尤其是在估计异质治疗效应（HTE）方面。以往的研究未能充分关注一个关键问题：个体是否可以同时属于具有不同平均治疗效应的多个群体。这项研究利用基于规则的工作流，即因果规则学习（CRL），来估计和提高对HTE的理解，特别是在处理复杂实际状况时。
### Innovation
创新点在于提出了一种新的CRL方法，该方法通过三个步骤进行：规则发现生成具有相应亚组平均治疗效应的规则集；规则选择识别出规则集中的子集，以构建个体层面的治疗效应为亚组层面效应的线性组合；规则分析为每个选定规则提供了详细分析的框架，旨在识别最有前途的规则进行验证。这种方法在仿真和实际数据研究中展示了相较于其他方法，尤其是在复杂真实情况和足够样本量下，如何提供更具有解释性的HTE估计。
### Conclusion
广泛的研究表明，CRL在提供具有良好解释性的HTE估计方面表现优异，尤其是在处理复杂属实和有足够的样本量时。
## 588. `cs.LG` - 非参数概率鲁棒性：具有优化扰动分布的保守度量 [PDF](https://arxiv.org/pdf/2511.17380), [HTML](https://arxiv.org/abs/2511.17380)
### Authors
Zheng Wang,Yi Zhang,Siddartha Khastgir,Carsten Maple,Xingyu Zhao
### Background
尽管深度学习模型在许多任务中表现出色，但它们仍然容易受到小输入 perturbations 的影响，这可能导致错误的输出。为此，最近提出了一种互补的替代方法——概率鲁棒性 (PR)。然而，现有的 PR 表述假设扰动分布是固定且已知的，这在实践中并不现实。
### Innovation
提出了非参数概率鲁棒性 (NPPR)，这是一种更实用的 PR 度量，不依赖于任何预定义的扰动分布。NPPR 在统计建模的非参数范式基础上，直接从数据中学习优化的扰动分布，从而在不确定性分布下实现保守的 PR 评估。基于高斯混合模型 (GMM) 与多层感知器 (MLP) 和双三次上采样的进一步开发，NPPR 能够涵盖输入依赖性和输入独立性扰动的各种情况。理论分析建立了 NPPR 与 AR 和 PR 之间的关系。
### Conclusion
在 CIFAR-10、CIFAR-100 和 Tiny ImageNet 数据集上的广泛实验结果显示，NPPR 作为一种更实用的鲁棒性度量，相对于常用的扰动分布假设，能提供高达 40% 更保守（更低）的 PR 估计。
## 589. `cs.LG` - 利用扩散语言模型的文本指导多属性分子优化 [PDF](https://arxiv.org/pdf/2410.13597), [HTML](https://arxiv.org/abs/2410.13597)
### Authors
Yida Xiong,Kun Li,Jiameng Chen,Hongzhi Zhang,Di Lin,Yan Che,Wenbin Hu
### Background
分子优化（MO）是药物发现的关键阶段，在此过程中，基于任务生成的分子被优化以满足实际工业需求。现有主流MO方法主要利用外部属性预测器来指导逐迭代的属性优化。然而，由于化学空间的庞大，属性预测器无法学习所有分子样本，这导致在属性预测过程中不可避免地引入错误和噪声，从而增加误差累积、泛化能力下降和生成亚优分子候选物的风险。
### Innovation
本文提出了一种利用基于变压器的扩散语言模型（TransDLM）进行文本指导的多属性分子优化方法。TransDLM通过使用标准化化学命名法作为分子的语义表示，并在文本描述中隐式嵌入属性要求，从而在扩散过程中减少错误传播。通过融合物理和化学详细文本语义与专门的分子表示，TransDLM高效地整合了多种信息源来引导精确的优化，提高了模型在保留结构和增强属性之间的平衡能力。实验结果证明，该方法在基准数据集上具有保持分子结构相似性和增强化学属性方面优于现有最先进的方法。
### Conclusion
通过利用TransDLM，方法在实际问题解决中表现出色。实验结果显示，与最先进的方法相比，该方法在保持分子结构相似性和提升化学属性方面具有明显优势。
## 590. `cs.LG` - 水管理中的多目标强化学习 [PDF](https://arxiv.org/pdf/2505.01094), [HTML](https://arxiv.org/abs/2505.01094)
### Authors
Zuzanna Osika,Roxana Rădulescu,Jazmin Zatarain Salazar,Frans Oliehoek,Pradeep K. Murukannaiah
### Background
许多实际问题（如资源管理、自动驾驶、药物发现）需要优化多个互相矛盾的目标。多目标强化学习（MORL）将经典强化学习扩展至同时处理多个目标，产出一组能够体现各种权衡的策略。然而，MORL领域缺少复杂且现实的环境和基准。
### Innovation
本研究介绍了水资源管理（尼罗河盆地）案例并将其建模为MORL环境。这为MORL算法提供了一个新的应用背景，并对现有MORL算法进行了基准测试，结果显示专门的水资源管理方法优于最先进的MORL方法，突显了MORL算法在实际应用中的扩展性挑战。
### Conclusion
现有MORL方法在复杂、现实环境中的表现不佳，特别在水管理这类实际场景中，需要专门设计的方法来应对多个目标之间的权衡。
## 591. `cs.LG` - 通过掩蔽和重排序自我监督来增强具有可验证奖励的强化学习 [PDF](https://arxiv.org/pdf/2511.17473), [HTML](https://arxiv.org/abs/2511.17473)
### Authors
Zhen Wang,Zhifeng Gao,Guolin Ke
### Background
已有研究表明，测试时缩放可以显著提升大规模语言模型（LLMs）的数学推理能力。然而，对于数学语料库中的大部分内容，尤其是在定理证明方面，基于强化学习的验证奖励（RLVR）的可扩展性有限：中间推理至关重要，而最终答案则难以直接且可靠地验证。同时，基于令牌的指令调整Fine-tuning（SFT）通常会导致死记硬背，而无法引发更长的思维链。我们受到BERT的自监督任务的启发，提出了MR-RLVR（Masked-and-Reordered RLVR），通过“掩蔽-填写”和“步骤重排序”构建过程级别的自监督奖励，以从中间推理中提取可学信号。我们的训练流程包括两个阶段：首先在采样的数学计算和证明数据上进行自监督训练；然后在仅结果可验证的数学计算数据集上进行RLVR微调。
### Innovation
提出了一种新的基于BERT自监督任务的MR-RLVR方法，通过“掩蔽-填写”和“步骤重排序”构建过程级别的自监督奖励，以从中间推理中提取可学信号。训练流程分为两个阶段：自监督训练和RLVR微调，实现了对Qwen2.5-3B和DeepSeek-R1-Distill-Qwen-1.5B模型的实施，并在AIME24、AIME25、AMC23和MATH500上进行了评估，结果显示在固定采样和解码预算下，MR-RLVR相较于原始RLVR在Pass@1、Pass@5和Pass@8上分别实现了平均10.86%、5.27%和4.00%的提升。
### Conclusion
通过引入具有过程意识的自监督信号，可以在只有结果可验证设置中有效增强RLVR的可扩展性和性能。
## 592. `cs.LG` - 通过测试时投影学习提高神经组合优化在车辆路线问题中的泛化能力 [PDF](https://arxiv.org/pdf/2506.02392), [HTML](https://arxiv.org/abs/2506.02392)
### Authors
Yuanyao Chen,Rongsheng Chen,Fu Luo,Zhenkun Wang
### Background
神经组合优化（NCO）已显示出处理车辆路线问题（VRPs）的潜力，尤其是在减少大量手动工程的需求方面。现有方法在小规模实例（如100个节点）上表现出色，但在大规模场景中的性能显著下降，这是因为训练数据和测试数据之间的分布差异导致小规模数据上学习的策略在大规模问题上无效。
### Innovation
提出了一种新的学习框架，该框架利用大型语言模型（LLMs）在测试时进行投影学习，用于学习训练和测试分布之间的投影，从而提高NCO模型的可扩展性。相较于需要与神经网络一同训练的现有技术，该方法仅在推断阶段工作，不需要重新训练模型。实验结果表明，该方法能使一个基于100节点实例训练的骨干模型在规模高达100K节点的旅行商问题（TSP）和有载量限制的车辆路线问题（CVRP）上取得优越性能。
### Conclusion
通过测试时的投影学习，该方法显著提高了神经组合优化在大规模车辆路线问题上的性能，突破了现有方法在大规模场景中的局限性。
## 593. `cs.LG` - 机器学习中特征缩放的影响：对回归和分类任务的影响 [PDF](https://arxiv.org/pdf/2506.08274), [HTML](https://arxiv.org/abs/2506.08274)
### Authors
João Manoel Herrera Pinheiro,Suzana Vilas Boas de Oliveira,Thiago Henrique Segreto Silva,Pedro Antonio Rabelo Saraiva,Enzo Ferreira de Souza,Ricardo V. Godoy,Leonardo André Ambrosio,Marcelo Becker
### Background
当前的研究意识到了在机器学习中全面研究特征缩放的不足，特别是缺乏系统性地评估多种特征缩放技术对不同算法和数据集预测性能和计算成本的影响。已有研究虽然提到特征缩放是模型性能的重要因素，但大多数都集中在少数几种方法上，且缺乏对不同模型、任务及数据集的全面探讨。
### Innovation
论文通过系统地评估12种特征缩放技术（包括一些较少使用的转化方式）对14种机器学习算法和16个数据集（涵盖分类和回归任务）的性能影响。研究使用精度、MAE、MSE和$R^2$等指标分析预测性能，并考虑训练时间、推理时间及内存使用等因素评估计算成本。这一研究提供了详细的实验证据和透明的实验资料，有助于实际应用中根据具体模型需求选择最合适的特征缩放技术。
### Conclusion
本研究的关键发现是，集成方法（如随机森林和梯度提升模型如XGBoost、CatBoost和LightGBM）对特征缩放的依赖性较低，表现出较好的整体性能，而其他常用模型（如逻辑回归、SVM、TabNet和MLPs）则对所选择的缩放技术表现出显著的不同性能，强调了对特定模型选择最合适特征缩放技术的重要性。所有代码、实验结果及模型参数均公开，以确保实验的完全透明性和可重复性。
## 594. `cs.LG` - TRACE: 时间序列参数高效微调 [PDF](https://arxiv.org/pdf/2503.16991), [HTML](https://arxiv.org/abs/2503.16991)
### Authors
Yuze Li,Wei Zhu
### Background
预训练的时间序列基础模型受到越来越多的关注，但它们面临着一些挑战：(1) 与自然语言任务不同，时间序列数据在频率、通道数、历史/预测长度等方面各不相同。特别是对于长期预测任务，有针对性的微调可以显著提升性能。(2) 现有的参数高效调优方法如LoRA虽然适用，但需要适应时间特性。
### Innovation
（1）Gated DSIC（门控动态模拟重要性计算），这是一种无偏的LoRA模块重要性选择机制，确保微调前后参数的一致性。实验表明，Gated DSIC优于通用的微调方法。（2）长期预测任务的重构预测头，相较于线性探查头，在参数数量大幅减少的情况下，实现了可比或更优的性能。
### Conclusion
我们的方法经过广泛的实验验证，在长期/短期预测、异常检测和自然语言任务上表现出有效性，尤其是在多样化数据集上进行的消融研究进一步证明了其效果。
## 595. `cs.LG` - 基于最优传输的可微序列对齐框架 [PDF](https://arxiv.org/pdf/2502.01588), [HTML](https://arxiv.org/abs/2502.01588)
### Authors
Yacouba Kaloga,Shashi Kumar,Petr Motlicek,Ina Kodrasi
### Background
准确的序列到序列（seq2seq）对齐是医学语音分析和依赖自动语音识别（ASR）的语言学习工具等应用的关键。当前最先进的端到端（E2E）ASR系统，如连接主义时序分类（CTC）和基于转换器的模型，表现出峰状行为和对齐不准确的问题。
### Innovation
本文提出了一种新颖的基于一维最优传输的可微对齐框架，使得模型能够学习单一的对齐方法并以端到端的方式进行ASR。引入了一种称为序列最优传输距离（SOTD）的伪度量，并讨论了其理论性质。基于SOTD，提出了一种用于ASR的最优传输分类（OTTC）损失，与CTC的行为进行了比较。实验结果表明，相比CTC和更近提出的正则化CTC，该方法在对齐性能上有了显著改进，尽管在ASR性能上有所牺牲。
### Conclusion
我们认为这项工作为seq2seq对齐研究开辟了新途径，提供了进一步探索和发展的坚实基础。我们的代码可在以下网址获取：this https URL
## 596. `cs.LG` - 通过弱监督表示学习实现物理可解释的世界模型 [PDF](https://arxiv.org/pdf/2412.12870), [HTML](https://arxiv.org/abs/2412.12870)
### Authors
Zhenjiang Mao,Mrinall Eashaan Umasudhan,Ivan Ruchkin
### Background
在信息物理系统中，通过高维感官观察学习预测模型是基础，但标准世界模型通过学习的潜在表示缺乏物理可解释性，这限制了其在关键安全性任务中的可靠性、通用性和适用性。
### Innovation
作者引入了物理可解释世界模型（PIWM），该框架通过部分已知物理动力学约束将潜在表示与实际物理量对齐，并通过自然地捕捉来自现实感官管道的状态不确定性进行弱分布监督。PIWM 结合使用基于 VQ 的视觉编码器、基于变换器的物理编码器和基于已知物理方程的可学习动力学模型。该研究在三个案例（Cart Pole、Lunar Lander 和 Donkey Car）中证实PIWM 实现了准确的长期预测，恢复真实系统参数，并显著改善了物理建模。
### Conclusion
这些结果表明，在弱监督下直接从图像中学习物理可解释的世界模型的可行性和优势。
## 597. `cs.LG` - 高容量核逻辑回归希普夫网络的定量吸引子分析 [PDF](https://arxiv.org/pdf/2505.01218), [HTML](https://arxiv.org/abs/2505.01218)
### Authors
Akira Tamamori
### Background
核基学习方法，如核逻辑回归（KLR），能够显著提高希普夫网络的存储容量，但这些方法的效果和稳定性原则尚未得到充分研究。
### Innovation
通过对KLR训练网络的吸引子景观进行全面定量分析，揭示KLR和核岭回归（KRR）表现出相似的高存储容量和干净的吸引子景观，探索了核宽度（γ）的非平凡、规模依赖的缩放定律，并展示了容量与网络规模线性关系的证据。
### Conclusion
该研究提供了设计高容量、稳健关联记忆的一系列明确的经验原则，并阐明了核方法克服希普夫类型模型经典限制的机制。此外，研究还表明，性能对正则化参数的选择表现出高度的鲁棒性。
## 598. `cs.LG` - 神经丛上度量张量的确定性界和随机估计 [PDF](https://arxiv.org/pdf/2505.13614), [HTML](https://arxiv.org/abs/2505.13614)
### Authors
Ke Sun
### Background
现代深度神经网络的高维参数空间被称为‘神经丛’，具有由Fisher信息定义的独特度量张量。估计这种张量对于理论分析和实际的深度学习方法都至关重要。本文旨在通过分析分类网络的概率分布核心空间来研究这种张量的谱，从而将发现延伸到神经丛上的确定性界，并引入基于Hutchinson跟踪估计的无偏随机度量张量估计。
### Innovation
论文提出了将度量张量的估计转换到低维概率分布核心空间中的新方法，并且通过Hutchinson跟踪估计提出了一种无偏随机估计方法，该方法可在单次反向传播过程中高效评估，并且与真实值的偏差可被准确控制。
### Conclusion
通过对核心空间进行详细分析，以及对神经丛上度量张量的确定性界和随机估计的引入，该研究表明了Fisher信息如何在深度学习中提供重要见解，并为进一步理论和实用方法的研究提供了基础。
## 599. `cs.LG` - 防御边缘计算中的后门攻击：基于代表注意的防御 [PDF](https://arxiv.org/pdf/2505.10297), [HTML](https://arxiv.org/abs/2505.10297)
### Authors
Chibueze Peace Obioma,Youcheng Sun,Mustafa A. Mustafa
### Background
联邦学习(Federated Learning)面临高度脆弱的适应性后门攻击威胁，这些攻击通过紧密模仿良性更新统计来保持隐蔽性。现有的防御方法主要依赖参数或梯度空间的异常检测，忽视了后门攻击必须满足的行为约束，以确保触发器的可靠激活。现有的基于异常的方法无法有效防御那些规范化更新幅度并模仿良性统计模式，同时保持后门功能的适应性攻击，从而在检测方面留下了基础的缺陷。
### Innovation
本文提出了FeRA（Federated Representative Attention）——一种新颖的基于注意力的防御方法，将检测范式从基于异常的分析转变为基于一致性的分析。FeRA 利用了后门在训练轮次中持续存在的内在需求，通过在表示空间中的低方差一致性或幅度放大来识别恶意客户端。框架结合频谱和空间注意力、方向对齐、互相似性和范数放大，实现了两个互补的检测机制，即一致性分析和范数放大检测，通过这种机制可以隔离恶意客户端。
### Conclusion
通过在六个数据集、九种攻击和三种模型架构下的广泛评估，验证FeRA在不同独立同分布(IID)和非IID设置下实现最优的后门缓解。在不同的非IID设置下，FeRA的平均后门准确率(Backdoor Accuracy, BA)最低，仅为约1.67%，同时保持高清洁准确性，优于其他最先进的防御方法。相关代码可以在此处获取：this https URL。
## 600. `cs.LG` - 边缘设备上语言模型推理的可行性和权衡：有时痛苦但必定前景广阔 [PDF](https://arxiv.org/pdf/2503.09114), [HTML](https://arxiv.org/abs/2503.09114)
### Authors
Maximilian Abstreiter,Sasu Tarkoma,Roberto Morabito
### Background
语言模型（LMs）的迅速发展扩大了自然语言处理的能力，广泛应用于文本生成和复杂决策等领域。尽管最先进的LMs通常具有数百亿参数并在数据中心部署，但最近的趋势显示，紧凑型模型（一般不到100亿参数）因其量化和其他模型压缩技术的应用而受到越来越多的关注。这种转变开辟了在边缘设备上部署LMs的可能性，带来了增强的隐私性、减少的延迟和改善的数据主权等潜在好处。然而，这些较小模型的固有复杂性与边缘硬件的有限计算资源的结合，引发了在云外执行LM推理时的实际权衡问题。
### Innovation
本文通过对代表性的CPU和GPU加速边缘设备上的生成LM推理进行了全面评估。它测量了关键性能指标，如内存使用、推理速度和能耗，并在各种设备配置下进行。研究还探讨了吞吐量-能耗权衡、成本考虑和易用性，并对模型的定性性能进行了评估。虽然量化有助于缓解内存占用，但并不能完全消除资源瓶颈，特别是对于大型模型。研究量化了实践中需要考虑的内存和能耗限制，提供了在模型大小、推理性能和效率之间做出权衡的具体见解。
### Conclusion
边缘设备上语言模型的探索仍处于初级阶段。希望这项研究为未来的进一步研究奠定基础，指导模型的细化、推理效率的提升以及边缘为中心AI系统的推进。
## 601. `cs.LG` - Muon优化器的收敛界和关键批次大小 [PDF](https://arxiv.org/pdf/2507.01598), [HTML](https://arxiv.org/abs/2507.01598)
### Authors
Naoki Sato,Hiroki Naganuma,Hideaki Iiduka
### Background
近期提出的优化器Muon利用了神经网络参数的内在矩阵结构，显示出了强大的实证性能，表明它可能成为AdamW等标准优化器的替代者。
### Innovation
提供了Muon优化器在四种实际设置下的收敛证明，系统地研究了Nesterov动量和权重衰减的包含与否对其行为的影响。证明了权重衰减值的引入带来了更紧的理论边界，并阐明了权重衰减系数与学习率之间的相互作用。推导出了优化Muon时最小化训练计算成本的关键批次大小，识别了控制这一值的超参数。
### Conclusion
理论分析证明了Muon优化器的实际性能，并通过实验证明了理论发现的有效性，包括图像分类和语言建模任务。
## 602. `cs.LG` - 全面评估原型神经网络 [PDF](https://arxiv.org/pdf/2507.06819), [HTML](https://arxiv.org/abs/2507.06819)
### Authors
Philipp Schlinge,Steffen Meinert,Martin Atzmueller
### Background
原型模型是可解释人工智能(XAI)和可解释机器学习的重要方法。本文对ProtoPNet、ProtoPool和PIPNet等几种重要的原型模型进行了深入分析。
### Innovation
本文不仅应用了标准的文献中提出的评估指标，还提出了几个新的评估指标，以进一步完善模型可解释性分析。此外，本文还在细粒度分类、非IID设置和多标签分类等多种数据集上对原型模型进行实验，以更全面地对比其性能。
### Conclusion
本文还提供了基于开源库的代码（提供链接），该库不仅方便直接应用这些指标，还具有良好的扩展性，便于添加新指标和模型。
## 603. `cs.LG` - 拓扑感知神经插值的标量场 [PDF](https://arxiv.org/pdf/2508.17995), [HTML](https://arxiv.org/abs/2508.17995)
### Authors
Mohamed Kissi,Keanu Sisouk,Joshua A. Levine,Julien Tierny
### Background
研究了时间变化的标量场的拓扑感知插值方法。给定时间变化的持久图序列和相应的稀疏时间采样的标量场关键帧，本文的方法旨在通过“反转”非关键帧的持久图来生成缺失数据的合理估计。
### Innovation
提出了一种神经架构，它基于关键帧示例学习时间值与相应标量场之间的关系，并可靠地将其关系扩展到非关键帧时间步。通过引入特定的拓扑损失，使用输入的持久图来增强神经网络架构，从而改善非关键帧时间步的几何重建和拓扑重构。
### Conclusion
实验结果表明，在二维和三维时间变化数据集上的插值表现优于参考插值方案。相关方法已在GitHub上开源。
## 604. `cs.LG` - SHIELD: 安全的超网络增量扩展学习防御 [PDF](https://arxiv.org/pdf/2506.08255), [HTML](https://arxiv.org/abs/2506.08255)
### Authors
Patryk Krukowski,Łukasz Gorczyca,Piotr Helm,Kamil Książek,Przemysław Spurek
### Background
在对抗条件下持续学习仍然是一个开放性问题，现有方法往往在鲁棒性、可扩展性或两者之间做出妥协。
### Innovation
提出了一种新的框架，将区间传播（IBP）与基于超网络的架构相结合，以实现顺序任务中的可认证鲁棒持续学习。该方法通过共享超网络生成任务特定的模型参数，该超网络仅依赖紧凑的任务嵌入，从而避免了重播缓冲区或完整模型拷贝的需求，实现随时间的高效学习。为增强鲁棒性，引入了区间混合策略，这种策略通过在混合点为中心的boldsymbol{l}_{boldsymbol{boldsymbol{boldsymbol{boldsymbol{boldsymbol{boldsymbol{∞}}}}}}}$球中融合虚拟示例，利用区间算术，该技术可以保证鲁棒性并缓解缠绕效应，形成更平滑的决策边界。
### Conclusion
在包括PGD和AutoAttack在内的强大白盒对抗攻击下，SHIELD在多个基准测试上的一致性能超过了现有的鲁棒持续学习方法，同时保持了可扩展性和认证性。这些结果标志着向对抗环境中实用和理论指导下的持续学习迈出了重要的一步。
## 605. `cs.LG` - 软决策树在生存分析中的应用 [PDF](https://arxiv.org/pdf/2506.16846), [HTML](https://arxiv.org/abs/2506.16846)
### Authors
Antonio Consolo,Edoardo Amaldi,Emilio Carrizosa
### Background
决策树在生存分析中因其可解释性和对复杂关系的建模能力而受到欢迎。传统的生存树通常通过启发式方法构建，用于预测单一事件的时间，并使用被截断的历史数据。近年来，全球优化的树结构引起了越来越多的关注，这类树的整体结构通过最小化所有参数的误差函数进行训练。传统的生存树通常缺乏灵活性和解释性，每一分支节点通常使用硬分割规则。
### Innovation
本文提出了一种新的软生存树模型（SST），在每个分支节点采用软分割规则，并通过易于分解的非线性优化公式进行训练。SSTs 为每个输入向量提供一个与单一叶子节点相关的具体生存函数，满足条件计算性质，并继承相关优势。SSTs 结合了灵活性和可解释性：可以使用最大似然估计的任意平滑生存函数（参数、半参数或非参数），且每个 SST 的叶子节点都对应一组独特的生存函数，这些生存函数与输送到它们的数据点相关。15 组知名数据集的数值实验表明，使用节点分解算法（Consolo等，2024）进行调整训练的 SSTs，特别是在使用参数和样条为基础的半参数生存函数时，相对于三种基准生存树在四个常用判别和校准指标方面表现更优。SSTs 还可以扩展以考虑群体公平性。
### Conclusion
SSTs 作为一种新的全局优化生存树模型，通过软分割规则和非线性优化训练，提高了生存分析的灵活性和解释性，特别是使用最大似然估计的各种平滑生存函数。实验结果表明，SSTs 在多个基准数据集上的性能优于传统生存树，并且有可能扩展以考虑群体公平性。
## 606. `cs.LG` - HiCL: 基于海马神经元的连续学习 [PDF](https://arxiv.org/pdf/2508.16651), [HTML](https://arxiv.org/abs/2508.16651)
### Authors
Kushal Kapoor,Wyatt Mackey,Yiannis Aloimonos,Xiaomin Lin
### Background
现有的连续学习模型存在灾难性遗忘的问题，即当学习新任务时，旧任务的表现会急剧下降。为了解决这一问题，本文提出了一种名为HiCL的新颖连续学习架构，该架构受人类海马神经元的启发，旨在减轻灾难性遗忘。
### Innovation
HiCL架构包括两个关键模块：一个通过类格细胞层编码输入，并使用受齿状回启发的模块进行稀疏模式分离，通过在CA3样自联想记忆中维护事件记忆痕迹；以及一个DG门控制的专家混合机制，根据余弦相似度将输入路由到任务特定的DG原型，该原型通过在线指数移动均值计算。这种基于生物学原理且数学合理的门控策略能够实现可微的、可扩展的任务路由，而无需单独的门控网络，从而提高了模型学习多个连续任务的适应性和效率。
### Conclusion
通过在标准连续学习基准测试上的评估，HiCL架构展示了其在减少任务干扰方面的有效性，并在较低的计算成本下实现了接近最先进的连续学习任务结果。
## 607. `cs.LG` - 利用强化生成组合结构：复杂性理论的应用 [PDF](https://arxiv.org/pdf/2509.18057), [HTML](https://arxiv.org/abs/2509.18057)
### Authors
Ansh Nagda,Prabhakar Raghavan,Abhradeep Thakurta
### Background
本文探讨了基于人工智能的方法是否能够帮助我们在复杂性理论方面取得进展。研究团队使用AlphaEvolve（一种代码变异代理）在三个特定场景中得到了新成果，展示了AI在复杂性理论中的潜力。
### Innovation
1. 提高了Kunisky和Yu的结果，对随机3-和4-正则图的MAX-CUT和MAX-独立集认证算法的上界和（条件性）下界提供了更接近最优的结果。2. 提出了新的MAX-4-CUT和MAX-3-CUT的不完全近似结果，证明了它们的NP难性，因子分别为0.987和0.9649，改进了现有技术的最佳结果。3. 提出了新的性质不完全近似结果，证明了度量旅行商问题的NP难性，因子为111/110，改进了现有技术的最佳结果。在这一过程中，提供了一种新的模块化证明技巧。关键技术挑战在于验证AlphaEvolve生成的候选构造是昂贵的，有时候需要时间呈指数增长。作者利用AlphaEvolve自身的进化，加速了验证过程。
### Conclusion
本文的结果表明，基于工具的证明将从基于AI的工具中受益，以获得更强的结果。
## 608. `cs.LG` - 为表格数据生成不可感知的在流形上的对抗攻击 [PDF](https://arxiv.org/pdf/2507.10998), [HTML](https://arxiv.org/abs/2507.10998)
### Authors
Zhipeng He,Alexander Stevens,Chun Ouyang,Johannes De Smedt,Alistair Barros,Catarina Moreira
### Background
表格数据因其混合类别和数值特征的异质性质，对抗攻击存在独特挑战。像素扰动在图像中保持视觉相似性，而在表格数据中缺乏直观的相似性度量，使得难以定义不可感知的修改。传统的基于梯度的方法优先考虑特定的范数约束，经常产生偏离原始数据分布的对抗样本。
### Innovation
提出了一种使用混合输入变分自编码器（VAE）的潜在空间扰动框架，以生成统计上一致的对抗样本。该VAE将类别嵌入与数值特征整合到一个统一的潜在流形中，允许保留统计一致性的扰动。引入了分布内成功率（IDSR），同时评估攻击效果和分布一致性。
### Conclusion
在六组公开数据集和三种模型架构上的评估表明，本文方法的异常值率明显较低且性能更一致，相比传统的输入空间攻击和其他适应图像领域方法的VAE基方法。全面分析超参数敏感性、稀疏控制和生成架构表明，基于VAE的攻击效果强烈依赖于重构质量和足够的训练数据。当这些条件满足时，本文提出的框架在实用性和稳定性方面明显优于输入空间方法。本研究强调了在表格领域生成真实且鲁棒的对抗样本时保持在流形上的修改的重要性。
## 609. `cs.LG` - ResCP: Reservoir Conformal Prediction for Time Series Forecasting [PDF](https://arxiv.org/pdf/2510.05060), [HTML](https://arxiv.org/abs/2510.05060)
### Authors
Roberto Neglia,Andrea Cini,Michael M. Bronstein,Filippo Maria Bianchi
### Background
现有的基于自举预测的时间序列方法依赖于构建较为复杂的时间模型来捕捉时间依赖性。这些方法在小样本情况下容易失败，并且在数据分布发生变化时需要昂贵的重新训练。
### Innovation
提出了一种名为Reservoir Conformal Prediction (ResCP) 的新型无监督训练方法，它可以利用蓄水池计算的效率和表示学习能力动态调整一致性得分的权重。其特别之处在于计算蓄水池状态之间的相似度得分，并在每个步骤中适应性地重新加权观察到的残差。
### Conclusion
我们证明在合理假设下，ResCP实现了渐近条件覆盖，并通过跨多样预测任务的实验证明了其有效性。
## 610. `cs.LG` - 基于稀疏自编码器的模型无关文本到图像生成性别偏见控制 [PDF](https://arxiv.org/pdf/2507.20973), [HTML](https://arxiv.org/abs/2507.20973)
### Authors
Chao Wu,Zhenyi Wang,Kangxian Xie,Naresh Kumar Devulapally,Vishnu Suresh Lokhande,Mingchen Gao
### Background
文本到图像（T2I）扩散模型经常会表现出性别偏见，尤其是在将职业与性别化主体关联时表现出刻板印象。现有的方法通常依赖于CLIP基过滤或提示工程，但这些方法常常需要特定模型的调整，并且提供有限的控制。
### Innovation
本文提出了一种基于稀疏自编码器(SAE)的轻量化且模型无关的框架(SAE Debias)，用于减轻T2I生成过程中的性别偏见。它直接在特征空间中工作，无需重新训练或架构修改。该方法利用预训练在性别偏见数据集上的稀疏自编码器来识别与性别相关的方向，捕捉职业刻板印象，并通过在推理过程中抑制职业的偏见方向，引导生成更加性别平衡的结果。训练一次后，稀疏自编码器提供了一个可重用的去偏见方向，为社会负责的生成AI提供了一种解释和模型无关的工具。
### Conclusion
SAE Debias在多个T2I模型（包括Stable Diffusion 1.4, 1.5, 2.1和SDXL）上进行了广泛评估，显示出显著减少性别偏见同时保持生成质量的能力。据我们所知，这是首次将稀疏自编码器应用到识别和干预T2I模型中的性别偏见的工作。这些发现有助于构建社会责任感更强的生成AI，提供了一种解释性和模型无关的工具，以支持文本到图像生成的公平性。
## 611. `cs.LG` - 具有内在探索性的大型语言模型高效强化学习 [PDF](https://arxiv.org/pdf/2511.00794), [HTML](https://arxiv.org/abs/2511.00794)
### Authors
Yan Sun,Jia Guo,Stanley Kok,Zihao Wang,Zujie Wen,Zhiqiang Zhang
### Background
强化学习带有可验证奖励（RLVR）能够提升大型语言模型的推理能力，但仍面临高昂的训练成本，因为很多rollout对优化贡献不多，且计算需求大。
### Innovation
提出了PREPO，这是一种通过利用内在数据特性提高数据效率的方法。具体包括采用提示困惑度作为模型适应性的指标，促使模型从熟悉的上下文过渡到更具挑战性的内容；并通过增强rollout之间的差异性来优先处理探索度较高的序列，从而在减少rollout需求的同时保持竞争力。
### Conclusion
PREPO在Qwen和Llama模型上实现了在数学推理基准测试上最多减少3倍rollouts的有效结果，并在理论上和深入分析了该方法提高RLVR数据效率的内在理由。
## 612. `cs.LG` - Bootstrap Off-policy with World Model [PDF](https://arxiv.org/pdf/2511.00423), [HTML](https://arxiv.org/abs/2511.00423)
### Authors
Guojian Zhan,Likun Wang,Xiangteng Zhang,Jiaxin Gao,Masayoshi Tomizuka,Shengbo Eben Li
### Background
在线规划已被证明在增强学习(强化学习，RL)中提高样本效率和最终性能方面非常有效。然而，规划在环境交互中使用时，会导致收集的数据与策略的实际行为之间出现偏差，这对模型学习和策略改进都造成了负面影响。
### Innovation
提出了一种名为BOOM（Bootstrap Off-policy with WOrld Model）的新框架，将在线规划与离策略学习紧密结合。该框架通过一个循环过程来改进策略：通过行为对齐逐步调整策略，循环过程由一个联合学习的世界模型支持，该模型允许规划者模拟未来的轨迹，并提供价值目标以促进策略改进。BOOM的核心是一种无概率分布对齐损失，利用规划者的非参数动作分布来启动策略，并结合一种软值加权机制，优先处理高回报的行为，并减轻回放缓冲区中规划者动作质量的变异性。
### Conclusion
在DeepMind Control Suite和Humanoid-Bench的实验结果表明，BOOM在训练稳定性和最终性能方面均达到最先进的效果。相关代码已公开在指定的URL地址。
## 613. `cs.LG` - 一小型数学模型：在受LLM启发的架构中重新阐释策略选择理论 [PDF](https://arxiv.org/pdf/2509.24068), [HTML](https://arxiv.org/abs/2509.24068)
### Authors
Roussel Rahman,Jeff Shrager
### Background
策略选择理论（SCT，Siegler和Shrager，1984；Siegler，2000）通过学习自然发展的数据、概率表示、基于信心的记忆检索和阶梯式的策略支撑（如手指计数）等原则，解释了儿童算术学习的重要方面。
### Innovation
作者将SCT重塑为“小型数学模型”（SMM），采用基于神经网络的架构，类似于大型语言模型（LLM），并进一步扩展SCT，包括加法练习、符号嵌入和门控注意等功能。该模型展示了在加法和计数之间建构性和破坏性干扰，并改进了手指计数作为结果回忆的“波状”使用。未来计划将SMM扩展到SCT长期项目的后续方面，包括适应性策略选择和最终的策略发现，形成统一的研究平台，探讨对于数学推理至关重要的数字特性和关系。
### Conclusion
该SMM为基于LLM代理的发展提供了一个统一平台，研究数学推理中的数字特性和关系是如何形成的。
## 614. `cs.LG` - 从噪声到叙事：Transformer中幻觉起源的追踪 [PDF](https://arxiv.org/pdf/2509.06938), [HTML](https://arxiv.org/abs/2509.06938)
### Authors
Praneet Suresh,Jack Stanley,Sonia Joseph,Luca Scimeca,Danilo Bzdok
### Background
随着生成式AI系统在科学、商业和政府等领域变得更为能干且普及，深入理解其失败模式的需求变得迫切。它们偶尔表现出的不可预测性，比如变压器模型的幻觉倾向，影响了新兴AI解决方案在关键领域中的信任度和采用率。
### Innovation
通过使用稀疏自编码器捕捉的概念表示，在实验可控的输入不确定性条件下，我们研究了预训练变压器模型中幻觉的产生及其机制。系统性的实验揭示，随着输入信息的不断不规则化，变压器模型所使用的意义概念数量也会增加。在输入空间高度不确定性的情况下，变压器模型更可能激活输入无关但连贯的意义特征，导致幻觉输出。特别是，当我们使用纯噪声输入时，我们发现了预训练变压器模型中广泛触发且有意义的中间激活的概念，这些概念的功能完整性通过定向控制得到了验证。此外，我们展示了可以从变压器层激活中嵌入的概念模式可靠预测变压器模型输出的幻觉。
### Conclusion
我们的这些见解直接关系到使AI模型与人类价值观保持一致、AI安全性、增加潜在对抗攻击的攻击面，以及为模型幻觉风险的自动量化提供基础。
## 615. `cs.LG` - 利用转移学习的神经推荐系统进行离子液体性质预测 [PDF](https://arxiv.org/pdf/2509.10273), [HTML](https://arxiv.org/abs/2509.10273)
### Authors
Sahil Sethi,Kai Sundmacher,Caroline Ganzer
### Background
离子液体（ILs）因其可精确定制的物理化学性质而在替代传统溶剂方面展现出广泛的应用潜力。然而，准确预测关键的热物性仍然是个挑战，这主要是由于存在的化学设计空间非常大，以及实验数据的有限性。
### Innovation
本文提出了一种数据驱动的迁移学习框架结合神经推荐系统（NRS），通过稀疏的实验数据集能够可靠地预测离子液体的性质。该方法包括两个阶段：首先，在固定温度和压力下使用COSMO-RS模拟数据预训练NRS模型，然后将经过简单前馈神经网络微调的实验数据在不同温度和压力下进行适应。研究表明，该框架支持了跨性质的知识迁移，且通过预训练的密度、粘度和比热模型微调目标性质的模型显著提升了性能。
### Conclusion
最终训练的模型不仅能够对之前未见的离子液体表现出稳健的外推能力，而且还能为超过70万种离子液体组合进行性质预测，为离子液体在过程设计中的筛选提供了可扩展的解决方案。这项工作证明了结合模拟数据和迁移学习在解决实验数据稀疏性问题上的有效性。
## 616. `cs.LG` - 全息知识流形：一种在大规模语言模型中实现连续学习而不发生灾难性遗忘的新型管道 [PDF](https://arxiv.org/pdf/2509.10518), [HTML](https://arxiv.org/abs/2509.10518)
### Authors
Justin Arndt
### Background
该研究背景是在AI知识表示中实现无灾难性遗忘的同时，保证最少的内存增长和高效率。当前的许多方法在处理连续学习任务时，都会面临灾难性遗忘的问题，即新的学习会损害之前学习到的知识。研究者们希望通过引入新的技术，解决这一问题。
### Innovation
该研究提出了Holographic Knowledge Manifold (HKM)，一种四阶段的管道系统。它采用了分形量化、概率缠结和动态衍射切片技术，有效地压缩了知识子模块，实现了三倍的压缩比，67%的存储节省，100%的全息集成，并支持了超过1,020次更新，每次增长仅为1%。在实验中，该系统在综合WikiText和FB15k数据集上展现了行业领先的性能，包括无遗忘、三倍压缩比以及在消费者级GPU硬件上的53%的训练时间减少。
### Conclusion
研究人员进行了假设的成本分析，预计在大规模情况下可节省9240万美元，同时减少21.2%的能源消耗和33%的碳足迹。该研究提出了一个大规模语言模型（LLMs）范式变革的可能性，允许“永恒”的适应能力而不重新训练。未来，该方法有可能借助多模态融合和量子硬件进一步普及，降低大规模模型如Llama-3或Grok-4的微调成本，最多可减少60-80%。
## 617. `cs.LG` - Conformal预测在捕捉 aleatoric 不确定性方面的表现 [PDF](https://arxiv.org/pdf/2509.05826), [HTML](https://arxiv.org/abs/2509.05826)
### Authors
Misgina Tsighe Hagos,Claes Lundström
### Background
Conformal预测是一种不受模型约束的生成具有高概率覆盖真实类别的预测集的方法。尽管预期预测集大小能够捕捉 aleatoric 不确定性，但缺乏这种有效性的相关证据。文献表明预测集大小可以作为 aleatoric 不确定性的上限或难以实例的预测集较大而简单实例较小，但验证 Conformal 预测器的这一属性的研究尚不存在。本研究旨在探讨 Conformal 预测器如何有效地量化 aleatoric 不确定性，特别是数据集中由于类别重叠引起的固有模糊性。通过测量预测集大小与每个实例由人工注释员分配的唯一标签数量之间的相关性来实现这一目标。进一步评估预测集与人工提供的注释之间的相似性。对于八个深度学习模型在四个数据集上的训练，使用三种 Conformal 预测方法生成预测集，且每个实例包含来自多名人工注释员（5至50名参与者）的注释，便于识别类别重叠。
### Innovation
本研究通过测量预测集大小与每个实例由人工注释员分配的唯一标签数量之间的相关性来评估 Conformal 预测在量化 aleatoric 不确定性方面的能力，并进一步评估预测集与人工提供的注释之间的相似性。使用三种 Conformal 预测方法为八个深度学习模型在四个数据集上生成预测集。
### Conclusion
研究结果显示，绝大多数 Conformal 预测输出与人类注释之间的相关性很弱到弱，只有少数相关性中等。这些发现强调了重新评估使用 Conformal 预测器生成的预测集的必要性。尽管它们可以提供真实类别的更高覆盖范围，但它们在捕捉 aleatoric 不确定性以及生成与人类注释相匹配的集合方面的能力仍然有限。
## 618. `cs.LG` - 在Bootstrapped DQN中的信息价值增强探索 [PDF](https://arxiv.org/pdf/2511.02969), [HTML](https://arxiv.org/abs/2511.02969)
### Authors
Stergios Plataniotis,Charilaos Akasiadis,Georgios Chalkiadakis
### Background
在深度强化学习中，高效探索仍然是一个基本挑战，特别是在高维度状态和稀疏奖励的环境中。传统的探索策略，如依赖随机局部策略噪声的ε-贪心和玻尔兹曼探索方法，往往难以有效地平衡探索和利用。
### Innovation
本文将信息价值（EVOI）的概念整合到著名的Bootstrapped DQN算法框架中，以增强算法的深度探索能力。作者开发了两种新的算法，将从学习信息价值中获得的预期收益融入到Bootstrapped DQN中。这些方法使用信息价值估计来衡量不同网络头部之间意见的差异，并引导探索向具有最大潜力的区域。
### Conclusion
研究者通过复杂的稀疏奖励Atari游戏实验评估了他们的算法，结果显示性能提高，并且更好地利用了不确定性，而无需引入额外的超参数。
## 619. `cs.LG` - 使用大型语言模型在可穿戴物联网系统中实现适应性和鲁棒的数据篡改检测与清理 [PDF](https://arxiv.org/pdf/2511.02894), [HTML](https://arxiv.org/abs/2511.02894)
### Authors
W.K.M Mithsara,Ning Yang,Ahmed Imteaj,Hussein Zangoti,Abdur R. Shahid
### Background
随着物联网（IoT）生态系统中可穿戴传感设备的广泛应用，特别是在医疗、智能家居和工业应用中，需要高度稳健的人体活动识别（HAR）技术来提升功能性和用户体验。尽管机器学习模型已经提升了HAR技术，但它们对数据投毒攻击越来越敏感，这种攻击会损害系统的数据完整性和可靠性。传统防御策略往往需要大量的、特定任务的标注数据训练，这限制了动态IoT环境中的适应性。
### Innovation
本文提出了一种新颖的框架，该框架利用大型语言模型（LLMs）在HAR系统中进行数据投毒检测和清理，采用了零样本、单样本和少量样本学习范式。该方法包括模拟专家角色进行传感器异常情境化和评估的任务提示策略，以及逐步推理引导LLM推断原始传感器数据中的投毒指标和可能的清理替代方案。这些策略减少了对大量数据集的依赖，并且能够在实时环境中提供稳健且灵活的防御机制。
### Conclusion
对该框架进行了全面评估，定量分析了检测准确率、清理质量、延迟和通信成本，从而展示了大型语言模型在提升可穿戴IoT系统的安全性和可靠性方面的可行性和有效性。
## 620. `cs.LG` - 探究更多，学习更好：互信息最小化下的并行MLLM嵌入 [PDF](https://arxiv.org/pdf/2511.01588), [HTML](https://arxiv.org/abs/2511.01588)
### Authors
Zhicheng Wang,Chen Ju,Xu Chen,Shuai Xiao,Jinsong Lan,Xiaoyong Zhu,Ying Chen,Zhiguo Cao
### Background
嵌入模型是现代AI的基础。随着多模态大型语言模型（MLLMs）的发展，它们在架构和数据收集方面取得了重要进展，但在整体范式上仍局限于单输入单一嵌入的结构，即对丰富、多面的输入进行简化的单体嵌入，未能充分利用MLLM的能力。
### Innovation
本文提出一种名为Parallel Decoupling Framework (PDF)的并行解耦框架，通过利用MLLMs的专用可调控性（即根据明确指令灵活生成差异化的响应），对输入进行多并行路径的条件化生成不同可学习的前端，生成并行嵌入。引入互信息最小化（MIM）作为明确约束，并结合路径间的对比性监督以保持语义对齐，实现广泛的语义覆盖和可推广的嵌入空间。模型的嵌入空间在推理中仅需一次前向传递，计算开销微乎其微。
### Conclusion
我们在多个MLLM主干上实例化PDF，并在MMEB基准上证明其有效性。其在各种分辨率和模型大小上均取得显著提升，例如，提升VLM2Vec-LLaVA-1.6-LR模型8.9%（7B），VLM2Vec-Qwen2VL模型2B版本4.2%、7B版本3.1%。在效率上，我们的2B模型在其基线之上仅使用一半的计算预算就取得了2.6%的提升。
## 621. `cs.LG` - 基于噪声时间序列学习混沌动力学的弱惩罚神经ODE [PDF](https://arxiv.org/pdf/2511.06609), [HTML](https://arxiv.org/abs/2511.06609)
### Authors
Xuyang Li,John Harlim,Dibyajyoti Chakraborty,Romit Maulik
### Background
复杂高维动态系统的准确预测对于科学和工程中的许多应用来说至关重要。然而，真实世界的测量通常受到噪声的干扰，这严重降低了数据驱动模型的性能。特别是在混沌动态系统中，一个小的误差会迅速放大，使得从噪声数据中识别出能够短期准确预测且能保持长期不变动力学性质的数据驱动模型非常具有挑战性。
### Innovation
本文提出了一种弱形式化作为数据驱动时间序列预测模型的经典强形式化的补充方法。具体地，我们关注神经常微分方程（NODE）架构。不同于标准的强形式化依赖于NODE的离散化和随后的优化，弱形式化通过在时间子区间上的一组集成残差约束模型。通过将弱形式化作为一种惩罚方法与经典强形式化的学习结合使用，我们可以进一步提高NODE模型的性能。研究结果表明，我们提出的方法，称为弱惩罚NODE（WP-NODE），在基准混沌动态系统和真实世界的气候数据集上实现了最先进的预测准确性和卓越的鲁棒性。
### Conclusion
通过数值演示，证明了我们提出的训练策略——弱惩罚NODE——在基准混沌动态系统和真实世界的气候数据集上实现了最先进的预测准确性和卓越的鲁棒性。
## 622. `cs.LG` - 基因下一个碱基预测器是上下文学习者 [PDF](https://arxiv.org/pdf/2511.12797), [HTML](https://arxiv.org/abs/2511.12797)
### Authors
Nathan Breslow,Aayush Mishra,Mahler Revsine,Michael C. Schatz,Anqi Liu,Daniel Khashabi
### Background
之前的研究主要关注大型语言模型在通过预测自然语言中词的下一个词进行训练时表现出的能力（即在输入中从实例中推断和应用抽象模式的能力），这种现象通常被归因于人类语言特有的统计特性。因此，研究提出一个基本的问题：这种能力是否能在其他符号序列域中，仅通过大规模预测性训练自然地出现？基因序列作为一个富含统计结构的替代符号域，提供了探索这一问题的机会。
### Innovation
研究者采用了控制实验框架，将语言和基因型推理任务实例化，并将基因模型与语言模型在上下文学习能力上进行直接比较。结果显示，基因模型在上下文示例数量增加时，也表现出对模式归纳的对数线性收益。这是首次在基因序列中发现自然出现的上下文学习能力的证据，支持了大规模预测建模在丰富数据集上自然产生上下文学习的能力的假说。这些发现扩展了预测性元学习的范围，为上下文学习提供了一个统一的、模态无关的观点。
### Conclusion
研究成果表明，基因模型与语言模型类似，在上下文示例数量增加时，能够自然地产生模式归纳的能力，这意味着上下文学习可能是由大规模预测建模在丰富数据上产生的结果。这一发现不仅扩展了传统意义上的上下文学习能力，还为跨模态的理解提供了新的视角。
## 623. `cs.LG` - 半监督矩阵填充的泛化误差边界的理论研究 [PDF](https://arxiv.org/pdf/2511.13049), [HTML](https://arxiv.org/abs/2511.13049)
### Authors
Antoine Ledent,Mun Chong Soo,Nong Minh Hieu
### Background
本文研究了一个矩阵填充问题，其中真实矩阵$R$和观测到的未标记数据的未知抽样分布$P$都是低秩矩阵，并共享一个共同子空间。我们知道一定的未标记数据来自分布$P$，还有少量来自同一分布并带有噪声的标记数据。这个设置类似于推荐系统的情景，其中未标记数据代表“隐式反馈”（如购买、点击等互动），标记数据代表“显式反馈”（用户对项目的显式评分互动）。通过利用低秩子空间恢复理论的结果以及矩阵填充模型的经典泛化界，本文展示了误差边界包括两个部分，分别与估计$P$和真实矩阵$text{ground}$相对应，这两个部分的误差分别遵循$tilde{O}bigl(frac{text{nd}}{M}bigr)^{frac{1}{2}}$和$tilde{O}bigl(frac{text{dr}}{N}bigr)^{frac{1}{2}}$的量级。
### Innovation
本文创新地探讨了一种半监督矩阵填充方法，利用未标记数据和少量标记数据共同估计真实矩阵和抽样分布。通过结合低秩子空间恢复理论和矩阵填充模型的泛化界，提出了新的误差界公式，明确区分了两种不同类型的误差，展示了该方法在推荐系统中应用的潜力，特别是在利用隐式反馈方面。
### Conclusion
通过合成实验和实际数据（如Douban和MovieLens）进行验证，本文方法在仅依赖显式反馈的基准模型上表现出更好的性能，验证了该假设的有效性及作为研究推荐系统中显式与隐式反馈交互的有效理论设置。
## 624. `cs.LG` - GeoPTH: 基于几何原型轨迹哈希的轻量级类别轨迹检索方法 [PDF](https://arxiv.org/pdf/2511.16258), [HTML](https://arxiv.org/abs/2511.16258)
### Authors
Yang Xu,Zuliang Yang,Kai Ming Ting
### Background
轨迹相似检索是时空数据挖掘中的一个重要组成部分，但现有方法存在以下局限性：传统的度量标准计算成本高，而基于学习的方法则面临较高的训练成本和潜在的不稳定问题。
### Innovation
本文提出了一种名为 Geometric Prototype Trajectory Hashing (GeoPTH) 的新型、轻量级且无需学习的框架，用于高效地基于类别的轨迹检索。GeoPTH 使用保有几何特征的小点集作为锚点来构造数据依赖性的哈希函数。
### Conclusion
实验结果表明，GeoPTH 的检索准确性与传统的度量标准及最先进的学习方法相当，并且在效率上显著优于通过简单二进制化学习嵌入生成的二进制代码。我们的研究表明，轻量级、以原型为中心的方法提供了一种实用而强大的替代方案，实现了优异的检索性能和计算效率。
## 625. `cs.LG` - SCALEX: 可扩展的概念和潜在空间探索在扩散模型中 [PDF](https://arxiv.org/pdf/2511.13750), [HTML](https://arxiv.org/abs/2511.13750)
### Authors
E. Zhixuan Zeng,Yuhao Chen,Alexander Wong
### Background
图像生成模型经常编码社会偏见，包括与性别、种族和职业相关的刻板印象。现有的分析扩散模型中这些偏见的方法要么专注于预定义的类别，要么依赖于对潜在方向的手动解释。这些限制导致了可扩展性差和对隐含或未预见模式的发现受阻。
### Innovation
作者引入了SCALEX框架，这是一种用于扩散模型潜在空间可扩展且自动化的探索框架。SCALEX仅使用自然语言提示从H空间提取语义上具有意义的方向，无需重新训练或标签化即可实现零样本解释。这使得用户能够系统地比较任意概念并大规模发现内部模型关联。
### Conclusion
通过将提示直接链接到潜在方向，SCALEX在扩散模型中的偏见分析比现有方法更具有可扩展性、可解释性和可扩展性。该框架能够检测职业提示中的性别偏见、根据身份描述的语义对齐进行排名，并揭示在无监督的情况下聚集的概念结构。
## 626. `cs.LG` - 具备SU($d$)对称性的超越多项式量子加速的交错量子算法 [PDF](https://arxiv.org/pdf/2207.07250), [HTML](https://arxiv.org/abs/2207.07250)
### Authors
Han Zheng,Zimu Li,Sergii Strelchuk,Risi Kondor,Junyu Liu
### Background
本文介绍了一种针对具有任意SU$(d)$对称性的物理系统上特定机器学习任务的等变卷积量子算法框架。该框架旨在增强一种自然的量子计算模型——置换量子计算（PQC），并定义了更强大的模型PQC+。尽管PQC已被证明可以高效地经典模拟，但仍存在可以被PQC+高效解决的问题，而目前并没有已知的经典多项式时间算法来解决这些问题，这为PQC+的不可经典模拟性提供了证据。此外，作者还讨论了可以在PQC+框架下执行的实际的量子机器学习算法。
### Innovation
本文提出了PQC+模型，该模型能够解决经典的多项式时间算法无法解决的问题，从而可能为量子计算提供超越多项式的加速。引入了一种新型的等变卷积量子算法框架，适用于具有任意SU$(d)$对称性的物理系统。
### Conclusion
该研究提供了一个新的框架来实现PQC+模型，其中包含的算法可能在特定的机器学习任务上实现量子优势。尽管PQC+无法被经典计算有效模拟，但其实际应用场景和潜在计算优势仍有待进一步探索。
## 627. `cs.LG` - 低秩神经表示的熵解 [PDF](https://arxiv.org/pdf/2406.05694), [HTML](https://arxiv.org/abs/2406.05694)
### Authors
Donsub Rim,Gerrit Welper
### Background
本文研究的是非线性标量守恒律在单一空间维度上的光滑凸函数通量的熵解表示方法。现有的表示方法通常基于特性的方法，本文提出了一种新的表示方法，这是一种特性的推广形式，并且具有复合形式。虽然它是非线性的，但是解决变量中的动力学是线性的。
### Innovation
本文创新地提出了熵解的低秩神经表示。这种表示形式是通过将前馈神经网络的架构设计为低秩结构，并将其离散化为隐式神经表示所构成的流形实现的。这种方法不仅能够线性表示动力学，而且在固定层数和较小系数的情况下，能够逼近任意复杂度的波状拓扑的熵解。
### Conclusion
研究结果表明，低秩神经表示方法可以在层固定数量和少量系数的情况下，无论波状拓扑的复杂程度如何，都能逼近任意的熵解。
## 628. `cs.LG` - GRaF 通用射频辐射场用于空间频谱合成 [PDF](https://arxiv.org/pdf/2502.05708), [HTML](https://arxiv.org/abs/2502.05708)
### Authors
Kang Yang,Yuning Chen,Wan Du
### Background
现有方法通常是特定场景的训练，使用通用的NeRF（神经辐射场）架构适应射频（RF）领域的射频信号传播模拟，但这些方法缺乏跨场景的泛化能力。
### Innovation
提出了一种名为GRaF（Generalizable Radio-Frequency Radiance Fields）的新框架，能够在任意的发送器或接收器位置上合成空间频谱。GRaF 包含两个部分：一个几何感知的Transformer编码器，可以捕获邻近发送器的空间相关性，学习场景独立的射频（RF）辐射场；以及一个神经光追算法，用于估计在接收器处的频谱接收。
### Conclusion
实验结果表明，GRaF 在单一场景基准测试中优于现有方法，并在未见过的场景布局中达到了最先进的性能。
## 629. `cs.LG` - (De)-正则化的最大均值偏差梯度流 [PDF](https://arxiv.org/pdf/2409.14980), [HTML](https://arxiv.org/abs/2409.14980)
### Authors
Zonghao Chen,Aratrika Mustafi,Pierre Glaser,Anna Korba,Arthur Gretton,Bharath K. Sriperumbudur
### Background
现有的梯度流方法在将样本从源分布转移到目标分布时，或者由于缺乏可处理的数值实现（如$f$-散度流），或者由于需要强大的假设（如最大均值差异流），而导致收敛性难以保证。本研究引入了一种最大均值差异（DrMMD）及其 Wasserstein 梯度流的（脱）正则化，旨在克服这些限制。
### Innovation
提出了DrMMD流，能够在连续时间和离散时间两种情况下，对广泛的靶分布提供近乎全局的收敛性保证，并且可以通过使用样本以闭式形式实现。通过一个自适应的（脱）正则化时间表在整个流中优化离散化误差和χ^2 区域偏差之间的权衡。
### Conclusion
通过若干数值实验，证明了DrMMD流在大尺度训练学生/教师网络等应用中的潜在价值。
## 630. `cs.LG` - 协作网络架构：学习结构化的网络作为感觉模式的表示 [PDF](https://arxiv.org/pdf/2407.05650), [HTML](https://arxiv.org/abs/2407.05650)
### Authors
Pascal J. Sager,Jan M. Deriu,Benjamin F. Grewe,Thilo Stadelmann,Christoph von der Malsburg
### Background
当前的视觉系统在应对噪声、变形和分布外数据时存在挑战。本文介绍了一种新的模型——协作网络架构（CNA），使用结构化的、递归连接的神经元网络来表示感官信号。CNA能够处理这些挑战，提供对噪声、变形和分布外数据的鲁棒性。
### Innovation
CNA模型通过学习统计学上的感官输入规律，动态地组装神经元网络片段（称为'nets'）。nets可以无监督地学习，并灵活地重新结合，以编码新的模式，支持图象补全和对噪声的抗性。这一架构为发展能整合局部特征处理与全局结构形成的神经表示提供了一个新的视角。
### Conclusion
研究结果证明CNA是一种前景广阔的方法，适用于开发神经表示，该表示结合了局部特征处理和全局结构形成。这一发现为未来的研究提供了基础，特别是在不变对象识别方面。
## 631. `cs.LG` - Reservoir computing中的信息处理能力的渐进评估 [PDF](https://arxiv.org/pdf/2502.15769), [HTML](https://arxiv.org/abs/2502.15769)
### Authors
Yohei Saito
### Background
水库计算（RC）因其短训练时间而变得越来越重要。信息处理能力（IPC）是指通过目标输出的平方误差来评估RC系统的性能。由于RC旨在学习输入和输出时间序列之间的关系，因此应该评估无限长数据的IPC而不是有限长度数据的IPC。然而，目前还没有评估无穷长数据IPC的方法。
### Innovation
作者利用IPC的渐进展开和加权最小二乘拟合来评估无穷长数据的IPC，并通过数值模拟验证了该方法的有效性，从而使RC的性能评估更加明确。
### Conclusion
该工作使得RC的性能评估更加明显。
## 632. `cs.LG` - Meta-World+: 一个改进的标准化强化学习基准 [PDF](https://arxiv.org/pdf/2505.11289), [HTML](https://arxiv.org/abs/2505.11289)
### Authors
Reginald McLean,Evangelos Chatzaroulas,Luc McCutcheon,Frank Röder,Tianhe Yu,Zhanpeng He,K.R. Zentner,Ryan Julian,J K Terry,Isaac Woungang,Nariman Farsad,Pablo Samuel Castro
### Background
Meta-World 广泛用于评估多任务和元强化学习代理，使其能够同时掌握多种技能。然而，自引入以来，Meta-World 一直在经历许多未记录的变化，这阻碍了算法之间的公平比较。
### Innovation
本文旨在从文献中澄清这些结果，并利用过去版本的 Meta-World 提供关于多任务和元强化学习基准设计的见解。作为一个创新点，作者发布了一个新的开源 Meta-World 版本，该版本具有完全可再现性，技术使用更加便捷，并允许用户更灵活地选择基准中的任务。
### Conclusion
通过这个过程，作者发布了一个新的 Meta-World 版本，该版本不仅能够完全再现过去的实验结果，而且操作上更加方便，同时也为未来研究提供了更多的灵活性和便利性。
## 633. `cs.LG` - 基于样条的Kolmogorov-Arnold网络特征重要性：监督分类表数据降维的框架 [PDF](https://arxiv.org/pdf/2509.23366), [HTML](https://arxiv.org/abs/2509.23366)
### Authors
Ange-Clément Akazan,Verlon Roel Mbingui
### Background
在许多基于表格的数据预测问题中，特征选择是一个关键步骤。候选特征可能冗余、噪声大或信息量不足。研究者通常使用特征选择方法来提高模型的泛化能力和性能。Kolmogorov-Arnold网络（KANs）通过使用样条函数参数化特征变换，并以自然方式暴露每个特征的重要性分数。论文基于这一思想，提出并比较了四种KAN基础选择标准，并将其与标准方法如LASSO、随机森林特征重要性、互信息以及SVM-RFE进行了对比。
### Innovation
论文创新性地提出了基于KAN的特征选择方法，并具体描述了四种特征选择标准：系数范数、基于梯度的显著性以及剔除得分。这些方法在多个真实和合成的数据集上与传统方法进行了比较。结果表明，基于KAN的选择器通常与经典基准相当甚至优于传统方法。具体来说，在分类任务中，KAN标准往往能够匹配甚至超过现有方法，通过去除冗余特征和捕捉非线性交互来提高性能；在回归任务中，基于KAN的得分对于嘈杂和异质数据集表现出强大的性能，并且能够确保变量选择的稳定性和非冗余性。
### Conclusion
研究结果显示，KAN基础的选择器为传统的选择方法提供了一个有力且可解释的替代方案，能够揭示非线性和多变量特征相关性，超越了基于稀疏性或杂质性的度量。进一步的稳定性与冗余分析表明，KAN基础选择器会生成一致的特征子集，避免了不必要的相关性膨胀，从而确保可信赖且非冗余的变量选择。总体而言，该论文证明了KAN基础的特征选择是一个强大的新方法，适用于监督表数据降维。
## 634. `cs.LG` - AV-Lip-Sync+: 利用AV-HuBERT发掘多模态不一致性以检测正脸视频的换脸 [PDF](https://arxiv.org/pdf/2311.02733), [HTML](https://arxiv.org/abs/2311.02733)
### Authors
Sahibzada Adil Shahzad,Ammarah Hashmi,Yan-Tsung Peng,Yu Tsao,Hsin-Min Wang
### Background
多模态换脸（也称为音频-视觉深度假）使得单一模态的深度假检测器难以检测多媒体内容中的伪造。为了防止假宣传和假新闻的传播，及时检测至关重要。通过利用同时利用视听信息的多模态模型才能发现单一模态（即视觉或音频）的损坏。然而，先前的方法主要采用单一模态视频取证，并使用监督预训练进行伪造检测。
### Innovation
本研究提出了一种新的基于多模态半监督学习（SSL）特征提取器的方法，用于利用视听模态之间的不一致性来进行多模态视频伪造检测。本研究使用基于变压器的SSL预训练AV-HuBERT模型来提取视听特征，并使用多尺度时空卷积神经网络捕获视听模态之间的时序相关性。对于AV-HuBERT仅从唇部区域提取视觉特征的问题，本研究还采用另一种基于变压器的视频模型来利用面部特征，并捕捉换脸生成过程中的空间和时间伪影。
### Conclusion
实验结果表明，本模型优于所有已知模型，并在FakeAVCeleb和DeepfakeTIMIT数据集上达到了新的有监督学习性能。
## 635. `cs.LG` - 扩展测试时缩放：上下文、批次和回合3D视角 [PDF](https://arxiv.org/pdf/2511.15738), [HTML](https://arxiv.org/abs/2511.15738)
### Authors
Chao Yu,Qixin Tan,Jiaxuan Gao,Shi Yu,Hong Lu,Xinting Yang,Zelai Xu,Yu Wang,Yi Wu,Eugene Vinitsky
### Background
强化学习（RL）展示了新的缩放效应：测试时缩放。思考模型如R1和o1在测试时间随着上下文长度增加而提高推理准确性。然而，测试时缩放本质上受到基模型上下文长度限制，其长度远小于训练时消耗的令牌数量。
### Innovation
提出了一种多维度测试时缩放统一框架，通过考虑上下文长度缩放、批次缩放和回合缩放三个维度，来扩展测试时推理的容量。提出了3D测试时缩放，集成上下文、批次和回合缩放。实验证明每个维度都能展示测试时缩放效应，但具有限制效应；结合所有三个维度可显著提高具有挑战性的测试平台（包括IOI、IMO和CPHO）的推理性能，并且进一步从人类反馈中受益；并且这种人-机环框架自然扩展到更开放的领域，即体态学习，能够设计类人控制行为。
### Conclusion
研究展示了每个维度在测试时缩放方面的效应具有边界性；结合三个维度显著提升了具有挑战性的测试平台的推理性能，并且从中受益于人类偏好反馈；并且人-机环框架自然适用于更开放的领域，比如体态学习，从而设计出类人控制行为。
## 636. `cs.LG` - 在Wasserstein污染下的最小最大统计估计 [PDF](https://arxiv.org/pdf/2308.01853), [HTML](https://arxiv.org/abs/2308.01853)
### Authors
Patrick Chao,Edgar Dobriban
### Background
在现代统计学习中，污染是一个核心问题，即使是微小但系统的数据点扰动也可能显著改变估计结果。本文研究了在$?ell_q$范数（$q ?in [1, ?infty]$）中的Wasserstein-$r$污染（$r ?ge 1$），其中每个观测值都可能发生有界成本的对抗性扰动，这扩展了经典的Huber污染模型，局限于仅有一部分观测值被任意破坏。
### Innovation
本文发展了在$?ell_q^r$损失下的最小最大理论，研究了独立和联合（协调）污染，并涵盖了位置估计、线性回归和点式非参数密度估计等基本问题。在位置估计和预测的联合污染下，本文获得了精确的最小最大风险，识别了最不利于的污染，并指出样本均值和最小二乘预测器分别是各自的最小最大最优解。
### Conclusion
对于独立污染的位置估计，本文提供了精确的上界和下界，包括当$q=r=2$时，在欧几里得Wasserstein污染情况下的最小最大最优性。对于任何维度下的点式密度估计，本文推导出了最优速率，并且通过核密度估计，关键带宽可能是经典带宽的更大值。我们的结果表明，与Huber污染模型不同，在基于范数的Wasserstein污染情况下，经典估计器可能几乎是最优鲁棒的。
## 637. `cs.LG` - UplinkNet: 实际商用5G独立组网（SA）上行吞吐量预测 [PDF](https://arxiv.org/pdf/2307.12417), [HTML](https://arxiv.org/abs/2307.12417)
### Authors
Kasidis Arunruangsirilert,Jiro Katto
### Background
尽管5G新无线电（NR）网络在上行吞吐量方面取得了显著改善，但这些增益主要依赖于用户设备（UE）连接到高频毫米波（mmWave）频段。随着对上行密集型应用的需求增加，如实时UHD 4K/8K视频流传输和虚拟现实（VR）/增强现实（AR）内容，准确的上行吞吐量预测变得至关重要，以优化用户体验（QoE）。文献指出，现有模型往往难以满足互联网设备（IoT）和低功耗设备的资源限制。
### Innovation
本文提出了一种名为UplinkNet的紧凑型神经网络，用于使用过去吞吐量和通过Android API可用的射频参数预测未来的上行吞吐量。UplinkNet的模型大小限制在约4,000参数，适合IoT和低功耗设备。该网络在来自日本东京和泰国曼谷的商用5G独立组网（SA）网络的真实道路测试数据中进行了训练，覆盖了各种移动条件。UplinkNet使用仅来自Android API的数据进行模型训练，并在未见数据上与其他模型进行了评估。结果显示，UplinkNet的平均预测准确率为98.9%，RMSE为5.22 Mbps，优于所有其他模型，同时保持紧凑的大小和低计算成本。
### Conclusion
UplinkNet有效地解决了上行吞吐量预测的资源限制问题，提供了精确且高效的上行吞吐量预测，特别适合IoT和低功耗设备的应用场景。
## 638. `cs.LG` - 使用神经运算符的环境噪声全波形反演 [PDF](https://arxiv.org/pdf/2503.15013), [HTML](https://arxiv.org/abs/2503.15013)
### Authors
Caifeng Zou,Zachary E. Ross,Robert W. Clayton,Fan-Chi Lin,Kamyar Azizzadenesheli
### Background
地震波传播的数值模拟在研究速度结构和提升地震风险评估方面至关重要，但传统的方法如有限差分法和有限元法计算成本高昂。最近的研究表明，一类新的机器学习模型——神经运算符——与传统方法相比，能够将弹性动力学波动方程的求解速度提升多个数量级。全波形反演特别受益于这种加速计算。神经运算符作为端到端可微运算符，结合自动求导，为全波形反演提供了替代的优化方法，与传统的反演状态法相比，可以利用先进的优化技术，如内置在PyTorch中的先进优化方法，提高优化动力学，从而缓解循环跳过等问题。
### Innovation
这项研究表明，神经运算符首次在实际地震数据集上应用于全波形反演，实现了高效且准确的地震波传播模拟，并且使用先进的优化技术，使反演过程更加灵活和稳定。
### Conclusion
使用神经运算符进行全波形反演的成功应用表明，这是一种有前途的加速地震成像和反演的新方法，未来有望在地震学中得到更广泛的应用。
## 639. `cs.LG` - 基于软实体约束的知识图谱交互式查询回答 [PDF](https://arxiv.org/pdf/2508.13663), [HTML](https://arxiv.org/abs/2508.13663)
### Authors
Daniel Daza,Alberto Bernardi,Luca Costabello,Christophe Gueret,Masoud Mansoury,Michael Cochez,Martijn Schut
### Background
现有方法用于查询回答的知识图谱主要针对那些可以通过直接图遍历找到的答案，但当答案因缺少边而无法直接到达时，它们的效果较差。现有方法主要处理符合一阶逻辑形式化描述的查询，但在实际应用中，许多查询包含内在模糊或依赖于上下文的约束条件，如属性偏好或相关类别偏好。
### Innovation
本文提出了一个处理软约束条件下查询回答的问题，并引入了两种高效的方法来调整查询回答分数，这些方法能够根据软约束调整答案得分，同时保持查询原始答案的排名结构。此外，通过扩展现有的查询回答基准数据集来生成包含软约束条件的数据集。
### Conclusion
实验结果表明，本文提出的方法能够在保留查询回答性能的同时捕捉软约束条件，并且几乎不增加额外的开销。
## 640. `cs.LG` - 统计物理分析下的图神经网络：通过上下文性的随机块模型接近最优性 [PDF](https://arxiv.org/pdf/2503.01361), [HTML](https://arxiv.org/abs/2503.01361)
### Authors
O. Duranthon,L. Zdeborová
### Background
图神经网络（GNNs）设计用于处理与图相关联的数据。尽管它们的应用范围不断扩大，但对其理论理解仍有限。GNNs在进行信息从节点间传递时，可能会遇到节点间距离较大时信息传递受限的问题，这一问题部分由所谓的过度平滑现象引起。论文通过分析深度为多步卷积的图卷积网络（GCNs）的泛化性能，利用复利方法推导该问题的自由能，探讨了在大型深度条件下的Bayes-最优性。研究发现，通过调整GCN架构以避免过度平滑，可以接近Bayes-最优性。
### Innovation
论文通过引入统计物理学中的方法，尤其是使用复利方法推导数据生成模型（通过上下文性的随机块模型）的自由能，提出了一种分析深度卷积神经网络的方法。论文揭示了随着卷积步骤的增加，为了接近Bayes-最优性，需要采用较大深度来优化GCN的结构和性能。研究还使用动态平均场理论（DMFT）框架和约束条件来探讨连续极限下的GCN性能，从而提供了一种研究进一步深层次神经网络的潜在工具。
### Conclusion
通过将统计物理方法应用于GNNs，本文证明了GCN在大型深度条件下的性能可以接近Bayes-最优性，并且提出了一种连续的GCN形式。这种方法不仅为GNNs的改进提供了新的视角，也为更深层次神经网络的分析提供了技术工具。
## 641. `cs.LG` - GLOBE: 基于领域启发架构和对称性的精准且通用PDE代理模型 [PDF](https://arxiv.org/pdf/2511.15856), [HTML](https://arxiv.org/abs/2511.15856)
### Authors
Peter Sharpe
### Background
该研究探讨了如何通过结合边界元素方法和李群对称性机器学习来构建精确且通用的偏微分方程(PDE)近似模型。背景在于当前的物理驱动机器学习方法在工业计算机辅助工程(如流体动力学)中的性能和通用性上存在限制。
### Innovation
论文提出了GLOBE，一种新型神经近似模型，该模型借鉴了边界元素方法和李群对称性的诱导偏置。GLOBE采用直推格林函数样的核函数构建解，并通过多尺度分支和通信超层聚合。该架构在平移、旋转和平行对称性、网格细分不变性以及单位不变性方面表现出色。GLOBE还通过明确的远区场衰减包络稳定了外推，通过边界到边界超层通信调节了远距离耦合，从而确保了全局接收场能尊重物理信息流，即使是对椭圆PDE亦然。
### Conclusion
在AirFRANS任务中，GLOBE实现了显著的精度提升。在“Full”分割中，与数据集的参考基线相比，GLOBE将所有场的均方误差降低了大约200倍，相比于下一个表现最好的模型降低了约50倍。在“Scarce”分割中，GLOBE在速度和压力字段上达到低于Transolver超过100倍的误差降低，在表面压力上降低了超过600倍的误差。定性结果显示出接近壁面的梯度，协调的尾流，并且即使在雷诺数和攻角稍微扩大下也能表现出有限的误差。此外，该模型较为精简（117k参数），并且可以任意点进行推理中的场评估。此外还展示了GLOBE能够使用非封闭网格进行训练和预测的能力，这具有重要的实际意义。这些结果表明，严谨的物理启发和领域引导的诱导偏置可以显著提高基于机器学习的PDE近似模型在工业领域中的精度、泛化能力和实用性。
## 642. `cs.LG` - 预测未来的脑部解剖结构：纵向脑MRI到MRI预测 [PDF](https://arxiv.org/pdf/2511.02558), [HTML](https://arxiv.org/abs/2511.02558)
### Authors
Ali Farki,Elaheh Moradi,Deepika Koundal,Jussi Tohka
### Background
预测未来脑状态从基线磁共振成像（MRI）是神经影像学中的核心挑战，对于研究阿尔茨海默病（AD）等神经退行性疾病具有重要影响。目前大多数方法是预测未来认知评分或临床结果，如从轻度认知障碍转化为痴呆。本文聚焦于纵向MRI图像到图像的预测，能够前瞻性地预测参与者几年后的整个大脑MRI图像，从而内在地建模复杂的、空间分布的神经退行性模式。
### Innovation
本文实施并评估了五种深度学习架构（UNet、U2-Net、UNETR、时间嵌入UNet和ODE-UNet）在两个纵向队列（ADNI和AIBL）上的表现。预测的后续MRI与实际的后续扫描进行直接对比，使用能捕捉全局相似性和局部差异的指标。最佳模型实现了高保真预测，并且所有模型都很好地泛化到独立外部数据集，显示出跨队列的稳健表现。
### Conclusion
我们的研究结果表明，深度学习可以可靠地在体素水平上预测参与者的脑MRI图像，为个体化预后提供了新的机会。
## 643. `cs.LG` - 基于强化学习的物联网水下路由协议 [PDF](https://arxiv.org/pdf/2506.00133), [HTML](https://arxiv.org/abs/2506.00133)
### Authors
Mohammadhossein Homaei,Mehran Tarif,Agustin Di Bartolo,Victor Gonzalez Morales,Mar Avila Vegas
### Background
水下物联网（IoUT）面临着诸如带宽低、延迟高、移动性强以及能量不足等问题。目前，用于陆地网络的路由协议，例如RPL，不适用于水下环境。
### Innovation
提出了一种新的基于强化学习的路由协议——RL-RPL-UA。每个节点都有一个小的RL代理，根据本地数据如链路质量、缓冲区水平、数据包送达比例和剩余能量等因素来选择最佳父节点。RL-RPL-UA能够与所有标准RPL消息兼容，增加了一个动态目标函数，以帮助实时决策。
### Conclusion
Aqua-Sim仿真结果显示，相对于先前的方法，RL-RPL-UA在提高数据包送达率（高达9.2%）、节省能量（每包14.8%）以及延长网络寿命（额外80秒）方面表现出显著优势。因此，该研究提出的方法是一种具有潜力的节能方式，适用于水下网络的数据路由。
## 644. `cs.LG` - LLMs学习推理的复杂网络视角 [PDF](https://arxiv.org/pdf/2509.23629), [HTML](https://arxiv.org/abs/2509.23629)
### Authors
Sihan Hu,Xiansheng Cai,Yuan Huang,Zhiyuan Yao,Linfeng Zhang,Pan Zhang,Youjin Deng,Kun Chen
### Background
本文探讨了使用强化学习和验证性奖励（RLVR）训练大型语言模型（LLM）时出现的一系列独特而令人困惑的行为，包括两阶段的学习曲线、响应长度的V形轨迹以及严重的灾难性遗忘倾向。这些行为的机制尚未得到很好的理解。
### Innovation
本文提出了一种新的理论，认为这些行为是由语义空间中潜在推理图的拓扑演变所驱动的自组织现象，而不是由神经实现细节决定的。通过将一个1.5B参数的LLM与一个最小概念网络模型（CoNet）进行动态同构，追踪因果来源到一个稀疏的概念网络，平均度为2。该几何视角提供了一个统一的物理解释：V形轨迹跟踪从局部技能优化并行到全局网络整合的过程；灾难性遗忘源于关键“主干”边的拓扑断开；策略崩溃则源于在网络边缘节点上积累的连续过渡，导致广泛的探索突然冻结为高奖励的固有轨迹。该理论提出了一种按原则设计的算法“RLVR退火”，通过注入针对性的SFT“加热”步骤来解决该拓扑瓶颈。
### Conclusion
通过将RLVR从黑盒优化转变为可预测的结构自组织过程，本文提供了一种新的物理直觉来解释未来AI系统的涌现推理能力。理论驱动的干预在分布内和分布外基准测试（包括Minerva和AIME）上优于标准的RLVR方法，显示了这一新方法的有效性。
## 645. `cs.LG` - FAR: Function-preserving Attention Replacement for IMC-friendly Inference [PDF](https://arxiv.org/pdf/2505.21535), [HTML](https://arxiv.org/abs/2505.21535)
### Authors
Yuxin Ren,Maxwell D Collins,Miao Hu,Huanrui Yang
### Background
尽管Transformer在现代视觉和语言模型中占据主导地位，但其注意力机制因依赖密集的激活到激活的乘法和非局部的内存访问，而不适合内存计算(IMC)设备，这在基于ReRAM的加速器上导致了显著的延迟和带宽开销。
### Innovation
提出了FAR（保持功能的注意力替换）框架，将预训练的DeiT中的所有注意力机制替换为与IMC数据流本源兼容的序列模块，通过区块蒸馏将自注意力替换为多头双向LSTM架构，同时保留功能等效性并使计算时间缩减至线性时间，同时实现了局部权重重用；进一步对FAR模型进行结构化剪枝，使其能够灵活适应资源受限的IMC阵列，同时保持功能的准确性。
### Conclusion
在DeiT家族的评估中，FAR在减少参数和延迟的情况下，仍可保持与基于注意力模型相当的准确度，并且进一步分析显示，FAR保留了注意力学习的语义令牌关系，提高了计算效率，突显了其在基于IMC的边缘加速器上进行Transformer推理的节能潜力。
## 646. `cs.LG` - 使用频域嵌入的3D高斯点绘制进行宽频RF辐射场建模 [PDF](https://arxiv.org/pdf/2505.20714), [HTML](https://arxiv.org/abs/2505.20714)
### Authors
Zechen Li,Lanqing Yang,Yiheng Bian,Hao Pan,Yongjian Fu,Yezhou Wang,Zhuxi Chen,Yi-Chao Chen,Guangtao Xue
### Background
室内环境中通常存在多个频率范围内的RF信号，包括NB-IoT、Wi-Fi和毫米波。这对于联合部署异构RF系统、跨频段通信和分布式RF感知等实际应用来说，宽带RF建模是必不可少的。虽然3D高斯点绘制（3DGS）技术能够有效地在单一频率下重建RF辐射场，但它们无法模拟任意或未知频率范围内的辐射场。传统的3DGS方法只能在单个频率下建模RF辐射场，而不能涵盖整个宽带范围。因此，提出了一种新型的3DGS算法，用于统一的宽带RF辐射场建模。
### Innovation
本文介绍了一种新型的3DGS算法，通过在每个空间位置利用3D高斯球体并结合频率嵌入的电磁特征网络，实现了在特定3D环境中从稀疏频率样本高效重建任意且未见频率下的RF辐射场。实验结果表明，该模型的结构相似度指数（SSIM）达到0.922，远超最先进的单频3DGS模型的0.863。
### Conclusion
基于多个频率数据训练的模型，能够高效重建大尺度功率角度谱（PAS）数据集中的PAS辐射场，且表现出卓越的性能，超过了现有的基于单频率3DGS的技术。
## 647. `cs.LG` - MOCHA: 多模态物体感知跨架构对齐 [PDF](https://arxiv.org/pdf/2509.14001), [HTML](https://arxiv.org/abs/2509.14001)
### Authors
Elena Camuffo,Francesco Barbato,Mete Ozay,Simone Milani,Umberto Michieli
### Background
个性化物体检测旨在根据少数几个示例适应通用检测器以识别用户特定的实例。轻量级模型在这个场景下往往表现不佳，因为它们的语义先验较弱。而大型的多模态视觉-语言模型（VLMs）尽管具有强大的物体级别理解能力，但在实时或设备端应用中计算成本过于昂贵。为了解决这一矛盾，作者提出了MOCHA框架，该框架将一个冻结的VLM教师的多模态区域级别知识转移到一个轻量级的仅视觉检测器中。
### Innovation
MOCHA是一个蒸馏框架，能够将VLM教师的多模态区域级别知识传递给一个轻量级的仅视觉检测器。该框架通过融合视觉和文本信息的嵌入表示，并利用双重目标损失来引导学生训练，该损失强制进行精确的局部对齐和全局关系一致性。该过程可以在无需修改教师模型或在推理时无需使用文本输入的情况下高效地传递语义信息。实验结果表明，MOCHA在四个严格的少样本基准测试中的性能均优于之前的基线方法，平均提高了10.1%。
### Conclusion
MOCHA在少样本个性化物体检测上表现出色，有效地将多模态视觉和文本知识传递给轻量级的仅视觉检测器，以处理因缺少实例而产生的语义不充分的问题，同时仅需少量的推理成本。
## 648. `cs.LG` - 通过基于物理的强化学习序列模型精细调整实现可持续制冷剂发现 [PDF](https://arxiv.org/pdf/2509.19588), [HTML](https://arxiv.org/abs/2509.19588)
### Authors
Adrien Goldszal,Diego Calanzone,Vincent Taboga,Pierre-Luc Bacon
### Background
当前大多数空调系统使用的制冷剂，如氢氟碳化合物，是强温室气体且正在减量。大规模分子筛选被应用于寻找替代品，但仅约300种制冷剂为人熟知，且在没有实验验证的情况下仅有少数候选物。由于可靠数据的稀缺，纯粹数据驱动的方法效果有限。
### Innovation
提出了Refgen，一种结合机器学习与物理基础归纳偏见的生成管道。Refgen不仅进行了有效分子的微调，还包含了预测关键性质、状态方程、热化学多项式及完整蒸气压缩循环模拟的模型。这些模型使得在热力学约束下进行强化学习微调成为可能，从而在效率、安全性和环境影响上确保一致性，并指导发现过程。通过将物理知识嵌入学习过程，Refgen有效利用了稀缺数据，并使发现超越现知化合物的新制冷剂成为可能。
### Conclusion
通过嵌入物理知识的学习过程，Refgen提高了数据利用率，并实现了在热力学约束下的制冷剂发现，从而实现了可持续制冷剂的发现。
## 649. `cs.LG` - Live-SWE-agent: Can Software Engineering Agents Self-Evolve on the Fly? [PDF](https://arxiv.org/pdf/2511.13646), [HTML](https://arxiv.org/abs/2511.13646)
### Authors
Chunqiu Steven Xia,Zhe Wang,Yan Yang,Yuxiang Wei,Lingming Zhang
### Background
大型语言模型（LLMs）正在重新定义几乎所有行业，包括软件工程。近年来，已经提出了许多LLM代理来解决现实世界中的软件问题。这些软件代理通常配备了一系列编程工具，可以自主决定下一步操作，从而构成完整的解决端到端软件任务的轨迹。尽管具有前景，但它们通常需要专门的设计，且可能仍不完全理想，因为彻底探索整个代理结构空间可能会极其复杂和昂贵。因此，研究人员提出了包括达尔文-哥德尔机器（DGM）等自我改进的软件代理，但这些自我改进的代理需要在特定基准上进行昂贵的离线训练，可能在不同LLM或基准之间泛化表现不佳。
### Innovation
本文提出了一种名为Live-SWE-agent的实时软件代理，它能自主且连续地在运行时自我进化，以解决现实世界中的软件问题。具体而言，Live-SWE-agent是从最基本的代理骨架（例如mini-SWE-agent）开始的，并在解决实际软件问题的过程中自主进化其自己的骨架实现。在广泛研究的SWE-bench Verified基准测试中，Live-SWE-agent在无需测试时扩展的情况下实现了77.4%的解题率，超越了所有现有的软件代理，包括最先进的定制解决方案。此外，Live-SWE-agent在最新的SWE-Bench Pro基准测试中也超越了最先进的手动构建软件代理，实现了最佳已知的解题率45.8%。
### Conclusion
Live-SWE-agent展示了自我改进的软件代理在解决实际软件工程问题方面的潜力，并且能够在运行时自我进化。它提供了高性能的解决方案，超过了以前的方法，证明了其在实际应用中的潜力和价值。
## 650. `cs.LG` - 使用大规模在线核学习估计双向因果效应 [PDF](https://arxiv.org/pdf/2511.05050), [HTML](https://arxiv.org/abs/2511.05050)
### Authors
Masahiro Tanaka
### Background
传统的因果推断通常关注单向效应，而忽视了现实世界现象中常见的双向关系。本研究旨在提出一种可扩展的在线核学习框架，以估计具有相互依赖性和异方差性的系统中的双向因果效应。
### Innovation
该方法结合了基于异方差性的识别、广义矩估计模型的拟似然估计器以及大规模在线核学习。利用随机傅里叶特征近似灵活建模非线性条件均值和方差，并采用自适应在线梯度下降算法以提高计算效率，适用于流式和高维数据。
### Conclusion
广泛的仿真实验表明，所提出的方法在不同的数据生成过程中比单一方程和多项式近似基线方法具有更优的准确性和稳定性，且具有接近线性的计算缩放。该框架将计量经济识别与现代机器学习技术相结合，为大规模因果推断提供了实际可行、可扩展且理论基础的方法，适用于自然/社会科学研究、政策制定、商业和工业应用等领域。
## 651. `cs.SE` - MOOT:一个许多多目标优化任务的仓库 [PDF](https://arxiv.org/pdf/2511.16882), [HTML](https://arxiv.org/abs/2511.16882)
### Authors
Tim Menzies,Tao Chen,Yulong Ye,Kishan Kumar Ganguly,Amirali Rayegan,Srinath Srinivasan,Andre Lustosa
### Background
软件工程师在决策时常常需要在不同的目标之间进行权衡（如更快 vs. 更便宜、更安全 vs. 更易用等）。尽管软件工程研究（SE）已经证明了探索这些目标的技巧，但研究人员仍然在这些权衡中挣扎。同样，工业实践者由于缺乏探索这些权衡所需的工具，交付的产品往往不是最优的。
### Innovation
本文介绍了MOOT，一个从最近的SE研究论文中提取的多目标优化任务仓库。MOOT的任务涵盖了软件配置、云调优、项目健康、过程建模、超参数优化等内容。MOOT的数据能够支持众多新的研究问题。
### Conclusion
MOOT目前已经包含了120多个任务，并以MIT开源许可证形式免费提供（并鼓励社区贡献）。
## 652. `cs.SE` - LLMs在自动化程序修复中的测试过拟合问题 [PDF](https://arxiv.org/pdf/2511.16858), [HTML](https://arxiv.org/abs/2511.16858)
### Authors
Toufique Ahmed,Jatin Ganhotra,Avraham Shinnar,Martin Hirzel
### Background
自动化程序修复已经被证明在生成修复代码时容易出现通过已见测试但无法通过隐藏测试的问题，这被称为测试过拟合。这个问题在大规模语言模型崛起之前就被识别和研究过。研究人员现在实验性地研究测试过拟合在当前仍然是一个问题的程度，通过使用Repository级别的SWE-bench任务。
### Innovation
该研究通过使用Repository级别的SWE-bench任务来实验性地研究大规模语言模型在自动化程序修复中的测试过拟合问题，以确定这一问题在目前是否仍然存在。这为评估自动化程序修复系统的有效性提供了一个新的视角。
### Conclusion
该研究结果表明，在使用大规模语言模型进行自动化程序修复时，测试过拟合仍然是一个问题，这使得修复的代码无法在实际环境中表现得好。因此，需要进一步改进自动化程序修复方法，以减少或避免测试过拟合问题。
## 653. `cs.SE` - 大型语言模型用于自动PRISMA 2020符合性检查 [PDF](https://arxiv.org/pdf/2511.16707), [HTML](https://arxiv.org/abs/2511.16707)
### Authors
Yuki Kataoka,Ryuhei So,Masahiro Banno,Yasushi Tsujimoto,Tomohiro Takayama,Yosuke Yamagishi,Takahiro Tsuge,Norio Yamamoto,Chiaki Suda,Toshi A. Furukawa
### Background
在同行评审过程中，遵循PRISMA 2020指南的依从性评估依然是一大负担。由于缺乏可分享的标准，本研究旨在构建一个基于版权的108个创意思源共享系统评价的基准，评估十种大型语言模型（LLMs）在五种输入格式下的表现。
### Innovation
本研究首次通过使用基于版权的108个创意思源共享系统评价基准，评估了十种大型语言模型在不同输入格式下的PRISMA 2020指南依从性。研究发现了结构化检查清单的提供显著提高了LLM基于自动评估的准确性，尽管人类专家的验证依然必不可少。
### Conclusion
结构化PRISMA 2020检查清单的提供显著改善了基于LLM的PRISMA评估准确性，但人类专家审核依然必要。研究进一步发现高敏感性开放加权模型Qwen3-Max在完整数据集上达到了95.1%的敏感性和49.3%的特异性。
## 654. `cs.LG` - 当偏见伪装成真相：虚假相关性如何在大语言模型中削弱幻觉检测 [PDF](https://arxiv.org/pdf/2511.07318), [HTML](https://arxiv.org/abs/2511.07318)
### Authors
Shaowen Wang,Yiqi Dong,Ruinian Chang,Tansheng Zhu,Yuebo Sun,Kaifeng Lyu,Jian Li
### Background
尽管在大语言模型（LLMs）方面取得了重大进展，但这些模型仍然表现出幻觉现象，即生成看似合理但实际上错误的响应。先前的研究集中于模型的规模和现有检测方法的效果，而本研究关注的是由虚假相关性引起的幻觉，这是一种表面特征（如姓氏）和属性（如国籍）之间的统计上显著但不真实的关联，这种关联存在于训练数据中。
### Innovation
本研究揭示了一种新的幻觉类型，通过系统的合成实验和对最先进开源和私有大语言模型（包括GPT-5）的实际评估，表明现有的基于置信度的过滤和内部状态探针等幻觉检测方法在遇到虚假相关性时根本不起作用。此外，通过理论分析解释了为什么统计偏差从根本上削弱了基于置信度的检测技术。研究结果强调了亟需设计新的方法来解决由虚假相关性引起的幻觉问题。
### Conclusion
本研究发现，现有的幻觉检测方法在存在虚假相关性的情况下根本无效，并且这些统计偏差本质上削弱了基于置信度的检测技术。因此，迫切需要开发新的方法来专门解决由虚假相关性引起的幻觉问题。
## 655. `cs.SE` - 多代理代码验证与复合漏洞检测 [PDF](https://arxiv.org/pdf/2511.16708), [HTML](https://arxiv.org/abs/2511.16708)
### Authors
Shreshth Rajan
### Background
大规模语言模型（LLMs）生成的代码存在大量错误，仅 29.6% 的 SWE-bench ‘解决’ 的补丁有效，62% 的 BaxBench 解决方案存在漏洞，而现有工具仅能检测出 65% 的错误，且有 35% 的误报。因此，需要一种新的方法来更有效地识别代码中的错误。
### Innovation
作者开发了一个名为 CodeX-Verify 的多代理系统，使用四个专门的代理检测不同类型的错误。数学证明显示，综合不同检测模式的代理可以比单一代理发现更多的错误。此外，该系统在检测代码中的多种漏洞时，表现出更高的风险评估能力。与单一代理相比，使用多个代理提高了72.4%的准确性，特别是在两个最佳代理组合下达到了79.3%的准确率。该系统可以在不到200ms的时间内处理300个实际补丁，显示出其实用性。
### Conclusion
通过建立一个使用四个代理的多代理系统，作者成功地提高了代码错误检测的准确性，并证明了使用多个代理的协同工作能够有效发现更多错误，同时提高了速度且无需执行测试。
## 656. `cs.LG` - SoK: Wi-Fi CSI生物特征认证的安全评估：攻击、指标及开放挑战 [PDF](https://arxiv.org/pdf/2511.11381), [HTML](https://arxiv.org/abs/2511.11381)
### Authors
Gioliano de Oliveira Braga,Pedro Henrique dos Santos Rocha,Rafael Pimenta de Mattos Paixão,Giovani Hoff da Costa,Gustavo Cavalcanti Morais,Lourenço Alves Pereira Júnior
### Background
Wi-Fi信道状态信息（CSI）多次被提议作为一种生物认证模态，经常报道其高准确率和操作可行性。然而，该领域缺乏对CSI的安全属性、对抗性鲁棒性和方法论一致性的系统理解。本文通过安全视角对基于CSI的生物认证进行系统性研究，揭示现有工作在传感基础设施、信号表示、特征管道、学习模型和评估方法上的差异，发现系统不一致性，如依赖聚合准确率指标、未充分报告FAR/FRR/EER、缺乏用户特定风险分析等。
### Innovation
本文构建了一个统一的评估框架，通过实证分析揭露这些问题，并使用如每类EER、评分频率计数和基尼系数等安全相关指标揭示传统报告中隐藏的风险集中。这些建立的分析结果指出了具体攻击面，包括重复攻击、几何模仿和环境扰动，展示了方法论选择对脆弱性分布的实际影响。基于这些发现，本文界定了当前CSI生物认证的安全边界，并提出了严格的评估、可重复实验和未来研究方向的指导方针。
### Conclusion
本文为安全界提供了一个结构化、证据驱动的Wi-Fi CSI生物特征认证重新评估，并探讨了其作为认证原语的适用性。
## 657. `cs.SE` - 在可配置软件系统中检测与性能相关的变更 [PDF](https://arxiv.org/pdf/2511.17271), [HTML](https://arxiv.org/abs/2511.17271)
### Authors
Sebastian Böhm,Florian Sattler,Norbert Siegmund,Sven Apel
### Background
软件系统的性能是一个易变的属性，因此需要频繁进行性能剖析以保持对软件系统性能行为的了解。每一版本的重新测量都是一个成本密集型的任务，特别是在存在配置可调性的情况下，需要测量多种配置来获得全面的画面。配置采样是控制测量成本的常用方法，但它不能保证完备性，可能会遗漏性能倒退，尤其是当这些倒退仅影响少数配置时。
### Innovation
提出了一种名为ConfFLARE的方法：通过识别数据流与性能相关代码的交互来估计变更对性能的影响，并提取参与此类交互的软件功能。基于这些特征，可以选取相关配置的子集，专注于性能剖析努力。
### Conclusion
在对合成和真实软件系统的研究中，ConfFLARE几乎在所有情况下都能正确检测出性能倒退，在98%的情况下识别出相关特征，对于合成软件系统，平均减少79%的配置测试数量，对于真实世界回归情景，平均减少70%的配置测试数量，从而节省了大量性能测试时间。
## 658. `cs.SE` - UI自动化测试框架中的能源效率差异 [PDF](https://arxiv.org/pdf/2511.17303), [HTML](https://arxiv.org/abs/2511.17303)
### Authors
Timmie M. R. Lagermann(1),Kristina Sophia Carter(1),Su Mei Gwen Ho(1),Luís Cruz(2),Kerstin Eder(3),Maja H. Kirkeby(1) ((1) Roskilde University, (2) Delft University of Technology, (3) University of Bristol)
### Background
本文旨在探讨四种Web用户界面（UI）自动化测试框架在执行相同操作时的能源消耗情况，以确定是否存在可以用来指导能源优化的规律。研究通过在控制的客户端-服务器环境中进行实验，使用外部电量计进行实时功率测量，分别对刷新、各类点击、复选框、拖拽、输入文本、滚动等操作进行35次重复测试。
### Innovation
研究表明，不同操作在不同框架下的能源消耗差异显著，最高可达六倍之多。Puppeteer在左键点击、右键点击、双击、复选框和输入文本方面表现最为节能；Selenium在页面刷新和滚动时表现更佳；Nightwatch则通常是最不节能的。这表明，提供UI自动化测试框架的能源消耗透明度能够让开发者在测试特定UI操作时做出更加明智和节能的决策。
### Conclusion
通过对四种UI自动测试框架的全面能源消耗分析，提出开发者可以利用这些信息进行能源感知的测试设计，从而在不影响测试准确性的同时降低能源消耗。研究结果表明，选择最节能的框架可以显著减少整体能耗，对可持续性节能具有重要意义。
## 659. `cs.SE` - Agentic Program Verification [PDF](https://arxiv.org/pdf/2511.17330), [HTML](https://arxiv.org/abs/2511.17330)
### Authors
Haoxin Tu,Huan Zhao,Yahui Song,Mehtab Zafar,Ruijie Meng,Abhik Roychoudhury
### Background
自动生成的代码正在受到广泛关注，得益于大型语言模型（LLMs）的使用。AlphaProof项目还展示了使用AI进行一般数学推理的可能性。通过一般数学推理可以进行程序（软件）的推理，但通常更加结构化和丰富。这为使用AI代理来验证由AI生成的大量代码提供了可能。
### Innovation
本文介绍了一种名为AutoRocq的第一代LLM代理，它能够进行程序验证。与以往依赖于LLMs对证明示例进行大量训练的工作不同，我们的代理是一种边学边用的方法，并通过迭代改进证明的过程。此过程通过证明代理与Rocq定理证明者进行通信，获取额外上下文和反馈。最终通过Rocq定理证明者验证了迭代的结果。这种自主协作方式促进了证明搜索和证明树结构决策。
### Conclusion
在SV-COMP基准测试和Linux内核模块上的实验评估表明，我们的证明代理具有实现自动程序验证的潜力。随着代码生成自动化变得更加普遍，我们提出可以将我们的证明代理与AI编码代理集成，以实现生成和验证循环，从而更接近可信自动编程的愿景。
## 660. `cs.SE` - SlsReuse：LLM驱动的无服务器函数重用 [PDF](https://arxiv.org/pdf/2511.17262), [HTML](https://arxiv.org/abs/2511.17262)
### Authors
Jinfeng Wen,Yuehan Sun
### Background
无服务器计算作为一种流行的技术，近年来迅速发展。它允许开发者无需管理基础设施即可实现函数级别的任务。虽然这降低了运维开销，但也给新手开发者带来了挑战。开发函数时，他们需要适应多种平台特定的编程风格，这使得过程既耗时又容易出错。函数重用被认为是解决这些问题的一种有希望的途径，但是，在无服务器计算领域缺乏专门的函数推荐方法。现有的传统技术方法对此问题的解决仍不足以跨越任务描述和不同函数实现之间的语义差距。随着大规模预训练语言模型（LLMs）的进步，这为通过将开发者需求与函数语义对齐来填补这一差距提供了可能性。
### Innovation
本文提出了SlsReuse框架，这是第一个利用LLM驱动的无服务器函数重用框架。SlsReuse首先构建了一个可重用函数库，作为基础知识库。然后，通过有效的提示工程和少量提示，学习了异构函数的一致语义增强表示，捕捉到了隐含的代码意图、目标平台、编程语言和云服务。最后，对于自然语言任务查询，SlsReuse执行了意图感知的发现，并结合多级修剪策略和相似性匹配。基于最具有代表性的LLM之一ChatGPT-4o，SlsReuse在110个任务查询的定制数据集上进行评估，实现了91.20%的Recall@10，相比现有的最先进基线超过24.53个百分点。
### Conclusion
SlsReuse框架是第一个使用LLM驱动的无服务器函数重用框架。通过构建可重用的函数库、学习异构函数的一致语义增强表示以及利用LLM进行意图感知的发现和相似性匹配，SlsReuse成功实现了对新手开发者面临挑战的解决。该框架在自然语言任务查询中展现出高精度，并且相比现有的最先进基线有着显著的改进。
## 661. `cs.LG` - SALT: 在链式思考中引导激活以实现无泄漏思维 [PDF](https://arxiv.org/pdf/2511.07772), [HTML](https://arxiv.org/abs/2511.07772)
### Authors
Shourya Batra,Pierce Tillman,Samarth Gaggar,Shashank Kesineni,Kevin Zhu,Sunishchal Dev,Ashwinee Panda,Vasu Sharma,Maheep Chaudhary
### Background
随着大规模语言模型（LLMs）演变为能够访问敏感用户数据的个人助手，它们面临一个关键的隐私挑战：尽管以往的工作已经解决了输出级别的隐私问题，但最新发现表明，LLMs 的内部推理过程会泄露私人信息，违反了上下文隐私预期。这些泄露发生在模型无意中在其推理跟踪中暴露敏感细节时，即使最终输出看似安全。挑战在于防止这种泄露而不影响模型的推理能力，需要在隐私和实用性之间取得微妙的平衡。
### Innovation
我们提出了指导激活以实现无泄漏思维（SALT），一种轻量级的测试时间干预方法，通过在隐态中注入目标导向向量，来减轻模型链式思考（CoT）中的隐私泄露。我们确定了导致这一行为的高泄露层。通过在多个 LLMs 上进行实验，我们证明了 SALT 可实现 QwQ-32B 上的 CPT 减少 18.2%，Llama-3.1-8B 上的 CPT 减少 17.9%，以及 Deepseek 在 AirGapAgent-R 上的 CPT 减少 31.2%，同时保持类似的任务性能和实用性。
### Conclusion
我们的工作将 SALT 确立为推理能力语言模型测试时间隐私保护的实用方法，提供了一条实现基于 LL consciousness 的个人代理更安全部署的途径。
## 662. `cs.SE` - UI-CUBE：超越任务准确性的企业级计算机使用代理基准测试到操作可靠性 [PDF](https://arxiv.org/pdf/2511.17131), [HTML](https://arxiv.org/abs/2511.17131)
### Authors
Horia Cristescu,Charles Park,Trong Canh Nguyen,Sergiu Talmacel,Alexandru-Gabriel Ilie,Stefan Adam
### Background
当前的计算机使用代理（CUA）基准测试虽然能有效地衡量任务完成情况，但对企业的部署准备度评估有限，过于强调对生产系统的功能正确性，而忽视了所需的运营可靠性。这些基准测试关注的是CUA能否正常运行，而不是它们在真实环境下是否足够可靠。
### Innovation
UI-CUBE（UiPath计算机使用基准测试）是一个系统性的基准测试，包含226个任务，其中涵盖了两个难度级别，旨在揭示当前CUA中的基本架构限制。它不仅仅针对简单的用户界面交互，还涵盖复杂的流程任务和企业应用场景，进行了系统的用户界面变体覆盖、多分辨率测试，并通过应用程序状态自动验证任务是否成功。
### Conclusion
UI-CUBE揭示了当前CUAs在简单任务上可以达到68-87%的人类性能，但在复杂工作流中仅能达到15-32%的人类性能，显示出这些代理在内存管理、层级规划和状态协调方面的根本性架构限制而非逐步的技术差距。这种不连续性能模式适用于没有先验应用程序经验的人类评估者，复杂任务的成功率仅达61.2%。这表明CUAs在非简化任务中的可靠性仍需进一步提高，UI-CUBE作为企业准备诊断工具，有助于发现CUA在执行复杂、多步骤的企业流程时的局限性，从而指导未来的开发工作。
## 663. `cs.SE` - NALA_MAINZ在BLP-2025任务2中的多智能体方法：孟加拉语指令到Python代码生成 [PDF](https://arxiv.org/pdf/2511.16787), [HTML](https://arxiv.org/abs/2511.16787)
### Authors
Hossain Shaikh Saadi,Faria Alam,Mario Sanz-Guerrero,Minh Duc Bui,Manuel Mager,Katharina von der Wense
### Background
该论文讨论了JGU Mainz团队在BLP-2025共享任务中的代码生成系统，该系统针对孟加拉语指令进行编程任务。
### Innovation
该论文提出了一种基于多智能体的管道，首先由代码生成代理从输入指令生成初始解决方案。候选程序随后执行所提供的单元测试（类似于pytest风格的断言）。只有失败的情况会被转发给调试代理，该代理重新运行测试，提取错误跟踪，并依据错误信息、当前程序和相关测试案例生成修订的解决方案。
### Conclusion
利用这种方法，该提交在共享任务中获得了第一的位置，成绩为$Pass@1$得分95.4。同时，他们也公开了他们的代码。
## 664. `cs.SE` - ReVul-CoT：借助检索增强生成和链式思考提示实现有效的软件漏洞评估 [PDF](https://arxiv.org/pdf/2511.17027), [HTML](https://arxiv.org/abs/2511.17027)
### Authors
Zhijie Chen,Xiang Chen,Ziming Li,Jiacheng Xue,Chaoyang Gao
### Background
软件漏洞评估（SVA）在评估和排名软件系统中的漏洞以确保其安全性和可靠性方面发挥着重要作用。尽管大型语言模型（LLMs）在SVA领域展现了显著的潜力，但仍面临两个主要限制。首先，大多数LLMs是基于通用语料库进行训练的，缺乏特定领域的知识，这使得它们在有效的SVA中显得不足。其次，它们倾向于依赖简单的模式匹配而非深入的上下文推理，这使得它们难以全面理解复杂的代码语义及其安全影响。
### Innovation
为了缓解上述限制，作者提出了一种名为ReVul-CoT的新颖框架，该框架结合了检索增强生成（RAG）与链式思考（COT）提示。ReVul-CoT中，RAG模块可以从构建的本地知识库中动态检索上下文相关的信息，该知识库综合了权威来源（如NVD和CWE）的漏洞数据，以及相应的代码片段和描述信息。基于DeepSeek-V3.1，COT提示引导LLM进行逐步推理，评估利用可能性、影响范围及其相关因素。实验结果表明，ReVul-CoT在准确率、F1分数和MCC等方面显著优于最先进的SVA基线，分别提高了10.43%、15.86%和16.50%。进一步的消融研究验证了动态检索、知识整合以及基于COT的推理在提升SVA中的贡献。
### Conclusion
我们的结果表明，结合RAG与COT提示显著增强了基于LLM的SVA，指出了未来研究的潜在方向。
## 665. `cs.SE` - CREST: 基于特定故障报告指标提高故障处理过程解释性和有效性的方法 [PDF](https://arxiv.org/pdf/2511.17417), [HTML](https://arxiv.org/abs/2511.17417)
### Authors
Soroush Javdan,Pragash Krishnamoorthy,Olga Baysal
### Background
通信行业的迅速发展对维护网络可靠性和软件可维护性提出了更高的要求，需要高效的故障处理流程。Ericsson的故障报告（Trouble Reports, TR）详细记录了生产系统中的问题，对于及时解决软件故障至关重要。然而，TR数据的复杂性和多样性使得检索系统难以有效进行故障报告的检索。
### Innovation
研究基于先前Ericsson的工作，采用了两阶段的工作流，通过初始检索（Initial Retrieval, IR）和重排（Re-Ranking, RR）阶段，进一步探索不同的TR观察指标及其对检索模型性能的影响。提出了CREST（Criteria-specific Retrieval via Ensemble of Specialized TR models，基于特定指标的通过专门模型的集合实现的检索方法），利用针对不同TR领域的专业化模型，提高检索效果和可解释性，从而加速故障解决和软件维护。
### Conclusion
实验结果表明，基于特定指标的方法在关键评估指标上显著优于单一模型方法，强调了所有目标指标在优化检索系统性能中的重要性。
## 666. `cs.SE` - Live-SWE-agent: 软件工程代理能否实时自我进化？ [PDF](https://arxiv.org/pdf/2511.13646), [HTML](https://arxiv.org/abs/2511.13646)
### Authors
Chunqiu Steven Xia,Zhe Wang,Yan Yang,Yuxiang Wei,Lingming Zhang
### Background
大型语言模型（LLMs）正在重新定义包括软件工程在内的几乎所有行业。近年来，许多基于LLM的代理被提出以解决实际的软件问题。这些软件代理通常配备了一套编程工具，并能够自主决定下一步行动以完成整个软件任务的解决过程。尽管这些代理很有前景，但它们通常需要专门设计，并且可能仍然不完善，因为完全探索代理架构设计空间将是非常具有挑战性和昂贵的。
### Innovation
本文提出了Live-SWE-agent，这是第一个可以在解决实际软件问题时自主且连续在运行时自我进化的软件代理。Live-SWE-agent从最基本的代理框架开始（例如仅具有bash工具访问权限的mini-SWE-agent），并在解决问题的过程中自主进化其架构实现。实验结果显示，Live-SWE-agent在广泛研究的SWE-bench Verified基准测试中实现了77.4%的解题率，优于所有现有软件代理，甚至是最佳的专有解决方案。此外，Live-SWE-agent在SWE-Bench Pro基准测试中也优于最新的手动构建的顶级软件代理，实现了最佳的解题率45.8%。
### Conclusion
本文展示了Live-SWE-agent在解决实际软件问题时的自主和连续自我进化的可能性。相较于现有的LLM代理，它在多个基准测试中表现出更高的解决率，证实了其在软件工程代理领域的创新进步。
## 667. `cs.SE` - 基于ur_rtde的Universal Robots协作 manipulators的ROS2接口 [PDF](https://arxiv.org/pdf/2511.17237), [HTML](https://arxiv.org/abs/2511.17237)
### Authors
Alessio Saccuti,Riccardo Monica,Jacopo Aleotti
### Background
UR机器人 manipulators在工业自动化中的应用日益广泛，需要与ROS2这样的机器人操作系统更好地整合。因此，开发一个基于ur_rtde库的ROS2驱动程序，以提供更多高阶命令支持，提高其在不同应用中的灵活性。
### Innovation
提出了一种新型的ROS2驱动程序，该程序基于ur_rtde C++库，旨在成为一个灵活的解决方案，适用于广泛的应用。该驱动程序暴露了Universal Robots URScripts的高级命令，并通过插件系统可以添加自定义命令。实现了多个命令，包括基于航点路径的运动执行。
### Conclusion
该驱动程序已作为开源程序发布，可以进一步扩展和优化，提高UR机器人在各种工业自动化任务中的性能和适应性。
## 668. `cs.SE` - 使用多智能体强化学习的LLM协作 [PDF](https://arxiv.org/pdf/2508.04652), [HTML](https://arxiv.org/abs/2508.04652)
### Authors
Shuo Liu,Tianle Chen,Zeyu Liang,Xueguang Lyu,Christopher Amato
### Background
过去在多智能体系统（MAS）中有大量的工作用于建模和解决多智能体交互的问题。然而，大多数语言模型（LLMs）是独立预训练的，并未针对协调进行优化。现有的LLM微调框架依赖于个体奖励，这需要为每个智能体设计复杂的奖励机制，从而促进合作。
### Innovation
本文将LLM协作建模为协同多智能体强化学习（MARL）问题，并开发了一个多智能体、多回合的算法——Multi-Agent Group Relative Policy Optimization（MAGRPO），通过结合现有的RL方法以及MARL技术，可有效解决智能体间的合作问题。实验显示，使用MAGRPO微调的MAS能够高效地生成高质量的响应。
### Conclusion
本文的方法为其他MARL方法在LLM中的应用打开了新的大门，并突显了相关挑战。我们的代码可在[此处](https://github.com/example)获取。
## 669. `cs.SE` - 探索科学债务：利用AI进行科学软件中自我承认的技术债务识别 [PDF](https://arxiv.org/pdf/2511.17368), [HTML](https://arxiv.org/abs/2511.17368)
### Authors
Eric L. Melin,Ahmed Musa Awon,Nasir U. Eisty,Neil A. Ernst,Shurui Zhou
### Background
在科学软件（SSW）领域，由于其快速的创新和紧密的协作特性，自我承认的技术债务（SATD）不仅普遍而且具有重大影响。研究依赖于准确和可重复的结果，累积的SATD可能会威胁到科学发现的基础。然而，由于SATD与SSW之间的关系尚未充分研究，因此如何在这一关键领域管理SATD存在重要知识空白。
### Innovation
本研究探索了科学软件仓库中的SATD，比较了科学和通用目的开源软件中的SATD，并评估了基 transformer 模型进行SATD识别。研究分析了多领域和多语言的27个科学和通用目的软件仓库中的SATD，对67,066个带标签的代码注释进行了10个基于transformer的模型（100M-7B参数）的调整和比较。结果发现，科学软件比通用软件含有的科学债务高9.25倍，SATD高4.93倍，这主要由于复杂的计算、领域约束和不断变化的研究需求。进一步地，研究的最佳模型优于现有模型。
### Conclusion
本研究揭示了科学软件中的SATD与通用软件的不同之处，揭示了其对质量和科学有效性的影响。通过识别这些挑战，开发者和研究人员可以采用更聪明的策略来管理债务并保护科学发现的完整性。
## 670. `cs.SE` - LLM-Agent-UMF: 基于LLM的代理统一建模框架，用于无缝设计多主动/被动核心代理架构 [PDF](https://arxiv.org/pdf/2409.11393), [HTML](https://arxiv.org/abs/2409.11393)
### Authors
Amine Ben Hassouna,Hana Chaari,Ines Belhaj
### Background
在大量数据从多种来源收集和处理的时代，对能够智能融合和分析信息的复杂AI系统的市场需求正在增长。然而，现有的工具整合和提升多款先进技术通常缺乏统一的软件架构，导致模块化不足和术语不一致等问题。
### Innovation
本文提出了一个新型的基于LLM的代理统一建模框架（LLM-Agent-UMF），它从功能和软件架构的角度明确了代理开发的基础，并通过架构权衡与风险管理框架（ATRAF）进行了开发和评估。该框架重点区分了LLM、工具和核心代理之间的不同组件，后者在之前的文献中常被忽视。通过核心代理的主动性和被动性分类，提出了多种组合独特代理特性的多核心代理架构，以更高效地处理复杂任务。
### Conclusion
通过将其应用于十三款先进的代理，并证明它与这些代理的功能一致，同时澄清了以往被忽视的架构方面，本文还详细评估了五种框架变体，通过设计结合了先进代理特性的新代理架构来实现特定目标。
## 671. `cs.SE` - CodeWiki：评估AI生成大规模代码库系统性文档的能力 [PDF](https://arxiv.org/pdf/2510.24428), [HTML](https://arxiv.org/abs/2510.24428)
### Authors
Anh Nguyen Hoang,Minh Le-Anh,Bach Le,Nghi D. Q. Bui
### Background
在大面积且不断演化的代码库中，自动生成具有整体性和架构感知性的文档，涵盖功能之间、跨文件、跨模块及系统级别的交互仍是一个开放的挑战。全面的文档对于软件长期维护和协作至关重要，然而当前的自动化工具仍无法准确建模现实世界软件系统的丰富语义依赖和架构结构。
### Innovation
CodeWiki 提出三个关键创新：(i) 多粒度层次分解，保留架构上下文；(ii) 递归多代理处理与动态任务委托，以提高生成的可扩展性；(iii) 多模态综合，将文本描述与架构图、数据流表示等视觉元素相结合。此外，还引入了一个全面的基准测试CodeWikiBench，包含多维度评估标准和基于LLM的评估协议。
### Conclusion
实验结果显示，CodeWiki 的自定义模型在这方面达到了68.79%的评分，这比商业封闭源代码的 DeepWiki 基线（64.06%）高出了4.73%，特别是在高级脚本语言方面表现优异，提高了10.47%。为促进未来的研究和社区采用，CodeWiki已被开源。
## 672. `cs.SE` - 患者为中心的区块链框架：安全电子健康记录管理与存储访问控制解耦 [PDF](https://arxiv.org/pdf/2511.17464), [HTML](https://arxiv.org/abs/2511.17464)
### Authors
Tanzim Hossain Romel,Kawshik Kumar Paul,Tanberul Islam Ruhan,Maisha Rahman Mim,Abu Sayed Md. Latiful Hoque
### Background
本研究旨在解决电子健康记录（EHR）共享中的隐私和安全问题，特别是在数据存储和访问控制之间的分离方面。目前的EHR系统中，数据存储与授权和审计紧密集成，缺乏灵活性。因此，需要一个简洁、灵活且安全的解决方案来改善现有的EHR系统。
### Innovation
提出了一种以患者为中心的架构，将内容存储与授权和审计分离。利用加密的FHIR资源存储在链下，并在区块链上记录加密承诺和患者签名的时间限制授权。通过公钥封装分发密钥，使存储提供商保持好奇心但保持诚实，从而保护用户隐私。同时，正式定义了安全目标，并提供了基于Solidity的单个患者合同的参考实现。
### Conclusion
该研究通过区块链和加密手段大幅减少了访问控制上的链上成本，并降低了整体末端访问延迟。对于敏感性的临床数据而言，这种技术实现了患者隐私保护的同时保持足够的安全性。现有的链上成本平均为78,000 gas，而端到端访问延迟平均也为0.7-1.4秒。L2部署方式进一步降低了费用，但数据可用性成本成为主要负担。该研究还讨论了元数据隐私、密钥注册需求以及符合HIPAA和GDPR监管的考虑，展示了恢复患者控制的实用途径。
## 673. `cs.SE` - DiffTester: 通过重复模式加速扩散LLMs的单元测试生成 [PDF](https://arxiv.org/pdf/2509.24975), [HTML](https://arxiv.org/abs/2509.24975)
### Authors
Lekang Yang,Yuetong Liu,Yitong Zhang,Jia Li
### Background
软件开发依赖于广泛的单元测试，因此自动单元测试生成（UTG）的效率变得尤为重要。然而，现有的大多数语言模型（LLMs）在每次前向传输中以单个标记生成测试用例，这导致了不高效的UTG。最近，扩散LLMs（dLLMs）的出现，提供了并行生成的潜力并展示了高效的UTG的强大潜力。尽管如此，它们在UTG中的应用仍受到效率和测试质量问题之间的明确权衡制约。通过在每个步骤生成更多的标记，通常会导致测试用例质量的急剧下降。
### Innovation
DiffTester是一种加速扩散LLMs单元测试生成的专用框架。其关键思想在于相同的焦点方法经常具有重复的结构模式，通过动态识别生成过程中的这些常见模式进行抽象语法树分析，DiffTester能在每个步骤增加生成的标记数量而不牺牲输出质量。为进一步测试，我们扩展了仅限于Python的原始TestEval基准，引入了Java和C++等其他编程语言，结果显示DiffTester在保持测试覆盖率的同时提供显著加速，并且能在不同的dLLMs和编程语言上很好地泛化。
### Conclusion
DiffTester为扩展的基准上的三种原始模型提供了实践和可扩展的解决方案，用于软件开发中的高效UTG。代码和数据已公开提供。
## 674. `cs.SE` - LLM生成代码中的测度、解释与缓解度量的因果视角 [PDF](https://arxiv.org/pdf/2511.15817), [HTML](https://arxiv.org/abs/2511.15817)
### Authors
Alejandro Velasco,Daniel Rodriguez-Cardenas,Dipin Khati,David N. Palacio,Luftar Rahman Alif,Denys Poshyvanyk
### Background
近年来，大规模语言模型（LLMs）的发展加速了其在软件工程中的应用。然而，人们对这些模型生成的代码的结构质量仍有担忧，尤其是它们频繁复制不良编码实践，引入了代码异味（即妨碍代码可读性、可维护性或设计完整性的模式）。虽然已有研究探索了异味的检测或修复，但对于这类问题在生成代码中如何及何时出现，我们仍缺乏清晰的理解。
### Innovation
本文通过系统地测量、解释和缓解LLM生成代码中的异味倾向填补了这一空白。构建了预测概率分数（PSC），这是一种估计生成特定类型异味可能性的概率度量，并证明了其作为结构质量信号的稳健性。利用PSC作为因果分析工具，本文揭示了生成策略、模型规模、模型架构和提示形式对生成代码的结构特性的影响。研究结果表明，提示设计和架构选择在异味倾向中起着决定性作用，并促使实际的缓解策略以降低其发生。进一步的用户研究证明了PSC有助于解释模型行为、评估代码质量，提供了证据表明异味倾向信号可以支持人类判断。
### Conclusion
本文的工作为在LLM代码评估和部署中整合质量意识评估奠定了基础。
## 675. `cs.SE` - CATCODER：利用相关代码和类型上下文的仓库级别代码生成 [PDF](https://arxiv.org/pdf/2406.03283), [HTML](https://arxiv.org/abs/2406.03283)
### Authors
Zhiyuan Pan,Xing Hu,Xin Xia,Xiaohu Yang
### Background
大型语言模型（LLMs）在代码生成任务中表现出色，但在仓库级别进行代码生成时，由于需要利用分布在多个文件中的信息，面临着独特挑战。这不仅要求具备一般性的、上下文无关的知识，还需要掌握具体的、依赖于上下文的知识。尽管LLMs广泛应用于上下文中较难获取一般性的部分，但现有的检索方法有时表现不佳，难以获取更广泛和深入的仓库上下文信息。
### Innovation
提出了一种名为CatCoder的新代码生成框架，专门设计用于静态类型编程语言。CatCoder通过集成相关代码和类型上下文增强仓库级别代码生成。具体而言，它利用静态分析器提取类型依赖关系，并将其与检索到的代码合并，生成更全面的提示，供LLMs使用。为了验证CatCoder的效果，构建了包含199个Java任务和90个Rust任务的基准测试集。结果显示，与基本的RepoCoder基准相比，CatCoder在编译@k和通过@k评分方面分别提高了14.44%和17.35%。此外，还在各种LLMs中评估了CatCoder的一般化能力，包括专门的代码模型和通用型模型，发现性能提升一致，印证了CatCoder的实际应用潜力。同时，研究还通过在大型开源仓库中评估CatCoder的时间消耗，展示了其可扩展性。
### Conclusion
CatCoder在仓库级别代码生成中通过集成相关代码和类型上下文显著提升了性能，尤其是在包含多文件信息利用的环境中。同时，不论是针对专用代码模型还是通用型模型，都可以观察到性能提升的一致性。此外，CatCoder在大规模开源仓库中的高效性也得到了验证，这为未来的应用提供了强大的基础。
## 676. `cs.SE` - 超越代码相似性：LLM生成的Smart Contracts的可信性、效率和复杂性的基准测试 [PDF](https://arxiv.org/pdf/2511.16224), [HTML](https://arxiv.org/abs/2511.16224)
### Authors
Francesco Salzano,Simone Scalabrino,Rocco Oliveto,Remo Pareschi
### Background
智能合约是区块链生态系统中的关键组件，Solidity 是主导的编程语言。尽管大型语言模型（LLMs）在通用代码生成中表现出色，但智能合约的特殊约束，如气体消耗、安全性和确定性，使得LLM生成的Solidity代码的可靠性成为一个开放问题。现有的研究缺乏对这些关键的功能性和非功能性属性进行全面的评估。为了填补这一空白，本研究通过基准测试四种最先进的模型，在零样本和检索增强生成的不同设置下对500个真实世界的函数进行了评估。
### Innovation
本研究通过采用代码相似度度量、语义嵌入、自动化测试执行、气体分析以及认知和环形复杂性分析等多维度评估方法，对LLM生成的智能合约的可信性、效率和复杂性进行了基准测试，揭示了LLM生成的代码与真实合同在语义上的相似性与功能上的合理性之间的差距。此外，研究发现在检索增强生成的设置下，生成的智能合约在功能正确性和效率上有了显著提升。
### Conclusion
研究结果表明，虽然LLM生成的代码在语义上与真实合同高度相似，但在功能正确性方面仍然较低，仅有20%到26%的零样本生成的代码在测试中与真实实现行为完全一致。生成的代码通常更加简单，复杂性和气体消耗更低，部分原因是省略了验证逻辑。检索增强生成显著提高了性能，使得功能正确性的提升高达45%，生成的代码更为简洁和高效。总体而言，本研究揭示了LLM生成的Smart Contracts在语义相似性和功能性之间的巨大差距。虽然检索增强生成显著提高了性能，但实现稳固、生产级别的代码生成仍面临重大挑战，需要专业人员的仔细验证。
