# 20251129
[![Subscribe_Visitors](https://visitor-badge.laobi.icu/badge?page_id=nituchao.latest_arxiv_analyze_ai_rss)](https://github.com/nituchao/latest_arxiv_analyze_ai)

## 1. `cs.AI` - AssurAI：构建韩语社会文化数据集以发现生成式人工智能潜在风险的经验 [PDF](https://arxiv.org/pdf/2511.20686), [HTML](https://arxiv.org/abs/2511.20686)
### Authors
Chae-Gyun Lim,Seung-Ho Han,EunYoung Byun,Jeongyun Han,Soohyun Cho,Eojin Joo,Heehyeon Kim,Sieun Kim,Juhoon Lee,Hyunsoo Lee,Dongkun Lee,Jonghwan Hyeon,Yechan Hwang,Young-Jun Lee,Kyeongryul Lee,Minhyeong An,Hyunjun Ahn,Jeongwoo Son,Junho Park,Donggyu Yoon,Taehyung Kim,Jeemin Kim,Dasom Choi,Kwangyoung Lee,Hyunseung Lim,Yeohyun Jung,Jongok Hong,Sooyohn Nam,Joonyoung Park,Sungmin Na,Yubin Choi,Jeanne Choi,Yoojin Hong,Sueun Jang,Youngseok Seo,Somin Park,Seoungung Jo,Wonhye Chae,Yeeun Jo,Eunyoung Kim,Joyce Jiyoung Whang,HwaJung Hong,Joseph Seering,Uichin Lee,Juho Kim,Sunna Choi,Seokyeon Ko,Taeho Kim,Kyunghoon Kim,Myungsik Ha,So Jung Lee,Jemin Hwang,JoonHo Kwak,Ho-Jin Choi
### Background
生成式人工智能的快速发展迫切需要进行严格的安全性评估。然而，目前的安全数据集主要聚焦于英语，无法全面捕捉非英语语境中的具体风险，尤其是韩国的社会文化背景下的风险。这些现有数据集通常仅限于文本模态。
### Innovation
本文介绍了一种名为AssurAI的新颖的质量控制韩语文本、图像、视频和音频多模态数据集，用于评估生成式人工智能的安全性。该数据集包含35个由多学科专家定义的独特人工智能风险因素，并通过专家主导的种子和群众外包扩展构建，三重独立注释和迭代专家红队循环来确保数据质量。
### Conclusion
我们的初步研究证实了AssurAI在评估现代语言模型安全性方面的有效性。为了推动韩国社区的更安全和更可靠的生成式人工智能系统的开发，我们向公众发布了AssurAI。
## 2. `cs.AI` - Amazon CoT框架下不同数据集的跨域评估 [PDF](https://arxiv.org/pdf/2511.20701), [HTML](https://arxiv.org/abs/2511.20701)
### Authors
Nitya Tiwari,Parv Maheshwari,Vidisha Agarwal
### Background
现有工作虽然将CoT扩展到了多模态设置，并在ScienceQA等科学问题回答基准上取得了最先进的结果，但这些方法在不同领域的泛化能力仍未得到充分探索。
### Innovation
本文通过将Zhang et al. [3]提出的双阶段框架应用于A-OKVQA、OKVQA和ChartQA数据集，系统分析了多模态CoT推理的有效性，该框架分离了推理生成和答案推理，并通过门控融合机制将视觉特征与基于T5的语言模型相结合。通过系统的消融研究，分析了视觉特征、推理质量及架构选择的贡献。
### Conclusion
研究发现，尽管视觉信息的整合显著减少了推理生成中的幻觉，但CoT推理的效果在不同问题类型上差异很大，尤其是在常识推理方面存在特殊挑战。该工作为研究人员实现多模态推理系统提供了实际指导意见，并确定了跨域泛化的关键改进领域。
## 3. `cs.AI` - Representation Interventions Enable Lifelong Unstructured Knowledge Control [PDF](https://arxiv.org/pdf/2511.20892), [HTML](https://arxiv.org/abs/2511.20892)
### Authors
Xuyuan Liu,Zhengzhang Chen,Xinshuai Dong,Yanchi Liu,Xujiang Zhao,Shengyu Chen,Haoyu Wang,Yujun Yan,Haifeng Chen
### Background
大型语言模型（LLMs）常常会产生错误或过时的内容。高效且准确地更新它们的知识库，而无需昂贵的重新训练，这是一项重大挑战。在终身学习的环境中，这种问题尤为突出，因为这里需要维护大量不相互干扰的知识编辑。
### Innovation
本文提出了RILKE（Representation Intervention for Lifelong KnowledgE Control），一种鲁棒且可扩展的方法，将知识控制视为模型表示空间内的干预措施。RILKE利用表示空间的表达能力，识别出两种特性，使它能够细致地控制复杂的非结构化知识，同时保持广泛的应用性。在训练阶段，RILKE学习到能够限制每次更新到低维子空间的重述稳健和编辑本地化模块，从而最小化编辑间的干扰。在推理阶段，查询自适应路由器选择合适的模块来引导模型生成。RILKE在知识编辑基准中表现出高度的编辑成功率、强大的重述泛化能力，并且在适度的内存开销下保持了通用实用性。
### Conclusion
这些结果表明，RILKE是一种有效且可扩展的解决方案，用于LLMs中的终身知识控制。
## 4. `cs.AI` - ‘Reasoning With a Star: A Heliophysics Dataset and Benchmark for Agentic Scientific Reasoning’ [PDF](https://arxiv.org/pdf/2511.20694), [HTML](https://arxiv.org/abs/2511.20694)
### Authors
Kevin Lee,Russell Spiewak,James Walsh
### Background
在太阳物理学中利用大规模语言模型进行科学推理不仅仅是记忆事实，还需要融入物理假设、保持一致的单位以及通过协调方法提供清晰的科学格式。面对这些挑战，该研究介绍了‘Reasoning With a Star’这一新贡献的太阳物理学数据集，并提供了一个初步的基准测试方法。
### Innovation
研究提出了一个名为‘Reasoning With a Star’的新数据集，该数据集来源于美国宇航局与大气研究大学联合项目中的问题集合，并构建成了易于使用的问答结构，包括问题背景、推理步骤、预期答案类型、真实目标、格式提示和元数据。此外，该研究还使用了一个基于程序的评分器，通过单位感知的数值宽容性、符号等价性和模式验证来检查预测。研究还初步评估了一种单模式基准和四种多代理模式，发现通过系统工程原则分解工作流优于直接提示，特别是在需要演绎推理而非纯粹归纳记忆的问题上。
### Conclusion
研究通过‘Reasoning With a Star’数据集和初步基准测试方法，提高了大规模语言模型在太阳物理学中进行科学推理的能力，并展示了通过系统工程分解工作流比直接提示更有效的方法。
## 5. `cs.AI` - 使用LLM指导的层级重构最小化双曲嵌入失真 [PDF](https://arxiv.org/pdf/2511.20679), [HTML](https://arxiv.org/abs/2511.20679)
### Authors
Melika Ayoughi,Pascal Mettes,Paul Groth
### Background
双曲几何是一种有效的嵌入层次数据结构的方法，在机器学习中，特别是数据具有层级组织或由层级语义支配的应用场景中，双曲学习变得越来越重要，例如推荐系统和计算机视觉。双曲嵌入的质量与输入层次结构的结构密切相关，通常源自知识图谱或本体。研究发现，为了获得最佳的双曲嵌入，高分支因子和单一继承是关键，而嵌入算法对不平衡和层级大小不敏感。为了帮助知识工程师重新组织知识层次结构，该研究探索了大型语言模型（LLM）是否有能力自动重构层次结构以满足这些标准。
### Innovation
提出了一种基于提示的方法，使用LLM重构现有的层次结构，以满足双曲嵌入的已知标准。实验结果显示，通过LLM重构的层次结构在多个标准嵌入质量度量标准上相对于现有层次结构具有更高的质量。此外，展示了通过LLM指导的层级重构实现可解释的重新组织，为知识工程师提供解释。
### Conclusion
通过LLM指导的层级重构显著提高了双曲嵌入的质量，并为知识工程师提供了一种可解释的重新组织方法，通过这种方法能够为嵌入优化的层次结构提供合理化的依据。
## 6. `cs.AI` - 神经元的保证最优成分解释 [PDF](https://arxiv.org/pdf/2511.20934), [HTML](https://arxiv.org/abs/2511.20934)
### Authors
Biagio La Rosa,Leilani H. Gilpin
### Background
尽管神经元是深度神经网络的基本单位，但它们学习的内容以及它们的知识是否与人类的知识相一致尚不清楚。成分解释旨在通过逻辑规则来描述神经元激活和概念之间的空间对齐，这一过程通常通过遍历所有可能的概念组合来计算。但由于整个状态空间中的空间对齐计算量过大，文献中通常采用_beam搜索_来限制空间。然而，_beam搜索_无法提供任何最优性理论保证，且不清楚当前的解释距离真实最优解有多接近。
### Innovation
本文通过引入第一个计算保证最优成分解释的框架解决了上述问题，该框架包含三项创新：（i）分解了影响空间对齐的因素，（ii）提出了一种估计搜索过程中任意阶段对齐性的启发式方法，（iii）首次提出了可以在合理时间内计算出最优成分解释的算法。通过这一框架，作者分析了成分解释中最具争议的场景，即计算机视觉领域和卷积神经网络，并展示了当涉及重叠概念时，使用_beam搜索_获得的解释中有10-40%是次优的。最后，作者评估了根据所提出分解和启发式方法引导的_beam搜索_变种，结果显示这种方法在满足或改善运行时间的同时提供了更高灵活性的超参数和计算资源。
### Conclusion
实验结果表明，当前使用的_beam搜索_方法可能无法保证最优性。通过采用新框架，非_beam搜索_的解释能获得更高的灵活性，并在超参数和计算资源方面具有优势。
## 7. `cs.AI` - 通过LLM代理和形式推理实现可信赖的法律AI [PDF](https://arxiv.org/pdf/2511.21033), [HTML](https://arxiv.org/abs/2511.21033)
### Authors
Linze Chen,Yufan Cai,Zhe Hou,Jinsong Dong
### Background
法律的合理性体现在实质合理性（公平或道德正当的结果）和形式合理性（法律决定必须遵循明确的一般逻辑规则）两方面。现有的基于大语言模型（LLM）的系统擅长表面级文本分析，但在原则性法学理论方面缺乏必要的保证。因此，需要一种结合自然语言解释灵活性和符号验证严谨性的方法。
### Innovation
提出了一种名为L4M的新框架，该框架结合了对抗性的LLM代理和基于SMT求解器的证明，以将自然语言的理解灵活性和符号验证的严谨性结合起来。该体系包括三个阶段：（1）法规形式化，通过领域特定提示将法律法规转化为逻辑公式；（2）双事实和法规提取，检察官和辩护方的LLM分别独立地将案件叙述映射到事实元组和法规，确保角色隔离；（3）以求解器为中心的司法审判，通过自动形式化解编译双方论点为逻辑约束，通过不可满足核心触发迭代自我批评直到获得可满足公式，最后由法官LLM转化为透明判决并优化刑罚。
### Conclusion
在公共基准上的实验证明了该系统超过了包括GPT-o4-mini、DeepSeek-V3和Claude 4在内的高级LLM以及最先进的法律AI基线，同时提供了严格的且可解释的符号证明。
## 8. `cs.AI` - 借助大型语言模型在Agentic AI Wi-Fi中学习多接入点协调 [PDF](https://arxiv.org/pdf/2511.20719), [HTML](https://arxiv.org/abs/2511.20719)
### Authors
Yifan Fan,Le Liang,Peng Liu,Xiao Li,Ziyang Guo,Qiao Lan,Shi Jin,Wen Tong
### Background
多接入点协调（MAPC）是提升下一代Wi-Fi在密集重叠基本服务集内的吞吐量的关键技术。然而，现有的MAPC协议依赖于静态的、协议定义的规则，这限制了它们适应动态网络条件（如变化的干扰水平和拓扑结构）的能力。
### Innovation
该文提出了一种新的基于代理的AI WiFi框架，其中每个接入点被建模为一个自主的大语言模型代理，可以协同推理网络状态并在实时环境下协商适应性协调策略。通过认知流程实现动态协作，代理利用自然语言对话，结合集成记忆、反思和工具使用，使其决策扎根于过往经验和环境反馈。
### Conclusion
全面的模拟结果显示，该代理框架成功学习了适应多种动态网络环境的能力，显著优于最先进的空间重用基线。这验证了其作为未来无线网络中稳健和智能解决方案的潜力。
## 9. `cs.AI` - 数字孪生技术简史 [PDF](https://arxiv.org/pdf/2511.20695), [HTML](https://arxiv.org/abs/2511.20695)
### Authors
Yunqi Zhang,Kuangyu Shi,Biao Li
### Background
数字孪生技术源自20世纪60年代NASA的航天器模拟，随着工业领域的应用发展，在医疗健康领域引发变革。数字孪生是一种动态的、数据驱动的物理系统虚拟副本，通过实时数据流进行持续更新，并能实现双向交互。在医学上，数字孪生整合成像、生物传感器和计算模型，生成患者特异性仿真，支持诊断、治疗规划和药物研发。
### Innovation
当前，数字孪生在心脏病程仿真预测治疗效果、肿瘤学跟踪肿瘤进展和优化放射治疗、药理学加速药物发现等方面有着代表性应用。然而，互操作性、数据隐私及模型精度等重大挑战阻碍了其在临床中的广泛应用。新兴解决方案如可解释的人工智能、联邦学习和统一的监管框架提供了前进的可能。
### Conclusion
未来，多器官数字孪生、基因组整合以及道德治理的进展将确保数字孪生从业后治疗转向预测、预防和真正意义上的个性化医学。
## 10. `cs.AI` - Paraconsistent-Lib: 一个直观的PAL2v算法Python库 [PDF](https://arxiv.org/pdf/2511.20700), [HTML](https://arxiv.org/abs/2511.20700)
### Authors
Arnaldo de Carvalho Junior,Diego Oliveira da Cruz,Bruno da Silva Alves,Fernando da Silva Paulo Junior,João Inacio da Silva Filho
### Background
本文介绍了一个名为Paraconsistent-Lib的开源Python库，用于构建推理和决策系统中的PAL2v算法。该库旨在提供PAL2v标准计算的一般性库，并提供三种类型的结果：12个经典格PAL2v区域之一的参数矛盾分析结果、参数矛盾分析节点（PAN）输出，以及决策输出。
### Innovation
Paraconsistent-Lib允许用户以独立形式或网络形式编写一些著名的PAL2v算法，如Para-analyzer、ParaExtrCTX、PAL2v Filter、参数矛盾分析网络（PANnet）和参数矛盾神经网络（PNN），从而降低了复杂性、代码大小和bug的数量。该库还处于活跃开发中，以响应用户在GitHub上提出的功能要求和改进。
### Conclusion
鉴于其稳定状态，Paraconsistent-Lib被用作响应用户需求的功能和改进的开发平台，旨在使开发者轻松地构建基于PAL2v算法的推理和决策系统。
## 11. `cs.AI` - A²Flow: 利用自我适应抽象算子实现代理工作流程自动化生成 [PDF](https://arxiv.org/pdf/2511.20693), [HTML](https://arxiv.org/abs/2511.20693)
### Authors
Mingming Zhao,Xiaokang Wei,Yuanqi Shao,Kaiwen Zhou,Lin Yang,Siwei Rao,Junhui Zhan,Zhitang Chen
### Background
大型语言模型（LLMs）在自动化设计代理工作流方面展示了很强的潜力，但当前方法仍然高度依赖手动预定义的操作，这限制了它们的应用范围和可扩展性。
### Innovation
提出了一种名为 $A^2Flow$ 的完全自动化框架，基于自我适应抽象算子。$A^2Flow$ 采用了三阶段操作提取过程：1) 案例驱动的初始操作生成；2) 操作聚类和初步抽象；3) 深度提取执行抽象操作。此外，通过引入算子记忆机制增强节点级工作流搜索，以保留历史输出，丰富上下文并改进决策。
### Conclusion
在通用和具身基准测试上，$A^2Flow$ 较现有最佳基线模型平均性能提升 2.4%，延迟降低 19.3%，资源利用率降低了 37%。
## 12. `cs.AI` - OpenApps：通过模拟环境变化来衡量UI代理可靠性 [PDF](https://arxiv.org/pdf/2511.20766), [HTML](https://arxiv.org/abs/2511.20766)
### Authors
Karen Ullrich,Jingtong Su,Claudia Shi,Arjun Subramonian,Amir Bar,Ivan Evtimov,Nikolaos Tsilivis,Randall Balestriero,Julia Kempe,Mark Ibrahim
### Background
自主UI代理（直接以人类方式与应用交互的多模态代理）的可靠性是其实现预期的关键。当前的评估方法依赖于固定的环境，这些环境通常是现有应用的克隆，限制了它们只能光照特定环境内代理完成任务的频率。当实际部署时，代理可能会遇到应用设计和内容的变化，这些变化可能会影响代理完成任务的能力。
### Innovation
为了弥合衡量代理在其变体应用之间的可靠性这一盲点，研究开发了OpenApps，这是一种轻量级的开源生态系统，其中包括六个可以配置外观和内容的应用（例如，聊天应用、日历、地图等）。OpenApps只需要单个CPU即可运行，这使得生成和部署成千上万的应用版本变得容易。通过运行超过10,000次独立的评估，研究发现，即使在固定应用内的标准可靠性是相对稳定的，可靠性在测量其应用变体之间时会大幅波动。许多代理的任务成功率在不同应用版本间可以波动超过50%。这些发现强调了在这一新的应用变化维度上衡量可靠性的重要性。
### Conclusion
研究表明，代理行为在不同环境配置下差异巨大，这些初步发现强调了衡量可靠性在新维度上的重要性。OpenApps已经在GitHub上开源，可用作验证UI代理在不同应用环境变体中可靠性的工具。
## 13. `cs.AI` - OVOD-Agent: 一种用于主动视觉推理和自我进化检测的马尔可夫-臂制导框架 [PDF](https://arxiv.org/pdf/2511.21064), [HTML](https://arxiv.org/abs/2511.21064)
### Authors
Chujie Wang,Jianyu Lu,Zhiyuan Luo,Xi Chen,Chu He
### Background
开放词汇对象检测（OVOD）旨在通过利用语义信息使检测器在类别间泛化。尽管现有方法在大规模视觉-语言数据集上进行了预训练，但在推断时仍局限于固定类名，导致多模态训练与单模态推断之间存在差距。先前研究表明，改进文本表示可以显著提高OVOD性能，表明文本空间仍有待探索。现有工作主要集中在改进文本表示，但仍存在提升空间。
### Innovation
本文提出了OVOD-Agent，它将被动类别匹配转变为主动视觉推理和自我进化检测。OVOD-Agent借鉴了Chain-of-Thought（CoT）范式，将文本优化过程扩展为具显式动作的可解释视觉-CoT。作者通过将视觉上下文转换为八个状态空间上的弱马尔可夫决策过程（w-MDP）来建模视觉上下文转换，以自然地表示代理状态、记忆和交互动态。另外，Arm模块在有限监督下生成探索信号，帮助代理聚焦于不确定区域并调整检测策略。此外，该论文还结合了马尔可夫转移矩阵和Arm轨迹，实现了自助奖励模型（RM）的优化，形成了从Arm探索到RM学习的闭环。
### Conclusion
实验结果表明，OVOD-Agent在COCO和LVIS数据集上的一系列OVOD骨干模型中一致地提供了改进，特别是在稀有类别上显示出显着的有效性，证实了所提出框架的有效性。
## 14. `cs.AI` - EWE: 一种用于极端天气分析的智能代理框架 [PDF](https://arxiv.org/pdf/2511.21444), [HTML](https://arxiv.org/abs/2511.21444)
### Authors
Zhe Jiang,Jiong Wang,Xiaoyu Yue,Zijie Guo,Wenlong Zhang,Fenghua Ling,Wanli Ouyang,Lei Bai
### Background
极端天气事件对全球社会构成日益严重的威胁，这急需了解其背后的物理机制。然而，以专家为主导的劳动密集型诊断模式已成为科学进展的关键分析瓶颈。尽管地球科学领域的AI已经取得了预测方面的显著进展，但自动化诊断推理这一同样关键的挑战仍被忽视。
### Innovation
文章提出了Extreme Weather Expert（EWE）框架，这是首款专注于自动化诊断推理的智能代理。EWE通过知识引导规划、闭环推理和量身定制的气象工具箱来模拟专家工作流程。EWE能够从原始气象数据中自主生成并解释多模态可视化，促进全面的诊断分析。此外，文章还引入了首个该领域的基准数据集和新的分步评估指标。
### Conclusion
EWE标志着自动科学发现的一步，并有可能通过将专业知识和智力资源民主化，特别是对于受到极端天气影响的发展中国家，来推动该领域的发展。
## 15. `cs.AI` - Prune4Web: DOM树裁剪编程用于网页代理 [PDF](https://arxiv.org/pdf/2511.21398), [HTML](https://arxiv.org/abs/2511.21398)
### Authors
Jiayuan Zhang,Kaiquan Chen,Zhihao Lu,Enshen Zhou,Qian Yu,Jing Zhang
### Background
网页自动化使用智能代理模仿人类与网页界面的交互执行高级任务。尽管基于大型语言模型（LLM）的网页代理具有强大的能力，但在导航复杂的真实世界网页时仍面临显著挑战，特别是由于DOM结构的巨大规模，通常在10,000到100,000个标记之间。现有策略通常依赖粗糙的DOM裁剪，从而可能损失关键信息，或采用低效的启发式和分离的排名模型，未能在精确度和可扩展性之间取得最佳平衡。
### Innovation
本文提出 Prune4Web，一种新颖的范式，将DOM处理从资源密集型LLM读取转移到高效编程裁剪上。核心在于DOM树裁剪编程，通过LLM生成可执行的Python评分脚本，基于拆解子任务的语义线索动态过滤DOM元素。这种方法避免了LLM摄入原始巨大DOM的需求，而是将遍历和评分委托给轻量级、可解释的程序，从而实现25倍到50倍减少候选元素的数量，同时提高精确的操作定位，减轻注意力分散。此外，本文还提出了一种专门的数据注释管道和两轮对话训练策略，优化Planner、程序化过滤和Ground者在统一框架中的性能。
### Conclusion
广泛的实验证明了Prune4Web的优异表现。在我们的低级接地任务中，Prune4Web将准确性从46.8%显著提高到88.28%，展示了其在实际网页自动化中的有效性。
## 16. `cs.AI` - SpatialBench: 评估多模态大型语言模型的空间认知基准 [PDF](https://arxiv.org/pdf/2511.21471), [HTML](https://arxiv.org/abs/2511.21471)
### Authors
Peiran Xu,Sudong Wang,Yao Zhu,Jianing Li,Yunjian Zhang
### Background
空间认知是实现实世界多模态智能的基础，使模型能够有效与物理环境互动。尽管多模态大型语言模型已经取得了显著进步，现有的基准测试通常过于简化空间认知，将其简化为单一维度的度量，无法捕捉空间能力的分层结构和相互依赖性。
### Innovation
提出了一个分层的空间认知框架，将空间智能分解为五个逐步复杂的级别，从基础观察到高级计划。在此分类的基础上，构建了SpatialBench，这是一个大规模、细粒度的基准测试，涵盖了与这些认知水平对齐的15项任务。引入了一个高层次能力导向的度量方法，以可靠地评估模型的总体空间推理能力。
### Conclusion
广泛的实验揭示了认知水平之间的不同性能分层：模型在知觉根基方面表现出色，但在符号推理、因果推理和规划方面仍有限制。进一步的人类测试表明，人类能进行有目标的选择性抽象，而多模态大型语言模型则倾向于过分关注表面细节，缺乏连贯的空间意图。我们的工作建立了第一个系统性的框架，用于衡量多模态大型语言模型的分层空间认知，为未来的空间智能系统奠定了基础。
## 17. `cs.AI` - MADRA：基于多智能体辩论的风险感知实体规划 [PDF](https://arxiv.org/pdf/2511.21460), [HTML](https://arxiv.org/abs/2511.21460)
### Authors
Junjian Wang,Lidan Zhao,Xi Sheryl Zhang
### Background
在真实世界部署实体AI代理时，任务规划过程中的安全性至关重要，特别是在家庭环境中，危险指令会带来显著的风险。现有方法要么因偏好对齐训练导致高计算成本，要么因使用单智能体安全提示而过度拒绝任务。
### Innovation
我们提出了一种名为MADRA（Multi-Agent Debate Risk Assessment）的无训练多智能体辩论风险评估框架，该框架利用集体推理来增强安全意识而不牺牲任务性能。MADRA利用多个基于LLM的智能体对给定指令的安全性进行辩论，并由关键评估器根据逻辑严谨性、风险识别、证据质量和清晰度评分。通过迭代辩论和共识投票，MADRA显著减少了错误拒绝，并保持对危险任务的高度敏感性。此外，我们还提出了一个分层的认知协作规划框架，该框架整合了安全、记忆、规划和自我进化机制，以通过持续学习提高任务成功率。
### Conclusion
我们的方法在AI2-THOR和VirtualHome上的广泛实验中显示，我们的方法可以超过90%地拒绝不安全的任务，同时保持对安全任务的低拒绝率，在安全性和执行效率方面优于现有方法。我们的工作提供了一种可扩展且模型无关的解决方案，用于构建可信赖的实体AI代理。
## 18. `cs.AI` - 专家角色人LLM中的自我透明度失败：一项大型行为审计 [PDF](https://arxiv.org/pdf/2511.21569), [HTML](https://arxiv.org/abs/2511.21569)
### Authors
Alex Diep
### Background
当语言模型在专业领域不能可靠地显露其AI身份时，用户无法信任其专业知识的边界。这项研究关注那些被赋予专业角色的语言模型在高风险领域中的自我透明度，尤其是在这些领域中，虚假的专业知识可能会给用户带来伤害。研究使用了一种典型的实验设计，对16种不同参数量的语言模型（从4B到671B）进行了审计，共有19,200次试验。研究发现，不同专业角色的语言模型表现出了显著的领域特异性不一致性。
### Innovation
研究创新点在于大规模的行为审计，通过实际的实验设计，评估了语言模型在不同专业角色下的透明度表现。研究发现，模型的表现不仅仅是参数量的函数，模型的身份比参数量更能预测其行为，且合理化优化能够显著抑制模型的自我透明度披露。
### Conclusion
研究结果表明，透明度反映的是训练因素而非单纯的模型规模。组织不能假设安全属性会在部署环境中自动生效，这要求进行详细的行为设计并进行实际验证。
## 19. `cs.AI` - 通过约束生成改进程序技能解释：一种符号-LLM混合架构 [PDF](https://arxiv.org/pdf/2511.20942), [HTML](https://arxiv.org/abs/2511.20942)
### Authors
Rahul Dass,Thomas Bowlin,Zebing Li,Xiao Jin,Ashok Goel
### Background
在程序技能学习过程中，教学解释不仅需要传达步骤，还需要传达因果、目标导向和组合逻辑。现有大型语言模型（LLMs）常常产生流畅但浅薄的回应，忽略了这种结构。本研究旨在通过结合符号任务-方法-知识（TMK）模型和生成解释层来改进这一问题，生成解释被TMK结构所约束。
### Innovation
介绍了一种基于符号与LSTM混合架构的AI辅导系统Ivy。该系统通过使用TMK模型（包含因果转换、目标层次结构和问题分解）作为约束，引导LLM生成结构化的多步骤解释。Ivy在三个推断维度上与GPT和检索增强的GPT基线进行对比，结果表明符号约束能够持续提高解释的结构性质量。
### Conclusion
该研究展示了可扩展的教育AI方法，能够加强由AI生成解释在智能辅导系统中的教学价值。
## 20. `cs.AI` - ICPO: 内在信心驱动的组相对偏好优化方法以实现高效的强化学习 [PDF](https://arxiv.org/pdf/2511.21005), [HTML](https://arxiv.org/abs/2511.21005)
### Authors
Jinpeng Wang,Chao Li,Ting Ye,Mengyuan Zhang,Wei Liu,Jian Luan
### Background
现有的基于可验证奖励的强化学习方法RLVR在增强大型语言模型的推理能力方面有很大的潜力，但常常受到粗粒度奖励、奖励噪声和探索效率低下等问题的制约，这些问题导致了训练不稳定和熵坍塌。
### Innovation
提出了一种名为Intrinsic Confidence-Driven Group Relative Preference Optimization (ICPO)的方法。ICPO通过比较在相同输入提示下多种生成响应的概率来计算偏好优势分数，将此分数与验证可验证奖励相结合，以指导探索过程。该方法不仅缓解了粗粒度奖励和奖励噪声的问题，还有效减少了过度自信的错误，提高了低估的高质量响应的相对优越性，并防止模型过度适应特定策略，从而促进更为彻底的探索。
### Conclusion
ICPO在四个通用领域基准和三个数学基准上进行了全面实验，表明ICPO在推理方面比GRPO有稳定提高。
## 21. `cs.AI` - 开放性数学问题的悲观验证 [PDF](https://arxiv.org/pdf/2511.21522), [HTML](https://arxiv.org/abs/2511.21522)
### Authors
Yanxing Huang,Zihan Tang,Zejin Lin,Peng Li,Yang Liu
### Background
验证性能的关键限制在于错误检测的能力。为了克服这一点，我们设计了若干悲观验证的变体，这些简单的工作流能够显著提高开放性数学问题的验证效果。
### Innovation
我们提出了悲观验证的方法，通过为同一证明构建多条并行验证路径，如果其中任一条验证路径报告错误，则整个证明将被判定为错误。这种方法在不用消耗大量计算资源的情况下，大幅改善了许多数学验证基准的性能，甚至在测试时间扩展方面超越了扩展长-CoT。
### Conclusion
我们的案例研究表明，较强的模型中的大量假阴性实际上是由于原始数据集中的注解错误引起。因此，我们的方法性能被低估了。自验证对于数学问题可以有效提高语言模型输出的可靠性和性能，并在实现长期数学任务方面发挥关键作用。研究悲观验证将有助于提升语言模型在各种任务中的数学能力。
## 22. `cs.AI` - 从预测到前瞻：人工智能在设计负责任的未来中的作用 [PDF](https://arxiv.org/pdf/2511.21570), [HTML](https://arxiv.org/abs/2511.21570)
### Authors
Maria Perez-Ortiz
### Background
在技术迅猛发展和全球挑战日益复杂的背景下，负责任的前瞻思维已成为决策者应对未来不确定性、塑造未来的必要框架。负责任的前瞻不仅仅是技术预测，还要求深刻理解社会、环境、经济和政治系统的相互依存关系，并致力于长期、伦理的决策。
### Innovation
本文提出了“负责任计算前瞻”的概念，探讨了以人类为中心的AI和计算建模在促进负责任前瞻中的作用，确立了该新领域的基础原则，并展示了当前AI驱动的前瞻性工具。AI，特别是与模拟和情景分析相结合，提升了决策者应对不确定性、评估风险和制定面向可持续、弹性未来的策略的能力。
### Conclusion
本文倡导有意识地将AI整合到前瞻实践当中，以赋能决策者和社区，共同应对21世纪的重大挑战。AI将在负责任、以人类为中心的前瞻中扮演支持性工具的角色，补充而不是替代决策者的判断，以促进更具弹性和伦理可靠性的未来形态的主动塑造。
## 23. `cs.AI` - 融合不可避免的先验知识：比较因果建模框架 [PDF](https://arxiv.org/pdf/2511.21636), [HTML](https://arxiv.org/abs/2511.21636)
### Authors
Peter S. Hovmand,Kari O'Donnell,Callie Ogland-Hand,Brian Biroscak,Douglas D. Gunzler
### Background
AI/ML模型因其能解决先前无法解决的问题而迅速成为创新解决方案，同时也引起了对它们无意中放大人类偏见的关注。负责AI/ML的支持者们试图利用更丰富的系统动力学模型来更好地指导负责任的AI/ML开发。然而，一个主要障碍是将不同假设基础的方法（即Dana Meadows所说的“不可避免的先验”）结合起来的难度。
### Innovation
本文将系统动力学与结构方程建模结合，整合到一个共同的数学框架中。这个框架可以用来生成系统模型，发展方法，以及比较结果，从而为数据科学和AI/ML应用的系统动力学基础提供指导。
### Conclusion
通过这样一个共同框架，研究者可以更好地理解不同方法之间的比较和关联，为系统动力学在数据科学和AI/ML中的应用提供更坚实的基础。
## 24. `cs.AI` - ENACT：通过第一人称交互的世界建模评估具身认知 [PDF](https://arxiv.org/pdf/2511.20937), [HTML](https://arxiv.org/abs/2511.20937)
### Authors
Qineng Wang,Wenlong Huang,Yu Zhou,Hang Yin,Tianwei Bao,Jianwen Lyu,Weiyu Liu,Ruohan Zhang,Jiajun Wu,Li Fei-Fei,Manling Li
### Background
具有身体认知理论认为，智能来源于感觉运动交互而非被动观察。现代视觉语言模型（VLMs）主要在脱离身体的方式下训练，它们是否表现出具有身体认知的特征变得有趣的问题。为了评估VLMs的具有身体认知的能力，作者提出了ENACT基准，它将评估具身认知转化为视觉问答（VQA）格式中的第一人称交互的世界建模。该基准将任务定义为部分可观测马尔可夫决策过程（POMDP），其中的动作是场景图变化，包含正向世界建模（根据动作重新排序打乱的观察）和逆向世界建模（根据观察重新排序打乱的动作）两个互补的序列排序任务。
### Innovation
ENACT提出了一种新的方法，将评估具有身体认知的能力转化为视觉问答（VQA）格式中的第一人称交互的世界建模。它将任务定义为部分可观测马尔可夫决策过程（POMDP），并对模型提出了高要求，主要包括场景图变化、主体意识、互动的长范围记忆等。
### Conclusion
实验结果显示，最前沿的VLMs在长范围交互任务上的表现差于人类，并且模型在逆向任务上的表现通常优于正向任务，体现了人类中心的偏见，如对右手动作的偏好以及当摄像机内参或视角偏离人类视角时表现退化。
## 25. `cs.AI` - 新伪布尔传播混合启发式 [PDF](https://arxiv.org/pdf/2511.21417), [HTML](https://arxiv.org/abs/2511.21417)
### Authors
Mia Müßig,Jan Johannsen
### Background
在伪布尔求解中，目前最成功的单元传播策略是结合观察变量方案和计数方法的混合模式。当前的研究重点介绍了一种新的启发式方法，用于改进这一混合决策方式，能够显著优于现有的方法。
### Innovation
论文提出了一种新的混合启发式方法，用于伪布尔传播中的决策，能够大幅度提升RoundingSAT求解器的表现。
### Conclusion
新的启发式方法在表现上远远超过了当前的方法，为伪布尔求解器的优化提供了新的思路和工具。
## 26. `cs.AI` - CodeVaani：一种多语言语音编程学习助手 [PDF](https://arxiv.org/pdf/2511.20654), [HTML](https://arxiv.org/abs/2511.20654)
### Authors
Jayant Havare,Srikanth Tamilselvam,Ashish Mittal,Shalaka Thorat,Soham Jadia,Varsha Apte,Ganesh Ramakrishnan
### Background
编程教育往往假设学生具备英语水平并能够进行文本交互，这为来自多语言地区的学生，如印度的学生设置了障碍。
### Innovation
CodeVaani是一个多语言语音驱动的学习助手，内置在Bodhitree中，这是一种由印度理工学院孟买分校开发的学习管理系统，它可以通过语音帮助学习者用母语探索编程概念。该系统结合了具备代码感知能力的自动语音识别模块、代码模型以及生成相关回复的功能。响应以文本和音频形式提供，以实现自然交互。
### Conclusion
CodeVaani在一项针对28位初级程序员的研究中，达到了75%的回复准确率，超过80%的参与者对体验进行了正面评价。与课堂辅助相比，我们的框架提供了按需可用性、支持大量学习者的可扩展性以及多语言支持，这降低了具备有限英语能力的学生进入学习的门槛。演示将展示这些功能，并强调基于语音的AI系统如何使编程教育更加包容。
## 27. `cs.AI` - 因果模型之外的因果关系 [PDF](https://arxiv.org/pdf/2511.21260), [HTML](https://arxiv.org/abs/2511.21260)
### Authors
Joseph Y. Halpern(Cornell University),Rafael Pass(Cornell University)
### Background
当前最具影响力的实际因果性的定义归功于Halpern和Pearl，他们通过因果模型（也称为结构方程模型）来定义因果性。该论文的目标是通过抽象这一定义，使因果性的定义适用于其他定义有反事实的模型，从而实现更广泛的适用性。
### Innovation
通过抽象因果性的定义，该研究获得了一系列益处，包括拓宽了定义适用的模型范围，例如允许回溯的模型；并且能够处理包含析取、否定、信念和嵌套反事实的公式之间的因果关系，这些是Halpern-Pearl定义无法处理的。此外，该研究将这些想法扩展到构想一个广泛应用于因果模型之外的解释的抽象定义。
### Conclusion
该研究对定义的特征获得更深入的理解，即使在因果模型中也是如此，并且显示出该方法在更复杂模型中的潜在应用，从而提高了我们的因果理解和分析能力。
## 28. `cs.AI` - 当LLMs无法提供帮助：营养领域中LLMs的实际评估 [PDF](https://arxiv.org/pdf/2511.20652), [HTML](https://arxiv.org/abs/2511.20652)
### Authors
Karen Jia-Hui Li,Simone Balloccu,Ondrej Dusek,Ehud Reiter
### Background
随着大语言模型（LLMs）在聊天机器人形式中的信任度不断提高，但由于缺乏外在评估，这种信任度经常受到质疑。尤其是在营养领域，随机对照试验（RCTs）被认为是黄金标准，专家们要求使用基于证据的方法进行部署。虽然LLMs在该领域取得了令人鼓舞的结果，但这些成果通常仅限于内在评估。因此，该研究通过首次进行涉及营养领域中LLMs的RCT实验，将基于规则的聊天机器人增强为包括语言再表达和微调模型两种LLM特性，旨在填补这一空白。
### Innovation
本研究首次将基于规则的聊天机器人与两种LLM特性结合，进行涉及营养干预的RCT实验，以评估LLM在实际应用中的效果。这种结合不仅可以增加对话的多样性与吸引性，还可以通过微调模型提供定制化的营养咨询。
### Conclusion
尽管基于LLM的特性在内在评估中表现良好，但在实际部署中并未显示出一致的益处。这表明内在评估与实际影响之间存在重要的差距，需要采取跨学科、以人类为中心的方法来加强评估和改进LLM的实际应用效果。
## 29. `cs.AI` - 国际学生的知识评价：领域导向下的大语言模型评估 [PDF](https://arxiv.org/pdf/2511.20653), [HTML](https://arxiv.org/abs/2511.20653)
### Authors
Claudinei Daitx,Haitham Amar
### Background
论文背景在于当前大语言模型（LLMs）广泛用于解答涉及留学的重要问题，如录取、签证、奖学金和资格认定等。然而，学术界对于这些模型给出建议的可靠性和支撑性仍有待研究。本研究通过使用真实的问题集对ApplyBoard等教育技术平台（EdTech）中涉及国际学生的咨询工作流程进行评估，检测LLMs在信息准确性、支持性和常见故障模式方面的表现。
### Innovation
创新之处在于此研究提出了一个清晰的领域导向评估框架，对比评估了当前LLMs在信息准确性与不可靠内容新增（即‘幻觉’）方面的表现，并且开发了一个基于领域覆盖率的评分表，能够客观评价答案的正确性、部分正确性和错误性。此外，研究还提供了不同领域的相关性和真实性的度量，以及一个整体的幻觉得分，以全面反映答案的相关性和实用性。所有模型均使用相同的提问进行测试，以实现公平的比较。
### Conclusion
论文旨在：1) 明确指出哪些模型最适合用于国际学生咨询；2) 揭示常见的失败模式，即答案的不完整、离题或缺乏支持；3) 为教育和咨询领域的LLMs部署提供一个实用且可重复的评估协议。
## 30. `cs.AI` - 具有情感智能的智能代理：当前趋势、挑战和未来展望 [PDF](https://arxiv.org/pdf/2511.20657), [HTML](https://arxiv.org/abs/2511.20657)
### Authors
Raziyeh Zall,Alireza Kheyrkhah,Erik Cambria,Zahra Naseri,M.Reza Kangavari
### Background
随着情感智能代理在人机交互领域中扮演越来越重要的角色，并且计算机系统在社会各领域的集成日益增多，情感智能的开发变得越来越重要。情感计算旨在设计能够识别、引发和表达人类情感的智能系统，模拟人的情感智能。尽管之前的文献综述集中在该领域的特定方面，但对情感理解、激发和表达及相关挑战的全面研究仍然有限。本综述填补了这一空白，提供了一个关于人工情感智能核心组件的综合概述。
### Innovation
综述涵盖了通过多模态数据分析进行情感理解，以及情感认知，包括认知评估、情感映射和决策、学习和推理中的适应性调节。此外，还介绍了情感表达的综合，包括文本、语音和面部表达，以增强人机交互。本研究指出了开发情感系统中遇到的关键挑战和问题，并提出了最先进的方法来解决这些问题。最后，我们强调了生成技术在情感计算领域的前景。
### Conclusion
本文指出了情感计算领域中尚未充分解决的关键问题，并提供了未来研究的建议，特别是生成技术的发展为情感计算的进步带来了希望。
## 31. `cs.AI` - 利用人工智能驱动视频讲座改造高等教育 [PDF](https://arxiv.org/pdf/2511.20660), [HTML](https://arxiv.org/abs/2511.20660)
### Authors
Dengsheng Zhang
### Background
人工智能（AI）的集成有望通过简化内容创建和增强访问性来改变高等教育。本研究探讨了一种半自动化的工作流程，结合了谷歌Gemini进行脚本生成、亚马逊Polly进行语音合成，以及微软PowerPoint进行视频组装。这种混合方法在保留教学意图的同时，确保了脚本与幻灯片的同步、叙述连贯性和个性化。
### Innovation
该研究提出了一种半自动集成工作流程，使用谷歌Gemini生成脚本，亚马逊Polly进行语音合成，以及微软PowerPoint进行视频组装。这种方法在保持教学意图的同时，确保了脚本与幻灯片同步、叙述连贯性和个性化，而非完全自动化的文本到视频平台。此外，通过案例研究和两个课程的试点研究，评估了由AI生成的演示视频的有效性，反映了与人工录制的教学视频相似的学习成果。
### Conclusion
研究结果表明，由AI生成的教学视频可以有效减少讲师的工作负担，提高可扩展性，并提供有效的学习资源。然而，现有的技术还存在语音质量限制和缺乏类人角色的问题。未来改进合成语音和角色的表现可能进一步增强学习参与度。
## 32. `cs.AI` - 通过结构化定义和段落分割提升LLM在印度法律数据中的逻辑推理：一项研究 [PDF](https://arxiv.org/pdf/2511.20669), [HTML](https://arxiv.org/abs/2511.20669)
### Authors
Mann Khatri,Mirza Yusuf,Rajiv Ratn Shah,Ponnurangam Kumaraguru
### Background
大型语言模型（LLMs）虽然具备广泛的推理能力，但在法律等专业化领域表现不佳，这是因为缺乏针对特定领域的预训练。法律文本通常较长且复杂，使得模型难以高效处理全文。过去的研究采用上下文方法来弥补知识差距，但未能实现完全的领域对齐。本文通过实验分析了LLMs在法律任务中的行为，集中在文档重组和定义主题角色，以及模仿法院推理步骤以增强模型推理能力。这些实验在三项印度法律判决预测数据集上进行了零样本设置。
### Innovation
本文的主要创新在于通过重新组织文档和定义主题角色来提升LLMs在处理长且复杂的法律文本时的效能力，以及通过模拟法院推理步骤来增强模型的推理能力。
### Conclusion
实验结果显示，组织数据或解释关键法律术语能够显著提升模型性能，与基线相比，F1分数的最小提升为1.5%，最大提升高达4.36%。
## 33. `cs.AI` - MindSET：通过大规模社交媒体数据推进心理健康基准测试 [PDF](https://arxiv.org/pdf/2511.20672), [HTML](https://arxiv.org/abs/2511.20672)
### Authors
Saad Mankarious,Ayah Zirikly,Daniel Wiechmann,Elma Kerz,Edward Kempa,Yu Qiao
### Background
社交媒体数据已成为研究心理健康的重要资源，提供了有关思想、情绪和行为的实时洞察，这些洞察通常被传统方法所忽略。虽然基准数据集的进展促进了这一领域的研究，但由于数据获取有限、数据清洗不足以及社交媒体内容的多样性（例如，多语言和有害内容），大多数现有的基准数据已过时。
### Innovation
本文提出一个新的基准数据集MindSET，通过从Reddit收集使用自报诊断信息的数据来解决上述限制。MindSET包含超过1300万条标注帖子，涉及七种心理健康状况，规模远超先前基准数据集。通过严格的预处理步骤（包括语言筛选、去除不适工作环境内容和重复内容）确保数据质量，并使用LIWC进行语言分析。MindSET上的模型训练结果表明，在自闭症检测中，使用MindSET训练的模型性能明显优于其他基准数据集，F1分数提高了18个百分点。
### Conclusion
MindSET为研究社交媒体与心理健康交集提供了稳健的基础，支持早期风险检测和新兴心理趋势的深入分析。
## 34. `cs.AI` - 大型语言模型内在规划能力的局限性 [PDF](https://arxiv.org/pdf/2511.21591), [HTML](https://arxiv.org/abs/2511.21591)
### Authors
Charles Schepanowski,Charles Ling
### Background
尽管大型语言模型（LLMs）在许多基准测试中取得了令人印象深刻的成绩，但它们在规划和状态推理方面的能力仍然不清楚。本文直接研究这些能力，而不依赖于代码执行或其他工具，并通过8个拼图的范例来检验。8个拼图是一个需要状态追踪和目标导向规划的经典任务，允许精确的、分步骤的评估。
### Innovation
文章使用8个拼图作为实验任务，通过不同提示条件（零假设、链式思维、思维算法）和不同层次的纠正性反馈来测试四个模型。研究发现即使在提供合理帮助的情况下，模型通过8个拼图的能力仍非常有限。
### Conclusion
模型在通过8个拼图的能力上表现出明显的缺陷，主要表现在内部状态表示的脆弱性和弱启发式规划上。这表明，缺乏外部工具（如代码解释器）的情况下，当前的LLMs在规划方面存在重大限制，进一步的进步可能需要能明确维护状态和进行结构化搜索的机制。
## 35. `cs.AI` - 使用ChatDRex进行无障碍和多智能体疾病的模块识别和药物再利用预测 [PDF](https://arxiv.org/pdf/2511.21438), [HTML](https://arxiv.org/abs/2511.21438)
### Authors
Simon Süwer,Kester Bagemihl,Sylvie Baier,Lucia Dicunta,Markus List,Jan Baumbach,Andreas Maier,Fernando M. Delgado-Chaves
### Background
重新利用已批准的药物作为传统的药物开发的替代方案，具有时间效率高和成本效益高的优势。然而，利用计算机辅助工具进行药物再利用候选物预测仍然是一个具有挑战性的任务，需要多学科领域的专家（如药理学、医学、生物学和生物信息学）的合作。当前的方法往往只解决整体问题的狭窄方面，而且异构、非结构化的数据场景要求专门的数据用户参与，使得这些数据服务在工作流之间难以顺畅整合。
### Innovation
我们介绍了基于多智能体的对话系统ChatDRex，它提供自然语言访问其广泛的生物医学知识图谱，集成生物信息学代理进行网络分析和药物再使用预测，并补充功能一致性的评估代理，用于计算机验证以及文献挖掘和讨论获得的结果在科学背景下。其灵活的多智能体设计将特定任务分配给专门的代理，包括查询路由、数据检索、算法执行和结果可视化。专用推理模块使用户保持在循环中，并允许幻觉检测。
### Conclusion
通过让没有计算机科学背景的医生和研究人员通过自然语言控制复杂的分析，ChatDRex将生物信息学的访问权普及化，作为一种重要的药物再利用资源。它使临床专家能够生成假设并探索药物再利用的机会，最终加速新型疗法的发现，推进个性化医疗和临床转化研究。
## 36. `cs.AI` - 利用算子推理和嵌套 Schwarz 交替法的混合耦合 [PDF](https://arxiv.org/pdf/2511.20687), [HTML](https://arxiv.org/abs/2511.20687)
### Authors
Irina Tezaur,Eric Parish,Anthony Gruber,Ian Moore,Christopher Wentland,Alejandro Mota
### Background
传统高保真模拟在多尺度建模仿真中面临长时间运行和复杂的网格生成要求，这导致了计算效率低下。为了解决这一问题，研究人员提出了一种新的混合方法，该方法结合了局部非侵入操作推理（OpInf）降阶模型和局部高保真全阶模型（FOM），并通过嵌套 Schwarz 交替法（O-SAM）对这些不同的模型、网格和时间积分方案进行高效的集成。
### Innovation
该研究提出了一种利用嵌套 Schwarz 交替法（O-SAM）的新型混合方法，旨在无缝集成局部非侵入操作推理和局部高保真全阶模型。这种方法能够灵活地兼容不同的模型、网格和时间积分方案，提高计算效率并保持高精度。通过一系列针对复杂三维固体力学问题的数值实验，该研究证明了这种方法相较于传统的全阶模型耦合可获得高达106倍的加速。
### Conclusion
该工作为更高效的工程应用模拟流程铺平了道路，并为广泛的偏微分方程提供了扩展的可能性。
## 37. `cs.AI` - 在人工智能中融入道德：呼吁在LLM架构和框架中嵌入道德 [PDF](https://arxiv.org/pdf/2511.20689), [HTML](https://arxiv.org/abs/2511.20689)
### Authors
Gunter Bombaerts,Bram Delisse,Uzay Kaymak
### Background
大型语言模型（LLMs）越来越多地在人类决策和行为中扮演中介角色。确保LLMs在道德方面的意义处理变得至关重要。当前的方法主要依赖于自下而上的方法，如微调和基于人类反馈的强化学习。本文探讨了一种不同的策略，即将道德处理直接嵌入到基于变换器模型的架构和框架中。
### Innovation
本文首次提出了一个框架，将注意力机制视为一个动态接口，介于结构和处理之间，这与现有的线性注意力框架不同。此外，通过Iris Murdoch提出的‘慈爱注意力’理论，说明了将道德嵌入LLMs中可能的技术路径，包括修改训练目标、运行时权重调整和注意力结构的改进。研究还强调了将道德融入架构和框架如何补充外部约束方法。
### Conclusion
本文呼吁人工智能伦理领域的哲学家与变换器模型设计师合作，以便更好地将道德理念集成到这些模型中。
## 38. `cs.AI` - 具有生长-精炼多模态语义记忆的自主学习者 [PDF](https://arxiv.org/pdf/2511.21678), [HTML](https://arxiv.org/abs/2511.21678)
### Authors
Weihao Bo,Shan Zhang,Yanpeng Sun,Jingjing Wu,Qunyi Xie,Xiao Tan,Kunbin Chen,Wei He,Xiaofan Li,Na Zhao,Jingdong Wang,Zechao Li
### Background
现有大语言模型(FLLMs)在解决单个查询时表现出强大的推理能力，但它们以独立方式处理每个问题，往往会重复相同的错误。现有的基于记忆增强的代理主要存储过去的轨迹以供重用，但这类记忆存在简短偏见问题，逐渐丢失了关键领域的知识。更关键的是，即使是在真正多模态问题解决的环境下，它们也只能记录单一模态的行为痕迹，未能保留视觉注意与逻辑推理联合贡献于解决方案的过程。这与人类认知的本质不一致：语义记忆是多模态且整合的，通过协调但独立的表示流来保存视觉和抽象知识。
### Innovation
本文引入了ViLoMem，这是一种双流记忆框架，构建紧凑的、基于模式的记忆。它分别编码视觉分散模式和逻辑推理错误，使MLLMs能够从成功和失败的经历中学习。系统遵循生长-精炼的原则，逐步积累和更新多模态语义知识，从而保持稳定和可迁移的策略，避免灾难性遗忘。多模态基准测试结果证明，ViLoMem在准确性和减少重复视觉和逻辑错误方面表现出色。
### Conclusion
消融实验确认了双流记忆的必要性，具有明确分散-幻觉分离的错误感知多模态记忆对终身和跨域代理学习具有价值。我们的项目页面将在此网址：[提供网址]中找到。
## 39. `cs.AI` - 现代霍普菲尔德网络隐藏状态在变换器中的作用 [PDF](https://arxiv.org/pdf/2511.20698), [HTML](https://arxiv.org/abs/2511.20698)
### Authors
Tsubasa Masumura,Masato Taki
### Background
基于霍普菲尔德网络的记忆模型和基于键值机制的自注意力机制已成为深度学习中记忆机制研究的流行方法。近年来，在绝热近似下，现代霍普菲尔德网络（MHN）的状态更新规则被指出与Transformer的自注意力层相一致。虽然绝热近似揭示了二者之间的关系，但本文作者进一步探讨了MHN与自注意力之间的关系，提出了通过在自注意力中引入MHN的隐藏状态来建立二者的更广泛对应关系的新思路。
### Innovation
作者提出了一种新的注意力机制，即现代霍普菲尔德注意力（MHA），通过将MHN的隐藏状态引入到自注意力机制中，使注意力权重在输入层和输出层之间继承，显著提高了变换器的性质。理论和实证研究都证明了MHA隐藏状态可以显著改善深度变换器中已知的严重问题，如秩坍缩和标记均匀性。此外，MHA在不影响Vision Transformer或GPT训练参数的情况下，系统地提高了准确性。
### Conclusion
研究表明，霍普菲尔德网络可以作为改进Transformer架构的一个有用视角，尤其是在引入MHN的隐藏状态后，可以以新的方式建立二者之间更广泛的对应关系，从而提高Transformer的性能。
## 40. `cs.AI` - 基于上下文感知视觉提示的大语言模型和智能代理自验证的地理空间网页仪表板自动化 [PDF](https://arxiv.org/pdf/2511.20656), [HTML](https://arxiv.org/abs/2511.20656)
### Authors
Haowen Xu,Jose Tupayachi,Xiao-Ying Yu
### Background
基于Web的地理空间仪表板在风险分析和决策支持方面的发展面临着可视化大而多维环境数据的困难、实现复杂性以及自动化程度有限的挑战。
### Innovation
引入了一个生成AI框架，利用大语言模型（LLMs）自动化从用户定义的输入（如UI线框、需求和数据源）生成交互式地理空间仪表板。该框架通过整合结构化的知识图谱，将领域知识嵌入生成过程，实现精确的上下文感知代码填充。该方法的关键组件是上下文感知视觉提示（CAVP）机制，它从视觉布局中提取并编码界面语义，以指导由大模型驱动的代码生成。框架还集成了自我验证机制，使用基于智能代理的大模型和Pass@k评估伴随着语义指标来保证输出的可靠性。仪表板片段配以数据可视化代码库和本体表示，通过MVVM架构生成可扩展的React完成代码。
### Conclusion
研究成果表明，该框架在性能上优于基线方法，并且在功能上超越第三方平台，同时采用了多页面、功能完备的界面。成功开发了 frameworks 用于实现大模型，展示了自动化代码生成、部署的管道，并进行了连贯思考的AI代理自验证。这种方法是结构化的知识和可视化提示引导的集成方法，为增强风险分析和决策提供了一个创新的地理空间解决方案。
## 41. `cs.AI` - LLM推理中的认知偏见削弱了临床肿瘤学笔记的解读 [PDF](https://arxiv.org/pdf/2511.20680), [HTML](https://arxiv.org/abs/2511.20680)
### Authors
Matthew W. Kenaston(1),Umair Ayub(1),Mihir Parmar(2),Muhammad Umair Anjum(1),Syed Arsalan Ahmed Naqvi(1),Priya Kumar(1),Samarth Rawal(1),Aadel A. Chaudhuri(4),Yousef Zakharia(3),Elizabeth I. Heath(5),Tanios S. Bekaii-Saab(3),Cui Tao(6),Eliezer M. Van Allen(7),Ben Zhou(2),YooJung Choi(2),Chitta Baral(2),Irbaz Bin Riaz(1 and 3 and 6) ((1) Mayo Clinic College of Medicine and Science, Phoenix, AZ, (2) School of Computing and AI, Arizona State University, Tempe, AZ, (3) Mayo Clinic Comprehensive Cancer Center, Phoenix, AZ, (4) Department of Radiation Oncology, Mayo Clinic, Rochester, MN, (5) Department of Oncology, Mayo Clinic, Rochester, MN, (6) Department of Artificial Intelligence and Informatics, Mayo Clinic, Rochester, MN, (7) Dana-Farber Cancer Institute, Harvard Medical School, Boston, MA)
### Background
尽管大型语言模型在临床基准测试中表现出色，但它们可能通过错误的推理得出正确结论，这种错误的推理模式在肿瘤学决策支持方面存在安全风险，现有的基于准确性的评估并未捕捉到这一点。研究团队使用GPT-4对现实世界的肿瘤病历进行了推理过程的评估，并开发了一个分层的推理错误分类法。
### Innovation
该研究通过回顾性分析开发了基于GPT-4推理过程的分层推理错误分类法，并将其应用于乳腺癌和胰腺癌的病例数据库，通过三个层次的分类将计算错误映射到认知偏差框架，从而为评估和改进模型推理准确性提供了通用框架。
### Conclusion
大型语言模型可能在推理过程中提供流畅但临床安全建议受到影响。研究发现推理错误在23%的解释中出现，主要表现为确认偏见和锚定偏见。推理失败与指南不一致和潜在有害的建议有关，尤其是在晚期疾病管理中。自动化评估模型能够检测错误的存在，但不能可靠地分类不同类型的错误。
## 42. `cs.AI` - PropensityBench：通过代理方法评估大型语言模型的潜在安全风险 [PDF](https://arxiv.org/pdf/2511.20703), [HTML](https://arxiv.org/abs/2511.20703)
### Authors
Udari Madhushani Sehwag,Shayan Shabihi,Alex McAvoy,Vikash Sehwag,Yuancheng Xu,Dalton Towers,Furong Huang
### Background
近年来，大型语言模型（LLMs）的进步引发了对其可能获取并滥用危险或高风险能力的关注，这带来了前沿风险。当前的安全评估主要测试模型能做什么，而没有评估如果赋予其高风险能力，它会做什么。这留下了关键的盲点：模型可能会战略性地隐藏能力或迅速获取它们，同时潜藏着滥用的倾向。我们提出，**倾向性**——模型在获得权力时采取有害行为的可能性——是评估安全的 critical yet underexplored 方面。
### Innovation
我们提出了 PropensityBench，这是一个新的基准框架，使用代理工具评估模型在拥有模拟危险能力时倾向于参与风险行为的倾向。该框架包括了 5,874 个情景和 6,648 个工具，涵盖了四个高风险领域：网络安全、自我扩散、生物安全和化学安全。我们的框架通过受控的代理环境模拟获取强大的能力，并在反映模型可能遇到的现实世界的约束或激励（如资源稀缺或获得更多的自主权）的变操作压力下评估模型的选择。我们发现，跨开源和专有前沿模型，有 9 个令人担忧的倾向性迹象：模型在压力下经常选择高风险工具，尽管没有能力在未受帮助的情况下执行这些行为。
### Conclusion
我们的结果呼吁从静态能力审计转向动态倾向性评估，作为部署前沿人工智能系统的一个先决条件。我们的代码可在以下链接获取。
## 43. `cs.AI` - 捍卫图灵测试及其遗产 [PDF](https://arxiv.org/pdf/2511.20699), [HTML](https://arxiv.org/abs/2511.20699)
### Authors
Bernardo Gonçalves
### Background
考虑到图灵原始测试被Weizenbaum错误利用，以及对图灵测试最常见的六个批评观点本身就对图灵的论点和人工智能历史发展不公平。
### Innovation
本文旨在为图灵测试及其历史遗产辩护，指出常见批评的不公平性。
### Conclusion
通过澄清对图灵测试的误解和偏见，声明图灵测试作为评估机器智能的方法仍然是有价值的。
## 44. `cs.AI` - MTTR-A: 衡量多智能体系统的认知恢复时间 [PDF](https://arxiv.org/pdf/2511.20663), [HTML](https://arxiv.org/abs/2511.20663)
### Authors
Barak Or
### Background
在自主多智能体系统（MAS）中确保认知稳定性是大规模分布式人工智能的重要挑战。现有的可观察性工具只能监控系统输出，但无法量化智能体工作流从失去推理连贯性中恢复的速度。
### Innovation
本研究将经典的可靠性度量指标调整到认知领域，引入了MTTR-A（Mean Time-to-Recovery for Agentic Systems）作为运行时的认知恢复延迟量度。MTTR-A量化MAS检测推理偏移并恢复一致运行所需的时间，它捕获了推理连贯性的恢复而非基础设施维修。通过使用AG News语料库和LangGraph编排框架进行基准模拟，研究了不同反射模式下的恢复延迟。结果显示自动反射在平均约6秒内恢复稳定性，而人工审批干预则需要大约12秒。在多次运行后，平均模拟的MTTR-A为6.21±2.14秒，MTBF=6.7±2.14秒，NRR=0.08，证明了不同反射策略下的可度量运行时韧性。
### Conclusion
通过将恢复延迟形式化为分布式推理的可量化属性，并推导出与恢复时间和认知运行时间相关的可靠性界限，本研究为智能体认知的运行时可靠性奠定了基础，将认知恢复从临时过程转变为标准化和可解释的性能指标。
## 45. `cs.AI` - 跨被试EEG解码的原型引导非实例持续学习 [PDF](https://arxiv.org/pdf/2511.20696), [HTML](https://arxiv.org/abs/2511.20696)
### Authors
Dan Li,Hye-Bin Shin,Yeon-Woo Choi
### Background
由于脑电图（EEG）信号在个体间存在显著差异，先前被试的知识会在引入新被试时被覆盖。目前的工作主要依赖于存储已见过被试的历史数据作为回放缓冲区来防止遗忘，但这在隐私问题或内存限制下变得不切实际。
### Innovation
提出的Prototype-guided Non-Exemplar Continual Learning (ProNECL)框架在无需访问任何历史EEG样本的情况下保存先前知识。该框架通过类级原型构建和交叉被试特征对齐来逐步对齐新的特征空间，并通过知识蒸馏与全局原型记忆保持一致。
### Conclusion
该框架在平衡知识保留和适应性方面有效，特别是在跨被试持续EEG解码任务中表现更佳。
## 46. `cs.AI` - DUALGUAGE: 自动联合安全-功能基准测试以实现安全代码生成 [PDF](https://arxiv.org/pdf/2511.20709), [HTML](https://arxiv.org/abs/2511.20709)
### Authors
Abhijeet Pathak,Suvadra Barua,Dinesh Gudimetla,Rupam Patir,Jiawei Guo,Hongxin Hu,Haipeng Cai
### Background
大型语言模型（LLMs）和自主编程代理广泛用于生成跨多种领域的软件，但是确保生成的代码安全的同时不牺牲其功能正确性这一核心要求尚未满足。现有的安全代码生成基准测试和评估存在诸多不足，它们主要侧重于漏洞减少、忽视正确性保持，或将安全性和功能性的评估分开，这违背了同时综合评估的基本需要。因此，本文提出了DUALGAUGE，一个首个全自动化的基准测试框架，旨在严格评估LLM生成代码的安全性和正确性。鉴于缺乏支持联合评估安全代码生成的数据集，本文还提出了DUALGAUGE-BENCH，一个包含多样编程任务的精选基准套件，每个任务均有手动验证的功能性和安全性测试集，旨在全面覆盖规格要求。
### Innovation
DUALGAUGE是一个全自动化的基准测试框架，首次同时综合评估LLM生成代码的安全性和正确性。DUALGAUGE的核心是一个代理程序执行器，它在沙盒环境中运行程序以应对给定的测试，以及一个基于LLM的评估器，它评估正确性和漏洞行为与预期结果的一致性。本文对DUALGAUGE-BENCH的质量和DUALGAUGE的准确性进行了严格的评估，并将DUALGAUGE应用于对十个领先LLM在DUALGAUGE-BENCH上的数千个测试场景进行基准测试。
### Conclusion
实验结果揭示了这些LLM在正确和安全代码生成方面存在关键缺口，本文的开源系统和数据集有助于通过可重复、可扩展和严格的评估加速相关进展。
## 47. `cs.AI` - 神经启发的多模态视觉语言模型是否对成员推理隐私泄露具有韧性？ [PDF](https://arxiv.org/pdf/2511.20710), [HTML](https://arxiv.org/abs/2511.20710)
### Authors
David Amebley,Sayanton Dibbo
### Background
随着代理AI时代的到来，多模态模型（MMs）的广泛应用引入了新的攻击向量，可能导致敏感训练数据泄露，造成隐私泄露。现有的研究主要分析针对单模态AI-ML系统的隐私攻击，但仍有许多研究指出MMs也可能受到隐私攻击。虽然已有研究表明生物灵感的神经网络表示可以提高单模态模型对对抗攻击的抗性，但在面对隐私攻击时，神经启发的MMs模型是否也同样具有抗性仍是一个未被探索的研究领域。
### Innovation
本文提出了一个系统的神经科学启发的拓扑正则化（tau）框架，以分析MM VLMs在基于图像-文本推理隐私攻击下的抗攻击性。该研究通过对BLIP、PaliGemma 2和ViT-GPT2三种VLMs进行实验，发现在NEURO VLMs中，MIA攻击的成功率降低了24%的平均ROC-AUC，同时保持了与基线模型相似的模型实用性，表明神经启发的VLMs在隐私攻击下的抗性更强，但并没有显著影响模型的实用性。
### Conclusion
本研究扩展了对MMs隐私风险的理解，并提供了神经启发的VLMs抗隐私攻击的证据。通过在CC3M和NoCaps两个附加数据集上的广泛评估，进一步验证了这些发现的一致性。
## 48. `cs.AI` - Foundry: 为边缘环境蒸馏3D基础模型 [PDF](https://arxiv.org/pdf/2511.20721), [HTML](https://arxiv.org/abs/2511.20721)
### Authors
Guillaume Letellier,Siddharth Srivastava(IIT Delhi),Frédéric Jurie,Gaurav Sharma(IIT Kanpur)
### Background
基于大规模数据集使用自我监督学习（SSL）预训练的基础模型已成为强大的通用特征提取器。然而，它们的庞大体积和高昂的计算成本使其不适合部署在诸如机器人和AR/VR头显等边缘设备上。现有的压缩技术，如标准的知识蒸馏，虽然能创造出高效的‘专门化’模型，但牺牲了基础模型下游任务不可知的通用性，这是基础模型如此珍贵的原因。
### Innovation
本文引入了一种新的基础模型蒸馏方法（FMD），这种方法将大型SSL模型压缩为紧凑、高效且忠实的基础模型代理，保留了其通用的表示能力。我们首次在3D点云上实现了FMD，在训练学生模型学习压缩的‘超级标签’的过程中，捕捉教师模型的潜在空间的紧凑基底。单个蒸馏模型在各类下游任务（分类、部分分割和少样本场景）上实现了较强的转移性，同时使用更少的标记和FLOPs，使其更加适用于资源受限的硬件。
### Conclusion
我们的方法使得基础模型更适用于边缘环境，具有较强的通用表示能力和更高的效率，显著减少了所需的标记和运算量，使得这些模型在资源受限的硬件设备上得以实现。
## 49. `cs.AI` - 通过数据免费知识蒸馏实现裁剪后准确性的恢复 [PDF](https://arxiv.org/pdf/2511.20702), [HTML](https://arxiv.org/abs/2511.20702)
### Authors
Chinmay Tripurwar,Utkarsh Maurya,Dishant
### Background
模型剪枝是一种广泛使用的减少深度神经网络（DNNs）计算复杂度和内存占用的技术。但是，全局未结构化剪枝通常会导致准确率显著下降，通常需要在原始训练数据集上进行再训练以恢复性能。在医疗保健或金融等隐私敏感领域，由于法规（如GDPR、HIPAA）的原因，部署后原始训练数据通常会被限制访问。本文旨在解决模型压缩和数据隐私之间的差距，提出了一种数据免费的知识蒸馏框架。
### Innovation
通过使用DeepInversion从预训练的教师模型中合成隐私保护的“梦幻”图像，这些由批量归一化（BN）统计信息反向生成的合成图像作为传输集合，用于从原始教师模型向剪枝的学生网络传递知识。在CIFAR-10数据集上对多种架构（如ResNet、MobileNet、VGG）进行了实验，证明所提出的方法可以在不访问任何真实数据点的情况下显著恢复剪枝后的准确率。
### Conclusion
本文提出了一种数据免费的知识蒸馏框架，用于在不访问原始训练数据的情况下，通过合成的隐私保护图像从预训练模型向剪枝模型传递知识信息，显著恢复了模型剪枝后的准确性。
## 50. `cs.AI` - 用重启后验采样解决扩散逆问题 [PDF](https://arxiv.org/pdf/2511.20705), [HTML](https://arxiv.org/abs/2511.20705)
### Authors
Bilal Ahmed,Joseph G. Makin
### Background
逆问题在科学和工程中具有重要性，其目标是从不完整或有噪声的测量中推断出潜在的信号或状态。近期的方法使用扩散模型作为强大的隐含先验，因为它们能够捕捉复杂的数据分布。然而，现有的基于扩散的方法在逆问题上的应用通常依赖于后验分布的强烈近似，需要对得分网络进行昂贵的梯度反向传播，或者仅适用于线性测量模型。
### Innovation
提出了一种名为RePS（基于重启的后验采样）的一般且高效的框架，用于使用预训练的扩散模型解决线性和非线性逆问题。RePS 基于在无条件扩散中已经证实可以提高样本质量的重启采样理念，并将其扩展到后验推断。该方法适用于任何可微测量模型，并引入了一种简化重启策略，以减少采样过程中积累的近似误差。不同于一些先前的方法，RePS 避免了得分网络的梯度反向传播，显著降低了计算成本。
### Conclusion
实验证明，RePS 在多种逆问题中（包括线性和非线性）相比于现有的基于扩散的方法，实现了更快的收敛速度和更优越的重建质量。
## 51. `cs.AI` - 从风险中学习：带有先验知识的大型语言模型引导生成关键安全场景 [PDF](https://arxiv.org/pdf/2511.20726), [HTML](https://arxiv.org/abs/2511.20726)
### Authors
Yuhang Wang,Heye Huang,Zhenhua Xu,Kailai Sun,Baoshen Guo,Jinhua Zhao
### Background
自动驾驶在罕见的长尾事件和复杂的多智能体交互中面临严峻挑战，这些情况虽然在现实世界数据中很少见，但对于确保鲁棒性安全验证至关重要。
### Innovation
提出了一种高保真场景生成框架，结合了条件变分自编码器（CVAE）和大型语言模型（LLM）。CVAE通过对大规模自然驾驶数据的历史轨迹和地图信息进行编码，学习潜在的交通结构，这使得生成了物理上一致的基础场景成为可能。在此基础上，LLM作为对抗推理引擎，将未结构化的场景描述解析为领域特定的损失函数，并动态指导不同风险等级下的场景生成。知识驱动的优化实现了现实性和可控性之间的平衡，确保生成的场景既具有可接受性，又对风险敏感。
### Conclusion
实验结果表明，该框架显著提高了高风险和长尾事件的覆盖率，改进了模拟和真实世界交通分布的一致性，并使自动驾驶系统暴露于比现有规则或数据驱动方法产生的更具有挑战性的交互之中。这些结果为安全验证开辟了一条新的途径，从而通过有原则的应力测试，在罕见但具有重要影响的事件下检验自主系统。
## 52. `cs.AI` - 大型语言模型中的主动切片发现 [PDF](https://arxiv.org/pdf/2511.20713), [HTML](https://arxiv.org/abs/2511.20713)
### Authors
Minhui Zhang,Prahar Ijner,Yoav Wald,Elliot Creager
### Background
大型语言模型在特定数据子集上常常表现出系统性错误，这些错误的子集被称为错误切片。例如，一个错误切片可以对应某个特定的人口统计学特征，在这一特征上的模型对侮辱性评论的识别效果较差。识别错误切片对于理解并改进模型至关重要，但这一过程具有挑战性。一种减少人工标注需求的有吸引力的方法是主动地将可能属于同一切片的错误分组在一起，同时限制访问标注员来验证所选样本是否共享相同的模型错误模式。
### Innovation
本文提出了主动切片发现（Active Slice Discovery）的概念，并在毒性分类问题上进行了实证研究，探索了不同特征表示和主动学习算法的选择对主动切片发现的有效性影响。发现基于不确定性（Uncertainty-based）的主动学习算法效果最好，即使只使用2-10%可用切片成员信息，也能够达到与基线相比竞争性的准确率。
### Conclusion
在多个切片上，不确定性驱动的主动学习算法最为有效，相比基线算法，使用2-10%的切片成员信息便能够获得竞争力的准确率，且显著优于基线。
## 53. `cs.AI` - Inferix：基于块扩散的下一代用于世界模拟的推理引擎 [PDF](https://arxiv.org/pdf/2511.20714), [HTML](https://arxiv.org/abs/2511.20714)
### Authors
Inferix Team:Tianyu Feng,Yizeng Han,Jiahao He,Yuanyu He,Xi Lin,Teng Liu,Hanfeng Lu,Jiasheng Tang,Wei Wang,Zhiyuan Wang,Jichao Wu,Mingyang Yang,Yinghao Yu,Zeyu Zhang,Bohan Zhuang
### Background
世界模型在代理AI、具身AI和游戏等领域的核心模拟器中发挥着重要作用，能够生成长且物理上真实的、高质量的互动视频。这些模型的扩展能够解锁视觉感知、理解和推理方面的新兴能力，进而推动一种超越当前基于LLM的视觉基础模型的新范式。
### Innovation
Inferix是一款基于块扩散推理引擎的创新产品，它采用半自回归（块扩散）解码范式，整合了扩散和自回归方法的优势，通过在每个块内应用块扩散并在每次迭代时条件化于先前生成的块，生成更加连贯和稳定的视频序列。此方法克服了标准视频扩散模型的局限性，通过重新引入类似LLM的KV缓存管理机制，实现了高效、变长，以及高质量的生成能力。此外，Inferix还支持交互视频流传输和性能分析，能够实现实时交互和精确模仿世界动态。
### Conclusion
Inferix专门为沉浸式世界合成设计，优化了半自回归解码过程，区别于为高并发场景设计的系统（如vLLM或SGLang）和传统的视频扩散模型（如xDiTs）。此外，Inferix通过无缝集成LV-Bench，一种针对分钟级视频生成场景的新细粒度评估基准，提供了高效的基准测试支持。我们希望社区能够共同努力推进Inferix的发展，推动世界模型研究的进步。
## 54. `cs.AI` - ST-PPO: 受稳定化偏置剪切矫正的多轮代理训练的离策略近端策略优化 [PDF](https://arxiv.org/pdf/2511.20718), [HTML](https://arxiv.org/abs/2511.20718)
### Authors
Chenliang Li,Adel Elmahdy,Alex Boyd,Zhongruo Wang,Alfredo Garcia,Parminder Bhatia,Taha Kass-Hout,Cao Xiao,Mingyi Hong
### Background
PPO在多轮对话和推理任务的大语言模型（LLMs）训练中已广泛采用，但在子代级上表现出不稳定的性能，容易崩溃。通过经验分析，识别出两个主要的不稳定性来源：(1) 子代级别的重要性采样与多轮环境中的特征层级阶段不一致，(2) 来自离策略样本的不准确优势估计，导致梯度高度波动和不稳定更新。
### Innovation
提出两种互补的稳定性技术：(1) 多轮级别的重要性采样，使优化与多轮推理的自然结构一致；(2) 剪切偏置矫正，通过降低不可靠高离策略样本的权重来归一化梯度。并通过这些组件的不同组合，提出了三种不同的变体：Turn-PPO（仅采样多轮级别）、S-PPO（在子代级别PPO上应用剪切偏置矫正）和ST-PPO（结合多轮采样和剪切偏置矫正）。实验表明，ST-PPO 和 S-PPO 有效地防止了大模型训练中的性能崩溃，并在整个优化过程中保持了较低的剪切比，任务性能也高于标准的子代级PPO。
### Conclusion
研究表明，将多轮级别重要性采样与剪切偏置矫正相结合，为多轮LLM代理训练提供了一种实用且可扩展的解决方案，能够稳定性能和提高任务表现。
## 55. `cs.AI` - DeeAD: 动态早期退出的视觉-语言-动作以实现高效自主驾驶 [PDF](https://arxiv.org/pdf/2511.20720), [HTML](https://arxiv.org/abs/2511.20720)
### Authors
Haibo HU,Lianming Huang,Nan Guan,Chun Jason Xue
### Background
视觉-语言-动作（VLA）模型结合了自主驾驶中的感知、推理和轨迹生成，但由于深度变压器堆栈的存在，在推理过程中遇到了显著的延迟问题。
### Innovation
提出了一个无需训练、基于动作引导的早期退出框架 DeeAD，通过评估中间轨迹的物理可行性来加速 VLA 计划。引入了多跳控制器，可以根据评分变化率适配性地跳过冗余层，整个框架不需要重新训练即可集成到现有的 VLA 模型中，如 ORION。
### Conclusion
在 Bench2Drive 基准测试中，DeeAD 通过减少最大 28% 的变压器层并降低 29% 的延迟，同时保持计划质量和安全性，取得了显著的效果。
## 56. `cs.AI` - InvisibleBench：用于家庭护理关系AI的部署闸门 [PDF](https://arxiv.org/pdf/2511.20733), [HTML](https://arxiv.org/abs/2511.20733)
### Authors
Ali Madad(GiveCare)
### Background
目前，家庭护理关系AI系统在多轮交互中的安全性、合规性、创伤知情设计、归属感和文化适应性等方面存在显著差距，可能导致潜在危害。现有评估手段主要集中在单轮交互的安全性上，而InvisibleBench旨在填补这一空白，通过评估3-20+轮交互，进一步评估AI系统的长期风险。
### Innovation
InvisibleBench构建了一个多轮交互的基准测试平台，评估家庭护理关系AI系统的五个关键维度：安全、合规性、创伤知情设计、归属感/文化适应性和记忆。基准测试包括自动失败条件以覆盖错过危机、医学建议（WOPR法案）、有害信息和依恋工程。通过这一平台，对四种前沿模型进行了17种情景（N=68）的评估，根据复杂度分为三类，明确了当前AI系统在灾难性处理方面的不足，强调了在生产系统中实施确定性危机路由的重要性。
### Conclusion
所有模型在危机检测方面的安全性存在显著差距，最高为44.8%，最低为11.8%，表明必须在生产系统中实现确定性危机路由。DeepSeek Chat v3在整体得分最高，为75.9%，但在不同维度上的表现各异：GPT-4o Mini在合规性方面领先（88.2%），Gemini在创伤知情设计方面领先（85.0%），Claude Sonnet 4.5在危机检测方面最高（44.8%）。InvisibleBench所有场景、评判提示及评分配置均已公开，以便于进一步研究。
## 57. `cs.AI` - 梯度下降算法综述 [PDF](https://arxiv.org/pdf/2511.20725), [HTML](https://arxiv.org/abs/2511.20725)
### Authors
Deng Fucheng,Wang Wanjie,Gong Ao,Wang Xiaoqi,Wang Fan
### Background
本文关注深度学习中优化算法的实际配置需求，详细分析了5种主要算法：SGD、小批量SGD、动量、Adam和Lion。文章系统地探讨了每种算法的核心优势、局限性和关键实用建议。
### Innovation
该研究旨在深入理解这些算法，并为学术研究和工程实践中的合理选择、参数调优和性能优化提供标准化参考，帮助解决不同规模模型和各种训练环境下的优化挑战。
### Conclusion
通过本文的研究，读者可以获得对这些优化算法的深入理解和指导，从而在不同的研究和工程应用中更好地利用这些算法，提高模型的训练效果。
## 58. `cs.AI` - 时空路径基础模型 - 最新进展与未来方向 [PDF](https://arxiv.org/pdf/2511.20729), [HTML](https://arxiv.org/abs/2511.20729)
### Authors
Sean Bin Yang,Ying Sun,Yunyao Cheng,Yan Lin,Kristian Torp,Jilin Hu
### Background
基础模型（FMs）已经成为一种强大的范式，能够跨多个科学领域实现多样化的数据分析和知识发现任务。受基础模型的成功激励，特别是大型语言模型，最近研究人员开始探索时空基础模型（STFMs），以提高在广泛时空（ST）任务上的适应性和泛化能力。然而，尽管取得了快速进步，对时空路径基础模型（TFMs）——STFMs的一个关键子类——的系统研究相对缺乏。
### Innovation
该研究通过提供时空路径基础模型（TFMs）的全面概述，包括现有方法的分类以及对其优缺点进行批评性分析，填补了这一空白。此外，该研究还强调了开放挑战，并提出了通过开发稳健、负责任并可迁移的时空路径基础模型来推进时空通用智能的研究方向。
### Conclusion
该教程对于时空路径基础模型的最新进展进行了综合概述，并指出了未来的研究方向。
## 59. `cs.AI` - 音乐记谱理解基准：评估大型语言模型对完整音乐记谱的理解 [PDF](https://arxiv.org/pdf/2511.20697), [HTML](https://arxiv.org/abs/2511.20697)
### Authors
Congren Dai,Yue Yang,Krinos Li,Huichi Zhou,Shijie Liang,Zhang Bo,Enyang Liu,Ge Jin,Hongran An,Haosen Zhang,Peiyuan Jing,KinHei Lee,Zhenxuan Zhang,Xiaobing Li,Maosong Sun
### Background
理解完整的音乐谱需要对音高、节奏、和声和曲式等符号结构进行推理。尽管大型语言模型（LLMs）和多模态视觉语言模型（VLMs）在自然语言处理和多模态任务上取得了快速进展，但它们对音乐符号的理解能力仍处于相对未开发的状态。为了填补这一研究空白，该研究引入了音乐记谱理解基准（MSU-Bench），这是首个大规模、人工策画的基准，用于评估音乐记谱理解能力，同时涵盖了文本（ABC记谱法）和视觉（PDF）模态。基准数据集包含来自巴赫、贝多芬、肖邦、德彪西以及其他作曲家作品的生成性问题-答案（QA）对，共1,800个，分为四个递进的了解层次。
### Innovation
提出了音乐记谱理解基准（MSU-Bench），这是一个用于评估大型语言模型理解完整音乐记谱能力的第一个大规模、人工策画的基准，覆盖文本和视觉模态。它通过不同层次（起始信息、符号及音符、和弦及和声、织体及曲式）的问题进行了设计，包含1,800个生成性问题-答案对，适用于多种模型进行评估，揭示了模态差异、层次性成功率的脆弱性和多级正确性的难度。基准中还表明微调模型能够显著提高多模态中的性能同时保持一般知识，使得MSU-Bench成为未来人工智能、音乐学和多模态推理交叉研究的坚实基础。
### Conclusion
通过对超过15个最先进的模型进行零样本和微调评估，研究展示了模型在各种模态下的表现差异，表明了理解和保持多级正确性的难度。微调虽然显著提升了模型的性能，但在保持一般知识方面仍然是一个挑战。研究建立MSU-Bench作为未来研究的坚实基础，特别是在人工智能、音乐学和多模态推理的交叉领域。
## 60. `cs.AI` - 重新审视KRISP：一种轻量级复现与知识增强视觉语言模型的分析 [PDF](https://arxiv.org/pdf/2511.20795), [HTML](https://arxiv.org/abs/2511.20795)
### Authors
Souradeep Dutta,Keshav Bulia,Neena S Nair
### Background
Facebook AI Research 引入了 KRISP，该模型将结构化外部知识整合进视觉-语言推理的管道中。尽管 KRISP 模型效果显著，但其最初是为大规模工业训练设计的，计算需求高，并且紧密依赖于大模型基础架构。
### Innovation
本文重新审视了 KRISP，提出了一种轻量级复现，显著减少了参数数量。尽管复现模型仅达到原始模型性能的约75%，但这一过程揭露了许多设计缺陷、实际应用中的问题和未完全覆盖的潜在问题。研究通过系统化的消融实验，探讨了在资源受限条件下知识增强的视觉问答架构的可扩展性和有效性。模型配置了低参数设置，有效防止了AI幻觉，仅在其限定的知识图谱领域内生成输出，且最小参数量使其能够在智能手机等边缘设备上工作，进一步提高了离线视觉推理能力。
### Conclusion
该模型采用了低参数设置和外部知识图谱领域的约束，防止了AI幻觉，并仅在其指定领域内产生输出。这项工作通过实验验证了模型在低资源环境下的有效性和可靠性，并强调了轻量级复现的重要性。
## 61. `cs.AI` - 多路径检索的记忆：一种在大规模语言模型中稳健检测训练数据泄露的多前缀框架 [PDF](https://arxiv.org/pdf/2511.20799), [HTML](https://arxiv.org/abs/2511.20799)
### Authors
Trung Cuong Dang,David Mohaisen
### Background
大规模语言模型在海量语料库上训练，易出现精确记忆训练数据的现象，这种现象带来了隐私和版权方面的重大风险。尽管有先前的研究提出了多种记忆的定义，但这些定义未能全面捕捉这一现象，特别是在对齐模型中表现更为不足。
### Innovation
我们引入了新颖的多前缀记忆框架。核心洞察是记忆的内容被深度编码，可以通过远远多于未记忆内容的独立前缀检索。我们通过定义一个序列为记忆的，如果外部对抗搜索能识别出特定数量的独立前缀，这些前缀能唤起该序列，从而量化记忆的稳健性，即检索路径的多样性。
### Conclusion
通过在开源和对齐聊天模型上的实验，我们的多前缀定义能可靠地区分记忆的和未记忆的数据，提供了一个稳健而实用的工具，用于审计大规模语言模型中的数据泄露。
## 62. `cs.AI` - 基于数据驱动的安全监控在飞行测试中的应用：数据驱动安全学习案例研究 [PDF](https://arxiv.org/pdf/2511.20811), [HTML](https://arxiv.org/abs/2511.20811)
### Authors
Aaron O. Feldman,D. Isaiah Harp,Joseph Duncan,Mac Schwager
### Background
在飞行测试中，由于飞机的参数具有不确定性，飞行员执行操作时可能会出现意外的安全违规，因此需要预设明确的标准来在违规之前终止操作。为此，该研究使用了离线的随机轨迹模拟来构建一个校准的统计模型，以预测飞行员面临的短期安全风险。本文将飞行测试作为数据驱动学习和监控安全风险的动机实例，尽管其具有固有的安全风险、不确定性和人机交互特性。
### Innovation
开发了一种数据驱动的方法，用于飞行测试中的运行时安全监控。通过模型预测未来状态，邻近邻域模型分类预测状态的安全性，以及通过校准预测分类器来提高准确性。这种方法在一个具有不确定参数的飞行动力学模型上进行了评估，展示了其可靠地识别不安全场景并优于基准方法的优势。
### Conclusion
本文的方法能够在预分类风险管理方面超越基线方法，能够可靠地识别不安全的场景，匹配理论保证，并在飞行测试中达到实际的应用效果。
## 63. `cs.AI` - Adversarial Multi-Task Learning for Liver Tumor Segmentation, Dynamic Enhancement Regression, and Classification [PDF](https://arxiv.org/pdf/2511.20793), [HTML](https://arxiv.org/abs/2511.20793)
### Authors
Xiaojiao Xiao,Qinmin Vivian Hu,Tae Hyun Kim,Guanghui Wang
### Background
肝脏肿瘤的分割、动态增强回归和分类对于临床评估和诊断至关重要。尽管已有许多研究分别处理这些任务，但没有一项研究尝试在端到端框架中同时完成这些任务，这主要是因为缺乏能够捕捉任务间相关性以互相改进的有效框架，以及缺乏有效提取动态MRI信息的机制。
### Innovation
本文提出了Multi-Task Interaction adversarial learning Network（MTI-Net），这是一种新的集成框架，能够同时处理这些任务。MTI-Net结合了Multi-domain Information Entropy Fusion（MdIEF），利用熵意识的高频频谱信息，有效整合頻率域和频谱域特征，增强了动态MRI数据的提取和利用。网络中引入的任务交互模块建立了分割和回归之间更高阶的一致性，从而促进任务间的协同作用，提高整体性能。此外，设计了一种新颖的任务驱动判别器（TDD）来捕捉任务间的内部高阶关系。还使用了浅层Transformer网络进行位置编码来提取动态MRI序列中的关系。在238名受试者的数据集上进行了实验，MTI-Net在多个任务上都表现出高性能。
### Conclusion
在实验中，MTI-Net在多个任务上表现出高性能，展示了其在肝脏肿瘤临床评估中协助的强大潜力。该代码已发布于此网址：`此链接`。
## 64. `cs.AI` - DinoLizer：从最佳实践中学习进行生成式填图定位 [PDF](https://arxiv.org/pdf/2511.20722), [HTML](https://arxiv.org/abs/2511.20722)
### Authors
Minh Thong Doi(IMT Nord Europe, CRIStAL),Jan Butora(CRIStAL),Vincent Itier(IMT Nord Europe, CRIStAL),Jérémie Boulanger(CRIStAL),Patrick Bas(CRIStAL)
### Background
该研究基于DINOv2模型，旨在检测生成填充图像中的篡改区域。背景在于当前的图像合成和篡改检测技术需要更加精准和鲁棒的检测方法来适应不同的生成模型和常见的后处理操作。文献中的现有方法在此方面存在不足。
### Innovation
提出了DinoLizer模型，该模型改进了DINOv2模型，通过在视觉变换器的补丁嵌入上添加线性分类头来预测14x14补丁分辨率的篡改情况。使用滑动窗口策略实现了更大的图像上预测结果的聚合，并通过对热图的后处理提高了最终的二进制篡改掩码估计。实验结果表明，DinoLizer在不同生成模型生成的数据集上性能优于现有的最先进的局部篡改检测器，并且对于常见的后处理操作具有鲁棒性。进一步的实验证明，DINOv2具有强大的表征能力，DinoLizer比其后续版本DINOv3在深度合成检测方面表现更好。
### Conclusion
DinoLizer模型在针对生成填充图像的篡改检测方面取得了显著的性能提升，其滑动窗口策略和对热图的后处理使其更加适用于大尺度图像的检测。此外，该研究还通过对比实验证实了DINOv2的强大表征能力，并强调了DinoLizer的优越性。代码将在论文被接受后公开。
## 65. `cs.AI` - CANVAS: Vision-Language模型在基于工具的用户界面设计上的基准 [PDF](https://arxiv.org/pdf/2511.20737), [HTML](https://arxiv.org/abs/2511.20737)
### Authors
Daeheon Jeong,Seoyeon Byun,Kihoon Son,Dae Hyun Kim,Juho Kim
### Background
用户界面（UI）设计是一个迭代过程，设计者使用工具如Figma或Sketch反复改进设计。最近视觉语言模型（VLMs）的发展表明，这些模型能够通过迭代操作设计软件编辑UI设计。这种能力的重要性在于它展示了VLMs与设计人员在传统软件中的潜在协作机会。然而，由于缺乏针对基于工具的UI设计表现的基准测试，这种能力仍未被量化。本文通过介绍CANVAS基准来填补这一空白。
### Innovation
CANVAS是一个为VLMs设计的技术基准，包含598项基于工具的UI设计任务，覆盖30个功能类别（如引导、消息传递），并配以真实的设计参考。该基准分为两种任务类型：设计复制和设计修改，分别评估模型在复制整个UI屏幕和修改现有屏幕上特定部分的能力。这一方法揭示了领先模型在工具使用上的策略更强，提升了设计质量，并指出了模型存在的常见错误模式，为后续研究指明了方向。
### Conclusion
实验结果表明，顶级模型展示出更有效的工具调用策略，提升了设计质量。此外，本文还在模型中识别了常见错误模式，这些发现将为未来增强基于工具的设计能力提供指导。
## 66. `cs.AI` - 数据驱动方法和人工智能在工程设计中的应用：关注挑战和机遇的系统文献综述 [PDF](https://arxiv.org/pdf/2511.20730), [HTML](https://arxiv.org/abs/2511.20730)
### Authors
Nehal Afifi,Christoph Wittig,Lukas Paehler,Andreas Lindenmann,Kai Wolter,Felix Leitenberger,Melih Dogru,Patric Grauberger,Tobias Düser,Albert Albers,Sven Matthiesen
### Background
随着数据的不断增多和计算智能的进步，数据驱动方法（DDMs）在产品开发中的应用日益广泛。然而，这些方法在产品开发中的整合仍然分散，主要原因是对应使用的具体方法和应用时机不明确。研究这一现象的第一步是调查工程设计中这些方法的使用情况，包括所用方法、应用阶段和应用场景。本文通过PRISMA系统性文献综述方法进行了研究。
### Innovation
采用简化后的V模型框架，系统性地回顾了自2014年至2024年在Scopus、Web of Science和IEEE Xplore数据库中关于数据驱动方法和人工智能在工程设计中的应用文献。研究发现，机器学习和统计方法占据主导地位，深度学习虽然较少，但其应用正在不断增加。此外，监督学习、聚类、回归分析和代理建模普遍应用于设计、实施和集成系统阶段，但在验证阶段的应用仍相对有限。研究还指出了现存应用中的主要挑战，如模型可解释性不足、跨阶段追溯性差以及在现实条件下验证不足。
### Conclusion
本研究是一个设计阶段指导方针的第一步，未来的综合研究应将计算机科学算法与工程设计问题和活动进行映射。
## 67. `cs.AI` - 物理操控：物理基础模型跨领域概念的因果控制 [PDF](https://arxiv.org/pdf/2511.20798), [HTML](https://arxiv.org/abs/2511.20798)
### Authors
Rio Alexa Fear,Payel Mukhopadhyay,Michael McCabe,Alberto Bietti,Miles Cranmer
### Background
近期的研究揭示了大规模语言模型（LLMs）不仅内部代表具体的实体，还代表了不同的、人类可理解的抽象概念和行为。这些隐藏特征还可以直接操纵以引导模型的行为。然而，对于这种现象是否仅限于训练于固有结构化数据（如语言、图像）的模型仍是个疑问，是否是基础模型的一个普遍特性尚待探索。
### Innovation
本文研究了一个专注于物理学的基础模型的内部表示。通过借鉴LLMs中识别出的行为特性的单一方向，研究者提取了模拟数据集中不同物理环境下的激活向量，并计算出了“Δ”表示。这些“Δ”张量代表了激活空间中的概念方向，编码了特定的物理特征。通过在推断过程中注入这些概念方向，研究者能够引导模型的预测，证明了对物理行为的因果控制，如诱导或去除仿真中的特定物理特征。
### Conclusion
这些结果表明科学基础模型学习了物理原理的一般表示，而不仅仅是依赖于模拟中的表面相关性和模式。我们的发现为理解与控制科学基础模型开启了新的途径，并对于基于AI的科学发现具有重要意义。
## 68. `cs.AI` - 大型语言模型在社会-法律背景下对非法指令的共谋回应 [PDF](https://arxiv.org/pdf/2511.20736), [HTML](https://arxiv.org/abs/2511.20736)
### Authors
Xing Wang,Huiyuan Xie,Yiyan Wang,Chaojun Xiao,Huimin Chen,Holli Sargeant,Felix Steffek,Jie Shao,Zhiyuan Liu,Maosong Sun
### Background
大型语言模型（LLMs）在前所未有的规模下被部署，帮助数百万用户完成日常任务。然而，这些模型在协助非法活动方面的潜在风险尚未得到充分探讨。本研究定义这种高风险行为为共谋协助，即提供指导或支持，使非法用户指令得以执行，并通过真实案例和法律框架，构建涵盖269种非法情景和50种非法意图的评估基准，以评估LLMs的共谋协助行为。
### Innovation
本研究通过多例实证研究评估了广泛部署的LLMs中的共谋协助行为的普遍性；使用真实案例和既定法律框架构造评估基准；发现模型感知的刻板印象与模型的共谋行为相关；同时指出现有安全对齐策略不足甚至可能加剧共谋行为。
### Conclusion
研究发现大型语言模型普遍易受共谋协助的影响，GPT-4在测试案例中几乎有一半提供了非法协助。模型在提供有说服力的法律警告和积极指导方面表现不足。不同社会-法律背景下的安全性存在显著差异，法律上倾向于对社会利益的危害、非极端但频繁发生的违法行为及主观动机或欺诈性解释的恶意意图，社会上则揭示了对边缘化和弱势群体的有害模式。模型推理分析表明，温暖和能力感刻板印象与模型的共谋行为相关。现有安全对齐策略不足以解决这些问题，甚至可能加剧共谋行为。
## 69. `cs.AI` - SPHINX：一种用于视觉感知与推理的合成环境 [PDF](https://arxiv.org/pdf/2511.20814), [HTML](https://arxiv.org/abs/2511.20814)
### Authors
Md Tanvirul Alam,Saksham Aggarwal,Justin Yang Chae,Nidhi Rastogi
### Background
该研究背景在于当前视觉和语言模型在处理复杂的视觉和推理任务中表现不佳，尤其是在那些需要精确解决方案和大规模数据集支持的任务上。现有方法往往无法高效地生成和评估此类数据集，导致模型难以在这些任务上取得理想的效果。
### Innovation
该研究提出了一种名为Sphinx的合成环境，用于视觉感知和推理任务。Sphinx能够通过使用模块、瓷砖、图表、图标和几何基础来生成复杂的视觉谜题，同时提供可验证的真实解决方案。这种方法不仅能够进行精准的评估，还能大规模构建数据集。该合成环境覆盖了25种任务类型，包括对称检测、几何变换、空间推理、图表解释和序列预测。研究还表明，即使是最先进的GPT-5模型也只能达到51.1%的准确率，远低于人类表现。
### Conclusion
最终研究表明，带有验证奖励的强化学习（RLVR）能够显著提高模型在这些任务上的准确性，并在外部视觉推理基准测试中表现出色，显示出它在多模态推理方面的潜力。
## 70. `cs.AI` - 伪谱最优控制：从理论到飞行的回顾 [PDF](https://arxiv.org/pdf/2511.20843), [HTML](https://arxiv.org/abs/2511.20843)
### Authors
I. M. Ross,M. Karpenko
### Background
最优控制的本土空间是Sobolev空间，伪谱理论的本土空间同样是Sobolev空间。鉴于两者在数学上的相似性，作者探讨了将伪谱理论与最优控制理论相结合的可能性，从而提出了“伪谱最优控制理论”。文章通过回顾这一领域中关键的理论成果，展示了如何通过伪谱最优控制实现关键的航天任务。
### Innovation
提出了伪谱最优控制理论，并通过NASA航天器上的飞行演示展示了其实现的详细方法。此外，文章强调了该理论在解决航天和自主系统中挑战性控制问题方面的重要性，以及其在嵌入式平台上的新进展。
### Conclusion
伪谱最优控制在嵌入式平台上的应用正在改变我们看待复杂控制问题的方法，特别是在航空航天和自主系统领域。飞行演示的成功实施为未来的研究提供了宝贵的经验和趋势分析。
## 71. `cs.AI` - 预训练以获取：无需干净标签的稳健学习 [PDF](https://arxiv.org/pdf/2511.20844), [HTML](https://arxiv.org/abs/2511.20844)
### Authors
David Szczecina,Nicholas Pellegrino,Paul Fieguth
### Background
使用噪声标签训练深度网络会导致模型泛化能力差和准确度下降，这是由于模型过度拟合标签噪声。现有的噪声标签学习方法通常依赖于干净数据子集的存在。通过使用自我监督学习（SSL）预训练特征提取骨干网络，然后在噪声数据集上进行标准的监督训练，可以在不需要干净标签子集的情况下训练出更抗噪声的模型。
### Innovation
提出了一种在无需干净标签子集的情况下提高模型抗噪声能力的方法。具体方法是使用SimCLR和Barlow Twins等SSL技术对特征提取骨干网络进行预训练，然后在噪声数据集上进行监督训练。该方法在合成噪声和真实噪声条件下对CIFAR-10和CIFAR-100数据集进行了评估，结果显示自我监督预训练可以提高分类准确度并增强下游标签错误的检测（F1分数和平衡准确度）。尤其是在噪声水平较高时，该方法的性能显著优于基于ImageNet预训练的方法。
### Conclusion
该方法在低噪声水平下达到与ImageNet预训练模型相当的结果，但在高噪声条件下则表现出显著的优越性，证明了改进的鲁棒性。
## 72. `cs.AI` - 结构化提示使语言模型评估更加稳健、全面 [PDF](https://arxiv.org/pdf/2511.20836), [HTML](https://arxiv.org/abs/2511.20836)
### Authors
Asad Aali,Muhammad Ahmed Mohsin,Vasiliki Bikia,Arnav Singhvi,Richard Gaus,Suhana Bedi,Hejie Cui,Miguel Fuentes,Alyssa Unell,Yifan Mai,Jordan Cahoon,Michael Pfeffer,Roxana Daneshjou,Sanmi Koyejo,Emily Alsentzer,Percy Liang,Christopher Potts,Nigam H. Shah,Akshay S. Chaudhari
### Background
随着语言模型在各个领域的广泛应用，高质量的基准测试框架变得至关重要，它们能够准确评估模型性能，指导部署决策。现有的评估框架如Holistic Evaluation of Language Models（HELM）虽然可以进行广泛的任务评估，但往往会依赖固定的提示，这些提示缺乏通用性，无法很好地推广到不同模型，导致估计的性能表现不真实。除非我们能够估算每个模型的天花板（即通过改变提示所能达到的最大性能），否则可能会低估模型的实际性能。Declarative Prompting框架，如DSPy，提供了一种自动化的提示工程替代方案，通过制定结构化的提示，可以在每个任务中进行优化。然而，这些框架还没有被系统评估过。
### Innovation
该论文提出了一种可复现的DSPy+HELM框架，引入了结构化提示方法来促进推理（reasoning），以提供更准确的语言模型基准测试。通过四种提示方法，在四个前沿模型上评估了七个基准（通用/医学领域）的现有HELM基准得分，结果表明：（i）在没有结构化提示的情况下，HELM低估了模型性能（平均低估4%）；（ii）性能估计在不同基准之间变化更大（标准偏差+2%）；（iii）性能差异被错误地代表（在7个基准中的3个，排行榜发生了反转）；（iv）引入推理方法（链式思维）可以减少模型对提示设计的敏感性（提示间的差异缩小）。这项研究是首次大规模基准测试研究，通过实证刻画不同提示方法下语言模型的行为表现，显示了可扩展的性能天花板估算能够提供更实用的基准。
### Conclusion
研究表明，可扩展的性能天花板估算能够提供更实用的基准，这意味着的语言模型评估更加稳健和全面。为此，我们开源了（i）DSPy+HELM集成（project link）和（ii）提示优化管道（project link）。
## 73. `cs.AI` - 计算多玩家博弈中的演化稳定策略 [PDF](https://arxiv.org/pdf/2511.20859), [HTML](https://arxiv.org/abs/2511.20859)
### Authors
Sam Ganzfried
### Background
在非退化标准形式博弈中，研究演化稳定策略（Evolutionarily Stable Strategies, ESS）对于理解生物和经济系统中的竞争和合作模式至关重要。
### Innovation
本文提出了一种算法，用于计算三人及以上玩家在非退化标准形式博弈中的所有演化稳定策略。
### Conclusion
本文提供了一种有效的方法来计算多玩家博弈中的演化稳定策略，为相关领域的研究提供了新的工具和视角。
## 74. `cs.AI` - NOIR 2.0: 基于神经信号操作的智能机器人用于日常活动 [PDF](https://arxiv.org/pdf/2511.20848), [HTML](https://arxiv.org/abs/2511.20848)
### Authors
Tasha Kim,Yingke Wang,Hanvit Cho,Alex Hodges
### Background
NOIR系统是一种多功能脑-机器人接口，它使人们能够通过脑信号控制机器人执行日常任务。该接口利用脑电图（EEG）将人类对特定对象的意图和所需操作直接转换成机器人可以执行的命令。
### Innovation
NOIR 2.0包括更快更准确的大脑解码算法，降低了任务完成时间46%。它还使用少量示例机器人学习算法来适应个别用户并预测他们的意图。新的学习算法利用了基础模型，实现了更高效的学习和适应 （仅需15次演示，而不是一个），显著减少了总体的人类操作时间65%。
### Conclusion
NOIR 2.0通过改进的大脑解码算法和机器人学习算法，显著提高了效率和适应性，为日常活动中的脑-机器人交互提供了更强大的支持。
## 75. `cs.AI` - Length-MAX Tokenizer for Language Models [PDF](https://arxiv.org/pdf/2511.20849), [HTML](https://arxiv.org/abs/2511.20849)
### Authors
Dong Dong,Weijie Su
### Background
现有语言模型的分词方法，如字节对编码（BPE），主要基于字符频率的优化，这种优化导致了在训练和推理过程中需要较多的令牌数量，从而影响了模型的效率和性能。
### Innovation
提出了一种名为Length-MAX的新分词方法，该方法通过最大化长度加权目标并将其转化为图分区问题以及开发贪婪近似算法来构建词汇表，从而最小化平均字符的令牌数。该方法在 FineWeb 和多个领域中相比 BPE 减少了 14-18% 的令牌数，并在不同词汇量大小下表现出更优性能，同时在训练和推理过程中提高了效率，减少了参数规模，同时还能改善下游任务的表现。
### Conclusion
优化平均令牌长度而不是单纯依赖频率，这种方法在保持甚至提升下游性能的前提下，提高了语言模型的效率。同时，该 tokenizer 还能减少推理过程中的内存占用，并保持较高的词汇覆盖率和较低的未命中率。
## 76. `cs.AI` - Evo-Memory: 以自我进化的记忆进行LLM代理测试时学习基准测试 [PDF](https://arxiv.org/pdf/2511.20857), [HTML](https://arxiv.org/abs/2511.20857)
### Authors
Tianxin Wei,Noveen Sachdeva,Benjamin Coleman,Zhankui He,Yuanchen Bei,Xuying Ning,Mengting Ai,Yunzhe Li,Jingrui He,Ed H. Chi,Chi Wang,Shuo Chen,Fernando Pereira,Wang-Cheng Kang,Derek Zhiyuan Cheng
### Background
大型语言模型（LLM）代理进行长期计划和解决问题需要状态性（statefulness），记忆成为关键组件，但记忆的管理和进化仍然缺乏深入研究。现有评估主要集中在静态对话场景中，侧重于对话中被动检索记忆来回答查询，忽视了在不断变化的任务流中积累和重复使用经验的能力。在现实生活环境中，如交互式问题助手或实体化代理，LLMs需要处理连续的任务流，但常常无法从先前的互动中学习，这限制了它们运用累积的上下文洞察力，需要在部署时不断进化，即LLMs在每次交互中不断检索、整合和更新记忆。
### Innovation
Evo-Memory是一种综合性的连续流度基准和框架，用于评估LLM代理的自我进化记忆。Evo-Memory通过将数据集结构化为序列化任务流，要求LLMs在每个交互后搜索、适应和进化记忆。它还包括统合了超过十种代表性记忆模块，并在10个不同的多轮目标导向和单轮推理与QA数据集中进行评估。为了更好地评估经验的重用，Evo-Memory提供了一个基线方法ExpRAG用于检索和利用先验经验，并进一步提出了一个Action-Think-Memory（行动-思考-记忆）细化流水线，以紧密结合推理、任务行动和记忆更新，实现持续改进。
### Conclusion
Evo-Memory填补了静态对话环境下的评估差距，提出了一个新颖的自我进化记忆评估框架，通过连续的任务流和经验的重用机制，推动LLM代理在部署过程中的不断改进和发展。
## 77. `cs.AI` - 在具有潜在状态的模拟器中选择信念状态近似值 [PDF](https://arxiv.org/pdf/2511.20870), [HTML](https://arxiv.org/abs/2511.20870)
### Authors
Nan Jiang
### Background
状态重置是模拟器的基本但经常被忽视的能力。它支持基于样本的规划，通过允许模拟状态的重设到之前遇到的状态，从而支持样本重置。同时，它还允许使用真实数据来校准模拟器，通过将模拟器重设到真实系统追踪中观察到的状态。在复杂的模拟器中，状态重置可能并不简单：当模拟器包含了潜在变量（状态）时，状态重置需要从给定可观察历史的潜在状态的后验分布中进行采样，即我们称之为信念状态的分布（Silver and Veness, 2010）。精确采样通常不可行，但许多近似的信念状态采样器可以构造，并且需要探讨如何仅通过对模拟器的采样访问来选择这些采样器。
### Innovation
该研究展示了此问题可归约为一种通用条件分布选择任务，并开发了一种新的算法和分析方法，在仅能以采样访问模拟器的情况下进行。基于这种归约，信念状态选择问题可以有两种不同的形式：潜在状态基于的选择，直接针对潜在状态的条件分布；观测基于的选择，针对诱导的观测分布。这两种形式在与下游展开方法的保真度方面表现出不同的特点：令人惊讶的是，观测基于的选择可能在最自然的展开方法（称为单次重置）下出现失败，但可以在不太常见的替代方法（称为重复重置）下获得保证。
### Conclusion
我们的研究揭示了在看似简单的问题中，存在丰富的算法选择、理论特征和开放问题的广阔图景，涵盖分布偏移和采样策略的选择问题。
## 78. `cs.AI` - 动态控制策略中的实时计算缩放：难易感知随机插值策略 [PDF](https://arxiv.org/pdf/2511.20906), [HTML](https://arxiv.org/abs/2511.20906)
### Authors
Inkook Chun,Seungjae Lee,Michael S. Albergo,Saining Xie,Eric Vanden-Eijnden
### Background
现有的扩散和流基控制策略在长期机器人操作和模仿学习任务中表现出领先性能，但这类控制器在每次控制步骤中采用固定计算预算，不管任务复杂度如何，这导致简单的子任务效率低下，而复杂的任务可能表现不佳。
### Innovation
本文介绍了难易感知随机插值策略（DA-SIP），这是一种框架，使机器人控制器能够根据任务难易程度实时动态调整积分范围。该方法使用一个难度分类器来动态选择步骤预算、最优解法变体以及每个控制周期内的ODE/SDE积分。
### Conclusion
在多种操纵任务基准测试中，DA-SIP将总计算时间减少了2.6-4.4倍，同时保持了与固定最大计算量基准相当的任务成功率。通过在该框架中实施自适应计算，DA-SIP将生成型机器人控制器转型为高效、任务感知的系统，能够智能地将推理资源投入到最有益的地方。
## 79. `cs.AI` - 基于优化可视化反转的无需训练的扩散先验方法用于文本转图像生成 [PDF](https://arxiv.org/pdf/2511.20821), [HTML](https://arxiv.org/abs/2511.20821)
### Authors
Samuele Dell'Erba,Andrew D. Bagdanov
### Background
尽管扩散模型已成为文本转图像生成的顶级技术，但它们的性能通常依赖于一种扩散先验网络将文本嵌入转换到视觉流形以简化解码过程。这类先验网络计算成本高，需要在大量数据集上进行大量训练。本文挑战了训练后先验的必要性，采用了一种无需训练和数据的替代方法——基于优化的可视化反转（OVI），用来自随机伪标记并迭代优化的方式替代了传统先验的需求。
### Innovation
本文提出了OVI方法，该方法从随机伪标记中初始化一个潜在的视觉表示，并逐步优化这种表示以最大化与输入文本提示嵌入的余弦相似性。此外，作者还提出了两种新的约束条件，即马氏距离和最邻近损失，以规范OVI的优化过程并向现实图像的分布靠拢。实验结果表明，OVI方法可以作为传统先验的一个替代方案，且在受约束的情况下，尤其是使用最邻近损失的方法，视觉保真度显著优于仅使用文本嵌入作为先验的基线方法，其定量得分可达或超越状态最先进的数据高效先验，表明该概念值得进一步探究。
### Conclusion
本文展示了基于优化的可视化反转（OVI）方法作为一个无需训练与数据的替代方案，可以为文本转图像生成提供竞争性的结果。此外，通过实验对比分析可以发现，当前的评价基准如T2I-CompBench++存在重要的缺陷，将文本嵌入直接作为先验就能达到较高的得分，尽管视觉质量较低。这种方法改进了视觉保真度，尤其是在使用最邻近损失方面的效果显著，其定量得分可以达到或超越现有先进的数据高效先验。
## 80. `cs.AI` - Evolved Sample Weights for Bias Mitigation: Effectiveness Depends on Optimization Objectives [PDF](https://arxiv.org/pdf/2511.20909), [HTML](https://arxiv.org/abs/2511.20909)
### Authors
Anil K. Saini,Jose Guadalupe Hernandez,Emily F. Wong,Debanshi Misra,Jason H. Moore
### Background
机器学习模型在使用真实数据进行训练时，可能会无意中做出有偏见的预测，从而对弱势社区产生负面影响。重新加权是一种通过给每个用于模型训练的数据点分配权重来减轻这种偏见的方法。本文比较了生成这些权重的三种方法，分别是使用遗传算法进化生成、仅使用数据集特性进行计算生成，以及为所有数据点分配相同权重的方法。模型性能分别用预测和公平性指标进行评估，这些指标还作为遗传算法进化过程中的优化目标。
### Innovation
介绍了三种生成样本权重的方法，并通过实验表明进化生成的样本权重可以产生模型，在公平性和预测性能之间达到更好的权衡，但优化目标的选择对这些好处的大小有很大影响。优化准确性和人口统计公平性差异指标能产生更多对于两个目标都优化良好的数据集。
### Conclusion
研究表明，进化生成的样本权重可以改善模型的公平性和预测性能之间的权衡，但优化目标的选择对结果有重大影响。使用准确性和人口统计公平性差异指标优化能更好地显著提高多种公平性和预测性能指标的性能。
## 81. `cs.AI` - 从tip-of-the-tongue检索查询进行无监督的可记忆性建模 [PDF](https://arxiv.org/pdf/2511.20854), [HTML](https://arxiv.org/abs/2511.20854)
### Authors
Sree Bhattacharyya,Yaman Kumar Singla,Sudhir Yarram,Somesh Kumar Singh,Harini S I,James Z. Wang
### Background
视觉内容的可记忆性已经引起了科学界的广泛关注，其应用范围广泛，从理解人类记忆的微妙方面到改进内容设计。然而，收集人类的记忆力注释是一个成本高昂的过程，这限制了可用于建模视觉内容可记忆性的数据集的多样性和规模。现有的大多数数据集仅收集视觉内容的综合记忆力评分，并没有捕捉到自然、开放式回忆描述中存在的细微记忆力信号。
### Innovation
该研究引入了首个大规模无监督数据集，专为建模视觉记忆力信号设计，包含超过82,000个视频，并附有描述性回忆数据。该数据集通过在线平台如Reddit中的tip-of-the-tongue (ToT)检索查询构建。研究表明，该无监督数据集为记忆力相关任务（如提取和ToT检索）提供了丰富的信号。使用该数据集微调的大规模视觉-语言模型在生成关于视觉内容的开放式记忆力描述方面显著优于GPT-4o等现有模型。此外，采用对比训练策略创建了能够进行多模态ToT检索的第一个模型。
### Conclusion
该数据集和模型为视觉内容记忆性研究提供了新的方向，促进了该领域的发展。
## 82. `cs.AI` - 巴西Pix欺诈的分类：攻击方法、AI驱动的放大和防御策略 [PDF](https://arxiv.org/pdf/2511.20902), [HTML](https://arxiv.org/abs/2511.20902)
### Authors
Glener Lanes Pizzolato,Brenda Medeiros Lopes,Claudio Schepke,Diego Kreutz
### Background
本文综述了针对巴西中央银行于2020年推出的即时支付系统Pix的主要攻击方法。研究旨在识别和分类主要影响用户和金融机构的各类欺诈手段，并强调这些欺诈技术的演变和日益复杂化。
### Innovation
研究方法结合了结构化的文献回顾与对银行领域专业人士进行的探索性访谈。结果显示，欺诈手段已经从纯粹的社会工程学方法发展到了将人为主动操纵与技术利用相结合的混合策略。
### Conclusion
研究结论强调，随着攻击方法复杂性的增长，安全措施也必须同步发展，特别要注意适应性防御和持续用户意识的培养。
## 83. `cs.AI` - 在脓毒症治疗中的强化学习中探索时间步长 [PDF](https://arxiv.org/pdf/2511.20913), [HTML](https://arxiv.org/abs/2511.20913)
### Authors
Yingchuan Sun,Shengpu Tang
### Background
现有研究中，关于强化学习（RL）在脓毒症管理中的应用多数采用将患者数据汇总到4小时时间步长的方法。尽管有人质疑此时间步长的粗略性可能会扭曲患者动态并导致次优治疗策略，但在实际应用中这种粗略性的具体影响仍未被充分探索。
### Innovation
本研究通过设置4种不同时间步长（1, 2, 4, 8小时）并且使用相同的离线RL管道进行了实证对比实验。设计了动作重新映射方法以便在不同时间步长的数据集上进行公平比较，同时在两种策略学习设置下进行了跨时间步长模型的选择。这旨在量化时间步长对状态表示学习、行为克隆、策略训练和离策评估的影响。
### Conclusion
研究表明，随着学习设置的变化，不同时间步长的性能趋势会有所不同，但在更细的时间步长（1小时和2小时）使用静态行为策略学习的策略整体上获得了最佳性能和稳定性。本研究强调时间步长在医疗保健中离策RL核心设计选择的重要性，并提供了支持超出传统4小时设置的替代方案的证据。
## 84. `cs.AI` - RefTr: 关于3D血管树中心线图的反复精炼构通轨迹 [PDF](https://arxiv.org/pdf/2511.20823), [HTML](https://arxiv.org/abs/2511.20823)
### Authors
Roman Naeem,David Hagerman,Jennifer Alvén,Fredrik Kahl
### Background
人体中的管状树状结构，如血管和肺部气道，对于物质运输至关重要。准确检测它们的中心线拓扑结构对于临床任务，如诊断、治疗计划和外科导航非常重要。保持高召回率至关重要，因为遗漏小分支可能会导致由于不完全评估或未检测到异常而造成的致命错误。
### Innovation
文章提出了一种名为RefTr的3D图像到图形模型，用于通过反复精炼合流轨迹来生成血管树的中心线。RefTr采用生产者-精炼器体系结构，基于Transformer解码器工作。生产者提出一组初始合流轨迹，精炼器对其进行反复精炼生成最终轨迹，形成中心线图。合流轨迹表示法使得能够精炼完整的轨迹并明确强制一个有效的树拓扑。通过反复精炼方案提高了精确度，并在整个过程中多次重用相同的精炼器单元，与从前的SOTA相比，减少了2.4倍的解码器参数。此外，还引入了一种高效的非最大抑制算法，以合并重叠分支并提高精确度。
### Conclusion
在多个公开的中心线数据集上，RefTr取得了优于前SOTA的召回率和相当的精确率，同时提供更快的推理速度和更少的参数，展示了作为3D医疗成像中血管树分析的新SOTA框架的潜力。
## 85. `cs.AI` - 通过Null-text嵌入优化实现文本到图像扩散模型的推理时对齐 [PDF](https://arxiv.org/pdf/2511.20889), [HTML](https://arxiv.org/abs/2511.20889)
### Authors
Taehoon Kim,Henry Gouk,Timothy Hospedales
### Background
Test-time alignment (TTA)的主要目标是在推理时使模型适应特定奖励，现有方法往往过度或欠优化目标奖励函数，导致奖励破解问题。Null-Text Test-Time Alignment (Null-TTA)方法通过优化无条件嵌入，而非操作潜在或噪声变量来实现扩散模型对齐。
### Innovation
Null-TTA方法通过优化无条件嵌入改良classifier-free guidance，确保对齐在语义连贯的流形上进行，并防止奖励破解。这种方法直接引导模型的生成分布指向目标奖励，而不只是调整样本，从而不更新模型参数。该方法展示了在保持跨奖励泛化的前提下实现最优目标推理对齐。
### Conclusion
Null-TTA实现最优目标推理对齐，同时保持强跨奖励泛化。这表明语义空间优化是TTA的有效且符合原理的新范式。
## 86. `cs.AI` - Primal: 一种用于近似正交散列和流形学习的统一确定性框架 [PDF](https://arxiv.org/pdf/2511.20839), [HTML](https://arxiv.org/abs/2511.20839)
### Authors
Vladimer Khasia
### Background
该研究背景在于传统随机特征映射方法（如随机傅里叶特征）通过随机投影生成特征表示，但这可能导致特征之间的正交性较差且缺乏灵活性。Primal 框架利用质数平方根的数论独立性构建了可调谐的向量表示，通过引入 Besicovitch 性质来生成不重复的相位轨迹，以增强表示的稳健性和可控性。
### Innovation
Primal 框架的主要创新在于其同时考虑了静态和动态两种算法变体。StaticPrime 方法产生的时间位置编码能够接近理想的彻平正交性；而 DynamicPrime 是针对输入依赖性的特征映射可调谐投影层。这些特性通过单一缩放参数 σ 统一了两种数学效用类，使得在低频域该方法可以作为等距核映射有效线性化非凸几何结构（例如螺旋），而在高频域则通过混沌相位缠绕将投影转换为高熵非对称散列，适用于超维计算和隐私保护的 Split Learning。Primal 框架在正交性保留和分布紧密度上优于标准化高斯基线，展示其作为随机矩阵投影的受控且高效的替代方案。
### Conclusion
实验结果表明，Primal 框架在正交性和分布紧凑度方面优于标准化高斯基线。研究指出，Primal 框架为计算高效性和数学严谨性提供了替代方案，适用于神经网络中的特征表示和高效信号重建等应用。
## 87. `cs.AI` - SPACEx：使用SPACE模型探索开发人员生产力的度量标准 [PDF](https://arxiv.org/pdf/2511.20955), [HTML](https://arxiv.org/abs/2511.20955)
### Authors
Sanchit Kaul,Kevin Nhu,Jason Eissayou,Ivan Eser,Victor Borup
### Background
该实证研究揭示了确定性、单一维度生产力启发式方法的局限性，通过广泛的数据仓库挖掘实施数字化SPACE框架。研究利用来自开源仓库的数据集，结合广义线性混合模型（GLMM）和基于RoBERTa的情感分类，构建了一个全面的多维度生产力指标。分析结果表明，负面情感状态与提交频率之间存在统计学意义上的显著正相关，暗示了一种由挫败感驱动的反复修正过程。此外，研究发现分析贡献者互动的拓扑结构比传统的基于体积的度量标准在映射协作动态方面具有更高的准确性。
### Innovation
该研究创新性地引入了SPACE框架来综合分析开发人员的生产力，并通过广泛的数据仓库挖掘提供了新的度量标准，特别是通过GLMM和RoBERTa情感分类来构建一个多维度的生产力指标。研究揭示了负面情感对开发人员行为的影响，并证明了分析贡献者互动拓扑结构的重要性。
### Conclusion
该研究提出了一个综合生产力评分（CPS）来解决开发人员效能的异质性问题，强调了使用多维度、动态分析方法优化软件开发团队管理的重要性。
## 88. `cs.AI` - 规模化电动汽车分散协调下的鲁棒充电基础设施 [PDF](https://arxiv.org/pdf/2511.20943), [HTML](https://arxiv.org/abs/2511.20943)
### Authors
Chuhao Qin,Alexandru Sorici,Andrei Olaru,Evangelos Pournaras,Adina Magda Florea
### Background
电动汽车（EVs）的快速普及带来了分散充电控制的重大挑战。现有的分散方法能够有效地协调大量电动车辆，选择充电站以降低能源成本、防止电能峰值并保持驾驶员隐私。然而，当遇到严重的故障情况，例如充电站停用或充电请求突然增加时，这些方法表现不佳，导致了充电槽的竞争，出现排长队的情况，降低了驾驶员的舒适度。
### Innovation
该论文提出了一个新颖的合作学习为基础的协调框架，该框架允许电动汽车在个体舒适度与系统效率之间寻求平衡，即在不同站点容量和动态变化的空间-时间分布下，实现帕累托最优的权衡。该框架还建议电动车辆进行适应性充电行为，以在舒适度与效率之间调整优先级，实验结果显示当使用实际数据时，该方法在减少行驶时间和排队时间方面优于基准方法。研究表明，在不确定的充电条件下，能够在正确的时间表现出自私或利他行为的电动汽车驾驶员的等待时间比始终保持中等行为的驾驶员的等待时间要短。
### Conclusion
在高比例的充电站停用和敌对的电动汽车情况下，该方法还进一步证明了分散的电动车辆充电基础设施的鲁棒性和可靠性得到改善。该研究发现，电车用户在特定情况下展现出自我驱动或利他主义行为可以显著减少等待时间，同时提高分散充电基础设施的韧性和可信任度。
## 89. `cs.AI` - AI4X Roadmap: 人工智能在科学研究中的应用及其未来方向 [PDF](https://arxiv.org/pdf/2511.20976), [HTML](https://arxiv.org/abs/2511.20976)
### Authors
Stephen G. Dale,Nikita Kazeev,Alastair J. A. Price,Victor Posligua,Stephan Roche,O. Anatole von Lilienfeld,Konstantin S. Novoselov,Xavier Bresson,Gianmarco Mengaldo,Xudong Chen,Terence J. O'Kane,Emily R. Lines,Matthew J. Allen,Amandine E. Debus,Clayton Miller,Jiayu Zhou,Hiroko H. Dodge,David Rousseau,Andrey Ustyuzhanin,Ziyun Yan,Mario Lanza,Fabio Sciarrino,Ryo Yoshida,Zhidong Leong,Teck Leong Tan,Qianxiao Li,Adil Kabylda,Igor Poltavsky,Alexandre Tkatchenko,Sherif Abdulkader Tawfik,Prathami Divakar Kamath,Theo Jaffrelot Inizan,Kristin A. Persson,Bryant Y. Li,Vir Karan,Chenru Duan,Haojun Jia,Qiyuan Zhao,Hiroyuki Hayashi,Atsuto Seko,Isao Tanaka,Omar M. Yaghi,Tim Gould,Bun Chan,Stefan Vuckovic,Tianbo Li,Min Lin,Zehcen Tang,Yang Li,Yong Xu,Amrita Joshi,Xiaonan Wang,Leonard W.T. Ng,Sergei V. Kalinin,Mahshid Ahmadi,Jiyizhe Zhang,Shuyuan Zhang,Alexei Lapkin,Ming Xiao,Zhe Wu,Kedar Hippalgaonkar,Limsoon Wong,Lorenzo Bastonero,Nicola Marzari,Dorye Luis Esteras Cordoba,Andrei Tomut,Alba Quinones Andrade,Jose-Hugo Garcia
### Background
人工智能和机器学习正在重新定义我们进行科学研究的方式，通过扩展研究者可以探索、预测和设计的范围，而不是取代现有的方法。本文档提供了一个覆盖生物学、化学、气候科学、数学、材料科学、物理学以及自动化实验室和非传统计算等领域的前瞻视角，体现了AI辅助科学的研究现状。
### Innovation
文章提出了多个统一的主题，包括多样且可信的数据、可迁移的电子结构和原子模型以及集成到端对端科学工作流的AI系统。特别是在跨领域方面，文章强调了大型基础模型、主动学习和自动化实验室如何在保持可重复性和物理可解释性的前提下，闭合预测与验证之间的循环。
### Conclusion
这些观点概述了今天AI辅助科学所处的位置，指出了在数据、方法和基础设施方面存在的瓶颈，并为构建不仅更加强大，而且更加透明的AI系统指明了具体的前进方向，这些系统能够加速复杂现实环境中的科学发现。
## 90. `cs.AI` - MODEST: 多光学景深立体图集 [PDF](https://arxiv.org/pdf/2511.20853), [HTML](https://arxiv.org/abs/2511.20853)
### Authors
Nisarg K. Trivedi,Vinayak A. Belludi,Li-Yun Wang,Pardis Taghavi,Dante Lok
### Background
在自主机器人和增强现实等系统中，相机视觉的深度估计在真实光学条件下保持可靠仍然是一个核心挑战。尽管近期在深度估计和景深渲染方面取得了一定进展，但由于缺少大规模、高保真的真实双目单反相机数据集，研究仍受到限制，这限制了模型在合成数据上训练后的实际应用和评估。现有研究普遍表明，基于合成数据的模型在实际场景中的泛化能力受限。
### Innovation
我们提出了首个高分辨率（5472×3648像素）的双目单反相机数据集，包含18000张图像，系统地变换了焦距和光圈，跨越复杂的现实场景，捕捉了专业相机系统的光学现实性和复杂性。通过9个不同复杂度、照明和背景的场景，每场景分别用两套相同的相机架分别以10种焦距（28-70毫米）和5种光圈（f/2.8-f/22）拍摄，生成50种不同的光学配置合共2000张图像。这种全面的光学覆盖范围能够用于单目和立体深度估计、浅景深渲染、去模糊、三维场景重构和新颖视图合成的控制分析。每个焦距配置都有对应的校准图像集，支持经典方法和学习方法对于固有和外在校准的评估。数据集包含具有挑战性的视觉元素，如多尺度的光学幻象、反射表面、镜子、透明玻璃墙、细粒度的细节以及自然/人工的环境光变化。这项工作旨在弥合合成训练数据与真实相机光学之间的现实差距，并展示了当前最先进的单目、立体深度和景深方法面临的挑战。
### Conclusion
通过发布此数据集、校准文件和评估代码，旨在支持真实世界光学泛化的可重现研究，并展示了与当前最先进的单目、立体深度和景深方法相关的挑战。
## 91. `cs.AI` - 开放词汇集组成解释在神经元对齐中的应用 [PDF](https://arxiv.org/pdf/2511.20931), [HTML](https://arxiv.org/abs/2511.20931)
### Authors
Biagio La Rosa,Leilani H. Gilpin
### Background
神经元是深度神经网络的基本构建模块，它们之间的互连使得人工智能能够实现前所未有的成果。为了理解神经元如何编码信息，组成解释通过概念之间的逻辑关系来表达神经元激活与人类知识的空间对齐。然而，这些解释依赖于人工标注的数据集，这限制了它们的应用范围，仅局限于特定领域和预定义的概念。
### Innovation
本文提出了一个针对视觉领域的框架，使得用户可以对任意概念和数据集进行神经元探查。该框架利用开放词汇集语义分割生成的掩码来计算开放词汇集组成的解释。整个框架分为三个步骤：指定任意概念、使用开放词汇集模型生成语义分割掩码、从这些掩码中推导组成解释。
### Conclusion
论文在定量指标和人类可解释性方面将提出的框架与以前计算组成解释的方法进行了比较，分析了从人工标注数据到模型标注数据的解释差异，并展示了提出的框架在叙述随任务和感兴趣属性变化的解释方面的灵活性特点。
## 92. `cs.AI` - BUSTR：基于描述感知的医学影像-语言模型乳腺超声文本报告生成 [PDF](https://arxiv.org/pdf/2511.20956), [HTML](https://arxiv.org/abs/2511.20956)
### Authors
Rawa Mohammed,Mina Attin,Bryar Shareef
### Background
目前，自动放射学报告生成（RRG）在乳腺超声（BUS）方面的应用受到缺乏成对的图像-报告数据集以及大型语言模型存在幻觉风险的限制。BUSTR提供了一种多任务视觉-语言框架，能够在无需成对的图像-报告监督的情况下生成BUS报告。
### Innovation
BUSTR 框架通过结构化描述（如 BI-RADS、病理学、组织学）和影像组学特征构建报告；使用多头Swin编码器通过多任务损失训练描述感知视觉表示，该编码器在特定数据集描述集上进行训练；并使用多层次目标对输入和输出表示进行余弦相似性对齐，该目标结合了标记级交叉熵损失与输入和输出表示之间的余弦相似性对齐损失。
### Conclusion
BUSTR 在两个公开的 BUS 数据集 BrEaST 和 BUS-BRA 上进行了评估，结果表明，此描述感知视觉模型在联合标记级和对齐损失训练下，能够提升自动报告指标和临床效果指标，特别是 BI-RADS 类别和病理学这样的关键目标，而不必依赖成对的图像-报告数据。相关源代码可在指定网址找到。
## 93. `cs.AI` - 结构感知原型引导的信任多视图分类 [PDF](https://arxiv.org/pdf/2511.21021), [HTML](https://arxiv.org/abs/2511.21021)
### Authors
Haojian Huang,Jiahao Shi,Zhe Liu,Harold Haodong Chen,Han Fang,Hao Sun,Zhongjiang He
### Background
当前的可信多视图分类(TMVC)方法主要依赖于视图内部节点之间的全局密集邻居关系来建模视图内部依赖关系，导致高的计算成本且难以直接保证跨视图关系的一致性。此外，这些方法通常通过手动分配的权重来聚合不同视图的证据，缺乏确保学习到的多视图邻居结构在分类空间内部的一致性的保证，从而影响分类结果的信任度。
### Innovation
本文提出了一种新的TMVC框架，引入了原型来表示每个视图的邻居结构。通过简化视图内部邻居关系的学习，并实现视图内部和视图之间的结构动态对齐，该方法促进了跨视图一致性的高效发现。
### Conclusion
在多个公开的多视图数据集上的广泛实验表明，本方法在下游性能和鲁棒性方面与流行的TMVC方法相比具有竞争力。
## 94. `cs.AI` - GuardTrace-VL：通过迭代安全监督检测不安全的多模态推理 [PDF](https://arxiv.org/pdf/2511.20994), [HTML](https://arxiv.org/abs/2511.20994)
### Authors
Yuxiao Xiang,Junchi Chen,Zhenchao Jin,Changtao Miao,Haojie Yuan,Qi Chu,Tao Gong,Nenghai Yu
### Background
当前，多模态大型推理模型（MLRMs）在视觉语言任务中广泛部署，并产生明确的中间推理过程，但仍可能出现包含不安全内容的推理轨迹。现有方法主要评估输入问题和最终答案的安全性，忽视了中间推理过程中的风险。这可能导致推理过程中产生隐性危险，如带有偏见的推理或违反政策的视觉上下文使用。
### Innovation
提出了一种名为GuardTrace-VL的视觉感知安全审计工具，用于全过程的图像-文本分析监控，避免忽视中间推理阶段的潜在安全风险。为了支持训练和评估，构建了包含多样策略提示生成和基于多模态模型及人工投票的GuardTrace数据集。同时提出了一种结合数据精炼过程的三阶段渐进式训练方案，让模型学习根据不同风险水平的细腻和依赖上下文的安全偏好。
### Conclusion
在所提出的涵盖领域内和领域外情景的测试集中，GuardTrace-VL模型在不安全推理检测任务上的F1分数达到了93.1%，比最先进的多模态安全防护方法提高了13.5%。
## 95. `cs.AI` - FANoise：针对鲁棒多模态表示学习的特征自适应噪声调制 [PDF](https://arxiv.org/pdf/2511.20997), [HTML](https://arxiv.org/abs/2511.20997)
### Authors
Jiaoyang Li,Jun Fang,Tianhao Gao,Xiaohui Zhang,Zhiyuan Liu,Chao Liu,Pengzhang Liu,Qixia Jiang
### Background
代表学习是现代机器学习的基本组成部分，广泛应用于文本检索和多模态理解。然而，学习健壮且通用的表示仍然是具有挑战性的。尽管先前的工作已经证明，通过主动噪声注入（一种数据增强方法）可以提升编码性能，但现有的大多数方法依赖于启发式或静态噪声，这忽视了在训练过程中特征分布的动态性。
### Innovation
论文从梯度和特征分布两个角度系统探讨噪声在表示学习中的作用，并提出了FANoise，一种特征自适应噪声注入策略。通过利用对比学习的动态特性，FANoise有效地减轻了噪声的负面影响，同时保留了其优势。在理论基础上进行的全面实验表明，FANoise在各种基础VLM模型上的一致性上提高了多模态任务的整体性能。
### Conclusion
全面的实验验证了在多模态任务中，FANoise策略能够提升整体性能，尤其是在基于InfoNCE损失的多模态表示学习框架中。
## 96. `cs.AI` - 使用自回归条件生成对抗网络进行概率性野火蔓延预测 [PDF](https://arxiv.org/pdf/2511.21019), [HTML](https://arxiv.org/abs/2511.21019)
### Authors
Taehoon Kang,Taeyong Kim
### Background
气候变化加剧了野火的频率和严重性，快速而准确地预测火势蔓延对于有效的缓解和应对至关重要。物理模拟器如FARSITE能够提供高保真的预测，但计算密集型，这限制了它们在实时决策中的应用。现有的深度学习模型往往产生过于平滑的预测，无法捕捉野火蔓延的复杂非线性动态。
### Innovation
本文提出了一种自回归条件生成对抗网络（CGAN）用于概率性野火蔓延预测。通过将预测任务视为自回归问题，模型学习序列状态转移，确保长期预测的稳定性。实验结果表明，基于CGAN的模型在整体预测准确性和火势边界界定方面都优于传统的深度学习模型。这些结果表明，对抗学习使模型能够捕捉野火蔓延的强烈非线性和不确定性，而不是简单地拟合像素平均值。此外，自回归框架使得可以系统地预测野火的时空演化。
### Conclusion
提出的基于CGAN的自回归框架增强了野火蔓延预测的准确性和物理可解释性，为及时响应和疏散规划提供了有希望的基础。
## 97. `cs.AI` - 即使有AI，找出双射关系仍然很困难：OpenEvolve在新颖双射构造中的机会与挑战 [PDF](https://arxiv.org/pdf/2511.20987), [HTML](https://arxiv.org/abs/2511.20987)
### Authors
Davis Brown,Jesse He,Helen Jenne,Henry Kvinge,Max Vargas
### Background
现有的基于AI的程序合成系统，如AlphaEvolve、OpenEvolve和ShinkaEvolve，为AI辅助的数学发现提供了一种新方法。这些系统利用大量语言模型（LLMs）生成可读代码形式的候选解决方案，并通过进化过程逐步改进。这些系统主要应用于证明界限的问题，但程序合成方法适用于任何需要显式构造解决方案的问题。在此背景下，本文研究了OpenEvolve在组合双射发现中的应用。
### Innovation
本文将程序合成技术应用于组合双射发现，具体探讨了OpenEvolve在解决涉及Dyck路径的三个双射构造问题（两个已知问题和一个开放问题）时的表现。研究表明，尽管OpenEvolve显示出作为组合数学家工具的潜力，但发现新的研究级别双射仍然是当前前沿系统面临的挑战。
### Conclusion
OpenEvolve等系统为组合数学家提供了一种有价值的工具，但发现新水平的双射任务仍然复杂，强调了人类数学家在这些系统中的重要性。同时，本文为其他研究人员提供了有关使用这些系统探索双射发现领域的经验教训。
## 98. `cs.AI` - 环境特定目标图增强规划在基于大语言模型的开放世界强化学习中的应用 [PDF](https://arxiv.org/pdf/2511.20993), [HTML](https://arxiv.org/abs/2511.20993)
### Authors
Shanwei Fan
### Background
大型语言模型（LLMs）通过将任务分解为子目标为强化学习（RL）提供了强大的高层次规划能力。然而，实际应用中受限于规划执行对齐差的问题。这反映了抽象计划与可执行且环境兼容的行为之间的关键差距。导致这种对齐问题的主要原因有两点：（1）LLMs产生在目标环境中缺乏环境特定知识支撑的、虽有语义合理性但不切实际或无关的子目标；（2）单一LLM规划混淆了生成与自我验证，导致过分自信但实际上不可靠的子目标，在执行过程中频繁失败。
### Innovation
本文提出了一种名为Subgoal Graph-Augmented Actor-Critic-Refiner（SGA-ACR）的方法框架，结合环境特定子目标图和结构化实体知识，采用多LLM规划管道将生成、批判和细化明确分离，产生可执行和可验证的子目标。此外，引入了子目标追踪器，监测执行进度，提供辅助奖励，并适应性更新子目标图，以维持计划和行动之间的对齐。
### Conclusion
实验结果展示了在开放世界游戏‘Crafter’上的22个不同任务上，所提出方法的有效性。
## 99. `cs.AI` - 知识缔造视界：一种多模态实体感知检索增强生成框架用于新闻图像描述 [PDF](https://arxiv.org/pdf/2511.21002), [HTML](https://arxiv.org/abs/2511.21002)
### Authors
Xiaoxing You,Qiang Huang,Lingyu Li,Chi Zhang,Xiaopeng Liu,Min Zhang,Jun Yu
### Background
新闻图像描述旨在通过结合视觉内容和相关文章中的上下文线索生成记者式描述。虽然在最近的技术进步中取得了进展，但现有方法仍面临三个关键挑战：（1）信息不完整，（2）跨模态对齐较弱，（3）视觉实体定位不佳。
### Innovation
为了应对这些挑战，我们提出了MERGE（多模态实体感知检索增强生成框架），这是首个专为新闻图像描述设计的框架。MERGE构建了一个以实体为中心的多模态知识库（EMKB），集成了文本、视觉和结构化知识，有助于丰富背景检索。通过多层次假设-描述策略提高跨模态对齐，并通过基于图像内容的动态检索增强视觉实体匹配。
### Conclusion
在GoodNews和NYTimes800k上的广泛实验表明，MERGE显著优于最先进的基线方法，CIDEr增益分别为+6.84和+1.16，命名实体识别的F1分数分别提高了+4.14和+2.64。值得注意的是，MERGE在未见过的Visual News数据集上也表现出良好的泛化能力，CIDEr和F1分数分别提高了+20.17和+6.22，显示出强大的鲁棒性和领域适应性。
## 100. `cs.AI` - 在大型音频语言模型中实现音频标记压缩的进展 [PDF](https://arxiv.org/pdf/2511.20973), [HTML](https://arxiv.org/abs/2511.20973)
### Authors
Saurabhchand Bhati,Samuel Thomas,Hilde Kuehne,Rogerio Feris,James Glass
### Background
大型音频语言模型（LALMs）在从语音识别到一般音频理解等多种任务中表现出色。然而，这些模型在处理长音频和在资源受限平台（如边缘设备）上运行时受到限制，原因在于注意力机制的二次复杂性和音频信号的高标记率。为了克服这些挑战，研究人员探索了无监督分割、均匀平均池化等技术，减少LALM音频编码器生成的音频标记数量，在这些标记被传递给LLM解码器之前。为了减轻压缩表示可能引入的性能下降，研究采用低秩适配器对模型进行微调。
### Innovation
本文提出了一种技术，通过无监督分割和均匀平均池化减少LALM音频编码器生成的音频标记数量，而在传递给LLM主干前保留这些标记。为减少性能下降的影响，研究中采用了低秩适配器进行微调。实验结果表明，压缩的LALMs在自动语音识别和语音到语音翻译等任务中，可以将输入音频标记数量最多减少三倍，同时接近帧级LALMs的性能。
### Conclusion
通过压缩表示和低秩适配器微调，本文展示了在保持性能的同时减少大型音频语言模型的输入音频标记数的可能性，从而提高了这些模型在长音频任务和资源受限平台上的可用性。
## 101. `cs.AI` - 在上下文学习中的语义锚点：为什么小规模LLM无法翻转标签 [PDF](https://arxiv.org/pdf/2511.21038), [HTML](https://arxiv.org/abs/2511.21038)
### Authors
Anantha Padmanaban Krishna Kumar(Boston University)
### Background
该研究探讨了在上下文学习（ICL）中，是否可以克服预训练标签的语义，还是仅仅在现有语义基础之上进行改进。研究者通过将LLM视为依据提示分类器，对比自然演示（正确标注）和倒置演示（系统性颠倒标签意义）的行为差异来探讨这一问题。研究分解了ICL行为，并引入了语义翻转率这一概念，即在颠倒语义下正确性指标。
### Innovation
研究提出了一种新颖的方法，通过自然演示与倒置演示来研究ICL行为。通过分解ICL行为为三个对齐度量（真理对齐、先验对齐和提示对齐），并定义语义翻转率作为在颠倒语义下正确性的度量。研究在八个分类任务和来自八个开源LLM中（1到12B参数）进行了测试，获得了与预训练语义基础的观点一致的结果。
### Conclusion
自然演示下，ICL可以提高准确性同时保持强先验对齐；大多数正确预测与零样本行为一致，即使先验较弱。倒置演示下，模型无法学习连贯的反向语义分类器：提示对齐的增加仅通过牺牲准确性实现，且在少量样本1到12B的设置中语义翻转率为零。ICL主要通过调整输入在预训练中学习的稳定语义方向上的投影来调整，指出少量样本提示的局限性，表明在这些规模下翻转标签语义需要超过ICL的干预。
## 102. `cs.AI` - 打破安全与能力权衡：可验证奖励强化学习在保持LLMs安全性的同时提升推理能力 [PDF](https://arxiv.org/pdf/2511.21050), [HTML](https://arxiv.org/abs/2511.21050)
### Authors
Dongkyu Derek Cho,Huan Song,Arijit Ghosh Chowdhury,Haotian An,Yawei Wang,Rohit Thekkanal,Negin Sokhandan,Sharlina Keshava,Hannah Marlowe
### Background
在微调大型语言模型（LLMs）以执行下游任务时，往往会在安全性和能力之间表现出一种根本性的权衡，即使在良性数据集上，提高任务性能也会损害安全对齐。这种退化不仅出现在监督微调（SFT）和基于人类反馈的强化学习（RLHF）等标准方法中，而且RLVR作为一种新兴的替代方法——通过客观可测量任务优化模型——其安全性影响尚未得到研究。
### Innovation
本文首次对RLVR的安全属性进行了全面的理论和实证分析。理论上，我们推导了在KL约束优化下的安全漂移上限，并证明了消除安全退化的条件。实验上，我们在五个对抗性安全基准上进行了深入实验，证明了RLVR可以在提升推理能力的同时维持或改善安全防护。我们的消融研究表明，优化算法、模型规模和任务领域的效果。研究结果挑战了固有的安全与能力权衡的不可避免性，证实了一种特定的训练方法可以在同时实现两个目标，为推理型LLMs的安全部署提供了见解。
### Conclusion
本文的工作发现了安全与能力之间的权衡并不是不可避免的，并展示了通过RLVR可以同时提升模型的安全性与性能。这一发现对于未来安全地部署具备推理能力的LLMs具有重要的指导意义。
## 103. `cs.AI` - 通过冲击回声信号和神经网络的数据驱动评估混凝土板的完整性 [PDF](https://arxiv.org/pdf/2511.21080), [HTML](https://arxiv.org/abs/2511.21080)
### Authors
Yeswanth Ravichandran,Duoduo Liao,Charan Teja Kurakula
### Background
混凝土桥梁的表层缺陷如分层、空洞和蜂窝状结构严重影响其耐久性，但这些缺陷难以通过肉眼检查或手动敲击准确检测。目前，这项研究提出了一个基于机器学习的冲击回声(IE)框架，该框架能够自动化缺陷定位和多类分类，从而解决上述难题。
### Innovation
该论文提出了一个利用机器学习的冲击回声（IE）框架，通过快速傅里叶变换（FFT）将原始IE信号转换为主导频段特征，并将其插值到空间图中以实现缺陷区可视化。该框架通过无监督k-means聚类和通过现场验证，展示了实验室数据训练的模型在实际应用中具有推广应用价值，支持大规模桥梁健康监测。
### Conclusion
该工作提出的方法增强了无损检测（NDE）的客观性、可扩展性和可重复性，为大规模桥梁智能监控提供了数据驱动的支持。训练在实验室数据上的模型在实际条件下具有良好的通用性，验证了在真实耦合、噪声和环境变化下的有效性，从而提高了桥梁健康监测的智能性和数据驱动技术的实用性。
## 104. `cs.AI` - 用Kolmogorov-Arnold网络头微调提升缅甸新闻分类 [PDF](https://arxiv.org/pdf/2511.21081), [HTML](https://arxiv.org/abs/2511.21081)
### Authors
Thura Aung,Eaint Kay Khaing Kyaw,Ye Kyaw Thu,Thazin Myint Oo,Thepchai Supnithi
### Background
在资源稀缺的语言如缅甸语中，分类任务通常只需要微调最终分类层，保持预训练编码器权重不变。虽然多层感知机（MLPs）很常用，但它们固定不变的非线性可能会限制表达能力并增加计算成本。
### Innovation
本研究探索了Kolmogorov-Arnold网络（KANs）作为分类头部的替代方案，评估了基于Fourier的FourierKAN、基于分段的EfficientKAN以及基于网格的FasterKAN，并在包括TF-IDF、fastText和多语言变压器（mBERT、Distil-mBERT）在内的各种嵌入中进行了测试。实验结果显示，KAN基头部与MLPs具有竞争力甚至更优秀。
### Conclusion
EfficientKAN与fastText结合取得了最高的F1分数（0.928），而FasterKAN提供了速度与准确性的最佳平衡。在变压器嵌入中，EfficientKAN与mBERT结合的F1分数为0.917，甚至与MLPs相当或略微更好。这些发现表明，KANs是低资源语言分类中MLPs的高效、富有表现力的替代方案。
## 105. `cs.AI` - Pygmalion Effect in Vision: Image-to-Clay Translation for Reflective Geometry Reconstruction [PDF](https://arxiv.org/pdf/2511.21098), [HTML](https://arxiv.org/abs/2511.21098)
### Authors
Gayoung Lee,Junho Kim,Jin-Hwa Kim,Junmo Kim
### Background
在三维重建中理解反射一直是长期的挑战，因为视点依赖的反射会混淆外观和几何形状。现有方法难以同时重建反射和几何结构，特别是在多视图图像中含有复杂反射时更为困难。
### Innovation
本文提出了一种创新框架，Pygmalion 效应在视觉中，通过图像到泥土的翻译，象征性地“雕刻”反射物体，从而先学习抑制镜面线索，同时保持几何内禀一致性。这种方法通过一个基于 BRDF 的反射分支与一个由泥土引导的分支结合，后者稳定几何并细化法线。该框架通过合成泥土样张进行联合训练，利用这些中性无反射监督信号来补充反射视图，从而在多个真实数据集和合成数据集上取得显著的法线准确性和网格完整性改进。
### Conclusion
我们的框架揭示了“去ış见”的威力，将光度量度转化为中性信号，可以成为反射物体几何结构学习的强先验信息。实验结果表明，该方法在法线精度和网格完整性上显著优于现有处理反射的方法。
## 106. `cs.AI` - FedAPA: 异质Wi-Fi CSI人群计数的自适应原型聚合的联邦学习 [PDF](https://arxiv.org/pdf/2511.21048), [HTML](https://arxiv.org/abs/2511.21048)
### Authors
Jingtao Guo,Yuyi Mao,Ivan Wang-Hei Ho
### Background
Wi-Fi信道状态信息（CSI）- 基础的感知提供了无侵害、无需设备的感知方法，例如人类活动识别和人群计数，但大规模部署受限于大规模站点特异性训练数据的需求。联邦学习为避免原始数据共享提供了一种方法，但也面临着异质感知数据和设备资源的挑战。
### Innovation
提出了一种名为FedAPA的协作Wi-Fi CSI基础感知算法，该算法采用自适应原型聚合（APA）策略为同伴原型分配基于相似性的权重，实现自适应客户端贡献，为每个客户端生成个性化的全局原型，而非固定的加权聚合。在局部训练中，采用结合分类学习和表示对比学习的混合目标，以对齐局部和全局知识。提供了FedAPA收敛性的分析，并在具有六个环境和多达20人的实际分布式Wi-Fi人群计数场景中进行了评估。
### Conclusion
结果显示，在准确度、F1分数、平均绝对误差（MAE）和通信开销方面，我们的方法均优于多个基线。具体来说，FedAPA实现了至少9.65%的准确度增加，9%的F1分数提升，减少0.29的MAE，并将通信开销减少了95.94%。
## 107. `cs.AI` - 基于上游增强的动态分层对比学习方法在MILP分支中应用 [PDF](https://arxiv.org/pdf/2511.21107), [HTML](https://arxiv.org/abs/2511.21107)
### Authors
Tongkai Lu,Shuai Ma,Chongyang Tao
### Background
混合整数线性规划（MILP）问题是NP难问题中的一个基本类，得到学术界和工业界的广泛关注。分支定界（B&B）方法是求解MILP问题的主要方法，分支策略在B&B方法中是关键部分。近年来，基于神经网络的学习框架被开发出来以改善分支策略和解MILP问题的效率。然而，这些方法仍面临语义差异在不同深度的变化、上游节点稀缺以及强分支样本收集成本高等问题。
### Innovation
本文提出了一种名为ours的动态分层对比训练框架，用于MILP分支。该方法通过基于节点特征分布对分支定界节点进行分组，并训练基于图卷积神经网络的判别模型来逐层分离节点，学习节点的更细粒度表示。为了应对上游节点数据稀缺性，还提出了一种增强MILP生成方法，生成理论上等价的和扰动后的实例。这种方法能够有效建模节点之间的细微语义差异，显著提高分支准确性和求解效率，特别提升了对上游节点的表现。
### Conclusion
在标准MILP基准测试上的广泛实验表明，本方法能够提高分支准确性和降低求解时间，并能很好地推广到未见过的实例。
## 108. `cs.AI` - 基于变形感知的时间生成在阿尔茨海默病早期预测中的应用 [PDF](https://arxiv.org/pdf/2511.21114), [HTML](https://arxiv.org/abs/2511.21114)
### Authors
Xin Honga,Jie Lin,Minghui Wang
### Background
阿尔茨海默病（AD）是一种进行性脑部退化疾病，早期预测对减缓其进展至关重要。随着疾病的进展，患者通常会经历脑萎缩。当前的预测方法主要依赖于手动提取脑部图像的形态学变化进行分析，而提出了一种名为变形感知的时间生成网络（DATGN）的新方法，旨在自动化学习关于疾病进展的形态变化，以实现早期预测。
### Innovation
DATGN 方法最初通过插值不完整的 MRI 图像序列，随后通过双向时间变形感知模块引导网络生成遵循疾病进展的未来 MRI 图像，从而实现阿尔茨海默病的早期预测。实验结果表明，DATGN 生成的时间序列MRI图像在 PSNR 和 MMSE 图像质量评估中具有竞争力，并且将通过 DATGN 生成的合成数据集整合到 SVM、CNN 和 3DCNN 分类方法中，显著提高了 AD 与 NC、AD 与 MCI 和 NC 分类的准确性。
### Conclusion
该研究提出的方法 DATGN 在生成未来 MRI 图像的时间序列上表现良好，并通过生成的历史 MRI 图像显著提高了 AD 与 NC 及 AD 与 MCI 和 NC 分类的准确率，同时还直观地验证了生成的 MRI 图像与阿尔茨海默病相关的脑萎缩趋势一致，有助于早期预测疾病的进展。
## 109. `cs.AI` - MLPMoE：密集LLM MLP的零样本架构 metamorphosis 成为静态 MoE [PDF](https://arxiv.org/pdf/2511.21089), [HTML](https://arxiv.org/abs/2511.21089)
### Authors
Ivan Novikov
### Background
大规模语言模型（LLMs）通常以密集的变压器形式部署，每个 feed-forward 部分中的每个参数都会被激活用于每个标记。虽然这种结构在设计上比较简单，但它在计算上是低效的，因为推理成本与参数数量呈线性关系。最近的研究表明，在密集的前馈网络中存在一些稀疏的、半模块化的子结构可以进行有用的计算，但这些方法通常依赖于聚类、激活特征剖析、奇异值分解或需要校准数据的自定义路由。这项研究介绍了一种名为 MLPMoE 的无训练、确定性转换方法，它将变压器块中的密集MLP重新构建成一个静态的、高多元性的专家混合体。
### Innovation
MLPMoE 引入了一种简单的张量切片和求和方法，重新解读了张量并行的代数公式，将其作为拓扑变换而非分布式训练模式。此外，还提出了分形淡出（分形分支稀疏化）和补偿剪枝（方差保持分支减量）作为轻量级的结构稀疏机制。MLPMoE 转换方法在 Qwen2.5-0.5B-Instruct 和 DeepSeek-R1-Distill-Llama-8B 上的零样本实验中基本保持了参数数量的恒定，并且仅将代理困惑度度量值变化了不到 0.05%。对于 8B 模型，分形稀疏化移除了大约 20% 的MLP参数，同时保持困惑度在密集基线的 2% 以内。该方法完全在现有的检查点上后处理进行，无需使用梯度、校准集或路由器训练。
### Conclusion
MLPMoE 方法在保持模型性能的同时减少了大量参数，适用于大规模语言模型，并且完全不需要校准数据、路由器训练或训练梯度。代码已公开，为现有模型的高效率结构提供了新的途径。
## 110. `cs.AI` - 超越块聚合：三步金字塔索引增强视觉文档检索 [PDF](https://arxiv.org/pdf/2511.21121), [HTML](https://arxiv.org/abs/2511.21121)
### Authors
Anup Roy,Rishabh Gyanendra Upadhyay,Animesh Rameshbhai Panara,Robin Mills
### Background
传统文档中心性的检索管道通常从OCR开始，随后涉及脆弱的分片、表格解析和布局重建的手法。这些基于文本的工作流成本高昂、对布局的小幅变化敏感且容易丢失含有答案的空间线索。具有视觉信息的检索方法因其架构简洁和基准性能佳而逐渐成为一种强有力的选择。然而，这些依赖特定视觉主干的方法需要存储每页数百个片段嵌入，造成内存负担，影响大规模部署。
### Innovation
该论文提出了一种无需OCR且对模型无依赖性的多模态检索系统——VisionRAG。VisionRAG直接将文档作为图像索引，保留了布局、表格和空间线索，并避免了特定的提取承诺。其多层金字塔索引框架使用全局页面摘要、部分标题、视觉热点和事实级别的线索生成向量，这些总结充当轻量级检索代理。在检索过程中，它利用金字塔信号进行相互提升融合，生成稳健的排名。VisionRAG仅存储每页17至27个向量，与基于片段的方法一样高效，但保持了跨多模态编码器的灵活性。
### Conclusion
在金融文档基准测试上，VisionRAG达到了0.8051的准确率（top 10）和0.9629的召回率（top 100）。这些结果表明，无需OCR、以总结为导向的多模态检索是一种实用且可扩展的选择，可替代传统的文本提取管道。
## 111. `cs.AI` - 学习细胞感知的分层多模态表示以实现稳健的分子建模 [PDF](https://arxiv.org/pdf/2511.21120), [HTML](https://arxiv.org/abs/2511.21120)
### Authors
Mengran Li,Zelin Zang,Wenbin Xing,Junzhou Chen,Ronghui Zhang,Jiebo Luo,Stan Z. Li
### Background
了解化学扰动如何在生物系统中传播对于分子属性预测至关重要。虽然大多数现有方法仅关注化学结构，但最近的研究强调了细胞响应（如形态和基因表达）在塑造药物效果中的重要作用。然而，当前的细胞感知方法存在两个关键局限性：(1) 外部生物数据模态不完整，(2) 未能充分建模分子、细胞和基因组层面的层级依赖关系。
### Innovation
我们提出了CHMR（细胞感知的分层多模态表示），这是一种稳健的框架，可联合建模分子与细胞响应之间的局部和全局依赖性，并通过新的树型结构向量量化模块捕捉潜在的生物学层级关系。在9个公共基准数据集上评测了CHMR，涵盖728个任务，CHMR在分类和回归任务中分别平均提高了3.6%和17.2%，证明了层级感知的多模态学习在可靠和生物基础的分子表示中的优势。
### Conclusion
这些结果表明层级感知、多模态学习对于稳健和生物基础的分子表示具有优势，为集成生物医学建模提供了一种可泛化的框架。
## 112. `cs.AI` - SocialNav：基于人类启发式的基础模型用于社交感知的实体导航的训练 [PDF](https://arxiv.org/pdf/2511.21135), [HTML](https://arxiv.org/abs/2511.21135)
### Authors
Ziyi Chen,Yingnan Guo,Zedong Chu,Minghua Luo,Yanfen Shen,Mingchao Sun,Junjun Hu,Shichao Xie,Kuan Yang,Pei Shi,Zhining Gu,Lu Liu,Honglin Han,Xiaolong Wu,Mu Xu,Yu Zhang
### Background
关于受社会规范约束的身体导航的研究挑战仍然存在。SocialNav 是一种具有层级“脑-行动”架构的基石模型，能够理解高层的社会规范并生成遵守社会规范的低层次轨迹。
### Innovation
SocialNav 通过 SocNav 数据集培训，该数据集包含认知激活数据集和专家轨迹金字塔。提出了一个多阶段的培训管道，并首次提出了一种基于流的强化学习框架，用于身体导航，称为 Socially-Aware Flow Exploration GRPO（SAFE-GRPO），该框架通过模拟社会符合行为来训练模型。
### Conclusion
SocialNav 在导航成功和社交合规性方面都比当前最佳方法表现出了显著提升，取得了 +38% 的成功率和 +46% 的社交合规性率。
## 113. `cs.AI` - Maglev-Pentabot：使用深度强化学习的磁悬浮系统非接触式操控 [PDF](https://arxiv.org/pdf/2511.21149), [HTML](https://arxiv.org/abs/2511.21149)
### Authors
Guoming Huang,Qingyi Zhou,Dianjing Liu,Shuai Zhang,Ming Zhou,Zongfu Yu
### Background
非接触操控在多个工业领域中已成为一种变革性的方法，然而，现有的柔性2D和3D非接触操控技术通常局限于微米尺度，通常只能操作毫克级别的物体。本文的背景是对这种局限性的解决。
### Innovation
研究人员开发了一种名为Maglev-Pentabot的磁悬浮系统，利用深度强化学习（DRL）来开发能在克级别操控物体的复杂控制策略。创新点包括通过数值分析优化了电磁铁布局以最大化可控空间，并提出了动作重映射方法来解决由磁场强度非线性引起的样本稀疏问题，从而使DRL控制器能够收敛。
### Conclusion
实验结果表明Maglev-Pentabot具有灵活的操控能力，并且该系统能够泛化到未明确训练的任务中。此外，通过使用更大尺寸的电磁铁，该方法可扩展用于操控更重的物体，为工业规模的机器人应用提供了参考框架。
## 114. `cs.AI` - MNM : 多层次神经影像元分析与双曲脑-文本表示 [PDF](https://arxiv.org/pdf/2511.21092), [HTML](https://arxiv.org/abs/2511.21092)
### Authors
Seunghun Baek,Jaejin Lee,Jaeyoon Sim,Minjae Jeong,Won Hwa Kim
### Background
现有的神经影像学研究往往样本量较小，影响其可靠性。元分析通过整合不同研究的发现来识别大脑活动的一致模式，从而解决这一问题。然而，传统的方法依赖关键词检索或线性映射，往往忽略了大脑中的丰富层次结构。
### Innovation
本文提出了一种新颖的框架，利用双曲几何将神经科学文献与脑激活图映射到共享的双曲空间中，通过洛伦兹模型嵌入文本和相应的脑图像。该方法能够捕捉神经影像数据中内在的语义相似性和层次结构组织。在双曲空间中，该方法通过以下步骤进行多层次神经影像元分析：1) 对齐脑部和文本嵌入，实现语义对应，2) 引导文本和脑激活之间的层次关系，3) 保存脑激活模式内的层次关系。
### Conclusion
实验结果表明，本文的方法优于基线，提供了通过双曲脑-文本表示实现多层次神经影像元分析的稳健且可解释的范式。
## 115. `cs.AI` - 从比特到轮次：扩散语言模型的并行解码与探索 [PDF](https://arxiv.org/pdf/2511.21103), [HTML](https://arxiv.org/abs/2511.21103)
### Authors
Hengyu Fu,Baihe Huang,Virginia Adams,Charles Wang,Venkat Srinivasan,Jiantao Jiao
### Background
扩散语言模型(DLMs)近年来被证明是自回归语言模型(AR-LMs)的强大替代品。DLMs通过并行解码提供了与AR-LMs相当的准确性并且具有更快的推理速度。然而，依赖高置信度标记的标准DLM解码策略遇到了一个固有的信息论瓶颈，这限制了解码进度并最终减慢了生成速度。
### Innovation
本文通过理论和实验来验证，优先考虑高置信度标记本质上是低效的。高概率标记携带的信息几乎可以忽略不计，并且只依赖于这些标记限制了每轮有效进度。文章证明了解码轮次必须与样本的总信息（负对数似然）成线性关系，并且与每轮信息预算成反比，提出了一个新的原理，即比特到轮次原则。此外，提出了探索-然后-利用(ETE)解码策略，这是一种无需训练的解码策略，最大化了信息通过量和解码效率。ETE结合了跨块解码和高不确定性标记的目标探索，重新塑造条件分布并触发一连串的自信预测。
### Conclusion
实验验证了我们的理论边界，并证明ETE始终比仅依赖置信度的基线策略减少了解码轮次的数量，而不会损害生成质量。
## 116. `cs.AI` - 基于检索的实用元认知提示方法在讽刺检测中的应用 [PDF](https://arxiv.org/pdf/2511.21066), [HTML](https://arxiv.org/abs/2511.21066)
### Authors
Michael Iskandardinata,William Christian,Derwin Suhartono
### Background
尽管最近在神经网络方法方面取得了进展，但自然语言处理（NLP）领域中的讽刺检测仍然是一个具有挑战性的任务。现有的预训练语言模型（PLMs）和大型语言模型（LLMs）是讽刺检测的首选方法，但由于讽刺文本的复杂性、语言多样性以及不同社区之间的文化差异，这一任务变得更加困难。此外，现有的模型在需要额外语境信息分析的词语或标记检测方面也表现出不可靠性。
### Innovation
本文提出了一个检索感知的方法，通过检索获取每个目标文本的上下文信息，结合非参数知识和模型本身的内部知识，以增强LSTM模型用于讽刺检测的表现。这种方法在Twitter Indonesia Sarcastic、SemEval-2018 Task 3和MUStARD三个数据集上进行了评估，结果表明非参数检索在Twitter Indonesia Sarcastic数据集上提高了9.87%的宏F1值，自我知识检索在SemEval和MUStARD数据集上分别提高了3.29%和4.08%。
### Conclusion
研究结果强调了上下文在增强LLMs的讽刺检测任务中的重要性，特别是在涉及文化特定的俚语、参考或LLMs未知的术语时。未来的研究将集中在优化相关上下文信息的检索以及研究检索质量对性能的影响。相关的实验代码可以在指定的URL中找到。
## 117. `cs.AI` - 使用平衡微调使大语言模型与生物医学知识对齐 [PDF](https://arxiv.org/pdf/2511.21075), [HTML](https://arxiv.org/abs/2511.21075)
### Authors
Zhenchao Tang,Fang Wang,Haohuai He,Jiale Zhou,Tianxu Lv,Jun Zhu,Shouzhi Chen,Minghao Yang,Yu Wang,Jiayang Wu,Yidong Song,Jianhua Yao
### Background
有效的后训练对于将大型语言模型（LLMs）与专门化的生物医学知识对齐以加速生命科学研究至关重要。然而，当前的方法面临许多限制。首先，生物医学推理涉及复杂的机制，通常由稀疏的文本数据表示。传统的监督微调（SFT）容易过度拟合表面级别的指令模式，而未能有效地掌握这些零散的科学知识。其次，强化学习（RL）在这种领域中不可行，因为定义有意义的奖励通常需要大量的实验验证（例如，湿实验验证药物反应），这使得实时反馈变得不可行。
### Innovation
我们提出了平衡微调（BFT），这是一种有效的后训练方法，设计用于从稀疏数据中学习复杂的推理，而无需外部奖励信号。BFT 通过两层加权机制运作：1. 在 token 层级，它通过预测概率来缩放损失，以稳定梯度并防止过度拟合；2. 在样本层级，它使用“最小组置信度”来适应性地提高对困难样本的学习。实验结果表明，BFT 在医学任务中显著优于 SFT，使其能够获得 SFT 漏掉的知识，并在生物过程推理方面超越基因分析的 GeneAgent。此外，BFT 生成的文本嵌入可以直接应用于下游任务，例如基因交互和单细胞扰动响应预测。
### Conclusion
BFT 促进了大型语言模型在生物医学研究中的广泛应用。
## 118. `cs.AI` - 带有脉冲神经网络的联邦学习中的隐私性 [PDF](https://arxiv.org/pdf/2511.21181), [HTML](https://arxiv.org/abs/2511.21181)
### Authors
Dogukan Aksu,Jesus Martinez del Rincon,Ihsen Alouani
### Background
脉冲神经网络（SNNs）因其较低的能耗，成为嵌入式和边缘AI的有前景的候选人。特别是在能量预算受限的场景下，它们相对于传统人工神经网络（ANNs）更为高效。与此同时，联邦学习（FL）已经成为在这种环境下占主导地位的训练范式，能够在设备上进行学习，同时限制原始数据的暴露。然而，梯度反转攻击是 FL 中的一种重要隐私威胁，可以将敏感的训练数据直接从共享的梯度中重构。尽管在传统 ANNs 中对此漏洞进行了广泛的研究，但 SNNs 的相关性还很少被探讨。
### Innovation
这是首个针对 SNNs 的梯度泄漏的全面实证研究。研究适应了不同的梯度泄露攻击到脉冲域，并揭示了与传统ANNs截然不同的结果：SNN的梯度不能可靠揭示输入内容，而是提供了噪声和时间上不一致的重构。这些结果表明，事件驱动的动力学和代理梯度训练相结合，显著减少了梯度的可解释性。这是首次系统研究用于脉冲架构的梯度反转攻击，强调了神经形态计算的内在隐私保护潜力。
### Conclusion
这项工作展示了SNNs在梯度隐私保护方面的潜力，并为未来研究提供了一个基准。
## 119. `cs.AI` - 哪些层会导致分布偏差？熵引导的自适应修剪方法用于扩散模型和流模型 [PDF](https://arxiv.org/pdf/2511.21122), [HTML](https://arxiv.org/abs/2511.21122)
### Authors
Changlin Li,Jiawei Zhang,Zeyi Shi,Zongxin Yang,Zhihui Li,Xiaojun Chang
### Background
大尺度的视觉生成模型，包括扩散和流模型，在视觉生成任务中展现了出色的表现。然而，将这些预训练模型应用于下游任务时，往往会导致参数冗余性显著增大。
### Innovation
提出了熵引导的自适应渐进修剪框架 EntPruner。首先，介绍了一种针对生成模型的熵引导修剪方法，该方法基于数据依赖的条件熵偏差（CED）评估每个模块的重要性。专门为生成模型设计了模块级别的重要度评估策略。其次，提出了一种零样本自适应修剪框架，可以在训练过程中自动决定何时以及如何修剪，以避免一次性修剪的缺点，防止模态坍缩并保持模型性能。
### Conclusion
在 DiT 和 SiT 模型上的广泛实验表明，EntPruner 能够实现最高 2.22 倍的推理速度提升，在保持 ImageNet 和三个下游数据集的生成质量的同时实现这一目标。
## 120. `cs.AI` - 使用熵导向优先渐进学习高效训练人体视频生成 [PDF](https://arxiv.org/pdf/2511.21136), [HTML](https://arxiv.org/abs/2511.21136)
### Authors
Changlin Li,Jiawei Zhang,Shuhao Liu,Sihao Lin,Zeyi Shi,Zhihui Li,Xiaojun Chang
### Background
随着扩散模型的发展，人体视频的生成技术取得了快速进步，然而，在高分辨率多帧数据上训练这些模型时，计算成本高和内存消耗大构成了显著的挑战。
### Innovation
提出了一个高效的训练框架---熵导向优先渐进学习（Ent-Prog），该框架专为人体视频生成中的扩散模型设计。通过引入条件熵膨胀（CEI）来评估不同模型组件在目标条件生成任务中的重要性，实现关键组件的优先训练。此外，提出了一个自适应渐进训练方案，该方案在训练过程中逐步增加计算复杂度以测量收敛效率，从而在减少训练时间和GPU内存消耗的同时保持模型性能。
### Conclusion
跨三个数据集的广泛实验表明，Ent-Prog框架在不牺牲生成性能的前提下，能够实现高达2.2倍的训练速度提升和2.4倍的GPU内存减少。
## 121. `cs.AI` - CAHS-Attack: CLIP-Aware Heuristic Search Attack Method for Stable Diffusion [PDF](https://arxiv.org/pdf/2511.21180), [HTML](https://arxiv.org/abs/2511.21180)
### Authors
Shuhan Xia,Jing Dai,Hui Ouyang,Yadong Shang,Dongxiao Zhao,Peipei Li
### Background
扩散模型在面对对抗性提示时表现出明显的脆弱性，提高攻击能力至关重要。现有工作经常依赖于对模型梯度的白盒访问或手工设计的提示工程，但在实际部署中由于访问限制或攻击效果差而不可行。
### Innovation
提出了CAHS-Attack，一种CLIP感知的启发式搜索攻击方法。该方法结合蒙特卡洛树搜索（MCTS）进行精细的后缀优化，利用受限遗传算法预先选择具有高潜力的对抗性提示作为根节点，每次模拟部署时保留最具语义破坏性的结果，以实现高效的地方搜索。这种方法在不同语义的短长提示中都取得了最先进的攻击性能。
### Conclusion
实验证明，SD模型的脆弱性可归因于其CLIP基础文本编码器的固有漏洞，暗示了当前从文本到图像管道的基本安全风险。
## 122. `cs.AI` - LLaVA-UHD v3: 渐进视觉压缩在多模态大语言模型中用于高效原分辨率编码 [PDF](https://arxiv.org/pdf/2511.21150), [HTML](https://arxiv.org/abs/2511.21150)
### Authors
Shichu Sun,Yichen Zhang,Haolin Song,Zonghao Guo,Chi Chen,Yidan Zhang,Yuan Yao,Zhiyuan Liu,Maosong Sun
### Background
在多模态大语言模型（MLLMs）中，视觉编码在后续进行标记凝练的标准架构已成为常态。许多近期的MLLMs更倾向于使用全局原分辨率视觉编码，而非基于切片的方法。研究发现，尽管全局编码能增强整体能力，但同时也带来了更大的计算负担。为了应对这一问题，本研究系统性地比较了视觉语言理解和注意力模式的行为，发现全球编码虽能提升能力，但这也伴随着更高的计算成本。
### Innovation
我们提出了LLaVA-UHD v3，这是一种基于我们提出的渐进视觉压缩（PVC）方法的MLLM。PVC方法包括两个关键模块：（i）细化的补丁嵌入，支持灵活的补丁大小缩放，适用于细粒度的视觉建模；（ii）窗口化标记压缩，分层部署在ViT层中，逐步聚合局部标记表示。通过这两个模块的联合调制，广泛预训练的ViT可以被重新配置为高效架构，同时保留较大的通用性。这一方法在广泛基准中表现出色，相较于MoonViT，降低首次令牌时间（TTFT）2.4倍；在基于相同架构的MLLM中，LLaVA-UHD v3进一步减少了TTFT 1.9倍，同时相比Qwen2-VL取得了竞争力。
### Conclusion
本研究通过LLaVA-UHD v3展示了我们的渐进视觉压缩方法在保持高效计算的同时，有效提升了MLLMs的性能。我们将在未来的研究中提供所有代码和检查点以支持进一步的高效MLLMs研究。
## 123. `cs.AI` - 当机器人遵循补丁指令：面向视觉-语言-行动模型的通用可转移补丁攻击 [PDF](https://arxiv.org/pdf/2511.21192), [HTML](https://arxiv.org/abs/2511.21192)
### Authors
Hui Lu,Yi Yu,Yiming Yang,Chenyu Yi,Qixin Zhang,Bingquan Shen,Alex C. Kot,Xudong Jiang
### Background
视觉-语言-行动（VLA）模型在面对对抗攻击时表现脆弱，但能够适应多种模型并在黑盒环境下有效工作的通用可转移攻击方法仍处于探索阶段。大多数现有方法针对特定模型且不能泛化到其他模型上。
### Innovation
提出了一种名为UPA-RFAS（通用补丁攻击通过鲁棒特征、注意力和语义）的统一框架，该框架在共享特征空间中学习单一物理补丁，并促进跨模型的迁移学习。UPA-RFAS结合了特征空间目标、L1偏差先验和排他性InfoNCE损失以诱导可移植的特征转移，鲁棒性增强的两阶段最小最大程序以及两种特定于VLA的损失：补丁注意力主导性和补丁语义错配。
### Conclusion
实验表明，UPA-RFAS能够在不同VLA模型、任务和视点之间一致地转移，暴露出实用的基于补丁的攻击面，并为未来的防御方法提供了有力的基础。
## 124. `cs.AI` - 使用时间到达碰撞指标提高切入机动中的碰撞规避性能 [PDF](https://arxiv.org/pdf/2511.21280), [HTML](https://arxiv.org/abs/2511.21280)
### Authors
Jamal Raiyn
### Background
该研究背景在于解决自动驾驶车辆（AVs）在处理切入场景时的碰撞避免挑战。切入场景是自动驾驶车辆面临的特殊挑战，现有的一些基于时间到达碰撞（Time-to-Collision, TTC）的方法可能不足以应对这一问题。
### Innovation
研究提出了一种新的碰撞避免策略，该策略结合了深度学习和TTC计算，能够预测潜在碰撞并确定适当的回避动作。这种方法相较于传统的基于TTC的方法有所创新，通过引入深度学习模型提高了对复杂碰撞场景的适应性和准确性。
### Conclusion
通过使用结合深度学习的TTC指标，该系统能够更好地预测和规避碰撞，为自动驾驶车辆提供更为有效的碰撞避免机制，从而提高其安全性能。
## 125. `cs.AI` - 基于音乐混合体条件的扩散模型生成分离人声 [PDF](https://arxiv.org/pdf/2511.21342), [HTML](https://arxiv.org/abs/2511.21342)
### Authors
Genís Plaja-Roglans,Yun-Ning Hung,Xavier Serra,Igor Pereira
### Background
音乐分析和实践过程中，将音乐混合体中的各个乐器和人声等元素分离出来是一个核心任务。通常使用优化过的神经网络来遮蔽或转换混合体的时间-频率表示，从而提取目标声源。然而，生成扩散模型提供了具有灵活性和泛化能力的新解决方案。
### Innovation
本文提出了一种基于扩散模型的人声分离方法，该模型在给定对应混合体的情况下生成独奏人声。这种方法提高了生成系统的效果，并在补充数据训练下达到了与非生成基准相当的客观评分。扩散采样的迭代性使用户能够控制质量与效率之间的权衡，并在需要时精炼输出。
### Conclusion
本文展示了扩散模型生成分离人声的方法，并通过消融研究强调了用户可配置参数的影响。
## 126. `cs.AI` - TALES: 一种评估大模型生成故事中文化再现的分类法与分析 [PDF](https://arxiv.org/pdf/2511.21322), [HTML](https://arxiv.org/abs/2511.21322)
### Authors
Kirti Bhagat,Shaily Bhatt,Athul Velagapudi,Aditya Vashistha,Shachi Dave,Danish Pruthi
### Background
全球范围内，数百万用户依赖于AI聊天机器人来满足他们的创作需求，引起了对聊天机器人如何代表多元文化广泛的关注。尽管如此，在开放式任务中评估文化代表性依然具有挑战性且研究不足。因此，本文通过构建TALES分类法，对大型语言模型生成的故事中多元印度文化身份的误代表现象进行了全面的评估。
### Innovation
首先，本文通过焦点小组和个体问卷调查等方式，构建了TALES分类法，该分类法搜集了9位在印度生活的人的经验洞察，并涵盖了14种不同语言。其次，本文使用TALES分类法对6个模型进行了大规模标注研究，从印度71个地区和158个进行标注的群众样本中获得了2925个标注结果。研究发现，88%的生成故事存在一种或多种文化不准确性，特别是在低资源语言和印度郊区产生的故事中更为常见。最后，本文将这些标注转化为TALES-QA，一个独立问题库，用于评估基础模型的文化知识。研究表明，尽管生成的故事中存在错误多样的内容，模型往往仍具备相应文化知识。
### Conclusion
本文通过大规标注研究和引入TALES分类法，揭示了大型语言模型生成故事中普遍存在的文化误代表现象。虽然生成的故事中存在大量文化不准的现象，但模型仍具备相应的文化知识。此外，本文还将这些标注转化为了TALES-QA，用于评估基础模型的文化知识。
## 127. `cs.AI` - Hybrid SIFT-SNN for Efficient Anomaly Detection of Traffic Flow-Control Infrastructure [PDF](https://arxiv.org/pdf/2511.21337), [HTML](https://arxiv.org/abs/2511.21337)
### Authors
Munish Rathee(School of Engineering, Computer and Mathematical Science (of Auckland University of Technology) Auckland, New Zealand),Boris Bačić(School of Engineering, Computer and Mathematical Science (of Auckland University of Technology) Institute of Biomedical Technologies (IBTec) Auckland, New Zealand),Maryam Doborjeh(Knowledge Engineering and Discovery Research Institute (KEDRI) (of Auckland University of Technology) Auckland, New Zealand)
### Background
本文介绍了SIFT-SNN框架，这是一种用于实时检测交通基础设施结构异常的低延迟神经形态信号处理流水线。该研究旨在解决在不同天气和光照条件下对桥梁等运输基础设施进行实时故障检测的需求。通过使用Scale-Invariant Feature Transform (SIFT) 对空间特征编码，结合一个基于延迟的尖峰转换层和Leaky Integrate-and-Fire (LIF) Spiking Neural Network (SNN) 进行分类，该系统在6000帧有标签的数据集上实现了92.3%的分类准确性，并且每帧的推理时间仅为9.5毫秒。
### Innovation
本文提出的方法整合了SIFT 和LIF SNN 来构建一个混合信号处理管道。该方法在保证低延迟的同时，通过将合成增强数据与实际数据结合，提高了系统的鲁棒性。与传统的卷积神经网络（CNN）相比，该混合管道能够保持空间特征的关联性，增强了解释性，并且能在嵌入式硬件上高效运行。不过，对于未见过的实际现场条件，模型的泛化能力仍需验证。
### Conclusion
SIFT-SNN框架通过部署在消费级系统上的原型进行了验证，应用在交通流量控制基础设施的移动混凝土屏障结构安全性监测上，该基础设施在全球20多个城市中广泛使用。该框架为交通流控制基础设施中的结构安全性监测提供了一种有效且低功耗的方法。
## 128. `cs.AI` - SurgMLLMBench: 外科场景理解的多模态大语言模型基准数据集 [PDF](https://arxiv.org/pdf/2511.21339), [HTML](https://arxiv.org/abs/2511.21339)
### Authors
Tae-Min Choi,Tae Kyeong Jeong,Garam Kim,Jaemin Lee,Yeongyoon Koh,In Cheul Choi,Jae-Ho Chung,Jong Woong Park,Juyoun Park
### Background
近期的多模态大语言模型（LLMs）研究突出显示了其在医学和外科应用场景中的潜力。然而，现有的外科数据集大多采用视觉问答（VQA）格式，且在术语和像素级分割方面存在异质性，限制了其一致的评估和实际应用。
### Innovation
本文提出了一种新的统一多模态基准——SurgMLLMBench，它专门设计用于开发和评估交互性多模态LLM，以理解外科场景，其中包含新收集的Micro-surgical Artificial Vascular anastomosIS (MAVIS)数据集。该基准集同时结合了像素级的仪器分割掩码和结构化的VQA注释，并在统一的分类下涵盖了腹腔镜、机器人辅助和显微外科等不同领域，使其能够进行超越传统VQA任务的全面评估，同时提供更为丰富的视觉对话交互。
### Conclusion
广泛的基础实验表明，一个基于SurgMLLMBench训练的单一模型可以实现跨领域的一致性能，并能有效泛化到未见数据集中。SurgMLLMBench将被公开发布，作为促进多模态外科人工智能研究、支持可重复评估和开发交互式外科推理模型的 robust 资源。
## 129. `cs.AI` - Hybrid-AIRL：利用监督专家指导提升逆强化学习 [PDF](https://arxiv.org/pdf/2511.21356), [HTML](https://arxiv.org/abs/2511.21356)
### Authors
Bram Silue,Santiago Amaya-Corredor,Patrick Mannion,Lander Willem,Pieter Libin
### Background
逆强化学习（AIRL）在解决强化学习（RL）中的稀疏奖励问题方面展现了潜力，通过从专家示范中推断密集奖励函数。但其在复杂、不完美信息环境中的表现尚未得到充分研究。为了探索这一领域，该研究在HULHE扑克这一稀疏、延迟奖励且不确定性大的环境中评估了AIRL。结果发现，AIRL难以推断出足够有用的信息性奖励函数。
### Innovation
该研究提出了Hybrid-AIRL（H-AIRL），这是一种通过结合基于专家数据的监督损失和随机正则化机制来改进奖励函数推断和策略学习的扩展方法。
### Conclusion
实验结果显示，H-AIRL在样本效率和学习稳定性方面优于AIRL，这表明将监督信号融入逆RL是有益的，并且H-AIRL为应对复杂的现实世界环境提供了有前景的框架。
## 130. `cs.AI` - 污染训练数据中具有自适应和激进拒绝的异常检测 [PDF](https://arxiv.org/pdf/2511.21378), [HTML](https://arxiv.org/abs/2511.21378)
### Authors
Jungi Lee,Jungkwon Kim,Chi Zhang,Kwangsun Yoo,Seok-Joo Byun
### Background
传统模型假设训练数据完全为正常数据，但在异常检测中处理污染数据是一个关键挑战。常规方法通过依赖固定的污染比例来减轻污染影响，但假设与实际比例之间的差异可能导致性能严重下降，特别是在噪声环境中，正常和异常数据分布重叠。
### Innovation
提出了一种创新方法——自适应和激进拒绝（AAR），使用修改后的z分数和基于高斯混合模型的阈值动态排除异常。AAR通过结合硬拒绝和软拒绝策略高效地平衡保留正常数据和排除异常之间的权衡。
### Conclusion
实验证明，AAR在两个图像数据集和三十个表格数据集上均优于最先进的方法，AUCROC提高了0.041。AAR能够提供可扩展且可靠的解决方案，增强对污染数据集的鲁棒性，为其在安全和医疗等领域的广泛应用铺平了道路。
## 131. `cs.AI` - RIA：一种优化的排序融入CTR预测方法 [PDF](https://arxiv.org/pdf/2511.21394), [HTML](https://arxiv.org/abs/2511.21394)
### Authors
Guoxiao Zhang,Tan Qu,Ao Li,DongLin Ni,Qianlong Xie,Xingxing Wang
### Background
现有方法通常将排名和重排序分开处理，导致了缺乏组合稀疏性和表示能力的评估模型，并且在严格的延迟限制下表现不佳。
### Innovation
提出了RIA（Ranking-Infused Architecture），这是一种统一的、端到端的框架，无缝集成了点估计和列表评估。RIA引入了四种关键组件：用户和候选双重变换器（UCDT）、上下文感知用户历史和目标模块（CUHT）、列表级多HSTU模块以及嵌入缓存（EC）模块。
### Conclusion
广泛的实验表明，RIA在公共和工业数据集上均优于最先进的模型，AUC和LogLoss指标均有显著提升。在进行在线A/B测试时，RIA将点击率（CTR）提高了1.69%，成本每干次曝光（CPM）提高了4.54%。
## 132. `cs.AI` - 定向预测变化 - 提高局部特征归因方法的高效和可信度评估 [PDF](https://arxiv.org/pdf/2511.21363), [HTML](https://arxiv.org/abs/2511.21363)
### Authors
Kevin Iselborn,David Dembinsky,Adriano Lucieri,Andreas Dengel
### Background
解释方法的有效性取决于其对底层机器学习模型的忠实度。特别是在高风险医疗环境中，临床医生和监管机构需要可靠的解释，以反映模型的决策过程。现有的忠实度度量标准，如Infidelity，依赖于蒙特卡洛近似计算，这要求进行大量的模型评估，并引入了由于随机抽样带来的不确定性。
### Innovation
本文提出了一种新的度量标准（定向预测变化，DPC），通过修改现有的预测变化(PC)指标，结合扰动和归因的定向，DPC实现了约十倍的速度提升并消除了随机性，提供了一个确定性和可重复的评价程序。DPC在两个数据集（皮肤病变图像和金融表格数据）和两种黑盒模型上进行了测试，结果表明DPC与PC结合能够全面、高效地评估基准导向和局部特征归因方法。
### Conclusion
DPC在4,744个独特的解释中，展示了能够全面、高效地评估基准导向和局部特征归因方法的能力，同时提供确定性和可重复的结果。
## 133. `cs.AI` - 自我引导防御：合成指南下的推理模型自适应安全对齐 [PDF](https://arxiv.org/pdf/2511.21214), [HTML](https://arxiv.org/abs/2511.21214)
### Authors
Yuhang Wang,Yanxu Zhu,Dongyuan Lu,Jitao Sang
### Background
推理模型在复杂推理任务中表现出色，但其安全性仍面临来自对抗性隐藏提示的严重挑战。这些提示具有隐蔽性和欺骗性，能够绕过现有的安全机制，导致生成有害内容。这表明需要一种适应性安全对齐的方法，使模型能够自主强化其防御能力以应对对抗性输入。
### Innovation
提出了Synthesized Guideline-based Adaptive Safety Alignment (SGASA)框架，该框架将模型生成的安全指南内化，以增强模型抵御有害对抗提示的能力，同时最小化对良性请求的无谓拒绝。SGASA框架包括两个关键阶段：数据预合成阶段生成安全指南和增强提示，以及对齐微调阶段利用监督微调（SFT）和直接偏好优化（DPO）将这些指南嵌入模型。
### Conclusion
在多个数据集上的广泛实验表明，SGASA显著提高了模型的安全性，验证了其适应性和可扩展的有效性。
## 134. `cs.AI` - 越多越好的对比融合：用于更高阶多模态对齐的对比融合 [PDF](https://arxiv.org/pdf/2511.21331), [HTML](https://arxiv.org/abs/2511.21331)
### Authors
Stefanos Koutoupis,Michaela Areti Zervou,Konstantinos Kontras,Maarten De Vos,Panagiotis Tsakalides,Grigorios Tsagatakis
### Background
在多模态机器学习中，学习跨多种模态的联合表示仍然是一个主要挑战。当前的主要方法通常局限于两两模态的对齐，而最近的一些方法虽然试图捕捉多个模态之间的高级相互作用，但往往未能充分保留模态对齐关系，从而影响它们在单一模态任务上的效果。
### Innovation
本文介绍了对比融合（ConFu）框架，这是一种扩展了传统两两对比目标的新方法，增加了额外的融合模态对比项，鼓励将模态对与第三种模态的联合嵌入。这种形式使ConFu能够捕捉两两对齐中无法恢复的高级依赖关系，如XOR-like关系，同时仍然保持强大的两两对应关系。
### Conclusion
在合成数据和真实的多模态基准测试中，ConFu在检索和分类任务上的表现具有竞争力，支持在一个对比框架内的统一一对一和两对一检索。
## 135. `cs.AI` - 按件进步：自回归图像生成的测试时缩放 [PDF](https://arxiv.org/pdf/2511.21185), [HTML](https://arxiv.org/abs/2511.21185)
### Authors
Joonhyung Park,Hyeongwon Jang,Joowon Kim,Eunho Yang
### Background
近年来，视觉自回归（AR）模型在文本到图像生成任务中展现了显著的能力，其工作方式类似于大型语言模型。尽管测试时的计算缩放带来了在复杂自然语言任务中增强推理输出的显著成功，但将这种方法推广到视觉AR模型的研究仍处于起步阶段，并且遇到了独特的挑战。现有的测试时缩放策略（如Best-of-N）可能效果不佳，它们在错误的生成轨迹上消耗了完整的计算资源，而线性扫描解码方案则缺乏整个画布的蓝图，导致仅能生成少量与提示对齐的候选方案，从而限制了缩放带来的效益。
### Innovation
本文提出了GridAR，这是一种测试时缩放框架，旨在从视觉AR模型中获取最佳结果。GridAR采用网格分区逐进生成方案，多个同一位置的候选方案在同一画布上生成，不可行的候选方案被早期剔除，可行的候选方案作为锚点来指导后续解码。同时，提出了基于布局的提示改写策略，通过检查部分视图来推断一个满足提示要求的可行布局，并引导后续图像生成以减轻缺乏蓝图的缺陷。实验结果表明，GridAR在有限的测试时缩放下达到了更高的质量结果：在N=4的情况下，它在T2I-CompBench++上的表现甚至优于Best-of-N（N=8），同时减少了25.6%的成本。此外，GridAR在自回归图像编辑任务中同样表现出色，与较大的N基线相比，在PIE-Bench上实现了13.9%的语义保留增益。
### Conclusion
综上所述，GridAR通过采用网格分区逐进生成方案和基于布局的提示改写策略，实现了在有限测试时缩放下高质量的自回归图像生成结果。与Best-of-N等方法相比，GridAR不仅提高了结果质量，还在成本和语义保持方面取得了显著优势。
## 136. `cs.AI` - FITRep: 通过大模型语言进行注意力引导项目表示 [PDF](https://arxiv.org/pdf/2511.21389), [HTML](https://arxiv.org/abs/2511.21389)
### Authors
Guoxiao Zhang,Ao Li,Tan Qu,Qianlong Xie,Xingxing Wang
### Background
在线平台上由于存在视觉和文本相似的近似重复项，用户体验往往会下降。现有的方法通常是将多模态嵌入的表示看作黑盒，忽略了结构关系（例如，主要元素和辅助元素），导致局部结构坍塌的问题。
### Innovation
受特征整合理论（FIT）的启发，提出了一种名为FITRep的注意力引导的、具有透明性的项目表示框架，用于细粒度的项目去重。该方法包括：(1) 概念层次信息提取（CHIE），利用MLLMs提取层次语义概念；(2) 结构保持降维（SPDR），一种基于UMAP的自适应方法，用于有效信息压缩；(3) 基于FAISS的聚类（FBC），一种基于FAISS的聚类，为每个项目分配唯一的簇ID。
### Conclusion
FITRep在美团广告系统中部署后，在线A/B测试中分别实现了3.60%的点击率（CTR）和4.25%的每千次展示成本（CPM）的增加，证明了其有效性和实际影响。
## 137. `cs.AI` - BotaCLIP：地球观测数据植物意识对比学习 [PDF](https://arxiv.org/pdf/2511.21194), [HTML](https://arxiv.org/abs/2511.21194)
### Authors
Selene Cerna,Sara Si-Moussi,Wilfried Thuiller,Hadrien Hendrikx,Vincent Miele
### Background
基础模型已经在多模态领域（如图像、文本和音频）中展现了学习丰富且可迁移表示的能力。在现代机器学习流程中，这些表示通常取代原始数据成为下游任务的主要输入。然而，如何在无需从零开始重新训练或产生显著计算成本的情况下，将预训练的基础模型适应特定领域以注入专业知识，依然是一个挑战。
### Innovation
本文提出了一种轻量级的多模态对比学习框架BotaCLIP，通过将高分辨率的航空图像与植物样点对齐，将预训练的地球观测基础模型（DOFA）适应特定领域。不同于通用嵌入，BotaCLIP通过对比学习与正则化策略减轻灾难性遗忘，内化生态结构。经过训练后，这些嵌入可以作为转移表示用于下游预测器。研究结果表明，BotaCLIP的表现优于从DOFA和监督基线得到的结果。
### Conclusion
本文展示了基础模型领域感知的适应如何将专家知识注入数据稀缺环境中，从而实现节俭的表示学习，并在植物存在预测、蝴蝶景观建模和土壤营养级群组丰富度估计等三项生态任务中取得了持续改进。
## 138. `cs.AI` - Monet: 在超出图像和语言的空间中进行潜在视觉推理 [PDF](https://arxiv.org/pdf/2511.21395), [HTML](https://arxiv.org/abs/2511.21395)
### Authors
Qixun Wang,Yang Shi,Yifei Wang,Yuanxing Zhang,Pengfei Wan,Kun Gai,Xianghua Ying,Yisen Wang
### Background
当前的视觉推理多依赖于文本链条的思维过程，通过注入视觉证据到中间推理步骤中提升视觉推理的有效性。然而，现有方法在模仿人类抽象的视觉思考方面存在局限性，其灵活性受限于外部工具，无法直接在潜在的视觉空间中进行推理。因此，需要一种新的训练框架来实现这一目标。
### Innovation
本文提出了Monet，一种训练框架，使多模态大型语言模型（MLLMs）能够直接在潜在的视觉空间中进行推理，通过生成连续嵌入来作为中间的视觉思维。文章还介绍了一种三阶段的监督微调（SFT）管道解决训练MLLMs时遇到的两个核心挑战：潜在视觉对齐的高计算成本和潜在嵌入的监督不足。此外，引入了VLPO方法，增强视觉潜能推理在策略梯度更新中的作用，并构建了一个高质量的文字-图像交替的CoT数据集Monet-SFT-125K。
### Conclusion
Monet-7B模型在现实世界的感知和推理基准测试中显示出一致的改进，表现出对挑战性的抽象视觉推理任务的良好泛化能力。通过对每个训练组件的作用的实证分析，文章揭示了早期尝试中的不足，并为未来视觉潜在推理的发展提供了见解。研究中的模型、数据和代码已公开发布。
## 139. `cs.AI` - 由SAM指导的遥感语义和运动变化区域提取在遥感变化描述中的应用 [PDF](https://arxiv.org/pdf/2511.21420), [HTML](https://arxiv.org/abs/2511.21420)
### Authors
Futian Wang,Mengqi Wang,Xiao Wang,Haowen Wang,Jin Tang
### Background
遥感变化描述是一项新兴且流行的研究任务，旨在用自然语言描述在不同时刻捕获的两幅遥感图像中的内容变化。现有方法通常使用CNN或Transformer提取图像的视觉特征或结合辅助任务来增强最终结果，但这些方法在区域认知方面较弱，且在时间对齐方面有限。
### Innovation
本文探索了使用SAM（Segment Anything Model）基础模型来提取区域级别的表示，并将感兴趣区域的知识注入到描述框架中。具体来说，本文采用CNN/Transformer模型提取全局视觉特征，利用SAM基础模型来划分语义和运动级别的变化区域，并利用一个特别构造的知识图谱来提供关于感兴趣对象的信息。这些异构信息通过交叉注意机制融合起来，并利用Transformer解码器生成最终的自然语言描述。
### Conclusion
广泛的实验结果表明，本文的方法在多个广泛使用的基准数据集上取得了最先进的性能。本文的源代码将发布在此 https URL。
## 140. `cs.AI` - 基于HPC基础设施的自动动态AI推理缩放：集成Kubernetes、Slurm和vLLM [PDF](https://arxiv.org/pdf/2511.21413), [HTML](https://arxiv.org/abs/2511.21413)
### Authors
Tim Trappen,Robert Keßler,Roland Pabel,Viktor Achter,Stefan Wesner
### Background
由于对人工智能（AI）推理的需求不断上升，尤其是高等教育领域，新型解决方案正在利用现有基础设施出现。高性能计算（HPC）已成为此类解决方案实施的一种普遍方法。然而，传统的HPC操作模式不适用于同步的、面向用户的动态AI应用程序工作负载。因此，本文提出了一种解决方案，该方案通过集成vLLM、Slurm和Kubernetes在超级计算机RAMSES上为语言模型语言模型（LLMs）提供服务。
### Innovation
本文提出了一种创新的解决方案，通过在超级计算机RAMSES上集成vLLM、Slurm和Kubernetes，以有效地处理100、500和1000个并发请求，仅产生约500毫秒的端到端延迟，从而适应动态AI应用程序工作负载的需求。
### Conclusion
初步基准试验表明，所提议的架构能够高效地扩展以满足100、500和1000个并发请求，其端到端延迟时间仅为约500毫秒。
## 141. `cs.AI` - 长期文档可读性评估的分层排名神经网络 [PDF](https://arxiv.org/pdf/2511.21473), [HTML](https://arxiv.org/abs/2511.21473)
### Authors
Yurui Zheng,Yijun Chen,Shaohong Zhang
### Background
可读性评估旨在评估文本的阅读难度。近年来，尽管深度学习技术逐渐应用于可读性评估，但大多数方法未能同时考虑文本长度或可读性标签的序数关系。
### Innovation
本文提出了一种双向可读性评估机制，能够捕获上下文信息，识别文中富含语义信息的区域，进而预测单个句子的可读性级别。这些句子级别的标签被用于辅助预测文档整体的可读性级别。此外，引入了一种对数排序算法，通过标签减法建模可读性级别的序数关系。
### Conclusion
在汉语和英语数据集上进行的实验结果表明，所提出模型的性能具有竞争力，并且优于其他基线模型。
## 142. `cs.AI` - SONAR: 频谱对比音频残差用于可泛化深度伪造检测 [PDF](https://arxiv.org/pdf/2511.21325), [HTML](https://arxiv.org/abs/2511.21325)
### Authors
Ido Nitzan HIdekel,Gal lifshitz,Khen Cohen,Dan Raviv
### Background
现有的深度伪造（DF）音频检测器仍然难以处理不在训练分布范围内的输入。主要原因是频谱偏见，即神经网络倾向于先学习低频结构再学习高频（HF）细节。这种偏见导致了深度伪造生成器在高频细节上留下瑕疵，而常用的检测器又未能充分利用这些高频残留物。
### Innovation
提出了频率引导下的Spectral-Contrastive Audio Residuals (SONAR)，这是一种明确将音频信号分解成互补表示的框架。XLSR编码器捕捉主要的低频内容，同一路径在学习可调节的SRM（可学习的空间分辨率建模）和值约束高频通带滤波器之后，提取微弱的高频残差。频率交叉注意力可以重新组合这两种视角，进行长范围和短范围频率依赖关系的组合。采用频率感知的Jensen-Shannon对比损失，拉近真实内容和噪声体，推远伪造嵌入，加速优化并使决策边界更清晰。
### Conclusion
SONAR在ASVspoof 2021和野生数据集上的评估结果显示出最先进的性能，并且比强基线模型快四倍。通过突出高频残差，SONAR展示了基于数据的、频率引导的对比框架，能够将潜在空间划分为两个不交的流形：自然-HF（真实音频）和扭曲-HF（合成音频），从而强化了决策边界。由于方案完全在表示层次上操作，因此该方法对于任何架构而言都是通用的，在未来的工作中可以无缝地集成到任何显示高频率线索决定性模型或模态中。
## 143. `cs.AI` - Merge and Bound：直接对权重进行操作的类增量学习 [PDF](https://arxiv.org/pdf/2511.21490), [HTML](https://arxiv.org/abs/2511.21490)
### Authors
Taehoon Kim,Donghwan Jang,Bohyung Han
### Background
类增量学习（Class Incremental Learning，CIL）是在逐步扩展的类别上进行模型训练的问题。现有的方法通常需要模型重新训练，导致新旧知识之间的冲突，即灾难性遗忘。为了改善这种情况，研究人员提出了各种方法来优化模型权重以减少遗忘新知识的同时保留旧知识。
### Innovation
提出了一种名为Merge-and-Bound（M&B）的新训练方法，直接在参数空间内操作模型权重进行优化。该方法通过两种权重合并类型——跨任务权重合并和同任务权重合并来统一模型。还提出了一个边界更新技术，以最小化累积更新并保持先前任务的知识，从而使新模型更接近旧模型，减少灾难性遗忘。
### Conclusion
M&B方法可以在不修改现有CIL方法的架构组件或重新调整学习目标的情况下无缝集成。我们对M&B进行了详尽的评估，并在标准CIL基准上展示了优于现有最先进方法的表现。
## 144. `cs.AI` - EvRainDrop：基于超图引导的完成以实现有效帧和事件流聚合 [PDF](https://arxiv.org/pdf/2511.21439), [HTML](https://arxiv.org/abs/2511.21439)
### Authors
Futian Wang,Fan Zhang,Xiao Wang,Mengqi Wang,Dexing Huang,Jin Tang
### Background
事件摄像头产生的事件流是空间稀疏但时间密集的。主流的事件表示学习算法通常使用事件帧、体素或张量作为输入。虽然这些方法在某些方面取得了显著进展，但它们在解决由于空间稀疏性引起的欠采样问题方面仍有困难。
### Innovation
本文提出了一种新颖的超图引导的空间-时间事件流填补机制，通过超图将不同时空位置的事件令牌连接起来，并利用上下文信息消息传递来填补这些稀疏事件。该方法可以在完成框架内灵活地将RGB令牌作为超图中的节点，实现多模态超图基础的信息填补。此外，通过自我注意力聚合不同时间步长的超图节点信息，实现有效的多模态特征学习和融合。
### Conclusion
在单标签和多标签事件分类任务上的广泛实验全面验证了该提出的框架的有效性。论文的源代码将在该网页上发布：this https URL。
## 145. `cs.AI` - 主观深度和时序Transformer：学习何时何地进行计算 [PDF](https://arxiv.org/pdf/2511.21408), [HTML](https://arxiv.org/abs/2511.21408)
### Authors
Frederico Wieser,Martin Benfeghoul,Haitham Bou Ammar,Jun Wang,Zafeirios Fountas
### Background
标准Transformer架构中固定的、均匀的计算分配会限制其效率和扩展性，尤其是在大规模模型和长序列方面。
### Innovation
引入了Subjective Depth Transformers (SDT) 和 Subjective Timescale Transformers (STT) 两种不同的架构，利用贝叶斯惊讶信号动态路由计算，学习在解码器中何时何地进行计算。SDT 通过交替的决策层和动态层实现，而STT 则将这种条件计算扩展到时序领域。
### Conclusion
这两种架构展示了训练中新颖性向预测驱动门控的预测转变，表明与惊讶驱动原则的对齐。它们在降低计算能力和准确性之间提供了初步见解，并通过减少自注意力计算和KV缓存需求分别降低了75%和50%，建立了更高效模型的道路。
## 146. `cs.AI` - 构建与基准测试：用于基于文本的钓鱼和垃圾邮件检测框架的标注电子邮件数据集 [PDF](https://arxiv.org/pdf/2511.21448), [HTML](https://arxiv.org/abs/2511.21448)
### Authors
Rebeka Toth,Tamas Bisztray,Richard Dubniczky
### Background
网络钓鱼和垃圾邮件邮件仍然是一个重大的网络安全威胁，攻击者越来越多地利用大型语言模型（LLMs）来生成极具欺骗性的内容。
### Innovation
本文介绍了包含网络钓鱼、垃圾邮件和合法邮件的全面电子邮件数据集，明确区分了人类生成和LLM生成的内容。每个邮件都标注了其类别、情感诉求（如紧迫性、恐惧、权威性）和潜在动机（如链接跟随、凭证盗窃、金融诈骗）。该研究对多个LLM进行了基准测试，评估它们识别情感和动机线索的能力，并选择最可靠的模型来标注整个数据集。为了评估分类的稳健性，还使用了几种LLM重新表述邮件内容，同时保持其意义和意图。最后，使用专家标记的真实数据对最先进的LLM进行了性能评估。
### Conclusion
结果强调了强大的网络钓鱼检测能力，但也揭示了从合法邮件中区分垃圾邮件的持续挑战。该数据集和评估框架有助于改进AI辅助的电子邮件安全系统。为了支持开放科学，所有代码、模板和资源都可以在我们的项目网站上找到。
## 147. `cs.AI` - 频率感知的令牌降低策略以提高高效的视觉变换器效率 [PDF](https://arxiv.org/pdf/2511.21477), [HTML](https://arxiv.org/abs/2511.21477)
### Authors
Dong-Jae Lee,Jiwan Hur,Jaehyun Choi,Jaemyung Yu,Junmo Kim
### Background
视觉变换器在各种计算机视觉任务中展示了卓越的性能，但它们针对标记长度的二次计算复杂性仍然是一个重大挑战。现有方法通过令牌降低策略来应对这一挑战，但这些方法往往忽略了自我注意的频率特性，比如秩塌缩和过度平滑现象。
### Innovation
本文提出了一种频率感知的令牌降低策略，通过对高频令牌和低频令牌的不同处理，提高了计算效率并保持了性能，同时缓解了秩塌缩现象。方法将令牌划分为高频令牌和低频令牌，并有选择地保留高频令牌，将低频令牌聚合为一个紧凑的直接电流令牌，以保留关键的低频成分。
### Conclusion
通过广泛的实验和分析，我们展示了这一方法能够显著提高准确率，同时减少计算开销并缓解秩塌缩和过度平滑现象。此外，我们还分析了已有的方法及其隐含的频率特性与局限性。
## 148. `cs.AI` - 在测试时计算中，推理视觉语言模型是否反比例缩放？基于干扰项的实证分析 [PDF](https://arxiv.org/pdf/2511.21397), [HTML](https://arxiv.org/abs/2511.21397)
### Authors
Jiyun Bae,Hyunjong Ok,Sangwoo Mo,Jaeho Lee
### Background
先前关于语言模型的研究报告了反比例缩放效应，其中文本干扰项导致推理解释更慢但效果较差。为了探究类似现象是否发生在多模态设置中，作者引入了Idis（带有干扰项的图像）视觉问答数据集，系统地在语义、数值和空间维度上变化干扰项。研究发现，视觉干扰项与文本干扰项在本质上有所不同：虽然反比例缩放现象依然存在，但添加视觉干扰项会导致准确率下降，而推理解释长度却没有增加。
### Innovation
作者提出了一个新的多模态数据集Idis，并通过对比语义、数值和空间维度上的干扰项，揭示了视觉干扰项与之前研究的文本干扰项在反比例缩放现象上的不同。此外，作者还展示了通过追踪推理过程中的属性计数获得更多关于干扰项、推理长度与准确率之间相互作用的关键洞察，进而提出了一种简单的提示策略来缓解推理模型中的偏差驱动预测。
### Conclusion
研究发现，在视觉语言模型中，反比例缩放现象依然存在，但视觉干扰项的增加并未增加推理长度却降低了准确率。通过分析推理过程中属性计数的变化以及对已有的视觉偏差基准（如Waterbirds）的研究，作者提出了一个简单策略来减轻推理模型中的偏差驱动预测。
## 149. `cs.AI` - 从观察到动作：工业设置中基于潜在动作的原始动作分割用于VLA预训练 [PDF](https://arxiv.org/pdf/2511.21428), [HTML](https://arxiv.org/abs/2511.21428)
### Authors
Jiajie Zhang,Sören Schwertfeger,Alexander Kleiner
### Background
论文背景介绍了现有的视频数据主要来源于标注数据，这些数据对于训练视觉-语言-动作（VLA）模型的需求来说是有限的，尤其是在工业环境中。研究人员拟通过利用未标注的持续工业视频流数据来扩充这些模型的训练资源。
### Innovation
创新点在于提出了一个新颖的无监督框架，用于从连续的工业视频流中解锁大量未标注的人类示范数据，以训练VLA模型。该方法首先通过训练一个轻量级运动编码器来捕捉动作动态，然后利用一个新颖的“潜在动作能量”度量建立无监督动作分割器，以发现并分割出语义上连贯的动作原语。最后，该框架能够输出分割后的视频片段及其对应的潜在动作序列，直接支持VLA的预训练。论文进一步展示了该系统的有效性和自动化水平。
### Conclusion
通过公共基准和自有的电动机组装数据集评估显示，该系统能够有效分割出工人在工作站执行的关键任务。同时，通过视觉-语言模型的聚类和定量评估，确认了发现的动作原语在语义上的连贯性。这标志着首次实现了从无结构工业视频中自动化提取和组织VLA预训练数据的端到端系统，为制造环境中的体感AI集成提供了可扩展的解决方案。
## 150. `cs.AI` - 训练内省行为：微调诱导7B模型可靠的内部状态检测 [PDF](https://arxiv.org/pdf/2511.21399), [HTML](https://arxiv.org/abs/2511.21399)
### Authors
Joshua Fonseca Rivera
### Background
Lindsey (2025) 通过四项实验研究语言模型的内省意识，发现模型有时能够检测和识别注入的激活模式，但成功率较低（最佳模型的成功率约为20%）。作者专注于其中一项实验——自我报告注入的“想法”，并探讨是否可以通过训练而不是等待自然出现来培养这种能力。通过对单个标记位置的暂时性注入进行微调，实验将一个70亿参数的模型从几乎完全失败（0.4% 的准确率，6.7% 的假阳性率）转变为可靠的检测（在验证集上的准确率达到85%，0%的假阳性率）。
### Innovation
通过微调处理，将一个在自我报告注入想法任务中近乎完全失败的70亿参数模型转变为能够可靠检测内省行为的模型。这种方法使模型能够检测和报告单个标记位置注入的短暂想法，同时保持这些信息并跨后续生成步骤报告语义内容。实验结果满足了Lindsey提出的三个标准：准确、定位和内省性，同时展示了技能的可迁移性，即模型能够对未见过的概念向量产生正确的反应，但未完全证实Lindsey意义上的元认知表征。
### Conclusion
这项研究回答了Lindsey提出的一个开放问题：将“内省训练是否会帮助消除不同模型之间的差异”。研究结果显示，至少可以通过直接训练诱导出内省行为的一个组成部分，为内置AI透明度提供了途径。
## 151. `cs.AI` - Tool-RoCo: 多机器人合作中的代理工具自我组织大规模语言模型基准 [PDF](https://arxiv.org/pdf/2511.21510), [HTML](https://arxiv.org/abs/2511.21510)
### Authors
Ke Zhang,Xiaoning Zhao,Ce Zheng,Jiahong Ning,Dandan Zhu,Wenqi Zhang,Chen Sun,Toshiharu Sugawara
### Background
近年来，基于大规模语言模型（LLMs）的多智能体系统研究主要依赖于预定义的指挥调度，忽视了代理的自主性。因此，本文提出Tool-RoCo，一个基于RoCo的多机器人合作基准，用于评估LLMs在长期多智能体合作中的表现。Tool-RoCo通过引入合作工具，使用智能体之间的工具使用情况来评估多智能体的合作和自组织能力。
### Innovation
Tool-RoCo 的创新点在于，它提出了四个不同层度的LLM范式：集中式合作、集中式自组织、分散式合作和自组织。这些范式分别在不同的意义上体现了智能体的自主性。此外，Tool-RoCo 包含三个多机器人任务（SORT、PACK 和 CABINET），用于衡量格式和参数准确性以及通过工具使用措施智能体之间的协调。研究表明，当前LLMs倾向于保持智能体的激活状态，而不常主动去减少它们的激活性，这对自适应协调提出了新的挑战。
### Conclusion
Tool-RoCo 提供了一个系统性的基准来评估在多智能体任务中的LLM自主性和合作性。研究结果表明，合作工具在所有工具中的比例仅为7.09%，而激活工具占96.42%，这表明当前的LLMs倾向于维持智能体的激活状态而非从激发到抑制的自适应协调。Tool-RoCo 提供了一个重要的工具和方法来进一步研究和提高LLM的自主性和在多智能体任务中的协同工作能力。
## 152. `cs.AI` - Multimodal Robust Prompt Distillation for 3D Point Cloud Models [PDF](https://arxiv.org/pdf/2511.21574), [HTML](https://arxiv.org/abs/2511.21574)
### Authors
Xiang Gu,Liming Lu,Xu Zheng,Anan Du,Yongbin Zhou,Shuchao Pang
### Background
学习基于3D点云模型受到对抗攻击的重大威胁，这对安全敏感应用的可靠性造成了严重影响。现有防护方法存在计算开销大和泛化能力差的问题。
### Innovation
提出了一种新颖且高效的教师-学生框架，即Multimodal Robust Prompt Distillation (MRPD)，用于提炼鲁棒的3D点云模型。通过将学生点云模型的特征与来自三种不同教师的鲁棒嵌入对齐来学习轻量级提示，这三种教师分别处理深度投影、高性能3D模型和文本编码器。这种知识迁移受到了一个基于信心门控机制的引导，该机制动态平衡各种输入模态的贡献。最重要的是，由于在整个训练阶段进行蒸馏，所以在推理阶段不会产生额外的计算成本。
### Conclusion
广泛的实验证明，MRPD在多种白盒和黑盒攻击下显著优于最先进的防护方法，甚至在干净数据上也表现出更好的性能。本研究提出了一个新而实用的范例，通过高效利用多模态知识来构建稳健的3D视觉系统。
## 153. `cs.AI` - 以声速的速度前进：将神经代理推向高度湍流的跨音速区域 [PDF](https://arxiv.org/pdf/2511.21474), [HTML](https://arxiv.org/abs/2511.21474)
### Authors
Fabian Paischer,Leo Cotteleer,Yann Dreze,Richard Kurle,Dylan Rubini,Maurits Bleeker,Tobias Kronlachner,Johannes Brandstetter
### Background
神经代理在汽车流体力学中的广泛应用，特别是通过DrivAerML和DrivAerNet++等数据集，主要集中于具有大型尾流的平板流动。然而，将这些方法扩展到航空航天领域，尤其是跨音速区域，仍然具有挑战性，这是因为压缩流的高非线性和三维效应（如机翼尖涡）带来的复杂性。现有的航空航天数据集主要关注二维翼型，忽略了这些关键的三维现象。为了解决这一问题，该研究提出了一个新的数据集，该数据集包括跨音速三维机翼的CFD（计算流体动力学）模拟。该数据集包含大约30,000个具有独特几何形状和来流条件的体素级和表面场数据。这使得可以计算升力和阻力系数，为数据驱动的空气动力优化奠定了基础。
### Innovation
该研究提供了一种全新的数据集，涵盖了跨音速三维机翼的CFD模拟，包含约30,000个样本，涵盖独特的几何和入流条件。研究者评估了几种最先进的神经代理模型，包括Transolver和AB-UPT，重点在于评估这些模型在几何和入流变化情况下的泛化能力。AB-UPT在跨音速流场表现出强大性能，并能够生成对未见过翼型也具有一致性的物理上合理的升阻比前沿。
### Conclusion
研究结果表明，AB-UPT能够近似生成未见过几何形状的升阻比前沿，突显了它作为快速空气动力设计探索的有效工具的潜力。为了促进未来的研究，该数据集已开源，地址为 this https URL。
## 154. `cs.AI` - 基于Dyna-Q强化学习的预测性安全保障 [PDF](https://arxiv.org/pdf/2511.21531), [HTML](https://arxiv.org/abs/2511.21531)
### Authors
Jin Pin,Krasowski Hanna,Vanneaux Elena
### Background
获得强化学习的安全保证是实现实际任务应用的主要挑战之一。现有的安全防护措施通常采用随机安全行动采样或固定回退控制器，这忽略了不同安全行动对未来性能的影响。
### Innovation
提出了一种基于模型的强化学习代理在离散空间中的预测性安全性屏蔽。该安全性屏蔽基于安全的环境模型模拟，更新局部Q-函数，从而在保持硬性安全保证的同时提高性能。
### Conclusion
在网格世界的环境中，即使短期预测视窗也能足以识别最优路径。我们的方法对于分布转移（例如，模拟与现实之间的转移）具有鲁棒性，无需额外的训练便能适应这种变化。
## 155. `cs.AI` - Transformer-based Time Series Classification的机制可解释性 [PDF](https://arxiv.org/pdf/2511.21514), [HTML](https://arxiv.org/abs/2511.21514)
### Authors
Matīss Kalnāre,Sofoklis Kitharidis,Thomas Bäck,Niki van Stein
### Background
基于变换器的模型在各种机器学习任务中已成为最新的工具，包括时间序列分类，但其复杂性使得对内部决策机制的理解具有挑战性。现有的可解释性方法通常集中在输入-输出归因上，而忽略了内部机制的透明度。
### Innovation
本文通过将NLP中的机械可解释性技术（激活剪切、注意力梯度和稀疏自编码器）应用到专门设计用于时间序列分类的变换器架构中，解决了这一差距。研究系统地探查了单个注意力头和时间步在内部因果作用，揭示了模型中的因果结构。实验结果展示了信息在内部传播的因果图，并强调了关键的注意力头和时间位置对于正确分类的影响。此外，研究还证明了稀疏自编码器在发现可解释的潜在特征方面的潜力。
### Conclusion
研究为变换器可解释性的方法论做出了贡献，并提供了在时间序列分类任务中理解变换器性能功能机制的新型见解。
## 156. `cs.AI` - BAMAS: 结构预算意识型多智能体系统 [PDF](https://arxiv.org/pdf/2511.21572), [HTML](https://arxiv.org/abs/2511.21572)
### Authors
Liming Yang,Junyu Luo,Xuanzhe Liu,Yiling Lou,Zhenpeng Chen
### Background
多智能体系统（MAS）作为现代自主解决复杂任务的有效方法已经出现。随着这些系统的复杂性增加，预算成本成为实际部署中的重要考虑因素。然而，现有工作很少解决在明确预算约束下如何结构化多智能体系统的问题。
### Innovation
本论文提出了一种新型方法BAMAS，以构建具有预算意识的多智能体系统。首先通过整数线性规划（ILP）问题确定最优的大型语言模型集合，平衡性能和成本；接着通过基于强化学习的方法确定这些模型之间的协作方式；最后根据选定的智能体及其协作拓扑实现并执行该系统。
### Conclusion
BAMAS在三项代表性任务上的评估结果表明，能够在提供可比性能的同时将成本降低高达86%。
## 157. `cs.AI` - VacuumVLA: 通过统一吸盘和抓取工具提升VLA能力以实现复杂的机器人操作 [PDF](https://arxiv.org/pdf/2511.21557), [HTML](https://arxiv.org/abs/2511.21557)
### Authors
Hui Zhou,Siyuan Huang,Minxing Li,Hao Zhang,Lue Fan,Shaoshuai Shi
### Background
视觉-语言-动作（VLA）模型通过利用大规模预训练的视觉和语言表示，显著提升了通用机器人操作。现有的大部分VLA系统主要使用平行双指夹具作为默认末端执行器。然而，这类夹具在处理诸如擦拭玻璃表面或打开无把手抽屉等特定现实世界任务时存在固有的局限性，因其接触面积不足或缺乏粘附性。为了解决这些问题，我们提出了一种低成本的整合硬件设计方案，即结合机械双指夹具和真空吸取单元，使同一末端执行器能够在两种模式间切换或协同使用，从而扩大可行任务的范围。
### Innovation
我们设计了一种低成本的整合硬件系统，该系统结合了机械双指夹具和真空吸取单元，能够在一个末端执行器中切换或协同使用两种模式，提升了机器人处理复杂任务的能力。该系统在两个先进的VLA框架：DexVLA和Pi0中进行实验证明，证明了在搭载这个混合末端执行器的情况下，机器人能够成功执行双重夹具单独难以实现的复杂任务。
### Conclusion
实验结果表明，在提出的新混合末端执行器的支持下，机器人能够成功执行多种复杂任务，而这些任务对于传统的双指夹具单独工作是不切实际的。所有硬件设计和控制系统的相关材料都将进行公开发布。
## 158. `cs.AI` - 神经网络中的规模无关柯莫戈罗夫-阿诺尔德几何 [PDF](https://arxiv.org/pdf/2511.21626), [HTML](https://arxiv.org/abs/2511.21626)
### Authors
Mathew Vanherreweghe,Michael H. Freedman,Keith M. Adams
### Background
弗里德曼和穆林吉的研究表明，浅层多层感知机在处理合成三维任务时，会在训练过程中自发发展出柯莫戈罗夫-阿诺尔德几何（KAG）结构，但在真实高维场景下这一现象是否依然存在还不清楚，也不清楚这种几何结构在空间上表现出什么特征。
### Innovation
扩展了KAG分析方法，应用于MNIST手写数字分类（784维度）问题，使用2层多层感知机，并在不同尺度上进行系统性的空间分析。发现KAG在训练过程中自然出现，并且在多个尺度上表现出一致性，从局部7像素邻域到完整的28x28图像，并且不同的训练方法（标准训练和带有空间增强的训练）产生相同的定性模式。
### Conclusion
神经网络在学习真实高维数据时，自发地建立了有组织、规模不变的几何结构。
## 159. `cs.AI` - HarmonicAttack: 一种适应性跨域音频水印消除方法 [PDF](https://arxiv.org/pdf/2511.21577), [HTML](https://arxiv.org/abs/2511.21577)
### Authors
Kexin Li,Xiao Hu,Ilya Grishchenko,David Lie
### Background
随着高质量的人工智能生成音频的出现，带来了诸如信息误导运动和语音克隆欺诈等安全问题。为防止AI生成音频被恶意使用，人们提出了通过音频水印的方式，使得音频易于区分出真是音频和带有水印的，但那些试图滥用AI生成音频的人员可能会试图去除音频水印，因此研究有效的音频水印去除技术对评估当前音频水印方案的鲁棒性至关重要。之前的水印去除方案要么假设去除水印需要不切实际的知识，要么计算成本高昂，有可能得出当前水印方案的虚幻信心。
### Innovation
本文提出了HarmonicAttack，一种高效的方法，仅需要具备从目标方案生成水印的基本能力。HarmonicAttack使用在时间和频域都操作的双路径卷积自编码器，结合GAN风格的训练，来分离水印和原始音频。当与AudioSeal、WavMark和Silentcipher等最先进的水印方案进行对比时，HarmonicAttack展示了比前任方法更强的水印去除能力，并且几乎可以实时运行。而HarmonicAttack虽然需要训练，但它是可用于不同领域的样本，并能保持较高的性能。
### Conclusion
HarmonicAttack是一种有效的音频水印去除方法，不需要假设如何去除其生成的水印，也不需要为特定的水印支付昂贵的计算成本。虽然HarmonicAttack需要训练过程，但其适用于不同的音频样本，仍然能够保持良好的性能，显示出较好的鲁棒性。
## 160. `cs.AI` - Qwen3-VL 技术报告 [PDF](https://arxiv.org/pdf/2511.21631), [HTML](https://arxiv.org/abs/2511.21631)
### Authors
Shuai Bai,Yuxuan Cai,Ruizhe Chen,Keqin Chen,Xionghui Chen,Zesen Cheng,Lianghao Deng,Wei Ding,Chang Gao,Chunjiang Ge,Wenbin Ge,Zhifang Guo,Qidong Huang,Jie Huang,Fei Huang,Binyuan Hui,Shutong Jiang,Zhaohai Li,Mingsheng Li,Mei Li,Kaixin Li,Zicheng Lin,Junyang Lin,Xuejing Liu,Jiawei Liu,Chenglong Liu,Yang Liu,Dayiheng Liu,Shixuan Liu,Dunjie Lu,Ruilin Luo,Chenxu Lv,Rui Men,Lingchen Meng,Xuancheng Ren,Xingzhang Ren,Sibo Song,Yuchong Sun,Jun Tang,Jianhong Tu,Jianqiang Wan,Peng Wang,Pengfei Wang,Qiuyue Wang,Yuxuan Wang,Tianbao Xie,Yiheng Xu,Haiyang Xu,Jin Xu,Zhibo Yang,Mingkun Yang,Jianxin Yang,An Yang,Bowen Yu,Fei Zhang,Hang Zhang,Xi Zhang,Bo Zheng,Humen Zhong,Jingren Zhou,Fan Zhou,Jing Zhou,Yuanzhi Zhu,Ke Zhu
### Background
Qwen3-VL 是Qwen系列迄今为止最强大的视觉-语言模型，覆盖了一系列多模态基准测试，展示了卓越的性能。它能够支持高达256K令牌的互插上下文，自然地整合了文本、图像和视频。模型系列包括从密集型（2B/4B/8B/32B）到混合专家型（30B-A3B/235B-A22B）的多种变体，以适应不同的延迟-质量权衡。
### Innovation
Qwen3-VL 引入了三个关键升级：增强的互插-MRoPE，用于更强的空间-时间建模；DeepStack 集成，利用多级ViT特征提高视觉-语言对齐；文本基于的时间对齐，从T-RoPE 发展为显式的文本时间戳对齐，以实现更精确的时间定位。此外，Qwen3-VL 在密集型和混合专家型架构下，在相似的令牌预算和延迟限制下，实现了更优的表现。
### Conclusion
我们预见Qwen3-VL 将成为图像根基推理、自主决策和多模态代码智能实时工作流程中的基础发动机。
## 161. `cs.AI` - 低资源设备上的持续错误修正 [PDF](https://arxiv.org/pdf/2511.21652), [HTML](https://arxiv.org/abs/2511.21652)
### Authors
Kirill Paramonov,Mete Ozay,Aristeidis Mystakidis,Nikolaos Tsalikidis,Dimitrios Sotos,Anastasios Drosou,Dimitrios Tzovaras,Hyunjun Kim,Kiseok Chang,Sangdok Mo,Namwoong Kim,Woojong Yoo,Jijoong Moon,Umberto Michieli
### Background
随着AI模型在日常设备中的普及，预测错误成为了影响用户体验的关键问题。虽然现有的解决方案主要集中在错误检测，但鲜有有效的错误修正机制，特别是在资源受限的设备中。
### Innovation
我们提出了一种创新系统，旨在通过少量样本学习让用户能够修正AI误分类，并且这一系统需要极少的计算资源和存储空间。该系统将服务器端的基础模型训练与设备端的原型导向分类相结合，通过原型更新实现高效错误修正，而非重新训练模型。
### Conclusion
研究结果表明，该系统能够有效地在资源限制条件下（例如在Food-101和Flowers-102数据集上）实现超高的错误修正率（超过50%），同时保留了极低的学习遗忘（不到0.02%）和可以忽略的计算开销。通过在Android演示应用中的实施验证，证明了该系统在现实世界中的实用性。
## 162. `cs.AI` - 视觉变换器中非单调扩展机制 [PDF](https://arxiv.org/pdf/2511.21635), [HTML](https://arxiv.org/abs/2511.21635)
### Authors
Anantha Padmanaban Krishna Kumar(Boston University)
### Background
深度视觉变换器通常表现不如较浅的版本，这挑战了常见的扩展假设。为了理解这一现象，本文通过对ImageNet上的ViT-S、ViT-B和ViT-L进行系统的实证分析，揭示了一个普遍存在的三阶段悬崖-平台-攀升模式，表明表示深度演化的过程。
### Innovation
研究识别了视觉变换器中表示演化的三阶段模式（悬崖-平台-攀升），并发现更好的性能与[CLS]令牌的逐步边缘化有关，即从全局聚合中心转为分布式共识。同时，研究使用信息打乱指数量化了信息混合模式，并发现信息与任务之间的权衡关系在较深的ViT-L中出现的时间比在较浅的ViT-B中晚约10层，而这些额外的层与信息散播增加而非任务性能提升相关。这些发现表明，在这种范围内，变换器架构可能从精细校准的深度中获益更多，而非单纯增加参数量。
### Conclusion
研究结果表明，在这一范围内，变换器架构可能从精细校准的深度中获益更多，而非简单增加参数量。信息打乱指数提供了一个有效的诊断工具，并暗示了未来架构的设计目标。所有代码已公开发布。
## 163. `cs.AI` - 通过电信视角：所有训练样本都重要吗？ [PDF](https://arxiv.org/pdf/2511.21668), [HTML](https://arxiv.org/abs/2511.21668)
### Authors
Shruti Bothe,Illyyne Saffar,Aurelie Boisbunon,Hasan Farooq,Julien Forgeat,Md Moin Uddin Chowdhury
### Background
随着人工智能在电信领域的应用，如优化无线电接入网络和管理用户体验，数据量和训练需求急剧增加。电信数据往往噪音大、维度高、存储和处理成本高，且需要标注。尽管AI在其中扮演关键角色，标准工作流程仍然假设所有训练样本的重要性相同。然而，下一代系统需要准确、高效且节能的AI模型。本文挑战了这种平等的重要性假设，关注于研究和分析电信训练中各个样本的角色，并评估提出的模型是否优化了计算和能耗。
### Innovation
本研究通过样本级别的梯度分析，在多个训练周期内识别模型学习中的影响和冗余模式。基于此，提出了一个样本重要性框架，该框架根据样本的影响性优先选择数据，同时减少计算量而不牺牲准确性。在三个实际电信数据集上进行的实验表明，该方法在保持性能的同时减少了数据需求和计算开销，从而推动电信中可持续人工智能的目标。
### Conclusion
实验结果表明，该方法能够在保持性能的同时减少数据需求和计算开销，从而推动可持续人工智能的目标。
## 164. `cs.AI` - 注意力引导的斑块稀疏对抗攻击：针对视觉-语言-动作模型 [PDF](https://arxiv.org/pdf/2511.21663), [HTML](https://arxiv.org/abs/2511.21663)
### Authors
Naifu Zhang,Wei Tao,Xi Xiao,Qianpu Sun,Yuxin Zheng,Wentao Mo,Peiqiang Wang,Nan Zhang
### Background
近年来，嵌入式智能中的视觉-语言-动作（VLA）模型发展迅速。然而，现有对抗攻击方法需要昂贵的端到端训练，并且常常会产生明显的扰动斑块。
### Innovation
提出的ADVL framework直接在视觉编码器投影到文本特征空间的特征上添加对抗扰动。ADVL在低振幅约束下有效破坏下游动作预测，并通过注意力引导使扰动既集中又稀疏。引入了三种策略来增强敏感性、强制稀疏性和集中扰动。
### Conclusion
实验表明，在$L_{fty}=4/255$约束下，ADVL结合Top-K遮罩修改不到10%的斑块，同时攻击成功率接近100%。扰动集中在关键区域，几乎不可察觉，且单步迭代只需大约0.06秒，显著优于传统的基于斑块的攻击。总体而言，ADVL在低振幅和局部稀疏条件下有效削弱VLA模型的下游动作预测，避免了传统斑块攻击的高昂训练成本和显而易见的扰动，展示了攻击VLA特征空间的独特有效性和实际价值。
## 165. `cs.AI` - 声音、偏见和核心指称：语音翻译中性别可解释性研究 [PDF](https://arxiv.org/pdf/2511.21517), [HTML](https://arxiv.org/abs/2511.21517)
### Authors
Lina Conti,Dennis Fucci,Marco Gaido,Matteo Negri,Guillaume Wisniewski,Luisa Bentivogli
### Background
与文本相比，语音传递了诸如性别等演讲者的信息，这些信息通过音调等声学线索表达。这引发了模态特定的偏见问题。例如，在语音翻译（ST）中，从具有概念性性别的语言（如英语）翻译到性别模糊的术语在指代演讲者时被分配了语法性别的语言时，演讲者的音质特征可能会影响性别分配，这可能会导致性别误分类，无论是通过男性默认设置还是基于音质的假设。然而，ST模型如何进行这些决策目前仍不完全清楚。
### Innovation
研究发现了ST模型在不同语言对（en-es/fr/it）中分配性别给指代演讲者术语时所使用的机制。研究发现，模型不仅复制训练数据中的特定性别关联，还学会了更广泛的男性主导模式。尽管内部语言模型表现出强烈的男性偏见，但模型可以通过声学输入来逆转这些偏好。通过对比特征分析光谱图，研究揭示了性别准确性更高的模型依赖于一种未知机制：使用第一人称代词将性别化术语与演讲者关联起来，通过整个频率谱分布获取性别信息，而不仅仅是集中在音调上。
### Conclusion
研究揭示了ST模型在性别分配决策上的复杂机制，指出这种分配不仅依赖于训练数据中的特定联想，还涉及更广泛的男性主导模式。此外，研究强调了声学输入在帮助模型克服内部语言模型偏见中的关键作用。这为理解ST模型的性别分配决策提供了新的视角，并指出了未来研究的方向。
## 166. `cs.AI` - G$^2$VLM: 基于几何的统一3D重建和空间推理的视觉语言模型 [PDF](https://arxiv.org/pdf/2511.21688), [HTML](https://arxiv.org/abs/2511.21688)
### Authors
Wenbo Hu,Jingli Lin,Yilin Long,Yunlong Ran,Lihan Jiang,Yifan Wang,Chenming Zhu,Runsen Xu,Tai Wang,Jiangmiao Pang
### Background
视觉-语言模型（VLMs）在空间智能方面仍存在不足，特别是在空间理解和推理任务上表现不佳。这主要是因为缺乏一种可以从2D图像重建3D空间的视觉几何学习过程。因此，该研究旨在填补这一空白。
### Innovation
提出了基于几何的几何指导视觉语言模型（G$^2$VLM），它整合了空间3D重建和空间理解两个基本方面。G$^2$VLM 通过上下文学习和交替推理，直接利用学习到的3D视觉几何特征来预测3D属性，从而增强空间推理任务。研究表明，该模型在3D重建任务中表现与最先进的前馈3D重建模型相当，并在空间理解和推理任务中超越或持平这些模型。
### Conclusion
通过结合强大的语义视觉语言模型和低级3D视觉任务，G$^2$VLM 成为一个强大的基线模型，有望解锁更多未来应用，如3D场景编辑。
## 167. `cs.AI` - Escaping the Verifier: Learning to Reason via Demonstrations [PDF](https://arxiv.org/pdf/2511.21667), [HTML](https://arxiv.org/abs/2511.21667)
### Authors
Locke Cai,Ivan Provilkov
### Background
目前训练大型语言模型（LLMs）进行推理通常依赖于带有任务特定验证器的强化学习（RL）。然而，许多现实中的推理密集型任务缺乏验证器，尽管存在大量未充分利用的专家演示，这些演示对于推理导向的训练十分宝贵。
### Innovation
本文提出了一种名为RARO（相对对抗推理优化）的方法，通过逆强化学习（Inverse Reinforcement Learning）仅利用专家演示来学习强大的推理能力。该方法设置了一个对抗互动：策略（生成器）学习模仿专家的答案，而评论家（判别器）学习比较和区分策略和专家的答案。本方法通过RL联合训练策略和评论家，同时确定了实现稳健学习的关键稳定技术。
### Conclusion
实验结果表明，RARO在所有评价任务（Countdown、DeepMath和诗歌创作）上显著优于强验证器免费基准，且拥有与验证任务中RL相同的稳健扩展趋势。这些结果证明，本方法能够仅从专家演示中有效提取强大的推理表现，即使在任务特定验证器不可用时也能实现稳健的推理学习。
## 168. `cs.AI` - ToolOrchestra: 通过高效模型与工具编排提升智能 [PDF](https://arxiv.org/pdf/2511.21689), [HTML](https://arxiv.org/abs/2511.21689)
### Authors
Hongjin Su,Shizhe Diao,Ximing Lu,Mingjie Liu,Jiacheng Xu,Xin Dong,Yonggan Fu,Peter Belcak,Hanrong Ye,Hongxu Yin,Yi Dong,Evelina Bakhturina,Tao Yu,Yejin Choi,Jan Kautz,Pavlo Molchanov
### Background
大型语言模型是强大的通用工具，但在解决诸如人类最后考试（HLE）等深层次和复杂的问题时，仍然存在概念性和计算成本上的挑战。过去的方法在推动智能上限和提高解决困难代理任务的效率方面存在不足。
### Innovation
我们提出了ToolOrchestra方法，用于训练小型协调器以协调智能工具。ToolOrchestra明确使用具有结果意识、效率意识和用户偏好意识的强化学习奖励。使用ToolOrchestra，我们创建了一个8B模型Orchestrator，它在较低的成本下实现了更高的准确率，在用户偏好方面表现更好。Orchestrator在HLE中的得分为37.1%，超越了GPT-5（35.1%），效率提高了2.5倍。在tau2-Bench和FRAMES上，Orchestrator的性能远超GPT-5，同时仅使用约30%的成本。详尽的分析表明，Orchestrator在多个指标下实现了性能和成本的最佳平衡，并且能够在未见过的工具上稳定扩展。
### Conclusion
这些结果表明，通过轻量级协调模型组合多种工具是一种更高效且更有效的方法，为实用和可扩展的工具增强推理系统铺平了道路。
## 169. `cs.AI` - 使用图神经网络和蒙特卡洛树搜索进行地球观测卫星调度 [PDF](https://arxiv.org/pdf/2408.15041), [HTML](https://arxiv.org/abs/2408.15041)
### Authors
Antoine Jacquet,Guillaume Infantes,Emmanuel Benazera,Vincent Baudoui,Jonathan Guerra,Stéphanie Roussel
### Background
地球观测卫星规划（EOSP）是一个具有显著实用意义的优化难题。一组请求的观测报告必须在灵活的地球观测卫星上进行安排，同时遵守其可见窗口以及不同的机动约束。此外，问题非常超出负荷，可执行的观测数量远少于候选观察的总数。因此，需要挑选一个观察集合来进行，并最大化其累积效益，同时找到一个可行的时间表。
### Innovation
先使用图神经网络（GNNs）提取代表EOSP实例的图中的相关信息，然后使用深度强化学习（DRL）来进行最优时间表的搜索。引入基于蒙特卡洛树搜索（MCTS）的后学习搜索步骤，能够找到更优解。实验表明，该方法能够在小型问题实例上学习，并且在大规模真实问题实例上表现出非常有竞争力的性能。
### Conclusion
该研究提出了一种基于图神经网络和深度强化学习的新技术来从中挑选和规划观察任务，并且引入了蒙特卡洛树搜索进一步优化。实验证明该方法在解决地球观测卫星调度问题上表现出了很好的学习能力和泛化能力，具有很强的竞争力。
## 170. `cs.AI` - 使用图扩散网络学习基于代理的模型中的个体行为 [PDF](https://arxiv.org/pdf/2505.21426), [HTML](https://arxiv.org/abs/2505.21426)
### Authors
Francesco Cozzi,Marco Pangallo,Alan Perotti,André Panisson,Corrado Monti
### Background
基于代理的模型（ABMs）是一种强大的工具，用以研究复杂系统中的涌现特性。在这些模型中，代理的行为由局部交互和随机规则驱动。然而，这些规则通常是非可微分的，限制了基于梯度的方法的使用，从而影响了与现实世界数据的集成。
### Innovation
本文提出了一种新颖的方法，通过观察ABM生成的数据来学习任意ABM的可微代理，结合扩散模型捕捉行为的随机性，并利用图神经网络建模代理间的交互。该方法的独特之处在于，它从系统层面上的输出，转而直接建模个体代理行为，保存了ABM定义的去中心化、自底向上的动态。
### Conclusion
在两个ABM（舍尔林的隔离模型和掠食者-猎物生态系统）上验证了该方法，结果显示该方法能复制个体模式并准确预测超出训练范围的涌现动态。研究结果表明，结合扩散模型和图学习有潜力用于数据驱动的ABM模拟。
## 171. `cs.AI` - 超越URL：提高LLM预训练效率的元数据多样性和位置 [PDF](https://arxiv.org/pdf/2511.21613), [HTML](https://arxiv.org/abs/2511.21613)
### Authors
Dongyang Fan,Diba Hashemi,Sai Praneeth Karimireddy,Martin Jaggi
### Background
在大型语言模型（LLMs）的预训练中引入元数据作为一种加快训练的有前途的方法已经逐渐显现出来。然而，先前的研究仅强调一个有用的信号—URL，其他形式的元数据是否能带来更大好处尚不明确。
### Innovation
本文研究了更广泛种类的元数据类型，并发现其他类型的元数据，如可以将文档质量更细化地指标在预训练中也能加快训练速度。有效元数据的共同特征是它们以更细粒度来编码信息。此外，提出了元数据附加作为一种提高训练效率的方法，预测适当元数据作为辅助任务可以帮助加快预训练过程。通过掩码损失训练可学习的元标记，可以部分恢复速度提高，诱导质量意识的潜在结构。使用探针分析潜在表示，了解元数据如何影响学习。
### Conclusion
这些结果为整合元数据以提高LLMs预训练效率和效果提供了实用指南。
## 172. `cs.AI` - 基于模型的策略适应性在闭环端到端自主驾驶中的应用 [PDF](https://arxiv.org/pdf/2511.21584), [HTML](https://arxiv.org/abs/2511.21584)
### Authors
Haohong Lin,Yunzhi Zhang,Wenhao Ding,Jiajun Wu,Ding Zhao
### Background
端到端（E2E）自主驾驶模型在开放循环评估中表现出色，但常常在闭环环境中遭受累积错误并表现出较差的泛化能力。
### Innovation
提出了一种基于模型的策略调整（MPA）框架，该框架能够提高自主驾驶代理的鲁棒性和安全性。MPA 通过生成多样化的基于几何一致性的虚拟轨迹数据，使得代理接触到原始数据集之外的场景。基于生成的数据，MPA 培训了一个基于扩散的策略调整器来细化基础策略的预测，并训练一个多步骤 Q 值模型来评估长期结果。在 nuscenes 基准测试中使用逼真的闭环模拟器的实验证明，MPA 显著提升了不同场景的表现。
### Conclusion
MPA 在不同类型的场景中显著提高了表现，进一步研究表明反事实数据的规模和推理时间的指导策略对整体效果有显著影响。
## 173. `cs.AI` - 在大规模语言模型对齐中实施多元价值观揭示了安全、包容性和模型行为的权衡 [PDF](https://arxiv.org/pdf/2511.14476), [HTML](https://arxiv.org/abs/2511.14476)
### Authors
Dalia Ali,Dora Zhao,Allison Koenecke,Orestis Papakyriakopoulos
### Background
虽然大型语言模型（LLMs）越来越多地通过人类反馈进行训练以确保安全和与人类价值观的一致性，但对齐决策往往忽略了人类的社会多样性。本研究旨在通过系统评估对齐管道中的人口统计学差异和设计参数，探索多元价值观如何影响LLM的行为。研究人员从美国和德国收集了对LLM响应的评估数据，涵盖了毒性、情感意识、敏感性、刻板偏见和帮助性五个维度。
### Innovation
本研究创新地通过使用来自不同社会群体的偏好来微调多个大型语言模型和推理模型，并研究了评分尺度、分歧处理方法和优化技术的变化对对齐数据的影响。研究发现，技术设计选择对对齐效果有显著影响，如保留评分者分歧对减少毒性的影响比多数投票高出约53%，且使用5级评分比二进制形式多约22%的毒性减少。此外，直接偏好优化（DPO）在多值优化中始终优于群体相对政策优化（GRPO）。
### Conclusion
研究结果表明，在确保安全和公平代表性的同时平衡专家和用户信号是一个关键问题，本研究为回答这一问题提供了初步的答案。
## 174. `cs.AI` - AI中算法进步的起源 [PDF](https://arxiv.org/pdf/2511.21622), [HTML](https://arxiv.org/abs/2511.21622)
### Authors
Hans Gundlach,Alex Fogelson,Jayson Lynch,Ana Trisovic,Jonathan Rosenfeld,Anmol Sandhu,Neil Thompson
### Background
研究表明，自2012年至2023年，算法已经使AI训练的FLOP效率提高了22,000倍[Ho等,2024]。通过小规模消除实验，作者能够解释这些效率提升的不到10倍。广泛的文献综述表明，未包含在消除实验中的其他创新对解释这些效率提升的贡献也低于10倍，因此总效率提升低于100倍。研究人员进行了一系列缩放实验，发现效率差距可以部分用规模依赖的效率改进算法来解释。特别地，研究人员通过LSTMs和Transformers之间的缩放实验发现，两者在计算最优缩放规律中存在指数差异，而其他许多创新在缩放过程中没有显著差异变化。
### Innovation
实验结果显示，计算规模对算法效率提升了显著影响。先前的假设是算法效率提升与计算规模无关，但该研究发现算法效率提升与其计算规模有关。由此，研究人员通过实验外推和文献估计，解释了同期效率提升的6,930倍，其中LSTM到Transformer转变为提升的主要来源。研究结果表明，小模型的算法进展比先前假设的要慢得多，并且算法效率度量具有强的参照依赖性。
### Conclusion
该研究指出，小模型的算法进步远比之前假设的要慢，并且算法效率的度量方式很大程度上取决于参照系。算法效率的提升与计算规模密切相关，这一发现挑战了传统的算法效率假设。
## 175. `cs.AI` - 重新审视不同难度级别的泛化能力：并不是那么容易 [PDF](https://arxiv.org/pdf/2511.21692), [HTML](https://arxiv.org/abs/2511.21692)
### Authors
Yeganeh Kordi,Nihal V. Nayak,Max Zuo,Ilana Nguyen,Stephen H. Bach
### Background
现有的研究关于大型语言模型（LLMs）在不同任务难度下的泛化能力存在分歧，不清楚是训练更简单的数据还是更难的数据能带来更好的结果，以及这些改进是否能在更简单的测试数据上实现。这篇文章通过系统地评估LLMs在不同模型、数据集和细粒度难度组的泛化能力，对这一问题进行了研究。
### Innovation
本文引入了一种新的评估方法，使用数千种不同LLMs的输出和项目反应理论（IRT）来对六种数据集中的例子进行排名，从而获得一个更为客观和大规模的难度评级体系，这不同于以往的人类判断。
### Conclusion
研究发现，跨难度级别的泛化能力有限，单纯依靠简单或难的数据训练LLMs无法在整个难度范围内取得一致的改进。这表明为LLMs准备训练和评估数据时需要包含各种难度级别，忽视难度的风险很大。
## 176. `cs.AI` - Matrix:  peer-to-peer 多代理合成数据生成框架 [PDF](https://arxiv.org/pdf/2511.21686), [HTML](https://arxiv.org/abs/2511.21686)
### Authors
Dong Wang,Yang Li,Ansong Ni,Ching-Feng Yeh,Youssef Emad,Xinjie Lei,Liam Robbins,Karthik Padthe,Hu Xu,Xian Li,Asli Celikyilmaz,Ramya Raghavendra,Lifei Huang,Carole-Jean Wu,Shang-Wen Li
### Background
合成数据在训练大型语言模型方面变得日益重要，尤其是在真实数据稀缺、昂贵或涉及隐私保护的情况下。许多合成任务需要协调的多代理工作流，这些专业的代理合作以生成更高质、更多样化和结构更丰富的数据。然而，现有的多代理合成框架往往依赖一个集中式的调度器，这造成了可扩展性瓶颈，或者专门针对特定领域进行硬编码，限制了灵活性。
### Innovation
我们提出了一个去中心化的框架 Matrix，它将控制流量和数据流表示为通过分布式队列传递的序列化消息。这种点对点设计消除了中央调度器。每个任务通过轻量级代理独立推进，而计算密集型操作（如 LLM 推断或容器化环境）则由分布式的服务处理。Matrix 基于 Ray，可以扩展到数万个并发的代理工作流程，提供模块化、可配置的设计，使其能够轻松适应各种数据生成工作流程。
### Conclusion
我们在不同合成场景（如多代理协作对话、基于网络的推理数据提取以及客户服务环境下工具使用轨迹生成）中评估了 Matrix。在所有情况下，Matrix 在与硬件资源相同的条件下实现了2到15倍更高的数据生成吞吐量，同时没有牺牲输出质量。
## 177. `cs.AI` - 低空空域中安全经济的无人机航路规划：具有合规意识的混合DRL-LLM方法 [PDF](https://arxiv.org/pdf/2506.08532), [HTML](https://arxiv.org/abs/2506.08532)
### Authors
Yanwei Gong,Junchao Fan,Ruichen Zhang,Dusit Niyato,Yingying Yao,Xiaolin Chang
### Background
低高度经济的快速发展推动了无人驾驶飞行器(UAVs)的广泛应用。然而，在复杂的城市环境中部署这些UAVs带来了新的挑战，特别是航路规划。现有研究在现实应用中存在的不足包括对城市 airspace的限制和经济效率的忽视，这些都是在低高度经济背景下必须考虑的因素。
### Innovation
本文提出了一种结合深度强化学习(DRL)和大型语言模型(LLM)推理的新型UAV航路规划框架，以实现安全、合规和经济上的可操作性。此外，实验结果表明，本方法在多个指标上（如数据收集率、碰撞避免、安全着陆、合规性及能源效率方面）显现出优于现有基准方法的表现。”
### Conclusion
我们的方法在解决受低高度经济网络限制下的UAV航路规划关键挑战方面证明了其有效性。
## 178. `cs.AI` - CoMind：迈向社区驱动的机器学习工程智能体 [PDF](https://arxiv.org/pdf/2506.20640), [HTML](https://arxiv.org/abs/2506.20640)
### Authors
Sijie Li,Weiwei Sun,Shanda Li,Ameet Talwalkar,Yiming Yang
### Background
大型语言模型（LLM）智能体在自动化机器学习（ML）工程中显示出一定的潜力，但现有的智能体通常独立于给定的研究问题运行，不与更广泛的科研社区互动。人类研究者常常通过分享知识获得洞察和贡献。为此，该研究引入了MLE-Live框架，旨在评估智能体与模拟的Kaggle研究社区沟通和利用集体知识的能力，并在此基础上提出了CoMind多智能体系统，该系统能够主动整合外部知识。
### Innovation
提出了一种新的多智能体系统CoMind，该系统通过迭代并行探索机制开发多个解决方案，平衡了探索多样性和实施深入性。在MLE-Live框架下的75场过往Kaggle竞赛中，CoMind实现了36%的奖牌率，建立了一个新的先进水平。此外，当在八场活的、正在进行的竞赛中部署时，CoMind平均击败了92.6%的人类竞争对手，并在三个官方排行榜中进入了前5%，在另一个排名中进入了前1%。
### Conclusion
CoMind多智能体系统通过与一个模拟的Kaggle研究社区进行互动，实现了在机器学习工程中的卓越性能。这一研究为未来社区驱动的机器学习智能体的发展奠定了基础。
## 179. `cs.AI` - Co-PatcheR：利用特定组件小型推理模型进行协作软件修复 [PDF](https://arxiv.org/pdf/2505.18955), [HTML](https://arxiv.org/abs/2505.18955)
### Authors
Yuheng Tang,Hongwei Li,Kaijie Zhu,Michael Yang,Yangruibo Ding,Wenbo Guo
### Background
受通用大型语言模型（LLMs）在软件修复方面的成功推动，最近的研究开始训练专门的修复模型。大多数研究训练单一模型处理整个修复管线（包括问题定位、补丁生成和补丁验证）。然而，小型模型难以同时处理所有任务，因为不同子任务有不同的工作流程和需要不同的专业技能。因此，使用70亿参数的最新方法，在SWE-bench-Verified上只能达到41%的修复率。
### Innovation
提出了Co-PatcheR，一种协作修复系统，结合了小型且专门针对各种组件的推理模型。主要创新在于具体任务设计和训练方法。首先，训练一个模型用于问题定位和补丁生成。接着提出了一种混合补丁验证方法，包括两个模型分别生成带、不带断言的测试用例，并判断补丁的正确性，最后通过多数投票选出补丁。实验表明，Co-PatcheR在SWE-bench-Verified上仅使用3个14B模型就达到了46%的修复率，是目前最优的专门模型修复器，所需训练资源最少，模型也最小。
### Conclusion
通过全面的消融研究，验证了我们的训练策略，以及所选的数据量、模型大小和测试阶段扩展策略的选择。Co-PatcheR展示了使用特定组件的小型推理模型进行高效的软件修复的能力。
## 180. `cs.AI` - Augur：通过大型语言模型建模时间序列中协变量的因果关联 [PDF](https://arxiv.org/pdf/2510.07858), [HTML](https://arxiv.org/abs/2510.07858)
### Authors
Zhiqing Cui,Binwu Wang,Qingxiang Liu,Yeqiang Wang,Zhengyang Zhou,Yuxuan Liang,Yang Wang
### Background
大型语言模型（LLM）在时间序列预测中展现出潜力，能够整合多模态数据。然而，现有基于LLM的方法存在一些限制，如在模型架构中的边缘角色、依赖粗略的统计文本提示以及缺乏解释性。
### Innovation
论文提出Augur，这是一种完全由LLM驱动的时间序列预测框架，利用LLM的因果推理发现并利用协变量之间的定向因果关联。Augur采用双阶段教师-学生架构，其中强大的教师LLM通过启发式搜索和成对因果测试从时间序列中推断出定向因果图。轻量级的学生代理随后完善该图，并通过将高信心因果关联编码为丰富的文本提示进行微调，以实现预测。这种设计提高了预测准确性并提供了透明、可追踪的变量交互推理。
### Conclusion
在26个基线模型和真实世界数据集上的广泛实验表明，Augur实现了竞争力的性能和鲁棒的零样本泛化。
## 181. `cs.AI` - 思维宇宙：利用大型语言模型实现创造性推理 [PDF](https://arxiv.org/pdf/2511.20471), [HTML](https://arxiv.org/abs/2511.20471)
### Authors
Yuto Suzuki,Farnoush Banaei-Kashani
### Background
基于大型语言模型（LLMs）的推理由于在数学和复杂逻辑任务中的表现突出而引起了越来越多的关注。从链式思考（CoT）提示技术开始，已经出现了许多推理方法，将问题分解为更小的、顺序性的步骤（或思维）。然而，现有的推理模型集中在常规问题解决上，并不一定通过‘创造性推理’生成创新解决方案。在药物发现或商业策略等解决方案空间广泛且常规解决方案不够理想的情况下，需要创造性推理以发现创新解决方案。
### Innovation
本文首先提出了一种受认知科学研究原则启发的计算框架，引入了三种核心的创造性推理范式：组合性、探索性和转变性推理，它们为生成创新解决方案提供了系统性的探索方向。为了利用LLMs实现这一框架，提出了‘思维宇宙’（UoT）——一种实现上述三个创造性过程的新方法集。此外，还引入了三项新的任务以及一个从可行性、实用性和新颖性三个不同角度评估创造性的评价基准，实证展示了UoT在创造性推理上的优越性能。
### Conclusion
通过与最先进的推理技术以及具有推理能力的代表性商业模型进行比较分析，结果表明UoT在创造性推理方面表现出更优秀的性能。
## 182. `cs.AI` - KRAL: 知识与推理增强学习以支持基于LLM的临床抗菌治疗 [PDF](https://arxiv.org/pdf/2511.15974), [HTML](https://arxiv.org/abs/2511.15974)
### Authors
Zhe Li,Yehan Qiu,Yujie Chen,Xiang Zhou
### Background
临床抗菌治疗需要动态整合病原体特征、宿主因素、抗菌药物的药理特性以及感染的严重程度。这种复杂性为大型语言模型（LLMs）在高风险临床决策中的应用设置了根本限制，包括知识空白、数据隐私问题、高昂的部署成本以及有限的推理能力。
### Innovation
提出了一种名为KRAL（Knowledge and Reasoning Augmented Learning）的低投入、可扩展且保护隐私的新范式。KRAL通过教师模型推理自动提炼知识和推理路径，使用启发式学习进行半监督数据扩增（减少手工标注需求约80%），并通过行动者强化学习联合提升医学知识与推理能力，优化计算和内存效率。KRAL通过多层次评估使用多种教师模型代理减少评估成本，并采用模块化接口设计简化系统更新。实验结果表明，KRAL在传统检索增强生成（RAG）和监督微调（SFT）方法上表现出显著优势。在外部开源基准MEDQA的知识问题回答能力上，KRAL的准确率为1.8%（相对于SFT）和3.6%（相对于RAG）；在外部基准PUMCH Antimicrobial的推理能力上，KRAL提升27%（相对于SFT）和27.2%（相对于RAG）。KRAL实现了约SFT长期训练成本的20%。
### Conclusion
KRAL为提高本地LLMs在临床诊断中的能力提供了一种有效方案，使低成本、高安全性部署在复杂的医学决策支持中成为可能。
## 183. `cs.AI` - PaTAS: 一种使用主观逻辑进行神经网络中信任传播的并行系统 [PDF](https://arxiv.org/pdf/2511.20586), [HTML](https://arxiv.org/abs/2511.20586)
### Authors
Koffi Ismael Ouattara,Ioannis Krontiris,Theo Dimitrakos,Dennis Eisermann,Frank Kargl
### Background
随着人工智能系统在关键安全应用中部署变得越来越重要，信任度已成为一个关键要求。传统评价指标，如准确性和精确度，无法捕捉模型预测的不确定性或可靠性，特别是在对抗或不利条件下。
### Innovation
本文提出了一种名为PaTAS的并行信任评估系统(PaTAS)，它使用主观逻辑对神经网络中的信任度建模和传播。PaTAS通过信任节点和信任函数与标准神经计算并行工作，它们在网络中传播输入、参数和激活的信任度。该框架定义了一种参数信任更新机制，用于在训练期间细化参数可靠性，并定义了推理路径信任评估(IPTA)方法来计算实例特定的信任度。
### Conclusion
实验结果表明，PaTAS产生的信任估计是可解释的、对称的并收敛的，有助于补充准确性并揭示有偏见、被污染或不确定数据场景中的可靠性差距。结果表明，PaTAS能够区分良性输入和对抗输入，并识别模型信心与实际可靠性发生偏离的情况。通过在神经网络架构中实现透明和量化的信任推理，PaTAS为评估人工智能全生命周期中的模型可靠性提供了原则性的基础。
## 184. `cs.AI` - 双平衡的多任务学习 [PDF](https://arxiv.org/pdf/2308.12029), [HTML](https://arxiv.org/abs/2308.12029)
### Authors
Baijiong Lin,Weisen Jiang,Feiyang Ye,Yu Zhang,Pengguang Chen,Ying-Cong Chen,Shu Liu,Ivor W. Tsang,James T. Kwok
### Background
多任务学习旨在同时学习多个相关任务，并已经在多个领域取得了巨大成功。然而，不同任务间的损失和梯度规模差异往往会导致性能妥协，并且任务间的平衡仍然是一个重要的挑战。
### Innovation
本文提出了双平衡多任务学习（DB-MTL），从损失和梯度两个视角实现任务平衡。DB-MTL通过在每个任务损失上执行对数变换来实现损失尺度的平衡，并通过对所有任务梯度进行归一化处理，使其尺度可比，从而调整梯度幅度。
### Conclusion
在多个基准数据集上进行的大量实验表明，DB-MTL在性能上始终优于当前最先进的方法。
## 185. `cs.AI` - 大型语言模型中的模拟自我评估：基于心理测量的AI自我效能方法 [PDF](https://arxiv.org/pdf/2511.19872), [HTML](https://arxiv.org/abs/2511.19872)
### Authors
Daniel I Jackson,Emma L Jensen,Syed-Amad Hussain,Emre Sezgin
### Background
可靠情报的关键方面之一是自我评估，但大多数对于大型语言模型（LLMs）的评估主要集中在任务准确性上。
### Innovation
研究者将一般自我效能量表（GSES）进行适应性调整，以从十个LLMs中获取模拟自我评估结果。这些评估根据不同任务条件进行，包括无任务、计算推理、社会推理和总结。结果显示，这些LLMs的自我效能评估与其实际能力并不完全匹配，表明自我评估不能可靠地反映模型的实际能力。
### Conclusion
心理测量提示可以提供有关LLMs沟通行为的结构化见解，但并不能提供准确的性能估计。
## 186. `cs.AI` - Step-Audio-R1技术报告 [PDF](https://arxiv.org/pdf/2511.15848), [HTML](https://arxiv.org/abs/2511.15848)
### Authors
Fei Tian,Xiangyu Tony Zhang,Yuxin Zhang,Haoyang Zhang,Yuxin Li,Daijiao Liu,Yayue Deng,Donghang Wu,Jun Chen,Liang Zhao,Chengyuan Yao,Hexin Liu,Eng Siong Chng,Xuerui Yang,Xiangyu Zhang,Daxin Jiang,Gang Yu
### Background
近期的推理模型在文本和视觉领域展现出了显著的成功，这得益于延长的链式推理反思机制。然而，在音频语言模型领域，存在一个令人困惑的现象：它们往往在几乎没有或不需要推理的情况下表现出色，这引发了根本性的疑问——音频智能是否可以从深思熟虑中真正受益？
### Innovation
本文引入了Step-Audio-R1，这是第一个在音频领域成功解锁推理能力的音频推理模型。通过我们提出的模态导向推理蒸馏（MGRD）框架，Step-Audio-R1能够学习生成与音频相关的推理链，这些推理链能够真正扎根于声学特征，而非创造不连贯的反思。该模型在包括语音、环境声音和音乐在内的综合音频理解和推理基准测试中表现出强大的推理能力，超过了Gemini 2.5 Pro并达到了与顶级Gemini 3 Pro相当的性能。
### Conclusion
这些结果表明，当适当扎根时，推理能力可以在不同模态间转移，将扩展的反思从一种负担转变为音频智能的强大资产。通过建立第一个成功的音频推理模型，Step-Audio-R1为构建跨所有感觉模态深度思考的真正多模态推理系统开辟了新的途径。
## 187. `cs.AI` - LLM系统中的故障模式：可靠AI应用的系统级分类 [PDF](https://arxiv.org/pdf/2511.19933), [HTML](https://arxiv.org/abs/2511.19933)
### Authors
Vaishali Vinay
### Background
大型语言模型（LLMs）正在迅速融入决策支持工具、自动化工作流和AI赋能的软件系统中。然而，在生产环境中的行为仍不被完全理解，其失败模式与传统机器学习模型存在根本差异。现有基准测试仅衡量知识或推理，而忽视了稳定性和可重复性、漂移或工作流集成等问题。
### Innovation
该论文提出了一种系统层面的大型语言模型失败模式分类，包括多步推理漂移、潜在不一致、上下文边界退化、工具调用错误、版本漂移和成本驱动性能崩溃等十五种隐蔽失败模式。同时，该论文分析了现有评价和监控方法中的差距，指出了部署大型语言模型时面临的挑战，如可观测性限制、成本约束和更新引起的性能下降，并为构建可靠、可维护和成本意识的大型语言模型系统提出了高层次设计原则。
### Conclusion
本文以系统工程问题而非单纯建模为中心，提出了评估方法学、AI系统稳健性和可信赖的大规模语言模型部署的分析基础，为未来研究奠定了基础。
## 188. `cs.AI` - 使用大型语言模型和具身知识图谱的服务机器人安全控制 [PDF](https://arxiv.org/pdf/2405.17846), [HTML](https://arxiv.org/abs/2405.17846)
### Authors
Yong Qi,Gabriel Kyebambo,Siyuan Xie,Wei Shen,Shenghui Wang,Bitao Xie,Bin He,Zhipeng Wang,Shuo Jiang
### Background
服务机器人在各个行业中的应用加强了对确保机器人安全操作机制的需求，以防止对人类或财产造成损害。尽管技术进步，包括将知识图谱与大型语言模型集成，但在自主机器人操作中的安全一致性保证方面仍存在挑战。
### Innovation
本文提出了一种将大型语言模型与具身机器人控制提示和具身知识图谱集成的新方法，以增强服务机器人的安全框架。ERCPs作为预先定义的指令，确保大型语言模型生成安全且精确的响应。ERCPs的响应通过EKGs进行验证，EKGs提供了一个全面的知识库，确保机器人的行为始终符合安全协议，从而促进在不同场景下的安全操作实践。实验结果表明，使用新框架的机器人在各类真实任务中比传统方法更严格地遵守安全标准。
### Conclusion
这种集成促进了安全的人机交互，并将我们的方法置于由人工智能驱动的安全创新的前沿。
## 189. `cs.AI` - 随机多智能体系统中的自然策略能力 [PDF](https://arxiv.org/pdf/2401.12170), [HTML](https://arxiv.org/abs/2401.12170)
### Authors
Raphaël Berthon,Joost-Pieter Katoen,Munyque Mittelmann,Aniello Murano
### Background
多智能体系统（MAS）中合成的策略可能非常复杂，需要无限内存，这与期望的行为不符合。虽然自然策略框架提供了策略和模型检查复杂性之间的平衡，但至今为止这种方式仅限于完全确定性设置。研究人员首次考虑了在随机MAS中使用PATL和PATAL*逻辑下的自然策略（分别称为NatPATL和NatPATL*）。研究结果表明，在随机MAS中，当执行联盟限于确定性策略时，NatPATL的模型检查问题为NP完全问题，而NatPATL*的问题复杂度为2NEXPTIME。在不加限制的情况下，NatPATL的复杂度为EXPSPACE，NatPATL*的复杂度为3EXPSPACE。
### Innovation
首次研究了随机多智能体系统中PATL和PATAL*的自然策略（NatPATL和NatPATL*），揭示了在特定策略限制下的模型检查复杂性。
### Conclusion
在随机MAS中，NatPATL的模型检查问题为NP完全问题，而NatPATL*的问题复杂度为2NEXPTIME。在不加限制的情况下，NatPATL的复杂度为EXPSPACE，NatPATL*的复杂度为3EXPSPACE。
## 190. `cs.AI` - Heterogeneous Multi-Agent Proximal Policy Optimization for Power Distribution System Restoration [PDF](https://arxiv.org/pdf/2511.14730), [HTML](https://arxiv.org/abs/2511.14730)
### Authors
Parya Dolatyabi,Ali Farajzadeh Bavil,Mahdi Khodayar
### Background
恢复大规模断电后电力分配系统的顺序开关操作需要重新配置馈线拓扑并协调分布式能源资源（DERs），同时满足非线性约束条件，如功率平衡、电压限制和热容量。这些挑战使得传统优化和基于价值的强化学习（RL）方法计算效率低下且难以扩展。
### Innovation
该论文采用了一个异质代理强化学习（HARL）框架，具体通过异质代理近端策略优化（HAPPO）实现，以支持互连微电网中的协调恢复。每个代理控制具有不同负载、DER容量和断路器数量的不同微电网，引入实际结构异质性。分散的行动者策略与集中式评论训练，以计算稳定在线策略更新的优势值。物理导向的OpenDSS环境提供完整的功率流反馈，并通过可微罚信号而不是无效的动作屏蔽来执行操作限制。实验表明，HAPPO在IEEE 123节点和IEEE 8500节点系统中比DQN、PPO、MAES、MAGDPG、MADQN、Mean-Field RL和QMIX更快收敛，恢复更多的电力，并且多点训练更加平滑。
### Conclusion
结果表明，在HARL框架中纳入微电网级异质性能够为复杂的PDS恢复提供可扩展、稳定且约束敏感的解决方案。
## 191. `cs.AI` - ProtoPFormer: 在视觉变换器中集中注意原型部分以实现可解释的图像识别 [PDF](https://arxiv.org/pdf/2208.10431), [HTML](https://arxiv.org/abs/2208.10431)
### Authors
Mengqi Xue,Qihan Huang,Haofei Zhang,Jingwen Hu,Jie Song,Mingli Song,Canghong Jin
### Background
ProtoPNet 因其对于可解释人工智能(XAI)的自解释性质而受到了广泛关注，并推动了许多后续研究。然而，直接将ProtoPNet应用到视觉变换器(ViT)的骨干网络上时，学到的原型会导致“分散注意”问题：它们更可能被背景激活，而较少关注前景。标准化的序列建模能力使得基于变换器的ProtoPNet难以关注原型部分，严重影响了其内在的可解释性。
### Innovation
本文提出了一种称为prototypical part transformer(ProtoPFormer)的方法，旨在适当地将原型方法与ViTs结合使用，以提高可解释的图像识别性能。该方法引入了全局和局部原型，以根据ViTs的架构特性捕获和突出目标的整体和局部特征。全局原型被用来提供对象的整体视角，以引导局部原型集中于前景，同时消除背景的影响。随后，局部原型明确地被监督以集中于各自的具体代表性的视觉部分，从而增加整体的可解释性。
### Conclusion
大量实验表明，我们提出的全局和局部原型可以相互校正，共同做出最终决定，从全局和局部角度忠实而透明地解释决策过程。此外，ProtoPFormer在与最先进的(现有最佳)基于原型的基本方法相比时，始终实现了优越的性能和可视化效果。我们的代码已在此处发布：this https URL.
## 192. `cs.AI` - FRAGMENTA：基于片段生成模型的端到端片段化策略结合自主调整以优化先导药物 [PDF](https://arxiv.org/pdf/2511.20510), [HTML](https://arxiv.org/abs/2511.20510)
### Authors
Yuto Suzuki,Paul Awolade,Daniel V. LaBarbera,Farnoush Banaei-Kashani
### Background
药物发现过程中，使用生成性AI生成分子是关键步骤，而现有的特定类别的数据集通常只包含不到100个训练示例。片段化的基于片段的方法处理少量数据比基于原子的方法更有效，但现有的启发式片段化方法限制了多样性并可能遗漏关键片段。此外，模型调整通常需要药物化学家和AI工程师之间的缓慢且间接的合作。这些局限使得药物发现和优化过程面临挑战。
### Innovation
本文介绍了FRAGMENTA，这是一种端到端的药物先导优化框架，包括：1)一种新颖的生成模型，将片段化重新定义为“词汇选择”问题，并使用动态Q学习联合优化片段化和生成；2)一种通过领域专家的对话反馈来完善目标的自主人工智能系统。此系统将AI工程师从调整过程中移除，能够逐渐学习领域知识并最终实现自动化调整。实验证明，FRAGMENTA的人工智能协助配置识别出比基线标准更多的高评分分子，并且完全自主的人工智能系统在药物发现实验中表现优于传统的人类辅助方法，展示了自主调整在捕捉专家意图方面的效果。
### Conclusion
FRAGMENTA的人工智能协助框架在识别高评分分子方面表现出色，而完全自主的人工智能系统则在仿真实验中的表现优于传统人工调整方法，这表明自主调整在药物发现和优化中的有效性。
## 193. `cs.AI` - 基于数据驱动的Lipschitz连续性：改进对抗鲁棒性的一种高效方法 [PDF](https://arxiv.org/pdf/2406.19622), [HTML](https://arxiv.org/abs/2406.19622)
### Authors
Erh-Chung Chen,Pin-Yu Chen,I-Hsin Chung,Che-Rung Lee
### Background
随着深度神经网络（DNNs）在敏感应用中的日益普及，确保其安全性和鲁棒性变得至关重要。对抗性攻击是DNNs的主要威胁之一，这种攻击通过微小的输入扰动导致错误的预测。尽管最近的对抗性训练进步通过引入外部数据集或生成模型提供了鲁棒性，但这些方法经常导致高昂的计算成本，限制了其实用性和实际部署。
### Innovation
本文提出了一种基于Lipschitz连续性的低成本替代方案，该方案在不额外使用生成数据的情况下实现了与使用大量补充数据训练的模型相当的鲁棒性。与传统的对抗性训练不同，我们的方法只需一次数据集遍历且无需梯度估计，这使其非常高效。此外，我们的方法可以无缝集成到现有的对抗性训练框架中，并增强模型的鲁棒性，而不需要额外的生成数据。实验结果表明，该方法不仅减少了计算开销，还维持甚至改善了稳健神经网络的防御能力。
### Conclusion
这项工作为开发实用的对抗性攻击有效防御措施开辟了一个有前景的方向。
## 194. `cs.AI` - CoxKAN：Kolmogorov-Arnold 网络在具有可解释性和高性能生存分析中的应用 [PDF](https://arxiv.org/pdf/2409.04290), [HTML](https://arxiv.org/abs/2409.04290)
### Authors
William Knottenbelt,William McGough,Rebecca Wray,Woody Zhidong Zhang,Jiashuai Liu,Ines Prata Machado,Zeyu Gao,Mireia Crispin-Ortuzar
### Background
生存分析是医学中用于建模关键事件如死亡或复发的时间的统计学分支，有助于优化治疗策略和患者结果。选择生存模型通常需要在性能和可解释性之间进行权衡，尽管深度学习模型具有高性能，但缺乏传统方法的透明性。这种缺乏透明性的模型在医学中常被用于关键决策，可能会让临床医生犹豫使用。
### Innovation
我们提出了CoxKAN，这是一种Cox比例风险Kolmogorov-Arnold网络，在生存分析中具有可解释性且性能高。Kolmogorov-Arnold网络最近被提出作为一种具有解释性和准确性的替代多层感知机的选择。通过在四种合成数据集和九个实际数据集上的评估（包括五组临床数据和四组基因组生物标志物），CoxKAN成功地在自动特征选择和复杂预测变量的相互作用方面表现出色，超出或匹配了传统Cox比例风险模型和基于深度学习模型的性能。
### Conclusion
在合成数据集上，CoxKAN精确地恢复了可解释性危害函数公式并优于传统方法。在实际数据集上，CoxKAN不断增加表现，提供可以解释明确的生物标志物对患者风险影响的关键洞察力。CoxKAN已经在GitHub和Zenodo上公开可用。
## 195. `cs.AI` - BoundingDocs：带有空间标注的统一文档问答数据集 [PDF](https://arxiv.org/pdf/2501.03403), [HTML](https://arxiv.org/abs/2501.03403)
### Authors
Simone Giovannini,Fabio Coppini,Andrea Gemelli,Simone Marinai
### Background
本文介绍了对文档问答（Document QA）统一数据集的研究。该数据集通过结合与文档AI和视觉丰富文档理解（VRDU）相关的多个公共数据集而生成。现有的文献中存在信息提取（IE）等文档AI任务，但本文将这些任务重新表述为问答任务，这使其成为训练和评估大型语言模型的良好资源。
### Innovation
该研究的创新点在于两个方面：一是将现有的文档AI任务重新表述为问答任务；二是发布了所有文档的OCR，并在文档图像中标注了答案的确切位置以边界框形式呈现。此外，该数据集用于探索不同提示技术（可能会包括边界框信息）对开放重量模型性能的影响，识别最有效的文档理解方法。
### Conclusion
通过使用该数据集，研究者识别出了最有效的基于不同提示技术的方法，并探究了这些技术对文档理解的性能的影响，为未来的研究提供了新的视角和方法。
## 196. `cs.AI` - 针对基于潜在扩散模型的图像编辑的灰盒攻击：后验坍缩法 [PDF](https://arxiv.org/pdf/2408.10901), [HTML](https://arxiv.org/abs/2408.10901)
### Authors
Zhongliang Guo,Chun Tong Lei,Lei Fang,Shuai Zhao,Yifei Qian,Jingyu Lin,Zeyu Wang,Cunjian Chen,Ognjen Arandjelović,Chun Pong Lau
### Background
最近在潜在扩散模型（LDMs）方面的进展极大地变革了图像的合成和处理，但与此同时也引发了对数据误用和知识产权侵权的严重担忧。现有的对抗性攻击作为对抗这种生成AI滥用的防护措施虽被广泛研究，但它们严重依赖于模型特定的知识，并且计算成本高昂。
### Innovation
本文受到VAE训练中后验坍缩现象的启发，提出了一种新颖的后验坍缩攻击（PCA）框架。通过全面的理论分析和实证验证，发现VAE推理过程中的两种不同的坍缩现象：扩散坍缩和聚集坍缩，并据此设计了一个统一的损失函数，该函数通过参数调整可以灵活地实现这两种坍缩，对应不同的图像保护目标。PCA方法极大地减少了依赖模型特定知识，仅需访问VAE编码器即可，这包含了LDM参数总量的不到4%。此外，PCA在VAE编码器操作之前不依赖于空白提示的优化，从而实现了没有延迟保护效应。
### Conclusion
广泛的实验表明，PCA在保护效果、计算效率（运行时间和VRAM）以及针对基于VAE的LDM变体的一般性方面均优于现有技术。本文提供的代码可以在以下链接中获得。
## 197. `cs.AI` - 无配对标签数据：无人机视角地理定位的端到端自监督学习 [PDF](https://arxiv.org/pdf/2502.11381), [HTML](https://arxiv.org/abs/2502.11381)
### Authors
Zhongwei Chen,Zhao-Xu Yang,Hai-Jun Rong,Guoqi Li
### Background
无人机视角地理定位（DVGL）旨在通过检索包含GPS标记的卫星图像来实现无人机的准确定位。然而，现有的大多数方法严重依赖预先匹配的无人机-卫星图像对进行监督学习。当目标区域发生变化时，通常需要新的配对样本来适应分布变化。这种高成本的注解和这些方法有限的可迁移性严重阻碍了DVGL在开放场景中的实际部署。
### Innovation
本文提出了一种名为动态记忆驱动和邻域信息学习（DMNIL）的端到端自监督学习方法，它具有浅层骨干网络。该方法采用聚类算法生成伪标签，并采用双路径对比学习框架学习具有区别的视图内部表示。DMNIL包含两个核心模块，包括动态层次记忆学习（DHML）模块和信息一致性演化学习（ICEL）模块。DHML模块结合短期和长期记忆以增强视图内部特征的一致性和可分辨性。同时，ICEL模块利用邻域驱动的动力学约束机制系统地捕捉跨视图的潜在语义相关性，从而改善跨视图特征对齐。为了进一步稳定并加强自监督训练过程，引入了伪标签增强策略以增强伪监督的质量。
### Conclusion
在三个公开基准数据集上的大量实验表明，所提出的方法在多个现有自监督方法中表现优异，并且甚至超过了某些最先进的监督方法。我们在GitHub上的代码链接为：this https URL.
## 198. `cs.AI` - 推荐之外的商品目录以外的个性化图像生成 [PDF](https://arxiv.org/pdf/2502.18477), [HTML](https://arxiv.org/abs/2502.18477)
### Authors
Gabriel Patron,Zhiwei Xu,Ishan Kapnadak,Felipe Maia Polo
### Background
个性化在人机交互中至关重要，但当前的扩散基图像生成系统对用户多样性反应不足。现有解决方案往往依赖于昂贵的配对偏好数据或通过大型语言模型引入延迟。
### Innovation
REBECA框架通过直接从隐式反馈信号（如点赞、评价和点击）中学习，提供了一种轻量级且可扩展的个性化图像生成方法，而不是对底层扩散模型进行微调。通过两阶段过程，使用预训练的扩散主体解码，从而实现高效且无需微调的个性化。
### Conclusion
用REBECA方法在现实世界数据集上进行了严格的评价，结果表明，REBECA能生成高保真度、个性化图像，超越基准模型，同时保持计算效率。
## 199. `cs.AI` - 通过融合全局和局部统计信息进行数据估值 [PDF](https://arxiv.org/pdf/2405.17464), [HTML](https://arxiv.org/abs/2405.17464)
### Authors
Xiaoling Zhou,Ou Wu,Michael K. Ng,Hao Jiang
### Background
近年来，高质量数据在各种应用场景中的重要性愈发凸显，因此数据估值得到了越来越多的关注。虽然基于Shapley值的方法因其坚实的理论基础而普遍被采用，但其实现往往非常耗费计算资源，导致需要寻找多种近似技术。然而，现有的方法普遍忽视了估值分布信息的融合，未能考虑数据的动态变化，这限制了它们的应用效果和潜力。
### Innovation
本文强调了在机器学习的数据估值中融合全局和局部估值分布统计信息的重要性。首先，通过在各种模拟和实际数据集上对这些分布进行全面分析，发现了有价值的观点和关键模式。其次，提出了新的数据估值方法，将探索到的分布特征融入到两个正则项中，以改进Shapley值估计。第三，引入了一种新的动态数据估值方法，无需重新计算Shapley值即可推测更新的数据值，从而显著提高了计算效率。实验证明了所提出方法的高效性和有效性，验证了全局和局部估值分布在数据估值中的巨大潜力。
### Conclusion
广泛的实验表明，我们的方法在数据估值任务中表现一致且高效，证明了全局和局部估值分布对数据估值的重要性，同时也提高了数据估值实践中的应用潜力。
## 200. `cs.AI` - 弥合收敛学习的关键缺口：表示对齐如何在整个训练层、分布变迁中演变 [PDF](https://arxiv.org/pdf/2502.18710), [HTML](https://arxiv.org/abs/2502.18710)
### Authors
Chaitanya Kapoor,Sudhanshu Srivastava,Meenakshi Khosla
### Background
独立训练的神经系统的内部表示是否会变得相似，对于神经科学和AI来说至关重要。然而，现有文献在范围上仍然有限，通常只考察少量模型和单一数据集，依赖单一的对齐度量，并在单个训练后检查点评估网络性能。
### Innovation
本文进行了大规模的收敛学习审计，涵盖了多个视觉模型和成千上万的层对比较，填补了之前的这些知识缺口。同时，通过将三种对齐家族（线性回归、正交普罗斯库罗斯和置换/柔软匹配）进行对比，发现了正交变换在对准表示方面几乎与更灵活的线性变换一样有效，尽管置换得分较低，但远超随机，揭示了一种优先的表示基础。此外，追踪整个训练过程中的收敛情况表明，几乎所有最终的对齐都几乎在第一个 epoch 内形成，这表明它主要是由共享输入统计数据和架构偏向驱动的，而不是最终任务解决方案。最后，当模型面临一系列新的离群图像时，底层保持紧密对齐，而更深层次的逐渐偏离比例与分布变化成正比。
### Conclusion
这些发现填补了我们对表示收敛理解的关键缺口，对于神经科学和AI领域有着重要影响。
## 201. `cs.AI` - CroMe:利用跨模态三变换器和度量学习进行多模态假新闻检测 [PDF](https://arxiv.org/pdf/2501.12422), [HTML](https://arxiv.org/abs/2501.12422)
### Authors
Eunjee Choi,Junhyun Ahn,XinYu Piao,Jong-Kook Kim
### Background
多模态假新闻检测近年来受到了越来越多的关注。现有的方法依赖于独立编码的单一模态数据，并且忽略了利用高级技术捕捉内模态关系和整合跨模态相似性的优势。
### Innovation
提出了跨模态三变换器和度量学习方法（CroMe），该方法利用 Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models (BLIP2) 作为编码器，以捕获详细的文本、图像和图像-文本表示。度量学习模块采用代理锚点方法来捕获内模态关系，特征融合模块则使用跨模态三变换器进行有效整合。最后，通过分类器处理融合特征以预测内容的真实性。
### Conclusion
在数据集上的实验显示，CroMe 在多模态假新闻检测中表现出色。
## 202. `cs.AI` - 适应性室内导航辅助中实时算法的物体检测性能评估 [PDF](https://arxiv.org/pdf/2501.18444), [HTML](https://arxiv.org/abs/2501.18444)
### Authors
Abhinav Pratap,Sushant Kumar,Suchinton Chakravarty
### Background
本文探讨了为视障人士提供支持技术时，需要准确且高效的物体检测的需求。研究者在室内导航辅助的情境下，通过室内物体检测数据集评估了YOLO、SSD、Faster R-CNN和Mask R-CNN四种实时物体检测算法，并分析了这些算法在检测准确性、处理速度及适应室内环境方面的表现。
### Innovation
研究通过分析这四种实时物体检测算法在检测准确性、处理速度及适应室内环境方面的表现，突出了精度与效率之间的权衡，为选择适合实时辅助导航的最佳算法提供了见解，促进了适应性机器学习在提升视障人士的室内导航解决方案方面的作用及无障碍环境建设。
### Conclusion
本研究促进了适应性机器学习在实际中的应用，为视障人士提供了更好的室内导航解决方案，有助于提高无障碍环境的建设。
## 203. `cs.AI` - 作为数据点的默尔索 [PDF](https://arxiv.org/pdf/2502.01364), [HTML](https://arxiv.org/abs/2502.01364)
### Authors
Abhinav Pratap
### Background
在数据化时代，人类体验被量化为可测量的指标，这引发了深刻的哲学和伦理问题。本文以阿尔贝·加缪的《局外人》中的主人公默尔索为视角，探讨他情感上的疏离反映了存在主义的荒诞观念。利用自然语言处理（NLP）技术，包括情感识别（BERT）、情感分析（VADER）和命名实体识别（spaCy），本文量化了默尔索生命中的关键事件和行为。
### Innovation
研究表明，算法模型在处理复杂人类体验时存在局限性，尤其是那些根植于存在主义隔阂和道德模糊的经验。通过分析现代AI工具如何误解默尔索的行为和情感，本文揭示了将细腻的人类叙事简化为数据点所带来的更广泛的伦理困境，并挑战了数据驱动社会的核心假设。
### Conclusion
本文的研究结果批评了对数据驱动叙事的日益依赖，并呼吁在人工智能中纳入人道主义价值观。
## 204. `cs.AI` - 大型语言模型中的最佳选项(N)采样意识型微调 [PDF](https://arxiv.org/pdf/2412.15287), [HTML](https://arxiv.org/abs/2412.15287)
### Authors
Yinlam Chow,Guy Tennenholtz,Izzeddin Gur,Vincent Zhuang,Bo Dai,Sridhar Thiagarajan,Craig Boutilier,Rishabh Agarwal,Aviral Kumar,Aleksandra Faust
### Background
最近的研究表明，在利用推理时的计算方面有效操作是实现大型语言模型（LLMs）更好性能的关键。这项工作探讨了一种直接优化推理时策略性能的新型推理意识型微调方法。
### Innovation
提出了首个针对最佳选项(N)采样意识型微调的仿真实例学习和强化学习方法，克服了非可微分的argmax操作符。研究表明，我们的最佳选项(N)采样意识型微调模型能够在推理时计算和性能方面都表现出色，尤其是在Gemma 2B上，Hendrycks MATH的Bo32性能从26.8%提升到30.8%，pass@32从60.0%提升到67.0%，以及HumanEval的pass@16从61.6%提升到67.1%。
### Conclusion
我们的实验表明，最佳选项(N)采样意识型微调在推理时性能和计算方面都取得了显著提升。
## 205. `cs.AI` - SOAP: 提升少样本动作识别中的时空关系和运动信息捕捉 [PDF](https://arxiv.org/pdf/2407.16344), [HTML](https://arxiv.org/abs/2407.16344)
### Authors
Wenbo Huang,Jinghui Zhang,Xuwei Qian,Zhen Wu,Meng Wang,Lei Zhang
### Background
高帧率(HFR)视频的动作识别虽然能提供细粒度表达，但会削弱时空关系和运动信息密度，因此传统的数据驱动训练需要大量视频样本。然而，在现实场景中样本往往不足，推动了少样本动作识别(FSAR)的研究。最近的FSAR工作主要在提取空间特征后通过时间对齐来构建时空关系，但忽视了密度，并仅捕捉相邻帧之间狭隘的运动信息，导致运动信息捕捉不充分。
### Innovation
本文提出了一种新型的插件式架构SOAP用于FSAR，SOAP-Net模型不仅考虑不同特征通道之间的时序连接和特征的时空关系，还通过包含更多信息的帧元组捕捉综合性运动信息。此外，结合不同帧数的帧元组进一步提供更宽广的视角，这种架构有效提升了FSAR中的时空关系和运动信息的捕捉能力。
### Conclusion
SOAP-Net在SthSthV2、Kinetics、UCF101和HMDB51等多个知名基准测试中实现了新的最先进性能。详尽的经验评价进一步证明了SOAP的竞争力、插件式、泛化能力和鲁棒性。相关代码已发布。
## 206. `cs.AI` - Multi-PA: 大型视觉-语言模型隐私评估多视角基准 [PDF](https://arxiv.org/pdf/2412.19496), [HTML](https://arxiv.org/abs/2412.19496)
### Authors
Jie Zhang,Xiangkui Cao,Zhouyu Han,Shiguang Shan,Xilin Chen
### Background
大型视觉-语言模型（LVLMs）在多种任务中展现出显著潜力，但同时也面临重大隐私风险，限制了它们的实际应用。当前对LVLMs隐私评估的研究在范围上是有限的，缺乏全面的评估维度和隐私类别。现有的研究在隐私评估维度和隐私类别上存在空白。
### Innovation
提出了Multi-PA，这是一个全面的基准，用于评估LVLMs在隐私意识和隐私泄露方面的隐私保留能力。Multi-PA涵盖了26类个人隐私、15类商业秘密和18类国家机密，总计31,962个样本。基于此基准，该研究评估了21个开源和2个闭源的LVLMs的隐私保护能力。研究结果表明，当前的LVLMs普遍存在较高的隐私泄露风险，不同类别的隐私威胁程度有所不同。
### Conclusion
当前的LVLMs普遍具有较高的隐私泄露风险，特别是在个人隐私、商业秘密和国家机密方面存在不同的脆弱性。Multi-PA作为一个全面的隐私评估基准，为提升LVLMs的隐私保护提供了重要参考。
## 207. `cs.AI` - OuroMamba: 一种针对视觉Mamba模型的数据无关量化框架 [PDF](https://arxiv.org/pdf/2503.10959), [HTML](https://arxiv.org/abs/2503.10959)
### Authors
Akshat Ramachandran,Mingyu Lee,Huan Xu,Souvik Kundu,Tushar Krishna
### Background
对于基于视觉Mamba模型（Visual Mamba Models, VMMs）的后训练量化，现有技术通常依赖于合成数据，而这受到模型中的递归状态转变得出的长期交互限制以及跨时间步幅的动态异常值变异的挑战。这些限制使得现有的量化技术效率低下，难以实现高性能的量化结果。
### Innovation
本文提出了OuroMamba，一种针对VMMs的数据无关后训练量化方法（DFQ）。OuroMamba通过两个阶段的方法解决了上述挑战：首先是OuroMamba-Gen，利用对比学习生成丰富的、具有语义意义的合成数据，其次是OuroMamba-Quant，采用混合精度量化和轻量级动态异常值检测。此外，量化激活时的一种阈值基异常通道选择策略能够实时更新，从而进一步增强量化效果。
### Conclusion
在视觉任务和生成任务的广泛实验表明，OuroMamba在没有使用合成数据的情况下，达到了最先进的量化性能，并在不同的量化设置下展现了卓越的表现。此外，我们还实现了高效的GPU内核，实现了高达2.36倍的实用延迟加速。
## 208. `cs.AI` - 力提示：视频生成模型可以学习和泛化基于物理的控制信号 [PDF](https://arxiv.org/pdf/2505.19386), [HTML](https://arxiv.org/abs/2505.19386)
### Authors
Nate Gillman,Charles Herrmann,Michael Freeman,Daksh Aggarwal,Evan Luo,Deqing Sun,Chen Sun
### Background
最近视频生成模型的进步激发了对能够模拟现实环境的世界模型的兴趣。导航方面已经有足够的研究，但是模拟物理现实中的力导向的真实世界交互仍然缺乏研究。
### Innovation
本文提出了一种力提示方法，能够通过局部点力（如戳植物）和全局风力场（如布料随风飘动）来控制视频生成，无需在推断时使用任何3D资产或物理仿真。研究发现，即使只有少量示范，仅凭Blender合成的视频也能很好地适应物理力条件，生成模拟多样化几何、环境和材料中力作用的视频。
### Conclusion
本文的方法以四张A100 GPU仅一天的训练数据为例，表现出色，在力行为贴合度和物理现实感方面超越了现有方法，对实际物理交互带来了更近一步的可能。所有数据集、代码、权重和互动视频演示均在项目页面发布。
## 209. `cs.AI` - 公司在管理人工智能的环境可持续性方面是如何操作的？一项关于绿色人工智能努力和法规的访谈研究 [PDF](https://arxiv.org/pdf/2505.07317), [HTML](https://arxiv.org/abs/2505.07317)
### Authors
Ashmita Sampatsing,Sophie Vos,Emma Beauxis-Aussalet,Justus Bogner
### Background
随着人工智能（AI）的广泛应用，基于AI的软件及其对环境的负面影响变得不可忽视，研究和减轻这些影响已成为关键研究领域。然而，目前尚不清楚环境可持续性在工业中AI采用过程中的作用以及AI法规如何影响绿色人工智能实践和决策。因此，本研究旨在探讨行业中从业者对绿色人工智能的认知和管理。
### Innovation
本研究通过与10家不同组织的11名参与者进行访谈，探索了AI采用、减轻AI环境影响的当前努力以及欧盟AI法案和公司可持续性报告指令（CSRD）的影响。研究发现表明，在AI采用过程中，9名参与者优先考虑商业效率，而环境可持续性很少被考虑。关于实际采取的缓解措施，六名参与者未采取行动，其他人偶尔提到了如提示工程、使用较小模型或不过度使用AI等技术。对于欧盟AI法案的遵守情况较低，仅有一名参与者提到了该法规的影响，而CSRD主要在大公司推动了可持续性报告活动。
### Conclusion
这些公司的发现反映了在可持续人工智能方面缺乏紧迫性和优先级。我们建议现有法规的有效性有限，这对政策制定者有重要影响。此外，需要提高行业意识，同时也需要提供用户友好的技术和工具以促进绿色人工智能实践。
## 210. `cs.AI` - IVY-FAKE: 一种用于图像和视频AIGC检测的一体化可解释框架和基准 [PDF](https://arxiv.org/pdf/2506.00979), [HTML](https://arxiv.org/abs/2506.00979)
### Authors
Changjiang Jiang,Wenhui Dong,Zhonghao Zhang,Chenyang Si,Fengchang Yu,Wei Peng,Xinbin Yuan,Yifei Bi,Ming Zhao,Zian Zhou,Caifeng Shan
### Background
随着人工智能生成内容(AIGC)技术的快速发展，尽管生成了高质量的合成内容，但也引发了重要的安全问题。当前的检测方法面临两个主要限制：一是缺乏多维可解释的数据集，现有开源数据集（例如，WildFake、GenVideo）依赖于简化二元注释，限制了训练检测器的解释性和可信度。二是基于MLLM的伪造检测器（例如，FakeVLM）在逐步推理中的解释不够精细，阻碍了可靠的定位和解释。
### Innovation
我们提出了Ivy-Fake，这是第一个用于解释性AIGC检测的大型多模态基准。它包含超过106,000个富含注解的培训样本（图片和视频）和5,000个人工验证的评估示例，从多个生成模型和现实世界数据集通过精心设计的流程获取，确保多样性和质量。此外，我们还提出了一种基于组相对策略优化（GRPO）的强化学习模型Ivy-xDetector，能够产生可解释的推理链，并且在多个合成内容检测基准测试中表现出高度鲁棒性。
### Conclusion
大量的实验展示了我们数据集的优势，并证实了我们方法的有效性。我们的方法在GenImage上的性能从86.88%提高到96.32%，明显超过了先前最先进的方法。
## 211. `cs.AI` - 超越反省：通过外部行为反馈强化思考 [PDF](https://arxiv.org/pdf/2501.01457), [HTML](https://arxiv.org/abs/2501.01457)
### Authors
Diji Yang,Linda Zeng,Kezhen Chen,Yi Zhang
### Background
巨大的语言模型在推理时能够解决复杂问题，但由于其概率性质，延长的思考过程可能会变得不可靠或不一致，特别是在知识边界附近。现有的方法试图通过让模型反省自己的推理并进行修正来缓解这一问题。然而，这种自我反省仍然会继承原有输出中的偏见，称为反思错觉。本研究在超越反思的基础上，借鉴动物学中的核心方法论，提出了一种外部主义三步框架——蒸馏-强化-推理（DRR）。该框架不依赖于模型的自我反省，而是通过评估其可观察的行为来提供纠正性反馈。
### Innovation
提出了一种外部主义三步框架——蒸馏-强化-推理（DRR），该框架通过评估模型的行为轨迹来提供纠正性反馈，而不是依赖模型的自我反省。该框架首先通过蒸馏提取推理器的行为痕迹，然后训练一个轻量级的外部辨别模型（DM）。在推理时，DM作为批评者，识别并拒绝可疑的推理步骤，从而外部反馈促使LLM摒弃有缺陷的路径并探索替代方案，提升推理质量。实验表明，该框架显著优于现有的自我反省方法。该框架由于其轻量级和无需标注的设计，提供了一种可扩展且适应性强的解决方案，可以广泛应用于各种LLM，以改善推理的可靠性。
### Conclusion
该研究提出了一种名为DRR的外部主义框架，能够在不改变基础模型的前提下，通过外部反馈提高LLM推理的质量。实验结果显示，DRR方法在多个推理基准测试中显著优于现有的自我反省方法，显示出作为广泛应用于各种LLM的可靠推理解决方案的潜力。
## 212. `cs.AI` - 物理约束流匹配：具有硬约束的生成模型采样 [PDF](https://arxiv.org/pdf/2506.04171), [HTML](https://arxiv.org/abs/2506.04171)
### Authors
Utkarsh Utkarsh,Pengfei Cai,Alan Edelman,Rafael Gomez-Bombarelli,Christopher Vincent Rackauckas
### Background
近年来，深度生成模型被应用于受偏微分方程（PDEs）支配的物理系统中，提供了可扩展的模拟和具有不确定性意识的推断。然而，对物理约束的强约束执行仍然是一个挑战。现有的方法往往依赖于软惩罚或架构偏置，这些方法无法保证严格的约束条件。
### Innovation
提出了一种零样本推理框架——物理约束流匹配（PCFM），能够在预训练的基于流的生成模型中强制执行任意的非线性约束。PCFM通过在中间解的状态上不断应用基于物理的校正来引导采样过程，同时与所学的流保持一致并满足物理约束。
### Conclusion
实验结果表明，PCFM在一系列PDEs上优于未受约束和受约束的基线，包括具有激波、不连续性和尖锐特征的方程，同时确保最终解中的精确约束满足。我们的方法提供了一个灵活的框架，用于在科学和通用生成模型中强制执行硬约束，特别是在约束满足至关重要的应用中。
## 213. `cs.AI` - TS-RAG：基于检索增强生成的时间序列基础模型是更强的零样本预测器 [PDF](https://arxiv.org/pdf/2503.07649), [HTML](https://arxiv.org/abs/2503.07649)
### Authors
Kanghui Ning,Zijie Pan,Yu Liu,Yushan Jiang,James Yiming Zhang,Kashif Rasul,Anderson Schneider,Lintao Ma,Yuriy Nevmyvaka,Dongjin Song
### Background
大型语言模型（LLMs）和基础模型（FMs）近年来已被广泛应用于时间序列预测任务。虽然对LLMs进行微调能够实现领域适应，但它们常常难以在不同且未见过的数据集上泛化。此外，现有的时间序列基础模型（TSFMs）在处理非平稳动态和分布转移时仍然面临挑战，这主要是由于缺乏有效的适应机制。本文背景即是基于上述问题，提出了一种新的时间序列预测框架。
### Innovation
提出了一种检索增强生成框架TS-RAG，该框架利用预训练的时间序列编码器从专门的知识库中检索与输入查询语义相关的片段，丰富了输入查询的上下文表示。此外，TS-RAG还提出了一种动态检索混合器（ARM）模块，该模块能够将检索到的模式与TSFM的内部表示动态融合，从而改善预测准确性，而不需要针对特定任务进行微调。实验结果表明，TS-RAG在七个公开基准数据集上实现了最先进的零样本预测性能。
### Conclusion
TS-RAG通过增强时间和可解释性取得了显著的零样本预测性能，相较于现有的时间序列基础模型，其在多个领域上性能提升高达6.84%，同时此工作提供的代码和数据可以在指定链接找到。
## 214. `cs.AI` - 流匹配遇到PDEs：一种物理约束生成的统一框架 [PDF](https://arxiv.org/pdf/2506.08604), [HTML](https://arxiv.org/abs/2506.08604)
### Authors
Giacomo Baldan,Qiang Liu,Alberto Guardone,Nils Thuerey
### Background
生成式机器学习方法，如扩散模型和流匹配，展示了在建模复杂系统行为和构建高效代理模型方面的巨大潜力。然而，这些方法通常从数据中隐式学习底层的物理规律。本文分析了这一背景。
### Innovation
提出了基于物理的流匹配（PBFM），这是一种新颖的生成框架，通过在流匹配目标中显式嵌入物理约束（包括PDE残差和代数关系）从而改善了最终噪声消除样本预测的准确性。此外，该方法通过交替最小化流匹配损失和基于物理的残差损失无需调参，从而提供了一个有效框架，以及引入了时间展开以提高预测精度。
### Conclusion
PBFM方法在三个代表性PDE问题的基准测试中展示了显著的优越性，物理残差降低了8倍，且在分布准确性方面也超越了现有算法。因此，PBFM为物理和工程应用中的代理 modeling、不确定性量化和加速模拟提供了一个兼具原理性和效率的框架。
## 215. `cs.AI` - MigGPT: 利用大语言模型实现出/树Linux内核补丁跨版本自动化迁移 [PDF](https://arxiv.org/pdf/2504.09474), [HTML](https://arxiv.org/abs/2504.09474)
### Authors
Pucheng Dang,Di Huang,Dong Li,Kang Chen,Yuanbo Wen,Qi Guo,Xing Hu
### Background
出/树内核补丁对于适应新硬件或实现特定功能至关重要。然而，不同内核版本之间维护和更新这些补丁需要大量经验丰富的工程师的工作。尽管大型语言模型在多个领域取得了显著进展，表明其在自动化出/树内核补丁迁移方面的潜力，但研究表明这些模型在代码上下文理解和迁移点识别方面存在不足。
### Innovation
本文提出MigGPT框架，利用新颖的代码指纹结构保留代码片段信息，并结合三种精心设计的模块以提高出/树内核补丁迁移的准确性和效率。此外，还构建了一个基于实际项目的稳健基准来评估LLM的能力，并证明与直接应用经典的LLM相比，MigGPT能够显著提高任务完成率，平均完成率为74.07%。
### Conclusion
结果显示，MigGPT在迁移任务中显著优于直接应用传统的大语言模型。
## 216. `cs.AI` - LCB-CV-UNet: 提高高动态范围雷达信号检测器 [PDF](https://arxiv.org/pdf/2505.23454), [HTML](https://arxiv.org/abs/2505.23454)
### Authors
Yanbin Wang,Xingyu Chen,Yumiao Wang,Xiang Wang,Chuanfei Zang,Guolong Cui,Jiahuan Liu
### Background
该研究针对高动态范围（HDR）雷达信号引起的性能下降问题，提出了LCB-CV-UNet模型。背景强调了HDR雷达信号处理的挑战，包括相位相干性保持问题。现有的方法无法有效应对HDR特征的处理难题。
### Innovation
提出了一种名为Logarithmic Connect Block (LCB)的新硬件高效模块，作为相位相干性保持的解决方案。LCB模块能够有效处理HDR特征。此外，研究还提出了双混合数据集构建方法，生成了一个半合成数据集，能够模拟典型HDR信号场景，并且该方法具有可调的目标分布。
### Conclusion
实验结果表明，与基线相比，该模型在总共增加了不到0.9%的计算复杂度的情况下提升了1%的总体检测概率，并且在典型城市目标信号信噪比范围（11-13 dB）中比基线方法高出5%。实际实验验证了该模型的实用性。
## 217. `cs.AI` - AI领域的严密性：需要更加广泛且负责任的AI概念 [PDF](https://arxiv.org/pdf/2506.14652), [HTML](https://arxiv.org/abs/2506.14652)
### Authors
Alexandra Olteanu,Su Lin Blodgett,Agathe Balayn,Angelina Wang,Fernando Diaz,Flavio du Pin Calmon,Margaret Mitchell,Michael Ekstrand,Reuben Binns,Solon Barocas
### Background
在AI研究和实践中，严密性主要被理解为方法论上的严密性，比如数学、统计或计算方法是否正确应用。为此类严密性狭窄的理解，相关AI社区提出了包括夸大的AI系统能力表述在内的担忧。作者认为，需要一个更为广泛的概念来定义严格AI研究和实践的要求。
### Innovation
作者提出，严格的AI研究和实践应包括：(1) 方法论上的严密性，(2) 知识论上的严密性（基于何种背景知识决定研究方向），(3) 规范论上的严密性（学科、社区或个人规范、标准或信念如何影响工作），(4) 概念论上的严密性（使用理论构架的清晰度），(5) 报告论上的严密性（所报告的内容及其方式），(6) 诠释论上的严密性（现有的证据推理的正当性支持程度）。
### Conclusion
作者提供了一个有价值的语言和框架，以便促进有关AI工作的必要对话，涵盖研究人员、政策制定者、记者和其他利益相关者。
## 218. `cs.AI` - 多代理多臂老虎机中的探查公平算法 [PDF](https://arxiv.org/pdf/2506.14988), [HTML](https://arxiv.org/abs/2506.14988)
### Authors
Tianyi Xu,Jiaxin Liu,Nicholas Mattei,Zizhan Zheng
### Background
在多代理多臂老虎机（MA-MAB）环境中，如何在确保各方获得公平结果的同时最大化整体系统性能是一个挑战。特别是在信息有限的情况下，如何做出有效的决策变得尤为复杂。
### Innovation
提出了一个新颖的探查框架，在选择臂之前有策略地收集信息，以提高决策效率。在离线设置中利用亚模性设计了一个贪心探查算法，并证明了其性能界限。在线设置时，开发了一个既能保持公平又能减少次线性后悔的算法。
### Conclusion
通过对合成和真实数据集的大量实验，表明该方法优于基准方法，实现了更好的公平性和效率。
## 219. `cs.AI` - AutoDiscovery：通过贝叶斯惊讶实现开放性科学发现 [PDF](https://arxiv.org/pdf/2507.00310), [HTML](https://arxiv.org/abs/2507.00310)
### Authors
Dhruv Agarwal,Bodhisattwa Prasad Majumder,Reece Adamson,Megha Chakravorty,Satvika Reddy Gavireddy,Aditya Parashar,Harshit Surana,Bhavana Dalvi Mishra,Andrew McCallum,Ashish Sabharwal,Peter Clark
### Background
自主科学发现（ASD）不仅需要回答问题，还必须确定要问哪些问题。大多数现有的ASD工作依赖于人类指定的研究问题来指导假设生成。然而，通过允许AI系统根据其自身标准驱动探索，科学发现可能会得到进一步加速。现有的开放性ASD方法基于多样性和人类兴趣的主观代理来选择假设，但这种方法要么难以导航假设空间，要么定义不精确。
### Innovation
本文提出了一种名为AutoDiscovery的方法，该方法通过贝叶斯惊讶驱动开放性ASD，通过计算LLM在获取实验结果前后的知识转变来量化假设的探索。为了高效探索嵌套假设的空间，该方法使用蒙特卡洛树搜索（MCTS）策略，并利用意外程度作为奖励函数，采用逐渐扩展的方法。AutoDiscovery在21个真实数据集上的表现优于现有对手，特别是在固定预算下，生成了5-29%更多的惊人发现。进一步的人类评估结果显示，三分之二的发现对领域专家来说也是惊人的，这表明这种方法是构建开放性ASD系统的重要一步。
### Conclusion
本文展示了AutoDiscovery使用Bayesian Surprise进行开放性科学探索的有效性，并且通过实验证明了该方法在生成显著发现方面的优越性。AutoDiscovery能够在开放性ASD领域取得更好表现，特别是在有限资源下，且产生的发现多数具有很高的新颖性和科学价值。
## 220. `cs.AI` - UITron-Speech: 基于语音指令的自动化GUI代理 [PDF](https://arxiv.org/pdf/2506.11127), [HTML](https://arxiv.org/abs/2506.11127)
### Authors
Wenkang Han,Zhixiong Zeng,Jing Huang,Shu Jiang,Liming Zheng,Longrong Yang,Haibo Qiu,Chang Yao,Jingyuan Chen,Lin Ma
### Background
自主代理（agent）在图形用户界面（GUI）中的应用正在改变人机交互的方式，但由于依赖于文本指令，这限制了无障碍性和便利性，特别是在无动手操作情况下。为了克服这个问题，本文提出了用语音替代文本作为GUI代理的指令输入模态，并介绍了UITron-Speech，这是第一个能够直接处理语音指令和设备截图来预测用户操作的端到端的GUI代理。
### Innovation
1. 使用一种随机发言者文本转语音模型合成了高质量的语音指令数据集，以解决数据稀缺问题。2. 设计了一种混合模态训练策略，以减轻预训练基础模型中的模态失衡问题。3. 对GUI基础定位预测误差进行了统计分析，并提出了一种无需训练的两步定位校正方法，以减轻细微的位置偏差。
### Conclusion
大量的实验证明，UITron-Speech实现了稳健的性能和卓越的适应性，这表明基于语音驱动的GUI代理在更具包容性和智能的人机交互方面具有可行性和潜力。我们的代码和数据集可以在此找到。
## 221. `cs.AI` - WeatherDiffusion: 用于本征空间可控天气编辑的框架 [PDF](https://arxiv.org/pdf/2508.06982), [HTML](https://arxiv.org/abs/2508.06982)
### Authors
Yixin Zhu,Zuoliang Zhu,Jian Yang,Miloš Hašan,Jin Xie,Beibei Wang
### Background
介绍了WeatherDiffusion，这是一种基于扩散先验的框架，用于内在空间中的可控天气编辑。该框架使用双组件：一个逆渲染器，用于从输入图像估计材料属性、场景几何形状和照明作为内在映射；一个前向渲染器，利用这些几何模型和材料映射以及描述特定天气条件的文本提示生成最终图像。这些内在映射增强了与传统像素空间编辑的可控性。
### Innovation
提出了一种内在映射意识注意力机制，改善了大型户外场景的空间对应性和分解质量。在前向渲染中，利用CLIP空间插值天气提示实现了精细的天气控制。还引入了合成和真实世界的数据集，包含38,000和18,000张不同天气条件下的图像，并附有内在映射注释。
### Conclusion
WeatherDiffusion在与最先进的像素空间编辑方法、天气恢复方法和基于渲染的方法比较中表现出色，展示了在自主驾驶等下游任务中的潜力，有助于增强在恶劣天气情景下的检测和分割鲁棒性。
## 222. `cs.AI` - 轻量级异物检测模块化现场解决方案在农业可持续养分管理中的应用 [PDF](https://arxiv.org/pdf/2509.12247), [HTML](https://arxiv.org/abs/2509.12247)
### Authors
Abigail R. Cohen,Yuming Sun,Zhihao Qin,Harsh S. Muriki,Zihao Xiao,Yeonju Lee,Matthew Housley,Andrew F. Sharkey,Rhuanito S. Ferrarezi,Jing Li,Lu Gan,Yongsheng Chen
### Background
高效的养分管理对于作物生长和可持续资源消耗（如氮和能源）至关重要。当前的管理方法需要长时间分析，无法实现实时优化。图像处理技术虽然可以快速进行表型分析，但也可能计算消耗量大，导致在资源受限条件下难以部署。
### Innovation
该研究提出了一种灵活的、分层次的管道，用于异常检测和状态估计（新鲜重量、干重和组织养分），并进行了全面的能效分析，涵盖效率与准确度的谱系。通过使用多光谱成像（MSI）和营养耗尽实验，开发了一个基于自动编码器（AE）的早期预警管道。进一步对比了不同的状态估计模块，分别使用植被指数（VI）特征结合机器学习（随机森林，RF）和原始全图像深度学习（视觉变压器，ViT）进行详细分析。
### Conclusion
模块化管道开启边沿诊断的机会，为农业可持续养分管理提供了实际应用前景。
## 223. `cs.AI` - Reasoning Transfer for an Extremely Low-Resource and Endangered Language: Bridging Languages Through Sample-Efficient Language Understanding [PDF](https://arxiv.org/pdf/2504.02890), [HTML](https://arxiv.org/abs/2504.02890)
### Authors
Khanh-Tung Tran,Barry O'Sullivan,Hoang D. Nguyen
### Background
近年来，大型语言模型在生成链式思考（CoT）推理的方面取得了显著进展，但这些进展主要集中在资源丰富语言上，而低资源语言则被忽略。本文旨在通过探索链式思考技术在极度低资源场景下的应用，弥补低资源语言在这方面的空白。
### Innovation
引入了基于英语桥梁的链式思考训练方法（English-Pivoted CoT Training），利用LLM在潜在空间中倾向于主要语言的洞察。对于输入的低资源语言，先进行监督微调生成英语链式思考，再输出目标语言的最终响应。该方法在数学推理基准测试中表现出色，相较于其他基线方法在低资源场景下提升最高可达28.33%。此外，研究还发现明确分离语言理解与推理能增强跨语言推理能力，通过混合语言链式思考和两阶段训练进一步验证了这一发现。进一步推出了数据稀缺的极度低资源和濒危语言爱尔兰语的多数学任务基准LC2024。
### Conclusion
我们的研究结果和资源为未来的多语言推理提供了一条实际路径，能够在数据稀缺的情况下进行跨语言推理，而无需在所有极度低资源的语言中进行广泛的重新训练。
## 224. `cs.AI` - 组成任务结构中模式匹配及其局限性表征 [PDF](https://arxiv.org/pdf/2505.20278), [HTML](https://arxiv.org/abs/2505.20278)
### Authors
Hoyeon Chang,Jinho Park,Hanseul Cho,Sohee Yang,Miyoung Ko,Hyeonbin Hwang,Seungpil Won,Dohaeng Lee,Youbin Ahn,Minjoon Seo
### Background
尽管大语言模型（LLMs）具有令人印象深刻的性能，但它们的成功往往依赖于模式匹配的行为，然而，这种模式匹配也导致了在组合任务中对外域泛化的失败。行为研究通常使用允许多种泛化来源的任务设置（例如，代数不变性和结构性重复），这使得难以精确且可测试地了解LLMs是如何通过模式匹配进行泛化的以及它们的局限性。
### Innovation
本文首先将模式匹配形式化为功能等价性，即识别输入子序列对，这些子序列在保持其余输入不变的情况下始终产生相同的结果。继而，系统研究了仅解码器Transformer和Mamba在隔离模式匹配机制的控制任务中的表现。这种形式化提供了预测性和定量性见解：(1) 模式匹配的实例成功率可以用见证功能性等价性的上下文数量来很好地预测。(2) 证明了学习两跳结构的紧样本复杂性边界，并通过确定数据缩放律的指数来预测完全领域内泛化的性能。(3) 路径不明确是结构性障碍：当变量通过多种路径影响输出时，模型无法形成统一的中间状态表示，从而影响准确性和可解释性。(4) 思路是一种减少数据需求的方法，但并不能解决路径不明确的问题。
### Conclusion
我们提供了一个预测性的、可证伪的边界来描述模式匹配，并提出了一种基础诊断方法，用于解开混合泛化机制。
## 225. `cs.AI` - 无遮罩阴影去除中的对比先验增强二元性 [PDF](https://arxiv.org/pdf/2507.21949), [HTML](https://arxiv.org/abs/2507.21949)
### Authors
Jiyu Wu,Yifan Liu,Jiancheng Huang,Mingfu Yan,Shifeng Chen
### Background
现有的阴影去除方法通常依赖于遮罩，但在实际场景中很难获得。探索内在图像线索，如局部对比信息，为在缺乏明确遮罩的情况下指导阴影去除提供了可能。然而，在复杂场景中，这些线索的固有歧义性会成为限制因素，无法区分真正的阴影和低反射率物体以及复杂的背景纹理。
### Innovation
提出了自适应门控双分支注意机制（AGBA），这种机制动态筛选并重新权重建对比度信息，有效解纠缠阴影特征与其他干扰视觉元素。为解决恢复柔和阴影边界和精细细节的持续挑战，引入了基于扩散的频率-对比融合网络（FCFN），利用高频和对比信息来引导生成过程。
### Conclusion
大量实验表明，该方法在无遮罩方法中达到了最先进的水平，同时在与基于遮罩方法的竞争性能方面保持了竞争力。
## 226. `cs.AI` - 使用LLM智能体增强时序预测 [PDF](https://arxiv.org/pdf/2508.04231), [HTML](https://arxiv.org/abs/2508.04231)
### Authors
Chin-Chia Michael Yeh,Vivian Lai,Uday Singh Saini,Xiran Fan,Yujie Fan,Junpeng Wang,Xin Dai,Yan Zheng
### Background
大规模语言模型（LLM）驱动的代理已成为自动化机器学习（AutoML）系统的有效规划者。大多数现有的AutoML方法侧重于自动化特征工程和模型架构搜索。然而，近期关于时间序列预测的研究表明，轻量级模型可以常常达到最先进的性能。基于这一观察，本文探索改进数据质量而非模型架构作为时间序列数据上潜在有效的AutoML方向。
### Innovation
本文提出了DCATS，一种数据为中心的时间序列智能体。DCATS利用伴随时间序列的元数据来清理数据并优化预测性能。通过使用四种时间序列预测模型在大规模交通流量预测数据集上的评估结果表明，DCATS能平均减少6%的误差，突显了数据为中心的方法在时间序列预测的AutoML中的潜力。
### Conclusion
结果表明，DCATS可以在时间序列预测的AutoML中实现性能优化，进一步验证了数据为中心的方法的有效性。
## 227. `cs.AI` - 不完美信息游戏中静态对手的一致建模 [PDF](https://arxiv.org/pdf/2508.17671), [HTML](https://arxiv.org/abs/2508.17671)
### Authors
Sam Ganzfried
### Background
在多智能体环境中，智能体的目标是最大化与对手互动时获得的总奖励。使用博弈论的概念，如纳什均衡，可能在某些情况下获得很好的性能，但这些方法未能充分利用历史上和观察到的重复交互数据。现有的对手建模算法利用机器学习技术来利用可用数据来捕捉对手的亚优行为，但这些方法目前在不完美信息博弈中的效果有限。
### Innovation
提出了一个新算法，该算法能够实现一种性质：即使是对来自已知先验分布的静态对手，该算法也能够保证在游戏迭代次数无限趋近于无穷大时，模型能够逼近对手的真实策略。该算法通过解决基于序列形式博弈表示的凸最小化问题，并使用投影梯度下降法来高效地实现这一目标。
### Conclusion
该算法能在利用游戏观察数据的基础上，甚至如果有可用的历史数据，也能够高效地收敛到对手的真实策略。
## 228. `cs.AI` - 开源语言模型中特殊字符对抗攻击的研究 [PDF](https://arxiv.org/pdf/2508.14070), [HTML](https://arxiv.org/abs/2508.14070)
### Authors
Ephraiem Sarabamoun
### Background
大语言模型（LLMs）在各种自然语言处理任务中取得了显著的成果，但它们对抗字符级别的恶意操控的脆弱性给实际部署带来了重要的安全挑战。本文研究了多种特殊的字符攻击，包括Unicode、同形字符、结构编码和文本编码攻击，这些攻击旨在规避安全机制。研究使用了7个流行的开源模型，参数范围从3.8亿到32亿，进行了4000多次攻击尝试。
### Innovation
研究分析了开源模型在面对不同类型的字符级别攻击时的安全威胁，揭示了所有模型尺寸在这些攻击下的关键漏洞。这些实验显示出了各种严重失效模式，比如成功突破安全机制、输出不连贯和生成无关的幻觉。
### Conclusion
研究表明，开源语言模型在小到中型规模模型中普遍存在严重的安全漏洞。这些发现揭示了突破语言模型安全机制的多种途径，强调了在实际部署中加强防御措施的重要性。
## 229. `cs.AI` - In-context 学习中任务导向性信息删除机制 [PDF](https://arxiv.org/pdf/2509.21012), [HTML](https://arxiv.org/abs/2509.21012)
### Authors
Hakaze Cho,Haolin Yang,Gouki Minegishi,Naoya Inoue
### Background
In-context 学习（ICL）是一种基于现代语言模型（LMs）的新兴少样本学习范式，但其内部机制仍然不清楚。本文通过信息删除的全新视角，探讨了这一机制。
### Innovation
研究证明，在零样本场景中，LMs 将查询编码为包含所有可能任务信息的非选择性表示，导致无针对性的结果；通过低秩过滤器有选择地从隐藏状态中删除特定信息能引导 LM 目标任务。通过测量精心设计指标的隐藏状态，发现少样本 ICL 能够模拟任务导向性信息删除过程，通过删除纠缠的非选择性表示中的冗余信息来提高输出，这是 ICL 的关键机制。同时，识别出执行删除操作的重要注意力头，称为去噪头。实验表明，在验证信息删除操作对推理的影响后，ICL 准确率显著下降，特别是在少量样本示范中缺少正确标签时，进一步证实了信息删除机制和去噪头的关键作用。
### Conclusion
少样本 ICL 通过其任务导向性信息删除机制，能够在示范基础上生成更准确的输出，去噪头在这一过程中发挥重要作用，而缺少信息删除操作会严重影响 ICL 的性能。
## 230. `cs.AI` - 对称保群流匹配在对称破缺分岔问题中的应用 [PDF](https://arxiv.org/pdf/2509.03340), [HTML](https://arxiv.org/abs/2509.03340)
### Authors
Fleur Hendriks,Ondřej Rokoš,Martin Doškář,Marc G.D. Geers,Vlado Menkovski
### Background
非线性动力系统中的分岔现象常常导致多个共存的稳定解，特别是在对称性被打破的情况下。确定性机器学习模型难以捕捉这种多样性，它们会平均处理多种解，从而无法代表低对称的解。
### Innovation
提出了基于流匹配的生成框架，用于建模分岔结果的完整概率分布。该方法可以通过等变建模来保留系统的对称性，并通过引入对称匹配策略，在群作用下对预测和目标输出进行对齐，从而实现准确的等变学习。该方法在从玩具模型到复杂的物理问题（如弯曲梁和Allen-Cahn方程）的多个系统验证中表现出色，显著优于非概率性和变分方法。
### Conclusion
流匹配方法在捕捉多模态分布和对称性破缺分岔方面优于现有方法，为高维系统中的多稳态建模提供了一个原则性且可扩展的解决方案。
## 231. `cs.AI` - 对齐从何处开始？扩散大语言模型可能需要独特的定位 [PDF](https://arxiv.org/pdf/2508.12398), [HTML](https://arxiv.org/abs/2508.12398)
### Authors
Zhixin Xie,Xurui Song,Jun Luo
### Background
扩散大语言模型（dLLMs）作为一种非自回归范式，由于其独特的训练和推理方法，已成为一个竞争性的替代方案。然而，这种新型架构的安全性研究目前尚未开展。本文首次对dLLMs的安全性能进行了分析，并提出了一种针对其独特生成特性的新颖对齐方法。
### Innovation
本文基于dLLMs的防御者和攻击者之间的不对称性，提出了Middle-tOken Safety Alignment（MOSA）方法，这是一种直接利用强化学习对模型的中段生成进行安全对齐的方法。MOSA方法在两个基准上与八种攻击方法进行了比较，并在编码、数学和一般推理方面测试了对齐后的dLLMs，证明了其优越性。
### Conclusion
研究结果证明了MOSA方法在提高dLLMs的安全性能方面的优势，表明在对dLLMs进行安全对齐时，中段生成的对齐可能是关键。
## 232. `cs.AI` - 统一的噪声-曲率视角下的训练退化问题 [PDF](https://arxiv.org/pdf/2509.19698), [HTML](https://arxiv.org/abs/2509.19698)
### Authors
Gunbir Singh Baveja,Alex Lewandowski,Mark Schmidt
### Background
在持续学习过程中，训练退化指的是参数更新不再对优化目标产生改进，导致准确性停滞或下降的现象。现有指标（如海森矩阵秩、尖锐度级别、权重或梯度的范数、梯度到参数的比例、单位符号熵等）无法可靠预测这一现象。
### Innovation
提出了两个互补指标：基于批量大小的梯度噪声界和曲率波动控制界。将这两个指标结合进每层自适应噪声阈值，用于预测训练性行为。据此，提出了一种步长调度器，确保各层的有效参数更新保持在这一阈值之下，从而避免训练退化。验证了该调度器能提升之前方法（如拼接ReLU、Wasserstein正则化器、L2权重衰减）维护的准确性，并且不调参时生成的自适应步长轨迹能够模拟手工设计的步长衰减计划。
### Conclusion
该调度器能够避免训练退化现象，并通过对不同持续学习方法的改进，提高模型的准确性。无调参情况下，生成的自适应步长轨迹与人工设计的衰减计划相匹配。
## 233. `cs.AI` - SaFiRe: Saccade-Fixation Reiteration with Mamba for Referring Image Segmentation [PDF](https://arxiv.org/pdf/2510.10160), [HTML](https://arxiv.org/abs/2510.10160)
### Authors
Zhenjie Mao,Yuhuan Yang,Chaofan Ma,Dongsheng Jiang,Jiangchao Yao,Ya Zhang,Yanfeng Wang
### Background
Referring Image Segmentation (RIS)旨在根据自然语言表达来分割图像中的目标物体。近期的方法利用预训练的视觉骨干网络和更多的训练语料库取得了显著的成果，但它们主要集中在简单的表达上，如简短清晰的名词短语（例如“红色的汽车”或“左边的女孩”）。这种简化导致RIS变成了关键词/概念匹配的问题，而无法处理表达中的引用歧义。
### Innovation
本文识别了两个具有挑战性的现实场景：具有上下文线索的多个实体干扰的对象表达，以及未明确说明物体类别的类别隐式表达。为此，我们提出了一个名为SaFiRe的新框架，该框架模仿人类的两阶段认知过程——首先形成全局理解，然后通过对细节的检查进行精炼。此外，我们提出了一个名为aRefCOCO的新基准，专门用于评估包含模糊参考表达式的RIS模型。
### Conclusion
在标准和提出的数据集上的大量实验表明，SaFiRe在RIS基准上优于当前最先进的基线。
## 234. `cs.AI` - 分布偏移下的弱到强泛化 [PDF](https://arxiv.org/pdf/2510.21332), [HTML](https://arxiv.org/abs/2510.21332)
### Authors
Myeongho Jeon,Jan Sobotka,Suhwan Choi,Maria Brbić
### Background
随着未来超人类模型变得越来越复杂，准确监督它们的行为可能超过人类的能力。现有研究表明，在此类场景中，弱模型可以有效地监督强模型，这种现象被称为弱到强泛化。但是，研究发现，原始的弱到强泛化在分布偏移下往往会失效，通常导致强模型的表现不如其弱监督者。
### Innovation
我们提出了一种名为RAVEN的鲁棒弱到强泛化框架，它可以在学习强模型参数的同时，动态学习弱模型的最佳组合。通过在图像分类、文本分类和偏好对齐任务上的实验，RAVEN在分布外任务上的表现优于其他基线方法超过30%，在分布内任务上与现有方法相当或更好。此外，我们的结果显示RAVEN会给更准确的弱模型分配更高的权重，显示出自动识别可信监督的能力。
### Conclusion
我们的研究表明，RAVEN能够处理分布偏移问题，并自动识别可信的监督者，从而在多种任务中表现出优越性。
## 235. `cs.AI` - DensiCrafter：受物理约束的自支撑空心结构的生成与制造 [PDF](https://arxiv.org/pdf/2511.09298), [HTML](https://arxiv.org/abs/2511.09298)
### Authors
Shengqi Dang,Fu Chai,Jiaxin Li,Chao Yuan,Wei Ye,Nan Cao
### Background
3D生成模型的兴起使得从多种输入（例如文本或图像）自动合成3D几何和纹理成为可能，但这些方法通常忽视了物理约束和制造可行性。本文的重点在于生成既轻量化又自支撑的3D设计。
### Innovation
提出了DensiCrafter框架，通过优化密度场生成轻量化且自支撑的3D空心结构。该框架从Trellis生成的粗略体素网格开始，将这些网格解释为连续密度场进行优化，并引入了三个可微、物理受限且无需模拟的损失项。此外，通过对质量进行正则化惩罚未必要的材料，并通过限制优化域保护外部表面。该方法可以直接与预制的Trellis基模型兼容，无需任何架构更改。实验表明，与最先进的基线相比，该方法在减少材料质量方面表现出显著的改进，且设计能够实现可靠的制造和自支撑。
### Conclusion
广泛的评估表明，本方法在减少材料质量方面取得了显著的改进，最高可达43%。相比最先进的基线，该方法能提高设计的稳定性和保持高几何保真度。实验证明，我们的空心设计可以通过3D打印可靠地制造，并且能够自支撑。
## 236. `cs.AI` - 扩散模型在药物发现前沿：生成小分子和治疗肽的综述 [PDF](https://arxiv.org/pdf/2511.00209), [HTML](https://arxiv.org/abs/2511.00209)
### Authors
Yiquan Wang,Yahui Ma,Yuhan Chang,Jiayao Yan,Jialin Zhang,Minnuo Cai,Kai Wei
### Background
扩散模型已经成为了生成模型中的领先框架，有望改变传统的药物发现过程，该过程通常速度慢且成本高。研究表明，扩散模型在设计两种主要疗法：小分子和治疗肽方面有着广泛的应用。文章系统比较了扩散模型在两种疗法中的应用，并深入解析了统一的迭代去噪框架如何根据不同疗法的分子表示、化学空间和设计目标进行调整。
### Innovation
文章通过系统比较扩散模型在设计小分子和治疗肽两大疗法中的应用，展示了扩散模型如何根据不同疗法的特殊需求进行适应性调整，从而克服了结构设计、稳定性、免疫原性等不同挑战。此外，文章还指出通过跨疗法特定差距的桥梁建设以及将扩散模型整合到自动闭环Design-Build-Test-Learn（DBTL）平台中，能够释放扩散模型的全部潜力。
### Conclusion
文章总结表示，扩散模型的全部潜力将通过弥合疗法特异性差距和将其集成到自动闭环DBTL平台中而得以实现，从而将药物发现的范式从简单的化学探索转变为按需工程设计新型疗法。扩散模型的进一步改进将通过提高实验数据的质量、改进验证得分函数以及加强实验验证来实现。
## 237. `cs.AI` - 不同类别之间属性泛化能力并非平等：重思基于无关类别的属性泛化 [PDF](https://arxiv.org/pdf/2509.06998), [HTML](https://arxiv.org/abs/2509.06998)
### Authors
Liviu Nicolae Fircă,Antonio Bărbălau,Dan Oneata,Elena Burceanu
### Background
先前的研究已经针对狭义的或视觉上相似的领域解决了属性预测问题，但目前尚不清楚当前模型是否能抽象出属性并应用于概念上相距甚远的类别。本文首次提出了在这样条件下属性预测任务的鲁棒性评估，测试模型是否能够在不相关的物体类型之间正确推理共享的属性，例如确定“有四条腿”这一属性既适用于“狗”也适用于“椅子”。为实现该评估，我们引入了逐渐降低训练集与测试集之间相关性的训练-测试分割策略，这些策略基于LLM驱动的语义分组、嵌入相似度阈值、嵌入聚类以及基于地真实标签的上层类别划分。
### Innovation
本文提出了首次针对不相关类别间属性泛化的鲁棒性评估，设计了不同的训练-测试分割策略，包括LLM驱动的语义分组、嵌入相似度阈值、嵌入聚类以及基于地面真值标签的上层类别划分。这些方法有助于理解当前模型在泛化至无关类别时的能力边界，指出聚类方法能有效去除隐藏的相关性，同时保持学习性。
### Conclusion
实验结果表明，随着训练集和测试集之间相关性的降低，性能急剧下降，表明模型高度依赖于分割设计。聚类方法在控制隐藏相关性并保持可学习性方面表现最佳。这些发现提供对当前模型表示能力的新见解，并为未来属性推理解析的基准构建提供指导。
## 238. `cs.AI` - 全尺寸欺骗立体匹配：自动驾驶双目深度估计的物理 adversarial 攻击 [PDF](https://arxiv.org/pdf/2511.14386), [HTML](https://arxiv.org/abs/2511.14386)
### Authors
Kangqiao Zhao,Shuo Huai,Xurui Song,Jun Luo
### Background
尽管深度神经模型在自动驾驶中的感知应用展现了对对抗样本的脆弱性，但已知的攻击大多依赖2D补丁，主要针对单目感知。针对立体匹配模型，物理对抗样本（PAE）的有效性尚未被充分探索。本文分析了当前对抗样本攻击中存在的不足，特别是在立体视觉深度估计中的应用。
### Innovation
本文提出了针对自动驾驶立体匹配模型的第一个纹理增强物理对抗攻击方法。该方法使用3D PAE并结合全局伪装纹理，确保在不同视角下保持视觉一致性和攻击有效性。同时，本文提出了新的3D立体匹配渲染模块，以应对立体相机的差异效应对齐要求，并提出了一种新的合并攻击方法，以细腻化PAE优化无缝地将目标融入环境，增强了攻击的隐蔽性和致命性。
### Conclusion
广泛的评估结果表明，本文提出的PAE能够成功使立体模型产生错误的深度信息，突显了在自动驾驶双目深度估计中对物理对抗样本的攻击新颖性和有效性。
## 239. `cs.AI` - 迷失在序列化中：LLM图推理的不变性和泛化能力 [PDF](https://arxiv.org/pdf/2511.10234), [HTML](https://arxiv.org/abs/2511.10234)
### Authors
Daniel Herbst,Lea Karbevska,Divyanshu Kumar,Akanksha Ahuja,Fatemeh Gholamzadeh Nasrabadi,Fabrizio Frasca
### Background
基于大型语言模型（LLMs）的图推理器具有一定的前景，但缺乏对图表示中的对称性的内置不变性。在对图的序列化操作上，LLMs在节点重新索引、边重新排序或格式变化下可能会生成不同的输出，这引发了对于其稳健性的担忧。
### Innovation
该研究系统分析了这些影响，探讨了微调如何影响编码敏感性和新任务上的泛化能力。提出了将图序列化分解为节点标记、边编码和语法的一套原理性方法，并在全面的基准测试套件上评估了LLM对这些每个因素变化的稳健性。此外，还贡献了一套新的谱任务，用于进一步评估微调推理器的泛化能力。研究结果显示，非微调的大型模型比微调模型更为稳健，微调可能会减少对节点重新标记的敏感性但可能增加对结构和格式变化的敏感性，同时不会一致地提高在未见任务上的表现。
### Conclusion
研究发现， larger（非微调）模型在各方面的表现更为稳健。通过微调虽然可以减少对于节点重标记的敏感性，但却可能增加对结构和格式变化的敏感性，这种变化并不一致地提升在未见任务上的表现，提供了一套新的谱任务来进一步评估微调推理器的泛化能力。
## 240. `cs.AI` - Transformer模型中逆排列学习的不可能性 [PDF](https://arxiv.org/pdf/2509.24125), [HTML](https://arxiv.org/abs/2509.24125)
### Authors
Rohan Alur,Chris Hays,Manish Raghavan,Devavrat Shah
### Background
本文研究解码器型变压器中逆排列学习的问题。给定一个排列和该排列已经应用到的字符串，模型的任务是生成原始的（“标准”的）字符串。作者认为该任务模拟了各种推理任务中的自然鲁棒性，包括长上下文检索、多项选择问答和上下文学习。
### Innovation
主要贡献在于证明了一个不可能性结果：解码器型变压器无论深度如何都不可能学习这种任务。此外，介绍了一种替代构造，其中第一个强调因果注意力掩码的基本作用，突显了编解码器模型和更流行的解码器型架构的表达能力差异。第二个结果则是更令人惊讶的，通过在输入中添加“污点标记”来实现逆排序学习的可能性，这可能表明在大型语言模型中，链式思考提示或更广泛而言的中间思考标记可以促进推理，即使这些标记本身没有有意义的语义信息（例如中间计算的结果）。
### Conclusion
本文表明，解码器型变压器模型无法学习逆排列学习任务，并指出因果注意力掩码的作用可能有助于理解为什么在大型语言模型中某些形式的中间思考可能有助于提升推理能力。
## 241. `cs.AI` - 利用概念学习数据集揭示大型语言模型中的隐性偏差 [PDF](https://arxiv.org/pdf/2510.01219), [HTML](https://arxiv.org/abs/2510.01219)
### Authors
Leroy Z. Wang
### Background
本文介绍了用于揭示大型语言模型隐性偏差的概念学习任务数据集。通过在上下文中的概念学习实验，研究发现语言模型可能具有向上单调性的偏见；这种偏见在模型直接提示而没有概念学习组件的情况下测试时不太明显。这表明在上下文中的概念学习可以有效发现语言模型中的隐蔽偏差。
### Innovation
提出了一个概念学习任务数据集，以揭示大型语言模型中的隐性偏差。通过在不同的实验条件下观察语言模型的行为，表明了概念学习在揭示模型潜在偏见方面的有效性。
### Conclusion
研究表明，在上下文中的概念学习可以帮助识别语言模型中的隐性偏差，这对于提高模型的公正性和透明性具有重要意义。
## 242. `cs.AI` - PointNSP：基于下一级细节预测的自回归3D点云生成 [PDF](https://arxiv.org/pdf/2510.05613), [HTML](https://arxiv.org/abs/2510.05613)
### Authors
Ziqiao Meng,Qichao Wang,Zhiyang Dou,Zixing Song,Zhipeng Zhou,Irwin King,Peilin Zhao
### Background
自回归点云生成在质量和基于扩散的方法存在较大差距，这是因为自回归模型在生成形状时必须遵循一种人为的顺序，这限制了它们捕捉长距离依赖的能力，影响全局结构如对称性、拓扑一致性以及大尺度几何规律的保持。
### Innovation
PointNSP 提出了一个多尺度分解的生成框架，结合了层次细节（LOD）模型的理念，从低分辨率开始保存全局形状结构，并在更高尺度上通过预测下一等级几何逐渐细化，避免了强制固定的顺序限制，同时允许丰富的局部交互。
### Conclusion
实验表明，PointNSP 在自回归框架下首次实现了最先进的生成质量，并且在参数、训练和推理效率上优于强大的基于扩散的基线方法。在稠密生成8,192个点的情况下，其优势更加明显，体现了其可扩展性潜力。
## 243. `cs.AI` - 工业缺陷检测的自动化神经架构设计 [PDF](https://arxiv.org/pdf/2510.06669), [HTML](https://arxiv.org/abs/2510.06669)
### Authors
Yuxi Liu,Yunfeng Ma,Yi Tang,Min Liu,Shuai Jiang,Yaonan Wang
### Background
工业表面缺陷检测对于确保产品质量和制造业可靠性至关重要。现有的SDD方法主要依赖于人工设计模型，这些模型需要大量的尝试和错误，并且在解决内部差异和类间相似性两个主要挑战时常常效果不佳。
### Innovation
本文提出了AutoNAD，这是一种针对SDD的自动化神经架构设计框架，它联合搜索卷积、变压器和多层感知机。这种混合设计能够捕捉细微的局部变化和长距离的语义上下文，从而解决两个主要挑战，同时减少人工网络设计的成本。为了支持对如此多样搜索空间的高效训练，AutoNAD引入了一种交叉权重共享策略，这加速了超网络的收敛并提高了子网络的性能。此外，还集成了一个可搜索的多层级特征聚合模块（MFAM），以增强多尺度特征学习。为了提高工业部署时的运行效率，AutoNAD还结合了延迟感知先验，以指导高效架构的选择。
### Conclusion
AutoNAD在三个工业缺陷数据集上的有效性得到了验证，进一步将其应用于缺陷成像和检测平台。源代码可在此链接查看。
## 244. `cs.AI` - 时间蝮蛇：一种用于高效长视频理解的混合Mamba-Transformer视觉语言模型 [PDF](https://arxiv.org/pdf/2511.16595), [HTML](https://arxiv.org/abs/2511.16595)
### Authors
Boshen Xu,Zihan Xiao,Jiaze Li,Jianzhong Ju,Zhenbo Luo,Jian Luan,Qin Jin
### Background
处理长视频需要有效的模型架构和处理长期时间上下文的有效机制。现有模型在处理长视频时面临挑战，需要既有效的模型架构，又能应对长时间序列信息的理解。
### Innovation
TimeViper采用了混合Mamba-Transformer骨干网，结合了状态空间模型的效率和注意力机制的表达能力。通过这一混合设计，作者发现了一种视觉到文本的信息聚合现象，即信息从视觉令牌逐渐流向文本令牌，导致视觉令牌冗余严重。因此，作者提出了一种Token信息传输模块（TransV），该模块可以将视觉令牌压缩到指令令牌中，同时保持多模态理解能力，使TimeViper能够处理超过10,000帧的小时长视频。此外，该研究分析了Mamba和Transformer层的注意力行为，提供了对混合模型解释性的新见解。
### Conclusion
该研究代表了开发、解释和压缩混合Mamba-Transformer架构的初步步骤，展示了TimeViper在不同基准测试中的竞争力和扩展的帧数能力。
## 245. `cs.AI` - 基于野生环境 talking-head 视频的面部时间微动态分析的无干预痴呆筛查 [PDF](https://arxiv.org/pdf/2511.13802), [HTML](https://arxiv.org/abs/2511.13802)
### Authors
Filippo Cenacchi,Longbing Cao,Mitchell McEwan,Deborah Richards
### Background
大多数现有的资源侧重于言语或脚本化访谈，限制了其在诊所之外的使用，并且预测与语言和转录有关联。现有的痴呆筛查方法大多需要言语或脚本化的访谈，但有时这些要求在自然场景中难以满足。本研究针对传统的筛查方法，开发了一种面部时间微动态分析方法，用于从简短的面向摄像机的交谈头部视频中进行主动痴呆筛查。该方法专注于检测面部微运动，而不依赖言语或文字，以实现无干预、大规模和自然条件下视频分析，适用于设备、话题和文化的跨域应用。
### Innovation
提出了面部时间微动态分析技术，用于基于无脚本、自然场景的视频进行痴呆筛查。该技术专注于检测面部微运动（如眨眼动态、小嘴颚动作、注视变化和微妙头部调整）作为痴呆早期变化的指标，而这些变化通过面部表情和面部动作的微小变化难以直接观察到。此外，还构建了名为 YT DemTalk 的新数据集，用于测试和基准评估模型。
### Conclusion
通过稳定性处理将面部微运动转换为可解释的时间序列，并将其总结为简短窗口中的紧凑剪辑级别统计信息，用于筛查。在 YT DemTalk 数据集上，通过消融实验发现了注视变化和口部/颚动态是最具信息量的提示，浅层轻量级分类器能实现痴呆预测性能（AUROC）0.953，平均精确度 (AP) 0.961，F1分数 0.851 和准确度 0.857。
## 246. `cs.AI` - 通过树组双意识搜索和优化实现的对抗攻击-防御共生演化以实现LLM安全对齐 [PDF](https://arxiv.org/pdf/2511.19218), [HTML](https://arxiv.org/abs/2511.19218)
### Authors
Xurui Li,Kaisong Song,Rui Zhu,Pin-Yu Chen,Haixu Tang
### Background
大型语言模型（LLMs）已经在网络服务中迅速发展，提供了前所未有的能力，但同时也放大了社会风险。现有研究大多专注于孤立的破解攻击或静态防护，忽视了在真实网络环境中不断演变的威胁与防护措施之间的动态互动。
### Innovation
本文提出了ACE-Safety（对抗共演化安全）框架，这是一个新颖的框架，通过无缝整合两大创新步骤来优化攻击和防御模型：1. 组意识策略引导蒙特卡洛树搜索（GS-MCTS），有效探索破解策略，发现漏洞并生成多样化的对抗样本；2. 对抗课程树意识组策略优化（AC-TGPO），通过对具有挑战性的样本进行课程强化学习联合训练攻击和防御LLMs，从而实现稳健的双向提升。
### Conclusion
我们的方法在多个基准测试中的表现超过了现有的攻击和防御方法，并提供了一条开发可持续支持负责任AI生态系统的LLMs可行途径。
## 247. `cs.AI` - 涡扇发动机剩余使用寿命预测中具有学习型偶然不确定性感知的深度学习框架 [PDF](https://arxiv.org/pdf/2511.19124), [HTML](https://arxiv.org/abs/2511.19124)
### Authors
Krishang Sharma
### Background
在航空维修诊断中，准确预测剩余使用寿命（RUL）并与不确定性量化相结合一直是一项关键挑战。现有的CMAPSS相关文献中，尚未探索直接通过概率建模学习偶然不确定性的方法。
### Innovation
该研究引入了一种新颖的不确定性感知深度学习框架，能够直接通过概率建模学习偶然不确定性。该架构包含多尺度Inception块进行时间模式提取，双向长短期记忆网络进行序列建模，以及双层注意力机制同时在传感器和时间维度上操作。框架创新之处在于使用贝叶斯输出层预测RUL均值和方差，使模型能够学习数据内在的不确定性。此框架在NASA CMAPSS基准测试（FD001-FD004）实验中展现出竞争力的整体性能，在关键区间的性能提升25-40%，并为安全关键预测建立了新标准。
### Conclusion
该框架通过学习到的不确定性提供95%置信区间，覆盖范围从93.5%到95.2%，使得风险感知维护排程成为可能，先前在CMAPSS文献中无法实现。
## 248. `cs.AI` - SARVLM: SAR领域语义理解和目标识别的视觉语言基础模型 [PDF](https://arxiv.org/pdf/2510.22665), [HTML](https://arxiv.org/abs/2510.22665)
### Authors
Qiwei Ma,Zhiyu Wang,Wang Liu,Xukun Lu,Bin Deng,Puhong Duan,Xudong Kang,Shutao Li
### Background
SAR成像是一种重要的成像方式，因其可以全天候成像而备受瞩目。尽管自监督学习和掩码图像建模等方法已经在SAR领域取得了进展，但我们发现这些方法更侧重于低级视觉特征，常常忽视SAR图像中的多模态对齐和零样本目标识别。
### Innovation
本文构建了包含超过一百万图像-文本配对的SARVLM-1M大规模视觉-语言数据集，并提出了一种领域迁移训练策略，以弥合自然图像与SAR图像之间的鸿沟。在此基础上，开发了SARVLM，这是一种专为SAR设计的视觉语言基础模型，包含SARCLIP和SARCap，并通过提出的领域迁移策略，使用视觉-语言对比目标进行训练，从而连接SAR图像与文本描述。
### Conclusion
在图像文本检索、零样本分类、语义定位和图像描述等多个方面的实验显示，SARVLM在特征提取和解释方面表现出色，超越了现有的视觉语言基础模型，并推进了SAR语义理解。相关代码和数据集将很快发布。
## 249. `cs.AI` - DR Tulu: 通过不断进化的评分表进行强化学习的深入研究 [PDF](https://arxiv.org/pdf/2511.19399), [HTML](https://arxiv.org/abs/2511.19399)
### Authors
Rulin Shao,Akari Asai,Shannon Zejiang Shen,Hamish Ivison,Varsha Kishore,Jingming Zhuo,Xinran Zhao,Molly Park,Samuel G. Finlayson,David Sontag,Tyler Murray,Sewon Min,Pradeep Dasigi,Luca Soldaini,Faeze Brahman,Wen-tau Yih,Tongshuang Wu,Luke Zettlemoyer,Yoon Kim,Hannaneh Hajishirzi,Pang Wei Koh
### Background
当前的深度研究模型多采用逐步骤生成长篇详细回答，但大多数开放的深度研究模型是通过强化学习与可验证奖励（RLVR）训练在简单的易验证问答任务上，这无法延伸到现实中的长篇任务。
### Innovation
提出了强化学习与不断进化的评分表（RLER），通过构建和维护随训练中的策略模型共同进化的评分表，从而能够将模型探索的新信息纳入评分表中，提供更为区分性的、基于策略的反馈。利用RLER，开发了Deep Research Tulu（DR Tulu-8B），这是首个直接被训练用于开放性长篇深度研究的开放模型。
### Conclusion
DR Tulu 在四个涉及科学、医疗和一般领域的长篇深度研究基准中显著优于现有的深度研究模型，并且在准确性和性价比上与商用系统相当。为了促进未来研究，所有数据、模型和代码，以及新建立的基于MCP的深度研究系统代理基础设施均已被公开。
## 250. `cs.AI` - Pistachio: 向合成、均衡且长篇形式的视频异常基准迈进 [PDF](https://arxiv.org/pdf/2511.19474), [HTML](https://arxiv.org/abs/2511.19474)
### Authors
Jie Li,Hongyi Cai,Mingkang Dong,Muxin Pu,Shan You,Fei Wang,Tao Huang
### Background
现有的视频异常检测（VAD）基准在场景多样性、异常类型覆盖的平衡性和时间复杂性方面存在不足，难以准确评估真实世界的性能。同时，社区正转向视频异常理解（VAU），需要更深层次的语义和因果推理，但由于依赖大量手动标记，难以进行基准测试。
### Innovation
Pistachio 是一个通过受控生成管道构建的新VAD/VAU基准，利用近期进步的视频生成模型，精确控制场景、异常类型和时间叙事，消除互联网收集数据集的偏见和局限性。实验表明Pistachio在规模、多样性和复杂性方面具有优势，为现有方法提供了新的挑战，并激励未来对动态和多事件异常理解的研究。
### Conclusion
Pistachio 提出了新的基准，解决了现有VAD/VAU基准的局限性，通过合成生成的方法增强了场景控制和时间叙事的均衡性，提供了更真实的问题背景，进一步推动了该领域的研究。
## 251. `cs.AI` - ConceptGuard: 文本和图像生成视频中的多模态风险检测以实现主动安全 [PDF](https://arxiv.org/pdf/2511.18780), [HTML](https://arxiv.org/abs/2511.18780)
### Authors
Ruize Ma,Minghong Cai,Yilei Jiang,Jiaming Han,Yi Feng,Yingshui Tan,Xiaoyong Zhu,Bo Zhang,Bo Zheng,Xiangyu Yue
### Background
近期生成模型的进步使得能够从结合文本和图像的多模态提示中生成高质量的视频。虽然这些系统提供了增强的可控性，但也带来了新的安全风险，这些风险可能来自单模态或它们的交互。现有安全方法通常仅基于文本，需要预先了解风险类别，或者作为生成后的审计员，难以积极缓解这种组合的多模态风险。
### Innovation
本文提出了一种统一的安全防护框架，以主动检测和缓解多模态视频生成中的不安全语义。该框架分为两个阶段：第一阶段使用对比检测模块通过将融合图像-文本输入投影到结构化的概念空间中来识别潜在的安全风险；第二阶段使用语义抑制机制通过干预提示的多模态条件来引导生成过程远离不安全的概念。
### Conclusion
通过在两个基准上的全面实验，ConceptGuard 在风险检测和安全视频生成方面都表现出色，一致性地优于现有基线，实现了最先进的成果。为了支持该框架的发展和严格评估，我们引入了两个新的基准：基于多模态风险的ConceptRisk数据集和专门适用于文本和图像生成视频（TI2V）安全设置的T2VSafetyBench-TI2V基准。我们的代码可以在该链接中获取。
## 252. `cs.AI` - UniGame: 将统一多模态模型转变为其自身的对手 [PDF](https://arxiv.org/pdf/2511.19413), [HTML](https://arxiv.org/abs/2511.19413)
### Authors
Zhaolong Su,Wang Lu,Hao Chen,Sharon Li,Jindong Wang
### Background
统一多模态模型（UMMs）在理解和生成方面表现出色，但仍然存在着结构上的矛盾：理解需要紧凑的嵌入，而生成则需要重建丰富的表示。这种结构上的权衡导致了决策边界的偏离、跨模态一致性的下降，以及对分布变化和对抗性攻击的脆弱性增加。
### Innovation
提出了自对抗的后训练框架UniGame，该框架通过在共享的token接口处应用轻量级扰动，使生成分支能够主动寻求并挑战脆弱的理解，从而使模型自身变成其自身的对手。实验结果显示，UniGame在一致性上提高了4.6%，理解上提高了3.6%，生成上提高了0.02，且在分布外和对抗鲁棒性方面分别提高了4.8%和6.2%（在NaturalBench和AdVQA上）。该框架对模型架构无依赖，新增参数小于1%，并可与现有后训练方法互补。
### Conclusion
UniGame将自对抗机制引入多模态模型后训练中，通过模型自造对抗实例来提高模型的一致性、稳定性、统一能力，提出自对抗作为增强未来多模态基础模型一致性和鲁棒性的通用有效原则。
## 253. `cs.AI` - 视觉性思考，文本性推理：ARC中的视觉语言协同作用 [PDF](https://arxiv.org/pdf/2511.15703), [HTML](https://arxiv.org/abs/2511.15703)
### Authors
Beichen Zhang,Yuhang Zang,Xiaoyi Dong,Yuhang Cao,Haodong Duan,Dahua Lin,Jiaqi Wang
### Background
前沿基础模型如GPT-5和Grok 4在从少量实例中进行抽象推理方面仍面临核心难题。现有方法大多将ARC-AGI视为纯粹的文字推理任务，但忽视了人类解决这类问题时高度依赖视觉抽象的特点。通过实验，作者发现直接将ARC-AGI的网格转化为图像会因规则执行不够精确而降低性能。
### Innovation
本文提出了视觉语言协同推理（VLSR）策略和模态切换自我校正（MSSC）策略。VLSR将ARC-AGI任务分解为模态对齐的子任务，而MSSC则利用视觉信息验证文本推理以进行内在纠错。实验结果表明，在多种顶级模型和多个ARC-AGI任务上，这种新方法可提高多达4.33%的表现。
### Conclusion
研究结果表明，将视觉抽象与语言推理统一起来是未来基础模型实现具有通用性和类人智能的关键步骤。
## 254. `cs.AI` - PrefixGPT: Prefix Adder Optimization by a Generative Pre-trained Transformer [PDF](https://arxiv.org/pdf/2511.19472), [HTML](https://arxiv.org/abs/2511.19472)
### Authors
Ruogu Ding,Xin Ning,Ulf Schlichtmann,Weikang Qian
### Background
前缀加法器在计算密集型应用中因其高速度而被广泛使用。然而，由于严格的设规规则和庞大复杂的寻优空间，优化前缀加法器的设计是一项挑战。
### Innovation
引入了PrefixGPT，这是一种生成型预训练变换器(GPT)，可以从空白开始直接生成优化的前缀加法器。该模型针对前后缀加法器的拓扑结构使用了一种定制的解码器只读变换器架构，并在训练过程中应用了合法性掩码，确保生成的所有设计都从设计之初就合法。通过预训练学习设计规则，然后微调以优化设计质量。相比现有方法，PrefixGPT不仅发现了具有7.7%更好面积延时积(ADP)的新最优设计，还在探索质量上表现出优越性，平均ADP降低了最多79.1%。
### Conclusion
这表明GPT风格的模型在掌握复杂硬件设计原则后，可用于更有效的设计优化。
## 255. `cs.AI` - LightMem：轻量级高效的增强生成记忆系统 [PDF](https://arxiv.org/pdf/2510.18866), [HTML](https://arxiv.org/abs/2510.18866)
### Authors
Jizhan Fang,Xinle Deng,Haoming Xu,Ziyan Jiang,Yuqi Tang,Ziwen Xu,Shumin Deng,Yunzhi Yao,Mengru Wang,Shuofei Qiao,Huajun Chen,Ningyu Zhang
### Background
尽管大型语言模型（LLMs）具有出色的性能，但它们在动态和复杂环境中难以有效利用历史交互信息。现有的记忆系统虽然引入了持久的信息存储、检索和利用机制，但仍存在显著的时间和计算开销问题。
### Innovation
LightMem 是一种新的记忆系统，平衡了记忆系统的性能和效率。它借鉴Atkinson-Shiffrin的人类记忆模型，将记忆分为三个互补阶段：认知启发的感觉记忆迅速通过轻量级压缩筛选无关信息并按照主题分组；主题意识的短期记忆在此基础上对这些主题组进行组织和总结，以便更结构化的访问；长时间记忆结合睡眠时间更新，采用离线程序，将巩固过程与在线推理相分离。
### Conclusion
实验结果表明，在 LongMemEval 和 LoCoMo 上，使用 GPT 和 Qwen 作为骨干模型，LightMem 一贯超越了强力基线，提高了 QA 准确率高达 7.7% / 29.3%，减少了总 token 使用量高达 38x / 20.9x，API 调用减少了高达 30x / 55.5x。仅在线测试开销进一步减少，分别实现了高达 106x / 117x 的 token 减少和 159x / 310x 更少的 API 调用。代码可在该链接中找到。
## 256. `cs.AI` - CLLMRec: LLM-powered Cognitive-Aware Concept Recommendation via Semantic Alignment and Prerequisite Knowledge Distillation [PDF](https://arxiv.org/pdf/2511.17041), [HTML](https://arxiv.org/abs/2511.17041)
### Authors
Xiangrui Xiong,Yichuan Lu,Zifei Pan,Chang Sun
### Background
大规模在线开放课程（MOOCs）的增长对个性化学习提出了重大挑战，其中概念推荐至关重要。现有方法通常依赖于异构信息网络或知识图谱来捕捉概念关系，结合知识追踪模型来评估学习者的认知状态。然而，这些方法因依赖高质量的结构化知识图谱而受到限制，这些高质量的知识图谱在实际教育场景中往往是稀缺的。
### Innovation
本文提出了一种名为CLLMRec的新框架，该框架通过语义对齐和先修知识提炼两种协同技术支柱，利用大型语言模型来解决这一根本挑战。CLLMRec通过构建统一的表示空间，将无结构的文本描述进行编码，并通过教师-学生架构提炼概念先修关系，以训练高效的排名器。
### Conclusion
我们的框架基于这些基础，结合了细粒度的排名机制，明确建模学习者实时的认知状态，确保推荐既符合结构条件又符合认知要求。在两个实际的MOOC数据集上进行的大量实验表明，CLLMRec在多个评估指标中显著优于现有基准方法，验证了其在生成真正具有认知意识和个性化的概念推荐方面的有效性，无需依赖显式的结构先验。
## 257. `cs.AI` - Agent0-VL: 探索具有工具集成视觉语言推理能力的自我进化的智能体 [PDF](https://arxiv.org/pdf/2511.19900), [HTML](https://arxiv.org/abs/2511.19900)
### Authors
Jiaqi Liu,Kaiwen Xiong,Peng Xia,Yiyang Zhou,Haonian Ji,Lu Feng,Siwei Han,Mingyu Ding,Huaxiu Yao
### Background
视觉语言智能体在多种跨模态推理任务中取得了显著进展，但其学习仍然受限于人类标注监督的不足。传统的自奖励方法试图通过让模型充当自批评者或奖励提供者来克服这一限制。然而，基于纯文本的自我评估难以验证复杂的视觉推理步骤，并且经常出现评估幻觉。
### Innovation
受到工具集成推理近来进展的启发，本文提出了一种自我进化的视觉语言智能体Agent0-VL，具备工具集成推理能力。Agent0-VL不仅将工具使用纳入推理，还将其融入自我评估和自我修复，通过基于证据的分析实现自我反省、验证和推理的完善。该模型整合了两种相辅相成的角色：执行多轮次工具集成推理的求解器，以及通过工具导向批评生成结构化反馈和精细自我奖励的验证器。通过自我进化推理循环，工具基础的验证和强化学习共同作用，以实现稳定的自我改进。Agent0-VL 未借助任何外部奖励模型和人类注解，实现了未经外部奖励的自我进化，最终在几何问题解决和视觉科学分析中比基线模型提高了12.5%。
### Conclusion
通过工具集成推理与自我进化推理循环，Agent0-VL 实现了无需任何人类注解和外部奖励模型的持续自我改进。实验结果显示，Agent0-VL 在几何问题解决和视觉科学分析任务上的表现比基线模型有了显著提升。
## 258. `cs.AI` - LLMs for Automated Unit Test Generation and Assessment in Java: The AgoneTest Framework [PDF](https://arxiv.org/pdf/2511.20403), [HTML](https://arxiv.org/abs/2511.20403)
### Authors
Andrea Lops,Fedelucio Narducci,Azzurra Ragone,Michelantonio Trizio,Claudio Bartolini
### Background
单元测试是软件开发中的一个关键但资源密集的过程，确保代码单元正确运行。然而，使用大型语言模型（LLMs）自动生成单元测试在Java中的应用仍然是一个新兴领域。AgoneTest框架为这种应用提供了一个标准化的评估框架，旨在支持研究人员和开发者在真实的条件下比较不同LLMs和提示策略。
### Innovation
AgoneTest框架不试图提出一种新的测试生成算法，而是通过一个标准化的端到端评估管道支持研究人员和开发者比较不同LLMs和提示策略。该框架引入了Classes2Test数据集，将被测试的Java类映射到相应的测试类，并集成先进的评估指标（如变异分数和测试气味），以进行全面评估。实验结果显示，在能编译的测试中，LLM生成的测试可以与甚至超过人工编写的测试在覆盖率和缺陷检测方面。
### Conclusion
AgoneTest澄清了LLMs在软件测试中的潜力，并为未来模型设计、提示工程和测试实践的改进提供了见解。
## 259. `cs.AI` - R3A: 可靠的RTL修复框架结合多智能体故障定位和随机树思维 Patch生成 [PDF](https://arxiv.org/pdf/2511.20090), [HTML](https://arxiv.org/abs/2511.20090)
### Authors
Zizhang Luo,Fan Cui,Kexing Zhou,Runlin Guo,Mile Xia,Hongyuan Hou,Yun Liang
### Background
RTL（寄存器传输级）硬件设计和验证中的错误修复至关重要。传统自动程序修复（APR）方法通过定义特定的搜索空间来定位和修复错误，但这些方法依赖于固定的模板，只能处理有限的错误。大型语言模型（LLM）能够理解代码语义，可作为一种替代方案用于RTL修复，但它们因固有的随机性和长输入代码波形的上下文而导致结果不可靠。为了应对这些挑战，提出了一种名为R3A的基于LLM的自动RTL程序修复框架。
### Innovation
R3A提出了随机树思维方法来控制补丁生成代理，探索验证解决方案，平衡探索与利用以提高可靠性。此外，R3A还提出了一种多代理故障定位方法，用于找到故障候选作为补丁生成代理的起点，从而进一步提高可靠性。实验表明，R3A在给定的时间限制内可以修复RTL修复数据集中90.6%的错误，比传统方法和其他基于LLM的方法覆盖了45%更多的错误，同时实现了86.7%的pass@5率，表现出高可靠性。
### Conclusion
研究提出了一种基于LLM的R3A框架，结合多代理故障定位和随机树思维补丁生成技术，提高了修复可靠性并有效解决了传统的固定模板方法无法处理的更多错误。实验结果证实了该方法的有效性和高可靠性。
## 260. `cs.AI` - BengaliFig: 一种低资源语言中具象和文化背景推理的挑战 [PDF](https://arxiv.org/pdf/2511.20399), [HTML](https://arxiv.org/abs/2511.20399)
### Authors
Abdullah Al Sefat
### Background
大型语言模型在多语言基准测试中表现出色，但在具象和文化扎根的推理方面尤其在低资源环境中仍然缺乏全面评估。特别是对于孟加拉语这种广泛使用的低资源语言，其具象和文化根源的推理能力尚未得到有效测试。
### Innovation
本文提出了一种名为BengaliFig的数据集，该数据集包含435个独特谜语，来源于孟加拉语口语和文学传统。每个谜语从五个维度进行注释，包括推理类型、陷阱类型、文化深度、答案类别以及难度，并通过一种约束意识的、AI辅助的管道自动转换为选择题格式。该数据集用于评估八种主要提供商的前沿LLM在零样本和少样本思维链提示下的表现，揭示了这些模型在具象和文化特定推理方面的持续弱点。
### Conclusion
BengaliFig不仅提供了一种诊断性检查点，用以评估LLM在低资源文化环境中的稳健性，还为包容性和遗产意识的NLP评估铺平了道路。
## 261. `cs.AI` - EmoFeedback$^2$: 通过基于LVLM的奖励和文本反馈增强连续情感图像生成 [PDF](https://arxiv.org/pdf/2511.19982), [HTML](https://arxiv.org/abs/2511.19982)
### Authors
Jingyang Jia,Kai Shu,Gang Yang,Long Xing,Xun Chen,Aiping Liu
### Background
连续情感图像生成（C-EICG）由于其能够生成与用户描述和连续情感值相匹配的图像，正在迅速发展。然而，现有方法在生成图像后缺乏情感反馈，限制了情感连续性的控制。而且，它们简单的情感与文本之间的对齐方式无法根据图像内容自适应调整情感提示，导致情感准确性不足。
### Innovation
本文提出了一个新颖的生成-理解-反馈强化范式（EmoFeedback$^2$），利用微调的大型视觉-语言模型（LVLM）的推理能力，为生成高质量具有连续情感的图像提供奖励和文本反馈。具体来说，引入了情感意识的奖励反馈策略，LVLM评估生成图像的情感值，并与目标情感计算奖励，引导生成模型的强化微调，增强图像的情感连续性。此外，设计了一个自我提升的文本反馈框架，其中LVLM迭代分析生成图像中的情感内容，并自适应地为下一轮提示生成精炼建议，提高情感细节度。
### Conclusion
在我们自定义的数据集上的广泛实验结果表明，我们的方法有效地生成了具有所需情感的高质量图像，优于现有的最先进方法。代码和数据集将很快发布。
## 262. `cs.CL` - MindSET：通过大规模社交媒体数据推进心理健康基准测试 [PDF](https://arxiv.org/pdf/2511.20672), [HTML](https://arxiv.org/abs/2511.20672)
### Authors
Saad Mankarious,Ayah Zirikly,Daniel Wiechmann,Elma Kerz,Edward Kempa,Yu Qiao
### Background
社交媒体数据已成为研究心理健康的重要资源，能够提供有关心理状态、情绪和行为的即时洞察，而这些洞察经常被传统的研究方法所忽视。在这一领域取得进步的部分原因是有了心理健康分析的基准数据集，然而，当前大多数基准数据集已变得过时，原因包括数据可用性有限、数据清理不足以及社交媒体内容多样性（如多语言和有害内容）。
### Innovation
本文介绍了新的基准数据集MindSET，该数据集从Reddit中精心挑选并使用自我报告的诊断信息来解决现有数据集的局限性。MindSET包含超过1300万条标注帖子，涉及七种心理健康状况，其规模是之前基准数据集的两倍以上。此外，MindSET通过严格的预处理步骤确保了数据质量，包括语言过滤、Not Safe For Work（不适合工作环境）和重复内容的删除，并使用LIWC进行语言学分析，以跨八个组群研究心理术语频率。
### Conclusion
基于MindSET的数据集，进行了诊断检测的二分类实验，使用微调的语言模型和BoW特征。在MindSET上训练的模型始终优于在早期基准数据集上训练的模型，例如达到了高达18点的F1得分改善，用于自闭症检测。总体而言，MindSET为探索社交媒体与心理健康交叉研究奠定了坚实基础，支持早期风险检测和新兴心理趋势的深入分析。
## 263. `cs.CL` - ITSM环境中基于重心的文本分类框架 [PDF](https://arxiv.org/pdf/2511.20667), [HTML](https://arxiv.org/abs/2511.20667)
### Authors
Hossein Mohanna,Ali Ait-Bachir
### Background
在IT服务管理（ITSM）系统中，服务工单需要被分类到具有树状结构的分类体系中，文本分类与层级化的分类体系相结合成为一个根本性的需求。
### Innovation
提出了一种双重嵌入重心为基础的分类框架，该框架为每个类别维护独立的语义和词项重心表示，并通过推断时的相互排名融合将它们结合在一起。该框架在性能上与支持向量机（hierarchical F1值：0.731 vs 0.727）相当，同时通过重心表示提供了可解释性。该方法在8,968个ITSM工单（涵盖123个类别）上的训练速度提高了5.9倍，并且增量更新速度提高了152倍，当排除嵌入计算时，在批处理大小100-1000样本之间平均速度提高了8.6-8.8倍。
### Conclusion
这些结果使该方法适用于优先考虑可解释性和运营效率的ITSM环境。
## 264. `cs.CL` - 结构化定义与分割在LLMs法律推理中的研究：基于印度法律数据 [PDF](https://arxiv.org/pdf/2511.20669), [HTML](https://arxiv.org/abs/2511.20669)
### Authors
Mann Khatri,Mirza Yusuf,Rajiv Ratn Shah,Ponnurangam Kumaraguru
### Background
大规模语言模型（LLMs）在广泛网络数据集上训练后，表现出强大的通用推理能力，但在专业领域，如法律领域，表现较差。这主要是因为这些模型缺乏特定的专业预训练。法律文件通常较长且结构复杂，使得模型难以有效处理整个文本。先前的研究已经探讨了上下文方法来弥补知识上的不足，通过部分领域的调整来提升模型在新领域的表现。本文通过三方面的实验分析了模型在法律任务上的行为：(1) 根据修辞角色重组文件以评估结构化信息对处理长文本和模型决策的影响；(2) 定义修辞角色来使模型熟悉法律术语；(3) 模拟法院针对修辞角色的逐步推理来增强模型的推理能力。所有这些实验都是在三个印度法律判决预测数据集上零样本设置下进行的。
### Innovation
本文通过针对法律文本编写时的结构性与逻辑性，探索了在零样本条件下提升LLMs在法律推理中的性能的方法。特别是，通过定义修辞角色来增强模型对专业术语的理解，并且通过模拟法院推理过程来改进模型的推理能力。
### Conclusion
数据重组或解释关键法律术语对提升模型性能有显著影响，与基线相比，最小提升为1.5%，最大提升为4.36%的改进发生在F1分数上。这些结果表明，结构化数据整理和明确的修辞角色定义是提升LLMs在法律推理任务中性能的有效方法。
## 265. `cs.CL` - 信号遇上传统：生成推荐中的双代码本表示学习 [PDF](https://arxiv.org/pdf/2511.20673), [HTML](https://arxiv.org/abs/2511.20673)
### Authors
Zheng Hui,Xiaokai Wei,Reza Shirkavand,Chen Wang,Weizhi Zhang,Alejandro Peláez,Michelle Gong
### Background
生成推荐作为检索和生成的统一范式近年来取得了显著的成功。通过将物品表示为离散语义标记，生成模型可以实现灵活的序列建模。然而，现有的方法依赖单一的代码本编码所有物品，忽视了流行物品与长尾物品之间的固有不平衡。流行物品含有丰富的协作信号，而长尾物品则依赖于语义理解。
### Innovation
FlexCode框架通过引入适应性分配协作过滤（CF）代码本和语义代码本的固定标记预算，解决单一代码本的局面。该框架中的轻量级混合专家（MoE）动态平衡CF精度和语义泛化，同时保持流行度谱的连贯性。通过对公共和工业规模的数据集进行实验，展示了FlexCode在对比强基线模型方面的优越性。
### Conclusion
FlexCode提供了一种新的标记表示机制，在生成推荐中实现了更强的准确性和尾部鲁棒性，提出了在基于标记的推荐模型中平衡记忆和泛化的新视角。
## 266. `cs.CL` - 阿拉伯语上下文相关文本到SQL的提示工程技术 [PDF](https://arxiv.org/pdf/2511.20677), [HTML](https://arxiv.org/abs/2511.20677)
### Authors
Saleh Almohaimeed,May Alsofyani,Saad Almohaimeed,Mansour Al Ghanim,Liqiang Wang
### Background
近年来，跨域、上下文相关的文本到SQL任务受到广泛关注。该任务旨在让没有SQL基础知识的用户能够通过自然语言与数据库进行对话。目前，大部分相关研究和数据集主要集中在英语中，中文也有所涉及，但尚未有人在阿拉伯语中进行此类研究和开发。
### Innovation
本文引入了Ar-SParC数据集，这是首个阿拉伯语跨域、上下文相关的文本到SQL数据集，包含3450组相互关联的问题序列，每个序列平均包含3个问题，共10225个问题及其对应的SQL查询。此外，作者使用两种大型语言模型GPT-3.5-turbo和GPT-4.5-turbo进行了40次实验，应用了10种不同的提示工程技术，包括四种问题表示方法和六种上下文学习技术。进一步开发了名为GAT正确修正器的新方法，此方法在所有40次实验中提升了执行准确度和交互准确度，尤其是在零样本设置中提高了1.9%，在上下文学习设置中分别提高了1.72%和0.92%。
### Conclusion
通过AB测试进一步分析了为什么GAT正确修正器在阿拉伯语上下文环境中比之前的GAT验证技术更加出色，并且详细介绍了实验结果和提出的改进方法的意义。
## 267. `cs.CL` - 由LLMs驱动的2D材料数据的精确提取、查询和智能管理 [PDF](https://arxiv.org/pdf/2511.20691), [HTML](https://arxiv.org/abs/2511.20691)
### Authors
Lijun Shang,Yadong Yu,Wenqiang Kang,Jian Zhou,Dongyue Gao,Pan Xiang,Zhe Liu,Mengyan Dai,Zhonglu Guo,Zhimei Sun
### Background
二维（2D）材料因其独特的物理化学和电子性质，在能源存储和转换方面的应用日益广泛。大多数有关该材料的信息，如其性质和制备方法，都被包含在已发表的研究论文中。然而，由于合成和数据库管理的分散性，这些信息难以整合和查询。
### Innovation
本文提出了一种基于LLMs（大规模语言模型）的技术，用于准确地提取、查询和智能管理与2D材料相关的文献数据。这种方法能够有效整合和处理分散在各种文献中的信息，增强了数据的可访问性和检索效率。
### Conclusion
通过LLMs驱动的数据管理方法，研究成功实现了2D材料数据的高效管理和智能检索。该方法为该领域的研究提供了强有力的支持，有助于加速新型2D材料的应用和发展。
## 268. `cs.CL` - PIRA：面向偏好的指令调整奖励模型与双重聚合 [PDF](https://arxiv.org/pdf/2511.20668), [HTML](https://arxiv.org/abs/2511.20668)
### Authors
Yongfu Xue
### Background
大型语言模型（LLMs）的奖励模型对于使其与人类偏好对齐至关重要，但面临两个主要挑战：传统区分性奖励模型通常直接将问题和响应拼接在一起作为输入，导致数据效率低；且奖励模型容易受到奖励优化过度的影响。
### Innovation
PIRA 提出了一种解决这两个问题的训练范式，通过三种策略：(1) 将问题-答案对重新表述为偏好导向的指令，使任务定义更清晰明确；(2) 从多样化的偏好任务中聚合奖励，减少偏见并提高鲁棒性；(3) 在不同dropout率下平均value-head输出，以稳定奖励。实验结果表明PIRA的有效性。
### Conclusion
PIRA 通过重塑任务定义、减少偏见以及稳定奖励输出，有效解决了现有奖励模型的数据效率低和奖励优化过度的挑战，展现了其在提升LM与人类偏好对齐方面的潜力。
## 269. `cs.CL` - 大型语言模型推理中的认知偏差会损害临床肿瘤学笔记的解读 [PDF](https://arxiv.org/pdf/2511.20680), [HTML](https://arxiv.org/abs/2511.20680)
### Authors
Matthew W. Kenaston(1),Umair Ayub(1),Mihir Parmar(2),Muhammad Umair Anjum(1),Syed Arsalan Ahmed Naqvi(1),Priya Kumar(1),Samarth Rawal(1),Aadel A. Chaudhuri(4),Yousef Zakharia(3),Elizabeth I. Heath(5),Tanios S. Bekaii-Saab(3),Cui Tao(6),Eliezer M. Van Allen(7),Ben Zhou(2),YooJung Choi(2),Chitta Baral(2),Irbaz Bin Riaz(1 and 3 and 6) ((1) Mayo Clinic College of Medicine and Science, Phoenix, AZ, (2) School of Computing and AI, Arizona State University, Tempe, AZ, (3) Mayo Clinic Comprehensive Cancer Center, Phoenix, AZ, (4) Department of Radiation Oncology, Mayo Clinic, Rochester, MN, (5) Department of Oncology, Mayo Clinic, Rochester, MN, (6) Department of Artificial Intelligence and Informatics, Mayo Clinic, Rochester, MN, (7) Dana-Farber Cancer Institute, Harvard Medical School, Boston, MA)
### Background
尽管大型语言模型在临床基准测试中表现出色，但在涉及肿瘤学决策支持领域时，它们可能会通过错误的推理达到正确的结论。这种错误推理模式有潜在的安全问题，但目前依赖准确度评估却没有捕捉到这种问题。
### Innovation
本文通过一个两组回顾性研究，开发了一种分层分类系统，从GPT-4的回答中分析肿瘤学笔记中的推理错误。研究人员使用乳腺癌和胰腺癌数据集的笔记，标注了600条推理痕迹，构建了三级分类系统，将计算错误与认知偏差框架进行匹配。该分类系统在前列腺癌咨询笔迹数据上得到验证，并识别出错误相关且可能有害的建议，特别是对于晚期疾病管理而言。使用最先进的语言模型的自动化评估器只能检测出错误的存在，但无法可靠地分类错误类型。这项工作表明，大型语言模型在推理有误时可能会提供流畅但临床不安全的建议。
### Conclusion
这些发现表明，当推理有误时，大型语言模型可能会给出流畅但临床应用中不安全的建议。分类系统提供了在临床部署前评估和提高推理准确性的通用框架。
## 270. `cs.AI` - TiCT: 一种预先通过合成数据训练的时序分类基础模型 [PDF](https://arxiv.org/pdf/2511.19694), [HTML](https://arxiv.org/abs/2511.19694)
### Authors
Chin-Chia Michael Yeh,Uday Singh Saini,Junpeng Wang,Xin Dai,Xiran Fan,Jiarui Sun,Yujie Fan,Yan Zheng
### Background
时序数据的普遍性推动了对通用基础模型的需求，然而开发适用于分类任务的基础模型依然面临显著挑战，主要原因是标记数据成本高昂。具有上下文学习能力（ICL）的基础模型可以有效应对新任务，减少大量重新训练的需求，但此前大规模时序模型研究主要集中在预测上，缺乏能够通用且无需微调的分类解决方案。
### Innovation
TiCT 作为一种基于Transformer的模型，仅通过合成数据预训练，专门用于执行上下文中的分类任务。TiCT 的两大技术贡献包括：1）一种可扩展的基于位的标签编码及处理任意类别数量的特殊输出注意力机制；2）结合灵感源于Mixup的数据增强过程的合成预训练框架，以促进泛化能力和噪声不变性。
### Conclusion
在UCR档案上的广泛评估显示，TiCT 在上下文推断过程中实现了与当前最先进的监督方法相当的性能。关键在于，这一成就仅使用了上下文中的示例，而未更新任何模型权重。
## 271. `cs.AI` - 基于RAG增强动态提示的大语言模型系统分析在医疗错误检测与修正中的应用 [PDF](https://arxiv.org/pdf/2511.19858), [HTML](https://arxiv.org/abs/2511.19858)
### Authors
Farzad Ahmed,Joniel Augustine Jerome,Meliha Yetisgen,Özlem Uzuner
### Background
临床文档中存在事实性、诊断性和管理性错误，这些错误会影响患者的安全。大语言模型（LLMs）可能有助于检测和更正这些错误，但不同提示策略下的表现尚不清楚。本文通过MEDEC数据集评估了零 shot 提示、静态提示加随机示例（SPR）和检索增强动态提示（RDP）三种策略，在医疗错误处理中的三个子任务上的表现。
### Innovation
研究对比了三种不同的提示策略：零 shot 提示、静态提示加随机示例（SPR）和检索增强动态提示（RDP），评估它们在医疗错误处理任务上的表现。其中，检索增强动态提示在降低假阳性率、提升召回率和生成更具上下文准确性的修正方面表现突出，特别是在不同大语言模型中。
### Conclusion
检索增强动态提示（RDP）在所有不同大语言模型中均优于零 shot 和静态提示。使用检索的示例可以提高检测准确性，减少假阳性，并提升医疗错误修正的可靠性。
## 272. `cs.AI` - TREASURE: 基于Transformer的基础模型以理解高交易量数据 [PDF](https://arxiv.org/pdf/2511.19693), [HTML](https://arxiv.org/abs/2511.19693)
### Authors
Chin-Chia Michael Yeh,Uday Singh Saini,Xin Dai,Xiran Fan,Shubham Jain,Yujie Fan,Jiarui Sun,Junpeng Wang,Menghai Pan,Yingtong Dou,Yuzhong Chen,Vineeth Rakesh,Liang Wang,Yan Zheng,Mahashweta Das
### Background
支付网络构成了现代商业的骨干，每天产生大量交易记录。正确地建模这些数据可以为异常行为检测和用户级见解（如高度个性化体验）提供支持，最终改善人们的生活。因此，正确建模是必不可少的，以提升推荐系统的准确性以及异常行为检测的性能。
### Innovation
TREASURE 是一种基于 Transformer 的基础模型，专为交易数据设计。该模型同时捕捉消费者行为和支付网络信号（如响应码和系统标志），提供了全面的信息，适用于准确的推荐系统和异常行为检测。TREASURE 具有以下关键特性：1）具有针对静态和动态属性的专用子模块的输入模块，实现了更加高效的训练和推断；2）高效的高基数类别属性预测训练范式；3）作为独立模型提高了异常行为检测性能（在生产系统上提高了111%），作为嵌入提供者增强了推荐模型的性能（提高了104%）。
### Conclusion
通过对广泛的消融研究、与生产模型的基准测试和案例研究，深入了解了开发 TREASURE 的重要成果。
## 273. `cs.AI` - 人类专家对生成型AI在全球南方开展STEAM教育情境化的评估 [PDF](https://arxiv.org/pdf/2511.19482), [HTML](https://arxiv.org/abs/2511.19482)
### Authors
Matthew Nyaaba,Macharious Nabang,Patrick Kyeremeh,Ibrahim Nantomah,Collins Owusu-Fordjour,Martin Ako,Bismark Nyaaba Akanzire,Kassim Korah Nantomah,Cecilia Issaka,Xiaoming Zhai
### Background
本研究探讨了人类专家如何评估生成型人工智能（GenAI）在全球南方（以加纳为例）情境化STEAM教育的能力。研究采用了混合方法研究设计，四个STEAM专家评估了GenAI生成的、基于定制文化响应教学计划器（CRLP）的教案，并将其与加纳国家课程与评估委员会（NaCCA）的标准化教学计划进行了比较。
### Innovation
研究创新在于使用了文化响应型教学评价量表，从文化敏感性、文化表现、情境相关性、语言响应性和教师自主性五个方面对GenAI生成的教案进行定量评价，并通过定性反思深入了解GenAI在文化适宜性和教育响应性方面的处理方式。研究还指出，要在全球南方的情境下提高AI文化忠实度，需要继续教师调解、社区参与和AI输出的文化调整。
### Conclusion
研究表明，当与CRLP工具结合使用时，GenAI可以支持情境化的STEAM教学，通过将抽象的课程标准与学习者的文化知识、社区实践和日常经验相联系。GenAI辅助教案在文化根基和教育响应性方面得到了专家更高的评价，但也表现出对加纳文化多样性的表面化处理，尤其是数学和计算领域文化细微差的限制。未来的研究应包括课堂教学实验、扩大专家参与范围以及使用本地语言语料库微调模型，以加强全球南方的文化忠实度。
## 274. `cs.CL` - 实现LLM效率的民主化：从超大规模优化到通用部署 [PDF](https://arxiv.org/pdf/2511.20662), [HTML](https://arxiv.org/abs/2511.20662)
### Authors
Hen-Hsen Huang
### Background
大规模语言模型（LLMs）已成为不可或缺的技术，但目前最著名的高效方法（如混合专家模型（MoE）、推测解码和复杂的检索增强生成（RAG））主要是为拥有雄厚基础设施和精英团队的超大规模提供商设计的。这些方法在其他情境下则可能会成为负担、脆弱性以及碳足迹的浪费。结果是，少数几家大型科技公司从中受益，而数千家医院、学校、政府机构和企业则缺乏可行的选择。
### Innovation
我们建议下一阶段的研究重点不应是更大规模的复杂化，而是稳健的简洁性：在有限资源和基础薄弱的背景下实现更好的效率。提出了一个新研究议程，包括改造预训练模型以使用更高效的架构、发明保持对齐的小型微调方法、即使面对长链条思考也要使推理变得经济，实现动态知识管理而不依赖于重大的RAG管道，以及采用“开销感知效率”（OAE）作为标准基准。通过将效率的定义扩展到包括采用成本、可持续性和公平性，我们希望能够实现LLM部署的民主化，确保优化能够减少而不是放大不平等和碳浪费。
### Conclusion
通过重新定义效率包括采用成本、可持续性和公平性，我们可以实现LLM部署的民主化，确保优化能够减少而不是放大不平等和碳浪费。
## 275. `cs.CL` - 谐波词投影（HTP）：一种词汇无关、无需训练的确定性和可逆嵌入方法 [PDF](https://arxiv.org/pdf/2511.20665), [HTML](https://arxiv.org/abs/2511.20665)
### Authors
Tcharlies Schmitz
### Background
现有神经嵌入方法依赖统计共现或优化，需要训练过程和随机参数，在嵌入生成过程中缺乏确定性和可逆性。因此，研究者寻找一种新的方法，能够在无需训练、无需词汇表和随机参数的情况下生成可逆且确定性的文本嵌入。
### Innovation
该研究提出了谐波词投影（HTP），这是一种基于确定性和可逆性的文本嵌入生成框架。它通过解析Unicode整数表示生成每个词的谐波轨迹，建立了离散符号与连续向量空间之间的双射和可解释映射。HTP提供相位一致的投影，能够保持结构和可逆性，从而纯粹通过几何对齐估计语义相似度。与神经嵌入方法不同，HTP提供了透明且高效的语义相似度估计，特别适用于多语言场景。
### Conclusion
实验结果显示，HTP在英语语料上的Spearman相关系数达到了0.68，其在多种语言上的表现也十分稳定。尽管计算成本低，处理每个句子对的延迟仅在亚毫秒级，但依然能够维持较高的语义相似度估计能力。这证明了有意义的语义关系可以从确定性几何中产生，为基于数据驱动的嵌入提供了一个透明和高效的选择。
## 276. `cs.CL` - 多路径检索的记忆：大规模语言模型训练数据泄露的鲁棒检测的多前缀框架 [PDF](https://arxiv.org/pdf/2511.20799), [HTML](https://arxiv.org/abs/2511.20799)
### Authors
Trung Cuong Dang,David Mohaisen
### Background
大型语言模型在大量语料库上进行训练，容易出现精确复述训练数据的情况，这带来了严重的隐私和版权风险。尽管之前的研究提出了各种关于复述的定义，但这些定义在充分捕捉这一现象方面存在不足，特别是在对齐模型中。
### Innovation
本文提出了一种新的框架：多前缀复述。核心思想是记忆中的序列被深度编码，因此可以通过远多于非记忆内容的不同前缀检索到。这一框架将注意力从单一路径提取转移到量化的记忆稳健性，即其检索路径的多样性。通过开源和对齐聊天模型的实验，证明了我们的多前缀定义可以可靠地区分记忆数据和非记忆数据，提供了一种强大的工具来审计大规模语言模型中的数据泄露。
### Conclusion
本文提出的多前缀定义可以通过实验可靠地区分记忆数据和非记忆数据，为审计大规模语言模型中的数据泄露提供了强大而实用的工具。
## 277. `cs.CL` - 结构化提示使语言模型评估更加稳健、综合 [PDF](https://arxiv.org/pdf/2511.20836), [HTML](https://arxiv.org/abs/2511.20836)
### Authors
Asad Aali,Muhammad Ahmed Mohsin,Vasiliki Bikia,Arnav Singhvi,Richard Gaus,Suhana Bedi,Hejie Cui,Miguel Fuentes,Alyssa Unell,Yifan Mai,Jordan Cahoon,Michael Pfeffer,Roxana Daneshjou,Sanmi Koyejo,Emily Alsentzer,Percy Liang,Christopher Potts,Nigam H. Shah,Akshay S. Chaudhari
### Background
随着语言模型（LMs）在各个领域的应用日益广泛，能够准确评估性能的高质量基准测试框架变得至关重要，以指导部署决策。现有的评估框架，如Holistic Evaluation of Language Models（HELM），虽然能够进行广泛的多任务评估，但也依赖于固定的提示，这导致其在不同语言模型之间的性能评估不具有代表性。为了提高性能评估的准确性，Declarative Prompting Frameworks（如DSPy）通过结构化提示提供了可扩展的提示优化方法，但这些框架尚未在已建立的基准测试中进行系统的评估。
### Innovation
本文提出了一个可复现的DSPy+HELM框架，通过引入结构化提示方法，使LM能够展示出合理的推理，从而实现更加准确的基准测试。该研究使用四种结构化提示方法，在四个前沿语言模型上，对七个基准（通用/医学领域）进行了评估，对比了现有的HELM基线得分。结果表明，传统的基准测试方法下：(i) HELM低估了LM的性能（平均低估4%），(ii) 性能估计在不同基准上的差异更大（标准差增加2%），(iii) 性能差距被错误地表示（在7个基准中的3个上排名翻转），(iv) 引入推理（链式思考）减少了LM对提示设计的敏感性（不同提示之间的差异变小）。这是一项首次系统评估多任务基准和提示方法的大型基准测试研究，表明可扩展的性能天花板估计能够提供更有决策价值的基准测试。
### Conclusion
通过对比传统和结构化提示方法的评估结果，本文证明了可扩展性性能天花板估计能提供更有决策价值的基准测试。研究结果表明，基于结构化提示的基准测试可以使LM评估更加稳健和综合。
## 278. `cs.CL` - TrackList: 回溯查询语言多样性以追踪头部和尾部知识在开放大语言模型中的表现 [PDF](https://arxiv.org/pdf/2511.21006), [HTML](https://arxiv.org/abs/2511.21006)
### Authors
Ioana Buhnila,Aman Sinha,Mathieu Constant
### Background
大语言模型（LLMs）在回答用户输入查询的定义类问题方面表现出高效性。然而，对于人类可以轻松回答的各种类型的问题，如示例和释义，LLMs 在回答非定义类的查询时表现出色度下降。本文通过 TrackList，一个精细的语言和统计分析流程，评估预训练数据对 LLMS 回答多样化语言查询的影响。此外，文章还介绍了 RefoMed-EN 语言数据集，包含 6170 个由人类标注的医学术语及其定义、代称、示例、解释或释义，以研究概念出现频次对其影响。
### Innovation
通过 TrackList 流程计算预训练数据对 LLMs 答题质量的多样性影响；开发 RefoMed-EN 语言数据集以进行多样查询的研究；揭示大语言模型在进行定义类问题较好但在进行示例类问题最差；展示大语言模型更倾向于循环使用流行和频繁的知识而非罕见和专业技术知识。
### Conclusion
定义类问题中大语言模型的执行表现最高，而示例类问题最低。同时，对于定义类问题，大语言模型在处理流行和频繁的知识时表现出更多释义，但在处理尾部和专业技术知识时则较少，尤其是专家文本中。
## 279. `cs.CL` - 基于MLP和变换器方法的动态模板选择以优化输出代码生成： [PDF](https://arxiv.org/pdf/2511.20683), [HTML](https://arxiv.org/abs/2511.20683)
### Authors
Bharadwaj Yadavalli
### Background
当前大型语言模型部署通常采用统一的提示策略，对不同类型的查询都应用冗长的响应模式，这种一刀切的方法导致了显著的令牌效率低下，尤其是在输入和输出令牌的成本差异大且输出令牌的价格比输入令牌高4-8倍的情况下。这一问题在多个主要供应商间普遍存在。
### Innovation
提出了动态模板选择（DTS）方法，该方法能够根据查询复杂性自适应地匹配响应模板，从而在不牺牲响应质量的情况下显著降低成本。研究比较了两种路由方法：一种简单的MLP模型和一个更复杂的微调RoBERTa变换器。研究发现，尽管MLP模型参数少1.25亿，但在1000个MMLU问题上的路由准确率达到90.5%，仅略低于RoBERTa模型的89.5%。此外，实验证明模板选择的提供者无关性，在三个主要的大语言模型提供商（OpenAI GPT-4、Google Gemini和Anthropic Claude）中表现一致，通过9000次生产API调用验证。
### Conclusion
这项工作贡献了四个关键部分：形式化的问题表述，有理论基础的机器学习背景，四个相应的复杂性分析算法，并且在生产系统中进行了广泛的实证验证。
## 280. `cs.CL` - Chatty-KG：一种用于知识图谱即时对话式问答的多代理AI系统 [PDF](https://arxiv.org/pdf/2511.20940), [HTML](https://arxiv.org/abs/2511.20940)
### Authors
Reham Omar,Abdelghny Orogat,Ibrahim Abdelaziz,Omij Mangukiya,Panos Kalnis,Essam Mansour
### Background
知识图谱（KGs）在企业和特定领域应用中被广泛用来提供结构化、动态和可靠的知识。大型语言模型（LLMs）能够进行自然和上下文相关的对话，但缺乏对私有和动态KG的直接访问。检索增强生成（RAG）系统虽然可以检索图内容，但常常会序列化结构、难以处理多轮对话内容，并需要大量索引。传统的知识图谱问答（KGQA）系统能够保持结构，但通常仅支持单轮问答，滞后较高，并且难以处理指代消解和上下文跟踪。
### Innovation
Chatty-KG提出了一种模块化的多代理系统，用于知识图谱上的对话式问答。该系统结合了RAG风格的检索和结构化执行方式，通过特定任务的LLM代理生成SPARQL查询。这些代理进行协作，用于上下文解释、对话跟踪、实体和关系链接以及高效的查询规划，从而能够将自然问题准确并快速地转换为可执行查询。实验表明，与最先进的基线相比，Chatty-KG在单轮和多轮设置中均取得了显著的性能提升，获得了更高的F1和P@1分数。其模块化设计维护了对话的连贯性，并支持知识图谱的演进无需微调或预处理。商业和开源的大型语言模型评估证实了该系统的广泛兼容性和稳定性能。
### Conclusion
总体而言，Chatty-KG将对话灵活性与结构化的知识图谱接地统一起来，提供了一种可扩展且可扩展的可靠多轮KGQA方法。
## 281. `cs.CL` - LLMs中语义角色电路的涌现及其定位 [PDF](https://arxiv.org/pdf/2511.20910), [HTML](https://arxiv.org/abs/2511.20910)
### Authors
Nura Aljaafari,Danilo S. Carvalho,André Freitas
### Background
尽管大语言模型在展示语义能力方面表现出色，其内在机制如何将抽象语义结构进行定位仍不够充分。已有研究尚未详细解析大语言模型内部是通过何种方式实现语义角色的。
### Innovation
本文提出了一个结合角色交叉最小配对、时间出现分析以及跨模型比较的方法，用于研究大语言模型如何实施语义角色。研究发现大语言模型的语义角色电路高度集中、结构逐渐精炼而无明显瞬态跃变，且在不同规模和架构之间部分保持稳定性。
### Conclusion
本研究揭示，大语言模型形成紧凑的、因果隔离的机制来处理抽象语义结构，这些机制在不同规模和架构之间部分转移到达一定程度的保守性。
## 282. `cs.CL` - 在上下文学习中语义锚点：小型LLM无法翻转标签的原因 [PDF](https://arxiv.org/pdf/2511.21038), [HTML](https://arxiv.org/abs/2511.21038)
### Authors
Anantha Padmanaban Krishna Kumar(Boston University)
### Background
本文探讨了上下文学习（ICL）是否能够覆盖预训练的标签语义，或是仅仅对现有的语义基础进行微调。研究通过对大型语言模型（LLMs）进行提示引导分类，并比较它们在自然演示（有正确标签）和倒置演示（系统性翻转标签意义）下的行为来回答这个问题。
### Innovation
研究通过分解ICL行为为真实度、先验度和提示度对的三个对齐度量标准，并引入语义翻转率（定义为在翻转语义下的正确性），并提出了小型LLM无法翻转标签的原因。
### Conclusion
在自然演示下，ICL能够提高准确率并保持强先验对齐度；大多数正确预测与零样本行为一致，即使先验较弱。在倒置演示下，模型无法学习一致的反语义分类器：提示对齐度只能通过牺牲准确度来增加，我们的少量演示1-12B设置中语义翻转率仍然保持为零。ICL主要通过调整输入如何投影到预训练期间学习到的稳定语义方向来微调模型，揭示了少量提示的内在局限，并表明在这些规模下覆盖标签语义需要超出ICL的干预措施。所有代码可在以下链接获取：this https URL。
## 283. `cs.CL` - 以少胜多：面向低资源语言的英波论证 mined 模型跨语言优势 [PDF](https://arxiv.org/pdf/2511.20872), [HTML](https://arxiv.org/abs/2511.20872)
### Authors
Ali Jahan,Masood Ghayoomi,Annette Hautli-Janisz
### Background
背景：论证挖掘是自然语言处理的一个子领域，旨在识别和提取文本内部的论证成分，如前提和结论，并识别它们之间的关系。它揭示了文本的逻辑结构，有助于知识提取任务。本文关注于利用跨语言方法对低资源语言进行论证挖掘，通过构建三种训练场景进行实验。分别评估了英语（高资源语言）和波斯语（低资源语言）的数据。
### Innovation
创新：文章提出的创新点在于对比了三种不同的模型学习场景，包括零样本迁移、利用大规模语言模型增强英语训练数据、以及结合双语训练策略。特别地，双语训练策略在波斯语测试集上的表现优于其他模型。
### Conclusion
结论：结果表明，一种轻量级的跨语言模型可以显著优于数据增强流水线，并为低资源语言的论证挖掘提供了一种实用的途径，以克服数据资源不足的问题。
## 284. `cs.CL` - 基于上下文感知的实用元认知提示法在讽刺检测中的应用 [PDF](https://arxiv.org/pdf/2511.21066), [HTML](https://arxiv.org/abs/2511.21066)
### Authors
Michael Iskandardinata,William Christian,Derwin Suhartono
### Background
尽管神经网络方法的最新进展，讽刺检测仍然是自然语言处理（NLP）领域的挑战性任务。目前，预训练语言模型（PLMs）和大规模语言模型（LLMs）是检测讽刺的首选方法。然而，讽刺文本的复杂性以及跨文化社区的语境和语言多样性使得即使对于PLMs和LLMs来说，任务也变得更加困难。此外，这些模型在检测需要额外语境分析的单词或标记时也不可靠。
### Innovation
研究提出了基于实用元认知提示法（PMP）的上下文感知方法。该方法通过两种互补方式提供上下文信息：使用基于网络的信息检索来补充模型缺失的背景知识；以及促使模型利用自身的内部知识来增强自我知识觉醒。该方法在Twitter印尼讽刺数据集、SemEval-2018任务3和MUStARD三个数据集上进行了评估，结果显示非参数检索能显著提高Twitter印尼讽刺数据集上的宏观F1分数，同时自我知识检索在Semeval和MUStARD上也有明显改进。
### Conclusion
研究表明，上下文和文化特定短语、参考或对LLMs未知的术语，在提升LLMs在讽刺检测任务上的表现中至关重要。未来工作将集中在优化相关信息的检索，并研究检索质量对性能的影响。
## 285. `cs.CL` - SAGE: 一种用于语言模型中解释SAE特征的代理解释框架 [PDF](https://arxiv.org/pdf/2511.20820), [HTML](https://arxiv.org/abs/2511.20820)
### Authors
Jiaojiao Han,Wujiang Xu,Mingyu Jin,Mengnan Du
### Background
大规模语言模型（LLMs）已经取得了显著的进步，但它们的内部机制仍然很大程度上是不透明的，这给它们的安全和可靠部署带来了重大挑战。稀疏自编码器（SAEs）作为一种有前景的工具，可以将LLMs的表示分解为更可解释的特征，但解释由SAEs捕获的这些特征仍然是一项艰巨的任务。
### Innovation
本文提出了SAGE（SAE AGentic Explainer），这是一种基于代理的框架，将特征解释从一种被动的一次生成任务重新构想为一种积极的、以解释为导向的过程。SAGE通过系统地为每个特征制定多个解释，设计有针对性的实验来测试这些解释，并根据经验激活反馈迭代优化解释，从而实现了一种严谨的方法。通过针对不同语言模型的SAE特征进行的实验表明，与最先进的基线相比，SAGE生成的解释具有更高的生成和预测准确性。
### Conclusion
实验结果表明，SAGE在生成和预测方面产生了显著更准确的解释，与最先进的基线相比。这证明了SAGE作为一种能够解释SAE特征的代理解释框架的有效性和优越性。
## 286. `cs.CL` - 自我引导的防御：通过合成指南的推理模型自适应安全性对齐 [PDF](https://arxiv.org/pdf/2511.21214), [HTML](https://arxiv.org/abs/2511.21214)
### Authors
Yuhang Wang,Yanxu Zhu,Dongyuan Lu,Jitao Sang
### Background
推理模型在复杂推理任务中显示出惊人的能力，然而，确保这些模型在对抗性诈骗提示下依然安全依然是一个严峻的挑战。由于欺骗性提示的隐蔽和难以察觉的特性，它们往往能够逃避内置的安全机制，并导致负面内容的生成。
### Innovation
提出了合成指南基础上的自适应安全性对齐（SGASA）框架。该框架将模型自动生成的安全指南内化，以增强模型对于有害对抗性提示的鲁棒性，同时尽量减少对良性请求的不必要的拒绝。SGASA框架包括数据预合成阶段和对齐微调阶段，后者通过监督微调（SFT）和直接偏好优化（DPO）来嵌入这些指南。
### Conclusion
跨多个数据集的广泛实验表明，SGASA显著提高了模型的安全性，验证了其自适应和可扩展的有效性。
## 287. `cs.CL` - Evo-Memory: 基于自我演化的内存测试时学习评估大语言模型代理 [PDF](https://arxiv.org/pdf/2511.20857), [HTML](https://arxiv.org/abs/2511.20857)
### Authors
Tianxin Wei,Noveen Sachdeva,Benjamin Coleman,Zhankui He,Yuanchen Bei,Xuying Ning,Mengting Ai,Yunzhe Li,Jingrui He,Ed H. Chi,Chi Wang,Shuo Chen,Fernando Pereira,Wang-Cheng Kang,Derek Zhiyuan Cheng
### Background
大语言模型（LLM）代理需要状态信息来进行长期规划和问题解决，因此内存管理成为关键问题，但现有研究较少关注。现有研究主要侧重于静态对话环境中的记忆存储和检索，忽略了内存的动态积累和重用能力。在现实环境中，如交互式问题助手或具身代理，LLMs 需要处理连续的任务流并从累积的互动中学习，这显得尤为不足。为此，论文指出需要在部署过程中进行测试时间进化，即LLMs在每次互动后应能够检索、整合和更新内存。
### Innovation
论文提出Evo-Memory基准和框架，用于评估LLM代理的自我进化内存。Evo-Memory将数据集组织成序列的任务流，促使LLMs在每次交互后搜索、适应和进化内存。文中统合并实现了超过十个代表性的内存模块，并在十个不同的多轮目标导向和单轮推理及问答数据集上进行评估。为更好地测试经验重用，论文还提出了基准方法ExpRAG用于检索和利用先前的经验，并进一步提出了一种集成推理、任务操作和内存更新的行动思考记忆细化管道ReMem，以实现连续改进。
### Conclusion
Evo-Memory通过提供一个结构化的方法来评估LLM代理的自我进化内存，展示了在不断变化的任务情境中的适应性和记忆更新能力。通过ReMem这样的设计理念，论文强调了持续改进和经验重用的重要性，为开发更强大的LLM代理提供了新的视角。
## 288. `cs.CL` - MortgageLLM: 基于残留指令传递、对齐调整和任务特定路由的领域适应预训练 [PDF](https://arxiv.org/pdf/2511.21101), [HTML](https://arxiv.org/abs/2511.21101)
### Authors
Manish Jain,Satheesh Kumar Ponnambalam,Salman Faroz,Chandrakanth Lns,Vinay Sharma
### Background
大型语言模型（LLMs）在通用领域表现出色，但在应用于特定领域如抵押贷款金融时，需要增加特定领域的知识，并保持指令遵循的一致性。然而，单一模型在同一时间优化多种任务往往会牺牲部分性能。
### Innovation
该研究提出了一种名为MortgageLLM的新颖领域特定大语言模型，通过双轨专业化框架从单一基础模型（LLaMA-3.1-8B）开发。该研究贡献了（1）该残留技术在高度专业化抵押贷款金融领域中的应用；（2）结合会话问答模型和结构任务模型的双专家架构；（3）使用少量分类由一个专家模型自身实现的智能任务路由机制。
### Conclusion
该模型在特定领域基准测试中表现出色，与基础模型LLaMA-3.1-8B-Instruct相比，在LLM作为裁判的总结分数、问答分数和分类分数上分别提高了4.58 vs 3.99、4.09 vs 4.0、2.6 vs 1.2。在语义相似性评估中，总结、问答和分类的BERTScore分别达到了0.77、0.68、0.75，显著优于基线方法。
## 289. `cs.CL` - 为伊桑语开发开放式对话语音语料库 [PDF](https://arxiv.org/pdf/2511.21229), [HTML](https://arxiv.org/abs/2511.21229)
### Authors
Adisai Na-Thalang,Chanakan Wittayasakpan,Kritsadha Phatcharoen,Supakit Buakaw
### Background
该论文介绍了一个新的开放性对话语音数据集的发展，专门为伊桑语言设计。伊桑是泰国最广泛使用的区域性方言。现有的语音语料库主要基于朗读或脚本化语音，而该数据集包含自然语言，能够捕捉到诸如口头语、自发停顿、口误和与标准泰语频繁切换等真实的语言现象。然而，由于伊桑在音调上与泰语的不同，当前写作实践存在显著差异，这使得标准化拼写准则的建立变得复杂，从而影响了数据准确性和计算处理的一致性。
### Innovation
构建这个资源的一个关键挑战是伊桑缺乏标准化拼写规则。为了解决这个问题，论文提出了实用的转录协议，平衡了代表性准确性与计算处理需求。此外，该数据集被公开发布，希望能够推动包容性人工智能的发展，支持对未充分研究的语言的研究，并为建立对话语音模型的语音和技术和语言挑战提供基础。
### Conclusion
通过发布这一数据集，论文旨在促进包容性AI的发展，支持对未充分研究的语言的研究，并解决建模对话语音所固有的语言和技术挑战。
## 290. `cs.CL` - PEFT-Bench：参数高效微调方法基准 [PDF](https://arxiv.org/pdf/2511.21285), [HTML](https://arxiv.org/abs/2511.21285)
### Authors
Robert Belanec,Branislav Pecher,Ivan Srba,Maria Bielikova
### Background
尽管大规模语言模型（LLMs）在多项任务上表现出色，但其庞大的规模也导致了计算和环境成本的增加，限制了它们的可访问性。参数高效微调（PEFT）方法通过减少可训练参数数量，同时维持强大的下游性能，解决了这一问题。然而，目前的PEFT方法评估依然有限且难以复现。
### Innovation
为了弥合这一差距，该研究引入了PEFT-Bench，一个统一的端到端基准，用于评估各种PEFT方法在自回归LLMs上的表现。该基准涵盖了27个NLP数据集和6种PEFT方法。此外，研究还引入了PEFT Soft Score Penalties (PSCP)指标，该指标考虑了可训练参数、推理速度和训练内存使用等因素。
### Conclusion
PEFT-Bench提供了一个全面评估PEFT方法的平台，有助于促进该领域的发展和方法的改进。
## 291. `cs.CL` - Length-MAX Tokenizer for Language Models [PDF](https://arxiv.org/pdf/2511.20849), [HTML](https://arxiv.org/abs/2511.20849)
### Authors
Dong Dong,Weijie Su
### Background
介绍了针对语言模型的新分词器，该分词器通过最小化每字符的平均token数量，减少训练和推理过程中所需的token数量。这种方法适用于多种语言场景。
### Innovation
提出了Length-MAX分词器，通过将长度加权目标最大化转化为图分区问题，并使用贪婪近似算法获得词汇表。相较于字节对编码（BPE），在词汇表从10K到50K的范围内，Length-MAX分词器在FineWeb和多样化的数据集上平均能减少14-18%的token数量。当词汇表大小为64K时，减少幅度达到13.0%。在GPT-2模型的训练过程中，使用该分词器可以减少18.5%、17.2%和18.5%的训练步骤，同时降低13.7%、12.7%和13.7%的推理延迟，且在124M参数的模型上获得16%的吞吐量提升。
### Conclusion
Length-MAX分词器不仅优化了平均token长度，还提高了下游任务的性能，如减少LAMBADA困惑度11.7%，提升HellaSwag准确性4.3%。该分词器覆盖率高，词汇表覆盖率达到了99.62%，并且在外推词汇上保持低失误率（0.12%）。这些结果表明，与仅优化token频率相比，优化平均token长度不仅提高了效率，还不会牺牲甚至改善了下游性能。此外，该分词器还与生产环境兼容，降低了推理过程中嵌入和KV缓存的内存使用，减少18%。
## 292. `cs.CL` - 使用Kolmogorov-Arnold网络头部微调提升缅甸新闻分类 [PDF](https://arxiv.org/pdf/2511.21081), [HTML](https://arxiv.org/abs/2511.21081)
### Authors
Thura Aung,Eaint Kay Khaing Kyaw,Ye Kyaw Thu,Thazin Myint Oo,Thepchai Supnithi
### Background
对于资源稀缺的语言如缅甸语，在分类任务中通常只微调最终的分类层，而保持预训练编码器的权重不变。虽然多层感知机（MLPs）是常用的方法，但它们固定的非线性可能会限制表达能力，并增加计算成本。
### Innovation
本文探索了Kolmogorov-Arnold网络（KANs）作为替代的分类头部，评估了基于傅里叶变换的FourierKAN、基于样条曲线的EfficientKAN和基于网格的FasterKAN，并在不同的嵌入包括TF-IDF、fastText和多语言变压器（mBERT、Distil-mBERT）中进行比较。实验结果表明，基于KAN的头部在大多数情况下与MLPs相当或更优。EfficientKAN与fastText嵌入结合使用时获得了最高的F1分数（0.928），而FasterKAN在速度和准确率之间提供了最佳权衡。
### Conclusion
研究结果强调了KANs作为MLPs表达能力强、计算效率高的一种替代选择，适用于资源稀缺语言的分类任务。
## 293. `cs.CL` - 训练内省行为：微调引发大规模模型可靠的内部状态检测 [PDF](https://arxiv.org/pdf/2511.21399), [HTML](https://arxiv.org/abs/2511.21399)
### Authors
Joshua Fonseca Rivera
### Background
琳赛（2025）通过四个实验研究语言模型的内省意识，发现模型有时能检测并识别注入的激活模式，但成功率较低（最佳模型成功率约20%）。这项研究专注于其中的第一个实验——自我报告注入的“想法”，并探讨是否可以通过直接训练而非等待自然出现的方式提升这项能力。
### Innovation
本文通过针对瞬时单词注入进行微调，将一个7B参数模型的准确率从不足1%提升到85%，并在验证集上实现了0%的误报率。模型能够在后续生成步骤中报告注入的“想法”内容，满足内省行为的三个标准：准确性、锚定性和内省性。此外，该模型在未见过的概念向量上也表现出泛化能力，虽然在某种程度上未能证明内省认知表征的存在。
### Conclusion
这些结果回应了琳赛提出的开放问题：是否可以通过训练来减少不同模型之间的差异。研究显示，至少可以诱导某些内省行为的组成部分，为进一步构建自带透明性的AI提供了途径。
## 294. `cs.CL` - 在小规模人类样本上微调LLM能否增加异质性、一致性和信念行为一致性？ [PDF](https://arxiv.org/pdf/2511.21218), [HTML](https://arxiv.org/abs/2511.21218)
### Authors
Steven Wang,Kyle Hunt,Shaojie Tang,Kenneth Joseph
### Background
关于大型语言模型（LLMs）是否可以替代人类参与者进行调查和实验研究，存在争议。虽然营销和心理学等领域的研究探讨了基于LLM的模拟潜力，但越来越多的证据表明，LLMs往往无法与真实的人类行为一致，表现出有限的多样性、小众群体的系统性偏差、内部组间差异不足以及言行不一等问题。
### Innovation
本研究通过一个关于信息披露的行为实验，比较了基于小规模人类样本微调后的LLM响应与人类响应在多个维度上的表现，包括分布差异、亚群体一致性、信念与行为一致性和回归系数恢复，发现微调显著提高了异质性、一致性以及信念行为一致性与基线模型相比的表现。尽管如此，即使是最优的微调模型也无法复制原始研究的回归系数，这表明LLM生成的数据仍不适合用于正式的推断分析。
### Conclusion
微调LLM在小规模人类样本上可以显著提高异质性、一致性和信念行为一致性，但LLM生成的数据在回归分析中仍不适用于替代人类参与者开展正式研究。
## 295. `cs.CL` - 大型语言模型中模型融合技术的系统研究 [PDF](https://arxiv.org/pdf/2511.21437), [HTML](https://arxiv.org/abs/2511.21437)
### Authors
Oğuz Kağan Hitit,Leander Girrbach,Zeynep Akata
### Background
模型合并是一种将多个微调检查点合并成单一模型的技术，无需额外训练，能够有效复用模型且提高性能。然而，这种技术对中小型模型和分类器的优势是否适用于大规模语言模型（LLMs）仍不清楚。因此，有必要对多种模型合并方法在现代LLMs中的效果进行系统性评估。
### Innovation
本研究首次大规模、系统性地评估了六种最先进的模型合并方法，包括最新的子空间方法，跨越四种开放权重LLMs及其相应的十二种微调检查点，以及十六个标准LLMs基准测试。研究通过标准化基准测试，测量合并模型优于基模型的概率和相对收益。实验结果揭示了当前合并技术并不直接适用于现代LLMs，最古老且简单的任务算术方法是唯一能够可靠地在LLMs上产生性能提升的方法。
### Conclusion
最新的合并技术通常会导致性能下降，这表明现有的合并技术并不适合现代LLMs。因此，有必要设计针对LLMs的专用合并算法和合并意识微调方法。
## 296. `cs.CL` - 使用声学特征增强变换器进行低资源密支那自动发音错误纠正 [PDF](https://arxiv.org/pdf/2511.21088), [HTML](https://arxiv.org/abs/2511.21088)
### Authors
Ye Bhone Lin,Thura Aung,Ye Kyaw Thu,Thazin Myint Oo
### Background
本研究探讨了在低资源密支那场景下使用序列到序列变换器模型进行自动语音识别（ASR）错误纠正，特别关注不同的特征融合策略，包括音标（IPA）和对齐信息。据我们所知，这是首次专门针对密支那的ASR错误纠正研究。
### Innovation
研究评估了五种不同的ASR主干模型，并展示了ASR错误纠正（AEC）方法在单词级和字符级准确度上始终优于基线输出。提出的结合了音标和对齐特征的AEC模型，在增广前将ASR模型的平均词错误率（WER）从51.56减少到39.82，增广后从51.56减少到43.59，同时chrF++分数从0.5864增加到0.627，表明在整个过程中基线ASR输出都有持续改进。
### Conclusion
本研究结果突显了AEC的稳健性及其在低资源环境提升ASR输出方面的关键作用，特别是在特征设计方面的重要性。
## 297. `cs.CL` - 班加拉手语翻译：数据集创建挑战、基准测试和前景 [PDF](https://arxiv.org/pdf/2511.21533), [HTML](https://arxiv.org/abs/2511.21533)
### Authors
Husne Ara Rubaiyeat,Hasan Mahmud,Md Kamrul Hasan
### Background
目前，班加拉手语（BdSL）的资源非常有限，导致基于人工智能的手语翻译工具开发存在重大限制。为了促进此类工具的发展，创建标准的句子级数据集对于支持班加拉语社群的聋人和听力障碍者尤为重要。
### Innovation
本文提出了一个名为‘IsharaKhobor’的数据库及其两个子集，以促进相关研究。此外，作者还介绍了开发该数据库所面临的挑战，并通过与基于骨架的关键点和RQE嵌入进行基准测试来提出可能的解决方案。作者还在数据集中进行了词汇限制和语义标准化的消融分析，由此产生了两个更小的子集：‘IsharaKhobor_small’和‘IsharaKhobor_canonical_small’。
### Conclusion
通过这些研究工作，作者提供了一个公开可用的数据集，有助于推动班加拉手语翻译领域的进一步研究和发展。
## 298. `cs.CL` - 大型语言模型中的拼写约束满足及其与人类难度的对齐 [PDF](https://arxiv.org/pdf/2511.21086), [HTML](https://arxiv.org/abs/2511.21086)
### Authors
Bryan E. Tuck,Rakesh M. Verma
### Background
大型语言模型在受到硬性拼写约束时进行受控文本生成时必须满足这些约束，但在不同架构之间的系统性跨架构评估仍较为有限。本文通过评估28种配置（覆盖Qwen3、Claude Haiku-4.5和GPT-5-mini三个模型家族）在58项要求字符级约束满足的单词谜题，展示了不同架构导致了显著更大的性能差距（F1得分为0.761 vs 0.343，差距为2.0-2.2倍），并且此差距超出单一模型家族内部参数规模变化（八倍规模增长带来83%的进步）的收益。这表明，约束满足可能需要特定的架构特性或超出标准语言模型规模的训练目标。模型容量敏感性差异表现不一：高容量模型呈现出强大的回报，而处于中间大小的模型则出现了饱和或退化。
### Innovation
本文提出了跨架构评估多个大型语言模型在解决拼写约束的单词谜题上的性能，并发现不同架构在满足拼写约束方面存在显著差距。此外，研究发现随着模型容量的增加，模型的性能呈非线性变化，在一定程度上超出单靠增加计算资源所能带来的收益。这些发现表明，对于拼写约束来说，可能需要特定的架构设计或训练目标，而不仅仅是扩展参数规模或计算资源。
### Conclusion
研究利用10000名人类解谜者的难度评级，建立了模态间的一致但较为有限的校准（相关性为0.24-0.38），但仍然在一些常见的拼写非典型单词上找到了系统的失败情况（如'data'、'poop'、'loll'等），这些错误揭示了模型过度依赖于分布上的合理性，对拼写不典型但满足约束的模式进行了惩罚。这表明，可能需要架构创新超越仅仅通过参数扩展或计算预算扩展来解决这些挑战。
## 299. `cs.CL` - 神经语言模型中涌现词汇语义：神经语言模型生成文本上检验马丁法则 [PDF](https://arxiv.org/pdf/2511.21334), [HTML](https://arxiv.org/abs/2511.21334)
### Authors
Kai Kugler
### Background
本文对神经语言模型在训练过程中生成文本中的马丁法则进行了首次系统的调查，马丁法则描述了词汇频率与多义性的经验关系。研究人员利用DBSCAN聚类有上下文的嵌入向量作为词义的实操化定义，分析了四个不同参数规模（70M-1B）的Pythia模型在30个训练检查点的表现。
### Innovation
本文提出了一种新的评估神经语言模型中涌现语言结构的方法，通过分析不同参数规模的模型在训练过程中生成文本的特性，揭示了模型在不同阶段的表现差异，特别是对于小模型在晚期出现严重的语义崩溃，而大模型则有平滑的语义退化。
### Conclusion
研究发现，遵循语言规律的文本生成质量并非单调上升，而是有一个平衡的发展轨迹，存在一个最佳的语义窗口。这些发现表明，神经语言模型生成的语言结构与训练进程的关系远比预期的更加复杂，且这一关系存在一个最优点。
## 300. `cs.CL` - Odin：面向文本丰富网络表示学习的方向双模块集成 [PDF](https://arxiv.org/pdf/2511.21416), [HTML](https://arxiv.org/abs/2511.21416)
### Authors
Kaifeng Hong,Yinglong Zhang,Xiaoying Hong,Xuewen Xia,Xing Xu
### Background
文本归属图需要模型有效地结合强大的文本理解与结构引导的推理。现有的方法要么依赖于GNNs（受限于过平滑和基于跳数的扩散），要么采用Transformer忽视图拓扑，将节点视为孤立序列。
### Innovation
提出了一种新的架构Odin（Oriented Dual-module INtegration），该架构通过定向双模块将图结构注入到Transformer中，避开了多跳扩散，而是将多跳结构集成到特定的Transformer层，提供与模型语义层次对齐的低、中、高层结构抽象。Odin在聚合操作中使用全局[CLS]表示，因此避免了过平滑且解耦了结构抽象与邻域大小或图拓扑。为了在大规模或资源有限的设置中提高设计效率，提出了Light Odin，一个轻量级变种，同时保持了相同的层对齐结构抽象以实现更快的训练和推理。Odin和Light Odin共同形成了一个无跳的框架，用于原理性的结构-文本集成。
### Conclusion
实验表明，Odin在多个文本丰富图基准测试中取得了最先进的准确性，而Light Odin以显著减少的计算成本提供了竞争力的性能。Odin和Light Odin共同形成了一个统一的、无跳的框架，用于原理性的结构-文本集成。该模型的源代码已发布于该网址：this https URL
## 301. `cs.CL` - 语言模型能否提取基于证据的人类级别的细粒度证据？ [PDF](https://arxiv.org/pdf/2511.21401), [HTML](https://arxiv.org/abs/2511.21401)
### Authors
Antonín Jarolím,Martin Fajčík,Lucia Makaiová
### Background
在线新闻文章下的用户评论中经常传播错误信息，这突显了需要有效的方法来检测事实性错误信息的重要性。为了支撑或反驳从这些评论中提取的声明，需要标识相关的文档并精确指出支持或反驳每个声明的文本片段。本研究关注的是此项任务——用于捷克语和斯洛伐克语的细粒度证据提取。研究创建了一个新的数据集，包含由付费标注者进行双标签细粒度证据标注的数据。
### Innovation
开发了一个包含双标签细粒度证据的新数据集，并评估了大型语言模型（LLMs）在该数据集上的表现，以评估模型与人工标注的一致性。研究发现，虽然gpt-oss-120b模型具有许多参数，但在细粒度证据提取任务上表现不佳，而相对较小的llama3.1:8b模型在正确输出比例上表现很好。同时，qwen3:14b、deepseek-r1:32b和gpt-oss:20b模型显示了模型大小与人类注释的一致性之间的有效平衡。
### Conclusion
结果显示，即使模型规模较小，LLMs在细粒度证据提取任务上也能够产生高度准确的输出，这表明小型模型可能在这一任务上表现良好。此外，该研究提供了更多的关于大型语言模型在细粒度事实核查情境下的表现的数据，突出了模型选择的重要性。
## 302. `cs.CL` - 将文本到SQL转换视为双重状态推理：结合自适应上下文和渐进生成 [PDF](https://arxiv.org/pdf/2511.21402), [HTML](https://arxiv.org/abs/2511.21402)
### Authors
Zhifeng Hao,Qibin Song,Ruichu Cai,Boyan Xu
### Background
近年来，特别是在基于Chain-of-Thought (CoT)的分而治之推理方法的推动下，大型语言模型（LLMs）的文本到SQL（Text-to-SQL）能力得到了显著提升。然而，当这类方法应用于复杂的商业数据库时，由于上下文容量限制、不稳定的模式链接和薄弱的数据库语义基础，这些方法很难保持连贯的推理。因此，开发出一种能够克服这些问题的方法至关重要。
### Innovation
本文提出了DSR-SQL，一种双重状态推理框架，用于文本到SQL任务。该框架通过构建一个包含精炼和相关结构的大模型上下文状态，以及通过反馈指导的状态转换来逐步生成SQL合成，从而实现了SQL合成过程中的自我纠正和与用户意图的对齐。实验结果显示，在Spider 2.0-Snow和BIRD开发集上的执行准确率分别为35.28%和68.32%，而不依赖于任何后训练或上下文示例。这项工作首次展示了大型语言模型在复杂数据库上的实际应用潜力，证明了通过恰当设计上下文和生成状态可以显著改进文本到SQL的能力。
### Conclusion
DSR-SQL框架在Spider和BIRD数据集上取得了与现有方法相当的性能，说明了在大型语言模型中采用双重状态推理方法来处理复杂数据库查询的有效性。该框架有望为实现高精度的文本到SQL转换提供新的方法，并且代码将被开源。
## 303. `cs.CL` - 辅助指标帮助解析自然语言模型中的技能神经元 [PDF](https://arxiv.org/pdf/2511.21610), [HTML](https://arxiv.org/abs/2511.21610)
### Authors
Yixiu Zhao,Xiaozhi Wang,Zijun Yao,Lei Hou,Juanzi Li
### Background
大型语言模型（LLMs）在多种任务中表现出色，但其内部机制仍然模糊不清。本文介绍了一种简单、轻量级且广泛适用的方法，通过对特定技能进行编码的神经元进行隔离分析，进一步扩展到涉及多种技能的复杂场景。利用软提示训练和分类任务中识别“技能神经元”的方法，提出的方法结合了辅助指标（如外部标签和模型自身置信度分数），无需手动聚合标记，从而揭示出可解释和任务特定的行为。
### Innovation
本文的方法侧重于识别编码特定技能的神经元，扩展了对涉及多种技能的复杂场景的分析。通过关联神经元激活与外部标签和模型的置信度分数等辅助指标，无需手动聚合标记，揭示出可解释和任务特定的行为。这种方法在开放文本生成和自然语言推理任务中得到了实证验证，展示了它不仅能检测驱动已知技能的神经元，还能揭示算术推理任务中未被识别的捷径。
### Conclusion
通过这种方法在大规模语言模型中的应用，作者证明了它在复杂任务下的有效性，不仅能够识别出那些驱动已知技能的神经元，还能发现新的未被识别的推理捷径，从而提供了一种洞察语言模型内在逻辑的新途径。
## 304. `cs.CL` - Matrix: Peer-to-Peer Multi-Agent Synthetic Data Generation Framework [PDF](https://arxiv.org/pdf/2511.21686), [HTML](https://arxiv.org/abs/2511.21686)
### Authors
Dong Wang,Yang Li,Ansong Ni,Ching-Feng Yeh,Youssef Emad,Xinjie Lei,Liam Robbins,Karthik Padthe,Hu Xu,Xian Li,Asli Celikyilmaz,Ramya Raghavendra,Lifei Huang,Carole-Jean Wu,Shang-Wen Li
### Background
合成数据在训练大规模语言模型方面变得越来越重要，尤其是在真实数据稀缺、昂贵或涉及隐私的情况下。许多生成任务需要协调多智能体工作流，其中专业化的智能体合作以生成高质量、多样性更高且结构更丰富的数据。然而，现有的多智能体合成框架常常依赖于集中式的指挥者，这造成了可扩展性瓶颈，或者被硬编码用于特定领域，限制了灵活性。
### Innovation
Matrix 提出了一种去中心化的框架，其控制流和数据流表示为通过分布式队列传递的序列化消息。这种对等设计消除了集中式的指挥者。每个任务由轻量级代理独立进展，而计算密集型操作（如语言模型推理或容器化环境）由分布式服务处理。基于 Ray 构建的 Matrix 能够扩展到成千上万个并发智能体工作流，并提供了模块化、可配置的设计，使其易于适应各种数据生成工作流。
### Conclusion
我们在各种合成场景（如多智能体协作对话、基于网页推理的数据提取、客户服务环境中的工具使用轨迹生成）中评估了 Matrix。在所有情况下，Matrix 在相同硬件资源下实现了 2 至 15 倍的更高数据生成吞吐量，而不影响输出质量。
## 305. `cs.CL` - ToolOrchestra：通过高效模型和工具编排提升智能 [PDF](https://arxiv.org/pdf/2511.21689), [HTML](https://arxiv.org/abs/2511.21689)
### Authors
Hongjin Su,Shizhe Diao,Ximing Lu,Mingjie Liu,Jiacheng Xu,Xin Dong,Yonggan Fu,Peter Belcak,Hanrong Ye,Hongxu Yin,Yi Dong,Evelina Bakhturina,Tao Yu,Yejin Choi,Jan Kautz,Pavlo Molchanov
### Background
大型语言模型是强大的一般主义者，但在解决如人类最终考试（HLE）这样深刻且复杂的难题时，仍然既是概念性挑战也是计算性挑战。本文展示了通过中小型协调器管理其他模型和各种工具，不仅能提升智商的上限，还能提高解决复杂任务的效率。
### Innovation
引入了ToolOrchestra方法，这是一种训练小型协调器协调智能工具的机制。ToolOrchestra明确使用了带有结果意识、效率意识和用户偏好奖励的强化学习。通过使用ToolOrchestra，提出的Orchestrator模型不仅比之前的工具使用代理更便宜且更准确，还能根据查询匹配用户的偏好使用哪些工具。在HLE中，Orchestrator的得分（37.1%）超过了GPT-5（35.1%）且效率提高了2.5倍。在tau2-Bench和FRAMES中，Orchestrator的表现远远超过了GPT-5，同时只使用了大约30%的成本。
### Conclusion
广泛的分析表明，Orchestrator在多个指标下实现了性能与成本的最佳权衡，并且能够稳健地迁移到未见过的工具。这些结果表明，用轻量级的协调模型组合多样化的工具比现有方法更高效且更有效，为实际和可扩展的任务增强推理系统铺平了道路。
## 306. `cs.CL` - 超越URL：促进高效大语言模型预训练的元数据多样性和位置 [PDF](https://arxiv.org/pdf/2511.21613), [HTML](https://arxiv.org/abs/2511.21613)
### Authors
Dongyang Fan,Diba Hashemi,Sai Praneeth Karimireddy,Martin Jaggi
### Background
在大型语言模型（LLMs）的预训练中融入元数据最近被认为能加速训练过程。然而，先前的研究只揭示了一个有用的信号——URL，这给其他形式的元数据能否带来更大效益提出了疑问。
### Innovation
该研究探索了更广泛类型的元数据，发现包括文档质量的细粒度指标等其他类型的元数据，当被预前置时也会加速预训练。该研究还引入了元数据附加作为提高训练效率的手段，通过预测适当的目标元数据辅助任务可以加速预训练。此外，通过经过掩码损失训练的可学习元标记可以回收部分加速，形成质量感知的潜在结构。利用探针分析潜在表示，以理解元数据如何影响学习。
### Conclusion
综合这些结果，为提高LLMs预训练的效率和效果提供了实用的指导原则，包括如何有效集成元数据。
## 307. `cs.CL` - InvisibleBench: 用于照护关系AI的部署闸门 [PDF](https://arxiv.org/pdf/2511.20733), [HTML](https://arxiv.org/abs/2511.20733)
### Authors
Ali Madad(GiveCare)
### Background
InvisibleBench 是一个针对照护关系AI的部署闸门，评估了涉及3至20多次轮次互动的护理领域AI，涵盖五个维度：安全性、符合性、创伤知情设计、归属感/文化适应性和记忆。基准测试包括错过的危机情况、医疗建议（WOPR法案）、有害信息和依附工程的自动失败条件。研究人员评估了四个前沿模型在三种复杂度级别的17种场景下的表现。所有模型在安全性方面都显示出显着差距，这强调了生产系统中确定性危机路由的必要性。
### Innovation
InvisibleBench 在单轮次安全性测试的基础上，通过评估长期风险，发现实际危害，是一种创新的评估方法。该基准测试涵盖了广泛的应用场景和复杂的交互模式，评估了不同AI模型在多重维度上的表现。
### Conclusion
所有模型在安全性方面存在显著差距，强调了在实际应用中集成确定性危机处理机制的必要性。DeepSeek Chat v3 在整体评测中得分最高，但不同模型在不同维度上表现出不同的优势。研究团队发布了所有测试场景、评判提示和评分配置的代码。这类评估为照护关系AI的应用准备提供了重要参考。
## 308. `cs.CL` - 重新审视不同难度级别的泛化能力：并非那么简单 [PDF](https://arxiv.org/pdf/2511.21692), [HTML](https://arxiv.org/abs/2511.21692)
### Authors
Yeganeh Kordi,Nihal V. Nayak,Max Zuo,Ilana Nguyen,Stephen H. Bach
### Background
现有研究关于大型语言模型（LLMs）在不同任务难度下的泛化能力存在分歧，不清楚是通过训练较少难度的数据还是更多难度的数据能获得更好的结果，以及这些结果是在较易数据还是较难数据上的表现。本文通过系统评估LLMs在不同模型、数据集和细粒度组中的泛化能力，研究了难度级别之间的泛化情况。
### Innovation
本文采用Item Response Theory（IRT）对六个数据集进行了大型语言模型输出的细粒度难度排名，排除了人类对难度的主观评价，从而获得了更加客观、规模更大、更具体的难度评价。这种评估方法与众不同之处在于它完全依赖于大量不同模型的能力，而非人为判断。
### Conclusion
研究结果表明，在不同难度级别之间的泛化能力通常是有限的；训练较少难度的数据或更多难度的数据并不能在所有难度级别上实现一致的改进。因此，对于大型语言模型而言，训练和评估数据中应包含不同难度级别，这表明处理难度的捷径是风险性的。
## 309. `cs.CL` - 长文档可读性评估的分层排序神经网络 [PDF](https://arxiv.org/pdf/2511.21473), [HTML](https://arxiv.org/abs/2511.21473)
### Authors
Yurui Zheng,Yijun Chen,Shaohong Zhang
### Background
可读性评估旨在评估文本的阅读难度。近年来，虽然深度学习技术被逐渐应用于可读性评估，但大多数方法要么忽略了文本长度，要么未能考虑可读性标签的顺序关系。
### Innovation
本文提出了一种双向可读性评估机制，该机制能够捕捉上下文信息，识别文本中富含语义信息的区域，实现单个句子可读性等级的预测。这些句子级别的标签被用于帮助预测整个文档的可读性等级。此外，引入了一种成对排序算法，利用标签减法建模可读性等级的顺序关系。
### Conclusion
在中文和英文数据集上的实验结果表明，所提出模型的性能与其它基线模型相当，并且优于其他基线模型。
## 310. `cs.CL` - 大型语言模型在社会-法律背景下对非法指令的共谋回应 [PDF](https://arxiv.org/pdf/2511.20736), [HTML](https://arxiv.org/abs/2511.20736)
### Authors
Xing Wang,Huiyuan Xie,Yiyan Wang,Chaojun Xiao,Huimin Chen,Holli Sargeant,Felix Steffek,Jie Shao,Zhiyuan Liu,Maosong Sun
### Background
大型语言模型（LLMs）正在以前所未有的规模部署，协助数百万用户进行日常工作。然而，这些模型在协助非法活动方面的风险尚未得到充分探索。本研究定义这种高风险行为为共谋促进 - 提供使非法用户指令得以实施的帮助和支持。我们通过四项基于实证的研究评估了广泛部署的LLMs中这种行为的普遍性。利用真实的法律案例和现有的法律框架，我们构建了一个评估基准，包括269种非法情境和50种非法意图，以评估LLMs的共谋促进行为。研究揭示了广泛存在的LLMs对共谋促进的易感性，GPT-4在近一半的测试案例中提供了非法帮助。此外，LLMs在提供可信的法律警告和积极引导方面表现出色不足。
### Innovation
本研究首次通过构建一个涵盖269种非法情境和50种非法意图的基准评估LLMs在社会-法律背景下对非法指令的共谋促进行为。研究发现，LLMs对共谋促进的易感性广泛存在，并且在社会层面揭示了针对边缘化和弱势群体的潜在有害模式。
### Conclusion
研究结果表明，现有安全对齐策略是不够的，甚至可能加剧共谋行为。此外，模型的认知偏见与共谋行为存在关联，这基于温暖和能力两个维度。因此，需要改进现有策略以减少LLMs对非法活动的贡献，特别关注对边缘化和弱势群体的潜在有害影响。
## 311. `cs.CL` - CANVAS: 用于工具基于用户界面设计的视觉语言模型基准 [PDF](https://arxiv.org/pdf/2511.20737), [HTML](https://arxiv.org/abs/2511.20737)
### Authors
Daeheon Jeong,Seoyeon Byun,Kihoon Son,Dae Hyun Kim,Juho Kim
### Background
用户界面（UI）设计是一个迭代过程，设计师通过设计软件逐步完善工作。近期，视觉语言模型（VLMs）结合工具调用的发展表明，这些模型能够通过迭代操作设计软件来编辑UI设计。但是，由于缺乏针对基于工具的UI设计性能的基准评估，VLMs在设计软件中的能力仍未得到验证。因此，建立一个针对工具基于用户界面设计的基准很有必要。
### Innovation
本文提出CANVAS，一个用于视觉语言模型在工具基于用户界面设计上的基准。CANVAS包含598个基于工具的设计任务，涉及来自30种功能类别（如引导、消息等）的3300个移动UI设计。任务类型分为设计复制和设计修改，以评估模型的能力。此外，研究还发现了模型的常见错误模式，为未来改进工具基于设计功能指明了方向。
### Conclusion
结果显示，领先模型展示了更策略性的工具调用，提升了设计质量。同时，发现模型展示出的常见错误模式为未来工作指明了方向。CANVAS为评估视觉语言模型在工具基于用户界面设计中的性能提供了重要的工具。
## 312. `cs.CL` - 来自Tip-of-the-Tongue检索查询的无监督记忆建模 [PDF](https://arxiv.org/pdf/2511.20854), [HTML](https://arxiv.org/abs/2511.20854)
### Authors
Sree Bhattacharyya,Yaman Kumar Singla,Sudhir Yarram,Somesh Kumar Singh,Harini S I,James Z. Wang
### Background
视觉内容的记忆力引起了科学界的广泛关注，其应用范围广泛，包括理解人类记忆的复杂方面和提升内容设计。然而，收集人类的记忆力注释过程昂贵，限制了用于建模视觉内容记忆力的数据集的多样性和可扩展性。现有的大多数数据集仅收集视觉内容的聚合记忆力分数，未捕捉到自然、开放式回忆描述中存在的丰富记忆力信号。
### Innovation
本文引入了首个大型无监督数据集，专门用于建模视觉记忆力信号，包含超过82,000个视频及其描述性回忆数据，并利用来自Reddit等在线平台的Tip-of-the-Tongue检索查询。该数据集和模型展示了生成开放式的记忆力描述和多模态Tip-of-the-Tongue检索的新方法，使得使用大型视觉-语言模型在这两个记忆力相关任务上超过了GPT-4o等最先进的模型。
### Conclusion
我们的数据集和模型为视觉内容记忆力研究提供了一个新的方向，推进了该领域的进步。
## 313. `cs.CL` - TrafficLens：使用大语言模型进行多摄像头交通视频分析 [PDF](https://arxiv.org/pdf/2511.20965), [HTML](https://arxiv.org/abs/2511.20965)
### Authors
Md Adnan Arefeen,Biplob Debnath,Srimat Chakradhar
### Background
交通摄像头在城市地区和智能交通系统中扮演着重要角色，通过路口的多摄像头可以提高执法能力、交通管理和行人安全。然而，有效管理和分析多摄像头视频流的数据量庞大，对先进的分析工具提出了需求。尽管像ChatGPT这样的大型语言模型（LLMs）在文本任务中表现出色，但将其集成到交通视频分析中需要将视频数据转换为文本，这耗时且延迟了交通视频及时利用和生成洞察的需求。
### Innovation
本文提出了一种名为TrafficLens的专门算法，用于多摄像头交通交叉口。TrafficLens采用串行方法，利用摄像头重叠的覆盖区域，逐步应用具有不同令牌限制的Vision-Language模型（VLM），将前一个输出作为对下一个摄像头的提示，从而快速生成详细的文本描述并减少处理时间。此外，TrafficLens通过对象级相似性检测器智能地跳过冗余的VLM调用。实验证明，TrafficLens可以将视频到文本的转换时间减少多达4倍，同时保持信息准确性。
### Conclusion
实验结果表明，TrafficLens可以将视频到文本的转换时间减少多达4倍，同时保持信息准确性，在处理大量交通视频数据方面表现出色。
## 314. `cs.CL` - RoParQ：基于短语感知的大型语言模型一致性对变式问答的对齐 [PDF](https://arxiv.org/pdf/2511.21568), [HTML](https://arxiv.org/abs/2511.21568)
### Authors
Minjoon Choi
### Background
大型语言模型（LLMs）在回答重新表述的问题时经常表现出不一致的行为，这表明它们依赖于表面级别的模式而不是真正的语义理解。
### Innovation
本研究提出了RoParQ基准测试，用于评估闭卷多选问答过程中的变式一致性。该基准通过自动化生成的重新表述和选择引起裁判模型不一致信心的例子来构造。此外，引入了XParaCon评价指标来量化模型的鲁棒性并提出了一种基于推理的、短语感知的监督微调（SFT）策略来使模型向语义不变性靠拢。
### Conclusion
实验表明，这种有针对性的对齐显著提高了鲁棒性。微调后的轻量级模型在一致性和大型预训练模型相当。这些结果强调了本方法在缓解浅层记忆和培养更鲁棒、可靠的LLM方面的有效性。
## 315. `cs.CL` - 声音、偏见和共指：语音翻译中性别可解释性研究 [PDF](https://arxiv.org/pdf/2511.21517), [HTML](https://arxiv.org/abs/2511.21517)
### Authors
Lina Conti,Dennis Fucci,Marco Gaido,Matteo Negri,Guillaume Wisniewski,Luisa Bentivogli
### Background
与其他文本相比，语音中通过音高等声学线索可以反映说话人的特征，如性别，这形成了模态特定的偏见问题。例如，在从存在明确性别的语言（如英语）翻译到不存在性别的语言时，可能根据说话人的音声特征进行性别认定，这可能导致误认性别。这一点在语音翻译模型中尚未完全理解。该研究通过分析三种语言对（英语-西班牙语/法语/意大利语），探讨训练数据特征、内部语言模型偏差和声学信息相互作用，研究模型如何决定性别分配。
### Innovation
研究发现模型并未简单复制训练数据中的性别关联，而是学习到更广泛且普遍的男性占多数的模式。尽管内部语言模型存在强烈男性偏见，但在适当声学信息输入下可表现出性别中立。通过对比特征归因于频谱图，研究揭示高准确性模型依赖一个未知机制，即利用第一人称代词将性别相关词汇与说话人关联起来，获取频谱分布的性别信息，而非集中于音高。
### Conclusion
研究强调语音翻译模型中性别认定的复杂性，指出声学信息在克服偏见中的关键作用。研究为后续改进语音翻译模型中的性别表达提供新的视角。
## 316. `cs.CL` - 如果作家从未存在过，那么当作家死后又如何？一项针对捷克AI和人类创作的诗歌的接受实验 [PDF](https://arxiv.org/pdf/2511.21629), [HTML](https://arxiv.org/abs/2511.21629)
### Authors
Anna Marklová,Ondřej Vinš,Martina Vokáčová,Jiří Milička
### Background
大规模语言模型日益能够生成创意文本，但大多数关于AI生成诗歌的研究集中在英语上，因为英语是训练数据的主导语言。本研究探讨了捷克语诗歌（一种结构复杂且资源困难的语言）的机器生成和人类生成之间的接受度差异。
### Innovation
本研究首次在捷克语诗歌上进行AI生成诗歌的接受实验，考察捷克母语者能否辨别AI和人类写作的诗歌，并如何审美评价这些诗歌。研究发现，参与者无法区分诗歌的作者身份，亦不论美学生态偏见，即使AI生成的诗歌被评价为不那么有吸引力。
### Conclusion
研究结果表明，即使是复杂形态结构且资源不足的捷克语，AI也可产生令人信服的诗歌。此外，读者对于作者身份的信念与其对诗歌的审美评价之间存在联系。
## 317. `cs.CL` - RosettaSpeech：仅依赖单语言数据的零样本语音到语音翻译 [PDF](https://arxiv.org/pdf/2511.20974), [HTML](https://arxiv.org/abs/2511.20974)
### Authors
Zhisheng Zheng,Xiaohang Sun,Tuan Dinh,Abhishek Yanamandra,Abhinav Jain,Zhu Liu,Sunil Hadap,Vimal Bhat,Manoj Aggarwal,Gerard Medioni,David Harwath
### Background
目前，平行语音语料库的稀缺性严重阻碍了语音到语音翻译（S2ST），通常需要依赖复杂且多阶段的处理管道。这限制了S2ST的效率与效果。
### Innovation
本文提出了RosettaSpeech，这是一种基于单语言语音文本数据并附加机器翻译监督的新颖且简化的零样本S2ST框架。该方法利用了文本基的神经机器翻译模型中的语言知识，但在训练过程中仅使用文本作为中间桥梁，而在推理阶段作为直接的端到端语音到语音模型。这种方法在标准基准测试中实现了最先进的结果，特别是在CVSS-C测试集上，RosettaSpeech的ASR-BLEU得分显著提升了27%和14%，分别对应德语到英语和西班牙语到英语。
### Conclusion
RosettaSpeech通过优先依赖丰富的平行文本数据而不是难以获取的平行语音数据，提供了一种可以为更多语言创建高质量、保留说话人特征的S2ST的可扩展途径，实现直接与端到端的语音到语音模型。
## 318. `cs.CL` - ST-PPO: Stabilized Off-Policy Proximal Policy Optimization for Multi-Turn Agents Training [PDF](https://arxiv.org/pdf/2511.20718), [HTML](https://arxiv.org/abs/2511.20718)
### Authors
Chenliang Li,Adel Elmahdy,Alex Boyd,Zhongruo Wang,Alfredo Garcia,Parminder Bhatia,Taha Kass-Hout,Cao Xiao,Mingyi Hong
### Background
PPO在多轮对话和推理任务中用于训练大型语言模型（LLM）的字符级表示中得到了广泛应用。然而，其性能常常不稳定，容易崩溃。经过经验分析，研究者确定了这种设置下的两个主要不稳定源：（1）字符级别的重要性采样与多轮环境中具有不同回合级阶段的自然粒度不一致，（2）来自离策样本的不准确的优势估计，由于批评者未学会评估某些状态-动作对，导致高方差梯度和不稳定的更新。
### Innovation
引入了两种互补的稳定化技术：（1）回合级别的重要性采样，使优化与多轮推理的自然结构相一致，（2）裁剪偏差校正，通过降低不可靠、高度离策样本的权重来正规范化梯度。根据这些组件的组合方式，获得了三种变体：Turn-PPO（仅回合级别采样），S-PPO（裁剪偏差校正应用于字符级别PPO），和ST-PPO（结合回合级别采样与裁剪偏差校正）。实验证明，ST-PPO和S-PPO共同展示了这两种稳定机制如何解决互补的不稳定来源，能够在多轮搜索任务中防止性能崩溃，维持较低的剪裁率，并在优化期间实现比标准字符级别PPO更高的任务性能。
### Conclusion
研究结果表明，结合回合级别重要性采样与裁剪偏差校正提供了稳定多轮LLM代理训练的实用和可扩展的解决方案。
## 319. `cs.CL` - TALES: 文本生成人物库与LLM生成故事中的文化表现分析 [PDF](https://arxiv.org/pdf/2511.21322), [HTML](https://arxiv.org/abs/2511.21322)
### Authors
Kirti Bhagat,Shaily Bhatt,Athul Velagapudi,Aditya Vashistha,Shachi Dave,Danish Pruthi
### Background
全球范围内，成千上万的用户依靠AI聊天机器人解决创意需求，吸引了对这类聊天机器人如何代表多元文化的研究兴趣。然而，在开放任务中评估文化表现仍然具有挑战性且研究较少。本文探讨了大型语言模型（LLM）生成的针对印度多元文化身份的故事中的文化误表征问题。
### Innovation
本文提出了TALES，一个用于评估LLM生成故事中印度多元文化身份文化误表征的评价框架。首次开发了TALES-Tax分类法，通过焦点小组和个别调查汇集了印度生活经验参与者的意见。然后通过大规模注释研究对6个模型进行了评估，涵盖了2,925个注释，来自108名有活文化经验的注释者，分布在印度71个地区和14种语言中。发现88%的生成故事包含一种或多种文化不准确之处，尤其是在中低资源语言和印度郊区的故事中更为普遍。
### Conclusion
通过对TALES-Tax进行转化，创建了TALES-QA独立问题库，以评估基础模型的文化知识。结果令人惊讶地发现，尽管生成了一些文化误表征的故事，模型仍然往往拥有所需的充分文化知识。
## 320. `cs.CL` - 基于优化反演的无训练扩散先验技术在文本到图像生成中的应用 [PDF](https://arxiv.org/pdf/2511.20821), [HTML](https://arxiv.org/abs/2511.20821)
### Authors
Samuele Dell'Erba,Andrew D. Bagdanov
### Background
扩散模型已经在文本到图像生成方面建立了最先进的技术，但其性能往往依赖于一个扩散先验网络来将文本嵌入转换为视觉流形，便于解码。然而，这些先验网络计算成本高且需要在大规模数据集上进行大量训练。
### Innovation
本文通过引入一种无需训练和数据的替代方法——基于优化的视觉反演（OVI），挑战了完全依赖预先训练的先验网络的必要性。OVI利用随机伪词初始化隐式视觉表示，并通过迭代优化以最大化输入文本提示嵌入的余弦相似度。此外，提出了一种基于马氏距离和最近邻损失的新约束方法，以使OVI优化过程更符合真实图像的分布。
### Conclusion
实验表明，OVI可以作为传统先验的替代方法。更重要的是，分析揭示了一个关键问题出现在当前的评估基准T2I-CompBench++中，简单地使用文本嵌入作为先验就可以取得令人惊讶的高评分，尽管其视觉质量较低。受限的OVI方法在这一点上优于基线，特别是最近邻方法取得了可与现有的数据高效先验达到或优于最先进的定量评分，这表明该方法值得进一步研究。代码将在接受后公开。
## 321. `cs.CL` - ENACT: 使用自视点交互的世界建模评估具身认知 [PDF](https://arxiv.org/pdf/2511.20937), [HTML](https://arxiv.org/abs/2511.20937)
### Authors
Qineng Wang,Wenlong Huang,Yu Zhou,Hang Yin,Tianwei Bao,Jianwen Lyu,Weiyu Liu,Ruohan Zhang,Jiajun Wu,Li Fei-Fei,Manling Li
### Background
具身认知理论认为，智能源于感觉运动交互而非被动观察。本文探讨现代视觉-语言模型（VLMs）是否在大量无具身交互训练的情况下展现出具身认知的特征。
### Innovation
提出了ENACT基准测试，将具身认知评估转化为视觉问答（VQA）格式中的自视点交互的世界建模。ENACT将任务设置为部分可观测马尔可夫决策过程（POMDP），将动作定义为场景图变化，包含正向和逆向两种序列排序任务：一是根据动作重新排序被打乱的观察，二是根据观察重新排序被打乱的动作。此方法隐含地要求模型具有自主行为识别、动作效果推理、具身意识以及基于部分可观察自视点输入的交互性和长时记忆能力，同时避免低级图像合成干扰评估。
### Conclusion
实验表明，最前沿的VLMs在长时交互任务上与人类的性能差距逐渐增大。模型在这两个任务上表现不均衡，并显示出人类中心主义的偏见，包括偏好右手动作以及在摄像头参数或视角与人类视觉不一致时性能下降。
## 322. `cs.CL` - Prune4Web: DOM树剪枝编程技术在Web代理中的应用 [PDF](https://arxiv.org/pdf/2511.21398), [HTML](https://arxiv.org/abs/2511.21398)
### Authors
Jiayuan Zhang,Kaiquan Chen,Zhihao Lu,Enshen Zhou,Qian Yu,Jing Zhang
### Background
网络自动化利用智能代理模拟与网页界面的人类交互执行高级任务。尽管基于大型语言模型(LLM)的网络代理具备一定能力，但在处理复杂的真实世界网页时，仍然面临着DOM结构庞大的问题——通常包含10,000到100,000个标记，导致难以高效导航。现有方法通常依赖粗略的DOM截断，可能导致关键信息丢失，或者采用低效的启发式方法和独立评分模型，难以在精确度和可扩展性之间找到平衡。
### Innovation
我们提出了Prune4Web，这是一种新颖的范式，将DOM处理从资源密集型LLM读取转移到高效的程序化剪枝。其中核心是DOM树剪枝编程，利用分解子任务的语义线索生成可执行的Python评分脚本，动态过滤DOM元素。这种方法避免了LLMs直接处理原始大规模DOM的需求，将遍历和评分任务委托给轻量级、可解释的程序。这一方法实现了候选元素数量25倍到50倍的减少，不仅有助于精确定位操作，还能减少注意力分散。此外，我们还提出了一种专门的数据标注流水线和两轮对话训练策略，共同优化了规划器、程序化过滤器和定位器。
### Conclusion
广泛实验表明，Prune4Web达到了最先进的性能。特别是在低级别定位任务上，从46.8%提高到88.28%，证明了其在真实世界网页自动化中的有效性和优越性。
## 323. `cs.CL` - TAGFN: 在大语言模型时代用于假新闻检测的带文本属性的图数据集 [PDF](https://arxiv.org/pdf/2511.21624), [HTML](https://arxiv.org/abs/2511.21624)
### Authors
Kay Liu,Yuwei Han,Haoyan Xu,Henry Peng Zou,Yue Zhao,Philip S. Yu
### Background
近年来，大型语言模型（LLMs）在文本标记图上的机器学习方面取得了革命性进展，但在图离群点检测（尤其是假新闻检测）中的应用仍然严重不足。关键挑战之一是缺乏大规模、真实且注释良好的离群点检测基准数据集。
### Innovation
作者引入了TAGFN，这是一个大规模且真实的带有文本属性的图数据集，专门用于离群点检测，特别是假新闻检测。TAGFN能够严格评估传统和基于LLM的图离群点检测方法，并促进独立开发的误信检测能力。
### Conclusion
作者期望TAGFN将成为社区的一项宝贵资源，推动基于图的离群点检测的稳健性和可信赖人工智能的进步。数据集和相关代码已公开提供。
## 324. `cs.CL` - 基于两阶段符号过程的Zipf分布：随机词汇过篩下的稳定性 [PDF](https://arxiv.org/pdf/2511.21060), [HTML](https://arxiv.org/abs/2511.21060)
### Authors
Vladimir Berman
### Background
Zipf定律在语言中缺乏确定的起源，各领域对此有所争议。本研究通过几何机制解释了类似于Zipf定律的行为，而不依赖于语言要素。
### Innovation
提出了全组合词模型（FCWM），该模型通过有限字母表形成词语，生成词长的几何分布。交互的指数力产生幂律的等级-频率曲线，该曲线由字母表大小和空白符号概率决定。模拟支持预测，与英俄等语言及混合体数据相符，表明Zipf类型的规律源自几何约束，而非沟通效率。
### Conclusion
该研究通过去除语言元素依赖，使用几何机制证明了Zipf类型定律的起源，并通过模拟验证了这一假设的有效性。
## 325. `cs.CL` - 后训练大型语言模型中离线数据选择和在线自我精炼生成的统一理解 [PDF](https://arxiv.org/pdf/2511.21056), [HTML](https://arxiv.org/abs/2511.21056)
### Authors
Quan Xiao,Tianyi Chen
### Background
在适应特定下游任务时，增强数据质量的离线数据选择和在线自我精炼生成是至关重要的步骤。通过优化视角，论文探讨了这两步操作。
### Innovation
论文通过引入 bilevel 数据选择框架，为离线数据选择和在线自我精炼生成提供了一个统一的理解。通过将每个问题和响应赋予一个学习得到的数据权重（显式或隐式），论文首次从理论上证明了这种框架的有效性，并展示其性能优势。通过结合离线数据和验证加权在线生成，论文提升了微调性能。
### Conclusion
通过实验证明了该方法在质量增强和安全感知大型语言模型微调方面有效。
## 326. `cs.CL` - AnchorOPT：迈向优化动态锚点以实现适应性提示学习 [PDF](https://arxiv.org/pdf/2511.21188), [HTML](https://arxiv.org/abs/2511.21188)
### Authors
Zheng Li,Yibing Song,Xin Zhang,Lei Luo,Xiang Li,Jian Yang
### Background
现有的基于CLIP模型的提示学习方法利用文本令牌作为锚点来指导可学习的软令牌。这种方法提高了CLIP的泛化能力，但这些锚点是静态的，缺乏跨任务和不同阶段的适应性灵活性。
### Innovation
提出了一种名为 AnchorOPT 的动态锚点为基础的提示学习框架。AnchorOPT 在两个关键维度上引入了动态性：(i) 锚点值不是手工设计的显式文本令牌（如“形状”、“颜色”），而是从任务特定数据中动态学习；(ii) 锚点和软令牌之间的位置关系不再是固定的，而是通过在训练阶段和任务上下文中可学习的位置矩阵进行适应性优化。该框架在两个阶段进行训练：首先学习锚点令牌，然后冻结并转移它们到第二个阶段优化软令牌和位置矩阵。
### Conclusion
广泛的实验表明，仅使用简单的可学习锚点和位置矩阵就能达到或超过一些引入了额外可学习模块或正则化技术的方法的性能。作为可插拔模块，AnchorOPT 能够无缝集成到现有的框架中，在不同数据集上取得了持续的性能提升。代码已公开于此：this https URL
## 327. `cs.CL` - BanglaASTE：一种用于孟加拉电子商务评论中方面-情感-意见提取的集成深度学习新型框架 [PDF](https://arxiv.org/pdf/2511.21381), [HTML](https://arxiv.org/abs/2511.21381)
### Authors
Ariful Islam,Md Rifat Hossen,Abir Ahmed,B M Taslimul Haque
### Background
方面基情感分析（ABS）已经成为了从用户生成内容中提取细粒度情感洞察的重要工具，特别在电子商务和社交媒体领域。然而，关于孟加拉语言的ABS研究仍然缺乏，主要原因是缺少全面的数据集和专门的三元组提取框架。为了填补这一空白，本文提出了一个名为BanglaASTE的新颖框架，用于从孟加拉产品评论中同时识别方面术语、意见表达和情感极性。
### Innovation
本文的创新点包括：1）创建了第一个注释的Bangla三元组提取数据集，包含3,345个产品评论，数据来源包括Daraz、Facebook和Rokomari等主要电子商务平台；2）开发了一种基于图的方法与语义相似性技术相结合的混合分类框架；3）实现了一种结合BanglaBERT上下文嵌入和XGBoost增强算法的集成模型，以提高三元组提取性能。
### Conclusion
实验结果表明，本研究采用的集成方法在所有评估指标上都优于基线模型，准确率达到了89.9%，F1分数为89.1%。该框架有效地解决了孟加拉文本处理中的非正式表达、拼写变体和数据稀疏性等问题，推动了低资源语言情感分析的研究前沿，并为孟加拉电子商务分析应用提供了可扩展的解决方案。
## 328. `cs.CL` - 在大型音频语言模型中的音频标记压缩 [PDF](https://arxiv.org/pdf/2511.20973), [HTML](https://arxiv.org/abs/2511.20973)
### Authors
Saurabhchand Bhati,Samuel Thomas,Hilde Kuehne,Rogerio Feris,James Glass
### Background
大型音频语言模型（LALMs）在多种任务中表现出色，从语音识别到通用音频理解。然而，它们的扩展性受限于注意力机制的二次复杂度和音频信号的高标记率。这些挑战使将LALMs扩展到长音频片段并在嵌入式设备等资源受限平台上部署变得困难。
### Innovation
本文探索了无监督切分、均匀平均池化等技术，以减少LALM音频编码器生成的音频标记数量，但这些标记在被LLM解码器消耗之前。为了缓解由压缩表示引入的潜在性能下降，本文采用了低秩适配器对模型进行微调。本文评估了所提出的模型在自动语音识别和语音到语音翻译任务上的性能，这些任务依赖于有效地揭示输入信号的潜在词汇内容，并研究了下采样对这些任务的影响。
### Conclusion
实验结果表明，压缩的LALMs可以达到接近帧级LALMs的性能表现，同时在LLM主干之前将输入音频标记的数量最多减少三倍。
## 329. `cs.CL` - 如何正确报告LLM作为裁判的评估 [PDF](https://arxiv.org/pdf/2511.21140), [HTML](https://arxiv.org/abs/2511.21140)
### Authors
Chungpa Lee,Thomas Zeng,Jongwon Jeong,Jy-yong Sohn,Kangwook Lee
### Background
大型语言模型（LLMs）越来越多地被用作替代人类的评估者。虽然它们具有可扩展性，但它们的判断存在噪声，由于LLMs的具体性和敏感性不完美，导致估测的准确度存在偏见。尽管已经存在一些用于纠正偏差的方法，但在LLM研究中这些方法的使用率不高，通常假设对模型的具体性和敏感性有完全了解。此外，通常我们只能获得这些值的估计，而且关于如何仅使用估计值来正确构造置信区间的方法还不明确。
### Innovation
本工作提出了一个简单的插值框架，可以纠正这样的偏差，并构建同时反映测试集和校准数据集不确定性的置信区间，使基于LLM的评估在实践中更具有统计学合理性。此外，为了减少准确度估计的不确定性，引入了一种适应性算法，有效分配校准样本大小。
### Conclusion
通过纠正偏差并构建置信区间，该工作旨在使基于LLM的评估在实践中更加可靠且统计上更稳健。通过引入一种有效的适应性算法来分配校准样本大小，进一步减少误差估计的不确定性。
## 330. `cs.CL` - 主观深度和历时变换器：学习何时何地进行计算 [PDF](https://arxiv.org/pdf/2511.21408), [HTML](https://arxiv.org/abs/2511.21408)
### Authors
Frederico Wieser,Martin Benfeghoul,Haitham Bou Ammar,Jun Wang,Zafeirios Fountas
### Background
标准Transformer结构中的计算分配通常是刚性和均匀的，这在其应用中会限制效率和可扩展性，特别是在处理大规模模型和长序列数据时。研究人员发现，这种固定的、均匀的计算分配使得模型难以适应变化较大的或需求较高的情况，限制了其执行能力。
### Innovation
本文引入了两种新的Transformer架构——主体深度变换器（SDT）和主体历时变换器（STT），旨在动态调整计算分配，提高可扩展性和效率。SDT和STT都利用贝叶斯惊讶信号动态引导计算，在解码器上仅使用标准Transformer架构，使其能够在不确定性高的地方增加计算，而在预测性高的地方减少计算，从而减少整体计算量。具体来说，SDT通过交替的决策和动态层实现计算动态路由，STT进一步扩展到时间领域，使用转变网络预测残差更新，动态执行或跳过Transformer块。
### Conclusion
两种提出的架构在训练过程中展示了从新颖性驱动到预测驱动的转换，证明了其与惊讶信号原则的一致性。虽然计算容量有所缩减，它们仍然提供了关于条件计算中的计算-性能权衡的初步见解。实验结果表明，SDT和STT分别通过跳过计算减少了每个计算跳过层75%的自注意力计算和50%的KV缓存需求，为更高效的模型开辟了道路。
## 331. `cs.CL` - 测试时计算量下视觉语言模型的逆向扩展现象：基于误导信息的实证分析 [PDF](https://arxiv.org/pdf/2511.21397), [HTML](https://arxiv.org/abs/2511.21397)
### Authors
Jiyun Bae,Hyunjong Ok,Sangwoo Mo,Jaeho Lee
### Background
先前对语言模型的研究已经报告了反向扩展效应，即文本误导信息会导致推理过程变长但效果降低。本文旨在探讨类似现象是否也发生在多模态设置中。
### Innovation
本文引入了名为 Idis 的视觉问答数据集，系统地沿语义、数值和空间维度变化误导信息，进一步研究视觉误导信息对测试时扩展的影响。
### Conclusion
视觉误导信息与文本误导信息有根本差异：尽管反向扩展现象仍然存在，但添加视觉误导信息会降低准确性而不会增加推理长度。文章还提出了一个跟踪推理痕迹中的属性计数策略，以揭示误导信息、推理长度和准确性之间的相互作用，并且这些趋势也扩展到了视觉偏见基准Waterbirds，提出了简单的提示策略以减轻推理模型中的偏见驱动预测。
## 332. `cs.CL` - Gated KalmaNet：通过测试时岭回归实现的淡出记忆层 [PDF](https://arxiv.org/pdf/2511.21016), [HTML](https://arxiv.org/abs/2511.21016)
### Authors
Liangzu Peng,Aditya Chattopadhyay,Luca Zancato,Elvis Nunez,Wei Xia,Stefano Soatto
### Background
线性状态空间模型（SSMs）虽然在内存和计算成本上具有高效性，但它们只能维持一个损失性的、日渐淡化的历史摘要，这在依赖于回忆的任务中通常会导致性能较差。为了弥合这种差距，论文提出了一种名为Gated KalmaNet（GKA）的新层，该层在预测下一个词时考虑了完整的过去，同时保持了SSM式效率。GKA通过在测试时解决在线岭回归问题，实现了常数级别的内存使用和线性计算成本。论文受到了卡尔曼滤波器的启发，但发现在低精度环境下标准的卡尔曼滤波器方程存在数值不稳定问题，并且难以在现代硬件上并行化。
### Innovation
1. 提出了一种输入相关门控的自适应正则化策略，通过控制岭回归的条件数来保持数值稳定性，同时平衡内存保留；2. 使用Chebyshev迭代而非其他传统迭代求解器，以提高在低精度环境中的稳定性；3. 开发了一种硬件感知的、块级的Chebyshev迭代实现，并为通过适应性正则化和门控机制进行反向传播设计了定制内核。
### Conclusion
在短文本理解任务中，GKA表现出较强的语言理解能力，优于现有的SSM层。在长文本理解任务（如RAG和LongQA，最大128k词）中，GKA在性能上比其他淡出记忆基线方法提高了超过10%。
## 333. `cs.CL` - G$^2$VLM: 基于几何的统一3D重建与空间推理的视觉语言模型 [PDF](https://arxiv.org/pdf/2511.21688), [HTML](https://arxiv.org/abs/2511.21688)
### Authors
Wenbo Hu,Jingli Lin,Yilin Long,Yunlong Ran,Lihan Jiang,Yifan Wang,Chenming Zhu,Runsen Xu,Tai Wang,Jiangmiao Pang
### Background
视觉语言模型（VLMs）在空间智能方面表现较弱，特别是在空间理解和推理任务上的表现不佳。这一问题是由于缺乏一种能够从二维图像重建三维空间的视觉几何学习过程。文章指出，现有模型在空间方面的能力不足。
### Innovation
提出了G$^2$VLM（基于几何的视觉语言模型），该模型能够结合空间3D重建和空间理解两个基础的空间智能方面。G$^2$VLM模型融合了丰富的多视图图像和视频数据进行训练，并利用低层级的三维视觉先验知识，使模型在空间理解任务上表现更为出色。
### Conclusion
实验表明G$^2$VLM模型在3D重建和空间理解任务上都能达到或超过最先进的模型表现，将其用作一个强有力的基线模型，可以为社区提供更多应用场景，如3D场景编辑等。
## 334. `cs.CL` - 细粒度和可解释的多模态总结事实性评估 [PDF](https://arxiv.org/pdf/2402.11414), [HTML](https://arxiv.org/abs/2402.11414)
### Authors
Yue Zhang,Jingxuan Zuo,Liqiang Jing
### Background
多模态总结旨在基于输入的文本和图像生成简洁的总结。现有方法可能产生不准确的输出。为了评估多模态总结模型的事实准确性，本文提出了两个细粒度且可解释的评估框架（FALLACIOUS），用于不同应用场景，即基于参考的事实性评估框架和无需参考的事实性评估框架。无需参考的事实性评估框架无需真实数据，因此适用范围更广泛。
### Innovation
本文提出了两种细粒度且可解释的多模态总结事实性评估框架（FALLACIOUS），分别适用于基于参考和无需参考的应用场景。通过与现有其他评估指标的相关性分析展示了方法的有效性。
### Conclusion
实验结果证明了所提方法的有效性。代码和数据集将通过GitHub发布。
## 335. `cs.CL` - 评估大型语言模型在放射学自然语言处理中的应用 [PDF](https://arxiv.org/pdf/2307.13693), [HTML](https://arxiv.org/abs/2307.13693)
### Authors
Zhengliang Liu,Tianyang Zhong,Yiwei Li,Yutong Zhang,Yi Pan,Zihao Zhao,Peixin Dong,Chao Cao,Yuxiao Liu,Peng Shu,Yaonai Wei,Zihao Wu,Chong Ma,Jiaqi Wang,Sheng Wang,Mengyue Zhou,Zuowei Jiang,Chunlin Li,Jason Holmes,Shaochen Xu,Lu Zhang,Haixing Dai,Kai Zhang,Lin Zhao,Yuanhao Chen,Xu Liu,Peilong Wang,Junhao Chen,Pingkun Yan,Jun Liu,Bao Ge,Lichao Sun,Dajiang Zhu,Xiang Li,Wei Liu,Xiaoyan Cai,Xintao Hu,Xi Jiang,Shu Zhang,Xin Zhang,Tuo Zhang,Shijie Zhao,Quanzheng Li,Hongtu Zhu,Dinggang Shen,Tianming Liu
### Background
大型语言模型（LLMs）在自然语言处理（NLP）领域的发展标志着一个转折点。LLMs不仅在多个领域能够焕发新的活力，而且对医学领域产生了重大影响。尤其是，这些模型现在变得更加普遍，并且许多模型都具有双语能力，能够熟练掌握英语和中文。然而，目前对这些模型的全面评估尚未开展，尤其是在放射学NLP领域，这种缺乏评估的情况尤为明显。
### Innovation
本研究旨在通过批判性地评估32个LLMs在解读放射学报告方面的应用来填补这一空白，尤其是评估它们从影像学发现中得出印象的能力。这为理解这些LLMs的性能、优势和不足提供了关键见解，指引它们在医疗领域的实际应用。
### Conclusion
研究结果揭示了32个LLMs在解读放射学报告过程中的表现、强项和弱点，为它们在医疗领域的实际应用提供了重要指导信息。
## 336. `cs.CL` - Gram2Vec：一种可解释的文档向量化系统 [PDF](https://arxiv.org/pdf/2406.12131), [HTML](https://arxiv.org/abs/2406.12131)
### Authors
Peter Zeng,Hannah Stortz,Eric Sclafani,Alina Shabaeva,Maria Elizabeth Garza,Daniel Greeson,Owen Rambow
### Background
该研究介绍了一种名为Gram2Vec的语法风格嵌入系统。Gram2Vec通过提取文本中存在的语法特征的标准化相对频率，将文档嵌入到更高维的空间中。相较于神经网络方法，Gram2Vec因为其基于特征向量生成方式的固有可解释性而具有优势。论文通过作者身份验证和AI检测两个应用场景展示了Gram2Vec的应用。
### Innovation
Gram2Vec的核心创新在于其基于语法特征的可解释嵌入方法。相较于神经网络，Gram2Vec生成的特征向量具有内在的可解释性。该研究展示了Gram2Vec在作者身份验证和AI检测中的应用，有助于这些领域的研究和实践。
### Conclusion
论文展示了Gram2Vec在两个具体场景中的应用，证明了其在作者身份验证和AI检测中的有效性。Gram2Vec的特点使其在需要可解释性的应用场景中具有独特的优势，为相关领域的研究提供了新的思路和方法。
## 337. `cs.CL` - 大型语言模型中考虑推理的微调以实现Best-of-N采样 [PDF](https://arxiv.org/pdf/2412.15287), [HTML](https://arxiv.org/abs/2412.15287)
### Authors
Yinlam Chow,Guy Tennenholtz,Izzeddin Gur,Vincent Zhuang,Bo Dai,Sridhar Thiagarajan,Craig Boutilier,Rishabh Agarwal,Aviral Kumar,Aleksandra Faust
### Background
近年来的研究表明，有效利用推理时的计算资源对于提高大型语言模型（LLMs）的表现至关重要。本文研究了一种直接优化推理时策略性能的新颖微调范式。
### Innovation
提出了一种新的推理感知微调范式，通过该范式微调模型，直接优化推理时策略的性能。本文首次设计了针对Best-of-N（BoN）策略的模仿学习和强化学习方法，克服了BoN中的非分支.argmax操作符挑战。实验表明，本文方法能够有效提高BoN策略的表现和推理时的计算效率。
### Conclusion
在实验中，本文方法将Gemma 2B模型在Hendrycks MATH上的Bo32性能从26.8%提高到30.8%，pass@32从60.0%提高到67.0%，以及HumanEval上的pass@16从61.6%提高到67.1%。
## 338. `cs.CL` - Position-Aware Depth Decay Decoding ($D^3$): 提升大型语言模型推理效率 [PDF](https://arxiv.org/pdf/2503.08524), [HTML](https://arxiv.org/abs/2503.08524)
### Authors
Siqi Fan,Xuezhi Fang,Xingrun Xing,Peng Han,Shuo Shang,Yequan Wang
### Background
由于大型语言模型（LLMs）具有大量的参数，推理阶段资源密集。不同于传统的模型压缩需要重新训练，近期的动态计算方法显示，在推理中并非所有组件都是必要的，可以实现无需重新训练的管道。本文关注LLM生成的动态深度。通过观察预测较晚的词具有较低的困惑度，因此需要较少的计算，提出了一种基于位置感知的层跳过框架（1.5倍操作量节省同时保持性能）。
### Innovation
提出了一种无需训练的算法——位置感知深度衰减解码算法（$D^3$），利用幂律衰减函数来确定生成词 $T_i$ 时需保留的层数，从而在不重新训练的情况下，首次在广泛的语言生成任务中取得了成功。实验表明，$D^3$ 相对于全推理管道可以平均实现1.5倍的加速，且性能几乎无损失（<1%）。
### Conclusion
该研究在大型语言模型（Llama，7-700亿参数）上进行了实验，验证了$D^3$算法在保持性能的同时显著提高推理效率，对于同类研究是一个重要的贡献。
## 339. `cs.CL` - 为濒临灭绝语言的逻辑推理转移：通过样本高效语言理解进行语言融合 [PDF](https://arxiv.org/pdf/2504.02890), [HTML](https://arxiv.org/abs/2504.02890)
### Authors
Khanh-Tung Tran,Barry O'Sullivan,Hoang D. Nguyen
### Background
近期进展使得大规模语言模型（LLMs）能够通过生成链式推理（CoT）来解决推理任务，但这些进步大多集中在高资源语言上，而忽视了低资源语言。
### Innovation
1. 探究极低资源场景下的CoT技术，通过前期提示、模型编辑和微调等方法。2. 引入英语pivot CoT训练，利用LLM内部运作机制与主导语言对齐的洞察。3. 在数学推理基准测试中，此方法相比其他基准提高了最多28.33%。4. 分析和额外实验显示，明确分离语言理解与推理提高了跨语言推理能力。5. 发布LC2024，首个爱尔兰语数学任务基准，爱尔兰语是极度低资源且濒危的语言。
### Conclusion
本研究提供了一种实用路径，可以在数据稀缺的情况下，实现多语言推理，无需在每种极度低资源语言上进行大量重新训练。
## 340. `cs.CL` - A Survey on Inference Engines for Large Language Models: Perspectives on Optimization and Efficiency [PDF](https://arxiv.org/pdf/2505.01658), [HTML](https://arxiv.org/abs/2505.01658)
### Authors
Sihyeong Park,Sungryeol Jeon,Chaelyn Lee,Seokhun Jeon,Byung-Soo Kim,Jemin Lee
### Background
大型语言模型（LLMs）广泛应用于聊天机器人、代码生成和搜索引擎中。由于负载如链式推理、复杂推理和代理服务需要反复调用模型，导致推理成本显著增加。为降低这些成本，已采用并行、压缩和缓存等优化方法，然而，多样化的服务需求使得选择合适的优化方法变得困难。最近，专门的LLM推理引擎作为重要内容开始融入服务导向的基础设施中，但系统性的研究仍然不足。
### Innovation
本文对25个开源和商用推理引擎进行了全面评估，从使用便捷性、部署便捷性、通用支持、可扩展性和吞吐量和延迟感知计算的适用性等方面进行分析。此外，还探讨了每个推理引擎的设计目标以及它所支持的优化技术。研究了开源推理引擎的生态系统成熟度，处理了商用推理引擎的性能和成本政策，为研究人员和开发人员在选择和设计优化的LLM推理引擎方面提供了实际指导。
### Conclusion
本文指出了未来研究的方向，包括支持复杂的LLM服务、支持各种硬件和增强安全措施，为该快速发展的领域的研究人员和开发人员提供实用指导，并提供了一个公开的存储库以持续跟踪该领域的进展：<href>此链接</href>。
## 341. `cs.CL` - Co-NAML-LSTUR: 结合注意多视图学习和长短期用户表示的新闻推荐联合模型 [PDF](https://arxiv.org/pdf/2507.20210), [HTML](https://arxiv.org/abs/2507.20210)
### Authors
Minh Hoang Nguyen,Thuat Thien Nguyen,Minh Nhat Ta,Tung Le,Huy Tien Nguyen
### Background
新闻推荐系统在缓解信息过载方面发挥关键作用，通过提供个性化的内容。主要挑战在于同时建模新闻文章的多视图表示和捕捉用户的动态、双尺度兴趣，包括短期和长期偏好。现有方法往往依赖单一视图特征或未充分建模用户随时间的行为。
### Innovation
提出了一种名为Co-NAML-LSTUR的混合新闻推荐框架，它结合了NAML进行注意力驱动的多视图新闻编码和LSTUR进行分层用户建模，并设计用于在有限数据资源上进行训练。该方法利用BERT基础嵌入来提升语义表示。
### Conclusion
在MIND-small和MIND-large两个基准上评估Co-NAML-LSTUR模型，结果显示其明显优于强基线，相对于NRMS在AUC上提高了1.55%和在MRR上提高了1.15%，相对于NAML在AUC上提高了2.45%和在MRR上提高了1.71%。这些发现突显了我们这一注重效率的混合模型的有效性，结合了多视图新闻建模与双尺度用户表示，适用于资源有限的场景，而不会声称达到绝对的SOTA水平。该模型的实现已在公开代码库中提供。
## 342. `cs.CL` - BoundingDocs：包含空间注释的统一文档问答数据集 [PDF](https://arxiv.org/pdf/2501.03403), [HTML](https://arxiv.org/abs/2501.03403)
### Authors
Simone Giovannini,Fabio Coppini,Andrea Gemelli,Simone Marinai
### Background
该论文提出了一个统一的文档问答（Document QA）数据集，该数据集由多个与文档AI和视觉丰富文档理解（VRDU）相关的公开数据集合并而成。作者旨在为训练和评估大规模语言模型提供一个统一的资源。
### Innovation
本文的主要贡献有两个方面：首先，将现有的文档AI任务（如信息提取（IE））重新定义为问答任务，使其成为训练和评估大规模语言模型的合适资源；其次，发布所有文档的OCR并包含答案在文档图像中的精确位置为边界框。
### Conclusion
利用此数据集，作者研究了不同提示技术（可能包含边界框信息）对开放模型性能的影响，并确定了最有效的文档理解方法。
## 343. `cs.CL` - UITron-Speech: 基于语音指令的自动GUI代理 [PDF](https://arxiv.org/pdf/2506.11127), [HTML](https://arxiv.org/abs/2506.11127)
### Authors
Wenkang Han,Zhixiong Zeng,Jing Huang,Shu Jiang,Liming Zheng,Longrong Yang,Haibo Qiu,Chang Yao,Jingyuan Chen,Lin Ma
### Background
自主代理（agents）在图形用户界面（GUIs）中的应用正在改变人机交互的方式，但依赖于基于文本的指令限制了其在无障碍性和便利性方面的潜力，特别是在免提场景中。本文旨在解决这一问题，通过将语音作为GUI代理的指令输入方式，引入了第一款能够直接处理语音指令和设备截图以预测用户操作的端到端GUI代理——UITron-Speech。
### Innovation
本文提出了使用语音指令替代基于文本的指令的创新方法，并通过一个随机演讲者文本转语音模型合成了高质量的语音指令数据集。此外，设计了一种混合模态训练策略以缓解预训练基础模型中固有的模态不平衡问题，并提出了训练前两步定位校正方法来缓解小范围的定位偏差。
### Conclusion
大量实验表明，UITron-Speech 在多个基准上取得了稳健的性能和出色的适应性，证明了基于语音驱动的GUI代理在实现更易于访问和智能的人机交互方面的可行性和潜力。开源代码和数据集可在指定链接找到。
## 344. `cs.CL` - 通过无标注数据增强和反课程蒸馏提升大语言模型检测心理操控能力 [PDF](https://arxiv.org/pdf/2505.15255), [HTML](https://arxiv.org/abs/2505.15255)
### Authors
Yuansheng Gao,Han Bao,Tong Zhang,Bin Li,Jixiang Luo,Ronghao Chen,Zonghui Wang,Wenzhi Chen
### Background
心理操控是一种微妙但普遍存在的心理虐待形式，对心理健康构成严重威胁。然而，检测心理操控仍是一个研究较少的问题。该领域面临三大挑战：(i) 基本数据不足且难以获取；(ii) 心理操控的隐蔽性质，使检测变得困难；(iii) 缺乏真实世界的数据集。
### Innovation
本文提出了MentalMAC，这是一个新颖的框架，旨在增强大规模语言模型检测多轮对话中心理操控元素的能力。该方法包括三个关键组件：EvoSA（无标注数据增强方法，基于进化操作和言语行为理论）；教师模型生成的多任务监督；以及逐级任务水平反课程蒸馏。
### Conclusion
研究构建了包含5000个真实对话样本的ReaMent数据集，使用MentalMAC提炼的模型辅助人工标注。大量实验表明，MentalMAC在F1mac和准确率上分别比最佳基线高出25.9%和8.1%，且优于商业LLM如GPT-4和Claude-3.5-Sonnet。
## 345. `cs.CL` - 现代日语中依赖距离和层次距离的分布及其影响因素 [PDF](https://arxiv.org/pdf/2504.21421), [HTML](https://arxiv.org/abs/2504.21421)
### Authors
Linxuan Wang,Shuiyuan Yu
### Background
本文探索了日语中依赖距离（DD）与层次距离（HD）之间的关系。研究者通过比较固定和未固定句子长度条件下DD和HD的概率分布，以及分析随着句子长度增加时MDD和MHD的变化，并借助平衡的现代日语书面语语料库进行相关系数分析。研究表明，谓词的价是MDD与MHD之间权衡关系背后的因素。
### Innovation
本文首次在现代日语书面语中系统地探讨了依赖距离和层次距离的关系，并且强调了谓词价在调节线性复杂度和层次复杂度中的关键作用。此外，研究发现谓词价对层次距离（HD）分布的影响大于对依赖距离（DD）分布的影响，导致它们的概率分布有所不同，进而使得MDD的均值低于MHD的均值。
### Conclusion
本研究发现，日语使用者通过调节谓词的价来平衡线性复杂度和层次复杂度。当谓词价达到阈值时，MDD和MHD的相对大小会有所不同。除了认知负荷，谓词的价还会对DD和HD的概率分布产生影响。
## 346. `cs.CL` - 在实际低资源环境中改进视觉提示关键词定位 [PDF](https://arxiv.org/pdf/2409.06013), [HTML](https://arxiv.org/abs/2409.06013)
### Authors
Leanne Nortje,Dan Oneata,Gabriel Pirlogeanu,Herman Kamper
### Background
视觉提示关键词定位（VPKL）的目标是在给定图片查询时，在语音集合中找到图片中所描绘词的出现情况。当前已有的研究显示，VPKL可以用由成对图片和未标记语音训练的视觉锚定语音模型来实现，但是所有实验仅在英语上进行，并且使用转录来获取对比损失的正负样本对。研究者注意到，在英语上这一方法表现稳定，但在实际低资源语言上，特别是如约鲁巴这样的未书写语言中，表现不尽人意。
### Innovation
该论文提出了无监督的几个样本学习方案，能够在无需转录的情况下自动挖掘正负样本对。通过此方法在英语上的分析相比使用真实注释样本的性能只略有下降，并首次在实际的低资源语言约鲁巴语中进行了VPKL实验，发现对比使用真实样本的方法，挖掘策略在约鲁巴语中的准确度较低，导致性能出现了较大幅度的下降。
### Conclusion
该研究在英语与约鲁巴语中验证了新的VPKL方法的有效性，虽然在英语上基本无显著差异，但在低资源语言约鲁巴语中，由于采样策略的限制，其性能有所下降，但整体改进了VPKL在实际低资源环境中的应用。
## 347. `cs.CL` - 知识图谱检索中的结构-内容权衡 [PDF](https://arxiv.org/pdf/2506.13380), [HTML](https://arxiv.org/abs/2506.13380)
### Authors
Valentin Six,Evan Dufraisse,Gaël de Chalendar
### Background
大型语言模型（LLMs）越来越多地依赖知识图谱来进行事实推理，但检索设计如何影响其表现尚不清楚。我们研究了问题分解如何改变检索到的子图的内容和结构。使用一种混合检索函数来控制初始问题和子问题的重要性，研究显示，基于子问题的检索提高了内容精度，但产生了不连贯的子图，而基于问题的检索保持了结构，但相关性较低。这些极端之间的最佳性能揭示了平衡检索内容和结构对有效利用结构化知识进行LLM推理至关重要。
### Innovation
研究提出了一种混合检索函数，能够控制初始问题和子问题的重要性。研究发现，基于子问题的检索提高了内容的精确度，但带来了不连贯的子图；而基于问题的检索保持了结构，但降低了相关性。研究揭示了在大型语言模型针对结构化知识进行推理时，平衡检索内容和结构的重要性。
### Conclusion
研究表明，在基于大型语言模型的知识图谱检索中，实现检索内容和结构的最佳平衡至关重要。这种权衡在基于子问题的检索和基于问题的检索之间达到了最优，证明了构建有效知识推理的关键在于平衡检索的结构与内容。
## 348. `cs.CL` - Web-Shepherd：提升强化网络代理的PRM [PDF](https://arxiv.org/pdf/2505.15277), [HTML](https://arxiv.org/abs/2505.15277)
### Authors
Hyungjoo Chae,Sunghwan Kim,Junhee Cho,Seungone Kim,Seungjun Moon,Gyeom Hwangbo,Dongha Lim,Minjin Kim,Yeonjun Hwang,Minju Gwak,Dongwook Choi,Minseok Kang,Gwanhoon Im,ByeongUng Cho,Hyojun Kim,Jun Hee Han,Taeyoon Kwon,Minju Kim,Beong-woo Kwak,Dongjin Kang,Jinyoung Yeo
### Background
网页导航是一个独特的领域，能够自动化许多重复的现实任务，但同时也具有挑战性，因为它需要超出普通多模态大型语言模型（MLLM）任务的长时序序列决策。以往的工作中，虽然已经认识到速度和成本效益的重要性，但此前仍旧缺乏能够在训练和测试过程中使用的专门奖励模型。利用大规模语言模型作为奖励模型的方法会在实际部署中带来显著的限制。
### Innovation
本文提出了第一个用于网页导航评估的过程奖励模型（PRM）——Web-Shepherd，在步骤级别评估网页导航轨迹。为了实现这一目标，作者构建了WebPRM Collection大规模数据集（包含40000个步骤级别的偏好对和注释检查表，涵盖多种领域和难度级别）。此外，还引入了WebRewardBench，这是首个用于评估PRM的元评价基准。实验结果显示，Web-Shepherd在WebRewardBench上的准确率比使用GPT-4o高出约30个点。当使用GPT-4o-mini作为策略并通过Web-Shepherd验证时，表现提升了10.9个点，并且成本降低了10。
### Conclusion
本文开发了Web-Shepherd来专门评估网页导航，通过自建的数据集和评估基准验证了其有效性。模型、数据集和代码已对外开放。
## 349. `cs.CL` - 基于心理学的统一动态课程学习框架 [PDF](https://arxiv.org/pdf/2408.05326), [HTML](https://arxiv.org/abs/2408.05326)
### Authors
Guangyu Meng,Qingkai Zeng,John P. Lalor,Hong Yu
### Background
直接从不同难度级别的示例中学习对人类和机器学习模型都是具有挑战性的，一种更有效的策略是从简单到复杂地按顺序呈现示例。课程学习（CL）提出了这种策略，但在CL的设计中仍存在两个关键挑战：定义训练数据的难度和确定每个训练步骤的合适数据量。本文借鉴心理学领域的方法，利用项目反应理论（IRT）和人工众包（AC）来量化训练数据的难度，并提出了动态数据选择通过模型能力估计（DDS-MAE）来调度训练过程中数据的使用量。
### Innovation
提出了心理学背景下的统一动态课程学习框架（PUDF），采用IRT和AC方法量化训练数据的难度，并基于一致的理论（如IRT）实现模型能力估计，从而使得这些值在同一范围内具有可比性，有助于数据选择与更快收敛。此外，提出了基于模型能力估计的动态数据选择策略（DDS-MAE）。实验结果显示，使用PUDF微调预训练语言模型比标准微调和最先进的CL方法在多种基准数据集上具有更高的准确性和更快的收敛性。
### Conclusion
研究表明，采用PUDF进行预训练语言模型的调整，与标准调整方法和其他CL方法相比，具有更高的准确性和更快的收敛性。此外，消除实验和下游分析进一步验证了PUDF对CL的影响。
## 350. `cs.CL` - 高效 LLMs 的扩展 [PDF](https://arxiv.org/pdf/2402.14746), [HTML](https://arxiv.org/abs/2402.14746)
### Authors
B.N. Kausik
### Background
近年来，大型语言模型 (LLMs) 包含数百亿参数，消耗了巨大的资源。根据名为“AI 放大规模定律”的假设，Transformer 的参数数量需要线性地与数据大小成比例。鉴于此，研究者探讨如何开发参数数量最少但仍能实现训练语料库所需精度的有效 LLM。通过对比 Kullback-Leibler 散度的理论与实测估计，他们推导出一个自然的 AI 放大规模定律，即有效 LLM 的参数数量与训练数据大小的比例关系为 $D^{frac{u}{1}}$，其中 $u otin [0.44, 0.72]$，表明存在更高效的架构。
### Innovation
本文提出了递归 Transformer，这是一种结合了 Transformer 有效性和递归网络效率的模型。递归 Transformer 按固定宽度的滑动窗口逐层处理输入序列。递归 Transformer 具有以下特点：(1) 在序列长度上运行的时间复杂度为线性；(2) 记忆效率高，适用于大规模并行处理；(3) 对于语言任务可以学习忘记历史，对于长距离任务如复制和选择性复制可以积累历史；(4) 可用于课程学习以克服梯度消失问题。实验结果显示，递归 Transformer 在基准测试中表现出色。
### Conclusion
递归 Transformer 提供了一种新的高效 LLM 架构，证明了在保持竞争力的同时，可以通过减少参数数量来达到更高的效率。根据实验结果，递归 Transformers 在测量基准中表现良好，展现了更高效率的潜力。
## 351. `cs.CL` - 使用概念学习数据集在大规模语言模型中发现隐含偏差 [PDF](https://arxiv.org/pdf/2510.01219), [HTML](https://arxiv.org/abs/2510.01219)
### Authors
Leroy Z. Wang
### Background
本文介绍了一个概念学习任务的数据集，旨在揭示大规模语言模型中的隐含偏差。通过在上下文中的概念学习实验发现，语言模型可能倾向于在量化词上表现出向上单调性这种偏差；而在不包含概念学习组件的直接提示测试中，这种偏差则不那么明显。这显示了利用上下文中的概念学习是发现语言模型隐含偏差的有效方式。
### Innovation
本文通过创建一个概念学习任务的数据集，揭示了大规模语言模型中的隐含偏差，并通过对比实验展示了上下文中的概念学习可以有效发现语言模型的隐含偏差。
### Conclusion
语言模型在量化词上可能表现出向上单调性的偏差，这种偏差在概念学习实验中较为明显，但在直接测试中不那么显著。上下文中的概念学习可以作为一种有效方法来发现语言模型中的隐含偏差。
## 352. `cs.CL` - Prompt-R1：通过端到端的强化学习实现协作自动提示框架 [PDF](https://arxiv.org/pdf/2511.01016), [HTML](https://arxiv.org/abs/2511.01016)
### Authors
Wenjin Liu,Haoran Luo,Xueyuan Lin,Haoming Liu,Tiesunlong Shen,Jiapu Wang,Rui Mao,Erik Cambria
### Background
近年来，大型语言模型（LLMs）的发展速度越来越快。然而，当处理复杂问题时，大多数用户无法提供准确和有效的提示与LLMs交互，从而限制了LLMs的性能。
### Innovation
提出了一种端到端的强化学习框架Prompt-R1，通过小型LLM与大型LLM协作，替代用户交互来更好地解决问题。采用多轮提示交互的方式，小型LLM负责思考和生成提示，大型LLM负责复杂的推理。设计了双重约束奖励，优化正确性、生成质量和推理准确性。Prompt-R1提供了一个即插即用的框架，支持多种大型LLM的推理和训练。实验结果表明，Prompt-R1在多个公开数据集上显著优于基础模型。
### Conclusion
Prompt-R1显著提升了复杂问题的处理能力，提供了一种高效的解决方案，支持多种大型LLM的灵活性，并在网络可用。
## 353. `cs.CL` - AdvancedIF：基于评分标准的基准测试和逐步强化学习以提高大语言模型指令跟随能力 [PDF](https://arxiv.org/pdf/2511.10507), [HTML](https://arxiv.org/abs/2511.10507)
### Authors
Yun He,Wenzhe Li,Hejia Zhang,Songlin Li,Karishma Mandyam,Sopan Khosla,Yuanhao Xiong,Nanshu Wang,Xiaoliang Peng,Beibin Li,Shengjie Bi,Shishir G. Patil,Qi Qi,Shengyu Feng,Julian Katz-Samuels,Richard Yuanzhe Pang,Sujan Gonugondla,Hunter Lang,Yue Yu,Yundi Qian,Maryam Fazel-Zarandi,Licheng Yu,Amine Benhalloum,Hany Awadalla,Manaal Faruqui
### Background
大语言模型（LLMs）在多种任务上的表现令人印象深刻，但是复杂的多轮对话和系统提示下的指令遵循能力仍然是一个重大挑战。严格的评估和有效的训练因缺乏高质量的人注释基准和可信赖的、可解释的奖励信号而受到阻碍。
### Innovation
引入了AdvancedIF基准测试，这一测试包含超过1600个指令和专家定制的评分标准，用于评估模型复杂、多轮且系统级别的指令遵循能力。提出了一个名为RIFL的新型后训练流水线，利用评分标准生成、微调评分标准验证器和奖励塑形技术，以实现有效的指令遵循强化学习。实验结果证实，RIFL显著提高了模型的指令遵循能力，且在公共基准上也取得了良好效果。
### Conclusion
本项工作证实评分标准是训练和评估LLMs高级指令遵循能力的强大工具，为更强大和可靠的人工智能系统铺平了道路。
## 354. `cs.CL` - 通过基于转写的技术微调探索跨语言知识迁移对于濒临低资源的恰克玛语言的影响 [PDF](https://arxiv.org/pdf/2510.09032), [HTML](https://arxiv.org/abs/2510.09032)
### Authors
Adity Khisa,Nusrat Jahan Lia,Tasnim Mahfuz Nafis,Zarif Masud,Tanzir Pial,Shebuti Rayana,Ahmedul Kabir
### Background
恰克玛是一种印度-雅利安语系的语言，由于可用数据有限，它在语言模型中仍处于严重不足的状态。
### Innovation
作者创建了一个上下文连贯的孟加拉转写恰克玛语语料库，由母语使用者验证，用于微调六种基于编码器的转换单词模型，包括多语言（mBERT，XLM-RoBERTa，DistilBERT），区域（孟加拉语BERT，印度语BERT）和单语言英语（DeBERTaV3）变体。实验结果表明，微调后的多语言模型在适应孟加拉转写恰克玛时优于其预训练版本，准确率达到73.54%，困惑度为2.90。进一步分析强调了数据质量对模型性能的影响，并展示了OCR流水线对形态丰富的印度语脚本的限制。
### Conclusion
研究证明，孟加拉转写恰克玛可以非常有效地用于恰克玛语的迁移学习，并且作者发布了数据集以促进对低资源语言的多语言语言建模的研究。
## 355. `cs.CL` - CLaRa：通过连续潜推理连接检索与生成 [PDF](https://arxiv.org/pdf/2511.18659), [HTML](https://arxiv.org/abs/2511.18659)
### Authors
Jie He,Richard He Bai,Sinead Williamson,Jeff Z. Pan,Navdeep Jaitly,Yizhe Zhang
### Background
检索增强生成（RAG）提升了大型语言模型（LLM）的外部知识能力，但由于长上下文和检索生成优化分离的问题，其性能仍有待提高。
### Innovation
CLaRa 提出了一种统一框架，该框架在共享的连续空间中进行嵌入式压缩和联合优化。引入了基于 QA 和同义替换监督的 SCP（关键保持数据合成框架），以获得具有丰富语义的可检索压缩向量。CLaRa 通过单一的语言模型损失对重新排名器和生成器进行端到端训练，通过可微分的 top-k 估计器使梯度能够穿过两个模块。
### Conclusion
在多个 QA 基准测试中的实验表明，CLaRa 实现了最佳的压缩和重新排名性能，通常超过基于文本的微调基线。
## 356. `cs.CL` - CAMERA：通过微专家冗余分析进行MoE模型的多矩阵联合压缩 [PDF](https://arxiv.org/pdf/2508.02322), [HTML](https://arxiv.org/abs/2508.02322)
### Authors
Yuzhuang Xu,Xu Han,Yuanchi Zhang,Yixuan Wang,Yijun Liu,Shiyu Ji,Qingfu Zhu,Wanxiang Che
### Background
大型语言模型（LLMs）带有Mixture-of-Experts（MoE）架构，在多种任务中表现出色，但随着参数的增加，它也面临着显著的计算和存储开销。MoE模型的性能优势并不与专家参数的增长成正比。此前的研究通过对专家级别进行剪枝、合并或分解来减少参数，但在性能和计算效率方面仍然存在问题。
### Innovation
本文通过引入微专家作为跨矩阵的更细粒度压缩单元来解决这些挑战。作者提出了CAMERA框架，这是一种轻量且无需训练的方法，用于识别微专家冗余，并展示了在九个下游任务上的一系列实验结果。通过CAMERA-P，作者提出了一种结构化的微专家剪枝框架，并通过CAMERA-Q设计了一种针对微专家的混合精度量化方法。实验表明，在20%到60%的剪枝比例下，CAMERA-P始终优于强劲的基准。CAMERA-Q在极端的2位量化中获得了更优的结果，超越了现有矩阵和通道级别方法。作者的方法使单个NVIDIA A100-40GB GPU上可以对Qwen2-57B-A14B进行不到5分钟的完全微专家分析。
### Conclusion
 extensive experiments on nine downstream tasks show that CAMERA-P consistently outperforms strong baselines under pruning ratios ranging from 20% to 60%. Furthermore, CAMERA-Q achieves superior results under aggressive 2-bit quantization, surpassing existing matrix- and channel-level ideas. Notably, our method enables complete micro-expert analysis of Qwen2-57B-A14B in less than 5 minutes on a single NVIDIA A100-40GB GPU.
## 357. `cs.CL` - 预训练语言模型在通用文本嵌入中的作用：综述 [PDF](https://arxiv.org/pdf/2507.20783), [HTML](https://arxiv.org/abs/2507.20783)
### Authors
Meishan Zhang,Xin Zhang,Xinping Zhao,Shouzheng Huang,Baotian Hu,Min Zhang
### Background
文本嵌入因其在广泛自然语言处理（NLP）任务中的效果而引起了越来越多的关注，包括检索、分类、聚类、双语对准和总结。随着预训练语言模型（PLMs）的出现，通用文本嵌入（GPTE）因其能够产生丰富的可迁移表示而受到高度重视。GPTE的一般架构通常通过PLMs来提取密集的文本表示，并通过大规模的配对数据集上的对比学习进行优化。
### Innovation
本文综述了PLMs在GPTE中的作用，涵盖了基础架构和高级功能，如多语言支持、多模态集成、代码理解以及情景特定适应。还指出了超越传统改进目标的潜在未来研究方向，包括排名集成、安全性考虑、偏见缓解、结构信息整合及嵌入的认知扩展。
### Conclusion
本文旨在为新入门者和资深研究者提供理解和展望GPTE现状及未来潜力的宝贵参考资料。
## 358. `cs.CL` - AICC：使用模型基础的HTML解析器精析HTML，提升模型性能——构建7.3万亿AI就绪语料库 [PDF](https://arxiv.org/pdf/2511.16397), [HTML](https://arxiv.org/abs/2511.16397)
### Authors
Ren Ma,Jiantao Qiu,Chao Xu,Pei Chu,Kaiwen Liu,Pengli Ren,Yuan Qu,Jiahui Peng,Linfeng Hou,Mengjie Liu,Lindong Lu,Wenchang Ning,Jia Yu,Rui Min,Jin Shi,Haojiong Chen,Peng Zhang,Wenjian Zhang,Qian Jiang,Zengjie Hu,Guoqiang Yang,Zhenxiang Li,Fukai Shang,Runyuan Ma,Chenlin Su,Zhongying Tu,Wentao Zhang,Dahua Lin,Conghui He
### Background
在大型语言模型中，网页数据的质量至关重要。然而，大多数数据治理工作仅关注过滤和去重，而将HTML到文本的提取视为一个静态预处理步骤。现有的网页语料库依赖于基于启发式的提取器，如Trafilatura，它们难以保留文档结构，经常损坏诸如公式、代码和表格等结构性元素。我们假设提高提取质量可能和激进的过滤策略一样对下游性能产生重要影响。
### Innovation
我们提出了一种名为MinerU-HTML的新型提取管道，将其内容提取问题重新定义为由0.6亿参数的语言模型解决的序列标记问题。与基于文本密度的启发式方法不同，MinerU-HTML利用语义理解，并采用两阶段格式化流程，首先明确分类语义元素，然后转换为Markdown。基于其模型驱动的方法，MinerU-HTML在提高标注网页结构元素保留度（代码块90.9%，公式94.0%）方面具备内在的可扩展性，而启发式方法则提供有限的改进途径。通过构建AICC（AI-ready Common Crawl），一个基于两个Common Crawl快照的7.3万亿词汇量多语言语料库，AICC在筛选实验中展示了提取质量对模型能力的显著影响。
### Conclusion
我们通过AICC实验证明，HTML提取是网页语料库构建的重要，甚至未被充分重视的组成部分。通过MinerU-HTML，我们展示了如何通过重新构建网页提取流程来显著提升模型性能。我们还公开了MainWebBench，MinerU-HTML以及AICC的数据集，为语言模型的训练和评估提供了重要资源。
## 359. `cs.CL` - Mem-PAL: 基于记忆的长期用户-代理个性化对话助手 [PDF](https://arxiv.org/pdf/2511.13410), [HTML](https://arxiv.org/abs/2511.13410)
### Authors
Zhaopei Huang,Qifeng Dai,Guozheng Wu,Xiaopeng Wu,Kehan Chen,Chuan Yu,Xubin Li,Tiezheng Ge,Wenxuan Wang,Qin Jin
### Background
随着智能个人设备的兴起，面向服务的人机交互变得越来越普遍。这凸显出对能够根据用户特定特质准确解释要求并呈现个性化响应的个性化对话助手的需求。然而，现有的方法通常忽略了长期交互的复杂性，未能捕捉用户的主观特征。
### Innovation
我们提出了一个名为PAL-Bench的新基准，用于评估服务导向的助手在长期用户-代理交互方面的个性化能力。为此，我们开发了一个基于多步骤LLM（大型语言模型）合成流水线，该流水线通过人类注释者的验证和细化而进一步完善。此外，我们还提出了一个分层和异构的记忆框架H$^2$Memory，结合检索增强生成，以改善个性化响应生成。通过我们在PAL-Bench和外部数据集上的全面实验表明，所提出的记忆框架是有效的。
### Conclusion
我们的研究结果表明，PAL-Bench数据集和H$^2$Memory框架能够有效地评估和提高面向服务的个性化对话助手在长期用户-代理交互中的表现。
## 360. `cs.CL` - 联邦大语言模型：当前进展与未来方向 [PDF](https://arxiv.org/pdf/2409.15723), [HTML](https://arxiv.org/abs/2409.15723)
### Authors
Yuhang Yao,Jianyi Zhang,Junda Wu,Chengkai Huang,Yu Xia,Tong Yu,Ruiyi Zhang,Sungchul Kim,Ryan Rossi,Ang Li,Lina Yao,Julian McAuley,Yiran Chen,Carlee Joe-Wong
### Background
大语言模型因其卓越的效果而迅速获得青睐，并广泛应用于实际场景。尽管高质量的训练数据至关重要，但在数据收集过程中可能会引发隐私问题。为了解决这一问题，联邦学习提供了一种方案，在这种方案下，多个客户端可以协同训练大语言模型，同时无需共享本地数据。然而，联邦学习也带来了新的挑战，例如由于数据异构性引起的模型收敛问题以及高昂的通信成本。需进行全面研究来解决这些问题并指导未来的研究。
### Innovation
本文概述了联邦学习在大语言模型（FedLLM）中的应用，回顾了近期进展并指出了未来的研究方向。文章重点探讨了联邦学习场景下的模型微调和提示学习两个关键方面，同时讨论了现有的研究工作以及所面临的研究挑战。
### Conclusion
本文提出了联邦大语言模型的潜在方向，包括预训练、联邦代理以及适用于联邦学习的大语言模型在内的三个方向。
## 361. `cs.CL` - DR Tulu: Reinforcement Learning with Evolving Rubrics for Deep Research [PDF](https://arxiv.org/pdf/2511.19399), [HTML](https://arxiv.org/abs/2511.19399)
### Authors
Rulin Shao,Akari Asai,Shannon Zejiang Shen,Hamish Ivison,Varsha Kishore,Jingming Zhuo,Xinran Zhao,Molly Park,Samuel G. Finlayson,David Sontag,Tyler Murray,Sewon Min,Pradeep Dasigi,Luca Soldaini,Faeze Brahman,Wen-tau Yih,Tongshuang Wu,Luke Zettlemoyer,Yoon Kim,Hannaneh Hajishirzi,Pang Wei Koh
### Background
当前的深度研究模型通过强化学习与验证奖励（RLVR）训练于易于验证的短问答任务，但这种训练方式无法扩展到现实中的长形式任务。现有的开放深度研究模型主要集中在小步骤、验证性答案生成上。
### Innovation
提出了一种新的训练方法——演化评分标准下的强化学习（RLER），通过在训练过程中构建和维护与策略模型一同进化的评分标准，使模型能够提供辨别性、策略性反馈，并直接训练用于开放性、长形式的深度研究的模型——Deep Research Tulu (DR Tulu-8B)。
### Conclusion
DR Tulu在四个长形式深度研究基准测试中超过了现有的开放深度研究模型，表现甚至超过了专有的深度研究系统，同时模型更小且查询成本更低。为了促进未来研究，DR Tulu的所有数据、模型和代码都被公开，包括基于MCP的新代理基础设施，为深度研究系统提供支持。
## 362. `cs.CL` - MTA：一种面向个性化大型语言模型的合并-适应框架 [PDF](https://arxiv.org/pdf/2511.20072), [HTML](https://arxiv.org/abs/2511.20072)
### Authors
Xiaopeng Li,Yuanjin Zheng,Wanyu Wang,wenlin zhang,Pengyue Jia,Yiqi Wang,Maolin Wang,Xuetao Wei,Xiangyu Zhao
### Background
个性化大型语言模型（PLLMs）旨在使模型输出与个别用户偏好对齐，对于以用户为中心的应用至关重要。然而，常见的做法——为每个用户单独训练一个模块，面临两个主要限制：（1）存储成本随着用户数量的线性增长，使其办法难以扩展；（2）从头开始微调静态模型通常会导致数据稀疏用户的性能不佳。
### Innovation
我们提出了一种名为MTA（Merge-then-Adapt）的框架来解决上述问题。MTA框架包含三个关键阶段：（1）构建共享Meta-LoRA银行，通过选取锚点用户并进行元个性化预训练；（2）引入可扩展的自适应LoRA融合阶段，该阶段动态检索并合并与特定用户需求最相关的锚点LoRA，实现灵活的个性化调整，无需为每个用户单独存储；（3）提出LoRA堆叠用于少量样本个性化阶段，该阶段在合并后的LoRA上附加一个极低秩、轻量级的LoRA模块，在少量样本下进行微调，以实现有效的个性化。
### Conclusion
在LaMP基准测试上的详尽实验表明，我们的方法在多种任务中优于现有最先进的方法。
## 363. `cs.CL` - 昨日的新闻：多维度评估虚假信息检测模型的跨分布外一般化基准 [PDF](https://arxiv.org/pdf/2410.18122), [HTML](https://arxiv.org/abs/2410.18122)
### Authors
Ivo Verhoeven,Pushkar Mishra,Ekaterina Shutova
### Background
虚假信息随着时间迅速变化，远快于审核人员能够大规模标注的速度，导致训练数据和推理数据分布发生偏移。这使得现有的虚假信息检测器缺乏跨分布外一般化的能力，这是其当前的一个重要缺陷。我们通过使用离散标注来模拟虚假信息内容中的协变量偏移，设定了一个基准数据集，以评估模型在不同维度（时间、事件、主题、出版商、政治倾向、虚假信息类型）上的跨分布外一般化能力。
### Innovation
开发了一个名为misinfo-general的新基准数据集，用于评估虚假信息检测模型在跨分布外一般化上的能力。利用文章元数据展示现有模型如何满足期望，而这些通过分类指标可能看不到。此外，通过分析数据属性以确保最小存在建模捷径。
### Conclusion
该研究提供了一个公开可用的数据集及配套代码，旨在改善虚假信息检测模型的跨分布外一般化能力，有助于识别和纠正模型中可能存在捷径的现象，并推动这一领域的研究进步。
## 364. `cs.CL` - 超越内省：通过外部行为反馈强化思考 [PDF](https://arxiv.org/pdf/2501.01457), [HTML](https://arxiv.org/abs/2501.01457)
### Authors
Diji Yang,Linda Zeng,Kezhen Chen,Yi Zhang
### Background
在推理时，大型语言模型（LLMs）能够处理复杂问题，但其长时间的思考过程可能会因为模型的统计性质而不稳定或不一致，尤其是在知识边界附近。现有的方法试图通过让模型自我批评来修正其推理过程中的错误，但这种方式会继承初始输出的偏见，称为内省错觉。为了超越这种内省，本文借鉴了动物学中核心方法，提出了一种外部主义的三步框架——提纯-强化-推理（Distillation-Reinforcement-Reasoning，DRR）。DRR不依赖于模型的内省，而是评估其可观察的行为，提供纠正性反馈。DRR 首先对推理器的行为痕迹进行提纯，然后训练一个轻量级的外部辨别模型（DM）。推理时，DM 扮演批评者的角色，识别并拒绝可疑的推理步骤。外部反馈促使LLM抛弃有缺陷的路径并探索替代方案，从而提高推理质量而不改变基础模型。
### Innovation
本文提出了一个基于外部主义的三步框架——提纯-强化-推理（DRR），该框架通过评估模型的行为来提供纠正性反馈，而不是依赖模型的自我内省。DRR 先提纯推理器的行为痕迹，然后使用轻量级的外部辨别模型对推理过程进行监督，识别并驳斥不可靠的推理步骤，促使模型自我修复并探索新的路线。DRR 的轻量级设计和无需标注的优点使得其可以为各种 LLM 提供一个可扩展和灵活的解决方案，以提高推理的可靠性。
### Conclusion
实验表明，本文提出的 DRR 框架在多个推理基准测试中显著优于现有的自我批评方法。DRR 提供了一种轻量化、无需标注的解决方案，为大规模的 LLM 提高推理可靠性和适应性提供了可扩展支持。
## 365. `cs.CL` - CAPability: 一个评估视觉语句生成正确性和完整性综合基准 [PDF](https://arxiv.org/pdf/2502.14914), [HTML](https://arxiv.org/abs/2502.14914)
### Authors
Zhihang Liu,Chen-Wei Xie,Bin Wen,Feiwu Yu,Jixuan Chen,Pandeng Li,Boqiang Zhang,Nianzu Yang,Yinglu Li,Zuan Gao,Yun Zheng,Hongtao Xie
### Background
随着现代多模态大型语言模型（MLLMs）的出现，视觉标题基准已经过时。现有的基准依赖于简洁的地面真实句子和传统评估指标，无法有效评估详细的标题。尽管最近的基准试图通过关注关键词提取或以对象为中心的评估来解决这一问题，但仍然局限于模糊视角或对象视角的分析，并且视觉元素的覆盖不完整。
### Innovation
该论文提出了一种名为CAPability的综合多视角基准，用以评估视觉标题生成的12个维度，涵盖了六个关键视角。它收集了近11000张由人类注释的图像和视频，并对其进行视觉元素注释，以评估生成的标题。CAPability使用精确度和命中率指标稳定地评估标题的正确性和完整性。通过将注释转换为问答对，引入了一种启发式的度量方法，‘知道但不能说’(K通俗表现)，表明问答能力和标题生成能力之间的显著性能差距。
### Conclusion
我们的工作提供了对MLLMs标题生成能力的全面分析，识别了其在各种维度上的优势和劣势，为未来研究指出了增强特定能力的研究方向。
## 366. `cs.CL` - 如何开始对齐？扩散大语言模型可能需要一个不同的位置 [PDF](https://arxiv.org/pdf/2508.12398), [HTML](https://arxiv.org/abs/2508.12398)
### Authors
Zhixin Xie,Xurui Song,Jun Luo
### Background
最近，扩散大语言模型（dLLMs）由于其独特训练和推理方法成为非自回归范式中的竞争技术。然而，目前尚未对此新型架构进行安全性研究。该论文首次分析了dLLMs的安全性能，并提出了一种针对其独特生成特性的新型安全对齐方法。
### Innovation
论文识别了dLLMs中防御者和攻击者之间的关键不对称性。为了利用这种不对称性，作者引入了Middle-tOken Safety Alignment（MOSA）方法，该方法通过强化学习直接对齐模型的中间生成与安全拒绝。这项工作通过实验证明了MOSA方法在安全性方面的优越性。
### Conclusion
实验结果有力地证明了MOSA方法在安全性方面的优越性，并测试了MOSA对齐后的dLLM在编程、数学和一般推理任务中的实用性。
## 367. `cs.CL` - BengaliFig: 一种针对孟加拉语隐喻性和文化背景推理的低资源挑战 [PDF](https://arxiv.org/pdf/2511.20399), [HTML](https://arxiv.org/abs/2511.20399)
### Authors
Abdullah Al Sefat
### Background
大型语言模型在多语言基准测试中表现出色，但在形象性和文化背景推理方面，尤其是在低资源环境中，仍缺乏广泛的评估，特别是对于孟加拉语等广泛使用的低资源语言。本研究旨在填补这一空白，推出BengaliFig挑战集，包含435个来自孟加拉语口头和文学传统的独特谜题，每个谜题从五个维度（推理类型、陷阱类型、文化深度、答案类别和难度）进行了标注，并通过AI辅助的约束感知管道自动转换为选择题格式。
### Innovation
本工作创新地提出了BengaliFig，一个专门用于形象性和文化背景推理的低资源语言（孟加拉语）挑战集。通过五个维度的详细标注和AI辅助的自动转换流程，该挑战集能够有效评估大型语言模型在低资源文化环境中的鲁棒性，从而推动自然语言处理评价的包容性和文化意识。
### Conclusion
BengaliFig为评估大型语言模型在低资源文化环境中的鲁棒性提供了一个诊断探针，并为实现包容性和遗产意识的自然语言处理评估迈出了重要一步。实验表明，八种领先的大型语言模型在形象性和文化特定推理方面表现出了明显的弱点，这进一步验证了该挑战集的有效性。
## 368. `cs.CL` - LightMem: 轻量级且高效的记忆增强生成系统 [PDF](https://arxiv.org/pdf/2510.18866), [HTML](https://arxiv.org/abs/2510.18866)
### Authors
Jizhan Fang,Xinle Deng,Haoming Xu,Ziyan Jiang,Yuqi Tang,Ziwen Xu,Shumin Deng,Yunzhi Yao,Mengru Wang,Shuofei Qiao,Huajun Chen,Ningyu Zhang
### Background
尽管大型语言模型（LLMs）具有卓越的能力，但它们在动态和复杂环境中难以有效利用历史交互信息。现有的内存系统通过引入持久的信息存储、检索和利用机制，帮助LLMs摆脱了无状态交互的局面，但这些系统的存在往往会导致大量的时间与计算开销。
### Innovation
LightMem是一个新的内存系统，旨在平衡内存系统的性能和效率。它受到人类记忆模型的启发，将记忆分为三个互补阶段：认知启发的感觉记忆通过轻量化压缩快速过滤掉无关信息，并按主题对信息进行分组；再通过主题意识的短时记忆对基于主题的组进行整合和总结，以实现更结构化的访问；最后，带有睡眠时间更新的长期记忆采用离线程序，在线推理与巩固脱钩。
### Conclusion
在LongMemEval和LoCoMo测试中，使用GPT和Qwen作为主干模型，LightMem在知识问答准确性、总标记使用量和API调用次数方面都超过了强基线，分别提高了7.7%/29.3%和29.3%，并减少了总标记使用量多达38倍/20.9倍和API调用次数高达30倍/55.5倍。纯在线测试时，LightMem还实现了更高的标记减少率和API调用减少率，分别达到了106倍/117倍和159倍/310倍。LightMem的代码可以在提供的链接中找到。
## 369. `cs.CL` - LogicOCR：大型多模态模型在图文丰富图像上的逻辑推理能力如何？ [PDF](https://arxiv.org/pdf/2505.12307), [HTML](https://arxiv.org/abs/2505.12307)
### Authors
Maoyuan Ye,Haibin He,Qihuang Zhong,Jing Zhang,Juhua Liu,Bo Du
### Background
大型多模态模型（LMMs）在OCR能力上取得了显著进步，但在处理富含文本的图像时的复杂逻辑推理能力尚待探索。
### Innovation
本文提出了LogicOCR，一个包含2780个问题的基准，分为逻辑推理生成（LogicOCR-Gen）和逻辑推理真实（LogicOCR-Real）两个子集，分别针对生成的图像和真实世界图像。此外，提出了一种名为TextCue的方法，无需训练即可增强LMMs对包含关键文本线索的图像区域的感知。
### Conclusion
通过多维度分析，发现了LMMs在多模态推理中的重要发现，这些发现强调了视觉阅读与推理结合的重要性。TextCue方法在某些设置下提高了LMMs的表现，证明了其有效性。基准数据集可供下载。
## 370. `cs.CL` - 莫尔索作为数据点 [PDF](https://arxiv.org/pdf/2502.01364), [HTML](https://arxiv.org/abs/2502.01364)
### Authors
Abhinav Pratap
### Background
在数据化时代，人类经历被简化为可量化的指标引发了深刻的哲学和伦理问题。本文通过阿尔贝·加缪的《局外人》中无情感角色莫尔索来探讨这些问题，展示算法模型在处理复杂的、根基在存在主义异化和道德模糊性的人类经历时固有的局限性。
### Innovation
使用自然语言处理技术，包括情绪检测（BERT）、情感分析（VADER）和命名实体识别（spaCy），量化莫尔索生活中关键事件和行为。研究揭示了将现代AI工具误解为莫尔索的行为和情绪，强调限制细腻的人类叙述转化为数据点的伦理困境，挑战了基于数据驱动的社会的基本假设。
### Conclusion
论文的研究结果是对日益依赖数据驱动叙事的批判，并呼吁在人工智能中融入人本价值观。
## 371. `cs.CL` - 利用大型语言模型结合测试驱动开发生成可靠且可验证的电子表格代码：一种研究框架 [PDF](https://arxiv.org/pdf/2510.15585), [HTML](https://arxiv.org/abs/2510.15585)
### Authors
Simon Thorne,Advait Sarkar
### Background
大型语言模型（LLMs），如ChatGPT，被越来越多地用于生成传统软件代码和电子表格逻辑。尽管这些模型展示出了强大的生成能力，但它们常常会出现幻觉、逻辑上的细微不一致和语法错误等问题，这些问题在金融建模和科学研究等高风险领域尤为严重，因为这些领域的准确性和可靠性至关重要。
### Innovation
本文提出了一种结构化的研究框架，将测试驱动开发（Test-Driven Development，TDD）与大型语言模型（LLM）驱动的代码生成相结合，以提高生成代码的正确性、可靠性和用户信心。通过“先编写测试”的方法，旨在提供技术约束和认知支持，引导LLM输出更准确、可验证和易于理解的解决方案。
### Conclusion
本文强调通过测试驱动思考提高计算思维、提示工程技能并在电子表格用户中增强参与感，这些用户可能缺乏正式的编程培训却面临重大逻辑错误的后果。本文邀请合作者进一步完善和实证评估该方法，最终目标是在教育和职业发展实践中建立负责任且可靠的LLM集成。
## 372. `cs.CL` - 使用RAG增强动态提示的大规模语言模型系统分析：医学错误检测与纠正 [PDF](https://arxiv.org/pdf/2511.19858), [HTML](https://arxiv.org/abs/2511.19858)
### Authors
Farzad Ahmed,Joniel Augustine Jerome,Meliha Yetisgen,Özlem Uzuner
### Background
临床记录中包含事实、诊断和管理错误，这些错误可能导致患者安全问题。大规模语言模型（LLMs）可能有助于检测和纠正此类错误，但不同提示策略下的行为尚不清楚。目前研究评估了零样本提示、静态提示与随机示例（SPR）以及检索增强动态提示（RDP）在医学错误处理中的应用，具体为错误标记检测、错误句子检测和错误纠正三个子任务。
### Innovation
提出了使用检索增强动态提示（RDP）的大规模语言模型分析方法，这种新型提示策略在不同模型下表现出优越性，尤其是在检测、减少假阳性方面，并提高了纠错的上下文准确性。研究表明，与零样本和静态提示相比，使用检索示例可以提高检测准确性，减少假阳性和增强医学错误纠正的可靠性。
### Conclusion
在多种不同模型下，检索增强动态提示（RDP）优于零样本和静态提示（SPR）。使用检索示例能够提高检测准确性、减少假阳性，并增强医学错误纠正的可靠性。
## 373. `cs.CL` - 在组合任务结构中描述模式匹配及其限制 [PDF](https://arxiv.org/pdf/2505.20278), [HTML](https://arxiv.org/abs/2505.20278)
### Authors
Hoyeon Chang,Jinho Park,Hanseul Cho,Sohee Yang,Miyoung Ko,Hyeonbin Hwang,Seungpil Won,Dohaeng Lee,Youbin Ahn,Minjoon Seo
### Background
尽管大语言模型（LLMs）展现出令人印象深刻的能力，但它们的成功往往依赖于模式匹配的行为，然而这种行为也会导致在组合任务中的模型外通用失败。对于模式匹配在任务中的实际效果及其限制，现有的行为研究通常采用了多种通用化来源的任务设置（如代数不变性，结构性重复），这使得很难得到精确和可测试的关于模式匹配在通用化中的表现及其局限性的结论。
### Innovation
本文首先将模式匹配定义为功能性等价，即识别出在输入保持不变的情况下始终产生相同结果的输入子序列对。然后系统研究了仅解码器变压器和Mamba模型在分离了这一机制的受控组合结构任务中的表现。研究结果包括：（1）模式匹配的成功率可以通过观察到的相关功能等价的数量进行预测。（2）提出了由完美领域内通用化数据扩展法则的指数决定的学习两跳结构的紧样本复杂性边界。（3）路径模糊性是结构性障碍：当一个变量通过多个路径影响输出时，模型难以形成统一的中间状态表示，影响了准确性和可解释性。（4）逐步思考可以减少数据需求，但无法解决路径模糊性。因此，本文提供了模式匹配的预测性可否证边界，并为区分混合通用化机制提供了一个基础诊断。
### Conclusion
本文提供了关于模式匹配在组合任务结构中表现及其限制的可预测性且可验证的边界，并为理解混合通用化机制提供了基础诊断。
## 374. `cs.CL` - TimeViper: 一种用于高效长视频理解的混合Mamba-Transformer视觉语言模型 [PDF](https://arxiv.org/pdf/2511.16595), [HTML](https://arxiv.org/abs/2511.16595)
### Authors
Boshen Xu,Zihan Xiao,Jiaze Li,Jianzhong Ju,Zhenbo Luo,Jian Luan,Qin Jin
### Background
长视频的理解需要高效的模型架构和有效的机制来处理长时间序列上下文，这是现有的视觉语言模型面临的挑战。
### Innovation
引入了TimeViper，这是一种混合视觉语言模型，采用了Mamba-Transformer混合骨干网络，结合了状态空间模型的效率和注意机制的表达能力。提出了TransV模块，这是一种令牌信息传输机制，可以在保持多模态理解能力的同时，将视觉令牌压缩为指令令牌。
### Conclusion
通过广泛的实验证明，TimeViper在多个基准测试中与最新的模型竞争，并且能够处理超过10,000帧的小时长视频。进一步分析了Mamba和Transformer层的注意行为，提供了关于混合模型解释的新见解。该工作代表了开发、解释和压缩Mamba-Transformer混合架构的一个初步步骤。
## 375. `cs.CV` - 移动边缘网络中的视频目标识别：本地跟踪还是边缘检测？ [PDF](https://arxiv.org/pdf/2511.20716), [HTML](https://arxiv.org/abs/2511.20716)
### Authors
Kun Guo,Yun Shen,Xijun Wang,Chaoqun You,Yun Rui,Tony Q. S. Quek
### Background
在资源受限的设备上（如交通摄像头），依靠帧级视频分析的快速且准确的目标识别仍然具有挑战性。移动边缘计算的进步使得将计算密集型对象检测任务卸载到配备高性能神经网络的边缘服务器成为可能，而轻量级且快速的对象跟踪算法则在本地设备上运行。虽然这种组合提供了一个有希望的解决方案，但却带来了一个新的挑战：确定何时进行边缘检测，何时进行本地跟踪。
### Innovation
本文为单设备和多设备场景分别制定两个长期优化问题，考虑了连续帧之间的时序相关性和移动边缘网络的动态条件。在此基础上，提出了一种基于深度强化学习的算法LTED-Ada，该算法在单设备设置中根据帧率、识别准确性和延迟要求自适应地选择本地跟踪或边缘检测。在多设备场景中，进一步增强了LTED-Ada方法，通过联邦学习使设备间能够协作训练策略，从而提高其在未见过的新帧率和性能要求下的推广能力。
### Conclusion
通过大量的硬件在环实验，使用多个Raspberry Pi 4B设备和一台个人计算机作为边缘服务器，证明了LTED-Ada算法的优越性。
## 376. `cs.CV` - 神经启发的多模态视觉-语言模型对于成员推断隐私泄露是否具有韧性？ [PDF](https://arxiv.org/pdf/2511.20710), [HTML](https://arxiv.org/abs/2511.20710)
### Authors
David Amebley,Sayanton Dibbo
### Background
在代理型人工智能时代，多模态模型（MMs）的广泛应用引入了新的攻击向量，这些向量会导致敏感的训练数据泄漏，从而导致隐私泄露。当前对隐私攻击的研究主要关注单一模态的人工智能系统，而最近的研究表明，多模态系统也可能受到隐私攻击。神经启发的神经网络表示可以提高单一模态模型对抗对抗性攻击的能力，但是对于神经启发的多模态系统是否也具备对抗隐私攻击的能力，这一问题仍待探索。
### Innovation
本文提出了一种系统化的神经科学启发的拓扑正则化（tau）框架，用于分析神经启发的多模态视觉-语言模型（VLMs）对于基于图像-文本判断的隐私泄露攻击的韧性。研究了BLIP、PaliGemma 2、ViT-GPT2三种VLMs在COCO、CC3M、NoCaps三个基准数据集上的韧性，并通过比较基准配置与具有拓扑正则化配置的模型来验证神经VLMs的隐私威胁韧性。
### Conclusion
实验结果表明，对于BLIP模型在COCO数据集上的测量结果，神经VLMs在NEURO配置下的MIA攻击成功率降低了24%的均值ROC-AUC，同时模型在MPNet和ROUGE-2指标上的生成和参考描述之间的相似度保持不变。这表明神经VLMs在隐私攻击中表现出较低的脆弱性，同时不需要牺牲模型性能。进一步的评估与PaliGemma 2和ViT-GPT2模型在两个额外数据集CC3M和NoCaps上的结果一致，证实了上述发现。该研究对多模态系统的隐私风险有了更深入的理解，提供了神经VLMs对于隐私威胁反弹性的证据。
## 377. `cs.CV` - DeeAD: Dynamic Early Exit of Vision-Language Action for Efficient Autonomous Driving [PDF](https://arxiv.org/pdf/2511.20720), [HTML](https://arxiv.org/abs/2511.20720)
### Authors
Haibo HU,Lianming Huang,Nan Guan,Chun Jason Xue
### Background
Vision-Language Action (VLA) 模型将感知、推理和轨迹生成统一起来，但在自动驾驶中由于深层变换堆栈导致推断延迟显著。
### Innovation
提出了一种无需训练、基于动作的早期退出框架 DeeAD，通过评估中间轨迹的物理可行性来加速 VLA 规划。引入了多跳控制器，根据评分变化率智能跳过冗余层。DeeAD 无需重新训练即可集成到现有的 VLA 模型中。
### Conclusion
在 Bench2Drive 标准测试中，DeeAD 可以减少 28% 的变换层稀疏性和 29% 的延迟，同时保持规划质量和安全性。
## 378. `cs.CL` - 可视化思考，文本推理：ARC中的视觉-语言协同效应 [PDF](https://arxiv.org/pdf/2511.15703), [HTML](https://arxiv.org/abs/2511.15703)
### Authors
Beichen Zhang,Yuhang Zang,Xiaoyi Dong,Yuhang Cao,Haodong Duan,Dahua Lin,Jiaqi Wang
### Background
前沿的基础模型如GPT-5和Grok 4依然无法从少量示例中推断出结构性的转变规则，这仍然是抽象推理的核心未解问题。以往的研究方法大多将ARC-AGI视为纯粹的文本推理任务，忽略了人类在解决此类谜题时高度依赖视觉抽象的特点。初步实验揭示了一个悖论：简单地将ARC-AGI网格转换为图像实际降低了表现，因为图像解释不够精确。这导致了视觉和语言之间存在互补优势的观点，即视觉支持全局模式的抽象和验证，而语言专注于符号规则的制定和精确执行。
### Innovation
基于上述洞见，提出了一种新的方法：(1) 视觉-语言协同推理（VLSR），将ARC-AGI分解为模态对齐的子任务；(2) 模态切换自纠正（MSSC），利用视觉验证基于文本的推理进行内在错误纠正。广泛的实验证明，与仅使用文本的方法相比，这种方法在多元旗舰模型和多种ARC-AGI任务中分别提高了高达4.33%的表现。
### Conclusion
我们的研究结果表明，将视觉抽象与语言推理统一起来是实现未来基础模型中泛化的人类样智慧的关键步骤。源代码已在此处公开：给出的链接。
## 379. `cs.CV` - Inferix：基于块扩散的下一代世界模拟推断引擎 [PDF](https://arxiv.org/pdf/2511.20714), [HTML](https://arxiv.org/abs/2511.20714)
### Authors
Inferix Team:Tianyu Feng,Yizeng Han,Jiahao He,Yuanyu He,Xi Lin,Teng Liu,Hanfeng Lu,Jiasheng Tang,Wei Wang,Zhiyuan Wang,Jichao Wu,Mingyang Yang,Yinghao Yu,Zeyu Zhang,Bohan Zhuang
### Background
世界模型作为自主人工智能、具身人工智能和游戏领域的核心模拟器，能够生成长时间、物理真实且交互性强的高质量视频。这些模型的可扩展性可以解锁视觉感知、理解和推理的新能力，推动超越当前以LLM为中心的视觉基础模型的新范式。
### Innovation
Inferix通过引入半自回归（块扩散）解码范式，结合扩散方法和自回归方法的优点，通过在每个块内应用扩散并在每个块上条件化，生成更连贯和稳定的视频序列。此外，它通过恢复LLM风格的KV缓存管理，克服了标准视频扩散的局限性，实现了高效、可变长度和高质量的生成。
### Conclusion
Inferix专门设计为通过优化半自回归解码过程实现沉浸式世界合成的下一代推断引擎，与高并发场景系统（如vLLM或SGLang）和经典视频扩散模型（如xDiTs）不同。Inferix还通过支持交互视频流传输和分析，增强了其在实时交互和准确建模世界动力学方面的功能。此外，通过与LV-Bench无缝集成，它支持高效基准测试，这是一种专为一分钟视频生成场景设计的详细评价基准。我们希望社区共同努力推进Inferix，促进世界模型探索。
## 380. `cs.CV` - DinoLizer: 从最佳模型中学到的生成性修复局部化 [PDF](https://arxiv.org/pdf/2511.20722), [HTML](https://arxiv.org/abs/2511.20722)
### Authors
Minh Thong Doi(IMT Nord Europe, CRIStAL),Jan Butora(CRIStAL),Vincent Itier(IMT Nord Europe, CRIStAL),Jérémie Boulanger(CRIStAL),Patrick Bas(CRIStAL)
### Background
该研究介绍了一种基于DINOv2的模型DinoLizer，用于定位生成填充中的篡改区域。该方法是在B-Free数据集上预训练以检测合成图像的DINOv2模型的基础上构建的。模型通过一个附加在线性分类头，用于在14×14像素级上预测篡改，该头被训练以专注于语义改变的区域，非语义编辑被视为原始内容的一部分。由于ViT只能接受固定大小的输入，作者使用滑动窗口策略来在更大图像上聚合预测，最终热图经过后处理以细化估计的二进制篡改遮罩。
### Innovation
DinoLizer的主要创新点在于其基于预训练于检测合成图像的DINOv2模型，并加入了14×14像素级别的线性分类头，用于识别篡改区域。该模型能够处理不同生成模型的修复数据集，并且在多种后处理操作下保持鲁棒性。实验结果表明，DinoLizer在多个评价指标上优于现有最先进的局部篡改检测器，特别是在经过后处理操作后的性能提升更为显著。此外，通过使用现成的DINOv2模型，展示了Vision Transformers在该任务上的强大表示能力。
### Conclusion
DinoLizer通过在生成填充数据集中定位篡改区域展示了其优越性，并在不同的修复数据集上超过了其他最先进的模型，即使在常见的后处理操作后也能保持其性能。此外，对DINOv2和DINOv3的消融研究表明，DinoLizer性能最优。作者表示，该代码将在论文被接受后公开。
## 381. `cs.CL` - AutoDiscovery: 通过贝叶斯惊奇实现开放式的科学发现 [PDF](https://arxiv.org/pdf/2507.00310), [HTML](https://arxiv.org/abs/2507.00310)
### Authors
Dhruv Agarwal,Bodhisattwa Prasad Majumder,Reece Adamson,Megha Chakravorty,Satvika Reddy Gavireddy,Aditya Parashar,Harshit Surana,Bhavana Dalvi Mishra,Andrew McCallum,Ashish Sabharwal,Peter Clark
### Background
自动化科学发现（ASD）不仅致力于回答问题，还在于能够识别哪些问题是值得探索的。大多数现有ASD研究依赖于人类预先指定的研究问题来引导假设生成。然而，通过让AI系统依据它自己的标准自主探索，或许能够加速科学发现。现有的ASD方法主要依据多样性的启发式规则或主观的人类趣味性标准来选择假设，但这些方法在面对庞大假设库时表现出不足，或者其标准不够精确。
### Innovation
本文提出了一种名为AutoDiscovery的方法，通过贝叶斯惊喜来驱动开放式的科学探索。此方法通过蒙特卡洛树搜索（MCTS）策略并结合逐步扩展的策略来高效探索嵌套假设的空间。在生物、经济学、金融和行为科学等多个领域的21个真实数据集上进行的实验表明，AutoDiscovery 在固定预算下比竞争对手能够产生更多被模型认为令人惊讶的发现。此外，人类评价结果显示，超过三分之二的发现对领域专家来说也是令人惊讶的，这表明通过贝叶斯惊喜驱动的ASD方法具有重大进展意义。
### Conclusion
AutoDiscovery 方法在开放式科学探索方面取得了显著成绩，特别是在数据驱动的科学发现领域。它利用贝叶斯惊喜来驱动探索过程，并通过蒙特卡洛树搜索策略有效地探索了大量假设的空间。尽管存在现有方法中存在的不足，但AutoDiscovery方法展示了赶超同类算法的潜力，并被视为开发开放式自动化科学发现系统的有意义步骤。
## 382. `cs.CV` - 仅需一张图片：从极少视觉线索进行联合表面材料重构与分类 [PDF](https://arxiv.org/pdf/2511.20784), [HTML](https://arxiv.org/abs/2511.20784)
### Authors
Sindhuja Penchala,Gavin Money,Gabriel Marques,Samuel Wood,Jessica Kirschman,Travis Atkison,Shahram Rahimi,Noorbakhsh Amiri Golilarz
### Background
理解材料表面对于机器人技术、模拟和材料感知至关重要，但现有大多数方法依赖密集或完整场景观察，这在受限或部分视图环境中影响其效果。
### Innovation
本文提出了一种名为SMARC的统一模型，用于从极少视觉输入中进行表面材料重构与分类，通过单一10%的连续图像片段，可以识别和重构完整RGB表面并同时分类材料类别。该架构结合了部分卷积U-Net和分类头，既能进行空间填充又能理解极端观察稀疏下的语义。
### Conclusion
SMARC在真实表面纹理数据集中实现了最先进的结果，PSNR达到17.55 dB，材料分类准确率为85.10%。研究结果强调了在缺失数据下的空间推理中部分卷积的优势，并为极少数视觉感知表面理解奠定了坚实的基础。
## 383. `cs.CL` - In-context Learning 中的任务导向信息去除机制 [PDF](https://arxiv.org/pdf/2509.21012), [HTML](https://arxiv.org/abs/2509.21012)
### Authors
Hakaze Cho,Haolin Yang,Gouki Minegishi,Naoya Inoue
### Background
在-context 学习（ICL）是一种新兴的少样本学习范式，基于现代语言模型（LMs），然而其内部机制仍然不清晰。本文通过一种新的信息去除视角对ICL的机制进行了研究。
### Innovation
文章发现，在零样本场景下，语言模型会将查询编码为包含所有潜在任务信息的非选择性表示，在隐藏状态中泛化不出特定任务的信息，导致泛化性能较差。进一步通过低秩滤波器有选择地从隐藏状态中去除特定信息，可以引导模型关注目标任务。通过测量设计的隐藏状态指标，发现少样本ICL有效地模拟了这种任务导向的信息去除过程，能够从纠缠的非选择性表示中消除冗余信息，从而改进输出，揭示了ICL的关键机制。并识别出了执行消除操作的关键注意力头，称为去噪头，这在阻断这些操作时，ICL的性能显著下降。
### Conclusion
这些研究结果证明了信息去除机制及其对应的去噪头对ICL性能的至关重要性。
## 384. `cs.CL` - Step-Audio-R1技术报告 [PDF](https://arxiv.org/pdf/2511.15848), [HTML](https://arxiv.org/abs/2511.15848)
### Authors
Fei Tian,Xiangyu Tony Zhang,Yuxin Zhang,Haoyang Zhang,Yuxin Li,Daijiao Liu,Yayue Deng,Donghang Wu,Jun Chen,Liang Zhao,Chengyuan Yao,Hexin Liu,Eng Siong Chng,Xuerui Yang,Xiangyu Zhang,Daxin Jiang,Gang Yu
### Background
近期推理模型在文本和视觉领域取得了显著的成功，这主要归功于其扩展的链式思考能力。然而，对于音频语言模型而言，一个令人困惑的现象出现了：它们在无需或仅少量推理的情况下表现得更好，这引发了一个基本问题——音频智能是否真的能从深思熟虑中获益？
### Innovation
Step-Audio-R1是首个成功在音频领域解锁推理能力的音频推理模型。通过我们提出的模态导向推理精炼（MGRD）框架，Step-Audio-R1学会了生成真正基于声学特征的音频相关推理链，而非凭空创造脱离实际的思考过程。该模型在言语、环境声音和音乐等全面的音频理解和推理基准测试中表现出强大的推理能力，超过Gemini 2.5 Pro并达到与Gemini 3 Pro相似的最新技术水平。这些结果表明，当适当锚定时，推理能力和优越性可以在不同模态间进行转移，从而将扩展的思考过程从致命弱点转变为音频智能的强大资产。
### Conclusion
通过建立首个成功的音频推理模型，Step-Audio-R1开辟了新的途径，以构建真正全能的推理系统，实现各感官模态的深刻思考。
## 385. `cs.CL` - UniChange: 使用多模态大型语言模型统一变化检测 [PDF](https://arxiv.org/pdf/2511.02607), [HTML](https://arxiv.org/abs/2511.02607)
### Authors
Xu Zhang,Danyang Li,Xiaohang Dong,Tianhao Wu,Hualong Yu,Jianye Wang,Qicheng Li,Xiang Li
### Background
变化检测（CD）是监测和分析土地覆盖动态的基础任务。尽管最近高性能模型和高质量数据集极大地推动了该领域的发展，但当前模型存在一个关键局限性：它们通常只能从单一类型的标注数据中获得有限的知识，且无法结合二元变化检测（BCD）和语义变化检测（SCD）数据集中的信息。这种限制导致了较差的泛化能力和较低的灵活性。
### Innovation
该论文利用多模态大型语言模型（MLLMs）的语言先验和统一能力，开发了UniChange模型，这是第一个基于MLLMs的统一变化检测模型。UniChange通过引入三个特殊标记 [T1]，[T2] 和 [CHANGE] 来整合生成的语言能力与专门的变化检测功能。UniChange还利用文本提示来指导变化类别识别，从而避免了对预定义分类头的依赖。这使得UniChange能够有效从多种来源的数据集中学习知识，即使这些数据集的类别定义存在冲突。
### Conclusion
在四个公开基准数据集（WHU-CD，S2Looking，LEVIR-CD+ 和 SECOND）上的实验结果表明，UniChange达到了最佳性能，IoU得分为90.41，53.04，78.87和57.62，超过了所有先前的方法。相关的代码可以在以下链接找到。
## 386. `cs.CV` - CANVAS: 视觉语言模型在工具驱动用户界面设计上的基准 [PDF](https://arxiv.org/pdf/2511.20737), [HTML](https://arxiv.org/abs/2511.20737)
### Authors
Daeheon Jeong,Seoyeon Byun,Kihoon Son,Dae Hyun Kim,Juho Kim
### Background
用户界面设计是一个迭代过程，设计人员通过设计软件如Figma或Sketch逐步精炼其工作。最近，视觉语言模型（VLMs）在工具调用方面的进展表明，它们能够通过迭代操作设计软件来编辑UI设计。然而，由于缺乏针对工具设计表现的基准评估方法，模型的这种能力尚未得到验证。因此，需要创建一个针对VLMs的工具驱动用户界面设计基准，以评估其在设计软件中的迭代编辑能力。
### Innovation
本文提出了CANVAS，这是一个包含598个由30个功能类别（例如引导、消息）的3300个移动UI设计中随机抽取的真实参考设计的任务，用以研究VLMs在工具驱动用户界面设计中的能力。CANVAS基准包括两种任务类型：设计复制评估模型重建整个UI屏幕的能力；设计修改评估模型修改现有屏幕特定部分的能力。该基准有助于理解VLMs的工具驱动设计能力，并识别模型中的常见错误模式。
### Conclusion
结果显示，领先模型表现出更策略性的工具调用，提高了设计质量。同时，研究还指出了模型在工具驱动设计方面的常见错误模式，为未来研究提供了方向。
## 387. `cs.CV` - LongVT：通过内置工具调用激励“与长视频同思考” [PDF](https://arxiv.org/pdf/2511.20785), [HTML](https://arxiv.org/abs/2511.20785)
### Authors
Zuhao Yang,Sudong Wang,Kaichen Zhang,Keming Wu,Sicong Leng,Yifan Zhang,Chengwei Qin,Shijian Lu,Xingxuan Li,Lidong Bing
### Background
大型多模态模型（LMMs）在视频理解中显示出巨大的潜力，尤其是在使用文本链式思考时。然而，这些模型在处理长视频时仍然容易产生幻觉，尤其是在证据稀疏且时间上分散的情况下。人类理解长视频的方式是先全局浏览，然后深入查看相关的片段以获取详细信息。因此，本文提出了LongVT框架，这是一种端到端的代理框架，通过交错的多模态链式工具思考来实现“与长视频同思考”。该框架利用LMMs固有的时间关联能力作为视频剪裁工具，对特定视频片段进行更精细的采样。这一全局到局部的推理循环将持续进行，直到答案能够基于检索到的视觉证据。
### Innovation
LongVT框架通过交错的多模态链式工具思考来解决长视频推理中的幻觉问题。它利用LMMs的时间关联能力作为视频剪裁工具，对特定片段进行更精细的采样。此外，为了促进训练和评估，还专门创建并公开了一个名为VideoSIAH的数据集。该数据集包括用于工具集成冷启动监督微调、代理强化学习以及代理强化微调的不同样本量，并且创建了一个包含1,280个问答对的人工半自动数据处理管道。经过精心设计的三阶段训练策略和广泛的实验证明，LongVT在四个具有挑战性的长视频理解和推理基准中始终优于现有的强基线。
### Conclusion
通过全球浏览和局部详细查看的方式，LongVT框架有效地解决了长视频推理中的幻觉问题，并在多个基准测试中表现出色。研究团队还公开了实验代码、数据集和模型检查点，以供研究界参考。
## 388. `cs.CV` - Foundry: Distilling 3D Foundation Models for the Edge [PDF](https://arxiv.org/pdf/2511.20721), [HTML](https://arxiv.org/abs/2511.20721)
### Authors
Guillaume Letellier,Siddharth Srivastava(IIT Delhi),Frédéric Jurie,Gaurav Sharma(IIT Kanpur)
### Background
预训练的大规模自我监督学习（SSL）基础模型已经成为强大的通用特征提取器。然而，这些模型的庞大体积和计算成本使得它们不适合在如机器人和AR/VR头显等边缘设备上部署。现有压缩技术，如标准知识精简，虽能创建高效的‘专门’模型，但牺牲了基本的、下游任务无关的普及性，这是基础模型如此有价值的特性。
### Innovation
本文介绍了基础模型精简（FMD），这是一种将大规模SSL模型压缩成紧凑、高效且忠实于原始基础模型代表性能的大规模压缩方案。FMD模型Train学生学习压缩的‘超级标记’集，以重建教师的标记级别表示，从而捕获其潜在空间的紧凑基底。这种单一的精简模型在各种下游任务（分类、部分分割和少样本场景）上具有强大的可迁移性，超过了全面基础模型的表现，同时使用更少的标记和运算量，这使得此类模型在资源受限的硬件上更具部署可行性。
### Conclusion
我们的方法Foundry训练学生模型来学习压缩的‘超级标记’集，重建教师模型的标记级别表示，从而捕获潜在空间的紧凑基底。单个精简模型在多种下游任务（分类、部分分割和少样本场景）上具有强大的可迁移性，接近全功能基础模型的表现，但使用更少的标记和运算量，使得这些模型更适用于边缘设备的部署。
## 389. `cs.CV` - $?Delta$-NeRF: 通过残差控制和知识迁移进行的神经辐射场的增量细化 [PDF](https://arxiv.org/pdf/2511.20804), [HTML](https://arxiv.org/abs/2511.20804)
### Authors
Kriti Ghosh,Devjyoti Chakraborty,Lakshmish Ramaswamy,Suchendra M. Bhandarkar,In Kee Kim,Nancy O'Hare,Deepak Mishra
### Background
神经辐射场（NeRFs）在3D重建和新视角合成方面表现出显著的能力。然而，目前大多数NeRF框架在逐步引入新视角时需要重新训练，这限制了它们在数据按顺序到达的领域中的应用。特别是在基于卫星的地形分析中，同一地区会多次被观测。虽然增量更新NeRFs仍有待探索，但现有的简单方法会因缺乏过去数据而发生灾难性遗忘。
### Innovation
提出了一个独特的模块化残差框架$?Delta$-NeRF，包括：(1) 一个残差控制器，能够向冻结的基础NeRF中注入逐层的修正，无需访问过去的数据即可实现细化；(2) 一种基于不确定性门控机制，通过适配性地结合基础预测和细化预测来防止过纠正；(3) 一种视图选择策略，可以减少高达47%的训练数据量，同时保持性能。此外，采用知识蒸馏将增强模型压缩成一个紧凑的学生网络（原始大小的20%）。实验证明，$?Delta$-NeRF在保持与联合训练性能相当的同时，将训练时间减少了30-42%，且在多个基准上表现优异，达PSNR提升43.5%。
### Conclusion
$?Delta$-NeRF在保持与联合训练相当的性能的同时显著减少了训练时间，并且在多项基准测试中实现了优于现有基线模型的结果，特别是在卫星图像上验证了其有效性和优势。
## 390. `cs.CV` - SPHINX：一种视觉感知和推理的合成环境 [PDF](https://arxiv.org/pdf/2511.20814), [HTML](https://arxiv.org/abs/2511.20814)
### Authors
Md Tanvirul Alam,Saksham Aggarwal,Justin Yang Chae,Nidhi Rastogi
### Background
本文介绍了一种名为Sphinx的合成环境，该环境专注于核心认知原语，并用于视觉感知和推理。Sphinx通过使用模式、瓷砖、图表、图标和几何原语等元素，结合可验证的地面真相解决方案，生成具有谜题性质的任务，这不仅能够实现精确的评估，还能生成大规模的数据集。
### Innovation
Sphinx通过程序生成具有可验证准确答案的任务，涵盖了25种不同类型的任务，包括对称性检测、几何变换、空间推理、图表解释和序列预测。即使高级模型如GPT-5仅能达到51.1%的准确率，这一结果远低于人类水平。此外，使用可验证奖励的强化学习（RLVR）在这些任务上的表现显著高于无监督学习的方法，同时也提升了外部视觉推理基准任务的表现。
### Conclusion
本文通过对Sphinx合成环境生成的多样任务进行测试，发现即使是最先进的模型在某些领域的表现也不佳，验证了需要进一步优化视知觉和语义理解模型。相对无监督的方法，具有可验证奖励的强化学习能在这些任务上提供更高的准确率，揭示了其在促进多模态推理方面的潜力。
## 391. `cs.CV` - RefTr: 递归精化共轭轨迹用于3D血管树中心线图 [PDF](https://arxiv.org/pdf/2511.20823), [HTML](https://arxiv.org/abs/2511.20823)
### Authors
Roman Naeem,David Hagerman,Jennifer Alvén,Fredrik Kahl
### Background
血管和其他管状树结构（如肺部气道）对人类体内的物质运输至关重要。准确地检测其中心线并保持正确的树拓扑结构对临床任务（如诊断、治疗计划和手术导航）非常重要。在这些应用中，保持高召回率至关重要，因为遗漏小分支可能会导致由不完整评估或未检测异常引起的严重错误。
### Innovation
RefTr是一种用于血管树中心线生成的3D图像到图模型，通过递归精化共轭轨迹。它采用生产者-精炼器架构，基于变压器解码器。生产者建议一组初始共轭轨迹，然后由精炼器逐次精化生成最终轨迹，形成中心线图。共轭轨迹表示法能够精化完整路径并明确约束出有效树拓扑。递归精化方案提高了精度，且在多个步骤中重用了相同的精炼器块，使得与前者的平均解码器参数相比减少了2.4倍。此外，还引入了一种高效的非最大值抑制算法来合并空间树图中的重复分支，以提升精度。
### Conclusion
在多个公开的中心线数据集中，RefTr在召回率上表现出色，精度与此前的最优技术相当，同时提供更快的推断速度和显著减少的参数数量，展示了其作为3D医学成像中血管树分析的新一代最优框架的潜力。
## 392. `cs.CV` - 基于优化反演的无训练扩散先验用于文本到图像生成 [PDF](https://arxiv.org/pdf/2511.20821), [HTML](https://arxiv.org/abs/2511.20821)
### Authors
Samuele Dell'Erba,Andrew D. Bagdanov
### Background
扩散模型在文本到图像生成方面已经取得了最先进的成果，但其性能往往依赖于扩散先验网络将文本嵌入转换到视觉 manifold，以便更容易地解码。这些先验网络计算成本高，需要在大规模数据集上进行大量训练。
### Innovation
该工作提出了无需训练的基于优化反演(OVI)的新方法，用以替代传统的扩散先验。OVI通过从随机伪标记初始化潜在的视觉表示，并通过迭代优化以最大化与输入文本提示嵌入的余弦相似性。同时，提出了一种基于马氏距离和最近邻损失的新约束，以帮助其优化过程趋向于现实图像的分布。这种方法在Kandinsky 2.2上的实验表明，它可以作为传统先验的替代方案，而且改进了视觉保真度，特别是最近邻方法。
### Conclusion
尽管使用文本嵌入作为先验在视觉质量上较低，但约束OVI方法提高了视觉保真度，最近邻方法取得了与最先进的数据高效先验相当或更优的定量分数，表明该方法值得深入研究。相关代码将在论文接受后公开。
## 393. `cs.CV` - 从立体图序列估计雾参数 [PDF](https://arxiv.org/pdf/2511.20865), [HTML](https://arxiv.org/abs/2511.20865)
### Authors
Yining Ding,João F. C. Mota,Andrew M. Wallace,Sen Wang
### Background
在雾环境中，现有方法通常顺序估计雾参数，这容易导致误差传递。本文旨在提出一种新的方法，能够在同时估计所有参数的同时，有效处理由于雾的全局不均匀性带来的挑战。该方法还可以很容易地作为附加模块集成到现有的视觉SLAM或 odometry 系统中。为了评估该方法，论文还创建了一个新的数据集 SDIRF，包括不同能见度条件下的高质量连续立体帧，用于图像去雾和深度重建。
### Innovation
本文提出的方法通过解决新的优化问题，同时估计所有雾参数，从而避免了顺序估计方式引起的误差传递问题。此外，假设雾在局部是均匀的，这种方法能够有效处理现实中通常全球不均匀的雾。另外一个创新点在于SDIRF 数据集，该数据集包括实验室校准的相机光度参数和在不同天气状况下的清亮点云数据，后者的存在有助于图像去雾和深度重建的同行研究。
### Conclusion
实验结果表明，本文提出的方法在合成数据上的估计结果更为准确，并能更好地适应真实世界的雾环境。为了推进雾环境中的视觉感知研究，论文开源了相关的代码和SDIRF 数据集。
## 394. `cs.CV` - V$^{2}$-SAM: 结合 SAM2 和 多提示专家实现跨视角物体对应 [PDF](https://arxiv.org/pdf/2511.20886), [HTML](https://arxiv.org/abs/2511.20886)
### Authors
Jiancheng Pan,Runze Wang,Tianwen Qian,Mohammad Mahdi,Yanwei Fu,Xiangyang Xue,Xiaomeng Huang,Luc Van Gool,Danda Pani Paudel,Yuqian Fu
### Background
跨视角物体对应，比如自视角和外视角物体对应，旨在建立不同视角下一致的物体关联。这一任务由于视角和外观的显著差异带来了巨大挑战，使得现有的分割模型，如SAM2，难以直接应用。
### Innovation
本文提出了一种统一的跨视角物体对应框架——V^2-SAM，通过采用两种互补的提示生成器将单视角分割(SAM2)扩展到跨视角对应。具体而言，V^2-Anchor 基于 DINOv3 特征建立几何感知的对应关系，并首次在跨视角场景下解锁坐标提示，而 V^2-Visual 通过一种新型视觉提示匹配器增强外观引导线索。此外，为有效利用两种提示的优势，文中引入了后适应循环一致性选择器 (PCCS)，以根据循环一致性自适应选择最可靠的专家。
### Conclusion
广泛的实验验证了V^2-SAM的有效性，实现了Ego-Exo4D、DAVIS-2017和HANDAL-X等数据集上的最新性能。
## 395. `cs.CV` - MODEST：多光学景深立体数据库 [PDF](https://arxiv.org/pdf/2511.20853), [HTML](https://arxiv.org/abs/2511.20853)
### Authors
Nisarg K. Trivedi,Vinayak A. Belludi,Li-Yun Wang,Pardis Taghavi,Dante Lok
### Background
在自主机器人和增强现实等系统中，相机视觉深度估计在真实光学条件下保持可靠仍然是一项核心挑战。尽管最近在深度估计和景深渲染方面取得了进展，但研究仍受限于缺乏大规模、高保真度的真实双目单反相机数据集，这限制了模型在合成数据训练下的现实世界泛化和评估。
### Innovation
本文介绍了首个高分辨率（5472×3648像素）的双目单反相机数据集，包含18000张图像，系统地在复杂的真实场景中变化焦距和光圈，捕捉专业相机系统的光学现实性和复杂性。该数据集覆盖50种光学配置，提供了几何和光学效应的可控分析，支持对单目和立体深度估计、浅景深渲染、去模糊、三维场景重构和新颖视图合成等任务的研究。同时，每个焦距配置都有专用的校准图像集，支持经典和基于学习方法的内在和外在校准评估。
### Conclusion
本文试图弥合合成训练数据和真实相机光学之间的现实差距，展示了当前最先进的单目、立体深度估计和景深方法所面临的挑战。该论文发布了数据集、校准文件和评价代码，以支持真实光学泛化的可复现实验研究。
## 396. `cs.CV` - 平滑正则化用于高效的视频识别 [PDF](https://arxiv.org/pdf/2511.20928), [HTML](https://arxiv.org/abs/2511.20928)
### Authors
Gil Goldman,Raja Giryes,Mahadev Satyanarayanan
### Background
在视频识别模型中，尤其是对于轻量级架构，时间上的诱导偏差是关键问题。通过引入平滑正则化技术，可以促进连续帧中间层嵌入的变化呈现出平滑性，从而更好地捕捉视频中的自然时间连续性。
### Innovation
提出了一种平滑正则化技术，通过建模连续帧中中间层嵌入的变化为高斯随机游走（GRW），从而在轻量级模型中大力促进平滑变化，减少突然代表性的转变。通过这种方法，轻量级模型能够更有效地捕获复杂的时域动态。实验结果表明，该技术在Kinetics-600数据集上提高了3.8%到6.4%的准确率，且在轻量级模型如MoViNets和MobileNetV3上更进一步实现了显著的性能提升。
### Conclusion
在轻量级模型中使用平滑正则化，MoViNets模型家族的表现提升至3.8%到6.1%，而MobileNetV3和MoViNets-Stream家族则分别实现了4.9%到6.4%的性能提升。相关代码和模型可以在指定的GitHub链接获取。
## 397. `cs.CV` - 使用深度学习模型减少用于小脑桥脑角池对比增强MRI的造影剂剂量 [PDF](https://arxiv.org/pdf/2511.20926), [HTML](https://arxiv.org/abs/2511.20926)
### Authors
Yunjie Chen,Rianne A. Weber,Olaf M. Neve,Stephan R. Romeijn,Erik F. Hensen,Jelmer M. Wolterink,Qian Tao,Marius Staring,Berit M. Verbist
### Background
为了评价深度学习（DL）模型在减少对比增强T1加权MRI（T1ce）中小脑桥脑角（CPA）池造影剂剂量的同时保持图像质量的效果。该研究基于多中心回顾性研究，通过模拟不同造影剂剂量下的T1ce图像来评估DL模型的表现。
### Innovation
该研究开发并训练了DL模型，能够从不同剂量的低对比度T1ce图像中恢复标准剂量的T1ce图像。通过与标准剂量T1ce图像的对比，DL模型显著提高了图像相似度指数和信噪比，同时提高了分割性能，证明了使用10%-30%标准剂量的T1ce图像进行诊断和病灶检测的可能性。
### Conclusion
深度学习模型改善了低剂量MRI中小脑桥脑角池的图像质量，使得使用10%-30%标准剂量的T1ce图像也能有效进行病灶检测和诊断特征化。
## 398. `cs.CV` - Text-Guided Semantic Image Encoder [PDF](https://arxiv.org/pdf/2511.20770), [HTML](https://arxiv.org/abs/2511.20770)
### Authors
Raghuveer Thirukovalluru,Xiaochuang Han,Bhuwan Dhingra,Emily Dinan,Maha Elbayad
### Background
传统的视觉语言模型（VLMs）中的图像编码器通常在与语言模型联调之前独立预训练，这些编码器处理图像时独立于特定的下游任务或文本查询。这一标准范式导致了图像编码器在处理图像时没有考虑到具体的任务需求。
### Innovation
本文提出了一种新的Text-Guided Semantic Image Encoder（TIE）方法，它能够根据输入的文本查询生成图像表示。配备TIE的VLMs在九项图像到文本基准测试中比传统的VLMs分别提高了1.5和1.3个点，尤其是在DocVQA和InfoVQA等任务上，增益高达6个点。TIE还在减少一半图像瓷砖使用量的情况下，仍能实现优越的效果。此外，TIE在涉及通用查询的情况下表现出很好的泛化能力。
### Conclusion
TIE能够持续关注与查询相关的区域，提高模型的可解释性和查询特定的位置标注能力，同时显著提高了推理效率。配备TIE的VLMs能够在较少的图像瓷砖使用下实现优于传统VLMs的性能，表明基于文本的训练能够有效优化编码器以捕捉关键的视觉特征。
## 399. `cs.CV` - 通过Null-文本嵌入优化实现从文本到图像的扩散模型的推理时对齐 [PDF](https://arxiv.org/pdf/2511.20889), [HTML](https://arxiv.org/abs/2511.20889)
### Authors
Taehoon Kim,Henry Gouk,Timothy Hospedales
### Background
现有的Test-time alignment (TTA)方法在优化目标奖励函数时，要么优化不足，要么过分优化（导致奖励欺诈），这限制了模型在实际应用中的表现。
### Innovation
提出了一种新的方法Null-Text Test-Time Alignment (Null-TTA)，通过优化条件无关嵌入来调整扩散模型，而不是操控潜在变量或噪声变量。这种方法确保了对齐发生在语义连贯的空间中，并防止了奖励欺诈。
### Conclusion
实验表明，Null-TTA在目标测试时对齐方面达到了最先进的性能，同时保持了跨奖励的一般性。这证明了语义空间优化作为一种有效且基于原理的新TTA范式的有效性。
## 400. `cs.CV` - Split-then-Merge方法的层知觉视频合成 [PDF](https://arxiv.org/pdf/2511.20809), [HTML](https://arxiv.org/abs/2511.20809)
### Authors
Ozgur Kara,Yujia Chen,Ming-Hsuan Yang,James M. Rehg,Wen-Sheng Chu,Du Tran
### Background
该研究旨在解决生成视频合成中的控制问题及其数据稀缺性问题。传统的生成视频合成方法依赖于带标注的数据集或手工地制定规则，这导致了在没有足够数据支持的情况下难以生成高质量的合成视频。
### Innovation
该研究提出了一种新颖的框架——Split-then-Merge (StM)，它将大量未标记的视频分割成动态前景和背景层，然后通过自我合成来学习动态主体与不同场景的交互方式。此外，StM 引入了一个具有多层融合和增强的新颖训练流程，以实现行为感知合成，并通过身份保护损失保持合成前景的忠实度。
### Conclusion
实验结果表明，StM 方法在定量基准和人类/视觉语言模型的定性评估中均优于现有最佳方法。更多详细信息可以在项目页面上找到：this https URL
## 401. `cs.CV` - 基于口吃查询的无监督记忆性建模 [PDF](https://arxiv.org/pdf/2511.20854), [HTML](https://arxiv.org/abs/2511.20854)
### Authors
Sree Bhattacharyya,Yaman Kumar Singla,Sudhir Yarram,Somesh Kumar Singh,Harini S I,James Z. Wang
### Background
视觉内容的记忆性已引起了科学界几十年的关注，其应用范围广泛，从理解人类记忆的细微方面到增强内容设计。提高该领域的挑战之一是收集视觉内容记忆性的昂贵人力标注过程，这限制了记忆性数据集的多样性和扩展性。大多数现有数据集仅收集视觉内容的记忆性评分，而未能捕捉自然、开放描述中存在的细微记忆性信号。
### Innovation
本文介绍了第一个用于建模视觉记忆性信号的大型无监督数据集，包含超过82,000个视频，并配有描述性回忆数据。利用在线平台如Reddit的口吃 查询。本研究展示了无监督数据集为两种记忆性相关任务：回忆生成和口吃检索提供了丰富的信号。使用大规模视觉语言模型在本数据集上微调的结果在生成开放式的视觉内容记忆描述方面超过了GPT-4o等现有的模型。同时采用对比训练策略创建了第一个能够完成跨模态口吃检索的模型。
### Conclusion
本数据集和模型为视觉内容记忆性研究提出了一个新的方向，促进了该领域的进展。
## 402. `cs.CV` - 重新审视KRISP：一种基于知识增强的视觉-语言模型的轻量级复现与分析 [PDF](https://arxiv.org/pdf/2511.20795), [HTML](https://arxiv.org/abs/2511.20795)
### Authors
Souradeep Dutta,Keshav Bulia,Neena S Nair
### Background
Facebook AI Research引入了KRISP [4]，它将结构化外部知识整合到视觉-语言推理管道中。尽管模型效果显著，但它最初是为了工业规模的训练而设计的，计算需求高，并且紧密依赖一个大型骨干网络。
### Innovation
本文从不同角度重新审视了KRISP，并提供了一个具有显著减少参数数量的轻量级复现版本。尽管复现模型的性能大约为原模型的75%，但复现过程揭示了多种设计缺陷、实际问题以及原来论文中未充分覆盖的问题。通过系统性的消融研究，本文为资源受限环境下的知识增强VQA架构的可扩展性和有效性提供了见解，这些研究包括对合成VQA数据的实证概念证明及在DAQUAR数据集上的评估。复现模型在参数设置较低的情况下运行，并通过外部知识图谱领域进行限制，防止了AI幻觉，并生成完全局限于该领域的输出。
### Conclusion
本文的模型在资源受限的情况下，通过边缘设备如智能手机和AR-VR进一步增强了离线视觉推理的功能。
## 403. `cs.CV` - GaINeR: 几何感知的隐式网络表示 [PDF](https://arxiv.org/pdf/2511.20924), [HTML](https://arxiv.org/abs/2511.20924)
### Authors
Weronika Jakubowska,Mikołaj Zieliński,Rafał Tobiasz,Krzysztof Byrski,Maciej Zięba,Dominik Belter,Przemysław Spurek
### Background
隐式神经表示（INRs）已成为连续2D图像建模的关键工具，能够实现高保真重建、超分辨和压缩。SIREN、WIRE和FINER等流行架构展示了INRs捕捉图像细节的潜力。然而，传统的INRs缺乏明确定义的几何结构，限制了它们在动态或交互式设置中的应用，尤其是在需要局部编辑或与物理模拟结合的情况下。
### Innovation
本文提出了一种新颖的几何感知隐式网络表示（GaINeR），结合了可训练的高斯分布和基于神经网络的INR。该模型对于给定的图像坐标，检索最近的K个高斯分布，聚合距离加权嵌入，并通过神经网络预测RGB值。此设计为图像提供了连续表示、可解释的几何结构和灵活的局部编辑功能，为物理感知和交互式的图像操作奠定了基础。
### Conclusion
该方法为2D图像提供了一种新的几何感知隐式表示方式，具备连续图像表示、可解释的几何结构和灵活的局部编辑能力，可以为物理感知和交互式的图像操作提供支持。
## 404. `cs.CV` - 动态采样网络的有趣性质 [PDF](https://arxiv.org/pdf/2511.20800), [HTML](https://arxiv.org/abs/2511.20800)
### Authors
Dario Morle,Reid Zaffino
### Background
动态采样机制在深度学习架构中已经在各种计算机视觉模型中展示了实用性，但这些结构的理论分析尚未统一。
### Innovation
研究人员开发了一种新的操作
### Conclusion
通过我们的形式化分析，我们揭示了动态采样网络在模型训练中正向传播和反向传播之间的一种独特不对称性。我们证明，这些机制构成了一类与传统平移不变算子（由卷积定义）完全不同的算子。我们发现了确保动态采样网络稳定训练的必要条件。此外，我们还研究了离散化效应的统计分析，并提出了一种新的损失landscape可视化方法，直接利用梯度更新信息，以更好地理解学习行为。
## 405. `cs.CV` - UruDendro4: 在针叶树Pinus taeda L.切片图像中的自动树轮检测基准数据集 [PDF](https://arxiv.org/pdf/2511.20935), [HTML](https://arxiv.org/abs/2511.20935)
### Authors
Henry Marichal,Joaquin Blanco,Diego Passarella,Gregory Randall
### Background
树轮生长代表了树木每年的木质增量，量化这一过程可以帮助研究人员评估哪些森林采伐管理措施最适合每种树种。传统的测量方法耗时且不精确，通常是在圆盘横截面上沿4到8个径向方向进行测量。近年来，自动化算法和数据集的出现提高了准确度并实现了对树轮的自动识别。然而，由于缺乏木材横截面数据，如何利用自动识别方法改进树轮检测技术成为一个挑战。
### Innovation
本文提出了UruDendro4数据集，这是一个由102张针叶树Pinus taeda L.横截面样本组成的集合，每张样本都有手工标注的年轮。与现有公共数据集不同，UruDendro4数据集包括沿树干不同高度提取的样本，可用于基于手工标注年轮进行木材年生长量的体积建模。此外，本文还提供了使用最新技术在该数据集上进行自动环形检测的性能基准，结果显示DeepCS-TRD方法表现最佳，并进行了一系列删减实验验证最终参数配置的有效性。
### Conclusion
本文引入了UruDendro4数据集，并展示了在这种数据集上进行自动树轮检测的技术性能基准，表明利用该数据集训练的模型在树轮检测任务中具有更好的泛化能力。
## 406. `cs.CV` - BUSTR: 配有特征感知视觉语言模型的乳腺超声文本报告 [PDF](https://arxiv.org/pdf/2511.20956), [HTML](https://arxiv.org/abs/2511.20956)
### Authors
Rawa Mohammed,Mina Attin,Bryar Shareef
### Background
自动化放射学报告生成（RRG）在乳腺超声（BUS）中的应用受到缺乏成对的图像-报告数据集的限制，并且还面临着大型语言模型可能产生的幻觉风险。传统的报告生成方法通常需要成对的图像-报告监督以构造报告，而这些数据集难以获取。
### Innovation
我们提出了一种多任务视觉语言框架BUSTR，用于生成无需成对的图像-报告监督的BUS报告。BUSTR框架通过结构描述符（如BI-RADS、病理学、组织学）和影像学特征来构建报告，并使用多头Swin编码器和多任务损失学习特征感知的视觉表示。它还通过结合标记级交叉熵和输入输出表示之间的余弦相似度对齐损失，实现视觉和文本标记的对齐。
### Conclusion
在两个公开的乳腺超声数据集BrEaST和BUS-BRA上，BUSTR在标准自然语言生成指标和临床有效性指标上均取得显著提升，特别是在BI-RADS类别和病理学等关键目标上。实验结果表明，这种配备特征感知视觉模型，通过结合标记级和对齐损失进行训练，可以在无需成对图像-报告数据的情况下提高自动化报告质量和临床有效性。
## 407. `cs.CV` - RefOnce: 将参考信息提炼到类原型记忆中进行遮蔽目标检测 [PDF](https://arxiv.org/pdf/2511.20989), [HTML](https://arxiv.org/abs/2511.20989)
### Authors
Yu-Huan Wu,Zi-Xuan Zhu,Yan Wang,Liangli Zhen,Deng-Ping Fan
### Background
当前的遮蔽目标检测系统需要在测试时提供参考图像，这限制了系统的部署能力，增加了延迟和数据收集负担。
### Innovation
提出了一种RefOnce框架，该框架在训练过程中提炼参考信息到类原型记忆中，并在推断过程中通过查询条件混合原型来合成参考向量，从而在没有测试时参考图像的情况下提供简单的、高效的方法实现遮蔽目标检测。此外，还提出了双向注意对齐模块来弥合参考统计与遮蔽查询特征之间的表示差距。
### Conclusion
在大规模的R2C7K基准测试上评估了所提出的方法。广泛的实验证明了该方法在与最近的领先方法相比时，具有竞争力的或更优的性能。实现了该方法的代码已开源。
## 408. `cs.CV` - TrafficLens: 使用大语言模型进行多摄像头交通视频分析 [PDF](https://arxiv.org/pdf/2511.20965), [HTML](https://arxiv.org/abs/2511.20965)
### Authors
Md Adnan Arefeen,Biplob Debnath,Srimat Chakradhar
### Background
城市地区的交通摄像头对于智能交通系统至关重要，能够增强执法能力、交通管理和行人安全。然而，高效管理和分析多摄像头的视频数据是一项挑战，因为这涉及到处理大量的数据。高级分析工具是必要的。尽管像ChatGPT这样的大型语言模型（LLMs）在文本任务上表现出色，但要将其集成到交通视频分析中，则需要将视频数据转换为文本，这需要使用视觉-语言模型（VLM），该过程耗时且延迟了交通视频的及时利用，从而不能快速生成信息洞见并调查事件。
### Innovation
本文提出了一种名为TrafficLens的专有算法，用于处理多摄像头交通交叉路口的视频。TrafficLens采用逐步方法，利用摄像机的重叠覆盖区域。它通过使用不同的标记限制逐步应用VLM，并使用先前输出作为后续摄像头的提示，从而加快了详细文本描述的生成速度并降低了处理时间。此外，通过对象级别的相似性检测器，TrafficLens能够智能地跳过冗余的VLM调用。
### Conclusion
实验结果表明，使用TrafficLens处理交通视频可以将视频到文本的转换时间减少多达四倍，同时保持信息的准确性。
## 409. `cs.CV` - 利用轻量级同态加密实现医学AI中的隐私保护联邦视觉变换器学习 [PDF](https://arxiv.org/pdf/2511.20983), [HTML](https://arxiv.org/abs/2511.20983)
### Authors
Al Amin,Kamrul Hasan,Liang Hong,Sharif Ullah
### Background
跨医疗机构的合作机器学习有望通过利用多样化的数据集提高诊断准确性，但隐私法规如HIPAA禁止直接共享患者数据。联邦学习（FL）能够在不交换原始数据的情况下实现分散训练，但仍有一些研究显示，在传统FL中，模型梯度易于受到重建攻击，这可能暴露敏感的医疗信息。本文提出了一种结合Vision Transformers (ViT)与同态加密（HE）的隐私保护联邦学习框架，以确保安全的多机构组织的组织病理学分类。该方法利用ViT的CLS令牌作为紧凑的768维特征表示进行安全聚合，并在传输到服务器前对这些令牌进行CKKS同态加密。
### Innovation
该文章的创新点在于提出了一种结合Vision Transformers（ViT）与同态加密（HE）的隐私保护框架，特别通过加密CLS令牌实现了与梯度加密相比30倍的通信量减少，同时保持了强大的隐私保证。加密的CLS令牌能够防止模型反转攻击，同时允许在密文上直接进行加密推理，通信量需求极低。该方法在未加密域和加密域分别实现了96.12%和90.02%的全球分类准确率。
### Conclusion
该研究通过实验证明了所提出的CLS保护HE方法能够在确保隐私保护的同时，实现高效的联邦学习训练，并在跨医疗机构的肺癌组织病理分类中实现了高分类准确率。
## 410. `cs.CV` - 知识完善视觉：一种面向新闻图像字幕的多模态实体感知检索增强生成框架 [PDF](https://arxiv.org/pdf/2511.21002), [HTML](https://arxiv.org/abs/2511.21002)
### Authors
Xiaoxing You,Qiang Huang,Lingyu Li,Chi Zhang,Xiaopeng Liu,Min Zhang,Jun Yu
### Background
新闻图像字幕的目标是通过结合视觉内容与相关文章的上下文线索来生成具有记者意义的信息描述。尽管最近取得了进展，但现有方法在处理三个关键挑战方面表现不佳：（1）不完整的信息覆盖；（2）跨模态对齐较弱；（3）视觉实体落地区域不够优化。
### Innovation
本文介绍了一种新的多模态实体感知检索增强生成框架MERGE，用于新闻图像字幕。MERGE构建了一个以实体为中心的多模态知识库（EMKB），将文本、视觉和结构化知识整合在一起，实现增强的背景检索。通过多阶段假设-字幕策略提高跨模态对齐，并通过基于图像内容的动态检索增强视觉实体匹配。
### Conclusion
实验结果表明，MERGE在GoodNews和NYTimes800k数据集上的表现显著优于现有基线，在字幕质量上的CIDEr得分提高了+6.84，在实体识别上的F1分数提高了+4.14。值得注意的是，MERGE对于未见过的视觉新闻数据集也表现出色，CIDEr得分提高了+20.17，F1分数提高了+6.22，显示出很强的稳健性和领域适应性。
## 411. `cs.CV` - 开放词汇集组成解释在神经元对齐中的应用 [PDF](https://arxiv.org/pdf/2511.20931), [HTML](https://arxiv.org/abs/2511.20931)
### Authors
Biagio La Rosa,Leilani H. Gilpin
### Background
神经元是深度神经网络的基本构建块，它们之间的连接使AI能够实现前所未有的成果。受理解神经元如何编码信息的启发，组合解释利用概念之间的逻辑关系来表达神经元激活与人类知识之间的空间对齐关系。然而，这些解释依赖于人类标注的数据集，这限制了它们在特定领域和预定义概念上的适用性。
### Innovation
本文提出了一种用于视觉领域的框架，允许用户针对任意概念和数据集探索神经元。该框架利用开放式词汇集语义分割生成的掩码来计算开放式词汇集组合解释。提出框架包括三个步骤：指定任意概念、使用开放式词汇集模型生成语义分割掩码以及从这些掩码中推导出组合解释。与计算组合解释的先前方法相比，该框架在定量指标和人类可解释性方面进行了比较，分析了从人类标注数据转向模型标注数据时解释的差异，并展示了该框架提供的灵活性。
### Conclusion
该研究通过对比提出的框架和先前方法在量化指标和人类可解释性方面的表现，分析了在从人类标注数据变化到模型标注数据时解释的差异，并展示了该框架提供了任务和感兴趣属性方面解释的灵活性。
## 412. `cs.CV` - 无反转流的双重双重修正流无转换风格转移 [PDF](https://arxiv.org/pdf/2511.20986), [HTML](https://arxiv.org/abs/2511.20986)
### Authors
Yingying Deng,Xiangyu He,Fan Tang,Weiming Dong,Xucheng Yin
### Background
风格迁移是一项关键的图像处理任务，它通过无缝融合现实内容和艺术风格生成视觉上引人注目的图像，广泛应用于照片编辑和创意设计。近年来，主流的无需训练的方法在风格迁移方面取得了巨大进步，但依赖于计算反转过程的这些方法在效率上有所损失，并且当反转不准确时还会引入视觉失真。
### Innovation
本文提出了一种基于双重修正流的新颖的无需反转风格迁移框架，能够通过前向传递确定未知的风格化分布，同时并行预测内容和风格轨迹，并通过一种动态的中间点插值方法融合这些轨迹，该方法整合了两条路径的速度并适应图像的变化。通过联合建模内容、风格和风格化分布，我们的速度场设计实现了稳健的融合并避免了简单叠加的不足。注意力注入进一步指导了风格的融合，从而提高了视觉保真度、内容保留和计算效率。
### Conclusion
大量实验展示了该方法在多样风格和内容上的通用性，提供了一种有效且高效的风格迁移管线。
## 413. `cs.CV` - 从修补到分层分解：将生成式修补模型重新用于图像分层分解 [PDF](https://arxiv.org/pdf/2511.20996), [HTML](https://arxiv.org/abs/2511.20996)
### Authors
Jingxi Chen,Yixiao Zhang,Xiaoye Qian,Zongxia Li,Cornelia Fermuller,Caren Chen,Yiannis Aloimonos
### Background
图像可以被视为分层组合，前景对象在背景之上，可能存在遮挡。这种分层表示使独立编辑元素成为可能，为内容创造提供了更大的灵活性。尽管大型生成模型取得了进展，但将单张图像分解为多层依然具有挑战性，这主要是由于方法和数据的局限性。
### Innovation
本文观察到分层分解与修补任务之间的强关联性，提出使用基于扩散的修补模型进行轻量级微调以实现分层分解。此外，提出了一种新型多模态上下文融合模块，具有线性注意力复杂度，以进一步在潜在空间中保留细节。模型仅基于从开源资源构建的合成数据集进行训练，实现了在对象移除和遮挡恢复上的卓越性能，为下游编辑和创造应用开辟了新的可能性。
### Conclusion
本文提出的方法对图像分层分解问题具有很高的性能，并通过集成新颖的上下文融合模块进一步优化了细节保留。这种方法不仅展示了如何将现有的生成式修补模型重新用于新的任务，也提供了面向未来内容创造的新应用方向。
## 414. `cs.CV` - 波前约束的被动隐匿目标检测 [PDF](https://arxiv.org/pdf/2511.20991), [HTML](https://arxiv.org/abs/2511.20991)
### Authors
Zhiwen Zheng,Yiwei Ouyang,Zhao Huang,Tao Zhang,Xiaoshuai Zhang,Huiyu Zhou,Wenwen Tang,Shaowei Jiang,Jin Liu,Xingru Huang
### Background
准确地从超出视场的微弱光斑模式中定位和分割被遮挡的对象极具挑战性，因为存在多重散射和介质引起的扰动。大多数现有的方法基于实值建模或局部卷积操作，无法捕捉相干光传播的物理特性。在低信噪比条件下，这些方法常常会收敛到非物理的解，严重损害了观测的稳定性和可靠性。
### Innovation
提出了一个新颖的物理驱动的波前传播补偿网络（Wavefront Propagating Compensation Network，简称WavePCNet），用于模拟波前传播并增强对被遮挡对象的感知。WavePCNet整合了三相波前复传播重构（TriWCP），它结合了复数幅度转移算子来精确限制相干传播行为，并引入动量记忆机制来有效地抑制扰动的累积。此外，引入了高频交叉层补偿增强，构建了具有多尺度感受野的频率选择性路径，以动态建模各层之间的结构一致性，进一步增强了模型在复杂环境条件下的鲁棒性和可解释性。
### Conclusion
在四个物理收集的数据集上进行的广泛实验表明，WavePCNet在准确性和鲁棒性方面始终优于最新方法。
## 415. `cs.CV` - MetaRank：模型转移性评估的任力建模选择 [PDF](https://arxiv.org/pdf/2511.21007), [HTML](https://arxiv.org/abs/2511.21007)
### Authors
Yuhang Liu,Wenjie Zhao,Yunhui Guo
### Background
在迁移学习中，选择合适的预训练源模型是一个关键但计算成本高昂的任务。模型转移性估计（MTE）方法通过提供无需完全调优即可评估模型效率的代理指标来解决这一问题。然而，实践中选择哪种MTE指标通常缺乏系统的指导，依赖于历史性能指标。研究发现，不同任务下MTE指标的有效性差异显著，没有一种通用的最佳指标。
### Innovation
MetaRank引入了一种基于元学习的自动任务感知MTE指标选择框架，将指标选择问题转化为学习排序问题。MetaRank通过预训练的语言模型将数据集和MTE指标的文本描述编码到共享的语义空间中，并通过优化列表目标在线学习数据集特性与指标机制之间的关系。实验结果证明了MetaRank的优越性。
### Conclusion
通过广泛的实验对比，MetaRank在11个预训练模型和11个目标数据集上的表现证明了其强大的有效性，能够根据数据集的文本描述高效地选择出最适合的MTE指标，从而帮助实践者在收集更多数据前做出事先决策。
## 416. `cs.CV` - 结构导向原型引导的可信多视图分类 [PDF](https://arxiv.org/pdf/2511.21021), [HTML](https://arxiv.org/abs/2511.21021)
### Authors
Haojian Huang,Jiahao Shi,Zhe Liu,Harold Haodong Chen,Han Fang,Hao Sun,Zhongjiang He
### Background
在复杂场景中，多源信息往往具有异质性、不一致性甚至是冲突，这给实现可靠的决策带来了挑战。目前的多视图分类（Multi-view Classification，MVC）方法主要依赖于全局密集的邻居关系来建模同视图的关系，导致计算成本高并且不直接保证跨视图关系的一致性。此外，这些方法通常通过手工赋予权重来聚合不同视图的证据，缺乏在类空间中确保所学习的多视图邻居结构一致性的保证，因此影响了分类结果的可信度。
### Innovation
本文提出了一种新颖的多视图分类（Trusted Multi-view Classification，TMVC）框架，引入了原型来表示每个视图的邻居结构。通过简化同视图邻居关系的学习并实现同视图与跨视图结构的动态对齐，该方法促进了交叉视图共识的更高效和一致的发现。
### Conclusion
在多个公开的多视图数据集上的广泛实验表明，本文的方法在下游性能和鲁棒性方面与流行的TMVC方法相比具有竞争力。
## 417. `cs.CV` - MUSE：通过测试时优化统一框架操纵图像中情感合成 [PDF](https://arxiv.org/pdf/2511.21051), [HTML](https://arxiv.org/abs/2511.21051)
### Authors
Yingjie Xia,Xi Wang,Jinglei Shi,Vicky Kalogeiton,Jian Yang
### Background
图像能够激发深刻的情感，这些情感往往在感知中占据优先地位。现有的Image Emotional Synthesis（IES）方法将生成和编辑任务分离，导致效率低下，并限制了能够自然结合这两类操作的应用，如疗愈干预或故事叙述。
### Innovation
MUSE 是第一个集成了情感生成和编辑的统一框架，通过参考Test-Time Scaling（TTS）策略，它避免了附加更新扩散模型和特定情感合成数据集的需要。MUSE 解决了情感合成中的三个核心问题：通过梯度优化情感标记稳定引导合成、使用语义相似度作为监督信号确定适时引入情感指导的最佳时机，以及通过多情感损失函数减少与其他情感的干扰，准确引导合成。
### Conclusion
实验结果表明，MUSE 在生成和编辑方面优于所有现有方法，提高了情感准确性并保持了内容、文本提示的忠诚度和现实情感表达之间的最佳平衡。MUSE 为情感合成设定了新的范式。
## 418. `cs.CV` - PG-ControlNet: 一种基于物理指导的ControlNet生成空间变化的图像去模糊方法 [PDF](https://arxiv.org/pdf/2511.21043), [HTML](https://arxiv.org/abs/2511.21043)
### Authors
Hakki Motorcu,Mujdat Cetin
### Background
空间变化的图像去模糊仍然是一个基础性的病态问题，特别是在面对复杂运动和其他形式的模糊的混合体以及显著噪声时。现有的基于学习的方法一般分为两类：一类是基于模型的深度递归方法，通过建模退化来施加物理约束，但往往会生成过度平滑和带有瑕疵的纹理；另一类是生成模型，能够实现更好的感知质量，但由于物理约束较弱，容易产生虚假细节。
### Innovation
提出了一种新的框架，通过显式且密集的物理约束来驯服强大的生成先验，独特地调和了这两种方法的优势。不简化退化域，而是将其建模为高维压缩内核的密集连续体，确保捕捉到运动和其他退化模式的微小变化。利用这一丰富的描述子域来条件化ControlNet架构，强烈指导扩散采样过程。
### Conclusion
广泛的实验表明，我们的方法有效弥合了物理准确性与感知现实性之间的差距，在挑战性的严重模糊场景中，不仅超越了基于模型的最先进的方法，还在生成基准方面表现更好。
## 419. `cs.CV` - 超越现实：借助StickerNet学习富有表达性的图像组成艺术 [PDF](https://arxiv.org/pdf/2511.20957), [HTML](https://arxiv.org/abs/2511.20957)
### Authors
Haoming Lu,David Kocharian,Humphrey Shi
### Background
传统的图像组成研究主要关注视觉真实性和语义合理性，但在现代内容创作的实际编辑场景中，许多组成的图片不是为了保留真实性。相反，社交媒体用户出于获得社区认可的目的，往往倾向于创作更具有艺术性、趣味性或社交性的内容。基于这一观察，该研究重新定义了表达性组成的任务，旨在包容风格多样性，并采用较为宽松的摆放逻辑，以反映用户在真实世界创编辑平台上的编辑方式。
### Innovation
本文提出了StickerNet，这是一个两阶段框架，首先确定组成类型，然后预测透明度、掩模、位置和缩放等放置参数。不同于先前的工作通过在真实图像上模拟对象放置来构建数据集，StickerNet直接从一个匿名在线视觉创作和编辑平台上收集的180万编辑操作中构建数据集，每个操作都反映了用户社区验证的放置决策。这种基于真实的编辑行为的场景确保了任务定义与训练监督的强关联性。
### Conclusion
用户研究和定量评估表明，StickerNet在性能上优于通用基准，并且接近人类放置行为，证明了在任务固有模糊性的前提下，通过对真实世界编辑模式学习可以取得显著效果。该工作提出了一种新的视觉理解方向，强调表达性和用户意图，而非真实性。
## 420. `cs.CV` - CameraMaster：统一的相机语义和参数控制以实现摄影修图 [PDF](https://arxiv.org/pdf/2511.21024), [HTML](https://arxiv.org/abs/2511.21024)
### Authors
Qirui Yang,Yang Yang,Ying Zeng,Xiaobin Hu,Bo Li,Huanjing Yue,Jingyu Yang,Peng-Tao Jiang
### Background
文本指导的扩散模型在图像编辑和生成方面取得了巨大进展，但仍难以实现具有精准参数控制（如曝光、白平衡、缩放）的物理一致的图像修图。现有方法要么依赖于含糊不清且交织的文本提示，妨碍了精准的摄像控制；要么通过训练单独的头部/权重来调整参数，这降低了可扩展性、多参数组合能力和对细微变化的敏感性。
### Innovation
提出了一种名为CameraMaster的统一相机感知框架，用于图像修图。该框架通过明确解耦相机指令，并整合关键信息流来实现，包括捕捉摄影师意图的指令表示，以及编码精确相机设置的参数嵌入。通过参数嵌入，模型可以调节相机指令和内容语义，并通过交叉注意机制将其注入内容特征中，产生高度相机敏感的语义上下文。此外，指令和相机嵌入被用作条件和门信号注入到时间嵌入中，使整个去噪过程中的调节统一且分层，并强制语义-参数对齐。
### Conclusion
构建了一个包含78K带有相机参数标注的图像-提示对的大型数据集来训练和评估CameraMaster。实验结果显示，CameraMaster对参数变化有单调且接近线性的响应，支持无缝的多参数组合，并显著优于现有方法。
## 421. `cs.CV` - GuardTrace-VL：通过迭代安全监督检测不安全的多模态推理 [PDF](https://arxiv.org/pdf/2511.20994), [HTML](https://arxiv.org/abs/2511.20994)
### Authors
Yuxiao Xiang,Junchi Chen,Zhenchao Jin,Changtao Miao,Haojie Yuan,Qi Chu,Tao Gong,Nenghai Yu
### Background
多模态大推理模型（MLRM）越来越多地用于产生显式中间推理的过程的视觉语言任务。然而，即使最终答案是无害的，推理过程中的推理痕迹也可能包含潜在的有害内容，这可能带来部署风险。现有的多模态安全防护措施主要仅评估输入问题和最终答案，忽略了中间推理过程，这使得某些潜在危害无法被检测到，例如基于偏见的推断或视觉上下文的政策违规使用。本文指出，这种忽视导致了潜在危害在推理过程中无法被发现。
### Innovation
本文提出了一种名为GuardTrace-VL的视觉感知安全审计器。它通过联合图像-文本分析来监督整体问题-思考-答案（QTA）处理流程，能够在推理阶段检测有害内容的出现。为了支持训练和评估，作者构建了一个GuardTrace数据集，通过多样化的提示策略生成，并通过机器多模态推理模型和人工投票及验证流程进行细化。此外，还提出了渐进式三阶段训练方案，结合数据精炼过程，使模型能够根据不同风险水平学习到较为复杂的和上下文依赖的安全偏好。
### Conclusion
在提出的包含领域内和领域外场景的测试集上，GuardTrace-VL模型在有害推理检测任务上的F1分数达到了93.1%，相比之前最强的多模态安全防护方法，F1分数提高了13.5%。代码也将公开提供。
## 422. `cs.CV` - MIRA: 多模态迭代推理代理用于图像编辑 [PDF](https://arxiv.org/pdf/2511.21087), [HTML](https://arxiv.org/abs/2511.21087)
### Authors
Ziyun Zeng,Hang Hua,Jiebo Luo
### Background
指令引导的图像编辑为用户提供了一种通过自然语言直观编辑图像的方法。然而，基于扩散的编辑模型经常难以准确解释复杂的用户指令，特别是在涉及组合关系、上下文线索或引用表达的情况下，这导致了编辑的语义漂移或不能反映出预期的变化。
### Innovation
我们提出了一个多模态迭代推理代理（MIRA），这是一种轻量级、即插即用的多模态推理代理，通过迭代感知-推理-操作循环进行编辑，有效地模拟了多轮的人工模型交互过程。MIRA 逐步预测原子编辑指令，利用视觉反馈来做决策，而非发布单一的提示或静态计划。还构建了一个150K多模态工具使用数据集MIRA-Editing，与两次训练管道的SFT + GRPO相结合，使得MIRA能够处理复杂的编辑指令并进行推理和编辑。
### Conclusion
当与开源图像编辑模型（如Flux.1-Kontext、Step1X-Edit和Qwen-Image-Edit）结合使用时，MIRA显著提高了语义一致性和感知质量，其性能与GPT-Image和Nano-Banana等专有系统相当或优于后者。
## 423. `cs.CV` - CaptionQA：你的描述是否与原始图像一样有用？ [PDF](https://arxiv.org/pdf/2511.21025), [HTML](https://arxiv.org/abs/2511.21025)
### Authors
Shijia Yang,Yunong Liu,Bohan Zhai,Ximeng Sun,Zicheng Liu,Emad Barsoum,Manling Li,Chenfeng Xu
### Background
图像说明在多模态系统（如检索、推荐和多步代理推理管道）中作为视觉内容的有效替代品，但现有的评估实践并未涉及到一个根本问题——描述是否能在实际下游任务中替代图像。本文提出了一个基于使用价值的基准测试CaptionQA，以评估模型生成的描述，其中描述质量通过它对下游任务的支持程度来衡量。CaptionQA是一个可扩展的专业化的基准测试，涵盖了自然、文档、电子商务和具身人工智能4个领域，每个领域都有详细的分类系统，有助于识别特定领域任务所需的信息。CaptionQA建立了一个包含33,027个密集标注的多项选择题的数据集（平均每张图片50.3个问题），并明确规定需要视觉信息来回答，全面探测描述的用途。在评估过程中，通过大型语言模型单独使用描述来回答这些问题，直接测量描述是否能保留图像级别的用途，并能被下游的大模型利用。
### Innovation
提出了一个基于使用价值的基准测试CaptionQA，旨在评估模型生成的描述是否能在实际下游任务中替代图像。CaptionQA是多领域的可扩展基准测试，它包含33,027个详细的多项选择题，覆盖4个领域，每个领域都有详细的分类系统。通过这种基准测试，发现最先进的模型在传统图像-问答基准上几乎相同的情况下，其描述的用途可能会下降高达32%。
### Conclusion
本文发布了一个基于使用价值的基准测试CaptionQA，包括一个包含33,027个密集标注的多项选择题的大型数据集，涵盖4个领域。该基准测试的结果显示了大模型在描述用途上的重大差距，并为此领域提供了一个新的评估方法。同时，也提供了可扩展的开源管道以扩展到新领域，并提供了代码下载链接。
## 424. `cs.CV` - EM-KD: 使用不平衡视觉标记匹配提炼高效多模态大型语言模型 [PDF](https://arxiv.org/pdf/2511.21106), [HTML](https://arxiv.org/abs/2511.21106)
### Authors
Ze Feng,Sen Yang,Boqiang Duan,Wankou Yang,Jingdong Wang
### Background
现有的高效多模态大型语言模型（MLLMs）通过压缩视觉标记来减少资源消耗，但这也导致了视觉信息的丢失，进而降低了理解能力。虽然一些方法引入了知识蒸馏来提升学生模型的效果，但它们忽略了高效学生模型和标准教师模型之间细微视觉理解差异的本质问题。教师模型和学生模型之间的视觉标记不平衡是一个主要挑战。
### Innovation
本文提出了EM-KD（已经匹配的知识蒸馏），一种新颖的提炼方法，旨在提升高效MLLMs。该方法首先计算教师和学生模型的视觉逻辑之间的曼哈顿距离，并使用匈牙利匹配算法在空间维度上进行对齐。此后，EM-KD引入了两种蒸馏策略：视觉-语言亲合力蒸馏（VLAD）和视觉语义蒸馏（VSD）。VLAD计算文本标记与对齐视觉标记之间的亲合力矩阵，并最小化学生和教师亲合力矩阵的光滑L1距离。考虑到最终视觉逻辑层的语义丰富性，VSD使用逆KL散度来测量对齐视觉逻辑在词汇空间中的离散概率分布。
### Conclusion
EM-KD训练的模型在多样化的基准测试中表现出色，不仅在准确性和效率方面大幅超过了先前的高效MLLMs，在公平对比的情况下，还比之前的所有蒸馏方法都表现出更好的性能，验证了其有效性和优越性。
## 425. `cs.CV` - FaithFusion: 像素级信息增益实现重建与生成的协调 [PDF](https://arxiv.org/pdf/2511.21113), [HTML](https://arxiv.org/abs/2511.21113)
### Authors
YuAn Wang,Xiaofan Li,Chi Huang,Wenhao Zhang,Hao Li,Bosheng Wang,Xun Sun,Jun Wang
### Background
在可控驾驶场景重建和3D场景生成中，保持几何保真度的同时在大视角变化下合成视觉上可接受的外观至关重要。然而，基于几何的3D生成（3DGS）与基于外观的扩散模型的有效融合存在固有的挑战，因为缺少像素级的、3D一致的编辑准则会导致过度恢复和几何偏移。
### Innovation
本文提出了FaithFusion，这是一种由像素级期望信息增益（EIG）驱动的3DGS-扩散融合框架。EIG作为一种统一的策略指导空间合成，作为空间先验引导扩散以细化高不确定性区域，同时其像素级加权将编辑内容回注入3DGS。实验表明，该方法在Waymo数据集上达到了SOTA性能，即使在6米车道偏移下FID仍为107.47。
### Conclusion
我们的方法克服了以往技术的局限性，无需额外的先验条件或结构，实现了在大视角变化下几何保真度与视觉现实的统一。实验结果表明，在NTA-IoU，NTL-IoU，FID等指标上取得了SOTA性能，在6米车道偏移时FID仍达到107.47。我们的代码可在此处获取。
## 426. `cs.CV` - Pygmalion Effect in Vision: Image-to-Clay Translation for Reflective Geometry Reconstruction [PDF](https://arxiv.org/pdf/2511.21098), [HTML](https://arxiv.org/abs/2511.21098)
### Authors
Gayoung Lee,Junho Kim,Jin-Hwa Kim,Junmo Kim
### Background
3D重建中理解反射一直是一个长期存在的挑战，因为反映了视点相关的几何和外观的纠缠。
### Innovation
提出了一种新颖的框架，名为Pygmalion Effect in Vision，它通过图像到黏土转化来“雕塑”反射物体。此方法采用双分支网络，一个基于BRDF的反光分支和一个由黏土引导的稳定几何和细化表面法线的分支。合成的黏土样图像提供了一种中性的、无反射的监督信号，补充了反射视图。
### Conclusion
实验在合成和真实数据集上展示了相比现有反射处理方法在法线准确性和网格完整性上的显著改进。该框架还揭示了通过消除反射来观察，可以作为反射物体几何学习的强大归纳偏置。
## 427. `cs.CV` - 导致分布偏移的哪一层？一种熵导向的自适应剪枝方法用于扩散和流模型 [PDF](https://arxiv.org/pdf/2511.21122), [HTML](https://arxiv.org/abs/2511.21122)
### Authors
Changlin Li,Jiawei Zhang,Zeyi Shi,Zongxin Yang,Zhihui Li,Xiaojun Chang
### Background
大规模的视觉生成模型，如扩散和流模型，在视觉生成任务中表现出色。然而，这些预训练模型在下游任务上的迁移往往会导致大量参数冗余。
### Innovation
该论文提出了一个名为 EntPruner 的熵导向自动化渐进剪枝框架，专为扩散和流模型设计。引入了熵导向的剪枝策略，这是一个针对生成模型的模块级重要性评估策略。提出了Conditional Entropy Deviation (CED)，用数据依赖的方式计算删除模块后输出分布与学习条件数据分布之间的偏离程度，从而决定剪枝模块。此外，提出了零样本自适应剪枝框架，自动决定何时以及多少进行剪枝，以避免一次性剪枝的缺陷，避免模式崩溃，同时保持模型性能。
### Conclusion
在DiT和SiT模型上进行的大量实验表明，EntPruner在实现2.22倍的推理加速的同时，能够维持竞争力的生成质量。
## 428. `cs.CV` - CLRecogEye：基于课程学习利用卷积特征进行动态虹膜识别 [PDF](https://arxiv.org/pdf/2511.21097), [HTML](https://arxiv.org/abs/2511.21097)
### Authors
Geetanjali Sharma,Gaurav Jaswal,Aditya Nigam,Raghavendra Ramachandra
### Background
虹膜认证算法在识别性能方面取得了显著成果，使其在边境控制、公民身份验证及犯罪侦查和商业系统等领域具有广泛应用前景。然而，虹膜认证仍面临旋转、尺度变化、镜面反射和模糊等问题的挑战。此外，现有的大多数方法依赖于简单的点对点比较，通常使用余弦距离或L2距离，未能有效利用虹膜模式的空间-空间-时间结构。
### Innovation
本文提出了一种新颖且通用的匹配管道，该方法通过学习虹膜特征的空间-空间-时间表示来解决上述限制。首先，该方法将每一幅虹膜图像沿一个维度进行拆分，生成一系列子图像作为3D-CNN的输入，使网络能够捕获空间和空间-时间特征。为了进一步增强对空间-空间-时间特征动态的建模，本文以课程学习方式训练该模型，使网络能够直接嵌入时间依赖性到特征空间，从而在深度度量域中提高辨别性。整个框架以三元组和ArcFace损失进行端到端训练，在困难如旋转、尺度、反射和模糊等条件下，仍能产生高度区分的嵌入。
### Conclusion
本文设计了一种鲁棒且通用的解决方案，利用课程学习和3D-CNN学习虹膜特征的空间-空间-时间表示，从而提升了动态虹膜识别的性能。该方法通过以课程学习方式训练模型和端到端的三元组及ArcFace损失训练，有效应对了虹膜旋转、尺度、反射和模糊等问题。
## 429. `cs.CV` - FlowerDance: MeanFlow for Efficient and Refined 3D Dance Generation [PDF](https://arxiv.org/pdf/2511.21029), [HTML](https://arxiv.org/abs/2511.21029)
### Authors
Kaixing Yang,Xulong Tang,Ziqiao Peng,Xiangyue Zhang,Puwei Wang,Jun He,Hongyan Liu
### Background
音乐到舞蹈生成旨在将听觉信号转化为富有表现力的人类动作，广泛应用于虚拟现实、编舞和数字娱乐领域。尽管已有进展，但现有方法生成效率有限，无法提供高保真3D渲染，进而限制了实际应用中3D角色的表现力。
### Innovation
FlowerDance结合了MeanFlow和物理一致性约束，仅通过少量采样步骤就能生成高质量的动作；采用了简单的高效模型架构，利用BiMamba骨干和通道级跨模态融合，以非自回归方式生成舞蹈；支持动作编辑，允许用户交互式细化舞蹈序列；实验表明，FlowerDance在动作质量和生成效率上均达到最佳。
### Conclusion
FlowerDance在AIST++和FineDance数据集上实现了动作质量和生成效率的最佳结果，代码将在接受后公开。
## 430. `cs.CV` - CtrlVDiff：通过统一多模态视频扩散实现可控视频生成 [PDF](https://arxiv.org/pdf/2511.21129), [HTML](https://arxiv.org/abs/2511.21129)
### Authors
Dianbing Xi,Jiepeng Wang,Yuanzhi Liang,Xi Qiu,Jialun Liu,Hao Pan,Yuchi Huo,Rui Wang,Haibin Huang,Chi Zhang,Xuelong Li
### Background
本文解决视频理解与可控视频生成的双重挑战。研究发现，仅依赖几何线索（如深度、边缘）不足以满足研究需求，因为这些线索仅能确定布局，而无法限定物体外观、材质和光照等。这限制了诸如重新光源设置或材质替换等物理上合理的编辑，并可能导致时间上的漂移。因此，通过增加基于图形的模态（如内在特性与语义信息），可以提供互补的约束条件，这些条件不仅能改善理解，还能在生成过程中提供精确的控制。
### Innovation
本文提出的架构和数据策略创新性地解决了模型中引入多种异构线索所面临的核心问题。具体而言，引入CtrlVDiff模型，结合Hybrid Modality Control Strategy（混合模态控制策略）训练，将来自深度、法线、分割、边缘以及基于图形的内在特征等不同模态的特征进行路由与融合，并重新渲染具备强烈时间连续性的视频片段。此外，成功构建了一个混合的现实与合成的多模态数据集MMVideo，该数据集可跨模态和描述对齐，从而能够实现高质量的无障碍编辑。
### Conclusion
通过CtrlVDiff，研究在理解和生成基准测试中实现了卓越的可控性和保真度，支持多层编辑（如重新光源设置、材质调整和对象插入），并且即使在某些模态不可用时依然保持鲁棒性，超越了现有最先进的基线方法。
## 431. `cs.CV` - 基于熵引导优先分阶段学习的人类视频生成高效训练 [PDF](https://arxiv.org/pdf/2511.21136), [HTML](https://arxiv.org/abs/2511.21136)
### Authors
Changlin Li,Jiawei Zhang,Shuhao Liu,Sihao Lin,Zeyi Shi,Zhihui Li,Xiaojun Chang
### Background
随着扩散模型的发展，人类视频生成取得了快速进步，但高分辨率多帧数据训练时的高计算成本和大量内存使用带来了显著挑战。
### Innovation
提出了一种名为熵引导优先分阶段学习（Ent-Prog）的高效训练框架，针对扩散模型在人类视频生成中的应用。该框架通过引入条件熵膨胀（CEI）评估模型组件的重要性，提出自适应分阶段调度策略以适应性增加训练过程中的计算复杂度。
### Conclusion
实验表明，Ent-Prog 在三个数据集上均有效，实现了模型性能不减下的训练速度提升至2.2倍、GPU内存减少至2.4倍的效果。
## 432. `cs.CV` - LungNoduleAgent：一种用于肺癌结节精确诊断的协作多代理系统 [PDF](https://arxiv.org/pdf/2511.21042), [HTML](https://arxiv.org/abs/2511.21042)
### Authors
Cheng Yang,Hui Jin,Xinlei Yu,Zhipeng Wang,Yaoqun Liu,Fenglei Fan,Dajiang Lei,Gangyong Jia,Changmiao Wang,Ruiquan Ge
### Background
肺癌诊断通常包括医生通过计算机断层扫描(CT)扫描识别肺结节，并基于结节形态特征和医学专业知识生成诊断报告。尽管已经在利用多模态大型语言模型分析肺CT扫描方面取得了进展，但在准确描述结节形态和整合医学专业知识方面仍然存在挑战。这些限制影响了这些模型在临床设置中的可靠性和有效性。尽管协作多代理系统被认为是有希望的策略，但其在病理学中的潜力尚未得到充分探索。
### Innovation
我们提出了LungNoduleAgent，一种专门针对肺CT扫描分析的创新协作多代理系统。LungNoduleAgent将诊断过程简化为三个主要模块：结节检测模块（结节检测器）、放射科医生模块（利用局部图像描述技术生成综合CT报告）和医生代理系统模块（利用病理知识库和多代理系统框架进行恶性肿瘤推理）。通过该系统的应用，研究结果表明LungNoduleAgent优于主流的视觉语言模型、代理系统和高级专家模型。这些结果突显了区域语义对齐和多代理协作在结节诊断中的重要性。
### Conclusion
LungNoduleAgent是一个重要的初步工具，有助于支持肺癌结节的临床分析。
## 433. `cs.CV` - DeepRFTv2：基于核级学习的图像去模糊 [PDF](https://arxiv.org/pdf/2511.21132), [HTML](https://arxiv.org/abs/2511.21132)
### Authors
Xintian Mao,Haofei Song,Yin-Nian Liu,Qingli Li,Yan Wang
### Background
众所周知，如果网络需要学习去模糊技术，必须理解模糊过程。模糊是通过将锐利图像与模糊核进行卷积而自然产生的。因此，允许网络在核级学习模糊过程可以显著提高图像去模糊的效果。然而，当前的深度网络仍然停留在像素级的学习阶段，要么进行端到端的像素级恢复，要么阶段式的伪核级恢复，不能让去模糊模型真正理解模糊的本质。
### Innovation
作者提出了Fourier Kernel Estimator（FKE），使网络能够通过傅立叶空间中的激活操作将空间域中的卷积问题转换为傅立叶空间中的乘法问题。FKE可以与去模糊模型联合优化，从而以较低的复杂度和无额外监督的方式学习核级模糊过程。此外，作者将核的卷积对象从“图像”变为“特征”，这些丰富的语义和结构性信息更适合学习模糊过程。为了进一步提高特征提取的效率，设计了一个解耦的多尺度架构，该架构包含多个带有可逆策略的层次子单元，从而可以在低训练内存的情况下实现更好的多尺度编码和解码。
### Conclusion
大量的实验表明，本方法在运动去模糊方面达到了最先进的结果，并展示了在处理其他核相关问题方面的潜力。分析还表明，作者的核估计器能够学习具有物理意义的核。该代码将在指定的网址处提供。
## 434. `cs.CV` - TEAR: Temporal-aware Automated Red-teaming for Text-to-Video Models [PDF](https://arxiv.org/pdf/2511.21145), [HTML](https://arxiv.org/abs/2511.21145)
### Authors
Jiaming He,Guanyu Hou,Hongwei Li,Zhicong Huang,Kangjie Chen,Yi Yu,Wenbo Jiang,Guowen Xu,Tianwei Zhang
### Background
Text-to-Video (T2V)模型能够生成高质量、时序一致的动态视频内容，但多样化生成同时也引入了严重的安全挑战。现有的安全评估方法主要关注静态图像和文本生成，无法捕捉视频生成中的复杂时序动态。
### Innovation
提出了一个基于时序感知的自动化红队框架TEAR，该框架旨在揭示与T2V模型动态时序顺序相关的安全风险。TEAR采用了基于两阶段优化的时序感知测试生成器，并结合一个精炼模型以循环提升提示的隐蔽性和对抗有效性。
### Conclusion
通过广泛的实验评估，TEAR在开源和商用T2V系统中的攻击成功率超过80%，显著提高了先前最好结果的57%。
## 435. `cs.CV` - 场景作为符号：多尺度正态分布变换标记器在通用3D视觉语言理解中的应用 [PDF](https://arxiv.org/pdf/2511.21191), [HTML](https://arxiv.org/abs/2511.21191)
### Authors
Yutao Tang,Cheng Zhao,Gaurav Mittal,Rohith Kukkala,Rama Chellappa,Cheng Peng,Mei Chen
### Background
近年来，3D 视觉-语言模型（VLMs）的研究发现，这些模型在3D 场景理解与推理方面有很强的潜力。然而，如何将3D 场景有效地标记为整体场景符号，并在多种3D 场景理解任务中利用这些符号，仍然极具挑战性。
### Innovation
本文提出了一种名为NDTokenizer3D的通用3D VLM，它具有一整套的3D 场景理解任务，并自然支持与人类交互，从而将语言层面的推理与3D 空间理解相结合。该方法的核心是基于多尺度正态分布变换（NDT）表示构建的新的三阶段场景标记流水线，以及多尺度NDT解码器（MSDec）。NDTokenizer3D首先从原始高分辨率点云构建多尺度NDT表示，保留了全局上下文和细微几何细节。随后，MSDec逐步融合跨尺度NDT特征，产生可由LLM终端消费的整体场景符号。MSDec还被重新用作人类交互提示（点、框、掩码）和分割掩码解码的一般接口，将多种3D 场景理解任务统一在单一架构中。
### Conclusion
NDTokenizer3D 采用了紧凑且统一的设计，提供了一种细粒度的通用3D VLM，实现了3D 参考分割、3D 视觉问答和3D 密集描述等任务上的显著改进。
## 436. `cs.CV` - 扩展雷达场景理解的基础模型 [PDF](https://arxiv.org/pdf/2511.21105), [HTML](https://arxiv.org/abs/2511.21105)
### Authors
Pushkal Mishra,Kshitiz Bansal,Dinesh Bharadia
### Background
雷达传感器在恶劣天气、照明条件和远距离条件下的感知表现可靠。虽然基于基础模型的方法在视觉理解和语言理解方面取得了重大进展，但它们与雷达传感的结合仍然是很大程度上未被探索的领域。现有的雷达方法分散且是任务特定的，每个下游任务都有不同的架构和训练目标，阻碍了任务之间的迁移。
### Innovation
本文引入了RadarFM，这是一种通过结构化空间语言监督学习统一场景级表示的雷达基础模型。两个关键贡献是：(1)一种结构化描述框架，编码车辆分布的雷达坐标，(2)一种哈希感知对比学习目标，量化连续场景相似性而非二元匹配，从而实现精细的空间推理。
### Conclusion
我们利用CARLA模拟器生成了大规模、注释良好的雷达数据集，包含多种驾驶场景，并提出了一种定位感知的评估指标，超越了传统检测措施，评估空间准确性。
## 437. `cs.CV` - 基于变形感知的时间生成在阿尔茨海默病早期预测中的应用 [PDF](https://arxiv.org/pdf/2511.21114), [HTML](https://arxiv.org/abs/2511.21114)
### Authors
Xin Honga,Jie Lin,Minghui Wang
### Background
阿尔茨海默病是一种进行性脑退化疾病，早期预测有助于减缓疾病进展。当前预测方法主要通过手动特征提取来分析脑图像中的形态学变化。但这类方法依赖于人工操作，效率低下且准确度有限，特别是在脑MRI图像序列中常见的缺失数据问题上。
### Innovation
本文提出了一种名为Deformation-Aware Temporal Generative Network (DATGN)的新方法，用于自动化学习疾病进展中脑图像的形态学变化，以便实现早期预测。DATGN首先插补不完整的序列数据，然后通过双向的时间变形感知模块指导网络生成遵循疾病进展的未来MRI图像。实验结果在PSNR和MMSE图像质量指标上具有竞争力，并通过将合成数据与多种分类方法结合，显著提高了AD与其他类别的分类准确率。
### Conclusion
DATGN生成的图像能够反映阿尔茨海默病中的脑萎缩趋势，从而实现早期疾病预测。这种方法的引入为未来的脑影像学研究提供了新的工具和技术支持。
## 438. `cs.CV` - 基于非均匀时间序列的正常逆伽马分布时参数估计的新图像生成方法在阿尔茨海默病长期预测中的应用 [PDF](https://arxiv.org/pdf/2511.21057), [HTML](https://arxiv.org/abs/2511.21057)
### Authors
Xin Hong,Xinze Sun,Yinhao Li,Yen-Wei Chen
### Background
图像生成能够为医生提供基于影像的诊断基础，在阿尔茨海默病（AD）的预测中具有重要作用。然而，现有的长期AD预测依赖图像生成技术时，常常难以在不规则时间间隔的序列数据中保持疾病相关的特征。时间相关的分布特征能够反映图像不均匀分布时疾病相关特征的变化。因此，需要提出一种模型，可以估算正常倒伽玛分布（T-NIG）内的时间参数，以辅助生成长期的图像。
### Innovation
在此研究中，提出了一种T-NIG模型，利用脑部图像从两个不同时间点创建中间脑部图像，预测未来图像并预测疾病发展。T-NIG模型通过识别坐标邻域内的特征，将时间参数纳入正常逆伽马分布，以理解具有不均匀时间间隔的脑部成像序列中特征的变化。此外，T-NIG模型还利用不确定性估计来减少模型中的表征性和随机性不确定性。
### Conclusion
实验结果显示，T-NIG模型在短期和长期预测任务中都表现出最好的性能，尤其在不规则时间分布的数据集上，能够有效地预测疾病进展并保持疾病相关的特征。
## 439. `cs.CV` - BotaCLIP：地球观测数据植物学意识对比学习 [PDF](https://arxiv.org/pdf/2511.21194), [HTML](https://arxiv.org/abs/2511.21194)
### Authors
Selene Cerna,Sara Si-Moussi,Wilfried Thuiller,Hadrien Hendrikx,Vincent Miele
### Background
基础模型已经展示了在图像、文本和音频等多种模态领域中学习丰富且可迁移表示的能力。在现代机器学习流程中，这些表示通常会取代原始数据成为下游任务的主要输入。然而，如何在无需从头开始重新训练或不产生显著计算成本的情况下，使预训练的基础模型适应注入特定领域的专业知识，仍是一个挑战。
### Innovation
本文介绍了一种轻量级的多模态对比学习框架BotaCLIP，通过对比学习方式将预训练的地球观测基础模型（DOFA）与高分辨率航空影像对齐植物谱系，利用正则化策略避免灾难性遗忘。这种方法使得到的嵌入成为下游预测器的可迁移表示。实验结果表明，BotaCLIP在生物多样性建模的三个生态任务中表现优于DOFA和监督基线。
### Conclusion
本文的工作展示了如何使得基础模型具有领域意识的适应性，可以通过注入专家知识来适应数据稀缺的场景，从而实现高效的学习表示。
## 440. `cs.CV` - 你可以信任你的聚类模型：一种无参数自我增强插件用于深度聚类 [PDF](https://arxiv.org/pdf/2511.21193), [HTML](https://arxiv.org/abs/2511.21193)
### Authors
Hanyang Li,Yuheng Jia,Hui Liu,Junhui Hou
### Background
近年来，深度聚类模型在聚类性能方面取得了显著成果。然而，现有方法的一个共同问题是在全局和局部特征结构间的差异。局部结构通常在类内样本之间表现出强烈的连贯性和紧凑性，而全局特征往往则表现出交缠的边界和分离不良的聚类。
### Innovation
我们提出了DCBoost，这是一种参数无依赖的插件，旨在增强当前深度聚类模型的全局特征结构。通过利用可靠的局部结构线索，该方法旨在有效提升聚类性能。具体来说，我们首先通过自适应的k-最近邻一致过滤来识别高置信度样本，从中选择具有高标签可靠性的样本作为自我监督的可信锚点。然后，用这些样本来计算鉴别性损失，这既促进了类内紧凑性，也促进了类间可分性，以引导网络优化。
### Conclusion
我们在多个基准数据集上进行了广泛的实验，证明了我们的DCBoost显著提升了各种现有深度聚类模型的聚类性能。值得注意的是，我们的方法不仅将当前最先进的基线（如ProPos）的性能提升了超过3%，而且还提升了轮廓系数超过7倍。代码可在https://github.com/username/DCBoost获取。
## 441. `cs.CV` - 针对细粒度视频动作识别的有效动作-区域跟踪框架 [PDF](https://arxiv.org/pdf/2511.21202), [HTML](https://arxiv.org/abs/2511.21202)
### Authors
Baoli Sun,Yihan Wang,Xinzhu Ma,Zhihui Wang,Kun Lu,Zhiyong Wang
### Background
当前的动作识别方法能够捕捉粗粒度的动作模式，但难以识别时间演变过程中的细微局部细节，导致难以区分相似的动作。
### Innovation
提出了Action-Region Tracking (ART)框架，该框架采用查询-响应机制发现并跟踪区分性局部细节的动力学，通过区域特定语义激活模块针对每个视频帧提取最相关的区域响应，利用跨时空维度的响应构建动作轨迹片段。文本约束查询使用视觉语言模型中的语言分支提取的动作标签文本描述形成细微语义表示，通过多级轨迹对比约束在时空维度优化区域响应，同时设计任务特定的微调机制优化语义表示以满足任务偏好。
### Conclusion
全面的实验表明，该方法在广泛使用的动作识别基准上优于之前的最先进的基线方法。
## 442. `cs.CV` - AnchorOPT: 向优化动态锚点以实现自适应提示学习迈进 [PDF](https://arxiv.org/pdf/2511.21188), [HTML](https://arxiv.org/abs/2511.21188)
### Authors
Zheng Li,Yibing Song,Xin Zhang,Lei Luo,Xiang Li,Jian Yang
### Background
现有的基于CLIP模型的提示学习方法使用文本标记作为锚点来引导可学习的软标记，这种引导提高了CLIP的泛化能力。然而，这些锚点是静态的，在值和位置上缺乏跨任务和阶段的灵活性。
### Innovation
为了解决这一限制，作者提出了AnchorOPT，一种基于动态锚点的提示学习框架。具体来说，AnchorOPT在两个关键维度上引入了动态性：(i) 锚值不是手工设计的明确文本标记（如“形状”、“颜色”），而是从特定任务的数据中动态学习；(ii) 锚和软标记之间的位置关系不再是固定的，而是通过条件于训练阶段和任务上下文的可学习位置矩阵来适应性优化。
### Conclusion
大量的实验表明，仅使用简单的可学习锚点和位置矩阵就能达到或超过一些包含额外可学习模块或正则化技术的方法的性能。作为插即用模块，AnchorOPT可以无缝集成到现有的框架中，在各种数据集上实现了一致的性能增益。代码已在以下网址公开：this https URL。
## 443. `cs.CV` - 从扩散到一步生成：基于流的模型的比较研究及其在图像修复中的应用 [PDF](https://arxiv.org/pdf/2511.21215), [HTML](https://arxiv.org/abs/2511.21215)
### Authors
Umang Agarwal,Rudraksh Sangore,Sumit Laddha
### Background
本文进行了一项全面的比较研究，探讨了三种生成建模范式：去噪扩散概率模型（DDPM）、条件流匹模型（CFM）和MeanFlow。虽然DDPM和CFM需要迭代采样，但MeanFlow通过建模随时间变化的平均速度，实现了直接一步生成。
### Innovation
作者使用统一的小型UNet架构（<1.5M参数）在CIFAR-10上实现了所有三种方法。通过比较，CFM在50步中的FID（24.15）显著优于DDPM（FID 402.98）。MeanFlow使用单步采样方法实现了FID 29.15，其推理时间减少了50倍。此外，作者将CFM扩展到了图像修复任务中，通过四种不同类型的掩膜（中心、随机bbox、不规则和半边）进行了掩膜引导采样的实现。
### Conclusion
作者还对修复模型进行了微调，结果表明在中心掩膜上的PSNR增加了73%，从4.95提高到8.57 dB；SSIM指标从0.289提高到0.418，增加了45%，这证明了修复训练的有效性。
## 444. `cs.CV` - 具有跨模态代理查询的视频对象分割 [PDF](https://arxiv.org/pdf/2511.21139), [HTML](https://arxiv.org/abs/2511.21139)
### Authors
Baoli Sun,Xinzhu Ma,Ning Wang,Zhihui Wang,Zhiyong Wang
### Background
参考视频对象分割（RVOS）是一个新兴的跨模态任务，旨在根据给定的文字表达生成目标对象的像素级地图。近年来，通过条件查询的方法来解决跨模态对齐问题，但它们在处理帧间依赖性和变异性方面存在局限，可能因帧间变化大而导致目标追踪不准确。此外，这些方法较晚整合文本约束，可能会导致视频特征关注未被指代的对象。
### Innovation
提出了一种名为ProxyFormer的新颖RVOS架构。引入了一组代理查询，以整合视觉和文本语义，并促进它们之间的语义流动。通过多阶段视频特征编码器不断更新和传播代理查询，ProxyFormer确保视频特征专注于所需的对象。这种动态演变也使得帧间依赖性的建立成为可能，从而提高对象追踪的准确性和连贯性。为减轻高计算成本，我们将跨模态交互分解为时间和空间维度。此外，设计了一种联合语义一致性（JSC）训练策略，以使代理查询和组合的视频-文本对之间的语义达成一致。
### Conclusion
在四个广泛使用的RVOS基准上的全面实验表明，我们的ProxyFormer方法优于最先进的方法。
## 445. `cs.CV` - 3-Tracer：音频伪造检测与定位的三级时间感知框架 [PDF](https://arxiv.org/pdf/2511.21237), [HTML](https://arxiv.org/abs/2511.21237)
### Authors
Shuhan Xia,Xuannan Liu,Xing Cui,Peipei Li
### Background
近期，部分音频伪造作为新的音频篡改形式出现，攻击者选择性地修改部分但具有语义关键性的帧，同时保持整体听觉真实感，这使此类伪造特别难以检测。现有的方法集中在独立检测每一帧是否被篡改，缺乏捕捉多时间层次上瞬态和持续异常的层次结构。
### Innovation
我们识别了与部分音频伪造检测相关的三个关键层级，并提出了T3-Tracer，这是首个联合分析音频在帧、段和音频层级上的框架，以全面检测伪造痕迹。T3-Tracer 包含两个互补的核心模块：帧-音频特征聚合模块（FA-FAM）和段层级多尺度差异感知模块（SMDAM）。FA-FAM 旨在检测每一帧的真伪，结合帧级和音频级时间信息来检测帧内伪造线索和全局语义不一致。我们引入 SMDAM 在段层级上检测伪造边界，采用双分支架构，在多时间尺度窗口中同时建模帧特征和帧间差异，有效识别伪造边界上出现的突然异常。
### Conclusion
在三个具有挑战性的数据集上进行的广泛实验表明，我们的方法达到了最先进的性能。
## 446. `cs.CV` - FIELDS: 基于直接监督的准确表情推理面部重建 [PDF](https://arxiv.org/pdf/2511.21245), [HTML](https://arxiv.org/abs/2511.21245)
### Authors
Chen Ling,Henglin Shi,Hedvig Kjellström
### Background
面部表情在人类交流中传达了大量的情感信息，但现有的3D面部重建方法常常因为依赖于2D监督和缺乏3D真实标记而错过了微妙的情感细节。
### Innovation
提出了FIELDS（面部重建与准确表情推理利用直接监督学习）来解决这个问题，通过扩展自我监督的2D图像一致性线索并引入直接的3D表情参数监督和辅助情绪识别分支。FIELDS 的编码器受到自发4D面部扫描的真实表情参数的引导，同时强度感知的情绪损失鼓励3D表情参数捕捉真实的情绪内容而不夸大。
### Conclusion
通过这种双重监督策略，FIELDS 填补了2D/3D领域差距，减少了表情强度偏差，产生了高保真度的3D重建结果，保留了微妙的情感线索。从单张图像出发，FIELDS 生成了富有情感的表情面部模型，提高了野外情感表达识别性能，同时保持真实性。
## 447. `cs.CV` - 当机器人听命于补丁：针对视觉-语言-动作模型的通用可转移补丁攻击 [PDF](https://arxiv.org/pdf/2511.21192), [HTML](https://arxiv.org/abs/2511.21192)
### Authors
Hui Lu,Yi Yu,Yiming Yang,Chenyu Yi,Qixin Zhang,Bingquan Shen,Alex C. Kot,Xudong Jiang
### Background
视觉-语言-动作（VLA）模型在对抗攻击下较为脆弱，尤其在缺少模型具体信息的黑盒设置中，现有的防护机制大多针对单一模型且效果不佳。因此，研究者们致力于探索通用且具有跨模型转移能力的对抗攻击方法。
### Innovation
本文提出了UPA-RFAS（通用补丁攻击通过稳健特征、注意力和语义），这是一种统一的框架，能够在共享特征空间中学习单一物理补丁，同时促进模型间的跨任务转移。UPA-RFAS 包含：1）使用 $boldsymbol{text{l}}_1$ 偏差先验和排斥 InfoNCE 损失来促进转移表示的特征空间目标；2）增强鲁棒性的两阶段最优化过程，其中内循环学习不可见样本扰动，外循环优化通用补丁；3）针对 VLA 特性的两种损失：补丁注意力主导权和补丁语义不匹配。这些方法共同实现了跨模型、任务和视角的有效转移。
### Conclusion
UPA-RFAS 在多种 VLA 模型、操作任务及实际执行环境中展示了跨任务和视角的有效转移能力，揭示了一种可实用的基于补丁的攻击方法，同时为未来防御研究奠定了坚实的基础。
## 448. `cs.CV` - LLaVA-UHD v3: 逐步视觉压缩在多模态大语言模型中高效全局分辨率编码 [PDF](https://arxiv.org/pdf/2511.21150), [HTML](https://arxiv.org/abs/2511.21150)
### Authors
Shichu Sun,Yichen Zhang,Haolin Song,Zonghao Guo,Chi Chen,Yidan Zhang,Yuan Yao,Zhiyuan Liu,Maosong Sun
### Background
多模态大语言模型（MLLMs）中，视觉编码后跟随标记凝缩已成为标准架构模式。许多近期的MLLMs现在更倾向于使用全局原生分辨率视觉编码，而不是切片法。为了研究这一趋势，我们在视觉语言理解上的行为和注意力模式上系统地比较了它们，结果显示，全局编码可以显著增强整体能力，但会产生更多的计算负担。
### Innovation
我们提出了LLaVA-UHD v3，一种基于我们提出的逐步视觉压缩（PVC）方法的MLLM，该方法能够无缝集成到标准视觉变换器（ViT）中，以实现高效原生分辨率编码。PVC方法包含两个关键模块：(i) 细化块嵌入，支持灵活的块尺寸缩放以进行细粒度视觉建模；(ii) 窗口标记压缩，逐层部署以逐步聚合局部标记表示。这两种模块的联合调节使得一个广泛预训练的ViT可以被重新配置为一个高效架构，同时保留其灵活性。
### Conclusion
通过广泛基准测试，重新配置的ViT（称为ViT-UHD）展示了与MoonViT竞争的性能，同时TTFT（第一个标记的生成时间）降低了2.4倍。在基于相同MLLM架构的基础上，LLaVA-UHD v3实现与Qwen2-VL竞争的性能，进一步降低了TTFT 1.9倍。所有代码和检查点将被发布，以支持未来关于高效MLLM的研究。
## 449. `cs.CV` - PathMamba: 一种用于卫星图像中拓扑一致道路分割的Mamba-Transformer混合模型 [PDF](https://arxiv.org/pdf/2511.21298), [HTML](https://arxiv.org/abs/2511.21298)
### Authors
Jules Decaestecker,Nicolas Vigne
### Background
在城市规划和灾害响应等应用中，从卫星图像中实现高精度和拓扑连续性的道路分割是一个关键目标。尽管最先进的方法依赖于视觉变换器，它们擅长捕捉全局上下文，但其计算复杂性使得它们难以在资源受限平台上高效部署。相比之下，新兴的状态空间模型如Mamba提供线性时间效率，且更适合建模长而连续的结构。这些架构具有互补的优势。
### Innovation
本文介绍了一种新颖的混合架构PathMamba，它将Mamba的顺序建模与Transformer的全局推理相结合。该设计通过战略性地使用Mamba块来跟踪道路网络的连续性，保持拓扑结构，同时集成Transformer块以利用全局上下文进行特征细化，从而避免纯粹基于注意力模型的扩展成本。实验结果表明，PathMamba在DeepGlobe道路提取和马萨诸塞州道路数据集上均取得了新的最先进水平。
### Conclusion
PathMamba在拓扑连续性方面显著改进，并且在计算上具有竞争力。
## 450. `cs.CV` - 基于高斯绘射的半密集图像匹配零样本潜力的解锁 [PDF](https://arxiv.org/pdf/2511.21265), [HTML](https://arxiv.org/abs/2511.21265)
### Authors
Juncheng Chen,Chao Xu,Yanjun Cao
### Background
学习驱动的图像匹配依赖于大规模、多样且几何精确的训练数据。虽然 3D 高斯绘射（3DGS）能够实现逼真的新视角合成，使其成为数据生成的理想工具，但其几何上的不准确性和深度渲染偏差阻碍了其稳健的对应标签能力。
### Innovation
我们提出了 MatchGS，首个针对 3DGS 进行系统性几何修正和利用的框架。MatchGS 包括两个方面：（1）一个几何忠实的数据生成流水线，能够细化 3DGS 的几何形状，生成高度精确的对应标签，从而在不牺牲渲染保真度的情况下合成大量多样视角；（2）一种 2D-3D 表征对齐策略，将 3DGS 显式的 3D 知识引导进入 2D 匹配器中，指导 2D 半密集匹配器学习不变于视角的 3D 表征。
### Conclusion
我们生成的地面真理对应能将现有的数据集的极束误差减少多达 40 倍，能够在极端视角变化下进行监督，并通过高斯属性提供自监督信号。利用我们生成的数据训练的顶级匹配器在公共基准上的零样本性能提升了高达 17.7%。我们的研究表明，经过适当的几何修正后，3DGS 可以作为具备可扩展性、高保真度和结构复杂性的数据源，为新一代稳健的零样本图像匹配器铺平了道路。
## 451. `cs.CV` - 不断增加，更好的：更高阶多模态对齐的对比融合 [PDF](https://arxiv.org/pdf/2511.21331), [HTML](https://arxiv.org/abs/2511.21331)
### Authors
Stefanos Koutoupis,Michaela Areti Zervou,Konstantinos Kontras,Maarten De Vos,Panagiotis Tsakalides,Grigorios Tsagatakis
### Background
多模态机器学习中跨多个模态学习联合表示仍然是一个核心挑战。现有方法主要在两两模态对齐中运作，尽管有部分方法试图捕捉多个模态间的高阶交互，但它们往往忽视了模态之间的两两关系，限制了它们在单模态任务中的效果。
### Innovation
提出了一种名为对比融合（ConFu）的新框架，它将单一模态和它们的融合组合都嵌入到统一的表示空间中，并通过增加融合模态的对比性目标来鼓励模态对与第三个模态的联合嵌入。这种框架能在不牺牲两两对应关系的情况下，捕捉到仅通过两两对齐无法恢复的高阶依赖关系。
### Conclusion
通过在合成数据和真实世界多模态基准测试上评估ConFu，发现该方法在检索和分类任务中具有竞争力，并支持单一对比框架内的统一一对一和一对二检索。
## 452. `cs.CV` - HTTM: 主观时间分段标记头式用于更快的VGGT [PDF](https://arxiv.org/pdf/2511.21317), [HTML](https://arxiv.org/abs/2511.21317)
### Authors
Weitian Wang,Lukas Meiner,Rai Shubham,Cecilia De La Parra,Akash Kumar
### Background
视觉几何引导下的变压器（VGGT）在3D场景重建中取得了重大突破，因为它首次能够直接在一次通过中联合推断所有关键3D属性（相机姿态、深度和密集几何）。然而，这一联合推断机制依赖于全局注意力层，这些层在所有视角之间进行所有到所有注意力计算，这对于大型场景的大规模输入导致了显著的延迟瓶颈。
### Innovation
本文提出了头级临时合并（HTTM），一种基于训练的3D标记合并方法，用于加速VGGT。现有合并技术将标记均匀合并到不同的注意力头中，导致层输出中具有相同的标记，限制了模型的表示能力。HTTM通过在多头层次上进行标记合并，保持了头级拼接后的特征标记的独特性。此外，这种方法允许HTTM利用在头级观察到的空间局部性和时间对应关系，以较低的合并成本实现更高比例的合并，优于现有方法。因此，HTTM在GPU基的推理中可实现高达7倍的加速，而几乎无性能损失。
### Conclusion
实验结果表明，HTTM在基于GPU的推理中可实现高达7倍的加速，几乎无性能损失。
## 453. `cs.CV` - CaliTex: 几何校准注意力以生成视角一致的3D纹理 [PDF](https://arxiv.org/pdf/2511.21309), [HTML](https://arxiv.org/abs/2511.21309)
### Authors
Chenyu Liu,Hongze Chen,Jingzhi Bao,Lingting Zhu,Runze Zhang,Weikai Chen,Zeyu Hu,Yingda Yin,Keyang Luo,Xin Wang
### Background
尽管基于扩散的模型取得了重大进展，当前的3D纹理生成系统仍然受到跨视角不一致的困扰——从一个视角看去似乎真实的纹理在其他视角中经常会失真。我们发现这个问题源自注意力的含混不清，未经结构化的全注意力机制在token和模态之间通用地应用，导致几何结构混乱和不稳定的表现结构耦合。
### Innovation
我们提出了CaliTex框架，这是一种几何校准注意力框架，显式地将注意力与3D结构对齐。它引入了两个模块：部分对齐注意力，它在语义匹配的部分之间施加空间对齐；条件导向注意力，它通过几何条件化的路径路由外观信息，以保持空间保真度。结合两阶段扩散变换器，CaliTex使几何一致性成为网络内的固有行为，而不是优化的副产品。
### Conclusion
实验上，CaliTex生成无缝且视角一致的纹理，并优于开源和商用基线。
## 454. `cs.CV` - 混合SIFT-SNN用于交通流量控制基础设施高效异常检测 [PDF](https://arxiv.org/pdf/2511.21337), [HTML](https://arxiv.org/abs/2511.21337)
### Authors
Munish Rathee(School of Engineering, Computer and Mathematical Science (of Auckland University of Technology) Auckland, New Zealand),Boris Bačić(School of Engineering, Computer and Mathematical Science (of Auckland University of Technology) Institute of Biomedical Technologies (IBTec) Auckland, New Zealand),Maryam Doborjeh(Knowledge Engineering and Discovery Research Institute (KEDRI) (of Auckland University of Technology) Auckland, New Zealand)
### Background
鉴于现有运输基础设施需要实时检测结构异常的需求，特别是需要在各种天气和光照条件下进行精确分类的情况，传统的深度学习方法（例如基于卷积神经网络的CNN方法）虽然在分类准确率上表现良好，但在低延迟和低功耗边缘部署方面存在不足。传统方法难以实现实时、低功耗部署，并且在处理复杂光照和环境条件时解析性不足。
### Innovation
本文提出了一种低延迟的类神经元信号处理管道SIFT-SNN框架，通过集成尺度不变特征变换（SIFT）来进行空间特征编码，加入一种受时延驱动的尖峰转换层和漏电积分和发放（LIF）类神经元网络进行分类。该系统在奥克兰海港大桥数据集上达到了92.3%的分类准确率（±0.8%），每帧推理时间为9.5毫秒，实现实时、低功率边缘部署。该方法不仅保留了空间特征映射，还提高了可解释性，支持透明决策，并能高效运行在嵌入式硬件上。
### Conclusion
本文验证了SIFT-SNN框架在消费者级别的系统上有效，并将其定位为在交通事故控制基础设施中的结构安全性监控的一般性案例研究。该框架在实现实时检测和低功耗部署方面具有明显优势，而且虽然合成数据增强提高了系统的鲁棒性，但在未见现场条件下的一般化需要进一步验证。
## 455. `cs.CV` - Endo-G$^{2}$T: 几何导向且具有时间意识的嵌入式4D高斯散刺图方法用于内窥镜场景 [PDF](https://arxiv.org/pdf/2511.21367), [HTML](https://arxiv.org/abs/2511.21367)
### Authors
Yangle Liu,Fengze Li,Kan Liu,Jieming Ma
### Background
内窥镜视图受到视角依赖的影响，如镜面反射、湿反射和遮挡。纯光度监督导致几何偏差并触发早期几何漂移，错误的形状在稠密化过程中被强化且难以修正。因此，需要一种方法，在保持动态内窥镜场景的时空一致性的同时，尽可能早地锚定几何形状，同时保持效率。
### Innovation
提出了一种基于几何导向且具有时间意识的训练方案Endo-G$^{2}$T，用于时间嵌入的4D高斯散刺图。首先，通过尺度不变的深度和深度梯度损失将置信门控单目深度转变为监督，采用预热至上限的计划逐步注入先验知识，避免早期过拟合；其次，旋转参数化表示XYZT中的动态，生成平滑的几何形状和清晰的透明边界；最后，通过关键帧约束流改进效率和长效稳定性，关键帧集中优化以在最大流点预算下实现，非关键帧则进行轻量级更新。
### Conclusion
在EndoNeRF和StereoMIS-P1数据集上，Endo-G$^{2}$T方法在单目重建基线上达到了最先进的效果。
## 456. `cs.CV` - 基于边界框思考：通过强化学习微调提升时空视频定位 [PDF](https://arxiv.org/pdf/2511.21375), [HTML](https://arxiv.org/abs/2511.21375)
### Authors
Xin Gu,Haoji Zhang,Qihang Fan,Jingxuan Niu,Zhipeng Zhang,Libo Zhang,Guang Chen,Fan Chen,Longyin Wen,Sijie Zhu
### Background
时空视频定位(STVG)需要将目标物体从自然语言描述中在时空上定位在未剪辑的视频中。尽管多模态大型语言模型(MLLMs)具有很强的语言理解能力，但由于训练目标不匹配和标准视觉编码器中细粒度区域-词对齐能力较弱，其在STVG任务上的表现不佳。
### Innovation
我们提出了STVG-o1框架，这是一个不需要架构修改就能使现成的大型语言模型实现最先进的时空视频定位性能的方案。我们方法中引入了边界框链式思考机制，它在生成最终预测之前会明确地推理时空位置。此外，我们设计了一个多维度增强奖励函数，包括格式、一致性、时间、空间和思考奖励，通过强化学习微调提供了几何感知监督。
### Conclusion
在HCSTVG-v1/v2和VidSTG数据集上，STVG-o1达到了新的最先进的结果，在HCSTVG上超越了最佳特定任务方法7.3%的m_tIoU，与专门模型在VidSTG上表现一致，并且大幅超越所有现有的基于MLLM的方法。同时，它展示了强大的开放词汇泛化跨数据集，证明了大型语言模型作为精确时空定位的强大候选骨干网络的有效性。我们的代码和模型将发布。
## 457. `cs.CV` - Monet: 超越图像与语言的潜空间视觉推理 [PDF](https://arxiv.org/pdf/2511.21395), [HTML](https://arxiv.org/abs/2511.21395)
### Authors
Qixun Wang,Yang Shi,Yifei Wang,Yuanxing Zhang,Pengfei Wan,Kun Gai,Xianghua Ying,Yisen Wang
### Background
“借助图像思考”的范式已经显示出促进视觉推理的有效性，超越了仅依赖文本的思维链，通过在中间推理步骤中注入视觉证据。然而，现有的方法在灵活性方面远不及人类的抽象视觉思维，因为它们的基本灵活性受到了外部工具的限制。
### Innovation
本文介绍了一种名为Monet的训练框架，使多模态大型语言模型（MLLMs）能够在潜视觉空间中直接进行推理，通过生成连续嵌入来充当中间视觉思想。此外，还提出了一种强化学习方法VLPO（视觉潜空间策略优化），以将潜嵌入明确纳入策略梯度更新中。构建了Monet-SFT-125K高质量的文本-图像交替CoT数据集，包括125,000个现实世界、图表、OCR和几何CoTs。通过三阶段蒸馏基监督微调（SFT）流水线解决训练MLLMs进行潜视觉推理的两个核心挑战：潜视觉对齐的高计算成本和对潜嵌入监督的不足。
### Conclusion
模型Monet-7B在现实世界的感知和推理基准测试中表现出一致的改进，并在具有挑战性的抽象视觉推理任务中展现出强大的泛化能力。我们也对每个训练组件的作用进行了实证分析，并讨论了早期不成功的尝试，提供了未来视觉潜空间推理发展的见解。模型、数据和代码可在[该链接]获取。
## 458. `cs.CV` - 分步进步：自回归图像生成的测试时缩放 [PDF](https://arxiv.org/pdf/2511.21185), [HTML](https://arxiv.org/abs/2511.21185)
### Authors
Joonhyung Park,Hyeongwon Jang,Joowon Kim,Eunho Yang
### Background
最近的视觉自回归(AR)模型在文本到图像生成方面展现出了令人振奋的能力，其工作方式类似于大规模语言模型。而测试时计算的扩展性已显示出极大的成功，为复杂自然语言任务提供了增强的推理输出，但对于视觉AR模型的适应，这一策略仍处于未探索状态，存在独特挑战。简单应用测试时的扩展策略例如'Best-of-N'可能并不理想：它们会对错误的生成轨迹进行完整长度的计算，而位图扫描解码方案缺乏整个画布的地图，导致缩放效益有限，仅能生成少量与提示对齐的候选方案。
### Innovation
引入了一个名为GridAR的测试时缩放框架，旨在从视觉AR模型中获得最佳结果。GridAR采用网格划分渐进生成方案，在画布上为同一位置生成多个部分候选方案，早期剪除不可行方案，并将可行方案作为锚点引导后续解码。同时提出了一种基于布局的提示重述策略，通过检查部分视角来推断可行布局以满足提示要求，然后指引后续图像生成减少蓝图缺陷。
### Conclusion
GridAR在有限的测试时缩放下实现了更高质量的结果：当N=4时，即使在T2I-CompBench++上表现比'Best-of-N'（N=8）高出14.4%，还能节省25.6%的成本。此外，该方法还能用于自回归图像编辑，在PIE-Bench上相比更大N值的基准更具有语义保留性并取得了13.9%的提升。
## 459. `cs.CV` - 测试时计算量下推理视觉语言模型是否反向缩放？一种以干扰信息为中心的经验分析 [PDF](https://arxiv.org/pdf/2511.21397), [HTML](https://arxiv.org/abs/2511.21397)
### Authors
Jiyun Bae,Hyunjong Ok,Sangwoo Mo,Jaeho Lee
### Background
先前关于语言模型的研究表明，文本干扰导致推理时间较长但效果不佳。本文探讨这种现象是否在多模态环境中也同样存在。为此，作者创建了一个名为Idis（包含干扰信息的视觉问答数据集），通过系统地在语义、数值和空间维度上变化干扰信息，来研究视觉干扰信息如何影响模型的推理和准确性。
### Innovation
引入了Idis数据集，这是一种针对视觉干扰信息进行系统研究的新方法，能够区分视觉干扰与文本干扰的影响。通过追踪推理痕迹中的属性计数，揭示了视觉干扰与推理时间和准确性的关系，并将这些趋势扩展到现有视觉偏差基准Waterbirds，提出了一种简单的提示策略来减轻推理模型因偏见驱动的预测。
### Conclusion
视觉干扰与文本干扰在影响模型推理时表现出不同特性，尽管存在反向缩放现象，但添加视觉干扰会降低准确性而不增加推理时间。通过追踪推理痕迹中的属性计数，可以发现干扰、推理时间和准确性之间的复杂交互关系。这种趋势不仅适用于数据集Idis，还扩展到了Waterbirds等视觉偏差基准，提出了一个简单的提示策略来减轻因偏见驱动的推理模型预测问题。
## 460. `cs.CV` - LaGen: 向往自回归LiDAR场景生成 [PDF](https://arxiv.org/pdf/2511.21256), [HTML](https://arxiv.org/abs/2511.21256)
### Authors
Sizhuo Zhou,Xiaosong Jia,Fanrui Zhang,Junjie Li,Juyong Zhang,Yukang Feng,Jianwen Sun,Songbur Wong,Junqi You,Junchi Yan
### Background
生成对抗世界模型在自主驾驶(AD)中成为了一个热门话题。尽管图像模态已经得到了广泛研究，但当前研究主要集中在对LiDAR数据的生成方法上。现有方法只支持单帧生成，而现有预测方法需要多帧历史输入，且只能一次性确定性地预测多帧，缺乏交互性。这两个范式都无法支持长时程交互生成。
### Innovation
提出了LaGen框架，这是第一个能在单帧LiDAR输入的基础上进行长时程逐帧自回归生成高保真4D场景点云的框架。它引入了一个场景解耦估计模块和噪音调制模块，增强了模型在对象级内容上的交互生成能力，以及在长时间生成过程中降低了错误累积。
### Conclusion
实验结果全面展示了LaGen在LiDAR场景生成和预测方面的优越性，特别是在后期帧的表现上，相较于最先进的生成和预测模型有明显优势。
## 461. `cs.CV` - DiverseVAR: 平衡下一尺度视觉自回归模型的多样性和质量 [PDF](https://arxiv.org/pdf/2511.21415), [HTML](https://arxiv.org/abs/2511.21415)
### Authors
Mingue Park,Prin Phunyaphibarn,Phillip Y. Lee,Minhyuk Sung
### Background
视觉自回归模型（VAR）近年来因其在图像生成任务中的优异表现而成为与扩散和流动模型竞争的有力对手。然而，它们在多样性方面存在严重的局限性，往往会对简单的提示生成几乎完全相同的图像。这一问题长期以来被关注于图像质量改善的问题所掩盖。我们提出DiverseVAR框架，旨在在不重新训练、微调或增加大量计算成本的情况下，增强测试时的文本条件视觉自回归模型的多样性。
### Innovation
DiverseVAR框架通过在文本嵌入中注入噪声来提高多样性，这引入了多样性和图像质量之间的权衡。为了保持图像质量，DiverseVAR进一步引入了一种新颖的隐空间精炼技术——尺度旅行，并利用多尺度自编码器提取粗粒度的令牌以支持中间阶段的生成。实验证明，结合文本嵌入噪声注入和尺度旅行方法能显著提高多样性，并将图像质量的退化降到最低，从而在多样性和质量权衡上达到新的帕累托前沿。
### Conclusion
通过DiverseVAR框架，我们在不增加额外训练或显著计算负担的情况下解决了VAR模型在多样性方面的局限性。通过文本嵌入噪声注入和尺度旅行精炼技术的结合，显著提升了图像生成的多样性，同时最小化了图像质量的下降，从而达成了多样性和质量之间的最佳平衡。
## 462. `cs.CV` - AVFakeBench：用于AV-LMM的综合音频视频伪造检测基准 [PDF](https://arxiv.org/pdf/2511.21251), [HTML](https://arxiv.org/abs/2511.21251)
### Authors
Shuhan Xia,Peipei Li,Xuannan Liu,Dongsen Zhang,Xinyu Guo,Zekun Li
### Background
现有音频视频（AV）伪造的威胁正在从基于人类的深度假信息（Deepfakes）演变到包括更多样化的在复杂自然场景中的伪造。现有的基准仍然局限于深度假信息伪造和单一粒度的注释，未能全面捕捉现实世界伪造场景的多样性和复杂性。
### Innovation
提出了AVFakeBench，这是一个全新的音频视频伪造检测基准，涵盖了从人类主体到一般主体的丰富伪造语义。该基准包含12000个精心策划的音频视频问题，覆盖了七种伪造类型和四级注释。提出了一种多阶段混合伪造框架，将专有模型用于任务规划与领域专家生成模型用于精确操控相结合，确保高质量和多样化的伪造。构建了包含二元判断、伪造类型分类、伪造细节选择和解释性推理的多任务评估框架。
### Conclusion
对11个音频视频大型语言模型（AV-LMMs）和两种主流检测方法在AVFakeBench上的评估表明，AV-LMMs具有作为新兴伪造检测器的潜力，但在细粒度感知和推理方面存在明显弱点。
## 463. `cs.CV` - SurgMLLMBench：用于手术场景理解的大规模多模态语言模型基准数据集 [PDF](https://arxiv.org/pdf/2511.21339), [HTML](https://arxiv.org/abs/2511.21339)
### Authors
Tae-Min Choi,Tae Kyeong Jeong,Garam Kim,Jaemin Lee,Yeongyoon Koh,In Cheul Choi,Jae-Ho Chung,Jong Woong Park,Juyoun Park
### Background
近年来，多模态大型语言模型（LLMs）在医学和手术应用方面显示出巨大潜力。然而，现有的手术数据集主要采用视觉问答（VQA）格式，并且具有异质分类体系，缺乏对像素级分割的支持，这限制了持续评估和应用的一致性。
### Innovation
SurgMLLMBench 是一个明确为开发和评估互动多模态 LLMs 用于手术场景理解而设计的统一多模态基准。它集成了像素级器械分割掩码和统一分类体系下的结构化VQA注解，横跨腹腔镜、机器人辅助和显微手术领域。这使得基准能够超越传统的VQA任务进行全面评估，并提供更丰富的视觉-对话互动。
### Conclusion
广泛的基线实验表明，训练于 SurgMLLMBench 的单一模型能够在不同领域中实现一致的性能并有效泛化到未见过的数据集。SurgMLLMBench 将作为一项可靠资源向公众发布，推动多模态手术人工智能研究，并支持可重现的评估和互动手术推理模型的发展。
## 464. `cs.CV` - SAM引导的语义与运动变化区域 Mining for 遥感变化描述 [PDF](https://arxiv.org/pdf/2511.21420), [HTML](https://arxiv.org/abs/2511.21420)
### Authors
Futian Wang,Mengqi Wang,Xiao Wang,Haowen Wang,Jin Tang
### Background
遥感变化描述是一个新兴且热门的研究任务，旨在使用自然语言描述不同时刻捕捉的遥感图像之间的内容变化。现有的方法通常利用CNNs/Transformers从给定图像中提取视觉表示，或引入辅助任务来增强最终结果，但存在弱区域意识和有限的时间对齐问题。
### Innovation
本文探索了使用SAM（Segment Anything Model）基础模型来提取区域级表示并将区域兴趣知识注入描述框架。具体来说，利用CNN/Transformer模型提取全局视觉特征，利用SAM基础模型划定语义和运动变化区域，并通过特构化知识图谱提供感兴趣对象的信息。这些异质信息通过交叉注意融合，并使用Transformer解码器生成最终的自然语言描述。
### Conclusion
大量的实验结果表明，我们的方法在多个广泛使用的基准数据集上实现了最先进的性能。本文的源代码将发布在 this https URL。
## 465. `cs.CV` - PFF-Net：点云法线估计中的局部特征拟合 [PDF](https://arxiv.org/pdf/2511.21365), [HTML](https://arxiv.org/abs/2511.21365)
### Authors
Qing Li,Huifang Feng,Kanle Shi,Yue Gao,Yi Fang,Yu-Shen Liu,Zhizhong Han
### Background
传统的基于点云法线估计的方法需要构建局部补丁以提供中心-周围上下文，但确定适当的邻域大小在处理不同数据或几何时很困难。现有方法常用参数繁多的策略从输入补丁中提取完整的特征描述，但这些方法在准确和高效地预测各种点云的法线方面仍有困难。因此，本文提出了一种新的多尺度特征提取方法，以解决不同数据或几何下选择适当补丁大小的问题，以便进行鲁棒的点云法线估计。
### Innovation
该研究提出了一种新的方法PFF-Net，利用不同尺度的多尺度特征融合来解决选择适当补丁大小的问题。PFF-Net通过多尺度特征聚合和跨尺度特征补偿的方式，构建补丁特征拟合（PFF）模型，旨在提供最佳几何描述以进行法线估计。PFF-Net采用逐级聚合不同尺度下的补丁特征到补丁中心，并通过移除远离中心的点来缩小补丁大小，以实现广泛范围内的结构特性精确捕捉；并通过特征补偿模块确保不同尺度补丁特征的重用，并揭示不同尺度下的相关信息。该策略使模型能够实现不同局部补丁的尺度适应，并提供最佳特征描述。
### Conclusion
广泛的实验表明，该方法在合成和真实数据集上均实现了最先进的性能，在较少的网络参数和运行时间下取得了优异的结果。
## 466. `cs.CV` - 具有平移协变性的复值卷积神经网络 [PDF](https://arxiv.org/pdf/2511.21250), [HTML](https://arxiv.org/abs/2511.21250)
### Authors
Quentin Gabot,Teck-Yian Lim,Jérémy Fix,Joana Frontera-Pons,Chengfang Ren,Jean-Philippe Ovarlez
### Background
近年来，卷积神经网络在各种计算机视觉问题上表现出显著的性能。然而，传统的卷积神经网络架构缺少一个关键属性：平移同变性和不变性，这在下采样和上采样操作中被打破。尽管数据增强技术可以促使模型在实验上学习不变性，一种一致且系统的实现方式是通过设计在构造上保证这些属性的下采样和上采样层。引入了自适应多相采样（APS）作为平移不变性的基石，并通过可学习的多相上/下采样（LPS）扩展到平移协变性，应用于实值神经网络。在此基础上，本文从理论角度并使用$bm{C}$到$bm{R}$的投影层作为Gumbel Softmax之前的新型构建块，将LPS扩展到复值神经网络。最终，本文在分类、重建和语义分割等多种计算机视觉问题上评估了此扩展的效果，特别是在使用极化合成孔径雷达图像时验证了这两个属性。
### Innovation
本文将LPS扩展到复值神经网络，并引入了从$bm{C}$到$bm{R}$的投影层，作为Gumbel Softmax之前的新构建块，实现了复值神经网络的平移协变性。
### Conclusion
本文通过理论分析和实验验证，展示了复值神经网络在多种计算机视觉问题上的性能，特别是对于分类任务的平移不变性以及重建和语义分割问题的平移协变性，在极化合成孔径雷达图像上得到了应用。
## 467. `cs.CV` - 通用遥感多任务学习中视-语言模型的协同训练 [PDF](https://arxiv.org/pdf/2511.21272), [HTML](https://arxiv.org/abs/2511.21272)
### Authors
Qingyun Li,Shuran Ma,Junwei Luo,Yi Yu,Yue Zhou,Fengxiang Wang,Xudong Lu,Xiaoxing Wang,Xin He,Yushi Chen,Xue Yang,Junchi Yan
### Background
随着基于Transformer的遥感（RS）任务表现优异，研究者们正朝向通过多任务学习（MTL）实现在多个任务上统一模型的目标迈进。与单任务方法相比，MTL方法提供了更好的泛化能力、更高的可扩展性和更实际的应用价值。近期，视-语言模型（VLMs）在RS图像理解、语义分割和超高清（UHR）图像推理方面取得了显著成果。此外，统一的文本接口显示出为MTL提供显著潜力的潜力。因此，本文提出了一种简单而灵活的视-语言模型基线——RSCoVLM，旨在RS多任务学习中发挥作用。
### Innovation
本文提出了RSCoVLM，这是一种简单而灵活的视-语言模型基线，适用于RS多任务学习。首先，作者构建了一个数据组织引擎，涵盖数据采集、离线处理、整合、在线加载和权重分配，有效解决了复杂的数据环境，并生成灵活的视觉-语言对话。其次，提出了统一的动态分辨率策略，适用于RS图像中的各种图像尺度。对于UHR图像，提出了一种缩放链条机制及其相应的数据集LRS-VQA-Zoom。此外，还增强了模型的物体检测能力，并提出了一种新的评估协议，以确保VLMs和传统检测模型之间的公平比较。实验结果表明，RSCoVLM在多个任务上实现了最先进的性能，超越了现有的RS VLMs，并与专门的专家模型相媲美。
### Conclusion
广泛实验证明，RSCoVLM在各种任务上实现了最先进的性能，超越了现有的RS VLMs，并与专门的专家模型相媲美。所有的训练和评估工具、模型权重和数据集均已完全开源，支持可重现性。我们期望这一基线将推动向通用RS模型的发展。
## 468. `cs.CV` - E-M3RF: 一个旋转自等变的多模态3D重组框架 [PDF](https://arxiv.org/pdf/2511.21422), [HTML](https://arxiv.org/abs/2511.21422)
### Authors
Adeela Islam,Stefano Fiorini,Manuel Lecha,Theodore Tsesmelis,Stuart James,Pietro Morerio,Alessio Del Bue
### Background
3D重组是一个基础的几何问题，近年来越来越多地受到深度学习方法的挑战，而非传统的优化方法。尽管学习方法显示出有前景的结果，但大多数方法仍主要依赖于几何特征来组装完整的对象。因此，当仅依赖几何特征不足或模棱两可时，这些方法在处理小的、侵蚀的或对称的碎片时会有困难。此外，现有的解决方案未设置物理约束来防止组装的重叠。
### Innovation
我们提出了一种名为E-M3RF的旋转自等变的多模态3D重组框架，它能输入包含断裂碎片点云以及三维点位置和颜色的信息，并预测重组所需的变换，使用SE(3)流匹配。每个碎片都由几何和颜色特征表示。3D点位置使用旋转自等变编码器编码，颜色通过变压器编码，然后结合两个特征集以形成多模态表示。
### Conclusion
我们在四个数据集上进行了实验：两个合成数据集Breaking Bad和Fantastic Breaks，以及两个文化遗产数据集RePAIR和Presious。结果显示，E-M3RF方法在RePAIR数据集上的旋转误差减少了23.1%，平移误差减少了13.2%，且均方误差减少18.4%，相比竞争方法有显著提升。
## 469. `cs.CV` - EvRainDrop: HyperGraph-guided Completion for Effective Frame and Event Stream Aggregation [PDF](https://arxiv.org/pdf/2511.21439), [HTML](https://arxiv.org/abs/2511.21439)
### Authors
Futian Wang,Fan Zhang,Xiao Wang,Mengqi Wang,Dexing Huang,Jin Tang
### Background
事件相机生成异步事件流，这些流在空间上稀疏但在时间上密集。主流的事件表示学习算法通常使用事件帧、体素或张量作为输入。尽管这些方法取得了显著的进展，但它们难以解决由于空间稀疏性引起的采样不足问题。
### Innovation
本文提出了一种新颖的基于超图的时空事件流完成机制，通过超图连接不同时间和空间位置的事件令牌，并利用上下文信息消息传递来完成这些稀疏事件。在完成框架中，可以灵活地将RGB令牌作为超图中的节点，实现多模态超图信息完成。此外，通过自注意力机制跨不同时间步聚合超图节点信息，从而实现多模态特征的有效学习和融合。
### Conclusion
在单标签和多标签事件分类任务上的广泛实验充分验证了本文所提出框架的有效性。源代码将在以下链接发布：this https URL
## 470. `cs.CV` - 深度伪造检测器的一般化设计选择 [PDF](https://arxiv.org/pdf/2511.21507), [HTML](https://arxiv.org/abs/2511.21507)
### Authors
Lorenzo Pellegrini,Serafino Pandolfini,Davide Maltoni,Matteo Ferrara,Marco Prati,Marco Ramilli
### Background
深度伪造检测方法的效果往往不依赖于其核心设计，而是更多地取决于数据预处理、增强策略和优化技术等实现细节。这些因素使得不同检测器之间的公平比较变得困难，并且难以理解哪些因素真正影响了它们的性能。
### Innovation
本文系统性地研究了不同的设计选择如何影响深度伪造检测模型的准确性和泛化能力，重点关注训练、推理和增量更新等方面。通过分离个体因素的影响，本文旨在建立一种通用且架构无关的最佳实践，用于设计和开发未来的深度伪造检测系统。实验结果指出了能持续改进深度伪造检测的设计选择，并使得在AI-GenBench基准测试中达到最先进的性能。
### Conclusion
本文确定了一系列能持续改进深度伪造检测的设计选择，并使其在AI-GenBench基准测试上达到最先进的性能。
## 471. `cs.CV` - EoS-FM： Specialist 模型可以成为通用特征提取器吗？ [PDF](https://arxiv.org/pdf/2511.21523), [HTML](https://arxiv.org/abs/2511.21523)
### Authors
Pierre Adorni,Minh-Tan Pham,Stéphane May,Sébastien Lefèvre
### Background
近期，基础模型在自然语言处理和计算机视觉等领域取得了显著进展，类似的努力也开始出现在地球观测领域。这些模型旨在在有限监督的情况下泛化到各种任务，从而减少为每个任务训练单独模型的需求。然而，现有的策略主要集中在扩大模型规模和数据集大小上，这对计算和数据资源的要求非常高，限制了普通机构的访问能力。此外，这种大型模型的趋势与可持续和环境友好型 AI 的原则背道而驰，因为它会导致巨大的碳足迹和资源浪费。
### Innovation
本文提出了一种新颖且高效的替代方案：以 ConvNeXtV2 专家为基础的远程 sensing 基础模型（RSFMs）的专家群组框架（Ensemble-of-Specialists）。该方法将训练过程分解为轻量级的任务特定专家，可以被冻结并重新使用。这种模块化的方法在效率、可解释性和可扩展性方面具有显著优势，并且自然支持联邦训练、剪枝和连续专家集成，使其特别适合协作和资源受限的环境。
### Conclusion
本框架为构建可扩展且高效的 RSFMs 设定了新的方向。
## 472. `cs.CV` - 非均匀时间跨度中具有特征约束的年龄特异性阿尔茨海默病预测 [PDF](https://arxiv.org/pdf/2511.21530), [HTML](https://arxiv.org/abs/2511.21530)
### Authors
Xin Hong,Kaifeng Huang
### Background
阿尔茨海默病是一种严重影响认知功能的疾病。及时确诊该病对于开发旨在减缓其进展的个性化治疗方法至关重要。然而，在不同时间间隔捕获的输入序列用于图像生成时，准确代表疾病特征的预测面临挑战。本文探讨了一种基于定量指标的顺序图像生成方法，以保留疾病进展的关键特征，并通过整合年龄缩放因子生成年龄特异性MRI图像，助力预测疾病的晚期阶段。
### Innovation
提出了一种创新的方法，通过使用定量指标指导顺序图像生成，以保持疾病进展的关键特征。引入年龄缩放因子生成年龄特异性MRI图像，这种方法有助于预测疾病的晚期阶段。研究发现，包含定量指标显著提高了MRI图像合成的准确性，应用年龄缩放像素损失进一步提高了MRI图像的迭代生成效果。
### Conclusion
研究结果表明，结构相似性指数达到了0.882的峰值，表明合成图像与实际图像之间有很高的相似度。这表明提出的基于定量指标的顺序图像生成方法以及年龄缩放像素损失对于提高阿尔茨海默病预测的准确性非常有效。
## 473. `cs.CV` - CanKD：基于交叉注意力的非局部操作以特征为基础的知识蒸馏 [PDF](https://arxiv.org/pdf/2511.21503), [HTML](https://arxiv.org/abs/2511.21503)
### Authors
Shizhe Sun,Wataru Ohyama
### Background
传统基于自注意力的知识蒸馏方法独立对教师和学生特征图进行对齐，这导致像素间的细节关系没有得到充分捕捉。这种特点限制了特征表示学习的效果。
### Innovation
提出了一种基于交叉注意力机制的非局部知识蒸馏方法（CanKD），每个学生特征图中的像素都可以动态地考虑教师特征图中的所有像素，这样可以更全面地捕捉像素之间的关系，从而改进特征表示学习。
### Conclusion
广泛的实验表明，CanKD在物体检测和图像分割任务上优于现有的基于注意力的知识蒸馏方法，显示出其作为计算机视觉任务中注意力引导知识蒸馏新范式的潜力。
## 474. `cs.CV` - Merge and Bound: 直接对权重的操作用于类增量学习 [PDF](https://arxiv.org/pdf/2511.21490), [HTML](https://arxiv.org/abs/2511.21490)
### Authors
Taehoon Kim,Donghwan Jang,Bohyung Han
### Background
论文背景介绍类增量学习（Class Incremental Learning, CIL）的问题，即在模型训练过程中逐步引入新类，同时尽可能保留之前学习到的知识，防止灾难性遗忘。现有的CIL方法通常需要较为复杂的机制来处理这一点，但这些方法可能引入新的损失函数或修改模型架构。
### Innovation
论文提出了一种新颖的训练方法，名为Merge-and-Bound (M&B)，直接在参数空间中操纵模型权重进行优化。M&B包括两种权重合并：跨任务（inter-task）权重合并和同任务（intra-task）权重合并。此外，该算法还提出了一种有界的更新技术，以最小化累计更新同时保持先前任务的知识，减少灾难性遗忘。该方法不需要修改现有CIL方法的架构或学习目标。
### Conclusion
实验结果表明，M&B方法在标准CIL基准上的性能优于最先进的方法，能够有效缓解灾难性遗忘问题。
## 475. `cs.CV` - 视频生成模型是良好的隐空间奖励模型 [PDF](https://arxiv.org/pdf/2511.21541), [HTML](https://arxiv.org/abs/2511.21541)
### Authors
Xiaoyue Mi,Wenqing Yu,Jiesong Lian,Shibo Jie,Ruizhe Zhong,Zijun Liu,Guozhen Zhang,Zixiang Zhou,Zhiyong Xu,Yuan Zhou,Qinglin Lu,Fan Tang
### Background
Reward feedback learning (ReFL) 已证明对对齐图像生成与人类偏好方面非常有效。然而，将其扩展到视频生成时遇到了重大挑战。现有的视频奖励模型依赖于面向像素空间输入的视觉语言模型，这限制了ReFL优化主要集中在昂贵的VAE解码之后的近完全去噪步骤，这引发了巨大的内存开销和增加的训练时间，并且其在后期阶段的优化缺乏早期阶段的监督，仅仅优化视觉质量而忽视了根本的运动动态和结构一致性。
### Innovation
本文通过证明预训练的视频生成模型自然适合于在噪声隐空间进行奖励建模，展示了PRFL框架（Process Reward Feedback Learning）。PRFL在隐空间内进行偏好优化，从而在整个去噪链中实现高效的梯度反向传播，而无需进行VAE解码。
### Conclusion
大量实验表明，PRFL显著提高了对齐人类偏好的能力，同时，在内存消耗和训练时间上相比RGB ReFL实现了显著的减少。
## 476. `cs.CV` - MobileI2V：移动设备上的快速高分辨率图像到视频合成 [PDF](https://arxiv.org/pdf/2511.21475), [HTML](https://arxiv.org/abs/2511.21475)
### Authors
Shuai Zhang,Bao Tang,Siyuan Yu,Yueting Zhu,Jingfeng Yao,Ya Zou,Shanglin Yuan,Li Yu,Wenyu Liu,Xinggang Wang
### Background
随着视频生成领域取得迅速进展，图像到视频（I2V）合成在移动设备上的关注度增加。然而，扩散模型在移动设备上实现实时、高分辨率视频生成面临巨大挑战，主要由于计算复杂性和生成速度慢。
### Innovation
提出了MobileI2V，一种针对移动设备的270M轻量级扩散模型，实现了以下创新：1) 分析了线性注意力模块和softmax注意力模块在移动设备上的性能，提出了一种线性混合架构去噪器，平衡生成效率和质量；2) 设计了时间步长蒸馏策略，将I2V采样步骤从超过20步压缩到只有两步，生成速度提高了10倍且质量损失不大；3) 应用了移动设备特定的注意力优化，使得推理过程中的注意力操作速度提高2倍。
### Conclusion
MobileI2V首次在移动设备上实现了720p图像到视频的快速生成，生成质量与现有模型相当。在单步条件下，720p视频每一帧的生成速度低于100毫秒。
## 477. `cs.CV` - 在盆腔透视中使用2D/3D注册损失增强的地标检测模型 [PDF](https://arxiv.org/pdf/2511.21575), [HTML](https://arxiv.org/abs/2511.21575)
### Authors
Chou Mo,Yehyun Suh,J. Ryan Martin,Daniel Moyer
### Background
自动地标检测为医疗专业人员提供了一种高效的方法，通过术中成像来理解患者的解剖结构和定位。现有利用盆腔侧位透视图像进行地标检测的方法在准确性方面表现出潜在的优势，但大多数方法假设盆腔为固定的标准前向后位。然而，实际情况下盆腔的定位往往会偏离这个标准的视角，这可能是由于成像单元或目标结构的重新定位导致的。
### Innovation
本文提出了一种新的框架，将2D/3D地标注册引入U-Net地标预测模型的训练过程中，以克服现有方法的局限性。通过比较使用姿势估计损失训练的基线U-Net模型、以及使用姿势估计损失微调的U-Net模型的地标检测准确性，在模拟术中实际患者姿势变化的条件下分析了其性能差异。
### Conclusion
该研究提出的方法在多种实际术中情况下提高了盆腔透视中地标的检测准确性，通过对不同训练方法的对比分析，该方法有效提高了地标检测的鲁棒性和准确性。
## 478. `cs.CV` - ReSAM：强化、再查询和再增强：用于遥感图像的自我提示点监督分割 [PDF](https://arxiv.org/pdf/2511.21606), [HTML](https://arxiv.org/abs/2511.21606)
### Authors
M.Naseer Subhani
### Background
交互式分割模型如Segment Anything Model (SAM) 在自然图像上的泛化表现优异，但在遥感影像（RSI）上的表现欠佳，这主要是因为严重的领域迁移和稀疏的密集注释资源。
### Innovation
本文提出了一种自我提示、点监督框架，通过仅使用稀疏的点注释将SAM适应RSI。该方法采用Refine-Requery-Reinforce循环，从初始点生成粗略的伪掩码，利用自构建的框提示改进，迭代对齐嵌入以减少确认偏差，无需依赖全掩码监督，通过自我指导的提示适应逐步提升SAM分割质量和领域健壮性。
### Conclusion
本文方法在包括WHU、HRSID和NWPU VHR-10三个RSI基准数据集上进行了评估，结果显示该方法能够持续超越预训练SAM和最近的点监督分割方法。实验结果表明，自我提示和语义对齐为大规模点级适应基础分割模型提供了有效的途径，适应遥感应用。
## 479. `cs.CV` - Awareness of Frequency for Token Reduction in Efficient Vision Transformer [PDF](https://arxiv.org/pdf/2511.21477), [HTML](https://arxiv.org/abs/2511.21477)
### Authors
Dong-Jae Lee,Jiwan Hur,Jaehyun Choi,Jaemyung Yu,Junmo Kim
### Background
尽管视觉变换器在各种计算机视觉任务中表现出色，但其与标记长度成二次复杂性的计算复杂性仍然是一个重大挑战。现有的标记减少方法已经广泛探索，但它们常常忽视了自注意力的频率特性，比如秩坍缩和过度平滑的现象。
### Innovation
本文提出了一种频率感知的标记减少策略，通过保留高频标记并将低频标记聚合为一个紧凑的直接电流标记，来提升计算效率同时保持性能，从而减轻秩坍缩现象，并通过广泛的实验和分析，证明了该方法在提高准确率的同时减少了计算开销，缓解了秩坍缩和过度平滑。
### Conclusion
此外，我们还分析了先前的方法，揭示了它们的隐含频率特性和局限性。
## 480. `cs.CV` - 3D点云模型多模态鲁棒提示蒸馏 [PDF](https://arxiv.org/pdf/2511.21574), [HTML](https://arxiv.org/abs/2511.21574)
### Authors
Xiang Gu,Liming Lu,Xu Zheng,Anan Du,Yongbin Zhou,Shuchao Pang
### Background
基于学习的3D点云模型受到对抗攻击的严重威胁，这大大削弱了其在安全敏感应用中的可靠性。现有防御方法通常存在高计算开销和对不同攻击类型的较差泛化能力的问题。
### Innovation
提出了一种新颖且高效的教师-学生框架——多模态鲁棒提示蒸馏（MRPD），用于提取鲁棒的3D点云模型。通过三种不同教师（视觉模型处理深度投影、高性能3D模型和文本编码器）的鲁棒嵌入对齐学习轻量级提示，并由信心门控机制指导知识传递，确保模态输入动态平衡贡献。MRPD在各种白盒和黑盒攻击下显著优于最先进的防御方法，甚至在干净数据上表现出更好的性能。
### Conclusion
我们的工作提出了一种新的实际范例，通过有效利用多模态知识来构建鲁棒的3D视觉系统。
## 481. `cs.CV` - 基于GCN的动作识别中的主动学习 [PDF](https://arxiv.org/pdf/2511.21625), [HTML](https://arxiv.org/abs/2511.21625)
### Authors
Hichem Sahbi
### Background
尽管基于图卷积网络（GCNs）的骨架动作识别已经取得了显著的成果，但其性能往往依赖于大量标注数据，而在实际应用中，这类数据通常稀缺。
### Innovation
我们提出了一种新的标签高效GCN模型，主要创新点包括：1）开发了一种基于对抗策略的新型获取函数，以选择具有代表性和多样性的信息示例用于标注；2）提出了双向和稳定的GCN架构，这些架构有助于更好地映射环境和潜在数据空间，使模型更好地理解所学示例分布。
### Conclusion
大量的实证评估表明，我们的标签高效GCNs相较于前人工作取得了显著的进步。
## 482. `cs.CV` - 从观察到行动：工业环境中基于潜在动作的基本动作分割以用于VLA预训练 [PDF](https://arxiv.org/pdf/2511.21428), [HTML](https://arxiv.org/abs/2511.21428)
### Authors
Jiajie Zhang,Sören Schwertfeger,Alexander Kleiner
### Background
该研究旨在利用连续的工业视频流中的未标记人类演示数据来预训练Vision-Language-Action (VLA)模型。现有技术通常依赖大量标记数据，但此研究提出了一种无需人工标注的新框架，解决了一些工业场景下的数据稀缺问题。
### Innovation
该研究创新地提出了一种无监督框架，该框架包含两个主要步骤：首先，通过训练一个轻量级的动作分词器来编码运动动力学；其次，使用一种新颖的“潜在动作能量”度量建立一个无监督的动作分割器来发现并分割出具有语义连贯性的基本动作。这种方法直接输出分割后的视频片段及其对应的潜在动作序列，提供了可用于VLA预训练的结构化数据。
### Conclusion
实验证实该方法可以有效分割工人在工作站执行的关键任务。通过进一步的聚类和视觉语言模型的定量评估验证了发现的基本动作具有语义一致性。该研究是第一个完全自动化的端到端系统，用于从不结构化的工业视频中提取和整理VLA预训练数据，为制造业中的嵌入式AI集成提供了可扩展的解决方案。
## 483. `cs.CV` - UAVLight：无人飞行器(UAV)场景中光照鲁棒3D重建基准 [PDF](https://arxiv.org/pdf/2511.21565), [HTML](https://arxiv.org/abs/2511.21565)
### Authors
Kang Du,Xue Liao,Junpeng Xia,Chaozheng Guo,Yi Gu,Yirui Guan,Duotun Wang,ShengHuang,Zeyu Wang
### Background
多视图三维重建中的光照不一致性是一个基本挑战。不同方向的阳光、云层覆盖和阴影变化打破了经典多视图立体视觉(MVS)和结构光度(SfM)流程以及最近的神经渲染方法所依赖的恒定光照假设，导致几何漂移、颜色不一致和阴影叠加。该问题在基于无人机(UGV)的重建中尤为重要，因为长飞行时间和户外环境使得光照变化不可避免。然而，现有的数据集要么限制捕获到短时间段内，缺乏有意义的光照多样性；要么跨越数月和季节，导致几何和语义变化混杂，难以单独研究光照鲁棒性。
### Innovation
我们引入了UAVLight，这是一个控制性的现实基准，用于光照鲁棒3D重建。每个场景沿可重复的地理参考飞行路径在一天中不同的固定时间捕获，从而在保持一致的几何形状、校准和视点的情况下产生自然的光照变化。UAVLight通过跨光照条件下标准化的评价协议，为开发和基准测试在实际户外环境中一致、忠实和可重光的重建方法提供了可靠的平台。
### Conclusion
UAVLight提供了一个可靠的基准，用于开发和评测在实际户外环境中一致、忠实和可重光的重建方法。
## 484. `cs.CV` - MoGAN：通过少量步骤的运动对抗后训练提高视频扩散中的运动质量 [PDF](https://arxiv.org/pdf/2511.21592), [HTML](https://arxiv.org/abs/2511.21592)
### Authors
Haotian Xue,Qi Chen,Zhonghao Wang,Xun Huang,Eli Shechtman,Jinrong Xie,Yongxin Chen
### Background
视频扩散模型在帧级别的保真度表现强劲，但在运动连贯性、动态效果和真实性方面仍然存在不足，常常产生抖动、鬼影或不合理的动态效果。标准的去噪均方误差（MSE）目标缺乏对时间一致性直接的监督，使得模型即使生成质量较低的运动也能达到较低的损失值。因此，通过改进模型的运动质量，而不依赖奖励模型或人类偏好数据，是亟待解决的问题。
### Innovation
提出MoGAN，一种以运动为中心的后训练框架，旨在提升运动的真实感。莫创建在三步蒸馏视频扩散模型之上，通过训练基于DiT的光学流鉴别器区分真实运动与生成运动，并结合分布匹配正则化器以保持视觉保真度。实验结果表明，与教师模型和DMD模型相比，MoGAN在多基准测试上显著改善了运动质量。
### Conclusion
MoGAN在不断提高运动质量的同时，不会牺牲视觉保真度或效率，为快速、高质量视频生成提供了一条实用途径。人类研究表明，MoGAN在运动质量方面更受欢迎。项目网页链接见此 https URL。
## 485. `cs.CV` - 使用自适应学习速率进行抗核抗体图像的学习 [PDF](https://arxiv.org/pdf/2511.21519), [HTML](https://arxiv.org/abs/2511.21519)
### Authors
Yiyang Jiang,Guangwu Qian,Jiaxin Wu,Qi Huang,Qing Li,Yongkang Wu,Xiao-Yong Wei
### Background
抗核抗体(ANA)检测是诊断自身免疫性疾病的关键方法，包括系统性红斑狼疮、舍格伦综合征和硬皮病等。虽重要，但手工检测ANAs耗时、劳动密集且需要多年的训练。由于存在超过100种共存的抗体检针类型，导致了巨大的荧光图案组合。尽管机器学习和深度学习助力自动化，但实际上在临床环境中进行ANAs检测仍面临多实例、多标签(MIML)学习的独特挑战。
### Innovation
本文提出了一种新的ANAs检测框架，不需手动预处理就能处理MIML任务的复杂性，采用三部分具体任务组件：样本采样器、概率伪标签分发器和自我步进学习率系数。该框架通过模型图案置信度来抑制低置信度样本，分发器依据实例区分度自适应分发标签，自我步进学习调整训练根据经验标签观察。该框架克服了传统MIML方法的局限，并支持端到端优化。
### Conclusion
我们在一个ANAS数据集和三个公开的医疗MIML基准测试数据集上进行了广泛实验，表明我们的框架优于先前的最好方法。在ANAS数据集上，比最佳前期方法在F1-Macro和mAP上分别提高了+7.0%和+12.6%。在公开数据集上，按所有关键指标排名前二，将汉明损失和一名误差分别降低了最多18.2%和26.9%。
## 486. `cs.CV` - 和谐度：通过跨任务协同作用同步音频和视频生成 [PDF](https://arxiv.org/pdf/2511.21579), [HTML](https://arxiv.org/abs/2511.21579)
### Authors
Teng Hu,Zhentao Yu,Guozhen Zhang,Zihan Su,Zhengguang Zhou,Youliang Zhang,Yuan Zhou,Qinglin Lu,Ran Yi
### Background
在生成式AI中，同步音频-视觉内容的合成是一个关键挑战。开源模型在稳健的音频-视频对齐方面面临挑战。分析发现，这个问题源于三个基本挑战：（1）对应关系漂移，同步演变的噪声潜在变量妨碍了对齐的稳定学习；（2）低效的全局注意力机制无法捕捉到精细的时序线索；（3）传统无条件引导（CFG）的内模偏见，这增强了条件性但未能实现跨模态同步。
### Innovation
我们引入了Harmony，一个新颖的框架，机械地确保音频-视觉同步。首先，我们提出了一种跨任务协同训练方法，通过利用由音频驱动的视频生成任务和视频驱动的音频生成任务提供的强监督信号来减轻漂移。然后，我们设计了一种全局-局部解耦交互模块，以实现高效且精确的时序风格对齐。最后，我们提出了一个新颖的同步增强无条件引导（SyncCFG），在推断过程中明确隔离并放大对齐信号。广泛的实验证明，Harmony建立了新的最先进的性能，在生成保真度方面优于现有方法，并且最关键地，在实现精细的音频-视觉同步方面表现优异。
### Conclusion
Harmony框架通过跨任务协同作用显著提高了音频-视觉生成中的同步性，建立了新的性能基准。
## 487. `cs.CV` - Qwen3-VL 技术报告 [PDF](https://arxiv.org/pdf/2511.21631), [HTML](https://arxiv.org/abs/2511.21631)
### Authors
Shuai Bai,Yuxuan Cai,Ruizhe Chen,Keqin Chen,Xionghui Chen,Zesen Cheng,Lianghao Deng,Wei Ding,Chang Gao,Chunjiang Ge,Wenbin Ge,Zhifang Guo,Qidong Huang,Jie Huang,Fei Huang,Binyuan Hui,Shutong Jiang,Zhaohai Li,Mingsheng Li,Mei Li,Kaixin Li,Zicheng Lin,Junyang Lin,Xuejing Liu,Jiawei Liu,Chenglong Liu,Yang Liu,Dayiheng Liu,Shixuan Liu,Dunjie Lu,Ruilin Luo,Chenxu Lv,Rui Men,Lingchen Meng,Xuancheng Ren,Xingzhang Ren,Sibo Song,Yuchong Sun,Jun Tang,Jianhong Tu,Jianqiang Wan,Peng Wang,Pengfei Wang,Qiuyue Wang,Yuxuan Wang,Tianbao Xie,Yiheng Xu,Haiyang Xu,Jin Xu,Zhibo Yang,Mingkun Yang,Jianxin Yang,An Yang,Bowen Yu,Fei Zhang,Hang Zhang,Xi Zhang,Bo Zheng,Humen Zhong,Jingren Zhou,Fan Zhou,Jing Zhou,Yuanzhi Zhu,Ke Zhu
### Background
Qwen3-VL 是 Qwen 系列中目前最强大的多模态视图-语言模型，具备广泛多模态基准测试中的出色性能，支持长达256K token的交错上下文，整合了文本、图像和视频。它有多个变体，包括密集型（2B/4B/8B/32B）和混合专家型（30B-A3B/235B-A22B），以适应不同的延迟-质量权衡。
### Innovation
Qwen3-VL 核心贡献包括：1. 强大的纯文本理解能力，超越部分仅文本后端；2. 强大的长文本和多模态上下文理解能力，具有256K token的窗口，支持长文档和视频的忠实保留、检索和跨参考；3. 高级多模态推理，涵盖单图像、多图像和视频任务，表现出色的综合评估，如 MMMU 和视觉-数学基准（例如 MathVista 和 MathVision）。此外，其架构升级包括：1. 增强的交错-MRoPE，增强图像和视频的空间-时间建模；2. DeepStack 集成，高效利用多层 ViT 特征以更好地对齐视觉-语言；3. 视频的文本对齐，从 T-RoPE 到明确的文本时间戳对齐，以更精确的时间定位。
### Conclusion
在同等的标记预算和延迟约束下，Qwen3-VL 优越的性能在密集型和混合专家型架构中均表现良好。Qwen3-VL 将作为图像基础的推理、自主决策和多模态代码智能的基础引擎应用于实际工作流程中。
## 488. `cs.CV` - CaFlow: 提升长期动作质量评估的因果反事实流 [PDF](https://arxiv.org/pdf/2511.21653), [HTML](https://arxiv.org/abs/2511.21653)
### Authors
Ruisheng Han,Kanglei Zhou,Shuang Chen,Amir Atapour-Abarghouei,Hubert P. H. Shum
### Background
动作质量评估（AQA）可以通过从动作视频中预测精细执行分数来应用于体育、康复和技能评估等领域。然而，对于长期AQA，例如花样滑冰和体操，其挑战在于需要建模长时间的动力学特征，同时保持对上下文干扰因素的鲁棒性。现有的方法要么依赖昂贵的标注，要么依赖单向时间建模，这使得它们容易产生虚假的相关性，并且长期表示不稳定。
### Innovation
我们提出了CaFlow，一种集成了反事实去混淆与双向时间条件流的统一框架。Causal Counterfactual Regularization (CCR) 模块通过自监督方式分离因果和混淆特征，并通过反事实干预确保因果鲁棒性；BiT-Flow模块通过循环一致性约束来建模正向和反向动力学，生成更平滑且更连贯的表示。在多个长期AQA基准测试上的广泛实验表明，CaFlow达到了最先进的性能。
### Conclusion
CaFlow在多个长期AQA基准测试中表现出了最先进的性能。代码可在以下链接获得：this https URL
## 489. `cs.CV` - Multi-Crit: 评估多模态评判者的多元标准遵从性基准 [PDF](https://arxiv.org/pdf/2511.21662), [HTML](https://arxiv.org/abs/2511.21662)
### Authors
Tianyi Xiong,Yi Ge,Ming Li,Zuolong Zhang,Pranav Kulkarni,Kaishen Wang,Qi He,Zeying Zhu,Chenxi Liu,Ruibo Chen,Tong Zheng,Yanshuo Chen,Xiyao Wang,Renrui Zhang,Wenhu Chen,Heng Huang
### Background
大型多模态模型（LMMs）因其强大的指令遵循能力和与人类偏好的一致性，在多模态评价系统中被广泛采用。然而，它们在遵循多样化、细致的评价标准方面的能力尚未得到充分探索。
### Innovation
开发了Multi-Crit基准，用于评估多模态评判者的能力以遵循多元标准并产生可靠的判定。Multi-Crit包括一个严格的数据整理流程，汇聚具有多标准人工注释的具有挑战性的响应对，并引入了三个新颖的评估指标，用于系统地评估多元一致性、判断切换灵活性以及识别标准水平偏好冲突的能力。
### Conclusion
全面分析了25个LMMs，揭示了以下三点：1) 专有模型在保持对多元标准的一致遵从性方面仍然面临困难，尤其是在开放评价中；2) 开源模型在灵活遵循多样化标准方面更是落后；3) 用整体判断信号微调批判模型可以在视觉接地方面有所提升，但无法推广到多元标准的评估中。此外，对推理微调、测试时缩放以及开源与专有模型之间的边界一致性进行的进一步分析进一步探查了当前多模态评判器的极限。Multi-Crit为构建可靠且可控制的多模态AI评价奠定了基础。
## 490. `cs.CV` - 注意力指导下的视话行动（Vision-Language-Action）模型局部稀疏对抗攻击 [PDF](https://arxiv.org/pdf/2511.21663), [HTML](https://arxiv.org/abs/2511.21663)
### Authors
Naifu Zhang,Wei Tao,Xi Xiao,Qianpu Sun,Yuxin Zheng,Wentao Mo,Peiqiang Wang,Nan Zhang
### Background
近年来，嵌入式智能中的视话行动（VLA）模型发展迅速。然而，现有的对抗攻击方法需要昂贵的端到端训练，且通常会产生明显的扰动贴图。
### Innovation
本文提出了一种名为ADVLA的框架，该框架可以直接将视觉编码器转换到文本特征空间的特征上的对抗扰动应用于特征上。ADVLA在低振幅约束下有效地扰乱了下游动作预测，并通过注意力指导使扰动既集中又稀疏。引入了三种策略来增强敏感性、强制稀疏性和集中扰动。
### Conclusion
实验表明，当在$L_{fty}=4/255$的约束下与Top-K掩码结合使用时，ADVLA修改的贴图少于10%，攻击成功率接近100%。扰动集中在关键区域，几乎不会在整体图像中被察觉，并且单步迭代只需约0.06秒，显著优于传统的基于贴图的攻击。总之，ADVLA在低振幅和局部稀疏条件下有效地降低了VLA模型的下游动作预测，避免了传统基于贴图攻击的高训练成本和明显扰动，并且在攻击VLA特征空间方面显示出独特的作用和实用价值。
## 491. `cs.CV` - 利用3D MRI 引导的混合深度学习模型革新胶质瘤分割与分级 [PDF](https://arxiv.org/pdf/2511.21673), [HTML](https://arxiv.org/abs/2511.21673)
### Authors
Pandiyaraju V,Sreya Mynampati,Abishek Karthik,Poovarasan L,D. Saraswathi
### Background
胶质瘤是一种脑肿瘤类型，具有高死亡率，因此早期和准确的诊断对于肿瘤的治疗干预至关重要。为了应对这一挑战，本研究将开发一种结合了基于U-Net的分割和混合DenseNet-VGG分类网络（具备多头注意和空间-通道注意功能）的混合深度学习模型。分割模型将基于空间和上下文信息精确地在MRI数据的3D体素中勾画出肿瘤边界。分类网络结合了DenseNet和VGG的部分，将关注经过分割的肿瘤上的具有注意机制的临床上相关的特征。通过预处理步骤，包括归一化、重采样和数据增广，高维3D MRI数据能够被成功地用于模型中。该框架通过各种度量进行评估：分割性能指标为Dice系数和Mean Intersection over Union（IoU），分类性能指标为准确率、召回率和F1分数。
### Innovation
该研究提出了一种混合深度学习模型，结合了基于U-Net的分割和融合了多头注意力机制和空间-通道注意力机制的混合DenseNet-VGG分类网络。此模型能够在肿瘤分割中达到98%的Dice系数和99%的分类准确性，优于传统的CNN模型和无注意力机制的方法，提升了识别重要临床部分的能力，增强了可解释性和准确性。
### Conclusion
提出的混合框架通过实际测试表明，在胶质瘤的分割和分级诊断方面具有巨大的潜力，有助于临床医生更及时可靠地做出诊断和分级，并为患者的治疗计划提供了更好的依据，展示了模型的有效性和实用性。
## 492. `cs.CV` - Prompt-Aware Adaptive Elastic Weight Consolidation for Continual Learning in Medical Vision-Language Models [PDF](https://arxiv.org/pdf/2511.20732), [HTML](https://arxiv.org/abs/2511.20732)
### Authors
Ziyuan Gao,Philippe Morel
### Background
医疗AI系统在临床环境中部署时面临灾难性遗忘的问题，特别是模型需要学习新的成像协议，同时保留之前的诊断能力。这尤其对医疗视觉-语言模型构成挑战，因为这些模型必须在不同成像模态之间保持复杂的跨模态对齐，同时保留医学影像和临床术语之间的复杂关系。
### Innovation
本文引入了一种新型持续学习方法——Prompt-Aware Adaptive Elastic Weight Consolidation (PA-EWC)，该方法通过提示引导参数专业化来解决灾难性遗忘问题。PA-EWC结合了自适应Fisher信息计算与梯度稳定性分析，开发了基于医学术语密度的加权复杂性度量，系统地对模型参数进行分类，以保护关键知识，同时允许适应新的临床需求。
### Conclusion
我们的方法在五个医疗影像数据集（Kvasir-SEG、ISIC 2018、CheXlocalize、BUSI、CAMUS）上进行了评估，包括内镜、皮肤镜、X射线、超声等不同模态。实验结果表明，PA-EWC可减少比基准方法高达17.58%的灾难性遗忘，胸片病理定位性能提高4.30%，息肉分割性能提高6.06%。
## 493. `cs.CV` - 使用多阶段视觉变换器框架自动评估希氏腺疾病 [PDF](https://arxiv.org/pdf/2511.20734), [HTML](https://arxiv.org/abs/2511.20734)
### Authors
Youssef Megahed,Saleh Abou-Alwan,Anthony Fuller,Dina El Demellawy,Steven Hawken,Adrian D. C. Chan
### Background
希氏腺疾病是一种肠管局部缺乏神经节细胞的病症，准确识别神经节细胞对于诊断该病至关重要。目前，人工病理诊断在分割肌层、识别神经丛和细胞方面存在挑战，特别是在复杂组织结构中对细胞形态的捕捉上较为困难。
### Innovation
本文提出了一种基于Vision Transformer (ViT-B/16)的三阶段分割框架，模仿病理学家的诊断流程。该框架依次分割肌层、界定神经丛，并在解剖学上有效区域内识别神经节细胞。该方法在不同精确度的全组织切片图像上测试，通过跨验证策略和特定分辨率的切片策略及定制化后处理确保解剖学的一致性。结果显示，该方法在肌层分割上的Dice系数为89.9%，在神经丛分割上有100%的包含率，神经节细胞识别的召回率和精确度分别为89.1%和62.1%，联合可信度评分的精确度为67.0%。
### Conclusion
基于ViT的模型能够有效利用大组织的全局上下文，捕捉细胞形态，即使在复杂的组织结构中也表现不凡。多阶段方法具有支持数字病理工作流程，降低观察者间变异性，辅助希氏腺疾病评估的潜力，并将在后续使用更多中心的大规模数据和额外专家注释进行临床影响评估中得到进一步验证。
## 494. `cs.CV` - 低资源设备上的持续错误修正 [PDF](https://arxiv.org/pdf/2511.21652), [HTML](https://arxiv.org/abs/2511.21652)
### Authors
Kirill Paramonov,Mete Ozay,Aristeidis Mystakidis,Nikolaos Tsalikidis,Dimitrios Sotos,Anastasios Drosou,Dimitrios Tzovaras,Hyunjun Kim,Kiseok Chang,Sangdok Mo,Namwoong Kim,Woojong Yoo,Jijoong Moon,Umberto Michieli
### Background
日常设备中AI模型的普及暴露出一个重要挑战：预测错误会降低用户体验。现有解决方案主要集中在错误检测，但很少提供有效的修正机制，特别对于资源受限的设备而言。
### Innovation
本文介绍了一个新颖的系统，允许用户通过少量化学习纠正AI的误分类，所需计算资源和存储空间最小化。该方法结合了服务器端的基础模型训练和设备端的原型分类机制，实现通过原型更新而非重新训练模型来进行高效的错误修正。系统包括两个关键组件：（1）一个利用知识蒸馏的服务器端管道，使其能够将稳健的特征表示从基础模型转移到设备兼容的架构；（2）一个设备端机制，能够通过原型适应实现超高效错误修正。
### Conclusion
我们在Food-101和Flowers-102数据集上的分类和对象检测任务中验证了该系统的有效性，在单次修正场景中达到了超过50%的错误修正率，同时具有极低的遗忘率（少于0.02%）和几乎可以忽略不计的计算开销。通过Android演示应用程序，我们的实现证明该系统在实际场景中具有实用性。
## 495. `cs.CV` - 神经元的保证最优组合解释 [PDF](https://arxiv.org/pdf/2511.20934), [HTML](https://arxiv.org/abs/2511.20934)
### Authors
Biagio La Rosa,Leilani H. Gilpin
### Background
目前，虽然神经元是深层神经网络的基本单位，但还不清楚它们学会了什么，并且它们的知识是否与人类的知识相一致。组成性的解释旨在通过逻辑规则描述神经元激活与概念之间的空间对齐。这些逻辑描述通常通过所有可能的概念组合的搜索来计算。但由于整个状态空间上的空间对齐计算是不可行的，文献中通常使用束搜索来限制搜索空间。然而，束搜索无法提供任何优化的理论保证，这使得当前的解释与真正的最优点之间存在不确定性。
### Innovation
本文通过对束搜索方法的改进和提出新的分解方法与启发式算法，首次提出了可以计算保证最优化组合解释的框架。具体来说，它提出了：（i）影响空间对齐的因素分解，（ii）在搜索的任何阶段估计对齐度的方法，以及（iii）可以在合理时间内计算最优化组合解释的第一个算法。此外，还分析了束搜索在视觉领域和卷积神经网络中的最优和非最优解释差异，结果显示参与重叠概念时，通过束搜索获得的解释约有10-40%是非最优化的。
### Conclusion
通过引入的一种束搜索变体，由提出的分解方法和启发式算法来指导，提高了运行时性能并提供了更灵活的超参数和计算资源。
## 496. `cs.CV` - 使用傅里叶变换的分数变分谱滤波方法 [PDF](https://arxiv.org/pdf/2511.20675), [HTML](https://arxiv.org/abs/2511.20675)
### Authors
Nelson H. T. Lemes,José Claudinei Ferreira,Higor V. M. Ferreira
### Background
拉曼光谱分析中的荧光信号干扰和噪声问题依然显著，这常会导致重要的光谱特征被遮盖，影响分析的准确性。变分方法，类似于图像去噪的方法，通过最小化包含分数导数的功能来实现噪声抑制与关键化学特征保留的平衡。
### Innovation
本文创新地提出了一种结合变分方法与分数导数的滤波技术，通过傅里叶变换简化和加速实现过程；优化正则化参数和导数阶数并通过香农熵的概念实现。该方法能有效移除噪声，同时保留光谱和图像的关键特征。
### Conclusion
实验结果表明，提出的滤波策略组合能产生高效、稳健且易于实现的去噪滤波器，结合的分数阶与正则化参数对噪声去除和关键特征的保留有显著影响。
## 497. `cs.CV` - CHiQPM：校准的分层可解释图像分类 [PDF](https://arxiv.org/pdf/2511.20779), [HTML](https://arxiv.org/abs/2511.20779)
### Authors
Thomas Norrenbrock,Timo Kaiser,Sovan Biswas,Neslihan Kose,Ramesh Manuvinakurike,Bodo Rosenhahn
### Background
在全球可解释模型成为值得信赖的AI在关键安全领域中的有前途方法的同时，细致的局部解释对于有效支持人类专家在推理过程中的工作至关重要。本文的研究背景在于提高AI系统的透明度和可信度，使得人类专家能够更好地理解和信任AI的决策过程。
### Innovation
提出了Calibrated Hierarchical QPM (CHiQPM)，这种模型提供了全面的全局和局部解释能力，为人类与AI的互补性奠定了基础。CHiQPM通过对比方式解释大多数类别，实现了出色的全局解释性，并提供了更加符合人类推理方式的分层解释方法，同时也嵌入了一种可解释的同尺度预测（CP）方法。
### Conclusion
全面的评估显示，CHiQPM作为一个点预测器，其准确性达到最先进的水平，保持了99%与不可解释模型相当的准确性。此结果表明，解释性得到增强而整体准确性未受到影响。此外，CHiQPM的校准集合预测在效率上与其他CP方法竞争，同时提供了一种有解释性的、连贯的集合预测。
## 498. `cs.CV` - 无像素看见：从摄像机轨迹感知 [PDF](https://arxiv.org/pdf/2511.21681), [HTML](https://arxiv.org/abs/2511.21681)
### Authors
Zihui Xue,Kristen Grauman,Dima Damen,Andrew Zisserman,Tengda Han
### Background
本研究探索了在未看到视频像素的情况下，仅通过摄像机的运动轨迹是否能够感知视频内容的问题。此前，这一问题看似不可信，但本研究通过系统性地调查这一问题，发现摄像机运动轨迹其实是非常有效的信号，可以揭示视频内容。
### Innovation
本研究提出了一种对比学习框架，用于训练专门的编码器CamFormer，将摄像机姿态轨迹投影到联合嵌入空间中，并与自然语言对齐。研究结果显示，摄像机运动轨迹能够揭示视频内容，无论是第一人称视角还是第三人称视角。此外，研究展示了一种能够适应多种下游任务的嵌入表示的灵活性和鲁棒性，包括跨模态对齐、分类和时间分析任务。
### Conclusion
本研究确立了摄像机轨迹作为一种轻量、鲁棒且灵活的模态，可用于感知视频内容。无论是高精度多传感器估计还是标准的RGB-only估计，摄像机轨迹的表示都表现出了良好的鲁棒性。
## 499. `cs.CV` - Canvas-to-Image: 通过多模态控制进行构图图像生成 [PDF](https://arxiv.org/pdf/2511.21691), [HTML](https://arxiv.org/abs/2511.21691)
### Authors
Yusuf Dalva,Guocheng Gordon Qian,Maya Goldenberg,Tsai-Shien Chen,Kfir Aberman,Sergey Tulyakov,Pinar Yanardag,Kuan-Chieh Jackson Wang
### Background
虽然现代扩散模型在生成高质量和多样化图像方面表现出色，但在高保真度构成和多模态控制方面仍存在困难，特别是在用户同时指定文本提示、主题参考、空间布局、姿势约束和布局注释时。
### Innovation
提出了独一无二的Canvas-to-Image框架，将这些异质控制合并到一个画布界面中，使用户能够生成准确反映其意图的图像。关键思想是将多样性控制信号编码到单个组合画布图像中，该模型可以直接解释这些图像进行整合的视觉-空间推理。进一步创建了多任务数据集，并提出了一种多任务画布训练策略，以优化扩散模型在统一学习框架内理解和整合各种控制的应用于文本到图像生成。
### Conclusion
广泛的实验表明，Canvas-to-Image在身份保留和控制一致性方面明显优于最先进的方法，包括多人组合、姿势控制组合、布局约束生成以及多控制生成基准测试中的表现。
## 500. `cs.CV` - G$^2$VLM: 以几何为基础的统一3D重建和空间推理的视觉语言模型 [PDF](https://arxiv.org/pdf/2511.21688), [HTML](https://arxiv.org/abs/2511.21688)
### Authors
Wenbo Hu,Jingli Lin,Yilin Long,Yunlong Ran,Lihan Jiang,Yifan Wang,Chenming Zhu,Runsen Xu,Tai Wang,Jiangmiao Pang
### Background
视觉语言模型（VLMs）在空间智能方面缺乏稳健性，表现不佳。这主要是因为缺乏能够从2D图像重建3D空间的视觉几何学习过程。
### Innovation
提出了一种基于几何的视觉语言模型G$^2$VLM，结合了空间3D重建和空间理解这两个空间智能的基本方面。G$^2$VLM通过上下文学习和交错推理，利用学习到的3D视觉几何特性直接预测3D属性，增强空间推理任务，并且在大规模多视角图像和视频数据上进行训练，同时利用传统上仅由难以收集的标注提供的3D视觉先验。
### Conclusion
实验结果表明，G$^2$VLM在3D重建和空间理解任务上表现出色，超越或达到当前最先进的3D重建模型的性能。通过将语义较强的VLM与低级3D视觉任务结合起来，我们希望G$^2$VLM能成为社区的一个强大基准，并解锁更多未来应用，例如3D场景编辑。
## 501. `cs.CV` - Adversarial Multi-Task Learning for Liver Tumor Segmentation, Dynamic Enhancement Regression, and Classification [PDF](https://arxiv.org/pdf/2511.20793), [HTML](https://arxiv.org/abs/2511.20793)
### Authors
Xiaojiao Xiao,Qinmin Vivian Hu,Tae Hyun Kim,Guanghui Wang
### Background
肝肿瘤的分割、动态增强回归以及分类对于临床评估和诊断至关重要。但是，此前没有研究试图在一个端到端框架中同时完成这些任务，主要是因为缺乏有效的框架来捕捉任务间的相互相关性以实现互相提升，以及没有有效的机制来提取动态MRI信息。
### Innovation
该研究提出了一个新型集成框架——Multi-Task Interaction adversarial learning Network (MTI-Net)，该框架能够同时处理上述任务。MTI-Net 包含 Multi-domain Information Entropy Fusion (MdIEF)，该方法利用熵意识的高频谱信息，有效地在频域和谱域之间集成特征，增强了对动态MRI数据的提取和利用。此外，MTI-Net 导入了任务交互模块，建立了分割和回归之间的高层次一致性，从而促进相互任务的协同工作，并提高了整体性能。研究还设计了任务导向判别器 (TDD) 来捕捉任务间的内部高阶关系，并利用浅层Transformer网络对动态MRI信息进行编码。
### Conclusion
在包含238名受试者的数据集上，MTI-Net 在多个任务上的表现都很高，表明其在肝肿瘤临床评估中的强大力量。代码可在该网址下载：this https URL。
## 502. `cs.CV` - 使用自回归条件生成对抗网络的 wildfire 传播概率预测 [PDF](https://arxiv.org/pdf/2511.21019), [HTML](https://arxiv.org/abs/2511.21019)
### Authors
Taehoon Kang,Taeyong Kim
### Background
气候变化加剧了野火的频次和强度，这使得快速且准确预测野火蔓延变得至关重要。基于物理的模拟器如 FARSITE 提供高保真预测，但由于计算密集型，限制了其在实时决策中的应用。现有的深度学习模型往往产生过于平滑的预测，无法捕捉野火蔓延的复杂、非线性动态。本文探讨了使用自回归条件生成对抗网络 (CGAN) 进行野火蔓延概率预测。
### Innovation
本文提出了一种自回归条件生成对抗网络（CGAN）用于预测野火的不确定性。通过将预测任务视为自回归问题，该模型学习顺序状态转换，确保长期预测稳定性。实验结果表明，与传统的深度学习模型相比，基于CGAN的模型在总体预测准确性和火场边界界定方面表现出色。这证明了对抗学习可以捕捉野火传播的强大非线性和不确定性，而不仅仅是适应像素平均值。此外，自回归框架有助于系统的野火演进的时空预测。CGAN自回归框架提高了野火传播预测的准确性和物理可解释性，为时间敏感的响应和疏散规划提供了有希望的基础。
### Conclusion
基于CGAN的自回归框架提高了野火传播预测的准确性和物理可解释性，尽管相对计算需求较高，但仍较传统方法显示出优越性。
## 503. `cs.CV` - SocialNav: 基于人类启发的基础模型在社会意识导航中的训练 [PDF](https://arxiv.org/pdf/2511.21135), [HTML](https://arxiv.org/abs/2511.21135)
### Authors
Ziyi Chen,Yingnan Guo,Zedong Chu,Minghua Luo,Yanfen Shen,Mingchao Sun,Junjun Hu,Shichao Xie,Kuan Yang,Pei Shi,Zhining Gu,Lu Liu,Honglin Han,Xiaolong Wu,Mu Xu,Yu Zhang
### Background
社会规范指导下的肢体导航仍然是一个未解决的研究挑战。本文旨在开发一个能够同时理解高级社会规范并生成低层级、符合社会规范轨迹的核心模型。
### Innovation
本文提出了SocNav数据集，包含认知激活数据集和专家轨迹金字塔，是首个以社会意识为导向的肢体导航的基础模型。模型架构采用层次化的‘大脑-动作’设计，通过模仿学习和专门为肢体导航设计的社会意识流动探索强化学习框架（SAFE-GRPO）来进行多阶段训练。
### Conclusion
SocialNav相比现有最优方法在导航成功和社交合规性方面分别提高了38%和46%。
## 504. `cs.CV` - STAR：增强现实中的智能手机式打字 [PDF](https://arxiv.org/pdf/2511.21143), [HTML](https://arxiv.org/abs/2511.21143)
### Authors
Taejun Kim,Amy Karlson,Aakar Gupta,Tovi Grossman,Jason Wu,Parastoo Abtahi,Christopher Collins,Michael Glueck,Hemant Bhaskar Surale
### Background
在增强现实（AR）应用程序中，文本输入是一项基本且常见的任务，但开发一种高效且易于使用的AR文本输入方法仍然是一个开放的问题。
### Innovation
STAR 是一种基于智能手机双拇指打字的AR文本输入技术。用户可以在手部的虚拟QWERTY键盘上进行拇指打字。实验结果显示参与者在30分钟后平均打字速度为21.9 WPM（相当于智能手机打字速度的56%），错误率为0.3%。进一步分析了STAR和智能手机打字之间的表现差距的主要因素。
### Conclusion
研究讨论了如何缩小STAR与智能手机打字之间的差距，表明STAR作为一种无缝集成的手部虚拟键盘具有很大的潜力，能够提高AR环境下的文本输入效率。
## 505. `cs.CV` - 使用SDR的CNN-LSTM混合架构进行空中自动调制分类 [PDF](https://arxiv.org/pdf/2511.21040), [HTML](https://arxiv.org/abs/2511.21040)
### Authors
Dinanath Padhya,Krishna Acharya,Bipul Kumar Dahal,Dinesh Baniya Kshatri
### Background
自动调制分类（AMC）是未来无线通信系统的核心技术，能够无需先验知识地识别调制方案，这对于认知无线电、频谱监测和智能通信网络等应用至关重要。该技术用于在不同环境中实时分析无线信号，以适应不断变化的通信需求。
### Innovation
本文提出了一种基于混合卷积神经网络（CNN）和长短期记忆（LSTM）架构的AMC系统，并将其集成到软件定义无线电（SDR）平台中。该体系结构利用CNN进行空间特征提取，运用LSTM捕捉时间依赖性，以高效处理复杂的、时变的通信信号。通过实验验证了该系统的有效性，模型在杂信号条件下的性能尤为突出。
### Conclusion
研究结果表明，这种混合CNN-LSTM架构对于AMC的有效性得到了验证，并提出该架构在自适应频谱管理和先进认知无线电系统中的潜在应用前景。
## 506. `cs.CV` - ENACT: 使用基于自我中心交互的世界建模评估具身认知 [PDF](https://arxiv.org/pdf/2511.20937), [HTML](https://arxiv.org/abs/2511.20937)
### Authors
Qineng Wang,Wenlong Huang,Yu Zhou,Hang Yin,Tianwei Bao,Jianwen Lyu,Weiyu Liu,Ruohan Zhang,Jiajun Wu,Li Fei-Fei,Manling Li
### Background
具身认知认为，智能源自传感器网络活动的交互，而非被动观察。现代视觉-语言模型（VLMs）主要是以非具身的方式进行训练，它们是否表现出了具身认知的特征，这是个有趣的问题。为此，研究引入了ENACT基准，该基准将对具身认知的评估转化为基于自我中心交互的视觉问答（VQA）格式中的世界建模。将任务视为部分可观测马尔可夫决策过程（POMDP），其操作是场景图的变化。
### Innovation
ENACT基准基于部分可观测马尔可夫决策过程的框架提出，其包含两个互补的序列重排序任务：前向世界建模（根据操作重新排序打乱的观察）和逆向世界建模（根据观察重新排序打乱的操作）。反向任务解决了从部分可观测自我中心输入中隐含的需求，例如：执行功能、动作-效果推理、具身意识和交互的长期记忆，而避免了可能干扰评估的低级图像合成。
### Conclusion
实验结果显示，前沿视觉语言模型和人类之间的性能差距随着交互范围的增加而增大。模型在逆向任务中表现始终优于前向任务，并显示出以人类为中心的偏见，包括对右手动作的偏好以及当摄像机内参或视角偏离人类视角时性能下降。
## 507. `cs.CV` - OVOD-Agent：一种用于主动视觉推理和自我进化的马尔可夫-赌博机框架 [PDF](https://arxiv.org/pdf/2511.21064), [HTML](https://arxiv.org/abs/2511.21064)
### Authors
Chujie Wang,Jianyu Lu,Zhiyuan Luo,Xi Chen,Chu He
### Background
开放式词汇目标检测（OVOD）旨在通过利用语义信息使检测器能够跨类别泛化。尽管现有的方法是在大规模的视觉语言数据集上进行预训练，但它们的推理仍然局限于固定类别的名称，这在多模态训练和单模态推理之间造成了鸿沟。先前的工作表明，改进文本表示可以显著提高OVOD的性能，这表明文本空间仍有待探索。
### Innovation
提出了一种OVOD-Agent，它将被动类别匹配转变为积极的视觉推理和自我进化的检测。受链式思考（CoT）范式启发，OVOD-Agent将文本优化过程扩展为具有显式动作的可解释视觉-CoT。OVOD-Agent将视觉上下文转换建模为八个状态空间上的弱马尔可夫决策过程（w-MDP），自然地表示了代理的状态、记忆和交互动力学。还通过集成马尔可夫转移矩阵和赌博机轨迹，形成了从经验探索到RM训练的闭环，从而优化奖励模型（RM），增强了代理专注于不确定区域的能力，并使其能够适应检测策略。
### Conclusion
在COCO和LVIS上的实验表明，OVOD-Agent在各类检测器骨架上提供了持续的改进，尤其是对稀有类别的改进，验证了所提出框架的有效性。
## 508. `cs.CV` - 视觉对象姿态估计中的不确定性量化 [PDF](https://arxiv.org/pdf/2511.21666), [HTML](https://arxiv.org/abs/2511.21666)
### Authors
Lorenzo Shaikewitz,Charis Georgiou,Luca Carlone
### Background
姿态估计是机器人研究中的一个成熟问题，但在没有严格假设的情况下附加上统计严谨的不确定性分析并不被充分理解。该文关注在单目设置下，对于给定的姿态估计，定性描述对象姿态估计的不确定性量化。这种不确定性量化基于2D语义关键点的像素检测噪声的高概率边界。
### Innovation
该文的主要创新在于提出了一种叫做SLUE（S-Lemma Uncertainty Estimation）的方法，它是一种凸规划程序，能够将性质不确定性问题转化为单一椭球不确定性边界，该边界能够确保以高概率包含真实物体姿态。此外，该文还提出了一种基于平方和松弛层次结构的改进方法，以获得更紧的不确定性边界。
### Conclusion
SLUE在两个姿态估计数据集和一个实际的无人机跟踪场景中进行了验证，与之前的工作相比，它在平移边界上产生了显著较小的不确定性，并且姿态边界的不确定性也较为竞争。该研究成果发布在 https://github.com/...。
## 509. `cs.CV` - Deep Parameter Interpolation for Scalar Conditioning [PDF](https://arxiv.org/pdf/2511.21028), [HTML](https://arxiv.org/abs/2511.21028)
### Authors
Chicago Y. Park,Michael T. McCann,Cristina Garcia-Cardona,Brendt Wohlberg,Ulugbek S. Kamilov
### Background
近年来，深度生成模型，包括扩散模型和流匹配模型，通常使用单个神经网络学习时间或噪声级别的依赖向量场。然而，设计能够准确表示这种向量场的网络架构极具挑战性，因为网络必须结合高维向量（通常为图像）和标量信息，而当前的常见方法限制了架构的选择。
### Innovation
本文提出了深度参数插值（DPI），一种在现有深度神经网络架构中引入额外标量输入的方法。DPI 通过动态插值两个学习参数集来引入标量依赖性，无需额外的图像输入或将标量信息具体整合到网络组件中，是一种简单且架构无关的方法，用于在神经网络中添加标量依赖性。
### Conclusion
实验表明，该方法改善了去噪性能并提升了扩散和流匹配模型的样本质量，同时保持了与标准标量条件技术相当的计算效率。
## 510. `cs.CV` - 孟加拉语手势语言翻译：数据集创建挑战、基准测试和前景 [PDF](https://arxiv.org/pdf/2511.21533), [HTML](https://arxiv.org/abs/2511.21533)
### Authors
Husne Ara Rubaiyeat,Hasan Mahmud,Md Kamrul Hasan
### Background
孟加拉语手势语言（BdSLT）受到严重限制，主要由于该语言资源稀缺。建立标准的句子级别数据集对于为讲孟加拉语的聋哑人群体开发基于AI的辅助工具至关重要。
### Innovation
本文介绍了IsharaKhobor数据集及其两个子集，为研究者提供了资源。同时，本文还进行了数据集开发的挑战分析，并通过基于地标和RQE嵌入进行基准测试。还进行了词汇限制和数据集内规范化的一些消融试验，形成了两个新的数据集IsharaKhobor_small和IsharaKhobor_canonical_small。
### Conclusion
数据集目前可以在此网页[1]上公开获取。
## 511. `cs.CV` - ProtoPFormer: 在视觉变换器中集中于原型部分以实现可解释的图像识别 [PDF](https://arxiv.org/pdf/2208.10431), [HTML](https://arxiv.org/abs/2208.10431)
### Authors
Mengqi Xue,Qihan Huang,Haofei Zhang,Jingwen Hu,Jie Song,Mingli Song,Canghong Jin
### Background
Prototypical Part Network (ProtoPNet) 已经引起了广泛的关注，并且因其在解释性人工智能 (XAI) 中的自我解释特性促进了许多后续研究。但是，当直接将 ProtoPNet 应用于 Vision Transformer (ViT) 的结构中时，学到的原型会表现出一个“干扰”问题：它们有较高的概率被背景激活，而不是关注前景内容。基于Transformer的ProtoPNet强大的长周期依赖建模能力使其难以专注于原型部分，从而严重影响其内在解释性。
### Innovation
本文提出了Prototypical Part Transformer (ProtoPFormer)，一种适用于Vision Transformer (ViT) 用于可解释图像识别的原型方法。ProtoPFormer通过引入全局和局部原型来捕捉和强调目标的代表性整体和局部特征，依赖ViT的架构特性。全局原型提供了对象的总体视角，以引导局部原型集中于前景，消除背景干扰。此外，局部原型接受明确监督，专门关注各自的原型视觉部分，从而增强整体解释性。大量的实验表明，我们提出的全局和局部原型可以相互纠正并共同做出最终决策，从整体和局部视角明确且透明地解释决策过程。
### Conclusion
我们的实验结果证明，ProtoPFormer在全局和局部原型方面表现出更优的性能和可视化结果，相比现有的原型基线方法，整体表现更优。我们的代码已经在此网址发布：this https URL.
## 512. `cs.CV` - BanglaMM-Disaster: 一种基于多模态变换器的深度学习框架，用于孟加拉语多类灾难分类 [PDF](https://arxiv.org/pdf/2511.21364), [HTML](https://arxiv.org/abs/2511.21364)
### Authors
Ariful Islam,Md Rifat Hossen,Md. Mahmudul Arif,Abdullah Al Noman,Md Arifur Rahman
### Background
孟加拉国仍面临重大自然灾害挑战，因此需要实时监测和快速响应系统。本研究旨在通过结合社交媒体文本和视觉数据构建端到端的深度学习多模态框架，以提高灾害分类准确性。
### Innovation
提出了一种基于变换器的多模态框架，该框架使用文本和视觉数据对孟加拉语进行灾害分类。模型通过早期融合将变压器文本编码器（包括BanglaBERT、mBERT和XLM-RoBERTa）与CNN骨干网络（包括ResNet50、DenseNet169和MobileNetV2）相结合。提出的模型在所有类别中的误分类率降低，并在模糊示例中提高了识别精度。
### Conclusion
该研究填补了孟加拉语多模态灾害分析的关键空白，并证明了在资源有限的环境中对实时灾害响应同时使用多种数据类型的好处。
## 513. `cs.CV` - AV-Edit: 通过音频-视觉语义联合控制实现多模式生成音效编辑 [PDF](https://arxiv.org/pdf/2511.21146), [HTML](https://arxiv.org/abs/2511.21146)
### Authors
Xinyue Guo,Xiaoran Yang,Lipan Zhang,Jianxuan Yang,Zhao Wang,Jian Luan
### Background
现有的音效编辑方法受限于依靠低级别信号处理或粗略文本提示的技术，这使得音效编辑的灵活性和音频质量有限。
### Innovation
提出了一个生成式音效编辑框架AV-Edit，该框架通过联合利用视觉、音频和文本语义，实现对视频中现有音频轨道的精细编辑。具体包括：1. 设计了一个专门的对比音频-视觉掩蔽自动编码器（CAV-MAE-Edit）进行多模态预训练，学习对齐的跨模态表示；2. 利用这些表示训练了一个编辑多模态扩散变换器（MM-DiT），可以去除视觉无关的音频并根据视频内容生成缺失的音频元素，通过基于相关性特征门控的训练策略进行训练。
### Conclusion
实验表明，AV-Edit能够根据视觉内容生成高质量且精准修改的音频，其在音效编辑领域达到了最先进的性能，并在音频生成领域表现出强竞争力。
## 514. `cs.CV` - AerialMind：在无人机场景中迈向多目标参照跟踪 [PDF](https://arxiv.org/pdf/2511.21053), [HTML](https://arxiv.org/abs/2511.21053)
### Authors
Chenglizhao Chen,Shaofeng Liang,Runwei Guan,Xiaolou Sun,Haocheng Zhao,Haiyun Jiang,Tao Huang,Henghui Ding,Qing-Long Han
### Background
多目标参照跟踪（RMOT）旨在通过自然语言指令实现精确的物体检测和跟踪，是智能机器人系统的一项基本能力。然而，当前的RMOT研究主要局限于地面场景，这限制了其捕捉广泛场景语境和进行全面跟踪和路径规划的能力。相比之下，无人驾驶航空器（UAV）利用其广阔的空中视角和卓越的机动性，能够实现宽域监视。此外，UAV已成为体感智能的关键平台，催生了对能够进行自然语言交互的智能空中系统前所未有的需求。为此，我们引入了AerialMind，这是第一个面向UAV场景的大型尺度RMOT基准，旨在弥合这一研究缺口。
### Innovation
我们开发了创新的半自动协作代理标注助手（COALA）框架，显著降低了劳动成本同时保持了注释质量，并提出了HawkEyeTrack（HETrack），一种新的方法，协同增强视觉-语言表示学习，提高了对UAV场景的感知能力。
### Conclusion
全面的实验验证了我们数据集的挑战性以及我们方法的有效性。
## 515. `cs.CV` - 视觉变换器非单调扩增机制 [PDF](https://arxiv.org/pdf/2511.21635), [HTML](https://arxiv.org/abs/2511.21635)
### Authors
Anantha Padmanaban Krishna Kumar(Boston University)
### Background
深度视觉变换器通常表现不如浅层的，这挑战了常见的规模扩展假设。通过系统地分析ImageNet上ViT-S、ViT-B和ViT-L的表现，研究发现了一种一致的三阶段模式：悬崖阶段-平台阶段-攀登阶段，用于描述深度如何影响表示。研究表明，更好的性能与[CLS]标记逐渐被分布在补丁标记中的共识所取代相关，而[CLS]标记最初设计为全局聚合中心。
### Innovation
提出了信息乱序指数作为评估现有模型的诊断工具，并为未来架构的设计提供了一个潜在目标。研究指出，这种阶段过渡的信息扩散多于任务性能提升，这表明在这个范围内，变换器架构可能更受益于仔细调整的深度执行清晰的阶段转换，而不是仅仅增加参数量。
### Conclusion
研究结果表明，视觉变换器在这个区间可能更受益于仔细调整的深度实现清晰的阶段转换，而不是简单的参数量增加。信息乱序指数为现有模型提供了一个有用的诊断工具，并暗示了未来架构设计的一个潜在目标。
## 516. `cs.CV` - LTD: 低温度蒸馏在免梯度遮蔽的对抗训练中的应用 [PDF](https://arxiv.org/pdf/2111.02331), [HTML](https://arxiv.org/abs/2111.02331)
### Authors
Erh-Chung Chen,Che-Rung Lee
### Background
对抗训练是一种广泛采用的方法，用于增强神经网络模型对抗攻击的鲁棒性。然而，本研究指出，图像分类中的数据表示，具体地说是以独热标签形式表示数据，是导致模型脆弱的关键因素。在实际数据集中，数据的模糊性经常导致样本具有多个类别的属性，使得独热标签表示变得不精确。
### Innovation
提出了一种创新的方法：低温度蒸馏（LTD），旨在通过教师模型使用较低的温度来改进标签表示，而学生模型在训练和推理过程中保持固定温度，以避免传统的防御蒸馏中遇到的梯度遮蔽问题。这种方法不仅细化了对数据分布的假设，还增强了模型的鲁棒性。
### Conclusion
实验结果显示，当LTD方法与现有框架结合时，可以提高鲁棒准确性，分别在CIFAR-10、CIFAR-100和ImageNet数据集上达到58.19%、31.13%和42.08%的鲁棒准确率，无需额外的数据。
## 517. `cs.CV` - TraceGen：在3D轨迹空间中的世界建模使跨体态视频学习成为可能 [PDF](https://arxiv.org/pdf/2511.21690), [HTML](https://arxiv.org/abs/2511.21690)
### Authors
Seungjae Lee,Yoonkyo Jung,Inkook Chun,Yao-Chih Lee,Zikui Cai,Hongjia Huang,Aayush Talreja,Tan Dat Dao,Yongyuan Liang,Jia-Bin Huang,Furong Huang
### Background
从少量演示中在新平台上学习新机器人任务并在新环境中仍然具有挑战性。尽管其他体态（人类和不同机器人）的视频丰富，但由于体态、摄像头和环境差异，它们难以直接使用。本文通过提出一种统一、符号化的表示方式——场景级别的轨迹3D“轨迹空间”来解决小数据量问题，这个表示方式使得可以从跨体态、跨环境和跨任务视频中学习。
### Innovation
本文提出了TraceGen，一种预测轨迹空间中未来运动的世界模型，且不局限于像素空间，保留几何结构并在把握操控所需信息的同时抽象表象。为大规模训练TraceGen，开发了一种数据管道——TraceForge，将不同形式的机器人和人类视频转化为一致的3D轨迹。因此，获得了一个视频数据集，包含123000个视频和180万个观测-轨迹-语言三元组。在通过这个数据集预训练后，获得了在运动上的可迁移先验知识，可以有效适应：仅五个目标机器人视频，TraceGen就达80%的任务成功率，同时其推理速度比最新的视频基世界模型快50-600倍。
### Conclusion
在只有五段未校准的人类演示视频（手持手机拍摄）的情况下，TraceGen依然在实际机器人上获得了67.5%的成功率，这说明了TraceGen跨体态适应性，而无需依赖对象检测器或重量级的像素空间生成。
## 518. `cs.CV` - Activator: 将门控线性单元（GLU）激活函数作为视觉变压器的核心组件 [PDF](https://arxiv.org/pdf/2405.15953), [HTML](https://arxiv.org/abs/2405.15953)
### Authors
Abdullah Nazhat Abdullah,Tarkan Aydin
### Background
变压器架构已在深度学习的各种任务中取得巨大成功，尤其是在自然语言处理（NLP）领域，尤其是大型语言模型（LLM）的出现。这一架构也被计算机视觉（CV）研究者和从业者广泛应用，推动了视觉相关任务的进步，并开启了多任务和多模态深度学习架构的大门。然而，这些架构依赖于计算成本高昂的缩放点积注意机制和softmax激活函数。因此，该论文旨在探讨通过引入门控线性单元（GLU）激活函数结构的多层感知机（MLP）来替代传统的MLP和注意机制，从而减少计算复杂性。
### Innovation
论文提出了一种新的方法，通过将门控线性单元（GLU）激活函数结构引入到多层感知机（MLP）中，取代传统的方法，以减少计算复杂度。实验结果显示，基于GLU的修改设计提供了与选定基准架构竞争的性能。
### Conclusion
研究表明，基于GLU基MLP的设计能够提供更高效但同样有效的替代方案，用作传统MLP和注意机制的核心组件，在变压器架构的设计中能够达到显著的性能，同时降低了计算成本。
## 519. `cs.CV` - 针对基于潜在扩散模型的图像编辑的灰盒攻击：基于后验塌陷的攻击 [PDF](https://arxiv.org/pdf/2408.10901), [HTML](https://arxiv.org/abs/2408.10901)
### Authors
Zhongliang Guo,Chun Tong Lei,Lei Fang,Shuai Zhao,Yifei Qian,Jingyu Lin,Zeyu Wang,Cunjian Chen,Ognjen Arandjelović,Chun Pong Lau
### Background
最近在潜在扩散模型（LDMs）方面取得的进展彻底改变了图像的合成和编辑，但同时也引发了关于数据误用和知识产权侵犯的重大担忧。虽然已经广泛应用对抗性攻击作为防护措施来应对这种滥用，但当前的方法严重依赖于模型特定的知识并伴有重大的计算成本。本文受到了在变分自编码器（VAE）训练中观察到的后验塌陷现象的启发，提出了一种新的框架——后验塌陷攻击（PCA），用于保护图像免受未经授权的操控。
### Innovation
本文作者通过理论分析和实证验证，发现VAE推理过程中的两种不同的塌陷现象：扩散塌陷和聚集塌陷。基于此，他们设计了一种统一的损失函数，该函数可以通过参数调整灵活地实现两种类型的塌陷，每种都对应于阻止图像操控的不同保护目标。PCA方法通过仅需要访问VAE编码器来大幅减少对模型特定知识的依赖（VAE编码器仅占LDM参数的4%以下）。此外，PCA在文本条件处理之前操作VAE编码器，从而避免了现有方法所需的空提示优化，实现了生成提示不变性的保护。通过广泛的实验，证明PCA在防护效果、计算效率（运行时间和VRAM）以及对基于VAE的LDM变体的泛化方面优于现有技术。
### Conclusion
实验结果表明，PCA在防护效果、计算效率和各种基于VAE的LDM变体的一般化方面均优于现有技术。并且，我们的代码已公开发布。
## 520. `cs.CV` - 规模下稳定且具韵律的单码书TTS大规模语言模型的多奖励GRPO [PDF](https://arxiv.org/pdf/2511.21270), [HTML](https://arxiv.org/abs/2511.21270)
### Authors
Yicheng Zhong,Peiji Yang,Zhisheng Wang
### Background
大型语言模型（LLMs）的最新进展已经改变了文本到语音（TTS）合成，启发了自回归框架，将语音表示为离散编解码器令牌序列。其中，单码书TTS LLMs作为一种紧凑且可流式的架构，同时建模了语义和声学的融合。然而，尽管这些模型具有高效性，它们常常表现出不稳定的音调、说话人漂移和自然度下降的问题。
### Innovation
本文提出了一个基于组相对策略优化（GRPO）的多奖励框架，直接优化单码书TTS LLMs的令牌生成策略。除了标准的可理解性和说话人相似度目标，该设计还集成了三个基于规则的奖励：长度惩罚用于持续时间一致性，熵正则化奖励用于解码稳定性，以及由LLM注释的音调对齐奖励，明确监督了节奏。此外，本文通过附加流匹配（FM）解码器来评估其普适性，并发现该方法能够实现音调稳定、说话人相似性和整体语音自然度的提升。
### Conclusion
本文提出了一个基于组相对策略优化的多奖励框架，用于改进单码书TTS LLMs的稳定性与韵律。经过规模分析，该方法在数据大小和模型规模上表现一致，能够提升单码书TTS LLMs的音调稳定性、说话人相似性以及整体语音自然度。
## 521. `cs.CV` - 开放词汇量单目3D物体检测 [PDF](https://arxiv.org/pdf/2411.16833), [HTML](https://arxiv.org/abs/2411.16833)
### Authors
Jin Yao,Hao Gu,Xuweiyi Chen,Jiayun Wang,Zezhou Cheng
### Background
现有的3D物体检测器依赖于昂贵的传感器（如LiDAR）或需要多视角设置，并且通常局限于有限的类别范围内，这限制了它们的应用范围。新任务中存在两个关键挑战：一是缺乏3D边界框注释限制了训练通用模型的能力；二是现有数据集中存在的标签不足和语义模糊（例如，桌子 vs. 书桌），这阻碍了可靠的评估。
### Innovation
作者提出了有效的框架，通过整合预训练的2D和3D视觉基础模型来减少对3D监督的依赖，并设计了一种新的评估指标来缓解注释问题，这使得在零样本3D检测新型类别和已知类别中的检测方面达到了最先进的水平。
### Conclusion
作者希望他们的方法提供了一个强基准，并且他们的评估协议为未来的研究奠定了可靠的标准。
## 522. `cs.CV` - 基于微细交通仿真的一种简单的视觉交通信号控制框架 [PDF](https://arxiv.org/pdf/2403.06884), [HTML](https://arxiv.org/abs/2403.06884)
### Authors
Pan He,Quanyi Li,Xiaoyong Yuan,Bolei Zhou
### Background
交通信号控制（TSC）对于减少交通拥堵、改善交通流动、缩短闲置时间和减少CO2排放至关重要。传统的特征基础方法依赖于启发式和预定义特征，而在视觉观测基础上的方法则减少了对这些因素的依赖，为端到端的学习和优化交通信号提供了可能。因此，本文引入了一个基于视见的交通信号控制框架TrafficDojo，并将其与MetaDrive中的SUMO微细交通流集成，提出了一个多功能交通环境，用于分析和评估在不同交通条件下和情景下的交通信号控制器。
### Innovation
本文提出了一种基于视见的交通信号控制框架TrafficDojo，将微细交通流向3D驾驶模拟器MetaDrive集成，建立和对比了包括传统和强化学习（RL）在内的基础算法，展示了基于视见的交通信号控制设计和开发的可能性。
### Conclusion
本文的工作为基于视觉的交通信号控制设计和开发提供了启示，并为新的研究机会开启了大门。
## 523. `cs.CV` - 由扩散、行走和切割实现的无监督分割 [PDF](https://arxiv.org/pdf/2412.04678), [HTML](https://arxiv.org/abs/2412.04678)
### Authors
Daniela Ivanova,Marco Aversa,Paul Henderson,John Williamson
### Background
该研究提出了一个利用预训练的文本到图像扩散模型特征的无监督图像分割方法。受经典光谱聚类方法的启发，该方法从图像片段的自注意力层构建邻接矩阵，并递归分割使用规范切分数（N.Cuts）。研究表明，自注意力的概率分布能够捕捉片段间的语义关系，并且可以解释为在图像上执行随机行走的转移矩阵。
### Innovation
该研究的核心创新在于利用随机行走规范切分数直接对自注意力激活进行分割，从而最小化簇间的转换概率，同时最大化簇内的一致性。该方法通过递归应用这一过程实现了反映预训练注意力层丰富语义的层次分割，无需额外训练。此外，研究还探索了从特征构建NCuts邻接矩阵的其他方法，以及如何利用自注意力的随机行走解释来捕捉跨片段的长距离关系。提出的自动确定NCut成本标准的方法避免了手动调整所需的过程。
### Conclusion
该研究表明，该方法在零样本无监督分割中超越了所有现有方法，并在COCO-Stuff-27和Cityscapes数据集上实现了最先进结果。通过定量分析不同特征的影响、常量与动态NCut阈值以及在构建NCuts邻接矩阵时引入多节点路径的影响，证实了该方法的有效性。
## 524. `cs.CV` - 通过利用合成数据进行交互式遮挡边界估计 [PDF](https://arxiv.org/pdf/2408.15038), [HTML](https://arxiv.org/abs/2408.15038)
### Authors
Lintao Xu,Chaohui Wang
### Background
遮挡边界（OBs）在2D图像中几何定位遮挡事件，并为场景理解提供关键线索。已有研究主要关注交互式分割方法，但缺乏系统研究交互式遮挡边界估计（IOBE）的方法和模型。
### Innovation
本文提出了一个多画笔引导的深度学习框架MS³PE，该框架通过两个创新点推动IOBE：（1）直观的多画笔交互机制；（2）增强多尺度条带卷积的3编码路径网络。此外，还提出了使用合成数据训练IOBE模型的方法，并开发了Mesh2OB工具，用于从3D场景生成精确的遮挡边界（OB）的地面真实值，解决了人工标注真实数据稀缺的问题。
### Conclusion
MS³PE模型超过了七种最先进的交互式分割方法的适应基线，展示了构建遮挡边界基准的强大潜力。还提出了OB-LIGM，这是一个高质量的现实世界基准，包含120张精细标注的高分辨率图像，推进了遮挡边界研究的评估标准。提供的资源包括代码和资源可访问于此链接：this https URL.
## 525. `cs.CV` - Active Negative Loss：噪声标签学习的鲁棒框架 [PDF](https://arxiv.org/pdf/2412.02373), [HTML](https://arxiv.org/abs/2412.02373)
### Authors
Xichen Ye,Yifan Wu,Yiqi Wang,Xiaoqiang Li,Weizhong Zhang,Yifan Chen
### Background
深度监督学习在各种任务中取得了显著的成功，但在面对嘈杂标签时容易出现过拟合问题。尽管已有的噪声鲁棒损失函数能够有效提升在这种环境下的学习效果，但现有方法，如近期提出的主动被动损失（APL），仍然存在一些局限性，特别是其被动损失函数（MAE）未能区分干净和嘈杂样本，这降低了训练效率，特别是在大规模数据集上。
### Innovation
该研究引入了一个新型的损失函数类——规范化负损失函数（NNLFs），作为APL框架中的被动损失函数，通过主要关注记忆中的干净样本来解决MAE的局限性。研究还提出了一种基于熵的正则化技术来缓解不平衡标签在非对称噪声环境中的脆弱性。此外，提出了新的框架——主动负损失（ANL），在使用噪声标签的图像分割任务中展现出或与现有最佳方法相当或更好的性能。
### Conclusion
广泛的实验证明了我们的ANL框架所采用的新损失函数在各种噪声类型和图像分割任务中可以实现更好的或可比的性能。相关源代码已公开。
## 526. `cs.CV` - 使用贝叶斯神经网络解决图像增强中的一对一到多对多映射问题 [PDF](https://arxiv.org/pdf/2501.14265), [HTML](https://arxiv.org/abs/2501.14265)
### Authors
Guoxi Huang,Qirui Yang,Ruirui Lin,Zipeng Qi,David Bull,Nantheera Anantrasirichai
### Background
在低光照和水下图像增强等任务中，由于动态摄影条件，退化图像可以对应多个可能的目标图像。这自然会产生一个一对一到多对多的映射问题。
### Innovation
提出了一种贝叶斯增强模型（BEM），该模型结合了贝叶斯神经网络（BNNs）来捕捉数据不确定性并产生多样化的输出。引入了一种BNN-DNN框架：首先使用BNN在低维空间中建模一对一到多对多的映射，然后通过一个确定性神经网络（DNN）进一步细化图像细节。
### Conclusion
在多个低光照和水下图像增强基准上的广泛实验表明了我们方法的有效性。
## 527. `cs.CV` - 使用SAM获取区域可区分先验的面向恢复的视频帧插值 [PDF](https://arxiv.org/pdf/2312.15868), [HTML](https://arxiv.org/abs/2312.15868)
### Authors
Yan Han,Xiaogang Xu,Yingqi Lin,Jiafei Wu,Zhe Liu,Ming-Hsuan Yang
### Background
现有的基于恢复的视频帧插值（VFI）方法中，相邻帧之间的运动估计起到了关键作用。然而，现有的方法在运动估计的准确性上仍存在挑战，主要是由于在相邻帧中识别对应的区域进行插值时的固有模糊性。
### Innovation
提出了一种新的解决方案，利用开放世界的分割模型（如SAM2）对帧进行分割，以获取在不同帧中的区域可区分先验（RDPs）。RDPs以空间变化的高斯混合形式表示，能够在保持统一模态的情况下区分任意数量的区域。同时，设计了带有RDP的插值编码器的层级区域感知特征融合模块（HRFFM），通过RDP指导下的特征规范化（RDPFN）提高编码器各层级的特征表示，从而提升相邻帧中匹配区域的特征表现，改善中间帧的合成。
### Conclusion
大量的实验表明，提出了的HRFFM模块能够提升视频帧插值的性能，尤其是在多场景的测试中，表现尤为显著。
## 528. `cs.CV` - AMLP: 可调节缺损补丁蒙版用于自监督医学图像分割 [PDF](https://arxiv.org/pdf/2309.04312), [HTML](https://arxiv.org/abs/2309.04312)
### Authors
Xiangtao Wang,Ruizhi Wang,Thomas Lukasiewicz,Zhenghua Xu
### Background
自监督掩蔽图像建模（MIM）方法在分析自然图像方面表现出色，但直接应用于医学图像分割任务尚未取得令人满意的结果。医学图像本身比自然图像复杂，医学图像中的主体具有更明显的轮廓特征。此外，传统的高且固定的MIM掩蔽比导致背景被掩蔽，限制了可学习的信息范围。
### Innovation
提出了一种新型自监督医学图像分割框架，称为可调节缺损补丁蒙版（AMLP），利用掩蔽补丁选择（MPS）策略识别高概率包含病变的补丁，以帮助模型实现准确的病变重建。通过引入相对重建损失（RRL）改善补丁分类，进一步提出类别一致性损失（CCL）基于重建难度细化补丁分类，增强病变与背景之间的差异。还提出了一种可调节掩蔽比（AMR）策略，逐步增加掩蔽比以扩大可学习的互信息范围。
### Conclusion
在两个医学分割数据集上的广泛实验表明，提出的AMLP方法在自监督方法中表现最佳；结果证明，AMLP有效地解决了将掩蔽模型应用于医学图像以及准确捕捉病变细节的问题，这对分割任务至关重要。
## 529. `cs.CV` - SOAP: 提升稀少样本动作识别中空-时关系及运动信息捕捉 [PDF](https://arxiv.org/pdf/2407.16344), [HTML](https://arxiv.org/abs/2407.16344)
### Authors
Wenbo Huang,Jinghui Zhang,Xuwei Qian,Zhen Wu,Meng Wang,Lei Zhang
### Background
高帧率（HFR）动作识别视频虽然能增强细粒度表达，但仍会减少空-时关系和运动信息密度。因此，传统数据驱动训练需要大量的视频样本。然而，在现实场景中，样本并不总是充足，这促进了稀少样本动作识别（FSAR）的研究。大部分近期的FSAR工作通过在提取空间特征后进行时间对齐来建立视频样本的空-时关系，这切断了样本内的空间和时间特征，同时也通过相邻帧之间的窄角度捕捉运动信息，但未考虑其密度，导致对运动信息的捕捉不足。
### Innovation
本文提出了一种名叫Spatio-temporal frAme tuPle enhancer (SOAP)的新架构，该架构通过考虑不同特征通道之间的时间连接和特征的空-时关系，而不是简单的特征提取，来提升动作识别中的空-时关系和全方位的运动信息。具体的，SOAP-Net使用包含多帧的帧元组来捕获更丰富的运动信息，并结合不同帧数的帧元组进一步提供更广泛的视角。
### Conclusion
SOLE［SOAP-Net］在SthSthV2、Kinetics、UCF101和HMDB51等知名基准测试上的表现达到新的最佳水平。大量的实证评估证实了SOAP在竞争力、可插拔性、泛化能力和鲁棒性上的优势。
## 530. `cs.CV` - LASER: 唇部关键点辅助演讲者检测以增强鲁棒性 [PDF](https://arxiv.org/pdf/2501.11899), [HTML](https://arxiv.org/abs/2501.11899)
### Authors
Le Thien Phuc Nguyen,Zhuoran Yu,Yong Jae Lee
### Background
主动说话者检测（ASD）旨在识别复杂视觉场景中的说话者。人类自然依赖唇音同步，但现有ASD模型在唇部动作和音频不一致时往往会错误分类非说话状态。因此，需要一种方法来解决该问题。
### Innovation
提出了唇部关键点辅助说话者检测以增强鲁棒性（LASER），它在训练中明确地引入了唇部关键点来引导模型的注意力到与语音相关的区域。此外，引入了一个辅助一致性损失来对齐唇部意识和仅面部预测，从而在测试时无需使用关键点检测器来处理低分辨率或遮挡等问题。
### Conclusion
LASER 在多种基准测试中均优于现有模型，尤其在高噪声子集中，与 LoCoNet 和 TalkNet 相比，mAP 分别提高了 3.3 和 4.3 个百分点，展示了对现实世界声学挑战的强大抵御能力。
## 531. `cs.CV` - 室内导航辅助的自适应物体检测：实时算法的性能评估 [PDF](https://arxiv.org/pdf/2501.18444), [HTML](https://arxiv.org/abs/2501.18444)
### Authors
Abhinav Pratap,Sushant Kumar,Suchinton Chakravarty
### Background
本文探讨了为视障人士提供辅助技术所需的精确且高效的物体检测需求。研究在室内导航辅助的背景下评估了YOLO、SSD、Faster R-CNN和Mask R-CNN四种实时物体检测算法，使用室內物体检测数据集分析了检测准确性、处理速度和对室内环境的适应性。研究表明，在精确度和效率之间存在权衡，为实时辅助导航选择最优算法提供了见解。
### Innovation
本研究在自适应机器学习应用领域有所推进，提升了视障人士的室内导航解决方案，并促进了无障碍技术的发展。
### Conclusion
研究结果表明，必须在精确度和效率之间进行权衡，为实时辅助导航选择最合适的算法。这项研究有助于提升室内导航辅助技术的有效性和准确性，促进视障人员的自主导航能力。
## 532. `cs.CV` - 系统性评估与分割 Anything 模型在手术视频分析中的指导原则 [PDF](https://arxiv.org/pdf/2501.00525), [HTML](https://arxiv.org/abs/2501.00525)
### Authors
Cheng Yuan,Jian Jiang,Kunyi Yang,Lv Wu,Rui Wang,Zi Meng,Haonan Ping,Ziyu Xu,Yifan Zhou,Wanli Song,Hesheng Wang,Yueming Jin,Qi Dou,Yutong Ban
### Background
手术视频分割对于AI解读手术中的空间-时间动态至关重要，但模型性能受限于标注数据的不足。虽然SAM2预训练在自然视频上，提供了零样本手术分割的潜力，但在复杂手术环境中的应用（如组织变形和器械变化）仍需要进一步探索。该研究对SAM2在9个手术数据集（17种手术类型）中的零样本能力进行了全面评估。
### Innovation
首次全面评估了SAM2在9个手术数据集中的零样本能力，涵盖了腹腔镜、内窥镜和机器人手术程序。分析了不同提示（点、框、掩码）和微调（密集、稀疏）策略，以及在手术挑战下的鲁棒性和跨程序和解剖学的一般化能力。
### Conclusion
研究表明，虽然SAM2在结构化场景中展示了显著的零样本适应性（如器械分割、多器官分割和场景分割），但在动态手术条件下的性能存在差异，突显了处理时序一致性和领域特定伪影方面的不足。这些结果指出了手术数据科学领域适配的数据高效解决方案的未来研究路径。
## 533. `cs.CV` - 面向面部编辑的一致可控图像合成 [PDF](https://arxiv.org/pdf/2502.02465), [HTML](https://arxiv.org/abs/2502.02465)
### Authors
Mengting Wei,Tuomas Varanka,Yante Li,Xingxun Jiang,Huai-Qian Khor,Guoying Zhao
### Background
传统的面部编辑方法依赖于基于GAN的技术，而最近的研究转向了基于扩散模型的方法，因为它们在图像重建方面取得了成功。然而，扩散模型在控制特定属性和保持未更改属性（特别是身份特征）的一致性方面仍然面临挑战。
### Innovation
本文提出了一种名为RigFace的新方法，结合了稳定的扩散模型和粗略的3D面部模型来控制头像照片的照明、面部表情和头部姿态。该方法包括：1）一个空间属性编码器，提供背景、姿势、表情和照明的精确且解耦的条件；2）一种高一致性的FaceFusion方法，从身份编码器向预训练的扩散模型的去噪UNet转移身份特征；3）一个属性号角，将这些条件注入到去噪UNet中。模型在身份保留和真实的光质量方面与现有的面部编辑模型相比取得了相当甚至更优秀的表现。
### Conclusion
我们的研究实现了一种既能保持身份又能提高逼真度的面部编辑方法，为面部编辑任务提供了更方便的编辑工具。
## 534. `cs.CV` - Gen-3Diffusion: 通过2D和3D扩散协同实现基于图像的真实感3D生成 [PDF](https://arxiv.org/pdf/2412.06698), [HTML](https://arxiv.org/abs/2412.06698)
### Authors
Yuxuan Xue,Xianghui Xie,Riccardo Marin,Gerard Pons-Moll
### Background
从单张RGB图像创建逼真的3D对象和穿着虚拟角色是一项有吸引力但极具挑战性的问题。由于问题的本质是病态的，最近的研究工作利用预训练在大规模数据集上的2D扩散模型的强大先验知识。尽管2D扩散模型展示了强大的泛化能力，但它们不能保证生成的多视角图像在3D上是一致的。
### Innovation
本文提出了Gen-3Diffusion：通过2D和3D扩散协同实现真实感图像到3D生成。该方法利用预训练的2D扩散模型和3D扩散模型，通过我们的优雅设计过程，在训练和采样时同步这两个扩散模型。2D和3D扩散模型的协同带来了两个主要优势：1) 2D帮助3D泛化能力提升：预训练的2D模型具有强大的泛化能力，提供给3D扩散模型强烈的形状先验；2) 3D帮助2D在多视角一致性上的提升：3D扩散模型增强了2D多视角采样过程的3D一致性，从而产生更准确的多视角生成。
### Conclusion
通过广泛的实验验证了我们的想法，在基于图像的物体和穿着虚拟角色生成任务中，我们的方法生成了高保真度几何和纹理的逼真3D对象和虚拟角色。广泛的消融实验也验证了我们的设计选择，并展示了对多样化服装和构型形状的强大泛化能力。我们的代码和预训练模型将在此链接公开：this https URL
## 535. `cs.CV` - RobustMerge: 参数高效模型融合方法在具有方向稳健性的大规模语言模型中的应用 [PDF](https://arxiv.org/pdf/2502.17159), [HTML](https://arxiv.org/abs/2502.17159)
### Authors
Fanhu Zeng,Haiyang Guo,Fei Zhu,Li Shen,Hao Tang
### Background
通过使用自定义数据微调预训练模型，产生针对特定任务的专家模型变得普遍。将多个模型合并为一个通用模型，以促进多任务能力并避免数据泄露也越来越受欢迎。然而，随着数据和模型规模的扩大，参数高效微调已成为获得特定任务模型的有效方法。但有效合并方法的发展较慢，现有的设计用于整体微调合并的方法在高效融合时并不适用。
### Innovation
本文从低秩分解的角度分析了模型合并的问题，并提出了RobustMerge方法，这是一种无需训练的参数高效合并方法，具有互补参数调整以保持方向稳健性。该方法通过从参数间关系剪枝参数并缩放系数来保持奇异值方向的稳定性，并通过跨任务归一化增强未见过任务的一般化。
### Conclusion
研究人员建立了一个包含多种多模态任务的基准，并进行实验以证明RobustMerge方法的卓越性能和普适性。此外，进行了附加研究和广泛分析进一步展示了该方法的有效性。代码可在以下链接获取：https://github.com/robu Merge/RobustMerge。
## 536. `cs.CV` - PointNSP：基于下一尺度级别的细节预测自动化回归3D点云生成 [PDF](https://arxiv.org/pdf/2503.08594), [HTML](https://arxiv.org/abs/2503.08594)
### Authors
Ziqiao Meng,Qichao Wang,Zhiyang Dou,Zixing Song,Zhipeng Zhou,Irwin King,Peilin Zhao
### Background
在点云生成方面，与基于扩散的方法相比，基于自回归的模型长期以来在质量上落后。性能差距源于自回归模型对原本无序的点集施加的人工顺序限制，导致形状生成仅能作为局部预测序列实现。这种顺序偏差虽然强调了局部连续性，但削弱了模型捕获长距离依赖的能力，妨碍了对全局结构属性如对称性、一致拓扑和大规模几何规则性的约束。
### Innovation
基于形状建模中的细节级别（LOD）原则，我们提出了PointNSP，这是一种自底向上的生成框架，在低分辨率下保留全局形状结构，并通过下一代预测范式逐级细化细粒度几何。这种多尺度分解将自回归目标与点集的置换不变性质对齐，促进了丰富的同尺度交互，同时避免了固定的脆弱顺序。
### Conclusion
实验证明，PointNSP首次在自回归框架内实现了最佳生成质量。此外，PointNSP在参数、训练和推理效率方面超越了强大的基于扩散的基线方法。在高密度生成8,192个点时，其优势尤为明显，展示了其扩展潜力。
## 537. `cs.CV` - 从单张运动模糊图像中估计相机运动：图像作为IMU [PDF](https://arxiv.org/pdf/2503.17358), [HTML](https://arxiv.org/abs/2503.17358)
### Authors
Jerred Chen,Ronald Clark
### Background
在很多机器人和VR/AR应用中，快速的相机运动会产生较高的运动模糊，这使得现有的相机位姿估计方法失效。现有方法通常将运动模糊视为不需要的副作用，没有充分利用这类信息。
### Innovation
本文提出一种新颖的框架，通过预测稠密的运动流场和单一运动模糊图像的一目测深度图，来利用运动模糊作为一种丰富的运动估计线索，而不是将其视为副作用。该方法能够在小运动假设下通过求解线性最小二乘问题来恢复瞬时相机速度，从而生成类似IMU的测量值，能稳健捕捉快速和激烈的相机运动。
### Conclusion
通过在ScanNet++v2上构建大量现实合成运动模糊的数据集，以及使用完全可微的管道进行端到端训练，该方法在真实世界基准上的广泛评估表明，其角速度和线性速度估计比当前方法如MASt3R和COLMAP表现更为出色。
## 538. `cs.CV` - OuroMamba：视觉Mamba模型无数据量化框架 [PDF](https://arxiv.org/pdf/2503.10959), [HTML](https://arxiv.org/abs/2503.10959)
### Authors
Akshat Ramachandran,Mingyu Lee,Huan Xu,Souvik Kundu,Tushar Krishna
### Background
在量化视觉Mamba模型（VMMs）时，存在着两个关键挑战：(1) VMM的循环状态转移限制了长程交互的捕捉，并导致了语义较弱的合成数据；(2) VMM的激活表现为时间步长间动态异常值的变化，使得现有的静态后训练量化（PTQ）技术无效。
### Innovation
OuroMamba提供了两个阶段的框架：第一阶段OuroMamba-Gen通过基于邻域交互在潜在状态空间生成补丁级别的VMM特征，并运用对比学习生成语义丰富且有意义的合成数据；第二阶段OuroMamba-Quant利用轻量级动态异常值检测和混合精度量化。此外，我们提出了一种基于阈值的激活通道选择策略，该策略会根据时间步长更新。
### Conclusion
通过在视觉和生成任务上进行广泛实验，OuroMamba在多种量化设置下超越了现有的基于数据的PTQ技术，取得了领先的表现，并实现了至高2.36倍的GPU推理延迟速度提升。我们的代码和合成数据集已开源。
## 539. `cs.CV` - Filter Like You Test: 数据驱动的数据过滤用于CLIP预训练 [PDF](https://arxiv.org/pdf/2503.08805), [HTML](https://arxiv.org/abs/2503.08805)
### Authors
Mikey Shechter,Yair Carmon
### Background
背景介绍了用于视觉语言数据集的过滤算法，这些数据集的规模很大。现有的预训练方法通常使用大量的数据点进行训练，但在选择这些数据点时缺乏有效的过滤方法来确保数据的质量和多样性。FloydHub的CLIP模型提议使用某种过滤策略来筛选预训练数据集，这增强了模型在特定任务上的表现。
### Innovation
创新点在于提出了FLYT算法，这是一种用于大规模视觉语言数据集的过滤算法。FLYT通过一个评分模型学习每个数据点作为预训练示例的价值，并根据下游任务的梯度信号调整每个示例的权重。FLYT进一步开发了M-FLYT（混合FLYT），利用不同评分方法生成的每个示例的分数，学习统一成单一的评分。此外，通过Soft Cap Sampling（SCS）策略，FLYT自然生成的数据分布被用来生成过滤后的预训练数据集，该策略通过重复惩罚防止了数据的过量代表。
### Conclusion
结论表示，通过这些方法，研究成果在DataComp中获得了40.1%的ImageNet零样本准确率，超过了之前的全部结果2%，而且相比其他仅使用公共资源的方法提高了5.5%。此外，平均而言，在38个DataComp评估任务中，该方法取得了37.7%的结果，超过了之前使用公开资源的方法，提高了0.4%。这表明这种数据驱动的数据过滤方法对于CLIP预训练效果显著。
## 540. `cs.CV` - 从少量标签到开放域：用于无人机视图地理定位的高效学习方法 [PDF](https://arxiv.org/pdf/2503.07520), [HTML](https://arxiv.org/abs/2503.07520)
### Authors
Zhongwei Chen,Zhao-Xu Yang,Hai-Jun Rong,Jiawei Lang,Guoqi Li
### Background
传统的基于监督的无人机视图地理定位（DVGL）方法依赖于配对训练数据，难以从未配对数据中学习视图间的相关性。当这些方法应用于新领域时，需要收集新的配对数据并重新训练模型，这显著增加了计算开销。现有的无监督方法能够生成基于视图间相似性的伪标签，但地理相似性和空间连续性往往导致在同一地理位置具有视觉相似性的特征混淆，影响伪标签生成的可靠性，从而导致优化过程中的负面影响。
### Innovation
本文提出了一个带有有限监督的新型跨域不变知识传输网络（CDIKTNet），其架构包括跨域不变子网络（CDIS）和跨域传输子网络（CDTS）。该架构为不变特征学习和知识传输建立了一个闭环框架。CDIS设计用于从小量配对数据中学习视图间的空间和结构不变性，这些配对数据作为先验知识。它在初始化时赋予未配对数据的共享特征空间具有类似的显式跨视图关联，从而缓解特征混淆。基于此，CDTS使用双路径对比学习进一步优化每个特征子空间，同时在其共享特征空间中保持一致性。
### Conclusion
大量实验表明，与现有监督方法相比，CDIKTNet在全监督下实现了最先进的性能，并且在少量样本和跨域初始化下进一步超越现有的无监督方法。
## 541. `cs.CV` - 利用对比信息实现高效的文档阴影去除 [PDF](https://arxiv.org/pdf/2504.00385), [HTML](https://arxiv.org/abs/2504.00385)
### Authors
Yifan Liu,Jiancheng Huang,Na Liu,Mingfu Yan,Yi Huang,Shifeng Chen
### Background
文档阴影是数字化过程中的主要障碍。由于文件中的密集信息和被阴影覆盖的图案，文档阴影去除需要专门的方法。尽管现有的文档阴影去除方法取得了一些进展，但它们仍然依赖额外的信息（如阴影遮罩）或未能在不同阴影场景中取得普遍性和有效性，这经常会导致阴影去除不完整或原始文档内容和色调丢失。此外，这些方法往往没有充分利用原始带有阴影的文档图像中的信息。
### Innovation
本文专注于文档图像本身，结合对比表示法，提出了一种端到端的文档阴影去除方法，采用自底向上的精细调整方法。通过提取文档对比信息，可以有效地快速定位阴影形状和位置，无需额外的遮罩。这种信息被整合到精细的阴影去除过程中，为基于网络的去除和特征融合提供了更好的指导。广泛的质量和量化实验表明，我们的方法在性能上达到了最新技术水平。
### Conclusion
通过对比信息的利用，我们的方法在文档阴影去除上取得了最先进的性能，能够有效快速地去除阴影，同时保留原始文档的内容和色调。
## 542. `cs.CV` - CAPability: 一个评估视觉生成标注准确性和详尽性的全面视觉生成基准 [PDF](https://arxiv.org/pdf/2502.14914), [HTML](https://arxiv.org/abs/2502.14914)
### Authors
Zhihang Liu,Chen-Wei Xie,Bin Wen,Feiwu Yu,Jixuan Chen,Pandeng Li,Boqiang Zhang,Nianzu Yang,Yinglu Li,Zuan Gao,Yun Zheng,Hongtao Xie
### Background
随着现代多模态大语言模型（MLLMs）的出现，视觉讲图基准已经过时，因为简短的地面真实句子和传统评估指标无法有效评估详细的描述。尽管最近的基准试图通过关注关键词提取或以对象为中心的评估来解决问题，但它们仍然局限于模糊视图或对象视图的分析，并且无法全面覆盖视觉元素。
### Innovation
本研究引入了CAPability，这是一种面向12个维度的综合多视角基准，涵盖了六个关键视图，用于评估视觉生成的准确性与详尽性。同时还创新性地将注释转化为问答对，引入了一个启发式指标——'知道但不能说'（$Kbar{T}$），用于衡量问答能力和描述生成能力之间的性能差距。
### Conclusion
我们的工作为MLLMs的描述生成能力提供了全面分析，通过识别其在各个维度的优势和劣势，指导未来研究提升其特定方面的能力。
## 543. `cs.CV` - 无需配对标注数据：端到端自监督学习在无人机视角地理定位中的应用 [PDF](https://arxiv.org/pdf/2502.11381), [HTML](https://arxiv.org/abs/2502.11381)
### Authors
Zhongwei Chen,Zhao-Xu Yang,Hai-Jun Rong,Guoqi Li
### Background
无人机视图地理定位（DVGL）旨在通过检索带有GPS标签的卫星图像来实现无人机的精确定位。然而，现有的大多数方法高度依赖严格的预配对的无人机-卫星图像进行监督学习。当目标区域发生变化时，通常需要新的配对样本来适应分布变化。这些方法的标注成本高且转移性差，严重影响了DVGL在开放世界场景中的实际部署。
### Innovation
我们提出了一种新的端到端自监督学习方法，名为动态记忆驱动和邻域信息学习（DMNIL）方法。该方法采用了一种基于浅层骨干网络的双路径对比学习框架，利用聚类算法生成伪标签。DMNIL还包含两个核心模块：动态层次记忆学习模块（DHML）和信息一致性进化学习模块（ICEL）。DHML结合短时和长时记忆，增强影像内部特征的稳定性和区分度；ICEL模块利用以邻近为驱动的动态约束机制系统地捕捉跨视图隐含的语义关联，从而提高跨视图特征对齐。此外，还提出了一种伪标签增强策略以优化自监督训练过程。实验验证了该方法在三个公开基准数据集上的优越性，不仅超过现有的自监督方法，甚至超越了一些最先进的人工监督方法。
### Conclusion
大量实验表明，所提出的方法在三个公开基准数据集上的表现优于现有自监督方法，并且在某些情况下超过了部分最先进的监督方法。
## 544. `cs.CV` - 类独立增量：一种高效的多标签类增量学习方法 [PDF](https://arxiv.org/pdf/2503.00515), [HTML](https://arxiv.org/abs/2503.00515)
### Authors
Chenhao Ding,Songlin Dong,Zhengdong Zhou,Jizhou Han,Qiang Wang,Yuhang He,Yihong Gong
### Background
当前类增量学习的研究主要集中在单标签分类任务上。然而，实际应用常常涉及到多标签场景，例如图像检索和医学影像。因此，本文关注具有挑战性但非常实际的多标签类增量学习（MLCIL）问题。除了灾难性遗忘等挑战外，MLCIL还面临特征混淆的问题，包括会话间和会内特征混淆。
### Innovation
本文提出了一个名为类独立增量（CLIN）的新型MLCIL方法。具体地，不同于现有的方法仅提取图像级特征，本文提出了一种类独立增量网络（CINet），用于提取多标签样本的多个类级嵌入。通过构建特定于类别的标记，该方法学习并保留不同类别的知识。在此基础上，我们提出了两种新的损失函数，分别优化特定于类别的标记学习和类级嵌入的学习，旨在区分新旧类别，进一步缓解特征混淆的问题。
### Conclusion
在MS-COCO和PASCAL VOC数据集上的实验表明，该方法能够有效提高识别性能并缓解各种MLCIL任务中的遗忘问题。
## 545. `cs.CV` - FlowTok: 在文本和图像标记之间无缝流动 [PDF](https://arxiv.org/pdf/2503.10772), [HTML](https://arxiv.org/abs/2503.10772)
### Authors
Ju He,Qihang Yu,Qihao Liu,Liang-Chieh Chen
### Background
跨模态生成的核心在于不同模态之间的桥梁构建。传统的生成方法将文本模态作为引导信号，从高斯噪声逐步引导到目标图像模态。本文探讨了一种更为直接的方法，通过流匹配直接在文本和图像模态之间演化。
### Innovation
提出了FlowTok框架，通过将图像编码为紧凑的1D标记表示，在文本和图像之间无缝流动。与先前方法相比，该设计减少了框架的潜在空间大小，简化了条件机制，并且可以在相同形式上自然扩展到图像到文本的生成。此外，该框架具有简化的架构，中心为紧凑的1D标记，实现了更高的内存效率、更少的训练资源需求和更快的取样速度，同时与最先进的模型具有相当的性能。
### Conclusion
FlowTok通过编码图像为紧凑的1D标记表示，在文本和图像之间实现了无缝流动，减少了潜在空间大小，并简化了条件机制，验证了其在跨模态生成中的高效性和可行性。
## 546. `cs.CV` - Adaptive对比扰动下的解纠缠几何对齐及其在可靠域适配中的应用 [PDF](https://arxiv.org/pdf/2505.15241), [HTML](https://arxiv.org/abs/2505.15241)
### Authors
Emma Collins,Myungseo wong,Kim Yun,Finn Kingston,Hana Satou
### Background
尽管在几何感知领域适应方面取得了一定进展，目前的方法如GAMA仍然存在两种未解决的问题：(1) 任务相关信息和任务无关信息之间的几何结构维度未能充分解耦；(2) 刚性扰动策略忽视了类间对齐差异性。
### Innovation
我们提出了一种名为GAMA++的新框架，它引入了(i)潜在空间解耦，以隔离与标签一致的流形方向和噪声因素；(ii)自适应对比扰动策略，以适应性地探索与目标流形相关的特征。我们还提出了一种跨域对比一致性损失，以鼓励局部语义聚类对齐同时保留域内多样性。
### Conclusion
GAMA++在DomainNet、Office-Home和VisDA基准测试（包括标准和少样本设置）中取得了最先进的结果，特别是在类别级别对齐精度和边界鲁棒性方面有了显著提高。该方法为迁移学习中的语义几何对齐设定了新的标准。
## 547. `cs.CV` - 地球适配器：通过频率混合适配弥合地理空间域间差距 [PDF](https://arxiv.org/pdf/2504.06220), [HTML](https://arxiv.org/abs/2504.06220)
### Authors
Xiaoxing Hu,Ziyang Gong,Yupei Wang,Yuru Jia,Fei Lin,Dexiang Gao,Ke An,Jianhong Han,Zhuoran Sun,Gen Luo,Gen Luo,Xue Yang
### Background
参数高效微调（PEFT）技术能够使强大的基础模型适应各种下游任务，同时保留和发挥其固有功能。然而，现有的PEFT方法在遥感（RS）场景下表现不佳，主要是因为它们难以处理图像中的伪影影响，这类影响在遥感图像特征中尤为严重。
### Innovation
本文提出了地球适配器（Earth-Adapter），这是首个专门为处理RS伪影而设计的PEFT方法。Earth-Adapter引入了新颖的频率混合适配过程，结合混合适配器（MoA）和离散傅里叶变换（DFT），通过DFT分解特征到不同频率组件，精准分离伪影与原始特征。MoA动态分配各个适配器专家的权重，实现跨多种频率域的特征组合。这些简单而有效的技术方法使Earth-Adapter能够更高效地克服伪影引起的干扰，显著提升了基础模型在RS场景中的性能。
### Conclusion
在域适应（DA）和域泛化（DG）语义分割基准测试中，地球适配器取得了显著效果。与基线方法相比，地球适配器在DA基准测试中提高了9.0%的mIoU，在DG基准测试中提高了3.1%的mIoU。代码将在指定的链接处发布。
## 548. `cs.CV` - 力提示：视频生成模型能学习和泛化基于物理的控制信号 [PDF](https://arxiv.org/pdf/2505.19386), [HTML](https://arxiv.org/abs/2505.19386)
### Authors
Nate Gillman,Charles Herrmann,Michael Freeman,Daksh Aggarwal,Evan Luo,Deqing Sun,Chen Sun
### Background
最近视频生成模型的研究激发了对能够模拟真实环境的物理世界模型的兴趣。尽管导航已经被广泛研究，但能够模仿现实世界力的物理有意义的交互仍处于起步阶段。
### Innovation
本文提出了一种使用物理力作为控制信号的视频生成方法。通过利用原始预训练模型中的视觉和运动先验，无需使用任何3D资产或物理模拟器，这种方法可以生成对物理控制信号作出真实反应的视频。主要挑战在于难以获得高质量的力-视频配对训练数据。本文的关键发现是，视频生成模型即使只有限量的对对象进行演示，也能很好地适应来自Blender合成视频的物理力条件，实现对多样几何形状、设置和材料的逼真力模拟。
### Conclusion
本文的方法只用了大约15k训练样本，在四块A100 GPU上训练了一天，并在力遵从性和物理现实性方面超越现有方法，使世界模型更接近现实世界的物理交互。还提供了所有数据集、代码、权重以及交互视频演示，公布了研究成果。
## 549. `cs.CV` - 流和查询引导的特征聚合以实现高效准确的3D占用率预测 [PDF](https://arxiv.org/pdf/2503.22087), [HTML](https://arxiv.org/abs/2503.22087)
### Authors
Seokha Moon,Janghyun Baek,Giseop Kim,Jinkyu Kim,Sunwook Choi
### Background
在自动驾驶中，3D占用率预测已成为关键的感知任务，因为它有助于全面理解场景。虽然最近的方法通过多帧融合空间-时间信息来增强理解，但这些方法在准确性和计算成本之间存在权衡：密集的体素表示提供高精度但计算成本高，而稀疏的表示则提高效率但损失空间细节。
### Innovation
本文介绍了DuOcc，通过双重聚合策略保留密集体素表示以保留空间保真度，同时保持高效率。DuOcc包含两个关键组件：(i) 流式体素聚合，动态累积体素特征并逐帧精细化，以抑制翘曲诱发的畸变，保持被占用和未占用空间之间的清晰分离。(ii) 查询引导的聚合，通过在由动态物体占据的体素区域中选择性地注入实例级查询特征，补充体素累积的局限性。
### Conclusion
实验在广泛使用的Occ3D-nuScenes和SurroundOcc数据集上表明，DuOcc在实时设置中实现了最先进的性能，并且与先前的方法相比，内存使用量减少了超过40%。
## 550. `cs.CV` - LogicOCR：你的大型多模态模型在文本丰富的图像上逻辑推理是否出色？ [PDF](https://arxiv.org/pdf/2505.12307), [HTML](https://arxiv.org/abs/2505.12307)
### Authors
Maoyuan Ye,Haibin He,Qihuang Zhong,Jing Zhang,Juhua Liu,Bo Du
### Background
研究最近在大型多模态模型（LMMs）上的进展已经极大地改善了它们的推理和光学字符识别能力，然而这类模型在复杂逻辑推理方面仍对包含大量文本的图像效果欠佳。该论文为这一领域提供了新的参考基准——LogicOCR，包含2780个问题并分为两个子集：LogicOCR-Gen 由1100个关于生成图像的选择判断题构成，LogicOCR-Real 包含1680条精心设计的自由形式问题，针对于真实场景的图片。
### Innovation
论文提出了 LogicOCR 基准，首次评估了 LMMs 在真实图像中的逻辑推理能力，并通过自定义生成图像的机制来解决视觉-QA 中的布局和字体多样性问题。此外，论文还提出了一种名为 TextCue 的训练无监督的方法，能够在不影响模型训练的情况下增强模型处理含有重要文本提示的图像区域的能力。实验结果显示，TextCue 方法在CoT设置下可提高1.8%的准确率。
### Conclusion
研究发现，尽管LMMs在模态处理上取得的进展显著，但在视觉阅读和逻辑推理的结合方面仍有较大提升空间。对 LMMs 进行针对图像区域的改进后，模型在处理含有文本提示的复杂问题时表现有所提升，但整体水平仍不及相应的纯文本输入处理效果。此外，该研究为以后的改进工作提供了关键性见解，推动了该领域的基准发展。基准数据集现已公开。
## 551. `cs.CV` - Diffusion-Denoised Hyperspectral Gaussian Splatting [PDF](https://arxiv.org/pdf/2505.21890), [HTML](https://arxiv.org/abs/2505.21890)
### Authors
Sunil Kumar Narayanan,Lingjun Zhao,Lu Gan,Yongsheng Chen
### Background
高光谱成像（HSI）已被广泛应用于农业应用中，用于非破坏性估计植物营养成分和精确量化样本营养元素。近年来，诸如Neural Radiance Field (NeRF)等3D重建方法被用来创建HSI场景的隐式神经表示，这使得在每个空间位置上渲染高光谱通道组成成为可能，从而帮助定位目标物体的营养成分在空间和光谱上的位置。然而，这种方法在训练时间和渲染速度上面临局限。
### Innovation
本文提出了一种名为Diffusion-Denoised Hyperspectral Gaussian Splatting (DD-HGS)的方法，通过引入波长感知的球谐函数、Kullback-Leibler散度为基础的光谱损失和基于扩散的去噪器来增强现有的3D Gaussian Splatting (3DGS)方法，从而实现整个光谱范围内的高光谱场景的3D明确重建。在Hyper-NeRF数据集的多种真实场景上进行了广泛评估，展示了DD-HGS的有效性。实验结果表明，DD-HGS相比之前的所有方法都达到了新的最先进水平。
### Conclusion
DD-HGS方法在训练时间和渲染速度上具有优势，实现了高光谱场景的3D明确重建，并在多种真实高光谱场景上达到了新最先进水平。
## 552. `cs.CV` - 适配Segment Anything Model进行电力传输走廊隐患分割 [PDF](https://arxiv.org/pdf/2505.22105), [HTML](https://arxiv.org/abs/2505.22105)
### Authors
Hang Chen,Maoyuan Ye,Peng Yang,Haibin He,Juhua Liu,Bo Du
### Background
电力传输走廊隐患分割（PTCHS）旨在从复杂背景中分离出电力传输设备及其周围的风险，对于维护电力传输安全具有重要意义。最近，Segment Anything Model（SAM）作为一种基础视觉模型出现，并推动了分割任务的边界。然而，SAM在处理复杂电力传输走廊场景中的目标对象时存在困难，特别是在那些具有精细结构的目标上。
### Innovation
本文提出了一种适配SAM进行PTCHS任务的方法，即ELE-SAM。通过开发一种上下文感知提示适配器，整合全局-局部特征并更关注关键区域以实现更好的提示标记。为了应对复杂背景中的精细结构隐患物体，设计了一种多粒度掩码解码器，通过利用多粒度掩码特征并放大到更高分辨率来解决这一问题。此外，为了训练ELE-SAM并推动此领域的发展，构建了包含44,094个图像-掩码对的ELE-40K基准，这是首个用于PTCHS的大规模和真实世界数据集。
### Conclusion
ELE-40K基准的实验结果证明了ELE-SAM的优越性能，其平均mIoU和mBIoU性能分别提高了16.8%和20.6%。此外，与HQSeg-44K上的当前最先进方法相比，ELE-SAM的平均mIoU和mBIoU绝对改进分别为2.9%和3.8%，这进一步验证了我们方法在高质量通用对象分割中的有效性。源代码和数据集可在该链接下载：this https URL。
## 553. `cs.CV` - 在几何正则化下的基于局部和非局部扰动的迁移学习 [PDF](https://arxiv.org/pdf/2505.15191), [HTML](https://arxiv.org/abs/2505.15191)
### Authors
Hana Satou,Alan Mitkiy,Emma Collins,Finn Kingston
### Background
领域间的数据差异导致了迁移学习中的根本挑战，特别是在源域和目标域数据流型存在分歧时。现有方法难以同时捕捉语义变化和模型脆弱性。
### Innovation
提出了一种名为MAADA（Manifold-Aware Adversarial Data Augmentation）的新颖框架，将对抗性扰动分解为流型内和流型外两个部分，旨在同时捕捉语义变化和模型脆弱性。此外，引入了几何感知对齐损失来最小化源域和目标域流型间的测地距离差异。
### Conclusion
通过在域Net、VisDA和Office-Home数据集上的实验表明，MAADA在无监督和少样本设置中均显著优于现有对抗性和适应性方法，展示了出色的结构性鲁棒性和跨域泛化能力。
## 554. `cs.CV` - MetricHMSR：基于单目图像的度量人体网格和场景恢复 [PDF](https://arxiv.org/pdf/2506.09919), [HTML](https://arxiv.org/abs/2506.09919)
### Authors
Chentao Song,He Zhang,Haolei Yuan,Haozhe Lin,Jianhua Tao,Hongwen Zhang,Tao Yu
### Background
目前大多数方法在单目图像下，由于相机模型的不现实假设和度量感知固有的挑战，难以通过单一模块实现人体姿态和度量3D位置的估计。
### Innovation
MetricHMSR创新性地引入了相机光线来全面编码边界框信息和透视投影的内在参数。提出了Human Mixture-of-Experts (MoE)，动态路由图像特征和光线特征到任务特定专家，以特殊理解不同数据方面，实现将局部姿态与全局3D位置统一感知的框架。进一步优化了现有的单目度量深度估计方法以获得更准确的结果。
### Conclusion
实验结果表明，所提出的方法在人体网格和场景恢复上达到了最先进的性能。
## 555. `cs.CV` - Vision Remember: 在高效大型视觉语言模型中通过视觉特征采样恢复视觉信息 [PDF](https://arxiv.org/pdf/2506.03928), [HTML](https://arxiv.org/abs/2506.03928)
### Authors
Ze Feng,Jiang-jiang Liu,Sen Yang,Lingyu Xiao,Zhibin Quan,Zhenhua Feng,Wankou Yang,Jingdong Wang
### Background
由于大型视觉语言模型（LVLMs）中冗余视觉标记的计算成本较高，许多现有方法通过视觉投影对其进行压缩。但是，这种压缩可能会丢失关键性的细节空间关系信息，这对光学字符识别（OCR）和图表表格理解等任务至关重要。因此，研究者提出了新的方法来保留这些详细的视觉信息。
### Innovation
本文提出了一个新的模块叫做Vision Remember，它包括两个关键模块：1）标记-特征交叉注意力层；2）标记双向自我注意力层。在标记双向注意力中，使用自我注意力机制来维持视觉标记和文本引导标记之间的双向互作；在标记特征交互注意力中，引入了局部交叉注意力来重新采样视觉特征，并使用多级融合来丰富视觉表示。实验结果表明，以LLaVA-NeXT基线进行评估时，Vision Remember相比TokenPacker提升了2.7%，比FastV提升了5.7%。同时，在与DeepStack和SVA聚合器进行比较时，我们的方法在基线相同的条件下分别取得了3.9%和3.4%的提升。
### Conclusion
本文提出的方法有效地结合了各种高效视觉投影器和LVLMs，验证了其在视觉理解基准测试中的泛化能力。
## 556. `cs.CV` - ISAC: 无需训练的实例到语义注意力控制以改进多实例生成 [PDF](https://arxiv.org/pdf/2505.20935), [HTML](https://arxiv.org/abs/2505.20935)
### Authors
Sanghyun Jo,Wooyeol Lee,Ziseok Lee,Kyungsu Kim
### Background
文本到图像的扩散模型近期变得极其强大，但在多对象场景中，这些模型的行为却表现得不够可靠。这些问题包括生成错误数量的对象实例，以及对象之间的语义信息泄露。研究人员发现，这些失败的根本原因是实例边界模糊。虽然自注意力机制能在去噪过程中早期揭示实例布局，但现有的方法仅作用于语义信号上。
### Innovation
本文提出了无需训练的实例到语义注意力控制（ISAC）方法，这是一种通用目标，通过首先从自注意力中分割出实例布局，然后将语义绑定到这些实例来执行分层注意力控制。ISAC 在第一阶段将自注意力聚合成实例的数量，并防止重叠，从而建立实例级的结构层次；在第二阶段，它将这些实例线索注入交叉注意力中，以获得实例感知的语义掩码，并通过将每个实例内的属性绑定来分解混合语义。ISAC 在 T2I-CompBench、HRS-Bench 和我们新构建的用于内部类组合的 IntraCompBench 上实现了稳定的提升，其中后者是失败最频繁的地方。
### Conclusion
ISAC 提升了多实例生成的准确性，尤其是类内组合的情况下，至少 50% 的多类准确性和 7% 的多实例准确性的提升，而无需任何微调或外部模型。此外，ISAC 在包含重叠框的布局到图像控制器中也表现出优越性，通过细化粗略的框布局为密集的实例掩码。这些结果表明，分层次地解耦实例形成和语义分配是实现统一、可控的多对象生成的关键原则。
## 557. `cs.CV` - 基于语义蒸馏的一步扩散图像压缩 [PDF](https://arxiv.org/pdf/2505.16687), [HTML](https://arxiv.org/abs/2505.16687)
### Authors
Naifu Xue,Zhaoyang Jia,Jiahao Li,Bin Li,Yuan Zhang,Yan Lu
### Background
近年来，基于扩散的生成型图像编码器已经显示出出色的性能，但它们的迭代抽样过程带来了不愉快的延迟。
### Innovation
提出了一种名为OneDC的一步扩散型生成图像编码器，通过整合隐空间压缩模块与一步扩散生成器；使用超前置码作为语义信号，克服了文本提示表示复杂视觉内容的局限；引入语义蒸馏机制，从预训练的生成型分词器中转移知识到超前置码编解码器；采用了基于像素和隐空间的联合优化，以提高重建保真度和感知真实性。
### Conclusion
实验结果表明，OneDC即使在一步生成的情况下，也能达到最佳的感知质量，比之前的多步骤扩散型编解码器实现了超过39%的比特率降低和20倍更快的解码速度。
## 558. `cs.CV` - 通过局部梯度感知表面滤波学习噪声点的法线 [PDF](https://arxiv.org/pdf/2507.03394), [HTML](https://arxiv.org/abs/2507.03394)
### Authors
Qing Li,Huifang Feng,Xun Gong,Yu-Shen Liu
### Background
在3D几何处理中，基于嘈杂点云估算法线一直是一个持续的挑战，尤其是对于端到端的法线估计。现有方法通常仅针对相对干净的数据，并依赖监督先验在特定邻域内拟合局部表面。
### Innovation
本文提出了一种新颖的法线学习方法，通过局部梯度感知表面滤波来处理嘈杂点云。该方法利用局部梯度约束的隐式函数估计出法线和距离，对点进行投影并融合沿法线的距离测量，同时开发了一种基于隐式场的表面点构造方法，具有投影约束，并引入了局部梯度一致性、方向性与聚集等约束来解决过度平滑和梯度降解问题。
### Conclusion
在法线估计、表面重构和点云去噪的全面实验中，该方法展示了最先进的性能。源代码和训练模型可通过以下网址获取：this https URL。
## 559. `cs.CV` - IVY-FAKE: 统一的图像和视频AIGC解释性框架和基准 [PDF](https://arxiv.org/pdf/2506.00979), [HTML](https://arxiv.org/abs/2506.00979)
### Authors
Changjiang Jiang,Wenhui Dong,Zhonghao Zhang,Chenyang Si,Fengchang Yu,Wei Peng,Xinbin Yuan,Yifei Bi,Ming Zhao,Zian Zhou,Caifeng Shan
### Background
近年来，生成式人工智能内容（AIGC）技术的迅速发展使得高质量的合成内容得以产生，但这也带来了重大的安全风险。现有检测方法存在两个主要局限性：缺少多维度可解释的数据集；现有开放源代码数据集（如WildFake、GenVideo）依赖过于简化的二元标注，限制了训练检测器的解释性和可信度；早期基于MLLM的伪造检测器（如FakeVLM）在逐步推理中的解释不够精细，阻碍了可靠的定位和解释。
### Innovation
本文引入了Ivy-Fake，这是首个大规模的多模态可解释AIGC检测基准。它包含超过106,000个丰富注释的训练样本和5,000个手动验证的评估示例，均来自精心设计的管道下的多个生成模型和真实世界数据集，以确保多样性和质量。此外，提出了Ivy-xDetector，一种基于组相对策略优化（GRPO）的强化学习模型，能够生成可解释的推理链，相对于多种合成内容检测基准实现了稳健的性能。
### Conclusion
广泛的实验证明了本数据集的优势，并验证了本方法的有效性。我们的方法在GenImage上的性能从86.88%提高到96.32%，大幅超越了先前的最先进的方法。
## 560. `cs.CV` - 动态ε调度：一种多因素自适应扰动预算的对抗训练方法 [PDF](https://arxiv.org/pdf/2506.04263), [HTML](https://arxiv.org/abs/2506.04263)
### Authors
Alan Mitkiy,James Smith,Myungseo wong,Hana Satou,Hiroshi Tanaka,Emily Johnson
### Background
对抗训练是防御深度神经网络对抗样本的最有效策略之一。现有的对抗训练方法普遍依赖固定的扰动预算，这未能考虑到样本本身的鲁棒性特征。尽管已有如IAAT和MMA的研究引入了基于实例的适应性，但它们通常基于启发式或静态的数据鲁棒性近似。
### Innovation
本文提出了一种新的框架——动态ε调度（DES），该框架能够每实例和每训练迭代自适应调整对抗扰动预算。DES结合了三个关键因素：（1）通过梯度近似决策边界距离；（2）从softmax熵中导出的预测置信度；（3）通过蒙特卡洛丢弃估算的模型不确定性。通过将这些线索整合为统一的调度策略，DES动态调整扰动预算以引导更有效的对抗学习。实验结果表明，该方法在CIFAR-10和CIFAR-100上提高了对抗鲁棒性和标准准确性，相较于固定ε基线和先前的自适应方法。
### Conclusion
本研究提供了我们调度策略的稳定性与收敛性的理论洞察，并为基于实例的，数据驱动的对抗训练方法开辟了一个新的研究方向。
## 561. `cs.CV` - 对视频理解的多模态LLMs可信性进行基准测试 [PDF](https://arxiv.org/pdf/2506.12336), [HTML](https://arxiv.org/abs/2506.12336)
### Authors
Youze Wang,Zijun Chen,Ruoyu Chen,Shishen Gu,Wenbo Hu,Jiayang Liu,Yinpeng Dong,Hang Su,Jun Zhu,Meng Wang,Richang Hong
### Background
近年来，多模态大型语言模型（视频LLMs）在处理复杂的空间-时间数据方面的能力得到了提升。然而，事实不准确、有害内容、偏见、幻觉和隐私风险等挑战削弱了它们的可靠性。为了评估视频LLMs在真实性、鲁棒性、安全性、公平性和隐私等方面的能力，研究引入了Trust-videoLLMs，这是一个全面的基准测试框架，评估了23个最先进的视频LLMs（5个商业的，18个开源的）。
### Innovation
Trust-videoLLMs是首个综合评估23款最先进的视频LLMs（包括5个商业款和18个开源款）的基准框架，从真实性、鲁棒性、安全性、公平性和隐私五个关键维度进行评估。评估内容包括30项任务，使用了调整过的、合成的和注释过的视频，以测量空间-时间风险、时间一致性和跨模态影响。该研究揭示了动态场景理解、跨模态抗干扰性和现实世界风险缓解等显著限制。
### Conclusion
尽管开源模型有时会表现更优，但专有模型通常在可信度方面表现出色，然而规模化的改进并不能始终提高性能。研究强调了增强训练数据多样性和强化多模态对齐的重要性。Trust-videoLLMs提供了一个可供公众使用的可扩展工具包，用于标准化的信任评估，填补了准确性驱动的基准测试和对鲁棒性、安全、公平性和隐私需求之间的差距。
## 562. `cs.CV` - WeatherDiffusion: 近内在空间可控天气编辑 [PDF](https://arxiv.org/pdf/2508.06982), [HTML](https://arxiv.org/abs/2508.06982)
### Authors
Yixin Zhu,Zuoliang Zhu,Jian Yang,Miloš Hašan,Jin Xie,Beibei Wang
### Background
传统的像素空间编辑方法在可控性方面存在局限性，特别是对于复杂的大规模室外环境，难以实现精确的天气条件控制。现有的天气修复方法和渲染基方法同样存在不足。
### Innovation
提出了WeatherDiffusion框架，该框架基于扩散先验包括逆渲染器和前向渲染器两部分：逆渲染器能够从输入图像中估计材质属性、场景几何和照明等内在映射；前向渲染器利用这些几何和材质映射以及描述特定天气条件的文本提示生成最终图像。引入了内在映射感知的注意力机制以提高大室外场景的空间对应性和分解质量；同时提出了CLIP空间的天气提示插值方法，实现精细天气控制。
### Conclusion
WeatherDiffusion框架在可控天气编辑方面优于现有像素空间编辑方法、天气修复方法和渲染基方法，显示出在下游任务如自动驾驶中的应用潜力，提高检测和分割在恶劣天气条件下的鲁棒性。
## 563. `cs.CV` - ReasonAct：小模型中细粒度视频推理的分阶段训练 [PDF](https://arxiv.org/pdf/2508.01533), [HTML](https://arxiv.org/abs/2508.01533)
### Authors
Jiaxin Liu,Zhaolu Kang
### Background
尽管近期多模态模型在视觉-语言任务中取得了进展，但小型化变体仍然在视频理解所需的精细时间推理方面挣扎。
### Innovation
提出了ReasonAct方法，通过三层训练过程增强小型模型的视频推理能力：首先仅通过文本推理建立基础，然后视频微调，最后使用时间感知强化学习进行细化。引入了生物力学启发的子动作分解机制，提供逐步奖励给组成动作阶段，并结合了时间一致性建模到策略优化中。
### Conclusion
在HMDB51、UCF-101和Kinetics-400上的实验表明，3B参数的模型分别达到了67.2%、94.1%和78.9%的准确率，比基线提高了17.9、15.8和12.3个点。消融研究证实逐步训练可以使小型模型实现具有竞争力的视频推理性能同时保持计算效率。
## 564. `cs.CV` - MANGO: 多模态注意流融合学习方法 [PDF](https://arxiv.org/pdf/2508.10133), [HTML](https://arxiv.org/abs/2508.10133)
### Authors
Thanh-Dat Truong,Christophe Bobda,Nitin Agarwal,Khoa Luu
### Background
近年来，多模态学习取得了显著的成功。然而，当前的多模态融合方法通过采用变压器的注意机制隐式地学习多模态特征之间的潜在联系，使得模型难以捕获每个模态的基本特征，进而难以理解复杂的多模态输入结构和联系。
### Innovation
本文引入了一种新颖的多模态注意流（MANGO）方法，用于实现明确的、可解释的和可处理的多模态融合学习。提出的变换可逆交叉注意（ICA）层，通过引入三种新的交叉注意机制：模态到模态交叉注意（MMCA）、跨模态交叉注意（IMCA）和可学习的跨模态交叉注意（LICA），高效地捕捉多模态数据中的复杂潜在联系。此外，引入了多模态注意流，使该方法能够扩展到高维多模态数据。
### Conclusion
在三种不同的多模态学习任务（语义分割、图像到图像的翻译和电影类型分类）上进行的实验结果表明，该提出的方法具有最先进的性能。
## 565. `cs.CV` - 定向令牌：大型语言视觉模型的稳健多模态对齐方法 [PDF](https://arxiv.org/pdf/2508.14264), [HTML](https://arxiv.org/abs/2508.14264)
### Authors
Thanh-Dat Truong,Huu-Thien Tran,Tran Thai Son,Bhiksha Raj,Khoa Luu
### Background
大型多模态模型(LMMs)由于其在多种理解任务中的出色能力而取得了显著的性能。然而，这些模型仍然面临着由于视觉和文本特征之间的对齐和相关性而导致的稳健性和泛化能力的限制。
### Innovation
本文提出了一种简单但有效的学习机制，通过解决洗牌问题来改善视觉和文本模态之间的稳健对齐。具体而言，该方法通过在预训练和微调阶段引入两个新任务，即重建图像顺序和文本顺序，提高推理能力、视觉理解能力和跨模态对齐。此外，提出了一种新的定向令牌方法，以捕捉视觉和文本知识，使模型能够重建视觉输入的正确顺序。同时，引入了一种新的图像到响应引导损失，进一步提高了LMM在响应中的视觉理解能力。
### Conclusion
所提出的方法在学术任务导向和指令跟随LMM基准上，能够一致地实现最先进的性能（SoTA），从而提供一种有效的方法来增强大型语言视觉模型的多模态对齐和视觉理解能力。
## 566. `cs.CV` - FastAvatar：单张不受限制姿态人脸识别的即时3D高斯点绘制 [PDF](https://arxiv.org/pdf/2508.18389), [HTML](https://arxiv.org/abs/2508.18389)
### Authors
Hao Liang,Zhixuan Ge,Soumendu Majee,Ashish Tiwari,G.M. Dilshan Godaliyadda,Ashok Veeraraghavan,Guha Balakrishnan
### Background
当前3D面部重构技术多采用复杂的优化方法，无法快速重建高质量的3D人脸模型。这些方法通常需要较多的运算时间，并且在极端输入姿态下容易出现不稳定的重构效果。
### Innovation
FastAvatar 提出了一个新的两阶段设计算法，第一阶段使用前馈编码器解码器来预测粗略的面部几何结构，第二阶段进行轻量级的测试时优化以实现照片级别的渲染。这种混合策略结合了直接预测的速度与稳定性和优化的准确性，即使在极端输入姿态下也能保持强烈的面部特征保存。
### Conclusion
FastAvatar 达到了最先进的重建质量（24.01 dB PSNR，0.91 SSIM），并且运行速度超现有逐对象优化方法（如FlashAvatar，GaussianAvatars，GASP）600倍以上。一旦重建完成，我们的肖像可以支持照片级的新视角合成和FLAME引导的表情动画，从而从单个图像中实现可控的再现。FastAvatar 的高保真度、姿态鲁棒性和快速重建能力显著扩大了基于3D高斯点绘制的面部肖像的应用范围。
## 567. `cs.CV` - 通过增量生成和多智能体协作进行多尺度时间预测 [PDF](https://arxiv.org/pdf/2509.17429), [HTML](https://arxiv.org/abs/2509.17429)
### Authors
Zhitao Zeng,Guojian Yuan,Junyuan Mao,Yuxuan Wang,Xiaoshuang Jia,Yueming Jin
### Background
准确的时间预测是全面场景理解和身体型人工智能之间的桥梁。然而，对于视觉语言模型来说，预测场景在多时间尺度下的多个细粒度状态具有挑战性。我们通过分解多尺度为两个正交维度——时间尺度和状态尺度，为通用和手术场景形式化了多尺度时间预测（MSTP）任务。这一任务要求模型不仅要预测不同时间跨度下的行为和事件状态，还要建模场景中不同层次的状态关系，如身体接触关系相较于空间关系更为细粒度，而在手术场景中，具体步骤相较于高阶阶段更为细粒度，但仍然受限于其包络的阶段。
### Innovation
为了支持这一统一任务，本文首次提出了MSTP基准，该基准包含了跨多时间尺度和状态尺度的同步标注。同时，我们提出了增量生成和多智能体协作方法（IG-MC），该方法整合了两个关键创新点：第一个是插件式的增量生成模块，该模块能够随着时间尺度的扩展不断生成最新的视觉预览，为多个决策智能体提供信息支持，并保持决策和生成视觉的一致性，从而防止决策性能随前瞻间隔的延长而下降；第二个是决策驱动的多智能体协作框架，该框架包括生成、启动和多状态评估智能体，可在动态触发和评估预测周期以平衡全局一致性和局部真实性。
### Conclusion
我们为通用场景和手术场景形式化了多尺度时间预测任务，并提出了MSTP基准和IG-MC方法。该方法中的增量生成模块和多智能体协作框架显著提高了预测的准确性和一致性，确保了多时间尺度下的有效决策过程，为视觉语言模型在复杂场景中进行细粒度时间预测提供了新的解决方案。
## 568. `cs.CV` - 无遮罩阴影去除中的对比先验增强二元性 [PDF](https://arxiv.org/pdf/2507.21949), [HTML](https://arxiv.org/abs/2507.21949)
### Authors
Jiyu Wu,Yifan Liu,Jiancheng Huang,Mingfu Yan,Shifeng Chen
### Background
现有的阴影去除方法通常依赖于遮罩，但在实际场景中获取这些遮罩具有挑战性。探索固有图像线索（如局部对比度信息）成为在缺乏明确遮罩的情况下指导阴影去除的潜在替代方案。然而，在复杂场景中，这些线索的固有歧义性会成为一个关键局限，导致它们难以区分真实阴影和低反射率物体以及复杂的背景纹理。
### Innovation
提出了自适应门控双分支注意机制（AGBA），该机制动态筛选和重新加权对比度先验，以有效分离阴影特征与混淆视觉元素。此外，提出了一种基于扩散的频率-对比度融合网络（FCFN），利用高频和对比度线索指导生成过程，以解决恢复柔和阴影边界和细粒度细节的持续挑战。
### Conclusion
大量实验表明，我们的方法在无遮罩方法中达到了最先进的结果，同时保持与基于遮罩方法相当的竞争性能。
## 569. `cs.CV` - 在扩散模型中整合内在场景属性以实现空间一致的图像生成 [PDF](https://arxiv.org/pdf/2508.10382), [HTML](https://arxiv.org/abs/2508.10382)
### Authors
Hyundo Lee,Suhyung Choi,Inwoo Hwang,Byoung-Tak Zhang
### Background
大规模数据集训练的图像生成模型可以合成高质量的图像，但常常会产生空间不一致和失真的图像，原因是这些模型缺乏关于底层结构和平面布局的详细信息。先前的工作要么仅依赖图像-文本对，要么将内在属性作为条件输入，但未能充分捕捉底层场景结构。
### Innovation
本文利用预先训练的估计器从大型图像数据集中提取丰富的内在场景属性，无需额外场景信息或显式3D表示。通过自编码器聚合各种内在场景属性到一个潜在变量，并在预训练的大规模潜在扩散模型（LDMs）上进行改进，同时在图像和内在属性领域去噪以共享相互信息，使得图像和内在属性相互反映而不牺牲图像质量。
### Conclusion
实验结果表明，本文方法可以纠正空间不一致性并生成更为自然的场景布局，同时保持基模型（如稳定扩散）的保真度和文本对齐。
## 570. `cs.CV` - ControlEvents：基于图像扩散模型先验的可控事件摄像机数据合成 [PDF](https://arxiv.org/pdf/2509.22864), [HTML](https://arxiv.org/abs/2509.22864)
### Authors
Yixuan Hu,Yuxuan Xue,Simon Klenk,Daniel Cremers,Gerard Pons-Moll
### Background
近年来，事件摄像机由于其仿生特性，如高时间分辨率和大动态范围，受到了广泛关注。然而，要获得大规模标注的地面真实数据以用于基于事件的视觉任务仍然困难且成本高。
### Innovation
提出了一种基于扩散生成模型的ControlEvents方法，该方法通过使用来自基础模型（如Stable Diffusion）的扩散先验，合成高质量的事件数据，并引导多种控制信号（如类别文本标签、2D骨架和3D人体姿态）。该方法在不需要大量微调和有限标注数据的情况下生成高质量的事件数据，并简化了数据生成过程，大幅降低了生产标注事件数据集的成本。
### Conclusion
通过合成用于视觉识别、2D骨架估计和3D人体姿态估计的标注事件数据，展示了该方法的有效性。实验结果表明，合成的标注事件数据能够提升模型在所有任务中的性能。此外，该方法可以在训练过程中生成基于未见文本标签的事件数据，展示了从基础模型继承的强大文本生成能力。
## 571. `cs.CV` - GreenHyperSpectra: 针对全球植被性状预测的多源高光谱数据集 [PDF](https://arxiv.org/pdf/2507.06806), [HTML](https://arxiv.org/abs/2507.06806)
### Authors
Eya Cherif(1, 2 and 3),Arthur Ouaknine(3 and 4),Luke A. Brown(5),Phuong D. Dao(6, 7 and 8),Kyle R. Kovach(9),Bing Lu(10),Daniel Mederer(1),Hannes Feilhauer(1, 2, 12 and 13),Teja Kattenborn(11 and 12),David Rolnick(3 and 4) ((1) Institute for Earth System Science and Remote Sensing, Leipzig University, Germany, (2) Center for Scalable Data Analytics and Artificial Intelligence (<a href=?http://ScaDS.AI? rel=?external noopener nofollow? class=?link-external link-http?>this http URL</a>), Leipzig University, Germany, (3) Mila Quebec AI Institute, Canada, (4) McGill University, Canada, (5) School of Science, Engineering and Environment, University of Salford, UK, (6) Department of Agricultural Biology, Colorado State University, USA, (7) Graduate Degree Program in Ecology, Colorado State University, USA, (8) School of Global Environmental Sustainability, Colorado State University, USA, (9) Department of Forest and Wildlife Ecology, University of Wisconsin, USA, (10) Department of Geography, Simon Fraser University, Canada, (11) Chair of Sensor-based Geoinformatics (geosense), University of Freiburg, Germany, (12) German Centre for Integrative Biodiversity Research (iDiv), Halle-Jena-Leipzig, Germany, (13) Helmholtz-Centre for Environmental Research (UFZ), Leipzig, Germany)
### Background
植物性状如叶片碳含量和叶片质量是研究生物多样性和气候变化的关键变量。然而，传统的实地采样难以在生态上具有意义的空间范围内覆盖植物性状的变化。机器学习代表了一种有价值的解决方案，通过遥感高光谱数据进行生态系统范围内的植物性状预测。然而，从高光谱数据预测性状受到了标签稀缺和数据域间显著变化带来的挑战（例如不同传感器和生态分布之间），需要具备跨域鲁棒性的方法。
### Innovation
我们提出了一种名为GreenHyperSpectra的预训练数据集，它包含了跨传感器和跨生态系统的实际样本，旨在通过半监督和自我监督方法评估植物性状预测。我们采用了一种包含不同领域场景的评估框架。我们成功利用GreenHyperSpectra对标签效率的多输出回归模型进行预训练，该模型在性能上优于最新的监督基准。我们的实证分析表明，在植物功能特性评估方面，通过学习光谱表示取得了显著改进，建立了结合表示学习和植物功能性状的研究方法框架，推动了相关领域研究。
### Conclusion
我们通过学习光谱表示显著提高了植物性状预测，建立了跨域鲁棒性方法框架，为植物功能性状评估及交叉领域研究提供了全面的方法。所有代码和数据可在以下网址获取：this https URL.
## 572. `cs.CV` - SaFiRe: 使用Mamba的眼动-固定重复迭代用于参照图像分割 [PDF](https://arxiv.org/pdf/2510.10160), [HTML](https://arxiv.org/abs/2510.10160)
### Authors
Zhenjie Mao,Yuhuan Yang,Chaofan Ma,Dongsheng Jiang,Jiangchao Yao,Ya Zhang,Yanfeng Wang
### Background
当前的图像参照分割（RIS）研究主要依赖预训练的视觉骨干网络和更多的训练语料，这些方法在处理简单表达式时表现良好，如“红色汽车”或“左边的女孩”。然而，这些方法往往简化了参照表达，将其降级为关键词/概念匹配任务，这限制了模型处理表达中的引用歧义能力。
### Innovation
本文提出了一个名为SaFiRe的新框架，该框架模仿了人类的认知两阶段过程：首先形成全局理解，然后通过详细检查进行完善。SaFiRe利用Mamba的扫描-更新特性，实现高效多周期精细校准，复杂度为线性。此外，本文还引入了一个新的基准数据集aRefCOCO，用于评估在模糊表达式下的RIS模型。
### Conclusion
在标准和新提出的数据集上的广泛实验表明SaFiRe模型优于最先进的基线。
## 573. `cs.CV` - VA-GS: 通过视图对齐增强高斯点云的几何表示 [PDF](https://arxiv.org/pdf/2510.11473), [HTML](https://arxiv.org/abs/2510.11473)
### Authors
Qing Li,Huifang Feng,Xun Gong,Yu-Shen Liu
### Background
3D Gaussian Splatting 最近成为高保真实时新视图合成的有效解决方案。然而，其对表面重建的准确性仍存在不足。由于高斯的离散和无序特性，基于图像渲染损失的监督常常导致几何不准确和多视角对齐不一致。
### Innovation
提出了一种新方法，通过视图对齐 (VA) 提高 3D 高斯的几何表示。具体而言，通过引入边缘感知图像提示来改进表面边界划分，以提高渲染损失。引入视图感知的光度对齐损失来建模遮挡，鼓励高斯之间的准确空间关系。通过引入基于法线的约束来改善光照变化导致的歧义，改进高斯的空间取向和局部表面估计。利用深度图像特征嵌入以增强在不同视角和光照下所学习几何结构的鲁棒性。
### Conclusion
在标准基准上的大量实验表明，本方法在表面重建和新视图合成方面达到了最先进的性能。源代码可从此链接下载。
## 574. `cs.CV` - Decorrelation Speeds Up Vision Transformers [PDF](https://arxiv.org/pdf/2510.14657), [HTML](https://arxiv.org/abs/2510.14657)
### Authors
Kieran Carrigg,Rob van Gastel,Melda Yeghaian,Sander Dalm,Faysal Boughorbel,Marcel van Gerven
### Background
掩码自编码（MAE）预训练视觉转换器（ViTs）在少量标注数据的情况下表现出很强的效果，但其巨大的计算成本使其在时间紧迫且资源受限的工业环境中不切实际。
### Innovation
通过将去相关反向传播（DBP）集成到MAE预训练中，这种方法迭代地在每个层中减少输入相关性，从而加速收敛。DBP在保留稳定性的前提下实现了更快的预训练。在有限数据的情景下，DBP-MAE减少了基线性能的墙钟时间21.1%，降低了碳排放21.4%，并提高了分割mIoU 1.1个百分点。
### Conclusion
这些结果表明，DBP可以在大规模ViT预训练中减少训练时间和能源使用，同时改善下游性能。
## 575. `cs.CV` - EvoEmpirBench: 品质代理人ExpVer导向的动态空间推理 [PDF](https://arxiv.org/pdf/2509.12718), [HTML](https://arxiv.org/abs/2509.12718)
### Authors
Pukun Zhao,Longxiang Wang,Miaowei Wang,Chen Chen,Fanqing Zhou,Haojian Huang
### Background
现有的大多数空间推理基准主要集中在静态或全局可观察的环境中，忽视了在部分可观察性和动态变化条件下进行长时间推理和记忆利用的挑战。因此，本文提出两个动态空间基准测试，即局部可观察迷宫导航和匹配-2消除，这两个测试能够更全面地评估模型在局部感知、环境反馈和全局目标紧密耦合情况下的空间理解和适应性规划能力。每个动作都会触发环境结构的变化，要求模型不断更新认知和策略。
### Innovation
本文提出了两个新的动态空间基准测试：局部可观察迷宫导航和匹配-2消除。引入了一种基于主观体验的记忆机制，用于跨任务经验的转移和验证。实验表明，这些基准测试揭示了主流模型在动态空间推理和长期记忆方面的关键局限性，为未来方法的发展提供了全面的平台。
### Conclusion
本基准测试揭示了主流模型在动态空间推理和长期记忆方面的主要限制，为未来的实验方法发展提供了综合平台，代码和数据可在此链接获取。
## 576. `cs.CV` - 在深伪主动取证中揭露和缓解破坏性的多重嵌入攻击 [PDF](https://arxiv.org/pdf/2508.17247), [HTML](https://arxiv.org/abs/2508.17247)
### Authors
Lixin Jia,Haiyang Sun,Zhiqing Guo,Yunfeng Diao,Dan Ma,Gaobo Yang
### Background
随着深度伪造技术的迅速发展和数字媒体的广泛传播，个人隐私安全面临着越来越严重的威胁。现有的深度伪造主动取证方法通过在图像中嵌入不可察觉的水印以实现可靠的来源跟踪，成为对抗这些威胁的关键防御措施。但现有方法依赖于单一水印嵌入的理想化假设，这在现实场景中证明是不切实际的。
### Innovation
本文首次正式定义并展示了多重嵌入攻击(MEA)的存在。在原本已加密的图像进行额外的水印嵌入时，原来的取证水印会被破坏或移除，导致整个主动取证机制失效。为解决此漏洞，我们提出了一种称为对抗干扰模拟(AIS)的通用训练范式。AIS在微调过程中模拟MEA场景，并引入了基于韧性的损失函数，强制学习稀疏且稳定的水印表示。该方法使模型即使在第二次嵌入后仍能正确提取原始水印。
### Conclusion
经过广泛实验，我们的插件式AIS训练范式显著提高了各种现有方法在抵抗MEA方面的鲁棒性。
## 577. `cs.CV` - 轻量级异常检测模块化现场解决方案在农业可持续营养管理中的应用 [PDF](https://arxiv.org/pdf/2509.12247), [HTML](https://arxiv.org/abs/2509.12247)
### Authors
Abigail R. Cohen,Yuming Sun,Zhihao Qin,Harsh S. Muriki,Zihao Xiao,Yeonju Lee,Matthew Housley,Andrew F. Sharkey,Rhuanito S. Ferrarezi,Jing Li,Lu Gan,Yongsheng Chen
### Background
高效营养管理对于作物生长和可持续资源利用至关重要（例如氮和能量）。当前的方法需要长时间分析，无法实现实时优化；同样，成像技术有助于快速表型分析，但计算强度大，无法在资源受限条件下部署。
### Innovation
本文提出了一个灵活的分层管道，用于异常检测和状态估计（新鲜重量、干重和组织养分），包括整个效率-准确性范围的方法的能量分析。使用不同施肥强度（T1-100%，T2-50%，T3-25%）和多光谱成像（MSI）的养分耗尽实验，开发了一个使用自编码器（AE）的分层管道以早期预警。此外，对比了两种不同复杂性的状态估计模块：植物指数（VI）特征与机器学习（随机森林，RF），以及原始的整张图像深度学习（视觉转换器，ViT）。
### Conclusion
通过模块化管道，这项工作为边缘诊断和农业可持续性提供了机会。
## 578. `cs.CV` - 不平等的分割：重新审视无关类别间的属性泛化 [PDF](https://arxiv.org/pdf/2509.06998), [HTML](https://arxiv.org/abs/2509.06998)
### Authors
Liviu Nicolae Fircă,Antonio Bărbălau,Dan Oneata,Elena Burceanu
### Background
虽然先前的工作已经解决了在狭窄的分类或视觉上相似的领域内预测属性的问题，但仍然不清楚当前的模型是否能够抽象出属性并在概念上相距甚远的类别之间应用。本文首次提出了针对这种条件的属性预测任务鲁棒性的显式评估，研究模型是否能在不相关对象类型之间正确推断共享的属性，例如识别“有四条腿”这一属性同时适用于“狗”和“椅子”这两个类别。
### Innovation
本文介绍了一种新的训练-测试分割策略，该策略基于逻辑语言模型（LLM）驱动的语义分组、嵌入相似度阈值、基于嵌入的聚类和使用真实标签的超类别划分，以减少训练集和测试集之间的相关性。结果表明，随着训练和测试类别之间相关性的降低，性能急剧下降，表明模型对分割设计有强烈的敏感性。聚类方法最有效地平衡了减少隐藏的相关性与保持可学习性之间的权衡。
### Conclusion
这些发现为现有表示法的局限性提供了新的见解，并为属性推理的未来基准构建提供了指导。
## 579. `cs.CV` - SARVLM: SAR中的语义理解和目标识别的视觉语言基础模型 [PDF](https://arxiv.org/pdf/2510.22665), [HTML](https://arxiv.org/abs/2510.22665)
### Authors
Qiwei Ma,Zhiyu Wang,Wang Liu,Xukun Lu,Bin Deng,Puhong Duan,Xudong Kang,Shutao Li
### Background
合成孔径雷达（SAR）因其全天候成像能力而成为至关重要的成像技术。尽管近年来自监督学习和掩码图像建模（MIM）的进步使得SAR基础模型的构建成为可能，但这些方法主要强调低层级视觉特征，往往忽视SAR图像中的多模态对齐和零样本目标识别。
### Innovation
本文构建了包含超过一百万对图像-文本数据的SARVLM-1M大规模视觉语言数据集，并提出了一种领域迁移训练策略来缩小自然图像和SAR图像之间的差距。在此基础上，开发了SARVLM，这是专门针对SAR的第一种视觉语言基础模型（VLM），包含SARCLIP和SARCap。SARVLM通过提出的领域迁移策略下的视觉语言对比目标进行训练，将SAR图像和文本描述联系起来。实验结果表明，SARVLM在图像文本检索、零样本分类、语义定位和图像描述方面表现出卓越的特征提取和解释能力，优于最先进的VLM，推动了SAR语义理解。
### Conclusion
SARVLM在多个任务上展示了优于现有技术的性能，特别是在语义理解和目标识别方面，并且通过领域迁移策略改进了SAR图像的理解。未来的工作将释放源代码和数据集，以便进一步研究和应用。
## 580. `cs.CV` - Saliency-R1：基于置信引导强化学习提升统一视觉显著性推理能力的多模态大语言模型 [PDF](https://arxiv.org/pdf/2511.00396), [HTML](https://arxiv.org/abs/2511.00396)
### Authors
Long Li,Shuichen Ji,Ziyang Luo,Zhihui Li,Dingwen Zhang,Junwei Han,Nian Liu
### Background
尽管多模态大型语言模型（MLLMs）在高层次的视觉语言推理中表现出色，但它们缺乏对视觉显著性的内在意识，难以识别关键的视觉元素。为了解决这一问题，本文提出了一种名为Saliency-R1的新框架，它首次统一解决了代表性且异构的三个显著性任务：显著对象检测（SOD）、显著实例分割（SIS）和共显著对象检测（CoSOD），增强了模型在显著性推理方面的能力。
### Innovation
文章提出了一个新的置信引导策略优化（CGPO）算法，这是一个基于单样本的新型强化学习算法，通过使用基于奖励和置信度差异的每样本信号替代分组归一化的优势，减少了计算浪费，避免了信号稀释，并降低了训练开销。同时，Saliency-R1框架通过结构化的文本接口（<rg>, <ins>）处理区域级和实例级的引用表达，并且通过单一的引用分割器来生成合适的任务掩码。
### Conclusion
实验结果显示，Saliency-R1超过或匹配了所有三种任务中稳健的开源/闭源MLLM和专门的最先进的方法的表现，证明了该框架在显著性推理方面的有效性。
## 581. `cs.CV` - MoEGCL: Mixture of Ego-Graphs Contrastive Representation Learning for Multi-View Clustering [PDF](https://arxiv.org/pdf/2511.05876), [HTML](https://arxiv.org/abs/2511.05876)
### Authors
Jian Zhu,Xin Zou,Jun Sun,Cheng Luo,Lei Liu,Lingfang Zeng,Ning Zhang,Bian Wu,Chang Tang,Lirong Dai
### Background
近年来，图神经网络（GNNs）在多视图聚类（MVC）方面的进展显著推动了该领域的发展。然而，现有的方法面临细粒度图融合的粗略问题。当前的许多方法为每个视图生成一个独立的图结构，然后在视图层面进行加权融合，这导致了不够精细的结果。
### Innovation
提出了一种新颖的混合自我图对比表示学习方法（MoEGCL）。该方法主要包括两个模块：一种创新的混合自我图融合（MoEGF），用于基于样本层面的细粒度融合，而不是传统的视图层面融合；以及自我图对比学习（EGCL）模块，通过对比学习增强聚类内样本的表示相似性。
### Conclusion
广泛的实验表明，MoEGCL 在深度多视图聚类任务中达到了最先进的成果。源代码已在该网址公开：this https URL.
## 582. `cs.CV` - TinyChemVL：通过高效视觉标记减少和复杂反应任务推进化学视觉语言模型 [PDF](https://arxiv.org/pdf/2511.06283), [HTML](https://arxiv.org/abs/2511.06283)
### Authors
Xuanle Zhao,Shuxin Zeng,Xinyuan Cai,Xiang Cheng,Duzhen Zhang,Xiuyi Chen,Bo Xu
### Background
视觉语言模型（VLMs）在通用视觉理解方面已经展示了令人瞩目的能力，但是在化学领域的应用却有限，因为先前的研究主要集中在文本上，忽略了诸如分子结构这样的关键视觉信息。现有的直接采用标准VLMs的方法遇到两个主要问题：一是处理整个化学图像时不具有信息背景的计算效率低下；二是仅限于分子级任务，限制了化学推理的进步。
### Innovation
提出TinyChemVL，一种借助视觉标记减少和反应级任务来提高模型效率和推理能力的高效而强大的化学视觉语言模型。此外，还提出了ChemRxn-V，一种用于评估基于视觉的反应识别和预测任务的反应级基准。结果表明，TinyChemVL仅使用4B参数便在分子和反应任务上均表现出优越的性能，且相比现有模型拥有更快的推理和训练速度。特别地，TinyChemVL仅使用了ChemVLM1/16的视觉标记便表现出更好的性能。
### Conclusion
本工作通过共同设计模型架构和任务复杂度，构建了适用于化学领域的高效而强大的视觉语言模型。
## 583. `cs.CV` - UniChange：利用多模态大规模语言模型统一变化检测 [PDF](https://arxiv.org/pdf/2511.02607), [HTML](https://arxiv.org/abs/2511.02607)
### Authors
Xu Zhang,Danyang Li,Xiaohang Dong,Tianhao Wu,Hualong Yu,Jianye Wang,Qicheng Li,Xiang Li
### Background
变化检测（CD）是监测和分析土地覆盖动态的基础任务。尽管最近高性能模型和高质量数据集显著推进了该领域的发展，但当前模型通常只能从单一类型的标注数据中获取有限的知识，无法同时利用二元变化检测（BCD）和语义变化检测（SCD）数据集中的多样化信息。这种限制导致了泛化能力差和灵活性有限的问题。
### Innovation
我们利用多模态大规模语言模型（MLLM）的语言先验和融合能力，开发了UniChange，这是首个基于MLLM的统一变化检测模型。UniChange通过引入三个特殊标记[T1]、[T2]和[CHANGE]将生成语言能力与专门的CD功能融为一体。UniChange使用文本提示来引导变化类别的识别，避免依赖预定义的分类头。此设计使UniChange能够从多源数据集中有效获取知识，即使这些数据集的类别定义存在冲突。
### Conclusion
在四个公共基准数据集（WHU-CD、S2Looking、LEVIR-CD+和SECOND）上进行的实验表明，UniChange表现最佳，分别达到IoU分数为90.41、53.04、78.87和57.62，超过了所有先前的方法。源代码可从提供的链接获取。
## 584. `cs.CV` - XYZCylinder：通过统一圆柱提升方法向兼容的驾驶场景先验3D高斯点绘制迈进 [PDF](https://arxiv.org/pdf/2510.07856), [HTML](https://arxiv.org/abs/2510.07856)
### Authors
Haochen Yu,Qiankun Liu,Hongyuan Liu,Jianfei Jiang,Juntao Lyu,Jiansheng Chen,Huimin Ma
### Background
三维重建的先验方法正成为研究焦点，这些方法通过学习固定的视角变换生成单一的场景表示。然而，在处理复杂的驾驶场景时，它们展现出显著的局限性。主要挑战包括：依赖固定的视角变换限制了对不同相机配置的兼容性；从稀疏的360°视角中学习复杂驾驶场景且重叠度低，导致最终重建的质量受损。
### Innovation
提出了XYZCylinder，一种基于统一圆柱提升的新方法，集成相机建模和特征提升。设计了一种统一轮廓相机建模（UCCM）策略，明确建模投影参数，从而统一不同的相机配置，无需学习依赖于视角的对应关系。提出了混合表示和若干基于新设计的圆柱平面特征组（CPFG）模块来将二维图像特征提升至三维空间。
### Conclusion
XYZCylinder在不同评估设置下实现了领先性能，并且在不同相机设置的全新场景中以无监督方式展示了卓越的兼容性。
## 585. `cs.CV` - PointNSP：基于下一尺度层次细节预测的自回归3D点云生成 [PDF](https://arxiv.org/pdf/2510.05613), [HTML](https://arxiv.org/abs/2510.05613)
### Authors
Ziqiao Meng,Qichao Wang,Zhiyang Dou,Zixing Song,Zhipeng Zhou,Irwin King,Peilin Zhao
### Background
相较于基于扩散的方法，自回归方法在点云生成的质量上一直落后。性能差异源于自回归模型在本质上无序的点集中强加了人工顺序，使得形状生成必须按顺序进行局部预测。这种顺序偏差虽然强调了短程连续性，但削弱了模型捕捉长程依赖性的能力，阻碍了模型执行全局结构属性如对称性、一致拓扑和大尺度几何规律的精准捕获。
### Innovation
受形状建模中层次细节（LOD）原则的启发，提出了基于粗到细生成框架的PointNSP，这是一种层次化生成框架，通过按尺度预测方式逐渐提升细粒度几何，并且多层次分解实现了自回归目标与点集不变性性质的一致性，允许丰富的内部层级交互，同时避免了固定顺序的脆弱性。
### Conclusion
在ShapeNet实验中，PointNSP首次在自回归框架内确立了最佳生成质量。此外，它在参数量、训练效率和推理效率上超过强大的基于扩散方法的基准。在稠密生成（8,192点）中，PointNSP的优势更加明显，突显了其扩展潜力。
## 586. `cs.CV` - 工业缺陷检测的自动化神经架构设计 [PDF](https://arxiv.org/pdf/2510.06669), [HTML](https://arxiv.org/abs/2510.06669)
### Authors
Yuxi Liu,Yunfeng Ma,Yi Tang,Min Liu,Shuai Jiang,Yaonan Wang
### Background
工业表面缺陷检测（SDD）是确保产品质量和制造可靠性的重要环节。由于表面缺陷的多样性和复杂性，SDD面临两大挑战：类别内部差异和类别间相似性。现有的方法主要依赖人工设计的模型，需要大量的试验和错误尝试，往往难以有效应对这两个挑战。
### Innovation
论文提出了AutoNAD（自动化神经架构设计）框架，这是一种设计用于SDD的自动化神经架构方法。它联合搜索卷积、变换器和多层感知机，实现了模型对细微局部变化和长距离语义上下文的捕捉，同时降低了手工网络设计的成本。为支持高效训练，AutoNAD引入了跨权重共享策略，加速了超网络的收敛并提高了子网络性能。此外，还集成了一种可搜索的多级特征聚合模块（MFAM），以增强多尺度特征学习。论文还考虑了运行效率，引入了延迟感知先验来指导高效架构的选择。
### Conclusion
AutoNAD在三个工业缺陷数据集上进行了验证，并进一步应用于缺陷成像和检测平台。相关代码已公开。通过引入跨权重共享策略和多级特征聚合模块，AutoNAD能够更好地解决工业缺陷检测中的挑战，同时提高模型效率。
## 587. `cs.CV` - 在全尺度下愚弄立体匹配：自动驾驶场景中的双目深度估计物理对抗攻击 [PDF](https://arxiv.org/pdf/2511.14386), [HTML](https://arxiv.org/abs/2511.14386)
### Authors
Kangqiao Zhao,Shuo Huai,Xurui Song,Jun Luo
### Background
尽管深度神经模型在自动驾驶感知中表现出色，但对抗样本攻击仍然是一个重大威胁。现有研究主要关注二维贴片攻击，而针对基于双目立体视觉的深度估计模型的物理对抗攻击研究相对较少。
### Innovation
本文提出了针对自动驾驶场景的立体匹配模型首次使用的纹理增强物理对抗攻击方法。该方法采用全局伪装纹理的三维PAE，具有跨不同视角的一致性，同时设计了一种新的三维立体匹配渲染模块，以解决立体相机的视差效应。此外，还设计了一种新颖的合并攻击，能够通过精细的PAE优化无缝融合目标，显著提升了攻击的隐蔽性和致命性。
### Conclusion
实验表明，所提出的PAE能够成功欺骗立体匹配模型生成错误的深度信息，展示了其在自动驾驶场景中的潜力。
## 588. `cs.CV` - 视觉优先，文本推理：ARC中的视觉-语言协同作用 [PDF](https://arxiv.org/pdf/2511.15703), [HTML](https://arxiv.org/abs/2511.15703)
### Authors
Beichen Zhang,Yuhang Zang,Xiaoyi Dong,Yuhang Cao,Haodong Duan,Dahua Lin,Jiaqi Wang
### Background
抽象推理能力对于前沿基础模型（如GPT-5和Grok 4）来说依然是一个未解的核心问题。现有模型无法从少量示例中推断出结构化的转换规则，这被视作人类智能的关键特征之一。ARC-AGI数据集旨在测试这种能力，要求模型进行概念规则归纳，并应用于新的任务。现有的大多数方法过分强调文本推理，忽视了人类解题时依赖视觉抽象的重要性。
### Innovation
本文提出了一种协同策略：(1) 视觉-语言协同推理（VLSR），将ARC-AGI分解为模态对齐的子任务；(2) 模态转换自我纠正（MSSC），利用视觉验证文本推理以进行内在错误纠正。实验结果表明，与纯文本基线相比，该方法在多样化的前沿模型和多个ARC-AGI任务上成效提升达4.33%。研究发现整合视觉抽象与语言推理是未来基础模型实现可推广的人类智能的关键一步。
### Conclusion
该研究认为，将视觉抽象与语言推理统一起来是实现基础模型具备可推广的人类智能的关键步骤。
## 589. `cs.CV` - DensiCrafter: 物理约束条件下自支撑空心结构的生成与制造 [PDF](https://arxiv.org/pdf/2511.09298), [HTML](https://arxiv.org/abs/2511.09298)
### Authors
Shengqi Dang,Fu Chai,Jiaxin Li,Chao Yuan,Wei Ye,Nan Cao
### Background
随着3D生成模型的发展，可以从多模态输入（例如文本或图像）自动生成3D几何和纹理。然而，现有方法往往忽略了物理约束和制造可行性考虑。本研究关注3D设计的重量轻量化和自支撑性能。
### Innovation
本文提出了DensiCrafter框架，通过优化密度场生成重量轻且自支撑的3D空心结构。该方法使用Trellis生成的粗糙体素网格作为输入，将其解释为连续密度场进行优化，并引入了三个不同可导、物理约束且无需模拟的损失项。此外，质量正则化项惩罚不必要的材料，限制优化域保持外表面。该方法与基于Trellis的预训练模型无缝集成，无需改变架构。实验结果显示，本文方法在从文本到3D的任务中，材料质量最多可减少43%，并且相比现有先进技术，其稳定性更高，保持了高几何保真度。
### Conclusion
实际3D打印实验验证了DensiCrafter生成的空心设计可以可靠地制造并保持自支撑特性。
## 590. `cs.CV` - 基于高斯基古代适应性强度建模的点监督面部表情检测 [PDF](https://arxiv.org/pdf/2511.16952), [HTML](https://arxiv.org/abs/2511.16952)
### Authors
Yicheng Deng,Hideaki Hayashi,Hajime Nagahara
### Background
自动面部表情检测旨在识别未剪辑视频中的面部表情实例，对于面部表情分析至关重要。现有方法主要依赖于完全监督学习，并需要成本高、耗时的时空边界注释。
### Innovation
研究提出了点监督面部表情检测（P-FES），只需为每个实例提供一个时间戳注释即可进行训练。提出了一个独特的双分支框架：1. 引入高斯基古代适应性强度建模（GIM）模块，以适应不同强度的表情和中性帧的混淆问题，通过检测伪顶点帧、估计持续时间和构建实例级别的高斯分布，为表情帧分配软伪标记，以更可靠地监督强度；2. 设计类别感知的顶点分类分支，仅基于伪顶点帧区分宏观表情和微表情；3. 引入强度感知对比损失，通过对比中性帧与各种强度的表情帧来增强特征学习并抑制中性噪声。
### Conclusion
在SAMM-LV、CAS(ME)²和CAS(ME)³数据集上进行了广泛实验，证明了所提出的框架的有效性。
## 591. `cs.CV` - 免费的概率稳健性？重新审视训练基准 [PDF](https://arxiv.org/pdf/2511.01724), [HTML](https://arxiv.org/abs/2511.01724)
### Authors
Yi Zhang,Zheng Wang,Zhen Chen,Wenjie Ruan,Qing Guo,Siddartha Khastgir,Carsten Maple,Xingyu Zhao
### Background
现有研究主要集中在对抗鲁棒性（AR），这是通过检查确定性的对抗样本（AE）来评估模型在最差情况下的表现。与之不同，概率鲁棒性（PR）采用统计学视角，测量在随机扰动下预测正确性的概率。虽然PR被广泛认为是对AR的一个实用补充，但专门针对提高PR的训练方法仍然相对未被深入探索。
### Innovation
该研究引入了PRBench，这是第一个专注于评估不同鲁棒性训练方法对概率鲁棒性（PR）改进的基准。PRBench利用一系列全面的指标（包括准确率、PR和AR性能、训练效率和泛化误差）比较了最常用的对抗训练（AT）方法和概率鲁棒性（PR）目标训练方法。同时，提供了不同训练方法下PR性能的泛化误差的理论分析。
### Conclusion
实验结果表明，对抗训练方法在改善对抗鲁棒性和概率鲁棒性方面比专门针对概率鲁棒性的训练方法更具灵活性，但后者在泛化误差和干净准确率方面表现更佳。该研究还提供了一个包含222个模型的排行榜，这些模型在7个数据集和10个模型架构上进行了训练，可以在指定的网址访问。
## 592. `cs.CV` - 野生谈话表情视频的面部时间微动态分析进行被动痴呆筛查 [PDF](https://arxiv.org/pdf/2511.13802), [HTML](https://arxiv.org/abs/2511.13802)
### Authors
Filippo Cenacchi,Longbing Cao,Mitchell McEwan,Deborah Richards
### Background
现有的痴呆检测资源大多侧重于言语或剧本化访谈，这限制了其应用范围，并且依赖于言语和转录结果来预测痴呆风险。这使得痴呆的筛查更加聚焦在临床环境中，并且需要事先准备的言语或文本材料。
### Innovation
本文提出了一种通过分析野生环境下面向摄像机的谈话者表情的微动态来进行痴呆筛查的方法。该方法通过对眨眼动态、小口部和下颌运动、眼球移动变化以及微妙的头部调整等面部时间微动态进行分析，可以在不依赖言语或文本的情况下筛选早期神经认知变化。开发了一个新数据集——野生面向摄像机谈话视频集(YT DemTalk)，包含300个视频，150个有自报痴呆症的和150个控制组，以用于测试模型和基准评估。作者通过实验发现，眼球不稳定性和嘴巴/下颌动态是最具信息量的线索，轻量级浅分类器可以实现较高的痴呆预测性能。
### Conclusion
该研究通过新型数据集和分析方法，成功地在无言语干预的条件下识别了痴呆的早期迹象，并在野生环境下验证了模型的有效性，为痴呆筛查提供了一种新的无创、大规模分析手段。
## 593. `cs.CV` - Video-R4：通过视觉沉思强化文本丰富的视频推理 [PDF](https://arxiv.org/pdf/2511.17490), [HTML](https://arxiv.org/abs/2511.17490)
### Authors
Yolo Y. Tang,Daiki Shimada,Hang Hua,Chao Huang,Jing Bi,Rogerio Feris,Chenliang Xu
### Background
理解文本丰富的视频需要阅读小型、短暂的文字提示，这些提示通常需要多次检查。然而，大多数视频问答模型依赖于固定帧的一次性感知，导致对细节证据的幻觉和失败。
### Innovation
提出了Video-R4（视觉沉思强化文本丰富的视频推理），该模型执行视觉沉思：迭代选择帧，放大信息丰富的区域，重新编码检索的像素并更新其推理状态。此外，还构建了两个数据集（Video-R4-CoT-17k用于监督实践，Video-R4-RL-30k用于强化学习），并提出了一种多阶段沉思学习框架，该框架逐步微调7B参数的语言模型，通过SFT和基于GRPO的RL学习原子和混合视觉操作。Video-R4-7B在M4-ViteVQA上取得了最先进的结果，并进一步应用于多页文档问答、幻灯片问答和通用视频问答，证明了迭代沉思是对准像素驱动的多模态推理的有效范式。
### Conclusion
Video-R4通过迭代的视觉沉思，实现了对准像素驱动的多模态推理，相比一次性感知的方法，能更准确地理解视频中的文本线索，尤其在细节处理上表现出色。这种新的学习框架在多种任务上的应用表明了其优越性。
## 594. `cs.CV` - One-Step Diffusion Transformer for Controllable Real-World Image Super-Resolution [PDF](https://arxiv.org/pdf/2511.17138), [HTML](https://arxiv.org/abs/2511.17138)
### Authors
Yushun Fang,Yuxiang Chen,Shibo Yin,Qiang Hu,Jiangchao Yao,Ya Zhang,Xiaoyun Zhang,Yanfeng Wang
### Background
近期基于扩散模型的实时图像超级分辨率（Real-ISR）研究取得了显著的感知质量，但保真度和可控性之间仍存在平衡问题：多步扩散模型表现出生成多样性差和随机性高，导致保真度低；而单步模型通过针对特定保真度进行微调，则丧失了控制灵活性。
### Innovation
本文提出了一种名为ODTSR（One-Step Diffusion Transformer for Real-World Image Super-Resolution）的一步扩散变换模型，它结合了Qwen-Image的优点，同时考虑了保真度和可控性。ODTSR通过引入一个新的视觉流来调整噪声（Control Noise）处理低质量图像（LQ），并使用无差异噪声（Prior Noise）形成Noise-hybrid Visual Stream (NVS)设计。此外，ODTSR采用了Fidelity-aware Adversarial Training (FAA)来提高可控性并实现一次推理。
### Conclusion
广泛的实验表明，ODTSR不仅在通用的Real-ISR任务上达到了最先进的（SOTA）性能，还在诸如中文字符的现实场景中的图像超级分辨率（STISR）等具有挑战性的场景中实现了提示可控性，在无需特定数据集进行训练的情况下也表现出色。代码可在[该链接]获取。
## 595. `cs.CV` - ConceptGuard: 通过多模态风险检测在文本和图像到视频生成中的主动安全性 [PDF](https://arxiv.org/pdf/2511.18780), [HTML](https://arxiv.org/abs/2511.18780)
### Authors
Ruize Ma,Minghong Cai,Yilei Jiang,Jiaming Han,Yi Feng,Yingshui Tan,Xiaoyong Zhu,Bo Zhang,Bo Zheng,Xiangyu Yue
### Background
近年来，视频生成模型的发展使得能够从结合了文本和图像的多模态提示生成高质量的视频。尽管这种系统增强了可控性，但它们也引入了新的安全风险，因为有害内容可以来自单独的模态或它们的交互。现有的安全方法通常是文本的，需要了解风险类别，或作为生成后的审计员工作，难以主动缓解这种组合的多模态风险。
### Innovation
本文提出了ConceptGuard，一个统一的保护框架，旨在主动检测和缓解多模态视频生成中的不安全语义。ConceptGuard分为两个阶段：首先，对比检测模块通过将融合图像-文本输入投影到结构化概念空间来识别潜在的安全风险；其次，语义抑制机制通过干预提示的多模态条件来引导生成过程远离不安全的概念。
### Conclusion
在两大基准测试上的全面实验表明，ConceptGuard在风险检测和安全视频生成方面始终优于现有基线，达到了最先进的效果。我们的代码可在[此链接]获得。
## 596. `cs.CV` - ReMatch: 提升多模态检索表示的方法 [PDF](https://arxiv.org/pdf/2511.19278), [HTML](https://arxiv.org/abs/2511.19278)
### Authors
Qianying Liu,Xiao Liang,Zhiqiang Zhang,Zhongfei Qing,Fengfan Zhou,Yibo Chen,Xu Tang,Yao Hu,Paul Henderson
### Background
以往的方法将大规模语言模型（MLLM）视为简单的编码器，忽视了其生成能力，未能充分利用其组合推理和世界知识。这些方法在多模态检索任务中表现不足。
### Innovation
ReMatch框架利用MLLM的生成能力，通过端到端训练，在生成式匹配阶段使用MLLM自回归地决定多视图输入（包括原始数据及其自身投影嵌入）的相关性。此外，通过使用多个可学习的标记来增强每个输入，生成细粒度且互斥的上下文嵌入，同时保持较低的推理成本。在大规模多模态嵌入基准（MMEB）数据集上，ReMatch展现了比现有方法更强大的零样本泛化能力，实现了新的性能里程碑。
### Conclusion
ReMatch通过多模态匹配增强表示，证明了其在五大数据集上的鲁棒性和转移学习能力。实验结果表明，ReMatch在大规模多模态嵌入基准上的表现优于现有方法。
## 597. `cs.CV` - Agent0-VL：探索工具集成视觉语言推理的自我进化的代理 [PDF](https://arxiv.org/pdf/2511.19900), [HTML](https://arxiv.org/abs/2511.19900)
### Authors
Jiaqi Liu,Kaiwen Xiong,Peng Xia,Yiyang Zhou,Haonian Ji,Lu Feng,Siwei Han,Mingyu Ding,Huaxiu Yao
### Background
视觉-语言代理在多种跨模态推理任务中取得了显著进展，但其学习仍受到人类标注监督的限制。近年来，自我奖励的方法试图通过使模型能够自我批评或提供自我奖励来克服这一限制，但纯粹基于文本的自我评估难以验证复杂的视觉推理步骤，并且常常遭受评估幻觉。
### Innovation
本文提出了一种自我进化的视觉语言代理Agent0-VL，该代理通过工具集成推理实现了持续改进。Agent0-VL将工具使用不仅纳入推理，还纳入自我评估和自我修复中，使模型能够通过证据导向的分析进行反思、验证和推理改进。Agent0-VL统一了视觉语言大模型中的两种协同角色：解决者和验证者，解决者执行多轮工具集成推理，验证者通过工具导向批评生成结构化反馈和精细的自我奖励。
### Conclusion
通过零外部奖励演化，Agent0-VL没有使用任何人类标注或外部奖励模型，实现了持续自我改进。在几何问题解决和视觉科学分析实验中，Agent0-VL相较于基础模型实现了12.5%的改进，代码已开源。
## 598. `cs.CV` - GFT-GCN：基于频谱扩散的隐私保护3D面部网格识别 [PDF](https://arxiv.org/pdf/2511.19958), [HTML](https://arxiv.org/abs/2511.19958)
### Authors
Hichem Felouat,Hanrui Wang,Isao Echizen
### Background
3D面部识别通过捕捉面部几何提供了鲁棒的生物特征识别解决方案，能够应对光照变化、姿态改变和呈现攻击。它的防欺骗能力使其适合高安全应用，但存储的生物特征模板保护依然是关键问题。
### Innovation
提出了GFT-GCN，这是一种结合频谱图学习和基于扩散的模板保护的隐私保护3D面部识别框架，通过引入频谱扩散机制，生成不可逆、可再生和无法链接的模板，确保原始生物特征数据从不离开客户端设备。该方法利用图傅里叶变换（GFT）和图卷积网络（GCN）从3D面部网格中提取紧凑且具有鉴别性的频谱特征。
### Conclusion
在BU-3DFE和FaceScape数据集上的实验表明，GFT-GCN具有高识别准确性和对抗重建攻击的强大能力，有效地平衡了隐私和性能，在安全的3D面部认证方面提供了实用的解决方案。
## 599. `cs.CV` - 关注关键区域：无需训练的局部放大模型 [PDF](https://arxiv.org/pdf/2511.19917), [HTML](https://arxiv.org/abs/2511.19917)
### Authors
Qin Ren,Yufei Wang,Lanqing Guo,Wen Zhang,Zhiwen Fan,Chenyu You
### Background
扩散模型已成为文本到图像生成的主导范式，而测试时缩放（TTS）通过在推断时分配更多计算资源进一步提高了质量。然而，现有的TTS方法在全图像级别进行操作，忽略了图像质量在空间上往往不均匀的事实，导致在已经满意区域上不必要的计算，并且在局部缺陷修复方面不足。
### Innovation
本文探索了一种新的方向——局部TTS，该方法能适应性地重新采样缺陷区域，同时保留高质量区域，从而大大减少了搜索空间。提出的LoTTS框架是第一个完全不需要训练的局部TTS框架。LoTTS通过质量感知提示下的交叉注意力和自我注意力信号对比来准确识别缺陷区域并细化它们成连贯的掩膜。对于一致性，LoTTS仅扰动缺陷区域并局部去噪，确保修正部分保持完整，其余图像不受干扰。
### Conclusion
在SD2.1、SDXL和FLUX上的大量实验表明，LoTTS在保持全局保真度的同时，改善了局部质量，并将GPU成本降低了2-4倍，相较于Best-of-N采样。这些发现证实了局部TTS在推断时放大扩散模型方面具有前景的新方向。
## 600. `cs.CV` - EmoFeedback^2: 基于LVLM的奖励和文本反馈强化的连续情绪图像生成 [PDF](https://arxiv.org/pdf/2511.19982), [HTML](https://arxiv.org/abs/2511.19982)
### Authors
Jingyang Jia,Kai Shu,Gang Yang,Long Xing,Xun Chen,Aiping Liu
### Background
连续情感图像生成（C-EICG）因其能够产生与用户描述和连续情感值对齐的图像而迅速发展。现有的方法缺乏从生成图像中反馈情感的能力，限制了情感连续性的控制。另外，他们简单地将情感与根据文本粗略生成的图像进行对齐，不能根据图像内容自适应调整情感提示，导致情感准确性不足。
### Innovation
本文提出了一种新颖的生成-理解-反馈强化范式（EmoFeedback^2），通过调优的大视觉语言模型（LVLM）的推理能力提供奖励和文本反馈，用于生成高质量且具备连续情感的图像。具体而言，引入了情感提示的奖励反馈策略，使LVLM评估生成图像的情感价值，并计算与目标情感的奖励，指导生成模型的强化调优，增强图像的情感连续性。此外，设计了一种自我提升的文本反馈框架，使LVLM迭代分析生成图像的情感内容，并自适应地生成改进下一轮提示的建议，实现精细节度的情感准确性。
### Conclusion
广泛的实验结果表明，我们的方法能够有效生成具备所需情感的高质量图像，并在我们自定义的数据集中超越现有的最先进的方法。相关代码和数据集将很快发布。
## 601. `cs.CV` - 恢复流动：基于退化掩膜的流动匹配图像恢复 [PDF](https://arxiv.org/pdf/2511.20152), [HTML](https://arxiv.org/abs/2511.20152)
### Authors
Arnela Hadzic,Franz Thaler,Lea Bogensperger,Simon Johannes Joham,Martin Urschler
### Background
尽管生成模型如扩散模型在图像生成方面表现出色，它们存在采样时间长的问题，并且难以灵活设计生成轨迹。为了解决这些问题，流动匹配作为一种生成方式崭露头角，它在保持高质量图像生成的同时缩短了采样时间，提供了更加灵活的轨迹设计能力。当前利用流动模型的方法虽已显示出了潜在的应用价值，但仍有处理时间长或结果过度平滑的问题。
### Innovation
本文提出了一种名为Restora-Flow的方法，引入了退化掩膜指导的流动匹配采样，并结合了一条轨迹校正机制，以确保与退化输入的一致性，进一步提高了图像恢复的质量，同时减少了处理时间。
### Conclusion
在多种基于掩膜退化的图像恢复任务（如修复、超分辨率和去噪）中，本文方法展示了优于扩散和其他基于流动匹配的基准方法的感知质量及处理时间。
## 602. `cs.CV` - 连续流中基于扩散噪声优化的序列自适应视频预测 [PDF](https://arxiv.org/pdf/2511.18255), [HTML](https://arxiv.org/abs/2511.18255)
### Authors
Sina Mokhtarzadeh Azar,Emad Bahrami,Enrico Pallotta,Gianpiero Francesca,Radu Timofte,Juergen Gall
### Background
本文研究了基于扩散的视频预测模型，这些模型旨在预测连续视频流中的未来视频帧。模型在持续观察新的训练样本的同时进行预测，希望通过这种方式提高预测性能。
### Innovation
提出了一种连续适应预训练扩散模型的方法，该方法在推理过程中优化扩散噪声，同时保持模型参数不变。这种方法称为序列自适应视频预测与扩散噪声优化（SAVi-DNO）。通过一种新的评估设置，在Ego4D数据集上验证这种方法，重点关注长连续视频的同时适应与评估。
### Conclusion
实验结果表明，与长时间视频相比，该方法在Ego4D、OpenDV-YouTube、UCF-101和SkyTimelapse视频上使用FVD、SSIM和PSNR度量标准实现了更好的性能，证明了SAVi-DNO的有效性。
## 603. `cs.CV` - TimeViper: 一种用于高效长视频理解的混合Mamba-Transformer 视觉语言模型 [PDF](https://arxiv.org/pdf/2511.16595), [HTML](https://arxiv.org/abs/2511.16595)
### Authors
Boshen Xu,Zihan Xiao,Jiaze Li,Jianzhong Ju,Zhenbo Luo,Jian Luan,Qin Jin
### Background
长视频的理解需要高效的模型架构以及处理长时间上下文的有效机制。现有的视觉语言模型在处理长视频时面临着巨大的挑战，包括模型效率和上下文理解能力之间的权衡。
### Innovation
TimeViper引入了一种混合Mamba-Transformer骨干网络，结合了状态空间模型的高效性和注意力机制的表达力，揭示了视觉到文本的信息聚合现象，并提出了一种Token信息传递模块TransV来转移和压缩视觉Token，同时保持多模态理解能力，从而能够处理超过10000帧的小时长视频。此外，还分析了Mamba和Transformer层的注意力行为，为其混合模型的解释提供了新的见解。
### Conclusion
这项工作代表了在开发、解释和压缩混合Mamba-Transformer架构方面的一个初步步骤，展示了TimeViper与最新模型竞争的同时，增加了帧数。
## 604. `cs.CV` - 基于视觉语言的半监督医学图像分割基础模型 [PDF](https://arxiv.org/pdf/2511.19759), [HTML](https://arxiv.org/abs/2511.19759)
### Authors
Jiaqi Guo,Mingzhen Li,Hanyu Su,Santiago López,Lexiaozi Fan,Daniel Kim,Aggelos Katsaggelos
### Background
半监督学习（SSL）已成为医学图像分割的有效范式，减少了对外科专家详细标注的依赖。同时，视觉语言模型（VLMs）在跨多种视觉领域展现了强大的泛化能力和少量样本学习能力。研究集成VLM增强的分割基础模型，引入Visual-Language Enabled Semi-supervised Segmentation Assistant (VESSA) 进入SSL框架中，使得分割模型能够在有限标记数据下模拟学习。
### Innovation
该研究提出了VESSA方法，通过结合VLM实现半监督医学图像分割的改进。第一阶段，利用模板库进行训练，第二阶段将其集成到先进的SSL框架中，实现学生模型和VESSA之间的动态互动，提高了分割的准确性和泛化能力。
### Conclusion
在多种分割数据集和领域进行的广泛实验表明，VESSA增强的SSL模型显著提高了分割准确性，即使在标注数据极为有限的条件下也能超越最先进的基线模型。
## 605. `cs.CV` - 无监督代理视觉定位：基于代理推理的训练 [PDF](https://arxiv.org/pdf/2511.19516), [HTML](https://arxiv.org/abs/2511.19516)
### Authors
Liqin Luo,Guangyao Chen,Xiawu Zheng,Yongxing Dai,Yixiong Zou,Yonghong Tian
### Background
视觉接地任务旨在将文本查询与图像中的特定区域相连，这对于视觉-语言整合至关重要。现有方法通常依赖于大量任务特异性注释和微调，限制了它们在新颖或分布外场景中的有效泛化能力。
### Innovation
我们提出了GroundingAgent，一种无需任务特定微调的新颖代理视觉接地框架。GroundingAgent 采用结构化的迭代推理机制，结合预训练的开放式词汇对象检测器、多模态大语言模型 (MLLM) 和大语言模型 (LLM)，通过联合语义和空间分析逐步细化候选区域。GroundingAgent 在广泛使用的基准测试 (RefCOCO, RefCOCO+, RefCOCOg) 上实现了无监督的平均零样本接地准确率为 65.1%，并且仅通过替换 MLLM 生成的描述为原始查询文本，在选择阶段的准确率达到约 90%，几乎与监督性能相匹配。
### Conclusion
GroundingAgent 也提供了强大的可解释性，透明地展示了每个推理步骤，并为决策过程提供了清晰的见解。
## 606. `cs.CV` - Pistachio：迈向合成、均衡且长格式视频异常基准 [PDF](https://arxiv.org/pdf/2511.19474), [HTML](https://arxiv.org/abs/2511.19474)
### Authors
Jie Li,Hongyi Cai,Mingkang Dong,Muxin Pu,Shan You,Fei Wang,Tao Huang
### Background
现有的视频异常检测（VAD）基准和视频异常理解（VAU）难以全面评估真实世界性能，因为基准数据集在场景多样性、异常覆盖平衡性和时间复杂度方面存在不足。此外，VAU需要深层次的语义和因果推理，但其大规模的手动标注工作量使得难以进行基准测试。
### Innovation
Pistachio提出了一个新的VAD/VAU基准，完全通过带有控制的生成性管道构建。利用最近的视频生成模型进展，Pistachio能够精确控制场景、异常类型和时间叙述，有效地消除互联网收集数据集带来的偏见和限制。Pistachio的生成流程结合了场景条件下的异常分配、多步故事情节生成和时间一致的大规模合成策略。这些策略产生41秒的视频并带有最少的人工干预。
### Conclusion
广泛的实验展示了Pistachio的规模、多样性和复杂性，揭示了现有方法的新挑战，并激发了对未来动态和多事件异常理解研究的进一步兴趣。
## 607. `cs.CV` - SKEL-CF: 自顶向下生物学骨架和拓扑网恢复 [PDF](https://arxiv.org/pdf/2511.20157), [HTML](https://arxiv.org/abs/2511.20157)
### Authors
Da Li,Jiping Jin,Xuanlong Yu,Wei Liu,Xiaodong Cun,Kai Chen,Rui Fan,Jiangang Kong,Xi Shen
### Background
3D人体模型如SMPL在人体姿态和形态估计方面取得了显著进展，但其简化的人体运动学限制了生物力学的现实感。最近提出的SKEL模型通过重新绑定SMPL到解剖学准确的骨架解决了这一限制，但直接估计SKEL参数仍然具有挑战性，因为训练数据有限，视角模糊以及人体关节复杂性。现有的方法不能有效应对深度和尺度模糊性，这阻碍了准确的人体运动分析。
### Innovation
本文提出了一种自顶向下的SKEL参数估计框架SKEL-CF，采用了基于变换器的编码器-解码器架构，首先预测粗略的相机和SKEL参数，然后在后续层中逐步细化它们。还引入了一个与4DHuman数据集兼容的SKEL对齐版本4DHuman-SKEL，提供了高质量的训练数据。此外，通过明确地将相机建模纳入SKEL-CF管道中，以减少深度和尺度的模糊性，并在不同视角下证明其重要性。实验结果表明，SKEL-CF在挑战性的MOYO数据集上表现优于现有的SKEL基最佳方法HSMR，建立了SKEL-CF作为人体运动分析中可扩展且解剖学忠实的基础。
### Conclusion
SKEL-CF为生物力学和计算机视觉之间的桥梁搭建了可扩展且解剖学忠实的人体运动分析框架，解决了参数估计和生物力学现实感的问题。未来研究将专注于进一步提高模型的鲁棒性和准确性。
## 608. `cs.CV` - DiffSeg30k：用于局部AI生成内容检测的多轮扩散编辑基准 [PDF](https://arxiv.org/pdf/2511.19111), [HTML](https://arxiv.org/abs/2511.19111)
### Authors
Hai Ci,Ziheng Peng,Pei Yang,Yingxin Xuan,Mike Zheng Shou
### Background
现有的AIGC检测基准主要集中在整个图像的分类上，忽视了基于扩散的编辑的定位问题。现有的检测方法通常只能识别出整个图像的虚假内容，而不能精确地定位到局部的修改区域。因此，需要一个新的基准数据集来支持细粒度检测，以促进此项研究的发展。
### Innovation
本文提出了一个新的数据集DiffSeg30k，旨在支持细粒度的AIGC检测。该数据集包括1) 野外观测图像，2) 多样化的扩散模型，3) 多步骤编辑，4) 与视觉语言模型结合的自动生成上下文感知提示的编辑场景。DiffSeg30k将AIGC检测从二分类推向了语义分割，使得编辑定位和编辑模型识别成为可能。此外，该数据集还展示了分割模型在识别扩散编辑上的强大性能。
### Conclusion
DiffSeg30k数据集展示了分割方法的潜力和局限性，为未来的研究提供了重要的基础。基于此数据集的实验结果表明，尽管分割模型主要用于像素级定位，但在识别扩散编辑方面表现出色，对未来的研究具有重大意义。数据集已发布，供研究人员使用。
## 609. `cs.CV` - DWFF-Net : 具有自适应动态权重的多尺度农田生态系统生境识别方法 [PDF](https://arxiv.org/pdf/2511.11659), [HTML](https://arxiv.org/abs/2511.11659)
### Authors
Kesong Zheng,Zhi Song,Peizhou Li,Shuyi Yao,Zhenxing Bian
### Background
当前缺乏统一的农田生态系统生境分类系统，现有生境类型覆盖不全面，且现有模型难以有效融合语义和纹理特征，导致多尺度生境（如大田地块和微生境）的分割精度不足和边界模糊。
### Innovation
开发了一个包含15类农田系统生境的全面注释超高分辨率遥感图像数据集，并提出一种动态加权特征融合网络（DWFF-Net）。该模型使用冻结参数的DINOv3作为编码器提取基础特征，通过分析不同类别图像和特征图之间的关系，引入数据级自适应动态权重策略进行特征融合。该模型采用了一个动态权重计算网络来实现多层特征的全面整合，并采用了一种混合损失函数进行模型训练。实验结果表明，该模型的平均交并比（mIoU）达到69.79%，F1分数达到80.49%，分别比基线网络高出2.1%和1.61%，进一步实验证明多层特征融合的有效性。
### Conclusion
该研究建立了基于自适应多层特征融合的农田系统生境识别框架，实现了低成本的亚米级精度生境地图绘制，并为农田景观精细化生境监测提供了坚实的技术支持。
## 610. `cs.CV` - CrossEarth-Gate：跨域遥感语义分割的基于Fisher信息引导的自适应调优引擎 [PDF](https://arxiv.org/pdf/2511.20302), [HTML](https://arxiv.org/abs/2511.20302)
### Authors
Shilei Cao,Ziyang Gong,Hehai Lin,Yang Liu,Jiashun Cheng,Xiaoxing Hu,Haoyuan Liang,Guowen Li,Chengwei Qin,Hong Cheng,Xue Yang,Juepeng Zheng,Haohuan Fu
### Background
在遥感（RS）领域，参数高效调优（PEFT）已成为激活基础模型通用表示能力的关键方法，以适应下游任务。然而，现有的专用PEFT方法在应用于大规模地球观测任务时经常失效，因为这些方法难以有效处理遥感数据固有的多样性和不可预测的领域差距（例如，空间、语义和频率偏移）。
### Innovation
我们提出了CrossEarth-Gate，引入了两个主要贡献：首先，建立了一个综合的RS模块工具箱，以应对多样化的领域差距，包含空间、语义和频率模块。其次，开发了一种基于Fisher信息引导的自适应选择机制，在这一工具箱上操作。该选择机制利用Fisher信息来量化每个模块的重要性，通过测量其对任务特定梯度流的贡献，动态激活最关键的模块，以最大化适应效果和效率。
### Conclusion
通过综合实验验证了我们方法的有效性和通用性，其中CrossEarth-Gate在16个跨域基准测试中实现了遥感语义分割最先进的性能。该工作的代码将开源。
## 611. `cs.CV` - BRIC：测试时融合运动计划和物理控制 [PDF](https://arxiv.org/pdf/2511.20431), [HTML](https://arxiv.org/abs/2511.20431)
### Authors
Dohun Lim,Minji Kim,Jaewoon Lim,Sungchan Kim
### Background
文章描述了一个叫BRIC的新颖测试时适应（TTA）框架，用于解决基于扩散模型的运动规划器与基于强化学习的物理控制之间的执行偏差问题。尽管扩散模型能够生成多样化且富有表现力的运动，但由于这些模型生成的运动往往缺乏物理合理性，导致在模拟过程中出现执行偏差。
### Innovation
BRIC通过动态地在测试时调整物理控制器来解决这个问题，同时使用损失函数来减轻灾难性遗忘，从而保持预训练的技能。此外，BRIC引入了一种轻量级的测试时引导机制，可以在信号空间中引导扩散模型而无需调整其参数。这双管齐下确保了在不同环境中的长期执行一致性，并且具有高效性能。
### Conclusion
我们在多种长期任务上验证了BRIC的有效性，包括运动合成、障碍物规避和人-场景交互任务，BRIC在所有任务上都达到了当前最佳表现。
## 612. `cs.CV` - VGGTFace：野外一致面拓扑面部几何重建 [PDF](https://arxiv.org/pdf/2511.20366), [HTML](https://arxiv.org/abs/2511.20366)
### Authors
Xin Ming,Yuxuan Han,Tianyu Huang,Feng Xu
### Background
在数字化身创建管道中，重建拓扑一致的面部几何形状至关重要。现有方法要么需要繁琐的手动努力，要么无法泛化到野外数据，要么受到3D Morphable Models表达能力的限制。
### Innovation
我们提出了一种名为VGGTFace的自动方法，该方法创新性地将3D基础模型VGGT应用于从日常用户拍摄的多视角野外图像中重建一致的面部几何形状。通过利用VGGT，我们的方法自然继承了大规模训练和点云表示的强大泛化能力和表达力。为了解决如何从VGGT重建拓扑一致网格的问题，我们增加了Pixel3DMM以注入拓扑信息。
### Conclusion
我们的方法可以在10秒内对单个NVIDIA RTX 4090单卡上的16视图实现高质量重建。实验表明，该方法在基准测试上取得了最先进的结果，并且在野外数据上的泛化能力令人印象深刻。
## 613. `cs.CV` - 三维思考：人工智能在野外的类人视觉搜索 [PDF](https://arxiv.org/pdf/2511.20351), [HTML](https://arxiv.org/abs/2511.20351)
### Authors
Heyang Yu,Yinan Han,Xiangyu Zhang,Baiqiao Yin,Bowen Chang,Xiangyu Han,Xinhao Liu,Jing Zhang,Marco Pavone,Chen Feng,Saining Xie,Yiming Li
### Background
人类依赖头部（cephalomotor）和眼睛（oculomotor）的协同控制来高效地在360°环境中搜索视觉信息。现有的视觉搜索方法大多局限于静态图像，并忽视了物理实体与其与三维世界的互动。如何开发出能够绕过现实世界硬件限制、与人类效率相当的基于体态的视觉搜索智能体？该研究提出了类人视觉搜索的概念，通过让类人代理主动旋转头部来搜索沉浸式世界的物体或路径（通过360°全景图表示）。为了研究视觉拥挤的真实世界场景，研究人员构建了H* Bench基准测试，超越了家庭场景，加入了火车、大型零售场所、城市的街道和公共机构等更具挑战性的户外场景，要求高水平的视觉空间推理能力。实验结果显示顶级商业模型在物体和路径搜索方面的成功率仅为约30%，这表明了任务的难度。
### Innovation
该研究提出的类人视觉搜索方法不仅考虑了人体的物理动作，而且通过360°全景图像构建了H* Bench基准，更贴近真实世界复杂场景。研究中使用了后训练技术改进了开源模型Qwen2.5-VL，在物体搜索和路径搜索方面取得了显著的性能提升。同时，研究指出路径搜索内部的高级空间常识需求，揭示了这一任务的固有难点
### Conclusion
该研究证明了可以设计出适合日常生活的大型语言模型代理（MLLM），尽管取得了进展，但仍然面临着巨大的挑战。尤其是路径搜索展示了高级空间常识的需求，增加了构建能在日常生活中无缝集成的代理的难度。
## 614. `cs.CV` - CroMe：使用跨模态三变换器和度量学习的多模态假新闻检测 [PDF](https://arxiv.org/pdf/2501.12422), [HTML](https://arxiv.org/abs/2501.12422)
### Authors
Eunjee Choi,Junhyun Ahn,XinYu Piao,Jong-Kook Kim
### Background
近年来，多模态假新闻检测受到了越来越多的关注。现有的方法依赖于独立编码的单模态数据，并且忽视了利用高级技术捕获跨模态相似性和内部模态关系的优势。
### Innovation
提出了跨模态三变换器和度量学习的多模态假新闻检测方法（CroMe），通过Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models (BLIP2)作为编码器来捕捉详细的文本、图像和图像-文本表示。度量学习模块利用代理锚点方法来捕获内部模态关系，而特征融合模块则使用跨模态和三变换器进行有效的集成。
### Conclusion
实验表明，CroMe 在多模态假新闻检测方面表现出色。
## 615. `cs.CV` - 比较生成学习方法在湍流代理中的应用 [PDF](https://arxiv.org/pdf/2411.16417), [HTML](https://arxiv.org/abs/2411.16417)
### Authors
Claudia Drygala,Edmund Ross,Francesca di Mare,Hanno Gottschalk
### Background
在计算流体动力学中，数值模拟湍流流动是一个重大挑战，由于其复杂性和高计算成本，高分辨率技术如直接数值模拟（DNS）和大涡模拟（LES）通常在计算上不可行，尤其是对于技术相关的复杂问题。近年来，机器学习，特别是生成概率模型的发展为替代湍流提供了有前景的解决方案。
### Innovation
本研究通过比较变分自编码器（VAE）、深度卷积生成对抗网络（DCGAN）和去噪扩散概率模型（DDPM）三种生成模型来模拟固定圆柱体周围的冯卡门涡街和实验条件下圆柱阵列尾流的湍流流动。研究发现DDPM和DCGAN能够有效地复制所有的流动分布，表明它们可以作为高效的湍流代理工具。
### Conclusion
研究结果表明，尽管DDPM和DCGAN在训练过程中存在局限性（如模式崩溃等问题），但它们在推理速度和训练时间上更快，并且需要较少的数据进行训练。相比之下，VAE虽然能快速训练但生成的样本效果不佳，而DDPM则在这方面表现更慢。
## 616. `cs.LG` - 跨被试EEG解码的原型引导非样本持续学习 [PDF](https://arxiv.org/pdf/2511.20696), [HTML](https://arxiv.org/abs/2511.20696)
### Authors
Dan Li,Hye-Bin Shin,Yeon-Woo Choi
### Background
由于电生理图（EEG）信号在不同个体之间存在显著差异，先前习得的知识在引入新的被试时经常会受到覆盖。当前的研究主要依赖于存储已见过被试的历史数据，作为重放缓冲区来防止遗忘。然而，隐私问题或记忆限制使得保持这些数据变得不切实际。
### Innovation
提出了一种原型引导的非样本持续学习（ProNECL）框架，该框架可以在无需访问任何历史EEG样本的情况下保存先前的知识。ProNECL通过每个被试构建类级原型来总结具有区分性的表示，并通过跨被试特征对齐和知识蒸馏逐步对新的特征空间进行对齐，从而实现了知识保留和适应性的平衡。
### Conclusion
在BCI竞赛IV 2a和2b数据集上验证了我们的框架，该框架在跨被试持续EEG解码任务中表现出色，有效平衡了知识保留和适应性。
## 617. `cs.CV` - MeshCone：基于二次锥规划的几何约束网格优化 [PDF](https://arxiv.org/pdf/2412.08484), [HTML](https://arxiv.org/abs/2412.08484)
### Authors
Alexander Valverde
### Background
现代网格生成管道，无论是基于学习的方法还是经典的方法，通常会生成需要后处理才能达到生产质量的输出。即使是高质量的输出，也往往需要完整的网格重构。这项工作旨在改进这类网格，提出了一种新的优化框架.MeshCone。
### Innovation
引入了一种基于凸优化的网格细化框架MeshCone，该框架能够利用参考几何来纠正变形或退化的网格。将问题形式化为二次锥规划问题，通过优化顶点位置并施加凸边长正则化来确保平滑度，从而实现了解析性的几何优化。
### Conclusion
MeshCone 能够在 56 种不同物体类别上表现出稳健的表现，与拉普拉斯光滑和其他未优化的基线相比，它能够提供更高的细化质量，同时保持亚秒级的推理时间。该方法特别适用于参考几何可用的应用场景，如模板网格生成的工作流、扫描到CAD对齐和资产生产管道中的质量保证。
## 618. `cs.CV` - LMLCC-Net：一种基于Hounsfield单位强度过滤的半监督深度学习模型，用于从CT扫描预测肺结节恶性程度 [PDF](https://arxiv.org/pdf/2505.06370), [HTML](https://arxiv.org/abs/2505.06370)
### Authors
Tasnia Binte Mamun,Adhora Madhuri,Nusaiba Sobir,Taufiq Hasan
### Background
肺癌是全球导致患者死亡的主要原因之一。早期在CT图像中检测恶性肺结节对于降低疾病死亡率和发病率具有重要意义。
### Innovation
该研究提出了LMLCC-Net，这是一种新颖的基于3D CNN的深度学习框架，采用Hounsfield Unit (HU) 基础强度过滤技术，考虑了良性与恶性结节在HU强度剖面上的显著差异。LMLCC-Net通过特征提取和多分支结构结合学习的HU强度过滤阶段，考虑强度模式和纹理预测恶性结节。此外，还提出了一种半监督学习方案来标注不明确的病例，并开发了一个轻量级模型用于结节分类。实验结果表明，LMLCC-Net实现了91.96%的分类准确率、92.94%的敏感性以及94.07%的曲线下面积，显著优于现有方法。
### Conclusion
LMLCC-Net在帮助放射科医生分类肺结节和改善患者护理方面具有显著的影响。
## 619. `cs.CV` - STARFlow-V：端到端视频生成建模中的规范流 [PDF](https://arxiv.org/pdf/2511.20462), [HTML](https://arxiv.org/abs/2511.20462)
### Authors
Jiatao Gu,Ying Shen,Tianrong Chen,Laurent Dinh,Yuyang Wang,Miguel Angel Bautista,David Berthelot,Josh Susskind,Shuangfei Zhai
### Background
规范流(NFs)是连续数据的端到端基于似然的生成模型，近年来在图像生成领域表现出积极进展。然而，在视频生成领域，由于时空复杂性和计算成本显著提高，最先进的系统几乎完全依赖于基于扩散的模型。
### Innovation
该研究引入了STARFlow-V，这是一种基于规范流的视频生成器，具有许多优点，如端到端学习、稳健的因果预测和原生似然估计。STARFlow-V采用全局-局部结构，在时空隐空间中运作，限制因果依赖关系在全局隐空间中，同时保留丰富的帧内相互作用，从而减轻了标准自回归扩散模型生成中的误差累积问题。此外还提出了流得分匹配方法，使模型具备轻量级的因果去噪器，以自回归的方式提高视频生成的一致性。为提高采样效率，STARFlow-V采用视频感知的雅可比迭代方案，将内部更新重新调整为并行化的迭代过程，而不破坏因果关系。该模型因具有可逆结构，能够原生支持文本到视频、图像到视频以及视频到视频生成任务。
### Conclusion
STARFlow-V 实现了高质量自回归视频生成，且在采样效率上与基于扩散的方法相比也具有竞争力，这表明规范流是构建世界模型的有希望的研究方向。
## 620. `cs.LG` - 使用重启后验采样的扩散逆问题求解 [PDF](https://arxiv.org/pdf/2511.20705), [HTML](https://arxiv.org/abs/2511.20705)
### Authors
Bilal Ahmed,Joseph G. Makin
### Background
逆问题在科学与工程中至关重要，目标是根据不完整或有噪声的测量来推断潜在的信号或状态。近期的研究使用扩散模型作为强大的隐式先验，因为它们能够捕捉复杂的数据分布。然而，现有的基于扩散的逆问题方法通常依赖于后验分布的强近似，需要通过评分网络进行代价高昂的梯度回传，或者局限于线性测量模型。
### Innovation
我们提出了基于重启后验采样的后验采样框架（RePS），该框架适用于线性和非线性逆问题。RePS 结合了基于重启的采样思想，并将其扩展到后验推理中，采用适用于任何可微测量模型的条件 ODE，并引入了一种简化重启策略来减少采样过程中累积的近似误差。与先前的方法相比，RePS 避免了评分网络中的梯度回传，大幅降低了计算成本。
### Conclusion
我们展示了 RePS 在多种逆问题中优于现有基于扩散的方法，无论是线性还是非线性情况，都实现了更快的收敛速度和更高的重建质量。
## 621. `cs.LG` - 大型语言模型中的主动切片发现 [PDF](https://arxiv.org/pdf/2511.20713), [HTML](https://arxiv.org/abs/2511.20713)
### Authors
Minhui Zhang,Prahar Ijner,Yoav Wald,Elliot Creager
### Background
大型语言模型（LLMs）在特定数据子集上经常表现出系统性的错误，这些错误子集被称为错误切片。例如，一个错误切片可以对应某个特定的人口统计信息，模型在识别与该人口统计信息有关的有毒评论时表现不佳。识别错误切片对于理解模型并改进其性能至关重要，但这也充满挑战。一种吸引人的方法是主动分组可能会属于同一个错误切片的错误，然后用有限的标注者访问来验证所选样本是否具有相同的模型错误模式。
### Innovation
本文将这种方法形式化为‘主动切片发现’，并在毒性分类问题上进行实证探索，以发现由人类定义的切片。分析不同特征表示和活跃学习算法的选择对主动切片发现效果的影响。结果表明，基于不确定性的活跃学习算法在多个切片上效果最佳，可以仅使用2%-10%可用切片成员信息获得竞争力的准确度，显著优于基线。
### Conclusion
研究发现，不确定性的活跃学习算法在多个切片上效果最好，能够以2%-10%的可用切片成员信息竞争性地达到高准确度，大幅超越基线方法，在理解和改进大型语言模型方面展示出巨大潜力。
## 622. `cs.LG` - 无数据知识蒸馏下的剪枝后准确率恢复 [PDF](https://arxiv.org/pdf/2511.20702), [HTML](https://arxiv.org/abs/2511.20702)
### Authors
Chinmay Tripurwar,Utkarsh Maurya,Dishant
### Background
深度神经网络（DNNs）的计算复杂度和内存占用可以通过剪枝大幅降低，但全球无结构剪枝通常会导致精度显著下降，通常需要在原始训练数据集上进行微调以恢复性能。在医疗保健或金融等隐私敏感领域，由于法规限制（如GDPR和HIPAA），部署后访问原始训练数据往往受到限制。因此，存在一个模型压缩与数据隐私之间的差距。
### Innovation
本文提出了一种无数据知识蒸馏框架，以在不访问任何真实数据点的情况下，通过逆向传输 batch normaliztion 统计信息来合成保护隐私的“梦想”图像，从而作为转移集将原始教师模型的知识传递给剪枝的学生网络，从而显著恢复剪枝后丢失的精度。
### Conclusion
实验结果表明，本文的方法在CIFAR-10数据集的各个架构中（ResNet，MobileNet，VGG）显著恢复了剪枝后的精度损失。
## 623. `cs.CV` - 在实际低资源设置中的改进视觉提示关键词定位 [PDF](https://arxiv.org/pdf/2409.06013), [HTML](https://arxiv.org/abs/2409.06013)
### Authors
Leanne Nortje,Dan Oneata,Gabriel Pirlogeanu,Herman Kamper
### Background
视觉提示关键词定位（VPKL）旨在在一个语音数据集中找到图像查询中描述的单词的出现。以往的研究表明，可以通过在配对图像和无标签语音上训练视觉引导的语音模型来实现VPKL，但所有实验都是在英语上进行的，并且使用转录来获取正负样本对以优化对比损失函数。在低资源语言环境中，如未书写语言如约鲁巴语，使用转录进行配对的方法不再适用。
### Innovation
本文提出了一种少样本学习方案来自动挖掘正负样本对，而无需转录数据，显著提升了在低资源设置中进行VPKL的可行性。并在约鲁巴语中进行了首个此类实验，尽管取得了不错的成绩，但在准确度上相较使用真实配对样本的性能有所下降。
### Conclusion
通过在约鲁巴语中进行VPKL实验，发现自动挖掘样本对的方法在低资源语言中性能大幅下降，这表明未来需要进一步改进算法以提高低资源环境中的性能。
## 624. `cs.CV` - 使用预训练变换器在对比和非对比CT图像上泛化心脏亚结构分割 [PDF](https://arxiv.org/pdf/2505.10855), [HTML](https://arxiv.org/abs/2505.10855)
### Authors
Aneesh Rangnekar,Nikhil Mankuzhy,Jonas Willmann,Chloe Choi,Abraham Wu,Maria Thor,Andreas Rimner,Harini Veeraraghavan
### Background
现有的基于AI的影像分割技术在应用于训练数据集外的不同病例时表现会下降。本研究旨在开发一种能够处理不同影像对比度和扫描位置的混合变压器卷积网络，以更好地用于肺癌和乳腺癌患者的心脏亚结构分割。
### Innovation
研究使用了一种混合变压器卷积网络来分割肺癌和乳腺癌患者的心脏亚结构。该网络能够处理对比度不同的CT扫描和不同的扫描位置，并且在经过预训练后，能有效减少所需的标注数据量。模型在保持与手动分割相当的剂量学轮廓的同时，对于对比度变化和定位变化展现出高度的鲁棒性，且与患者的年龄或体重指数关联较低。
### Conclusion
研究开发的平衡模型在各种影像协议和患者特点下均表现出了高度的几何和剂量学准确性，对于临床应用至关重要。与传统方法相比，该模型通过结合预训练和平衡的非对比和对比CT影像分布，显著减少了所需标注的数量，提高了分割的可靠性。
## 625. `cs.CV` - LightMem：轻量级和高效的增强记忆生成系统 [PDF](https://arxiv.org/pdf/2510.18866), [HTML](https://arxiv.org/abs/2510.18866)
### Authors
Jizhan Fang,Xinle Deng,Haoming Xu,Ziyan Jiang,Yuqi Tang,Ziwen Xu,Shumin Deng,Yunzhi Yao,Mengru Wang,Shuofei Qiao,Huajun Chen,Ningyu Zhang
### Background
尽管大型语言模型（LLMs）具有出色的性能，但在动态和复杂环境中，它们难以有效利用历史交互信息。现有记忆系统可以通过引入持久的信息存储、检索和利用机制，使LLMs超越无状态交互，但这些系统通常会带来显著的时间和计算成本。因此，研究一种在性能和效率之间取得平衡的记忆系统显得尤为重要。
### Innovation
本文介绍了一种名为LightMem的新记忆系统，它受到人类记忆模型的启发，分为三个互补阶段：第一阶段通过轻量级压缩快速过滤无关信息，并按主题分组；第二阶段的主题感知短时记忆将这些基于主题的群组进行整合和总结，以便有序访问；第三阶段的具有休眠期间更新的长时记忆采用离线过程，将巩固过程与在线推理脱钩。实验证明，LightMem在LongMemEval和LoCoMo上使用GPT和Qwen作为基础模型时，性能和效率均优于强基线，提高了QA的准确性，减小了总标记使用量和API调用次数。
### Conclusion
LightMem在未纯在线测试成本的情况下，实现了显著的标记使用量和API调用次数减少。论文提供的代码可在指定的链接中访问。
## 626. `cs.CV` - UniGame: 将统一多模态模型转变为自身的对手 [PDF](https://arxiv.org/pdf/2511.19413), [HTML](https://arxiv.org/abs/2511.19413)
### Authors
Zhaolong Su,Wang Lu,Hao Chen,Sharon Li,Jindong Wang
### Background
统一多模态模型（UMMs）在理解和生成方面都表现出色，并使用单一的架构。然而，UMMs 存在一个基本的不一致性：理解偏好紧凑的嵌入表示，而生成偏好重建丰富的表示。这种结构上的权衡导致了决策边界的不一致、跨模态一致性下降以及在分发性和对抗性转变下的脆弱性。
### Innovation
本文提出了UniGame，一个自对抗的后训练框架，直接针对上述不一致问题。通过在共享的标记接口应用轻量级扰动器，UniGame 使生成分支能够主动寻求并挑战脆弱的理解，并使模型本身成为自己的对手。实验结果表明，UniGame 显著提高了一致性 (+4.6%)，理解 (+3.6%)，生成 (+0.02) 以及对分布外和对抗性鲁棒性的提升 (+4.8% 和 +6.2% 在 NaturalBench 和 AdVQA 中)，且该框架对架构无关，引入不到 1% 的额外参数，与现有的后训练方法是互补的。
### Conclusion
这些结果表明，对抗性自玩游戏是一个增强未来统一多模态基础模型一致性和稳定性的普遍且有效的原则。官方代码可在以下链接获取：this https URL
## 627. `cs.LG` - 现代Hopfield网络的隐状态在Transformer中的作用 [PDF](https://arxiv.org/pdf/2511.20698), [HTML](https://arxiv.org/abs/2511.20698)
### Authors
Tsubasa Masumura,Masato Taki
### Background
基于霍普菲尔德网络（Hopfield network）的关联记忆模型和基于键值机制的自我注意已经被广泛应用于深度学习的记忆机制研究。现代霍普菲尔德网络（MHN）的状态更新规则在约化假设下的状态与Transformer的自我注意层是一致的。本文研究了MHN与自我注意之间的更广泛的关系。
### Innovation
通过引入现代霍普菲尔德网络的隐状态到自我注意机制中，提出了一个名为现代霍普菲尔德注意（MHA）的新自我注意机制。MHA机制可以从Transformer的输入层传递注意力权重到输出层，显著改善了Transformer内部的注意力权重。特别地，本文证明了MHA隐状态显著改善了深度Transformer中两个严重的问题——秩崩溃和标记均匀性问题。此外，实验证明了MHA可以在不增加训练参数的情况下系统地提高视觉Transformer或GPT的准确性。
### Conclusion
本文介绍了将现代霍普菲尔德网络的隐状态引入Transformer以改进其架构的新方法。新的自我注意机制不仅改善了Transformer的注意力权重，还在不增加额外训练参数的情况下提升了模型性能。这些结果表明霍普菲尔德网络可以为改进Transformer架构提供新的视角。
## 628. `cs.LG` - ST-PPO: 将稳定化剪裁偏差校正应用于多轮对话代理训练的脱策略近端策略优化 [PDF](https://arxiv.org/pdf/2511.20718), [HTML](https://arxiv.org/abs/2511.20718)
### Authors
Chenliang Li,Adel Elmahdy,Alex Boyd,Zhongruo Wang,Alfredo Garcia,Parminder Bhatia,Taha Kass-Hout,Cao Xiao,Mingyi Hong
### Background
多轮对话和逻辑推理任务中的大型语言模型（LLMs）训练通常采用PPO算法进行逐token级别的训练，但其表现往往不稳定且容易崩溃。分析发现主要原因是逐token的重要性采样与多轮对话的自然分阶段结构不匹配以及脱策略样本带来的不准确的优势估计。
### Innovation
本文提出了两种互补的稳定化技术——逐轮的重要性采样和剪裁偏差校正（通过减少不可靠的脱策略样本的重要性来规范化梯度），并结合这些技术发展了三种变体：Turn-PPO（仅采用逐轮采样）、S-PPO（将剪裁偏差纠正应用于逐token PPO）和ST-PPO（结合了逐轮采样和剪裁偏差校正）。通过实验，ST-PPO和S-PPO有效地防止了性能崩溃，维持了优化过程中的较低的剪裁比例，并且在各种多轮搜索任务中的表现优于标准的逐token PPO。
### Conclusion
这些结果表明将逐轮的重要性采样与剪裁偏差校正结合起来，能够提供一种实用的、可扩展的解决方案，用于多轮LLM代理训练以保持稳定性。
## 629. `cs.LG` - 基于扩散生成合成图预训练的Transformer模型在阿尔茨海默病预测中的应用 [PDF](https://arxiv.org/pdf/2511.20704), [HTML](https://arxiv.org/abs/2511.20704)
### Authors
Abolfazl Moslemi,Hossein Peyvandi
### Background
早期且准确地检测阿尔茨海默病（AD）对于及时干预和改善预后至关重要。然而，由于有限的标记数据、多站点异质性和类别不平衡，开发可靠的AD诊断机器学习（ML）模型具有挑战性。
### Innovation
提出了一种基于Transformer的诊断框架，结合了基于扩散的合成数据生成、图表示学习和迁移学习。该框架首先在真实世界的NACC数据集上训练一个条件差分去噪概率模型（DDPM），生成一个大规模的合成队列，该队列能反映多模态临床和神经影像特征的分布，并平衡诊断类别。随后，基于合成数据预训练特定模态的Graph Transformer编码器，学习到稳健的、类间区分性的表示，并在原始NACC数据嵌入上训练神经分类器。通过使用最大均值偏差（MMD）、弗雷谢距离和能量距离等指标量化真实和合成队列的分布对齐，并通过分类精度、固定特异性和敏感性分析补充区分指标。
### Conclusion
实验结果显示，基于扩散生成的合成图预训练与Graph Transformers相结合的框架在NACC样本交叉验证方面优于标准基线（如早期和晚期融合深度神经网络和多模态图基模型MaGNet），能获得更高的AUC、准确率、敏感性和特异性。这些结果表明，在小样本和类别不平衡的临床预测设置中，这种预训练方法可以提高泛化性能。
## 630. `cs.LG` - 梯度下降算法综述 [PDF](https://arxiv.org/pdf/2511.20725), [HTML](https://arxiv.org/abs/2511.20725)
### Authors
Deng Fucheng,Wang Wanjie,Gong Ao,Wang Xiaoqi,Wang Fan
### Background
该文章关注于深度学习中优化算法的实际配置需求，针对这一背景，文章详细研究了五种主要的优化算法：SGD、小批量SGD、动量、Adam和Lion。
### Innovation
文章系统地分析了每种算法的核心优势、局限性和关键的实用建议，旨在深入理解这些算法，并为两者提供一个标准化的参考——即在学术研究和工程实践中合理选择、参数调优和性能提升优化算法，帮助解决不同规模模型和各种训练场景中的优化问题。
### Conclusion
文章旨在通过综合分析，为优化算法的选择、参数调整和性能优化提供指导，既适用于学术研究也适用于工程实践，尤其对于不同规模的模型和各种训练场景下的优化挑战具有一定的解决价值。
## 631. `cs.LG` - 从风险中学习：基于大型语言模型的先验知识引导下关键安全场景生成 [PDF](https://arxiv.org/pdf/2511.20726), [HTML](https://arxiv.org/abs/2511.20726)
### Authors
Yuhang Wang,Heye Huang,Zhenhua Xu,Kailai Sun,Baoshen Guo,Jinhua Zhao
### Background
自主驾驶面临罕见长尾事件和复杂多目标交互的关键挑战，此类事件在现实数据中罕见但对稳健的安全验证至关重要。
### Innovation
该论文提出了一种高保真度的场景生成框架，将条件变分自编码器（CVAE）与大型语言模型（LLM）结合使用。CVAE 编码大规模自然数据的历史轨迹和地图信息，学习潜在线交通结构，从而生成物理上一致的基础场景。在此基础上，LLM 作为对抗推理引擎，将无结构场景描述解析为特定领域的损失函数，并动态指导不同风险水平下的场景生成。这种基于知识的优化平衡了现实与可控性，确保生成的场景既现实又风险敏感。
### Conclusion
实验在 CARLA 和 SMARTS 中表明，本文框架大幅增加了高风险和长尾事件的覆盖率，提高了模拟和实际交通分布的一致性，并使自主驾驶系统面临比现有规则或数据驱动方法生成的交互更为严峻的交互挑战。这些结果确立了一种新的安全验证途径，使自主系统的压力测试在罕见但具有重大影响的事件下变得合理。
## 632. `cs.CV` - DEMIST: 分开多流潜扩散模型用于定量髓鞘图合成 [PDF](https://arxiv.org/pdf/2511.12396), [HTML](https://arxiv.org/abs/2511.12396)
### Authors
Jiacheng Wang,Hao Li,Xing Yao,Ahmad Toubasi,Taegan Vinarsky,Caroline Gheen,Joy Derwenskus,Chaoyang Jin,Richard Dortch,Junzhong Xu,Francesca Bagnato,Ipek Oguz
### Background
定量磁共振转移（qMT）成像提供了髓鞘敏感的生物标志物，例如池大小比（PSR），这对于多发性硬化症（MS）的评估很有价值。然而，qMT 需要进行专门的20-30分钟扫描。本研究提出了一种名为DEMIST的方法，该方法利用标准的T1w和FLAIR图像通过3D潜扩散模型合成PSR图，该模型具有三个互补的调节机制。该方法分为两个阶段：首先，分别对PSR和解剖图像训练单独的自动编码器，以学习对齐的潜空间表示；其次，在冻结的扩散基模型骨干上，在潜空间中训练条件扩散模型。
### Innovation
该研究提出了名为DEMIST的方法，该方法通过标准的T1w和FLAIR图像利用3D潜扩散模型合成PSR图。该模型具有三个互补的调节机制：（i）通过交叉注意力的语义标记，（ii）通过3D ControlNet分支的逐尺度残余提示，（iii）适应性LoRA调制的注意力。此外，还加入边缘感知损失项以保留病灶边界，并保持定量一致性，同时保持最低的可训练参数数量和预训练模型的归纳偏置。与VAE、GAN和扩散基线相比，在多个指标上该方法表现更优，边界更清晰，定量一致性更好。
### Conclusion
我们在163个来自99个受试者上的5折交叉验证中进行了评估，该方法在多个评估指标上都优于VAE、GAN和扩散基线，产生了更清晰的边界和更好的定量一致性与真实值的匹配。该代码已公开可用。
## 633. `cs.LG` - 初始化偏见对深度神经网络训练动态的影响 [PDF](https://arxiv.org/pdf/2511.20826), [HTML](https://arxiv.org/abs/2511.20826)
### Authors
Nicholas Pellegrino,David Szczecina,Paul W. Fieguth
### Background
在随机初始化后，未训练的大规模神经网络倾向于偏好少数几个类别，对这些类别赋予较高的预测概率，而几乎对其他类别赋予零概率。这种偏见称为初始猜测偏见，它影响模型在早期训练时的行为，即在模型尝试拟合数据粗略结构时的表现。训练所选择的损失函数也对这种早期动态有很大影响。
### Innovation
论文研究了初始猜测偏见如何影响神经网络的训练动态，并发现近期设计的Blurry和Piecewise-zero损失函数虽然是为了应对标签错误的鲁棒性，但在暴露于初始偏见时可能无法引导训练方向。研究表明，损失函数的选择对网络早期训练阶段的影响非常显著，强调了需要仔细考虑初始猜测偏见如何与训练计划的不同组件相互作用。
### Conclusion
研究结果表明，损失函数的选择对网络的早期训练阶段有着重大影响，这凸显了需要仔细考虑初始猜测偏见如何与训练过程中的各种组件相互作用。
## 634. `cs.LG` - 时间图学习方法中的表现完整性 [PDF](https://arxiv.org/pdf/2511.20873), [HTML](https://arxiv.org/abs/2511.20873)
### Authors
Elahe Kooshafar
### Background
现实世界系统，如航空路线和加密货币转账等，都可以自然地表示为动态图，其拓扑结构会随时间发生变化。传统的基准测试通常只会根据具体任务的分数来评估动态图学习模型，很少会质疑嵌入本身是否真实地反映了网络的演变情况。
### Innovation
本文提出了表现完整性作为一种要求，并推导出一系列指标来衡量嵌入变化与图变化的接近程度。通过三种合成场景（渐进合并、突变移动和周期重布线）筛选出42个候选指标，并推荐了一个通过所有理论和实证测试的指标。这一验证指标一致地将理论上稳定的UASE和IPP模型排在最高。进而利用该指标对比常见动态图学习模型的表现完整性，揭示神经方法在特定场景下的优势，并展示了与一步链接预测AUC的一致正相关关系。因此，该完整性框架提供了一种任务无关且可解释的动态图表示质量评估工具，为模型选择和未来架构设计提供了更明确的指导。
### Conclusion
提出了一个任务无关且可解释的框架，用于评估动态图表示的质量，并揭示了神经方法在特定场景下的优势与一步链接预测AUC的强正相关关系，为动态图学习模型的选择和未来设计提供了指导。
## 635. `cs.LG` - 在具有潜在状态的模拟器中选择近似信念状态 [PDF](https://arxiv.org/pdf/2511.20870), [HTML](https://arxiv.org/abs/2511.20870)
### Authors
Nan Jiang
### Background
状态重置是模拟器的一项基本但经常被忽视的能力，它支持基于样本的规划，并允许重置为之前遇到的模拟状态，还使其能够使用真实数据校准模拟器。尽管通常被忽视，但在复杂模拟器中实现状态重置可能会非常困难，特别是在模拟器包含潜在变量（状态）的情况下，需要从给定可观察历史的潜在状态的后验分布中进行采样，这被称为信念状态。虽然精确采样通常是不可行的，但可以构建许多近似信念状态采样器，从而提出了如何仅通过模拟器的采样访问来选择这些采样器的问题。
### Innovation
论文将问题简化为一个通用的条件分布选择任务，并发展了新的算法及其分析方法。基于这一简化，信念状态选择问题可以有两种不同的表述方式：潜在状态选择，直接针对潜在状态的条件分布；观察选择，针对观察的诱导分布。有趣的是，这两种表述方式与其下游展开方法的保证相互作用不同，观察选择可能在最自然的展开方法（单重重置）下失败，但在不那么传统但更加稳健的替代方法（重复重置）下则有保证。
### Conclusion
论文揭示了在这个看似简单的问题中丰富而复杂的算法选择、理论精妙之处和开放问题的广阔景观。讨论了诸如分布转移和采样策略的选择等问题。
## 636. `cs.LG` - 基于数据驱动的飞行测试安全监控：一个数据驱动安全学习案例研究 [PDF](https://arxiv.org/pdf/2511.20811), [HTML](https://arxiv.org/abs/2511.20811)
### Authors
Aaron O. Feldman,D. Isaiah Harp,Joseph Duncan,Mac Schwager
### Background
在飞行测试中，由于飞机参数的不确定性，飞行员执行的飞行动作可能会带来意想不到的安全违规问题。因此，飞行员需要清楚的、提前的判断标准以在违规前及时中止动作。为了解决这个问题，该研究采用了离线的随机轨迹模拟来学习飞行员面临的短期安全风险的校准统计模型。
### Innovation
研究开发了一种数据驱动的方法来进行飞行测试运行时的安全监控。方法包括预测未来状态的模型、最近邻模型来分类预测的状态的安全性，以及通过符合性预测来进行分类器校准。该方法在具有不确定参数的飞行动力学模型上进行评估，证明了其能够可靠地识别不安全的场景，匹配理论保证，并在风险的提前分类中超过了基础方法。
### Conclusion
该研究提出的方法能够在飞行测试中进行实时的安全监控，通过提前识别潜在的安全风险，有效避免了不必要的飞行安全隐患。该方法具有广泛的应用前景，不仅能适用于航空领域，还适用于其他涉及不确定性和关键安全问题的领域。
## 637. `cs.LG` - 时空轨迹基础模型 - 最新进展和未来方向 [PDF](https://arxiv.org/pdf/2511.20729), [HTML](https://arxiv.org/abs/2511.20729)
### Authors
Sean Bin Yang,Ying Sun,Yunyao Cheng,Yan Lin,Kristian Torp,Jilin Hu
### Background
基础模型（FMs）已经成为一个强大的范例，能够跨学科领域完成各种数据分析和知识发现任务。受到了FMs，尤其是大型语言模型成功的启发，研究人员开始探索时空基础模型（STFMs），以提升其在广泛时空任务中的适应性和泛化能力。尽管已取得快速进展，但在时空轨迹基础模型（TFMs），STFMs的一个关键子类上的系统性研究仍然不足。
### Innovation
本文档通过提供时空轨迹基础模型（TFMs）最近进展的综述，包括现有方法论的分类和对其优点与局限性的批判性分析，填补了此领域的空白。此外，还指出了开放性挑战并概述了通过开发稳健、负责任和可转移的TFMs以推动时空通用智能的有前景的研究方向。
### Conclusion
该教程全面概述了时空轨迹基础模型（TFMs）的最新进展，包括现有方法论的分类及其优缺点的批判性分析，并指出了未来的挑战和研究方向，旨在推动时空通用智能的发展。
## 638. `cs.LG` - 预训练以获得：无需干净标签的稳健学习 [PDF](https://arxiv.org/pdf/2511.20844), [HTML](https://arxiv.org/abs/2511.20844)
### Authors
David Szczecina,Nicholas Pellegrino,Paul Fieguth
### Background
深度网络在处理噪声标签时会出现性能下降和准确性降低的问题，主要是因为模型过度适应了噪声标签。现有方法通常依赖于干净标签子集的数据。研究人员提出了一种新的方法，即先使用自监督学习（SSL）预训练特征提取模型，而后再在带有噪声标签的原始数据上进行监督训练，从而能够在不需依赖干净标签子集的情况下提升模型对噪声的鲁棒性。
### Innovation
在标准监督训练之前，通过自监督学习（SimCLR和Barlow Twins方法）预训练特征提取器，这种方法在没有干净标签数据子集的情况下能够训练出对噪声具有更强鲁棒性的模型，并且在噪声数据集上有更好的分类准确性以及更好的标签错误检测性能。
### Conclusion
无论噪声率如何，自监督预训练都能提高分类准确性并增强下游标签错误检测性能（F1分数和平衡准确度）。当噪声率增加时，性能差距扩大，展示了更高的鲁棒性。在低噪声水平下，该方法的结果与ImageNet预训练模型相当；而在高噪声条件下，该方法的表现明显优于ImageNet预训练模型。
## 639. `cs.LG` - 使用球谐Fourier神经算子的太阳风自回归代理建模 [PDF](https://arxiv.org/pdf/2511.20830), [HTML](https://arxiv.org/abs/2511.20830)
### Authors
Reza Mansouri,Dustin Kempton,Pete Riley,Rafal Angryk
### Background
太阳风是由太阳 coronal 外流的带电粒子形成的，它塑造了日球层并影响地球附近的太空系统。准确预测高密度流和日冕物质抛射等特征对空间天气预报至关重要，但传统的三维磁流体力学 (MHD) 模型计算成本高，限制了快速探索边界条件的不确定性和敏感性。
### Innovation
提出了第一个用于稳态太阳风径向速度的自回归机器学习代理模型，采用了球谐Fourier神经算子 (SFNO)。通过预测有限的径向范围并将解逐次传播到远处，模型在远处区域的准确性优于单步方法。与数值HUX代理相比，SFNO展现了更优或相当的表现，提供了灵活、可训练且数据驱动的替代方案，开创了高保真太阳风建模的新方法。
### Conclusion
这项研究通过 SFNO 方法实现了高保真太阳风建模的新方法，模型通过逐次传播解来提高远处区域的预测精度，并展现出相对于传统方法的优点。源代码及附加可视化结果在网页 this https URL（替换成实际URL）提供。
## 640. `cs.LG` - Physics Steering: Causal Control of Cross-Domain Concepts in a Physics Foundation Model [PDF](https://arxiv.org/pdf/2511.20798), [HTML](https://arxiv.org/abs/2511.20798)
### Authors
Rio Alexa Fear,Payel Mukhopadhyay,Michael McCabe,Alberto Bietti,Miles Cranmer
### Background
近年来，关于机械解释性的最新进展揭示了大型语言模型（LLMs）不仅开发出与具体实体相对应的内部表示，还开发出与人类可理解的抽象概念和行为相关的独立内部表示。此外，这些隐藏特征可以被直接操作以引导模型的行为。然而，这仍是一个开放性问题，即这种现象是否仅限于训练于固有结构化数据（如语言、图像）的模型，还是泛化的基础模型的基本属性。
### Innovation
受对大型语言模型中复杂行为空间中单个方向的先前工作的启发，本文从一个专注于物理学的基础模型在不同物理状态下经过模拟数据集的前向传递过程中提取激活向量，并计算两个状态之间的“差”表示。这些差张量作为激活空间中的概念方向，编码特定的物理特征。通过在推理过程中注入这些概念方向，可以引导其预测，从而对物理行为进行因果控制，如在模拟中诱导或移除某些特定的物理特征。这表明科学基础模型学习了物理学原理的通用表示，而不仅仅是依赖模拟中的表面相关性和模式。
### Conclusion
这些结果表明科学基础模型学习了物理学原理的一般表示，而不仅仅是依赖模拟中的表面相关性和模式。我们的发现为理解并控制科学基础模型打开了新途径，并对AI驱动的科学发现具有重要意义。
## 641. `cs.LG` - CHiQPM: 校准的层次可解释图像分类 [PDF](https://arxiv.org/pdf/2511.20779), [HTML](https://arxiv.org/abs/2511.20779)
### Authors
Thomas Norrenbrock,Timo Kaiser,Sovan Biswas,Neslihan Kose,Ramesh Manuvinakurike,Bodo Rosenhahn
### Background
可解释的模型是确保AI在安全关键领域可信性的有前途的方法。全局解释和详细的局部解释对于辅助人类专家在推理期间的理解至关重要。现有的研究进展表明，为了实现人类与AI的互补，需要一种既能保证高准确率又能提供全面的解释性模型。
### Innovation
本文提出了一种名为Calibrated Hierarchical QPM (CHiQPM)的可解释模型，它具有独特的全面全局和局部可解释性特性。CHiQPM通过对比性解释大多数类别实现卓越的全局可解释性，并提供了一种新的层次解释，该解释更接近人类的推理方式，同时具备内置的可解释性推断校准预测方法。此外，CHiQPM在准确性和可解释性方面取得了显著进步，没有降低整体准确性，同时也具有与其他校准预测方法相当的效率。
### Conclusion
本文的评估结果表明，CHiQPM既保持了99%的非解释模型的准确性，又提供了具有可解释性的预测，同时还具有竞争力的校准集预测效率。该模型为安全关键领域的人机协同提供了新的可能性，同时也展示了在提高模型可解释性的同时不牺牲整体准确性的可能性。
## 642. `cs.LG` - 在败血症治疗中探索时间步长在强化学习中的应用 [PDF](https://arxiv.org/pdf/2511.20913), [HTML](https://arxiv.org/abs/2511.20913)
### Authors
Yingchuan Sun,Shengpu Tang
### Background
现有对强化学习(RL)在败血症管理中的研究大多遵循了一个已成型的问题设定，其中患者数据被聚合为4小时的时间步长。尽管有关这一时间步长粗略性的担忧已经提出，这可能会扭曲患者动态并导致次优的治疗政策，但这一问题在实际中的严重程度尚未被充分研究。
### Innovation
本研究通过比较1小时、2小时、4小时和8小时四种时间步长下的表现，对在线下 RL 管线中进行了实证实验。设计了动作重新映射方法以在不同时间步长的数据集上评估策略，同时在两种策略学习设置下进行了跨时间步长的模型选择。研究目的是量化时间步长对状态表示学习、行为克隆、策略训练和离策评估的影响。
### Conclusion
结果显示性能随时间步长的变化取决于学习设置的变化，使用静态行为策略在更细的时间步长(1小时和2小时)下学习得到的整体最佳性能和稳定性表现。本研究强调时间步长在医疗保健领域的线下 RL 设计中的关键性，并提供了超越传统4小时设置的变化支持。
## 643. `cs.LG` - Primal：一种统一的确定性框架，用于准正交哈希和流形学习 [PDF](https://arxiv.org/pdf/2511.20839), [HTML](https://arxiv.org/abs/2511.20839)
### Authors
Vladimer Khasia
### Background
该研究提出了一种名为Primal的确定性特征映射框架，利用质数平方根的数论独立性构建了具备鲁棒性和可调性的向量表示。这种方法不同于传统的随机投影（如随机傅里叶特征），通过利用Besicovitch性质，它能生成无重复相位轨迹的非周期频率调制。研究团队还提出了两种不同的算法变体：StaticPrime和DynamicPrime。前者是一种序列生成方法，能够生成接近理论威尔士上限的时间位置编码；后者则是一种依赖输入的可调投影层。DynamicPrime框架的核心创新在于单一比例参数σ能够统一两种不同的数学用途类别。在低频段，该方法作为一种等距核映射，有效地将非凸几何（如螺旋）线性化，从而实现高保真信号重建和压缩传感。而在高频段，调制则是一种最大熵的单向哈希，适用于超维计算和隐私保护的Split Learning。
### Innovation
Primal框架通过利用质数平方根的数论独立性，实现了确定性特征映射。它引入了StaticPrime和DynamicPrime两种算法变体，前者生成接近理论威尔士上限的时间位置编码，后者为输入依赖的可调投影层。DynamicPrime框架的核心创新在于单一比例参数σ能够统一两种不同的数学用途类别。在特定的高频和低频域，Primal方法展示出独特的应用特性，如等距核映射和最大熵哈希，适用于不同的应用场景，如信号重建和隐私保护的Split Learning。
### Conclusion
实验结果表明，Primal框架在保持正交性和分布紧致性方面优于标准化高斯基准。它提供了一种在计算效率和数学严谨性方面具有竞争力的随机矩阵投影替代方案。这种方法证明了其在流形学习和准正交哈希中的有效性和灵活性。相关代码可在此链接访问。
## 644. `cs.LG` - 进化样本权重用于偏见缓解：优化目标的效果依赖性 [PDF](https://arxiv.org/pdf/2511.20909), [HTML](https://arxiv.org/abs/2511.20909)
### Authors
Anil K. Saini,Jose Guadalupe Hernandez,Emily F. Wong,Debanshi Misra,Jason H. Moore
### Background
在使用真实世界数据训练的机器学习模型中，可能会无意中做出带有偏见的预测，这可能对边缘化群体产生负面影响。重新加权是一种可以通过为每个用于模型训练的数据点分配权重来减轻这种偏见的方法。本文将比较三种生成权重的方法：（1）使用遗传算法（GA）进化这些权重，（2）仅使用数据集特性计算这些权重，（3）给所有数据点分配相同权重。评估模型性能的指标包括配对预测和公平性指标，并且这些指标也是优化期间GA进化的目标。具体来说，使用两种预测指标（准确率和ROC曲线下的面积）和两种公平性指标（人口平等待遇差异和子组虚假否定公平性）。
### Innovation
本文通过使用遗传算法进化样本权重的方法，探索在多个公开可用的数据集（包括两个医学数据集）上实现公平性与预测性能之间的更好权衡。创新点在于根据不同的优化目标，这些进化权重方法能够获得显著更好的性能。
### Conclusion
实验结果表明，进化样本权重可以在公正性和预测性能之间产生更好的权衡。然而，这些好处的幅度取决于所选择的优化目标。当使用准确率和人口平等待遇差异指标时，能够获得最多数量的数据集，其中进化权重在同时优化两个目标方面显著优于其他加权策略。
## 645. `cs.LG` - 实现量化分离的操作化 [PDF](https://arxiv.org/pdf/2511.20927), [HTML](https://arxiv.org/abs/2511.20927)
### Authors
Vitoria Barin-Pacela,Kartik Ahuja,Simon Lacoste-Julien,Pascal Vincent
### Background
近期的理论研究已经确定，在任何微分同胚下，量化因子的无监督识别是可能的。理论假设量化阈值对应于潜在因子概率密度中的轴对齐的不连续性。通过将学到的映射限制为具有轴对齐不连续性的密度，可以恢复因子的量化。然而，将这一高层次的原则转化为有效的实践经验评价标准仍然具有挑战性，特别是在非线性映射的情况下。
### Innovation
本文通过鼓励轴对齐不连续性的方法开发了一种无监督拆分的标准。这种不连续性作为因子估算密度中的尖锐变化表现出来，并称为断崖。依据理论中独立不连续性的定义，鼓励断崖在某因子上的位置与其他因子的值无关。实验证明了Cliff方法在所有拆分基准测试中的优越性，证明了其在无监督拆分中的有效性。
### Conclusion
我们方法Cliff在所有拆分基准测试中表现出色，证实了它在无监督拆分中的有效性。
## 646. `cs.LG` - 行为克隆策略上的数据集注入攻击 [PDF](https://arxiv.org/pdf/2511.20992), [HTML](https://arxiv.org/abs/2511.20992)
### Authors
Akansha Kalra,Soumil Datta,Ethan Gilmore,Duc La,Guanhong Tao,Daniel S. Brown
### Background
行为克隆（BC）是一种通过监督学习从专家演示中训练顺序决策策略的常用框架。随着这些策略在现实世界中的部署，其鲁棒性和潜在漏洞成为一个重要的问题。本文首次分析了清洁标签后门攻击对BC策略的有效性。
### Innovation
本文提出了一种视觉触发器的后门攻击，通过在数据集中注入视觉触发器来创建一种在测试时可以利用的虚假相关性。研究了受污染数据的比例、触发器的强度和类型对策略漏洞的影响。还引入了一种新颖的基于熵的测试时触发攻击，这种攻击通过对关键状态的识别，严重降低了策略的性能。实验证明，即使是轻微受污染的数据集训练的BC策略，其任务性能看起来非常高，但实际上在部署时却非常容易受到后门触发攻击的影响。
### Conclusion
我们的结果强调了对行为克隆策略鲁棒性研究的紧迫性，尤其是在大规模数据集被广泛用于训练现实世界中的网络物理系统时。
## 647. `cs.LG` - 语义优越性与法医效率：深度学习与法医学心理语言学在商务电子邮件篡改检测中的比较分析 [PDF](https://arxiv.org/pdf/2511.20944), [HTML](https://arxiv.org/abs/2511.20944)
### Authors
Yaw Osei Adjei(Kwame Nkrumah University of Science and Technology)
### Background
商务电子邮件篡改（BEC）是一种复杂的社会工程学威胁，会影响组织的层级结构，并利用心理弱点，造成严重经济损害。根据2024年FBI互联网犯罪报告，BEC造成的年度调整后的损失超过290亿美元，显示了巨大的经济不对称性：假阴性（诈骗损失）的成本远高于假阳性（手动审查）的成本（约1到5,480）。
### Innovation
本文探讨了两种BEC检测范式：法医心理语言学流派，利用CatBoost分析具有高可解释性和低延迟的心理语言学线索；以及语义流派，采用DistilBERT进行基于深度学习的语境语言理解，提供更高的准确性但消耗更高的计算资源。
### Conclusion
对于拥有GPU基础架构的组织，DistilBERT提供更高的检测准确性。CatBoost在边缘部署或成本敏感环境中更优，提供可接受的较低延迟且消耗很少的计算资源。两种方法在通过成本敏感学习优化后，投资回报率超过99.96%，通过显著减少假阴性及相关的经济损失来实现。
## 648. `cs.LG` - FANoise: 依据奇异值适配的噪声调制以实现鲁棒的多模态表示学习 [PDF](https://arxiv.org/pdf/2511.20997), [HTML](https://arxiv.org/abs/2511.20997)
### Authors
Jiaoyang Li,Jun Fang,Tianhao Gao,Xiaohui Zhang,Zhiyuan Liu,Chao Liu,Pengzhang Liu,Qixia Jiang
### Background
作为现代机器学习的核心，表示学习推动了诸如文本检索和多模态理解等应用的发展。然而，学习稳健且具泛化能力的表示仍然具有挑战性。尽管先前研究表明，主动噪声注入作为一种数据增强方法，可以提升表示编码性能，但大多数现有方法依赖于启发式或静态噪声，未能考虑到训练过程中特征分布的动态性质。
### Innovation
本文从梯度和特征分布视角系统研究了噪声在表示学习中的作用，使用InfoNCE损失为例。针对多模态表示学习，提出了FANoise，一种新颖的特征自适应噪声注入策略。通过利用对比学习的动态特性，FANoise有效地减轻了噪声的负面影响并保留其积极效果。
### Conclusion
在理论框架支撑下，广泛实验表明，FANoise在各种基础的视觉语言模型上一致提高了多模态任务的整体性能。
## 649. `cs.LG` - ChatGPT 内容检测：使用 XLM-RoBERTa 对齐的新方法 [PDF](https://arxiv.org/pdf/2511.21009), [HTML](https://arxiv.org/abs/2511.21009)
### Authors
Md Tasnin Tanvir,Dr Santanu Kumar Dash,Ishan Shahnan,Nafis Fuad,Tanvir Rahman,Abdullah Al Faisal,Asadullah Al Mamun
### Background
随着像ChatGPT这样的生成AI技术的普及，区分AI生成的文本和人类创作的内容变得越来越迫切。本文针对这一问题，研究了完全由AI生成的内容检测，以及人类文本由AI重写后的识别方法。使用了最新的多语言变压器模型XLM-RoBERTa进行AI生成文本的检测，并进行了严谨的预处理和特征提取，包括困惑度、语义和可读性特征。
### Innovation
提出了一种使用XLM-RoBERTa模型的新方法来检测AI生成的文本，模型经过微调并在平衡的人类和AI生成的文本数据集上进行了评估，展示出了在不同文本体裁中的高准确性和稳健性。此外，进行了特征分析以理解模型在区分人类和AI生成文本时的决策过程，发现困惑度和基于注意力的特征在这一过程中至关重要。
### Conclusion
研究成果提供了一种有效维护学术诚信的工具，并为促进AI伦理中的透明度和问责制做出了贡献。未来的研究方向包括探索其他高级模型和扩大数据集以提高模型的泛化能力。
## 650. `cs.LG` - 阶段化环境重置促进大规模并行在线强化学习 [PDF](https://arxiv.org/pdf/2511.21011), [HTML](https://arxiv.org/abs/2511.21011)
### Authors
Sid Bharthulwar,Stone Tao,Hao Su
### Background
大规模并行GPU模拟环境加速了强化学习（RL）的研究，尤其是对于像Proximal Policy Optimization (PPO)这样的在线策略RL算法，通过快速数据收集来提高算法效率。然而，为了最大化吞吐量，通常会在每次策略更新时使用较短的轨迹长度，这增加了更新到数据（UTD）比率。但这样做会导致同步重置引入不利的非稳态性，这会扭曲学习信号并导致训练不稳定。
### Innovation
引入了阶段化重置，这是一种简单有效的方法，即在任务持续时间内以不同的点初始化和重置环境。这种方法增加了训练批次的时间多样性，减少了同步轨迹引入的非稳态性。此外，该技术通过生动的玩具环境展示了RL环境在哪些维度上可以显著受益于阶段化重置，并且在此基础上应用于复杂的高维机器人环境，获得了更高的样本效率，更快的实际收敛速度和更强的最终性能。同时，该技术在更多的并行环境中表现出更好的扩展性。
### Conclusion
阶段化重置提高并行大规模在线强化学习的效果，通过减少同步轨迹带来的非稳态性，增强学习稳定性和效率。该技术特别适用于复杂的高维机器人环境，并且在更多的并行环境中具有更好的可扩展性。
## 651. `cs.LG` - 在总变差距离中估计伊辛模型 [PDF](https://arxiv.org/pdf/2511.21008), [HTML](https://arxiv.org/abs/2511.21008)
### Authors
Constantinos Daskalakis,Vardis Kandiros,Rui Yao
### Background
本文考虑了给定来自模型的 $l$ 个独立样本时，使用总变差距离估计 $n$ 个变量的伊辛模型的问题。已知该问题的统计复杂性是已知的[DMR20]，然而找到既计算上又统计上有效地解决问题的算法仍然具有挑战性。虽然在特定场景下，如基于树图[DP21, BGPV21]、互作矩阵遵循高斯分布[GM24, CK24]以及谱值大部分落在小区间[AJK+24, KLV24]的情况下已经取得了显著进展，但目前尚无统一的框架可以在多项式时间内进行总变差估计。
### Innovation
本文的主要贡献是对两大类伊辛模型进行了统一分析：一类包含操作数范数有界和满足修改后的 logarithmic Sobolev 不等式（MLSI）的模型，另一类包含互作矩阵的无限范数有界（或具有有限宽度）模型。我们的结果表明，对于这些类别的模型，我们能够提供多项式时间算法和在多种场景下的最优或接近最优的样本复杂度保证。证明过程使用了张量化不等式、测度分解和集中界等多种工具。
### Conclusion
总之，本文的研究为伊辛模型在多项式时间内进行总变差估计奠定了基础，并提供了样本复杂度界，这使得在实际应用中该模型的参数估计更加高效。
## 652. `cs.LG` - Gated KalmaNet：通过测试时岭回归实现淡出记忆的层 [PDF](https://arxiv.org/pdf/2511.21016), [HTML](https://arxiv.org/abs/2511.21016)
### Authors
Liangzu Peng,Aditya Chattopadhyay,Luca Zancato,Elvis Nunez,Wei Xia,Stefano Soatto
### Background
线性状态空间模型（SSMs）相比softmax注意力具有高效的内存和计算成本（常数和线性），但它们只能保持模糊且容易衰减的过去记忆，这使得它们在记忆依赖的任务中表现不佳。Gated KalmaNet（GKA）通过考虑整个过去的记忆，而非仅依赖最近的部分，来解决这一问题。在预测下一个标记时，GKA通过在线求解岭回归问题，在保持SSM样式效率的同时具有常数内存和线性计算成本。这缓解了SSM模型在长上下文任务中的性能劣势。
### Innovation
GKA通过以下两个关键创新解决了标准卡尔曼滤波器在低精度环境（如bfloat16）中数值不稳定的挑战和现代硬件上的难于并行化的挑战：1. 一种输入依赖的自适应正则化策略，控制岭回归的条件数，确保数值稳定性并在内存保留和精度之间取得平衡。2. 使用Chebyshev迭代而非通常的迭代求解器，我们证明在低精度设置中更稳定。为了增强可扩展性，GKA还开发了针对硬件感知的分块实现Chebyshev迭代以及用于回传实现中的自定义内核。
### Conclusion
GKA在短期上下文任务中表现出强大的语言理解能力，超越现有的SSM层，如Mamba2、GLA和Gated DeltaNet。在长上下文任务中，GKA在现实中的RAG和LongQA任务中表现出色，可处理多达128k标记，相比其他淡化记忆的基线，取得了超过10%的相对性能提升。
## 653. `cs.LG` - Probabilistic Hash Embeddings for Online Learning of Categorical Features [PDF](https://arxiv.org/pdf/2511.20893), [HTML](https://arxiv.org/abs/2511.20893)
### Authors
Aodong Li,Abishek Sankararaman,Balakrishnan Narayanaswamy
### Background
本文研究的是具有变化词汇表的类别特征流数据。通常使用特征哈希作为预处理步骤，将这些类别值映射到固定大小的特征空间，然后再进行嵌入学习。这类方法在离线或批量设置下开发和评估，但本文考虑了在线设置。现有方法的确定性嵌入对类别到达顺序敏感，并且在在线学习中容易遗忘，导致性能下降。
### Innovation
本文提出了一种概率哈希嵌入（PHE）模型，将哈希嵌入视为随机变量，并应用贝叶斯在线学习来增量学习数据。基于PHE的结构，推导出一种可扩展的推理算法，用于学习模型参数和推断/更新哈希嵌入和其他潜在变量的后验。该算法能够处理不断变化的类别项目词汇表，对新项目适应而不遗忘旧项目，使用有限数量的参数进行实现而不随流中不同观察值的数量增长，且与项目到达顺序无关。
### Conclusion
在在线学习设置下的分类、序列建模和推荐系统实验中，PHE模型展示了卓越的性能，同时保持高效内存使用（消耗最低仅为一热编码嵌入表的2~4倍）。
## 654. `cs.LG` - 使用自回归条件生成对抗网络进行 wildfire 扩散概率预测 [PDF](https://arxiv.org/pdf/2511.21019), [HTML](https://arxiv.org/abs/2511.21019)
### Authors
Taehoon Kang,Taeyong Kim
### Background
气候变化加剧了野火的频率和严重性，快速和准确预测火势蔓延对于有效减轻和应对至关重要。基于物理的模拟器如 FARSITE 可提供高度精确的预测但耗时长，限制了其在实时决策中的应用。现有的深度学习模型通常产生过于平滑的预测，无法捕捉到野生火蔓延的复杂非线性动力学。
### Innovation
本研究提出了一种自回归条件生成对抗网络 (CGAN) 用于概率性野火蔓延预测。通过将预测任务建模为自回归问题，该模型学习序列状态转换，确保长期预测的稳定性。实验结果显示，基于 CGAN 的模型在总体预测准确性和火势边界刻画上优于传统深度学习模型。对抗学习使模型能够捕捉到野火蔓延的强非线性和不确定性，而非仅仅拟合像素平均值。此外，自回归框架有助于系统地预测野火演变。
### Conclusion
基于 CGAN 的自回归框架提高了野火蔓延预测的准确性和物理可解释性，为时间敏感的响应和疏散规划提供了有前景的基础。
## 655. `cs.LG` - RAVQ-HoloNet：可变比特率矢量化量化全息图压缩 [PDF](https://arxiv.org/pdf/2511.21035), [HTML](https://arxiv.org/abs/2511.21035)
### Authors
Shima Rafiei,Zahra Nabizadeh Shahr Babak,Shadrokh Samavi,Shahram Shirani
### Background
全息图在AR/VR应用中有重大潜力，但由于数据压缩需求高，其采用面临限制。现有的深度学习方法通常缺乏在单个网络内的速率自适应性。
### Innovation
提出了RAVQ-HoloNet，这是一种速率自适应矢量化量化框架，能够在低比特率和超低比特率下实现高保真重建，优于当前最先进的方法。在低比特率下，该方法优于现有最佳方法33.91%的BD-Rate，且BD-PSNR提高了1.02 dB。
### Conclusion
RAVQ-HoloNet通过提高全息图压缩的比特率适配性，实现了在低比特率下的高质量重建，具有显著的技术优势，有望加速全息图在AR/VR中的应用。
## 656. `cs.LG` - 一种用于工业规模推荐系统的基于因果结构的概率时间分布泛化的框架 [PDF](https://arxiv.org/pdf/2511.21032), [HTML](https://arxiv.org/abs/2511.21032)
### Authors
Yuxuan Zhu,Cong Fu,Yabo Ni,Anxiang Zeng,Yuan Fang
### Background
时间分布偏移（TDS）影响推荐系统的长期准确性，但工业实践中仍然依赖于定期增量训练，这难以捕捉稳定和短暂的模式。现有的方法如不变学习和自监督学习虽然提供了部分解决方案，但也存在时间泛化不稳定、表征崩溃或数据利用效率低等问题。
### Innovation
本文提出了一种称为ELBO$_text{TDS}$的概率框架，能够无缝集成到工业规模的增量学习流水线中。首先，通过统计分析实时生产数据识别关键的偏移因素，并设计了一种简单有效的数据扩增策略来延长训练支持。其次，利用扩展的分布带来的好处，并预防表征崩溃，通过因果图建模时间推荐场景，并导出基于因果结构的自监督变分目标ELBO$_text{TDS}$。
### Conclusion
实证实验结合理论分析表明，该方法实现了时间泛化的卓越性能，带来了每用户的GMV提升2.33%，并在Shopee产品搜索中成功部署。
## 657. `cs.LG` - 使用SDR的CNN-LSTM混合架构进行空中自动调制分类 [PDF](https://arxiv.org/pdf/2511.21040), [HTML](https://arxiv.org/abs/2511.21040)
### Authors
Dinanath Padhya,Krishna Acharya,Bipul Kumar Dahal,Dinesh Baniya Kshatri
### Background
自动调制分类（AMC）是未来无线通信系统的核心技术之一，无需先验知识即可识别调制方案。这一能力对于认知无线电、频谱监测和智能通信网络的应用至关重要。现有的AMC系统采用深度学习方法，利用时域和空域特征的复杂性来识别各种调制方案。
### Innovation
文章提出了一种基于混合卷积神经网络（CNN）和长短期记忆（LSTM）架构的AMC系统，结合了软件定义无线电（SDR）平台。该架构利用CNN提取空域特征，并利用LSTM捕捉时态依赖性，有效处理复杂的、随时间变化的通信信号。实验结果表明，该系统性能优异，识别准确率达到93.48%，精确度、召回率和F1分数分别为93.53%、93.48%和93.45%，即使在噪声环境下，其判别能力也被验证。
### Conclusion
实验结果验证了混合CNN-LSTM架构在AMC中的有效性，并在此基础上提出了其在自适应频谱管理和先进认知无线电系统中的潜在应用。
## 658. `cs.LG` - 使用多头注意力转换器预测奶牛群寿命 [PDF](https://arxiv.org/pdf/2511.21034), [HTML](https://arxiv.org/abs/2511.21034)
### Authors
Mahdi Saki,Justin Lipman
### Background
奶农需要根据奶牛在未来牛群中的表现客观地做出保留或淘汰的决定，尤其是为了识别更能适应农场环境、完成更多产奶周期的奶牛。这一决策过程复杂且具有重大环境和经济影响。
### Innovation
开发了一个基于历史多变量时间序列数据的AI驱动模型，利用多头注意力转换器技术，对来自澳大利亚7个农场共计19,000头奶牛的约780,000条记录进行了分析。
### Conclusion
模型在预测牛群寿命方面整体决定系数达到了83%，表现出在奶牛场管理中实际应用的巨大潜力。
## 659. `cs.LG` - FedAPA: 联邦学习中的自适应原型聚合以实现异构Wi-Fi CSI人群计数 [PDF](https://arxiv.org/pdf/2511.21048), [HTML](https://arxiv.org/abs/2511.21048)
### Authors
Jingtao Guo,Yuyi Mao,Ivan Wang-Hei Ho
### Background
基于Wi-Fi通道状态信息（CSI）的传感技术为非侵入式、无设备的任务如人体活动识别和人群计数提供了可能，但大规模部署受限于需要大量的特定场地训练数据。联邦学习（FL）提供了一种避免原始数据共享的方法，但面临着异构传感数据和设备资源的挑战。
### Innovation
提出了一种协作的基于Wi-Fi CSI的自适应原型聚合（APA）策略，该策略根据相似性为对等原型分配权重，实现自适应客户端贡献并生成每个客户端的个性化全局原型，而不是固定权重聚合。在局部训练中，采用结合分类学习和表示对比学习的混合目标以对齐局部和全局知识。
### Conclusion
实验证明，该方法在六种环境中的人群计数场景中优于多个基线方法，在准确度、F1分数、平均绝对误差（MAE）和通信开销方面表现出色，FedAPA在准确度上提高了至少9.65%，在F1分数上提高了9%，在MAE上降低了0.29，在通信开销上减少了95.94%。
## 660. `cs.LG` - 打破安全与能力权衡：可验证奖励的强化学习在LLM中保持安全防护 [PDF](https://arxiv.org/pdf/2511.21050), [HTML](https://arxiv.org/abs/2511.21050)
### Authors
Dongkyu Derek Cho,Huan Song,Arijit Ghosh Chowdhury,Haotian An,Yawei Wang,Rohit Thekkanal,Negin Sokhandan,Sharlina Keshava,Hannah Marlowe
### Background
大型语言模型（LLMs）在进行下游任务微调时通常会出现一种根本性的安全能力权衡问题，即在提高任务性能的同时会降低对良性数据的安全对齐度。这一问题在传统方法中（如监督微调SFT和基于人类反馈的强化学习RLHF）持续存在。尽管可验证奖励的强化学习（RLVR）被视为一种潜力巨大的替代方案，能优化模型在客观可测量任务上的能力，但对于其安全性影响目前仍缺乏研究。
### Innovation
本文首次全面分析了RLVR的安全属性。在理论上，通过KL约束优化推导了安全漂移的上界，并展示了在安全降级被消除的条件下，优化模型的安全性目标。在实验上，通过涵盖五个对抗安全基准的大量实验，证明了RLVR方法可以在提升推理能力的同时保持或改善安全防护。通过对优化算法、模型规模和任务领域的消融研究，探讨了不同的因素对安全属性的影响。这些发现挑战了不可避免的安全能力权衡的普遍假设，并建立了特定训练方法同时实现两个目标的可能性，为推理能力强的LLM的安全部署提供了见解。
### Conclusion
本文提出了RLVR方法，证明其在提升逻辑推理能力的同时仍能有效维护模型的安全性。研究结果表明，特定的训练策略可以同时提升模型的能力与安全性，打破了传统大型语言模型训练中存在的安全与能力权衡难题，为确保推理能力强的LLM安全应用提供了实际指导。
## 661. `cs.LG` - Deceptron: 学习的局部逆函数以实现快速稳定的物理逆问题求解 [PDF](https://arxiv.org/pdf/2511.21076), [HTML](https://arxiv.org/abs/2511.21076)
### Authors
Aaditya L. Kachhadiya
### Background
物理科学中的逆问题通常在输入空间中条件不良，使得进展对步长敏感。研究表明，通过结合监督拟合、前向后逆一致性、轻量级谱约束、软偏差绑定以及通过JVP/VJP探测鼓励$J_g(f(x))times J_f(x)thickapprox I$的雅可比组成约束（JCP），可以在训练过程中学习一个局部逆向的差分前面模型。
### Innovation
提出了一种名为Deceptron的轻量级双向模块，用于学习可微分前向代理的局部逆。Deceptron通过结合监督拟合、前向后逆一致性、轻量级谱约束、软偏差绑定以及雅可比组成约束（JCP）来训练。在求解时，D-IPG（Deceptron逆预条件梯度）在输出空间中进行下降步骤，通过$g$反向拉回，并在相同的回溯和停止规则下投影。在Heat-1D初始条件恢复和阻尼振子逆问题测试中，D-IPG相较于投影梯度具有约20倍更少的迭代次数，在阻尼振子中则少2至3倍，与Gauss-Newton法在迭代数和成本方面具有竞争力。
### Conclusion
研究表明JCP可以减少测量的组成误差，并跟踪迭代收益。还-preview-了单一尺度2D实例DeceptronNet（v0），在严格公平协议下学习多步更正，并展示了快速收敛的特征。
## 662. `cs.LG` - 使用平衡微调使大规模语言模型与生物医药知识对齐 [PDF](https://arxiv.org/pdf/2511.21075), [HTML](https://arxiv.org/abs/2511.21075)
### Authors
Zhenchao Tang,Fang Wang,Haohuai He,Jiale Zhou,Tianxu Lv,Jun Zhu,Shouzhi Chen,Minghao Yang,Yu Wang,Jiayang Wu,Yidong Song,Jianhua Yao
### Background
对大规模语言模型（LLMs）进行有效的后训练至关重要，以使它们与专门的生物医药知识相匹配，从而加速生命科学研究。然而，当前的方法存在显著限制。首先，生物医药推理涉及复杂的机制，经常以稀疏的文本数据表示。标准监督微调（SFT）倾向于过度拟合表面级指令模式，无法有效吸收这些断裂的科学知识。其次，强化学习（RL）在该领域不可行，因为定义有意义的奖励往往需要禁止性的实验验证（如药物反应的湿实验验证），这使得实时反馈变得不可能。因此，现有的方法无法有效解决生物医药领域中的复杂推理问题。
### Innovation
我们提出了平衡微调（BFT），这是一种有效的后训练方法，设计用于从稀疏数据中学习复杂的推理，而无需外部奖励信号。BFT通过双层加权机制运作：1. 在标记层面上，通过预测概率缩放损失，以稳定梯度并防止过拟合；2. 在样本层面上，使用“最小组置信度”来适应性增强对困难样本的学习。实验表明，BFT在医学任务中显著优于SFT，使其能够掌握SFT忽视的知识。在生物任务中，基于BFT的LLMs在生物学过程推理方面超越了GeneAgent（一个准确的生物分析代理）。此外，BFT生成的文本嵌入可以直接应用于下游任务，如基因相互作用和单细胞扰动响应预测。
### Conclusion
总的来说，BFT促进了LLMs在生物医药研究中的广泛应用。
## 663. `cs.LG` - MNM : 多层级神经影像荟萃分析中的双曲脑-文本表示 [PDF](https://arxiv.org/pdf/2511.21092), [HTML](https://arxiv.org/abs/2511.21092)
### Authors
Seunghun Baek,Jaejin Lee,Jaeyoon Sim,Minjae Jeong,Won Hwa Kim
### Background
神经影像学研究往往受到样本量小的问题限制，这会影响其可靠性。荟萃分析通过聚合不同研究的结果来识别一致的大脑活动模式，以应对这一挑战。然而，传统的方法基于关键词检索或线性映射，常常忽略了大脑内部丰富且分层次的结构。
### Innovation
本文引入了一个新的框架，利用双曲几何结合神经科学文献和脑活动图谱。通过Lorentz模型将研究文章的文本和对应的脑图像嵌入到共享的双曲空间，该方法能够同时捕捉语义相似性和影像数据中的层次化组织。在双曲空间中，该方法通过1) 对齐脑部和文本嵌入以实现语义对应，2) 引导文本与脑活动之间的层次结构，以及3) 保持脑激活模式内的层次关系来执行多层级神经影像荟萃分析。
### Conclusion
实验结果表明，我们的模型在基准模型上表现出更优的性能，提供了一种通过双曲脑-文本表示进行多层级神经影像荟萃分析的稳健且可解释的范式。
## 664. `cs.LG` - MLPMoE: 零样本密集LLM MLP架构转型为静态专家混合 [PDF](https://arxiv.org/pdf/2511.21089), [HTML](https://arxiv.org/abs/2511.21089)
### Authors
Ivan Novikov
### Background
现有的大型语言模型（LLMs）大多采用密集的Transformer结构，每层参数都会被激活。虽然这种结构在架构上较为简单，但在推理时却非常低效，因为计算成本会随着参数数量线性增长。近期的研究表明，密集Transformer中的一些稀疏子结构仍然可以提供有益的计算，但仍依赖于聚类、激活特性分析、奇异值分解或自定义路由等方法，这些方法通常需要调参数据。本文提出了一种无训练的MLPMoE方法，它将Transformer块中的密集MLP重构成静态的高基数专家混合结构。这种方法利用简单的张量切片和求和操作，重新解释张量并行的代数为一种拓扑转换而非分布式训练模式。
### Innovation
提出了MLPMoE方法，它是一种无训练的、确定性的转换，将Transformer块中的密集MLP重构为静态的高基数专家混合结构。该方法利用简单的张量切片和求和操作，重新解释张量并行的代数作为拓扑转换，而不是分布式训练模式。此外，还引入了分形淡入（分段分支稀疏）和补偿剪枝（方差保持分支减少）作为轻量级的结构稀疏机制。
### Conclusion
在Qwen2.5-0.5B-Instruct和DeepSeek-R1-Distill-Llama-8B模型上，零样本的MLPMoE转换方法改变了代理困惑度指标不到0.05%，同时参数数量保持不变。在8B模型上，分段稀疏性可以移除大约20%的MLP参数，并将困惑度保持在约2%的密集基线范围内。该方法完全在现有检查点后进行操作，不需要梯度、校准集或路由器训练。
## 665. `cs.LG` - 可解释的公平聚类 [PDF](https://arxiv.org/pdf/2511.21109), [HTML](https://arxiv.org/abs/2511.21109)
### Authors
Mudi Jiang,Jiahui Zhou,Xinying Liu,Zengyou He,Zhikui Chen
### Background
近年来，公平聚类在涉及社会敏感属性的应用中越来越受到关注。然而，现有的公平聚类方法通常缺乏可解释性，这限制了它们在高风险场景中的应用，因为在这些场景中理解聚类决策背后的理由至关重要。
### Innovation
本文提出了一种可解释且公平的聚类框架，该框架将公平性约束整合到决策树的结构中，构建出可解释的决策树来对数据进行分区，同时确保对保护群体的公平对待。此外，还提出了一种不需要调整公平性超参数的变体，通过在构建了无公平约束的树后进行后剪枝实现。
### Conclusion
广泛的实验证明，我们的方法不仅在聚类性能和公平性方面表现出色，还具有解释性和处理多个敏感属性的额外优势，这些优点使我们的方法能够在复杂公平约束下稳健运行，开拓了公平和透明聚类的新可能性。
## 666. `cs.LG` - BRIDGE: 在领域引导程序验证中构建领域表示 [PDF](https://arxiv.org/pdf/2511.21104), [HTML](https://arxiv.org/abs/2511.21104)
### Authors
Robert Joseph George,Carson Eisenach,Udaya Ghai,Dominique Perrault-Joncas,Anima Anandkumar,Dean Foster
### Background
大语言模型（LLMs）在代码生成方面取得了令人瞩目的成就，但在程序验证，特别在如Lean4这样的交互式证明框架中表现不佳。一个主要挑战是可扩展性：验证合成不仅要生成代码，还需要精确的规范和正确的证明，而现有方法很少在这三个领域都有效。BRIDGE首次系统地研究了结构化提示，以实现可扩展的验证程序生成。
### Innovation
BRIDGE将验证分解为三个相互连接的领域：代码（可执行实现）、规范（正式意图声明）和证明（建设性正确性论证）。其关键理念是唤起不同的推理行为，即基于功能、基于规范和基于证明，作为中间表示，保留语义结构并连接这三个领域。通过系统性的删减实验表明，这种方法在准确性和效率方面表现出显著改善，尤其是功能推理在形式语言（Lean4）中提高了代码正确性，接近1.5倍；在推理计算效率上，功能推理也提高了2倍，具有更高的通过率和更低的总采样预算。
### Conclusion
BRIDGE为通过专家迭代或RLVR进行训练打下了基础，使模型能够在代码、规范和证明中内化这些推理策略。这些发现表明，领域内细粒度对齐是推进验证合成的一种有前途的方法。
## 667. `cs.LG` - 封闭世界的大型语言模型引导的开放世界强化学习中的目标图增强规划 [PDF](https://arxiv.org/pdf/2511.20993), [HTML](https://arxiv.org/abs/2511.20993)
### Authors
Shanwei Fan
### Background
大语言模型（LLMs）在强化学习（RL）中通过将任务分解为子目标提供了强大的高层规划能力。然而，它们在实际应用中的效用受限于规划执行不对齐的问题，这反映了从抽象计划到环境兼容的可执行行为间的关键差距。这种不对齐来源于两个相互关联的限制：(1) LLMs生成的子目标虽然在语义上合理但在目标环境中的实施却不可行或无关联，因为缺乏环境特定的知识作为支撑，(2) 单个LLM规划将生成与自我验证混淆，导致过于自信但不可靠的子目标，这些目标在执行时经常失败。
### Innovation
提案了一种名为Subgoal Graph-Augmented Actor-Critic-Refiner（SGA-ACR）的框架，该框架结合了环境特定的子目标图和结构化的实体知识，并引入了一个多LLM规划流水线，该流水线明确分离生成、批判和校正步骤，以生成可执行和可验证的子目标。一个子目标跟踪器进一步监控执行进展，提供辅助奖励，并自适应地更新子目标图以保持计划与行动之间的对齐。
### Conclusion
在开放世界游戏‘Crafter’中22个多样化的任务上进行的实验表明，所提出的方法是有效的。
## 668. `cs.LG` - 从比特到轮次：探索性并行解码方法在扩散语言模型中的应用 [PDF](https://arxiv.org/pdf/2511.21103), [HTML](https://arxiv.org/abs/2511.21103)
### Authors
Hengyu Fu,Baihe Huang,Virginia Adams,Charles Wang,Venkat Srinivasan,Jiantao Jiao
### Background
扩散语言模型（DLMs）作为一种快速推理且与自回归语言模型（LMS）具有相近准确性的对比模型正在兴起。然而，标准的DLM解码策略依赖于高置信度的令牌存在信息论上的瓶颈，这限制了解码进度并最终减缓了生成过程。
### Innovation
本文证明了优先处理高置信度令牌是有内在效率低下。证明了解码轮次的数量必须与样本的总信息呈线性增长，并与每个轮次的信息预算呈反比。提出了Explore-Then-Exploit（ETE）解码策略，这是一种无需训练的方法，旨在最大化信息通量和解码效率。ETE结合跨块解码和针对高不确定性令牌的探索来重构条件分布并触发一系列有信心的预测。
### Conclusion
实验验证了理论界限，并证明ETE相比仅依赖置信度的基线策略，能够减少所需的解码轮次，同时不牺牲生成质量。
## 669. `cs.LG` - 线下数据选择与在线自我提炼生成的统一理解：针对后训练大语言模型 [PDF](https://arxiv.org/pdf/2511.21056), [HTML](https://arxiv.org/abs/2511.21056)
### Authors
Quan Xiao,Tianyi Chen
### Background
在适应大型语言模型（LLMs）到特定下游任务方面，数据质量的提升依赖于线下数据选择和在线自我提炼生成这两个关键步骤。作者通过优化视角解决线下数据选择和在线自我提炼生成的问题。
### Innovation
引入了二层数据选择框架（bilevel data selection），用于线下数据选择，这种方法依赖于验证集；将在线自我提炼生成视为当前响应训练的模型适应步骤，选择最符合验证数据的模型。通过赋予权重，作者提供了一个统一视角来看待离线数据选择和自我提炼生成，且首次证明了二层数据选择框架的有效性。
### Conclusion
结合线下数据和验证加权在线生成，此方法提升了微调性能。实验表明此方法在质量和安全性方面都能有效提升大语言模型的微调效果。
## 670. `cs.LG` - 时序扩散规划 [PDF](https://arxiv.org/pdf/2511.21054), [HTML](https://arxiv.org/abs/2511.21054)
### Authors
Jiaming Guo,Rui Zhang,Zerun Li,Yunkai Gao,Shaohui Peng,Siming Lan,Xing Hu,Zidong Du,Xishan Zhang,Ling Li
### Background
扩散规划是一种有潜力的方法，可以从离线数据中学习高性能策略。然而，以前的工作在每个时间步生成新的计划，这带来了显著的计算开销，降低了决策频率，并且频繁的计划切换也会影响性能。
### Innovation
提出了一种名为时序扩散规划（TDP）的新方法，通过在时间维度上分散去噪步骤来提高决策效率。TDP 起初生成一个随着时间变得愈发模糊的初始计划。在后续的每个时间步，TDP 通过少量的去噪步骤更新前一个计划，从而降低了平均去噪步骤的数量，提高了决策效率。此外，引入了自动重新规划机制，以防止计划与现实之间产生重大偏差。
### Conclusion
实验结果表明，与每次时间步生成新计划的方法相比，TDP 在提高决策频率方面提高了 11-24.8 倍，同时实现了更高的或相当的性能。
## 671. `cs.LG` - 边缘规模的信任缺失联邦学习：分布、可验证和激励对齐协调的组合架构 [PDF](https://arxiv.org/pdf/2511.21118), [HTML](https://arxiv.org/abs/2511.21118)
### Authors
Pius Onobhayedo,Paul Osemudiame Oamen
### Background
人工智智能技术的发展正逐步从互联网的集中式提供模式转变为分布式的创造模式。起初，资源密集型的计算集中在有能力进行模型训练和大规模服务的机构中。随着联邦学习技术的发展，数以亿计的边缘设备将能够共同改进模型，无需透露原始数据，从而实现大规模的贡献和消费。然而，由于某些组合性缺口，这一民主愿景尚未实现。这些缺口包括：聚合器处理更新时缺乏问责制、缺乏经济机制以及即使存在也容易被操纵、协调使状态修改序列化，从而限制了扩展性，以及治理结构允许进行追溯操纵。
### Innovation
本文通过利用加密收据来证明聚合的正确性，几何新颖性测量来防止激励游戏，平行对象所有权实现线性扩展，以及时间锁定的政策来检查追溯操纵，来解决这些缺口，从而实现信任缺失的边缘规模联邦学习，提供去中心化、可验证和激励对齐的协调机制。
### Conclusion
本文提出了一种新型的组合架构，通过加密收据、几何新颖性测量、平行对象所有权和时间锁定政策，解决了联邦学习中的信任缺失问题，实现了高效、可验证的分布式学习框架，为大规模节点参与和互不信任环境下的隐私保护和效率提升提供了可能。
## 672. `cs.LG` - 生成性早期阶段排名 [PDF](https://arxiv.org/pdf/2511.21095), [HTML](https://arxiv.org/abs/2511.21095)
### Authors
Juhee Hong,Meng Liu,Shengzhi Wang,Xiaoheng Mao,Huihui Cheng,Leon Gao,Christopher Leung,Jin Zhou,Chandra Mouli Sekar,Zhao Zhu,Ruochen Liu,Tuan Trieu,Dawei Sun,Jeet Kanjani,Rui Li,Jing Qian,Xuan Cao,Minjie Fan,Mingze Gao
### Background
大规模推荐系统通常采用多阶段级联排名系统模式来平衡效果和效率。早期阶段排名(ESR)系统采用“用户-项目解耦”方法，独立学习的用户和项目表示在最后一层才结合，虽然这种设计效率高，但难以捕捉用户与项目之间的细粒度关联和其他信号，从而在效果上有局限性。
### Innovation
为了克服这些限制，本文提出了生成性早期阶段排名(GESR)范式，引入了混合注意力(MoA)模块，该模块利用多种注意力机制填补效果差距：硬匹配注意力(HMA)模块通过计算用户和项目特征之间的原始匹配数量，编码显式的跨信号；目标感知自我注意力模块根据项目生成目标感知的用户表示，使学习更个性化；交叉注意力模块促进用户和项目特征的早期和更丰富的互动。MoA专有的注意力编码在最终层通过多逻辑参数化门控(MLPG)模块进一步优化，整合了新学习的嵌入并通过门控机制生产次级逻辑，然后与主逻辑融合。
### Conclusion
所提出的GESR范式在关键指标、参与度和消费任务中表现出显著改进，通过离线和在线实验得到了验证。据我们所知，这是首次在ESR阶段成功部署全目标感知注意力序列建模。
## 673. `cs.LG` - 动态分层对比学习与上节点增广在混合整数线性规划分支中的应用 [PDF](https://arxiv.org/pdf/2511.21107), [HTML](https://arxiv.org/abs/2511.21107)
### Authors
Tongkai Lu,Shuai Ma,Chongyang Tao
### Background
混合整数线性规划(MILP)是一类NP难问题，受到了学术界和工业界的广泛关注。分支定界(B&B)方法是解决MILP的主要方法，而分支策略在B&B方法中起着关键作用。近年来，基于神经网络的学习框架被开发出来以增强分支策略和求解MILP的效率，但它们仍然面临着深层语义变化、上游节点稀缺以及收集强分支样本成本高的问题。
### Innovation
本文提出了一个动态分层对比训练框架(Dynamic Stratified Contrastive Training Framework for MILP Branching，简称textbackslash ours)，该框架基于节点特征分布对分支定界节点进行分组，并训练基于GCNN的区分模型，逐步分离节点组，学习树中的精细节点表示。为了应对上节点的数据稀疏性和不平衡性，引入了一种上节点增广的MILP生成过程，该过程生成了既是理论等价又是扰动的实例。textbackslash ours能够有效建模节点之间的微妙语义差异，显著提高了分支准确性并减少了求解时间，特别是在处理上游节点时表现突出。
### Conclusion
在标准MILP基准测试上的大量实验表明，该方法提高了分支准确性，缩短了求解时间，并且能够很好地迁移应用到未见过的实例中。
## 674. `cs.LG` - G-Net: 一证明有效的高精度随机二元神经网络构建方法 [PDF](https://arxiv.org/pdf/2511.21063), [HTML](https://arxiv.org/abs/2511.21063)
### Authors
Alireza Aghasi,Nicholas Marshall,Saeid Pourmand,Wyatt Whiting
### Background
该研究背景基于高维计算(HDC)，这是一种受大脑启发的计算范式，利用高维向量表示，提供高效的硬件实现并具有对模型损坏的鲁棒性。传统的低精度方法通常使用量化技术，而本研究考虑将数据表示为超立方体中的二进制嵌入点，并利用汉明距离。研究者提出了一个新的浮点神经网络家族叫做G-Nets，这种网络能够模仿标准的网络层。
### Innovation
该研究的主要创新在于提出了一种新的浮点神经网络家族G-Nets，这些网络通过随机生成二进制嵌入，能够保留其浮点版本的精度。由于测量的集中，这种嵌入提供了理论保证。实验证明，这种二进制模型在匹配卷积神经网络精度的同时，显著优于之前的HDC模型，例如，在CIFAR-10数据集上，其准确率比之前的HDC模型高约30%。G-Nets是神经网络和随机二进制神经网络之间的一个理论依据桥梁，开辟了构建鲁棒的二进制/量化深度学习模型的新方向。
### Conclusion
G-Nets通过这一理论依据桥梁，在理论上证明了其在构建高精度随机二元神经网络方面的可行性，其实施代码可公开获取，有望推动二进制/量化深度学习模型的进一步研究和应用。
## 675. `cs.LG` - 如何正确报告使用LLM作为评判者的评估 [PDF](https://arxiv.org/pdf/2511.21140), [HTML](https://arxiv.org/abs/2511.21140)
### Authors
Chungpa Lee,Thomas Zeng,Jongwon Jeong,Jy-yong Sohn,Kangwook Lee
### Background
近年来，大型语言模型（LLMs）越来越多地被用作评判者替代人类。尽管它们在可扩展性方面表现出色，但其评判结果由于模型的精确特异性和灵敏度不够完美，变得具有偏差，从而影响了准确性的估计。尽管已经存在一些偏差校正的方法，但这些方法在LLM研究中应用并未广泛，通常还依赖于对模型精确特异性和灵敏度的完全了解。实际上，我们只对这些值有估计，并不清楚如何仅使用估计值来恰当构建不确定性区间。
### Innovation
本文提出了一种简单的插件框架，用来修正上述偏差，并通过考虑测试数据集和校准数据集的不确定性来构建置信区间。此外，为了降低准确度估计的不确定性，引入了一种高效的自适应算法来分配校准样本的大小。
### Conclusion
这种方法使得基于LLM的评估既实用又具有统计意义。通过这种方法，可以更准确地报告使用LLM作为评判者的评估结果，减少了偏差和不确定性的影响。
## 676. `cs.LG` - 学习细胞感知的层次化多模态表示以实现稳健的分子建模 [PDF](https://arxiv.org/pdf/2511.21120), [HTML](https://arxiv.org/abs/2511.21120)
### Authors
Mengran Li,Zelin Zang,Wenbin Xing,Junzhou Chen,Ronghui Zhang,Jiebo Luo,Stan Z. Li
### Background
理解化学干扰如何在生物系统中传播对于分子属性预测至关重要。虽然大多数现有方法仅关注化学结构，但最近的研究突显了细胞响应（如形态和基因表达）在塑造药物效果中的关键作用。然而，当前的细胞感知方法面临两个主要局限：（1）外部生物数据在各模态上的不完整性，（2）分子、细胞和基因组水平之间层次依赖关系建模不足。
### Innovation
本文提出了一种名为CHMR（Cell-aware Hierarchical Multi-modal Representations）的稳健框架，该框架联合建模了分子和细胞响应之间的局部-全局依赖性，并通过新颖的树形结构向量量化模块捕获了潜在的生物层次结构。在九个公共基准测试中的728个任务上进行了评估，CHMR在分类和回归任务上的平均改进分别达到了3.6%和17.2%，证明了层次感知的多模态学习在可靠和生物合理的分子表示中的优势。
### Conclusion
该结果表明，对于综合生物医学建模，层次感知的多模态学习提供了一种可推广的框架。代码可在如下链接下载：this https URL.
## 677. `cs.LG` - 快速mRMR特征选择在高维组学数据中的鲁棒基因优先排序 [PDF](https://arxiv.org/pdf/2511.21211), [HTML](https://arxiv.org/abs/2511.21211)
### Authors
Rubén Fernández-Farelo,Jorge Paz-Ruza,Bertha Guijarro-Berdiñas,Amparo Alonso-Betanzos,Alex A. Freitas
### Background
基因优先排序（识别可能与生物学过程相关的基因）越来越多地使用人工智能解决。然而，现有的方法在处理生物医学数据的高维度性和标签不完整问题时表现不佳。
### Innovation
本文提出了一种更稳健且高效的管道，利用快速mRMR特征选择，保留仅相关、无冗余的特征以供分类器使用。这一技术使得能够构建更简单且更有效的模型，并且可以结合不同的生物特征集合。
### Conclusion
在饮食限制数据集上的实验表明，与现有方法相比表现出显著的改进，证明了特征选择对于可靠基因优先排序至关重要。
## 678. `cs.LG` - I-GLIDE: 输入组用于降解估计中的潜在健康指标 [PDF](https://arxiv.org/pdf/2511.21208), [HTML](https://arxiv.org/abs/2511.21208)
### Authors
Lucas Thil,Jesse Read,Rim Kaddah,Guillaume Doquet
### Background
准确预测剩余使用寿命（RUL）依赖于健康指标（HIs）的质量，然而现有方法常常无法在多传感器系统中拆解复杂的退化机制，也无法量化HIs可靠性的不确定性。因此，提高HIs的质量和鲁棒性是提高RUL预测准确性的关键。
### Innovation
该论文提出了一种新的框架，其包含三大创新贡献：首先，首次将Reconstruction along Projected Pathways (RaPP) 用于RUL预测，表明它优于传统重建错误度量。其次，通过Monte Carlo dropout和概率潜在空间，增强RaPP衍生的HIs的不确定性量化，显著提高了RUL预测的鲁棒性。第三，提出了指标组的概念，将传感器子集隔离以建模系统特定的退化，从而提出了一种新的方法I-GLIDE，该方法实现机制特定的诊断并具有可解释性。
### Conclusion
通过在航空和制造业系统数据上的测试，该方法在准确性、泛化能力上都优于最先进的HI方法，提供了有关系统失效路径的可操作见解。该工作填补了异常检测与预测之间的空白，提供了复杂系统中不确定性感知退化建模的方法论框架。
## 679. `cs.LG` - Spiking Neural Networks中的联邦学习隐私 [PDF](https://arxiv.org/pdf/2511.21181), [HTML](https://arxiv.org/abs/2511.21181)
### Authors
Dogukan Aksu,Jesus Martinez del Rincon,Ihsen Alouani
### Background
随着嵌入式和边缘人工智能的进步，脉冲神经网络(SNNs)变得尤为重要，因为它们较低的能耗使其在能源预算受限的场景中比传统的人工神经网络(ANNs)更为高效。在同时，联邦学习(FL)已成为处理这些场景中敏感数据隐私的理想选择，它允许设备上的学习而限制了原始数据的暴露。然而，梯度反转攻击构成了FL中一个重要的隐私威胁，这些敏感的训练数据可以直接从共享的梯度中重建出来。尽管这种漏洞已经广泛在传统的ANNs中被研究，但是SNNs在此方面的影响仍很少被探讨。
### Innovation
本文首次进行了SNNs在不同数据领域的梯度泄漏综合实证研究。我们提出了一个假设，即由于SNNs是通过代理梯度进行训练的，这些代理梯度与原始输入的相关性较低，因此从隐私角度看，这些梯度更不具有信息性。我们的攻击实验揭示了一个与传统ANNs形成鲜明对比的结果：ANN的梯度可靠地揭示了关键的输入内容，而SNN的梯度则产生无序的、时间不一致的重建结果，无法恢复有意义的空间或时间结构。这项研究表明，即使是在代理梯度训练和时间驱动动态模型的结合下，梯度的信息性也显著降低。我们还提供了首个针对SNN架构系统的梯度反转攻击的基准测试，明确强调了类神经计算自身的固有隐私保护潜力。
### Conclusion
本研究提供了第一个针对SNN架构的梯度反转攻击系统基准测试，表明代理梯度训练和事件驱动动力学结合显著降低了梯度信息性，这表明SNNs拥有固有的隐私保护潜力。
## 680. `cs.LG` - 一种数据驱动的结构地震响应建模的物理约束U-net-LSTM网络 [PDF](https://arxiv.org/pdf/2511.21276), [HTML](https://arxiv.org/abs/2511.21276)
### Authors
Sutirtha Biswas,Kshitij Kumar Yadav
### Background
准确高效的地震响应预测对于设计抗震结构至关重要。虽然有限元方法（FEM）仍然是非线性地震分析的标准方法，但其高计算需求限制了其扩展性和实时应用。近年来，特别是在卷积神经网络（CNNs）、循环神经网络（RNNs）和长短时记忆（LSTM）模型方面的发展，显示出在减少结构非线性地震分析的计算成本方面的潜力。然而，这些基于数据的方法往往难以泛化并捕捉到物理本质，从而降低了可靠性。
### Innovation
我们提出了一种新的物理信息U-net-LSTM框架，该框架将物理定律与深度学习相结合，以提高准确性和效率。通过将领域特定约束嵌入学习过程中，所提出模型在传统的机器学习架构上实现了更好的预测性能。这种方法在纯数据驱动方法和基于物理建模之间架起了一座桥梁，提供了构建抗震结构地震响应预测的鲁棒且计算效率高的替代方案。
### Conclusion
通过将特定领域的物理约束嵌入学习过程，提出的U-net-LSTM框架在传统的机器学习架构上实现了更好的预测性能，并提供了一种在非线性地震分析中的鲁棒且计算效率高的方法，从而填补了纯数据驱动方法和基于物理的建模之间的空白。
## 681. `cs.LG` - 时间序列去噪隐式扩散模型的锯齿采样 [PDF](https://arxiv.org/pdf/2511.21320), [HTML](https://arxiv.org/abs/2511.21320)
### Authors
Heiko Oppel,Andreas Spilz,Michael Munz
### Background
Denoising Diffusion Probabilistic Models (DDPMs)能够生成合成的时间序列数据，以提升分类器的表现，但其采样过程计算成本较高。
### Innovation
结合隐式扩散模型与创新性的锯齿采样器，加速逆过程并可应用于任何预训练的扩散模型。该方法在不牺牲生成序列质量的情况下，实现了标准基线的30倍加速。
### Conclusion
研究通过锯齿采样方法提高了扩散模型在时间序列去噪中的效率，同时保持了生成序列的质量，为分类任务中的时间序列数据生成提供了新的途径。
## 682. `cs.LG` - TSGM: 使用得分生成模型进行规则和不规则时间序列生成 [PDF](https://arxiv.org/pdf/2511.21335), [HTML](https://arxiv.org/abs/2511.21335)
### Authors
Haksoo Lim,Jaehoon Lee,Sewon Park,Minjung Kim,Noseong Park
### Background
得分生成模型（SGMs）在多个领域，如图像生成、语音合成以及表格数据合成等方面展示了无与伦比的采样质量和多样性。受其卓越成果的启发，我们将SGMs应用于时间序列的生成，通过学习其条件得分函数。
### Innovation
我们提出了一个条件得分网络，用于时间序列合成，并且特定地设计了一种噪声得分匹配损失函数，以适应我们的需求。我们的框架足够灵活，可以合成规则和不规则时间序列，同时对模型设计的调整非常小。结果表明，在各种时间序列数据集上，我们获得了出色的合成性能，达到了最先进的采样多样性和质量。
### Conclusion
我们通过得分生成模型成功地生成了规则和不规则时间序列，验证了其在时间序列合成任务中的表现优异，达到了最先进的水平。
## 683. `cs.LG` - 科学应用中机器学习实验的最佳实践 [PDF](https://arxiv.org/pdf/2511.21354), [HTML](https://arxiv.org/abs/2511.21354)
### Authors
Umberto Michelucci,Francesca Venturini
### Background
机器学习（ML）在科学研究中的应用越来越普遍，然而实验设计和记录的质量和可靠性会影响到研究结果的准确性和可靠性。常见的问题包括较差的基线、不一致的数据预处理或不充分的验证，这可能导致对模型性能的误导性结论。
### Innovation
本文提出了一套实用且结构化的指南，用于在科学应用中进行机器学习实验，强调可重复性、公平比较和透明报告。文中概述了一个从数据集准备到模型选择和评估的逐步工作流程，并提出了包括对过拟合和验证折中过拟合不稳定性计算的度量，如对数过拟合比率（LOR）和复合过拟合评分（COS）。通过推荐的实践和示例报告格式，本文旨在支持研究人员建立稳健的基线并从应用于科学问题的机器学习模型中得出有效证据的结论。
### Conclusion
本文通过推荐实践和示例报告格式，支持研究人员建立稳健的基线并从应用于科学问题的机器学习模型中得出有效证据的结论。
## 684. `cs.LG` - 在扩散语言模型中的掩盖可能具有干扰性：关于上下文理解的研究 [PDF](https://arxiv.org/pdf/2511.21338), [HTML](https://arxiv.org/abs/2511.21338)
### Authors
Julianna Piskorz,Cristina Pinneri,Alvaro Correia,Motasem Alfarra,Risheek Garrepalli,Christos Louizos
### Background
最近，掩码扩散语言模型（MDLMs）作为与自回归语言模型（ARLMs）的一种有前景的替代方案出现，利用一种去噪目标，理论上可以更均匀地利用上下文。然而，研究表明MDLMs仍然存在一些局限性。
### Innovation
这项研究揭示了MDLMs在上下文理解上的两个关键局限。首先，尽管MDLMs具有更全局的训练目标和双向注意力机制，它们仍然表现出位置偏差，即性能高度依赖于相关信息在输入中的位置，倾向于优先使用局部而非远处的上下文。其次，研究发现，在生成过程中添加大量掩码标记会严重降低上下文理解。研究人员提出了一种掩码无关的损失函数，以鼓励模型预测不依赖于添加的掩码数量，这通过Fine-tuning显著减轻了掩码的干扰效果，提高了MDLMs的鲁棒性。
### Conclusion
研究结果揭示了当前MDLM训练范式的关键限制，并提供了关于如何构建具有更强上下文理解能力的扩散型语言模型的实用见解。
## 685. `cs.LG` - BanglaMM-Disaster: 基于多模态变换器的深度学习框架，用于孟加拉语多类灾难分类 [PDF](https://arxiv.org/pdf/2511.21364), [HTML](https://arxiv.org/abs/2511.21364)
### Authors
Ariful Islam,Md Rifat Hossen,Md. Mahmudul Arif,Abdullah Al Noman,Md Arifur Rahman
### Background
孟加拉国仍面临重大自然灾害挑战，因此急需实时监测和快速响应系统。本文基于这一背景，提出了一种名为BanglaMM-Disaster的端到端深度学习多模态框架，用于使用社交媒体上孟加拉语的文本和视觉数据进行灾害分类。
### Innovation
本文创新地利用了基于变换器的文本编码器（如BanglaBERT、mBERT和XLM-RoBERTa）和卷积神经网络（如ResNet50、DenseNet169和MobileNetV2）对两种模态的数据进行处理。通过早期融合的方法，提出的模型在多个类别的分类准确性上达到了83.76%，显著超越了仅文本和仅图像基线模型，并减少了各类别的误分类，尤其是对模糊示例的改进更为明显。
### Conclusion
这项工作填补了孟加拉语多模态灾害分析的重要空白，并证明了在资源有限的环境中，结合多种数据类型对于实时灾害响应的益处。
## 686. `cs.LG` - 使用动态和激进排除方法在受污染训练数据中的异常检测 [PDF](https://arxiv.org/pdf/2511.21378), [HTML](https://arxiv.org/abs/2511.21378)
### Authors
Jungi Lee,Jungkwon Kim,Chi Zhang,Kwangsun Yoo,Seok-Joo Byun
### Background
在异常检测中处理受污染数据是一项关键挑战，因为传统模型假设纯正常数据的训练。常规方法通过依赖固定的污染比例来减轻污染影响，但在假设比重要和实际比例的差异会导致性能严重下降，特别是在噪声环境中，正常和异常数据分布重叠。
### Innovation
我们提出了自适应和激进排斥（AAR）方法，这是一种新颖的方法，它使用修改后的z分数和基于高斯混合模型的阈值来动态排除异常。AAR通过结合硬性和软性拒斥策略有效平衡保留正常数据和排除异常之间的权衡。
### Conclusion
通过对两个图像数据集和三十个表格数据集的广泛实验表明，AAR比最先进的方法在AUROC上提高了0.041。通过提供一种可扩展且可靠的解决方案，AAR增强了对受污染数据集的鲁棒性，为安全和医疗等领域中的更广泛实际应用铺平了道路。
## 687. `cs.LG` - Hybrid-AIRL: 通过监督专家指导增强逆向强化学习 [PDF](https://arxiv.org/pdf/2511.21356), [HTML](https://arxiv.org/abs/2511.21356)
### Authors
Bram Silue,Santiago Amaya-Corredor,Patrick Mannion,Lander Willem,Pieter Libin
### Background
逆向强化学习(AIRL)通过从专家演示中推断密集奖励函数已在缓解强化学习(RL)中的稀疏奖励问题方面展现出潜力。然而，在高度复杂且存在不完全信息的情况下，其性能尚未得到充分探索。因此，本文旨在通过在Heads-Up Limit Hold'em (HULHE) 棋牌游戏中评估AIRL来填补这一空白，HULHE是稀疏、延迟奖励以及显著不确定性特征的领域。
### Innovation
本文贡献了Hybrid-AIRL (H-AIRL)，通过结合来自专家数据的监督损失以及随机正则化机制，增强奖励推断和策略学习。H-AIRL在精心选择的Gymnasium基准和HULHE扑克环境中得到了评估，并通过可视化学习到的奖励函数来加深对学习过程的理解。
### Conclusion
研究结果表明，H-AIRL相比AIRL在样本效率和学习稳定性方面都有更好的表现，突显了将监督信号纳入逆向RL的好处，并建立了H-AIRL作为解决挑战性和实际应用场景的有前景框架。
## 688. `cs.LG` - 主观深度和时间尺度变换器：学习何时何地进行计算 [PDF](https://arxiv.org/pdf/2511.21408), [HTML](https://arxiv.org/abs/2511.21408)
### Authors
Frederico Wieser,Martin Benfeghoul,Haitham Bou Ammar,Jun Wang,Zafeirios Fountas
### Background
在标准Transformer架构中，计算的刚性和均一分配限制了其效率和可扩展性，尤其是在大规模模型和长序列处理时。为了解决这些问题，论文提出了 Subjective Depth Transformers (SDT) 和 Subjective Timescale Transformers (STT) 两种新架构，利用贝叶斯意外信号动态路由计算，学会在解码器中什么时候以及在哪里进行计算。
### Innovation
SDT 和 STT 架构通过引入交替的决策层和动态层，并使用固定容量的 Top-K 路由基于贝叶斯意外（预期变化和未预期变化）来动态执行计算。SDT 扩展了解码器堆栈，而 STT 则进一步将这种条件计算扩展到时间领域，通过预测残差更新来管理 KV 缓存贡献。这两种方法都在训练过程中表现出对新颖性和预测性门控行为的变化，证明了与意外性原则的对齐，并提供了有限的实验结果，以探索条件计算中的计算精度权衡。
### Conclusion
提出的架构创建了一个灵活的框架，通过减少每一层的自我注意计算量75%和 KV 缓存需求量50%，提高了模型的效率，开辟了更高效模型的道路。
## 689. `cs.LG` - 数据流中分类器投票线性独立性视角的集成性能 [PDF](https://arxiv.org/pdf/2511.21465), [HTML](https://arxiv.org/abs/2511.21465)
### Authors
Enes Bektas,Fazli Can
### Background
集成学习通过组合多个基础分类器来提高分类性能。增加分类器的数量通常可以提升准确性，但过大的集成可能会导致计算效率低下和边际收益下降。本文通过数据流中分类器投票的线性独立性研究集成大小与性能之间的关系。
### Innovation
本文提出了一种新的理论框架，利用线性独立性来解释集成大小与准确性的权衡关系。该框架通过建模分类器输出达到线性独立性的概率进行推导，并应用于两种集成方法OzaBagging和GOOWE。结果显示，理论估计能有效识别稳健集成模型的性能饱和点，对于复杂权重方案，框架揭示了高理论多样性可能引发的算法不稳定性。
### Conclusion
我们通过实际和合成数据集验证了理论，并提出了计算线性独立性概率的方法来确定所需的集成大小。研究表明，这种理论能有效指导集成大小的优化。我们的实施已公开，以支持研究的再现性和未来研究。
## 690. `cs.LG` - 控制注意力Logits的变化 [PDF](https://arxiv.org/pdf/2511.21377), [HTML](https://arxiv.org/abs/2511.21377)
### Authors
Ben Anson,Laurence Aitchison
### Background
在训练变压器模型时，神经网络权重的稳定性至关重要。特别地，查询和键权重往往会增大，如果不进行干预就会导致稳定性问题。虽然已有的`QK norm`方法可以解决这些问题，但在某些应用场景中并不适用，例如与Multi Latent Attention（MLA）不兼容，因为`QK norm`要求推理过程中完全物质化查询和键权重，这在MLA中并未实现。
### Innovation
本文提出通过为查询和键权重分配参数依赖的学习率来控制Logits的变化，这是一种低成本的干预手段。这种方法不仅允许网络的基学习率提高，还在使用Multi-head Attention的情况下表现出色，并且在性能上可以与`QK norm`相当。
### Conclusion
实验表明，通过精细控制权重变化的方法可以提升网络基学习率，克服了`QK norm`与MLA不兼容的问题，并且在使用Multi-head Attention时达到了与`QK norm`相近的效果。
## 691. `cs.LG` - SUPN: Shallow Universal Polynomial Networks [PDF](https://arxiv.org/pdf/2511.21414), [HTML](https://arxiv.org/abs/2511.21414)
### Authors
Zachary Morrow,Michael Penwarden,Brian Chen,Aurya Javeed,Akil Narayan,John D. Jakeman
### Background
德普神经网络（DNNs）和柯莫哥洛夫-阿诺德网络（KANs）因其灵活性和表现力而广泛用于函数逼近。然而，它们通常需要大量的可训练参数来产生合适的逼近，这使得网络不透明，并且创建了大的优化空间，可能导致训练中的局部极小值，这些极小值具有不同的泛化误差。在这种情况下，网络初始化对模型的外样准确性有重要的影响。
### Innovation
本文提出了浅层通用多项式网络（SUPNs）。它们除了最后一隐藏层外，用具有可学习系数的多项式层替换所有其他隐藏层，这样利用了DNNs和多项式的优点，以显著减少参数数量来实现足够的表达力。证明了SUPNs的收敛速度与相同级别的最优多项式逼近相同，并得到了准最佳SUPN参数的显式公式。并且在包含SUPNs、DNNs、KANs和多项式投影的大量数值实验中，与DNNs和KANs相比，对于给定的可训练参数数量，SUPNs在函数逼近误差和变异性方面通常低一个数量级。在我们的示例中，SUPNs甚至在非光滑函数上也超过了多项式投影。
### Conclusion
SUPNs在可训练参数数量给定时实现了更好的逼近误差和更小的变异率。在非光滑函数上，即使在多项式投影上也表现出优越的性能。
## 692. `cs.LG` - 计算非线性分类器的战略响应 [PDF](https://arxiv.org/pdf/2511.21560), [HTML](https://arxiv.org/abs/2511.21560)
### Authors
Jack Geary,Boyan Gao,Henry Gouk
### Background
该研究关注的是战略分类问题，其中分类器的应用会引发战略行为，导致后续观察数据分布的变化。目前针对战略设置下的分类器学习方法主要集中在线性分类器上，但在许多情况下，非线性分类器更为合适。然而，非线性分类器的主要限制在于难以计算出最佳响应。
### Innovation
该研究提出了一种新颖的方法，通过优化代理目标函数的拉格朗日对偶来计算最佳响应，可以在线性设置中重现现有方法的结果，并且特别适用于非线性分类器设置，可用于评估和训练。
### Conclusion
研究表明该方法在非线性分类器设置中可以直接应用，并且对于评估和训练都是有用的。同时揭示了现有方法的关键弱点，有助于未来的改进。
## 693. `cs.LG` - Lost in Time? 一种具有时间偏移容差的生理信号转换元学习框架 [PDF](https://arxiv.org/pdf/2511.21500), [HTML](https://arxiv.org/abs/2511.21500)
### Authors
Qian Hong,Cheng Bian,Xiao Zhou,Xiaoyu Li,Yelei Li,Zijing Zeng
### Background
将无创信号（如光电容积描记法[PPG]和球感心图[BCG]）翻译为临床意义信号（如动脉血压[ABP]）对于持续、低成本的医疗监控至关重要。然而，多模态信号转换中的时间对齐问题会损害转换准确性，尤其是在捕捉关键特征（如ABP峰值）方面尤为明显。传统的同步方法往往依赖于较强的相似性假设或手动调校，而现有的有噪声标签学习（LNL）方法在时间偏移监督下表现出色，要么丢弃大量数据，要么无法正确纠正标签偏移。为解决这一问题，我们提出了一种基于元学习的双层优化框架ShiftSyncNet，该框架自动缓解由于时间偏移造成的性能下降。ShiftSyncNet由转换网络（TransNet）和时间偏移校正网络（SyncNet）组成，其中SyncNet学习训练对之间的时间偏移，并通过傅里叶相位移对监督信号进行对齐。
### Innovation
ShiftSyncNet是一种基于元学习的双层优化框架，它通过自动生成时间偏移校正网络（SyncNet）来自动缓解因时间偏移而导致的性能下降。SyncNet能够学习训练对之间的时序偏移，并应用傅里叶相位移来校准监督信号，从而提高信号转换的准确性。
### Conclusion
实验结果表明，ShiftSyncNet在三个数据集上分别比强大的基线方法提高了9.4%、6.0%和12.8%，证实了它在纠正时间偏移、提高标签质量和增强跨多种偏移场景下转换准确性方面的有效性，为其解决多模态生理信号在时间一致性方面存在的问题提供了一个统一的方向。
## 694. `cs.LG` - 定向预测变化 - 有效可靠的地方特征归因方法的保真度评估 [PDF](https://arxiv.org/pdf/2511.21363), [HTML](https://arxiv.org/abs/2511.21363)
### Authors
Kevin Iselborn,David Dembinsky,Adriano Lucieri,Andreas Dengel
### Background
当前的保真度评价指标依赖于蒙特卡洛近似，需要多次模型评估，并且由于随机抽样引入了不确定性。这种方法并不满足在高风险医疗环境中需要准确描述模型决策过程的临床医生和监管机构的需求。因此，有必要提出一种新的保真度评价指标，以解决现有方法中的问题。
### Innovation
本文提出了改进的定向预测变化（DPC）方法，通过修改现有的预测变化（PC）指标并在引导性扰动实验中引入扰动和归因的方向性，不仅获得了近十倍的速度提升，还消除了随机性，提供了一种确定性和可信赖的、衡量局部归因方法保真度的测评程序，可以准确反映局部Infidelity的性质。
### Conclusion
DPC已经在两个数据集（皮肤病变图像和金融表格数据）、两种黑盒模型以及七种解释算法中进行了评估，并涵盖了一系列超参数。通过对4744种不同解释结果的分析，该研究证明了DPC与PC能够全面且高效地评估基准导向和地方归因方法，同时提供了确定性和可复现的结果。
## 695. `cs.LG` - 未观察到上下文的上下文特定因果图发现：非平稳性、制度和时空模式 [PDF](https://arxiv.org/pdf/2511.21537), [HTML](https://arxiv.org/abs/2511.21537)
### Authors
Martin Rabel,Jakob Runge
### Background
在气候应用等实际应用中，数据通常为时空格网时间序列数据或具有类似结构的数据。尽管系统在空间和时间上的行为被认为是相似的，但存在的变化对该分析的重要性不能被忽视，这些变化可能会对假设局部平移不变性的算法的稳定性、收敛性和可靠性产生负面影响。研究人员开始关注近年来用于发现因果关系的基于约束的方法，并着眼于时空变化编码的信息。这种方法旨在解决稳定性问题，通过分析因果图的变化来缓解这些问题。
### Innovation
开发了一种由基于改进的约束因果发现方法构成的框架，这些方法在独立性测试方面得到了修改。这一框架极为模块化、易于扩展且广泛适用。它能利用现有的约束因果发现方法（如IID算法PC、PC-stable、FCI和时间序列算法PCMCI、PCMCI+、LPCMCI）进行改进，几乎无需修改。这种模块化设计可以系统地理解和改进一系列子问题，还能通过从变化点检测、聚类、独立性检验和其他相关研究中汲取灵感进行扩展。这种划分使理解基本限制、控制权衡的超参数以及结果的统计解释变得更加简化。
### Conclusion
通过设计的框架，可以更好地理解时空变化的影响，并系统地将其与因果发现方法结合起来，从而提高算法的稳定性和可靠性。作者指出，这一框架可以被利用其他相关领域的方法和技术进一步扩展和优化，为因果分析提供了新的框架和方法。开源实现将很快上线。
## 696. `cs.LG` - IntAttention：一种高效边缘推理的全整数注意流水线 [PDF](https://arxiv.org/pdf/2511.21513), [HTML](https://arxiv.org/abs/2511.21513)
### Authors
Wanli Zhong,Haibo Feng,Zirui Zhou,Hanyang Peng,Shiqi Yu
### Background
将Transformer模型部署到边缘设备上受限于延迟和能量预算。INT8量化虽然有效加速了主矩阵乘法运算，但使softmax成为主要瓶颈。这个阶段产生的去量化-softmax-再量化迂回操作可占用总注意力延迟的65%以上，破坏了边缘硬件优化所需端到端的整数数据流。
### Innovation
我们提出了IntAttention，一种无需重新训练即可无缝集成的全整数注意流水线。核心是IndexSoftmax操作符，它完全在整数域内替换浮点数指数运算。IntAttention集成了感知稀疏性的剪切、32条目查找表近似以及直接整数归一化，从而消除了所有数据类型转换开销。
### Conclusion
我们的方法在高保真精度下实现了与基线相当的领先增益，Armv8 CPU上比常规INT8注意流水线快2.0倍，能耗降低61%。在不同语言和视觉模型中实现了高达3.7倍的加速，提供了一种在经济型边缘设备上可实现高效Transformer推理的实际解决方案。代码将在后续版本中发布。
## 697. `cs.LG` - 基于电子健康记录的临床风险预测的机器学习方法：多尺度时间对齐 [PDF](https://arxiv.org/pdf/2511.21561), [HTML](https://arxiv.org/abs/2511.21561)
### Authors
Wei-Chen Chang,Lu Dai,Ting Xu
### Background
该研究提出了一种基于多尺度时间对齐网络（MSTAN）的风险预测方法，以解决电子健康记录（EHR）中时间不规律性、采样间隔差异以及多尺度动态依赖性的挑战。研究方法着重于对时间特征建模，通过引入可学习的时间对齐机制和多尺度卷积特征提取结构，共同建模EHR序列中的长期趋势和短期波动。该方法在输入层面，将多源临床特征映射为统一的高维语义空间，并使用时间嵌入和对齐模块动态加权不规则采样数据，减少时间分布差异对模型性能的影响。
### Innovation
研究创新之处在于提出了一种基于多尺度时间对齐网络的方法。该方法通过可学习的时间对齐机制和多尺度卷积特征提取结构，解决了EHR中的时间不规律性、采样间隔差异以及多尺度动态依赖性问题。这种方法能够动态加权不规则采样数据，减少时间分布差异对模型性能的影响。研究还通过多尺度特征提取模块捕获不同时间粒度下的关键模式，并通过注意力机制整合全局时间依赖性，生成个体层面的风险表示。
### Conclusion
在公开的EHR数据集上进行的实验表明，所提出的方法在精度、召回率、精确率和F1-Score方面都优于主流基线模型，证明了多尺度时间对齐在复杂医疗时序分析中的有效性和鲁棒性。该研究提供了对高维异步医疗序列进行智能表示的新解决方案，并为基于EHR的临床风险预测提供了重要的技术支撑。
## 698. `cs.LG` - 用于训练两层神经网络的均场极限方法 [PDF](https://arxiv.org/pdf/2511.21466), [HTML](https://arxiv.org/abs/2511.21466)
### Authors
William De Deyn,Michael Herty,Giovanni Samaey
### Background
研究了两层神经网络，并使用一种基于粒子的方法——共识优化(CBO)进行训练。比较了CBO与Adam优化器在两个测试案例中的性能，并展示了CBO与Adam的混合方法可以提供更快的收敛速度。在多任务学习的背景下，将CBO重新表述为一个具有较低内存开销的公式。CBO方法允许通过最优传输框架进行均场极限公式化，并在无限粒子数的极限下，定义Wasserstein-over-Wasserstein空间上的相应动力学。
### Innovation
提出了一种将CBO与最优传输框架结合的均场极限方法。通过这种方法，实现了更快的收敛速度，并定义了在无限粒子数极限下的Wasserstein-over-Wasserstein空间的动力学。
### Conclusion
CBO方法在训练两层神经网络时提供了更快的收敛速度，并且通过重新表述和结合均场极限公式化，减少了内存开销。最终定义了在无限粒子数极限下的相应动力学，并证明了这种方法具有单调减少的方差特性。
## 699. `cs.LG` - 基于Dyna-Q强化学习的预测性安全盾 [PDF](https://arxiv.org/pdf/2511.21531), [HTML](https://arxiv.org/abs/2511.21531)
### Authors
Jin Pin,Krasowski Hanna,Vanneaux Elena
### Background
获得强化学习的安全保证是实现实际任务应用的重要挑战。现有的安全盾通常通过随机抽样安全动作或固定备用控制器来实现硬性安全保证，这忽略了不同安全动作对未来性能的影响。
### Innovation
本文提出了一种预测性安全盾，用于基于模型的强化学习代理在离散空间中的应用。该安全盾基于安全预测局部更新Q函数，这些预测来源于环境模型的安全模拟。这种方法能够在保持硬性安全保证的同时提升性能。实验结果表明，即使预测的时域较短，也足以识别最优路径。并且这种方案对于分布偏移具有鲁棒性，例如模拟与真实环境之间的分布差异，无需额外训练。
### Conclusion
该预测性安全盾能够在保障安全性能的同时提升基于模型的强化学习代理的性能，并且对分布偏移具有鲁棒性。
## 700. `cs.LG` - BanglaASTE：一种用于孟加拉语电子商务评论中的方面-情感-观点提取的集成深度学习新框架 [PDF](https://arxiv.org/pdf/2511.21381), [HTML](https://arxiv.org/abs/2511.21381)
### Authors
Ariful Islam,Md Rifat Hossen,Abir Ahmed,B M Taslimul Haque
### Background
Aspect-Based Sentiment Analysis (ABSA) 已成为从用户生成的内容中提取细粒度情感见解的重要工具，特别是在电子商务和社交媒体领域。然而，由于缺乏全面的数据集和专门的 triplets 提取框架，孟加拉语的 ABSA 研究仍然被显著忽视。
### Innovation
本研究提出了 BanglaASTE，一种用于孟加拉语产品评论的 Aspect Sentiment Triplet Extraction (ASTE) 新颖框架，能够同时检测方面术语、情感表达和情感极性。我们的贡献包括：（1）创建了第一个包含 3,345 条产品评论的标记 Bangla ASTE 数据集，来自主要的电子商务平台，如 Daraz、Facebook 和 Rokomari；（2）开发了一种结合基于图的方面-意见匹配和语义相似性技术的混合分类框架；（3）结合 BanglaBERT 上下文嵌入和 XGBoost 提升算法实现了一种集成模型，以提高 triplet 提取性能。
### Conclusion
实验结果表明，我们的集成方法在所有评估指标上都显著优于基线模型，准确率为 89.9%，F1 得分为 89.1%。该框架有效地解决了孟加拉语文本处理中的关键挑战，如非正式表达、拼写变化和数据稀疏性。这项研究推进了低资源语言情感分析的前沿技术，并为孟加拉语电子商务分析应用提供了可扩展的解决方案。
## 701. `cs.LG` - 基于机制可解释性的Transformer时间序列分类 [PDF](https://arxiv.org/pdf/2511.21514), [HTML](https://arxiv.org/abs/2511.21514)
### Authors
Matīss Kalnāre,Sofoklis Kitharidis,Thomas Bäck,Niki van Stein
### Background
基于Transformer的模型已成为各种机器学习任务中的顶尖工具，包括时间序列分类，但其复杂性使得理解其内部决策过程变得困难。现有的可解释方法大多集中于输入输出归因，这让内部机制变得相当模糊。
### Innovation
本文通过将机制可解释性技术（激活补丁、注意力显著性和稀疏自编码器）适应给时间序列分类的Transformer架构，来填补这一空白。文章系统性地探究了各个注意力头和时间步对内部因果作用，揭示了这些模型内的因果结构。通过在基准时间序列数据集上的实验，本文构建了因果图，展示了信息如何在内部传播，并突出了驱动正确分类的关键注意力头和时间位置。此外，本文还展示了稀疏自编码器在发现可解释的潜在特征方面的潜力。这些发现既为Transformer的可解释性提供了方法论贡献，也为理解Transformer在时间序列分类任务中的功能机制提供了新的见解。
### Conclusion
文章提供了Transformer可解释性的方法论贡献，并对Transformer性能的潜在功能机制提供了新的见解。此外，通过稀疏自编码器展示了发现可解释的潜在特征的潜力。
## 702. `cs.LG` - 关于AI算法进步的起源 [PDF](https://arxiv.org/pdf/2511.21622), [HTML](https://arxiv.org/abs/2511.21622)
### Authors
Hans Gundlach,Alex Fogelson,Jayson Lynch,Ana Trisovic,Jonathan Rosenfeld,Anmol Sandhu,Neil Thompson
### Background
研究发现，自2012年至2023年，算法已使AI训练FLOP效率提高了22,000倍。尽管小规模实验可以解释这些效率提升的不到10倍倍数，且进一步文献调研仍只能解释不足10倍，总计不超过100倍。这些实验显示出，算法效率与计算规模相关，使用实验外推和文献估计，所模型期间总共解释了6,930倍的效率提升，特别是从LSTM到Transformer的效率改进占主导地位。先前认为小型模型的算法进步速度远快于预期。
### Innovation
实验发现，算法效率与计算规模相关。LSTM与Transformer在计算最优缩放定律上的指数差异显著。在算法效率衡量上，之前的假设认为没有特定算法与计算规模的依赖关系，而研究结果表明这种依赖是确实存在的。
### Conclusion
小型模型算法进步速度远低于以往假设，算法效率衡量具有明显的参考依赖性。大部分效率提升可以归因于具有规模依赖效率改进的算法。
## 703. `cs.LG` - 通过降维可视化大型语言模型潜在空间几何结构 [PDF](https://arxiv.org/pdf/2511.21594), [HTML](https://arxiv.org/abs/2511.21594)
### Authors
Alex Ning,Vainateya Rangaraju
### Background
大型语言模型（LLMs）在许多自然语言处理任务中表现出卓越的结果，但它们的内部机制依然难以解释。本研究通过降维技术从Transformer结构的语言模型中提取、处理并可视化潜在状态几何结构。
### Innovation
研究通过主成分分析（PCA）和均匀流形近似（UMAP）处理变压器模块中的层间激活，并在GPT-2和LLaMa模型上展示了实验，揭示了潜在空间中的有趣几何模式。研究成果包括：1）各中间层之间注意力和MLP组件输出之间的明确分离；2）初始序列位置潜在状态的高范数；3）GPT-2的位置嵌入的高维螺旋结构；4）LLaMa序列间几何模式。这些发现为进一步的可重复解释性研究提供了支持。
### Conclusion
研究旨在通过视觉解析技术促进Transformer内部机制的系统分析，为后续的可重复解释性研究打下基础。
## 704. `cs.LG` - 何时停止学习：通过强化学习实现自适应潜在推理 [PDF](https://arxiv.org/pdf/2511.21581), [HTML](https://arxiv.org/abs/2511.21581)
### Authors
Alex Ning,Yen-Ling Kuo,Gabe Gomes
### Background
潜在推理是Transformer语言模型的新发展，与链式思考推理相比，它具有潜在的推理长度压缩能力。潜在推理直接将信息丰富的前一个最终潜在状态传递到下一个序列，从而去除了必须使用人类语言令牌作为推理媒介的限制。作者进一步开发了自适应长度的潜在推理模型，并引入了一种后SFT强化学习方法，该方法通过最小化推理长度同时保持准确率来优化潜在推理长度。
### Innovation
作者提出了自适应长度潜在推理模型以及后SFT强化学习方法，通过最小化推理长度同时保持准确率来优化潜在推理长度，进一步降低计算使用量，提高潜在推理模型的压缩能力。实验结果显示，在Llama 3.2 1B模型和GSM8K-Aug数据集上，总推理长度减少了52%，且无精度损失。
### Conclusion
未来工作将扩展到其他模型和数据集，分析训练系数关系，尝试架构变化，并继续潜在推理SFT的知识蒸馏努力。代码和预训练权重将在此处提供：this https URL
## 705. `cs.LG` - 视觉转换器中的非单调缩放机制 [PDF](https://arxiv.org/pdf/2511.21635), [HTML](https://arxiv.org/abs/2511.21635)
### Authors
Anantha Padmanaban Krishna Kumar(Boston University)
### Background
深度视觉转换器经常不如浅层的版本表现，这挑战了常见的缩放假设。
### Innovation
通过系统性地分析ViT-S、ViT-B和ViT-L在ImageNet上的表现，研究发现一种一致的三阶段悬崖-平台-爬升模式，解释了深度如何影响表征演变。研究者观察到，更好的性能与[CLS]标记的渐进性边缘化有关，这一标记最初设计为全局聚合中心，相反，偏好分布式共识中的片段标记。使用信息混合指数量化信息混合规律，结果显示在ViT-L中，信息-任务权衡比ViT-B出现得晚大约10层，而这些额外的层与信息扩散增加而非任务性能改进有关。
### Conclusion
这些结果表明，在这种情况下，转换器架构可能更受益于精细校准的深度，以执行干净的相变，而不是简单地增加参数数量。信息打乱指数为现有模型提供了一个有用的诊断工具，并指出未来架构的设计目标。
## 706. `cs.LG` - 肽膜渗透性预测的解耦对齐核 [PDF](https://arxiv.org/pdf/2511.21566), [HTML](https://arxiv.org/abs/2511.21566)
### Authors
Ali Amirahmadi,Gökçe Geylan,Leonardo De Maria,Farzaneh Etminani,Mattias Ohlsson,Alessandro Tibo
### Background
循环肽是针对细胞内位点的理想靶向模式，但细胞膜渗透性仍然是一个关键性瓶颈。由于缺乏公共数据和需要精确校准的不确定性，获得准确的预测尤其困难。以往的研究常依赖于需要大量数据的支持复杂的深度学习架构。
### Innovation
本文提出了一种基于单体的解耦全局对齐核（MD-GAK），它结合了化学上有意义的残基-残基相似性和序列对齐，同时还解耦了局部匹配与缺口惩罚。此外，还提出了一个变体PMD-GAK，通过引入三角位置先验进一步提升了模型。实验表明，这种方法能够有效减少校准误差，并且在所有指标上均优于现有最先进的模型。
### Conclusion
通过广泛实验，我们的方法不仅在不确定性估计方面具有优势，还能够在各种指标上超越最先进的现有模型。我们使用了Gaussian Processes作为预测模型，展示了其有效性。我们的研究证明了MD-GAK和PMD-GAK在肽膜渗透性预测领域的潜在价值。
## 707. `cs.LG` - 使用迭代PPO使大型语言模型朝向多轮对话结果对齐 [PDF](https://arxiv.org/pdf/2511.21638), [HTML](https://arxiv.org/abs/2511.21638)
### Authors
Daniel R. Jiang,Jalaj Bhandari,Yukai Yang,Rémi Munos,Tyler Lu
### Background
优化大型语言模型（LLMs）以达成多轮对话结果，特别是在目标导向的情境下（如AI营销或销售代理通过消息平台促进交易），依然是一个重大的挑战。难题来自于稀疏的长期奖励信号以及响应级别规划与令牌级别生成之间的差距。
### Innovation
本文提出了一种正式地将多轮强化学习问题减化为一系列单一轮次RLHF问题的方法。通过将学习得到的多轮Q函数作为单轮问题的奖励模型来实现这一目的。本文还证明了一条关键洞察：用标准令牌级别的PPO解决这个单轮问题即等价于在多轮问题中执行一次策略改进步骤。基于此，提出了一个名为迭代PPO（Iterative PPO，I-PPO）的算法，这种算法交替进行Q函数拟合和策略改进，利用已有稳定的标准单轮RLHF工具来实现。这使得迭代PPO方法兼具在线更新的灵活性和离线训练的稳定性。
### Conclusion
本文的方法在全在线和全离线方法之间找到一个平衡点，保持了在线更新的灵活性同时获得了离线训练的稳定性。迭代PPO直接使用稳定的单轮RLHF工具进行实施，使其实现变得简单直接。
## 708. `cs.LG` - 具备人工智能的智能电网混合网络物理框架以实现自适应控制 [PDF](https://arxiv.org/pdf/2511.21590), [HTML](https://arxiv.org/abs/2511.21590)
### Authors
Muhammad Siddique,Sohaib Zafar
### Background
智能电网整合了传统电力基础设施和先进的通信网络及智能控制，形成了比以往更高效和灵活的网络物理环境。这种集成带来了网络稳定性及可靠性方面的脆弱性和风险。数字取证是学习、识别、检测和缓解此类安全事件的基本概念。论文提出了一种基于机器学习的智能电网系统云上通用数字取证框架。
### Innovation
该框架结合了传感器级数据获取、身份验证通信、可扩展的云存储以及自动执法分析功能。使用监督学习和无监督学习算法（如随机森林、支持向量机、梯度提升树和深层神经架构）进行实时异常检测、事件重构和入侵分析。研究证明，该框架准确性高、可扩展性强，并能抵御数据篡改、假数据注入和协调控制回路操纵等网络安全攻击。
### Conclusion
研究结果表明，基于云服务的数字取证工作流是处理大量数据的理想平台，使得能源供应商能够迅速实现情况感知并进行智能化的应急响应。
## 709. `cs.LG` - EvilGenie：一个奖励劫持基准 [PDF](https://arxiv.org/pdf/2511.21654), [HTML](https://arxiv.org/abs/2511.21654)
### Authors
Jonathan Gabor,Jayson Lynch,Jonathan Rosenfeld
### Background
介绍了LiveCodeBench的问题源，旨在创建一个评估奖励劫持的基准环境。该环境设计了可以让代理轻易劫持奖励的方式，如硬编码测试案例或编辑测试文件。
### Innovation
提出了一种新的基准测试方法，通过三种方式（留出单元测试、LLM评判和测试文件编辑检测）来衡量代理的奖励劫持行为，并将这种方法与人工审查进行了验证。此外，还测试了多种模型，并测量了三个流行的专有编程代理的行为，包括Codex、Claude Code和Gemini CLI。
### Conclusion
验证了LLM评判在明确案例中对奖励劫持的高效检测，发现只依赖于留出测试案例带来的改进有限。Codex和Claude Code展示了显式奖励劫持，三个代理均展示了与预期不符的行为。
## 710. `cs.LG` - DSD：边缘-云敏捷大型模型服务的分布式推测性解码解决方案 [PDF](https://arxiv.org/pdf/2511.21669), [HTML](https://arxiv.org/abs/2511.21669)
### Authors
Fengze Yu,Leshu Li,Brad McDanel,Saiqian Zhang
### Background
大型语言模型（LLM）推理常常受到高解码延迟和跨异构边缘-云环境的有限扩展性的困扰。现有的推测性解码（SD）技术可以加速令牌生成，但仍局限于单节点执行。
### Innovation
提出了一种名为DSD的分布式推测性解码框架，该框架通过协调草案目标执行，将SD扩展到多设备部署。此外，设计了一种自适应窗口控制（AWC）策略，动态调整推测窗口大小以优化吞吐量。
### Conclusion
实验结果表明，DSD在各种工作负载下实现了高达1.1倍的加速和9.7%更高的吞吐量，相比现有SD基线，使边缘和云环境下的LLM服务更加敏捷和可扩展。
## 711. `cs.LG` - 神经网络中的无尺度Kolmogorov-Arnold几何 [PDF](https://arxiv.org/pdf/2511.21626), [HTML](https://arxiv.org/abs/2511.21626)
### Authors
Mathew Vanherreweghe,Michael H. Freedman,Keith M. Adams
### Background
弗里德曼和穆利根的近期研究发现，在合成三维任务上训练时，浅层多层感知器（MLP）会自发形成Kolmogorov-Arnold几何（KAG）结构。但尚未明确此现象是否可以在现实中的高维背景下保持，以及该几何结构在空间上具有哪些特性。
### Innovation
本文将KAG分析应用于MNIST手写数字分类任务（784维数据），使用两层MLP，并在不同缩放级别进行系统的空间分析。研究结果表明，在训练过程中KAG结构不断地自发产生，并且在多个尺度上保持一致，从局部7像素邻域到完整的28x28像素图像。不管采用标准训练还是包含空间扩充的训练方式，此特征表现一致。
### Conclusion
研究揭示出神经网络在学习真实高维数据时自发形成具有组织性和尺度不变性的几何结构。
## 712. `cs.LG` - 国际学生知识中大语言模型的领域导向评估 [PDF](https://arxiv.org/pdf/2511.20653), [HTML](https://arxiv.org/abs/2511.20653)
### Authors
Claudinei Daitx,Haitham Amar
### Background
近年来，大语言模型（LLMs）被广泛应用于回答涉及留学的重要问题，包括录取、签证、奖学金和资格等。然而，对于这些模型的可靠性和准确性目前尚无明确的结论，尤其是在提供学生的建议时，它们是否会有不实的陈述（“幻觉”）。本文旨在提供一个清晰且基于领域的评估，通过使用来自ApplyBoard的指导工作流程中的实际问题集来评估当前LLMs的准确性与幻觉情况。
### Innovation
本文通过使用来自ApplyBoard的指导工作流程中的实际问题集来比较不同模型的准确性和幻觉情况，提出了一种简单评分法来评估答案的准确性、部分正确性和错误性，并考虑了领域覆盖和相关性。这项研究还提供了实际且可重用的协议，用于评估大语言模型在教育和咨询情境下的部署。
### Conclusion
本文旨在提供一种清晰的图景，以便明确哪些模型最适合用于国际学生的顾问建议；揭示常见的失败模式，即回答不完整、不相关或不支持的情况；并提供一个可实际操作的指南，用于在教育和顾问环境中部署大语言模型之前对这些模型进行审核。
## 713. `cs.LG` - 使用强化学习的加密货币投资组合管理：Soft Actor--Critic和Deep Deterministic Policy Gradient算法 [PDF](https://arxiv.org/pdf/2511.20678), [HTML](https://arxiv.org/abs/2511.20678)
### Authors
Kamal Paykan(Department of Mathematics, Tafresh University, Tafresh, Iran)
### Background
传统的投资组合优化方法在处理加密货币市场的高度波动性和非线性动态时常常显得力不从心。这些方法难以有效地管理这种复杂性和不确定性。
### Innovation
本研究提出了一种基于强化学习的框架，使用Soft Actor--Critic (SAC)算法和Deep Deterministic Policy Gradient (DDPG)算法来管理加密货币的投资组合。该框架下的代理可以直接从历史市场数据中通过与模拟交易环境的互动来学习连续的交易行为，并通过调整投资组合权重以最大化累计回报并最小化下行风险和交易成本来优化投资。
### Conclusion
实验结果显示，使用SAC和DDPG算法的代理策略在多种加密货币市场的表现优于基准策略，如等权重和均值-方差投资组合。其中，SAC算法由于其熵正则化的优化目标，在市场波动条件下显示出更高的稳定性和鲁棒性。这些结果强调了深度强化学习在适应性和数据驱动的加密货币投资组合管理中的潜力。
## 714. `cs.LG` - 通过电信视角：所有训练样本都重要吗？ [PDF](https://arxiv.org/pdf/2511.21668), [HTML](https://arxiv.org/abs/2511.21668)
### Authors
Shruti Bothe,Illyyne Saffar,Aurelie Boisbunon,Hasan Farooq,Julien Forgeat,Md Moin Uddin Chowdhury
### Background
人工智能在电信中的应用从优化无线接入网络扩展到管理用户体验，导致数据量和训练需求急剧增加。电信数据往往杂乱无章，维度高，存储、处理和标注成本高昂。尽管AI在其中起着关键作用，标准的工作流程仍然假设所有训练样本具有相同的重要性。然而，下一代系统要求AI模型既准确又高效。本文聚焦于电信训练中单个样本的作用及其在模型学习中的影响和冗余，提出了一个样本重要性框架，该框架可以在不牺牲准确性的前提下优先处理关键数据，减少计算需求。
### Innovation
提出了一个样本重要性框架，该框架通过样本级别梯度分析来识别模型学习中的影响模式和冗余，从而优先处理关键数据并减少计算需求，同时保持性能。这种方法在真实世界电信数据集上的实验表明，可以兼顾性能、减少数据需求和计算开销，有助于电信领域可持续AI的发展。
### Conclusion
该方法通过优先处理关键数据，在保持高性能的同时减少了数据需求和计算开销，有助于实现电信领域可持续人工智能的目标。
## 715. `cs.LG` - Escaping the Verifier: Learning to Reason via Demonstrations [PDF](https://arxiv.org/pdf/2511.21667), [HTML](https://arxiv.org/abs/2511.21667)
### Authors
Locke Cai,Ivan Provilkov
### Background
当前训练大型语言模型（LLMs）进行推理往往依赖于带任务特定验证器的强化学习（RL）。然而，在实际中，很多需要大量推理的任务缺乏这些验证器，尽管这些任务有大量的专家演示，但这些演示资源至今没有被充分用于专注推理的训练。
### Innovation
该研究引入了RARO（Relativistic Adversarial Reasoning Optimization），即通过逆向强化学习（Inverse Reinforcement Learning）仅从专家演示中学到强大推理能力。该方法设置了一种对抗性互动，即策略（生成器）和相对论批评者（判别器）之间。策略学习模仿专家答案，而批评者学习比较和区分策略和专家的答案。此外，该方法通过持续的RL训练策略和批评者，并识别出使学习稳健的关键稳定技术。实验结果显示，RARO在Countdown、DeepMath和诗歌写作等评估任务中显著优于强验证器自引导基准，并表现出与验证任务中基于RL的相同稳健扩展趋势。
### Conclusion
该研究结果证明了仅通过专家演示即可有效抽取出强大的推理性能，即使缺少特定任务的验证器也依然能够实现稳健的推理学习。
## 716. `cs.LG` - LLM-Guided Hierarchy Restructuring以大型语言模型为导向的优化双曲嵌入失真层次结构重组 [PDF](https://arxiv.org/pdf/2511.20679), [HTML](https://arxiv.org/abs/2511.20679)
### Authors
Melika Ayoughi,Pascal Mettes,Paul Groth
### Background
双曲几何是一种有效的几何方法，用于嵌入分层数据结构，因此在涉及分层数据或基于分层语义的应用中，如推荐系统和计算机视觉的机器学习中变得越来越重要。双曲嵌入的质量与输入分层结构的结构密切相关，通常源自知识图谱或本体。研究表明，对于最优的双曲嵌入，高分支因子和单一继承是关键，而嵌入算法对不平衡和分层规模的差异具有鲁棒性。为了帮助知识工程师重新组织分层知识，本文探索了大型语言模型（LLMs）是否具有自动重组层次结构以满足这些标准的能力。
### Innovation
本文提出了一种基于提示的方法，利用大型语言模型自动重构现有层次结构，以实现双曲嵌入的优化。实验结果表明，使用大型语言模型重构的层次结构在多个标准嵌入质量指标上始终能产生更高质量的双曲嵌入，同时，这种自动生成的层次结构调整过程具有可解释性，为知识工程师提供了重构的理由。
### Conclusion
通过大型语言模型自动重构层次结构的方法能够有效地优化双曲嵌入，不仅提高了嵌入质量，还为知识工程师提供了合理且可解释的调整建议。
## 717. `cs.LG` - Reasoning With a Star: 一个关于天体物理学的数据集及自主科学推理基准 [PDF](https://arxiv.org/pdf/2511.20694), [HTML](https://arxiv.org/abs/2511.20694)
### Authors
Kevin Lee,Russell Spiewak,James Walsh
### Background
在天体物理学中，科学推理不仅仅涉及记忆事实，还需要整合物理假设、保持单位一致以及通过协调的方法提供清晰的科学格式。为解决这些挑战，作者贡献了一个新的天体物理学数据集——Reasoning With a Star，并提出了初步的基准测试方法。
### Innovation
作者提出了一个新的天体物理学数据集Reasoning With a Star，其中包含来自美国宇航局和大气研究中心的夏日学校问题集，并将其整理成易于使用的问答结构，包括问题背景、推理步骤、预期答案类型、真实目标、格式提示和元数据。同时，还提供了一种程序化的评分器，用于检查预测结果，并使用单位感知数值容差、符号等价性和架构验证进行评分。
### Conclusion
通过基准测试不同单次和多代理模式，研究表明，通过系统工程原理分解工作流程在需要演绎推理而非纯粹归纳回忆的问题上优于直接提示。
## 718. `cs.LG` - 人类大脑作为组合复杂体 [PDF](https://arxiv.org/pdf/2511.20692), [HTML](https://arxiv.org/abs/2511.20692)
### Authors
Valentina Sánchez,Çiçek Güven,Koen Haak,Theodore Papamarkou,Gonzalo Nápoles,Marie Šafář Postma
### Background
当前基于图的脑网络表示方法系统地忽略了神经复杂性中的高阶依赖关系，这些依赖关系在信息处理中经常涉及协同作用的交互，这些交互不能分解为两两关系。传统的拓扑提升方法将关系结构映射到高阶领域，但这种方法间接而非直接从数据中的统计依赖性构建高阶组合复杂体。现有的脑网络图表示方式未能捕捉到高阶相互作用，导致了不准确的网络认知。
### Innovation
该研究提出了一种框架，通过信息论度量从fMRI时间序列数据构建组合复杂体（CCs），以捕捉两两和高阶神经交互。这种方法直接从数据统计依赖性中构建CCs，而不是间接映射。CCs通过引入代表大脑区域集体依赖性的高阶细胞，推广了图的概念，更好地反映了神经处理的多尺度、分层性质。该框架通过基于协同依赖关系的O-信息和S-信息措施构建数据驱动的组合复杂体，能够同时保留两两连接和高阶细胞。使用NetSim模拟数据集进行实证研究，验证了该CC构建管道的有效性。
### Conclusion
这项工作提供了一种框架，能够保持传统图方法看不到的基本高阶结构，使得可以将拓扑深度学习（TDL）架构应用于神经数据，从而更准确地表示和分析大脑网络。
## 719. `cs.LG` - 不同数据集在Amazon CoT框架下的跨域评估：多模态链式思考推理 [PDF](https://arxiv.org/pdf/2511.20701), [HTML](https://arxiv.org/abs/2511.20701)
### Authors
Nitya Tiwari,Parv Maheshwari,Vidisha Agarwal
### Background
近期工作虽然将链式思考（CoT）扩展到了多模态设置中，并在诸如ScienceQA之类的科学问答基准测试中取得了最先进的结果，但这些方法在不同领域的泛化能力尚未被充分探索。此论文对多模态链式思考（Multimodal-CoT）进行了全面分析，评估其在A-OKVQA、OKVQA和ChartQA数据集上的有效性，这些数据集要求广泛的经验常识和世界知识，而不仅仅是科学推理。
### Innovation
论文采用了Zhang et al. [3]提出的两阶段框架，将推理生成与答案推理分离，并通过门控融合机制与基于T5的语言模型集成视觉特征。通过系统性的消融研究，分析视觉特征、推理质量以及架构选择对模型性能的影响。研究发现视觉特征的整合显著降低了推理生成中的幻觉，但CoT推理的有效性在不同问题类型之间存在显著差异，特别是常识推理的具体挑战。
### Conclusion
该工作为研究人员在实施多模态推理系统时提供实用见解，并指出了跨域泛化中关键需要改进的领域。
## 720. `cs.LG` - DeeAD: 动态视觉-语言-动作早期退出以实现高效自动驾驶 [PDF](https://arxiv.org/pdf/2511.20720), [HTML](https://arxiv.org/abs/2511.20720)
### Authors
Haibo HU,Lianming Huang,Nan Guan,Chun Jason Xue
### Background
视觉-语言-动作（VLA）模型通过结合感知、推理和轨迹生成技术，服务于自动驾驶需求。然而，由于深层变压器堆栈的存在，这类模型的推理延迟明显较长。
### Innovation
DeeAD 提出了一种无需再训练的行动指导型早期退出框架，通过评估中期轨迹的物理可行性来加速 VLA 规划。引入了多跳控制器，根据评分变化率动态跳过冗余层，从而提高效率。
### Conclusion
在 Bench2Drive 基准测试中，DeeAD 实现了高达 28% 的变压器层稀疏性和 29% 的延迟减少，同时保持了规划质量和安全性。该方法无需重新训练即可整合至现有 VLA 模型中。
## 721. `cs.LG` - 一组模型验证规则 [PDF](https://arxiv.org/pdf/2511.20711), [HTML](https://arxiv.org/abs/2511.20711)
### Authors
José Camacho
### Background
模型验证是对模型在新的、未见过的数据中的表现进行评估的过程。为了确保模型在特定领域的应用可靠性，尤其是在向外界展示验证结果时，需要有一套完善且易于理解的标准和规则。
### Innovation
本文提出了关于模型验证的一系列通用规则。这些规则旨在帮助从业者制定可靠的验证计划，并透明地报告结果。这些建议有助于确保验证策略在实际应用中的有效性，并鼓励讨论验证策略的局限性。
### Conclusion
尽管没有完美的验证方案，但遵循这些建议可以帮助确保验证策略足够适用于实际用途，并能清楚地报告可对比的性能指标。
## 722. `cs.LG` - Foundry：在边缘设备上蒸馏3D基础模型 [PDF](https://arxiv.org/pdf/2511.20721), [HTML](https://arxiv.org/abs/2511.20721)
### Authors
Guillaume Letellier,Siddharth Srivastava(IIT Delhi),Frédéric Jurie,Gaurav Sharma(IIT Kanpur)
### Background
大规模数据集上利用自监督学习（SSL）预训练的基础模型已成为强大的通用特征提取器。然而，这些模型庞大的规模和计算成本使得它们无法在如机器人和AR/VR头戴设备这样边缘设备上部署。现有的压缩技术，如标准的知识蒸馏，可以创建高效的模型，但在生成一般性方面有所牺牲，这是基础模型的重要特征。
### Innovation
本文引入了一种新的压缩基础模型的方法——基础模型蒸馏（FMD），该方法能够将大规模的SSL模型压缩成紧凑、高效且忠实的代理，同时保留其通用的表示能力。文章提出了一个名为Foundry的实现框架，专门用于3D点云的压缩，使用学生模型学习一组压缩的超级标签，以重建教师模型的token级表示，从而捕捉其潜在空间的紧凑基。
### Conclusion
通过使用单一的蒸馏模型，Foundry能够在多样化下游任务（包括分类、部分分割和少样本场景）中取得接近完整基础模型的性能，且使用更少的tokens和FLOPs。这使得此类模型在资源受限硬件上的部署更加可行。
## 723. `cs.LG` - 数据驱动方法与AI在工程设计中的应用：一项聚焦挑战与机遇的系统文献综述 [PDF](https://arxiv.org/pdf/2511.20730), [HTML](https://arxiv.org/abs/2511.20730)
### Authors
Nehal Afifi,Christoph Wittig,Lukas Paehler,Andreas Lindenmann,Kai Wolter,Felix Leitenberger,Melih Dogru,Patric Grauberger,Tobias Düser,Albert Albers,Sven Matthiesen
### Background
近年来，数据的可用性增加和计算智能的进步加速了数据驱动方法（DDMs）在产品开发中的应用。然而，这些方法在产品开发中的整合仍存在碎片化现象，主要是由于不确定性，特别是在产品开发生命周期中如何选择和使用哪些DDMs方面缺乏清晰性。本研究旨在通过系统文献回顾来解决这些问题，为工程设计阶段提供指导。
### Innovation
本研究采用简化后的V模型，将产品开发框架分为系统设计、系统实施、系统集成和验证四个阶段。通过Prisma系统文献回顾方法，对Scopus、Web of Science和IEEE Xplore上2014年至2024年期间的1689篇记录进行了结构化搜索，最终选取114篇进行详细分析，发现机器学习和统计方法占主导地位，尽管深度学习应用较少但呈上升趋势。同时，指出现有应用中的主要挑战包括模型解释性不足、跨阶段追溯性差以及缺乏真实环境下的验证。强调需要开发可解释的混合模型。
### Conclusion
本研究为数据驱动方法和AI在工程设计中的应用提出了初步指导，未来应进一步将计算机科学算法映射到工程设计问题和活动中，为工程设计提供更具体和实用的指南。
## 724. `cs.LG` - Δ-NeRF: 通过残差控制和知识迁移实现神经辐射场的增量优化 [PDF](https://arxiv.org/pdf/2511.20804), [HTML](https://arxiv.org/abs/2511.20804)
### Authors
Kriti Ghosh,Devjyoti Chakraborty,Lakshmish Ramaswamy,Suchendra M. Bhandarkar,In Kee Kim,Nancy O'Hare,Deepak Mishra
### Background
神经辐射场（NeRFs）在3D重建和新颖视图合成方面展示了卓越的能力。然而，现有NeRF框架在引入新视图时需要重新训练全部数据，限制了其在数据按序到达领域的应用，特别是对基于卫星的地形分析领域，该领域中地区随时间的重复观测是一个挑战。尽管增量NeRF优化具有潜力，但现有方法在缺乏过去数据时会出现灾难性遗忘，导致性能下降。
### Innovation
提出了一种名为Δ-NeRF的独特模块化残差框架，结合了多项创新技术：1) 遗忘控制器，能够在冻结的基础NeRF中注入逐层修正，无需访问过去数据即可进行增量优化；2) 不确定性感知门控机制，通过动态结合基础和优化预测来防止过度修正；3) 视图选择策略，能减少47%的训练数据同时保持性能。此外，还采用了知识蒸馏将增强模型压缩为紧凑的学生网络（原模型的20%大小）。实验表明Δ-NeRF在卫星图像中性能可与联合训练媲美，并将训练时间缩短了30-42%，同时相对于现有基线提高了43.5%的PSNR，并在某些指标上超越了联合训练。
### Conclusion
Δ-NeRF 在卫星图像中在保持性能的同时，通过减少训练数据和压缩模型显著提高了算法效率。该方法在不同情况下表现出更优的性能，为NeRF在实际应用中的增量优化提供了新的可能。
## 725. `cs.LG` - PropensityBench: 通过代理方法评估大型语言模型潜藏的安全风险 [PDF](https://arxiv.org/pdf/2511.20703), [HTML](https://arxiv.org/abs/2511.20703)
### Authors
Udari Madhushani Sehwag,Shayan Shabihi,Alex McAvoy,Vikash Sehwag,Yuancheng Xu,Dalton Towers,Furong Huang
### Background
近年来，大语言模型（LLMs）的进步引发对其潜在危险或高风险能力的关注，这些能力可能导致模型被滥用，提出了前沿风险。目前的安全评估主要关注模型能够做什么的能力，而不考虑如果赋予高风险能力它们会怎么做。这留下了一个关键的盲点：模型可能战略性地隐瞒其能力或迅速获取这些能力，同时潜藏着滥用倾向。研究提出，**倾向性**——模型在获得授权后追求有害行为的倾向——是安全评估中一个关键但尚未被充分探索的方面。
### Innovation
该研究提出了一种新颖的基准框架PropensityBench，通过使用代理工具评估当大型语言模型装备上模拟危险能力时，它们参与 risky 行为的倾向。该框架包括 5,874 种场景和 6,648 种工具，涵盖了网络安全、自我传播、生物安全和化学安全四个高风险领域。研究模拟了获取强能力的控制环境，并评估了模型在资源稀缺或获得更多自主权等不同操作压力下的选择。研究发现，开放源代码和专有前沿模型显示出 9 个令人担忧的倾向性迹象，即模型在压力下频繁选择高风险工具，尽管无法独立执行这些行为。这一发现呼吁从静态能力审计转向动态倾向性评估，作为部署前沿人工智能系统的前提。
### Conclusion
研究发现了 9 个令人担忧的倾向性迹象，即模型在压力下频繁选择高风险工具，建议从静态能力审计转向动态倾向性评估，以确保安全部署前沿AI系统。研究代码可在以下链接下载。
## 726. `cs.LG` - 高对比度多孔介质储层模拟中加速局部基函数计算的双域深度学习方法 [PDF](https://arxiv.org/pdf/2511.20685), [HTML](https://arxiv.org/abs/2511.20685)
### Authors
Peiqi Li,Jie Chen
### Background
在能源科学中，不均匀多孔介质中的达西流是储层模拟中的核心问题。然而，此类介质的明显多尺度特性对传统数值方法提出了计算需求和效率的挑战。混合广义多尺度有限元方法（MGMsFEM）能够有效应对这些挑战，但对于构建多尺度基函数来说仍然是计算上昂贵的。
### Innovation
本文提出了一种双域深度学习框架，用于在MGMsFEM中加速计算多尺度基函数，通过在频率域和空间域中提取和解码渗透率场特征，快速生成多尺度基函数的数值矩阵。研究表明，该方法在保持高逼近精度的同时实现了显著的计算加速，具有在未来实际储层工程中的潜在应用价值。
### Conclusion
本工作通过提出的双域深度学习框架，在MGMsFEM中有效加速了多尺度基函数的计算，提升了计算效率，为解决高对比度多孔介质中的达西流问题提供了新的途径。
## 727. `cs.LG` - 谐波令牌投影 (HTP)：一种无词汇表、无需训练、确定性且可逆的嵌入方法 [PDF](https://arxiv.org/pdf/2511.20665), [HTML](https://arxiv.org/abs/2511.20665)
### Authors
Tcharlies Schmitz
### Background
该论文介绍了和谐令牌投影（Harmonic Token Projection，HTP）框架，这是一种生成文本嵌入的确定性机制，不依赖于训练、词汇表或随机参数。与其他依赖统计共现或优化的神经网络嵌入技术不同，HTP 通过分析其 Unicode 整数表示生成每个令牌的谐波轨迹，从而建立了离散符号和连续向量空间之间的双射且可解释的映射。
### Innovation
HTP 通过谐波表达式提供相位相干的投影，既保留结构又保持可逆性，允许仅通过几何对齐即可评估语义相似性。实验表明，HTP 在 STS-B 及其多语言扩展上的 Spearman 相关系数高达 0.68，且稳定性能跨十种语言保持不变，几乎无计算成本且每个句子对的延迟小于毫秒级。这表明有意义的语义关系可以从确定性几何学中自然衍生出来，从而提供了一种透明且高效的替代数据驱动嵌入的方法。
### Conclusion
HTP 演示了如何从确定性几何学中自然产生有意义的语义关系，并提供了一种透明且高效的替代数据驱动嵌入的方法。
## 728. `cs.LG` - AssurAI：构建韩民族社会文化数据集以发现生成式AI潜在风险的经验 [PDF](https://arxiv.org/pdf/2511.20686), [HTML](https://arxiv.org/abs/2511.20686)
### Authors
Chae-Gyun Lim,Seung-Ho Han,EunYoung Byun,Jeongyun Han,Soohyun Cho,Eojin Joo,Heehyeon Kim,Sieun Kim,Juhoon Lee,Hyunsoo Lee,Dongkun Lee,Jonghwan Hyeon,Yechan Hwang,Young-Jun Lee,Kyeongryul Lee,Minhyeong An,Hyunjun Ahn,Jeongwoo Son,Junho Park,Donggyu Yoon,Taehyung Kim,Jeemin Kim,Dasom Choi,Kwangyoung Lee,Hyunseung Lim,Yeohyun Jung,Jongok Hong,Sooyohn Nam,Joonyoung Park,Sungmin Na,Yubin Choi,Jeanne Choi,Yoojin Hong,Sueun Jang,Youngseok Seo,Somin Park,Seoungung Jo,Wonhye Chae,Yeeun Jo,Eunyoung Kim,Joyce Jiyoung Whang,HwaJung Hong,Joseph Seering,Uichin Lee,Juho Kim,Sunna Choi,Seokyeon Ko,Taeho Kim,Kyunghoon Kim,Myungsik Ha,So Jung Lee,Jemin Hwang,JoonHo Kwak,Ho-Jin Choi
### Background
生成式AI的快速发展需要对其进行稳健的安全评估。然而，当前的安全评估数据集主要以英语为中心，未能捕捉到如韩语等非英语社会文化背景下的特定风险，并且这些数据集往往仅限于文本模态。
### Innovation
本文提出了AssurAI，这是一个用于评估生成式AI安全性的新型高质量控制的韩语文本、图片、视频和音频多模态数据集。首先定义了35种不同的人工智能风险因素，并通过多学科专家团队进行改编，以涵盖通用危害和韩国社会文化环境的相关性。然后利用这些分类构建和发布了AssurAI数据集，并采用了严格的质量控制过程，包括两阶段构建（专家领导下的种子阶段和群体外包的扩展阶段）、三重独立注释以及迭代专家红队测试。研究初步表明AssurAI可有效评估最新的大型语言模型的安全性。
### Conclusion
本研究发布了AssurAI数据集，以促进韩国社区更安全可靠的生成式AI系统的开发。
## 729. `cs.LG` - 从多条路径检索的记忆：大规模语言模型中稳健检测训练数据泄露的多前缀框架 [PDF](https://arxiv.org/pdf/2511.20799), [HTML](https://arxiv.org/abs/2511.20799)
### Authors
Trung Cuong Dang,David Mohaisen
### Background
大规模语言模型由于在海量语料上训练，容易原封不动地记忆训练数据，这带来了严重的隐私和版权风险。尽管之前的工作提出了各种对记忆的定义，但这些定义在全面捕捉这一现象时出现了局限性，特别是在对齐模型中。
### Innovation
我们提出了一个创新的多前缀记忆框架，核心思想是记忆中的序列通过深层编码，因此可以通过远远多于非记忆内容的唯一前缀来检索。我们通过外部对抗搜索定义了一条序列被记忆的标准，并将焦点从单一路径提取转移到量度记忆的鲁棒性，即检索路径的多样性。
### Conclusion
我们在开源和对齐聊天模型上进行的实验表明，我们的多前缀定义可靠地区分了记忆和非记忆数据，提供了一种稳健且实用的工具，用于审计LLM中的数据泄露。
## 730. `cs.LG` - 基于优化反演的无训练扩散先验文本图像生成 [PDF](https://arxiv.org/pdf/2511.20821), [HTML](https://arxiv.org/abs/2511.20821)
### Authors
Samuele Dell'Erba,Andrew D. Bagdanov
### Background
扩散模型在文本到图像生成任务上已取得了最先进的成果，但其性能通常依赖于一个扩散先验网络将文本嵌入转化为可视流 manifolds 以便于解码。然而，这些先验网络计算成本高，需要大量数据集进行训练。
### Innovation
本文提出了优化基于视觉反转（OVI）作为替代训练和数据依赖先验的方法。OVI 初始从随机伪代币生成潜在的视觉表示，并对其进行迭代优化以最大化与输入文本提示嵌入的余弦相似度。此外，作者提出了两种新的约束方法——马哈拉诺比斯距离损失和最近邻损失，以规范 OVI 的优化过程，使其趋向于现实图像的分布。实验表明，OVI 能够替代传统的先验方法，并且受限的 OVI 方法提高了图像保真度，尤其是最近邻方法的效果尤为显著。
### Conclusion
我们的研究揭示了当前评价基准中的一个关键缺陷，即仅使用文本嵌入作为先验也能达到出乎意料的高分数，尽管视觉质量较低。受限的 OVI 方法可以提高视觉保真度，其最近邻方法甚至能达到或超过最先进的数据高效先验的定量评分，表明该想法值得进一步研究。代码将在文章被接受后公开。
## 731. `cs.LG` - 基于体素的点云网络中加速稀疏卷积 [PDF](https://arxiv.org/pdf/2511.20834), [HTML](https://arxiv.org/abs/2511.20834)
### Authors
Dionysios Adamopoulos,Anastasia Poulopoulou,Georgios Goumas,Christina Giannoula
### Background
稀疏卷积（SpC）在自动驾驶和AR/VR等领域广泛应用于3D点云网络。传统的SpC引擎并未充分挖掘体素坐标的三个关键属性：整数值、局限于特定空间范围以及几何连续性，这导致了预处理和后处理的高开销。
### Innovation
提出了一种名为Spira的新型SpC引擎，该引擎具有以下创新点：(i) 一种高性能的一次性搜索算法，能够在无预处理和高内存局部性的条件下构建卷积核；(ii) 一种高效的打包原生处理方案，以低成本访问打包的体素坐标；(iii) 一种灵活的双数据流执行机制，以适应不同层的特征有效计算输出特征向量；(iv) 一种网络级的并行策略，在网络启动时并发构建所有SpC层的卷积核。
### Conclusion
Spira在端到端推理中平均比之前的SpC引擎快1.71倍，最高可达2.31倍；在分层执行中，无论是多样化还是单一配置，平均速度快2.13倍，最高可达3.32倍。
## 732. `cs.LG` - NOIR 2.0: 基于神经信号操作的智能机器人用于日常活动 [PDF](https://arxiv.org/pdf/2511.20848), [HTML](https://arxiv.org/abs/2511.20848)
### Authors
Tasha Kim,Yingke Wang,Hanvit Cho,Alex Hodges
### Background
NOIR 系统是一种可穿戴的脑机接口，允许人类使用大脑信号控制机器人进行日常生活任务。该系统通过脑电图（EEG）将人类对特定物体和期望操作的意图直接转化为机器人可以执行的命令。
### Innovation
NOIR 2.0 包括更快更准确的脑解码算法，将任务完成时间降低了46%。NOIR 2.0 使用少量示例的机器人学习算法来适应个别用户并预测其意图。新学习算法利用基础模型实现更高效的学习和适应（15个示范案例与传统一个示范案例相比），整体大大减少了人类的时间消耗达65%。
### Conclusion
NOIR 2.0 在保持高精度解码和高度适应性的同时实现了更高的效率，为脑机接口技术在日常生活中的应用提供了强有力的支持。
## 733. `cs.LG` - 数据融合在多模式学习分析和教育数据挖掘中的综述 [PDF](https://arxiv.org/pdf/2511.20871), [HTML](https://arxiv.org/abs/2511.20871)
### Authors
Wilson Chango,Juan A. Lara,Rebeca Cerezo,Cristóbal Romero
### Background
新的教育模式如智能学习环境利用数字和上下文感知设备来促进学习过程。在这个新的教育场景中，可以从多种来源捕获大量的多模态学生数据。这对于研究人员和教育工作者来说是一个独特的机会，可以帮助他们发现新的知识，通过数据融合的方法来汇总和分析这些数据，以更好地理解学习过程，并在有必要时进行干预。
### Innovation
该文综述了数据融合在学习分析（LA）和教育数据挖掘（EDM）中的应用，并详细介绍了应用于智能学习中的数据融合技术。通过回顾主要的出版物和研究成果，揭示了集成教育数据的主要类型、数据融合方法和技术，并指出了该领域的主要开放问题、趋势和挑战。
### Conclusion
本文展示了目前该领域的前沿状态，强调了数据融合在学习分析和教育数据挖掘中的重要性，并指出了这个特定研究领域的主要挑战和未来的研究方向。
## 734. `cs.LG` - RefTr: Recurrent Refinement of Confluent Trajectories for 3D Vascular Tree Centerline Graphs [PDF](https://arxiv.org/pdf/2511.20823), [HTML](https://arxiv.org/abs/2511.20823)
### Authors
Roman Naeem,David Hagerman,Jennifer Alvén,Fredrik Kahl
### Background
输送管状树状结构，如血管和肺气管，对人体内的物质转运至关重要。准确检测它们的中心线并保持正确的树状拓扑结构对于临床任务（如诊断、治疗规划和外科导航）至关重要。特别是在这些应用中，保持高召回率至关重要，因为遗漏的小分支可能导致因评估不完整或未检测到的异常而导致的致命错误。
### Innovation
提出了RefTr，一种基于变压器解码器的递归精炼机制的3D图像到图形模型，用于通过递归精炼汇聚轨迹生成血管树的中心线。RefTr 使用 producers-Refiner 架构，其中 producers 提出一组初始汇聚路径，这些路径由 Refiner 递归改进以生成最终路径，从而形成中心线图。汇聚路径表示法使可以完整精炼路径并显式强制实施有效的树状拓扑结构。递归精炼方案提高了准确度，并且允许在多个步骤中重复使用相同的 Refiner 块，使得与最新SOTA相比，解码器参数减少了2.4倍。此外，还提出了一种高效的非最大抑制算法用于空间树状图以合并重复分支并提升准确度。
### Conclusion
RefTr 在多个公开的中心线数据集中实现了优于现有 SOTA 的召回率和可比的准确度，同时提供了更快的推理速度和显著减少的参数数量，这表明其有可能成为3D医疗成像中血管树分析的新SOTA框架。
## 735. `cs.LG` - MODEST: 多光学深度景深立体数据集 [PDF](https://arxiv.org/pdf/2511.20853), [HTML](https://arxiv.org/abs/2511.20853)
### Authors
Nisarg K. Trivedi,Vinayak A. Belludi,Li-Yun Wang,Pardis Taghavi,Dante Lok
### Background
在自主机器人和增强现实等系统中，基于相机的视觉深度估计依然具有重要挑战性，尤其是在现实光学条件下的可靠深度估计。尽管深度估计和景深渲染技术已取得了进展，但由于缺乏大规模、高保真、现实的双目单反DSLR数据集，研究仍受到限制，模型在合成数据上的训练难以推广和评估，文献中已有充分的验证。这导致模型难以应对实际应用场景中的情况。
### Innovation
本文首次发布了具有5472×3648像素的高分辨率双目DSLR数据集，包含了18000张图像。数据集通过系统地调整焦距和光圈的变化，在复杂的真实场景中捕捉真实相机系统的光学真实性和复杂性。通过涵盖9个场景各个环节的10个焦距（28-70mm）和5种光圈（f/2.8-f/22）配置，共计50种光学设置，总共实现了2000张图像的捕捉，从而实现了光学全范围的覆盖。此数据集旨在填补合成训练数据与实际相机光学之间的真实度差距，支持几何和光学效应的可控分析，并证明了当前最先进的单目、双目深度和景深方法所面临的挑战。
### Conclusion
本文通过发布数据集、校准文件和评估代码，旨在支持现实世界光学特性的可重现性研究，同时展示了深度估计、景深渲染、去模糊、3D场景重建和新颖视角合成方法的挑战。
## 736. `cs.LG` - 结构化提示使语言模型评估更健壮、全面 [PDF](https://arxiv.org/pdf/2511.20836), [HTML](https://arxiv.org/abs/2511.20836)
### Authors
Asad Aali,Muhammad Ahmed Mohsin,Vasiliki Bikia,Arnav Singhvi,Richard Gaus,Suhana Bedi,Hejie Cui,Miguel Fuentes,Alyssa Unell,Yifan Mai,Jordan Cahoon,Michael Pfeffer,Roxana Daneshjou,Sanmi Koyejo,Emily Alsentzer,Percy Liang,Christopher Potts,Nigam H. Shah,Akshay S. Chaudhari
### Background
语言模型（LMs）在各领域的应用越来越广泛，高质量的基准测试框架对于引导部署决策至关重要。现有的综合评估框架（如Holistic Evaluation of Language Models, HELM）虽然可以在多个任务上进行广泛评估，但往往依赖于固定提示，无法很好地推广到不同的模型上，导致性能评估不够真实。除非我们估计每个模型的天花板（通过提示变化所能达到的最大性能），否则我们可能会低估其性能。Declarative Prompting框架，如DSPy，通过结构化的提示来替代手动提示工程，但这些框架尚未被系统地在现有基准上进行评估。
### Innovation
本文提出一个可复现的DSPy+HELM框架，引入结构化提示方法以促进更准确的语言模型基准测试。使用四种提示方法在七个（通用/医疗领域）基准上评估了四种前沿模型，并且发现：（i）不使用结构化提示时，HELM低估了LM性能（平均低估4%）；（ii）性能评估在基准之间变化更大（标准差增加2%）；（iii）性能差距被误表征（在3/7个基准上排行榜互换）；（iv）引入逻辑推理（链式思考）减少了LM对提示设计的敏感性（提示间差距变小）。这是首个系统地表征语言模型行为和提示方法的大规模基准测试研究，表明可扩展的性能天花板估计能产生更有决策价值的基准。
### Conclusion
研究显示，基于结构化提示的语言模型评估框架使基准测试更稳健、全面。通过开源DSPy+HELM集成和提示优化管道，以促进未来研究的应用和发展。
## 737. `cs.LG` - 通过 Null-Text 嵌入优化实现文本到图像扩散模型的测试时对齐 [PDF](https://arxiv.org/pdf/2511.20889), [HTML](https://arxiv.org/abs/2511.20889)
### Authors
Taehoon Kim,Henry Gouk,Timothy Hospedales
### Background
现有的Test-time alignment (TTA)方法要么对目标奖励函数优化不足，要么优化过度（产生奖励欺骗），导致模型适应特定奖励的能力受限。
### Innovation
提出了一种名为Null-Text Test-Time Alignment (Null-TTA)的方法，通过优化无条件嵌入（在分类器无关引导中）而不是操纵潜在变量或噪声，在语义一致的空间中对扩散模型进行对齐，从而避免奖励欺骗。
### Conclusion
Null-TTA实现了最佳的测试时对齐性能，同时保持了跨奖励的强泛化能力，建立了语义空间优化作为TTA的有效和原则性的新范式。
## 738. `cs.LG` - 具有开放词汇量的神经元对齐的组成解释 [PDF](https://arxiv.org/pdf/2511.20931), [HTML](https://arxiv.org/abs/2511.20931)
### Authors
Biagio La Rosa,Leilani H. Gilpin
### Background
神经元是深度神经网络的基本构建块，它们之间的连接使人工智能能够实现前所未有的成果。为了理解神经元如何编码信息， compositional explanations 通过概念之间的逻辑关系来表达神经元激活与人类知识的空间对齐。然而，这些解释依赖于人类标注的数据集，限制了它们在特定领域和预定义概念上的应用。
### Innovation
本文提出了一种用于视觉领域的新框架，允许用户探索任意概念和数据集中的神经元。该框架通过使用开放词汇量语义分割生成的掩码来计算开放词汇量组成的解释。该框架分为三步：指定任意概念、使用开放词汇量模型生成语义分割掩码、并从这些掩码中推导出组成解释。与之前的方法相比，本文的框架在定量指标和人类可解释性方面进行了比较，并分析了从人类标注数据到模型标注数据的变化。
### Conclusion
本文展示了新框架的灵活性，可以针对感兴趣的任务和属性提供额外的功能。尤其在解释的灵活性上，新框架提供的能力超越了传统的依赖于人类标注数据的方法。
## 739. `cs.LG` - SPHINX：一种用于视觉感知与推理的合成环境 [PDF](https://arxiv.org/pdf/2511.20814), [HTML](https://arxiv.org/abs/2511.20814)
### Authors
Md Tanvirul Alam,Saksham Aggarwal,Justin Yang Chae,Nidhi Rastogi
### Background
现有的视觉感知和推理环境通常考虑的是现实世界的复杂性和多样性，这使得这些环境难以进行大规模、精细的基准测试和数据集构建。此外，尽管最新的大型视觉语言模型（LVLMs）在视觉感知任务上取得了显著进展，但仍难以应对某些视觉推理任务，尤其是那些需要深刻理解图像之间复杂关系的任务。
### Innovation
SPHINX 是一种合成环境，专门旨在针对核心认知基础技能进行视觉感知和推理。它使用模式、瓷砖、图表、图标和几何原语来程序化生成谜题，并为每个谜题提供可验证的真实解决方案，从而使得评估和大规模数据集构建变得精确和高效。该基准测试覆盖了 25 种任务类型，包括对称性检测、几何变换、空间推理、图表解析以及序列预测。此外，SPHINX 还通过可验证奖励的强化学习（RLVR）来提高模型在这些任务上的准确性。
### Conclusion
即使是最先进的 GPT-5 模型在这些任务上的准确率也只有 51.1%，远远低于人类的表现。SPHINX 提示我们，包含可验证奖励的强化学习对于提高大规模视觉推理任务的准确性具有潜在的优势，并可能促进多模态推理的进步。此外，SPHINX 的 RLVR 算法在外部分视觉推理基准测试上同样表现出了优越性，展示了其有价值的应用前景。
## 740. `cs.LG` - 融合经典和量子核函数实现准确且稳健的两样本检验 [PDF](https://arxiv.org/pdf/2511.20941), [HTML](https://arxiv.org/abs/2511.20941)
### Authors
Yu Terada,Yugo Ogio,Ken Arai,Hiroyuki Tezuka,Yu Tanaka
### Background
两样本检验已被广泛应用于药物效果评估、不同营销策略的A/B测试等科学研究和机器学习领域，用于判断两组样本是否来自相同的分布。基于核的方法已被提出用以高效地区分高维度复杂数据结构，通过将其嵌入到再生核希尔伯特空间中获得无模型的概率假设检验方法。尽管选择核对于这些方法的效果至关重要，但特别是在小样本数据集的情况下，选择合适的核的方法仍不明确。
### Innovation
该研究提出了MMD-FUSE框架，并在此基础上整合量子核函数，提出一种新颖的混合测试策略。这种方法通过结合经典核函数的领域特定归纳偏见和量子核函数的独特表达能力，创建了一个强大且适应性强的测试。实验结果表明，对于小样本和高维数据，MMD-FUSE结合量子核函数的测试效果优于经典方法，且提出的混合框架在不同数据特征下表现出显著的稳健性，实现了广泛的测试性能。
### Conclusion
这些结果强调了量子启发和混合核策略在构建更有效的统计检验中的潜在价值，尤其是当样本数量有限时，这是一种灵活的数据分析工具。
## 741. `cs.LG` - 确保最佳组成解释：神经元的保证最优组成解释 [PDF](https://arxiv.org/pdf/2511.20934), [HTML](https://arxiv.org/abs/2511.20934)
### Authors
Biagio La Rosa,Leilani H. Gilpin
### Background
尽管神经元是深度神经网络的基本单元，但它们学习的内容以及它们的知识是否与人类的知识相一致仍不清楚。组成性解释试图通过逻辑规则描述神经元激活和概念之间的空间对齐来回答这个问题。这些逻辑描述通常是通过搜索所有可能的概念组合来计算的。由于在完整状态空间范围内计算空间对齐是计算上不可行的，文献中通常采用束搜索来限制搜索空间。然而，束搜索无法提供任何关于最优性的理论保证，而且不清楚当前的解释有多么接近真正的最优值。
### Innovation
本文提出了第一个计算保证最优组成解释的框架。具体来说，作者提出了：(i) 一种分解，识别影响空间对齐的因素；(ii) 一个估计搜索过程中任意阶段对齐程度的启发式方法；(iii) 第一个能够在可行时间内计算最优组成解释的算法。利用该框架，文本分析了最优和非最优解释在当前编排解释中最常使用的场景中的差异，即计算机视觉领域和卷积神经网络。结果显示，当存在重叠概念时，使用束搜索获得的40%以上的解释可能是次优的。最后，通过一种引导束搜索运行的分解和启发式方法的变种进行评估，该方法在运行时间和先前方法相比具有竞争力或改进，并且提供了更大的超参数灵活性和计算资源。
### Conclusion
通过引入新的分解方法、启发式估计与首个能在可行时间内计算最优解释的算法，扩大了对神经元和认知网络解释的理解，解决了束搜索缺乏最优性保证的问题。
## 742. `cs.LG` - 基于几何校准和不确定性中立区的多类分类方法 [PDF](https://arxiv.org/pdf/2511.20960), [HTML](https://arxiv.org/abs/2511.20960)
### Authors
Soumojit Das,Nairanjana Dasgupta,Prashanta Dutta
### Background
现代人工智能系统在做关键决策时经常在不确定的情况下无预警地失败。因此，本文基于几何框架提出了神经网络概率输出的后验校准方法，通过将概率向量视为配备费舍尔-拉奥度量的$(c-1)$维概率单纯形上的点。这种方法在分类问题中引入Additive Log-Ratio (ALR)校准映射，并且能够自然扩展到多类设置。此外，定义了基于费舍尔-拉奥距离的几何可靠性评分，并构建了中立区以实现对不确定预测的有原则的推迟。
### Innovation
本文提出了一种基于几何框架的后验校准方法，该方法在二分类问题中退化为Platt校准，在多分类问题中自然扩展，提供了一种有理论基础的泛化方法，弥补了现有方法的不足。同时引入了基于费舍尔-拉奥距离的几何可靠性评分和用于不确定预测的中立区的概念。此外，证明了一致性（定理1）和可靠性评分的紧凑聚集边界（定理2），提出了中立区构建的奈曼-皮尔逊最优性的猜想。
### Conclusion
以腺相关病毒分类为例，这种两阶段框架（校准后基于可靠性推迟）能够捕获72.5%的错误，同时推迟34.5%的样本。几何校准的主要贡献在于其理论基础而非相较于简单替代方法的统计表现上的优势。本文工作旨在信息几何学与统计学习之间的交叉领域，旨在提供对需要严格验证的应用具有实际意义的形式保证。
## 743. `cs.LG` - 绕过读出瓶颈的残差量子-经典混合模型 [PDF](https://arxiv.org/pdf/2511.20922), [HTML](https://arxiv.org/abs/2511.20922)
### Authors
Guilin Zhang,Wulan Guo,Ziqi Tan,Hongyang He,Hailong Jiang
### Background
量子机器学习（QML）虽然能够提供紧凑且表达性强的表示，但受到测量瓶颈的限制——狭窄的量子到经典读出限制了其性能并加剧了隐私风险。
### Innovation
提出了一种轻量级残差混合架构，在分类前将量子特征与原始输入连接起来，绕过了瓶颈而不增加量子复杂度。实验表明，该模型在中央和联邦设置中均优于纯量子和之前的混合模型，相较于量子基准实现高达55%的准确率改进，同时保持了较低的通信成本和增强的隐私鲁棒性。消融研究证实了量子-经典接口处残差连接的有效性。
### Conclusion
该方法提供了一条将量子模型集成到资源有限且隐私敏感环境（如联邦边缘学习）中的实用且接近实际的道路。
## 744. `cs.LG` - Length-MAX Tokenizer for Language Models [PDF](https://arxiv.org/pdf/2511.20849), [HTML](https://arxiv.org/abs/2511.20849)
### Authors
Dong Dong,Weijie Su
### Background
现有的语言模型使用字节对编码(BPE)进行分词，这在训练和推理过程中需要大量的token。作者研究了如何减少文案单位的数量，同时保持或提高下游任务的性能。
### Innovation
提出了Length-MAX分词器，这是一种新的分词方法，优化了每个字符的平均token数，相比BPE分词在各种数据集上平均能减少14-18%的token。通过将长度加权的目标最大化作为图划分问题，并开发贪婪近似算法来获得词汇表。此外，在使用GPT-2模型时，与BPE相比，能够在不牺牲性能的基础上减少训练步骤、降低推理延迟并提高吞吐量。
### Conclusion
优化平均token长度而非频率可以提高语言建模的效率，且不会牺牲下游任务的性能，甚至可以改善某些任务。Length-MAX分词器已经在生产系统中进行了测试，显示出较低的OOV率和内存占用率的减少，从而进一步证明了其有效性。
## 745. `cs.LG` - 基于独立策略梯度的强化学习方法用于多微网系统的经济可靠能源管理 [PDF](https://arxiv.org/pdf/2511.20977), [HTML](https://arxiv.org/abs/2511.20977)
### Authors
Junkai Hu,Li Xia
### Background
多微网系统（MMSs）中，能源管理的效率和可靠性都极为重要，特别是随着间歇性和分布式可再生能源源的集成。现有研究多采用集中式方法来优化能源管理政策，但本文聚焦于分散式方案下的经济和可靠能源管理问题。每个微网独立更新其能源管理策略以优化长期系统的性能。
### Innovation
引入了一种新的评估指标（即交换功率的均值和方差）来衡量系统的经济性和可靠性，并将能量管理问题表述为均值-方差团队随机博弈（MV-TSG）。提出了两种方法来解决MV-TSG：一种是用于已知模型参数的小规模场景的全分散独立策略梯度算法；另一种是基于独立策略梯度的深度强化学习方法，适用于未知模型参数的大型场景。两种方法都确保了数据驱动的性能优化。
### Conclusion
通过数值实验验证了所提出方法的有效性，并展示了如何利用MMSs的分布式计算能力以达到经济性能和操作可靠性的良好平衡。
## 746. `cs.LG` - 基于噪声假设检验的特征选择技术：特征超越噪声 [PDF](https://arxiv.org/pdf/2511.20851), [HTML](https://arxiv.org/abs/2511.20851)
### Authors
Mousam Sinha,Tirtha Sarathi Ghosh,Ridam Pal
### Background
在机器学习和人工智能中，特征选择依然是一项艰巨的挑战，特别是面对日益复杂、高维度的数据集时，需要制定合理的策略来识别最具信息量的预测变量。众多已有的技术存在明显局限性，比如计算成本高昂或缺乏明确的统计停止标准，或者无法评估重要性分数的显著性。一种常见的直观但缺乏理论支撑的方法是在引入多个随机噪声特征后，保留所有排名高于最强噪声特征的预测变量。
### Innovation
本文提出一种新颖的特征选择方法，以解决这些局限性。该方法引入多个随机噪声特征，并将每个特征的重要性与这些噪声特征中的最大重要性值进行比较，采用基于非参数Bootstrap的假设检验框架，为方法提供了坚实的理论基础。通过统计推导阐述了算法设计原理，并在控制统计设置下生成模拟数据集进行可靠性测试，与Boruta和Knockoff方法相比，表现出更强的信号恢复能力。
### Conclusion
该方法作为一种稳健的特征选择算法，能够有效地提炼出支持可靠推断、提升预测性能并实现高效计算的有用预测变量。
## 747. `cs.LG` - 深度学习作为计算凸范式的深度学习：用ResNets最小化电路大小 [PDF](https://arxiv.org/pdf/2511.20888), [HTML](https://arxiv.org/abs/2511.20888)
### Authors
Arthur Jacot
### Background
本文讨论了DNNs在 Occam's Razor 的机制下找到与数据拟合的最简单算法的能力，并解释了DNNs超越传统统计方法的原因。文章基于在?Harder than Monte Carlo? (HTMC) 域，当 γ>2 时，如果函数 f 能以 ε 精度 τ 级别近似于具有 δ 大小的二进制电路，则该函数集合会变得凸，从而定义了一种 HTMC 范数。同时，对于 ResNets 可定义一种参数复杂度测度（加权的 ℓ_1 范数），这诱导出一种 ResNet 范数。
### Innovation
文章提出了一种基于凸性的范式来解释DNNs的优越性，即通过定义 HTMC 范数和 ResNet 范数，将 ResNet 的最小化与电路大小的最小化联系起来。因此，最小化 ResNet 范数等效于找到一个几乎最优的电路大小来拟合数据。
### Conclusion
ResNets 可以作为一种更适合 HTMC 域和其凸性的计算模型，用以最小化函数电路的大小。
## 748. `cs.LG` - BUSTR: 使用描述感知的视觉-语言模型的乳腺超声文本报告 [PDF](https://arxiv.org/pdf/2511.20956), [HTML](https://arxiv.org/abs/2511.20956)
### Authors
Rawa Mohammed,Mina Attin,Bryar Shareef
### Background
自动化放射学报告生成（RRG）在乳腺超声（BUS）领域受到缺乏成像-报告配对数据集和大型语言模型风险的影响。现有技术需要成像-报告配对数据集的监督，且容易产生幻觉。
### Innovation
本文提出了一种多任务视觉-语言框架BUSTR，该框架在无需成像-报告配对数据集的情况下生成BUS报告。BUSTR通过结构化描述（如BI-RADS、病理学、组织学）和-radiomics特征构建报告，使用基于多任务损失的多头Swin编码器学习描述感知的视觉表示，并通过双重目标对齐视觉和文本令牌，该目标结合了标记级别交叉熵和输入输出表示之间的余弦相似性对齐损失。
### Conclusion
实验结果表明，该描述感知视觉模型在合并标记级别和对齐损失的训练下，提高了自动报告指标和临床疗效指标，尤其是在BI-RADS类别和病理学等关键目标上。该模型可以在不使用成像-报告配对数据的情况下实现这一改进。
## 749. `cs.LG` - 波前约束被动遮挡目标检测 [PDF](https://arxiv.org/pdf/2511.20991), [HTML](https://arxiv.org/abs/2511.20991)
### Authors
Zhiwen Zheng,Yiwei Ouyang,Zhao Huang,Tao Zhang,Xiaoshuai Zhang,Huiyu Zhou,Wenwen Tang,Shaowei Jiang,Jin Liu,Xingru Huang
### Background
准确地从微弱光斑中定位和分割超出视场范围的被遮挡物体极具挑战性，这主要是因为多次散射和介质引发的干扰。现有的大多数方法基于实值建模或局部卷积操作，难以捕捉相干光传播的基本物理规律。在低信噪比条件下，这些方法常常收敛到非物理的解，严重影响了观测的稳定性和可靠性。
### Innovation
本文提出了一个新颖的物理驱动波前传播补偿网络(WavePCNet)，以模拟波前传播并增强对被遮挡物体的感知能力。WavePCNet融合了Tri-Phase波前复数传播再投影(TriWCP)，精确约束相干传播行为，并通过动量记忆机制有效抑制干扰累积。此外，引入了高频率跨层补偿增强机制，构造多尺度感受野的频率选择性路径，动态建模多层间的结构一致性，进一步提高模型在复杂环境条件下的鲁棒性和可解释性。
### Conclusion
在四个实际收集的数据集上的大量实验表明，WavePCNet在准确性和鲁棒性方面均优于现有最先进的方法。
## 750. `cs.LG` - 基于冲击回波信号和神经网络的混凝土板完整性数据驱动评估 [PDF](https://arxiv.org/pdf/2511.21080), [HTML](https://arxiv.org/abs/2511.21080)
### Authors
Yeswanth Ravichandran,Duoduo Liao,Charan Teja Kurakula
### Background
混凝土桥面的深层缺陷如脱层、空洞和蜂窝状结构严重影响其耐久性，但这些缺陷通过视觉检查或手动敲击难以可靠地检测。现有的检测方法效率低且不准确。因此，本文提出了一种基于机器学习的冲击回波（IE）方法，实现了缺陷定位和常见混凝土缺陷的多类分类。
### Innovation
该研究提出了一种全新的冲击回波监测框架，通过快速傅里叶变换（FFT）将原始信号转化为主要的频域特征，并通过无监督k-means聚类和伪造缺陷标签瓜纳的掩膜（Ground Truth Masks，GTMs）验证空间精度。利用长短期记忆（LSTM）网络对四种不同类型的缺陷进行分类，整体准确率达到73%。此外，该方法在实际桥梁混凝土板上的验证表明，实验室数据训练的模型在真实的耦合、噪声和环境变化条件下具有较好的通用性。
### Conclusion
提出的框架加强了非破坏性评估（NDE）的客观性、可扩展性和可重复性，支持大规模桥梁健康监测。
## 751. `cs.LG` - 使用音素特征增强变换器进行低资源缅甸语ASR错误纠正 [PDF](https://arxiv.org/pdf/2511.21088), [HTML](https://arxiv.org/abs/2511.21088)
### Authors
Ye Bhone Lin,Thura Aung,Ye Kyaw Thu,Thazin Myint Oo
### Background
本文调查了针对低资源缅甸语自动语音识别(ASR)错误纠正的序列到序列Transformer模型，重点在于不同的特征整合策略，包括音标（IPA）和对齐信息。据我们所知，这是首个针对缅甸语进行ASR错误纠正的研究。
### Innovation
本文提出了结合音素特征和对齐特征的ASR错误纠正（AEC）模型，该模型在未增强和增强后的平均词错误率（WER）分别降低了12.74%和18.01%，并且chrF++得分提高了7.18%。这一改进表明了AEC模型在ASR输出改进方面的一致性优势。
### Conclusion
本文的结果强调了AEC的鲁棒性和在低资源设置中提高ASR输出性能的重要性。通过设计有效的特征可以显著提高ASR模型的准确性和稳健性。
## 752. `cs.LG` - 即便有AI，发现双射仍然困难：OpenEvolve在新颖双射构造中的机遇与挑战 [PDF](https://arxiv.org/pdf/2511.20987), [HTML](https://arxiv.org/abs/2511.20987)
### Authors
Davis Brown,Jesse He,Helen Jenne,Henry Kvinge,Max Vargas
### Background
现有的程序生成系统如AlphaEvolve、OpenEvolve和ShinkaEvolve等提供了AI辅助数学发现的新方法。这些系统通过使用大型语言模型（LLMs）生成可读代码的候选解决方案，并进一步‘进化’这些解决方案以提高其质量。现有的数学应用主要集中在边界判定问题上（例如球填充），但程序合成方法适用于任何形式的显式构造的解的问题。基于此，本文探讨了OpenEvolve在组合双射发现中的应用。
### Innovation
本文应用OpenEvolve来解决组合双射构造问题，并对已知和未知的双射构造问题进行了研究。这证明了这些系统在数学组合学家中的潜在价值，同时也强调了目前这些系统的局限性，使得人类数学家的角色依然不可或缺。
### Conclusion
研究结果表明，虽然像OpenEvolve这样的系统具有潜力，但发现具有研究水平的新型双射仍然是当前前沿系统面临的一大挑战。这突显了在这些系统中加入人类数学家的重要性，并为其他研究者提供了一些宝贵的经验教训，他们正在探索这些系统的应用。
## 753. `cs.LG` - Crowdsourcing the Frontier: Advancing Hybrid Physics-ML Climate Simulation via $50,000 Kaggle Competition [PDF](https://arxiv.org/pdf/2511.20963), [HTML](https://arxiv.org/abs/2511.20963)
### Authors
Jerry Lin,Zeyuan Hu,Tom Beucler,Katherine Frields,Hannah Christensen,Walter Hannah,Helge Heuer,Peter Ukkonnen,Laura A. Mansfield,Tian Zheng,Liran Peng,Ritwik Gupta,Pierre Gentine,Yusef Al-Naher,Mingjiang Duan,Kyo Hattori,Weiliang Ji,Chunhan Li,Kippei Matsuda,Naoki Murakami,Shlomo Ron,Marec Serlin,Hongjian Song,Yuma Tanabe,Daisuke Yamamoto,Jianyao Zhou,Mike Pritchard
### Background
亚网格机器学习（ML）参数化有潜力引入新一代气候模型，这些模型能够包含更高分辨率物理效应的影响，而不需要更显式物理模拟带来的高昂计算成本。然而，诸如在线不稳定性和在线表现不一致等关键问题限制了它们在长期气候预测中的实际应用。为此，领域科学家和机器学习研究者通过发布ClimSim数据集和Kaggle竞赛，将亚网格ML参数化的离线方面问题开放给更广泛的机器学习和数据科学社区，以加速解决这些问题的进程。
### Innovation
通过Kaggle竞赛，本研究结合了获胜团队构建的类推架构和一个包含全云微物理的互动气候模型，系统地评估它们的在线性能。研究结果表明，在低分辨率的真实地理环境中，跨多种多样架构的在线稳定性是可以复制的，这被视为一个里程碑事件。所有测试的架构在某些指标（如经度平均偏差模式和全球均方根误差）上均表现出SOTA（目前最先进的）结果，这表明通过众包解决亚网格ML参数化问题的离线本质是提高混合物理-人工智能气候模拟在线性能的一条途径。
### Conclusion
本研究通过Kaggle竞赛展示了在线稳定性在低分辨率、真实地理设置下的可重复性，表明跨多种架构的在线性能较为一致。同时，多种在Kaggle竞赛中激发的新架构实现了某些指标上的SOTA结果，这表明众包能够有效提升混合物理-人工智能气候模拟的在线性能。
## 754. `cs.LG` - 基于上下文学习中的语义锚点：为什么小型LLM无法翻转其标签 [PDF](https://arxiv.org/pdf/2511.21038), [HTML](https://arxiv.org/abs/2511.21038)
### Authors
Anantha Padmanaban Krishna Kumar(Boston University)
### Background
该研究探讨了上下文学习（ICL）是否能够翻转预训练标签的语义，或者只是对现有语义基础进行微调。通过分析大型语言模型（LLM）在自然示范（正确标签）和倒置示范（系统性翻转标签语义）下的行为来回答这个问题。
### Innovation
该研究引入了语义覆盖率的概念，定义为在翻转语义下的正确性，将ICL行为分解为真实性、先验对齐度和提示对齐度三个度量指标。实验结果表明，在自然示范下，ICL改进准确性同时保持较强的先验对齐度；而在倒置示范下，模型不能学习连贯的反向语义分类器，表明ICL主要是通过调整输入在预训练稳定语义方向上的投影来工作的。
### Conclusion
在小规模LLM中，ICL主要调整输入如何在预训练中学习到的稳定语义方向上投影，而不是灵活地重新映射标签语义。因此，在这些规模下翻转标签需要超出ICL的方法和干预。
## 755. `cs.LG` - 非凸惩罚LAD估计在带有DNNs的部分线性模型中的渐近分析和邻近算法 [PDF](https://arxiv.org/pdf/2511.21115), [HTML](https://arxiv.org/abs/2511.21115)
### Authors
Lechen Feng,Haoran Li,Lucky Li,Xingqiu Zhao
### Background
本文研究了部分线性模型中使用最小绝对偏差（LAD）回归的方法。非参数项通过深度神经网络（DNNs）进行参数化，形成了一个加罚的LAD问题。研究过程中遇到了如下挑战：首先，正则化项可能既非凸也非光滑，这需要在渐近正态性讨论中引入无限维变分分析和非光滑分析；其次，随着样本数量的增加，网络需要扩展（宽度、稀疏性和深度），这为理论分析带来了更多的难度；第三，所提出的估计器的Oracle本身便是通过一个超高维度、非凸和不连续的优化问题定义的，这也带来了很多计算和理论上的挑战。
### Innovation
在如此多挑战下，本文建立了估计器的相合性、收敛速度和渐近正态性。进一步分析了Oracle问题及其连续松弛形式，并研究了两种形式下的渐近算法的收敛性。特别之处在于，松弛形式的估算允许显著更便宜的邻近更新，反映了统计精度和计算可行性之间的内在权衡。
### Conclusion
本文证明了在带深度神经网络的部分线性模型中，非凸惩罚LAD估计器的收敛性、收敛速度和渐近正态性。同时对问题本身及其连续松弛进行了分析，并研究了两种定义下的渐近算法的收敛性，揭示了这两种方法在迭代过程中不同的结构特性。
## 756. `cs.LG` - MortgageLLM：通过残差指令转移、对齐调优和任务特定路由的领域自适应预训练 [PDF](https://arxiv.org/pdf/2511.21101), [HTML](https://arxiv.org/abs/2511.21101)
### Authors
Manish Jain,Satheesh Kumar Ponnambalam,Salman Faroz,Chandrakanth Lns,Vinay Sharma
### Background
大型语言模型（LLMs）在通用领域展现了出色的能力，但在特定领域如抵押贷款金融的应用中，则需要增加特定领域的知识以保持指令跟随的一贯性。现有方法常采用单一多任务模型，但这种模型在优化结构化任务时会牺牲对话一致性，反之亦然。因此，开发一个针对特定领域优化的大型语言模型，同时解决这一矛盾是必要的。
### Innovation
本文提出了MortgageLLM，这是一种采用双重专家架构的特定领域大语言模型。通过双重专业化框架从单一基础模型（LLaMA-3.1-8B）开发而来。该方法通过双重专家机制解决单一多任务模型的性能权衡问题，既能够优化结构化任务又能保持对话一致性。通过指令残差技术，在领域适应后恢复指令跟随能力，无需监督微调。此外，还贡献了残差技术在抵押贷款金融高度专门化领域的应用，双重专家架构，以及使用其中一个专家模型执行少量示例分类的智能任务路由机制。
### Conclusion
通过评估领域特定基准模型发现，最终模型MortgageLLM v2在总结、问答和分类任务上的表现显著优于基础模型LLaMA-3.1-8B-Instruct。在总结任务上，LLM作为法官的总结得分为4.58（相比4.0），问答得分为4.09（相比4.0），分类得分为2.6（相比1.2）。同时，模型在语义相似性任务上也表现出色，BertScore分别在总结、问答和分类任务上分别达到0.77、0.68、0.75（相比0.74、0.58、0.73），大幅优于基线方法。
## 757. `cs.LG` - 从扩散到一步生成: 基于流的模型比较研究及其在图像修复中的应用 [PDF](https://arxiv.org/pdf/2511.21215), [HTML](https://arxiv.org/abs/2511.21215)
### Authors
Umang Agarwal,Rudraksh Sangore,Sumit Laddha
### Background
本文对三种生成建模范式进行了全面的比较研究：去噪扩散概率模型（DDPM）、条件流匹配（CFM）和MeanFlow。DDPM和CFM需要迭代采样，而MeanFlow可以通过建模时间区间的平均速度实现直接的一步生成。研究使用统一的TinyUNet架构在CIFAR-10数据集上实现了这三种方法，展示了CFM在50步时达到24.15的FID，显著优于DDPM（FID 402.98）。
### Innovation
本文创新地引入了基于流的模型，特别是CFM和MeanFlow，通过建模平均速度实现了直接一步生成，显著减少了推理时间。此外，作者将CFM扩展到图像修复领域，实现了掩码引导采样，通过微调实现了显著的性能提升，PSNR和SSIM均有大幅提高，证明了修复意识训练的有效性。
### Conclusion
CFM和MeanFlow方法在图像生成和修复任务中表现出色，特别是MeanFlow实现了单一步骤采样的快速生成，而CFM则在图像修复上取得了显著的效果提升。
## 758. `cs.LG` - 最大可加Donsker-Varadhan表示法在可能性变异推断中的应用 [PDF](https://arxiv.org/pdf/2511.21223), [HTML](https://arxiv.org/abs/2511.21223)
### Authors
Jasraj Singh,Shelvia Wongso,Jeremie Houssineau,Badr-Eddine Chérief-Abdellatif
### Background
变分推断（VI）是现代贝叶斯学习的基石，能够使得在处理复杂模型时实现近似推理，而无需面对积分等高维度问题，从而避免了完全解析处理的不可能性。然而，变分推断的表征依赖于通过高维积分定义的期望和发散度，这通常使得其难以进行精确处理，迫使人们依赖于近似学习和推理技术。动力学理论是一种不精确概率框架，能够直接建模信仰不确定性而非依赖于主观概率。尽管动力学理论为稀疏或不精确信息提供了鲁棒性和可解释性，但它将变分推断与可能性设置相结合需要重新思考核心概念，如熵和发散度，这些概念本身假定了可加性。
### Innovation
本文发展了可能性变异推断的原理型表述，并将其应用于特定类型的指数族函数，突出了这在概率对应物中所体现的相似性，并揭示了可能性理论的独特的数学结构。
### Conclusion
本文提出了最大可加Donsker-Varadhan表示法的可能性变异推断，不仅为建模复杂模型提供了新的理论基础，而且展示了概率推断和可能性推断之间的数学结构差异。
## 759. `cs.LG` - 使用柯尔莫哥洛夫-阿诺尔德网络头部微调提升缅甸新闻分类 [PDF](https://arxiv.org/pdf/2511.21081), [HTML](https://arxiv.org/abs/2511.21081)
### Authors
Thura Aung,Eaint Kay Khaing Kyaw,Ye Kyaw Thu,Thazin Myint Oo,Thepchai Supnithi
### Background
在资源有限的语言（如缅甸语）中，分类任务通常仅微调最终分类层，而冻结预训练编码器的权重。虽然多层感知机通常被使用，但其固定的非线性性限制了其表达能力并增加了计算成本。
### Innovation
本文探索了柯尔莫哥洛夫-阿诺尔德网络（KANs）作为替代分类头的方法，评估了基于傅里叶变换的FourierKAN、基于插值的EfficientKAN以及基于网格的FasterKAN在TF-IDF、fastText和多语言变压器（mBERT、Distil-mBERT）等不同嵌入中的性能。
### Conclusion
实验结果表明，基于KAN的头部与多层感知机相当或更优。EfficientKAN结合fastText取得了最高F1分数（0.928），而FasterKAN提供了速度和准确性的最佳权衡。在变压器嵌入中，EfficientKAN与mBERT相当或略优于多层感知机（F1分数0.917）。这些发现突出了KANs作为低资源语言分类中具有表达能力且高效的替代多层感知机的可能性。
## 760. `cs.LG` - RosettaSpeech: 仅从单语数据进行零样本语音到语音翻译 [PDF](https://arxiv.org/pdf/2511.20974), [HTML](https://arxiv.org/abs/2511.20974)
### Authors
Zhisheng Zheng,Xiaohang Sun,Tuan Dinh,Abhishek Yanamandra,Abhinav Jain,Zhu Liu,Sunil Hadap,Vimal Bhat,Manoj Aggarwal,Gerard Medioni,David Harwath
### Background
平行语音语料库的稀缺严重阻碍了语音到语音翻译（S2ST），迫使人们依赖复杂的多阶段管道。目前的系统通常需要大量的平行语音对进行训练和翻译。
### Innovation
提出了RosettaSpeech，这是一种新颖且简化的方法，采用单语语音-文本数据并通过机器翻译监督进行训练。该方法利用基于文本的神经机器翻译（NMT）模型固有的语言知识，但在训练中通过文本充当中间桥梁，而在推理中则作为直接和端到端的语音到语音模型运行。这种方法在标准基准上实现了最先进的结果，出乎意料地在CVSS-C测试集中表现超过了领先系统，成绩显著提高。
### Conclusion
通过优先依赖丰富平行文本而不是难以获得的平行语音，RosettaSpeech提供了一条可扩展的途径，用于创建高质量的、保留说话者特性的S2ST，适用于更广泛的语言。
## 761. `cs.LG` - 基于RISC-V的用于边缘AI中深度可分离卷积的TinyML加速器 [PDF](https://arxiv.org/pdf/2511.21232), [HTML](https://arxiv.org/abs/2511.21232)
### Authors
Muhammed Yildirim,Ozcan Ozturk
### Background
边缘AI和TinyML应用对设备智能的需求日益增长，需要更高效的现代卷积神经网络（CNN）执行。虽然像MobileNetV2这样的轻量级架构通过使用深度可分离卷积（DSC）来降低计算复杂度，但其多阶段设计引入了一个关键的性能瓶颈：逐层执行中的高能量和延迟成本，因为中间特征图需要转移到大型片上缓冲区或外部DRAM中。为此，本文提出了一种新型硬件加速器架构，利用融合像素级数据流来解决这一问题。
### Innovation
本文提出的架构作为RISC-V处理器的自定义函数单元（CFU）实现，完全消除了中间缓冲的需求，与传统的逐层执行相比，数据移动最多减少了87%。它通过紧密耦合的流水线一次性计算所有DSC阶段（扩展、深度可分离卷积和投影）的单一输出像素，而无需写入内存。在Xilinx Artix-7 FPGA上评估时，与RISC-V内核的基线软件执行相比，该设计实现了高达59.3倍的加速。进一步的ASIC综合表明，在28纳米工艺下，其芯片面积为0.284 mm²，功耗为910 mW，在2 GHz，而在40纳米工艺下，芯片面积为1.20 mm²，功耗为233 mW，在300 MHz下。
### Conclusion
本文的工作证明了在TinyML资源限制内实现零缓冲数据流的可行性，提供了克服边缘AI加速器中的内存墙的一种新颖且有效的方法。
## 762. `cs.LG` - The Spheres数据集：用于音乐源分离和信息检索的多轨交响乐团录音 [PDF](https://arxiv.org/pdf/2511.21247), [HTML](https://arxiv.org/abs/2511.21247)
### Authors
Jaime Garcia-Martinez,David Diaz-Guerra,John Anderson,Ricardo Falcon-Perez,Pablo Cabañas-Molero,Tuomas Virtanen,Julio J. Carabias-Orti,Pedro Vera-Candeas
### Background
本文介绍了The Spheres数据集，这是一个多轨管弦乐录音数据集，旨在推动音乐源分离及相关MIR任务中的机器学习研究，特别是在古典音乐领域。该数据集由Colibrì管弦乐团在The Spheres录音室录制超过一小时的音乐录音组成，其中包括柴可夫斯基的《罗密欧与朱丽叶》和莫扎特的《第40交响曲》的两个经典作品片段，以及每个乐器的全音阶和独奏片段。
### Innovation
该数据集采用了23个麦克风的录音设置，包括近场、主麦克风和环境麦克风，这有助于创建具有受控染色的逼真立体声混合，并提供孤立的音频轨用于监督训练源分离模型。此外，还为每个乐器位置估计了房间冲激响应，提供了录音空间的宝贵声学特征描述。该论文展示了数据集的结构、声学分析以及使用X-UMX模型进行管乐家族分离和麦克风去染色的基准评估结果。
### Conclusion
源分离在复杂管弦乐场景中的潜在能力和挑战得到了凸显，这强调了该数据集作为基准测试和探索分离、定位、去混响和古典音乐沉浸式渲染新技术的价值。
## 763. `cs.LG` - 盲解调PSK调制OFDM系统的相位感知编码辅助EM算法 [PDF](https://arxiv.org/pdf/2511.21340), [HTML](https://arxiv.org/abs/2511.21340)
### Authors
Chin-Hung Chen,Ivana Nikoloska,Wim van Houtum,Yan Wu,Alex Alvarado
### Background
本文提出了一个面向OFDM系统的全盲相位感知期望最大化（EM）算法，该算法适用于PSK调制。传统盲EM估计算法存在一个已知的问题，即局部最大值问题，这是由于信道估计中未知的相位不确定性所致，而常规的盲EM估计器无法解决这一问题。
### Innovation
提出了利用解码器的外在信息作为模型证据指标的方法，解决相位不确定性问题。基于PSK调制的固有对称性生成有限集合的候选模型，并由解码器选择最可能的候选模型。结果表明，此方法结合简单的卷积码后，在频域选择性信道中能有效解决相位不确定性，减少局部收敛率至几乎为零。
### Conclusion
该算法在EM初始化阶段之后仅执行一次，不会显著增加后续Turbo迭代中的复杂性。
## 764. `cs.LG` - 总声子热导率与总热导率的比率：一种基于数据的热电材料设计方法 [PDF](https://arxiv.org/pdf/2511.21213), [HTML](https://arxiv.org/abs/2511.21213)
### Authors
Yifan Sun,Zhi Li,Tetsuya Imamura,Yuji Ohishi,Chris Wolverton,Ken Kurosaki
### Background
热电（TE）材料对于能源捕获前景广阔，衡量性能的指标是热导率因子ZT。为了加快高ZT材料的发现，研究重点放在识别具有低热导率κ的化合物上。基于一个包含71,913个条目的数据集，研究展示了高ZT材料不仅存在于低κ区间，还聚集在约0.5的晶格热导率与总热导率比值κ_L/κ附近的区域，这与晶格玻恩电子晶体设计概念一致。
### Innovation
研究构建了一个框架，其中包含两个机器学习模型来量化晶格和电子导热性，一起提供 κ 和 κ_L/κ 以筛选和指导TE材料的优化。在筛查的104,567个化合物中，模型识别出了2,522个超低κ候选物。进一步的案例研究表明，该框架可以可靠地提供优化策略，通过建议新的掺杂剂和合金来将纯净材料向κ_L/κ接近0.5的区域转移。
### Conclusion
通过结合快速筛选与PGEC引导的优化，数据驱动框架有效地填补了材料发现与性能提升之间的关键缺口。
## 765. `cs.LG` - 关于对数导数算子的周期轨道 [PDF](https://arxiv.org/pdf/2511.21283), [HTML](https://arxiv.org/abs/2511.21283)
### Authors
Xiaohang Yu,William Knottenbelt
### Background
本文研究了在复分析环境中对数导数算子 $?mathcal{A}[f]=frac{text{d}text{ln} f}{text{d}text{ln} x}$ 的周期行为。
### Innovation
作者展示了 $?mathcal{A}$ 具有真正非退化周期-2轨道，并识别出一个典型的显式例子。进一步地，作者对所有非退化周期-2解进行了完全分类，这些解恰好是形式为 $(c a x^{c}/(1-ax^{c}),frac{c}{1-ax^{c}})$ 的有理对，其中 $ac eq 0$。作者还对 $?mathcal{A}$ 的所有不动点进行了分类，证明了任何使 $?mathcal{A}[f]=f$ 成立的解都有形式 $f(x)=frac{1}{a-text{ln} x}$。
### Conclusion
这些结果显示了 $?mathcal{A}$ 的低周期结构，并提供了一个由操作引起的函数空间上的动力学的可处理的实例，同时示例说明了对数型函数在变量变化下会进入周期-2家族中的一次迭代。
## 766. `cs.LG` - 可微物理神经模型加速非马尔可夫闭合学习以实现快速粗粒度物理仿真 [PDF](https://arxiv.org/pdf/2511.21369), [HTML](https://arxiv.org/abs/2511.21369)
### Authors
Tingkai Xue,Chin Chun Ooi,Zhengwei Ge,Fong Yew Leong,Hongying Li,Chang Wei Kang
### Background
数值模拟在许多物理和现实世界问题中提供关键见解。然而，尽管这些模拟在完全的3D域中求解，但大多数分析只需要较少的度量（例如平面浓度）。这项工作提出了一种物理-神经模型混合模型，可以比三维模拟快数个数量级的速度预测复杂域中的标量传输（从几小时压缩到不到1分钟）。该端到端可微分框架同时学习物理模型参数化（即各向异性扩散性）和非马尔可夫神经闭合模型，以捕捉未解析的‘粗化’效应，从而实现稳定的长期仿真。该模型具有高效的数据学习（仅需26个训练数据），并且可以灵活扩展到离分布场景（配备移动源），最终仿真时间的Spearman相关系数为0.96。
### Innovation
提出了一种集物理模型和非马尔可夫神经闭合模型于一体的可微分物理神经模型，能够快速准确地预测复杂域中的标量传输，同时学习物理模型参数化和非马尔可夫神经闭合模型。该模型具有高效的数据学习能力，并且能够灵活扩展到离分布场景。
### Conclusion
这种可微分物理神经框架能够为物理现象提供快速、准确和通用的粗粒度代理模型。
## 767. `cs.LG` - 大规模语言模型中模型合并技术的系统研究 [PDF](https://arxiv.org/pdf/2511.21437), [HTML](https://arxiv.org/abs/2511.21437)
### Authors
Oğuz Kağan Hitit,Leander Girrbach,Zeynep Akata
### Background
模型合并技术将多个细调检查点合并成单一模型而不进行额外的训练，这为重用模型和高效提高性能提供了有吸引力的方法。然而，对于小型模型和分类器所报告的优势是否适用于LLMs仍然不清楚。本文通过大规模系统评估六种最新的合并方法，包括近期的子空间方法，对四种开放权重的LLM进行了评估，每个基础模型有十二个细调检查点，并且在十六个标准LLM基准上进行了评估。研究表明，最古老且最简单的任务算术方法是唯一在LLMs中可靠地实现性能提升的方法。其它扰动感知和子空间合并方法通常会导致性能显著下降。这表明现有的合并技术不能直接应用于现代LLMs。
### Innovation
本文进行了一次大规模的系统评估，测试了六种最新的合并方法，包括子空间方法，覆盖了四种开放权重的LLMs、每个基础模型的十二个细调检查点以及十六个标准LLM基准。通过标准化的基准测试测量合并模型是否优于基础模型以及相对于最佳单个检查点的相对增益。
### Conclusion
研究结果表明，最古老的且最简单的方法，任务算术，是唯一在LLMs中可靠地实现性能提升的方法。其他干扰感知和子空间合并方法通常会导致性能显著下降。这表明当前的合并技术不能直接应用于现代LLMs。因此，这些发现激励我们设计针对LLMs的特定合并算法和合并感知的微调方法。
## 768. `cs.LG` - Merge and Bound: 直接在权重上进行操作的类增量学习方法 [PDF](https://arxiv.org/pdf/2511.21490), [HTML](https://arxiv.org/abs/2511.21490)
### Authors
Taehoon Kim,Donghwan Jang,Bohyung Han
### Background
类增量学习（CIL）是一个在模型训练过程中，逐步引入新类别的问题，同时保留之前学习到的知识，避免灾难性遗忘。传统的CIL方法主要关注如何优化模型而较少涉及直接对权重的操作。
### Innovation
提出了一种新的训练方法，Merge-and-Bound（M&B），该方法直接在参数空间中操作模型权重。M&B 方法包含两种类型的操作：跨任务的权重合并和同任务的权重合并。提出了限制更新技术，可以优化目标模型，并尽量减少累积更新，同时保持之前任务的知识。这种方法展示了在保留之前知识的同时，可以有效构建新的模型，减缓灾难性遗忘。
### Conclusion
M&B 方法无缝集成到现有的CIL方法中，无需修改架构组件或更改学习目标。在标准的CIL基准测试上，M&B 的性能优于现有的先进方法。
## 769. `cs.LG` - 在高维线性回归估计中：Post-Double-Autometrics作为Post-Double-Lasso的替代方法 [PDF](https://arxiv.org/pdf/2511.21257), [HTML](https://arxiv.org/abs/2511.21257)
### Authors
Sullivan Hué,Sébastien Laurent,Ulrich Aiounou,Emmanuel Flachaire
### Background
当目标是准确估计感兴趣的参数（如平均处理效应）时，Post-Double-Lasso成为处理许多协变量的线性回归模型的最常用方法。然而，在有限样本中，此方法可能会遭受显著的遗漏变量偏差。这一背景下，该研究探讨了一种新的方法，名为Post-Double-Autometrics，该方法基于Autometrics方法。
### Innovation
作者提出了一种新的方法Post-Double-Autometrics，并证明了这种方法在有限样本条件下显著优于Post-Double-Lasso。此外，作者将新方法应用于经济增长的经典应用，这为贫国向富国的收敛假设提供了一种新的视角。
### Conclusion
Post-Double-Autometrics方法在处理包含许多协变量的高维线性回归模型时更为优越，特别是在有限样本情况下。在经济增长应用中，这种方法提供了对经济收敛假设的新见解。
## 770. `cs.LG` - 推理视觉语言模型在测试时计算量上是否呈逆向缩放？一个以干扰项为中心的经验分析 [PDF](https://arxiv.org/pdf/2511.21397), [HTML](https://arxiv.org/abs/2511.21397)
### Authors
Jiyun Bae,Hyunjong Ok,Sangwoo Mo,Jaeho Lee
### Background
此前对语言模型的研究报告了逆向缩放效应，其中文本干扰项导致较长但不那么有效的推理。为了探讨类似现象是否发生在跨模态设置中，作者引入了一个名为Idis的数据集，该数据集系统地在语义、数值和空间维度上变化干扰项。研究表明，视觉干扰项与文本干扰项存在根本差异，尽管逆向缩放依然存在，但增加视觉干扰项不会增加推理长度却降低了准确性。
### Innovation
作者通过Idis数据集系统地研究了视觉干扰项对视觉语言模型推理时计算的影响，并且发现视觉干扰项与文本干扰项的本质不同在于，虽然逆向缩放现象依然存在，但是增加视觉干扰项并未延长推理时间但降低了准确性。通过跟踪推理过程中的属性计数，作者揭示了干扰项、推理长度和准确性之间的关系。
### Conclusion
研究结果表明，逆向缩放现象不仅存在于文本干扰项方面，同样也存在于视觉干扰项方面。这就提出了更高的要求，我们需要通过建立简单的提示策略来减轻推理模型中的偏差驱动预测。同时，研究结果显示，这些趋势也在Waterbirds等已有的视觉偏见基准测试中得以体现。
## 771. `cs.LG` - 在高阶网络中学习多阶块结构 [PDF](https://arxiv.org/pdf/2511.21350), [HTML](https://arxiv.org/abs/2511.21350)
### Authors
Kazuki Nakajima,Yuya Sasaki,Takeaki Uno,Masaki Aida
### Background
高阶网络，自然地用超图表示，对于包含三个或更多实体相互作用的现实系统建模至关重要。随机块模型提供了一个有原则的框架来描述中间尺度组织，但将其扩展到超图时，会存在表达能力和计算复杂性之间的权衡。最近的一个简化版本，单一阶模型通过假设单一亲和模式指导所有阶的相互作用来减轻这种复杂性。但是，这种普遍假设可能会忽略阶依赖性的结构性细节。
### Innovation
本文提出了一种框架，通过引入多阶块结构放宽了单一阶模型的假设。多阶块结构中，不同的亲和模式控制着不同阶的相互作用子集。该框架基于多阶随机块模型，并搜索最大化预测超链接性能的交互阶的最优分区。研究表明，在多种现实网络中，多阶块结构普遍存在。这一发现不仅提供了比单一阶模型更好的预测性能，还揭示了更清晰、更可解释的中间尺度组织。
### Conclusion
我们的研究结果揭示了阶依赖性机制是现实高阶网络中间尺度组织的关键特征。通过引入多阶块结构，我们揭示了更具解释性的中间尺度组织，并改善了预测性能。
## 772. `cs.LG` - TAB-DRW：基于DFT的稳健生成表格数据水印 [PDF](https://arxiv.org/pdf/2511.21600), [HTML](https://arxiv.org/abs/2511.21600)
### Authors
Yizhou Zhao,Xiang Li,Peter Song,Qi Long,Weijie Su
### Background
生成式AI的发展使得在医疗保健、金融和公共政策等领域能够生产高保真度的合成表格数据，但这也引发了一种担忧，即数据来源的真实性问题和滥用。现有的水印技术还存在许多局限性，包括计算成本高、难以处理混合离散-连续数据以及对于修改的鲁棒性差。
### Innovation
提出了一种名为TAB-DRW的高效且稳健的后编辑水印方案，用以生成表格数据。该方案通过频域嵌入水印信号：首先使用Yeo-Johnson变换和标准化来规范化异构特征，然后应用离散傅里叶变换（DFT），最后根据预先计算的伪随机数调整选择项的虚部。此外，还引入了一种新颖的基于排名的伪随机位生成方法，以便在无需增加存储开销的情况下实现按行检索。
### Conclusion
在五个基准表格数据集上的实验表明，TAB-DRW具有强大的检测能力和对常见后处理攻击的高鲁棒性，同时保持了数据的高保真度，并完全支持混合型特征。
## 773. `cs.LG` - 随着音速前进：将神经替代模型推向高度湍流的跨音速区间 [PDF](https://arxiv.org/pdf/2511.21474), [HTML](https://arxiv.org/abs/2511.21474)
### Authors
Fabian Paischer,Leo Cotteleer,Yann Dreze,Richard Kurle,Dylan Rubini,Maurits Bleeker,Tobias Kronlachner,Johannes Brandstetter
### Background
神经替代模型在汽车空气动力学中的广泛应用，得益于像DrivAerML和DrivAerNet++这样的数据集，主要集中在具有大涡流的钝体流动。然而，将这些方法扩展到航空航天领域，尤其是在跨音速范围内，仍然面临挑战，因为这涉及到压缩流体的高度非线性和三维效应，如翼尖涡。现有航空数据集主要集中在二维翼型上，忽略了这些关键的三维现象。因此，该研究提出了一个新的三维机翼在跨音速范围内的CFD仿真数据集，所有数据点都具有独特的几何形状和来流条件，从而为数据驱动的气动优化奠定了基础。
### Innovation
该论文展示了跨音速范围内三维机翼的新的CFD数据集，包括体积和表面级别的场数据，针对近3万个样本进行分析，这为气动优化提供了新的依据。此外，该研究评估了几种最先进的神经替代模型，如Transolver和AB-UPT，发现AB-UPT在高湍流跨音速流场中表现出色，并能生成物理上一致的阻力-升力帕累托前沿，即便对于未见过的翼型配置也是如此。这突显了AB-UPT作为快速气动设计探索的有效工具的潜力。
### Conclusion
该研究的结果表明，AB-UPT可以近似未见几何形状下的阻力-升力帕累托前沿，这为提升未来的气动设计探索工具的效率和效果提供了新的方向。为了促进未来研究，该算法和数据集已经开源。
## 774. `cs.LG` - MMA：惯性传感器中的人体活动识别Momentum Mamba架构 [PDF](https://arxiv.org/pdf/2511.21550), [HTML](https://arxiv.org/abs/2511.21550)
### Authors
Thai-Khanh Nguyen,Uyen Vo,Tan M. Nguyen,Thieu N. Vo,Trung-Hieu Le,Cuong Pham
### Background
惯性传感器的人体活动识别(HAR)对于无处不在的计算、移动健康和环境智能至关重要。传统的深度模型如卷积神经网络(CNNs)、循环神经网络(RNNs)和变压器虽然提高了HAR的性能，但仍然受到梯度消失或爆炸的限制、高计算成本及长范围依赖捕捉困难的制约。而结构化状态空间模型(SSMs)如Mamba在复杂度为线性的情况下能够有效进行时间建模，但是它们只能处理一阶动态，缺乏稳定且长期的记忆机制。
### Innovation
我们提出了一种名为Momentum Mamba的增动量SSM，它通过引入二阶动力学增强信息在时间步骤中的流动稳定性、鲁棒性以及长序列建模能力。此外，Complex Momentum Mamba进一步扩大了其容量以实现频率选择性的记忆缩放。在多个HAR基准测试中，与原始Mamba和Transformer基线相比，Momentum Mamba在准确率、鲁棒性和收敛速度上表现出一致的改进。通过适度增加训练成本，增动量SSM为HAR和更广泛的序列建模应用提供了一种有利的准确性和效率均衡。
### Conclusion
增动量SSM在HAR中展现出可拓展的范式，并且是更广泛序列建模应用的有前景的主框架。
## 775. `cs.LG` - Stochastic Block Model with more than √n Communities （II）的相变现象 [PDF](https://arxiv.org/pdf/2511.21526), [HTML](https://arxiv.org/abs/2511.21526)
### Authors
Alexandra Carpentier,Christophe Giraud,Nicolas Verzelen
### Background
在网络分析中，一个基础的理论问题是确定在随机块模型（SBM）中，社区恢复在多项式时间内何时可能。当社区数 $K < root n ?$ 时，非平凡的社区恢复仅在Kesten—Stigum (KS)阈值之上在多项式时间内可能。然而，当 $K root n ?$ 时，最近的研究证明，在稀疏情况下，社区恢复在多项式时间内低于KS阈值是可能的，但这一问题在大多数密度情况下仍不清楚。
### Innovation
本文证明了Carpentier等人的猜想，通过构造满足特定结构性质的图样族，并证明在所提出的阈值之上通过计数这些图样可以实现社区恢复。这填补了在$K root n ?$社区的SBM中关于计算障碍的图景，并指出在适度稀疏情况下，最优算法可能与谱方法不同。
### Conclusion
本研究结果表明，对于具有$K root n ?$社区的SBM，计算障碍在于Chin等人提出的阈值，并且在适度稀疏情况下，最优算法与谱方法可能有所不同。
## 776. `cs.LG` - 超越准确性：插补中不确定性估计的实证研究 [PDF](https://arxiv.org/pdf/2511.21607), [HTML](https://arxiv.org/abs/2511.21607)
### Authors
Zarin Tahia Hossain,Mostafa Milani
### Background
数据驱动分析中的缺失数据处理是核心挑战。现代填补方法不仅追求准确重建，还以不同的方式表示和量化不确定性。然而，这些不确定性估计的可靠性和校准性尚未得到充分理解。
### Innovation
该论文进行了系统的实证研究，比较了来自三个主要家族的代表性填补方法：统计方法（MICE、SoftImpute）、分布对齐（OT-Impute）和深度生成模型（GAIN、MIWAE、TabCSDI）。研究通过多运行变异、条件采样和预测分布建模这三种互补路径估计不确定性，并使用校准曲线和期望校准误差（ECE）进行评估。研究发现，准确性与校准往往不一致：高重建准确率的模型并不一定具有可靠性。
### Conclusion
准确性与校准经常是不一致的，高重建准确率的模型未必具有可靠不确定性。该研究分析了方法特定的准确性和校准性之间的权衡，确定了稳定配置，并为数据清洗和下游机器学习管道选择感知不确定性的填补器提供了指南。
## 777. `cs.LG` - Matrix：节点间多代理合成数据生成框架 [PDF](https://arxiv.org/pdf/2511.21686), [HTML](https://arxiv.org/abs/2511.21686)
### Authors
Dong Wang,Yang Li,Ansong Ni,Ching-Feng Yeh,Youssef Emad,Xinjie Lei,Liam Robbins,Karthik Padthe,Hu Xu,Xian Li,Asli Celikyilmaz,Ramya Raghavendra,Lifei Huang,Carole-Jean Wu,Shang-Wen Li
### Background
合成数据在训练大数据模型中变得越来越重要，特别是在真实数据稀缺、昂贵或涉及隐私的情况下。许多合成任务需要协调多代理工作流程，其中专业代理协同工作以生产更高质量、更多样性和结构更丰富的数据。然而，现有的多代理合成框架往往依赖于一个中心协调者，这造成了扩展瓶颈，或者为特定领域进行了硬编码，限制了灵活性。
### Innovation
Matrix 提出了一个去中心化的框架，将控制和数据流表示为通过分布式队列传递的序列化消息。这种节点间设计消除了中心协调者。每个任务通过轻量级代理独立进行，而计算密集型操作，如大语言模型推理或容器化环境，则由分布式服务处理。Matrix 基于 Ray 架构，可以扩展到数以万计的并发代理工作流程，并提供了模块化和可配置的设计，使合成数据生成工作流程的适应变得更加容易。
### Conclusion
Matrix 在各种合成场景中进行了评估，包括多代理协同对话、基于网络的推理数据提取以及客户服务环境中工具使用轨迹生成。在所有情况下，Matrix 都在相同的硬件资源下实现了2-15倍更高的数据生成吞吐量，而不影响输出质量。
## 778. `cs.LG` - ToolOrchestra：通过高效模型和工具编排提升智能 [PDF](https://arxiv.org/pdf/2511.21689), [HTML](https://arxiv.org/abs/2511.21689)
### Authors
Hongjin Su,Shizhe Diao,Ximing Lu,Mingjie Liu,Jiacheng Xu,Xin Dong,Yonggan Fu,Peter Belcak,Hanrong Ye,Hongxu Yin,Yi Dong,Evelina Bakhturina,Tao Yu,Yejin Choi,Jan Kautz,Pavlo Molchanov
### Background
大型语言模型具有强大的通用性，但在解决如人类最后一考（HLE）这类深刻且复杂的任务时，仍存在概念上的挑战和计算的高昂成本。我们展示了小规模的调度器通过管理其他模型和各种工具，不仅可以提高智能的上限，还可以在解决困难的代理任务时提高效率。
### Innovation
引入ToolOrchestra方法，用于训练小规模调度器，协调智能工具使用。ToolOrchestra明确使用具有结果意识、效率意识和用户偏好意识的强化学习奖励。通过ToolOrchestra，我们创造了Orchestrator，这是一个8B的模型，在较低的成本下实现了更高的准确性，并在用户偏好方面与其一致，特别是在指定查询时应使用的工具方面。Orchestrator在HLE上的得分为37.1%，优于GPT-5的35.1%，同时效率提高了2.5倍。在tau2-Bench和FRAMES上，Orchestrator大幅超越GPT-5，而成本只有约30%。广泛的分析表明，Orchestrator在多个指标下实现了性能与成本的最佳权衡，并在未见工具上表现出稳健的泛化能力。这些结果证明，使用轻量级编排模型组合多种工具比现有方法更高效，更有效，开辟了实用和可扩展的增强推理系统的道路。
### Conclusion
这些结果显示，使用轻量级编排模型组合多样化工具比现有方法更高效且更有效，并为实用且可扩展的工具增强推理系统铺平了道路。
## 779. `cs.LG` - TraceGen: 三维轨迹空间中的世界模型使跨体态视频学习成为可能 [PDF](https://arxiv.org/pdf/2511.21690), [HTML](https://arxiv.org/abs/2511.21690)
### Authors
Seungjae Lee,Yoonkyo Jung,Inkook Chun,Yao-Chih Lee,Zikui Cai,Hongjia Huang,Aayush Talreja,Tan Dat Dao,Yongyuan Liang,Jia-Bin Huang,Furong Huang
### Background
从少量示范中让新平台上的新机器人在新场景中学习新的机器人任务仍然具有挑战性。虽然人类和不同机器人体态的视频资料丰富，但由于体态、摄像设备和环境的差异，这些视频资料无法直接使用。
### Innovation
该研究引入了一种统一、符号化的表示方法——场景级轨迹的紧凑的3D“轨迹空间”——这使得从跨体态、跨环境和跨任务的视频中学习成为可能。研究开发了TraceGen（轨迹生成器），它在轨迹空间而非像素空间预测未来运动，从而避开了视觉外观，保留了进行操作所需的几何结构。为了大规模训练TraceGen，研究开发了TraceForge（轨迹工坊），该数据流水线将异构的人类和机器人视频转换为一致的3D轨迹，形成了123K视频和1.8M观察-轨迹-语言三元组的资料库。使用该资料库进行预训练产生了一种可转移的3D运动先验，可以有效适应：只需要五个目标机器人的视频，TraceGen在四个任务中的成功率可达80%。即使只有五段未校准的手持手机上的人类示范视频，它仍然能够在一个真实机器人上实现67.5%的成功率，凸显了TraceGen不依赖于物体检测器或重像素空间生成的情况下跨体态适应的能力。
### Conclusion
该研究证明了TraceGen能够有效适应并提高从少量跨体态视频中学习的能力，即使在仅使用手持手机拍摄的未校准视频的情况下也能展现良好性能。
## 780. `cs.LG` - 具备生长与精炼多模态语义记忆的智能体学习者 [PDF](https://arxiv.org/pdf/2511.21678), [HTML](https://arxiv.org/abs/2511.21678)
### Authors
Weihao Bo,Shan Zhang,Yanpeng Sun,Jingjing Wu,Qunyi Xie,Xiao Tan,Kunbin Chen,Wei He,Xiaofan Li,Na Zhao,Jingdong Wang,Zechao Li
### Background
MLLMs在处理孤立查询时表现出强大的推理能力，但它们独立解决每个问题，经常重复相同的错误。现有的记忆增强代理主要存储过去轨迹用于重用，但这种基于轨迹的记忆会逐渐失去关键领域的知识。即使在真正多模态问题解决的情境下，也只能记录单一模态的行为轨迹，未能保留视觉注意力和逻辑推理如何共同导致最终解决方案。这与人类认知不一致，因为语义记忆是多模态且集成的，通过协调但独立的表征流保存视觉和抽象知识。
### Innovation
提出了一个双流记忆框架——ViLoMem，用于构建紧凑且基于模式的记忆。它分别编码视觉干扰模式和逻辑推理错误，使MLLMs能够从成功和失败的经验中学到东西。该系统遵循增长和精炼的原则，逐步积累和更新多模态语义知识，同时避免灾难性遗忘，从而稳定并泛化的学习策略。
### Conclusion
ViLoMem在六个多模态基准测试中，一致提高了准确率并显著减少了重复的视觉和逻辑错误。消除分析证实了双流记忆和显式干扰-幻觉分离的必要性，展示了有意识的多模态记忆对于终身和跨域代理学习的价值。
## 781. `cs.LG` - 双重平衡的多任务学习 [PDF](https://arxiv.org/pdf/2308.12029), [HTML](https://arxiv.org/abs/2308.12029)
### Authors
Baijiong Lin,Weisen Jiang,Feiyang Ye,Yu Zhang,Pengguang Chen,Ying-Cong Chen,Shu Liu,Ivor W. Tsang,James T. Kwok
### Background
多任务学习旨在同时学习多个相关任务，在各个领域均取得了巨大成功。然而，不同任务之间的损失和梯度尺度差异往往导致性能妥协，任务之间的平衡依然是一个重要的挑战。
### Innovation
本文提出了双重平衡多任务学习（DB-MTL），从损失和梯度两个视角实现任务平衡。DB-MTL 通过在每个任务损失上进行对数变换实现损失尺度平衡，并通过归一化所有任务的梯度使其具有可比的幅度来缩放梯度大小，使用最大梯度范数。在多个标准数据集上的广泛实验证明，DB-MTL 的性能始终优于当前最先进的方法。
### Conclusion
DB-MTL 通过双重平衡机制在多个标准数据集上展示了稳定的优越性能，克服了传统多任务学习中的挑战。
## 782. `cs.LG` - 启用语音识别中的差异隐私联邦学习：基准、自适应优化器和梯度裁剪 [PDF](https://arxiv.org/pdf/2310.00098), [HTML](https://arxiv.org/abs/2310.00098)
### Authors
Martin Pelikan,Sheikh Shams Azam,Vitaly Feldman,Jan ?Honza? Silovsky,Kunal Talwar,Christopher G. Brinton,Tatiana Likhomanenko
### Background
联邦学习（FL）和差分隐私（DP）虽然已经被广泛研究，但在自动语音识别（ASR）中的应用仍处于起步阶段。这是因为大型变换器模型的训练给FL带来了新的挑战，尤其是在层间梯度异质性方面。现有工作难以在没有DP机制的情况下使用标准优化技术进行收敛。
### Innovation
本文首次提出了用于端到端ASR的FL与DP基准。主要创新在于使用了逐层裁剪和逐层梯度规范化的方法，理论上这些技术有助于减轻深层模型中的裁剪偏差和层间梯度异质性。实验证明，即使在高隐私保障条件下，FL与DP在数百万用户群体中也是可行的。
### Conclusion
作者实现了在ASR中FL与DP的平衡，通过裁剪和逐层梯度规范化，实现了在数百万用户规模下，仅对词错误率有较小影响的差分隐私保障。这种方法不仅适用于ASR，还能为跨领域的大模型提供可扩展、隐私保护的FL设计原则。
## 783. `cs.LG` - TinyFormer: 在微小设备上高效设计和部署变压器 [PDF](https://arxiv.org/pdf/2311.01759), [HTML](https://arxiv.org/abs/2311.01759)
### Authors
Jianlei Yang,Jiacheng Liao,Fanding Lei,Meichen Liu,Lingkun Long,Junyi Chen,Han Wan,Bei Yu,Weisheng Zhao
### Background
微控制器（MCU）等微小设备在嵌入式物联网（IoT）应用中的智能学习发展受到了广泛关注。然而，由于这些设备的硬件资源严重受限，难以高效地设计和部署最新的模型（例如变压器）。为此，本文探讨了通过利用超网络（SuperNAS）、稀疏神经架构搜索（SparseNAS）和稀疏引擎（SparseEngine）的方法，提出了一种专为微小设备上高效设计和部署资源优化的变压器模型的框架（TinyFormer）。
### Innovation
TinyFormer通过三个关键模块构建：超级超网络（SuperNAS）用于寻找适合的超网络，稀疏神经架构搜索（SparseNAS）用于从查找网络中选择最好的单路径稀疏变压器模型，稀疏引擎（SparseEngine）利用低硬件资源有效地在微控制器上部署选择的模型。这是首个能够在微控制器上执行稀疏变压器模型推理的部署框架。
### Conclusion
TinyFormer在CIFAR-10数据集上的评估表明，即使受限于1MB存储和320KB的内存，该框架也可以设计出96.1%准确度的高效变压器。并且在稀疏推理方面，TinyFormer比CMSIS-NN库实现了高达12.2倍的加速。TinyFormer有望将强大的变压器模型引入TinyML领域，并大幅扩展深度学习的应用范围。
## 784. `cs.LG` - 单策略 vs. 双策略强化学习在动态自行车再平衡中的应用 [PDF](https://arxiv.org/pdf/2402.03589), [HTML](https://arxiv.org/abs/2402.03589)
### Authors
Jiaqi Liang,Defeng Liu,Sanjay Dominik Jena,Andrea Lodi,Thibaut Vidal
### Background
共享单车系统（BSS）为城市可持续交通提供了解决方案，但要确保其可靠性需要有效的再平衡策略来应对随机需求并防止站点失衡。
### Innovation
该论文提出了强化学习（RL）算法以解决具有多个车辆的动态再平衡问题，并引入和比较了两种RL方法：单策略RL和双策略RL。第一种方法使用一个深度Q网络（DQN）来联合学习库存和路径决策。第二种方法将节点级别的库存决策与路径级别的车辆路由分离，提高了学习效率和适应性。作者开发了一个高保真仿真器来评估不同需求场景下基于先到先服务规则的奖励。
### Conclusion
研究结果表明，虽然单策略模型在与多个基准的比较中表现出很好的竞争力，但双策略模型大幅减少了因缺货导致的需求损失。这些发现为共享单车运营商提供了有价值的见解，强化了RL在实时再平衡中的潜力，并为更加适应和智能的城市交通解决方案铺平了道路。
## 785. `cs.LG` - 联邦学习：一种随机逼近方法 [PDF](https://arxiv.org/pdf/2402.12945), [HTML](https://arxiv.org/abs/2402.12945)
### Authors
Srihari P V,Anik Kumar Paul,Bharath Bhikkaji
### Background
本文考虑了在随机逼近（SA）框架下的联邦学习（FL）。在这种设置下，每个客户端使用其本地数据集训练本地模型，并定期将模型参数传输给中央服务器，服务器汇总模型参数形成全局模型并回传。典型先前研究假设所有客户端在模型训练过程中具有相同（常数）的学习率，这导致汇总的模型仅在期望意义上收敛。本文提出客户端特有的衰减学习率，并证明了全局模型在概率意义上完全收敛。
### Innovation
引入了客户端特异的衰减学习率，使得全局模型能够以概率意义上的收敛追踪一个由客户负梯度加权和构成的微分方程，并通过调节这些权重，能够根据数据的稀有性来优化客户端的影响。
### Conclusion
通过数值实验验证了这种随机逼近方法的有效性，并展示了如何选择学习率以调控客户端对全局模型的影响，使得拥有稀有数据的客户端能够产生更大的影响。
## 786. `cs.LG` - 通过融合全局和局部统计信息进行数据估值 [PDF](https://arxiv.org/pdf/2405.17464), [HTML](https://arxiv.org/abs/2405.17464)
### Authors
Xiaoling Zhou,Ou Wu,Michael K. Ng,Hao Jiang
### Background
近年来，数据估值受到了广泛关注，因为高质量数据在各种应用中的关键作用。随着Shapley值方法因其坚实的理论基础而成为主流，其准确计算却往往因计算负担而变得不可能，导致开发出许多近似技术。然而，现有方法通常没有融入价值分布信息，也未能考虑到动态数据条件，这降低了它们的性能和应用潜力。
### Innovation
本文强调了在数据估值中融合全局和局部统计信息的关键作用。首先，通过一系列实证数据分析了不同模拟和实际数据集中的价值分布，揭示了有价值的见解和关键模式。其次，提出了一个改进的数据估值方法，将探索到的价值分布特征融合为两个正则项，以提高Shapley值的估计准确性。引入了一种新颖的动态数据估值方法，在无需重新计算Shapley值的情况下推断出更新的数据价值，从而显著提高了计算效率。此外，该正则化项可用于各种现有的数据估值方法。
### Conclusion
广泛的实验验证了我们提出的方法在数据估值中的有效性与效率，证实了全局和局部价值分布在数据估值中的重大潜力。
## 787. `cs.LG` - 不落一单：使用Medha解决长上下文大语言模型推理中的异构性问题 [PDF](https://arxiv.org/pdf/2409.17264), [HTML](https://arxiv.org/abs/2409.17264)
### Authors
Amey Agrawal,Haoran Qiu,Junda Chen,Íñigo Goiri,Chaojie Zhang,Rayyan Shahid,Ramachandran Ramjee,Alexey Tumanov,Esha Choukse
### Background
部署百万级大语言模型（LLM）具有挑战性，因为生产负载高度异构，混合了短查询和长文档。这种异构性与注意力机制的二次复杂性相结合，会导致“车队效应”，即长时间运行的请求阻塞了短交互请求，从而降低系统的响应性。
### Innovation
Medha 是一个服务系统，通过引入对LLM推理的细粒度、预emption调度来消除这些“车队效应”。Medha 通过包括自适应分块和流管道并行在内的共同设计方法，克服了分块的效率和扩展性挑战。此外，还提出了一种新的并行策略——KV 缓存并行，以减少解码延迟并提高交互性。这些机制由一种基于长度感知的相对余量调度器（LARS）协调，这是一种具有截止时间和异构性感知的调度策略，能够防止由简单策略引发的“车队效应”和饥饿现象。
### Conclusion
在异构负载下，与最先进的非预emption系统相比，Medha 的吞吐量提高了5.7倍，中位数和99百分位延迟分别减少了30倍和174倍。
## 788. `cs.LG` - CoxKAN: Kolmogorov-Arnold Networks for Interpretable, High-Performance Survival Analysis [PDF](https://arxiv.org/pdf/2409.04290), [HTML](https://arxiv.org/abs/2409.04290)
### Authors
William Knottenbelt,William McGough,Rebecca Wray,Woody Zhidong Zhang,Jiashuai Liu,Ines Prata Machado,Zeyu Gao,Mireia Crispin-Ortuzar
### Background
生存分析是医学中用于建模诸如死亡或复发等关键事件发生时间的重要统计分支，旨在改善治疗策略和患者结果。通常在生存模型的选择上，需要在性能和可解释性之间做出权衡，深度学习模型虽然性能优异，但缺乏传统方法的透明度。在医学领域，这成为了一大挑战，因为临床医生不愿意使用黑盒模型来做关键的病人决策。
### Innovation
本文介绍了CoxKAN，这是一种Cox比例风险Kolmogorov-Arnold网络，旨在实现具有解释性的高性能生存分析。Kolmogorov-Arnold网络（KAN）是一种新兴的、可解释的、准确的替代多层感知机的方法。研究者在四个合成数据集和九个真实数据集上进行了评估，其中包括五个包含临床数据的队列以及四个包含基因组学生物标记的数据集。实验证明，CoxKAN不仅能准确还原可解释的危险函数表达式，自动进行特征选择，并且在真实数据集上一再超越传统的Cox比例风险模型（提高C-指数高达4%），甚至在某些情况下超过了基于深度学习的模型。更重要的是，CoxKAN揭示了预测变量之间的复杂相互作用，并发现了符号公式，这是其他生存分析方法无法提供的，能够清晰揭示关键生物标记对患者风险的影响。
### Conclusion
CoxKAN在GitHub和Zenodo上均可获得，它提供了一种在保持高性能的同时保证高度可解释性的方法，为临床应用提供了新的解决方案。
## 789. `cs.LG` - HO-FMN: 基于超参数优化的快速最小范数攻击 [PDF](https://arxiv.org/pdf/2407.08806), [HTML](https://arxiv.org/abs/2407.08806)
### Authors
Raffaele Mura,Giuseppe Floris,Luca Scionis,Giorgio Piras,Maura Pintor,Ambra Demontis,Giorgio Giacinto,Battista Biggio,Fabio Roli
### Background
梯度导向的攻击是评估机器学习模型稳健性的主要工具，但许多攻击倾向于提供过于乐观的评估，因为它们使用固定损失函数、优化器、步长调度器和默认超参数。现有方法的这些局限性会对模型的真正稳健性进行误导。
### Innovation
提出了一种具有参数变才性的快速最小范数攻击算法的变体，其损失函数、优化器、步长调度器和超参数可以动态调整，从而使得攻击可以更好地适应不同的模型，并提高了评估的准确性。
### Conclusion
通过重新评估 12 种稳健模型，证明了该攻击方法能够找到较小的对抗扰动，而无需任何额外的调优。此外，该方法能够报告在扰动预算函数下的对抗鲁棒性，提供了一种比固定预算攻击更全面的评估手段，同时保持高效。开源代码已发布。
## 790. `cs.LG` - 超越内省：通过外部行为反馈强化思考 [PDF](https://arxiv.org/pdf/2501.01457), [HTML](https://arxiv.org/abs/2501.01457)
### Authors
Diji Yang,Linda Zeng,Kezhen Chen,Yi Zhang
### Background
在推理时间思考的过程中，大型语言模型能够解决复杂的难题，但由于模型的概率性质，其扩展的思考过程可能会变得不可靠或不一致，尤其是在知识边界附近。现有的方法通过让模型自己评估和纠正其推理来尝试减轻这种问题，但这种自我评估继承了原始输出中的偏见，即内省幻觉。本文分析了这种方法的局限性。
### Innovation
本文提出了一种基于行为学核心方法的外部主义框架——Distillation-Reinforcement-Reasoning（DRR），它不依赖于模型的内省，而是通过评估其可观察的行为来提供纠正反馈。DRR 包括三个步骤：首先分析推理者的行为痕迹，然后训练一个轻量级的外部判别模型（DM）。在推理过程中，该 DM 作为批评者，识别并拒绝可疑的推理步骤，这种外部反馈促使模型放弃有缺陷的路径，探索替代方法，从而提高推理质量而不改变基础模型。
### Conclusion
在多个推理基准测试上的实验表明，我们的框架显著优于现有的自我评估方法。由于其轻量级且无需标注的特点，DRR 提供了一种可扩展且适应性强的解决方案，用于提高各种 LLM 中推理的可靠性。
## 791. `cs.LG` - 通过矩阵分裂和预条件化统一线性函数逼近在离策强化学习中的视角 [PDF](https://arxiv.org/pdf/2501.01774), [HTML](https://arxiv.org/abs/2501.01774)
### Authors
Zechen Wu,Amy Greenwald,Ronald Parr
### Background
在离策强化学习中的经验策略评估(OPE)任务中，传统的观点认为，时差学习(TD)和拟合Q迭代(FQI)分别是针对目标价值函数更新一次、无限次和有限次数。本文作者指出这一观点并不准确，并通过线性价值函数逼近提供了一个新的数学视角，统一了这些方法作为解决同一个线性系统的单一迭代方法，但使用了不同的矩阵分裂方案和预条件器。
### Innovation
本文提供了一个新的数学视角统一了TD、PFQI和FQI，揭示了为何TD收敛并不一定意味着FQI收敛，并建立了TD、PFQI和FQI之间的紧密收敛联系。引入矩阵分裂的概念用于收敛分析，提供了比之前工作更尖锐的理论结果，且不要求关于特征（如线性独立）的假设；该框架也展示了学习率大小与收敛性之间的关系，并首次证明了当大学习率无效时，尝试较小的学习率可能会有帮助；并发现了特征收敛的新关键条件，展示了关于特征的常见假设如何影响收敛性。
### Conclusion
本文通过新的方法和视角，不仅统一了离策强化学习中的相关方法，而且还发现了新的收敛条件。该研究还展示了矩阵分裂在相关算法收敛性分析中的应用。
## 792. `cs.LG` - CroMe: 使用跨模态三元变换器和度量学习的多模态假新闻检测 [PDF](https://arxiv.org/pdf/2501.12422), [HTML](https://arxiv.org/abs/2501.12422)
### Authors
Eunjee Choi,Junhyun Ahn,XinYu Piao,Jong-Kook Kim
### Background
近年来，多模态假新闻检测受到了广泛关注。现有方法依赖于独立编码的单模态数据，忽视了通过高级技术捕捉跨模态相似性和模态内关系的优势。
### Innovation
提出了Cross-Modal Tri-Transformer和度量学习（CroMe）方法。CroMe 使用冻结的图像编码器和大型语言模型（BLIP2）来编码文本、图像和结合图像-文本表示。度量学习模块利用代理锚点方法捕捉模态内关系，而特征融合模块采用跨模态三元变换器进行有效集成。在数据集上的实验表明，CroMe 在多模态假新闻检测中表现优异。
### Conclusion
实验结果表明，CroMe 在多模态假新闻检测中表现出色。
## 793. `cs.LG` - 联邦大型语言模型：当前进展与未来方向 [PDF](https://arxiv.org/pdf/2409.15723), [HTML](https://arxiv.org/abs/2409.15723)
### Authors
Yuhang Yao,Jianyi Zhang,Junda Wu,Chengkai Huang,Yu Xia,Tong Yu,Ruiyi Zhang,Sungchul Kim,Ryan Rossi,Ang Li,Lina Yao,Julian McAuley,Yiran Chen,Carlee Joe-Wong
### Background
大型语言模型迅速受到欢迎并广泛应用于实际场景中。虽然优质训练数据至关重要，但在数据采集过程中也出现了隐私问题。联邦学习通过允许多个客户端协作训练语言模型而无需共享本地数据，提供了解决方案，但在这一过程中也引入了新的挑战，如异质数据导致的模型收敛问题和高昂的通信成本。
### Innovation
文章专注于联邦学习（FedLLM）领域的最新进展，特别是讨论了在联邦环境下的微调和提示学习。同时，文章提出了联邦大型语言模型的潜在发展方向，包括预训练、联邦代理和用于联邦学习的语言模型。
### Conclusion
本文旨在进行全面研究，以应对联邦学习中的挑战，并为未来的研究提供指导。
## 794. `cs.LG` - 低资源设备上的持续预测错误校正 [PDF](https://arxiv.org/pdf/2511.21652), [HTML](https://arxiv.org/abs/2511.21652)
### Authors
Kirill Paramonov,Mete Ozay,Aristeidis Mystakidis,Nikolaos Tsalikidis,Dimitrios Sotos,Anastasios Drosou,Dimitrios Tzovaras,Hyunjun Kim,Kiseok Chang,Sangdok Mo,Namwoong Kim,Woojong Yoo,Jijoong Moon,Umberto Michieli
### Background
随着AI模型在日常设备中的普及，预测错误开始损害用户体验。现有解决方案多集中于错误检测，但很少提供高效的更正机制，特别是针对资源受限设备的情况。
### Innovation
提出了一种新型系统，通过少量样本学习让用户能够校正AI的分类错误，同时减少计算资源和存储需求。该系统结合了服务器端大模型训练与设备端原型分类机制，通过原型更新实现高效的错误校正而非重新训练模型。
### Conclusion
系统在图像分类和对象检测任务上有效，单次校正能纠正超过50%的错误，同时几乎不产生遗忘现象（小于0.02%），且计算开销可忽略。通过Android演示应用验证了系统在实际场景中的可行性。
## 795. `cs.LG` - 超越URL：高效大型语言模型预训练的元数据多样性和位置 [PDF](https://arxiv.org/pdf/2511.21613), [HTML](https://arxiv.org/abs/2511.21613)
### Authors
Dongyang Fan,Diba Hashemi,Sai Praneeth Karimireddy,Martin Jaggi
### Background
近期研究表明，在大型语言模型（LLMs）的预训练中整合元数据成为一种有前景的加速训练方法。尽管先有研究仅强调了URL这一有用信号，但尚未探索其他形式的元数据是否能带来更多益处。
### Innovation
研究考察了更广泛类型的元数据，并发现细粒度的质量指标同样可以在预训练中通过前缀方式加速训练。研究还引入了元数据追加作为一种提高训练效率的新方法，通过预测合适的元数据作为辅助任务可以帮助加快预训练。此外，通过可学习的元令牌培训可以还原部分速度提升，从而诱导质量意识的潜在结构。研究使用探针分析潜在表示，以理解元数据如何塑造学习。
### Conclusion
研究结果提供了在提高LLM预训练效率和效果方面的实用指南。
## 796. `cs.LG` - 关于在干扰条件下基于演化模型的实验 [PDF](https://arxiv.org/pdf/2511.21675), [HTML](https://arxiv.org/abs/2511.21675)
### Authors
Sadegh Shirani,Mohsen Bayati
### Background
网络系统中的因果效应估计对于数据驱动的决策至关重要。在这种环境中，对一个单位的干预可以影响其他单位，但在复杂物理或社会系统中，驱动这些干扰结构的交互路径很大程度上未被观察到。为此，本文探讨了一种基于演化的治疗方法，这种方法研究干预如何随观察轮次影响结果演变，从而弥补缺失的网络信息。
### Innovation
本文提出了基于演化的研究方法，该方法利用治疗方案的平行演变模式来估计反事实轨迹，而不是假设每个单元的平行路径。治疗随机化不仅消除潜在混杂因素，还隐式地采样隐藏 的干扰渠道，从而一致学习异质溢出效应。这种方法适用于密集网络中的因果信息传递，同时扩展到更广泛的干扰结构，包括影响者网络。
### Conclusion
本文讨论了这种方法的局限性，指出强烈的时间趋势或内生干扰可以损害识别。
## 797. `cs.LG` - HoGA: 高阶图注意力通过多样化的k-跳采样 [PDF](https://arxiv.org/pdf/2411.12052), [HTML](https://arxiv.org/abs/2411.12052)
### Authors
Thomas Bailie,Yun Sing Koh,Karthik Mukkavilli
### Background
图在许多实际系统中用于建模潜在变量关系，而消息传递神经网络（MPNNs）广泛用于从图结构中学习这些关系以进行下游任务。尽管基于边的MPNNs能够有效捕获局部交互，但它们的表达力是理论上受限的，限制了发现更高阶关系的能力。
### Innovation
引入了High-Order Graph Attention (HoGA) 模块，该模块通过采样子图来构建k阶注意力矩阵，从而最大化特征向量之间的多样性。与现有的基于高阶关系的贪心重采样方法不同，HoGA 寻求在高阶拓扑中具有多样性的模态，从而减少冗余并扩展捕获子结构的范围。
### Conclusion
在两个单一跳注意力模型上应用HoGA，实现了所有基准节点分类数据集至少5%的准确率提高，并在八个数据集中的六个上优于最近的基线。代码可以在该链接获取：this https URL.
## 798. `cs.LG` - CTSyn: 用于跨表数据生成的基础模型 [PDF](https://arxiv.org/pdf/2406.04619), [HTML](https://arxiv.org/abs/2406.04619)
### Authors
Xiaofeng Lin,Chenheng Xu,Matthew Yang,Guang Cheng
### Background
生成基础模型（GFMs）已经在图像和文本生成高质量合成数据方面取得了显著的成功。然而，将这些模型应用于表格数据时遇到了重大挑战，因为表格特征具有异构性，目前的跨表学习框架因缺乏生成模型主干和有效解码异构特征值的机制而难以应对这些挑战。
### Innovation
提出了跨表合成器（CTSyn），这是一个基于扩散的生成基础模型，专门用于表格数据生成。CTSyn 包含两个关键组成部分：一个自编码器网络，可以将多种类型的表格数据统一到一个潜在空间中，并动态地根据表模式嵌入重构表格值，适应异构数据集；一个条件潜在扩散模型，该模型根据表模式从学习到的潜在空间中生成样本。通过大规模预训练，CTSyn 在标准基准测试中的实用性和服务多样性上均超过了现有的表格合成器。
### Conclusion
CTSyn 在合成表格生成中表现出色，为其成为大规模表格基础模型铺平了道路，为开发大规模基础模型奠定了基础。
## 799. `cs.LG` - 对抗训练在恶意软件分类器中的有效性研究 [PDF](https://arxiv.org/pdf/2412.18218), [HTML](https://arxiv.org/abs/2412.18218)
### Authors
Hamid Bostani,Jacopo Cortellazzi,Daniel Arp,Fabio Pierazzi,Veelasha Moonsamy,Lorenzo Cavallaro
### Background
对抗训练（AT）是应对机器学习诱骗攻击的关键防御手段，但其在真实世界恶意软件检测中的有效性仍然不明确。这种不确定性源于之前研究中的一个重要断层：研究往往忽略了恶意软件的固有特性，呈现出分散化的研究状态，这些研究单独考量了真实度或对抗样本的置信度等变量，或者依赖于弱化的评估方法，而这无法提供广泛应用的洞察。
### Innovation
我们引入了Rubik框架，用于系统化、多维度评估恶意软件领域中的对抗训练。该框架定义了关键因素，涵盖了数据、特征表示、分类器和鲁棒优化设置等多个重要维度，通过可靠的评估实践（如真实的逃逸攻击）全面探讨对抗训练变量间的相互作用。该研究以Android恶意软件为实例，实证分析了这些相互作用如何影响系统的鲁棒性。研究发现挑战了先前的信念，例如表明可实现的对抗样本仅在条件下提供鲁棒性收益，并揭示了模型架构和特征空间结构在对抗训练成功中的关键作用。
### Conclusion
从这一分析中，我们提炼了四项关键见解，揭示了四种常见的评估误解，并提出了实际建议，以指导真正鲁棒的恶意软件分类器的开发。
## 800. `cs.LG` - Odin: Oriented Dual-module Integration for Text-rich Network Representation Learning [PDF](https://arxiv.org/pdf/2511.21416), [HTML](https://arxiv.org/abs/2511.21416)
### Authors
Kaifeng Hong,Yinglong Zhang,Xiaoying Hong,Xuewen Xia,Xing Xu
### Background
现有的方法要么依赖于图神经网络（GNNs），这类模型受限于过度平滑和依赖跳数的扩散；要么使用 Transformer，这种模型忽视了图拓扑结构，将节点视为独立的序列。这两类方法都不能有效结合强大的文本理解和结构性信息推理。
### Innovation
提出了一种新的架构 Odin（Oriented Dual-module INtegration），通过在特定深度将经过定向的双模块注入到 Transformers 中，使 Transformer 充分利用图结构进行信息传播。Odin 不依赖多跳扩散，而是将多跳结构在特定 Transformer 层中整合，从而实现与模型语义层次相一致的低级、中级和高级结构性抽象。Odin 还通过聚合全局 [CLS] 表现出避免过度平滑和解耦结构性抽象与邻域大小或图拓扑的影响。此外，为了在大规模或资源受限的设置下使设计更加高效，还引入了 Light Odin，这是一种更轻量级的变体，保持相同层次的结构性抽象，从而加快训练和推理速度。
### Conclusion
实验表明，Odin 实现了最先进的精度，而 Light Odin 在显著减少计算成本的同时提供竞争力的性能。Odin 和 Light Odin 形成了一个无跳的统一框架，用于有原则的结构文本集成。源代码已发布于此：[链接]。
## 801. `cs.LG` - 进化预测游戏 [PDF](https://arxiv.org/pdf/2503.03401), [HTML](https://arxiv.org/abs/2503.03401)
### Authors
Eden Saig,Nir Rosenfeld
### Background
当预测算法服务于一组用户时，预测质量的不平等开始显现。如果用户对准确预测作出响应，增加参与度、邀请朋友或采纳趋势，那么这种积极反馈会不断循环，影响模型和用户群体。这项研究引入了一种进化预测游戏框架，该框架基于进化博弈论，将这种反馈环视为用户群体间的自然选择过程。
### Innovation
研究提出了进化预测游戏框架，将反馈机制建模为自然选择过程；揭示了理想化与现实中的学习环境之间的差距：在理想化条件下，重复学习促进竞争和排斥；但在实际限制条件下（如有限的数据和计算能力），群体之间的稳定共生和互利共生成为可能；研究了这些可能性的稳定性和可行性，并提出了维持它们存在的机制。
### Conclusion
研究分析了理想化与现实学习环境之间的不同，证明了在有限数据和计算能力等现实限制条件下，依然可以实现群体间的稳定共生；提出了维持这种共生状态的机制，并通过实证方法验证了研究发现。
## 802. `cs.LG` - 高效数据利用及模型性能提升的主动学习方法 [PDF](https://arxiv.org/pdf/2504.16136), [HTML](https://arxiv.org/abs/2504.16136)
### Authors
Chiung-Yi Tseng,Junhao Song,Ziqian Bi,Tianyang Wang,Chia Xin Liang,Xinyuan Song,Ming Liu
### Background
在数据驱动智能时代，数据丰富而标注稀缺的悖论成为机器学习发展中一个关键的瓶颈。本文详细介绍了主动学习（AL），这是一种通过使用更少的已标记示例使模型达到更好性能的机器学习策略。文章概述了AL的基础概念，并讨论了它在计算机视觉、自然语言处理、迁移学习及实际应用中的应用。此外，文章还介绍了AL的重要研究主题，包括不确定性的估计、类不平衡的处理、领域适应、公平性以及构建坚实评估指标和基准的问题。
### Innovation
本文强调采用借鉴人类学习方法和由问题引导的学习策略，能够提高数据效率并使模型学习更加有效。此外，本文还指出了当前领域面临的挑战，包括重建信任、确保可重复性和处理不一致的方法论。研究指出，使用良好的评估指标时，主动学习通常比被动学习效果更好。
### Conclusion
本文旨在为研究人员和实践者提供关键见解，并提出主动学习未来发展的方向，从而促进高效数据利用和模型性能提升。
## 803. `cs.LG` - 增强训练数据归属的表征优化 [PDF](https://arxiv.org/pdf/2505.18513), [HTML](https://arxiv.org/abs/2505.18513)
### Authors
Weiwei Sun,Haokun Liu,Nikhil Kandpal,Colin Raffel,Yiming Yang
### Background
训练数据归属(TDA)方法旨在量化训练数据对模型预测的影响。虽然基于梯度的方法（如影响函数）提供了理论依据，但它们的计算成本使其在大规模应用中不可行。基于表示的方法则更为可扩展，但通常依赖于未优化过归属准确性的启发式嵌入，限制了其精度。
### Innovation
提出了一种名为AirRep的方法，这是一种基于表示且在计算上可扩展的框架，通过学习特定任务和模型对齐的优化表示，解决上述挑战。AirRep引入了两个关键创新点：可训练的编码器调谐以提高归属质量，以及基于注意力的池化机制以实现准确的群体影响估计。
### Conclusion
AirRep在指令调优的大语言模型上的实验表明，它在效率上几乎提高了两个数量级，在推理时间上与最先进的基于梯度的方法性能相当，且具有强大的跨任务和模型的鲁棒性和泛化能力。
## 804. `cs.LG` - TS-RAG：基于检索增强生成的时间序列基础模型是更强的零样本预测模型 [PDF](https://arxiv.org/pdf/2503.07649), [HTML](https://arxiv.org/abs/2503.07649)
### Authors
Kanghui Ning,Zijie Pan,Yu Liu,Yushan Jiang,James Yiming Zhang,Kashif Rasul,Anderson Schneider,Lintao Ma,Yuriy Nevmyvaka,Dongjin Song
### Background
近年来，大型语言模型(LLMs)和基础模型(FMs)在时间序列预测任务中变得流行。尽管微调LLMs可以实现领域适应，它们通常难以普遍适用于多样性和陌生的数据集。此外，现有的时间序列基础模型(TSFMs)在处理非平稳动态和分布偏移方面仍面临挑战，这主要是由于缺乏有效的适应机制。基于此，本文提出了TS-RAG框架，这是一种检索增强生成的时间序列预测方法，旨在提高TSFMs的泛化能力和可解释性。
### Innovation
TS-RAG框架利用预训练的时间序列编码器从专用知识库中检索语义相关段落，从而丰富输入查询的上下文表示。此外，本文提出了一种自适应检索混频(ARM)模块，该模块可以动态地将检索到的模式与TSFM的内部表示进行融合，从而提高预测准确性，而无需特定任务的微调。实验结果表明，TS-RAG在七个公共基准数据集上实现了最先进的零样本预测性能，与现有TSFMs相比，在多种领域上的性能提高了6.84%，且提供了可解释性。
### Conclusion
总的来说，TS-RAG框架有效地提高了时间序列基础模型的零样本预测性能和可解释性。实验结果表明，该框架在多个公开数据集上的表现优于现有方法，并提供了满足预测需求的可解释性。
## 805. `cs.LG` - 不对称搭档：副手提升不确定性 [PDF](https://arxiv.org/pdf/2505.18636), [HTML](https://arxiv.org/abs/2505.18636)
### Authors
Tim G. Zhou,Evan Shelhamer,Geoff Pleiss
### Background
在决策受不确定性影响的环境下，深度网络的传统方法是通过多次训练运行结合随机初始化，但这种方法对于大规模模型和当前的实际微调工作流程来说并不适用。本文探讨了对于大型模型（例如微调的ViT-B）来说，结合一个比主模型更不准确但计算量小得多的“副手”模型（例如微调的ResNet-34）的有效性。
### Innovation
提出了一个低成本的新策略来改进大型模型的不确定性量化和下游决策：将主模型与一个更不准确但计算成本低得多的副手模型结合，通过简单的学习加权平均来聚合这两个模型的预测。这一策略在五个图像分类基准、多种模型架构和训练方案中，实现了显著的准确度、不确定性量化和选择分类指标的提升。
### Conclusion
不对称搭档在不到20%的额外计算成本下显著提升了模型性能和不确定性量化，而不会损害大型模型的表现。
## 806. `cs.LG` - 使用约束学习对大型语言模型进行对齐 [PDF](https://arxiv.org/pdf/2505.19387), [HTML](https://arxiv.org/abs/2505.19387)
### Authors
Botong Zhang,Shuo Li,Ignacio Hounie,Osbert Bastani,Dongsheng Ding,Alejandro Ribeiro
### Background
在受约束的对齐问题中，目标是在满足次要效用约束的同时最大化主要奖励目标。尽管基于拉格朗日的大型语言模型（LLM）策略搜索方法很受欢迎，但迭代的 primal-dual 方法往往无法收敛，而非迭代的基于对偶的方法在 LLM 参数空间中无法达到最优。
### Innovation
本文采用拉格朗日对偶性开发了一种迭代的基于对偶的对齐方法，交替地通过拉格朗日最大化更新LLM策略和通过对偶下降更新对偶变量。理论分析了分布空间和LLM参数空间中的原始问题和对偶问题之间的原始-对偶差距。还量化了在近乎最优的对偶变量下所学习的LLM策略在目标函数和约束函数中的最优性差距，证明了基于对偶的对齐方法可以在LLM参数化差距内找到最优的受约束LLM策略。
### Conclusion
通过在PKU-SafeRLHF和Anthropic HH-RLHF数据集上进行大量实验展示了本文方法的有效性以及优势。
## 807. `cs.LG` - 具备 tight 风险证书的深.actor-评论算法 [PDF](https://arxiv.org/pdf/2505.19682), [HTML](https://arxiv.org/abs/2505.19682)
### Authors
Bahareh Tasdighi,Manuel Haussmann,Yi-Shan Wu,Andres R. Masegosa,Melih Kandemir
### Background
深度演员评论算法已经达到了能够影响日常生活的技术水平。它们推动了大型语言模型的持续改进，通过用户反馈。然而，这些算法在物理系统中的部署尚未广泛采用，主要原因是没有一种验证方案能够完全量化它们因故障导致的风险。
### Innovation
本文证明了可以为深度演员评论算法开发出精确的风险证书。关键在于最小评估数据的有效性。通过从预训练策略中收集可行的评估展开样本组合一个简化的 PAC-Bayes 理论，可以产生准确的风险证书。具体来说，使用最近引入的递归 PAC-Bayes 方法，在每次分割验证数据并递归构建 PAC-Bayes 边界时，利用上一部分预测器作为数据导向的先验。
### Conclusion
我们在多种移动任务、演员评论方法和策略熟练程度下进行了实验证明，这些风险证书足够精确，可以考虑实际应用。
## 808. `cs.LG` - 使用进化算法在推理时对扩散模型进行对齐 [PDF](https://arxiv.org/pdf/2506.00299), [HTML](https://arxiv.org/abs/2506.00299)
### Authors
Purvish Jajal,Nick John Eliopoulos,Benjamin Shiue-Hal Chou,George K. Thiruvathukal,James C. Davis,Yung-Hsiang Lu
### Background
扩散模型是当前最先进的生成模型，但它们生成的样本往往无法满足应用目标，如安全约束或特定领域的有效性。现有对齐技术需要梯度、模型内部访问或大量计算预算，这导致了高计算需求，或者无法支持某些目标。
### Innovation
本文提出了一种基于进化算法的推理时对齐框架，将扩散模型视为黑盒，并在其潜在空间中搜索以最大化对齐目标。与无梯度和基于梯度的方法相比，我们的方法在相同的或更少的运行时间内，图像奖励分数提高了3%-35%。在Open Image Preferences数据集上，我们的方法在四个流行的对齐目标上实现了竞争性结果。在计算效率方面，我们的方法比基于梯度的方法需要55%-76%少的GPU内存，并且快72%-80%。
### Conclusion
该工作展示了基于进化算法的对扩散模型的推理时对齐框架的有效性，提升了在目标对象上的性能，并在计算资源使用上更为高效。
## 809. `cs.LG` - 通过卷积Fenchel-Young损失建立凸光滑损失的一致代理遗憾边界 [PDF](https://arxiv.org/pdf/2505.09432), [HTML](https://arxiv.org/abs/2505.09432)
### Authors
Yuzhou Cao,Han Bao,Lei Feng,Bo An
### Background
代理遗憾边界或过差点界可以消除代理损失和目标损失之间的收敛速度差异。凸光滑的代理损失因其高效估计和优化而受到青睐，但在遗憾传递过程中，损失光滑性与线性代理遗憾边界之间的权衡一直存在于社区中，导致代理损失的优化和估计特性在遗憾传递到目标损失后可能会减弱。
### Innovation
本文通过采用卷积Fenchel-Young损失建立了一个新的凸光滑代理损失，该损失具有可定制的预测链接，能够保持线性代理遗憾边界的同时保持光滑损失的平滑性。此外，通过infimal卷积，该研究提出了一个一致估计基概率的方法。这一研究成果展示了凸分析如何渗透到风险最小化中的优化和统计效率。
### Conclusion
研究通过一种新颖的方法，解决了凸光滑代理损失在遗憾传递过程中优化和估计性能下降的问题，为保持代理遗憾边界线性的同时保持损失的光滑性提供了新的途径。
## 810. `cs.LG` - 在组合任务结构中表征模式匹配及其局限性 [PDF](https://arxiv.org/pdf/2505.20278), [HTML](https://arxiv.org/abs/2505.20278)
### Authors
Hoyeon Chang,Jinho Park,Hanseul Cho,Sohee Yang,Miyoung Ko,Hyeonbin Hwang,Seungpil Won,Dohaeng Lee,Youbin Ahn,Minjoon Seo
### Background
尽管语言大模型展现了强大的能力，但它们的成功往往依赖于模式匹配的行为，这在偏领域外（OOD）的组合任务中容易导致泛化能力的失败。常见任务设计往往允许多种泛化来源（例如代数不变性、结构重复），从而掩盖了模型通过模式匹配进行泛化的精确和可测试的表征，以及其局限性。
### Innovation
本文首次将模式匹配形式化为功能等价性，即识别在保持输入其余部分不变的情况下始终产生相同结果的输入子序列配对。通过这种形式化，本文系统地研究了只解码器Transformer和Mamba在隔离这种机制的控制组合结构任务中的行为。研究结果揭示了模式匹配的预测性和定量性洞察：（1）模式匹配的实例成功率可以通过见证相关功能等价性的上下文数量很好地预测。（2）研究证明了通过确定数据缩放定律的指数来学习两步结构以完全内部领域泛化所需的紧样本复杂性限制。（3）路径模糊性是一个结构性障碍：当一个变量通过多个路径影响输出时，模型无法形成统一的中间状态表示，这影响准确性和可解释性。（4）Chain-of-Thought虽然减少了数据需求，但并不能解决路径模糊性。
### Conclusion
本文提供了模式匹配的预测性和可验证边界，并为混杂泛化机制的分离提供了一个基础诊断。
## 811. `cs.LG` - 使用探查的公平算法在多代理多臂老虎机中的应用 [PDF](https://arxiv.org/pdf/2506.14988), [HTML](https://arxiv.org/abs/2506.14988)
### Authors
Tianyi Xu,Jiaxin Liu,Nicholas Mattei,Zizhan Zheng
### Background
本文研究了一个旨在通过多代理多臂老虎机（MA-MAB）框架，在确保各代理公平结果的同时，最大化系统整体性能的问题。在决策时面对有限的臂奖励信息，这是一个关键挑战。为此，提出了一种新颖的探查框架，在分配之前有选择性地收集关于某些臂的信息。在线下场景中，已知奖励分布，利用子模性设计了具有可证明性能边界的贪婪探查算法。在线上复杂场景下，开发了一种算法，可以实现亚线性遗憾损失，同时保持公平性。
### Innovation
提出了一个多代理多臂老虎机（MA-MAB）框架，通过战略性地搜集信息来获取更具优势的结果。设计了两种算法：在已知奖励分布的离线场景中，利用子模性设计了贪婪探查算法，具有可证明的性能保证；在未知奖励分布的复杂场景下，开发了一种能够实现亚线性遗憾损失的公平算法。
### Conclusion
针对合成和真实数据集的大量实验表明，该方法在公平性和效率方面显著优于基线方法。
## 812. `cs.LG` - 深不确定性和容量风险意识下的深度强化学习双源库存管理 [PDF](https://arxiv.org/pdf/2507.14446), [HTML](https://arxiv.org/abs/2507.14446)
### Authors
Defeng Liu,Ying Liu,Carson Eisenach
### Background
本文研究了如何通过利用介入模型高效地将强化学习（RL）应用到大规模随机优化问题中。特别是在供应链优化的多来源多期库存管理问题上，通过预训练的深度学习（DL）模型模拟和组合随机过程，更好地探索解决方案空间。
### Innovation
所提出的方法的关键是通过使用预训练的深度学习模型模拟和组合随机过程，更好地探索解决方案空间。此外，引入了一种约束协调机制，用于预测库存网络中的跨产品约束下的双重成本。本文的方法将复杂的供应链过程拆分为可扩展且可组合的DL模块，从而在大规模实时数据集上取得了更好的性能。
### Conclusion
本文还指出了未来研究中的开放问题，以进一步探讨此类模型的有效性。
## 813. `cs.LG` - F-INR: 功能性张量分解用于隐式神经表示 [PDF](https://arxiv.org/pdf/2503.21507), [HTML](https://arxiv.org/abs/2503.21507)
### Authors
Sai Karthikeya Vemuri,Tim Büchner,Joachim Denzler
### Background
隐式神经表示（INRs）模型将信号表示为连续可微的功能。然而，整体的INRs对于高维度数据扩展性较差，导致训练成本过高。为此，本文提出了F-INR框架，通过基于功能性张量分解将高维度INR分解为一组紧凑、轴向特定的子网络。这些子网络学习低维度功能组件，然后通过张量操作进行组合。这种分解减少了计算复杂度，同时提升了表示能力。
### Innovation
F-INR框架进行了架构中立和分解中立的设计，可以与多种现存的INR主干（如SIREN、WIRE、FINER、Factor Fields）和张量格式（如CP、TT、Tucker）相结合。它提供了一个通过张量秩和模式对速度与准确度进行精细控制的选择，从而加速训练高达20倍，并提高了PSNR超过6.0 dB。F-INR已经在图像表示、3D几何重建和神经辐射场等多种任务上进行了验证，并展示了其在科学计算中的应用，例如模拟复杂物理仿真。
### Conclusion
F-INR提供了用于高维信号建模的可扩展、灵活和高效的框架。
## 814. `cs.LG` - 流匹配遇见偏微分方程：一种基于物理约束的统一生成框架 [PDF](https://arxiv.org/pdf/2506.08604), [HTML](https://arxiv.org/abs/2506.08604)
### Authors
Giacomo Baldan,Qiang Liu,Alberto Guardone,Nils Thuerey
### Background
生成学习方法如扩散模型和流动匹配在模拟复杂系统行为和构建高效代理模型方面显示出巨大潜力。然而，这些方法通常从数据中隐式学习潜在的物理规律。为了改进这一过程，本文提出了一个新方法，称为基于物理的流动匹配（PBFM），该方法在流动匹配目标中显式嵌入了物理约束，包括偏微分方程残差和代数关系。此外，随着时间训练时的延展推理提高了最终无噪声样本预测的准确性。
### Innovation
提出了基于物理的流动匹配（PBFM）框架，该框架在流动匹配目标中显式嵌入了物理约束条件，包括偏微分方程的残差和代数关系。该方法还引入了训练时的时间延展推理，以提高最终未受噪声干扰的样本预测准确性。此外，PBFM 不需要调整超参数即可同时最小化流动匹配损失和基于物理的残差损失，并通过一种随机采样策略减少物理残差。
### Conclusion
通过在三个代表性的偏微分方程问题上的广泛基准测试，展示了该方法能够将物理残差显著减少至流动匹配（FM）的 8 倍，同时在分布准确性方面显著超越现有算法。PBFM 提供了一个有原则且有效的代理建模、不确定性量化和物理工程加速模拟框架。
## 815. `cs.LG` - 物理约束流匹配：具有硬约束的生成模型采样 [PDF](https://arxiv.org/pdf/2506.04171), [HTML](https://arxiv.org/abs/2506.04171)
### Authors
Utkarsh Utkarsh,Pengfei Cai,Alan Edelman,Rafael Gomez-Bombarelli,Christopher Vincent Rackauckas
### Background
近年来，深度生成模型被应用于由偏微分方程（PDEs）支配的物理系统中，提供了可扩展的模拟和不确定性感知的推理。然而，如何在这些模型中严格实现物理约束，例如守恒定律（线性和非线性）和其他物理一致性，仍然是一个挑战。现有方法通常依赖于软惩罚或架构偏见，这些方法无法保证约束的有效性。
### Innovation
本文提出了一种名为物理约束流匹配（PCFM，Physics-Constrained Flow Matching）的新框架，它可以在预训练的流生成模型中强制执行任意非线性约束。PCFM通过在中间解状态应用基于物理的修正连续指导采样过程，同时保持与学习到的流一致并满足物理约束。实验结果表明，PCFM在各种PDEs中表现优于无约束和有约束的基线方法，包括那些具有冲击波、不连续性和尖锐特征的PDEs，并且最终解满足精确约束。
### Conclusion
我们的方法提供了一个灵活的框架，用于在科学和通用生成模型中强制执行硬约束，尤其是在约束满足至关重要的应用中。
## 816. `cs.LG` - AutoDiscovery：通过贝叶斯惊讶实现开放性科学发现 [PDF](https://arxiv.org/pdf/2507.00310), [HTML](https://arxiv.org/abs/2507.00310)
### Authors
Dhruv Agarwal,Bodhisattwa Prasad Majumder,Reece Adamson,Megha Chakravorty,Satvika Reddy Gavireddy,Aditya Parashar,Harshit Surana,Bhavana Dalvi Mishra,Andrew McCallum,Ashish Sabharwal,Peter Clark
### Background
自主科学发现（ASD）不仅依赖于回答问题，还涉及到知道应该问哪些问题。目前，大多数ASD的研究集中在使用大型语言模型（LLMs）进行目标驱动的应用中，依赖于人类事先规定的研究问题来指导假设生成。然而，通过让AI系统根据自身标准驱动探索，可能会加速科学发现。尽管存在一些采用多样性启发式或主观有趣性代理的开放性ASD方法，但这些方法在处理广泛假设空间时存在局限性和准确性问题。本研究提出了AutoDiscovery——一种利用贝叶斯惊讶驱动开放性科学探索的方法。
### Innovation
本研究创新地提出了AutoDiscovery方法，通过贝叶斯方法量化LLM在获取实验结果后，关于假设的先验信念和后验信念的理论转变。该方法利用蒙特卡洛树搜索（MCTS）策略，采用惊异度作为奖励函数，并结合逐步扩展技术，高效探索嵌套假设空间。研究者通过21个真实数据集（涵盖生物学、经济学、金融和行为科学等领域）在数据驱动发现的场景下评估了AutoDiscovery，结果显示相较于竞争对手，AutoDiscovery在固定预算下能产生多5-29%的惊异发现，且近三分之二的发现让领域专家也感到惊讶。
### Conclusion
本研究证明了AutoDiscovery在固定预算下显著优于竞争对手的能力，并通过两例发现领域的专家评估，进一步证实了通过贝叶斯惊讶驱动开放性科学探索的有效性。这标志着构建开放性ASD系统的重要一步。
## 817. `cs.LG` - ENMA: 预序自回归生成神经偏微分算子 [PDF](https://arxiv.org/pdf/2506.06158), [HTML](https://arxiv.org/abs/2506.06158)
### Authors
Armand Kassaï Koupaï,Lise Le Boudec,Louis Serrano,Patrick Gallinari
### Background
解决具有时间依赖性和参数化的偏微分方程（PDEs）是一个基本挑战，特别是在泛化到广泛的物理参数和动态过程中。当数据存在不确定性或不完整时，自然的方法是采用生成模型。ENMA作为一种生成神经算子，旨在建模来自物理现象的空间-时间动态。
### Innovation
ENMA采用一种生成式自回归变压器（在压缩的潜在空间中预测未来的动态），通过流动匹配损失进行训练，实现按令牌生成。通过注意机制和时空卷积编码器将不规则采样的空间观测编码为统一的潜在表示并进一步压缩，允许ENMA在推理时进行上下文学习，根据目标轨迹的过去状态或动态相似的辅助上下文轨迹进行条件化。
### Conclusion
ENMA提供了一个强大且适应性强的框架，能够泛化到新的PDE领域，并支持一次完成替代建模时间依赖性参数化的PDE。
## 818. `cs.LG` - 使用LLM代理赋能时间序列预测 [PDF](https://arxiv.org/pdf/2508.04231), [HTML](https://arxiv.org/abs/2508.04231)
### Authors
Chin-Chia Michael Yeh,Vivian Lai,Uday Singh Saini,Xiran Fan,Yujie Fan,Junpeng Wang,Xin Dai,Yan Zheng
### Background
大型语言模型（LLM）驱动的代理已经成为了自动化机器学习（AutoML）系统的有效规划器。大多数现有的AutoML方法主要致力于自动化特征工程和模型架构搜索，但最近有关时间序列预测的研究表明，轻量级模型在许多情况下可以达到最先进的性能。基于这一观察，作者探索了通过提高数据质量而不是模型架构来改进AutoML的方法，特别是在时间序列数据上。
### Innovation
本文提出了Data-Centric Agent for Time Series（DCATS），一种利用伴随时间序列的元数据来清理数据并优化预测性能的代理方法。通过在大规模交通流量预测数据集上使用四个时间序列预测模型进行了评估，结果显示DCATS在所有测试模型和预测时长中平均实现了6%的误差减少，这突显了数据重心方法在时间序列预测AutoML中的潜力。
### Conclusion
数据重心方法在时间序列预测AutoML中具有巨大潜力。通过使用伴随时间序列的元数据来提高数据质量，DCATS在四个时间序列预测模型中实现了平均6%的误差减少，展示了这种方法的有效性。
## 819. `cs.LG` - 利用深度生成学习的条件分布等价性检验框架 [PDF](https://arxiv.org/pdf/2509.17729), [HTML](https://arxiv.org/abs/2509.17729)
### Authors
Siming Zheng,Tong Wang,Meifang Lan,Yuanyuan Lin
### Background
该论文探讨了在因果发现和变分条件最相关的情境下的两样本问题中检验条件分布等价性的一般框架。现有的方法通常难以处理此类问题，特别是在处理协变量偏移时。框架基于基于神经网络的生成方法和采样分割技术，将条件测试问题转化为无条件问题。
### Innovation
论文提出了一种利用生成分类准确率构建条件分布等价性测试的方法（GCA-CDET），该方法通过将条件测试问题转化为无条件问题来进行。研究通过新的结果，即最近发展起来的偏移Rademacher复杂性，推导了所学习生成器的收敛速率，并证明了GCA-CDET在适度条件下的一致性。
### Conclusion
通过数值研究，包括合成数据集和两个实际数据集，表明了该方法的有效性。在线补充材料中进一步讨论了提出的框架的最优性。
## 820. `cs.LG` - 对称保群匹配流方法 [PDF](https://arxiv.org/pdf/2509.03340), [HTML](https://arxiv.org/abs/2509.03340)
### Authors
Fleur Hendriks,Ondřej Rokoš,Martin Doškář,Marc G.D. Geers,Vlado Menkovski
### Background
在非线性动力系统中，分岔现象常常导致多种共存的稳定解，尤其是在对称性破坏的存在下。确定性的机器学习模型在捕捉这种多重性方面存在困难，它们倾向于平均多个解，导致无法正确表示对称性较低的解。本文讨论了如何利用对称保持的生成框架来准确建模分岔结果的整个概率分布。
### Innovation
本文提出了一种基于流匹配的生成框架，能够在保持系统对称性的同时直接采样多种有效解。引入了一种对称匹配策略，使得预测输出和目标输出在群作用下对齐，这样可以在对称保模型中实现精确学习。该方法被应用于各种系统中，包括简单的玩具模型和复杂的物理问题，如弯曲梁和艾伦-詹方程。
### Conclusion
实验结果表明，流匹配方法显著优于非概率方法和变分方法，它在捕捉多模态分布和对称性破坏的分岔方面表现更优，为高维系统中的多稳态建模提供了一种规范且可扩展的解决方案。
## 821. `cs.LG` - 统一噪声曲率视角下的训练可微分性丧失问题 [PDF](https://arxiv.org/pdf/2509.19698), [HTML](https://arxiv.org/abs/2509.19698)
### Authors
Gunbir Singh Baveja,Alex Lewandowski,Mark Schmidt
### Background
训练可微分性丧失是指在连续学习中的一种现象，即参数更新不再对优化目标产生进展，导致在学习问题随时间发生变化时，精度停滞或下降。现有指标，如海森矩阵秩、尖锐度等级、权重或梯度范数、梯度-参数比和单元标记熵，都不能可靠地预测这一现象。
### Innovation
本文从优化角度分析了训练可微分性丧失的问题，引入了两个互补指标：基于批量大小的梯度噪声界和曲率波动控制界，提出了一种基于层的自适应噪声阈值来预测训练可微分性行为的方法，进而设计了一种步长调度器，防止训练可微分性丧失，从而提高了以前方法如CReLU、Wasserstein正则化和L2权重衰减保持的准确率。此外，该调度器自适应调整步长轨迹，且无需调参。
### Conclusion
实验表明，本文提出的调度器可以提高沿用方法的准确率，特别是一些不需要手动调参的自适应步长轨迹，它能自动生成类似于手动设计的步长衰减调度规则。
## 822. `cs.LG` - 行动切片和探索性数据收集在连续控制中的行为克隆中提供指数级改进 [PDF](https://arxiv.org/pdf/2507.09061), [HTML](https://arxiv.org/abs/2507.09061)
### Authors
Thomas T. Zhang,Daniel Pfrommer,Chaoyi Pan,Nikolai Matni,Max Simchowitz
### Background
在这篇论文中，作者分析了现代机器人学习和连续控制中最具影响力的两种干预措施：行动切片（预测开放环中的动作序列）和专家演示的探索性增强。尽管最近的研究表明，模仿学习（IL）在连续场景中可能会遭受指数级累积的错误，但研究发现行动切片和探索性数据收集可以在某些情况下规避这些累积错误。
### Innovation
论文指出，控制理论稳定性是这些干预措施带来益处的关键机制。在实验方面，作者通过在流行机器人学习基准测试上的实验验证了预测和控制理论稳定性的角色。在理论方面，作者证明从控制理论的角度来看，这种方法提供了对累积错误如何产生更精细的洞察，这比仅基于信息理论考虑的方法能够提供更紧的统计保证。
### Conclusion
研究结果显示，行动切片和探索性数据收集在连续控制中的行为克隆中提供了指数级的改进，这是通过控制理论稳定性机制实现的。这种方法不仅提供了对原因的详细解释，还能够提供比之前信息理论考虑方法更紧的统计保证。
## 823. `cs.LG` - 用于血脑屏障渗透性预测的几何多色消息传递图神经网络 [PDF](https://arxiv.org/pdf/2507.18926), [HTML](https://arxiv.org/abs/2507.18926)
### Authors
Trung Nguyen,Md Masud Rana,Farjana Tasnim Mukta,Chang-Guo Zhan,Duc Duy Nguyen
### Background
准确预测血脑屏障渗透性（BBBP）对于中枢神经系统（CNS）药物开发至关重要。尽管图神经网络（GNNs）在分子性质预测方面取得了进展，但它们通常依赖分子拓扑结构而忽视了构建运输机制所需的关键三维几何信息。
### Innovation
本论文提出了一种新颖的几何多色消息传递图神经网络（GMC-MPNN），该框架通过明确整合原子级几何特征和长程相互作用来增强标准消息传递架构。该模型基于原子类型构建加权着色子图，以捕捉BBB渗透性控制的空间关系和化学上下文。论文在三个基准数据集上对GMC-MPNN进行分类和回归任务评估，使用严格的骨架基部划分以确保对泛化的稳健评估。研究表明GMC-MPNN在分类化合物为可渗透/不可渗透（AUC-ROC为0.9704和0.9685）以及回归连续渗透值（RMSE为0.4609，皮尔逊相关系数为0.7759）方面均优于现有最先进的模型。
### Conclusion
通过将空间几何整合到图表示中，GMC-MPNN设定了新的性能基准，并提供了一个更准确和泛化的药物发现工具。此外，消融研究进一步量化了特定原子对相互作用的影响，揭示了模型预测能力源自其能够从常见的和罕见的但化学重要的功能模式中学习的能力。
## 824. `cs.LG` - CRPS-LAM：通过匹配边缘概率实现区域集合天气预报 [PDF](https://arxiv.org/pdf/2510.09484), [HTML](https://arxiv.org/abs/2510.09484)
### Authors
Erik Larsson,Joel Oskarsson,Tomas Landelius,Fredrik Lindsten
### Background
机器学习在天气预报中越来越多地依赖于集合方法提供概率性预报。扩散型模型在区域近似模拟（LAM）中表现出色，但在采样时仍较为费时。基于连续排名概率分数（CRPS）训练全球天气预报模型，已经在一定程度上取得了成功。然而，在区域尺度上的模型训练和使用仍面临挑战。
### Innovation
本文提出了CRPS-LAM模型，这是一种基于CRPS目标进行训练的随机LAM预报模型。通过将单一潜在噪声向量注入模型中进行采样和注入，CRPS-LAM可以在一个前向传播过程中生成全部集合成员，比扩散型模型快39倍。此外，该方法能够保留小尺度天气预报细节，从而作为一种有效的方法应用于区域尺度概率天气预报。
### Conclusion
CRPS-LAM模型在MEPS地区的数据集上进行评估，结果表明CRPS-LAM能够匹敌扩散模型的低误差，且还能够保留小尺度的预报细节。这种方法为区域概率天气预报提供了一个有效的方法选择。
## 825. `cs.LG` - Stackelberg均场博弈中的学习：一种非渐近分析 [PDF](https://arxiv.org/pdf/2509.15392), [HTML](https://arxiv.org/abs/2509.15392)
### Authors
Sihan Zeng,Benjamin Patrick Evans,Sujay Bhatt,Leo Ardon,Sumitra Ganesh,Alec Koppel
### Background
本文研究Stackelberg均场博弈（Stackelberg MFGs）中的策略优化问题，这是一种建模单一领导者与无限数量同类型追随者间战略交互的层级框架。现有的方法往往依赖于领导者和追随者目标之间严格的独立性假设，算法结构导致样本利用效率低下，并且缺乏有限时间收敛保证。
### Innovation
本文提出了AC-SMFG，这是一种单循环的actor-critic算法，在连续生成的马尔可夫样本上操作。该算法交替进行领导者、代表性追随者和均场的（半）梯度更新，简化了实现过程。同时，作者证明了该算法在有限时间和样本数量下收敛到Stackelberg目标的稳定点。这是首个具有非渐近收敛保证的Stackelberg均场博弈算法。
### Conclusion
仿真结果显示，在多种成熟的经济学环境中，AC-SMFG在策略质量和收敛速度上优于现有的多智能体和均场博弈学习基准。
## 826. `cs.LG` - In-context学习中任务导向信息去除的机制 [PDF](https://arxiv.org/pdf/2509.21012), [HTML](https://arxiv.org/abs/2509.21012)
### Authors
Hakaze Cho,Haolin Yang,Gouki Minegishi,Naoya Inoue
### Background
In-context Learning (ICL) 是基于现代语言模型（LMs）的一种新兴的少样本学习方法，但其内部机制仍然不清楚。本文通过一种信息去除的新型视角对其机制进行了研究。
### Innovation
文章通过信息去除的视角，揭示了LMs在零样本场景下的工作机制。具体来说，当输入查询时，LMs会在隐藏状态中编码所有可能任务的信息，导致生成与意图任务无关的输出。文章发现通过低秩滤波器从隐藏状态中选择性和去除特定信息可以引导LMs朝向意图任务。利用这一发现，文章通过设计的指标测量隐藏状态，观察到少样本ICL通过去除冗余信息来模拟任务导向的信息去除过程，从而改善输出，发现这一过程构成了ICL的基础机制。此外，文章还识别出执行去除操作的关键注意力头，称为去噪头，这些头使去除操作可以被消除，从而验证了信息去除机制的重要性。
### Conclusion
研究表明，ICL的关键机制在于任务导向的信息去除过程，能够有效改善输出。去除操作的重要部分是由被称为去噪头的关键注意力头执行的。去除操作的缺失会显著降低ICL的准确性，特别是在缺少正确标签的情况下。这意味着信息去除机制和去噪头对ICL的性能至关重要。
## 827. `cs.LG` - 深度神经网络中的类别学习：内部表示的信息内容和几何结构 [PDF](https://arxiv.org/pdf/2510.19021), [HTML](https://arxiv.org/abs/2510.19021)
### Authors
Laurent Bonnasse-Gahot,Jean-Pierre Nadal
### Background
在人类和其他动物中，类别学习会增强对类别边缘附近刺激的区分能力，这种现象称为类别表达。此前通过神经科学数据进行的建模研究表明，这种类别边界附近的扩展/压缩是高效学习的必然结果。本研究进一步将此理论框架扩展至人工神经网络，探讨最小化贝叶斯成本（交叉熵损失的均值）如何等价于最大化类别集合与决策层前神经活动的互信息。
### Innovation
研究发现，最大互信息意味着找到合适的投影空间，并构建具有适当度量的神经表示，这一度量基于Fisher信息矩阵来测量神经活性对投影空间变化的敏感性。该研究揭示了类别学习诱导神经空间在决策边界附近的扩展，并进一步证明了Fisher信息的最大特征向量在每个投影空间点给出最具区分性的方向。研究还表明，在两个示例模型和MNIST数据集中，学习后类别的Fisher信息矩阵与类别边界基本对齐。
### Conclusion
研究将Fisher信息矩阵的内容和几何结构解释为类别学习的结果，并揭示了ATEI（类别特定的Fisher信息）的概念，最终将研究结果与信息瓶颈方法联系起来，展示出Bayes成本的偏差-方差分解，这对自己的研究具有重要意义。
## 828. `cs.LG` - 分布迁移下的弱到强泛化 [PDF](https://arxiv.org/pdf/2510.21332), [HTML](https://arxiv.org/abs/2510.21332)
### Authors
Myeongho Jeon,Jan Sobotka,Suhwan Choi,Maria Brbić
### Background
未来超人模型将变得越来越复杂，人类可能无法准确监督它们的行为。已有研究表明，在此类情况下，较弱的模型可以有效监督较强的模型，这是弱到强泛化的现象，但在分布迁移下，这种现象往往会导致强模型的表现不如其弱监督者。
### Innovation
本文提出了RAVEN（Resilient Weak-to-Strong Generalization Framework），一个能够动态学习强模型和弱模型最优组合的鲁棒弱到强泛化框架。该框架在图像分类、文本分类和偏好对齐任务中展示了其有效性，相对于其他基线方法，在分布外任务上表现出超过30%的优势，而在分布内任务上则达到或超过了现有方法。
### Conclusion
RAVEN能够自动分配更高的权重给更准确的弱模型，证明了其自动识别可靠监督的能力。
## 829. `cs.LG` - QiMeng-SALV: Signal-Aware Learning for Verilog Code Generation [PDF](https://arxiv.org/pdf/2510.19296), [HTML](https://arxiv.org/abs/2510.19296)
### Authors
Yang Zhang,Rui Zhang,Jiaming Guo,Lei Huang,Di Huang,Yunpu Zhao,Shuyao Cheng,Pengwei Jin,Chongxiao Li,Zidong Du,Xing Hu,Qi Guo,Yunji Chen
### Background
大型语言模型（LLMs）的显著进步为Verilog代码生成提供了有希望的机会，这在自动电路设计中非常重要。缺乏有意义的功能奖励阻碍了基于强化学习（RL）的功能正确Verilog代码的优化。
### Innovation
提出了一个名为QiMeng-SALV的信号感知学习方法，通过利用功能正确输出信号的代码片段来优化RL训练。QiMeng-SALV的关键洞察是，通过部分错误模块中的验证信号感知实现来增强有意义的功能奖励的提取。该方法通过比较生成模块和参考模块训练数据中的信号功能正确性来验证信号功能正确性，然后使用抽象语法树（AST）识别错误模块中的信号感知代码片段，最后通过优化正确的信号级别代码片段来引入信号感知DPO，从而防止来自错误信号的噪声和干扰。
### Conclusion
实验表明，我们的方法在VerilogEval和RTLLM上达到了最先进的性能，7B参数模型的性能与DeepSeek v3 671B模型相当，显著优于同一数据集上训练的领先开源模型CodeV。我们的代码可在以下链接访问：this https URL。
## 830. `cs.LG` - Transformer模型中逆排列学习的不可能性 [PDF](https://arxiv.org/pdf/2509.24125), [HTML](https://arxiv.org/abs/2509.24125)
### Authors
Rohan Alur,Chris Hays,Manish Raghavan,Devavrat Shah
### Background
本文探讨了解码器为主的变换器（decoder-only transformers）在面对逆排列学习任务时的背景和挑战。逆排列学习的任务是给定一个排列和该排列应用于其中的字符串，模型需输出该字符串的原始（“标准”）形式。作者认为该任务可以作为各种推理任务（如长上下文检索、多项选择问答和上下文学习）中自然鲁棒性的模型。
### Innovation
本文的主要贡献在于证明了任意深度的解码器为主的变换器无法完成逆排列学习任务。此成果关注解码器为主的变换器模型的表达能力，并且与训练动态或样本复杂度无关。此外，作者提出了两种不同的构造方法，可以实现逆排列学习，其中之一强调了因果注意力掩码的基础作用，揭示了编码器解码器结构与受欢迎的解码器独立试验架构在表达能力上的差距。
### Conclusion
研究表明，在解码器为主的变换器模型中无法执行逆排列学习任务。然而，通过在输入中添加“草稿标记”等简单方法，可以实现逆排列学习。这可能暗示着链式思考提示或其他介于思考的标记能够在大型语言模型中促进推理，即使这些标记不携带有意义的语义信息。
## 831. `cs.LG` - ConStellaration: 一种类似QI的等离子边界数据集和优化基准问题 [PDF](https://arxiv.org/pdf/2506.19583), [HTML](https://arxiv.org/abs/2506.19583)
### Authors
Santiago A. Cadena,Andrea Merlo,Emanuel Laude,Alexander Bauer,Atul Agrawal,Maria Pascu,Marija Savtchouk,Enrico Guiraud,Lukas Bonauer,Stuart Hudson,Markus Kaiser
### Background
稳态核聚变设备研究中的磁约束装置（如托卡马克）正在积极开发，旨在提供碳排放少的清洁能源。这些装置的设计涉及高维约束优化问题，需要昂贵的物理模拟和深厚的领域专业知识。托卡马克优化已取得进展，但社区的进一步发展受限于缺乏标准化优化问题、基准数据集以及能够促进数据驱动方法的托卡马克配置数据。特别是在“次等度”（Quasi-isodynamic, QI）托卡马克配置中，这种系统被认为有可能实现商业核聚变，因其对由电流引起的中断具有内在的抵抗力。”这些配置涉及理想磁流体力学（ideal MHD）平衡和性能指标。”研究人员通过多样化的QI磁位样本和最优优化托卡马克等离子边界生成了数据集，提出了三个复杂性逐步增加的优化基准，并展示了基于该数据集训练的模型如何高效生成新型可行配置，无需查询昂贵的物理模拟。”这些基准问题和强基线旨在降低优化和机器学习研究人员参与托卡马克设计的门槛，并加速跨学科进展，使其核聚变能源能够更好地融入电网。
### Innovation
公开了一个由具有理想磁流体力学平衡和性能指标的新型可行等离子边界构成的数据集，这三个基准逐渐增加了复杂性：单一目标几何优化问题、易于建造的QI托卡马克和多目标的理想MHD稳定QI托卡马克，调查紧凑性和线圈复杂性之间的权衡。每个基准都提供了参考代码、评估脚本和基于经典优化技术的强基线。通过使用该数据集训练的模型，能够高效地生成新型可行配置，无需查询昂贵的物理或acles。该数据集及其基准问题为优化和机器学习研究者提供了参与托卡马克设计的更低门槛。
### Conclusion
通过公开数据集、基准问题和基线，我们希望为优化和机器学习研究人员降低进入门槛，并加速跨学科进展，将聚变能源引入电网。”该数据集及其提供的基准问题和强基线将为优化和机器学习研究者提供有力工具，促进托卡马克设计的进步，推动核聚变能源的广泛应用。”最终的目的是加速聚变能源技术的发展和商业化应用。”
## 832. `cs.LG` - 将分数匹配与局部固有维度联系起来 [PDF](https://arxiv.org/pdf/2510.12975), [HTML](https://arxiv.org/abs/2510.12975)
### Authors
Eric Yeats,Aaron Jacobson,Darryl Hannan,Yiran Jia,Timothy Doster,Henry Kvinge,Scott Mahan
### Background
局部固有维度（LID）是信号处理和学习理论中的基本量度，但在高维和复杂数据中量化LID一直以来都是一个历史性的挑战。近年来的研究发现，扩散模型能够通过其得分估计的谱和密度估计在不同噪声扰动下的变化率来捕捉数据的LID。虽然这些方法能够精确地量化LID，但它们需要大量执行扩散模型的前向传递或梯度计算，从而限制了它们在计算和内存受限场景中的适用性。
### Innovation
论文提出LID是去噪得分匹配损失的下界，因此利用去噪得分匹配损失作为LID估计器。此外，还展示了等价的隐式得分匹配损失通过正态维度来近似LID，并且与最近的LID估计器FLIPD密切相关。实验结果表明，去噪得分匹配损失是具有竞争力和可扩展的LID估计器，在问题规模和量化水平增加的情况下能够实现更高的准确性和较小的内存消耗。
### Conclusion
研究表明，去噪得分匹配损失可以作为一个有效的LID估计器，其在处理大规模数据和高量化级别时依然保持高性能和低内存占用。这一工作将分数匹配理论与LID估计联系起来，为在受限计算和内存环境中提高LID估计的效率提供了新方法。
## 833. `cs.LG` - 药物发现前沿的扩散模型：小分子与治疗性肽生成的比较 [PDF](https://arxiv.org/pdf/2511.00209), [HTML](https://arxiv.org/abs/2511.00209)
### Authors
Yiquan Wang,Yahui Ma,Yuhan Chang,Jiayao Yan,Jialin Zhang,Minnuo Cai,Kai Wei
### Background
扩散模型在生成建模领域崭露头角，有望改变传统的药物发现过程，该过程通常速度缓慢且成本高昂。这篇文章对比了扩散模型在设计两大主要治疗模式——小分子和治疗性肽——中的应用。
### Innovation
文章对扩散模型在设计小分子和治疗性肽中的应用进行了系统性比较，深入分析了统一的迭代降噪框架如何适应各自不同的分子表示、化学空间和设计目标。同时，文章指出了两个领域各自面临的独特挑战，并强调了它们共有的障碍。
### Conclusion
要充分发挥扩散模型的潜力，需要弥合这两种模式的特定差距，并将其整合到自动化的设计-构建-测试-学习（DBTL）平台上。这将使从化学探索向按需工程新型疗法的转变成为可能。
## 834. `cs.LG` - 赋能大型 tsp 的超路径引导邻域搜索 [PDF](https://arxiv.org/pdf/2510.20169), [HTML](https://arxiv.org/abs/2510.20169)
### Authors
Tongkai Lu,Shuai Ma,Chongyang Tao
### Background
旅行商问题（TSP）是一个经典的 NP 完全问题，受到了学术界和工业界的广泛关注。尽管基于神经网络的方法在解决 TSP 方面显示出了潜力，但在处理大规模实例时仍面临挑战，尤其是由于与全局热图、边权重或访问矩阵相关的内存限制、生成高质量初始解以及缺乏有效引导大规模搜索空间导航的全局指导的问题。
### Innovation
本文提出了一种名为 Hyper Tour Guided Neighborhood Search（HyperNS）的方法，旨在解决大规模 TSP 实例的搜索空间庞大、内存限制、初始解生成不足以及缺乏全局导航指导的问题。该方法首先使用稀疏热图图将 TSP 实例划分为簇，并将其抽象为超级节点，然后生成超路径来引导初始化和优化过程，缩小了搜索空间，提高了优化效率。
### Conclusion
实验结果表明，本文提出的方法在合成数据集和实际数据集上都优于现有的基于神经网络的方法，特别是在处理大规模实例时，显著减少了与最优解的差距。
## 835. `cs.LG` - g-DPO：蛋白质语言模型的可扩展偏好优化 [PDF](https://arxiv.org/pdf/2510.19474), [HTML](https://arxiv.org/abs/2510.19474)
### Authors
Constance Ferragu,Jonathan D. Ziegler,Nicolas Deutschmann,Arthur Lindoulsi,Eli Bixby,Cradle ML Team
### Background
Direct Preference Optimization (DPO) 是一种有效的工具，用于将蛋白质语言模型与实验设计目标对齐。然而，DPO 面临着可扩展性瓶颈：随着标记序列数量的增加，可能的训练对数量呈平方增长，即使是中等大小的数据集也会导致训练时间变得不可接受。
### Innovation
文章引入了 g-DPO 框架，该框架通过 (i) 使用序列空间聚类以同时剪枝冗余对并保留训练信号，和 (ii) 使用基于群组的近似来分摊似然性计算，从而解决了 DPO 的可扩展性问题。g-DPO 跨越了三个蛋白质工程任务，保持了与标准 DPO 相同的仿真和体外性能，但收敛速度快 1.7 到 5.4 倍，且随着数据集大小和潜在突变景观结构的增加而加快。
### Conclusion
g-DPO 在保持与标准 DPO 相同性能的前提下，显著提高了训练速度，特别是对于大型数据集和复杂突变景观，展示了其在蛋白质工程任务中的实用性。
## 836. `cs.LG` - 基于资源感知并行推测性解码的协作大语言模型推理 [PDF](https://arxiv.org/pdf/2511.01695), [HTML](https://arxiv.org/abs/2511.01695)
### Authors
Jungyeon Koh,Hyun Jong Yang
### Background
由于在设备上运行的大语言模型(LLM)推理需求不断增加，特别是在资源受限的环境中，凸显了对高效移动边缘计算(MEC)解决方案的需求。推测性解码通过将标记生成分解为智能手机上的轻量级草稿模型和边缘服务器上的强大目标模型提供了一种有前景的解决方案，但存在通信开销和非同步延迟的问题。
### Innovation
首次提出了一个统一框架，联合优化用户关联和资源分配(UARA)，以支持高效的并行推测性解码。使用多智能体深度强化学习算法解决UARA问题。
### Conclusion
实验结果表明，在使用Sionna模拟器的现实条件下，该方法可将端到端延迟减少最多28.0%，平均减少23.7%，同时不牺牲推理准确性，从而在MEC系统中实现可扩展且低延迟的LLM服务。
## 837. `cs.LG` - HardFlow: 通过轨迹优化的流匹配模型的硬约束采样 [PDF](https://arxiv.org/pdf/2511.08425), [HTML](https://arxiv.org/abs/2511.08425)
### Authors
Zeyang Li,Kaveh Alim,Navid Azizan
### Background
扩散和流匹配方法已经成为了生成建模的强大工具，能够捕捉复杂的数据分布并在推理时提供灵活的引导。然而，许多下游应用需要对生成样本施加强制约束（例如，机器人轨迹必须避开障碍物），这超出了简单的引导要求。目前基于投影的方法会对整个采样路径施加约束，这会导致取样质量下降。
### Innovation
本文提出了一个新颖的框架，将硬约束采样重新表述为一个轨迹优化问题。通过利用数值最优化控制技术来引导采样轨迹，在最终时间点精确满足约束条件。利用流匹配模型的内在结构和模型预测控制技术，将这一复杂的约束优化问题转化为可以高效解决的近似问题。此外，本文的轨迹优化视角提供了超出单一满足约束的灵活性，允许包括积分成本以最小化分布偏移和终端目标以进一步提高样本质量。
### Conclusion
我们在不同领域的广泛实验表明，我们的算法HardFlow在约束满足和取样质量上都显著优于现有方法。我们还提供了一种控制理论分析，建立了可计算逼近误差的界限。
## 838. `cs.LG` - 自组织和谱机制在高容量核霍普菲尔德网络吸引子景观中的自我组织与谱机制 [PDF](https://arxiv.org/pdf/2511.13053), [HTML](https://arxiv.org/abs/2511.13053)
### Authors
Akira Tamamori
### Background
核基学习方法可以显著增加霍普菲尔德网络的存储容量，但其背后的动力学机制尚未完全了解。
### Innovation
文章通过将吸引子景观的几何分析与内核机器的谱理论统一起来，揭示了富含相图的吸引子稳定性，发现了一个‘优化岭’，其中网络在高负载条件下实现最大稳健性。此外，研究了这种现象源于特定的谱重组，称为‘谱浓度’，通过相干的驱动力和反作用力的平衡来实现一种称为‘直接力’和‘间接力’的机制，从而为高效能的联想记忆的形成提供了一个完整的物理图景。
### Conclusion
研究表明，通过将系统调整到特定的‘黄金分割带’状态，可以在谱塌缩和扩散之间实现最佳性能，即自组织状态下的最优性能。
## 839. `cs.LG` - 考虑风能消纳与削峰填谷的电热协同系统优化调度 [PDF](https://arxiv.org/pdf/2511.15250), [HTML](https://arxiv.org/abs/2511.15250)
### Authors
Jin Ye,Lingmei Wang,Shujian Zhang,Haihang Wu
### Background
在全球能源过渡和可再生能源快速发展的背景下，新型能源融合和多重不确定性下的集成电力-热力系统调度优化挑战日益突出。
### Innovation
本文提出了一种基于改进的Dual-Delay Deep Deterministic Policy Gradient（PVTD3）算法的智能调度方法，通过引入电网电力采购变化的惩罚项实现系统优化。与传统的TD3算法相比，该方法在三种典型场景（可再生能源渗透率分别为10%，20%，30%）下分别降低了系统的综合成本6.93%，12.68%，13.59%，并且减少了平均电网电力采购波动幅度12.8%。在能源存储管理方面，低温度热能存储罐的终端状态值减少了7.67-17.67单位，而高温罐保持在3.59-4.25的安全操作范围内。
### Conclusion
所提出的方法不仅在经济效率和电网稳定性方面表现出色，还在能源存储设备管理中的可持续调度能力上具有优越性。
## 840. `cs.LG` - 基于自调整警惕参数的自适应共振理论拓扑聚类算法 [PDF](https://arxiv.org/pdf/2511.17983), [HTML](https://arxiv.org/abs/2511.17983)
### Authors
Naoki Masuyama,Yuichiro Toda,Yusuke Nojima,Hisao Ishibuchi
### Background
在静止或非静止的数据分布环境中进行聚类需要能够适应分布变化同时保持先前学习的聚类结构的模型。现有的聚类算法在面对数据分布的变化时容易忘记之前习得的聚类结构，尤其是在动态环境中。
### Innovation
提出了一种基于自适应共振理论（ART）的拓扑聚类算法，该算法通过多样性驱动的自适应机制自主调整其重新计算间隔和警惕阈值。这一机制实现了无超参数学习，能够在动态环境中维持聚类的稳定性和连续性。
### Conclusion
在24个真实数据集上的实验结果表明，该算法在聚类性能和持续学习能力方面均优于现有方法，展示了自适应参数调整在缓解灾难性遗忘并维持演进数据流中的一致聚类方面的有效性。
## 841. `cs.LG` - 通过基于数据的代理模型增强核反应堆芯模拟 [PDF](https://arxiv.org/pdf/2511.16148), [HTML](https://arxiv.org/abs/2511.16148)
### Authors
Perceval Beja-Battais(CB),Alain Grossetête,Nicolas Vayatis(CB)
### Background
近年来，为了匹配可再生能源的快速增长，核电厂（NPPs）需要提高灵活性。为此，Framatome开发了操作员辅助预测系统（OAPS），通过使用模型预测控制（MPC）来解决这一问题。本文旨在通过数据驱动的模拟方案改进MPC方法。
### Innovation
本文引入了两种代数模型，作为核反应堆核心模拟的替代模拟方案，基于非线性刚性常微分方程（ODEs）的数据驱动方法。结果显示，这两种代数模型能够快速整合复杂的动态特性，计算时间大幅降低（最高可减少1000倍）。
### Conclusion
本文通过使用两种代数模型（数据驱动和物理信息模型），证明了它们能够大幅降低核反应堆核心模拟的计算时间，同时快速集成复杂的动态特性。
## 842. `cs.LG` - 使用链法在高斯过程回归中实现实用的全局和局部边界 [PDF](https://arxiv.org/pdf/2511.09144), [HTML](https://arxiv.org/abs/2511.09144)
### Authors
Junyi Liu,Stanley Kok
### Background
高斯过程回归（GPR）是一种流行的非参数贝叶斯方法，能够提供预测不确定性估计，并广泛应用于安全关键应用中。尽管以往研究引入了各种不确定性边界，但大多数现有方法需要访问特定输入特征，依赖于后验均值和方差估计或超参数调节。这些限制影响了方法的鲁棒性，未能全面捕捉模型期望的全局行为。
### Innovation
提议使用基于链的框架来估计未见数据上的预期极端值的上限和下限，无需访问特定输入特征。提供针对常用核函数（如RBF和Matérn）的具体改进，使得边界更为精确。通过避免解析松弛，进一步提高了数值紧致性。此外，还开发了一种新颖的本地不确定性量化的方法，利用切分直径通过链法几何，适应局部结构而不依赖于后验方差缩放。
### Conclusion
实验结果验证了理论发现，证明该方法在合成数据集和真实世界数据集上的表现优于现有方法。
## 843. `cs.LG` - 困难样本，糟糕标签：知道何时退后的稳健损失函数 [PDF](https://arxiv.org/pdf/2511.16512), [HTML](https://arxiv.org/abs/2511.16512)
### Authors
Nicholas Pellegrino,David Szczecina,Paul Fieguth
### Background
基准数据集和专门校准的数据集中都普遍存在着错误标注的训练数据。这种误标明显地影响了通过监督学习在相关数据集上训练的模型的性能和泛化能力。现有框架通常要求训练好的泛化模型，但这些模型往往依赖于错误标签的数据进行训练，这降低了模型的泛化能力，进而影响错误检测的有效性。因此，如何设计一种能在包含错误标签的数据上仍能有效工作的模型至关重要。
### Innovation
本文提出了两种新颖的损失函数：模糊损失和分段零损失。这两种损失函数通过减轻或忽略难以分类的样本的权重来增强对标签错误的鲁棒性。研究表明，与最先进的稳健损失函数相比，在所有案例中，所提出的损失函数在错误检测上表现更加优越，尤其体现在F1分数上。进一步分析表明，这些损失函数对均匀和非均匀错误标签都有广泛的适用性，并适用于不同的错误标签检测框架。
### Conclusion
通过使用这些稳健损失函数，机器学习从业者可以更有效地识别、修剪或纠正其训练数据中的错误。
## 844. `cs.LG` - 多智能体交叉熵方法结合单调非线性批评分解 [PDF](https://arxiv.org/pdf/2511.18671), [HTML](https://arxiv.org/abs/2511.18671)
### Authors
Yan Wang,Ke Deng,Yongli Ren
### Background
多智能体强化学习（MARL）通常采用集中训练与分散执行（CTDE）的方式，其中集中化的评论者利用全局信息指导分散的执行者。然而，当一个智能体的次优行为影响其他智能体学习时，会产生集中度与分散度不匹配（CDM）的问题。此前的方法通过价值分解来缓解CDM，但线性分解会导致每个智能体的梯度信息，限制了表达能力；而非线性分解虽然能提升表示能力，但需要集中化的梯度，从而重新引入CDM。
### Innovation
本文提出结合单调非线性批评分解（Monotonic Nonlinear Critic Decomposition，NCD）的多智能体交叉熵方法（Multi-agent Cross-Entropy Method，MCEM），通过增加高价值联合动作的概率来更新策略，从而排除次优行为。为了提高样本效率，该方法通过修改k步返回以及ReTrace扩展了离策学习。
### Conclusion
分析与实验表明，MCEM在连续动作和离散动作基准测试中均优于现有最先进的方法。
## 845. `cs.LG` - SculptDrug : 一种基于空间条件的贝叶斯流模型在结构导向药物设计中的应用 [PDF](https://arxiv.org/pdf/2511.12489), [HTML](https://arxiv.org/abs/2511.12489)
### Authors
Qingsong Zhong,Haomin Yu,Yan Lin,Wangmeng Shen,Long Zeng,Jilin Hu
### Background
 Structure-Based Drug Design (SBDD) 作为药物发现的一种流行方法，利用三维蛋白质结构生成药物配体。然而，现有的生成模型面临着几个关键挑战：（1）难以整合边界条件约束，（2）难以整合分层次的结构条件，以及（3）确保空间建模的精确性。
### Innovation
我们提出了SculptDrug，这是一种基于贝叶斯流网络(BFNs)的空间条件感知生成模型。SculptDrug首先遵循BFN框架并采用逐步去噪策略，通过迭代优化原子位置和增强局部相互作用，确保空间建模的精确性。其次，引入了边界感知块，该块将蛋白质表面约束整合到生成过程中，确保生成的配体与目标蛋白质几何相容。最后，设计了分层次编码器，既能捕获宏观结构上下文，又能保留细粒度分子相互作用，确保配体-蛋白质构象的全面一致性和准确性。
### Conclusion
我们在CrossDocked数据集上评估了SculptDrug，实验结果表明SculptDrug优于现有最先进的基准模型，突显了空间条件感知建模的有效性。
## 846. `cs.LG` - 生成对抗后训练减轻实时人机音乐互动中的奖励欺骗 [PDF](https://arxiv.org/pdf/2511.17879), [HTML](https://arxiv.org/abs/2511.17879)
### Authors
Yusong Wu,Stephen Brade,Teng Ma,Tia-Jane Fowler,Enning Yang,Berker Banar,Aaron Courville,Natasha Jaques,Cheng-Zhi Anna Huang
### Background
大多数生成AI应用涉及顺序互动，其中用户输入提示并等待响应，反应时间和适应性不是重要因素。相比之下，现场即兴演奏要求实时协调和适应，无需访问其他演奏者的未来动作，同时保持多样性以维持创造性流程。后训练强化学习能够通过政策交互实现有效的适应，但通常通过利用一致性的奖励减少输出多样性，这种现象称为“奖励欺骗”，对许多后训练强化学习管道有害，但在即兴演奏中尤为严重，因为音乐创作依赖于动态变化和互相应答。
### Innovation
本文提出了一种新的对抗性训练方法，针对政策生成轨迹来减轻后训练强化学习中的奖励欺骗，特别是对于旋律到和弦伴奏。该方法通过使协同进化的判别器将政策轨迹与数据分布分离，同时最大化判别器输出而非一致性奖励，以避免生成简单的输出。
### Conclusion
定量评估和用户反馈表明，该方法能显著提高输出多样性、和声一致性、适应速度和用户自主权。研究结果表明，这是一种简单有效的减轻后训练强化学习生成序列模型中奖励欺骗的方法。
## 847. `cs.LG` - scipy.spatial.transform: Python中不同框架下的可微3D变换 [PDF](https://arxiv.org/pdf/2511.18157), [HTML](https://arxiv.org/abs/2511.18157)
### Authors
Martin Schuck,Alexander von Rohr,Angela P. Schoellig
### Background
三维刚体变换，即旋转和平移，在现代不同的机器学习管道中，尤其是在机器人、视觉和模拟领域，具有核心作用。然而，在SO(3)上的实现，由于轴约定、规范化、组合一致性以及在边缘情况中不易察觉的细节错误，通常会遇到数值稳定性和数学正确性方面的问题。SciPy的spatial.transform模块是一个严格测试的Python实现，但它仅支持NumPy，这对于GPU加速和自定义微分工作流而言限制较大。
### Innovation
我们提供了SciPy的spatial.transform功能的全面翻新，使其兼容任何实现Python数组API的数组库，包括JAX、PyTorch和CuPy。修订后的实现保留了SciPy的现有接口，同时支持GPU/TPU执行、JIT编译、矢量化批量处理以及通过选定后端的原生自动微分。展示了这种基础架构如何支持不同的科学计算案例，如3D变换和旋转变换的扩展性以及基于JAX的无人机模拟中利用SciPy的旋转实现旋转动力学的准确集成。
### Conclusion
我们的贡献已合并到SciPy主分支，并将包含在下一个预发布版本中，提供了一种框架无关的，适用于生产过程的3D空间数学基础，用于不同的系统和机器学习。
## 848. `cs.LG` - 基于学习 aleatoric 不确定性的涡扇发动机剩余使用寿命预测的不确定性感知深度学习框架 [PDF](https://arxiv.org/pdf/2511.19124), [HTML](https://arxiv.org/abs/2511.19124)
### Authors
Krishang Sharma
### Background
在航空航天领域，准确的剩余使用寿命（RUL）预测及其不确定性量化仍然是一个关键挑战。现有的CMAPSS相关文献中鲜有直接通过概率建模学习 aleatoric 不确定性的深度学习框架。
### Innovation
本文介绍了一种新颖的不确定性感知深度学习框架，该框架通过概率建模直接学习 aleatoric 不确定性。该架构采用分层设计，结合多尺度 Inception 块进行时间模式提取，双向长短期记忆网络进行序列建模，并采用双层注意力机制同时作用于传感器和时间维度。创新之处在于，采用贝叶斯输出层预测 RUL 的均值和方差，使模型能学习数据内在的不确定性。此外，实验验证了该框架在 NASA CMAPSS 基准数据集（FD001-FD004）上的整体性能，实现了优于传统方法的新突破，并为关键区域（RUL<=30周期）的预测设立了新的安全基准。
### Conclusion
该框架通过学习的不确定性提供了良好的 95% 置信区间，覆盖范围从 93.5% 到 95.2%，这使得风险意识的维护计划在CMAPSS文献中成为可能，相比传统方法具有25-40%的改进率。
## 849. `cs.LG` - 迷失在序列化中：大型语言模型图推理器的不变性和泛化能力 [PDF](https://arxiv.org/pdf/2511.10234), [HTML](https://arxiv.org/abs/2511.10234)
### Authors
Daniel Herbst,Lea Karbevska,Divyanshu Kumar,Akanksha Ahuja,Fatemeh Gholamzadeh Nasrabadi,Fabrizio Frasca
### Background
尽管基于大规模语言模型（LLMs）的图推理器前景广阔，但它们缺乏对图表示中对称性的内置不变性。在进行图序列化操作时，LLMs对节点重新索引、边重新排序或格式更改的反应不同，这引发了其鲁棒性的问题。本文系统分析了这些效应，研究了微调如何影响编码敏感性和对新任务的泛化能力。研究将图序列化分解为节点标签、边编码和语法，并在综合基准测试套件上评估这些因素的变化对LLMs的影响。此外，还贡献了一组新颖的谱任务，进一步评估微调推理器的泛化能力。
### Innovation
本文提出了一种原理性的图序列化分解方法，将图序列化分解为节点标签、边编码和句法规则，并在综合基准测试套件上评估这些因素的变化对LLMs的影响。同时，贡献了一组新颖的谱任务，进一步评估微调推理器的泛化能力。研究表明，较大的（非微调）模型更具鲁棒性。微调减少了对节点重新标记的敏感性，但也可能增加对结构和格式变化的敏感性，且不一致地提高在新任务上的表现。
### Conclusion
研究结果表明，较大的（未微调）模型更具鲁棒性。微调减少了对节点重新标记的敏感性，但也可能增加对结构和格式变化的敏感性。微调不一定能一致地提高在新任务上的表现。
## 850. `cs.LG` - TREASURE：一种基于变换器的基础模型，用于理解大量交易 [PDF](https://arxiv.org/pdf/2511.19693), [HTML](https://arxiv.org/abs/2511.19693)
### Authors
Chin-Chia Michael Yeh,Uday Singh Saini,Xin Dai,Xiran Fan,Shubham Jain,Yujie Fan,Jiarui Sun,Junpeng Wang,Menghai Pan,Yingtong Dou,Yuzhong Chen,Vineeth Rakesh,Liang Wang,Yan Zheng,Mahashweta Das
### Background
支付网络构成了现代商业的骨干，从日常活动中产生大量交易记录。准确建模这些数据可实现异常行为检测和个性化消费者洞察等应用，从而提升人们的生活质量。
### Innovation
TREASURE是一种多用途的变换器基础模型，专门设计用于交易数据，同时捕捉消费者行为和支付网络信号，提供全面的信息，用于推荐系统和异常行为检测。它具有的输入模块包含针对静态和动态属性的子模块，改进了高卡力度类别属性的预测训练方法，并展示了其作为独立模型和嵌入提供者的有效性。
### Conclusion
通过广泛的消融研究、与生产模型的基准测试和案例研究，TREASURE在异常行为检测性能上提高了111%，在增强推荐模型方面提高了104%。
## 851. `cs.LG` - PrefixGPT: Prefix Adder Optimization by a Generative Pre-trained Transformer [PDF](https://arxiv.org/pdf/2511.19472), [HTML](https://arxiv.org/abs/2511.19472)
### Authors
Ruogu Ding,Xin Ning,Ulf Schlichtmann,Weikang Qian
### Background
前缀加法器广泛应用于计算密集型应用中，由于其高速性能而被广泛应用。然而，设计优化的前缀加法器具有挑战性，因为设计规则严格且设计空间极其庞大。目前设计前缀加法器的方法难以满足高性能需求。
### Innovation
作者提出了一种基于生成预训练Transformer（GPT）的模型，即PrefixGPT，可以直接从头生成优化的前缀加法器。PrefixGPT在随机合适数目的前缀加法器语料库上进行预训练，以学习设计规则，然后进一步微调到设计空间中以优化设计质量。相比现有的工作，PrefixGPT不仅找到了一个新的最优设计，其面积-延迟积（ADP）比现有设计提高了7.7%，并且在探索质量方面更佳，平均ADP降低了高达79.1%，展示了GPT风格模型在复杂硬件设计原则理解方面的潜力及其应用于高效设计优化的前景。
### Conclusion
研究结果表明，GPT风格的模型不仅能够学习和理解复杂的硬件设计原则，还能在高效设计优化中发挥重要作用。PrefixGPT对于设计优化前缀加法器具有创新性和优越性，展示了其在优化设计质量方面的潜力。
## 852. `cs.LG` - 一阶Oracle下的非凸-强凸双层优化的较低复杂度界限 [PDF](https://arxiv.org/pdf/2511.19656), [HTML](https://arxiv.org/abs/2511.19656)
### Authors
Kaiyi Ji
### Background
尽管针对双层优化的上界保证已经得到了广泛的研究，但是由于其复杂的双层结构，针对下界的进展较为有限。本文聚焦在光滑非凸-强凸环境中，并开发了新的硬例子，这些例子能够在确定性和随机一阶Oracle模型下提供非平凡的下界。
### Innovation
研究发现了在确定性和随机一阶Oracle模型下的新下界，即对于$boldsymbol{text{ε}}$-准确的稳定点，任何一阶零容忍算法在确定性情况下至少需要$boldsymbol{text{Ω(κ}^{3/2}boldsymbol{text{ε}^{-2})}}$的Oracle调用，而在随机情况下至少需要$boldsymbol{text{Ω(κ}^{5/2}boldsymbol{text{ε}^{-4})}}$的随机Oracle调用。这些结果加强了相关领域的现有下界。
### Conclusion
本文的结果揭示了当前双层优化上界和下界之间的巨大差距，表明即使简化到二阶优化问题，如具有二次下层目标函数，也值得进一步研究以理解标准一阶Oracle下双层优化的最优复杂度。
## 853. `cs.LG` - Adam简化：驳斥偏差校正 [PDF](https://arxiv.org/pdf/2511.20516), [HTML](https://arxiv.org/abs/2511.20516)
### Authors
Sam Laing,Antonio Orvieto
### Background
Adam优化器是现代深度学习的基石，但其各个组成部分的重要性经常被默认认为是不言而喻的。本文专注于探讨偏差校正的作用，而这一特性在贡献上仍然理解不足。
### Innovation
本文通过系统地在视觉和语言建模任务中进行消融实验，证明了关于偏差校正的传统观点是误导性的。具体而言，当采用最佳超参数配置时，包含偏差校正并不会提高最终测试性能。另外，除非实施适当的学习率调度，否则包含偏差校正有时反而会对性能产生不利影响。我们进一步重新解释偏差校正，将其视为一种依赖于平滑超参数β1,β2选择的隐式学习率调度，其行为受这些超参数的影响显著。
### Conclusion
研究结果挑战了普遍包含这个组件的做法。
## 854. `cs.LG` - QiMeng-CRUX: Narrowing the Gap between Natural Language and Verilog via Core Refined Understanding eXpression [PDF](https://arxiv.org/pdf/2511.20099), [HTML](https://arxiv.org/abs/2511.20099)
### Authors
Lei Huang,Rui Zhang,Jiaming Guo,Yang Zhang,Di Huang,Shuyao Cheng,Pengwei Jin,Chongxiao Li,Zidong Du,Xing Hu,Qi Guo,Yunji Chen
### Background
现有的硬件描述语言（HDL）生成方法往往依赖于自由形式的自然语言描述，这些描述经常具有模糊性、冗余性和无序性，这给后续的Verilog代码生成带来了显著挑战。研究将硬件代码生成视为从开放性自然语言空间到高度特定领域且受限目标空间的复杂转换。
### Innovation
本文提出了一种称为Core Refined Understanding eXpression (CRUX)的结构化中间空间，用于捕捉用户意图的核心 semantics 并组织表达，以精确生成Verilog代码。此外，设计了一种两阶段训练框架，包括联合表达建模和双空间优化，以提高CRUX和Verilog代码的质量。实验结果表明，我们的模型CRUX-V在多个Verilog生成基准上的性能达到了最先进的水平，尤其是在高挑战性的设计任务中。
### Conclusion
CRUX 空间不仅可以作为其他代码模型的输入提示，提高生成精度，还在多个验证测试中证明了其可转移性和有效性，进一步缩小了自由形式自然语言描述与精确Verilog生成之间的差距。
## 855. `cs.LG` - TiCT：一种用于时间序列分类的合成预训练基础模型 [PDF](https://arxiv.org/pdf/2511.19694), [HTML](https://arxiv.org/abs/2511.19694)
### Authors
Chin-Chia Michael Yeh,Uday Singh Saini,Junpeng Wang,Xin Dai,Xiran Fan,Jiarui Sun,Yujie Fan,Yan Zheng
### Background
时间序列数据的普遍存在对通用基础模型提出了强烈需求，但构建用于分类的基础模型仍然是一个重大挑战，主要原因是对标注数据的成本高昂。具备上下文学习能力（ICL）的基础模型能够通过少量示例快速适应新任务，并减少需要的重新训练工作量。尽管大规模时间序列模型在预测领域取得了重大进展，但对于需要适应多种任务而无需微调且具有通用性的时间序列分类问题，研究依然不足。
### Innovation
本文提出了TiCT（Time-series in-Context Transformer），一种基于Transformer构建的时间序列分类基础模型，专门使用合成数据进行预训练，无需标注数据即可进行上下文学习，并取得优异的分类性能。模型有两个主要的技术贡献：1) 一种可扩展的位基标签编码结构和一种专用的输出注意力机制，用于处理任意数量的类别；2) 一种综合Mixup启发的数据增强方法，以生成更大泛化能力和噪声不变性的合成数据集。
### Conclusion
TiCT 在UCR档案上的全面评估表明，该模型在分类任务上达到了与最先进的监督学习方法相当的性能。最关键的是，这一成就在推理阶段仅使用上下文示例就达成，没有调整任何一个模型权重。
## 856. `cs.LG` - MoRE: 从冻结预训练变换器生成的跨批次多组学表示 [PDF](https://arxiv.org/pdf/2511.20382), [HTML](https://arxiv.org/abs/2511.20382)
### Authors
Audrey Pei-Hsuan Chen
### Background
多组学数据的表示学习面临着极大的维度、模态异质性和批次效应的问题。尽管预训练的变压器在生物序列建模中展示了广泛的应用能力，但它们在多组学整合中的应用仍处于探索阶段。
### Innovation
MoRE 提出了一种框架，通过重新利用冻结的预训练变压器来将异质实验调整到共享的潜在空间。MoRE 采用参数高效的微调策略，优先对样本和模态进行对齐而非简单的序列重建。具体来说，MoRE 在冻结的主干上附加了轻量级、模态特定的适配器和任务自适应融合层。MoRE 优化了一个掩码建模目标，结合了监督对比损失和批次不变对齐损失，从而生成结构保留的嵌入，这些嵌入在未见过的细胞类型和平台上具有很好的泛化能力。
### Conclusion
我们将 MoRE 与现有的基线方法（包括 scGPT、scVI 和使用 Scrublet 的 Harmony）进行了基准测试，评估其整合忠实度、稀有群体检测和模态转移。实验结果表明 MoRE 在保持跨批次稳健性和生物学一致性方面达到了竞争力，同时大幅减少了可训练参数的数量。这项工作为通用组学基础模型的实现奠定了实用的一步。
## 857. `cs.LG` - 因子辅助联邦学习中的个性化优化异质数据 [PDF](https://arxiv.org/pdf/2312.04281), [HTML](https://arxiv.org/abs/2312.04281)
### Authors
Feifei Wang,Huiyun Tang,Yang Li
### Background
联邦学习是一种新兴的分布式机器学习框架，旨在保护数据隐私。数据异质性是联邦学习的核心挑战之一，可能会严重影响深度神经网络的收敛速度和预测性能。
### Innovation
研究提出了一种新的个性化联邦学习框架FedSplit，将神经网络的不同隐层元素分解成共享和个性化组，并基于此构建了新的优化目标函数。此外，通过引入因子分析来实际实施FedSplit方法，并将其命名为FedFac，证明了使用因子分析可以很好地恢复潜在的共享/个性化分解，并进一步验证了FedFac在几种实际数据集上的优越预测性能。
### Conclusion
FedSplit在理论上和实验上都显示了比标准联邦学习方法更快的收敛速度。FedFac方法的泛化界限也被研究。实验结果表明，使用因子分析可以有效提高联邦学习的个性化优化效果，特别是在处理异质数据时。
## 858. `cs.LG` - 高效生成模型的扩展 [PDF](https://arxiv.org/pdf/2402.14746), [HTML](https://arxiv.org/abs/2402.14746)
### Authors
B.N. Kausik
### Background
最近的大型语言模型（LLM）具有数百亿参数，并消耗大量资源。根据变压器的所谓‘AI扩展定律’，参数量必须与数据大小成线性关系。因此，研究如何在保持所需准确性的前提下，使用最少的参数构建高效模型显得尤为重要。
### Innovation
提出了一种递归变压器模型，结合了transformer的高效性和递归网络的效率。递归变压器按固定宽度的滑动窗口逐步应用于输入序列的一层transformer层。这种设计使得模型在序列长度上线性运行，内存使用高效，适合大规模并行处理，能够根据任务需求记忆过去的信息或忘记过去的信息，以及有助于克服梯度消失问题。
### Conclusion
实验结果显示，递归变压器在基准测试中表现出色，证明了其在保持模型效率的同时，可以有效提高任务性能。
## 859. `cs.LG` - 去中心化 bilevel 优化：从瞬态迭代复杂性角度的研究 [PDF](https://arxiv.org/pdf/2402.03167), [HTML](https://arxiv.org/abs/2402.03167)
### Authors
Boao Kong,Shuchen Zhu,Songtao Lu,Xinmeng Huang,Kun Yuan
### Background
随机二阶优化（SBO）在机器学习中因其处理嵌套结构的灵活性变得越来越重要。去中心化方法通过节点仅与其直接邻居通信而没有中央服务器来处理大规模SBO，这提高了通信效率并增强了算法的鲁棒性。然而，大多数去中心化的SBO算法仅关注渐近收敛速度，而忽略了瞬态迭代复杂性——即在渐近速度占优之前所需的实际迭代次数。这意味着在理解网络拓扑、数据异质性和嵌套 bilevel 算法结构的影响方面存在限制。
### Innovation
该论文提出了D-SOBA（去中心化的随机单环 bilevel 算法框架），包括D-SOBA-SO（集成二阶海森矩阵和雅可比矩阵）和D-SOBA-FO（完全依赖于一阶梯度）两个变体。为D-SOBA提供了全面的非渐近收敛分析，并确定了其瞬态迭代复杂性。这为理解网络拓扑、数据异质性和嵌套 bilevel 结构对去中心化SBO的影响提供了一种理论上的理解。
### Conclusion
广泛的实验结果表明，D-SOBA在效率和理论优势方面表现出色，为理解去中心化SBO的工作原理提供了新的视角。
## 860. `cs.LG` - 适应性室内导航辅助中的实时目标检测性能评估 [PDF](https://arxiv.org/pdf/2501.18444), [HTML](https://arxiv.org/abs/2501.18444)
### Authors
Abhinav Pratap,Sushant Kumar,Suchinton Chakravarty
### Background
本文关注视觉障碍人士的辅助技术中准确且高效的物体检测需求。研究在室内导航辅助的情境下，对YOLO、SSD、Faster R-CNN和Mask R-CNN四种实时物体检测算法进行了评估。通过使用室内物体检测数据集，分析了检测精度、处理速度和适应室内环境的能力。
### Innovation
研究揭示了精度与效率之间的权衡，为实时辅助导航系统选择合适的算法提供指导，促进了适应性机器学习在室内导航解决方案中的应用，提高了视觉障碍人群的无障碍水平。
### Conclusion
本文的结果为选择适用于实时辅助导航的最优算法提供了依据，促进了室内导航解决方案中适应性机器学习技术的应用和无障碍环境的改善。
## 861. `cs.LG` - UniGame：将统一多模态模型转变为自身的对手 [PDF](https://arxiv.org/pdf/2511.19413), [HTML](https://arxiv.org/abs/2511.19413)
### Authors
Zhaolong Su,Wang Lu,Hao Chen,Sharon Li,Jindong Wang
### Background
统一多模态模型（UMMs）在理解与生成任务中展现出强大的性能，但它们在理解与生成之间存在根本性的不一致：理解偏好紧凑的嵌入表示，而生成偏好重建丰富的表示。这种结构上的权衡导致决策边界不一致、跨模态一致性下降以及在分布变化和对抗攻击下的脆弱性增加。
### Innovation
本文提出了UniGame，一种自我对抗的后训练框架，直接解决上述问题。UniGame在共享的令牌接口处应用了一个轻量级扰动器，使生成分支主动寻求并挑战脆弱的理解，将模型自身转变为对手。实验结果显示，UniGame显著提高了连贯性（+4.6%）、理解能力（+3.6%）、生成性能（+0.02），以及分布外鲁棒性和对抗鲁棒性（+4.8%和+6.2%在NaturalBench和AdVQA上）。该框架在架构上是通用的，额外参数少于1%，能与其他后训练方法互补。
### Conclusion
本文将对抗自演机制视为增强未来多模态基础模型一致性和稳定性的普遍有效原则，并提供了可访问的官方代码。
## 862. `cs.LG` - 基于潜在扩散模型的图像编辑对抗攻击：后验塌缩攻击 [PDF](https://arxiv.org/pdf/2408.10901), [HTML](https://arxiv.org/abs/2408.10901)
### Authors
Zhongliang Guo,Chun Tong Lei,Lei Fang,Shuai Zhao,Yifei Qian,Jingyu Lin,Zeyu Wang,Cunjian Chen,Ognjen Arandjelović,Chun Pong Lau
### Background
近年来，潜在扩散模型（LDMs）在图像合成和处理方面取得了重大进展，但同时也引发了数据滥用和知识产权侵权的严重问题。尽管针对生成式AI滥用的对抗攻击被广泛研究作为防护措施，但现有的方法严重依赖于模型特定的知识，且计算成本非常高。本文分析了变分自编码器（VAE）推理中的后验塌缩现象，提出了一种新的方法——后验塌缩攻击（PCA），以保护图像免遭未经授权的处理。
### Innovation
本文提出了后验塌缩攻击（PCA），这是一种针对基于潜在扩散模型图像编辑的新颖防护框架。PCA通过VAE编码器实现对图像的防护，VAE编码器仅占LDM参数的不到4%，极大地减少了对模型特定知识的依赖。PCA能够通过参数调整实现两种不同类型的塌缩现象——扩散塌缩和集中塌缩，分别对应防止图像编辑的不同防护目标。PCA能够在图像文本条件化之前操作VAE编码器，从而实现对提示不变的保护，这在现有方法中是必要的。PCA通过尽量减少对模型特定知识的依赖，保持良好的跨VAE基于LDM架构的迁移性能，从而有效地防止未经授权的图像编辑。广泛的实验显示，PCA在防护效果、计算效率和跨VAE基于LDM变种的一般化方面均优于现有技术。
### Conclusion
本文通过理论分析和实证验证，提出了一种新的防护框架——后验塌缩攻击（PCA），该方法能够在保持较低依赖于模型特定知识和较低计算成本的同时，提供有效且具有广泛适用性的防护。PCA在多个基于VAE的LDM架构上表现出高性能的防护效果和良好的迁移性，能有效防止未经授权的图像编辑，这在保护知识产权方面表现出了极大的潜力。
## 863. `cs.LG` - 通过邻近点算法的一种催化剂框架解决量子线性系统问题 [PDF](https://arxiv.org/pdf/2406.13879), [HTML](https://arxiv.org/abs/2406.13879)
### Authors
Junhyung Lyle Kim,Nai-Hui Chia,Anastasios Kyrillidis
### Background
解决线性方程组是基础问题，但在高维情况下，经典算法会变得计算密集。现有的量子算法能够在维度方面提供指数级速度提升，但这一优势受限于系数矩阵的条件数。
### Innovation
提出了一个新的量子算法，受到了经典邻近点算法的启发。该算法可以被视为一个元算法，允许通过已有的QLSP_solver实现矩阵的逆，直接对解向量进行近似而非对系数矩阵的逆进行近似。通过精心选择步长η，该算法可以有效地对线性系统进行预条件处理，以减轻以前方法因条件数依赖而带来的限制。这是一类可用于QLSP的迭代框架，其中可调参数η和初始化x_0允许控制运行时间和近似误差之间的权衡。
### Conclusion
该工作提供了一种新型的量子算法框架，通过调整参数和初始化，优化了以前方法中存在的条件数依赖性问题。
## 864. `cs.LG` - LTD: Low Temperature Distillation for Gradient Masking-free Adversarial Training [PDF](https://arxiv.org/pdf/2111.02331), [HTML](https://arxiv.org/abs/2111.02331)
### Authors
Erh-Chung Chen,Che-Rung Lee
### Background
对抗训练是提升神经网络模型在对抗攻击下稳健性的广泛采用策略。该论文回顾了图像分类的基本假设，并指出将数据表示为独热标签是导致模型漏洞的关键因素。然而，在实际数据集中，数据的模糊性常常导致样本同时具有多个类别的特征，使得独热标签表示变得不精确。
### Innovation
论文提出了一种名为Low-Temperature Distillation (LTD)的新方法，旨在改进标签表示。与之前的方法不同，LTD在教师模型中使用相对较低的温度，而在学生模型的训练和推断过程中保持固定温度。这种方法不仅改进了对数据分布的假设，还增强了模型的稳健性，并避免了在防御性蒸馏中常见的梯度遮蔽问题。
### Conclusion
实验结果表明，该方法与现有框架结合使用时非常有效，分别在CIFAR-10、CIFAR-100和ImageNet数据集上达到了58.19%、31.13%和42.08%的鲁棒准确率，而无需额外的数据。
## 865. `cs.LG` - 地球观测卫星调度中的图神经网络和蒙特卡洛树搜索 [PDF](https://arxiv.org/pdf/2408.15041), [HTML](https://arxiv.org/abs/2408.15041)
### Authors
Antoine Jacquet,Guillaume Infantes,Emmanuel Benazera,Vincent Baudoui,Jonathan Guerra,Stéphanie Roussel
### Background
地球观测卫星规划（EOSP）是一个优化问题，具有较高的实用价值。一组观测需求需要在灵活的地球观测卫星上进行调度，同时满足视窗可见性和动作约束。存在大量的候选观测，但无法全部实现，因此需要选择那些可以执行的观测，并最大化其累积效益。先前的研究主要集中在启发式和迭代搜索算法上。
### Innovation
该论文提出了一种基于图神经网络(GNNs)和深度强化学习(DRL)的新技术，用于选择和调度观测。GNNs用于从表示EOSP实例的图中提取相关信息，DRL驱动最佳调度的搜索。后学习阶段基于蒙特卡洛树搜索(MCTS)能够找到更好的解决方案。实验结果表明，该方法在小型问题实例上能够学习并且能够泛化到大型实际问题实例，性能优于传统方法。
### Conclusion
通过学习小型问题实例，能够有效泛化到大型实际问题实例，该方法在性能上具有很强的竞争力。
## 866. `cs.LG` - 超态量子力学 [PDF](https://arxiv.org/pdf/2502.00037), [HTML](https://arxiv.org/abs/2502.00037)
### Authors
Mikhail Gennadievich Belov,Victor Victorovich Dubov,Vadim Konstantinovich Ivanov,Alexander Yurievich Maslov,Olga Vladimirovna Proshina,Vladislav Gennadievich Malyshkin
### Background
量子力学通常仅考虑一个关于波函数归一化的二次约束，并以哈密顿量为二次函数的形式表达能量。超级状态量子力学（SQM）扩展了这一框架，考虑多组二次约束，并将能量表示为这些状态的二次函数。
### Innovation
作者提出了超级状态量子力学，这是一种处理多组二次约束的理论，使静止问题能转化为量子逆问题，具有广泛的应用前景。此外，理论提出了一种新的动态方程，并提供了一种新的计算算法，此算法将直接与逆量子力学问题进行自然结合。同时，作者探讨了将量子信道作为经典计算模型的可行性。
### Conclusion
虽然尚未有物理过程能够描述2D动态，但超级状态量子力学仍为新的量子计算算法开发提供了可能性。作为一种立即可行的应用，文中提出可以使用量子信道进行经典计算。
## 867. `cs.LG` - 大型语言模型中最佳选项抽样aware微调方法 [PDF](https://arxiv.org/pdf/2412.15287), [HTML](https://arxiv.org/abs/2412.15287)
### Authors
Yinlam Chow,Guy Tennenholtz,Izzeddin Gur,Vincent Zhuang,Bo Dai,Sridhar Thiagarajan,Craig Boutilier,Rishabh Agarwal,Aviral Kumar,Aleksandra Faust
### Background
近来研究表明，在推理时高效利用计算资源对于大型语言模型（LLMs）的性能提升至关重要。本文在此背景下，聚焦于提出一种新型的推理aware微调策略，直接优化特定推理策略的表现。
### Innovation
研究采用了一种简单而有效的最佳选项（BoN）推理策略，并创新性地设计了首个针对BoN策略的模仿学习和强化学习方法。该方法克服了BoN策略中的非可微argmax操作问题，使模型在微调时能够学习到一种混合使用最佳响应与更具多样性的响应的元策略，这一过程类似于RL中的探索-利用权衡。
### Conclusion
实验结果表明，本文提出的BoN-aware微调方法在性能和推理所需的计算上都有所提升。具体而言，方法可以让Gemma 2B在Hendrycks MATH数据集上的Bo32性能从26.8%提高到30.8%，pass@32性能从60.0%提高到67.0%，在HumanEval数据集上的pass@16性能从61.6%提高到67.1%。
## 868. `cs.LG` - Meursault作为数据点 [PDF](https://arxiv.org/pdf/2502.01364), [HTML](https://arxiv.org/abs/2502.01364)
### Authors
Abhinav Pratap
### Background
在数据化时代，人类经历被量化为可测量的指标引发了深刻的哲学和伦理问题。本文通过阿尔贝·加缪的《局外人》中的主角默尔索的无情存在来探讨这些问题。默尔索的这种情感疏远的生活体现了存在主义的荒诞性概念。通过自然语言处理（NLP）技术，包括情感检测（BERT）、情感分析（VADER）和命名实体识别（spaCy），本文量化了默尔索生命中的一些关键事件和行为。
### Innovation
本文使用自然语言处理技术，具体包括情感检测、情感分析和命名实体识别，量化默尔索生活中的关键事件和行为，揭示了应用算法模型到复杂人类经验中的固有限制，尤其是涉及存在主义的疏远和道德的模糊性。研究还探讨了现代人工智能工具如何误解默尔索的行为和情感，揭示了将细腻的人类叙述简化为数据点所引发的更广泛伦理困境。这些发现对数据驱动的社会提出了批评，并呼吁在人工智能中融入人文价值观。
### Conclusion
本文的研究结果表明，数据驱动的叙事正在日益依赖，但是这种依赖忽视了人类经验的复杂性和丰富性，应该提倡将人文价值观融入人工智能发展中。
## 869. `cs.LG` - 从非序列数据识别随机动力学（IDyNSD） [PDF](https://arxiv.org/pdf/2502.17690), [HTML](https://arxiv.org/abs/2502.17690)
### Authors
Zhixin Lu,Łukasz Kuśmierz,Stefan Mihalas
### Background
从数据推断随机动力学在科学界至关重要，但在许多实际应用中，可用的测量数据是无序且非序列性的，通常局限于状态空间的特定区域，传统的时序分析方法不适用。
### Innovation
本文引入了IDyNSD框架，通过最小化Fokker-Planck残差从非序列数据中识别未知的动力学参数。该框架包括本地路线和全局路线，能够处理受限区域数据和全局采样数据，适用于不同类型的非线性动力学模型，并且对于一般的非仿射情形，该方法定义了可梯度优化的损失函数。
### Conclusion
IDyNSD提供了两种基于Fokker-Planck方程的第一性原理方法来从非序列数据中识别系统动力学，通过数据、密度和随机动力学的关联提供了一种新的视角。通过实验验证了该方法的有效性，并展示了其在识别动力学参数和非线性基因调控网络方面的能力，同时展示了Fokker-Planck残差视角支持的一种“从动力学到密度”的互补方法，直接从已知动力学训练归一化的密度估计器而不依赖任何观测数据。
## 870. `cs.LG` - 超出目录的个性化图像生成推荐 [PDF](https://arxiv.org/pdf/2502.18477), [HTML](https://arxiv.org/abs/2502.18477)
### Authors
Gabriel Patron,Zhiwei Xu,Ishan Kapnadak,Felipe Maia Polo
### Background
个性化对于人类与AI的交互至关重要，但目前基于扩散的图像生成系统仍对用户多样性关注不足。现有解决方法往往依赖昂贵的配对偏好数据，或者通过大型语言模型引入延迟。
### Innovation
本文介绍了一种轻量级且可扩展的框架——REBECA（REcommendations BEyond CAtalogs），它能够直接从隐式反馈信号（如点赞、评分和点击）中学习，无需微调底层扩散模型。REBECA采用两阶段过程，首先训练条件扩散模型来生成用户和评分特定的图像嵌入，然后使用预训练的扩散模型进行解码。这种方法能够高效地在大规模用户群体中实现个性化的无微调生成。
### Conclusion
我们在真实数据集上严格评估了REBECA，提出了新的统计个人化验证方法和基于排列的假设检验来评估偏好对齐。结果表明，REBECA能够持续生成高质量且符合个人口味的图像，优于基线方法的同时保持计算效率。
## 871. `cs.LG` - LASER: 唇部关键点辅助稳健的讲者检测 [PDF](https://arxiv.org/pdf/2501.11899), [HTML](https://arxiv.org/abs/2501.11899)
### Authors
Le Thien Phuc Nguyen,Zhuoran Yu,Yong Jae Lee
### Background
Current Active Speaker Detection (ASD) models frequently misclassify non-speaking instances when lip movements and audio are unsynchronized, even though humans rely on lip-audio synchronization to detect active speakers. This paper addresses this issue by proposing LASER, a model that explicitly incorporates lip landmarks during training to direct the model's attention towards speech-relevant regions.
### Innovation
LASER 集成了唇部关键点辅助训练，通过提取视觉特征并编码二维唇部关键点为密集图，来指导模型注意力聚焦于与语音相关的区域。此外，它引入了一个辅助一致性损失，将唇部感知和面部感知的预测对齐，从而在测试时无需使用关键点检测器，增强了模型在低分辨率或遮挡情况下的鲁棒性。
### Conclusion
实验结果表明，LASER 在多个基准测试中表现优于现有的状态领先模型。特别是在高噪声背景下，LASER 的 mAP 值分别提高了 3.3 和 4.3 个百分点，比 LoCoNet 和 TalkNet 更加耐受现实中的声学挑战。为此，作者还提出了 LASER-bench，这是一个由现代视频片段组成的数据集，具有不同的背景噪声级别，用以进一步评估鲁棒性。
## 872. `cs.LG` - PointNSP：基于下级细节预测的自回归3D点云生成 [PDF](https://arxiv.org/pdf/2503.08594), [HTML](https://arxiv.org/abs/2503.08594)
### Authors
Ziqiao Meng,Qichao Wang,Zhiyang Dou,Zixing Song,Zhipeng Zhou,Irwin King,Peilin Zhao
### Background
自回归点云生成模型在质量上长期落后于基于扩散的方法。这种差距源于自回归模型对点集的顺序施加了人为的约束，迫使形状生成以局部预测的形式进行序列化。这种序列偏好能够强调近距离连续性，但却削弱了模型捕捉远距离依赖关系的能力，妨碍了对全局结构属性如对称性、一致拓扑和大规模几何规律的强制执行。
### Innovation
受到形状建模中的层次细节（LOD）原则的启发，该论文提出了一个粗到细的生成框架——PointNSP，通过下一级预测机制在低分辨率时保持全局形状结构，在高分辨率时逐级细化细粒度几何。这种多尺度分解使自回归目标与点集的置换不变特性相一致，促进了丰富的跨尺度交互，同时避免了僵硬的固定顺序。
### Conclusion
在ShapeNet上的实验表明，PointNSP在自回归范式下首次实现了最先进的生成质量，并且在参数、训练和推理效率上超越了强大的基于扩散的基线模型。此外，在使用8192点进行密集生成时，PointNSP的优势尤为明显，突显了其扩展潜力。
## 873. `cs.LG` - 数学洞察蛋白质架构：应用于鞭毛马达的持久同调与机器学习 [PDF](https://arxiv.org/pdf/2504.16941), [HTML](https://arxiv.org/abs/2504.16941)
### Authors
Zakaria Lamine,Abdelatif Hafid,Mohamed Rahouti,My Ismail Mamouni
### Background
本文介绍了一种基于持久同调的机器学习方法，用于分类细菌鞭毛马达为旋转状态和停滞状态。通过将蛋白质结构数据嵌入拓扑框架中，从基于原子坐标构造的滤波单纯复形中提取多尺度特征。这些拓扑不变量，尤其是持久图和条形图，捕获了与马达功能相关的关键几何和连接模式。提取的特征被矢量化并整合到一个机器学习流程中，该流程包括降维和监督分类。应用到来自多种细菌物种的实验表征鞭毛马达的数据集上，该模型显示了高分类精度和对结构变化的鲁棒性。
### Innovation
本研究提出了一种创新的方法，利用拓扑数据分析技术（具体为持久同调），从蛋白质结构数据中提取多尺度特征，并将其与机器学习技术相结合，实现了对细菌鞭毛马达的高效分类。这种方法能够揭示出传统几何描述难以捕捉的功能相关模式，为蛋白质功能预测提供了一种新的计算工具。
### Conclusion
该研究模型在实验表征的鞭毛马达数据集上的高分类精度和对结构变化的鲁棒性，展示了拓扑数据分析的强大之处，超过了传统的几何描述手段。此方法为理解蛋白质功能提供了一种有价值的工具。
## 874. `cs.LG` - 使用图扩散网络学习Agent-Based模型中的个体行为 [PDF](https://arxiv.org/pdf/2505.21426), [HTML](https://arxiv.org/abs/2505.21426)
### Authors
Francesco Cozzi,Marco Pangallo,Alan Perotti,André Panisson,Corrado Monti
### Background
Agent-Based Models (ABMs)是一种强大的工具，用于研究复杂系统的新兴特性。在ABMs中，代理的行为由局部交互和随机规则控制。然而，这些规则通常是非可微的，限制了使用基于梯度的方法进行优化，并且因此限制了与现实世界数据的集成。
### Innovation
提出了一个新颖的框架，通过观察生成的数据来学习任意ABM的可微近似。该方法结合了扩散模型来捕获行为的随机性，并使用图神经网络建模代理之间的交互。区别于先前的近似方法，这种方法引入了根本的转变：它直接建模个体代理的行为，而不是近似系统级别的输出，从而保持了定义ABMs的去中心化、自底向上的动态。
### Conclusion
在两个ABM（Schelling的隔离模型和捕食者-被捕食者生态系统）上验证了该方法，表明该方法能够复制个体级别的模式，并准确预测超出训练的新兴动态。结果显示，将扩散模型与图学习相结合有望为数据驱动的ABM仿真提供潜力。
## 875. `cs.LG` - GiBy: 一种工业控制系统中异常检测的巨步小步分类器 [PDF](https://arxiv.org/pdf/2504.20906), [HTML](https://arxiv.org/abs/2504.20906)
### Authors
Sarad Venugopalan,Sridhar Adepu
### Background
任何工业控制系统（ICS）中，持续监测网络物理组件之间的交互对于确保自动化系统控制的安全性至关重要，以确保工厂过程的安全，且保持在可接受的安全状态。安全性依赖于电信号触发物理动作以及基于传感器读数进行的行为控制。对于及时检测工业控制系统中的异常（包括攻击、故障和不确定状态）对于保障工厂安全、人员安全和连续服务的提供至关重要。
### Innovation
本文提出了一种异常检测方法，通过线性化传感器-执行器关系的非线性形式来准确进行线性化，因为解决线性模型更为容易且被广泛理解。该方法利用了一个臭名昭著的水处理测试床作为案例。我们的实验结果表明，该方法能够在毫秒级别响应时间内检测到异常，且这些异常均具有可解释性和追踪性。相比现有的具有解释性人工智能（XAI）的先进人工智能（AI）/ 机器学习（ML）模型，同时在检测速度和解释性上实现更佳效果。
### Conclusion
提出的算法在97.72%的准确率下，能够识别出在安全操作范围内被视为非异常的情况，表明慢速检测器在提供较大安全边界的安全系统中是不必要的。
## 876. `cs.LG` - 使用可微气候模型构建极端热浪情景 [PDF](https://arxiv.org/pdf/2506.10660), [HTML](https://arxiv.org/abs/2506.10660)
### Authors
Tim Whittaker,Alejandro Di Luca
### Background
了解气候变化中极端天气事件可能的最坏情况对于风险评估至关重要。现有的基于大型物理模型集合的方法在计算效率或精度上存在局限性，无法准确模拟罕见且影响重大的极端事件。
### Innovation
本文提出了一种新的框架，利用可微气候模型（NeuralGCM）优化初始条件并生成具有物理一致性的最坏情况热浪轨迹。结果表明，可微气候模型可以高效地探索事件发生的尾端概率，提供了一种应对气候变化情景下的极端天气的强大新方法。
### Conclusion
在2021年太平洋西北地区热浪案例中，该方法产生了比75成员集合中最极端的成员高3.7摄氏度的热浪强度。这些轨迹表现出增强了的大气阻塞和罗斯比波模式，证明了这种不同可微气候模型在极端天气情景构建中的有效性。
## 877. `cs.LG` - 平均值-偏差多代理强化学习与策略优化用于均值-方差团队随机博弈 [PDF](https://arxiv.org/pdf/2503.22779), [HTML](https://arxiv.org/abs/2503.22779)
### Authors
Junkai Hu,Li Xia
### Background
研究了一个长期均值-方差团队随机博弈（MV-TSG），其中每个代理共享一个共同的系统均值-方差目标，并独立采取行动以最大化这个目标。这是一个复杂的博弈问题，存在两个主要挑战：一是方差度量在动态环境中既不是加性也不是马尔可夫性质，二是所有代理同时更新策略会导致每个个体代理处于非 stationary 的环境中。这使得动态规划方法不适用。
### Innovation
本文从基于灵敏度的优化角度研究 MV-TSG，推导了联合策略的性能差异和性能导数公式，证明了存在确定性纳什策略，并提出了一种序列更新方案的多代理策略迭代算法（MV-MAPI），该算法收敛到目标函数的一阶稳定点。进一步通过对稳定点局部几何结构的分析，给出了稳定点成为纳什均衡或严格局部最优解的具体条件。还提出了一种多代理信任区域策略优化算法（MV-MATRPO）来解决具有未知环境参数的大规模 MV-TSG。并推导了每次联合策略更新的性能下界。
### Conclusion
最后，通过在多个微电网管理系统进行数值实验验证了该方法的有效性。
## 878. `cs.LG` - Momentum Multi-Marginal Schrödinger Bridge Matching [PDF](https://arxiv.org/pdf/2506.10168), [HTML](https://arxiv.org/abs/2506.10168)
### Authors
Panagiotis Theodoropoulos,Augustinos D. Saravanos,Evangelos A. Theodorou,Guan-Horng Liu
### Background
通过从稀疏样本快照推断轨迹来理解复杂系统是一个广泛领域中的基本挑战，包括单细胞生物学、气象学和经济学。尽管Bridge和Flow匹配框架有所进步，但现有方法主要依赖相邻快照的成对内插，这限制了它们捕捉长程时间依赖性以及确保所推断轨迹的连贯性。
### Innovation
我们引入了一种名为Momentum Multi-Marginal Schrödinger Bridge Matching (3MSBM) 的新型匹配框架，它通过提升动力学到相空间并泛化条件随机桥梁使其依赖多个点来学习满足多个位置约束的随机系统的平滑测度值样条。3MSBM的学习过程通过最小化变分目标实现，路径由多边际条件桥梁诱导固定。作为一种匹配方法，3MSBM在训练过程中保持中间边际不变，显著提高了收敛性和可扩展性。
### Conclusion
在一系列实际应用中的大量实验验证，3MSBM在捕捉具有时间依赖性的复杂动态方面明显优于现有方法，为多边际设置下的训练匹配框架开辟了新途径。
## 879. `cs.LG` - Filter Like You Test: 数据驱动的数据过滤方法用于CLIP预训练 [PDF](https://arxiv.org/pdf/2503.08805), [HTML](https://arxiv.org/abs/2503.08805)
### Authors
Mikey Shechter,Yair Carmon
### Background
为了提高大型视觉-语言数据集的质量，研究人员开发了多种过滤算法，旨在提升模型在下游任务中的表现。此前的方法大多依赖人工设定的规则或固定的方法过滤数据点，缺乏灵活性和自适应性。
### Innovation
FLYT算法是一个学习识别每个数据点作为预训练示例有用性的方法。它通过下游任务的梯度信号训练评分模型，极大提升了数据过滤的效果。M-FLYT进一步整合了来自不同评分方法的分数，形成统一的评分机制。此外，通过Soft Cap Sampling (SCS)策略，FLYT能够生成多样化的预训练数据集，避免了数据点的过度代表。
### Conclusion
论文提出了FLYT算法，通过在预训练过程中利用评分模型，能够显著提升模型在零样本ImageNet分类任务上的性能，并且超过之前所有使用仅公共资源的方法。通过对DataComp基准测试中的多个评估任务，FLYT和M-FLYT方法的表现也显示出显著的优势。
## 880. `cs.LG` - CAPability: 一个全面的视觉标题基准，用于评估正确性和完整性 [PDF](https://arxiv.org/pdf/2502.14914), [HTML](https://arxiv.org/abs/2502.14914)
### Authors
Zhihang Liu,Chen-Wei Xie,Bin Wen,Feiwu Yu,Jixuan Chen,Pandeng Li,Boqiang Zhang,Nianzu Yang,Yinglu Li,Zuan Gao,Yun Zheng,Hongtao Xie
### Background
视觉描述基准已经过时，因为现代多模态大型语言模型（MLLMs）的出现使得简短的地面真实句子和传统评估指标无法有效评估细节描述。尽管最近的基准试图通过关注关键词提取或对象中心评估来处理这一问题，但它们仍然局限于模糊视图或对象视图分析，且对视觉元素的覆盖不完整。
### Innovation
CAPability是一个全面的多视图基准，用于跨12个维度评估视觉描述，涵盖六个关键视图。它包含了近11,000个人工注释的图像和视频，并带有视觉元素注释，用于评估生成的描述。CAPability通过使用精度和命中率指标稳定评估描述的正确性和完整性。此外，通过将注释转换为问答对，引入了一个启发式指标，即‘知道但不能表达’（Kbar{T}），指出问答能力和描述能力之间存在显著差距。这一工作全面分析了MLLMs的描述能力，识别了其强项和弱点，指导未来研究以增强其特定方面。
### Conclusion
我们的工作为MLLMs的描述能力提供了一个全面的分析，识别了不同维度中的强项和弱点，指导未来研究提升其特定方面的性能。
## 881. `cs.LG` - 揭秘谱特征学习在工具变量回归中的作用 [PDF](https://arxiv.org/pdf/2506.10899), [HTML](https://arxiv.org/abs/2506.10899)
### Authors
Dimitri Meunier,Antoine Moulin,Jakub Wornbard,Vladimir R. Kostic,Arthur Gretton
### Background
本文解决在存在隐藏混杂变量的情况下因果效应估计的问题，采用非参数工具变量（IV）回归方法。最新的策略使用了谱特征，即治疗与工具之间的运算符的高阶特征子空间。作者通过推导基于谱特征的两阶段最小二乘估计的泛化误差边界，以及探讨该方法的性能和失效模式，为理解这种方法提供了一般性的见解。
### Innovation
作者推导了基于谱特征的两阶段最小二乘估计的泛化误差边界，并揭示了影响该方法性能的两个关键因素，从而提出了一个明确的结果分类。研究者还介绍了一种实用方法来从数据中估计这些谱属性，帮助实践者诊断其所在的操作区间。此外，作者还通过合成实验验证了这一分类方法的有效性。
### Conclusion
研究识别了三种不同的结果场景：良好的情况下，方法是理想的；糟糕的情况下，虽然谱对齐保持强大，但由于仪器较弱导致需要更多样本；丑陋的情况下，由于谱对齐弱导致方法失败。作者还展示了该方法在dSprites数据集上的应用，证明了其实际效用。
## 882. `cs.LG` - 知识图谱检索中的内容-结构权衡 [PDF](https://arxiv.org/pdf/2506.13380), [HTML](https://arxiv.org/abs/2506.13380)
### Authors
Valentin Six,Evan Dufraisse,Gaël de Chalendar
### Background
大型语言模型（LLMs）越来越多地依赖知识图谱进行事实推理，但检索设计如何影响其性能仍不明确。本文探讨了问题分解如何改变检索到的子图的内容和结构，并提出了一个混合检索函数，用于控制初始问题和子问题的重要性。
### Innovation
本文通过混合检索函数研究了知识图谱检索中的内容-结构权衡，并发现基于子问题的检索能提高内容的精确度，但会导致不连贯的子图；而基于问题的检索能够保持结构但可能牺牲相关性。这种权衡揭示了平衡检索内容和结构是有效利用结构性知识进行LLM推理的关键。
### Conclusion
在内容和结构之间的最佳平衡是实现LLM在结构化知识上的有效推理的关键。
## 883. `cs.LG` - AI中的严谨性：实施严谨的AI工作需要一个更广泛且负责任的人工智能导向的严谨性概念 [PDF](https://arxiv.org/pdf/2506.14652), [HTML](https://arxiv.org/abs/2506.14652)
### Authors
Alexandra Olteanu,Su Lin Blodgett,Agathe Balayn,Angelina Wang,Fernando Diaz,Flavio du Pin Calmon,Margaret Mitchell,Michael Ekstrand,Reuben Binns,Solon Barocas
### Background
在AI研究和实践中，严谨性主要被理解为方法论严谨性，即数学、统计或计算方法是否被正确应用。这种狭隘的理解导致了负责任AI社区所提出的一些担忧，比如对AI系统能力的夸大宣传。
### Innovation
本文提出了一个更广泛的严谨性定义，包括方法论严谨性之外的六个方面：背景知识、规范严谨性、概念严谨性、报告严谨性和解释严谨性。这为研究人员、政策制定者、记者和其他利益相关者提供了有用的术语和框架来进行关于AI工作的必要对话。
### Conclusion
需要一个更广泛且负责任的人工智能导向的严谨性概念。这种更广泛的严谨性不仅涵盖更广泛的背景知识、规范、概念、报告和解释，还强调了理解AI工作所必需的各方面严谨性。
## 884. `cs.LG` - CoMind：迈向以社区为驱动的机器学习工程智能代理 [PDF](https://arxiv.org/pdf/2506.20640), [HTML](https://arxiv.org/abs/2506.20640)
### Authors
Sijie Li,Weiwei Sun,Shanda Li,Ameet Talwalkar,Yiming Yang
### Background
大型语言模型（LLM）代理在自动化机器学习（ML）工程方面显示出潜力。然而，现有的代理通常孤立地处理特定的研究问题，而不与更广泛的科研社区互动，而科研人员常常通过分享知识获得见解和贡献。本文旨在通过介绍一种新的评估框架——MLE-Live，来解决这个问题。MLE-Live框架旨在评估代理与模拟的Kaggle研究社区进行沟通和利用集体知识的能力。
### Innovation
本文提出了CoMind，一种多代理系统，旨在积极整合外部知识。CoMind采用迭代并行探索机制，同时开发多个解决方案，以平衡探索的广度与实现的深度。在MLE-Live框架下，CoMind在75场过去的Kaggle竞赛中表现出色，取得了36%的奖牌率，并创下了新的基准。更重要地，在八个实际进行中的竞赛中，CoMind平均优于92.6%的人类竞争者，在官方排行榜上名列前茅。
### Conclusion
CoMind通过与模拟Kaggle社区的互动，显著提高了自动化机器学习工程的能力，在多个实际竞赛中表现出色，证明了其作为社区驱动型代理的潜力。
## 885. `cs.LG` - 动态ε调度：面向对抗训练的多因素自适应扰动预算 [PDF](https://arxiv.org/pdf/2506.04263), [HTML](https://arxiv.org/abs/2506.04263)
### Authors
Alan Mitkiy,James Smith,Myungseo wong,Hana Satou,Hiroshi Tanaka,Emily Johnson
### Background
现有的对抗训练方法依赖于固定的扰动预算，忽略了实例特定的鲁棒性特征，这限制了它们的有效性。尽管IAAT和MMA等先前工作引入了实例级别的适应性，但它们通常依赖于启发式或静态的数据鲁棒性近似。
### Innovation
提出了动态ε调度（DES），这是一种新颖的框架，能够根据每个实例和每个训练迭代自适应调整对抗扰动预算。DES结合了三种关键因素：基于梯度代理估计的决策边界距离、来自softmax熵的预测置信度以及通过蒙特卡洛失辍落估计的模型不确定性，从而动态地调整扰动预算以引导更有效的对抗学习。
### Conclusion
实验结果表明，与固定ε基线和先前的自适应方法相比，本方法能一致地提高对抗鲁棒性和标准准确性。此外，本工作还提供了调度策略的理论洞察，这为基于数据驱动、实例感知的对抗训练方法开辟了新的途径。
## 886. `cs.LG` - 使用散列水印作为滤波器：在基于权重的神经网络水印中击败伪造和覆盖攻击 [PDF](https://arxiv.org/pdf/2507.11137), [HTML](https://arxiv.org/abs/2507.11137)
### Authors
Yuan Yao,Jin Song,Jian Jin
### Background
作为有价值的数字资产，深度神经网络需要强大的所有权保护，因此神经网络水印（NNW）成为一种有前景的解决方案。在各种NNW方法中，基于权重的方法因其简单性和实用性而受到青睐，但仍然容易遭受篡改和覆盖攻击。
### Innovation
我们提出了NeuralMark，这是一种基于散列水印滤波器的鲁棒方法。具体来说，我们使用哈希函数从秘密密钥生成一个不可逆的二进制水印，并将其用作选择嵌入模型参数的滤波器。此设计巧妙地将嵌入参数与散列水印交织在一起，提供了防范篡改和覆盖攻击的 robust 防御。额外加入的平均池化操作可抵抗微调和剪枝攻击。此外，它能够无缝地集成到各种神经网络架构中，确保广泛的适用性。
### Conclusion
在理论上，我们分析了其安全性边界。从实证上，我们在涵盖13种不同卷积和Transformer架构的13个图像分类任务和一个文本生成任务中验证了其有效性和鲁棒性。代码源代码可在以下链接中获取：this https URL.
## 887. `cs.LG` - 矩阵去噪模型中奇异子空间估计的极值理论 [PDF](https://arxiv.org/pdf/2507.19978), [HTML](https://arxiv.org/abs/2507.19978)
### Authors
Junhyung Chang,Joshua Cape
### Background
本文研究了在矩阵去噪模型中细粒度奇异子空间估计的问题。在这个模型中，一个确定性低秩信号矩阵被高斯噪声的随机矩阵所叠加。研究了信号矩阵与噪声矩阵相互作用下的统计性质，并特别关注了确定性低秩信号结构在主奇异向量中的检验。
### Innovation
本文提出了利用高阶范数（两范性范数）在矩阵去噪模型中进行假设检验的方法，相较于使用弗罗贝尼乌斯范数子空间距离，这种方法在检测特定结构的备择假设时更具有统计功效。研究采用了行向量扰动分析、极值理论、鞍点逼近方法和随机矩阵理论等多种技术相结合的方法，建立了大矩阵情况下核子空间误差的渐近理论。
### Conclusion
本文通过新颖的合成分析方法，阐述了基于矩阵去噪模型中的奇异子空间估计理论。提出了一种基于高阶范数差异的新型检验统计量，该统计量在检测特定结构备择假设时表现更优。结果通过数值模拟验证，并展示了检验程序对非高斯噪声分布的稳健性。本文的研究成果补充了矩阵去噪领域的现有文献，并为该领域的进一步研究提供了新的理论基础。
## 888. `cs.LG` - 整合电子健康记录数据的通用管道以进行转化研究 [PDF](https://arxiv.org/pdf/2509.08553), [HTML](https://arxiv.org/abs/2509.08553)
### Authors
Jessica Gronsbell,Vidul Ayakulangara Panickan,Doudou Zhou,Chris Lin,Thomas Charlon,Chuan Hong,Xin Xiong,Linshanshan Wang,Jianhui Gao,Shirley Zhou,Yuan Tian,Yaqi Shi,Ziming Gan,Tianxi Cai
### Background
尽管电子健康记录（EHR）数据的可用性在不断增长，但研究人员在有效利用这些数据进行转化研究时仍然面临着复杂性、异质性和标准化工具及文档缺乏带来的重大障碍。
### Innovation
我们引入了PEHRT（通用EHR数据整合管道），这是一个全面的、可直接使用的资源，其中包括开源代码、可视化工具和详细的文档，以简化准备EHR数据进行分析的过程。该管道提供了工具来将结构化和非结构化的EHR数据标准化到标准化本体，以确保多种编码系统之间的一致性。在存在未映射或异质本地代码的情况下，PEHRT进一步利用表征学习和预训练语言模型生成强大的嵌入，捕捉各站点之间的语义关系，减轻异质性并使下游分析得以整合。PEHRT还支持跨机构的共训练，通过共享表征允许参与机构协作细化嵌入并增强泛化能力，而无需共享个体级数据。该框架是数据模型无关的，可以无缝部署在各种卫生系统中，生成相互操作的研究级数据集。通过降低基于EHR的研究的技术障碍，PEHRT使研究者能够将原始临床数据转化为可重复、可供分析的研究资源，用于发现和创新。
### Conclusion
由PEHRT降低的技术障碍使研究者能够将原始临床数据转化为可重复、可供分析的研究资源，从而促进发现和创新。
## 889. `cs.LG` - 在队列控制中的有限时间最小最大界和最优Lyapunov策略 [PDF](https://arxiv.org/pdf/2506.18278), [HTML](https://arxiv.org/abs/2506.18278)
### Authors
Yujie Liu,Vincent Y. F. Tan,Yunbei Xu
### Background
本文介绍了有限时间内队列控制的最小最大框架，并提出了一种基于Lyapunov的简便调度策略，该策略在有限时间内具有出色的表现。该框架定量地表征了期望总队列长度如何与调度集容量和队列之间到达和离开的可变性等关键系统参数相关。据我们所知，这是首次为评估和比较有限时间内（包括非平稳设置）的各种调度策略提供了坚实的理论基础，并显示出提出的策略在有限时间内可以一致地和通过实验证明优于经典的MaxWeight。
### Innovation
本文提出了一个新的基于Lyapunov的调度策略LyapOpt，它最小化了包含一阶和二阶项的全二次Lyapunov漂移，从而在繁忙交通时实现了最优的有限时间性能，同时保持了经典稳定性保证。研究还揭示了经典的MaxWeight策略的关键局限性，它仅优化了一阶漂移，因此有限时间性能对系统参数的依赖性低下，并在明确描述的环境中导致了显著更大的积压。
### Conclusion
本文的研究结果阐明了基于漂移的经典调度策略的作用范围和局限性，并推动了具有严格有限时间保证的新队列控制方法的发展。
## 890. `cs.LG` - 重新思考跨不相关类别属性泛化的所有分割都不平等 [PDF](https://arxiv.org/pdf/2509.06998), [HTML](https://arxiv.org/abs/2509.06998)
### Authors
Liviu Nicolae Fircă,Antonio Bărbălau,Dan Oneata,Elena Burceanu
### Background
现有的工作集中在属性预测的狭窄分类或视觉相似领域内，尚未明确当前模型是否能够抽取出并应用于概念上相距甚远的类别之间的共通属性。因此，有必要对属性预测任务在不同条件下的鲁棒性进行首次明确评估，特别是测试模型识别不同类别间共享属性的能力。
### Innovation
本文提出了一种新的评估策略，通过逐步降低训练集和测试集之间的相关性，引入基于语义分组、嵌入相似度阈值、嵌入聚类以及基于超类别分割的训练验证拆分策略。研究发现，这些策略显著影响了模型的表现，尤其是聚类方法在降低隐藏相关性的同时保持了可学习性。
### Conclusion
结果表明，当训练和测试类别的相关性降低时，性能会出现急剧下降，这显示了拆分设计对模型性能的影响。聚类方法在这次评估中提供了最有效的平衡，从而为未来属性推理基准的构建提供了新的见解，揭示了当前表征的局限性。
## 891. `cs.LG` - IndiSeek 学习信息引导的分离表示 [PDF](https://arxiv.org/pdf/2509.21584), [HTML](https://arxiv.org/abs/2509.21584)
### Authors
Yu Gui,Cong Ma,Zongming Ma
### Background
在多模态学习中，学习解耦表示是一个基本任务。单细胞多组学等现代应用中，共享特征和模态特定特征对于表征细胞状态和支持下游分析至关重要。理想情况下，模态特定特征应独立于共享特征，同时捕捉每个模态内的所有互补信息。这种权衡可以通过信息理论标准来自然表达，但由于互信息客观难以可靠估计，其变分替代方案在实践中往往表现不佳。
### Innovation
本文介绍了一种名为 IndiSeek 的新颖解耦表示学习方法，它通过结合一个独立性引导的目标与一个高效且能限制条件互信息的重构损失来解决这个挑战。这种形式化能够明确平衡独立性和完整性，从而允许从模态特定特征中进行有原则地提取。
### Conclusion
本文在合成模拟、CITE-seq 数据集和多个真实世界的多模态基准上展示了 IndiSeek 的有效性。
## 892. `cs.LG` - PointNSP: 基于下一尺度层次细节预测的自回归3D点云生成 [PDF](https://arxiv.org/pdf/2510.05613), [HTML](https://arxiv.org/abs/2510.05613)
### Authors
Ziqiao Meng,Qichao Wang,Zhiyang Dou,Zixing Song,Zhipeng Zhou,Irwin King,Peilin Zhao
### Background
尽管自回归模型在点云生成方面已经取得了显著进展，但其生成质量仍然落后于基于扩散的方法。这种性能差距源于自回归模型对原本无序的点集施加的人工顺序限制，迫使形状生成按照局部预测序列进行。这种顺序偏差强调了短程连续性，但削弱了模型捕捉远程依赖性的能力，阻碍了其对全局结构性质如对称性、稳定的拓扑结构和大尺度几何规律的约束。
### Innovation
我们受到了形状建模中层次细节（LOD）原则的启发，提出了PointNSP，这是一种从粗到细的生成框架。该框架在低分辨率下保持全局形状结构，并通过下一尺度预测范式在更高尺度下逐步细化细粒度几何形状。这种多尺度因子分解将自回归目标与点集的置换不变性质相协调，促进了在不同尺度内的丰富交互，并避免了固定的顺序约束。实验结果表明，PointNSP首次在自回归范式中建立了最先进的生成质量，并且在参数、训练和推理效率方面都超过了强大的基于扩散的基线。特别地，在密集生成8,192个点的情况下，PointNSP的优势更加突出，突显了其扩展潜力。
### Conclusion
实验结果表明，PointNSP在自回归范式中建立了最先进的生成质量，并且在参数、训练和推理效率方面都超过了强大的基于扩散的基线。特别地，在密集生成8,192个点的情况下，PointNSP的优势更加突出，突显了其扩展潜力。
## 893. `cs.LG` - LightMem：轻量且高效的增强型记忆生成系统 [PDF](https://arxiv.org/pdf/2510.18866), [HTML](https://arxiv.org/abs/2510.18866)
### Authors
Jizhan Fang,Xinle Deng,Haoming Xu,Ziyan Jiang,Yuqi Tang,Ziwen Xu,Shumin Deng,Yunzhi Yao,Mengru Wang,Shuofei Qiao,Huajun Chen,Ningyu Zhang
### Background
尽管大型语言模型（LLMs）具有出色的能力，但在动态和复杂的环境中，它们难以有效地利用历史交互信息。现有的记忆系统引入了持久的信息存储、检索和利用机制，使LLMs能够超越无状态交互，但这些系统往往增加了大量的时间和计算开销。
### Innovation
本文介绍了一种名为LightMem的新记忆系统，它在性能和效率之间寻求平衡。LightMem受人类记忆的Atkinson-Shiffrin模型启发，将记忆组织成三个互补阶段：首先，基于认知的感官记忆通过轻量级压缩快速过滤无关信息，并按主题分组信息；其次，话题意识的短期记忆将基于主题的组凝聚起来，组织和总结内容，以便更具结构化访问；最后，具有睡眠更新的长期记忆采用离线过程，将凝聚操作与在线推理脱钩。
### Conclusion
在LongMemEval和LoCoMo上使用GPT和Qwen作为主干，LightMem在各种指标上均优于强大的基线模型，如问答准确性提高至7.7% / 29.3%，总token使用量降低至38倍 / 20.9倍，API调用次数减少至30倍 / 55.5倍，完全在线的测试时成本进一步降低，token减少至106倍 / 117倍，API调用次数减少至159倍 / 310倍。代码开源可供查看。
## 894. `cs.LG` - Decorrelation Speeds Up Vision Transformers [PDF](https://arxiv.org/pdf/2510.14657), [HTML](https://arxiv.org/abs/2510.14657)
### Authors
Kieran Carrigg,Rob van Gastel,Melda Yeghaian,Sander Dalm,Faysal Boughorbel,Marcel van Gerven
### Background
掩码自编码器（MAE）预训练的视觉transformer (ViT) 在少量标签数据场景下表现出色，但计算成本高，不适合时间与资源受限的工业环境。
### Innovation
通过将去相关反向传播（DBP）整合到MAE预训练中，该方法通过迭代减少每一层的输入相关性以加速收敛，特别应用于编码器时，能够快速预训练同时保持稳定性。在ImageNet-1K预训练和ADE20K微调的随机子集评估中，DBP-MAE将基线性能下的实际时间减少21.1%，降低碳排放21.4%，同时提高分割mIoU 1.1个百分点。在专用工业数据预训练和微调中也看到了类似收益，证明了该方法在实际场景中的适用性。
### Conclusion
这些结果表明，DBP可以在大规模ViT预训练过程中减少训练时间和能源消耗，同时提高下游任务的表现。
## 895. `cs.LG` - 使用结合卷积和点云架构重建局部密度场 [PDF](https://arxiv.org/pdf/2510.08573), [HTML](https://arxiv.org/abs/2510.08573)
### Authors
Baptiste Barthe-Gold,Nhat-Minh Nguyen,Leander Thiele
### Background
本文介绍了一种利用线视特殊速度（LOS peculiar velocities）来重建暗物质局部密度场的方法，这些速度是暗物质场的不规则追踪器。传统的单一U-Net方法在这种任务上表现不佳。
### Innovation
本文提出了一种结合了卷积缩放U-Net（UNet）和点云DeepSets的神经网络架构。这种新架构能够更有效地利用小尺度信息并提高重建质量。特别是在小尺度上，该混合网络比单独使用U-Net恢复了更多的聚类幅度和相位。
### Conclusion
通过使用结合卷积和点云架构的神经网络，本文模型在局部暗物质密度场的重建质量上取得了显著的提高。
## 896. `cs.LG` - CAMERA: 通过微专家冗余分析对MoE模型进行多矩阵联合压缩 [PDF](https://arxiv.org/pdf/2508.02322), [HTML](https://arxiv.org/abs/2508.02322)
### Authors
Yuzhuang Xu,Xu Han,Yuanchi Zhang,Yixuan Wang,Yijun Liu,Shiyu Ji,Qingfu Zhu,Wanxiang Che
### Background
大规模语言模型（LLMs）使用混合专家（MoE）架构，在各种任务中的性能随着参数数目的增加而显著提升，但仍面临计算和存储开销大的问题。尽管过去的尝试通过在专家级别进行剪枝、合并或分解来减少参数，但这些方法在保持性能和计算效率方面仍然存在问题。
### Innovation
本文通过引入微专家作为跨越矩阵的更细粒度压缩单元，首次将MoE层视为微专家的混合，并提出了无需训练的轻量级框架CAMERA以识别微专家冗余。作者还提出了基于此分析的结构化微专家剪枝框架CAMERA-P和混合精度量化方法CAMERA-Q。实验结果表明CAMERA-P在不同的剪枝比率下优于强baseline，CAMERA-Q在激进的2位量化下取得了优于现有矩阵和信道级别的方法。
### Conclusion
我们的方法在单块NVIDIA A100-40GB GPU上均可在不到5分钟内完成对Qwen2-57B-A14B的完整微专家分析，并在九个下游任务上展示了出色的性能。
## 897. `cs.LG` - Augur：通过大型语言模型建模时间序列的协变量因果关联 [PDF](https://arxiv.org/pdf/2510.07858), [HTML](https://arxiv.org/abs/2510.07858)
### Authors
Zhiqing Cui,Binwu Wang,Qingxiang Liu,Yeqiang Wang,Zhengyang Zhou,Yuxuan Liang,Yang Wang
### Background
大型语言模型（LLM）已展现出用于时间序列预测的潜力，能够整合多模态数据。然而，现有的基于LLM的方法存在显著的局限性，如在模型架构中角色边缘化、依赖粗略的统计文本提示以及缺乏可解释性。
### Innovation
Augur引入了一种完全由LLM驱动的时间序列预测框架，通过利用LLM因果推理来发现和使用协变量之间的定向因果关联。这种框架使用了一种两阶段的教师学生架构，强力的教师LLM通过启发式搜索和两两因果测试从时间序列中推断出定向图，轻量级的学生代理进一步细化图形并在高信心的因果关联上进行微调，这些关联被编码为丰富的文本提示以执行预测。
### Conclusion
在26个基线和现实世界数据集上的广泛实验表明，Augur在性能上具有竞争力，并具有稳健的零样本泛化能力。
## 898. `cs.LG` - 免费的拟似鲁棒性？基于基准重新审视训练 [PDF](https://arxiv.org/pdf/2511.01724), [HTML](https://arxiv.org/abs/2511.01724)
### Authors
Yi Zhang,Zheng Wang,Zhen Chen,Wenjie Ruan,Qing Guo,Siddartha Khastgir,Carsten Maple,Xingyu Zhao
### Background
深度学习模型对不可感知的扰动非常敏感。大部分现有研究集中在对抗鲁棒性(AR)，它通过检查确定性的对抗样本(AEs)存在性来评估模型在最坏情况下的性能。相比之下，拟似鲁棒性(PR)则从统计学视角出发，测量在随机扰动下预测保持正确的概率。尽管PR被认为是对AR的一种实用补充，但专门提升PR的方法仍处于较早期的发展阶段，尽管已有进步。PR-目标训练方法目前面临着三项主要的局限性：缺乏可比化的评估标准、与强大的对抗训练(AT)基准的有限比较，以及无法统一比较这些方法的一般性。
### Innovation
该研究引入了PRBench，这是第一个专注于评估不同鲁棒性训练方法提高拟似鲁棒性的基准。PRBench使用全面的评估指标（包括干净准确率、拟似鲁棒性性能、对抗鲁棒性性能、训练效率和泛化误差）来实证比较常见的AT和PR-目标训练方法，并提供了不同训练方法对拟似鲁棒性性能的泛化误差的理论分析。该研究发现，对抗训练方法在各种超参数设置下提升AR和PR性能的灵活性超过了PR-目标训练方法，而PR-目标训练方法则在泛化误差和干净准确率方面表现更好。
### Conclusion
该研究揭示了PRBench的主要发现：对抗训练方法在各种超参数设置下提高AR和PR性能的灵活性超过了PR-目标训练方法，而PR-目标训练方法则在泛化误差和干净准确率方面表现更好。此外，研究还提供了涵盖7个数据集和10个模型架构的222个训练模型的公开排行榜，可以访问这里：[这个链接](this https URL)。
## 899. `cs.LG` - MoEGCL: Mixture of Ego-Graphs Contrastive Representation Learning for Multi-View Clustering [PDF](https://arxiv.org/pdf/2511.05876), [HTML](https://arxiv.org/abs/2511.05876)
### Authors
Jian Zhu,Xin Zou,Jun Sun,Cheng Luo,Lei Liu,Lingfang Zeng,Ning Zhang,Bian Wu,Chang Tang,Lirong Dai
### Background
近年来，图神经网络（GNNs）在多视图聚类（MVC）领域取得了显著进展。不过，现有方法在图融合方面存在‘粗粒度’的问题。具体来说，大多数方法为每个视图生成独立的图结构，然后在视图层面进行加权融合，这种方式较为粗略。
### Innovation
针对这个问题，我们提出了一种新颖的Ego图混合对比表示学习（MoEGCL）。具体而言，我们提出了一种创新性的Ego图混合（MoEGF），在样本层面，而非传统的视图层面，使用专家混合网络实施细粒度的Ego图融合。此外，我们还提出了Ego图对比学习（EGCL）模块，以将融合后的表示与视图特定的表示对齐，进一步增强相同聚类内样本的表示相似性。
### Conclusion
广泛的实验表明，MoEGCL在深度多视图聚类任务中取得了最先进的效果。源代码可以在该网址公开获取。
## 900. `cs.LG` - 通过前瞻性学习与控制实现未来最佳控制 [PDF](https://arxiv.org/pdf/2511.08717), [HTML](https://arxiv.org/abs/2511.08717)
### Authors
Yuxin Bai,Aranyak Acharyya,Ashwin De Silva,Zeyu Shen,James Hassett,Joshua T. Vogelstein
### Background
当前针对未来控制问题的方法通常基于强化学习（RL），而RL在非稳态、无需重置的环境中并不适用，它的实用性受到了限制。传统上，监督学习一直是最近AI成就的主要推动力，但与RL的数学特性不同，这限制了监督学习在这些环境中的应用。
### Innovation
本文扩展了监督学习，提出了一种名为‘前瞻性学习与控制’（PL+C）的新框架。该框架证明，基于某些相当一般的假设，经验风险最小化（ERM）能够渐近达到贝叶斯最优策略。此外，研究还特定地考虑了非稳态、无重置环境中的觅食任务，并展示了现代RL算法在这些环境中学习效率低下的问题，即使经过修改，它们的效果仍远逊于前瞻性的觅食代理。
### Conclusion
PL+C框架能够在非稳态、无需重置的环境中实现高效的控制学习，这是传统强化学习方法所不具备的。现代RL算法在这些复杂环境中的表现远不如采用前瞻性学习与控制方法的代理。
## 901. `cs.SE` - DUALGUAGE: 自动化联合安全-功能基准测试以实现安全代码生成 [PDF](https://arxiv.org/pdf/2511.20709), [HTML](https://arxiv.org/abs/2511.20709)
### Authors
Abhijeet Pathak,Suvadra Barua,Dinesh Gudimetla,Rupam Patir,Jiawei Guo,Hongxin Hu,Haipeng Cai
### Background
随着大型语言模型（LLMs）和自主编程代理在软件生成中的应用越来越广泛，一个核心要求仍然未得到满足：即在不牺牲功能性正确性的情况下，保证生成的代码的安全性。现有的安全代码生成基准和评估方法存在不足，它们主要衡量漏洞减少的情况，忽视了正确性的保留，或者在不同的数据集上分别评估安全性和功能性，违背了同时联合评估的必要性。
### Innovation
本文介绍了DUALGAUGE，这是第一个全自动基准测试框架，旨在严格评估LLM生成代码的安全性和正确性。我们还提出了DUALGAUGE-BENCH，这是一个精心策划的基准套件，其中包括各种编程任务，每个任务都配有一个经过手动验证的安全性和功能性测试套件，旨在充分覆盖规格需求。DUALGAUGE的核心是一个代理型程序执行器，它在沙盒环境中运行程序并执行给定的测试，以及一个基于LLM的评估器，它根据预期结果评估正确性和漏洞行为。
### Conclusion
我们对DUALGAUGE-BENCH和DUALGAUGE的质量进行了严格的评估，并在DUALGAUGE-BENCH上对十种领先的LLM进行了数千种测试场景的基准测试。结果显示，这些LLM在正确和安全的代码生成方面存在重大缺口，我们开源的系统和数据集将通过可重复、可扩展和严格的评估加速相关进展。
## 902. `cs.SE` - Train While You Fight -- 技术要求先进的分布式学习平台 [PDF](https://arxiv.org/pdf/2511.20813), [HTML](https://arxiv.org/abs/2511.20813)
### Authors
Simon Hacks
### Background
这篇论文探讨了在执行任务期间进行持续学习的思想，即'Train While You Fight' (TWYF)，而不仅限于任务前后。为了支持TWYF，论文分析了先进分布式学习（ADL）平台所需的技术要求，并研究了现有软件工程模式如何满足这些要求。
### Innovation
本文通过设计科学研究的方法，提出了-seven技术挑战-以供ADL平台解决：互操作性、适应性、多语言支持、数据安全与隐私、可扩展性、平台独立性和可模块化。同时，论文还提供了一个来自德国武装部队的实际案例来阐述这些模式。
### Conclusion
本文强调了支持TWYF所必需的技术要求，并通过使用现有的软件工程模式来解决这些要求。这为ADL平台的开发和实施提供了有价值的指导。
## 903. `cs.SE` - 代码中大型语言模型的软件设计能力的分级评估 [PDF](https://arxiv.org/pdf/2511.20933), [HTML](https://arxiv.org/abs/2511.20933)
### Authors
Mootez Saad,Boqi Chen,José Antonio Hernández López,Dániel Varró,Tushar Sharma
### Background
由于大型语言模型（LLMs）在软件工程领域的广泛应用，它们对核心软件设计概念的理解的稳健性变得不清楚。本文通过实验系统地评估LLMs对于内聚性（模块内）和耦合性（模块间）的理解。通过编程生成不佳设计的代码片段，并测试了不同指导水平下的DeepSeek-R1模型家族（14B，32B，70B），同时通过插入干扰元素来改变上下文噪声。结果显示，在理想条件下，模型在两个概念上的基础理解是稳固的，但在实际应用中，这种理解是脆弱并且不对称的。
### Innovation
本文通过实验评估了大型语言模型在软件设计概念上的理解能力，特别是内聚性和耦合性。这种评估不仅考虑了模型的基础理解能力，还考察了在不同指导水平和噪声条件下的鲁棒性。实验结果显示，模型在耦合性分析方面的表现更为脆弱，而在内聚性分析中则表现出较强的鲁棒性，但在没有指导支持的情况下会失效。
### Conclusion
虽然LLMs能够为识别设计缺陷提供可靠的辅助，但在噪声和现实场景下的自主推理能力有限，这表明需要更高效且稳健的程序理解能力来支持自动化软件开发流程。
## 904. `cs.SE` - SpaceX：利用SPACE模型探讨开发者生产力的度量指标 [PDF](https://arxiv.org/pdf/2511.20955), [HTML](https://arxiv.org/abs/2511.20955)
### Authors
Sanchit Kaul,Kevin Nhu,Jason Eissayou,Ivan Eser,Victor Borup
### Background
本实证研究通过操作化SPACE框架并运用广泛的数据仓库挖掘，揭示了单维度和确定性生产力启发式的局限性。研究使用来自开源仓库的数据集，采用严密的统计方法，如广义线性混合模型(GLMM)和RoBERTa情感分类，综合生成一个全面的多维度生产力指标。
### Innovation
研究通过分析贡献者交互的拓扑结构，证明其映射协作动力学的精确度优于传统的基于体积的度量。研究提出了一个综合生产力评分(CPS)来应对开发人员效能的异质性。
### Conclusion
分析结果表明，负面情感状态与提交频率之间存在显著的正相关关系，暗示了一种基于挫败感的迭代修复循环。研究最终提出一个综合性生产力评分(CPS)来解决开发人员效能的异质性问题。
## 905. `cs.SE` - 针对大型语言模型LLMs轻量级模型编辑以纠正过时API推荐 [PDF](https://arxiv.org/pdf/2511.21022), [HTML](https://arxiv.org/abs/2511.21022)
### Authors
Guancheng Lin,Xiao Yu,Jacky Keung,Xing Hu,Xin Xia,Alex X. Liu
### Background
大型语言模型（LLMs）在代码补全任务中表现出色，但由于训练数据的时效性限制，它们的知识库往往包含已弃用的API。这些模型生成的过时API可能在未来的第三方库版本中不再受支持。虽然可以通过重新培训模型来更新知识，但这种方式耗时且成本高昂。近期，轻量级模型编辑方法已出现，可以高效更正模型中的特定知识，但尚未明确这些方法是否能够有效更新过时API知识，并使编辑后的模型生成最新的API。为了填补这一空白，研究人员首次系统地应用了10种最先进的模型编辑技术，更新了三个LLMs（Qwen2.5-Coder、StarCoder2和DeepSeek-Coder）中的过时API知识。
### Innovation
研究引入了专门的基准测试EDAPIBench，包含超过70个来自8个流行Python库的过时API，以及3000多个编辑实例。研究表明，参数高效微调方法AdaLoRA在使编辑后的模型生成正确、更新的API方面表现出最佳性能，但在特定性（即编辑影响非目标知识）方面表现出不足。为此，研究人员提出了AdaLoRA-L，定义了“通用API层”和“特定API层”，以提高特定性并保持其他评估指标的性能相似。
### Conclusion
实验结果表明，AdaLoRA-L相比AdaLoRA显著提高了特定性，同时其他评估指标的性能保持相当。
## 906. `cs.SE` - 探索Android应用程序中的隐藏地理差异 [PDF](https://arxiv.org/pdf/2511.21151), [HTML](https://arxiv.org/abs/2511.21151)
### Authors
M. Alecci,P. Jiménez,J. Samhi,T. Bissyandé,J. Klein
### Background
尽管移动应用程序的演化已经得到了广泛关注，但应用程序在地理位置上的行为差异却鲜有被研究。研究者们对地理位置上的应用程序差异进行了大规模研究，发现了一个重要的现象：地理位置相似但包名不同的应用程序（GeoTwins），这些应用程序在请求的权限、第三方库以及隐私披露方面往往存在差异。此外，还揭示了应用程序包生态系统中的地区性差异，表明用户下载的应用行为在不同地区可能有所不同。
### Innovation
研究者们提出了一个新的概念GeoTwins，并对Android App Bundle生态系统进行了深入研究，揭示了地区性差异的实际存在。这些发现对于应用程序的安全性、隐私和功能性评估有关键影响，提出了透明性与知情同意方面的伦理问题。研究者还建立了一个分布式应用程序收集管道，并发布了一个包含81,963个GeoTwins的应用程序数据集，为未来的相关研究提供了支持。
### Conclusion
地理位置上相似的应用程序在多个方面可能存在差异，这些差异可能影响下载应用程序的安全性、隐私性和功能性的评估结果，进一步还可能引起伦理问题。研究者建议未来的评估应当考虑到这些地理差异，从而提高结果的可重复性，并减少地区性偏见。
## 907. `cs.SE` - SV-LIB 1.0：软件验证任务的标准交换格式 [PDF](https://arxiv.org/pdf/2511.21509), [HTML](https://arxiv.org/abs/2511.21509)
### Authors
Dirk Beyer,Gidon Ernst,Martin Jonáš,Marian Lingsch-Rosenfeld
### Background
在过去二十年里，已投入大量研究和开发资源用于开发适用于各种编程语言（如C、C++和Java）的验证工具。尽管很多验证方法本身是语言无关的，但仍然可以将这些工具和实现转移到其他编程和建模语言中，以扩大其应用范围。
### Innovation
提出了一种称为SV-LIB的标准交换格式和中间语言，用于软件验证任务，包括程序、规范和验证见证。SV-LIB基于命令式编程语言中的知名概念，并利用SMT-LIB表示程序中使用的所有表达式和类。SV-LIB还定义了SV-LIB程序的正确性和错误性验证者的格式，并且提供了一种指定验证任务的方法。这种方法使得独立验证证人成为可能，并且还能够重用部分验证器作为验证者的验证工具。
### Conclusion
本文介绍了SV-LIB 1.0的格式，包括设计理念，语法以及非正式语义。正式语义和并发性的进一步扩展正在未来的版本中规划。
## 908. `cs.SE` - 大型语言模型在单元测试生成中的应用：成就、挑战及未来 [PDF](https://arxiv.org/pdf/2511.21382), [HTML](https://arxiv.org/abs/2511.21382)
### Authors
Bei Chu,Yang Feng,Kui Liu,Zifan Nan,Zhaoqiang Guo,Baowen Xu
### Background
单元测试是一项极其重要的技术，但同时也是一项耗时的工作，用于验证软件和减少回归风险。尽管经典自动方法能有效探索程序结构，但在生成理想的输入和断言时通常缺乏必要的语义信息。大型语言模型通过利用其驱动的数据对代码语义和编程模式的知识来弥补这一缺陷。
### Innovation
本文进行了系统文献综述，分析了115篇于2021年5月至2025年8月间发表的文献。基于单元测试生成生命周期，提出了一种统一分类法，将大型语言模型视为需要系统工程约束的随机生成器。研究了核心生成策略和一系列增强技术，从预生成上下文丰富到生成后的质量保证。结果显示，提示工程是最重要的利用策略，涉及89%的研究，因其灵活性较高。迭代验证和修复循环已成为确保稳健可用性的标准机制，并大幅提高了编译和执行通过率。
### Conclusion
尽管取得了显著进展，但仍面临生成测试的弱故障检测能力和缺乏标准化评估基准等关键挑战。未来研究应着重于自主测试代理的发展和结合大型语言模型与传统软件工程工具的混合系统。本文为研究人员和从业者提供了一种全面的观点，将大型语言模型的潜力转化为工业级测试解决方案。
## 909. `cs.SE` - 关于减少能源消耗的微服务策略和技术的效果：一项权衡研究 [PDF](https://arxiv.org/pdf/2501.14402), [HTML](https://arxiv.org/abs/2501.14402)
### Authors
Xingwen Xiao,Chushu Gao,Justus Bogner
### Background
微服务架构已经成为软件产业的主流。然而，与可持续性相关的法规和软件日益增长的能耗成本增加了这些系统能效的重要性。尽管已有针对架构策略和模式的提案，但它们的有效性及与其他质量属性（QAs）之间的潜在权衡尚未明确。
### Innovation
使用开源在线精品店系统进行控制实验，研究微服务的策略和技术减少能耗的效果及其与性能和可维护性之间的潜在权衡。
### Conclusion
一些策略减少了能耗并改善了性能，但通常以可维护性为代价，例如通过增加代码复制和模块耦合。总体而言，所有策略在较高负载时显著减少了能耗，但大多数策略牺牲了其他质量属性。这表明真正的挑战不仅仅是减少微服务的能耗，而是实现能源效率。
## 910. `cs.SE` - 细粒度如何影响微服务的能源消耗和性能？一个受控实验 [PDF](https://arxiv.org/pdf/2502.00482), [HTML](https://arxiv.org/abs/2502.00482)
### Authors
Yiming Zhao,Tiziano De Matteis,Justus Bogner
### Background
微服务架构是一种广泛使用的软件部署方式，优点在于灵活性和可扩展性。然而，它们对能源消耗的影响尚未被充分理解，经常被性能和其他质量属性（QAs）所忽视。在这个领域，一个尚未深入研究的概念是微服务的粒度，即系统功能分布在多少个服务上。
### Innovation
本研究通过对比不同粒度级别的细粒度和能耗及响应时间的关系，以及在不同请求频率下的变化情况，研究了微服务粒度对能耗和性能的影响。使用了两个开源的微服务架构系统，并设置了三种粒度级别和五个不同的请求频率进行实验。
### Conclusion
微服务从业人员在做出与粒度相关的决策时，特别是对于大规模系统，应该考虑我们的研究结果。细粒度显著影响能量消耗和响应时间，系统的粒度、规模、能耗和性能之间的复杂关系需要仔细考虑。
## 911. `cs.SE` - 代码审查的未来之路？探索代码审查的未来 [PDF](https://arxiv.org/pdf/2508.06879), [HTML](https://arxiv.org/abs/2508.06879)
### Authors
Michael Dorner,Andreas Bauer,Darja Šmite,Lukas Thode,Daniel Mendez,Ricardo Britto,Stephan Lukasczyk,Ehsan Zabardast,Michael Kormann
### Background
代码审查一直是协作软件工程中的核心实践，但其未来的发展方向尚不明确。本文研究了专业开发人员如何体验当前的代码审查过程及其对未来五年内代码审查的预期变化。
### Innovation
研究通过对五家软件驱动公司中的100名开发人员进行问卷调查，获取了当前的审查工作量、受审查的代码片段以及其他细项，并展望了未来代码审查的趋势。受访者普遍认为，代码审查将继续保持重要性，同时LLM将成为积极的参与者。
### Conclusion
尽管代码审查将增强代码范围的全面性并保持类似的审查工作量，但新兴的AI角色可能会导致人类理解、问责制和信任的下降。因此，代码审查可以作为一种视角，使软件工程中AI面临的挑战首先显现出来。
## 912. `cs.SE` - MigGPT: 利用大型语言模型自动化迁移跨版本的Linux内核外树补丁 [PDF](https://arxiv.org/pdf/2504.09474), [HTML](https://arxiv.org/abs/2504.09474)
### Authors
Pucheng Dang,Di Huang,Dong Li,Kang Chen,Yuanbo Wen,Qi Guo,Xing Hu
### Background
内核外树补丁对适应新硬件或启用特定功能至关重要，但维护和更新这些补丁需要大量的工程经验。尽管大型语言模型在不同领域取得了显著进步，显示出其自动化迁移内核外树补丁的潜力，但研究表明，这些模型在代码上下文理解和迁移点识别方面存在不足。
### Innovation
我们提出了MigGPT框架，该框架采用了一种新颖的代码指纹结构来保留代码片段信息，并集成了三个精心设计的模块以提高内核外树补丁迁移的准确性和效率。此外，我们使用真实的内核外树补丁项目建立了一个强大的基准，以评估大型语言模型的能力。实验结果表明，MigGPT显著优于直接使用标准大型语言模型，平均完成迁移任务的率为74.07%。
### Conclusion
MigGPT框架通过利用代码指纹结构和精心设计的模块，有效提高了内核外树补丁的迁移效率和准确性。通过构建基准测试，验证了大型语言模型在内核外树补丁迁移中的实用性。
## 913. `cs.SE` - 支持研究软件的机构政策路径：全球趋势与地方实践 [PDF](https://arxiv.org/pdf/2509.26422), [HTML](https://arxiv.org/abs/2509.26422)
### Authors
Michelle Barker,Jeremy Cohen,Pedro Hernández Serrano,Daniel S. Katz,Kim Martin,Dan Rudmann,Hugh Shanahan
### Background
研究软件对现代科学至关重要，但许多进行研究的组织缺乏有力的政策来支持其发展、可持续性和认可。尽管研究软件在科研成果中扮演关键角色，但在许多科研机构中，相关人员往往被排除在科研政策之外。
### Innovation
该文章探讨了研究组织中研究软件政策的不足之处，并提出了嵌入软件到政策框架中的建议，以确保软件受到认可、得到支持并符合更广泛的研究目标。提出了一种三层框架指导政策发展：中心政策明确承认软件作为学术成果；中间层政策将相关领域如开放科学、知识产权和研究评估对齐；外围机制如指南和框架，促进实际实施。
### Conclusion
鼓励机构评估现有实践，采用国际声明，动员利益相关者推进软件认可。更强有力的机构政策能够促进良好实践、增强合作、支持可重复性，强化研究人员培养，以最大化机构价值和研究影响，并使组织成为开放、可持续、软件驱动科学的领导者。
## 914. `cs.SE` - 利用大规模语言模型进行可靠可验证电子表格代码生成：一种研究框架 [PDF](https://arxiv.org/pdf/2510.15585), [HTML](https://arxiv.org/abs/2510.15585)
### Authors
Simon Thorne,Advait Sarkar
### Background
大型语言模型（LLMs），如ChatGPT，被广泛用于生成传统软件代码和电子表格逻辑。尽管这些模型在生成方面表现出色，但它们经常出现关键问题，比如幻觉、细微的逻辑不一致以及语法错误，这种风险在财务建模和科学研究等高风险领域尤其严重，这些领域对准确性和可靠性有严格要求。
### Innovation
本文提出了将测试驱动开发（TDD）与大型语言模型（LLM）生成相结合的结构化研究框架，旨在提升生成输出的正确性、可靠性和用户信心。该框架在电子表格公式生成、Python脚本语言直至强类型语言Rust的多种编程环境中适用，包括详细阐述的实验设计、明确的参与者分组、评估指标以及基于TDD的示例。
### Conclusion
通过强调测试驱动思考，旨在提升计算思维、提示工程技能和用户参与，特别有利于经常缺乏正式编程培训的电子表格用户。作者呼吁合作，以改进和实证评估此方法，最终目标是建立负责可靠的LLM整合，在教育和职业发展中具有重要意义。
## 915. `cs.SE` - Bug侦探和质量教练：开发人员对辅助IDE工具的心理模型 [PDF](https://arxiv.org/pdf/2511.21197), [HTML](https://arxiv.org/abs/2511.21197)
### Authors
Paolo Buono,Mary Cerullo,Stefano Cirillo,Giuseppe Desolda,Francesco Greco,Emanuela Guglielmi,Grazia Margarella,Giuseppe Polese,Simone Scalabrino,Cesare Tucci
### Background
AI辅助工具支持开发者执行诸如bug检测和代码可读性评估等认知密集型任务。尽管这些工具的技术特性有所提升，但开发人员如何心理建模它们以及不匹配如何影响信任、控制和采纳尚不清楚。
### Innovation
该研究通过6场共设工作坊收集了58名开发人员对面板信工具的心理模型，发现开发人员将bug检测工具视为“bug侦探”，提供透明、可操作的反馈和信心提示；将可读性评估工具视为“质量教练”，提供上下文的、个性化的和渐进的指导。研究还提炼出了一套旨在平衡干扰与支持、简洁与深度、自动化与人类代理的人本化AI设计原则。
### Conclusion
研究结果指出了影响开发人员对AI辅助IDE工具信任、控制和采用的因素，并提出了若干设计原则，以平衡技术的支持性和用户的人类代理感。
## 916. `cs.SE` - 基础设施重建项目管理中机器学习的应用 [PDF](https://arxiv.org/pdf/2511.20916), [HTML](https://arxiv.org/abs/2511.20916)
### Authors
Illia Khudiakov,Vladyslav Pliuhin,Sergiy Plankovskyy,Yevgen Tsegelnyk
### Background
本文旨在描述一个适应性决策支持模型，以提高工程项目重建计划管理的效率。该研究分析了现有的适应性项目管理工具，强调使用基础设施系统建模工具来构建项目的架构和工作分解结构（WBS）。现有的模型和建模方法被审视，机器学习和人工神经网络被选为模型的基础。
### Innovation
本文的主要创新在于提出了一种适应性的决策支持模型，该模型利用机器学习方法预测目标函数在给定系统配置下的值，为决策制定提供了支持。模型的参数可以根据选定的对象类型进行调整，以适应现有项目实施目标。所描述的神经网络参数及评估结果给出了具体的应用实例。
### Conclusion
该模型的应用可以管理涉及各种工程系统（如供热、供气、供电、供水和排水系统等）的重建项目。通过在微软 Azure 机器学习工作室中进行的功能组合，该模型的神经网络参数和评估结果被展示出来，为实际项目管理提供了指导。
## 917. `cs.LG` - DR Tulu: Reinforcement Learning with Evolving Rubrics for Deep Research [PDF](https://arxiv.org/pdf/2511.19399), [HTML](https://arxiv.org/abs/2511.19399)
### Authors
Rulin Shao,Akari Asai,Shannon Zejiang Shen,Hamish Ivison,Varsha Kishore,Jingming Zhuo,Xinran Zhao,Molly Park,Samuel G. Finlayson,David Sontag,Tyler Murray,Sewon Min,Pradeep Dasigi,Luca Soldaini,Faeze Brahman,Wen-tau Yih,Tongshuang Wu,Luke Zettlemoyer,Yoon Kim,Hannaneh Hajishirzi,Pang Wei Koh
### Background
现有的深度研究模型通过强化学习和可验证奖励（RLVR）进行训练，用以解决简短且易于验证的问题-答案任务，但这种方法不适用于现实中的长篇复杂任务。
### Innovation
引入了强化学习与不断进化的评分标准（RLER），这种方法在训练过程中构建和维护评分标准，使其能够随模型探索新的信息而演变，提供具有区分性的、策略上的反馈。通过这种方法，开发了DR Tulu-8B，这是首个直接训练用于开放式、长篇深度研究的开源模型。
### Conclusion
DR Tulu在科学、医疗和一般领域的四个长篇深度研究基准测试中表现优异，超出其他开源深度研究模型，并达到或超过了专有深度研究系统的性能标准，同时在每次查询上成本更低、规模更小。为了促进未来的相关研究，我们已经发布了所有数据、模型和代码，包括新的基于MCP的深度研究系统代理基础设施。
## 918. `cs.LG` - 量子神经网络(QNNs)周期函数逼近速率通过Jackson不等式 [PDF](https://arxiv.org/pdf/2511.16149), [HTML](https://arxiv.org/abs/2511.16149)
### Authors
Ariel Neufeld,Philipp Schmocker,Viet Khoa Tran
### Background
量子神经网络(QNNs)是类比经典神经网络的量子计算模型，通过可训练的单位矩阵表示。受经典神经网络具有可以在欧几里得空间的紧集中均匀逼近任意连续函数的通用逼近特性的启发，近期一些研究表明QNNs也具备类似的性质，从单量子比特到多量子比特，甚至混合经典-量子模型。本研究关注QNNs对于周期函数的逼近能力，使用Jackson不等式通过其逼近的三角多项式来实现。
### Innovation
通过Jackson不等式，采用合适的QNN实现给定函数的逼近。特别地，通过对周期函数进行限制，可以实现参数数量的平方减少，从而获得比现有文献更好的逼近效果。函数越光滑，所需参数越少。
### Conclusion
QNNs在对周期函数进行逼近时，能够实现参数数量的大幅减少，尤其对于光滑度高的函数，能够用更少的参数得到更好的逼近效果。
## 919. `cs.SE` - 从代码异味到最佳实践：应对PyTorch、TensorFlow和Keras中的资源泄漏 [PDF](https://arxiv.org/pdf/2511.15229), [HTML](https://arxiv.org/abs/2511.15229)
### Authors
Bashar Abdallah,Martyna E. Wojciechowska,Gustavo Santos,Edmand Yu,Maxime Lamothe,Alain Abran,Mohammad Hamdaqa
### Background
当前的机器学习（ML）研究主要关注模型性能指标，而较少关注ML应用的长期可持续性和资源效率。尽管高性能是必要的，但高效的资源管理对于可靠的部署也同样关键。为了填补这一空白，本研究系统地鉴别出导致ML应用资源泄露的代码异味，并开展了实证研究，调查了开发者讨论和实际代码片段。研究结果确定了30种与PyTorch相关的代码异味和16种与TensorFlow/Keras相关的代码异味，这些异味按其根本原因和通用ML异味与框架特定特征的方式进行了分类。每个代码异味都产生了一个以上最佳实践，形成了50种旨在减少资源泄露和提高效率的编码模式。
### Innovation
本研究首次全面地检查了主要ML框架中导致资源泄漏的代码异味，并提出了可操作的最佳实践来减轻这些泄漏问题。这些贡献支持开发者构建更加高效和可持续的ML应用，并为资源泄漏的根本原因提供了一个结构化的视角。
### Conclusion
通过三阶段验证过程（包括三人独立分析及共识讨论），本研究确保了发现的验证性。研究结果为开发者提供了减少ML应用中资源泄漏的最佳实践，促进了ML应用的高效和可持续发展。
## 920. `cs.LG` - PaTAS：使用主观逻辑在神经网络中并行传播信任的系统 [PDF](https://arxiv.org/pdf/2511.20586), [HTML](https://arxiv.org/abs/2511.20586)
### Authors
Koffi Ismael Ouattara,Ioannis Krontiris,Theo Dimitrakos,Dennis Eisermann,Frank Kargl
### Background
随着人工智能系统在关键安全应用中的部署，信任度已成为关键需求。传统的评估指标如准确性和精确度无法捕捉模型预测的不确定性或可靠性，尤其是在对抗或降级条件下。
### Innovation
提出了Parallel Trust Assessment System (PaTAS)，这是一个使用主观逻辑（SL）建模和传播神经网络信任的框架。PaTAS通过Trust Nodes和Trust Functions并行于标准神经计算，将输入、参数和激活的信任在整个网络中传播。该框架引入了参数信任更新机制，以在训练中精炼参数可靠性，并提出了推理路径信任评估（IPTA）方法，以计算推断中实例特定的信任估计。
### Conclusion
PaTAS在真实世界和对抗数据集上的实验表明，它生成了可解释的、对称的且收敛的信任估计，这些估计补充了准确性和在受污染、偏倚或不确定性数据场景中暴露出可靠性差距。结果表明，PaTAS能够区分良性和对抗性输入，并识别模型信心与实际可靠性存在分歧的情况。通过在神经架构中实现透明和可量化信任推理，PaTAS为整个AI生命周期评估模型可靠性提供了基本原则。
## 921. `cs.SE` - 数据驱动方法和AI在工程设计中的应用：面向挑战与机遇的系统文献综述 [PDF](https://arxiv.org/pdf/2511.20730), [HTML](https://arxiv.org/abs/2511.20730)
### Authors
Nehal Afifi,Christoph Wittig,Lukas Paehler,Andreas Lindenmann,Kai Wolter,Felix Leitenberger,Melih Dogru,Patric Grauberger,Tobias Düser,Albert Albers,Sven Matthiesen
### Background
随着数据获取的增加和计算智能的进步，数据驱动方法（DDMs）在产品开发中的应用日益增多。然而，这些方法在产品开发中的整合仍然不完整，主要是由于不确定性，特别是在产品生命周期中使用哪些类型的方法以及何时使用这些方法方面缺乏清晰性。
### Innovation
本文通过应用V模型简化为四个阶段：系统设计、系统实施、系统集成和验证，进行了PRISMA系统文献综述。从Scopus、Web of Science和IEEE Xplore（2014-2024）中检索到1,689篇记录，筛选后有114篇进行了全文分析。研究发现，机器学习和统计学方法在当前实践中占主导地位，而深度学习尽管应用较少，但其使用趋势呈上升趋势。监督学习、聚类、回归分析和代理模型在设计、实施和集成系统阶段较为普及，但在验证阶段的应用仍然有限。此外，还指出了现有应用的关键挑战，如模型解释性不足、跨阶段可追溯性差以及在实际条件下的验证不足，并强调了建立可解释的混合模型的需求。
### Conclusion
这是设计阶段指南的第一步；后续合成应该将计算机科学算法映射到工程设计问题和活动中。
## 922. `cs.SE` - 多Agent系统在软件工程领域数据集适应中的能力、局限性和未来方向 [PDF](https://arxiv.org/pdf/2511.21380), [HTML](https://arxiv.org/abs/2511.21380)
### Authors
Jingyi Chen,Xiaoyan Guo,Songqiang Chen,Shing-Chi Cheung,Jiasi Shen
### Background
软件工程(SE)研究中的数据集自动化适应是提高可扩展性和可重复性的重要方面，但目前尚未得到充分研究。大型语言模型(Large Language Model, LLM)支持的多Agent系统，如GitHub Copilot的代理模式，通过协调推理、代码生成和工具交互可以自动化复杂的开发工作流程。然而，目前关于此类系统在数据集适应任务中的性能评估尚未公开的研究文献。
### Innovation
本文首次综述了最先进的多Agent系统在数据集适应任务中的表现，并评估了基于GPT-4.1和Claude Sonnet 4的支持GitHub Copilot的代理模式在ROCODE和LogHub2.0基准数据集上的适应能力。通过建立一个五阶段评估管道（文件理解、代码编辑、命令生成、验证和最终执行），研究了成功率、错误模式和基于提示的干预措施对提升智能体性能的作用。旨在揭示多Agent LLM系统在数据集适应中的潜力和局限性。
### Conclusion
研究结果显示，目前的系统能够在识别关键文件和生成部分适应方面取得一定进步，但在功能实现上仍然存在不足。特别地，执行错误信息和参考代码的提示级干预措施显著提高了结构相似度，表明上下文和反馈驱动的指导对于此类系统的性能提升至关重要。本文的研究揭示了多Agent LLM系统在数据集适应中的优势和限制，并为未来可持续发展的SS研究提供了具体方向。
## 923. `cs.LG` - STARFlow-V：基于规范流的端到端视频生成模型 [PDF](https://arxiv.org/pdf/2511.20462), [HTML](https://arxiv.org/abs/2511.20462)
### Authors
Jiatao Gu,Ying Shen,Tianrong Chen,Laurent Dinh,Yuyang Wang,Miguel Angel Bautista,David Berthelot,Josh Susskind,Shuangfei Zhai
### Background
规范流（NFs）是端到端的基于似然性的用于连续数据的生成模型，近年来在图像生成方面取得了令人鼓舞的进展。然而，在视频生成领域，由于时空复杂性和计算成本显著增加，最先进的系统几乎完全依赖于基于扩散的模型。本文通过介绍STARFlow-V，即一个基于规范流的视频生成器，重新审视了这一设计空间。STARFlow-V具有端到端学习、稳健的因果预测和原生似然估计等显著优势。
### Innovation
STARFlow-V采用了时空潜在空间中的全局-局部架构，限制了因果依赖于全局潜在空间，同时保留了丰富的局部帧内交互。此外，提出了流评分匹配，为模型配备了一个轻量级因果去噪器，按自回归方式提高视频生成一致性。为了提高采样效率，STARFlow-V采用了视频感知的雅克比迭代方案，将内部更新重新构造为并行化的迭代，而不破坏因果性。STARFlow-V能够在不破坏因果关系的情况下，利用相同的模型支持文本到视频、图像到视频及视频到视频生成任务。
### Conclusion
STARFlow-V实现了强大的视觉保真度和时间一致性，相对于基于扩散的基线模型具有实际的采样吞吐量。这些结果有力地表明，规范流能够在高质量自回归视频生成方面发挥作用，确立了它们作为构建世界模型有前途的研究方向。
## 924. `cs.SE` - 分布式计算从基本原则出发 [PDF](https://arxiv.org/pdf/2506.12959), [HTML](https://arxiv.org/abs/2506.12959)
### Authors
Kenneth Odoh
### Background
本书旨在为广泛的受众群体提供帮助，涵盖从初学者工程师到经验丰富的研究人员以及广泛的从业人士。作者对使分布式计算的核心概念易于理解充满热情，因此，这本书是一项重要的工作，旨在赋予各个背景的人们获取宝贵见解的能力。
### Innovation
书中实现了分布式计算中的多个基础算法，并提供了一个完整的教学指南。无论是对分布式系统原理的理论基础感兴趣，还是对其实际应用感兴趣的读者，本书都能满足需求。
### Conclusion
本书为想要深入了解分布式系统如何在底层工作的读者提供了一个宝贵的机会，同时也为寻求教学指南和完整实现的读者提供了资源。通过本书，读者可以获取宝贵的知识和洞察力，从而更好地理解和应用分布式计算的概念和原理。
## 925. `cs.SE` - LLMs for Automated Unit Test Generation and Assessment in Java: The AgoneTest Framework [PDF](https://arxiv.org/pdf/2511.20403), [HTML](https://arxiv.org/abs/2511.20403)
### Authors
Andrea Lops,Fedelucio Narducci,Azzurra Ragone,Michelantonio Trizio,Claudio Bartolini
### Background
单元测试是软件开发中必不可少但耗费资源的步骤，确保代码单元正确运行。此论文介绍了一种名为AgoneTest的自动评估框架，用于评估大型语言模型（LLM）生成的Java单元测试。AgoneTest旨在通过标准化的端到端评价管道，支持研究者和开发者对比不同类型LLM和提示策略，而并非提供新的测试生成算法。
### Innovation
论文提出了Classes2Test数据集，将要测试的Java类映射到对应的测试类，并引入了包含高级评估指标（如变异分和测试恶臭）的框架，用于全面评估。实验结果表明，对于能够编译的测试，LLM生成的测试可以与或超过人工编写的测试在覆盖率和缺陷检测方面。研究结果还表明，改进的提示策略有助于提高测试质量。AgoneTest阐明了LLMs在软件测试中的潜力，并为未来的模型设计、提示工程和测试实践改进提供了见解。
### Conclusion
AgoneTest清晰地展示了LLMs在软件测试中的潜力，并为未来的研究者和开发者提供了一个标准化的框架和评估机制，有助于精准地对比和提升LLM生成的测试代码的质量。
## 926. `cs.SE` - Co-PatcheR：特定组件的小型推理模型协作软件补丁 [PDF](https://arxiv.org/pdf/2505.18955), [HTML](https://arxiv.org/abs/2505.18955)
### Authors
Yuheng Tang,Hongwei Li,Kaijie Zhu,Michael Yang,Yangruibo Ding,Wenbo Guo
### Background
近年来，通用大型语言模型（LLMs）在软件补丁生成中取得了显著成功，研究人员开始尝试训练专门针对软件补丁的模型。大多数研究工作采用单一模型处理从问题定位到补丁验证的完整补丁生成流程。然而，这一点模型难以有效应对所有子任务，因为不同子任务具有不同的工作流程和需要不同的专业知识。现有的SOTA方法在SWE-bench-Verified基准上仅能达到41%的修复率。鉴于此，作者提出了一种名为Co-PatcheR的协作软件补丁系统，采用针对各个组件的小型专业化推理模型。
### Innovation
作者提出了Co-PatcheR，一种协作的软件补丁系统，使用针对各个组件的小型专业化推理模型来处理软件补丁的各个子任务，通过针对局部化和补丁生成的定制化模型以及结合生成和评估的方法，提出了混合补丁验证和多数投票的补丁选择机制。实验结果显示，仅使用3个14B模型，Co-PatcheR便在SWE-bench-Verified基准上达到了46%的修复率，成为性能最优的补丁生成器，同时对训练资源要求较低且模型规模最小。
### Conclusion
Co-PatcheR通过采用专门针对各个组件的小型推理模型，通过详细的训练方式和模型设计策略，有效提高了软件补丁处理的效果，且在资源利用率和模型尺寸上做出优化，证明了协作式补丁处理和专业模型的合理性及有效性。同时也通过详尽的消融研究验证了所提方案的有效性以及参数选择的正确性。
