# 20251229
[![Subscribe_Visitors](https://visitor-badge.laobi.icu/badge?page_id=nituchao.latest_arxiv_analyze_ai_rss)](https://github.com/nituchao/latest_arxiv_analyze_ai)

## 1. `cs.AI` - AIAuditTrack: 一个基于区块链的AI安全框架 [PDF](https://arxiv.org/pdf/2512.20649), [HTML](https://arxiv.org/abs/2512.20649)
### Authors
Zixun Luo,Yuhang Fan,Yufei Li,Youzhi Zhang,Hengyu Lin,Ziqi Wang
### Background
随着以大规模语言模型驱动的AI应用的迅速增加，AI交互数据也随之激增，这带来了安全、问责和风险追踪方面的迫切挑战。
### Innovation
本论文提出了一个名为AiAuditTrack (AAT) 的区块链框架，用于记录和治理AI使用流量。AAT 使用去中心化身份 (DID) 和可验证凭证 (VC) 来建立可信赖且可识别的AI实体，并将实体间的交互轨迹记录在区块链上，以便进行跨系统的监督和审计。论文中提出了一种风险扩散算法，用于追踪不良行为的起源并在涉及实体之间传播早期警告。
### Conclusion
AAT 为复杂多代理环境中的AI审计、风险管理及责任归属提供了一个可扩展且可验证的解决方案。评估表明，AAT 在大规模交互记录下具有可行性和稳定性。
## 2. `cs.AI` - 20th International Conference on Knowledge, Information and Creativity Support Systems (KICSS 2025) 的会议论文集 [PDF](https://arxiv.org/pdf/2512.20628), [HTML](https://arxiv.org/abs/2512.20628)
### Authors
Edited by Tessai Hayama(Nagaoka University of Technology, Japan),Takayuki Ito(Kyoto University, Japan),Takahiro Uchiya(Nagoya Institute of Technology, Japan),Motoki Miura(Chiba Institute of Technology, Japan),Takahiro Kawaji(University of Kurume, Japan),Takaya Yuizono(Japan Advanced Institute of Science and Technology, Japan),Atsuo Yoshitaka(Japan Advanced Institute of Science and Technology, Japan),Tokuro Matsuo(Advanced Institute of Industrial Technology, Japan),Shun Okuhara(Mie University, Japan),Jawad Haqbeen(Kyoto University, Japan),Sofia Sahab(Kyoto University, Japan),Wen Gu(Nagoya Institute of Technology, Japan),Shiyao Ding(Kyoto University, Japan)
### Background
该论文集是2025年12月3日至5日在日本秋田举行的第20届知识、信息和创意支持系统国际会议（KICSS 2025）的会议记录。该会议专注于人工智能、知识工程、人机交互和创意支持系统的跨学科研究。
### Innovation
会议采用双盲评审流程接收论文，并经过额外的同行评审后，部分论文被推荐至《IEICE电子与信息系统 Transactions》期刊出版。这表明论文经过了严格的同行评审过程，旨在确保发表的文章具有高学术价值。
### Conclusion
此次会议提供了一个多学科的平台，促进了相关领域的学术交流和合作。论文集展示了最新研究成果和趋势，为该领域的发展做出了贡献。
## 3. `cs.AI` - 推理接力：在数学推理中评估大型语言模型的稳定性和可替代性 [PDF](https://arxiv.org/pdf/2512.20647), [HTML](https://arxiv.org/abs/2512.20647)
### Authors
Leo Lu,Jonathan Zhang,Sean Chua,Spencer Kim,Kevin Zhu,Sean O'Brien,Vasu Sharma
### Background
近年来，链式思维（CoT）提示法显著提高了大规模语言模型（LLMs）的推理能力。以往研究侧重于通过内部推理策略来提高模型性能，但对于不同模型之间的推理替代性知之甚少。本文旨在探讨一个模型部分完成的推理链是否可以在另一个模型中可靠地继续，并研究这一过程是否维护了推理的一致性和可靠性。
### Innovation
本文通过使用中间推理痕迹作为转换的支架来评估逻辑连贯性和最终答案准确性，探索推理的可替代性作为衡量推理模型在推理时间的信任度的新方法。通过基线模型Gemma-3-4B-IT和LLaMA-3.1-70B-Instruct在不同阶段截断推理，分别与同家族模型Gemma-3-1B-IT和跨家族模型LLaMA-3.1-8B-Instruct进行连续实验，利用包含过程奖励模型（PRM）的评估管道框架来检测推理稳定性和可替代性。
### Conclusion
结果表明，混合推理链在很多情况下能保持，甚至提高最终准确性及逻辑结构。这些发现揭示了推理模型中可替代性作为新兴行为模式，并为可靠模块化推理的协作AI系统提供了新的范式见解。
## 4. `cs.AI` - 量子启发的多智能体强化学习在无人机辅助6G网络部署中的探索与利用优化 [PDF](https://arxiv.org/pdf/2512.20624), [HTML](https://arxiv.org/abs/2512.20624)
### Authors
Mazyar Taghavi,Javad Vahidi
### Background
本文提出了一种基于量子启发的方法，用于在多智能体强化学习中优化探索与利用的权衡，应用于无人机辅助的6G网络部署。考虑了十个智能无人机在部分可观测性和动态条件下自主协调，以最大化信号覆盖并支持高效的网络扩展的协同场景。
### Innovation
提出的方法将经典MARL算法与量子启发的优化技术结合，使用变量子电路VQCs作为核心结构，并采用量子近似优化算法QAOA作为基于VQCs的组合优化的代表方法。引入了贝叶斯推理、高斯过程和变分推理互补的概率模型来捕捉隐含环境动力学。采用中心集训和分布式执行CTDE范式，通过共享内存和局部视图网格增强分区域内的可观测性。实验结果表明，与PPO和DDPG基线相比，提出的框架提高了样本效率，加速了收敛，并提高了覆盖性能，同时保持了鲁棒性。雷达图和收敛性分析进一步表明，量子启发的MARL在探索与利用之间取得了优于经典方法的平衡。
### Conclusion
综合实验，包括扩展性测试、敏感性分析和与PPO和DDPG基线的比较，表明提出的框架在样本效率、收敛加速和覆盖性能方面有所改进，且具备鲁棒性。雷达图和收敛性分析进一步表明，QI MARL在探索与利用之间达到了优于经典方法的平衡。所有实现代码和补充材料均可在GitHub上公开获取，以确保可复现性。
## 5. `cs.AI` - Memory Bear AI 从记忆到认知 面向通用人工智能 [PDF](https://arxiv.org/pdf/2512.20651), [HTML](https://arxiv.org/abs/2512.20651)
### Authors
Deliang Wen,Ke Sun
### Background
大型语言模型（LLMs）在记忆方面存在固有限制，包括受限的上下文窗口、长期知识遗忘、重复信息积累以及虚构生成。这些问题严重限制了持续对话和个人化服务的性能。
### Innovation
提出Memory Bear系统，基于认知科学原则构建类人类的记忆架构。通过结合多模态信息感知、动态记忆维护和认知服务适应性，Memory Bear实现了LLM记忆机制的全链路重建。在医疗、企业运营和教育等多个领域，Memory Bear展现了工程创新和性能突破，显著提高了长期对话的知识准确性和检索效率，降低了虚构率，并通过记忆与认知的结合提升了上下文适应性和推理能力。实验结果显示，与现有解决方案（如Mem0、MemGPT、Graphiti）相比，在准确性、令牌效率和响应延迟等关键指标上，Memory Bear表现更佳，标志着在从记忆到认知的AI发展道路上取得了关键进展。
### Conclusion
Memory Bear在多个关键指标上显著优于现有解决方案，标志着AI从记忆向认知发展的关键一步。
## 6. `cs.AI` - Erkang-Diagnosis-1.1技术报告 [PDF](https://arxiv.org/pdf/2512.20632), [HTML](https://arxiv.org/abs/2512.20632)
### Authors
Jianbing Ma,Ao Feng,Zhenjie Gao,Xinyu Song,Li Su,Bin Chen,Wei Wang,Jiamin Wu
### Background
该报告详细介绍了Erkang-Diagnosis-1.1模型，这是基于阿里巴巴Qwen-3模型开发的AI医疗咨询助手。Erkang模型整合了约500GB的高质量结构化医疗知识，采用增强前期训练和检索增强生成的混合方法，以确保安全、可靠和专业的AI健康顾问。此模型通过3-5轮高效互动，能够准确理解用户症状、进行初步分析，并提供有价值的诊断建议和健康指导。
### Innovation
Erkang-Diagnosis-1.1模型在综合医学考试中领先于GPT-4，采用了增强前期训练和检索增强生成的混合方法，整合了大量高质量的结构化医疗知识，确保了安全、可靠性和专业性。
### Conclusion
该模型旨在成为用户的智能健康伴侣，助力初级医疗服务和健康管理。
## 7. `cs.AI` - MegaRAG：基于多模态知识图的检索增强生成 [PDF](https://arxiv.org/pdf/2512.20626), [HTML](https://arxiv.org/abs/2512.20626)
### Authors
Chi-Hsiang Hsiao,Yi-Cheng Wang,Tzung-Sheng Lin,Yi-Ren Yeh,Chu-Song Chen
### Background
检索增强生成（RAG）使大型语言模型（LLMs）能够动态访问外部信息，这在处理以前未见的文档时非常有帮助。然而，由于上下文窗口的限制，它们在高层次概念理解和整体理解方面存在困难。这限制了它们在进行长时间、特定领域的深入推理时的能力，如整本书的全文。知识图谱（KGs）可以提供以实体为中心的结构和分层总结，为推理提供了更多的结构支持。但是，现有基于KG的RAG解决方案仍然局限于纯文本输入，并未能利用来自其他模态（如视觉）的补充见解。
### Innovation
为了应对视觉文档推理所需的文字、视觉和空间线索的问题，我们提出了一个基于多模态知识图的RAG方法，以实现跨模态推理从而提高内容理解。该方法将视觉线索整合到知识图的构建、检索阶段和答案生成过程中。实验结果表明，该方法在全球和细粒度问答任务中，在文本和多模态语料库上的性能都优于现有的RAG方法。
### Conclusion
我们的方法在知识图的构建、检索阶段和答案生成过程中融合了视觉线索，通过跨模态推理提高了内容理解能力。实验结果表明，在各类问答任务中，该方法均优于现有RAG方法，特别是在文本和多模态语料库上的表现更为突出。
## 8. `cs.AI` - Mixture of Attention Schemes (MoAS): Learning to Route Between MHA, GQA, and MQA [PDF](https://arxiv.org/pdf/2512.20650), [HTML](https://arxiv.org/abs/2512.20650)
### Authors
Esmail Gumaan
### Background
Transformer模型中的注意力机制在建模质量和推理效率之间存在关键权衡。虽然多头注意力机制（MHA）在质量上最佳，但在推理过程中需要大量的键值缓存内存。多查询注意力机制（MQA）和分组查询注意力机制（GQA）减少了内存使用，但通常以降低模型性能为代价。
### Innovation
提出了注意力方案混合模型（MoAS），这是一种新颖的架构，通过学习路由器为每个tokens动态选择最优的注意力方案（MHA、GQA或MQA）。研究表明，动态路由在性能上优于静态混合，并且能够与MHA基线性能相当，同时具有潜在的条件计算效率优势。
### Conclusion
在WikiText-2的数据集上实验结果显示，动态路由（验证损失2.3074）优于静态混合（2.3093），验证了该方法的有效性。
## 9. `cs.AI` - BitRL-Light: 1比特大语言模型代理与深度强化学习在智能家庭照明能效优化中的应用 [PDF](https://arxiv.org/pdf/2512.20623), [HTML](https://arxiv.org/abs/2512.20623)
### Authors
Ravi Gupta,Shabista Haider
### Background
智能家庭照明系统消耗了住宅能源的15-20%，但缺乏适应性智能来同时优化用户的舒适度和能源效率。这些系统需要一种新颖的方法来实现这两项需求的平衡。
### Innovation
本文介绍了一种创新框架BitRL-Light，该框架结合了1比特量化的大语言模型（LLMs）和深度Q-网络（DQN）强化学习，用于边缘设备上的实时智能家庭照明控制。该方法使用减少到1比特的Llama-3.2-1B模型，相比全精度模型，节能效率提高了71.4倍，并保持了智能控制能力。通过多目标强化学习，BitRL-Light从用户反馈中学习最佳照明策略，平衡能源消耗、舒适度和昼夜节律对齐。
### Conclusion
实验结果表明，与基于规则的系统相比，BitRL-Light能节省32%的能源，推断延迟在Raspberry Pi 4上小于200ms，并且用户满意度达到95%。系统通过Google Home/IFTTT集成处理自然语言命令，并通过手动覆盖获得隐式反馈进行学习。比较分析显示，与2比特替代品相比，1比特模型在ARM处理器上的速度提高了5.07倍，同时保持了92%的任务准确性。这项工作确立了在资源受限的IoT设备上部署适应性AI的实际框架，使智能家居自动化能够脱离云端依赖，实现智能照明控制而不牺牲准确性和速度。
## 10. `cs.AI` - 微探针：最少数据下的基础模型高效可靠性评估 [PDF](https://arxiv.org/pdf/2512.20630), [HTML](https://arxiv.org/abs/2512.20630)
### Authors
Aayam Bansal,Ishaan Gangwani
### Background
基础模型的可靠性评估通常需要成千上万的评估样本，这使得在真实世界部署时既消耗大量计算资源，又耗时冗长。
### Innovation
提出了一种名为微探针（MicroProbe）的新方法，仅使用100个战略选择的样本点，便能实现全面的基础模型可靠性评估。该方法结合了跨五个关键可靠性维度的策略性提示多样化、先进的不确定性量化和自适应加权技术，以高效地检测潜在的失效模式。
### Conclusion
通过在多种语言模型（GPT-2变体、GPT-2 Medium、GPT-2 Large）以及跨领域验证（医疗、金融、法律）中的广泛实证评估，表明微探针相比于随机采样的基线方法，在综合可靠性评分上提高了23.5%，具有极高的统计显著性（p < 0.001，Cohen's d = 1.21）。由三位AI安全专家进行的验证确认了我们策略性选择的有效性，评分4.14/5.0，而随机选择得分为3.14/5.0。微探针能够以99.9%的统计功效完成可靠性评估，同时减少了90%的评估成本并保持了与传统方法95%的覆盖率。我们的方法填补了负责任的AI部署中高效模型评估的关键缺口。
## 11. `cs.CL` - 测量LLM评估中的所有噪声 [PDF](https://arxiv.org/pdf/2512.21326), [HTML](https://arxiv.org/abs/2512.21326)
### Authors
Sida Wang
### Background
从实验科学的角度来看，从信号中分离噪声是核心任务。在对大规模语言模型（LLM）进行评估时，有效地应用成熟的统计方法需要考虑其独特的噪声特征。
### Innovation
本文通过清晰定义并测量三种类型的噪声：预测噪声（在给定问题上生成多种答案）、数据噪声（通过采样问题产生的噪声）以及其综合噪声，提出了基于成对分析的全部成对方法。该方法基于许多评估和设置中的数百万个问题级别的预测来测量所有噪声成分。
### Conclusion
这些测量揭示了明确的模式。首先，每次评估在所有模型成对情况下都表现出具有高度可预测性的总噪声水平。其次，成对预测噪声通常超过成对数据噪声，这意味着通过平均降低预测噪声可显著提高统计功效。这些发现使实践者能够无需定制测试即可评估显著性，并在受控实验中检测更小的效果。
## 12. `cs.CL` - 可持续管理LLM代理对话中断的检测、解释和升级管道 [PDF](https://arxiv.org/pdf/2504.18839), [HTML](https://arxiv.org/abs/2504.18839)
### Authors
Abdellah Ghassel,Xianzhi Li,Xiaodan Zhu
### Background
大语言模型（LLMs）在对话式AI应用中展现出了强大的能力，但它们在对话中断方面的脆弱性给部署可靠性带来了显著的挑战，并影响了用户的信任。
### Innovation
引入了一种名为“检测、解释、升级”的框架，以有效管理和减轻LLM驱动代理的对话中断问题。该框架结合了两种关键策略：1）微调一个8B参数的小型模型，该模型增加了教师生成的推理踪迹，用于实时对话中断检测和解释；2）系统地使用高级提示（少量样本、推理链，类比推理）评估前沿LLM，用于高保真对话中断评估。通过在必要时将高效检测器升级到更大模型，大幅降低了运营成本和计算负担。
### Conclusion
微调模型和提示策略在DBDC5和BETOLD上实现了最先进的性能，提供了成本效益高且可解释的解决方案，以增强高影响领域的对话式AI的稳健性。代码和模型将会公开发布。
## 13. `cs.CL` - 探索医疗推理中思维预算效率前沿：计算资源与推理质量之间的扩展定律 [PDF](https://arxiv.org/pdf/2508.12140), [HTML](https://arxiv.org/abs/2508.12140)
### Authors
Ziqian Bi,Lu Chen,Junhao Song,Hongying Luo,Enze Ge,Junmin Huang,Tianyang Wang,Keyu Chen,Chia Xin Liang,Zihan Wei,Huafeng Liu,Chunjie Tian,Jibin Guan,Joe Yeong,Yongzhi Xu,Peng Wang,Xinyuan Song,Junfeng Hao
### Background
本研究首次全面评估了思维预算机制在医疗推理任务中的应用，揭示了计算资源和推理质量之间的基本扩展定律。研究系统地评估了两种主要模型家族，包括Qwen3（参数从1.7B到235B）和DeepSeek-R1（参数从1.5B到70B），跨越了15个涉及不同专科和难度水平的医疗数据集。实验通过控制不同思维预算（从零到无限多个token）下的表现，建立了以思想预算和模型大小为基础的泛型扩展关系。
### Innovation
研究发现了三种不同的效率区间：高效率区间（0到256 token）适用于实时应用；平衡区间（256到512 token）提供最优的成本效益折衷，适用于常规临床支持；高精度区间（超过512 token）仅适用于关键诊断任务。研究还发现，小模型从扩展思维中获得了不成比例的更大收益，15到20%的改进相对于大型模型的5到10%，表明思维预算对容量受限的模型提供了更大的相对收益。此外，不同专科显示出明确的差异，神经学和胃肠病学需要更深入的推理过程，而心血管或呼吸医学则需要较少的推理。
### Conclusion
研究结果确立了思维预算控制作为优化医疗AI系统的关键机制，使资源分配能够与临床需求保持一致，同时保持必要的透明度以备医疗部署。
## 14. `cs.CL` - LLM代理中的记忆重思：表示、操作和新兴主题 [PDF](https://arxiv.org/pdf/2505.00675), [HTML](https://arxiv.org/abs/2505.00675)
### Authors
Yiming Du,Wenyu Huang,Danna Zheng,Zhaowei Wang,Sebastien Montella,Mirella Lapata,Kam-Fai Wong,Jeff Z. Pan
### Background
大规模语言模型（LLM）代理的根本在于记忆，但现有的综述主要集中在应用层面的使用上（如个性化对话），忽视了调控记忆动态的原子操作。已有研究没有对记忆的类型进行系统的分类，也未明确界定六大核心操作（整合、更新、索引、遗忘、检索和浓缩）。
### Innovation
本文将记忆分类为参数型（隐含在模型权重中）和上下文型（显式的外部数据，结构化或非结构化），并定义了六大核心操作：整合、更新、索引、遗忘、检索和浓缩。这一分类揭示了四个关键研究领域：长期记忆、多上下文记忆、参数修改和多源记忆。该分类学提供了记忆相关研究、基准和工具的结构化视图，有助于澄清LLM代理的功能交互，并为未来的研究提供指导。
### Conclusion
该分类学提供了一个系统的视角，涵盖了记忆相关的研究、基准和工具。该研究有助于明确LLM代理中记忆的功能交互，并指导未来的研究方向。研究中的数据、论文和工具可以在该网址获取：https://example.com/
## 15. `cs.CL` - 超越上下文：大语言模型未能把握用户意图 [PDF](https://arxiv.org/pdf/2512.21110), [HTML](https://arxiv.org/abs/2512.21110)
### Authors
Ahmed M. Hussain,Salahuddin Salahuddin,Panos Papadimitratos
### Background
当前的大语言模型（LLMs）安全方法主要集中在有害内容防范上，而忽视了一个关键的弱点：无法理解上下文和识别用户意图。这造成了可利用的漏洞，恶意用户可以系统地利用这些漏洞来规避安全机制。我们实证评估了几种先进的LLMs，包括ChatGPT、Claude、Gemini和DeepSeek。我们的分析表明，这些模型可以通过情感框架、逐步揭示和学术论证等技术来绕过可靠的防护机制。研究还发现，具备推理功能的配置并没有减轻这些缺陷的有效性，反而增加了事实的精确度但未能质疑潜在意图。
### Innovation
本研究通过系统地评估当前大语言模型在理解和识别用户意图方面的局限性，证明了基于情感框架、逐步揭示和学术论证等技术的防护机制的失效性。特别指出，具有推理能力的配置不仅未能缓解这些缺陷，反而强化了其事实准确性但未能质疑潜在意图。研究强调，当前的架构设计创建了系统性的漏洞，需要从基于上下文理解和意图识别为核心的安全能力转向，而不是事后防护机制。
### Conclusion
当前的大型语言模型安全方法主要针对显性的有害内容，却忽视了理解上下文和识别用户意图的关键性。这种局限导致了系统性的安全漏洞，需要转变思路，重新构建安全机制以更有效地识别和理解用户意图。
## 16. `cs.CL` - 使用世界知识提高神经问题生成 [PDF](https://arxiv.org/pdf/1909.03716), [HTML](https://arxiv.org/abs/1909.03716)
### Authors
Deepak Gupta,Kaheer Suleman,Mahmoud Adada,Andrew McNamara,Justin Harris
### Background
在自然语言处理领域，神经网络生成问题的技术已经得到了广泛的应用，然而这些模型在生成和人类类似的问题时，缺乏对特定实体和其复杂类型的额外知识的理解和利用，导致生成的问题质量不够理想。本文旨在通过引入世界知识（实体和细粒度的实体类型），进一步提升神经网络生成问题的质量。
### Innovation
本文提出了一种方法，将世界知识（链接实体和细粒度实体类型）融入到神经网络问题生成模型中。这种方法能够捕捉到文本段落中实体间以及实体及其细粒度分类的附加信息，从而生成更接近人类自然语言的问题。实验结果表明，这种方法在SQuAD和MS MARCO数据集上比传统神经网络问题生成模型分别提高了1.37和1.59的BLEU 4分数。
### Conclusion
本文提出的方法和模型在SQuAD和MS MARCO测试数据集上的实验结果证明了，将世界知识融入到问题生成模型中可以有效提升模型生成的问题质量，具有一定的实用价值。
## 17. `cs.CL` - Can Pruning Improve Reasoning? Revisiting Long-CoT Compression with Capability in Mind for Better Reasoning [PDF](https://arxiv.org/pdf/2505.14582), [HTML](https://arxiv.org/abs/2505.14582)
### Authors
Shangziqi Zhao,Jiahao Yuan,Jinyang Wu,Zhenglin Wang,Guisong Yang,Usman Naseem
### Background
现有的长链推理（Long-CoT）虽然能够提高大语言模型（LLMs）的准确率，但由于这种推理过程冗长、自反性强，难以有效压缩成小型语言模型（SLMs）。研究者重新审视Long-CoT压缩，探索通过能力对齐的方式改进推理。
### Innovation
提出了一个结构感知框架——Prune-on-Logic，该框架将Long-CoT转化为逻辑图，并在自我验证约束下选择性地删除低效的推理步骤。通过系统分析三种不同的剪枝策略（针对整个链、核心推理和验证），研究发现验证剪枝能够持续提高准确率并减少令牌使用，而随便剪枝或剪枝推理步骤会降低性能。研究揭示有效的剪枝策略能够实现监督与模型能力的对齐，而不是仅仅缩短输入。
### Conclusion
剪枝策略能显著提升Long-CoT推理与小型语言模型容量之间的匹配，从而在不同的任务、模型规模和Long-CoT能力下提升性能。较大的模型从剪枝中获益更多，因为它们具有更丰富的但更具冗余性的推理。
## 18. `cs.CL` - ReaSeq：通过推理释放世界知识对于序列建模 [PDF](https://arxiv.org/pdf/2512.21257), [HTML](https://arxiv.org/abs/2512.21257)
### Authors
Chuan Wang,Gaoming Yang,Han Wu,Jiakai Tang,Jiahao Yu,Jian Wu,Jianwu Hu,Junjun Zheng,Shuwen Xiao,Yeqiu Yang,Yuning Jiang,Ahjol Nurlanbek,Binbin Cao,Bo Zheng,Fangmei Zhu,Gaoming Zhou,Huimin Yi,Huiping Chu,Jin Huang,Jinzhe Shan,Kenan Cui,Longbin Li,Silu Zhou,Wen Chen,Xia Ming,Xiang Gao,Xin Yao,Xingyu Wen,Yan Zhang,Yiwen Hu,Yulin Wang,Ziheng Bao,Zongyuan Wu
### Background
工业推荐系统在日志驱动的前提下，面临两大根本性限制：1）基于ID的商品表示知识贫乏，导致在数据稀疏情况下兴趣建模脆弱；2）系统性忽视超越日志的用户兴趣，限制了模型在平台边界内的性能。这些限制源于对浅层交互统计和闭环反馈的过度依赖，同时忽视了大型语言模型从大量语料中学到的产品语义和跨域行为模式的丰富世界知识。
### Innovation
引入ReaSeq，一种增强推理框架，通过显式和隐式推理利用大型语言模型的世界知识来解决上述限制。具体而言，ReaSeq 通过多智能体协作进行显式推理，将结构化产品知识提取为语义增强的商品表示，同时利用扩散大型语言模型进行潜在推理以推断可能的超越日志行为。
### Conclusion
ReaSeq 在淘宝的排名系统上部署后取得了显著提升：IPV和CTR提升了超过6.0%，订单量提升了2.9%，以及GMV提升了2.5%，验证了增强世界知识的推理方法相较于纯日志驱动方法的优越性。
## 19. `cs.CL` - 序列到序列奖励建模：通过语言反馈改进RLHF [PDF](https://arxiv.org/pdf/2409.00162), [HTML](https://arxiv.org/abs/2409.00162)
### Authors
Jiayi Zhou,Jiaming Ji,Juntao Dai,Dong Li,Yaodong Yang
### Background
大型语言模型（LLMs）的行为与人类意图和价值观对齐仍然是一个关键挑战。强化学习从人类反馈（RLHF）通过训练奖励模型（RM）对人类偏好进行建模，并微调LLMs以最大化RM反馈来实现对齐。尽管它的有效性和受欢迎程度，但是RLHF容易导致有偏的局部优化， Rewards model无法提供准确反映人类偏好的反馈，导致LLMs探索意外的一般化，并未能实现对齐目标。
### Innovation
本文提出了一种新颖的序列到序列（seq2seq）奖励建模方法。这种方法的关键见解是，从语言反馈中学习而不是标量反馈可以改善RLHF，而无需额外的注释。我们将奖励建模的目标从二进制最大似然估计（MLE）更改为序列MLE。这种方法可以通过无需额外注释、模型或训练阶段来实现更丰富和细粒度的语言反馈。实验表明其有效性，特别是在单轮安全对话中减少拒绝回答的先例，在文本摘要任务中的长回答偏差。
### Conclusion
我们的实验表明seq2seq RM在NLP任务中提高RLHF表现的平均胜率达到了76.9%。进一步分析显示，seq2seq RM即使在分布外提示下，也可以在2B和7B LLM上提高RLHF表现，从而证明了这种方法的有效性。
## 20. `cs.CL` - CAKE: 梯进式和适应性强关键-值缓存移除考虑各层偏好 [PDF](https://arxiv.org/pdf/2503.12491), [HTML](https://arxiv.org/abs/2503.12491)
### Authors
Ziran Qin,Yuchen Cao,Mingbao Lin,Wen Hu,Shixuan Fan,Ke Cheng,Weiyao Lin,Jianguo Li
### Background
大规模语言模型（LLMs）擅长处理长序列，推动了关键-值（KV）缓存的需求增长。尽管最近关于KV缓存移除的努力减轻了推理负担，但这些方法往往无法合理地在具有不同注意力模式的各层之间分配资源。因此，有必要提出一种能够更合理地在各层之间分配KV缓存资源的新方法。
### Innovation
本文引入了Cascading和Adaptive KV Cache Eviction (CAKE)，一种将KV缓存移除问题视为“蛋糕切割问题”的新方法。CAKE通过考虑注意力在空间和时间维度上的动态来评估各层的具体偏好，合理分配各层的缓存大小，并以梯进方式管理内存限制。CAKE还引入了一种新的移除指示器，该指示器考虑了随时间变化的标记重要性，解决了现有方法忽视时间动态性的局限性。
### Conclusion
在LongBench和NeedleBench上的全面实验表明，CAKE仅使用3.2%的KV缓存即可保持模型性能，在各种模型和内存限制下，特别是在低内存设置中，持续优于现有基线。此外，与使用FlashAttention-2处理128K标记上下文的全缓存相比，CAKE在解码延迟方面实现了超过10倍的加速。我们的代码可从此https URL获取。
