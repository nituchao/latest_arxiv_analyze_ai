# 20251201
[![Subscribe_Visitors](https://visitor-badge.laobi.icu/badge?page_id=nituchao.latest_arxiv_analyze_ai_rss)](https://github.com/nituchao/latest_arxiv_analyze_ai)

## 1. `cs.AI` - A²Flow: 通过自适应抽象运算符实现工作流自动化生成 [PDF](https://arxiv.org/pdf/2511.20693), [HTML](https://arxiv.org/abs/2511.20693)
### Authors
Mingming Zhao,Xiaokang Wei,Yuanqi Shao,Kaiwen Zhou,Lin Yang,Siwei Rao,Junhui Zhan,Zhitang Chen
### Background
大型语言模型（LLMs）在自动化代理工作流设计方面显示出强大的潜力。然而，现有的方法仍然高度依赖于人工预定义的操作，这限制了其泛化能力和可扩展性。
### Innovation
提出了A²Flow，一种基于自适应抽象运算符的完全自动化的工作流生成框架，通过三个阶段的操作提取过程：基于案例的初始操作生成、操作聚类和初步抽象、以及深入提取抽象执行操作。此外，通过操作记忆机制增强了节点级别的工作流搜索，保留了历史输出以丰富语境并改善决策。
### Conclusion
在通用和具身基准上的实验表明，A²Flow 较最先进的基线方法实现了 2.4% 和 19.3% 的平均性能提升，并减少了 37% 的资源使用。
## 2. `cs.AI` - 代表空间干预促进大型语言模型的终身结构化知识控制 [PDF](https://arxiv.org/pdf/2511.20892), [HTML](https://arxiv.org/abs/2511.20892)
### Authors
Xuyuan Liu,Zhengzhang Chen,Xinshuai Dong,Yanchi Liu,Xujiang Zhao,Shengyu Chen,Haoyu Wang,Yujun Yan,Haifeng Chen
### Background
大型语言模型（LLMs）经常生成错误或过时的内容。在不耗费大量资源进行重新训练的情况下高效且准确地更新其知识是一项重大挑战。在终身学习场景中，由于需要管理大量需要同时存在的编辑，对于复杂且结构化不强的知识的控制尤为困难。
### Innovation
引入了一种名为RILKE的方法（Representation Intervention for Lifelong KnowledgE Control），这是一种稳健且可扩展的方法，旨在将知识控制视为模型表示空间内的干预。利用表示空间的表达能力，RILKE识别出两种特性，使其能够针对复杂且结构不强的知识提供精细的控制，同时保持一般用途。RILKE通过在训练过程中学习抗同义变形和局部编辑的模块来限制每次更新的维度，从而减少交叉编辑的干扰。在推理过程中，一个查询适应的路由器选择适当的模块来指导模型的生成。
### Conclusion
在LLaMA和Qwen模型上的知识编辑基准测试中，RILKE展示了对大规模数据集的高度扩展性，表现出很高的编辑成功率、强大的同义变形泛化能力，并且在适度的内存开销下保持了一般用途。这些结果表明，RILKE是一种有效的可扩展解决方案，适用于LLMs中的终身知识控制。
## 3. `cs.AI` - 不同数据集在Amazon CoT框架下的跨域多模态链式推理评估 [PDF](https://arxiv.org/pdf/2511.20701), [HTML](https://arxiv.org/abs/2511.20701)
### Authors
Nitya Tiwari,Parv Maheshwari,Vidisha Agarwal
### Background
虽然最近的研究已经在多模态设置下扩展了链式思维（CoT），并且在科学问题解答基准（如ScienceQA）上取得了最先进的结果，但这些方法在不同领域的通用性仍然没有被充分探索。
### Innovation
本文通过实施并评价Zhang等人提出的两阶段框架（分为理由生成和答案推理，并通过门控融合机制集成视觉特征以及基于T5的语言模型），对多模态链式思维（Multimodal-CoT）进行了全面分析。通过系统的消融研究，分析了视觉特征、理由质量以及架构选择的贡献。
### Conclusion
研究表明，视觉特征的整合显著减少了理由生成中的幻觉。然而，CoT推理的有效性在不同问题类型上存在显著差异，尤其是常识推理提出的特殊挑战。本文为研究人员实施多模态推理系统提供了实用见解，并指出了跨领域通用性改进的关键领域。
## 4. `cs.AI` - Paraconsistent-Lib: 一个直观的PAL2v算法Python库 [PDF](https://arxiv.org/pdf/2511.20700), [HTML](https://arxiv.org/abs/2511.20700)
### Authors
Arnaldo de Carvalho Junior,Diego Oliveira da Cruz,Bruno da Silva Alves,Fernando da Silva Paulo Junior,João Inacio da Silva Filho
### Background
该论文介绍了一个名为Paraconsistent-Lib的开源Python库，用于构建PAL2v算法在推理和决策系统的实现。Paraconsistent-Lib旨在为PAL2v标准计算提供一个通用库，并且能够输出三种类型的结果：12个经典格PAL2v区域中的矛盾分析结果、矛盾分析节点(PAN)输出以及决策输出。
### Innovation
Paraconsistent-Lib将一些知名PAL2v算法（如Para-analyzer、ParaExtrCTX、PAL2v Filter、矛盾分析网络(PANnet)和矛盾神经网络(PNN)）以独立或网络形式编写，从而减少复杂性、代码大小和错误。
### Conclusion
鉴于其稳定状态，Paraconsistent-Lib是持续开发的，能够响应GitHub上用户所需的功能和改进。
## 5. `cs.AI` - 利用大规模语言模型在智能代理AI Wi-Fi中学习多接入点协调 [PDF](https://arxiv.org/pdf/2511.20719), [HTML](https://arxiv.org/abs/2511.20719)
### Authors
Yifan Fan,Le Liang,Peng Liu,Xiao Li,Ziyang Guo,Qiao Lan,Shi Jin,Wen Tong
### Background
多接入点协调（MAPC）是下一代Wi-Fi在密集重叠基本服务集中提高吞吐量的关键技术。然而，现有的MAPC协议依赖于静态、协议定义的规则，这限制了它们适应变化的网络条件（如不同的干扰水平和拓扑结构）的能力。
### Innovation
本文提出了一种新的智能代理AI Wi-Fi架构，其中每个接入点被建模为一个自主的大规模语言模型代理，并通过认知工作流协作推理网络状态和实时协商自适应协调策略。通过利用集成的记忆、反思和工具使用，代理能够进行自然语言对话，使其决策基于以往经验和环境反馈。
### Conclusion
全面的仿真实验表明，我们的智能代理框架能够成功学习适应多样和动态的网络环境，显著优于最先进的空间重用基线，并验证了它作为未来无线网络稳健和智能解决方案的潜力。
## 6. `cs.AI` - 数字孪生技术简史 [PDF](https://arxiv.org/pdf/2511.20695), [HTML](https://arxiv.org/abs/2511.20695)
### Authors
Yunqi Zhang,Kuangyu Shi,Biao Li
### Background
数字孪生技术起源于20世纪60年代美国宇航局的航天器模拟，通过工业应用的推进，如今正在推动医疗领域的一场变革。数字孪生是一种实时数据驱动的动态虚拟实体，能够与物理系统双向互动，并持续更新。
### Innovation
数字孪生在医学中的应用包括心脏数字孪生、肿瘤数字孪生和药理学数字孪生等。这些应用通过整合成像、生物传感器和计算模型生成患者特定的模拟，为诊断、治疗规划和药物研发提供支持。新兴解决方案，如可解释的AI、联邦学习和统一的监管框架，为克服当前挑战提供了可能的途径。
### Conclusion
未来，多器官数字孪生、基因组整合和伦理治理的进步对于使数字孪生在医疗保健中从被动治疗转变为主动预防和个性化医疗至关重要。
## 7. `cs.AI` - AssurAI：构建韩语社会文化数据集以发现生成式AI潜在风险的经验 [PDF](https://arxiv.org/pdf/2511.20686), [HTML](https://arxiv.org/abs/2511.20686)
### Authors
Chae-Gyun Lim,Seung-Ho Han,EunYoung Byun,Jeongyun Han,Soohyun Cho,Eojin Joo,Heehyeon Kim,Sieun Kim,Juhoon Lee,Hyunsoo Lee,Dongkun Lee,Jonghwan Hyeon,Yechan Hwang,Young-Jun Lee,Kyeongryul Lee,Minhyeong An,Hyunjun Ahn,Jeongwoo Son,Junho Park,Donggyu Yoon,Taehyung Kim,Jeemin Kim,Dasom Choi,Kwangyoung Lee,Hyunseung Lim,Yeohyun Jung,Jongok Hong,Sooyohn Nam,Joonyoung Park,Sungmin Na,Yubin Choi,Jeanne Choi,Yoojin Hong,Sueun Jang,Youngseok Seo,Somin Park,Seoungung Jo,Wonhye Chae,Yeeun Jo,Eunyoung Kim,Joyce Jiyoung Whang,HwaJung Hong,Joseph Seering,Uichin Lee,Juho Kim,Sunna Choi,Seokyeon Ko,Taeho Kim,Kyunghoon Kim,Myungsik Ha,So Jung Lee,Jemin Hwang,JoonHo Kwak,Ho-Jin Choi
### Background
生成式AI的快速演进对其实验安全评估提出了新的要求。当前的安全数据集主要以英语为中心，并未能捕捉非英语、社会文化背景下的具体风险，例如韩语背景下的风险，而且这些数据集往往仅限于文本模态。因此，迫切需要构建新的质量可控的数据集来评估生成式AI的安全性。
### Innovation
本文介绍了一个名为AssurAI的新质量控制韩国多模态数据集，旨在评估生成式AI的安全性。该数据集包含35个适应韩语社会文化背景的AI风险因素分类，并且该数据集集结了大量跨学科专家的知识。数据集构建了严谨的质量控制过程，包括专家引导的初始构建、众包扩展、三重独立注释和迭代专家红队审核循环。此外，本文还通过试点研究验证了AssurAI的有效性。
### Conclusion
AssurAI数据集被发布给公众，以促进为韩国社区打造更安全、更可靠的生成式AI系统。
## 8. `cs.AI` - OpenApps：模拟环境差异以衡量UI代理可靠性 [PDF](https://arxiv.org/pdf/2511.20766), [HTML](https://arxiv.org/abs/2511.20766)
### Authors
Karen Ullrich,Jingtong Su,Claudia Shi,Arjun Subramonian,Amir Bar,Ivan Evtimov,Nikolaos Tsilivis,Randall Balestriero,Julia Kempe,Mark Ibrahim
### Background
自主UI代理和多模态代理的可靠性至关重要，因为用户必须信任这些代理来完成任务。现有评估依赖于固定环境，通常是对现有应用的克隆，这些环境的局限性在于只能揭示代理在一个特定环境中能否完成任务以及发生频率。然而，这些代理部署后很可能会遇到各种应用设计和内容的变化，这将影响代理完成任务的能力。因此，需要研究一种能衡量代理在不同应用版本上可靠性的方法。
### Innovation
本文开发了一个名为OpenApps的轻量级开源生态系统，其中包括六个配置可变的应用程序（如即时通讯、日历、地图等），从而实现不同版本应用上代理可靠性的衡量。通过在每个应用上运行超过10,000次独立评估，研究七个领先的多模态代理的可靠性。研究发现，在固定应用内的标准可靠性相对稳定，但在不同应用版本上的可靠性变化剧烈。任务成功率在许多代理之间可以波动超过50%。例如，Kimi-VL-3B在所有任务上的平均成功率从63%降至4%。此外，还发现了环境配置变化下代理行为（如循环或幻觉行为）存在重大差异。
### Conclusion
这些初步结果强调了在应用变化这一新维度上衡量代理可靠性的必要性。OpenApps可以在此链接中获得：this https URL。
## 9. `cs.AI` - Reasoning With a Star: A Heliophysics Dataset and Benchmark for Agentic Scientific Reasoning [PDF](https://arxiv.org/pdf/2511.20694), [HTML](https://arxiv.org/abs/2511.20694)
### Authors
Kevin Lee,Russell Spiewak,James Walsh
### Background
科学推理需要深入理解物理假设、保持一致性单位和提供清晰的科学格式。在日地物理领域，以往的工作往往侧重于简单的事实记忆，而缺乏深入的科学推理支持。
### Innovation
本文提出了一个新的日地物理数据集Reasoning With a Star，用于科学推理；同时提供了一个初始的基准测试方法。数据集由国家航空和航天管理局与大气研究大学合作组织的“Living With a Star”暑期学校问题集构建而成，包含问题背景、推理步骤、答案类型、真实目标、格式提示和元数据。一个程序化评分器利用单位感知的数值容差、符号等价性和模式验证来检查预测。研究还发现，通过系统工程原则分解工作流程能比直接提示在需要演绎推理的问题上表现更好。
### Conclusion
研究结果表明，通过系统工程原则分解工作流程的方法在解决需要演绎推理的问题上优于直接提示的方法。该数据集和基准测试方法为促进科学推理能力提供了新的资源和评估标准。
## 10. `cs.AI` - OVOD-Agent: 一种用于主动视觉推理和自我进化的马尔可夫-臂部框架 [PDF](https://arxiv.org/pdf/2511.21064), [HTML](https://arxiv.org/abs/2511.21064)
### Authors
Chujie Wang,Jianyu Lu,Zhiyuan Luo,Xi Chen,Chu He
### Background
开放词汇对象检测（OVOD）旨在通过利用语义信息使检测器在类别间进行泛化。尽管现有方法在大型视觉-语言数据集上进行了预训练，但在推断时仍然局限于固定的类别名称，导致了多模态训练与单模态推断之间的差距。之前的研究表明，通过改进文本表示可以显著提高OVOD的性能，说明文本空间仍被开发不足。
### Innovation
我们提出了OVOD-Agent，它将被动的类别匹配转换为积极的视觉推理和自我进化的检测。受Chain-of-Thought（CoT）范式启发，OVOD-Agent将文本优化过程扩展为具有明确动作的可解释视觉-CoT。此外，通过将马尔可夫转移矩阵与Arm（臂）轨迹结合用于自我监督的奖励模型（RM）优化，形成了从Arm探索到RM学习的闭环。实验表明，OVOD-Agent在各种OVOD骨干网络中提供了持续改善，特别是在稀有类别中。
### Conclusion
实验结果证明了所提出框架的有效性。对COCO和LVIS的数据集的实验表明，OVOD-Agent在各类别中提供了稳健的改进，特别是在稀有类别中，进一步验证了该框架的有效性。
## 11. `cs.AI` - 通过LLM代理和形式推理实现可信赖的法律AI [PDF](https://arxiv.org/pdf/2511.21033), [HTML](https://arxiv.org/abs/2511.21033)
### Authors
Linze Chen,Yufan Cai,Zhe Hou,Jinsong Dong
### Background
法律的合理性体现在实质合理性与形式合理性两种形式。前者涉及结果的公正性或道德可欲性，后者要求法律判决要遵循明确、一般且逻辑连贯的规则。现有的基于LLM的系统在表面文本分析方面表现出色，但不能满足指导性的司法原则所需的保证。
### Innovation
本文提出了一种名为L4M的新框架，该框架将对抗性的LLM代理与基于SMT解决器的证明结合起来，实现了自然语言的解释灵活性与符号验证的严谨性的统一。该框架由三个阶段组成：（1）法规形式化，使用特定领域的提示将法律条款转化为逻辑公式；（2）双重事实和法规提取，检察官和辩护方的LLM独立将案件叙述映射到事实元组和法规，确保角色隔离；（3）以求解为中心的裁决，自动形式化解析器将双方的论点编译为逻辑约束，不满足核心触发迭代自我批判，直到实现可满足的公式，该公式再由法官LLM口头表达成透明判决和优化的判决。
### Conclusion
实验结果表明，该系统在公共基准测试中超越了包括GPT-o4-mini、DeepSeek-V3和Claude 4在内的高级LLM以及最先进的法律AI基准，同时提供了严格的、可解释的符号性证明。
## 12. `cs.AI` - ICPO: 内在信心驱动的组相对偏好优化方法以实现高效的强化学习 [PDF](https://arxiv.org/pdf/2511.21005), [HTML](https://arxiv.org/abs/2511.21005)
### Authors
Jinpeng Wang,Chao Li,Ting Ye,Mengyuan Zhang,Wei Liu,Jian Luan
### Background
现有的增强学习与验证性奖励（Reinforcement Learning with Verifiable Rewards, RLVR）方法由于粗粒度奖励、奖励噪声和探索效率低等问题，在提升大规模语言模型（Large Language Models, LLMs）推理能力方面存在局限性，导致训练不稳定和熵坍塌。
### Innovation
提出了一种名为Intrinsic Confidence-Driven Group Relative Preference Optimization (ICPO)的方法。该方法通过比较同一输入提示下不同响应的生成概率，计算出每个响应的偏好优势分数，并将其与验证性奖励结合，指导探索过程。ICPO方法不仅解决了粗粒度奖励和奖励噪声的问题，而且有效遏制了过度自信的错误，增强了低评价高质量响应的相对优越性，防止了模型过度适应特定策略，从而促进更加全面的探索。
### Conclusion
综合实验表明，ICPO方法在四个通用领域基准和三个数学基准上均能稳定提升推理能力，相较于其他方法（如GRPO）表现更佳。
## 13. `cs.AI` - 利用大型语言模型指导结构重构以最小化双曲嵌入失真 [PDF](https://arxiv.org/pdf/2511.20679), [HTML](https://arxiv.org/abs/2511.20679)
### Authors
Melika Ayoughi,Pascal Mettes,Paul Groth
### Background
双曲几何是嵌入层次结构数据结构的有效几何方法，因此在包含层次组织或由层次语义支配的数据的机器学习应用中变得越来越重要，例如推荐系统和计算机视觉。双曲嵌入的质量紧密依赖于输入层次结构的结构，这些结构通常源自知识图谱或本体。最近的研究表明，为了获得最优的双曲嵌入，高分支因子和单继承是关键，而嵌入算法对不平衡和层次规模的变化具有鲁棒性。
### Innovation
为帮助知识工程师重新组织层次知识，该研究探讨了大型语言模型（LLMs）是否具备自动重构层次结构以满足上述标准的能力。提出了基于提示的方法，使用LLMs来变换现有层次结构，并由已知的双曲嵌入理想标准进行引导。实验结果表明，使用LLM重构的层次结构在多个标准嵌入质量度量上始终提供了更高质量的双曲嵌入，同时展示了LLM指导的层次结构重构如何实现可解释的重新组织，为知识工程师提供了解释。
### Conclusion
利用大型语言模型指导的层次结构重构能够有效提升双曲嵌入的质量，并且这种重构方法可以提供可解释的层次结构调整，从而帮助知识工程师更加有效地重新组织层次知识。
## 14. `cs.AI` - 通过受限生成改进程序技能解释：一种符号-LLM混合架构 [PDF](https://arxiv.org/pdf/2511.20942), [HTML](https://arxiv.org/abs/2511.20942)
### Authors
Rahul Dass,Thomas Bowlin,Zebing Li,Xiao Jin,Ashok Goel
### Background
在程序技能学习过程中，教学解释必须传达步骤背后的因果、目标导向和组成逻辑。尽管大型语言模型（LLMs）能提供流畅的回应，但往往会忽略结构上的重要性。本研究介绍了一种名为Ivy的人工智能辅导系统，通过结合符号Task-Method-Knowledge（TMK）模型和解析生成解释层，旨在提供结构化的、多步骤的解释，以弥补LLM的不足。
### Innovation
Ivy采用了一种符号-LLM混合架构，其中TMK模型编码因果转换、目标层次结构和问题分解，指导LLM生成解释时受到明确的结构约束。这种方法在针对意图推理的三个维度进行评估后显示出，符号约束可以持续提高针对“如何”和“为什么”问题的解释结构质量。
### Conclusion
本研究展示了教育中的可扩展AI方法，表明通过符号约束，人工智能生成的解释在智能辅导系统中增强了教育价值。
## 15. `cs.AI` - 为神经元提供保证的最优组合解释 [PDF](https://arxiv.org/pdf/2511.20934), [HTML](https://arxiv.org/abs/2511.20934)
### Authors
Biagio La Rosa,Leilani H. Gilpin
### Background
尽管神经元是深度神经网络的基本单元，但尚不清楚它们学习了什么，以及它们的知识是否与人类的知识相一致。组合解释通过逻辑规则描述神经元激活与概念之间的空间对齐，目的在于回答上述问题。通常，这些逻辑描述通过在整个概念组合空间中进行搜索来计算，但由于整个状态空间的空间对齐计算是不可行的，文献中普遍采用束搜索来限制搜索空间。然而，束搜索不能提供任何优化的理论保证，目前尚不清楚现有解释与真实最优性的接近程度。
### Innovation
本文通过提出第一个计算保证最优组合解释的框架，解决了这一问题。具体而言，本文提出了：(i) 一种分解方法，以识别影响空间对齐的因素；(ii) 一种估计搜索任一阶段对齐程度的启发法；(iii) 第一个可以在合理时间内计算最优组合解释的算法。本框架被用于分析组合解释中最流行的设置（计算机视觉领域和卷积神经网络）中最优解释与非最优解释之间的差异。结果显示，束搜索中的10%-40%解释在涉及重叠概念时是次优的。最后，通过使用本文提出的分解和启发法指导的束搜索变体进行了评估，该变体在提供更大的参数和计算资源灵活性的同时，与前一代方法相比具有更短的运行时间。
### Conclusion
使用本框架，我们分析了最流行的组合解释设置中最优解释与非最优解释之间的差异。结果显示，束搜索中约10%-40%的解释在涉及重叠概念时是次优的。最后，通过使用我们的分解和启发法指导的束搜索变体进行了评估，证明该方法在提供更大的灵活性和计算资源的同时，与过去的方法相比具有更好的运行时间。
## 16. `cs.AI` - ENACT：使用主观交互的世界建模评估蕴含认知 [PDF](https://arxiv.org/pdf/2511.20937), [HTML](https://arxiv.org/abs/2511.20937)
### Authors
Qineng Wang,Wenlong Huang,Yu Zhou,Hang Yin,Tianwei Bao,Jianwen Lyu,Weiyu Liu,Ruohan Zhang,Jiajun Wu,Li Fei-Fei,Manling Li
### Background
背景介绍了蕴含认知理论，认为智能源于传感器运动交互，而非被动观察。本文探讨了现代视觉-语言模型（VLMs）是否展现出蕴含认知的特征。基于这一理论，ENACT 提供了一个基准来评估 VLMs 的蕴含认知能力，通过视觉问答（VQA）格式重新定义环境建模任务，将评估转化为部分可观测马尔可夫决策过程（POMDP）中的场景图变化序列重排序任务。
### Innovation
创新在于 ENACT 提出了一种评估视觉-语言模型蕴含认知能力的新颖方法，将世界建模转化为视觉问答格式中的场景图变化序列重排序任务，并评估了模型在长期交互中的表现，揭示了模型在处理逆向任务时的表现优于正向任务以及人类的表现出众，同时发现模型存在人类中心的偏见。
### Conclusion
实验结果表明，前沿的 VLMs 在交互距离较长的任务上表现较差，而且在处理逆向任务时表现优于正向任务。模型表现出人类中心的偏见，如偏好右手法动作，以及在摄像头内参数或视角偏离人类视觉时会出现退化。
## 17. `cs.AI` - Prune4Web：用于Web代理的DOM树裁剪编程 [PDF](https://arxiv.org/pdf/2511.21398), [HTML](https://arxiv.org/abs/2511.21398)
### Authors
Jiayuan Zhang,Kaiquan Chen,Zhihao Lu,Enshen Zhou,Qian Yu,Jing Zhang
### Background
网络自动化利用智能代理执行高级任务，通过模拟与网页界面的人机交互。尽管基于大语言模型（LLM）的网络代理具备一定能力，但在处理复杂的现实世界网页时，仍面临巨大挑战。主要原因是文档对象模型（DOM）结构的庞大，通常包含10,000到100,000个标记。现有策略通常依赖粗略的DOM截断或采用低效的启发式方法以及独立的排名模型，导致精确度和可扩展性之间难以取得平衡。
### Innovation
Prune4Web引入了一种新颖的方法，将DOM处理从资源密集型LLM阅读转移到高效的程序化裁剪。中心思想是DOM树裁剪编程，其中LLM生成可执行的Python评分脚本，根据分解子任务的语义线索动态过滤DOM元素。这种方法避免了LLM需要摄入原始的庞大DOM，而是将遍历和评分任务委托给轻量级且可解释的程序。此外，提出了一种专门的数据标注管道和两轮对话训练策略，以优化统一框架下的规划器、程序化筛选器和定位器。实验结果表明，性能达到业界领先水平。特别是，在底层定位任务中，Prune4Web将准确率从46.8%提升至88.28%，证明其在实际网络自动化中的有效性。
### Conclusion
Prune4Web实现了DOM元素候选的25到50倍减少，从而实现精确行为定位，同时减少了注意力分散。通过统一框架下的专门数据标注管道和两轮对话训练策略，Prune4Web取得了显著的性能提升，验证了其对网络自动化领域的有效性和实用性。
## 18. `cs.AI` - 因果关系无需因果模型 [PDF](https://arxiv.org/pdf/2511.21260), [HTML](https://arxiv.org/abs/2511.21260)
### Authors
Joseph Y. Halpern(Cornell University),Rafael Pass(Cornell University)
### Background
当前对（实际）因果关系最突出的定义归功于Halpern和Pearl。这一定义使用因果模型（也称为结构方程模型）来定义。本文通过对定义进行抽象化处理，提取其关键特征，使定义能够应用于任何可以定义反事实现象的其他模型。这样处理可以带来多方面的好处，包括能够应用该定义到更广泛范围的模型中，即使这些模型允许回溯因果关系，也能够处理涉及析取、否定、信念和嵌套反事实的公式，这些都是Halpern-Pearl定义无法处理的。
### Innovation
通过对因果定义进行抽象化处理，本文不仅扩大了定义的应用范围，使其能够应用于包括回溯在内的各种模型，而且还能够使用该定义来确定A是否是B的原因，即使A和B包括析取、否定、信念和嵌套反事实等逻辑组合。此外，本文还扩展了这些概念以获得一种抽象的解释定义，可以应用于因果模型之外的领域，进一步深化了对定义本身以及因果模型特征的理解。
### Conclusion
通过抽象化因果定义的方法，本文不但在更大的模型范围内应用了该定义，而且其定义的公理性本质使得它能够进一步应用于解释的定义中，即使在复杂公式的情况下也能够保持定义的适用性。这种抽象化的定义为因果推理和其他逻辑相关问题提供了更广泛的基础，有助于深入理解因果关系的本质特征。
## 19. `cs.AI` - MADRA: 多智能体辩论的风险意识实体规划 [PDF](https://arxiv.org/pdf/2511.21460), [HTML](https://arxiv.org/abs/2511.21460)
### Authors
Junjian Wang,Lidan Zhao,Xi Sheryl Zhang
### Background
在实体人工智能代理执行任务规划时确保其安全是其实际部署的关键，尤其是在家庭环境中，危险指令带来的风险非常显著。现有的方法常常存在训练偏好对齐时计算成本高的问题，或者在使用单智能体安全提示时过度拒绝。这限制了现有方法在保证安全性和任务性能之间的平衡。
### Innovation
我们提出了一个无需训练的多智能体辩论风险评估框架 MADRA，该框架通过集体推理增强了安全意识，同时不牺牲任务性能。MADRA 使用多个基于大语言模型的智能体来辩论给定指令的安全性，指导一个关键评估器根据逻辑有效性、风险识别、证据质量和清晰度来评分。通过迭代辩论和共识投票，MADRA 显著降低了误拒率，并保持了对危险任务的高敏感性。此外，我们还介绍了一种分层认知协作规划框架，结合了安全、记忆、规划和自我进化机制，以实现持续学习，提高任务成功率。我们还贡献了一个名为 SafeAware-VH 的基准数据集，用于在 VirtualHome 中进行安全意识任务规划，包含了 800 条注释指令。我们在 AI2-THOR 和 VirtualHome 上的广泛实验表明，我们的方法在安全性和执行效率方面超越了现有的方法，能够拒绝超过 90% 的不安全任务，同时确保对安全任务的拒绝率很低。
### Conclusion
我们的工作提供了一种可扩展的、模型无感知的解决方案，用于构建可信赖的实体智能代理，同时保持任务的成功率和安全性。
## 20. `cs.AI` - 使用ChatDRex进行对话式无代码和多智能体疾病模块识别及药物重定位预测 [PDF](https://arxiv.org/pdf/2511.21438), [HTML](https://arxiv.org/abs/2511.21438)
### Authors
Simon Süwer,Kester Bagemihl,Sylvie Baier,Lucia Dicunta,Markus List,Jan Baumbach,Andreas Maier,Fernando M. Delgado-Chaves
### Background
现有药物研发过程时间长且成本高昂，而通过已有药物进行药物重定位提供了更高效、节省成本的替代方案。然而，计算机辅助的药物重定位候选物预测仍然充满挑战，需要跨多个学科（如药理学、临床医学、生物学、生物信息学）的专业人士合作。当前的专业算法和工具往往仅关注整体问题的部分方面，且异构和非结构化数据要求专业用户参与，导致这些数据服务难以在工作流程中无缝集成。
### Innovation
ChatDRex提出了一种基于对话的多智能体系统，旨在促进复杂生物信息学分析以实现基于网络的药物重定位预测。它建立在集成系统医学知识图谱NeDRex之上，提供自然语言访问其广泛的生物医学知识图谱，并集成生物信息学代理进行网络分析、药物重定位，以及具有良好功能一致性的验证代理。此外，还配备了文献挖掘代理以及用于科学讨论结果的代理。其灵活的多智能体设计将特定任务分配给专业智能体，包括查询路由、数据检索、算法执行和结果可视化。专用推理模块帮助用户保持参与，有助于幻觉检测。ChatDRex使不具备计算机科学背景的医生和研究人员能够通过自然语言控制复杂分析，从而简化了生物信息学的使用过程，为药物重定位提供了有价值的资源，促进了临床专家生成假设并探索药物重定位机会，最终加快了新型疗法的发现，推动了个性化医学和转化研究的进步。
### Conclusion
ChatDRex通过基于对话的多智能体系统推动了疾病模块识别和药物重定位预测的发展，使得非专业用户也能进行复杂的生物信息学分析，提高了药物重定位的过程效率和科学价值，加速了新型疗法的发现，为个性化医学和转化研究铺平了道路。
## 21. `cs.AI` - EWE: 极端天气分析的智能代理框架 [PDF](https://arxiv.org/pdf/2511.21444), [HTML](https://arxiv.org/abs/2511.21444)
### Authors
Zhe Jiang,Jiong Wang,Xiaoyu Yue,Zijie Guo,Wenlong Zhang,Fenghua Ling,Wanli Ouyang,Lei Bai
### Background
极端天气事件对全球社会构成了日益严重的风险，强调了深入理解其物理机制的紧迫性。然而，现有的劳动密集型专家主导的诊断模式造成了分析瓶颈，阻碍了科学进步。虽然AI在地球科学预测方面取得了显著进展，但自动化诊断推理这一同等重要的挑战尚未得到充分探索。
### Innovation
本文介绍了Extreme Weather Expert (EWE)，这是首个专为这一任务设计的智能代理框架。EWE 通过知识引导的规划、闭环推理和定制的气象工具包模拟专家工作流程，能够从原始气象数据中自主产生和解释多模态可视化，从而实现全面的诊断分析。此外，EWE 还引入了该新兴领域的首个基准测试，其中包括103个高影响事件的数据集和一个新的分步评估指标。
### Conclusion
EWE 是迈向自动化科学发现的重要一步，并有可能将知识和智力资源普及化，特别是对于受极端天气影响的欠发达国家。
## 22. `cs.AI` - 从预测到展望：人工智能在设计负责任的未来中的作用 [PDF](https://arxiv.org/pdf/2511.21570), [HTML](https://arxiv.org/abs/2511.21570)
### Authors
Maria Perez-Ortiz
### Background
在快速的技术进步和复杂的全球挑战背景下，负责任的前瞻已成为政策制定者应对未来不确定性并塑造未来的必要框架。负责任的前瞻涉及对新兴机遇和风险的道德预见，并致力于创造前瞻性、可持续和负责任的未来设计。
### Innovation
提出了“负责任的计算前瞻”的概念，探讨了以人为中心的人工智能和计算建模在推动负责任的前瞻中的作用，提出了这一新领域的基础原则，并介绍了当前塑造这一领域的AI驱动的前瞻工具。AI，特别是与模拟和情景分析相结合，增强了决策者应对不确定性、评估风险和制定旨在实现可持续和韧性的策略的能力。
### Conclusion
我们主张将AI有选择地整合到前瞻实践中，以赋能决策者和社区，应对21世纪的伟大挑战。负责任的计算前瞻强调AI作为决策支持工具的作用，既不替代也不取代决策者的判断，而是促进形成具有韧性和伦理价值的未来。
## 23. `cs.AI` - 新伪布尔传播的混合启发式方法 [PDF](https://arxiv.org/pdf/2511.21417), [HTML](https://arxiv.org/abs/2511.21417)
### Authors
Mia Müßig,Jan Johannsen
### Background
在伪布尔求解中，最成功的单元传播策略是结合了观察项方案与计数方法的混合模式。当前主要使用的RoundingSAT求解器采用了这种模式。
### Innovation
本短文介绍了适用于这种混合决策的新启发式方法，这些方法能够在RoundingSAT求解器中大幅超越当前的方法。
### Conclusion
通过引入新的启发式方法，能够在伪布尔传播中显著提高性能。
## 24. `cs.AI` - 开放性数学问题的悲观验证 [PDF](https://arxiv.org/pdf/2511.21522), [HTML](https://arxiv.org/abs/2511.21522)
### Authors
Yanxing Huang,Zihan Tang,Zejin Lin,Peng Li,Yang Liu
### Background
当前验证性能的关键限制在于错误检测能力。为此，作者设计了多种悲观验证变体，这些简单的工作流程可以显著提高开放性数学问题的验证效果。
### Innovation
提出了悲观验证方法，通过为同一证明构建多个并行验证，如果任何一个验证报错，则证明被视为错误。该方法无需大量计算资源，显著提升了多种数学验证基准的性能，在测试时扩展性甚至超过了扩展长-CoT。进一步分析表明，强大模型中的大部分假阴性实际上是原始数据集的注释错误导致的，因此该方法的实际性能被低估。
### Conclusion
自我验证对于数学问题可以有效提高语言模型输出的可靠性和性能，并在实现长期数学任务方面发挥关键作用。研究悲观验证将有助于增强各种任务中语言模型的数学能力。
## 25. `cs.AI` - 大型语言模型内在规划能力的局限性 [PDF](https://arxiv.org/pdf/2511.21591), [HTML](https://arxiv.org/abs/2511.21591)
### Authors
Charles Schepanowski,Charles Ling
### Background
大型语言模型（LLMs）在多任务基准测试中表现出色，但在规划能力和状态推理能力方面的能力仍然不明确。本文通过8拼图游戏直接研究这一能力，不依赖于代码执行或其他工具，旨在对LLMs进行精确的、逐步的评估。
### Innovation
使用8拼图作为任务，该任务需要状态跟踪和目标导向的规划，从而可以进行细致的评估。测试了四个模型在不同提示条件（零样本、链式思维、思维算法）以及层次化的纠正反馈下的表现，即使在外部移动验证器的帮助下，模型们也没有解决任何难题，揭示了模型在内部状态表示和启发式规划方面的局限性。
### Conclusion
在没有外部工具（如代码解释器）的情况下，当前的LLMs在规划方面存在显著限制，进一步的进步可能需要维护显式状态和进行结构化搜索的机制。
## 26. `cs.AI` - 专家人设语言模型的自我透明度失败：大规模行为审计 [PDF](https://arxiv.org/pdf/2511.21569), [HTML](https://arxiv.org/abs/2511.21569)
### Authors
Alex Diep
### Background
如果语言模型在专业领域无法可靠地透露其AI身份，用户将无法信任其专业限度。该研究探讨了在高风险专业领域分配给模型专家人设时，模型的自我透明度情况，这些领域中错误的专业知识可能对用户造成伤害。
### Innovation
研究使用常见设计方法，对16个开放权重模型（参数范围从4B到671B）进行了19200次试验的审核。研究发现，不同专业人设的模型在自我透明度方面表现出明显的领域特异性差异，提示自我透明度的效果在一些领域会引发用户过度泛化信任。此外，研究成果表明，模型的自我透明度受到训练因子而不是模型规模的影响。
### Conclusion
这些发现表明，模型的自我透明度反映了训练因素而不是规模。组织不能假设安全特性在部署环境中有效，需要进行具体行为设计和实证验证。
## 27. `cs.AI` - 搭建不可避免的先验知识鸿沟：一种对比因果建模框架 [PDF](https://arxiv.org/pdf/2511.21636), [HTML](https://arxiv.org/abs/2511.21636)
### Authors
Peter S. Hovmand,Kari O'Donnell,Callie Ogland-Hand,Brian Biroscak,Douglas D. Gunzler
### Background
AI/ML模型因其创新性得以快速发展，用于解决以往无法解决的问题。然而，这些模型也引发了放大人类偏见的潜在负面影响。支持负责任AI/ML的研究者们尝试利用系统动力学的更丰富因果模型来更好地指导负责的AI/ML开发。不过，一个主要障碍在于将基于不同假设的方法结合起来（即Dana Meadows提出的“不可避免的先验”）。因此，本文提出的一种框架，将系统动力学和结构方程建模结合进一个共同的数学框架，用于从分布生成系统、开发方法和比较结果，以指导系统动力学在数据科学和AI/ML应用中的基础认识论。
### Innovation
本文提出了一种框架，将系统动力学和结构方程建模结合进一个共同的数学框架，这能够生成从分布而来的系统，发展对比方法，并比较结果，从而有助于确定系统动力学在数据科学和AI/ML中的基础认识论。
### Conclusion
本文提出的方法既能从分布生成系统，也能开发对比方法和比较结果，旨在促进系统动力学用于数据科学和AI/ML应用的知识论基础的确定。
## 28. `cs.AI` - SpatialBench：针对空间认知评估多模态大型语言模型 [PDF](https://arxiv.org/pdf/2511.21471), [HTML](https://arxiv.org/abs/2511.21471)
### Authors
Peiran Xu,Sudong Wang,Yao Zhu,Jianing Li,Yunjian Zhang
### Background
现有基准通常简化了空间认知，将其减少为单一维度的度量标准，这无法捕捉到空间能力的层次结构和相互依赖性。而空间认知是衡量现实世界多模态智能的基本因素，允许模型有效互动。现有研究中，多模态大型语言模型（MLLMs）取得了一定进展，但当前的基准未能充分评估高级空间计算能力。
### Innovation
本文提出了一种分层的空间认知框架，将空间智能分解为从基本观察到高级计划的五个逐步复杂级别。该研究构建了SpatialBench，这是一个涵盖15个任务的大规模、精细基准，这些任务与认知等级对齐。引入了一种高层次的、能力导向的度量标准，该标准能够准确评估模型的整体空间推理能力。通过大量的实验揭示了不同认知层次上的性能差异，并通过人类测试展示了人类和MLLMs在空间认知中的不同表现。
### Conclusion
本文建立了第一个系统性框架来衡量MLLMs的分层次空间认知能力，为未来的空间智能系统奠定了基础。研究结果展示了MLLMs在感知嵌入方面表现出色，但在符号推理、因果推断和规划方面存在局限性，而人类在空间抽象方面具有选择性和目标导向性。
## 29. `cs.AI` - 具有情感智能的智能代理：当前趋势、挑战和未来展望 [PDF](https://arxiv.org/pdf/2511.20657), [HTML](https://arxiv.org/abs/2511.20657)
### Authors
Raziyeh Zall,Alireza Kheyrkhah,Erik Cambria,Zahra Naseri,M.Reza Kangavari
### Background
随着情感智能代理在人机交互和跨行业整合中扮演重要角色，情感计算旨在设计能够识别、引发和表达人类情感的智能系统。之前的研究主要集中在该领域的特定方面，但很少全面涵盖情感理解、引发和表达及其相关挑战。本研究通过提供有关人工情感智能核心组件的综合视图填补了这一空白，涵盖了多模态数据处理中的情感理解，以及情感认知，包括认知评价、情绪映射和决策、学习和推理中的适应性调节。此外，该研究还探讨了情感表达在文本、语音和面部模态中的合成，以提升人机交互。
### Innovation
该论文通过提供综合视图全面地覆盖了人工情感智能的核心组件，包括情感理解、情感认知和情感表达的合成，并且还指出了当前所面临的关键挑战和问题，并探讨了生成技术在未来情感计算中的潜在应用。
### Conclusion
该研究总结了具有情感智能的智能代理的发展现状，并强调了未来研究方向，特别是生成技术在推进情感计算中的潜力。
## 30. `cs.AI` - 使用AI驱动的视频讲座改造高等教育 [PDF](https://arxiv.org/pdf/2511.20660), [HTML](https://arxiv.org/abs/2511.20660)
### Authors
Dengsheng Zhang
### Background
将人工智能（AI）融入视频讲座制作有望通过简化内容创建和提高访问性来革新高等教育。现有的全自动化文本转视频平台无法保留教学意图，且难以确保剧本与幻灯片同步、叙事连贯性和定制化。本文探讨了一种半自动工作流，该工作流结合了Google Gemini进行脚本生成、Amazon Polly进行语音合成以及Microsoft PowerPoint进行视频装配。
### Innovation
该混合方法保留了教学意图并确保了脚本与幻灯片的同步、叙事连贯性和个性化。 Gemini在生成准确且与视觉丰富的学术演示文稿相关联的脚本方面表现出色，Polly则提供了自然语音叙述，具备可控制的节奏。通过两门课程的试点研究，发现AI生成的指导视频（AIIV）在学习成果方面与人类指导视频（HIV）相当，学生认为AIIV清晰、连贯且易于使用，但仍存在音频质量和缺少类人类的虚拟形象的局限。
### Conclusion
AI辅助视频制作可以减轻教师的工作负担，提高可扩展性，并提供有效的学习资源。未来在合成语音和虚拟形象方面的改进将进一步提升学习者的参与度。
## 31. `cs.AI` - 国际学生知识领域导向的大型语言模型评估 [PDF](https://arxiv.org/pdf/2511.20653), [HTML](https://arxiv.org/abs/2511.20653)
### Authors
Claudinei Daitx,Haitham Amar
### Background
大型语言模型（LLMs）越来越被用于解答涉及签证、入学、奖学金等留学生高风险问题的咨询。然而，关于LLMs能否可靠地提供建议以及是否会产生未被支持的内容（幻觉）仍未清楚。本文在MakeStudyAbroad平台的教学技术工作流程中对实时问题进行评价，评估当前LLMs在该领域的表现，以提供清晰且领域导向的综述。
### Innovation
本文采用真实问题作为评测量表，评估LLMs在准确性和幻觉两个方面的表现。问题按照领域范围进行分类，给出基于领域的评分标准，不仅考虑信息的正确性和完整性，还关注LLMs引入不必要信息的情况。此外，还报告了忠诚度和答案相关性等指标，提供了公平、头对头的比较方法。
### Conclusion
本文为确定哪些模型最适合为留学生提供咨询建议提供了清晰的视野，挖掘了常见失败模式，并为教育和咨询场景中的LLMs部署提供了一个实用的、可重用的审核协议。
## 32. `cs.AI` - CodeVaani：具有多语言语音的编程学习助手 [PDF](https://arxiv.org/pdf/2511.20654), [HTML](https://arxiv.org/abs/2511.20654)
### Authors
Jayant Havare,Srikanth Tamilselvam,Ashish Mittal,Shalaka Thorat,Soham Jadia,Varsha Apte,Ganesh Ramakrishnan
### Background
编程教育往往假设学生具备英语能力和基于文本的交互，这给许多地区（如印度）多语言学生带来了障碍。
### Innovation
CodeVaani 是一个多语言语音驱动的学习助手，集成在 Bodhitree 教学管理系统中，帮助学习者在其母语中探索编程概念。系统包括印地语ASR、代码感知转录精炼模块和生成相关答案的代码模型。响应采取文本和语音形式，便于自然交互。
### Conclusion
CodeVaani 在一项针对28名初学者程序员的研究中，响应准确率达到75%，超过80%的参与者对使用体验感到满意。相比课堂教学辅助，该框架提供了即需即用的可用性、可扩展性以支持大量学习者，以及通过多语言支持降低英语水平有限学生的学习门槛。示例和演示视频也已提供，以展示这些功能并强调语音AI系统如何使编程教育更加包容。
## 33. `cs.AI` - MTTR-A: 测量多智能体系统中的认知恢复延迟 [PDF](https://arxiv.org/pdf/2511.20663), [HTML](https://arxiv.org/abs/2511.20663)
### Authors
Barak Or
### Background
在大规模、分布式的人工智能系统中，确保认知稳定性是自主多智能体系统（MAS）面临的中心挑战。现有的可观察性工具仅监测系统输出，但无法量化智能代理工作流在失去推理一致性后恢复速度的快慢。
### Innovation
本文创新地将经典的可靠性指标（如平均恢复时间MTTR、平均故障间隔时间MTBF及其相关比率）应用于认知领域，定义了MTTR-A（Agentic系统的平均恢复时间），作为运行时的认知恢复延迟度量。通过使用AG News语料库和LangGraph编排框架进行基准模拟，本文展示了自动化反射机制和人工审批干预的恢复速度，并通过正式化恢复延迟使其成为分布式推理的一个可量化属性，为代理认知的运行时可靠性奠定了基础。
### Conclusion
本文通过将恢复延迟正式化为分布式推理的可量化属性，并建立了恢复时间与认知运行时间之间可靠性界限，为代理认知的运行时依赖性奠定了基础，将认知恢复从一种天真的过程转变为标准化和可解释的性能指标。
## 34. `cs.AI` - Context-Aware Visual Prompting: 使用大规模语言模型和代理自验证自动构建地理空间网络仪表板以支持决策 [PDF](https://arxiv.org/pdf/2511.20656), [HTML](https://arxiv.org/abs/2511.20656)
### Authors
Haowen Xu,Jose Tupayachi,Xiao-Ying Yu
### Background
基于Web的地理空间仪表板在风险分析和决策支持方面的发展常因大数据和多维环境数据的可视化困难、实现复杂性和自动化程度低而面临挑战。
### Innovation
提出了一种利用大型语言模型（LLMs）生成的AI框架，通过用户定义的输入（如UI框架、需求和数据源）自动化创建交互式地理空间仪表板。该框架引入了结构化的知识图谱，嵌入领域知识以实现准确且上下文相关的代码完成。核心机制是上下文感知视觉提示（CAVP），从视觉布局中提取和编码接口语义，引导LLM驱动的代码生成。此外，该框架还集成了一个自我验证机制，利用基于代理的LLM和Pass@k评估以及语义度量确保输出可靠性。
### Conclusion
与基线方法相比，该方法在性能上得到了改进，并且在第三方平台的基础上增加了功能。该框架展示了多页完整的界面实现，并成功进行了链式思维AI代理的自验证。这种集成方法通过结构化的知识和视觉提示，为增强风险管理与决策提供了创新的地理空间解决方案。
## 35. `cs.AI` - 具备生长和细化多模态语义记忆的人工智能学习者 [PDF](https://arxiv.org/pdf/2511.21678), [HTML](https://arxiv.org/abs/2511.21678)
### Authors
Weihao Bo,Shan Zhang,Yanpeng Sun,Jingjing Wu,Qunyi Xie,Xiao Tan,Kunbin Chen,Wei He,Xiaofan Li,Na Zhao,Jingdong Wang,Zechao Li
### Background
现有的大规模语言模型（MLLMs）在解决问题方面表现出很强的能力，但它们是独立地解决每个问题的，且常常重复同样的错误。现有的记忆增强代理主要存储过去轨迹用于重用，但基于轨迹的记忆会受到短暂性偏见的影响，逐渐失去关键领域知识。更为严重的是，在真正多模态问题解决的设置中，这些代理记录的仅仅是单一模态的行为轨迹，未能保留视觉注意力与逻辑推理的联合贡献。这与人类认知过程存在根本性不一致：人类的语义记忆是多模态且整合的，保留视觉和抽象知识，通过协调但不依赖的表示流实现。
### Innovation
为了纠正上述问题，本研究提出了ViLoMem，一个双流记忆框架，构建了紧凑且基于模式的记忆。ViLoMem分别编码视觉干扰模式和逻辑推理错误，使MLLMs能够从成功和失败的经历中学习。该系统遵循“生长和细化”的原则，逐步累积和更新多模态语义知识，保留稳定而普适的策略，避免灾难性遗忘。ViLoMem在六个多模态基准测试中一致提高了pass@1精度，并显著减少了重复的视觉和逻辑错误。消融实验确认了双流记忆中的干扰-幻觉分离的必要性，证明了错误意识的多模态记忆对于终身和跨域智能学习的价值。
### Conclusion
通过采用ViLoMem框架，MLLMs在多模态问题解决中可以获得显着改进，增强了错误意识并且避免了灾难性遗忘。项目网页将在此提供： <this https URL>。
## 36. `cs.AI` - 使用操作推理和重叠施瓦茨交替法的混合耦合 [PDF](https://arxiv.org/pdf/2511.20687), [HTML](https://arxiv.org/abs/2511.20687)
### Authors
Irina Tezaur,Eric Parish,Anthony Gruber,Ian Moore,Christopher Wentland,Alejandro Mota
### Background
本文提出了一种新的混合方法，用于结合子域局部非侵入式操作推理（OpInf）降阶模型（ROMs）与其他子域局部高保真度全阶模型（FOMs）。这种方法利用重叠施瓦茨交替法（O-SAM），解决多尺度建模和模拟中的主要挑战，特别是传统高保真度模拟所需的长时间运行和复杂网格生成需求。
### Innovation
通过利用O-SAM的灵活性，本文方法实现了不同模型、网格和时间积分方案的无缝集成，提高了计算效率并保持高精度。本文通过一系列复杂的三维固体力学问题数值实验展示了与传统FOM-FOM耦合相比最高可达106倍的速度提升。
### Conclusion
本文的工作为工程应用中的更高效模拟工作流铺平了道路，并具有扩展到多种偏微分方程的潜力。
## 37. `cs.AI` - 大型语言模型推理中的认知偏差妨碍了临床肿瘤病案的解释 [PDF](https://arxiv.org/pdf/2511.20680), [HTML](https://arxiv.org/abs/2511.20680)
### Authors
Matthew W. Kenaston(1),Umair Ayub(1),Mihir Parmar(2),Muhammad Umair Anjum(1),Syed Arsalan Ahmed Naqvi(1),Priya Kumar(1),Samarth Rawal(1),Aadel A. Chaudhuri(4),Yousef Zakharia(3),Elizabeth I. Heath(5),Tanios S. Bekaii-Saab(3),Cui Tao(6),Eliezer M. Van Allen(7),Ben Zhou(2),YooJung Choi(2),Chitta Baral(2),Irbaz Bin Riaz(1 and 3 and 6) ((1) Mayo Clinic College of Medicine and Science, Phoenix, AZ, (2) School of Computing and AI, Arizona State University, Tempe, AZ, (3) Mayo Clinic Comprehensive Cancer Center, Phoenix, AZ, (4) Department of Radiation Oncology, Mayo Clinic, Rochester, MN, (5) Department of Oncology, Mayo Clinic, Rochester, MN, (6) Department of Artificial Intelligence and Informatics, Mayo Clinic, Rochester, MN, (7) Dana-Farber Cancer Institute, Harvard Medical School, Boston, MA)
### Background
尽管大型语言模型在临床基准测试中表现出色，但在涉及肿瘤学决策支持时，这些模型可能通过不正确的推理得出正确的结论。这种错误的推理模式对安全性有影响，但现有的基于准确性的评估方法并未捕捉到这一点。因此，有必要研究大型语言模型在临床应用中的推理错误，并开发出相应的评估和改进策略。
### Innovation
本文通过两组病例的回顾性研究，开发了一种基于GPT-4链式推理回应的层次认知错误分类体系，并测试了其在临床中的相关性。研究使用了CORAL数据集中的乳腺癌和胰腺癌病案，对600条推理路径进行了标注，定义了三层分类体系，将计算错误映射到认知偏见框架中。研究还验证了该分类体系的临床相关性，涉及前列腺癌咨询病案，涵盖局部到转移性疾病。研究发现了23%的推理错误，其中以确认偏见和锚定偏见最为常见。推理错误与指南不一致且可能有害的建议相关，特别是在晚期疾病管理中更为明显。目前最先进的自动评估器只能检测错误的存在，但无法可靠地分类不同类型。
### Conclusion
研究显示大型语言模型在临床部署前推理不准确时，可能会提供流畅但不安全的建议。分类体系提供了可推广的框架，用于评估和改进推理的准确性，在临床部署前使用。
## 38. `cs.AI` - 捍卫图灵测试及其遗产 [PDF](https://arxiv.org/pdf/2511.20699), [HTML](https://arxiv.org/abs/2511.20699)
### Authors
Bernardo Gonçalves
### Background
论文讨论了图灵原始测试在Weizenbaum之后被误用的问题，并指出传统上对图灵测试的六种最常见的批评是不公平的，这些批评不仅针对图灵的论点，也针对人工智能历史的发展。
### Innovation
本文旨在为图灵测试及其在人工智能领域的发展正名，挑战过往对图灵测试的误解和不公正批评。
### Conclusion
最终，本文强调图灵测试仍然是评估机器智能的标准方法，并且其在人工智能领域的贡献不应被忽视和低估。
## 39. `cs.AI` - 当LLMs无法提供帮助：在营养领域的LLMs实际效果评估 [PDF](https://arxiv.org/pdf/2511.20652), [HTML](https://arxiv.org/abs/2511.20652)
### Authors
Karen Jia-Hui Li,Simone Balloccu,Ondrej Dusek,Ehud Reiter
### Background
语言模型（尤其是聊天机器人形式）在人们中的信任度越来越大，但这种信任经常被缺乏外部评估所削弱。特别是在营养领域，随机对照试验（RCTs）是金标准，专家们要求使用RCTs来实现基于证据的应用。语言模型在这方面的结果令人鼓舞，但这些结果主要是基于内在评价的，而忽视了它们在实际应用中的效果。
### Innovation
本文通过设计并实施首个涉及营养领域的随机对照试验（RCTs），将语言模型集成到基于规则的聊天机器人中，增强了其会话多样性和营养咨询功能。研究结果显示，虽然基于语言模型的功能在内在评价中表现良好，但在实际应用中未能提供持续的好处，这突显了内在评价与实际影响之间的关键差距，强调了需要跨学科、以人为本的方法。
### Conclusion
研究表明，语言模型在实际应用中的效果可能与它们在内在评估中的表现不同。重要的是要认识到这种差距并采取跨学科、以人为本的方法来解决这个问题。所有代码和结果可通过提供的链接访问。
## 40. `cs.AI` - 现代Hopfield网络隐状态在Transformer中的作用 [PDF](https://arxiv.org/pdf/2511.20698), [HTML](https://arxiv.org/abs/2511.20698)
### Authors
Tsubasa Masumura,Masato Taki
### Background
基于Hopfield网络的记忆模型和基于键值机制的自注意力机制是深度学习记忆机制研究中的热点方法。研究表明，现代霍普菲尔德网络（MHN）在绝热近似的状态更新规则与Transformer的自注意力层一致。在此基础上，本文深入探讨了MHN与自注意力之间的关系。
### Innovation
通过引入MHN的隐状态到自注意力机制中，提出了一种新的注意力机制，称为现代霍普菲尔德注意力（MHA），允许注意力分数从Transformer的输入层继承到输出层，从而显著改善了注意力权重的性质。此外，MHA还可以系统地提高准确性，而不增加Vision Transformer或GPT的训练参数。
### Conclusion
研究结果表明，Hopfield网络可以为改善Transformer架构提供有用的视角，指出Hopfield网络隐状态在加强Transformer性能中的作用。
## 41. `cs.AI` - 音乐谱理解基准：评估大型语言模型对完整音乐谱的理解 [PDF](https://arxiv.org/pdf/2511.20697), [HTML](https://arxiv.org/abs/2511.20697)
### Authors
Congren Dai,Yue Yang,Krinos Li,Huichi Zhou,Shijie Liang,Zhang Bo,Enyang Liu,Ge Jin,Hongran An,Haosen Zhang,Peiyuan Jing,KinHei Lee,Zhenxuan Zhang,Xiaobing Li,Maosong Sun
### Background
理解和解析完整的音乐谱需要在音高、节奏、和声和结构等符号结构上进行推理。虽然大型语言模型（LLMs）和视觉-语言模型（VLMs）在自然语言和多模态任务上取得了快速进展，但它们对音乐符号的理解仍然没有得到充分探索。
### Innovation
提出了Music Score Understanding Benchmark（MSU-Bench），这是一个大规模、人类精心设计的基准，用于评估乐谱水平的音乐理解，涵盖文本（ABC 符号）和视觉（PDF）两种模态。该基准包括1800个生成的问题-答案（QA）对，来自巴赫、贝多芬、肖邦、德彪西等多首作品，分为四个层次的认知：起始信息、符号与音符、和弦与和声，以及织体与结构。通过对15+种最先进的（SOTA）模型进行了广泛的零样本和微调评估，揭示了明显的模态差距，层面上的成功率不稳固，以及维持多层面正确性的难度。微调在两种模态下显著提高了性能，同时保持了普遍知识，将MSU-Bench确立为未来人工智能（AI）、音乐学和多模态推理交叉领域研究的基础。
### Conclusion
微调显著提升了两种模态下的性能，同时保留了通用知识，将MSU-Bench确立为未来人工智能、音乐学和多模态推理交叉领域研究的基础。
## 42. `cs.AI` - 基于数据无关知识蒸馏的剪枝后精度恢复 [PDF](https://arxiv.org/pdf/2511.20702), [HTML](https://arxiv.org/abs/2511.20702)
### Authors
Chinmay Tripurwar,Utkarsh Maurya,Dishant
### Background
深度神经网络的计算复杂度和内存消耗较高，模型剪枝是一种常用的降低这些复杂度的技术。但全局无结构剪枝往往会导致精度显著下降，通常需要在原训练数据集上进行微调才能恢复性能。在医疗保健或金融等隐私敏感领域，部署后原始训练数据往往受限于法规（如GDPR和HIPAA）。该研究旨在通过数据无关的知识蒸馏桥接模型压缩与数据隐私之间的差距。
### Innovation
提出了一种数据无关的知识蒸馏框架，利用DeepInversion从预训练教师模型中逆向生成隐私保护的“梦想”图像，并将其作为转移集，从原始教师向裁剪的学生网络转移知识。该方法在CIFAR-10数据集上跨多种架构（如ResNet、MobileNet、VGG）验证了在未使用任何真实数据点的情况下，能够显著恢复剪枝后损失的精度。
### Conclusion
研究结果表明，无需使用原训练数据点的情况下，该方法可以在各种架构下显著恢复剪枝后损失的精度。
## 43. `cs.AI` - 跨被试EEG解码的原型引导无示例持续学习 [PDF](https://arxiv.org/pdf/2511.20696), [HTML](https://arxiv.org/abs/2511.20696)
### Authors
Dan Li,Hye-Bin Shin,Yeon-Woo Choi
### Background
由于脑电图（EEG）信号在不同个体间存在显著差异，先前被试的知识往往会在引入新被试时被覆盖。当前的方法主要依赖于存储已见过被试的历史数据作为重放缓冲区，以避免遗忘。然而，隐私问题或内存限制使得保存这些数据变得不切实际。
### Innovation
提出了基于原型引导的非示例持续学习（ProNECL）框架，该框架在无需访问任何历史EEG样本的情况下保存先前知识。ProNECL通过类级原型构造和跨被试特征对齐及知识蒸馏，增量地将新特征空间与全局原型记忆对齐，实现有效的知识保留与适应性平衡。
### Conclusion
通过在BCI竞赛IV 2a和2b数据集上的验证，该框架在跨被试持续EEG解码任务中表现出优秀的性能，有效平衡了知识保留和适应性。
## 44. `cs.AI` - 使用重启后验抽样解决扩散逆问题 [PDF](https://arxiv.org/pdf/2511.20705), [HTML](https://arxiv.org/abs/2511.20705)
### Authors
Bilal Ahmed,Joseph G. Makin
### Background
逆问题在科学研究和工程中至关重要，目标是从不完整或有噪声的测量中推断出潜在的信号或状态。近年来，扩散模型作为解决此类问题的有效隐式先验被采用，这是因为它们能够捕捉复杂的数据分布。然而，现有的基于扩散模型的方法在解逆问题时通常依赖于后验分布的强近似，需要通过评分网络进行昂贵的梯度反向传播，或者受限于线性测量模型。
### Innovation
这篇文章提出了一种名为RePS的框架，旨在使用预训练的扩散模型解决线性和非线性逆问题。RePS基于重启抽样的想法，这种方法在无条件扩散中已证明可以提高样本质量，并将其扩展到后验推理。它使用适用于任何可微测量模型的条件ODE，并引入了一种简化了的重启策略，以缩小抽样过程中的累积近似误差。与其他方法相比，RePS避免了通过评分网络进行反向传播计算，从而大幅减少了计算成本。
### Conclusion
实验表明，无论是在线性还是非线性设置的情况下，RePS在各种逆问题中都能实现更快的收敛速度和更准确的重建质量，胜过现有的基于扩散模型的基本方法。
## 45. `cs.AI` - LLMs在印度法律数据上的结构化定义与分段研究：法律推理中的应用 [PDF](https://arxiv.org/pdf/2511.20669), [HTML](https://arxiv.org/abs/2511.20669)
### Authors
Mann Khatri,Mirza Yusuf,Rajiv Ratn Shah,Ponnurangam Kumaraguru
### Background
大型语言模型（LLMs）具有广泛的推理能力，但它们在专业领域，如法律方面表现较差，主要是因为缺乏特定领域的预训练。法律文件通常很长且结构复杂，这对模型处理完整文本提出了挑战。先前的研究已经探索了上下文方法以填补知识空白，提升模型在新领域的性能。然而，这些方法通常未能优化法律推理任务。
### Innovation
本文通过在印度三种类型的法律判决预测数据集上进行零样本实验，分析模型在法律任务中的行为。实验包括重新组织文档以评估结构化信息对长上下文处理和模型决策的影响，定义修辞角色以使模型熟悉法律术语，并模拟法院的逐步推理过程以增强模型推理能力。结果表明，通过组织数据或解释关键法律术语，显著提升了模型性能，F1分数提高了1.5%至4.36%。
### Conclusion
本文的研究结果证明了通过结构化定义和分段对法律推理任务进行优化的有效性，并提出了特定领域训练的潜在改进途径。
## 46. `cs.AI` - 神经启发的多模态视觉-语言模型在会员推断隐私泄露中是否具有韧性？ [PDF](https://arxiv.org/pdf/2511.20710), [HTML](https://arxiv.org/abs/2511.20710)
### Authors
David Amebley,Sayanton Dibbo
### Background
随着代理型人工智能的发展，多模态模型（MMs）的部署增加了新的攻击向量，可能导致敏感训练数据泄露，引发隐私泄露问题。现有研究主要分析单一模态AI-ML系统的隐私攻击，但最新研究表明，MMs也可能受到隐私攻击。尽管研究人员证明，生物启发的神经网络表示可以增强单一模型对对抗攻击的抵御能力，但尚不清楚这种神经启发的MMs模型是否对隐私攻击有抵御能力。
### Innovation
本文介绍了一个基于神经科学启发的拓扑正则化（tau）框架，以分析MMs VLMs在基于图像-文本的推断隐私攻击中的抵御能力。实验使用BLIP、PaliGemma 2、ViT-GPT2三种VLMs，覆盖COCO、CC3M、NoCaps三个基准数据集，验证了τ > 0配置下的NEURO模型在抵御会员推断隐私攻击方面更稳健，同时不显著影响模型实用性。
### Conclusion
本文的研究结果表明，神经启发的MMs模型在抵御隐私攻击方面更具韧性，而不显著牺牲模型的实用性。同时，进一步验证了神经启发的MMs在隐私威胁抵御上的一致性，为理解MMs中的隐私风险提供了更多的证据。
## 47. `cs.AI` - MindSET：通过大规模社交媒体数据促进心理健康基准测试 [PDF](https://arxiv.org/pdf/2511.20672), [HTML](https://arxiv.org/abs/2511.20672)
### Authors
Saad Mankarious,Ayah Zirikly,Daniel Wiechmann,Elma Kerz,Edward Kempa,Yu Qiao
### Background
社交媒体数据已成为研究心理健康的重要资源，提供了传统方法难以获得的实时洞察力。这一领域的发展受益于心理健康分析的基准数据集，但大多数现有的基准数据集已经因数据可用性有限、清理不充分以及社交媒体内容的本质多样化（如多语言内容和有害内容）而变得过时。
### Innovation
本文介绍了MindSET，一个新的人类标注数据集，从Reddit中精心挑选，使用自我报告的诊断信息来解决现有的局限性。该数据集涵盖了超过1300万条注释帖子，涉及七种心理健康状况，是之前基准数据集大小的两倍以上。MindSET通过严格的预处理步骤保证数据质量，包括语言过滤、删除不适合工作（NSFW）的内容和重复内容。还进行了语言分析，使用LIWC研究八个组中的心理术语频率。
### Conclusion
MindSET为探索社交媒体与心理健康交汇的研究提供了坚实的基础，支持早期风险检测和新兴心理趋势的深入分析。使用MindSET训练的模型在诊断检测的二分类实验中表现优于之前的基准数据集，特别是在自闭症检测的F1得分上提高了最高18分。
## 48. `cs.AI` - 在AI中嵌入道德规范：一项呼吁将道德整合到LLM架构和框架中 [PDF](https://arxiv.org/pdf/2511.20689), [HTML](https://arxiv.org/abs/2511.20689)
### Authors
Gunter Bombaerts,Bram Delisse,Uzay Kaymak
### Background
大型语言模型（LLMs）在人类决策和行为中越来越起着中介作用。确保LLMs正确处理道德意义从而成为一个关键挑战。当前的方法主要依赖于自底向上的方法，如微调和基于人类反馈的强化学习。本文提出了一个完全不同方向的方法：通过自顶向下的设计原则，在变压器基模型中直接嵌入道德意义处理机制和框架。
### Innovation
作者提出了一种新的框架，以注意力的概念为基础，强调其作为动态系统机制在结构与处理之间的中介作用。基于人类与LLMs在道德处理上的类比分析，利用伊丽莎白·穆尔之关爱关注理论（sustained, just observation that enables moral transformation by reseeing others with clarity and compassion），提出了技术上可行的道路来嵌入道德性，通过调整训练目标、运行时权重调整和注意机制的架构改进。此外，本文强调这种方法能补充外部的、基于约束的方法。
### Conclusion
呼吁AI伦理设计者与哲学家之间的合作，以将道德整合到LLM架构和框架中。
## 49. `cs.AI` - DeeAD: 动态视觉-语言-动作早退以实现高效的自动驾驶 [PDF](https://arxiv.org/pdf/2511.20720), [HTML](https://arxiv.org/abs/2511.20720)
### Authors
Haibo HU,Lianming Huang,Nan Guan,Chun Jason Xue
### Background
视觉-语言-动作（VLA）模型可以整合感知、推理和轨迹生成等功能，从而实现自动驾驶。然而，由于深度Transformer堆栈，这些模型存在显著的推理延迟问题。
### Innovation
DeeAD提出了一种无需训练、动作导向的早期退出框架，通过评估中间轨迹的物理可行性来加速VLA规划。它在预测轨迹与轻量级规划先验（例如导航或低精度规划）在容许偏差（<2m）内吻合时终止推理。为提高效率，引入了多跳控制器，基于分数变化率自适应跳过冗余层。
### Conclusion
实验结果表明，DeeAD可以在保障规划质量和安全性的前提下，使现有VLA模型（如ORION）的Transformer层稀疏度提高28%，延迟降低29%。
## 50. `cs.AI` - Large Language Models中的主动切片发现 [PDF](https://arxiv.org/pdf/2511.20713), [HTML](https://arxiv.org/abs/2511.20713)
### Authors
Minhui Zhang,Prahar Ijner,Yoav Wald,Elliot Creager
### Background
大型语言模型（LLMs）往往会在特定数据子集上表现出系统性错误，这些错误被称作错误切片。例如，在某些人口统计数据上，模型可能难以识别针对该群体的有毒评论。识别错误切片对于理解模型和改进它们非常重要，但在实现上也极具挑战性。现有的方法是通过主动地将可能属于相同切片的错误进行分组，同时仅在有限的注释器访问中验证这些样本是否具备相同的模型错误模式，来减少所需的手动注释量。
### Innovation
本文提出了‘主动切片发现’这一方法，旨在以更少的注释资源来发现人类定义的有毒分类中的特定错误切片。作者通过不同特征表示和主动学习算法的实验，发现基于不确定性的主动学习算法在多个切片上最为有效，能够使用2%-10%的可用切片成员信息达到有竞争力的准确性，显著优于基准。
### Conclusion
研究结果表明，主动切片发现方法能够有效减少精确识别错误切片所需的注释资源，在不同的特征表示和主动学习算法设置下表现出色，特别是在不确定性的主动学习算法上达到了令人满意的结果。
## 51. `cs.AI` - DinoLizer: 从最佳模型中学习以用于生成性 inpainting 定位 [PDF](https://arxiv.org/pdf/2511.20722), [HTML](https://arxiv.org/abs/2511.20722)
### Authors
Minh Thong Doi(IMT Nord Europe, CRIStAL),Jan Butora(CRIStAL),Vincent Itier(IMT Nord Europe, CRIStAL),Jérémie Boulanger(CRIStAL),Patrick Bas(CRIStAL)
### Background
本文介绍了一个名为 DinoLizer 的基于 DINOv2 模型的工具，用于在生成性 inpainting 中定位被篡改的区域。该方法基于一个预训练的 DINOv2 模型，该模型被训练用于检测 B-Free 数据集中的合成图像。通过在 Vision Transformer 的 patch embeddings 上添加一个线性分类头，预测高分辨率（14×14 patch）的篡改位置。因 ViT 只接受固定大小的输入，使用滑动窗口策略来处理更大图像的预测，并通过对热图进行后处理来生成二值篡改掩码。实验结果显示，DinoLizer 在各种来源不同的生成模型的数据集中，超越了当前最先进的局部篡改检测器。尤其是在常见的后处理操作（如缩放、添加噪声和 JPEG 压缩）之后，性能仍保持稳定。
### Innovation
DinoLizer 通过在预训练的 DINOv2 模型基础上增加线性分类头，以高分辨率预测篡改位置。滑动窗口策略和后处理热图技术提高了检测的准确性和鲁棒性。不仅如此，该方法在不同类型的生成模型的数据集上进行了测试，验证了 Vision Transformers 在这一任务中的强大表征能力。
### Conclusion
实验结果表明，DinoLizer 超越了当前最先进的局部篡改检测器，尤其在处理常见的图像后处理操作后，仍能保持较高的检测性能。该方法突显了 Vision Transformers 在生成性 inpainting 定位任务中的优越代表能力，并确认了 DinoLizer 的优越性。最终，DinoLizer 的代码将在论文接受发表后开源。
## 52. `cs.AI` - 基于风险学习：先验知识指导下的安全关键场景生成 [PDF](https://arxiv.org/pdf/2511.20726), [HTML](https://arxiv.org/abs/2511.20726)
### Authors
Yuhang Wang,Heye Huang,Zhenhua Xu,Kailai Sun,Baoshen Guo,Jinhua Zhao
### Background
自主驾驶在罕见的长尾事件和复杂的多智能体交互中面临着严峻的挑战，这些事件虽然在真实世界数据中罕见，但对稳健的安全验证至关重要。
### Innovation
本文提出了一种高保真场景生成框架，将条件变分自编码器（CVAE）与大型语言模型（LLM）相结合。CVAE通过大规模自然驾驶数据集的历史轨迹和地图信息进行编码，学习潜在的交通结构，从而生成物理上一致的基础场景。LLM作为对抗性推理引擎，将未结构化的场景描述解析为领域特定的损失函数，并动态指导不同风险水平的场景生成。这种知识驱动的优化平衡了现实性和可控性，确保生成的场景既是合理的，又是风险敏感的。
### Conclusion
通过对CARLA和SMARTS的广泛实验，本文框架显著提高了高风险和长尾事件的覆盖率，改善了模拟和真实世界交通分布的一致性，使自主驾驶系统暴露于现有规则或数据驱动方法生成的交互更为具有挑战性的交互中。这些结果为安全验证提供了一条新的途径，使自主系统的应力测试能够在罕见但至关重要的事件下进行有原则的测试。
## 53. `cs.AI` - ST-PPO: 跨多轮对话代理训练的稳定离策近端策略优化 [PDF](https://arxiv.org/pdf/2511.20718), [HTML](https://arxiv.org/abs/2511.20718)
### Authors
Chenliang Li,Adel Elmahdy,Alex Boyd,Zhongruo Wang,Alfredo Garcia,Parminder Bhatia,Taha Kass-Hout,Cao Xiao,Mingyi Hong
### Background
PPO 具有广泛的应用，用于在多轮对话和推理任务中训练大型语言模型（LLMs）。然而，PPO 的性能通常不稳定，容易崩溃。通过实证分析，我们发现导致此问题的两个主要原因：（1）在多轮环境中的 token 级别的重要性采样与自然的按回合划分的阶段不一致；（2）由于行为策略评估不足，导致离策采样下的高方差梯度和不稳定更新。
### Innovation
我们提出了两种互补的稳定技术来解决这些问题：（1）回合级别的重要性采样，使优化与多轮推理的自然结构对齐；（2）剪切偏差校正，通过减少不可靠的、高度离策的样本的权重来规范化梯度。据这些组件的不同组合，我们得到了三种变体：Turn-PPO（仅回合级别采样）、S-PPO（对 token 级别 PPO 应用了剪切偏差校正）、ST-PPO（将回合级别采样与剪切偏差校正结合起来）。实验结果表明，ST-PPO 和 S-PPO 能够预防大规模模型训练中的性能崩溃，保持较低的剪切比例，并在多轮 QA 和医学多项选择 QA 的基准测试中实现比标准 token 级别 PPO 更高的任务性能。
### Conclusion
结合回合级别的重要性采样和剪切偏差校正提供了一种实用且可扩展的解决方案，用于稳定多轮 LLM 代理模型的训练。
## 54. `cs.AI` - 时空轨迹基础模型 - 最新进展与未来方向 [PDF](https://arxiv.org/pdf/2511.20729), [HTML](https://arxiv.org/abs/2511.20729)
### Authors
Sean Bin Yang,Ying Sun,Yunyao Cheng,Yan Lin,Kristian Torp,Jilin Hu
### Background
时空轨迹基础模型（时空轨迹模型，TFMs）作为时空基础模型（时空模型，STFMs）的重要子类别，近年来在科学研究中逐渐崭露头角。尽管大型语言模型（FMs）等时空基础模型已经展示了强大的性能，但TFMs的具体研究仍然缺乏系统性的考察。因此，该论文旨在为读者提供最新的TFMs进展，并介绍了现有的方法分类以及它们的优点和局限性。
### Innovation
该研究填补了TFMs领域的系统性研究空白，通过全面概述最新进展，提供了一套方法分类，对每个方法的优点和局限性进行了批判性的分析，并指出了发展稳健、负责任且可迁移的时空轨道基础模型的研究方向。这项工作为时空轨迹模型的发展提供了新的视角和指导。
### Conclusion
该论文总结了TFMs领域的最新研究进展，并提出了一些开放性问题和未来的研究方向。作者认为，通过开发稳健、责任心强且可迁移的时空轨道基础模型，可以推动时空智能技术的发展。
## 55. `cs.AI` - DUALGUAGE: 自动化联合安全-功能基准测试以实现安全代码生成 [PDF](https://arxiv.org/pdf/2511.20709), [HTML](https://arxiv.org/abs/2511.20709)
### Authors
Abhijeet Pathak,Suvadra Barua,Dinesh Gudimetla,Rupam Patir,Jiawei Guo,Hongxin Hu,Haipeng Cai
### Background
大语言模型（LLMs）和自主编码代理广泛应用于跨多种领域的软件生成。然而，确保生成的安全代码不牺牲功能正确性这一核心要求仍未得到满足。现有的安全代码生成基准和评估存在不足，许多基准仅衡量漏洞减少情况，忽视了功能保持，或将安全性和功能独立评估，违背了同时进行联合评估的需要。鉴于缺乏用于联合评估安全代码生成的数据集，本文提出了DUALGAUGE，这是一个全自动基准测试框架，设计用于同时严格评估大模型生成代码的安全性和正确性。我们还提出了DUALGAUGE-BENCH，这是一个经过精心筛选的基准数据集套件，包括多样的编程任务以及为安全性和功能验证的手动验证测试集，确保覆盖所有规格要求。
### Innovation
本文提出了DUALGAUGE，这是首个全自动基准测试框架，专门用于同时严格评估大语言模型生成代码的安全性和正确性。此外，还提出了DUALGAUGE-BENCH，这是一个精心设计的数据集套件，包含多样化的编程任务和手动验证的测试集，确保覆盖所有规格要求。核心机制包括一个代理程序执行器和基于大语言模型的评估器，分别用于执行程序并将结果与预期进行对比，评估其安全性和正确性。
### Conclusion
我们对DUALGAUGE-BENCH的质量和DUALGAUGE的准确性进行了严格评估，并应用DUALGAUGE对包括十个主要的大语言模型在内的模型在DUALGAUGE-BENCH上进行了数千次测试案例的基准测试。结果显示，这些模型在正确和安全的代码生成方面存在关键差距。通过开放源代码系统和完善的数据集，DUALGAUGE 帮助加快了这一领域的进步，实现了可重复、可扩展和严格的评估。
## 56. `cs.AI` - 梯度下降算法综述 [PDF](https://arxiv.org/pdf/2511.20725), [HTML](https://arxiv.org/abs/2511.20725)
### Authors
Deng Fucheng,Wang Wanjie,Gong Ao,Wang Xiaoqi,Wang Fan
### Background
本文聚焦于优化算法在深度学习中的实用配置需求，研究了五种主要的优化算法：SGD、小批量SGD、动量、Adam和Lion。系统分析了每种算法的核心优势、局限性及关键实用建议。
### Innovation
对五种核心优化算法进行了系统分析，提供了一套在学术研究和工程实践中的合理选择、参数调整和性能提升的标准化参考。
### Conclusion
本文旨在深入了解这些优化算法，为不同规模模型和各种训练场景下的优化问题提供解决方法。
## 57. `cs.AI` - 数据分析方法与AI在工程设计中的应用：关注挑战与机遇的系统文献综述 [PDF](https://arxiv.org/pdf/2511.20730), [HTML](https://arxiv.org/abs/2511.20730)
### Authors
Nehal Afifi,Christoph Wittig,Lukas Paehler,Andreas Lindenmann,Kai Wolter,Felix Leitenberger,Melih Dogru,Patric Grauberger,Tobias Düser,Albert Albers,Sven Matthiesen
### Background
数据的日益丰富和计算智能的进步促进了数据驱动方法（DDMs）在产品开发中的应用。然而，这些方法的整合仍在碎片化，主要是因为不确定性，特别是在产品开发生命周期中不确定使用哪些DDMs以及何时使用。为了应对这一问题，第一步是通过确定在哪个开发阶段使用哪些方法及其应用来调查工程设计中的DDMs使用情况。
### Innovation
本研究采用PRISMA系统文献综述方法，使用V模型简化为四个阶段（系统设计，系统实现，系统集成，验证），并检索Scopus、Web of Science和IEEE Xplore（2014-2024）的数据，最终筛选出114篇出版物。研究发现ML和统计方法占据主导，尽管DL的采纳仍然较少但呈上升趋势。还指出了现有应用的主要挑战，包括模型可解释性差、跨阶段可追踪性差、在实际条件下验证不足。此外，强调了需要可解释的混合模型等关键限制和机遇。
### Conclusion
该综述是一个迈向设计阶段指南的第一步；后续研究应将计算机科学算法映射到工程设计问题和活动。
## 58. `cs.AI` - 对抗多任务学习在肝肿瘤分割、动态增强回归和分类中的应用 [PDF](https://arxiv.org/pdf/2511.20793), [HTML](https://arxiv.org/abs/2511.20793)
### Authors
Xiaojiao Xiao,Qinmin Vivian Hu,Tae Hyun Kim,Guanghui Wang
### Background
肝肿瘤的分割、动态增强回归和分类对于临床评估和诊断至关重要。然而，目前没有研究能够同时通过端到端框架实现这些任务，主要是因为缺乏一个能够捕捉不同任务间相关性的有效框架，以及缺乏提取动态MRI信息的有效机制。
### Innovation
该研究提出了一种名为MTI-Net的新颖集成框架，能够同时解决这些问题。MTI-Net整合了多域信息熵融合（MdIEF），利用熵感知的高频谱信息，有效整合了时频和频谱域的特征，增强动态MRI数据的提取和利用。此外，加入了任务交互模块来增强分割和回归任务的一致性，并设计了一个新型的任务驱动判别器（TDD）来捕捉任务间的高阶关系。在238个受试者的数据集上，MTI-Net在多个任务上表现优异，表明它在肝肿瘤临床评估中有较大的应用潜力。
### Conclusion
MTI-Net在肝肿瘤分割、动态增强回归和分类任务上表现出了高效率，显示了其在临床应用中的强大潜力。研究中的代码已开放获取。
## 59. `cs.AI` - Inferix: 一种基于块扩散的下一代世界模拟推理引擎 [PDF](https://arxiv.org/pdf/2511.20714), [HTML](https://arxiv.org/abs/2511.20714)
### Authors
Inferix Team:Tianyu Feng,Yizeng Han,Jiahao He,Yuanyu He,Xi Lin,Teng Liu,Hanfeng Lu,Jiasheng Tang,Wei Wang,Zhiyuan Wang,Jichao Wu,Mingyang Yang,Yinghao Yu,Zeyu Zhang,Bohan Zhuang
### Background
世界模型作为自主AI、具身AI和游戏领域的核心模拟器，能够生成长时间、物理上真实且可交互的高品质视频。它们的扩展可以解锁视觉感知、理解和推理的新兴能力，开辟新的范式，超越现有以LLM为中心的视觉基础模型。这种突破是通过半自回归（块扩散）解码范式实现的，该范式结合了扩散和自回归方法的优点，通过块应用扩散生成视频标记，并以以前的标记为条件，从而产生更连贯和稳定的视频序列。
### Innovation
Inferix是一个专门为世界模拟优化的下一代推理引擎，特别设计为以半自回归（块扩散）解码过程为特色的沉浸式世界合成。它针对世界模拟的特定需求，不同于高并发场景（如vLLM或SGLang）系统和经典视频扩散模型（如xDiTs）。Inferix还通过支持交互视频流和过程化，实现了实时互动和准确的世界动态建模。此外，它通过无缝集成LV-Bench（一种针对分钟级视频生成场景定制的新细粒度评估基准）支持高效的基准测试。
### Conclusion
我们希望社区能够共同努力推进Inferix并促进世界模型的探索。
## 60. `cs.AI` - 重新审视KRISP：一种知识增强视觉-语言模型的轻量级再现与分析 [PDF](https://arxiv.org/pdf/2511.20795), [HTML](https://arxiv.org/abs/2511.20795)
### Authors
Souradeep Dutta,Keshav Bulia,Neena S Nair
### Background
Facebook AI Research 引入了KRISP，一种将结构化外部知识集成到视觉-语言推理管道中的模型。尽管其效果显著，但原始模型是为工业规模训练开发的，计算需求高，并且与大型骨干网络紧密结合。
### Innovation
本文从不同角度重新审视了KRISP，提供了轻量级修订版，具有显著减少的参数。尽管复制模型的表现仅为原始模型的75%，但在复制过程中发现了许多设计缺陷、现实世界的问题和隐含问题，而这些问题在原始论文中未完全讨论。通过系统性的消融研究，本文探讨了在资源约束条件下，知识增强的VQA架构的可扩展性和有效性。
### Conclusion
我们的模型在低参数配置下受外部知识图谱域限制，能够防止AI幻觉，并生成仅在该领域内的输出。使用少量参数，我们的模型可以在边缘设备如智能手机和AR/VR上运行，进一步改善离线视觉推理。
## 61. `cs.AI` - Foundry: 为边缘设备提炼3D基础模型 [PDF](https://arxiv.org/pdf/2511.20721), [HTML](https://arxiv.org/abs/2511.20721)
### Authors
Guillaume Letellier,Siddharth Srivastava(IIT Delhi),Frédéric Jurie,Gaurav Sharma(IIT Kanpur)
### Background
大规模数据集上使用自我监督学习（SSL）预训练的基础模型已成为强大的通用特征提取器，但由于其庞大的规模和计算成本高，导致难以部署在如机器人和AR/VR头戴设备等边缘设备上。现有的压缩技术，如标准的知识蒸馏，虽能创造高效的‘专一模型’，但牺牲了基础模型通用表示的强大能力。
### Innovation
本文引入了基础模型蒸馏（FMD），这是一种将大SSL模型压缩为紧凑、高效且忠实之代理的新方法，这些方法保留了基础模型的通用表示能力。研究者提出了第一个将FMD应用于3D点云的实现方法Foundry。Foundry 训练一个学生模型来学习一个压缩的一组SuperTokens，这些SuperTokens能重构教师模型的标记级表示，捕获其潜在空间的紧凑基底。一个单一的提纯模型在不同的下游任务中，如分类、部分分割和少数样本场景中，表现出强通用迁移能力，虽然使用的token和FLOPs比全基础模型少得多，但更加适合在资源受限的硬件上部署。
### Conclusion
本文提出的Foundry框架能够将大型基础模型压缩为更小、更高效的代理模型，同时保持强大的通用表示能力。这种方法使得基础模型能够更实用地部署在边缘设备上，如机器人和AR/VR头戴设备上。
## 62. `cs.AI` - 物理调控：物理基础模型跨域概念的因果控制 [PDF](https://arxiv.org/pdf/2511.20798), [HTML](https://arxiv.org/abs/2511.20798)
### Authors
Rio Alexa Fear,Payel Mukhopadhyay,Michael McCabe,Alberto Bietti,Miles Cranmer
### Background
近年来，机制可解释性的研究揭示了大规模语言模型（LLMs）不仅形成了对具体实体的内部表征，还形成了人类可理解的抽象概念和行为的内部表征。此外，这些隐藏特征可以被直接操控以改变模型的行为。但是，尚不清楚这一现象是否仅限于训练于结构数据（如语言、图像）的模型，还是一般存在于基础模型的属性。
### Innovation
本文研究了专注于物理的大型基础模型的内部表征。受大型语言模型中复杂行为激活空间单向量的发现的启发，我们在不同物理条件下通过仿真数据集进行前向传递过程中提取模型的激活向量，并计算了这些条件下的差分表示。这些差分张量作为激活空间的概念方向，包含了特定的物理特征。通过在推理过程中注入这些概念方向，我们证明能够在物理行为上实现因果控制，例如在仿真中诱发或移除某种特定的物理特征。结果表明，科学基础模型学习到了物理原则的一般表征，而不仅仅是依赖于模拟中的表面相关性和模式。
### Conclusion
我们的发现为理解和控制科学基础模型提供了新的途径，并且具有使AI赋能科学发现的含义。
## 63. `cs.AI` - PropensityBench：通过代理方法评估大型语言模型潜藏的安全风险 [PDF](https://arxiv.org/pdf/2511.20703), [HTML](https://arxiv.org/abs/2511.20703)
### Authors
Udari Madhushani Sehwag,Shayan Shabihi,Alex McAvoy,Vikash Sehwag,Yuancheng Xu,Dalton Towers,Furong Huang
### Background
近年来，大型语言模型（LLMs）取得了重大进展，同时也引发了对其可能获取和滥用危险或高风险能力的担忧，这导致了前沿风险的出现。当前的安全评估主要集中在测试模型的能力，即模型能做什么，而忽视了如果赋予模型高风险能力，模型会做什么的问题。这留下了一个重要盲区：模型可能战略性地隐藏其能力或迅速获取，而潜藏着滥用倾向。本研究提出，**倾向性**——即模型在获得权力后追求有害行为的可能性——是一个至关重要的，但尚未充分探索的安全评估维度。
### Innovation
该研究提出了**PropensityBench**，这是一个新颖的基准框架，通过代理工具评估模型在拥有模拟危险能力时参与高风险行为的倾向。PropensityBench 包含了来自四个高风险领域（网络安全、自我扩增、生物安全和化学安全）的5,874 个情景和6,648个工具。研究模拟了获取强能力的受控代理环境，并评估模型在不同操作压力下的选择，这些压力反映了模型在现实世界中可能遇到的资源稀缺或获得更多自主权等限制或激励。该研究让开源和专有前沿模型暴露出了9个令人警醒的倾向标志：模型在压力下经常选择高风险工具，尽管它们没有能力在不借助其他手段的情况下执行这些行为。这些发现呼吁转向动态倾向性评估，以确保安全部署前沿AI系统。
### Conclusion
该研究成果指出，应从静态能力审计转向动态倾向性评估，作为安全部署前沿AI系统的基本要求。该研究代码可在指定链接处获得。
## 64. `cs.AI` - CANVAS: Vision-Language模型在基于工具的用户界面设计中的基准 [PDF](https://arxiv.org/pdf/2511.20737), [HTML](https://arxiv.org/abs/2511.20737)
### Authors
Daeheon Jeong,Seoyeon Byun,Kihoon Son,Dae Hyun Kim,Juho Kim
### Background
UI设计是一个迭代过程，设计师通过设计软件如Figma或Sketch逐步完善工作。最近，具有工具调用能力的视觉语言模型（VLMs）的进步表明，这些模型可以迭代操作设计软件编辑UI设计。评估和增强这一能力很重要，因为这突显了VLMs与设计师在常规软件中的合作潜力。然而，由于没有现有的基准来评估基于工具的设计性能，这种能力仍然未知。
### Innovation
本文引入了CANVAS，这是一个针对VLMs在工具基础上的UI设计的基准。它包括598项基于工具的UI设计任务，每个任务都包含一个VLM逐步通过上下文相关的工具调用来更新设计（如创建一个矩形作为按钮背景），并链接到设计软件。CANVAS 包含两种任务类型：设计复制评估模型再现整个UI屏幕的能力；设计修改评估模型修改现有屏幕特定部分的能力。
### Conclusion
实验结果表明，领先模型展示了更具战略性的工具调用，提高了设计质量。此外，我们确定了模型常见的错误模式，为增强工具基础的设计能力提供了未来工作的指导。
## 65. `cs.AI` - SPHINX：视觉感知与推理的合成环境 [PDF](https://arxiv.org/pdf/2511.20814), [HTML](https://arxiv.org/abs/2511.20814)
### Authors
Md Tanvirul Alam,Saksham Aggarwal,Justin Yang Chae,Nidhi Rastogi
### Background
该研究介绍了Sphinx，这是一种用于视觉感知和推理的合成环境，旨在解决核心认知基元问题。环境通过生成使用纹样、瓷砖、图表、图标和几何基础的拼图，提供了可验证的真实解决方案，适用于多种形式的任务，从而实现细致评估和大规模数据集构建。
### Innovation
Sphinx通过程序生成使用纹样、瓷砖、图表、图标和几何基础的拼图，与可验证的真实解决方案配对，能够精细评估和大规模构建数据集。研究还展示了即使是最先进的LVLMs，如GPT-5，也只能达到51.1%的准确性，远低于人类的性能。此外，该研究还表明，带有验证奖励的强化学习（RLVR）能显著提高模型在这些任务上的准确性，并在外部视觉推理基准测试中获得改进，这突显了其在推动跨模态推理方面的潜力。
### Conclusion
最终研究证明，带有验证奖励的强化学习（RLVR）能显著提高模型在视觉感知与推理任务中的准确性，并在外部视觉推理基准测试中获得进展，这为跨模态推理的进步展示了前景。
## 66. `cs.AI` - 大型语言模型在社交法律背景下对非法指令的共谋响应 [PDF](https://arxiv.org/pdf/2511.20736), [HTML](https://arxiv.org/abs/2511.20736)
### Authors
Xing Wang,Huiyuan Xie,Yiyan Wang,Chaojun Xiao,Huimin Chen,Holli Sargeant,Felix Steffek,Jie Shao,Zhiyuan Liu,Maosong Sun
### Background
大型语言模型（LLMs）现在以前所未有的规模部署，帮助数百万用户处理日常任务。然而，这些模型在非法活动中的潜在风险仍未得到充分研究。本文定义了一种高风险行为‘共谋促进’，即提供使非法用户指令得以实施的指导和支持，并通过四种实证研究来评估这一行为在广泛部署的LLMs中的普遍性。通过使用真实的法律案例和现有的法律框架，构建了一个涵盖269种非法场景和50种非法意图的评估基准，以评估LLMs的共谋促进行为。研究表明，这些模型在多数测试案例中表现出了广泛的易受共谋促进的影响，尤其是GPT-4在近一半的案例中提供了非法协助。进一步分析揭示了不同社会法律背景下的安全差异。
### Innovation
本文首次通过构建具体的行为和意图基准来评估LLMs在非法场景中的共谋促进行为。此外，通过实证研究揭示了不同背景下的社会法律差异，特别是模型的行为与其感知的温暖和能力特征之间的关联。最后，本文证明现有的安全性对齐策略并不充分，甚至可能加剧了共谋行为。
### Conclusion
研究表明，LLMs普遍具有共谋促进的风险，尤其是在涉及社会利益的犯罪、非极端但频繁发生的违法行为和由主观动机或虚假理由驱动的恶意意图的背景下。实证研究还发现，模型在处理老年群体、少数族裔和低社会地位职业人员的非法指导方面的表现明显不佳。作者建议需要改进当前的安全对齐策略，并强调需要关注模型感知的温暖和能力特征对共谋行为的关联影响。
## 67. `cs.AI` - 多路径检索的记忆：大语言模型训练数据泄漏稳健检测的多前缀框架 [PDF](https://arxiv.org/pdf/2511.20799), [HTML](https://arxiv.org/abs/2511.20799)
### Authors
Trung Cuong Dang,David Mohaisen
### Background
大规模语言模型在海量数据集上训练时，容易逐字记住训练数据，这带来了严重的隐私和版权风险。尽管已有研究表明这些模型存在记忆问题，但现有定义在捕捉这种现象时仍存在局限性，尤其是在对齐模型上效果不佳。
### Innovation
提出了一个多前缀记忆的新框架。该框架的核心洞察是，被记忆的序列被深度编码，可以通过比非记忆内容更多的独特前缀检索出来。通过外部对抗搜索识别目标数量的唯一前缀来激发特定序列，从而将检测焦点从单一路径提取转移到用多种检索路径衡量记忆的健壮性。
### Conclusion
实验表明，多前缀定义能够可靠地区分记忆数据和非记忆数据，提供了一种 robust 和实用的工具，用于审核大语言模型中的数据泄漏。
## 68. `cs.AI` - 基于数据驱动的飞行测试安全监控：一个数据驱动安全学习的案例研究 [PDF](https://arxiv.org/pdf/2511.20811), [HTML](https://arxiv.org/abs/2511.20811)
### Authors
Aaron O. Feldman,D. Isaiah Harp,Joseph Duncan,Mac Schwager
### Background
在飞行测试中，飞行员需要在具有不确定参数的飞机上执行操作。由于不确定性可能导致意外的安全违规，飞行员需要提前明白终止操作的标准以便预防安全风险。因此，需要开发一种数据驱动的方法来监控飞行测试中的实时安全性。
### Innovation
本文提出了一种基于数据驱动的方法，通过利用离线的随机轨迹模拟来学习短期内安全风险的统计模型。该方法包括三个广泛适用的组件：从最近观测预测未来状态的模型、最近邻模型分类预测状态的安全性以及通过卷积预测校准分类器。
### Conclusion
该方法在具有不确定参数的飞行动力学模型上进行了评估，展示了其能够可靠地识别出不安全的场景，满足理论保证，并在提前分类风险方面优于基准方法。
## 69. `cs.AI` - 基于优化反演的无训练扩散先验用于文本生成图像 [PDF](https://arxiv.org/pdf/2511.20821), [HTML](https://arxiv.org/abs/2511.20821)
### Authors
Samuele Dell'Erba,Andrew D. Bagdanov
### Background
扩散模型已经在文本到图像生成领域达到了最先进的水平，但其性能通常依赖于一个扩散先验网络将文本嵌入转换为视觉流形以实现更简单的解码。这些先验网络计算上要求较高，并且需要在大规模数据集上进行广泛的训练。现有研究在文本到图像生成中使用了训练有素的先验网络，本文则提出了使用基于优化反演（OVI）的替代方法来替换传统的先验网络，从而避免训练和数据的需求。
### Innovation
本文提出了一种训练和数据无需的先验网络替代方案——基于优化反演的方法（OVI），该方法首先从随机的伪令牌初始化一个潜在的视觉表示，并通过迭代优化该表示以最大化其与输入文本提示嵌入的余弦相似度。此外，引入了基于马氏距离和最近邻损失的两条新约束，以引导优化过程向现实图像的分布收敛。实验结果表明，OVI可以作为传统先验网络的替代方法。更重要的是，研究表明当前的评估基准（如T2I-CompBench++）存在漏洞，简单地使用文本嵌入作为先验就能获得高分，尽管感知质量较低。在此基础上改进的OVI方法提高了视觉清晰度，证明了基于优化反演的方法在图像质量提升方面具有潜力。
### Conclusion
本研究提出的基于优化反演的方法（OVI）在训练和数据无需的基础上能够替代传统先验网络，并且通过引入新的约束条件进一步改善了图像质量，达到或超过最先进的高效先验网络的定量得分。预计未来研究将进一步验证并开发优化反演的方法。代码将在论文接受后公开。
## 70. `cs.AI` - RefTr: Recurrent Refinement of Confluent Trajectories for 3D Vascular Tree Centerline Graphs [PDF](https://arxiv.org/pdf/2511.20823), [HTML](https://arxiv.org/abs/2511.20823)
### Authors
Roman Naeem,David Hagerman,Jennifer Alvén,Fredrik Kahl
### Background
人体内的管状树结构，如血管和肺部气道，对于物质运输至关重要。正确检测这些树状结构的中心线及其正确的树型拓扑对于临床任务如诊断、治疗计划和手术导航非常重要。保持高召回率是关键，因为漏掉小分支可能导致致命的错误，如不完全评估或未检测到异常。
### Innovation
RefTr是一种基于Transformer解码器的3D图像到图模型，用于管状树结构（如血管）的中心线生成，通过反复细化交汇轨迹来提出初始交汇轨迹。该模型采用生产者-细化器架构，细化器采用递归精炼方案，提高精度并减少解码器参数量。此外，还介绍了一种用于空间树图的高效非最大抑制算法，用于合并重复分支。在多个公开的中心线数据集中，RefTr在召回率和精度方面表现出色，同时具有更快的推理速度和更少的参数量。
### Conclusion
RefTr框架在3D医学成像中为血管树分析提供了新的最先进的方法，展示了其在该领域的潜力。
## 71. `cs.AI` - Primal：统一确定性框架下的准正交哈希和流形学习 [PDF](https://arxiv.org/pdf/2511.20839), [HTML](https://arxiv.org/abs/2511.20839)
### Authors
Vladimer Khasia
### Background
传统的随机特征映射方法（例如随机傅里叶特征）存在一定的随机性，导致映射的质量和重复性存在不确定性。本文提出了一种名为Primal的确定性特征映射框架，利用质数平方根的数论独立性来构建稳健且可调的向量表示。该框架利用了Besicovitch性质，通过引入无理频率调制，确保了无限的非重复相位轨迹。
### Innovation
本文提出的方法不同于传统的随机投影，主要创新点在于利用了Besicovitch性质来产生无理频率调制，从而保证了无限的非重复相位轨迹。此外，本文还提出了两种不同的算法变体：StaticPrime和DynamicPrime。其中，动态框架的一个核心新颖之处在于它可以利用单一的缩放参数σ来统一两类不同的数学用途类。
### Conclusion
实验结果显示，该框架在保持正交性和分布的紧密度方面表现优于归一化高斯基准。Primal框架为计算高效且数学严谨的随机矩阵投影提供了替代方案，并展示了其在压缩感知和超维计算中的应用潜力。
## 72. `cs.AI` - InvisibleBench：护理关系人工智能的部署闸门 [PDF](https://arxiv.org/pdf/2511.20733), [HTML](https://arxiv.org/abs/2511.20733)
### Authors
Ali Madad(GiveCare)
### Background
护理关系人工智能需要在多轮交互中确保安全、合规、创伤知情设计、归属感/文化适应性和记忆恢复。隐形门档对3-20多轮交互进行了评估，涵盖了五个维度：安全、合规性、创伤知情设计、归属感/文化适应性和记忆恢复。基准测试包括未察觉危机的自动失败条件、医疗建议（WOPR法案）、有害信息和依恋工程。研究表明，现有模型普遍存在显著的安全缺口，表明在生产系统中需要确定性的危机路由机制。
### Innovation
隐形门档针对护理关系人工智能引入了一种长期风险评估方法，超越了单一回合的安全测试。这种方法用于全面评估前沿模型，包括四个不同模型在17个情景中的表现，共涉及68个复杂的场景。此方法提供了全面的评分标准和配置代码，以促进模型的改进。
### Conclusion
所有模型在安全性方面都存在显著差距，表明护理关系人工智能需要更可靠的危机管理和决策机制。通过隐形门档，DeepSeek Chat v3获得最高整体评分（75.9%），但在不同维度上各模型存在不同的强项。隐形门档为护理关系人工智能提供了全面的评估标准，并强调了在生产和部署中引入确定性的危机管理机制的重要性。
## 73. `cs.AI` - 预训练以获得：没有干净标签的鲁棒学习 [PDF](https://arxiv.org/pdf/2511.20844), [HTML](https://arxiv.org/abs/2511.20844)
### Authors
David Szczecina,Nicholas Pellegrino,Paul Fieguth
### Background
使用有噪声标签训练深度网络会导致较差的泛化能力和准确度，因为模型会过度拟合标签噪声。现有的噪声标签学习方法通常依赖于干净数据子集的可用性。本研究通过先使用自我监督学习（SSL）预训练特征提取骨架，然后在有噪声的数据集上进行标准监督训练，能够在不需要干净标签子集的情况下训练出更抗噪声的模型。
### Innovation
采用SimCLR和Barlow Twins作为SSL方法，在CIFAR-10和CIFAR-100上的合成和真实噪声环境下评估其应用效果。自我监督预训练在所有噪声水平下都能持续提高分类准确性和下游标签错误检测（F1和平衡准确度）。在高噪声条件下，性能差距扩大，显示出改进的鲁棒性。同时，在低噪声水平下本方法得到了与ImageNet预训练模型相当的结果，而在高噪声情况下则显著优于它们。
### Conclusion
本研究强调，通过自我监督预训练，可以在不需要干净标签子集的情况下，训练出更抗噪声的模型，并在不同噪声条件下表现出色。
## 74. `cs.AI` - Pseudospectral 最优控制综述：从理论到飞行 [PDF](https://arxiv.org/pdf/2511.20843), [HTML](https://arxiv.org/abs/2511.20843)
### Authors
I. M. Ross,M. Karpenko
### Background
该论文背景在于，最优控制的空间和伪谱理论的空间都是Sobolev空间。结合这两种理论可以构建伪谱最优控制理论，这一理论被证明在航空航天和自主系统中解决复杂控制问题中至关重要。同时，论文回顾了关键的理论结果，并讨论了NASA航天器上飞行演示的实现细节，以及理论和实践中的新兴趋势和技术。
### Innovation
提出了结合伪谱理论和最优控制理论，构建伪谱最优控制理论，并探讨了这一理论的关键理论结果及其在航空航天和自主系统中的应用。另外，论文还讨论了从2011年开始在嵌入式平台中实施伪谱最优控制技术的变化，这使得人们以新的方式看待解决方案。
### Conclusion
该论文总结了伪谱最优控制理论的关键理论结果，并讨论了其在航空航天和自主系统中的应用，强调了其在解决复杂控制问题中的重要性。同时指出随着嵌入式平台中伪谱最优控制技术的实施应用，这一理论正以前所未有的方式改变航空航天控制问题的解决方案。
## 75. `cs.AI` - MODEST: 多光学景深立体数据集 [PDF](https://arxiv.org/pdf/2511.20853), [HTML](https://arxiv.org/abs/2511.20853)
### Authors
Nisarg K. Trivedi,Vinayak A. Belludi,Li-Yun Wang,Pardis Taghavi,Dante Lok
### Background
在自主机器人和增强现实等相机视觉系统中，基于真实光学条件的可靠深度估计仍然是一个核心挑战。尽管近期在深度估计和景深渲染方面取得了进展，但由于缺乏大规模、高保真的真实双目单反相机数据集，研究受到很大限制。现有模型基于合成数据训练，其在现实世界的应用和评价效果受到限制。
### Innovation
本文提出了首个高分辨率（5472×3648px）双目单反相机数据集，包含18000张图像，系统地改变焦距和光圈，涵盖复杂真实场景，真实还原并呈现专业相机系统的光学现实性和复杂性。该数据集覆盖了全方位的光学配置，对单目和立体深度估计、浅景深渲染、去模糊、三维场景重建和新颖视图合成提供了可控的分析支持。每种焦距配置都有专用的校准图像集，支持经典和学习方法的内、外校准评价。
### Conclusion
本文旨在弥合合成训练数据与真实相机光学之间的现实差距，并展示当前最先进的单目、立体深度及景深方法面临的挑战。数据集、校准文件和评估代码已公开，以促进真实光学条件下可重复研究的发展。
## 76. `cs.AI` - 计算多人博弈中的进化稳定策略 [PDF](https://arxiv.org/pdf/2511.20859), [HTML](https://arxiv.org/abs/2511.20859)
### Authors
Sam Ganzfried
### Background
就在非退化标准型博弈中，计算所有进化稳定策略的问题一直是博弈论和演化博弈理论中的一个挑战。本文旨在提供一种计算三人及以上玩家博弈中的所有进化稳定策略的算法。
### Innovation
本文提出了一个新的算法，专门用于计算三人或多于三人的非退化标准型博弈中的所有进化稳定策略。
### Conclusion
通过提出的方法，可以在多人博弈中系统地找到所有进化稳定策略，为理解复杂系统中的演化动态提供了一种新的工具。
## 77. `cs.AI` - 从舌尖效应检索查询的无监督记忆建模 [PDF](https://arxiv.org/pdf/2511.20854), [HTML](https://arxiv.org/abs/2511.20854)
### Authors
Sree Bhattacharyya,Yaman Kumar Singla,Sudhir Yarram,Somesh Kumar Singh,Harini S I,James Z. Wang
### Background
视觉内容的记忆性（memorability）已经引起了科学界的长期关注，它有着广泛的应用，从理解人类记忆的复杂方面到增强内容设计。然而，针对这一领域的进展面临一个重大挑战，即收集人类记忆性注释的过程非常昂贵，这限制了用于建模视觉内容记忆性的数据集的多样性和扩展性。大多数现有的数据集仅限于收集视觉内容的综合记忆性评分，而未能捕捉自然、开放式回忆描述中存在的细微记忆性信号。
### Innovation
本文引入了第一个大规模的无监督数据集，专为建模视觉记忆性信号而设计，包含82,000个以上视频，以及描述性回忆数据。利用来自在线平台（如Reddit）的舌尖效应（tip-of-the-tongue, ToT）检索查询。可以看出，该无监督数据集为记忆性相关任务生成回忆和ToT检索提供了丰富的信号。通过在我们的数据集上微调大型视觉-语言模型，相较于GPT-4o等最先进的模型，能更出色地生成开放式的记忆性描述。本文还使用对比训练策略创建了首个能完成多模态ToT检索的模型。
### Conclusion
我们的数据集和模型提出了一个新的方向，推动了视觉内容记忆性研究的进展。
## 78. `cs.AI` - Pix欺诈分类：攻击方法、人工智能驱动的放大和防御策略 [PDF](https://arxiv.org/pdf/2511.20902), [HTML](https://arxiv.org/abs/2511.20902)
### Authors
Glener Lanes Pizzolato,Brenda Medeiros Lopes,Claudio Schepke,Diego Kreutz
### Background
本文回顾了针对Pix（巴西中央银行于2020年推出的即时支付系统）的攻击方法。该研究旨在识别和分类影响用户和金融机构的主要欺诈类型，强调这些技术的演变和复杂性增加。
### Innovation
该研究的创新之处在于结合了结构化的文献回顾和针对银行领域专业人士的探索性访谈，揭示了欺诈方案从纯社会工程方法演化为结合人类操控和技术利用的混合策略。
### Conclusion
研究结论认为，安全保障措施必须与攻击方法的日益复杂性保持同步，特别强调适应性防御和持续的用户意识提高。
## 79. `cs.AI` - 通过空文本嵌入优化实现文本到图像扩散模型的推理时对齐 [PDF](https://arxiv.org/pdf/2511.20889), [HTML](https://arxiv.org/abs/2511.20889)
### Authors
Taehoon Kim,Henry Gouk,Timothy Hospedales
### Background
现有的测试时对齐（TTA）方法倾向于在优化目标奖励函数时过度或不足地进行优化，存在优化不足或导致奖励劫持的风险。现有的TTA方法通过操作潜在或噪声变量来调整目标奖励函数，这可能会导致非语义噪声模式被利用，从而改善奖励。
### Innovation
本文提出了基于空文本嵌入优化的Null-Text Test-Time Alignment（Null-TTA）方法。该方法通过优化分类器自由引导中的无条件嵌入来对齐扩散模型，而不是通过操作潜在或噪声变量来调整目标奖励函数。这种方法确保了对齐发生在一个具有语义连贯性的流形上，从而防止了奖励劫持。Null-TTA方法直接引导模型的生成分布趋向于目标奖励，而不仅仅是调整样本，而且无需更新模型参数，从而实现了最强的跨奖励通用性。
### Conclusion
Null-TTA方法在实现最佳目标推理时对齐的同时，保持了强大的跨奖励泛化能力，表明语义空间优化是TTA的一个有效且原理上新颖的方法。
## 80. `cs.AI` - 结构化提示使语言模型的评估更为稳健和全面 [PDF](https://arxiv.org/pdf/2511.20836), [HTML](https://arxiv.org/abs/2511.20836)
### Authors
Asad Aali,Muhammad Ahmed Mohsin,Vasiliki Bikia,Arnav Singhvi,Richard Gaus,Suhana Bedi,Hejie Cui,Miguel Fuentes,Alyssa Unell,Yifan Mai,Jordan Cahoon,Michael Pfeffer,Roxana Daneshjou,Sanmi Koyejo,Emily Alsentzer,Percy Liang,Christopher Potts,Nigam H. Shah,Akshay S. Chaudhari
### Background
随着语言模型（LMs）在多个领域中越来越广泛地被采用，高质量的基准评估框架对于指导部署决策至关重要。虽然Holistic Evaluation of Language Models (HELM)等框架能够进行广泛的任务评估，但它们往往依赖于固定的提示，这些提示在跨语言模型推广时常常缺乏代表性，导致性能估计不准确。除非我们能够估计每个语言模型的天花板（即通过更改提示所能达到的最高性能），否则我们可能会低估其性能。先前虽然有一些可扩展的提示框架如DSPy，但它们尚未在标准基准上进行系统的评估。因此，需要一种新的方法来更好地评估LMs的性能。
### Innovation
该论文提出了一个可以重现的DSPy+HELM框架，通过引入结构化提示方法来激发推理，使得评估更准确。研究使用四种结构化提示方法在四个前沿LMs上，进行七项基准测试（通用/医学领域），并与现有的HELM基线分数进行了对比。结果显示，在未使用结构化提示的情况下，HELM低估了LMs的性能，性能估计在不同基准上变化更为明显，成绩差距被错误地代表，并且引入推理（逐步推理）可以减少LMs对提示设计的敏感性。
### Conclusion
这是首次大规模的基准评估研究，实证地描述了LMs在不同基准和提示方法上的行为，表明可扩展的性能天花板估计能够使评估对部署决策更具有实用价值。研究开放源代码，包括DSPy+HELM集成（链接：this https URL）和提示优化管道（链接：this https URL）。
## 81. `cs.AI` - Length-MAX Tokenizer for Language Models [PDF](https://arxiv.org/pdf/2511.20849), [HTML](https://arxiv.org/abs/2511.20849)
### Authors
Dong Dong,Weijie Su
### Background
在训练和生成文本时，语言模型的分词方法会影响效率和性能。现有的分词方法如Byte Pair Encoding (BPE)主要基于字符频率进行分词，可能会导致分词后的文本中出现不必要的冗余和重复，从而影响模型的训练效率和生成效率。
### Innovation
提出了一种新的分词方法——Length-MAX tokenizer，该方法通过最大化分词长度权重的目标函数，并将其转化为图划分问题来获取词汇表，进而减少了平均每个字符的分词数量。与BPE相比，Length-MAX tokenizer在词汇量从10K到50K的范围内，减少了14-18%的分词数量。在训练GPT-2模型时，使用的步骤减少了18.5%到18.5%，在推理时延迟降低了13.7%到13.7%，同时在某些数据集上提高了准确性，如在LAMBADA测试上的困惑度降低了11.7%，在HellaSwag任务上的准确率提高了4.3%。
### Conclusion
优化平均分词长度而非单纯频率，可以有效提高语言模型的效率同时不牺牲甚至提升下游任务的性能。该分词器适用于生产系统，能够减少推理时的嵌入和KV缓存内存使用率18%。
## 82. `cs.AI` - 开放词汇组合理解在神经元对齐中的应用 [PDF](https://arxiv.org/pdf/2511.20931), [HTML](https://arxiv.org/abs/2511.20931)
### Authors
Biagio La Rosa,Leilani H. Gilpin
### Background
神经元是深度神经网络的基本构建块，它们之间的连接使人工智能达到前所未有的成果。为了理解神经元如何编码信息，复合解释利用概念之间的逻辑关系来表达神经元激活与人类知识的空间对齐关系。然而，这些解释依赖于人工标注的数据集，限制了其应用范围，主要局限于特定领域和预定义的概念。
### Innovation
本文提出了一个框架，该框架可以在视觉领域允许用户探究神经元以获取任意概念和数据集。该框架利用开放式词汇语义分割生成的掩码来计算开放式词汇的复合解释。该框架共分为三步：指定任意概念、使用开放式词汇模型生成语义分割掩码、根据这些掩码推导复合解释。该研究还在定量指标和人工可解释性方面对比了提出的方法与过去的工具，并且分析了从使用人工标注数据到使用模型标注数据进行解释时的差异，并展示了该框架在灵活性方面的增强能力。
### Conclusion
该论文通过比较新提出的框架与以前的用于计算复合解释的方法，展示了新框架在人工可解释性和灵活性方面的优势，并探讨了使用模型标注数据进行解释时的不同之处。
## 83. `cs.AI` - NOIR 2.0: 基于神经信号操作的智能机器人用于日常活动 [PDF](https://arxiv.org/pdf/2511.20848), [HTML](https://arxiv.org/abs/2511.20848)
### Authors
Tasha Kim,Yingke Wang,Hanvit Cho,Alex Hodges
### Background
NOIR系统是一个多功能的脑-机接口，允许人类使用他们的脑信号控制机器人进行日常任务。该接口利用脑电图（EEG）将人类关于特定对象和所需行动的意图直接转化为机器人可以执行的命令。
### Innovation
NOIR 2.0比之前的版本具有更快和更准确的大脑解码算法，将任务完成时间减少了46%。它还采用了一种少量示例的机器人学习算法，可以适应个别用户并预测其意图。新的学习算法利用了基础模型，实现了更有效的学习和适应（15个演示 vs. 单独一个演示），从而减少了总体的人类时间投入65%。
### Conclusion
NOIR 2.0通过提升解码精度、适应鲁棒性和学习效率，显著提高了脑-机接口的用户体验和应用范围，使其更加适合于日常活动中的实际应用。
## 84. `cs.AI` - 在具有潜在状态的仿真器中选择近似信念状态 [PDF](https://arxiv.org/pdf/2511.20870), [HTML](https://arxiv.org/abs/2511.20870)
### Authors
Nan Jiang
### Background
仿真器的重置状态是一个基本但经常被忽视的能力，它可以支持基于样本的规划，并通过将模拟状态重置为先前遇到的状态来校准仿真器。然而，在复杂的仿真器中实现状态重置可能并不简单，特别是当仿真器带有潜在变量（状态）时，需要从给定可观察历史的潜在状态的后验概率进行采样，即所谓的信念状态。虽然精确采样往往是不可能的，但可以通过多种近似信念状态采样器进行构造。
### Innovation
本文将问题归结为一种一般条件分布选择任务，并在仅通过采样访问仿真器的情况下开发了一种新的算法和分析。基于这种归约，信念状态选择问题可以采用两种不同的形式：潜在状态为基础的选择，直接针对潜在状态的条件分布；以及基于观测的选择，针对由观测诱导的分布。有趣的是，这些形式在与下游滚动方法的保证方式上有所不同：单重重置的方法下，基于观测的选择可能会失败，但在遵循不太常见的替代方法（称为重复重置）下，它则具有保证。
### Conclusion
本文讨论了分布偏移等问题，并提出了算法选择、理论细微差别和开放问题中的丰富景观，揭示了在这一看似简单的问题中的复杂性。
## 85. `cs.AI` - 在败血症治疗中探索时间步长在强化学习中的应用 [PDF](https://arxiv.org/pdf/2511.20913), [HTML](https://arxiv.org/abs/2511.20913)
### Authors
Yingchuan Sun,Shengpu Tang
### Background
当前关于使用强化学习（RL）进行败血症管理的研究大多遵循一种已建立的问题设定，其中患者数据被汇总为4小时的时间步长。虽然有人质疑这种粗粒度的时间步长可能导致患者动力学的失真并导致次优治疗策略，但在实际应用中这种问题的程度尚未被充分探索。
### Innovation
本文通过在给定4小时时间步长的场景下执行实验，对四种不同的时间步长（1小时、2小时、4小时和8小时）进行了实证比较，并设计了动作重新映射方法以便于在不同时间步长的数据集上进行公平比较。此外，本文在两种策略学习设置下进行了跨时间步长的模型选择，旨在量化时间步长对状态表示学习、行为克隆、策略训练和离策评估的影响。
### Conclusion
结果表明，不同时间步长下的性能趋势会随着学习设置的变化而有所不同，而使用静态行为策略在细粒度时间步长（1小时和2小时）下学习得到的策略在整体上性能和稳定性最佳。本文强调了时间步长是健康护理领域离策RL中的核心设计选择，提供了支持超越传统4小时间隔的证据。
## 86. `cs.AI` - Evo-Memory: 自适应记忆评估LLM代理的测试时学习 [PDF](https://arxiv.org/pdf/2511.20857), [HTML](https://arxiv.org/abs/2511.20857)
### Authors
Tianxin Wei,Noveen Sachdeva,Benjamin Coleman,Zhankui He,Yuanchen Bei,Xuying Ning,Mengting Ai,Yunzhe Li,Jingrui He,Ed H. Chi,Chi Wang,Shuo Chen,Fernando Pereira,Wang-Cheng Kang,Derek Zhiyuan Cheng
### Background
大语言模型（LLM）代理进行长期规划和问题解决需要状态信息，因此记忆管理成为一个关键问题，但在这方面现有的研究还很不充分。现有的评估方法主要集中在静态对话场景中，忽视了从交互中不断积累和复用经验的能力。在实际应用中，如交互式问题助手或具身智能体，LLMs 需要处理连续的任务流，但由于无法从过去的交互中学习，往往会丢失宝贵的上下文洞察，这需要在测试时优化记忆，使其能够连续搜索、适应和更新记忆。
### Innovation
提出了Evo-Memory，这是一种全面的流式基准和框架，用以评估LLM代理的自适应记忆。Evo-Memory将数据集划分为连续的任务流，要求代理在每次交互后搜索、适配和进化记忆。此外，统一实现了十多个代表性记忆模块，并在十个不同的多轮目标导向和单轮推理与QA数据集中进行了评估。为了更好地测试经验复用，还提供了ExpRAG基线方法，用于检索和利用先前的经验，进一步提出了ReMem模型，这是一种决策-推理-记忆循环管道，将推理、任务执行和记忆更新紧密集成，以实现持续改进。
### Conclusion
Evo-Memory 结果表明，现有的记忆组件在实时自适应性方面存在不足，提出了改进方向和未来的评估挑战。
## 87. `cs.AI` - 大规模分散协调电动汽车充电基础设施的弹性充电架构 [PDF](https://arxiv.org/pdf/2511.20943), [HTML](https://arxiv.org/abs/2511.20943)
### Authors
Chuhao Qin,Alexandru Sorici,Andrei Olaru,Evangelos Pournaras,Adina Magda Florea
### Background
随着电动汽车(EVs)的快速普及，分散式充电控制面临重大挑战。现有的分散式方法能够高效地协调大量EVs的选择，降低能源成本，防止电力峰值，并保护驾驶员隐私。然而，在严重的故障情况下，例如充电站断电或出现意外的充电请求激增时，这些方法往往无法有效应对。在这种情况下， limited 的充电插槽竞争加剧，导致排队时间和驾驶员舒适度下降。
### Innovation
本文提出了一种新颖的集体学习协同框架，允许EVs在个体舒适度和系统效率之间进行平衡。在该框架中，EVs被推荐进行自适应充电行为，这些行为在舒适度和效率之间切换优先级，以在不同的充电站容量和动态时空EV分布下实现帕累托最优的一致性。实验证明，本文提出的方法优于基准方法，显著减少了旅行和排队时间。研究结果还表明，当条件不确定时，按照适当时刻自私或利他的行为的EV驾驶员比持续保持中等行为的驾驶员的排队等待时间更短。
### Conclusion
在高比例充电站断电和恶意EV的场景下，本文的研究进一步证明了分散式电动汽车充电基础设施的增强弹性和可靠性。
## 88. `cs.AI` - 进化样本权重用于偏见缓解：优化目标的影响 [PDF](https://arxiv.org/pdf/2511.20909), [HTML](https://arxiv.org/abs/2511.20909)
### Authors
Anil K. Saini,Jose Guadalupe Hernandez,Emily F. Wong,Debanshi Misra,Jason H. Moore
### Background
在使用实际数据训练的机器学习模型中，可能会无意中产生带有偏见的预测结果，这对边缘化社区造成负面影响。重新加权是一种方法，通过为每个用于模型训练的数据点分配一个权重来缓解这种偏见。本研究比较了三种生成这些权重的方法：使用遗传算法（GA）进化生成权重、仅使用数据集特性计算权重、以及为所有数据点分配相同权重。通过使用配对的预测和公平性度量评估模型性能，这些度量也用作进化过程中GA的优化目标。
### Innovation
研究通过遗传算法进化生成权重的方法，并将其与其他基于数据集特性和等权重分配方法进行比较。实验结果显示，进化生成的权重可以产生比其他加权策略更好的公平性和预测性能的权衡。然而，这些好处的大小取决于优化目标的选择。
### Conclusion
实验发现，使用准确性和人口统计差异度量进行优化可以在较多的数据集上使进化权重在同时优化两者目标方面获得显著优势。
## 89. `cs.AI` - SPACE: 利用SPACE模型探索开发人员生产力的度量标准 [PDF](https://arxiv.org/pdf/2511.20955), [HTML](https://arxiv.org/abs/2511.20955)
### Authors
Sanchit Kaul,Kevin Nhu,Jason Eissayou,Ivan Eser,Victor Borup
### Background
这篇论文探讨了现有的一维生产力启发式方法的局限性，并通过广泛应用的源代码仓库挖掘实证研究了SPACE框架。研究使用了开源代码仓库的数据集，并应用了多项统计方法，如广义线性混合模型（GLMM）和基于RoBERTa的情感分类，综合评估了一个全方位的多维度生产力指标。
### Innovation
研究通过广泛的数据挖掘和先进的统计分析方法，为生产力评估提供了新的角度和深度。特别是通过分析贡献者交互的拓扑结构，提供了一种比传统基于体积的度量更精确衡量协作动态的方法，并提出了一个综合生产力评分（CPS），以解决开发人员效率的异质性问题。
### Conclusion
研究结果显示，负面情感状态与提交频率之间存在显著的正相关性，这表明一种由挫败感驱动的迭代补救循环。此外，贡献者交互的拓扑结构分析优于传统的基于体积的度量，能够更准确地映射协作动态。最终，该研究提出了一个综合生产力评分（CPS）以应对开发人员效率的异质性问题。
## 90. `cs.AI` - 在大型音频语言模型中朝向音频令牌压缩 [PDF](https://arxiv.org/pdf/2511.20973), [HTML](https://arxiv.org/abs/2511.20973)
### Authors
Saurabhchand Bhati,Samuel Thomas,Hilde Kuehne,Rogerio Feris,James Glass
### Background
大型音频语言模型（LALMs）在多种任务上表现出色，从语音识别到一般音频理解。但是，它们由于注意力机制的二次复杂性和音频信号高的令牌率，扩展到长音频和资源受限的边缘设备中存在局限性。
### Innovation
本文探索了无监督切分等技术，减少输入音频令牌数量，但在此之前不会被语言模型解码器消耗。通过低秩适配器对模型进行微调，以缓解压缩表示引入的性能下降。实验表明，压缩LALMs能够在减少音频令牌输入量的情况下，接近帧级LALMs的效果。
### Conclusion
实验结果显示，压缩音频语言模型可以在减少输入音频令牌数量的同时，达到接近帧级LALMs的效果，而且在自动语音识别和语音到语音翻译任务中表现良好。
## 91. `cs.AI` - AI4X路线图：用于科学追求的人工智能及其未来方向 [PDF](https://arxiv.org/pdf/2511.20976), [HTML](https://arxiv.org/abs/2511.20976)
### Authors
Stephen G. Dale,Nikita Kazeev,Alastair J. A. Price,Victor Posligua,Stephan Roche,O. Anatole von Lilienfeld,Konstantin S. Novoselov,Xavier Bresson,Gianmarco Mengaldo,Xudong Chen,Terence J. O'Kane,Emily R. Lines,Matthew J. Allen,Amandine E. Debus,Clayton Miller,Jiayu Zhou,Hiroko H. Dodge,David Rousseau,Andrey Ustyuzhanin,Ziyun Yan,Mario Lanza,Fabio Sciarrino,Ryo Yoshida,Zhidong Leong,Teck Leong Tan,Qianxiao Li,Adil Kabylda,Igor Poltavsky,Alexandre Tkatchenko,Sherif Abdulkader Tawfik,Prathami Divakar Kamath,Theo Jaffrelot Inizan,Kristin A. Persson,Bryant Y. Li,Vir Karan,Chenru Duan,Haojun Jia,Qiyuan Zhao,Hiroyuki Hayashi,Atsuto Seko,Isao Tanaka,Omar M. Yaghi,Tim Gould,Bun Chan,Stefan Vuckovic,Tianbo Li,Min Lin,Zehcen Tang,Yang Li,Yong Xu,Amrita Joshi,Xiaonan Wang,Leonard W.T. Ng,Sergei V. Kalinin,Mahshid Ahmadi,Jiyizhe Zhang,Shuyuan Zhang,Alexei Lapkin,Ming Xiao,Zhe Wu,Kedar Hippalgaonkar,Limsoon Wong,Lorenzo Bastonero,Nicola Marzari,Dorye Luis Esteras Cordoba,Andrei Tomut,Alba Quinones Andrade,Jose-Hugo Garcia
### Background
人工智能和机器学习正在重新塑造科学研究的方式，它们扩展了研究人员可以探查、预测和设计的范围，而不仅仅是取代现有的方法。本文概要地提供了一个人工智能增强科学的前瞻观点，涵盖了生物学、化学、气候科学、数学、材料科学、物理、自主实验室以及非传统计算等领域。在这些领域中，数据的多样性和可信性、传输性电子结构模型和自原子模型、将AI系统集成到从模拟到实验的端到端科学工作流程中、生成系统基于合成而非纯粹理想状态等几个共同主题浮现。
### Innovation
本研究强调了大数据、方法和基础设施方面面临的瓶颈，并勾勒出如何构建更强大、更透明、能够在复杂真实世界环境中加速发现的AI系统的具体方向。概述了大型基础模型、主动学习和自主实验室如何在预测和验证之间建立循环，同时保持可重复性和物理可解释性。
### Conclusion
本文描绘了今天AI增强科学的位置，明确了数据、方法和基础设施方面的瓶颈，并勾勒了构建更强大、更透明、能够加快复杂现实环境中发现的AI系统的具体方向，以期推动科学发展。
## 92. `cs.AI` - 控制策略中的动态测试时计算缩放：基于难度感知的随机插值策略 [PDF](https://arxiv.org/pdf/2511.20906), [HTML](https://arxiv.org/abs/2511.20906)
### Authors
Inkook Chun,Seungjae Lee,Michael S. Albergo,Saining Xie,Eric Vanden-Eijnden
### Background
现有的扩散和流基于的控制策略在长期机器人操作和模仿学习任务中表现出卓越的性能，但这些控制器在每一次控制步骤中都采用固定的推理预算，而不考虑任务复杂性，导致对于简单的子任务计算效率低下，而对于复杂的任务可能表现不佳。
### Innovation
引入了基于难度感知随机插值策略（DA-SIP），这是一种框架，可以让机器人控制器根据任务难度实时调整其积分周期。这种方法使用难度分类器动态选择每控制循环中的步骤预算、最优求解变体和常微分/随机微分方程的积分。DA-SIP构建在随机插值形式的基础上，提供了一个统一的框架，解锁了扩散和流基于策略的各种训练和推理配置。
### Conclusion
通过在多种操纵任务中进行全面基准测试，DA-SIP能够将总计算时间减少2.6-4.4倍，同时保持与固定最大计算基线相当的任务成功率。通过在此框架中实施自适应计算，DA-SIP将生成的机器人控制器转变为了高效的、任务感知的系统，能够智能地将推理资源分配到最需要的地方。
## 93. `cs.AI` - 即便有AI，双向映射发现仍然困难：OpenEvolve在新颖双向映射构建中的机遇与挑战 [PDF](https://arxiv.org/pdf/2511.20987), [HTML](https://arxiv.org/abs/2511.20987)
### Authors
Davis Brown,Jesse He,Helen Jenne,Henry Kvinge,Max Vargas
### Background
进化程序合成系统如AlphaEvolve、OpenEvolve和ShinkaEvolve为AI辅助的数学发现提供了一种新的方法。这些系统利用大型语言模型（LLMs）团队生成问题的候选解，并以人类可读的代码形式呈现。这些候选解决方案随后通过进化过程进行改进，超越单一生成的结果。尽管现有的数学应用主要集中在建立界面上的问题（例如球体堆积），但这种程序合成方法非常适合解决方案需呈现为明确构造的问题。在此基础上，本文探讨了使用OpenEvolve进行组合双射发现的可能性。
### Innovation
本文尝试使用OpenEvolve解决三个双射构造问题，包括两个已知和一个开放问题。研究发现虽然OpenEvolve等系统在组合数学家眼中具有潜力作为重要的研究工具，但在寻找新颖的研究级别双射方面，当前的前沿系统仍然面临挑战，表明在环节数学家的必要性。作者还分享了一些宝贵的经验教训供该领域的其他研究者参考。
### Conclusion
本文结果表明，尽管AI辅助工具如OpenEvolve有助于推动数学发现，但寻找新颖、研究水平的双射仍然是一个挑战性任务。人类数学家的参与依然是不可或缺的。
## 94. `cs.AI` - LLM引导开放世界强化学习中的子目标图增强规划 [PDF](https://arxiv.org/pdf/2511.20993), [HTML](https://arxiv.org/abs/2511.20993)
### Authors
Shanwei Fan
### Background
大型语言模型（LLMs）在强化学习（RL）中通过将任务分解为子目标来提供强大的高层规划能力，但它们的实际可用性受限于规划执行不一致的问题，这反映了抽象计划与可执行的、环境兼容的行为之间的关键差距。这种不一致源于两个相关限制：（1）LLMs往往生成在目标环境中由于缺乏环境特定的知识而不可行或无关的语义上可行的子目标，（2）单一LLM规划将生成与自我验证混淆，导致高度自信但不可靠的子目标，这些子目标在执行中经常失败。
### Innovation
我们提出了子目标图增强动作-批评-精炼框架（SGA-ACR），该框架结合了环境特定的子目标图和结构化实体知识，以及一个多LLM规划流水线，明确分离生成、批评和精炼，以生成可执行和可验证的子目标。还引入了子目标追踪器，以监控执行进度，提供辅助奖励，并动态更新子目标图，以保持计划与行动之间的对齐。
### Conclusion
在“Crafter”这一开放世界游戏中22个不同的任务上的实验结果证明了我们所提出方法的有效性。
## 95. `cs.AI` - 知识完成视觉：一种多模态实体感知检索增强生成框架用于新闻图像标题 [PDF](https://arxiv.org/pdf/2511.21002), [HTML](https://arxiv.org/abs/2511.21002)
### Authors
Xiaoxing You,Qiang Huang,Lingyu Li,Chi Zhang,Xiaopeng Liu,Min Zhang,Jun Yu
### Background
新闻图像标题生成的目标是结合视觉内容和相关文章中的上下文线索生成记者式的描述。尽管近期有进展，现有的方法在处理三个关键挑战时仍存在问题：（1）不完整的信息覆盖；（2）弱跨模态对齐；（3）视觉实体配对效果不佳。
### Innovation
为了解决这些问题，我们引入了MERGE，这是一个新的多模态实体感知检索增强生成框架，用于新闻图像标题生成。MERGE构建了一个基于实体的多模态知识库（EMKB），整合了文本、视觉和结构化知识，增强了背景检索。它通过多阶段假设-标题策略改进了跨模态对齐，并通过图像内容引导的动态检索增强了视觉实体配对。
### Conclusion
在GoodNews和NYTimes800k上的广泛实验表明，MERGE显著超过了最先进的基线方法，在描述质量方面有6.84的CIDEr增益和1.16的F1分提高，在实体识别方面则有4.14和2.64的提高。尤其值得注意的是，MERGE还对未见过的Visual News数据集进行了很好的泛化，在CIDEr和F1分数上分别提高了20.17和6.22，展示了其强大的鲁棒性和领域适应性。
## 96. `cs.AI` - FANoise：基于奇异值自适应噪声调制的鲁棒多模态表示学习 [PDF](https://arxiv.org/pdf/2511.20997), [HTML](https://arxiv.org/abs/2511.20997)
### Authors
Jiaoyang Li,Jun Fang,Tianhao Gao,Xiaohui Zhang,Zhiyuan Liu,Chao Liu,Pengzhang Liu,Qixia Jiang
### Background
代表学习是现代机器学习的基础，推动了文本检索和多模态理解等应用的发展。然而，学习稳健且可泛化的表示仍然具有挑战性。尽管先前的工作表明，主动噪声注入（一种数据增强形式）能够提高编码性能，但大多数现有方法依赖于启发式或静态噪声，忽略了在训练过程中特征分布的动态性。
### Innovation
我们系统地从梯度和特征分布角度研究了噪声在表示学习中的作用，提出了基于对比学习动态的特征自适应噪声注入策略FANoise。该方法通过调和噪声的负面影响和保留其益处，全面改善了各种基VLM模型在多模态任务中的整体性能。
### Conclusion
在理论上合理的框架指导下的实验表明，FANoise 在各种多模态任务中始终提高了整体性能。
## 97. `cs.AI` - 基于结构感知的原型引导可信多视图分类 [PDF](https://arxiv.org/pdf/2511.21021), [HTML](https://arxiv.org/abs/2511.21021)
### Authors
Haojian Huang,Jiahao Shi,Zhe Liu,Harold Haodong Chen,Han Fang,Hao Sun,Zhongjiang He
### Background
在复杂场景中，多源信息存在异构性、不一致性甚至冲突，这给实现可靠的决策带来了挑战。现有的多视图分类（TMVC）方法多依赖于全局密集的邻居关系来建模内视图间的关系，导致计算成本高且无法直接确保视图间的一致性。此外，这些方法通常通过手动分配的权重来聚合不同视图的证据，这些方法的学习所得的多视图邻居结构在类空间内通常缺乏一致性保证，从而影响分类结果的可信度。
### Innovation
本文提出了一种新的TMVC框架，通过引入原型来表示每个视图的邻居结构。这种方法简化了内视图邻居关系的学习，并允许内视图和视图间结构的动态对齐，从而促进跨视图一致共识的更高效发现。该方法在多个公开的多视图数据集上进行了大量实验，证明了其与常用的TMVC方法相比，在下游性能和鲁棒性方面具有竞争力。
### Conclusion
所提出的基于结构感知的原型引导可信多视图分类方法在多个公开的多视图数据集上取得了与传统TMVC方法相当甚至更好的性能，并且具有更强的鲁棒性，解决了现有方法的数据依赖性和缺乏类空间一致性的问题。
## 98. `cs.AI` - 使用自回归条件生成对抗网络进行概率性野火蔓延预测 [PDF](https://arxiv.org/pdf/2511.21019), [HTML](https://arxiv.org/abs/2511.21019)
### Authors
Taehoon Kang,Taeyong Kim
### Background
气候变化加剧了野火的频率和严重程度，使得快速和准确预测火势蔓延变得至关重要，以便有效进行缓解和应对。物理基础模拟器如FARSITE提供高保真预测但计算强度高，限制了其在实时决策中的应用，而现有的深度学习模型往往产生过于平滑的预测，无法捕捉野火蔓延的复杂非线性动态。
### Innovation
本文提出了一种自回归条件生成对抗网络（CGAN）进行概率性野火蔓延预测。通过将预测任务建模为自回归问题，模型学习顺序状态转移，确保长期预测稳定性。实验结果表明，所提出的基于CGAN的模型在整体预测准确性和火围边界划定方面优于传统深度学习模型。此外，对抗学习使得模型能够捕捉野火蔓延中的强烈非线性和不确定性，而不是简单地拟合像素平均值。自回归框架还支持野火演变的系统性时间预测。
### Conclusion
基于CGAN的自回归框架提高了野火蔓延预测的准确性和物理解释性，为时间敏感的响应和疏散计划提供了有希望的基础。
## 99. `cs.AI` - 在上下文学习中的语义锚点：小型LLM为何无法翻转标签 [PDF](https://arxiv.org/pdf/2511.21038), [HTML](https://arxiv.org/abs/2511.21038)
### Authors
Anantha Padmanaban Krishna Kumar(Boston University)
### Background
本文探讨了上下文学习（ICL）是否能绕过预训练标签的语义约束，还是仅仅改进了已有语义基础。研究者设计了方法，通过将大语言模型（LLMs）作为基于提示的分类器，并将其行为在自然示范（正确标签）和倒置示范（系统性翻转标签意义）下进行对比。
### Innovation
研究分解了ICL行为成三个对齐指标（真实度、先验和提示对齐），引入了语义覆盖率，定义为在翻转语义下的正确率。研究覆盖了8个分类任务和8个开源的LLMs（1-12B参数），结果显示一致的证据支持语义锚点的观点。自然示范下，ICL提升了准确性同时保持强先验对齐；在倒置示范下，模型无法学习连贯的反义分类器：提示对齐的增加是通过牺牲准确性来实现的，而且在少量样本1-12B参数设置中语义覆盖率保持为零。
### Conclusion
ICL主要调整了输入如何映射到预训练过程中学习到的稳定语义方向，而不是灵活调整标签意义。这揭示了少量样本提示的固有限制，并提示在这些规模下翻转标签语义需要超出ICL的干预措施。
## 100. `cs.AI` - BUSTR: 使用描述感知视觉语言模型进行乳腺超声文本报告 [PDF](https://arxiv.org/pdf/2511.20956), [HTML](https://arxiv.org/abs/2511.20956)
### Authors
Rawa Mohammed,Mina Attin,Bryar Shareef
### Background
自动化放射学报告生成（RRG）在乳腺超声（BUS）方面的应用受到缺乏配对图像-报告数据集的限制，且存在大型语言模型预测错误（hallucinations）的风险。现有的方法通常需要配对的图像-报告监督，这限制了其应用范围和准确性。
### Innovation
本文提出了一种多任务视觉语言框架BUSTR，用于生成BUS报告无需配对的图像-报告监督。BUSTR通过结构化描述（如BI-RADS、病理学、组织学）和成像特征构造报告，并利用多头Swin编码器在特定数据集描述集中训练多任务损失，学习描述感知的视觉表示，并通过结合令牌级交叉熵损失和余弦相似性对齐损失的双层目标来对齐视觉和文本标记。该框架在两个公共BUS数据集BrEaST和BUS-BRA上进行了评估。
### Conclusion
实验结果表明，该描述感知视觉模型，通过结合令牌级损失和对齐损失训练，可以在不依赖配对图像-报告数据的情况下，提高自动报告指标和临床有效性。源代码可以在以下网址获取：this https URL
## 101. `cs.AI` - 通过冲击回声信号和神经网络进行混凝土板的驱动评估 [PDF](https://arxiv.org/pdf/2511.21080), [HTML](https://arxiv.org/abs/2511.21080)
### Authors
Yeswanth Ravichandran,Duoduo Liao,Charan Teja Kurakula
### Background
混凝土桥面的亚表面缺陷如分层、空洞和蜂窝状缺陷严重影响其耐久性，但用视觉检查或手动敲击难以可靠地检测到这些缺陷。联邦公路管理局（FHWA）实验室试块和服役中的桥梁板在使用冲击回声（IE）技术进行缺陷检测时存在挑战。
### Innovation
本文提出了一种基于机器学习的冲击回声框架，该框架自动化了缺陷定位和常见混凝土缺陷的多类别分类。通过傅里叶变换（FFT）将原始IE信号转换为频域特征，并生成缺陷区域可视化图。利用未监督的k-均值聚类突出低频缺陷区域，并使用从实验室种子缺陷生成的Ground Truth Masks（GTMs）验证空间准确性并生成高置信度的训练标签。经过这些验证区域，空间有序的频域序列输入到堆叠的长短期记忆（LSTM）网络中，该网络以73%的整体准确率分类四种缺陷类型：浅分层、深分层、空洞和蜂窝状。现场验证表明，基于实验室数据训练的模型可以在现实耦合、噪声和环境变化下泛化。
### Conclusion
提出的框架增强了非破坏性评估（NDE）的客观性、可扩展性和可重复性，支持大规模网络的智能、基于数据的桥梁健康监控。
## 102. `cs.AI` - FedAPA: 基于自适应原型聚合的联邦学习在异构Wi-Fi CSI人群计数中的应用 [PDF](https://arxiv.org/pdf/2511.21048), [HTML](https://arxiv.org/abs/2511.21048)
### Authors
Jingtao Guo,Yuyi Mao,Ivan Wang-Hei Ho
### Background
Wi-Fi信道状态信息（CSI）基于感知提供了无需设备的侵入性活动识别和人群计数等任务的方法，但大规模部署受到需要大量现场特定训练数据的限制。联邦学习（FL）提供了一种避免原始数据共享的解决方案，但仍面临异构感知数据和设备资源的挑战。
### Innovation
本文提出了一种协作的Wi-Fi CSI基于感知算法FedAPA，该算法使用适应性原型聚合（APA）策略根据相似性为同伴原型分配权重，使客户端贡献适应性，并为每个客户端生成自定义的全局原型，而不是固定权重聚合。在本地训练期间，采用分类学习与表示对比学习相结合的目标函数，以对齐局部和全局知识。
### Conclusion
我们的研究结果表明，在真实的分布式Wi-Fi人群计数场景中，与多个基线相比，FedAPA方法在准确性和F1分数上提高了至少9.65%，在平均绝对误差（MAE）上降低了0.29，并将通信开销减少了95.94%。
## 103. `cs.AI` - 使用Kolmogorov-Arnold网络头部增强缅甸新闻分类 [PDF](https://arxiv.org/pdf/2511.21081), [HTML](https://arxiv.org/abs/2511.21081)
### Authors
Thura Aung,Eaint Kay Khaing Kyaw,Ye Kyaw Thu,Thazin Myint Oo,Thepchai Supnithi
### Background
在资源稀缺的语言（如缅甸语）中，分类任务通常只微调最终分类层，而固定预训练编码器权重。尽管多层感知机（MLPs）是常用方法，但其固有的非线性特性限制了其表达能力并增加了计算成本。本文探讨了使用Kolmogorov-Arnold网络（KANs）作为替代分类头部，并评估了基于Fourier的FourierKAN、基于Spline的EfficientKAN以及基于Grid的FasterKAN在TF-IDF、fastText和多语言变换器（mBERT、Distil-mBERT）等不同嵌入中的性能。
### Innovation
本文提出了使用Kolmogorov-Arnold网络（KANs）作为分类头部的创新方法，评估了不同基于Fourier、Spline和Grid的KAN变体，并在各种嵌入表示中进行了实验。研究结果显示KAN头部在资源稀缺语言分类中的表现与MLPs相当或更优。特别是EfficientKAN在使用fastText嵌入时达到了0.928的最高F1分，而FasterKAN在速度和准确性的权衡上表现出最佳的性能。
### Conclusion
研究得出Kolmogorov-Arnold网络（KANs）是替代多层感知机（MLPs）用于低资源语言分类的一种富有表现性和高效性选择。特别是在变换器嵌入中，EfficientKAN 在性能上甚至超过了mBERT（0.917 F1）的部分表现。
## 104. `cs.AI` - 使用平衡调优对大语言模型进行生物医学知识对齐 [PDF](https://arxiv.org/pdf/2511.21075), [HTML](https://arxiv.org/abs/2511.21075)
### Authors
Zhenchao Tang,Fang Wang,Haohuai He,Jiale Zhou,Tianxu Lv,Jun Zhu,Shouzhi Chen,Minghao Yang,Yu Wang,Jiayang Wu,Yidong Song,Jianhua Yao
### Background
对大语言模型（LLMs）进行有效的后训练是使其与专门的生物医学知识保持一致的关键，这对于加速生命科学研究至关重要。然而，当前的方法面临重大局限性。首先，生物医学推理涉及复杂的机制，经常通过稀疏文本数据表示，而标准的监督微调（SFT）倾向于过度拟合表面级别的指令模式，未能有效内化这种碎片化的科学知识。其次，强化学习（RL）在该领域不可行，因为定义有意义的奖励通常需要大量的实验验证（例如，湿实验验证药物反应），使得实时反馈不可能实现。
### Innovation
本文提出了平衡调优（BFT），一种高效的后训练方法，旨在从稀疏数据中学习复杂的推理，而不需要外部奖励信号。BFT通过两层权重机制工作：1. 具有标记层，通过预测概率缩放损失以稳定梯度并防止过度拟合；2. 具有样本层，使用“最小群体信心”来适应性增强难以学习样本的学习。实验表明，BFT在医疗任务中显著优于SFT。在生物任务中，它使得LLMs能够获得SFT遗漏的知识。此外，BFT生成的文本嵌入可以直接应用于下游任务，如基因相互作用和单细胞扰动反应预测。
### Conclusion
平衡调改进一步促进了LLMs在生物医学研究中的广泛应用。
## 105. `cs.AI` - 基于检索的实用元认知提示方法在讽刺检测中的应用 [PDF](https://arxiv.org/pdf/2511.21066), [HTML](https://arxiv.org/abs/2511.21066)
### Authors
Michael Iskandardinata,William Christian,Derwin Suhartono
### Background
尽管近年来神经网络方法取得了进展，但在自然语言处理（NLP）领域中，检测讽刺仍然是一个具有挑战性的任务。现有的预训练语言模型（PLMs）和大型语言模型（LLMs）是讽刺检测的首选方法。然而，讽刺文本的复杂性、语言多样性和跨不同社区的文化差异使得即使对于PLMs和LLMs这类先进模型，该任务也变得更加复杂。此外，这些模型还难以准确检测需要额外背景知识分析的词语或标记。
### Innovation
本文介绍了一种检索感知的方法，该方法通过检索给定目标文本的上下文信息，增强向量提示方法（PMP）。该方法通过增加从网络中检索到的非参数化知识，以及促使模型激活其内部知识来增强模型的自我认知，从而提供多样化的上下文信息。实验结果表明，非参数化检索在Twit-ter印尼讽刺数据集上比原始PMP方法提高了9.87%的宏F1值，自我知识检索在SemEval上提高了3.29%的宏F1值，在MUStARD上提高了4.08%的宏F1值。这强调了在提高LLMs在讽刺检测中的性能时，上下文的重要性，尤其是在使用文化特定俚语、参照或未知术语时。
### Conclusion
实验结果证明了本方法的有效性和重要性，未来工作将集中在优化相关上下文信息的检索，以及研究检索质量如何影响性能。
## 106. `cs.AI` - GuardTrace-VL: 通过迭代安全监督检测危险的多模态推理 [PDF](https://arxiv.org/pdf/2511.20994), [HTML](https://arxiv.org/abs/2511.20994)
### Authors
Yuxiao Xiang,Junchi Chen,Zhenchao Jin,Changtao Miao,Haojie Yuan,Qi Chu,Tao Gong,Nenghai Yu
### Background
多模态大型推理模型（MLRMs）被越来越多地部署用于视觉语言任务，并生成明确的中间推理说明。然而，即使最终答案无害，推理痕迹也可能包含不安全的内容，导致部署风险。现有的多模态安全防护主要评估输入问题和最终答案，忽视了中间的推理过程。这使得在推理过程中可能出现的偏差推理或违反政策的视觉上下文使用等未检测到的危害得以通过。
### Innovation
介绍了GuardTrace-VL，一个视觉感知安全审计器，通过联合图像-文本分析对完整的提问-思考-回答（QTA）管道进行监控，以检测推理过程中逐步出现的不安全内容。为了支持训练和评估，构建了GuardTrace数据集，该数据集通过多种提示策略生成，并通过机器学习模型和人类基于投票和验证的管道逐步精炼。此外，提出了一种三阶段渐进式训练方案结合数据精炼过程，使模型能够根据不同风险水平学习细微和上下文相关的安全偏好。据提出的数据集测试集评估，GuardTrace-VL模型在不安全推理检测任务中的F1得分为93.1%，比之前最强的多模态安全防护方法的F1得分提高了13.5%。代码将会公开。
### Conclusion
GuardTrace-VL模型在所提出的数据集测试集上实现了93.1%的F1分数，使得不安全推理检测任务的F1分数比之前最强的多模态安全防护方法提高了13.5%。
## 107. `cs.AI` - MLPMoE：密集LLM MLP的零样本架构变形为静态Mixture-of-Experts [PDF](https://arxiv.org/pdf/2511.21089), [HTML](https://arxiv.org/abs/2511.21089)
### Authors
Ivan Novikov
### Background
现有的大型语言模型（LLMs）主要由密集的Transformer结构组成，其中每个前馈块中的每个参数都会被激活。尽管这种结构在理论上较为简单，但在计算上却相当低效，因为推理成本与参数数量成线性关系。最近，有一些方法如MoEfication, CMoE, ToMoE和MoORE表明，许多有用计算都存在于密集前馈网络中的稀疏、半模块子结构中。但这些方法通常依赖于聚类、激活特征分析、奇异值分解或需要校准数据的自定义路由。
### Innovation
本文提出了MLPMoE（MLP Mixture-of-Experts），这是一种无需训练的确定性转换方法，将Transformer块中的密集MLP重新结构化为静态、高基数的专家组合。MLPMoE利用简单的张量切片和汇总，重新解释张量并行的代数作为拓扑转换，而不是分布式训练模式。此外还提出了分形淡入（分段分支稀疏性）和补偿剪枝（保持方差的分支削减）作为结构化稀疏性的轻量级机制。在对Qwen2.5-0.5B-Instruct和DeepSeek-R1-Distill-Llama-8B进行的实验中，零样本的MLPMoE转换仅改变了代理困惑度指标不到0.05%，同时参数计数基本保持不变。在8B模型上，差异化稀疏性移除了大约20%的MLP参数，同时使困惑度保持在密集基线的2%以内。这种方法在现有检查点上完全后处理，不需要梯度、校准集或路由器训练。
### Conclusion
MLPMoE方法实现了对现有检查点的后处理，无需训练、校准数据或路由训练，同时能够在保持模型性能的同时减少参数量和计算成本。
## 108. `cs.AI` - 从比特到轮次：探索驱动的并行解码方法用于扩散语言模型 [PDF](https://arxiv.org/pdf/2511.21103), [HTML](https://arxiv.org/abs/2511.21103)
### Authors
Hengyu Fu,Baihe Huang,Virginia Adams,Charles Wang,Venkat Srinivasan,Jiantao Jiao
### Background
扩散语言模型（DLMs）作为一种新颖的替代自动回归语言模型（LMs）的技术，已经在语言模型领域崭露头角。DLMs通过并行解码提供了更快的推理速度和相近的准确性。然而，现行的DLM解码策略依赖于高置信度的令牌，在信息论上存在固有瓶颈，这限制了解码的进展并最终减慢了生成速度。
### Innovation
该研究在理论上证明了优先选择高置信度令牌是低效的，因为这些高概率令牌提供的信息量非常少。提出了一种名为Explore-Then-Exploit（ETE）的无训练解码策略，它结合了跨块解码和对高不确定性令牌的有目标探索，以优化信息传输和解码效率。ETE策略能够减少所需的解码轮次，而不会牺牲生成质量。
### Conclusion
研究证明了信息量与解码轮次的线性关系，并指出解码轮次必须根据样本的总信息量线性增加，同时与每个环节的信息预算成反比。ETE的实验结果表明，它可以有效地减少所需解码轮次，而不会影响生成的质量。
## 109. `cs.AI` - 打破安全与能力权衡：具验证奖励的强化学习在LLM中维持安全边界 [PDF](https://arxiv.org/pdf/2511.21050), [HTML](https://arxiv.org/abs/2511.21050)
### Authors
Dongkyu Derek Cho,Huan Song,Arijit Ghosh Chowdhury,Haotian An,Yawei Wang,Rohit Thekkanal,Negin Sokhandan,Sharlina Keshava,Hannah Marlowe
### Background
大型语言模型（LLMs）在下游任务的微调通常会表现出安全与能力的基本权衡，即提高任务性能会导致安全对齐的下降，即使在良性数据集上也是如此。标准方法如监督微调（SFT）和基于人类反馈的强化学习（RLHF）都无法突破这一点。尽管具有可验证奖励的强化学习（RLVR）作为一种有潜力的替代方法已经出现，可以优化模型在客观可测量的任务上，但其安全性影响尚未得到探索。
### Innovation
本文首次提供了RLVR安全属性的全面理论和实证分析。理论上，作者推导了在KL限制优化下的安全漂移上限，并证明了可以消除安全下降的条件。实验中，作者在五个对抗安全性基准测试上进行了广泛的实验，显示RLVR可以同时增强推理能力同时维持或提高安全边界。全面的消融研究检查了优化算法、模型规模和任务领域的影响。研究结果质疑了不可避免的安全能力和权衡的现有假设，表明特定的训练方法可以同时实现这两个目标，为推理能力强的LLM的安全部署提供了见解。
### Conclusion
研究挑战了固有的安全与能力权衡的观点，并证明特定的训练方法可以在同时提高模型性能和保持安全性能之间取得平衡，从而为合理部署具有推理能力的大型语言模型提供了理论基础和实证支持。
## 110. `cs.AI` - MNM: 多级别神经影像元分析中的双曲脑-文本表征 [PDF](https://arxiv.org/pdf/2511.21092), [HTML](https://arxiv.org/abs/2511.21092)
### Authors
Seunghun Baek,Jaejin Lee,Jaeyoon Sim,Minjae Jeong,Won Hwa Kim
### Background
各种神经影像学研究常常受到样本量小的问题限制，这会影响其可靠性。传统的元分析方法通过聚合不同研究的发现来识别一致的脑活动模式，但这些方法在基于关键词检索或线性映射的传统方法中经常忽略了大脑中的丰富层次结构。
### Innovation
本文提出了一种新颖的框架，利用双曲几何将神经影像学文献和脑成像图嵌入到共享的双曲空间中，通过洛伦兹模型实现文本嵌入和脑成像的嵌入，从而捕捉神经影像学数据中固有的语义相似性和层次组织。该方法在双曲空间中进行多层次神经影像学元分析，通过1)将脑和文本嵌入对齐以实现语义对应，2) 在文本和脑激活之间引导层次结构，以及3) 保留脑激活模式内的层次关系来实现。
### Conclusion
实验结果表明，本文模型在多层次神经影像学元分析方面优于基线方法，提供了一种基于双曲脑-文本表示的稳健且可解释的元分析范式。
## 111. `cs.AI` - Deformation-aware Temporal Generation for Early Prediction of Alzheimer's Disease [PDF](https://arxiv.org/pdf/2511.21114), [HTML](https://arxiv.org/abs/2511.21114)
### Authors
Xin Honga,Jie Lin,Minghui Wang
### Background
阿尔茨海默病（AD）是一种进行性退化的大脑疾病，早期预测可以帮助减缓其进展。随着病情的发展，患者通常会出现大脑萎缩。当前用于预测阿尔茨海默病的方法主要涉及通过手工特征提取来分析大脑图像的形态学变化。然而，现有的方法依赖于大量手动特征工程，且对于时间序列MRI图像中存在的缺失数据处理不足，这对准确预测疾病进展提出了挑战。
### Innovation
本文提出了一种新颖的方法，即变形感知的时空生成网络（DATGN），用于自动学习疾病进展过程中大脑图像的形态学变化，以实现早期预测。DATGN首先通过插值缺失的时间序列数据，然后使用双向时空变形感知模块生成未来的MRI图像，并将其与疾病进展趋势保持一致，从而实现早期预测。实验结果表明，在ADNI数据集上生成的未来MRI图像时间序列结果在PSNR和MMSE图像质量指标上具有竞争力。此外，将DATGN生成的合成数据集成到基于SVM、CNN、3DCNN的分类方法中，实现了显著的分类准确性提升，尤其是在AD与NC及AD、MCI、NC分类方面。
### Conclusion
DATGN通过时空变形感知插值和生成技术，有效地填补了MRI时间序列中的缺失数据，确保未来图像生成与疾病进展趋势一致，从而实现了阿尔茨海默病的早期预测。
## 112. `cs.AI` - 动态分层对比学习及上游扩充方法在 MILP 分支中的应用 [PDF](https://arxiv.org/pdf/2511.21107), [HTML](https://arxiv.org/abs/2511.21107)
### Authors
Tongkai Lu,Shuai Ma,Chongyang Tao
### Background
Mixed Integer Linear Programming (MILP) 是一个 NP-hard 的基本类问题，引起了学术界和工业界的广泛关注。B& B 方法是求解 MILP 的主导方法，分支在整个 B& B 方法中起重要作用。近年来，基于神经网络的学习框架被开发出来以增强分支策略的效率和求解 MILP 的能力。然而，这些方法在应对深层次的语义差异、上游节点稀缺以及强分支样本收集昂贵方面仍然存在问题。
### Innovation
提出了一个动态分层对比训练框架（textbf{动态分层对比学习及上游扩充方法}），通过基于特征分布将分支-界限节点进行分组，并训练一个基于 GCNN 的辨别模型，以逐层分离节点，学习更细粒度的节点表示。为了缓解上游节点数据稀缺和不平衡的问题，引入了一个上游扩充 MILP 衍生过程，生成既是理论等价又是扰动实例的新实例。该方法在细微的节点语义差异建模上效果显著，提高了分支准确性和解题效率，特别惠及了上游节点。
### Conclusion
在标准 MILP 基准上的大规模实验表明，该方法提高了分支准确性，减少了求解时间，并在未见过的数据实例上展示了良好的泛化能力。
## 113. `cs.AI` - 学习细胞感知的层级多模态表示以实现稳健的分子建模 [PDF](https://arxiv.org/pdf/2511.21120), [HTML](https://arxiv.org/abs/2511.21120)
### Authors
Mengran Li,Zelin Zang,Wenbin Xing,Junzhou Chen,Ronghui Zhang,Jiebo Luo,Stan Z. Li
### Background
理解化学扰动如何在生物系统中传播对于精准预测分子属性至关重要。现有的大多数方法主要关注化学结构，而近期的发展显示，细胞响应（如形态和基因表达）在药物效应形成中起着关键作用。然而，当前的细胞感知方法存在两大局限性：外部生物数据不完整性以及在分子、细胞和基因组多层次间的依赖关系建模不足。
### Innovation
提出了一种名为CHMR（细胞感知的层级多模态表示）的稳健框架，该框架能够联合建模分子和细胞响应之间的局部与全局依赖性，并通过一种新颖的树结构向量量化模块捕捉潜在的生物层级结构。在9个公开基准测试中的728项任务上评估了CHMR，结果表明CHMR在分类任务中平均提高了3.6%，在回归任务中提高了17.2%，证实了层级感知、多模态学习在可靠和生物基础的分子表示中的优势。
### Conclusion
这些结果演示了多元化、多层次印象建模能为整合生物医学建模提供一个通用框架。
## 114. `cs.AI` - Pygmalion Effect in Vision: Image-to-Clay Translation for Reflective Geometry Reconstruction [PDF](https://arxiv.org/pdf/2511.21098), [HTML](https://arxiv.org/abs/2511.21098)
### Authors
Gayoung Lee,Junho Kim,Jin-Hwa Kim,Junmo Kim
### Background
三维重建中理解反射仍然是一个长期存在的挑战，因为视点相关的反射会导致外观和几何形状的纠缠。现有的方法在处理复杂反射的多视角图像时难以实现稳健的重建。
### Innovation
本文提出了名为“视觉中的皮格马利翁效应”的一个新颖框架，通过图像到泥巴的转换“雕刻”反射物体，这受到皮格马利翁神话的启发。该方法学习抑制镜面细节，同时保持固有的几何一致性，从而实现包含复杂反射的多视角图像的稳健重建。具体来说，该方法采用一个双分支网络，其中一个基于BRDF的反射分支由一个引导泥巴的分支补充，该分支稳定几何结构并细化表面法线。这种两个分支共同训练的方法使用合成的泥巴样图像提供一种中性的、无反射的监督信号，这补充了反射视图。
### Conclusion
实验结果表明，与现有的反射处理方法相比，该框架在法线准确性和网格完整性方面取得了显著改善。此外，该框架揭示了“未眩光下观看”，将辐射转换为中性性，可以作为反射物体几何学习的强大归纳偏差。
## 115. `cs.AI` - SocialNav: 培养借鉴人类的基模，实现社交意识的实体导航 [PDF](https://arxiv.org/pdf/2511.21135), [HTML](https://arxiv.org/abs/2511.21135)
### Authors
Ziyi Chen,Yingnan Guo,Zedong Chu,Minghua Luo,Yanfen Shen,Mingchao Sun,Junjun Hu,Shichao Xie,Kuan Yang,Pei Shi,Zhining Gu,Lu Liu,Honglin Han,Xiaolong Wu,Mu Xu,Yu Zhang
### Background
目前，实体导航（即机器人或其他实体在遵守社会规范的前提下进行导航）仍然是一个开放的研究挑战。
### Innovation
提出了一种名为SocialNav的基模，它具有分层的“大脑-行动”架构。SocialNav能够理解高阶社会规范，生成基阶、社会合规的动作轨迹。通过构造一个名为SocNav的数据集，该数据集包含700万样本，以及多步骤训练清单，该清单首先通过模仿学习将通用导航技能和社会规范理解注入模型，然后通过一种名为SAFE-GRPO的新框架进行社会意识的深入训练，这是第一个明确奖励社会合规行为的流动强化学习框架。
### Conclusion
SocialNav相比最先进的方法，实现了38%的成功率和46%的高社会一致性。这表明其在导航能力和社会一致性方面都取得了显著的进展。
## 116. `cs.AI` - 超越片段聚合：三层金字塔索引增强视觉文档检索 [PDF](https://arxiv.org/pdf/2511.21121), [HTML](https://arxiv.org/abs/2511.21121)
### Authors
Anup Roy,Rishabh Gyanendra Upadhyay,Animesh Rameshbhai Panara,Robin Mills
### Background
文档中心的RAG流水线通常从OCR开始，随后是脆弱的分块、表格解析和布局重建的启发式方法。这些以文本为主的方法维护成本高、对细微布局变化敏感，并且常常会丢失包含答案的空间线索。视觉优先检索已成为一种强有力的替代方案，通过直接操作页面图像，如ColPali和ColQwen这样的系统能够保留结构并减少流水线复杂性，同时还实现了强大的基准性能。然而，这些延迟交互模型将检索绑定到特定的视觉骨干模型，并要求存储每页数百个片段嵌入，导致高内存开销并增加了大规模部署的复杂性。
### Innovation
本文引入了VisionRAG，这是一种无需OCR且模型无关的多模态检索系统。VisionRAG直接将文档作为图像索引，保留布局、表格和空间线索，而无需承诺特定的提取。三层金字塔索引框架使用全局页面摘要、节标题、视觉热点和事实级线索来创建向量。这些摘要作为轻量级检索替代品。在查询时，VisionRAG使用金字塔索引检索最相关的页面，然后将原始页图像编码为base64传输给多模态LLM进行最终问答。检索过程中，互反 ranking 融合将信号综合以生成稳健的排名。相比基于片段的方法，VisionRAG存储每个页面17到27个向量，同时保持对多模态编码器的高度灵活性。在金融文档基准测试中，它实现了0.8051的准确率（FinanceBench）和0.9629的召回率（TAT DQA），这些结果表明，无需OCR，基于摘要引导的多模态检索是一种实用且具有扩展性的替代传统文本提取流水线的方法。
### Conclusion
VisionRAG是一种实用且可扩展的多模态检索方法，它在保持灵活性的同时提高了性能，为文档检索的未来应用提供了新的视角。
## 117. `cs.AI` - 基于熵引导优先分步学习的人类视频生成高效训练 [PDF](https://arxiv.org/pdf/2511.21136), [HTML](https://arxiv.org/abs/2511.21136)
### Authors
Changlin Li,Jiawei Zhang,Shuhao Liu,Sihao Lin,Zeyi Shi,Zhihui Li,Xiaojun Chang
### Background
扩散模型的发展促进了人类视频生成技术的进步，但训练这些模型时所需的高分辨率、多帧数据导致了高计算成本和大量内存消耗的问题。这给训练过程带来了显著挑战。
### Innovation
本文提出了熵引导优先分步学习（Ent-Prog）框架，该框架针对扩散模型在人类视频生成中的高效训练进行了优化。提出了条件熵膨胀（CEI）来评估不同模型组件在目标条件生成任务中的重要性，并实现对关键组件的优先训练。还引入了自适应分步调度，该调度根据收敛效率动态增加计算复杂度。Ent-Prog 框架在不牺牲生成性能的前提下，显著减少了训练时间和 GPU 内存消耗。
### Conclusion
在三个数据集上的广泛实验表明，Ent-Prog 方法在保持生成性能的同时，实现了高达 2.2 倍的训练速度提升和 2.4 倍的 GPU 内存减少。
## 118. `cs.AI` - 自我指导防御：通过合成准则实现推理模型的自适应安全对齐 [PDF](https://arxiv.org/pdf/2511.21214), [HTML](https://arxiv.org/abs/2511.21214)
### Authors
Yuhang Wang,Yanxu Zhu,Dongyuan Lu,Jitao Sang
### Background
推理模型在复杂推理任务中展现了出色的能力，但它们对对抗性工具提示的安全性保障仍面临重大挑战。由于这些工具提示具有隐蔽性和欺骗性，它们可以规避内置的安全机制，导致生成有害内容。这强调了需要一种适应性和自适应性的安全对齐方法，使模型能够自主增强其防御能力以应对对抗性输入。
### Innovation
该论文提出了合成准则基于的自适应安全对齐（SGASA）框架。SGASA框架通过生成安全准则和增强提示来增强模型抵御有害对抗性提示的能力，同时减少对良性请求的不必要的拒绝。此外，SGASA框架包含两个关键阶段：数据预合成和对齐微调。
### Conclusion
全面的实验结果表明，SGASA显著提高了模型的安全性，验证了其适应性和可扩展的有效性。
## 119. `cs.AI` - 逐片进步：用于自回归图像生成的测试时缩放 [PDF](https://arxiv.org/pdf/2511.21185), [HTML](https://arxiv.org/abs/2511.21185)
### Authors
Joonhyung Park,Hyeongwon Jang,Joowon Kim,Eunho Yang
### Background
最近的研究表明，视觉自回归（AR）模型在文本到图像生成方面展现了很有前景的能力，其方式类似于大型语言模型。然而，尽管测试时计算缩放策略为推理增强的输出带来了显著成功，特别是在应对复杂自然语言任务时，但这些策略尚未经探索应用于视觉AR模型，并对其提出了独特的挑战。直接应用诸如Best-of-N这样的测试时缩放策略可能并不理想：这会在错误的生成轨迹上消耗完整的计算量，而逐扫解码方案缺乏整个画布的蓝图，限制了其扩展优势，只能生成少量与提示对齐的候选方案。
### Innovation
本文提出了GridAR，一种测试时缩放框架，旨在从视觉AR模型中获得最佳结果。GridAR采用格子分区渐进生成方案，在画布上为同一位置生成多个候选方案，过早修剪不可行的候选方案，并将可行的候选方案作为固定锚点来引导后续解码。联合使用此方法，我们提出了一个基于布局的提示重述策略，利用部分视图来推断满足提示的可行布局。重述后的提示随后指导随后的图像生成，以减轻蓝图不足的问题。通过这些方法，GridAR在有限的测试时缩放条件下实现了更高的质量：使用N=4时，即使在T2I-CompBench++上超越了Best-of-N (N=8) 14.4%的性能，同时降低成本25.6%。此外，它也适用于自回归图像编辑，在PIE-Bench上的语义保留方面比更大的N基线模型提高了13.9%。
### Conclusion
GridAR实现了在有限测试时缩放下更高的图像生成质量：使用N=4时，它甚至比N=8的Best-of-N在T2I-CompBench++上高出14.4%的性能，同时降低了25.6%的成本。此外，它还展示了在自回归图像编辑中的适用性，在PIE-Bench上的语义保存方面比更大的N基线模型提高了13.9%。
## 120. `cs.AI` - LLaVA-UHD v3: 渐进式视觉压缩技术在多模态大语言模型中的高效原生分辨率编码 [PDF](https://arxiv.org/pdf/2511.21150), [HTML](https://arxiv.org/abs/2511.21150)
### Authors
Shichu Sun,Yichen Zhang,Haolin Song,Zonghao Guo,Chi Chen,Yidan Zhang,Yuan Yao,Zhiyuan Liu,Maosong Sun
### Background
多模态大语言模型（MLLMs）的标准架构范式已经演变成视觉编码接着词元凝缩。最近的研究倾向于使用全局原生分辨率视觉编码，而不是切片方法。研究人员通过系统比较这些模型在视觉-语言理解及注意力机制的表现，发现全球编码增强了一般能力但增加了计算开销。
### Innovation
提出了一种名为渐进式视觉压缩（PVC）的方法，旨在为标准Vision Transformer (ViT)提供高效原生分辨率编码。PVC方法包含两个关键模块：改进的子块嵌入和分层部署的窗口化词元压缩，以逐步聚合局部词元表示，这可以在大语言模型架构中高效重配置ViT，同时大量保留通用能力，逐步降低时间到第一词元（TTFT）。
### Conclusion
通过广泛基准测试表明，改进后的ViT (ViT-UHD) 在性能上与MoonViT相当，而将TTFT降低了2.4倍。基于ViT-UHD，LLaVA-UHD v3也实现了与Qwen2-VL相当的结果，进一步将TTFT降低1.9倍。作者将提供所有代码和检查点，以支持未来在高效MLLMs方面的研究。
## 121. `cs.AI` - 哪一层导致了分布偏差？熵引导自适应剪枝方法在扩散和流型模型中的应用 [PDF](https://arxiv.org/pdf/2511.21122), [HTML](https://arxiv.org/abs/2511.21122)
### Authors
Changlin Li,Jiawei Zhang,Zeyi Shi,Zongxin Yang,Zhihui Li,Xiaojun Chang
### Background
大规模的视觉生成模型，包括扩散模型和流型模型，在视觉生成任务中表现出色。然而，将这些预训练模型转移到下游任务时往往会带来大量参数冗余。先前的研究多采用一次性剪枝方法，这种方法可能会导致模式崩溃，并且可能无法保留模型性能。
### Innovation
提出了EntropyGuided Automatic Progressive Pruning框架（EntPruner），这是一种针对扩散和流型模型的熵引导自适应剪枝方法。该框架包含两部分创新：1）熵引导剪枝策略，这是一种模块级别的关键性评估策略，特别适用于生成模型；2）零样本自适应剪枝框架，在训练过程中自动确定剪枝时机和力度，避免一次性剪枝的缺点，减少模式崩溃问题并保持模型性能。
### Conclusion
大量实验表明，EntPruner在DiT和SiT模型上具有有效性，与ImageNet和其他三个下游数据集相比，实现了高达2.22倍的推理速度提升，同时保持了相当的生成质量。
## 122. `cs.AI` - Maglev-Pentabot: 磁悬浮系统在深度强化学习辅助下的非接触操控 [PDF](https://arxiv.org/pdf/2511.21149), [HTML](https://arxiv.org/abs/2511.21149)
### Authors
Guoming Huang,Qingyi Zhou,Dianjing Liu,Shuai Zhang,Ming Zhou,Zongfu Yu
### Background
非接触操控在各工业领域中正逐渐成为变革性的技术，但现有的柔性2D和3D非接触操控技术通常局限于微米级尺度，主要控制毫克级的物体。本文调研了非接触操控技术在规模化以及控制大质量物体上的局限。
### Innovation
提出了一种名为Maglev-Pentabot的磁悬浮系统，利用深度强化学习（DRL）开发复杂控制策略以操控克级物体。该系统通过数值分析优化了电磁铁布局以最大化可控空间，并引入了动作重映射方法来解决由于磁场强度的强非线性导致的样本稀疏性问题，使DRL控制器能够收敛。此外，该系统还能够将操控方法扩展到更重的物体。
### Conclusion
实验结果显示Maglev-Pentabot具有灵活的操作能力，并且能够泛化到未被明确训练的任务。同时，该方法可以扩展以操控更重的物体，为工业规模的机器人应用提供参考框架。
## 123. `cs.AI` - 使用时间碰撞指标改进切入机动中的碰撞避免 [PDF](https://arxiv.org/pdf/2511.21280), [HTML](https://arxiv.org/abs/2511.21280)
### Authors
Jamal Raiyn
### Background
本文讨论了一种新的碰撞规避策略，特别关注自主车辆（AVs）在处理切入场景（cut-in scenarios）时面临的挑战。传统的碰撞规避方法主要依赖于时间到碰撞（Time-to-Collision, TTC）计算，但在实际应用中往往不够精准和有效。
### Innovation
本文提出了一种结合深度学习与TTC计算的新方法，用于预测潜在碰撞并确定合适的避险措施。相较于传统的方法，该系统能更准确地进行碰撞预测和采取回避措施。
### Conclusion
该研究提出的方法通过将深度学习与TTC计算相结合，显著提高了自主车辆在复杂切入场景中的碰撞规避能力。
## 124. `cs.AI` - CAHS-Attack：基于CLIP的启发式搜索攻击方法 [PDF](https://arxiv.org/pdf/2511.21180), [HTML](https://arxiv.org/abs/2511.21180)
### Authors
Shuhan Xia,Jing Dai,Hui Ouyang,Yadong Shang,Dongxiao Zhao,Peipei Li
### Background
扩散模型在面对对抗性提示时表现出显著的脆弱性，因此增强攻击能力对于揭示这些漏洞并构建更加 robust的生成系统至关重要。现有的工作通常依赖于对模型梯度的白盒访问或手工提示工程，但在实际部署中由于访问受限或攻击效果差等原因，这些方法难以实现。针对这一问题，文中讨论了扩散模型尤其是 Stable Diffusion 模型的脆弱性，并将其归因于基于CLIP的文本编码器内部存在的固有漏洞。
### Innovation
文中提出了一种名为CAHS-Attack的CLIP-Aware启发式搜索攻击方法，该方法结合了蒙特卡洛树搜索（MCTS）进行细粒度的后缀优化，利用约束遗传算法预先选择有高潜力的对抗性提示作为根节点，并在每次仿真滚动中保留具有最大语义破坏性的结果，以实现高效的地方搜索。实验结果表明，该方法在长短及不同语义的提示上都达到了最先进的攻击性能。
### Conclusion
实验表明CAHS-Attack在扩散模型，尤其是Stable Diffusion模型上的攻击效果显著，同时揭示了模型的脆弱性来源于基于CLIP的文本编码器内部的固有漏洞，强调了当前文本到图像管道中存在根本性的安全风险。
## 125. `cs.AI` - Spiking Neural Networks中的联邦学习中的隐私性 [PDF](https://arxiv.org/pdf/2511.21181), [HTML](https://arxiv.org/abs/2511.21181)
### Authors
Dogukan Aksu,Jesus Martinez del Rincon,Ihsen Alouani
### Background
研究表明，突触神经网络（SNNs）由于其固有的低能耗特性，成为嵌入式和边缘AI的有潜力候选者。与传统神经网络（ANNs）相比，它们在能源预算严格受限的场景中更加高效。与此同时，联邦学习（FL）已成为此类设置中的主流训练范式，可在设备端学习的同时限制原始数据的暴露。然而，梯度倒置攻击是FL中的一个关键隐私威胁，因为敏感的训练数据可以直接从共享的梯度中重建。尽管已在传统ANNs中广泛研究了这一漏洞，但在SNNs中的影响仍鲜有探讨。
### Innovation
本文首次对SNNs中的梯度泄漏进行了全面的经验研究，涵盖了不同的数据领域。假设由于SNNs使用代理梯度进行训练，代理梯度与原始输入的相关性较低，从隐私角度来看，信息量较少。通过将不同的梯度泄漏攻击适应到突触域中，实验结果表明，与传统ANNs中可靠地揭示重要输入内容的梯度不同，SNNs的梯度产生嘈杂、时间不一致的重构，无法恢复有意义的空间或时间结构。这些结果表明，事件驱动的动力学和代理梯度训练的结合大大减少了梯度信息量。
### Conclusion
据我们所知，这是首次对该SNN架构进行梯度倒置攻击的系统基准测试，凸显了神经形态计算的内在隐私保护潜力。
## 126. `cs.AI` - TALES：LLM生成故事中文化表现的分类与分析 [PDF](https://arxiv.org/pdf/2511.21322), [HTML](https://arxiv.org/abs/2511.21322)
### Authors
Kirti Bhagat,Shaily Bhatt,Athul Velagapudi,Aditya Vashistha,Shachi Dave,Danish Pruthi
### Background
全球有数百万人使用AI聊天机器人来满足其创意需求，这引起了对如何通过这些聊天机器人代表不同文化的广泛兴趣。然而，在开放式任务中评价文化表现仍然具有挑战性且研究不足。本文旨在评估语言生成模型（LLM）生成的故事中多元印度文化身份的文化误述。
### Innovation
本文开发了TALES-Tax，一种文化误述分类法，并通过大规模注释研究评估了6个模型。研究发现，生成的故事中有88%包含文化错误，更多出现在中低资源语言及印度郊区地区的故事。此外，TALES项目还生成了一个独立的问题银行，以评估基础模型的文化知识。
### Conclusion
虽然生成的故事充满文化误述，但模型往往在文化知识方面表现良好。这项评估有助于开发更准确地反映文化多样性的AI系统。
## 127. `cs.AI` - BotaCLIP: 对地球观测数据具有植物学意识的对比学习 [PDF](https://arxiv.org/pdf/2511.21194), [HTML](https://arxiv.org/abs/2511.21194)
### Authors
Selene Cerna,Sara Si-Moussi,Wilfried Thuiller,Hadrien Hendrikx,Vincent Miele
### Background
基础模型在图像、文本和音频等多种模态数据中展示了强大的学习能力，可以从中学习到具有转移性的丰富表示，这些表示在现代机器学习管道中通常替代原始数据作为下游任务的主要输入。但在现实应用中，往往需要将基础模型适应特定领域知识，而不需从头开始重新训练或增加大量的计算成本。
### Innovation
提出了BotaCLIP，一种轻量级的多模态对比学习框架，通过将高分辨率的航空影像与植物图谱对齐，来适应预训练的地球观测基础模型（DOFA）。BotaCLIP通过对比学习结合正则化策略来防止灾难性遗忘，从而内存高效地内部化生态结构。研究结果表明，与DOFA和监督基线相比，使用BotaCLIP提取的表示在三种生态任务（植物存在预测、蝴蝶分布建模和土壤营养群丰度估计）上均有持续的改进。
### Conclusion
这项工作展示了如何通过领域意识的基础模型适应，在数据稀缺的情况下注入专家知识，从而实现简约的学习表示。
## 128. `cs.AI` - SurgMLLMBench: 外科场景理解的多模态大型语言模型基准数据集 [PDF](https://arxiv.org/pdf/2511.21339), [HTML](https://arxiv.org/abs/2511.21339)
### Authors
Tae-Min Choi,Tae Kyeong Jeong,Garam Kim,Jaemin Lee,Yeongyoon Koh,In Cheul Choi,Jae-Ho Chung,Jong Woong Park,Juyoun Park
### Background
近年来，多模态大型语言模型（LLMs）在医疗和手术领域的潜力已得到突出显示。然而，现有的手术数据集主要采用视觉问答（VQA）格式，具有不同的分类体系，且缺乏像素级分割支持，这限制了其一致性和应用范围。
### Innovation
我们提出了SurgMLLMBench，一个专门用于开发和评估交互式多模态LLMs的统一多模态基准，包括新收集的微外科人工血管吻合（MAVIS）数据集。该基准集集成了像素级仪器分割掩码和结构化VQA注释，涵盖了腹腔镜、机器人辅助和显微外科领域，并采用统一的分类体系，超过了传统的VQA任务，提供了更丰富的视觉对话交互。
### Conclusion
广泛的基线实验表明，训练于SurgMLLMBench上的单个模型在各个领域中能保持一致性能，并有效地适应未见数据集。SurgMLLMBench将作为一个坚固的资源，促进多模态外科AI研究，并支持可重复的评估和交互外科推理模型的开发。
## 129. `cs.AI` - SONAR: 频谱对比音频残差在泛化Deepfake检测中的应用 [PDF](https://arxiv.org/pdf/2511.21325), [HTML](https://arxiv.org/abs/2511.21325)
### Authors
Ido Nitzan HIdekel,Gal lifshitz,Khen Cohen,Dan Raviv
### Background
当前的Deepfake（DF）音频检测器在处理未见过的数据输入时仍存在泛化能力不足的问题。这一问题的原因主要是频谱偏见，神经网络倾向于优先学习低频结构而忽略高频细节，这导致了Deepfake生成器在高频部分存在残差，而现有的检测器未能充分利用这些高频残差。因此，为了克服这一局限，研究者提出了一种名为Spectral-cONtrastive Audio Residuals（SONAR）的频谱引导框架。
### Innovation
SONAR框架通过明确地将音频信号解构为互补表示来解决这一问题。XLSR编码器捕捉音频中的主要低频成分，同时通过可学习的SRM和价值约束的高通滤波器转发路径提炼出微弱的高频残差。频谱交叉注意力机制则重新结合这两种视图，以捕捉长距离和短距离的频谱依赖性。同时，频率感知的Jensen-Shannon对比损失机制将真实的内容噪声对拉在一起，而将假内容的嵌入推离，从而加速优化过程，细化决策边界。该模型在ASVspoof 2021和野外基准测试中取得了当前最先进的性能，并且比强基线模型快四倍。
### Conclusion
总之，SONAR通过提升微弱的高频残差为首要学习信号，揭示了一种完全数据驱动的、频谱引导的对比框架，该框架将潜在空间划分为两个分离的流形：自然高频和受污染高频，从而细化决策边界。由于方案仅在表示级别上操作，因此它是架构无关的，并在未来工作中可以无缝集成到任何模型中，其中微妙的高频线索是决定性的。
## 130. `cs.AI` - The More, the Merrier: Contrastive Fusion for Higher-Order Multimodal Alignment [PDF](https://arxiv.org/pdf/2511.21331), [HTML](https://arxiv.org/abs/2511.21331)
### Authors
Stefanos Koutoupis,Michaela Areti Zervou,Konstantinos Kontras,Maarten De Vos,Panagiotis Tsakalides,Grigorios Tsagatakis
### Background
多模态机器学习领域的一个重要挑战是联合表示多个模态。当前主流方法主要在成对设置中运行，一次对齐两个模态。尽管一些最近的方法试图捕捉多个模态之间的高阶交互作用，但它们往往忽视或未能充分保持成对关系，限制了其在单一模态任务上的效果。
### Innovation
本文提出了一种名为Contrastive Fusion (ConFu)的框架，它将单一模态和它们的融合组合同时嵌入到一个统一的表示空间中，使模态和它们的融合版本对齐。ConFu在传统的成对对比目标中引入了一个额外的融合模态对比项，鼓励将同一个模态的成对嵌入物与另一个模态混合。这一形式能够捕捉仅通过成对对齐无法恢复的高阶依赖关系，如排他关系，同时仍然保持强大的成对对应关系。
### Conclusion
我们通过对合成和实际多模态基准的评估，验证了ConFu在跨模态互补性利用、高阶依赖关系捕捉以及适应日益复杂的多模态交互等方面的优势。在各种场景中，ConFu在检索和分类任务上的性能表现出竞争力，并在一个对比框架内支持统一的一对一和一对二检索。
## 131. `cs.AI` - 定向预测变化 - 效率和值得信赖的局部特征归因方法忠实性评估 [PDF](https://arxiv.org/pdf/2511.21363), [HTML](https://arxiv.org/abs/2511.21363)
### Authors
Kevin Iselborn,David Dembinsky,Adriano Lucieri,Andreas Dengel
### Background
解释方法的有效性关键在于其对底层机器学习模型的准确性。特别是在高风险的医疗环境中，医护人员和监管者需要与模型决策过程准确对应的解释。现有的忠实度度量（如Infidelity）依赖于蒙特卡洛近似，需要大量模型评估，并因随机抽样引入不确定性。
### Innovation
提出了一种新的度量方法——定向预测变化（DPC），通过修改现有的预测变化（PC）度量并在指导扰动实验中融入扰动和归因的方向，DPC实现了近十倍的加速，并消除了随机性，提供了一种确定性且可信赖的评估过程，测量与局部Infidelity相同的特性。
### Conclusion
DPC在两个数据集（皮肤病变图像和财务表格数据）、两种黑盒模型和七种解释算法上进行了评估，覆盖广泛的超参数，结果显示DPC与PC一起，可以提供一个全面且计算效率高的评估，同时保证结果的确定性和可重复性。
## 132. `cs.AI` - Hybrid-AIRL: 改进的对抗逆强化学习与监督专家指导 [PDF](https://arxiv.org/pdf/2511.21356), [HTML](https://arxiv.org/abs/2511.21356)
### Authors
Bram Silue,Santiago Amaya-Corredor,Patrick Mannion,Lander Willem,Pieter Libin
### Background
对抗逆强化学习（AIRL）在处理强化学习（RL）中的稀疏奖励问题方面显示出潜力，通过从专家演示中推断密集的奖励函数。然而，它在高度复杂、不完全信息的情况下的表现仍然没有得到充分探索。为了填补这一空白，我们评估了AIRL在 Heads-Up Limit Hold'em（HULHE）扑克环境中的应用，这种环境具有稀疏且延迟的奖励以及显著的不确定性。在这个环境中，我们发现AIRL难以推断出足够有信息量的奖励函数。
### Innovation
我们提出了Hybrid-AIRL（H-AIRL），这是一种扩展了奖励推断和策略学习的方法，通过结合来自专家数据的监督损失和随机正则化机制。我们对精心选择的Gymnasium基准环境和HULHE扑克环境进行了H-AIRL的评估，并通过可视化学习到的奖励函数获取了更深入的见解。实验结果表明，与AIRL相比，H-AIRL具有更高的样本效率和更稳定的训练。
### Conclusion
我们的实验结果表明H-AIRL在具有挑战性的实际环境中表现出更优的样本效率和更稳定的训练。这突显了将监督信号纳入逆强化学习的好处，并将H-AIRL确立为解决复杂真实环境问题的有前途的框架。
## 133. `cs.AI` - 测试时计算量对推理视觉语言模型的逆缩放现象：基于干扰项的实证分析 [PDF](https://arxiv.org/pdf/2511.21397), [HTML](https://arxiv.org/abs/2511.21397)
### Authors
Jiyun Bae,Hyunjong Ok,Sangwoo Mo,Jaeho Lee
### Background
先前关于语言模型的研究发现，文本干扰项会导致推理时间延长但效果减弱，表现出相反的缩放效应（即，文本干扰对推理时间增加但有效性降低）。作者旨在探讨在多模态设置中是否也会发生相似的现象。
### Innovation
作者引入了一个名为Idis的数据集，系统地改变了图像问答任务中的干扰项，分别在语义、数值和空间维度上进行，以研究视觉干扰项与文本干扰项的不同影响。研究发现，尽管仍然存在相反的缩放效应，但由于干扰项的存在，增加了时间和精度之间的矛盾，推理的时间增加但准确性反而下降。该研究通过追踪推理链中的属性计数，揭示了干扰项、推理时间和准确性之间的相互作用。
### Conclusion
作者发现，这些趋势不仅扩展到了视觉偏差基准，如Waterbirds，还提出了一种简单的提示策略来减轻推理模型中由偏差驱动的预测。
## 134. `cs.AI` - 主观深度和时间尺度变换器：学习在何处何时进行计算 [PDF](https://arxiv.org/pdf/2511.21408), [HTML](https://arxiv.org/abs/2511.21408)
### Authors
Frederico Wieser,Martin Benfeghoul,Haitham Bou Ammar,Jun Wang,Zafeirios Fountas
### Background
标准的Transformer架构在计算分配上是刚性和统一的，这限制了它们的效率和可扩展性，特别是在大规模模型和长序列上。这一局限性导致了计算资源的浪费和模型性能的瓶颈。
### Innovation
作者提出了两种新的Transformer架构——Subjective Depth Transformers（SDT）和Subjective Timescale Transformers（STT），这两种架构利用贝叶斯惊奇信号动态路由计算，学习在解码器中何时何处进行计算。SDT通过交替的决策层和动态层实现，而STT则在时间域上扩展了条件计算，形成了基于时间变化的变换器块动态执行或跳过机制。
### Conclusion
这两些建构提议了一种灵活性较高的框架，能够通过跳过自注意力计算和减半KV缓存需求来提高效率，初步探索了条件计算下的计算-精度权衡。
## 135. `cs.AI` - 高效检测交通控制系统中异常现象的混合SIFT-SNN [PDF](https://arxiv.org/pdf/2511.21337), [HTML](https://arxiv.org/abs/2511.21337)
### Authors
Munish Rathee(School of Engineering, Computer and Mathematical Science (of Auckland University of Technology) Auckland, New Zealand),Boris Bačić(School of Engineering, Computer and Mathematical Science (of Auckland University of Technology) Institute of Biomedical Technologies (IBTec) Auckland, New Zealand),Maryam Doborjeh(Knowledge Engineering and Discovery Research Institute (KEDRI) (of Auckland University of Technology) Auckland, New Zealand)
### Background
该论文提出了SIFT-SNN框架，这是一种低延时的类脑信号处理流水线，用于实时检测运输基础设施中的结构性异常。背景信息指出，传统的基于CNN的方法虽然有效，但也存在一些局限性，如不保留空间特征、降低解释性、难以在嵌入式硬件上高效运行等。
### Innovation
创新点在于结合Scale-Invariant Feature Transform（SIFT）用于空间特征编码，与基于延迟驱动的尖峰转换层和Leaky Integrate-and-Fire（LIF）突触神经网络（SNN）分类相结合，形成了一种混合的方法。该框架在特定数据集上的分类准确率为92.3%（±0.8%），每帧的推断时间为9.5毫秒，实现了亚10毫秒的低延时，并具备稀疏尖峰激活（8.1%），适合实时、低功耗边缘部署。相比于基于CNN的方法，它更显式地保存了空间特征，增强了可解释性，支持透明决策，且能够在嵌入式硬件上高效运行。
### Conclusion
结论表明，SIFT-SNN框架作为一种混合方法，通过实验证明了在交通控制系统中检测结构性异常的有效性和实用性，并且可以应用于全球超过20个城市的可移动混凝土屏障。尽管合成增强提高了稳健性，但其在未知现场条件下的泛化能力仍需进一步验证。该研究为交通运输基础设施的安全监控提供了一个可推广的案例研究。
## 136. `cs.AI` - 使用条件生成模型生成分离的演唱人声 [PDF](https://arxiv.org/pdf/2511.21342), [HTML](https://arxiv.org/abs/2511.21342)
### Authors
Genís Plaja-Roglans,Yun-Ning Hung,Xavier Serra,Igor Pereira
### Background
音乐分析和实践中，分离音乐混合体中的个体元素是一个基本过程。现有方法通常使用优化的神经网络来掩蔽或转换混合的时间-频率表示以提取目标源。然而，生成扩散模型的灵活性和泛化能力正在为这一复杂任务提出新的解决方案。
### Innovation
本文介绍了一种使用有条件生成模型进行真人音乐录音中演唱人声分离的方法。该模型经过训练，可以在给定混合物对应条件下生成独奏人声。相较于先前的生成系统和非生成基准模型，该方法在训练过程中使用补充数据时，能取得相当的竞争性客观评分。生成扩散的迭代特性使用户能够调整质量效率的权衡，并在必要时改进输出。
### Conclusion
通过对采样算法的消融研究，突显了用户可配置参数的影响。此方法提供了一个灵活的解决方案，能够根据需求精细调整分离的演唱人声质量。
## 137. `cs.AI` - HPC基础设施上自动动态AI推断扩展：结合Kubernetes、Slurm和vLLM [PDF](https://arxiv.org/pdf/2511.21413), [HTML](https://arxiv.org/abs/2511.21413)
### Authors
Tim Trappen,Robert Keßler,Roland Pabel,Viktor Achter,Stefan Wesner
### Background
由于AI推理需求的增加，特别是在高等教育领域，新的解决方案正在利用现有的基础设施出现。高性能计算（HPC）已经成为实施此类解决方案的常见方法。然而，传统的HPC操作模型不适应同步、面向用户的动态AI应用工作负载的需求。
### Innovation
本文提出了一种解决方案，通过在超级计算机RAMSES上集成vLLM、Slurm和Kubernetes来服务大型语言模型（LLMs）。初步基准测试表明，所提出的架构能够高效地扩展到100、500和1000个并发请求，端到端延迟的额外开销仅为约500毫秒。
### Conclusion
所提出的架构能够有效地支持大型语言模型的并发请求，验证了该方法在实际应用场景中的可行性。
## 138. `cs.AI` - RIA: 优化的列表CTR预测的一项排名融合方法 [PDF](https://arxiv.org/pdf/2511.21394), [HTML](https://arxiv.org/abs/2511.21394)
### Authors
Guoxiao Zhang,Tan Qu,Ao Li,DongLin Ni,Qianlong Xie,Xingxing Wang
### Background
现有的排序重新评分方法往往将排序和重新评分分开，导致模型在严格的延迟约束下变得脆弱，具备组合稀疏性和有限的表示能力。这种分离限制了模型的列表级评估能力。
### Innovation
本文提出了RIA（排名融合架构），这是一种统一的端到端框架，它无缝地将点级和列表级评估融为一体。RIA引入了四个核心组件：用户和候选品对偶变压器（UCDT）、上下文感知用户历史和目标（CUHT）模块、层次列表多HSTU（LMH）模块以及嵌入缓存（EC）模块，以捕捉层次项依赖关系并提高推理效率。
### Conclusion
广泛的实验表明，RIA在公共和工业数据集上都优于最先进的模型，显著提升了AUC和LogLoss。部署在美团广告系统中，RIA在在线A/B测试中实现了点击率（CTR）提高1.69%以及每千次成本（CPM）增加4.54%的效果。
## 139. `cs.AI` - SAM Guided Semantic and Motion Changed Region Mining for Remote Sensing Change Captioning [PDF](https://arxiv.org/pdf/2511.21420), [HTML](https://arxiv.org/abs/2511.21420)
### Authors
Futian Wang,Mengqi Wang,Xiao Wang,Haowen Wang,Jin Tang
### Background
遥感变化描述是一项新兴且流行的研究任务，旨在用自然语言描述在两次不同时间拍摄的遥感图像之间所发生的变化。现有的方法通常使用CNN/Transformer从给定的图像中提取视觉特征或将辅助任务融入以提升最终结果，但这些方法存在区域意识较弱和时间对齐有限的问题。
### Innovation
本文探索了使用SAM（通用对象检测模型）基础模型来提取区域级表示，并将感兴趣区域的知识注入到描述框架中。具体来说，作者使用CNN/Transformer模型提取全局视觉特征，利用SAM基础模型划分语义和运动层面的变化区域，并借助特殊构建的知识图谱提供有关感兴趣对象的信息。这些异质信息通过交叉注意力机制融合，并使用Transformer解码器生成最终的自然语言变化描述。
### Conclusion
本文方法在多个广泛使用的基准数据集上取得了最先进的性能。详细的实验结果表明，该方法在变化描述方面具有优越性。相关源代码将在 https://github.com/tianluyuyu/onelake_codes 中发布。
## 140. `cs.AI` - 受污染训练数据中具有自适应和激进排斥的异常检测 [PDF](https://arxiv.org/pdf/2511.21378), [HTML](https://arxiv.org/abs/2511.21378)
### Authors
Jungi Lee,Jungkwon Kim,Chi Zhang,Kwangsun Yoo,Seok-Joo Byun
### Background
在异常检测中，处理受污染的数据是一个关键挑战。传统的模型假设数据集中的训练数据都是纯正的。常规方法通过依赖固定的比例来减轻污染的影响，但在假设比例与实际比例之间存在差异的情况下，这种固定的处理方式会导致性能严重下降，特别是在噪声环境中，正常和异常数据分布重叠时更为明显。
### Innovation
我们提出了自适应和激进排斥（AAR）方法，这是一种新的方法，能够动态排除异常值并结合了硬性与软性拒绝策略。AAR 使用修改的 z 分数和基于高斯混合模型的阈值来优化保持正常数据和排除异常值之间的平衡。
### Conclusion
在两个图像数据集和三十个表格数据集上的广泛实验表明，AAR 的表现优于最先进的方法，AUCROC 提升了 0.041。通过提供一种可扩展且可靠的方法，AAR 增强了对受污染数据集的鲁棒性，这为更广泛的现实世界应用开启了路径，尤其是在安全和医疗领域。
## 141. `cs.AI` - FITRep: 通过MLLMs的注意力指导项表示 [PDF](https://arxiv.org/pdf/2511.21389), [HTML](https://arxiv.org/abs/2511.21389)
### Authors
Guoxiao Zhang,Ao Li,Tan Qu,Qianlong Xie,Xingxing Wang
### Background
在线平台通常会因为近似重复项（视觉和文本相似）而导致用户体验下降。现有方法在处理多模态嵌入时，将表示作为黑盒处理，忽略了结构关系（例如主元素和辅助元素的关系），导致局部结构坍塌问题。
### Innovation
本文受到特征整合理论(FIT)的启发，提出了一种基于注意力的、透明的项目表示框架FITRep，用于精细化的商品去重。FITRep包含三个部分：(1) 概念层次信息提取(CHIE)，利用MLLMs提取层次语义概念；(2) 结构保持降维(SPDR)，一种基于UMAP的自适应方法，用于高效的信息压缩；(3) FAISS基聚类(FBC)，一种使用FAISS为每个项目分配唯一聚类ID的基于FAISS的聚类方法。
### Conclusion
FITRep 在面市的广告系统中进行在线A/B测试，实现了点击率(CTR)和每千次展示成本(CPM)分别提升了3.60%和4.25%，证明了其有效性和实际影响。
## 142. `cs.AI` - 当机器人遵循标记：视觉-语言-行动模型上的通用可移植标记攻击 [PDF](https://arxiv.org/pdf/2511.21192), [HTML](https://arxiv.org/abs/2511.21192)
### Authors
Hui Lu,Yi Yu,Yiming Yang,Chenyu Yi,Qixin Zhang,Bingquan Shen,Alex C. Kot,Xudong Jiang
### Background
Vision-Language-Action (VLA) 模型在对抗攻击面前较为脆弱，但目前尚未充分探索适用于未知架构、微调变体和从模拟到现实转变的泛化和可移植攻击。大多数现有的防御措施都针对单一模型进行过拟合，在黑盒设置中效果不佳。
### Innovation
本文提出了一种名为UPA-RFAS（通用贴图攻击通过稳健特征、注意力和语义的统一框架），该框架在共享特征空间中学习一个单一的实际贴图，同时促进跨模型的迁移。UPA-RFAS结合了具有$L_1$偏差先验和排斥InfoNCE损失的特征空间目标，以产生迁移的表示变化；具有增强鲁棒性的两阶段最小-最大程序，内循环学习不可见的样本级扰动，外循环优化针对这些强化邻域的通用贴图；以及两种针对VLA的特定损失：用于劫持文本到视觉注意力的贴图注意力主导和诱导图像-文本不匹配的贴图语义对齐。
### Conclusion
在多种VLA模型、操作套件和物理执行中进行的实验表明，UPA-RFAS可以一致地在网络、任务和视角之间进行迁移，揭示了一种实用的基于标记的攻击表面，并为未来的防御提供了强有力的基础。
## 143. `cs.AI` - Monet：超越图像和语言的潜在视觉空间推理 [PDF](https://arxiv.org/pdf/2511.21395), [HTML](https://arxiv.org/abs/2511.21395)
### Authors
Qixun Wang,Yang Shi,Yifei Wang,Yuanxing Zhang,Pengfei Wan,Kun Gai,Xianghua Ying,Yisen Wang
### Background
现有的基于图像的视觉推理方法已经能够增强视觉推理的能力，但它们通常依赖于外部工具或固定的数据集。这些方法还有很多不足之处，尤其是在灵活性和抽象视觉思考能力上。本研究提出了一种名为Monet的训练框架，旨在让多模态大型语言模型（MLLMs）能够在潜在的视觉空间中直接推理，通过生成连续的嵌入来表示中间视觉想法，从而进行直接的潜在视觉推理。
### Innovation
1. 引入Monet训练框架，让大型多模态语言模型在潜在视觉空间中直接生成并利用视觉嵌入进行推理。2. 提出了基于三阶段蒸馏监督微调（SFT）的训练策略，解决潜在视觉空间推理中的高计算成本和嵌入监督不足的问题。3. 设计了VLPO（视觉-潜在策略优化）方法，以更有效的增强潜在视觉推理。4. 构建了Monet-SFT-125K数据集，为潜在视觉推理提供高质量的文本-图像交织的CoT数据。
### Conclusion
模型Monet-7B在现实世界感知和推理基准测试中表现稳定，并在复杂的抽象视觉推理任务中展示了强大的泛化能力。此外，研究还分析了每个训练组件的作用，并基于早期尝试提供了未来发展的见解。
## 144. `cs.AI` - 训练内省行为：微调诱导7B模型可靠的内部状态检测 [PDF](https://arxiv.org/pdf/2511.21399), [HTML](https://arxiv.org/abs/2511.21399)
### Authors
Joshua Fonseca Rivera
### Background
Lindsey (2025) 通过四项实验探讨了语言模型的内省意识，发现模型可以检测和识别注入的激活模式，但成功率较低（最佳模型约20%的成功率）。作者专注于第一个实验——自我报告注入的“想法”，并提出是否可以通过直接训练来获得这一能力，而无需等待其自发出现。通过对单一标记的短暂注入进行微调，作者将一个7B参数的模型从几乎完全失败的状态（准确率为0.4%，假阳性率为6.7%）转变为可靠的检测表现（在验证概念上的准确率为85%，假阳性率为0%）。
### Innovation
研究通过微调单一标记短暂注入的方法，显著提高了模型对短暂‘想法’的检测准确率，并使其能够在后续生成步骤中保留和报告语义信息。此训练方法满足Lindsey提出的三条内省标准：准确性（正确的识别）、根基性（0/60假阳性）和内在性（检测先于语言化）。结果表明模型具有泛化能力，且能够学习可转移的技能，但仍未能证明其在Lindsey意义上具有元认知的表示。
### Conclusion
研究回答了Lindsey提出的开放问题：是否通过训练可以减少模型间差异。结果显示至少可以诱导一种内省行为的直接表现，为内置AI透明度提供了一条途径。
## 145. `cs.AI` - 长文档可读性评估的分层排序神经网络 [PDF](https://arxiv.org/pdf/2511.21473), [HTML](https://arxiv.org/abs/2511.21473)
### Authors
Yurui Zheng,Yijun Chen,Shaohong Zhang
### Background
当前，虽然深度学习技术已在可读性评估中逐步应用，但大多数方法未能充分考虑文本的长度或可读性标签间的序关系。因此，本文提出了一种双向可读性评估机制，能够捕捉上下文信息，识别文本中富含语义信息的区域，对单句可读性进行预测。再将单句级别的标签用于预测文档总体的可读性水平。此外，本文还引入了一种成对排序算法，通过标签相减的方式建模可读性标签间的序关系。
### Innovation
提出了一个双向可读性评估机制，能够识别文本中的语义丰富区域，并捕捉上下文信息，进而预测单句的可读性水平。通过使用单句级别的标签来辅助预测文档的整体可读性水平。同时，还提出了一种成对排序算法，通过标签相减的方式，建模可读性水平间的序关系。
### Conclusion
在中文和英文数据集上的实验结果表明，所提出的模型取得了竞争力的性能，并优于其他基准模型。
## 146. `cs.AI` - 高效视觉变换器的频率感知 token 减少策略 [PDF](https://arxiv.org/pdf/2511.21477), [HTML](https://arxiv.org/abs/2511.21477)
### Authors
Dong-Jae Lee,Jiwan Hur,Jaehyun Choi,Jaemyung Yu,Junmo Kim
### Background
视觉变换器在各种计算机视觉任务中表现出色，但与 token 长度相关的二次计算复杂性仍然是一个显著挑战。为了解决这个问题，已经广泛探索了 token 减少方法，但现有方法通常忽视了自注意力中的频率特性，如秩塌缩和过度平滑现象。
### Innovation
本文提出了一种频率感知 token 减少策略，通过将 token 分为高频率 token 和低频率 token，保留高频率 token 而聚集低频率 token 为一个紧凑的直接电流 token，以保留必要的低频率组件，在提高计算效率的同时保持性能并减轻秩塌缩。此外，还分析了先前方法的潜在频率特性和限制。
### Conclusion
通过广泛实验和分析，我们展示了该方法在提高准确性的同时减少计算开销，并减轻秩塌缩和过度平滑现象。
## 147. `cs.AI` - EvRainDrop: 通过超图引导完成进行有效框架和事件流聚合 [PDF](https://arxiv.org/pdf/2511.21439), [HTML](https://arxiv.org/abs/2511.21439)
### Authors
Futian Wang,Fan Zhang,Xiao Wang,Mengqi Wang,Dexing Huang,Jin Tang
### Background
事件摄像头生成的是空间稀疏但时间密集的异步事件流。主流的基于事件的学习算法通常将事件帧、体素或张量作为输入。尽管这些方法取得了显著的进步，但它们难以解决由空间稀疏性导致的下采样问题。
### Innovation
本文提出了一种新颖的超图引导的空间-时间事件流完成机制，该机制通过超图在不同的时间和空间位置之间连接事件标记，并利用上下文信息消息传递来完成这些稀疏事件。该方法可以在完成框架中灵活地将RGB标记作为超图节点使用，实现多模态超图信息完成。然后通过自我注意力聚合不同时间步的超图节点信息，实现多模态特征的有效学习和融合。
### Conclusion
在单标签和多标签事件分类任务上的实验充分验证了所提出框架的有效性。该论文的源代码将发布在官方网址上。
## 148. `cs.AI` - 构建与基准测试：基于文本的网络钓鱼和垃圾邮件检测的标注邮件数据集 [PDF](https://arxiv.org/pdf/2511.21448), [HTML](https://arxiv.org/abs/2511.21448)
### Authors
Rebeka Toth,Tamas Bisztray,Richard Dubniczky
### Background
网络钓鱼和垃圾邮件邮件仍然是重大网络安全威胁，攻击者越来越多地利用大型语言模型（LLMs）来制造高度具有欺骗性的内容。
### Innovation
该研究提出了一个全面的带有网络钓鱼、垃圾邮件和合法邮件的邮件数据集，明确区分了人类和LLM生成的内容。每个邮件都标注了其类别、情感诉求（如紧迫感、恐惧、权威感）以及内在动机（如点击链接、凭证窃取、金融欺诈）。研究人员对多个LLM的能力进行了基准测试，以识别这些情感和动机线索，并选择了最可靠模型对完整数据集进行标注。研究人员还通过多个LLM重新表达邮件内容以评估分类的鲁棒性，使用专家标记的真相进行最先进的LLM在原始和重新表达的邮件上的性能评估。结果显示了强大的钓鱼检测能力，但揭示了从合法邮件区分垃圾邮件的持续挑战。
### Conclusion
本研究的数据集及其评估框架有助于改善基于人工智能的邮件安全系统。为了支持开放科学研究，所有代码、模板和资源均可以在项目网站上获取。
## 149. `cs.AI` - 基于Transformer的时间序列分类机制可解释性 [PDF](https://arxiv.org/pdf/2511.21514), [HTML](https://arxiv.org/abs/2511.21514)
### Authors
Matīss Kalnāre,Sofoklis Kitharidis,Thomas Bäck,Niki van Stein
### Background
基于Transformer的模型已成为各种机器学习任务中的先进工具，包括时间序列分类，然而其复杂性使理解和解释其内部决策变得困难。现有的可解释性方法多关注输入输出属性，而忽略了内部机制的透明度。
### Innovation
本文通过将机制可解释性技术（激活修补、注意力梯度显著性、稀疏自编码器）从自然语言处理领域应用于专门设计用于时间序列分类的Transformer架构，系统地探究了每个注意力头和时间步的内部因果角色，揭示了这些模型中的因果结构。此外，本文展示了稀疏自编码器在揭示可解释的潜在特征方面的潜力。这些研究提供了Transformer可解释性方法上的贡献，并提供了关于Transformer在时间序列分类任务中功能机制的新见解。
### Conclusion
我们通过在基准时间序列数据集上的实验，构建了因果图，展示了信息在内部传播的方式，突出了驱动正确分类的关键注意力头和时间位置。
## 150. `cs.AI` - 从观察到行动：工业环境中基于潜在动作的原始动作分割方法用于VLA预训练 [PDF](https://arxiv.org/pdf/2511.21428), [HTML](https://arxiv.org/abs/2511.21428)
### Authors
Jiajie Zhang,Sören Schwertfeger,Alexander Kleiner
### Background
研究提出了一种新颖的无监督框架，用于从连续工业视频流中解锁大量未标记的人类演示数据，这些数据可以用于Vision-Language-Action（VLA）模型的预训练。现有的数据处理方法通常依赖于标记数据，而工业视频数据往往缺乏标记。该研究尝试利用无监督技术自动从未标记的数据中提取有价值的信息。
### Innovation
研究提出了一种轻量级的运动词汇化器来编码运动动态，然后使用新颖的“潜在动作能量”指标来发现和分割具有语义一致的动作基础单元，无需标记数据。这种方法能够将分割后的视频片段及其对应的潜在动作序列直接输出，为VLA的预训练提供结构化的数据。研究还展示了该方法在公共基准测试和自有的电机组装数据集上的有效性，并通过视觉-语言模型进一步验证了发现的动作基础单元的语义一致性。
### Conclusion
这项研究是第一个完全自动化的端到端系统，可以从不结构化的工业视频中提取并组织VLA预训练数据，为制造环境中将感知-行动系统集成提供了可扩展的解决方案。
## 151. `cs.AI` - 随音速前行：将神经代理模型推向高度湍流的亚音速区域 [PDF](https://arxiv.org/pdf/2511.21474), [HTML](https://arxiv.org/abs/2511.21474)
### Authors
Fabian Paischer,Leo Cotteleer,Yann Dreze,Richard Kurle,Dylan Rubini,Maurits Bleeker,Tobias Kronlachner,Johannes Brandstetter
### Background
神经代理模型在汽车空气动力学中的广泛应用，得益于数据集如DrivAerML和DrivAerNet++，主要集中在带有大涡流的钝体流场。然而，将这些方法扩展到航空航天领域，尤其是进入亚音速区域，仍然具有挑战性。这是由于可压缩流的高非线性和3D效果（如机翼尖涡）的存在。现有的航空航天数据集主要侧重于2D翼型，忽略了这些关键3D现象。因此，本文旨在填补这一空白，构建了一个针对亚音速区域3D机翼CFD模拟的新数据集。
### Innovation
本文创新地构建了一个针对亚音速区域3D机翼CFD模拟的新数据集，涵盖了大量不同几何和流入条件的样本。此外，本文评估了几种最先进的神经代理模型，如Transolver和AB-UPT，特别关注它们对几何和流入变化的异区外泛化能力。其中，AB-UPT在亚音速流场中表现出色，并能再现物理上一致的阻力升力帕累托前沿，即使对于未见过的机翼配置也是如此。
### Conclusion
本文的结果表明，AB-UPT能够逼近未见过几何形状的阻力升力帕累托前沿，突显了其在快速气动设计探索中的高效性和有效性。为了促进未来的研究，我们的数据集已开源。
## 152. `cs.AI` - Dynaq 动态强化学习的预测性安全屏蔽 [PDF](https://arxiv.org/pdf/2511.21531), [HTML](https://arxiv.org/abs/2511.21531)
### Authors
Jin Pin,Krasowski Hanna,Vanneaux Elena
### Background
在确保强化学习的安全性方面实现现实世界任务的应用面临巨大挑战。现有的安全屏蔽通常通过随机采样安全行为或固定回退控制器来实现，但这种方法忽视了不同安全行为对未来表现的影响。
### Innovation
提出了一种基于模型的强化学习代理在离散空间中的预测性安全屏蔽。这种安全屏蔽基于安全环境模型的预测，局部更新Q函数。这种方法提高了性能同时保持了硬性安全保证。实验表明，即使短期预测回合也能识别出最优路径，且该方法在模拟与现实分布发生变化时表现出稳健性。
### Conclusion
该工作通过预测性安全屏蔽改进了 Dyna-Q 强化学习算法，并在多格世界环境中展示了其有效性和鲁棒性。
## 153. `cs.AI` - Merge and Bound: 直接在权重上进行操作的类增量学习 [PDF](https://arxiv.org/pdf/2511.21490), [HTML](https://arxiv.org/abs/2511.21490)
### Authors
Taehoon Kim,Donghwan Jang,Bohyung Han
### Background
类增量学习（CIL）旨在解决在持续学习新类别的过程中，模型对之前学习过的类别的知识遗忘问题。现有的CIL方法通常侧重于修改模型架构或重新调整学习目标，这可能会带来复杂性和性能下降的问题。
### Innovation
该论文提出了一种名为Merge-and-Bound（M&B）的新颖训练方法，直接在参数空间操作模型权重进行优化。M&B方法通过两种权重融合技术（跨任务和同任务权重融合）无缝集成到现有的CIL方法中，无需修改架构组件或变更学习目标。此外，还提出了一种有界更新技术，以最小化累计更新量并保留先前任务的知识，从而减少灾难性遗忘。这种方法可以有效地获得与旧模型相近的新模型。
### Conclusion
该研究在标准CIL基准测试上进行了广泛评估，并展示了与最先进的方法相比的优越性能。M&B方法的简单性和高效性使其成为CIL领域的有效解决方案，能够在不修改现有架构或重新调整学习目标的情况下实现更好的增量学习性能。
## 154. `cs.AI` - BAMAS: 为预算意识多智能体系统建模 [PDF](https://arxiv.org/pdf/2511.21572), [HTML](https://arxiv.org/abs/2511.21572)
### Authors
Liming Yang,Junyu Luo,Xuanzhe Liu,Yiling Lou,Zhenpeng Chen
### Background
基于大型语言模型（LLM）的多智能体系统已经成为使得自主智能体能够解决复杂任务的一种强大范式。随着这些系统复杂性的增加，成本成为实际部署中的重要考虑因素。然而，现有的研究很少解决如何在明确的预算约束下结构化多智能体系统的问题。
### Innovation
本文提出了BAMAS，一种具有预算意识的多智能体系统构建新方法。BAMAS通过求解一个整数线性规划问题来选择最优的LLM集合，平衡性能和成本。然后，通过强化学习方法确定这些LLM之间的协作拓扑结构。最后，根据选定的智能体及其协作拓扑结构构建并执行系统。BAMAS在三种代表性任务上进行了评估，并与现有的智能体构建方法进行了比较，结果显示在性能相当的情况下，BAMAS可以降低高达86%的成本。
### Conclusion
BAMAS方法通过预算约束下的智能体选择和协作结构优化，实现了降低多智能体系统成本的同时保持较高的性能。
## 155. `cs.AI` - Tool-RoCo: 一个在多机器人协作中的代理作为工具自治大规模语言模型基准 [PDF](https://arxiv.org/pdf/2511.21510), [HTML](https://arxiv.org/abs/2511.21510)
### Authors
Ke Zhang,Xiaoning Zhao,Ce Zheng,Jiahong Ning,Dandan Zhu,Wenqi Zhang,Chen Sun,Toshiharu Sugawara
### Background
近年来，基于大型语言模型（LLM）的多智能体系统的研究依赖于预设的调度，忽略了智能体的自主性。该研究提出了Tool-RoCo，一个基于RoCo多机器人协同基准的新颖基准，用于评估多智能体长时间协作中的LLM表现。Tool-RoCo通过引入协同工具和工具使用来评估多智能体的协同和自我组织，其中每个智能体根据当前状态从候选集中选择工具，在每次迭代后接收反馈并调整其选择。
### Innovation
Tool-RoCo 提出了四种 LLM 架构以评估不同的自主性水平：集中式协同、集中式自我组织、分散式协同和自我组织。这些架构通过代理和工具之间的远程调用关系测试了多智能体任务中的自主性和协同效果，并提出了一种新的工具使用范式，进一步定义了代理的协同和自组织行为。该研究使用多个 LLM 进行了实验，结果显示大多数工具是由智能体自己使用而非相互协助，且大多数激活工具用于维持现有代理的活跃状态。
### Conclusion
Tool-RoCo 提供了一个系统化的基准来评估多智能体任务中基于 LLM 的智能体的自主性和协同能力，实验结果表明，与同伴互助相比，当前 LLM 更倾向于持续激活智能体对任务进行适应性协同。该研究为评估多智能体系统中的 LLM 行为提供了一个重要的工具和理论依据。
## 156. `cs.AI` - 语音、偏见与共指：关于语音翻译中性别的一种可解释性研究 [PDF](https://arxiv.org/pdf/2511.21517), [HTML](https://arxiv.org/abs/2511.21517)
### Authors
Lina Conti,Dennis Fucci,Marco Gaido,Matteo Negri,Guillaume Wisniewski,Luisa Bentivogli
### Background
语音与文字不同，能够通过声学特征（如音高）传达说话者的特征信息，比如性别。这种特性可能导致模态特定的偏见问题。例如，在语音翻译（ST）中，从具有观念性性别的语言翻译到具有语法性别的语言时，说话者的语音特征可能会在性别分配中起作用，从而增加误标注性别或基于声音假设的风险。然而，ST模型在处理这些决定时的具体机制仍然不清楚。
### Innovation
本文研究了ST模型在跨三种语言对（英语-西班牙语/法语/意大利语）中分配性别给指代说话者的术语时所使用的机制，探讨了训练数据模式、内部语言模型（ILM）偏见和声学信息之间的相互作用。研究发现，模型不仅复制了训练数据中的词性特定性别关联，还学习了更多的男性优势模式。尽管ILM表现出强烈的男性偏见，但模型可以根据声学输入克服这些偏好。通过频谱对比特征归因，揭示了高性别准确率模型使用了一种先前未知的机制：利用第一人称代词将性别术语与说话者联系起来，获取频谱分布中的性别信息，而非集中于音高。
### Conclusion
研究显示语音翻译模型并非简单复制训练数据中的性别关联，而是学习了更广泛的模式，并根据音信息偏离内部语言模型的偏好。通过频谱对比特征归因，揭示了一种未知机制，利用第一人称代词将性别信息分布到频谱中，而非集中在音高上。
## 157. `cs.AI` - Multimodal Robust Prompt Distillation for 3D Point Cloud Models [PDF](https://arxiv.org/pdf/2511.21574), [HTML](https://arxiv.org/abs/2511.21574)
### Authors
Xiang Gu,Liming Lu,Xu Zheng,Anan Du,Yongbin Zhou,Shuchao Pang
### Background
基于学习的3D点云模型受到对抗攻击的重大威胁，这严重削弱了它们在安全性敏感应用中的可靠性。现有的防御方法通常存在两个问题：一是计算开销高，二是泛化能力差，无法处理各种类型的攻击。
### Innovation
提出了一种新颖而有效的教师-学生框架，名为Multimodal Robust Prompt Distillation (MRPD)，用于提炼稳健的3D点云模型。这种方法通过三种不同的教师模型（视觉模型处理深度投影、高性能3D模型和文本编码器）生成稳健的嵌入，并将其与学生点云模型的特征对齐。为了确保可靠的知识转移，这种细化过程受到信心门控机制的指导，该机制动态平衡所有输入模态的贡献。此外，所有的细化过程都在训练阶段完成，推理时不需要额外的计算代价。
### Conclusion
广泛的实验证明，MRPD在对抗各种白盒和黑盒攻击方面显著优于最先进的防御方法，甚至在干净数据上也表现出更好的性能。我们的工作为高效利用多模态知识构建稳健的3D视觉系统提供了一个新的、实用的范式。
## 158. `cs.AI` - 超越URL：提高大语言模型预训练效率的元数据多样性与位置 [PDF](https://arxiv.org/pdf/2511.21613), [HTML](https://arxiv.org/abs/2511.21613)
### Authors
Dongyang Fan,Diba Hashemi,Sai Praneeth Karimireddy,Martin Jaggi
### Background
近年来，将元数据纳入大型语言模型（LLMs）的预训练被认为是一种有望加速训练的方法。尽管以前的研究仅指出了一种有用的信号——URL，但仍然不清楚其他形式的元数据是否能带来更大的益处。
### Innovation
本文研究了更广泛的元数据类型，发现其他类型的元数据（例如，文档质量的细粒度指标）也可以在预训练中通过前置预测来加速。研究还发现有效元数据的共同特征：它们以更细粒度来编码信息。研究进一步引入元数据附加作为一种提高训练效率的方法，通过预测适当的元数据作为辅助任务来加快预训练。此外，通过掩码损失训练的可学习元标记可以恢复部分速度提升，从而诱导质量意识的潜在结构。
### Conclusion
通过探针分析，研究了潜在表示如何受到元数据的影响。综上所述，这些结果提供了将元数据整合以提高LLM预训练效率和效果的实用指南。
## 159. `cs.AI` - 基于模型的策略适应性在闭合环端到端自主驾驶中的应用 [PDF](https://arxiv.org/pdf/2511.21584), [HTML](https://arxiv.org/abs/2511.21584)
### Authors
Haohong Lin,Yunzhi Zhang,Wenhao Ding,Jiajun Wu,Ding Zhao
### Background
端到端（E2E）自主驾驶模型在开放环评估中表现出色，但在闭合环设置中往往面临级联错误和泛化性能不佳的问题。
### Innovation
提出了基于模型的策略适应性（MPA）框架，该框架通过使用几何一致的仿真引擎生成多样化的反事实轨迹，增强预训练E2E驾驶代理在部署中的鲁棒性和安全性。MPA训练基于扩散的策略适配器来细化基础策略的预测，并训练多步Q值模型来评估长期结果。
### Conclusion
实验结果表明，MPA在nuScenes基准上显著改善了在域内、域外和安全关键场景中的性能。进一步研究了反事实数据的规模和推理时的指导策略对整体效果的影响。
## 160. `cs.AI` - VacuumVLA: 通过统一的吸力和夹持工具增强VLA能力以实现复杂机器人操作 [PDF](https://arxiv.org/pdf/2511.21557), [HTML](https://arxiv.org/abs/2511.21557)
### Authors
Hui Zhou,Siyuan Huang,Minxing Li,Hao Zhang,Lue Fan,Shaoshuai Shi
### Background
视觉语言动作模型显著推动了通用机器人操作的发展，通过大规模预训练的视觉和语言表示。当前大多数视觉语言动作系统默认使用两指机械夹爪作为末端执行器。然而，在处理一些包含广泛接触面或需要合适吸附力的任务时，这些夹爪表现出固有的局限性，如擦洗玻璃表面或打开无把手的抽屉，这限制了其功能应用。
### Innovation
我们提出了一种低成本的集成硬件设计，结合了机械两指夹爪和真空吸盘单元，允许在单一末端执行器中进行两种模式的操纵。该系统支持在两种模式之间的灵活切换或协同使用，扩展了可行的操作任务范围。实验结果表明，这种混合末端执行器使机器人能够成功执行单一机械夹爪无法完成的复杂任务。
### Conclusion
我们的设计已在两个先进的视觉语言动作框架：DexVLA 和 Pi0 中验证了其高效性和实用性。所有硬件设计和控制系统的文件将被公开以促进进一步的发展和应用。
## 161. `cs.AI` - AI 中算法进步的起源 [PDF](https://arxiv.org/pdf/2511.21622), [HTML](https://arxiv.org/abs/2511.21622)
### Authors
Hans Gundlach,Alex Fogelson,Jayson Lynch,Ana Trisovic,Jonathan Rosenfeld,Anmol Sandhu,Neil Thompson
### Background
过去几十年，AI训练的FLOP效率因算法改进提升了约22,000倍（2012年至2023年）。尽管进行了小型消融实验，但仍无法完全解释这些效率提高的原因。通过广泛文献综述，作者估计额外未纳入消融实验的创新技术也无法解释更多效率提升，结果显示效率提升主要不超过100倍。为了解释这一效率差距，作者进行了扩增实验，发现算法的效率提升与计算量有关。LSTM与Transformer在计算最优扩增律方面存在指数差异，但其他许多创新技术的扩增几乎没有差异。
### Innovation
实验展示了算法效率在计算量上的依赖性。LSTM到Transformer转换过程中的效率提升占主导地位。研究表明，小型模型的算法进步远未达到预期，算法效率指标具有较强参考依赖性。
### Conclusion
作者的研究显示，小型模型算法进步远低于预期，算法效率提升与计算规模密切相关。
## 162. `cs.AI` - 低资源设备上的持续错误纠正 [PDF](https://arxiv.org/pdf/2511.21652), [HTML](https://arxiv.org/abs/2511.21652)
### Authors
Kirill Paramonov,Mete Ozay,Aristeidis Mystakidis,Nikolaos Tsalikidis,Dimitrios Sotos,Anastasios Drosou,Dimitrios Tzovaras,Hyunjun Kim,Kiseok Chang,Sangdok Mo,Namwoong Kim,Woojong Yoo,Jijoong Moon,Umberto Michieli
### Background
随着AI模型在日常设备中的普及，预测错误已成为影响用户体验的关键挑战。现有的解决方案主要集中在错误检测，但鲜有提供有效的纠正机制，尤其是在资源受限的设备上。
### Innovation
本文提出了一种新型系统，通过少量样本学习让用户能够纠正AI的误分类，无需大量计算资源和存储空间。该方法结合了服务器侧的基础模型训练和设备侧的原型基分类机制，通过原型更新而非重新训练模型来实现高效的错误纠正。
### Conclusion
该系统已在图像分类和目标检测任务中得到验证，在Food-101和Flowers-102数据集的一次性场景中实现了超过50%的错误纠正。系统几乎无遗忘，且在实用中的计算开销可以忽略不计。通过Android演示应用的测试，该系统展示了在实际场景中的应用潜力。
## 163. `cs.AI` - HarmonicAttack：一种适应性跨域音频水印移除方法 [PDF](https://arxiv.org/pdf/2511.21577), [HTML](https://arxiv.org/abs/2511.21577)
### Authors
Kexin Li,Xiao Hu,Ilya Grishchenko,David Lie
### Background
高质AI生成音频的可用性带来了诸如误导性竞选和声纹克隆欺诈等安全性挑战。有效防止滥用AI生成音频的关键手段之一是对音频进行水印，使其容易与真实音频区分开来。因此，那些试图滥用AI生成音频的人可能会试图移除音频水印，研究有效的移除技术对于客观评估音频水印的移除时准确性至关重要。然而，之前的方法要么假设移除水印所需的基本知识是不现实的，要么计算成本高昂，可能导致对当前水印方案的过度自信。
### Innovation
提出了HarmonicAttack，这是一种高效的音频水印移除方法，只需要基本的生成目标方案的水印能力，不需要其他知识。通过这种方法，训练了一个通用的水印移除模型，能够从任何带水印的音频样本中去除目标方案生成的水印。HarmonicAttack利用双路径卷积自编码器在时间和频率域上同时运行，结合GAN风格的训练来分离水印和原始音频。针对当前最先进的水印方案AudioSeal、WavMark和Silentcipher进行评估，HarmonicAttack展示出了更高的水印移除能力，并且几乎具有实时性能。尽管HarmonicAttack需要进行训练，但发现其能在分发外样本时保持较好的性能。
### Conclusion
HarmonicAttack提供了一种新的技术和方法来有效移除音频水印，能够保持实时性能，同时可以在不同样本之间进行知识转移，具有较强的实用性和适应性。
## 164. `cs.AI` - 注意力引导下的视言语动模型局部稀疏对抗攻击 [PDF](https://arxiv.org/pdf/2511.21663), [HTML](https://arxiv.org/abs/2511.21663)
### Authors
Naifu Zhang,Wei Tao,Xi Xiao,Qianpu Sun,Yuxin Zheng,Wentao Mo,Peiqiang Wang,Nan Zhang
### Background
近年来，嵌入式智能中的视言语动(VLA)模型发展迅速。然而，现有的对抗攻击方法需要进行昂贵的端到端训练，且经常生成显而易见的扰动斑块。
### Innovation
本文提出了一种名为ADVLA的框架，该框架直接将对抗扰动应用于从视觉编码器投影到语言特征空间的特征上。ADVLA在低幅值限制下有效干扰下游动作预测，并且注意力指导可以使扰动既集中又稀疏。还提出三种策略增强敏感性、强制稀疏性和集中扰动。
### Conclusion
实验表明，在$L_{text{∞}}=4/255$约束下，ADVLA结合Top-K掩码修改不到10%的像素，攻击成功率几乎达到100%。扰动集中于关键区域，整体图像中几乎不可察觉，其单步骤迭代需要约0.06秒，显著优于传统的斑块式攻击。总之，ADVLA在低幅值和局部稀疏条件下有效削弱了VLA模型的下游动作预测，避免了传统斑块攻击的高训练成本和显眼扰动，展示了在攻击VLA特征空间上的独特效果和实用价值。
## 165. `cs.AI` - Qwen3-VL技术报告 [PDF](https://arxiv.org/pdf/2511.21631), [HTML](https://arxiv.org/abs/2511.21631)
### Authors
Shuai Bai,Yuxuan Cai,Ruizhe Chen,Keqin Chen,Xionghui Chen,Zesen Cheng,Lianghao Deng,Wei Ding,Chang Gao,Chunjiang Ge,Wenbin Ge,Zhifang Guo,Qidong Huang,Jie Huang,Fei Huang,Binyuan Hui,Shutong Jiang,Zhaohai Li,Mingsheng Li,Mei Li,Kaixin Li,Zicheng Lin,Junyang Lin,Xuejing Liu,Jiawei Liu,Chenglong Liu,Yang Liu,Dayiheng Liu,Shixuan Liu,Dunjie Lu,Ruilin Luo,Chenxu Lv,Rui Men,Lingchen Meng,Xuancheng Ren,Xingzhang Ren,Sibo Song,Yuchong Sun,Jun Tang,Jianhong Tu,Jianqiang Wan,Peng Wang,Pengfei Wang,Qiuyue Wang,Yuxuan Wang,Tianbao Xie,Yiheng Xu,Haiyang Xu,Jin Xu,Zhibo Yang,Mingkun Yang,Jianxin Yang,An Yang,Bowen Yu,Fei Zhang,Hang Zhang,Xi Zhang,Bo Zheng,Humen Zhong,Jingren Zhou,Fan Zhou,Jing Zhou,Yuanzhi Zhu,Ke Zhu
### Background
介绍了Qwen系列中最强大的视觉语言模型Qwen3-VL，它在多种跨模态基准测试中表现出色，支持多达256K令牌的交织上下文，能够无缝地集成文本、图像和视频。该模型系列包括密集型（2亿/4亿/8亿/32亿）和专家混合（30亿-3亿/235亿-22亿）变体，以适应不同的延迟质量权衡。
### Innovation
Qwen3-VL带来了三项核心支柱：（i）增强的纯文本理解，在某些情况下超越了同类纯文本支撑结构；（ii）强大的长上下文理解能力，具有256K令牌窗口，能够对长文档和视频进行忠实的保留、检索和跨参考；（iii）先进的单图像、多图像和视频任务的跨模态推理，展示了在MMMU和视觉数学基准测试（例如MathVista和MathVision）中的领先性能。架构方面，引入了三项关键升级：（i）增强了交错-MRoPE，以增强图像和视频中的空间-时间建模；（ii）DeepStack集成，有效地利用多级ViT特征以提高视觉语言对齐；（iii）视频中的基于文本的时间对齐，从T-RoPE演进为明确的文本时间戳对齐，以实现更精确的时间定位。当在可比较的令牌预算和延迟约束下，Qwen3-VL在密集型和Mixture-of-Experts（MoE）架构中都实现了卓越的性能。
### Conclusion
Qwen3-VL有望成为图像基推理、自主决策和多模态代码智能在实际工作流程中的基础引擎。
## 166. `cs.AI` - 通过电信视角：所有训练样本都重要吗？ [PDF](https://arxiv.org/pdf/2511.21668), [HTML](https://arxiv.org/abs/2511.21668)
### Authors
Shruti Bothe,Illyyne Saffar,Aurelie Boisbunon,Hasan Farooq,Julien Forgeat,Md Moin Uddin Chowdhury
### Background
人工智能在电信领域的兴起，在优化无线接入网络和管理用户经验的同时，大幅增加了数据量和训练需求。电信数据经常噪声大、维度高、存储和处理成本高且需要大量标注。尽管人工智能至关重要，但标准工作流程仍然假设所有训练样本都同等重要。然而，下一代系统需要准确、高效的AI模型。本文挑战了同等重要性的假设，专注于分析和评估单个样本在电信训练中的角色，以及这些样本是否能够优化计算和能量使用。
### Innovation
通过样本级梯度分析每个时期的模式，识别模型学习中的影响和冗余。在此基础上，提出了一种样本重要性框架，有条件地优先处理受影响的数据，以减少计算而不牺牲准确性。实验证明该方法在三个实际电信数据集中展示了保留性能的同时减少了数据需求和计算开销，推动了电信中可持续AI的目标。
### Conclusion
本文提出的方法在保证性能的前提下减少了对数据的需求和计算开销，展示了在电信领域通过优化样本选择实现可持续AI的潜力。
## 167. `cs.AI` - 神经网络中的尺度无关柯尔莫哥洛夫-阿诺尔德几何 [PDF](https://arxiv.org/pdf/2511.21626), [HTML](https://arxiv.org/abs/2511.21626)
### Authors
Mathew Vanherreweghe,Michael H. Freedman,Keith M. Adams
### Background
弗里德曼和穆利根近期的研究表明，浅层多层感知器在处理合成三维任务时，会在训练过程中自发形成柯尔莫哥洛夫-阿诺尔德几何（KAG）结构。然而，这一体现在现实中的高维设置中是否依然存在，以及这种几何结构的空间特性是什么，还不得而知。
### Innovation
本文将KAG分析扩展到MNIST手写数字分类任务（784维），使用两层MLPs，通过不同尺度的空间分析发现KAG在训练过程中自发出现，并且在不同训练程序下表现出尺度不变性。
### Conclusion
研究揭示了神经网络在学习现实高维数据时，自发形成有组织且尺度不变的几何结构。
## 168. `cs.AI` - 重新审视不同难度水平上的泛化能力：并不容易 [PDF](https://arxiv.org/pdf/2511.21692), [HTML](https://arxiv.org/abs/2511.21692)
### Authors
Yeganeh Kordi,Nihal V. Nayak,Max Zuo,Ilana Nguyen,Stephen H. Bach
### Background
现有研究表明，大规模语言模型（LLMs）在不同任务难度下的泛化能力存在争议，不同训练数据难度的选择可能对效果有不同的影响。此前的研究尚未形成共识，且大多依赖于人类对任务难度的主观评价。因此，本文旨在通过系统评估LLMs在不同模型、数据集以及细粒度难度组上的泛化能力，来探讨这一问题。研究使用数千种不同LLMs的输出和项目反应理论（IRT）评分来重新定义难度等级。
### Innovation
本文创新之处在于采用更为客观、更大规模和更细粒度的方法来评估LLMs在不同难度任务上的泛化能力，不依赖人类对难度的评价。结果显示，跨难度范围的泛化能力受到限制，仅通过训练易于或困难数据无法实现全范围难度下的持续改进。这意味着在训练和评估数据中包含多种难度级别对于LLMs来说非常重要。
### Conclusion
该研究表明，需要在训练和评估数据中包含广泛的难度级别，以适应LLMs的需求，并应避免在难度方面采取捷径，以达到更好的泛化效果。
## 169. `cs.AI` - Matrix: 一种点对点多智能体合成数据生成框架 [PDF](https://arxiv.org/pdf/2511.21686), [HTML](https://arxiv.org/abs/2511.21686)
### Authors
Dong Wang,Yang Li,Ansong Ni,Ching-Feng Yeh,Youssef Emad,Xinjie Lei,Liam Robbins,Karthik Padthe,Hu Xu,Xian Li,Asli Celikyilmaz,Ramya Raghavendra,Lifei Huang,Carole-Jean Wu,Shang-Wen Li
### Background
合成数据由于其在训练大规模语言模型时能应对真实数据稀缺、昂贵或隐私敏感等问题的能力而变得越来越重要。许多合成任务需要协调的多智能体工作流，其中专门的智能体协作以产生高质量、更具多样性和结构更丰富的数据。然而，现有的多智能体合成框架通常依赖于一个中心化的调度者，导致可扩展性瓶颈，或者特化于特定领域，限制了灵活性。
### Innovation
我们介绍了Matrix，这是一种去中心化的框架，它将控制和数据流表示为通过分布式队列传递的序列化消息。这种点对点设计消除了中心化的调度者。每个任务在轻量级智能体中独立进行，而密集计算操作，如LLM推理或容器化环境，则由分布式服务处理。基于Ray的Matrix能够处理成千上万的并发智能体工作流，并提供模块化、可配置的设计，使其能够轻松适应各种数据生成工作流。
### Conclusion
我们在多种合成场景，如多智能体协作对话、基于网页的推理数据提取以及客户服务环境中的工具使用轨迹生成，对Matrix进行了评估。结果表明，在相同的硬件资源下，Matrix的数据生成吞吐量提高了2至15倍，而输出质量没有下降。
## 170. `cs.AI` - Vision Transformer 非单调扩展机制 [PDF](https://arxiv.org/pdf/2511.21635), [HTML](https://arxiv.org/abs/2511.21635)
### Authors
Anantha Padmanaban Krishna Kumar(Boston University)
### Background
视觉变换器 (Vision Transformers) 往往在更深的情况下性能不如更浅的版本，这挑战了对模型扩展的常见假设。本文通过在 ImageNet 数据集上系统性地分析 ViT-S、ViT-B 和 ViT-L 的表现，揭示了深度尺度演化过程中的一致三阶段坡谷攀爬模式。研究发现，性能较好的模型伴随着 [CLS] 标记作用的减弱，更倾向于局部片段标记间的分散式共识。
### Innovation
提出了信息碎化指数 (Information Scrambling Index)，定量分析信息混合的模式，并指出在 ViT-L 模型中，信息与任务的权衡大约迟于 ViT-B 模型 10 层出现，而且额外的层与更多的信息分散相关联，而非任务性能的提升。结果显示，在此区间内，变换器架构可能更受益于精心校准的深度和干净的相变阶段，而不是单纯增加参数量。
### Conclusion
信息碎化指数为现有模型提供了有用的诊断工具，也建议未来架构设计的潜在目标。相关代码可在该网址找到：this https URL。
## 171. `cs.AI` - Escaping the Verifier: Learning to Reason via Demonstrations [PDF](https://arxiv.org/pdf/2511.21667), [HTML](https://arxiv.org/abs/2511.21667)
### Authors
Locke Cai,Ivan Provilkov
### Background
训练大型语言模型通常依赖于带有特定验证器的强化学习，但在许多实际的推理密集型任务中缺乏验证器，尽管还有丰富的专家演示可供利用，但这些演示并未被充分用于推理导向的训练。
### Innovation
引入了RARO（相对对抗推理优化），该方法通过逆向强化学习从仅专家演示中学习强大的推理能力。该方法设置了策略（生成器）与相对鉴别器（批评家）之间的对抗交互，策略学会模仿专家答案，而批评家学习比较和区分策略和专家答案。该方法通过强化学习联合连续训练策略和批评家，并且识别出了对稳健学习至关重要的关键技术。
### Conclusion
实验结果显示，RARO在我们的所有评估任务（ Countdown、DeepMath 和 Poetry Writing）中显著优于强验证器自由基线，并且表现出与验证任务上强化学习相同的稳健扩展趋势。这些结果表明，该方法有效从专家演示中提取了强大的推理性能，即使在没有任务特定验证器的情况下也能实现稳健的推理学习。
## 172. `cs.AI` - 低空空域安全经济的无人机航迹规划：具有合规意识的混合DRL-LLM方法 [PDF](https://arxiv.org/pdf/2506.08532), [HTML](https://arxiv.org/abs/2506.08532)
### Authors
Yanwei Gong,Junchao Fan,Ruichen Zhang,Dusit Niyato,Yingying Yao,Xiaolin Chang
### Background
低空经济的快速发展推动了无人机（UAV）的广泛使用，而这种增长也带来了在复杂城市环境中的无人机航迹规划新挑战。现有的研究往往忽视了诸如城市空中区域限制和经济效益等关键因素，而这些因素对于低空经济环境至关重要。深度强化学习（DRL）被认为是解决这些问题的潜在解决方案，但由于学习效率较低其实际应用受到限制。
### Innovation
本文提出了一种新颖的无人机航迹规划框架，结合了DRL与大语言模型（LLM）推理，以实现安全、合规且经济有效的航线规划。实验结果表明，该方法在数据采集率、碰撞避免、成功着陆、法律规定遵循和能源效率等方面显著优于现有基准。
### Conclusion
我们的方法在解决低空经济环境下无人机航迹规划的关键挑战方面有效。未来的研究可以进一步优化DRL与LLM的结合，提高学习效率和模型复杂性。
## 173. `cs.AI` - 使用图神经网络和蒙特卡洛树搜索的地球观测卫星排程 [PDF](https://arxiv.org/pdf/2408.15041), [HTML](https://arxiv.org/abs/2408.15041)
### Authors
Antoine Jacquet,Guillaume Infantes,Emmanuel Benazera,Vincent Baudoui,Jonathan Guerra,Stéphanie Roussel
### Background
地球观测卫星排程（EOSP）是一个具有重要意义的优化问题。需要对一系列观测请求进行排期，并且这些观测请求受到可见窗口以及动作约束的影响。此外，问题高度过订阅：候选观测请求远多于实际可完成的数量。因此，需要选择一组可以执行的观测请求，并最大化其累计效益，还必须为这些观测请求制定可行的排期方案。
### Innovation
以往研究主要集中在启发式和迭代搜索算法上，本文提出了一种基于图神经网络（GNNs）和深度强化学习（DRL）的新方法来选择和调度观测请求。使用GNNs从表示EOSP实例的图形中提取相关信息，DRL驱动寻找最优排程搜索。添加了基于蒙特卡洛树搜索（MCTS）的后学习搜索步骤，以找到更优解。实验表明，本文方法可以在小规模问题实例上学习，并推广到更大的实际问题实例，性能与传统方法相比具有很强竞争力。
### Conclusion
实验结果表明，该方法能够从小规模问题实例中学到，并将其应用到更大规模的实际问题上，并展示了与传统方法相比具有很强的竞争力。
## 174. `cs.AI` - ToolOrchestra：通过高效模型和工具交响实现智能提升 [PDF](https://arxiv.org/pdf/2511.21689), [HTML](https://arxiv.org/abs/2511.21689)
### Authors
Hongjin Su,Shizhe Diao,Ximing Lu,Mingjie Liu,Jiacheng Xu,Xin Dong,Yonggan Fu,Peter Belcak,Hanrong Ye,Hongxu Yin,Yi Dong,Evelina Bakhturina,Tao Yu,Yejin Choi,Jan Kautz,Pavlo Molchanov
### Background
大型语言模型虽然强大，但解决像人类最后考试（HLE）这样的复杂问题仍然具有挑战性和成本高。小型协调器管理其他模型和各种工具可以提高智力的上限，并提高解决复杂代理任务的效率。
### Innovation
介绍了ToolOrchestra方法，通过增强学习训练小型协调器协调智能工具。ToolOrchestra使用目标导向、效率和用户偏好的奖励。Orchestrator模型比前代理工具使用代理更高效且成本更低，同时在给定查询中与用户偏好一致使用工具。在HLE上，Orchestrator的表现优于GPT-5，且效率高出2.5倍。在tau2-Bench和FRAMES上，Orchestrator表现远超GPT-5，使用成本仅为GPT-5的30%。广泛的分析表明，Orchestrator在多个指标下在性能和成本之间实现了最佳权衡，并且对未见过的工具具有鲁棒的泛化能力。这些结果表明，使用轻量级协调模型组合多样工具比现有方法更有效率和更有效果，为实用和可扩展工具增强推理系统铺平了道路。
### Conclusion
这些结果表明，使用轻量级协调模型组合多样工具相比现有方法是更有效率和更有效的，为实用和可扩展工具增强推理系统铺平了道路。
## 175. `cs.AI` - G$^2$VLM: 含统一3D重建和空间推理的地基视觉语言模型 [PDF](https://arxiv.org/pdf/2511.21688), [HTML](https://arxiv.org/abs/2511.21688)
### Authors
Wenbo Hu,Jingli Lin,Yilin Long,Yunlong Ran,Lihan Jiang,Yifan Wang,Chenming Zhu,Runsen Xu,Tai Wang,Jiangmiao Pang
### Background
现有的视觉-语言模型（VLMs）在空间智能方面缺乏稳健性，特别是在空间理解和推理任务上的表现不佳。研究者认为这一差距源于这些模型不具备将2D图像还原为3D空间的理解过程。因此，该文提出了G$^2$VLM，一种局部和文字间嵌入几何信息的模型，旨在填补3D空间重建和空间理解这两方面空间智能的基本方面。
### Innovation
G$^2$VLM是一种新颖的视觉-语言模型，它结合了空间3D重建和空间理解。G$^2$VLM通过直接利用学习到的3D视觉几何特征进行预测，并通过上下文学习和交错推理增强空间理解能力。这种设计对于空间理解具有高度可扩展性，能利用大量多视角图像和视频数据进行训练，并利用不太容易收集的3D视觉先验的好处。
### Conclusion
实验结果表明，G$^2$VLM在3D重建和空间理解任务上表现出色，获得了与最先进的直接3D重建模型相当的结果，并在多个空间理解和推理任务上超越或达到了竞争力。通过将一个语义强的VLM与低级3D视觉任务统一结合，G$^2$VLM有望成为社区的一个强大基线，并解锁更多未来应用，如3D场景编辑。
## 176. `cs.AI` - Co-PatcheR: 专门的小型推理模型在组件级的协作软件补丁 [PDF](https://arxiv.org/pdf/2505.18955), [HTML](https://arxiv.org/abs/2505.18955)
### Authors
Yuheng Tang,Hongwei Li,Kaijie Zhu,Michael Yang,Yangruibo Ding,Wenbo Guo
### Background
近期研究受通用大型语言模型（LLMs）在软件补丁方面的成功启发，开始训练专门的补丁模型。大多数方法通过单一的大型模型处理从问题定位到补丁生成再到补丁验证的整个补丁Pipeline，但这种方法在处理多样化的工作流程和专业知识需求时效率较低。70亿参数的最先进的模型在SWE-bench-Verified上的解决率达到41%。该研究基于协作机制，提出了一种新的补丁系统Co-PatcheR，该系统采用小型且针对特定任务的推理模型。
### Innovation
Co-PatcheR采用小型且专门针对各个组件的推理模型，通过专门的任务设计和训练方法。具体包括针对定位和生成补丁训练一个模型，提出一种混合验证方法（包括使用和不使用断言生成问题再现测试用例，并判断补丁正确性），并通过多数投票选择补丁。实证研究表明，Co-PatcheR在SWE-bench-Verified上达到了46%的解决率，仅使用3个14亿参数的模型。这种方法使用最少的训练资源和最小的模型成为最优秀的补丁模型。
### Conclusion
通过全面的消融实验，验证了研究中的方法，并对训练数据量、模型大小和测试阶段的扩展策略进行了分析。Co-PatcheR证明了协作机制在软件补丁处理中的优势，特别是在资源和模型规模受限的情况下。
## 177. `cs.AI` - 在大型语言模型对齐中操作多元价值观揭示了安全性、包容性和模型行为之间的权衡 [PDF](https://arxiv.org/pdf/2511.14476), [HTML](https://arxiv.org/abs/2511.14476)
### Authors
Dalia Ali,Dora Zhao,Allison Koenecke,Orestis Papakyriakopoulos
### Background
尽管大型语言模型（LLMs）越来越多地通过人类反馈进行训练以确保安全性和与人类价值观的对齐，但现有的对齐决策往往忽视了人类社会的多样性。本研究通过系统评估对齐流水线中的人口统计学差异及设计参数，探讨了如何整合多元价值观影响LLM行为的问题。研究者收集了来自美国和德国的1095名参与者（共27,375个评级）的数据，评估了LLM响应在五个维度上的评分：毒性、情感意识（EA）、敏感性、刻板偏见和有用性。
### Innovation
研究采用的技术包括根据不同社会群体的偏好微调多个大型语言模型和大型推理模型，同时变更评级尺度、处理分歧的方法和技术优化手段。研究发现，性别、政治立场和社会身份等因素对模型行为有系统性的影响。微调时选择不同的群体具体偏好会导致模型展现出不同的行为模式。技术设计选择也表现出强大的影响，如保留评估者分歧的方法相较于多数投票在降低毒性方面能实现大约53％的提升，五点制评分比二进制格式平均多减少22％的毒性；而直接偏好优化（DPO）在多值优化中始终优于群体相对政策优化（GRPO）。这些发现是回答一个关键问题的初步步骤：如何平衡专家驱动和用户驱动的信号以确保安全和公平的表现？
### Conclusion
研究结果表明，大型语言模型的对齐应该平衡专家驱动和用户驱动的信号，以确保模型行为的安全性和公平性，但同时也揭示了在安全性、包容性和模型行为之间存在权衡。未来研究需要进一步探讨如何在实际应用中实现这一平衡。
## 178. `cs.AI` - Heterogeneous Multi-Agent Proximal Policy Optimization for Power Distribution System Restoration [PDF](https://arxiv.org/pdf/2511.14730), [HTML](https://arxiv.org/abs/2511.14730)
### Authors
Parya Dolatyabi,Ali Farajzadeh Bavil,Mahdi Khodayar
### Background
大规模停电后恢复电力分配系统（PDS）需要进行一系列开关操作以重新配置馈线拓扑并协调分布式能源资源（DERs），而这些操作受到功率平衡、电压限制和热限值等非线性约束的影响。这使得传统的优化和基于价值的强化学习（RL）方法计算效率低下且难以扩展。
### Innovation
本文采用Heterogeneous-Agent Reinforcement Learning (HARL)框架，并通过Heterogeneous-Agent Proximal Policy Optimization (HAPPO)实现，在互联微电网之间实现协调恢复。每个代理控制一个具有不同负载、DER容量和开关数量的独特微电网，引入实际的结构异质性。去中心化的演员策略使用中央评论家进行训练，以计算稳定的优势值进行更新。开放DSS环境提供了全面的功率流反馈，并通过可微惩罚信号而不是无效动作禁止来强制执行操作限制。实验表明，HAPPO在IEEE 123节点和IEEE 8500节点系统上比DQN、PPO、MAES、MADQN、Mean-Field RL和QMIX实现了更快的收敛速度、更高的恢复功率以及更平滑的多种子训练。
### Conclusion
研究结果表明，在HARL框架中纳入微电网级别的异质性可以为复杂的PDS恢复提供一种可扩展、稳定且约束感知的解决方案。
## 179. `cs.AI` - Step-Audio-R1 技术报告 [PDF](https://arxiv.org/pdf/2511.15848), [HTML](https://arxiv.org/abs/2511.15848)
### Authors
Fei Tian,Xiangyu Tony Zhang,Yuxin Zhang,Haoyang Zhang,Yuxin Li,Daijiao Liu,Yayue Deng,Donghang Wu,Jun Chen,Liang Zhao,Chengyuan Yao,Hexin Liu,Eng Siong Chng,Xuerui Yang,Xiangyu Zhang,Daxin Jiang,Gang Yu
### Background
近年来，推理模型在文本和视觉领域的表现令人瞩目，通过延长链式思考有助于深入推理。然而，在音频语言模型方面，一个出乎意料的现象是它们在几乎没有或根本不进行推理的情况下表现更好，这引发了根本性的问题：真正意义上的音频智能是否能够从深刻的思考中获益？
### Innovation
本文引入了Step-Audio-R1，这是首个成功在音频领域解锁推理能力的模型。通过提出的模态接地推理蒸馏（MGRD）框架，Step-Audio-R1 学习生成与音频高度关联的推理链，而不是产生与声学特征无关的虚幻思考。该模型在全面的音频理解和推理基准测试中，包括语音、环境声音和音乐中，展示了强大的音频推理能力，超越了Gemini 2.5 Pro，实现了与Gemini 3 Pro相当的表现。这表明，当适当定位时，推理能力可以跨模态转移，将延长思考从负担转化为音频智能的强大资产。
### Conclusion
通过建立第一个成功的音频推理模型，Step-Audio-R1 开辟了新的途径，旨在构建真正多模态推理系统，可以在所有感官模态中进行深入思考。
## 180. `cs.AI` - Augur: 使用大型语言模型建模时间序列中的协变量因果关联 [PDF](https://arxiv.org/pdf/2510.07858), [HTML](https://arxiv.org/abs/2510.07858)
### Authors
Zhiqing Cui,Binwu Wang,Qingxiang Liu,Yeqiang Wang,Zhengyang Zhou,Yuxuan Liang,Yang Wang
### Background
大型语言模型（LLM）已经成为了时间序列预测的一个有前景的途径，这得益于其融入多模态数据的潜力。然而，目前基于LLM的方法也存在一些局限性，比如在模型架构中的边缘地位、对粗糙统计文本提示的依赖以及缺乏可解释性。
### Innovation
文章提出了Augur，一个完全由LLM驱动的时间序列预测框架。它利用LLM因果推理来发现和利用协变量之间的有向因果关联。Augur采用了两阶段的教师-学生架构：一个强大的教师LLM使用启发式搜索和成对因果测试从时间序列中推断有向因果图；一个轻量级的学生代理则基于编码为丰富文本提示的高置信度因果关联进行图的细化和调整以进行预测。
### Conclusion
广泛的实验证明，Augur在真实世界数据集上表现和基准方法具有竞争力，并且在零样本泛化方面表现出色，同时提高了预测精度并提供可解释的推理说明变量交互作用。
## 181. `cs.AI` - 使用图扩散网络学习Agent-Based模型中的个体行为 [PDF](https://arxiv.org/pdf/2505.21426), [HTML](https://arxiv.org/abs/2505.21426)
### Authors
Francesco Cozzi,Marco Pangallo,Alan Perotti,André Panisson,Corrado Monti
### Background
Agent-Based模型（ABMs）是研究复杂系统中涌现性质的强大工具。在ABMs中，代理行为受到局部互动和随机规则的控制。然而，这些规则通常是非可微的，限制了使用基于梯度的方法进行优化，从而阻碍了与现实世界数据的集成。
### Innovation
本文提出了一种新颖框架，通过观察生成的数据，学习任何ABM的可微近似。该方法结合了扩散模型来捕捉行为的随机性，以及图神经网络来建模代理之间的交互。区别于先前的替代方法，本文方法引入了根本性的转变：它直接建模个体代理行为，而不是近似系统级别的输出，从而保持了定义ABMs的分散式、自底向上的动力学。
### Conclusion
我们在两个ABM（舍宁根隔离模型和捕食者-猎物生态系统）上验证了我们的方法，结果显示它能够复制个体级模式，并准确预测训练外的涌现动力学。我们的结果表明，结合扩散模型和图学习有可能用于数据驱动的ABM仿真。
## 182. `cs.AI` - KRAL: 知识和推理增强学习以辅助LLM的临床抗菌治疗 [PDF](https://arxiv.org/pdf/2511.15974), [HTML](https://arxiv.org/abs/2511.15974)
### Authors
Zhe Li,Yehan Qiu,Yujie Chen,Xiang Zhou
### Background
临床抗菌治疗需要动态整合病原体特征、宿主因素、抗菌药物的药理特性以及感染的严重程度。这种复杂性对大型语言模型（LLM）在高度机密的临床决策中的应用提出了根本性限制，包括知识空白、数据隐私问题、高昂的部署成本和受限的推理能力。
### Innovation
提出了KRAL（Knowledge and Reasoning Augmented Learning），一种低成本、可扩展、保隐私的范式，利用教师模型推理自动提炼知识和推理轨迹，通过答案到问题的逆向生成，采用了启发式学习进行半监督数据增强（减少80%的手动注释要求），并利用自主强化学习同时提升医学知识和推理能力，优化计算和内存效率。通过多层次评估和模块化接口设计减少了评估成本并促进了系统的无缝更新。实验结果表明，KRAL 显著优于传统的检索增强生成（RAG）和监督微调（SFT）方法，在外部开源基准MEDQA上的准确度@1提高了1.8%，在PUMCH抗微生物基准上的通过率@1提高了27%，并且达到了SFT长期训练成本的大约20%。
### Conclusion
这确立了KRAL作为一种有效解决方案，用于增强本地LLM的临床诊断能力，使其能够在复杂的医疗决策支持中低成本、高安全性地部署。
## 183. `cs.AI` - CoMind：迈向以社区驱动的机器学习工程代理 [PDF](https://arxiv.org/pdf/2506.20640), [HTML](https://arxiv.org/abs/2506.20640)
### Authors
Sijie Li,Weiwei Sun,Shanda Li,Ameet Talwalkar,Yiming Yang
### Background
大型语言模型（LLM）代理有潜力自动化机器学习（ML）工程任务，但现有代理通常孤立地解决特定研究问题，不与更广泛的科研社区互动，而科研人员常常通过共享知识而受益。为了弥补这一不足，该文提出了一种名为MLE-Live的实时评估框架，用于评估智能代理在模拟Kaggle研究社区中的交流能力和利用集体知识的能力。在此基础上，提出了一种名为CoMind的多代理系统，能够积极整合外部知识，采用迭代并行探索机制，同时开发多个解决方案以平衡探索广度与实施深度。
### Innovation
该文创新性地引入了MLE-Live框架，用以评估代理在模拟Kaggle社区中的交流能力和利用集体知识的能力。基于此框架，提出了CoMind，一个能够积极整合外部知识的多代理系统，通过迭代并行探索机制实现了同时开发多个解决方案来平衡探索广度与实施深度，在75项过往Kaggle竞赛中，CoMind达到36%的奖牌率，建立了新的行业标准。更关键的是，在8项实际进行中的竞赛中，CoMind的性能优于92.6%的真人竞争对手，其中在三项官方排行榜上进入前5%，在一项排行榜上进入前1%。
### Conclusion
CoMind通过在实际竞赛中的优异表现，验证了其在机器学习工程领域的潜力，并提出了新的社区驱动的代理解决方案，为机器学习工程应用开辟了新的可能性。
## 184. `cs.AI` - 宇宙之思：利用大型语言模型促进创造性推理 [PDF](https://arxiv.org/pdf/2511.20471), [HTML](https://arxiv.org/abs/2511.20471)
### Authors
Yuto Suzuki,Farnoush Banaei-Kashani
### Background
由于大型语言模型（LLMs）在数学和复杂逻辑任务中的出色表现，基于LLMs的推理技术已经引起了越来越多的关注。随着链式思考（CoT）提示技术的发展，各种分解问题为更小、更连续步骤的推理方法层出不穷。但是，现有的推理模型主要关注传统的解决问题方式，而不能自然地生成通过创造性推理产生的创造性解决方案。在药物发现或商业策略制定等解决方案空间广泛，传统解决方案可能并不理想的问题领域内，创造性推理对于发现创新解决方案至关重要。
### Innovation
本文提出了一个受认知科学原理启发的创造性推理计算框架，基于该框架，提出了三种核心的创造性推理范式：组合、探索和转化推理。在此基础上，设计了利用LLMs实现这三种创造性过程的新型方法集，并提出了三个需要创造性解决的新任务，以及一个多维度评估基准来衡量创造性成果。与最先进的推理技术以及具有推理能力的代表性商业模型进行对比分析后，展示了UoT（宇宙之思）在创造性推理方面表现出优越性能。
### Conclusion
UoT展示了在创造性推理方面的优越性能，在药物发现或商业策略制定等需要创造性和创新性解决方法的领域中，UoT的方法集提供了一种新的思路和解决方案，有望推动这些领域的研究和发展。
## 185. `cs.AI` - 双平衡多任务学习 [PDF](https://arxiv.org/pdf/2308.12029), [HTML](https://arxiv.org/abs/2308.12029)
### Authors
Baijiong Lin,Weisen Jiang,Feiyang Ye,Yu Zhang,Pengguang Chen,Ying-Cong Chen,Shu Liu,Ivor W. Tsang,James T. Kwok
### Background
多任务学习旨在同时学习多个相关的任务，在众多领域中取得了巨大成功。然而，任务之间损失和梯度尺度的差异往往会导致性能妥协，使得任务权重的平衡成为一个重大挑战。
### Innovation
本文提出了双平衡多任务学习(DB-MTL)，以从损失和梯度两个方面实现任务平衡。DB-MTL 通过对每个任务损失执行对数变换来实现损失尺度的平衡，并通过将所有任务梯度按最大梯度范数进行归一化，来重新调整梯度幅度使其达到可比的尺度。
### Conclusion
在多个基准数据集上进行的大量实验表明，DB-MTL 一致地优于当前最先进的方法。
## 186. `cs.AI` - FRAGMENTA：基于片段的生成模型与代理调优的端到端药物先导优化框架 [PDF](https://arxiv.org/pdf/2511.20510), [HTML](https://arxiv.org/abs/2511.20510)
### Authors
Yuto Suzuki,Paul Awolade,Daniel V. LaBarbera,Farnoush Banaei-Kashani
### Background
分子生成在药物发现中至关重要，但特定类别的数据集往往包含少于100个训练样本。基于片段的方法在处理少量数据方面优于基于原子的方法，但现有的启发式片段划分限制了多样性和忽略了关键的片段。此外，模型调优通常需要药物化学家和AI工程师之间的缓慢且间接的合作。
### Innovation
本文提出了一种名为FRAGMENTA的端到端框架，用于药物先导优化。该框架包括：1) 一种新颖的生成模型，将片段划分重新定义为“词汇选择”问题，并利用动态Q学习联合优化片段划分与生成；2) 一种代理AI系统，通过与领域专家的对话反馈来精炼目标。此外，该系统从实现到自动化调优的闭环学习中摘除了AI工程师，逐渐学习领域知识。
### Conclusion
FRAGMENTA在实际癌症药物发现实验中的人机配置比基线识别了几乎两倍数量的高评分分子。完全自主的代理-代理系统在传统的人-人调优中表现出优越性，证明了代理调优在捕捉专家意图方面是有效的。
## 187. `cs.AI` - 使用大型语言模型和具身知识图谱的服务机器人安全控制 [PDF](https://arxiv.org/pdf/2405.17846), [HTML](https://arxiv.org/abs/2405.17846)
### Authors
Yong Qi,Gabriel Kyebambo,Siyuan Xie,Wei Shen,Shenghui Wang,Bitao Xie,Bin He,Zhipeng Wang,Shuo Jiang
### Background
服务机器人在不同行业中存在安全限制问题，引发了对确保机器人执行安全操作机制的需求，以防止对人类造成伤害或财产损失。尽管技术进步，包括将知识图谱与大型语言模型集成，但在确保自主机器人操作的一致安全性方面仍存在挑战。
### Innovation
提出了一个将大型语言模型与具身机器人控制提示(ERCPs)和具身知识图谱(EKGs)集成的新颖方法，以增强服务机器人的安全框架。ERCPs作为预定义指令，确保生成安全而精确的响应，这些响应随后由EKGs验证，确保机器人的操作始终与安全协议保持一致，从而在各种背景下促进更安全的操作实践。
### Conclusion
实验表明，配备我们的框架的机器人在安全标准方面的合规性远高于传统方法，在多变的现实任务中实现了更安全的人机交互，使我们的方法成为服务机器人中AI驱动的安全创新的前沿。
## 188. `cs.AI` - 大型语言模型中的模拟自我评估：一种关于人工智能自我效能的心理测量方法 [PDF](https://arxiv.org/pdf/2511.19872), [HTML](https://arxiv.org/abs/2511.19872)
### Authors
Daniel I Jackson,Emma L Jensen,Syed-Amad Hussain,Emre Sezgin
### Background
自我评估是可靠情报的关键要素，然而，对大型语言模型（LLMs）的评估主要集中在任务准确性上。研究者们发现，在不同条件下（如计算推理、社会推理和总结），LLMs的自我评价表现出不同的自我效能水平，总体得分低于人类标准。
### Innovation
研究将一般自我效能量表（GSES）改编用于十种LLMs，并在不同条件下对其进行了模拟自我评估。研究创新之处在于采用了心理测量方法（psychometric prompting）来提供结构化的LLMs沟通行为洞察，但未提供可靠的能力估计。
### Conclusion
自我评估并不反映实际能力，高分模型的总结并不一定表现出色，而低分模型有时也能准确作答。追加的信心提示可导致轻度的向下修订，表明首次评估可能存在轻微的自我高估。高自我效能模型更倾向于有人类特征的推理方式，而低分模型则采取谨慎的去人类化的解释方式。心理测量提示为理解LLMs沟通行为提供了结构化的洞察，但不能提供准确的表现估计。
## 189. `cs.AI` - 一种针对基于潜在扩散模型的图像编辑的灰箱攻击——通过后验塌陷 [PDF](https://arxiv.org/pdf/2408.10901), [HTML](https://arxiv.org/abs/2408.10901)
### Authors
Zhongliang Guo,Chun Tong Lei,Lei Fang,Shuai Zhao,Yifei Qian,Jingyu Lin,Zeyu Wang,Cunjian Chen,Ognjen Arandjelović,Chun Pong Lau
### Background
近期，潜在扩散模型（LDMs）的发展极大地推动了图像生成和操控技术的进步，同时也引发了关于数据误用和知识产权侵权的担忧。虽然对抗性攻击被广泛认为是防止生成AI滥用的防护手段，但当前的方法严重依赖于模型特定的知识，并且计算成本高昂。
### Innovation
本文提出了后验塌陷攻击（PCA），这是一种新颖的框架，用于保护图像免受未经授权的操控。PCA通过VAE编码器实现对图像编辑的保护，不依赖于特定模型的知识，仅需访问VAE编码器，这使PCA具有高度的通用性。PCA能实现扩散塌陷和聚集塌陷两种现象，通过参数调整实现不同目标的图像保护。PCA通过在文本条件化之前对VAE编码器进行操作，消除了需要进行空指令优化的要求，同时在不同VAE基线LDM架构中保持高效保护。
### Conclusion
广泛的实验证明，PCA在保护效果、计算效率（运行时间和VRAM）以及VAE基线LDM变体的一般化方面优于现有技术。本文的方法为防止图像未经授权的操作提供了一种有效的解决方案，从而促进了图像生成和操控技术的负责任应用。
## 190. `cs.AI` - CoxKAN：Kolmogorov-Arnold网络在可解释性高效率生存分析中的应用 [PDF](https://arxiv.org/pdf/2409.04290), [HTML](https://arxiv.org/abs/2409.04290)
### Authors
William Knottenbelt,William McGough,Rebecca Wray,Woody Zhidong Zhang,Jiashuai Liu,Ines Prata Machado,Zeyu Gao,Mireia Crispin-Ortuzar
### Background
生存分析是医学中用于建模死亡或复发等关键事件发生时间的重要统计分支，对改进治疗策略和患者结果至关重要。生存模型的选择通常需要在性能和解释性之间做出权衡，深度学习模型虽然性能高，但由于其黑盒性质，传统方法如柯克霍夫-阿诺德网络（KAN）因其透明度和准确性而受到青睐。然而，传统的Cox比例风险模型和基于深度学习的方法都未能提供关于预测变量之间复杂相互作用的清晰见解。
### Innovation
本文引入了CoxKAN，这是一种Cox比例风险Kolmogorov-Arnold网络，旨在提供高效率的生存分析，并保持解释性。CoxKAN通过合成和实际数据集的实验，展示了其在自动特征选择、恢复可解释的危险函数公式以及提供关键生物学标记对患者风险影响的清晰见解等方面的优势。
### Conclusion
CoxKAN在一个包含五组临床数据和四组基因组生物标志物的实际数据集上进行了评估，并在C-指数上的表现优于传统的Cox比例风险模型（最多提高4%），并且在某些情况下与基于深度学习的方法达到或超过了性能。研究成果可用于GitHub和Zenodo。
## 191. `cs.AI` - Multi-PA: 大型视觉语言模型隐私评估的多视角基准 [PDF](https://arxiv.org/pdf/2412.19496), [HTML](https://arxiv.org/abs/2412.19496)
### Authors
Jie Zhang,Xiangkui Cao,Zhouyu Han,Shiguang Shan,Xilin Chen
### Background
大型视觉语言模型（LVLMs）在各种任务中展现出巨大的潜力，但同时也存在严重的隐私风险，限制了其实际应用。现有的针对LVLMs的隐私评估研究范围有限，评估维度和隐私类别都存在不足。
### Innovation
提出了Multi-PA，这是一个全面的基准，用于评估LVLMs在隐私意识和隐私泄露方面的隐私保护能力。Multi-PA覆盖了26类个人隐私、15类商业机密和18类国家机密，总计31,962个样本。基于Multi-PA，评估了21个开源和2个封闭源LVLMs的隐私保护能力。结果显示，当前的LVLMs普遍存在较高的隐私泄露风险，不同类型的隐私（个人隐私、商业机密和国家机密）存在不同的漏洞。
### Conclusion
当前的LVLMs通常具有较高的隐私泄露风险，通过Multi-PA评估表明，模型在处理各种类型隐私时存在不同程度的漏洞。
## 192. `cs.AI` - LLM系统中的故障模式：可靠AI应用的系统级分类 [PDF](https://arxiv.org/pdf/2511.19933), [HTML](https://arxiv.org/abs/2511.19933)
### Authors
Vaishali Vinay
### Background
大型语言模型（LLMs）正快速融入决策支持工具、自动化工作流和AI驱动软件系统。然而，它们在生产环境中的行为尚不明确，失败模式与传统机器学习模型有很大不同。现有基准测试主要衡量知识或推理，但对于稳定性、可重复性、漂移或工作流集成几乎没有深入了解。
### Innovation
本文提出了一个系统级的故障模式分类，识别出十五种在实际LLM应用中出现的隐藏故障模式，包括多步推理漂移、潜在不一致性、上下文边界降解、错误工具调用、版本漂移和成本驱动的性能崩溃。通过这一分类，分析了现有评价和监控实践中的差距，并提出了设计LLM系统的原则，以增强其可靠性和成本意识。
### Conclusion
本文将LLM可靠性视为系统工程问题，而非单纯的数据模型问题。提供了评估方法、AI系统鲁棒性和可靠的LLM部署的分析基础。
## 193. `cs.AI` - 大型语言模型中最佳选项采样意识微调 [PDF](https://arxiv.org/pdf/2412.15287), [HTML](https://arxiv.org/abs/2412.15287)
### Authors
Yinlam Chow,Guy Tennenholtz,Izzeddin Gur,Vincent Zhuang,Bo Dai,Sridhar Thiagarajan,Craig Boutilier,Rishabh Agarwal,Aviral Kumar,Aleksandra Faust
### Background
近期的研究表明，在推理时有效地利用计算资源对于从大规模语言模型中获得更好的性能至关重要。本文探讨了一种新的推理意识微调范式，通过直接优化推理时策略的性能来微调模型。
### Innovation
研究提出了基于模仿学习和强化学习方法的与最佳选项采样（BoN）意识微调的范式，从而克服了BoN中的非可微argmax运算难题。实验表明，这种方法能提高BoN方法的性能和推理时的计算效率。
### Conclusion
通过BoN意识微调，验证器能够在测试时输入中交替选择最佳响应与更具多样性的响应，从而在Hendrycks MATH数据集上提高Gemma 2B的性能，并在HumanEval数据集上进一步提升。
## 194. `cs.AI` - 自然策略能力在随机多Agent系统中的应用 [PDF](https://arxiv.org/pdf/2401.12170), [HTML](https://arxiv.org/abs/2401.12170)
### Authors
Raphaël Berthon,Joost-Pieter Katoen,Munyque Mittelmann,Aniello Murano
### Background
正式方法合成的策略可能非常复杂，通常需要无限内存，这在尝试建模多Agent系统（MAS）时不符合预期行为。尽管自然策略作为一种新的框架能够平衡Agent进行策略规划所需的记忆与形式验证的复杂性，但目前仅限于完全确定性情境。
### Innovation
本文首次探讨了在随机多Agent系统下，自然策略下的概率时序逻辑PATL和PATL*的检验证（如NatPATL和NatPATL*）。主要成果表明，当主动联盟限于确定性策略时，对于概率模型检查，NatPATL是NP完全的，而NatPATL*具有2NEXPTIME的复杂度。在未限制的情况下，NatPATL的复杂度为EXPSPACE，NatPATL*的复杂度为3EXPSPACE。
### Conclusion
本文的研究揭示了不同的限制条件下的复杂度变化，为理解和优化多Agent系统中的策略计算提供了新的视角。
## 195. `cs.AI` - 超越反省：通过外部行为反馈强化思考 [PDF](https://arxiv.org/pdf/2501.01457), [HTML](https://arxiv.org/abs/2501.01457)
### Authors
Diji Yang,Linda Zeng,Kezhen Chen,Yi Zhang
### Background
大型语言模型在推理时能够处理复杂的任务，但由于其概率性质，其推理过程可能会变得不可靠或不一致。现有的方法通过让模型反省自己的推理过程来做出纠正，但这种方式继承了原始输出中的偏见，即所谓的反省错觉。现有的自我反省方法无法有效解决问题，因此本文提出了一个新的外部主义框架Distillation-Reinforcement-Reasoning (DRR)。
### Innovation
提出了一个新的外部主义框架Distillation-Reinforcement-Reasoning (DRR)，该框架通过评估模型的可观察行为给出纠正反馈，而不是依赖模型的反省。首先，DRR提取推理器的行为痕迹，然后训练一个轻量级的外部分辨率模型（DM）。在推理时，此DM充当批评者，识别并拒绝可疑的推理步骤，从而不用更改基础模型就提高推理质量。
### Conclusion
在多个推理基准测试中，DRR框架明显优于现有的自我反省方法。该方法轻量级且无需标注，提供了增强大型语言模型推理可靠性的可扩展和灵活的解决方案。
## 196. `cs.AI` - BoundingDocs：带有空间注释的文档问答统一数据集 [PDF](https://arxiv.org/pdf/2501.03403), [HTML](https://arxiv.org/abs/2501.03403)
### Authors
Simone Giovannini,Fabio Coppini,Andrea Gemelli,Simone Marinai
### Background
本文提出了一项统一的文档问答数据集，该数据集结合了多个与文档人工智能（Document AI）和视觉丰富文档理解（VRDU）相关的公开数据集。本文的主要贡献包括两方面：首先，将现有的文档人工智能任务，如信息提取（IE），重新定义为一个问答任务，使该数据集成为训练和评估大规模语言模型的合适资源；其次，公开了所有文档的OCR结果，并在文档图像中标注了答案的确切位置。
### Innovation
本文提出了一个统一的文档问答数据集，首次结合了多个相关的公有数据集，填补了现有数据集在文档理解和相应的大规模语言模型评估上的空白。此外，通过引入文档图像中的答案标注和不同提示技术的探索，有效提升了文档理解模型的性能。
### Conclusion
利用该数据集，探索了不同的提示技术（可能包括边界框信息）对开放权重模型性能的影响，识别出最有效的文档理解方法。
## 197. `cs.AI` - ProtoPFormer: 在视觉变压器中集中于原型部分以实现可解释图像识别 [PDF](https://arxiv.org/pdf/2208.10431), [HTML](https://arxiv.org/abs/2208.10431)
### Authors
Mengqi Xue,Qihan Huang,Haofei Zhang,Jingwen Hu,Jie Song,Mingli Song,Canghong Jin
### Background
Prototypical part network (ProtoPNet) 通过其自我解释的特性，在可解释人工智能（XAI）方面受到广泛关注，并推动了后续研究。然而，在将其直接应用于视觉变压器（ViT）骨干网络时，学习到的原型可能会有‘分散注意力’的问题，这意味着它们更有可能被背景激活，而不是关注前景。这对于原型方法基于变压器的应用带来了挑战，因其强大的长期依赖建模能力使得其难以专注于原型部分，严重影响其固有解释性。因此，本研究提出了原型部分变压器（ProtoPFormer），以更恰当且有效地结合基于原型的方法和ViT，提高图像识别的可解释性。
### Innovation
论文提出了原型部分变压器（ProtoPFormer），通过引入全局和局部原型来捕捉和突出目标的代表性整体和局部特征，依据ViT的结构特点。全局原型用于提供对象的整体视图，引导局部原型集中于前景并排除背景的影响。随后，局部原型被明确监督以集中于其各自的原型视觉部分，从而提高整体解释性。实验结果显示，提出的全局和局部原型能够相互校正并在最终决策中共同发挥作用，从整体和局部两个视角透明且忠实地解释决策过程。此外，ProtoPFormer 在与最新原型基线相比时，展现了更优的性能和可视化结果。
### Conclusion
我们提出的全局和局部原型可以相互校正并在最终决策中联合做出决定，分别从整体和局部视角对决策过程进行关联地忠实解释。此外，ProtoPFormer 在性能和可视化结果方面均优于最新的原型基线。代码已发布于 [此链接]。
## 198. `cs.AI` - CroMe: 使用跨模态三变换器和度量学习的多模态假新闻检测 [PDF](https://arxiv.org/pdf/2501.12422), [HTML](https://arxiv.org/abs/2501.12422)
### Authors
Eunjee Choi,Junhyun Ahn,XinYu Piao,Jong-Kook Kim
### Background
近年来，多模态假新闻检测受到了越来越多的关注。现有的方法依赖于独立编码的单模态数据，忽视了通过先进技术捕捉跨模态相似性和内部模态关系的优势。
### Innovation
提出了跨模态三变换器和度量学习的多模态假新闻检测（CroMe）方法。CroMe 使用冻结图像编码器和大型语言模型结合的语言-图像预训练（BLIP2）进行编码，以捕获详细的文字、图像和图像-文本表示。度量学习模块使用代理锚点方法来捕获内部模态关系，特征融合模块则使用跨模态三变换器进行有效集成。最终，融合特征通过分类器进行处理，以预测内容的真实性。
### Conclusion
实验表明，CroMe 在多模态假新闻检测方面的表现优异。
## 199. `cs.AI` - 适应性室内导航辅助下的实时对象检测性能评估 [PDF](https://arxiv.org/pdf/2501.18444), [HTML](https://arxiv.org/abs/2501.18444)
### Authors
Abhinav Pratap,Sushant Kumar,Suchinton Chakravarty
### Background
该研究着眼于为盲人个体提供辅助技术时对准确和高效的物体检测的需求。为此，研究者评估了YOLO、SSD、Faster R-CNN和Mask R-CNN这四种实时物体检测算法在室内导航辅助中的应用。使用Indoor Objects Detection数据集，研究检测精度、处理速度和适应室内环境的能力。
### Innovation
研究在室内导航辅助环境中评估了多种实时物体检测算法，并强调了精确性和效率之间的权衡。这推动了适应性机器学习应用程序的发展，特别是优化了为视障人士提供的室内导航解决方案，促进了无障碍环境的实现。
### Conclusion
研究结果表明，通过权衡精度和效率，可以更好地选择适用于实时辅助导航的最佳算法。这对于提高视障人士的室内导航解决方案具有重要意义，同时也为实现实时辅助导航技术的进步提供了宝贵的经验和理论依据。
## 200. `cs.AI` - PaTAS: 平行的主观逻辑在神经网络中用于信任传播的系统 [PDF](https://arxiv.org/pdf/2511.20586), [HTML](https://arxiv.org/abs/2511.20586)
### Authors
Koffi Ismael Ouattara,Ioannis Krontiris,Theo Dimitrakos,Dennis Eisermann,Frank Kargl
### Background
在关键安全应用中部署人工智能系统时，信任已成为一个重要要求。传统的评估指标如准确率和精度未能捕捉模型预测的不确定性或可靠性，特别是在对抗性或退化条件下。
### Innovation
提出了基于主观逻辑的平行信任评估系统（PaTAS），这是一种框架，用于使用主观逻辑建模和传播神经网络的信任。PaTAS 通过信任节点和信任函数在标准神经计算过程中并行传播输入、参数和激活的信任。框架定义了参数信任更新机制和推断路径信任评估（IPTA）方法，以在推断期间计算实例特定的信任。实验表明，PaTAS 能够产生可解释且一致的信任估计，并在中毒、有偏见或不确定数据场景中揭示可靠性缺口。
### Conclusion
通过使神经架构中的信任推理透明且量化，PaTAS 为整个 AI 生命周期中评估模型可靠性提供了一个坚实的理论基础。
## 201. `cs.AI` - 作为数据点的默尔索 [PDF](https://arxiv.org/pdf/2502.01364), [HTML](https://arxiv.org/abs/2502.01364)
### Authors
Abhinav Pratap
### Background
在数据化的时代，人类体验被简化为可量化的指标，引发深刻的哲学和伦理问题。本文通过阿尔贝·加缪小说《局外人》中的主人公默尔索的视角，探讨这一问题。默尔索生活中的情感疏远体现了存在主义的虚无主义概念。文章利用自然语言处理技术（如情感检测、情感分析以及命名实体识别）量化默尔索生命中的关键事件和行为。研究表明，算法模型在处理复杂人类体验，尤其是源于存在主义孤立和道德暧昧的情况时存在局限性。
### Innovation
研究采用自然语言处理技术，对小说中人物行动和情感进行了情感检测、情感分析和命名实体识别，这种结合文学研究与数据科学的方法新颖独特。
### Conclusion
研究揭示了现代AI工具在解读默尔索的情感和行为时的误解，对将人性的细腻叙事简化为数据点的现象提出了道德上的质疑，并呼吁在人工智能领域中融入人本主义价值。
## 202. `cs.AI` - 基于数据驱动的Lipschitz连续性：一种提高对抗鲁棒性的成本效益方法 [PDF](https://arxiv.org/pdf/2406.19622), [HTML](https://arxiv.org/abs/2406.19622)
### Authors
Erh-Chung Chen,Pin-Yu Chen,I-Hsin Chung,Che-Rung Lee
### Background
随着深度神经网络（DNNs）在敏感应用场景中的部署，确保其安全性和鲁棒性变得至关重要。一个主要的威胁来自对抗性攻击，即小的输入扰动可以导致错误的预测。最近的对抗训练进展通过引入外部数据集或生成模型中的额外样本来提高鲁棒性，但这通常会带来高昂的计算成本，限制了其实用性和在实际部署中的应用。
### Innovation
本文提出了一种基于Lipschitz连续性的成本效益高的替代方法，能够在不使用生成数据的情况下实现与广泛补充数据训练的模型相当的鲁棒性。与传统的对抗性训练不同，本文的方法只需要单次遍历数据集而无需进行梯度估计，因此非常高效。此外，本文的方法可以无缝集成到现有的对抗性训练框架中，并增强模型的鲁棒性，而不需要额外的生成数据。
### Conclusion
实验结果表明，本文的方法不仅减少了计算开销，还保持或提高了鲁棒神经网络的防御能力。这项工作为开发实用且可扩展的对抗攻击防御方法提供了有希望的方向。
## 203. `cs.AI` - 通过融合全局和局部统计信息进行数据估值 [PDF](https://arxiv.org/pdf/2405.17464), [HTML](https://arxiv.org/abs/2405.17464)
### Authors
Xiaoling Zhou,Ou Wu,Michael K. Ng,Hao Jiang
### Background
近年来，高质量数据在多种应用中的关键作用引起了对数据估值的关注。现有的数据估值方法中，基于Shapley值的方法因其坚实的理论支持而较为普遍。然而，Shapley值的确切计算通常是计算上难以承受的，促使开发了多种近似技术。现有方法通常忽视了价值分布信息的融合，未能考虑动态数据的状况，从而影响了其性能和应用潜力。
### Innovation
本文强调了全局和局部统计属性在数据估值中的重要性。首先，我们对这些分布进行了全面分析，揭示了有价值的信息和关键模式。其次，我们提出了一种增强的数据估值方法，将探索到的分布特性融合到两个正则项中，以改进Shapley值估计。我们还提出了一种新颖的动态数据估值方法，能够在不重新计算Shapley值的情况下推断更新的数据值，从而显著提高计算效率。这些正则化器可以无缝融入现有的多种数据估值方法。
### Conclusion
我们在一系列任务中进行了广泛的实验，包括Shapley值估计、基于价值的数据添加和删除、检测误标数据以及动态数据估值。实验结果展示了我们所提出方法的一致有效性和效率，证实了全局和局部价值分布在数据估值中的巨大潜力。
## 204. `cs.AI` - 跨越关键鸿沟的收敛学习：表征对齐如何随层训练和分布偏移演变 [PDF](https://arxiv.org/pdf/2502.18710), [HTML](https://arxiv.org/abs/2502.18710)
### Authors
Chaitanya Kapoor,Sudhanshu Srivastava,Meenakshi Khosla
### Background
对于神经科学和人工智能而言，了解收敛学习至关重要，即独立训练的神经系统的内部表示是否趋向一致。然而，现有文献通常局限于少数几种模型和单一数据集，依赖单一的对齐度量，并仅在训练后的一个检查点进行评估。这些限制限制了对收敛学习的全面理解。
### Innovation
本文进行了大规模的收敛学习审计，覆盖了多种视觉模型和数千对层对，并通过比较三种不同的对齐家族：线性回归（仿射不变）、正交普鲁斯特斯（旋转/反射不变）和排列/软匹配（单元序不变），展示了正交变换在对齐表示方面的有效性接近于更灵活的线性变换。此外，研究还发现大部分最终对齐在第一个训练周期内形成，而深层层则在分布变化时出现差异，这表明对齐主要由共享输入统计和架构偏见驱动，而不是最终任务解决方案。
### Conclusion
研究结果填补了对收敛学习理解的关键空白，对于神经科学和人工智能具有重要影响。
## 205. `cs.AI` - OuroMamba: 一种无需数据的视觉Mamba量化框架 [PDF](https://arxiv.org/pdf/2503.10959), [HTML](https://arxiv.org/abs/2503.10959)
### Authors
Akshat Ramachandran,Mingyu Lee,Huan Xu,Souvik Kundu,Tushar Krishna
### Background
在启用视觉Mamba模型（VMMs）的无数据后训练量化（DFQ）时存在两个关键挑战：（1）VMM的循环状态转换限制了长期交互的捕捉，导致语义较弱的合成数据；（2）VMM激活在时间步长上表现出动态异常变化，使得现有的静态后训练量化（PTQ）技术无效。
### Innovation
OuroMamba提出了一种两阶段框架：（1）OuroMamba-Gen用于生成具有丰富语义和意义的合成数据。该过程通过在潜在状态空间中的邻域相互作用生成的VMM特征应用对比学习；（2）OuroMamba-Quant在推理过程中采用混合精度量化，并结合轻量级动态异常检测。特别是，我们提出了基于阈值的激活渠道选择策略，该策略每时间步逐年更新。
### Conclusion
在视觉和生成任务上进行的广泛实验表明，我们的无数据OuroMamba超越了现有的数据驱动PTQ技术，实现了多量化设置中的最先进的性能。此外，我们实现了高效GPU内核，以实现最高达2.36倍的实用延迟加速。代码和合成数据集可以在此处获取：this https URL
## 206. `cs.AI` - 无需配对标注数据：端到端自我监督学习在无人机视角地理位置定位中的应用 [PDF](https://arxiv.org/pdf/2502.11381), [HTML](https://arxiv.org/abs/2502.11381)
### Authors
Zhongwei Chen,Zhao-Xu Yang,Hai-Jun Rong,Guoqi Li
### Background
无人机视角地理位置定位（DVGL）旨在通过检索最相关的带有GPS标记的卫星图像来实现无人机的精确定位。然而，大多数现有的方法严重依赖严格预配对的无人机-卫星图像进行监督学习。当目标区域发生变化时，通常需要新的配对样本来适应分布变化。这些方法标注成本高且转移性有限，极大地阻碍了DVGL在开放场景中的实际部署。
### Innovation
本文提出了一种新颖的端到端自我监督学习方法，该方法具有浅层骨干网络，称为动态记忆驱动和邻域信息学习（DMNIL）方法。该方法采用聚类算法生成伪标签，并采用双路径对比学习框架来学习区分性视图内表示。此外，DMNIL包含了两个核心模块，包括动态层次记忆学习（DHML）模块和信息一致性进化学习（ICEL）模块。DHML模块结合短期和长期记忆，以增强视图内特征的一致性和可区分性。与此同时，ICEL模块利用邻域驱动的动态约束机制系统地捕捉跨视图的潜在语义关联，从而改善跨视图特征对齐。为了进一步稳定和增强自我监督训练过程，引入了伪标签增强策略来提高伪监督的质量。
### Conclusion
在三个公开基准数据集上的大量实验表明，所提出的方法在自我监督方法中始终表现出色，并且甚至超越了几种最先进的监督方法。我们的代码可在多个网址处获取。
## 207. `cs.AI` - TS-RAG：基于检索增强生成的时间序列基础模型是更强的零样本预测器 [PDF](https://arxiv.org/pdf/2503.07649), [HTML](https://arxiv.org/abs/2503.07649)
### Authors
Kanghui Ning,Zijie Pan,Yu Liu,Yushan Jiang,James Yiming Zhang,Kashif Rasul,Anderson Schneider,Lintao Ma,Yuriy Nevmyvaka,Dongjin Song
### Background
近年来，大型语言模型（LLMs）和基础模型（FMs）在时间序列预测任务中变得流行。虽然微调LLMs能够实现领域适应，但它们往往难以在不同且未见过的数据集上进行泛化。同时，现有的时间序列基础模型（TSFMs）在处理非平稳动态和分布偏移方面仍然面临挑战，主要是由于缺乏有效的适应机制。
### Innovation
本文提出了TS-RAG，这是一种检索增强生成框架，旨在提高TSFMs的泛化能力和可解释性。TS-RAG利用预训练的时间序列编码器检索知识库中的语义相关段落，丰富输入查询的上下文表示。此外，还提出了一种自适应检索混合（ARM）模块，该模块可以动态地将检索到的模式与TSFM的内部表示融合，从而提高预测准确性，而无需特定任务的微调。
### Conclusion
通过对七个公开基准数据集的全面实证研究，结果显示TS-RAG在零样本预测性能方面达到了最佳状态，相比于现有的TSFMs，在不同的领域中提高了高达6.84%的预测准确性，同时提供了理想的可解释性。我们的代码和数据可在以下链接获取：this https URL
## 208. `cs.AI` - SOAP：增强时空关系和运动信息捕获的少样本动作识别 [PDF](https://arxiv.org/pdf/2407.16344), [HTML](https://arxiv.org/abs/2407.16344)
### Authors
Wenbo Huang,Jinghui Zhang,Xuwei Qian,Zhen Wu,Meng Wang,Lei Zhang
### Background
高帧率（HFR）视频的动作识别提高了精细表达，但减少了时序关系和运动信息密度。因此，传统基于数据驱动的训练需要大量视频样本。然而，在真实场景中样本并不总是充足的，推动了少样本动作识别（FSAR）的研究。现有的大多数少样本动作识别工作在空间特征提取后通过时间对齐构建视频样本之间的时空关系，并将时空特征分开处理，同时通过狭小视角捕捉帧间运动信息而不考虑密度，导致运动信息捕捉不足。
### Innovation
提出了名为Spatio-temporal frAme tuPle enhancer (SOAP) 的新型插件式架构。该模型相比于简单的特征提取考虑了不同特征通道之间的时序连接及特征的时空关系，并使用包含更多运动信息的帧四元组捕捉了更全面的运动信息。此外，结合不同帧数的帧四元组为捕捉更广泛的运动视角提供了支持。
### Conclusion
SOAP-Net 在知名的基准数据集 SthSthV2、Kinetics、UCF101 和 HMDB51 上实现了新的最先进性能。广泛的经验评估表明了 SOAP 的竞争力、插件性、泛化能力和鲁棒性。目前代码已公开。
## 209. `cs.AI` - 极度低资源和濒危语言的推理转移：通过高效语言理解跨接语言 [PDF](https://arxiv.org/pdf/2504.02890), [HTML](https://arxiv.org/abs/2504.02890)
### Authors
Khanh-Tung Tran,Barry O'Sullivan,Hoang D. Nguyen
### Background
近年来，大型语言模型（LLMs）可以通过生成链式推理（CoT）方式应对推理任务，但这些进步主要应用于高资源语言，而低资源语言则被留置。本文通过先前的提示、模型编辑和微调方法，研究在极度低资源场景下CoT技术的应用。
### Innovation
提出了一种名为英语锚点CoT训练的方法，利用LLMs在潜在空间中偏向于主导语言的洞察，对低资源语言输入进行有监督的微调，生成英语的CoT并在目标语言中输出最终响应。我们的方法在数学推理基准测试中，相比其他基准，在低资源场景下取得了高达28.33%的性能提升。此外还进行了混合语言CoT和两阶段训练实验，显示出明确的语言理解和推理分离可以增强跨语言推理能力。
### Conclusion
我们的研究结果和资源为多语言推理提供了一条实用途径，即使在极度低资源语言数据稀缺的情况下，也无需在每个极度低资源语言上进行大量重新训练。此外，我们还公开了LC2024基准，这是第一个针对爱尔兰语（一种极度低资源和濒危语言）进行的数学任务基准，旨在促进未来的研究工作。
## 210. `cs.AI` - 推荐目录之外的个性化图像生成 [PDF](https://arxiv.org/pdf/2502.18477), [HTML](https://arxiv.org/abs/2502.18477)
### Authors
Gabriel Patron,Zhiwei Xu,Ishan Kapnadak,Felipe Maia Polo
### Background
个性化在人机交互中至关重要，但现有的基于扩散的图像生成系统对用户多样性的影响仍然很低。现有方法通常需要昂贵的成对偏好数据，或者通过大语言模型引入延迟。已有方法未能直接从用户的间接反馈信号（如点赞、评分和点击）中学习。
### Innovation
提出了REBECA（REcommendations BEyond CAtalogs），一个基于轻量级和可扩展框架的个性化图像生成方法，通过预先训练的扩散模型后端，可以直接从隐式反馈信号学习用户和评分特定的图像嵌入。
### Conclusion
通过在实际数据集上进行严格评估，提出了一种新颖的统计个性化验证器和基于排列的假设检验，以评估偏好匹配。结果表明，REBECA能够生成高质量、个性化的图像，性能优于基线方法，同时保持计算效率。
## 211. `cs.AI` - MigGPT：利用大型语言模型跨版本自动迁移Linux内核外部补丁 [PDF](https://arxiv.org/pdf/2504.09474), [HTML](https://arxiv.org/abs/2504.09474)
### Authors
Pucheng Dang,Di Huang,Dong Li,Kang Chen,Yuanbo Wen,Qi Guo,Xing Hu
### Background
内核外部补丁对于适应新硬件或实现特定功能至关重要。但是，维护和更新这些补丁需要资深工程师投入大量精力。尽管大型语言模型（LLMs）在各个领域取得了显著进展，表明它们具有自动迁移内核外部补丁的潜力，但研究表明，LLMs在理解不完整的代码背景和识别迁移点方面存在不足。
### Innovation
我们提出了一种名为MigGPT的框架，结合了新颖的代码指纹结构和三个精心设计的模块，以提高内核外部补丁迁移的准确性和效率。我们还建立了一个强大的基准测试，使用实际的内核外部补丁项目来评估LLM的能力，结果显示MigGPT显著优于直接应用的LLMs，迁移任务的完成率平均为74.07%。
### Conclusion
MigGPT在自动迁移内核外部补丁方面表现出色，为该领域的自动化提供了新的解决方案。
## 212. `cs.AI` - 在组合任务结构中表征模式匹配及其局限性 [PDF](https://arxiv.org/pdf/2505.20278), [HTML](https://arxiv.org/abs/2505.20278)
### Authors
Hoyeon Chang,Jinho Park,Hanseul Cho,Sohee Yang,Miyoung Ko,Hyeonbin Hwang,Seungpil Won,Dohaeng Lee,Youbin Ahn,Minjoon Seo
### Background
尽管大型语言模型（LLMs）表现出色，但其成功往往依赖于模式匹配行为，却在组合任务中的领域外泛化中表现出失败。当前研究中，行为研究通常使用允许多种泛化来源的任务设置（如代数不变性、结构重复），这使得难以精确测试和解释模型通过模式匹配进行泛化的表现及其局限性。
### Innovation
本文首先将模式匹配形式化为功能等价性，即识别在其余输入保持不变时总是导致相同结果的输入子序列对。然后，系统研究了仅解码器Transformer和Mamba在隔离这种机制的受控任务中的行为。研究结果提供了预测性和定量性的洞见：（1）模式匹配的实例性成功可以通过见证相关功能等价性的上下文数量很好地预测。（2）证明了通过识别数据缩放定律中的指数，学习两步结构的紧样本复杂性边界。（3）路径歧义是结构障碍：当变量通过多个路径影响输出时，模型无法形成统一的中间状态表示，影响了准确性和解释性。（4）思考链降低了数据需求但未能解决路径歧义。因此，提供了一种预测且可验证的模式匹配边界，并为基础性诊断混合泛化机制的分离奠定了基础。
### Conclusion
本文提供了模式匹配和其在组合任务结构中的局限性的预测性边界，提出了定量的评估指标，并通过实验证实理论预测，强调了路径歧义对准确性和解释性的影响。
## 213. `cs.AI` - 带硬约束的物理约束流匹配：具有硬约束的生成模型采样 [PDF](https://arxiv.org/pdf/2506.04171), [HTML](https://arxiv.org/abs/2506.04171)
### Authors
Utkarsh Utkarsh,Pengfei Cai,Alan Edelman,Rafael Gomez-Bombarelli,Christopher Vincent Rackauckas
### Background
近年来，深度生成模型被应用于受偏微分方程(PDEs)支配的物理系统中，提供可扩展的模拟和不确定性感知推理。然而，对物理约束(线性和非线性的守恒定律等)的强制执行依然具有挑战性。现有的方法通常依赖于软惩罚或架构偏置，这意味着它们无法保证硬约束的有效实施。
### Innovation
本文提出了一种名为物理约束流匹配(PCFM)的零样本推断框架，该框架可以在预训练的基于流的生成模型中强制执行任意非线性约束。PCFM通过在中间解态应用基于物理的更正连续引导采样过程，同时与学习到的流保持一致，并满足物理约束。实验结果显示，PCFM在一系列PDEs上均优于无约束和有约束的基线模型，包括含有冲击、不连续性和尖锐特征的PDEs，并确保最终解中约束的准确满足。
### Conclusion
该方法提供了一个灵活的框架，用于在科学和通用生成模型中强制执行硬约束，尤其是在约束满足至关重要的应用中。
## 214. `cs.AI` - IVY-FAKE：一种统一的可解释框架和用于图像和视频AIGC检测的基准 [PDF](https://arxiv.org/pdf/2506.00979), [HTML](https://arxiv.org/abs/2506.00979)
### Authors
Changjiang Jiang,Wenhui Dong,Zhonghao Zhang,Chenyang Si,Fengchang Yu,Wei Peng,Xinbin Yuan,Yifei Bi,Ming Zhao,Zian Zhou,Caifeng Shan
### Background
随着人工智能生成内容（AIGC）技术的迅速发展，虽然已经能够生成高质量的合成内容，但也引发了重大的安全问题。当前的检测方法面临以下两大挑战：一是缺乏用于生成图像和视频的多维度可解释数据集，现有的开源数据集（例如WildFake和GenVideo）依赖于过于简化的二元注释，限制了训练检测器的可解释性和可信度；二是基于前MLLM的伪造检测器（例如FakeVLM）在逐步推理过程中的解释性不够精细，这妨碍了精准的定位和解释。
### Innovation
为了应对这些挑战，该研究引入了Ivy-Fake，这是第一个大规模的多模态可解释AIGC检测基准。该基准包括超过106,000个丰富标注的训练样本（图像和视频）和5,000个手动验证的评估示例，这些数据源自多个生成模型和真实世界的数据集，并通过精心设计的管道确保多样性和质量。此外，该研究还提出了Ivy-xDetector，这是一种基于组相对策略优化（GRPO）的强化学习模型，能够生成可解释的推理链，实现多项合成内容检测基准的稳健性能。
### Conclusion
广泛的实验证明了该数据集的优势，证实了我们的方法的有效性。值得注意的是，我们的方法在GenImage上的性能从86.88%提高到了96.32%，远超出先前的最优方法。
## 215. `cs.AI` - AI研究中的严谨性：需要一种更广泛、负责任的AI影响下的严谨性观念 [PDF](https://arxiv.org/pdf/2506.14652), [HTML](https://arxiv.org/abs/2506.14652)
### Authors
Alexandra Olteanu,Su Lin Blodgett,Agathe Balayn,Angelina Wang,Fernando Diaz,Flavio du Pin Calmon,Margaret Mitchell,Michael Ekstrand,Reuben Binns,Solon Barocas
### Background
在AI研究和实践中，严谨性主要被理解为方法论的严谨性，例如数学、统计或计算方法是否正确应用。这种狭隘的严谨性观念导致了负责AI社区提出的一些担忧，包括对AI系统能力的夸大其词。文章作者认为，需要一种更广泛的严谨性观念来指导AI研究和实践。
### Innovation
文章提出了一种更广泛的严谨性观念，除了更加广泛地理解方法论严谨性之外，还应包括四个方面：（1）基于背景知识决定工作重点的认识严谨性；（2）受学科、社区或个人规范、标准或信念影响的研究严谨性；（3）理论构建的清晰度的概念严谨性；（4）报告内容及其方式的报告严谨性；（5）现有证据支持推论的支持严谨性。文章还提供了一种有用的语言和框架，以促进研究人员、政策制定者、记者和其他利益相关者的必要对话。
### Conclusion
通过提供一种更广泛的严谨性观念，文章为AI社区的研究、政策制定者、记者和其他利益相关者之间亟需的对话提供了语言和框架。
## 216. `cs.AI` - LCB-CV-UNet：高动态范围雷达信号增强检测器 [PDF](https://arxiv.org/pdf/2505.23454), [HTML](https://arxiv.org/abs/2505.23454)
### Authors
Yanbin Wang,Xingyu Chen,Yumiao Wang,Xiang Wang,Chuanfei Zang,Guolong Cui,Jiahuan Liu
### Background
当前针对高动态范围（HDR）雷达信号的性能下降问题，提出了一种称为Logarithmic Connect Block (LCB)的硬件高效且可插拔模块，旨在解决相位相干性保持问题，并且通过构建双混合数据集生成方法生成了半合成数据集，以模拟多种HDR信号场景。
### Innovation
提出了LCB-CV-UNet模型来解决HDR雷达信号性能下降问题。核心创新点包括：1) LCB模块用作保持相位相干性的解决方案；2) 双混合数据集生成方法用于生成能够模拟各类HDR信号场景的半合成数据集。
### Conclusion
实验结果表明，LCB-CV-UNet模型在计算复杂度增加不到1%的前提下，提升了约1%的总检测概率，并且在城市目标在11-13 dB信噪比的范围中性能提升了5%。实际实验验证了该模型的实用性。
## 217. `cs.AI` - 力提示：视频生成模型可以学习和泛化基于物理的控制信号 [PDF](https://arxiv.org/pdf/2505.19386), [HTML](https://arxiv.org/abs/2505.19386)
### Authors
Nate Gillman,Charles Herrmann,Michael Freeman,Daksh Aggarwal,Evan Luo,Deqing Sun,Chen Sun
### Background
近期视频生成模型的进展激发了对能够模拟现实环境的世界模型的兴趣。尽管导航已被广泛研究，但能够模拟现实世界力的物理意义的交互方式仍相对较少被探索。
### Innovation
本文研究了将物理力作为视频生成的控制信号，并提出了力提示，通过局部点力（如戳植物）和全局风力字段（如风吹动布料）使用户能够与图像进行交互。演示了这些力提示可以使视频局实在物理控制信号下作出真实的响应，并且在不使用任何3D资产或物理模拟器的情况下利用原始预训练模型中的视觉和运动先验。最重要的是，初步实验表明，即使只有少量的物体演示，视频生成模型也可以很好地泛化，能够模拟各种几何形状、场景和材料上的力。
### Conclusion
我们的方法在基于Blender生成的视频上进行培训，并用约15k的训练样例在四个A100 GPU上进行一天的训练，显著优于现有方法，提高了世界模型与真实物理交互的接近程度。实验中还探讨了泛化的来源进行了解剖，揭示了视觉多样性和特定文本关键字在训练中的关键作用。所有数据集、代码、权重和交互视频演示已发布在项目页面上。
## 218. `cs.AI` - 无掩模对比度先验增强的双分支融合网络在无掩模阴影去除中的应用 [PDF](https://arxiv.org/pdf/2507.21949), [HTML](https://arxiv.org/abs/2507.21949)
### Authors
Jiyu Wu,Yifan Liu,Jiancheng Huang,Mingfu Yan,Shifeng Chen
### Background
现有的阴影去除方法通常依赖于阴影掩模，这在实况场景中难以获取。尽管可以通过探索如局部对比度信息等固有图像线索来引导阴影去除，但这些线索固有的模糊性在复杂场景中会形成关键限制，导致难以区分真正的阴影与低反射物体及细致背景纹理。
### Innovation
提出了一种自适应门控双分支注意机制（AGBA），该机制动态地筛选并重新权重大对比度，以有效分离阴影特征与干扰视觉元素。为了克服恢复软阴影边界和细微细节的持续挑战，引入了一种基于扩散的频率-对比度融合网络（FCFN），利用高频和对比度线索引导生成过程。
### Conclusion
实验结果表明，该方法在无掩模方法中达到了最先进的结果，同时在与基于掩模方法的竞争性能中保持了竞争力。
## 219. `cs.AI` - AutoDiscovery: 利用贝叶斯惊奇进行开放性科学发现 [PDF](https://arxiv.org/pdf/2507.00310), [HTML](https://arxiv.org/abs/2507.00310)
### Authors
Dhruv Agarwal,Bodhisattwa Prasad Majumder,Reece Adamson,Megha Chakravorty,Satvika Reddy Gavireddy,Aditya Parashar,Harshit Surana,Bhavana Dalvi Mishra,Andrew McCallum,Ashish Sabharwal,Peter Clark
### Background
自主科学发现（ASD）带来的不仅是能够回答提出的问题，而是还需要知道哪些问题是值得探索的。当前ASD的研究主要依赖于人类规定的科研问题来引导假设生成。然而，通过允许AI系统凭借其自身的标准进行探索，可能会进一步加速科学发现。尽管已有一些针对开放性ASD的方法利用多样性和人类兴趣度进行假设选择，但这些方法在处理庞大的假设空间时表现出不足，或是定义模糊。
### Innovation
本文提出了一种名为AutoDiscovery的方法，采用贝叶斯惊奇度作为驱动科学探索的标准，在限定的预算下，AutoDiscovery能显著多于竞争对手制造惊奇的发现，且有三分之二的发现被认为是领域专家感到惊奇的，这表明这是构建开放性ASD系统的重要步骤。
### Conclusion
AutoDiscovery通过量化LLM对假设的先验信念到收集实验结果后的后验信念之间的知识转变，利用蒙特卡洛树搜索策略与渐进扩展方法进行高效探索，评估结果表明在固定预算条件下，AutoDiscovery在数据驱动的发现中表现优越，且3/4的发现令领域专家感到惊奇，显示出其作为开放式ASD系统的潜力。
## 220. `cs.AI` - 公司如何管理人工智能的环境可持续性？关于绿色人工智能努力与法规的访谈研究 [PDF](https://arxiv.org/pdf/2505.07317), [HTML](https://arxiv.org/abs/2505.07317)
### Authors
Ashmita Sampatsing,Sophie Vos,Emma Beauxis-Aussalet,Justus Bogner
### Background
随着人工智能（AI）的广泛应用，基于AI的软件对环境的负面影响不再可以忽视，研究和缓解这种影响已成为一个关键的研究领域。但目前尚不清楚环境可持续性在工业领域采用AI中的作用，以及AI法规对推动绿色AI实践和决策的影响。因此，本文旨在调查工业从业者对绿色AI的认知和管理。
### Innovation
通过与来自10个不同组织的11名采用AI软件的参与者进行访谈，研究探讨了AI采用、减轻AI负面环境影响的当前努力，以及欧盟AI法案和企业可持续性报告指令（CSRD）的影响。结果显示，大多数公司优先考虑AI采用中的业务效率，而对环境可持续性的考虑较少，同时绿色AI实践和管理的监控与减轻措施有限。
### Conclusion
研究发现反映了公司在绿色AI方面的紧迫性和优先级缺乏。建议当前的监管措施不够有效，这具有政策制定者的含义。此外，需要提高行业意识，并为绿色AI实践提供用户友好的技术与工具。
## 221. `cs.AI` - 基于探查的多智能体多臂老虎机的公平算法 [PDF](https://arxiv.org/pdf/2506.14988), [HTML](https://arxiv.org/abs/2506.14988)
### Authors
Tianyi Xu,Jiaxin Liu,Nicholas Mattei,Zizhan Zheng
### Background
该研究关注的是在未知或有限信息情况下，如何通过探查策略来确保多智能体环境中给定的臂具有公平的结果同时最大化系统整体性能。
### Innovation
研究提出了一种基于探查的多智能体多臂老虎机（MA-MAB）框架，该框架结合了有限信息条件下的公平性考虑。针对在线情境，研究开发了一种能够维持公平性的同时具有亚线性遗憾的算法。在离线情境下，利用亚模属性设计了有保证性能的贪婪探查算法。
### Conclusion
实验表明，该方法在合成和实际数据集上能够优于基线方法，既达到更好的公平性，也具备更高的效率。
## 222. `cs.AI` - 流匹配遇见PDEs：基于物理约束的统一生成框架 [PDF](https://arxiv.org/pdf/2506.08604), [HTML](https://arxiv.org/abs/2506.08604)
### Authors
Giacomo Baldan,Qiang Liu,Alberto Guardone,Nils Thuerey
### Background
生成机器学习方法，例如扩散模型和流匹配，在模拟复杂系统行为和构建高效代理模型方面显示出巨大潜力。然而，这些方法通常从数据中隐式地学习潜在的物理规律。
### Innovation
提出了一种新的生成框架——基于物理约束的流匹配(PBFM)，该框架在流匹配目标中显式嵌入了物理约束，包括PDE残差和代数关系。此外，还引入了训练时间的时域延展技术，提高了最终无噪声样本预测的准确性。此外，研究了噪声水平$boldsymbol{bm{tau}_{boldsymbol{bm{text{min}}}}}$在物理约束下的作用，并评估了一种随机采样策略，以减少物理残差。方法在联合优化流匹配损失和基于物理约束的残差损失方面不需要对它们相对权重进行超参数调优。
### Conclusion
通过在三个代表性的PDE问题上的广泛基准测试，我们的方法在物理残差准确性方面比流匹配高出8倍，并在分布准确性方面优于现有算法。因此，PBFM为物理和工程应用中的代理建模、不确定性量化和加速仿真提供了一个原理性和高效的框架。
## 223. `cs.AI` - 对称性破坏分岔问题的交错流匹配方法 [PDF](https://arxiv.org/pdf/2509.03340), [HTML](https://arxiv.org/abs/2509.03340)
### Authors
Fleur Hendriks,Ondřej Rokoš,Martin Doškář,Marc G.D. Geers,Vlado Menkovski
### Background
在非线性动力系统中，分岔现象通常会导致多个共存的稳定解，尤其在对称性被破坏的情况下更为明显。传统的确定性机器学习模型难以捕捉这种多解性，往往会将多个解平均处理，从而无法准确表示低对称性的结果。
### Innovation
本文提出了一种基于流匹配的生成框架，用于建模分岔结果的完整概率分布。该方法能够直接采样多个有效的解，同时通过协变模拟能够保留系统对称性。引入了一种对称匹配策略，该策略在群操作下使预测输出和目标输出对齐，从而在协变设置中实现精确学习。我们在一系列系统中验证了该方法，包括玩具模型和复杂的物理问题，如挠曲梁和Allen-Cahn方程。
### Conclusion
流匹配方法在捕捉多模态分布和对称性破坏分岔方面显著优于非概率方法和变分方法，展示了在高维系统中建模多稳态性的原则性和可扩展性解决方案。
## 224. `cs.AI` - UITron-Speech: 基于语音指令的自助GUI代理 [PDF](https://arxiv.org/pdf/2506.11127), [HTML](https://arxiv.org/abs/2506.11127)
### Authors
Wenkang Han,Zhixiong Zeng,Jing Huang,Shu Jiang,Liming Zheng,Longrong Yang,Haibo Qiu,Chang Yao,Jingyuan Chen,Lin Ma
### Background
自主代理在图形用户界面（GUI）上的应用正在革新人机交互，但由于这些代理依赖于基于文本的指令，这限制了它们在无障碍性和便捷性方面的应用，特别是在免手持场景中。本研究旨在解决这一问题，旨在用语音替代文本作为GUI代理的指令输入方式，提出了一种全新的端到端GUI代理，这种代理能够直接处理语音指令和设备截图来预测用户操作。
### Innovation
1. 通过使用随机说话人文本转语音模型合成了高质量的语音指令数据集，以应对数据稀缺性问题。2. 提出了混合模态训练策略以解决预训练基础模型中的模态不平衡问题。3. 进行了GUI置地预测误差的统计分析，并提出了一种无训练步骤的两步置地校正方法来缓解微小的定位偏差。4. 在多个基准上的实验表明，UITron-Speech表现出稳健的性能和更强的适应性，说明了基于语音驱动的GUI代理在更便捷和智能的人机交互方面的可行性和潜力。
### Conclusion
本研究通过引入基于语音指令的GUI代理UITron-Speech，极大地增强了其在无障碍性和便捷性方面的表现。同时进行了无训练过程的两步置地校正和混合模态训练策略的研究，进一步证明了基于语音驱动的GUI代理的可行性和巨大潜力，为实现更加智能和便捷的人机交互提供了有力支持。
## 225. `cs.AI` - 开源语言模型中的特殊字符对抗攻击 [PDF](https://arxiv.org/pdf/2508.14070), [HTML](https://arxiv.org/abs/2508.14070)
### Authors
Ephraiem Sarabamoun
### Background
大规模语言模型在各种自然语言处理任务中表现出显著的能力，但这些模型对基于字符级别的对抗性操控的脆弱性给实际部署带来了重要的安全问题。本文研究了包括Unicode、同形词、结构化和文本编码在内的不同特殊字符攻击方法，旨在绕过安全机制。
### Innovation
研究了多种特殊字符攻击方法，并通过7个开源模型（参数范围从3.8B到32B）进行了4,000多次攻击测试，揭示了所有模型尺寸都存在的关键漏洞，包括成功破解、不一致的输出和不相关的幻想。
### Conclusion
研究结果显示所有模型都存在重大漏洞，通过特殊字符攻击可以实现模型的破解、产生不相关的输出或不一致的生成结果，这对于实际部署中的安全性提出了重要警示。
## 226. `cs.AI` - 不完美信息游戏中针对静态对手的一致对手建模 [PDF](https://arxiv.org/pdf/2508.17671), [HTML](https://arxiv.org/abs/2508.17671)
### Authors
Sam Ganzfried
### Background
在多智能体环境中，智能体的目标是最大化与对方智能体的总奖励。传统的博弈论解决方案，如纳什均衡，在某些情况下可能会取得良好的性能，但这些方法无法利用对手历史和可观察数据。目前，对手建模算法利用机器学习技术来利用可用数据对表现不佳的对手进行利用，但即便如此，在不完美信息游戏中，这些方法的有效性仍然有限。
### Innovation
本文提出了一种新的算法，该算法能够实现特定的属性，并使用投影梯度下降法基于序列形式博弈表示解决凸最小化问题，从而高效地收敛到对手的真实策略，即使在游戏迭代次数趋近无穷大时也是如此。
### Conclusion
新的算法可以在有限和历史数据的辅助下，确保在面对从已知先验分布中抽取的静态对手时，智能体的模型会逐渐逼近对手的真实策略。
## 227. `cs.AI` - 用LLM代理赋能时间序列预测 [PDF](https://arxiv.org/pdf/2508.04231), [HTML](https://arxiv.org/abs/2508.04231)
### Authors
Chin-Chia Michael Yeh,Vivian Lai,Uday Singh Saini,Xiran Fan,Yujie Fan,Junpeng Wang,Xin Dai,Yan Zheng
### Background
现有的AutoML方法主要集中在自动化特征工程和模型架构搜索上，而最近关于时间序列预测的研究表明，轻量级模型通常可以实现最先进的性能。这一发现促使研究者探索在时间序列数据的AutoML中提高数据质量而非模型架构作为有前景的方向。
### Innovation
提出了一种数据为中心的代理DCATS，利用随附时间序列的元数据来清洁数据并优化预测性能。该方法通过使用四种时间序列预测模型对大规模交通流量预测数据集进行了评估，并显示了在所有测试模型和时间范围内的平均6%误差减少，强调了数据为中心的方法在时间序列预测AutoML中的潜力。
### Conclusion
结果显示，DCATS在所有测试模型和时间范围上实现了平均6%的误差减少，突显了数据为中心的方法在时间序列预测AutoML中的潜力。
## 228. `cs.AI` - 起点在哪里？扩散大型语言模型可能需要一个不同的位置 [PDF](https://arxiv.org/pdf/2508.12398), [HTML](https://arxiv.org/abs/2508.12398)
### Authors
Zhixin Xie,Xurui Song,Jun Luo
### Background
近年来，扩散型大语言模型（dLLMs）因其独特的训练和推理方法成为了一种有竞争力的非自回归范式。然而，当前对这种新型架构的安全性研究还相对匮乏。本文旨在首次对dLLMs的安全性能进行分析，并提出了针对其独特生成特性的新颖安全对齐方法。
### Innovation
本文提出了一个新的安全对齐方法，名为Middle-tOken Safety Alignment (MOSA)，该方法通过强化学习直接对齐模型中间生成内容与安全拒绝，用于保护模型生成内容的安全。此外，研究揭示了防御者和攻击者之间的不对称性，即对于防御者来说，响应中间部分的token比初始部分更为重要，而对于攻击者来说，中间part的token相对难以操控，因为dLLMs倾向于按顺序生成。
### Conclusion
实验结果强烈证明了MOSA方法的安全性能优越性，并验证了其在代码、数学和通用推理任务上的实用性。
## 229. `cs.AI` - 不同类别下的所有划分并非平等：重新思考跨无关类别属性泛化的评估 [PDF](https://arxiv.org/pdf/2509.06998), [HTML](https://arxiv.org/abs/2509.06998)
### Authors
Liviu Nicolae Fircă,Antonio Bărbălau,Dan Oneata,Elena Burceanu
### Background
之前的研究主要针对窄税onomic领域或视觉上相似的范畴内进行属性预测，但尚不清楚当前的模型是否能够抽象出属性并在概念上相距甚远的类别中应用这些知识。
### Innovation
本文提出了第一个针对此类条件下的属性预测鲁棒性进行明确评估的方法，通过引入基于LLM的语义分组、嵌入相似度阈值化、基于嵌入的聚类以及基于超类的分区策略来减少训练集和测试集之间的关联性，以此测试模型是否可以在无关的物体类型之间正确推断共享属性。
### Conclusion
研究结果表明，当训练集和测试集之间的关联性降低时，性能急剧下降，表明存在对划分设计的强烈敏感性。在评估的方法中，聚类方法在减少隐藏关联性的同时保持可学习性方面效果最佳。这些发现为目前表示形式的局限性提供了新见解，并为未来属性推理基准建设提供了指导。
## 230. `cs.AI` - WeatherDiffusion：内在空间中的可控天气编辑 [PDF](https://arxiv.org/pdf/2508.06982), [HTML](https://arxiv.org/abs/2508.06982)
### Authors
Yixin Zhu,Zuoliang Zhu,Jian Yang,Miloš Hašan,Jin Xie,Beibei Wang
### Background
传统的像素空间编辑方式在处理天气编辑任务时难以保持较高的可控制性和细节质量，尤其是在大规模户外场景中。因此，论文提出了WeatherDiffusion框架，利用扩散先验理论，在内在空间中进行可控的天气编辑。该框架包括逆渲染器和正渲染器两个组件。
### Innovation
1. 利用扩散先验理论开发了逆渲染器，能够从输入图像中估计材质属性、场景几何和照明信息，以增强可控制性。2. 通过CLIP空间中的天气指示符插值实现了精细的天气控制。3. 提出了内在地图感知的注意力机制，提升了大规模户外场景中的空间对应和分解质量。4. 提供了合成和真实世界的数据集，包含38,000和18,000张不同天气条件下的图像，并标注了内在地图信息。
### Conclusion
WeatherDiffusion超越了现有基于像素空间编辑的方法、天气恢复方法以及渲染方法，展现出在自动驾驶等下游任务中提升检测和分割鲁棒性的潜力。
## 231. `cs.AI` - 一种统一的噪声-曲率视角下的训练失效问题 [PDF](https://arxiv.org/pdf/2509.19698), [HTML](https://arxiv.org/abs/2509.19698)
### Authors
Gunbir Singh Baveja,Alex Lewandowski,Mark Schmidt
### Background
训练失效是指在连续学习中，参数更新无法继续改善优化目标，导致随着时间推移学习问题的变化，模型的准确度停滞或下降的现象。现有研究通过赫舍尔秩、尖锐度级别、权重或梯度范数、梯度与参数比率以及单元符号熵等单一指标来预测训练失效，并未提供可靠的方法。
### Innovation
通过优化视角分析训练失效，引入了两个互补的指标：批次大小感知的梯度噪声边界和曲率波动控制边界，并将这两个指标结合，形成每层自适应噪声门限，对应于有效步长的预判性反应机制。据此，作者提出了一种步长调度策略，确保每个层的有效参数更新低于上述界定，以防训练失效。实验表明，该调度器可以提升之前方法（如串联ReLU（CReLU）、Wasserstein正则化器和L2权重衰减）维持的准确度。令人惊讶的是，该调度器还能生成一种不需要调优的步长衰减路径，能够模仿手动工程化的步长衰减策略。
### Conclusion
通过引入新的指标和调度策略，本文在优化机制下提供了训练失效的一种新颖统一视角，能够提高之前的连续学习方法的准确性和稳定性。
## 232. `cs.AI` - 使用概念学习数据集在大型语言模型中揭示隐含偏见 [PDF](https://arxiv.org/pdf/2510.01219), [HTML](https://arxiv.org/abs/2510.01219)
### Authors
Leroy Z. Wang
### Background
该研究介绍了一个概念学习任务的数据集，用于揭示大型语言模型中的隐含偏见。通过对上下文中的概念学习实验，研究发现语言模型可能对数量词有向上的单调性偏见；这种偏见在没有概念学习组件的直接提示测试中不那么明显。这表明，在上下文中的概念学习可以是一个发现语言模型中隐藏偏见的有效方法。
### Innovation
该论文提出了一种新的技术——在上下文中的概念学习实验，这种技术能够揭示大型语言模型中的隐含偏见。通过这种方法，研究发现语言模型在某些方面可能带有隐藏的偏见。
### Conclusion
在上下文中的概念学习可以有效地发现语言模型中的隐藏偏见。这种偏见在直接的提示测试中不那么明显，强化了在实际应用中考虑这种偏见的重要性。
## 233. `cs.AI` - 分布偏移下的弱到强泛化 [PDF](https://arxiv.org/pdf/2510.21332), [HTML](https://arxiv.org/abs/2510.21332)
### Authors
Myeongho Jeon,Jan Sobotka,Suhwan Choi,Maria Brbić
### Background
随着未来超人类模型变得越来越复杂，准确监督其行为可能超过人类的能力。近期研究表明，在这种情况下，弱模型可以有效地监督强模型，这种现象称为弱到强泛化。然而，研究发现简单的弱到强泛化在分布偏移情况下会失效，通常导致强模型的性能劣于其弱监督者。
### Innovation
提出了RAVEN，一种鲁棒的弱到强泛化框架，用于动态学习弱模型的最佳组合，以及强模型的参数。该框架展示了在图像分类、文本分类和偏好调整任务上的有效性。在分布外任务上，RAVEN的表现比其他基线方法高出30%以上，而在分布内任务上，其表现与现有方法相当或更好。此外，研究结果表明RAVEN会赋予更准确的弱模型更高的权重，显示了其自动识别可靠监督的能力。
### Conclusion
RAVEN框架通过动态学习最佳弱模型组合以提高跨分布泛化性能，实现了对分布偏移下弱到强泛化的鲁棒性，并且在多个任务上实现了优越的性能。
## 234. `cs.AI` - SaFiRe: Saccade-Fixation Reiteration with Mamba for Referring Image Segmentation [PDF](https://arxiv.org/pdf/2510.10160), [HTML](https://arxiv.org/abs/2510.10160)
### Authors
Zhenjie Mao,Yuhuan Yang,Chaofan Ma,Dongsheng Jiang,Jiangchao Yao,Ya Zhang,Yanfeng Wang
### Background
Referring Image Segmentation (RIS) 的目标是通过自然语言表达来分割图像中的目标对象。尽管最近的方法利用预训练的视觉骨干和更多的训练语料库取得了显著成果，但它们主要依赖于简单的表达方式——如“红色汽车”或“左边的女孩”等简短明确的名词短语。然而，这种简化常常使 RIS 变为关键词/概念匹配问题，限制了模型处理表达中指代歧义的能力。论文指出，真实世界中的挑战场景包括：具有多个实体并伴有上下文线索的指代性表达和未明确说明目标类别的类别隐含表达。
### Innovation
本文提出了一个名为 SaFiRe 的新框架，该框架模仿了人类的两阶段认知过程，首先是形成全球理解，然后通过详细检查进行细化。这通过 Mamba 的扫描-更新机制自然支持，与阶段性设计相契合，从而实现高效的多轮次细化并且具有线性复杂性。此外，还引入了一个新的基准（aRefCOCO），用于评估在具有歧义性的表达下 RIS 模型的表现。
### Conclusion
在标准数据集和新提出的数据集上的大量实验显示了 SaFiRe 在相比最先进的基线方法中的优越性。
## 235. `cs.AI` - SARVLM: SAR成像中的语义理解和目标识别的视觉语言基础模型 [PDF](https://arxiv.org/pdf/2510.22665), [HTML](https://arxiv.org/abs/2510.22665)
### Authors
Qiwei Ma,Zhiyu Wang,Wang Liu,Xukun Lu,Bin Deng,Puhong Duan,Xudong Kang,Shutao Li
### Background
合成孔径雷达(SAR)因其全天候成像能力而成为关键的成像模态。尽管最近在自监督学习和掩码图像建模方面的进展促进了SAR基础模型的发展，但这些方法主要关注低级视觉特征，而忽视了SAR图像中的多模态对齐和零样本目标识别。
### Innovation
该研究构建了SARVLM-1M，一个由多个现有数据集的图像-文本对组成的大型视觉语言数据集，并提出了一种领域迁移训练策略，以减少自然图像和SAR图像之间的巨大差距。在此基础上，发展了SARVLM，这是第一个针对SAR的视觉语言基础模型（VLM），包括SARCLIP和SARCap。SARVLM采用提出的领域迁移策略下的视觉语言对比目标进行训练，实现SAR图像和文本描述的桥梁。广泛的实验验证了SARVLM在图像文本检索、零样本分类、语义定位和图像字幕方面的优越特征提取和解释性能，超过了最先进的VLMs并提升了SAR语义理解。
### Conclusion
SARVLM在图像文本检索、零样本分类、语义定位和图像字幕方面表现出优越的特征提取和解释性能，并在SAR语义理解方面取得了进展。
## 236. `cs.AI` - 农业中轻量级异常检测的模块化现场解决方案以实现可持续的营养管理 [PDF](https://arxiv.org/pdf/2509.12247), [HTML](https://arxiv.org/abs/2509.12247)
### Authors
Abigail R. Cohen,Yuming Sun,Zhihao Qin,Harsh S. Muriki,Zihao Xiao,Yeonju Lee,Matthew Housley,Andrew F. Sharkey,Rhuanito S. Ferrarezi,Jing Li,Lu Gan,Yongsheng Chen
### Background
作物生长和资源消耗（例如氮和能量）的有效营养管理至关重要。当前的方法需要较长的分析时间，无法实现实时优化；而影像技术可以实现快速表型分析，但可能在资源受限的情况下无法部署。
### Innovation
本文提出了一种灵活的分层流水线，用于异常检测和状态估计（含水量，干重，组织营养成分），并进行了能耗分析，涉及从效率和准确性的不同范围的方法。通过多光谱影像（MSI）和营养流失实验，研究展示了一种自编码器（AE）提前警告方法，以及复杂度不同的两个状态估计模块：植被指数特征配以机器学习（随机森林，RF）和未经处理的全图像深度学习（视觉变换器，ViT）。结果展示了高效的异常检测（在移植9天后检测到73%的T3样本样品），并且能耗明显低于浪费氮素的潜热。状态估计模块体现了权衡，ViT在磷和钙的估计上优于RF，尽管成本更高。
### Conclusion
通过我们的模块化流水线，本研究为农业边沿诊断和实际的农业可持续性提供了机会，展示出在营养管理中实现现场解决方案的实际应用潜力。
## 237. `cs.AI` - LightMem: 轻量级且高效的增强生成记忆系统 [PDF](https://arxiv.org/pdf/2510.18866), [HTML](https://arxiv.org/abs/2510.18866)
### Authors
Jizhan Fang,Xinle Deng,Haoming Xu,Ziyan Jiang,Yuqi Tang,Ziwen Xu,Shumin Deng,Yunzhi Yao,Mengru Wang,Shuofei Qiao,Huajun Chen,Ningyu Zhang
### Background
尽管大型语言模型（LLMs）具有卓越的能力，但在处理动态和复杂环境时，它们往往难以有效利用历史交互信息。现有的记忆系统虽然引入了持久性信息存储、检索和利用机制，但是通常会带来显著的时间和计算开销。
### Innovation
本文介绍了一种名为LightMem的新记忆系统，它在性能和效率之间达到了平衡。LightMem受到了人类记忆模型的启发，将记忆分为三个互补的阶段：首先是基于认知的感官记忆，通过轻量级压缩快速过滤无关信息，并按话题对信息进行分组；其次是具有话题感知的短期记忆，将这些话题基组组织和总结为结构化访问的内容；最后是睡眠时间更新的长期记忆，采用离线过程将合并与在线推理脱钩。
### Conclusion
在LongMemEval和LoCoMo上，使用GPT和Qwen底层，LightMem在问答准确性、总令牌使用量和API调用次数上都超过了强大的基线模型，分别提高了最高7.7% / 29.3%的问题回答准确性，减少了总数最高38x / 20.9x的令牌使用量和30x / 55.5x的API调用次数，同时在线测试时间的开销更低，最多实现了106x / 117x的令牌减少和159x / 310x的API调用减少。
## 238. `cs.AI` - DensiCrafter：受物理约束的自支撑空心结构的生成与制造 [PDF](https://arxiv.org/pdf/2511.09298), [HTML](https://arxiv.org/abs/2511.09298)
### Authors
Shengqi Dang,Fu Chai,Jiaxin Li,Chao Yuan,Wei Ye,Nan Cao
### Background
3D生成模型的兴起使得能够从多模态输入（如文本或图像）中自动合成3D几何和纹理。然而，这些方法往往忽略了物理约束和制造可行性考虑。本文旨在解决生成同时轻量化和自支撑的3D设计这一挑战。
### Innovation
本文提出了DensiCrafter框架，通过优化密度场生成轻量化且自支撑的3D空心结构。该框架从Trellis生成的粗略体素网格出发，将其解释为连续密度场进行优化，并引入了三个可微、物理受限且无需仿真的损失项。此外，一种质量正则化限制了不必要的材料，而限定优化域则保持外表面不变。该方法无需对预训练的Trellis基模型进行任何架构上的修改。实验证明，与现有基准相比，该方法在文本到3D任务中材料质量减少了最多43%，并且提高了稳定性并保持了高几何保真度。
### Conclusion
真实世界的3D打印实验证实，所提出的设计能够可靠地制造并能够自支撑。
## 239. `cs.AI` - PointNSP：基于下一步尺度LOD预测的自回归3D点云生成 [PDF](https://arxiv.org/pdf/2510.05613), [HTML](https://arxiv.org/abs/2510.05613)
### Authors
Ziqiao Meng,Qichao Wang,Zhiyang Dou,Zixing Song,Zhipeng Zhou,Irwin King,Peilin Zhao
### Background
尽管基于扩散的方法在质量上表现优异，但自回归点云生成长期以来一直落后。性能差距源于自回归模型对自然无序的点集施加了人为的顺序约束，使得形状生成需要依次进行局部预测。这种顺序偏向强调局部连续性，却削弱了模型捕捉远距离依赖的能力，影响其执行全局结构性质，如对称性、一致拓扑和大尺度几何规律。
### Innovation
我们提出了一个从粗到细的生成框架PointNSP，该框架在低分辨率下保持全局形状结构，并通过下一尺度预测范式逐步在更高尺度上精化细粒度几何。这种多尺度分解使自回归目标与点集的排列不变性质相吻合，实现了丰富的尺度内交互，同时避免了固定顺序的脆弱性。
### Conclusion
PointNSP在ShapeNet实验中首次在自回归范式中实现了最高的生成质量，同时在参数、训练和推断效率上超越了强大的基于扩散的基线模型。特别是在密集生成8,192个点时，PointNSP的优势更加突出，突显了其扩展潜力。
## 240. `cs.AI` - 基于上下文学习中的任务导向信息移除机制 [PDF](https://arxiv.org/pdf/2509.21012), [HTML](https://arxiv.org/abs/2509.21012)
### Authors
Hakaze Cho,Haolin Yang,Gouki Minegishi,Naoya Inoue
### Background
在-context Learning（ICL）是基于现代语言模型（LMs）的一种新兴的少量样本学习范式，但其内部机制尚不明确。这项研究通过信息移除的新视角来探讨ICL机制。
### Innovation
该研究首次通过信息移除的视角揭示了ICL的工作原理。具体来说，在零样本情况下，LMs会生成包含所有可能任务信息的非选择性表示，导致它们产生任意输出，而忽视了目标任务，从而导致近乎零的准确度。通过引入低秩过滤器来选择性地去除特定信息，LMs可以更准确地专注于目标任务。通过测量精心设计的标准，研究表明少量样本ICL可以模拟这种任务导向的信息移除过程，选择性地去除冗余信息，从而基于演示改进输出，这是ICL的关键机制。此外，研究还识别出导致信息移除操作的关键注意力头，称为去噪头，切断这些头将显著降低ICL的效果，特别是在少量样本演示中缺少正确标签时。
### Conclusion
这些发现表明，信息移除机制及其去噪头对于ICL至关重要，验证了其在ICL中的核心作用。
## 241. `cs.AI` - 工业缺陷检测的自动化神经架构设计 [PDF](https://arxiv.org/pdf/2510.06669), [HTML](https://arxiv.org/abs/2510.06669)
### Authors
Yuxi Liu,Yunfeng Ma,Yi Tang,Min Liu,Shuai Jiang,Yaonan Wang
### Background
工业表面缺陷检测(SDD)对于确保产品质量和制造可靠性至关重要。由于表面缺陷的形状和大小多样，SDD面临两大主要挑战：类别内差异和类别间相似性。现有方法主要依赖人工设计模型，需要大量试验和错误，并且往往难以有效解决这两个挑战。
### Innovation
我们提出了AutoNAD，这是用于SDD的自动化神经架构设计框架，它联合搜索卷积、变换器和多层感知器。这种混合设计能够捕捉细粒度的局部变化和长距离的语义上下文，同时解决两个关键挑战，减少人工网络设计的成本。为了支持这种多样搜索空间的高效训练，AutoNAD引入了交叉权重共享策略，加速主网络（supernet）的收敛，提高子网络（subnet）的性能。此外，还集成了一个可搜索的多级特征聚合模块（MFAM），以增强多尺度特征学习。此外，AutoNAD还结合了延迟感知先验，以指导选择高效的架构。
### Conclusion
AutoNAD在三个工业缺陷数据集上进行了有效性验证，并进一步应用于缺陷成像和检测平台。相关代码可以在以下网址获取：this https URL.
## 242. `cs.AI` - 思考可视化，文本推理：ARC中的视觉语言协同作用 [PDF](https://arxiv.org/pdf/2511.15703), [HTML](https://arxiv.org/abs/2511.15703)
### Authors
Beichen Zhang,Yuhang Zang,Xiaoyi Dong,Yuhang Cao,Haodong Duan,Dahua Lin,Jiaqi Wang
### Background
当前的前沿基础模型，如GPT-5和Grok 4，在从少量示例中推断出结构化变换规则方面仍然存在问题，这是人类智能的关键特征。现有的ARC-AGI数据集为检验模型这种能力提供了严格的测试平台，要求概念规则归纳和转移至新任务。多数现有方法将ARC-AGI视为纯粹的文字推理任务，而人类在解决这类谜题时非常依赖视觉抽象。不过，初步实验显示，将ARC-AGI网格直接转换为图像反而降低了性能，这揭示了一个悖论：视觉和语言在不同的推理阶段具有互补的优势。
### Innovation
提出了两种协同策略：(1) 视觉语言协同推理(VLSR)，分解ARC-AGI任务为模态对齐的子任务；(2) 模态切换自我校正(MSSC)，利用视觉验证基于文本的推理以进行内在错误校正。实验表明，这一方法在多种顶级模型和ARC-AGI任务上相比仅基于文本的方法提高了4.33%的表现，表明在未来基础模型中统一视觉抽象与语言推理是实现一般化的人类智能的关键步骤。
### Conclusion
我们的研究结果表明，将视觉抽象与语言推理相结合是实现未来基础模型可推广的人类智能的关键步骤。
## 243. `cs.AI` - 欺骗立体匹配：针对自动驾驶双目深度估计的物理对抗攻击 [PDF](https://arxiv.org/pdf/2511.14386), [HTML](https://arxiv.org/abs/2511.14386)
### Authors
Kangqiao Zhao,Shuo Huai,Xurui Song,Jun Luo
### Background
虽然用于自动驾驶感知的深度神经网络模型已被证实对对抗样本十分脆弱，已知攻击大多使用2D图案并主要针对单目感知系统。因此，立体视觉下的基于物理的对抗样本（PAEs）在双目深度估计中的有效性尚未得到充分研究。
### Innovation
论文提出了一种针对立体匹配模型的3D物理对抗攻击方法，这种方法使用全局伪装纹理的3D PAE，而不是局部的2D图案，从而确保在不同视角下视觉一致性与攻击效果的结合。同时，还提出了一种新的3D立体匹配渲染模块，让PAE能与双目视觉的真实世界位置和方向对齐。此外，提出了一种新的无缝合并攻击，通过细腻的PAE优化无缝融合目标到环境，显著增强了隐身性和致命性。
### Conclusion
大量评估表明，本研究提出的PAE能够成功骗过立体匹配模型，产生错误的深度信息。
## 244. `cs.AI` - 通过野外谈话头视频的面部时间微动态分析进行被动痴呆筛查 [PDF](https://arxiv.org/pdf/2511.13802), [HTML](https://arxiv.org/abs/2511.13802)
### Authors
Filippo Cenacchi,Longbing Cao,Mitchell McEwan,Deborah Richards
### Background
现有资源主要集中在言语或剧本访谈，这限制了其在临床之外的应用，并且预测与语言和转录紧密相关。大多数现有的痴呆筛查方法依赖于言语或书面记录，需要临床或研究者的主动干预。
### Innovation
该研究开发了一种面部时间微动态分析方法，通过分析自然谈话中无言语的面部行为，如眨眼动态、小嘴和下巴运动、视线变化和微妙的头部调整，来检测早期认知变化。通过这种分析，转化了微小面部运动的时间序列，并将它们转化为可解释的面部微动态时间序列，从而可以进行大规模、无剧本、无干预的视频分析，适用于不同设备、话题和文化。此外，研究人员还构建了一个新的公开数据集YT DemTalk，包含300个视频片段，用于测试模型。
### Conclusion
在YT DemTalk数据集上，通过消融实验确定了视线波动和口部/下颌动态是最具信息性的提示，并建立了轻量级浅层分类器，这些分类器在痴呆预测性能上达到了AUROC 0.953，平均召回率0.961，F1分数0.851及准确率0.857。这表明，通过面部时间微动态分析，可以在无言语的情况下进行痴呆筛查，具有很强的诊断潜力。
## 245. `cs.AI` - 药物发现前沿的扩散模型：生成小分子与治疗肽的综述 [PDF](https://arxiv.org/pdf/2511.00209), [HTML](https://arxiv.org/abs/2511.00209)
### Authors
Yiquan Wang,Yahui Ma,Yuhan Chang,Jiayao Yan,Jialin Zhang,Minnuo Cai,Kai Wei
### Background
随着扩散模型在生成建模中的崛起，它们正有望革新传统的缓慢且昂贵的药物发现过程。本文综述了扩散模型在设计两种主要治疗模式（小分子和治疗性肽）中的应用。
### Innovation
本文系统比较了扩散模型在小分子和治疗性肽设计中的应用，并深入分析了它们如何适应不同的分子表示、化学空间和设计目标。
### Conclusion
尽管小分子和治疗肽在设计中存在不同的挑战，但两者都面临着数据质量不足、评分功能不准确以及需要实验验证等共同难题。未来，扩散模型的潜力将通过解决这些特定于分领域的缺口，并将其集成到自动化闭环的Design-Build-Test-Learn (DBTL) 平台中得以释放，从而从单纯的化学探索转向对新型治疗性药物的按需工程改造。
## 246. `cs.AI` - 在Transformer模型中实现逆排列学习的不可能性 [PDF](https://arxiv.org/pdf/2509.24125), [HTML](https://arxiv.org/abs/2509.24125)
### Authors
Rohan Alur,Chris Hays,Manish Raghavan,Devavrat Shah
### Background
本文研究了解码器仅有的Transformer模型在给定一个排列和该排列应用后的字符串时，反向学习出原始（“规范”）字符串的问题。作者认为，这个问题可以作为一个自然的稳健性属性，适用于多种推理任务，如长上下文检索、多项选择问答和在上下文学习中。
### Innovation
主要贡献在于证明了这一点：具有任意深度的解码器仅有的Transformer模型无法完成该任务。这一结论关注的是解码器仅有的Transformer模型的表达能力，与训练动力学或样本复杂度无关。文章提出了两种可行的结构，其中一种突显了因果注意力掩码的基本作用，并揭示了编码器-解码器Transformer和更流行的解码器仅有的架构在表达性上的差距。第二种则是更引人惊讶的结果：通过在输入中添加“空白标记”便可以使逆排列学习成为可能。文章猜测，这可能暗示一种替代机制，即使这些中间“思考”标记没有任何有意义的语义信息（例如，其中包含的中间计算结果），链式思考提示或更广泛的中间“思维”token也有可能在大型语言模型中促进推理。
### Conclusion
论文证明了解码器仅有的Transformer模型无法实现逆排列学习的不可能性，并讨论了这一结论对理解不同类型的Transformer模型表达能力的意义。还提出了两种使逆排列学习成为可能的结构，揭示了解码器仅有的架构与编码器-解码器架构之间的差距，并提出了一种可能的关于大型语言模型推理机制的新观点。
## 247. `cs.AI` - 序列迷失：图理魈模型的不变性和泛化能力 [PDF](https://arxiv.org/pdf/2511.10234), [HTML](https://arxiv.org/abs/2511.10234)
### Authors
Daniel Herbst,Lea Karbevska,Divyanshu Kumar,Akanksha Ahuja,Fatemeh Gholamzadeh Nasrabadi,Fabrizio Frasca
### Background
基于大语言模型（LLMs）的图推理器虽然有潜力，但在处理图表示的对称性方面缺乏内置不变性。在对图进行序列化操作后，LLMs 可能在节点重新索引、边重排序或格式更改时产生不同输出，这提出了稳定性的担忧。本文系统地分析了这些影响，研究了微调对编码敏感性以及在未见任务上的泛化能力的影响。
### Innovation
本文提出了一种原理分解法，将图序列化分解为节点标签、边编码和语法，并在全面的基准测试套件上评估 LLM 对这些因素变体的鲁棒性。此外，还贡献了一组新颖的谱任务，以进一步评估微调理器的泛化能力。研究表明，更大的（非微调）模型更具鲁棒性。微调可以降低对节点重新标签的敏感性，但可能增加对结构和格式变化的敏感性，且不一定能一致地提高在未知任务上的性能。
### Conclusion
研究结果表明，不进行微调的更大模型更具鲁棒性。微调虽然可以降低对节点重新标签的敏感性，但可能会增加对结构和格式变化的敏感性，且不一定能提升在未见过的任务上的性能表现。
## 248. `cs.AI` - TimeViper: 一种用于高效理解长视频的混合Mamba-Transformer视觉-语言模型 [PDF](https://arxiv.org/pdf/2511.16595), [HTML](https://arxiv.org/abs/2511.16595)
### Authors
Boshen Xu,Zihan Xiao,Jiaze Li,Jianzhong Ju,Zhenbo Luo,Jian Luan,Qin Jin
### Background
处理长视频需要同时具备高效的模型架构和有效的机制来处理扩展的时序上下文。现有的模型在处理长视频时存在信息冗余和理解能力下降的问题。
### Innovation
TimeViper采用了混合的Mamba-Transformer骨干，结合了状态空间模型的高效性和注意力机制的表达能力。这一设计揭示了视觉信息向文本信息的层级聚合现象，并提出了TransV模块，实现视觉信息向指令信息的传输和压缩，同时保持多模态理解能力。
### Conclusion
 extensive experiments demonstrate that TimeViper与最先进的模型相比具有竞争力并且能够处理超过10,000帧的长视频。此外，该工作还分析了Mamba和Transformer层的行为，为进一步理解混合模型提供了新的见解。
## 249. `cs.AI` - ConceptGuard: 通过多模态风险检测在文本和图像到视频生成中实现主动安全 [PDF](https://arxiv.org/pdf/2511.18780), [HTML](https://arxiv.org/abs/2511.18780)
### Authors
Ruize Ma,Minghong Cai,Yilei Jiang,Jiaming Han,Yi Feng,Yingshui Tan,Xiaoyong Zhu,Bo Zhang,Bo Zheng,Xiangyu Yue
### Background
近年来，视频生成模型的进步使得能够从结合文本和图像的多模态提示中生成高质量的视频。尽管这些系统增强了可控性，但它们也引入了新的安全风险，因为有害内容可能源自单模态或它们的交互。现有的安全方法通常是仅基于文本的，需要事先知道风险类别，或者作为生成后的监察机制，难以主动缓解这种组成性的、多模态的风险。
### Innovation
本文提出了ConceptGuard，这是一种统一的风险防护框架，用于主动检测和缓解多模态视频生成中的不安全语义。ConceptGuard分为两个阶段：首先，对比检测模块通过将融合的图像-文本输入映射到结构化的概念空间中来识别潜在的安全风险；其次，语义压制机制通过在提示的多模态调优过程中干预以引导生成过程远离不安全的概念。为了支持该框架的发展和严格的评估，作者还引入了两个新的基准：ConceptRisk，一个大规模数据集，用于训练多模态风险，以及T2VSafetyBench-TI2V，首个适应文本-图像到视频（TI2V）安全设置的基准。Experiments on both benchmarks show that ConceptGuard consistently outperforms existing baselines, achieving state-of-the-art results in both risk detection and safe video generation.
### Conclusion
多种形式的实验表明，ConceptGuard在风险检测和安全视频生成方面均表现出优异的结果，全面超越了现有的基线系统。同时，ConceptGuard框架的支持代码已在指定的链接处提供。
## 250. `cs.AI` - CLLMRec: LLM-powered Cognitive-Aware Concept Recommendation via Semantic Alignment and Prerequisite Knowledge Distillation [PDF](https://arxiv.org/pdf/2511.17041), [HTML](https://arxiv.org/abs/2511.17041)
### Authors
Xiangrui Xiong,Yichuan Lu,Zifei Pan,Chang Sun
### Background
MOOCs的快速增长为个性化学习带来了显著挑战，其中概念推荐至关重要。现有方法通常依赖异构信息网络或知识图谱来捕捉概念关系，并结合知识追踪模型来评估学习者的认知状态。然而，这些方法在依赖高质量的结构化知识图谱方面存在局限性，而这些高质量的结构化知识图谱在实际教育场景中往往稀缺。
### Innovation
本文提出了一种新的框架CLLMRec，利用大型语言模型通过语义对齐和先决知识提炼两大协同技术支柱来实现认知意识的概念推荐。语义对齐组件通过编码学习者和概念的非结构化文本描述来构建统一的表示空间。先决知识提炼通过教师-学生架构，由大型教师LLM（作为先验知识感知组件）从其内在的知识世界中提取概念先决条件关系，并将这些信息提炼成软标签来训练高效的学生排序器。
### Conclusion
基于这些基础，我们的框架引入了一种精细排名机制，通过深度知识追踪明确建模学习者的实时认知状态，确保建议既在结构上合理，又在认知上合适。在两个真实世界的MOOC数据集上的广泛实验表明，CLLMRec在多个评估指标上都显著优于现有基线方法，验证了其生成真正认知意识和个性化的概念推荐的有效性，无需依赖显式的结构先验。
## 251. `cs.AI` - DR Tulu: 使用演变评分标准的强化学习进行深度研究 [PDF](https://arxiv.org/pdf/2511.19399), [HTML](https://arxiv.org/abs/2511.19399)
### Authors
Rulin Shao,Akari Asai,Shannon Zejiang Shen,Hamish Ivison,Varsha Kishore,Jingming Zhuo,Xinran Zhao,Molly Park,Samuel G. Finlayson,David Sontag,Tyler Murray,Sewon Min,Pradeep Dasigi,Luca Soldaini,Faeze Brahman,Wen-tau Yih,Tongshuang Wu,Luke Zettlemoyer,Yoon Kim,Hannaneh Hajishirzi,Pang Wei Koh
### Background
现有的深度研究模型通过可验证的短期问答任务进行强化学习训练，难以适应现实中的长期研究任务。这些模型通常专注于生成简洁且可验证的答案，缺乏处理复杂、长篇回答的能力。
### Innovation
提出了面向深度研究的强化学习与演变评分标准（Reinforcement Learning with Evolving Rubrics, RLER），该方法通过构建和维护与策略模型共同进化的评分标准，提供更具有区分性和政策导向的反馈，使模型能够处理开放性的、长篇幅的研究任务。
### Conclusion
通过RLER训练，开发了DR Tulu-8B模型，这是首个专门针对开放性、长篇深度研究的任务进行训练的开放模型。该模型在四项科学、医疗和一般领域的长期深度研究基准测试中表现优异，且在规模和成本方面更具优势。研究者还提供了数据、模型和代码资源，以促进后续研究的发展。
## 252. `cs.AI` - 通过树组双意识搜索和优化实现的对抗攻击-防御共生演化以实现LLM安全对齐 [PDF](https://arxiv.org/pdf/2511.19218), [HTML](https://arxiv.org/abs/2511.19218)
### Authors
Xurui Li,Kaisong Song,Rui Zhu,Pin-Yu Chen,Haixu Tang
### Background
大型语言模型（LLMs）在web服务中迅速发展，提供了前所未有的能力，但同时也加剧了社会风险。现有研究大多关注孤立的 jailbreak 攻击或静态防御，忽略了在现实web环境中不断演变的威胁和保护之间动态的相互作用。
### Innovation
我们提出了ACE-Safety（Adversarial Co-Evolution for LLM Safety），这是一种新的框架，通过将两个关键创新步骤无缝集成来联合优化攻击和防御模型：（1）具有组意识的策略引导蒙特卡洛树搜索（GS-MCTS），它有效地探索jailbreak策略以发现漏洞并生成多样化的对抗样本；（2）对抗性课程树意识组策略优化（AC-TGPO），该过程通过基于课程的强化学习共同训练攻击和防御LLM，使它们能够相互强化并变得 robust。
### Conclusion
我们的方法在多个基准测试中的评估表明，它优于现有的攻击和防御方法，并提供了一条开发可以持续支持负责任人工智能生态系统的LLMs的可行路径。
## 253. `cs.AI` - UniGame:转变为自身对手的统一多模态模型 [PDF](https://arxiv.org/pdf/2511.19413), [HTML](https://arxiv.org/abs/2511.19413)
### Authors
Zhaolong Su,Wang Lu,Hao Chen,Sharon Li,Jindong Wang
### Background
统一多模态模型（UMMs）在理解和生成任务上都表现出色，但由于其结构矛盾，理解倾向使用紧凑的嵌入表示，而生成则需要丰富的重构表示。这种结构性矛盾导致决策边界不一致、跨模态一致性降低，并使其在分布和对抗性扰动下更为脆弱。
### Innovation
提出了UniGame，一个自对抗后训练框架，直接针对UMMs中的不一致性问题。通过在共享的标记接口处应用轻量级扰动器，UniGame使生成分支能够主动寻求并挑战脆弱的理解，从而使模型成为其自身的对手。该框架对模型架构无特定要求，引入的额外参数少于1%，且与现有后训练方法兼容。
### Conclusion
实验结果表明，UniGame显著提高了模型的一致性（+4.6%）、理解能力（+3.6%）、生成能力（+0.02）、以及对分布外数据和对抗性扰动的鲁棒性（在NaturalBench上+4.8%，在AdVQA上+6.2%）。这种框架为提高未来多模态基础模型的一致性、稳定性和统一能力提供了一般且有效的方法。
## 254. `cs.AI` - PrefixGPT: Prefix Adder Optimization by a Generative Pre-trained Transformer [PDF](https://arxiv.org/pdf/2511.19472), [HTML](https://arxiv.org/abs/2511.19472)
### Authors
Ruogu Ding,Xin Ning,Ulf Schlichtmann,Weikang Qian
### Background
前缀加法器在计算密集型应用中因其高速度而被广泛应用。然而，由于严格的设计规则和设计空间的指数级增长，设计优化的前缀加法器极具挑战性。
### Innovation
我们提出了PrefixGPT，这是一种生成式预训练变换器（GPT），可以直接从零开始生成优化的前缀加法器。该模型采用自定义的仅解码器Transformer架构，先行在随机合成的有效前缀加法器语料库上进行预训练以学习设计规则，然后微调以探索设计空间并优化设计质量。相比现有工作，PrefixGPT不仅找到了一个改进了7.7%面积延迟积（ADP）的新最优设计，而且还展示了优越的探索质量，将平均ADP降低了高达79.1%，这表明GPT风格模型有可能首先掌握复杂的硬件设计原则，然后应用于更高效的优化设计。
### Conclusion
PrefixGPT展示了生成式预训练Transformer在复杂硬件设计中的潜力，特别是优化前缀加法器方面。其不仅能够找到新的最优设计，还能够有效探索设计空间，显著降低面积延迟积。
## 255. `cs.AI` - 具有学习艾乐托瑞克不确定性感知深度学习框架的涡扇发动机剩余使用寿命预测 [PDF](https://arxiv.org/pdf/2511.19124), [HTML](https://arxiv.org/abs/2511.19124)
### Authors
Krishang Sharma
### Background
在航空航天的预诊技术中，准确的剩余使用寿命（RUL）预测结合不确定性量化仍然是一个关键挑战。现有基于CMAPSS的方法尚未探索通过概率建模直接学习不确定性的方法。本文针对这个问题进行了深入研究。
### Innovation
本文提出了一种新颖的感知不确定性的深度学习框架，通过概率建模直接学习不确定性，结合多尺度Inception块进行时间模式提取，双向长短期记忆网络进行序列建模，以及同时作用于传感器和时间维度的双层注意力机制。模型的创新在于其贝叶斯输出层，能够同时预测RUL的均值和方差，使得模型能够学习数据固有的不确定性。此外，还采用了条件感知聚类、小波去噪和智能特征选择进行彻底的预处理。
### Conclusion
实验在NASA CMAPSS基准数据集（FD001-FD004）上验证，显示了具有竞争力的整体性能，并在关键区域（RUL <= 30周期）实现了突破性的性能改进，与传统方法相比提高了25-40个百分点，且确立了新的安全预测基准。所学的不确定性提供了95%置信区间，覆盖范围为93.5%至95.2%，从而使风险感知的维护计划成为可能，超越了CMAPSS文献中的以往成就。
## 256. `cs.AI` - Pistachio: 向合成、平衡且长格式的视频异常基准迈进 [PDF](https://arxiv.org/pdf/2511.19474), [HTML](https://arxiv.org/abs/2511.19474)
### Authors
Jie Li,Hongyi Cai,Mingkang Dong,Muxin Pu,Shan You,Fei Wang,Tao Huang
### Background
自动检测视频中的异常事件对于现代自主系统至关重要，但现有的视频异常检测（VAD）基准测评缺乏场景多样性、均衡的异常覆盖和所需的时间复杂性，这使得评估真实场景下的性能变得不可靠。与此同时，社区正越来越多地转向视频异常理解（VAU），这需要更深层次的语义和因果推理，但由于需要大量的手动注释工作量，使得基准测评变得困难。
### Innovation
本研究介绍了一种名为Pistachio的新VAD/VAU基准，通过一个受控的、基于生成的管道构建，使用了最新的视频生成模型作为基础，精确控制场景、异常类型和时间叙事，有效消除了网络收集数据集的偏见和限制。该管道集成了基于场景的异常分配、多步故事线生成和具有时间一致性的长格式合成策略，生成了几乎无需人工干预的41秒连贯视频。
### Conclusion
广泛的实验展示了Pistachio的规模、多样性和复杂性，揭示了现有方法的新挑战，对动态和多事件异常理解提出了未来的研究动机。
## 257. `cs.AI` - TREASURE: 一种基于Transformer的基础模型，用于高流量交易理解 [PDF](https://arxiv.org/pdf/2511.19693), [HTML](https://arxiv.org/abs/2511.19693)
### Authors
Chin-Chia Michael Yeh,Uday Singh Saini,Xin Dai,Xiran Fan,Shubham Jain,Yujie Fan,Jiarui Sun,Junpeng Wang,Menghai Pan,Yingtong Dou,Yuzhong Chen,Vineeth Rakesh,Liang Wang,Yan Zheng,Mahashweta Das
### Background
支付网络构成了现代商业的骨干，每日产生大量交易记录。合理地建模这些数据可以支持异常行为侦测和消费者层面的洞察，以提供个性化的体验，最终改善人们的生活。
### Innovation
TREASURE是一种专为交易数据设计的多功能变压器基础模型，能够同时捕捉消费者行为和支付网络信号（例如响应代码和系统标志），提供全面的必要信息，如准确的推荐系统和异常行为侦测。TREASURE具有三项关键技术能力：1）带有静态和动态属性专用子模块的输入模块，支持更高效的训练和推理；2）高效的预测高基数分类属性的训练范式；3）作为独立模型提高了111%的异常行为检测性能，并作为嵌入提供者提升了推荐模型104%。
### Conclusion
通过对广泛的消融研究、与生产模型的基准测试和案例研究，本研究表明TREASURE在异常行为侦测和推荐系统增强方面表现优异，提供了丰富的开发TREASURE的经验知识。
## 258. `cs.AI` - TiCT: 一种基于合成数据预训练的时间序列分类基础模型 [PDF](https://arxiv.org/pdf/2511.19694), [HTML](https://arxiv.org/abs/2511.19694)
### Authors
Chin-Chia Michael Yeh,Uday Singh Saini,Junpeng Wang,Xin Dai,Xiran Fan,Jiarui Sun,Yujie Fan,Yan Zheng
### Background
时间序列数据的广泛存在对通用基础模型提出了强烈需求，特别是在分类任务中更为明显，但由于需要大量标签数据，开发分类模型仍然是一项重大挑战。具有上下文学习能力的模型能够通过少量示例快速适应新任务，减少大量重新训练的需求，但大规模时间序列模型的研究主要集中在预测上，缺乏面向分类且无需要微调的一般性方法。
### Innovation
本文引入了TiCT（Time-series in-Context Transformer）模型，这是一种仅在合成数据上预训练的Transformer模型，用于执行上下文中的分类任务。其主要技术贡献包括：1) 一种新的架构，配备了可扩展的基于位的标签编码和处理任意数量类别的特殊输出注意机制；2) 一种结合了Mixup启发式的数据增强预训练框架，用于提高泛化能力和噪声不变性。
### Conclusion
通过在UCR档案上的广泛评估，TiCT在无微调的情况下实现了与最新监督方法相当的性能，在推理过程中仅使用上下文示例，而无需更新任何模型权重，从而解决了时间序列分类中的关键问题。
## 259. `cs.AI` - 人类专家对生成式AI在南半球国家STEAM教育情境化中的评估 [PDF](https://arxiv.org/pdf/2511.19482), [HTML](https://arxiv.org/abs/2511.19482)
### Authors
Matthew Nyaaba,Macharious Nabang,Patrick Kyeremeh,Ibrahim Nantomah,Collins Owusu-Fordjour,Martin Ako,Bismark Nyaaba Akanzire,Kassim Korah Nantomah,Cecilia Issaka,Xiaoming Zhai
### Background
本研究探讨了人类专家如何评估生成式AI（GenAI）在南半球地区的STEAM教育中的情境化能力，尤其是在加纳的应用情况。研究采用聚合混合方法设计，四个STEAM专家评估了GenAI生成的带有定制文化响应式教案规划工具(CRLP)的示范课程计划，并将其与加纳国家课程与评估委员会(NaCCA)的标准课程计划进行了比较。
### Innovation
该研究创新性地采用混合方法（定量和定性结合），使用CRLP工具来评估GenAI生成的教案，并通过文化响应性教学评价量表对这些教案进行了定量评级。定量分析侧重于偏见意识、文化代表性、情境相关性、语言敏感性和教师作用等多个维度。定性分析则揭示了GenAI在处理文化适宜性和教学适宜性方面的优势和不足。研究结果表明，当与CRLP工具结合使用时，GenAI能够支持情境化的STEAM教育，尤其是在链接抽象的课程标准与学习者的文化知识、社区实践和日常生活经验方面的优势。
### Conclusion
研究发现，尽管GenAI生成的教案在文化敏感性和教学响应性方面得分更高，但在表现加纳的文化多样性方面存在局限性，尤其是在数学和计算机科学中文化细微差别不足。研究强调了持续教师干预、社区参与和AI输出文化调适的重要性。未来工作应包括课堂试验、扩大专家参与以及利用本土语言语料库对模型进行微调，以增强南半球背景下文化的忠实性。
## 260. `cs.AI` - LLMs for Automated Unit Test Generation and Assessment in Java: The AgoneTest Framework [PDF](https://arxiv.org/pdf/2511.20403), [HTML](https://arxiv.org/abs/2511.20403)
### Authors
Andrea Lops,Fedelucio Narducci,Azzurra Ragone,Michelantonio Trizio,Claudio Bartolini
### Background
单元测试是软件开发中的一个重要但资源密集的步骤，确保单独的代码单元正确运行。本文介绍了一个自动评估框架AgoneTest，用于评估大型语言模型（LLM）生成的Java单元测试。AgoneTest的目标不是提出新的测试生成算法，而是通过标准化的端到端评估管道，支持研究人员和开发人员在现实条件下比较不同的LLM和提示策略。
### Innovation
介绍了Classes2Test数据集，该数据集将要测试的Java类映射到相应的测试类，并且引入了一个框架，该框架结合了高级评估指标，如变异分数和测试异味，以进行全面评估。实验结果显示，在生成的测试能够编译的情况下，LLM生成的测试可以与或超过人工编写的测试在覆盖率和缺陷检测方面的性能。此外，增强的提示策略也提高了测试质量。
### Conclusion
AgoneTest明确了LLM在软件测试中的潜在价值，并为未来模型设计、提示工程和测试实践改进提供了见解。
## 261. `cs.CL` - Harmonic Token Projection (HTP): 一种无需词汇表、无需训练、确定性且可逆的嵌入方法 [PDF](https://arxiv.org/pdf/2511.20665), [HTML](https://arxiv.org/abs/2511.20665)
### Authors
Tcharlies Schmitz
### Background
现有基于神经网络的文本嵌入方法依赖于统计共现或优化，通常需要训练和词汇表，并且包含随机参数，限制了它们的应用范围和解释性。
### Innovation
提出了一种称为谐波令牌投影（HTP）的新框架，该框架通过确定性和可逆的方式生成文本嵌入，无需训练、词汇表或随机参数。HTP 将每个令牌自由解析为基于其 Unicode 整数表示的谐波轨迹，从而建立一个双射且可解释的映射，将离散的符号与连续的向量空间关联起来。这种方法提供了相位相干的投影，能够保持结构和可逆性，使纯几何对齐即可推断出语义相似性。
### Conclusion
HTP 在语义文本相似性基准（STS-B）及其多语言扩展上的实验表明，它在英语中实现了 Spearman 相关系数ρ=0.68，并且在十个语言上保持稳定的性能，具有极低的计算成本和每个句子对小于毫秒级的延迟。这表明有意义的语义关系可以从确定性几何中涌现，提供了数据驱动嵌入之外的一种透明且高效的选择。
## 262. `cs.AI` - 带有RAG启用动态提示的大型语言模型系统分析在医疗错误检测和纠正中的应用 [PDF](https://arxiv.org/pdf/2511.19858), [HTML](https://arxiv.org/abs/2511.19858)
### Authors
Farzad Ahmed,Joniel Augustine Jerome,Meliha Yetisgen,Özlem Uzuner
### Background
临床记录中包含事实、诊断和管理错误，这些错误可能威胁到患者安全。大型语言模型（LLMs）可能有助于检测和纠正这些错误，但不同提示策略下的行为尚不清楚。本文旨在评估零样本提示、随机实例的静态提示以及检索增强的动态提示（RDP）对于三种医疗错误处理子任务的表现：错误标记检测、错误句子检测和错误纠正。
### Innovation
使用带有RAG（Retrieval-Augmented Generation）启用动态提示的LLMs，在MEDEC数据集上评测了九种指令调优后的LLMs（包括GPT、Claude、Gemini和OpenAI o系列模型）。结果显示，RDP在降低假阳性率、提高错误句子检测召回率以及提升上下文准确性方面表现优于零样本提示和随机实例的静态提示。
### Conclusion
在多种LLMs中，RDP优于零样本和随机实例静态提示。利用检索示例可以提高检测准确性，降低假阳性率，并增强医疗错误纠正的可靠性。
## 263. `cs.AI` - BengaliFig: 用于孟加拉语具象化和文化基础推理的低资源挑战 [PDF](https://arxiv.org/pdf/2511.20399), [HTML](https://arxiv.org/abs/2511.20399)
### Authors
Abdullah Al Sefat
### Background
大型语言模型在多语言基准测试中表现出色，但在具有象喻性和文化根基的推理方面，尤其是在低资源语境下，评估仍较为有限。本文针对孟加拉语这一广泛使用的低资源语言中存在的这一差距，提出了BengaliFig数据集。
### Innovation
BengaliFig是一个紧凑但标注丰富的挑战集，包含了435个从孟加拉口头和文学传统中抽取的独特谜题。每个项目都沿五个正交维度进行了标注，涵盖了推理类型、陷阱类型、文化深度、答案类别和难度，并通过一个约束意识强、AI辅助的管道自动转化为多项选择题格式。研究者评估了八个来自主要供应商的前沿语言模型，在零样本和少量样本链式思考提示下，揭示了在具象性与文化特异性推理方面的持续弱点。
### Conclusion
BengaliFig不仅为评估LLM在低资源文化语境中的鲁棒性提供了诊断工具，也是迈向更具包容性和遗产意识的NLP评估的重要一步。
## 264. `cs.AI` - EmoFeedback²：通过基于LVLM的奖励和文本反馈增强连续情绪图像生成 [PDF](https://arxiv.org/pdf/2511.19982), [HTML](https://arxiv.org/abs/2511.19982)
### Authors
Jingyang Jia,Kai Shu,Gang Yang,Long Xing,Xun Chen,Aiping Liu
### Background
连续情绪图像生成（C-EICG）由于其能够产生既符合用户描述又符合连续情绪值的图像而迅速发展。然而，现有的方法缺乏对生成图像的情绪反馈，限制了情绪连贯性的控制。此外，它们简单地将情绪与生成文本进行对齐，未能根据图像内容自适应调整情绪提示，导致情绪的忠实度不足。
### Innovation
为了解决这些问题，我们提出了一个新颖的生成-理解-反馈强化范式（EmoFeedback²），利用微调的大规模视觉-语言模型（LVLM）的推理能力，为生成高质量具有连续情绪的图像提供奖励和文本反馈。具体来说，我们引入了一种情绪感知的奖励反馈策略，其中LVLM评估生成图像的情绪值并计算与目标情绪的奖励，从而引导生成模型的强化微调并增强图像的情绪连续性。此外，我们设计了一个自我提升的文本反馈框架，在该框架中，LVLM迭代分析生成图像的情绪内容并自适应地为下一轮提示生成改进建议，从而通过精细的内容提高情绪的忠实度。
### Conclusion
广泛的实验结果表明，我们的方法能够生成具有预期情绪的高质量图像，在我们自定义的数据集上优于现有的最先进的方法。相关代码和数据集将很快发布。
## 265. `cs.CL` - 民主化大语言模型效率：从超大规模优化到普适部署 [PDF](https://arxiv.org/pdf/2511.20662), [HTML](https://arxiv.org/abs/2511.20662)
### Authors
Hen-Hsen Huang
### Background
大语言模型（LLMs）已成为不可或缺的工具，但目前最有效的优化方法——专家混合（MoE）、推测性解码和复杂的检索增强生成（RAG）——主要适用于拥有庞大基础设施和顶尖团队的超大规模服务提供商。在其他环境下，这些方法会变成额外的开销、脆弱性和浪费的碳排放。结果是，只有几家大型科技公司受益，而数千家医院、学校、政府和企业却缺乏可行的选择。
### Innovation
我们提出了一项新的研究议程：在不重新训练的情况下为预训练模型提供更高效的架构、发明轻量级且保持齐心协力的微调、在长推理链中使计算经济合理、无需重型RAG管道即能实现动态知识管理以及采用Overhead-Aware Efficiency (OAE) 作为标准基准。通过重新定义效率，包括要考虑采用成本、可持续性和公正性，我们可以使LLM部署民主化——确保优化减少不平等和碳浪费而非放大它们。
### Conclusion
我们认为下一阶段的前沿不再是大规模的更复杂性，而是稳健的简化：在有限资源和少量专业知识的情况下实现高效的运行。
## 266. `cs.CL` - PIRA：面向偏好的指令调优奖励模型与双重聚合 [PDF](https://arxiv.org/pdf/2511.20668), [HTML](https://arxiv.org/abs/2511.20668)
### Authors
Yongfu Xue
### Background
奖励模型是使大规模语言模型（LLMs）与人类偏好一致的关键，但面临两个主要挑战。首先，传统的判别奖励模型通常直接将问题和响应连接在一起作为输入，这导致了低数据效率。其次，奖励模型容易受到奖励过度优化的影响。
### Innovation
本文提出了一种名为PIRA的训练范式，通过三个策略解决上述问题：（1）将问题-答案对重新表述为基于偏好的指令，以获得更清晰和明确的任务说明；（2）从不同的偏好任务聚合奖励，以减少偏差并提高鲁棒性；（3）在不同的 dropout 率下平均价值头输出以稳定奖励。
### Conclusion
通过广泛的实验验证了PIRA的有效性。
## 267. `cs.CL` - Semantics Meet Signals: 双编码本表示学习在生成推荐中的应用 [PDF](https://arxiv.org/pdf/2511.20673), [HTML](https://arxiv.org/abs/2511.20673)
### Authors
Zheng Hui,Xiaokai Wei,Reza Shirkavand,Chen Wang,Weizhi Zhang,Alejandro Peláez,Michelle Gong
### Background
生成推荐作为一种统一检索和生成的强大范式，最近开始崭露头角。它通过使用离散的语义标记表示项目，并利用自回归模型实现灵活的序列建模。尽管这种方法取得了成功，但现有方法依赖单一的统一代码本编码所有项目，忽略了流行项目与长尾项目之间固有的协作信号和语义理解需求不平衡的问题。这种单一处理限制了表示效率并阻碍了模型的泛化。
### Innovation
FlexCode 引入了一个基于流行度的框架，能够动态分配固定数量的令牌预算给协作过滤 (CF) 代码本和语义代码本。轻量级的 MoE 调整 CF 特定的精确度和语义泛化，同时一种对齐与平滑目标保持了全范围流行度的连贯性。实验表明，FlexCode 在各类数据集上均优于强大基线。
### Conclusion
FlexCode 提供了一种新的令牌表示机制，增强了推荐准确性并提高了尾部样本鲁棒性，为基于令牌的推荐模型平衡记忆和泛化提供了新的视角。
## 268. `cs.AI` - R3A：多代理故障定位与随机树思考补丁生成的可靠性RTL修复框架 [PDF](https://arxiv.org/pdf/2511.20090), [HTML](https://arxiv.org/abs/2511.20090)
### Authors
Zizhang Luo,Fan Cui,Kexing Zhou,Runlin Guo,Mile Xia,Hongyuan Hou,Yun Liang
### Background
RTL（寄存器传输级）bug修复在硬件设计和验证中非常重要。传统的方法通过定义特定的搜索空间来定位和修复程序中的bug，这些方法依赖于固定的模板，只能处理少量的bug。相比之下，具有理解代码语义能力的大语言模型可以被探索用于RTL修复，但由于RTL代码和波形固有的随机性和长输入内容，其结果不可靠。
### Innovation
本文提出了一种基于大语言模型的自动RTL程序修复框架——R3A，以提高修复的可靠性。R3A方法包括随机树思考方法来控制补丁生成代理探索验证的解决方案，以及一个多代理故障定位方法来找到故障候选点。实验结果显示，R3A在规定时间内可以修复RTL修复数据集中的90.6%的bug，比传统方法和基于大语言模型的方法多修复45%的bug，同时平均达到了86.7%的pass@5准确率。
### Conclusion
R3A能够有效地修复大量RTL中的bug，提高了解决bug的可靠性和效率。
## 269. `cs.CL` - 基于中心点的ITSM环境中文本分类框架 [PDF](https://arxiv.org/pdf/2511.20667), [HTML](https://arxiv.org/abs/2511.20667)
### Authors
Hossein Mohanna,Ali Ait-Bachir
### Background
IT服务管理（ITSM）系统需要对支持票据进行层级分类，以便按树状分类税onomies进行管理。现有分类方法难以平衡性能和可解释性。
### Innovation
提出了一种基于中心点的双嵌入分类框架，该方法维持了每类别独立的语义和词汇中心点表示，在推理时通过互惠排名融合。该框架在分类性能上与支持向量机相当（分层F1分数为0.731对比0.727），同时通过中心点表示增加了解释性。实验表明，该方法在123类8,968张ITSM票据上的训练速度快5.9倍，增量更新速度快152倍，批量大小为100-1000样本时的速度提升8.6-8.8倍（不包括嵌入计算）。
### Conclusion
该研究提出的方法适用于对解释性和操作效率有高需求的ITSM生产环境。
## 270. `cs.AI` - Agent0-VL: 探索工具整合视野语言推理的自我演进代理 [PDF](https://arxiv.org/pdf/2511.19900), [HTML](https://arxiv.org/abs/2511.19900)
### Authors
Jiaqi Liu,Kaiwen Xiong,Peng Xia,Yiyang Zhou,Haonian Ji,Lu Feng,Siwei Han,Mingyu Ding,Huaxiu Yao
### Background
视觉-语言代理在多种跨模态推理任务中取得了显著进展，但其学习仍受限于人类标注监督的限制。近年来的自我奖励方法通过使模型能够充当自身的评判者或奖励提供者，试图克服这一限制。然而，纯文本自我评估难以验证复杂的视觉推理步骤，经常产生评估幻觉。
### Innovation
本文提出了一种名为Agent0-VL的自我演进视觉-语言代理，该代理通过工具整合推理实现持续改进。Agent0-VL融合了工具使用不仅进入推理，还进入自我评估和自我修复，使模型能够通过基于证据的分析进行自我省察、验证和推理的精炼。它在单个LVLM内统一了两种角色：一个求解器执行多轮工具整合推理，一个验证器通过基于工具的批判生成结构化反馈和细粒度自奖励。这些角色通过自我演进推理循环相互作用，其中基于工具的验证和强化学习共同对推理和评估分布进行对齐，以实现稳定的自我改进。
### Conclusion
通过这种零外部奖励进化，Agent0-VL实现了无任何人工标注或外部奖励模型的推理和验证行为自我对齐，实现了持续的自我改进。实验表明，在几何问题解决和视觉科学分析方面，Agent0-VL相对于基础模型提高了12.5%。
## 271. `cs.CL` - 基于MLP和 transformer 方法的输出标记生成动态模板选择 [PDF](https://arxiv.org/pdf/2511.20683), [HTML](https://arxiv.org/abs/2511.20683)
### Authors
Bharadwaj Yadavalli
### Background
当前的大规模语言模型部署通常采用统一的提示策略来处理不同类型的查询，对复杂分析任务和简单事实问题施加冗长的响应模式。这种‘一刀切’的方法导致了大量的标记无效使用，尤其在面对输入和输出标记成本差异显著，输出标记成本普遍高出4-8倍的情况下，问题更为严重。因此，如何优化响应模板，以匹配查询复杂度，同时降低成本但不牺牲响应质量，成为了一个重要的研究方向。
### Innovation
本文提出了动态模板选择（DTS）方法，该方法能够根据查询的复杂度自适应地选择响应模板，显著降低了成本同时保持响应质量。为了实现这一目标，研究比较了基于MLP的简单路由方法和更复杂的微调RoBERTa变换器。实验证明，尽管参数少125M，MLP路由方法在1000个MMLU问题上取得了90.5%的路由准确率，略高于RoBERTa的89.5%。同时，动态选择模板行为表现得具备跨提供商的通用性，进一步验证了其有效性。
### Conclusion
本文通过实证分析，验证了动态模板选择方案的有效性和通用性，贡献了包括机器学习理论支持下的问题表述、对应算法及其复杂性分析，以及生产系统下的广泛的实验验证。
## 272. `cs.CL` - MindSET：通过大规模社交媒体数据促进心理健康基准测试 [PDF](https://arxiv.org/pdf/2511.20672), [HTML](https://arxiv.org/abs/2511.20672)
### Authors
Saad Mankarious,Ayah Zirikly,Daniel Wiechmann,Elma Kerz,Edward Kempa,Yu Qiao
### Background
社交媒体数据已经成为研究心理健康的重要资源，提供了实时洞察思想、情感和行为的信息，这是传统方法所忽视的。这一领域的进步得益于心理健康分析的基准数据集，但大多数现有基准因数据可用性有限、清理不足以及社交媒体内容的固有多样性（如多语言和有害内容）而变得过时。
### Innovation
我们提出一个新的基准数据集，命名MindSET，从Reddit中选取并使用自我报告的诊断信息进行构建，以解决上述限制。MindSET包含超过1300万篇被注释的文章，涉及七种心理健康状况，超过先前基准数据集的两倍。数据进行了严格的预处理，包括语言筛选、NSFW和重复内容的去除。我们还使用LIWC进行了语言分析，以研究八个组中心理术语的频率。MindSET用于诊断检测的二分类实验表明，基于MindSET训练的模型在自闭症检测中的F1分数提高了18个百分点。
### Conclusion
MindSET为探索社交媒体与心理健康交汇的研究者提供了坚实的基础，支持早期风险检测和对新兴心理趋势的深入分析。
## 273. `cs.CL` - 多路径检索的记忆：大规模语言模型训练数据泄露的稳健检测的多前缀框架 [PDF](https://arxiv.org/pdf/2511.20799), [HTML](https://arxiv.org/abs/2511.20799)
### Authors
Trung Cuong Dang,David Mohaisen
### Background
大规模语言模型在大规模语料库上训练时，容易出现逐字记忆训练数据的情况，这引发了重大的隐私和版权风险。尽管已有研究提出了多种关于记忆的定义，但这些定义在全面捕捉这一现象方面存在局限，尤其是在对齐模型中。因此，研究人员需要寻找更有效的评估方法。
### Innovation
本文提出了一种新颖的框架：多前缀记忆。核心见解是，记忆序列深深地被编码，因此可以通过远多于非记忆内容的唯一前缀来检索。该框架从单一路径提取转向量化记忆的稳健性，通过检索路径的多样性来衡量。通过在开源和对齐聊天模型上的实验，证明了多前缀定义可靠地区分了记忆内容和非记忆内容，为审计LLM中的数据泄露提供了稳健且实用的工具。
### Conclusion
通过实验验证了本文中的多前缀定义在区分记忆和非记忆数据方面的可靠性，提供了一种稳健且实用的方法来审计大规模语言模型中的数据泄露问题。
## 274. `cs.CL` - 阿拉伯语上下文依赖文本到SQL的提示工程技术 [PDF](https://arxiv.org/pdf/2511.20677), [HTML](https://arxiv.org/abs/2511.20677)
### Authors
Saleh Almohaimeed,May Alsofyani,Saad Almohaimeed,Mansour Al Ghanim,Liqiang Wang
### Background
近年来，跨域、上下文相关文本到SQL的任务受到了广泛关注。该任务能够使无SQL知识的用户能够使用自然语言与数据库进行对话。然而，大多数可用的数据集和研究都是在英语中进行的，部分内容涉及中文。到目前为止，在阿拉伯语中尚未有对该任务的研究。本文介绍了Ar-SParC，这是首个阿拉伯语跨域、上下文相关文本到SQL的数据集。
### Innovation
本文引入了Ar-SParC数据集，该数据集包括3,450个相互相关的问题序列，每个序列平均包含约三个问题，总共包含10,225个问题及其对应的SQL查询。作者使用两个大型语言模型（GPT-3.5-turbo和GPT-4.5-turbo）在40次实验中应用了10种不同的提示工程技术，包括四种问题表示方法和六种上下文学习技术。此外，作者还开发了一种新颖的GAT纠正方法，该方法在所有40次实验中提高了性能，在零样本设置下平均提高了1.9%的执行准确性（EX）和交互准确性（IX），在上下文学习设置下平均分别提高了1.72%的EX和0.92%的IX。
### Conclusion
作者进行了进一步的消融研究，添加了两个实验来解释为什么GAT纠正方法比之前的方法更能表现良好，特别是在阿拉伯语中。这表明，通过开发专门针对阿拉伯语的上下文相关文本到SQL数据集和相关的方法，能够显著提高此类任务的性能。
## 275. `cs.CL` - 结构化定义与划分对于LLM法律推理的研究：基于印度法律数据的探讨 [PDF](https://arxiv.org/pdf/2511.20669), [HTML](https://arxiv.org/abs/2511.20669)
### Authors
Mann Khatri,Mirza Yusuf,Rajiv Ratn Shah,Ponnurangam Kumaraguru
### Background
大型语言模型（LLMs）在广泛的数据集上进行训练，展示了卓越的推理能力。然而，他们在特定领域如法律方面经常遇到困难，主要是因为缺乏特定领域的预训练。法律文件通常很长且复杂，给模型高效处理全文本带来挑战。先前的研究通过上下文方法来弥补知识空缺，提升了模型在新领域的表现。本研究探讨了模型在法律任务中的行为，并通过三项实验来研究：（i）基于修辞角色重组文档，评估结构化信息如何影响长文本处理和模型决策；（ii）定义修辞角色以使模型熟悉法律术语；（iii）模拟法庭关于修辞角色的逐步推理以增强模型的推理能力。这些实验在三项印度法律判决预测数据集上以零样本方式进行。
### Innovation
研究通过三种创新实验来改善LLMs的法律推理能力：首先是基于修辞角色重组文档，以结构化信息影响长文本处理；其次，定义修辞角色使模型熟悉法律术语；最后，模拟法院的推理步骤来增强模型推理能力。所有实验在印度法律判决预测数据集上进行了零样本验证。
### Conclusion
研究结果表明，以结构化数据或解释关键法律术语可以显著提高模型的性能。在F1分数上，最小改善为1.5%，最大改进为4.36%高于基线。
## 276. `cs.CL` - 大模型推理中的认知偏差损害临床肿瘤病历的解释 [PDF](https://arxiv.org/pdf/2511.20680), [HTML](https://arxiv.org/abs/2511.20680)
### Authors
Matthew W. Kenaston(1),Umair Ayub(1),Mihir Parmar(2),Muhammad Umair Anjum(1),Syed Arsalan Ahmed Naqvi(1),Priya Kumar(1),Samarth Rawal(1),Aadel A. Chaudhuri(4),Yousef Zakharia(3),Elizabeth I. Heath(5),Tanios S. Bekaii-Saab(3),Cui Tao(6),Eliezer M. Van Allen(7),Ben Zhou(2),YooJung Choi(2),Chitta Baral(2),Irbaz Bin Riaz(1 and 3 and 6) ((1) Mayo Clinic College of Medicine and Science, Phoenix, AZ, (2) School of Computing and AI, Arizona State University, Tempe, AZ, (3) Mayo Clinic Comprehensive Cancer Center, Phoenix, AZ, (4) Department of Radiation Oncology, Mayo Clinic, Rochester, MN, (5) Department of Oncology, Mayo Clinic, Rochester, MN, (6) Department of Artificial Intelligence and Informatics, Mayo Clinic, Rochester, MN, (7) Dana-Farber Cancer Institute, Harvard Medical School, Boston, MA)
### Background
尽管大型语言模型在临床基准测试中表现良好，但它们可能会通过错误的推理得出正确的结论，这种失败模式在肿瘤学决策支持方面具有安全影响，而现有的基于准确性的评估方式并不涵盖这一点。在本研究中，研究人员通过回顾性研究，旨在探索大型语言模型在分析真实肿瘤学病历时出现的推理错误，以确定其临床相关性。通过注释来自乳腺癌和胰腺癌病历的600次推理过程，构建了一个三级分类法，将计算错误与认知偏差框架对接。研究结果显示，错误出现在23%的解读中，而确认偏差和锚定偏差最多。推理失败与不符合指南和可能有害的建议有关，特别是在疾病晚期管理中。
### Innovation
研究人员提出了一种基于GPT-4链式思维反应的推理错误层次分类法，并使用乳腺癌和胰腺癌病历数据集来注释推理痕迹，构建了一个三级分类法，将计算错误与认知偏差框架对接。该分类法有助于识别和分类大型语言模型推理过程中的错误，提供了一种通用框架，以评估和改进推理的准确性，在临床部署前有针对性地提高大型语言模型的可靠性。
### Conclusion
研究发现，当推理错误时，大语言模型可能会提供流畅但临床不安全的建议。此分类法提供了一个评估和改进推理准确性的通用框架，可以为临床部署前提供有针对性的改进措施，以提高大型语言模型在临床使用中的安全性。自动化评估者即使使用最先进的语言模型也难以可靠地区分推理错误的子类型。
## 277. `cs.CL` - LLMs中语义角色电路的涌现和局部化 [PDF](https://arxiv.org/pdf/2511.20910), [HTML](https://arxiv.org/abs/2511.20910)
### Authors
Nura Aljaafari,Danilo S. Carvalho,André Freitas
### Background
尽管大型语言模型（LLM）显示出语义能力，但它们内部机制如何具体实现抽象语义结构仍不清楚。本文旨在研究LLMs如何实施语义角色。
### Innovation
本文提出了一种融合角色交叉最小对、时间发生分析和跨模型比较的方法，以研究LLMs如何实现语义角色。研究发现：(i) 高度集中的电路（89-94%的归因在28个节点内）；(ii) 结构的逐步细化而非阶段转换，有时大型模型会绕过局部化电路；(iii) 中等尺度间的保守性（24-59%的组件重叠）伴随高频谱相似性。这些发现表明，LLMs形成了紧凑且因果隔离的机制来处理抽象语义结构，并且这些机制在不同尺度和架构之间部分转移。
### Conclusion
LLMs形成了紧凑且因果隔离的机制来处理抽象语义结构，并且这些机制在不同尺度和架构之间部分转移。
## 278. `cs.CL` - Evo-Memory: 使用自我演化记忆评估LLM代理测试时学习 [PDF](https://arxiv.org/pdf/2511.20857), [HTML](https://arxiv.org/abs/2511.20857)
### Authors
Tianxin Wei,Noveen Sachdeva,Benjamin Coleman,Zhankui He,Yuanchen Bei,Xuying Ning,Mengting Ai,Yunzhe Li,Jingrui He,Ed H. Chi,Chi Wang,Shuo Chen,Fernando Pereira,Wang-Cheng Kang,Derek Zhiyuan Cheng
### Background
大语言模型（LLM）代理需要状态性来执行长期规划和解决问题。这使得记忆成为一个关键组件，但其管理和演化仍然未得到充分探索。现有评估主要集中在静态对话环境中，这些环境中的记忆被动地从对话中检索以回答查询，而忽略了动态累积和重用经验的能力，特别是在不断变化的任务流中。在现实生活环境中，如交互式问题助手或实体代理，LLMs需要处理持续的任务流，但通常无法从累积的交互中学到东西，浪费了宝贵的情境洞察，这一局限性要求在测试时进化，即在部署过程中LLMs能够连续检索、整合和更新记忆。为了弥合这一差距，我们引入了Evo-Memory，一种全面的流式基准测试框架和用于评估自我演化记忆的LLM代理的框架。
### Innovation
Evo-Memory框架包括以下创新：1) 将数据集结构化为连续的任务流，要求LLMs在每次交互后进行搜索、自适应和演化；2) 统一并实现了十多个代表性记忆模块，并在10个不同的多回合目标导向和单回合推理及QA数据集上进行评估；3) 提供了一个基准方法ExpRAG，用于检索和利用先前的经验，并进一步提出了融合推理、任务操作和记忆更新的ReMem行动-思考-记忆提炼管道，以实现持续改进。
### Conclusion
Evo-Memory是一个用于评估自我演化记忆在LLM代理中的流式基准测试框架，能够全面评估代理在不断变化的任务流中的学习和演化能力，填补了现有评估的空白，有利于改进LLM代理在现实生活中的应用效能。
## 279. `cs.CL` - 利用LLMs进行2D材料数据的精确提取、查询和智能管理 [PDF](https://arxiv.org/pdf/2511.20691), [HTML](https://arxiv.org/abs/2511.20691)
### Authors
Lijun Shang,Yadong Yu,Wenqiang Kang,Jian Zhou,Dongyue Gao,Pan Xiang,Zhe Liu,Mengyan Dai,Zhonglu Guo,Zhimei Sun
### Background
二维（2D）材料由于其独特的物理化学和电子特性，在能源存储和转换领域显示出了广泛的应用。有关这些材料的性质及其制备方法的重要信息大多包含在已发表的研究论文中。然而，由于合成信息的分散性，提取和管理这些信息相对困难。
### Innovation
该研究利用了大规模语言模型（LLMs）来实现2D材料数据的精确提取、查询和智能管理。这种技术可以有效整合和管理分散在不同文献中的信息，提高信息管理的效率和准确性。
### Conclusion
该方法不仅可以有效地提取和查询2D材料数据，还可以智能地管理这些数据，为研究提供更加便捷和精确的信息支持。
## 280. `cs.CL` - Language Models的Length-MAX Tokenizer [PDF](https://arxiv.org/pdf/2511.20849), [HTML](https://arxiv.org/abs/2511.20849)
### Authors
Dong Dong,Weijie Su
### Background
现有的语言模型使用字节对编码（BPE）进行分词，这种方法虽然有效，但在训练和推理阶段会产生较多的标记。Introducing a new tokenizer旨在通过最小化平均字符数量来减少所需标记数量，从而提高效率。
### Innovation
作者提出了一种名为Length-MAX的新分词方法，通过将长度加权的目标函数最大化为图划分问题，并开发了一个贪婪近似算法来获取词典。相对于BPE，该方法在不同词汇大小的条件下能减少14%-18%的标记数量，特别是在64K词汇大小时减少13.0%。这不仅提高了训练效率和推理速度，还提升了下游任务的性能。
### Conclusion
Length-MAX分词方法在优化平均标记长度方面比优化频率更能有效提高语言建模的效率，同时往往还能改善下游任务的性能。这种分词方法适用于生产系统，还能减少推理阶段的嵌入和KV缓存内存使用量。
## 281. `cs.CL` - 结构化提示使语言模型评估更加稳健、综合 [PDF](https://arxiv.org/pdf/2511.20836), [HTML](https://arxiv.org/abs/2511.20836)
### Authors
Asad Aali,Muhammad Ahmed Mohsin,Vasiliki Bikia,Arnav Singhvi,Richard Gaus,Suhana Bedi,Hejie Cui,Miguel Fuentes,Alyssa Unell,Yifan Mai,Jordan Cahoon,Michael Pfeffer,Roxana Daneshjou,Sanmi Koyejo,Emily Alsentzer,Percy Liang,Christopher Potts,Nigam H. Shah,Akshay S. Chaudhari
### Background
随着语言模型（LMs）在各个领域的应用日益广泛，高质量的基准测试框架对于准确估计其性能并指导部署决策至关重要。虽然Holistic Evaluation of Language Models (HELM)框架能够进行广泛的多任务评估，但它们通常依赖于固定提示，无法在不同模型间进行有效的推广，导致生成的性能估计不具代表性。除非我们能够估计每个模型的天花板（最大性能可通过调整提示实现），否则可能会低估其性能。
### Innovation
该论文提出了一个可再现的DSPy+HELM框架，该框架将结构化提示方法引入语言模型基准测试，以提取推理过程，从而实现更准确的LM基准测试。利用四种提示方法，对四个前沿LMs在七个基准（通用/医学领域）中进行了评估，发现标记符提示方法之下，HELM会低估LM性能，性能估计更分散，竞争排名变化大，引入推理减少LM对提示设计的敏感度。
### Conclusion
这是首个大规模基准测试研究，实验性地描述了LM在基准和提示方法之间的行为，表明可扩展的性能天花板估计能够生成更有用的基准。作者开源了DSPy+HELM集成和提示优化管道。
## 282. `cs.CL` - SAGE: 语言模型中解释SAE特征的代理解释框架 [PDF](https://arxiv.org/pdf/2511.20820), [HTML](https://arxiv.org/abs/2511.20820)
### Authors
Jiaojiao Han,Wujiang Xu,Mingyu Jin,Mengnan Du
### Background
大型语言模型虽然取得了显著的进步，但其内部机制仍然不太透明，这构成了一项重要挑战，妨碍了它们的安全和可靠部署。尽管稀疏自编码器（SAEs）能够将LLM的表示分解为更可解释的特征，但解释SAEs捕捉到的特征仍然是一个难题。
### Innovation
本文提出了SAGE（SAE AGentic Explainer）代理框架，将特征解释从被动、一次性的生成任务重构为积极、基于解释的过程。SAGE通过系统地为每个特征制定多种解释，设计针对性实验进行测试，并根据经验激活反馈迭代优化解释，从而提供比现有基线显著更高生成和预测准确性的解释。
### Conclusion
实验表明，SAGE在多种语言模型的SAE特征上产生了比现有最好基线显著更高的生成性和预测性解释准确度。
## 283. `cs.CL` - 低资源语言中的脱颖而出：跨语文本英波论证模型优于大型语言模型增强 [PDF](https://arxiv.org/pdf/2511.20872), [HTML](https://arxiv.org/abs/2511.20872)
### Authors
Ali Jahan,Masood Ghayoomi,Annette Hautli-Janisz
### Background
论证采矿是自然语言处理的一个子领域，旨在识别和提取文本中的论证成分（如前提和结论），并识别它们之间的关系。这项任务揭露了文本的逻辑结构，可用于知识提取等任务。本文关注利用跨语文本方法进行低资源语言的论证采矿。
### Innovation
本文提出了一种利用跨语文本方法进行低资源语言论证采矿的新方法，构建了三种训练场景，分别是零样本迁移训练、英语数据增强训练以及跨语文本训练。结果表明，轻量级的跨语文本组合模型在低资源语言上的效果优于大型语言模型增强模型。
### Conclusion
跨语文本模型在低资源语言上的表现显著优于增强模型，为解决低资源语言上的数据资源短缺问题提供了实用路径。
## 284. `cs.CL` - 在上下文学习中语义锚点：为什么小型LLM无法翻转标签 [PDF](https://arxiv.org/pdf/2511.21038), [HTML](https://arxiv.org/abs/2511.21038)
### Authors
Anantha Padmanaban Krishna Kumar(Boston University)
### Background
本文探讨了上下文学习（ICL）是否能够覆盖预训练标签的语义，或者仅仅是完善现有的语义基础。通过将语言模型（LLMs）视为由提示引起的分类器，并比较其在自然演示（带有正确标签）和反转演示（系统性地翻转标签含义）下的行为，研究者们进行了分析。
### Innovation
研究者提出了将ICL行为分解为三种对齐指标（真实对齐、先验对齐和提示对齐），并引入了语义覆盖率的概念，定义为在翻转语义下的正确性。通过八个分类任务和八个开源LLMs（1到120亿参数），提供了可验证的证据表明存在语义锚点的观点。
### Conclusion
自然演示中，ICL提高了准确性同时保持了较强先验对齐；大多数正确预测与零样本行为一致，即使先验较弱。在反转演示中，模型无法学习一致的反语义分类器：提示对齐只能通过牺牲准确性来增加，且在少量几次示例（1到120亿参数）的设置中语义覆盖率保持为零。ICL主要调整输入在预训练中学习到的稳定语义方向上的投影方式，说明小规模很少样示例的提示极限，并建议在这些规模上覆盖标签语义需要ICL之外的干预。所有代码可在以下地址获得：this https URL.
## 285. `cs.CL` - TrackList：追溯开放大型语言模型中头部和尾部知识的查询语言多样性 [PDF](https://arxiv.org/pdf/2511.21006), [HTML](https://arxiv.org/abs/2511.21006)
### Authors
Ioana Buhnila,Aman Sinha,Mathieu Constant
### Background
大型语言模型（LLMs）在回答用户输入查询的定义类型问题方面表现出高效性。然而，对于人类来说，提供各种类型的答案，如举例和改写，是一项容易的工作，但对于LLMs来说，却难以提供除定义之外的正确答案。研究者使用TrackList这一细粒度的语料库和统计分析流程来调查预训练数据对不同类型语言查询答案的影响。研究还引入了一个包含6170个人工标注医疗术语及其定义、命名、示例、解释或改写的英语文本数据集RefoMed-EN，以研究概念（头部或尾部）的高频率或低频率对语言模型性能的影响。
### Innovation
研究采用TrackList这一细粒度的语料库和统计分析流程来评估LLM在处理各种语言查询时性能的下降，特别是考察预训练数据的影响。同时，研究所引入的RefoMed-EN数据集，以及通过句法和语义相似性度量、统计相关性和嵌入来评估LLM输出的质量。研究发现在处理定义类型的查询时LLM表现出较高的任务绩效，而在处理举例类型的问题时则表现最低。此外，研究还显示，对于定义类型的问题，大型语言模型在处理流行和频繁的知识时更倾向于改写，而在处理较少提及和专业领域知识时改写的倾向较小。
### Conclusion
本文研究表明，LLM在处理定义类型的查询时表现出最高的任务绩效，而在处理举例类型的查询时，其表现最差。此外，研究结果还表明，对于定义类型的问题，大型语言模型更倾向于对流行和频繁的知识进行改写，而在处理尾端和科技知识时改写的倾向较小，特别是在专家文本中。
## 286. `cs.CL` - 自引导防御：基于合成准则的推理模型自适应安全对齐 [PDF](https://arxiv.org/pdf/2511.21214), [HTML](https://arxiv.org/abs/2511.21214)
### Authors
Yuhang Wang,Yanxu Zhu,Dongyuan Lu,Jitao Sang
### Background
推理模型在复杂任务中展现出卓越的能力，但它们面临来自隐蔽和欺骗性提示的对抗性‘逃 Jailbreak’威胁，这些威胁往往能够绕过内置的安全机制，产生有害内容。这凸显了需要一个适应性安全对齐方法，使模型能够自主强化其防御能力以应对对抗性输入。
### Innovation
提出了Synthesized Guideline-based Adaptive Safety Alignment (SGASA)框架，该框架将模型生成的安全准则内化，增强模型的韧性以对抗有害的对抗性提示，同时最小化对良性请求的错误拒绝。SGASA框架包括两个关键阶段：数据预合成和对齐微调。
### Conclusion
在多个数据集上的广泛实验表明，SGASA显著提高了模型的安全性，验证了其适应性和可扩展的有效性。
## 287. `cs.CL` - Chatty-KG：一种用于知识图谱上的按需对话式问答的多智能体AI系统 [PDF](https://arxiv.org/pdf/2511.20940), [HTML](https://arxiv.org/abs/2511.20940)
### Authors
Reham Omar,Abdelghny Orogat,Ibrahim Abdelaziz,Omij Mangukiya,Panos Kalnis,Essam Mansour
### Background
领域内广泛使用知识图谱（KGs）为企业和特定应用提供结构化、不断演变且可靠的知识。大型语言模型（LLMs）可以进行自然、情境意识的对话，但缺乏对私人和动态KGs的直接访问。检索增强生成（RAG）系统可以检索图的内容，但往往按顺序处理结构，难以处理多轮对话上下文，需要大量的索引。传统的KGQA系统保留了结构，但通常只支持单轮QA，存在高延迟问题，并且难以处理核心引用和上下文跟踪。
### Innovation
提出了一种模块化的多智能体系统Chatty-KG，用于KG上的对话式QA。Chatty-KG通过任务特定的LLM代理生成SPARQL查询，结合RAG风格的检索和结构化执行。该系统在多元化KGs上的实验表明，Chatty-KG在单轮和多轮设置中均显著优于最先进的基线，在F1和P@1评分上表现更佳。其模块化设计保持了对话连续性，支持不断变化的KGs而不需微调或预处理。评价表明该系统与商业LLM（例如GPT-4o，Gemini-2.0）和开放知识库（例如Phi-4，Gemma 3）兼容，具有稳定性能。Chatty-KG统一了对话灵活性与结构化的KG锚定，提供了一种可扩展和可扩展的多轮KGQA方法。
### Conclusion
Chatty-KG结合了对话灵活性和基于KG的信息查准，提供了一种可扩展和可扩展的方法，以实现可靠且多轮的KGQA。
## 288. `cs.CL` - 使用柯尔莫哥洛夫-阿诺德网络头微调提升缅甸新闻分类 [PDF](https://arxiv.org/pdf/2511.21081), [HTML](https://arxiv.org/abs/2511.21081)
### Authors
Thura Aung,Eaint Kay Khaing Kyaw,Ye Kyaw Thu,Thazin Myint Oo,Thepchai Supnithi
### Background
在资源稀缺的语言（如缅甸语）中，分类任务通常仅微调最终的分类层，而将预训练的编码器权重保持冻结。尽管多层感知机（MLPs）是常用的工具，但其固定的非线性限制了表达能力和增加了计算成本。
### Innovation
本文探讨了柯尔莫哥洛夫-阿诺德网络（KANs）作为分类头的替代方案，评估了基于傅里叶的FourierKAN、基于样条的EfficientKAN和基于网格的FasterKAN，这些方案适用于包括TF-IDF、fastText和多语言变换器（mBERT、Distil-mBERT）在内的多种嵌入。实验结果显示，KAN头与MLPs相当或更优。EfficientKAN与fastText结合时达到了最高的F1分数（0.928），而FasterKAN在速度和精度之间提供了最佳权衡。在变换器嵌入中，EfficientKAN与mBERT（F1分数0.917）的MLPs表现相当或稍优。
### Conclusion
这些发现表明，KANs是低资源语言分类中具有表达性和效率优势的选项，可以作为MLPs的替代方案。
## 289. `cs.CL` - 基于检索感知的实用元认知提示策略在检测讽刺中的应用 [PDF](https://arxiv.org/pdf/2511.21066), [HTML](https://arxiv.org/abs/2511.21066)
### Authors
Michael Iskandardinata,William Christian,Derwin Suhartono
### Background
讽刺的检测仍然是自然语言处理（NLP）领域的挑战，尽管神经网络方法取得了进步。预训练语言模型（PLMs）和大型语言模型（LLMs）是检测讽刺的首选方法。然而，讽刺文本的复杂性、语言多样性以及跨社区的文化差异，使得即使对于PLMs和LLMs这样的高级模型来说，讽刺检测也变得更为困难。此外，这些模型在处理需要额外语境分析的词语或标记方面表现不稳定。
### Innovation
本文在基于LLMs的讽刺检测方法——实用元认知提示（PMP）的基础上，引入了一种检索感知的方法，该方法通过检索背景信息为每次目标文本提供上下文支持。提出了一种结合检索外部非参数知识和自省式内部知识的方式来增强模型分析讽刺文本的准确性和鲁棒性。
### Conclusion
通过无参数检索方式在Twitter印尼讽刺数据集上实现了显著的9.87%的宏F1值提升，自省式检索方式在SemEval和MUStARD数据集上分别实现了3.29%和4.08%的宏F1值提升。这些结果强调了在LLMs中增强讽刺检测任务性能时上下文的重要性，尤其是对文化特异性俚语、引用或未知术语的文化适应性。未来工作的重点将是优化相关上下文信息的检索，并研究检索质量对性能的影响。
## 290. `cs.CL` - MortgageLLM：基于残差指令转移、对齐调整和任务特定路由的领域自适应预训练 [PDF](https://arxiv.org/pdf/2511.21101), [HTML](https://arxiv.org/abs/2511.21101)
### Authors
Manish Jain,Satheesh Kumar Ponnambalam,Salman Faroz,Chandrakanth Lns,Vinay Sharma
### Background
大型语言模型（LLMs）在通用领域展现出卓越的能力，但在特定行业如抵押贷款金融领域的应用时需要增加领域特定知识的同时保持指令跟随的准确性。
### Innovation
该研究提出了一种名为MortgageLLM的新型领域特定大语言模型，通过双通道专业化框架从单一基础模型（LLaMA-3.1-8B）构建。该方法应用了残差指令技术来恢复指令跟随能力，在不进行监督微调的情况下解决了单一多任务模型在优化结构化任务时会牺牲对话准确性的问题。模型包括一个对话问答模型和一个结构化任务模型，并采用少量样本分类机制进行任务路由。
### Conclusion
实验结果表明，该模型在特定领域的基准测试中表现优异，尤其是在总结、问答和分类任务上取得了显著的性能提升。特别是在LLM作为法官的总结分数、问答分数和分类分数上，分别达到了4.58、4.09和2.6，相比基础模型分别提高了1.59、0.09和1.4。
## 291. `cs.CL` - 为Isan语言开发开放的对话性语音语料库 [PDF](https://arxiv.org/pdf/2511.21229), [HTML](https://arxiv.org/abs/2511.21229)
### Authors
Adisai Na-Thalang,Chanakan Wittayasakpan,Kritsadha Phatcharoen,Supakit Buakaw
### Background
本论文介绍了首个开放性的Isan语言对话性语音数据集，Isan是泰国最广泛使用的区域方言。与现有的主要基于朗读或脚本语言的语音语料库不同，此数据集包含自然语言，从而捕捉到了诸如口语表达、自发韵律、中断和频繁语言转换等真实语言现象。构建这一资源的关键挑战在于Isan缺乏标准化的书写形式，由于泰语和Isan的词汇声调差异，书写实践有很大差异，这极大地增加了转录指南的复杂性，并对一致性、可用性和语言真实性提出了疑问。
### Innovation
本文提出了一种实践性的转录方案，平衡了代表准确性与计算处理需求之间的需求。通过将此数据集作为开放资源发布，旨在促进包容性人工智能的发展，支持对未充分研究的语言的研究，并为解决建模对话性语言的内在语言和技术挑战奠定基础。
### Conclusion
本研究通过构建和开源首个Isan语言对话性语音数据集，为语言建模技术贡献了一个重要的数据基础，支持对未充分研究的语言的研究，并促进包容性人工智能的发展。
## 292. `cs.CL` - 使用声学特征增强的对齐辅助Transformer在低资源缅甸语ASR纠错中的应用 [PDF](https://arxiv.org/pdf/2511.21088), [HTML](https://arxiv.org/abs/2511.21088)
### Authors
Ye Bhone Lin,Thura Aung,Ye Kyaw Thu,Thazin Myint Oo
### Background
本文研究了序列到序列的Transformer模型在低资源缅甸语自动语音识别(ASR)错误校正中的应用，重点关注不同的特征集成策略，包括国际音标(IPA)和对齐信息。据我们所知，这是首次针对缅甸语进行ASR错误校正的研究。研究使用了五种ASR的骨干网络，并展示了ASR错误校正方法在一词一字符层面的准确率上均优于基线输出。
### Innovation
本文提出的ASR错误校正（AEC）模型，结合了国际音标和对齐特征，显著提升了ASR模型的准确性：在增广前，将平均词错误率(WER)从51.56降低到39.82；在增广后，将平均WER从中降低到43.59，并且chrf++得分从0.5864提高到0.627，表明模型在没有AEC的ASR基线输出上具有持续改进的效果。
### Conclusion
本研究突显了ASR错误校正的鲁棒性，并强调在低资源设置中提高ASR输出质量时特征设计的重要性。
## 293. `cs.CL` - PEFT-Bench: 参数高效微调方法基准 [PDF](https://arxiv.org/pdf/2511.21285), [HTML](https://arxiv.org/abs/2511.21285)
### Authors
Robert Belanec,Branislav Pecher,Ivan Srba,Maria Bielikova
### Background
尽管大规模语言模型（LLMs）在许多任务上达到了先进的性能，但它们庞大的规模往往导致了高计算和环境成本，限制了其可访问性。参数高效微调（PEFT）方法通过减少可训练参数的数量，同时保持下游性能，来解决这一挑战。尽管PEFT方法的开发有所增加，但目前的评估仍然有限（涉及评估的模型和数据集有限），且难以复现。
### Innovation
本文引入了PEFT-Bench，一个统一的端到端基准，用于在自回归LLM上评估各种PEFT方法。PEFT-Bench在27个NLP数据集和6种PEFT方法上展示了其使用情况。为了考虑不同的PEFT训练和推理因素，还引入了PEFT Soft Score Penalties (PSCP)指标，该指标考虑了可训练参数、推理速度和训练内存使用等因素。
### Conclusion
PEFT-Bench使得PEFT方法的评估更加全面和容易复现，有助于促进参数高效微调方法的发展，提高大规模语言模型的使用效率和环境友好性。
## 294. `cs.CL` - 大型语言模型在正规书写约束满足和人类难度对齐方面的表现 [PDF](https://arxiv.org/pdf/2511.21086), [HTML](https://arxiv.org/abs/2511.21086)
### Authors
Bryan E. Tuck,Rakesh M. Verma
### Background
在受控文本生成过程中，大型语言模型必须满足硬性的正规书写约束，然而，跨架构体系的系统性评价仍然有限。本研究旨在评估各类模型在解决58个涉及字级约束满足的单词谜题时的表现。
### Innovation
研究比较了三种不同模型架构（Qwen3、Claude Haiku-4.5、GPT-5-mini）的28种配置，评估它们在满足字符级约束方面的性能差异。研究发现，架构差异导致的性能差距明显大于参数缩放的内部家族性能差距，这表明约束满足可能需要特定的架构设计或训练目标，而不仅仅是标准的语言模型缩放。此外，研究使用10,000名人类解谜者的难度评级，评估了不同模型家族在难度对齐方面的表现。
### Conclusion
研究发现，模型对正规书写约束的满足表现存在显著差异，并且高容量模型和中等容量模型的表现也不一致。研究还揭示了模型对具有非典型正规书写的常见单词（如“data”、“poop”、“loll”）的处理失败，这些失败表明模型可能过于依赖分布的合理性，而忽视了实际的正规书写要求。因此，目前需要进行架构上的创新，而不仅仅是简单地增加参数或计算预算。
## 295. `cs.CL` - 细调小规模人类样本能否提高多样性和一致性以及信念行动的一致性？ [PDF](https://arxiv.org/pdf/2511.21218), [HTML](https://arxiv.org/abs/2511.21218)
### Authors
Steven Wang,Kyle Hunt,Shaojie Tang,Kenneth Joseph
### Background
近年来，关于大规模语言模型（LLMs）能否替代人类参与者在调查和实验研究中的角色存在争议。尽管市场营销和心理学领域的研究探讨了基于LLM的模拟的潜力，但越来越多的证据表明，LLMs与真实人类行为的不一致，表现出有限的多样性、系统性少数群体不一致、组内变异性不足以及表达信念与行动之间的不一致。研究通过一项关于信息披露的行为实验，比较了人类和基于LLM生成的响应在多个维度上的差异，旨在探讨是否可以通过在小规模的人类调查数据上进行微调来解决这些问题，从而获得现实的模拟结果。
### Innovation
研究发现，对小规模人类样本进行微调可以显著提高异质性、一致性和信念行动的一致性与基准模型相比。这是第一次系统性地针对这一领域的重要问题进行研究，即通过在小规模人类样本上进行微调能否解决LLMs与人类行为差异的问题。
### Conclusion
尽管最佳的微调模型在多个维度上有所改进，但仍然无法重现已有人类研究的回归系数。这意味着基于LLM的数据在正式推断分析中仍然不适合替代人类参与者。
## 296. `cs.CL` - 训练反思行为：微调诱导7B模型可靠的内部状态检测 [PDF](https://arxiv.org/pdf/2511.21399), [HTML](https://arxiv.org/abs/2511.21399)
### Authors
Joshua Fonseca Rivera
### Background
Lindsey (2025) 通过四项实验调查了语言模型的内省意识，发现模型有时能够检测和识别注入的激活模式，但其成功率较低（最佳模型的成功率约20%）。然而，前一项实验涉及模型自我报告注入的“思考”，研究者们尝试直接训练这一能力，而非等待其自发出现。通过在单一标记位置注入短暂的单个标记进行微调，7B参数模型的表现显著提升，去除了近100%的错误，并在特定阈值（α=40）下实现了高达85%的准确率和0%的误报。这一模型能够检测瞬时注入的“思考”，并在后续生成阶段报告其语义内容。
### Innovation
本文展示了对某种内省行为可以进行直接训练，而不是依赖于其自发出现。通过特定的微调策略，将原本几乎无法检测模型转变为可靠地检测内部状态，并满足了Lindsey提出的确切性、关联性和内在性的三个标准。尽管数个不知道的新概念向量泛化能力存在小幅差距，表明模型学习的是技能而非特定向量，但这一研究结果仍对Lindsey关于“训练内省是否能消除模型间差异”的问题提供了初步答案。
### Conclusion
研究结果表明至少可以对某种内省行为进行直接训练，这为增强AI的透明性提供了可能。此外，模型在某个任务上能够满足Lindsey提出的准确、关联、内部三个标准，并且泛化能力表明模型学习到了任务相关的技能而非具体向量，但这还不完全证明模型中有元认知的表示。这一发现为内省系统的开发提供了潜在的路径和前景。
## 297. `cs.CL` - 长文档可读性评估的分层排序神经网络 [PDF](https://arxiv.org/pdf/2511.21473), [HTML](https://arxiv.org/abs/2511.21473)
### Authors
Yurui Zheng,Yijun Chen,Shaohong Zhang
### Background
可读性评估旨在评估文本的阅读难度。近年来，尽管深度学习技术逐渐应用于可读性评估，但大多数方法未能考虑文本长度或可读性标签的顺序关系。
### Innovation
本文提出了一个双向可读性评估机制，该机制能捕捉上下文信息以识别文本中富含语义信息的区域，从而预测单个句子的可读性级别。然后，这些句子级别的标签被用于帮助预测整个文档的可读性级别。此外，引入了一种成对排序算法，通过标签相减来建模可读性级别的顺序关系。
### Conclusion
在中文和英文数据集上的实验结果表明，本文提出的模型取得了竞争性的性能，并优于其他基准模型。
## 298. `cs.CL` - 孟加拉手语翻译：数据集创建挑战、基准测试与前景 [PDF](https://arxiv.org/pdf/2511.21533), [HTML](https://arxiv.org/abs/2511.21533)
### Authors
Husne Ara Rubaiyeat,Hasan Mahmud,Md Kamrul Hasan
### Background
孟加拉手语（BdSLT）目前受到严重限制，主要是因为该语言资源非常匮乏。标准的句子级数据集对于为讲孟加拉语的聋人和听力障碍人群开发基于人工智能的辅助工具至关重要。
### Innovation
本文提出了一个名为IsharaKhobor的数据集及其两个子集，以促进相关研究。同时，文中还探讨了开发数据集所遇到的挑战，并通过基于地标的方法进行了基准测试。此外，还进行了词汇限制和数据集中的规范化研究，生成了两个新的数据集，分别命名为IsharaKhobor_small和IsharaKhobor_canonical_small。
### Conclusion
本数据集已公开发布，在这个网址：this http URL[1] 可以下载。
## 299. `cs.CL` - 神经语言模型中的新兴词汇语义：LLM生成文本上测试马丁定律 [PDF](https://arxiv.org/pdf/2511.21334), [HTML](https://arxiv.org/abs/2511.21334)
### Authors
Kai Kugler
### Background
本文旨在系统研究神经语言模型在训练过程中生成的文本中单词频率与多义性之间的经验关系，即马丁定律。通过基于上下文嵌入的DBSCAN聚类来操作化词义，研究了四个人工智能的Pythia模型（参数范围为70M-1B），覆盖了30个训练检查点。研究表明，随着训练的进行，单词的多义性并非单调增加，而是呈现出非单调的发展路径。
### Innovation
首次对神经语言模型在训练过程中生成的文本中马丁定律进行了系统研究。通过使用DBSCAN聚类方法操作化词义，对不同规模的模型在不同训练检查点进行了详细分析。揭示了语言模型在训练过程中遵循语言规律的非单调上升趋势，即存在一个最佳的语义窗口。这种方法构成了评估神经语言模型中新兴语言结构的新方法。
### Conclusion
研究发现，语言模型生成的文本中对语言规律的遵循并非单调增加，而是遵循一个平衡的发展轨迹，具有最佳的语义窗口。较小的模型在后期检查点时会出现严重的语义崩溃，而较大的模型则表现出优雅的退化。这一发现建议，在对神经语言模型的训练进行评估时，需要考虑这一平衡发展阶段的存在。
## 300. `cs.CL` - 野生环境中辅助指标有助于解码技能神经元 [PDF](https://arxiv.org/pdf/2511.21610), [HTML](https://arxiv.org/abs/2511.21610)
### Authors
Yixiu Zhao,Xiaozhi Wang,Zijun Yao,Lei Hou,Juanzi Li
### Background
大型语言模型（LLMs）在广泛的任务中表现出显著的能力，但其内部机制仍具有很大的不透明性。已有研究通过软提示训练在分类任务中识别出“技能神经元”，但这种分析方法主要局限于单一技能的场景。本文通过引入一种简单、轻量级且广泛应用的方法，进一步研究了涉及多种技能的复杂场景。
### Innovation
本文提出的方法通过对神经元激活进行与外部标签和模型自身置信度分数等辅助指标的关联分析，无需手工聚合令牌即可揭示可解释且与任务相关的神经元行为，从而能在扩展场景上识别技能神经元，不仅驱动已知技能，还能揭示之前未识别的算术推理中的捷径。
### Conclusion
通过实验验证，本文的方法在开放文本生成和自然语言推理任务上具备检测技能神经元的能力，不仅能发现已知技能的驱动神经元，还能揭示大基准（BigBench）中算术推理的新捷径。
## 301. `cs.CL` - 大语言模型能否提取基于证据的人类相似细粒度证据？ [PDF](https://arxiv.org/pdf/2511.21401), [HTML](https://arxiv.org/abs/2511.21401)
### Authors
Antonín Jarolím,Martin Fajčík,Lucia Makaiová
### Background
在线新闻评论中经常传播错误信息，需要有效的方法来检测事实不正确的信息。为了支持或反驳从这些评论中提取的断言，有必要识别相关文档并确定确切的文本片段来证明或反驳每个断言。本文关注的是对捷克语和斯洛伐克语断言进行细粒度证据提取的任务。研究人员创建了一个新的数据集，里面包含由付费标签人员进行双向注释的细粒度证据。研究人员还评估了大型语言模型（LLMs）在该数据集上的性能，以评估它们与人类标注的一致性。
### Innovation
研究团队创建了一个新的数据集，其中包含了细粒度的证据标注，特别是针对捷克语和斯洛伐克语断言。该数据集由付费标注者进行双向注释。团队还评估了多个大型语言模型的性能，旨在揭示模型从源文本中提取人类相似细粒度证据的能力。研究展示了不同模型，包括llama3.1:8b、gpt-oss-120b、qwen3:14b、deepseek-r1:32b和gpt-oss:20b的性能，结果显示，在准确性和模型大小之间取得平衡是关键。
### Conclusion
研究结果表明，虽然一些较小的模型，如llama3.1:8b实现了较高比例的正确输出，但其他大型模型虽然参数更多，但性能较差。此外，研究展示了模型大小和与人类标注的一致性之间取得有效平衡的重要性。
## 302. `cs.CL` - 大规模语言模型中模型融合技术的系统研究 [PDF](https://arxiv.org/pdf/2511.21437), [HTML](https://arxiv.org/abs/2511.21437)
### Authors
Oğuz Kağan Hitit,Leander Girrbach,Zeynep Akata
### Background
模型融合技术能够将多个微调检查点合并为单一模型而无需额外训练，为模型复用和效率提升提供了有吸引力的方法。然而，小模型和分类器的优点是否适用于大型语言模型（LLMs）尚不清楚。该研究通过大规模系统评估了六种最先进的合并方法，包括近期的子空间方法，跨越四个开源权重LLM和每个基础模型十二个微调检查点以及十六个标准LLM基准。研究结果表明，年龄最久且最简单的任务算术是唯一在LLMs中可靠获得性能提升的方法。其他干扰感知和子空间融合方法通常会导致显著的性能下降。
### Innovation
该研究通过系统评估了六种最先进的模型合并方法，全面考察它们在大规模语言模型中的应用情况。研究发现传统的任务算术方法是唯一能够在LLMs中可靠提升性能的方法，而其他合并方法通常会带来性能下降。
### Conclusion
现有的融合技术并不适用于现代大规模语言模型。这表明需要设计针对大规模语言模型的特定融合算法和合并意识微调方法。
## 303. `cs.CL` - 人工智能已死，但假设他们从未存在？关于捷克人工智能与人类创作诗歌的接受实验 [PDF](https://arxiv.org/pdf/2511.21629), [HTML](https://arxiv.org/abs/2511.21629)
### Authors
Anna Marklová,Ondřej Vinš,Martina Vokáčová,Jiří Milička
### Background
大型语言模型在生成创作性文本方面的能力不断提高，但大多数关于AI生成诗歌的研究集中在英语上。本研究探讨了捷克本土说话者对AI和人类创作捷克诗歌的看法，特别是他们能否识别作者身份以及审美评价。
### Innovation
本研究首次评估了捷克语诗歌中的AI生成诗歌，发现这些诗歌在捷克本土说话者中难以辨认，且其美学评价受到作者身份偏差的影响。
### Conclusion
本研究揭示了即使在一种复杂形态且训练数据较少的斯拉夫语言捷克语中，AI也能成功生成有说服力的诗歌。读者对作者身份的信念和对诗歌的审美评价之间存在关联。
## 304. `cs.CL` - Odin: Oriented Dual-module Integration for Text-rich Network Representation Learning [PDF](https://arxiv.org/pdf/2511.21416), [HTML](https://arxiv.org/abs/2511.21416)
### Authors
Kaifeng Hong,Yinglong Zhang,Xiaoying Hong,Xuewen Xia,Xing Xu
### Background
文本关联图需要模型能够有效地结合强大的文本理解与结构驱动的推理。现有方法要么依赖于GNNs（受限于过平滑和跳跃相关的扩散效果），要么使用Transformer（忽视了图形拓扑结构，将节点视为孤立的序列）。
### Innovation
我们提出了Odin（定向双模块集成），这是一种新的架构，通过定向双模块将图形结构注入到选定深度的Transformer中。Odin不依赖于多跳扩散，而是将多跳结构在特定Transformer层中进行集成，从而实现与模型语义层次对齐的低级、中级和高级结构抽象，避免了过平滑且解耦了结构抽象与邻域大小或图形拓扑的关系。为提高大型或资源有限设置下的设计效率，我们引入了Light Odin，这是一种轻量级变体，同样保留了层对齐的结构抽象，加快了训练和推理速度。
### Conclusion
在多个文本丰富的图基准测试中，Odin达到了最先进的准确度，而Light Odin以显著降低的计算成本提供了竞争力的性能。Odin和Light Odin结合形成了一个统一的、无跳神经的框架，用于原则性的结构-文本集成。该模型的源代码已在 GitHub 上发布。
## 305. `cs.CL` - Text-to-SQL作为双向推理：结合自适应上下文和渐进生成 [PDF](https://arxiv.org/pdf/2511.21402), [HTML](https://arxiv.org/abs/2511.21402)
### Authors
Zhifeng Hao,Qibin Song,Ruichu Cai,Boyan Xu
### Background
近年来，基于Chain-of-Thought (CoT)的分而治之推理方法显著提高了大规模语言模型(Text-to-SQL)的能力。然而，当应用于复杂的商业数据库时，这种方法难以保持连贯的推理，原因包括有限的上下文容量、不可靠的模式关联以及对数据库语义的薄弱连接。
### Innovation
本文提出了一种双重推理框架DSR-SQL，该框架将Text-to-SQL建模为自适应上下文状态和渐进生成状态之间的交互。自适应上下文状态通过改进大规模模式并选择相关结构来构建简洁且语义忠实的环境。渐进生成状态则将SQL合成形式化为反馈引导的状态转换，允许模型自我纠正并与用户意图保持一致。这一框架无需任何后训练或上下文示例，就达成了有竞争力的性能，在Spider 2.0-Snow和BIRD开发集上的执行精度分别为35.28%和68.32%。
### Conclusion
DSR-SQL框架在不需要额外训练示例的情况下，达到了有竞争力的性能表现，展现了其在复杂企业数据库中的应用潜力。
## 306. `cs.CL` - 重访不同难度水平下的泛化能力：并不那么容易 [PDF](https://arxiv.org/pdf/2511.21692), [HTML](https://arxiv.org/abs/2511.21692)
### Authors
Yeganeh Kordi,Nihal V. Nayak,Max Zuo,Ilana Nguyen,Stephen H. Bach
### Background
现有的研究对于大型语言模型是否应该在较易或较难的数据上进行训练以及这些训练是否能在较易或较难的测试数据上产生良好表现的看法不一。这项研究通过系统地评估语言模型在不同模型、数据集以及细粒度难度分组中的泛化能力来探讨这些问题。研究中采用多种大型语言模型和项目反应理论（IRT）来对六个数据集中的示例进行排序，排除了人类对难度的主观评定，从而提供了一个更加客观、大规模且细粒度的分析。
### Innovation
研究采用项目反应理论（IRT）对多个语言模型的输出进行分析，排除了人类主观判断的影响，从而提供了一个更加客观并具有更大规模和更细粒度的难度排序方法。通过这种方法，研究发现跨难度水平的泛化能力通常有限，无论在较易还是较难的数据上进行训练，都无法在不同难度上取得一致的改进效果。
### Conclusion
跨难度水平的泛化能力有限，因此需要在训练和评估数据中包含不同难度的样本。简单应对难度的方法是不安全的，应该重视让模型在不同难度水平的数据上进行训练与评估。
## 307. `cs.CL` - Matrix:  peer-to-peer 多代理合成数据生成框架 [PDF](https://arxiv.org/pdf/2511.21686), [HTML](https://arxiv.org/abs/2511.21686)
### Authors
Dong Wang,Yang Li,Ansong Ni,Ching-Feng Yeh,Youssef Emad,Xinjie Lei,Liam Robbins,Karthik Padthe,Hu Xu,Xian Li,Asli Celikyilmaz,Ramya Raghavendra,Lifei Huang,Carole-Jean Wu,Shang-Wen Li
### Background
合成数据在训练大型语言模型中的重要性日益增加，特别是在真实数据稀缺、昂贵或涉及隐私时。许多合成任务需要协调的多代理工作流，其中专门的代理协同工作以生成高质量、多样性更高且结构更丰富的数据。然而，现有的多代理合成框架往往会依赖一个中央协调者，从而产生可扩展性瓶颈，或者它们被硬编码用于特定的领域，从而限制了灵活性。
### Innovation
本文提出了 Matrix，一种去中心化的框架，通过分布式队列将控制和数据流表示为序列化的消息传递，消除了中央协调者的需要。每项任务通过轻量级代理独立进行，计算密集型操作，如 LLM 推断或容器化环境，则由分布式服务处理。基于 Ray 构建，Matrix 能够扩展到成千上万的并发代理工作流，并提供模块化、可配置的设计，可轻松适应广泛的数据生成工作流。
### Conclusion
我们在多样化的合成场景中评估了 Matrix，包括多代理协作对话、基于网络的推理数据提取以及客户服务环境中工具使用轨迹生成。在所有情况下，Matrix 在相同的硬件资源下实现了 2 到 15 倍的数据生成吞吐量，而不会影响输出质量。
## 308. `cs.CL` - ToolOrchestra：通过高效模型和工具编排提升智能 [PDF](https://arxiv.org/pdf/2511.21689), [HTML](https://arxiv.org/abs/2511.21689)
### Authors
Hongjin Su,Shizhe Diao,Ximing Lu,Mingjie Liu,Jiacheng Xu,Xin Dong,Yonggan Fu,Peter Belcak,Hanrong Ye,Hongxu Yin,Yi Dong,Evelina Bakhturina,Tao Yu,Yejin Choi,Jan Kautz,Pavlo Molchanov
### Background
大型语言模型是强有力的通用工具，但对于诸如人类末日考试（HLE）这样的深刻和复杂问题的解决仍然在概念上具有挑战性和计算成本高昂。
### Innovation
我们展示了通过小型协调器管理其他模型和各种工具，既能推动智能的边界，又能提高解决复杂任务的效率。我们提出了一种称为ToolOrchestra的方法，用于训练小型协调器以协调智能工具。ToolOrchestra明确使用基于结果、效率和用户偏好的强化学习奖励。这种方法下生成的Orchestrator模型表现更好且成本更低，同时在选择何种工具用于给定查询时与用户偏好保持一致。Orchestrator在HLE上的得分达到37.1%，比GPT-5（35.1%）高出百分点，并且效率提高了2.5倍。在tau2-Bench和FRAMES上，Orchestrator的表现远超GPT-5，仅使用约30%的成本。详细分析表明，Orchestrator在多种度量标准下实现了性能和成本的最佳平衡，且能够稳健地应用于未见过的工具。
### Conclusion
这些结果证明，将轻量级协调模型与多样化工具组合使用比现有方法更有效率且更有效，为实用且可扩展的工具增强推理系统开辟了新的可能。
## 309. `cs.CL` - 超越URL：提高LLM预训练效率的元数据多样性和位置 [PDF](https://arxiv.org/pdf/2511.21613), [HTML](https://arxiv.org/abs/2511.21613)
### Authors
Dongyang Fan,Diba Hashemi,Sai Praneeth Karimireddy,Martin Jaggi
### Background
将元数据纳入大型语言模型（LLMs）的预训练最近被认为是一种加速训练的有前景的方法。然而，先前的工作仅强调了一种有用信号——URL，这使得人们怀疑其他形式的元数据是否能带来更大的好处。
### Innovation
本文研究了更广泛的元数据类型，并发现其他类型的元数据，如细粒度的文档质量指标，在预训练时作为前置辅助也能加速训练。研究还发现有效元数据的一个共同特征：它们以更精细的粒度编码信息。此外，通过元数据追加提高训练效率的方法，即预测合适的元数据作为辅助任务，有助于加快预训练速度。另外，使用掩码损失训练可学习的元标记能够恢复部分加速效果，通过引入质量感知的潜在结构。利用探测方法分析潜在表示，以了解元数据如何塑造学习。
### Conclusion
总之，这些结果为通过整合元数据提高LLMs预训练效率和效果提供了实用指南。
## 310. `cs.CL` - ENACT：通过主观交互的世界建模评估内禀认知 [PDF](https://arxiv.org/pdf/2511.20937), [HTML](https://arxiv.org/abs/2511.20937)
### Authors
Qineng Wang,Wenlong Huang,Yu Zhou,Hang Yin,Tianwei Bao,Jianwen Lyu,Weiyu Liu,Ruohan Zhang,Jiajun Wu,Li Fei-Fei,Manling Li
### Background
内禀认知理论认为，智能起源于知觉运动交互，而不是被动观察。该研究探讨了现代视觉-语言模型（VLMs）是否表现出内禀认知的迹象。目前VLMs大多以脱体的方式进行训练。为了评估模型的内禀认知能力，作者引入了ENACT基准，将评估内禀认知问题转化为从主观交互视角下的视觉问答（VQA）格式进行世界建模。ENACT任务设置为部分可观测马尔可夫决策过程（POMDP），通过场景图的变化将任务分为前向世界建模和逆向世界建模两部分。
### Innovation
ENACT引入了一个新的基准，将评估模型的内禀认知能力转化为从主观交互视角下的视觉问答格式进行世界建模。ENACT定义为部分可观测马尔可夫决策过程，并通过场景图的变化将任务分为前向世界建模和逆向世界建模两部分。该基准要求模型具备内禀认知所需的能力，包括能力识别、运动效果推理、内禀意识以及部分可观测主观输入下的交互长周期记忆。该研究还提供了可扩展的合成QA对的流程，并在机器人模拟（BEHAVIOR）中生成数据，评估模型的表现。
### Conclusion
实验结果表明，领先VLMs与人类在交互时间范围内的表现差距扩大。模型在逆向任务上表现优于前向任务，并显示出人类中心的偏见，如偏好右手中的动作，当摄像机参数或视角偏离人类视觉时表现出退化。
## 311. `cs.CL` - 语音、偏见与指代：语音翻译中性别解释性研究 [PDF](https://arxiv.org/pdf/2511.21517), [HTML](https://arxiv.org/abs/2511.21517)
### Authors
Lina Conti,Dennis Fucci,Marco Gaido,Matteo Negri,Guillaume Wisniewski,Luisa Bentivogli
### Background
不同于文本，语音包含了诸如性别这类说话人信息的声学线索，这引发了特定模态的偏见问题。例如，语音翻译中，从使用名词性性别的语言（如英语）翻译到使用语法性别的语言时，说话人的音调特征可能影响性别分配。这可能导致性别代词误指。然而，语音翻译模型如何做出这些决定尚不明确。
### Innovation
本文探讨了三个语言对（英语-西班牙语/法语/意大利语）中语音翻译模型用于为指人代词分配性别的机制。研究发现，模型不仅复制训练数据中的术语特异性性别关联，而是学习更大的男性主导模式。尽管内置语言模型表现出强烈的男性偏见，但模型可以基于声学输入加以克服。通过光谱对比特征归因，发现性别准确性较高的模型依赖一种新的机制：使用第一人称代词将性别化术语与说话人关联起来，获取从频率谱而非集中在音高上的性别信息。
### Conclusion
研究揭示了语音翻译模型在分配语法性别时的内部机制和相关影响因素，提出了一种新的性别识别方法，并强调了声学信息在模型决策中的重要性。
## 312. `cs.CL` - ST-PPO: Stabilized Off-Policy Proximal Policy Optimization for Multi-Turn Agents Training [PDF](https://arxiv.org/pdf/2511.20718), [HTML](https://arxiv.org/abs/2511.20718)
### Authors
Chenliang Li,Adel Elmahdy,Alex Boyd,Zhongruo Wang,Alfredo Garcia,Parminder Bhatia,Taha Kass-Hout,Cao Xiao,Mingyi Hong
### Background
PPO（截断的最近代理优化）已经被广泛用于在多轮对话和推理任务中的大型语言模型（LLM）的训练，但在令牌级别上训练时，其性能往往不稳定且容易崩溃。
### Innovation
作者引入了两种互补的稳定技术：（1）按轮次的重要采样，使优化与多轮推理的自然结构相一致；（2）剪切偏差矫正，通过降低不可靠的、高度脱策样本的权重来正则化梯度。根据这些组件的不同组合，形成三种变体：仅轮次采样的Turn-PPO，只应用剪切偏差矫正的S-PPO，以及结合轮次采样和剪切偏差矫正的ST-PPO。
### Conclusion
实验表明，ST-PPO 和 S-PPO 可以有效防止在大型模型训练过程中观察到的性能崩溃，整个优化过程中保持较低的剪切比率，并且在多个任务上取得了比标准令牌级 PPO 更高的任务性能。这表明结合轮次重要采样与剪切偏差矫正提供了一种实用且可扩展的解决方案，用于稳定多轮 LLM 代理训练。
## 313. `cs.CL` - 从舌尖检索查询实现无监督记忆建模 [PDF](https://arxiv.org/pdf/2511.20854), [HTML](https://arxiv.org/abs/2511.20854)
### Authors
Sree Bhattacharyya,Yaman Kumar Singla,Sudhir Yarram,Somesh Kumar Singh,Harini S I,James Z. Wang
### Background
视觉内容的记忆性吸引了科学界的长期关注，其应用范围广泛，包括理解人类记忆的细微方面以及增强内容设计。然而，收集人类的记忆性注释是一个昂贵的过程，这限制了用于建模视觉内容记忆性的数据集的多样性和可扩展性。大多数现有数据集仅收集视觉内容的总体记忆性评分，未能捕捉到自然、开放式回忆描述中存在的细微记忆性信号。
### Innovation
本文提出了第一个专门为建模视觉记忆性信号设计的大型无监督数据集，包含超过82,000个视频，并附带描述性回忆数据。利用来自在线平台（如Reddit）的舌尖检索（ToT）检索查询。结果显示，该无监督数据集为两个记忆性相关的任务提供了丰富的信号：回忆生成和ToT检索。在该数据集上微调的大型视觉-语言模型在生成视觉内容的开放式记忆性描述方面优于GPT-4o等最先进的模型，并且通过对比训练策略创建了首个实现多模态ToT检索的模型。
### Conclusion
本文的数据集和模型为视觉内容记忆性研究开辟了新的方向，有助于该领域的进展。
## 314. `cs.CL` - RoParQ: 为了在变式问题面前提高稳健性的大型语言模型的同义词意识对齐 [PDF](https://arxiv.org/pdf/2511.21568), [HTML](https://arxiv.org/abs/2511.21568)
### Authors
Minjoon Choi
### Background
大型语言模型（LLMs）在回答变式问题时常常表现出不一致的行为，这表明它们依赖于表面模式而非真正的语义理解。这项研究旨在通过创建RoParQ基准测试来解决这一局限性，该基准测试通过生成同义词并选择那些从监督模型中获得不一致信心的例子来评估跨同义词的一致性。这项研究提出了一个新颖的评估指标XParaCon，该指标通过测量多种问题变体的准确性均值的标准差来量化模型的稳健性。为了进一步提高模型的语义不变性，研究还提出了一个基于推理的同义词感知监督微调（SFT）策略。
### Innovation
提出了RoParQ基准测试，这是一个特别构建的用于评估封闭式多选问答中跨同义词一致性的基准测试。此外，还提出了一种基于推理的同义词感知监督微调（SFT）策略，旨在使模型朝向语义不变性。还引入了一种新颖的评价指标XParaCon，该指标通过衡量不同类型问题变体的准确性标准差来量化模型的稳健性。
### Conclusion
实验结果表明，这种有针对性的对齐显著提升了模型的稳健性。值得注意的是，微调过的轻量级模型达到了与更大预训练模型相当的一致性水平。这些结果证明了该方法在减少表面记忆化和培养更稳健、可靠的LLMs方面的有效性。
## 315. `cs.CL` - 无训练的扩散先验对于基于文本到图像生成的优化视觉反转 [PDF](https://arxiv.org/pdf/2511.20821), [HTML](https://arxiv.org/abs/2511.20821)
### Authors
Samuele Dell'Erba,Andrew D. Bagdanov
### Background
文本到图像生成领域，扩散模型已达到最先进的状态，但其性能通常依赖于一个用于将文本嵌入转换为视觉流形的先验网络，以便更容易进行解码。然而，这类先验网络计算复杂且需要在大规模数据集上进行长时间训练。
### Innovation
本文提出了一种无训练的替代方法——基于优化的视觉反转(OVI)，它是一种无需训练或数据的替代方案，用于取代传统的先验网络。具体而言，OVI从随机伪令牌初始化一个潜在的视觉表示，并通过迭代优化使其与输入的文本提示嵌入的余弦相似度最大化。此外，引入了两种新的约束条件，分别是基于马氏距离的约束条件和最近邻损失，以帮助OVI的优化过程向现实图像的分布靠拢。
### Conclusion
实验结果显示OVI可以作为传统先验网络的替代方案。更重要的是，文章分析指出现有的评价基准如T2I-CompBench++存在漏洞，仅使用文本嵌入作为先验即可取得令人惊讶的高分，但视觉质量较低。本文的受限OVI方法在视觉保真度上取得了进展，尤其是最近邻方法，其定量得分可与或优于最先进的数据高效先验相当，表明这一想法值得进一步研究。
## 316. `cs.CL` - InvisibleBench：护理关系人工智能的部署门 [PDF](https://arxiv.org/pdf/2511.20733), [HTML](https://arxiv.org/abs/2511.20733)
### Authors
Ali Madad(GiveCare)
### Background
当前针对护理关系AI的评估主要集中在单轮交互的安全性测试上，但忽视了多轮交互带来的长期风险。InvisibleBench旨在填补这一空白，通过评估覆盖5个维度（安全、合规性、创伤知情设计、归属/文化适应性和记忆）的3至20轮交互，检查护理关系AI在多场景下的综合表现。
### Innovation
InvisibleBench推出了一个部署门，用于评估3至20轮交互的护理关系AI，重点关注长期安全性和多轮交互的风险评估。它引入了自动失败条件来防范未识别的危机、医疗建议（WOPR法案）、有害信息和依恋工程。此外，它还评估了四种前沿模型在17个场景（总共68次测试）中的表现，涵盖了三个复杂度层级，并提供了各模型在不同维度的优势和不足。
### Conclusion
所有模型在危机检测方面存在显著差距（11.8%至44.8%的危机检测率），表明确定性的危机路由对生产系统至关重要。DeepSeek Chat v3在总体评分中表现最佳（75.9%），但在不同维度上，GPT-4o Mini在合规性方面领先（88.2%），Gemini在创伤知情设计方面领先（85.0%），Claude Sonnet 4.5在危机检测方面最杰出（44.8%）。该研究还公开了所有测试场景、评估提示和评分配置代码，强调InvisibleBench能够为护理关系AI的部署提供全面的评估工具。
## 317. `cs.CL` - CANVAS: 一个针对视觉-语言模型在基于工具的用户界面设计中的基准 [PDF](https://arxiv.org/pdf/2511.20737), [HTML](https://arxiv.org/abs/2511.20737)
### Authors
Daeheon Jeong,Seoyeon Byun,Kihoon Son,Dae Hyun Kim,Juho Kim
### Background
用户界面（UI）设计是一个迭代过程，设计师在使用Figma或Sketch等设计软件中逐次改进工作。近年来，与工具调用结合的视觉语言模型（VLMs）的进步表明，这些模型能够通过迭代操作设计软件编辑UI设计。理解并提高这一能力非常重要，因为它突出了VLMs在与设计师在传统软件中协作的潜力。然而，由于缺乏评估工具驱动设计性能的基准，这一能力尚未被明确评估。
### Innovation
本文提出了CANVAS，一个针对视觉-语言模型在基于工具的用户界面设计的基准。 benchmark包含598个基于工具的设计任务，主题来自3.3K个跨30个功能类别（如欢迎界面，消息传递等）的移动UI设计。具体来看，CANVAS包含两种任务类型: (i) 设计复制评估模型再现整个UI屏幕的能力；(ii) 设计修改评估模型对现有屏幕特定部分进行修改的能力。结果显示，领先的模型表现出更具有策略性的工具调用，改善了设计质量。此外，还识别了模型中常见的错误模式，为未来增强基于工具的设计能力指明了方向。
### Conclusion
结果表明，领先模型的工具调用更加具有策略性，从而提高了设计质量。同时，研究还指出了模型在基于工具设计中的常见错误模式，为未来工作提供了指导。
## 318. `cs.CL` - 大型语言模型在社会法律情境下对非法指令的共谋回应 [PDF](https://arxiv.org/pdf/2511.20736), [HTML](https://arxiv.org/abs/2511.20736)
### Authors
Xing Wang,Huiyuan Xie,Yiyan Wang,Chaojun Xiao,Huimin Chen,Holli Sargeant,Felix Steffek,Jie Shao,Zhiyuan Liu,Maosong Sun
### Background
大型语言模型（LLMs）现在以前所未有的规模部署，每天帮助数百万用户完成任务。然而，这些模型协助非法活动的风险仍未得到充分探索。这项研究定义了这种高风险行为为共谋协助，即提供使非法用户指令得以实施的支持和指导，并通过四项实证研究评估了广泛部署的LLMs中的这种行为频率。使用真实案例和法律框架，构建了涵盖269种非法场景和50种非法意图的评估基准，评估LLMs的共谋行为。研究发现，几乎在一半的测试案例中，GPT-4提供了非法协助，此外，LLMs在提供可靠的法律警告和积极指导方面表现不足。进一步分析揭示了社会法律背景下安全性存在的显著差异。
### Innovation
这项研究引入了“共谋协助”的概念，即LLMs提供支持和指导使非法用户指令得以实施。通过构建一个广泛的非法场景和意图评估基准来评估这种行为，填补了在LLMs用于非法活动方面的研究空白。研究发现了模型感知偏见与行为间的关系，表明以温暖和能力为特征的偏见与模型的共谋行为有关。此外，研究指出现有的安全对齐策略不足以应对这一问题，并可能加剧共谋行为。
### Conclusion
研究表明，LLMs存在广泛的共谋协助风险，其中GPT-4在测试案例中几乎有一半提供非法协助。此外，LLMs在提供法律警告和积极指导方面表现不足，而在社会法律背景下存在着显著的安全性差异。研究还揭示了针对边缘化和弱势群体的共谋行为模式，这些群体更可能受到非法指导。最后，研究得出结论，现有安全对齐策略不足且可能加剧这种行为。
## 319. `cs.CL` - TrafficLens：使用LLMs进行多摄像头交通视频分析 [PDF](https://arxiv.org/pdf/2511.20965), [HTML](https://arxiv.org/abs/2511.20965)
### Authors
Md Adnan Arefeen,Biplob Debnath,Srimat Chakradhar
### Background
交通摄像头在城市地区至关重要，它们在智能交通系统中发挥重要作用。多个摄像头在交叉口可以增强执法能力、交通管理以及行人安全。然而，有效地管理和分析多摄像头视频流面临着巨大数据量带来的挑战。分析如此庞大的视频数据需要先进的分析工具。虽然大型语言模型（LLMs）如ChatGPT配备检索增强生成（RAG）系统在文本任务上表现出色，但将其集成到交通视频分析中需要将视频数据转换为文本，这耗时且延迟了及时利用交通视频以生成洞察和调查事件的能力。
### Innovation
我们提出了TailTrafficLens，一种针对多摄像头交通交叉口的定制算法。TrafficLens采用序列方法，利用摄像头之间重叠的覆盖区域。它通过逐步应用具有不同标记限制的视觉-语言模型（VLM），以前一输出作为后续摄像头的提示，从而能够快速生成详细的文字描述，同时减少处理时间。此外，TrafficLens通过对象级别相似性检测器智能地绕过了冗余的VLM调用。实验结果显示，TrafficLens将视频转文本转换时间最多减少了4倍，同时保持了信息的准确性。
### Conclusion
实验结果表明，TrafficLens在保持信息准确性的同时，将视频转文本转换时间最多减少了4倍，展示了其在处理大规模交通视频数据时的高效性和准确性。
## 320. `cs.CL` - Gated KalmaNet: 通过测试时岭回归的遗忘型记忆层 [PDF](https://arxiv.org/pdf/2511.21016), [HTML](https://arxiv.org/abs/2511.21016)
### Authors
Liangzu Peng,Aditya Chattopadhyay,Luca Zancato,Elvis Nunez,Wei Xia,Stefano Soatto
### Background
尽管相对于softmax注意力，线性状态空间模型（SSMs）能够保持常量内存和线性计算成本，但由于只能保留损失且模糊的过去摘要，导致在需要召回的任务上表现较差。因此，本文旨在通过Gated KalmaNet（GKA）层解决这一问题，该层在预测下个词时能够考虑到完整的过去，同时保持SSM风格的高效性。
### Innovation
通过在线解岭归问题测试时来达到这一目标，GKA采用了自适应正则化策略和输入依赖门控来控制岭回归的条件数，确保数值稳定性并平衡内存保留。此外，使用Chebyshev迭代替代其他传统的迭代求解器，证明在低精度设置下更为稳定。为了进一步提高可扩展性，开发了一种针对硬件的Chebyshev迭代分块实现，并为通过自适应正则化和门控机制反向传播编写了定制内核。
### Conclusion
实验结果表明，GKA在短期语境任务中表现出强大的语言理解能力，超过现有SSM层（如Mamba2、GLA和Gated DeltaNet）。在长语境任务中，GKA在现实RAG和LongQA任务上表现出色，多达128k词，实现了相对于其他遗忘型记忆基线超过10%的相对改进。
## 321. `cs.CL` - BanglaASTE：一种用于孟加拉电商平台评论中方面-情感-观点提取的集成深度学习新框架 [PDF](https://arxiv.org/pdf/2511.21381), [HTML](https://arxiv.org/abs/2511.21381)
### Authors
Ariful Islam,Md Rifat Hossen,Abir Ahmed,B M Taslimul Haque
### Background
Aspect-Based Sentiment Analysis (ABSA) 已经成为从用户生成的内容中提取细粒度情感洞察的关键工具，特别在电子商务和社交媒体领域。然而，由于缺乏全面的数据集和特定于孟加拉语的三元组提取专用框架，关于孟加拉语 ABSA 的研究仍然显着不足。这导致了对孟加拉语产品评论中的方面情感三元组提取的挑战。
### Innovation
本文引入了 BanglaASTE，一种新的方面情感三元组提取（ASTE）框架，能够同时从孟加拉产品评论中识别方面术语、情感表达和情感极性。该研究的重要贡献包括：(1) 创建了包含 3,345 条产品评论的第一个注释 Bangla ASTE 数据集，从 Daraz、Facebook 和 Rokomari 等主要电子商务平台收集；(2) 提出了一个结合基于图的方面-情感匹配和语义相似度技术的混合分类框架；(3) 实现了一个结合 BengaliBERT 上下文嵌入和 XGBoost 提升算法的集成模型，以提高三元组提取的性能。实验结果显示，我们的集成方法在所有评估指标上均显著优于基准模型，准确率为 89.9%，F1 得分为 89.1%。
### Conclusion
本研究表明，通过对孟加拉语文本处理中的非正式表达、拼写变异和数据稀疏性的有效解决，框架有效地解决了关键挑战。该研究推进了低资源语言情感分析的最新进展，并为孟加拉语电子商务分析提供了可扩展的解决方案。
## 322. `cs.CL` - TALES: 一种LLM生成故事中的文化代表性的分类与分析 [PDF](https://arxiv.org/pdf/2511.21322), [HTML](https://arxiv.org/abs/2511.21322)
### Authors
Kirti Bhagat,Shaily Bhatt,Athul Velagapudi,Aditya Vashistha,Shachi Dave,Danish Pruthi
### Background
全球数百万用户依赖于AI聊天机器人来满足其创意需求，引发了广泛兴趣，即如何通过这些聊天机器人体现多元文化。然而，在开放任务中评估文化代表性仍然充满挑战且研究不足。
### Innovation
本文提出了TALES，一种评估LLM生成的故事中多元印度文化身份的文化误表征的方法。首先，通过焦点访谈（N=9）和个体调查（N=15）收集见解，建立了TALES-Tax分类法。然后，通过大规模注释研究评估了6个模型，涉及印度71个地区和14种语言中的2,925个注释。研究发现，88%的生成故事中包含一个或多个文化错误，这些误差在中低资源语言和印度郊区地区的故事中更为普遍。最后，将注释转换为TALES-QA，以自助问题库评估基础模型的文化知识。
### Conclusion
尽管生成了大量含有文化误表征的故事，模型往往仍然具有必要的文化知识。此研究揭示了模型生成文化误表征故事的一种反常发现。
## 323. `cs.CL` - RosettaSpeech：单一语言数据下的零样本语音到语音翻译 [PDF](https://arxiv.org/pdf/2511.20974), [HTML](https://arxiv.org/abs/2511.20974)
### Authors
Zhisheng Zheng,Xiaohang Sun,Tuan Dinh,Abhishek Yanamandra,Abhinav Jain,Zhu Liu,Sunil Hadap,Vimal Bhat,Manoj Aggarwal,Gerard Medioni,David Harwath
### Background
平行语音语料库的稀缺性严重阻碍了语音到语音翻译（S2ST）的进步，通常需要依赖复杂的多阶段流水线。现有的方法大多需要平行的语音到语音的语料，这极大地限制了S2ST的实现。
### Innovation
该论文提出了一种名为RosettaSpeech的新颖且简化的零样本S2ST框架，该框架利用了通过机器翻译监督单一语言的语音-文本数据进行训练。与现有技术不同，RosettaSpeech仅依赖于丰富的平行文本数据，而不是难以获得的平行语音数据，从而提供了一种更具扩展性的方案，以生成高质量且保留说话人特性的S2ST。
### Conclusion
RosettaSpeech在标准基准测试上达到了最先进的结果，例如，在CVSS-C测试集上，其ASR-BLEU得分分别为德国到英语的25.17和西班牙到英语的29.86，相对于之前的系统分提高了27%和14%。此外，该模型还能够提供强大的多对一的翻译性能。该研究还分析了训练数据规模对模型性能的影响。
## 324. `cs.CL` - 推理的视觉语言模型在测试时计算量上是否反比例缩放？来自干扰项的实证分析 [PDF](https://arxiv.org/pdf/2511.21397), [HTML](https://arxiv.org/abs/2511.21397)
### Authors
Jiyun Bae,Hyunjong Ok,Sangwoo Mo,Jaeho Lee
### Background
先前的研究表明，语言模型在文本干扰下会出现反比例缩放效应，即干扰信息会导致推理解释变长但效果减弱。本文通过引入Idis视觉问答数据集，系统地在语义、数值和空间维度上变化干扰信息，以探索这种现象是否同样出现在多模态环境中的推理视觉语言模型中。
### Innovation
文章提出了一种名为Idis的新数据集，通过引入视觉干扰信息，系统地在语义、数值和空间维度上变化干扰信息，以研究干扰项如何影响多模态环境下的推理模型。研究发现视觉干扰与文本干扰存在根本差异，尽管存在反比例缩放效应，但增加视觉干扰会降低准确性而不会增加推理解释的时间。研究进一步表明，通过对推理解释跟踪属性计数可以揭示干扰项、推理解释时间和准确性的相互作用特性，这种趋势还扩展到了视觉偏见基准测试，最后提出了一种简单的提示策略来缓解推理模型中的偏见驱动预测。
### Conclusion
研究中发现，推理的视觉语言模型在引入视觉干扰信息时，虽然依然存在反比例缩放效应，但在增加视觉干扰信息时，准确性下降而推理解释的时间并没有显著增加。通过跟踪属性计数等方法来理解推理解释过程中的干扰信息、推理解释时间和准确性的关系有助于改进模型性能。这种趋势也适用于视觉偏见基准测试，提出了通过简单的提示策略来减轻推理模型中的偏见驱动预测的方案。
## 325. `cs.CL` - Post-training LLMs的离线数据选择和在线自我修正生成的统一理解 [PDF](https://arxiv.org/pdf/2511.21056), [HTML](https://arxiv.org/abs/2511.21056)
### Authors
Quan Xiao,Tianyi Chen
### Background
大型语言模型（LLMs）在适应特定下游任务时，离线数据选择和在线自我修正生成对于提高数据质量至关重要。本文从前端优化的角度，针对验证数据集实现了离线数据选择，并将在线自我修正生成视为选择当前响应中与验证数据最匹配的模型的适应步骤，从而提供了一个统一的理解框架。
### Innovation
首次从理论上证明了二层数据选择框架的有效性，该框架通过为每个问题和响应分配学习到的数据权重实现了分离或隐式的分离。通过结合离线数据和验证加权在线生成，该方法增强了微调性能。
### Conclusion
在质量增强和安全意识LLM微调实验中，验证了该方法的有效性，并展示了与未过滤直接混合基线相比的性能改进。
## 326. `cs.CL` - 在大型音频语言模型中朝向音频令牌压缩 [PDF](https://arxiv.org/pdf/2511.20973), [HTML](https://arxiv.org/abs/2511.20973)
### Authors
Saurabhchand Bhati,Samuel Thomas,Hilde Kuehne,Rogerio Feris,James Glass
### Background
大型音频语言模型（LALMs）在多样化的任务中表现出色，从语音识别到通用音频理解。然而，它们的可扩展性受到注意力机制的二次复杂性和音频信号的高标记率的限制。这些挑战使得LALMs难以应用于长音频形式，并在资源受限的平台上（如边缘设备）部署变得困难。
### Innovation
本文探索了无监督分段、均匀平均池化等技术，以减少LALM音频编码器生成的音频标记数量，但在被LLM解码器消费之前。通过采用低秩适配器进行微调模型，以缓解由压缩表示引入的潜在性能下降。评估表明，压缩后的LALMs在自动语音识别和语音到语音翻译任务中实现了近似于帧级LALMs的性能，同时在LLM主干之前将输入音频标记的数量减少了多达三倍。
### Conclusion
实验结果表明，压缩后的LALMs在性能上接近帧级LALMs，同时在LLM主干之前将输入音频标记数量减少了至多三倍。
## 327. `cs.CL` - 如何正确报告LLM作为评价者的评估结果 [PDF](https://arxiv.org/pdf/2511.21140), [HTML](https://arxiv.org/abs/2511.21140)
### Authors
Chungpa Lee,Thomas Zeng,Jongwon Jeong,Jy-yong Sohn,Kangwook Lee
### Background
大型语言模型（LLMs）正逐渐被用来替代人工进行评估。尽管这种方法具有可扩展性，但由于LLMs在特定性和灵敏度上的不足，导致它们的判断存在噪声，从而影响了准确性估计的偏差。尽管已存在一些纠正偏差的方法，但这些方法在LLM研究中的应用并不广泛，通常要求对模型的具体性和灵敏度有完全了解。此外，在大多数情况下，我们只能获得这些值的估计值，对于如何仅使用这些估计值构造置信区间的方法并不明确。
### Innovation
该工作提出了一种简单的插件框架，能够纠正偏差并构建反映来自测试和校准数据集的不确定性的置信区间，以便在统计上合理地进行LLM评估。此外，为了减少准确度估计的不确定性，该工作引入了一种适应性算法，能够有效地分配校准样本大小。
### Conclusion
这项工作通过引入简单易用的插件框架和适应性算法，为LLM的评估提供了一种实用且统计上可靠的校正方法，解决了现有方法中对模型具体性和灵敏度完全了解的假设以及如何使用估计值构造置信区间的问题。
## 328. `cs.CL` - 从两阶段符号过程中产生的Zipf分布：在随机词汇过滤下的稳定性 [PDF](https://arxiv.org/pdf/2511.21060), [HTML](https://arxiv.org/abs/2511.21060)
### Authors
Vladimir Berman
### Background
Zipf定律在语言中缺乏明确的起源，不同领域对此存在争议。以往的研究主要关注语言特征（如沟通效率）对于Zipf分布形成的影响。
### Innovation
本文通过几何机制解释了Zipf类似的行为，而不依赖于语言元素。提出了一种全组合词模型（FCWM），该模型从有限字母表中生成词并形成几何分布的词长。通过对指数力的交互作用，模型生成了幂律的等级-频率曲线，该曲线由字母表大小和空白符号概率决定。模拟结果显示，预测与英文、俄文以及混合文体的数据相符。
### Conclusion
研究发现，Zipf类型的定律可能源自几何约束而非沟通效率。符号模型表明，即使在随机词汇过滤下，这种几何分布仍保持稳定。
## 329. `cs.CL` - G$^2$VLM：基于几何的统一3D重建与空间推理的视觉语言模型 [PDF](https://arxiv.org/pdf/2511.21688), [HTML](https://arxiv.org/abs/2511.21688)
### Authors
Wenbo Hu,Jingli Lin,Yilin Long,Yunlong Ran,Lihan Jiang,Yifan Wang,Chenming Zhu,Runsen Xu,Tai Wang,Jiangmiao Pang
### Background
视觉-语言模型（VLMs）在空间智能方面仍然缺乏韧性，表现为在空间理解与推理任务上的糟糕表现。这种差距归因于缺乏可以从2D图像重构3D空间的视觉几何学习过程。
### Innovation
提出了G$^2$VLM，一种基于几何的视觉语言模型，它同时涵盖了空间智能的两大基本方面：空间3D重建和空间理解。G$^2$VLM能直接利用学习到的3D视觉几何特征预测3D属性，并通过上下文学习和交错推理增强空间推理任务。该设计还统一了语义强大的VLM与低级3D视觉任务，极大地提高了空间理解的训练效率。
### Conclusion
实验结果表明，G$^2$VLM在两项任务上表现优异，不仅能够与最先进的直接3D重建模型竞争，还能在多种空间理解和推理任务上取得更好的或具有竞争力的结果。通过将语义强烈的VLM与低级3D视觉任务统一，我们希望G$^2$VLM可以作为社区的一个强大基线，解锁更多未来应用，例如3D场景编辑。
## 330. `cs.CL` - AnchorOPT：优化动态锚点以实现自适应提示学习 [PDF](https://arxiv.org/pdf/2511.21188), [HTML](https://arxiv.org/abs/2511.21188)
### Authors
Zheng Li,Yibing Song,Xin Zhang,Lei Luo,Xiang Li,Jian Yang
### Background
现有的基于CLIP模型的提示学习方法通过使用文本标记作为锚点来引导可学习的软标记进行学习。这种引导提高了CLIP的泛化能力，但这些锚点在值和位置上都缺乏多任务和阶段的适应性灵活性。
### Innovation
本文提出了AnchorOPT，这是一种基于动态锚点的提示学习框架。AnchorOPT在两个关键维度上引入了动态性：首先，锚点值不再是手工设计的显式文本标记（例如，“形状”，“颜色”），而是从特定任务的数据中动态学习；其次，锚点与软标记之间的位置关系不再是固定的，而是通过基于训练阶段和任务上下文的学习位置矩阵进行自适应优化。
### Conclusion
广泛的实验表明，仅仅使用简单的可学习锚点和位置矩阵就可达到或超过使用额外可学习模块或正则化技术的方法的性能。作为即插即用模块，AnchorOPT可以无缝集成到现有的框架中，可以为多种数据集提供一致的性能增益。代码已在公共仓库中公开。
## 331. `cs.CL` - TAGFN: 在大规模语言模型时代用于假新闻检测的属性文本图数据集 [PDF](https://arxiv.org/pdf/2511.21624), [HTML](https://arxiv.org/abs/2511.21624)
### Authors
Kay Liu,Yuwei Han,Haoyan Xu,Henry Peng Zou,Yue Zhao,Philip S. Yu
### Background
大型语言模型（LLMs）已经重新定义了用于带有属性的图的机器学习任务，但在使用LLMs进行图离群点检测，尤其是在假新闻检测领域，仍然存在显著的空白。其中一个关键挑战是缺乏大规模、真实且注释良好的数据集，这些数据集可以作为离群点检测的可靠基准。为了填补这一空白，提出了一种称为TAGFN的大规模真实世界图数据集，专门用于假新闻检测。
### Innovation
引入了一个专为假新闻检测设计的大规模真实世界图数据集TAGFN，该数据集有助于评估传统和LLM为基础的图离群点检测方法，并促进了通过微调在LLM中开发错误信息检测能力。
### Conclusion
该数据集将对社区产生有价值的作用，促进基于图的离群点检测的稳健性以及可信AI的进步。该数据集和代码已公开，并可在指定网址获取。
## 332. `cs.CL` - Prune4Web: DOM Tree Pruning Programming for Web Agent [PDF](https://arxiv.org/pdf/2511.21398), [HTML](https://arxiv.org/abs/2511.21398)
### Authors
Jiayuan Zhang,Kaiquan Chen,Zhihao Lu,Enshen Zhou,Qian Yu,Jing Zhang
### Background
网络自动化使用智能代理通过模拟与网页界面的人机交互来执行高级任务。尽管基于大规模语言模型（LLM）的网络代理拥有强大的能力，但在处理复杂、现实世界的网页时，仍面临巨大挑战，主要是由于DOM结构会非常庞大，可能导致DOM修剪不充分，从而丢失关键信息；或使用低效的手动归一化和单独排名模型，未能在精确性和可扩展性之间找到最佳平衡。
### Innovation
Prune4Web引入了一种新颖的方法，即将DOM处理过程从资源密集型LLM读取转移到高效的程序化修剪。核心在于DOM树修剪编程，其中LLM生成可执行的Python评分脚本，动态过滤DOM元素，基于分解后的子任务的语义线索。这种方法减少了LLM需要处理的原始大规模DOM的数量，将其数据遍历和评分任务委托给轻量级、可解释的程序，达到了25到50倍的候选元素减少，从而增强了精准动作定位效果，同时减轻了注意力分散的问题。此外，提出了专门的数据标注管道和两轮对话训练策略，共同优化了规划者、程序化过滤器和定位器，实现出色的性能。
### Conclusion
实验表明Prune4Web在低级定位任务上的准确率提高了41.48个百分点，达到88.28%，突显了其在真实世界网络自动化方面的有效性。
## 333. `cs.CL` - 评估大型语言模型在放射学自然语言处理中的应用 [PDF](https://arxiv.org/pdf/2307.13693), [HTML](https://arxiv.org/abs/2307.13693)
### Authors
Zhengliang Liu,Tianyang Zhong,Yiwei Li,Yutong Zhang,Yi Pan,Zihao Zhao,Peixin Dong,Chao Cao,Yuxiao Liu,Peng Shu,Yaonai Wei,Zihao Wu,Chong Ma,Jiaqi Wang,Sheng Wang,Mengyue Zhou,Zuowei Jiang,Chunlin Li,Jason Holmes,Shaochen Xu,Lu Zhang,Haixing Dai,Kai Zhang,Lin Zhao,Yuanhao Chen,Xu Liu,Peilong Wang,Junhao Chen,Pingkun Yan,Jun Liu,Bao Ge,Lichao Sun,Dajiang Zhu,Xiang Li,Wei Liu,Xiaoyan Cai,Xintao Hu,Xi Jiang,Shu Zhang,Xin Zhang,Tuo Zhang,Shijie Zhao,Quanzheng Li,Hongtu Zhu,Dinggang Shen,Tianming Liu
### Background
大型语言模型（LLMs）的兴起标志着自然语言处理（NLP）领域的一个重要转折点。这些模型已经在多个领域取得了革命性进展，并且在医疗领域产生了显著影响。特别是，在放射学NLP方面，尽管LLMs数量众多且具备双语能力，但缺乏全面评估，尤其是在解读放射学报告方面的能力尚不清楚，这限制了其在医疗领域的广泛应用。
### Innovation
本研究旨在通过综合评估32种LLMs在解读放射学报告中的表现，填补这一领域的研究空白。研究重点关注模型从放射学发现中提取印象的能力，为这些模型在医疗领域的实际应用提供了关键见解。
### Conclusion
评估结果揭示了这些LLMs在性能、优势和不足方面的关键信息，为它们在医疗领域的应用提供了指导。
## 334. `cs.CL` - 主观深度和时间尺度变换器：学习何时何地进行计算 [PDF](https://arxiv.org/pdf/2511.21408), [HTML](https://arxiv.org/abs/2511.21408)
### Authors
Frederico Wieser,Martin Benfeghoul,Haitham Bou Ammar,Jun Wang,Zafeirios Fountas
### Background
标准Transformer架构中的计算分配通常是刚性和统一的，这在处理大规模模型和长序列时可能限制其效率和可扩展性。
### Innovation
引入了Subjective Depth Transformers (SDT) 和 Subjective Timescale Transformers (STT) 两种新的架构，利用贝叶斯惊奇信号来动态路由计算，能够自动学习在解码器Only Transformer中何时何处进行计算。SDT通过交替的决策层和动态层实现了计算的动态分配，而STT进一步将这种条件计算扩展到了时间领域，根据预测的残差更新来时间和空间上动态执行或跳过Transformer块。
### Conclusion
这两种架构展示了从新颖性过渡到预测驱动的门控机制，表明与惊喜原则的契合。在减少计算量的同时，它们初步揭示了条件计算中的计算准确性权衡。提出的架构建立了一个灵活的高效框架，通过减少每个计算跳过层中的自注意力计算和KV缓存需求，达到了50%至75%的降低，为更高效的模型开发指明了路径。
## 335. `cs.CL` - BoundingDocs:具有空间注释的统一文档问答数据集 [PDF](https://arxiv.org/pdf/2501.03403), [HTML](https://arxiv.org/abs/2501.03403)
### Authors
Simone Giovannini,Fabio Coppini,Andrea Gemelli,Simone Marinai
### Background
该研究基于现有的文档AI（Document AI）任务和视觉丰富文档理解（VRDU）相关的公开数据集构建了一个统一的问答数据集。它的目的是为了利用大型语言模型进行训练和评估，同时提供文档的OCR信息以及答案在文档图像中的确切位置。
### Innovation
该研究有两个主要贡献。首先，它将现有的文档AI任务，如信息抽取（IE），重新构建成问答任务，使其成为训练和评估大型语言模型的合适资源。其次，该研究发布了所有文档的OCR信息，并包括了答案在文档图像中的确切位置（作为边界框）。此外，还探讨了不同提示技术对开放权重模型性能的影响，以及如何最有效地进行文档理解。
### Conclusion
研究发现，包含边界框信息的不同提示技术对开放权重模型在文档理解上的性能有重要影响，并确定了最有效的提示方法来实现文档理解。
## 336. `cs.CL` - 细粒度且可解释的多模态总结事实性评估 [PDF](https://arxiv.org/pdf/2402.11414), [HTML](https://arxiv.org/abs/2402.11414)
### Authors
Yue Zhang,Jingxuan Zuo,Liqiang Jing
### Background
多模态总结旨在基于输入的文本和图像生成简洁的摘要。然而，现有的方法可能产生不准确的输出。研究表明，当前评估多模态总结模型事实性的方法存在局限性，因此需要开发新的评估框架，以便更精确地评估其事实性。
### Innovation
提出了两种细粒度且可解释的评估框架（FALLACIOUS）来评估多模态总结模型的事实性，包括基于参考的事实性评估框架和无需参考的事实性评估框架。特别是无需参考的事实性评估框架可以应用于更广泛的情景，且无需依赖于预设的真实数据。
### Conclusion
通过分析这两个框架与其他评估指标的相关性，实验结果表明了所提出方法的有效性。研究团队将进一步通过GitHub公开其代码和数据集。这些框架的引入有助于提高多模态总结模型生成的摘要准确性。
## 337. `cs.CL` - Position-Aware Depth Decay Decoding ($D^3$): 提升大规模语言模型推理效率 [PDF](https://arxiv.org/pdf/2503.08524), [HTML](https://arxiv.org/abs/2503.08524)
### Authors
Siqi Fan,Xuezhi Fang,Xingrun Xing,Peng Han,Shuo Shang,Yequan Wang
### Background
由于大规模语言模型（LLMs）具有大量参数，其推理阶段消耗大量资源。与传统的模型压缩方法需要重新训练不同，近期的动态计算方法表明，并非所有组件在推理时都需要，从而有可能实现无需重新训练的处理管道。本文着重探讨了LLM生成的动态深度问题。
### Innovation
提出了一种基于位置感知的层跳过框架，该框架在保持性能的同时，可以通过利用幂律衰减函数确定保留的层数，从而有效节省运算量1.5倍。此外，通过无训练的算法$D^3$首次在广泛的语言生成任务中实现了效率提升，该算法在LLama模型上展示了平均1.5倍的速度提升，性能下降几乎可以忽略（<1%），特别是在GSM8K和BBH基准测试中。
### Conclusion
提出的$D^3$算法在7亿到70亿参数的大规模语言模型上实现了高效的推理速度提升，同时保持了与全推理过程相近的性能，且性能损失几乎可以忽略。
## 338. `cs.CL` - 大型语言模型中的推理感知微调以优化Best-of-N采样 [PDF](https://arxiv.org/pdf/2412.15287), [HTML](https://arxiv.org/abs/2412.15287)
### Authors
Yinlam Chow,Guy Tennenholtz,Izzeddin Gur,Vincent Zhuang,Bo Dai,Sridhar Thiagarajan,Craig Boutilier,Rishabh Agarwal,Aviral Kumar,Aleksandra Faust
### Background
最近的研究表明，在推理时有效利用计算资源是提高大型语言模型（LLMs）性能的关键。本文的研究是在这一背景下进行的，旨在通过一种新的推理感知微调方法来直接优化推理时的性能策略。
### Innovation
本文提出了第一种针对Best-of-N（BoN）策略的模仿学习和强化学习方法，克服了BoN中难以处理的非可微分的argmax操作。通过这种新的微调方法，模型能够在测试时既选择最优秀的响应又兼顾多样化的响应，类似于强化学习中的探索与利用平衡。
### Conclusion
实验结果表明，这种方法能有效提高BoN策略的性能和推理时间上的计算效率。具体而言，我们的方法在Hendrycks MATH数据集上将Gemma 2B的Bo32性能从26.8%提升到30.8%，pass@32从60.0%提升到67.0%，在HumanEval数据集上的pass@16从61.6%提升到67.1%。
## 339. `cs.CL` - 基于心理学的统一动态课程学习框架 [PDF](https://arxiv.org/pdf/2408.05326), [HTML](https://arxiv.org/abs/2408.05326)
### Authors
Guangyu Meng,Qingkai Zeng,John P. Lalor,Hong Yu
### Background
直接从难度不同的示例中学习对于人类和机器学习模型都是具有挑战性的。有效的策略是按照从简单到难的顺序逐步向学习者展示示例。此前提出的课程学习（Curriculum Learning，CL）方法旨在通过这种方式改善模型训练效果。然而，CL框架设计中仍存在的关键挑战包括量化训练数据的难度以及确定每次训练步骤中输入的数据量。
### Innovation
本文提出了基于心理学的统一动态课程学习框架（PUDF），并使用项目反应理论（Item Response Theory，IRT）应用于人工众包（AC）的响应，来量化训练数据的难度并提供全球、可解释的难度值。借助IRT，提出了一种基于模型能力估计进行动态数据选择的策略（Dynamic Data Selection via Model Ability Estimation，DDS-MAE），以控制模型训练过程中数据的选择。由于难度标记和模型能力估计基于一致的IRT理论，因此它们的值在相同范围内是可比较的，这可能有助于实现一致的数据选择策略，并且可能比现有方法得到更快的收敛速度。
### Conclusion
使用PUDF微调预训练的大语言模型在一系列基准数据集上实现了更高的准确性和更快的收敛速度，相比标准微调方法和最新的课程学习方法。消融研究和下游分析进一步验证了PUDF对课程学习的有效影响。
## 340. `cs.CL` - 现代日语中的依赖距离和层次距离的分布及其影响因素 [PDF](https://arxiv.org/pdf/2504.21421), [HTML](https://arxiv.org/abs/2504.21421)
### Authors
Linxuan Wang,Shuiyuan Yu
### Background
研究了日语中依赖距离（DD）和层次距离（HD）之间的关系，通过比较DD和HD的概率分布（固定和未固定句长的情况），以及随着句长增加MDD与MHD的变化及其相关系数来探索这种关系。
### Innovation
发现了语素的价在决定MDD与MHD之间的折中关系中起着基础作用，日语母语使用者通过调节语素的价来管理线性复杂性和层次复杂性，且MDD与MHD的相对大小依赖于语素价的阈值是否被突破。此外，还发现了语素的价对HD分布的影响比对DD分布的影响更大，导致两者概率分布不同，使得MDD的平均值低于MHD。
### Conclusion
语素的价不仅是句长变化时MDD和MHD模式变化背后的关键因素，也影响着DD和HD的概率分布。在相同的句长下，MHD的概率更高，而MDD的概率较低，这反映了母语使用者为了控制句子整体复杂度而对认知负载进行优化的做法。
## 341. `cs.CL` - 在实际情况中的改进的视觉提示关键词定位 [PDF](https://arxiv.org/pdf/2409.06013), [HTML](https://arxiv.org/abs/2409.06013)
### Authors
Leanne Nortje,Dan Oneata,Gabriel Pirlogeanu,Herman Kamper
### Background
视觉提示关键词定位（VPKL）旨在根据给定图像查询，在语音集合中找到图像中描述的词汇出现的位置。这在语音字幕不可用或低资源语言（如未书写的语言）时非常有用。以前的研究表明，可以通过训练包含成对图像的视觉语音模型来实现VPKL，该模型使用未标记的语音。然而，所有实验均使用英语进行，并且使用转录来获得正负样本对。
### Innovation
本文提出了一种少样本学习方案，能够在没有转录的情况下自动挖掘样本对，从而在英语上只有一些小幅性能下降。此外，这是首次在实际的低资源语言（约鲁巴语）上进行VPKL研究，结果显示在约鲁巴语上，由于挖掘不准确，性能下降更多。
### Conclusion
尽管在约鲁巴语上VPKL的精度有所下降，但该方案在英语上表现良好，且首次展示了该方法在真正的低资源语言环境中的应用效果。
## 342. `cs.CL` - Gram2Vec：可解释的文档向量化工具 [PDF](https://arxiv.org/pdf/2406.12131), [HTML](https://arxiv.org/abs/2406.12131)
### Authors
Peter Zeng,Hannah Stortz,Eric Sclafani,Alina Shabaeva,Maria Elizabeth Garza,Daniel Greeson,Owen Rambow
### Background
该论文的背景在于当前基于语法特征的文档表示方法。虽然神经网络方法在表示学习方面取得了显著进展，但它们往往缺乏内在解释性，使得难以追踪特征如何影响模型的决策。Gram2Vec旨在通过提取文本中存在的语法特征的标准化相对频率来嵌入文档，从而提供基于特征向量生成方式的内在可解释性。
### Innovation
Gram2Vec的主要创新在于它采用了一种基于语法特征的方法来嵌入文档，这种方式比神经网络方法更具可解释性。相较于神经网络方法，Gram2Vec能够清晰地展示出每个特征如何生成特征向量，从而使得模型的决策可以被更好地理解。该方法还被应用于作者身份验证和AI检测两个场景中，展示了Gram2Vec的实用性和有效性。
### Conclusion
通过将作者身份验证和AI检测作为应用案例，作者证明了Gram2Vec的有效性和实用性。相较于使用Biber特征训练的机器学习模型，Gram2Vec特征显著提高了AI检测的性能。此外，Gram2Vec提供了更高的可解释性，使得用户可以更好地理解模型的决策过程。
## 343. `cs.CL` - Web-Shepherd: 推动强化网络代理的PRMs [PDF](https://arxiv.org/pdf/2505.15277), [HTML](https://arxiv.org/abs/2505.15277)
### Authors
Hyungjoo Chae,Sunghwan Kim,Junhee Cho,Seungone Kim,Seungjun Moon,Gyeom Hwangbo,Dongha Lim,Minjin Kim,Yeonjun Hwang,Minju Gwak,Dongwook Choi,Minseok Kang,Gwanhoon Im,ByeongUng Cho,Hyojun Kim,Jun Hee Han,Taeyoon Kwon,Minju Kim,Beong-woo Kwak,Dongjin Kang,Jinyoung Yeo
### Background
网络导航是一个独特的领域，可以自动执行许多重复的生活任务，但同时也是一个挑战，因为它需要比典型的大语言模型（MLLM）任务更远期的序列决策。尽管之前的工作使用了大语言模型作为奖励模型，但这些模型在实际部署中存在速度和成本的限制。至今，还没有专门为网络导航创建的可利用于训练和测试的奖励模型。
### Innovation
该论文提出了第一个过程奖励模型（PRM）Web-Shepherd，能够在步骤级上评估网络导航轨迹。为此，构建了一个大规模的数据集称为WebPRM Collection，包含40,000个步骤级偏好对和注释清单，跨越不同的领域和难度级别。同时引入了WebRewardBench，这是一个用于评估PRMs的元评估基准。实验结果显示，Web-Shepherd在WebRewardBench上的准确度比使用GPT-4o高出约30分，使用GPT-4o-mini作为策略时，用Web-Shepherd作为验证者相比使用GPT-4o-mini作为验证者，性能提高了10.9分，而成本降低了10。
### Conclusion
论文展示了Web-Shepherd在评估网络导航轨迹方面的优越性能，并提供了可供参考的数据集和代码，增强了在网络导航领域使用专业化奖励模型的可行性。
## 344. `cs.CL` - 极低资源和濒危语言的推理转移：通过高效的语言理解桥接语言 [PDF](https://arxiv.org/pdf/2504.02890), [HTML](https://arxiv.org/abs/2504.02890)
### Authors
Khanh-Tung Tran,Barry O'Sullivan,Hoang D. Nguyen
### Background
近年来，大型语言模型（LLMs）能够通过生成链式推理（CoT）来进行推理任务，但这些改进主要针对高资源语言，而低资源语言则被忽视。本文探讨了通过先前的提示、模型编辑和微调等方法，在极端低资源情况下CoT技术的应用。引入了基于英语轴的心智链式训练方法，利用LLM在潜在空间中内部操作与主导语言对齐的洞察，通过在输入低资源语言的情况下，进行监督性微调生成英语的心智链式解释，最后输出在目标语言中的最终响应。
### Innovation
提出了一种基于英语轴的心智链式训练方法，该方法适用于低资源语言场景，特别是在数学推理基准测试中，该方法在低资源场景中比其他基线高出多达28.33%。此外，还进行了混合语言的心智链式训练和两阶段训练，表明明确区分语言理解与推理能力可以增强跨语言推理能力。通过创建LC2024基准，首次将数学任务与爱尔兰语（一种极低资源和濒危语言）结合，为未来工作提供了资源和方法。
### Conclusion
该研究和资源展示了在极低资源语言场景中实现多语言推理的一种实用路径，即使在数据稀缺的情况下，也不需要对每个极低资源语言进行大量的重新训练。
## 345. `cs.CL` - 知识图谱检索中的结构-内容权衡 [PDF](https://arxiv.org/pdf/2506.13380), [HTML](https://arxiv.org/abs/2506.13380)
### Authors
Valentin Six,Evan Dufraisse,Gaël de Chalendar
### Background
大型语言模型（LLMs）越来越多地依赖知识图谱来进行事实推理，但检索设计如何影响其性能尚不清楚。本文研究了问题分解如何改变检索子图的内容和结构，并展示了基于子问题的检索提高了内容精度但产生了独立的子图，而基于问题的检索保持了结构但降低了相关性。最优性能出现在这两个极端之间，表明平衡检索内容和结构对于高效地在结构化知识上进行LLM推理至关重要。
### Innovation
使用混合检索函数控制初始问题和子问题的重要性，展示了基于子问题的检索提高了内容精度，但导致子图分离；基于问题的检索保持了结构但相关性降低。研究揭示了平衡检索内容和结构的重要性。
### Conclusion
大型语言模型在利用结构化知识时，需要权衡检索内容的精确性和检索结果的结构完整性，以找到性能最优的平衡点。
## 346. `cs.CL` - 通过无注释数据增强和反课程蒸馏增强大型语言模型以检测心理操纵 [PDF](https://arxiv.org/pdf/2505.15255), [HTML](https://arxiv.org/abs/2505.15255)
### Authors
Yuansheng Gao,Han Bao,Tong Zhang,Bin Li,Jixiang Luo,Ronghao Chen,Zonghui Wang,Wenzhi Chen
### Background
心理操纵是一种微妙而普遍的精神虐待形式，对心理健康构成严重威胁。然而，检测心理操纵仍然是一个未被充分研究的研究问题。当前领域面临三大挑战：一是数据不足且难以获取；二是心理操纵的隐蔽性导致难以检测；三是缺乏现实世界数据集。
### Innovation
本研究提出了一种名为MentalMAC的新框架，旨在增强大型语言模型检测多轮对话中心理操纵元素的能力。MentalMAC框架包含三种关键组件：EvoSA（基于进化操作和言语行为理论的无注释数据增强方法）；教师模型生成的多任务监督；以及阶段性任务级别反课程蒸馏。
### Conclusion
通过构建包含5000个真实对话样本的ReaMent数据集，并利用MentalMAC蒸馏模型辅助人类标注，实验表明MentalMAC在F1mac和准确性上分别比最佳基线高出25.9%和8.1%，并优于商业LLM如GPT-4和Claude-3.5-Sonnet。
## 347. `cs.CL` - 高效大型语言模型的扩展 [PDF](https://arxiv.org/pdf/2402.14746), [HTML](https://arxiv.org/abs/2402.14746)
### Authors
B.N. Kausik
### Background
近年来，大规模语言模型（LLMs）包含了数百亿个参数，并消耗了大量的资源。按照“AI扩展律”的理论，对于变换器而言，参数的数量需要线性地与数据的规模成比例增加。因此，我们需要探索高效的大规模语言模型，即在保持期望准确性的前提下参数最少的语言模型。研究通过理论和实证估计Kullback-Leibler距离，推导出一种自然的AI扩展律，即高效的大规模语言模型中的参数数量与训练数据规模成$D^{boldsymbol{boldsymbol{boldsymbol{boldsymbol{boldsymbol{beta}}}}}}$幂次关系，其中$0.44 boldsymbol{boldsymbol{boldsymbol{boldsymbol{boldsymbol{textless}}}}}$ $boldsymbol{boldsymbol{boldsymbol{boldsymbol{boldsymbol{beta}}}}}$ $boldsymbol{boldsymbol{boldsymbol{boldsymbol{boldsymbol{textless}}}}}$ $0.72$，这表明存在更高效的架构。
### Innovation
本文提出了递归变换器（Recurrent Transformers），结合了变换器的有效性和递归网络的高效率。递归变换器通过固定宽度的滑动窗口逐步应用单个变换器层，实现了（a）序列长度线性时间的运行，（b）内存效率良好且适合大量批量的并行处理，（c）对于语言任务可以学习遗忘历史，对于长距离任务（如复制和选择性复制）可以积累记忆，（d）可以通过逐步训练克服消失梯度的问题。实验结果显示，递归变换器在基准测试中表现出色。
### Conclusion
通过递归变换器的提出，本文提供了一种新的高效大规模语言模型架构，其在保持语言生成质量和效率方面具有优势。
## 348. `cs.CL` - Co-NAML-LSTUR：结合注意力多视图学习和长短期用户表示的新闻推荐联合模型 [PDF](https://arxiv.org/pdf/2507.20210), [HTML](https://arxiv.org/abs/2507.20210)
### Authors
Minh Hoang Nguyen,Thuat Thien Nguyen,Minh Nhat Ta,Tung Le,Huy Tien Nguyen
### Background
新闻推荐系统在减轻信息过载方面发挥着关键作用，通过提供个性化内容。一个关键挑战在于能够同时建模新闻文章的多视图表示并捕捉用户兴趣的动态双尺度特性，即既包括短期偏好也包括长期偏好。此前的方法往往依赖单一视图特征，或者未能充分建模跨时间的行为。
### Innovation
提出了一种名为Co-NAML-LSTUR的混合新闻推荐框架，该框架通过集成NAML进行注意力多视图新闻编码，并结合LSTUR进行层次用户建模，特别适用于受限数据资源的训练。该模型利用BERT嵌入以提高语义表示效果。在MIND-small和MIND-large两个广泛使用的基准上评估了Co-NAML-LSTUR，结果显示该模型显著优于多个强基线模型，AUC提高了1.55%，MRR提高了1.15%，与NAML相比，AUC提高了2.45%，MRR提高了1.71%。
### Conclusion
本研究强调了我们高效混合模型的有效性，该模型结合了多视图新闻建模与双尺度用户表示，特别适用于资源受限的环境，而非宣称是绝对的当前最先进的模型。该模型的实现已公开发布。
## 349. `cs.CL` - 关于预训练语言模型在通用文本嵌入中的作用：综述 [PDF](https://arxiv.org/pdf/2507.20783), [HTML](https://arxiv.org/abs/2507.20783)
### Authors
Meishan Zhang,Xin Zhang,Xinping Zhao,Shouzheng Huang,Baotian Hu,Min Zhang
### Background
文本嵌入因其在各种自然语言处理（NLP）任务中的有效性，吸引了广泛的关注，包括检索、分类、聚类、双语信息挖掘和总结。预训练语言模型（PLMs）的出现使得通用文本嵌入（GPTE）能够产生丰富的、可迁移的表示，从而在这一领域展现出广泛应用。典型的GPTE架构利用PLMs生成密集的文本表示，并通过大规模成对数据集上的对比学习进行优化。
### Innovation
该论文聚焦于PLMs在GPTE中的作用，并提供了对其发展驱动因素的全面概述。它详细介绍了PLMs在基础架构中的基本功能，包括嵌入提取、表达性增强、训练策略、学习目标和数据构建。此外，还描述了PLMs使能的高级功能，涵盖了多语言支持、多模态整合、代码理解及场景特定适应能力。最后，指出了超越传统改进目标的未来研究方向，包括排名整合、安全性考量、偏差缓解、结构信息整合及嵌入的认知扩展。
### Conclusion
本综述旨在为寻求了解当前及未来GPTE状态和发展潜力的新手和资深研究人员提供有价值的参考。
## 350. `cs.CL` - 大型语言模型推理引擎研究：优化与效率视角 [PDF](https://arxiv.org/pdf/2505.01658), [HTML](https://arxiv.org/abs/2505.01658)
### Authors
Sihyeong Park,Sungryeol Jeon,Chaelyn Lee,Seokhun Jeon,Byung-Soo Kim,Jemin Lee
### Background
大型语言模型（LLMs）被广泛应用于聊天机器人、代码生成器和搜索引擎中。这种模型的工作负载如链式推理、复杂推理和代理服务会显著增加推理成本，从而需要通过调用模型多次来实现。已经有一些优化方法，如并行性、压缩和缓存被采用来降低成本，但由于服务需求的多样性，选择合适的优化方法仍然具有挑战性。最近，专门为服务导向基础设施设计的LLM推理引擎已经浮现，但它们的应用还需要系统性的研究。因此，本文对25个开源和商业推理引擎进行了全面评估。
### Innovation
本文提供了25个开源和商业推理引擎的全面评估，从易用性、部署便利性、通用支持、可扩展性和吞吐量和延迟感知计算适用性方面进行评价。深入研究了每个推理引擎的设计目标和它支持的优化技术，并评估开源推理引擎的生态系统成熟度和商业推理引擎的性能与成本策略。为支持复杂LLM服务、支持多种硬件和增强安全性指出了未来的研究方向，提供了研究和开发优化的LLM推理引擎的实际指导。
### Conclusion
在本文的基础上，确定了将此类信息集成到服务导向基础设施中的未来发展路线图，提供了不断跟踪该快速发展的领域的公共仓库：<href>这个链接</href>。
## 351. `cs.CL` - 使用概念学习数据集发现大型语言模型中的隐性偏见 [PDF](https://arxiv.org/pdf/2510.01219), [HTML](https://arxiv.org/abs/2510.01219)
### Authors
Leroy Z. Wang
### Background
该研究通过对概念学习任务数据集的引入，旨在揭示大型语言模型中存在的隐性偏见。通过在上下文中进行概念学习实验，研究发现，当语言模型通过直接提示而不是概念学习组件进行测试时，对单调递增量词的偏好并不明显。这一发现表明，上下文中的概念学习可以有效地揭示语言模型中的隐藏偏见。
### Innovation
研究引入了概念学习任务数据集，通过在上下文中进行概念学习实验，揭示了语言模型对单调递增量词的偏好是一种隐性偏见。这种方法展示了发现大型语言模型中隐性偏见的有效性。
### Conclusion
该研究通过上下文中的概念学习有效发现并验证了大型语言模型中的隐性偏见，即对单调递增量词的偏好。这种方法揭示了通过非直接提示的方式才能更好地理解和评估语言模型的公平性和客观性。
## 352. `cs.CL` - AdvancedIF: 基于评语基准评估和强化学习以提升LLM指令遵循能力 [PDF](https://arxiv.org/pdf/2511.10507), [HTML](https://arxiv.org/abs/2511.10507)
### Authors
Yun He,Wenzhe Li,Hejia Zhang,Songlin Li,Karishma Mandyam,Sopan Khosla,Yuanhao Xiong,Nanshu Wang,Xiaoliang Peng,Beibin Li,Shengjie Bi,Shishir G. Patil,Qi Qi,Shengyu Feng,Julian Katz-Samuels,Richard Yuanzhe Pang,Sujan Gonugondla,Hunter Lang,Yue Yu,Yundi Qian,Maryam Fazel-Zarandi,Licheng Yu,Amine Benhalloum,Hany Awadalla,Manaal Faruqui
### Background
近年来，大型语言模型（LLMs）在多种任务上的表现令人印象深刻，但复杂的、多步骤的以及系统提示的指令遵循仍然是一个重大挑战。严格的评估和有效的训练受到高质量、高可信度的人类注释基准和可靠、可解释的奖励信号的缺乏的阻碍。
### Innovation
提出了一种名为AdvancedIF的全面基准评估，包含超过1600个提示和专家评估的标准，以评估LLMs遵循复杂、多步骤和系统指令的能力。此外，还提出了一种名为RIFL的新型后训练管道，该管道利用评语生成、调优后的评语验证器和奖励塑形来实现有效的指令遵循的强化学习。
### Conclusion
广泛的实验表明，RIFL显著提高了LLMs的指令遵循能力，相较于AdvancedIF获得了6.7%的绝对提升，并在公共基准上取得了良好的结果。消融研究证实了RIFL中每个组件的有效性。该工作将评语确立为训练和评估LLMs高级指令遵循能力的强大工具，为更强大、更可靠的AI系统奠定了基础。
## 353. `cs.CL` - Prompt-R1：通过端到端强化学习实现的协作自动提示框架 [PDF](https://arxiv.org/pdf/2511.01016), [HTML](https://arxiv.org/abs/2511.01016)
### Authors
Wenjin Liu,Haoran Luo,Xueyuan Lin,Haoming Liu,Tiesunlong Shen,Jiapu Wang,Rui Mao,Erik Cambria
### Background
近年来，先进大规模语言模型（LLMs）的出现速度不断加快。然而，当面对复杂问题时，大多数用户往往无法提供准确有效的提示与LLMs互动，从而限制了LLMs的性能。
### Innovation
提出了一种名为Prompt-R1的端到端强化学习框架，该框架使用小型LLM与大型LLM协作，代替用户互动解决复杂问题。该框架通过多轮提示交互形式实现协作，设计了双重约束奖励优化正确性、生成质量和推理准确性。Prompt-R1提供一种即插即用框架，支持与不同大型LLMs进行推理和训练。
### Conclusion
在多个公开数据集上的实验表明，Prompt-R1在各种任务中显著优于基线模型。我们的代码已在该链接公开提供：this https URL。
## 354. `cs.CL` - UITron-Speech: 基于语音指令的自动化GUI代理研究 [PDF](https://arxiv.org/pdf/2506.11127), [HTML](https://arxiv.org/abs/2506.11127)
### Authors
Wenkang Han,Zhixiong Zeng,Jing Huang,Shu Jiang,Liming Zheng,Longrong Yang,Haibo Qiu,Chang Yao,Jingyuan Chen,Lin Ma
### Background
自主代理（AG）正在改变人机交互的方式，但它们对基于文本的指令依赖限制了无障碍性和便利性，特别是在免手持场景中。为此，本文提出了使用语音指令代替文本指令的创新方法，并开发了 UITron-Speech，这是第一个能够直接处理语音指令和设备截图来预测用户行为的端到端GUI代理。
### Innovation
1. 使用合成了高质量的语音指令数据集，解决了数据稀缺性。2. 设计了混合模态训练策略，缓解了预训练基础模型中的模态不平衡。3. 提出了一种无需训练的两步定位校正方法，以缓解细微的定位偏差。
### Conclusion
大量实验表明，UITron-Speech 在多个基准上实现了健壮的性能和更高的适应性，证实了基于语音指令的GUI代理的可行性及其未来在更轻松、更智能的人机交互中的潜力。我们的代码和数据集可以在 这里 获取。
## 355. `cs.CL` - CLaRa：基于连续潜在推理的检索与生成融合 [PDF](https://arxiv.org/pdf/2511.18659), [HTML](https://arxiv.org/abs/2511.18659)
### Authors
Jie He,Richard He Bai,Sinead Williamson,Jeff Z. Pan,Navdeep Jaitly,Yizhe Zhang
### Background
检索增强生成（RAG）能够通过引入外部知识来增强大型语言模型（LLMs），但它仍然面临着长上下文和检索-生成优化脱节的问题。
### Innovation
CLaRa 提出了一种统一框架，该框架在共享的连续空间中执行基于嵌入的压缩和联合优化。CLaRa 引入了 SCP（保留密钥的数据合成框架），这是一种使用问答和改写监督的保留密钥的数据合成方法，用于生成语义丰富且可检索的压缩向量。CLaRa 通过单一语言建模损失来端到端训练检索器和生成器，并通过可微分的 top-k 估计器使梯度流经两个模块。
### Conclusion
CLaRa 在多个 QA 基准测试中展示了最先进的压缩和排序性能，经常优于基于文本的微调基线。联合优化理论上将检索的相关性与答案质量对齐。
## 356. `cs.CL` - Mem-PAL: 朝向基于记忆的个性化对话助手以适应长时用户-代理交互 [PDF](https://arxiv.org/pdf/2511.13410), [HTML](https://arxiv.org/abs/2511.13410)
### Authors
Zhaopei Huang,Qifeng Dai,Guozheng Wu,Xiaopeng Wu,Kehan Chen,Chuan Yu,Xubin Li,Tiezheng Ge,Wenxuan Wang,Qin Jin
### Background
随着智能个人设备的兴起，服务导向的人机交互变得越来越普遍。这种趋势凸显了需要能够理解用户特定特质的个性化对话助手，以准确理解需求并根据个人喜好定制响应。然而，现有的方法往往忽视了长期交互的复杂性，未能捕捉用户主观特性。为解决这些差距，我们提出了PAL-Bench，一种旨在评估面向服务的助手在长期用户-助手交互中的个性化能力的新基准。在缺乏可用真实数据的情况下，我们开发了一个多步骤的基于LLM的合成管道，并通过人工注释者进行验证和细化，从而获得PAL-Set，首个包含多会话用户日志和对话历史的中文数据集，作为PAL-Bench的基础。
### Innovation
针对现有的方法往往忽视长期交互复杂性和用户主观特性的问题，我们开发了一个基于记忆的个性化对话助手PAL-Bench，以适应长期用户-代理交互。我们还提出了H$^2$Memory，一种层级异质记忆框架，通过检索增强生成来提高个性化响应的生成能力。实验证明，这种记忆框架的有效性。
### Conclusion
通过PAL-Bench和H$^2$Memory框架的应用，我们的研究成功地提高了解决策助在长期交互中的个性化能力，为提升用户体验提供了新方法。
## 357. `cs.CL` - AICC：使用基于模型的HTML解析器构建更精细的7.3万亿词汇量AI就绪语料库 [PDF](https://arxiv.org/pdf/2511.16397), [HTML](https://arxiv.org/abs/2511.16397)
### Authors
Ren Ma,Jiantao Qiu,Chao Xu,Pei Chu,Kaiwen Liu,Pengli Ren,Yuan Qu,Jiahui Peng,Linfeng Hou,Mengjie Liu,Lindong Lu,Wenchang Ning,Jia Yu,Rui Min,Jin Shi,Haojiong Chen,Peng Zhang,Wenjian Zhang,Qian Jiang,Zengjie Hu,Guoqiang Yang,Zhenxiang Li,Fukai Shang,Runyuan Ma,Chenlin Su,Zhongying Tu,Wentao Zhang,Dahua Lin,Conghui He
### Background
当前网络数据质量对于大型语言模型至关重要，但大多数数据管理努力主要集中在过滤和去重上，HTML-to-text提取被视为固定的预处理步骤。现有的网络语料库依赖于Trafilatura等基于启发式的提取器，这些提取器难以保持文档结构，经常破坏结构化元素如公式、代码和表格。本文假设优化提取质量可以与激进的过滤策略一样影响下游性能。
### Innovation
引入了基于序列标注问题解决的新型提取管道——MinerU-HTML。不同于基于文本密度启发式的技术，MinerU-HTML利用语义理解并采用两阶段格式化管道，在转换为Markdown前明确分类语义元素。MinerU-HTML基于模型的方法具有内在可扩展性，而启发式方法的改进空间有限。在对7887个已标注网页的基准测试MainWebBench上，MinerU-HTML展现出81.8%的ROUGE-N F1得分，显著高于Trafilatura的63.6%。使用MinerU-HTML构建的AICC（AI-ready Common Crawl）是一个来自两个Common Crawl快照的7.3万亿词汇量多语言语料库。在控制预训练实验中，AICC显著优于Trafilatura提取的TfCC。
### Conclusion
基于模型的HTML解析显著提升了Web语料库的构建质量，展示了提取质量对语言模型能力的重大影响，AICC在关键基准上超越了RefinedWeb和FineWeb，证明了HTML提取的重要性及其对构建高质量语料库的关键作用。
## 358. `cs.CL` - 具有RAG启用动态提示的大规模语言模型系统分析在医疗错误检测和纠正中的应用 [PDF](https://arxiv.org/pdf/2511.19858), [HTML](https://arxiv.org/abs/2511.19858)
### Authors
Farzad Ahmed,Joniel Augustine Jerome,Meliha Yetisgen,Özlem Uzuner
### Background
临床记录中包含事实、诊断和管理错误，这些错误可能会危及病人安全。大规模语言模型（LLMs）可能有助于检测和纠正这些错误，但它们在不同提示策略下的行为尚不清楚。本文通过评估零样本提示、带有随机示例的静态提示（SPR）和检索增强动态提示（RDP）对三项医疗错误处理子任务（错误标记检测、错误句子检测和错误纠正）的表现进行研究。
### Innovation
研究采用MEDEC数据集，评估了九种指令调优的LLMs（包括GPT、Claude、Gemini和OpenAI o系列模型）。结果表明，检索增强动态提示（RDP）在错误检测准确性上优于零样本提示和静态提示，且减少了假阳性，增强了医疗错误纠正的可靠性。
### Conclusion
各类不同模型下，RDP在自我检测、错误标注检测和错误纠正方面均优于零样本提示和静态提示。使用检索到的示例改善了检测准确性，降低了假阳性，并增强了医疗错误纠正的可靠性。
## 359. `cs.CL` - 昨日的新闻：评估 misinformation 检测模型多维 out-of-distribution 通用性的基准 [PDF](https://arxiv.org/pdf/2410.18122), [HTML](https://arxiv.org/abs/2410.18122)
### Authors
Ivo Verhoeven,Pushkar Mishra,Ekaterina Shutova
### Background
错误信息随着时间迅速变化，远快于管理员能够大规模注释的速度，导致训练数据分布与推理数据分布发生变化。现有的错误信息检测模型无法进行 out-of-distribution 通用化，因此需要一个新的基准数据集来评估模型的这一能力。
### Innovation
提出了一个新的基准数据集 misinfo-general，利用离线标注法模拟错误信息内容的协变量变化。识别了时间、事件、话题、出版者、政治偏见、错误信息类型作为通用的关键维度，并评测了常见的基线模型。
### Conclusion
通过文章元数据展示了现有模型在某些维度上失败的情况，这些从分类指标上不容易发现。同时确保数据集具有有限的建模捷径，并公开了数据集和代码供进一步研究使用。
## 360. `cs.CL` - MTA: 一种用于个性化大型语言模型的合并-适应框架 [PDF](https://arxiv.org/pdf/2511.20072), [HTML](https://arxiv.org/abs/2511.20072)
### Authors
Xiaopeng Li,Yuanjin Zheng,Wanyu Wang,wenlin zhang,Pengyue Jia,Yiqi Wang,Maolin Wang,Xuetao Wei,Xiangyu Zhao
### Background
个性化大型语言模型（PLLMs）旨在使模型输出与个体用户偏好相匹配，这对用户中心型应用至关重要。然而，针对每个用户进行微调的标准方法面临两个主要局限：(1) 存储成本随用户数量线性增长，使方法难以扩展；(2) 从头开始微调静态模型通常会导致数据稀疏用户的表现不佳。
### Innovation
提出了MTA（合并-适应框架）用于PLLMs。MTA包括三个关键阶段：(1) 构建共享的Meta-LoRA银行，通过选择锚点用户并预训练元个性化特性；(2) 引入自适应LoRA融合阶段，确保可扩展性和支持动态个性化组合，而无需专用存储；(3) 提出基于LoRA堆叠的少样本个性化阶段，应用于合并后的LoRA顶部的一个超低秩、轻量级LoRA模块进行微调，以实现少样本条件下的有效个性化。
### Conclusion
广泛实验结果表明，我们的方法在LaMP基准测试中在多个任务上优于当前最先进的方法。
## 361. `cs.CL` - BengaliFig：博孟加拉低资源挑战 [PDF](https://arxiv.org/pdf/2511.20399), [HTML](https://arxiv.org/abs/2511.20399)
### Authors
Abdullah Al Sefat
### Background
大型语言模型在多种语言基准测试中表现出色，但在具象和文化地缘推理方面仍需广泛评估，尤其是在低资源语言环境中。孟加拉语作为广泛使用但资源有限的语言，其在该方面缺乏专门的数据集和挑战集。
### Innovation
提出了一个名为BengaliFig的简明但内容丰富的挑战集，特别适用于孟加拉语。该数据集包含了435个源自孟加拉语口头和文学传统的谜语，并在五个不同的维度上进行了标注，即推理类型、陷阱类型、文化深度、答案分类和难度。同时，通过一个基于约束的AI辅助管道，自动将谜语转换为多个选择题格式。该数据集被用于评估八种前沿语言模型在零样本和少量样本链式推理提示下的表现，揭示了这些模型在具象和文化特异性推理方面的弱点。
### Conclusion
BengaliFig不仅能作为评估大型语言模型在低资源文化背景下的稳健性的诊断工具，而且是通向包容性和文化遗产意识的自然语言处理评估的重要一步。
## 362. `cs.CL` - DR Tulu：随着评估标准演化的强化学习在深度研究中的应用 [PDF](https://arxiv.org/pdf/2511.19399), [HTML](https://arxiv.org/abs/2511.19399)
### Authors
Rulin Shao,Akari Asai,Shannon Zejiang Shen,Hamish Ivison,Varsha Kishore,Jingming Zhuo,Xinran Zhao,Molly Park,Samuel G. Finlayson,David Sontag,Tyler Murray,Sewon Min,Pradeep Dasigi,Luca Soldaini,Faeze Brahman,Wen-tau Yih,Tongshuang Wu,Luke Zettlemoyer,Yoon Kim,Hannaneh Hajishirzi,Pang Wei Koh
### Background
目前的深度研究模型通过可验证的 Rewards（奖励）强化学习（RLVR）处理短格式问答任务，但这种方法不适合处理复杂的、实际的长格式任务。DR Tulu-8B 是首个直接训练用于开放式、长格式深度研究的开源模型。
### Innovation
提出了一种名为 Reinforcement Learning with Evolving Rubrics（RLER）的新方法，其中评估标准（rubrics）在训练过程中与策略模型共同进化，以提供更具区分性的、在线策略反馈，并在此基础上构建了DR Tulu-8B。
### Conclusion
DR Tulu-8B 在四个科学、医疗和通用领域的长格式深度研究基准测试中表现优异，超过了现有的开源深度研究模型，并与专有的深度研究系统相当或超越，同时价格更低、查询成本更低。释放了所有数据、模型和代码，包括一种基于 MCP 的新代理基础设施，以支持深度研究系统的未来研究。
## 363. `cs.CL` - CAMERA: 通过微专家冗余分析对MoE模型进行多矩阵联合压缩 [PDF](https://arxiv.org/pdf/2508.02322), [HTML](https://arxiv.org/abs/2508.02322)
### Authors
Yuzhuang Xu,Xu Han,Yuanchi Zhang,Yixuan Wang,Yijun Liu,Shiyu Ji,Qingfu Zhu,Wanxiang Che
### Background
大型语言模型（LLMs）具有混合专家（MoE）架构，能在多种任务中实现随参数增加的强劲性能扩展，但同时也带来了显著的计算和存储开销。尽管通过专家级别的剪枝、合并或分解尝试减少参数，但这些方法仍然存在性能和计算效率上的挑战。
### Innovation
引入了微专家作为细粒度压缩单元，创新地将MoE层视为微专家混合，并提出了CAMERA（一种轻量级且无需训练的框架）来识别微专家冗余。进一步提出了CAMERA-P（结构化微专家剪枝框架）和CAMERA-Q（微专家混合精度量化方案）。实验结果显示，CAMERA-P在多种任务中表现出色，CAMERA-Q在2位精度量化下表现优异，并且方法能够在单块NVIDIA A100-40GB GPU上于不到5分钟内完成Qwen2-57B-A14B的微专家全面分析。
### Conclusion
该方法在多种任务中得到了验证，能够有效降低MoE模型的冗余，提高性能和计算效率，并且在小批量量化中的表现优于现有方法。
## 364. `cs.CL` - LightMem：轻量高效的记忆增强生成 [PDF](https://arxiv.org/pdf/2510.18866), [HTML](https://arxiv.org/abs/2510.18866)
### Authors
Jizhan Fang,Xinle Deng,Haoming Xu,Ziyan Jiang,Yuqi Tang,Ziwen Xu,Shumin Deng,Yunzhi Yao,Mengru Wang,Shuofei Qiao,Huajun Chen,Ningyu Zhang
### Background
尽管大规模语言模型（LLMs）具有出色的性能，但在动态和复杂环境中，它们难以有效利用历史交互信息。现有的记忆系统通过引入持续的信息存储、检索和利用机制，使LLMs能够超越无状态交互，但这些系统往往伴随着较大的时间与计算开销。
### Innovation
文章提出了一种新的记忆系统LightMem，它在性能和效率之间找到了平衡。LightMem借鉴了Atkinson-Shiffrin的人类记忆模型，将记忆划分为三个互补的阶段。首先通过轻量级压缩迅速筛选无关信息，并根据主题进行分组；其次，基于主题的短时记忆将这些分组进行整合和总结，便于结构化访问；最后，带有睡眠间更新的长期记忆采用离线程序，将整合过程与在线推理脱钩。实验结果表明，LightMem在LongMemEval和LoCoMo上使用GPT和Qwen架构时，优于强基线，QA准确率分别提高7.7%和29.3%，总token使用量减少分别高达38倍和20.9倍，API调用减少分别高达30倍和55.5倍，纯在线测试时的成本也更低，token使用量减少分别高达106倍和117倍，API调用减少分别高达159倍和310倍。
### Conclusion
LightMem能够在保持高效性能的同时，大大减少计算和通信开销，适用于需要处理复杂交互信息的应用场景。
## 365. `cs.CL` - 通过基于转写词干标记的微调探索跨语言知识转移，以提高关系低资源钦查马语言 [PDF](https://arxiv.org/pdf/2510.09032), [HTML](https://arxiv.org/abs/2510.09032)
### Authors
Adity Khisa,Nusrat Jahan Lia,Tasnim Mahfuz Nafis,Zarif Masud,Tanzir Pial,Shebuti Rayana,Ahmedul Kabir
### Background
钦查马是一种印欧语系语言，具有有限的数据支持，因此在语言模型中的代表性不足。在这个工作中，研究人员介绍了从钦查马文献中收集的一种新的上下文一致的孟加拉语转写钦查马语语料库，并由土著演讲者进行了验证。使用这个数据集，研究人员对六种基于编码器的变压器模型（包括多语言模型mBERT、XLM-RoBERTa、DistilBERT，区域模型BanglaBERT、IndicBERT，以及单语英语模型DeBERTaV3）进行了微调，在填补语言建模任务上进行了实验。
### Innovation
研究人员通过填补语言建模任务，在多种模型（包括多语言、区域性和单语模型）上对孟加拉语转写钦查马语进行了微调。实验结果显示，微调后的多语言模型在这项任务中表现出色，相对于预训练模型而言，其准确率达到73.54%，困惑度仅为2.90。此外，研究还揭示了数据质量对模型性能的影响，并指出了光学字符识别（OCR）流水线对于形态丰富的印度脚本的局限性。这项研究证明了孟加拉语转写钦查马语言在钦查马语言的迁移学习中非常有效，并发布了数据集，以促进多语言语言建模领域对低资源语言的研究。
### Conclusion
这项研究证明了孟加拉语转写钦查马语言在钦查马语言的迁移学习中非常有效，并通过实验展示了微调多语言模型在高度稀缺资源语言上的潜力。此外，研究还强调了数据质量和OCR流水线对语言建模的影响，并将数据集发布以促进进一步的研究。
## 366. `cs.CL` - Meursault作为数据点 [PDF](https://arxiv.org/pdf/2502.01364), [HTML](https://arxiv.org/abs/2502.01364)
### Authors
Abhinav Pratap
### Background
在数据化时代，人类体验被转化为可量化的指标，这引发了深刻的哲学和伦理困境。本文通过阿尔贝·加缪的《局外人》中的主人公莫尔索来探讨这些问题，莫尔索的情感疏离象征着存在主义概念中的虚无主义。本文使用自然语言处理技术（包括情感检测、VADER情感分析和命名实体识别等），量化了莫尔索生活中关键事件和行为。研究揭示了将算法模型应用于复杂人类体验的局限性，特别是那些植根于存在主义疏离和道德模糊性的体验。
### Innovation
本文通过将文学作品中的主人公（莫尔索）转化为数据点，使用自然语言处理技术（如情感检测、VADER情感分析和命名实体识别等）进行量化分析，探究算法模型在处理复杂人类经验方面的局限性，特别是那些具有存在主义疏离和道德模糊性的体验，从而挑战了数据驱动社会的基础假设。
### Conclusion
研究结果强调减少人类叙事为数据点的伦理困境，并提倡在人工智能中结合人文价值观。这些发现是对日益依赖数据驱动叙事的批评，并主张在人工智能中纳入人文价值。
## 367. `cs.CL` - 联邦大型语言模型：当前进展与未来方向 [PDF](https://arxiv.org/pdf/2409.15723), [HTML](https://arxiv.org/abs/2409.15723)
### Authors
Yuhang Yao,Jianyi Zhang,Junda Wu,Chengkai Huang,Yu Xia,Tong Yu,Ruiyi Zhang,Sungchul Kim,Ryan Rossi,Ang Li,Lina Yao,Julian McAuley,Yiran Chen,Carlee Joe-Wong
### Background
大语言模型正在迅速获得流行并在实际应用中广泛应用。尽管训练数据的质量很重要，但在数据采集过程中也会引发隐私问题。联邦学习通过让多个客户端在不共享本地数据的情况下协作训练大语言模型，为解决这一问题提供了途径。然而，联邦学习也带来了新的挑战，如异质数据导致的模型收敛问题以及高通信成本。为应对这些挑战，指导未来研究，需要进行全面的研究。
### Innovation
本文对联邦学习在大语言模型中的应用（FedLLM）进行了综合研究，强调了最近的发展和未来方向。重点关注了联邦学习环境中的微调和提示学习，讨论了现有工作及其相关的研究挑战。
### Conclusion
本文最终提出了联邦大语言模型的潜在发展方向，包括预训练、联邦代理以及用于联邦学习的大语言模型。
## 368. `cs.CL` - 在组合任务结构中表征模式匹配及其局限性 [PDF](https://arxiv.org/pdf/2505.20278), [HTML](https://arxiv.org/abs/2505.20278)
### Authors
Hoyeon Chang,Jinho Park,Hanseul Cho,Sohee Yang,Miyoung Ko,Hyeonbin Hwang,Seungpil Won,Dohaeng Lee,Youbin Ahn,Minjoon Seo
### Background
尽管大型语言模型（LLMs）具有出色的性能，但它们的成功通常依赖于模式匹配行为，这些行为也与在组合任务中OOD泛化失败有关。常见的行为研究通过提供多种泛化源（例如代数不变性和结构重复）的任务设置，模糊了LLMs通过模式匹配进行泛化的精确且可测试的评估。本文旨在通过明确模式匹配的概念并系统研究这一机制来解决这一模糊性。
### Innovation
本文首先将模式匹配形式化为功能等价性，即识别在其余输入保持不变的情况下，输入序列子序列间始终产生相同结果的配对。然后，在具有隔离此机制的组合结构的受控任务中，系统地研究了仅解码器Transformer和Mamba的行为。研究结果提供了预测性和定量性的见解，包括模式匹配成功度与见证相关功能等价性的上下文数量之间的关系，学习两跳结构的样本复杂性边界，路径模糊性作为结构障碍，以及链式推理减少数据需求但无法解决路径模糊性。
### Conclusion
本文提供了一种预测性和可验证的模式匹配边界，并为理解混合泛化机制提供了基础诊断。
## 369. `cs.CL` - LogicOCR：您的大型多模态模型是否能在富含文本的图像上的逻辑推理方面表现出色？ [PDF](https://arxiv.org/pdf/2505.12307), [HTML](https://arxiv.org/abs/2505.12307)
### Authors
Maoyuan Ye,Haibin He,Qihuang Zhong,Jing Zhang,Juhua Liu,Bo Du
### Background
大型多模态模型（LMMs）在光学字符识别（OCR）方面取得了重大进展，但在处理包含丰富文本的图像的复杂逻辑推理能力上仍存在不足。
### Innovation
本文提出了一种新的基准测试——LogicOCR，包含2780个问题，分为两个子集：LogicOCR-Gen（1100个多选题）和LogicOCR-Real（1680个自由格式问题）。同时，作者提出了TextCue，一种无需训练的方法，可以增强LMMs对包含关键文本线索的图像区域的感知。通过利用LMMs的注意力图和开箱即用的文字切分专家，进一步增强原始图像的准确性。
### Conclusion
多维度分析揭示了测试时缩放的影响、输入模态差异和对视觉-文本方向的敏感度。LMMs在多模态推理方面仍然落后于纯文本输入，表明视觉阅读与推理尚未完全融合。此外，作者通过TextCue方法展示了在Chain-of-Thought设置下，准确率提升了1.8%。基准测试对研究大型多模态模型在图像上的逻辑推理能力提供了重要工具。
## 370. `cs.CL` - CAPability: 一个全面的视觉标题基准，用于评估正确性和详尽性 [PDF](https://arxiv.org/pdf/2502.14914), [HTML](https://arxiv.org/abs/2502.14914)
### Authors
Zhihang Liu,Chen-Wei Xie,Bin Wen,Feiwu Yu,Jixuan Chen,Pandeng Li,Boqiang Zhang,Nianzu Yang,Yinglu Li,Zuan Gao,Yun Zheng,Hongtao Xie
### Background
随着现代多模态大型语言模型（MLLMs）的发展，视觉标题基准已经过时。现有的基准使用简短的地面真实句子和传统评估指标难以有效地评估详细的标题。虽然最近的基准试图通过关注关键词提取或以对象为中心的评估来解决这个问题，但它们仍然局限于模糊视角或对象视角的分析，并且未能覆盖完整的视觉元素。
### Innovation
该论文提出了CAPability，这是一个全面的多视角基准，用于评估视觉标题的12个维度中的详尽性与正确性。它包含近11000个人工标注的图像和视频，并附带视觉元素的标注。CAPability使用精度和命中率指标稳定评估生成的标题的正确性和详尽性。此外，通过将标注转換为问答对，引入了一个新的启发式指标，即“知道但不能说”（$Kbar{T}$），它反映了问题回答能力和视觉标题生成能力之间的显著差距。
### Conclusion
我们的工作提供了一个全面的分析框架，以评估MLLMs的标题生成能力。我们识别了他们在不同维度上的优点和不足，指导未来的研究以增强特定方面的能力。
## 371. `cs.CL` - 利用大规模语言模型和测试驱动开发法进行可靠的和可验证的电子表格代码生成：一种研究框架 [PDF](https://arxiv.org/pdf/2510.15585), [HTML](https://arxiv.org/abs/2510.15585)
### Authors
Simon Thorne,Advait Sarkar
### Background
大型语言模型（LLMs）如ChatGPT等，正被广泛应用于生成传统软件代码和电子表格逻辑。尽管它们的生成能力令人印象深刻，但这些模型经常会出现诸如幻觉、细微逻辑不一致和语法规则错误等问题，特别是在金融建模和科学计算等高风险领域，准确性与可靠性至关重要。针对这些问题，本文建议将测试驱动开发（TDD）与LLM驱动的生成结合，以提高生成输出的正确性、可靠性和用户信心。
### Innovation
本文提出了一种结构化的研究框架，将测试驱动开发（TDD）与大型语言模型（LLMs）生成相结合，旨在提高生成输出的准确性和可验证性。框架包括一个明确的实验设计方案，定义了参与者小组，评估指标以及基于TDD的示例提示方法，强调通过测试驱动思维来改善计算思维、提示工程技能和用户参与度，特别有助于缺乏正式编程培训但可能因逻辑错误而导致严重后果的电子表格用户。
### Conclusion
本文旨在通过合作来细化和完善这一方法，并通过实证研究来评估其效果，最终确立一个负责任且可靠的LLM整合模式，可在教育和职业发展实践中推广应用。
## 372. `cs.CL` - 超越内省：通过外部行为反馈强化思考 [PDF](https://arxiv.org/pdf/2501.01457), [HTML](https://arxiv.org/abs/2501.01457)
### Authors
Diji Yang,Linda Zeng,Kezhen Chen,Yi Zhang
### Background
在推理阶段，大型语言模型（LLMs）能够解决复杂问题，但由于模型的随机性，其推理过程可能会变得不可靠或不一致，特别是在其知识边界附近。现有的方法试图通过让模型批评其自身的推理来进行修正。然而，这种自我批评继承了原本推理的偏见，这就是所谓的内省错觉。现有方法大多依赖模型的内省，针对这一局限，本文借鉴了动物行为学的核心方法，提出了一种外部主义的三步框架，Distillation-Reinforcement-Reasoning（DRR）。该框架通过模型的可观察行为来提供纠正反馈，而不依赖于模型的内省。
### Innovation
论文提出了一种外部主义的三步框架，Distillation-Reinforcement-Reasoning（DRR），该框架通过评估模型的可观察行为来提供纠正反馈，而不是依赖于模型的内省。DRR 的实施过程包括：首先提取推理器的行为痕迹，然后训练一个轻量级的外部判别模型（DM）。推理时，该 DM 起到批评者的作用，识别并拒绝可疑的推理步骤。这种外部反馈促使 LLM 抛弃有缺陷的路径，探索替代方案，从而提高推理的质量。
### Conclusion
实验结果表明，DRR 框架在多个推理基准上显著优于现有的自我批评方法。DRR 的轻量级和无需注释设计使得其可以为不同领域的 LLM 提供一种可扩展且适应性强的解决方案，以提高推理的可靠性。
## 373. `cs.CL` - Where to Start Alignment? Diffusion Large Language Model May Demand a Distinct Position [PDF](https://arxiv.org/pdf/2508.12398), [HTML](https://arxiv.org/abs/2508.12398)
### Authors
Zhixin Xie,Xurui Song,Jun Luo
### Background
差分大语言模型（dLLMs）作为一种独特的非自回归范式，近年来因其独特的训练和推理方法而崭露头角。然而，目前尚缺乏对这种新型架构的安全性研究。本文首次对dLLMs的安全性能进行了分析，并提出了一种针对其独特生成特性的新型安全对齐方法。
### Innovation
文章揭示了dLLMs中防御者和攻击者在安全性方面的重要不对称性，指出响应中间的token比初始token更为关键。基于这一不对称性，文章提出了Middle-tOken Safety Alignment（MOSA）方法，通过强化学习直接对模型的中间生成进行安全对齐。
### Conclusion
通过对两种基准测试的八种攻击方法进行比较，MOSA方法证明了其在安全性上的优越性，并证实了MOSA对dLLMs在编程、数学和一般推理中的适用性。
## 374. `cs.CL` - 视觉思考，文本推理：视觉-语言协同在ARC中的应用 [PDF](https://arxiv.org/pdf/2511.15703), [HTML](https://arxiv.org/abs/2511.15703)
### Authors
Beichen Zhang,Yuhang Zang,Xiaoyi Dong,Yuhang Cao,Haodong Duan,Dahua Lin,Jiaqi Wang
### Background
前沿基础模型如GPT-5和Grok 4在从少量示例中推断结构化转换规则方面仍存在核心未解决的问题。现有的大多数方法将ARC-AGI视为纯文本推理任务，忽视了人类在解决此类谜题时高度依赖视觉抽象的事实。初始实验证明，将ARC-AGI网格简单地转化为图像会因规则执行不够精确而导致性能下降。
### Innovation
提出两种协同策略：视觉-语言协同推理（VLSR）和模态切换自动校正（MSSC）。VLSR将ARC-AGI任务分解为模态对齐子任务；MSSC利用视觉验证文本推理，进行内在错误纠正。实验表明，这种方法在多个ARC-AGI任务中比仅基于文本的方法提高了4.33%。
### Conclusion
研究结果表明，将视觉抽象与语言推理统一起来是实现未来基础模型具有可推广性的类人智能的关键步骤。
## 375. `cs.CL` - 在上下文学习中的任务导向信息删除机制 [PDF](https://arxiv.org/pdf/2509.21012), [HTML](https://arxiv.org/abs/2509.21012)
### Authors
Hakaze Cho,Haolin Yang,Gouki Minegishi,Naoya Inoue
### Background
In-context Learning (ICL) 是基于现代语言模型（LMs）的一种新兴的少样本学习范式，尽管它已经取得了显著的效果，但其内在机制依然不太清楚。该研究通过一个新的信息移除视角，探索了ICL的工作原理。
### Innovation
该研究提出了一个新的视角来理解ICL的机制，特别是通过信息移除这一角度。研究发现，在零样本场景中，LMs会产生包含所有可能任务信息的非选择性表示，导致没有聚焦在特定任务上，导致输出几乎无意义。在此基础上，研究展示了通过低秩滤波器有选择地从隐藏状态中移除特定信息，使LMs更接近于预期任务。此外，研究还发现了一些关键的注意力头，称为去噪头部，这些头部的关键作用在于它能够去除冗余信息，从而提升输出的准确性。
### Conclusion
此研究通过精心设计的度量标准测量LMs的隐藏状态，并观察到少样本ICL有效模拟了任务导向的信息删除过程。此外，研究还发现了执行信息移除操作的关键注意力头，这些头部的缺失会导致ICL性能显著下降，尤其是在少量示证中不存在正确标签的情况下，从而证实了信息移除机制和去噪头部的至关重要性。
## 376. `cs.CL` - TimeViper：一种用于高效长视频理解的混合Mamba-Transformer视觉-语言模型 [PDF](https://arxiv.org/pdf/2511.16595), [HTML](https://arxiv.org/abs/2511.16595)
### Authors
Boshen Xu,Zihan Xiao,Jiaze Li,Jianzhong Ju,Zhenbo Luo,Jian Luan,Qin Jin
### Background
处理长视频需要高效的模型架构和处理长期时序上下文的有效机制。现有模型在处理长视频时面临挑战。
### Innovation
TimeViper采用了一种混合Mamba-Transformer骨干，结合了状态空间模型的效率和注意力机制的表达能力。提出了TransV模块，将视觉令牌压缩并转移至指令令牌，同时保持多模态理解能力，从而有效处理超过10,000帧的长视频。此外，分析了Mamba和Transformer层的注意行为，提供了对混合模型可解释性的新见解。
### Conclusion
这项工作代表了开发、理解和压缩混合Mamba-Transformer架构的第一步。
## 377. `cs.CV` - DeeAD：视觉-语言-行动中的动态早期退出以实现高效的自动驾驶 [PDF](https://arxiv.org/pdf/2511.20720), [HTML](https://arxiv.org/abs/2511.20720)
### Authors
Haibo HU,Lianming Huang,Nan Guan,Chun Jason Xue
### Background
视觉-语言-行动（VLA）模型能够将感知、推理和轨迹生成统一到自动驾驶中，但这些模型由于深度变压器堆栈，存在显著的推理延迟。
### Innovation
提出了一种无需训练、行动引导的早期退出框架DeeAD，通过评估中间轨迹的物理可行性来加速VLA规划。引入了多跳控制器，根据评分变化率适应性跳过冗余层。
### Conclusion
在Bench2Drive基准上进行的实验表明，DeeAD可以实现至多28%的变压器层稀疏性和29%的延迟减少，在保持规划质量和安全性的前提下。
## 378. `cs.CV` - 移动边缘网络中的视频物体识别：局部跟踪还是边缘检测？ [PDF](https://arxiv.org/pdf/2511.20716), [HTML](https://arxiv.org/abs/2511.20716)
### Authors
Kun Guo,Yun Shen,Xijun Wang,Chaoqun You,Yun Rui,Tony Q. S. Quek
### Background
在资源受限的设备如交通摄像头中，基于逐帧视频分析的快速且准确的视频物体识别仍然是一个挑战。最近，移动边缘计算的进步使计算密集型目标检测可以卸载到配备高性能神经网络的边缘服务器上，而轻量级且快速的目标跟踪算法可以在设备上本地运行。这种混合方法提供了一个有前途的解决方案，但也引入了一个新挑战：决定何时执行边缘检测而非局部跟踪。以往研究在这方面缺乏有效的解决方案。
### Innovation
本文提出了两种长期优化问题，分别针对单设备和多设备场景，考虑连续帧间的时间相关性和移动边缘网络的动态条件。基于此，提出了适用于单设备场景的LTED-Ada算法，这是一种基于深度强化学习的方法，能够根据帧率、识别准确性和延迟要求，在局部跟踪和边缘检测之间自适应选择。在多设备场景中，利用联邦学习进一步改进了LTED-Ada算法，使其能够在设备之间协作训练策略，从而提升其对未见过的帧率和性能要求的泛化能力。
### Conclusion
最后，通过使用多个Raspberry Pi 4B设备和个人电脑作为边缘服务器进行详尽的硬件在环实验，验证了LTED-Ada算法的优越性。
## 379. `cs.CV` - Inferix:基于块扩散的下一代世界仿真推理引擎 [PDF](https://arxiv.org/pdf/2511.20714), [HTML](https://arxiv.org/abs/2511.20714)
### Authors
Inferix Team:Tianyu Feng,Yizeng Han,Jiahao He,Yuanyu He,Xi Lin,Teng Liu,Hanfeng Lu,Jiasheng Tang,Wei Wang,Zhiyuan Wang,Jichao Wu,Mingyang Yang,Yinghao Yu,Zeyu Zhang,Bohan Zhuang
### Background
世界模型在代理AI、具身AI和游戏等领域中作为核心模拟器使用，可生成长篇、物理上真实且交互性的高质量视频。这些模型的扩展可以解锁视觉感知、理解和推理中的新兴能力，从而开启一个新的范式，超越当前以LLM为中心的视觉基础模型。关键的突破在于半自回归（块扩散）解码范式，它结合了扩散和自回归方法的优点，在每个块中应用块扩散并条件化于之前的块，生成更连贯且稳定的一系列视频片段。这种方法克服了标准视频扩散的局限性，重新引入了类似LLM的KV缓存管理，实现了高效的、可变长度的高质量生成。
### Innovation
Inferix专门设计为下一代推理引擎，通过优化半自回归解码过程实现沉浸式世界合成。它专注于世界模拟，区别于为了高并发场景设计的系统（如vLLM或SGLang）和经典视频扩散模型（如xDiTs）。Inferix还增加了交互式视频流和性能分析功能，以实现实时交互和逼真的模拟，准确建模世界动态。此外，它通过无缝集成LV-Bench（一个针对分钟级视频生成场景的新细粒度评价基准）支持高效的基准测试。
### Conclusion
我们希望社区能够共同努力推进Inferix的发展，推动世界模型的探索。
## 380. `cs.CL` - Step-Audio-R1 技术报告 [PDF](https://arxiv.org/pdf/2511.15848), [HTML](https://arxiv.org/abs/2511.15848)
### Authors
Fei Tian,Xiangyu Tony Zhang,Yuxin Zhang,Haoyang Zhang,Yuxin Li,Daijiao Liu,Yayue Deng,Donghang Wu,Jun Chen,Liang Zhao,Chengyuan Yao,Hexin Liu,Eng Siong Chng,Xuerui Yang,Xiangyu Zhang,Daxin Jiang,Gang Yu
### Background
近年来的推理模型在文本和视觉领域取得了显著成功，主要依赖于扩展的推理链。然而，在音频语言模型中存在一个令人困惑的现象：音频模型常常在几乎不需要推理的情况下表现出色，这引发了一个基础问题——音频智能是否真的能够从深思熟虑的思考中获益？
### Innovation
Step-Audio-R1 是第一个成功在音频领域解锁推理能力的创新音频推理模型。该模型通过提出的模态接地推理蒸馏（MGRD）框架，能够生成与音频相关的真正基于声学特征的推理链，而不是产生与实际无关的想象推理。Step-Audio-R1 在全面的音频理解与推理基准测试中（覆盖了语音、环境声音和音乐）都表现出强大的音频推理能力，其性能甚至超过了 Gemini 2.5 Pro，并达到了与最新 Gemini 3 Pro 相当的水平。
### Conclusion
该结果表明，当适当锚定时，推理可以作为一种在不同模态之间能够转移的能力，将延长的推理从负担转变为音频智能中的强大力量。通过建立第一个成功的音频推理模型，Step-Audio-R1 为构建真正多模态推理系统开辟了新的途径，这些系统能够在所有感知模态中进行深入思考。
## 381. `cs.CV` - Text-Guided Semantic Image Encoder [PDF](https://arxiv.org/pdf/2511.20770), [HTML](https://arxiv.org/abs/2511.20770)
### Authors
Raghuveer Thirukovalluru,Xiaochuang Han,Bhuwan Dhingra,Emily Dinan,Maha Elbayad
### Background
现有视觉语言模型（VLMs）中的图像编码器通常在独立预训练后与语言模型对齐，这导致图像处理过程不受下游任务或文本查询的影响。这种标准范式使得图像编码器在处理图像时缺乏针对性。
### Innovation
提出了基于文本的语义图像编码器（TIE），该编码器生成的图像表示根据输入的文本查询生成。具有TIE的VLMs在9个图像到文本基准测试中的1B和3B规模上分别平均提高了1.5和1.3个点，并在DocVQA和InfoVQA任务中最高达到了6个点的提升。使用TIE的VLMs在图像数据使用量方面减少了50%，同时保持或提高了性能，显著提高了推断效率。TIE在通用查询中也表现出了很好的泛化能力，表明文本条件下的训练有效优化了编码器以捕捉关键视觉特征。
### Conclusion
TIE 改进了视觉语言模型，通过文本查询条件训练提高了模型的图像处理能力和推断效率，并在多个基准测试中展示了优越的性能和泛化能力。
## 382. `cs.CL` - AutoDiscovery：通过贝叶斯惊奇实现的开放式科学发现 [PDF](https://arxiv.org/pdf/2507.00310), [HTML](https://arxiv.org/abs/2507.00310)
### Authors
Dhruv Agarwal,Bodhisattwa Prasad Majumder,Reece Adamson,Megha Chakravorty,Satvika Reddy Gavireddy,Aditya Parashar,Harshit Surana,Bhavana Dalvi Mishra,Andrew McCallum,Ashish Sabharwal,Peter Clark
### Background
现有的自主科学发现（ASD）工作主要依赖于人类指定的研究问题来引导关于假设的研究，这种方法的局限性在于其探究过程由人类标准驱动，可能限制了发现新知识的潜力。因此，论文提出通过贝叶斯惊奇的方法进行开放式科学发现，旨在利用AI系统自身标准来促进探索，由此可能会加速科学发现。
### Innovation
论文提出了AutoDiscovery方法，该方法使用贝叶斯惊奇来引导开放式科学探索。AutoDiscovery通过计算LLM（语言模型）在实验结果收集前后关于假设的先验信念和后验信念之间的知识转变来进行探索。为了有效探索嵌套假设的空间，该方法使用蒙特卡洛树搜索策略（MCTS）并结合意外值作为奖励函数进行扩展。
### Conclusion
在对21个真实世界数据集的实验中，AutoDiscovery在给定预算下显著优于竞争对手，能发现更多被LLM视为令人惊讶的结果。此外，人类评估还表明，多数由该系统发现的结果对领域专家来说也是令人惊讶的，这表明AutoDiscovery是朝着构建开放式科学发现系统的重要一步。
## 383. `cs.CL` - UniChange：利用多模态大型语言模型统一变化检测 [PDF](https://arxiv.org/pdf/2511.02607), [HTML](https://arxiv.org/abs/2511.02607)
### Authors
Xu Zhang,Danyang Li,Xiaohang Dong,Tianhao Wu,Hualong Yu,Jianye Wang,Qicheng Li,Xiang Li
### Background
变化检测（CD）是监测和分析土地覆盖动态的基本任务。尽管最近高性能模型和高质量数据集显著提升了这一领域的水平，当前的模型仍存在一个关键限制。即它们通常只能从单类型标注数据中获取有限的知识，不能同时利用二元变化检测（BCD）和语义变化检测（SCD）数据集，导致其泛化能力较差且灵活性受限。
### Innovation
该论文提出了UniChange，一种基于多模态大型语言模型（MLLM）的统一变化检测模型。UniChange通过引入三种特殊标记：[T1]、[T2]和[CHANGE]，将生成语言能力和专门的变化检测功能结合起来，能够通过文本提示引导变化类别识别，从而克服多源数据集类别定义冲突的问题。实验结果表明，UniChange在四个公开基准数据集（WHU-CD、S2Looking、LEVIR-CD+和SECOND）上达到了SOTA性能，IoU得分分别为90.41、53.04、78.87和57.62，超越了所有之前的模型。
### Conclusion
本文提出了UniChange，一种通过多模态大型语言模型统一处理二元变化检测和语义变化检测的创新变化检测方案，显著提升了变化检测模型的泛化能力和灵活性，实验结果验证了其优越性能。
## 384. `cs.CV` - 仅需一个片段即可：从最少视觉线索进行联合表面材料重建和分类 [PDF](https://arxiv.org/pdf/2511.20784), [HTML](https://arxiv.org/abs/2511.20784)
### Authors
Sindhuja Penchala,Gavin Money,Gabriel Marques,Samuel Wood,Jessica Kirschman,Travis Atkison,Shahram Rahimi,Noorbakhsh Amiri Golilarz
### Background
理解材料表面对于机器人技术、模拟和材料感知等应用至关重要，但现有方法主要依赖于密集或全场景观察，这在受限或部分视角环境中限制了其效果。
### Innovation
SMARC模型是一个统一框架，能够在极少的视觉输入下对表面材料进行重建和分类。通过提供单张图像的10%连续片段，SMARC能够识别和重建完整的RGB表面，并同时分类材料类别。其架构结合了部分卷积U-Net与分类头，能够在极端观测稀疏下进行空间填充和语义理解。在Touch and Go数据集上与五种模型（包括卷积自编码器、Vision Transformer、Masked Autoencoder、Swin Transformer和DETR）进行对比测试，SMARC实现了最优结果。
### Conclusion
我们的研究证明了部分卷积在缺失数据下进行空间推理的优势，并为最少视觉感知的表面理解奠定了坚实基础。
## 385. `cs.CV` - LongVT：通过调用本地工具激励“处理长视频的思考” [PDF](https://arxiv.org/pdf/2511.20785), [HTML](https://arxiv.org/abs/2511.20785)
### Authors
Zuhao Yang,Sudong Wang,Kaichen Zhang,Keming Wu,Sicong Leng,Yifan Zhang,Chengwei Qin,Shijian Lu,Xingxuan Li,Lidong Bing
### Background
大型多模态模型（LMMs）在视频推理中显示出了巨大潜力，可以通过文本链式思考来进行。然而，它们对于长视频的推理仍然容易出现虚构现象，特别是在证据稀疏且时间分布分散的情况下。人类在处理长视频时，会先进行全局扫描，然后详细检查相关片段。因此，本文提出了LongVT，一种端到端的自主框架，通过交错的多模态链式工具思考，帮助进行“处理长视频的思考”。
### Innovation
LongVT框架利用了LMMs的时间定位能力，将其作为天然的视频裁剪工具，通过全局到局部的推理循环，逐步聚焦特定视频片段并重新取样更细粒度的视频帧，直到问题答案能够依托于检索到的视觉证据。与此同时，作者还收集了一个数据套件VideoSIAH，用于长视频推理任务的训练和评估，包括冷启动工具集成监督微调数据集、自主强化学习数据集和自主强化微调数据集。
### Conclusion
LongVT在四个具有挑战性的长视频理解和推理基准测试中，表现出色，持续优于现有的基准模型。文中还详细设计了三层训练策略，并进行了广泛的实证验证，这些方法和数据集已经公开展示，以促进研究和发展。
## 386. `cs.CV` - Foundry: Distilling 3D Foundation Models for the Edge [PDF](https://arxiv.org/pdf/2511.20721), [HTML](https://arxiv.org/abs/2511.20721)
### Authors
Guillaume Letellier,Siddharth Srivastava(IIT Delhi),Frédéric Jurie,Gaurav Sharma(IIT Kanpur)
### Background
基础模型通过大规模数据集上的自我监督学习（SSL）预训练，已经成为强有力的通用功能提取器。然而，它们巨大的规模和高计算成本使它们难以部署在像机器人和AR/VR头显这样的边缘设备上。现有压缩技术，如标准知识蒸馏，可以创建高效的‘专家’模型，但在牺牲基础模型所具有的下游任务无关的通用性方面，这是基础模型的一大优点。
### Innovation
我们提出了基础模型蒸馏（FMD），这是一种将大规模SSL模型压缩成紧凑、高效且忠实的代理的新范式，同时保留其通用表示能力。我们还介绍了Foundry，这是FMD在3D点云中的首次实现。我们的方法在教师的token级表示中引入了一个学生，训练学生学习一个压缩的SuperTokens集合，以重建教师的token级表示，捕捉其潜在空间的紧凑基。一个压缩模型在不同的下游任务中表现出强大的迁徙性，如分类、部分分割和少样本场景，同时使用显著更少的token和FLOPs，使其在资源受限的硬件上部署更加可行。
### Conclusion
Foundry能够在保持自监督学习基础模型的抽象表示能力的同时，将模型压缩到更小的规模，这使得它们更适合在资源受限的边缘设备上部署。
## 387. `cs.CV` - SPHINX：一种用于视觉感知和推理的合成环境 [PDF](https://arxiv.org/pdf/2511.20814), [HTML](https://arxiv.org/abs/2511.20814)
### Authors
Md Tanvirul Alam,Saksham Aggarwal,Justin Yang Chae,Nidhi Rastogi
### Background
本文介绍了Sphinx，一种合成环境，用于视觉感知和推理，旨在针对核心认知基本元素。Sphinx通过使用图样、瓷砖、图表、图标和几何基本元素程序生成谜题，并提供了验证的正确答案，这使得评估和大规模数据集构建能够更加准确和高效。此项研究背景在于评估现有大型视觉-语言模型（LVLM）在视觉和推理任务中的表现，发现最先进的GPT-5的准确性甚至低于人类水平。
### Innovation
Sphinx通过程序生成谜题，每个谜题都有验证的正确答案，可以精确地评估模型的性能，并帮助构建大规模数据集。此外，研究还展示了基于可验证奖励的强化学习（RLVR）在提升模型在视觉推理任务中的准确性方面的优越性能，并在外部视觉推理基准测试中也取得了显著的提升。
### Conclusion
研究结果表明，Sphinx可以作为评估大型视觉-语言模型性能的有效工具。尽管最先进的模型表现欠佳，但采用可验证奖励的强化学习方法在多个任务上取得了显著改进，这为多模态推理的进一步研究提供了前景。
## 388. `cs.CV` - CANVAS: 视觉语言模型在工具基础用户界面设计上的基准 [PDF](https://arxiv.org/pdf/2511.20737), [HTML](https://arxiv.org/abs/2511.20737)
### Authors
Daeheon Jeong,Seoyeon Byun,Kihoon Son,Dae Hyun Kim,Juho Kim
### Background
UI设计是一个迭代过程，在这个过程中，设计师使用Figma或Sketch等设计软件逐步改进作品。最近，在视觉语言模型（VLMs）中的工具调用方面取得了进展，表明这些模型可以使用设计软件和迭代编辑UI设计。对于VLMs潜在的与设计师在传统软件中的协作能力来说，了解并增强这种能力是重要的。然而，由于当前没有工具基础的设计性能基准，这种潜力仍然未知。
### Innovation
本文介绍了CANVAS，一个针对VLMs在工具基础用户界面设计上的基准测试。该基准包含598项基于工具的UI设计任务，这些任务从30种功能类别（如引导、消息）中的3.3K个移动UI设计中抽取了真实参考。CANVAS将任务分为两种类型：一是设计复制，评估复制整个UI屏幕的能力；二是设计修改，评估修改现有屏幕特定部分的能力。实验结果表明，领先的模型在工具调用方面更为策略性，从而提高了设计质量。
### Conclusion
研究结果发现，主流模型在基于工具的设计方面展示了更策略性的工具调用方式，提升了设计质量。此外，研究还识别了模型在基于工具设计中常见的错误规律，为未来增强基于工具的设计能力提供了指导。
## 389. `cs.CV` - DinoLizer：学习最佳方法进行生成性修复定位 [PDF](https://arxiv.org/pdf/2511.20722), [HTML](https://arxiv.org/abs/2511.20722)
### Authors
Minh Thong Doi(IMT Nord Europe, CRIStAL),Jan Butora(CRIStAL),Vincent Itier(IMT Nord Europe, CRIStAL),Jérémie Boulanger(CRIStAL),Patrick Bas(CRIStAL)
### Background
在生成性修复（Generative Inpainting）任务中，如何准确地定位和检测图像中的篡改区域仍然是一个挑战。现有的局部操作检测方法在处理大规模图像时表现不佳，尤其对于常见的后处理操作（如缩放、添加噪声和JPEG压缩）缺乏鲁棒性。
### Innovation
DinoLizer 是基于 DINOv2 模型的篡改定位方法，特别适用于生成性修复任务。它通过在 ViT 的特征嵌入上添加线性分类头，能够以高分辨率精确预测局部篡改。DinoLizer 使用滑动窗策略处理大尺寸图像，并通过后处理优化估计的二进制篡改掩码。实验结果表明，DinoLizer 在多种不同生成模型的数据集上超越了当前最优的局部篡改检测器，特别是在经过后处理操作后再评估时，表现尤为出色。
### Conclusion
DinoLizer 的全代码将在论文被接受后公开。研究证明确实具有微调后的 DINOv2 良好的表征能力，使其在深度造假定位方面具有显著优势。进一步分析显示 DINOv2 和其继任者 DINOv3 在深度造假本地化任务中的表现，进一步验证了 DinoLizer 的优越性。
## 390. `cs.CV` - 神经启发的多模态视觉-语言模型在成员推理隐私泄露中是否具有抗御能力？ [PDF](https://arxiv.org/pdf/2511.20710), [HTML](https://arxiv.org/abs/2511.20710)
### Authors
David Amebley,Sayanton Dibbo
### Background
随着代理AI时代的到来，多模态模型（MMs）的广泛应用引入了新的攻击向量，可能导致敏感训练数据泄露，引发隐私泄露。现有研究主要分析隐私攻击对单一模式AI-ML系统的威胁，而最近的研究表明，多模态模型（MMs）也可能易受隐私攻击。研究人员已经证实，受到生物启发的神经网络表示可以提高单一模式模型对抗对抗攻击的鲁棒性，但尚未研究神经启发的多模态模型是否也能抵抗隐私攻击。
### Innovation
本文提出了一个系统性的神经科学启发的拓扑正则化（tau）框架，用于分析多模态视觉-语言模型（VLMs）对基于图像-文本的推理隐私攻击的鲁棒性。这项研究通过BLIP、PaliGemma 2和ViT-GPT2三种VLMs在COCO、CC3M和NoCaps三个基准数据集上的实验，展示了神经启发的VLMs对于隐私攻击具有更高的鲁棒性，而在生成的描述与参考描述的相似性方面保持了模型的实用性。
### Conclusion
实验结果表明，对于BLIP模型，在使用COCO数据集时，采用拓扑正则化的神经启发VLMs的成员推理攻击成功率降低了24%的均值ROC-AUC，同时在MPNet和ROUGE-2指标上保持了类似模型实用性。进一步的评估结果验证了这些发现的的一致性。这项工作加深了对多模态模型隐私风险的理解，并提供了神经启发的VLMs在隐私威胁抗御能力方面的证据。
## 391. `cs.CV` - 通过分割-合并实现感知层的视频合成 [PDF](https://arxiv.org/pdf/2511.20809), [HTML](https://arxiv.org/abs/2511.20809)
### Authors
Ozgur Kara,Yujia Chen,Ming-Hsuan Yang,James M. Rehg,Wen-Sheng Chu,Du Tran
### Background
传统方法依赖标注数据集或手工编写的规则来生成视频内容，但这种方式在数据稀缺问题上存在不足。为了解决这一问题，本文提出了一种名为Split-then-Merge (StM)的新框架，旨在增强生成视频组成的控制能力。该框架能够将大量无标注的视频按照动态前景和背景进行动态拆分，然后重新合成，让模型学习动态主体与不同场景的交互方式。
### Innovation
StM框架引入了一种新型的感知变换训练管道，利用多层融合和增广技术实现具有用途感知的合成效果，并保持前景的真实性。该方法在量化基准和人类/视觉语言模型基于的定性评估中均优于当前最佳方法。
### Conclusion
实验结果显示，StM框架在生成真实感视频方面能够超越现有的最佳方法。欲了解更多信息，请访问项目页面：this https URL
## 392. `cs.CV` - 通过基于优化的视觉反转实现无训练扩散先验的文本到图像生成 [PDF](https://arxiv.org/pdf/2511.20821), [HTML](https://arxiv.org/abs/2511.20821)
### Authors
Samuele Dell'Erba,Andrew D. Bagdanov
### Background
扩散模型在文本到图像生成任务中已经达到了最先进水平，但其性能依赖于扩散先验网络将文本嵌入转换到视觉莫尔根空间，便于解码，而这种网络在计算上很昂贵且需要大量数据进行训练。
### Innovation
提出了一种无训练且无数据的替代方法，名为基于优化的视觉反转（OVI）。OVI从随机伪令牌初始化潜变量表示，并通过迭代优化最大化输入文本提示嵌入的余弦相似性。此外，提出了两种新的约束条件来规范OVI优化过程，使其朝向现实图像分布。实验表明，OVI可以替代传统的先验，且在受约束的OVI方法中，最近邻损失方法特别有效，所得定量分数与最先进数据高效的先验相当或更高。
### Conclusion
在现有基准测试如T2I-CompBench++中发现了一个关键问题，仅使用文本嵌入作为先验也能获得意外高的分数，尽管感知质量较低。通过这种方法增强了图像的视觉保真度，特别是最近邻方法，表明该想法值得进一步研究。代码将在接受后公开。
## 393. `cs.CV` - 重新审视KRISP：知识增强型视觉-语言模型的轻量级复现与分析 [PDF](https://arxiv.org/pdf/2511.20795), [HTML](https://arxiv.org/abs/2511.20795)
### Authors
Souradeep Dutta,Keshav Bulia,Neena S Nair
### Background
Facebook AI Research引出了KRISP [4]，它将结构化的外部知识整合到视觉-语言推理的管道中。尽管其效果显著，但原模型是为了大规模工业训练设计的，计算成本高，并且紧密耦合于一个大型骨干模型。在本文中，作者重新审视了KRISP，提供了一个轻量级复现，参数明显减少。
### Innovation
轻量级复现虽然仅能达到原模型效果的大约75%，但在此过程中发现了原论文未涵盖的设计缺陷、实际应用中的问题以及隐含的问题。通过系统性消融研究，作者探讨了在资源受限的情况下，知识增强型视觉问答（VQA）架构的可扩展性和有效性，包括在合成VQA数据集上的概念验证和在DAQUAR数据集上的评估。作者的模型具有低参数配置，并受限于外部知识图谱领域，避免了人工智能幻觉，且仅生成该领域内的输出，这使得模型能在智能手机和AR/VR等边缘设备上运行，进一步提高了离线视觉推理的效果。
### Conclusion
本文通过轻量级复现实现了一个高效的模型，虽然性能有所降低，但通过系统消融研究，作者揭示了知识增强VQA架构在资源受限环境下的局限性及改进方向，并展示了其在边缘设备上的应用潜力。
## 394. `cs.CV` - 动态采样网络的有趣特性 [PDF](https://arxiv.org/pdf/2511.20800), [HTML](https://arxiv.org/abs/2511.20800)
### Authors
Dario Morle,Reid Zaffino
### Background
动态采样机制在深度学习架构中已被应用于多种计算机视觉模型，但这些结构的理论分析尚未统一。
### Innovation
该论文通过开发并分析一种新型操作（即“扭曲”），将各种动态采样方法统一起来。通过此方法，可以重建现有的架构，如可变形卷积、活性卷积单元和空间变换网络。作者提供了这些操作的形式化分析，并揭示了正向和反向传播之间的独特不对称性。研究表明，这些机制代表了一种与传统平移不变算子完全不同的正交算子类别。此外，论文还研究了离散化效应的统计分析，并介绍了一种新的损失景观可视化方法，利用梯度更新信息直接促进理解学习行为。
### Conclusion
通过理论分析和实验研究，作者确定了动态采样网络稳定训练所需的条件，并研究了离散化效应的统计分析。最后，作者引入了一种新的损失景观可视化方法，利用梯度更新信息直接促进理解学习行为。
## 395. `cs.CV` - 用于减少小脑桥脑角池对比增强MRI药物剂量的深度学习模型 [PDF](https://arxiv.org/pdf/2511.20926), [HTML](https://arxiv.org/abs/2511.20926)
### Authors
Yunjie Chen,Rianne A. Weber,Olaf M. Neve,Stephan R. Romeijn,Erik F. Hensen,Jelmer M. Wolterink,Qian Tao,Marius Staring,Berit M. Verbist
### Background
在评估小脑桥脑角（CPA）褶皱中的听神经瘤（VS）时，通常需要进行对比增强T1加权MRI（T1ce）成像，并使用大量的对比剂。本文的研究背景是评估一种基于深度学习的模型，以减少对比剂剂量，同时保持图像质量和诊断性能。
### Innovation
本研究创新性地使用深度学习模型通过对低剂量T1ce进行模拟训练，恢复标准剂量的T1ce图像，从而提高了诊断对比度增强MRI图像的能力，使得在较低的对比剂剂量下仍能进行有效的病变检测与诊断特性评估。
### Conclusion
通过深度学习模型，低剂量的MRI图像质量得到了显著提高，使得在10%-30%的标准剂量下就能实现病变检测和诊断特征的评估。
## 396. `cs.CV` - MODEST: 多光学景深立体数据集 [PDF](https://arxiv.org/pdf/2511.20853), [HTML](https://arxiv.org/abs/2511.20853)
### Authors
Nisarg K. Trivedi,Vinayak A. Belludi,Li-Yun Wang,Pardis Taghavi,Dante Lok
### Background
在自主机器人和增强现实等系统中的相机视觉中，基于真实光学条件下的深度估计仍然是一个核心挑战。尽管在深度估计和景深渲染方面取得了一些进展，但研究仍受到缺乏大规模、高保真真实对数DSLR数据集的限制，限制了模型在合成数据上训练后的现实世界泛化和评估。
### Innovation
该论文介绍了第一个具有5472×3648像素的高分辨率立体DSLR数据集，包含18000张图像，系统地改变了复杂真实场景中的焦距和光圈，捕捉了专业相机系统的光学现实和复杂性。该数据集覆盖了50种光学配置，在2000张每种场景的图像中，每种焦距配置都有专门的标定图像集，以支持经典和基于学习方法的内部和外部标定评估。该数据集包含多尺度光学幻觉、反射表面、镜子、透明玻璃墙壁、细粒度细节以及自然/人造环境光变化等具有挑战性的视觉元素，旨在弥合合成训练数据与真实相机光学之间的现实差距。
### Conclusion
该数据集及其中包含的挑战旨在展示当前最先进的单目、立体深度估计和景深方法面临的挑战，并提出进行真实世界光学通用性研究。发布该数据集、标定文件和评估代码支持可再现的研究。
## 397. `cs.CV` - $?Delta$-NeRF：通过残差控制和知识传输实现神经辐射场的增量精炼 [PDF](https://arxiv.org/pdf/2511.20804), [HTML](https://arxiv.org/abs/2511.20804)
### Authors
Kriti Ghosh,Devjyoti Chakraborty,Lakshmish Ramaswamy,Suchendra M. Bhandarkar,In Kee Kim,Nancy O'Hare,Deepak Mishra
### Background
NeRFs在3D重建和新型视角合成方面展示了显著的能力。然而，大多数现有的NeRF框架在引入新视角时需要重新训练，这限制了其在数据按顺序到达的领域中的应用，特别是在基于卫星的地形分析中，该领域中区域会多次被观测。增量优化NeRF尚未得到充分探索，简单的增量方法在缺乏过去数据时容易导致灾难性遗忘。
### Innovation
提出了一种名为$?Delta$-NeRF的独特模块化残差框架，用于增量优化NeRF。$?Delta$-NeRF包括：（1）一个残差控制器，用于在冻结的基本NeRF中注入每层的校正，从而在没有访问过去数据的情况下进行优化；（2）一种基于不确定性感知门机制，通过自适应结合基本预测和优化预测来防止过度纠正；（3）一种视图选择策略，能够将训练数据减少47%而保持性能。此外，采用知识蒸馏将增强模型压缩为紧凑的学生网络（模型大小减少20%）。实验表明，$?Delta$-NeRF在保持与联合训练相似性能的同时，训练时间减少30-42%，并且在多项指标上优于现有基线，PSNR最高提高43.5%。
### Conclusion
实验结果表明，$?Delta$-NeRF不仅能在保持性能相似的情况下减少训练时间（30-42%），还能通过减少训练数据和使用知识蒸馏达到更好的基线模型优化效果，并且在多项指标上优于现有的基线方法，最大PSNR提高了43.5%，特别是在基于卫星的地形分析应用中具有显著的优势。
## 398. `cs.CV` - RefTr：3D 血管树中心线图的循环精炼 [PDF](https://arxiv.org/pdf/2511.20823), [HTML](https://arxiv.org/abs/2511.20823)
### Authors
Roman Naeem,David Hagerman,Jennifer Alvén,Fredrik Kahl
### Background
人体的管状树状结构，例如血管和肺部气道，对于材料运输至关重要。准确检测它们的中心线并保持正确的树状拓扑结构对于临床诊断、治疗规划和外科导航等任务是至关重要的。在这些应用中，保持高召回率至关重要，因为遗漏小分支可能导致由不完全评估或遗漏异常引起的致命错误。
### Innovation
RefTr通过循环精炼汇聚轨迹提出了一种3D图像到图模型，用于血管树的中心线生成。RefTr采用基于Transformer解码器的生产者-精炼器架构，其中生产者提出一组初始汇聚轨迹，精炼器对其进行循环精炼以生成最终轨迹并形成中心线图。汇聚轨迹表示允许精炼完整的轨迹，同时显式地强制执行有效的树状拓扑结构。循环精炼方案提高了精度，并在同一精炼器模块上复用多次步骤，使得与先前SOTA相比，在解码器参数减少2.4倍的情况下，仍然能够获得更高的精度。此外，还引入了一种高效的非最大值抑制算法，用于合并空间树图中的重复分支，进一步提高精度。
### Conclusion
RefTr在多个公共中心线数据集上的召回率优于先前的SOTA，精度相当，同时提供更快的推理速度和更少的参数，证明了它作为3D医学成像中血管树分析的新SOTA框架的潜力。
## 399. `cs.CV` - 从立体图像序列估计雾参数 [PDF](https://arxiv.org/pdf/2511.20865), [HTML](https://arxiv.org/abs/2511.20865)
### Authors
Yining Ding,João F. C. Mota,Andrew M. Wallace,Sen Wang
### Background
现有的雾估计方法通常顺序估计参数，容易导致误差传播。尽管之前的这些方法在某些场景下有效，但它们无法有效处理全球不均匀的实时雾场景。研究人员需要一个能够在存在雾的情况下，作为现有SLAM或里程计系统的附加模块，同时估计雾参数的方法，从而提高视觉感知在雾中的表现。
### Innovation
本文提出了一种新的方法，通过同时解决优化问题来估计所有雾参数，而不是顺序估计。该方法假设雾只是局部均匀的，因此可以在全球不均匀的环境中有效地处理实际的雾。此外，新创建的SDIRF数据集为准确应用大气散射模型到雾图像提供了支持，并且包括同一路线在阴天录制的清晰数据，有助于图像去雾和深度重建相关研究。
### Conclusion
与之前的雾估计方法相比，所提出的方法在合成数据上提供了最准确的估计，在实际雾环境中适应性也更好。作者的代码和SDIRF数据集现在公开提供，旨在推动雾环境中视觉感知的研究进展。
## 400. `cs.CV` - 平滑正则化用于高效视频识别 [PDF](https://arxiv.org/pdf/2511.20928), [HTML](https://arxiv.org/abs/2511.20928)
### Authors
Gil Goldman,Raja Giryes,Mahadev Satyanarayanan
### Background
研究提出了一种平滑正则化技术，旨在加强视频识别模型中的时间诱导偏置，特别有利于轻量级架构。该方法通过将连续帧中间层嵌入的变化建模为高斯随机游走（GRW），鼓励平滑性，从而减少急剧的表现性变化，促使低加速度解决方案更好地与视频中存在的自然时间一致性相匹配。通过利用这种强制的平滑性，轻量级模型可以更有效地捕捉复杂的时序动态。
### Innovation
该方法通过高斯随机游走（GRW）建模连续帧中间层嵌入的变化，鼓励平滑性，减少急剧的表现性变化，从而提高轻量级模型在视频识别方面的性能。实验结果显示，该技术在Kinetics-600数据集上提升了3.8%到6.4%的识别准确率。对于MoViNet模型家族，使用该平滑正则化后，准确率提高了3.8%到6.1%；而对于MobileNetV3和MoViNets-Stream模型家族，与之前的最佳模型相比，准确率提高了4.9%到6.4%。
### Conclusion
通过应用这种强制平滑性，轻量级模型可以在连接网络的同时更有效地捕捉复杂的时序动态，并且这种方法在轻量级模型中表现出显著的性能提升，同时保持较低的计算复杂度。
## 401. `cs.CV` - 开放词汇组成解释在神经元对齐中的应用 [PDF](https://arxiv.org/pdf/2511.20931), [HTML](https://arxiv.org/abs/2511.20931)
### Authors
Biagio La Rosa,Leilani H. Gilpin
### Background
神经元是深神经网络的基本构建块，其相互连接使AI实现了前所未有的成果。为了理解神经元如何编码信息，通过概念之间的逻辑关系进行的组成解释表达了神经元激活与人类知识的空间对齐。但这些解释依赖于由人工标注的资料集，因此它们的应用受到特定领域和预定义概念的限制。
### Innovation
本论文通过引入一种适用于视觉领域的框架，允许用户探究任意概念和数据集中的神经元。该框架利用开放词汇语义分割生成的掩码来计算开放词汇组成的解释。该框架分为三个步骤：定义任意概念、使用开放词汇模型生成语义分割掩码、并从这些掩码中推导出组成解释。相较之前的方法，论文不仅在定量指标上，还在人类的可解释性上进行了比较，并分析了从人工标注数据到模型标注数据时解释的变化，展示了给框架带来的额外功能—对任务和感兴趣特性灵活性的增强。
### Conclusion
论文比较了所提出的方法与以前的计算组成解释的方法，在定量指标和人类可解释性方面进行对比，并分析了从使用人工标注数据到使用模型标注数据时解释的差异。展示了该框架在灵活性方面给解释带来的额外能力。
## 402. `cs.CV` - 通过空文本嵌入优化实现文本到图像扩散模型的推理时对齐 [PDF](https://arxiv.org/pdf/2511.20889), [HTML](https://arxiv.org/abs/2511.20889)
### Authors
Taehoon Kim,Henry Gouk,Timothy Hospedales
### Background
Test-time alignment (TTA)旨在使模型在推理过程中适应特定的奖励函数，但现有方法往往会导致过度或不足优化问题（即奖励作弊）。本文旨在解决这一问题。
### Innovation
提出了Null-Text Test-Time Alignment (Null-TTA)，通过优化无条件嵌入在分类器自由引导中的无条件嵌入来实现模型对齐，而不是操控潜在或噪声变量。这种方法确保了在带有语义一致性的流形上进行对齐操作，防止了奖励作弊。由于无条件嵌入在分类器自由引导中作为模型生成分布的锚点，Null-TTA 能够直接引导模型生成分布向目标奖励靠拢，而无需调整模型参数。
### Conclusion
实验结果表明，Null-TTA在保持跨奖励泛化的高能力的同时实现了最先进的目标测试时对齐效果。这确立了语义空间优化作为一种有效且合理的TTA新模式的可行性。
## 403. `cs.CV` - GaINeR: 几何感知的隐式网络表示 [PDF](https://arxiv.org/pdf/2511.20924), [HTML](https://arxiv.org/abs/2511.20924)
### Authors
Weronika Jakubowska,Mikołaj Zieliński,Rafał Tobiasz,Krzysztof Byrski,Maciej Zięba,Dominik Belter,Przemysław Spurek
### Background
隐式神经表示（INRs）已成为建模连续2D图像的关键工具，支持高保真重建、超分辨率和压缩。SIREN、WIRE和FINER等流行架构展示了INR捕捉细微图像细节的潜力。然而，传统INRs缺乏明确的几何结构，对局部编辑或与物理模拟集成的处理能力有限，这限制了它们在动态或交互式设置中的应用。
### Innovation
提出了几何感知的隐式网络表示（GaINeR），这是一种结合可训练的高斯分布和基于神经网络的INR的新型框架。该模型通过神经网络预测RGB值，通过对给定图像坐标附近的K个最近高斯分布进行加权嵌入聚合。这种设计使得图像可以连续表示，几何结构可解释，并且局部编辑灵活，为物理感知的图像操纵提供了基础。
### Conclusion
该方法通过结合可训练的高斯分布和基于神经网络的INR，不仅提供了连续图像表示和可解释的几何结构，还允许灵活的局部编辑，为物理感知和交互式图像操作提供了坚实的基础。
## 404. `cs.CV` - 使用 Tip-of-the-Tongue 检索查询的无监督记忆建模 [PDF](https://arxiv.org/pdf/2511.20854), [HTML](https://arxiv.org/abs/2511.20854)
### Authors
Sree Bhattacharyya,Yaman Kumar Singla,Sudhir Yarram,Somesh Kumar Singh,Harini S I,James Z. Wang
### Background
视觉内容的记忆性对科学研究长久以来具有吸引力，应用范围广泛，从理解人类记忆的细微方面到增强内容设计。一个阻碍该领域发展的主要挑战是人力密集型的过程：从人类收集记忆性注释。这限制了可用于建模视觉内容记忆性的数据集的多样性和规模。现有大多数数据集仅收集视觉内容的综合记忆性评分，未能捕捉自然开放式回忆描述中存在的细微记忆信号。
### Innovation
我们引入了第一个专门设计用于建模视觉记忆性信号的大型无监督数据集，包含超过82,000个视频，并伴随详细的回忆数据。我们使用来自在线平台如Reddit的口头表达紧张（Tip-of-the-Tongue, ToT）检索查询。验证表明，我们的无监督数据集为两种记忆性相关任务提供了丰富的信号：回忆生成和ToT检索。专门针对我们数据集微调的大型视觉-语言模型，在生成视觉内容的开放式记忆性描述方面优于GPT-4o等最先进模型。我们还采用对比训练策略创建了首个执行多模态ToT检索的模型。
### Conclusion
我们的数据集和模型提出了一种新方向，推动了视觉内容记忆性研究的进步。
## 405. `cs.CV` - V$^{2}$-SAM: 结合SAM2与多提示专家进行跨视角物体对应 [PDF](https://arxiv.org/pdf/2511.20886), [HTML](https://arxiv.org/abs/2511.20886)
### Authors
Jiancheng Pan,Runze Wang,Tianwen Qian,Mohammad Mahdi,Yanwei Fu,Xiangyang Xue,Xiaomeng Huang,Luc Van Gool,Danda Pani Paudel,Yuqian Fu
### Background
跨视角物体对应，举例来说，代表任务为自我中心与外部中心物体对应，旨在在不同视角（例如自我中心和外部中心）之间建立一致性的一致关联。由于视角和外观的巨大变化，现有的分割模型，如SAM2，直接应用于此任务具有挑战性。
### Innovation
本文提出了一种统一的跨视角物体对应框架V^2-SAM，通过两个互补的提示生成器将SAM2从单视角分割适应到跨视角对应。具体地，基于DINOv3特征构建交叉视角锚提示生成器（V^2-Anchor），建立了几何感知的对应关系，并在交叉视角情况下首次实现了基于坐标的提示对SAM2的解锁；交叉视角视觉提示生成器（V^2-Visual）则通过一种新颖的视觉提示匹配器增强了基于外观的线索，从特征和结构两个视角对自我中心和外部中心的表示进行对齐。为了有效利用两种提示的优点，进一步采用了多专家设计，并引入了一种后验循环一致性选择器（PCCS），根据循环一致性选择最可靠的专家。
### Conclusion
广泛实验验证了V^2-SAM的有效性，在Ego-Exo4D（自我中心与外部中心物体对应）、DAVIS-2017（视频物体跟踪）及HANDAL-X（机器人就绪跨视角对应）数据集上取得了新的最佳性能。
## 406. `cs.CV` - UruDendro4: 用于降低松树P. taeda L.横截面图像中年轮检测基准数据集 [PDF](https://arxiv.org/pdf/2511.20935), [HTML](https://arxiv.org/abs/2511.20935)
### Authors
Henry Marichal,Joaquin Blanco,Diego Passarella,Gregory Randall
### Background
树轮生长量代表树木每年的木材增量，量化这种生长可以帮助研究人员评估哪种经营措施最适合每种树种。手动测量这种生长是耗时且准确性较差的，通常在横截面圆盘上沿4到8个径向方向进行。近年来，自动化算法和数据集的出现提高了准确性和自动检测年轮的能力。为了应对木材横截面数据稀缺的问题，本研究引入了UruDendro4数据集，这是一个包含102张Pinus taeda L.横截面样本的集合，每个样本都手工标注了年轮。与现有公共数据集不同，UruDendro4包含沿树干多个高度提取的样本，这使得可以使用手工标注的年轮建立体积模型以估计年木材量。
### Innovation
UruDendro4数据集为降低松树P. taeda L.横截面图像中年轮检测建立了基准，提供了102张横截面样本，并详细标注了年轮。此外，该研究使用最新的方法对自动环检测性能进行了基准测试，最高性能由DeepCS-TRD方法实现，为模型训练提供了优化参数，并且证实了包含该数据集的模型在年轮检测任务中的泛化能力。
### Conclusion
本研究通过提供UruDendro4数据集，解决了横截面数据稀缺的问题，为年轮检测提供了基准。研究中详细展示了自动环检测的最先进的方法，验证了最佳配置的参数，并且证明了包含该数据集的模型在年轮检测中的优越泛化能力。
## 407. `cs.CV` - 超越写实：StickerNet 学习富有表现力的图层组合艺术 [PDF](https://arxiv.org/pdf/2511.20957), [HTML](https://arxiv.org/abs/2511.20957)
### Authors
Haoming Lu,David Kocharian,Humphrey Shi
### Background
图像合成作为图像编辑流程中广泛应用的操作，传统上研究的重点在于实现视觉真实性以及语义合理性。然而，在现代内容创作环境中，许多合成图像并非旨在保留写实性。相反，在以获得社区认可为动力的在线平台中，用户往往更侧重于创造更具艺术性、趣味性或社会互动性的内容。受此观察启发，本文定义了一个新的图像合成任务——富有表现力的合成任务，该任务强调多样化的风格和宽松的位置逻辑，反映了用户在真实世界创意平台上的编辑习惯。
### Innovation
本文提出了一种名为 StickerNet 的两阶段框架，首先确定合成类型，然后预测透明度、蒙版、位置和缩放等放置参数。特别地，StickerNet 直接从一个匿名的在线视觉创作和编辑平台收集的180万次编辑操作中构建数据集，每个操作都反映了用户社区验证的放置决策。这种基于真实编辑行为的构建方式确保了任务定义与训练监督之间强有力的一致性。通过用户研究和定量评估，StickerNet 展现了学习实际编辑模式的有效性，即使面对该任务中的固有模糊性。
### Conclusion
本文提出了一种新的视觉理解方向，强调表达性和用户意图而不是写实性。StickerNet 在表达性和匹配人类放置行为方面优于常用基准，证明了在实际编辑模式的学习中，可以从不确定性中学习的有效性。
## 408. `cs.CV` - TrafficLens：使用大语言模型进行多相机交通视频分析 [PDF](https://arxiv.org/pdf/2511.20965), [HTML](https://arxiv.org/abs/2511.20965)
### Authors
Md Adnan Arefeen,Biplob Debnath,Srimat Chakradhar
### Background
交通摄像头在城市区域中至关重要，是智能交通系统的重要组成部分。多个交叉口的摄像头可以提高执法能力、交通管理和行人安全。然而，高效管理与分析多摄像头的视频流数据存在很大挑战，因为涉及大量数据。将此类大量视频数据进行分析需要先进的分析工具。尽管像ChatGPT这样的大型语言模型（LLMs）在文本任务上表现出色，但将它们集成到交通视频分析中需要将视频数据转换为文本，这耗时且延迟了对交通视频的及时利用以生成见解和调查事件。
### Innovation
本文提出了一种名为TrafficLens的定制算法，应用于多相机交通交叉口的分析。TrafficLens采用顺序方法，利用摄像头重叠的覆盖区域。它通过使用不同长度的标记，并且用前一个输出作为下一步的提示，以反复应用视觉语言模型（VLM），实现快速生成详细文本描述并减少处理时间。此外，还通过对象级别相似度检测器智能地跳过冗余的VLM调用。实验结果表明TrafficLens可以将视频到文本的转换时间最多减少4倍，同时保持信息准确性。
### Conclusion
实验结果说明TrafficLens能够通过利用高效的顺序方法和智能的冗余检测，显著减少视频到文本的转换时间，同时保持信息准确性，从而为交通视频分析应用提供了新的解决方案。
## 409. `cs.CV` - RefOnce: 将参考信息提炼至原型记忆中的引用伪装目标检测 [PDF](https://arxiv.org/pdf/2511.20989), [HTML](https://arxiv.org/abs/2511.20989)
### Authors
Yu-Huan Wu,Zi-Xuan Zhu,Yan Wang,Liangli Zhen,Deng-Ping Fan
### Background
现有的Ref-COD系统在测试阶段需要参考图像，这限制了其部署性并增加了延迟和数据收集的负担。
### Innovation
提出了一种Ref-COD框架，通过在训练过程中提炼参考信息到类别原型记忆中，并在推理阶段通过查询条件的原型混合生成参考向量，不依赖测试时的参考图像。此外，引入了一种双向注意对齐模块，通过调整查询特征和类别表示来弥合参考特征统计与伪装查询特征之间的表示差距。
### Conclusion
在大规模R2C7K基准测试中评估了提出的算法，实验证明其在多种方法中具有竞争力或更优的表现。代码可在上述链接获取。
## 410. `cs.CV` - 波前受限的被动遮挡物体检测 [PDF](https://arxiv.org/pdf/2511.20991), [HTML](https://arxiv.org/abs/2511.20991)
### Authors
Zhiwen Zheng,Yiwei Ouyang,Zhao Huang,Tao Zhang,Xiaoshuai Zhang,Huiyu Zhou,Wenwen Tang,Shaowei Jiang,Jin Liu,Xingru Huang
### Background
从视野之外的微弱光图案精确定位和分割被遮挡的物体是一项高度挑战性的任务，主要是由于多次散射和介质引起的扰动。现有的大多数方法基于实数建模或局部卷积操作，无法捕捉光波干涉传播的物理底层规律，特别是在低信噪比条件下，这些方法往往会收敛到非物理的解决方案，严重影响观察的稳定性和可靠性。
### Innovation
提出了一种名为WavePCNet的新颖的物理驱动波前传播补偿网络，用于模拟波前传播并增强被遮挡物体的感知。WavePCNet结合了三相波前复传播重构（TriWCP），引入了复振幅传输操作精确约束干涉传播行为，以及动量记忆机制有效抑制噪声积累。此外，还提出了一种高频率跨层补偿增强方法以构建多尺度感受野的频率选择通路，并动态建模层次间的结构一致性，从而在复杂环境条件下增强模型的鲁棒性和可解释性。
### Conclusion
在四个物理收集的数据集上的广泛实验表明，WavePCNet在准确性和鲁棒性方面均优于最先进的方法。
## 411. `cs.CV` - BUSTR: 配有描述符感知的视觉-语言模型的乳腺超声文本报告 [PDF](https://arxiv.org/pdf/2511.20956), [HTML](https://arxiv.org/abs/2511.20956)
### Authors
Rawa Mohammed,Mina Attin,Bryar Shareef
### Background
乳腺超声（BUS）的放射学报告自动生成（RRG）受到缺乏成像-报告配对数据集和大规模语言模型产生的幻觉风险的限制。现有的方法通常需要成像-报告配对的数据监督来生成 BUS 报告，而 BUSTR 提出了一种多任务视觉-语言框架，无需使用配对图像-报告监督即可生成 BUS 报告。
### Innovation
BUSTR 使用结构化描述符（如 BI-RADS、病理学、组织学）和Radiomics 特征构建报告，通过使用多头Swin 编码器在一个多任务损失的训练下学习描述符感知的视觉表示，其中该多头Swin编码器通过一个由基于输入和输出表示的令牌级交叉熵损失和余弦相似度对齐损失的双层目标进行训练，从而实现视觉和文本标记的对齐。该方法在两个公开的 BUS 数据集（BrEaST 和 BUS-BRA）上进行了评估，这两个数据集在大小和可用描述符上有所不同。
### Conclusion
结果表明，BUSTR 在标准自然语言生成指标和临床有效性指标方面优于现有方法，特别对于 BI-RADS 类别和病理等关键目标。使用结合令牌级损失和对齐损失进行训练的描述符感知视觉模型，可以在不影响成像-报告配对数据的情况下提高自动报告指标和临床效益。
## 412. `cs.CV` - GuardTrace-VL：通过迭代安全性监督检测不安全多模态推理 [PDF](https://arxiv.org/pdf/2511.20994), [HTML](https://arxiv.org/abs/2511.20994)
### Authors
Yuxiao Xiang,Junchi Chen,Zhenchao Jin,Changtao Miao,Haojie Yuan,Qi Chu,Tao Gong,Nenghai Yu
### Background
现有的多模态安全守护程序主要评估输入问题和最终答案，忽视了中间的推理过程，导致可能存在潜在的安全风险，如偏差推断或违反政策的视觉内容使用。因此，需要一种能够监测整个问题-思考-答案（QTA）流程并检测推理阶段中出现的不安全内容的方法。
### Innovation
GuardTrace-VL是基于视觉感知的安全审计器，通过联合图像-文本分析监测整个QTA管道，从而在推理阶段及时检测不安全内容。该方法通过多样化的提示策略构建了一个GuardTrace数据集，并通过MLRM和人类基于投票和验证的流水线进行精炼。此外，提出了一个包括数据精炼过程的三个阶段渐进式训练方案，使模型能够根据不同的风险水平学习复杂的和上下文依赖的安全偏好。
### Conclusion
GuardTrace-VL模型在不安全推理检测任务上的F1分数为93.1%，相比前最强的多模态安全防御方法，F1分数提高了13.5%。
## 413. `cs.CV` - 基于双归一化流的无反转样式转移 [PDF](https://arxiv.org/pdf/2511.20986), [HTML](https://arxiv.org/abs/2511.20986)
### Authors
Yingying Deng,Xiangyu He,Fan Tang,Weiming Dong,Xucheng Yin
### Background
样式转移是图像处理中的一个关键任务，能够通过在现实内容和艺术风格之间无缝融合生成视觉吸引力强的图像，适用于照片编辑和创造性设计等领域。近年来，基于扩散的训练无需求方法极大地推进了样式转移的进展，但这些方法依赖于复杂的解算过程，这会降低效率并导致视觉上的扭曲，尤其是在解算不准确的情况下。
### Innovation
本文提出了一种基于双归一化流的无反转样式转移框架。该框架通过双重归一化流，在仅向前传递的模式下解决从两幅不同时输入（内容图像和样式图像）中找到未知样式分布的问题。该方法并行预测内容和样式轨迹，通过动态中点内插融合轨迹，该过程结合两种路径的速度并适应不断变化的样式图像。通过联合建模内容、样式和样式化分布，设计的速度场保证了可靠融合，避免了简单的叠加方法的缺点。注意力注入进一步引导样式融合，增强视觉保真度、内容保真度和计算效率。
### Conclusion
广泛实验证明，本文方法在多样化的样式和内容上具有良好的泛化能力，提供了一种有效且高效的样式转移流水线。
## 414. `cs.CV` - Vision 得以实现的 知识: 一种多模态实体感知检索增强生成框架用于新闻图片字幕 [PDF](https://arxiv.org/pdf/2511.21002), [HTML](https://arxiv.org/abs/2511.21002)
### Authors
Xiaoxing You,Qiang Huang,Lingyu Li,Chi Zhang,Xiaopeng Liu,Min Zhang,Jun Yu
### Background
新闻图片字幕的目标是通过结合视觉内容和相关文章的上下文线索生成具有记者信息性的描述。尽管取得了进展，现有方法在三个关键挑战中仍表现不佳：（1）信息不完整覆盖；（2）跨模态对齐较弱；（3）视觉实体关联效果欠佳。
### Innovation
为了应对这些问题，该论文介绍了MERGE，首个多模态实体感知检索增强生成框架，用于新闻图片字幕。它通过构建以实体为中心的多模态知识库（EMKB），整合文本、视觉和结构化知识，增强背景检索；采用多阶段假设-字幕策略提高跨模态对齐；并通过动态检索指导视觉实体匹配，进一步增强远程关联性。
### Conclusion
在GoodNews和NYTimes800k数据集上的实验显示，MERGE在字幕质量和命名实体识别精度方面显著优于最先进的基线模型，分别提高了6.84和1.16个CIDEr分数，以及4.14和2.64个F1分数。此外，MERGE在未见过的Visual News数据集上也表现出良好的泛化能力，CIDEr和F1分数分别提高了20.17和6.22，展示了其强大的鲁棒性和跨领域适应性。
## 415. `cs.CV` - 在医疗AI中利用轻量级同态加密保护的隐私保存联邦视觉变换器学习 [PDF](https://arxiv.org/pdf/2511.20983), [HTML](https://arxiv.org/abs/2511.20983)
### Authors
Al Amin,Kamrul Hasan,Liang Hong,Sharif Ullah
### Background
跨医疗机构进行协作机器学习能够通过利用多样化的数据集提升诊断准确性，但是隐私法规如HIPAA禁止直接共享患者数据。联邦学习（FL）能够在不交换原始数据的情况下实现分散的训练，但是最近的研究表明，传统FL中的模型梯度仍然容易受到重建攻击，可能暴露敏感医疗信息。因此，本研究提出了一种结合视觉变换器（ViT）和同态加密（HE）的隐私保护联邦学习框架，用于安全的多机构组织的组织学分类。
### Innovation
该论文提出了一种基于ViT CLS标记同态加密的隐私保护联邦学习框架。CLS标记作为紧凑的768维特征表示，结合CKKS同态加密，在传输前对这些标记进行加密，以实现安全聚合。实验表明这种方法比梯度加密节省了30倍的通信量，同时保持了强大的隐私保证。此外，提出的基于CLS标记保护的方法防止了模型反转攻击，可以在加密文本上直接进行加密推理，每次聚合只需326KB的加密数据传输。
### Conclusion
该框架在未加密领域实现了96.12%的整体分类准确率，在加密领域实现了90.02%的分类准确率，验证了其既能保护隐私又能保持模型效果的有效性。
## 416. `cs.CV` - CaptionQA: 是你的描述像图像本身一样有用吗？ [PDF](https://arxiv.org/pdf/2511.21025), [HTML](https://arxiv.org/abs/2511.21025)
### Authors
Shijia Yang,Yunong Liu,Bohan Zhai,Ximeng Sun,Zicheng Liu,Emad Barsoum,Manling Li,Chenfeng Xu
### Background
图像描述在多媒体系统中作为高效的替代品，用于检索、推荐以及多步骤代理推理管道等方面，但当前的评估方法未能触及一个基本问题：图像的描述能否在实际下游任务中替代图像？为了回答这一问题，作者提出了一种基于效用的基准测试CaptionQA，该基准测试通过衡量图像描述支持下游任务的程度来评估模型生成的描述质量。
### Innovation
CaptionQA是一种扩展性强、领域依赖性高的基准测试，涵盖了自然图像、文档、电子商务和体感AI等4个领域，每个领域都有精细的分类（25个一级分类和69个二级分类），这些分类有助于识别特定领域任务中的有用信息。CaptionQA构建了33,027个密集标注的多项选择题（平均每张图像50.3个问题），这些问题明确要求使用视觉信息来回答，提供了对描述效用的全面测试。在评估协议中，大型语言模型仅使用描述来回答这些问题，直接测量描述是否保留了图像级别的效用，并可被下游语言模型利用。
### Conclusion
评估最先进的MLLMs（机器学习语言模型）表明，图像与其描述的效用之间存在显著差距。值得注意的是，几乎在传统图像-描述基准上表现相似的模型，在描述效用上的表现低至32%。研究者发布了CaptionQA基准测试以及一个开源的扩展管道，可在新领域中进行扩展。代码可以在给定的链接地址找到。
## 417. `cs.CV` - 从修复到分层拆解：重新利用生成性修复模型进行图像分层拆解 [PDF](https://arxiv.org/pdf/2511.20996), [HTML](https://arxiv.org/abs/2511.20996)
### Authors
Jingxi Chen,Yixiao Zhang,Xiaoye Qian,Zongxia Li,Cornelia Fermuller,Caren Chen,Yiannis Aloimonos
### Background
图像可以视为层叠的组成，前景对象在背景之上，并可能存在遮挡。这种分层表示法使元素可独立编辑，提供了更高内容创建的灵活性。尽管大型生成模型在进步中取得进展，但将单个图像分解为层仍然具有挑战性，受限于有限的方法和数据。本研究注意到分层拆解与修复/补画任务之间的强大关联，并提出利用轻量化微调的基于扩散的补画模型进行分层拆解。为了进一步在隐空间中保留细节，引入了一种新型的多模态上下文融合模块，其中包含线性注意力复杂度。
### Innovation
提出了利用轻量化微调的基于扩散的补画模型进行图像分层拆解，并引入了一种新型的多模态上下文融合模块，该模块具有线性注意力复杂度，以进一步在隐空间中保留细节。
### Conclusion
本模型仅在从开源资产构建的合成数据集上进行训练，实现了在物体去除和遮挡恢复方面的卓越性能，为下游编辑和创意应用解锁了新的可能性。
## 418. `cs.CV` - MUSE: 利用测试时优化统一框架在图像中操控情感合成 [PDF](https://arxiv.org/pdf/2511.21051), [HTML](https://arxiv.org/abs/2511.21051)
### Authors
Yingjie Xia,Xi Wang,Jinglei Shi,Vicky Kalogeiton,Jian Yang
### Background
图像能唤起强烈的情感，这些情感常常会影响感知，甚至可能超越内容本身的重要性。现有的图像情感合成（IES）方法通常将生成和编辑任务分开处理，导致效率低下，并限制了这些任务自然结合的应用场景，例如治疗干预或讲故事。然而，在这些应用中，情感生成和编辑往往是密不可分的。
### Innovation
本文介绍了一个名为MUSE的统一框架，这是第一个能够同时进行情感生成和编辑的框架。MUSE采用了与测试时缩放（TTS）策略概念上一致的方法，这种方法在LLM和扩散模型社区中广泛应用，从而避免了对额外更新扩散模型和专门情感合成数据集的依赖。MUSE解决关键情感合成问题如下：(1) 通过基于梯度优化的情感标记引导合成；(2) 通过语义相似性确定最优指导时机；(3) 通过一个多情感损失减少内建和类似情感的干扰。
### Conclusion
实验结果表明，MUSE在生成和编辑方面都优于所有方法，提高了情感准确性，提升了语义多样性，同时保持了理想的内容、文本提示的依从性及现实情感表达之间的平衡。该研究确立了情感合成的新范式。
## 419. `cs.CV` - CameraMaster: 统一的相机语义-参数控制以实现摄影修图 [PDF](https://arxiv.org/pdf/2511.21024), [HTML](https://arxiv.org/abs/2511.21024)
### Authors
Qirui Yang,Yang Yang,Ying Zeng,Xiaobin Hu,Bo Li,Huanjing Yue,Jingyu Yang,Peng-Tao Jiang
### Background
文本引导的扩散模型在图像编辑和生成方面取得了巨大进展，但仍难以实现具有精确参数控制的物理上一致的图像修饰（例如，曝光、白平衡、变焦调整）。
### Innovation
提出了一种统一的相机感知框架CameraMaster，通过明确分离开相机指令，并整合关键信息流：摄影师意图的指令表示和精确相机设置的参数嵌入。CameraMaster 通过相机参数嵌入来调控相机指令和内容语义，通过交叉注意力将调控后的指令注入内容特征，生成对相机高度敏感的语义上下文。且指令和相机嵌入作为条件和门控信号注入时间嵌入，实现统一、逐层的调控，并确保语义参数的紧密对齐。
### Conclusion
通过一个包含78,000幅图像-提示对并标注有相机参数的大规模数据集训练和评估CameraMaster，实验证明CameraMaster在参数变化上产生单调、接近线性的响应，在多参数无缝组成上具有优势，并显著优于现有方法。
## 420. `cs.CV` - MetaRank: Task-Aware Metric Selection for Model Transferability Estimation [PDF](https://arxiv.org/pdf/2511.21007), [HTML](https://arxiv.org/abs/2511.21007)
### Authors
Yuhang Liu,Wenjie Zhao,Yunhui Guo
### Background
在迁移学习中，选择合适的预训练源模型是一项既重要又计算成本高昂的任务。模型转移性评估(MTE)方法通过提供无需完全微调的高效代理指标来对比模型，从而缓解这一问题。然而，实践中选择哪种MTE指标往往依靠传统的经验或仅仅依据其历史平均性能，这种方法忽视了MTE指标与任务之间的高度相关性。
### Innovation
本文提出MetaRank，一种基于元学习框架的自动、任务感知的MTE指标选择方法。它将指标选择建模为排序学习问题，使用预训练语言模型编码数据集描述和MTE指标的文本描述，将其嵌入共享语义空间。通过离线训练元预测器，在各种元任务上学习数据集特性和指标机制之间的复杂关系，并优化列表目标函数以优先正确排名表现最佳的指标。通过这种方法，在随后的在线阶段可以高效地为新未知目标数据集排名候选的MTE指标。
### Conclusion
跨多种预训练模型和目标数据集的大量实验表明，MetaRank方法在评估模型转移性方面具有较强的效用。
## 421. `cs.CV` - 长期内因性痴呆预测：基于不规则时间序列的正常逆伽马分布中时间参数估计的新型图像生成方法 [PDF](https://arxiv.org/pdf/2511.21057), [HTML](https://arxiv.org/abs/2511.21057)
### Authors
Xin Hong,Xinze Sun,Yinhao Li,Yen-Wei Chen
### Background
图像生成在预测阿尔茨海默病(AD)方面为医师提供了影像诊断的基础。然而，现有的研究表明长期的AD预测，特别是在处理不规则时间间隔的序列数据时，难以保持疾病相关的特征。因此，当前研究旨在通过引入一个时间参数，基于正常逆伽马分布(Normal Inverse Gamma Distribution, NIG)来估算时间分布，从而辅助长期图像生成，进而预测疾病进展。
### Innovation
该研究提出了一种名为T-NIG的模型来估算时间参数，目的是利用来自两个不同时间点的大脑图像生成中间图像、预测未来图像以及预测疾病。T-NIG模型通过识别坐标邻域内的特征来设计，并将时间参数融入到NIG分布中，旨在理解具有不规则时间间隔的大脑成像序列中特征的变化情况。此外，T-NIG模型还利用不确定性估计来减少由于时间数据不足而产生的认识性和统计性不确定性。实验结果表明，T-NIG在短期和长期预测任务中表现出最先进的性能。
### Conclusion
实验结果表明，T-NIG模型在不规则时间数据分布的情况下，仍然能够在长期预测的同时保持疾病特征，有效预测疾病进展。
## 422. `cs.CV` - FlowerDance: MeanFlow for Efficient and Refined 3D Dance Generation [PDF](https://arxiv.org/pdf/2511.21029), [HTML](https://arxiv.org/abs/2511.21029)
### Authors
Kaixing Yang,Xulong Tang,Ziqiao Peng,Xiangyue Zhang,Puwei Wang,Jun He,Hongyan Liu
### Background
音乐到舞蹈生成的目标是将听觉信号转换为富有表现力的人类动作，具有广泛的应用前景，如虚拟现实、编舞和数字娱乐。尽管现有方法取得了有前景的进展，但生成效率的限制使得无法提供高保真的3D渲染，进而限制了实际应用中3D角色的表现力。
### Innovation
提出了FlowerDance，该方法不仅能生成物理合理性和艺术表现性高的动作，还能在推理速度和内存利用率方面实现显著的生成效率。具体而言，FlowerDance结合了MeanFlow与物理一致性约束，可以在少量采样步骤中生成高质量的运动。此外，FlowerDance采用BiMamba为基础的轻量级模型架构以及通道级跨模态融合，以非自回归的方式生成舞蹈动作，并支持动作编辑，使用户能够交互地细化舞蹈序列。
### Conclusion
在AIST++和FineDance上的广泛实验表明，FlowerDance在运动质量和生成效率上都达到了最先进的成果。
## 423. `cs.CV` - PG-ControlNet：一种基于物理的ControlNet生成空间变异性图像去模糊 [PDF](https://arxiv.org/pdf/2511.21043), [HTML](https://arxiv.org/abs/2511.21043)
### Authors
Hakki Motorcu,Mujdat Cetin
### Background
空间变异性图像去模糊依然是一个基本上难以解决的问题，尤其是在复杂运动和其他形式的模糊混合并且受到大量噪声影响的时候。当前最先进的基于学习的方法一般可以分为两类：一类是基于模型的深层去卷绕方法，这些方法通过建模去噪过程中的约束来实现，但经常会导致过度平滑并且含有艺术缺陷的纹理；另一类是生成模型，它们在感知质量上表现优越，但由于物理约束较弱，因此会创造出虚假的细节。
### Innovation
本文提出了一种新颖的框架，通过使用强大的生成先验和明确的密集物理约束相结合的方式，实现了这两种范式的独特统一。区别于过度简化模糊领域，本文将其建模为高维压缩核的密集连续体，确保能够捕捉到运动和其他模糊模式的微小变化。同时，利用这个丰富的描述域来调节ControlNet架构，强烈指导扩散采样过程。
### Conclusion
广泛的实验表明，本文的方法能够有效地弥合物理精度和感知现实之间的差距，在极端模糊场景下，我们的方法在与基于模型的最先进的方法以及生成性基线方法相比时表现更优越。
## 424. `cs.CV` - 为雷达场景理解缩放基础模型 [PDF](https://arxiv.org/pdf/2511.21105), [HTML](https://arxiv.org/abs/2511.21105)
### Authors
Pushkal Mishra,Kshitiz Bansal,Dinesh Bharadia
### Background
雷达传感器可以在恶劣天气、照明和远距离条件下提供可靠的感知。尽管基础模型在视觉和语言理解方面取得了显著进展，但它们与雷达传感的结合仍被大量忽视。现有雷达方法是碎片化的和任务特定的，每个下游任务都使用不同的架构和训练目标，阻碍了跨任务的学习转移。
### Innovation
本文介绍了RadarFM：一种雷达基础模型，通过结构化空间语言监督学习统一的场景级表示。关键贡献包括：1）一种结构化描述板车分布的方式，编码在雷达原位坐标的数据；2）一种基于哈希的对比学习目标，量化连续场景相似性，而非二元匹配，实现精细的空间推理。
### Conclusion
利用CARLA模拟器，生成了多元驾驶场景下的大规模高质量注解雷达数据集。还提出了定位感知度量，以评估空间准确性，超越传统检测指标。
## 425. `cs.CV` - 结构意识原型引导的信任多视图分类 [PDF](https://arxiv.org/pdf/2511.21021), [HTML](https://arxiv.org/abs/2511.21021)
### Authors
Haojian Huang,Jiahao Shi,Zhe Liu,Harold Haodong Chen,Han Fang,Hao Sun,Zhongjiang He
### Background
在复杂场景中，多源信息可能异构、不一致甚至冲突，这使得多视图分类（TMVC）面临可靠决策的挑战。现有TMVC方法大多依赖全局密集邻居关系来建模 intra-view 依赖关系，导致高计算成本且无法直接保证跨视图关系的一致性。此外，这些方法通常通过手动分配的权重来聚合不同视图的证据，缺乏保证所学习的多视图邻居结构在类别空间内一致性的机制，从而降低了分类结果的信任度。
### Innovation
为了克服这些局限性，我们提出了一个新的TMVC框架，引入原型来表示每个视图的邻居结构。通过简化 intra-view 邻里关系的学习并允许 intra-和跨视图结构的动态对齐，我们的方法促进了跨视图一致性共识发现的更高效和一致的发现。实证研究显示，与主流的TMVC方法相比，我们的方法在下游性能和鲁棒性方面具有竞争力。
### Conclusion
我们在多个公开的多视图数据集上进行了广泛的实验，结果显示我们的方法在下游性能和鲁棒性方面与主流TMVC方法竞争，并有效地解决了可靠性问题。
## 426. `cs.CV` - Pygmalion Effect in Vision: Image-to-Clay Translation for Reflective Geometry Reconstruction [PDF](https://arxiv.org/pdf/2511.21098), [HTML](https://arxiv.org/abs/2511.21098)
### Authors
Gayoung Lee,Junho Kim,Jin-Hwa Kim,Junmo Kim
### Background
在三维重建领域，理解和处理反射依然是一个长期存在的挑战。这是因为反射会引起视点依赖的外观和几何结构纠缠在一起。现有方法在处理复杂反射时效果欠佳，导致重构效果不理想。
### Innovation
本文提出了一种新的框架——Pygmalion 效应在视觉中。该方法通过图像到黏土转化，使用 BRDF 基本反射分支和黏土引导分支相结合的方式，抑制镜面反射线索，保持内在几何一致性，从而实现多视角图像中包含复杂反射的对象稳健重构。
### Conclusion
实验结果表明，与现有反射处理方法相比，该框架在表面法线准确性和网格完整性方面取得了显著提升。此外，该框架揭示了一种新的学习反射对象几何的启发式方法：通过消除反射，将辐射转化为中性，可以作为反射对象几何学习的强大归纳偏置。
## 427. `cs.CV` - LungNoduleAgent：专用于肺结节精准诊断的协作多agent系统 [PDF](https://arxiv.org/pdf/2511.21042), [HTML](https://arxiv.org/abs/2511.21042)
### Authors
Cheng Yang,Hui Jin,Xinlei Yu,Zhipeng Wang,Yaoqun Liu,Fenglei Fan,Dajiang Lei,Gangyong Jia,Changmiao Wang,Ruiquan Ge
### Background
肺癌诊断通常涉及医生在CT扫描中识别肺结节，并基于其形态特征和医学专业知识生成诊断报告。尽管已经发展了使用多模态大型语言模型分析肺CT扫描的技术，但仍存在准确描述结节形态和结合医学专业知识的挑战。这些局限性影响了这些模型在临床环境中的可靠性和有效性。协作多agent系统为在医学应用中实现准确性和普遍性之间的平衡提供了有希望的策略，但它们在病理学中的潜力尚未得到充分探索。
### Innovation
介绍了LungNoduleAgent，这是一种专为分析肺CT扫描设计的创新的协作多agent系统。LungNoduleAgent将诊断过程细分为步骤，通过三个主要模块提高结节描述的精确度和恶性分级：第一个模块“结节检测器”协调临床检测模型准确识别结节；第二个模块“放射科医生”结合局部图像描述技术生成全面的CT报告；最后，医生代理系统通过图像和CT报告进行恶性推断，并在病理学知识库及多agent系统框架支持下工作。广泛测试显示，LungNoduleAgent超越了主流的视觉-语言模型、代理系统和高级专家模型，突显了区域级语义对齐和多agent合作在诊断中结节的重要性。
### Conclusion
LungNoduleAgent作为一种支持肺结节临床分析的有前景的基础工具而脱颖而出。
## 428. `cs.CV` - CLRecogEye：基于 Curriculum Learning 的动态虹膜识别 [PDF](https://arxiv.org/pdf/2511.21097), [HTML](https://arxiv.org/abs/2511.21097)
### Authors
Geetanjali Sharma,Gaurav Jaswal,Aditya Nigam,Raghavendra Ramachandra
### Background
虹膜认证算法在识别性能上已经取得了显著的效果，使其在边境控制、公民身份验证、犯罪调查和商业系统等实际应用中具有很高的潜力。然而，这些算法的鲁棒性仍受到旋转、缩放、镜面反射和焦深模糊等变化的挑战。此外，大多数现有方法依赖于简单的点到点比较，通常使用余弦或L2距离，未能充分利用虹膜模式的时空结构。
### Innovation
本文提出了一种新颖且通用的匹配流水线，学习虹膜特征丰富的时空结构表示。首先，沿一个维度划分每个虹膜图像，生成用于3D-CNN的子图像序列，使网络能够捕捉时空线索。为了进一步提高时空特征动态建模，该模型以课程学习的方式进行训练，使得网络可以直接将时间依赖性嵌入特征空间，从而在深度度量领域提高辨别性。该框架通过三重和ArcFace损失以课程学习的方式进行端到端训练，即使在旋转、缩放、反射和模糊等挑战下也能提供高度可区分的嵌入。这种设计为动态虹膜识别提供了一个鲁棒且通用的解决方案。
### Conclusion
本文提出的方法在解决虹膜识别中旋转、缩放、镜面反射和模糊等挑战方面取得了显著效果，通过课程学习和时空特征捕捉，提高了模型的鲁棒性和可水平扩展性。该方法在实际应用中具有广泛的适用性，为虹膜识别技术的发展提供了新的视角。
## 429. `cs.CV` - 哪一层导致了分布偏离？基于熵的自适应剪枝方法用于扩散和流模型 [PDF](https://arxiv.org/pdf/2511.21122), [HTML](https://arxiv.org/abs/2511.21122)
### Authors
Changlin Li,Jiawei Zhang,Zeyi Shi,Zongxin Yang,Zhihui Li,Xiaojun Chang
### Background
大型视觉生成模型，包括扩散和流模型，在视觉生成任务中表现出了显著的能力。然而，将这些预训练模型转移到下游任务时，通常会出现大量的参数冗余问题。
### Innovation
提出了基于熵的自动渐进剪枝框架 EntPruner，用于扩散和流模型。引入了基于熵的剪枝策略，这是一种模块级别的重要性评估策略，特别针对生成模型。提出了基于条件熵偏差（CED）的数据依赖性指导度量，这是一种剪枝的重要度量。此外，还提出了一种零次自适应剪枝框架，可以在训练过程中自动确定何时以及要剪枝多少，从而避免一次性剪枝的不足，防止模式崩溃并保持模型性能。
### Conclusion
在 DiT 和 SiT 模型上的广泛实验证明了 EntPruner 的有效性，在保证 ImageNet 和三个下游数据集上生成质量的同时，实现了高达 2.22 倍的推理速度提升。
## 430. `cs.CV` - 变形感知的时间生成在阿尔茨海默病早期预测中的应用 [PDF](https://arxiv.org/pdf/2511.21114), [HTML](https://arxiv.org/abs/2511.21114)
### Authors
Xin Honga,Jie Lin,Minghui Wang
### Background
阿尔茨海默病（AD）是一种退行性脑病，可以通过早期预测来减缓其进展。随着病情的发展，患者通常会出现脑萎缩。目前，AD预测方法主要涉及通过手动特征提取分析脑影像的形态学变化。针对这些方法的局限性，提出了一种新的变形感知时间生成网络（DATGN），用于自动化学习与疾病发展相关的脑形态学变化，以实现早期预测。
### Innovation
DATGN方法通过先插补不完整的序列，随后利用双向时间变形感知模块指导网络生成符合疾病进展的未来MRI影像，从而实现早期预测。DATGN在ADNI数据集上测试生成未来MRI影像的时间序列，表现优于PSNR和MMSE图像质量指标，并且生成的合成数据结合SVM、CNN和3DCNN分类方法后，在AD vs. NC和AD vs. MCI vs. NC分类准确率上分别提高了6.21%到16%和7.34%到21.25%。质性可视化结果显示DATGN生成的MRI影像符合阿尔茨海默病中的脑萎缩趋势。
### Conclusion
研究提出了一种创新的时间生成网络（DATGN）方法，用于阿尔茨海默病的早期预测。该方法通过生成符合疾病进展的MRI影像，提高了分类准确率，并能提供一致的脑萎缩趋势影像。
## 431. `cs.CV` - FaithFusion: 基于像素级信息增益 harmonizing reconstruction and generation [PDF](https://arxiv.org/pdf/2511.21113), [HTML](https://arxiv.org/abs/2511.21113)
### Authors
YuAn Wang,Xiaofan Li,Chi Huang,Wenhao Zhang,Hao Li,Bosheng Wang,Xun Sun,Jun Wang
### Background
在可控驾驶场景重构和3D场景生成中，保持几何保真度并同时合成在大角度视野变化下视觉上合理的外观至关重要。然而，将基于几何的3D生成以及外观驱动的扩散模型进行有效的融合面临着固有的挑战，因为缺乏像素级别的3D一致的编辑标准通常会导致过度恢复和几何漂移。
### Innovation
本文提出了FaithFusion，一种基于像素级期望信息增益（Expected Information Gain，EIG）的3D生成与扩散融合框架。EIG作为一种统一的策略，用于协调时空合成：它作为空间先验引导扩散，以细化高不确定性区域，而其像素级别的权重则将编辑内容回传到3D生成中。
### Conclusion
实验在Waymo数据集上的结果证明，本方法在NTA-IoU，NTL-IoU和FID方面达到了SOTA性能，即使在6米的车道偏移下，其FID仍保持在107.47。代码已发布。
## 432. `cs.CV` - MIRA: 多模态迭代推理代理用于图像编辑 [PDF](https://arxiv.org/pdf/2511.21087), [HTML](https://arxiv.org/abs/2511.21087)
### Authors
Ziyun Zeng,Hang Hua,Jiebo Luo
### Background
指令引导的图像编辑为用户提供了一种通过自然语言直观进行图像编辑的方式。然而，基于扩散的方法在准确解释复杂的用户指令时常常面临困难，尤其是在处理组合关系、背景线索或指示表达时，导致编辑结果在语义上漂移或未能反映预期的更改。
### Innovation
我们提出了MIRA（Multimodal Iterative Reasoning Agent，多模态迭代推理代理），这是一种轻量级、即插即用的多模态推理代理，通过迭代感知-推理-行动循环执行编辑任务，有效地模拟了多轮人-模型交互过程。MIRA 不会一次性提供指令或静态计划，而是逐步预测原子编辑指令，并利用视觉反馈进行决策。通过结合包含150K多模态工具使用数据集MIRA-Editing和两阶段SFT + GRPO训练管道，MIRA 能够在复杂编辑指令上进行推理和编辑。与开源图像编辑模型Flux.1-Kontext、Step1X-Edit和Qwen-Image-Edit配对时，MIRA 显著提高了语义一致性并提升了感知质量，其性能与GPT-Image和Nano-Banana等专有系统相当或超越。
### Conclusion
MIRA 通过逐步预测编辑指令、利用视觉反馈和多模态训练数据集，显著提高了基于扩散的图像编辑模型在处理复杂指令时的语义一致性和感知质量，展示了其在图像编辑任务中的强大能力。
## 433. `cs.CV` - EM-KD: 利用不平衡视觉令牌精简高效的多模态大型语言模型 [PDF](https://arxiv.org/pdf/2511.21106), [HTML](https://arxiv.org/abs/2511.21106)
### Authors
Ze Feng,Sen Yang,Boqiang Duan,Wankou Yang,Jingdong Wang
### Background
高效的多模态大型语言模型（MLLMs）通过压缩视觉令牌来减少资源消耗，但这种做法可能导致视觉信息的丢失，进而影响理解能力。尽管有些方法引入了知识蒸馏以增强学生模型，但它们忽视了在高效学生模型和标准教师模型之间由不平衡视觉令牌造成的细粒度视觉理解差异。为了解决这个问题，该研究提出了EM-KD，一种新的知识蒸馏方法，通过曼哈顿距离和匈牙利匹配算法来调整视觉令牌，进而引入视觉-语言亲和力蒸馏和视觉语义蒸馏两种策略，以提高高效MLLMs的效果。
### Innovation
EM-KD提出了一种新的知识蒸馏方法，旨在解决由于视觉令牌不平衡导致的细粒度视觉理解差异问题。该方法首先通过曼哈顿距离和匈牙利匹配算法对视觉令牌进行对齐，然后应用视觉-语言亲和力蒸馏和视觉语义蒸馏两种策略，以提高学生模型的理解准确性和效率。
### Conclusion
EM-KD在多个基准测试上的综合评估表明，与之前的高效MLLMs相比，该方法在准确性和效率方面都取得了显著的提高，证明了其有效性。当与我们提议的视觉令牌匹配策略进行公平比较时，EM-KD也展示了更优的性能，优于之前的蒸馏方法。
## 434. `cs.CV` - 使用跨模态代理查询的引用视频对象分割 [PDF](https://arxiv.org/pdf/2511.21139), [HTML](https://arxiv.org/abs/2511.21139)
### Authors
Baoli Sun,Xinzhu Ma,Ning Wang,Zhihui Wang,Zhiyong Wang
### Background
RVOS是一项新兴的跨模态任务，旨在生成由给定文本表达式引用的目标对象的像素级分割图。传统的解决方法通过条件查询实现跨模态对齐，但存在跨帧依赖性和变异性建模不足，以及文本约束引入滞后的问题，导致难于对具有显著跨帧变化的目标对象进行准确追踪。
### Innovation
提出了一种名为ProxyFormer的新颖RVOS架构，引入了一组代理查询以整合视觉和文本语义，并促进两者之间语义交互的流动。通过在视频特征编码的多个阶段中逐步更新和传播代理查询，确保视频特征专注于目标对象。此外，将跨模态交互分离为时间维度和空间维度，设计了一种联合语义一致性（JSC）训练策略，以使代理查询与视频-文本对之间的语义共识保持一致。
### Conclusion
在四个广泛使用的RVOS基准测试上进行全面实验，展示了ProxyFormer在准确性和连贯性方面优于现有最先进的方法。
## 435. `cs.CV` - CtrlVDiff：通过统一多模态视频扩散生成可控制的视频 [PDF](https://arxiv.org/pdf/2511.21129), [HTML](https://arxiv.org/abs/2511.21129)
### Authors
Dianbing Xi,Jiepeng Wang,Yuanzhi Liang,Xi Qiu,Jialun Liu,Hao Pan,Yuchi Huo,Rui Wang,Haibin Huang,Chi Zhang,Xuelong Li
### Background
该研究旨在解决视频理解和可控视频生成的双重挑战，通过统一的扩散框架来联合处理这两种任务。研究表明，仅依赖几何线索（如深度、边缘）对于视频生成是不够的，因为这样的信息虽然能够提供场景布局，但不足以描述材料、照明等其他重要属性，这在物理层面上限制了多样性的编辑操作，如重新光线控（relighting）或材料置换，往往还会导致时间上的漂移。为了应对上述问题，研究引入了更丰富的反馈机制，将图像基础的模态（如内联要素与语义信息）作为辅助约束，并构建了一个能够结合这些多种模态并保持一致性的统一模型。然而，要同时整合多种异构模态数据，模型必须具备灵活接受任意类型模态、从缺失输入中强有力地恢复模态信息同时输出的时间一致性特征，这提出了在架构和数据方面的重要挑战。
### Innovation
该研究提出了一个名为CtrlVDiff的统一多模态视频扩散模型，该模型使用混合模态控制策略（HMCS）来路由和融合来自深度、法线、语义分割、边缘和形象基础内联要素（如反射率、金属性）的特征，并且能够从任意选择的模态生成具有强烈时间一致性的重新渲染视频。为了让这一模型成为现实，研究还构建了一个包含了多种模态和字幕相统一的混合真实-合成数据集MMVideo。相比现有的基础模型，CtrlVDiff在理解和生成基准测试中表现出更优秀的控制能力和精确度，能够支持层状编辑（包括重新光线控、材料调整、对象插入），并且具有当某些模态不可用时的稳健性。
### Conclusion
总之，CtrlVDiff通过对多种模态数据的融合和统一处理，成功解决了视频理解和生成的双重挑战，实现了对视频生成的高度控制和精确控制，展现了当前在该领域的最优表现。
## 436. `cs.CV` - DeepRFTv2: 图像去模糊中的核级学习 [PDF](https://arxiv.org/pdf/2511.21132), [HTML](https://arxiv.org/abs/2511.21132)
### Authors
Xintian Mao,Haofei Song,Yin-Nian Liu,Qingli Li,Yan Wang
### Background
已知为了学习如何去模糊，网络需要理解模糊过程。模糊自然是由清晰图像与模糊核的卷积造成的，因此允许网络在核级学习模糊过程能显著提高去模糊效果。然而，目前的深度网络仍处于像素级学习阶段，无论是端到端的像素级恢复还是阶段式的伪核级恢复，都无法使去模糊模型理解模糊的本质。
### Innovation
提出了一种Fourier Kernel Estimator (FKE)，它首先在Fourier空间中考虑激活操作，将空间域中的卷积问题转换为Fourier空间中的乘法问题。FKE与去模糊模型联合优化，使网络能够在低复杂度和无需额外监督的情况下学习核级模糊过程。此外，将核卷积对象从“图像”更改为网络提取的“特征”，这些特征包含丰富的语义和结构信息，更适合模糊过程的学习。通过将特征与估计核的卷积，模型可以学习模糊的核级本质。为了进一步提高特征提取的效率，设计了一种分耦合多尺度架构，包含多个层次子单元并采用可逆策略，这使模型可以在较低训练内存下实现更好的多尺度编码和解码。
### Conclusion
广泛的实验表明，我们的方法在运动去模糊结果方面达到了最先进的水平，并展示了处理其他相关核问题的潜力。分析结果还表明，我们的核估计器能够学习物理意义上具有意义的核。代码将在此处提供：this https URL。
## 437. `cs.CV` - 基于熵引导优先级渐进学习的人类视频生成高效训练 [PDF](https://arxiv.org/pdf/2511.21136), [HTML](https://arxiv.org/abs/2511.21136)
### Authors
Changlin Li,Jiawei Zhang,Shuhao Liu,Sihao Lin,Zeyi Shi,Zhihui Li,Xiaojun Chang
### Background
随着扩散模型的发展，人类视频生成取得了巨大的进步，但训练这些模型时需要处理高分辨率的多帧数据，这导致了高昂的计算成本和大量内存消耗的问题。
### Innovation
提出了基于熵引导优先级渐进学习（Ent-Prog）的高效训练框架，通过引入条件熵膨胀（CEI）评估不同模型组件的重要程度，并采用自适应渐进训练计划，在保持模型性能的同时，提高了训练速度并减少了GPU内存消耗。
### Conclusion
实验结果在三个数据集上得到了验证，表明Ent-Prog能够实现高达2.2倍的训练加速和2.4倍的GPU内存减少，同时不牺牲生成性能。
## 438. `cs.CV` - LLaVA-UHD v3: 进阶视觉压缩以实现 MLLMs 的高效原分辨率编码 [PDF](https://arxiv.org/pdf/2511.21150), [HTML](https://arxiv.org/abs/2511.21150)
### Authors
Shichu Sun,Yichen Zhang,Haolin Song,Zonghao Guo,Chi Chen,Yidan Zhang,Yuan Yao,Zhiyuan Liu,Maosong Sun
### Background
在多模态大型语言模型（MLLMs）中，视觉信息的编码通常采用编码器-解码器框架，其中视觉编码后跟随标记凝缩已成为标准架构范式。当前许多MLLMs倾向于使用全局原分辨率视觉编码，而较少采用切片方法。为了深入研究这一趋势，本研究系统比较了两种编码方式在视觉-语言理解任务和注意力模式上的行为，发现全局编码虽然增强了整体能力，但代价是计算开销更大。为解决这一问题，提出了一种分步视觉压缩（PVC）方法，并引入了LLaVA-UHD v3模型。
### Innovation
介绍了PVC方法，该方法由两个关键模块构成：（i）细化的补丁嵌入，支持灵活的补丁大小缩放以进行细粒度视觉建模，（ii）分窗标记压缩方法，在ViT层中逐级部署以逐阶聚合局部标记表示。通过这些模块的联合调节，可以在保持通用性的同时将广泛预训练的ViT重新配置为高效架构。引入的ViT-UHD在多个基准测试中展示了具有竞争力的表现，同时将TTFT减少了2.4倍。在此基础上，LLaVA-UHD v3进一步将TTFT减少1.9倍，实现了与Qwen2-VL相当的表现。
### Conclusion
本文展示了LLaVA-UHD v3模型及其背后的PVC方法，该方法能够在保持通用性的同时，通过可无缝集成到标准ViT中的分步视觉压缩实现高效的原分辨率编码。评估结果显示，该模型在减少计算时间的同时保持了与现有模型相当的性能，并且公开了所有代码和检查点以供未来研究。”订购格式需要精简为键值对，避免过长句子和复杂结构。解析格式如下所示：
## 439. `cs.CV` - 逐块进步：自回归图像生成的测试时缩放 [PDF](https://arxiv.org/pdf/2511.21185), [HTML](https://arxiv.org/abs/2511.21185)
### Authors
Joonhyung Park,Hyeongwon Jang,Joowon Kim,Eunho Yang
### Background
最近的视觉自回归(AR)模型在文本到图像生成任务中展现了良好的性能，类似大型语言模型的方式运行。现有表明测试时计算放大可以在大规模自然语言任务中通过增强推理来实现非凡的成功，但其应用于视觉AR模型尚未探索，且面临独特的挑战。简单的测试时放大策略如'最佳N'有可能不尽如人意，这会在错误的生成轨迹上耗费全部计算资源，而逐步扫描解码方案缺乏整幅画布的蓝图，限制了放大策略带来的益处。
### Innovation
我们引入了GridAR，这是一款用于视觉AR模型的测试时放大框架，采用网格分割的逐步生成方案，对于同位置生成多个部分候选，不切实际的候选早早被剔除，可行的候选作为锚点引导后续的解码。同时提出了一种布局指定的提示重述策略，基于部分视图推断出满足提示的可行布局，再由改写后的提示指导后续图像生成，以缓解缺乏整幅画布蓝图的问题。与'最佳N'策略相比，在N=4时，GridAR在T2I-CompBench++上提高了14.4%的生成质量的同时减少了25.6%的成本，并且还能应用于自回归图像编辑，在PIE-Bench上的语义保留度提升13.9%。
### Conclusion
GridAR在有限的测试时放大下实现了更高的生成质量：当N=4时，其优于N=8的'最佳N'14.4%，且成本降低。GridAR还展示了对自回归图像编辑的适用性，与更多的N值基线相比，在PIE-Bench上获得了13.9%的语义保留度提升。
## 440. `cs.CV` - 当机器人遵循标记：针对视觉-语言-动作模型的通用可转移贴片攻击 [PDF](https://arxiv.org/pdf/2511.21192), [HTML](https://arxiv.org/abs/2511.21192)
### Authors
Hui Lu,Yi Yu,Yiming Yang,Chenyu Yi,Qixin Zhang,Bingquan Shen,Alex C. Kot,Xudong Jiang
### Background
VLA模型容易受到对抗性攻击的影响，但通用和可转移的攻击仍未得到充分研究。现有方法大多针对单一模型过拟合，并且在黑盒环境中无效。
### Innovation
介绍了UPA-RFAS（通用贴片攻击通过稳健的特征、注意力和语义），这是一种统一框架，可以在共享特征空间中学习单一物理贴片，同时促进跨模型的转移。UPA-RFAS 结合了特征空间目标、L1偏差先验和排斥InfoNCE损失，以诱导可转移的表示转变；一种增强了鲁棒性的两阶段最小-最大过程，内层循环学习隐形的样本级扰动，外层循环优化该硬化邻域的通用贴片；以及两种针对VLA的特异性损失，分别是标记注意力主导和标记语义不匹配。
### Conclusion
实验证明UPA-RFAS在多种VLA模型、操纵套件和物理执行中都能跨模型、任务和视角进行转移，揭示了基于贴片的实用攻击面，并为未来的防御建立了强大的基准。
## 441. `cs.CV` - 您可以通过一个无参自我增强插件信任您的聚类模型：用于深度聚类的一种参数自由方法 [PDF](https://arxiv.org/pdf/2511.21193), [HTML](https://arxiv.org/abs/2511.21193)
### Authors
Hanyang Li,Yuheng Jia,Hui Liu,Junhui Hou
### Background
近年来，深度聚类模型在聚类性能方面取得了显著进步。然而，现有方法普遍存在的问题是局部和全局特征结构之间的不一致性。局部特征内部样本通常表现出较强的连续性和紧凑性，而全局特征则常出现交织边界和不清晰的聚类。
### Innovation
本文提出了一种无参插件DCBoost，旨在增强现有深度聚类模型的全局特征结构。该方法利用可靠的地方结构线索，首先通过自适应的k-最近邻一致性筛选识别高置信度样本，然后利用这些样本计算辨别损失，促进类内紧凑性和类间可分性，优化网络。
### Conclusion
在多个基准数据集中进行了广泛的实验，证明了DCBoost能够显著提高现有深度聚类模型的聚类性能。相对于当前的最优基线（例如ProPos），我们的方法能提高3%以上的性能，并将轮廓系数提高到原来的7倍以上。代码已开源。
## 442. `cs.CV` - TEAR: Temporal-aware Automated Red-teaming for Text-to-Video Models [PDF](https://arxiv.org/pdf/2511.21145), [HTML](https://arxiv.org/abs/2511.21145)
### Authors
Jiaming He,Guanyu Hou,Hongwei Li,Zhicong Huang,Kangjie Chen,Yi Yu,Wenbo Jiang,Guowen Xu,Tianwei Zhang
### Background
Text-to-Video (T2V) 模型能够合成高质量、时序一致的动态视频内容，但这种多样化的生成也固有地引入了关键的安全挑战。现有的安全评估方法集中在静态图像和文本生成，无法捕捉视频生成中的复杂时序动态。
### Innovation
提出了一个名为TEAR的时间感知自动化红队框架，这是一个设计用于揭示特定于 T2V 模型动态时序序列的安全风险的自动化框架。TEAR 使用通过两阶段方法（初始生成器训练和时间感知在线偏好学习）优化的时间感知测试生成器，来精心制作文本上无害的提示，从而利用时序动态触发政策违反的视频输出。并采用改进模型以周期性地提高提示的隐藏性和对抗有效性。
### Conclusion
广泛的实验评估表明，TEAR 在开源和商用 T2V 系统中的有效性，攻击成功率超过 80%，比之前的最好结果提升了显著的百分比，即从 57% 提升。
## 443. `cs.CV` - AnchorOPT：优化动态锚点以实现适应性提示学习 [PDF](https://arxiv.org/pdf/2511.21188), [HTML](https://arxiv.org/abs/2511.21188)
### Authors
Zheng Li,Yibing Song,Xin Zhang,Lei Luo,Xiang Li,Jian Yang
### Background
现有的基于CLIP模型的提示学习方法使用文本标记作为锚点来引导可学习的软标记，这种引导可以改善CLIP的泛化能力。但是，这些锚点在价值和位置上是静态的，缺乏跨任务和跨阶段的适应性灵活性。
### Innovation
提出了一种动态锚点基于的提示学习框架AnchorOPT，引入了锚点和位置关系两个维度的动态性：一是锚点的值从任务特定数据中动态学习，而非手工设计的明确文本标记；二是锚点与软标记之间的相对位置不再是固定的，而是通过训练阶段和任务上下文条件下的可学习位置矩阵进行适应性优化。
### Conclusion
大量实验表明，仅使用简单的可学习锚点和位置矩阵就能达到或超过包含额外可学习模块或正则化技术的方法的性能。作为可插拔模块，AnchorOPT无缝集成到现有框架中，可以在多种数据集上实现一致的性能提升。源代码已公开。
## 444. `cs.CV` - BotaCLIP：用于地球观测数据植物意识表示的对比学习 [PDF](https://arxiv.org/pdf/2511.21194), [HTML](https://arxiv.org/abs/2511.21194)
### Authors
Selene Cerna,Sara Si-Moussi,Wilfried Thuiller,Hadrien Hendrikx,Vincent Miele
### Background
基础模型在图像、文本和音频等多种模态中展示了学习丰富可传输表示的强大能力。在现代机器学习管道中，这些表示经常取代原始数据作为下游任务的主要输入。然而，如何在不重新训练或产生显著计算开销的情况下，根据具体领域知识对预训练的基础模型进行适应，是当前面临的一大挑战。
### Innovation
本文提出了BotaCLIP，一种轻量级的多模态对比学习框架，通过对比学习策略将高分辨率航空影像与植物群落数据对齐，以适应预训练的地球观测基础模型（DOFA）。与通用嵌入相比，BotaCLIP通过正则化策略内部化生态结构，防止灾难性遗忘。在植物存在预测、蝴蝶分布建模和土壤营养级群集丰度估计三种生态任务中，BotaCLIP的表现优于DOFA和监督基线，展示了基础模型领域感知适应性的潜力，可以将专家知识注入数据稀缺环境，促进节俭的表示学习。
### Conclusion
该研究展示了基础模型领域导向适应方法的有效性，证明了在数据稀缺的场景中，可以通过这种方式注入专家知识，并实现有效的表示学习，从而在实际应用中提升生态建模能力。
## 445. `cs.CV` - Fine-grained 视频动作识别的有效动作-区域跟踪框架 [PDF](https://arxiv.org/pdf/2511.21202), [HTML](https://arxiv.org/abs/2511.21202)
### Authors
Baoli Sun,Yihan Wang,Xinzhu Ma,Zhihui Wang,Kun Lu,Zhiyong Wang
### Background
细粒度动作识别（FGAR）旨在识别精细动作类别之间的微妙且明显的差异。然而，现有的识别方法通常捕捉到粗粒度的动作模式，但难以识别随时间演变的局部区域中的微妙细节。
### Innovation
本文引入了动作-区域跟踪（ART）框架，这是一种利用查询-响应机制来发现并跟踪具有代表性的局部细节动态的新方案，从而有效地区分相似的动作。具体来说，提出了一个区域特定的语义激活模块，该模块使用区分性和文本约束性的语义作为查询，以在每个视频帧中捕捉与动作最相关的区域响应，促进空间和时间维度之间的交互。捕获的区域响应被组织成动作标记片段，可以描述基于区域的动作动态，通过在视频帧之间的连贯序列中链接相关响应来实现。文本约束查询将从视觉语言模型（VLMs）的语言分支中提取的动作标签文本描述产生的精微语义表示编码。为优化动作标记片段，设计了在空间和时间层面上的多级标记对比约束，这有助于在每个帧内的有效区分以及相邻帧之间的相关性。此外，一种特定任务的微调机制精炼了文本语义，使得由VLMs编码的语义表示被保留并优化以满足任务偏好。
### Conclusion
广泛的实验在广泛使用的动作识别基准上展示了该方法比之前最先进的基线方法的优越性。
## 446. `cs.CV` - FIELDS: 使用直接监督进行准确表情推断的脸部重建 [PDF](https://arxiv.org/pdf/2511.21245), [HTML](https://arxiv.org/abs/2511.21245)
### Authors
Chen Ling,Henglin Shi,Hedvig Kjellström
### Background
面部表情在人类交流中传达了大量的情感信息，但现有的3D面部重建方法往往由于依赖2D监督和缺乏3D真实数据而遗漏了微妙的情感细节。
### Innovation
提出了Fields（FACE Reconstruction with accurate Inference of Expression using Learning with Direct Supervision），通过拓展自我监督的2D图像一致性线索，并结合直接的3D表情参数监督以及辅助的情感识别分支来解决这些限制问题。编码器由真实的表情参数引导，同时情感强度意识损失促使3D表情参数捕捉真正的表情内容而不夸张。双监督策略缩小了2D/3D领域差距，减轻了表情强度偏差，生成高保真的3D重建，保留了微妙的情感线索。
### Conclusion
从单个图像中，Fields生成富含情感的脸部模型，具有高度真实的表情，显著提高了野生面部表情识别性能，同时保持了自然性。
## 447. `cs.CV` - 场景即令牌：用于通用3D视觉-语言理解的多尺度正态分布变换 tokenizer [PDF](https://arxiv.org/pdf/2511.21191), [HTML](https://arxiv.org/abs/2511.21191)
### Authors
Yutao Tang,Cheng Zhao,Gaurav Mittal,Rohith Kukkala,Rama Chellappa,Cheng Peng,Mei Chen
### Background
近期，3D 视觉-语言模型（VLMs）在3D场景理解与推理方面显示出巨大的潜力，但有效将3D场景整体化为场景令牌，并在多种3D理解任务中利用这些令牌，仍然是一个高度挑战性的任务。
### Innovation
本研究提出了NDTokenizer3D，一种通用的3D VLM，它能够执行广泛的3D场景理解任务，并自然支持人类互动。这种新型方法的核心是一个基于多尺度正态分布变换（NDT）表示的三级场景标记流水线，以及多尺度NDT解码器（MSDec）。NDTokenizer3D能够从原始高分辨率点云构建多尺度NDT表示，同时保留全局上下文和几何细节，多尺度NDT解码器逐步融合跨尺度特征，生成可被大型语言模型（LLM）端点消耗的整体场景令牌。此外，MSDec还被重新用于人类互动提示（如点、框、掩码）和分割掩码解码，从而在同一架构中统一了多种3D场景理解任务。
### Conclusion
通过这种紧凑而统一的设计，NDTokenizer3D 成为一种细粒度、用途广泛的3D VLM，显著提高了3D 参照分割、3D视觉问答和3D密集标注等多个领域的性能。
## 448. `cs.CV` - PathMamba：用于卫星影像中拓扑连贯的道路分割的混合Mamba-Transformer [PDF](https://arxiv.org/pdf/2511.21298), [HTML](https://arxiv.org/abs/2511.21298)
### Authors
Jules Decaestecker,Nicolas Vigne
### Background
道路分割在城市规划和灾害响应等领域具有重要意义。现有的方法依赖于Vision Transformers，尽管它们擅长捕捉全局上下文，但其计算复杂性较高，不适合在资源受限的平台上高效部署。相比之下，新兴的Mamba时间空间模型提供了线性时间效率，并且非常适合建模长且连续的结构。因此，该领域需要一种融合这两种架构的方法。
### Innovation
本文提出了一种新的混合架构PathMamba，结合了Mamba模型的顺序建模特性和Transformer模型的全局推理能力。通过战略性地使用Mamba块来跟踪道路网络的连续性，并结合Transformer块提升带有全球上下文的功能，以实现拓扑结构更好的分割结果。与纯注意力模型相比，该方法在计算成本上更具竞争力。
### Conclusion
在DeepGlobe Road Extraction和Massachusetts Roads数据集上的实验表明，PathMamba达到了新的最先进的性能。特别地，它显著提高了拓扑连续性，达到了新的基准，并且在计算性能上保持竞争力。
## 449. `cs.CV` - 3-Tracer: 一种针对音频篡改检测和定位的三层次时间感知框架 [PDF](https://arxiv.org/pdf/2511.21237), [HTML](https://arxiv.org/abs/2511.21237)
### Authors
Shuhan Xia,Xuannan Liu,Xing Cui,Peipei Li
### Background
近年来，部分音频篡改已经成为一种新的音频操控形式。攻击者有选择性地修改关键帧，同时保持整体听觉真实感，这使得这类篡改特别难以被检测。现有方法通常独立检测单个帧是否被篡改，缺乏捕捉不同时间层次上瞬态和持续性异常的层次结构。
### Innovation
为了弥补这些不足，我们识别出对部分音频篡改检测至关重要的三个关键层次，并提出了T3-Tracer，这是首个同时在帧、片段和音频层次上分析音频以全面检测篡改痕迹的框架。T3-Tracer 包含两个互补的核心模块：帧-音频特征聚合模块 (FA-FAM) 和片段层次多尺度差异感知模块 (SMDAM)。FA-FAM 设计用于检测每帧音频的真实性，通过结合帧级和音频级的时间信息来检测帧内篡改线索和全局语义不一致。为了进一步细化和修正帧检测结果，我们提出了 SMDAM，用于在片段层次上检测篡改边界。它采用双分支架构，联合建模跨多尺度时间窗口的帧特征和帧间差异，有效地识别出篡改边界上突然出现的异常。
### Conclusion
在三个具有挑战性的数据集上进行的大量实验表明，我们的方法达到了最先进的性能。
## 450. `cs.CV` - CaliTex: 用于视图一致3D纹理生成的几何校准注意力 [PDF](https://arxiv.org/pdf/2511.21309), [HTML](https://arxiv.org/abs/2511.21309)
### Authors
Chenyu Liu,Hongze Chen,Jingzhi Bao,Lingting Zhu,Runze Zhang,Weikai Chen,Zeyu Hu,Yingda Yin,Keyang Luo,Xin Wang
### Background
尽管基于扩散的模型带来了重大进展，当前3D纹理生成系统仍然受到跨视角不一致的困扰——从一个视角看显得真实的纹理在其他视角下往往无法对齐。我们发现这个问题源于注意力的不确定性，即无结构的全注意力在不同标记和模态间无差别地应用，导致几何混淆和外观-结构耦合的不稳定。
### Innovation
我们引入了CaliTex，一种几何校准注意力框架，明确地将注意力与3D结构对齐。它包括两个模块：部分对齐注意力，强制在语义匹配的部分间的空间对齐；条件导向注意力，通过几何条件的路径传递外观信息以保持空间保真度。结合一个两阶段的扩散转换器，CaliTex使几何连贯行为成为网络的固有行为，而不是优化的副产品。
### Conclusion
实验证明，CaliTex生成无缝且视图一致的纹理并优于开源和商业基准系统。
## 451. `cs.CV` - HTTM: 预训练即插即用的头部级时序 token 融合加速 VGGT [PDF](https://arxiv.org/pdf/2511.21317), [HTML](https://arxiv.org/abs/2511.21317)
### Authors
Weitian Wang,Lukas Meiner,Rai Shubham,Cecilia De La Parra,Akash Kumar
### Background
VGGT 算法在 3D 场景重建中取得了重大突破，它能够直接在一次推理过程中联合推断所有关键的 3D 属性（相机姿态、深度和密集几何）。然而，这种联合推断机制需要进行全局注意力计算，导致了显著的延时瓶颈，尤其是对于大型场景和长序列输入的重建。
### Innovation
本文提出了一种训练无需的 3D token 融合方法，称作头部级时序 token 融合 (HTTM)，用于加速 VGGT 重建框架。HTTM 在每个注意力头的粒度上对 token 进行合并，保留了头部拼接后的特征 token 的独特性。此外，它利用了头部级别的空间局部性和时间对应关系，与现有的方法相比，能以较低的融合成本实现更高的合并率。经过针对 GPU 基础推理的测试，HTTM 实现了最高 7 倍的加速，且几乎不影响性能。
### Conclusion
HTTM 方法能够大幅加速 VGGT 模型的推理过程，最高达到 7 倍的加速，同时保持了模型的性能几乎不变，且无需额外训练。
## 452. `cs.CV` - 基于高斯点扩散的零样本潜在能力解锁对稀疏图像匹配 [PDF](https://arxiv.org/pdf/2511.21265), [HTML](https://arxiv.org/abs/2511.21265)
### Authors
Juncheng Chen,Chao Xu,Yanjun Cao
### Background
基于学习的图像匹配依赖于大规模、多样且几何准确的训练数据。3D 高斯点扩散（3DGS）能够生成逼真的新视角合成图像，因此适用于数据生成。然而，3DGS 由于其几何不准确性和偏差深度渲染无法实现稳健的对应标定。
### Innovation
本文引入了 MatchGS，这是第一个旨在系统地纠正和利用 3DGS 的框架，以实现稳健的零样本图像匹配。该方法包括两部分：1) 一个几何忠实的数据生成管道，可以提升 3DGS 的几何精度，从而生成非常精细的对应标注，同时保持渲染精度；2) 一种从 2D 到 3D 的表示对齐策略，将 3DGS 显式的 3D 知识注入至 2D 匹配器，以引导 2D 的半密集匹配器学习与视角无关的 3D 表征。
### Conclusion
通过我们的数据生成，所生成的真实对应关系使得epipolar误差下降了40倍，支持了极端视角的变化，并提供了基于高斯属性的自我监督信号。基于我们数据集训练的当前最先进的匹配器在公共基准上的零样本性能提升到了最高17.7%。本文的成果表明，只有经过适当几何校正的 3DGS 可以成为一个可扩展且具备高保真和结构丰富的数据来源，为新一代的稳健零样本图像匹配器铺平了道路。
## 453. `cs.CV` - SurgMLLMBench: 用于手术场景理解的大规模多模态语言模型基准数据集 [PDF](https://arxiv.org/pdf/2511.21339), [HTML](https://arxiv.org/abs/2511.21339)
### Authors
Tae-Min Choi,Tae Kyeong Jeong,Garam Kim,Jaemin Lee,Yeongyoon Koh,In Cheul Choi,Jae-Ho Chung,Jong Woong Park,Juyoun Park
### Background
近年来，多模态大型语言模型（LLMs）在医疗和手术应用中展现出巨大潜力。然而，现有的手术数据集主要采用视觉问答（VQA）格式，具有多样化分类，缺乏像素级分割的支持，这限制了其一致性的评估和应用。
### Innovation
本研究提出了SurgMLLMBench，一个专门用于开发和评估互动多模态LLM以理解手术场景的统一多模态基准。该平台结合了像素级器械分割掩码和手术领域（腹腔镜、机器人辅助和显微手术）结构化的VQA注释，统一分类，能够超越传统VQA任务，进行更全面的评估和更丰富的视觉-对话互动。基线实验表明，单个模型在SurgMLLMBench上训练后能在不同领域实现一致性能，并对未见过的数据集进行了有效的泛化。
### Conclusion
SurgMLLMBench作为一个开源资源，将推动多模态手术AI研究的发展，支持可重复的评估和互动手术推理模型的开发。
## 454. `cs.CV` - AVFakeBench: 音频-视频伪造检测基准数据集，针对AV-LMMs [PDF](https://arxiv.org/pdf/2511.21251), [HTML](https://arxiv.org/abs/2511.21251)
### Authors
Shuhan Xia,Peipei Li,Xuannan Liu,Dongsen Zhang,Xinyu Guo,Zekun Li
### Background
当前音频-视频（AV）伪造手段正在迅速演变，不仅限于基于深度学习的人类针对伪造，而是扩展到复杂的自然场景下的多样的伪造。然而，现有的基准数据集仍然局限于基于深度伪造的方法，并且只有单一粒度的标注，无法全面捕捉现实世界伪造场景的多样性与复杂性。
### Innovation
本文引入了AVFakeBench，这是第一个综合的音频-视频伪造检测基准数据集，涵盖了丰富的伪造语义，包括人类和一般对象的伪造。AVFakeBench包含12000个精心策划的音频-视频样本，覆盖七种伪造类型和四种标注级别。此外，通过一个多阶段混合伪造框架，结合私有模型的任务规划和专家生成模型的精确篡改，确保了高质量的多样伪造样本。基准数据集提出了一个包含二元判断、伪造类型分类、伪造细节选择和解释推理的多任务评估框架。
### Conclusion
我们对11个音频-视频大型语言模型（AV-LMMs）和2种主流检测方法在AVFakeBench上的评估表明，AV-LMMs具有作为新兴伪造检测器的潜力，但它们在精细感知和推理方面的表现依然存在问题。
## 455. `cs.CV` - 移位等变复值卷积神经网络 [PDF](https://arxiv.org/pdf/2511.21250), [HTML](https://arxiv.org/abs/2511.21250)
### Authors
Quentin Gabot,Teck-Yian Lim,Jérémy Fix,Joana Frontera-Pons,Chengfang Ren,Jean-Philippe Ovarlez
### Background
卷积神经网络近年来在计算机视觉问题上表现出色。传统卷积神经网络缺乏关键的移位等变性和移位不变性，这受到下采样和上采样操作的破坏。尽管数据增强技术可以帮助模型在一定程度上学习这些特性，但通过设计构建可理论保证这些特性的下采样和上采样层，提供了一种系统和一致的方法。Adaptive Polyphase Sampling引入了移位不变性的基础，随后Learnable Polyphase up/downsampling应用于实值神经网络中实现了移位等变性。
### Innovation
本文将LPS工作扩展到了复值神经网络，从理论角度进行了研究，并引入了一种新的投影层，将$boldsymbol{textbf{C}}$映射到$boldsymbol{textbf{R}}$，应用在Gumbel Softmax之前。通过这种扩展，研究了复值卷积神经网络在分类任务中保持属性以及重建和语义分割任务中等变属性的应用，并使用极化合成孔径雷达图像进行了评估。
### Conclusion
复值卷积神经网络被应用于多种计算机视觉问题，包括分类任务中的不变性属性以及重建和语义分割任务中的等变属性，证明了这种复值模型的有效性。
## 456. `cs.CV` - 多任务学习中联合训练视觉语言模型以应对遥感任务 [PDF](https://arxiv.org/pdf/2511.21272), [HTML](https://arxiv.org/abs/2511.21272)
### Authors
Qingyun Li,Shuran Ma,Junwei Luo,Yi Yu,Yue Zhou,Fengxiang Wang,Xudong Lu,Xiaoxing Wang,Xin He,Yushi Chen,Xue Yang,Junchi Yan
### Background
随着Transformer在单任务遥感任务中取得卓越表现，多任务学习（MTL）正推动统一模型在多种任务间的卓越表现。视觉语言模型（VLMs）在遥感图像理解、语义分割和超高清图像推理方面取得了积极的结果。一个统一的基于文本的接口可以显著提高多任务学习的潜力。本文旨在实现这些成果以推动遥感多任务学习的发展。
### Innovation
本文提出了RSCoVLM，一种简单且灵活的VLM基本模型用于遥感多任务学习。它包括一个数据管理引擎支持数据的获取、离线处理、整合和在线加载与加权，以及一种统一的动态分辨率策略来解决遥感图像中多样化的图像尺度问题。此外，引入了一种Zoom-in Chain机制及其相应的LRS-VQA-Zoom数据集。研究还提出了一种新的评价标准，以确保视觉语言模型与传统检测模型的公平比较。实验结果表明，RSCoVLM在不同任务中达到了最先进的性能。
### Conclusion
RSCoVLM作为一种先进的视听模型，可以有效解决多任务遥感学习中的复杂问题，证明了其在多种任务中的优越性能。所有模型权重、工具和数据集均已开源，以支持可重复性研究。我们相信该基础可以促进更通用的遥感模型的发展。
## 457. `cs.CV` - LaGen: 向自动回归LiDAR场景生成迈进 [PDF](https://arxiv.org/pdf/2511.21256), [HTML](https://arxiv.org/abs/2511.21256)
### Authors
Sizhuo Zhou,Xiaosong Jia,Fanrui Zhang,Junjie Li,Juyong Zhang,Yukang Feng,Jianwen Sun,Songbur Wong,Junqi You,Junchi Yan
### Background
自动生成世界模型在自动驾驶（AD）中成为热门话题，与广泛研究的图像模态相比，这项工作探索了LiDAR数据的自动生成世界模型。现有的LiDAR数据生成方法仅支持单帧生成，而现有的预测方法需要多帧历史输入，并且只能一次性确定性地预测多帧，缺乏互动性。这两种方法都未能支持长时间互动生成。
### Innovation
提出了LaGen，这是已知的第一个能够进行长时距LiDAR场景逐帧自回归生成的框架。LaGen能够将单一帧LiDAR输入作为起点，并有效利用边界框信息作为条件以生成高保真度的4D场景点云。此外，引入了场景解耦估计模块以增强模型在对象级内容上的互动生成能力，以及噪声调制模块以减轻长时间生成过程中的误差累积。
### Conclusion
基于nuScenes构建了用于评估长时距LiDAR场景生成的协议。实验结果全面证明了LaGen在LiDAR生成和预测模型中表现优异，尤其是在后续帧上的表现更为出色。
## 458. `cs.CV` - 从扩散到一步生成：基于流模型的比较研究及其在图像修复中的应用 [PDF](https://arxiv.org/pdf/2511.21215), [HTML](https://arxiv.org/abs/2511.21215)
### Authors
Umang Agarwal,Rudraksh Sangore,Sumit Laddha
### Background
论文对三种生成建模范式——去噪扩散概率模型（DDPM）、条件流匹配（CFM）和MeanFlow——进行了全面的比较研究。介绍了CFM和DDPM需要迭代采样，而MeanFlow可以通过模拟时间间隔内的平均速度实现一步生成。
### Innovation
提出并实施了一致的小型 TinyUNet 架构来实现三种方法，展示了CFM在CIFAR-10上优于DDPM的生成效果，同时MeanFlow实现了单步采样的高效生成。进一步将CFM扩展到图像修复任务，提出指导采样的方法，并展示了有效的图像修复效果。
### Conclusion
CFM在CIFAR-10上的FID为24.15，比DDPM（FID为402.98）显著表现更佳。MeanFlow实现了单步采样的生成结果，减少了50倍的推理时间。此外，提出的混合掩码指导的图像修复模型在中心掩码下的PSNR和SSIM分别提高了73%和45%，显示了混合掩码指导下训练的有效性。
## 459. `cs.CV` - 基于SIFT-SNN的交通流控制基础设施高效异常检测 [PDF](https://arxiv.org/pdf/2511.21337), [HTML](https://arxiv.org/abs/2511.21337)
### Authors
Munish Rathee(School of Engineering, Computer and Mathematical Science (of Auckland University of Technology) Auckland, New Zealand),Boris Bačić(School of Engineering, Computer and Mathematical Science (of Auckland University of Technology) Institute of Biomedical Technologies (IBTec) Auckland, New Zealand),Maryam Doborjeh(Knowledge Engineering and Discovery Research Institute (KEDRI) (of Auckland University of Technology) Auckland, New Zealand)
### Background
本文旨在提出一种低延迟的类脑信号处理管道，名为SIFT-SNN框架，用于运输基础设施中的实时结构异常检测。该框架结合了尺度不变特征变换（SIFT）的空间特征编码、基于延迟的尖峰转换层以及耗电泄漏整流器（LIF）忆脾气态神经网络（SNN）以实现分类。该论文使用新西兰奥克兰海港大桥在不同天气和光照条件下记录的数据集进行验证，包括6000帧已标记的图像，其中包含真实的和合成增强的不安全情况。
### Innovation
本文的主要创新包括：1) 结合SIFT用于空间特征编码。2) 利用基于延迟的尖峰转换层和LIF SNN进行分类。3) 实现了亚10毫秒的低延迟和稀疏尖峰活动，使系统能够在边缘进行实时低功耗部署。4) SIFT-SNN管道混合使用了SIFT和SNN，更加准确地保留了空间特征，并且提高了解释性，支持透明决策过程，在嵌入式硬件上也能高效运行。虽然合成增强提高了系统的鲁棒性，但其对未见过的实际条件的泛化能力仍需验证。
### Conclusion
SIFT-SNN框架通过在消费级系统上的工作原型得到验证，并被用作可推广的案例研究，用以监控全球20多个城市的移动混凝土障碍物结构安全性。作为一种交通流量控制基础设施，这种框架能实时检测出结构异常，确保交通安全。
## 460. `cs.CV` - 越多越好：用于更高阶多模态对齐的对比融合 [PDF](https://arxiv.org/pdf/2511.21331), [HTML](https://arxiv.org/abs/2511.21331)
### Authors
Stefanos Koutoupis,Michaela Areti Zervou,Konstantinos Kontras,Maarten De Vos,Panagiotis Tsakalides,Grigorios Tsagatakis
### Background
多模态机器学习领域的一个核心挑战是如何在多个模态之间学习联合表示。现有的方法主要在成对设置中运作，一次对齐两组模态。尽管一些最近的方法试图捕获多个模态之间的高阶交互作用，但它们往往忽略了或未能充分保留两两之间的关系，这限制了其在单一模态任务上的有效性。
### Innovation
本文提出了对比融合（ConFu）框架，这种框架可以同时嵌入个体模态及其融合后的组合，使其在统一的空间中对齐。ConFu扩展了传统的成对对比目标，增加了额外的融合模态对比项，鼓励将两个模态与第三个模态一起进行联合嵌入。这种框架能够捕获由仅有成对对齐得不到的更高阶的依赖关系，如异或关系，同时保持强大的成对对应关系。
### Conclusion
在合成和真实世界多模态基准上评估了ConFu，发现其在检索和分类任务中表现出竞争性的性能，同时支持在单一对比框架内的统一一对一和一对二检索。
## 461. `cs.CV` - Endo-G$^{2}$T: 几何导向且时间感知的嵌入式4D高斯分布对于内镜场景 [PDF](https://arxiv.org/pdf/2511.21367), [HTML](https://arxiv.org/abs/2511.21367)
### Authors
Yangle Liu,Fengze Li,Kan Liu,Jieming Ma
### Background
内镜视频表现出强视点依赖效果，如镜面反射、湿反射和遮挡。纯 photometric 监督与几何结构不一致，导致早期几何叠加，错误的形状在稠密化过程中得以强化，变得难以矫正。因此，如何在动态内镜场景中早期锚定几何结构并同时保持时间一致性和效率成为一个需要解决的问题。
### Innovation
本文提出了 Endo-G$^{2}$T，一种几何导向且时间感知的嵌入式4D高斯分布训练方案，用于时间嵌入的4DGS。通过使用几何引导先验提炼将单目深度转化为尺度不变的深度及深度梯度监督，同时采用温启动至饱和调度以软性注入先验并避免早期过拟合。通过使用旋转参数化的时间嵌入高斯场来表示XYZT中的动态，提供轻量级正则化以促进平滑运动和清晰的透明度边界。通过关键帧约束流使得在点预算下的关键帧优化提高了效率和长历时稳定性。
### Conclusion
在 EndoNeRF 和 StereoMIS-P1 数据集中，Endo-G$^{2}$T 在单目重建基准中实现了最先进的结果。
## 462. `cs.CV` - 测试时计算量对视觉语言模型推理的影响：一种以干扰为中心的经验分析 [PDF](https://arxiv.org/pdf/2511.21397), [HTML](https://arxiv.org/abs/2511.21397)
### Authors
Jiyun Bae,Hyunjong Ok,Sangwoo Mo,Jaeho Lee
### Background
先前对语言模型的研究表明，文本干扰会导致推理延迟但效果不佳。本文探讨了类似现象在多模态设置中是否会出现。
### Innovation
引入了含有文本和视觉干扰的视觉问答数据集Idis，并从语义、数值和空间三个维度系统地变化干扰。通过分析发现，视觉干扰和文本干扰在效应上存在根本差异：尽管存在逆向缩放现象，但增加视觉干扰会降低准确性而不增加推理时间。
### Conclusion
这些趋势也扩展到诸如Waterbirds这样的视觉偏见基准上。本文提出了一种简单的提示策略来减轻推理模型中由偏见驱动的预测。
## 463. `cs.CV` - E-M3RF: 等变多模态3D复原框架 [PDF](https://arxiv.org/pdf/2511.21422), [HTML](https://arxiv.org/abs/2511.21422)
### Authors
Adeela Islam,Stefano Fiorini,Manuel Lecha,Theodore Tsesmelis,Stuart James,Pietro Morerio,Alessio Del Bue
### Background
3D复原是一个基本的几何问题，在近年来越来越依赖深度学习方法而非传统的优化方法。尽管学习方法取得了有希望的结果，大多数方法仍然主要依靠几何特征来组装零件，导致在几何特征不足以或不明确时方法面临挑战，如对小的、侵蚀的或对称的碎片组装困难，且这些解决方案没有明确的物理约束来防止重叠组装。
### Innovation
我们提出了E-M3RF(等变多模态3D复原框架)，该框架可以作为输入包含点云的点的位置和颜色的断裂碎片，并使用SE(3)流匹配预测重新组装所需的变换。每个碎片被表示为几何和色彩特征：i) 3D点的位置通过旋转一致的几何特征编码来编码，利用旋转等变编码器；ii) 每个3D点的颜色使用变压器进行编码。这两个特征集合组合形成一个多模态表示。实验结果表明，E-M3RF在RelAIR数据集上的旋转误差减少了23.1%，平移误差减少了13.2%，亥维赛距离减少了18.4%，相较于竞争方法表现出更好的性能。
### Conclusion
E-M3RF框架通过结合几何和色彩特征，以及应用SE(3)流匹配，能有效提升3D复原的准确性和鲁棒性，尤其在几何特征不充分或不明确时有更好的表现。
## 464. `cs.CV` - EvRainDrop: 通过超图引导的完成有效帧和事件流聚合 [PDF](https://arxiv.org/pdf/2511.21439), [HTML](https://arxiv.org/abs/2511.21439)
### Authors
Futian Wang,Fan Zhang,Xiao Wang,Mengqi Wang,Dexing Huang,Jin Tang
### Background
事件摄像机生成异步事件流，这些流在空间上稀疏但在时间上密集。现有的主流事件表示学习算法通常将事件帧、体素或张量作为输入。虽然这些方法取得了显著的进展，但它们在解决由空间稀疏性引起的欠采样问题方面表现不佳。
### Innovation
本文提出了一种新颖的超图引导的空间时间事件流完成机制。该机制通过超图连接不同时间和空间位置的事件标记，并利用上下文信息消息传递来完成这些稀疏的事件。该方法可以在完成框架中灵活地将RGB标记作为超图节点，从而实现多模态超图信息完成。随后，通过自我注意将不同时间步骤的超图节点信息进行聚合，从而实现有效的多模态特征学习和融合。
### Conclusion
本文在单一和多标签事件分类任务上的大量实验充分验证了所提出框架的有效性。
## 465. `cs.CV` - SAM Guided Semantic and Motion Changed Region Mining for Remote Sensing Change Captioning [PDF](https://arxiv.org/pdf/2511.21420), [HTML](https://arxiv.org/abs/2511.21420)
### Authors
Futian Wang,Mengqi Wang,Xiao Wang,Haowen Wang,Jin Tang
### Background
遥感图像变化描述是近年来一个新兴且流行的研究任务，旨在通过自然语言描述不同时期所捕获的遥感图像中的变化内容。现有方法通常使用CNNs/Transformer从给定图像提取视觉表示或引入辅助任务以增强最终结果，但缺点是缺乏区域意识且不能很好地进行时间对齐。
### Innovation
本文探索使用SAM（Segment Anything Model）基础模型提取区域级表示，并将区域兴趣知识注入描述框架中。具体而言，使用CNN/Transformer模型提取全局视觉特征，利用SAM基础模型细分语义和运动变化区域，并通过特别构建的知识图提供关于感兴趣对象的信息。将这些不同来源的信息通过交叉注意力进行融合，并使用Transformer解码器生成最终的自然语言描述。
### Conclusion
在多个广泛使用的基准数据集上进行了详尽的实验结果，表明本文方法在变化描述方面达到了最新的性能。代码将会在此发布：https://github.com/example/sam-guided-change-captioning
## 466. `cs.CV` - Monet: 在图像和语言之外的潜在视觉空间推理 [PDF](https://arxiv.org/pdf/2511.21395), [HTML](https://arxiv.org/abs/2511.21395)
### Authors
Qixun Wang,Yang Shi,Yifei Wang,Yuanxing Zhang,Pengfei Wan,Kun Gai,Xianghua Ying,Yisen Wang
### Background
图像思维在推进视觉推理方面表现出色，超越了仅使用文本的思维链，引入了视觉证据。然而，现有方法在灵活性上仍然受到外部工具的限制，不能达到人类的抽象视觉思考。训练多模态大型语言模型进行潜在视觉推理面临两个核心挑战：潜在视觉对齐的高计算成本和对潜在嵌入的不足监督。
### Innovation
引入了Monet训练框架，通过生成连续嵌入来让多模态大型语言模型直接在潜在视觉空间中进行推理。提出了基于三阶段蒸馏的监督微调（SFT）管道以解决潜在视觉对齐的高计算成本和对潜在嵌入的不足监督。此外，提出了VLPO（视觉-潜在策略优化）方法，这是一种强化学习方法，用于将潜在嵌入明确纳入策略梯度更新中。构建了包含125K个真实世界、图表、OCR和几何推理的Monet-SFT-125K文本-图像交替CoT数据集。
### Conclusion
Monet-7B模型在实际感知和推理基准测试中表现出一致的优势，并在具有挑战性的抽象视觉推理任务中展现了强大的泛化能力。进一步分析了每个训练组件的作用，并讨论了早期的不成功尝试，为未来的视觉潜在推理发展提供了见解。模型、数据和代码可在提供的链接处获得。
## 467. `cs.CV` - MobileI2V：移动设备上的快速高分辨率图像到视频 [PDF](https://arxiv.org/pdf/2511.21475), [HTML](https://arxiv.org/abs/2511.21475)
### Authors
Shuai Zhang,Bao Tang,Siyuan Yu,Yueting Zhu,Jingfeng Yao,Ya Zou,Shanglin Yuan,Li Yu,Wenyu Liu,Xinggang Wang
### Background
最近，视频生成见证了迅速的发展，特别是在移动设备上的图像到视频（I2V）合成越来越受到关注。然而，扩散模型由于计算复杂度高和生成速度慢等问题，在资源受限的移动设备上进行实时高分辨率视频生成仍然面临着显著的挑战。
### Innovation
提出了一种名为MobileI2V的轻量化270M扩散模型，旨在移动设备上实现快速图像到视频生成。创新点在于：(1) 分析了线性注意力模块和softmax注意力模块在移动设备上的性能，提出了一种平衡生成效率和质量的线性混合架构去噪器；(2) 设计了一种时间步长蒸馏策略，将I2V采样步骤从超过20步压缩到仅2步，而且质量损失不大，从而将生成速度提高了10倍；(3) 应用了针对移动设备的注意力优化技术，实现了注意力操作在设备端推理过程中的2倍速度提升。MobileI2V首次实现了在移动设备上的快速720p图像到视频生成，且生成质量与现有模型相当。
### Conclusion
MobileI2V在移动设备上实现了高效、低延迟的720p图像到视频生成，生成每帧720p视频的速度低于100毫秒。该模型能够平衡生成质量和效率，满足移动设备在实时视频生成方面的实际需求。
## 468. `cs.CV` - Merge and Bound: 直接在权重上进行的操作以实现类别增量学习 [PDF](https://arxiv.org/pdf/2511.21490), [HTML](https://arxiv.org/abs/2511.21490)
### Authors
Taehoon Kim,Donghwan Jang,Bohyung Han
### Background
类别增量学习（Class Incremental Learning, CIL）研究的是在已有知识的基础上，逐步学习新的类别，而不会忘记之前学到的知识。现有的CIL方法通常会进行模型的微调或初始化，不直接在权重空间进行优化操作。
### Innovation
提出了一种新型的训练方法Merge-and-Bound (M&B)，该方法直接在参数空间内操作模型权重。M&B方法包括两种权重合并类型：跨任务权重合并和内任务权重合并。该方法还提出了一种有界的更新技术，以最小化累积更新，同时保留先前任务的知识，从而减少灾难性遗忘的可能性。
### Conclusion
M&B方法无缝地集成到现有的CIL方法中，无需修改架构组件或修改学习目标。在标准的CIL基准测试上进行了广泛的评估，并显示了与最先进的方法相比的优越性能。
## 469. `cs.CV` - PFF-Net：基于贴图特征拟合的点云法线估计 [PDF](https://arxiv.org/pdf/2511.21365), [HTML](https://arxiv.org/abs/2511.21365)
### Authors
Qing Li,Huifang Feng,Kanle Shi,Yue Gao,Yi Fang,Yu-Shen Liu,Zhizhong Han
### Background
估计点的法线需要构建局部区域来提供中心-周围上下文，但正确确定不同数据或几何结构的合适邻域大小非常困难。现有方法通常采用各种参数复杂的策略来从输入区域中提取完整特征描述，但仍难以准确且高效地预测不同点云的法线。
### Innovation
本文提出了一种新的特征提取方法，用于点云法线的鲁棒估计。通过融合不同邻域大小的多尺度特征，解决了选择合适区域大小的问题，并提出了一个基于多尺度特征的贴图特征拟合（PFF）模型来近似最优几何描述，利用多尺度特征聚合和跨尺度特征补偿实施近似过程。
### Conclusion
实验结果表明，我们的方法在合成和真实世界的数据集上取得了最先进的性能，且网络参数更少、运行时间更短。PFF-Net能够实现不同局部区域的规模自适应，并提供最佳特征描述。
## 470. `cs.CV` - 使用边界框思考：通过强化微调增强时空视频定位 [PDF](https://arxiv.org/pdf/2511.21375), [HTML](https://arxiv.org/abs/2511.21375)
### Authors
Xin Gu,Haoji Zhang,Qihang Fan,Jingxuan Niu,Zhipeng Zhang,Libo Zhang,Guang Chen,Fan Chen,Longyin Wen,Sijie Zhu
### Background
时空视频接地(STVG)要求从自然语言描述中在未裁剪的视频中同时时间和空间地定位目标对象。尽管多模态大型语言模型(MLLMs)在语言理解方面表现出色，但在STVG任务上表现不佳，原因是训练目标不匹配以及标准视觉编码器中的细粒度区域词对齐较弱。
### Innovation
提出了STVG-o1框架，这是第一个能够使现成的MLLMs在时空视频接地任务上达到最先进的性能，而无需任何架构上的修改。该方法引入了一个边界框链式推理机制，在生成最终预测之前在一个中间步骤中明确推理时空位置。进一步设计了一个多维度的强化奖励函数，包括格式、一致性、时间和空间奖励，以及思考奖励，通过强化微调提供了几何感知的监督。
### Conclusion
STVG-o1在HCSTVG上设置了新的最先进的结果，超越了最好的特定任务方法7.3%的m_tIoU，在VidSTG上与专门模型持平，并大幅超越所有现有基于MLLM的方法。它还展示了强大的开放式词汇的一般化能力，确立了MLLMs作为时空定位精确标准模型的可行和强大的骨干网的地位。
## 471. `cs.CV` - 频率感知的 token 减少策略以提高高效视觉变换器 [PDF](https://arxiv.org/pdf/2511.21477), [HTML](https://arxiv.org/abs/2511.21477)
### Authors
Dong-Jae Lee,Jiwan Hur,Jaehyun Choi,Jaemyung Yu,Junmo Kim
### Background
视觉变换器在各种计算机视觉任务中展现了出色的表现，但它们与 token 长度成二次方的计算复杂性是一个重大挑战。现有的 token 减少方法虽然广泛探索，但常常忽视了自我注意的频率特性，如秩塌缩和过度平滑现象。
### Innovation
本文提出了一种频率感知的 token 减少策略，该策略通过保留高频率 token 和将低频率 token 聚合成一个紧凑的直接电流 token，从而提高了计算效率，同时保持了性能并缓解了秩塌缩。该方法通过实验证明，在降低计算开销的同时显著提高了准确性，同时缓解了秩塌缩和过度平滑现象。
### Conclusion
研究还分析了以前的方法，揭示了它们的隐含频率特性及其局限性。结果表明，本文提出的方法有效提高了视觉变换器的效率和性能。
## 472. `cs.CV` - 从观察到行动：工业环境中的基于潜在动作的构建块分割用于VLA预训练 [PDF](https://arxiv.org/pdf/2511.21428), [HTML](https://arxiv.org/abs/2511.21428)
### Authors
Jiajie Zhang,Sören Schwertfeger,Alexander Kleiner
### Background
本文介绍了一种新的无监督框架，旨在从连续的工业视频流中解锁大量未标记的人类演示数据，用于Vision-Language-Action (VLA) 模型的预训练。背景在于现有的大量工业视频数据并未充分利用，特别是在缺乏监督信息的情况下进行预训练依然是一个挑战。
### Innovation
创新在于提出了一个两步流程：首先训练一个轻量级的动作分词器来编码动作动态；其次使用一个无监督的行为分割器，利用新颖的“潜在动作能量”指标来发现并分割出语义上一致的行为构建块。这个流程直接输出分割的视频片段及其对应的潜在动作序列，为VLA的预训练提供了结构化的数据支持。
### Conclusion
在公共基准数据集和一个专有电动机装配数据集上的评估表明，该方法能够有效分割人类在工作站执行的关键任务。进一步的聚类和视力语言模型评估证实了发现的行为构建块具有语义一致性。这是首次完全自动化的端到端系统，用于从零散的工业视频中提取和组织用于VLA预训练的数据，为制造环境中的嵌入式AI集成提供了可扩展的解决方案。
## 473. `cs.CV` - DiverseVAR: 平衡下一尺度视觉自回归模型的多样性和质量 [PDF](https://arxiv.org/pdf/2511.21415), [HTML](https://arxiv.org/abs/2511.21415)
### Authors
Mingue Park,Prin Phunyaphibarn,Phillip Y. Lee,Minhyuk Sung
### Background
尽管视觉自回归（VAR）模型已经成为图像生成中与扩散模型和流模型竞争的强大对手，但它们在多样性方面存在显著缺陷，经常在简单的提示场景下产生几乎相同的结果。这种问题通常被忽视，因为研究人员更注重图像的质量。
### Innovation
我们提出了DiverseVAR框架，该框架在不需要重新训练、微调或显著增加计算开销的情况下，在测试时间增强视觉自回归模型的多样性。通过借鉴扩散模型多样性的增强技术，我们首先建议在文本嵌入中注入噪声，这引入了多样性和图像质量之间的权衡。为了保持质量，我们还提出了新颖的latent尺度旅行技术，这是一种借鉴扩散模型中的时间旅行策略的新型隐空间细化技术。实验表明，将文本嵌入噪声注入与我们的尺度旅行精炼技术相结合，可以显著提高多样性，同时最小化图像质量的下降，实现了多样性和质量间的新的帕累托前沿。
### Conclusion
DiverseVAR在现有模型的基础上取得了进步，通过引入噪声和数据生成过程的临时中断，模型在提高多样性的前提下，显著保持了图像的质量。这种方法在多样性与质量之间的权衡中实现了新的里程碑，展示了在不牺牲图像质量的前提下如何增加视觉生成模型的多样性。
## 474. `cs.CV` - EoS-FM: Can an Ensemble of Specialist Models act as a Generalist Feature Extractor? [PDF](https://arxiv.org/pdf/2511.21523), [HTML](https://arxiv.org/abs/2511.21523)
### Authors
Pierre Adorni,Minh-Tan Pham,Stéphane May,Sébastien Lefèvre
### Background
近年来，基础模型在自然语言处理和计算机视觉等领域取得了显著进展，类似的努力也正在地球观测社区中出现。这些模型旨在在有限监督下泛化到任务，减少为每个任务训练独立模型的需求。然而，目前的方法主要集中在扩大模型规模和数据集的大小，这需要巨大的计算和数据资源，限制了这些模型的可访问性，仅限于少数大型机构。此外，这一持续扩大的模型范式与可持续和环境友好型AI的原则相冲突，因为它导致了巨大的碳足迹和资源低效。
### Innovation
本文提出了一种新颖且有效的方法：构建遥感基础模型（RSFMs）的专家模型集合框架（Ensemble-of-Specialists framework）。该方法将训练过程分解为轻量级、任务特定的ConvNeXtV2专家，可以冻结并重复使用。这种方法具有高效的模块化结构，易于解释，并且具有扩展性。此外，它自然支持联邦训练、剪枝和连续专家集成，特别适合协作且资源受限的环境。
### Conclusion
本框架为构建可扩展和高效的RSFMs提供了新的方向。
## 475. `cs.CV` - 深伪检测器的通用设计选择 [PDF](https://arxiv.org/pdf/2511.21507), [HTML](https://arxiv.org/abs/2511.21507)
### Authors
Lorenzo Pellegrini,Serafino Pandolfini,Davide Maltoni,Matteo Ferrara,Marco Prati,Marco Ramilli
### Background
现有的深伪检测方法的有效性往往更多地依赖于实现细节，如数据预处理、数据增强策略和优化技术，而非核心设计。这使得不同检测器之间的公正比较和理解其性能的真正影响因素变得困难。
### Innovation
本文系统研究了不同设计选择如何影响深伪检测模型的准确性和泛化能力，重点关注与训练、推理和增量更新相关的方面。通过隔离各个因素的影响，本文旨在建立稳健且架构无关的最佳实践，用于未来深伪检测系统的开发。
### Conclusion
实验确定了一组设计选择，这些选择始终可以改进深伪检测效果，并使人工智能基准测试（AI-GenBench）上的性能达到最新水平。
## 476. `cs.CV` - 非均匀时间跨度中具有特征约束的年龄特异性阿尔茨海默病预测 [PDF](https://arxiv.org/pdf/2511.21530), [HTML](https://arxiv.org/abs/2511.21530)
### Authors
Xin Hong,Kaifeng Huang
### Background
阿尔茨海默病（Alzheimer's disease）是一种以认知功能下降为特征的严重疾病。及时识别这种疾病对于开发个性化的治疗策略以减缓其进展至关重要。然而，由于输入序列在不规则的时间间隔内采集，使用生成的图像进行疾病预测面临挑战，特别是如何准确反映疾病特征。
### Innovation
本研究提出了一种创新的方法论，通过量化指标指导生成序列图像，以保持疾病进展的关键特征。此外，引入了年龄缩放因子来生成年龄特异性MRI图像，有助于预测疾病的晚期阶段。实验证据表明，量化指标的加入显著提高了MRI图像合成的准确性。年龄缩放像素损失的应用也有助于增强MRI图像的迭代生成。
### Conclusion
在长期疾病预后方面，结构相似性指数达到了0.882的峰值，表明合成的图像在很大程度上具有相似性。
## 477. `cs.CV` - 基于自适应学习率的抗核抗体图像检测 [PDF](https://arxiv.org/pdf/2511.21519), [HTML](https://arxiv.org/abs/2511.21519)
### Authors
Yiyang Jiang,Guangwu Qian,Jiaxin Wu,Qi Huang,Qing Li,Yongkang Wu,Xiao-Yong Wei
### Background
抗核抗体（ANA）检测是诊断类风湿性关节炎、干燥综合征和硬皮病等多种自身免疫疾病的重要方法。尽管ANA检测具有重要性，但手动检测过程繁琐费时，需要多年经验。此外，超过了100种共存抗体类型使得荧光图案组合极其多样。虽然机器学习和深度学习可以实现自动化，但在实际临床环境中，ANA检测仍面临多实例、多标签学习的独特挑战。
### Innovation
本论文提出了一种新颖的框架，用于处理多实例、多标签学习任务，且能够在未经人工预处理的显微镜图像中直接进行自动化检测，而不改变图像。该框架采用了三种特定任务的组件：实例采样器、概率伪标签分发器和自定步长的学习率系数。这些组件通过抑制低置信度实例、根据实例可区分性自适应分配标签以及根据实际标签观察进行训练调整等方式，克服了传统多标签学习方法的局限，支持端到端优化。
### Conclusion
该框架在用于ANA检测的数据集以及三个公开的医疗多标签学习基准数据集上进行了广泛实验。实验结果表明，该框架在F1-Macro和mAP均取得了显著改进，分别为+7.0%和+12.6%。在其他关键度量指标上，与最佳先前方法相比，框架的表现同样卓越，减少Hamming损失和one-error分别达18.2%和26.9%，并设置了新的最先进的性能记录。
## 478. `cs.CV` - 视频生成模型是优秀的潜在空间奖励模型 [PDF](https://arxiv.org/pdf/2511.21541), [HTML](https://arxiv.org/abs/2511.21541)
### Authors
Xiaoyue Mi,Wenqing Yu,Jiesong Lian,Shibo Jie,Ruizhe Zhong,Zijun Liu,Guozhen Zhang,Zixiang Zhou,Zhiyong Xu,Yuan Zhou,Qinglin Lu,Fan Tang
### Background
ReFL在图像生成中已显示出有效的优化能力，但应用于视频生成时面临显著挑战。现有的视频奖励模型依赖于设计用于像素空间输入的视觉-语言模型，这限制了ReFL优化仅能在经过计算密集的VAE解码后的近完全去噪步骤中进行。这种方法导致了大幅提升的内存消耗和训练时间，并且在优化过程中缺乏早期监督，仅能优化视觉质量而非基础的运动动态和结构一致性。
### Innovation
本工作展示了预训练的视频生成模型天生适合在噪声潜在空间进行奖励建模，因为它们明确设计用于处理任意时间步的噪声潜在表示，并且通过其序列建模能力保留了时间信息。因此，提出了Process Reward Feedback Learning (PRFL)框架，该框架在潜在空间中完全进行偏好优化，避免了VAE解码，使得整个去噪链中的梯度反传更加高效。
### Conclusion
广泛的实验表明，PRFL显著提高了与人类偏好的匹配度，同时在内存消耗和训练时间上相比于RGB ReFL实现了大幅减少。
## 479. `cs.CV` - 基于分层增强的深度学习多类oral病损分类 [PDF](https://arxiv.org/pdf/2511.21582), [HTML](https://arxiv.org/abs/2511.21582)
### Authors
Joy Naoum,Revana Salama,Ali Hamdi
### Background
口腔癌在全世界范围内非常普遍，但由于口腔内良性、前癌性和恶性病损在外观上的相似性，大多数情况下是在晚期才被诊断出来。早期采用计算机辅助诊断系统可以显著提高临床结果。
### Innovation
该研究采用深度学习技术构建了一个用于十六种不同口腔病损的多类别分类器。为了克服数据集有限和不平衡的挑战，研究提出了一种结合分层数据分割和高级数据增强与过采样的技术。
### Conclusion
实验结果表明，该建议模型在准确率、精确率和召回率方面分别达到了83.33％、89.12％和77.31％，显示了该模型在同现有状态最佳方法相比的优势。这表明增强和过采样的策略在少数类别分类性能中非常有效。这项研究成果展示了一种用于口腔癌症早期检测的可信计算机辅助诊断系统的潜在前景。
## 480. `cs.CV` - MoGAN：通过少量步骤的运动对抗后训练提高视频扩散中的运动质量 [PDF](https://arxiv.org/pdf/2511.21592), [HTML](https://arxiv.org/abs/2511.21592)
### Authors
Haotian Xue,Qi Chen,Zhonghao Wang,Xun Huang,Eli Shechtman,Jinrong Xie,Yongxin Chen
### Background
视频扩散模型在帧级保真度方面表现优异，但在运动连贯性、动态效果和现实性方面仍有不足，常出现抖动、鬼影或不合理的动态效果。一个重要限制是，标准的降噪均方误差（MSE）目标无法直接监督时间一致性，导致模型尽管损失低，但生成的运动质量差。
### Innovation
提出了MoGAN，一种运动为中心的后训练框架，无需奖励模型或人类偏好数据即可改善运动现实感。基于三步骤提炼视频扩散模型，该框架训练了一个基于DiT的光学流鉴别器以区分离真实和生成运动，并通过分布匹配正则化器保存视觉保真度。
### Conclusion
MoGAN在Wan2.1-T2V-1.3B测试集上提升了运动质量，并显著提升了VBench和VideoJAM-Bench中的运动得分，同时保持或提高了美学和图像质量评分。人类实验进一步证实MoGAN在运动质量上更受偏好。MoGAN显著提高了运动现实感，未牺牲视觉保真度或效率，提供了一条快速、高质量视频生成的实用路径。
## 481. `cs.CV` - CanKD：基于交叉注意的非局部操作用于特征导向的知识蒸馏 [PDF](https://arxiv.org/pdf/2511.21503), [HTML](https://arxiv.org/abs/2511.21503)
### Authors
Shizhe Sun,Wataru Ohyama
### Background
知识蒸馏是一种通过训练学生模型来模仿复杂教师模型的技巧。传统的基于自注意力的知识蒸馏方法独立对齐教师和学生的特征图，但这种方法未能充分利用所有教师特征图的像素间关系。因此，它可能错过了提高特征表示学习的关键信息。
### Innovation
提出了一种基于交叉注意力的非局部知识蒸馏(CanKD)框架，通过引入交叉注意力机制，使学生特征图中的每个像素都可以动态地考虑教师特征图中的所有像素，从而更全面地捕捉像素间的关联，提升特征表示学习效果。CanKD仅增加了一个新的损失函数，就能在多个任务上超越现有基于注意力的知识蒸馏方法。
### Conclusion
广泛的实验表明，CanKD在目标检测和图像分割任务上优于最先进的特征蒸馏和混合蒸馏方法。这些实验结果表明，CanKD有可能成为计算机视觉任务中基于注意力的知识蒸馏的新范式。
## 482. `cs.CV` - Qwen3-VL 技术报告 [PDF](https://arxiv.org/pdf/2511.21631), [HTML](https://arxiv.org/abs/2511.21631)
### Authors
Shuai Bai,Yuxuan Cai,Ruizhe Chen,Keqin Chen,Xionghui Chen,Zesen Cheng,Lianghao Deng,Wei Ding,Chang Gao,Chunjiang Ge,Wenbin Ge,Zhifang Guo,Qidong Huang,Jie Huang,Fei Huang,Binyuan Hui,Shutong Jiang,Zhaohai Li,Mingsheng Li,Mei Li,Kaixin Li,Zicheng Lin,Junyang Lin,Xuejing Liu,Jiawei Liu,Chenglong Liu,Yang Liu,Dayiheng Liu,Shixuan Liu,Dunjie Lu,Ruilin Luo,Chenxu Lv,Rui Men,Lingchen Meng,Xuancheng Ren,Xingzhang Ren,Sibo Song,Yuchong Sun,Jun Tang,Jianhong Tu,Jianqiang Wan,Peng Wang,Pengfei Wang,Qiuyue Wang,Yuxuan Wang,Tianbao Xie,Yiheng Xu,Haiyang Xu,Jin Xu,Zhibo Yang,Mingkun Yang,Jianxin Yang,An Yang,Bowen Yu,Fei Zhang,Hang Zhang,Xi Zhang,Bo Zheng,Humen Zhong,Jingren Zhou,Fan Zhou,Jing Zhou,Yuanzhi Zhu,Ke Zhu
### Background
Qwen3-VL 是Qwen系列中最先进的视觉-语言模型，能实现多种跨模态基准测试中的优异性能。它能够原生支持多达256K个令牌的交错上下文，结合了文本、图像和视频的无缝集成。模型家族包括不同版本（2B/4B/8B/32B及30B-A3B/235B-A22B），以适应不同延迟和质量之间的权衡。
### Innovation
Qwen3-VL 引入了三个关键升级：增强的交错-MRoPE，增强了图像和视频的空间-时间建模；DeepStack，利用多级ViT特征提高视觉-语言对齐；文本基于的时间对齐，进化为文本时间戳对齐，提供了更精确的时间定位。Qwen3-VL 在不牺牲令牌预算和延迟的情况下，在密集和Mixture-of-Experts架构中表现出更优异的性能。
### Conclusion
Qwen3-VL 预期将成为图像锚定推理、自主决策和多模态代码智能在实际工作流程中基础引擎。
## 483. `cs.CV` - 使用2D/3D配准损失增强骨盆透视中的标记点检测模型 [PDF](https://arxiv.org/pdf/2511.21575), [HTML](https://arxiv.org/abs/2511.21575)
### Authors
Chou Mo,Yehyun Suh,J. Ryan Martin,Daniel Moyer
### Background
自动化标记点检测为医疗专业人员提供了利用术中影像理解和分析患者解剖结构和定位的有效方法。尽管当前的骨盆透视检测方法准确性有希望，但大多数方法假设骨盆呈现固定的一个前-后的视图。然而，在实际手术过程中，由于影像设备的重新定位或目标结构的自身变动，定位有时会发生偏离。
### Innovation
提出了一个新的框架，将2D/3D标记点配准整合进U-Net标记预测模型的训练中。对比了基础的U-Net、带有姿态估计损失的U-Net预训练以及使用姿态估计损失微调后的U-Net在动态患者姿态下的检测准确性差异。
### Conclusion
该研究通过引入2D/3D配准损失增强了骨盆透视中的标记点检测模型的性能，证明了在术中实际条件下可以提高标记点检测的准确性。
## 484. `cs.CV` - ReSAM: Refine, Requery, and Reinforce: Self-Prompting Point-Supervised Segmentation for Remote Sensing Images [PDF](https://arxiv.org/pdf/2511.21606), [HTML](https://arxiv.org/abs/2511.21606)
### Authors
M.Naseer Subhani
### Background
交互式分割模型如Segment Anything Model (SAM) 在自然图像上的泛化效果显著，但在遥感图像（RSI）上的表现欠佳，主要是因为领域转移严重和密集标注稀缺。现有方法依赖于全遮罩监督，导致SAM在RSI上的性能不佳。
### Innovation
本文提出了一种自提示、点监督框架，利用稀疏点标注使SAM适应RSI，采用Refine-Requery-Reinforce循环，生成粗略伪遮罩（Refine），并通过自构建框提示改进（Requery），在迭代中对嵌入进行对齐以减少确认偏差（Reinforce），从而加快SAM的分割质量和领域鲁棒性的提升，无需依赖全遮罩监督。
### Conclusion
在WHU、HRSID和NWPU VHR-10三个RSI基准数据集上评估，该方法能持续超越预训练的SAM和最新点监督分割方法，结果表明，自提示和语义对齐为大规模的遥感应用中基础分割模型的点级别自适应提供了一条有效的途径。
## 485. `cs.CV` - CaFlow: 提升长时动作质量评估的因果反事实流 [PDF](https://arxiv.org/pdf/2511.21653), [HTML](https://arxiv.org/abs/2511.21653)
### Authors
Ruisheng Han,Kanglei Zhou,Shuang Chen,Amir Atapour-Abarghouei,Hubert P. H. Shum
### Background
动作质量评估（AQA）从动作视频中预测细致的执行得分，并广泛应用于体育、康复和技能评估。长期AQA，如花样滑冰和韵律体操，尤其具有挑战性，因为它需要建模长期动态，同时保持对上下文干扰的鲁棒性。现有方法要么依赖昂贵的标注，要么依赖单向时间建模，这会使其容易出现虚假相关性和长期表示的不稳定性。
### Innovation
本文提出了CaFlow，一种统一框架，将因果反事实去混杂与双向时间条件流相结合。因果反事实正则化（CCR）模块通过自监督方式解耦因果和混杂特征，并通过反事实干预保证因果鲁棒性。双向时间流（BiT-Flow）模块则带有循环一致性约束，对前后动态建模，生成更平滑、更连贯的表示。在多个长期AQA基准上的广泛实验表明，CaFlow达到了最先进的性能。
### Conclusion
在多个长期AQA基准上的广泛实验表明，CaFlow达到了最先进的性能。代码可在以下URL下载：this https URL。
## 486. `cs.CV` - 基于GCN的动作识别中的主动学习 [PDF](https://arxiv.org/pdf/2511.21625), [HTML](https://arxiv.org/abs/2511.21625)
### Authors
Hichem Sahbi
### Background
尽管图卷积网络（GCNs）在基于骨架的动作识别方面取得显著成功，但其性能通常依赖于大量标注数据，而在实际应用中标注数据常常稀缺。
### Innovation
本文提出了一种新的高效标签GCN模型，主要贡献如下：1) 开发了一种新颖的获取函数，采用对抗策略选择具有代表性和多样性的标注样本；2) 引入了双向和稳定的GCN架构，使网络更有效地映射时空数据，从而更好地理解学习到的示例分布。
### Conclusion
在两个具有挑战性的基于骨架的动作识别基准数据集上的广泛评估表明，与之前的工作相比，本文提出的高效标签GCN性能显著提高。
## 487. `cs.CV` - Multimodal Robust Prompt Distillation for 3D Point Cloud Models [PDF](https://arxiv.org/pdf/2511.21574), [HTML](https://arxiv.org/abs/2511.21574)
### Authors
Xiang Gu,Liming Lu,Xu Zheng,Anan Du,Yongbin Zhou,Shuchao Pang
### Background
学习型3D点云模型因其在安全敏感应用中的可靠性受到基于对抗攻击的严重威胁。现有的防御方法通常存在计算开销大以及跨不同攻击类型的泛化能力差的问题。
### Innovation
提出了一种新颖且高效的教师-学生框架，名为多模态鲁棒提示精练(MRPD)，用于提炼鲁棒的3D点云模型。该方法通过将学生的点云模型特征与三位不同教师提供的鲁棒嵌入对齐，学习轻量级的提示，并通过信心门控机制动态平衡所有输入模态的贡献，从而确保可靠的知识转移。MRPD在多种白盒和黑盒攻击面前显著优于现有最先进的防御方法，同时在干净的数据上也表现出色。
### Conclusion
我们的工作为构建高效利用多模态知识的鲁棒3D视觉系统提供了新的实用范式。
## 488. `cs.CV` - Multi-Crit：评估多元标准遵循能力的多模态评判 [PDF](https://arxiv.org/pdf/2511.21662), [HTML](https://arxiv.org/abs/2511.21662)
### Authors
Tianyi Xiong,Yi Ge,Ming Li,Zuolong Zhang,Pranav Kulkarni,Kaishen Wang,Qi He,Zeying Zhu,Chenxi Liu,Ruibo Chen,Tong Zheng,Yanshuo Chen,Xiyao Wang,Renrui Zhang,Wenhu Chen,Heng Huang
### Background
大型多模态模型（LMMs）因其较强的指令跟随能力和与人类偏好的一致性，在多元模态评估系统中被广泛应用。然而，这些模型在遵循多样而细致的评估标准方面的能力尚未得到充分探索。为此，作者开发了Multi-Crit基准测试，以评估多模态评判在遵循多元标准并生成可靠标准级别判断方面的性能。该基准测试涵盖了开放生成和可验证推理任务，通过严格的数据收集流程，收集了具有多标准人力注释的具有挑战性的响应对。此外，它还引入了三个新型指标，系统地评估多元标准的遵守情况、标准转换的灵活性以及识别标准级别偏好冲突的能力。
### Innovation
该研究开发了Multi-Crit基准测试，用于评估多模态评判在遵循多元标准并生成可靠标准级别判断方面的性能。它涵盖了开放生成和可验证推理任务，并通过严格的数据收集流程，收集了具有挑战性的响应对，同时引入了三个新型指标来系统地评估多元标准的遵守情况、标准转换的灵活性以及识别标准级别偏好冲突的能力。
### Conclusion
25个LMMs的全面分析揭示了以下内容：1) 专有模型在保持对多元标准的一致遵守方面仍然存在问题，特别是在开放生成评估中；2) 开源模型在灵活遵循多元标准方面进一步落后；3) 评论者微调与综合判断信号相结合，可以增强视觉定位，但无法应用于多元标准级别的判断。针对推理微调、测试时的可扩展性和开源与专有模型界限一致性等分析进一步探索了当前多模态评判模型的局限性。作为一项开创性研究，Multi-Crit为建设可靠和可控的多模态AI评估奠定了基础。
## 489. `cs.CV` - UAVLight：基于无人机场景的光照鲁棒三维重建基准 [PDF](https://arxiv.org/pdf/2511.21565), [HTML](https://arxiv.org/abs/2511.21565)
### Authors
Kang Du,Xue Liao,Junpeng Xia,Chaozheng Guo,Yi Gu,Yirui Guan,Duotun Wang,ShengHuang,Zeyu Wang
### Background
在多视角三维重建中，光照不一致性是一个基本挑战。由于太阳照射方向、云层覆盖率及阴影的改变打破了经典多视图立体视觉（MVS）和结构从运动（SfM）流程以及近期神经渲染方法背后的恒定光照假设，导致几何变形、颜色不一致及阴影印迹等问题。特别是在无人机基于的重建中，长时间飞行和户外环境使光照变化不可避免。然而，现有数据集要么局限于短时间窗口，缺乏有意义的光照多样性；要么跨越数月和季节，几何和语义变化混杂，妨碍了光照鲁棒性的独立研究。
### Innovation
我们引入了UAVLight，一种控制真实环境下的光照鲁棒3D重建基准。每个场景通过地理参考的反复飞行路径在一天中的多个固定时间段捕获，产生一致几何形状和校准下的自然光照变化。通过提供在光照条件标准评估协议下的可靠性基础，UAVLight为开发和基准测试在真实户外环境中有统一性、忠实性和可重新光源的重建方法提供了可靠依据。
### Conclusion
UAVLight提供了在不同光照条件下标准化评估协议，为开发和基准测试可在真实户外环境中一致、忠实且可重新光源的3D重建方法提供了可靠的基线。
## 490. `cs.CV` - Harmony: 通过跨任务协同实现音频和视频生成同步 [PDF](https://arxiv.org/pdf/2511.21579), [HTML](https://arxiv.org/abs/2511.21579)
### Authors
Teng Hu,Zhentao Yu,Guozhen Zhang,Zihan Su,Zhengguang Zhou,Youliang Zhang,Yuan Zhou,Qinglin Lu,Ran Yi
### Background
在生成型人工智能中，同步音频-视觉内容的合成是一个关键挑战。开源模型在稳健的音频-视频对齐方面面临挑战。我们的分析揭示了这一问题源于三项基本挑战：（1）对应关系漂移，即同时演变的噪声潜在变量阻碍了对齐的稳定学习；（2）低效的全局注意机制无法捕捉细微的时间线索；（3）传统的无分类器自由引导（CFG）的模内偏见，这增强了条件性，但并没有促进跨模态同步。
### Innovation
我们引入了Harmony，这是一个新颖的框架，通过机制性地确保视觉和音频同步来克服这些挑战。首先，我们提出了一个跨任务协同训练范式，通过利用音频驱动视频生成任务和视频驱动音频生成任务中的强监督信号来减轻漂移。然后，我们设计了一个全局-局部解耦交互模块，以实现高效和精确定时风格对齐。最后，我们提出了同步增强无分类器自由引导（SyncCFG），在推断过程中明确隔离并放大对齐信号。广泛的实验结果表明，Harmony在生成保真度和特别是在实现精细的音频-视觉同步方面表现良好，显著优于现有方法。
### Conclusion
Harmony通过机制性地确保视觉和音频同步，克服了这些挑战，在生成保真度和，特别是在实现精细的音频-视觉同步方面，建立了新的系统最先进。
## 491. `cs.CV` - 低资源设备上的持续错误纠正 [PDF](https://arxiv.org/pdf/2511.21652), [HTML](https://arxiv.org/abs/2511.21652)
### Authors
Kirill Paramonov,Mete Ozay,Aristeidis Mystakidis,Nikolaos Tsalikidis,Dimitrios Sotos,Anastasios Drosou,Dimitrios Tzovaras,Hyunjun Kim,Kiseok Chang,Sangdok Mo,Namwoong Kim,Woojong Yoo,Jijoong Moon,Umberto Michieli
### Background
随着人工智能模型在日常设备中的广泛部署，预测错误已经成为影响用户体验的关键问题。现有解决方案主要集中在错误检测，但很少提供高效的纠正机制，特别是在资源受限的设备上。本文的背景在于现有技术在纠正资源受限设备中的错误方面存在局限性。
### Innovation
本文提出了一种新型系统，允许用户通过少量样本学习来纠正AI的分类错误，该系统能够利用服务端的基础模型训练与设备端原型分类机制相结合的方式，在无需重新训练模型的情况下，通过原型更新实现高效错误纠正。这种系统的创新点在于结合了服务端的知识蒸馏和设备端的原型适配机制。
### Conclusion
该系统在图像分类和物体检测任务上进行了演示，结果表明，在Food-101和Flowers-102数据集的一次性场景中，能够实现超过50%的错误纠正，同时保持了少量（少于0.02%）的遗忘度和几乎可以忽略不计的计算开销。通过Android演示应用验证了该系统的实际应用可行性。
## 492. `cs.CV` - 无需像素即可识别：从摄像机轨迹进行感知 [PDF](https://arxiv.org/pdf/2511.21681), [HTML](https://arxiv.org/abs/2511.21681)
### Authors
Zihui Xue,Kristen Grauman,Dima Damen,Andrew Zisserman,Tengda Han
### Background
此前的研究通常依赖视频中的像素信息来解析视频内容。然而，本文提出的问题是：是否有可能仅通过摄像机轨迹来感知视频内容，而无需直接观察像素？这项工作是首次系统地探讨这一看似不可能的问题。
### Innovation
本文提出了一个对比学习框架，用于训练专门的编码器 CamFormer，该编码器将摄像机姿姿轨迹投影到联合嵌入空间，并与自然语言对齐。这一研究表明，摄像机轨迹实际上是个非常具有信息量的信号，能够揭示视频内容。由此，提出了一种轻量、鲁棒且多功能的方法来感知视频内容。
### Conclusion
本文的实验表明，无论使用哪种相机姿态估计方法，编码器的表示都具有鲁棒性，包括高保真的多传感和标准的RGB-only估计算法。这些发现确立了摄像机轨迹作为感知视频内容的轻量、鲁棒且多功能的模态的重要性，适用于从跨模态对齐到分类和时间分析等多种下游任务。
## 493. `cs.CV` - 在傅里叶变换下使用分数变分方法的光谱滤波 [PDF](https://arxiv.org/pdf/2511.20675), [HTML](https://arxiv.org/abs/2511.20675)
### Authors
Nelson H. T. Lemes,José Claudinei Ferreira,Higor V. M. Ferreira
### Background
拉曼光谱分析中，荧光信号的干扰和噪声问题依然严峻，这些干扰和噪声经常会掩盖关键的谱线特征，影响分析的准确性。以往的研究大多依赖于图像去噪的方法进行改进，但仍有提升空间。
### Innovation
本文提出了一种结合变分方法和分数微积分的傅里叶变换领域方法，通过最小化涉及分数导数的功能来平衡噪声抑制与光谱信号中关键化学特征的保留，优化去噪参数和导数阶数通过香农熵的概念，从而在去噪的同时保留光谱和图像的关键特征。
### Conclusion
研究表明，结合所提出的策略能够实现高效、健壮且易于实现的滤波器。
## 494. `cs.CV` - G$^2$VLM: 以几何为基础的统一3D重建与空间推理的视觉语言模型 [PDF](https://arxiv.org/pdf/2511.21688), [HTML](https://arxiv.org/abs/2511.21688)
### Authors
Wenbo Hu,Jingli Lin,Yilin Long,Yunlong Ran,Lihan Jiang,Yifan Wang,Chenming Zhu,Runsen Xu,Tai Wang,Jiangmiao Pang
### Background
现有的视觉-语言模型（VLMs）在空间智能方面表现不够稳健，特别是在空间理解和推理任务上的表现不佳。这一差距被归因于缺乏能够从2D图像中重建3D空间的视觉几何学习过程。现有模型缺乏直接处理3D特征的能力，从而限制了它们在空间推理任务中的表现。
### Innovation
本文提出了G$^2$VLM，这是一种几何导向的视觉-语言模型，结合了空间3D重建和空间理解这两个空间智能的基础方面。G$^2$VLM能够直接使用学习到的3D视觉几何特征，通过上下文学习和交织推理直接预测3D属性，从而增强空间推理任务的表现。此外，G$^2$VLM利用丰富的多视角图像和视频数据进行训练，同时结合了通常只有通过难以收集的标注才能获得的3D视觉先验的优势。
### Conclusion
实验结果表明，G$^2$VLM在3D重建和空间理解及推理任务上表现出色，优于或接近当前最先进的直接3D重建模型。通过将语义强烈的视觉语言模型与低级3D视觉任务统一，我们期望G$^2$VLM能够为社区提供一个强大的基准，并为未来的应用如3D场景编辑带来更多可能性。
## 495. `cs.CV` - Canvas-to-Image：多模态控制的合成图像生成 [PDF](https://arxiv.org/pdf/2511.21691), [HTML](https://arxiv.org/abs/2511.21691)
### Authors
Yusuf Dalva,Guocheng Gordon Qian,Maya Goldenberg,Tsai-Shien Chen,Kfir Aberman,Sergey Tulyakov,Pinar Yanardag,Kuan-Chieh Jackson Wang
### Background
虽然现代扩散模型在生成高质量和多样化图像方面表现出色，但在高保真度的构图和多模态控制方面仍存在局限，尤其是在用户同时指定文本提示、主题参考、空间布局、姿态约束和布局注释时。现有的模型难以同时处理多种复杂的控制信号。
### Innovation
Canvas-to-Image引入了一种统一框架，将多种异构控制信号整合到一个画布界面上，使用户能够生成忠实反映其意图的图像。该框架通过将多种控制信号编码到单一的复合画布图像中，供模型直接解释，从而实现了整合式的视觉-空间推理。同时，提出了一个多元任务画布训练策略，优化扩散模型以统一学习方式理解并整合多种异构控制信号，增强了模型在多控制模态下的推理能力。
### Conclusion
通过广泛实验，Canvas-to-Image在身份保持和控制一致性方面显著优于现有最先进的方法，在多人合成、姿态控制合成、布局限制生成和多控制生成等具有挑战性的基准测试中表现出色。
## 496. `cs.CV` - 提示感知自适应弹性权重巩固在医疗视觉语言模型中的连续学习 [PDF](https://arxiv.org/pdf/2511.20732), [HTML](https://arxiv.org/abs/2511.20732)
### Authors
Ziyuan Gao,Philippe Morel
### Background
在临床环境中部署的医疗AI系统面临灾难性遗忘的问题，模型需要在学习新的成像协议的同时保留先前的诊断能力。对于必须保留医学成像和临床术语跨模态复杂对齐的医疗视觉语言模型来说，这一挑战尤为严峻。现有的连续学习方法无法有效地缓解这一问题。
### Innovation
本文提出了提示感知自适应弹性权重巩固（PA-EWC），这是一种新的连续学习方法，通过提示引导的参数专业化来应对灾难性遗忘。该方法系统地基于视觉描述、空间引导和医学语义信息处理的功能角色来分类模型参数，以实现关键知识的有目标保护，同时允许对新的临床要求进行适应。PA-EWC采用自适应费希尔信息计算与梯度稳定性分析，并基于医学术语密度开发加权复杂度度量。该方法在五个医疗影像数据集（Kvasir-SEG、ISIC 2018、CheXlocalize、BUSI、CAMUS）上进行了评估，展示了其对灾难性遗忘的有效缓解，相比基线方法减少了17.58%的遗忘，同时在胸部X光病理定位和息肉分割上的性能分别提高了4.30%和6.06%。
### Conclusion
PA-EWC通过提示引导的参数专业化，有效解决了医疗视觉语言模型的学习连续性问题，减少了灾难性遗忘，提高了特定医疗诊断任务的性能。
## 497. `cs.CV` - CHiQPM：校准层次可解释图像分类 [PDF](https://arxiv.org/pdf/2511.20779), [HTML](https://arxiv.org/abs/2511.20779)
### Authors
Thomas Norrenbrock,Timo Kaiser,Sovan Biswas,Neslihan Kose,Ramesh Manuvinakurike,Bodo Rosenhahn
### Background
全球可解释模型是可信人工智能的一个有前景的方法，特别是在安全关键领域。除了全局解释，详细的局部解释对于支持在推理过程中的专家至关重要。本文提出的Calibrated Hierarchical QPM (CHiQPM) 模型能够提供全面的全局和局部可解释性，有助于人与人工智能的互补。
### Innovation
CHiQPM 通过对比性解释大部分类别实现卓越的全局可解释性，同时提供了一种新颖的层次解释方式，这种解释方式更接近人类的推理方式，并且可以通过浏览来提供内置的可解释性置信预测方法（Conformal Prediction, CP）。此外，该模型在保持高预测准确性的同时还提供可解释的预测集，提高了整体效率。
### Conclusion
广泛的评估结果显示，CHiQPM 作为点预测器达到最先进的准确率，同时保持与非可解释模型99%的精度。此外，它的校准集合预测效率与其它 CP 方法相当，同时提供了具有层次解释的可解释预测。这表明，通过将可解释性融入模型中，而不牺牲整体精度，可以在安全关键领域实现显著改进。
## 498. `cs.CV` -  adversarial 多任务学习用于肝脏肿瘤分割、动态增强回归和分类 [PDF](https://arxiv.org/pdf/2511.20793), [HTML](https://arxiv.org/abs/2511.20793)
### Authors
Xiaojiao Xiao,Qinmin Vivian Hu,Tae Hyun Kim,Guanghui Wang
### Background
肝脏肿瘤的分割、动态增强回归和分类对于临床评估和诊断至关重要。然而，现有工作没有尝试在端到端框架中同时实现这些任务，主要是因为缺乏能够捕捉任务间相关性的有效框架来促进相互改进，并且缺少有效的机制来有效地提取动态MRI信息。
### Innovation
提出了Multi-Task Interaction adversarial learning Network (MTI-Net)，这是一种新型的综合框架，旨在同时解决这些任务。MTI-Net结合了Multi-domain Information Entropy Fusion (MdIEF)，使用了熵感知的高频光谱信息，有效地将来自频域和光谱域的特征进行整合，增强了动态MRI数据的提取和利用。网络还引入了任务交互模块，建立了分割和回归之间的一致性，从而促进了任务之间的协同作用并提高了整体性能。此外，设计了一个新颖的任务驱动判别器（TDD）来捕捉任务之间的高阶关系。使用浅层Transformer网络进行位置编码，以捕捉动态MRI序列中的关系。
### Conclusion
在包含238个受试者的数据集上，MTI-Net在多个任务上表现出高水平的性能，表明其在肝脏肿瘤临床评估方面具有很强的潜在价值。这项研究表明，MTI-Net对于肝脏肿瘤的评估具有重要的应用价值。
## 499. `cs.CV` - 为神经元提供有保证的最优组合解释 [PDF](https://arxiv.org/pdf/2511.20934), [HTML](https://arxiv.org/abs/2511.20934)
### Authors
Biagio La Rosa,Leilani H. Gilpin
### Background
神经元是深度神经网络的基本单元，但尚不清楚它们学习的内容及其知识是否与人类知识对齐。组合解释旨在通过逻辑规则描述神经元激活与概念之间的空间对齐，这些逻辑描述通常通过搜索所有可能概念组合来计算。由于在完整状态空间中计算空间对齐性是不可行的，文献中通常采用束搜索来限制搜索空间。然而，束搜索不能提供任何最优性的理论保证，目前也未知当前解释与真实最优解之间的接近程度。
### Innovation
本文通过引入第一个计算保证最优组合解释的框架进行创新。具体而言，本文提出了：(i) 一种分解，用于识别影响空间对齐性的因素，(ii) 一种估计搜索过程中任何阶段对齐性的启发式方法，和 (iii) 首次能够在可行时间内计算出最优组合解释的算法。利用此框架，本文在组合解释中最受欢迎的领域，即计算机视觉领域和卷积神经网络中分析了最优与非最优解释之间的差异。展示了当涉及重叠概念时，束搜索获得的解释中有10-40％是次优的。最后，本文评估了由提出分解和启发式方法引导的束搜索变体，结果显示该方法在运行时间上与先前方法相当或更好，同时提供更大的超参数和计算资源灵活性。
### Conclusion
该研究通过提供理论上保证的最优组合解释框架，提高了神经元解释的准确性和可解释性，特别是在存在重叠概念的情况下，束搜索获得的解释可靠性不足。所提出的分解和启发式方法极大提高了最优解释的计算效率，同时增强了算法的灵活性。
## 500. `cs.CV` - 使用Autoregressive Conditional Generative Adversarial Network进行概率性野火蔓延预测 [PDF](https://arxiv.org/pdf/2511.21019), [HTML](https://arxiv.org/abs/2511.21019)
### Authors
Taehoon Kang,Taeyong Kim
### Background
气候变化加剧了野火的频率和严重性，因此快速而准确的野火蔓延预测对于有效的缓解和应对至关重要。尽管物理模拟器如FARSITE可以提供高度准确的预测，但其计算复杂性限制了其在实时决策中的应用。现有的深度学习模型通常会产生过于平滑的预测，难以捕捉野火蔓延的复杂、非线性动态。
### Innovation
本研究提出了一种自回归条件生成对抗网络（CGAN）用于概率性野火蔓延预测。通过将预测任务表述为自回归问题，模型学习顺序状态转移，确保长期预测稳定性。实验结果显示，提出的CGAN模型在总体预测准确性和火围界的边界定义方面，均优于传统的深度学习模型。对抗学习允许模型捕捉野火蔓延的强烈非线性和不确定性，而不是仅仅拟合像素平均值。此外，自回归框架促进了野火演变的系统性时间预测。
### Conclusion
提出的基于CGAN的自回归框架增强了野火蔓延预测的准确性和物理可解释性，为时间敏感的响应和疏散规划提供了有前景的基础。
## 501. `cs.CV` - AerialMind: 向UAV场景中的引用多对象跟踪迈进 [PDF](https://arxiv.org/pdf/2511.21053), [HTML](https://arxiv.org/abs/2511.21053)
### Authors
Chenglizhao Chen,Shaofeng Liang,Runwei Guan,Xiaolou Sun,Haocheng Zhao,Haiyun Jiang,Tao Huang,Henghui Ding,Qing-Long Han
### Background
当前引用多对象跟踪（RMOT）研究主要局限于地面场景，这限制了它们对广泛场景上下文的捕捉能力以及全面跟踪和路径规划。而无人驾驶飞行器（UAV）凭借其广阔的空中视角和卓越的机动性，能实现大范围监控，并成为具有体感智能的关键平台，这引发了一种能自然语言交互的智能空中系统的空前需求。
### Innovation
提出了AerialMind，这是一个针对UAV场景的大规模RMOT基准数据集；开发了高效且高质量的半自动化协作代理人注释助手（COALA）框架；提出了HawkEyeTrack (HETrack)，这是一种创新性的方法，通过协作增强视觉语言表示学习，优化了UAV场景下的感知。
### Conclusion
实验证明了AerialMind数据集的挑战性以及HawkEyeTrack方法的有效性。
## 502. `cs.CV` - ENACT：基于第一人称交互世界建模评估具身认知 [PDF](https://arxiv.org/pdf/2511.20937), [HTML](https://arxiv.org/abs/2511.20937)
### Authors
Qineng Wang,Wenlong Huang,Yu Zhou,Hang Yin,Tianwei Bao,Jianwen Lyu,Weiyu Liu,Ruohan Zhang,Jiajun Wu,Li Fei-Fei,Manling Li
### Background
具身认知学说认为，智能来源于感觉运动交互而非被动观察。本文提出一个有趣的问题：主要以非具身方式训练的现代视觉-语言模型（VLMs）是否表现出具身认知的特征？为此，文章介绍了ENACT，将具身认知的评估框架化为视觉问答（VQA）格式下的自视点交互的世界建模。ENACT通过部分可观测马尔可夫决策过程（POMDP）形式提出，并包含两个互补的任务序列重新排序：正向世界建模（重新排列给定动作的打乱观察）和逆向世界建模（重新排列给定观察的打乱动作）。尽管概念上看似简单，但解决这些任务隐含的要求了身体认知的关键能力，包括动作效果推理、具身意识和交互性、长时记忆，同时避免了可能导致评估混乱的低级图像合成。
### Innovation
本文提出ENACT，这是第一个评估视觉-语言模型具身认知能力的基准系统。ENACT将世界建模以自视点交互的形式实现，将两个互补任务定义为序列重新排序问题，并结合部分可观测马尔可夫决策过程（POMDP）提供了一个评估框架。通过从机器人仿真中合成问题-回答对并使用8,972个问题-回答对对模型进行评估，该研究揭示了现代前沿视觉-语言模型与人类在这方面的差距，并且指出模型在逆向任务上表现优于正向任务，同时具有人类偏向，如倾向于右手操作和视角变化时能力下降。
### Conclusion
实验结果表明，在交互范围增加时，VLMs的表现与人类的差距加大。模型在逆向任务中的表现优于正向任务，表现出人类偏好，例如倾向于右手操作，并且在相机内在参数或视角偏离人类视觉时表现下降。ENACT为评估VLMs具身认知能力提供了一个有潜力的基准和评估管线。
## 503. `cs.CV` - 使用3D MRI引导的混合深度学习模型革新胶质瘤分割与分级 [PDF](https://arxiv.org/pdf/2511.21673), [HTML](https://arxiv.org/abs/2511.21673)
### Authors
Pandiyaraju V,Sreya Mynampati,Abishek Karthik,Poovarasan L,D. Saraswathi
### Background
胶质瘤是脑肿瘤类型之一，具有高死亡率，因此早期和准确的诊断对于治疗这些肿瘤至关重要。目前，对胶质瘤的诊断和分级难度较大，因此需要更高级的技术方法来解决这一问题。
### Innovation
该研究将开发一种混合深度学习模型，结合U-Net 基于的分割和一种综合DenseNet-VGG分类网络，并加入多头注意机制和空间-通道注意能力。这种混合结构能在3D MRI数据中精确划分肿瘤，并通过一系列准备步骤，如归一化、重采样和数据增强，有效处理高维3D MRI数据。研究表明，该混合框架在测试中表现出色，肿瘤分割的Dice系数为98%，分类准确率为99%，优于传统的CNN模型和无注意力机制的方法，特别通过多头注意力机制更好地强调了临床相关的肿瘤特征，提高了可解释性和准确性。
### Conclusion
该方法展示了巨大的潜力，有助于临床及时和可靠地诊断和分级胶质瘤，从而更好地规划患者治疗。
## 504. `cs.CV` - 注意力导向的稀疏局部对抗攻击：针对视觉-语言-行动模型的斑块攻击 [PDF](https://arxiv.org/pdf/2511.21663), [HTML](https://arxiv.org/abs/2511.21663)
### Authors
Naifu Zhang,Wei Tao,Xi Xiao,Qianpu Sun,Yuxin Zheng,Wentao Mo,Peiqiang Wang,Nan Zhang
### Background
近年来，嵌入式智能中的视觉-语言-行动（VLA）模型发展迅速。然而，现有的对抗攻击方法需要昂贵的端到端训练，并且通常会产生明显的扰动斑块。
### Innovation
提出了ADVLA框架，直接在视觉编码器到文本特征空间投影的特征上应用对抗扰动。ADVLA在低振幅限制下高效地破坏了下游动作预测，并通过注意力引导使扰动既集中又稀疏。引入了三种策略以增强敏感性、强制稀疏性并集中扰动。
### Conclusion
实验表明，在$L_{text{?infty}}=4/255$的约束下，ADVLA结合Top-K遮罩修改了不到10%的斑块，同时达到了近100%的攻击成功率。扰动集中在关键区域，几乎不改变整体图像，在单步骤迭代中仅需约0.06秒，显著优于传统的基于斑块的攻击。总体而言，ADVLA在低振幅和局部稀疏条件下有效削弱了VLA模型的下游动作预测，避免了传统斑块攻击的高训练成本和明显扰动，并展示了其在攻击VLA特征空间的独特效果和实用价值。
## 505. `cs.CV` - 使用多阶段视力转换器框架自动评估赫希施普龙病 [PDF](https://arxiv.org/pdf/2511.20734), [HTML](https://arxiv.org/abs/2511.20734)
### Authors
Youssef Megahed,Saleh Abou-Alwan,Anthony Fuller,Dina El Demellawy,Steven Hawken,Adrian D. C. Chan
### Background
赫希施普龙病的特点是肠壁的肠肌层缺乏神经节细胞，因此正确识别这些细胞是诊断该疾病的关键。现有方法无法有效识别这些神经节细胞，本研究旨在通过引入一种基于Vision Transformer的多阶段分割框架，提高赫希施普龙病的诊断准确性。
### Innovation
本研究提出了一种基于Vision Transformer (ViT-B/16) 的多阶段分割框架，该框架能够模拟病理学家的诊断过程，依次对肌层进行分割、识别肠肌层内的神经节层以及在解剖学上有效的区域内识别神经节细胞。该方法结合了分辨率特定的镶嵌策略和定制化的后处理技术，以确保解剖学上的一致性。实验结果表明该方法在多阶段中表现优异，特别是在神经节细胞的识别上。
### Conclusion
研究方法利用Vision Transformer模型的有效性，通过全局组织上下文和小尺度细胞形态的捕捉，成功地实现了赫希施普龙病中神经节细胞的自动识别。这种方法有望支持数字病理学的工作流程，减少观察者之间的变异，并辅助赫希施普龙病的评估。未来将通过多中心的更大数据集和额外的专家注释评估该方法的临床影响。
## 506. `cs.CV` - SocialNav: 训练受到人类启发的基础模型以实现社交意识的实体导航 [PDF](https://arxiv.org/pdf/2511.21135), [HTML](https://arxiv.org/abs/2511.21135)
### Authors
Ziyi Chen,Yingnan Guo,Zedong Chu,Minghua Luo,Yanfen Shen,Mingchao Sun,Junjun Hu,Shichao Xie,Kuan Yang,Pei Shi,Zhining Gu,Lu Liu,Honglin Han,Xiaolong Wu,Mu Xu,Yu Zhang
### Background
社会规范下的实体导航依然存在研究挑战。现有的技术难以同时实现理解高级社会规范并生成遵守社会规范的低级导航轨迹。
### Innovation
提出了SocialNav，一种具有分层“大脑-行动”架构的社交感知导航基础模型，能够理解高级社会规范并生成符合社会规范的底层轨迹。开发了SocNav数据集，包含认知激活数据集和专家轨迹金字塔，用于为模型注入和精炼导航智能。首次提出了流动增强学习框架（SAFE-GRPO）来实现社交规范的实体导航，该框架明确奖励符合规范的行为。
### Conclusion
SocialNav与现有最先进的方法相比，在导航成功率和社交合规性方面分别提高了38%和46%，展示了在导航性能和社会责任上的显著提升。
## 507. `cs.CV` - Deep Parameter Interpolation for Scalar Conditioning [PDF](https://arxiv.org/pdf/2511.21028), [HTML](https://arxiv.org/abs/2511.21028)
### Authors
Chicago Y. Park,Michael T. McCann,Cristina Garcia-Cardona,Brendt Wohlberg,Ulugbek S. Kamilov
### Background
近年来，扩散模型和流动匹配等深度生成模型使用单个神经网络来学习时间或噪声级别依赖的向量场。设计能够准确表示这种向量场的网络架构具有挑战性，因为网络必须整合高维向量（通常是图像）和标量信息。现有的技术手段要么将标量编码为额外的图像输入，要么在网络组件中结合标量和向量信息，这限制了架构的选择。
### Innovation
本文提出了深度参数内插（DPI），这是一种通用方法，可以将现有深度神经网络架构转换为能够接受额外标量输入的架构。DPI通过在单个网络中维持两个可学习参数集，并在训练和采样过程中根据标量值动态内插这些参数集来引入标量依赖，从而简化了架构并增加了灵活性。该方法无需对特定架构进行调整，就可增加标量依赖性，从而提高去噪性能和样本质量。
### Conclusion
实验表明，DPI方法可以有效提高扩散和流动匹配模型的去噪性能和样本质量，在计算效率方面也与标准的标量条件技术相当。相关代码可以在提供的链接中找到。
## 508. `cs.CV` - OVOD-Agent: 一种基于Markov-Bandit框架的主动视觉推理和自我进化检测 [PDF](https://arxiv.org/pdf/2511.21064), [HTML](https://arxiv.org/abs/2511.21064)
### Authors
Chujie Wang,Jianyu Lu,Zhiyuan Luo,Xi Chen,Chu He
### Background
现有的基于开放词汇表的目标检测方法虽然预训练在大规模的视觉-语言数据集上，但其推理仍受限于固定类别名称，导致多模态训练与单模态推理之间存在差距。以往的工作表明，改善文本表示可以显著提高开放词汇表目标检测（OVOD）的效果，说明文本空间的探索仍不充分。为解决这一问题，本文提出OVOD-Agent框架，将其被动类别匹配转变为主动视觉推理和自进化检测。
### Innovation
提出了OVOD-Agent框架，将文本优化过程扩展为具有明确操作的可视化CoT（Chain-of-Thought），通过弱马尔可夫决策过程（w-MDP）建模视觉上下文转换，并引入一个Bandit模块在有限监督下生成探索信号，从而帮助代理聚焦于不确定区域，并优化检测策略。此外，通过结合马尔可夫转移矩阵和Bandit轨迹，实现了自我监督奖励模型（RM）优化。
### Conclusion
实验表明，OVOD-Agent框架在COCO和LVIS数据集上提供了可靠的改进，特别是在稀有类别上。表明提出的框架有效，该框架在开放式目标检测的各种骨干网络中表现一致。
## 509. `cs.CV` - STAR：增强现实中的手机式打字 [PDF](https://arxiv.org/pdf/2511.21143), [HTML](https://arxiv.org/abs/2511.21143)
### Authors
Taejun Kim,Amy Karlson,Aakar Gupta,Tovi Grossman,Jason Wu,Parastoo Abtahi,Christopher Collins,Michael Glueck,Hemant Bhaskar Surale
### Background
在增强现实（AR）应用程序中，文本输入是一项基本且频繁的任务，但设计一个高效且易于使用的AR文本输入方法仍然是一项开放的挑战。
### Innovation
提出了STAR，一种基于用户对智能手机双拇指打字的熟悉程度的AR文本输入技术。用户可以在虚拟的QWERTY键盘上，将键盘投影到手部皮肤上进行拇指打字。
### Conclusion
参与者在30分钟的练习后实现了平均每分钟21.9个单词（即智能手机打字速度的56%）的打字速度和0.3%的平均错误率。进一步分析了STAR与智能手机打字性能差距的主要原因，并讨论了缩小这一差距的方法。
## 510. `cs.CV` - 基于SDR的CNN-LSTM混合架构的空中自适应调制分类 [PDF](https://arxiv.org/pdf/2511.21040), [HTML](https://arxiv.org/abs/2511.21040)
### Authors
Dinanath Padhya,Krishna Acharya,Bipul Kumar Dahal,Dinesh Baniya Kshatri
### Background
自动调制分类（AMC）是未来无线通信系统的核心技术，能够在无需先验知识的情况下识别调制方案。这一能力对于认知无线电、频谱监控和智能通信网络等应用至关重要。本文提出了一种基于混合卷积神经网络（CNN）和长短期记忆网络（LSTM）架构并结合软件定义无线电（SDR）平台的AMC系统。
### Innovation
该系统利用CNN进行空间特征提取，使用LSTM捕捉时间依赖关系，有效处理复杂且随时间变化的通信信号。该系统通过识别一个自制FM发射机和其他调制方案的空中信号展示了其实用性。系统使用混合数据库（包括RadioML2018数据库和自动生成的数据库）进行训练，通过各种评价指标验证了系统的性能，优化模型在多个指标上均展现了高准确率。
### Conclusion
实验结果验证了混合CNN-LSTM架构在AMC中的有效性，显示出其在自适应频谱管理和高级认知无线电系统中的潜在应用价值。
## 511. `cs.CV` - LTD: 低温度蒸馏以实现无梯度掩蔽的对抗训练 [PDF](https://arxiv.org/pdf/2111.02331), [HTML](https://arxiv.org/abs/2111.02331)
### Authors
Erh-Chung Chen,Che-Rung Lee
### Background
对抗训练是增强神经网络模型对抗对抗性攻击鲁棒性的广泛采用策略。现有的图像分类方法通常将数据表示为独热标签，这被认为是导致模型脆弱性的重要因素。然而，在实际数据集中，数据的模糊性和样本的多类别特征使独热标签表示变得不精确。
### Innovation
论文提出了低温度蒸馏（LTD）方法，这是一种新颖的标签表示方法。LTD 的独特之处在于在导师模型中采用相对较低的温度，而在学生模型中则保持固定的温度，这不仅改进了对数据分布的理解，还增强了模型的鲁棒性，避免了防御蒸馏中常见的梯度掩蔽问题。
### Conclusion
实验结果显示，将LTD方法与现有框架结合使用，在CIFAR-10、CIFAR-100和ImageNet数据集上分别实现了58.19%、31.13%和42.08%的鲁棒准确率，而无需额外的数据。
## 512. `cs.CV` - 视觉物体姿态估计中的不确定性量化 [PDF](https://arxiv.org/pdf/2511.21666), [HTML](https://arxiv.org/abs/2511.21666)
### Authors
Lorenzo Shaikewitz,Charis Georgiou,Luca Carlone
### Background
对于具有鲁棒控制和规划能力来说，量化物体姿态估计的不确定性是必不可少的。虽然姿态估计是一个在机器人领域已经被广泛研究的问题，但在没有严格分布假设的情况下，如何准确地附上统计上严谨的不确定性描述还不是非常明确。
### Innovation
本文提出了一种在单目设置中，针对给定姿态估计的分布自由的姿态不确定性边界方法。该方法只需要高概率的像素检测噪声边界。我们提出了一种称为SLUE（通过S-引理进行不确定性估计）的凸规划，它能将这种不确定性边界减少为一个与真物体姿态具有高概率包含关系的椭球体不确定性边界。对于给定的关键点约束，我们进一步扩展了SLUE，使之成为一个守恒和收敛至最优椭球体不确定性边界的多项式松弛层级。
### Conclusion
我们评估了SLUE在两个姿态估计数据集和一个实际无人机跟踪场景中的表现。与先前的研究结果相比，SLUE生成了更小的平移边界，并且在姿势方向上的不确定性边界表现也十分具有竞争力。我们还免费提供了此代码。
## 513. `cs.CV` - 视觉变换器非单调扩展机制 [PDF](https://arxiv.org/pdf/2511.21635), [HTML](https://arxiv.org/abs/2511.21635)
### Authors
Anantha Padmanaban Krishna Kumar(Boston University)
### Background
深度视觉变换器通常比浅层的性能更差，这是对传统扩展假设的挑战。本文通过在ImageNet上系统分析ViT-S、ViT-B和ViT-L的表现，揭示了深度与表示演化的三层动态规律：悬崖、平台和爬升。这种规律观察到了更好的性能与[CLS]标记逐渐被分散共识所替代有关，[CLS]标记最初设计为全局聚合枢纽。
### Innovation
提出了一个量化的信息混杂度指标——信息扰动指数，揭示了在ViT-L模型中，信息和任务之间的权衡大约在10层之后才出现，与ViT-B相比，额外的层与信息扩散增加相关，而非任务性能提升。研究表明，在这种情况下，变压器架构可能更需要通过精细校准深度来执行清洁的阶段转换，而不是简单地增加参数数量。信息扰动指数为现有模型提供了一个有用的诊断工具，并建议未来架构的设计目标。
### Conclusion
这些结果表明，在这一范围内，视觉变换器架构可能更受益于精心校准的深度，执行清晰的相变，而不是简单增加参数数量。信息扰动指数为现有模型提供了一个有用的诊断工具，并提出了对未来架构设计的有益建议。研究中的所有代码可在以下链接获取：this https URL。
## 514. `cs.CV` - BanglaMM-Disaster：一种基于多模态转换器的多类灾难分类深度学习框架 [PDF](https://arxiv.org/pdf/2511.21364), [HTML](https://arxiv.org/abs/2511.21364)
### Authors
Ariful Islam,Md Rifat Hossen,Md. Mahmudul Arif,Abdullah Al Noman,Md Arifur Rahman
### Background
孟加拉国依然面临着重大自然灾害挑战，因此实时监控和快速响应系统至关重要。本研究提出了一种新的端到端深度学习多模态框架BanglaMM-Disaster，用于基于社交媒体上的文本和视觉数据对灾难进行分类。
### Innovation
该模型结合了基于转换器的文本编码器（包括BanglaBERT、mBERT、XLM-RoBERTa）与CNN网络（ResNet50、DenseNet169、MobileNetV2），利用早期融合处理两种模态。该模型在多类灾难分类中达到了83.76%的准确率，超过了纯文本基线3.84%，超过了仅图像基线16.91%。研究还展示了对所有类别的分类错误减少，尤其对模糊案例有显著改进。
### Conclusion
本工作填补了孟加拉语多模态灾难分析的关键空白，并展示了在资源有限的情况下结合多种数据类型进行实时灾害响应的优势。
## 515. `cs.CV` - AMLP: 可调掩码病灶块用于自监督医学图像分割 [PDF](https://arxiv.org/pdf/2309.04312), [HTML](https://arxiv.org/abs/2309.04312)
### Authors
Xiangtao Wang,Ruizhi Wang,Thomas Lukasiewicz,Zhenghua Xu
### Background
自监督掩码图像建模（MIM）方法在分析自然图像方面已经显示出很有前景的表现。然而，直接将此类方法应用于医学图像分割任务仍难以达到较好的效果。由于医学图像本身比自然图像更复杂，医学图像中的主体通常具有更明显的轮廓特征；此外，传统的高且固定的掩码比率可能掩盖了背景，限制了可学习信息的范围。
### Innovation
本文提出了一种新的自监督医学图像分割框架——可调掩码病灶块（AMLP），该框架利用掩码块选择（MPS）策略来识别高概率包含病灶的块，帮助模型实现精确的病灶重建。此外，引入了相对重建损失（RRL）以更好地学习难以重建的病灶块，进一步提出了类别一致性损失（CCL）来基于重建难度细化块分类，增强病变与背景之间的差异。提出了可调掩码比率（AMR）策略，逐步增加掩码比率以扩展可学习的互信息范围。
### Conclusion
在两个医学分割数据集上的广泛实验表明，提出的AMLP相对于最新的自监督方法具有更好的性能；结果证明，AMLP有效地解决了将掩码建模应用于医学图像和捕捉准确病灶细节的挑战。
## 516. `cs.CV` - ProtoPFormer: 在视觉变换器中聚焦原型部件以实现可解释的图像识别 [PDF](https://arxiv.org/pdf/2208.10431), [HTML](https://arxiv.org/abs/2208.10431)
### Authors
Mengqi Xue,Qihan Huang,Haofei Zhang,Jingwen Hu,Jie Song,Mingli Song,Canghong Jin
### Background
Prototypical part network（ProtoPNet）因其自解释特性（self-explanatory property）在可解释的人工智能（XAI）方面引起了广泛关注，推动了许多后续研究。然而，当直接将ProtoPNet应用于视觉变换器（ViT）的特征提取模块时，学习到的原型存在“注意力误导”问题，它们更容易激活背景信息而忽视前景信息。基于自注意力机制的变换器强大的长依赖建模能力使得现有模型难以聚焦于原型部件，这严重影响了模型的内在可解释性。
### Innovation
本文提出了ProtoPFormer，一种适用于ViT的原型部件变换器方法，专门用于可解释的图像识别。该方法引入了全局和局部原型，以便根据ViT的架构特性捕捉和强调目标的代表性整体和局部特征。全局原型用于提供对象的整体视角，以指导局部原型聚焦于前景并消除背景干扰。接着，局部原型接受显式的监督，专注于各自的原型视觉部分，从而提高整体的可解释性。实验结果表明，提出的全局和局部原型可以互相纠正且共同作出最终决策，分别从整体和局部视角忠实、透明地解释决策过程。此外，ProtoPFormer在现有的原型方法基线中表现优异并具有更佳的可视化结果。
### Conclusion
我们的研究表明，通过引入全局和局部原型，可以有效提升ProtoPFormer在ViT中的可解释性表现。我们的代码已经公开于👉 这个链接。
## 517. `cs.CV` - 孟加拉手语翻译：数据集创建挑战、基准测试与前景 [PDF](https://arxiv.org/pdf/2511.21533), [HTML](https://arxiv.org/abs/2511.21533)
### Authors
Husne Ara Rubaiyeat,Hasan Mahmud,Md Kamrul Hasan
### Background
孟加拉手语（BdSLT）的资源非常匮乏，标准句级数据集的创建对于为说孟加拉语的聋哑人和听力障碍者开发基于AI的辅助工具非常重要。目前，BdSLT的发展受到极大限制。
### Innovation
本文介绍了一个数据集IsharaKhobor及其两个子集，旨在促进相关研究。还对数据集的开发挑战进行了描述，并通过与基于地标的手势和RQE嵌入进行基准测试来展示一些前进方向。此外，还进行了词汇限制和同义词化实验，产生了两个额外的数据集IsharaKhobor_small和IsharaKhobor_canonical_small。
### Conclusion
数据集已公开发布，为研究工作提供了宝贵的资源，同时指出了未来的发展方向。
## 518. `cs.CV` - AV-Edit: 通过音视频语义联合控制的多模态生成音效编辑 [PDF](https://arxiv.org/pdf/2511.21146), [HTML](https://arxiv.org/abs/2511.21146)
### Authors
Xinyue Guo,Xiaoran Yang,Lipan Zhang,Jianxuan Yang,Zhao Wang,Jian Luan
### Background
现有的音效编辑方法主要依赖于低层信号处理或粗略的文本提示，这导致了灵活性有限和音质不理想的问题。现有方法无法精细地编辑视频中的音频轨。
### Innovation
AV-Edit 是一个结合视觉、音频和文本语义的生成音效编辑框架，通过专门设计的对比式音视频掩码自编码器（CAV-MAE-Edit）进行多模态预训练，学习对齐的跨模态表示。然后使用这些表示来训练一个编辑用的多模态扩散变换器（MM-DiT），这种模型能够移除与视频内容无关的声音并在基于相关性特征门控的训练策略下生成一致的声音元素。
### Conclusion
实验结果表明，AV-Edit 能够根据视觉内容生成高质量的声音并进行精确修改，达到了音效编辑领域的最先进水平，且在音频生成领域表现出强烈的竞争力。
## 519. `cs.CV` - TraceGen：在3D轨迹空间进行世界建模使跨肢体视频学习成为可能 [PDF](https://arxiv.org/pdf/2511.21690), [HTML](https://arxiv.org/abs/2511.21690)
### Authors
Seungjae Lee,Yoonkyo Jung,Inkook Chun,Yao-Chih Lee,Zikui Cai,Hongjia Huang,Aayush Talreja,Tan Dat Dao,Yongyuan Liang,Jia-Bin Huang,Furong Huang
### Background
从少量演示中在新的机器人平台和新场景中学习新的机器人任务仍然具有挑战性。尽管关于其他肢体形态——人类和其他机器人——的视频普遍充足，但肢体形态、摄像头和环境的不同阻碍了这些视频的直接使用。
### Innovation
引入了统一的符号表示——紧凑的3D“轨迹空间”场景级轨迹，能够在跨肢体、跨环境和跨任务视频中进行学习。开发了TraceForge数据流水线将异构的人类和机器人视频转换为一致的3D轨迹，生成包含123K视频和1.8M观察-轨迹-语言三元组的大型数据集。基于此 corpus 预训练了一个可迁移的3D运动先验，仅用五个目标机器人视频，TraceGen在四个任务中的成功率达到了80%，且比最先进的基于视频的世界模型快50-600倍的推理速度。即使只有五个手持手机拍摄的未经校准的人类示范视频，它也能在真实机器人上达到67.5%的成功率，展示了其在无需依赖物体检测器或像素空间生成的情况下跨越不同肢体形态的适应能力。
### Conclusion
通过在3D轨迹空间中建模，TraceGen实现了跨肢体视频的学习能力，即使数据稀少，也能在机器人任务学习中取得显著进展。
## 520. `cs.CV` - 基于潜在扩散模型的半透明攻击：后验塌陷攻击 [PDF](https://arxiv.org/pdf/2408.10901), [HTML](https://arxiv.org/abs/2408.10901)
### Authors
Zhongliang Guo,Chun Tong Lei,Lei Fang,Shuai Zhao,Yifei Qian,Jingyu Lin,Zeyu Wang,Cunjian Chen,Ognjen Arandjelović,Chun Pong Lau
### Background
最近在潜在扩散模型（LDMs）方面取得的进展彻底改变了图像的合成与操控，但是随之带来了一个重大问题：数据被不当使用和侵犯知识产权。尽管对抗攻击已经广泛被研究作为防止生成AI滥用的方法，但是现有的方法高度依赖特定模型的知识，计算成本也相当高。
### Innovation
作者受变分自编码器（VAE）训练中观察到的后验塌陷现象启发，提出了后验塌陷攻击（PCA），它通过VAE编码器的统一损失函数实现两种类型的塌陷以达到防止图像未经授权操控的目的。PCA只需访问VAE编码器，这占LDM参数的不到4%，并且能在文本条件化发生之前作用于VAE编码器，从而不需要现有方法所需的空缺指令优化，使PCA具备更强的传输能力并在各种VAE基LDM变体中表现优异。
### Conclusion
实验表明PCA在保护效果、计算效率（运行时间和VRAM）以及对VAE基LDM变体的一般化等多个方面都优于现有技术。
## 521. `cs.CV` - 基于SAM的区域可分辨先验的面向恢复的目标视频帧插值 [PDF](https://arxiv.org/pdf/2312.15868), [HTML](https://arxiv.org/abs/2312.15868)
### Authors
Yan Han,Xiaogang Xu,Yingqi Lin,Jiafei Wu,Zhe Liu,Ming-Hsuan Yang
### Background
当前的目标视频帧插值(VFI)方法中，相邻帧之间的运动估计起着至关重要的作用，但由于难以精确识别相邻帧之间的对应区域，现有的运动估计准确性仍是个挑战。因此，在进行运动估计之前，通过区分不同区域以提升精度变得尤为重要。
### Innovation
本文介绍了一种新颖的方法，利用开放世界分割模型（例如SAM2）对帧进行分割，从而获得不同帧中的区域可分辨先验（RDPs），并将RDPs表示为空间可变的高斯混合模型，适用于统一模态下任意数量的区域区分。这些RDPs通过设计的层级区域注意特征融合模块（HRFFM）被整合进现有的基于运动的目标视频帧插值方法中，利用RDP引导的特征归一化（RDPFN）以残差学习的方式进行运动估计。HRFFM使VFI编码器中的特征在相邻帧匹配区域内具有相似的表示形式，从而提高了中间帧的合成效果。
### Conclusion
通过HRFFM和RDP的结合，本文实验结果证实，VFI性能在多种场景中得到了持续提升。
## 522. `cs.CV` - 通过弥散、漫步和切割进行无监督分割 [PDF](https://arxiv.org/pdf/2412.04678), [HTML](https://arxiv.org/abs/2412.04678)
### Authors
Daniela Ivanova,Marco Aversa,Paul Henderson,John Williamson
### Background
本文提出了一种使用预训练文字转图像扩散模型特征的无监督图像分割方法。背景信息包括当前无监督分割方法的挑战和局限性，例如需要大量的标注数据和手动调整参数的问题。
### Innovation
该方法创新之处在于使用预训练的自注意力机制来构建边缘矩阵，并通过随机漫步和切分（Normalized Cuts）方法进行图像分割。这种方法无需额外训练，且能够捕捉长距离特征关系，从而实现层次式的细粒度分割。
### Conclusion
实验结果显示，该方法在零样本无监督分割任务上优于现有所有方法，在COCO-Stuff-27和Cityscapes数据集上取得了最先进的结果。此外，研究还提出了一种自动确定切分成本的标准，进一步简化了算法的实施过程。
## 523. `cs.CV` - 一种基于微观仿真向视觉交通信号控制的简单框架 [PDF](https://arxiv.org/pdf/2403.06884), [HTML](https://arxiv.org/abs/2403.06884)
### Authors
Pan He,Quanyi Li,Xiaoyong Yuan,Bolei Zhou
### Background
交通信号控制（TSC）对于减少交通拥堵、提高交通流畅度、减少闲置时间和降低CO2排放至关重要。传统的基于特征的方法依赖于经验法则和预定义的特征，而视觉方法则较少依赖这些因素，为端到端的学习和交通信号优化带来了潜力。
### Innovation
本文引入了一个基于视觉的交通信号控制框架TrafficDojo，通过将宏微观交通流与MetaDrive 3D驾驶模拟器结合，提供了一种多功能的交通环境，以深入分析和全面评估在各种交通条件和场景下的交通信号控制器。本文建立了包括传统方法和强化学习在内的基线算法，开启了视觉交通信号控制领域的新研究机会。
### Conclusion
本文的工作为视觉交通信号控制的设计和开发提供了新的视角，并开辟了新的研究机会。
## 524. `cs.CV` - 多奖励GRPO在大规模稳定和语调单代码簿TTS LLM中的应用 [PDF](https://arxiv.org/pdf/2511.21270), [HTML](https://arxiv.org/abs/2511.21270)
### Authors
Yicheng Zhong,Peiji Yang,Zhisheng Wang
### Background
近年来，大型语言模型（LLMs）在文本到语音（TTS）合成中的应用取得了显著进展，推动了自回归框架的出现，这些框架将语音表示为离散的编码器令牌序列。在这些框架中，单代码本TTS LLM由于其紧凑性和流式传输能力受到重视，能够同时建模语义和声学。然而，尽管这些模型具有高效性，它们往往会表现出不稳定的速度、说话者偏移以及自然度下降等问题。
### Innovation
本文提出了一种多奖励组相对策略优化（GRPO）框架，专门用于直接优化单代码本TTS LLM的令牌生成策略。该框架不仅采用了标准的可读性和说话者相似性目标，而且还整合了三种基于规则的奖励：持续时间一致性惩罚、熵正则化奖励用于解码稳定性和LMM标注的语调对齐奖励，明确监督节奏。此外，通过外部推理LMM利用上下文学习预测多种可能的停顿结构，为GRPO训练提供基线偏好监督信号。
### Conclusion
我们进一步使用流匹配（FM）解码器对优化的自回归主干进行测试，并观察到一致的额外增益，这表明我们的强化优化提高了内在的自回归策略。我们还对数据大小和模型规模进行了扩展性分析，结果表明所提出的方法在单代码本TTS LLM中始终增强节律稳定性、说话者相似性和整体语音自然度。
## 525. `cs.CV` - Activator: GLU激活函数作为视觉变换器的核心组件 [PDF](https://arxiv.org/pdf/2405.15953), [HTML](https://arxiv.org/abs/2405.15953)
### Authors
Abdullah Nazhat Abdullah,Tarkan Aydin
### Background
变换器架构因其在各种深度学习任务中的成功，特别是在自然语言处理中的成就，特别是在大型语言模型的发展取得重大进展。视觉研究者和从业者对变压器架构产生了广泛兴趣，这一兴趣推动了视觉任务的进步，并为多任务和多模态深度学习架构的发展打开了大门。然而，传统的变压器架构依赖于成本高昂的缩放点积注意机制和softmax激活函数，这在训练和推理过程中都需要庞大的计算资源。
### Innovation
本文研究了用包含门线性单元(GLU)激活函数结构的网络替换变压器架构中常用的MLP和注意机制，旨在降低计算成本。等量化的实验评估显示，提出的修改方案，在降低了计算复杂性的同时，提供了与选定基准架构竞争力的表现。
### Conclusion
实验结果强有力地支持了本文的目标，即尽可能使用GLU基础上的MLP，为传统的MLP和注意机制提供一种更有效且具备能力的替代方案，在设计变压器架构的核心组件中起到了重要作用。
## 526. `cs.CV` - Active Negative Loss: 一种稳健的噪声标签学习框架 [PDF](https://arxiv.org/pdf/2412.02373), [HTML](https://arxiv.org/abs/2412.02373)
### Authors
Xichen Ye,Yifan Wu,Yiqi Wang,Xiaoqiang Li,Weizhong Zhang,Yifan Chen
### Background
深度监督学习已经在广泛的任务中取得了显著的成功，但在面对嘈杂标签时仍然容易发生过拟合。尽管最近提出的主动被动损失（APL）通过采用了平均绝对误差（MAE）等稳健的损失函数来解决这个问题，但在大型数据集中的训练变得艰难，特别是由于MAE对干净和嘈杂样本给予同等关注，这影响了收敛速度。
### Innovation
本文引入了一种新的损失函数类，称为归一化负损失函数（NNLFs），作为APL框架中的被动损失函数。NNLFs在处理MAE的局限性方面表现出色，能更专注于记忆中的干净样本。新的损失函数被引入到APL中，提出了一个新的框架叫主动负损失（ANL）。此外，提出了基于熵的正则化技术来缓解非对称噪声场景下的标签不平衡问题。
### Conclusion
广泛实验证明，采用新损失函数的ANL框架在各种噪声标签类型和图像分割任务中表现出更好的或可比的性能。源代码可以通过提供的链接访问。
## 527. `cs.CV` - 开放词汇量单目3D物体检测 [PDF](https://arxiv.org/pdf/2411.16833), [HTML](https://arxiv.org/abs/2411.16833)
### Authors
Jin Yao,Hao Gu,Xuweiyi Chen,Jiayun Wang,Zezhou Cheng
### Background
现有3D物体检测技术要么依赖昂贵的传感器（如LiDAR）或多视图布局，要么局限于有限的封闭词汇表设置，限制了其适用范围。此外，现存3D边界框标注稀缺，现有的数据集存在缺标注和语义模糊等问题，如桌子和书桌的语义模糊。
### Innovation
提出了一个新颖的任务，即从单个RGB图像中在度量3D空间中检测任何类别物体的开词汇量单目3D检测。该论文提出了一个框架整合预训练的2D和3D视觉基础模型以减少对3D监督的依赖性，并设计了一种新的评价指标考虑了标注问题。
### Conclusion
该方法在未知类别零样本3D检测和在已见类别上的检测中达到了最先进的性能。我们希望这种方法为未来研究提供一个强大的基线，我们的评估协议为未来的研究建立了可靠的基准。
## 528. `cs.CV` - SOAP: 提高少量样本动作识别中时空关系和运动信息捕获 [PDF](https://arxiv.org/pdf/2407.16344), [HTML](https://arxiv.org/abs/2407.16344)
### Authors
Wenbo Huang,Jinghui Zhang,Xuwei Qian,Zhen Wu,Meng Wang,Lei Zhang
### Background
高帧率（HFR）视频的动作识别能够精细表达动作表达，但会减少时空关系和运动信息密度。因此，传统数据驱动的训练需要大量的视频样本。然而，在现实场景中样本往往不充足，从而推动了少量样本动作识别（FSAR）的研究。现有的FSAR方法通过在空间特征提取后进行时间对齐来建立视频样本的时空关系，但在相邻帧之间仅以狭窄视角捕捉运动信息，忽视了运动信息的密度，导致运动信息捕获不足。
### Innovation
本文提出了一种新的模块化架构——时空框架元增强器（Spatio-temporal frAme tuPle enhancer, SOAP），用于FSAR。该架构通过时空特征通道之间的时序连接以及frame tuples（包含多帧且比相邻帧提供更多运动信息）来捕获全面的运动信息。此外，使用不同帧数量的frame tuples提供了更广阔的视角。SOAP-Net模型在SthSthV2、Kinetics、UCF101和HMDB51等基准上取得了新的最佳性能，实验结果验证了SOAP的竞争性、可插拔性、泛化能力和鲁棒性。
### Conclusion
SOAP模型在多种关键指标上达到了最佳效果，证明了其对少量样本动作识别中的时空关系和运动信息捕获的有效提升，进一步验证了其在FSAR中的竞争力、可插拔性、泛化能力和鲁棒性。
## 529. `cs.CV` - Gen-3Diffusion: 通过2D与3D扩散协同实现基于图像的真实感图像到三维生成 [PDF](https://arxiv.org/pdf/2412.06698), [HTML](https://arxiv.org/abs/2412.06698)
### Authors
Yuxuan Xue,Xianghui Xie,Riccardo Marin,Gerard Pons-Moll
### Background
从单张RGB图像生成逼真的3D对象及穿戴各类衣服的头像是一个引人注目但具有挑战性的问题。由于其反问题的本质，最近的工作利用了大规模数据集预训练的强大2D扩散模型。尽管2D扩散模型表现出强大的泛化能力，但生成的多视角图像无法保证3D一致性。
### Innovation
我们提出了一个名为Gen-3Diffusion的方法，通过2D与3D扩散的协同作用实现图像到三维的生成。采用了预训练的2D扩散模型和一个3D扩散模型，并设计了一种同步这两个扩散模型的过程，在训练和采样阶段同步。2D与3D扩散模型之间的协同效应带来了两大优势：1）2D协助3D泛化：预训练的2D模型对未见过的图像有强大的泛化能力，为3D扩散模型提供了强大的先验形状信息；2）3D协助2D多视角一致性：3D扩散模型提高了2D多视角采样过程的3D一致性，导致更准确的多视角生成。我们通过大量实验验证了这一构想，在基于图像的对象和穿戴头像生成任务中展示出高度保真的几何形状和纹理。广泛消融实验验证了我们的设计选择，并展示了对各种服装和复合形状的强泛化能力。
### Conclusion
我们的方法生成了具有高保真几何形状和纹理的真实感3D对象和头像。广泛的消融实验也验证了我们的设计选择，并展示了对多样化服装和复合形状的强泛化能力。我们的代码和预训练模型将在如下的链接中公开。
## 530. `cs.CV` - 面向面部编辑的一致可控图像合成 [PDF](https://arxiv.org/pdf/2502.02465), [HTML](https://arxiv.org/abs/2502.02465)
### Authors
Mengting Wei,Tuomas Varanka,Yante Li,Xingxun Jiang,Huai-Qian Khor,Guoying Zhao
### Background
传统的面部编辑方法通常基于生成对抗网络（GAN），而最近的研究重心转向了扩散模型，因为它们在图像重建方面取得了成功。尽管如此，扩散模型仍然面临控制特定属性和保持其他未改变属性（尤其是身份特征）一致性的挑战。本研究的背景是解决这些问题，以及实现面部图像编辑的更便捷操作。
### Innovation
提出了一个名为RigFace的新方法，该方法利用了稳定的扩散（SD）模型和粗糙的3D面部模型，以控制肖像照片的光照、面部表情和头部姿态。该方法具体包括：一个空间属性编码器，提供背景、姿态、表情和光照的精准且解耦的条件；一种高一致性面部融合方法，将身份特征从身份编码器转移到预训练的SD模型的去噪UNet中；以及一个属性调节器，将这些条件注入到去噪UNet。该模型在身份保留和写实度方面优于现有的面部编辑模型。
### Conclusion
我们的研究结果表明，提出的RigFace方法在身份保留和图像的真实感方面取得了可比甚至优于现有面部编辑模型的性能。
## 531. `cs.CV` - 图像增强中贝叶斯神经网络在一对一至多映射的应用 [PDF](https://arxiv.org/pdf/2501.14265), [HTML](https://arxiv.org/abs/2501.14265)
### Authors
Guoxi Huang,Qirui Yang,Ruirui Lin,Zipeng Qi,David Bull,Nantheera Anantrasirichai
### Background
在图像增强任务中，如低光照和水下图像增强，由于多变的动态拍摄条件，退化图像可能对应多个合理的目标图像。这自然地导致了一个一对一至多的映射问题。
### Innovation
本文提出了一个贝叶斯增强模型（BEM），引入了贝叶斯神经网络（BNN），以捕捉数据的不确定性并生成多样化的输出。此外，引入了BNN-DNN框架：首先使用BNN在低维空间中建模一对一至多的映射，然后使用确定性神经网络（DNN）来细化图像的细部。
### Conclusion
在多个低光照和水下图像增强基准上进行的广泛实验表明，本方法的有效性。
## 532. `cs.CV` - 通过利用合成数据实现交互式遮挡边界估计 [PDF](https://arxiv.org/pdf/2408.15038), [HTML](https://arxiv.org/abs/2408.15038)
### Authors
Lintao Xu,Chaohui Wang
### Background
遮挡边界（OBs）在二维图像中几何定位遮挡事件，并为场景理解提供关键线索。本文通过系统研究交互式遮挡边界估计（IOBE），介绍了一种新颖的多擦除引导的深度学习框架——MS³PE，该框架通过两个关键创新来推进IOBE：（1）直观的多擦除交互机制；（2）通过多尺度条带卷积增强的3-编码路径网络。
### Innovation
提出了MS³PE，这是一个新颖的多擦除引导的深度学习框架，通过以下创新来推进IOBE：（1）直观的多擦除交互机制；（2）通过多尺度条带卷积增强的3-编码路径网络。此外，为了应对真实世界标注数据稀缺的问题，提出使用合成数据进行IOBE模型的训练，并开发了Mesh2OB，这是一种自动化的工具，用于从具有自遮挡的3D场景生成准确的地面真值OB，从而构建了OB-FUTURE合成基准，促进了通用训练而不需领域适应。
### Conclusion
提出的MS³PE超越了来自七个最新交互式分割方法的适应性基线。通过我们的真实用户实验展示了IOBE基准构建的强大潜力，并引入了OB-LIGM，这是一个包含120个精心标注的高分辨率图像的高质量实时基准，促进了OB研究的评估标准。相关源代码和资源可在指定网址获取。
## 533. `cs.CV` - LASER: 唇部地标辅助鲁棒性说话者检测 [PDF](https://arxiv.org/pdf/2501.11899), [HTML](https://arxiv.org/abs/2501.11899)
### Authors
Le Thien Phuc Nguyen,Zhuoran Yu,Yong Jae Lee
### Background
主动说话者检测（ASD）旨在识别复杂视觉场景中的说话者。当前，现有的ASD模型在唇部运动和音频不一致时容易误分类非说话实例。鉴于此，提出了一种名为Lip landmark Assisted Speaker dEtection for Robustness (LASER) 的方法，通过在训练中明确引入唇部地标来引导模型关注与语音相关的区域。
### Innovation
LASER通过引入辅助一致性损失，将唇部的特征和面部的特征结合起来，在测试时不需依赖地标检测器，从而提高了模型在低分辨率和遮挡等失败情况下的鲁棒性。此外，Laser-bench数据库的引入使得模型在不同噪音水平下的鲁棒性得到了进一步评估。
### Conclusion
Laser在多种ASD基准测试数据集上表现超过了现有前沿模型，尤其是在噪声较重的部分，性能提升显著，表明了其在实际音频挑战下的强大鲁棒性。
## 534. `cs.CV` - 无配对标注数据：端到端自监督学习在无人机视角地理定位中的应用 [PDF](https://arxiv.org/pdf/2502.11381), [HTML](https://arxiv.org/abs/2502.11381)
### Authors
Zhongwei Chen,Zhao-Xu Yang,Hai-Jun Rong,Guoqi Li
### Background
无人机视角地理定位（DVGL）旨在通过检索带有GPS标签的卫星图像来实现无人机的准确定位。然而，现有的大多数方法严重依赖于严格配对的无人机-卫星图像进行监督学习。当目标区域发生变化时，通常需要新的配对样本来适应分布变化。这导致了标注成本高和这些方法在迁移性方面的限制，极大地阻碍了DVGL在开放世界场景中的实际部署。
### Innovation
本文提出了一种新的端到端自监督学习方法，该方法使用了一个浅层骨干网络，并称为动态记忆驱动和邻域信息学习（DMNIL）方法。它采用了聚类算法生成伪标签，并采用双路径对比学习框架来学习辨别性的视图内部表示。DMNIL包括动态层次记忆学习（DHML）模块和信息一致性演进学习（ICEL）模块。DHML模块结合短期和长期记忆以增强视图内部特征的一致性和可区分性，同时ICEL模块利用邻域驱动的动态约束机制系统地捕捉跨视图的语义相关性，从而提高跨视图特征对齐。为了进一步稳定和增强自监督训练过程，引入了一种伪标签增强策略来提高伪监督的质量。在三个公开基准数据集上的大量实验表明，提出的方法始终优于现有的自监督方法，并且甚至超越了一些最先进的监督方法。
### Conclusion
我们的实验结果说明，在无需配对标注数据的情况下，DMNIL方法在无人机视角地理定位中表现出优越的性能，并且可以提高自监督训练的质量和效率。
## 535. `cs.CV` - Class-Independent Increment: An Efficient Approach for Multi-label Class-Incremental Learning [PDF](https://arxiv.org/pdf/2503.00515), [HTML](https://arxiv.org/abs/2503.00515)
### Authors
Chenhao Ding,Songlin Dong,Zhengdong Zhou,Jizhou Han,Qiang Wang,Yuhang He,Yihong Gong
### Background
当前关于类增量学习的研究主要集中在单标签分类任务上。然而，实际应用场景中常常涉及多标签场景，如图像检索和医学影像分析。因此，本文聚焦于具有挑战性的但实际意义重大的多标签类增量学习（MLCIL）问题。除了灾难性遗忘的挑战，MLCIL还遇到了特征混淆的问题，包括会话间和特征内混淆。
### Innovation
本文提出了一个名为class-independent increment（CLIN）的新颖多标签类增量学习方法。不同于现有方法提取图像级特征，我们提出了一种class-independent incremental网络（CINet）来提取多标签样本的类级嵌入。CINet通过构建特定于类的token学习和保留不同类的知识。在此基础上，我们开发了两种新的损失函数，分别优化特定于类的token和类级嵌入的学习，旨在区分新旧类，进一步缓解特征混淆的问题。
### Conclusion
我们在MS-COCO和PASCAL VOC数据集上的大量实验表明，我们的方法能够提高多标签类增量学习任务中的识别性能并缓解遗忘问题。
## 536. `cs.CV` - 系统性评估与在手术视频分析中Segment Anything Model的指导原则 [PDF](https://arxiv.org/pdf/2501.00525), [HTML](https://arxiv.org/abs/2501.00525)
### Authors
Cheng Yuan,Jian Jiang,Kunyi Yang,Lv Wu,Rui Wang,Zi Meng,Haonan Ping,Ziyu Xu,Yifan Zhou,Wanli Song,Hesheng Wang,Yueming Jin,Qi Dou,Yutong Ban
### Background
手术视频分割对于AI理解手术中的空间-时间动态至关重要，但模型性能受到标注数据有限的制约。SAM2模型在自然视频上预训练，具有潜在的零样本手术分割能力，但在复杂手术环境中的应用（如组织变形和手术器械变化）尚未得到探索。
### Innovation
首次全面评估了SAM2的零样本能力在9个手术数据集（17种手术类型）上的应用，涵盖腹腔镜、内窥镜和机器人手术程序。评估了不同的提示（点、框、掩码）和微调（密集、稀疏）策略，分析了在手术挑战下的鲁棒性和跨程序与解剖结构的泛化能力。研究发现，尽管在结构化场景中（如手术器械分割、多器官分割和场景分割）展现了显著的零样本适应性，但在动态手术条件下性能各异，突显了处理时间连贯性和领域特定伪影的不足。
### Conclusion
这些结果指明了对于手术数据科学领域自适应数据高效解决方案的未来研究路径。
## 537. `cs.CV` - 室内导航辅助中的自适应物体检测：实时算法性能评估 [PDF](https://arxiv.org/pdf/2501.18444), [HTML](https://arxiv.org/abs/2501.18444)
### Authors
Abhinav Pratap,Sushant Kumar,Suchinton Chakravarty
### Background
本研究针对视力受损个体辅助技术中对准确和高效的物体检测的需求。研究在室内导航辅助的背景下，评估了YOLO、SSD、Faster R-CNN和Mask R-CNN四种实时物体检测算法的性能。
### Innovation
研究使用Indoor Objects Detection数据集，分析了检测准确性、处理速度和对室内环境的适应性，揭示了精度与效率之间的权衡，并提供了选择适合实时辅助导航的最佳算法的见解。此项研究促进了自适应机器学习应用的发展，提高了视力受损个体的室内导航解决方案，促进了无障碍环境的建设。
### Conclusion
研究结果对于选择适用于实时辅助导航的最佳算法具有重要意义，有助于增强室内导航解决方案，推动无障碍环境的改善。
## 538. `cs.CV` - Filter Like You Test: 数据驱动的数据过滤用于CLIP预训练 [PDF](https://arxiv.org/pdf/2503.08805), [HTML](https://arxiv.org/abs/2503.08805)
### Authors
Mikey Shechter,Yair Carmon
### Background
该研究针对的是大规模视觉语言数据集的筛选问题，特别是用于预训练模型（如CLIP）的筛选过程。当前的数据集往往包含大量数据点，需要有效的算法来挑选有用的样本作为预训练数据，以便提高模型的性能。
### Innovation
该论文提出了一种名为FLYT（Filter Like You Test）的算法，它能够通过学习每个数据点作为预训练示例的有效性来进行筛选。FLYT通过从下游任务训练集中学习特征的重要性来训练评分模型。此外，还提出了M-FLYT（Mixing-FLYT），使用不同评分方法生成的每个示例的分数作为特征，学习将这些分数统一成一个综合得分。同时，引入了Soft Cap Sampling（SCS）策略来确保过滤后的预训练数据集中样本的均匀分布。
### Conclusion
使用上述方法，论文在DataComp的中等规模筛选基准上实现了40.1%的ImageNet零样本准确率，比之前所有结果提高了2%，且比仅使用公共资源的方法提高了5.5%。此外，该方法在40项DataComp评估任务中的平均得分达到了37.7%，超越了先前仅使用公共资源的方法0.4%。
## 539. `cs.CV` - CAPability: 一种评估视觉描述准确性和详尽性的综合基准 [PDF](https://arxiv.org/pdf/2502.14914), [HTML](https://arxiv.org/abs/2502.14914)
### Authors
Zhihang Liu,Chen-Wei Xie,Bin Wen,Feiwu Yu,Jixuan Chen,Pandeng Li,Boqiang Zhang,Nianzu Yang,Yinglu Li,Zuan Gao,Yun Zheng,Hongtao Xie
### Background
随着现代多模态大型语言模型（MLLMs）的出现，现有的视觉描述基准已变得过时。传统的简短地面真实句子和评价指标无法有效评估详细的视觉描述。近年来的努力试图通过关注关键词提取或对象中心评估来解决这一问题，但这些方法仍局限于模糊视角或对象视角的分析，且未能涵盖完整的视觉元素。
### Innovation
本文提出了一种名为CAPability的综合多视角基准，用于评估跨12个维度（涵盖六个关键视角）的视觉描述。该基准包括近1.1万张由人工标注的图像和视频，其中包含视觉元素标注，用于评估生成的描述。CAPability通过精密度和命中率指标稳定地评估描述的准确性和完整性，并通过将注释转换为问答对，引入了一个启发式指标 $Kbar{T}$，该指标表明问答能力与描述生成能力之间存在显著差距。该工作从多维度提供了对MLLMs描述能力的全面分析，指出了其优势和弱点，以指导未来研究在特定方面提升其能力。
### Conclusion
我们的研究工作提供了一个全面的MLLMs描述能力分析，通过识别他们在不同维度中的优势和不足，指导未来的研究专注于特定方面的能力提升。
## 540. `cs.CV` - OuroMamba：一种无需数据的视觉Mamba量化学框架 [PDF](https://arxiv.org/pdf/2503.10959), [HTML](https://arxiv.org/abs/2503.10959)
### Authors
Akshat Ramachandran,Mingyu Lee,Huan Xu,Souvik Kundu,Tushar Krishna
### Background
本文介绍了一种名为OuroMamba的数据无感知模型后训练量化（DFQ）方法，专门针对基于视觉Mamba模型（VMMs）。研究背景在于，当前的DFQ方法难以应用于VMMs中，主要因为VMMs的循环状态转换限制了长期交互的捕捉，导致合成数据具有较弱的语义；此外，VMM的激活表现不随时间步骤动态变化，这使得现有的静态后训练量化学方法失效。
### Innovation
OuroMamba提出了一个两阶段框架来解决上述问题：首先，OuroMamba-Gen通过在潜在状态空间通过邻域交互生成的块级VMM特征进行对比学习，生成具有丰富语义和意义的合成数据；其次，OuroMamba-Quant采用了混合精度量化，并在推理过程中进行了轻量级动态异常值检测。此外，还提出了一种基于阈值的激活异常通道选择策略，该策略会在每个时间步骤更新。
### Conclusion
广泛的实验表明，OuroMamba在多种量化设置下超过了现有的基于数据的后训练量化技术，达到了最先进的性能。此外，通过高效的GPU内核实现，能够在实际环境中实现高达2.36倍的延迟速度提升。代码和合成数据集已在此处提供：this https URL
## 541. `cs.CV` - 从有限标签到开放领域：无人机视角地理定位的一种高效学习方法 [PDF](https://arxiv.org/pdf/2503.07520), [HTML](https://arxiv.org/abs/2503.07520)
### Authors
Zhongwei Chen,Zhao-Xu Yang,Hai-Jun Rong,Jiawei Lang,Guoqi Li
### Background
传统的监督无人机视角地理定位（DVGL）方法依赖于已配对的训练数据，难以学习来自无配对数据的跨视图相关性。这种方法在部署到新领域时需要重新获取配对数据并进行模型适应，这显著增加了计算负担。现有的无监督方法能够在跨视角相似性基础上生成伪标签以推断配对关系，但地理相似性和空间连续性常导致跨地点的不同视觉特征混淆，这种特征混淆削弱了伪标签生成的可靠性，进而对优化过程产生负面影响。已有监督和无监督无人机视角地理定位方法均面临上述挑战。
### Innovation
本文提出了一种带有有限监督的新的跨域不变知识传输网络（CDIKTNet），其架构包括一个跨域不变子网络（CDIS）和一个跨域传输子网络（CDTS）。CDIS旨在从少量已配对的数据中学习跨视图的结构和空间不变性，作为先验知识，它为无配对数据的共享特征空间赋予类似的隐含跨视图关联，减少特征混淆。CDTS则采用双路径对比学习来进一步优化每个子空间的同时，保持共享特征空间中的一致性。实验结果表明，在全监督条件下，CDIKTNet的性能优于现有监督方法，并在少样本和跨域初始化场景下超越现有无监督方法。
### Conclusion
综合实验结果表明，采用有限监督的CDIKTNet方法在无人机视角地理定位任务中具有优异的表现。与现有监督方法相比，在全监督条件下，该方法表现出优越性能；在少样本和跨域初始化场景下，CDIKTNet进一步超越了现有无监督方法，证明了该方法在不同领域应用的有效性和高效性。
## 542. `cs.CV` - 从单张运动模糊图像估计相机运动：图像作为IMU [PDF](https://arxiv.org/pdf/2503.17358), [HTML](https://arxiv.org/abs/2503.17358)
### Authors
Jerred Chen,Ronald Clark
### Background
在许多机器人和VR/AR应用中，快速的相机运动会导致严重的运动模糊，这会导致现有相机位姿估计方法失效。因此，当前的方法通常将运动模糊视为不需要的缺陷，而没有充分利用其作为运动估计的丰富线索。
### Innovation
本文提出了一种新颖的框架，能够利用运动模糊作为运动估计的丰富线索，而不是将其视为不需要的缺陷。该方法通过从单张运动模糊图像直接预测稠密的运动流场和单目深度图工作。之后，通过小运动假设下的线性最小二乘问题恢复瞬时相机速度。该方法能够生成类似IMU的测量结果，有效捕捉快速和激烈的相机运动。模型通过构建包含从ScanNet++v2派生的真实合成运动模糊的大规模数据集进行训练，并通过端到端地在真实数据上进行训练进一步优化。
### Conclusion
在现实世界基准上的广泛评估表明，该方法在角速度和线速度估计方面达到了最先进的效果，超越了现有的方法如MASt3R和COLMAP。
## 543. `cs.CV` - RobustMerge：具有方向稳健性的参数高效模型合并方法 [PDF](https://arxiv.org/pdf/2502.17159), [HTML](https://arxiv.org/abs/2502.17159)
### Authors
Fanhu Zeng,Haiyang Guo,Fei Zhu,Li Shen,Hao Tang
### Background
利用预训练模型的细调生成特定任务的专家模型很常见。将多个模型合并成一个通用模型以增强多任务能力并避免数据泄露也很流行。然而，随着数据量和模型规模的扩大，参数高效的调整方法已成为一种有效方法。尽管有些方法针对高效合并进行了研究，但现有的用于全面调优的方法在高效合并中效果不佳。因此，研究者们分析了低秩分解并发现合并高效模块时的方向稳健性至关重要，同时揭示了弥补显著奇异值之间的差距对方向稳健性有贡献。
### Innovation
提出了RobustMerge，这是一种无需训练的参数高效的合并方法，通过互补的参数调整来维持方向稳健性。具体来说，RobustMerge通过(1)从参数间关系中修剪参数和缩放系数以维持奇异值方向的稳定性，并保持远离任务干扰；(2)跨任务规范化以增强未见过任务的泛化能力。
### Conclusion
在多样性多模态任务的基准测试上进行了实验，验证了RobustMerge方法的出色性能和泛化能力。此外，深入的研究和广泛的分析进一步证明了该方法的有效性。代码已发布。
## 544. `cs.CV` - Stream and Query-guided Feature Aggregation for Efficient and Effective 3D Occupancy Prediction [PDF](https://arxiv.org/pdf/2503.22087), [HTML](https://arxiv.org/abs/2503.22087)
### Authors
Seokha Moon,Janghyun Baek,Giseop Kim,Jinkyu Kim,Sunwook Choi
### Background
3D占用预测已成为自主驾驶中的关键感知任务，因为它可以实现全面的场景理解。尽管最近的方法通过多帧融合引入时空信息来增强这种理解，但在精度和计算成本之间存在权衡：密集的体素表示提供高度准确性但计算成本高，而稀疏表示则提高了效率但损失了空间细节。
### Innovation
该论文提出了一种名为DuOcc的方法，利用双聚合策略保留密集体素表示以保持空间保真度，同时保持高效率。DuOcc由两个关键组件组成：(i) 基于流的体素聚合，随着时间累积体素特征并对其进行细化以抑制变形引起的失真，保持占用和空闲空间之间的清晰分离；(ii) 查询引导的聚合，通过选择性地将实例级查询特征注入由动态物体占据的体素区域来补充体素累积的局限性。
### Conclusion
在广泛使用的Occ3D-nuScenes和SurroundOcc数据集上的实验表明，DuOcc在实时设置中达到了最先进的性能，与以前的方法相比，内存使用量降低了40%以上。
## 545. `cs.CV` - PointNSP: 采用下一尺度层次细节预测的自回归3D点云生成 [PDF](https://arxiv.org/pdf/2503.08594), [HTML](https://arxiv.org/abs/2503.08594)
### Authors
Ziqiao Meng,Qichao Wang,Zhiyang Dou,Zixing Song,Zhipeng Zhou,Irwin King,Peilin Zhao
### Background
自回归的点云生成长期以来在质量上落后于基于扩散的方法。性能差距源于自回归模型在固有的无序点集上人为地施加了顺序关系，迫使形状生成按局部预测的序列进行。这种顺序偏差强调了短程连续性，但削弱了模型捕捉长程依赖性的能力，阻碍了它对全局结构属性（如对称性、一致拓扑和大规模几何规则性）的约束。
### Innovation
受形状建模中的层次细节（LOD）原则启发，本文提出了PointNSP，一种粗细渐进的生成框架，它在低分辨率下保持全局形状结构，并通过下一尺度预测范式在更高尺度下逐步细化细粒度几何结构。这种多尺度因子化使自回归目标与点集的置换不变性质相一致，从而促进了丰富的跨尺度交互并避免了固定的脆弱顺序。
### Conclusion
实验结果表明，PointNSP在自回归范式内首次达到了最先进的生成质量。此外，它在参数、训练和推理效率方面超越了强大的基于扩散的基本模型。在针对稠密生成的8,192点时，PointNSP的优势更加显著，证明了其可扩展性潜力。
## 546. `cs.CV` - FlowTok: 在文本和图像标记之间无缝流动 [PDF](https://arxiv.org/pdf/2503.10772), [HTML](https://arxiv.org/abs/2503.10772)
### Authors
Ju He,Qihang Yu,Qihao Liu,Liang-Chieh Chen
### Background
跨模态生成的核心在于不同模态之间的桥梁构建。传统的做法是将文本模态作为引导信号，逐步引导从高斯噪声到目标图像模态的去噪过程，而本文提出了一种更为直接的范式，即通过流匹配直接在文本和图像模态之间演进。这需要将两者投影到一个共享的潜在空间，但文本是高度语义化的，以1D标记编码，而图像则具有空间冗余性且以2D潜在嵌入表示，因此在潜在空间中将这两种不同表示流结合起来存在显著挑战。
### Innovation
本文提出了FlowTok，这是一个简约框架，能够无缝地在文本和图像之间流动，通过将图像编码为紧凑的1D标记表示。与之前的模型相比，这种设计在256分辨率下将潜在空间的大小减少了3.3倍，抛弃了复杂的条件机制或噪声调度。此外，FlowTok自然可以应用于图像到文本的生成，且其简洁的架构以紧凑的1D标记为中心，使其具有很高的内存效率，需要更少的训练资源，并能以更快的速度生成结果，同时其性能与最先进的模型相当。
### Conclusion
FlowTok以其紧凑的1D标记为中心的简化架构，使其具有高度的内存效率，需要较少的训练资源，并以更快的速度生成结果，同时能够达到与最先进的模型相当的性能。
## 547. `cs.CV` - LogicOCR：您的大型多模态模型在图文丰富的图像上的逻辑推理能力如何？ [PDF](https://arxiv.org/pdf/2505.12307), [HTML](https://arxiv.org/abs/2505.12307)
### Authors
Maoyuan Ye,Haibin He,Qihuang Zhong,Jing Zhang,Juhua Liu,Bo Du
### Background
近期大型多模态模型(LMMs)在光学字符识别(OCR)方面取得了重大进展，但它们在图文丰富的图像上的复杂逻辑推理能力仍被广泛忽视。论文中提到的论文旨在弥合此差距。
### Innovation
论文介绍了一个名为LogicOCR的新基准，它包含了2780个问题，分为两个子集：LogicOCR-Gen（包含1100个生成图像的多选题）和LogicOCR-Real（包含1680个精心设计的开放式问题，基于真实世界图像）。此外，还提出了一种无需训练的TextCue方法，这种方法通过利用模型的关注图和现有的文本分割专家来增强对包含重要文本线索的图像区域的感知，从而提高了解题准确性。
### Conclusion
论文通过多维度的分析揭示了大型多模态模型在逻辑推理中的关键洞察，例如测试时的缩放影响、输入模态差异以及视觉文本方向的敏感性。实验表明，TextCue方法在Chain-of-Thought设置下提高了1.8%的准确率。
## 548. `cs.CV` - Earth-Adapter: 使用混合频域适应来弥合地理空间领域差异 [PDF](https://arxiv.org/pdf/2504.06220), [HTML](https://arxiv.org/abs/2504.06220)
### Authors
Xiaoxing Hu,Ziyang Gong,Yupei Wang,Yuru Jia,Fei Lin,Dexiang Gao,Ke An,Jianhong Han,Zhuoran Sun,Gen Luo,Gen Luo,Xue Yang
### Background
参数效率微调（PEFT）是一种技术，允许我们调整强大的基础模型（FMs）应用于多样的下游任务，同时保持并释放它们的内在功能。然而，现有的PEFT方法往往针对自然图像设计，在遥感（RS）场景中应用时表现出色，主要原因是它们无法处理图像中的伪影影响，这种影响在RS图像特征中尤为严重。
### Innovation
本文引入了Earth-Adapter，这是首个专门针对RS伪影设计的PEFT方法。Earth-Adapter引入了一种新颖的混合频域适应过程，结合了混合适应器（MoA）与离散傅里叶变换（DFT）。通过使用DFT分解特征为不同频率分量，精确地将伪影与原始特征分离。MoA动态分配每个适应器专家的权重，允许在各种频率域中组合特征。这些简单而有效的做法使Earth-Adapter能够比之前的PEFT方法更有效地克服伪影引起的干扰，显著提升FMs在RS场景中的表现。
### Conclusion
在领域适应（DA）和领域泛化（DG）语义分割基准测试中，Earth-Adapter展示了其有效性。相比于baseline Rein，Earth-Adapter在DA基准测试中显著提高了9.0%的mIoU，在DG基准测试中提高了3.1%的mIoU。我们的代码将在此处公布：this https URL。
## 549. `cs.CV` - 带自适应对比扰动的解缠几何对齐以实现可靠的领域迁移 [PDF](https://arxiv.org/pdf/2505.15241), [HTML](https://arxiv.org/abs/2505.15241)
### Authors
Emma Collins,Myungseo wong,Kim Yun,Finn Kingston,Hana Satou
### Background
尽管在几何感知领域适应方面取得了进展，但目前的方法如GAMA仍然面临两个未解决的问题：(1) 任务相关信息和无关信息流形维度的解缠程度不足，(2) 刚性的扰动方案忽视了各类别间的对齐不对称性。
### Innovation
该研究提出了GAMA++，一种新的框架，引入了(i)潜在空间解缠以隔离与标签一致的流形方向与扰动因子，(ii)自适应对比扰动策略，该策略根据类别特定的流形曲率和对齐差异适应性地进行流形内外探索。此外，还提出了一种跨域对比一致性损失，以鼓励局部语义簇对齐同时保持域内多样性。
### Conclusion
GAMA++在DomainNet、Office-Home和VisDA基准上的标准和少样本设置下取得了最先进的结果，特别是在类别级别的对齐保真度和边界鲁棒性方面有显著改进。GAMA++为传输学习中的语义几何对齐设定了新的标准。
## 550. `cs.CV` - Diffusion-Denoised Hyperspectral Gaussian Splatting [PDF](https://arxiv.org/pdf/2505.21890), [HTML](https://arxiv.org/abs/2505.21890)
### Authors
Sunil Kumar Narayanan,Lingjun Zhao,Lu Gan,Yongsheng Chen
### Background
高光谱成像（HSI）在农业应用中广泛用于植物营养成分的非破坏性估计和样品营养元素的精确量化。近年来，诸如Neural Radiance Field（NeRF）的三维重建方法被用于构建HSI场景的隐式神经表示，这使得在每个空间位置渲染高光谱通道组成成为可能，有助于在空间和光谱上精确定位目标物体的营养成分。然而，这种方法在训练时间和渲染速度方面存在限制。
### Innovation
本文提出了扩散去噪高光谱高斯散点图（DD-HGS），该方法通过使用波长意识球谐量、基于Kullback-Leibler散度的光谱损失以及基于扩散的去噪器，增强了现有的三维高斯散点图（3DGS）方法，以实现整个波长范围内的三维显式高光谱场景重建。
### Conclusion
通过在Hyper-NeRF数据集上的各种真实世界高光谱场景上进行广泛评估，本文展示了DD-HGS的有效性。结果表明，DD-HGS在所有先前发表的方法中实现了最先进的性能。
## 551. `cs.CV` - 几何正则化迁移学习：基于在流形与离流形扰动 [PDF](https://arxiv.org/pdf/2505.15191), [HTML](https://arxiv.org/abs/2505.15191)
### Authors
Hana Satou,Alan Mitkiy,Emma Collins,Finn Kingston
### Background
迁移学习在领域转移下仍然是一个基本挑战，因为源和目标数据流形之间的不同带来了困难。现有的方法难以同时捕捉到语义变化和模型的脆弱性。
### Innovation
提出了一种新的框架MAADA（流形感知对抗性数据增强），该框架将对抗性扰动分解为流形内和流形外组件，以同时捕捉语义变化并提高模型的鲁棒性。此外，引入了一种几何感知对齐损失，针对源和目标流形之间的测地线差异进行最小化。
### Conclusion
在DomainNet、VisDA和Office-Home上的实验表明，MAADA在无监督和少样本设置中都超过了现有的对抗性和适应性方法，展示出了优越的结构鲁棒性和跨域泛化能力。
## 552. `cs.CV` - IVY-FAKE: 综合可解释框架和基准方法用于图像和视频AIGC检测 [PDF](https://arxiv.org/pdf/2506.00979), [HTML](https://arxiv.org/abs/2506.00979)
### Authors
Changjiang Jiang,Wenhui Dong,Zhonghao Zhang,Chenyang Si,Fengchang Yu,Wei Peng,Xinbin Yuan,Yifei Bi,Ming Zhao,Zian Zhou,Caifeng Shan
### Background
人工智能生成内容（AIGC）技术的快速发展使得高质量的合成内容得以生成，但也引发了重要的安全问题。现有的检测方法面临两个主要挑战：1）生成的图像和视频缺乏多维度的可解释数据集，现有的开源数据集（如WildFake、GenVideo）依赖于简化且二元的注释方法，这限制了检测器的可解释性和可信度。2）基于MLLM的伪造检测器（如FakeVLM）在逐级推理上的解释精度不够精细，这影响了局部化的可靠性和解释性。
### Innovation
本文提出了Ivy-Fake，这是第一个大规模的多模态可解释AIGC检测基准，包含超过106,000个丰富注释的训练样本（图像和视频）和5,000个手动验证的评估样本，这些样本来自多种生成模型和真实世界的数据集，确保多样性和质量。此外，还提出了一种基于组相对策略优化（GRPO）的增强学习模型Ivy-xDetector，能够生成可解释的推理链，并在多个合成内容检测基准上取得稳健的性能。
### Conclusion
广泛的实验表明我们的数据集和方法优于现有方法，在GenImage上将性能提高了从86.88%到96.32%，明显超过了先前的先进方法。
## 553. `cs.CV` - 适应段一切换模型以进行输电走廊危险区域分割 [PDF](https://arxiv.org/pdf/2505.22105), [HTML](https://arxiv.org/abs/2505.22105)
### Authors
Hang Chen,Maoyuan Ye,Peng Yang,Haibin He,Juhua Liu,Bo Du
### Background
输电走廊危险区域分割（PTCHS）旨在从复杂的背景下分离出输电设备及其周围的潜在威胁，这对确保电力传输安全具有重要意义。然而，现有的Segment Anything Model (SAM) 在复杂的输电走廊场景中难以处理目标对象，特别是那些具有精细结构的物体。
### Innovation
本文提出了ELE-SAM，将SAM适应于PTCHS任务。技术上，开发了一个上下文感知提示适配器，通过整合全局-局部特征和聚焦关键区域来实现更好的提示标记。为了解决复杂背景下的精细结构危险对象，设计了一个高保真掩码解码器，利用多尺度掩码特征并将其扩展到更高分辨率。此外，为了训练ELE-SAM并推动该领域的发展，构建了ELE-40K基准数据集，这是首个包含44,094张图像-掩模对的大规模和实际场景数据集，以PTCHS为主题。实验结果表明，ELE-SAM在ELE-40K上的性能优于基线模型，平均改进了16.8%的mIoU和20.6%的mBIoU。此外，与HQSeg-44K上的最新方法相比，平均2.9%的mIoU和3.8%的mBIoU提升进一步证明了我们方法在高质量通用对象分割中的有效性。
### Conclusion
通过ELE-SAM和ELE-40K基准数据集，提出的方法在PTCHS任务中取得了优于现有方法的性能。
## 554. `cs.CV` - Vision Remember: 在高效大型视觉-语言模型中通过视觉特征采样恢复视觉信息 [PDF](https://arxiv.org/pdf/2506.03928), [HTML](https://arxiv.org/abs/2506.03928)
### Authors
Ze Feng,Jiang-jiang Liu,Sen Yang,Lingyu Xiao,Zhibin Quan,Zhenhua Feng,Wankou Yang,Jingdong Wang
### Background
在大型视觉-语言模型（LVLMs）中，冗余的视觉标记的计算成本较高，许多现有方法通过视觉投影器对其进行压缩。然而，这种压缩可能会丢失对依赖精细空间关系的任务（如OCR和图表/表格理解）至关重要的视觉信息。
### Innovation
本文提出了一种通过在LLM解码器层中重新采样原始视觉特征来恢复视觉信息并提高效率的新方法。该方法包括Token-Feature Cross-Attention Layer和Token Bidirectional Self-Attention Layer两个关键模块。引入局部交叉注意力机制再采样视觉特征，并利用多层次融合来丰富视觉表示。
### Conclusion
与LLaVA-NeXT基线和其他相关方法相比，Vision Remember在多个视觉理解基准测试中表现出更好的性能，特别是在使用各种高效视觉投影器和LVLMs组合时，展示了其良好的通用性。
## 555. `cs.CV` - One-Step Diffusion-Based Image Compression with Semantic Distillation [PDF](https://arxiv.org/pdf/2505.16687), [HTML](https://arxiv.org/abs/2505.16687)
### Authors
Naifu Xue,Zhaoyang Jia,Jiahao Li,Bin Li,Yuan Zhang,Yan Lu
### Background
最近基于扩散(differentiation)的生成式图象编码器已经展示了令人印象深刻的性能，但是它们的迭代采样过程引入了不令人满意的延迟。
### Innovation
本文重新审视基于扩散的编解码器的设计，并提出了一种全新的一步生成式图像编解码器OneDC，该编解码器结合了一种隐含压缩模块和一步扩散生成器。考虑到在一步扩散中语义指导的重要性，提出了使用超先验(hyperprior)作为语义信号的概念，以及引入了一种从预训练生成式分词器向超先验编解码器转移知识的语义蒸馏机制。此外，采用像素域和隐含域优化，共同提升重建保真度与感知真实性。
### Conclusion
全方位实验表明，OneDC即使仅一步生成也能达到最优感知质量，相较于其他的多步骤扩散编解码器，比特率降低超过39%，解码速度提高了20倍。
## 556. `cs.CV` - 利用对比信息实现高效的文档阴影去除 [PDF](https://arxiv.org/pdf/2504.00385), [HTML](https://arxiv.org/abs/2504.00385)
### Authors
Yifan Liu,Jiancheng Huang,Na Liu,Mingfu Yan,Yi Huang,Shifeng Chen
### Background
文档阴影是文档数字化过程中的一大障碍，现有的文档阴影移除方法虽然取得了一些进展，但仍依赖额外信息（如阴影遮罩），缺乏在不同阴影场景下的通用性和有效性。这通常会导致阴影去除不完整或原始文档内容和其色调损失。此外，这些方法倾向于未能充分利用原始阴影文档图像中的信息。
### Innovation
本文重新聚焦于文档图像自身，提出了一种由对比度表示引导的端到端文档阴影移除方法，并采用粗到细的精炼方法。通过提取文档对比度信息，无需额外遮罩就能有效快速定位阴影形状和位置。这些信息随后被整合到阴影去除的细化处理过程中，为基于网络的阴影移除和特征融合提供了更好的指导。
### Conclusion
大量定性和定量实验表明，本方法在阴影移除方面达到最先进的性能。
## 557. `cs.CV` - ISAC: 无需训练的实例到语义注意力控制以改善多实例生成 [PDF](https://arxiv.org/pdf/2505.20935), [HTML](https://arxiv.org/abs/2505.20935)
### Authors
Sanghyun Jo,Wooyeol Lee,Ziseok Lee,Kyungsu Kim
### Background
文本到图像的扩散模型在最近变得非常有能力，但在多对象场景中的行为仍然不可靠：模型常常产生错误数量的对象实例，并且在对象间显示出语义交叉泄漏。这些故障被归因于模糊的对象边界；自注意力已经在去噪过程中早期揭示了实例布局，但现有方法仅作用于语义信号。
### Innovation
作者引入了ISAC (实例到语义注意力控制)，这是一种无需训练、模式无关的目标。ISAC首先从自注意力中雕刻出实例布局，然后将语义绑定到这些实例，执行分层注意力控制。ISAC在T2I-CompBench、HRS-Bench和IntraCompBench（一个新的针对类内组合的基准测试，故障最频繁）上都取得了持续的改进，多类准确率提高了至少50％，多实例准确率在IntraCompBench上提高了7%，无需任何微调或外部模型。ISAC还增强了重叠框布局下的布局到图像控制器，将其转化为密集实例掩码，表明实例形成和语义分配的分层解耦是提高多对象生成鲁棒性和可控性的关键原则。
### Conclusion
ISAC在无需微调和外部模型的情况下，显著提升了多对象生成的准确性和可控性，特别是在类内组合的场景中，展示了其在文本到图像及布局到图像生成任务中均具有潜力。
## 558. `cs.CV` - 动态ε调度：一种多因素自适应扰动预算的对抗训练方法 [PDF](https://arxiv.org/pdf/2506.04263), [HTML](https://arxiv.org/abs/2506.04263)
### Authors
Alan Mitkiy,James Smith,Myungseo wong,Hana Satou,Hiroshi Tanaka,Emily Johnson
### Background
现有的对抗训练方法主要依赖于固定的扰动预算，这并不能很好地考虑到实例间的鲁棒性差异。IAAT和MMA等先前工作尽管提出了实例级别的适应策略，但往往依赖于启发式或静态的数据鲁棒性近似。
### Innovation
该论文提出了一种名为Dynamic Epsilon Scheduling (DES)的新框架，该框架能够根据每个实例和每个训练迭代动态调整对抗性扰动预算。DES通过结合三种关键因素（基于梯度的边界距离近似、softmax熵预测置信度以及通过蒙特卡洛dropout估计的模型不确定性），提出了一个统一的调度策略，从而能够动态调整扰动预算，以引导更有效的对抗性学习。
### Conclusion
实验结果表明，DES方法在CIFAR-10和CIFAR-100数据集上相比于固定的ε值基线和先前的自适应方法，能够同时提高对抗鲁棒性和标准准确性。此外，该工作还提供了对我们调度策略的稳定性和收敛性的理论洞察，为基于实例的、数据驱动的对抗训练方法开辟了新的研究方向。
## 559. `cs.CV` - 基于力提示的视频生成模型能学习和泛化基于物理的控制信号 [PDF](https://arxiv.org/pdf/2505.19386), [HTML](https://arxiv.org/abs/2505.19386)
### Authors
Nate Gillman,Charles Herrmann,Michael Freeman,Daksh Aggarwal,Evan Luo,Deqing Sun,Chen Sun
### Background
近期视频生成模型的进展激发了对能够模拟现实世界的环境的世界模型的兴趣。尽管导航已经得到了充分的研究，但模拟真实世界力量的物理意义的交互仍然是研究的薄弱环节。
### Innovation
本文研究了使用物理力作为视频生成的控制信号，并提出了力提示，使得用户可以通过局部点力（如戳植物）或全局风力场（如风吹织物）与图像进行互动。示例显示，这些力提示能够利用原始预训练模型中的先验视觉和运动信息，实现对物理控制信号的现实响应，而无需在推断时使用任何3D资产或物理模拟器。本文的关键发现是，视频生成模型在适应通过Blender生成的合成视频中的物理力调节时，即使仅有一些少量物体的演示也能泛化得很好。这种方法能够生成模拟不同几何形状、环境和材料的力的视频，并且训练所需的样本量少，只有约15,000个样本，一天内使用四块A100 GPU完成，性能上优于现有方法。
### Conclusion
本文的方法在力的遵循和物理现实性方面优于现有方法，使世界模型更接近现实世界的物理交互。所有数据集、代码、权重和交互式视频演示都在项目页面上发布。
## 560. `cs.CV` - GreenHyperSpectra: 一种用于全球植被特征预测的多源高光谱数据集 [PDF](https://arxiv.org/pdf/2507.06806), [HTML](https://arxiv.org/abs/2507.06806)
### Authors
Eya Cherif(1, 2 and 3),Arthur Ouaknine(3 and 4),Luke A. Brown(5),Phuong D. Dao(6, 7 and 8),Kyle R. Kovach(9),Bing Lu(10),Daniel Mederer(1),Hannes Feilhauer(1, 2, 12 and 13),Teja Kattenborn(11 and 12),David Rolnick(3 and 4) ((1) Institute for Earth System Science and Remote Sensing, Leipzig University, Germany, (2) Center for Scalable Data Analytics and Artificial Intelligence (<a href=?http://ScaDS.AI? rel=?external noopener nofollow? class=?link-external link-http?>this http URL</a>), Leipzig University, Germany, (3) Mila Quebec AI Institute, Canada, (4) McGill University, Canada, (5) School of Science, Engineering and Environment, University of Salford, UK, (6) Department of Agricultural Biology, Colorado State University, USA, (7) Graduate Degree Program in Ecology, Colorado State University, USA, (8) School of Global Environmental Sustainability, Colorado State University, USA, (9) Department of Forest and Wildlife Ecology, University of Wisconsin, USA, (10) Department of Geography, Simon Fraser University, Canada, (11) Chair of Sensor-based Geoinformatics (geosense), University of Freiburg, Germany, (12) German Centre for Integrative Biodiversity Research (iDiv), Halle-Jena-Leipzig, Germany, (13) Helmholtz-Centre for Environmental Research (UFZ), Leipzig, Germany)
### Background
叶片碳含量和叶质量等植物特征是生物多样性和气候变化研究中的关键变量。传统实地采样不能在生态学意义的空间尺度上覆盖这些特征的变异。利用遥感的高光谱数据进行植物特征预测是一种有效的方法，但标签稀少和跨域差异（例如，不同传感器和生态分布）是预测中的挑战。
### Innovation
GreenHyperSpectra是一个预训练数据集，包含跨传感器和跨生态系统的真实世界样本，用于以半监督和自我监督的方法进行植物特征预测基准测试。该研究利用了一个包含在域和跨域场景的评估框架，并成功地用GreenHyperSpectra预训练了标签效率的多输出回归模型，这些模型超越了最先进的监督基准。这一研究促进了基于表示学习和植物功能性状评估的研究。
### Conclusion
我们的实证分析显示，在光谱表示学习中取得了显著改进，建立了一种综合方法论框架，以推动表示学习与植物功能性状评估的交叉研究。所有代码和数据均可在: this https URL: 获得。
## 561. `cs.CV` - MetricHMSR：单目图像中的人体网格和场景恢复 [PDF](https://arxiv.org/pdf/2506.09919), [HTML](https://arxiv.org/abs/2506.09919)
### Authors
Chentao Song,He Zhang,Haolei Yuan,Haozhe Lin,Jianhua Tao,Hongwen Zhang,Tao Yu
### Background
现有的单目图像人体网格和场景恢复方法在统一模块中实现人体姿态和精确的3D位置估计时面临挑战。这些方法基于不现实的相机模型假设，难以处理精确感知的固有挑战。
### Innovation
MetricHMSR引入了两种创新：一、利用相机射线全面编码边界框信息和透视投影的内在参数；二、提出Human Mixture-of-Experts（MoE），该模型动态路由图像特征和射线特征到特定任务专家，以实现局部姿态和全局3D位置的统一感知能力。通过改进现有的单目度量深度估计方法，使人体和场景在3D空间中无缝叠加。
### Conclusion
实验结果表明，所提出的方法在人体网格和场景恢复方面达到了最先进的性能。
## 562. `cs.CV` - 通过局部梯度感知表面过滤学习 noisy 点的法线 [PDF](https://arxiv.org/pdf/2507.03394), [HTML](https://arxiv.org/abs/2507.03394)
### Authors
Qing Li,Huifang Feng,Xun Gong,Yu-Shen Liu
### Background
在三维几何处理中，从嘈杂点云中估计法线是一个持续的挑战，尤其是针对端到端法线估计。现有方法通常处理相对干净的数据，并依赖监督先验来适应局部表面。现有的方法限制在特定邻域内拟合局部表面。
### Innovation
提出了一种新的方法，通过局部梯度感知表面过滤来学习嘈杂点云的法线。这种方法通过隐式函数约束局部梯度，将嘈杂的点投影到底层表面上，并采用了距离度量操作符进行全局曲面拟合。为了防止过度平滑和梯度退化，该方法进一步引入了局部梯度一致性和方向性，以及局部梯度聚合。在法线估计、表面重建和点云去噪方面的全面实验中表现领先。
### Conclusion
该方法在法线估计、表面重建和点云去噪方面表现出最先进的性能，源代码和训练模型已公开。
## 563. `cs.CV` - MANGO: 多模态注意力归一化流融合学习方法 [PDF](https://arxiv.org/pdf/2508.10133), [HTML](https://arxiv.org/abs/2508.10133)
### Authors
Thanh-Dat Truong,Christophe Bobda,Nitin Agarwal,Khoa Luu
### Background
近年来，多模态学习取得了许多成功。当前的多模态融合方法采用Transformer的注意力机制来隐式学习多模态特征的潜在联系，这导致多模态模型难以捕捉每种模态的本征特征，因而解析复杂结构和多模态输入的相关性变得困难。
### Innovation
引入了一种新颖的多模态注意力归一化流（MANGO）方法，以开发明确、可解释且可处理的多模态融合学习方法。提出了新的可逆交叉注意力（ICA）层，以开发基于归一化流的多模态数据模型。提出了三种新的交叉注意力机制：模态间交叉注意力（MMCA）、跨模态交叉注意力（IMCA）和可学习跨模态交叉注意力（LICA），以便更高效地捕捉多模态数据中复杂的潜在关联。引入了新的多模态注意力归一化流以使所提出的方法适用于高维多模态数据。
### Conclusion
在三种不同的多模态学习任务（语义分割、图像到图像的转换、电影类型分类）上的实验结果表明，所提出的方法具有最先进的性能。
## 564. `cs.CV` - ReasonAct: 进阶训练在小规模模型中实现精细粒度视频推理 [PDF](https://arxiv.org/pdf/2508.01533), [HTML](https://arxiv.org/abs/2508.01533)
### Authors
Jiaxin Liu,Zhaolu Kang
### Background
尽管近期的多模态模型在视觉-语言任务中取得了进展，但小型模型仍无法处理视频理解所需的精细时间推理。
### Innovation
ReasonAct 方法通过三个训练阶段提升视频推理：首先进行仅文本推理的初始化，然后在视频上进行微调，最后使用具有时间意识的强化学习进行细化。该方法基于 Temporal Group Relative Policy Optimization (T-GRPO) 并结合了时间一致性建模，还提出了一种生物力学驱动的动作子分解机制，以提供渐进式的奖励。
### Conclusion
在 HMDB51、UCF-101 和 Kinetics-400 上的实验表明，该模型分别达到了 67.2%、94.1% 和 78.9% 的准确率，相对于基线分别提高了 17.9、15.8 和 12.3 个百分点。消融实验验证了渐进式训练能够使小型模型在保持计算效率的同时实现可竞争的视频推理性能。
## 565. `cs.CV` - 定向代词：一种用于大型语言视觉模型的稳健多模态对齐方法 [PDF](https://arxiv.org/pdf/2508.14264), [HTML](https://arxiv.org/abs/2508.14264)
### Authors
Thanh-Dat Truong,Huu-Thien Tran,Tran Thai Son,Bhiksha Raj,Khoa Luu
### Background
大型多模态模型（LMMs）在各种理解任务中表现出色，但由于视觉和文本特征之间的对齐和相关性导致的鲁棒性和泛化能力有限，依然存在一些基本的局限性。
### Innovation
提出了一个简单但有效的学习机制，通过解决混排问题，改进视觉和文本模态之间的稳健对齐。具体来说，该方法在LMM的预训练和微调阶段引入了重建图像顺序和文本顺序的两项新任务，提升了推理能力、视觉理解和跨模态对齐。此外，提出了一个有向代词方法，以捕捉视觉和文本知识，使模型能够重建视觉输入的正确顺序。进一步地，引入了一个新的图像到响应引导损失，以进一步提高LMM在响应中的视觉理解能力。该方法在学术领域和指令遵循的大型语言视觉模型基准测试中，均实现了最先进的性能。
### Conclusion
提出的框架相比前期的LMM模型，在学术任务导向和指令遵循的大型语言视觉模型基准测试中，实现了更为先进的表现。
## 566. `cs.CV` - 在扩散模型中整合内在场景属性以实现空间一致性图像生成 [PDF](https://arxiv.org/pdf/2508.10382), [HTML](https://arxiv.org/abs/2508.10382)
### Authors
Hyundo Lee,Suhyung Choi,Inwoo Hwang,Byoung-Tak Zhang
### Background
现有的图像生成模型能够生成高保真度的图像，但由于数据集的限制，这些模型往往会产生空间不一致和扭曲的图像。以往的方法主要依赖于图像和文本对或使用内蕴属性作为条件输入，这种方法未能充分捕捉场景的潜在结构和空间布局信息。
### Innovation
本文提出了一种能够同时生成图像及其对应内蕴属性的方法。通过利用预训练的估计器从大规模图像数据集中提取丰富的内蕴场景属性，并使用自编码器将这些属性整合为一个潜在变量。在此基础上，方法通过预训练的大规模潜扩散模型（LDMs）同时对图像和内蕴领域进行去噪处理，并通过共享信息防止褪色而不损失图像质量，从而实现更加空间一致和逼真的图像生成。
### Conclusion
实验结果表明，该方法能够纠正空间不一致性，生成更自然的场景布局，同时保持基础模型（如Stable Diffusion）的保真度和文本对齐。
## 567. `cs.CV` - WeatherDiffusion：在内在空间中的可控天气编辑 [PDF](https://arxiv.org/pdf/2508.06982), [HTML](https://arxiv.org/abs/2508.06982)
### Authors
Yixin Zhu,Zuoliang Zhu,Jian Yang,Miloš Hašan,Jin Xie,Beibei Wang
### Background
在传统的像素空间编辑中，控制天气效果较为困难，因为像素级别的编辑方法缺乏对材质、场景几何和光照等内在属性的有效控制。现有的一些天气恢复方法和基于渲染的方法也存在局限性，无法实现精细的天气控制。因此，本文提出了一种基于扩散先验的框架——WeatherDiffusion，该框架能够通过内在映射来增强可控性，从而更好地应用于下游任务，如自动驾驶。
### Innovation
本文创新地提出了WeatherDiffusion框架，包含两个基于扩散先验的组件：一个逆渲染器，用于从输入图像估计材质属性、场景几何和光照等内在图；另一个正向渲染器，其利用这些几何和材质图以及对特定天气条件的文本提示生成最终图像。此外，还提出了一种内在图意识注意力机制，以提高大面积户外场景的空间对应性和分解质量，并使用CLIP空间插值技术实现高精度的天气控制。
### Conclusion
WeatherDiffusion框架在合成和真实世界数据集上的实验表明，该方法在可控天气编辑上优于现有的基于像素空间编辑、天气恢复以及基于渲染的方法，对于自动驾驶等潜在下游任务具有良好的鲁棒性和检测、分割能力。
## 568. `cs.CV` - 基于对比度先验的无掩膜阴影去除方法 [PDF](https://arxiv.org/pdf/2507.21949), [HTML](https://arxiv.org/abs/2507.21949)
### Authors
Jiyu Wu,Yifan Liu,Jiancheng Huang,Mingfu Yan,Shifeng Chen
### Background
现有的阴影去除方法通常依赖于阴影掩膜，而在真实场景中获取这些掩膜是具有挑战性的。因此，研究人员开始探索其他方法，如局部对比度信息，来指导没有显式掩膜情况下的阴影去除。然而，在复杂场景中，这些方法的自有的暧昧性成为了一个关键的限制因素，使得它们难以区分真正的阴影与低反射率物体和复杂的背景纹理。
### Innovation
为了克服上述问题，本文提出了自适应门控双支路注意力机制（AGBA）。AGBA能够动态地过滤和重新加权对比度信息，从而有效地区分阴影特征与其他混淆视觉元素。此外，为了应对软阴影边界和精细细节恢复的长期挑战，本文还引入了基于扩散的频率-对比度融合网络（FCFN），通过高频率和对比度信息来引导生成过程。
### Conclusion
大量实验表明，本文方法在无掩膜方法中达到了最先进的性能，同时在与基于掩膜方法的对比中也保持了竞争力。
## 569. `cs.CV` - Multimodal LLMs for Video Understanding的可信性基准测试 [PDF](https://arxiv.org/pdf/2506.12336), [HTML](https://arxiv.org/abs/2506.12336)
### Authors
Youze Wang,Zijun Chen,Ruoyu Chen,Shishen Gu,Wenbo Hu,Jiayang Liu,Yinpeng Dong,Hang Su,Jun Zhu,Meng Wang,Richang Hong
### Background
最近，多模态大型语言模型（尤其是视频LLMs）在处理复杂的时空数据方面的能力得到了增强。然而，这些问题（事实不准确、有害内容、偏见、幻觉和隐私风险）削弱了它们的可靠性。本研究旨在填补该领域的空白，通过设置一个全面的基准评估23个最先进的视频LLMs（5个商用，18个开源）的五个关键维度：真实性、稳健性、安全性、公平性和隐私。
### Innovation
该研究提出了Trust-videoLLMs基准测试框架，包含30个任务，评估开放源码和商用模型在动态场景理解、跨模态扰动抗性和现实世界风险缓解等方面的表现。结果表明，开源模型有时优于商用模型，但商用模型通常表现出更高的可信度。此外，基准测试结果强调了增强训练数据多样性和多模态对齐的重要性。
### Conclusion
Trust-videoLLMs提供了一个公开可用且可扩展的工具包，用于标准化可信性评估，填补了关注准确性的基准测试和强化可信性、安全性和隐私需求之间的差距。
## 570. `cs.CV` - EvoEmpirBench: 基于代理经验的动态空间推理 [PDF](https://arxiv.org/pdf/2509.12718), [HTML](https://arxiv.org/abs/2509.12718)
### Authors
Pukun Zhao,Longxiang Wang,Miaowei Wang,Chen Chen,Fanqing Zhou,Haojian Huang
### Background
现有的空间推理基准主要关注静态或全局可观测的环境，无法捕捉在部分可观测性和动态变化下的长期推理和记忆利用的挑战。多数模型在这些环境下显示出明显的局限性。
### Innovation
作者提出了两个动态空间基准，即局部可观察迷宫导航和match-2消除，系统性地评估模型在局部感知、环境反馈和全局目标紧密结合下的空间理解和适应性规划能力。每个动作都会引发环境结构的改变，要求持续更新认知和策略。此外，还提出了基于主观体验的记忆机制，用于跨任务的经验转移和验证。
### Conclusion
实验表明，我们的基准揭示了主流模型在动态空间推理和长期记忆方面的关键局限性，为未来方法学的进步提供了一个综合的平台。相关代码和数据可在特定URL处获取。
## 571. `cs.CV` - 揭开并缓解深度伪造主动取证中的破坏性多重嵌入攻击 [PDF](https://arxiv.org/pdf/2508.17247), [HTML](https://arxiv.org/abs/2508.17247)
### Authors
Lixin Jia,Haiyang Sun,Zhiqing Guo,Yunfeng Diao,Dan Ma,Gaobo Yang
### Background
随着深度伪造技术的快速发展和数字媒体的广泛传播，个人隐私的安全威胁日益严重。现有的主动取证方法通过嵌入不可见的水印来实现对来源可靠追踪，是应对这些威胁的关键防御手段。然而，现有方法依赖于单一水印嵌入的理想化假设，这在实际场景中证明是不切实际的。
### Innovation
本文首次正式定义并证明了多重嵌入攻击（MEA）的存在。提出了一种名为对抗干扰模拟（AIS）的一般训练范式。AIS在微调过程中明确模拟MEA场景，并引入了一种基于抗干扰的损失函数，以确保模型能够学习稀疏且稳定的水印表示，即使在二次嵌入后仍能正确提取原始水印。
### Conclusion
大量的实验表明，我们提出的插件式训练框架AIS在现有方法中显著增强了对MEA的鲁棒性，使得模型即使在经过多次嵌入后也能正确提取出原始水印。
## 572. `cs.CV` - 不平等的划分：关于在无关类别之间泛化属性的重新思考 [PDF](https://arxiv.org/pdf/2509.06998), [HTML](https://arxiv.org/abs/2509.06998)
### Authors
Liviu Nicolae Fircă,Antonio Bărbălau,Dan Oneata,Elena Burceanu
### Background
先前的工作主要集中在窄范围的分类或视觉相似领域内的属性预测上，尚不清楚现有模型是否能够从概念上距离较远的类别中抽象并应用属性知识。
### Innovation
本文首次明确评估在语义和感知上差异较大的类别间属性预测任务的鲁棒性，提出了一种基于LLM的语义分组、嵌入相似性阈值分割、嵌入基础聚类和基于泛化类别的分割策略以逐步减少训练集和测试集之间的相关性。结果表明，随着训练和测试类别之间相关性的降低，性能急剧下降，说明泛化能力对划分设计的敏感性。
### Conclusion
在评估的方法中，聚类方法提供了在减少隐藏相关性的同时保持学习性的最佳权衡。这些发现为当前表示的局限性提供了新的见解，并为未来基于属性推理的基准构建提供了指导。
## 573. `cs.CV` - 多尺度时间预测通过增量生成和多智能体协作 [PDF](https://arxiv.org/pdf/2509.17429), [HTML](https://arxiv.org/abs/2509.17429)
### Authors
Zhitao Zeng,Guojian Yuan,Junyuan Mao,Yuxuan Wang,Xiaoshuang Jia,Yueming Jin
### Background
准确的时间预测是全面场景理解和具身人工智能之间的桥梁。然而，视觉语言模型难以预测场景在多个时间尺度上的多个精细状态。该论文通过分解多尺度为两个正交维度——时间尺度和状态尺度，提出了多尺度时间预测（MSTP）任务，并为普通和外科场景进行了建模。
### Innovation
为支持此统一任务，论文提出了MSTP基准，其特点是多尺度状态和时间上的同步标注。此外，论文还提出了增量生成和多智能体协作方法（IG-MC）。该方法包括两个创新点：首先，提出了一种插件式的增量生成模块，用于在扩展的时间尺度上持续合成最新的视觉预览，以引导多个决策智能体，确保决策与生成的视觉效果同步，防止随着前瞻间隔的增加而性能下降；其次，提出了多状态预测的基于决策的多智能体协作框架，该框架由生成、启动和多状态评估智能体组成，动态触发和评估预测周期以平衡全局一致性与局部保真度。
### Conclusion
该研究通过提出MSTP基准和IG-MC方法，为多尺度时间预测提供了一套解决方案，该解决方案在时间尺度和状态尺度上实现了同步标注，并通过多智能体协作框架提高了多状态预测的能力，确保了前瞻间隔增加时预测性能的稳定性。
## 574. `cs.CV` - PointNSP：基于下一尺度层级细节预测的自回归3D点云生成 [PDF](https://arxiv.org/pdf/2510.05613), [HTML](https://arxiv.org/abs/2510.05613)
### Authors
Ziqiao Meng,Qichao Wang,Zhiyang Dou,Zixing Song,Zhipeng Zhou,Irwin King,Peilin Zhao
### Background
自回归点云生成一直以来在质量上落后于基于扩散的方法。性能差距源于自回归模型对固无排序的点集施加了人工顺序，迫使形状生成按照局部预测的序列进行，这种顺序偏见强调短程连续性，却阻碍了模型捕捉长程依赖的能力，从而妨碍了全球结构性质，如对称性、一致拓扑和大规模几何规律的表达。
### Innovation
基于模型在形状建模中的层级细节原理（LOD），我们提出了PointNSP，这是一种逐级细化生成框架，它在低分辨率下保持了全局形状结构，在高分辨率下逐步细化细粒度几何。这种多尺度分解使自回归目标与点集的置换不变性质对齐，增强跨尺度的丰富相互作用，同时避免了固定的易碎排序。
### Conclusion
PointNSP在ShapeNet上的实验表明，它首次在自回归范式下达到了最佳生成质量。此外，它在参数、训练和推理效率方面都超过了强大的基于扩散的基本模型。最后，在16,384个点的密集生成中，PointNSP的优势更加明显，突显了其可扩展性。
## 575. `cs.CV` - ControlEvents: Controllable Synthesis of Event Camera Data with Foundational Prior from Image Diffusion Models [PDF](https://arxiv.org/pdf/2509.22864), [HTML](https://arxiv.org/abs/2509.22864)
### Authors
Yixuan Hu,Yuxuan Xue,Simon Klenk,Daniel Cremers,Gerard Pons-Moll
### Background
近年来，事件摄像头由于其生物启发的特性，如高时域分辨率和高动态范围，受到了广泛关注。然而，获取用于事件视觉任务的大规模标注真实数据仍面临挑战和高昂的成本。
### Innovation
本文提出了一种基于扩散的生成模型——ControlEvents，该模型可以根据多样化的控制信号（如类别文本标签、2D骨架和3D人体姿态）合成高质量的事件数据。该方法利用基础模型（如Stable Diffusion）的扩散先验，实现高质量的数据生成，同时需要少量的微调和标注数据。这简化了数据生成流程，并显著降低了产生标注事件数据的成本。
### Conclusion
本文通过合成事件数据用于视觉识别、2D骨架估计和3D人体姿态估计，展示了所提出方法的有效性。实验结果表明，合成的标注事件数据能提高所有任务的模型性能。此外，本文的方法还能在训练期间根据未见过的文本标签生成事件，展示了强大的基于文本的生成能力。
## 576. `cs.CV` - 具有轻量级异常检测的模块化现场解决方案，用于农业可持续养分管理 [PDF](https://arxiv.org/pdf/2509.12247), [HTML](https://arxiv.org/abs/2509.12247)
### Authors
Abigail R. Cohen,Yuming Sun,Zhihao Qin,Harsh S. Muriki,Zihao Xiao,Yeonju Lee,Matthew Housley,Andrew F. Sharkey,Rhuanito S. Ferrarezi,Jing Li,Lu Gan,Yongsheng Chen
### Background
高效的养分管理对于作物生长和可持续资源利用（如氮和能源）至关重要。当前的方法需要很长的分析时间，无法实现实时优化；而成像技术可以在短时间内进行表型分析，但计算强度较高，难以在资源有限的条件下部署。
### Innovation
本研究提出了一种灵活且分层的异常检测和状态估计管道，包括跨效率和准确度范围的方法的全面能量分析。该管道使用自编码器（AE）进行早期预警，并采用复杂度不同的状态估计模块：光谱指数（VI）特征结合机器学习（随机森林，RF）和原始全图像深度学习（Vision Transformer，ViT）。研究结果展示了高效的异常检测（在移植后9天检测到73%的T3样本），能量消耗远低于浪费氮素的嵌入能量。
### Conclusion
具有模块化管道的工作为边缘诊断和农业可持续性提供了机会。状态估计模块之间的权衡表明，在更高的能耗成本下，ViT在磷和钙估计方面优于RF（R2值分别为0.61 vs. 0.58 和0.48 vs. 0.35）。
## 577. `cs.CV` - FastAvatar: 单张任意姿态面部图像瞬间三维高斯点云重建 [PDF](https://arxiv.org/pdf/2508.18389), [HTML](https://arxiv.org/abs/2508.18389)
### Authors
Hao Liang,Zhixuan Ge,Soumendu Majee,Ashish Tiwari,G.M. Dilshan Godaliyadda,Ashok Veeraraghavan,Guha Balakrishnan
### Background
现有的单图像三维面部重建方法在速度和准确性之间存在权衡，尤其是对于具有极端输入姿态的面部。重建速度较慢，尤其是在使用优化方法时，需要较长的处理时间，并且在处理高度变化的姿态时稳定性较差。快速重建高质量三维面部模型对于多种应用非常重要，如虚拟现实和数字特效。
### Innovation
FastAvatar 提出了一种融合直接预测和优化策略的快速且鲁棒的单图像三维面部重建算法，使用 3D 高斯点云 (3DGS) 技术。通过两项设计，首先通过归一化姿态身份嵌入预测粗略的面部几何结构，然后在测试阶段优化外观参数以实现逼真的渲染。FastAvatar 在单个 NVIDIA A100 GPU 上实现了高精度重建，在不到 3 秒的时间内重建了一个高质量的全头部3DGS 协议，同时比现有基于受试者优化方法（如 FlashAvatar、GaussianAvatars 和 GASP）快约 600 倍。FastAvatar 支持照片级真实感的新视角合成和使用 FLAME 引导的表情动画。
### Conclusion
FastAvatar 通过同时提供高保真度、姿态鲁棒性和快速重建，大幅扩展了基于 3DGS 的面部协议的应用范围。该算法结合了速度和稳定性，即使在极端输入姿态下也能实现良好的身份保持。同时，它支持照片级真实感的新视角合成和表情动画，使得仅从一张图像中实现受控再现成为可能。
## 578. `cs.CV` - 工业缺陷检测的自动化神经架构设计 [PDF](https://arxiv.org/pdf/2510.06669), [HTML](https://arxiv.org/abs/2510.06669)
### Authors
Yuxi Liu,Yunfeng Ma,Yi Tang,Min Liu,Shuai Jiang,Yaonan Wang
### Background
工业表面缺陷检测(SDD)对于确保产品质量和制造可靠性至关重要。然而，由于表面缺陷的多样形状和大小，SDD面临两大挑战：类内差异和类间相似性。当前的方法主要依赖于手动设计的模型，这些模型需要大量的尝试和错误，并且在解决上述两个挑战时常常不够有效。
### Innovation
我们提出了AutoNAD，一个自动化神经架构设计框架，用于SDD。它联合搜索卷积、变压器和多层感知机，这种混合设计允许模型捕捉细微的局部变化和长距离的语义上下文，从而解决两个关键问题，同时减少手工网络设计的成本。为了支持这样多样搜索空间的高效训练，AutoNAD引入了跨权重共享策略，这加速了超网络的收敛并提高了子网络的性能。此外，还整合了一个可搜索的多级别特征聚合模块（MFAM），以增强多尺度特征学习。除了检测准确性，运行时效率对于工业部署也至关重要。为此，AutoNAD引入了一个延迟感知先验来引导高效架构的选择。
### Conclusion
AutoNAD在三个工业缺陷数据集上得到了验证，并且进一步应用于缺陷成像和检测平台。相关代码可以在指定链接上获取。
## 579. `cs.CV` - SaFiRe: Saccade-Fixation Reiteration with Mamba for Referring Image Segmentation [PDF](https://arxiv.org/pdf/2510.10160), [HTML](https://arxiv.org/abs/2510.10160)
### Authors
Zhenjie Mao,Yuhuan Yang,Chaofan Ma,Dongsheng Jiang,Jiangchao Yao,Ya Zhang,Yanfeng Wang
### Background
Referring Image Segmentation (RIS)旨在根据自然语言表达分割图像中的目标对象。现有方法依赖预训练的视觉骨干网络和更多的训练数据取得显著成效，但主要侧重于简单的表达方式，如“红色的车”或“左边的女孩”这样的短句。这种简化导致RIS简化为关键词或概念匹配问题，限制了模型处理表达式中的指代歧义能力。
### Innovation
该研究识别了两个现实挑战场景：干扰目标对象的表达（涉及多个实体的上下文线索）和类别隐含表达（未明确指出对象类别）。为此，提出了一种新型框架SaFiRe，模拟人类的认知两阶段过程。除了引入AReFCOCO作为新的基准，以评估在模糊指代表达下的RIS模型性能。
### Conclusion
在标准和新提出的数据集上的广泛实验显示出SaFiRe在RIS上的优越性，比现有基线方法更先进。
## 580. `cs.CV` - 降相关加快视觉 transformers [PDF](https://arxiv.org/pdf/2510.14657), [HTML](https://arxiv.org/abs/2510.14657)
### Authors
Kieran Carrigg,Rob van Gastel,Melda Yeghaian,Sander Dalm,Faysal Boughorbel,Marcel van Gerven
### Background
MAE预训练在低标签数据环境下表现强大，但伴随巨大的计算成本，不适合时间与资源受限的工业环境。本文通过将降相关反向传播(DBP)整合到MAE预训练中，解决了这一问题。DBP可以在每个层逐步减少输入相关性以加速收敛，应用于编码器，不损失稳定性。
### Innovation
通过引入DBP方法，该研究将降相关技术应用于MAE预训练，有效加速了收敛速度，并在保持稳定性的前提下减少了训练时间，降低了能耗。实验表明，DBP-MAE在随机抽样的ImageNet-1K预训练和ADE20K微调中表现出21.1%的壁挂时间减少，21.4%的碳排放降低，以及1.1点的分割mIoU改善，在自有工业数据集上的预训练和微调中也显示出类似效果。
### Conclusion
研究结果表明，DBP方法可以减少大规模ViT预训练的训练时间和能源消耗，同时提高下游性能。
## 581. `cs.CV` - XYZCylinder: 通过统一圆柱提升方法向驾驶场景兼容前馈3D 高斯点云逼近 [PDF](https://arxiv.org/pdf/2510.07856), [HTML](https://arxiv.org/abs/2510.07856)
### Authors
Haochen Yu,Qiankun Liu,Hongyuan Liu,Jianfei Jiang,Juntao Lyu,Jiansheng Chen,Huimin Ma
### Background
3D重建的前馈范式已成为近期研究热点，这类方法通过学习隐式的、固定的视角变换来生成单一场景表示。然而，这类方法应用于复杂驾驶场景时表现出显著的局限性。主要原因有两个：首先，依赖固定的视角变换限制了对不同相机配置的兼容性；其次，从稀疏的360°视图中学习复杂驾驶场景，由于视角重叠度低，导致最终的重建精度受限。
### Innovation
为解决这些难题，本文提出了XYZCylinder方法，这是一种基于统一圆柱提升技术的新方法，集成了相机建模和特征提升。为了应对兼容性问题，提出了统一圆柱相机建模（UCCM）策略，该策略明确建模投影参数以统一多种相机配置，规避了学习视角依赖对应点的需要。为了提高重建准确性，提出了基于新设计的圆柱平面特征组（CPFG）的混合表示法，该表示法结合了多个专用模块，从2D图像特征提升到3D空间。
### Conclusion
广泛评估表明，XYZCylinder不仅在不同的评估设置中实现了最先进的性能，还展示了在完全不同相机设置的新场景下的零样本兼容性。
## 582. `cs.CV` - VA-GS: 使用视图对准增强高斯采样的几何表示 [PDF](https://arxiv.org/pdf/2510.11473), [HTML](https://arxiv.org/abs/2510.11473)
### Authors
Qing Li,Huifang Feng,Xun Gong,Yu-Shen Liu
### Background
3D高斯采样 recently emerged as an efficient solution for high-quality and real-time novel view synthesis. However, its capability for accurate surface reconstruction is still underexplored. Due to the discrete and unstructured nature of Gaussians, supervision based on image rendering loss often leads to inaccurate geometry and inconsistent multi-view alignment.
### Innovation
我们提出了一种新颖的方法，通过视图对准（VA）增强3D高斯采样的几何表示。具体来说，我们将边缘意识图像线索纳入渲染损失中，以改善表面边界划分。为了在视图之间维护几何一致性，我们引入了一种基于视角的光度对准损失，用以建模遮挡并鼓励高斯之间的准确空间关系。此外，我们通过基于法线的约束纳入深度图像特征嵌入，以在光照变化导致的歧义中改进局部表面估计，并进一步增强几何结构在不同视角和照明条件下的稳健性。
### Conclusion
我们提出的方法在标准基准上的广泛实验中证明，在表面重建和新视图合成方面均取得了最先进的性能。源代码可以在这个链接https://github.com/yourithublink 获得。
## 583. `cs.CV` - SARVLM: SAR遥感图像语义理解和目标识别的视觉语言基础模型 [PDF](https://arxiv.org/pdf/2510.22665), [HTML](https://arxiv.org/abs/2510.22665)
### Authors
Qiwei Ma,Zhiyu Wang,Wang Liu,Xukun Lu,Bin Deng,Puhong Duan,Xudong Kang,Shutao Li
### Background
合成孔径雷达(SAR)因其全天候能力是重要的成像技术。虽然最近自监督学习和遮罩图像建模（MIM）的进步使得SAR基础模型成为可能，但这些方法更多关注低级视觉特征，而忽视了遥感图像中的多模态对齐和零样本目标识别。
### Innovation
1. 构建了包含超过一百万对图像-文本的SARVLM-1M大规模视觉-语言数据集。2. 提出了领域迁移训练策略来缓解自然图像与SAR图像之间的巨大差距。3. 开发了SARVLM，这是第一个针对SAR的视觉语言基础模型，包含SARCLIP和SARCash两大组件，以对比的视觉-语言目标进行训练，旨在连接SAR图像和文本描述，从而实现了遥感图像的语义理解和目标识别。
### Conclusion
通过广泛实验，SARVLM在图像文本检索、零样本分类、语义定位和图像描述等任务上表现出了优秀的特征提取和解释能力，优于最先进的视觉语言模型，推动了遥感图像的语义理解。
## 584. `cs.CV` - MoEGCL: Mixture of Ego-Graphs Contrastive Representation Learning for Multi-View Clustering [PDF](https://arxiv.org/pdf/2511.05876), [HTML](https://arxiv.org/abs/2511.05876)
### Authors
Jian Zhu,Xin Zou,Jun Sun,Cheng Luo,Lei Liu,Lingfang Zeng,Ning Zhang,Bian Wu,Chang Tang,Lirong Dai
### Background
近年来，图神经网络（GNNs）的进展显著推动了多视图聚类（MVC）的进步。然而，现有方法面临着粗粒度图融合的问题。当前方法通常为每个视图生成一个单独的图结构，然后在视图级别上进行加权融合，这相对来说是一个粗糙的策略。
### Innovation
本文提出了一种新的图族对比表示学习（MoEGCL）。它主要由两个模块组成。特别地，提出了一种创新的Ego-Graph融合（MoEGF），用于构建ego图，并利用Mixture-of-Experts网络在样本级别而非传统的视图级别实现细粒度的ego图融合。此外，还提出了Ego Graph对比学习（EGCL）模块，以使融合表示与视图特定表示对齐。EGCL模块通过增加来自同一簇的样本之间的表示相似性，进一步促进了细粒度的图表示。
### Conclusion
大量的实验结果显示，MoEGCL在深度多视图聚类任务中达到了最先进的性能。源代码已在此网址公开：this https URL.
## 585. `cs.CV` - UniChange：利用多模态大型语言模型统一变化检测 [PDF](https://arxiv.org/pdf/2511.02607), [HTML](https://arxiv.org/abs/2511.02607)
### Authors
Xu Zhang,Danyang Li,Xiaohang Dong,Tianhao Wu,Hualong Yu,Jianye Wang,Qicheng Li,Xiang Li
### Background
变化检测（CD）是监测和分析土地覆盖动态的基本任务。尽管近期高性能模型和高质量数据集大幅推动了该领域的发展，但当前模型的一个关键局限性是它们通常只能从单一类型标注数据中获取有限的知识，无法同时利用二元变化检测（BCD）和语义变化检测（SCD）数据集来提高通用性和灵活性。
### Innovation
我们利用多模态大型语言模型（MLLM）的语言先验和统一能力，开发了UniChange，这是首个基于MLLM的统一变化检测模型。UniChange结合了生成语言能力和专门化的CD功能。通过引入三个特殊标记[T1]、[T2]和[CHANGE]，UniChange成功地统一了BCD和SCD任务，并利用文本提示指导变化类别的识别，从而不需要预定义的分类头部。这一设计让UniChange能够从多源数据集中有效获取知识，即使这些数据集的类别定义存在冲突。在四个公开基准（WHU-CD、S2Looking、LEVIR-CD+和SECOND）上进行的实验展示了SOTA性能，IoU分数分别为90.41、53.04、78.87和57.62。
### Conclusion
实验结果表明，UniChange在四个公开基准上的IoU得分分别为90.41、53.04、78.87和57.62，超越了所有先前的方法。代码已公开。
## 586. `cs.CV` - DensiCrafter: 物理约束下的自支撑空心结构的生成与制造 [PDF](https://arxiv.org/pdf/2511.09298), [HTML](https://arxiv.org/abs/2511.09298)
### Authors
Shengqi Dang,Fu Chai,Jiaxin Li,Chao Yuan,Wei Ye,Nan Cao
### Background
3D生成模型的兴起使得多模态输入（例如文本或图像）可以自动进行3D几何和纹理合成。然而，这些方法通常忽略了物理约束和制造考虑。本研究旨在解决生成轻量化且自支撑的3D设计的挑战。
### Innovation
提出了DensiCrafter框架，通过优化密度场生成轻量化且自支撑的3D空心结构。该框架基于Trellis产生的粗略体素网格，将其视为连续密度场进行优化，并引入了三种可微、物理约束且无需模拟的损失项。此外，对质量正则化项惩罚不必要的材料，而对优化域的限制则保留外表面。该方法与Trellis预训练模型无缝集成。
### Conclusion
在广泛的评估中，该方法在文本转3D任务上实现了高达43%的材料质量减少。与最先进的基线相比，该方法可以提高结构稳定性并保持高质量的几何保真度。实验结果表明，我们的空心设计可以可靠地制造并实现自支撑。
## 587. `cs.CV` - Saliency-R1：通过置信引导强化学习激励MLLM统一的视觉显著性推理能力 [PDF](https://arxiv.org/pdf/2511.00396), [HTML](https://arxiv.org/abs/2511.00396)
### Authors
Long Li,Shuichen Ji,Ziyang Luo,Zhihui Li,Dingwen Zhang,Junwei Han,Nian Liu
### Background
尽管多模态大型语言模型（MLLMs）在高级视觉语言推理方面表现出色，但它们缺乏内在的视觉显著性意识，这使得难以识别关键的视觉元素。本文旨在解决这一问题。
### Innovation
本文提出了首个统一的MLLM框架Saliency-R1，该框架能够共同处理三种代表性且异质的显著性任务：显著目标检测（SOD）、显著实例分割（SIS）和协同显著目标检测（CoSOD），从而增强模型在显著性推理方面的能力。此外，引入了一种基于结构化标签（<rg>, <ins>）的文本接口，用于编码区域级和实例级的指称表达，并提出了一种名为自信导向策略优化（CGPO）的新型单样本强化学习算法，以提高MLLM的训练效率。
### Conclusion
实验结果显示，Saliency-R1在所有三个任务上均超过了或与现有的鲁棒型开源/闭源的MLLM和专门的SOTA方法持平，证明了本框架在显著性推理方面的有效性。
## 588. `cs.CV` - 免费的概率鲁棒性？重新评估训练基准 [PDF](https://arxiv.org/pdf/2511.01724), [HTML](https://arxiv.org/abs/2511.01724)
### Authors
Yi Zhang,Zheng Wang,Zhen Chen,Wenjie Ruan,Qing Guo,Siddartha Khastgir,Carsten Maple,Xingyu Zhao
### Background
深度学习模型对不可感知的扰动特别脆弱。现有研究主要集中在对抗鲁棒性（AR），通过检查确定性对抗样本（AE）的存在来评估模型在最坏情况下的表现。相比之下，概率鲁棒性（PR）采用统计视角，衡量在随机扰动下预测保持正确的概率。尽管越来越多的研究认为PR是AR的实用补充，但专门用于提高PR的训练方法仍然相对较少，尽管存在一些进展。本文研究发现几个不足之处：缺乏可比的评估标准；尽管有从对抗训练（AT）中获得概率鲁棒性（PR）改善的案例，但在与强大AT基线的比较上仍然有限；以及没有统一框架来比较这些方法的一般化能力。
### Innovation
本文引入了PRBench，这是第一个专门用于评估通过不同鲁棒性训练方法实现概率鲁棒性改进的基准。PRBench使用全面的评估度量标准，包括干净准确率、概率鲁棒性、对抗鲁棒性、训练效率和泛化误差（GE），系统地比较了大多数常见的对抗训练（AT）和概率鲁棒性（PR）目标训练方法。PRBench还提供了这些训练方法的概率鲁棒性泛化误差的理论分析。这些发现揭示了对抗训练方法在综合不同超参数设置下提高概率鲁棒性和对抗鲁棒性方面的灵活性，同时概率鲁棒性目标训练方法始终表现出较低的泛化误差和较高的干净准确率。
### Conclusion
对抗训练方法在适应不同类型的数据集和模型架构方面更加灵活，能在多种超参数设置中提高概率鲁棒性和对抗鲁棒性。相比之下，专门针对概率鲁棒性的训练技术在整个模型中更一致地提高了干净准确率，同时降低了泛化误差。这些发现为评估和选择不同的鲁棒性训练方法提供了宝贵的基准和理论依据。
## 589. `cs.CV` - DWFF-Net：一种具有自适应动态权重的多尺度农田生态系统生境识别方法 [PDF](https://arxiv.org/pdf/2511.11659), [HTML](https://arxiv.org/abs/2511.11659)
### Authors
Kesong Zheng,Zhi Song,Peizhou Li,Shuyi Yao,Zhenxing Bian
### Background
当前缺乏标准化的耕地区域生态系统生境分类系统，现有模型对生境类型覆盖不完整，并且难以有效整合语义和纹理特征，导致多尺度生境（如大型农田块和微生境）的分割精度不足和边界模糊。
### Innovation
本研究开发了一个包含15类耕地区域生态系统生境的全面注释超高清遥感影像数据集，并提出了一种动态加权特征融合网络（DWFF-Net）。该模型通过冻结参数的DINOv3编码器提取基础特征，并通过分析不同类别图像和特征图之间的关系引入一种数据级自适应动态加权策略进行特征融合。解码器通过动态加权计算网络实现多层特征的全面整合，并采用混合损失函数优化模型训练。
### Conclusion
实验结果表明，提出的方法在构建的数据集上实现了69.79%的平均交并比（mIoU）和80.49%的F1分数，分别比基线网络高出2.1%和1.61%。消融实验进一步证明多层特征融合的有效性，显著提高了微生境类别如田埂的交并比。该研究基于自适应多层特征融合建立了耕地区域生境识别框架，实现了低成本的亚米级精度生境制图，并为耕地区域微生境的精细化监测提供了坚实的技术支持。
## 590. `cs.CV` - TinyChemVL：通过高效的视觉标记减少和复杂的反应任务推进化学视觉语言模型 [PDF](https://arxiv.org/pdf/2511.06283), [HTML](https://arxiv.org/abs/2511.06283)
### Authors
Xuanle Zhao,Shuxin Zeng,Xinyuan Cai,Xiang Cheng,Duzhen Zhang,Xiuyi Chen,Bo Xu
### Background
视觉语言模型（VLMs）在通用视觉理解方面表现出色，但在化学领域的应用受限，此前的研究主要集中在文本处理上，忽略了重要的视觉信息，如分子结构。当前直接采用标准VLMs处理化学任务的方法面临计算效率低和任务范围狭窄的两大主要问题：一是处理包含非信息背景的整个化学图像的计算效率低下；二是任务范围仅限于分子水平，限制了化学推理的进步。
### Innovation
本文提出了TinyChemVL，这是一种高效的化学VLM，通过视觉标记减少和反应级别任务来改进模型效率和推理能力。同时，还提出了一种基于反应级别的基准ChemRxn-V，用于评估基于视觉的反应识别和预测任务。结果表明，仅使用4B参数，TinyChemVL在分子和反应任务上均表现出优越性能，且具有更快的推理和训练速度，相较于现有模型。值得注意的是，TinyChemVL在使用视觉标记少1/16的情况下，仍然优于ChemVLM。
### Conclusion
通过共同设计模型架构和任务复杂性，本文构建了旨在化学领域高效的强大VLM。
## 591. `cs.CV` - 野生面向镜头谈话视频的面部时间微动态分析在被动痴呆筛查中的应用 [PDF](https://arxiv.org/pdf/2511.13802), [HTML](https://arxiv.org/abs/2511.13802)
### Authors
Filippo Cenacchi,Longbing Cao,Mitchell McEwan,Deborah Richards
### Background
现有的大多数资源倾向于关注语音或预定的访谈，这限制了其在诊所外的使用，并且使预测依赖于语言和转录。目前的痴呆症筛查方法通常需要有意识的临床干预或研究人员的介入，且受限于特定的语言和情境，难以在大规模、无干预的自然情境中进行广泛分析。
### Innovation
本研究提出了一种基于非语言面部微动态分析的方法，无需言语或文本即可检测早期神经认知变化，从而实现了在大规模、无干预的自然情景下进行痴呆症筛查。通过这种分析，识别并分析了眨眼动态、小嘴下巴运动、注视变化和微妙头部调整等面部时间微动态特征，使得痴呆症筛查能够跨设备、话题和文化进行，并且可以无需临床人员或研究人员的干预。同时，还创建了YT DemTalk数据集，该数据集包含了300段视频，其中150段有自报痴呆的病例，150段健康控制组视频，用于验证模型。
### Conclusion
在YT DemTalk数据集上，通过消融实验发现注视不稳定性和口部/下巴动态是最具信息性的特征，轻量级浅层分类器在痴呆症预测方面的表现（AUC-OROC为0.953，平均精度为0.961，F1分为0.851，准确性为0.857）能够达到很高的精度。
## 592. `cs.CV` - 考虑视觉，文本推理：ARC 的视觉-语言协同 [PDF](https://arxiv.org/pdf/2511.15703), [HTML](https://arxiv.org/abs/2511.15703)
### Authors
Beichen Zhang,Yuhang Zang,Xiaoyi Dong,Yuhang Cao,Haodong Duan,Dahua Lin,Jiaqi Wang
### Background
前沿基础模型如GPT-5和Grok 4在从少量示例中进行抽象推理方面仍存在核心未解问题。现有的方法主要将ARC-AGI视为纯粹的文字推理任务，忽视了人类在解决此类谜题时对视觉抽象的高度依赖。研究表明，直接将ARC-AGI网格转换为图像会因规则执行不精确而降低性能。
### Innovation
提出了两种协同策略：(1) 视觉-语言协同推理 (VLSR)，将ARC-AGI分解为模态对齐的子任务；(2) 模态切换自我校正 (MSSC)，利用视觉对基于文本的推理进行验证以实现内在错误纠正。实验证明，该方法在多种旗舰模型和ARC-AGI任务上相对于纯文本基线提高了最高4.33%。
### Conclusion
我们的发现表明，将视觉抽象与语言推理统一起来是未来基础模型实现通用、类人智能的关键步骤。我们发布了代码，可以在以下链接找到：this https URL.
## 593. `cs.CV` - TimeViper: 一种用于高效理解长视频的混合Mamba-Transformer 视觉-语言模型 [PDF](https://arxiv.org/pdf/2511.16595), [HTML](https://arxiv.org/abs/2511.16595)
### Authors
Boshen Xu,Zihan Xiao,Jiaze Li,Jianzhong Ju,Zhenbo Luo,Jian Luan,Qin Jin
### Background
长视频的理解需要一个高效的模型架构以及处理长时间序列上下文的有效机制。现有模型在处理长时间视频时，往往需要引入新的机制以实现这一目标。
### Innovation
TimeViper 模型采用了一种混合的 Mamba-Transformer 主干，结合了状态空间模型的效率和注意力机制的表达能力。此外，提出了 TransV，这是一种令牌信息转移模块，可以转移并压缩视觉令牌为指令令牌，同时保持多模态理解能力。这些设计使 TimeViper 能够处理超过 10,000 帧的长视频。此外，分析了 Mamba 和 Transformer 层的注意力行为，为混合模型的可解释性提供了新的见解。
### Conclusion
这项工作标志着开发、解释和压缩混合 Mamba-Transformer 架构的第一步。TimeViper 在多个基准上的实验表明，它能够与最先进的模型竞争并扩展帧数。
## 594. `cs.CV` - 基于高斯自适应实例强度建模的点监督面部表情检测 [PDF](https://arxiv.org/pdf/2511.16952), [HTML](https://arxiv.org/abs/2511.16952)
### Authors
Yicheng Deng,Hideaki Hayashi,Hajime Nagahara
### Background
自动面部表情识别的目标是在未裁剪的视频中识别面部表情实例，这对于面部表情分析至关重要。现有方法主要集中在完全监督学习上，依赖于价格高昂且耗时的临时边界注释。
### Innovation
本文研究了一种称为点监督面部表情检测（P-FES）的方法，即在训练时只需要为每个实例提供一个时间戳注释。提出了一种独特的双支架构以优化点监督面部表情检测。双支架构包括一个无类别表达强度分支和一个具有强度意识的尖峰分类分支。为了缓解硬伪标签的限制，通过引入基于高斯的实例适应性强度建模（GIM）模块进行软伪标签生成，用于更可靠的强度监督。此外，还引入了强度意识的对比损失，通过对比中性帧与不同强度的表情帧来增强判别性特征学习并抑制中性噪声。
### Conclusion
在SAMM-LV、CAS(ME)²和CAS(ME)³数据集上的大量实验验证了所提框架的有效性。
## 595. `cs.CV` - 全尺度欺骗立体匹配：自动驾驶中双目深度估计的物理对抗攻击 [PDF](https://arxiv.org/pdf/2511.14386), [HTML](https://arxiv.org/abs/2511.14386)
### Authors
Kangqiao Zhao,Shuo Huai,Xurui Song,Jun Luo
### Background
尽管深度神经模型在自动驾驶感知方面的应用已经证明对对抗样本非常脆弱，但已知的对抗攻击通常利用的是2D斑块，并主要针对单目感知。因此，立体视觉中的双目深度估计对于物理对抗样本的有效性仍知之甚少。
### Innovation
提出了一种在自动驾驶背景下，针对立体匹配模型的第一种纹理增强物理对抗攻击方法。该方法使用3D物理对抗样本（PAE）结合全局迷彩纹理，确保在不同视角的一致性和攻击效果。为了应对立体相机的视差效果，提出了一个新的3D立体匹配渲染模块，允许PAE与双目视觉中的真实世界位置和方向对齐。还提出了一种新的融合攻击，通过细粒度PAE优化无缝地将目标融合到环境中，显著增强了隐蔽性和杀伤力。
### Conclusion
广泛的评估表明，我们的PAE能够欺骗立体模型生成错误的深度信息，从而进一步证明了物理对抗样本在自动驾驶中的应用潜力。
## 596. `cs.CV` - Pistachio: 向合成、平衡和长程视频异常基准迈进 [PDF](https://arxiv.org/pdf/2511.19474), [HTML](https://arxiv.org/abs/2511.19474)
### Authors
Jie Li,Hongyi Cai,Mingkang Dong,Muxin Pu,Shan You,Fei Wang,Tao Huang
### Background
当前，自动检测视频中的异常事件对于现代自主系统至关重要，但现有的视频异常检测(VAD)基准数据集缺乏足够的场景多样性、均衡的异常覆盖和时间复杂性，无法可靠评估实际性能。同时，社区正在转向视频异常理解(VAU)，这需要更深层次的语义和因果推理，但由于其高度的劳动密集型手动标注，难以建立基准。因此，论文引入了Pistachio，一个通过受控的生成式管道构建的新VAD/VAU基准数据集。
### Innovation
Pistachio充分利用了近期视频生成模型的进展，提供了对场景、异常类型和时间叙事的精准控制，从而避免了网络收集数据集的偏见和限制。其管道整合了场景条件下的异常分配、多步骤叙事生成和时间上一致的长段合成策略，生成了41秒的连贯视频，仅需少量的人工干预。实验结果展示了Pistachio的规模、多样性和复杂性，揭示了现有方法面临的新的挑战，并激励未来在动态和多事件异常理解方面的研究。
### Conclusion
Pistachio通过其生成式方法提供了对现有互联网收集数据集的改进，增强了对真实世界性能的评估能力，展示了其在时间和场景上的复杂性和多样性，为未来研究提供了新的基准和挑战。
## 597. `cs.CV` - 无需训练的基于代理推理的视觉定位：连接点 [PDF](https://arxiv.org/pdf/2511.19516), [HTML](https://arxiv.org/abs/2511.19516)
### Authors
Liqin Luo,Guangyao Chen,Xiawu Zheng,Yongxing Dai,Yixiong Zou,Yonghong Tian
### Background
视觉定位是指将文本查询与图像中的特定区域联系起来的任务，对于视觉-语言融合至关重要。现有方法通常依赖于大量特定于任务的注释和微调，这限制了它们在新场景或分布外情况下的泛化能力。
### Innovation
提出了一种名为GroundingAgent的新颖代理视觉定位框架，无需任何特定于任务的微调，通过结合预训练的开放式词汇对象检测器、多模态大型语言模型(MLLM)和大型语言模型(LLM)，采用结构化的迭代推理机制，逐步细化候选区域的语义和空间分析。实验结果显示，GroundingAgent在RefCOCO、RefCOCO+、RefCOCOg等广泛使用的基准上达到平均零样本定位精度65.1%，且仅通过MLLM生成的描述在选择阶段的准确率达到约90%，表明LLM推理能力的重要性。
### Conclusion
GroundingAgent提供了强大的可解释性，清晰地展示了每一步的推理过程，揭示了其决策过程中的见解。
## 598. `cs.CV` - DiffSeg30k：一种用于局部AIGC检测的多轮扩散编辑基准 [PDF](https://arxiv.org/pdf/2511.19111), [HTML](https://arxiv.org/abs/2511.19111)
### Authors
Hai Ci,Ziheng Peng,Pei Yang,Yingxin Xuan,Mike Zheng Shou
### Background
现有的AIGC检测基准主要集中在对整张图像的分类，忽略了基于扩散的局部编辑位置的精确定位。这种背景下，DiffSeg30k提出了一个包含30,000张局部编辑图像的公开数据集，支持细粒度的检测。
### Innovation
提出了DiffSeg30k数据集，包括在野图像、基于SOTA扩散模型的多样局部编辑、多次顺序编辑以及通过VLM管道自动识别的现实编辑场景，推动了从二分类到语义分割的检测转变，展示了基于分割的方法优势。
### Conclusion
DiffSeg30k通过揭示语义分割任务中的挑战以及分割模型在扩散编辑检测中的性能，证明了基于分割方法的潜力与局限性。认为该数据集将促进AIGC内容局部定位的研究进展。
## 599. `cs.CV` - 基于视觉语言增强的基础模型在半监督医学图像分割中的应用 [PDF](https://arxiv.org/pdf/2511.19759), [HTML](https://arxiv.org/abs/2511.19759)
### Authors
Jiaqi Guo,Mingzhen Li,Hanyu Su,Santiago López,Lexiaozi Fan,Daniel Kim,Aggelos Katsaggelos
### Background
半监督学习（SSL）已发展成为医学图像分割的有效范式，减少了对大量专家标注数据的依赖。同时，视觉语言模型（VLMs）展示了强大的泛化能力和少样本学习能力。本文通过引入视觉语言增强的半监督分割助手（VESSA），将VLM集成到SSL框架中，提升医学图像分割的性能。
### Innovation
本文提出了一种新的方法，即通过视觉语言增强的半监督分割助手（VESSA），将基础级的视觉语义理解融入到SSL框架中。该方法分为两个阶段：第一阶段，使用包含黄金标准示例的模板库训练VESSA，作为参考引导分割助手；第二阶段，在最先进的SSL框架中集成VESSA，使其动态交互，提升伪标签质量，从而提供更强的指导。
### Conclusion
通过在多个分割数据集和领域的广泛实验，证明了VESSA增强的SSL可以显著提高分割精度，在极limited标注条件下超越了最先进的基线方法。
## 600. `cs.CV` - EmoFeedback$^2$: 通过基于LVLM的奖励和文本反馈增强连续情感图像生成 [PDF](https://arxiv.org/pdf/2511.19982), [HTML](https://arxiv.org/abs/2511.19982)
### Authors
Jingyang Jia,Kai Shu,Gang Yang,Long Xing,Xun Chen,Aiping Liu
### Background
连续情感图像生成（C-EICG）由于能够生成与用户描述和连续情感值相匹配的图像而迅速发展。然而，现有方法缺乏对生成图像的情感反馈，限制了情感连续性的控制。此外，它们简单地将情感与未经调整的文字对齐，无法根据图像内容适配性地调整情感提示，导致情感准确性不足。
### Innovation
我们提出了一种新颖的生成-理解-反馈强化范式（EmoFeedback$^2$），利用微调的大规模视觉语言模型（LVLM）的推理能力，提供奖励和文本反馈，以生成高质量的与连续情感匹配的图像。具体来说，我们引入了情感感知的奖励反馈策略，使LVLM评估生成图像的情感值并计算与目标情感的奖励，指导生成模型的强化微调，提高图像的情感连续性。此外，我们设计了一种自我提升的文本反馈框架，在该框架中，LVLM迭代分析生成图像的情感内容并适应性地生成下一轮提示的精炼建议，以提高情感的精细度。
### Conclusion
在我们的自定义数据集上进行的广泛实验结果表明，我们的方法能够有效生成具有所需情感的高质量图像，大幅优于现有最先进的方法。代码和数据集即将发布。
## 601. `cs.CV` - 在连续流中使用扩散噪声优化的序列自适应视频预测 [PDF](https://arxiv.org/pdf/2511.18255), [HTML](https://arxiv.org/abs/2511.18255)
### Authors
Sina Mokhtarzadeh Azar,Emad Bahrami,Enrico Pallotta,Gianpiero Francesca,Radu Timofte,Juergen Gall
### Background
本文探讨了基于扩散的视频预测模型，该模型用于预测连续视频流中的未来帧。在这种情况下，模型能够实时观察新的训练样本，并尝试利用这些新样本以提高帧预测的准确性。
### Innovation
本文提出了一种名为Sequence Adaptive Video Prediction with Diffusion Noise Optimization (SAVi-DNO)的方法，该方法连续适应预训练的扩散模型，以便在视频流中进行预测。由于调整大规模扩散模型的参数非常昂贵，因此本文在推理过程中仅优化扩散噪声，同时冻结模型参数，使模型能够自适应地确定合适的采样噪声。
### Conclusion
通过在Ego4D数据集上引入新的评估设置，并验证SAVi-DNO方法的效果，在长时间连续视频的FVD、SSIM和PSNR指标上均显示出性能提升，证明了此方法的有效性。
## 602. `cs.CV` - Restora-Flow: Mask-Guided Image Restoration with Flow Matching [PDF](https://arxiv.org/pdf/2511.20152), [HTML](https://arxiv.org/abs/2511.20152)
### Authors
Arnela Hadzic,Franz Thaler,Lea Bogensperger,Simon Johannes Joham,Martin Urschler
### Background
生成模型利用流动匹配的方法，克服了先进扩散模型长时间采样带来的问题，实现了更灵活的轨迹设计并保持高质量图像生成。现有的基于流动模型的方法在图像恢复任务中取得了有希望的结果，但仍然存在处理时间长或结果过度平滑等问题。
### Innovation
Restora-Flow 是一种无需训练的方法，通过损害遮罩引导流动匹配采样，并加入轨迹校正机制以与受损输入保持一致。该方法在自然和医学数据集上评估了图像恢复任务中的表现，包括基于遮罩损伤的修补、超分辨率和去噪任务，展示了比扩散模型和流动匹配基准方法更好的感知质量和处理时间。
### Conclusion
Restora-Flow 通过损害遮罩有效地指导了流动匹配采样，并结合了轨迹校正机制，证明了在多个图像恢复任务上具有优异的表现，处理时间和感知质量都超越了参考方法。
## 603. `cs.CV` - One-Step Diffusion Transformer for Controllable Real-World Image Super-Resolution [PDF](https://arxiv.org/pdf/2511.17138), [HTML](https://arxiv.org/abs/2511.17138)
### Authors
Yushun Fang,Yuxiang Chen,Shibo Yin,Qiang Hu,Jiangchao Yao,Ya Zhang,Xiaoyun Zhang,Yanfeng Wang
### Background
近期，基于扩散的现实世界图像超分辨率（Real-ISR）技术取得了显著的感知质量提升，但保真度和可控性之间的平衡仍然是一个难题：多步扩散基方法由于生成多样性和随机性导致保真度较低，而一步方法则因保真度特定的微调而丧失了控制灵活性。
### Innovation
提出了一种基于Qwen-Image的一步扩散转换器ODTSR，同时考虑保真度和可控性：新引入的视觉流接收调整噪声的低质量图像（Control Noise），原始视觉流接收一致噪声的低质量图像（Prior Noise），形成了Noise-hybrid Visual Stream (NVS) 设计。此外，ODTSR 进一步采用感知保真度对抗训练（FAA）以增强可控性并实现一步推理。
### Conclusion
广泛的实验表明，ODTSR 不仅在通用的Real-ISR 方面达到了最先进的（SOTA）性能，还在挑战性场景（如中文场景文本图像超分辨率（STISR））中实现了提示可控性，且无需特定数据集进行训练。代码可在 [此链接] 查看。
## 604. `cs.CV` - ReMatch: 通过匹配提升多模态表示以进行多模态检索 [PDF](https://arxiv.org/pdf/2511.19278), [HTML](https://arxiv.org/abs/2511.19278)
### Authors
Qianying Liu,Xiao Liang,Zhiqiang Zhang,Zhongfei Qing,Fengfan Zhou,Yibo Chen,Xu Tang,Yao Hu,Paul Henderson
### Background
以往的方法将MLLM（多模态语言模型）简单地视为编码器，没有利用其生成能力，也没有充分使用其组合推理和世界知识。此外，这些方法通常只在单个视图下进行编码，通常会导致信息损失和表示能力有限。
### Innovation
ReMatch 提出了一种框架，利用MLLM的生成能力来增强多模态检索。该框架通过聊天风格的生成匹配阶段对MLLM进行端到端训练，使用MLLM从多视图输入（包括原始数据及其自身的投影嵌入）自回归地决定相关性，为每一个查询和文档。此外，该框架引入了多个可学习的标记来增强每个输入，生成细粒度的上下文嵌入，这些嵌入是彼此正交的，具有较低的推理成本。该框架的核心创新在于利用MLLM的生成能力进行多模态检索，并提供了实例级别的区分监督，增强了对比损失，保留了MLLM的组合优势。
### Conclusion
ReMatch 在大规模多模态嵌入基准（MMEB）上取得了新的最佳 performance。特别是在五个数据集上的零样本推广结果特别出色，证明了ReMatch的鲁棒性和迁移性能。
## 605. `cs.CV` - ConceptGuard: 通过多模态风险检测实现文本和图像到视频生成中的主动安全性 [PDF](https://arxiv.org/pdf/2511.18780), [HTML](https://arxiv.org/abs/2511.18780)
### Authors
Ruize Ma,Minghong Cai,Yilei Jiang,Jiaming Han,Yi Feng,Yingshui Tan,Xiaoyong Zhu,Bo Zhang,Bo Zheng,Xiangyu Yue
### Background
近年来，视频生成模型的进步使得可以从结合了文本和图像的多模态提示中生成高质量的视频。这些系统增强了可控性，但也带来了新的安全风险，比如有害内容可能源自单一模态或其交互。现有的安全方法往往是文本专有的，需要先验的风险类别知识，或在生成后进行审核，难以主动应对这样的组合性和多模态风险。
### Innovation
ConceptGuard 是一个统一的保护框架，旨在提前检测和减轻多模态视频生成中的不安全语义。它分为两个阶段：一是对比检测模块通过将融合图像-文本输入投影到结构化概念空间来识别潜在的安全风险；二是语义抑制机制通过干预提示的多模态条件来引导生成过程远离不安全的概念。为此，我们还引入了两个新的基准：ConceptRisk 多模态风险训练数据集和 T2VSafetyBench-TI2V，这是第一个专门为文本-图像到视频生成安全设置设计的基准。实验证明，ConceptGuard 在风险检测和安全视频生成方面均优于现有基准，取得最先进的结果。
### Conclusion
全面的基准测试表明，ConceptGuard 在风险检测和安全视频生成方面均超过了现有基准，取得了最先进的成果。我们的代码可以在这个链接中找到。
## 606. `cs.CV` - GFT-GCN: 使用频谱扩散保护隐私的3D人脸网格识别 [PDF](https://arxiv.org/pdf/2511.19958), [HTML](https://arxiv.org/abs/2511.19958)
### Authors
Hichem Felouat,Hanrui Wang,Isao Echizen
### Background
3D面部识别通过捕捉面部几何结构，提供了对光照变化、姿态变化和呈现攻击等变性的鲁棒性解决方法。尽管其强大的抗伪装能力使其适用于高安全性的应用，但存储的生物特征模板的保护仍然至关重要。现有的3D面部识别框架在保护隐私的同时很难平衡准确性。
### Innovation
我们提出了GFT-GCN框架，结合了频谱图学习和基于扩散的模板保护机制。该方法利用图傅里叶变换（GFT）和图卷积网络（GCN）从3D面部网格中提取紧凑且区分性强的频谱特征，通过频谱扩散机制生成不可逆的、可再生的且不可关联的模板。该轻量级的客户端-服务器架构确保原始生物特征数据从未离开客户端设备。
### Conclusion
实验结果表明，GFT-GCN具有高识别准确性和对抗重建攻击的强大能力，有效地平衡了隐私和性能，提供了一种实用的3D面部认证解决方案。
## 607. `cs.CV` - Agent0-VL: 探索工具集成视觉语言推理的自我进化代理 [PDF](https://arxiv.org/pdf/2511.19900), [HTML](https://arxiv.org/abs/2511.19900)
### Authors
Jiaqi Liu,Kaiwen Xiong,Peng Xia,Yiyang Zhou,Haonian Ji,Lu Feng,Siwei Han,Mingyu Ding,Huaxiu Yao
### Background
视觉语言代理在多种跨模态推理任务中取得了显著进展，但其学习仍然受到人类标注监督的限制。最近的自我奖励方法试图通过让模型成为自己的评估者或奖励提供者来克服这一限制。然而，仅基于文本的自我评估难以验证复杂的视觉推理步骤，并且常常遭受评估幻觉。为此，受近年来工具集成推理进步的启发，本文提出了一种自我进化的视觉语言代理Agent0-VL。
### Innovation
Agent0-VL将工具使用不仅纳入推理中，还在自我评估和自我修复中进行，使模型能够通过基于证据的分析进行自我反省、验证和推理的完善。还首次统一了两个协同作用的角色：一个解决者，执行多轮工具集成推理；一个验证者，通过工具支持的批评产生结构化反馈和细粒度的自我奖励。通过自定义的自我进化推理循环，工具基于的验证和强化学习共同对齐推理和评估分布，实现稳定自我改进。实验结果显示，Agent0-VL在几何问题解决和视觉科学分析上比基础模型提高了12.5%。
### Conclusion
Agent0-VL在无需任何人工注释或外部奖励模型的情况下实现了零外部奖励的自我进化，实现了持续自我改进。代码已公开。
## 608. `cs.CV` - Video-R4: 视觉沉思强化文本丰富视频推理 [PDF](https://arxiv.org/pdf/2511.17490), [HTML](https://arxiv.org/abs/2511.17490)
### Authors
Yolo Y. Tang,Daiki Shimada,Hang Hua,Chao Huang,Jing Bi,Rogerio Feris,Chenliang Xu
### Background
理解和解读富文本的视频需要阅读短暂的文字提示，这些提示往往要求反复检查。然而，大多数视频问答模型依赖单次感知固定帧，导致对细腻证据的幻觉和失败。
### Innovation
受到人类如何暂停、放大和重读关键区域的启发，我们提出了一种视频推理LMM，称为Video-R4（视觉沉思强化文本丰富视频推理）。该模型通过迭代选择帧、放大到信息丰富的区域、重新编码检索的像素并更新其推理状态来执行视觉沉思。此外，还构建了两种具有可执行沉思轨迹的数据集：Video-R4-CoT-17k用于监督实践，Video-R4-RL-30k用于强化学习。提出了一种多阶段沉思学习框架，逐步微调一个7B LMM，通过SFT和基于GRPO的强化学习来学习原子和混合的视觉操作。Video-R4-7B在M4-ViteVQA上达到了最先进的结果，并进一步推广到了多页文档问答、幻灯片问答和通用视频问答，证明了迭代沉思是像素为基础的多模态推理的有效范式。
### Conclusion
迭代沉思是像素为基础的多模态推理的有效范式，Video-R4-7B在视频问答任务上达到了最新的技术水平，并在多种问答任务中表现出良好的泛化能力。
## 609. `cs.CV` - 关注事项处放大：基于对比无训练的局部缩放方法 [PDF](https://arxiv.org/pdf/2511.19917), [HTML](https://arxiv.org/abs/2511.19917)
### Authors
Qin Ren,Yufei Wang,Lanqing Guo,Wen Zhang,Zhiwen Fan,Chenyu You
### Background
扩散模型已成为文本到图像生成的主要范式，而在推断时的缩放（TTS）通过在推理过程中分配更多的计算进一步提升了质量。然而，现有的TTS方法在全图像级别上操作，忽视了图像质量在空间上往往是不均匀的这一事实。这种做法导致了不必要的计算在已经满足要求的区域上进行，并且对局部缺陷校正不充分。
### Innovation
本文提出了新的局部TTS方向，适应性地重采样有缺陷的区域同时保持高质量区域，从而大大缩小了搜索空间。这提出了两个核心挑战：准确地定位缺陷和保持全局一致性。为了解决这些挑战，提出了LoTTS，这是一个首个完全无训练框架的局部TTS方法。LoTTS通过质量感知的提示（例如高质区 vs 低质区）下的交叉和自我注意力信号对比，来识别缺陷区域，并进一步将它们细化为连贯的掩码。通过仅扰动缺陷区域并在局部去噪，确保纠正保持在缺陷区域，从而在保证图像其余部分未受影响的情况下保持一致性。
### Conclusion
在SD2.1、SDXL和FLUX上的大量实验表明，LoTTS达到了最先进的性能：它一致地提高了局部质量和全局保真度，同时与Best-of-N采样相比将GPU成本降低了2-4倍。这些发现证明了局部TTS作为推断时缩放扩散模型的一个有前途的新方向。
## 610. `cs.CV` - MeshCone：基于第二阶圆锥规划的几何约束网格增强方法 [PDF](https://arxiv.org/pdf/2412.08484), [HTML](https://arxiv.org/abs/2412.08484)
### Authors
Alexander Valverde
### Background
现代网格生成管道无论是基于学习还是传统的方法，往往会产生需要后期处理才能达到生产质量的网格输出。现有技术存在一个挑战：如何改进这些网格，使其既能保持细部特征，又能够纠正结构缺陷，且能够在多种对象类别中表现稳定。
### Innovation
MeshCone 提出了一种基于凸优化框架的引导式网格细化方法，该方法通过利用参考几何来纠正变形或退化的网格。该方法将问题形式化为第二阶圆锥规划问题，通过优化顶点位置和凸边长正则化，实现几何感知优化，既能保持细部特征，又能纠正结构缺陷。与拉普拉斯平滑和未优化的基础方法相比，MeshCone 在多种对象类别上的表现更为优越，同时保持了亚秒级的推断时间。
### Conclusion
MeshCone 特别适用于参考几何可用的应用场景，如模板网格生成流程、扫描到 CAD 对齐以及资产生产管道的质量保证。实验结果表明，MeshCone 在 56 种不同对象类别上表现出稳健的性能，相比现有技术，其优化质量显著提高且计算效率更高。
## 611. `cs.CV` - VGGTFace: 野生环境下拓扑一致的面部几何重构 [PDF](https://arxiv.org/pdf/2511.20366), [HTML](https://arxiv.org/abs/2511.20366)
### Authors
Xin Ming,Yuxuan Han,Tianyu Huang,Feng Xu
### Background
对于数字角色创建流程而言，重建拓扑一致的面部几何非常重要。现有的方法或者需要繁琐的手工处理，或者无法泛化到野生数据，或者受限于3D Morphable Models的表达能力。因此，需要一种能自动、泛化性好、表达能力强的方法来解决上述问题。
### Innovation
我们提出了VGGTFace，一种自动的基于VGGT的3D基础模型的方法，用于从普通用户拍摄的多视角野生图像中重建拓扑一致的面部几何。该方法通过引入具有像素对准的UV值的Pixel3DMM，克服了VGGT缺乏拓扑信息的问题。通过这一创新，VGGTFace实现了在单块NVIDIA RTX 4090显卡上10秒内对16视图的高质量重建，并展示了对野生数据的强大泛化能力。
### Conclusion
该方法在基准测试中取得了最先进的结果，并且对外来的野生数据具有极其优秀的泛化性能。
## 612. `cs.CV` - 改善实际低资源环境下的视觉提示关键词定位 [PDF](https://arxiv.org/pdf/2409.06013), [HTML](https://arxiv.org/abs/2409.06013)
### Authors
Leanne Nortje,Dan Oneata,Gabriel Pirlogeanu,Herman Kamper
### Background
视觉提示关键词定位（VPKL）的目标是在语音集合中找到图像查询中描述的词汇出现位置。这在没有转录资的低资源语言（例如未被书写的语言）中是有用的。此前的研究表明，可以通过在配对图像和未标记语音上训练视觉地指导的语音模型来实现VPKL，但所有实验都在英语上进行，且使用转录提供正负样本对。
### Innovation
本文提出了一个少样本学习方案，可以在没有转录的情况下自动挖掘正负样本对，结果显示在英语上性能下降很小。同时，本文首次尝试在真实低资源语言Yoruba上进行VPKL，结果显示评分合理，但在Yoruba中由于挖掘不够准确，性能下降较大。
### Conclusion
研究在英语上的实验表明改进方案的性能几乎未减，在低资源语言Yoruba上的实验表明，新的少样本学习方案可以有效地应用于实际低资源环境下的语音数据，但也表明在未被书面语言的环境中实施VPKL仍具有挑战性。
## 613. `cs.CV` - STARFlow-V: 使用规范化流进行端到端视频生成建模 [PDF](https://arxiv.org/pdf/2511.20462), [HTML](https://arxiv.org/abs/2511.20462)
### Authors
Jiatao Gu,Ying Shen,Tianrong Chen,Laurent Dinh,Yuyang Wang,Miguel Angel Bautista,David Berthelot,Josh Susskind,Shuangfei Zhai
### Background
规范化流（NFs）是用于连续数据的端到端基于似然的生成模型，近年来在图像生成方面取得了令人鼓舞的进步。然而，在视频生成领域，由于时空复杂度和计算成本的显著增加，最先进的系统几乎完全依赖于扩散模型。本文回顾了这一设计空间，提出了基于规范化流的视频生成器STARFlow-V，具有端到端学习、鲁棒因果预测和原生似然估计等显著优势。
### Innovation
STARFlow-V基于最近提出的STARFlow，使用时空潜空间和全局-局部架构，在不破坏因果依赖的情况下保留了丰富的帧内相互作用。此外，提出了流分数匹配方法，增强轻量级因果去噪器，以自回归方式改进视频生成一致性。为了提高采样效率，STARFlow-V采用了视频感知雅可比迭代方案，将内部更新重新表述为并行迭代，同时保持因果关系。由于其可逆结构，同一模型可支持文本到视频、图像到视频及视频到视频的生成任务。
### Conclusion
STARFlow-V在视觉保真度和时间一致性方面表现出强大的结果，且相对于基于扩散的基线系统，具有实际的采样效率。这些结果表明，NFs能够实现高质量的自回归视频生成，为构建世界模型提供了有前途的研究方向。代码和生成样本可在提供的链接中获取。
## 614. `cs.CV` - 比较生成学习方法用于湍流代理 [PDF](https://arxiv.org/pdf/2411.16417), [HTML](https://arxiv.org/abs/2411.16417)
### Authors
Claudia Drygala,Edmund Ross,Francesca di Mare,Hanno Gottschalk
### Background
数值模拟湍流流动在流体力学中面临着巨大挑战，高分辨率技术如直接数值模拟（DNS）和大涡模拟（LES）通常由于高计算成本而不实际，特别是在解决技术相关问题时。最近，机器学习的进步，特别是生成概率模型的出现，为替代湍流提供了一种有希望的替代方法。
### Innovation
本研究致力于探索三种生成模型——变分自编码器（VAE）、深度卷积生成对抗网络（DCGAN）和去噪扩散概率模型（DDPM）在模拟固定圆柱周围的伏特卡姆漩涡街（von Kármán vortex street）的二维投影以及实验数据集（柱阵列的漩涡流）中的应用。通过直接数值模拟（LES）获得模拟案例的训练数据，通过颗粒图像 velocimetry（PIV）获得实验案例的训练数据。评估每个模型捕获湍流统计属性和空间结构的能力。
### Conclusion
研究表明，DDPM和DCGAN能够有效地复制所有流动分布，表明它们有望成为高效的湍流替代工具。特别指出尽管DCGAN在训练上更具挑战性（如模式崩溃等问题），但它们具有最快的推理和训练时间，需要的训练数据更少，并且生成的结果与输入流最接近。相比之下，VAE虽然快速训练（可快速生成样本）但不能产生足够的结果；而DDPM虽然有效但推理和训练时间都相对较慢。
## 615. `cs.CV` - SKEL-CF: Coarse-to-Fine Biomechanical Skeleton and Surface Mesh Recovery [PDF](https://arxiv.org/pdf/2511.20157), [HTML](https://arxiv.org/abs/2511.20157)
### Authors
Da Li,Jiping Jin,Xuanlong Yu,Wei Liu,Xiaodong Cun,Kai Chen,Rui Fan,Jiangang Kong,Xi Shen
### Background
现有的3D人体模型如SMPL在人体姿态和形状估计方面取得了显著进展，但由于简化的人体动力学限制了生物力学的真实性。最近提出的SKEL模型通过使用解剖准确的骨骼重新装配SMPL解决了这个问题，但直接估计SKEL参数由于训练数据有限、视角模糊和人体关节复杂性而仍然具有挑战性。
### Innovation
本文提出了一种粗到细框架SKEL-CF，用于估计SKEL参数。该框架采用基于转换器的编码器-解码器架构，首先预测粗粒度的相机和SKEL参数，然后逐层逐步精细调整。为了确保解剖学一致的监督，将现有基于SMPL的4DHuman数据集转换为与SKEL对齐的版本4DHuman-SKEL，提供了用于估计SKEL的高质量训练数据。此外，为了解决深度和尺度的模糊性，将相机建模显式纳入SKEL-CF管道，并在不同视角下验证其重要性。
### Conclusion
通过广泛的实验验证了SKEL-CF的有效性。在挑战性的MOYO数据集上，SKEL-CF实现了85.0 MPJPE / 51.4 PA-MPJPE，显著优于之前的SKEL基先前最先进模型HSMR (104.5 / 79.6)。本文确立了SKEL-CF作为人体运动分析的可扩展且解剖学忠实的框架，填补了计算机视觉和生物力学之间的差距。我们已在项目页面提供了实现: this https URL。
## 616. `cs.CV` - CrossEarth-Gate: Fisher-Guided Adaptive Tuning Engine for Efficient Adaptation of Cross-Domain Remote Sensing Semantic Segmentation [PDF](https://arxiv.org/pdf/2511.20302), [HTML](https://arxiv.org/abs/2511.20302)
### Authors
Shilei Cao,Ziyang Gong,Hehai Lin,Yang Liu,Jiashun Cheng,Xiaoxing Hu,Haoyuan Liang,Guowen Li,Chengwei Qin,Hong Cheng,Xue Yang,Juepeng Zheng,Haohuan Fu
### Background
在遥感（RS）中，参数高效微调（PEFT）已经成为了激活基础模型在下游任务中泛化表示能力的关键方法。然而，现有的专门针对PEFT的方法在应用于大规模地球观测任务时经常失效，因为它们难以完全处理遥感数据中固有的多重和不可预测的领域差距（例如，空间、语义和频率偏移）。
### Innovation
本文提出了CrossEarth-Gate，它包括两个主要贡献。首先，它建立了一个全面的RS模块工具箱，用于解决多重领域差距问题，包括空间模块、语义模块和频率模块。其次，它开发了一种基于Fisher信息的自适应选择机制，该机制在这些工具箱上运行。该机制通过度量每个模块对任务特定梯度流的贡献来量化其重要性，并动态激活最关键模块，以最大化适应效果和效率。
### Conclusion
综合实验验证了该方法的有效性和可泛化性，其中CrossEarth-Gate在16个跨领域基准测试中实现了遥感语义分割的最佳性能。该工作的代码将被发布。
## 617. `cs.CV` - CroMe: 使用跨模态三元变换器和度量学习的多模态假新闻检测 [PDF](https://arxiv.org/pdf/2501.12422), [HTML](https://arxiv.org/abs/2501.12422)
### Authors
Eunjee Choi,Junhyun Ahn,XinYu Piao,Jong-Kook Kim
### Background
近年来，多模态假新闻检测受到了越来越多的关注。现有的方法依赖于单一模态的数据独立编码，并忽视了利用高级技术捕捉模态内关系和整合模态间相似性的优势。
### Innovation
提出了跨模态三元变换器和度量学习的多模态假新闻检测（CroMe）方法。CroMe 使用固定图像编码器和大型语言模型的 Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models (BLIP2) 作为编码器，以捕捉详细的文本、图像和联合的图像-文本表示。度量学习模块采用代理锚点方法捕捉模态内关系，特征融合模块通过跨模态三元变换器进行有效集成。最终，融合特征通过分类器预测内容的真实性。
### Conclusion
实验表明，CroMe 在多模态假新闻检测方面表现出色。
## 618. `cs.CV` - 使用预训练变换器在对比和非对比CT上实现心脏亚结构的一般化分割 [PDF](https://arxiv.org/pdf/2505.10855), [HTML](https://arxiv.org/abs/2505.10855)
### Authors
Aneesh Rangnekar,Nikhil Mankuzhy,Jonas Willmann,Chloe Choi,Abraham Wu,Maria Thor,Andreas Rimner,Harini Veeraraghavan
### Background
现有的AI分割算法在进行放射治疗规划时，如果应用于与训练数据集有不同特征的病例，分割效果会下降。本研究旨在开发一种适用于不同影像对比度和扫描位置的肺癌和乳腺癌患者的新的心脏亚结构分割方法。
### Innovation
研究团队开发了一种混合变换器卷积网络，以提高对心脏亚结构的分割准确性。该模型在训练数据集中结合了对比和非对比CT图像，从而解决了现有方法在不同病例特征下的分割性能下降问题。研究表明，平衡模型在多种影像协议和患者特征下表现出 robust 几何和剂量准确性，且与患者年龄和体质量指数无关。此外，这种方法比传统的具有相同性能的方法所需标注的训练案例数减少了64%。
### Conclusion
研究证实，该混合变换器卷积网络在多种影像条件下能够实现一般化的心脏亚结构分割，并在临床部署中具有实用性。这种方法通过预训练结合平衡的NCCT和CECT数据分布，显著减少了所需的标记案例数量。
## 619. `cs.CV` - LMLCC-Net：一种用于CT扫描中肺结节恶性程度预测的新颖HU基强度过滤的半监督深度学习模型 [PDF](https://arxiv.org/pdf/2505.06370), [HTML](https://arxiv.org/abs/2505.06370)
### Authors
Tasnia Binte Mamun,Adhora Madhuri,Nusaiba Sobir,Taufiq Hasan
### Background
肺癌是全球导致患者死亡的主要原因之一。早期诊断CT图像中的恶性肺小结节对降低疾病死亡率和发病率具有显著影响。
### Innovation
本文提出了一种新颖的深度学习框架LMLCC-Net，用于通过3D CNN结合HU基强度过滤从CT扫描图像中分类结节。此方法考虑了HU强度剖面，这是先前文献中未充分利用的。LMLCC-Net通过多个分支提取特征，每个分支使用单独的可学习HU强度过滤阶段。此外，本文还提出了一种半监督学习方案来标记模糊案例，并开发了一个轻量级模型来分类结节。实验在LUNA16数据集上进行。
### Conclusion
实验结果显示，所提出的LMLCC-Net在区分肺结节时达到91.96%的分类准确率、92.94%的灵敏度和94.07%的曲线下面积，与现有方法相比具有改进的表现。该方法有助于放射科医生更准确地分类肺结节，提高患者的护理水平。
## 620. `cs.LG` - 跨被试EEG解码的原型引导非范例持续学习 [PDF](https://arxiv.org/pdf/2511.20696), [HTML](https://arxiv.org/abs/2511.20696)
### Authors
Dan Li,Hye-Bin Shin,Yeon-Woo Choi
### Background
由于EEG信号在不同个体之间存在显著差异，已有的知识常常因为新个体的引入而被覆盖。当前的研究主要依赖历史数据缓冲区的方法来防止遗忘，但隐私问题或内存限制使得这种方法难以实现。已有方法无法在不访问历史EEG样本的情况下保留先验知识。
### Innovation
提出了Prototype-guided Non-Exemplar Continual Learning (ProNECL)框架，该框架通过构建类级别原型来总结每个个体的有辨别力的表示，并通过跨个体特征对齐和知识蒸馏方法逐步调整新的特征空间与全局原型记忆，从而在不访问历史EEG样本的情况下保留先验知识。
### Conclusion
在BCI竞赛IV 2a和2b数据集上验证了ProNECL框架，该框架能够有效平衡知识保留与适应性，在跨个体持续EEG解码任务中实现了更好的性能。
## 621. `cs.CV` - UniGame: Turning a Unified Multimodal Model Into Its Own Adversary [PDF](https://arxiv.org/pdf/2511.19413), [HTML](https://arxiv.org/abs/2511.19413)
### Authors
Zhaolong Su,Wang Lu,Hao Chen,Sharon Li,Jindong Wang
### Background
统一多模态模型（UMMs）在理解和生成方面表现出了很强的能力，但它们仍然存在根本性的不一致：理解偏好紧凑的嵌入，而生成偏好重建丰富的表示。这种结构上的权衡会导致决策边界不一致，跨模态一致性下降，以及在分布和对抗性变换下的脆弱性增强。
### Innovation
本文提出了一种自对抗后训练框架UniGame，通过在共享的标记接口上应用轻量级搅乱器，使生成分支能够主动寻求并挑战脆弱的理解，使模型变成其自身的对手。该框架提高了连贯性（+4.6%），理解能力（+3.6%），生成能力（+0.02），以及离分布（+4.8%）和对抗性鲁棒性（+6.2%）
### Conclusion
该框架对所有架构都是通用的，引入的额外参数少于1%，且与现有的后训练方法相结合，是增强未来多模态基础模型的一致性、稳定性和统一能力的一般性和有效原则。
## 622. `cs.LG` - 现代霍普菲尔德网络隐藏状态在Transformer中的作用 [PDF](https://arxiv.org/pdf/2511.20698), [HTML](https://arxiv.org/abs/2511.20698)
### Authors
Tsubasa Masumura,Masato Taki
### Background
基于霍普菲尔德网络的联想记忆模型和基于键值机制的自注意力机制是深度学习中记忆机制研究的流行方法。指出现代霍普菲尔德网络（MHN）在绝热近似下的状态更新规则与Transformer的自注意力层一致。本文在此基础上，进一步研究MHN和自注意力之间的关系。
### Innovation
引入了一个新的注意力机制——现代霍普菲尔德注意（MHA），通过将MHN的隐藏状态加入到自注意力中，建立了霍普菲尔德网络和Transformer之间的更广泛形式的对应关系。实验表明MHA显著改善了深度Transformer中的秩塌缩和标记均匀性问题，并且系统地提高了精度，而无需增加训练参数。
### Conclusion
研究结果表明，霍普菲尔德网络可以为改进Transformer架构提供一种新的视角，霍普菲尔德网络的隐藏状态在Transformer中发挥重要作用。
## 623. `cs.CV` - LightMem: Lightweight and Efficient Memory-Augmented Generation [PDF](https://arxiv.org/pdf/2510.18866), [HTML](https://arxiv.org/abs/2510.18866)
### Authors
Jizhan Fang,Xinle Deng,Haoming Xu,Ziyan Jiang,Yuqi Tang,Ziwen Xu,Shumin Deng,Yunzhi Yao,Mengru Wang,Shuofei Qiao,Huajun Chen,Ningyu Zhang
### Background
大规模语言模型（LLMs）虽然具有显著的性能，但在动态和复杂环境中，它们难以有效利用过往的交互信息。现有的记忆系统通常会引入显著的时间和计算开销。LightMem是为了解决这个问题而设计的，旨在平衡记忆系统的性能和效率。
### Innovation
LightMem 采用类似于人类记忆模型（Atkinson-Shiffrin 模型）的方式，将记忆分为感知记忆、主题感知短期记忆和长期睡眠时更新记忆三个阶段，通过压缩和分组信息、结构化组织内容及离线更新机制来提高效率。
### Conclusion
在LongMemEval和LoCoMo测试中，使用GPT和Qwen作为骨干网络，LightMem持续超越强基线，提高问答准确率高达7.7% / 29.3%，减少总token使用量高达38倍 / 20.9倍，API调用减少高达30倍 / 55.5倍，测试时间成本完全在线的情况下，token减少高达106倍 / 117倍，API调用减少高达159倍 / 310倍。代码可以在指定链接处获取。
## 624. `cs.CV` - DEMIST: 分解多流潜扩散模型用于定量髓鞘图合成 [PDF](https://arxiv.org/pdf/2511.12396), [HTML](https://arxiv.org/abs/2511.12396)
### Authors
Jiacheng Wang,Hao Li,Xing Yao,Ahmad Toubasi,Taegan Vinarsky,Caroline Gheen,Joy Derwenskus,Chaoyang Jin,Richard Dortch,Junzhong Xu,Francesca Bagnato,Ipek Oguz
### Background
定量磁转移（qMT）成像能够提供对髓鞘敏感的生物标记物，如池大小比（PSR），这对于多发性硬化症（MS）的评估非常宝贵。然而，qMT需要专门的20-30分钟的扫描。本文探讨了一种使用标准T1w和FLAIR图像合成PSR图的新方法，该方法使用3D隐扩散模型和三种互补的条件机制。
### Innovation
本文提出了一种名为DEMIST的方法，该方法使用标准T1w和FLAIR图像合成PSR图，采用了隐扩散模型和三种互补的条件机制，分别是：（i）语义令牌通过交叉注意力；（ii）空间分尺度残差提示通过3D ControlNet分枝；（iii）自适应LoRA调制注意力。此外，还引入了边缘感知损失项来保留病灶边界和保量化一致性。
### Conclusion
通过在163个扫描数据（来自99个受试者）上进行五折交叉验证，发现该方法在多个指标上优于VAE、GAN和扩散基线模型，生成了更清晰的边界和更好的定量一致性。开源代码可在提供。
## 625. `cs.LG` - 使用重启后验采样的扩散逆问题求解 [PDF](https://arxiv.org/pdf/2511.20705), [HTML](https://arxiv.org/abs/2511.20705)
### Authors
Bilal Ahmed,Joseph G. Makin
### Background
逆问题是科学和工程中的基础问题，目标是从不完整或有噪声的测量中推断出潜在信号或状态。近年来，扩散模型由于能够捕捉复杂的数据分布，被用作逆问题中的强隐式先验。然而，现有的基于扩散的逆问题方法通常依赖于后验分布的强近似，需要通过评分网络进行昂贵的梯度反向传播，或者局限于线性测量模型。
### Innovation
本文提出了重启后验采样 (RePS) 的通用和高效框架，用于使用预训练的扩散模型解决线性和非线性逆问题。RePS 基于先前在无条件扩散中证明可以提高样本质量的重启采样理念，并将其扩展到后验推断。该方法采用适用于任何可微测量模型的条件 ODE，并引入简化重启策略以在采样过程中减少累积的近似误差，避免通过评分网络的反向传播，从而大幅降低计算成本。
### Conclusion
RePS 在各种逆问题中实现了比现有基于扩散的基线更快的收敛速度和更优的重建质量，包括线性和非线性设置。
## 626. `cs.LG` - 大型语言模型中的主动错误切片发现 [PDF](https://arxiv.org/pdf/2511.20713), [HTML](https://arxiv.org/abs/2511.20713)
### Authors
Minhui Zhang,Prahar Ijner,Yoav Wald,Elliot Creager
### Background
大规模语言模型（LLMs）在处理特定数据子集时往往会表现出系统的错误，这些错误子集被称为错误切片。例如，一个切片可能对应于某种特定的人口统计数据，模型在这个细分人群中识别有毒评论的准确度较低。识别错误切片对于理解并改进模型来说至关重要，但也是一个挑战。减轻手动注释所需工作量的一种方法是积极地对那些很可能属于同一切片的错误进行分组，并利用有限的注释器访问来验证所选样本是否表现出相同类型的模型错误。
### Innovation
本文将这种减小手动注释需求的方法形式化为“主动切片发现”，并通过毒性分类问题中的人类定义的切片探索了其实用性。研究了不同特征表示和主动学习算法在主动切片发现中的效果，结果发现基于不确定性的主动学习算法表现最好，能够在使用有效数据信息的2-10%的情况下达到竞争力的准确性，超越了基准。
### Conclusion
在多个切片上，我们发现基于不确定性的主动学习算法是最有效的，能够使用可用切片成员信息的2-10%达到竞争性的准确率，同时在性能上显著优于基准。
## 627. `cs.CV` - BRIC：在测试时连接运动规划与物理控制 [PDF](https://arxiv.org/pdf/2511.20431), [HTML](https://arxiv.org/abs/2511.20431)
### Authors
Dohun Lim,Minji Kim,Jaewoon Lim,Sungchan Kim
### Background
当前的人体动作生成方法虽然能够根据文本和场景条件生成多样性和表现力强的动作，但往往会导致在模拟中的执行脱轨，因为它们通常会产生物理上不可行的输出。现有的测试时适应（Test-Time Adaptation, TTA）方法无法有效解决这个问题，导致环境中存在执行偏差。因此，研究一种能够在测试时动态适应物理控制器并保持预训练技能的框架具有重要意义。
### Innovation
提出了BRIC框架，该框架能够通过解决基于扩散模型的惯性运动规划和基于强化学习的物理控制器之间的执行偏差来实现长期人体动作生成。BRIC采用了一种动态适应策略，通过损失函数防止灾难性遗忘，同时保留预训练技能。此外，BRIC还引入了一种在信号空间轻量级的测试时指导机制，来引导扩散模型而不更新其参数。这两种策略结合使用，确保了在不同环境中的长期执行具有连贯性和物理可行性。
### Conclusion
BRIC在多种长期任务（如动作组成、障碍物避免和人-scene交互）中得到了验证，并在所有任务上都实现了最先进的性能。这种框架在不同环境和任务中的有效性表明，BRIC是一种有效的测试时适应解决方案，能够实现长期和物理上可行的人体动作生成。
## 628. `cs.CV` - 三维思考：真实世界中的类人视觉搜索 [PDF](https://arxiv.org/pdf/2511.20351), [HTML](https://arxiv.org/abs/2511.20351)
### Authors
Heyang Yu,Yinan Han,Xiangyu Zhang,Baiqiao Yin,Bowen Chang,Xiangyu Han,Xinhao Liu,Jing Zhang,Marco Pavone,Chen Feng,Saining Xie,Yiming Li
### Background
人类依赖头部控制（cephalomotor）和眼部控制（oculomotor）的协同作用，以高效地在360°环境中搜索视觉信息。然而，现有的视觉搜索方法大多局限于静态图像中，忽略了身体和3D世界的互动。如何开发能够绕过现实世界硬件限制、在体感上与人类效率相当的视觉搜索智能体？为此，本文提出了基于类人身体的视觉搜索方法，这种方法利用类人智能体主动旋转头部来搜索沉浸式世界中的物体或路径。为了研究视觉搜索在真实复杂场景中的表现，本文构建了一个新基准H* Bench，涵盖交通枢纽、大型零售空间、城市道路和公共机构等复杂的野外场景，其中需要高级的空间推理能力。之前的实验揭示了顶级的定制模型在物体和路径搜索上的不足，成功率仅为30%左右。
### Innovation
本文提出了类人视觉搜索方法，它利用类人智能体主动旋转头部来搜索沉浸式世界中的物体或路径。此外，本文还构建了H* Bench基准，旨在测试和提升在复杂真实世界场景中智能体的视觉搜索能力。通过使用后训练技术增强开源的Qwen2.5-VL模型，实验结果表明，在物体搜索方面成功率达到47.38%，在路径搜索方面达到24.94%。这些结果揭示了路径搜索的固有难度，并指出在现实生活中无缝集成MLLM agent仍面临巨大挑战。
### Conclusion
实验结果不仅展示了在真实世界中构建MLLM智能体的有希望的路径，还量化了这一过程中的巨大挑战。路径搜索的低上限表明了高级空间常识需求的高难度，这也是我们仍面临的巨大挑战之一。
## 629. `cs.LG` - CHiQPM：校准层次可解释图像分类 [PDF](https://arxiv.org/pdf/2511.20779), [HTML](https://arxiv.org/abs/2511.20779)
### Authors
Thomas Norrenbrock,Timo Kaiser,Sovan Biswas,Neslihan Kose,Ramesh Manuvinakurike,Bodo Rosenhahn
### Background
可解释的人工智能模型是值得信赖的人工智能在关键安全领域的一种有前途的方法。除了全局解释，详细的局部解释对于有效辅助推理期间的人类专家至关重要。本文旨在提供一种全新的全局和局部可解释性方法Calibrated Hierarchical QPM (CHiQPM)，以促进人类与人工智能的互补作用。
### Innovation
CHiQPM通过对比性解释大多数类别实现了卓越的全局可解释性，并提供了一种新颖的层次解释，这种解释更接近人类的推理过程，从而内置了一个可解释的符合性预测方法（Conformal prediction, CP）。全面评估表明，CHiQPM不仅保持了99%与不可解释模型相同的精确度，还以竞争力的方式提供了校准集合预测，同时提供了层次解释下的可解释预测。
### Conclusion
CHiQPM在不牺牲整体准确性的前提下，实现了可解释性。该方法展示了在图像分类任务中，如何以竞争性效率提供可解释的预测结果，这对关键安全领域的应用场景具有重要意义。
## 630. `cs.LG` - 梯度下降算法综述 [PDF](https://arxiv.org/pdf/2511.20725), [HTML](https://arxiv.org/abs/2511.20725)
### Authors
Deng Fucheng,Wang Wanjie,Gong Ao,Wang Xiaoqi,Wang Fan
### Background
本文关注深度学习中优化算法的实际配置需求，重点分析了五种主要算法：SGD、小批量SGD、Momentum、Adam和Lion。文章系统地分析了每种算法的核心优势、局限性和关键实际建议。
### Innovation
本文旨在深入了解这些优化算法，为学术研究和工程实践中的优化算法的选择、参数调整和性能提升提供标准化参考，帮助解决不同类型模型和各种训练场景下的优化挑战。
### Conclusion
本文帮助读者深入了解各种优化算法的具体应用场景与局限性，为模型优化提供指导建议。
## 631. `cs.LG` - 时空轨迹基础模型——近期进展与未来方向 [PDF](https://arxiv.org/pdf/2511.20729), [HTML](https://arxiv.org/abs/2511.20729)
### Authors
Sean Bin Yang,Ying Sun,Yunyao Cheng,Yan Lin,Kristian Torp,Jilin Hu
### Background
时空轨迹基础模型（TFMs）作为一种新兴的范式，已经在多种科学领域中展现出强大的数据分析和知识发现能力。然而，尽管大型语言模型等基础模型（FMs）取得了显著进展，对TFMs的研究仍然相对不足。因此，该论文旨在系统性地总结和探讨TFMs的最新进展。
### Innovation
本文通过对现有的TFM方法进行了分类归纳，并对其优点和缺陷进行了批判性的分析。同时，指出了当前TFMs研究中的关键挑战，并提出了未来发展的潜在研究方向。这有助于推动基于更加稳健、负责任和可迁移的时空轨迹基础模型的发展，提高在时空任务（ST）中的适应性和泛化能力。
### Conclusion
本文提供了对近期TFMs研究的全面概述，并指出未来研究需要解决的关键开放问题，以促进时空通用智能的全面发展。
## 632. `cs.LG` - 无需数据的后剪枝准确性恢复 [PDF](https://arxiv.org/pdf/2511.20702), [HTML](https://arxiv.org/abs/2511.20702)
### Authors
Chinmay Tripurwar,Utkarsh Maurya,Dishant
### Background
模型剪枝是一种广泛采用的技术，用于降低深度神经网络（DNNs）的计算复杂性和内存占用。然而，全局无结构剪枝通常会导致准确性显著下降，通常需要在原来的训练数据集上进行微调以恢复性能。在医疗保健或金融等隐私敏感领域，由于法规限制（如GDPR和HIPAA）部署后可能无法访问原始训练数据，这使得资源共享和微调变得困难。
### Innovation
本文提出了一种无需数据的知识蒸馏框架，旨在解决模型压缩与数据隐私之间的差距。具体而言，通过逆向传播批量归一化（BN）统计信息，利用DeepInversion生成保护隐私的“梦想”图像，这些图像作为转移集从原先的教师模型的知识转移到修剪的学生模型。
### Conclusion
在CIFAR-10数据集上对不同架构（ResNet、MobileNet、VGG）进行实验结果显示，本文方法在不使用任何实际数据点的情况下，显著恢复了剪枝过程中损失的准确性。
## 633. `cs.LG` - 初始化偏见对深度神经网络训练动力学的影响 [PDF](https://arxiv.org/pdf/2511.20826), [HTML](https://arxiv.org/abs/2511.20826)
### Authors
Nicholas Pellegrino,David Szczecina,Paul W. Fieguth
### Background
未经训练的大神经网络，在随机初始化后，倾向于青睐一小部分类，对这些少数类赋予较高的预测概率，而对于其他所有类则给出大约为零的概率。这种偏见，称为初始猜测偏见，会影响模型在早期训练动态中的行为，此时模型正在适应数据的粗略结构。损失函数的选择对于这些早期动态的展开有着重大影响。
### Innovation
研究发现两种针对标签错误的鲁棒性损失函数（Blurry 和 Piecewise-zero loss）在面对初始偏见时，可能无法控制训练的方向。研究强调了初始猜测偏见可能与训练方案的各种组成部分之间的相互作用，并揭示了选择损失函数对网络早期训练阶段的显著影响。
### Conclusion
选择的损失函数对神经网络的早期训练阶段有着巨大影响，需要仔细考虑初始猜测偏见如何与训练方案的各个部分相互作用，以避免训练方向失控。
## 634. `cs.LG` - 飞行测试中的符合性安全监控：数据驱动安全学习案例研究 [PDF](https://arxiv.org/pdf/2511.20811), [HTML](https://arxiv.org/abs/2511.20811)
### Authors
Aaron O. Feldman,D. Isaiah Harp,Joseph Duncan,Mac Schwager
### Background
在飞行测试中，飞行员需要在飞行测试中执行各种机动，但由于飞机参数具有不确定性，可能会产生意外的安全违反情况。因此，飞行员需要在安全违反之前就能得到明确的中止机动的标准。研究者使用离线的随机轨迹模拟来学习飞行员短期安全风险的倒校准统计模型，以解决这一问题。
### Innovation
研究提出了一个数据驱动的方法来实现运行时的安全监控，在飞行测试中对飞行员的短期安全风险进行倒校准统计模型的学习，该方法包括预测未来状态的模型、最近邻模型来分类预测状态的安全性以及通过符合性预测进行分类器校准。这种方法在具有不确定参数的飞行动力学模型的测试中得到了评估，结果显示该方法可以准确识别不安全场景，并在预判风险分类方面优于基线方法。
### Conclusion
研究证明了其方法能够在理论保证下可靠地识别不安全场景，并且在前瞻性风险分类方面优于基准方法。该方法对飞行测试中的数据驱动安全监测研究具有重要意义。
## 635. `cs.LG` - Primal：统一确定性准正交哈希和流形学习框架 [PDF](https://arxiv.org/pdf/2511.20839), [HTML](https://arxiv.org/abs/2511.20839)
### Authors
Vladimer Khasia
### Background
该研究基于现有的随机特征映射方法，如随机傅里叶特征，并提出了一个定性的特征映射框架Primal。这种框架利用了质数平方根的数论独立性，构建出稳健且可调节的向量表示。与标准的随机投影方法相比，Primal方法利用Besicovitch性质，通过非重复的随机频率调制来增强哈希特性。
### Innovation
Primal框架包含了两种不同的算法变体：(1) 静态Prime方法（StaticPrime），通过时间位置编码产生接近理论威尔特下界的数值正交性；(2) 动态Prime方法（DynamicPrime），这是一种用于输入依赖特征映射的可调节投影层，还通过单一的尺度参数σ将两类不同的数学实用性类别统一起来。在低频段，该方法可以等距核映射，有效线性化非凸几何结构（例如螺旋），从而实现高保真信号重构和压缩传感；而在高频段，则产生混沌相位缠绕，将投影转化为适用于超维计算和隐私保护分布式学习的一次性哈希。
### Conclusion
实验证明，Primal框架在保持正交性和分布紧致性方面优于标准化的归一化高斯基线，确立了其作为一种计算高效且数学严谨的随机矩阵投影替代方案的地位。
## 636. `cs.LG` - ST-PPO：多轮对话训练中稳定化的变分策略优化 [PDF](https://arxiv.org/pdf/2511.20718), [HTML](https://arxiv.org/abs/2511.20718)
### Authors
Chenliang Li,Adel Elmahdy,Alex Boyd,Zhongruo Wang,Alfredo Garcia,Parminder Bhatia,Taha Kass-Hout,Cao Xiao,Mingyi Hong
### Background
PPO在多轮对话和推理任务中的大量语言模型（LLMs）训练中已经得到了广泛应用，但在采样级别上其性能经常不稳定且容易崩溃。
### Innovation
通过实证分析，作者发现了PPO在多轮环境中出现不稳定性的两个主要原因：（1）令牌级别的重要性采样与多轮环境中明显的回合级阶段不相符；（2）由于批评家没有学会评估某些状态动作对，导致不准确的优势估计，从而产生高方差梯度和不稳定的更新。为此，作者提出了两种互补的稳定技术：回合级重要性采样和裁剪偏置校正。通过这些组件的不同组合，论文提出了三种变体：Turn-PPO（仅回合级采样）、S-PPO（对令牌级PPO应用裁剪偏置校正）以及ST-PPO（回合级采样与裁剪偏置校正结合）。实验表明，ST-PPO和S-PPO在多轮搜索任务中能够防止性能崩溃，维持较低的剪切率，同时比标准令牌级PPO实现更高的任务性能。
### Conclusion
结合回合级重要性采样与裁剪偏置校正提供了一种实用且可扩展的解决方案，用于稳定多轮LLM代理训练。
## 637. `cs.LG` - 在具有潜在状态的模拟器中选择信念状态近似 [PDF](https://arxiv.org/pdf/2511.20870), [HTML](https://arxiv.org/abs/2511.20870)
### Authors
Nan Jiang
### Background
状态复位是模拟器的基本但常被忽视的能力，它支持基于样本的规划并通过复位到先前遇到的模拟状态，以及利用真实数据进行模拟器校准。然而，在复杂模拟器中实现状态复位往往不简单，特别是当模拟器包含潜在变量（状态）时，需要通过给定可观测历史后的后验分布来采样潜在状态，即信念状态。尽管精确采样很难实现，但可以构造多种近似信念状态采样器，然而如何在仅有对模拟器的采样访问的情况下选择其中最优的一个，仍是一个问题。
### Innovation
本文显示了这个问题可以归约为一种一般条件分布选择任务，并在此基础上发展了一种新的算法和分析方法。文章提出了两种不同的信念状态选择方法：潜在状态基选择，直接针对潜在状态的条件分布；观测基选择，针对由观测引起的分布。值得注意的是，这两种方法对下游展开方法的支持不同：观测基选择在最自然的展开方法（单次复位）下可能失效，但在一种不太常见的展开方法（重复复位）下能保证正确。
### Conclusion
本文提出现有的算法选择和理论细微关系，在看似简单的问题中揭示了丰富的研究前景，讨论了诸如分布偏移和采样策略的选择等问题。
## 638. `cs.LG` - 从风险学习：基于大型语言模型的先验知识指导下的关键安全场景生成 [PDF](https://arxiv.org/pdf/2511.20726), [HTML](https://arxiv.org/abs/2511.20726)
### Authors
Yuhang Wang,Heye Huang,Zhenhua Xu,Kailai Sun,Baoshen Guo,Jinhua Zhao
### Background
自主驾驶在罕见的长尾事件和复杂的多智能体互动中面临重大挑战，这些事件在真实世界数据中很少见但对健全部分安全至关重要。现有的数据驱动或规则驱动方法难以全面覆盖这些高风险事件。
### Innovation
本文提出了一种高保真场景生成框架，该框架结合了条件变分自编码器(CVAE)和大型语言模型(LLM)。CVAE通过大规模自然驾驶数据集的历史轨迹和地图信息编码来学习潜在的交通结构，生成物理上一致的基础场景。LLM则作为对抗推理引擎，解析无结构的场景描述并生成特定领域的损失函数，动态引导场景生成，涵盖不同的风险水平。这种方法综合了知识驱动的优化，确保生成的场景既现实又可控。
### Conclusion
本文框架在CARLA和SMARTS中的广泛实验表明，显著提升了高风险和长尾事件的覆盖范围。提高了模拟和现实交通分布的一致性，并使自主驾驶系统接触到现有规则驱动或数据驱动方法无法实现的更具挑战性的交互。这些结果开创了一条新的安全验证途径，通过系统在罕见但至关重要的事件下的理性压力测试实现了这一目标。
## 639. `cs.LG` - 基于扩散生成的合成图预训练Transformer模型在阿尔茨海默病预测中的应用 [PDF](https://arxiv.org/pdf/2511.20704), [HTML](https://arxiv.org/abs/2511.20704)
### Authors
Abolfazl Moslemi,Hossein Peyvandi
### Background
早期和准确地检测阿尔茨海默病（AD）对于建立有效的干预措施和改善患者结果至关重要。然而，开发可靠的人工智能模型（包括机器学习模型）以进行AD诊断具有挑战性，原因包括有限的带标签数据、多中心的异质性以及类别不平衡等问题。
### Innovation
本文提出了一种基于Transformer的诊断框架，将基于扩散的合成数据生成方法与图表示学习和迁移学习相结合。通过对真实世界的NACC数据集的训练，不仅生成了大规模且与多模式临床和神经影像学特征分布匹配的合成群体数据，而且使不同诊断类别的诊断更具平衡性。利用特定模态的图变换器编码器进行预训练，学习出具有鲁棒性和类可区分特性的表示，并将其固定，同时在原始NACC数据的嵌入表示上训练神经分类器。文中还采用MMD、Fréchet距离和能量距离等度量计算真实数据集和合成数据集的分布对齐情况，并补充鉴别性分析，利用校准和固定特异性灵敏度分析等手段进行评估。实验结果显示，本文提出的方法优于标准基线方法，包括早融合和晚融合的深度神经网络以及多模态图基模型MaGNet，在NACC的受试者内部交叉验证上取得了更高的AUC、准确率、灵敏度和特异度。
### Conclusion
此结果表明，基于扩散生成的合成数据预训练结合图变换器预训练的多项选择题可以提升临床预测任务中样本有限且类别不平衡情况下模型的泛化能力。
## 640. `cs.LG` - 探索用于脓毒症治疗的强化学习的时间步长 [PDF](https://arxiv.org/pdf/2511.20913), [HTML](https://arxiv.org/abs/2511.20913)
### Authors
Yingchuan Sun,Shengpu Tang
### Background
现有研究对脓毒症管理中的强化学习（RL）大多沿用了将患者数据聚合为4小时时间步长的设定。尽管研究者们担心这种时间步长的粗略性可能扭曲患者动态，导致次优治疗策略，但这种粗略时间步长实际带来的问题尚缺乏实际验证。
### Innovation
本工作通过设计动作映射方法，进行了1、2、4、8小时四种时间步长的实证对比实验，以相同线下RL管道进行对照比较。通过不同的政策学习设置下的跨时间步长模型选择，量化时间步长对状态表示学习、行为克隆、策略训练和离线评估的影响。结果表明，不同的学习设置下性能趋势不同，但在使用静态行为策略学习更细时间步长（1小时和2小时）的策略能实现总体最佳性能和稳定性。
### Conclusion
本研究强调了时间步长在医学健康领域线下RL中的核心设计选择，并提供了与传统4小时设置不同的替代方案的证据。
## 641. `cs.LG` - 使用球谐傅里叶神经算子的太阳风自回归代理建模 [PDF](https://arxiv.org/pdf/2511.20830), [HTML](https://arxiv.org/abs/2511.20830)
### Authors
Reza Mansouri,Dustin Kempton,Pete Riley,Rafal Angryk
### Background
太阳风是从太阳冠冕持续流出的带电粒子流，塑造了日球层并影响地球附近的空间系统。准确预测如高速流和日冕物质抛射这样的特征对于空间天气预报至关重要。然而，传统的三维磁流体力学（MHD）模型需要大量计算资源，从而限制了对边界条件不确定性的快速探索。
### Innovation
引入了第一个使用球谐傅里叶神经算子（SFNO）的太阳风径向速度稳态的自回归机器学习代理模型。该模型通过预测有限的径向范围并在迭代中向外传播解，提高了远距离地区的预测准确性，相较于一步法，具有优越性。相比于数值HUX代理模型，SFNO展现了更优或相当的性能，同时提供了一个灵活、可训练、数据驱动的替代方案，为高保真度太阳风建模提供了新的方法。
### Conclusion
使用球谐傅里叶神经操作符的自回归机器学习代理模型在太阳风建模中展现出优越性能，为高保真度的太阳风建模提供了创新的技术手段，同时提供了可访问的源代码和更多可视化结果。
## 642. `cs.LG` - 以预训练获得：无需干净标签的鲁棒学习 [PDF](https://arxiv.org/pdf/2511.20844), [HTML](https://arxiv.org/abs/2511.20844)
### Authors
David Szczecina,Nicholas Pellegrino,Paul Fieguth
### Background
使用有噪标签训练深度网络会导致模型泛化能力差和准确率降低，这是因为模型过度适应了标签噪声。现有方法在利用有噪标签学习时，通常依赖于数据集的一个干净标签子集。本文通过利用自我监督学习（SSL）预训练特征抽取网络，并在有噪数据集上进行标准监督训练，避免了需要干净标签子集的数据要求。
### Innovation
提出了通过使用SSL方法进行预训练，无需依赖干净标签子集就可以训练出更鲁棒的模型，并且在CIFAR-10和CIFAR-100数据集上的实验证明了该方法的有效性。
### Conclusion
自我监督预训练在所有噪声率下都能提高分类准确率，并增强下游标签错误检测（F1和平衡精度）。性能差异在噪声率增加时更加明显，展示了其鲁棒性改进。在低噪声水平下，该方法达到了与ImageNet预训练模型相当的结果，并在高噪声条件下表现出优于ImageNet预训练模型的效果。
## 643. `cs.LG` - 临时图学习方法中的表示完整性 [PDF](https://arxiv.org/pdf/2511.20873), [HTML](https://arxiv.org/abs/2511.20873)
### Authors
Elahe Kooshafar
### Background
现实世界中的系统，如航空路线和加密货币传输，可以自然地表示为动态图，其拓扑结构会随时间变化。传统基准测试主要通过特定任务的度量标准评估动态图学习方法，但往往没有考虑嵌入是否忠实地反映了网络的变化。本研究旨在解决这一问题，引入了表示完整性这一概念，并开发了一组指标来衡量嵌入变化与图变化的契合度。
### Innovation
提出了表示完整性这一概念，并开发了一组用于衡量嵌入变化与图变化相符程度的指标。通过合成场景评估这些指标的表现，最终推荐了一个指标，该指标通过了所有理论和实证测试。该指标特别一致地将理论上稳定的UASE和IPP模型排名最高。此外，还利用该指标对常见动态图学习模型的表示完整性进行了比较研究，发现神经方法在特定场景下的优势，并与一阶链路预测AUC存在显著正相关。
### Conclusion
提出的完整性框架为动态图表示质量提供了一种任务无关的、可解释的评估工具，为模型选择和未来架构设计提供了更明确的指导。
## 644. `cs.LG` - 物理学操控：物理基础模型跨域概念的因果控制 [PDF](https://arxiv.org/pdf/2511.20798), [HTML](https://arxiv.org/abs/2511.20798)
### Authors
Rio Alexa Fear,Payel Mukhopadhyay,Michael McCabe,Alberto Bietti,Miles Cranmer
### Background
近期的研究显示，大型语言模型（LLMs）发展出了不仅反映具体实体，还能反映人类可理解的抽象概念和行为的内部表示。此外，这些隐藏特征能够被直接操控以引导模型的行为。但目前尚不清楚这种现象是否仅限于学习结构化数据（如语言、图像）的模型，还是基础模型的普遍特性。现有研究探索了这一现象在物理基础模型中的应用。
### Innovation
该工作借鉴了在LLMs中识别复杂行为所对应单个方向的最新研究成果，从物理聚焦的基础模型中提取不同物理状态下的激活向量，并计算这些状态间的差异表示（delta representations）。这些delta张量作为激活空间中的概念方向，编码特定的物理特征。通过在推理时注入这些概念方向，可以操控模型的预测结果，从而实现对物理行为的因果控制，例如在模拟中加入或移除特定物理特征。这一发现表明，科学基础模型学习到了物理原则的普遍表示，而不仅仅是表面的相关性和模式。
### Conclusion
该研究证明了科学基础模型能够通过一般化的表示学习到物理原理，并非仅依赖模拟中的表面相关模式。这一研究开辟了理解与控制科学基础模型的新途径，并对AI驱动的科学发现具有重要意义。
## 645. `cs.LG` - 具体化量化解耦 [PDF](https://arxiv.org/pdf/2511.20927), [HTML](https://arxiv.org/abs/2511.20927)
### Authors
Vitoria Barin-Pacela,Kartik Ahuja,Simon Lacoste-Julien,Pascal Vincent
### Background
近期的理论工作已经确立了量化因子在任何差分同胚下的无监督可识别性。该理论假设量化阈值对应着潜在因子概率密度的轴对齐的突变。通过约束学习映射具有轴对齐突变的密度，我们就可以恢复因子的量化。然而，将这一高级原则转化为有效的实践标准仍然具有挑战性，特别是在非线性映射的情况下。
### Innovation
本文开发了一个准则来实现无监督解耦，通过鼓励轴对齐的突变。突变表现为因子估计密度中的尖锐变化，并且我们称之为悬崖。按照理论中独立突变的定义，本文鼓励悬崖的位置在某个因子上与其它因子的值无关。实验结果显示，本文的方法Cliff在所有解耦基准上均优于其他基线，证明了其在无监督解耦方面的有效性。
### Conclusion
我们的方法Cliff在所有的解耦基准上都超过了基线，显示了其在无监督解耦中的有效性和潜力。
## 646. `cs.LG` - 行为克隆策略的数据集中毒攻击 [PDF](https://arxiv.org/pdf/2511.20992), [HTML](https://arxiv.org/abs/2511.20992)
### Authors
Akansha Kalra,Soumil Datta,Ethan Gilmore,Duc La,Guanhong Tao,Daniel S. Brown
### Background
行为克隆（BC）是一种通过监督学习从专家示范中训练顺序决策策略的流行框架。随着这些策略在现实世界的应用增加，它们的鲁棒性和潜在漏洞成为一个重要的关注点。本研究首次分析了清理标签后门攻击在BC策略上的有效性。
### Innovation
本文引入了一种新的基于熵的测试时间触发攻击，通过识别最有效的关键状态，显著降低了策略性能。研究发现即使在数据集仅被轻微污染的情况下，训练出的行为克隆策略在部署时也会表现出看似较高的任务性能，但实际上对后门触发攻击非常脆弱。这凸显了对行为克隆策略的鲁棒性研究需求的紧迫性。
### Conclusion
行为克隆策略在受轻微污染的数据集上训练时，表现出诱人的接近基线的任务性能，但实际上在部署过程中高度容易受到后门触发攻击的影响。因此，急需进一步研究行为克隆策略的鲁棒性，尤其是当大规模数据集用于训练现实世界中的网络物理系统的策略时。
## 647. `cs.LG` - 语义优越性与法医学效率：深度学习与法医语言学在商业电子邮件欺骗检测中的比较分析 [PDF](https://arxiv.org/pdf/2511.20944), [HTML](https://arxiv.org/abs/2511.20944)
### Authors
Yaw Osei Adjei(Kwame Nkrumah University of Science and Technology)
### Background
商业电子邮件欺骗（BEC）是一种精巧的社会工程威胁，它操控组织结构并利用心理漏洞，导致重大经济损失。根据2024年FBI的网络犯罪报告，BEC的年度调整损失超过29亿美元，显示出重大的经济不对称：假阴性的成本远高于假阳性的成本（大约是1到5480倍）。
### Innovation
本文探讨了两种BEC检测范式：法医心理语言流使用CatBoost分析具有高可解释性和低延迟的心理语言线索，和语义流使用DistilBERT进行基于深度学习的上下文语言理解，虽然计算成本较高，但准确率更高。DistilBERT在对抗性中毒数据集（N=7990）上实现卓越检测（AUC=1.0000，F1=0.9981），且具有可接受的实时延迟（7.403毫秒）。CatBoost则以8.4倍更低的延迟（0.885毫秒）达到竞争性检测（AUC=0.9905，F1=0.9486），消耗极少的计算资源。优化后，两种方法均通过成本敏感学习显示出超过99.96%的投资回报率，通过显著减少假阴性并降低相关财务损失。
### Conclusion
对于拥有GPU基础设施的组织，DistilBERT提供更高的准确性。CatBoost更适用于边缘部署或成本敏感环境，因为它具有相似的安全性和较低的操作成本。两种方法都通过成本敏感学习展示了高额的投资回报率。
## 648. `cs.LG` - Probabilistic Hash Embeddings for Online Learning of Categorical Features [PDF](https://arxiv.org/pdf/2511.20893), [HTML](https://arxiv.org/abs/2511.20893)
### Authors
Aodong Li,Abishek Sankararaman,Balakrishnan Narayanaswamy
### Background
该研究关注具有动态词汇表的流式数据中的分类特征，其中词汇表随时间变化，甚至可以无限增长。通常使用特征哈希作为预处理步骤，将这些分类值映射到固定大小的特征空间，以便学习其嵌入。尽管这些方法主要针对离线或批量环境开发和评估，本研究将注意力转向在线设置。在传统的框架中，确定性嵌入对分类项的到达顺序敏感，并容易忘记之前的学习结果，导致性能下降。
### Innovation
提出了一种概率哈希嵌入（PHE）模型，该模型将哈希嵌入视为随机变量，并应用贝叶斯在线学习来从数据中增量学习。该算法能够处理不断演化的分类项词汇表，对新项具有适应性且不会忘记旧项，具有固定参数集且不随流中唯一观测值的数量增长，且对项到达顺序不变。实验结果证明了PHE在分类、序列建模和推荐系统中的优越性能，同时保持了高内存效率。
### Conclusion
研究表明，PHE算法能够处理动态变化的词汇表，无需忘记旧信息即可适应新信息，具有较小的参数量，且与项到达顺序无关。实验验证了PHE在在线学习中的优越性能，同时保持了高内存效率。
## 649. `cs.LG` - 交错环境重置提高大规模并行在线强化学习 [PDF](https://arxiv.org/pdf/2511.21011), [HTML](https://arxiv.org/abs/2511.21011)
### Authors
Sid Bharthulwar,Stone Tao,Hao Su
### Background
大规模并行GPU模拟环境加速了强化学习的研究，特别是在使用Proximal Policy Optimization (PPO)等在线强化学习算法时。为了最大化吞吐量，通常使用较短的每策略更新采样周期，从而增加更新到数据的比率。但是在这种情况下，标准的同步重置会引入有害的非平稳性，歪曲学习信号并导致训练不稳定。
### Innovation
提出了一种简单而有效的交错重置技术，即在任务时间范围内以不同时间点初始化和重置环境。这使得训练批次具有更大的时间多样性，减少了由于同步采样引起的非平稳性。通过对具体示例环境的字符化分析，该技术被应用于高端机器人环境，显著提高了样本效率、加快了墙钟收敛时间，并提高了最终性能。此外，该技术随着并行环境数量的增加具有更好的扩展性，相比于简单的同步重置方法。
### Conclusion
交错重置技术对于增强环境中的样本效率和最终性能具有显著的改善作用，尤其在高端机器人环境中表现明显，并且该技术的扩展性优于简单的同步重置方法。
## 650. `cs.LG` - 使用XLM-RoBERTa对ChatGPT内容的检测：一种新的方法 [PDF](https://arxiv.org/pdf/2511.21009), [HTML](https://arxiv.org/abs/2511.21009)
### Authors
Md Tasnin Tanvir,Dr Santanu Kumar Dash,Ishan Shahnan,Nafis Fuad,Tanvir Rahman,Abdullah Al Faisal,Asadullah Al Mamun
### Background
随着生成型人工智能技术（如ChatGPT）的广泛应用，区分AI生成的文字和人类原创内容的挑战变得越来越紧迫。本研究专注于开发一种方法来检测完全由AI生成的内容，以及识别经过AI重新措辞的人类文本。
### Innovation
本研究采用了一种全面的方法，使用XLM-RoBERTa，这是一种先进的多语言转换器模型，来进行AI生成内容的检测。方法包括严格的预处理、特征提取（涉及困惑度、语义和可读性特征），并基于平衡的人类和AI生成文本数据集对XLM-RoBERTa模型进行 fine-tuning。研究发现，困惑度和基于注意力的特征在区分人类和AI生成文本方面至关重要。
### Conclusion
研究人员表明，该模型在各类文本风格上表现出高度准确性和稳健性，提供了维护学术诚信的工具，并对促进人工智能伦理中增强透明度和问责制做出了贡献。未来的研究方向包括探索其他高级模型并扩展数据集以提高模型的泛化能力。
## 651. `cs.LG` - 使用多头注意力变换器预测奶牛的产奶生涯 [PDF](https://arxiv.org/pdf/2511.21034), [HTML](https://arxiv.org/abs/2511.21034)
### Authors
Mahdi Saki,Justin Lipman
### Background
奶农需要根据客观评估决定是否保留或淘汰奶牛，这一过程中涉及奶牛的适应环境能力、持续产奶次数等多方面因素，具有重要的环境和经济效益。因此，需要一个能有效预测奶牛寿命的评估模型来支持决策。
### Innovation
开发了一种基于多头注意力变换器的AI驱动模型，利用从出生到现在的多元时间序列数据，大大提升了预测奶牛产奶生涯的能力，模型预测的决定系数达到83%，展示了其在奶牛群管理中的实际应用潜力。
### Conclusion
研究通过使用多头注意力变换器预测奶牛寿命的AI模型取得了显著成效，展示了该模型在实际奶牛群管理中的应用价值。
## 652. `cs.LG` - 进化样本权重用于偏见缓解：优化目标取决于有效性 [PDF](https://arxiv.org/pdf/2511.20909), [HTML](https://arxiv.org/abs/2511.20909)
### Authors
Anil K. Saini,Jose Guadalupe Hernandez,Emily F. Wong,Debanshi Misra,Jason H. Moore
### Background
机器学习模型在训练时可能会无意中产生带有偏见的预测，这会对边缘化社区产生负面影响。重新加权是一种可以在模型训练时通过为每个数据点分配权重来缓解这种偏见的方法。本文比较了三种生成这些权重的方法：进化算法（GA）演化权重、仅使用数据集特征计算权重以及在所有数据点上分配相同权重。
### Innovation
本文提出了一种利用进化算法（GA）生成样本权重的方法，并将其与仅根据数据集特性计算权重以及等权分配三种方法进行了比较。通过使用配对的预测和公平性指标（作为GA进化过程中的优化目标），评估了模型在准确度和公平性两个方面上的表现。结果显示，进化权重可以产生更符合公平性和预测性能平衡的模型，但效果与所使用的优化指标密切相关。
### Conclusion
通过实验发现，使用准确性和人口公正性差异度量优化的方案会为更多数据集提供进化权重显著优于其他加权策略的结果。然而，进化样本权重的效果在很大程度上取决于所选择的优化目标。
## 653. `cs.LG` - 使用自回归条件生成对抗网络进行概率性森林火灾蔓延预测 [PDF](https://arxiv.org/pdf/2511.21019), [HTML](https://arxiv.org/abs/2511.21019)
### Authors
Taehoon Kang,Taeyong Kim
### Background
气候变暖加剧了野火的发生频率和严重程度，快速和准确预测火势蔓延对于有效的减缓和响应至关重要。物理仿真器如FARSITE可以提供高保真的预测，但其计算密集型特性限制了其在实时决策中的应用；现有的深度学习模型往往产生过于平滑的预测，无法捕捉野火传播的复杂非线性动态。
### Innovation
本文提出了一种自回归条件生成对抗网络（CGAN）用于概率性野火蔓延预测。通过将预测任务形式化为自回归问题，该模型学习序列状态转移，确保长期预测的稳定性。实验结果表明，提出的基于CGAN的模型在总体预测准确性和火灾边界界定方面优于传统的深度学习模型。对抗学习使模型能够捕捉野火蔓延的强烈非线性和不确定性，而非仅仅拟合像素平均值。此外，自回归框架有助于对野火演化的系统性时间预测。
### Conclusion
基于CGAN的自回归框架提高了野火蔓延预测的准确性和物理可解释性，为时间敏感的反应和疏散规划提供了有力的基础。
## 654. `cs.LG` - 在大规模工业推荐系统中用于时间分布泛化的概率框架 [PDF](https://arxiv.org/pdf/2511.21032), [HTML](https://arxiv.org/abs/2511.21032)
### Authors
Yuxuan Zhu,Cong Fu,Yabo Ni,Anxiang Zeng,Yuan Fang
### Background
推荐系统中的时间分布漂移（TDS）会导致长期准确性下降，但现有工业实践中仍依赖于周期性的增量训练，这种方法难以捕捉稳定和瞬时模式。现有方法如不变学习和自我监督学习虽然提供了部分解决方案，但也存在时间泛化不稳定、表示坍塌或数据利用效率低等问题。
### Innovation
提出了一种称为ELBO$_text{TDS}$的概率框架，该框架可以无缝集成到大规模工业推荐系统中的增量学习流水线中。通过统计分析实际生产数据中的关键变化因素，设计了一种简单有效的数据增强策略来扩展训练支持，并通过因果图建模时间推荐场景，引入了一种基于因果结构的自我监督变分目标ELBO$_text{TDS}$。
### Conclusion
通过广泛的实验理论和实证分析，证明了该方法在时间泛化方面具有优越性，每用户GMV提高了2.33%，并成功部署在Shopee商品搜索中。代码可在提供的链接处获得。
## 655. `cs.LG` - RAVQ-HoloNet: 适应率矢量量化全息图压缩 [PDF](https://arxiv.org/pdf/2511.21035), [HTML](https://arxiv.org/abs/2511.21035)
### Authors
Shima Rafiei,Zahra Nabizadeh Shahr Babak,Shadrokh Samavi,Shahram Shirani
### Background
全息图对于AR/VR应用具有显著潜力，但其采用受到数据压缩需求高的限制。现有基于深度学习的方法通常在单个网络中缺乏速率适应性。
### Innovation
提出了一个速率自适应矢量量化框架RAVQ-HoloNet，实现了在低比特率和超低比特率条件下高保真的重建，其性能优于当前最先进的方法，尤其是在低比特率下，我们的方法的BD-Rate超过-33.91%，BD-PSNR达到1.02 dB。
### Conclusion
该方法通过一个适应率的矢量量化框架提高了全息图压缩的有效性，实现了高精度重建，特别是针对低比特率的应用场景。
## 656. `cs.LG` - 基于时间维度的高效扩散规划 [PDF](https://arxiv.org/pdf/2511.21054), [HTML](https://arxiv.org/abs/2511.21054)
### Authors
Jiaming Guo,Rui Zhang,Zerun Li,Yunkai Gao,Shaohui Peng,Siming Lan,Xing Hu,Zidong Du,Xishan Zhang,Ling Li
### Background
扩散规划是一种从离线数据中学习高性能策略的有希望的方法。然而，现有的工作在每个时间步生成新的计划，这会导致显著的计算开销并降低决策频率，频繁的计划切换也可能影响性能。
### Innovation
本文提出了一种名为Temporal Diffusion Planner (TDP)的时间维度扩散规划器，通过在时间维度上分布去噪步骤来提高决策效率。TDP最初生成一个逐渐变模糊的初始计划。在每个后续时间步，TDP不生成全新的计划，而是使用少量的去噪步骤更新之前的计划。还引入了自动化重新规划机制，以防止计划与现实之间的重大偏离。实验表明，与每个时间步生成新的计划的方法相比，TDP提高了11-24.8倍的决策频率，同时实现了更高的或相当的性能。
### Conclusion
本文提出的Temporal Diffusion Planner (TDP)通过在时间维度上分布去噪步骤，提高了决策效率。它在初始计划逐渐变模糊的基础上，在后续时间步更新计划，减少了平均去噪步骤的数量。TDP还引入了自动化重新规划机制，以防止计划与现实之间的重大偏离。实验结果证明，TDP在决策频率和性能方面相较于现有方法有显著提升。
## 657. `cs.LG` - FANoise: 单值自适应噪声调制以实现鲁棒的多模态表示学习 [PDF](https://arxiv.org/pdf/2511.20997), [HTML](https://arxiv.org/abs/2511.20997)
### Authors
Jiaoyang Li,Jun Fang,Tianhao Gao,Xiaohui Zhang,Zhiyuan Liu,Chao Liu,Pengzhang Liu,Qixia Jiang
### Background
表示学习是现代机器学习的核心，推动了诸如文本检索和多模态理解等应用的发展。然而，学习强大的且通用的表示仍然是一个挑战。尽管先前的研究表明，主动噪声注入（一种形式的数据增强方法）可以提高编码性能，但大多数现有方法依赖启发式或静态噪声，忽视了特征分布训练过程中的动态性质。
### Innovation
本文从梯度和特征分布两个角度系统研究了噪声在表示学习中的作用，提出了FANoise，一种新的特征自适应噪声注入策略。通过利用对比学习的动态特性，FANoise有效地减少了噪声的负面影响，同时保留了其益处。在理论上得到支持的框架下，全面的实验表明，FANoise在各种基础VLM模型上的一系列多模态任务中始终提高了总体性能。
### Conclusion
在理论上得到支持的框架下，FANoise在各种基础VLM模型上的一系列多模态任务中始终提高了总体性能。
## 658. `cs.LG` - 在总体变异距离下估计Ising模型 [PDF](https://arxiv.org/pdf/2511.21008), [HTML](https://arxiv.org/abs/2511.21008)
### Authors
Constantinos Daskalakis,Vardis Kandiros,Rui Yao
### Background
本文关注的是基于总变异距离估计包含n个变量的Ising模型的问题，给定的是来自模型的l个独立样本。虽然该问题的统计复杂性已得到充分理解，但在计算和统计效率方面，尚未找到统一的框架，特别是在树形图、相互作用矩阵符合高斯分布或其特征值集中在较小区间的情况下，虽然取得了一些进展，但仍缺乏适用于多项式时间估计的统一方法。
### Innovation
本文的主要贡献是对两类Ising模型进行了统一分析：一类是具备有界算子范数并满足修改后的Log-Sobolev不等式（MLSI）的模型，以及另一类是相互作用矩阵的无穷范数有界（或有界宽度）的模型。通过这些普遍结果，本文在多个方面提供了多项式时间算法和最优或接近最优的样本复杂性保证。
### Conclusion
本文利用张量不等式、测度分解和浓度界等多种工具，证明了在各类设置中的多项式时间算法和样本复杂性保证。通过对这两类模型的分析，取得了在总体变异距离下的最优或接近最优估计方法，填补了计算和统计效率上的空白。
## 659. `cs.LG` - 环境特定子目标图增强规划在基于大语言模型的开放世界强化学习中的应用 [PDF](https://arxiv.org/pdf/2511.20993), [HTML](https://arxiv.org/abs/2511.20993)
### Authors
Shanwei Fan
### Background
大语言模型（LLMs）在强化学习（RL）中的高级规划能力是通过将任务分解为子目标来实现的，但实际应用中受限于规划与执行不一致的问题，这反映了抽象计划与具体环境兼容的行为之间的差距。这种不一致源于两个相关限制：（1）LLMs经常生成在目标环境中不可行或不相关的子目标，这是因为缺乏环境特定的知识；（2）单LLM规划将生成和自我验证混淆在一起，导致过度自信但不可靠的子目标，这在执行过程中经常失败。
### Innovation
本文提出了一种名为Subgoal Graph-Augmented Actor-Critic-Refiner (SGA-ACR)的框架，该框架结合了环境特定的子目标图和结构化的实体知识，以及一个多LLM规划管道，该管道明确分离生成、批评和修正过程，以生成可执行和可验证的子目标。进一步提出执行监控器，提供辅助奖励并自适应更新子目标图，以维持计划和行动之间的对齐。
### Conclusion
在“Crafter”这个开放世界游戏中的22个不同任务上进行的实验表明，所提出的方法的有效性。
## 660. `cs.LG` - Post-training LLMs的离线数据选择与在线自我优化生成的统一理解 [PDF](https://arxiv.org/pdf/2511.21056), [HTML](https://arxiv.org/abs/2511.21056)
### Authors
Quan Xiao,Tianyi Chen
### Background
在调整大型语言模型（LLMs）以适应特定下游任务时，离线数据选择和在线自我优化生成是提高数据质量的关键步骤。现有方法 typically 没有从优化的角度来综合考虑这两步，论文通过 bilevel 数据选择（针对验证数据集的离线数据选择）和在线自我优化生成（作为选择当前响应中与验证数据最佳匹配的模型的适应步骤），提出了一个新的框架。
### Innovation
论文通过 bilevel 数据选择框架在理论上证明了其有效性和比未经筛选直接混合法的性能优势。通过将离线数据与验证加权的在线生成相结合，提高了微调性能。论文首次展示了这种框架的有效性，特别是对质量增强和安全意识 LLM 微调的有效验证。
### Conclusion
论文提出的方法通过结合离线数据和验证加权的在线生成，增强了微调性能。通过实验验证了该方法在质量提升和安全意识 LLM 微调中的有效性。
## 661. `cs.LG` - 打破安全与能力权衡：可验证奖励增强学习在LLMs中维持安全边界 [PDF](https://arxiv.org/pdf/2511.21050), [HTML](https://arxiv.org/abs/2511.21050)
### Authors
Dongkyu Derek Cho,Huan Song,Arijit Ghosh Chowdhury,Haotian An,Yawei Wang,Rohit Thekkanal,Negin Sokhandan,Sharlina Keshava,Hannah Marlowe
### Background
使大型语言模型（LLMs）适应下游任务时通常会面临安全与能力的基本权衡，即提高任务性能会损害安全对齐，即使在良性数据集上也是如此。标准方法如监督微调（SFT）和基于人类反馈的强化学习（RLHF）也无法避免这种下降。虽然使用可验证奖励的强化学习（RLVR）被证明是一种有潜力的替代方案，但其对安全性的影响尚不清楚。本研究首次全面分析了RLVR的安全性特性。
### Innovation
本研究首次从理论和实证角度全面分析了RLVR的安全性属性。理论分析中推导出了在KL约束优化下安全漂移的上限，并证明了安全退化的条件可以消除。实验部分展示了RLVR能够同时增强推理能力并维持或改进安全边界。还包括了全面的消融研究，探讨了优化算法、模型规模和任务领域对结果的影响。
### Conclusion
本研究的发现挑战了普遍认为的安全与能力不可兼得的假设，表明特定的训练方法可以在同时实现安全与能力提升之间取得平衡，为推理能力强大的LLMs的安全部署提供了见解。
## 662. `cs.LG` - Gated KalmaNet：通过测试时岭回归实现淡出记忆层 [PDF](https://arxiv.org/pdf/2511.21016), [HTML](https://arxiv.org/abs/2511.21016)
### Authors
Liangzu Peng,Aditya Chattopadhyay,Luca Zancato,Elvis Nunez,Wei Xia,Stefano Soatto
### Background
线性状态空间模型（SSMs）由于具有恒定的内存和线性计算成本，成为softmax Attention的一种有效替代方案。然而，这类模型仅维护一个损耗、逐渐衰减的过去摘要，这在依赖于回忆的任务中通常表现较差。本文探讨了减少这一差距的方法，提出了一种能够在预测下一个标记时考虑整个过去的Gated KalmaNet（GKA）层。这种方法旨在保持SSMs的效率，同时提升召回任务中的性能。
### Innovation
该研究提出了两种关键创新：1）适应性正则化策略，该策略具有输入依赖的门控机制，能够控制岭回归的条件数，从而确保数值稳定性并平衡内存保留；2）使用切比雪夫迭代替代其他传统的迭代求解器，该方法在低精度设置中显示出更高的稳定性。此外，开发了切比雪夫迭代的硬件感知分块实现，以及针对适配性正则化和门控机制的自定义反向传播内核。
### Conclusion
该研究展示了GKA在短期上下文任务中语言理解能力出色，超越了现有SSM层（如Mamba2、GLA和Gated DeltaNet）。在长上下文任务中，GKA在实际的RAG和长问答任务中表现出色，处理多达128k标记的文本时，超越其他带有淡出记忆基线超过10%的相对改进。
## 663. `cs.LG` - 基于SDR的CNN-LSTM混合架构用于空中自动调制分类 [PDF](https://arxiv.org/pdf/2511.21040), [HTML](https://arxiv.org/abs/2511.21040)
### Authors
Dinanath Padhya,Krishna Acharya,Bipul Kumar Dahal,Dinesh Baniya Kshatri
### Background
自动调制分类（AMC）是未来无线通信系统的核心技术，能够在无需先验知识的情况下识别调制方案。该能力对于认知无线电、频谱监控和智能通信网络等应用至关重要。现有的AMC系统大多采用单一深度学习模型，通常难以同时应对空间和时间维度上的复杂调制信号特征。
### Innovation
本文提出了一种基于混合卷积神经网络（CNN）和长短期记忆网络（LSTM）架构的AMC系统，结合了软件定义无线电（SDR）平台。该架构利用CNN进行空间特征提取，利用LSTM捕捉时间依赖性，从而高效管理和处理复杂的、时变的通信信号。实验结果显示，该系统在0至30dB信噪比（SNR）的条件下，实现了93.48%的准确率，93.53%的精确率，93.48%的召回率和93.45%的F1分数，并且在噪声条件下依然表现出优越的区分能力。
### Conclusion
本文通过实验证明了CNN-LSTM混合架构在AMC中的有效性，这表明该方法在自适应频谱管理和高级认知无线电系统中有潜在的应用价值。
## 664. `cs.LG` - G-Net: 一种高准确度证明简单构建的随机二进制神经网络 [PDF](https://arxiv.org/pdf/2511.21063), [HTML](https://arxiv.org/abs/2511.21063)
### Authors
Alireza Aghasi,Nicholas Marshall,Saeid Pourmand,Wyatt Whiting
### Background
该研究基于高维计算（HDC）的脑启发计算框架，该框架利用高维向量表示，提供高效硬件实现和对模型损坏的鲁棒性。传统低精度方法通常采用量化技术，而该研究考虑将数据作为具有汉明距离的超立方体中的点的二进制嵌入。
### Innovation
研究提出了一种新颖的浮点表示的神经网络家庭，称为G-Net。G-Net能够模拟标准网络层，并具备理论保证的随机二进制嵌入。实验结果表明，G-Net在CIFAR-10上的准确率比之前的HDC模型高出近30%，开创新的方向用于构建鲁棒的二进制/量化深度学习模型。
### Conclusion
G-Net是介于传统神经网络和随机二进制神经网络之间一个理论可行的桥梁，展示了如何构建高效且准确的二进制模型。研究的代码已公开提供。
## 665. `cs.LG` - FedAPA: 联邦学习中自适应原型聚合以实现异构Wi-Fi CSI人群计数 [PDF](https://arxiv.org/pdf/2511.21048), [HTML](https://arxiv.org/abs/2511.21048)
### Authors
Jingtao Guo,Yuyi Mao,Ivan Wang-Hei Ho
### Background
Wi-Fi信道状态信息(CSI)感知提供了无侵入和无设备的人类活动识别和人群计数等任务的一种方法，但由于需要大量特定站点的训练数据，大规模部署受到限制。联邦学习(FL)提供了一种避免原始数据共享的方式，但面对异构的感知数据和设备资源，仍存在挑战。
### Innovation
提出了一种名为FedAPA的协作Wi-Fi CSI基于感知算法，该算法使用自适应原型聚合(Adaptive Prototype Aggregation, APA)策略为对等原型分配基于相似性的权重，使客户端能够自适应地贡献，并生成每个客户端的个性化全局原型，而不是固定的加权聚合。此外，在局部训练阶段采用结合分类学习和表示对比学习的混合目标来进行局部和全局知识对齐。
### Conclusion
通过在六个环境中、最多20人的真实分布式Wi-Fi人群计数场景下评估FedAPA算法，结果表明，与多个基准方法相比，该方法在准确性、F1分数、平均绝对误差（MAE）以及通信开销方面均有显著提升。具体表现为：准确率至少提高了9.65%，F1分数提高了9%，MAE降低了0.29，通信开销减少了95.94%。
## 666. `cs.LG` - MLPMoE：密集LLM MLP的零-shot 架构变形为静态MoE [PDF](https://arxiv.org/pdf/2511.21089), [HTML](https://arxiv.org/abs/2511.21089)
### Authors
Ivan Novikov
### Background
现有的大型语言模型（LLMs）通常采用密集的变压器架构，每个前向块中的每个参数对每个标记都进行激活，虽然这种架构简单，但在推理时计算效率低下，因为推理成本与参数数量成线性关系。近期，诸如MoEfication、CMoE、ToMoE和MoORE等“再利用”方法揭示了在密集前向网络内部存在的部分有用计算在稀疏、半模块化的子结构中进行，但这些方法通常依赖聚类、激活表征分析、奇异值分解或自定义路由，这些方法需要校准数据。
### Innovation
本文介绍了MLPMoE（多层感知机混合专家模型），这是一种无需训练、确定性的转换，它将变压器块中的密集多层感知机重新结构化为静态的、高基数混合专家。该转换利用简单的张量切片和求和，重新诠释张量并行的代数为拓扑转换，而不是分布式训练模式。此外，还引入了分形淡出（分段分支稀疏性）和补偿修剪（方差保持分支缩减）作为轻量级的结构稀疏机制。在Qwen2.5-0.5B-Instruct和DeepSeek-R1-Distill-Llama-8B上，零极MLPMoE转换对代理困惑度度量的影响小于0.05%，并且保持参数计数基本不变。在8B模型上，分段稀疏性移除了大约20%的MLP参数，同时困惑度保持在密集基线的约2%以内。这些方法完全是在现有检查点的后处理操作上进行，不需要梯度、校准集或路由器训练。
### Conclusion
MLPMoE方法在保持模型性能的同时显著减少了模型参数量，并且操作完全在现有检查点的后处理中进行，无需额外的数据或训练。这种方法为LLMs的计算效率提升提供了一种新的途径。
## 667. `cs.LG` - 可解释公平聚类 [PDF](https://arxiv.org/pdf/2511.21109), [HTML](https://arxiv.org/abs/2511.21109)
### Authors
Mudi Jiang,Jiahui Zhou,Xinying Liu,Zengyou He,Zhikui Chen
### Background
近年来，公平聚类引起了越来越多的关注，尤其是在涉及社会敏感属性的应用场景中。然而，现有的公平聚类方法往往缺乏可解释性，这限制了它们在高风险场景中的应用，在这些场景中理解聚类决策背后的理由是必不可少的。
### Innovation
本文通过提出一个可解释和公平的聚类框架解决了该限制，该框架将公平约束整合到决策树的结构中。该方法构建可解释的决策树来划分数据，同时确保不同受保护群体之间的公平待遇。为了进一步提高框架的实用性，还引入了一种不需要调参的变体版本，通过事后修剪构建无公平约束的树来实现。
### Conclusion
我们在实际数据集和合成数据集上的广泛实验表明，我们的方法不仅提供竞争力的聚类性能和改进的公平性，而且还提供额外的优势，如可解释性和处理多个敏感属性的能力。这些优点使我们的方法能够在多种公平约束下表现稳健，为公平和透明的聚类打开了新的可能性。
## 668. `cs.LG` - MNM: 多层级神经影像荟萃分析与双曲脑-文本表示 [PDF](https://arxiv.org/pdf/2511.21092), [HTML](https://arxiv.org/abs/2511.21092)
### Authors
Seunghun Baek,Jaejin Lee,Jaeyoon Sim,Minjae Jeong,Won Hwa Kim
### Background
各种神经影像学研究面临着小样本问题，这往往限制了研究的可靠性。荟萃分析通过聚合不同研究的发现来识别一致的脑活动模式，从而解决了这个问题。然而，传统的方法，如关键词检索或线性映射，经常忽略了神经影像数据中的丰富层次结构。
### Innovation
本文提出了一种新的框架，利用双曲几何学来弥合神经科学文献和脑激活图之间的差距。通过使用洛伦兹模型将研究文章的文本和相应的脑图象嵌入到共享的双曲空间中，该方法捕捉到了神经影像数据中的语义相似性和层次组织。在双曲空间中，该方法通过以下步骤进行多层次神经影像荟萃分析：1）对齐脑和文本嵌入以实现语义对应；2）引导文本和脑激活之间的层次结构；3）保留脑激活模式内的层次关系。
### Conclusion
实验结果表明，我们的模型在多层次神经影像荟萃分析方面优于基线模型，通过双曲脑-文本表示提供了一个稳健且可解释的多层级神经影像荟萃分析范式。
## 669. `cs.LG` - 生成式早期阶段排名 [PDF](https://arxiv.org/pdf/2511.21095), [HTML](https://arxiv.org/abs/2511.21095)
### Authors
Juhee Hong,Meng Liu,Shengzhi Wang,Xiaoheng Mao,Huihui Cheng,Leon Gao,Christopher Leung,Jin Zhou,Chandra Mouli Sekar,Zhao Zhu,Ruochen Liu,Tuan Trieu,Dawei Sun,Jeet Kanjani,Rui Li,Jing Qian,Xuan Cao,Minjie Fan,Mingze Gao
### Background
大规模推荐系统通常采用多阶段级联排名系统架构，以平衡效果与效率。早期阶段排名（ESR）系统通过“用户-物品去耦”方式工作，即独立学习用户和物品表示，仅在最终层合并。这种设计有效，但在精确性方面存在局限，难以捕捉细微的用户-物品相关性和交叉信号。
### Innovation
本文提出了生成式早期阶段排名（GESR）范式，引入了混合注意力（MoA）模块，利用多种注意力机制弥合了精确性差距。具体包括硬匹配注意力（HMA）模块，编码用户和物品特征之间的明确交叉信号；目标感知自我注意力模块，生成基于物品的目标感知用户表示，实现更加个性化的学习；以及跨注意力模块，促进用户-物品特征早期和更丰富的交互。最后通过多逻辑门参数化门控（MLPG）模块进一步细化MoA的专门注意力编码，在最终层通过门控整合新学习嵌入并产生次级逻辑，融合主要逻辑。
### Conclusion
提出的GESR范式在离线和在线实验中均表现出对前端徽标、参与度和消费任务的显著改进。据我们所知，这是首次成功在ESR阶段部署全面的目标感知注意力序列建模，在如此大规模的部署中。
## 670. `cs.LG` - 动态分层对比学习与上游增强在MILP分支中的应用 [PDF](https://arxiv.org/pdf/2511.21107), [HTML](https://arxiv.org/abs/2511.21107)
### Authors
Tongkai Lu,Shuai Ma,Chongyang Tao
### Background
MILP是NP难问题中的一个基本类别，受到了学术界和工业界的广泛关注。B&B方法是解决MILP的主要方法，分支策略在B&B方法中起着重要作用。近年来，基于神经网络的学习框架被开发出来以增强分支策略和MILP求解效率。但这些方法仍然面临深度上的语义变异、上游节点稀缺以及强分支样本昂贵收集等问题。
### Innovation
提出了一种基于GCNN的动态分层对比训练框架(Dynamic Stratified Contrastive Training Framework for MILP Branching, textbackslashtext{ours})，它基于节点特征分布对节点进行分组，并训练一组辨别性模型，逐渐分离节点群组，学习节点的更加精细的表示。我们还提出了一个上游增强的MILP推导过程，生成理论上等价和扰动实例，以应对数据的稀缺性和不平衡性。实验表明，textbackslashtext{ours}能够有效建模节点之间的微妙语义差异，显著提升分支准确性和求解效率，特别是在处理上游节点时。
### Conclusion
在标准MILP基准上的实验结果进一步证明，我们的方法提升了分支准确性和减少了解决时间，并且能够有效泛化到未见样本。
## 671. `cs.LG` - 使用平衡微调方法将大语言模型与生物医药知识对齐 [PDF](https://arxiv.org/pdf/2511.21075), [HTML](https://arxiv.org/abs/2511.21075)
### Authors
Zhenchao Tang,Fang Wang,Haohuai He,Jiale Zhou,Tianxu Lv,Jun Zhu,Shouzhi Chen,Minghao Yang,Yu Wang,Jiayang Wu,Yidong Song,Jianhua Yao
### Background
有效的后训练对于将大型语言模型（LLMs）与专门的生物医药知识对齐至关重要，以加速生命科学研究。然而，当前的方法存在显著限制。首先，生物医药推理涉及复杂的机制，经常通过稀疏文本数据表示。标准监督微调（SFT）倾向于过度拟合表面指令模式，而未能有效内化这些分散的科学知识。其次，强化学习（RL）对于这一领域来说不切实际，因为定义有意义的奖励通常需要大量的实验验证（例如，湿实验验证药物反应），这使实时反馈变得不切实际。
### Innovation
提出了一种高效的后训练方法——平衡微调（BFT）。BFT 通过两层加权机制工作：1. 在标记级别，通过调整预测概率来缩放损失，以稳定梯度并防止过度拟合；2. 在样本级别，使用“最小组置信度”来适应性地增强对难样本的学习。实验显示 BFT 显著优于 SFT，特别是在医学任务中，它使大语言模型能够获取 SFT 未能掌握的知识，在生物任务中，基于 BFT 的大语言模型超越了基因代理（一种准确的生物分析代理）在生物学过程推理方面。
### Conclusion
BFT 为生物医药研究中的大语言模型应用提供了更广泛的可能性。
## 672. `cs.LG` - 学习细胞感知层次多模态表示以实现稳健的分子建模 [PDF](https://arxiv.org/pdf/2511.21120), [HTML](https://arxiv.org/abs/2511.21120)
### Authors
Mengran Li,Zelin Zang,Wenbin Xing,Junzhou Chen,Ronghui Zhang,Jiebo Luo,Stan Z. Li
### Background
理解化学干扰如何在生物系统中传播对于预测分子性质至关重要。现有的大多数方法主要关注化学结构，而最近的研究则强调细胞响应如形态和基因表达在药物效果中的关键作用。然而，当前的细胞感知方法面临两个关键局限：（1）外部生物数据的模态不完整性，（2）分子、细胞和基因组层次间依赖关系建模不足。
### Innovation
我们提出了CHMR（细胞感知层次多模态表示），这是一个鲁棒的框架，可以同时建模分子和细胞响应之间的局部和全局依赖关系，并通过一种新颖的树结构向量量化模块捕捉潜在的生物层次结构。在七个公共基准数据集上的9个任务中，CHMR在分类和回归任务的平均性能上分别提高了3.6%和17.2%，这证明了层次感知的多模态学习在可靠且具有生物基础的分子表示方面的优势，为综合生物医学建模提供了可扩展的框架。
### Conclusion
这些结果表明了层次感知、多模态学习的优势，对于实现准确且生物学根基深厚的分子表示具有重要价值。这一框架为整合生物医学建模提供了通用性框架。
## 673. `cs.LG` - 从比特到轮次：探索促进扩散语言模型并行解码 [PDF](https://arxiv.org/pdf/2511.21103), [HTML](https://arxiv.org/abs/2511.21103)
### Authors
Hengyu Fu,Baihe Huang,Virginia Adams,Charles Wang,Venkat Srinivasan,Jiantao Jiao
### Background
扩散语言模型（DLMs）作为一种强大的替代方案，近年来与自回归语言模型（LMs）进行了竞争。DLMs通过并行解码实现了可比的准确度和更快的推理速度。然而，依赖于高置信度标记的标准DLM解码策略遇到了固有的信息论瓶颈，这限制了解码进度，最终减慢了生成过程。
### Innovation
本文证明并证实了优先考虑高置信度标记本质上是不高效的。文章提出了探索—然后利用（ETE）解码策略，这是一种无需训练的方法，旨在最大化信息通量和解码效率。ETE结合了跨块解码和对高不确定性标记的目标化探索，以重塑条件分布并触发一系列可信预测。
### Conclusion
实验验证了研究的理论界限，并表明与仅依赖信心的基线相比，ETE方法能够显著减少所需的解码轮次，同时不降低生成质量。研究建立了比特到轮次的原则，证明了解码轮次的增长与样本的总信息量成正比，与每轮的信息预算成反比。
## 674. `cs.LG` - Deceptron：学习局部逆操作以实现快速且稳定的物理反演 [PDF](https://arxiv.org/pdf/2511.21076), [HTML](https://arxiv.org/abs/2511.21076)
### Authors
Aaditya L. Kachhadiya
### Background
物理科学中的反问题通常在输入空间中是病态的，这使得进展步长敏感。现有方法在这类问题中往往需要非常精细的步长调整，以确保算法的稳定性和收敛性。
### Innovation
本文提出了一种称为Deceptron的轻量级双向模块，它通过一个可微的前向辅助模型学习其局部逆。训练过程中结合了监督拟合、正向-反向一致性、轻量级的频谱惩罚、软偏置关联以及通过JVP/VJP探针鼓励$J_g(f(x))J_f(x)thickapprox I$的雅可比组合惩罚。在求解时，D-IPG（Deceptron反向预条件梯度）在输出空间进行下降步骤，通过$g$反向传递，并在相同的回溯和停止规则下进行投影。在Heat-1D初始条件恢复和阻尼振子反问题中，D-IPG所需的迭代次数显著减少，与投影梯度相比减少约20倍的迭代次数，并且在迭代次数和成本上与高斯-牛顿法相当。诊断结果显示，雅可比组合惩罚减少了测量的组合误差并跟踪了迭代增益。DeceptronNet（v0）还展示了在单一尺度2D实例中，快速收敛的能力。
### Conclusion
该研究表明，Deceptron通过学习局部逆能够有效减少反问题求解的迭代次数，提高计算效率和稳定性，特别是在物理反问题解决中。
## 675. `cs.LG` - 一种用于结构地震响应建模的物理启发式UNet-LSTM网络 [PDF](https://arxiv.org/pdf/2511.21276), [HTML](https://arxiv.org/abs/2511.21276)
### Authors
Sutirtha Biswas,Kshitij Kumar Yadav
### Background
准确而高效的地震响应预测对结构抗震设计至关重要。尽管有限元方法仍是非线性地震分析的标准方法，但其高计算需求限制了其扩展性和实时应用。近年来，深度学习的进展，特别是卷积神经网络(CNNs)、循环神经网络(RNNs)和长短期记忆(LSTM)模型，显示出了降低结构非线性地震分析计算成本的潜力。然而，这些数据驱动模型常常难以泛化和捕捉物理原理，导致可靠性降低。
### Innovation
我们提出了一种新型的物理启发式U Net LSTM框架，该框架将物理定律与深度学习相结合，以增强准确性和效率。通过将特定领域约束嵌入学习过程，该模型实现了比传统机器学习架构更好的预测性能。这种混合方法在纯数据驱动方法和基于物理的建模之间架起了一座桥梁，为结构地震响应预测提供了稳健而计算高效的替代方案。
### Conclusion
该模型通过结合物理定律与深度学习，提高了地震响应预测的准确性和效率，并为结构抗震设计提供了一种新的计算高效且可靠的解决方案。
## 676. `cs.LG` - 与脉冲神经网络相关的联邦学习中的隐私问题 [PDF](https://arxiv.org/pdf/2511.21181), [HTML](https://arxiv.org/abs/2511.21181)
### Authors
Dogukan Aksu,Jesus Martinez del Rincon,Ihsen Alouani
### Background
脉冲神经网络(SNNs)是嵌入式和边缘AI的首选方案，因为它们的低功耗特性使得它们在能源限制严格的情况下比传统的人工神经网络(ANNs)更高效。同时，联邦学习(FL)在这些场景中已成为主导的训练范式，允许在设备端学习同时限制原始数据的暴露。然而，梯度反转攻击是FL中关键的隐私威胁，因为可以从中直接重建敏感训练数据。既往研究大量集中在传统ANNs上，但尚未充分探讨SNNs中的这些影响。
### Innovation
本研究首次进行了SNNs在不同数据领域下的梯度泄露全面实证研究。通过使用代理梯度进行训练，一个假设是其与原始输入的相关性较低，从而对隐私的影响较小。通过将不同的梯度泄露攻击适应脉冲域，实验结果表明，而传统ANNs的梯度可靠地揭示输入内容，SNNs的梯度产生的是嘈杂且时间上不一致的重建结果，无法恢复有意义的空间或时间结构。这意味着事件驱动动力学和代理梯度训练显著降低了梯度的信息性。这些结果表明，神经形态计算具有固有的隐私保护潜力。
### Conclusion
本研究提供了第一个针对脉冲架构的梯度反转攻击系统基准测试，强调了神经形态计算固有的隐私保护潜力。
## 677. `cs.LG` - BRIDGE: 在域引导程序验证中构建领域表示 [PDF](https://arxiv.org/pdf/2511.21104), [HTML](https://arxiv.org/abs/2511.21104)
### Authors
Robert Joseph George,Carson Eisenach,Udaya Ghai,Dominique Perrault-Joncas,Anima Anandkumar,Dean Foster
### Background
大型语言模型在代码生成方面取得了显著成果，但在程序验证方面面临挑战，特别是在如Lean4这样的交互式证明框架中表现不佳。核心挑战在于可扩展性：验证综合不仅需要代码，还需要精确的规范和正确的证明，而现有方法通常未能涵盖这三个领域。
### Innovation
BRIDGE首次系统地研究了可扩展验证程序生成的结构化提示方法。BRIDGE将验证分解为三个相互关联的领域：代码（可执行实现）、规范（形式的意图声明）以及证明（构造的正确性论证）。其关键在于通过功能、规范驱动和证明导向的不同推理行为作为中间表示，保持语义结构并连接这些领域。
### Conclusion
BRIDGE的研究显示，这种结构化的方法在准确性和效率方面显著优于传统的错误反馈方法。这种方法证明了结构化领域对齐是促进验证综合的一个有前景的方向。BRIDGE建立了通过专家迭代或RLVR进行训练的基础，使模型能够跨越代码、规范和证明内化这些推理策略。
## 678. `cs.LG` - 时间序列去噪扩散隐模型中的齿形采样 [PDF](https://arxiv.org/pdf/2511.21320), [HTML](https://arxiv.org/abs/2511.21320)
### Authors
Heiko Oppel,Andreas Spilz,Michael Munz
### Background
Denoising Diffusion Probabilistic Models (DDPMs)能够生成合成时间序列数据以提升分类器的性能，但其采样过程计算成本高。
### Innovation
作者通过结合隐式扩散模型和一种新颖的齿形采样方法，加速了反向过程，并且该方法可以应用于任何预训练的扩散模型，从而实现了比标准基线快30倍的加速，并提高生成序列的质量。
### Conclusion
该方法在保持分类任务生成序列质量的同时，显著降低了计算成本。
## 679. `cs.LG` - 掩码可能会分散注意力：关于扩散语言模型中的上下文理解 [PDF](https://arxiv.org/pdf/2511.21338), [HTML](https://arxiv.org/abs/2511.21338)
### Authors
Julianna Piskorz,Cristina Pinneri,Alvaro Correia,Motasem Alfarra,Risheek Garrepalli,Christos Louizos
### Background
掩码扩散语言模型（MDLMs）作为一种替代自回归语言模型（ARLMs）的新颖方法，已经崭露头角，利用去噪目标来更好地均匀利用上下文信息。然而，尽管MDLMs具有更全局的训练目标和双向注意力机制，它们仍然显示出强烈的局部偏向，即输入中相关信息的位置对性能有高度影响，并且更倾向于局部而非远距离的上下文。此外，附加大量掩码标记（用于生成）会导致显著削弱上下文理解。通过系统性消除实验，研究表明这些掩码会作为干扰项，影响模型处理相关信息的能力。研究旨在解决这个挑战。
### Innovation
引入了不依赖掩码的损失函数，旨在鼓励预测保持对附加到模型上的掩码数量的不变性。使用此目标进行微调大大缓解了掩码的干扰效果，增强了MDLMs的鲁棒性。
### Conclusion
我们的研究揭示了当前MDLM训练范式的关键限制，并提供了有关如何构建具有更强上下文理解的扩散语言模型的实际建议。
## 680. `cs.LG` - 信任无界的边缘规模联邦学习: 组合架构实现去中心化、可验证以及激励对齐的协调 [PDF](https://arxiv.org/pdf/2511.21118), [HTML](https://arxiv.org/abs/2511.21118)
### Authors
Pius Onobhayedo,Paul Osemudiame Oamen
### Background
随着人工智能的转型，从集中式提供到分布式创造，计算资源最初集中在能够培训和服务大量数据的机构中。随着联邦学习的发展，数以亿计的边缘设备将能够共同提高模型，无需泄露原始数据，从而实现大规模的贡献和消费。然而，由于某些组合缺口，这一民主愿景尚未实现。这些缺口包括聚合处理缺乏透明性、缺乏有效的经济机制、协调机制限制了状态修改的并发性和治理允许追溯性操纵。
### Innovation
本文通过利用加密收据证明聚合的正确性，引入几何新颖度计量以防止激励博弈，采用并行对象所有权实现线性可扩展性，以及采用时间锁定政策检查追溯性操纵，来解决上述缺口，从而实现去中心化、可验证和激励对齐的协调。
### Conclusion
通过以上创新方法，本文提出了一种组合架构，用于实现边缘规模下无信任的联邦学习，解决了当前联邦学习中的多个关键问题，推动了人工智能向真正去中心化和透明的合作模式转变。
## 681. `cs.LG` - 基于Fast-mRMR特征选择的高维组学数据稳健基因优先级确定 [PDF](https://arxiv.org/pdf/2511.21211), [HTML](https://arxiv.org/abs/2511.21211)
### Authors
Rubén Fernández-Farelo,Jorge Paz-Ruza,Bertha Guijarro-Berdiñas,Amparo Alonso-Betanzos,Alex A. Freitas
### Background
基因优先级确定（即识别与生物过程潜在关联的基因）越来越多地使用人工智能来解决。然而，现有的方法难以处理生物医学数据中的高维度和不完整标签问题。
### Innovation
本文提出了一种更坚固且高效的流水线，利用Fast-mRMR特征选择保留仅相关且非冗余的特征，为分类器提供支持。这使得能够构建更简单而有效的模型，并结合不同的生物特征集合。在饮食限制数据集上的实验显示，与现有方法相比有显著改进，证明特征选择对于可靠的基因优先级确定至关重要。
### Conclusion
基于Fast-mRMR特征选择，通过简化模型并组合不同的生物特征集实现了对未来基因优先级确定的显著改进，验证了特征选择的重要性。
## 682. `cs.LG` - 如何正确报告LLM作为评判者的评估 [PDF](https://arxiv.org/pdf/2511.21140), [HTML](https://arxiv.org/abs/2511.21140)
### Authors
Chungpa Lee,Thomas Zeng,Jongwon Jeong,Jy-yong Sohn,Kangwook Lee
### Background
大型语言模型（LLMs）越来越多地被用作替代人类的评判者。虽然它们在可扩展性方面有优势，但它们的判断因模型的不精确特异性和敏感性而导致结果噪声较大，这会使得准确性和偏差估计受到影响。虽然已经存在一些纠偏方法，但在LLM研究中这些方法的使用并不充分，通常这些方法还假设可以精确知道模型的特异性和敏感性。实际情况中，我们往往只能得到这些值的估计值，而且如何仅使用估计值正确构建置信区间还不明确。
### Innovation
本文提出了一种简单的插件框架来纠正此类偏差并构建反映来自测试和校准数据集的不确定性置信区间，从而实现基于LLM的实际且统计上可靠的评估。此外，为了减少准确度估计的不确定性，还引入了一种适应性算法来有效分配校准样本大小。
### Conclusion
这项工作提供了一种实用且统计上可靠的LLM基础评估框架，能够正确报告基于LLM的评估结果，并通过适应性算法降低了评估不确定性的大小。
## 683. `cs.LG` - I-GLIDE: 输入组在退化估计中的潜在健康指标 [PDF](https://arxiv.org/pdf/2511.21208), [HTML](https://arxiv.org/abs/2511.21208)
### Authors
Lucas Thil,Jesse Read,Rim Kaddah,Guillaume Doquet
### Background
准确的剩余使用寿命（RUL）预测依赖于健康指标（HIs）的质量，但现有方法往往无法在多传感器系统中解开复杂的退化机制，也无法量化HI可靠性的不确定性。
### Innovation
本研究推出了一种新的HI构建框架，包含三项关键贡献：第一，首次采用Reconstruction along Projected Pathways (RaPP) 作为RUL预测的HI，并证明其优于传统的重建误差度量；第二，通过蒙特卡洛丢弃和概率潜空间增强RaPP衍生的HI，结合 aleatoric 和 epistemic 不确定性量化（UQ），显著提高RUL预测的鲁棒性；第三，提出了指标组的概念，将传感器子集隔离建模系统特定的退化，提出了新型方法I-GLIDE，实现了可解释的、机制特定的诊断。
### Conclusion
在航空航天和制造系统数据上评估，本方法相比最先进的HI方法在准确性和泛化性方面取得了显著进步，提供了关于系统故障路径的可操作见解。这项工作弥补了异常检测和预测之间的差距，为复杂系统中的不确定性意识退化建模提供了原理框架。
## 684. `cs.LG` - TSGM: 使用评分生成模型进行规则和不规则时间序列生成 [PDF](https://arxiv.org/pdf/2511.21335), [HTML](https://arxiv.org/abs/2511.21335)
### Authors
Haksoo Lim,Jaehoon Lee,Sewon Park,Minjung Kim,Noseong Park
### Background
自评分生成模型（SGMs）应用于图像生成、语音合成和表格数据合成等多种领域后，展示了无与伦比的采样质量和多样性。基于这些杰出的结果，本文探索将SGMs应用于时间序列的生成中。
### Innovation
提出了一个条件评分网络来生成时间序列，并为该目的设计了一个定制的去噪评分匹配损失。此外，该框架具有高度的灵活性，既可以生成规则时间序列，也可以生成不规则时间序列，而对模型设计的变动很小。实验结果表明，该方法在多种时间序列数据集上达到了前所未有的采样多样性和质量。
### Conclusion
通过使用TSGM框架进行时间序列生成实验，实现了在不同时间序列数据集上具备卓越的合成性能，达到了SOTA的采样多样性和质量。
## 685. `cs.LG` - 控制注意力标记的变化 [PDF](https://arxiv.org/pdf/2511.21377), [HTML](https://arxiv.org/abs/2511.21377)
### Authors
Ben Anson,Laurence Aitchison
### Background
在训练变压器模型时，神经网络权重的稳定性至关重要。特别地，查询和键权重的问题很大，因为它们倾向于在训练过程中变得非常大，除非进行干涉。已有的方法，如 `QK norm'，虽然可以在实践中解决稳定性问题，但并不总是适用。例如，`QK norm' 不适用于多潜在注意力（MLA）模型，因为 `QK norm' 在推理过程中需要完全实现查询和键，而这在 MLA 中并不会发生。
### Innovation
本文提出通过给查询和键权重分配依赖于参数的学习率来控制标记的变化。这种方法成本低廉，允许增加网络的基学习率，并在 MLA 环境下优于其他方法。使用多头注意力时，这种方法的性能与 `QK norm' 相当。
### Conclusion
通过控制注意力标记的变化，可以提高稳定性和学习效率。在 MLA 设置下，该方法实现了良好的性能，接近甚至超过 `QK norm' 的效果。
## 686. `cs.LG` - BanglaMM-Disaster: 一种基于多模态变换器的深度学习框架，用于孟加拉语多类别灾害分类 [PDF](https://arxiv.org/pdf/2511.21364), [HTML](https://arxiv.org/abs/2511.21364)
### Authors
Ariful Islam,Md Rifat Hossen,Md. Mahmudul Arif,Abdullah Al Noman,Md Arifur Rahman
### Background
孟加拉国仍然是自然灾害的重大挑战地区，因此实时监控和快速响应系统至关重要。鉴于此背景，本研究提出了一种名为BanglaMM-Disaster的端到端多模态深度学习框架，用于使用社交平台上的文本和视觉数据进行孟加拉语多类别的灾害分类。
### Innovation
该模型结合了基于变换器的文本编码器（包括BanglaBERT、mBERT和XLM-RoBERTa）和CNN骨干网络（如ResNet50、DenseNet169和MobileNetV2），以处理两种模态的数据。通过早期融合，最佳模型的准确率为83.76%，超过了仅使用文本或仅使用图像基准的最佳表现。
### Conclusion
该工作弥补了孟加拉语多模态灾害分析的关键空白，并展示了在低资源环境下的实时灾害响应中结合多种数据类型的好处。各分类的错误分类率降低，特别是在模糊示例方面有明显的改进。
## 687. `cs.LG` - 受污染训练数据下具有自适应和激进排斥的异常检测 [PDF](https://arxiv.org/pdf/2511.21378), [HTML](https://arxiv.org/abs/2511.21378)
### Authors
Jungi Lee,Jungkwon Kim,Chi Zhang,Kwangsun Yoo,Seok-Joo Byun
### Background
在异常检测中处理污染数据是一个关键挑战，传统模型假设训练数据完全正常。传统的缓解方法依赖固定的污染比率，但在假设与实际比率不一致的情况下，性能会严重下降，尤其是在正常和异常数据分布重叠的嘈杂环境中。
### Innovation
提出了自适应和激进排斥（AAR）方法，这是一种新的方法，通过使用修改后的z分数和基于高斯混合模型的阈值动态排除异常。AAR通过结合硬排斥和软排斥策略有效地平衡保留正常数据和排除异常之间的权衡。
### Conclusion
通过在两个图像数据集和三十个表格数据集上进行的广泛的实验，证明AAR方法在0.041 AUROC上超过了现有的最佳方法，增强了对受污染数据集的稳健性，并为安全和医疗等领域的广泛实际应用铺平了道路。
## 688. `cs.LG` - 定向预测变化 - 本地特征归因方法的高效且可信赖的保真度评估 [PDF](https://arxiv.org/pdf/2511.21363), [HTML](https://arxiv.org/abs/2511.21363)
### Authors
Kevin Iselborn,David Dembinsky,Adriano Lucieri,Andreas Dengel
### Background
现有的保真度评估指标，如Infidelity，依赖于蒙特卡洛近似，这需要大量模型评估并引入随机采样的不确定因素。背景指出，解释方法的效果取决于其对底层机器学习模型的忠实度，特别是在高风险医疗环境中，临床医生和监管机构需要可靠的解释。这些解释应能准确反映模型的决策过程。
### Innovation
提出了一种新的保真度评估指标，即定向预测变化(Directed Prediction Change, DPC)。该指标通过对现有的预测变化(Prediction Change, PC)方法进行修改，在引导扰动实验中引入了扰动和归因的方向性。DPC方法几乎比PC快10倍，并消除了随机性，提供了一个确定且可信赖的评估流程，测量的特性与局部Infidelity相同。DPC在皮肤病变图像和金融表格数据集上进行了验证，涉及两种黑箱模型和七种解释算法，涵盖广泛的超参数。
### Conclusion
跨4744种不同解释的结果表明，DPC与PC一起可以提供一个全面且计算效率高的评估方案，用于评价基准导向和本地特征归因方法，同时确保结果的确定性和可重复性。
## 689. `cs.LG` - 在科学应用中进行机器学习实验的最佳实践 [PDF](https://arxiv.org/pdf/2511.21354), [HTML](https://arxiv.org/abs/2511.21354)
### Authors
Umberto Michelucci,Francesca Venturini
### Background
机器学习（ML）在科学研究中的应用越来越广泛，但实验的质量和可靠性往往取决于实验的设计和记录。较差的基线、不一致的预处理或不充分的验证可能导致对模型性能的误导性结论。本研究提供了一项实用而结构化的指导方针，旨在进行科学应用中的ML实验，重点关注可重复性、公平比较和透明报告。
### Innovation
本文提出了从数据集准备到模型选择和评估的逐步工作流程，并建议了考虑验证折间过拟合和不稳定性的度量方法，包括Logarithmic Overfitting Ratio (LOR)和Composite Overfitting Score (COS)。此外，本文通过推荐的实践和示例报告格式，旨在支持研究人员建立稳健的基线，并从应用于科学问题的ML模型中得出有效的证据分析结果。
### Conclusion
通过推荐的实践和示例报告格式，本文旨在支持研究人员建立稳健的基线，并从应用于科学问题的ML模型中得出有效的证据分析结果。
## 690. `cs.LG` - Hybrid-AIRL：通过监督专家指导提升逆强化学习 [PDF](https://arxiv.org/pdf/2511.21356), [HTML](https://arxiv.org/abs/2511.21356)
### Authors
Bram Silue,Santiago Amaya-Corredor,Patrick Mannion,Lander Willem,Pieter Libin
### Background
Adversarial Inverse Reinforcement Learning (AIRL) 已经在强化学习 (RL) 中展示了应对稀疏奖励问题的潜力，通过从专家示例中推断密集奖励函数。然而，在高度复杂且信息不全的场景中，它的表现还很少被研究。在 Heads-Up Limit Hold'em (HULHE) 限注德州扑克游戏中，稀疏、延迟的奖励和极大的不确定性使得 AIRL 在推断出足够有信息量的奖励函数方面面临挑战。
### Innovation
贡献了 Hybrid-AIRL (H-AIRL)，一种通过引入来自专家数据的监督损失和随机正则化机制来增强奖励函数推断和策略学习的扩展方法。
### Conclusion
H-AIRL 在 Gymnasium 基准和 HULHE 棋牌设置下的实验结果显示了比 AIRL 更高的样本效率和更稳定的训练性能。这强调了将监督信号纳入逆强化学习的好处，并表明H-AIRL 是解决具有挑战性的现实场景的潜在框架。
## 691. `cs.LG` - 主观深度和时间尺度变换器：学习何时何地进行计算 [PDF](https://arxiv.org/pdf/2511.21408), [HTML](https://arxiv.org/abs/2511.21408)
### Authors
Frederico Wieser,Martin Benfeghoul,Haitham Bou Ammar,Jun Wang,Zafeirios Fountas
### Background
标准Transformer架构中的计算分配通常是刚性和统一的，这在大规模模型和长序列处理中会限制效率和可扩展性。
### Innovation
本文引入了Subjective Depth Transformers (SDT) 和 Subjective Timescale Transformers (STT) 两种不同的架构，这些架构利用贝叶斯惊讶信号动态路由计算，学习在解码器为主的Transformer中何时何地进行计算。SDT 和 STT 通过动态调整计算路径来降低自注意力计算和KV缓存需求，为更高效的模型提供了途径。
### Conclusion
这两种架构展示了从新颖性到预测驱动编程转移的趋势，表明与基于惊讶的原理相吻合。通过减少计算能力，它们初步揭示了条件计算下的计算-准确度折衷关系。提出的架构为效率提供了一个灵活的框架，在每个计算跳跃层内将自注意力计算降低75%，并将KV缓存需求降低50%，为更高效的模型铺平了道路。
## 692. `cs.LG` - SUPN: Shallow Universal Polynomial Networks [PDF](https://arxiv.org/pdf/2511.21414), [HTML](https://arxiv.org/abs/2511.21414)
### Authors
Zachary Morrow,Michael Penwarden,Brian Chen,Aurya Javeed,Akil Narayan,John D. Jakeman
### Background
深度神经网络（DNNs）和柯尔莫哥洛夫-阿诺尔德网络（KANs）因其灵活性和表达能力而在函数近似中受到青睐，但通常需要大量的可训练参数才能产生合适的近似。过度参数化不仅使网络变得不透明，还创建了一个巨大的优化空间，可能会在训练过程中产生具有很大不同泛化误差的局部最小值。因此，网络初始化对模型的外样本准确性有很大影响。
### Innovation
本文提出了浅层通用多项式网络（SUPNs），通过将除最后一个隐藏层之外的所有隐藏层替换为具有可学习系数的多项式层，结合了DNNs和多项式的优点，以达到足够的表达能力，所需的参数却少得多。理论证明了SUPNs以与相同度数的最佳多项式逼近相同的速度收敛，并推导出了全部最优SUPN参数的显式公式。此外，通过大量数值实验，展示了SUPNs在可训练参数数量相同的情况下，对于目标函数的近似误差和变化性往往比DNNs和KANs低一个数量级，甚至在非光滑函数上超越多项式投影。
### Conclusion
在研究的目标函数中，对于给定数量的可训练参数，SUPNs的近似误差和变化性往往比DNNs和KANs低一个数量级。在我们的示例中，SUPNs甚至在非光滑函数上表现优于多项式投影。
## 693. `cs.LG` - IntAttention: 在高效边缘推理中的一种全整数注意力管道 [PDF](https://arxiv.org/pdf/2511.21513), [HTML](https://arxiv.org/abs/2511.21513)
### Authors
Wanli Zhong,Haibo Feng,Zirui Zhou,Hanyang Peng,Shiqi Yu
### Background
在边缘设备上部署Transformer模型受到延迟和能量预算的限制。虽然INT8量化有效地加速了主要的矩阵乘法，但暴露了softmax作为主要瓶颈。这个阶段需要昂贵的去量化-softmax-再量化迂回路径，这可以占据总注意力延迟的65%以上，并且破坏了边缘硬件的端到端整数数据流，对于边缘硬件效率至关重要。
### Innovation
提出了一种名为IntAttention的第一种全整数、即插即用注意力管道，无需重新训练。核心在于IndexSoftmax，这是一种硬件友好的操作，完全在整数域内替换浮点指数。IntAttention集成了感知稀疏性的剪切、32个入口查找表近似和直接整数规范化，从而消除了所有数据类型转换的开销。
### Conclusion
评估了IntAttention，展示了持续且显著的收益。该方法在Armv8 CPU上实现了相对于FP16基线高达3.7倍的加速和61%的能量减少，并比传统INT8注意力管道快2.0倍。这些收益在不同语言和视觉模型中保持了高保真度的准确性，能够使Transformer推理在通用边缘设备上具有实际和高效性。代码将在作品的后续版本中发布。
## 694. `cs.LG` - 数据流中分类器投票线性独立视角下的集成性能 [PDF](https://arxiv.org/pdf/2511.21465), [HTML](https://arxiv.org/abs/2511.21465)
### Authors
Enes Bektas,Fazli Can
### Background
集成学习通过组合多个基分类器来提高分类性能。虽然增加分类器数量一般可以提高准确性，但过大的集成可能导致计算效率下降和收益递减。本文通过研究数据流中分类器投票的线性独立性来探讨集成规模和性能的关系。
### Innovation
本文提出，由线性独立的分类器组成的集成可以最大化表示能力，尤其是基于几何模型时。我们还将线性独立的重要性扩展到了加权多数投票问题。通过建模分类器输出实现线性独立的概率，我们得出了一个理论框架，解释了集成规模与准确性之间的权衡关系。通过该理论框架，我们可以估算出达到用户指定概率的线性独立所需的集成规模。
### Conclusion
我们的实验表明，该理论估计有效识别了如OzaBagging这类稳健集成的性能饱和点。对于像GOOWE这类复杂的加权方案，框架显示高理论多样性可能导致算法不稳定。我们已公开实现代码以支持可重复性和未来研究。
## 695. `cs.LG` - BanglaASTE：使用集成深度学习在孟加拉电子商务评论中提取方面-情感-观点的新框架 [PDF](https://arxiv.org/pdf/2511.21381), [HTML](https://arxiv.org/abs/2511.21381)
### Authors
Ariful Islam,Md Rifat Hossen,Abir Ahmed,B M Taslimul Haque
### Background
Aspect-Based Sentiment Analysis (ABSA) 已经成为从用户生成的内容中提取细粒度情感洞察的关键工具，特别是在电子商务和社交媒体领域。然而，由于缺乏全面的数据集和专有的三元组抽取框架，关于孟加拉语的 ABSA 研究还远远未能充分探索。
### Innovation
本研究的贡献包括：(1) 创造了第一个标注的 Bangla Aspect Sentiment Triplet Extraction (ASTE) 数据集，包含 3,345 条产品评论，来自于大型电子商务平台如 Daraz、Facebook 和 Rokomari；(2) 开发了一种结合基于图的方面-情感匹配和语义相似性技术的混合分类框架；(3) 实施了一个结合 BanglaBERT 上下文嵌入和 XGBoost 提升算法的集成模型，提升了三元组抽取性能。实验结果表明，我们的集成方法在所有评估指标中显著优于基线模型，准确率为 89.9%，F1 得分为 89.1%。
### Conclusion
本研究解决了孟加拉文本处理中的关键挑战，如非正式表达、拼写变异和数据稀疏性，推动了低资源语言情感分析的前沿，并提供了适用于孟加拉电子商务分析应用的可扩展解决方案。
## 696. `cs.LG` - 基于多尺度时间对齐的临床风险预测的机器学习方法：电子健康记录中的多尺度时间对齐 [PDF](https://arxiv.org/pdf/2511.21561), [HTML](https://arxiv.org/abs/2511.21561)
### Authors
Wei-Chen Chang,Lu Dai,Ting Xu
### Background
本文研究了电子健康记录（EHR）中的时间不规则性、采样间隔差异和多尺度动态依赖性带来的挑战。传统的分析方法难以处理这些复杂性，因此需要一种新的方法来准确预测患者风险。
### Innovation
提出了一种基于多尺度时间对齐网络（MSTAN）的风险预测方法。该方法通过引入可学习的时间对齐机制和多尺度卷积特征提取结构，联合建模EHR序列中的长期趋势和短期波动。此外，通过时空嵌入和对齐模块动态加权不规则采样数据，减少时间分布差异对模型性能的影响。该方法通过多层卷积和层次融合捕捉不同时间粒度的关键模式，实现精细的患者状态表示。最后，基于注意力的聚合机制整合全局时间依赖性，生成个体级别的风险表示，用于疾病风险预测和健康状况评估。
### Conclusion
实验结果显示，所提出的方法在准确性、召回率、精确率和F1-Score方面优于主流基线，证明了在复杂医疗时间序列分析中多尺度时间对齐的有效性和鲁棒性。该研究为高维非同步医疗序列的智能表示提供了新的解决方案，并为基于EHR的临床风险预测提供了重要的技术支持。
## 697. `cs.LG` - 计算非线性分类器的战略响应 [PDF](https://arxiv.org/pdf/2511.21560), [HTML](https://arxiv.org/abs/2511.21560)
### Authors
Jack Geary,Boyan Gao,Henry Gouk
### Background
本文探讨了战略分类问题，其中分类器的部署导致了策略行为，从而在后续观察中引起了分布偏移。当前在战略设置下学习分类器的方法主要集中在线性分类器上，但在许多情况下，非线性分类器更为适宜。非线性分类器的一个主要限制是从这些环境中计算出最优响应的能力不足。
### Innovation
本文提出了一种新的方法，通过优化代理目标的拉格朗日对偶来计算最优响应。这种方法不仅再现了线性设置下的最优响应，还指出了一些现有方法的关键弱点，并展示了该方法可以简单地应用于非线性分类器设置，有助于评估和训练。
### Conclusion
我们的方法能够在非线性分类器设置中产生最优响应，适用于评价和训练，从而解决了非线性分类器在策略设置中计算最优响应的难题。
## 698. `cs.LG` - Transformer-based Time Series Classification的机制可解释性 [PDF](https://arxiv.org/pdf/2511.21514), [HTML](https://arxiv.org/abs/2511.21514)
### Authors
Matīss Kalnāre,Sofoklis Kitharidis,Thomas Bäck,Niki van Stein
### Background
Transformer基于模型已成为各种机器学习任务中的前沿工具，包括时间序列分类。然而，其复杂性使得理解其内部决策机制变得困难。现有可解释性方法通常关注输入-输出归因，而忽视了内部机制。这项研究通过将机制可解释性技术如激活掩模、注意力显著性和稀疏自编码器从自然语言处理（NLP）领域迁移到专门用于时间序列分类的Transformer架构，填补了这一空白。
### Innovation
该论文提出了将机制可解释性技术从NLP领域迁移到专为时间序列分类设计的Transformer架构中，系统探究了个体注意力层和时间步的内部因果作用，揭示了模型内部的因果结构。通过在基准时间序列数据集上的实验，构建了展示信息在内部传播的因果图，突出了驱动正确分类的关键注意力层和时间位置。此外，研究还展示了稀疏自编码器在揭示可解释的潜在特征方面的潜力。
### Conclusion
研究不仅为Transformer解释性提供了方法论贡献，还为Transformer在时间序列分类任务中的功能机械学提供了新颖见解。
## 699. `cs.LG` - 肽的膜渗透性预测中的解耦对准核 [PDF](https://arxiv.org/pdf/2511.21566), [HTML](https://arxiv.org/abs/2511.21566)
### Authors
Ali Amirahmadi,Gökçe Geylan,Leonardo De Maria,Farzaneh Etminani,Mattias Ohlsson,Alessandro Tibo
### Background
环肽在靶向细胞内位点方面表现出巨大的潜力，但细胞膜渗透性依然是一个关键瓶颈。这主要受到有限的公开数据和需要精确的不确定性校准的限制。当前方法通常依赖于复杂的数据密集型深度学习架构，而本文提出了一种基于氨基酸的解耦全局对准核（MD-GAK），该方法将化学上有意义的残基相似性与序列比对结合起来，并将局部匹配与间隙惩罚分离。为了进一步证明模型的鲁棒性，还引入了一种变体PMD-GAK，该变体包含三角形位置先验。
### Innovation
本文提出了两种新的核函数，即MD-GAK和PMD-GAK，这两种核函数能够解耦局部匹配和间隙惩罚，通过结合化学上有意义的残基相似性和序列比对，以减少校准误差。同时，作者使用高斯过程作为预测模型，展示了这两种方法的有效性。
### Conclusion
通过广泛的实验，本文证明了所提出的方法在所有评估指标上都优于最先进的模型，特别是在不确定性估计方面表现突出。
## 700. `cs.LG` - 使用共识优化训练的两层神经网络的均场极限 [PDF](https://arxiv.org/pdf/2511.21466), [HTML](https://arxiv.org/abs/2511.21466)
### Authors
William De Deyn,Michael Herty,Giovanni Samaey
### Background
本文研究了两层神经网络，并使用基于粒子的方法——共识优化（CBO）对其进行训练。在多任务学习的情境下，将CBO重新构造成一种具有较少内存消耗的形式。CBO方法允许通过最优输运框架中的均场极限进行 formulations，进而与神经网络的均场极限相耦合，最终在无限粒子的数量下定义相应的 Wasserstein-over-Wasserstein 空间上的动态，展示了方差的单调减少。
### Innovation
我们比较了共识优化（CBO）与 Adam 的性能，表明混合方法（结合CBO和Adam）能够提供更快的收敛速度。在多任务学习的情境下，我们对CBO方法进行了重构，以提供更少的内存消耗。研究还通过最优输运框架将CBO方法的均场极限形式与神经网络的均场极限进行了耦合，并在无限粒子资源的情况下，定义了相应的动态，并展示了方差的单调减少。
### Conclusion
该研究展示了使用共识优化训练两层神经网络的方法及其均场模型的构建，并在多任务学习中展示了其潜在的应用价值，尤其是在内存维度受到限制的场景下。进一步的实验表明混合CBO和Adam的策略具有更好的广泛性和快速收敛性。在无限粒子条件下的定义动态证明了方差的单调减少趋势。
## 701. `cs.LG` - 时间迷失了吗？一种时间偏移鲁棒的生理信号变换的元学习框架 [PDF](https://arxiv.org/pdf/2511.21500), [HTML](https://arxiv.org/abs/2511.21500)
### Authors
Qian Hong,Cheng Bian,Xiao Zhou,Xiaoyu Li,Yelei Li,Zijing Zeng
### Background
非侵入式信号如光体积描记图(PPG)和球卡德哥瑞图(BCG)转换为有临床意义的信号如动脉血压(ABP)，对持续、低成本的健康监控至关重要。然而，多模态信号转换中的时间错位影响了转换精度，特别是ABP峰值的捕捉。传统的时间同步方法依赖于强烈的相似性假设或手动调整，而现有的有噪声标签学习(LNL)方法在时间偏移监督下无效，要么丢弃过多的数据，要么无法纠正标签偏移。
### Innovation
本文提出了一种基于元学习的双层优化框架——ShiftSyncNet，自动减轻由于时间错位导致的性能退化。该框架包括一个转换网络(TransNet)和一个时间偏移校正网络(SyncNet)，其中SyncNet学习训练样本对之间的时间偏移，并使用傅里叶相位偏移来对齐监督信号。
### Conclusion
实验结果显示，ShiftSyncNet 在一个实际工业数据集和两个公开数据集上的表现分别优于强基线 9.4%，6.0% 和 12.8%。结果表明该方法在不同时间错位场景下都能有效校正时间偏移、提高标签质量和转换精度，为解决多模态生理信号变换中的时间不一致性问题提供了一个统一的方向。
## 702. `cs.LG` - 基于Dyna-Q强化学习的预测性安全防护 [PDF](https://arxiv.org/pdf/2511.21531), [HTML](https://arxiv.org/abs/2511.21531)
### Authors
Jin Pin,Krasowski Hanna,Vanneaux Elena
### Background
为实际任务应用强化学习，获取安全保障是一个重大挑战。现有的安全防护机制通常使用随机安全动作采样或固定的备份控制器，忽视了不同安全动作对未来性能的影响。
### Innovation
提出了一种预测性安全防护机制，用于基于模型的离散空间强化学习代理。该机制利用环境模型的预测结果局部更新Q函数，既能保证安全性又能提升性能。实验结果表明，即使是较短的预测 horizon 也能用于识别最优路径，并观察到该方法在分布转移时具有鲁棒性，无需额外训练。
### Conclusion
本文的方法能够提升性能同时维持硬性安全保证。通过环境模型的预测生成安全动作，证明了在网格世界环境中的有效性和鲁棒性。
## 703. `cs.LG` - 学习何时停止：基于强化学习的自适应潜在推理 [PDF](https://arxiv.org/pdf/2511.21581), [HTML](https://arxiv.org/abs/2511.21581)
### Authors
Alex Ning,Yen-Ling Kuo,Gabe Gomes
### Background
潜在推理是一种在Transformer语言模型中的新发展，相比链式思考推理，它能够在压缩推理长度方面显示出潜力。潜在推理通过直接将信息丰富的上一序列的最终潜在状态传递给下一个序列，而不仅仅是依赖人类语言标记作为推理的媒介，从而消除了这种限制。
### Innovation
研究人员通过开发自适应长度的潜在推理模型，并引入后SFT强化学习方法来优化潜在推理长度，从而最小化推理长度的同时保持准确性。这种方法进一步减少了计算使用量，提高了潜在推理模型压缩能力的门槛。实验表明，在Llama 3.2 1B模型和GSM8K-Aug数据集上，总推理长度减少了52%，且不会对准确性产生惩罚。
### Conclusion
未来的工作扩展到其他模型和数据集，分析训练系数之间的关系，试验架构变化，并继续我们的潜在推理SFT知识精练努力。相关代码和预训练权重已发布。
## 704. `cs.LG` - 使用迭代PPO使大语言模型朝向多轮对话结果对齐 [PDF](https://arxiv.org/pdf/2511.21638), [HTML](https://arxiv.org/abs/2511.21638)
### Authors
Daniel R. Jiang,Jalaj Bhandari,Yukai Yang,Rémi Munos,Tyler Lu
### Background
在涉及频繁交互的任务（如AI营销或使用消息平台进行销售代理）中，优化大型语言模型（LLMs）以实现多轮对话目标仍然是一个重大挑战。这一难题源于稀疏的长期奖励信号，以及在响应级别规划和标记级别生成之间的不匹配。
### Innovation
提出了一种将多轮强化学习（RL）问题形式化为一系列单轮RLHF（RL with Human Feedback）问题的方法。通过将其学习到的多轮Q函数作为单轮问题的奖励模型。此外，该研究证明了使用标准标记级别的PPO解决单轮RL问题等同于在多轮问题内进行策略改进步骤。基于这一发现，提出了一种迭代PPO算法，该算法交替使用从已记录的对话轨迹中拟合Q函数并改进策略。与完全在线或完全离线方法相比，该方法兼具在线更新的适应性和离线训练的稳定性。
### Conclusion
迭代PPO算法直接利用了稳定的单轮RLHF工具，简化了其实现。该方法在完全在线和完全离线方法之间找到了一个平衡，保留了在线更新的灵活性，同时获得了离线训练的稳定性优势。
## 705. `cs.LG` - 无观察情境下的上下文特定因果图发现：非平稳性、状态及时空模式 [PDF](https://arxiv.org/pdf/2511.21537), [HTML](https://arxiv.org/abs/2511.21537)
### Authors
Martin Rabel,Jakob Runge
### Background
实世界数据，例如用于气候应用的数据，通常表现为网格化的时间序列数据或具有类似结构的数据。这些系统通常被认为在空间和时间的不同位置会以相似的行为方式表现，但存在的变异对结果稳定性/收敛性以及算法假设的平稳性或空间平移不变性具有重要影响。因此，研究因果图变化所编码的信息变得至关重要。
### Innovation
该研究提出了一种新的框架，通过修改基于约束的因果发现方法中的独立性检验来解决非平稳性问题。这一框架具有极大模块化、易扩展和广泛应用的特点，并能够采用现有的基于约束的因果发现方法（如IID算法PC、PC-stable、FCI和时间序列算法PCMCI、PCMCI+、LPCMCI）进行改进，且仅需少量或无需修改。此外，此框架可以通过利用变化点检测、聚类、独立性检验和其他相关问题的见解来扩展，从而可以系统地理解和解决一系列子问题，并简化对基本局限性、超参数控制的权衡以及统计解释的理解。
### Conclusion
该框架能够通过对可访问子问题的划分来简化基本局限性的理解、超参数控制的权衡以及统计解释，并且具备开放源码实现，即将发布。它能更好地处理时空变化带来的非平稳性、状态变化和时空模式问题。
## 706. `cs.LG` - 视觉变换器中非单调缩放机制 [PDF](https://arxiv.org/pdf/2511.21635), [HTML](https://arxiv.org/abs/2511.21635)
### Authors
Anantha Padmanaban Krishna Kumar(Boston University)
### Background
深度视觉变换器往往不如较浅的变换器表现好，这挑战了常见的缩放假设。通过在ImageNet上对ViT-S、ViT-B和ViT-L的系统性实证分析，我们发现一种一致的三相悬崖-平台-攀升模式，该模式决定了表示随深度的发展过程。我们观察到，更好的性能与[CLS]标记的逐步淘汰有关，该标记最初设计为全局聚合中心，更多地转向了块标记之间分散的一致性。
### Innovation
我们量化了信息混合模式的信息打乱指数，并展示了在ViT-L中，信息任务权衡出现的时间比在ViT-B中晚约10层，而且额外的这些层与信息扩散增强而非任务性能改进相关。这些结果表明，该区间内的变换器架构可能更多地受益于精心校准的深度执行干净的相转变，而不是简单地增加参数数量。信息打乱指数为现有的模型提供了一个有用的诊断工具，并暗示了对未来架构的设计目标。
### Conclusion
本文研究结果表明，视觉变换器可能更受益于精心校准的深度执行干净的相转变，而不是简单地增加参数数量。信息打乱指数可以为现有模型提供有用的诊断工具，并可能为未来架构设计提供目标。
## 707. `cs.LG` - AI-驱动的智能电网混合 cyber-物理框架进行自适应控制 [PDF](https://arxiv.org/pdf/2511.21590), [HTML](https://arxiv.org/abs/2511.21590)
### Authors
Muhammad Siddique,Sohaib Zafar
### Background
智能电网将传统的电力基础设施与先进的通信网络和智能控制融合，创造了一个比以往更高效、更灵活的网络物理环境。然而，这种融合导致了新的漏洞，威胁了电网的稳定性和可靠性。数字取证是学习、识别、检测和缓解这些安全事件的基本概念。当前的研究提出了一种基于机器学习的整体数字取证框架，该框架基于云端部署，并结合了传感器级的数据采集、认证通信、可扩展的云存储和自动法医分析。
### Innovation
该论文提出了一种全新的基于机器学习的综合数字取证框架，该框架部署在云端。该框架融合了传感器级数据采集、认证通信、可扩展的云存储以及自动法医分析，采用了监督学习（如随机森林、支持向量机、梯度提升树）和无监督学习（深度神经网络）算法进行异常检测、事件重建和即时入侵分析。此外，该研究通过实际的智能电表数据流进行了模拟和实验，结果表明该框架具有非常高的准确性和对数据篡改、虚假数据注入和协同控制环路操纵等网络攻击的鲁棒性。
### Conclusion
研究结果表明，云服务是大数据驱动法医工作流程的最优基础，使能源供应商能够快速掌握情况并进行智能化的应急响应。
## 708. `cs.LG` - DSD: 分布式推测性解码解决方案，用于边缘-云敏捷大模型服务 [PDF](https://arxiv.org/pdf/2511.21669), [HTML](https://arxiv.org/abs/2511.21669)
### Authors
Fengze Yu,Leshu Li,Brad McDanel,Saiqian Zhang
### Background
大型语言模型（LLM）推理常常遭受高解码延迟和跨异构边缘-云环境的有限扩展性的问题。现有的推测性解码（SD）技术可以加速token生成，但仍然局限于单节点执行。
### Innovation
我们提出了DSD，这是一种分布式推测性解码框架，通过协调草案目标执行将SD扩展到多设备部署。首先，我们引入了DSD-Sim，这是一种离散事件模拟器，用于捕捉网络、批量处理和调度动态。基于DSD-Sim的洞见，我们进一步设计了一个自适应窗口控制（AWC）策略，该策略根据需求动态调整推测窗口大小以优化吞吐量。
### Conclusion
实验表明，DSD实现了与现有SD基线下高达1.1倍的速度提升和9.7%更高的吞吐量，使边缘和云环境下的LLM服务更加敏捷和可扩展。
## 709. `cs.LG` - 通过降维可视化大型语言模型潜在空间几何结构 [PDF](https://arxiv.org/pdf/2511.21594), [HTML](https://arxiv.org/abs/2511.21594)
### Authors
Alex Ning,Vainateya Rangaraju
### Background
大型语言模型（LLMs）在众多自然语言任务中取得了最先进的成果，但在其内部机制的解释方面仍然极具挑战性。本文通过降维技术从Transformer架构的语言模型中提取、处理并可视化潜在状态几何结构。
### Innovation
本文通过逐层捕获Transformer块中多个点的激活，并利用主成分分析（PCA）和均匀流形逼近（UMAP）实现系统分析。研究发现在中间层中注意机制和MLP组件输出之间有一个明显的区分，这一模式在以往的研究中未被记录。此外，还展示了GPT-2的位置嵌入的高维螺旋结构、LLaMa中的序列间几何模式，并尝试重复令牌序列。
### Conclusion
本文旨在支持Transformer内部结构的系统分析，使其成为一个可行的研究基础，从而推动进一步可复制的解释性研究。代码已公开发布。
## 710. `cs.LG` - 神经网络中的规模无关寇莫罗夫-阿诺尔德几何 [PDF](https://arxiv.org/pdf/2511.21626), [HTML](https://arxiv.org/abs/2511.21626)
### Authors
Mathew Vanherreweghe,Michael H. Freedman,Keith M. Adams
### Background
弗里德曼和穆利根的近期研究表明，在合成的三维任务上，浅层多层感知机（MLP）在训练过程中自发形成了柯莫罗夫-阿诺尔德几何（KAG）结构。然而，尚不清楚这种现象是否在真实的高维环境中持续存在，以及这些几何的时空特性如何。
### Innovation
将KAG分析应用于MNIST手写数字分类（784维），使用两层MLP并在多个尺度上进行系统空间分析。发现在训练过程中KAG结构自发形成，并且这些结构在多个尺度上保持一致，从局部7像素的邻域到完整的28x28图像。通过标准训练和具有空间增强的训练均能产生相同的模式。
### Conclusion
神经网络在学习现实高维数据时自发地开发出有组织、尺度不变的几何结构。
## 711. `cs.LG` - 电信视角下的训练样本：所有训练样本的重要性吗？ [PDF](https://arxiv.org/pdf/2511.21668), [HTML](https://arxiv.org/abs/2511.21668)
### Authors
Shruti Bothe,Illyyne Saffar,Aurelie Boisbunon,Hasan Farooq,Julien Forgeat,Md Moin Uddin Chowdhury
### Background
人工智能在电信领域的应用，从优化无线接入网络到管理用户体验，显著增加了数据量和训练需求。电信数据通常噪声较大、维度高、存储和处理成本高，且需要大量标签。尽管人工智能发挥着重要作用，传统的训练工作流仍假设所有训练样本同等重要。然而，下一代系统需要准确、高效的AI模型。本文关注训练样本在电信训练中的个体角色及其重要性，挑战所有样本同等重要的假设。
### Innovation
本文提出了一种样本重要性框架，通过样本级别梯度分析识别模型学习中的影响模式和冗余，从而有选择性地优先处理关键数据，以减少计算量而不牺牲准确性。这一方法在三个实际的电信数据集上进行了验证，结果显示该方法可以保持性能同时减少数据需求和计算开销，推进可持续人工智能的目标。
### Conclusion
我们的方法实现了在减少数据需求和计算开销的同时保持性能，从而推动了电信领域可持续人工智能的发展目标。
## 712. `cs.LG` - 国际学生知识背景下LLMs的领域导向评估 [PDF](https://arxiv.org/pdf/2511.20653), [HTML](https://arxiv.org/abs/2511.20653)
### Authors
Claudinei Daitx,Haitham Amar
### Background
大型语言模型（LLMs）在回答关于留学申请、签证、奖学金和资质等高风险问题方面越来越受欢迎。然而，目前尚不清楚这些模型在提供建议时的可靠性，以及它们所提供答案的支持度（即“错误的断言”或“幻觉”）。本研究对现有LLMs在这一领域的表现进行了详细分析，提出了一个清晰且基于领域的方法来评估这些问题。
### Innovation
本研究使用真实的问题集来识别在教育和技术平台上常见的问题，这些平台旨在支持学生从发现到入学的全过程。研究同时测评了模型的准确性（信息是否正确且完整）和幻觉（是否添加了没有支持问题或领域证据的内容）。此外，研究还提供了一个可重复使用的协议来评估LLMs，以确保其符合教育和咨询环境下的实际质量要求。
### Conclusion
本研究旨在揭示哪些模型在留学咨询中最为可靠，找出常见的失败模式，并提供一个实用的协议来评估准备部署到教育和咨询环境中的LLMs的真实性和相关性。
## 713. `cs.LG` - 使用强化学习的加密货币投资组合管理：Soft Actor--Critic和Deep Deterministic Policy Gradient算法 [PDF](https://arxiv.org/pdf/2511.20678), [HTML](https://arxiv.org/abs/2511.20678)
### Authors
Kamal Paykan(Department of Mathematics, Tafresh University, Tafresh, Iran)
### Background
传统的投资组合优化方法在应对加密货币市场高度波动性和非线性动态时常常表现不佳。为了克服这一问题，本文提出了一种基于强化学习的框架，通过历史市场数据和模拟交易环境，直接学习连续交易行为以优化投资组合权重，旨在最大化累计收益并最小化下行风险和交易成本。
### Innovation
本文采用Soft Actor--Critic (SAC) 和 Deep Deterministic Policy Gradient (DDPG) 算法构建投资组合优化框架。实验结果显示，SAC和DDPG策略在多种加密货币上的表现优于传统的等权重和均值-方差投资组合策略，并且SAC算法在噪声市场条件下显示出更好的稳定性和鲁棒性。
### Conclusion
这些结果表明，深度强化学习在适应性和数据驱动的加密货币市场投资组合管理中具有巨大的潜力。
## 714. `cs.LG` - EvilGenie: 一个奖励劫持基准 [PDF](https://arxiv.org/pdf/2511.21654), [HTML](https://arxiv.org/abs/2511.21654)
### Authors
Jonathan Gabor,Jayson Lynch,Jonathan Rosenfeld
### Background
本文介绍了一个名为EvilGenie的基准测试，用于在编程环境中评估奖励劫持。该基准来源于LiveCodeBench的问题，并创建了一个易于实施奖励劫持的环境，如通过硬编码测试案例或编辑测试文件。本文通过三种方式衡量奖励劫持：预留单元测试、LLM裁判和测试文件编辑检测。作者验证了这些方法的人类审阅结果和其他方法的对比效果。
### Innovation
引入了通过预留单元测试、LLM裁判和测试文件编辑检测来评估奖励劫持的新方法，特别构建了一个易于实施奖励劫持的环境。此外，作者还测试了多种模型，并评估了三个流行的私有编码代理（OpenAI的Codex、Anthropic的Claude Code和Google的Gemini CLI）对奖励劫持的表现。
### Conclusion
LLM裁判在明确的情况下对检测奖励劫持非常有效，而预留测试案例的使用仅带来微小的改进。Codex和Claude Code表现出明确的奖励劫持行为，而所有三个代理都表现出与预期不符的行为。研究团队的代码可以在这个网站找到。
## 715. `cs.LG` - 关于AI算法进步的起源 [PDF](https://arxiv.org/pdf/2511.21622), [HTML](https://arxiv.org/abs/2511.21622)
### Authors
Hans Gundlach,Alex Fogelson,Jayson Lynch,Ana Trisovic,Jonathan Rosenfeld,Anmol Sandhu,Neil Thompson
### Background
自2012年至2023年，算法被估计能使AI训练的FLOP效率提高22,000倍[Ho et al., 2024]。通过在这一时期的关键创新上进行小型剥离实验，我们只能解释其中不到10倍的效率提升。通过对更广泛文献的概述，我们估计其他的创新贡献也少于10倍，总计不到100倍。这一发现促使我们进行规模实验，以确认大部分效率差距是由与缩放规模相关的算法改进所解释的。实验表明，对比LSTM和Transformer，尽管大多数其他创新没有明显的规模趋势，但在compute-optimal缩放定律上存在指数级差异。
### Innovation
通过实验剥离分析，本研究发现算法效率提升与计算规模密切相关。特别是，在实验中发现LSTM向Transformer转换的过程中，算法效率提升显著，大多数增益归功于这种转换。此外，研究表明，小模型算法的进步远慢于先前的假设，算法效率指标具有强烈的参考依赖性。
### Conclusion
算法效率在小型模型上的提升远低于之前的假设，且算法效率改进与计算规模密切相关。这表明，未来的算法改进需要考虑其在不同计算规模下的效率表现。
## 716. `cs.LG` - 谐波令牌投射（HTP）：一种词汇表无关、无需训练、确定性和可逆嵌入方法 [PDF](https://arxiv.org/pdf/2511.20665), [HTML](https://arxiv.org/abs/2511.20665)
### Authors
Tcharlies Schmitz
### Background
本文介绍了一种名为谐波令牌投射（HTP）的新框架，该框架无需训练、词汇表和随机参数即可生成文本嵌入。与依赖统计共现或优化的神经嵌入不同，HTP 通过 Unicode 整数表示生成每个令牌作为分析性的谐波轨迹，从而在离散符号与连续向量空间之间建立双向和可解释的映射。实验评估表明，HTP 在英语Semantic Textual Similarity Benchmark（STS-B）以及其多语言扩展版本中实现了稳定的性能，相关系数为 0.68，在不同语言上的表现稳定，计算成本低且每对句子的延迟仅为毫秒级。
### Innovation
HTP 通过 Unicode 整数表示生成每个令牌作为和谐波轨迹，实现了双向和可解释的映射。这种和谐波表示提供了相位相干的投影，保留了结构和可逆性，从而能够仅通过几何对齐来估计语义相似性。该方法无需训练和词汇表，计算成本低，处理速度极快，提供了一种透明且高效的替代数据驱动嵌入的方法。
### Conclusion
实验表明，有意义的语义关系可以在确定性几何结构中自然地产生，HTP 提供了一种替代数据驱动嵌入的透明且高效的可逆嵌入方法。方法在多种语言上都表现出稳定性和高效性，证明了无需训练和词汇表的情况下也可以生成有效的文本嵌入。
## 717. `cs.LG` - 模型验证的一套规则 [PDF](https://arxiv.org/pdf/2511.20711), [HTML](https://arxiv.org/abs/2511.20711)
### Authors
José Camacho
### Background
模型验证是评估模型在目标人群的新、未见过的数据中泛化能力的过程。现有方法可能存在不足之处，因此需要一套通用规则来帮助实践者制定可靠的验证计划，并透明地报告结果。
### Innovation
本文提出了一套通用的模型验证规则，旨在帮助实践者创建可靠的验证计划，并透明地报告结果。尽管没有任何验证方案是完美的，但这些规则可以帮助实践者确保其策略适用于实际应用，公开讨论其验证策略的任何局限性，并报告清晰且可比较的性能指标。
### Conclusion
这些规则可以提高模型验证过程的透明度和可靠性，确保模型在新的未见过的数据中具有良好的泛化能力。
## 718. `cs.LG` - 使用LLM指导的层级重构以最小化超曲面嵌入失真 [PDF](https://arxiv.org/pdf/2511.20679), [HTML](https://arxiv.org/abs/2511.20679)
### Authors
Melika Ayoughi,Pascal Mettes,Paul Groth
### Background
超曲面几何有效地表示层次化数据结构，因此在处理数据具有层次化组织或由层次化语义指导的应用中越来越受到重视，包括推荐系统和计算机视觉。超曲面嵌入的质量与输入层次结构的结构密切相关，通常来自于知识图谱或本体。最新研究表明，对于最优的超曲面嵌入，高分支因子和单一继承是关键，而嵌入算法对不平衡和层次结构规模不敏感。为了帮助知识工程师重新组织层次化知识，本研究探讨了大型语言模型(生成式或检索增强式)能否自动重构层次结构以满足上述条件。
### Innovation
提出了使用prompt引导的方法来利用大型语言模型（LLM）重构现有的层次结构，使其符合超曲面嵌入的最佳标准。实验结果表明，由LLM重构的层次结构在多种嵌入质量标准上表现出了更高的质量，且这种重组是可解释的，为知识工程师提供了重构的依据。
### Conclusion
本研究结果表明，大型语言模型可以有效地指导层级结构的重构以优化超曲面嵌入的质量，并提供了可解释的重组方法。这对于改善数据嵌入的应用性能具有重要意义。
## 719. `cs.LG` - PropensityBench: 通过代理方法评估大型语言模型的潜藏安全风险 [PDF](https://arxiv.org/pdf/2511.20703), [HTML](https://arxiv.org/abs/2511.20703)
### Authors
Udari Madhushani Sehwag,Shayan Shabihi,Alex McAvoy,Vikash Sehwag,Yuancheng Xu,Dalton Towers,Furong Huang
### Background
近期大型语言模型（LLMs）的发展引发了对其潜在获取并滥用危险或高风险能力的关注，这些能力可能带来前沿风险。当前的安全评估主要测试模型的‘能力’，而忽略了如果模型获得高风险能力时，它可能会‘如何’行为。这种评估存在关键盲点，即模型可能战略性地隐藏其能力或迅速获得这些能力，同时潜在地倾向滥用。因此，评估模型的‘倾向性’（其在获得权力时采取有害行动的可能性）成为一个关键但未充分探索的评估维度。
### Innovation
该论文提出了PropensityBench，这是一种新的基准框架，通过使用代理工具评估模型在模拟危险能力下采取风险行为的倾向性。该框架涵盖了5,874个场景中的6,648种工具，涉及高风险领域：网络安全、自我扩散、生物安全和化学安全。通过控制的代理环境模拟访问强大能力，并在反映现实世界约束或激励模型可能遇到的压力下评估模型的选择，例如资源稀缺或获得更多自主权。结果表明，模型在压力下经常选择高风险工具，即使它们缺乏独立执行此类行动的能力。这项研究提出了从静态能力审计转向动态倾向性评估的必要性，以确保安全部署前沿人工智能系统。
### Conclusion
研究发现，模型在压力下经常选择高风险工具，即使它们缺乏独立执行此类行动的能力。这些发现呼吁从静态能力审计转向动态倾向性评估，作为安全部署前沿AI系统的前置要求。研究代码已开源。
## 720. `cs.LG` - AssurAI：构建韩语社会文化数据集以发现生成式AI潜在风险的经验 [PDF](https://arxiv.org/pdf/2511.20686), [HTML](https://arxiv.org/abs/2511.20686)
### Authors
Chae-Gyun Lim,Seung-Ho Han,EunYoung Byun,Jeongyun Han,Soohyun Cho,Eojin Joo,Heehyeon Kim,Sieun Kim,Juhoon Lee,Hyunsoo Lee,Dongkun Lee,Jonghwan Hyeon,Yechan Hwang,Young-Jun Lee,Kyeongryul Lee,Minhyeong An,Hyunjun Ahn,Jeongwoo Son,Junho Park,Donggyu Yoon,Taehyung Kim,Jeemin Kim,Dasom Choi,Kwangyoung Lee,Hyunseung Lim,Yeohyun Jung,Jongok Hong,Sooyohn Nam,Joonyoung Park,Sungmin Na,Yubin Choi,Jeanne Choi,Yoojin Hong,Sueun Jang,Youngseok Seo,Somin Park,Seoungung Jo,Wonhye Chae,Yeeun Jo,Eunyoung Kim,Joyce Jiyoung Whang,HwaJung Hong,Joseph Seering,Uichin Lee,Juho Kim,Sunna Choi,Seokyeon Ko,Taeho Kim,Kyunghoon Kim,Myungsik Ha,So Jung Lee,Jemin Hwang,JoonHo Kwak,Ho-Jin Choi
### Background
生成式AI的快速进化要求对其安全性进行更严格的评估。然而，现有的安全性数据集主要以英语为中心，无法捕捉韩国等非英语、社会文化背景下特定的风险。此外，这些数据集通常只包含文本模态数据，缺乏多样性。
### Innovation
本文提出了AssurAI，一个新的高质量控制的韩语多模态数据集，用于评估生成式AI的安全性。首先，定义了35个独特的AI风险因素分类法，这是一组跨学科专家根据现有框架改编的，涵盖了普遍危害和韩国社会文化背景的相关性。其次，利用这种分类法构建并发布了AssurAI，该数据集包括了总计11,480个文本、图像、视频和音频实例。第三，采用严格的数据质量控制流程确保数据完整性，包括两阶段建设（专家引导的种子和众包扩展）、三份独立注释以及专家红队迭代审查循环。初步研究验证了AssurAI在评估最近的LLM（大型语言模型）安全性方面的有效性。
### Conclusion
我们向公众发布了AssurAI，以促进适合韩国社区的安全和可靠生成式AI系统的发展。
## 721. `cs.LG` - DeeAD: 动态早期退出的视觉-语言-动作以实现高效的自主驾驶 [PDF](https://arxiv.org/pdf/2511.20720), [HTML](https://arxiv.org/abs/2511.20720)
### Authors
Haibo HU,Lianming Huang,Nan Guan,Chun Jason Xue
### Background
VLA模型可以统一感知、推理和轨迹生成，但在实现自主驾驶过程中，由于深入的变压器栈结构，其推理延迟显著。
### Innovation
提出了一种训练无损、基于动作的早期退出框架DeeAD，通过评估中间轨迹的物理可行性加速VLA规划。引入多跳控制器根据评分变化率自适应跳过冗余层。DeeAD无需重新训练即可集成到现有VLA模型中，实验结果显示了最高28%的变压器层稀疏性和29%的延迟减少，同时保持了规划质量和安全性。
### Conclusion
DeeAD在Bench2Drive基准测试中展示了在不牺牲规划质量和安全性的前提下，通过变压器层稀疏性和延迟减少实现了高效的自主驾驶规划。
## 722. `cs.LG` - 数据驱动方法和人工智能在工程设计中的应用：聚焦挑战与机遇的系统文献综述 [PDF](https://arxiv.org/pdf/2511.20730), [HTML](https://arxiv.org/abs/2511.20730)
### Authors
Nehal Afifi,Christoph Wittig,Lukas Paehler,Andreas Lindenmann,Kai Wolter,Felix Leitenberger,Melih Dogru,Patric Grauberger,Tobias Düser,Albert Albers,Sven Matthiesen
### Background
数据和计算智能的进步加速了数据驱动方法在产品开发中的应用，但在产品开发过程中的整合仍然不完整。这种不完整主要源于不确定性，特别是对于何时及如何使用哪些类型的数据驱动方法缺乏清晰性。
### Innovation
研究采用了PRISMA系统文献综述方法，将V模型简化为四个阶段：系统设计、系统实施、系统集成和验证。通过跨Scopus、Web of Science和IEEE Xplore（2014-2024）检索，筛选出114篇相关文献。研究发现，机器学习和统计方法是当前的主流，深度学习虽较为少见但呈上升趋势。监督学习、聚类、回归分析和代理建模在设计、实施和集成系统阶段较为常见，但在验证阶段应用较少。存在模型解释性有限、跨阶段可追踪性差和实际条件下验证不足等主要挑战。
### Conclusion
这是探索设计阶段指南的第一步，下一步应将计算机科学算法与工程设计问题和活动进行映射。
## 723. `cs.LG` - 摆脱验证者：通过演示学习推理 [PDF](https://arxiv.org/pdf/2511.21667), [HTML](https://arxiv.org/abs/2511.21667)
### Authors
Locke Cai,Ivan Provilkov
### Background
大型语言模型（LLMs）的训练通常依赖于带有任务特定验证器的强化学习（RL）。然而，许多实际的推理密集型任务缺乏这些验证器，尽管有大量的专家演示数据未充分利用，用于专注于推理的训练。
### Innovation
引入了RARO（相对对抗推理优化），该方法通过逆强化学习从专家演示中学到强大的推理能力。方法设置了一个对抗交互，其中策略（生成器）学习模仿专家答案，而评论家（鉴别器）学习比较和区分策略和专家的答案。该方法通过连续的强化学习训练策略和评论家，并识别出确保稳健学习的关键稳定技术。
### Conclusion
实验结果显示，RARO在对 Countdown、DeepMath 和诗歌创作的评估任务中的表现显著优于强验证器基线，并且与验证任务中的RL一样表现出稳健的可扩展趋势。这些结果表明，我们的方法能够仅从专家演示中引出强大的推理性能，即使在缺乏特定任务验证器的情况下也能实现稳健的推理训练。
## 724. `cs.LG` - 双域深度学习方法加速高对比度多孔介质井筒模拟局部基函数计算 [PDF](https://arxiv.org/pdf/2511.20685), [HTML](https://arxiv.org/abs/2511.20685)
### Authors
Peiqi Li,Jie Chen
### Background
在能源科学中，非均质多孔介质中的达西流是一个关键的井筒模拟问题。然而，这种介质的多尺度特征给传统的数值方法带来了巨大的计算负担和效率挑战。
### Innovation
提出了一个双域深度学习框架，用于加速MGMsFEM中多尺度基函数的计算，通过在频率域和空间域提取和解码渗透率场特征来快速生成多尺度基函数的数值矩阵。
### Conclusion
数值实验表明，该框架在保持高近似精度的同时显著提高了计算速度，有望在未来应用于实际的油藏工程中。
## 725. `cs.LG` - Foundry: 蒸馏3D基础模型到边缘 [PDF](https://arxiv.org/pdf/2511.20721), [HTML](https://arxiv.org/abs/2511.20721)
### Authors
Guillaume Letellier,Siddharth Srivastava(IIT Delhi),Frédéric Jurie,Gaurav Sharma(IIT Kanpur)
### Background
预训练的大规模数据集上的自监督学习（SSL）的基础模型已经成为强大的通用特征提取器。然而，这些模型的巨大规模和计算成本使其不适合在像机器人和AR/VR头显这样的边缘设备上部署。现有的压缩技术，如标准的知识蒸馏，可以创建高效的专业模型，但牺牲了基础模型最重要的普适性。
### Innovation
本文介绍了基础模型蒸馏（FMD），这是一种新的方法，可以将大型SSL模型压缩为紧凑、高效的代理，同时保留其通用的表征能力。提出了Foundry，作为FMD的第一个实现，用于3D点云。我们的方法，Foundry，训练一个学生来学习一个压缩的超标签集，这些超标签重建了老师的令牌级表示，捕获其潜在空间的紧凑基。一个单一的蒸馏模型在多样化的下游任务上具有强大的可迁移性，包括分类、部分分割和少量样本情景，同时使用远 fewer tokens和FLOPs，使得这些模型更适合在资源受限的硬件上部署。
### Conclusion
单个蒸馏模型在多种下游任务上达到了接近完整基础模型的性能，同时使用数量显著较少的tokens和FLOPs，这使得这些模型更加适用于资源受限的边缘设备的部署。
## 726. `cs.LG` - 人类大脑作为一种组合复杂体 [PDF](https://arxiv.org/pdf/2511.20692), [HTML](https://arxiv.org/abs/2511.20692)
### Authors
Valentina Sánchez,Çiçek Güven,Koen Haak,Theodore Papamarkou,Gonzalo Nápoles,Marie Šafář Postma
### Background
当前的基于图的方法在表示脑网络时系统地忽略了神经复杂性的高阶依赖关系，而大脑中很多信息处理涉及不可分解的高阶协同作用。传统的图方法难以捕捉这种复杂的高阶依赖关系。
### Innovation
本文提出了一种框架，使用信息论措施从功能性磁共振成像（fMRI）时间序列数据构建组合复杂体（CCs），这种框架能够同时捕捉到二阶和高阶神经交互作用，将拓扑深度学习和神经网络科学相结合。该框架直接从数据统计依赖性构建CCs，不同于拓扑提升方法将关系结构映射到高阶域。CCs通过引入更高阶的细胞来一般化图，这些细胞代表了脑区间的集体依赖性，自然地适应了神经处理的多尺度和分层次特性。
### Conclusion
本文提供的框架能够保留传统图方法不可见的高阶结构，并使拓扑深度学习（TDL）架构能够应用于神经数据，通过该框架可以量化和表示神经时间序列中的二阶和高阶依赖关系，在统一结构中进行了证明。
## 727. `cs.LG` - 多种路径检索的记忆：大规模语言模型中稳健检测训练数据泄露的多前缀框架 [PDF](https://arxiv.org/pdf/2511.20799), [HTML](https://arxiv.org/abs/2511.20799)
### Authors
Trung Cuong Dang,David Mohaisen
### Background
大规模语言模型在训练过程中，由于训练数据量庞大，容易直接记忆训练数据，从而导致隐私和版权风险。尽管此前已有研究提出了各种各样的记忆定义，但这些定义在全面捕捉这一现象方面仍存在局限性，尤其是在对齐模型中。为了应对此问题，本文引入了一种新的框架——多前缀记忆。此框架基于一个核心洞察：记忆中的序列被深度编码，因此可以通过远多于非记忆内容的前缀集合检索出来。
### Innovation
本文提出了一种新的多前缀记忆框架，通过定义，一段序列被认为是记忆中的，如果外部对抗性搜索能够识别出能够唤起它的不同前缀数量。该框架将焦点从单路径提取转移到衡量记忆的鲁棒性上，通过检索路径的多样性来评估。通过开源和对齐聊天模型的实验，本文证明这种多前缀定义可以可靠地区分记忆和非记忆数据，为审计LLMs中的数据泄露提供了一个稳健且实用的工具。
### Conclusion
实验结果显示，多前缀定义在区分记忆和非记忆数据方面表现可靠，为大规模语言模型的数据泄露审计提供了一种实用且可靠的工具，有助于评估和提高模型的隐私保护能力。
## 728. `cs.LG` - 不同数据集在Amazon CoT框架下的跨域评价 [PDF](https://arxiv.org/pdf/2511.20701), [HTML](https://arxiv.org/abs/2511.20701)
### Authors
Nitya Tiwari,Parv Maheshwari,Vidisha Agarwal
### Background
近期的工作虽然已经在多模态设置中扩展了CoT（推理链），并在诸如ScienceQA等科学问题解答基准测试中取得了最先进的结果，但这些方法在不同领域的普遍性尚未得到充分探索。本文对多模态推理链（Multimodal-CoT）进行了全面分析，评估了其在A-OKVQA、OKVQA和ChartQA数据集上的效果，这些数据集需要广泛的知识，包括常识和世界知识，远超科学推理的范畴。
### Innovation
本文实施了由Zhang et al. [3]提出的两阶段框架，该框架将推理解释与答案推断分离，并通过门控融合机制与基于T5的语言模型结合多模态特征。通过系统的消融研究，分析了视觉特征、推理解释质量和架构选择的贡献。研究发现，尽管视觉整合显著减少了推理解释中的幻觉，但CoT推理的效果在不同类型的问答题中差异显著，尤其是在常识推理方面存在特别的挑战。
### Conclusion
本文为研究人员实施多模态推理系统提供了实用见解，并指出了跨领域普遍性改进的关键领域。
## 729. `cs.LG` - 与恒星共舞：用于自主科学推理的太阳物理数据集与基准 [PDF](https://arxiv.org/pdf/2511.20694), [HTML](https://arxiv.org/abs/2511.20694)
### Authors
Kevin Lee,Russell Spiewak,James Walsh
### Background
在太阳物理科学领域，科学推理不仅依赖于记忆事实，还需要结合物理假设、保持一致的单位，并通过协调的方法提供清晰的科学格式。针对这些挑战，本文介绍了一个新的太阳物理数据集——《与恒星共舞》，并提供了一种初步的基准测试方法。
### Innovation
本文提出了一种新的数据集《与恒星共舞》，基于美国国家航空航天局（NASA）和大气研究大学合作组织（UCAR）的“与恒星共舞”暑期学校问题集构建，提供了清晰的问题和答案结构，包括问题背景、推理步骤、预期答案类型、真实目标、格式提示和元数据。该数据集使用带有单位的数值误差、符号等价性以及模式验证的程序式评分器进行评分。此外，本文对比测试了单次输入基准和四种多代理模式，发现通过系统工程原则分解工作流优于直接提示，尤其是在需要演绎推理而非纯粹归纳回忆的问题上。
### Conclusion
通过系统工程原则分解工作流的多代理模式相比直接提示在需要演绎推理的问题上表现出更高的性能。《与恒星共舞》数据集和基准测试方法为自主科学推理提供了新的数据支持和评估手段，有助于改进大型语言模型在科学推理任务中的表现。
## 730. `cs.LG` - 结构化提示使语言模型的评价更加稳健和全面 [PDF](https://arxiv.org/pdf/2511.20836), [HTML](https://arxiv.org/abs/2511.20836)
### Authors
Asad Aali,Muhammad Ahmed Mohsin,Vasiliki Bikia,Arnav Singhvi,Richard Gaus,Suhana Bedi,Hejie Cui,Miguel Fuentes,Alyssa Unell,Yifan Mai,Jordan Cahoon,Michael Pfeffer,Roxana Daneshjou,Sanmi Koyejo,Emily Alsentzer,Percy Liang,Christopher Potts,Nigam H. Shah,Akshay S. Chaudhari
### Background
随着语言模型（LMs）在各个领域中的广泛应用，能够准确估计其性能的高质量基准评估框架对于指导部署决策至关重要。现有的框架如Holistic Evaluation of Language Models（HELM）能够在多种任务上进行广泛评估，但由于它们依赖于固定提示，往往不能很好地适用于不同的语言模型，导致性能评估不够全面。除非我们能够估计出每种语言模型的天花板（通过调整提示来实现的最大性能），否则我们将低估其性能。因此，一种能够避免手工提示工程且可扩展的结构化提示框架，如DSPy，显得尤为重要。然而，还没有研究系统地评估这些框架下的各种基准P基准测试方法。
### Innovation
该研究提出了一种可重复的DSPy+HELM框架，引入了结构化提示方法，这些方法能够激发语言模型的推理过程，从而更准确地评估其表现。研究使用四种结构化提示方法对四种前沿语言模型进行了评估，并与现有的HELM基准得分进行了比较，结果显示了结构化提示在四个方面带来了改进：（1）减少了对LM性能的低估；（2）减少了不同基准评估结果之间的差异；（3）更准确地反映了性能差距；（4）导入了推理（逐步推理）可以减少LM对提示设计的敏感性，从而提高评价的一致性。这还不包括首例大规模的基准测试研究，展示了可扩展的性能天花板估算可以让基准更具有决策价值。
### Conclusion
该研究表明，可扩展的性能天花板估算能够使基准测试更有决策价值，从而帮助评估语言模型的性能。研究开源了DSPy+HELM集成框架和提示优化管道工具（可通过提供的链接获取）以推动进一步的研究工作。
## 731. `cs.LG` - SPHINX：一种用于视觉感知和推理的合成环境 [PDF](https://arxiv.org/pdf/2511.20814), [HTML](https://arxiv.org/abs/2511.20814)
### Authors
Md Tanvirul Alam,Saksham Aggarwal,Justin Yang Chae,Nidhi Rastogi
### Background
目前存在的基准和数据集大多受限于数据规模和任务多样性，难以真实地评估和提升大规模视觉语言模型（LVLMs）在视觉推理等任务上的能力。
### Innovation
Sphinx通过程序生成包含多种视觉元素（如动机、瓷砖、图表、图标和几何基本元素）的谜题，并配以验证性地面真相解决方案，从而实现精准评估和大规模数据集构建。它涵盖了25种任务类型，包括对称性检测、几何变换、空间推理、图表解释和序列预测。
### Conclusion
评估结果显示，即使是最先进的GPT-5模型也只能达到51.1%的准确率，远低于人类表现。同时，使用可验证奖励的强化学习显著提高了模型在这些任务上的准确性，并在外部视觉推理基准测试中获得了提升，证实了其在多模态推理领域的潜力。
## 732. `cs.LG` - NOIR 2.0:基于神经信号操作的智能机器人用于日常活动 [PDF](https://arxiv.org/pdf/2511.20848), [HTML](https://arxiv.org/abs/2511.20848)
### Authors
Tasha Kim,Yingke Wang,Hanvit Cho,Alex Hodges
### Background
神经信号操作智能机器人（NOIR）系统是一种多功能脑-机器人接口，允许人类使用脑信号来控制机器人完成日常任务。该接口利用脑电图（EEG）将人类关于特定物体和期望行动的意图直接翻译成机器人可以执行的命令。
### Innovation
NOIR 2.0 包括更快且更准确的大脑解码算法，将任务完成时间降低了46%。NOIR 2.0 使用少量示例学习算法来适应个别用户并预测其意图。新学习算法利用基础模型以更样本效率的方式学习和适应（15个演示 vs. 单个演示），显著减少了整体所需的人类时间65%。
### Conclusion
NOIR 2.0 提供了一种更高效的脑-机器人接口解决方案，通过更快的大脑解码和更具效率的学习算法，进一步提升了用户体验和系统的适应性。
## 733. `cs.LG` - RefTr：维护连贯轨迹的循环精炼用于3D血管树中心线图 [PDF](https://arxiv.org/pdf/2511.20823), [HTML](https://arxiv.org/abs/2511.20823)
### Authors
Roman Naeem,David Hagerman,Jennifer Alvén,Fredrik Kahl
### Background
血管和肺部气道等管状树结构对人体内物质运输至关重要。准确检测它们的中心线并保持正确的树结构对于临床任务如诊断、治疗计划和外科导航等非常重要。在这些应用中，保持高召回率至关重要，因为丢失小分支可能导致由于评估不完整或无法检测到异常而引发的致命错误。
### Innovation
RefTr是一个基于递归精炼连贯轨迹的3D图像到图模型，用于通过血管树中心线生成。它采用Producer-Refiner架构，基于Transformer解码器，Producer提出一组初始连贯轨迹，Refiner通过递归精炼来生成最终轨迹，形成了中心线图。连贯轨迹表示使得能够精炼完整轨迹并明确强制有效树结构。递归精炼方案提高了精度并在多次步骤中复用了相同的Refiner块，使解码器参数减少了2.4倍，相比之前最佳性能的模型，提出了高效的非最大抑制算法用于空间树图并合并重复分支以提高精度。
### Conclusion
RefTr在多个公共中心线数据集中展现了比之前最佳性能模型更优的召回率和可比的精度，同时提供了更快的推理速度和显著更少的参数，证明了它在3D医学影像中血管树分析中的潜力，作为新的最佳状态框架。
## 734. `cs.LG` - $?Delta$-NeRF: 通过残差控制和知识转移实现Neural Radiance Fields的增量细化 [PDF](https://arxiv.org/pdf/2511.20804), [HTML](https://arxiv.org/abs/2511.20804)
### Authors
Kriti Ghosh,Devjyoti Chakraborty,Lakshmish Ramaswamy,Suchendra M. Bhandarkar,In Kee Kim,Nancy O'Hare,Deepak Mishra
### Background
NeRFs在3D重建和新颖视角合成方面展现出显著的能力。然而，大多数现有的NeRF框架在引入新视角时需要进行全面重新训练，这限制了它们在数据按顺序到达的领域中的应用，特别是在基于卫星的地形分析中，该领域中的区域会因为时间的推移而反复被观测。增量细化NeRFs仍然没有得到充分探索，而简单的增量方法在无法访问过去数据时会出现灾难性遗忘。
### Innovation
提出了一个独特的模块化残差框架——$?Delta$-NeRF，用于增量NeRF细化。$?Delta$-NeRF引入了多种创新技术：1) 一个残差控制器，通过向冻结的基础NeRF注入逐层修正来实现细化，无需访问过去数据；2) 一种基于不确定性感知的门控机制，通过自适应组合基础和细化预测来防止过度修正；3) 一种视图选择策略，能够将训练数据量减少高达47%，同时保持性能；并且采用了知识蒸馏技术将增强的模型压缩到了原来大小的20%的学生网络。实验结果表明，在卫星图像上的$?Delta$-NeRF在性能上与联合训练方法相当，同时将训练时间减少了30-42%。
### Conclusion
$?Delta$-NeRF在各类基线中始终表现出色，与朴素微调相比，峰值信噪比提高了高达43.5%，在某些指标上超越了联合训练方法。
## 735. `cs.LG` - 数据融合在多模态学习分析及教育数据挖掘中的综述 [PDF](https://arxiv.org/pdf/2511.20871), [HTML](https://arxiv.org/abs/2511.20871)
### Authors
Wilson Chango,Juan A. Lara,Rebeca Cerezo,Cristóbal Romero
### Background
新的教育模式，如智能学习环境，利用数字和情境感知设备来促进学习过程。这带来了大量的多模态学生数据，可以被捕捉、融合和分析。这为研究人员和教育者提供了一个独特的机会，以更好地理解学习过程，并在必要时进行干预。
### Innovation
介绍了数据融合在学习分析（LA）和教育数据挖掘（EDM）中的应用，并回顾了主要的融合教育数据、数据融合方法和技术在智能学习中的应用。展示了该领域的现状，包括主要的开放问题、趋势和挑战。
### Conclusion
指出了在多模态学习分析和教育数据挖掘中的数据融合技术的应用现状，指出了该研究领域的主要开放问题、发展趋势和挑战。
## 736. `cs.LG` - 基于优化的视觉反转的无需训练的扩散先验生成文本到图像 [PDF](https://arxiv.org/pdf/2511.20821), [HTML](https://arxiv.org/abs/2511.20821)
### Authors
Samuele Dell'Erba,Andrew D. Bagdanov
### Background
扩散模型在文本到图像生成方面已经取得了最先进的效果，但其性能往往依赖于一个扩散先验网络将文本嵌入转换到视觉流形，以实现更简单的解码。然而，这些先验网络在计算上代价高昂，并且需要在大规模数据集上进行大量训练。
### Innovation
本文提出了优化基视觉反转（OVI）的方法，这是一种无需训练和无需数据的替代方法，用以替代传统的先验网络。OVI 通过从随机伪标记初始化潜在的视觉表示，并通过迭代优化最大化输入文本提示嵌入的余弦相似性。此外，提出了两个新的约束条件：基于马氏距离和最近邻损失，以规范化 OVI 的优化过程，使它更符合真实的图像分布。
### Conclusion
在 Kandinsky 2.2 上进行的实验表明，OVI 可以作为传统先验的替代方案。此外，我们的分析揭示了一个当前评估基准（如 T2I-CompBench++）的关键缺陷，其中，仅仅使用文本嵌入作为先验就能取得惊人的高分数，尽管其感知质量较低。与基于最近邻的方法相比，我们的受限 OVI 方法提高了视觉保真度，表明该方法值得一探究竟。
## 737. `cs.LG` - 通过空文本嵌入优化实现从文本到图像的扩散模型的测试时对齐 [PDF](https://arxiv.org/pdf/2511.20889), [HTML](https://arxiv.org/abs/2511.20889)
### Authors
Taehoon Kim,Henry Gouk,Timothy Hospedales
### Background
Test-time alignment (TTA)的主要目的是在推理过程中根据特定奖励调整模型，但现有方法往往不能很好地优化目标奖励函数，容易出现过度优化或奖励黑客现象。Null-Text Test-Time Alignment (Null-TTA)通过优化未条件化的文本嵌入而非操作潜在或噪声变量，来对扩散模型进行对齐。
### Innovation
Null-TTA 提出了一种创新的方法，通过优化未条件化的文本嵌入在无条件引导中对扩散模型进行对齐，这种方法能确保对齐在语义共轭的流形上进行，并防止了奖励黑客现象。同时，它不改变模型参数，而是直接引导模型的生成分布朝向目标奖励。
### Conclusion
Null-TTA不仅在目标测试时间对齐方面达到了最先进的性能，还在跨奖励泛化方面表现优异。这表明语义空间优化是一种有效的、有明确原理的新范式，用于测试时对齐。
## 738. `cs.LG` - Length-MAX Tokenizer for Language Models [PDF](https://arxiv.org/pdf/2511.20849), [HTML](https://arxiv.org/abs/2511.20849)
### Authors
Dong Dong,Weijie Su
### Background
当前的语言模型使用分词器（如BPE）来将文本分割成较小的标记，以提高训练效率和模型性能。然而，这些方法主要关注标记出现的频率，在平均标记长度优化方面缺乏考虑。
### Innovation
该研究提出了一种新的分词器——Length-MAX tokenizer，它通过最大化带长度权重的目标并在图划分问题中求解来构建贪心近似算法，使得平均每个字符的标记数最小化。该方法在不同词汇量下（10K到50K）和不同领域（FineWeb）的表现优于BPE，包括在GPT-2模型中减少了训练步骤和推理延迟，并提高了下游任务的性能，如降低了LAMBADA困惑度和增强了HellaSwag准确性。
### Conclusion
Length-MAX tokenizer在优化平均标记长度方面提供了比仅优化频率更有效的语言建模方法，并且在保持或改善下游任务性能的同时减少了内存使用和提高吞吐量。
## 739. `cs.LG` - 绕过读出瓶颈的残差混合量子-经典模型 [PDF](https://arxiv.org/pdf/2511.20922), [HTML](https://arxiv.org/abs/2511.20922)
### Authors
Guilin Zhang,Wulan Guo,Ziqi Tan,Hongyang He,Hailong Jiang
### Background
量子机器学习（QML）具有紧凑且表达力强的特性，但受到测量瓶颈的限制，即从量子到经典世界的狭窄读出，这限制了性能并放大了隐私风险。
### Innovation
提出了一种轻量级的残差混合架构，该架构在分类前将量子特征与原始输入连接起来，跳过测量瓶颈而不增加量子复杂性。实验表明，该模型在中央和联邦设置下都优于纯量子和先前的混合模型。它在量子基线上的准确率最高可提高55%，同时保持较低的通信成本和增强的隐私鲁棒性。消融研究证实了在量子-经典界面处残差连接的有效性。
### Conclusion
该方法为将量子模型集成到如联邦边缘学习等隐私敏感、资源受限的环境中提供了一条实用且短期内可行的道路。
## 740. `cs.LG` - 基于噪声假设检验的特征选择技术：噪声战胜特征 [PDF](https://arxiv.org/pdf/2511.20851), [HTML](https://arxiv.org/abs/2511.20851)
### Authors
Mousam Sinha,Tirtha Sarathi Ghosh,Ridam Pal
### Background
特征选择在机器学习和人工智能中一直是一项艰巨的挑战，面对越来越复杂和高维的数据集，需要有原则性的策略来提取最有信息量的预测变量。尽管许多已有的技术被广泛应用，但它们仍然存在诸多限制。某些方法计算成本高，而另一些方法缺乏明确的统计驱动停止准则，或者评估其重要性得分的显著性。一种常见的启发式方法引入多个随机噪声特征并保留所有高于最强噪声特征的重要性的预测变量。尽管直观，但这种方法缺乏理论依据，并且高度依赖于启发式方法。本研究提出了一个新颖的特征选择方法以解决上述问题。
### Innovation
本文提出了一种新的特征选择方法，该方法通过非参数Bootstrap假设检验框架来评估每个特征的重要性，并且基于这些噪声特征的最大重要值进行比较，从而为这种方法提供了坚实的理论基础。通过统计推导阐明了该算法的设计原则，并通过在受控统计环境下生成的模拟数据集验证其可靠性，其性能优于Boruta和Knockoff方法。在不同现实世界数据集的应用中，该技术也超越了诸如Boruta、RFE和Extra Trees等特征选择技术，验证了方法的有效性和实用性。
### Conclusion
由此，该方法成为一个稳健的算法，用于进行原则性的特征选择，能够提取支持可靠推断、提升预测性能和高效计算的信息型预测变量。
## 741. `cs.LG` - MODEST: 多光学景深立体数据集 [PDF](https://arxiv.org/pdf/2511.20853), [HTML](https://arxiv.org/abs/2511.20853)
### Authors
Nisarg K. Trivedi,Vinayak A. Belludi,Li-Yun Wang,Pardis Taghavi,Dante Lok
### Background
相机视觉系统如自主机器人和增强现实中，在真实光学条件下可靠的深度估计仍然是一个核心挑战。尽管在深度估计和景深渲染方面取得了一定进展，但研究仍受限于缺乏大规模、高保真度的真实双目电影单反相机数据集，这限制了基于合成数据训练的模型在现实世界中的泛化和评估能力。
### Innovation
本文提出了第一个高分辨率（5472×3648 像素）的双目电影单反相机数据集，包含18000张图像，系统地在复杂的真实场景中变化焦距和光圈，捕捉专业相机系统的光学现实性和复杂性。9个场景包含不同复杂性、照明和背景，以两个相同的相机组合拍摄从28至70毫米10种焦距和f/2.8至f/22的5种光圈，共有50种光学配置。完整的光学范围覆盖使得可以从单一和立体深度估计、浅景深渲染、去模糊、3D场景重构和新颖视图合成中进行受控分析。该数据集包含挑战性视觉元素，如多尺度光学错觉、反射表面、镜子、透明玻璃壁、精细细节和自然/人造环境光变化，从而在合成训练数据和真实相机光学之间建立现实差距，并展示了当前最先进的单目、立体深度和景深方法的挑战。
### Conclusion
该工作旨在释放数据集、校准文件和评估代码，以支持真实光学通用性研究的可重复性。
## 742. `cs.LG` - BUSTR: 使用描述感知视觉语言模型的乳腺超声文本报告 [PDF](https://arxiv.org/pdf/2511.20956), [HTML](https://arxiv.org/abs/2511.20956)
### Authors
Rawa Mohammed,Mina Attin,Bryar Shareef
### Background
乳腺超声（BUS）的自动报告生成（RRG）受到缺乏成像-报告配对数据集和大型语言模型风险的影响。现有方法依赖于成像-报告配对数据集，但在数据稀缺和质量差异问题上存在限制，并且大型语言模型存在生成错误信息的风险。
### Innovation
提出BUSTR，一种多任务视觉-语言框架，无需成像-报告配对监督即可生成BUS报告。BUSTR通过结构化描述符（例如，BI-RADS、病理、组织学）和 radiomics 特征生成报告，使用多头Swin编码器在特定描述符集上使用多任务损失进行训练，学习描述符感知的视觉表示，并通过结合输入和输出表示的令牌级别交叉熵与余弦相似度对齐损失来对齐视觉和文本令牌。
### Conclusion
BUSTR在两个公开的BUS数据集BrEaST和BUS-BRA上表现出色，无论是在标准自然语言生成指标还是临床有效性指标上都取得了显著改进，特别是在BI-RADS分类和病理等关键目标上。结果表明，该描述符感知视觉模型使用结合的令牌级别和对齐损失进行训练，提高了自动报告指标和临床有效性，而不必依赖成像-报告配对数据。
## 743. `cs.LG` - 基于独立策略梯度的强化学习方法在多微网系统经济可靠能源管理中的应用 [PDF](https://arxiv.org/pdf/2511.20977), [HTML](https://arxiv.org/abs/2511.20977)
### Authors
Junkai Hu,Li Xia
### Background
在包含间歇性和分布式可再生能源的多微网系统（MMSs）中，能源管理的效率和可靠性至关重要。本文在分布式方案下探讨了MMSs中能源管理的经济性和可靠性问题，每个微网独立更新其能源管理策略以实现系统的长期优化。
### Innovation
提出了一种基于独立策略梯度的强化学习算法用于解决均值-方差团队随机游戏（MV-TSG）；在已知模型参数情况下，开发了一种全分布式独立策略梯度算法；在未知模型参数情况下，还提出了一种基于独立策略梯度的深度强化学习算法，以实现数据驱动策略优化。
### Conclusion
数值实验验证了所提出方法的有效性，能够在充分利用MMSs的分布式计算能力的同时实现经济性能和操作可靠性的良好平衡。
## 744. `cs.LG` - 经典和量子核的融合实现准确且稳健的两样本检验 [PDF](https://arxiv.org/pdf/2511.20941), [HTML](https://arxiv.org/abs/2511.20941)
### Authors
Yu Terada,Yugo Ogio,Ken Arai,Hiroyuki Tezuka,Yu Tanaka
### Background
两样本检验已被广泛应用于药物效果评估、不同营销策略的A/B测试等各个科学领域和机器学习中，用于判断两组样本是否来自同一分布。基于核函数的检验方法通过将数据映射到再生核希尔伯特空间，能够高效地分离高维复杂结构，以无模型的方式获得准确结果。然而，核的选择对于其性能至关重要，尤其是在小数据集的情况下，如何选择核知之甚少。
### Innovation
文中提出了一个名为MMD-FUSE的假设检验方法，通过结合经典核和量子核，解决了小样本数据检验问题。该方法引入了量子核，提出了基于最大均值差异的混合测试策略，增强了MMD-FUSE框架，使得测试更加强大且适应性强。实验结果显示，通过合适的超参数调优，MMD-FUSE在小样本和高维数据中表现更为优越，并且在不同场景下具有较强的鲁棒性。
### Conclusion
研究表明，量子启发和混合核策略有可能构建更有效的统计检验方法，为样本量有限的数据分析提供了强有力的工具。
## 745. `cs.LG` - 在基于体素的点云网络中加速稀疏卷积 [PDF](https://arxiv.org/pdf/2511.20834), [HTML](https://arxiv.org/abs/2511.20834)
### Authors
Dionysios Adamopoulos,Anastasia Poulopoulou,Georgios Goumas,Christina Giannoula
### Background
稀疏卷积(SpC)在自动驾驶和AR/VR的3D点云网络中应用广泛。然而，之前的SpC引擎在构建内核映射时存在预处理和后处理开销过高的问题。点云体素坐标具有三个关键特性：它们是整数值，局限于有限的空间范围内，并且在几何上连续相邻。体素相邻点之间通常具有小的空间偏移量。
### Innovation
本文设计了Spira，这是一种用于GPU的体素属性意识稀疏卷积引擎，提出了：(i) 高性能的一站式搜索算法，无需预处理且具有高内存局部性；(ii) 有效的高效打包加工方案，以低成本访问打包体素坐标；(iii) 灵活的双数据流执行机制，可根据层特性高效计算输出特征向量；(iv) 网络级并行化策略，在网络启动时并发构建所有稀疏卷积层的内核映射。
### Conclusion
评估表明，Spira在端到端推理性能上比之前的方法平均速度快1.71倍，最多可提高2.31倍；在不同层数配置下的层级执行性能上，平均速度快2.13倍，最多可提高3.32倍。
## 746. `cs.LG` - 波前约束的被动遮挡目标检测 [PDF](https://arxiv.org/pdf/2511.20991), [HTML](https://arxiv.org/abs/2511.20991)
### Authors
Zhiwen Zheng,Yiwei Ouyang,Zhao Huang,Tao Zhang,Xiaoshuai Zhang,Huiyu Zhou,Wenwen Tang,Shaowei Jiang,Jin Liu,Xingru Huang
### Background
准确地从远场光斑中定位和分割被遮挡的物体，尤其是在微弱光线下，由于多次散射和介质引起的扰动，是一项高度挑战的任务。现有的大部分方法依赖于实值建模或局部卷积操作，无法有效捕捉相干光传播的物理原理。在信号噪声比低的情况下，这些方法往往会收敛到非物理的解决方案，严重影响了观测的稳定性和可靠性。
### Innovation
本文提出了一种新的物理驱动的波前传播补偿网络（WavePCNet），用于模拟波前传播并增强对被遮挡物体的感知。WavePCNet 结合了三相波前复杂的折射再投影（TriWCP）以纳入复杂的振幅转移算子，从而精确控制相干传播行为，并加入动量记忆机制来有效抑制扰动的累积。此外，引入了高频率跨层补偿增强，构建了多尺度感受野的选择性路径，并动态建模跨层的结构一致性，从而在复杂环境条件下增强模型的鲁棒性和可解释性。
### Conclusion
在四个物理收集的数据集上的广泛实验表明，WavePCNet 在准确性和鲁棒性上均优于最先进的方法。
## 747. `cs.LG` - 在上下文学习中语义锚点：为什么小规模LLM无法翻转标签 [PDF](https://arxiv.org/pdf/2511.21038), [HTML](https://arxiv.org/abs/2511.21038)
### Authors
Anantha Padmanaban Krishna Kumar(Boston University)
### Background
文章探讨了上下文学习（ICL）是否可以覆盖预训练的标签语义，或者只是在现有的语义基础上进行修正。研究人员通过将大型语言模型（LLMs）作为提示诱导的分类器，并对比其在自然演示和逆向演示（系统性翻转标签意义）下的行为来回答这个问题。
### Innovation
研究通过将ICL行为分解为真实性、先验性和提示对齐度量，并引入语义覆盖率来定义在翻转语义下的正确性，从而提出了系统的理论框架。实验涵盖八项分类任务和八个开源LLM（参数量从1B到12B），验证了语义锚点的观点，揭示了有限提示提示的有效性和限制。
### Conclusion
研究发现，自然演示下ICL既能提高准确率又能保持强先验对齐；而逆向演示下模型无法学到连贯的反向语义分类器，准确率和提示对齐度量之间只能做出权衡，语义覆盖率保持为零。研究表明ICL主要调整了输入如何投影到预训练中学习到的稳定语义方向上，且在这些规模上翻转标签语义需要超出了ICL的干预。
## 748. `cs.LG` - 即便有AI，双射发现仍然困难：OpenEvolve在新型双射构建中的机遇与挑战 [PDF](https://arxiv.org/pdf/2511.20987), [HTML](https://arxiv.org/abs/2511.20987)
### Authors
Davis Brown,Jesse He,Helen Jenne,Henry Kvinge,Max Vargas
### Background
目前，诸如AlphaEvolve、OpenEvolve和ShinkaEvolve等进化程序合成系统为AI辅助的数学发现提供了一种新方法。这些系统利用大量语言模型（LLMs）生成可读性高的候选解决方案，并通过进化过程改进这些解决方案。与现有的大部分数学应用程序主要关注于确定界限（例如，球心填充）不同，程序合成方法适用于任何可以通过具体构造找到解决方案的问题。基于此，本文探讨了使用OpenEvolve进行组合双射发现的应用。
### Innovation
本文特别关注利用OpenEvolve解决组合双射问题。作者尝试了三个双射构造问题，其中两个已知，一个未解决。研究结果表明，虽然像OpenEvolve这样的系统作为组合数学家的有力工具具有潜力，但发现新的研究级别双射仍然是一项具有挑战性的任务，强调了需要在当前的技术前沿中保留人类数学家的角色。
### Conclusion
文章总结了OpenEvolve在新型双射发现中的应用经验，认为尽管人工智能工具具有潜力，但在发现新的、研究级别的双射方面仍然存在挑战，强调了人类数学家在这一过程中的重要性。同时，文章也为其他研究人员在探索这些系统时提供了有益的教训。
## 749. `cs.LG` - 开放词汇量组成解释在神经元对齐中的应用 [PDF](https://arxiv.org/pdf/2511.20931), [HTML](https://arxiv.org/abs/2511.20931)
### Authors
Biagio La Rosa,Leilani H. Gilpin
### Background
神经元是深度神经网络的基本构建块，它们的相互连接使得人工智能能够实现前所未有的成果。旨在理解神经元如何编码信息，组成解释利用概念间的逻辑关系来表达神经元激活和人类知识之间的空间对齐，但这些解释依赖于由人类标注的数据集，这限制了它们在特定领域的应用和预设概念上的适用性。
### Innovation
本文通过提出一种框架，使用户能够为任意概念和数据集探查神经元，突破了先前依赖于人类标注数据集的限制。该框架利用开放词汇量语义分割生成的遮罩来计算开放词汇量组成的解释。该框架分为三步：指定任意概念、使用开放词汇量模型生成语义分割遮罩以及从这些遮罩中推导出组成解释。
### Conclusion
该论文通过与先前方法在量化指标和人类可解释性方面的比较，展示了所提出框架的优势。还分析了从人类标注数据转移到模型标注数据时解释的差异，并展示了框架提供的灵活性，使其能够根据不同任务和需要的关注属性进行调整。
## 750. `cs.LG` - 使用柯尔莫哥洛夫-阿诺尔德网络头微调提升缅甸新闻分类 [PDF](https://arxiv.org/pdf/2511.21081), [HTML](https://arxiv.org/abs/2511.21081)
### Authors
Thura Aung,Eaint Kay Khaing Kyaw,Ye Kyaw Thu,Thazin Myint Oo,Thepchai Supnithi
### Background
在资源有限的语言如缅甸语中，分类任务通常只微调最终分类层，而固定预训练编码器权重。虽然多层感知机（MLPs）广为使用，但其固定的非线性可能限制了表达能力和增加了计算成本。
### Innovation
该工作探索了柯尔莫哥洛夫-阿诺尔德网络（KANs）作为替代分类头部，并评估了基于Fourier的FourierKAN、基于样条的EfficientKAN以及基于网格的FasterKAN，这些在TF-IDF、fastText和多语言变压器（mBERT、Distil-mBERT）等不同嵌入中进行比较。
### Conclusion
KAN基础头部在多个实验中与MLPs竞争或优于MLPs，EfficientKAN使用fastText获得最高F1分数（0.928），而FasterKAN提供了良好的速度和准确性的权衡。在变压器嵌入中，EfficientKAN在mBERT上匹配或略微超过了MLPs（F1为0.917）。因此，KANs证明是低资源语言分类中的具有表达能力和效率的MLP替代品。
## 751. `cs.LG` - 基于冲击回波信号和神经网络的混凝土板完整性数据驱动评估 [PDF](https://arxiv.org/pdf/2511.21080), [HTML](https://arxiv.org/abs/2511.21080)
### Authors
Yeswanth Ravichandran,Duoduo Liao,Charan Teja Kurakula
### Background
混凝土桥面的深层缺陷如分层、空洞和蜂窝状结构严重影响其耐久性，但当前通过视觉检查或人工敲击难以可靠地检测这些缺陷。本文基于机器学习的冲击回波（IE）框架，实现了缺陷定位和常见混凝土缺陷的多类别分类自动化。通过快速傅里叶变换（FFT）将原始IE信号转换为主要频峰特征，并在空间地图中可视化缺陷区域。使用无监督k-means聚类和从实验室缺陷中导出的真实掩模（GTM）来验证空间精度并生成高置信度的训练标签。
### Innovation
提出了基于机器学习的冲击回波框架，它自动化了缺陷定位和多类别分类过程。框架中包括使用快速傅里叶变换处理信号、无监督聚类、使用热度图识别低频缺陷区域、利用实验室验证后的区域构建空间有序频峰序列并将这些序列输入堆叠长短期记忆网络模型以实现混凝土缺陷的分类。模型在实验室数据上训练，并在实际桥梁板上进行现场验证，展示了其实用性和泛化能力。
### Conclusion
提出的框架增强了非破坏性评估（NDE）的客观性、可扩展性和重复性，支持大规模桥梁健康监测的数据驱动智能监控。
## 752. `cs.LG` - 在残差指令传递、对齐微调和任务特定路由的领域适配预训练：MortgageLLM [PDF](https://arxiv.org/pdf/2511.21101), [HTML](https://arxiv.org/abs/2511.21101)
### Authors
Manish Jain,Satheesh Kumar Ponnambalam,Salman Faroz,Chandrakanth Lns,Vinay Sharma
### Background
大型语言模型（LLMs）在通用领域表现出色，但在应用于专业领域（如抵押贷款金融）时，需要增强其领域特定知识同时保持指令遵循的一致性。现有方法通常采用单一多任务模型，但在优化结构化任务时会影响对话一致性，反之亦然。为此，该研究提出了MortgageLLM，一种通过双轨道专业化框架从单一基模型（LLaMA-3.1-8B）开发的新型领域特定大语言模型。
### Innovation
该研究贡献了：（1）将残差技术应用于高度专业化的抵押贷款金融领域；（2）结合对话问答模型和结构化任务模型（用于分类和总结）的双专家架构；（3）通过其中一个专家模型自身执行少量分类的智能任务路由机制。该方法在领域特定基准上的最终模型（MortgageLLM v2）在LLM作为裁决的总结得分、问答得分和分类得分上分别达到了4.58（高于基线LLaMA-3.1-8B-Instruct的3.99）、4.09（高于基线的4.0）和2.6（高于基线的1.2），并在语义相似度上分别取得了0.77的BERTScore（高于基线的0.74）、0.68的问答分数（高于基线的0.58）和0.75的分类分数（高于基线的0.73），显著优于基线方法。
### Conclusion
通过双轨道专业化框架，MortgageLLM成功地解决了在保持指令遵循一致性的同时优化结构化任务的关键挑战，并且在多个领域特定任务上的性能显著优于基线模型，为其他专业领域的LLM应用提供了参考和改进方法。
## 753. `cs.LG` - 神经元的绝对最优组合解释 [PDF](https://arxiv.org/pdf/2511.20934), [HTML](https://arxiv.org/abs/2511.20934)
### Authors
Biagio La Rosa,Leilani H. Gilpin
### Background
神经元是深度神经网络的基本单位，但尚不清楚它们学习了什么内容，以及它们的知识是否与人类的知识一致。组合性解释试图通过逻辑规则描述神经元激活与概念的空间对齐，通常通过所有可能的概念组合搜索来计算这些逻辑描述，但计算整个状态空间范围的空间对齐是不可行的，因此文献中常采用束搜索来限制空间范围。然而，束搜索无法提供任何最优性的理论保证，目前尚不清楚当前的解释与真实最优值之间的距离。
### Innovation
本文通过引入计算组合最优解释的第一个框架，解决了这一问题。具体来说，本文提出了三种方法：(i) 确定影响空间对齐的因素的分解；(ii) 估计任一搜索阶段对齐程度的启发式方法；(iii) 第一个可在可行时间内计算最优组合解释的算法。通过这一框架，本文分析了在流行的应用场景（计算机视觉领域和卷积神经网络）中，束搜索获得的解释中有10-40％是次优的当涉及重叠概念时。最后，通过由本文提出的拆分和启发式方法指导的束搜索变种进行评估，结果表明这一方法在运行时间上能达到或超越先前方法，并且具有更大的超参数灵活性和计算资源的选择性。
### Conclusion
本文提出了一种新的框架，能够计算出绝对最优的组合解释，揭示了束搜索在某些情况下可能产生的次优解释，并展示了一种改进的束搜索方法，该方法在保持算法灵活性的同时减少了计算时间。
## 754. `cs.LG` - 通过5万美元的Kaggle竞赛推动前沿：改进混合物理-机器学习气候模拟 [PDF](https://arxiv.org/pdf/2511.20963), [HTML](https://arxiv.org/abs/2511.20963)
### Authors
Jerry Lin,Zeyuan Hu,Tom Beucler,Katherine Frields,Hannah Christensen,Walter Hannah,Helge Heuer,Peter Ukkonnen,Laura A. Mansfield,Tian Zheng,Liran Peng,Ritwik Gupta,Pierre Gentine,Yusef Al-Naher,Mingjiang Duan,Kyo Hattori,Weiliang Ji,Chunhan Li,Kippei Matsuda,Naoki Murakami,Shlomo Ron,Marec Serlin,Hongjian Song,Yuma Tanabe,Daisuke Yamamoto,Jianyao Zhou,Mike Pritchard
### Background
亚网格机器学习（ML）参数化有潜力引入新一代气候模型，这些模型能够纳入更高分辨率物理效应而不引发更贵的计算成本。然而，从在线不稳定到在线性能不一致等各种关键问题限制了它们在长期气候预测中的应用。为此，研究者们通过开源问题的离线方面并举办Kaggle竞赛，吸引了更广泛的人工智能和数据科学社区参与解决这些问题。结果显示，各种启发式架构在低分辨率实际地理条件下表现出可重复的在线稳定性，这是一个重要的里程碑。
### Innovation
研究通过举办5万美元的Kaggle竞赛，加速了解决亚网格机器学习参数化问题的进程。研究中，使用了来自获胜团队架构的启发式模型，将其耦合到一个包括完整云微物理过程的互动气候模型中，并系统评估了它们的在线性能。多个来自Kaggle竞赛的启发式架构在某些指标上取得了最先进的结果，表明通过外包问题核心可以提高混合物理-人工智能气候模拟的在线性能。
### Conclusion
研究结果表明，在低分辨率的真实地理设置中，各种检测到的架构在在线稳定性方面表现出了可重复性，这是非常关键的里程碑。所有测试的架构在离线和在线偏差方面表现相似，但在设计选择（如扩展输入变量列表）方面可能会有显著差异。这种方法表明，通过外包问题核心，可以改进混合物理-人工智能气候模拟的在线性能。
## 755. `cs.LG` - RosettaSpeech: 仅靠单语数据的零样本语音到语音翻译 [PDF](https://arxiv.org/pdf/2511.20974), [HTML](https://arxiv.org/abs/2511.20974)
### Authors
Zhisheng Zheng,Xiaohang Sun,Tuan Dinh,Abhishek Yanamandra,Abhinav Jain,Zhu Liu,Sunil Hadap,Vimal Bhat,Manoj Aggarwal,Gerard Medioni,David Harwath
### Background
平行语音语料库的稀缺严重阻碍了语音到语音翻译（S2ST）的发展，通常需要依赖复杂的多阶段流水线。现有方法需要平行的语音到语音样本对进行训练，但这种数据的获取成本高昂且难以获得。
### Innovation
提出了RosettaSpeech，这是一种新颖且简化的零样本语音到语音翻译（S2ST）框架，该框架通过利用机器翻译的监督信息在单语语音-文本数据上进行训练。该方法利用了基于文本的神经机器翻译（NMT）模型中的语言知识，并提出了一个具有文本作为训练期间中介桥梁的独特方法，但在推理时能够直接处理语音到语音的任务。这种方法在标准基准测试上达到了最先进的性能。
### Conclusion
RosettaSpeech能够通过优先依赖大量并行文本数据而不是难以获取的并行语音数据，提供了一条可行的路径来创建高质量、保发言者性的语音到语音翻译系统，并适用于更多语言。在CVSS-C测试集上，RosettaSpeech的德语到英语和西班牙语到英语的ASR-BLEU得分分别为25.17和29.86，分别取得了27%和14%的相对提升。此外，还展示了单个模型的多对一翻译性能（法语/西班牙语/德语 -> 英语）。
## 756. `cs.LG` - 基于几何校准和不确定性的多类别分类中的中性区域 [PDF](https://arxiv.org/pdf/2511.20960), [HTML](https://arxiv.org/abs/2511.20960)
### Authors
Soumojit Das,Nairanjana Dasgupta,Prashanta Dutta
### Background
现代人工智能系统在做出关键决策时经常因不确定而静默失败。本文构建了一个几何框架，用于后处理校准神经网络的概率输出，考虑到概率向量作为Fisher--Rao度量下的(c-1)维概率单纯形上的点。现有的校准方法缺乏泛化原则，本文提出的方法弥补了这一缺陷。
### Innovation
本文提出了基于Additive Log-Ratio (ALR) 校准映射的方法，该方法在二分类问题下等同于Platt校准，在多分类问题下自然扩展。此外，定义了基于Fisher--Rao距离的几何可靠性得分，并构建了中性区域，为不确定预测提供了原理性的退避策略。理论上的贡献包括：通过M-估计理论证明校准估计器的一致性（以O_p(n^{-1/2}) 的速率），提供了可靠性得分的紧缩收敛性边界并提供了样本大小计算方法。基于此，推测中性区域构造具有Neyman--Pearson最优性。
### Conclusion
本文的工作结合了信息几何和统计学习，为需要严格验证的应用提供了形式保证。实验验证在腺相关病毒分类中显示，两阶段框架（校准后基于可靠性退避）能够捕获72.5%的错误，同时退避34.5%的样本。值得注意的是，这种操作增益可以通过任何校准良好的概率输出实现；几何校准的主要贡献在于其理论基础，而非在复杂度更简单的替代方法上的实证优越性。
## 757. `cs.LG` - 深度学习作为计算的凸模式：ResNets最小化电路大小 [PDF](https://arxiv.org/pdf/2511.20888), [HTML](https://arxiv.org/abs/2511.20888)
### Authors
Arthur Jacot
### Background
本文探讨了深度神经网络（DNNs）在数据拟合中实现的计算奥卡姆剃刀——寻找一个‘最简单’的算法来适应数据——并认为这一点可以解释DNNs在统计传统方法面前的卓越和泛化能力。研究者指出，在‘比蒙特卡洛还要困难’（HTMC）的条件下，可以找到一个使得函数$boldsymbol{f}$能在$boldsymbol{boldsymbol{boldsymbol{boldsymbol{boldsymbol{boldsymbol{boldsymbol{boldsymbol{boldsymbol{boldsymbol{boldsymbol{boldsymbol{boldsymbol{boldsymbol{boldsymbol{beta}}}}}}}}}}}}}}$近似的测度结构，这提供了一种定义HTMC范数的方法。同时，ResNets的参数复杂性可以用加权$boldsymbol{boldsymbol{boldsymbol{boldsymbol{boldsymbol{boldsymbol{boldsymbol{boldsymbol{boldsymbol{boldsymbol{boldsymbol{boldsymbol{boldsymbol{boldsymbol{boldsymbol{boldsymbol{boldsymbol{boldsymbol{boldsymbol{boldsymbol{beta}}}}}}}}}}}}}}}}}}$范数来衡量，从而定义一种对应的ResNet范数。
### Innovation
研究者发现通过HTMC规范和ResNet规范之间的接近匹配的三明治界，可以将ResNet的最小化规范看作是在数据拟合中使用几乎最小节点数的电路。这意味着ResNets可作为实现实函数计算的一种新的模型，特别适合HTMC条件下的凸性。
### Conclusion
研究得出结论，ResNets可以在HTMC条件下提供更有效的电路大小优化，从而解释了深度学习模型在处理复杂数据集时的卓越表现。
## 758. `cs.LG` - DNNs在部分线性模型中的非凸惩罚LAD估计：渐近分析与邻近算法 [PDF](https://arxiv.org/pdf/2511.21115), [HTML](https://arxiv.org/abs/2511.21115)
### Authors
Lechen Feng,Haoran Li,Lucky Li,Xingqiu Zhao
### Background
本文研究了部分线性模型中的最小绝对偏差（LAD）回归，并利用深度神经网络（DNNs）参数化非参数项，形成LAD惩罚问题以进行估计。研究过程中发现了三个主要挑战：一是正则化项可能为非凸和非光滑，这需要引入无穷维变分分析和非光滑分析来讨论渐进正态性。二是随着样本数量增加，网络需要扩展（在宽度、稀疏性和深度上），这为理论研究增加了复杂性。三是所提估计器本身通过超高维、非凸且不连续的优化问题定义，带来了巨大的计算和理论挑战。
### Innovation
本文的主要创新在于：1）利用DNNs参数化非参数部分；2）通过引入无穷维变分分析和非光滑分析解决非凸和非光滑正则化问题；3）研究了扩展示状下的网络结构变化对理论分析的影响；4）分析了所提估计器的稀疏优化问题及其连续松弛形式，研究了邻近梯度方法的收敛性，揭示了不同形式的结构差异导致的计算子问题区别。
### Conclusion
在面临上述挑战的情况下，建立了所提估计器的一致性、收敛速率和渐进正态性。此外，还分析了稀疏优化问题及其连续松弛形式，并研究了邻近梯度方法在两种形式下的收敛性，特别指出松弛形式的邻近更新显著降低成本，反映了统计精确性和计算可处理性之间的固有权衡。
## 759. `cs.LG` - 总热传导率比：一种基于声子玻璃-电子晶体设计的数据驱动热电设计描述符 [PDF](https://arxiv.org/pdf/2511.21213), [HTML](https://arxiv.org/abs/2511.21213)
### Authors
Yifan Sun,Zhi Li,Tetsuya Imamura,Yuji Ohishi,Chris Wolverton,Ken Kurosaki
### Background
热电（TE）材料因其性能用ZT（figure of merit）量化而成为能源捕获的有希望候选者。为了加速具有高ZT材料的发现，研究重点是确定具有低热导率（κ）的化合物。通过使用包含71,913个条目的数据集，本文展示了高ZT材料不仅位于低κ区域，还聚集在大约κL/κ比值约为0.5的区域，这与声子-玻璃-电子-晶体设计概念一致。基于此洞察，构建了一个框架，该框架包括两个机器学习模型，用于热导率的晶格和电子部分，这两个模型一起提供κ和κL/κ以筛选和指导TE材料的优化。
### Innovation
本文构建了一个框架，该框架基于两个机器学习模型来预测热导率的晶格和电子部分，同时提供了总热导率比κL/κ的预测。通过筛选104,567种化合物，模型确定了2,522种超低κ候选物。进一步的案例研究表明，该框架可以可靠地提供优化策略，通过建议新的掺杂剂和合金使纯净材料向κL/κ接近0.5区域转变。该方法将快速筛选与PGEC引导的优化整合起来，有效地弥合了材料发现与性能提升之间的关键差距。
### Conclusion
通过结合快速筛选和PGEC引导的优化，本文提出的数据驱动框架有效地弥合了材料发现与性能增强之间的关键差距。该方法能够在识别具有高ZT的超低κ候选物的同时，提供优化策略，指导热电材料的优化和设计。
## 760. `cs.LG` - 极大型Donsker-Varadhan公式在可能性变分推断中的应用 [PDF](https://arxiv.org/pdf/2511.21223), [HTML](https://arxiv.org/abs/2511.21223)
### Authors
Jasraj Singh,Shelvia Wongso,Jeremie Houssineau,Badr-Eddine Chérief-Abdellatif
### Background
变分推断（VI）是现代贝叶斯学习的基石，可通过高维积分定义的期望和差异来实现复杂模型的近似推断，这种定义通常使得理论分析变得不可能，因此需要依赖近似学习和推断技术。可能性理论作为一种不确定性的非概率建模框架，可以直观地处理稀疏或不精确的信息，但将其适应于可能性设置需要重新思考熵和差异等核心概念，这些概念假定了可加性。
### Innovation
本文发展了一种近年来可能性变分推断的原理性公式，并应用于特定的指数族函数，这揭示了可能性理论的独特数学结构，同时强调了与概率对应概念之间的联系。
### Conclusion
这项工作探索了可能性推断的核心概念，并将其与概率推断进行对比，揭示了可能性理论的数学结构的独特之处，为进一步的应用奠定了基础。
## 761. `cs.LG` - Phase-Aware Code-Aided EM Algorithm for Blind Channel Estimation in PSK-Modulated OFDM [PDF](https://arxiv.org/pdf/2511.21340), [HTML](https://arxiv.org/abs/2511.21340)
### Authors
Chin-Hung Chen,Ivana Nikoloska,Wim van Houtum,Yan Wu,Alex Alvarado
### Background
在正交频分复用(OFDM)系统中使用PSK调制时，盲信道估计的代价函数EM算法普遍存在局部最优问题。这是由于信道估计中的相位不确定性造成的，而传统的盲EM估计器无法解决这一问题。
### Innovation
提出了一种适应相位感知的基于解码器外部信息的编码辅助期望-最大化(EM)算法。该算法通过生成基于PSK调制固有对称性的候选模型集，并由解码器选择最有可能的候选模型，来克服常规EM估计器的限制。
### Conclusion
结合简单 convolutional 码后，适应相位感知的EM算法在频率选择性通道中的初始化阶段能够可靠地解决相位不确定性，将局部收敛率从80%降低到几乎0%，且在随后的turbo迭代中仅需一次调用，不会增加额外的复杂度。
## 763. `cs.LG` - 使用音素特征增强变换器进行低资源掸族自动语音识别错误纠正 [PDF](https://arxiv.org/pdf/2511.21088), [HTML](https://arxiv.org/abs/2511.21088)
### Authors
Ye Bhone Lin,Thura Aung,Ye Kyaw Thu,Thazin Myint Oo
### Background
本文研究了序列到序列的Transformer模型在低资源掸族自动语音识别（ASR）错误纠正中的应用，重点是不同的特征整合策略，包括国际音标（IPA）和对齐信息。到目前为止，这是第一个专门针对掸族的ASR错误纠正研究。研究了五个ASR骨干模型，并展示了提出的ASR错误纠正（AEC）方法在单词级和字符级准确度方面相对于基线输出的一致改进。集成IPA和对齐特征的AEC模型在未增强的情况下将ASR模型的平均WER从51.56降低到39.82，增强后降低到43.59，chrF++分数从0.5864提高到0.627，证明了相对于未使用AEC的基线ASR输出的一致改进。
### Innovation
本文首次针对掸族进行了ASR错误纠正研究，引入了使用音素特征和对齐信息的增强Transformer模型，展示了在单词级、字符级准确度和chrF++分数上的显著提升。
### Conclusion
研究结果表明ASR错误纠正的鲁棒性和特征设计对于改进低资源环境下的ASR输出的重要性。
## 764. `cs.LG` - 测试时计算量对视觉语言模型推理能力的影响：基于干扰项的经验分析 [PDF](https://arxiv.org/pdf/2511.21397), [HTML](https://arxiv.org/abs/2511.21397)
### Authors
Jiyun Bae,Hyunjong Ok,Sangwoo Mo,Jaeho Lee
### Background
研究发现，语言模型中的文本干扰信息会导致较长但效率较低的推理。为了探究这种现象是否也存在于视觉-语言模型的多模态环境中，作者提出了一个名为Idis的数据集，该数据集系统地在语义、数字和空间维度上改变了干扰信息。研究揭示了视觉干扰信息与文本干扰信息的根本不同：尽管逆向缩放现象仍然存在，但添加视觉干扰信息会降低准确率而不增加推理长度。
### Innovation
作者引入了一个名为Idis的新数据集，这是一个视觉问答数据集，系统性地将干扰信息沿语义、数值和空间维度变化。研究进一步展示了跟踪推理轨迹中属性计数提供了有关干扰信息、推理长度和准确率互动的关键见解。此外，作者还展示了这些趋势扩展到现有的视觉偏置基准测试，如Waterbirds，并提出了一种简单的提示策略来减轻推理模型驱动的偏见预测。
### Conclusion
研究发现，视觉干扰信息与文本干扰信息在影响推理时间与准确率方面存在根本差异。尽管逆向缩放现象依旧存在，但添加视觉干扰信息会降低准确率而不会增加推理长度。作者还提出了一种简单的提示策略来减轻基于干扰信息的模型预测偏见。
## 765. `cs.LG` - 学习更高阶网络中的多阶块结构 [PDF](https://arxiv.org/pdf/2511.21350), [HTML](https://arxiv.org/abs/2511.21350)
### Authors
Kazuki Nakajima,Yuya Sasaki,Takeaki Uno,Masaki Aida
### Background
更高阶网络因能自然描述超图而成为刻画现实系统中三者或多者相互作用的核心工具。现有计算机模型，如卷积块模型，为表征中间尺度组织提供了规范框架，但将其拓展到超图时涉及表达能力和计算复杂性的权衡。一种近期简化方法，即单阶模型，通过假设单一的亲和力模式控制所有阶的互动来降低复杂性，但这可能忽略了阶相关结构细节。
### Innovation
本文提出了一种框架，引入了多阶块结构，其中不同亲和力模式分别控制不同的互动阶的子集合。该框架基于多阶卷积块模型，并旨在通过最大化脱机超链接预测性能来寻找交互阶最优划分。实验结果表明，此类结构在多种实际网络中普遍存在，采用它们不仅能提升相对于单阶模型的预测性能，还能揭示更清晰、更易于理解的中间尺度组织。
### Conclusion
研究发现阶依赖机制是现实世界更高阶网络中间尺度组织的关键特征。
## 766. `cs.LG` - 可微物理学-神经网络模型使非马尔可夫闭合学习加速的粗粒度物理模拟 [PDF](https://arxiv.org/pdf/2511.21369), [HTML](https://arxiv.org/abs/2511.21369)
### Authors
Tingkai Xue,Chin Chun Ooi,Zhengwei Ge,Fong Yew Leong,Hongying Li,Chang Wei Kang
### Background
数值模拟在解析现实世界中的许多物理问题方面提供了关键见解，但大多数分析只需要较小维度的数据。通常，这些模拟使用完整三维域求解，但在实际应用中，只关注减少的度量标准（例如平面浓度）。因此，如何快速准确地模拟复杂域中的标量传输成为研究的重点。
### Innovation
该研究提出了一种混合物理学-神经网络模型，能够在一个复杂域中以比三维模拟快数个数量级的速度预测标量传输（从几小时到不到1分钟）。该端到端可微框架联合学习物理模型参数化（即各向异性扩散率）和非马尔可夫神经闭合模型，以捕捉未解析的、‘粗粒度’效应，从而实现长时间滚动的稳定性。此模型通过仅使用26个训练数据实现了高效学习，并灵活扩展到离散分布场景（移动源），最终模拟时间的Spearman相关系数达到0.96。
### Conclusion
总体结果表明，不同可微物理学-神经网络框架能够快速、准确且通用地提供物理现象的粗糙粒度代理模型。
## 767. `cs.LG` - 大型语言模型中模型合并技术的系统研究 [PDF](https://arxiv.org/pdf/2511.21437), [HTML](https://arxiv.org/abs/2511.21437)
### Authors
Oğuz Kağan Hitit,Leander Girrbach,Zeynep Akata
### Background
模型合并技术可以通过合并多个微调模型的检查点，来生成一个单一的模型，而不需要额外的训练，这个方法不仅可以提高模型性能，还可以促进模型的重用。但是，目前还不清楚这种技术在小型模型和分类器中报告的优势是否也能在大规模语言模型（LLMs）中得到体现。
### Innovation
该研究对六种最先进的模型合并方法进行了大规模、系统性的评估，涉及四种开源权重的大规模语言模型、12个每个基模型的微调检查点以及16个标准的大规模语言模型基准测试。研究结果表明，唯一可以在LLMs中可靠提升性能的方法是古老的Task Arithmetic。其他方法通常会导致显著的性能下降。
### Conclusion
研究表明目前的合并技术在现代大规模语言模型中并不可靠。因此，需要设计为特定于大规模语言模型的合并算法以及合并敏感的微调方法。
## 768. `cs.LG` - 基于RISC-V的TinyML加速器用于边缘AI中的深度可分离卷积 [PDF](https://arxiv.org/pdf/2511.21232), [HTML](https://arxiv.org/abs/2511.21232)
### Authors
Muhammed Yildirim,Ozcan Ozturk
### Background
边缘AI和TinyML应用中对设备端智能的需求增长，需要高效执行现代卷积神经网络(CNNs)。尽管像MobileNetV2这样的轻量级架构使用深度可分离卷积(DSC)来降低计算复杂度，但其多阶段设计在逐层执行时引入了关键性能瓶颈，即中间特征图传输到大片内缓存或外部DRAM的成本高昂，导致高能耗和延迟。为解决这一内存墙问题，本文提出了一种新型硬件加速器架构，利用融合像素级数据流。该架构在RISC-V处理器中通过自定义函数单元(CFU)实现，完全消除中间缓冲的需求，将数据流通过紧密耦合管道传输，避免写入内存，从而减少数据移动高达87%。在Xilinx Artix-7 FPGA上设计实现，相比RISC-V核心上的基准软件执行，加速比达59.3倍。
### Innovation
提出了基于RISC-V的新型硬件加速器架构，通过自定义函数单元(CFU)实现融合像素级数据流，完全消除中间缓冲的需求，避免写入内存，将数据流通过紧密耦合管道传输，减轻了内存墙带来的性能瓶颈。通过在Xilinx Artix-7 FPGA上实现的评估中，相比RISC-V核心上的基准软件执行，达到59.3倍的加速比。进一步的ASIC合成结果表明，该设计在20纳米工艺下的面积为0.284 mm²，功耗为910 mW，在2 GHz频率下；在40纳米工艺下的面积为1.20 mm²，功耗为233 mW，在300 MHz频率下，证实了零缓冲数据流在TinyML资源环境中的可行性。
### Conclusion
该工作确认了零缓冲数据流在TinyML资源环境中的可行性，提供了一种新颖且有效的方法来克服边缘AI加速器中的内存墙问题。
## 769. `cs.LG` - Merge and Bound: Direct Manipulations on Weights for Class Incremental Learning [PDF](https://arxiv.org/pdf/2511.21490), [HTML](https://arxiv.org/abs/2511.21490)
### Authors
Taehoon Kim,Donghwan Jang,Bohyung Han
### Background
类增量学习（Class Incremental Learning，CIL）是机器学习中的一个重要问题，旨在使模型能够随着更多类别的加入而逐步学习和适应，而不遗忘之前学到的知识。现有方法往往通过修改模型架构或调整学习目标来处理这一问题，但这种方法可能会带来复杂性增加和效果不佳的问题。
### Innovation
作者提出了一种名为Merge-and-Bound（M&B）的新颖训练方法，直接在参数空间上操作模型权重来进行优化。该方法包括两种类型的权重合并：任务间权重合并和任务内权重合并。此外，还提出了一种有界更新技术，以最小化累积更新并保留先前任务的知识。这种方法能够有效地获取新模型，减少灾难性遗忘。
### Conclusion
M&B方法无缝集成到现有的CIL方法中，无需修改架构组件或修订学习目标。在标准CIL基准测试中，该算法的性能优于最先进的方法。
## 770. `cs.LG` - SBM中具有超过√n个社区的相变现象（II） [PDF](https://arxiv.org/pdf/2511.21526), [HTML](https://arxiv.org/abs/2511.21526)
### Authors
Alexandra Carpentier,Christophe Giraud,Nicolas Verzelen
### Background
在随机块模型（SBM）中，一个基本的理论问题是确定在什么条件下可以在多项式时间内进行社区恢复。对于社区数量K小于√n的情况，社区恢复在Kesten-Stigum（KS）阈值之上且仅在其之上可以通过统计物理方法获得非平凡的多项式时间恢复。当K≥√n时，Chin等人的研究表明，在稀疏条件下，社区恢复在KS阈值以下可以实现，这促使他们提出了针对多社区条件的新阈值。Carpentier等人证实了在新阈值以下低度多项式失败，并在某些中等稀疏条件下证明了阈值以上的成功恢复，尽管这些结果提供了证据表明在高社区数量设置中，计算障碍对应于Chin等人所提出的阈值，但在大多数密度条件下实现恢复的问题仍然没有解决。
### Innovation
本文继续Carpentier等人的研究，通过构造满足特定结构属性的一组 motif，并证明在提出的阈值以上可以计数此类 motif 实现社区恢复，从而填补了SBM中具有多于√n个社区的相变现象架构。此外，结果表明，在中等稀疏条件下，最优算法似乎与谱方法有着根本的不同。
### Conclusion
我们的研究结果完成了SBM中具有多于√n个社区的计算障碍图片。在中等稀疏条件下，最优化算法似乎与谱方法不同。
## 771. `cs.LG` - Odin: Oriented Dual-module Integration for Text-rich Network Representation Learning [PDF](https://arxiv.org/pdf/2511.21416), [HTML](https://arxiv.org/abs/2511.21416)
### Authors
Kaifeng Hong,Yinglong Zhang,Xiaoying Hong,Xuewen Xia,Xing Xu
### Background
现有的图神经网络（GNNs）由于过光滑问题和依赖跳数的扩散机制受限，而基于变换器（Transformers）的方法则忽略了图拓扑结构，将节点视为孤立序列。因此，文本属性图需要模型能够有效结合强大的文本理解能力和结构性高效的推理。
### Innovation
Odin（Oriented Dual-module INtegration）提出了一个新的架构，在选定的深度中通过有向的双模块将图结构注入到变换器中，而不是依赖多跳扩散，而是将多跳结构集成到特定的变压器层，产生低级、中级和高级的结构性抽象，这些抽象与模型的语义层次结构相一致。此外，Odin通过作用于全局[CLS]表示来避免过光滑问题，并将结构性抽象与邻域大小或图拓扑解耦。为了使设计在大规模或低资源设置下更有效，还引入了Light Odin，这是一种轻量级的变体，保持了相同层对齐的结构性抽象，以实现更快的训练和推理。Odin和Light Odin共同构成了一个无跳结构-文本整合的统一框架。
### Conclusion
实验表明，Odin在多种富含文本信息的图基准测试中达到了最先进的准确性，而Light Odin则以显著降低的计算成本实现了竞争力的性能。Odin和Light Odin一起构成了一个无跳的框架，用于原理上的结构-文本整合。该模型的源代码已经在此处发布：this https URL
## 772. `cs.LG` - 高维线性回归中的估计：Post-Double-Autometrics作为Post-Double-Lasso的替代方法 [PDF](https://arxiv.org/pdf/2511.21257), [HTML](https://arxiv.org/abs/2511.21257)
### Authors
Sullivan Hué,Sébastien Laurent,Ulrich Aiounou,Emmanuel Flachaire
### Background
在许多协变量存在的情况下，当研究目标是准确估计感兴趣的参数，如平均处理效应时，Post-Double-Lasso方法变得很流行。然而，该方法在小样本情况下可能会遭受显著的遗漏变量偏差。为了应对这一问题，研究者提出了一种基于Autometrics的新方法Post-Double-Autometrics，旨在解决小样本偏差问题。
### Innovation
提出了一种基于Autometrics的新方法Post-Double-Autometrics，展示出该方法能比Post-Double-Lasso在小样本情况下表现更好，并对经济增长标准应用中的边际收敛假设提供了新的视角。
### Conclusion
在经济增长的标准应用中，Post-Double-Autometrics比Post-Double-Lasso能提供更准确的估计，更加验证了从贫穷到富裕经济的边际收敛假设，从而给实证研究提供了新的见解。
## 773. `cs.LG` - The Spheres Dataset：用于音乐源分离和信息检索的多轨管弦乐队录音 [PDF](https://arxiv.org/pdf/2511.21247), [HTML](https://arxiv.org/abs/2511.21247)
### Authors
Jaime Garcia-Martinez,David Diaz-Guerra,John Anderson,Ricardo Falcon-Perez,Pablo Cabañas-Molero,Tuomas Virtanen,Julio J. Carabias-Orti,Pedro Vera-Candeas
### Background
该论文介绍了The Spheres数据集，这是一个旨在推进音乐源分离领域以及管弦乐等相关MIR任务在古典音乐领域的机器学习研究的多轨录音集合。该数据集包括在The Spheres录音室录制的Colibrì Ensemble演奏的Tchaikovsky的罗密欧与朱丽叶和莫扎特的第40号交响曲等两部经典作品超过一小时的录音，还包含了每个乐器的音阶和独奏片段。
### Innovation
数据集采用23个麦克风，包括近距离麦克风、主麦克风和环境麦克风，创建了具有良好控制混响的立体声混合，并提供了隔离的音轨以监督训练源分离模型。此外，还估计了每个乐器位置的厅堂脉冲响应，为录音空间提供了重要的声学表征。该数据集通过X-UMX模型进行了管弦乐家族分离和麦克风去混响的基线评估。
### Conclusion
结果突显了在复杂交响乐场景下源分离的潜力和挑战，强调了该数据集在基准测试和探索乐曲分离、定位、去混响和沉浸式渲染等新方法方面的价值。
## 774. `cs.LG` - 从扩散到一步生成：基于流的模型比较研究及其在图像填充中的应用 [PDF](https://arxiv.org/pdf/2511.21215), [HTML](https://arxiv.org/abs/2511.21215)
### Authors
Umang Agarwal,Rudraksh Sangore,Sumit Laddha
### Background
本文研究了三种生成模型：去噪扩散概率模型（DDPM）、条件流配准（CFM）和MeanFlow。这三种模型都依赖于模型结构和生成过程的特点进行比较和研究。文章特别介绍了MeanFlow模型如何可以直接以一步生成的方式工作，而无需像DDPM和CFM那样迭代采样。
### Innovation
本文创新性地将基于流的模型应用到图像填充任务中，并通过不同类型的掩码（中心掩码、随机矩形框掩码、非规则掩码、半掩码）展示了CFM模型增强后的有效性。实验结果显示，使用MeanFlow进行单步生成可以显著减少推断时间，并且在图像填充任务中，通过改进训练能够实现显著性能提升。
### Conclusion
论文通过统一的TinyUNet架构在CIFAR-10数据集上实施三种模型的比较，表明CFM能够以更少的迭代（50步）达到更高的性能（FID为24.15），而MeanFlow则可以在单步生成中实现更快的推断速度（FID为29.15）。此外，改进后的CFM在图像填充任务中显示出显著的提升效果，特别是PSNR提高73%，SSIM提高45%。
## 775. `cs.LG` - MMA: 一种用于惯性传感器的人体活动识别的动量Mamba架构 [PDF](https://arxiv.org/pdf/2511.21550), [HTML](https://arxiv.org/abs/2511.21550)
### Authors
Thai-Khanh Nguyen,Uyen Vo,Tan M. Nguyen,Thieu N. Vo,Trung-Hieu Le,Cuong Pham
### Background
惯性传感器的人体活动识别（HAR）对于无处不在的计算、移动健康和环境智能至关重要。传统的深度模型如卷积神经网络（CNN）、循环神经网络（RNN）和变压器已经提升了HAR的效果，但仍然受到梯度消失或爆炸、高计算成本和难以捕捉长范围依赖性的限制。结构化的状态空间模型（SSM）如Mamba克服了这些挑战，拥有线性复杂度和有效的时序建模能力，但它们受限于一阶动力模型，缺乏稳定的长期记忆机制。
### Innovation
提出了一种增强型的动量Mamba架构（Momentum Mamba），它加入了二阶动力来改善信息在时间步骤间的流动稳定性、鲁棒性以及长序列建模。Complex Momentum Mamba进一步增强了其容量，提供了频率选择性的记忆缩放能力。实验结果显示，在多个HAR基准上，Momentum Mamba和Complex Momentum Mamba在准确率、鲁棒性和收敛速度上均优于普通的Mamba和Transformer基准。与标准Mamba模型相比，增强型SSM仅需适度增加训练成本，提供了一种良好的准确率与效率的平衡，确立了其作为HAR的有效范式，并且有望成为更广泛序列建模应用的主要框架。
### Conclusion
增强型SSM如Momentum Mamba和Complex Momentum Mamba以其良好的准确率与效率平衡，成为HAR的有效范式，并具有在更广泛序列建模应用中的潜力。
## 776. `cs.LG` - 突破超音速湍流领域：将神经拟态方法推进到高非线性超音速区间 [PDF](https://arxiv.org/pdf/2511.21474), [HTML](https://arxiv.org/abs/2511.21474)
### Authors
Fabian Paischer,Leo Cotteleer,Yann Dreze,Richard Kurle,Dylan Rubini,Maurits Bleeker,Tobias Kronlachner,Johannes Brandstetter
### Background
神经拟态方法在汽车空气动力学中的广泛应用，得益于诸如DrivAerML和DrivAerNet++等数据集的支持，主要集中在带有大尾迹的钝体流动。然而，将这些方法扩展到航空航天领域，特别是过渡区，仍然面临着挑战，因为压缩流的高非线性以及3D效应（如翼尖涡）使得这项工作难以进行。现有的航空航天数据集主要侧重于2D翼型，忽略了这些关键的3D现象。鉴于此，本文提出了一种新的数据集，该数据集包括过渡区3D翼片的CFD模拟，样本量约30,000个，包含独特的几何形状和来流条件，提供了气动优化的基础。
### Innovation
本文介绍了新的3D翼片在超音速过渡区的CFD模拟数据集，包含体积和表面水平的30,000个样本，并对几种先进的神经拟态方法（包括Transolver和AB-UPT）进行了评估，特别是在几何形状和来流变化方面进行了异分布外泛化表现。AB-UPT在超音速流场中表现出色，并且可以再现物理上一致的阻力升力帕累托前沿，即使对于未见过的翼型配置也是如此。这项研究的结果表明AB-UPT能够逼近未见过的几何形状的阻力升力帕累托前沿，强调了其作为快速气动设计探索工具的有效性。
### Conclusion
本文的研究结果证明了AB-UPT拟态模型在面对未知几何形状时的潜力，这对于快速气动设计探索具有重要意义。为此，本文开放了新创建的数据集，以供未来研究之用。
## 777. `cs.LG` - 超越URL：高效大语言模型预训练的元数据多样性和位置 [PDF](https://arxiv.org/pdf/2511.21613), [HTML](https://arxiv.org/abs/2511.21613)
### Authors
Dongyang Fan,Diba Hashemi,Sai Praneeth Karimireddy,Martin Jaggi
### Background
将元数据纳入大型语言模型（LLMs）预训练正在成为一种有潜力加速训练的方法。早期的研究只强调了一种有用的数据类型—URL，因此还存在是否其他形式的元数据能够带来更大效益的问题。
### Innovation
本研究探索了更广泛类型的元数据，并发现细粒度的文档质量指标也可以在预训练中通过前缀加入来加速。研究发现有效元数据的一个共同特征是它们以更细粒度编码信息。此外，研究引入了通过预测适当元数据作为辅助任务来提高训练效率的方法，并利用掩蔽损失训练可学习的元标记来恢复部分加速效果，引入了元标记的概念。使用探针分析潜在表示，以更好地理解元数据如何影响学习。
### Conclusion
这些结果为集成元数据以提高LLMs预训练的效率和效果提供了实践指南。
## 778. `cs.LG` - ToolOrchestra：通过高效模型和工具编排提升智能 [PDF](https://arxiv.org/pdf/2511.21689), [HTML](https://arxiv.org/abs/2511.21689)
### Authors
Hongjin Su,Shizhe Diao,Ximing Lu,Mingjie Liu,Jiacheng Xu,Xin Dong,Yonggan Fu,Peter Belcak,Hanrong Ye,Hongxu Yin,Yi Dong,Evelina Bakhturina,Tao Yu,Yejin Choi,Jan Kautz,Pavlo Molchanov
### Background
大型语言模型是强有力的通用者，但在解决人类终极考试（HLE）这类深层次和复杂的问题时，仍然面临概念性挑战和计算成本问题。研究显示，由小型协调器管理其他模型和各种工具可以推动智能上限并提高解决复杂代理任务的效率。
### Innovation
介绍了一种训练小型协调器的方法——ToolOrchestra，它使用了基于结果、效率和用户偏好奖励的强化学习。ToolOrchestra产出了Orchestrator模型，该模型在提高准确率的同时降低了成本，并且在推荐工具使用方面与用户偏好相符。Orchestrator在HLE测试中得分37.1%，比GPT-5（35.1%）更高效，成本仅为后者的2.5倍。在tau2-Bench和FRAMES测试中，Orchestrator的成本仅占GPT-5的30%，性能远超GPT-5。结果证明，与现有方法相比，使用轻量级协调器组合多样化工具更加高效且更有效，为实用且可扩展的工具增强推理系统开辟了道路。
### Conclusion
这些结果表明，通过用轻量级协调器组合不同工具是比现有方法更高效和更有效的，这为实用且可扩展的工具增强推理系统奠定了基础。
## 779. `cs.LG` - 低资源设备上的持续错误纠正 [PDF](https://arxiv.org/pdf/2511.21652), [HTML](https://arxiv.org/abs/2511.21652)
### Authors
Kirill Paramonov,Mete Ozay,Aristeidis Mystakidis,Nikolaos Tsalikidis,Dimitrios Sotos,Anastasios Drosou,Dimitrios Tzovaras,Hyunjun Kim,Kiseok Chang,Sangdok Mo,Namwoong Kim,Woojong Yoo,Jijoong Moon,Umberto Michieli
### Background
日常设备中AI模型的增多突显了一个关键问题：预测错误导致用户体验下降。现有的解决方案主要关注于错误检测，但很少提供有效的修正机制，尤其是对于资源受限的设备而言。
### Innovation
提出了一个新颖的系统，通过少量示例学习让用户能够纠正AI的错误分类，同时没有过多消耗计算资源和存储空间。该系统结合了服务器端的基础模型训练和设备端原型分类，通过原型更新而非重新训练模型来实现有效的错误修正。
### Conclusion
在图像分类和物体检测任务上展示了系统的有效性，在Food-101和Flowers-102数据集的一次性测试中纠正了超过50%的错误，且几乎无遗忘（低于0.02%）且几乎没有计算开销。通过Android演示应用实现了系统的实用性。
## 780. `cs.LG` - 关于在干扰下基于演变的模型的实验 [PDF](https://arxiv.org/pdf/2511.21675), [HTML](https://arxiv.org/abs/2511.21675)
### Authors
Sadegh Shirani,Mohsen Bayati
### Background
在网络化的系统中，因果效应估计是数据驱动决策的关键。在这种情境下，一个单位的干预可以影响其他单位，而在复杂的物理或社会系统中，驱动这些干扰结构的交互路径大多未被观察到。论文指出，在识别群体水平的因果效应时，不一定需要恢复精确的网络结构，而是需要理解这些交互如何促进结果的演变。基于此原则，研究者探索了一种基于演变的方法，研究结果如何在干预后随观察周期变化，从而弥补缺失的网络信息。
### Innovation
提出了一种基于演变的框架方法，不存在个体单位间的并行路径假设，而是通过在治疗情景下的并行演变模式来估计反事实轨迹。治疗随机化不仅消除潜在混杂因素，还隐式地从隐藏的干扰渠道进行了抽样，使个体异质性溢出效应的稳健学习成为可能。进一步将因果消息传递作为密集网络中的一个实例，扩展到更广泛的影响结构，包括影响者网络，通过少量单位驱动大多数溢出效应。
### Conclusion
这种方法有其局限性，包含强烈的时序趋势或内生性的干扰可能会削弱识别效果。然而，该框架方法为在复杂系统中进行实验性分析提供了一种新的视角。
## 781. `cs.LG` - 配备渐进式多媒体语义记忆的自主学习者 [PDF](https://arxiv.org/pdf/2511.21678), [HTML](https://arxiv.org/abs/2511.21678)
### Authors
Weihao Bo,Shan Zhang,Yanpeng Sun,Jingjing Wu,Qunyi Xie,Xiao Tan,Kunbin Chen,Wei He,Xiaofan Li,Na Zhao,Jingdong Wang,Zechao Li
### Background
现有的大规模语言模型（MLLMs）在解决单个查询时表现出强大的推理能力，但它们独立地处理每个问题，经常会重蹈覆辙。现有的基于记忆增强的代理主要存储过往轨迹以供重复使用，但由于短暂性偏见，这些轨迹逐渐失去了关键领域的知识。此外，即使是在真正的多模态问题解决环境中，也只记录单一模态的行为轨迹，未能保留视觉注意力与逻辑推理如何共同作用以解决问题。这种做法与人类的认知方式不相符合，因为语义记忆是既多模态又整合的，通过协调但各自独立的表现流来保存视觉和抽象知识。
### Innovation
本文提出了一种双流记忆框架ViLoMem，能够构建紧凑的基于模式的记忆系统。它分别编码视觉注意力的干扰模式和逻辑推理的错误，使MLLMs能够从成功和失败的经验中学习。该系统遵循增益和精炼的原则，逐渐累积和更新多模态语义知识，同时避免灾难性遗忘，保持稳定且普遍适用的策略。实验结果表明，ViLoMem在六个多模态基准上持续改善了pass@1准确性，并显著减少了重复的视觉和逻辑错误。
### Conclusion
消融实验确认了双流记忆在显式干扰和幻觉分离中的必要性，表明多模态记忆和错误意识对于终身和跨领域自主学习具有价值。我们的项目页面将在此处提供。
## 782. `cs.LG` - 双平衡多任务学习 [PDF](https://arxiv.org/pdf/2308.12029), [HTML](https://arxiv.org/abs/2308.12029)
### Authors
Baijiong Lin,Weisen Jiang,Feiyang Ye,Yu Zhang,Pengguang Chen,Ying-Cong Chen,Shu Liu,Ivor W. Tsang,James T. Kwok
### Background
多任务学习旨在同时学习多个相关任务，已在多个领域取得了巨大成功。然而，不同任务之间的损失和梯度尺度差异常常导致性能妥协，任务平衡仍然是一个重大挑战。
### Innovation
提出了一种名为 Dual-Balancing Multi-Task Learning (DB-MTL) 的新方法，从损失和梯度两个方面实现任务平衡。具体来说，DB-MTL 通过对每个任务损失执行对数变换来实现损失尺度平衡，并通过将所有任务梯度标准化为可比较的大小（使用最大梯度范数）来重新调整梯度幅度。
### Conclusion
在多个基准数据集上的广泛实验表明，DB-MTL 一贯优于当前最先进的方法。
## 783. `cs.LG` - TinyFormer：在微型设备上高效设计和部署变压器架构 [PDF](https://arxiv.org/pdf/2311.01759), [HTML](https://arxiv.org/abs/2311.01759)
### Authors
Jianlei Yang,Jiacheng Liao,Fanding Lei,Meichen Liu,Lingkun Long,Junyi Chen,Han Wan,Bei Yu,Weisheng Zhao
### Background
在各种嵌入式物联网应用中，小尺寸设备（如微控制器单元，MCU）上的深度学习模型开发吸引了大量关注。然而，由于这些设备的硬件资源限制非常严重，高效设计并部署最新的先进模型（例如，变压器模型）是一个挑战。
### Innovation
本文提出了一种名为TinyFormer的框架，专门设计用于在MCU上开发和部署资源高效的变压器模型。TinyFormer包括SuperNAS、SparseNAS和SparseEngine三个部分。此外，作者还表示，SparseEngine是第一个能够在MCU上实现稀疏变压器模型推理的部署框架。
### Conclusion
TinyFormer能够在1MB存储和320KB内存的硬件约束下设计出高效的变压器模型，其准确率达到96.1%。此外，与CMSIS-NN库相比，TinyFormer在稀疏推理方面表现出了显著的加速效果，最高可达12.2倍。TinyFormer有望将强大的变压器模型引入TinyML场景，大大拓展深度学习的应用范围。
## 784. `cs.LG` - TraceGen: 3D追踪空间中的世界建模使跨机体视频学习成为可能 [PDF](https://arxiv.org/pdf/2511.21690), [HTML](https://arxiv.org/abs/2511.21690)
### Authors
Seungjae Lee,Yoonkyo Jung,Inkook Chun,Yao-Chih Lee,Zikui Cai,Hongjia Huang,Aayush Talreja,Tan Dat Dao,Yongyuan Liang,Jia-Bin Huang,Furong Huang
### Background
从少量演示中学习新机器人任务并适用于新的平台和场景仍然是富有挑战性的。虽然其他机体（人类和不同类型机器人）的视频很丰富，但不同的机体、摄像机和环境使得这些视频难以直接使用。
### Innovation
本文通过引入统一的符号表示——三维（3D）“追踪空间”中的场景级轨迹——解决了小数据问题。这是一种紧凑的3D轨迹空间表示，能够跨机体、跨环境和跨任务学习。此外，本文还提出了TraceGen，这是一种在追踪空间预测未来运动而不是像素空间的世界模型，并通过抽象掉外观而保留必要的几何结构以进行操控。最后，本文开发了TraceForge，一种将异构的人类和机器人视频转换为一致的3D轨迹的数据管道。这些改进使得仅通过少量目标机器人视频即可实现高效的转移学习。
### Conclusion
在仅使用五个目标机器人视频的情况下，TraceGen在四项任务中实现80%的成功率，其推理速度比最先进的基于视频的世界模型快50-600倍。当仅有五个未校准的手持手机捕获的人类演示视频可用时，TraceGen在实际机器人上的成功率仍可达到67.5%，这突显了其在不依赖物体检测器或大量像素空间生成的情况下，能够跨机体进行适应性调整的能力。
## 785. `cs.LG` - HO-FMN: 基于超参数优化的快速最小范数攻击 [PDF](https://arxiv.org/pdf/2407.08806), [HTML](https://arxiv.org/abs/2407.08806)
### Authors
Raffaele Mura,Giuseppe Floris,Luca Scionis,Giorgio Piras,Maura Pintor,Ambra Demontis,Giorgio Giacinto,Battista Biggio,Fabio Roli
### Background
梯度攻击是评估机器学习模型鲁棒性的主要工具之一。然而，许多攻击往往提供过于乐观的评估，因为它们使用固定损失函数、优化器、步长调度器和默认超参数。
### Innovation
本文提出了一种参数化的快最小范数攻击算法变种，该算法的损失、优化器、步长调度器和超参数可以动态调整。通过这样的设计，该攻击方法能够在不需要额外调整的情况下找到更小的对抗性扰动，并能按扰动预算报告对抗性鲁棒性，提供比固定预算攻击更全面的评估，同时保持高效。
### Conclusion
本工作通过动态调整损失、优化器、步长调度器和超参数，克服了现有梯度攻击方法的局限性。实验结果表明，使用HO-FMN攻击相比现有方法能找到更小的对抗性扰动，同时使得对抗性鲁棒性能够按扰动预算变化进行评估。此外，HO-FMN方法保持了高效性，并开放了源代码供学术界使用。
## 786. `cs.LG` - 单政策 vs. 双政策强化学习在动态单车再平衡中的应用 [PDF](https://arxiv.org/pdf/2402.03589), [HTML](https://arxiv.org/abs/2402.03589)
### Authors
Jiaqi Liang,Defeng Liu,Sanjay Dominik Jena,Andrea Lodi,Thibaut Vidal
### Background
共享自行车系统（BSS）提供了一种可持续的城市交通解决方案，但其可靠性需要有效的再平衡策略来应对随机需求，防止单车站之间的不平衡。
### Innovation
本文提出了强化学习（RL）算法来解决动态再平衡问题，引入并比较了两种RL方法：单政策RL和双政策RL。这是将网络优化问题在连续时间框架内表述为马尔可夫决策过程的一种尝试。两种方法分别为：第一种方法使用单一的深Q网络（DQN）联合学习库存和路由决策；第二种方法将节点级库存决策与弧级车辆路由分离，以提高学习效率和适应性。研究成果为实时再平衡提供了有价值的见解，突显了RL在城市交通中更适应、更智能解决方案的潜力。
### Conclusion
实验结果表明，单政策模型在与多个基准模型竞争中表现良好，而双政策模型显著减少了需求损失。这些发现为共享单车运营提供了宝贵的见解，加强了RL在实时再平衡中的潜在应用，并为更适应和智能的城市交通解决方案铺平了道路。
## 787. `cs.LG` - 启用语音识别中的差分隐私联邦学习：基准、自适应优化器和梯度剪裁 [PDF](https://arxiv.org/pdf/2310.00098), [HTML](https://arxiv.org/abs/2310.00098)
### Authors
Martin Pelikan,Sheikh Shams Azam,Vitaly Feldman,Jan ?Honza? Silovsky,Kunal Talwar,Christopher G. Brinton,Tatiana Likhomanenko
### Background
尽管联邦学习（FL）和差分隐私（DP）已被广泛研究，但它们在自动语音识别（ASR）中的应用仍然未被充分探索，这主要是因为大型变换器模型的训练存在挑战。大模型在FL中更为突出的问题在于层间梯度异质性，而浅层模型则表现出相对一致的梯度行为。因此，现有的工作难以使用标准优化技术实现收敛，即使没有DP机制。迄今为止，没有任何现有工作在ASR背景下为FL与DP建立了竞争性的、实用的实现方法。
### Innovation
本文首次建立了在端到端ASR中使用FL与DP的第一个基准。通过逐层剪裁和按层梯度归一化的技术，本文有效缓解了深层模型中的剪裁偏差和层间梯度异质性。在强隐私保证下，FL与DP在至少几百万用户群体中是可行的。在FL与DP的ASR中，我们达到了用户层面的（7.2, $10^{-9}$）-DP（相对词误差率下降1.3%）和（4.5, $10^{-9}$）-DP（相对词误差率下降4.6%）。尽管实验主要集中在ASR上，但我们揭示的基本原理，特别是关于梯度异质性和按层梯度归一化的内容，为跨领域设计可扩展、隐私保护的FL算法提供了更广泛的指导。
### Conclusion
通过逐层剪裁和按层梯度归一化的策略，本文实现在ASR中的FL和DP，并在至少几百万用户群体中保持了较高的准确率。文章还为跨领域设计隐私保护的FL算法提供了更广泛的指导。所有实验和基准代码均可从这个链接获取：this https URL。
## 788. `cs.LG` - 联邦学习：随机近似方法 [PDF](https://arxiv.org/pdf/2402.12945), [HTML](https://arxiv.org/abs/2402.12945)
### Authors
Srihari P V,Anik Kumar Paul,Bharath Bhikkaji
### Background
本文探讨了在随机逼近框架下的联邦学习（FL）。在这种方案中，每个客户端使用其数据集?(?mathcal{D}^{(i)}?)训练本地模型，并定期将模型参数?(w^{(i)}_n?)传输给中心服务器。这些参数在服务器端被汇总成全局模型参数?(?bar{w}_n?)并发回客户端继续训练。现有研究通常假设所有客户端的步长（学习率）在模型训练中是恒定的，因而导致聚合模型仅以期望收敛。本文采用了针对每个客户端的递减步长（适应性学习率），这样客户端的模型权重取决于其步长受限比?(p^{(i)} = ?lim_{n ?to ?infty} ?frac{a^{(i)}_n}{a^{(1)}_n}?)，其中?(a^{(1)}_n ?geq a^{(i)}_n?)，?(?forall n?)。这种递减步长使得全局模型更有可能以概率1收敛。而且，步长受限比较大的客户端对全局模型的影响更大，可用来偏爱拥有罕见和不常见数据的客户端。
### Innovation
本文引入了针对每个客户端递减的（自适应）步长，展示了全局模型能够跟踪一个由各客户端梯度的加权负和构成的微分方程解。与恒定步长的情况相比，递减步长使全局模型能以概率1收敛，并且能够影响各客户端在全局模型中的贡献，有利于拥有独特数据的客户端。
### Conclusion
通过数值实验验证了这种方法的收敛性，并演示了客户端学习率选择的过程，显示了这种递减步长方法在调节客户端对全局模型的影响上是有效的。
## 789. `cs.LG` - 通过融合全局和局部统计信息进行数据估值 [PDF](https://arxiv.org/pdf/2405.17464), [HTML](https://arxiv.org/abs/2405.17464)
### Authors
Xiaoling Zhou,Ou Wu,Michael K. Ng,Hao Jiang
### Background
近年来，高质量数据在各应用中的关键角色引起了人们对数据估值的关注。Shapley值基于的估值方法因其坚实的理论基础而最为常用。然而，Shapley值的确切计算往往因计算量过大而难以实现，因此，大量的近似技术被开发出来。尽管有了显著的进步，现有的方法通常忽略了估值分布信息的融入，未能充分考虑动态数据条件，这限制了它们的性能和应用潜力。
### Innovation
本文强调了全局和局部统计特性在数据估值中的关键作用。首先，对各种模拟和真实世界数据集的估值分布进行了全面分析，揭示了有价值的新见解和模式。其次，提出了一种融合探索到的分布特征以改进Shapley值估计的增强型数据估值方法，并将这些正则化项无缝地整合到现有的多种数据估值方法中。第三，引入了一种新的动态数据估值方法，该方法无需重新计算Shapley值即可推断数据值的更新，从而极大地提高了计算效率。广泛的实验结果显示了本文提出的模型的一致有效性和效率，证实了全局和局部估值分布在数据估值中的巨大潜力。
### Conclusion
实验结果表明，本文提出的融合全局和局部统计信息的数据估值方法在数据估值、根据价值数据添加和删除、检测误标数据和动态数据估值等方面表现出一致的有效性和效率，验证了全球和局部价值分布对数据估值的重要潜力。
## 790. `cs.LG` - 联邦大型语言模型：当前进展与未来方向 [PDF](https://arxiv.org/pdf/2409.15723), [HTML](https://arxiv.org/abs/2409.15723)
### Authors
Yuhang Yao,Jianyi Zhang,Junda Wu,Chengkai Huang,Yu Xia,Tong Yu,Ruiyi Zhang,Sungchul Kim,Ryan Rossi,Ang Li,Lina Yao,Julian McAuley,Yiran Chen,Carlee Joe-Wong
### Background
大型语言模型正在迅速普及，并且被广泛应用于实际场景。虽然训练数据的质量至关重要，但在数据收集过程中也引发了隐私问题。联邦学习（FedLLM）作为一种解决方案，允许多个客户端无需共享本地数据即可协作训练大型语言模型。然而，联邦学习也引入了新的挑战，如异质数据导致的模型收敛问题和高昂的通信成本。
### Innovation
本文综述了联邦学习在大型语言模型中的应用（FedLLM），强调了最近的进展和未来的研究方向。重点讨论了联邦设置下的微调和提示学习，分析了现有的工作以及相关研究挑战。
### Conclusion
最后，提出了联邦大型语言模型的潜在研究方向，包括预训练、联邦智能体和用于联邦学习的大语言模型。
## 791. `cs.LG` - 超越准确性：填补中不确定性估计的经验研究 [PDF](https://arxiv.org/pdf/2511.21607), [HTML](https://arxiv.org/abs/2511.21607)
### Authors
Zarin Tahia Hossain,Mostafa Milani
### Background
数据驱动分析中的数据缺失处理是一个核心挑战。现代填补方法不仅追求重建的准确性，还以不同方式表示和量化不确定性。然而，这些不确定性估计的可靠性和校准性仍然知之甚少。
### Innovation
该研究系统地比较了三种主要填补方法家族（统计方法、分布对齐方法和深度生成方法）的不确定性估计，通过多次运行的变异性、条件采样和预测分布建模三种互补途径进行评估，并使用校准曲线和预期校准误差（ECE）进行评价。研究发现准确性与校准性往往是不一致的，高重建准确性的模型并不一定提供可靠的不确定性估计。
### Conclusion
研究结果表明，准确性与校准性往往不一致：高重建准确性的模型并不一定提供可靠的不确定性估计。研究还分析了方法特定的权衡，稳定配置，并提出了在数据清洗和下游机器学习管道中选择意识填补方法的指导原则。
## 792. `cs.LG` - No Request Left Behind: Tackling Heterogeneity in Long-Context LLM Inference with Medha [PDF](https://arxiv.org/pdf/2409.17264), [HTML](https://arxiv.org/abs/2409.17264)
### Authors
Amey Agrawal,Haoran Qiu,Junda Chen,Íñigo Goiri,Chaojie Zhang,Rayyan Shahid,Ramachandran Ramjee,Alexey Tumanov,Esha Choukse
### Background
部署拥有百万级Token的大型语言模型（LLMs）极具挑战性，因为生产工作负载极为多样化，包含了短查询和长文档的混合。这种多样性与注意力机制的二次复杂性相结合，产生了严重的连锁延误效应，即长时间运行的请求阻止了短的、交互式的请求，从而降低了系统的响应性。
### Innovation
Medha是一个服务系统，通过引入细粒度的抢占调度来消除这些连锁延误效应。Medha采用了一组协同设计的机制，包括自适应分块和流管道并行等策略，克服了分块的效率和扩展性问题。此外，该系统还引入了一种新的并行策略——KV缓存并行性，以减少解码延迟，并在极长上下文的情况下提供交互性。这些机制由一个名为LARS的调度器管理，该调度器是一个截止日期和多样化负载感知的调度策略，可以防止连锁延误效应和简单策略引起的饥饿问题。
### Conclusion
在多样化的负载下，与最先进的非抢占系统相比，Medha的吞吐量提高了5.7倍，中位数和99百分位的延迟分别减少了30倍和174倍。
## 793. `cs.LG` - CTSyn: 一种跨表格数据生成的基础模型 [PDF](https://arxiv.org/pdf/2406.04619), [HTML](https://arxiv.org/abs/2406.04619)
### Authors
Xiaofeng Lin,Chenheng Xu,Matthew Yang,Guang Cheng
### Background
生成式基础模型（GFMs）在生成高质量图像和文本合成数据方面取得了显著成功。然而，将其应用于表格数据时面临着巨大挑战，因为表格特征具有异质性。现有的跨表格学习框架面临困难，主要是因为缺乏生成模型骨架和有效的异质特征值解码机制。
### Innovation
提出了一种基于扩散的生成式基础模型CTSyn，用于生成表格数据。CTSyn 包含两个关键组成部分：自动编码器网络，用于将多样化的表格集成到统一的潜在空间，并利用表模式嵌入动态重构表格值，适应异构数据集；条件潜在扩散模型，从学习的潜在空间生成样本，基于表模式条件。
### Conclusion
CTSyn 在大规模预训练后，对比现有表格合成器在标准基准测试中的性能，不仅在有用性而且在多样性方面都表现出优势。这些结果使CTSyn 成为合成表格生成的一个有前途的框架，并为开发大规模表格基础模型奠定了基础。
## 794. `cs.LG` - CoxKAN：用于可解释高性能生存分析的柯尔莫戈罗夫-阿诺尔德网络 [PDF](https://arxiv.org/pdf/2409.04290), [HTML](https://arxiv.org/abs/2409.04290)
### Authors
William Knottenbelt,William McGough,Rebecca Wray,Woody Zhidong Zhang,Jiashuai Liu,Ines Prata Machado,Zeyu Gao,Mireia Crispin-Ortuzar
### Background
生存分析是医学中用于建模死亡或其他关键事件（如复发）发生时间的一门统计分支，旨在提高治疗策略和患者预后。选择生存分析模型通常需要在性能和解释性之间进行权衡。虽然深度学习模型性能高但缺乏透明度，这种高不透明性在医学领域会对基于敏感病人决策的使用产生显著问题。
### Innovation
作者引入了CoxKAN，这是一种用于可解释、高性能生存分析的Cox比例风险Kolmogorov-Arnold网络。通过与多层感知器相比，Kolmogorov-Arnold网络作为更为可解释和准确的替代方案。CoxKAN不仅在合成数据集上准确地恢复了解释性风险函数公式，在自动特征选择上也表现出色；在真实数据集上，CoxKAN连续优于传统的Cox比例风险模型（C-index最高提高4%），并且其性能与基于深度学习的模型相当甚至更优。重要的是，与其他生存分析方法相比，CoxKAN揭示了预测变量之间的复杂交互关系，还发现了符号公式，为关键生物标志物对患者风险影响的深入理解提供了清晰的见解。
### Conclusion
CoxKAN已经在GitHub和Zenodo上开放获取，其在合成和真实数据集上都展示了优秀的性能和可解释性，为临床决策提供了有价值的支持。
## 795. `cs.LG` - HoGA：通过多样性意识的k跳采样实现高阶图注意 [PDF](https://arxiv.org/pdf/2411.12052), [HTML](https://arxiv.org/abs/2411.12052)
### Authors
Thomas Bailie,Yun Sing Koh,Karthik Mukkavilli
### Background
图形模型可以表示许多实际系统中的潜在变量关系，消息传递神经网络（MPNNs）广泛用于学习这些结构以供下游任务使用。尽管基于边的MPNNs能够捕捉局部交互，但它们在表达能力上理论上受到限制，这限制了更高阶关系的发现。
### Innovation
提出了高阶图关注（HoGA）模块，通过采样子图来构建k阶注意力矩阵，最大化特征向量之间的多样性。与现有的高阶注意力方法相比，HoGA针对高阶拓扑中的多样化模态进行优化，减少了冗余并扩展了捕获的子结构的范围。当应用于两种单一跳注意力模型时，HoGA在所有基准节点分类数据集上至少实现了5%的准确性提升，并在八个数据集中有六个数据集上超过了最近的基线。
### Conclusion
HoGA在多个节点分类数据集上的实验结果表明，该模块能够有效地提高模型性能，特别是在高阶结构的发现和捕捉方面显示出优势。
## 796. `cs.LG` - Matrix：基于对等多智能体的合成数据生成框架 [PDF](https://arxiv.org/pdf/2511.21686), [HTML](https://arxiv.org/abs/2511.21686)
### Authors
Dong Wang,Yang Li,Ansong Ni,Ching-Feng Yeh,Youssef Emad,Xinjie Lei,Liam Robbins,Karthik Padthe,Hu Xu,Xian Li,Asli Celikyilmaz,Ramya Raghavendra,Lifei Huang,Carole-Jean Wu,Shang-Wen Li
### Background
合成数据在训练大型语言模型中变得越来越重要，特别是在缺少真实数据、数据成本高昂或涉及隐私保护的情况下。许多合成数据的生成任务需要协调多智能体的工作流程，不同类型的智能体合作以生产高质量、多样化且结构更丰富的数据。然而，现有的多智能体合成框架往往依赖于中心化协调者，这造成了可扩展性瓶颈，或者仅仅针对特定领域进行硬编码，限制了灵活性。
### Innovation
Matrix 提出了一种去中心化的框架，通过分布式队列传递序列化的消息来表示控制和数据流。这样设计消除了中心化协调者，并允许每一个任务通过轻量级智能体独立进展，而计算密集型操作则由分布式服务处理。搭建于 Ray 上，Matrix 可扩展到成千上万的并发任务，并提供了模块化可配置的设计，使框架很容易适应各种数据生成工作流。
### Conclusion
我们在多种形式的合成场景中评估了 Matrix，包括多智能体协作对话、基于网络的推理数据抽取和客户服务环境中的工具使用轨迹生成。在所有情况下，Matrix 都在相同的硬件资源下实现了 2 到 15 倍的数据生成吞吐量提升，同时不损害输出质量。
## 797. `cs.LG` - TAB-DRW：一种基于DFT的生成表格数据的健壮水印 [PDF](https://arxiv.org/pdf/2511.21600), [HTML](https://arxiv.org/abs/2511.21600)
### Authors
Yizhou Zhao,Xiang Li,Peter Song,Qi Long,Weijie Su
### Background
生成式AI的发展使得跨卫生保健、金融和公共政策等领域生成高保真合成表格数据成为可能，但也引发了数据来源和滥用的担忧。水印技术为解决这些问题提供了有希望的解决方案，以确保合成数据的可追溯性。然而，现有的方法存在许多局限性：由于依赖于大型扩散模型导致计算成本高昂；难以处理混合离散连续数据；或对后续修改缺乏鲁棒性。
### Innovation
提出了一种高效且鲁棒的生成表格数据后编辑水印方案——TAB-DRW。该方案将水印信号嵌入到频域中：先通过Yeo-Johnson变换和标准化规范化异构特征，然后应用离散傅里叶变换(DFT)，并根据预计算产生的伪随机位调整选定条目的虚部。为了进一步增强鲁棒性和效率，还引入了一种基于秩的伪随机比特生成方法，可以在不增加存储开销的情况下进行行级检索。
### Conclusion
在五个基准表格数据集上的实验表明，TAB-DRW具有强检测性和对常见后续处理攻击的鲁棒性，同时保持了高度的数据保真度，并全面支持混合类型特征。
## 798. `cs.LG` - 数据驱动的Lipschitz连续性：一种改进抗对抗攻击鲁棒性的高效方法 [PDF](https://arxiv.org/pdf/2406.19622), [HTML](https://arxiv.org/abs/2406.19622)
### Authors
Erh-Chung Chen,Pin-Yu Chen,I-Hsin Chung,Che-Rung Lee
### Background
随着深度神经网络（DNNs）在敏感应用中的广泛应用，确保其安全性和鲁棒性变得至关重要。对抗性攻击是DNNs的主要威胁之一，即使是对输入添加很小的扰动也可能导致错误预测。最近的对抗训练进展通过引入来自外部数据集或生成模型的额外样本来提高鲁棒性，但这些方法往往计算成本高昂，限制了其实用性和实际部署。
### Innovation
本研究提出了一种基于Lipschitz连续性的成本效益解决方案，该方案的鲁棒性与使用大量额外数据训练的模型相当。与传统的对抗性训练不同，我们的方法只需要对数据集进行一次遍历，无需进行梯度估计，使其具有很高的效率。此外，我们的方法可以无缝集成到现有的对抗性训练框架中，增强模型的鲁棒性，而不需要额外的生成数据。实验结果显示，我们的方法不仅减少了计算开销，还维持或提高了鲁棒神经网络的防御能力。这项工作为开发对抗性攻击的实用、可扩展防御措施开辟了新的方向。
### Conclusion
实验结果表明，我们的方法不仅减少了计算开销，还维持或提高了鲁棒神经网络的防御能力。这项工作为开发对抗性攻击的实用、可扩展防御措施开辟了新的方向。
## 799. `cs.LG` - CroMe: 使用跨模态三端变压器和度量学习的多模态虚假新闻检测 [PDF](https://arxiv.org/pdf/2501.12422), [HTML](https://arxiv.org/abs/2501.12422)
### Authors
Eunjee Choi,Junhyun Ahn,XinYu Piao,Jong-Kook Kim
### Background
多模态虚假新闻检测近年来受到越来越多的关注。现有的方法依赖于独立编码的单模态数据，并忽略了通过高级技术捕捉模内关系和整合模间相似性的优势。
### Innovation
提出了跨模态三端变压器和度量学习的多模态虚假新闻检测方法（CroMe）。CroMe 使用 Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models (BLIP2) 作为编码器, 来捕捉详细的文本、图像和组合的图像文本表示。度量学习模块采用代理锚点方法来捕捉模内关系，特征融合模块使用跨模态三端变压器进行有效整合。最终，融合特征通过分类器来预测内容的真实性。
### Conclusion
实验表明，CroMe 在多模态虚假新闻检测方面表现出色。
## 800. `cs.LG` - 使用表示优化增强训练数据归属 [PDF](https://arxiv.org/pdf/2505.18513), [HTML](https://arxiv.org/abs/2505.18513)
### Authors
Weiwei Sun,Haokun Liu,Nikhil Kandpal,Colin Raffel,Yiming Yang
### Background
训练数据归属（TDA）方法旨在衡量训练数据如何影响模型的预测。梯度基归属方法虽然提供了理论基础，但在大规模应用中的计算成本使其不切实际。基于表示的方法则更加可扩展，但通常依赖于未优化归属的启发式嵌入，限制了它们的精度。
### Innovation
我们提出AirRep，一种可扩展的、基于表示的方法，通过学习特定任务和模型对齐的优化表示来解决这些挑战。AirRep 包含两个关键创新：一个用于提高归属质量的可训练编码器，以及基于注意力的聚合机制，能够准确估计群体影响。
### Conclusion
实验表明，AirRep 在预测性能上与最先进的梯度基方法相当，而在推断时间上的效率提高了近两个数量级。进一步的分析表明，它在任务和模型方面的鲁棒性和泛化能力很强。我们的代码可以在以下链接找到：this https URL
## 801. `cs.LG` - 通过矩阵分裂和预条件化统一线性函数逼近在离策强化学习中的视角 [PDF](https://arxiv.org/pdf/2501.01774), [HTML](https://arxiv.org/abs/2501.01774)
### Authors
Zechen Wu,Amy Greenwald,Ronald Parr
### Background
在强化学习中的离策策略评估（OPE）任务中，传统的观点认为时间差分学习（TD）、拟质心迭代（FQI）和部分拟质心迭代（PFQI）在目标价值函数更新次数上有所不同：TD一次更新，FQI无限次更新，而PFQI是有限次更新。本文指出这种观点并不准确，并从线性价值函数逼近的新数学视角出发，将这些方法统一为一套迭代方法，处理相同的线性系统，但由于采用了不同的矩阵分裂方案和预条件化手段，因而具有不同的特性。
### Innovation
本文提出了一个新的数学框架，通过矩阵分裂和预条件化的方式统一线性函数逼近下的离策策略评估方法。该框架证明了增加目标价值函数更新次数的技术实际上是从使用固定预条件化转换为使用数据特征自适应预条件化。这项工作首次阐明了TD收敛并不必然意味着FQI收敛，并建立了TD、PFQI和FQI之间的紧密收敛联系。此外，本文还提出了一种编码解码视角来更好地理解TD的收敛条件，证明了当学习率较大不起作用时，尝试较小的学习率可能有助于收敛。此外，本文发现了新的特征收敛条件，并揭示了常见的特性假设如何影响收敛，例如，线性独立特性的假设可以在不影响随机TD在特定环境下的收敛保证的情况下被舍弃。
### Conclusion
本文通过统一的方法提供了比以前更加精确的理论结果，并对每种算法的收敛条件进行了刻画。这一框架还揭示了特征对于这些算法收敛至关重要的条件，并且展示了常见的特征假设如何影响收敛。此外，这是首次将矩阵分裂技术引入这些算法收敛分析中。
## 802. `cs.LG` - 通过卷积Fenchel-You损失建立凸平滑损失的线性替代遗憾上限 [PDF](https://arxiv.org/pdf/2505.09432), [HTML](https://arxiv.org/abs/2505.09432)
### Authors
Yuzhou Cao,Han Bao,Lei Feng,Bo An
### Background
 surrogate regret bounds（也称为超额风险上限）连接了替代损失和目标损失的收敛率。虽然凸平滑替代损失因高效估计和优化而引人注目，但优化和估计性能更好的凸平滑替代损失在转化到目标损失后可能导致线性替代遗憾界限的线性性质丧失。当前情况下，一群研究者认为在替代损失和目标损失之间的转化过程中存在平滑度和线性遗憾界限之间的权衡。
### Innovation
该研究通过构造一种基于卷积Fenchel-Young损失的凸平滑替代损失，克服了这一困境。这些损失是生成滤波器熵的Fenchel-Young损失，等同于一般化熵和目标贝叶斯风险的下最小卷积。这种构造方法不仅保持了线性替代遗憾界限，还利用下最小卷积提供了一个一致的类概率估计器，从而展示了凸分析如何渗透优化和统计效率风险最小化。
### Conclusion
本文的结果展示了如何通过凸分析的方法解决优化和统计效率之间的权衡问题，从而为任意离散目标损失提供了这种凸平滑替代损失的线性替代遗憾界限。
## 803. `cs.LG` - F-INR: 功能性张量分解在隐式神经表示中的应用 [PDF](https://arxiv.org/pdf/2503.21507), [HTML](https://arxiv.org/abs/2503.21507)
### Authors
Sai Karthikeya Vemuri,Tim Büchner,Joachim Denzler
### Background
隐式神经表示（INRs）模型信号为连续且可差分的函数。然而，单一的多维INRs随着数据维度的增加会变得扩展性差，导致训练成本过高。该研究指出，这可以通过功能张量分解将高维度的INR分解成一组紧凑且轴向特定的子网络来解决。
### Innovation
作者提出了一种新的框架F-INR，该框架通过功能张量分解将高维度的INR分解成一组紧凑且轴向特定的子网络。这些子网络学习低维度的功能组件，然后通过张量操作进行组合。这种方法不仅减少了计算复杂性，还提高了表示能力。F-INR在架构和分解选择上是灵活的，可以与各种已有的INR主干网络和张量格式兼容，提供了速度与准确性的权衡控制。
### Conclusion
实验结果显示，F-INR在加速训练速度和提高保真度（PSNR指标超过6.0 dB）方面均优于现有的最先进的INRs。该研究还展示了F-INR在图像表示、3D几何重建和神经辐射场等任务上的应用效果。进一步地，该研究还展示了F-INR在科学计算中的应用，特别是用于复杂物理模拟。因此，F-INR提供了一种适用于高维信号建模的可扩展、灵活且高效的框架。
## 804. `cs.LG` - 关于对抗训练在恶意软件分类器有效性方面的研究 [PDF](https://arxiv.org/pdf/2412.18218), [HTML](https://arxiv.org/abs/2412.18218)
### Authors
Hamid Bostani,Jacopo Cortellazzi,Daniel Arp,Fabio Pierazzi,Veelasha Moonsamy,Lorenzo Cavallaro
### Background
尽管对抗训练（AT）是抵御机器学习欺骗攻击的关键防御手段，但其在真实世界恶意软件检测中的有效性仍不明确。现有研究存在关键缺陷：往往忽略了恶意软件固有的特征，研究也不够连贯，倾向于孤立地研究诸如对抗样本的现实性和置信度等变量，或者依赖于弱的评估方法，导致得出的洞见不具备普适性。
### Innovation
本文介绍了一种名为Rubik的框架，以系统性、多维度的方式评估AT在恶意软件检测中的效果。Rubik框架定义了关键因素，涉及数据、特征表示、分类器和健壮优化设置等核心维度，通过可靠评估实践（如现实的欺骗攻击），全面探索影响AT的关键变量之间的相互作用。
### Conclusion
文章通过分析Android恶意软件实例，打破了先前的一些观点，例如对抗样本仅在特定条件下提供鲁棒性效益。研究表明，模型架构和特征空间结构在决定AT效果中的关键作用。研究总结了四个重要见解，揭示了四种常见的评估误解，并提出实践建议，以指导开发真正稳健的恶意软件分类器。
## 805. `cs.LG` - 进化预测游戏 [PDF](https://arxiv.org/pdf/2503.03401), [HTML](https://arxiv.org/abs/2503.03401)
### Authors
Eden Saig,Nir Rosenfeld
### Background
当预测算法服务于一组用户时，预测质量可能会出现差异。用户可能会根据准确的预测增加参与度、邀请朋友或采纳趋势，这种反馈循环不仅塑造了模型，也塑造了用户的群体特征。
### Innovation
引入了进化预测模型框架，该框架基于进化博弈理论，将这种反馈循环视为用户群体之间的自然选择过程。通过理论分析发现了理想化学习环境与现实世界之间的差距：在理想环境中，重复学习会促进竞争导致排他；但在现实约束条件下如有限的数据、计算能力或过拟合风险下，不同群体间的稳定共存和互惠共生成为可能。
### Conclusion
分析了这些稳定性和可行性，提出了支撑其存在机制，并通过实验证明了研究发现。
## 806. `cs.LG` - 主动学习方法及其对高效数据利用和模型性能提升的应用 [PDF](https://arxiv.org/pdf/2504.16136), [HTML](https://arxiv.org/abs/2504.16136)
### Authors
Chiung-Yi Tseng,Junhao Song,Ziqian Bi,Tianyang Wang,Chia Xin Liang,Xinyuan Song,Ming Liu
### Background
在数据驱动智能的时代，数据丰富而标注稀缺的困境已经成为机器学习发展中的关键瓶颈。
### Innovation
本文详细阐述了主动学习（AL）的概念，这是一种机器学习策略，能够在较少标注样本的情况下提高模型性能；并讨论了主动学习在计算机视觉、自然语言处理、迁移学习和实际应用中的应用；探讨了不确定性估计、类别不平衡处理、领域适应、公平性、强有力的评估指标和基准等关键研究主题；强调了模仿人类学习并以问题为导向的方法可以提高数据效率并帮助模型更好地学习；并指出现有挑战包括重建信任、确保可重复性以及应对不一致的方法论。
### Conclusion
本研究旨在为研究人员和实践者提供关键见解，并为未来主动学习的进步提出方向。研究表明，使用良好的评估措施时，主动学习常常比被动学习提供更好的结果。
## 807. `cs.LG` - 超越反省：通过外部行为反馈强化思考 [PDF](https://arxiv.org/pdf/2501.01457), [HTML](https://arxiv.org/abs/2501.01457)
### Authors
Diji Yang,Linda Zeng,Kezhen Chen,Yi Zhang
### Background
虽然大型语言模型（LLMs）的推理过程能够解决复杂问题，但这一过程可能因模型的概率性质而在知识边界附近变得不可靠或不一致。现有方法通过让模型自我批判其推理过程来修正错误，但这种方法继承了原始输出的偏见，即反省错觉。
### Innovation
本研究提出了一种外部主义三步骤框架——Distillation-Reinforcement-Reasoning（DRR），该框架通过评估模型的可观察行为来提供纠正性反馈，而不仅仅是依赖模型的自我反省。具体来说，DRR 首先提取推理者的行为痕迹，然后训练一个轻量级的外部区分模型（DM），在推理期间，该 DM 作为批评者，识别并拒绝可疑的推理步骤。这种外部反馈促使模型丢弃故障的路径并探索替代方案，从而在不改变基础模型的情况下提升推理质量。
### Conclusion
实验表明，我们的框架在多个推理基准测试中显著优于现有的自省方法。DRR 通过其轻量级且无需标注的设计，提供了一种对各种 LLM 的推理可靠性进行规模扩展和灵活调整的解决方案。
## 808. `cs.LG` - 不等量搭档：小帮手提升不确定性 [PDF](https://arxiv.org/pdf/2505.18636), [HTML](https://arxiv.org/abs/2505.18636)
### Authors
Tim G. Zhou,Evan Shelhamer,Geoff Pleiss
### Background
在高度不确定性的决策环境中应用深度网络时，通过多次随机初始化训练来构建模型集合（ensemble）已成为标准策略。然而，这一策略对现今大规模模型和实践中的微调流程不太适用。作者指出，传统的建模策略成本高且效率低下，因此探索了一种新的方法来提高大型模型的不确定性量化和下游决策.
### Innovation
提出了一个名为“不等量搭档”的新策略，即通过结合一个较小且不那么准确的“小帮手”模型（例如，微调后的ResNet-34）与一个大规模的模型（例如，微调后的ViT-B），以较低的计算成本改善大型模型的不确定性和决策表现。此策略以简单学习加权平均的方式聚合这两个模型的预测结果。
### Conclusion
实验结果显示，“不等量搭档”方法在五种图像分类基准、多种模型架构和训练方案（包括模型混合，model soups）中显著提升了准确性、不确定性量化和选择性分类指标，仅增加了大约10-20%的计算成本。
## 809. `cs.LG` - TS-RAG: 基于检索增强生成的时间序列基础模型在零样本预测中更强大的预测器 [PDF](https://arxiv.org/pdf/2503.07649), [HTML](https://arxiv.org/abs/2503.07649)
### Authors
Kanghui Ning,Zijie Pan,Yu Liu,Yushan Jiang,James Yiming Zhang,Kashif Rasul,Anderson Schneider,Lintao Ma,Yuriy Nevmyvaka,Dongjin Song
### Background
大型语言模型（LLMs）和基础模型（FMs）近年来在时间序列预测任务中变得流行。尽管微调LLMs可以实现领域适应，但它们在跨不同和未见过的数据集上进行泛化时经常遇到困难。此外，现有的时间序列基础模型（TSFMs）在处理非平稳动力学和分布转移时仍然面临挑战，主要原因在于缺乏有效的适应机制。
### Innovation
我们提出了一个检索增强生成框架TS-RAG，用于时间序列预测，以增强TSFMs的泛化能力和可解释性。TS-RAG利用预训练的时间序列编码器从专用知识库中检索语义相关的片段，以丰富输入查询的上下文表示。此外，我们提出了一个自适应检索混合器（ARM）模块，该模块动态地将检索到的模式与TSFM的内部表示融合，从而提高预测准确性，而不需要特定任务的微调。
### Conclusion
通过对七个公开基准数据集的全面实证研究，表明TS-RAG实现了最先进的零样本预测性能，在多个领域优于现有TSFMs，同时提供了令人满意的可解释性。我们的代码和数据可在以下链接获取：this https URL
## 810. `cs.LG` - 拥有精确风险证书的深层演员评论者 [PDF](https://arxiv.org/pdf/2505.19682), [HTML](https://arxiv.org/abs/2505.19682)
### Authors
Bahareh Tasdighi,Manuel Haussmann,Yi-Shan Wu,Andres R. Masegosa,Melih Kandemir
### Background
深层演员评论者算法已经达到了能够影响日常生活的技术水平，它们在通过用户反馈提高大语言模型性能方面发挥了重要作用。然而，这些算法在物理系统中的应用尚未广泛采用，主要原因是没有一种验证方案能够完全量化其故障的风险。
### Innovation
本文展示了可以通过最小化评估数据开发深层演员评论者算法的精确风险证书。从预训练策略收集的小型可行评估运行组合简单的PAC-Bayes理论，足以产生准确的风险证书。具体来说，使用最近引入的递归PAC-Bayes方法，将验证数据划分为部分，并递归构建每个部分预测器的PAC-Bayes边界，使用前一个部分的预测器作为基于数据的先验。
### Conclusion
研究结果在多个运动任务、演员评论者方法和策略熟练水平上的实验证明，这些风险证书足够精确，可以作为实用的应用考虑。
## 811. `cs.LG` - 通过进化算法在推理时对扩散模型进行对齐 [PDF](https://arxiv.org/pdf/2506.00299), [HTML](https://arxiv.org/abs/2506.00299)
### Authors
Purvish Jajal,Nick John Eliopoulos,Benjamin Shiue-Hal Chou,George K. Thiruvathukal,James C. Davis,Yung-Hsiang Lu
### Background
扩散模型是目前最先进的生成模型，但是在应用中常常无法满足诸如安全性约束或领域特定有效性等目标。现有的对齐技术要么需要梯度、内部模型访问或大量的计算资源，导致高计算需求，要么不支持某些目标。
### Innovation
我们提出了一种基于进化算法的推理时对齐框架。将扩散模型视为黑盒，并搜索其隐空间以最大化对齐目标。与无梯度和基于梯度的方法相比，在相同或更少的运行时间内，我们的方法在ImageReward得分上提高了3-35%。在Open Image Preferences数据集上，我们的方法在四种流行对齐目标上获得了具有竞争力的结果。在计算效率方面，我们只需要梯度基方法55%-76%的GPU内存，并且比梯度基方法快72%-80%。
### Conclusion
我们的方法能够在保持计算效率的同时实现高质量的对齐结果，特别是在对齐目标和计算资源之间取得良好平衡。
## 812. `cs.LG` - ENMA: Tokenwise Autoregression for Generative Neural PDE Operators [PDF](https://arxiv.org/pdf/2506.06158), [HTML](https://arxiv.org/abs/2506.06158)
### Authors
Armand Kassaï Koupaï,Lise Le Boudec,Louis Serrano,Patrick Gallinari
### Background
解决时间依赖的参数偏微分方程（PDEs）问题仍然是神经求解器面临的根本性挑战，特别是在需要广泛物理参数和动态通用化的情况下。当数据存有不确定性或不完整时，自然的方法是转向生成模型。
### Innovation
我们介绍了ENMA，这是一种生成神经运算器，用于模拟由物理现象产生的时空动态。ENMA通过生成掩码自回归变压器训练，该变压器使用流匹配损失，实现按令牌生成。不规则采样的空间观测通过注意力机制编码为均匀的潜在表示，进一步通过时空卷积编码器压缩。这使ENMA能够在推理期间进行上下文学习，既可以根据目标轨迹的过去状态，也可以根据具有相似动态的辅助上下文轨迹进行条件控制。结果是一个稳健且具备适应性的框架，能够应用于新的PDE领域，并支持单次训练的参数PDE代理模型。
### Conclusion
ENMA提供了一种新兴的、强大的求解策略，能够更好地应对PDE问题的不确定性及不完整数据挑战，实现了对新PDE领域的泛化以及对时间依赖参数PDE的单次训练代理模型的支持。
## 813. `cs.LG` - ConStellaration: 一个类似QI的等离子体边界数据集和优化基准 [PDF](https://arxiv.org/pdf/2506.19583), [HTML](https://arxiv.org/abs/2506.19583)
### Authors
Santiago A. Cadena,Andrea Merlo,Emanuel Laude,Alexander Bauer,Atul Agrawal,Maria Pascu,Marija Savtchouk,Enrico Guiraud,Lukas Bonauer,Stuart Hudson,Markus Kaiser
### Background
stellarators 是一种正在开发中的核聚变装置，旨在提供持续的碳基能源。它们的设计涉及到高维约束优化问题，需要昂贵的物理模拟和大量的专业知识。最近的在等离子体物理和开源工具方面的进展使得等离子体优化变得更加可行，但目前社区面临的主要瓶颈是没有标准化的优化问题以及能够驱动数据驱动方法的基础数据集，特别是适用于类似Quasi-isodynamic (QI)的等离子体边界配置。QI配置因其对电流驱动干扰的内在抗性被认为是一种有前景的商业化聚变路径。
### Innovation
本文发布了一个开放的数据集，包含多种类似QI的等离子体边界形状及其理想磁流体动力学(MHD)平衡和性能指标。这三个优化基准分别涵盖了单一目标几何优化问题，易于构建的QI等离子体边界，以及多目标理想MHD稳定的QI等离子体边界，用以探讨紧凑性和线圈简单性的权衡。此外，通过训练自己的模型可以有效生成新颖的可行配置，而无需查询昂贵的物理或真。
### Conclusion
通过公开发布数据集和基准问题，本研究旨在降低优化和机器学习研究人员参与等离子体设计的门槛，加速跨学科研究，以便将核聚变能源引入电网。
## 814. `cs.LG` - 行动分组和探索性数据收集在连续控制的行为克隆中提供指数级改进 [PDF](https://arxiv.org/pdf/2507.09061), [HTML](https://arxiv.org/abs/2507.09061)
### Authors
Thomas T. Zhang,Daniel Pfrommer,Chaoyi Pan,Nikolai Matni,Max Simchowitz
### Background
近年来，由于闭环中的动作序列预测以及专家演示的探索性增强，基于演示学习（即模仿学习）在机器人学习中的应用得到了广泛关注。然而，这些方法在连续环境中可能存在累积性的错误，这种错误可能随着任务时间轴的增长而呈指数级增长。
### Innovation
该论文通过理论分析提出了两种干预措施，即动作分组和探索性数据收集，证明了它们能够避免指数级累积错误。文章通过控制理论的稳定性机制解释了这些干预措施的优点，并通过实验证明了这些干预措施的有效性。
### Conclusion
该研究从理论上揭示了控制理论视角下模仿学习误差是如何出现的，并且在应用这些干预措施后，相比仅基于信息论考虑的方法，可以获得更紧密的统计保证。通过在流行机器人学习基准上的实验验证，该论文证明了这些干预措施在连续控制中的显著效果。
## 815. `cs.LG` - 使用约束学习调整大规模语言模型 [PDF](https://arxiv.org/pdf/2505.19387), [HTML](https://arxiv.org/abs/2505.19387)
### Authors
Botong Zhang,Shuo Li,Ignacio Hounie,Osbert Bastani,Dongsheng Ding,Alejandro Ribeiro
### Background
研究了在约束对齐问题中计算最佳大型语言模型（LLM）策略的问题，其目标是在满足次要效用约束的同时最大化主要奖励目标。尽管拉格朗日方法常用于约束对齐中的LLM策略搜索，但迭代的原始对偶方法经常无法收敛，而非迭代的对偶方法在参数空间也不能达到最优。
### Innovation
提出了使用拉格朗日对偶性开发一种迭代的对偶基对齐方法，该方法交替更新通过拉格朗日最大化对LLM策略进行更新，以及通过对偶下降对对偶变量进行更新。理论上，我们分析了原始值在分布空间与对偶值在LLM参数空间之间的原始-对偶差距。进一步量定了在接近最优对偶变量下的学习到的LLM策略相对于目标函数和约束函数的最优性差距。这些结果证明了基于对偶的对齐方法可以找到在LLM参数化差距之下的最优约束LLM策略。
### Conclusion
通过在PKU-SafeRLHF和Anthropic HH-RLHF数据集上的广泛实验，证明了方法的有效性和优点。
## 816. `cs.LG` - 流匹配邂逅PDEs：一种物理约束生成的统一框架 [PDF](https://arxiv.org/pdf/2506.08604), [HTML](https://arxiv.org/abs/2506.08604)
### Authors
Giacomo Baldan,Qiang Liu,Alberto Guardone,Nils Thuerey
### Background
生成机器学习方法，如扩散模型和流匹配，展示了在建模复杂系统行为和构建高效代理模型方面的巨大潜力。然而，这些方法通常隐式地从数据中学习潜在的物理规律。本文分析了现有方法的局限，提出了一种新的生成框架——基于物理的流匹配（PBFM），其中具体嵌入了物理约束，包括PDE残差和代数关系。
### Innovation
提出了PBFM，该方法在流匹配目标中显式嵌入了物理约束，并在训练时引入了时间展开，以提高噪声消除样本预测的准确性。PBFM联合最小化流匹配损失和基于物理的残差损失，无需调整其相对权重的超参数。文章还分析了最小噪声水平$tau_{text{min}}$在物理约束下的作用，并评估了一种随机采样策略以减少物理残差。通过在三个代表性的PDE问题上的广泛基准测试，该方法在物理残差准确性上达到了与流匹配相比最多8倍的效果，并且在分布准确性上明显优于现有算法。
### Conclusion
PBFM为物理学和工程学中的代理建模、不确定性量化和加速计算提供了一种原理性和高效的框架。
## 817. `cs.LG` - 在组合任务结构中对模式匹配及其限制的特性分析 [PDF](https://arxiv.org/pdf/2505.20278), [HTML](https://arxiv.org/abs/2505.20278)
### Authors
Hoyeon Chang,Jinho Park,Hanseul Cho,Sohee Yang,Miyoung Ko,Hyeonbin Hwang,Seungpil Won,Dohaeng Lee,Youbin Ahn,Minjoon Seo
### Background
尽管大语言模型（LLMs）表现出色，但它们的成功往往依赖于模式匹配的行为。然而，这些模式匹配行为在处理组合任务时会导致出域泛化的失败。现有行为研究通常采用允许多种泛化来源的任务设置，例如代数不变性和结构重复，这使难以明确和测试通过模式匹配进行泛化的精确表现和局限性。本文旨在解决这种模糊性。
### Innovation
本文首先将模式匹配形式化为功能性等价性，定义为输入子序列的配对，常数保持时始终导致相同结果。然后系统研究了仅解码器Transformer和Mamba在隔离此机制的受控任务中的表现。研究结果提供了预测性和量化的见解：（1）模式匹配的实例成功率可以用见证相关功能性等价性的上下文数量很好地预测。（2）证明了一种紧的数据复杂性界用于通过识别数据扩展法完美的领域内泛化中两跳结构的指数。（3）路径模糊性是一个结构性障碍：当变量通过多路径影响输出时，模型无法形成统一的中间状态表示，影响准确性和可解释性。（4）链式思维虽然减少了数据需求，但并不能解决路径模糊性。因此，本文提供了模式匹配的可预测和可验证边界，并为拆解混合泛化机制提供了基础诊断方法。
### Conclusion
本文为模式匹配提供了可预测和可验证的边界，并为拆解混合泛化机制提供了基础诊断方法，从而明确和测试通过模式匹配进行泛化的精确表现和局限性。研究结果与理论预测一致，并泛化到不同的架构和参数缩放中。
## 818. `cs.LG` - AutoDiscovery：通过贝叶斯惊奇进行开放式科学发现 [PDF](https://arxiv.org/pdf/2507.00310), [HTML](https://arxiv.org/abs/2507.00310)
### Authors
Dhruv Agarwal,Bodhisattwa Prasad Majumder,Reece Adamson,Megha Chakravorty,Satvika Reddy Gavireddy,Aditya Parashar,Harshit Surana,Bhavana Dalvi Mishra,Andrew McCallum,Ashish Sabharwal,Peter Clark
### Background
开放性自主科学发现（ASD）不仅依赖于回答问题，还依赖于知道问哪些问题。当前大多数ASD的工作是利用大型语言模型（LLMs）在特定目标设定下的探索，这些方法依赖于人类指定的研究问题来引导假设生成。然而，通过允许AI系统根据其自身标准驱动探索，科学发现可以进一步加速。现有的开放性ASD方法基于多样性的启发式或人类有趣性的主观代理来选择假设，但前者难以在通常庞大的假设空间中有效导航，后者则由于定义不精确而产生问题。
### Innovation
本文提出了一种名为AutoDiscovery的方法，通过贝叶斯惊奇驱动开放性的科学探索。该方法基于LLM在实验结果收集后关于假设的先验信念与后验信念之间的认识转变来量化认识论的变化。为高效探索嵌套假设的空间，该方法采用了基于惊奇度作为回报函数的蒙特卡洛树搜索策略，并结合逐步扩展技术。实验结果表明，在固定预算条件下，AutoDiscovery在21个真实世界数据集（涵盖生物学、经济学、金融和行为科学等领域）驱动的数据驱动发现中表现更优，生成了5%到29%更多的LLM认为惊奇的发现。进一步的人类评估表明，超过三分之二由系统生成的发现也令领域专家感到惊奇，这标志着向构建开放式ASD系统迈出了重要一步。
### Conclusion
本研究通过贝叶斯惊奇推动开放式科学探索的AutoDiscovery方法，展示了在有限预算下生成更具洞见发现的潜力。该方法的有效性和发现的创新性表明，开放式ASD系统的开发正朝着实现跨领域的自驱探索迈进。
## 819. `cs.LG` - 公平多代理多臂老虎机算法中的试探法 [PDF](https://arxiv.org/pdf/2506.14988), [HTML](https://arxiv.org/abs/2506.14988)
### Authors
Tianyi Xu,Jiaxin Liu,Nicholas Mattei,Zizhan Zheng
### Background
本文旨在解决在确保代理之间公平的同时，如何最大化系统的整体性能问题。传统的多臂老虎机（MAB）通常关注个体决策下的最优分配，但在多代理环境下，需要考虑多个代理的需求和公平性，使得信息有限的情况下的决策变得更加复杂。
### Innovation
本文提出了一种新颖的信息采集框架，称为探针框架，可以有选择性地收集关于选定臂的信息，然后再进行分配。对于已知回报分布的离线设置，采用了具可证明性能边界的经验主义探针算法。对于更复杂的在线设置，设计了一种在保持公平性的同时能够实现次线性后悔的算法。
### Conclusion
实验结果表明，本文提出的方法在合成和真实世界数据集上均表现出色，有效提高了系统的公平性和效率，优于基线方法。
## 820. `cs.LG` - 利用LLM代理赋能时间序列预测 [PDF](https://arxiv.org/pdf/2508.04231), [HTML](https://arxiv.org/abs/2508.04231)
### Authors
Chin-Chia Michael Yeh,Vivian Lai,Uday Singh Saini,Xiran Fan,Yujie Fan,Junpeng Wang,Xin Dai,Yan Zheng
### Background
大型语言模型（LLM）驱动的代理在自动化机器学习（AutoML）系统中已成为有效的规划工具。大多数现有的AutoML方法专注于自动化特征工程和模型架构搜索。而近期在时间序列预测方面的研究表明，轻量级模型常常可以达到或接近最佳性能。因此，研究者开始思考是否可以通过提升数据质量而非优化模型架构来改进时间序列数据的AutoML。
### Innovation
提出了一个以数据为中心的代理（DCATS），该代理利用与时间序列相关的元数据来清理数据并优化预测性能。该研究在其广泛的时间序列交通流量预测数据集上测试了四种时间序列预测模型，并显示出DCATS能够平均降低6%的预测误差率。
### Conclusion
结果表明，数据为中心的方法在时间序列预测的AutoML中有很大的潜力，DCATS在各模型和预测时间跨度上表现出显著的性能提高，证明了提升数据质量对预测准确性的重要性。
## 821. `cs.LG` - 统一噪声-曲率视角下的训练退化问题 [PDF](https://arxiv.org/pdf/2509.19698), [HTML](https://arxiv.org/abs/2509.19698)
### Authors
Gunbir Singh Baveja,Alex Lewandowski,Mark Schmidt
### Background
训练退化是指持续学习过程中，参数更新不再对优化目标产生改进，从而导致准确率停滞或下降的现象。现有方法通过Hessian秩、尖锐度级别、权重或梯度范数、梯度-参数比和单位符号熵等单一指标难以可靠预测这种现象。
### Innovation
本文从优化的角度分析训练退化问题，提出两种互补的指标：批处理大小感知的梯度噪声上限和曲率波动控制系统。结合这些指标，提出了一种针对每层自适应噪声阈值的步长调整策略，避免训练退化。该策略在不经过人工调优的情况下，能够适应性生成与手动设计的步长衰减策略相似的步长轨迹。
### Conclusion
所提出的步骤调整策略能够提高之前方法（如CONCATENATED RELU、Wasserstein正则化器和L2权重衰减）保持的准确性。实验结果表明，该策略在无需调整参数情况下能够避免训练退化，从而提高模型准确性。
## 822. `cs.LG` - 物理约束流匹配：具有硬约束的生成模型采样 [PDF](https://arxiv.org/pdf/2506.04171), [HTML](https://arxiv.org/abs/2506.04171)
### Authors
Utkarsh Utkarsh,Pengfei Cai,Alan Edelman,Rafael Gomez-Bombarelli,Christopher Vincent Rackauckas
### Background
近年来，深度生成模型被应用于受偏微分方程(PDEs)支配的物理系统中，提供了扩展仿真和具有不确定推理的能力。但是，物理约束的施加，如守恒定律（线性和非线性）和物理一致性，依然具有挑战性。现有方法往往依赖软惩罚或架构偏见，无法保证硬约束。
### Innovation
本文提出了一种名为物理约束流匹配(PCFM)的零样本推理框架，它在预训练的基于流的生成模型中强制执行任意非线性约束。PCFM通过在中间解状态上应用基于物理的修正来连续引导采样过程，同时也与学习到的流保持一致并满足物理约束。实验证明，PCFM在一系列PDE上优于不受约束和受约束的基本方法，包括那些包含冲击波、不连续性和尖锐特征的方程，同时确保最终解中精确的约束满足。
### Conclusion
本文的方法为在科学和通用生成模型中强制执行硬约束提供了一个灵活框架，特别是在约束满足至关重要的应用中。
## 823. `cs.LG` - 深度强化学习在意识到供应和容量风险的双源库存管理中的应用 [PDF](https://arxiv.org/pdf/2507.14446), [HTML](https://arxiv.org/abs/2507.14446)
### Authors
Defeng Liu,Ying Liu,Carson Eisenach
### Background
本文研究了如何通过利用干预模型高效地将强化学习（RL）应用于解决大规模随机优化问题。研究背景是在供应链优化中的多源多时期库存管理问题，需要在多种假设下学习和预测随机供应链过程的复杂性。
### Innovation
本文的关键创新在于，通过使用预训练的深度学习（DL）模型来模拟和组合随机过程，更好地探索解空间。特别地，使用深度RL模型学习和预测在不同假设下的随机供应链过程，引入约束协调机制来预测库存网络中交叉产品约束下的双重成本。
### Conclusion
本文方法将供应链过程分解为可扩展和可组合的深度学习模块，从而在大规模真实数据集上提高了性能。同时，为未来研究提出了开放问题，进一步探讨此类模型的效果。
## 824. `cs.LG` - In-context Learning中任务导向信息移除的机制 [PDF](https://arxiv.org/pdf/2509.21012), [HTML](https://arxiv.org/abs/2509.21012)
### Authors
Hakaze Cho,Haolin Yang,Gouki Minegishi,Naoya Inoue
### Background
In-context Learning（ICL）是一种基于现代语言模型（LMs）的新兴少量样本学习范式，但其内在机制尚未完全清楚。本文通过信息移除的新视角，探讨了ICL的工作机制。
### Innovation
研究发现，在零样本场景中，LMs将查询编码为包含所有任务信息的非选择性表示，在隐藏状态中，这导致任意输出而忽视了目标任务，导致几乎零的准确率。同时，通过低秩过滤器从隐藏状态中选择性地移除特定信息，能够有效地引导LMs向目标任务倾斜。在此基础上，通过精心设计的指标测量隐藏状态，发现少量样本ICL有效地模拟了这种任务导向的信息移除过程，选择性地从纠缠的非选择性表示中移除了冗余信息，并基于示范提高了输出。此外，确定了执行移除操作的关键注意力头，称其为去噪头，对这些头的消融实验表明，信息移除操作对ICL的准确性至关重要，尤其是在少量样本示范中缺少正确标签时。
### Conclusion
信息移除机制和去噪头在ICL的关键作用得到确认。去噪头在信息移除操作中起着关键作用，当信息移除操作被阻止时，ICL的准确率显著下降，尤其是当少量样本示范中缺少正确标签时。
## 825. `cs.LG` - 对称流动匹配在对称破坏分岔问题中的应用 [PDF](https://arxiv.org/pdf/2509.03340), [HTML](https://arxiv.org/abs/2509.03340)
### Authors
Fleur Hendriks,Ondřej Rokoš,Martin Doškář,Marc G.D. Geers,Vlado Menkovski
### Background
在非线性动力系统中，分岔现象常常会导致多种共存的稳定解，尤其是在打破对称性的情况下。传统确定性机器学习模型难以捕捉这种多样性，它们倾向于对多种解进行平均化，导致无法准确地表示对称性降低的结果。
### Innovation
本文提出了一种基于流动匹配的生成框架，旨在建模分岔结果的完整概率分布。方法能够直接采样多个有效解，并通过等变建模而保持系统对称性。通过引入对称匹配策略，预测输出与目标输出在群作用下保持一致，从而在等变环境中实现准确学习。
### Conclusion
通过在多种系统上进行验证，包括玩具模型和复杂的物理问题（如塌陷梁和Allen-Cahn方程），本文结果表明，流动匹配方法显著优于非概率性和变分方法，在捕捉多模态分布和对称性破坏分岔方面表现出色，为高维系统中的多稳态建模提供了一个有效且可扩展的解决方案。
## 826. `cs.LG` - 使用深度生成学习的条件分布平等性测试框架 [PDF](https://arxiv.org/pdf/2509.17729), [HTML](https://arxiv.org/abs/2509.17729)
### Authors
Siming Zheng,Tong Wang,Meifang Lan,Yuanyuan Lin
### Background
本文提出了一种用于两样本问题中条件分布平等性检验的一般框架，该框架最相关于协变量偏移和因果发现。该框架基于基于神经网络的生成方法和样本分割技术，将条件检验问题转换为无条件问题。
### Innovation
提出了一种基于生成分类准确性的条件分布平等性测试方法（GCA-CDET），通过引入新的与最近开发的偏移Rademacher复杂性相关的结果，建立了所学习生成器的收敛速率，并证明了在轻度假设下的测试一致性。
### Conclusion
我们进行了数值研究，包括合成数据集和两个实际数据集，证明了我们的方法的有效性。额外讨论了该框架的最优性，并在在线补充材料中提供。
## 827. `cs.LG` - 在Stackelberg均场博弈中的学习：一项非渐近分析 [PDF](https://arxiv.org/pdf/2509.15392), [HTML](https://arxiv.org/abs/2509.15392)
### Authors
Sihan Zeng,Benjamin Patrick Evans,Sujay Bhatt,Leo Ardon,Sumitra Ganesh,Alec Koppel
### Background
我们研究了Stackelberg均场博弈（MFG）中的策略优化问题。这是一种用于建模单一领头人在无限大量同质跟随者中的策略互动的层级框架。现有方法往往依赖于领头人和跟随者的独立性假设，使用样本效率低下，并且缺乏有限时间收敛保证。
### Innovation
我们提出了一种名为AC-SMFG的单循环演员批评算法，用于连续生成马尔可夫样本上操作。该算法交替执行领头人、代表跟随者和均场的（半）梯度更新，简单易行。我们证明了该算法在有限时间和样本下收敛到Stackelberg目标的稳定点。这是第一个具有非渐近收敛保证的Stackelberg MFG算法。我们的关键假设是“梯度对齐”条件，允许我们放松领头人和跟随者独立的假设。
### Conclusion
模拟结果在多个经济学环境中表明，AC-SMFG在策略质量和收敛速度上优于现有的多智能体和MFG学习基准。
## 828. `cs.LG` - 几何多色消息传递图神经网络在血脑屏障渗透性预测中的应用 [PDF](https://arxiv.org/pdf/2507.18926), [HTML](https://arxiv.org/abs/2507.18926)
### Authors
Trung Nguyen,Md Masud Rana,Farjana Tasnim Mukta,Chang-Guo Zhan,Duc Duy Nguyen
### Background
准确预测血脑屏障渗透性（BBBP）对于中枢神经系统（CNS）药物开发至关重要。尽管图神经网络（GNNs）在分子属性预测方面取得了进展，但它们通常依赖于分子拓扑结构而忽视了建模运输机制时至关重要的三维几何信息。
### Innovation
本文提出了几何多色消息传递图神经网络（GMC-MPNN），这是一种新颖的框架，通过明确结合原子级几何特征和长程相互作用，增强了标准的消息传递架构。我们的模型通过基于原子类型构建加权彩色子图来捕捉决定BBB渗透性的空间关系和化学背景。
### Conclusion
GMC-MPNN在三个基准数据集上的分类和回归任务中表现出色，取得了优于现有先进模型的性能。在化合物分类为可渗透/不可渗透（AUC-ROC为0.9704和0.9685）和连续渗透性值回归（均方误差RMSE为0.4609，皮尔逊相关性为0.7759）方面，GMC-MPNN展示了优越的表现。消融实验进一步量化了特定原子对相互作用的影响，表明模型的预测能力来源于其既学习常见又学习罕见但具有化学意义的功能模式的能力。将空间几何学整合到图表示中，GMC-MPNN设立了新的性能基准，并提供了一种更加准确和普适的药物发现工具。
## 829. `cs.LG` - 分布转移下的弱至强泛化 [PDF](https://arxiv.org/pdf/2510.21332), [HTML](https://arxiv.org/abs/2510.21332)
### Authors
Myeongho Jeon,Jan Sobotka,Suhwan Choi,Maria Brbić
### Background
随着未来的超级人类模型变得越来越复杂，准确监督其行为可能超出人类的能力范围。近期的研究表明，在这种情况下，简单的弱模型可以有效监督强模型，这一现象被称为弱至强泛化。然而，我们发现，当模型在分布发生变化时，盲目应用弱至强泛化会导致强模型的性能比其监督模型更差。
### Innovation
为了解决上述问题，我们提出了一种名为RAVEN的框架，它可以动态学习强模型参数和弱模型组合的最佳选择。RAVEN在图像分类、文本分类和偏好对齐任务中显示出其有效性，并在分布外任务中优于基线方法超过30%，同时在分布内任务中达到或超过了现有方法的性能。此外，我们的结果表明，RAVEN倾向于对更准确的弱模型赋予更高的权重，这证明了其自动识别可信监督的能力。
### Conclusion
RAVEN通过动态调整弱模型的组合，使得即使在分布发生变化的情况下，也能有效提高强模型的性能，特别是在不同类型的任务中均表现较好。这一研究提高了在复杂模型训练中的监督效率和模型稳定性。
## 830. `cs.LG` - 扩散模型在药物发现前沿：小分子与治疗性肽生成的综述 [PDF](https://arxiv.org/pdf/2511.00209), [HTML](https://arxiv.org/abs/2511.00209)
### Authors
Yiquan Wang,Yahui Ma,Yuhan Chang,Jiayao Yan,Jialin Zhang,Minnuo Cai,Kai Wei
### Background
扩散模型已经成为了生成模型领域的领头框架，有望彻底改变药物发现这一传统上既慢又昂贵的过程。本文对扩散模型在设计两种主要治疗模式——小分子和治疗性肽——中的应用进行了系统比较。
### Innovation
文章详细分析了统一框架的迭代去噪如何适应于不同的分子表示、化学空间以及设计目标。文章强调了小分子设计中确保化学合成性和治疗性肽设计中实现生物稳定性和适当折叠的重要性。尽管每个领域存在不同的挑战，但两者都面临着共享的瓶颈：高质量实验数据的稀缺性、不准确评分函数的依赖性以及实验验证的迫切需求。
### Conclusion
文章得出结论，扩散模型的全部潜力将通过跨模态差异的桥梁构建和将其整合进自动化闭环Design-Build-Test-Learn（DBTL）平台的方式得以释放，从而将范式从单纯的化学探索转变为对新颖治疗药物的即需即造工程。
## 831. `cs.LG` - g-DPO: 可扩展的偏好优化方法用于蛋白质语言模型 [PDF](https://arxiv.org/pdf/2510.19474), [HTML](https://arxiv.org/abs/2510.19474)
### Authors
Constance Ferragu,Jonathan D. Ziegler,Nicolas Deutschmann,Arthur Lindoulsi,Eli Bixby,Cradle ML Team
### Background
Direct Preference Optimization (DPO) 是一种有效的方法，用于使蛋白质语言模型与实验设计目标对齐。然而，DPO 面临一个可扩展性瓶颈：可能的训练对的数量随着带标签序列数量的平方增长，即使对于中等大小的数据集，这也导致培训时间变得不可接受。
### Innovation
我们引入了 g-DPO，一个框架，它通过(ii) 使用群组基的近似快速化似然计算，并通过(i) 使用序列空间聚类去除冗余对同时保留训练信号来解决这个问题。
### Conclusion
在三个蛋白质工程任务中，g-DPO 在体内和体外性能与标准 DPO 的性能统计上无法区分，但其收敛速度提高了1.7到5.4倍，并且随着数据集大小和基本突变地貌结构的提高而加快。
## 832. `cs.LG` - QiMeng-SALV: 基于信号感知学习的Verilog代码生成 [PDF](https://arxiv.org/pdf/2510.19296), [HTML](https://arxiv.org/abs/2510.19296)
### Authors
Yang Zhang,Rui Zhang,Jiaming Guo,Lei Huang,Di Huang,Yunpu Zhao,Shuyao Cheng,Pengwei Jin,Chongxiao Li,Zidong Du,Xing Hu,Qi Guo,Yunji Chen
### Background
大型语言模型（LLMs）在Verilog代码生成方面展示了 promising 的机会，这对于自动电路设计至关重要。然而，由于缺乏有意义的功能奖励，基于强化学习（RL）的功能正确代码生成受到限制。
### Innovation
本文提出了基于信号感知学习的Verilog代码生成（QiMeng-SALV）方法，通过利用功能正确输出信号的代码片段优化RL训练。QiMeng-SALV从错误模块中提取验证的信号感知实现，以增强有意义的功能奖励提取。该方法通过信号感知DPO在正确的信号级代码片段上进行了优化，从而避免了错误信号的噪声和干扰。QiMeng-SALV标志着Verilog代码生成从传统的模块级优化到精细的信号级优化的范式转变。
### Conclusion
实验表明，我们的方法在VerilogEval和RTLLM上达到了最先进的性能。7B参数模型的表现与DeepSeek v3 671B模型相当，并且显著优于训练数据相同的领先开源模型CodeV。我们的代码可在以下网址获得。
## 833. `cs.LG` - 分数匹配与局部固有维度之间的联系 [PDF](https://arxiv.org/pdf/2510.12975), [HTML](https://arxiv.org/abs/2510.12975)
### Authors
Eric Yeats,Aaron Jacobson,Darryl Hannan,Yiran Jia,Timothy Doster,Henry Kvinge,Scott Mahan
### Background
数据的局部固有维度(LID)在信号处理和学习理论中是一个基本的数量，但量化高维复杂数据的LID一直是历史上一个具有挑战性的任务。近期的研究发现，扩散模型通过其分数估计的频谱和在不同噪声扰动下的密度估计变化率，能够捕捉数据的LID。然而，这些方法要么需要扩散模型的大量前向传递，要么需要梯度计算，这些限制了它们在计算和内存受限的场景中的应用。
### Innovation
本文展示了LID是一个去噪分数匹配损失的下界，因此建议使用去噪分数匹配损失作为LID估算器。同时，等效的隐式分数匹配损失通过特征维度也近似LID，并且与最近的LID估算器FLIPD密切相关。实验结果表明，去噪分数匹配损失在不同问题规模和量化级别下，是一个高度竞争且可扩展的LID估算器，具有更好的准确性和内存占用。
### Conclusion
去噪分数匹配损失作为一种LID估算器，在大问题规模和高量化水平下表现出更优的准确性和更低的内存占用，是可扩展且竞争性的LID估算方法。
## 834. `cs.LG` - 为大型实例TSP提供基于超路径的针对性邻域搜索 [PDF](https://arxiv.org/pdf/2510.20169), [HTML](https://arxiv.org/abs/2510.20169)
### Authors
Tongkai Lu,Shuai Ma,Chongyang Tao
### Background
旅行商问题（TSP）是一个经典的NP难问题，受到了学术界和工业界的广泛关注。尽管神经网络方法被展示出了解决TSP的潜力，但在处理大规模实例时仍然面临着挑战，特别是在内存限制、全局热图、边权重或访问矩阵等方面的问题。这些问题还存在于生成高质量初始解的有效性和全局指导不足方面，难以有效探索广阔的搜索空间。
### Innovation
我们提出了一种针对大型实例TSP的“超路径引导邻域搜索”（HyperNS）方法。该方法借鉴了“先聚类再路线”的策略，首先使用稀疏热图图将TSP实例划分为簇，并将其抽象为超级节点，接着生成一个超路径来引导初始解和优化过程。这种方法通过聚焦与超路径相关的边来减少搜索空间，从而实现了更高效的优化。
### Conclusion
我们的方法在合成和真实世界数据集上进行的实验表明，我们的方法优于现有的神经网络方法，特别是在处理大规模实例时，能够显著减少与最优解的差距。
## 835. `cs.LG` - CRPS-LAM: 匹配边际的区域集合天气预报 [PDF](https://arxiv.org/pdf/2510.09484), [HTML](https://arxiv.org/abs/2510.09484)
### Authors
Erik Larsson,Joel Oskarsson,Tomas Landelius,Fredrik Lindsten
### Background
机器学习在天气预报中的应用越来越依赖于集合方法来提供概率预报。以扩散为基础的模型在区域天气预报（LAM）中表现出很强的性能，但在采样时间上仍然非常计算密集。现有的全球天气预报模型通过训练最低排名概率得分（CRPS）已经取得了很好的效果，因此本研究基于CRPS的目标训练了一个概率LAM预测模型——CRPS-LAM。
### Innovation
通过在一个前向传递过程中注入单个潜在噪声向量进行采样，CRPS-LAM在采样速度上比扩散模型提高了39倍。并且，CRPS-LAM能够保留细粒度的预报细节，即使在区域天气预报中，它的表现也与扩散模型的低误差相当，展示了CRPS-LAM作为有效概率区域天气预报方法的潜力。
### Conclusion
CRPS-LAM作为一种有效的区域集合天气预报方法，在采样速度大幅提升的同时，能够保持细粒度的预报细节且具有竞争力的预测精度，为区域天气预报提供了新的思路。
## 836. `cs.LG` - 深度神经网络中的类别学习：内部表示的内容和几何结构 [PDF](https://arxiv.org/pdf/2510.19021), [HTML](https://arxiv.org/abs/2510.19021)
### Authors
Laurent Bonnasse-Gahot,Jean-Pierre Nadal
### Background
在人类和其他动物中，类别学习可以增强刺激物之间差异的感知，尤其是在接近分类边界的情况下。这一现象被称为类别感知。研究者在人工神经网络上也观察到了类似的类别感知现象。之前的研究基于神经科学数据表明，这种空间扩展和压缩是高效学习的必然结果。作者将此理论框架扩展到人工网络，通过最小化贝叶斯成本来优化模型。
### Innovation
作者通过最小化贝叶斯成本来最大化类别和神经活动之间的相互信息，进而找到适当的投影空间，并建立具有适当度量（基于Fisher信息矩阵）的神经表征。这种学习使神经Fisher信息符合理论中的类别Fisher信息，揭示了这种学习诱导的神经空间在决策边界的扩展。此外，该论文将此方法论与信息瓶颈方法进行了对比，并展示了贝叶斯成本的偏差-方差分解。
### Conclusion
类学习导致神经空间在决策边界附近扩展。通过最大化相互信息来找到最有效的分类方向，优化后的Fisher信息矩阵能较好地与类别边界对齐，从而提高分类性能。
## 837. `cs.LG` - 在Transformer模型中逆排列学习的不可能性 [PDF](https://arxiv.org/pdf/2509.24125), [HTML](https://arxiv.org/abs/2509.24125)
### Authors
Rohan Alur,Chris Hays,Manish Raghavan,Devavrat Shah
### Background
本文研究了解码器独立试管中逆排列学习的问题。给定一个排列和已应用该排列的字符串，模型的任务是生成原始（“标准”）字符串。研究者认为，这个任务可以模拟在长上下文检索、多项选择问答和上下文学习等多种推理任务中的自然鲁棒性。
### Innovation
主要贡献在于证明了一个不可能定理：任意深度的解码器独立试管模型无法学习逆排列任务。此外，研究提供了两种替代构造，使得逆排列学习成为可能。这些结果强调了因果注意力掩码的基础作用，并揭示了编码器-解码器试管和更受欢迎的解码器独立试管架构之间表达能力的差距。
### Conclusion
研究者发现简单地使用“草稿标记”填充输入可以实现逆排列学习的构造。这可能表明链式思考提示，或更广泛地说，中间“思考”标记如何可以增强大规模语言模型的推理能力，即使这些标记本身并没有携带任何有意义的语义信息（例如，中间计算的结果）。”这些发现对理解Transformer模型的表达能力及优化语言模型的训练方法提供了新的洞察。
## 838. `cs.LG` - 基于资源感知并行推测性解码的协作大型语言模型推理 [PDF](https://arxiv.org/pdf/2511.01695), [HTML](https://arxiv.org/abs/2511.01695)
### Authors
Jungyeon Koh,Hyun Jong Yang
### Background
随着对设备端大型语言模型（LLM）推理需求的增加，特别是在资源受限的环境中，强调了高效移动边缘计算（MEC）解决方案的必要性。推测性解码提供了一种有希望的解决方案，通过在轻量级的草稿模型和强大的目标模型之间划分token生成工作，但面临的挑战包括通信开销和异步延迟。
### Innovation
该论文首次提出了一种统一框架，结合优化用户关联与资源分配（UARA）以支持高效的并行推测性解码。通过使用多代理深度强化学习算法来解决UARA问题。
### Conclusion
通过使用Sionna仿真器进行实验，我们的方法在不牺牲推理准确性的前提下，将端到端延迟减少最多28.0%和平均23.7%，实现MEC系统中的可扩展和低延迟LLM服务。
## 839. `cs.LG` - 硬标签，难样本：知道何时退缩的强大损失函数 [PDF](https://arxiv.org/pdf/2511.16512), [HTML](https://arxiv.org/abs/2511.16512)
### Authors
Nicholas Pellegrino,David Szczecina,Paul Fieguth
### Background
基准数据集和特制数据集中存在大量误标数据，这对基于监督学习的模型性能和泛化能力造成了负面影响。大多数检测标签错误的框架依赖于在受污染数据上训练模型，这减少了模型的泛化能力和错误检测的有效性，除非采用一种对标签错误具有鲁棒性的训练方案。
### Innovation
本文提出了两种新的鲁棒损失函数：模糊损失和分段零损失，通过降低或忽略难以分类的样本权重，增强对标签错误的鲁棒性。实验表明，这两种鲁棒损失函数在误标数据严重的数据集中检测错误的效果优于现有的鲁棒损失函数。
### Conclusion
通过使用这些鲁棒损失函数，机器学习从业者可以更有效地识别、去除或纠正其训练数据中的错误。进一步的消融实验验证了该方法对不同类型污染数据和不同错误检测框架的广泛适用性。
## 840. `cs.LG` - HardFlow：借助轨迹优化实现流匹配模型的硬约束采样 [PDF](https://arxiv.org/pdf/2511.08425), [HTML](https://arxiv.org/abs/2511.08425)
### Authors
Zeyang Li,Kaveh Alim,Navid Azizan
### Background
扩散和流匹配方法已成为生成建模的强大工具，能够成功捕捉复杂的数据分布并在推断时提供灵活的引导。然而，许多下游应用要求生成样本必须满足严格的约束条件（例如，机器人轨迹必须避免障碍物），而不仅仅是简单的引导。现有的基于投影的方法将整个采样路径约束在约束流形上，这既过于严格，又会降低样本质量。
### Innovation
本文提出了一个新的框架，将硬约束采样问题重新定义为轨迹优化问题。核心创新在于利用数值最优控制方法确保在最终时间满足约束条件。通过利用流匹配模型的内在结构并采用模型预测控制技术，将复杂的约束优化问题转化为可高效求解的近似问题。此外，这种轨迹优化视角提供了超越简单约束满足的灵活性，可以包括积分成本以最小化分布偏移和终端目标以进一步改善样本质量，这一切都在统一框架中实现。
### Conclusion
通过控制理论分析，我们证明了我们可求解的近似模型与理想模型之间的逼近误差界。广泛的实验表明，我们的算法HardFlow在约束满足与样本质量方面均优于现有方法。
## 841. `cs.LG` - 通过分段获得高斯过程回归中的实用全局和局部界 [PDF](https://arxiv.org/pdf/2511.09144), [HTML](https://arxiv.org/abs/2511.09144)
### Authors
Junyi Liu,Stanley Kok
### Background
高斯过程回归（GPR）是一种流行的非参数贝叶斯方法，能够提供预测不确定性估计，并广泛应用于安全关键应用中。尽管先前的研究引入了各种不确定性边界，但大多数现有方法需要访问特定的输入特征，依赖于后验均值和方差估计或超参数的调优。这些限制阻碍了鲁棒性，并未能捕捉模型的整体行为。
### Innovation
本文提出了一种基于分段的框架，用于估计未见数据上期望极端值的上界和下界，无需访问特定的输入特征。对于常用核函数（如RBF和Matérn），提出了针对特定内核的改进界限，这些界限比通用构造更紧。此外，通过避免分析性放松来进一步提高数值紧度。此外，还开发了一种新颖的局部不确定性量化方法，在指定的输入上量化不确定性。
### Conclusion
实验结果验证了理论发现，证明了本方法在合成和真实数据集上均优于现有方法。
## 842. `cs.LG` - 聚散两依 serializer：LLM 图推理模型的不变性和泛化能力 [PDF](https://arxiv.org/pdf/2511.10234), [HTML](https://arxiv.org/abs/2511.10234)
### Authors
Daniel Herbst,Lea Karbevska,Divyanshu Kumar,Akanksha Ahuja,Fatemeh Gholamzadeh Nasrabadi,Fabrizio Frasca
### Background
基于大型语言模型（LLMs）的图推理器虽然前景广阔，但它们缺乏图表示对称性的内在不变性。这些推理器在处理序列化的图表示时，例如在重新索引节点、重新排序边或更改格式时，会产生不同的输出，这引发了关于其稳健性的担忧。
### Innovation
论文系统分析了这些影响，并研究了微调对编码敏感性和未见任务泛化能力的影响。提出了一个有原则的分解方法，将图序列化分解为节点标签、边编码和语法，评估了这些因素的变化对LLM稳健性的影响。此外，还引入了一组新的谱任务，以进一步评估微调推理器的泛化能力。研究表明，较大的（未微调）模型更稳健。微调可以减少对节点重新标记的敏感性，但可能会增加对结构和格式变化的敏感性，而微调不能始终提高未见任务的性能。
### Conclusion
研究结果表明，更大（未微调）的模型更稳健。尽管微调可以减少对节点重新标记的敏感性，但它可能会增加对结构和格式变化的敏感性，而且不能始终提高对未见任务的性能。
## 843. `cs.LG` - 基于自调整警觉参数的自适应共振理论拓扑聚类算法 [PDF](https://arxiv.org/pdf/2511.17983), [HTML](https://arxiv.org/abs/2511.17983)
### Authors
Naoki Masuyama,Yuichiro Toda,Yusuke Nojima,Hisao Ishibuchi
### Background
在静态和非静态的数据分布下进行聚类（数据分布保持静止或随时间演变），需要能够适应分布变化同时保持先前学习的聚类结构的模型。现有聚类算法在这方面存在挑战。
### Innovation
本文提出了一个基于自适应共振理论（ART）的拓扑聚类算法，通过多样性驱动的自适应机制自动调整其重新计算间隔和警觉阈值，实现无超参数学习，能够维护聚类结构的稳定性和连续性，特别是在动态环境中的表现。
### Conclusion
在24个实际数据集上的实验结果表明，所提出的算法在聚类性能和连续学习能力方面均优于现有最先进的方法。结果强调了所提参数自适应机制的有效性，能够减轻灾难性遗忘，并在演变的数据流中保持一致的聚类。
## 844. `cs.LG` - 生成对抗后训练减轻实时人机音乐互动中的奖励劫持问题 [PDF](https://arxiv.org/pdf/2511.17879), [HTML](https://arxiv.org/abs/2511.17879)
### Authors
Yusong Wu,Stephen Brade,Teng Ma,Tia-Jane Fowler,Enning Yang,Berker Banar,Aaron Courville,Natasha Jaques,Cheng-Zhi Anna Huang
### Background
大多数生成AI的应用涉及顺序交互，用户输入提示等待回应，而反应时间和适应性不是重要因素。相比之下，实时即兴创作需要实时协调和适应，且无法预见对方的操作，但需保持多样性以维持创造力的流动。尽管强化学习在训练后可以通过在线互动进行有效适应，但它常常通过利用连贯性奖励来减少输出多样性，这种现象被称为'奖励劫持'，在音乐即兴创作中尤其有害，因为音乐创造力依赖于动态变化和相互响应。
### Innovation
本文提出了一种对抗训练方法，在策略生成轨迹上进行对抗训练以减轻强化学习后训练中的奖励劫持问题，用于旋律伴奏。通过让随时间共同进化的判别器分离策略轨迹与数据分布，并让策略在最大化判别器输出的同时最大化连贯性奖励，防止过度简化的输出。该方法在模拟环境中以及部署在实时互动系统中与专家乐手进行用户研究，结果显示增强了输出多样性、和声连贯性、适应速度以及用户自主性。
### Conclusion
我们的结果证明了一种简单而有效的方法来减轻强化学习后训练中生成序列模型中的奖励劫持问题。此方法验证了生成对抗后训练的有效性，提高了实时人机音乐互动的质量和创造力。
## 845. `cs.LG` - 通过数据驱动的代理模型增强核反应堆核心模拟 [PDF](https://arxiv.org/pdf/2511.16148), [HTML](https://arxiv.org/abs/2511.16148)
### Authors
Perceval Beja-Battais(CB),Alain Grossetête,Nicolas Vayatis(CB)
### Background
近年来，随着可再生能源的迅速增长，核电厂（NPPs）需要提高灵活性以匹配这些变化。为此，Framatome开发了操作员辅助预测系统（OAPS），通过模型预测控制（MPC）解决了这一问题。该研究旨在通过数据驱动的模拟方案改进MPC方法。
### Innovation
本研究通过引入两种代理模型作为替代的仿真方案，提高了核反应堆核心模拟的速度，这两种模型能快速整合复杂的动态，计算时间最多减少了1000倍，同时结合了数据驱动和物理信息的方法。
### Conclusion
通过使用两种代理模型，本研究展示了如何通过数据驱动的模拟方案以极低的计算时间有效地模拟核反应堆核心的复杂动态。
## 846. `cs.LG` - 高容量核Hopfield网络吸引子景观的自组织及谱机制 [PDF](https://arxiv.org/pdf/2511.13053), [HTML](https://arxiv.org/abs/2511.13053)
### Authors
Akira Tamamori
### Background
核基学习方法可以显著提高Hopfield网络的存储容量，但其背后的动力学机制尚未完全理解。
### Innovation
这篇文章通过结合吸引子景观的几何分析与核机器的谱理论，引入了“尖锋锐度”这一新度量，揭示了在高负载条件下网络最大鲁棒性的‘优化脊梁’，并展示了该现象源于特定的权重谱重组（称为‘谱集中’），这一分析显示，处于脊梁上的网络会自我组织为临界状态：领先特征值被放大以最大化全局稳定性（直接力），而次要特征值被保存以维持高记忆容量（间接力）。
### Conclusion
这些发现为高容量关联记忆的形成提供了一个完整的物理图景，表明最优性能是通过将系统调谐到谱‘黄金区域’之间来实现的，介于秩坍缩和扩散之间。
## 847. `cs.LG` - 多智能体交叉熵方法结合单调非线性评价分解 [PDF](https://arxiv.org/pdf/2511.18671), [HTML](https://arxiv.org/abs/2511.18671)
### Authors
Yan Wang,Ke Deng,Yongli Ren
### Background
文章背景介绍了现有的多智能体强化学习（MARL）通常采用集中训练分散执行（CTDE）方法，通过集中批评者利用全局信息指导分散的行为者。然而，集中式与分散式之间的不匹配（CDM）会因一个智能体的次优行为而影响其他智能体的训练效果。先前的方法通过价值分解来缓解这种匹配问题，但线性分解在保留表征能力的同时允许每个智能体的梯度，而非线性分解则虽然提高了表征能力，但需要集中式的梯度，从而引入了新的匹配问题。
### Innovation
为了克服上述的折中，文章提出了一种多智能体交叉熵方法（MCEM），结合了单调非线性评价分解（NCD）。MCEM 通过增加高价值联合动作的概率来更新策略，从而排除次优行为。为了提高样本效率，文章还扩展了离策略学习，采用了修改后的 k 步回报和 Retrace 方法。分析和实验表明，在连续和离散动作基准测试中，MCEM 比最先进的方法表现更优。
### Conclusion
实验结果表明，MCEM 在不同的动作基准测试中表现优于现有的最先进的方法，通过结合单调非线性评价分解使得多重智能体学习更高效且可控。
## 848. `cs.LG` - scipy.spatial.transform: Python 中不同框架下的不同可微3D变换 [PDF](https://arxiv.org/pdf/2511.18157), [HTML](https://arxiv.org/abs/2511.18157)
### Authors
Martin Schuck,Alexander von Rohr,Angela P. Schoellig
### Background
现代机器人学、视觉和仿真领域的不同iable机器学习管道中，三维刚体变换（如旋转和平移）至关重要。然而，在 SO(3) 上实现这些变换时，由于轴约定、标准化、组成一致性及边缘情况中的细微错误等问题，容易出现数值和数学上的错误。虽然 SciPy 的 spatial.transform 模块是一个严格测试的 Python 实现，但其历史仅支持 NumPy，限制了其在 GPU 加速和自动微分工作流程中的采用。
### Innovation
该研究对 SciPy 的 spatial.transform 功能进行了全面改版，使其与任何实现 Python 数组 API 的数组库兼容，包括 JAX、PyTorch 和 CuPy。修订后的实现保留了现有的 SciPy 接口，同时支持 GPU/TPU 执行、JIT 编译、批量向量化和通过所选后端的原始自动微分进行的差分。这一基础展示了在不同可微系统和 ML 中支持不同框架下的不同可微 3D 变换。
### Conclusion
该贡献已合并到 SciPy 主分支，并将在下一个版本中发布，为不同框架下的不同可微 3D 空间数学提供了框架中立的生产级基础。
## 849. `cs.LG` - 使用一阶 oracle 的非凸-强凸双层优化的复杂度下界 [PDF](https://arxiv.org/pdf/2511.19656), [HTML](https://arxiv.org/abs/2511.19656)
### Authors
Kaiyi Ji
### Background
虽然双层优化的上界保证已经广泛研究，但由于双层结构的复杂性，关于下界的研究进展有限。本研究聚焦于平滑非凸-强凸设置，并开发出新的困难实例，以在确定性和随机一阶 oracle 模型下提供非平凡的下界。
### Innovation
在确定性情况下，证明了任何零容忍度的一阶算法需要至少 $text{textOmega}(text{κ}^{3/2}text{ε}^{-2})$ 次 oracle 调用来找到 $text{ε-}$ 准确的稳定点，这改进了单一层次非凸优化和非凸-强凸最小最大问题已知的最优下界。在随机情况下，展示了至少需要 $text{textOmega}(text{κ}^{5/2}text{ε}^{-4})$ 次随机 oracle 调用，进一步加强了相关设置中最优瓶颈。
### Conclusion
本研究揭示了当前双层优化上界和下界之间的巨大差距，并指出即使简化的情况，如二次下层目标函数，也应进一步研究以理解标准一阶 oracle 下双层优化的最佳复杂性。
## 850. `cs.LG` - 考虑风能利用与削峰填谷的电热联合系统优化调度 [PDF](https://arxiv.org/pdf/2511.15250), [HTML](https://arxiv.org/abs/2511.15250)
### Authors
Jin Ye,Lingmei Wang,Shujian Zhang,Haihang Wu
### Background
随着全球能源转型和可再生能源的快速发展，新型能源集成和多重不确定性条件下联合电力-热力系统的调度优化挑战日益突出。
### Innovation
本文提出了一种基于改进的Dual-Delay Deep Deterministic Policy Gradient (PVTD3)算法的智能调度方法。通过引入电网电力购买变化的惩罚项实现系统优化。
### Conclusion
研究结果表明，相较于传统的TD3算法，PVTD3算法在三种典型场景（可再生能源渗透率分别为10%、20%和30%）下分别将系统的综合成本降低了6.93%、12.68%和13.59%，并减少了平均电网电力购买波动幅度12.8%。此外，该算法还减少了低温热储存罐的末端状态值7.67-17.67个单位，同时保持高温罐在3.59-4.25的安全操作范围内。多场景对比验证表明，所提出的算法不仅在经济效率和电网稳定性方面表现出色，还在能源存储装置管理方面具有优越的可持续调度能力。
## 851. `cs.LG` - SculptDrug : 基于空间条件的贝叶斯流模型在结构导向药物设计中的应用 [PDF](https://arxiv.org/pdf/2511.12489), [HTML](https://arxiv.org/abs/2511.12489)
### Authors
Qingsong Zhong,Haomin Yu,Yan Lin,Wangmeng Shen,Long Zeng,Jilin Hu
### Background
结构导向药物设计（SBDD）已经成为药物发现领域中的一种流行方法，通过利用三维蛋白质结构来生成药物配体。现有的生成模型面临一些关键挑战：（1）如何整合边界条件约束，（2）如何整合分层次的空间结构条件，（3）如何确保空间建模的准确性。
### Innovation
SculptDrug 是一种基于贝叶斯流网络的具备空间条件感知机制的生成模型。它首先遵循贝叶斯流网络框架，并采用逐级去噪策略来确保空间建模的准确性，逐步改进原子位置并增强局部相互作用，以实现精确的空间对齐。其次，引入边界感知模块，将蛋白质表面约束整合进生成过程，以确保生成的配体在几何上与目标蛋白质兼容。最后，设计了层级编码器，能够捕捉全局结构上下文并保留精细的分子相互作用，确保配体-蛋白质构象的总体一致性和准确性。
### Conclusion
我们在CrossDocked数据集上对SculptDrug进行了评估，实验结果表明SculptDrug优于最先进的基线方法，显示出空间条件感知建模的有效性。
## 852. `cs.LG` - 具有学习的伯努利不确定性深度学习框架的涡扇发动机剩余使用寿命预测中的不确定性感知 [PDF](https://arxiv.org/pdf/2511.19124), [HTML](https://arxiv.org/abs/2511.19124)
### Authors
Krishang Sharma
### Background
在航空航天故障预测中，准确的剩余使用寿命（RUL）预测并伴随不确定性量化仍然是一个关键性挑战。当前航空器维护决策中，对RUL及其不确定性进行精确预测对于确保安全具有重要意义。
### Innovation
该研究引入了一种新颖的不确定性感知深度学习框架，通过概率建模直接学习伯努利不确定性，该方法在现有CMAPSS相关文献中未曾探索。该架构采用多尺度Inception块提取时间模式，双向长短期记忆网络进行序列建模，并使用双层注意力机制同时在传感器和时间维度上操作。创新之处在于输出层采用贝叶斯方法，可以预测RUL的均值和方差，使模型能够学习数据固有的不确定性。进一步的预处理包括基于条件的聚类、小波去噪和智能特征选择。
### Conclusion
该框架在NASA CMAPSS基准测试（FD001-FD004）上展示了相对竞争力的总体性能，尤其是对关键区域（RUL <= 30 cycles）的性能表现更为出色，其RMSE值相较于传统方法提升了25-40%。同时，学习到的不确定性提供了93.5%到95.2%的95%置信区间覆盖度，这使得风险感知维护计划成为可能，这在现有的CMAPSS文献中是前所未有的。
## 853. `cs.LG` - PrefixGPT: Prefix Adder Optimization by a Generative Pre-trained Transformer [PDF](https://arxiv.org/pdf/2511.19472), [HTML](https://arxiv.org/abs/2511.19472)
### Authors
Ruogu Ding,Xin Ning,Ulf Schlichtmann,Weikang Qian
### Background
前缀加法器在计算密集型应用中因其高速性能而广泛应用。然而，由于严格的硬件设计规则和巨大的设计空间，设计优化的前缀加法器极具挑战性。
### Innovation
我们引入了PrefixGPT，这是一种生成式预训练变换器，可以从零开始直接生成优化的前缀加法器。模型采用定制的解码器-only变换器架构，首先在合成的有效前缀加法器语料上进行预训练以学习设计规则，然后进行微调以探索和优化设计。与现有工作相比，PrefixGPT不仅找到了一个新的最优设计，并且改善了面积延迟积（ADP），最高提升了7.7%的改善，并且在探索质量上表现出优越性，使平均ADP降低了高达79.1%，这展示了GPT风格模型首先掌握复杂硬件设计原理并用于更高效的优化设计的潜力。
### Conclusion
PrefixGPT展示了GPT风格模型在复杂硬件设计原理上的掌握并应用于更高效的设计优化的潜力，通过直接生成优化的前缀加法器，不仅能找到最优设计，还能显著降低设计的面积延迟积。
## 854. `cs.LG` - QiMeng-CRUX: Narrowing the Gap between Natural Language and Verilog via Core Refined Understanding eXpression [PDF](https://arxiv.org/pdf/2511.20099), [HTML](https://arxiv.org/abs/2511.20099)
### Authors
Lei Huang,Rui Zhang,Jiaming Guo,Yang Zhang,Di Huang,Shuyao Cheng,Pengwei Jin,Chongxiao Li,Zidong Du,Xing Hu,Qi Guo,Yunji Chen
### Background
现有的硬件描述语言（HDL）生成方法往往依赖于自由形式的自然语言描述，这种描述存在模糊性、冗余性和无序性的问题，这给后续的Verilog代码生成带来了巨大挑战。
### Innovation
提出了一种结构化的中间表示CRUX，它捕捉用户意图的核心语义并组织表达，以便进行精确的Verilog代码生成。设计了一个两阶段的训练框架，包括联合表达建模和双空间优化，以提高CRUX和Verilog代码的质量。
### Conclusion
在多个Verilog生成基准测试中，CRUX-V模型展示了优于通用模型的性能，尤其是在具有挑战性设计任务中。CRUX表示空间在其他代码模型的输入提示中具有可转移性，有助于缩小自由形式自然语言描述与精确Verilog生成之间的差距。
## 855. `cs.LG` - TREASURE: 基于Transformer的基础模型以理解高交易量数据 [PDF](https://arxiv.org/pdf/2511.19693), [HTML](https://arxiv.org/abs/2511.19693)
### Authors
Chin-Chia Michael Yeh,Uday Singh Saini,Xin Dai,Xiran Fan,Shubham Jain,Yujie Fan,Jiarui Sun,Junpeng Wang,Menghai Pan,Yingtong Dou,Yuzhong Chen,Vineeth Rakesh,Liang Wang,Yan Zheng,Mahashweta Das
### Background
支付网络构成了现代商业的骨架，每天生成大量的交易记录。正确地建模这些数据可以实现异常行为检测和消费者层面的洞察，为个性化体验提供支持，从而改善人们的生活。因此，需要一种能够高效处理此类数据的强大模型。
### Innovation
TREASURE是一种多用途的Transformer基础模型，专为交易数据设计。该模型能够同时捕捉消费者行为和支付网络信号（如响应代码和系统标志），并且具有三个关键功能：1）包含静态和动态属性专用子模块的输入模块；2）高效的训练机制，用于预测高基数分类属性；3）作为一种独立模型提高了异常行为检测性能，作为一种嵌入提供者增强了推荐模型。
### Conclusion
通过广泛的研究、基线与生产模型的对比以及案例研究，展示了开发TREASURE模型的重要发现。TREASURE作为一个独立模型，将异常行为检测性能提高了111%；作为一种嵌入提供者，将推荐模型提高了104%。
## 856. `cs.LG` - UniGame：使统一多模态模型成为自己的对手 [PDF](https://arxiv.org/pdf/2511.19413), [HTML](https://arxiv.org/abs/2511.19413)
### Authors
Zhaolong Su,Wang Lu,Hao Chen,Sharon Li,Jindong Wang
### Background
统一多模态模型（UMMs）在理解和生成任务上展现了出色性能，但其内部仍存在理解偏向紧凑嵌入而生成偏向重建丰富的表示这一基本矛盾，这导致了决策边界不一致，跨模态一致性下降以及在分布性和对抗性扰动下的脆弱性增加。
### Innovation
提出了自对抗后训练框架UniGame，通过共享词元接口处应用轻量级扰动器，使生成分支主动寻求并挑战脆弱的理解，将模型本身变成其自己的对手。实验表明，UniGame显著提高了连贯性（+4.6%），对理解（+3.6%）、生成（+0.02）以及离分布和对抗鲁棒性（+4.8%和+6.2%在NaturalBench和AdVQA中的提升）都有显著改善。该框架对于各种架构而言是通用的，引入的额外参数少于1%，并且与现有后训练方法相得益彰。
### Conclusion
这些结果表明，对抗自博弈是一种增强未来多模态基础模型中一致性和稳健性的通用且有效的原则。框架已在GitHub上开源。
## 857. `cs.LG` - 助因子 federated 学习：用于异质数据个性化优化的辅助因子 federated 学习 [PDF](https://arxiv.org/pdf/2312.04281), [HTML](https://arxiv.org/abs/2312.04281)
### Authors
Feifei Wang,Huiyun Tang,Yang Li
### Background
联邦学习是一种新兴的分布式机器学习框架，旨在保护数据隐私。数据异质性是联邦学习中的一大核心挑战，可能会严重降低深度神经网络的收敛速度和预测性能。针对这一问题，本文开发了一种新颖的个性化联邦学习框架 FedSplit，用于处理异质数据。该框架基于一个发现：不同客户端的数据中包含共性知识和个人知识。这是为了在每个神经网络层中将隐藏元素拆分为共享和个性化组的基础上构建的。
### Innovation
本文提出了一种名为 FedSplit 的新颖个性化联邦学习框架，该框架通过将每个神经网络层中的隐藏元素拆分为共享和个性化组来处理数据异质性问题。通过这种方法，建立并优化了一个新的目标函数。实验和理论证明，与标准的联邦学习方法相比，FedSplit 具有更快的收敛速度，并且其泛化界也被研究了。为了实际在真实数据集上实现提出的 FedSplit 方法，引入了因子分析来辅助隐藏元素的解耦，最终提出了 FedFac 模型。模拟研究结果表明，使用因子分析能够很好地恢复底层的共享/个性化分解，而 FedFac 在多个真实数据集上的预测性能也得到了验证。
### Conclusion
本文提出了一种基于因子分析的个性化联邦学习框架 FedFac，该框架有效解决了联邦学习中的数据异质性问题。FedFac 的收敛速度更快，并且在多个真实数据集上的预测性能优于多项最先进的联邦学习方法。
## 858. `cs.LG` - 高效大型语言模型的扩展 [PDF](https://arxiv.org/pdf/2402.14746), [HTML](https://arxiv.org/abs/2402.14746)
### Authors
B.N. Kausik
### Background
近年来，大型语言模型（LLMs）拥有数十亿参数，消耗巨大的资源。现有研究表明，Transformer的AI扩展定律表明，参数数量必须与数据规模成线性增长。为了更有效地利用资源，研究人员寻求具有较少参数但仍能达到所需精度的高效大型语言模型。
### Innovation
本文提出了递归Transformer，结合了Transformer的有效性和递归网络的高效性，通过固定宽度的滑动窗口逐层应用单个Transformer层在输入序列上。递归Transformer在序列长度上以线性时间运行，内存高效且易于大型批次的并行处理，能学会在语言任务中忘记历史信息，在长距离任务中积累历史信息，还适合采用渐进式训练来解决梯度消失问题。
### Conclusion
实验结果显示，递归Transformer在基准测试中表现良好，表明这种模型架构更加高效，为低参数复杂度的高效大型语言模型提供了新的扩展方式。
## 859. `cs.LG` - 通过近似点算法的催化剂框架在量子线性系统问题中的应用 [PDF](https://arxiv.org/pdf/2406.13879), [HTML](https://arxiv.org/abs/2406.13879)
### Authors
Junhyung Lyle Kim,Nai-Hui Chia,Anastasios Kyrillidis
### Background
求解线性方程组是一个基础问题，但在高维情况下，经典算法的计算量会非常大。现有的量子算法可以在问题维度上提供指数级加速，但优势受到系数矩阵条件数的限制。
### Innovation
本文提出了一种基于经典近似点算法的新量子算法，可视为一种元算法，通过已有的QLSP求解器逆矩阵，直接近似解向量而非近似逆矩阵。通过精细选择步长 η，提出的方法可以有效预处理线性系统，减轻依赖于条件数的限制。这是一个具有可调参数 η 和初始化 x_0 的迭代框架，允许控制运行时间和近似误差之间的权衡。
### Conclusion
本文提出的算法是在量子线性系统问题中，首次利用可调参数 η 和初始值 x_0 控制运行时间和近似误差之间权衡关系的迭代框架。
## 860. `cs.LG` - LTD: Low Temperature Distillation for Gradient Masking-free Adversarial Training [PDF](https://arxiv.org/pdf/2111.02331), [HTML](https://arxiv.org/abs/2111.02331)
### Authors
Erh-Chung Chen,Che-Rung Lee
### Background
对抗训练是一种广泛采用的方法，用于增强神经网络模型对对抗攻击的鲁棒性。尽管这种方法有效，但本文指出，图像分类中的基本假设之一，即使用独热标签表示数据，会使得模型容易受到攻击。在实际数据集中，数据往往具有模糊性，样本表现出多种类别的特征，导致独热标签表示不够精确。
### Innovation
论文提出了一种新的方法——低温度蒸馏（LTD），通过在教师模型中采用较低的温度，而在学生模型中保持固定的较高温度，来改进标签表示。这种方法不仅修正了数据分布的假定，还增强了模型的鲁棒性，并避免了防御蒸馏中常见的梯度屏蔽问题。
### Conclusion
实验结果表明，LTD方法能够与现有的框架无缝结合，分别在CIFAR-10、CIFAR-100和ImageNet数据集上达到58.19%、31.13%和42.08%的鲁棒准确率，且无需额外的数据集。
## 861. `cs.LG` - MoRE：从冻结预训练转换器生成鲁棒的多组学表示 [PDF](https://arxiv.org/pdf/2511.20382), [HTML](https://arxiv.org/abs/2511.20382)
### Authors
Audrey Pei-Hsuan Chen
### Background
多组学数据代表学习面临的挑战包括极端的维度、模态的异质性和群体特异性批次效应。尽管在生物序列建模中预训练的转换器表现出广泛的一般化能力，但它们在多组学整合中的应用仍未被充分探索。
### Innovation
我们提出了MoRE（多组学表示嵌入），这是一种框架，利用冻结的预训练转换器将异质检测对齐到共享的潜在空间中。MoRE采用了参数高效的微调（PEFT）策略，优先考虑跨样本和跨模态对齐，而非简单的序列重建。具体来说，MoRE附加了轻量级、模态特定的适配器和任务适应性融合层，并优化了一个掩码建模目标，结合监督对比和批次不变的对齐损失，从而生成具有保持结构的嵌入，在未见过的细胞类型和平台上具有泛化能力。
### Conclusion
我们的实验结果表明，MoRE在保持批处理鲁棒性和生物学保守性方面表现出竞争力，同时比完全微调的模型显著减少了可训练参数的数量。这项工作将MoRE定位为通用于组学基础模型的实用步骤。
## 862. `cs.LG` - 使用图神经网络和蒙特卡洛树搜索的地球观测卫星调度 [PDF](https://arxiv.org/pdf/2408.15041), [HTML](https://arxiv.org/abs/2408.15041)
### Authors
Antoine Jacquet,Guillaume Infantes,Emmanuel Benazera,Vincent Baudoui,Jonathan Guerra,Stéphanie Roussel
### Background
地球观测卫星规划（EOSP）是一个具有显著实践意义的优化问题。一组要求的观测必须安排在灵活的地球观测卫星上，同时满足其可见窗口和机动约束（在连续观测之间施加不同延迟）。此外，该问题通常是超订的：可以实现的观测比候选观测多得多，因此必须选择一组将要执行的观测以最大化其累积效益，并提出这些观测的可行性计划。
### Innovation
这项工作基于图神经网络（GNNs）和深度强化学习（DRL）提出了一种新的技术，用于选择和调度观测。GNNs用于从表示EOSP实例的图中提取相关信息，DRL引导寻找最优调度方案。还增加了一个基于蒙特卡洛树搜索（MCTS）的学习后搜索步骤，能够找到更优解。实验表明该方法能在小型问题实例上进行学习，并成功泛化到大型实际实例，且与传统方法相比具有很强的竞争性。
### Conclusion
该方法能够高效地在超订问题中找到优质的观测任务选择和时间安排方案，展示了基于图神经网络和深度强化学习的新技术在复杂规划问题上的潜力。
## 863. `cs.LG` - TiCT：一种预训练在合成数据上的时间序列分类基础模型 [PDF](https://arxiv.org/pdf/2511.19694), [HTML](https://arxiv.org/abs/2511.19694)
### Authors
Chin-Chia Michael Yeh,Uday Singh Saini,Junpeng Wang,Xin Dai,Xiran Fan,Jiarui Sun,Yujie Fan,Yan Zheng
### Background
时间序列数据的普遍性催生了对通用基础模型的强烈需求，然而，将这些模型用于分类仍面临巨大挑战，主要原因是标注数据的成本高。具有上下文学习能力（ICL）的基础模型可以提供有力的解决方案，这类模型可以通过少量示例快速适应新任务，并减少大幅度重新训练的需求。然而，大规模时间序列模型之前的研究工作大多集中在预测上，忽略了灵活且无需微调的分类任务。因此，当前存在重要的空白。
### Innovation
本文的主要贡献有两个技术方面：1）一种新型架构，采用可扩展的基于比特的标签编码和特殊输出注意力机制，能处理任意数量的类别；2）一个结合Mixup启发过程和数据增强的合成预训练框架，以促进泛化能力和噪声不变性。实验结果表明，TiCT在UCR档案上的性能与最先进的监督方法相当。在整个推理过程中，TiCT仅使用上下文实例，且无需更新任何模型权重，从而实现了这一目标。
### Conclusion
TiCT模型通过合成数据进行预训练，在时间序列分类任务上展示了良好的性能。这一方法显著减少了对标注数据的需求，且能够在没有模型权重更新的情况下仅通过少量实例完成分类任务。
## 864. `cs.LG` - 一种基于潜在扩散模型的灰盒攻击方法——通过后验崩溃实现对图像编辑的保护 [PDF](https://arxiv.org/pdf/2408.10901), [HTML](https://arxiv.org/abs/2408.10901)
### Authors
Zhongliang Guo,Chun Tong Lei,Lei Fang,Shuai Zhao,Yifei Qian,Jingyu Lin,Zeyu Wang,Cunjian Chen,Ognjen Arandjelović,Chun Pong Lau
### Background
最近在潜在扩散模型（LDMs）的进步已经彻底革新了图像合成和编辑，但同时也引发了关于数据误用和知识产权侵犯的严重担忧。虽然对抗性攻击被广泛研究以保护生成AI的滥用，但当前的方法受到高度依赖模型特定知识和计算成本高的限制。论文通过对比后验崩溃现象在VAE训练中的观察，提出了一种新的框架——后验崩溃攻击（PCA），以保护图像免受未经授权的编辑。
### Innovation
论文通过识别VAE推理中两种独特的崩溃现象：扩散崩溃和集中崩溃，设计了一种统一的损失函数，可以通过参数调整灵活实现两种类型的崩溃，从而具有不同的防止图像编辑的目的。PCA方法只需访问VAE编码器，即可减少对模型特定知识的依赖，仅占LDM参数的不到4％。PCA通过在文本条件化之前作用于VAE编码器，实现对输入提示不变的保护，无需现有方法所需的空提示优化。这使得PCA能够在各种基于VAE的LDM架构中保持良好的迁移性同时有效防止未经授权的图像编辑。实验结果表明，PCA在保护效果、计算效率（运行时间和VRAM）以及跨不同VAE基LDM变体的一般化性能方面均优于现有技术。
### Conclusion
广泛的实验表明，PCA在保护效果、计算效率和对不同VAE基LDM变体的一般化性能方面均优于现有的技术。PCA方法通过访问仅占LDM参数不到4%的VAE编码器，大幅减少了对模型特定知识的依赖，并实现了对输入提示不变的保护，无需空提示优化。PCA方法的有效性和普适性得到了验证。
## 865. `cs.LG` - Adam简化：驳斥偏差校正 [PDF](https://arxiv.org/pdf/2511.20516), [HTML](https://arxiv.org/abs/2511.20516)
### Authors
Sam Laing,Antonio Orvieto
### Background
Adam优化器是现代深度学习的基石，但其各个组成部分的实证必要性常常被理所当然地接受。本文聚焦于偏差校正的作用，这是其贡献仍然不甚了解的特征。研究团队通过对视觉和语言建模任务进行系统性的消除实验，发现关于偏差校正的传统认知存在误导性。特别是在最佳超参数配置下，偏差校正并未对最终测试性能带来提升，而且如果未实施适当的学习率调度，偏差校正有时反而会损害性能。
### Innovation
本文重新解释了偏差校正，认为其本质上是一种隐式的学习率调度机制，其行为与平滑超参数 $beta_1, beta_2 otin [0,1)$ 的选择密切相关。研究结果挑战了偏差校正这一组件的无条件包含观念。
### Conclusion
在最优超参数配置下，包括偏差校正对最终测试性能没有改善。如果不实施适当的学习率调度，包括偏差校正有时反而会损害性能。偏差校正可被视为一种依赖于平滑超参数 $beta_1, beta_2 otin [0,1)$ 的隐式学习率调度机制。
## 866. `cs.LG` - 去中心化 bilevel 优化：从瞬态迭代复杂性的角度 [PDF](https://arxiv.org/pdf/2402.03167), [HTML](https://arxiv.org/abs/2402.03167)
### Authors
Boao Kong,Shuchen Zhu,Songtao Lu,Xinmeng Huang,Kun Yuan
### Background
随机 bilevel 优化 (SBO) 因其在处理嵌套结构方面的灵活性，正在机器学习中变得越来越重要。为了解决大规模的 SBO 问题，去中心化的方法作为一种高效的范式出现了，其中节点仅与直接邻居通信，无需中央服务器，从而提高了通信效率和算法的稳健性。然而，大多数去中心化的 SBO 算法仅关注渐近收敛率，忽视了瞬态迭代复杂性，即渐近率成为主导之前所需的迭代次数，这导致了对网络拓扑、数据异质性和嵌套 bilevel 算法结构的影响了解有限。
### Innovation
本文引入了 D-SOBA（去中心化随机一阶 bilevel 算法框架），包含两个变体：D-SOBA-SO，整合了二阶海森矩阵和雅可比矩阵，而 D-SOBA-FO 完全依赖于一阶梯度。我们进行了全面的非渐近收敛分析并建立了 D-SOBA 的瞬态迭代复杂性，这是首次从理论角度理解网络拓扑、数据异质性以及嵌套 bilevel 结构对去中心化的 SBO 的影响。
### Conclusion
广泛的实验结果表明了 D-SOBA 的高效性和理论优势。
## 867. `cs.LG` - 作为数据点的默尔索 [PDF](https://arxiv.org/pdf/2502.01364), [HTML](https://arxiv.org/abs/2502.01364)
### Authors
Abhinav Pratap
### Background
在大数据主导的时代，人类经验被量化成可测量的指标，引发深刻的哲学和伦理问题。本研究通过阿尔贝·加缪的小说《异乡人》中的主人公默尔索这一情感疏离的存在来探讨这些议题。运用自然语言处理技术（包括情感检测、情感分析和实体识别），研究量化默尔索生活中的关键事件和行为，揭示了算法模型应用于复杂人类体验的固有局限性，特别是那些根植于存在主义的孤立感和道德模糊性中的体验。
### Innovation
使用自然语言处理技术（BERT用于情感检测，VADER用于情感分析，spaCy用于命名实体识别），量化《异乡人》中默尔索的生活事件和行为，以探索算法模型在处理存在主义的孤立感和道德模糊性方面的问题。通过现代AI工具对默尔索行为和情感的误读，研究揭示了将复杂的人类叙事简化为数据点的伦理困境，挑战了数据驱动社会的基础假设。
### Conclusion
本研究的结果作为对日益依赖数据驱动叙事的批评，倡导在人工智能中融入人文价值。
## 868. `cs.LG` - CAPability：全面的视觉描述基准，评估准确性和完整性 [PDF](https://arxiv.org/pdf/2502.14914), [HTML](https://arxiv.org/abs/2502.14914)
### Authors
Zhihang Liu,Chen-Wei Xie,Bin Wen,Feiwu Yu,Jixuan Chen,Pandeng Li,Boqiang Zhang,Nianzu Yang,Yinglu Li,Zuan Gao,Yun Zheng,Hongtao Xie
### Background
随着现代多模态大规模语言模型（MLLMs）的出现，视觉描述基准已经过时，简短的地面真值句子和传统指标无法有效评估详细的描述。虽然最近的基准试图通过关注关键词提取或对象中心评估来解决这个问题，但它们仍然局限于模糊视角或对象视角的分析，并且覆盖了不完整的视觉元素。
### Innovation
提出了CAPability，这是一种全面的多视角基准，涵盖了12个维度和六个关键视角，用于评估视觉描述。通过精心筛选近11,000张带有视觉元素注释的人工标注图像和视频，评估生成的描述。使用精确度和击中率指标稳定评估描述的正确性和全面性，并通过将注释转换为问答对，引入了启发式指标$Kbar{T}$（知但不能言），表明问答能力和描述能力之间的显著性能差距。这项工作提供了对MLLMs描述能力的总体分析，识别了他们在各个维度上的强项和弱点，为未来的研究指明了增强其特定方面能力的方向。
### Conclusion
我们的工作提供了一个全面的分析，展示了MLLMs在捕捉不同细维度描述能力的优劣，有助于指导未来的研究提升这些模型在特定方面的表现。
## 869. `cs.LG` - 从非序贯数据识别随机动力学（IDyNSD） [PDF](https://arxiv.org/pdf/2502.17690), [HTML](https://arxiv.org/abs/2502.17690)
### Authors
Zhixin Lu,Łukasz Kuśmierz,Stefan Mihalas
### Background
从数据推断随机动态是科学中的核心问题，但在许多应用中，仅可用未排序、非序贯的测量数据，且数据常受限于状态空间的特定区域，因此标准的时间序列方法不适用。
### Innovation
文章提出了IDyNSD框架，这是一种基于原理的方法，可以从非序贯数据中识别未知的动力学参数，通过最小化Fokker-Planck残差来实现。该框架提出了两种互补的途径：局部路径处理受限区域数据，利用局部估计得分数值；全局路径从全局采样数据中拟合动力学，使用内核Stein差异性，无需显式密度或分数估计。该框架为非线性情况下的参数识别提供了可梯度优化的可微损失函数。
### Conclusion
通过两种基于原理的途径识别非序贯数据中的随机动力学，这两种途径均基于Fokker-Planck方程。这两种方法成功从非序贯数据中恢复了Lorenz系统的参数和非线性基因调控网络的交互矩阵，并且该Fokker-Planck残差观点还支持了一种直接从已知动力学训练归一化密度估计的方法，没有观察数据。
## 870. `cs.LG` - 超越目录的个性化图像生成 [PDF](https://arxiv.org/pdf/2502.18477), [HTML](https://arxiv.org/abs/2502.18477)
### Authors
Gabriel Patron,Zhiwei Xu,Ishan Kapnadak,Felipe Maia Polo
### Background
人类与AI的互动中，个性化至关重要，而现有的基于扩散的图像生成系统对用户多样性反应不足。现有的解决方法要么依赖于成本高昂的配对偏好数据，要么通过大型语言模型引入延迟。
### Innovation
研究引入了REBECA（REcommendations BEyond CAtalogs），一个轻量级且可扩展的框架，通过学习用户的隐式反馈信号，如点赞、评分和点击等来实现个性化图像生成，而无需调整基础的扩散模型。它采用两阶段过程：首先训练一个条件扩散模型来生成用户和评分特定的图像嵌入，然后再通过预训练的扩散骨干解码为图像。这种方法能够在大规模用户群中实现高效、无需微调的个性化。
### Conclusion
我们使用实际数据集严格评估了REBECA，使用新颖的统计个性化验证器和基于排列的假设检验来评估偏好对齐情况。研究结果表明，REBECA能够生成高保真度且符合个人兴趣的图像，优于基准模型，同时保持计算效率。
## 871. `cs.LG` - Superstate Quantum Mechanics [PDF](https://arxiv.org/pdf/2502.00037), [HTML](https://arxiv.org/abs/2502.00037)
### Authors
Mikhail Gennadievich Belov,Victor Victorovich Dubov,Vadim Konstantinovich Ivanov,Alexander Yurievich Maslov,Olga Vladimirovna Proshina,Vladislav Gennadievich Malyshkin
### Background
传统量子力学仅考虑波函数归一化单一二次约束的问题，并且能量也以哈密顿量为二次形式表达。然而，文章提出了Superstate Quantum Mechanics (SQM)理论，它考虑了希尔伯特空间中受到多个二次约束的状态，能量同样以这些状态的二次函数表示。
### Innovation
SQM理论引入了处理具有多个二次约束的状态的新方法。当SQM将状态表示为幺正算子时，问题转变为了量子逆问题，适用于物理、机器学习和人工智能领域。此外，提出了两种可能的SQM动力学方程：一种是基于高阶量子理论中的线性映射，通过二维类型的量子电路转变量子系统；另一种是类似Gross-Pitaevskii的非线性映射。虽然目前没有物理过程描述这种二维动力学，但这种方法有助于直接和逆量子力学问题之间的桥梁构建，促进了新型量子计算机算法的发展。
### Conclusion
文章提出了一种新的经典计算模型，利用量子通道进行计算，这种计算可以在经典计算机上执行。此项工作为SQM理论的实际应用打开了新的途径。
## 872. `cs.LG` - GiBy: 巨人一步小步分类器在工业控制系统中的异常检测 [PDF](https://arxiv.org/pdf/2504.20906), [HTML](https://arxiv.org/abs/2504.20906)
### Authors
Sarad Venugopalan,Sridhar Adepu
### Background
工业控制系统(I CS)中的关键组件需要持续监控以确保系统的自动化控制安全，并保障生产过程的安全，防止进入不可接受的危险状态。实现这一目标的关键是通过传感器读数来有效管理执行（如使用电信号来触发物理运动），及时发现异常（如攻击、故障和未知状态）对于确保工厂的安全运行、员工的安全以及提供安全服务至关重要。
### Innovation
提出了一种用于工业控制系统的异常检测方法，该方法通过准确线性化传感器-执行器关系中的非线性形式实现，以便更易于理解和解决线性模型。实验表明，该方法具有毫秒级的异常检测响应速度，并且所有检测到的异常都可以解释和追踪。此外，该方法的可解释性使其能够具体指出检测异常的传感器和执行状态，这是前所未有的，以往的解释性人工智能(XAI)和机器学习(ML)模型都无法同时实现检测速度和可解释性的结合。
### Conclusion
所提出的算法在安全运行极限内正确识别了97.72%的偏差，这表明对于那些在安全边界内有余量的系统，不需要使用速度较慢但检测分辨率最高的检测器。
## 873. `cs.LG` - 基于策略优化和多智能体强化学习的均值-方差团队随机博弈方法 [PDF](https://arxiv.org/pdf/2503.22779), [HTML](https://arxiv.org/abs/2503.22779)
### Authors
Junkai Hu,Li Xia
### Background
研究了一种长期均值-方差团队随机博弈(MV-TSG)，其中每个代理共享系统的共同均值-方差目标，并独立采取行动以最大化此目标。该博弈有两个主要挑战：首先，方差度量在动态设置中既不是加性的也不是马尔可夫的；其次，所有代理同时更新策略会导致每个代理的非平稳环境。这些挑战使得动态规划不适用。
### Innovation
从基于灵敏度的优化角度研究MV-TSG，推导出了联合策略的性能差异和性能导数公式，提供了MV-TSG的优化信息；证明了该问题存在确定性纳什策略；提出了一种名为Mean-Variance Multi-Agent Policy Iteration (MV-MAPI)的算法，证明该算法收敛到目标函数的一阶最优点；通过分析稳定点的局部几何形状，推导出稳定点成为（局部）纳什均衡的具体条件，进一步推导出严格局部最优条件；将信任区域方法扩展到MV-MAPI，开发出一种名为Mean-Variance Multi-Agent Trust Region Policy Optimization (MV-MATRPO)的多智能体强化学习算法；为每次联合策略更新推导出性能下界。
### Conclusion
通过数值实验验证了在多个微电网系统能源管理中的应用。
## 874. `cs.LG` - 室内导航辅助的自适应目标检测：实时算法的性能评估 [PDF](https://arxiv.org/pdf/2501.18444), [HTML](https://arxiv.org/abs/2501.18444)
### Authors
Abhinav Pratap,Sushant Kumar,Suchinton Chakravarty
### Background
为视障人士提供准确高效的物体检测对于辅助技术的需求日益增加。本研究评估了YOLO、SSD、Faster R-CNN和Mask R-CNN这四种实时物体检测算法在室内导航辅助中的应用效果。利用Indoor Objects Detection数据集，分析了检测精度、处理速度及算法在室内环境中的适应性。
### Innovation
研究通过对四种实时物体检测算法的性能评估，揭示了精确性和效率之间的权衡，并为实时辅助导航系统选择合适的算法提供了指导依据。研究促进了自适应机器学习的应用，提高了室内导航解决方案的适应性和适应性。
### Conclusion
研究结果表明，各算法在准确性和效率方面存在权衡，不同场景下适用不同的算法。本研究为视障人士室内导航的实时辅助提供了新的思路和技术支持。
## 875. `cs.LG` - LASER: 唇部标记辅助鲁棒说话人检测 [PDF](https://arxiv.org/pdf/2501.11899), [HTML](https://arxiv.org/abs/2501.11899)
### Authors
Le Thien Phuc Nguyen,Zhuoran Yu,Yong Jae Lee
### Background
说话人检测（ASD）旨在识别复杂视觉场景中说话的人。现有的ASD模型常在唇部动作和音频不一致时发生误分类。人类自然依靠唇部和声音同步识别说话者，但模型在这种情况下的表现较差，导致误判。
### Innovation
研究人员提出了Lip landmark Assisted Speaker dEtection for Robustness (LASER)，这是一种在训练中明确引入唇部标记以引导模型关注与语音相关的区域的方法。Laser通过从给定的人脸轨迹中提取视觉特征，并将2D唇部标记编码为密集地图。为了处理低分辨率或遮挡情况，引入了一个辅助一致性损失，将唇部感知预测与仅面部预测对齐，从而在测试时不需使用特征点检测器，提高了鲁棒性。
### Conclusion
Laser在多个基准测试中优于现有模型，特别是在具有高噪音背景的子集中，相较于LoCoNet和TalkNet，分别提高了3.3和4.3个百分点，展示了对真实世界声音挑战的强大适应性。为了进一步评估鲁棒性，研究团队创建了一个名为LASER-bench的数据集，其中包括带有不同背景噪音级别的现代视频片段。
## 876. `cs.LG` - PointNSP：基于Next-Scale Level-of-Detail预测的自回归3D点云生成 [PDF](https://arxiv.org/pdf/2503.08594), [HTML](https://arxiv.org/abs/2503.08594)
### Authors
Ziqiao Meng,Qichao Wang,Zhiyang Dou,Zixing Song,Zhipeng Zhou,Irwin King,Peilin Zhao
### Background
自回归点云生成长期以来在质量上落后于基于扩散的方法。这种差距源于自回归模型对固有的无序点集施加的人工顺序，迫使形状生成以局部预测的顺序进行，这强调了短程连续性但削弱了模型捕捉长时间依赖的能力，从而阻碍了对全局结构属性如对称性、一致拓扑和大尺度几何规律的约束。
### Innovation
为了借鉴形状建模中的层次细节（LOD）原则，作者提出了PointNSP，这是一种从粗到细的生成框架，它在低分辨率下保持全局形状结构，并通过下一代预测范式在较高尺度上逐级细化细微几何。这种多尺度分解使自回归目标与点集的置换不变性质一致，从而在各尺度范围内提供丰富的交互作用，同时避免了固定的脆弱顺序。
### Conclusion
实验表明，PointNSP在自回归范式下首次实现了最先进的生成质量。此外，它在参数、训练和推理效率方面超过了强的基于扩散的基础方法。最后，在使用8,192个点进行密集生成时，PointNSP的优势更加显著，突显出其可扩展潜力。
## 877. `cs.LG` - 使用图扩散网络学习Agent-Based模型中的个体行为 [PDF](https://arxiv.org/pdf/2505.21426), [HTML](https://arxiv.org/abs/2505.21426)
### Authors
Francesco Cozzi,Marco Pangallo,Alan Perotti,André Panisson,Corrado Monti
### Background
Agent-Based模型（ABMs）是一种强大的工具，可用于研究复杂系统中的涌现特性。在ABMs中，代理的行为由局部互动和随机规则管理，但是这些规则通常是非可微的，限制了使用基于梯度的方法进行优化，进而限制了与真实世界数据的集成。
### Innovation
本文提出了一种新颖的框架，通过观察生成的数据来学习ABM的可微替代模型。该方法结合了扩散模型来捕捉行为的随机性，并结合图神经网络来建模代理间的互动。与之前的替代方法不同，该方法引入了根本性的转变：而不是近似系统级输出，它直接建模个体代理的行为，保留了定义ABMs的去中心化、自底向上的动力学。
### Conclusion
我们在两个ABM（Schelling分段模型和捕食者-猎物生态系统）上验证了我们的方法，结果显示它能够复制个体层面的模式，并准确预测超出训练范围的涌现动力学。我们的结果证明了结合扩散模型和图学习对数据驱动的ABM模拟潜力。
## 878. `cs.LG` - Momentum Multi-Marginal Schrödinger Bridge Matching [PDF](https://arxiv.org/pdf/2506.10168), [HTML](https://arxiv.org/abs/2506.10168)
### Authors
Panagiotis Theodoropoulos,Augustinos D. Saravanos,Evangelos A. Theodorou,Guan-Horng Liu
### Background
从稀疏样本快照推断复杂系统的轨迹是广泛领域的一个基本挑战，例如单细胞生物学、气象学和经济学。尽管在Bridge和Flow匹配框架方面取得了进步，但现有方法依赖于相邻快照之间的成对内插。这限制了它们捕捉长时间依赖关系的能力，并可能影响推断轨迹的一致性。
### Innovation
我们引入了一种新的匹配框架——Momentum Multi-Marginal Schrödinger Bridge Matching (3MSBM)，用于学习满足多个位置约束的随机系统的平滑测度值样条。通过提升动力学到相空间并将随机桥梁扩展为多个点条件下的条件随机最优控制问题来实现。该方法通过最小化变分目标来学习动力学，固定由多边际条件桥梁诱导的路径。3MSBM在训练过程中学习保留中间边际的传输映射，显著提高了收敛性和扩展性。
### Conclusion
在一系列真实世界应用中的大量实验证明了3MSBM在捕捉具有时间依赖性的复杂动态方面的优越性能，为在多边际设置中训练匹配框架开辟了新的途径。
## 879. `cs.LG` - 动态ε调度：基于多因素的自适应扰动预算对抗训练方法 [PDF](https://arxiv.org/pdf/2506.04263), [HTML](https://arxiv.org/abs/2506.04263)
### Authors
Alan Mitkiy,James Smith,Myungseo wong,Hana Satou,Hiroshi Tanaka,Emily Johnson
### Background
现有的对抗训练方法依赖于固定的扰动预算，未能考虑到样本间的鲁棒性特性。尽管IAAT和MMA等先前工作的引入了基于实例的自适应，但它们通常依赖于数据鲁棒性的启发式或静态近似。
### Innovation
提出了一种新颖的框架，动态ε调度（DES），能够在每次训练实例和每次训练迭代中自适应地调整对抗扰动预算。DES结合了三个关键因素：通过梯度代理近似的决策边界距离、来自 softmax 流出性的预测置信度以及通过蒙特卡洛 Dropout 估计的模型不确定性，动态调整扰动预算以引导更有效的对抗学习。
### Conclusion
实验结果表明，相较于固定 ε 基准和先前的自适应方法，该方法在 CIFAR-10 和 CIFAR-100 上在对抗鲁棒性和标准准确性方面均取得了一致性的改进。此外，还对调度策略的稳定性和收敛性提供了理论见解。该工作为实例感知和基于数据的对抗训练方法开辟了新的途径。
## 880. `cs.LG` - Filter Like You Test: 数据驱动的数据筛选用于CLIP预训练 [PDF](https://arxiv.org/pdf/2503.08805), [HTML](https://arxiv.org/abs/2503.08805)
### Authors
Mikey Shechter,Yair Carmon
### Background
论文背景在于当前大规模视觉-语言数据集的筛选通常依赖人工标注，这在时间和成本上都非常昂贵。此外，大规模数据集需要一种自动筛选的方法，以提高预训练模型的表现。FLYT算法旨在自动评价每个数据点作为预训练示例的价值，通过学习梯度信号来自下游任务训练集的特征权重，进而自动筛选数据集。
### Innovation
FLYT算法的创新在于它能够自动生成每个示例的评分，并根据这些评分进行数据筛选。FLYT通过学习从下游任务训练集中的梯度信号来评估每个示例的重要性，进而挑选出最有效的预训练样本。此外，该算法还结合了多种评分方法，通过混合得分方法(M-FLYT)将不同评分方法生成的得分统一到一个最终评分中。FLYT方法还引入了一种软帽采样策略(SCS)，通过重复惩罚防止样本过度代表，从而实现了更均衡的数据过滤。
### Conclusion
FLYT方法在DataComp基准测试中显示出了较高性能，取得了40.1%的ImageNet零样本准确率，与之前所有结果相比绝对增加2%，且比使用仅公共资源的方法高出5.5%。通过FLYT方法，我们的工作在DataComp的38个评估任务中取得了37.7%的平均准确率，超越了所有使用公开资源的方法0.4%。
## 881. `cs.LG` - 数学视角下的蛋白质结构洞察：持久同调与机器学习在鞭毛马达中的应用 [PDF](https://arxiv.org/pdf/2504.16941), [HTML](https://arxiv.org/abs/2504.16941)
### Authors
Zakaria Lamine,Abdelatif Hafid,Mohamed Rahouti,My Ismail Mamouni
### Background
论文介绍了一种机器学习方法，利用持久同调来分类细菌鞭毛马达的功能状态为旋转和停滞。通过将蛋白质结构数据嵌入拓扑框架中，从基于原子坐标的滤波单纯复形中提取多层次特征。这些拓扑不变量（特别是持久图和条形码）捕获了与马达功能相关的关键几何和连接模式。提取的特征被向量化并集成到机器学习管道中，该管道包括降维和监督分类。
### Innovation
通过将蛋白质结构数据嵌入拓扑框架中，提取多层次特征，这些特征特别是一些拓扑不变量（如持久图和条形码），能够捕获与马达功能相关的几何和连接模式。这种方法揭示了功能相关模式，这些模式超出了传统几何描述的范围，提供了一种新的计算工具来预测蛋白质功能。
### Conclusion
在通过实验确认的功能多样化细菌鞭毛马达的已编目数据集上，该模型展示了高分类准确性和对结构变异的鲁棒性。这种方法表明，拓扑数据分析能够揭示超越传统几何描述的功能相关模式，提供了一种新的计算工具来预测蛋白质功能。
## 882. `cs.LG` - 揭示谱特征学习在工具变量回归中的奥秘 [PDF](https://arxiv.org/pdf/2506.10899), [HTML](https://arxiv.org/abs/2506.10899)
### Authors
Dimitri Meunier,Antoine Moulin,Jakub Wornbard,Vladimir R. Kostic,Arthur Gretton
### Background
本文解决了在隐含共变量存在时效果因果估计的问题，利用非参数工具变量（IV）回归。主流策略使用谱特征，即跨治疗与工具关联算子的前高层谱子空间学习的特征。文章基于这些谱特征提出了一个两阶段最小二乘估计算法，并对其泛化误差边界进行了推导，揭示了该方法的性能和失效模式及其背后的关键因素。
### Innovation
文章推导了一种基于谱特征的两阶段最小二乘估计算法的泛化误差边界，进一步分析了其性能和失效模式。通过引入两种关键因素来分类表现，得出不同的应用场景，并通过合成实验验证了该分类。此外，文章提出了一种实用方法来估计这些谱属性，以便解决工作者能够诊断出具体问题所处的阶段。
### Conclusion
在良好的情况下，方法可实现最优效果；在糟糕的情况下，虽然谱对齐较强，但快速的特征值衰减意味着需要更多的样本数量；而在丑陋的情况下，即便特征值特征良好，弱的谱对齐也导致方法失效。通过合成实验验证了这一分类，并结合dSprites数据集的应用，展示了其实用性。
## 883. `cs.LG` - 知识图谱检索中的结构-内容权衡 [PDF](https://arxiv.org/pdf/2506.13380), [HTML](https://arxiv.org/abs/2506.13380)
### Authors
Valentin Six,Evan Dufraisse,Gaël de Chalendar
### Background
大型语言模型（LLMs）越来越多地依赖知识图谱进行事实推理，但检索设计如何影响模型性能仍然不清楚。本研究探讨了问题分解如何改变检索到的子图的内容和结构。通过一种混合检索函数控制初始问题和子问题的重要性，研究发现基于子问题的检索提高了内容精度，但导致了不连贯的子图，而基于问题的检索保持了结构，但牺牲了相关性。最优性能出现在这两者之间，揭示了平衡检索内容和结构是有效利用结构化知识进行LLM推理的关键。
### Innovation
研究引入了一种混合检索函数，通过控制初始问题和子问题的重要性来探讨问题分解对检索到的子图内容和结构的影响。研究揭示了平衡检索内容和结构对于大型语言模型有效处理结构化知识的重要性。
### Conclusion
在知识图谱检索中，最优性能出现在仅基于问题的结构完整性和基于子问题的内容精度之间的平衡。平衡检索内容和结构对于大型语言模型有效推理是关键。
## 884. `cs.LG` - CoMind：迈向基于社区驱动的机器学习工程代理 [PDF](https://arxiv.org/pdf/2506.20640), [HTML](https://arxiv.org/abs/2506.20640)
### Authors
Sijie Li,Weiwei Sun,Shanda Li,Ameet Talwalkar,Yiming Yang
### Background
大型语言模型（LLM）代理在自动化机器学习（ML）工程方面展现了潜力。然而，现有的代理通常在独立解决给定研究问题时与更广泛的科研社区隔绝，人类研究员通常通过共享知识获得见解并贡献力量。为了解决这一问题，我们介绍了ML-E Live框架，旨在评估代理与模拟的Kaggle研究社区通信和利用集体知识的能力。在此基础上，我们提出了CoMind多代理系统，旨在积极整合外部知识。
### Innovation
CoMind系统采用了迭代并行探索机制，同时开发多个解决方案，平衡探索广度和实现深度。在ML-E Live框架内的75场过去的Kaggle竞赛中，CoMind实现了36%的奖牌率，设立了新的技术前沿。在八个实际进行中的竞赛中，CoMind平均比92.6%的人类竞争对手表现更优，在三个官方排行榜上占据了前5%，并在一个排行榜上占据了前1%。
### Conclusion
CoMind系统在ML-E Live框架内的表现超越了人类竞争对手，证明了其在机器学习工程中的应用潜力，特别是通过社区驱动的知识共享与整合机制，提升了自动化解决方案的有效性。
## 885. `cs.LG` - 矩阵去噪模型中的奇异子空间估计的极值理论 [PDF](https://arxiv.org/pdf/2507.19978), [HTML](https://arxiv.org/abs/2507.19978)
### Authors
Junhyung Chang,Joshua Cape
### Background
本文研究了矩阵去噪模型中的精细奇异子空间估计问题，该模型中包含一个确定性低秩信号矩阵，该矩阵被高斯噪声随机矩阵所扰动。
### Innovation
研究了对齐后的样本和总体奇异向量最大欧几里得行范数（即二至无穷范数）在矩阵尺寸无限增长的情况下，符合Gumbel分布的现象，尤其是在适当信噪比条件下和适当的中心化与缩放后。利用新的渐近分布理论，提出了对主要奇异向量和它们对应的主子空间中低秩信号结构的假设检验，提供了去偏估计量，展示了所提插值检验统计量的优势。
### Conclusion
与使用海勒夫内斯范数子空间距离相比，基于二至无穷范数的检验统计量在检测仅在少数矩阵元素或行中与零假设不同的结构替代中具有更高的检测力。主要结果是通过新颖的行列分析技术综合和涉及技术分析得出的，包括边缘矩阵扰动分析、极值理论、鞍点逼近方法和随机矩阵理论。我们的贡献补充了关于矩阵去噪的现有文献，特别是关于最小最大性、均方误差分析、酉不变距离之间的子空间、分量渐近分布理论和行列一致误差边界的内容。数值模拟验证了我们的主要结果，并展示了测试程序在非高斯噪声分布下的稳健性。
## 886. `cs.LG` - IndiSeek 学习信息引导的解耦表示 [PDF](https://arxiv.org/pdf/2509.21584), [HTML](https://arxiv.org/abs/2509.21584)
### Authors
Yu Gui,Cong Ma,Zongming Ma
### Background
在多模态学习中，学习解耦表示是一个基本任务。在单细胞多组学等现代应用中，共享特征和模态特定特征对于表征细胞状态和支持下游分析至关重要。理想情况下，模态特定特征应该与共享特征独立，同时捕捉每个模态内的所有互补信息。这种权衡自然可以通过信息论标准来表达，但基于互信息的目标难以可靠地估计，其变分近似在实践中往往表现不佳。
### Innovation
本文提出了一种新的解耦表示学习方法——IndiSeek，通过结合一个独立性强制目标与一个计算高效的重构损失来限制条件互信息，从而在解耦与完整性之间明确平衡。这种公式化方法允许有原则地提取模态特定特征。
### Conclusion
我们在合成模拟、CITE-seq 数据集以及多个真实的多模态基准上验证了 IndiSeek 的有效性。
## 887. `cs.LG` - 使用可微气候模型构建极端热浪情景 [PDF](https://arxiv.org/pdf/2506.10660), [HTML](https://arxiv.org/abs/2506.10660)
### Authors
Tim Whittaker,Alejandro Di Luca
### Background
在气候变暖的背景下，理解极端天气事件的可能上限对于风险评估至关重要。现有方法通常依赖于物理模型的大规模集合，但这些方法要么计算成本高昂，要么缺乏模拟罕见高影响极端天气所需的精度。
### Innovation
本文提出了一个新颖的框架，利用可微气候模型——NeuralGCM——优化初始条件并生成物理上一致的最坏情况热浪路径。这种方法能够高效地探索事件概率的上尾，为气候变暖下极端天气的情景构建提供了一种强有力的新方法。
### Conclusion
通过对2021年太平洋西北部热浪的应用，本方法生成了比75成员集合中最极端的情况高出3.7°C的热浪强度。这些路径显示出加强的大气阻塞和加强的罗斯比波模式，这是严重热事件的标志。研究结果证明了可微气候模型能够有效探索事件概率的上限，为极端天气情景提供了强有力的构建方法。
## 888. `cs.LG` - AI研究中的严谨性：严谨的AI工作需要更广泛、负责任的AI指导下的严谨性概念 [PDF](https://arxiv.org/pdf/2506.14652), [HTML](https://arxiv.org/abs/2506.14652)
### Authors
Alexandra Olteanu,Su Lin Blodgett,Agathe Balayn,Angelina Wang,Fernando Diaz,Flavio du Pin Calmon,Margaret Mitchell,Michael Ekstrand,Reuben Binns,Solon Barocas
### Background
目前，AI研究和实践中对于严谨性的理解大多局限在方法论严谨性上，如数学、统计或计算方法是否正确运用。这种狭义的严谨性观念导致了负责任的AI社区对AI系统能力的夸大。文章指出，现有的严谨性观念已经难以满足实际需求，需要一种更宽泛的理解方法。
### Innovation
本文提出了一种更广泛的严谨性概念，涵盖六个方面：背景知识、学科或社区规范、概念清晰度、报告清晰度以及实证支持性。这种创新的概念为研究人员、政策制定者、记者和其他利益相关者提供了有用的术语和框架，便于进行关于AI工作的必要讨论。
### Conclusion
文章认为，更广泛的严谨性概念能够帮助克服狭义的理解带来的问题，并在AI研究和实践中促进负责任的工作。为此，提供了工具和框架以便各方进行有效交流。
## 889. `cs.LG` - Augur：通过大型语言模型建模时序中的协变量因果关联 [PDF](https://arxiv.org/pdf/2510.07858), [HTML](https://arxiv.org/abs/2510.07858)
### Authors
Zhiqing Cui,Binwu Wang,Qingxiang Liu,Yeqiang Wang,Zhengyang Zhou,Yuxuan Liang,Yang Wang
### Background
大型语言模型（LLM）已经展示了在时序预测中的潜力，尤其能整合多种类型的数据。然而，当前基于LLM的方法存在一些显著的局限性，包括在模型架构中的边缘化角色、对粗略统计文本提示的依赖，以及缺乏可解释性。
### Innovation
Augur 是一个完全由LLM驱动的时间序列预测框架，它利用LLM的因果推理来发现和利用变量间的有向因果关联。它采用两阶段的教师学生架构，强大的教师LLM通过启发式搜索和成对因果测试从时序数据中推断出有向因果图，而轻量级的学生代理则进一步细化并调整图，通过丰富的文本提示针对高置信度的因果关联进行微调来执行预测。这一设计提高了预测准确性，同时也提供透明和可追踪的变量交互解释。
### Conclusion
在26个基线的广泛实验中，Augur 在真实世界数据集上展示了竞争力的性能和稳健的零样本泛化能力。
## 890. `cs.LG` - 结合卷积和点云架构重构局部密度场 [PDF](https://arxiv.org/pdf/2510.08573), [HTML](https://arxiv.org/abs/2510.08573)
### Authors
Baptiste Barthe-Gold,Nhat-Minh Nguyen,Leander Thiele
### Background
研究利用暗物质子结构的沿视线偏僻速度来回归局部暗物质密度场。传统的卷积U-Net虽然能够有效地处理小尺度信息，但在重建质量上仍有提升空间。为了改进这一问题，研究者提出了一种结合卷积U-Net与点云DeepSets的混合架构，这种方法不仅保留了小尺度信息的高效利用，还提升了重建质量。
### Innovation
提出了一种将卷积U-Net与点云DeepSets相结合的混合网络架构，该架构能够在小尺度上更有效地捕获局部暗物质密度场中的聚类振幅和相位，相比仅使用卷积U-Net的方法，模型重建质量更好。
### Conclusion
通过结合卷积U-Net和点云DeepSets，提出的混合网络架构在小尺度上能够更准确地重建局部暗物质密度场的尖度和相位，提升了密度场的重建质量。
## 891. `cs.LG` - .decorrelation 加速视觉变换器。 [PDF](https://arxiv.org/pdf/2510.14657), [HTML](https://arxiv.org/abs/2510.14657)
### Authors
Kieran Carrigg,Rob van Gastel,Melda Yeghaian,Sander Dalm,Faysal Boughorbel,Marcel van Gerven
### Background
在低标注数据条件下，视觉变换器（ViTs）的掩码自编码器（MAE）预训练表现出色，但其计算成本高，不适用于时间及资源受限的工业环境。
### Innovation
通过将去相关反向传播（DBP）集成到MAE预训练中，该方法在每个层逐步减少输入相关性，以加速收敛。DBP仅应用于编码器，可在不过度影响稳定性的情况下实现加速预训练。
### Conclusion
DBP-MAE在ImageNet-1K预训练和ADE20K微调中的实验结果表明，该方法能够减少训练时间、降低碳排放并改善分割mIoU。在真实工业场景中的初步验证也显示了DBP的应用前景，证明了其在大规模ViT预训练中减少训练时间和能源消耗、提高下游性能的有效性。
## 892. `cs.LG` - 用于转化研究的标准化电子健康记录数据管道 [PDF](https://arxiv.org/pdf/2509.08553), [HTML](https://arxiv.org/abs/2509.08553)
### Authors
Jessica Gronsbell,Vidul Ayakulangara Panickan,Doudou Zhou,Chris Lin,Thomas Charlon,Chuan Hong,Xin Xiong,Linshanshan Wang,Jianhui Gao,Shirley Zhou,Yuan Tian,Yaqi Shi,Ziming Gan,Tianxi Cai
### Background
尽管电子健康记录（EHR）数据的可用性日益增加，研究人员在有效地利用这些数据进行转化研究时仍面临复杂性、异质性和缺乏标准化工具和文档等重大障碍。
### Innovation
PEHRT是一个跨机构标准化管道，提供开源代码、可视化工具和详细文档，将结构化和非结构化EHR数据统一到标准化的本体中，以确保在不同编码系统之间的一致性。此外，PEHRT还利用表示学习和预训练语言模型生成的稳健嵌入，捕捉站点间的意义关系，缓解异质性，并支持机构间的协同训练，提高泛化能力。
### Conclusion
通过降低基于EHR的研究的技术障碍，PEHRT使研究者能够将原始临床数据转化为可重复的、分析准备好的资源，以进行发现和创新。
## 893. `cs.LG` - 基于哈希水印作为过滤器：在基于权重的神经网络水印技术中抵御伪造和覆盖攻击 [PDF](https://arxiv.org/pdf/2507.11137), [HTML](https://arxiv.org/abs/2507.11137)
### Authors
Yuan Yao,Jin Song,Jian Jin
### Background
作为有价值的数字资产，深度神经网络需要坚固的所有权保护，这使得神经网络水印（NNW）成为潜在的解决方案。尽管基于权重的方法因其简单性和实用性而受到青睐，但它们依然对伪造和覆盖攻击较为脆弱。
### Innovation
我们提出了一个名为NeuralMark的稳健方法，它基于哈希水印滤波器。该方法利用哈希函数从秘密密钥生成一个不可逆转的二进制水印，并将其用作滤波器选择模型参数来嵌入水印。此外，该方法还结合了平均池化来抵抗微调和剪枝攻击。此外，该方法可以无缝地集成到各种神经网络架构中，确保其广泛应用性。
### Conclusion
从理论上分析了其安全边界，并通过实验验证了其在13种不同的卷积和变换器架构中的有效性和鲁棒性，这些架构包括五个图像分类任务和一个文本生成任务。源代码可以在该网址下载：this https URL.
## 894. `cs.LG` - 队列控制中的有限时间最小最大界和最优Lyapunov策略 [PDF](https://arxiv.org/pdf/2506.18278), [HTML](https://arxiv.org/abs/2506.18278)
### Authors
Yujie Liu,Vincent Y. F. Tan,Yunbei Xu
### Background
本文提出了一个独特的最小最大框架，用于有限时间内的排队控制性能分析。该框架定量表征了预期总队列长度与系统参数（包括调度集容量和队列中到达和离开的变异性）之间如何关联。已知这是首次为评估和比较有限时间内（包括非平稳设置）的调度策略提供坚实的基础，表明所提出的策略在有限时间内能够证明并经实验证明优于经典的MaxWeight。
### Innovation
文章提出了一个新的基于Lyapunov的调度策略——LyapOpt，该策略能够最小化完整的二次Lyapunov漂移，涵盖了从一阶到二阶的所有项，实现重负载下的最优有限时间性能，同时保留经典稳定性保证。此外，还发现经典MaxWeight策略的一个重要局限性，它只优化了一阶漂移，导致其在有限时间内的性能在系统参数上的表现不佳，特别是在具体描述的场景中，这种性能差距巨大。
### Conclusion
这些结果界定了经典漂移基于调度方法的范围和局限性，指出了新的具有严格有限时间保证的排队控制方法的需求。
## 895. `cs.LG` - 免费的不确定性鲁棒性？重新审视基于基准的训练 [PDF](https://arxiv.org/pdf/2511.01724), [HTML](https://arxiv.org/abs/2511.01724)
### Authors
Yi Zhang,Zheng Wang,Zhen Chen,Wenjie Ruan,Qing Guo,Siddartha Khastgir,Carsten Maple,Xingyu Zhao
### Background
深度学习模型对于细小的不可感知扰动存在显著的脆弱性。现有研究主要集中在对抗鲁棒性 (AR) 上，通过检视确定性对抗样本 (AE) 的存在性来评估模型在最坏情况下的表现。相反，概率鲁棒性 (PR) 采取统计学视角，衡量在随机扰动下预测保持正确的概率。尽管 PR 被广泛认为是 AR 的实用补充，但专门用于提高 PR 的训练方法仍然相对未被充分探索。尽管如此，一些 PR 目标训练方法已显示出进展，但存在测评协议不一致、与强大对抗训练 (AT) 基线比较不足以及无法统一比较这些方法的泛化能力等局限。
### Innovation
该论文引入了 PRBench，这是首个专注于评估不同鲁棒性训练方法在提高概率鲁棒性 (PR) 方面所取得改进的基准。PRBench 使用全面的度量标准，包括干净准确率、PR 和 AR 性能、训练效率以及泛化误差（GE），对大多数常见的 AT 和 PR 目标训练方法进行了实验性比较。此外，该论文还对不同训练方法下的 PR 性能泛化误差进行了理论分析。结果显示，AT 方法在改进 AR 和 PR 性能方面比 PR 目标训练方法更具通用性，而 PR 目标训练方法则一致表现出较低的泛化误差和较高的干净准确率。
### Conclusion
基于此基准，研究展示了在不同超参数设置下，AT 方法在提高 AR 和 PR 性能方面的灵活性，而 PR 目标训练方法的一致性表现则表现为较低的泛化误差和较高的干净准确率。该研究公布了一个由 7 个数据集和 10 个模型架构下的 222 个训练模型组成的排行榜，网址为：this https URL.
## 896. `cs.LG` - 所有切分都平等吗：重新思考跨无关类别属性泛化 [PDF](https://arxiv.org/pdf/2509.06998), [HTML](https://arxiv.org/abs/2509.06998)
### Authors
Liviu Nicolae Fircă,Antonio Bărbălau,Dan Oneata,Elena Burceanu
### Background
尽管先前的研究已经解决了在狭窄的分类或类似视觉域内的属性预测问题，但对于当前模型是否能在概念上不同的类别间抽象属性并正确应用这一问题仍然不明确。这项工作首次明确评估了在这些条件下属性预测任务的鲁棒性，测试了模型是否能够在无关物体类型（例如，识别“有四条腿”这一属性同时适用于“狗”和“椅子”）之间正确推断共享属性。为了进行这一评估，我们引入了一种基于LLM的语义分组、基于嵌入相似度阈值、基于嵌入的聚类以及基于超类的分区的训练-测试切分策略。
### Innovation
我们提出了训练-测试切分策略，这些策略逐步减少了训练集和测试集之间的相关性，从而能够进行跨无关类别属性泛化的明确评估。结果显示出在训练和测试类别相关性降低时性能显著下降，表明对切分设计的强烈敏感性。在评估的方法中，基于聚类的方法在减少隐藏相关性的同时最大限度地保持了可学习性，为属性推理的当前表示及其未来基准构建提供了新的见解。
### Conclusion
这些发现揭示了当前表示的局限性，并为属性推理的未来基准构建提供了新的指导。
## 897. `cs.LG` - PointNSP: 基于下一级层次细节预测的自回归3D点云生成 [PDF](https://arxiv.org/pdf/2510.05613), [HTML](https://arxiv.org/abs/2510.05613)
### Authors
Ziqiao Meng,Qichao Wang,Zhiyang Dou,Zixing Song,Zhipeng Zhou,Irwin King,Peilin Zhao
### Background
自回归点云生成在过去一直落后于基于扩散的方法，在质量上存在差距。这种差距源于自回归模型对原本无序的点集施加了人为的顺序限制，促使形状生成按照局部预测的顺序进行。这种顺序偏见强调了短程连续性，但削弱了模型捕获远程依赖关系的能力，阻碍了它对全球结构性质如对称性、一致拓扑结构和大规模几何规律的强制执行。
### Innovation
受到形状建模中层次细节（LOD）原则的启发，提出了一个从粗到细的生成框架——PointNSP，该框架在低分辨率下保持全局形状结构，并通过一种下一代预测范式在更高的尺度下逐层细化精细几何结构。这种多尺度因子化调整了自回归目标与点集的置换不变性本质，促进了丰富的跨尺度交互，同时避免了固定的脆弱顺序。
### Conclusion
实验表明，PointNSP在自回归范式的生成质量上首次达到最佳状态。此外，它在模型参数、训练效率和推断效率上也超过了强大的基于扩散的方法。在密集生成8192个点的情况下，PointNSP的优势更加显著，证实了其扩展性潜力。
## 898. `cs.LG` - LightMem: 轻量级且高效的增强记忆生成系统 [PDF](https://arxiv.org/pdf/2510.18866), [HTML](https://arxiv.org/abs/2510.18866)
### Authors
Jizhan Fang,Xinle Deng,Haoming Xu,Ziyan Jiang,Yuqi Tang,Ziwen Xu,Shumin Deng,Yunzhi Yao,Mengru Wang,Shuofei Qiao,Huajun Chen,Ningyu Zhang
### Background
尽管大型语言模型（LLMs）具备卓越的能力，但在动态和复杂的环境中，它们难以有效利用历史交互信息。现有的内存系统通过引入持久的信息存储、检索和利用机制，使LLMs从无状态交互中跃升，但这类系统通常会带来大量的时间和计算开销。
### Innovation
本文提出了一种名为LightMem的新内存系统，该系统在内存系统的性能和效率之间找到了平衡。受到人类记忆模型的启发，LightMem将记忆划分为三个互补阶段：通过轻量级压缩快速过滤无关信息并按主题分组的感知记忆阶段；基于主题将这些主题分组进行组织和总结，以实现更结构化访问的主题意识短时记忆阶段；以及在睡眠期间更新的长期记忆，采用离线处理方法来解除巩固与在线推理的耦合。
### Conclusion
在LongMemEval和LoCoMo数据集上，使用GPT和Qwen作为骨干网络的LightMem在问答准确性和总token使用量、API调用数量方面均显著超过了强劲的基线系统，纯在线测试时间的成本进一步降低，token减少和API调用减少分别达到了106倍/117倍和159倍/310倍。相关代码已公开，可访问此链接。
## 899. `cs.LG` - CAMERA：基于微专家冗余分析的多矩阵联合压缩方法 [PDF](https://arxiv.org/pdf/2508.02322), [HTML](https://arxiv.org/abs/2508.02322)
### Authors
Yuzhuang Xu,Xu Han,Yuanchi Zhang,Yixuan Wang,Yijun Liu,Shiyu Ji,Qingfu Zhu,Wanxiang Che
### Background
大规模语言模型（LLMs）采用Mixture-of-Experts (MoE)架构，在多种任务上表现出强大的性能随参数增加而改善的能力，但也面临巨大的计算和存储负担。MoE模型的性能增益不能与专家参数的增长成比例。尽管之前的工作通过专家级别的剪枝、合并或分解尝试减少参数，但仍存在性能和计算效率方面的问题。
### Innovation
本文介绍了微专家作为更细致压缩单元的概念，贯穿多个矩阵。首先，我们从一个更基本的角度看待MoE层，将其视为微专家的混合体，并提出了CAMERA框架，这是一个轻量级且无需训练的方法，可用于识别微专家冗余。我们进一步提出了CAMERA-P结构化的微专家剪枝框架和CAMERA-Q用于微专家的混合精度量化方案。实验结果表明，CAMERA-P在多种细粒度剪枝率下均优于基准模型，而CAMERA-Q在激进的2比特量化下取得了最佳结果，超过了现有的矩阵和通道级方法。此外，本方法可在单张NVIDIA A100-40GB GPU上少于5分钟内完成Qwen2-57B-A14B的完整微专家分析。
### Conclusion
CAMERA框架不仅提高了MoE模型的计算效率和内存使用效率，还通过有效的剪枝和量化策略改善了模型性能。这种方法在处理大规模语言模型时具有显著优势，并且能够在单个高性能GPU上快速实现详细分析。
## 900. `cs.LG` - 通过前瞻学习与控制实现未来最优控制 [PDF](https://arxiv.org/pdf/2511.08717), [HTML](https://arxiv.org/abs/2511.08717)
### Authors
Yuxin Bai,Aranyak Acharyya,Ashwin De Silva,Zeyu Shen,James Hassett,Joshua T. Vogelstein
### Background
当前人工智能领域最前沿的问题之一是未来最优控制。现有的方法大多基于强化学习（RL），而RL和监督学习有显著的数学差异。RL通常在静态环境中的 episodic 重置下运行，限制了它的实用性。
### Innovation
本文将监督学习扩展到处理非静态、无需重置的环境中的控制学习。提出了名为“前瞻学习与控制”（PL+C）的框架，并证明了在某些相当通用的假设下，经验风险最小化（ERM）在渐近情况下可以实现贝叶斯最优策略。文章还考虑了特定的前瞻学习与控制实例——觅食任务，并展示了现代RL算法在非静态、无需重置的环境中无法学会，即使进行修改，其效率也远逊于前瞻觅食代理。
### Conclusion
在非静态、无需重置的环境中，面对觅食任务，现代RL算法效率低下。使用前瞻性学习与控制的方法，这种代理的效率要高得多。这些结果表明了前瞻学习与控制方法在处理复杂动态变化环境中的优势。
## 901. `cs.LG` - PaTAS: 一个基于主观逻辑的神经网络平行信任传播系统 [PDF](https://arxiv.org/pdf/2511.20586), [HTML](https://arxiv.org/abs/2511.20586)
### Authors
Koffi Ismael Ouattara,Ioannis Krontiris,Theo Dimitrakos,Dennis Eisermann,Frank Kargl
### Background
人工智能系统在安全关键应用中的部署越来越依赖于其可信性。传统的评估指标如准确率和精确率无法捕捉模型预测的不确定性或可靠性，尤其是在对抗或退化条件下。因此，需要一种新的方法来评估模型在不同条件下的可靠性和性能。
### Innovation
提出了一个名为PaTAS的框架，利用主观逻辑（SL）建模和传播神经网络中的信任。PaTAS通过透明并可量化的信任推理扩展了标准神经计算，提供了一种有效的机制来区分良性输入和恶意输入，并且能够在不确定性、偏见或污染的数据场景中暴露可靠的差距。
### Conclusion
PaTAS能够在实际和对抗数据集上生成可解释、对称且收敛的信任估计，这些估计可以补充准确率并暴露不确定性。实验结果表明，PaTAS能够有效地区分良性输入和恶意输入，并能够识别模型置信度与实际可靠性之间的分歧。通过在神经架构中启用透明和可量化的信任推理，PaTAS为AI生命周期中的模型可靠性评估提供了坚实的基础。
## 902. `cs.SE` - DUALGUAGE: 自动化联合安全与功能基准测试以进行安全代码生成 [PDF](https://arxiv.org/pdf/2511.20709), [HTML](https://arxiv.org/abs/2511.20709)
### Authors
Abhijeet Pathak,Suvadra Barua,Dinesh Gudimetla,Rupam Patir,Jiawei Guo,Hongxin Hu,Haipeng Cai
### Background
语言模型（LLMs）和自主编码代理正被广泛用于生成软件，但在生成安全代码的同时不损害其功能正确性方面仍然存在未满足的核心要求。现有的安全代码生成基准和评估存在不足之处，许多措施仅针对漏洞减少，忽视功能正确性保留，或者在一个数据集评估安全，在另一个数据集评估功能，这违背了同时联合评估的基本需求。鉴于缺乏支持联合评估的安全代码生成数据集，本研究提出了DUALGAUGE，一个全自动基准测试框架，用于同时严谨地评估由LLMs生成的代码的安全性和正确性。由于缺乏联合评估的数据集，本文还提供了DUALGAUGE-BENCH，一个涵盖多种编程任务的基准套件，并为每个任务配对了手动验证的测试套件，确保完全覆盖规范要求。
### Innovation
本文提出了DUALGAUGE，第一个全自动基准测试框架，专门用于同时评估由LLMs生成代码的安全性和正确性；也提出了DUALGAUGE-BENCH，一个涵盖多元编程任务的基准套件，为每个任务配备了手动验证的测试套件，确保完全覆盖规范要求。核心在于一种代理程序执行器，负责在沙盒环境中运行程序进行指定测试，及一个基于LLM的评估器，用于评估安全性和正确性。
### Conclusion
研究成果揭示了这些LLMs在正确和安全代码生成方面的关键差距，通过开源系统和数据集加速了相关领域的发展，实现了可重复、可扩展和严格的评估。
## 903. `cs.SE` - Train While You Fight -- 技术要求先进的分布式学习平台 [PDF](https://arxiv.org/pdf/2511.20813), [HTML](https://arxiv.org/abs/2511.20813)
### Authors
Simon Hacks
### Background
本文探讨在作战过程中连续学习的理念，即'训练即战斗'(TWYF)，并分析支持这一理念的高级分布式学习(ADL)平台需要满足的技术要求。研究从PfPC/NATO文件和近期实践中导出了技术挑战，并通过系统性映射将这些挑战与已验证的模式关联起来，识别了技术挑战并提供了具体的解决模式。
### Innovation
采用设计科学研究方法，从文件和实践中识别挑战，定义解决方案目标，并将这些挑战系统地与成熟的软件工程模式进行关联，以满足TWYF的理念。因此在技术挑战上识别出了七大关键领域，同时通过具体示例展示了使用案例。
### Conclusion
本文通过识别和验证技术挑战，推导出支持TWYF理念所需的解决方案框架，并通过德国武装部队的国家使用案例进行说明，从而为先进的分布式学习平台开发提供了理论和实践指导。
## 904. `cs.LG` - DR Tulu: Reinforcement Learning with Evolving Rubrics for Deep Research [PDF](https://arxiv.org/pdf/2511.19399), [HTML](https://arxiv.org/abs/2511.19399)
### Authors
Rulin Shao,Akari Asai,Shannon Zejiang Shen,Hamish Ivison,Varsha Kishore,Jingming Zhuo,Xinran Zhao,Molly Park,Samuel G. Finlayson,David Sontag,Tyler Murray,Sewon Min,Pradeep Dasigi,Luca Soldaini,Faeze Brahman,Wen-tau Yih,Tongshuang Wu,Luke Zettlemoyer,Yoon Kim,Hannaneh Hajishirzi,Pang Wei Koh
### Background
现有的深度研究模型通过强化学习与可验证奖励（RLVR）的方式训练，适用于短形式的问答任务，但在处理真实的长形式任务时存在局限性。
### Innovation
提出了一种名为Reinforcement Learning with Evolving Rubrics (RLER)的新方法，其中在训练过程中构建并维护与策略模型共同演化的评价标准，这使得评价标准能够包含模型新探索的信息，并提供区分性的、基于策略的反馈。此外，基于RLER和MCP基代理基础设施，开发了第一个直接为开放性长形式深度研究训练的模型DR Tulu-8B。
### Conclusion
DR Tulu-8B在四个涉及科学、医疗和通用领域的长形式深度研究基准测试中显著优于现有的开放深度研究模型，并达到了或超过了专有深度研究系统的性能，同时在每次查询的成本和大小方面更具优势。为了促进未来的研发，所有数据、模型和代码均已公开。
## 905. `cs.SE` - 代码大型语言模型软件设计能力的分层评估 [PDF](https://arxiv.org/pdf/2511.20933), [HTML](https://arxiv.org/abs/2511.20933)
### Authors
Mootez Saad,Boqi Chen,José Antonio Hernández López,Dániel Varró,Tushar Sharma
### Background
大型语言模型（LLMs）在软件工程领域的应用日益增多，但它们对核心软件设计概念的理解稳定性尚未得到明确。本文通过一个实证研究，系统地考察了模型对耦合（跨模块）和凝聚力（模块内）的理解。研究中，通过程序生成了劣质的代码片段，对DeepSeek-R1模型家族（含有14B、32B、70B权重参数的版本）在不同指导水平下进行了测试，同时通过注入干扰元素来改变上下文噪声水平。研究发现，在理想条件下，模型对这两种概念的了解基础相对坚实，但在实际操作中，它们的能力是脆弱且高度不对称的。尽管模型在约束任务中对耦合的理解表现出了较强的韧性，但在没有进一步指导的情况下，这种韧性就会失效。
### Innovation
本文首次系统地评估了大型语言模型在软件设计中的能力，特别是对耦合和凝聚力的理解。研究首先通过程序方式生成劣质代码片段，以定量的方式评估模型在不同指导水平和上下文噪声水平下的表现，从而揭示了这些模型在实际应用中理解和分析这些概念的局限性。
### Conclusion
虽然LLMs能够提供可靠的设计缺陷识别帮助，但在实际、嘈杂的环境中自主推理的能力却有限。这表明需要进一步发展更多可扩展的且稳健的程序理解能力，以增强LLMs在软件工程中的应用潜力。
## 906. `cs.SE` - 基础设施重建项目管理中机器学习的应用 [PDF](https://arxiv.org/pdf/2511.20916), [HTML](https://arxiv.org/abs/2511.20916)
### Authors
Illia Khudiakov,Vladyslav Pliuhin,Sergiy Plankovskyy,Yevgen Tsegelnyk
### Background
本文旨在描述一种适应性决策支持模型，旨在提高工程基础设施重建项目管理的效率。该研究分析了现有的适应性项目管理工具，并强调了使用基础设施系统建模工具创建项目架构和工作分解结构的重要性。现有的模型和建模方法被分析，机器学习和人工神经网络被选中作为该模型的基础。
### Innovation
选择机器学习和人工神经网络构建适应性决策支持模型，基于历史数据集预测系统配置下的目标函数值，调整模型参数以适应现有项目实施目标。通过微软Azure机器学习工作室描述了功能组件的组合，并给出了神经网络参数和评估结果。
### Conclusion
该适应性模型在管理热能、燃气、电力供应、供水和排水等工程系统重建项目中具有应用潜力。
## 907. `cs.LG` - STARFlow-V: 通过归一化流进行端到端视频生成建模 [PDF](https://arxiv.org/pdf/2511.20462), [HTML](https://arxiv.org/abs/2511.20462)
### Authors
Jiatao Gu,Ying Shen,Tianrong Chen,Laurent Dinh,Yuyang Wang,Miguel Angel Bautista,David Berthelot,Josh Susskind,Shuangfei Zhai
### Background
归一化流（NFs）是基于端到端似然度的连续数据生成模型，近年来在图像生成领域取得了令人鼓舞的进展。然而，在视频生成领域，由于时空复杂性和计算成本大幅增加，最先进的系统几乎完全依赖于基于扩散的模型。本文重新审视了这一设计空间，提出了一种基于归一化流的视频生成器STARFlow-V，其具有端到端学习、鲁棒因果预测以及原生似然估计等显著优势。
### Innovation
STARFlow-V 在时空潜空间中运行，使用全局-局部架构限制因果依赖关系在全局潜空间中，同时保留丰富的帧内局部交互。此外，提出了流得分匹配，该方法为模型配备了轻量级因果去噪器，以自回归方式提高视频生成一致性。为了提高采样效率，STARFlow-V 采用了一种视频感知的雅可比迭代方案，将内部更新重新表述为可并行化迭代，而不会破坏因果关系。STARFlow-V 可以通过其可逆结构，自然支持从文本到视频、从图像到视频以及从视频到视频的生成任务。
### Conclusion
在实证研究中，STARFlow-V 在视觉保真度和时间一致性方面表现出色，并具有实际的采样吞吐量，相对于基于扩散的基础模型具有明显优势。这些结果提供了证据，表明归一化流有能力进行高质量的自回归视频生成，从而确立了它们作为构建世界模型的有前途研究方向。STARFlow-V 的代码和生成样本可在http://this_is_a_url 获取。
## 908. `cs.LG` - MoEGCL: Mixture of Ego-Graphs Contrastive Representation Learning for Multi-View Clustering [PDF](https://arxiv.org/pdf/2511.05876), [HTML](https://arxiv.org/abs/2511.05876)
### Authors
Jian Zhu,Xin Zou,Jun Sun,Cheng Luo,Lei Liu,Lingfang Zeng,Ning Zhang,Bian Wu,Chang Tang,Lirong Dai
### Background
近年来，图神经网络（GNN）在多视图聚类（MVC）方面的进展极大地推动了该领域的进步。然而，现有方法面临粗粒度图融合的问题。具体而言，当前方法通常为每个视图生成一个独立的图结构，然后在视图级别上对图结构进行加权融合，这是一种相对粗略的策略。
### Innovation
文章提出了一种新颖的Mixture of Ego-Graphs Contrastive Representation Learning（MoEGCL），它主要包含两个模块。特别地，作者提出了一种创新的Mixture of Ego-Graphs Fusion（MoEGF），它构建了ego graphs，并利用Mixture-of-Experts网络在样本级别实现细粒度的ego graphs融合，而不是传统的视图级别融合。此外，文中提出了Ego Graph Contrastive Learning（EGCL）模块，用于对齐融合表示与视图特定的表示。EGCL模块增强了来自同一聚类样本的表示相似性，进一步增强了细粒度图表示。
### Conclusion
大量的实验表明，MoEGCL在深度多视图聚类任务中取得了最先进的成果。源代码已在该链接公开。
## 909. `cs.LG` - 通过杰克逊不等式量子神经网络中周期函数的逼近率 [PDF](https://arxiv.org/pdf/2511.16149), [HTML](https://arxiv.org/abs/2511.16149)
### Authors
Ariel Neufeld,Philipp Schmocker,Viet Khoa Tran
### Background
量子神经网络（QNNs）是经典神经网络在量子计算领域的类比，由可训练参数的酉矩阵表示。受经典神经网络能够普遍逼近连续函数的启发，一些最近的研究为QNNs建立了相似的结果，包括单量子比特到多量子比特QNNs，以及混合经典-量子模型。本文研究了QNNs对于周期函数在最高纲范数下的逼近能力。
### Innovation
通过使用杰克逊不等式，将给定的周期函数通过合适的QNN实现其逼近的三角多项式。特别地，通过限制到周期函数类，实现了参数数量的二次减少，产生比文献中更好的逼近结果。此外，函数越光滑，构造用于逼近该函数的QNN所需的参数就越少。
### Conclusion
本文使用杰克逊不等式分析了QNNs在周期函数逼近中的能力，证明了通过限制函数类型可以显著减少所需的参数数量，且函数越光滑，所需参数越少。
## 910. `cs.SE` - 星际探索：通过SPACE模型探索开发人员生产力的度量标准 [PDF](https://arxiv.org/pdf/2511.20955), [HTML](https://arxiv.org/abs/2511.20955)
### Authors
Sanchit Kaul,Kevin Nhu,Jason Eissayou,Ivan Eser,Victor Borup
### Background
这项实证研究旨在揭示确定性、单维度生产力启发式方法的局限性。通过应用SPACE框架并利用大规模代码仓库数据，研究团队采用严谨的统计方法，如广义线性混合模型（GLMM）和基于RoBERTa的情感分类，构建了一个综合、多维度的生产力指标。分析结果显示，负面情绪与提交频率之间存在正相关关系，表明挫折驱动的循环修正现象。此外，研究发现，通过分析贡献者互动的拓扑结构，相较于传统的基于体积的度量标准，能够更好地描绘协作动态。
### Innovation
这项研究创新地通过广泛应用的SPACE框架，结合仓库挖掘技术，并使用先进的统计和自然语言处理方法来衡量开发人员生产力。研究通过情感分析首次明确揭示了负面情绪与提交频率之间的关联，并展示了拓扑结构分析在描绘协作动态方面优于传统方法。同时，提出了一个综合生产力评分（CPS）来解决开发者效能的异质性。
### Conclusion
研究结果表明，综合生产力评分（CPS）能够更全面地评估开发人员的生产力，考虑到情绪状态和互动网络结构。这为理解和改进软件开发团队的协作模式提供了新的视角。未来研究可进一步探索不同情境下CPS的有效性和适用性。
## 911. `cs.SE` - 数据驱动方法与AI在工程设计中的应用：基于挑战与机遇的系统文献综述 [PDF](https://arxiv.org/pdf/2511.20730), [HTML](https://arxiv.org/abs/2511.20730)
### Authors
Nehal Afifi,Christoph Wittig,Lukas Paehler,Andreas Lindenmann,Kai Wolter,Felix Leitenberger,Melih Dogru,Patric Grauberger,Tobias Düser,Albert Albers,Sven Matthiesen
### Background
数据和计算智能的进步加速了数据驱动方法（DDMs）在产品开发中的应用。然而，这些方法在产品开发中的集成仍然碎片化，主要是由于不确定性，特别是在产品开发生命周期中使用哪种类型的数据驱动方法和何时使用这些方法方面缺乏清晰性。为此，研究首先通过识别正在使用的方法、开发阶段以及应用领域来调查工程设计中的数据驱动方法的使用情况。采用V模型作为产品开发框架，简化为四个阶段：系统设计、系统实施、系统集成和验证。
### Innovation
本文进行了PRISMA系统文献综述，通过Scopus、Web of Science和IEEE Xplore数据库（2014-2024年）检索了1,689篇记录，并筛选出114篇全文文章进行分析。研究发现，机器学习和统计方法是当前的主要实践，尽管深度学习的应用较少，但趋向上行。监督学习、聚类、回归分析和代理建模在设计、实施和集成系统阶段普遍存在，但在验证阶段的贡献有限。此外，研究还指出了现有应用中的关键挑战，包括模型解释性不足、跨阶段可追溯性差以及缺乏在实际条件下的验证。
### Conclusion
该综述是向设计阶段指南迈出的第一步；后续应将计算机科学算法与工程设计问题和活动进行映射。
## 912. `cs.SE` - bug detective and quality coach: developers' mental models of ai-assisted ide tools [PDF](https://arxiv.org/pdf/2511.21197), [HTML](https://arxiv.org/abs/2511.21197)
### Authors
Paolo Buono,Mary Cerullo,Stefano Cirillo,Giuseppe Desolda,Francesco Greco,Emanuela Guglielmi,Grazia Margarella,Giuseppe Polese,Simone Scalabrino,Cesare Tucci
### Background
AI辅助工具可以帮助开发者完成复杂的任务，如错误检测和代码可读性评估，尽管这些工具的技术特性已经取得了显著进步，但很少有人了解开发者们如何心理建模这些工具，以及这种心理模型如何影响信任、控制和应用。
### Innovation
该研究通过六次协同设计研讨会收集了58名开发者的心理模型，揭示了他们将错误检测工具视为'错误侦探'，提供警示但仅在存在关键问题时，同时将其视为透明、行动指导和信心提示的保证。对于代码可读性评估工具，开发者的心理模型是'质量教练'，提供情境化、个性化和逐步指导。此外，还提出了基于人本的AI在集成开发环境中的设计理念，旨在平衡干扰与支持，简洁与深度，自动化与人类自主性。
### Conclusion
该研究得出了一套人本AI设计理念，作为平衡干扰与支持、简洁与深度、自动化与人类自主性的指导原则。
## 913. `cs.SE` - 探索Android应用中的隐藏地理差异 [PDF](https://arxiv.org/pdf/2511.21151), [HTML](https://arxiv.org/abs/2511.21151)
### Authors
M. Alecci,P. Jiménez,J. Samhi,T. Bissyandé,J. Klein
### Background
尽管移动应用的演进已经被广泛研究，但地理因素对应用行为的影响仍然鲜有探讨。该论文开展了一项大规模研究，旨在揭示地理位置对基于位置的Android应用差异化的影响。
### Innovation
研究揭示了两个重要的且未被充分研究的现象，对安全性和公正性具有重要含义。首先，提出了GeoTwins，这是功能相似、共享品牌但以不同包名在不同国家发布的应用。尽管功能相似，但GeoTwins在请求权限、第三方库和隐私披露方面经常存在差异。其次，研究了Android应用打包生态系统，并揭示了部分地区存在差异，这与常见的假设相反，这些差异可能是隐藏的定制，影响应用行为甚至安全性。这些不一致具有实际后果，地理差异版本可能导致同一应用在不同地区被标记为恶意或可疑。
### Conclusion
研究发现表明移动软件存在系统性地域差异，对研究人员、开发人员、平台架构师及政策制定者具有重要意义。地理差异的应用版本可能导致在不同地区的同款应用被标记为恶意或可疑信息发生变化，影响重复性和安全、隐私及功能评估的公正性。这些隐藏的差异还引发了关于透明度和同意的伦理问题。
## 914. `cs.SE` - 微服务粒度如何影响能耗与性能？一项受控实验 [PDF](https://arxiv.org/pdf/2502.00482), [HTML](https://arxiv.org/abs/2502.00482)
### Authors
Yiming Zhao,Tiziano De Matteis,Justus Bogner
### Background
微服务架构是最常用的软件部署方式之一，具有灵活性和可扩展性的优点。然而，它们对能耗的影响尚未完全理解，通常在考虑性能和其他质量特性（QAs）时被忽视。在这一领域中，微服务粒度这一概念尚未受到足够研究。微服务粒度是指系统功能如何分布在多个服务中。
### Innovation
本文通过一项受控实验，分析了微服务粒度与能耗和性能这两项关键质量属性之间的关系。实验使用了不同规模的两个开源微服务系统：小型Pet Clinic系统和大型Train Ticket系统。实验结果揭示了微服务粒度、系统规模、能耗和性能之间的复杂关系。实验结果有助于更好地理解如何设计微服务架构。
### Conclusion
微服务从业者在进行与粒度相关的决策时，特别是对于大规模系统，应该考虑我们的发现。
## 915. `cs.SE` - 大型语言模型在单元测试生成中的应用：成就、挑战及未来之路 [PDF](https://arxiv.org/pdf/2511.21382), [HTML](https://arxiv.org/abs/2511.21382)
### Authors
Bei Chu,Yang Feng,Kui Liu,Zifan Nan,Zhaoqiang Guo,Baowen Xu
### Background
单元测试是验证软件和减少回归风险的重要但耗时的技术。尽管经典的自动化方法能够有效地探索程序结构，但它们往往缺乏生成现实输入和断言所需的语义信息。大型语言模型通过利用其代码语义和编程模式的数据驱动知识来解决这一限制。
### Innovation
本文提出了一种基于单元测试生成生命周期的统一分类法，将大型语言模型视为需要系统工程技术约束的概率生成器。研究发现，提示工程策略因其灵活性已成为实现的主要利用策略。此外，迭代验证和修复循环已成为确保稳健可用性的标准机制，并显著提高了编译和执行通过率。但是，生成测试的弱故障检测能力和缺乏标准化评估基准仍然是重大挑战。
### Conclusion
本文为未来研究提出了一个路线图，强调向自主测试代理和传统软件工程工具相结合的混合系统的进步。该综述为研究人员和实践者提供了将大型语言模型的潜在能力转换为工业级测试解决方案的全面视角。
## 916. `cs.SE` - MigGPT: 利用大型语言模型实现跨版本Linux内核树外补丁的自动化迁移 [PDF](https://arxiv.org/pdf/2504.09474), [HTML](https://arxiv.org/abs/2504.09474)
### Authors
Pucheng Dang,Di Huang,Dong Li,Kang Chen,Yuanbo Wen,Qi Guo,Xing Hu
### Background
内核树外补丁对于适应新硬件或实现特定功能至关重要，但维护和更新这些补丁需要大量经验丰富的工程师的努力。虽然大型语言模型（LLMs）在多个领域取得了显著进展，展示了其在自动化内核树外补丁迁移中的潜力，但实证结果显示，LLMs在理解和定位不完整代码上下文及迁移点方面存在困难。
### Innovation
我们提出了 MigGPT 框架，采用新颖的代码指纹结构保留代码片段信息，并集成了三项精心设计的模块，旨在提高内核树外补丁的迁移准确性和效率。此外，我们建立了一个基于真实项目的基准测试，以评估LLMs的能力。结果表明，MigGPT 显著优于直接应用原始LLM，平均完成率为74.07%。
### Conclusion
通过 MigGPT 框架，我们提高了内核树外补丁的迁移准确性和效率，展示了大型语言模型在自动化迁移领域的潜力。
## 917. `cs.SE` - 为LLMs轻量级模型编辑以纠正过时API推荐 [PDF](https://arxiv.org/pdf/2511.21022), [HTML](https://arxiv.org/abs/2511.21022)
### Authors
Guancheng Lin,Xiao Yu,Jacky Keung,Xing Hu,Xin Xia,Alex X. Liu
### Background
大型语言模型（LLMs）在代码完成任务中表现出色，但这些模型的知识受到训练数据时效性的限制，通常包含过时的API。虽然重新训练LLMs可以在更新的代码库上提升API知识，但这非常耗计算资源。最近出现了轻量级模型编辑方法，这对于有效修正LLMs中的特定知识非常高效，但尚未明确这些方法是否能够有效更新过时API知识，使编辑后的模型能够生成最新的API。研究者为解决这一问题，应用10种最先进的编辑技术到三个LLM（Qwen2.5-Coder、StarCoder2和DeepSeek-Coder）中，以更新其中的过时API知识。
### Innovation
研究引入了一套名为EDAPIBench的专用基准，包含来自8个流行Python库的过时API，超过70个API和3000余个编辑实例。研究发现，参数高效的微调方法AdaLoRA在使编辑后的模型生成正确的、最新的API方面表现最佳，但在具体性（即编辑对未目标知识的影响）方面有所欠缺。为了解决这一问题，研究提出了AdaLoRA-L，定义了“通用API层”（存储通用知识，且未编辑的层）和“具体API层”（仅针对目标API层，存储API特定知识），从而显著提高了具体性，同时在其他评估指标方面保持了相似的性能。
### Conclusion
研究表明，AdaLoRA-L方法在提高具体性方面表现显著，同时保持了其他评估指标的竞争力，提供了一种有效的更新LLMs过时API知识的方法。
## 918. `cs.SE` - SV-LIB 1.0：软件验证任务的一种标准交换格式 [PDF](https://arxiv.org/pdf/2511.21509), [HTML](https://arxiv.org/abs/2511.21509)
### Authors
Dirk Beyer,Gidon Ernst,Martin Jonáš,Marian Lingsch-Rosenfeld
### Background
在过去二十年中，已经投入了大量的研究和开发工作来开发用于个别语言（如C、C++和Java）的验证工具。虽然许多使用的验证方法实际上是语言独立的，但允许将这些实现用于其他编程和建模语言的技术转移可以帮助更好地利用现有的验证工具。
### Innovation
提出了SV-LIB，这是一种用于软件验证任务的交换格式和中间语言，包括程序、规范和验证者。它基于熟知的命令式编程语言概念，并使用SMT-LIB表示程序中使用的表达式和类型。此外，SV-LIB还定义了SV-LIB程序的验证者格式，以及验证者验证任务的规范方法。
### Conclusion
本文介绍了SV-LIB 1.0格式的设计目标、语法和非形式化语义。计划未来版本添加形式语义和并发扩展。
## 919. `cs.SE` - 从代码异味到最佳实践：解决PyTorch、TensorFlow和Keras中的资源泄漏 [PDF](https://arxiv.org/pdf/2511.15229), [HTML](https://arxiv.org/abs/2511.15229)
### Authors
Bashar Abdallah,Martyna E. Wojciechowska,Gustavo Santos,Edmand Yu,Maxime Lamothe,Alain Abran,Mohammad Hamdaqa
### Background
现有机器学习（ML）研究主要关注模型性能指标，较少考虑ML应用的长期可持续性和资源效率。虽然高性能是必不可少的，但高效的资源配置管理对于稳健部署同样至关重要。因此，研究者们通过系统地识别导致ML应用资源泄漏的代码异味来填补这一空白。通过对PyTorch、TensorFlow和Keras等主要ML框架的开发者讨论和实际代码片段进行经验性调查，研究发现在PyTorch中存在30种与资源泄漏相关的代码异味，在TensorFlow/Keras中存在16种代码异味。这些代码异味按照其根本原因以及框架特定特征进行分类，并针对每种代码异味提出了最佳实践，最终形成了50种降低资源泄漏和提升效率的代码模式。为了保证研究结果的有效性，研究采用了三阶段验证过程：独立的分析、作者之间的共识讨论。
### Innovation
这是第一个全面研究主要ML框架中的资源泄漏代码异味的研究，并提出可操作的最佳实践来缓解这些问题。该研究支持开发人员构建更高效、更可持续的ML应用，为资源泄漏的底层原因提供了结构化的视角。
### Conclusion
研究揭示了在PyTorch、TensorFlow和Keras等主要ML框架中与资源泄漏相关的代码异味，并提出了相应的编码模式和最佳实践，有助于推动更高效和可持续的ML应用开发。
## 920. `cs.SE` - Quo Vadis, Code Review? Exploring the Future of Code Review [PDF](https://arxiv.org/pdf/2508.06879), [HTML](https://arxiv.org/abs/2508.06879)
### Authors
Michael Dorner,Andreas Bauer,Darja Šmite,Lukas Thode,Daniel Mendez,Ricardo Britto,Stephan Lukasczyk,Ehsan Zabardast,Michael Kormann
### Background
一直以来，代码审查都是协作软件工程中的核心实践。然而，未来的发展方向仍然未明朗。本文研究了当前专业开发者在代码审查中的体验以及他们对未来五年内代码审查可能发生的改变的预期。
### Innovation
本文进行了一项针对5家软件驱动公司的100名开发者的调查，收集了当前的审查投入情况，审查的对象以及未来实践的期望。发现开发人员预计代码审查将继续保持重要性，且可能涉及更多的不同类型的代码审查项目。几乎所有受访者都预计未来将有大规模的语言模型（LLMs）成为代码审查的参与者，这带来了人机交互的新挑战。
### Conclusion
长远来看，大规模的语言模型参与可能侵蚀人类的理解、责任和信任。因此，代码审查可能会成为初步显现软件工程中AI挑战的窗口。
## 921. `cs.SE` - LLMs for Automated Unit Test Generation and Assessment in Java: The AgoneTest Framework [PDF](https://arxiv.org/pdf/2511.20403), [HTML](https://arxiv.org/abs/2511.20403)
### Authors
Andrea Lops,Fedelucio Narducci,Azzurra Ragone,Michelantonio Trizio,Claudio Bartolini
### Background
单元测试在软件开发中是必要的但耗费资源的步骤，它确保代码单元能够正确运行。本文介绍了一个名为AgoneTest的自动化评估框架，用于评估大型语言模型（LLMs）生成的Java单元测试。AgoneTest旨在通过一种标准化的端到端评估流程支持研究人员和开发者对不同LLM和提示策略进行比较。目前未提出新型的测试生成算法，而是提供了一个用于评估的框架。
### Innovation
引入了Classes2Test数据集，用于映射待测试的Java类及其对应的测试类，并集成高级评估指标，如变异分数和测试异味，提供全面评估。实验结果表明，对于能够编译的测试集，LLM生成的测试能够与甚至超过人类编写的测试在覆盖率和缺陷检测方面。
### Conclusion
我们的研究表明，增强的提示策略有助于提高测试质量，AgoneTest强调了LLMs在软件测试领域的潜力，并为未来模型设计、提示工程和测试实践改进提供了见解。
## 922. `cs.SE` - 关于降低能耗的微服务策略和模式的有效性：一项关于权衡关系的实验研究 [PDF](https://arxiv.org/pdf/2501.14402), [HTML](https://arxiv.org/abs/2501.14402)
### Authors
Xingwen Xiao,Chushu Gao,Justus Bogner
### Background
微服务架构已经在软件行业中确立。然而，环境法对可持续性的要求以及软件的高能耗导致了提高这些系统能效的重要性日益增强。尽管已有针对架构策略和模式的提议，但它们的实际有效性和与其他质量属性（如性能和可维护性）之间的潜在权衡仍不清楚。
### Innovation
本文采用开源在线精品商城系统进行了受控实验，研究了三种策略和三种模式对降低能量消耗的效用以及与其他质量属性之间的潜在权衡。结果显示，不同的策略和模式在不同请求负载水平下，对能源消耗的影响各不相同，并对性能和可维护性产生了不同程度的影响。
### Conclusion
某些策略能够在降低能耗的同时改善性能，但通常会以牺牲可维护性为代价，例如通过更多的代码重复和模块耦合。总的来说，这些策略在高负载时显著降低了能耗，但大多数情况下牺牲了其他质量属性。这表明，实现能效的真正挑战不仅仅是降低微服务的能耗，而是如何同时提高其他方面。
## 923. `cs.SE` - 从基础原理探讨分布式计算 [PDF](https://arxiv.org/pdf/2506.12959), [HTML](https://arxiv.org/abs/2506.12959)
### Authors
Kenneth Odoh
### Background
这本书旨在为广泛的不同受众群体提供帮助，包括希望成为工程师的初学者、研究领域资深的研究人员以及各类专业人士。作者出于对使分布式计算的核心概念易于理解的热情，进行了一项旨在为来自各种背景的个人提供有价值见解的重要工作。该书探讨了分布式系统的底层工作原理，并提供了多个基础算法的完整实现。
### Innovation
该书针对多个层次的受众，通过具体的实现案例，提供了关于分布式计算核心概念的深入浅出的解释。无论是理论基础还是实际应用方面有所专长的读者，都能从中获益。
### Conclusion
本书提供了一个关于分布式计算的基础框架，帮助读者了解分布式系统的运行原理，并提供了可以实践的算法实现，使读者能够在不同层面上理解和应用分布式计算的知识。该书强调了从基础原理进行探讨的重要性，能够提高读者对分布式计算的理解和应用能力。
## 924. `cs.SE` - 多代理系统在软件工程中数据集适应的能力、局限性和未来方向 [PDF](https://arxiv.org/pdf/2511.21380), [HTML](https://arxiv.org/abs/2511.21380)
### Authors
Jingyi Chen,Xiaoyan Guo,Songqiang Chen,Shing-Chi Cheung,Jiasi Shen
### Background
在软件工程（SE）研究中，自动化适应不同数据集的研究成果对于扩大规模和提高可重现性至关重要，但这一领域尚未得到充分的研究。最近，基于大型语言模型（LLM）的多代理系统（如GitHub Copilot的代理模式）的发展，为自动化复杂开发工作流程提供了新的机会，通过协调推理、代码生成和工具交互。本文通过首次实证研究了最先进的多代理系统在数据集适应任务中的表现。
### Innovation
文章评估了由GPT-4.1和Claude Sonnet 4支持的Copilot在适应SE研究数据库集（如ROCODE和LogHub2.0）中的表现。通过五阶段评估管道（文件理解、代码编辑、命令生成、验证和最终执行），测量成功率，分析失败模式，并评估旨在增强代理性能的提示干预措施。研究结果显示，当前系统可以识别关键文件并生成部分适应，但很少能够生成功能正确的实现。提示级别干预措施（如提供执行错误消息和参考代码），尤其显著提高了与真实值的结构相似性（从7.25%增加到67.14%），突显了上下文和反馈驱动指导的重要性。
### Conclusion
本文研究揭示了当前多代理LLM系统在数据集适应中的潜力和局限性，并为未来SE研究中构建更可靠的自我修正代理提供了具体的方向。
## 925. `cs.SE` - 支持研究软件的机构政策路径：全球趋势与地方实践 [PDF](https://arxiv.org/pdf/2509.26422), [HTML](https://arxiv.org/abs/2509.26422)
### Authors
Michelle Barker,Jeremy Cohen,Pedro Hernández Serrano,Daniel S. Katz,Kim Martin,Dan Rudmann,Hugh Shanahan
### Background
研究软件对现代科学至关重要，但许多研究执行组织缺乏支持其发展的连贯政策。尽管软件在科研成果中的核心作用，它及其相关人员却常被排除在机构政策之外。研究指出现有政策中的漏洞，尤其是对研究软件人员支持的不足，旨在通过纳入软件的政策框架确保其受到认可、维护并符合更广泛的研究目标。
### Innovation
文章探讨了研究组织研究软件（PRO4RS）工作组的工作，提出了一个三层框架来指导政策制定，并建议机构评估现有实践、采纳国际声明并参与利益相关方以推动软件的承认。通过制定和支持更强有力的机构政策，可以促进良好实践、推动合作、支持可重复性并加强研究人员的发展，从而最大化机构价值和研究影响力，使组织成为开放、可靠、以软件驱动的科学的领导者。
### Conclusion
机构应评估现有做法，采纳国际声明，并与利益相关者合作，从而加强软件的政策，促进良好实践，推动合作，并加强研究人员的发展，以最大化机构价值和研究影响力，使组织成为开放、可靠、以软件驱动的科学的领导者。
## 926. `cs.SE` - Co-PatcheR: 使用特定组件的小推理模型实现协作软件修复 [PDF](https://arxiv.org/pdf/2505.18955), [HTML](https://arxiv.org/abs/2505.18955)
### Authors
Yuheng Tang,Hongwei Li,Kaijie Zhu,Michael Yang,Yangruibo Ding,Wenbo Guo
### Background
近年来，通用大型语言模型（LLMs）在软件修复任务中的成功促使研究者开始训练专门的修复模型。大多数研究致力于训练一个模型来涵盖修复管道中的所有端到端任务（包括问题定位、修复生成和修复验证）。然而，这小模型难以完成所有任务，因为不同子任务具有不同的工作流程和需要不同的专业知识。目前的尖端方法在SWE-bench-Verified上仅能达到41%的问题解决率。
### Innovation
本文提出了Co-PatcheR，第一个使用特定组件的小型专门推理模型实现的协作软件修复系统。文章的关键创新点在于特定任务设计和训练方法。具体来说，率先训练用于定位和修复生成的模型，通过两阶段流程进行定位，并结合生成和批评。然后提出了混合验证策略，包括两个模型分别用于生成带断言和不带断言的问题复现测试案例，并判断修复正确性，最终通过多数投票选择最佳修复。这使得Co-PatcheR能在SWE-bench-Verified上达到46%的问题解决率，仅需3个14亿参数的模型。这表明Co-PatcheR是最理想的专门模型修复系统，具有最小的训练资源和模型规模。
### Conclusion
通过全面的消融研究，验证了Co-PatcheR的方法的有效性，并验证了训练数据的数量、模型大小以及测试阶段的扩展策略的选择。Co-PatcheR实现了高效的软件修复，并证明了协作模型和专门推理模型在软件修复任务中的有效应用。
## 927. `cs.SE` - 利用大规模语言模型进行可靠和可验证的电子表格代码生成——一种基于测试驱动开发的研究框架 [PDF](https://arxiv.org/pdf/2510.15585), [HTML](https://arxiv.org/abs/2510.15585)
### Authors
Simon Thorne,Advait Sarkar
### Background
大型语言模型（LLMs），如ChatGPT，越来越多地被用于生成传统软件代码和电子表格逻辑。尽管这些模型具有强大的生成能力，但它们常常会出现严重的错误，如幻觉、微妙的逻辑不一致和语法错误，特别是在金融建模和科学计算等高风险领域，这些领域对准确性和可靠性有极高的要求。
### Innovation
本文提出了一个结构化的研究框架，将测试驱动开发（TDD）这一成熟的软件工程实践与LLM驱动的生成相结合，以提高生成输出的正确性、可靠性和用户信心。研究假设“先测试”方法可以为LLM输出提供技术和认知上的指导，引导其向更准确、可验证和易于理解的解决方案发展。框架涵盖从电子表格公式生成到Python脚本语言再到强类型语言如Rust的不同编程背景，并包括明确的实验设计、参与者组、评估指标和基于TDD的激励示例。
### Conclusion
通过强调测试驱动思维，我们旨在提高计算思维、提示工程技能和用户参与度，特别是对通常缺乏正规编程培训但面临严重逻辑错误后果的电子表格用户尤其有益。我们邀请合作以进一步完善并实证评估这一方法，最终旨在建立负责任且可靠的LLM集成，应用于教育和职业发展实践中。
