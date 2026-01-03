# 20260103
[![Subscribe_Visitors](https://visitor-badge.laobi.icu/badge?page_id=nituchao.latest_arxiv_analyze_ai_rss)](https://github.com/nituchao/latest_arxiv_analyze_ai)

## 1. `cs.AI` - CASCADE: 自主发展和演化以累积代理技能创造 [PDF](https://arxiv.org/pdf/2512.23880), [HTML](https://arxiv.org/abs/2512.23880)
### Authors
Xu Huang,Junwu Chen,Yuxing Fei,Zhuohan Li,Philippe Schwaller,Gerbrand Ceder
### Background
当前的大语言模型（LLM）代理依赖预定义工具或脆弱的工具生成，这限制了它们在复杂科学任务中的能力和适应性。
### Innovation
引入了CASCADE框架，这是一种自适应的代理框架，实现了从「LLM + 工具使用」向「LLM + 技能获取」的过渡。CASCADE使代理能够掌握复杂的外部工具并通过网络搜索和代码提取来实现持续学习，并通过自我反思和知识图谱探索等技能实现自我反思。
### Conclusion
CASCADE在SciSkillBench上对116项材料科学和化学研究任务进行了评估，使用GPT-5实现了93.3%的成功率，而没有进化机制的情况下为35.4%。此外，CASCADE还展示了在计算分析、自动化实验室实验和发表论文中的实际应用。结合人机协作和记忆巩固，CASCADE累积的可执行技能可以在代理间和科学家之间共享，朝着可扩展的人工智能辅助科学研究迈进。
## 2. `cs.AI` - LoongFlow：通过认知计划-执行-总结范式进行定向进化搜索 [PDF](https://arxiv.org/pdf/2512.24077), [HTML](https://arxiv.org/abs/2512.24077)
### Authors
Chunhui Wan,Xunan Dai,Zhuo Wang,Minglei Li,Yanpeng Wang,Yinan Mao,Yu Lan,Zhiwen Xiao
### Background
传统进化方法在静态大型语言模型（LLMs）向自我改善代理过渡时受到缺乏结构化推理的阻碍。现有方法经常难以避免过早收敛和高维代码空间中的低效探索。
### Innovation
LoongFlow 是一种自我发展的智能代理框架，通过结合多岛模型、MAP-Elites 和自适应玻尔兹曼选择，采用认知“计划-执行-总结”（PES）范式，有效实现进化搜索与高推理过程映射。同时引入混合进化记忆系统，保持行为多样性，促进长期架构的连贯性，显著降低计算成本，提高进化效率。
### Conclusion
LoongFlow 在算法发现的一般代理和机器学习代理流水线优化方面表现出色，在 AlphaEvolve 基准测试和 Kaggle 竞赛中，其进化效率最高可提升60%，发现更优解。因此，LoongFlow 是自主科学发现的一个重要进步，减少了计算开销的同时生成专家级解决方案。
## 3. `cs.AI` - 利用大型语言模型和回答集编程实现可解释疾病诊断的概念验证 [PDF](https://arxiv.org/pdf/2512.23932), [HTML](https://arxiv.org/abs/2512.23932)
### Authors
Ioanna Gemou,Evangelos Lamprou
### Background
准确的疾病预测对于及时干预、有效治疗以及减少医疗并发症至关重要。虽然符号AI在医疗领域应用广泛，但由于构建高质量知识库的努力需求限制了其广泛应用。
### Innovation
McCoy框架将大型语言模型与回答集编程相结合，通过让大型语言模型将医学文献翻译成ASP代码，并结合患者数据使用ASP求解器进行处理，最终得出诊断结果。这种集成为利用两种范式的优点提供了稳健且可解释的预测框架。
### Conclusion
初步结果显示，McCoy在小型疾病诊断任务上表现出色。
## 4. `cs.AI` - 钻下和伪造测试（DDFT）：一种衡量语言模型认知稳健性的协议 [PDF](https://arxiv.org/pdf/2512.23850), [HTML](https://arxiv.org/abs/2512.23850)
### Authors
Rahul Baxi
### Background
当前的语言模型评估标准仅在理想条件下衡量模型的知识，忽视了在实际压力下模型保持知识正确性的能力。现有的静态基准，如MMLU和TruthfulQA，无法区分缺乏知识的模型与验证机制在信息降级或对手探查弱点时失效的模型。本文介绍了一种名为钻下和伪造测试（DDFT）的协议，旨在衡量模型在渐进语义压缩和对抗伪造下的认知稳健性：这种能力确保模型在知识准确性方面即使在压力下也能保持稳定。
### Innovation
本文提出了一种新的两系统认知模型，包括生成流畅文本的语义系统和验证事实准确性的知识验证器。通过评估9种前沿模型在8个知识领域的5种压缩水平下的表现（共8000轮次的评估），研究发现认知稳健性与传统设计范式无关，参数量和架构类型对稳健性无显著预测力，而错误检测能力是总体稳健性的关键瓶颈。该研究肯定了大规模模型的脆弱性，并揭示了小型模型可以实现稳健性能的可能性，挑战了模型规模与可靠性之间关系的假设。
### Conclusion
DDFT框架为评估语言模型认知稳健性提供了理论基础和实用工具，在关键应用中部署之前可以使用此框架进行评估。
## 5. `cs.AI` - CogRec：融合大规模语言模型和Soar的认知推荐代理实现可解释的推荐 [PDF](https://arxiv.org/pdf/2512.24113), [HTML](https://arxiv.org/abs/2512.24113)
### Authors
Jiaxin Hu,Tao Wang,Bingsan Yang,Hongrun Wang
### Background
大规模语言模型（LLMs）在理解用户偏好方面表现出强大的能力，但它们受到了诸如“黑箱”特性、知识幻觉以及在线学习能力不足等重大挑战的影响。认知架构，如Soar，虽然提供了结构化的可解释推理过程，但其知识获取过程非常耗时。因此，为了解决这些互补的问题，提出了一种名为CogRec的认知推荐代理，该代理结合了LLMs和Soar的认知架构的优势。
### Innovation
CogRec采用Soar作为其核心符号推理引擎，并利用LLMs初始化知识，填充其工作记忆中的生产规则。该代理遵循感知-认知-行动（PCA）循环。当遇到困境时，它会动态查询LLM以获取合理的解决方案。通过Soar的分块机制将该解决方案转换为新的符号生产规则，从而实现稳健的在线学习。这种学习范式使代理能够不断进化其知识库，并提供高度可解释的推荐理由。
### Conclusion
在三个公开数据集上进行的广泛评估表明，CogRec在推荐准确度、可解释性以及解决长尾问题的有效性方面具有显著优势。
## 6. `cs.AI` - 使用深度强化学习解决车队规模和混合车辆路由问题 [PDF](https://arxiv.org/pdf/2512.24251), [HTML](https://arxiv.org/abs/2512.24251)
### Authors
Pengfu Wan,Jiawei Chen,Gangyan Xu
### Background
车辆路由问题（VRP）的 fleet size and mix 车队规模和混合车辆路由问题（FSMVRP）是运筹学和计算科学领域广泛研究的一个重要变体。它需要同时做出车队构成和路径规划的决策，这使得它非常适合实际应用场景，如短期车辆租赁和按需物流。然而，这种要求也增加了 FSMVRP 的复杂性，特别是在大规模和时间受限的环境中，提出了重大挑战。
### Innovation
本文提出了一种基于深度强化学习（DRL）的方法来解决 FSMVRP，能够在几秒内生成近似最优解。将问题形式化为马尔可夫决策过程 (MDP)，并开发了一个称为 FRIPN 的新的策略网络，该网络无缝地整合了车队构成和路径决策。专门的输入嵌入被融入进来，设计用于不同的决策目标，包括剩余图嵌入，以促进有效的车辆使用决策。
### Conclusion
实验结果表明，本方法在计算效率和可扩展性方面表现出显著优势，特别是在大规模和时间受限的场景中。这些优势突显了本方法在实际应用中的潜力，并为将 DRL 基础技术扩展到 VRP 的其他变体提供了宝贵的启发。
## 7. `cs.AI` - 基于图的探索用于ARC-AGI-3交互推理任务 [PDF](https://arxiv.org/pdf/2512.24156), [HTML](https://arxiv.org/abs/2512.24156)
### Authors
Evgenii Rudakov,Jonathan Shock,Benjamin Ultan Cowley
### Background
ARC-AGI-3基准包括代理需要通过有限的互动来推断任务机制的游戏任务，并随着级别的推进适应不断增加的复杂性。成功需要形成假设、测试它们并跟踪发现的机制。基准研究表明，当前最先进的大语言模型（LLMs）无法可靠地解决这些任务。
### Innovation
作者提出了一种无需训练的方法来解决ARC-AGI-3基准中的交互推理任务，结合了基于视觉框的处理和基于图的结构化的系统状态空间探索。该方法将视觉框分割成有意义的组件，根据视觉显著性优先选择动作，并维护一个已探索状态及其转换的有向图。通过跟踪已访问的状态和已测试的动作，代理优先选择能提供最少已测试状态-动作对路径的动作。在ARC-AGI-3预览挑战中，该结构化的探索策略在六款游戏的52个级别中平均解决了30个，并在私人排行榜上排名第三，显著优于前沿的基于LM的代理。
### Conclusion
这些结果表明，即使是不学习的显式图结构探索也能为交互推理提供一个强有力的基准，并突显了系统状态跟踪和动作优先级的重要性，特别是在当前LLMs无法捕捉到任务动力学的稀疏反馈环境中。
## 8. `cs.AI` - SCP：利用全球自治科学代理网络加速发现 [PDF](https://arxiv.org/pdf/2512.24189), [HTML](https://arxiv.org/abs/2512.24189)
### Authors
Yankai Jiang,Wenjie Lou,Lilong Wang,Zhenyu Tang,Shiyang Feng,Jiaxuan Lu,Haoran Sun,Yaning Pan,Shuang Gu,Haoyang Su,Feng Liu,Wangxu Wei,Pan Tan,Dongzhan Zhou,Fenghua Ling,Cheng Tan,Bo Zhang,Xiaosong Wang,Lei Bai,Bowen Zhou
### Background
随着科学研究的发展，需要一种标准化的方法来加速全球范围内的科学发现。现有的科学资源分散在不同的平台和机构中，难以被有效整合和利用。因此，需要一种能够统一资源描述、标准化工具集成且能够协调实验生命周期管理的协议。
### Innovation
SCP（Science Context Protocol）提出了一个开源标准，旨在通过一个全球网络的自主科学代理来加速科学研究发现。该协议基于两个核心支柱：统一资源集成和组织化实验生命周期管理。精心设计的服务架构包括一个集中式的SCP Hub和分散式的SCP Servers，这些都使跨平台、跨机构的科学资源能在各个分散的应用中被无缝发现、调用和组合，进而建立了一个跨越大量工具资源的科研平台，支持安全的大规模协作，显著减少了整合成本并增强了可重复性。
### Conclusion
SCP通过标准化科学环境和工具集成，在协议层面建立了多机构、代理驱动的科学基础设施，助力科学发现的快速发展和大规模协作。依托SCP，已经建立了具备超过1600种工具资源的大规模科研生态系统，支持跨系统和研究人员的协作，大幅减少集成成本并提高可重复性。
## 9. `cs.AI` - ROAD：通过自动化调试实现反思优化以实现零样本代理对齐 [PDF](https://arxiv.org/pdf/2512.24040), [HTML](https://arxiv.org/abs/2512.24040)
### Authors
Natchaya Temyingyong,Daman Jain,Neeraj Kumarsahu,Prabhat Kumar,Rachata Phondi,Wachiravit Modecrua,Krittanon Kaewtawee,Krittin Pachtrachai,Touchapon Kraisingkorn
### Background
自动提示优化(Auto Prompt Optimization, APO)作为一种增强大语言模型（Large Language Model, LLM）性能的关键技术已经出现，但目前最先进的方法通常依赖于大规模、标注良好的高质量开发集来计算进化或强化学习（Reinforcement Learning, RL）方法的适应度分数。然而，在实际软件工程中，尤其是在代理开发的初始冷启动阶段，工程师们通常难以获取这样的精心制作的数据集，取而代之的是面对杂乱的生产日志和不断演变的失败模式。
### Innovation
本研究提出了ROAD (Reflective Optimization via Automated Debugging)，这是一种新的框架，它通过将优化视为动态调试调查而不是随机搜索，从而绕过了需要精炼数据集的需求。它采用了一个特殊设计的多代理架构，包括Analyzer（根因分析器）、Optimizer（模式聚合器）和Coach（策略集成器），将无结构的失败日志转化为强大的、结构化的决策树协议。
### Conclusion
通过在标准学术基准和实时生产知识管理引擎上的实验评估，我们展示了ROAD具有很高的采样效率，仅通过三次自动迭代，成功率提高了5.6%（从73.6%提高到79.2%），搜索准确性提高了3.8%。此外，在零售领域复杂的推理任务上，与基线相比，ROAD将代理性能提高了约19%。这些结果表明，模仿人类工程师的失败分析和补丁循环，提供了一种可行的、数据高效的替代资源密集型RL训练的方法，用于部署可靠的LLM代理。
## 10. `cs.AI` - SPARK：基于代理驱动检索和知识共享的个性化搜索 [PDF](https://arxiv.org/pdf/2512.24008), [HTML](https://arxiv.org/abs/2512.24008)
### Authors
Gaurab Chhetri,Subasish Das,Tausif Islam Chowdhury
### Background
个性化搜索要求模型能够准确理解用户不断变化的、多维度的信息需求，这对于受限于静态用户画像或单一检索管道系统的解决方案来说是一个挑战。
### Innovation
SPARK提出了一种框架，其中协调的人格化大型语言模型（LLM）代理执行任务特定的检索和新兴个性化。该框架正式化了由角色、专家领域、任务上下文和领域定义的人格空间，并引入了一种人格协调器，能够动态解释查询以激活最具相关性的专业化代理。每个代理执行独立的检索增强生成过程，由专门的长期和短期记忆存储和上下文感知推理模块支持。通过结构化通信协议促进代理间合作，包括共享记忆库、迭代辩论和接力式的知识转移。SPARK通过对认知架构、多代理协调理论和信息检索原理的应用，展示了由最小协调规则指导的分布式代理行为如何产生新兴个性化特性。
### Conclusion
SPARK框架提供了关于协调效率、个性化质量和认知负荷分布可验证的预测，并融入了适应性学习机制以持续优化人物模型。通过集成细粒度的代理专业化与合作式检索，SPARK为未来能够捕捉人类信息寻求行为的复杂性、流动性和上下文敏感性的新一代搜索引擎提供了见解。
## 11. `cs.CL` - 关于LLM安全过滤器的 jailbreak 攻击：我们在LLM安全竞赛中进展到什么程度？ [PDF](https://arxiv.org/pdf/2512.24044), [HTML](https://arxiv.org/abs/2512.24044)
### Authors
Yuan Xin,Dingfan Chen,Linyi Yang,Michael Backes,Xiao Zhang
### Background
随着大型语言模型（LLMs）的广泛应用，确保其安全使用变得至关重要。未经授权的 jailbreak 攻击，即利用对抗性提示绕过模型对齐机制以触发有害输出的行为，带来了显著的风险。尽管已有研究表明这类攻击在大部分常见LLM上的成功率很高，但前期的研究主要关注模型本身，而忽略了部署过程中额外的安全机制，如内容过滤。这项研究填补了这一空白，全面评估了各种 jailbreak 攻击对LLM安全对齐的影响。
### Innovation
首次系统性评估 jailbreak 攻击对LLM安全的影响，不仅覆盖推理阶段，还包括输入和输出的过滤环节。研究发现，大多数已评估的 jailbreak 技术均能被至少一个安全过滤机制检测到，但安全过滤机制在检测方面的有效性仍有提升的空间，尤其是在平衡召回率和精确率方面。
### Conclusion
研究揭示了关键的差距，并呼吁提高检测准确性和用户体验，以进一步优化LLM安全系统。
## 12. `cs.CL` - 基于分解学习的时空定位视频语言模型 [PDF](https://arxiv.org/pdf/2512.24097), [HTML](https://arxiv.org/abs/2512.24097)
### Authors
Wenzheng Zeng,Difei Gao,Mike Zheng Shou,Hwee Tou Ng
### Background
近年来，视频-语言模型在视频理解方面展示了巨大的潜力，但在事件级感知的准确时间定位方面仍然存在挑战。现有研究大多将这两项任务（即时间定位和文本响应）耦合在一起处理，缺乏清晰的逻辑层次结构，导致效果不尽如人意。
### Innovation
本文从分解学习的角度提出了一种新框架D$^{2}$VLM，该框架将学习这两大任务的过程分离出来，同时还强调它们之间的固有依赖关系。同时引入了一种新的分解偏好优化（FPO）算法，该算法在优化目标中明确地将概率时间定位建模纳入偏好学习中，从而促进了这两项任务的学习。
### Conclusion
实验结果表明，本文的方法在各种任务上的表现更为优越。同时，为了支持分解偏好学习，我们还构建了一个合成数据集，以解决现有缺乏明确时间定位的适合数据集的问题。
## 13. `cs.CL` - Let It Flow: Agentic Crafting on Rock and Roll, Building the ROME Model within an Open Agentic Learning Ecosystem [PDF](https://arxiv.org/pdf/2512.24873), [HTML](https://arxiv.org/abs/2512.24873)
### Authors
Weixun Wang,XiaoXiao Xu,Wanhe An,Fangwen Dai,Wei Gao,Yancheng He,Ju Huang,Qiang Ji,Hanqi Jin,Xiaoyang Li,Yang Li,Zhongwen Li,Shirong Lin,Jiashun Liu,Zenan Liu,Tao Luo,Dilxat Muhtar,Yuanbin Qu,Jiaqiang Shi,Qinghui Sun,Yingshui Tan,Hao Tang,Runze Wang,Yi Wang,Zhaoguo Wang,Yanan Wu,Shaopan Xiong,Binchen Xu,Xander Xu,Yuchi Xu,Qipeng Zhang,Xixia Zhang,Haizhou Zhao,Jie Zhao,Shuaibing Zhao,Baihui Zheng,Jianhui Zheng,Suhang Zheng,Yanni Zhu,Mengze Cai,Kerui Cao,Xitong Chen,Yue Dai,Lifan Du,Tao Feng,Tao He,Jin Hu,Yijie Hu,Ziyu Jiang,Cheng Li,Xiang Li,Jing Liang,Chonghuan Liu,ZhenDong Liu,Haodong Mi,Yanhu Mo,Junjia Ni,Shixin Pei,Jingyu Shen,XiaoShuai Song,Cecilia Wang,Chaofan Wang,Kangyu Wang,Pei Wang,Tao Wang,Wei Wang,Ke Xiao,Mingyu Xu,Tiange Xu,Nan Ya,Siran Yang,Jianan Ye,Yaxing Zang,Duo Zhang,Junbo Zhang,Boren Zheng,Wanxi Deng,Ling Pan,Lin Qu,Wenbo Su,Jiamang Wang,Wei Wang,Hu Wei,Minggang Wu,Cheng Yu,Bing Zhao,Zhicheng Zheng,Bo Zheng
### Background
现有的开源社区缺乏一个从开发到部署的全方位系统，用于简化代理AI的开发流程。这些代理AI需要在现实世界环境中多次迭代地行动、观察和改进，以实现作品的优化。
### Innovation
本文介绍了一种名为Agentic Learning Ecosystem (ALE)的基础架构，它包含三个组成部分：ROLLO，用于模型调优的框架；ROCK，用于生成轨迹环境管理器；iFlow CLI，用于高效情境工程的代理框架。此外，通过数据合成协议和一种新的基于互动策略对齐（IPA）的策略优化算法，该研究提高了长时间训练的稳定性。
### Conclusion
在带有结构化的设定中评估了基于ALE开放系统构建的ROME模型，并通过Terminal Bench Pro基准测试对其进行验证，结果显示了强大的性能，证明了ALE基础设施的有效性。
## 14. `cs.CL` - AHA：通过反事实硬负样例对大型音频语言模型进行幻觉对齐 [PDF](https://arxiv.org/pdf/2512.24052), [HTML](https://arxiv.org/abs/2512.24052)
### Authors
Yanxi Chen,Wenhui Zhu,Xiwen Chen,Zhipeng Wang,Xin Li,Peijie Qiu,Hao Wang,Xuanzhao Dong,Yujian Xiong,Anderson Schneider,Yuriy Nevmyvaka,Yalin Wang
### Background
虽然大型音频语言模型（LALMs）能够达到最先进的（SOTA）性能，但在生成文本时往往会遇到幻觉问题，即生成的文本与音频输入不相关。本文通过分析这些地壳错误，确定了四种特定的分类：事件遗漏、虚假事件识别错误、时间关系错误和量化时间错误。
### Innovation
本文提出了AHA（Audio Hallucination Alignment）框架，通过利用反事实硬负样本挖掘技术，构建了一个高质量的偏好数据集，迫使模型区分严格的声学证据和语义上可接受的虚构。此外，还建立了一个诊断基准AHA-Eval，用于严格测试模型的精细时间推理能力。并应用这一数据集对Qwen2.5-Omni模型进行对齐，得到的模型Qwen-Audio-AHA在AHA-Eval上取得了13.7%的提升，这种优势不仅仅局限于诊断集，还在公共基准测试中表现出色。
### Conclusion
本文提出的方法在多个公开基准测试中表现出显著的改进，如MMAU-Test提高1.3%，MMAR提高1.6%，并且优于最新的SOTA方法。模型在处理音频生成任务中的幻觉问题上取得了实质性的进展，并证明方法的有效性。
## 15. `cs.CL` - 递归语言模型 [PDF](https://arxiv.org/pdf/2512.24601), [HTML](https://arxiv.org/abs/2512.24601)
### Authors
Alex L. Zhang,Tim Kraska,Omar Khattab
### Background
研究使大型语言模型（LLMs）能够处理任意长的提示，从推理时的扩展策略角度出发。
### Innovation
提出了一种名为递归语言模型（RLMs）的通用推理策略，它将长提示视为外部环境的一部分，允许LLMs通过编程方式检查、分解，并递归地在其提示片段上调用自身。实验结果显示，RLMs能够有效处理比模型上下文窗口大两个数量级的输入，并且即使在较短的提示下，其质量也大幅优于基础LLMs和常见的长上下文支架，同时具有可比或更低成本。
### Conclusion
RLMs成功处理了比模型上下文窗口大两个数量级的输入，并在四个不同长上下文任务中表现出色，相比基础LLMs和常见的长上下文支架，其质量更高，且具有可比或更低的成本。
## 16. `cs.CL` - 超越比特：多包络双二进制因子化以实现极端量化 [PDF](https://arxiv.org/pdf/2512.24545), [HTML](https://arxiv.org/abs/2512.24545)
### Authors
Yuma Ichikawa,Yoshihiko Fujisawa,Yudai Fujimoto,Akira Sakai,Katsuki Fujisawa
### Background
对于大型语言模型（LLMs）的极端低比特量化，双二进制因子化（DBF）是一个有吸引力的选择，因为它能够在不牺牲准确性的情况下实现高效的推理。然而，DBF的比例参数过于限制性，在消除符号后，所有秩分量共享相同的幅度分布，导致性能饱和。
### Innovation
提出了多包络双二进制因子化（MDBF），它保留了一对共享的1比特符号基矩阵，但用秩-$l$包络替代了单个包络。通过在包络组件间共享符号矩阵，MDBF有效地保持了二进制载体并利用有限的内存预算来提高幅度表达能力。引入了闭式初始化方法和交替优化方法来优化MDBF。
### Conclusion
在LLaMA和Qwen系列模型中，MDBF在匹配比特/权重的情况下比以前的二进制格式提高了困惑度和零样本准确度，同时保留了相同的部署友好推理特性。
## 17. `cs.CL` - 量子视觉词汇消歧：通过量子推理模型阐明歧义 [PDF](https://arxiv.org/pdf/2512.24687), [HTML](https://arxiv.org/abs/2512.24687)
### Authors
Wenbo Qiao,Peng Zhang,Qinghua Hu
### Background
视觉词汇消歧主要是针对多义词的问题，候选图像可能会导致混淆。传统方法使用经典概率计算目标词每个义项与图像匹配的可能性，通过这些可能性之和形成后验概率。但由于语义不确定性，来自不同来源的义项不可避免地带有语义偏见，这可能导致偏颇的消歧结果。
### Innovation
本文受到量子超位置在处理不确定性中的灵感，提出了一种新的量子推理模型（Q-VWSD），将目标词的多个义项编码为超位置态以减轻语义偏见。随后执行量子电路并观察结果。我们的方法是我们经典的基于概率的方法的量子扩展。在此基础上，我们还设计了一种高效的经典计算版本的Q-VWSD。
### Conclusion
实验表明，我们的方法在提高性能的同时，优于最先进的经典方法，特别是通过有效地利用大型语言模型的非专门化义项。我们的方法展示了量子机器学习在实际应用中的潜力，并提供了在量子硬件尚不成熟时利用量子建模优势在经典计算机上的机会。
## 18. `cs.CL` - DermaVQA-DAS：皮肤病评估框架（DAS）及患者生成的皮肤病图像中的闭合问题回答和分割数据集 [PDF](https://arxiv.org/pdf/2512.24340), [HTML](https://arxiv.org/abs/2512.24340)
### Authors
Wen-wai Yim,Yujuan Fu,Asma Ben Abacha,Meliha Yetisgen,Noel Codella,Roberto Andres Novoa,Josep Malvehy
### Background
近年来，皮肤科图像分析的进步主要得益于大规模标注数据集的推动，但现有基准大多集中在皮肤镜图像上，缺少患者生成的查询和临床上下文，从而限制了其在以患者为中心的护理中的应用。
### Innovation
本文引入了DermaVQA-DAS，它是DermaVQA数据集的扩展，支持闭合式问题回答（QA）和皮肤病变分割两个互补任务。核心是皮肤病学评估方案（DAS），这是一种新型的专家开发的框架，用于系统化地捕获具有临床意义的皮肤科特征，结构化且标准化，并提供了36个高层次和27个细粒度的评估问题，以及英语和中文的多项选择选项。此外，使用DAS，作者为闭合QA和分割提供了专家标注的数据集，并对最先进的多模态模型进行了基准测试。
### Conclusion
对于分割，通过评估多种提示策略，发现默认提示在Mean-of-Max和Mean-of-Mean评估聚合方案下取得了最佳结果，而结合患者查询标题和内容的增强提示在基于多数投票的微评分评估下表现最佳，Jaccard指数为0.395，Dice分数为0.566，BiomedParse表现出色。对于闭合问答，各模型性能较强，平均准确率在0.729至0.798之间，o3表现最佳，为0.798，紧随其后的是GPT-4.1（0.796）和Gemini-1.5-Pro（0.783），性能表现良好。文中公开发布了DermaVQA-DAS、DAS框架和评估协议，以支持和加速患者为中心的皮肤病视觉语言模型未来研究。（提供链接）
## 19. `cs.CL` - OptRot: 通过无数据旋转缓解训练后量化中的权重异常值 [PDF](https://arxiv.org/pdf/2512.24124), [HTML](https://arxiv.org/abs/2512.24124)
### Authors
Advait Gadhikar,Riccardo Grazzi,James Hensman
### Background
在大型语言模型（LLMs）的权重和激活存在异常值的情况下，量化这些模型变得非常困难。近期研究中，旋转方法被用于减少这些异常值的影响。本研究在此背景下提出了一种新的方法，通过最小化精确且低成本的代理目标来量化权重。
### Innovation
该研究提出了一个名为OptRot的方法，通过旋转权重来最小化量化误差的四次方，从而有效地减少了权重异常值。此外，还提出了一种数据依赖性方法OptRot^+，通过纳入激活统计信息进一步提升了性能。这些方法显著优于现有方法，如Hadamard旋转和数据依赖方法SpinQuant和OSTQuant。
### Conclusion
实验结果显示OptRot在W4A8设置中表现优于其他方法，并且还在激活量化中有所改进。但在W4A4设置中，OptRot和OptRot^+的表现较差，表明了权重和激活量化之间的权衡。
## 20. `cs.CL` - 从构建块到规划：基于强化学习的LLMs多步空间推理 [PDF](https://arxiv.org/pdf/2512.24532), [HTML](https://arxiv.org/abs/2512.24532)
### Authors
Amir Tahmasbi,Sadegh Majidi,Kazem Taram,Aniket Bera
### Background
大语言模型（LLMs）在导航和规划应用中对空间推理的关注越来越多。尽管LLMs在一般语言能力上有很强的表现，但在结构化环境中的空间变换和多步规划方面仍存在问题。目前的方法通常难以处理这类复杂的任务。
### Innovation
本文提出了一种两阶段的方法来分解空间推理为原子构建块及其组合。首先，使用监督微调对基本的空间变换（如旋转、平移和缩放）进行训练，使模型具备基本的空间物理知识。然后，冻结这些物理意识的模型并在GRPO框架中训练轻量级LoRA适配器，以学习将这些构建块组合起来用于基于拼图的环境中的多步规划。此外，本文还合成了一个基于ASCII的艺术数据集，并构建了一个对应的基于ASCII的强化学习环境，以支持这种方法。
### Conclusion
本文的方法在动态和静态环境中都表现出色，优于基线方法，包括通用主干、物理意识模型和端到端的RL模型。此外，该方法在收敛速度和培训稳定性上也表现更好。最后，分析了注意力模式来评估微调是否能引起有意义的空间理解改进。
## 21. `cs.LG` - 多步检索与推理提高大型语言模型的放射学问题回答 [PDF](https://arxiv.org/pdf/2508.00743), [HTML](https://arxiv.org/abs/2508.00743)
### Authors
Sebastian Wind,Jeta Sopa,Daniel Truhn,Mahshad Lotfinia,Tri-Thien Nguyen,Keno Bressem,Lisa Adams,Mirabela Rusu,Harald Köstler,Gerhard Wellein,Andreas Maier,Soroosh Tayebi Arasteh
### Background
放射学中的临床决策越来越多地受益于人工智能技术，尤其是在大型语言模型中。然而，传统的放射学问题回答检索增强生成（RAG）系统通常依赖于单步检索，这限制了它们处理复杂临床推理任务的能力。
### Innovation
提出了放射学检索与推理（RaR）框架，这是一个多步检索和推理框架，旨在提高大型语言模型在放射学问题回答中的诊断准确性、事实一致性和临床可靠性。通过对104个专家筛选的放射学问题和65个未见过的现实世界放射学考试问题进行评估，证明了RaR在提升诊断准确性、减少幻觉以及检索临床相关背景方面的有效性。
### Conclusion
研究结果强调了RaR框架在提高放射学问题回答的事实性和诊断准确性方面的潜在价值，建议未来研究验证其临床实用性。所有数据集、代码和完全的RaR框架均已公开，以支持开放研究和临床应用。
## 22. `cs.LG` - 使用潜在桥梁模型的音频超分辨率 [PDF](https://arxiv.org/pdf/2509.17609), [HTML](https://arxiv.org/abs/2509.17609)
### Authors
Chang Li,Zehua Chen,Liyuan Wang,Jun Zhu
### Background
音频超分辨率（SR）即通过扩增低分辨率（LR）波形得到高分辨率（HR）版本。尽管扩散模型和桥梁模型近年来被用于音频超分辨率，但先前的方法往往因缺乏有效的生成先验而导致超分辨率质量不佳。
### Innovation
提出了一个具有潜在桥梁模型（LBMs）的新系统。通过将音频波形压缩到连续的潜在空间，并设计LBMs以实现潜在到潜在的生成过程，该过程自然匹配了LR到HR的扩增过程，从而充分利用了LR波形中包含的指导性先验信息。引入了频率感知的LBMs以增强训练结果，设计了级联LBMs并提出了两种先验增强策略，解锁了超过48kHz的音频超分辨率，并为音频后期制作提供更高的灵活性。
### Conclusion
在VCTK、ESC-50、Song-Describer基准数据集和两个内部测试集上的全面实验结果表明，该方法在语音、音频和音乐信号从任何采样率到48kHz的超分辨率方面达到业界领先的质量水平，纪录首次192kHz音频超分辨率的性能。
## 23. `cs.LG` - MedQARo: 用于罗马尼亚语医疗问答评估的大规模基准 [PDF](https://arxiv.org/pdf/2508.16390), [HTML](https://arxiv.org/abs/2508.16390)
### Authors
Ana-Cristina Rogoz,Radu Tudor Ionescu,Alexandra-Valentina Anghel,Ionut-Lucian Antone-Iordache,Simona Coniac,Andreea Iuliana Ionescu
### Background
医疗问答（QA）是自然语言处理（NLP）的核心任务，对于实现人工通用智能（AGI）至关重要。然而，特定领域和语言的医疗问答数据集的缺乏阻碍了跨领域和跨语言的稳健AI模型的发展。为了应对这一挑战，作者提出了MedQARo，这是一个首屈一指的大型医疗QA基准库，专为罗马尼亚语设计。该基准库包含了一个高质量的、包含105,880个医疗问答对的数据集，这些数据是从两家医疗机构中关于1,242个癌症患者的病例总结中收集的。这些数据集经过了七位专科医生手工标注，共计花费了约3,000工作小时。
### Innovation
MedQARo是首个大规模的医疗QA基准库，专为罗马尼亚语设计。通过对该基准库中包含的高质量数据进行标注，作者对四种来自不同模型家族的开源大型语言模型（LLMs）和两个通过API提供的先进模型进行了实验，发现预训练模型无法很好地泛化到MedQARo任务上，进一步强调了在罗马尼亚语中进行领域特定和语言特定的微调的重要性。
### Conclusion
研究表明，微调后的模型在MedQARo任务上明显优于零样本模型，这表明预训练模型在该任务上几乎无法泛化。该研究还表明了对罗马尼亚医疗问答系统中进行领域特定和语言特定的模型微调的重要性。作者公开发布了该数据集和相关代码，这为未来的医疗NLP研究提供了宝贵的资源。
## 24. `cs.LG` - 生成模型中Lipschitz引导的插值表设计 [PDF](https://arxiv.org/pdf/2509.01629), [HTML](https://arxiv.org/abs/2509.01629)
### Authors
Yifan Chen,Eric Vanden-Eijnden,Jiawei Xu
### Background
本文研究了在流和扩散生成模型的随机插值框架下的插值表设计。作者指出，所有标量插值表在路径空间的Kullback-Leibler散度下，在最优扩散系数调整后，能达到相同的统计效率，但在数值效率上却可能有很大差异。这促使研究者们开始重视插值表结果的数值特性而非仅仅依赖统计标准。
### Innovation
提出了平均平方Lipschitz性最小化作为一种数值优化的原理性标准，作为Kinetic能量最小化方法的替代。此外，提出了一个转移公式，使在推理时可以在不同的插值表间转换而无需重新训练神经网络。对于高维不变分布，优化插值表在Lipschitz常数上实现了指数级改善，特别是在高斯混合分布的少量步骤采样中减少模式塌陷。
### Conclusion
本文验证了在随机Allen-Cahn方程和Navier-Stokes方程的高维不变分布中，优化后的插值表显现出稳健的性能提升。对于高斯分布，优化后的插值表在Lipschitz常数上实现了指数级的改善；而对于高斯混合分布，则在少量步长抽样中减少了模态坍塌。
## 25. `cs.LG` - 多模态LLM在空间智能上的全面评估 [PDF](https://arxiv.org/pdf/2508.13142), [HTML](https://arxiv.org/abs/2508.13142)
### Authors
Zhongang Cai,Yubo Wang,Qingping Sun,Ruisi Wang,Chenyang Gu,Wanqi Yin,Zhiqian Lin,Zhitao Yang,Chen Wei,Oscar Qian,Hui En Pang,Xuanke Shi,Kewang Deng,Xiaoyang Han,Zukai Chen,Jiaqi Li,Xiangyu Fan,Hanming Deng,Lewei Lu,Bo Li,Ziwei Liu,Quan Wang,Dahua Lin,Lei Yang
### Background
近年来，多模态模型取得了显著的进步，但在空间理解与推理方面仍然存在明显的局限性，这是人工智能要真正落地物理世界的关键能力。最近发布了GPT-5，可能是迄今为止最强大的AI模型，现在是评估最先进的模型（GPT、Gemini、Grok、Seed、Qwen、Intern）在空间智能方面表现的好时机。因此，本文提出了EASI（全面评价多模态LLM的空间智能），以系统地评估最先进的模型。
### Innovation
EASI提出了一个全面的空间任务分类体系，集成了现有的基准测试和新收集的基准测试，使得系统性评估最先进的模型成为可能。该研究涵盖了八个关键基准，研究总花费超过100亿个令牌。研究发现GPT-5在空间智能方面表现出色，但在广泛的空间任务中仍远低于人类表现。同时，空间任务暴露了更大的模型能力缺陷，让使用私有模型在解决最困难的任务时不再占据明显优势。
### Conclusion
EASI是一个持续的社区努力项目，已经开源了EASI代码库，提供了一站式和可重复的解决方案，简化了多个基准的配置和运行流程。还推出了EASI排行榜，提供了一个持续更新的性能快照，加速了对稳健空间智能的集体进步。
## 26. `cs.LG` - 多模态任务感知语义通信的分布式信息瓶颈理论 [PDF](https://arxiv.org/pdf/2510.04000), [HTML](https://arxiv.org/abs/2510.04000)
### Authors
Yujie Zhou,Cheng Peng,Rulong Wang,Yong Xiao,Yingyu Li,Guangming Shi,Ping Zhang
### Background
语义通信将关注点从比特级别的准确性转移到对下游任务具有重要意义的语义信息的传递上。然而，现有的多模态解决方案往往会对所有可用信息模态进行非区分处理，忽视了这些模态对下游任务贡献的不平等性，这不仅导致了资源利用效率低下，还因为不相关或冗余信息的存在而影响了任务的推理性能。
### Innovation
提出了一个新颖的任务感知分布式信息瓶颈（TADIB）框架，该框架量化了任何一组模态对给定任务的贡献。基于这个理论框架，设计了一种智能选择并压缩最相关模态的编码方案。采用离散选择的概率松弛，使分布式编码器通过评分函数估计和公共随机性进行协调决策。
### Conclusion
在公共数据集上的大量实验表明，该解决方案在显著减少通信和计算成本的同时，能够匹配或超越全模态基线的推理性能。
## 27. `cs.LG` - 高维空间中学习二次神经网络：SGD动力学与缩放定律 [PDF](https://arxiv.org/pdf/2508.03688), [HTML](https://arxiv.org/abs/2508.03688)
### Authors
Gérard Ben Arous,Murat A. Erdogdu,Nuri Mert Vural,Denny Wu
### Background
研究在高维条件下基于梯度的两层神经网络参数优化及样本复杂度。数据生成方式为$f_*(boldsymbol{x}) text{与} boldsymbol{x} text{的线性组合，}boldsymbol{x} text{遵循标准正态分布，二次层激活函数为2阶赫密特多项式，信号方向相互正交。考虑宽度与维度的关系以及系数的幂律衰减。}
### Innovation
提出了特征学习阶段SGD动态的精细分析，无论是总体极限还是有限样本离散化；推导出预测风险的缩放定律，明确表示了优化时间、样本量和模型宽度之间的幂律依赖关系；结合矩阵刘维尔积分微分方程的精确描述和新型矩阵单调性论证来提供无限维有效动态的收敛保证。
### Conclusion
分析了高维环境中两层神经网络的学习过程，得到不同因素如优化时间、样本量和模型宽度对预测风险的影响规律，并为无限维有效动态的收敛提供了保证。
## 28. `cs.LG` - 深层不对称递归神经网络中的动力学习 [PDF](https://arxiv.org/pdf/2509.05041), [HTML](https://arxiv.org/abs/2509.05041)
### Authors
Davide Badalotti,Carlo Baldassi,Marc Mézard,Mattia Scardecchia,Riccardo Zecchina
### Background
本文研究了具有不对称相互作用的递归神经网络，在这些网络中引入自我耦合或稀疏的单模间兴奋性连接，使得能够形成动态可访问的稳定配置密集相连流形。这个表示流形在系统规模上呈指数增长，并可以通过简单的局部动力学到达，尽管它只是全局配置空间中的次要子集。
### Innovation
通过一个完全局部、无梯度的方法在结构上直接实现学习，该方法选择性地稳定一个与任务相关的网络配置。此外，这种方法不需要进行显式的网络状态对比，只需利用瞬态监督信号偏向动力学并进入表示流形，然后通过局部可塑性巩固所达到的配置，从而有效地塑造潜在表示空间。
### Conclusion
数值评估表明，这种方法在标准图像分类基准上的表现与使用反向传播训练的多层感知器相当。更广泛地说，这些结果表明，固定点的动力学可访问性及其内部网络动力学的稳定化是递归系统学习的可行替代原则，这些原则与统计物理学概念有关，并可能对生物启发式计算架构及神经形态计算具有重要意义。
## 29. `cs.LG` - 使用分子集体变量增强扩散基采样的方法 [PDF](https://arxiv.org/pdf/2510.11923), [HTML](https://arxiv.org/abs/2510.11923)
### Authors
Juno Nam,Bálint Máté,Artur P. Toshev,Manasa Kaniselvan,Rafael Gómez-Bombarelli,Ricky T. Q. Chen,Brandon Wood,Guan-Horng Liu,Benjamin Kurt Miller
### Background
基于扩散的采样器能够仅使用能量或对数密度来学习采样复杂的高维分布，而无需训练数据。然而，在分子采样中，这些方法通常比分子动力学慢，且往往无法捕捉到与热力学相关的模态。受到增强采样的启发，研究者通过在特定的信息丰富、低维投影（即集体变量）上施加顺序偏置，来促进探索。这种方法通过在最新样本中心施加排斥势能，将未来的样本推向新颖的集体变量区域，并在投影空间中有效提高温度。
### Innovation
提出了一种基于排斥势能在集体变量上的偏置方法，这种方法能提高采样的效率，发现新的模态，并估计自由能变化。该方法还确保了采样大致独立于近似玻兹曼分布，通过偏置的再加权实现。这种方法在标准多肽构象采样基准测试中表现优异，能够恢复多种构象状态和准确的自由能曲线。此外，这是首次使用基于扩散的采样器实现反应性采样，这种方法能够以近量子力学准确度捕捉到共价键的断裂和形成，显著缩短采样所需的时间，从而推动了基于扩散的采样方法在分子科学中的实用化。
### Conclusion
该方法在标准多肽构象采样基准测试中表现出色，能够恢复多种构象状态和准确的自由能曲线。这是首个使用基于扩散的采样器实现反应性采样的方法，能够以近量子力学准确度捕捉到共价键的断裂和形成，显著缩短采样所需的时间，从而推动了基于扩散的采样方法在分子科学中的实用化。
## 30. `cs.LG` - 基于轻量级深度学习的辅助超大规模MIMO系统的RIS增强通道估计在资源有限的边缘设备上 [PDF](https://arxiv.org/pdf/2507.09627), [HTML](https://arxiv.org/abs/2507.09627)
### Authors
Muhammad Kamran Saeed,Ashfaq Khokhar,Shakil Ahmed
### Background
下一代无线技术如6G旨在满足超高速率数据、超低延迟和增强连接的需求。极其大规模MIMO (XL-MIMO) 和可重构智能表面 (RIS) 是关键技术，XL-MIMO 通过大量天线提高频谱和能效，而 RIS 则通过被动反射元件动态控制无线环境。然而，要充分发挥它们的潜力，关键在于准确的信道状态信息 (CSI)。尽管深度学习的进步有助于有效的级联信道估计，但现有建模在XL-MIMO系统中的可扩展性和实际部署仍然有限。随着天线和RIS元件数量的增加，实时和有效的信道估计变得具有挑战性，数据量增加，计算复杂度上升，需要高级硬件，并且导致大量能耗。
### Innovation
本文提出了一种轻量级深度学习框架，用于资源有限的边缘设备上的XL-MIMO系统中有效级联信道估计。通过利用信道的空间相关性，我们引入了一种基于补丁的训练机制，减少了输入维度到补丁级别的表示，同时保留了关键信息，从而实现大系统中的可扩展训练。仿真结果表明，无论是在XL-MIMO系统中天线和RIS元件数量增加的情况下，该框架都显著提高了信道估计的准确性并降低了计算复杂度。
### Conclusion
本文提出的轻量级深度学习框架能够在资源受限的边缘设备上有效应用于XL-MIMO系统中的级联信道估计，该框架通过减少计算复杂度和关键信息的保留，实现了高性能的估计，提高了实际部署的可能性。
