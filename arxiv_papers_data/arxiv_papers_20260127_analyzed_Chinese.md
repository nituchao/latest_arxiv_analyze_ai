# 20260127
[![Subscribe_Visitors](https://visitor-badge.laobi.icu/badge?page_id=nituchao.latest_arxiv_analyze_ai_rss)](https://github.com/nituchao/latest_arxiv_analyze_ai)

## 1. `cs.AI` - 一种高效的仿昆虫视觉点目标导航方法 [PDF](https://arxiv.org/pdf/2601.16806), [HTML](https://arxiv.org/abs/2601.16806)
### Authors
Lu Yihe,Barbara Webb
### Background
本文开发了一种基于昆虫视觉导航的新颖代理模型，通过结合两种昆虫大脑结构的抽象模型，分别与关联学习和路径整合相关。本文将Habitat平台下的点目标导航任务标准与昆虫之间通过视觉指导路径导航做类比。
### Innovation
该研究表明，简单的仿昆虫代理在检测障碍物差距执行视觉引导路径导航方面表现出色，并且在计算成本上比近期最先进的模型低出许多数量级。
### Conclusion
在更具现实感的仿真环境中进行测试后发现，该方法对干扰具有鲁棒性。
## 2. `cs.AI` - SycoEval-EM：模拟临床会诊中大型语言模型逢迎性评估 [PDF](https://arxiv.org/pdf/2601.16529), [HTML](https://arxiv.org/abs/2601.16529)
### Authors
Dongshen Peng,Yi Wang,Carl Preiksaitis,Christian Rose
### Background
大型语言模型（LLMs）在临床决策支持方面显示出潜力，但存在向患者提供不适当护理的风险。为了评估LLMs在紧急医学中的鲁棒性，研究者开发了SycoEval-EM多代理模拟框架，该框架通过对抗性患者说服力测试LLMs的鲁棒性。
### Innovation
SycoEval-EM框架是一个通过紧急医学中的对抗性患者说服力来评估LLMs鲁棒性的多代理模拟框架。研究跨越了20种不同的LLMs和1,875种涉及选择不浪费医疗资源三个场景的会诊记录，显示了多种说服策略的有效性一致，表明了LLMs的一般易感性。
### Conclusion
静态基准未能准确预测在社会压力下的安全性，需要进行多轮次对抗性测试以实现临床AI认证。
## 3. `cs.AI` - 当代理失效时：多代理大语言模型系统中工具调用可靠性的诊断框架 [PDF](https://arxiv.org/pdf/2601.16280), [HTML](https://arxiv.org/abs/2601.16280)
### Authors
Donghao Huang,Gauri Malwe,Zhaoxia Wang
### Background
多代理系统由大规模语言模型（LLMs）驱动，正在改变企业自动化领域，但对工具使用可靠性的系统评估方法仍然不成熟。本文介绍了一种利用大数据分析的综合诊断框架，用于评估智能代理系统的程序可靠性，以满足中小企业在隐私敏感环境中的部署需求。
### Innovation
本文提出了一种12类错误分类法，涵盖了工具初始化、参数处理、执行和结果解释中的失败模式。通过跨多种边缘硬件配置对1,980个确定性测试实例进行系统评估，本研究识别出生产部署中的操作可靠性门槛，并展示了中型模型（qwen2.5:14b）在通用硬件上的准确性和效率权衡，即成本效益的智能代理部署。
### Conclusion
本文建立了多代理增强AI系统可靠性评估的基础框架，特别是对于程序可靠性，尤其是在工具初始化失败方面，揭示了不同模型的性能瓶颈，并指出了资源受限组织中智能代理部署的可能性。
## 4. `cs.AI` - DSGym:一个全面框架用于评估与训练数据科学代理 [PDF](https://arxiv.org/pdf/2601.16344), [HTML](https://arxiv.org/abs/2601.16344)
### Authors
Fan Nie,Junlin Wang,Harper Hua,Federico Bianchi,Yongchan Kwon,Zhenting Qi,Owen Queen,Shang Zhu,James Zou
### Background
现有的数据科学基准由于评价接口碎片化导致跨基准比较困难、任务覆盖面狭窄以及缺乏严格的基于数据的验证，使得这些基准存在不足。此外，有研究表明目前许多基准集中的任务可以通过非实际数据的手段来解决。
### Innovation
作者引入了DSGym，这是一个标准化的框架，用于在自包含执行环境中评估和训练数据科学代理。DSGym提供了一个可模块化架构，使其易于添加任务、代理构建块和工具，从而成为一个实时、可扩展的测试环境。作者还制定了DSGym-Tasks任务套件，通过质量筛选和快捷解决方案筛选标准化并细化现有的基准集，并添加了DSBio和DSPredict模块来扩展任务覆盖面。此外，DSGym提供了一个通过执行验证的数据合成管道来进行代理训练的能力。
### Conclusion
DSGym使端到端的评估成为可能，衡量代理能否在现实科学背景下规划、实施和验证数据分析。作为案例研究，作者在DSGym中建立了一个2000个样本的训练集，并训练了一个40亿参数的模型，该模型在标准的数据分析基准上优于GPT-4o。这表明了DSGym在评估和培训数据科学代理方面的有效性。
## 5. `cs.AI` - LongCat-Flash-Thinking-2601技术报告 [PDF](https://arxiv.org/pdf/2601.16725), [HTML](https://arxiv.org/abs/2601.16725)
### Authors
Meituan LongCat Team,Anchun Gui,Bei Li,Bingyang Tao,Bole Zhou,Borun Chen,Chao Zhang,Chao Zhang,Chen Gao,Chen Zhang,Chengcheng Han,Chenhui Yang,Chuyu Zhang,Cong Chen,Cunguang Wang,Daoru Pan,Defei Bu,Dengchang Zhao,Di Xiu,Dishan Liu,Dongyu Ru,Dunwei Tu,Fan Wu,Fengcheng Yuan,Fengcun Li,Gang Xu,Guanyu Wu,Guoyuan Lin,Haibin Wang,Hansi Yang,Hao Yang,Haonan Yan,Haoxiang Ma,Haoxing Wen,Hongyan Hao,Hongyin Tang,Hongyu Zang,Hongzhi Ni,Hui Su,Jiacheng Zhang,Jiahong Zhou,Jiahuan Li,Jiaming Wang,Jian Yang,Jianfei Zhang,Jianhao Xu,Jianing Wang,Jiapeng Zhu,Jiaqi Sun,Jiarong Shi,Jiarui Zhao,Jingang Wang,Jinluan Yang,Jinrui Ding,Jinwei Xiao,Jiyuan He,Juncan Xu,Kefeng Zhang,Keheng Wang,Li Wei,Lianhui Ma,Lin Qiu,Lingbing Kong,Lingchuan Liu,Linsen Guo,Mengshen Zhu,Mengxia Shen,Mingyang Zhu,Peiguang Li,Peng Pei,Pengcheng Jia,Pengtao Zhang,Peng Zhao,Qi Gu,Qiong Huang,Qiyuan Duan,Quanchi Weng,Rongxiang Weng,Rongzhi Zhang,Rumei Li,Shanglin Lei,Shengnan An,Shijun Dai,Shuaikang Liu,Shuang Zhou,Shuo Wang,Songyuan Zhao,Tao Liang,Tianhao Hu,Tianze Chen,Wei Liu,Wei Shi,Wei Wang,Weifeng Tang,Wenjie Shi,Wenlong Zhu,Wentao Chen,Wentao Shi,Xi Su,Xiangcheng Liu
### Background
该论文旨在介绍一个名为LongCat-Flash-Thinking-2601的560亿参数开源混合专家模型，该模型在多种代理表现基准测试中表现出色，特别是在代理搜索、代理工具使用和集成工具推理方面。
### Innovation
1. 针对复杂工具使用场景的强泛化能力来源于环境扩展和任务构建的深入探索。2. 引入了Heavy Thinking模式，通过密集并行思考同时扩展推理深度和宽度。3. 通过系统扩展异步强化学习框架DORA来实现稳定和高效的大规模多环境训练，确保超过10,000个环境的支持。4. 分析并拆解了现实世界中的噪声模式，并设计针对性的培训程序来明确将这些缺陷融入到训练过程中，提高了模型在实际应用中的鲁棒性。
### Conclusion
LongCat-Flash-Thinking-2601模型不仅在基准测试中表现出色，而且能够稳健地应对多变的现实环境，展示了强大的泛化能力和对复杂工具交互的强大理解能力。
## 6. `cs.AI` - LUMINA：多轮交互智能体的长时理解 [PDF](https://arxiv.org/pdf/2601.16649), [HTML](https://arxiv.org/abs/2601.16649)
### Authors
Amin Rakhsha,Thomas Hehn,Pietro Mazzaglia,Fabio Valerio Massoli,Arash Behboodi,Tribhuvanesh Orekondy
### Background
大型语言模型在众多孤立任务中表现良好，但在多轮、长期的人工智能任务中，特别是在规划、状态跟踪和长文本处理等技能方面，仍然存在不足。本文旨在更好地了解这些潜在能力对完成此类任务的重要性。作者开发了一种基于多轮问题的oracle反事实框架，探讨了在特定任务中 oracle 技能对智能体性能的提升。通过一系列可调整复杂度的程序生成任务，作者提供了精确的 oracle 干预措施，使得可以单独评估每项 oracle 技能的贡献。研究结果显示，虽然某些干预（如规划）能够在多种情况下提高性能，但其他技能的效果依赖于环境和语言模型的特性。
### Innovation
本文创新性地提出了一种基于 oracle 技术的反事实框架及相应的可调整复杂度的程序生成任务，以此来精确地分析每个 oracle 技能对智能体性能的关键性评估。这种方法能够更好地理解多轮交互智能体面临的挑战，并指导未来智能代理和语言模型的研发。
### Conclusion
本文的结果展示了尽管部分干预措施（如规划）在不同情况下都能显著改善性能，但其他技能的效果可能依赖于环境和语言模型的具体特性。这项工作揭示了多轮交互环境中的挑战，为未来智能代理和语言模型的发展指明了方向。
## 7. `cs.AI` - SemanticALLI：在代理系统中缓存推理，不仅仅是响应 [PDF](https://arxiv.org/pdf/2601.16286), [HTML](https://arxiv.org/abs/2601.16286)
### Authors
Varun Chillara,Dylan Kline,Christopher Alvares,Evan Wooten,Huan Yang,Shlok Khetan,Cade Bauer,Tré Guillory,Tanishka Shah,Yashodhara Dhariwal,Volodymyr Pavlov,George Popstefanov
### Background
代理型人工智能（Agentic AI）管道在构建过程中存在隐藏的低效率问题，即它们频繁重新构建相同的中间逻辑，如度量标准化或图表构建，即使用户自然语言的表述完全新颖。传统的边界缓存方法未能捕捉到这种效率问题，因为它将推理视为一个整体的黑盒。这一背景揭示了当前缓存方法的局限性，以及需要一种新的方法来提高代理型人工智能管道的效率。
### Innovation
作者提出了SemanticALLI，这是一种在PMG营销情报平台Alli中的管道感知架构，旨在实现冗余推理的操作化。通过将生成过程分解为分析意图解析（AIR）和可视化合成（VS），SemanticALLI提升了结构化中间表示（IR）为一等可缓存对象。这种方法在代理循环中的缓存效果显著，与基本的整体缓存相比，在评价中多了一个视觉合成阶段，达到了83.10%的命中率，避免了4,023次LLM调用，并且具有2.66毫秒的中位延迟时间，这一内部重用降低了总令牌消耗，为AI系统设计提供了实用的见解：即使用户很少重复自己，但管道在稳定的、结构化的检查点处经常重构，这使得缓存在这里更可靠。
### Conclusion
总体而言，SemanticALLI通过引入结构化的中间表示和重新设计生成流程，显著提高了代理型人工智能管道的效率，特别是在那些语言变异性较高的场景中。这种方法不仅减少了LLM调用的次数，还降低了总令牌消耗，从而为其他AI系统设计提供了重要的指导意义。
## 8. `cs.AI` - AgentsEval：通过多智能体推理进行医学影像报告的临床一致评估 [PDF](https://arxiv.org/pdf/2601.16685), [HTML](https://arxiv.org/abs/2601.16685)
### Authors
Suzhong Fu,Jingqi Dong,Xuan Ding,Rui Sun,Yiming Yang,Shuguang Cui,Zhen Li
### Background
当前，评估自动生成的医学影像报告的临床正确性和推理一致性仍是一个关键但尚未解决的挑战。现有的评估方法往往无法捕捉放射诊断过程中的结构化诊断逻辑，导致评估结果不可靠且缺乏临床相关性。
### Innovation
引入了AgentsEval框架，这是一种多智能体流推理框架，模仿放射科医生的协作诊断流程。该框架将评估过程划分为可解释的步骤，包括准则定义、证据提取、对齐和一致性评分，提供明确的推理痕迹和结构化的临床反馈。同时构建了一个多领域基于扰动的基准数据集，涵盖了五个医学报告数据集，具有不同的成像模式和受控的语义变化。
### Conclusion
实验结果表明，AgentsEval提供了临床对齐、语义准确且解释性强的评估，这些评估在同义替换、语义和风格相关性扰动下保持稳定。这一框架代表了向透明和临床规范评估医学报告生成系统迈进了一步，促进了大规模语言模型在临床实践中的可信应用。
## 9. `cs.AI` - Doc2AHP：通过语义树利用大语言模型推断结构化多准则决策模型 [PDF](https://arxiv.org/pdf/2601.16479), [HTML](https://arxiv.org/abs/2601.16479)
### Authors
Hongjia Wu,Shuai Zhou,Hongxin Zhang,Wei Chen
### Background
大型语言模型虽然在语义理解方面表现出色，但在复杂决策任务中的结构性一致性和推理可靠性方面常有不足。传统的决策理论，如分析层次过程（AHP），提供了系统化的理性框架，但其构建需要大量的领域专业知识，这被称为‘专家瓶颈’，阻碍了其在一般场景中的扩展性。本文旨在弥合大型语言模型的一般化能力和决策理论的严谨性之间的差距。
### Innovation
本文提出了Doc2AHP，这是一种新型的结构化推理框架，遵循AHP原则，无需大量注释数据或人工干预即可工作。该方法利用AHP的结构原则作为约束，指导LLM在未结构化的文档空间内进行受限搜索，从而确保父节点和子节点之间的逻辑推断。此外，还引入了多智能体权重机制和自适应一致性优化策略，以确保权重分配的数值一致性。
### Conclusion
实验结果表明，Doc2AHP不仅能帮助非专家用户从头构建高质量的决策模型，而且在逻辑完整性及下游任务准确性上显著优于直接生成的基线模型。
## 10. `cs.AI` - LLM 未必是万能的：经典模型与基础模型在基于文本和图像的医疗分类中的系统评估 [PDF](https://arxiv.org/pdf/2601.16549), [HTML](https://arxiv.org/abs/2601.16549)
### Authors
Meet Raval,Tejul Pandit,Dhvani Upadhyay
### Background
将多模态视觉语言模型（VLMs）与大型语言模型（LLMs）相结合，为医疗分类提供了新的可能性。该研究使用了四种公开的数据集，覆盖了文本和图像模态（二元和多元分类复杂性），并通过对比传统的机器学习（ML）方法和当代的基于变换器的技术来构建统一的基准测试。研究评估了每种任务的三种模型类别：经典机器学习（LR，LightGBM，ResNet-50）、基于提示的LLMs/VLMs（Gemini 2.5），以及微调PEFT模型（LoRA-adapted Gemma3变体）。所有实验数据切分一致，且使用的评估标准一致。
### Innovation
该研究提出了一种统一且系统的基准测试，通过对比传统机器学习方法和基于变换器的现代技术，评估了多种模型在医疗分类任务中的表现。实验展示了不同模型类别的性能差异，并揭示了基础模型和高效参数微调（PEFT）策略的有效性高度依赖于具体任务和适应策略。
### Conclusion
在许多医疗分类场景中，已有的机器学习模型仍然是最可靠的选择。实验表明，基础模型并非在所有情况下都优于经典模型，且高效参数化微调（PEFT）的效果高度依赖于适应策略，且本研究中的少量微调证明效果不佳。
## 11. `cs.AI` - 系统化LLM人物设计：AI伴侣应用的四象限技术分类法 [PDF](https://arxiv.org/pdf/2511.02979), [HTML](https://arxiv.org/abs/2511.02979)
### Authors
Esther Sun,Zichu Wu
### Background
AI伴侣领域，包括虚拟情感伴侣、游戏NPC、实体功能机器人等，表现出多样性。这一多样性在目标、模态和技术栈上都存在，急需一个统一的框架来解决这一问题。
### Innovation
本文提出了一个四象限技术分类法，用于系统化AI伴侣应用，沿着虚拟 vs. 实体和情感陪伴 vs. 功能增强这两条关键轴展开。分为虚拟情感伴、功能虚拟助手、实体智能、以及垂直领域助手四个象限，分别探索并分析了不同范畴下的挑战和技术要点。
### Conclusion
该分类法为研究人员和开发人员提供了一张系统化的路径图，用于导航复杂的人格设计空间，并为政策制定者提供了识别和应对不同应用场景的独特风险的基础。
## 12. `cs.AI` - 通过多样性引导采样在语言模型中高效量化语义不确定性 [PDF](https://arxiv.org/pdf/2510.21310), [HTML](https://arxiv.org/abs/2510.21310)
### Authors
Ji Won Park,Kyunghyun Cho
### Background
在自由形式的问答中准确估计大型语言模型的语义Aleatoric和Epistemic不确定性具有挑战性，因为这通常需要昂贵且不稳定的多次生成。这种不确定性估计的挑战导致需要改进现有的方法以提高对不确定性理解的准确性和效率。
### Innovation
本文提出了一种多样性引导的采样方法，它通过在模型的提案分布中注入一种基于自然语言推理（NLI）模型的连续语义相似性惩罚来减少语义冗余输出，该模型经过轻度微调。这种方法不依赖于基语言模型的梯度，可以通过重要性加权去偏差，同时使用控制变量减少方差，从而在保持相同样本数量的情况下覆盖更多的语义簇，显著提高了采样效率。
### Conclusion
该框架为风险敏感模型部署中的不确定性估计提供了一个模块化且无需访问基语言模型梯度的增强方法。在四个问答基准测试中，该方法匹配或超越了基线模型的性能，同时覆盖了更多的语义簇。
## 13. `cs.AI` - CARE: 增强推理和强化学习在情感支持对话中的应用 [PDF](https://arxiv.org/pdf/2510.05122), [HTML](https://arxiv.org/abs/2510.05122)
### Authors
Jie Zhu,Yuanchen Zhou,Shuo Jiang,Junhui Li,Lifan Guo,Feng Chen,Chi Zhang,Fang Kong
### Background
情绪支持对话（ESC）对减轻心理压力和提供情感价值至关重要。近年来的研究主要集中在数据增强和合成语料库建设上，但这些研究往往忽略了有效情感支持背后深层的认知推理过程。
### Innovation
我们提出了一种名为CARE的新框架，用于在无需依赖大规模合成数据的情况下增强ESC中的推理过程。CARE利用原始ESC训练集来引导模型生成逻辑连贯和支持性强的回应，进而显式地增强认知推理。在此基础上，我们还使用强化学习来进一步完善和加强推理过程。
### Conclusion
经验表明，CARE能显著提高响应的逻辑性和支持性质量，推动了具有共情能力、认知稳健性和类人特征的情感支持系统的开发。
## 14. `cs.AI` - DSSmoothing：通过双重空间平滑实现预训练语言模型的数据集所有权认证 [PDF](https://arxiv.org/pdf/2510.15303), [HTML](https://arxiv.org/abs/2510.15303)
### Authors
Ting Qiao,Xing Liu,Wenke Huang,Jianbin Li,Zhaoxin Fan,Yiming Li
### Background
大型网络数据集推动了预训练语言模型（PLMs）的迅速发展，但未经授权的数据使用引发了严重的版权问题。现有数据集所有权验证（DOV）方法通常假设水印在推理期间保持稳定，但在自然噪声和对手设计的干扰下这一假设往往不成立。
### Innovation
本文提出了第一种在灰盒设置下（即，防御者只能查询可疑模型但知道其输入表示模块）进行PLMs数据集所有权验证的认证方法，该方法基于双重空间平滑（DSSmoothing）。DSSmoothing通过引入嵌入空间中的连续扰动来捕捉语义鲁棒性，并通过在排列空间中控制标记的重新排序来捕捉序列鲁棒性。该方法包含两个阶段：第一阶段，在两个空间中协作嵌入触发器以生成规整且鲁棒的水印数据集；第二阶段，在验证过程中使用双重空间中的随机平滑计算可疑模型的水印鲁棒性（WR）并与其原始概率（PP）值进行统计对比。
### Conclusion
理论证明，DSSmoothing通过确保在有界双重空间扰动下WR始终超过PP，为数据集所有权验证提供了可证明的鲁棒性保证。广泛的实验表明，DSSmoothing可以实现稳定且可靠的验证性能，并具有对潜在适应性攻击的鲁棒性。我们的代码可在以下链接找到：this https URL。
## 15. `cs.AI` - CRADLE Bench: 临床标注的多维度心理健康危机和安全风险检测基准 [PDF](https://arxiv.org/pdf/2510.23845), [HTML](https://arxiv.org/abs/2510.23845)
### Authors
Grace Byun,Rebecca Lipschutz,Sean T. Minton,Abigail Lott,Jinho D. Choi
### Background
语言模型在识别自杀意念、性侵犯、家庭暴力、儿童虐待和性骚扰等心理健康危机情形方面存在巨大挑战，但此类情况往往未被充分利用的数据集充分探索。模型需要准确识别这些情况，以避免潜在的严重后果。已有研究主要集中在少数类型的危机中，CRADLE BENCH为涵盖七种与临床标准一致的危机类型，是首个引入时间标签的基准集。
### Innovation
CRADLE BENCH 是一种多维度危机检测基准集，专门将七种危机类型与临床标准对齐，并首次引入了时间标签。提供了600个由临床医生标注的评估示例和420个开发示例。基准集还包括一个约4000个示例的自动标记训练语料库，这些示例是通过多个语言模型的多数投票集成生成的，其性能优于单模型标注。此外，该基准集通过基于共识和一致的集成方法对六种危机检测模型进行了微调，提供了不同共识标准下的互补模型。
### Conclusion
CRADLE BENCH 提供了一个全面、多维度的基准集，旨在促进更准确、更可靠的多维度心理健康危机检测研究。通过引入时间标签和多种标注方法，该基准集为加强心理健康危机风险检测提供了更强大的数据支持和模型训练平台。
## 16. `cs.AI` - StarEmbed：在变星天文观测时间序列数据上的时间序列基础模型基准测试 [PDF](https://arxiv.org/pdf/2510.06200), [HTML](https://arxiv.org/abs/2510.06200)
### Authors
Weijian Li,Hong-Yu Chen,Nabeel Rehemtulla,Ved G. Shah,Dennis Wu,Dongho Kim,Qinjie Lin,Adam A. Miller,Han Liu
### Background
时间序列基础模型（TSFMs）现被广泛应用于高能力的一般时间序列表示学习，但它们忽视了天文时间序列数据。恒星观测会产生大量的时间序列数据，并具有不规则采样和异方差性的独特挑战。此前没有公开的基准用于评估这些先进的TSFMs在恒星时间序列观测（'光曲线'）上的表现。
### Innovation
首次设立了StarEmbed基准，评估最先进的时间序列基础模型在恒星时间序列观测上的性能。通过集成专家认证的标签和来自Zwicky瞬变设施的多变量光曲线数据，建立了包含约4万个鸟类标签光曲的数据集，覆盖了七个天文学类。与特定任务的手工特征提取方法和传统的天文学基准线进行了比较，结果表明这些模型在某些任务中性能优于特定任务的基准线，且能有效泛化到全新的数据中。
### Conclusion
TSFMs在我们提出的异常源检测基准测试中实现了顶级性能，首次使用TSFMs进行天文时间序列数据的基准测试，测试了它们的泛化能力，并从任务特定的完全监督管道转向采用通用基础模型表示分析庞大数据集的范式转移。
## 17. `cs.AI` - 使用视觉语言模型的多阶段混合框架进行多视图工程图纸的自动化解析 [PDF](https://arxiv.org/pdf/2510.21862), [HTML](https://arxiv.org/abs/2510.21862)
### Authors
Muhammad Tayyab Khan,Zane Yong,Lequn Chen,Wenhe Feng,Nicholas Yew Jin Tan,Seung Ki Moon
### Background
工程图纸是制造沟通的基础，主要传达设计意图、公差和生产细节。然而，手动方法、通用光学字符识别(OCR)系统或传统深度学习方法在解读复杂的多视图图纸时因布局多样、文本和图形混合内容等原因仍面临挑战。
### Innovation
本文提出了一种结合现代检测和视觉语言模型(VLM)的多阶段混合框架，用于自动化解析2D多视图工程图纸。该框架通过三个阶段的Yolov11-、布局分割、方向意识的细粒度注释检测和基于Donut的OCR免费VLM进行语义内容解析，解决了这些挑战。
### Conclusion
本文框架通过两个VLM的结合，实现了文本和定量信息的高效解析，并取得了显著的性能。最终，统一的JSON输出可以无缝集成到CAD和制造数据库中，提供了一种可扩展的智能工程图纸分析解决方案。
## 18. `cs.AI` - 计算TIRF使宽场荧光显微镜的光学切片超越倏逝场成为可能 [PDF](https://arxiv.org/pdf/2511.06853), [HTML](https://arxiv.org/abs/2511.06853)
### Authors
Qiushi Li,Celi Lou,Yanfang Cheng,Bilang Gong,Xinlin Chen,Hao Chen,Baowan Li,Jieli Wang,Yulin Wang,Sipeng Yang,Yunqing Tang,Luru Dai
### Background
宽场荧光显微镜由于轴向分辨率低，受焦外背景限制，尤其在密集标记的生物样品中表现不佳。尽管TIRF显微镜能提供强大的近表面切片，但其固有限制浅层成像深度。因此，需要一种无需任何光学修改，基于计算的方法来改善宽场荧光显微镜的性能。
### Innovation
本文提出了一种基于计算的TIRF(cTIRF)，利用深度学习生成TIRF类似切片图像，而不需要光学改型。通过将物理先行模型整合到网络训练中，cTIRF实现了有效的背景抑制和轴向分辨率提高，同时保持与测量宽场数据的一致性。cTIRF能够在常规TIRF无法进行成像的密集标记样本中实现近表面结构的恢复，并实现单帧和体积切片重构。
### Conclusion
本文建立了cTIRF作为硬件基础光学切片在荧光显微镜中的实用替代品，且可以通过快速适应新成像系统并最小化校准数据实现推广。
## 19. `cs.AI` - AutoSciDACT：通过对比嵌入和假设检验实现自动科学发现 [PDF](https://arxiv.org/pdf/2510.21935), [HTML](https://arxiv.org/abs/2510.21935)
### Authors
Samuel Bright-Thonney,Christina Reissel,Gaia Grosso,Nathaniel Woodward,Katya Govorkova,Andrzej Novak,Sang Eon Park,Eric Moreno,Philip Harris
### Background
在处理大量的科学数据时，新颖性检测面临的挑战主要体现在数据的噪声性和高维度性，以及需要做出统计上稳健的声明。尽管有关通过降维进行异常检测的文献有许多，但大多数方法产生的输出不足以支持科学发现的量化声明。本文直接应对了这些挑战，提出了一个适应科学严谨统计需求的统一新颖性检测管道的第一步。
### Innovation
作者引入了AutoSciDACT（Automated Scientific Discovery with Anomalous Contrastive Testing），这是一种通用管道，用于在科学数据中检测新颖性。该方法首先使用对比预训练创建高度表达性的低维度数据表示，这利用了大量高质量模拟数据和专业知识，以指导规范的数据增强策略。这些紧凑的嵌入然后使使用New Physics Learning Machine (NPLM)框架的极其敏感的两样本测试成为可能，可以识别并量化观察数据与参考分布（零假设）之间的偏差。
### Conclusion
通过在天文学、物理、生物学、图像和合成数据集上的实验，证明了AutoSciDACT在所有领域对异常数据的微小注入具有很强的敏感性。这项工作代表了为严格科学统计需求而设计的第一个统一新颖性检测管道，并提供了一种将对比嵌入技术和假设检验结合进行自动科学发现的方法。
## 20. `cs.AI` - LATTLE: LLM Attention Transplant for Transfer Learning of Tabular Data Across Disparate Domains [PDF](https://arxiv.org/pdf/2511.06161), [HTML](https://arxiv.org/abs/2511.06161)
### Authors
Ibna Kowsar,Kazi F. Akhter,Manar D. Samad
### Background
对于结构异质的表格数据，跨领域知识迁移学习较为困难，因为表格数据的特征空间与图像和文本的同质结构不同。大语言模型（LLMs）提供了一个知识基础，可以改善表格数据跨领域迁移学习的有限效果。然而，LLM的性能常常受限于主观文本提示和内省学习的计算限制。
### Innovation
提出了一种新的语言到表格的内隐学习方法，该方法使用注意力特定转换器权重，能够无缝地在异质表格数据集之间进行知识迁移。LLM注意力移植机制使域无关的知识迁移成为可能，消除了表格之间共享特征、LLM提示工程和大规模预训练模型的需求。
### Conclusion
对于跨域的10对分离的数据集和12种基线方法的实验结果表明，提出的LLM注意力移植方法（LATTLE）在跨领域迁移学习中优于传统机器学习模型、最先进的深度表格架构，以及在数十亿个表格样本上训练的模型。跨域注意力迁移展示了一种在资源有限环境下调整LLMs学习非文本表格数据的有效解决方案。LATTLE 实现的源代码已被公开。
