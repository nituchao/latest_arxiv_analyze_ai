# 20251226
[![Subscribe_Visitors](https://visitor-badge.laobi.icu/badge?page_id=nituchao.latest_arxiv_analyze_ai_rss)](https://github.com/nituchao/latest_arxiv_analyze_ai)

## 1. `cs.AI` - Erkang-Diagnosis-1.1 技术报告 [PDF](https://arxiv.org/pdf/2512.20632), [HTML](https://arxiv.org/abs/2512.20632)
### Authors
Jianbing Ma,Ao Feng,Zhenjie Gao,Xinyu Song,Li Su,Bin Chen,Wei Wang,Jiamin Wu
### Background
本文报告详细介绍了使用阿里云Qwen-3模型开发的Erkang-Diagnosis-1.1模型，这是一种AI医疗咨询助手。Erkang模型融合了大约500GB高质量结构化医疗知识，采用了增强预训练和检索增强生成相结合的方法，旨在创建一个安全、可靠且专业的AI健康管理顾问。
### Innovation
Erkang-Diagnosis-1.1模型通过3-5轮有效交互，能够准确理解用户症状，进行初步分析，并提供有价值的诊断建议和健康指导。在全面医学考试中，该模型的表现超越了GPT-4。
### Conclusion
Erkang Diagnosis能够作为用户智能健康伴侣，赋能基层医疗和健康管理。
## 2. `cs.AI` - Mixture of Attention Schemes (MoAS): Learning to Route Between MHA, GQA, and MQA [PDF](https://arxiv.org/pdf/2512.20650), [HTML](https://arxiv.org/abs/2512.20650)
### Authors
Esmail Gumaan
### Background
Transformer模型中的注意力机制选择涉及建模质量和推理效率之间的关键权衡。多头注意力机制（MHA）提供最佳质量，但在推理过程中需要大量的键值缓存记忆。多查询注意力机制（MQA）和组查询注意力机制（GQA）减少了内存使用，但往往以模型性能为代价。
### Innovation
我们提出了混合注意力方案（MoAS），这是一种新颖的架构，能够动态地为每个令牌选择最优的注意力方案（MHA、GQA或MQA）。研究显示，动态路由优于静态混合方法，并且在性能上与MHA基准方法相当，同时也具有条件计算效率的潜力。
### Conclusion
在WikiText-2上的实验结果表明，动态路由（验证损失2.3074）优于静态混合（2.3093），这验证了所提出方法的有效性。我们的代码已发布。
## 3. `cs.AI` - MicroProbe：使用最少数据进行基础模型可靠性的高效评估 [PDF](https://arxiv.org/pdf/2512.20630), [HTML](https://arxiv.org/abs/2512.20630)
### Authors
Aayam Bansal,Ishaan Gangwani
### Background
基础模型的可靠性评估通常需要成千上万的评估示例，这使得其实用部署在计算和时间上都非常昂贵。目前的评估方法缺乏高效性和经济性。
### Innovation
提出了一种名为Microprobe的新方法，仅使用100个经过战略选择的探测示例就可以进行全面的可靠性评估。该方法结合了五个关键可靠维度上的策略提示多样性、先进的不确定性量化和自适应加权，从而能够有效探测潜在的失败模式。
### Conclusion
通过在多个语言模型（GPT-2变体、GPT-2中型、GPT-2大型）上进行广泛的实证测试和跨域验证（医疗保健、金融、法律），证明Microprobe相比随机抽样的基线方法，额外可靠性得分提高了23.5%，具有显著的统计意义（p < 0.001，Cohen's d = 1.21）。专家评估证实了该策略选择的有效性，并表明微探针能够在保持95%的传统方法覆盖率的同时将评估成本减少90%，同时保持99.9%的统计效能。该方法填补了负责任的人工智能部署中高效模型评估的关键缺口。
## 4. `cs.AI` - AIAuditTrack: 一种AI安全系统框架 [PDF](https://arxiv.org/pdf/2512.20649), [HTML](https://arxiv.org/abs/2512.20649)
### Authors
Zixun Luo,Yuhang Fan,Yufei Li,Youzhi Zhang,Hengyu Lin,Ziqi Wang
### Background
大规模语言模型驱动的应用程序迅速扩展导致了大量AI交互数据的产生，这引发了安全、问责和风险追溯的紧急挑战。
### Innovation
AIAuditTrack（AAT）提出了一种基于区块链的框架，用于记录和治理AI使用流量。该框架利用分散式身份（DID）和可验证凭证（VC）来建立可信赖且可识别的AI实体，并在区块链上记录实体之间的交互轨迹以实现跨系统监督和审计。AAT通过动态交互图模型中的风险扩散算法来追溯风险行为的源头，并在涉及的实体间传播早期预警。
### Conclusion
使用区块链每秒事务处理量（TPS）指标评估系统性能，证明了AAT在大规模交互记录下的可行性和稳定性。AAT提供了一种可扩展且可验证的解决方案，用于复杂的多代理环境中AI审计、风险管理及责任归属。
## 5. `cs.AI` - BitRL-Light：1比特LLM代理与深度强化学习在高效智能家庭照明优化中的应用 [PDF](https://arxiv.org/pdf/2512.20623), [HTML](https://arxiv.org/abs/2512.20623)
### Authors
Ravi Gupta,Shabista Haider
### Background
智能家庭照明系统占住宅能耗的15-20%，但缺乏智能适应机制，无法同时优化用户舒适度和能效。当前研究旨在开发一个能够实时控制边缘设备中照明系统，并能根据用户反馈优化照明策略的框架。
### Innovation
提出了一种结合1比特量化的大语言模型（1-bit quantized LLMs）与深度Q-网络（DQN）强化学习的新框架——BitRL-Light。该框架在资源受限的物联网设备上部署了一个1比特量化的大语言模型Llama-3.2-1B，实现了比全精度模型71.4倍的能耗降低，同时保持了智能控制能力。通过多目标强化学习，BitRL-Light能够学习到平衡能源消耗、舒适度以及昼夜节律的最优照明策略。
### Conclusion
实验证明，与基于规则的系统相比，BitRL-Light在节能方面有32%的提升，模型推理延迟低于200ms，用户满意度达到95%。该系统通过Google Home/IFTTT集成处理自然语言命令，并通过手动操作获取隐式反馈。对比分析表明，1比特模型在ARM处理器上的加速比为5.07倍，同时保持92%的任务准确性。这项工作证明了在资源受限的物联网设备上部署具备适应性的AI框架的可行性。
## 6. `cs.AI` - 2025年知识、信息与创造力支持系统国际会议(KICSS 2025)的会议论文集 [PDF](https://arxiv.org/pdf/2512.20628), [HTML](https://arxiv.org/abs/2512.20628)
### Authors
Edited by Tessai Hayama(Nagaoka University of Technology, Japan),Takayuki Ito(Kyoto University, Japan),Takahiro Uchiya(Nagoya Institute of Technology, Japan),Motoki Miura(Chiba Institute of Technology, Japan),Takahiro Kawaji(University of Kurume, Japan),Takaya Yuizono(Japan Advanced Institute of Science and Technology, Japan),Atsuo Yoshitaka(Japan Advanced Institute of Science and Technology, Japan),Tokuro Matsuo(Advanced Institute of Industrial Technology, Japan),Shun Okuhara(Mie University, Japan),Jawad Haqbeen(Kyoto University, Japan),Sofia Sahab(Kyoto University, Japan),Wen Gu(Nagoya Institute of Technology, Japan),Shiyao Ding(Kyoto University, Japan)
### Background
本会议是在日本那加日本举行的2025年知识、信息与创造力支持系统国际会议(KICSS 2025)的会议论文集。会议旨在为人工智能、知识工程、人机交互和创造力支持系统等领域研究人员提供一个多学科的交流平台。论文经过双重匿名审查并被接受，之后有选择地推荐到IEICE信息系统事务进行出版。
### Innovation
通过提供一个多学科的交流平台，促进不同领域的学者之间的交流和合作。采用双重匿名审查机制以确保论文质量，并选择性推荐论文至权威期刊进行进一步发表。
### Conclusion
这些会议论文反映了人工智能、知识工程、人机交互和创造力支持系统领域的最新研究成果，为相关领域的进一步发展提供了宝贵的参考。
## 7. `cs.AI` - 数学推理中的推理接力：评估大型语言模型推理稳定性和互换性 [PDF](https://arxiv.org/pdf/2512.20647), [HTML](https://arxiv.org/abs/2512.20647)
### Authors
Leo Lu,Jonathan Zhang,Sean Chua,Spencer Kim,Kevin Zhu,Sean O'Brien,Vasu Sharma
### Background
链式思维（CoT）提示显著提升了大规模语言模型（LLMs）的推理能力。尽管先前的研究主要集中在通过内部推理策略提高模型表现上，很少探讨不同模型之间的推理互换性。本文探索了一种模型完成的部分推理链能否被另一种模型（即使是不同家族的模型）可靠地继续，无论是同一模型家族内还是跨家族。
### Innovation
通过评估中间推理痕迹作为逻辑一致性和最终答案准确性的可转移支撑结构，研究推理解释的互换性作为检查推理时可信度的方式。利用基线模型Gemma-3-4B-IT和LLaMA-3.1-70B-Instruct在token级别对日志概率设置阈值，将推理过程在早期、中期和晚期进行裁剪，并测试了同一家族及跨家族模型的行为。利用过程奖励模型（PRM）评估推理稳定性的评估框架揭示了混合推理链通常能保持甚至提高最终准确性和逻辑结构。
### Conclusion
研究结果表明推理解释的互换性是一个新兴的行为属性，为可靠模块化推理在协作AI系统中的新范式提供了见解。
## 8. `cs.AI` - MegaRAG: 基于多模态知识图谱的检索增强生成 [PDF](https://arxiv.org/pdf/2512.20626), [HTML](https://arxiv.org/abs/2512.20626)
### Authors
Chi-Hsiang Hsiao,Yi-Cheng Wang,Tzung-Sheng Lin,Yi-Ren Yeh,Chu-Song Chen
### Background
检索增强生成（RAG）使大型语言模型（LLMs）能够动态获取外部信息，这在回答以前未见过的文档的问题时非常强大。然而，由于上下文窗口的限制，它们在高层次的概念理解和整体理解方面存在困难，这限制了它们对长篇、领域特定内容（如完整书籍）进行深入推理的能力。现有基于知识图谱（KGs）的RAG解决方案通常仅限于文本输入，未能利用其他模态（如视觉）提供的互补洞察。因此，从视觉文档进行推理需要结合文本、视觉和空间线索，将结构化的、层次的概念融入其中。
### Innovation
我们提出了一个基于多模态知识图谱的RAG方法，该方法能支持跨模态推理，从而更好地理解内容。该方法将视觉线索融入知识图谱的构建过程、检索阶段和回答生成过程中。
### Conclusion
我们的方法在从全球性和细粒度问题回答任务中，在文本和多模态语料库上的一系列实验表明，与现有的基于RAG的方法相比，我们的方法表现更优。
## 9. `cs.AI` - Memory Bear AI: A Breakthrough from Memory to Cognition Toward Artificial General Intelligence [PDF](https://arxiv.org/pdf/2512.20651), [HTML](https://arxiv.org/abs/2512.20651)
### Authors
Deliang Wen,Ke Sun
### Background
大语言模型（LLMs）在记忆方面存在固有的限制，包括有限的上下文窗口、长期知识遗忘、重复信息累积以及虚构生成。这些问题严重限制了长期对话和个性化服务的持续性。
### Innovation
本文提出了Memory Bear系统，该系统基于认知科学原理构建了一个类人类的记忆架构。通过整合多模态信息感知、动态记忆维护和适应性认知服务，Memory Bear实现了LLM记忆机制的全链条重构。实验结果表明，与现有解决方案（如Mem0、MemGPT、Graphiti）相比，Memory Bear在关键指标如准确性、令牌效率和响应延迟等方面表现出色，显著提高了长期对话的知识准确性和检索效率，减少了虚构生成率，并通过记忆认知整合增强了上下文适应性和推理能力。
### Conclusion
Memory Bear为人工智能从记忆向认知发展迈出了关键一步，展示了在健康医疗、企业运营和教育等多个领域的重要工程创新和性能突破。
## 10. `cs.AI` - 基于无人机辅助6G网络部署的量子启发式多智能体强化学习探究 [PDF](https://arxiv.org/pdf/2512.20624), [HTML](https://arxiv.org/abs/2512.20624)
### Authors
Mazyar Taghavi,Javad Vahidi
### Background
本文介绍了一种用于多智能体强化学习中探索与利用权衡优化的量子启发式框架，该框架应用于无人机辅助的6G网络部署。研究背景在于，在复杂、动态的环境中，十个自主协作的智能无人机需要在不完全可观测的条件下协调行动，以最大化信号覆盖并支持网络的高效扩展。
### Innovation
本文创新地结合了经典MARL算法与量子启发式优化技术，采用变分量子电路作为核心结构，并运用量子近似优化算法作为组合优化的代表性方法。通过贝叶斯推断、高斯过程和变分推断等概率建模技术捕捉环境的潜在动态。研究采用集中训练分散执行的范式，并通过共享记忆和局部视图网格增强智能体间的局部观察性。实验结果表明，所提出的框架提高了样本效率，加速了收敛，增强了覆盖性能，同时保持了鲁棒性。通过雷达图和收敛性分析进一步表明，量子启发式MARL相比经典方法实现了更好的探索与利用之间的平衡。
### Conclusion
本研究表明，量子启发式多智能体强化学习框架在无人机辅助6G网络部署中的应用，能够有效提高探索与利用的平衡。通过公开研究中的全部实现代码和补充材料，确保了结果的可复制性。
## 11. `cs.LG` - 通过缺陷矫正物理知情的高维偏微分方程求解缩放推理时间方法 [PDF](https://arxiv.org/pdf/2504.16172), [HTML](https://arxiv.org/abs/2504.16172)
### Authors
Zexi Fan,Yan Sun,Shihao Yang,Yiping Lu
### Background
高维偏微分方程（PDEs）的求解是一个重要挑战，现代数据驱动的求解器往往缺乏可靠性及严格的误差保证。
### Innovation
提出了一种名为 Simulation-Calibrated Scientific Machine Learning (SCaSML) 的框架，该框架在无需重新训练的情况下，系统地改善预训练的 PDE 求解器在推理时间的表现。核心思想是使用缺陷矫正方法推导出一个新的 PDE，称为结构保持缺陷定律，精确描述给定代理模型的误差。这种方法保留了原始问题的结构，可以利用传统的随机模拟器高效求解，并对初始的机器学习解决方案进行纠正。
### Conclusion
在160个维度的挑战性PDEs上，SCaSML 降低了多种代理模型（包括 PINNs 和高斯过程）的误差，降低了20-80%。证明 SCaSML 达到了更快的收敛速度，并且最终误差被代理误差和模拟误差的乘积所界定了。SCaSML 的代码可在此获取：this https URL.
## 12. `cs.LG` - Optimal Model Selection for Conformalized Robust Optimization [PDF](https://arxiv.org/pdf/2507.04716), [HTML](https://arxiv.org/abs/2507.04716)
### Authors
Yajie Bao,Yang Hu,Haojie Ren,Peng Zhao,Changliang Zou
### Background
在不确定性决策中，Contextual Robust Optimization (CRO) 通过在预测集内最小化最坏情况的决策损失来提供可靠性。而最近的研究使用同态预测来构建机器学习模型的预测集，但下游决策高度依赖于模型选择。
### Innovation
本文引入了新型的CRO模型选择框架，将鲁棒性控制与决策风险最小化统一。提出了Conformalized Robust Optimization with Model Selection (CROMS) 框架，选取约最小化CRO解决方案的平均决策风险的模型。给出了E-CROMS，一种高效的算法，实现了渐近鲁棒性控制和决策最优性。为进一步矫正样本有限情况下的控制偏差，提出了F-CROMS和J-CROMS算法，并扩展CROMS框架至个体化设置，通过最小化协变量条件下的决策风险进行模型选择。
### Conclusion
数值结果表明，在从合成到真实世界的多种应用中，这些方法在决策效率方面取得了显著改进，并优于基准方法。此外，该框架通过实现协变量感知的模型选择，推进了同态预测方法的发展。
## 13. `cs.LG` - MatchMiner-AI: 开源解决方案用于癌症临床试验匹配 [PDF](https://arxiv.org/pdf/2412.17228), [HTML](https://arxiv.org/abs/2412.17228)
### Authors
Jennifer Altreuter,Pavel Trukhanov,Morgan A. Paul,Michael J. Hassett,Irbaz B. Riaz,Muhammad Umar Afzal,Arshad A. Mohammed,Sarah Sammons,James Lindsay,Emily Mallaber,Harry R. Klein,Gufran Gungor,Matthew Galvin,Michael Deletto,Stephen C. Van Nostrand,James Provencher,Joyce Yu,Naeem Tahir,Jonathan Wischhusen,Olga Kozyreva,Taylor Ortiz,Hande Tuncer,Jad El Masri,Alys Malcolm,Tali Mazor,Ethan Cerami,Kenneth L. Kehl
### Background
癌症治疗和结果的改进依赖于临床试验，然而大多数癌症患者并未参与其中，且临床试验往往因患者人数不足而无法完成。人工智能（AI）可用于加速对患者的适应症研究，但由于数据限制，未允许训练AI模型并共享其在患者记录上的成果。
### Innovation
开发了一个名为MatchMiner-AI的开源平台，基于合成数据训练，用于临床试验搜索和排名。该平台能够从患者的长期电子健康记录中提取关键历史信息，并快速排序试验和患者的匹配情况。此外，平台还能够预测患者是否符合标准排除条件，如器官功能障碍等。
### Conclusion
MatchMiner-AI平台通过使临床试验匹配过程更加高效和自动化，能够帮助更准确地将患者与合适的临床试验匹配，促进临床研究的发展。
## 14. `cs.LG` - 神经动态数据估值：随机最优控制方法 [PDF](https://arxiv.org/pdf/2404.19557), [HTML](https://arxiv.org/abs/2404.19557)
### Authors
Zhangyong Liang,Ji Zhang,Xin Wang,Pengfei Zhang,Zhao Li
### Background
数据估值已经成为现代数据经济的基石，数据集作为可交易的知识产权，驱动决策制定、模型训练和市场交易。尽管有了显著进展，现有的估值方法仍然受到高计算成本、弱公平保证和解释性差的限制，阻碍了其在大规模、高风险应用中的部署。
### Innovation
本文引入了神经动态数据估值（NDDV），这是一种新的框架，将数据估值形式化为一个随机最优控制问题以捕捉数据效用随着时间动态演变。NDDV 通过反映个体和集体学习动态的连续轨迹来建模数据交互，而不是静态组合方法。
### Conclusion
通过将数据估值问题表述为随机最优控制问题，NDDV 能够更好地捕捉数据效用的动态变化，同时提供更好的交互建模和解释性，有望在大规模、高风险数据决策中得到广泛应用。
## 15. `cs.LG` - AutoAdv：大规模语言模型多轮攻击的自动化对抗性提示生成 [PDF](https://arxiv.org/pdf/2507.01020), [HTML](https://arxiv.org/abs/2507.01020)
### Authors
Aashray Reddy,Andrew Zagula,Nicholas Saban
### Background
大型语言模型（LLMs）仍然存在受到脱壳攻击的漏洞：精心设计的恶意输入旨在规避安全防护措施并引发有害响应。因此，本文提出了一种名为AutoAdv的新框架，该框架能自动化对抗性提示生成以系统性地评估和暴露LLM安全机制的漏洞。
### Innovation
AutoAdv框架通过参数化的攻击LLM生产语义伪装的恶意提示，运用策略重写技术、专项系统提示和优化超参数配置。主要贡献是动态的、多轮次的攻击方法，该方法分析脱壳失败并迭代生成优化的后续提示，利用诸如角色扮演、误导和语境操纵等技术。通过使用StrongREJECT框架对最新模型进行定量评估，包括ChatGPT、Llama和DeepSeek，自动攻击实现了高达86%的有害内容生成脱壳成功率。
### Conclusion
我们的研究揭示了当前安全机制对复杂的多轮攻击依然保持脆弱性，强调了应立即采取更稳健的防御策略的必要性。
## 16. `cs.LG` - Agnostic Process Tomography [PDF](https://arxiv.org/pdf/2410.11957), [HTML](https://arxiv.org/abs/2410.11957)
### Authors
Chirag Wadhwa,Laura Lewis,Elham Kashefi,Mina Doosti
### Background
研究量子系统的学习状态或演化是量子物理和机器学习理论中的一个基本问题，具有广泛的应用。最近，作为一种新方法，无假设态重构被定义，旨在通过简化形式逼近未知量子态。进一步将此概念推广到量子过程，本文首次探讨无假设过程重构的任务。给定未知量子通道$boldsymbol{boldsymbol{text{Φ}}}$和已知的知识通道概念类$boldsymbol{text{C}}$，目标是输出一个近似$boldsymbol{text{Φ}}$的最佳量子通道，使得其与概念类$boldsymbol{text{C}}$中的任意通道误差最小。
### Innovation
本文提出了一种新的无假设过程重构任务，其创新点在于引入了给定知识通道概念类的方向，旨在最大范围地逼近未知的量子通道，并提出了适用于多种概念类的有效算法，包括Pauli字符串、Pauli通道、量子共轭通道、低阶通道以及$boldsymbol{text{QAC}^{0}}$电路生成的通道。通过使用算子和超算子的Pauli谱分析技术，本文解决了广泛的概念类无假设过程重构问题，并证明了利用辅助比特可以将任何无假设态重构算法扩展为解决兼容概念类中的任何会话重构问题，从而为克利福德电路、带少量$boldsymbol{text{T}}$门的克利福德电路及单比特运算电路的无假设学习提供了有效的算法。
### Conclusion
本文研究成果揭示了从标准结构化设置扩展到无假设重构所需的条件和新算法，并为量子机器学习、量子计量学、经典模拟和错误缓解等领域的应用提供了新的视角和方法。
## 17. `cs.LG` - 通过交互式提问进行逆强化学习以引导风险厌恶 [PDF](https://arxiv.org/pdf/2308.08427), [HTML](https://arxiv.org/abs/2308.08427)
### Authors
Ziteng Cheng,Anthony Coache,Sebastian Jaimungal
### Background
本文研究了罗bo顾问估计非专家客户风险厌恶量的框架，利用自适应二元选择问卷。在静态背景下，使用成本函数和光谱风险度量建模风险厌恶。证明了有限样本识别性，并在适当设计的问题下，得到了每平方根N的收敛率，其中N是问题的数量。
### Innovation
引入了区分力量的概念，并通过模拟实验表明，通过最大化区分力量设计问题可以在不到50个问题的情况下获得满意的准确性。此外，还对具有额外折扣因子的无限期背景下动态风险厌恶进行了初步研究，证明了这种情况下定量识别的可能性。
### Conclusion
本文研究了一种通过交互式提问利用逆强化学习估计客户风险厌恶的方法，证明了有限样本识别性和适当的收敛率。通过模拟实验验证了通过最大化区分力量设计问题的有效性，并初步探索了动态风险厌恶的可识别性。
## 18. `cs.LG` - 序列变化点定位检测后的推断 [PDF](https://arxiv.org/pdf/2502.06096), [HTML](https://arxiv.org/abs/2502.06096)
### Authors
Aytijhya Saha,Aaditya Ramdas
### Background
这篇论文聚焦于序列变化点分析中的一个基础但尚未充分研究的挑战：在检测到变化后进行推断。传统的序列变化点分析主要集中在检测变化点，而忽视了变化点检测后对变化点的具体推断，尤其是在检测停止时间依赖于所用序列检测算法的情况。本文旨在填补这一空白。
### Innovation
论文提出了一个非常通用的框架，用于仅使用检测停止时间（该停止时间依赖于任意的顺序检测算法）之前观测到的数据来构造未知变化点的置信集。该框架非参数化，适用于复合后变化类别、观测空间以及所使用的序列检测程序，且是非渐近有效的。此外，该框架还扩展到处理在适当假设下的复合前变化类别，并推导了参数设置下的变化幅度的置信集。提供了对置信区间的宽度的理论保证。
### Conclusion
实验证明生成的置信集具有合理的大小和轻微保守的覆盖率。总之，本文提供了首个针对序列变化点定位的通用方法，理论上可靠，且在实践中应用广泛。
## 19. `cs.LG` - 学习增强的集成滤波器 [PDF](https://arxiv.org/pdf/2504.17836), [HTML](https://arxiv.org/abs/2504.17836)
### Authors
Eviatar Bach,Ricardo Baptista,Edoardo Calvello,Bohan Chen,Andrew Stuart
### Background
在隐马尔可夫模型中，滤波分布遵循状态观测量空间中的均值场模型的规律。通常使用的资料同化方法，如集合卡尔曼滤波（EnKF），通过一组相互作用的粒子来近似均值场模型，并假设状态和观测在每次观测时间步的联合分布是高斯分布。这些方法在实际应用中具有鲁棒性，但该高斯假设限制了其准确性。
### Innovation
本文通过使用机器学习将联合预测的状态和观测映射到更新的状态估计，解决了高斯假设的局限性。并提出了一种新的神经运算形式——度量神经映射（MNM），用于集成滤波器的新框架。这种方法不仅在均值场极限中定义，还在有限交互粒子的近似中得到应用。实验表明，相对于领先的滤波方法，该方法在洛伦兹 '96 和库拉托夫斯基-希瓦什模型的滤波性能方面具有更好的均方根误差表现。
### Conclusion
研究提出了一种基于均值场方法的集成滤波器，通过MNM增强了集成滤波器的准确性。该方法同时适用于均值场极限和交互粒子的近似，并且通过少量参数的微调可进一步提高其性能。
## 20. `cs.LG` - EEG基础模型：当前进展和未来方向的批判性评述 [PDF](https://arxiv.org/pdf/2507.11783), [HTML](https://arxiv.org/abs/2507.11783)
### Authors
Gayal Kuruppu,Neeraj Wagh,Vaclav Kremen,Sandipan Pati,Gregory Worrell,Yogatheesan Varatharajah
### Background
脑电图（EEG）活动记录的电生理模式对于科学研究和临床研究具有巨大价值。然而，监督学习的EEG编码器难以学习稳健的EEG模式，并且对昂贵的信号注释过度依赖，促使转向通用的自我监督EEG编码器，即EEG基础模型（EEG-FMs），以实现稳健和可扩展的EEG特征提取。尽管早期的EEG-FMs在实际应用中的准备状态和长期研究进展仍不明朗，但已有研究正在逐步推进。
### Innovation
本文对10种早期EEG-FMs进行了回顾，通过三个基础建模支柱（输入数据表示、自我监督建模和评估策略）进行比较分析，揭示了EEG-FMs的常见模式和关键发展方向。研究发现大多数EEG-FMs采用基于序列的建模方案，并依赖于变压器骨干和掩蔽时间序列EEG的重建进行自我监督。未来研究应注意标准化和现实的评估、展示更显著的扩展效果并确保整条EEG表示学习管道中的原则性和可靠性选择。
### Conclusion
本文的研究结果表明，与领域专家合作制定基准、软件工具、技术和应用，可以提高EEG-FMs的转化质量和实际应用程度。
