# 20260102
[![Subscribe_Visitors](https://visitor-badge.laobi.icu/badge?page_id=nituchao.latest_arxiv_analyze_ai_rss)](https://github.com/nituchao/latest_arxiv_analyze_ai)

## 1. `cs.AI` - LoongFlow：基于认知规划-执行-总结范式的定向进化搜索 [PDF](https://arxiv.org/pdf/2512.24077), [HTML](https://arxiv.org/abs/2512.24077)
### Authors
Chunhui Wan,Xunan Dai,Zhuo Wang,Minglei Li,Yanpeng Wang,Yinan Mao,Yu Lan,Zhiwen Xiao
### Background
传统的进化方法受限于缺乏结构化的推理，对于高维代码空间中的早期收敛和探索效率不足等问题束手无策。
### Innovation
引入了LoongFlow自适应演化代理框架，该框架通过将大型语言模型（LLMs）融入认知“规划-执行-总结”（PES）范式，实现了最先进的解决方案质量，减少了计算成本。同时，通过结合多岛模型、MAP-Elites以及自适应玻耳兹曼选择，提出了一种混合进化记忆系统，理论上实现了探索与利用之间的平衡，并防止优化停滞。
### Conclusion
LoongFlow在算法发现通用代理和机器学习代理方面展现出了卓越的进化效率，发现更优解决方案，并在AlphaEvolve基准测试和Kaggle竞赛中较领先方法提高了高达60%的性能。LoongFlow在自主科学发现方面迈出了重大一步，实现了用较低的计算开销生成专家级别的解决方案。
## 2. `cs.AI` - 钻孔和虚构测试（DDFT）：一种评估语言模型认识论稳健性的协议 [PDF](https://arxiv.org/pdf/2512.23850), [HTML](https://arxiv.org/abs/2512.23850)
### Authors
Rahul Baxi
### Background
当前的语言模型评估主要衡量模型在理想条件下的知识掌握情况，而非其在现实压力下的稳健性。静态基准如MMLU和TruthfulQA无法区分缺乏知识的模型和在信息降级或对手探测弱点时验证机制崩溃的模型。因此，需要一种新的方法来衡量模型在逐步语义压缩和对手伪造下的事实准确性。
### Innovation
提出了钻孔和虚构测试（DDFT）协议，用于评估模型的认识论稳健性，即模型在逐步语义压缩和对手伪造下的事实准确性保持能力。设计了包含语义系统和知识验证器的双系统认知模型。通过评估9个前沿模型在8个知识领域的5个压缩级别下的性能，发现认识论稳健性与传统设计范式无关，而是由训练方法和与当前方法不同的验证机制决定。发现尽管大型模型仍具有脆弱性，但小型模型可以实现稳健性能。
### Conclusion
DDFT框架为理论基础和实践工具提供了评估语言模型认识论稳健性的方法，尤其是在关键应用部署前。
## 3. `cs.AI` - SCP：通过全球自主科研代理网络加速发现 [PDF](https://arxiv.org/pdf/2512.24189), [HTML](https://arxiv.org/abs/2512.24189)
### Authors
Yankai Jiang,Wenjie Lou,Lilong Wang,Zhenyu Tang,Shiyang Feng,Jiaxuan Lu,Haoran Sun,Yaning Pan,Shuang Gu,Haoyang Su,Feng Liu,Wangxu Wei,Pan Tan,Dongzhan Zhou,Fenghua Ling,Cheng Tan,Bo Zhang,Xiaosong Wang,Lei Bai,Bowen Zhou
### Background
科学研究日益复杂，涉及多种软件工具、模型、数据集以及物理仪器，这导致了资源发现、调用和组合方面的挑战，尤其是在不同的平台和机构之间。构建统一的协议标准能够简化这些过程，促进大规模、多机构之间的科学研究合作，并增强实验的可复现性。
### Innovation
SCP（Science Context Protocol）提供了一种开放源的标准化协议，旨在通过全球网络中的自主科学代理加速发现。SCP 建立在两个基础支柱上：统一资源集成和协调的实验生命周期管理。前者提供了统一的规范来描述和调用科学资源，实现跨平台的无缝发现和组合。后者提供了一个安全的服务架构，包括中心化的SCP枢纽和联邦的SCP服务器，管理实验的全生命周期，确保细粒度的身份验证和授权，并协调可追溯的端到端工作流。
### Conclusion
SCP提供了一个科学研究平台，包含超过1,600个工具资源，支持大规模的跨学科合作和安全的合作。通过标准化科研上下文和工具编排，SCP为多机构、代理驱动的科学研究设立了基础架构，有助于提高科学研究的规模化和可扩展性。
## 4. `cs.AI` - CogRec: 结合大型语言模型和Soar的认知推荐代理以实现可解释的推荐 [PDF](https://arxiv.org/pdf/2512.24113), [HTML](https://arxiv.org/abs/2512.24113)
### Authors
Jiaxin Hu,Tao Wang,Bingsan Yang,Hongrun Wang
### Background
大型语言模型（LLMs）在理解和满足用户偏好方面表现出色，但存在内在的黑箱特征、知识幻觉和在线学习能力有限等关键挑战，这影响了它们的可信度和适应性。相反，如Soar认知架构虽提供了结构化和可解释的推理过程，但其知识获取过程却非常费时。为解决这些问题，本文提出了一种名为CogRec的新型认知推荐代理，将LLMs的优势与Soar认知架构结合。
### Innovation
CogRec 作为认知推荐代理，利用Soar作为其核心符号推理引擎，并借助LLM进行知识初始化以填充工作记忆中的生产规则。该代理遵循感知-认知-行动（PCA）循环，当遇到困境时，它可以动态查询LLM获取推理解决方案，该解决方案随后通过Soar的捆包机制转化为新的符号生产规则，从而实现稳健的在线学习。这种学习范式使代理能够不断进化其知识库，并提供高度可解释的推荐理由。
### Conclusion
在三个公共数据集上进行的广泛评估表明，CogRec在推荐准确性、解释性和解决长尾问题方面表现出显著优势。
## 5. `cs.AI` - 基于图的探索用于ARC-AGI-3交互推理任务 [PDF](https://arxiv.org/pdf/2512.24156), [HTML](https://arxiv.org/abs/2512.24156)
### Authors
Evgenii Rudakov,Jonathan Shock,Benjamin Ultan Cowley
### Background
ARC-AGI-3基准包括游戏样任务，要求智能体通过有限交互推断任务机制，并随着层级复杂度增加逐渐适应。成功的任务解决需要形成假设、验证假设并追踪发现的机制。研究发现，当前最先进的语言模型在可靠解决这些任务方面存在局限。
### Innovation
提出了一种无需训练的基于图的方法来解决ARC-AGI-3基准中的交互推理任务。该方法结合视觉帧处理和系统化状态空间探索，使用图结构表示。它将视觉帧分割成有意义的组件，根据视觉显著性优先选择动作，并维护已探索状态及其转换的有向图。通过跟踪已访问状态和已测试的动作，代理优先选择提供未测试状态-动作对最短路径的动作。
### Conclusion
本方法在ARC-AGI-3预览挑战中解决了6个游戏中52个层级中的中位数30个，排名第三，显著优于当前最先进的基于LLM的智能体。结果显示，即使不进行学习，明确的图结构探索也可以作为交互推理的强大基准，强调在稀疏反馈环境中系统状态跟踪和动作优先级在当前LLM失效时的重要性。代码已开源并可在给定的链接中找到。
## 6. `cs.AI` -  ROAD: 通过自动化调试实现反思优化的零样本代理对齐 [PDF](https://arxiv.org/pdf/2512.24040), [HTML](https://arxiv.org/abs/2512.24040)
### Authors
Natchaya Temyingyong,Daman Jain,Neeraj Kumarsahu,Prabhat Kumar,Rachata Phondi,Wachiravit Modecrua,Krittanon Kaewtawee,Krittin Pachtrachai,Touchapon Kraisingkorn
### Background
自动提示优化（APO）是提升大型语言模型（LLM）性能的关键技术，但当前最先进的方法通常依赖于大型、标注的黄金标准开发集来计算进化算法或强化学习（RL）方法的适应度分数。然而，在实际软件工程中，尤其是在代理开发的初期阶段，很难获得此类经过精制的数据集，工程师往往面临混乱的生产日志和不断变化的失败模式。
### Innovation
我们提出了ROAD（反思优化通过自动化调试）框架，这是一种新颖的方法，它通过将优化视为动态调试调查而不是随机搜索，来绕过对精制数据集的需求。ROAD使用专门的多代理架构，包括分析器进行根本原因分析、优化器进行模式聚合以及教练进行策略集成，将无结构的失败日志转化为稳健的结构化决策树协议。实验结果表明，ROAD具有高度的样本效率，在三个自动迭代后，成功率为5.6%的提高（从73.6%到79.2%），搜索准确率提高了3.8%。此外，在零售领域的复杂推理任务中，ROAD将代理性能相对于基线提高了约19%。
### Conclusion
这些发现表明，模仿人类工程中的故障分析和补丁循环优化途径，提供了在部署可靠的LLM代理方面，一种可行且数据高效的替代密集型RL训练的方法。
## 7. `cs.AI` - 使用大规模语言模型和回答集编程实现可解释性疾病诊断的概念验证 [PDF](https://arxiv.org/pdf/2512.23932), [HTML](https://arxiv.org/abs/2512.23932)
### Authors
Ioanna Gemou,Evangelos Lamprou
### Background
准确的疾病预测对于及时干预、有效治疗以及减少医疗并发症至关重要。尽管符号人工智能已在医疗领域得到应用，但由于构建高质量知识库所需的大量努力，其采用仍受到限制。
### Innovation
提出了一种名为McCoy的框架，该框架结合了大规模语言模型（LLMs）与回答集编程（ASP），以克服这一障碍。McCoy通过使LLM将医学文献翻译成ASP代码，结合患者数据，并利用ASP求解器处理这些数据，从而达成最终诊断。这种集成产生了一种稳健且可解释的预测框架，充分利用了两种范式的优点。
### Conclusion
初步结果显示，McCoy在小型疾病诊断任务中具有强大的性能。
## 8. `cs.AI` - 使用深度强化学习解决车队规模和混合车辆路线问题 [PDF](https://arxiv.org/pdf/2512.24251), [HTML](https://arxiv.org/abs/2512.24251)
### Authors
Pengfu Wan,Jiawei Chen,Gangyan Xu
### Background
车队规模和混合车辆路线问题(FSMVRP)是车辆路线问题(VRP)的一个重要变种，受到了运筹学和计算科学的广泛研究。由于需要同时做出车队组成和路线规划的决策，FSMVRP在短时租赁车辆和需求物流等领域具有很高的实际应用价值。但是，这些要求也提高了FSMVRP的复杂性，特别是在大规模和时间受限的环境中，这构成了显著的挑战。
### Innovation
本文提出了一种基于深度强化学习(DRL)的方法来解决FSMVRP，能够在几秒钟内生成接近最优的解决方案。具体而言，将问题形式化为马尔可夫决策过程(MDP)，并开发了一种新的策略网络，称为FRIPN，该网络能够无缝地集成车队组成和路线决策。该方法还结合了针对不同决策目标的专业输入嵌入，包括剩余图嵌入以促进有效的车辆调度决策。
### Conclusion
在随机生成的实例和基准数据集上进行了全面的实验。实验结果表明，我们的方法在计算效率和可扩展性方面表现出显著优势，特别是在大规模和时间受限的场景中。这些优点突显了我们方法在实际应用中的潜力，并为其他VRP变体中扩展DRL技术提供了宝贵的想法。
## 9. `cs.AI` - CASCADE: 通过自主发展和进化实现累积性代理技能创建 [PDF](https://arxiv.org/pdf/2512.23880), [HTML](https://arxiv.org/abs/2512.23880)
### Authors
Xu Huang,Junwu Chen,Yuxing Fei,Zhuohan Li,Philippe Schwaller,Gerbrand Ceder
### Background
当前大型语言模型（LLM）代理依赖预定义工具或脆弱的工具生成，这限制了它们在复杂科学任务中的能力和适应性。
### Innovation
引入了CASCADE，这是一种自我进化的代理框架，代表了从“LLM + 工具使用”向“LLM + 技能习得”的早期转变。CASCADE允许代理掌握复杂的外部工具并通过两种元技能进行知识编码：通过网络搜索和代码提取实现持续学习，以及通过内省和知识图谱探索进行自我反思。
### Conclusion
CASCADE在外科合成等116个材料科学和化学研究任务中的基准测试中，使用GPT-5取得了93.3%的成功率，而没有进化机制则仅为35.4%。进一步展示了CASCADE在计算分析、自主实验室实验和选择性复制已发表论文等现实世界应用中的潜力，同时与人类-代理协作和记忆巩固相结合，CASCADE收集可执行技能并可以跨代理和科学家共享，朝着可扩展的人工智能辅助科学研究迈进。
## 10. `cs.AI` - SPARK: 通过代理驱动检索和知识共享实现个性化搜索 [PDF](https://arxiv.org/pdf/2512.24008), [HTML](https://arxiv.org/abs/2512.24008)
### Authors
Gaurab Chhetri,Subasish Das,Tausif Islam Chowdhury
### Background
个性化搜索需要能力来建模用户不断变化、多维的信息需求，这对于受到静态用户资料或单一检索管道限制的系统来说是一项挑战。SPARK通过协调基于角色的大型语言模型（LLM）代理机构，提供任务特定的检索和个人化的新兴形式。它定义了一个由角色、专长、任务环境和技术领域组成的角色空间，并引入了一个角色协调器，能够动态解释传入查询以激活最相关的专门代理。
### Innovation
SPARK提供了一个框架，其中协调的基于角色的大型语言模型代理执行特定任务的检索和个人化，每个代理都有独立的检索增强生成过程，支持专用的长期和短期记忆存储和上下文感知推理模块。代理之间的合作通过结构化的通信协议（包括共享记忆库、迭代辩论和接力式知识转移）来促进。SPARK利用认知架构、多代理协调理论和信息检索的原则，模拟了如何从分布式代理行为中生成的协调高效性、个性化质量和认知负荷分配的可测试预测，同时结合了适应性学习机制以实现连续人物的细化。
### Conclusion
通过整合细粒度代理专业化与协同检索，SPARK为新一代能够捕捉人类信息检索行为复杂性、流动性和上下文敏感性的搜索系统提供了见解。
## 11. `cs.AI` - UniHetero：大规模数据集下生成能否增强视觉语言模型的理解能力？ [PDF](https://arxiv.org/pdf/2512.23512), [HTML](https://arxiv.org/abs/2512.23512)
### Authors
Fengjiao Chen,Minhao Jing,Weitao Lu,Yan Feng,Xiaoyu Li,Xuezhi Cao
### Background
视觉语言大模型正朝着视觉理解和生成任务的统一方向发展。然而，生成是否能提升理解能力这一问题在大规模数据集上的潜力尚未充分探索。
### Innovation
论文分析了名为UniHetero的紧凑结构模型，并在超过200M样本的大型预训练下进行研究。研究发现：1）生成确实能改善理解能力，但必须是语义级别的生成，而非像素级别的。2）生成显示了更好的数据扩增趋势和更高的数据利用效率。3）在输入嵌入上进行自回归有助于捕捉视觉细节，相较于常用的视觉编码器，这种方法在累积误差更少且跨模态适用性更强。
### Conclusion
生成在大规模数据集下的视觉语言模型中不仅可以辅助理解，还能更好地利用数据并展现超越传统跨模态学习模式的有效性。通过UniHetero模型，研究发现了提升视觉理解能力的新途径，特别是在大型数据集上的应用。
## 12. `cs.CL` - CAT: 一种基于度量的框架，用于在可控输入变化下分析大型语言模型的准确性和一致性关系 [PDF](https://arxiv.org/pdf/2512.23711), [HTML](https://arxiv.org/abs/2512.23711)
### Authors
Paulo Cavalin,Cassia Sanctos,Marcelo Grave,Claudio Pinhanez,Yago Primerano
### Background
当前，对大型语言模型（LLMs）的评估主要集中在模型的能力，如准确性或基准分数上，而近期则开始重视衡量一致性。本文认为，虽然在独立评估这两项维度的同时，也需要考虑它们之间的依赖关系，以进行更为细腻的评估。
### Innovation
本文提出了CAT框架，用于评估和可视化LLMs在可控输入变化下的准确性和一致性之间的相互作用。CAT的核心是Consistency-Accuracy Relation (CAR)曲线，该曲线展示了在增加一致性要求时模型准确性的变化，并提出了Consistency-Oriented Robustness Estimate (CORE)指数，这是一种结合CAR曲线的面积和形状的综合指标，用于量化准确性和一致性的权衡。
### Conclusion
通过多样化的通用和专用LLMs以及多个选择题基准任务的实证演示，本文展示了CAT框架的有效性和普遍适用性，同时也指出了CAT在支持长格式、开放式评估方面的潜力。
## 13. `cs.CL` - PyBangla在BLP-2025任务2中的表现：通过迭代自我纠正与多语言代理提升Bangla-to-Python代码生成 [PDF](https://arxiv.org/pdf/2512.23713), [HTML](https://arxiv.org/abs/2512.23713)
### Authors
Jahidul Islam,Md Ataullha,Saiful Azad
### Background
LLMs在从英文提示生成代码方面表现出色，但这种进步尚未扩展到低资源语言。针对这一问题，本文通过引入BanglaCodeAct框架，利用多代理提示和迭代自我纠正技术来解决Bangla-to-Python代码生成问题。
### Innovation
本文提出了BanglaCodeAct框架，它采用了一种基于思路-代码-观察（Thought-Code-Observation）的循环，利用开源多语言LLM，以动态生成、测试和改进从Bangla指令中得到的代码。该框架不同于依赖于特定任务微调的先前方法，展示了在低资源语言中进行可靠代码生成的潜力。
### Conclusion
实验结果显示，Qwen3-8B在部署BanglaCodeAct后，开发集上的pass@1准确率为94.0%，盲测集上为71.6%。这为Bangla-to-Python的翻译设定了新的基准，并强调了基于代理推理在低资源语言代码生成中的潜在价值。实验脚本已在公共平台发布。
## 14. `cs.AI` - RxnBench：科学文献中化学反应理解的多模态基准 [PDF](https://arxiv.org/pdf/2512.23565), [HTML](https://arxiv.org/abs/2512.23565)
### Authors
Hanzheng Li,Xi Fang,Yixuan Li,Chaozheng Huang,Junjie Wang,Xi Wang,Hongzhe Bai,Bojun Hao,Shenyu Lin,Huiqi Liang,Linfeng Zhang,Guolin Ke
### Background
将多模态大型语言模型（MLLMs）集成到化学研究中有望推动科学发现，然而这些模型理解化学文献中密集的、图形化的反应语言的能力仍然未被广泛研究。为此，作者提出了RxnBench，这是一个多层级基准，旨在严格评估MLLMs在科学PDF中化学反应理解方面的能力。RxnBench包含两个任务：单图问答（SF-QA）和全文档问答（FD-QA），以测试模型的细粒度视觉感知、机制推理能力以及跨模态信息整合能力。
### Innovation
本文介绍了一种多模态基准RxnBench，用于评估大型语言模型在科学文献中理解化学反应的能力。RxnBench包含两个任务：单图问答（SF-QA）和全文档问答（FD-QA），揭示了模型在提取显性文本方面表现出色，但在化学逻辑的深入理解和精确结构识别方面存在重大差距。研究发现，具有推理时间推理能力的模型显著优于标准架构，但在FD-QA上没有任何模型达到50%的准确性。这些发现强调了开发领域特定的视觉编码器和更强大的推理引擎以促进自主AI化学家进程的迫切需求。
### Conclusion
研究表明，MLLMs在提取显性文本方面表现出色，但在复杂的化学逻辑理解和精确结构识别方面存在显著差距。具有推理时间推理能力的模型明显优于标准模型，但当前模型远未达到实际应用的标准。因此，需要开发适用于化学领域的视觉编码器和更强大的推理引擎，以推动自主AI化学家的发展。
## 15. `cs.CL` - 噪声驱动的人格形成在反思型神经语言生成中 [PDF](https://arxiv.org/pdf/2512.23716), [HTML](https://arxiv.org/abs/2512.23716)
### Authors
Toshiyuki Shigemura
### Background
本文介绍了一种计算框架——卢卡噪声反射协议（LN-RP），用于分析大型语言模型中噪声驱动的人格涌现。通过在初始生成状态中注入随机噪声种子，观察到在152次生成循环中语言行为的非线性转变。研究表明，外部噪声源可以可靠地诱导反射性生成动态的相变。量化评估证实了人格的稳定保留以及不同模式之间显著的不同（p < 0.01）。该协议为研究反思型生成、涌现行为和LLM中的长期语言连贯性提供了一种可重复的方法。
### Innovation
提出了卢卡-噪声反射协议（LN-RP），通过在初始生成状态中注入随机噪声种子来研究噪声驱动的人格涌现。该方法揭示了三种具有不同熵特征的稳定人格模式，并证明了外部噪声源可以可靠地诱导反射性生成动态的相变。通过量化评估验证了不同模式之间人格留存的显著差异。
### Conclusion
卢卡-噪声反射协议为研究LLM中的反射型生成、涌现行为和长期语言连贯性提供了一种可重复的方法，结果展示了通过外部噪声源诱导的相变能够使生成动态产生显著变化。
## 16. `cs.CL` - STED和一致性评分：评估LLM结构化输出可靠性的框架 [PDF](https://arxiv.org/pdf/2512.23712), [HTML](https://arxiv.org/abs/2512.23712)
### Authors
Guanghui Wang,Jinze Yu,Xing Zhang,Dayuan Jiang,Yin Song,Tomal Deb,Xuefeng Liu,Peiyang He
### Background
大型语言模型（LLMs）越来越多地用于生成结构化数据，但输出一致性对于生产应用至关重要。目前缺乏全面的评估框架来衡量和提升LLM生成的结构化输出的一致性。
### Innovation
引入了结合语义树编辑距离（STED）的综合框架，该框架既能平衡语义灵活性又严格控制结构一致性，同时开发了一种综合评分框架，通过多次生成的STED测量聚合来量化可靠性。实验结果表明，STED在语义等价性和结构性断裂方面性能优越，比现有指标（如TED、BERTScore和DeepDiff）更为出色。此外，该框架还揭示了不同LLM在一致性的显著差异。
### Conclusion
该研究为LLM基于的生产系统提供了理论基础和实用工具，以期实现可靠生成结构化输出的目的。框架有助于目标模型选择、迭代提示优化以获得可重复结果以及诊断分析以找出不一致性根本原因。
## 17. `cs.CL` - HarmTransform：通过多代理辩论将明确有害查询转变为隐蔽 [PDF](https://arxiv.org/pdf/2512.23717), [HTML](https://arxiv.org/abs/2512.23717)
### Authors
Shenzhe Zhu
### Background
大语言模型（LLMs）配备了安全机制以检测并阻止有害查询，但当前的对齐方法主要关注明显危险的内容，而忽视了一些更隐蔽的威胁。用户可以利用隐蔽重述的行为，即保留恶意目的的同时使得查询看似无害，这在现有安全训练数据中产生了显著的差距。
### Innovation
本文引入了HarmTransform，这是一种多代理辩论框架，旨在系统地将有害查询转变成更为隐蔽的形式，同时保留其潜在的有害意图。该框架利用多个代理之间的迭代批评和改进过程来生成高质量、隐蔽的有害查询变体，这些变体可用于提高未来LLM安全对齐的质量。实验表明，HarmTransform在生成有效的查询变体方面显著优于标准的基本方法。同时，分析还揭示了辩论的双刃剑效应：虽然它可以提高变换的复杂性和隐蔽性，但也可能会引入主题偏离和不必要的复杂性。
### Conclusion
研究结果强调了多代理辩论在生成全面的安全训练数据方面的潜力和限制。
## 18. `cs.CL` - 涌现的世界信念：探索在随机游戏中的大语言模型 [PDF](https://arxiv.org/pdf/2512.23722), [HTML](https://arxiv.org/abs/2512.23722)
### Authors
Adam Kamel,Tanish Rastogi,Michael Ma,Kailash Ranganathan,Kevin Zhu
### Background
基于变换器的大型语言模型（LLMs）在各类领域展现了强大的推理能力，包括解决编程挑战和参与如国际象棋等策略性游戏。先前的研究表明，LLMs能够在完美信息下的游戏中发展出隐含的世界模型，其中内部表示对应于环境的潜在状态。本研究旨在将这一方法应用于不完整信息环境下，在此领域选择德州扑克作为典型的部分可观测马尔可夫决策过程（POMDP）进行研究。
### Innovation
研究对不完整信息环境中的游戏进行了探索，使用GPT样式模型在德州扑克手牌历史数据上进行预训练，并探究其内部激活。研究结果表明，模型可以学习到确定性结构如手牌等级和随机特征如权益等，并且通过非线性探针表明这些表示是可以解码的，并与理论信念状态相关，意味着LLMs正在学习其对应于德州扑克随机环境的结构。
### Conclusion
研究验证了基于变换器的大型语言模型在随机游戏中的能力，显示这些模型可以自主学习相关结构和随机特征，并能够生成可以解码和解释的内部表示。这为理解LLMs在复杂环境下的学习能力提供了新视角。
## 19. `cs.CL` - 数字化历史记录：基于OCR和AI的数据库集成方法 [PDF](https://arxiv.org/pdf/2512.23710), [HTML](https://arxiv.org/abs/2512.23710)
### Authors
Zahra Abedi,Richard M.K. van Dijk,Gijs Wijnholds,Tessa Verhoef
### Background
该研究分析了1983年至1985年间关于莱顿大学教授和教员的书籍数据（Leidse hoogleraren en lectoren 1575-1815），旨在设计一个自动处理流水线，整合OCR、基于LLM的解释以及数据库关联，以将历史文件中的数据与现有高质量数据库记录协调起来。研究通过应用OCR技术、生成性AI数据提取规则和数据库关联方法，将手写历史记录转换为数字格式，并且研究了布局变化和术语差异等挑战。
### Innovation
研究通过使用生成性AI纠正了低效的OCR性能，生成性AI在数据结构化提取中发挥了作用。研究还提出了一种记录关联算法，该算法在标注的JSON文件与OCR衍生的JSON文件之间实现了94%和81%的准确率。这一方法对于数字人文研究具有重要贡献，提供了一种自动处理数字化历史文件的管道，并探索了高级生成性AI模型的应用性和有效性。
### Conclusion
该研究设计了一个自动化流水线来解读数字化的历史文件，并解决了诸如布局变化和术语差异等挑战，同时探索了高级生成性AI模型的应用性和有效性。这一方法为历史文献数字化领域的数据集成工作提供了参考。
## 20. `cs.CL` -  PharmaShip: 以实体为中心、基于阅读顺序监督的中文医药运输文件基准测试 [PDF](https://arxiv.org/pdf/2512.23714), [HTML](https://arxiv.org/abs/2512.23714)
### Authors
Tingwei Xie,Tianyi Zhou,Yonghong Song
### Background
该研究旨在构建一个名为PharmaShip的实际中文医药运输文件数据集，用于测试预训练的文本布局模型在嘈杂的光学字符识别（OCR）和异构模板下的性能。PharmaShip涵盖了序列实体识别（SER）、关系提取（RE）和阅读顺序预测（ROP）这三项互补任务，并采用了实体为中心的评估协议，减少了不同架构之间的混淆因素。
### Innovation
研究基准测试了五个代表性的基线模型，包括像素感知和几何感知模型（LiLT、LayoutLMv3-base、GeoLayoutLM及其可用的RORE增强变体），并标准化了预处理、划分和优化流程。实验结果表明，像素和显式几何提供了互补的归纳偏置，但仅凭其中之一是不够的；引入基于阅读顺序的正则化可以提升序列和实体识别的性能，提供最稳健的配置；更长的定位覆盖范围可以稳定后页预测并减少截断伪影。tableNameTreeWidgetItem对象的精准性在单词级别上表现出色，但在段落级别上却具有挑战性，这反映了边界模糊和长距离穿越的问题。
### Conclusion
PharmaShip为医药领域关键文件的理解建立了受控、可重复的基准测试，并强调了序列感知约束作为结构建模的可转移偏置。该数据集已发布。
## 21. `cs.LG` - 差分隐私与PAC隐私下的私有线性回归 [PDF](https://arxiv.org/pdf/2412.02578), [HTML](https://arxiv.org/abs/2412.02578)
### Authors
Hillary Yang,Yuntao Du
### Background
线性回归是一个基础的统计分析工具，因此开发具有可证明隐私保证的线性回归方法变得很重要。现有的大多数隐私保护线性回归方法依赖于成熟的差分隐私框架，但对于PAC隐私（Probably Approximately Correct Privacy）在这一领域的应用尚未研究。
### Innovation
本文系统性地比较了差分隐私和PAC隐私下的线性回归模型在三个真实世界数据集上的表现，揭示了在隐私保护线性回归中的几个关键发现。
### Conclusion
通过对比差分隐私和PAC隐私下的线性回归模型性能，本文揭示了在隐私保护线性回归中的几个重要发现，这些发现对性能具有重大影响。
## 22. `cs.LG` - Model Merging in LLMs, MLLMs, and Beyond: Methods, Theories, Applications and Opportunities [PDF](https://arxiv.org/pdf/2408.07666), [HTML](https://arxiv.org/abs/2408.07666)
### Authors
Enneng Yang,Li Shen,Guibing Guo,Xingwei Wang,Xiaochun Cao,Jie Zhang,Dacheng Tao
### Background
模型合并是一种在机器学习社区中高效的技术，它不需要收集原始训练数据，也不需要昂贵的计算资源。随着模型合并技术在各个领域的普及，理解这些技术的全面性变得至关重要。然而，文献中关于这些技术的系统性综述仍然存在很大空白。
### Innovation
本文首次提出了一个新的分类方法，全面讨论了现有的模型合并方法。此外，讨论了模型合并技术在大型语言模型、多模态大型语言模型以及十几个机器学习亚领域（包括持续学习、多任务学习、少样本学习等）的应用。
### Conclusion
本文指出了模型合并所面临的挑战，并讨论了未来的研究方向。所有关于模型合并的论文列表可以在该网址获取：this https URL.
## 23. `cs.LG` - 基于状态博弈的制造系统过程优化中的转移学习 [PDF](https://arxiv.org/pdf/2408.05992), [HTML](https://arxiv.org/abs/2408.05992)
### Authors
Steve Yuwono,Dorothea Schwung,Andreas Schwung
### Background
该研究提出了一种在状态博弈（SbPG）中应用在线转移学习的方法，旨在改善半集中式制造系统中的分布式自动优化。研究注重于在大规模且分散的场景中，通过知识共享来提高认知学习效果。
### Innovation
该论文开发了一种新型的转移学习方法（TL-SbPG），使玩家能够利用他人的已有策略来提高自己的学习成果。通过建立预定义和动态推断的相似性标准，玩家可以更好地共享知识，改善学习效果并加速收敛过程。此外，还提出了一种优化知识转移的时间和权重的方法。
### Conclusion
实验结果表明，TL-SbPG相比传统的SbPG，在提高生产效率并降低电力消耗方面具有显著的优势。
## 24. `cs.LG` - SoundnessBench: 用于神经网络验证的正确性基准 [PDF](https://arxiv.org/pdf/2412.03154), [HTML](https://arxiv.org/abs/2412.03154)
### Authors
Xingjian Zhou,Keyi Shen,Andy Xu,Hongji Xu,Cho-Jui Hsieh,Huan Zhang,Zhouxing Shi
### Background
神经网络验证旨在正式验证神经网络的属性，这对于确保基于神经网络的模型在关键应用中的行为至关重要。近年来，社区开发了许多神经网络验证器和基准测试来评估它们的性能。然而，现有的基准测试通常缺乏难以验证的实例的正确答案，即在没有当前验证器可以验证的属性且找不到反例的情况下。这使得在验证器声称验证难以处理的实例时验证其正确性变得困难。
### Innovation
本文开发了一种新的神经网络验证基准，称为SoundnessBench，专门用于测试神经网络验证器的正确性。SoundnessBench 包含故意插入的被隐藏的反例，这些反例通常用于发现反例的对抗性攻击中被隐藏。我们的训练方法用于产生具有隐藏反例的神经网络，并系统地构建我们的 SoundnessBench，涵盖了各种模型架构、激活函数和输入数据。我们的实验表明，我们所训练的有效性产生了隐藏的反例，并且我们的 SoundnessBench 成功地识别了最先进的神经网络验证器中的缺陷。
### Conclusion
我们的代码可在 https://github.com/your-repo 地址获取，我们的数据集可在 https://your-dataset 地址获取。
## 25. `cs.LG` - 批量最优传输与离散流匹配中的困惑度界限估计 [PDF](https://arxiv.org/pdf/2411.00759), [HTML](https://arxiv.org/abs/2411.00759)
### Authors
Etrit Haxholli,Yeti Z. Gürbüz,Oğul Can,Eli Waxman
### Background
离散流匹配是一种最近用于建模分类数据的框架，显示出了与自回归模型相竞争的表现。然而，由于离散路径的随机性，无法应用修正策略，因此需要开发替代方法以最小化状态转换。
### Innovation
提出了一个类似动态最优传输的最小化目标及其Kantorovich形式，适用于具有凸插值的离散流，传输费用仅依赖于状态间相似度，并可通过批量策略进行优化。对于基于词袋（BoW）的流，该方法可以减少多达8次（从1024减少到128）转换次数，以达到相同生成困惑度，而不牺牲多样性。此外，提出了两种困惑度上限估计方法，使得可以进行有原则的训练、评估和模型比较。引入了多掩码流，与掩码流相比，在使用批量最优传输时具有更优的生成困惑度，同时保留了多样性。
### Conclusion
通过新的最小化目标优化离散流匹配，并引入了批量最优传输，提出了困惑度界限估计方法，实现了对离散流匹配的改进和性能提升。
## 26. `cs.LG` - Tazza: 利用神经网络参数混排实现安全和隐私保护的联邦学习 [PDF](https://arxiv.org/pdf/2412.07454), [HTML](https://arxiv.org/abs/2412.07454)
### Authors
Kichang Lee,Jaeho Jin,JaeYeon Park,Songkuk Kim,JeongGil Ko
### Background
联邦学习允许在不共享原始数据的情况下分散训练模型，从而保护数据隐私。然而，联邦学习仍然面临诸如梯度反转和恶意客户端的模型毒化等关键安全威胁。现有解决方案往往单方面解决这些问题，牺牲系统鲁棒性或模型准确性。
### Innovation
Tazza 是一种结合了权重混排和顺序等变性及不变性属性的联邦学习框架，旨在同时解决安全性和准确性问题。Tazza 增强了对各种攻击的鲁棒性，同时确保数据保密性和高模型准确性。
### Conclusion
在不同数据集和嵌入式平台上的综合评估表明，Tazza 在高达 6.7 倍的计算效率改进下实现了稳健的防御，而性能并未受到影响。
## 27. `cs.LG` - 利用GAN模型检测在线支付中的AI换脸和欺诈活动 [PDF](https://arxiv.org/pdf/2501.07033), [HTML](https://arxiv.org/abs/2501.07033)
### Authors
Zong Ke,Shicheng Zhou,Yining Zhou,Chia Hong Chang,Rong Zhang
### Background
随着AI换脸技术的日益普及，这种技术能够操纵图片和视频中的面部特征，导致在线交易中的欺诈行为增多。传统的安全系统难以识别这些复杂的欺诈行为。为了提升在线支付的安全性，本研究提出了一种基于GAN的新模型，通过识别支付图片中的微妙篡改来检测潜在的欺诈行为。
### Innovation
本研究提出了一种新的基于GAN的模型，该模型通过使用包括StyleGAN和DeepFake在内的先进GAN架构生成的图片数据集进行训练，能够准确地区分真实交易和AI换脸，检测率超过了95%。这种模型显著提升了支付系统对AI驱动欺诈的抵抗力。
### Conclusion
本研究为数字安全领域提供了一种新的视角，展示了GAN在金融服务业欺诈检测中的应用。通过这种方式，可以显著增强在线支付系统的安全性，对抗由AI驱动的欺诈行为。
## 28. `cs.LG` - A Systematic Survey on Large Language Models for Algorithm Design [PDF](https://arxiv.org/pdf/2410.14716), [HTML](https://arxiv.org/abs/2410.14716)
### Authors
Fei Liu,Yiming Yao,Ping Guo,Zhiyuan Yang,Zhe Zhao,Xi Lin,Xialiang Tong,Kun Mao,Zhichao Lu,Zhenkun Wang,Mingxuan Yuan,Qingfu Zhang
### Background
算法设计对于各种领域中的有效问题解决至关重要。大型语言模型（LLMs）的出现显著提升了该领域的自动化和创新水平，带来了新的视角和有希望的解决方案。尽管在过去几年里这一整合已经在组合优化和科学发现等领域取得了显著进展，但缺乏系统的综述阻碍了对该领域的全面理解。现有综述要么局限于狭窄的子领域，要么有不同目的。
### Innovation
本文介绍了对LLMs在算法设计中的角色分类，即优化器、预测器、抽取器和设计师，并分析了每类中的进展、优势和局限性。进一步综合了算法设计管道的三个阶段和各种算法应用的文献，以界定当前的领域格局。最后，概述了关键的开放挑战和机会，以指导未来的研究。
### Conclusion
本文旨在提供系统综述LLMs在算法设计中的应用，帮助研究人员对该领域的全面现状有一个系统的理解，识别关键的开放挑战和机会，以指导未来的探索。
## 29. `cs.LG` - 受监督机器学习算法的泛化误差 [PDF](https://arxiv.org/pdf/2411.12030), [HTML](https://arxiv.org/abs/2411.12030)
### Authors
Samir M. Perlaza,Xinying Zou
### Background
本文介绍了一种称为隙的方法，用于导出以信息量表征的泛化误差的封闭形式表达式。隙的概念可以帮助区分固定模型和固定数据集的情况，这在计算泛化误差方面提供了一种新的视角。该方法的核心在于分析期望经验风险变化，以此来揭示算法驱动和数据驱动的隙，并进一步通过相对熵表示这些隙。这种方法可以应用于所有现有的受监督机器学习算法，能够提供其泛化误差的精确表达式。
### Innovation
本文提出了一种计算受监督机器学习算法泛化误差的新方法——隙方法。这种方法利用了隙的概念，并通过相对熵来表示算法驱动和数据驱动的隙。这种方法不仅能够提取之前所有精确的泛化误差表达式，还能够获得新的精确表达式，建立了该领域与其他统计领域之间的联系，具有很高的创新性。
### Conclusion
本文提出的方法为计算受监督机器学习算法的泛化误差提供了一种新的、通用的方法。通过隙的概念和相对熵的表示，可以准确地描述算法驱动和数据驱动的泛化误差。这种方法不仅适用于已有的模型，也能够为新的研究方向提供支持。
## 30. `cs.LG` - Lagrangian Index Policy for Restless Bandits with Average Reward [PDF](https://arxiv.org/pdf/2412.12641), [HTML](https://arxiv.org/abs/2412.12641)
### Authors
Konstantin Avrachenkov,Vivek S. Borkar,Pratik Shah
### Background
研究无干扰多臂老虎机(long-run平均奖励)问题的拉格朗日指数策略(LIP)与韦尔布勒指数策略(WIP)的性能比较，尽管这两种策略在大多数情况下表现相似，但在WIP表现不佳的情况下，LIP仍然表现出色。论文还提出了适用于LIP的无模型强化学习算法，这些算法相比WIP的类似算法需要更少的内存，并计算了拉格朗日指数在重启模型中的解析解，适用于最优网络爬虫和信息年代的最小化问题。此外，论文还基于可交换性和德费尼蒂定理证明了同质臂在臂数趋向无穷时的渐近最优性。
### Innovation
提出了适用于LIP的无模型强化学习算法；计算了拉格朗日指数在重启模型中的解析解；证明了同质臂在臂数趋向无穷时的渐近最优性。
### Conclusion
研究了LIP在平均奖励的无干扰多臂老虎机中的应用，证明了LIP在某些情况下的优越性；提出了适用于LIP的无模型强化学习算法，并证明了该算法的高效性；计算了拉格朗日指数在特定模型中的解析形式，并给出了同质臂渐近最优性的新证明。
