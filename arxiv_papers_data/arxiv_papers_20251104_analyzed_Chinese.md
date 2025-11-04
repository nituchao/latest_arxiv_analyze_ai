# 20251104
[![Subscribe_Visitors](https://visitor-badge.laobi.icu/badge?page_id=nituchao.latest_arxiv_analyze_ai_rss)](https://github.com/nituchao/latest_arxiv_analyze_ai)

## 1. `cs.AI` - Glia：一种启发于人类的自动化系统设计与优化的人工智能 [PDF](https://arxiv.org/pdf/2510.27176), [HTML](https://arxiv.org/abs/2510.27176)
### Authors
Pouya Hamadanian,Pantea Karimi,Arash Nasr-Esfahany,Kimia Noorbakhsh,Joseph Chandler,Ali ParandehGheibi,Mohammad Alizadeh,Hari Balakrishnan
### Background
近年来，人工智能在系统设计和优化方面取得了显著进展，但许多方法仍依赖于黑箱模型，缺乏人类专家的创造性与可解释性。本文探讨了自动化设计能否达到与人类专家相当的创造力和分析能力，尤其是在网络系统设计中。
### Innovation
提出了一种基于大语言模型（LLMs）的人工智能架构Glia，它采用了类似人类的多agent工作流，每个agent专注于推理、实验和分析，并通过评估框架将抽象推理与经验反馈相结合。Glia能够生成可解释的设计，并公开其推理过程，而不像先前的ML方法那样仅仅优化黑箱策略。在分布式GPU集群上进行的实验展示了Glia能够以更快的速度生成与人类专家同等水平的新算法，同时揭示了工作负载行为的新见解。
### Conclusion
通过将推理LLMs与结构化实验相结合，本文表明AI能够产生复杂系统问题的创新且可理解的设计。
## 2. `cs.AI` - SUSTAINABLE 平台：无缝智能农业集成以实现农艺自动化 [PDF](https://arxiv.org/pdf/2510.26989), [HTML](https://arxiv.org/abs/2510.26989)
### Authors
Agorakis Bompotas,Konstantinos Koutras,Nikitas Rigas Kalogeropoulos,Panagiotis Kechagias,Dimitra Gariza,Athanasios P. Kalogeras,Christos Alexakos
### Background
全球农业部门正在经历一场变革，受到日益增长的食品需求、气候变化和可持续实践的驱动。本文介绍了智能农业的当前解决方案、进行了比较评估，并介绍了SUSTAINABLE平台的核心功能，如卫星指数集成、实时环境数据和根据地中海葡萄园角色智能管理的任务管理。
### Innovation
SUSTAINABLE是一个智能农业平台，利用物联网（IoT）、人工智能（AI）、卫星成像和基于角色的任务编排，旨在实现高效、可追踪和可持续的农业。它特别适用于地中海葡萄园，通过集成卫星成像、实时环境数据和角色感知任务管理，提供了无缝的智能农业集成解决方案，以促进农艺的自动化。
### Conclusion
本文通过探讨当前的智能农业解决方案，进行对比分析，并介绍了SUSTAINABLE平台的关键功能，如卫星指数集成、实时环境数据和角色感知任务管理，展示了SUSTAINABLE平台在智能农业和可持续农业中的创新和应用潜力。
## 3. `cs.AI` - 认知边界在自主UAS操作中有界AI推理中的应用 [PDF](https://arxiv.org/pdf/2510.26905), [HTML](https://arxiv.org/abs/2510.26905)
### Authors
Pedro Antonio Alarcón Granadeno,Arturo Miguel Bernal Russell,Sofia Nelson,Demetrius Hernandez,Maureen Petterson,Michael Murphy,Walter J. Scheirer,Jane Cleland-Huang
### Background
随着网络物理系统的日益发展，它们越来越多地依赖于大型语言模型（LLMs）和视觉语言模型（VLMs）等基础模型来提高自主性，通过增强感知、推理和规划。然而，这些模型也带来了新的错误类型，例如幻觉、过度概括和上下文错位，导致错误和不正确的决策。目前缺乏有效的机制来管理这些错误并确保决策的准确性。
### Innovation
本文提出了一种新的概念——认知边界，用于限制AI生成决策的推理边界，同时与元认知和传统安全边界相结合。该概念需要具体的指导方针和系统的流程来定义、验证和确保其有效性。该研究填补了基于模型的自主决策系统中的认知控制空白。
### Conclusion
通过引入认知边界，本文提出了一种新的机制，以构建AI生成决策的推理边界，从而确保自主系统操作过程中的决策准确性。该方法将为未来的设计和操作提供实用的指导原则和系统流程，确保系统运行的安全性和可靠性。
## 4. `cs.AI` - 在空间数据上使用因果掩蔽：学习空间数据集的一种信息论案例 [PDF](https://arxiv.org/pdf/2510.27009), [HTML](https://arxiv.org/abs/2510.27009)
### Authors
Jared Junkin,Samuel Nathanson
### Background
语言模型传统上围绕因果掩蔽设计。但在具有空间或关系结构的领域中，因果掩蔽通常被认为是不合适的，而更倾向于使用序列线性化。关于因果掩蔽在非序列数据中是否会导致可接受的信息损失的研究较少，因为很少有领域能够同时提供空间和序列表示的数据集。
### Innovation
该研究在象棋领域探讨了因果掩蔽在空间数据上的应用，使用双向和因果注意力机制在空间（基于棋盘）和序列（基于移动）数据上训练语言模型。实验结果表明，即使使用因果掩蔽，基于空间棋盘状态训练的模型也能比基于序列数据训练的模型表现出更强的棋力。这项研究的方法论意义在于，因果掩蔽可用于训练单一模态语言模型的空间数据，并在某些领域甚至优于序列化。
### Conclusion
研究结果表明，在空间数据上使用因果掩蔽是一种有效方法，可以用于训练单一模态语言模型。虽然实验是在象棋领域进行的，但研究结果具有广泛的意义，表明因果掩蔽在处理空间数据的单模态LSTM模型训练中是可行的，并在某些领域甚至是序列化方法的优选方案。
## 5. `cs.AI` - CombiGraph-Vis：离散数学推理的精选多模态奥林匹克基准 [PDF](https://arxiv.org/pdf/2510.27094), [HTML](https://arxiv.org/abs/2510.27094)
### Authors
Hamed Mahdavi(Pennsylvania State University),Pouria Mahdavinia(Pennsylvania State University),Alireza Farhadi(Amirkabir University of Technology),Pegah Mohammadipour(Pennsylvania State University),Samira Malek(Pennsylvania State University),Majid Daliri(New York University),Pedram Mohammadipour(Amirkabir University of Technology),Alireza Hashemi(City University of New York),Amir Khasahmadi(Autodesk),Vasant Honavar(Pennsylvania State University)
### Background
最先进的大型语言模型（LLMs）在过去已经从无法解决奥林匹克证明问题发展到能够解决2025年IMO绝大多数问题，其中有的顶级系统甚至能够解决6道题目中的5道。鉴于这一进展，本文评估这些模型在评分证明方面的表现：检测错误、判断错误的严重程度、以及给予公平的得分，而不仅仅是二元的正确性评价。研究团队使用90个Gemini 2.5生成的解决方案进行评估，并使用详细的错误注解对这些解决方案进行1到4的评分，还使用了MathArena的IMO/USAMO 2025解决方案集进行评分。研究发现，这些模型可以可靠地标识出错误的解决方案，但表现出部分评分难以校准的缺陷。
### Innovation
本文引入了具有代理意识的工作流程，用于提取和分析参考解决方案，并自动生成适用于多步评分过程的问题特定评估标准。通过比较不同设计选择并评估权衡，研究者展示了这些流程在标注语料库和MathArena中的应用，最终实现了与人类评分更高的共识，并且在处理部分得分方面表现更为一致。
### Conclusion
本文提出的工作流程在注释语料库和MathArena中实现了更高的评分一致性和更高的评分一致性处理，所有代码和数据都已公开发布，为未来的相关研究提供了便利。
## 6. `cs.AI` - e1：学习适应性的推理努力控制 [PDF](https://arxiv.org/pdf/2510.27042), [HTML](https://arxiv.org/abs/2510.27042)
### Authors
Michael Kleinman,Matthew Trager,Alessandro Achille,Wei Xia,Stefano Soatto
### Background
提高AI模型的思考预算可以显著提高准确性，但是不同的问题并不需要相同的推理努力。用户可能根据输出质量和延迟及成本之间的权衡来选择分配不同的推理努力。为了有效利用这种权衡，用户需要对查询的推理量有细粒度的控制，但现有方法很少能够提供这种控制。现有方法需要用户指定绝对数量的所需令牌数，这要求用户事先知道问题的难度来为查询设置适当的令牌预算。
### Innovation
本文提出了一种自我适应的强化学习方法——自适应努力控制（Adaptive Effort Control）。该方法训练模型根据每个查询当前平均思考链长度的用户指定比例来使用令牌。该方法避免了特定数据集和阶段的调优，并在成本-准确度折中曲线上优于标准方法。用户可以在推理时间动态调整成本-准确度折中的连续努力参数。实验证明，该模型能够自动学习按任务难度分配资源，并在参数从1.5B到32B的各个模型规模中，通过这种方法可以实现基模型用于强化学习训练时约3倍的思考链长度的减少，同时保持或提升性能。
### Conclusion
该方法通过自我适应的强化学习训练模型，实现用户在推理时对推理努力的动态微调。在不同规模的模型上都显示出了优异的成本-准确度折中效果。
## 7. `cs.AI` - 自适应数据飞轮：应用MAPE控制回路改进AI代理 [PDF](https://arxiv.org/pdf/2510.27051), [HTML](https://arxiv.org/abs/2510.27051)
### Authors
Aaditya Shukla,Sidney Knowles,Meenakshi Madugula,Dave Farris,Ryan Angilly,Santiago Pombo,Anbang Xu,Lu An,Abhinav Balasubramanian,Tan Yu,Jiaxiang Ren,Rama Akkiraju
### Background
企业AI代理必须不断适应以保持准确性、减少延迟并符合用户需求。该论文分析了NVIDIA的NVInfo AI中Mixture-of-Experts (MoE)知识助手的实施，该助手服务于超过30,000名员工。通过将MAPE驱动的数据飞轮概念化，构建了一个闭环系统，系统地处理检索增强生成（RAG）管道中的失败，并实现持续学习。论文监测了部署后三个月的反馈并收集了495个负面样本，揭示了两大主要失败模式：路由错误和查询重述错误。研究者使用NVIDIA NeMo微服务实现了有针对性的改进以微调模型，从而提高了准确性和减少了延迟时间。
### Innovation
研究引入了一种基于MAPE控制回路的数据飞轮概念，通过人类在环（HITL）反馈来提高企业AI代理的自适应性和学习能力。它通过实施细调方法，成功将一个70B参数的Llama模型替换为8B参数的变体，并提高了准确率和减少了延迟时间。这种方法提供了一个实用的蓝图，以迅速构建具有强大适应性的企业级AI代理，这些代理可以大规模从实际使用中学习并改进。
### Conclusion
该研究发现，即使在有限的用户反馈下，通过数据飞轮的设计和HITL方法仍能确保代理的健壯性和持续改进。研究人员还讨论了在隐私约束下执行分阶段生产的策略。该工作为构建能够大规模学习和适应的稳健、自适应企业AI代理提供了可重复的方法。
## 8. `cs.AI` - The Denario项目：为科学发现设计的深度知识AI代理 [PDF](https://arxiv.org/pdf/2510.26887), [HTML](https://arxiv.org/abs/2510.26887)
### Authors
Francisco Villaescusa-Navarro,Boris Bolliet,Pablo Villanueva-Domingo,Adrian E. Bayer,Aidan Acquah,Chetana Amancharla,Almog Barzilay-Siegal,Pablo Bermejo,Camille Bilodeau,Pablo Cárdenas Ramírez,Miles Cranmer,Urbano L. França,ChangHoon Hahn,Yan-Fei Jiang,Raul Jimenez,Jun-Young Lee,Antonio Lerario,Osman Mamun,Thomas Meier,Anupam A. Ojha,Pavlos Protopapas,Shimanto Roy,David N. Spergel,Pedro Tarancón-Álvarez,Ujjwal Tiwari,Matteo Viel,Digvijay Wadekar,Chi Wang,Bonny Y. Wang,Licong Xu,Yossi Yovel,Shuwen Yue,Wen-Han Zhou,Qiyao Zhu,Jiajun Zou,Íñigo Zubeldia
### Background
这篇文章介绍了一个名为Denario的AI多代理系统，用于作为科研助手。Denario可以执行多种任务，包括产生想法、查阅文献、制定研究计划、编写和执行代码、制作图表以及撰写和审查科学论文。系统具有模块化架构，允许它处理特定任务，如生成想法或端到端的科学分析。该研究详细描述了Denario及其模块，并通过展示在多个科学领域（如天体物理学、生物、生物物理学、生物医学信息学、化学、材料科学、数学物理、医学、神经科学和天文学）中生成的多篇AI论文，展示了其能力。此外，还通过展示一篇结合量子物理和机器学习方法的天文学数据论文，展示了在不同学科之间结合想法的能力。
### Innovation
Denario是一个多代理的AI系统，专为科学探索设计。它能够执行多种科学任务，具有模块化架构，能够有效处理特定任务。系统还能够跨学科结合点子，展示出强大的综合能力和创新性。通过专家评价，进一步验证了其有效性和潜力。作者还探讨了AI驱动研究的伦理问题，即这种技术将如何影响科学研究的哲学思想。此外，研究人员公开发布了代码，以支持这一创新研究的发展。
### Conclusion
Denario系统已经展示出强大的能力，不仅能够高效完成各类科学任务，还能跨学科整合知识。通过对AI生成的科学论文进行专家评审，发现其在某些方面还存在不足。同时，该系统在伦理和哲学层面提出了重要的思考和讨论点。最终，研究人员希望这一技术将进一步促进科学界的进步，同时也引发了对该技术使用时伦理和哲学考量的重视。
## 9. `cs.AI` - CATArena：通过迭代锦标赛竞争评估LLM代理 [PDF](https://arxiv.org/pdf/2510.26852), [HTML](https://arxiv.org/abs/2510.26852)
### Authors
Lingyue Fu,Xin Ding,Yaoming Zhu,Shao Zhang,Lin Qiu,Weiwen Liu,Weinan Zhang,Xuezhi Cao,Xunliang Cai,Jiaxin Ding,Yong Yu
### Background
现有的基准测试主要评估固定场景中的端到端性能，这限制了对特定技能的评估，并且随着代理能力的提高，评分趋于饱和，对专家注解的依赖也在增加。大型语言模型（LLM）代理已经从基本的文本生成进化到通过与外部工具的交互自主完成复杂的任务。然而，当前的基准测试只能评估某些特定的技能，限制了对代理自改进和同伴学习能力的评估。为此，该研究强调了学习能力的重要性，认为这是代理进化到接近人类智能的核心驱动力。为此，文章提出了一种迭代且具有竞争性的同伴学习框架，该框架允许代理通过反复交互和反馈来逐步提高和优化其策略，从而系统地评估其学习能力。为了应对当前基准测试中的评分饱和问题，作者引入了CATArena平台，这是一个包含四个不同板牌游戏的锦标赛式评价平台，具有开放的评分机制，以便能满足灵活且动态的评分需求。通过提供没有明确得分上限的任务，CATArena能够持续且动态地评估代理能力的最新进展。实验结果表明，CATArena为智能代理的核心能力提供了一个可靠、稳定和可扩展的基准，特别是学习能力和策略编码的能力。
### Innovation
本文提出了一种迭代且具有竞争性的同伴学习框架，通过让代理通过反复交互和反馈来逐步提高和优化其策略，从而系统地评估其学习能力。此外，为了应对当前基准测试中的评分饱和问题，作者还提出了CATArena平台，这是一个包含四个不同板牌游戏的锦标赛式评价平台，能够持续且动态地评估代理能力的最新进展。
### Conclusion
实验结果表明，CATArena为智能代理的核心能力提供了一个可靠、稳定和可扩展的基准，特别是学习能力和策略编码的能力。
## 10. `cs.AI` - 基于可验证推理的逆向知识搜索：从长推理链知识库合成科学百科 [PDF](https://arxiv.org/pdf/2510.26854), [HTML](https://arxiv.org/abs/2510.26854)
### Authors
Yu Li,Yuan Huang,Tao Wang,Caiyu Fan,Xiansheng Cai,Sihan Hu,Xinzijian Liu,Cheng Shi,Mingjun Xu,Zhen Wang,Yan Wang,Xiangqi Jin,Tianhan Zhang,Linfeng Zhang,Lei Wang,Youjin Deng,Pan Zhang,Weijie Sun,Xingyu Li,Weinan E,Linfeng Zhang,Zhiyuan Yao,Kun Chen
### Background
大多数科学研究材料压缩了推理过程，直接呈现结论而省略了证明它们的推理链。这种压缩使验证变得困难，因为它缺乏明确的、逐步的证明，并且忽略了建立概念之间逻辑和因果联系的路径。现有的知识表示和系统未能充分捕捉和验证科学推理过程中的细微差别，从而限制了跨领域的知识链接与理解。本文提出了一种可扩展的框架，该框架解压缩科学推理，构建一个可验证的“长推理链”（LCoT）知识库，并将其投影到新兴的科学百科全书，SciencePedia中。该框架采用了自下而上、还原主义的方法，通过一个苏格拉底式的代理生成大量原理级问题，这些代理指导下的课程大约有200门。抽样的准确度通过多重独立求解模型生成的LCoT进行验证，并通过提示清洗和跨模型答案共识进行过滤，只保留那些具有验证端点的LCoT。最终通过的LCoT构成了推理引擎和合成器的基础，对目标概念进行推理检索，并合成具有连贯性的科学文章。这些合成的文章在六个学科的评估中表现出更高的知识点密度和更低的错误率，与没有检索的服务端基准相比更为出色。该方法提供了一种在科学领域进行可信、规模化的跨领域合成的方法，奠定了一个不断扩展的科学百科全书的基础。
### Innovation
本文引入了一个可扩展的框架，能够解压缩科学研究中的推理过程，创建一个可验证的LCoT知识库，以及构建基于该知识库的新兴科学百科全书，SciencePedia。框架采用自下而上的还原主义策略，生成大量的原理级问题，通过提示清洗和跨模型答案共识进行多轮验证，确保生成的知识链的可靠性。这种方法能有效地实现跨学科的知识合成，为科学信息的可验证存储和检索提供了全新途径。
### Conclusion
本文提出的方法能够实现跨领域的科学合成，其验证过的LCoT知识库为科学信息的可验证存储和检索提供了基础。通过建立“基于可验证推理的逆向知识搜索”，该方法增强了科学信息的透明度和可信度，并为建立一个不断扩展的科学百科全书奠定了基础。
## 11. `cs.AI` - GUI-Rise：GUI导航中的结构化推理和历史总结 [PDF](https://arxiv.org/pdf/2510.27210), [HTML](https://arxiv.org/abs/2510.27210)
### Authors
Tao Liu,Chongyu Wang,Rongjie Li,Yingchen Yu,Xuming He,Bai Song
### Background
虽然多模态大型语言模型（MLLMs）已经提升了GUI导航代理，但当前方法在跨域泛化和历史有效利用方面仍然存在局限性。
### Innovation
本文提出了一种增强推理框架，该框架系统地整合了结构化推理、动作预测和历史总结。该框架通过监督微调和使用组相对策略优化（GRPO）的强化学习训练了一个GUI代理，名为GUI-Rise。此外，该框架采用了专门奖励，包括带历史意识的目标，直接链接总结质量与后续动作性能。
### Conclusion
在标准基准上的全面评估表明，在相同训练数据条件下具有最佳结果，尤其是在跨域场景中的表现尤为出色。这些发现验证了该框架在各种GUI导航任务中保持稳健推理和泛化的能力。
## 12. `cs.AI` - 长时序未排序任务的强化学习：从布尔型到耦合奖励机器 [PDF](https://arxiv.org/pdf/2510.27329), [HTML](https://arxiv.org/abs/2510.27329)
### Authors
Kristina Levina,Nikolaos Pappas,Athanasios Karapantelakis,Aneta Vulgarakis Feljan,Jendrik Seipp
### Background
奖励机器（RMs）指导强化学习代理识别环境中的奖励结构。这对于复杂非马尔可夫任务尤其有利，因为拥有RM的代理可以从更少的样本中学得更有效率。然而，在长时序问题中，当一组子任务可以以任意顺序执行时，通过RMs学习变得不适合。在这种情况下，需要学习的信息量随着未排序子任务数量的增加呈指数级增长。
### Innovation
本文提出了三种奖励机器的一般化：（1）数值型RM允许用户以紧凑形式表示复杂任务；（2）议程RM将状态与跟踪剩余待完成子任务的议程相关联；（3）耦合RM将与议程中每个子任务相关的耦合状态相关联。此外，还提出了一种新的组合学习算法：带有耦合RM的Q学习（CoRM）。
### Conclusion
我们的实验表明，CoRM在处理含有未排序子任务的长时序问题时比最先进的RM算法具有更好的扩展性。
## 13. `cs.AI` - Fints: Efficient Inference-Time Personalization for LLMs with Fine-Grained Instance-Tailored Steering [PDF](https://arxiv.org/pdf/2510.27206), [HTML](https://arxiv.org/abs/2510.27206)
### Authors
Kounianhua Du,Jianxing Liu,Kangning Zhang,Wenxiang Jiao,Yuan Lu,Jiarui Jin,Weiwen Liu,Yong Yu,Weinan Zhang
### Background
大型语言模型（LLMs）的迅速发展加剧了对有效个性化技术的需求，这些技术可以适应个体用户偏好。尽管非参数方法利用了LLMs的部分内省学习能力，但最近的参数化适应方法，如个性化参数高效微调和奖励建模也在涌现。然而，这些方法在处理动态用户模式和高数据稀疏场景时面临着局限性，原因是适应性低和数据效率差。
### Innovation
提出了一种细粒度的、实例定制的导向框架，该框架能从用户数据动态生成样本级干扰向量，并注入模型的前向传播过程中，以实现个性化适应。该方法引入了两种关键技术创新：一个细腻的导向组件，通过挂钩注意和MLP层的激活来捕捉复杂信号，以及一个输入感知的聚合模块，将这些信号整合成与上下文相关的增强功能。该方法展示了高度的灵活性和数据效率，在快速变化的分布和高数据稀疏场景中表现出色。此外，所提出的方法与现有方法正交，可以与其他个性化技术无缝集成。
### Conclusion
在不同场景下的大量实验验证了我们的方法的有效性和兼容性。结果表明，在快速变化的环境中，与现有方法保持鲁棒性的同时，我们的方法显著提升了个性化性能。实现已在 provided official website 上可用。
## 14. `cs.AI` - LLM Contributions to Bin Packing Problem [PDF](https://arxiv.org/pdf/2510.27353), [HTML](https://arxiv.org/abs/2510.27353)
### Authors
Julien Herrmann,Guillaume Pallez
### Background
近期的研究表明，大规模语言模型（LLMs）可以为数学发现提供有价值的灵感。此前的研究报告称，基于LLMs的遗传算法生成了适用于均匀分布和威布ull分布下的在线分箱问题的新颖启发式方法。这项工作通过对这些启发式方法的详细分析，重新评估了这一主张，研究了这些启发式方法的性能和可解释性。尽管这些启发式方法对人类是可读的，但即使是领域专家也无法完全理解它们。
### Innovation
本文提出了一类针对这些问题的新算法，这些算法更简单、更高效、更易解释、更具有泛化能力。研究发现，所考虑的实例本身相对简单。在此基础上，讨论了关于LLMs对分箱问题贡献的主张中的局限性，即错误假设了这些实例之前已被研究。与此同时，强调了在评估LLMs生成的输出的科学价值时，严格的验证和情境化的重要性。
### Conclusion
本研究强调了在评估LLMs生成的输出的科学价值时，严格的验证和情境化的重要性。虽然LLMs可以提供有价值的启发式方法，但其贡献需在合理的科学背景下进行评估。
## 15. `cs.AI` - 基于结果导向的过程模型发现的可解释区分规则学习 [PDF](https://arxiv.org/pdf/2510.27343), [HTML](https://arxiv.org/abs/2510.27343)
### Authors
Ali Norouzifar,Wil van der Aalst
### Background
事件日志来源于信息系统的提取可以为理解并改进业务流程提供丰富的基础。许多实际应用中，可以通过区分有正面和负面流程执行来进一步理解这些流程，其中正面痕迹反映了高效或合规的行为，而负面痕迹可能涉及效率低下、规则违规、延迟或资源浪费。这些区分为结果意识更强的过程发现提供了机会。在不考虑结果的情况下，发现单一的过程模型可能会导致不适用于符合性检查及性能分析的表示结果，因为可能会遗漏关键的行为差异。此外，优先考虑一种行为可能会掩盖那些理解流程结果至关重要的结构差异。通过学习控制流特征的可解释区分规则，我们对具有相似可取性概况的痕迹进行分组，并在每个组内分别应用过程发现。这种方法可以揭示正面和负面执行的驱动因素，并得到专注于且可解释的过程模型。
### Innovation
该方法通过学习控制流特征的可解释区分规则来对具有相似可取性概况的痕迹进行分组，并在每个组内分别进行过程发现。这种方法能揭示正面和负面执行的驱动因素，并得到专注于且可解释的过程模型，而传统方法则可能得到不适用于符合性检查及性能分析的表示结果。
### Conclusion
该方法被实施为一个公开可用的工具，已在多个实际生活中的事件日志上进行了评估，证明了其在隔离和可视化关键流程模式方面的有效性。
## 16. `cs.AI` - ToolScope: 一种视觉导向和长期工具使用的智能框架 [PDF](https://arxiv.org/pdf/2510.27363), [HTML](https://arxiv.org/abs/2510.27363)
### Authors
Mengjie Deng,Guanting Dong,Zhicheng Dou
### Background
近年来，大型语言模型（LLMs）通过自主整合外部工具进行协作推理，展示了引人注目的问题解决能力。然而，由于多模态信息本身的复杂性和多样性，使多模态大型语言模型（MLLMs）在长周期视觉问答（VQA）任务中灵活高效地利用外部工具进行推理仍是一个未被充分探索的挑战。
### Innovation
本研究提出了ToolScope，这是一种旨在统一全局规划与局部多模态感知的主动框架，通过专用的Perceive工具减轻长期VQA任务中视觉上下文的降级。ToolScope由三个主要组件组成：全局导航器、主动执行器和响应合成器。全局导航器提供高层战略指导，主动执行器通过整合外部工具（搜索、代码和感知）进行迭代操作以增强MLLM的局部感知，最后，响应合成器将推理过程整合成一个连贯且用户友好的输出。
### Conclusion
我们在包括VQA 2.0、ScienceQA、MAT-Search和MathVista在内的四个不同的VQA基准上评估了ToolScope。结果显示，它具有很强的泛化能力，在所有数据集上的平均性能提升了高达6.69%。
## 17. `cs.AI` - 从产品到系统网络：系统集管理中系统网络生命周期管理的挑战 [PDF](https://arxiv.org/pdf/2510.27194), [HTML](https://arxiv.org/abs/2510.27194)
### Authors
Vahid Salehi,Josef Vilsmeier,Shirui Wang
### Background
今天的产品不再是孤立的实体，而是网络系统中的节点。这意味着传统的线性生命周期模型受到限制：跨学科的互操作性、变体和配置管理、跨组织边界的可追溯性和治理变得至关重要。本文基于当前文献和行业经验，识别了移动性、健康护理和公共部门等领域的四个原则，旨在解决系统网络生命周期管理中的挑战，明确提出参考架构和数据模型、端到端的配置主权而非工具孤岛、受控模型及其清晰审查门以及时间、质量、成本和可持续性的可测量价值贡献。
### Innovation
分类了系统网络生命周期管理的现状，提出了实用框架，包括基于模型的系统工程（MBSE）作为语义支撑、产品生命周期管理（PLM）作为治理和配置层级、CAD-CAE作为模型衍生领域、数字线程和数字孪生作为持续反馈。识别了四个原则：1. 参考架构和数据模型；2. 端到端的配置主权而非工具孤岛；3. 受控模型及明确审查门；4. 沿时间、质量、成本和可持续性的可测量价值贡献。最后给出了三个步骤的路线图，展示产品到网络中心发展的过渡：基于参考架构的试点阶段、在变体和供应链空间中的规模化、组织扎根（角色、培训、合规）
### Conclusion
这种从产品到网络的中心化发展增强了变化的稳健性，缩短了流程时间，提高了重用性和基于可持续性的决策质量。这篇文章面向希望简化复杂性且能够设计缩放系统网络价值流的决策者和从业者。
## 18. `cs.AI` - 对话作为发现：通过原则性的询问导航人类意图 [PDF](https://arxiv.org/pdf/2510.27410), [HTML](https://arxiv.org/abs/2510.27410)
### Authors
Jianwen Sun,Yukang Feng,Yifan Chang,Chuanhao Li,Zizhen Li,Jiaxin Ai,Fanrui Zhang,Yu Dai,Kaipeng Zhang
### Background
人类与人工智能合作中的一个基本瓶颈是“意图表达差距”，即人类难以有效地向AI传达复杂、高维的思想。这种挑战常常导致用户在低效的试错循环中被困，而用户的不同专业知识水平使其更加复杂。
### Innovation
本文重新构想了这一问题，从被动的指令遵循转向苏格拉底式的合作范式，提出了一种主动探询信息的代理，以解决其关于用户意图的不确定性。作者提出了一种名为Nous的代理，训练它以掌握这种询问策略。Nous的核心机制是基于信息论基本原则的训练框架，在此框架内，对话的信息增益被定义为内在的奖励信号，这本质上等同于Shannon熵在结构任务空间中的减少。这种奖励设计使得无需依赖昂贵的人类偏好注释或外部奖励模型。为了验证框架的有效性，作者开发了一个自动化模拟管道来生成大规模的偏好数据集，用于生成科学图表等艰巨任务。
### Conclusion
全面的实验，包括消融实验、主观和客观评估以及不同用户专业知识水平的测试，证明了所提框架的有效性。Nous不仅在效率和输出质量上取得了领先地位，而且在不同用户专业知识水平下仍然保持了稳健性。此外，其设计具有领域通用性，实验结果表明它在超越图表生成的其他应用场景中也有泛化能力。研究工作提供了一个原则性的、可扩展的和自适应的解决复杂人类-人工智能协作中用户意图不确定性问题的范式。
## 19. `cs.AI` - GeoFM：通过形式语言生成合成数据以增强多模态大语言模型的几何推理能力 [PDF](https://arxiv.org/pdf/2510.27448), [HTML](https://arxiv.org/abs/2510.27448)
### Authors
Yuhao Zhang,Dingxin Hu,Tinghao Yu,Hao Liu,Yiting Liu
### Background
多模态大语言模型（MLLMs）在处理多模态任务方面展现出显著的能力，但在数学几何推理方面面临挑战，主要是由于高质量几何数据的稀缺性。目前生成合成几何数据的方法通常涉及重新表述或扩展现有问题，并使用预定义的规则和模板来创建几何图像和问题，但这些方法往往会生成缺乏多样性和容易产生噪声的数据。现有的方法生成的几何图像往往表现出有限的变化，并且与真正的几何图表相差甚远。
### Innovation
本文提出了一个新的方法GeoFM，通过使用形式语言探索度量空间内条件的组合来生成高保真几何问题，同时确保正确性通过符号引擎。实验结果显示，与现有方法相比，我们的合成数据表现显著更好，使用我们数据训练的模型在MathVista几何问题解决任务上优于专有GPT-4o模型18.7%，在GeoQA上优于16.5%。此外，在MathVista和GeoQA上，该模型的性能分别超过了领先开源模型5.7%和2.7%。
### Conclusion
我们的方法GeoFM显著提升了多模态大语言模型在数学几何推理任务上的性能，通过使用形式语言生成的几何数据可以克服现有数据生成方法中的局限性。
## 20. `cs.AI` - 使用人类感知-动作约束的多智能体RL实现现实的行人-驾驶员交互建模 [PDF](https://arxiv.org/pdf/2510.27383), [HTML](https://arxiv.org/abs/2510.27383)
### Authors
Yueyang Wang,Mehmet Dogar,Gustav Markkula
### Background
分析和建模行人和驾驶员之间的交互对于理解人类交通用户行为和开发安全的自动驾驶车辆系统至关重要。现有方法通常依赖于基于规则的逻辑、博弈论模型或‘黑箱’机器学习方法。然而，这些方法通常缺乏灵活性或忽视了如感觉和运动限制等基础机制，这些机制影响着行人和驾驶员在交互场景中的感知和行为表现。
### Innovation
提出了一种多智能体强化学习（RL）框架，该框架将行人和驾驶员智能体的视觉和运动约束结合起来。使用无信号人行横道的实际数据集来评估四种模型变体，结果显示结合了视觉和运动约束的模型性能最佳。在数据有限的情况下，该模型优于监督行为克隆模型，表明即使在训练数据量较少的情况下，我们的方法也有效。此外，该框架通过将控制人类约束的模型参数建模为人群层面的分布，来考虑个体差异，这是先前行人-车辆交互建模工作中未探索的一种视角。
### Conclusion
本文的研究表明，结合人类感知-动作约束的多智能体RL是一种有潜力的模拟现实道路交互行为的建模方法。通过同时考虑视觉和运动约束，模型能够更好地模拟行人和驾驶员之间的交互行为，尤其是在资源有限的数据环境中，也能表现出色。
## 21. `cs.AI` - SIGMA：代理数学推理中的搜索增强按需知识整合 [PDF](https://arxiv.org/pdf/2510.27568), [HTML](https://arxiv.org/abs/2510.27568)
### Authors
Ali Asgarov,Umid Suleymanov,Aadyant Khatri
### Background
解决数学推理问题不仅需要准确地访问相关知识，还需要进行仔细的多步骤思考。目前的检索增强模型往往依赖单一视角，遵循固定的搜索策略，并且难以有效地结合多个来源的信息。
### Innovation
SIGMA 是一种统一框架，通过管理专门的代理，使其独立推理、执行有针对性的搜索并在协调机制下综合发现结果。每个代理生成假设性段落以优化其分析视角下的检索，确保知识整合既具有上下文敏感性又能提高计算效率。在MATH500、AIME和博士级科学QA GPQA等挑战性基准测试中，SIGMA 以7.4%的绝对性能改进持续超越开源和闭源系统。
### Conclusion
我们的结果表明，多代理、按需知识整合显著提高了推理准确性和效率，为复杂的知识密集型问题解决提供了可扩展的方法。我们将发布源代码（待发表）。
## 22. `cs.AI` - InnovatorBench：评估执行创新大语言模型研究能力的代理 [PDF](https://arxiv.org/pdf/2510.27598), [HTML](https://arxiv.org/abs/2510.27598)
### Authors
Yunze Wu,Dayuan Fu,Weiye Si,Zhen Huang,Mohan Jiang,Keyu Li,Shijie Xia,Jie Sun,Tianze Xu,Xiangkun Hu,Pengrui Lu,Xiaojie Cai,Lyumanshan Ye,Wenhong Zhu,Yang Xiao,Pengfei Liu
### Background
现有的基于人工智能的代理可以在科学发现中通过自动化假设形成、实验设计、编程、执行和分析加速过程，然而现有的基准测试仅针对简化的设置中狭窄的能力进行评估。鉴于这一限制，本文介绍了InnovatorBench，这是一个用于评估代理端到端进行大语言模型研究的基准平台。该平台涵盖了20项任务，包括数据构建、筛选、增强、损失设计、奖励设计和支架构建，旨在评估生成的可执行程序及其正确性、性能、输出质量和不确定性。
### Innovation
本文提出了InnovatorBench和ResearchGym平台，前者是一个全方位评估代理进行大语言模型研究能力的基准平台，后者是以出色的研究环境，提供了丰富的动作空间、分布式和长时间执行、异步监控和快照保存等功能。同时，本文还实现了一个轻量级的ReAct代理，结合明确定理与可执行计划。
### Conclusion
实验表明，前沿模型在代码驱动的研究任务中显示出潜力，但在脆弱算法相关任务和长时决定中仍存在不足，例如易疲劳、资源管理不当和过于依赖模板推理。同时，代理在InnovatorBench上实现最优性能需要超过11小时，这进一步证明了InnovatorBench的难度，并展示了作为下一代基于代码研究基准的潜力。
## 23. `cs.AI` - Valid性是你需要的 [PDF](https://arxiv.org/pdf/2510.27628), [HTML](https://arxiv.org/abs/2510.27628)
### Authors
Sebastian Benthall,Andrew Clark
### Background
随着AI代理在计算机科学领域长期被讨论和研究，今天的Agentic AI系统是一种全新的事物。论文回顾了Agentic AI的已有多义定义，并提出了一个新的现实主义定义：Agentic AI是一种软件交付机制，类似于软件即服务（SaaS），它能使应用程序在复杂的商业环境中有自主性地工作。最近大规模语言模型（LLMs）作为基础模型的进步也推动了Agentic AI领域的兴趣。然而，论文指出，Agentic AI系统主要涉及应用程序而不是基础模型，因此其成功依赖于终端用户的验证和主要利益相关者的确认。这需要与评估基础模型不同的工具和技术。
### Innovation
论文提出了一个新的、现实主义的Agentic AI定义，并分析了近年来大规模语言模型的进步如何驱动了对Agentic AI的兴趣。然而，它强调Agentic AI系统主要是应用程序，成功依赖于终端用户的验证，而且提出了在有效的验证措施下，可以使用更简单的、更快的、更具解释性的模型来实现核心逻辑。
### Conclusion
对于Agentic AI而言，最重要的是有效性。大规模语言模型（LLMs）是可能实现这一目标的一个选项。
## 24. `cs.AI` - DeepCompress: 一种动态探索和压缩推理链的双重奖励策略 [PDF](https://arxiv.org/pdf/2510.27419), [HTML](https://arxiv.org/abs/2510.27419)
### Authors
Tian Liang,Wenxiang Jiao,Zhiwei He,Jiahao Xu,Haitao Mi,Dong Yu
### Background
大型推理模型（LRMs）虽然表现出色，但在解决简单和复杂问题时会表现出认知上的低效率，即对简单问题的“过度思考”和对复杂问题的“思考不足”。现有通过监督微调（SFT）或使用基于标记长度的奖励进行强化学习（RL）的方法可以在一定程度上提升效率，但往往以牺牲准确性为代价。研究者认为目前一致青睐较短推理路径的方法并不总是最佳选择，更长的回答可以涵盖更多正确解决方案，尤其是对于困难的问题。因此，他们提出了一个基于可变长度奖励机制的DeepCompress框架来同时提高模型的准确性和效率。
### Innovation
DeepCompress框架通过一个可动态调整问题难度的机制，根据模型的能力实时分类问题为“简单”或“困难”。对于“简单”问题，它鼓励更短、更高效的思考过程；而对于“困难”问题，则倾向于更长、更探索性的推理链。这种方法允许模型根据需要自主调整其推理链（CoT）的长度，从而在熟练掌握的问题上压缩推理，在遇到挑战的问题上延长推理。实验结果表明，DeepCompress在具有挑战性的数学基准测试上超越了基线方法，不仅提高了准确性，还显著提升了标记效率。
### Conclusion
DeepCompress框架通过双重奖励策略，能够在保持高准确性的同时，有效提高模型的推理效率，特别是在处理复杂问题时更为显著。
## 25. `cs.AI` - Learned Reasoning 机械学习推理1：TempoBench，一种可解释的推理系统性能拆解基准 [PDF](https://arxiv.org/pdf/2510.27544), [HTML](https://arxiv.org/abs/2510.27544)
### Authors
Nikolaus Holzer,William Fishell,Baishakhi Ray,Mark Santolucito
### Background
大语言模型（LLMs）在许多任务上的表现已超过人类。然而，在提高LLMs推理能力方面，研究者们要么依赖手工构建的数据集，要么依赖正式的数学证明系统，如Lean证明助手。手工构建的数据集虽然可以捕捉到现实世界推理过程中的决策链，但也可能无意中在覆盖的推理空间中编码一些偏差；而且也不能被形式验证。相较之下，系统如Lean可以确保可验证性，但并不适合捕捉基于代理人决策链的任务的本质。这种差距造成了在诸如商务代理或代码助手等功能中性能表现的不足，以及LLMs推理基准的实用性不足，这些基准在推理结构和现实世界对齐上存在局限性。
### Innovation
本文介绍了TempoBench，这是首个基于形式理论并可验证的诊断基准，能够在系统中参数化难度，以系统分析LLMs的推理表现。TempoBench使用两种评估基准来分解推理能力，包括时间跟踪评估（TTE），测试LLMs在理解并模拟给定多步骤推理系统执行方面的能力；以及时间因果评估（TCE），测试LLMs在执行多步骤因果推理及从复杂系统中提炼因果关系的能力。研究表明，模型在TCE-normal上的得分是65.6%，而在TCE-hard上的得分仅为7.5%，表明最先进的LLMs已明确理解了TCE任务，但在系统复杂性增加时表现不佳。同时，我们的代码已发布在GitHub仓库中。
### Conclusion
通过引入TempoBench，我们的工作填补了LLM推理评估中的空白，提供了更加精细和准确的测试工具，为理解LLM在多步骤因果推理任务中的能力提供了新的洞见。
## 26. `cs.AI` - 交互作为智能 II：长时任务训练中的异步人机演示 [PDF](https://arxiv.org/pdf/2510.27630), [HTML](https://arxiv.org/abs/2510.27630)
### Authors
Dayuan Fu,Yunze Wu,Xiaojie Cai,Lyumanshan Ye,Shijie Xia,Zhen Huang,Weiye Si,Tianze Xu,Jie Sun,Keyu Li,Mohan Jiang,Junfei Wang,Qishuo Hua,Pengrui Lu,Yang Xiao,Pengfei Liu
### Background
大型语言模型（LLM）代理在自动编码、深入研究和图形用户界面操作等领域表现出强大的潜在能力。然而，它们在长期领域特定任务中的表现仍然面临挑战。当前的方法主要分为两类：一类依赖于行为克隆的密集人工标注，这在长期任务中非常昂贵，因为这些任务可能需要几天或几个月的时间；另一类依赖于结果驱动的采样，由于在特定领域任务中有效正向轨迹的稀有性，这种方法常常会因为结果的不理想而失效。
### Innovation
该研究引入了Apollo，这是一种结合异步人类指导和动作级数据过滤的采样框架。Apollo允许标注者在代理偏离有希望的轨迹时进行干预，而非全程跟随代理操作。这种轻量级的设计使得保持超过30小时的互动成为可能，并以较低的成本产生有价值的轨迹。Apollo还应用监督控制来过滤出次优动作，防止错误传播。这些成分共同使得在长时环境中可靠有效地收集数据成为了可能。
### Conclusion
通过在InnovatorBench上应用Apollo，研究证明Apollo在对GLM-4.5模型进行训练时，相较于未训练基线和未与人交互训练的变体，它分别取得了超过50%和28%的改进。这些结果强调了人机环绕采样的关键作用，以及Apollo设计在处理长期领域特定任务方面的鲁棒性。
## 27. `cs.AI` - MolChord：基于结构-序列对齐的蛋白质导向药物设计 [PDF](https://arxiv.org/pdf/2510.27671), [HTML](https://arxiv.org/abs/2510.27671)
### Authors
Wei Zhang,Zekun Guo,Yingce Xia,Peiran Jin,Shufang Xie,Tao Qin,Xiang-Yang Li
### Background
结构基于药物设计（SBDD）是药物发现中的一个基本任务，它将靶点蛋白质与候选分子配体进行匹配。有效将蛋白质结构表示与分子表示对接，并确保生成的药物与其药理性质之间的一致性，仍然是一个关键挑战。
### Innovation
本文提出了一种名为MolChord的方法，该方法结合了两种关键技术：(1) 使用NatureLM自回归模型统一文本、小分子和蛋白质，并利用扩散基础结构编码器将蛋白质和分子的结构与他们的文本描述和序列表示对接；(2) 通过整合偏好数据生成一种属性感知的数据集，并采用直接属性优化（DPO）进一步优化对接过程，以引导分子向目标特性发展。
### Conclusion
实验结果表明，我们的方法在CrossDocked2020数据集的关键评估指标上达到了最佳性能，突显了其在SBDD领域的实际应用潜力。
## 28. `cs.AI` - 基于Transformer架构的神经架构搜索方法 [PDF](https://arxiv.org/pdf/2505.01314), [HTML](https://arxiv.org/abs/2505.01314)
### Authors
Shang Wang,Huanrong Tang,Jianquan Ouyang
### Background
本文介绍了一种基于Transformer架构的神经架构搜索方法，该方法针对不同的编码器和解码器组合，搜索跨多头注意力的计算方式。为了寻找具有良好翻译结果的神经网络结构，研究者在算法中加入了困惑度作为辅助评估指标，同时使用多目标遗传算法逐步优化群体中的每个神经网络个体。实验结果表明，所搜索到的神经网络结构优于基线模型，并且引入辅助评估指标可以找到比仅使用BLEU分数作为评价指标更优秀的模型。
### Innovation
研究提出了一种基于Transformer的神经架构搜索方法，通过困惑度和BLEU分数作为评估指标，并采用多目标遗传算法优化神经网络结构。这种方法能够在多个目标中寻找最优解，从而提高翻译的准确性。
### Conclusion
实验结果显示，所提出的算法搜索的神经网络结构优于基线模型，引入困惑度作为评估指标可以帮助找到比仅依赖BLEU分数更优秀的模型。
## 29. `cs.AI` - 通过对比触发学习在基于MLLM的实体决策中实现视觉后门攻击 [PDF](https://arxiv.org/pdf/2510.27623), [HTML](https://arxiv.org/abs/2510.27623)
### Authors
Qiusi Zhan,Hyeonjeong Ha,Rui Yang,Sirui Xu,Hanyang Chen,Liang-Yan Gui,Yu-Xiong Wang,Huan Zhang,Heng Ji,Daniel Kang
### Background
多模态大语言模型（MLLMs）通过从视觉输入中实现直接感知、推理和规划任务导向性的行动，增强了实体代理的能力。然而，这些视觉驱动的实体代理也打开了新的攻击面——视觉后门攻击。在这种攻击中，实体代理在识别到视觉触发信号时才会执行攻击者指定的多步骤策略，而在触发信号未出现时则表现正常。此前没有针对这种攻击开发出有效的防御框架，特别是使用对象作为触发器的攻击：由于对象触发器在不同视角和照明下都有广泛的变异，使得植入可靠触发器变得困难。BEAT框架通过构建涵盖多样场景、任务和触发位置的训练集，同时引入两阶段训练方案实现该类攻击，从而首次提出了这种攻击框架，为MLLM基础的实体代理植入视觉后门攻击。
### Innovation
BEAT框架通过两种方式解决了视觉后门攻击实施中的挑战：（1）创建一个涵盖多样场景、任务和触发位置的训练集，以使代理适应触发器的变化；（2）提出了一种两阶段训练方案，先进行监督微调，然后应用新颖的对比触发学习（CTL）。CTL将触发器的识别问题表述为具有触发器存在和不存在的输入之间的偏好学习，明确锐化决策边界，以确保精确的后门激活。与简单的监督微调相比，CTL在有限的后门数据下使后门激活准确性提高了39%。该框架在多种实体代理基准和MLLM中实现了高达80%的攻击成功率，同时保持了良好的良性任务性能，并可靠地推广到未见过的触发器位置。这项研究揭示了基于MLLM的实体代理中存在的一个关键但未被探索的安全风险，强调了实际部署前需要开发强大的防御措施。
### Conclusion
BEAT通过对比触发学习（CTL）成功实现了对基于MLLM的实体代理的视觉后门攻击，显著提高了攻击成功率，并保持了良好的任务表现。这一研究发现了MLLM基础实体代理中的一个重要但未被深入研究的安全风险，强调了在实际部署前需要开发和部署可靠的防御措施。
## 30. `cs.AI` - VeriMoA: 混合代理框架用于规格到硬件描述语言生成 [PDF](https://arxiv.org/pdf/2510.27617), [HTML](https://arxiv.org/abs/2510.27617)
### Authors
Heng Ping,Arijit Bhattacharjee,Peiyu Zhang,Shixuan Li,Wei Yang,Anzhe Cheng,Xiaole Zhang,Jesse Thomason,Ali Jannesari,Nesreen Ahmed,Paul Bogdan
### Background
自动化寄存器传输级（RTL）设计可以满足日益增长的计算需求。大型语言模型（LLMs）在硬件描述语言（HDL）生成方面具有潜力，但由于参数知识有限和领域特定约束，它们面临着挑战。虽然提示工程和微调在知识覆盖和训练成本方面有限制，但多代理架构提供了一种无需培训的范式，通过协作生成增强推理。然而，目前的多代理方法在噪声传播的易感性和推理空间探索的局限性方面存在两个关键问题。因此，需要一种无需训练的混合代理（MoA）框架来解决这些问题，该框架能够通过跨整个生成过程的质量排名和选择机制来促进知识积累，并通过一种多路径生成策略来分解规格到HDL的翻译，利用LLM在高资源语言中的流畅性和促进解决方案多样性。相关的基准研究表明，VeriMoA在各种LLM架构下的pass@1指标中实现了15-30%的改进，特别是能够让较小的模型匹配较大模型和微调模型，而不需要成本高昂的训练过程。
### Innovation
VeriMoA提出了两种创新，首先，一种质量引导的缓存机制，用于保存所有中间的HDL输出，并在整个生成过程中进行质量排名和选择，以鼓励多层次推理过程中的知识积累。其次，一种多路径生成策略，利用C++和Python作为中间表示，分解规格到HDL的翻译为两阶段过程，利用LLM在高资源语言中的流畅性，同时促进多样化的解决方案。这种策略利用了LLM在高资源编程语言中的优势，提高了生成过程的效率和多样性。
### Conclusion
实验结果表明，VeriMoA框架在VerilogEval 2.0和RTLLM 2.0基准上实现了15-30%的pass@1指标改进，特别是在较小的模型能够与较大模型和微调模型相匹配方面表现出色，而无需进行昂贵的训练过程。
## 31. `cs.AI` - 基于ResNet架构的辅助评估指标神经架构搜索方法 [PDF](https://arxiv.org/pdf/2505.01313), [HTML](https://arxiv.org/abs/2505.01313)
### Authors
Shang Wang,Huanrong Tang,Jianquan Ouyang
### Background
该论文提出了一种以ResNet为基础框架的神经架构搜索空间，并涵盖了卷积参数、池化、全连接层以及残差网络的连接性的搜索目标。除了准确率之外，该论文还将验证集的损失值作为优化的次要目标。在此之前，已有研究使用ResNet架构进行神经架构搜索，但该研究引入了新的优化目标，并在多个数据集上验证了其效果。
### Innovation
该研究首次将验证集的损失值作为优化的次要目标，扩展了传统的仅用准确率作为优化目标的策略。此外，它提供了一种基于ResNet架构的新神经架构搜索方法，适用于处理卷积、池化、全连接层和残差网络连接性的搜索。
### Conclusion
实验结果表明，该研究提出的方法在MNIST、Fashion-MNIST和CIFAR100数据集上能够找到与现有网络架构具有竞争力的新架构。
## 32. `cs.AI` - VeriStruct：在Verus中使用AI辅助自动化验证数据结构模块 [PDF](https://arxiv.org/pdf/2510.25015), [HTML](https://arxiv.org/abs/2510.25015)
### Authors
Chuyue Sun,Yican Sun,Daneshvar Amrollahi,Ethan Zhang,Shuvendu Lahiri,Shan Lu,David Dill,Clark Barrett
### Background
尽管现有的自动验证工具已经开始提供对程序代码中单个函数的自动验证能力，但仍然缺乏能够处理更复杂的数据结构模块的工具。特别是在确保复杂数据结构的正确性方面，仍需新的方法和工具。
### Innovation
VeriStruct 引入了一种新型框架，旨在扩展AI辅助自动化验证的范围，从单个函数扩展到更复杂的数据结构模块。VeriStruct 特别强调使用规划模块来系统生成抽象、类型不变式、规范和证明代码，并且还内置了语法指导和修复阶段来自动化纠正注释错误，以应对语言模型对Verus注解语法和验证特定语义的理解不足问题。
### Conclusion
VeriStruct 在对Verus的11个Rust数据结构模块进行评估时，成功地验证了129个函数中的128个（成功率99.2%），其中有十个模块全部通过验证。这些结果代表了自动AI辅助形式验证目标的重要进展。
## 33. `cs.AI` - EARS-UDE: 使用通用微分方程评估感觉超载中听觉反应 [PDF](https://arxiv.org/pdf/2510.26804), [HTML](https://arxiv.org/abs/2510.26804)
### Authors
Miheer Salunke,Prathamesh Dinesh Joshi,Raj Abhijit Dandekar,Rajat Dandekar,Sreedath Panat
### Background
感觉超载在自闭症谱系障碍（ASD）患者中影响50-70%的人群，现有方法如机制模型（Hodgkin Huxley类型、Wilson Cowan、兴奋性抑制平衡）、临床工具（EEG/MEG、感官指标量表）和机器学习方法（神经ODEs、预测编码）要么假设固定的参数，要么缺乏解释性，没有考虑到ASD的异质性。
### Innovation
提出了使用通用微分方程（UDEs）的科学机器学习方法来建模自闭症中的感官适应动力学。该框架结合了基于生物物理的微分方程与神经网络，能够捕捉机制理解与个体差异。该方法在参数量减少73.5%的情况下，实现了神经ODEs 90.8%的性能提升。该模型成功地恢复了生理参数，并以2%的误差范围进行了感官超载的定量风险评估，预测了具有特定时间模式的脉冲刺激的17.2%风险。
### Conclusion
该框架为自闭症的个性化、基于证据的干预措施奠定了基础，并直接应用于可穿戴技术和临床实践。
## 34. `cs.AI` - LLM基模型奖励模型中前缀偏差检测 [PDF](https://arxiv.org/pdf/2505.13487), [HTML](https://arxiv.org/abs/2505.13487)
### Authors
Ashwin Kumar,Yuzi He,Aram H. Markosyan,Bobbie Chern,Imanol Arrieta-Ibarra
### Background
Reinforcement Learning with Human Feedback (RLHF) 已经成为使用人类偏好数据对语言模型进行任务特定微调的关键框架。现有的公开偏好数据集提供响应间的成对比较，但模型中由此产生的奖励模型的潜在偏差尚未得到充分研究。这项研究旨在检测和评估由于查询前缀微小变化引起的模型偏见（前缀偏见）在基于LLM的奖励模型中的表现。研究涵盖广泛的开源偏好数据集和奖励模型架构，显示了这种偏见对不同模型架构的敏感性。研究结果强调了在开发公平可靠的奖励模型时需要为数据集设计和评估建立偏见意识，推动了AI公平性的更广泛讨论。
### Innovation
该研究引入了检测和评估前缀偏见的新方法，揭示了前缀偏见在种族和性别维度上的显著偏差，评估涉及多种开源偏好数据集和奖励模型架构。进一步提出了一种数据增强策略来缓解这些偏见，证明其在减少前缀偏见影响方面的有效性。
### Conclusion
研究发现强调了为奖励模型设计和评估提供偏见意识数据集的重要性，有助于开发公平可靠的奖励模型，促进了AI公平性的更广泛讨论。
## 35. `cs.AI` - LeMat-Synth: 一种从科学文献中构建广泛合成程序数据库的多模态工具箱 [PDF](https://arxiv.org/pdf/2510.26824), [HTML](https://arxiv.org/abs/2510.26824)
### Authors
Magdalena Lederbauer,Siddharth Betala,Xiyao Li,Ayush Jain,Amine Sehaba,Georgia Channing,Grégoire Germain,Anamaria Leonescu,Faris Flaifil,Alfonso Amayuelas,Alexandre Nozadze,Stefan P. Schmid,Mohd Zaki,Sudheesh Kumar Ethirajan,Elton Pan,Mathilde Franckel,Alexandre Duval,N. M. Anoop Krishnan,Samuel P. Gleason
### Background
材料合成程序的发展仍然是材料发现中的一个基本挑战，相关的合成程序知识散落在过去的科学文献中，以非结构化的形式存在，难以进行系统分析。
### Innovation
本文提出了一个结合大型语言模型（LLMs）和视觉语言模型（VLMs）的多模态工具箱，能够自动从材料科学出版物中提取和组织合成程序及性能数据，涵盖文本和图表。并通过专家注释和可扩展的大规模伪评审框架对提取质量进行了严格评估。此外，还提供了一个模块化、开源的软件库，支持社区驱动的新语料库和合成领域的扩展。
### Conclusion
这项工作提供了一个可扩展的基础设施，将无结构的文献转换为机器可读的信息，为合成程序的预测建模以及合成-结构-性能关系模型的构建奠定了基础。
## 36. `cs.AI` - 加速器束线控制的强化学习方法：基于模拟的方法 [PDF](https://arxiv.org/pdf/2510.26805), [HTML](https://arxiv.org/abs/2510.26805)
### Authors
Anwar Ibrahim,Alexey Petrenko,Maxim Kaledin,Ehab Suleiman,Fedor Ratnikov,Denis Derkach
### Background
粒子加速器在促进科学研究方面发挥着关键作用，但优化束线配置以最大化粒子传输通常是一项劳动密集型任务，需要专家干预。Elegant模拟框架被用来自动创建强化学习环境，从而实现磁场参数的逐级调整以减少粒子损失。研究引入了一个全面的状态表示，涵盖了束流统计、调整磁性参数的动作以及专注于传输效率的奖励函数。
### Innovation
RLBC（加速器束线控制的强化学习）是一个基于Python的库，将束线优化重新定义为强化学习问题。它通过利用Elegant模拟框架，自动化创建RL环境，并使用深度确定性策略梯度算法（DDPG）实现了高传输效率，接近专家的手动优化效果。这种方法将加速器物理与机器学习相结合，提供了一个适用于物理学家和RL研究人员的工具，以简化束线调整过程。
### Conclusion
RLBC在两个束线上实现了94%和91%的传输率，与专家的手动优化相当。这种方法为物理学家和机器学习研究人员提供了简化束线调整的新途径。
## 37. `cs.AI` - 使用领域知识声学特征在乌尔都语跨语料库情感识别中的跨语料库验证 [PDF](https://arxiv.org/pdf/2510.26823), [HTML](https://arxiv.org/abs/2510.26823)
### Authors
Unzela Talpur,Zafi Sherhan Syed,Muhammad Shehram Shah Syed,Abbas Shah Syed
### Background
情感识别（SER）是情感计算中的关键技术，能够使人工智能具有情感智能。然而，SER在低资源语言（如乌尔都语）上尤为具有挑战性。尽管有研究探究了广泛的SER问题，但乌尔都语这种低资源语言的情感识别仍是一个未被充分研究的领域。
### Innovation
该研究首次在不同乌尔都语情感语音数据集之间采用跨语料库验证框架，使用自语料库验证与其他跨语料库验证结果进行对比，发现后者更真实地反映了模型的稳健性。研究运用了结合领域知识的声学特征集（eGeMAPS和ComParE）来代表语音信号，并将其传递给逻辑回归和多层感知机分类器，通过未加权平均召回率评估分类性能。
### Conclusion
研究强调了跨语料库验证在乌尔都语情感识别中的重要性，指出其对于低资源语言社区的情感计算研究有着积极的推进作用。
## 38. `cs.AI` - 依据先验指导与区域精修构建高分辨率说话人肖像 [PDF](https://arxiv.org/pdf/2510.26819), [HTML](https://arxiv.org/abs/2510.26819)
### Authors
Jinting Wang,Jun Wang,Hei Victor Cheng,Li Liu
### Background
现有的方法主要依赖源图像作为外观参照，并利用源语音生成运动，但这些方法在将语音转化为说话人面部表情时面临着关键挑战。本文提出了一种新颖的方法，直接从语音中提取信息，以解决语音到说话人脸这一领域的关键问题。
### Innovation
本文的方法主要有以下创新点：首先，采用一种语音条件下的扩散模型结合统计面部先验和样本自适应加权模块，实现高质量语音肖像生成；随后，通过嵌入表情动态（如唇动、面部表情和眼球运动）到扩散模型的潜在空间，并使用区域增强模块优化唇同步，以生成高保真的语音驱动说话人脸；此外，为了生成高分辨率输出，集成了一种基于Transformer的离散代码本与图像渲染网络，从端到端增强视频帧细节。
### Conclusion
实验结果表明，本文方法在HDTF、VoxCeleb和AVSpeech数据集上的表现优于现有方法。值得注意的是，这是唯一一个能够仅从单一语音输入生成高分辨率、高质量说话人脸视频的方法。
## 39. `cs.AI` - 基于R3GAN的小规模医疗数据增强优化策略 [PDF](https://arxiv.org/pdf/2510.26828), [HTML](https://arxiv.org/abs/2510.26828)
### Authors
Tsung-Wei Pan,Chang-Hong Wu,Jung-Hua Wang,Ming-Jer Chen,Yu-Chiao Yi,Tsung-Hsien Lee
### Background
医疗图像分析常常受到数据稀缺和类别不平衡的限制，这影响了深度学习模型在临床应用中的效果。以人类胚胎时间拉伸成像(TLI)为案例研究，本工作探讨了如何通过生成对抗网络(GANs)优化小型数据集以生成现实且具有诊断意义的图像。
### Innovation
基于R3GAN的系统实验建立了有效的训练策略，包括全程预热阶段和低且逐渐增加的gamma范围(5 -> 40)，并设计了256x256分辨率数据集的优化配置。生成的样本被用于平衡不平衡的胚胎数据集，显著提高了分类性能，t3的召回率和F1分数分别从0.06和0.11提升至0.69和0.60，而其他类别的性能没有受损。
### Conclusion
定制化的R3GAN训练策略可以有效缓解数据稀缺，提高小规模医疗成像任务中的模型鲁棒性。
## 40. `cs.AI` - GACA-DiT: 基于扩散的舞蹈-音乐生成，具有通用适应节奏和上下文感知对齐 [PDF](https://arxiv.org/pdf/2510.26818), [HTML](https://arxiv.org/abs/2510.26818)
### Authors
Jinting Wang,Chenxing Li,Li Liu
### Background
舞蹈-音乐（D2M）生成旨在自动生成与舞蹈动作节奏和时间上对齐的音乐。现有方法通常依赖粗略的节奏嵌入，如全局运动特征或基于关节的二进制节奏值，这些方法会丢弃细粒度的运动提示，导致节奏对齐较弱。此外，特征下采样引入的时间不匹配还进一步阻碍了舞蹈与音乐的精确同步。
### Innovation
本文提出了一种基于扩散转换器的框架GACA-DiT，该框架包含两个创新模块，用于生成节奏一致、时间对齐的音乐。首先，一种通用适应节奏提取模块结合了多尺度时域小波分析和空间相位直方图，并采用自适应关节加权，以捕捉细粒度、特定于风格的节奏模式。其次，一种上下文感知时间对齐模块通过可学习的上下文查询解决时间不匹配问题，以将音乐潜在特征与相关的舞蹈节奏特征对齐。
### Conclusion
在AIST++和TikTok数据集上进行的大量实验表明，GACA-DiT在客观指标和人类评估方面均优于现有方法。
## 41. `cs.AI` - VIIRS主动火检测产品中夜间低置信度火检测缺失的系统性机制：未记录的算法过滤证据 [PDF](https://arxiv.org/pdf/2510.26816), [HTML](https://arxiv.org/abs/2510.26816)
### Authors
Rohit Rajendra Dhage
### Background
可见红外成像光谱仪（VIIRS）主动火产品被广泛用于全球火灾监测，但其置信度分类方案存在一个未记录的系统性模式。通过对2023年1月至2024年1月间覆盖21,540,921次火灾检测的数据分析，研究发现了夜间观测中完全缺乏低置信度分类的现象。夜间火灾共6,007,831次，但没有一次被分类为低置信度，而按照统计独立性本应有约696,908次。这种现象在世界各地、所有月份、不同纬度带和不同卫星上均存在。机器学习逆向工程、自助模拟（1,000次迭代）和时空分析均证实这是算法限制而非地理物理现象。夜间低于大约295K的亮度温度的火灾被完全排除而没有被标记为低置信度，而日间火灾的置信度分布则正常。这种未记录的行为影响了所有VIIRS火检测的27.9%，对火灾风险评估、日夜检测比较、置信度加权分析和任何依赖置信水平作为不确定性指标的研究有重要影响。
### Innovation
该研究发现了VIIRS主动火产品中夜间火检测完全缺失低置信度分类的未记录系统性模式，并通过多种方法证实这一现象是算法限制而非模拟现象。这项研究对于理解火灾监测中数据处理算法的限制具有重要创新意义，对卫星火灾监测数据的应用和解释具有重要影响。同时，研究提出了明确记录这一算法限制并重新处理受影响分析的建议。
### Conclusion
夜间火灾检测中完全没有低置信度分类这一未记录的系统性现象显著影响了27.9%的VIIRS火检测数据。这一现象是由算法限制而非地理物理现象导致的，特别是在低于295K亮度温度的夜间火灾全被排除。该发现对火灾风险评估、日夜检测比较、置信度加权分析及任何认为置信水平为不确定性指标的研究有重要影响。研究建议在VIIRS用户指南中明确记录这一算法限制，并重新处理受影响的分析。
## 42. `cs.AI` - CDSS on临床决策支持系统（CDSS）在低收入和中等收入国家临床结果和医疗服务中的影响：一项系统综述和meta分析的协议 [PDF](https://arxiv.org/pdf/2510.26812), [HTML](https://arxiv.org/abs/2510.26812)
### Authors
Garima Jain,Anand Bodade,Sanghamitra Pati
### Background
临床决策支持系统（CDSS）被用来提升临床和医疗服务结果。然而，关于低收入和中等收入国家（LMICs）的相关证据是分散的。本文档概述了量化CDSS在LMICs中对患者和医疗服务结果影响的方法。我们将纳入世界银行定义的LMICs中评估CDSS的对比定量设计，如随机对照试验、控制前后试验、中断时间序列和对比队列研究。独立 QUAL Qualitative 研究将被排除；混合方法研究仅当它们报告对比定量结果时才被考虑，我们将提取其中的定量部分。搜索涵盖了从创刊日起至2024年9月30日的MEDLINE、Embase、CINAHL、CENTRAL、Web of Science、Global Health、Scopus、IEEE Xplore、LILACS、African Index Medicus、IndMED以及灰色文献源。筛查和提取将在双人操作下进行。随机偏倚将使用RoB 2（随机对照试验）和ROBINS-I（非随机）进行评估。当结果在概念或统计上可比较时，将进行随机效应meta分析；否则，将展示结构化的综述合成。异质性将通过相对和绝对指标以及先验亚组或元回归（条件领域、护理水平、CDSS类型、准备度代理和研究设计）进行探索。
### Innovation
该研究通过系统综述和meta分析的方式，首次系统性地评估了CDSS在LMICs中的影响，填补了关于CDSS在这些国家临床结果和医疗服务影响方面的证据空白。研究将采用广泛的纳入标准和严格的偏倚评估方法，确保结果的全面和准确性。同时，该研究将采用随机效应meta分析和结构化叙事合成相结合的方法，提供较为详尽和科学的CDSS效果评估。
### Conclusion
该研究将全面评估CDSS在LMICs中的影响，通过综合分析，为政策制定者和医疗服务提供者提供可靠的证据支持，以改善临床结果和医疗服务。结果将揭示CDSS在不同条件领域、护理水平和CDSS类型下的有效性和潜在挑战，为后续研究和实践提供方向。
## 43. `cs.AI` - 准确目标下的目标隐私保护联邦学习：平衡公平与功能 [PDF](https://arxiv.org/pdf/2510.26841), [HTML](https://arxiv.org/abs/2510.26841)
### Authors
Kangkang Sun,Jun Wu,Minyi Guo,Jianhua Li,Jianwei Huang
### Background
联邦学习(FL)允许在无需数据共享的情况下进行协作模型训练，但参与者面临着一个根本性的挑战，即同时确保不同群体之间的公平性，同时保护敏感的客户端数据。现有方法在满足数据保护和公平性两个目标之间存在冲突和挑战。
### Innovation
提出了一个差分隐私公平FL算法(FedPF)，将一个多目标优化问题转化为零和博弈，其中公平性和隐私约束与模型功能相互竞争。证明了公平性和隐私保护之间的非单调关系，即适度的公平性约束在初期会提升模型泛化能力，但随后可能导致性能下降。实验结果表明，在保持竞争力的同时，算法可以减少高达42.9%的歧视现象，揭示了隐私公平性权衡的不可避免性。
### Conclusion
平衡隐私和公平性的主要挑战是需要在一定程度上进行权衡，而不能孤立优化其中之一。算法的源代码可以在指定的URL中找到，提供给读者进一步研究和应用的便利。
## 44. `cs.AI` - SpotIt: 通过形式验证评估Text-to-SQL评估 [PDF](https://arxiv.org/pdf/2510.26840), [HTML](https://arxiv.org/abs/2510.26840)
### Authors
Rocky Klopfenstein,Yang He,Andrew Tremante,Yuepeng Wang,Nina Narodytska,Haoze Wu
### Background
社区驱动的Text-to-SQL评估平台在追踪Text-to-SQL性能的最新状态方面发挥着关键作用。当前的评估方法主要依赖于测试，即比较生成的SQL查询和人类标注的黄金标准在静态测试数据库上的执行结果。然而，这种方法存在乐观的评估问题，即两个查询可能在测试数据库上产生了相同的输出结果，但实际上两者是不同的。
### Innovation
本文提出了一种新的评估管道，称为SpotIt，该管道使用形式上绑定的等价性验证引擎来积极搜索区分生成的SQL查询和黄金标准查询的数据库。开发了扩展现有验证器以支持与Text-to-SQL相关的更丰富的SQL子集的技术。实验证明，基于测试的方法可能会忽略生成的查询和黄金标准之间的差异。
### Conclusion
对十种Text-to-SQL方法在高知名度BIRD数据集上的性能评估表明，基于测试的方法经常会忽略生成的查询和黄金标准之间的差异。进一步分析验证结果揭示了当前Text-to-SQL评估的一个更复杂的情况。
## 45. `cs.AI` - 利用基础模型提升机器人感知与行动 [PDF](https://arxiv.org/pdf/2510.26855), [HTML](https://arxiv.org/abs/2510.26855)
### Authors
Reihaneh Mirjalili
### Background
该论文研究如何系统地利用基础模型来增强机器人的能力，使其能够在未结构化的环境中更有效地进行定位、交互和操作。具体而言，研究围绕四个核心问题展开，每个问题都解决了一个基本的机器人挑战，并为语义感知的机器人智能建立了统一框架
### Innovation
该论文创新性地探索了基础模型在提升机器人感知和行动能力方面的系统应用，旨在解决未结构化环境下的关键问题，并构建了一个语义感知的机器人智能框架
### Conclusion
本文提出的研究框架和方法能够为机器人在未结构化环境中的有效运行提供支持，展示了基础模型在机器人领域的潜在应用价值
## 46. `cs.AI` - 基于扩散驱动的预处理极简脑MRI生成 [PDF](https://arxiv.org/pdf/2510.26834), [HTML](https://arxiv.org/abs/2510.26834)
### Authors
Samuel W. Remedios,Aaron Carass,Jerry L. Prince,Blake E. Dewey
### Background
该研究旨在展示并对比三种用于生成3D $T_1$加权MRI人体脑部图像的去噪扩散概率模型（DDPMs）。研究人员使用了来自42,406名参与者的80,675幅图像，这些图像来自38个公开的脑MRI数据集。图像经过手动检查，以确保其质量较高并且排除了场形貌问题和病理过多的图像。这些图像经过了最小的预处理以保留视觉变异，并且为使DDPMs能够生成具有自然方向变化和不均匀性的图像，图像未被归一化到同一个坐标系统下也未进行偏差场校正。通过分割、弗雷切-碘尼森距离（FID）及主观检查进行了评估，结果表明三种DDPMs生成了连贯的MRI脑部体积。流速和流动预测模型获得了比样本预测模型更低的FID值，但所有模型在不同群体中的FID值仍高于实际图像。在重新排列实验中，生成的脑区体积分布与实际数据存在统计学差异，但流速和流动预测模型在丘脑和壳核的体积分布上的差异较少。
### Innovation
该研究首次提出了不进行颅骨去除或归一化的脑部数据3D非潜在扩散模型，即使统计测试结果不理想，所展示的DDPMs依然能够生成高分辨率的3D $T_1$加权脑部图像。所有模型权重及相应的推理代码均已公开发布。
### Conclusion
本文展示了并推出了首个用于生成无头骨去除或对齐的脑部数据的3D无潜伏扩散模型。尽管统计测试结果呈负面，但是所展示的这些DDPMs仍具备生成高分辨率的3D $T_1$加权脑部图像的能力。所有模型的权重与相应的推理代码均已在公开网址.setAlignmentavenir-com随时可访问。
## 47. `cs.AI` - Broken-Token: 通过计算字符每词（Characters-Per-Token）筛选混淆的提示 [PDF](https://arxiv.org/pdf/2510.26847), [HTML](https://arxiv.org/abs/2510.26847)
### Authors
Shaked Zychlinski,Yuval Kainan
### Background
大型语言模型（LLMs）容易受到减狱攻击，即恶意提示通过加密和字符级编码的形式进行伪装，从而绕过安全边界。尽管这些边界往往无法解读编码内容，但底层模型依然能够处理有害指令。现有方法成本高且依赖于额外模块，如专用的LLM或困惑度模型。
### Innovation
本文提出了一种名为CPT-Filtering的新颖、模型无关、代价几乎可以忽略且接近完美的安全边界技术。该方法利用字节对编码（BPE）分词器的内在行为，基于训练在自然语言上的分词器倾向于使用更多更短的分词来表示异常文本（如加密文本）。研究发现，即使是短输入，通过平均字符每词（CPT）的数量也能准确地识别出编码文本。
### Conclusion
CPT-Filtering提供了一种实用的防御层，可以立即部署于实时文本过滤和离线数据梳理中。实验显示，CPT阈值在大量数据集中的识别准确性很高。
## 48. `cs.AI` - VISAT：基于视觉属性在交通标志识别中的对抗性和分布偏移鲁棒性基准测试 [PDF](https://arxiv.org/pdf/2510.26833), [HTML](https://arxiv.org/abs/2510.26833)
### Authors
Simon Yu,Peilin Yu,Hongbo Zheng,Huajie Shao,Han Zhao,Lui Sha
### Background
本研究开发了一个名为VISAT的新颖开放数据集和基准测试套件，用于评估交通标志识别任务中模型的鲁棒性，特别是在存在视觉属性的情况下。该研究基于Mapillary交通标志数据集（MTSD），引入了两个基准，分别强调了对抗性攻击和分布偏移的鲁棒性。通过使用最先进的投影梯度下降（PGD）方法生成对抗性输入，研究团队评估了这些输入对流行模型的影响，并探讨了对抗性攻击对属性特定多任务学习（MTL）网络的影响，揭示了MTL任务之间的虚假相关性。对于分布偏移基准，研究团队利用ImageNet-C的现实数据污染和自然变化技术，评估了基模型和MTL模型的鲁棒性，并进一步通过交通标志颜色的合成变化（使用颜色量化技术）研究了MTL任务之间的虚假相关性。实验集中在两种主要的骨干网络上，即ResNet-152和ViT-B/32，并比较了基模型和MTL模型之间的性能。该研究旨在提高人们对交通标志识别中模型鲁棒性的理解，并揭示对抗性攻击和分布偏移带来的挑战。
### Innovation
该研究首次创建了一个基于视觉属性的交通标志数据集（VISAT），包含两个基准分别评估模型对抗性攻击和分布偏移的鲁棒性。通过使用PGD方法生成对抗性输入，研究探讨了对抗性攻击对MTL网络的影响，并利用ImageNet-C的数据腐蚀和自然变化技术来评估模型的鲁棒性。此外，还通过颜色量化技术进一步探索了MTL任务之间的虚假相关性。
### Conclusion
VISAT数据集和基准测试框架有助于理解交通标志识别中模型的鲁棒性，揭示了对抗性攻击和分布偏移带来的挑战。该研究认为，这将有助于推动更鲁棒模型在自动驾驶和网络物理系统等实际应用中的发展。
## 49. `cs.AI` - CAS-Spec：针对LLMs的自适应级联自我推测解码的即时无损推理加速 [PDF](https://arxiv.org/pdf/2510.26843), [HTML](https://arxiv.org/abs/2510.26843)
### Authors
Zhiyuan Ning,Jiawei Shao,Ruge Xu,Xinfei Guo,Jun Zhang,Chi Zhang,Xuelong Li
### Background
自推测解码已成为一种广泛采用的有效技术，用于加速大型语言模型（LLMs）的无损推理。尽管在线自我推测方法提供了无缝集成和广泛的用途，但它们通常未能达到依赖于专门训练的方法所实现的速度增益。级联多个快速模型可以带来进一步的加速和灵活性，但多模型训练的高昂成本限制了其实用应用。
### Innovation
本文提出了名为CAS-Spec的新颖方法，该方法利用动态可切换的推理加速（DSIA）策略（包括层稀疏性和激活量化）来构造推测性草稿模型。为了解决传统分级算法在自我推测解码方法中的低效率问题，引入了一种动态树级联（DyTC）算法，该算法根据接受率和延迟预测的启发式规则动态路由多级草稿模型并分配草稿长度。CAS-Spec方法在各LLM和数据集上相对于现有即时自我推测解码方法实现了最先进的加速，平均加速从1.1倍到2.3倍不等。与基于级联和基于树的基线算法相比，DyTC分别提高了平均加速率47%和48%。
### Conclusion
CAS-Spec方法可以很容易地集成到大多数现有的LLM中，并且随着自我推测解码技术的不断进步，CAS-Spec方法有望进一步加速。
## 50. `cs.AI` - 感知类别语义缓存以适用于异构大语言模型工作负载 [PDF](https://arxiv.org/pdf/2510.26835), [HTML](https://arxiv.org/abs/2510.26835)
### Authors
Chen Wang,Xunzhuo Liu,Yue Zhu,Alaa Youssef,Priya Nagpurkar,Huamin Chen
### Background
LLM服务系统处理具有不同特性的异构查询负载。代码查询在嵌入空间中紧密聚集，而对话查询则分布稀疏。内容的新鲜度可以从分钟到数月不等。查询重复模式范围广泛，代码为幂律分布，而对话为均匀分布，导致缓存命中率分布呈现长尾效应。高重复类别可能会达到40-60%的缓存命中率，而低重复或易变类别会达到5-15%的缓存命中率。向量数据库由于远程搜索成本较高（30ms），为了收支平衡需要达到15-20%的缓存命中率，这意味着20-30%的生产流量无法被缓存。固定缓存策略加剧了这一问题，固定阈值在密集空间会导致错误的正面命中，而在稀疏空间则会错过有效的同义短语；固定TTL可能会浪费内存或提供过时的数据。
### Innovation
该论文提出了一种感知类别的语义缓存方法，其中相似阈值、TTL和配额根据查询类别有所不同。论文还提出了一个混合架构，将内存中的HNSW搜索与外部文档存储分离，将错过成本从30ms降低到2ms。这一降低使得低缓存命中率类别（在3-5%命中率下）变得更加经济可行，从而可以覆盖整个负载分布的流量。动态负载基于策略扩展了这一框架，在理论上将受过载模型影响的流量减少了9-17%。
### Conclusion
这种感知类别的语义缓存方法通过根据不同查询类别调整相似阈值、TTL和配额来优化缓存策略。通过混合架构解决了固定缓存策略的问题，并提高了缓存效率，使得低缓存命中率的类别也变得经济可行，从而极大地扩展了缓存能够覆盖的流量范围。动态负载调整策略进一步增强了这种方法的适应性和效率。
## 51. `cs.AI` - 视觉语言模型在视读测量方面表现如何？使用MeasureBench进行基准测试 [PDF](https://arxiv.org/pdf/2510.26865), [HTML](https://arxiv.org/abs/2510.26865)
### Authors
Fenfen Lin,Yesheng Liu,Haiyu Xu,Chen Yue,Zheqi He,Mingxuan Zhao,Miguel Hu Chen,Jiakang Liu,JG Yao,Xi Yang
### Background
阅读测量仪器对于人类来说是轻而易举的事，不需要太多领域的专业知识。然而，即使是最先进的视觉语言模型（VLMs）依然在这方面遇到了很大的挑战，在初步评估中发现它们处理视觉测量阅读任务并不容易。
### Innovation
本文引入了MeasureBench，这是一个涵盖不同类型测量的真实和合成图像的视觉测量阅读基准。文中还提供了一个可扩展的数据生成管道，能够生成具有可控制视觉效果的指定类型的测量表，从而实现关键细节的缩放变化，例如指针、刻度、字体、照明和杂乱。评估结果显示，即使是最强大的视觉语言模型在测量阅读任务上依然表现不佳，主要表现为指示器定位错误，模型能够识别数字或标签，但错误识别指针的关键位置或对齐，导致大量数值错误。
### Conclusion
我们的分析指出了当前视觉语言模型在精细空间定位方面的基本局限性。希望这个资源能够促进未来对于视觉和语言之间关联数值能力和精细空间感知的进展，缩小识别数字和测量世界之间的差距。初步实验证明基于强化学习的方法在模拟数据集上效果较好，但在真实世界图像上表现不太理想。
## 52. `cs.AI` - BI-DCGAN：一种高效多样性的理论支持贝努里框架生成对抗网络 [PDF](https://arxiv.org/pdf/2510.26892), [HTML](https://arxiv.org/abs/2510.26892)
### Authors
Mahsa Valizadeh,Rui Tuo,James Caverlee
### Background
生成对抗网络（GANs）在生成合成数据方面表现出色，但是仍然面临着模式崩溃的问题，即生成器生成的输出范围狭窄，能够蒙骗判别器但未能捕捉到数据的完整分布。这种局限性在需要多样性和不确定性意识的实际应用场景中尤其突出。为应对这一问题，作者引入了BI-DCGAN，该模型是DCGAN的贝叶斯拓展，能够将模型不确定性融入生成过程，同时保持计算效率。BI-DCGAN通过Backpropagation的方式学习网络权重分布，并使用均值场变分推断在生成对抗网络训练中高效地近似后验分布。理论证明表明，贝叶斯模型能够增强生成样本的多样性。
### Innovation
引入了BI-DCGAN，这是一种基于贝叶斯方法的DCGAN扩展版本，结合了贝叶斯学习和高效的变分推断，能够在保持计算效率的同时增强生成样本的多样性。该研究首次通过协方差矩阵分析给出了理论证明，证明了贝叶斯建模能够在GAN中增强样本多样性。
### Conclusion
实验结果验证了这一理论结论，BI-DCGAN在标准生成基准测试上生成的样本比传统DCGAN更加多样化且更具鲁棒性，同时保持了高效训练。这些发现使BI-DCGAN成为在需同时考虑多样性和不确定性的应用领域中一个可扩展且及时的解决方案，与当前资源密集度较高的替代方法如扩散模型相比，它更具可行性。
## 53. `cs.AI` - 如何看待Grokipedia和Wikipedia的相似性？多维度文本和结构比较 [PDF](https://arxiv.org/pdf/2510.26899), [HTML](https://arxiv.org/abs/2510.26899)
### Authors
Taha Yasseri
### Background
Grokipedia是xAI开发的一款由人工智能生成的百科全书，旨在回应维基百科中的意识形态和结构偏见。本文通过对比Grokipedia和Wikipedia的382篇文章对齐对，使用词汇丰富度、可读性、结构组织、参考密度和语义相似性等指标来评估两者在形式和内容上的相似性。
### Innovation
本研究采用了大规模的计算方法进行对比分析，通过多个维度（如词汇丰富度、可读性、结构组织、参考密度和语义相似性）对两个平台的内容进行评估，从而揭示AI生成的内容与传统平台的异同。
### Conclusion
研究结果显示，尽管Grokipedia在语义和风格上与Wikipedia非常接近，但在词汇多样性、参考密度和结构深度上存在差异，AI生成的内容更倾向于扩展叙述而非基于引用的验证。这表明AI生成的知识内容在信息范围上与Wikipedia基本一致，但在编辑规范上有所不同，未来可能引发新的透明性、来源和知识治理方面的矛盾。
## 54. `cs.AI` - 在解锁生成智能指导下的无结构环境中的异构机器人协作 [PDF](https://arxiv.org/pdf/2510.26915), [HTML](https://arxiv.org/abs/2510.26915)
### Authors
Zachary Ravichandran,Fernando Cladera,Ankit Prabhu,Jason Hughes,Varun Murali,Camillo Taylor,George J. Pappas,Vijay Kumar
### Background
异构机器人团队在现实环境中执行复杂的任务往往需要协作和根据获取的信息进行适应。由于这些团队经常在不受结构化的环境中操作——不确定、开放的环境且没有先验地图——子任务必须基于机器人能力和物理世界进行操作。现阶段的大规模语言模型（LLM）赋能的团队方法通常假设结构化和已知的环境，这限制了它们在无结构环境中的应用。
### Innovation
我们提出了SPINE-HT框架，通过一个三阶段的过程将LLM的推理能力扎根于异构机器人团队的上下文中。给定语言规范，描述任务目标和团队能力，LLM生成可操作的子任务，并进行可行性验证。基于能力（如可通行性或感知）分配任务，并根据在线操作期间收集的反馈进行调整。在仿真和实际实验中，该框架在成功率上表现优异，超越了之前的LLM赋能的异构团队方法。
### Conclusion
我们的方法在模拟和实际实验中达到了87%的成功率，证明了其在涉及机器人能力推理和在线反馈调整子任务的能力。这一框架扩大了LLM在无结构环境中的应用范围。
## 55. `cs.AI` - Scale-Aware Curriculum Learning for Data-Efficient Lung Nodule Detection with YOLOv11 [PDF](https://arxiv.org/pdf/2510.26923), [HTML](https://arxiv.org/abs/2510.26923)
### Authors
Yi Luo,Yike Guo,Hamed Hooshangnejad,Kai Ding
### Background
肺结节检测在胸部CT中对于早期肺癌诊断至关重要，但现有的深度学习方法在临床应用中遇到挑战，尤其是在标注数据有限的情况下。传统的分阶段学习策略在数据稀缺场景中表现不佳。
### Innovation
提出了可适应规模的分阶段学习策略（SACL），这是一种基于可用数据规模动态调整课程设计的新训练策略。SACL引入了三种关键机制：自适应周期调度、困难样本注入以及规模感知优化。
### Conclusion
SACL在LUNA25数据集上使用YOLOv11作为基础检测器进行评估，结果显示SACL在全数据集上达到与静态分阶段学习相当的mAP50性能，在数据受限条件下（10%、20%、50%的训练数据）分别提高了4.6%、3.5%和2.0%。SACL无需修改架构即可在不同数据规模下提供鲁棒训练，为医疗保健机构提供了在有限注释资源下开发有效肺结节检测系统的实用解决方案。
## 56. `cs.AI` - 机器能高效地思考吗？ [PDF](https://arxiv.org/pdf/2510.26954), [HTML](https://arxiv.org/abs/2510.26954)
### Authors
Adam Winchell
### Background
传统的图灵测试已经不足以区分人类和机器智能，并且现有的高级人工智能系统已经通过了原始的图灵测试，从而引发了一些严重的伦理和环境问题。因此，迫切需要更新这个测试，使其更加准确且有实际意义。
### Innovation
本文扩展了最初的模仿游戏，新增了衡量因素：回答问题所消耗的能量。通过增加能量约束，新的测试要求我们从效率的角度来评价智能，将抽象的思维问题与有限资源的现实联系起来。此外，由于新测试有一个可衡量的、实际的终点，这弥补了原始测试缺乏这个特点的不足。这种额外的约束促使社会权衡使用人工智能的时间节省与其总资源成本之间的关系。
### Conclusion
这项新的测试确保了智能评估有一个实际可衡量的终点，同时从效率的角度重新定义图灵测试，使得智能评估更加符合现实世界的限制。
## 57. `cs.AI` - 基于LLM的物联网/工业物联网网络多分类攻击分析与缓解框架 [PDF](https://arxiv.org/pdf/2510.26941), [HTML](https://arxiv.org/abs/2510.26941)
### Authors
Seif Ikbarieh,Maanak Gupta,Elmahedi Mahalal
### Background
物联网迅速发展，改变了各行业的通信和操作方式，同时也增加了攻击面和安全漏洞。尽管人工智能在保障物联网安全方面起着关键作用，能够实现攻击检测、攻击行为分析和缓解建议，但关于其效果的评估仍然停留在定性阶段。由于缺乏用于量化衡量AI攻击分析和缓解的标准、客观基准，使得模型效果的一致性评估受到阻碍。
### Innovation
本文提出了一种结合机器学习（ML）进行多分类攻击检测与大语言模型（LLMs）进行攻击行为分析和缓解建议的混合框架。通过在Edge-IIoTset和CICIoT2023数据集上对几种ML和深度学习（DL）分类器进行基准测试，采用结构化角色扮演提示工程和检索增强生成（RAG）技术，引导ChatGPT-o3和DeepSeek-R1生成详细且情境意识的回复。引入了新的评价指标并利用由ChatGPT-4o、DeepSeek-V3等组成的多个法官LLM独立评价这些回复。
### Conclusion
研究表明，随机森林在检测模型中表现出最佳性能，而ChatGPT-o3在攻击分析和缓解方面优于DeepSeek-R1。
## 58. `cs.AI` - Mind the Gaps: 审计和减少大规模移动预测中的群体不平等 [PDF](https://arxiv.org/pdf/2510.26940), [HTML](https://arxiv.org/abs/2510.26940)
### Authors
Ashwin Kumar,Hanyu Zhang,David A. Schweidel,William Yeoh
### Background
移动预测在移动应用、零售和公共卫生等领域得到越来越多的应用，但其社会影响尚未得到充分研究。本文审计了大型数据集上训练的最先进的移动预测模型，并指出基于用户人口统计信息的隐藏差异。这些模型中的许多并没有充分考虑到不同群体之间的差异性，这可能导致在不同地理位置和用户群体之间预测准确性的显著差异。
### Innovation
本文提出了一种公平导向的增量采样方法（FGIS），该方法是一种群体感知的采样策略，适用于增量数据收集场景。为了进行群体划分，引入了一种大小感知的K均值聚类方法（SAKM），它在隐式移动空间中分组用户，并确保遵循人口普查数据提供的群体比例。基于这些标签，我们提出了一个采样算法，该算法优先考虑预期性能提升和当前群体代表性的用户。该方法逐步构建训练数据集，以减少群体间的性能差距同时保持整体准确性。
### Conclusion
实验结果表明，该方法在最先进的MetaPath2Vec模型和变压器编码器模型上，能够将群体间的整体差异减少高达40%，且几乎没有准确性方面的损失。在早期采样阶段效果尤为显著，这表明公平导向的策略即使在资源有限的情况下也能带来实质性的好处。研究结果揭示了移动预测管道中的结构性不平等，并展示了如何通过轻量级的数据中心干预来改进公平性，尤其是对于数据有限的应用而言。
## 59. `cs.AI` - RepV：可实现安全分离的潜在空间以实现可扩展的神经符号计划验证 [PDF](https://arxiv.org/pdf/2510.26935), [HTML](https://arxiv.org/abs/2510.26935)
### Authors
Yunhao Yang,Neel P. Bhatt,Pranay Samineni,Rohan Siva,Zhanyang Wang,Ufuk Topcu
### Background
随着AI系统迁移到关键安全领域，确保其行为符合预定义规则仍是一个挑战。形式方法可以提供可验证的保证，但需要手工编写的时序逻辑规范，这在表达能力和用户友好性方面相对有限。深度学习方法能够使用自然语言约束评估计划，但其不透明的决策过程可能导致潜在严重的误分类问题。现有方法各有利弊：形式验证方法需要手工编写规范，而深度学习方法虽然能够处理自然语言约束但决策过程不透明。
### Innovation
本文介绍了一种名为RepV的神经符号验证器，它通过学习一个潜在空间，使安全和不安全的计划得以线性分离，同时兼备这两种方法的优点。从一个简单的预标记计划集中开始，RepV使用轻量级投影器嵌入每个计划及其生成的语言模型解释，并在一个前向传播中使用冻结的线性边界验证未见过的自然语言规则。RepV提供了基于潜在空间中位置的概率性验证保证，这使得可以通过验证驱动的规划精炼提升规则的遵循性，而无需人工注释。与基线方法相比，RepV提高了计划合规性预测的准确性，在多个规划领域中还优于普通的微调基线。
### Conclusion
研究结果表明，安全分离的潜在空间提供了一个可扩展的、即插即用的原理，用于可靠的神经符号计划验证。通过RepV，可以在保持准确性的同时减少参数数量，并且能够驱动规划器的精炼，提升规则的合规性。代码和数据可在指定链接获取。
## 60. `cs.AI` - 使用显著对象检测识别规避GDPR的操控性饼干通知栏 [PDF](https://arxiv.org/pdf/2510.26967), [HTML](https://arxiv.org/abs/2510.26967)
### Authors
Riley Grossman,Michael Smith,Cristian Borcea,Yi Chen
### Background
本文研究了遵守《通用数据保护条例》（GDPR）的饼干通知栏中是否使用了美学操纵，以吸引用户注意个人数据共享许可按钮。同时评估了这些通知栏是否符合GDPR和国家数据保护机构的建议。作者访问了2,579个网站，发现45%的网站拥有完全合规的通知栏，但有38%的合规通知栏使用了美学操纵。为了研究用户和/或网站位置对饼干通知栏设计的影响，作者选取了在欧盟（规则执行更为严格）和非欧盟内的网站进行比较分析，结果显示，来自欧盟的网站中有13.9%的网站会在用户来自美国时改变通知栏设计，并且欧盟网站使用美学操纵的比例比非欧盟网站高48.3%.
### Innovation
本文创新性地使用计算机视觉模型进行显著对象检测，测量通知栏元素的显著性（即吸引注意力的程度），从而发现新的美学操纵形式。研究结果表明，美学操纵更为普遍（38% vs 27%）。此外，作者通过比较考查不同地理位置的网站来研究隐私法规执行对网站设计的影响，提供了新的研究视角。
### Conclusion
通过计算机视觉模型识别显著对象，发现欧盟网站在用户来自美国时更常改变通知栏设计，并且欧盟网站使用美学操纵的比例比非欧盟网站高出48.3%，暗示其创新性地回应隐私法规。
## 61. `cs.AI` - MEDIQA-OE 2025 年医疗订单提取共享任务概述 [PDF](https://arxiv.org/pdf/2510.26974), [HTML](https://arxiv.org/abs/2510.26974)
### Authors
Jean-Philippe Corbeil,Asma Ben Abacha,Jerome Tremblay,Phillip Swazinna,Akila Jeeson Daniel,Miguel Del-Agua,Francois Beaulieu
### Background
临床文档越来越多地使用自动语音识别和总结，但将对话转化为电子健康记录中的可操作医疗命令尚未得到探索。解决这一问题可以大幅减轻医务人员的文档负担，直接对下游患者护理产生影响。
### Innovation
介绍了 MEDIQA-OE 2025 共享任务，这是首次针对从医生-患者咨询中提取医疗命令的挑战。六支队伍参与了此次共享任务，尝试了广泛的策略和大型语言模型（包括闭合权重和开放权重两种类型）。
### Conclusion
在这篇文章中，我们描述了 MEDIQA-OE 任务、数据集、最终排行榜和参赛队伍的解决方案。
## 62. `cs.AI` - 在有限计算预算下的细粒度迭代对抗攻击 [PDF](https://arxiv.org/pdf/2510.26981), [HTML](https://arxiv.org/abs/2510.26981)
### Authors
Zhichao Hou,Weizhi Gao,Xiaorui Liu
### Background
在AI安全研究中，特别是在计算资源有限的情况下，如何在固定计算预算内最大化迭代对抗攻击的有效性是一个关键挑战。粗略减少攻击迭代次数虽能降低成本，但也显著削弱了攻击效果。因此，该研究旨在通过一种精细的控制机制，在预算限制下实现攻击效果的最大化。
### Innovation
文中提出了一种选择性重计算层激活的细粒度控制机制，用于在迭代和层间层面进行精细控制。这一机制能够在固定计算预算内有效提升攻击效果，即使是在对抗训练场景中，仅用原来的30%预算也能达到相近的性能。
### Conclusion
实验结果表明，该方法在同等成本条件下持续优于现有基线方法，并且在对抗训练中能够显著节省预算，同时保持性能。
## 63. `cs.AI` - LLMs are Overconfident: Evaluating Confidence Interval Calibration with FermiEval [PDF](https://arxiv.org/pdf/2510.26995), [HTML](https://arxiv.org/abs/2510.26995)
### Authors
Elliot L. Epstein,John Winnicki,Thanawat Sornwanee,Rajat Dwaraknath
### Background
大型语言模型（LLMs）擅长数值估计，但在准确量化不确定性方面存在困难。已有研究指出，LLMs 在构建对自己答案的置信区间上表现不佳，经常表现为系统性地过于自信。
### Innovation
作者提出了一个名为 FermiEval 的基准测试，用于评估 LLMs 对 Fermi 风格估计问题的置信区间建构情况。通过这种方法，作者发现即使名义上的 99% 置信区间也仅覆盖真实答案的 65%。通过调用 conformal prediction 方法和直接对数概率汲取以及分位数调整方法，作者能够减少 LLMs 的高置信区间下的过度自信。
### Conclusion
作者提出了一种感知隧道理论来解释为什么 LLMs 展现过度自信的现象：在处理不确定性时，它们仿佛从自己推断出的分布的截断区域中采样，忽略了分布的尾部。
## 64. `cs.AI` - 基于AIoT的智能教育系统：两层认证和情境感知辅导框架 [PDF](https://arxiv.org/pdf/2510.26999), [HTML](https://arxiv.org/abs/2510.26999)
### Authors
Adithya Neelakantan,Pratik Satpute,Prerna Shinde,Tejas Manjunatha Devang
### Background
当前教室面临诸多持久性的挑战，包括考勤作假、个性化不足、学生参与度低以及资源配置效率低下。这些挑战限制了教育的有效性和效率，为此，需要一种结合人工智能和物联网技术的综合解决方案来解决这些问题。
### Innovation
该智能教育系统通过集成基于RFID的双因素认证系统、AI驱动的助手、自动生成测验工具以及自动调节教室环境的功能，提供了安全、适应性强且高效的学习环境。特别是，系统通过两层认证和情境感知技术，增强了安全性和个性化支持，同时减少了行政负担，并改善了学生参与度和考试评估的灵活性。
### Conclusion
通过结合人工智能和物联网技术，该系统为教育创新提供了可扩展的蓝本，能够有效提升学生的学习成果，并通过综合应用最新的技术手段支持更具包容性的学习环境。
## 65. `cs.AI` - Jasmine: 一种简单、高性能且可扩展的JAX基世界建模代码库 [PDF](https://arxiv.org/pdf/2510.27002), [HTML](https://arxiv.org/abs/2510.27002)
### Authors
Mihir Mahajan,Alfred Nguyen,Franz Srambical,Stefan Bauer
### Background
随着世界模型在解决机器人等领域的数据稀缺性问题方面的地位日益重要，现有的开源世界建模训练基础设施仍处于起步阶段。鉴于此，本文介绍了一种名为Jasmine的高性能JAX基世界模型代码库，该代码库能够从单个主机扩展到数百个加速器，同时仅需最小的代码更改。
### Innovation
Jasmine实现了比之前开源实现快一个数量级的CoinRun案例研究复现，这得益于其在数据加载、训练和检查点方面的一系列性能优化。此外，代码库还确保了全程可重复训练，并支持多种切分配置。
### Conclusion
通过将Jasmine与精心筛选的大型数据集相结合，本文建立了不同模型家族和架构变体的严格基准测试管道，从而有助于深入研究和比较不同方法的性能。
## 66. `cs.AI` - 适用于高效语言模型的弹性架构搜索 [PDF](https://arxiv.org/pdf/2510.27037), [HTML](https://arxiv.org/abs/2510.27037)
### Authors
Shang Wang
### Background
随着大型预训练语言模型在自然语言理解（NLU）任务中的重要性日益增加，其庞大的计算和内存需求引发了经济和环境方面的担忧。
### Innovation
本文引入了一种名为Elastic Language Model (ELM)的新型神经架构搜索（NAS）方法，该方法针对紧凑型语言模型进行了优化。ELM通过引入灵活的搜索空间、高效的变压器块和动态模块来调整维度和头的数量，这些创新提高了搜索过程的效率和灵活性，促进了模型架构的更全面和有效地探索。此外，还提出了新颖的知识蒸馏损失，以保留每个块的独特特性，在搜索过程中提高对架构选择的区分能力。
### Conclusion
实验表明，由ELM发现的模型在掩码语言建模和因因果语言建模任务中明显优于现有方法。
## 67. `cs.AI` - 机器人领域基于空间推理的多模态神经符号方法视觉定位 [PDF](https://arxiv.org/pdf/2510.27033), [HTML](https://arxiv.org/abs/2510.27033)
### Authors
Simindokht Jahangard,Mehrzad Mohammadi,Abhinav Dhall,Hamid Rezatofighi
### Background
视觉推理，尤其是空间推理，是一项具有挑战性的认知任务，要求理解对象之间的关系及其在复杂环境中的相互作用，尤其是在机器人领域。现有的视觉语言模型（VLMs）在感知任务上表现出色，但在细粒度的空间推理方面存在困难，这是因为它们依赖于隐式的、基于相关性的推理及单一图像的使用。
### Innovation
我们提出了一种新颖的神经符号框架，结合全景图像和3D点云信息，将神经感知与符号推理结合起来，明确建模空间和逻辑关系。该框架包括一个感知模块，用于检测实体并提取属性，以及一个推理模块，用于构建结构化的场景图以支持精确和可解释的查询。
### Conclusion
我们在JRDB-Reasoning数据集上评估了这种方法，结果表明该方法在拥挤的、由人构建的环境中表现出优越的性能和可靠性，并且保持了适合机器人和具备形体AI应用的轻量设计。
## 68. `cs.AI` - 基于公平评估的方差感知类臂算法框架 [PDF](https://arxiv.org/pdf/2510.27001), [HTML](https://arxiv.org/abs/2510.27001)
### Authors
Elise Wolf
### Background
多臂老虎机（MAB）问题作为更加复杂的强化学习算法的基本构件，但对其算法性能的评估和比较仍然具有挑战性，主要由于缺乏标准化的评估条件和可重复性。特别是，对于基于方差的古典方法（如UCB）的扩展，在不同环境下的表现差异显著。因此，研究如何系统地观察不同类型算法之间的性能差异及其具体应用场景下的比较条件变得十分必要。
### Innovation
本研究提出了一个可用于系统评估MAB算法的框架，并通过定义明确的实验设置、多种性能指标（奖励、遗憾、奖励分布、价值风险以及动作最优性）及交互式评估界面，实现了评估模型的可重复性和透明分析。研究结果表明，在高不确定性条件下，方差感知算法可以提供优势；而传统算法则在较为分离的场景或经过精细调整后表现出色。这项研究的主要贡献在于提供了一种评估框架和展示了方差感知算法优势的具体条件。
### Conclusion
本研究为MAB算法的系统评估提供了一个框架，并揭示了方差感知方法在特定条件下优于经典方法的条件。
## 69. `cs.AI` - 基于框架语义模式在医疗保健领域识别上报不足的可报告事件：以性别暴力为例 [PDF](https://arxiv.org/pdf/2510.26969), [HTML](https://arxiv.org/abs/2510.26969)
### Authors
Lívia Dutra,Arthur Lorenzi,Laís Berno,Franciany Campos,Karoline Biscardi,Kenneth Brown,Marcelo Viridiano,Frederico Belcavello,Ely Matos,Olívia Guaranha,Erik Santos,Sofia Reinach,Tiago Timponi Torrent
### Background
本文介绍了一种在医疗领域识别可报告事件的方法，该方法利用语义框架定义细粒度模式并在非结构化数据中搜索这些模式，具体是通过在电子医疗记录的开放文本字段中查找这些模式来实现。本文将该方法应用于医学记录中的性别暴力报告不足问题，相关数据来自巴西SUS APS系统中的2100万句葡萄牙语句子。研究结果表明，该方法能够识别暴力报告，精度达到0.726，证明了其实用价值。该方法设计为透明、高效、低碳且语言无关的方式，并具有在其他公共卫生领域应用的潜力，从而推动自然语言处理技术在公共卫生系统中的广泛、伦理及可解释使用.
### Innovation
该方法使用语义框架定义细粒度模式并搜索在未结构化的数据中（此例中是电子医疗记录的开放文本字段），用于识别健康护理领域中的可报告事件，尤其是性别暴力。该创新方法能够有效提高性别暴力的报告率与系统识别的准确性，验证了在公共及伦理角度上对自然语言处理技术的应用价值，同时也提供了一种可扩展的应用框架至其他健康监测场景，并且具有透明、效率高、低碳和语言无关的特点，更加符合现代公共卫生系统的需求.
### Conclusion
本文验证了框架语义模式在识别医疗保健领域可报告事件中的有效性和实用性，并展示了它们对于提高性别暴力报告的努力和贡献。精确度达到0.726的结果证明了所提出方法的有效性。该方法作为一种开放且易于扩展的方式，可以被用于其他健康监控场合，推进自然语言处理技术在公共健康系统中的广泛应用，同时也证实了其具备透明、高效、低碳和语言无关的特点。
## 70. `cs.AI` - 通过上下文学习检测LLMs中的数据污染 [PDF](https://arxiv.org/pdf/2510.27055), [HTML](https://arxiv.org/abs/2510.27055)
### Authors
Michał Zawalski,Meriem Boubdir,Klaudia Bałazy,Besmira Nushi,Pablo Ribalta
### Background
该研究背景在于当前大型语言模型(Large Language Models, LLMs)在训练过程中可能面临数据污染问题，即训练数据中包含不适宜或错误的数据，这会影响模型的性能和可靠性。因此，如何有效检测和量化这种污染成为学术界和工业界关注的焦点。
### Innovation
该论文提出了一种名为CoDeC的方法，通过上下文学习来检测和量化训练数据污染。CoDeC通过测量内语境学习对模型性能的影响，将模型记住的训练数据与不在训练分布中的数据区分开来。实验表明，这种方法能够生成可解释的污染得分，并清晰区分已见过的数据集和未见过的数据集，揭示了开放权重模型中未披露培训语料库的强大记忆特征。
### Conclusion
CoDeC方法简单自动化，并且对模型和数据集具有广泛的适用性，便于纳入基准评估中。该方法有望成为检测和量化大型语言模型训练数据污染的有效工具。
## 71. `cs.AI` - Hausa性别歧视检测数据集的创建及基线模型研究 [PDF](https://arxiv.org/pdf/2510.27038), [HTML](https://arxiv.org/abs/2510.27038)
### Authors
Fatima Adam Muhammad,Shamsuddeen Muhammad Hassan,Isa Inuwa-Dutse
### Background
性别歧视通过维持刻板印象、偏见和歧视性规范而强化性别不平等和社交排斥。随着在线平台为各种形式的性别歧视提供了滋生的土壤，及时有效检测和减轻性别歧视的需求日益增长。目前虽然在资源丰富语言中有广泛使用计算方法进行性别歧视检测，但在资源匮乏语言中这一领域进展有限，由于这些语言的语用特征和文化差异使得性别歧视的表达和感知方式受到影响。
### Innovation
本研究首次创建了Hausa性别歧视检测数据集，通过社区参与、定性编码和数据增广的方式进行开发。进一步探索了传统机器学习分类器及预训练多语言语言模型的应用，并研究了少样本学习在检测Hausa语言中性别歧视方面的有效性。研究结果强调了捕捉文化细微差别的挑战，特别是在需要澄清和使用惯用语表达的情况下，并揭示了这些情况下出现大量误报的趋势。
### Conclusion
这项研究不仅填补了Hausa性别歧视检测领域的空白，还为该领域的其他研究提供了基线模型参考，特别是在文化和语言多样性背景下检测性别歧视的新方法方面取得了实质性的进展。
## 72. `cs.AI` - 使用检索增强生成适应新兴网络安全的大语言模型 [PDF](https://arxiv.org/pdf/2510.27080), [HTML](https://arxiv.org/abs/2510.27080)
### Authors
Arnabh Borah,Md Tanvirul Alam,Nidhi Rastogi
### Background
随着安全应用越来越多地依赖大型语言模型（LLMs）进行网络威胁检测，LLMs 的不透明推理限制了信任，特别是在需要特定网络安全知识的决策中。由于安全威胁迅速演变，LLMs 不仅需要回忆历史事件，还需要适应新兴的漏洞和攻击模式。检索增强生成（RAG）在一般LLM应用中已经显示出有效性，但在网络安全领域的潜力尚未被充分探索。
### Innovation
本文介绍了一种基于RAG的框架，旨在通过外部数据集和Llama-3-8B-Instruct模型，增强LLM在知识保留和时间推理方面的准确性。评估了基本的RAG、优化的混合检索方法，并在多个性能指标上进行了比较分析。研究结果表明混合检索对于增强LLM在网络安全任务中的适应性和可靠性具有潜力。
### Conclusion
研究结果强调了混合检索增强框架在强化LLM的适应性和可靠性方面的潜力，使其更适用于网络安全任务。
## 73. `cs.AI` - 向算法相似性度量迈进 [PDF](https://arxiv.org/pdf/2510.27063), [HTML](https://arxiv.org/abs/2510.27063)
### Authors
Shairoz Sohail,Taher Ali
### Background
给定同样的问题，两种算法是否有实质性的差异？在全背景下，这个问题是不可计算的，尤其是竞争相似度概念使其实际难以见效。但在许多应用场景，如代码克隆检测或程序合成中，实用且一致的相似性度量是必要的。已有研究介绍了几种等价性和相似性概念，但缺乏合适的框架将其嵌入到适合下游任务的特征空间中。因此，本文旨在构建一个评估、记忆和操作复杂性的框架（EMOC），以支持算法类型分类、接近克隆检测和LLM生成程序多样性量化等任务。
### Innovation
本文介绍了一种新的框架EMOC（评估-记忆-操作复杂性），将算法实现嵌入到适合下游任务的特征空间中。开发了一个精心构建的数据集PACD，涵盖了来自三种问题的验证Python实现。结果表明，使用EMOC特征可以支持算法类型分类、接近克隆检测以及LLM生成程序多样性量化。为了促进未来的研究和可重现实验，代码、数据和用于计算EMOC嵌入的实用工具均被公布出来。
### Conclusion
本文构建的EMOC框架成功支持了算法类型分类、克隆检测和多样性量化等任务；发布的PACD数据集和实用工具有助于算法相似性研究的未来进步。然而，仍然需要进一步研究以改善EMOC框架并适应更多不同的算法类型。
## 74. `cs.AI` - 一致性训练有助于阻止奉承和越界 [PDF](https://arxiv.org/pdf/2510.27062), [HTML](https://arxiv.org/abs/2510.27062)
### Authors
Alex Irpan,Alexander Matt Turner,Mark Kurzeja,David K. Elson,Rohin Shah
### Background
大型语言模型（LLM）的准确性与其接受的提示有关，简单的提示变更可能会损害模型的准确性。模型可能接受用户的主观信念（谄媚行为）或执行不适当的要求，这些要求可能是被封装在特殊文本中的（打破囚笼）。已有研究表明某种类型的对齐训练可以减轻这些问题的影响。这些训练方法通过使模型在面对某些无关提示时的行为保持一致来减少模型的脆弱性。
### Innovation
本文介绍了一种新的自监督一致性训练方法——激活一致性训练（ACT），旨在使模型在数据增强后的行为保持一致。同时，它还采用了另一种一致性训练方法——偏置增强一致性训练（BCT），并通过这两者减少了Gemini 2.5 Flash模型对外部输出和内部激活的不相关提示的敏感性。该方法的优点在于使用模型自身的响应作为训练数据，从而避免了使用静态数据集训练带来的过时数据问题。研究还表明，这两种方法在减少奉承行为方面效果相同，但在破解控制方面BCT更为有效。
### Conclusion
一致性训练是改善LLM对齐问题的一种有效方法，特别是在面对奉承和破解控制等问题时。通过这种训练，可以增强模型的稳健性，减少其对外部扰动的敏感性，从而提高其整体效果和适用性。这种训练方法还可简化训练流程，减少对外部数据集的依赖。
## 75. `cs.AI` - QiNN-QJ：一种基于量子跳变的量子启发式神经网络在多模态情感分析中的应用 [PDF](https://arxiv.org/pdf/2510.27091), [HTML](https://arxiv.org/abs/2510.27091)
### Authors
Yiwei Chen,Kehuan Yan,Yu Pan,Daoyi Dong
### Background
量子理论提供了一些非经典原理，如叠加和纠缠，这些原理有望在机器学习中开辟新的范式。然而，现有的大多数量子启发式融合模型仅依赖于单元或类似单元的变换来生成量子纠缠。虽然理论上具有表达力，但这些方法在训练稳定性方面经常表现出问题，并且在泛化能力方面有限。
### Innovation
本文提出了一种名为QiNN-QJ的量子启发式神经网络，用于多模态纠缠建模。QiNN-QJ首先将每个模态编码为一个量子纯净态，然后通过模拟量子跃迁操作符的可微模块将可分的纯态转换为纠缠表示。QiNN-QJ通过学习哈密顿算子和林德布洛姆算子，能够生成具有耗散动力学可控跨模态纠缠，并通过结构化的随机性和稳态吸引子性质来稳定训练和限制纠缠塑造。
### Conclusion
QiNN-QJ在基准数据集CMU-MOSI、CMU-MOSEI和CH-SIMS上优于最新的模型，同时通过冯诺伊曼纠缠熵提供了增强的后见之明的可解释性。这项工作为纠缠多模态融合建立了一个原则性的框架，并为建模复杂的跨模态相关性提供了基于量子启发的方法。
## 76. `cs.AI` - AURA: 一种基于强化学习的AI驱动自适应对话式调查框架 [PDF](https://arxiv.org/pdf/2510.27126), [HTML](https://arxiv.org/abs/2510.27126)
### Authors
Jinwen Tang,Yi Shang
### Background
传统的在线调查缺乏个性化，导致参与度低和浅薄的回应。虽然AI聊天机器人调查提高了便利性，但大多数仍具有反应性：依靠固定的话语树或静态提示模板，无法在会话中适应个体用户，导致通用跟进和弱回应质量。
### Innovation
提出了AURA（Adaptive Understanding through Reinforcement Learning for Assessment）框架，这是一种基于强化学习的AI驱动的自适应对话式调查方法。AURA通过使用LSDE四个维度（长度、自我披露、情绪、具体性）量化回应质量，并通过ε贪婪策略在每次会话内更新预期质量收益来选择后续问题类型。该系统在10-15次对话交换中动态适应个体参与者。实验结果表明，AURA在响应质量上获得了0.12的平均增量，并显著优于不适应基线（p=0.044，d=0.66），通过减少63%的细节提示和增加10倍的验证行为。
### Conclusion
强化学习可以使调查聊天机器人更具适应性，将静态问卷转化为互动的、自我提升的评价系统。
## 77. `cs.AI` - ZEBRA: 向无监督跨被试泛化的通用脑视觉解码迈进 [PDF](https://arxiv.org/pdf/2510.27128), [HTML](https://arxiv.org/abs/2510.27128)
### Authors
Haonan Wang,Jingyu Lu,Hongrui Li,Xiaomeng Li
### Background
近年来，神经解码的最新进展使从脑活动重建视觉体验成为可能，定位fMRI到图像重建为神经科学与计算机视觉之间的桥梁。然而，当前的方法主要依赖于被试特定的模型或需要特定的微调，这限制了它们的可扩展性和实际应用。
### Innovation
本文引入了ZEBRA，这是第一个无监督跨被试泛化的脑视觉解码框架，消除了对被试特定适应的需求。ZEBRA基于关键洞察，即fMRI表示可以分解为与被试相关的和与语义相关的组件。通过利用对抗训练，我们的方法显式地分离这些组件，以隔离被试不变、语义特异性表示。这种分离使ZEBRA能够在无需额外fMRI数据或重新训练的情况下应用于未见过的被试。广泛的实验表明，ZEBRA在几个指标上显著优于无监督基线，并且其性能与完全微调的模型相当。
### Conclusion
我们的工作代表了向通用神经解码的可扩展和实用步骤。代码和模型权重可在以下链接获取：this https URL。
## 78. `cs.AI` - 开放文本到音频模型的表达范围表征 [PDF](https://arxiv.org/pdf/2510.27102), [HTML](https://arxiv.org/abs/2510.27102)
### Authors
Jonathan Morse,Azadeh Naderi,Swen Gaudl,Mark Cartwright,Amy K. Hoover,Mark J. Nelson
### Background
文本到音频模型是一种生成模型，可以根据给定的文字提示生成音频输出。尽管层级生成器及其生成功能内容的属性（如可玩性）占据了程序性生成内容（PCG）讨论的主导地位，但能够与玩家产生情感共鸣的游戏往往将创意和多模态内容（如音乐、声音、视觉和叙述风格）结合起来。多模态模型已经开始在这一目的上进行至少实验性的应用。然而，这些模型究竟生成了什么、以及生成的变异性和精确度仍然是不清楚的：音频是生成系统非常广泛的输出类型之一。在PCG社区中，已使用表达范围分析（ERA）作为量化方式来表征生成器的输出空间，尤其是针对层级生成器。本研究将ERA适应于文本到音频模型，通过分析特定固定提示下的输出表达范围来使分析变得可行。实验使用了来源于Environment Sound Classification（ESC-50）数据集的多个标准化提示，研究生成的音频在关键声学维度（如音高、音量和音色）上的表现。
### Innovation
本文创新地将表达范围分析（ERA）应用于文本到音频模型，通过固定提示下的输出表达范围分析，使得对文本到音频模型的评估变得更加可行。研究使用了ESC-50数据集中的标准化提示，分析了生成音频的关键声学维度，并提供了一种ERA为基础的探索性评估框架，用于生成音频模型。
### Conclusion
本文提出了一种基于ERA的探索性评价框架，用于评估生成音频模型的表达能力。通过使用特定的标准化提示和关键声学维度进行分析，为文本到音频模型提供了一种定量的方法来表征其生成的能力，并为进一步的研究和应用提供了指引。
## 79. `cs.AI` - MARIA：无需真实标签的AI系统边际风险评估框架 [PDF](https://arxiv.org/pdf/2510.27163), [HTML](https://arxiv.org/abs/2510.27163)
### Authors
Jieshan Chen,Suyu Ma,Qinghua Lu,Sung Une Lee,Liming Zhu
### Background
在部署AI系统替代现有程序之前，必须对其进行比较以确保没有增加风险。传统的评估依赖于两个系统的真值，但出于延迟或未知的后果、高昂的成本或数据不完整等原因，真实标签往往不可用，特别是对于那些经过传统安全认定的长期运行系统。更加实际的解决办法是计算系统之间的相对差异而非绝对风险。因此，本文提出了一种边际风险评估框架，避免依赖真实标签或绝对风险，强调了预测性、能力和交互主导性三种相对评估方法。
### Innovation
本文提出了一种边际风险评估框架（MARIA），该框架不依赖于真实标签或绝对风险，重点关注三种相对评估方法：预测性、能力和交互主导性。
### Conclusion
通过从绝对评估转向相对评估，我们的方法为软件团队提供了可操作的指导：识别AI如何增强结果，以及它引入的新风险，并以负责任的方式采用这些系统。
## 80. `cs.AI` - 沿着山谷探索景观以找到更好的极小值 [PDF](https://arxiv.org/pdf/2510.27153), [HTML](https://arxiv.org/abs/2510.27153)
### Authors
Tong Zhao,Jiacheng Li,Yuanchang Zhou,Guangming Tan,Weile Jia
### Background
在深度学习中，找到更低且泛化性能更好的极小值至关重要。然而，现有的许多优化器在找到局部极小值后就停止了搜索，这使得保证找到的极小值是最低的或具有最佳泛化性能变得困难。鉴于损失景观复杂的几何特性，现有方法难以确保找到的点是最低的或提供最佳泛化。
### Innovation
本文提出了一个名为'E'的适配器，用于现有的基于梯度的优化器。适配的优化器倾向于在抵达局部极小值之后继续探索低损失区域（低且几乎相同的损失值区域），以寻找到潜在更佳的局部极小值。这种策略增加了找到更低且更平坦的局部极小值的可能性，而这样的极小值通常与更好的泛化有关。论文还提供了适配优化器在凸和非凸场景下的收敛证明，证明了该方法的有效性。特别是在大规模训练场景中，本文展示了适配的Lamb优化器，称为ALTO，在多种大规模训练任务中平均提高了当前最佳优化器2.5%的测试精度，验证了该方法的有效性。
### Conclusion
本文的工作为优化算法的设计开拓了一个新的研究方向，通过在复杂的损失景观中探索，提高了优化器在大规模训练中的泛化性能。
## 81. `cs.AI` - H2-Cache: 一种用于生成扩散模型高性能加速的新型分层双阶段缓存 [PDF](https://arxiv.org/pdf/2510.27171), [HTML](https://arxiv.org/abs/2510.27171)
### Authors
Mingyu Sung,Il-Min Kim,Sangseok Yun,Jae-Mo Kang
### Background
生成扩散模型在图像生成方面取得了最先进的成果，但由于其迭代去噪过程的巨大计算成本，实际部署受到阻碍。现有的缓存技术可以加快推理速度，但常常在速度和保真度之间造成矛盾，导致质量下降和高计算开销。
### Innovation
我们提出了一种新颖的分层缓存机制H2-Cache，特别适用于现代生成扩散模型架构。H2-Cache通过将去噪过程功能上区分为结构定义阶段和细节精炼阶段，并通过独立的阈值系统选择性地缓存每个阶段来解决上述限制。为了确保双重检查方法的效率，我们引入了一种轻量级的技术——聚合特征总结（PFS），用于快速稳健的相似性估计。
### Conclusion
我们对Flux架构的大量实验表明，H2-Cache可以在加速（最高5.08倍）的同时保持与基线几乎相同的图像质量，从定量和定性上都优于现有的缓存方法。我们的工作提供了一个稳健且实用的解决方案，有效解决了速度和质量之间的矛盾，显著降低了高质量扩散模型在实际应用中的门槛。
## 82. `cs.AI` - 为高分辨率图像生成准确和详细的描述 [PDF](https://arxiv.org/pdf/2510.27164), [HTML](https://arxiv.org/abs/2510.27164)
### Authors
Hankyeol Lee,Gawon Seo,Kyounggyu Lee,Dogun Kim,Kyungwoo Song,Jiyoung Jung
### Background
视觉语言模型（VLMs）在生成高分辨率图像的准确和详细的描述方面存在困难，因为它们通常在较小尺寸的输入（如224x224或336x336像素）上进行预训练。高分辨率图像降尺度到这些尺寸可能导致视觉细节丢失和重要对象的遗漏。现有方法无法捕捉到所有重要信息，导致生成的描述不够准确和详细。
### Innovation
本文提出了一种新颖的管道，将视觉语言模型、大型语言模型（LLMs）和对象检测系统结合起来，以提升描述的质量。该管道通过多阶段过程增强描述。首先使用VLM生成初始描述，然后利用LLM识别图像中的关键对象，并预测与这些对象相关的其他对象。这些预测通过对象检测系统验证，未被初始描述提到的新增对象被进行针对性的区域描述，确保它们被纳入描述中。这种方法增加了描述的详细性，同时减少了虚构信息的出现，避免提及未被检测到的对象。
### Conclusion
在鉴赏数据集上的实验表明，本文提出的方法能够生成更加详尽和可靠的图像描述，同时有效减少了虚构信息。通过成对比较和大型多模态模型的定量评分，以及一款虚构检测基准测试也验证了方法的有效性。
## 83. `cs.AI` - 基于贝叶斯数据调度器的大型语言模型有害微调适应性防御 [PDF](https://arxiv.org/pdf/2510.27172), [HTML](https://arxiv.org/abs/2510.27172)
### Authors
Zixuan Hu,Li Shen,Zhenyi Wang,Yongxian Wei,Dacheng Tao
### Background
有害微调对基于大型语言模型的微调服务构成了严重的安全风险。现有的防御策略通过预先构建鲁棒性的方式应对这些风险，即通过攻击模拟，但存在根本性的局限性：一是难以扩展攻击模拟超出预设的威胁模型，因为预测未知攻击十分困难；二是适应性有限，攻击设置的变化无法被充分捕捉和模拟。
### Innovation
本文提出了一种无需攻击模拟的自适应微调阶段防御策略——贝叶斯数据调度器 (BDS)。BDS 将防御有害微调问题表述为贝叶斯推断问题，学习基于微调和对齐数据集中每个数据点的安全属性的后验分布。通过给数据分配其安全属性的后验样本权重，微调过程得以约束，从而减轻有害数据的影响。进一步地，基于实 avidity 贝叶斯学习的神经调度器增强了其高效性，能够在无需重新训练的情况下向新数据转移。在多种攻击与防御设置下，本文方法展示了最先进的性能。
### Conclusion
通过使用基于贝叶斯推断的后验分布，贝叶斯数据调度器能够针对特定数据集进行调整，从而实现适应性防御。此外，神经调度器使得该方法能够高效地应用于新数据集，无需重新训练。广泛的结果表明，该方法在多种攻击和防御设置下表现出最佳性能。
## 84. `cs.AI` - 跨视角地帜定位(Dual-level Progressive Hardness-Aware Reweighting for Cross-View Geo-Localization) [PDF](https://arxiv.org/pdf/2510.27181), [HTML](https://arxiv.org/abs/2510.27181)
### Authors
Guozheng Zheng,Jian Guan,Mingjie Xie,Xuanjia Zhao,Congyi Fan,Shiheng Zhang,Pengming Feng
### Background
无人机和卫星图像之间的跨视角地理定位（CVGL）仍具挑战性，主要由于视角差距显著以及存在的硬负样本——这些样本视觉相似但地理匹配错误。现有策略通常采用静态加权，这种加权方式对分布转移敏感且容易在优化早期过度强调困难样本，导致梯度噪音及相关训练不稳定。
### Innovation
本文提出了双重层次渐进难度感知重新加权（DPHR）策略。在样本级别，引入基于比率的难度感知（RDA）模块评估相对难度并为负样本分配细粒度权重；在批次级别，采用渐进自适应损失加权（PALW）机制利用训练进度信号在早期优化阶段衰减噪音梯度，并随着训练成熟逐步强化硬负样本挖掘。实验表明，所提出的DPHR方法在University-1652和SUES-200基准上的效果和鲁棒性优于最新方法。
### Conclusion
在University-1652和SUES-200基准上的实验结果证实了所提出的DPHR的有效性和鲁棒性，能够一致地超过现有方法的表现。
## 85. `cs.AI` - FMint-SDE：通过误差校正加速SDE数值模拟的多模态基础模型 [PDF](https://arxiv.org/pdf/2510.27173), [HTML](https://arxiv.org/abs/2510.27173)
### Authors
Jiaxin Yuan,Haizhao Yang,Maria Cameron
### Background
动态系统的快速和准确模拟是科学和工程领域的一项基本挑战。传统数值积分器往往在准确性和计算效率之间存在权衡，现有的基于神经网络的方法通常需要为每个特定场景训练一个独立模型。为克服这些限制，我们引入了一种新型面向大规模微分方程模拟的基础模型：FMint-SDE（基于初始化的多模态基础模型用于随机微分方程）。FMint-SDE基于解码器的变压器结构和即时学习机制，利用数值和文本模态学习一个通用的误差校正方案。模型使用由常规求解器生成的粗糙解决方案序列进行预训练，从而使模型可以跨不同系统进行广泛泛化。我们在涵盖分子动力学、机械系统、金融和生物学等应用的复杂SDE基准测试集上评估了我们的模型。实验结果表明，我们的方法在准确性和效率之间实现了优于经典求解器的权衡，表明FMint-SDE作为动力系统通用模拟工具的潜力巨大
### Innovation
引入了一种新型基于初始化的多模态基础模型FMint-SDE，通过解码器的变压器结构和即时学习机制，结合数值和文本模态来学习一个通用的误差校正方案。它使用由常规求解器生成的粗糙解决方案序列进行预训练，从而实现广泛的泛化能力。相比传统方法，该模型在准确性和效率之间取得了更好的权衡，为动力系统的通用模拟工具提供了新的解决方案
### Conclusion
实验结果表明，我们的方法在准确性和效率之间实现了优于经典求解器的权衡，这表明FMint-SDE作为动力系统通用模拟工具的潜力巨大。
## 86. `cs.AI` - 未验证的信任：大规模语言模型架构中的跨阶段漏洞 [PDF](https://arxiv.org/pdf/2510.27190), [HTML](https://arxiv.org/abs/2510.27190)
### Authors
Dominik Schwarz
### Background
随着大型语言模型（LLMs）越来越多地整合到自动化的多阶段管道中，多阶段处理过程中因未经验证的信任而产生的风险模式成为了实际的关注点。输入往往以非中立的方式被解释，并且在没有明确指令的情况下也可能触发实现特定响应或意外状态变化。本文研究了41种在商业LLMs中反复出现的风险模式，分析表明字符串级别的过滤不足以缓解此类风险，因此推荐采用零信任架构原则，包括追溯性控制、上下文密封和计划重验证，以减轻这种跨阶段的漏洞风险
### Innovation
本文提出了一个机制中心的分类框架，识别出41种在商业LLMs中反复出现的风险模式，并指出这些行为构成架构故障模式。作者强调，单纯的字符串过滤不足以缓解此类风险，因此提出了零信任架构原则，包括追溯性控制、上下文密封和计划重验证；同时引入了“反心智”（Countermind）作为实施这些防御措施的概念蓝图
### Conclusion
为了缓解大规模语言模型架构中的跨阶段漏洞风险，本文建议采用零信任架构原则，并提出“反心智”作为实现这些防御措施的概念蓝图。
## 87. `cs.AI` - 稀疏模型反转：高效反转视觉变换器以实现无数据应用 [PDF](https://arxiv.org/pdf/2510.27186), [HTML](https://arxiv.org/abs/2510.27186)
### Authors
Zixuan Hu,Yongxian Wei,Li Shen,Zhenyi Wang,Lei Li,Chun Yuan,Dacheng Tao
### Background
模型反转旨在从预先训练的判别模型中重建原始训练数据，特别适用于原始训练数据因隐私、使用权限或数据量限制等原因不可用的情况。然而，现有的密集反转方法试图重建整个图像区域，这使得从大规模视觉变换器（如ViTs）中反转高分辨率图像变得极其低效。研究还发现，这种低效性的原因主要有两点：冗余地反转噪声背景和无意中反转的虚假关联，这一现象称为模型反转中的‘幻觉’。
### Innovation
本研究提出了一种新颖的稀疏模型反转策略，可以作为现有的密集反转方法的即插即用扩展，无需修改其原始损失函数即可显著加快反转速度。该方法选择性地反转语义前景并停止噪声背景及潜在虚假关联的反转，通过理论和实验研究验证了该方法在实现显著的反转加速（最高可达3.79倍）的同时保持或增强下游性能的能力，特别是在无数据模型量化和无数据知识传递中的应用。
### Conclusion
我们通过理论和实证研究，验证了该稀疏模型反转方法在显著加速模型反转速度的同时保持并可能增强下游应用的性能。此方法是现有密集反转方法的有效补充，通过简单的调整即可显著提升处理大规模视觉变换器的能力。
## 88. `cs.AI` - Soft Task-Aware Routing of Experts for Equivariant Representation Learning [PDF](https://arxiv.org/pdf/2510.27222), [HTML](https://arxiv.org/abs/2510.27222)
### Authors
Jaebyeong Jeon,Hyeonseo Jang,Jy-yong Sohn,Kibok Lee
### Background
现有的研究显示，在下游任务中同时学习不变性表示和对称性表示通常是有益的，方法是使用单独的投影头。然而，这种设计忽略了不变性学习和对称性学习之间共享的信息，导致了冗余的特征学习和模型容量的低效利用。
### Innovation
提出了Soft Task-Aware Routing (STAR) 策略，将其视为专家路由机制。STAR促使专家专注于捕捉共享或特定于任务的信息，从而减少了冗余的特征学习。通过观测不变性嵌入和对称性嵌入之间的陈规定律相关性降低，验证了这种效果。
### Conclusion
实验结果表明，这种方法在不同的迁移学习任务中一致提高了表现。代码可以在该链接下载：this https URL
## 89. `cs.AI` - 通过层次图神经网络进行传统村庄空间形态多模态特征融合分析 [PDF](https://arxiv.org/pdf/2510.27208), [HTML](https://arxiv.org/abs/2510.27208)
### Authors
Jiaxin Zhang,Zehong Zhu,Junye Deng,Yunqin Li,and Bowen Wang
### Background
村庄地区的研究对理解人地关系至关重要。然而，随着城市化的推进，村庄的地理特征逐渐消失，景观出现同质化趋势。现有研究多从单一学科角度出发，采用定性分析方法来研究村庄的空间形态及其影响因素，这些研究受限于缺乏数字基础设施和数据不足。因此，本文提出了一种层次图神经网络（HGNN）模型，该模型整合多源数据以深入分析村庄的空间形态。
### Innovation
本文提出了层次图神经网络（HGNN）模型，结合图卷积网络（GCN）和图注意网络（GAT），在两阶段特征更新机制下高效地整合多模态特征。通过引入关系池化机制和联合训练策略，该方法在多模态融合和分类任务中实现了显著性能提升。
### Conclusion
实验结果表明，该方法在多模态融合和分类任务中的性能优于现有方法，在所有子类型的联合优化下，平均准确度和F1值分别从0.71/0.83提高到0.82/0.90，特别是在地块任务上提高了6%。该方法为探索村庄空间模式和生成逻辑提供了科学依据。
## 90. `cs.AI` - 隐私保护的多窗位胸部CT连续自我监督学习以实现域迁移鲁棒性 [PDF](https://arxiv.org/pdf/2510.27213), [HTML](https://arxiv.org/abs/2510.27213)
### Authors
Ren Tasai,Guang Li,Ren Togo,Takahiro Ogawa,Kenji Hirata,Minghui Tang,Takaaki Yoshimura,Hiroyuki Sugimori,Noriko Nishioka,Yukie Shimizu,Kohsuke Kudo,Miki Haseyama
### Background
在医学图像诊断中建立稳健且高度通用的模型具有挑战性，主要原因是大规模准确注释的数据集稀缺以及动态医疗服务环境下固有的领域变化。具体来说，在胸部CT中，这些领域变化通常源自不同窗位设置的差异，这些窗位设置是为了满足不同的临床目的而优化的。现有的自我监督学习（SSL）框架通常通过重新使用过去的数据来缓解领域变化，然而这种方法由于隐私限制通常不太实际。
### Innovation
本文提出了一种新颖的连续自我监督学习（CSSL）框架，用于同时从多窗位获得的胸部CT图像中学习多样特征，确保数据隐私。通过连续前向训练在未标记图像上捕捉之前学习的知识与新信息之间的关系，本文方法利用潜在重放机制缓解了连续前向训练期间由于领域变化导致的灾难性遗忘，同时确保数据隐私。此外，本文还提出了一种特征蒸馏技术，该技术结合了基于Wasserstein距离的知识蒸馏（WKD）和批次知识联合（BKE），增强模型学习有意义且面对领域变化具有鲁棒性表示的能力。
### Conclusion
本文通过在两个不同窗位获得的胸部CT图像上验证了这种方法，与其它方法相比，表现出更好的性能。
## 91. `cs.AI` - MemeArena: 自动化多元语境下无偏见的有害性理解评估框架 [PDF](https://arxiv.org/pdf/2510.27196), [HTML](https://arxiv.org/abs/2510.27196)
### Authors
Zixin Chen,Hongzhan Lin,Kaixin Li,Ziyang Luo,Yayue Deng,Jing Ma
### Background
社交媒体平台上的 meme 越发普及，要求多模态大型语言模型（mLLMs）具备有效的理解多模态有害性的能力。现有的评估方法主要集中在 mLLMs 对二元分类任务的检测准确度上，但往往无法体现不同背景下有害性的深层次阐释差异。因此，需要一种能够提供上下文意识和无偏见评估的框架，以便更好地理解和评估 mLLMs 的多模态有害性理解能力。
### Innovation
本文提出 MemeArena，一种基于代理的三维评估框架，它能够提供上下文感知和无偏见评估，并为 mLLMs 的多模态有害性理解能力提供分析任务。MemeArena 通过模拟多元阐释背景，促使 mLLMs 进行视角特定的分析，并通过整合多种视角和达成评估者共识来实现公平、无偏见的比较。该框架的有效性通过大量实验得到验证，其评价结果与人类偏好高度一致，提供了关于 mLLMs 多模态有害性理解的可靠和全面评估的宝贵见解。
### Conclusion
我们的框架有效减少了裁判代理的评价偏见，判断结果紧密符合人类偏好，提供了有关 mLLMs 多模态有害性理解的可靠和全面评估的有价值见解。我们的代码和数据可在如下网址公开访问：this https URL.
## 92. `cs.AI` - DRAMA: 统一开放域数据分析查询中的数据获取与分析 [PDF](https://arxiv.org/pdf/2510.27238), [HTML](https://arxiv.org/abs/2510.27238)
### Authors
Chuxuan Hu,Maxwell Yang,James Weiland,Yeji Lim,Suhas Palawala,Daniel Kang
### Background
手动进行现实世界的数据分析既耗费人力又低效。尽管尝试了许多自动化数据科学工作流的方法，现有的范例或系统均未能全面展示支持它们的三个关键能力：开放域数据采集、结构化数据转换以及分析推理。为了克服这些局限，本文提出了一个端到端的范例DRAMA，它以自然语言响应用户的大规模开放域数据分析查询。DRAMA将数据采集、转换和分析作为一个单一的工作流整体处理。为评估DRAMA在仿真实例中的性能，构建了一个基准DRAMA-Bench，包括验证声明和问题回答两类任务，每类包含100个实例。这些任务来源于已获得广泛社会关注的现实应用，需要检索和分析开放域数据。
### Innovation
DRAMA 是一个端到端的范例，实现了将数据采集、转换和分析统一在一个工作流中。开发了一个多代理系统 DRAMA-Bot，能够高效地进行数据检索和分析，且成本效益显著。DRAMA-Bot 在DRAMA-Bench 上的表现优于五个最先进的基线系统，任务准确率高达86.5%，成本仅为基线系统的1/6，准确率提高6.9倍。
### Conclusion
DRAMA 提供了一个统一的框架，能够自动处理开放域数据，并展示了高效的性能。DRAMA 已经开放给公众使用。
## 93. `cs.AI` - 从与语音相关的生物信号重构前所未见的句子以实现开放词汇神经通信 [PDF](https://arxiv.org/pdf/2510.27247), [HTML](https://arxiv.org/abs/2510.27247)
### Authors
Deok-Seon Kim,Seo-Hyun Lee,Kang Yin,Seong-Whan Lee
### Background
脑-语音（BTS）系统是一种革命性的交流方式，通过直接将神经活动转化为语言表达而实现。最近的研究大多集中在解码预定义的单词或句子上，但为了实现类似自然人类交流的开放词汇神经通信，必须能够解码非限定性口语。此外，有效整合来自不同语音模式的多样信号对于开发个性化和适应性强的神经通信和康复解决方案至关重要。
### Innovation
本研究通过利用高密度脑电图（EEG）信号中的音素级信息（单独或与肌电图（EMG）信号结合），探索用于重建未见过的句子的语音合成的潜力，特别是在不同语音模式下。此外，研究考察了句子重建期间影响音素解码准确性的属性，并提供了神经生理学见解，以进一步增强EEG解码，从而提供更有效的神经通信解决方案。
### Conclusion
研究结果证明了基于生物信号的句子级语音合成的可行性，可以用于重建未见过的句子，迈出了一步实现适应不同患者需求和条件的开放词汇神经通信系统。此外，本研究为利用EEG解码技术开发通信和康复解决方案提供了有价值的见解。
## 94. `cs.AI` - 特征-函数曲率分析：解释可微模型的几何框架 [PDF](https://arxiv.org/pdf/2510.27207), [HTML](https://arxiv.org/abs/2510.27207)
### Authors
Hamed Najafi,Dongsheng Luo,Jason Liu
### Background
解释性人工智能(XAI)对于建立复杂机器学习模型的信任至关重要。然而，主流的归因方法往往只提供模型最终状态的不完整、静态图景。通过将特征的作用简化为单一分数，这些方法会受到非线性和交互性的影响，陷入困境。针对这一问题，本文提出了一种新的方法叫做特征-函数曲率分析(FFCA)，该方法从几何学角度分析了模型学习到的函数。FFCA为每个特征生成了一个4维签名，量化了其(1)影响，(2)波动性，(3)非线性和(4)交互性。更重要的是，本文将该框架扩展到了动态典范分析，通过该方法可以在训练过程中跟踪这些签名的演变。这种时间视角不仅解释了模型学到了什么，还揭示了它是如何学习的。FFCA提供了首次直接、经验性证据，证明了层次化学习的现象，即模型在学习复杂交互之前会先学习简单的线性效应。此外，这种动态分析还提供了新颖和实用的诊断工具，用于识别模型能力不足，并预测过拟合的发生。
### Innovation
本文提出了一种新的框架——特征-函数曲率分析(FFCA)。该方法从几何学角度分析了模型学习到的函数，并且为每个特征生成了一个4维签名，量化了其影响、波动性、非线性和交互性。此外，本文将该框架扩展到了动态典范分析，对学过的特征随训练过程的变化进行了跟踪。这种动态分析提供了第一次直接的经验性证据，证明了层次化学习的现象，揭示了模型是如何学习的，同时也提供了一些实用的诊断工具，用于识别模型能力不足和预测过拟合的发生。
### Conclusion
FFCA，凭借其静态和动态组件，提供了关键的几何上下文，将模型解释从简单的量化转变为了对整个学习过程的准确、可信赖的分析。通过对不同的模型进行全面实验，本文证明了FFCA的重要性。
## 95. `cs.AI` - 更高阶的线性注意力 [PDF](https://arxiv.org/pdf/2510.27258), [HTML](https://arxiv.org/abs/2510.27258)
### Authors
Yifan Zhang,Zhen Qin,Quanquan Gu
### Background
自回归语言模型在长上下文场景下的扩展受到阶乘时间复杂的点积注意力成本的限制。线性时间注意力和状态空间模型（SSMs）提供了一种可扩展的替代方案，但它们通常仅限于一阶或基于核的近似，这可能会限制其表达能力。
### Innovation
论文引入了一种因果性更高阶线性注意力（Higher-order Linear Attention, HLA），这是一种紧凑的前缀充分统计数据驱动的机制，用于实现更复杂的交互作用。在二阶情况下，HLA能够维持固定的大小状态并在线计算每个单词的输出，无需形成任何n×n矩阵。此外，论文还给出了闭合形式的在线身份、一种严格因果性的掩蔽变体、以及基于结合扫描的分区并行训练方案，该方案可以精确再现串行循环激活。
### Conclusion
这些结果共同将HLA定位为一种原理性的、可扩展的基础组件，它结合了类似注意力的数据依赖性混合和现代递归架构的效率。
## 96. `cs.AI` - 非所有实例具有同等价值：迈向影响加权数据集蒸馏 [PDF](https://arxiv.org/pdf/2510.27253), [HTML](https://arxiv.org/abs/2510.27253)
### Authors
Qiyan Deng,Changqian Zheng,Lianpeng Qiao,Yuping Wang,Chengliang Chai,Lei Cao
### Background
数据集蒸馏可以将大型数据集压缩成合成子集，同时保持与在完整数据集上训练相当的性能，但大幅减少存储和计算成本。现有数据集蒸馏方法通常假定所有真实实例对过程的贡献是相等的。然而，实际数据集中包含具有信息价值、冗余甚至有害的实例，若不考虑数据质量，直接从完整数据集中蒸馏可能会降低模型性能。
### Innovation
提出了一个称为影响加权蒸馏(IWD)的框架，该框架利用影响函数明确地在蒸馏过程中考虑数据质量。IWD根据每个实例对蒸馏目标的估计影响为其分配自适应权重，从而优先考虑有帮助的数据，并降低无用或有害数据的权重。由于其模块化设计，IWD可以无缝集成到各种数据集蒸馏框架中。
### Conclusion
实验证明，将IWD整合到数据集蒸馏过程中，通常可以提高蒸馏数据集的质量，增强模型性能，最高可增加7.8%的准确率。
## 97. `cs.AI` - MedCalc-Eval和MedCalc-Env：提高大型语言模型在医学计算能力 [PDF](https://arxiv.org/pdf/2510.27267), [HTML](https://arxiv.org/abs/2510.27267)
### Authors
Kangkun Mao,Jinru Ding,Jiayuan Chen,Mouxiao Bian,Ruiyao Chen,Xinwei Peng,Sijie Ren,Linyang Li,Jie Xu
### Background
当前大多数基准测试主要评估大型语言模型（LLMs）在医学领域的问答和描述性推理能力，而忽视了临床决策中至关重要的定量推理。现有的数据集如MedCalc-Bench覆盖的计算任务有限，未能反映实际的计算场景。为了解决这些问题，引入了MedCalc-Eval，作为评估LLMs在医学计算能力的最大基准，包括700多个跨内部医学、外科、儿科和心脏病学等专科的任务。
### Innovation
MedCalc-Eval 基准涵盖了两种类型的医学计算任务：基于公式的（如Cockcroft-Gault、BMI、BSA）和基于规则的评分系统（如Apgar、Glasgow昏迷量表）。此外，还开发了MedCalc-Env，这是在InternBootcamp框架上构建的强化学习环境，用于多步骤的临床推理和规划。通过在这种环境中对Qwen2.5-32B模型进行微调，取得了MedCalc-Eval上的最先进的结果。剩余的挑战包括单位转换、多条件逻辑和情景理解。
### Conclusion
MedCalc-Eval 和MedCalc-Env 为评估和改善 LLMs 的医学计算能力提供了重要的框架和基准。
## 98. `cs.AI` - 为什么推理语言模型中会出现多语言推理差距？ [PDF](https://arxiv.org/pdf/2510.27269), [HTML](https://arxiv.org/abs/2510.27269)
### Authors
Deokhyung Kang,Seonjeong Hwang,Daehui Kim,Hyounghun Kim,Gary Geunbae Lee
### Background
推理语言模型（RLMs）在复杂的推理任务上表现出色，但它们仍然在处理多语言输入时存在差距，高低资源语料库之间的性能差异显著。尽管最近的努力已经缩小了这一差距，但其根本原因仍不明确。本文探讨了多语言推理差距的主要来源是模型在推理过程中理解多语言输入的能力不足。模型不能将输入语言的意义转换为主导语言（如英语）进行推理，这导致了多语言推理差距的产生。基于此，研究者提出了一个名为‘选择性翻译’的策略，该策略仅在检测到理解错误时将多语言输入翻译为英语以进行推理。实验结果证明，这种方法可以有效减少多语言推理差距，以不到20%的翻译量实现了接近完全翻译的效果。总之，本文揭示了理解错误是造成多语言推理差距的主要原因，并可以被检测和部分减轻，提供了一个新的方向以实现更公平的多语言推理能力。
### Innovation
本文发现多语言推理差距的主要原因是模型在处理多语言输入时的理解能力不足，并开发了‘选择性翻译’策略，该策略根据理解错误与否决定是否进行翻译，从而有效缩小了多语言推理差距。这种方法仅需大约20%的翻译量就能接近完全翻译的效果，展示了显著的创新性。此外，‘选择性翻译’提供了一个可以减轻多语言推理差距的有效策略。
### Conclusion
我们的工作表明，理解错误是多语言推理差距的主要原因，并且这种错误可以被检测并选择性地减轻，为更公平的多语言推理提供重要的见解。我们提供的代码和数据可在该网址获取。
## 99. `cs.AI` - HiF-DTA：用于药物-靶点亲和力预测的分层特征学习网络 [PDF](https://arxiv.org/pdf/2510.27281), [HTML](https://arxiv.org/abs/2510.27281)
### Authors
Minghui Li,Yuanhang Wang,Peijin Guo,Wei Wan,Shengshan Hu,Shengqing Hu
### Background
药物-靶点亲和力（Drug-Target Affinity, DTA）的准确预测对于减少实验成本并加速计算药物发现中的早期筛选至关重要。基于序列的深度学习方法虽然避免了对昂贵的3D结构的依赖，但仍未能同时建模药物和蛋白质中的全局序列语义特征和局部拓扑结构特征，并且将药物表示为平坦序列，缺少原子级、亚结构级和分子级的多尺度特征。
### Innovation
本文提出了HiF-DTA，一种分层网络，采用双路径策略从药物和蛋白质序列中提取全局序列语义特征和局部拓扑特征，并通过多尺度双线性注意力模块学习药物的多尺度表示。在Davis、KIBA和Metz数据集上的实验表明，HiF-DTA优于最先进的基线方法，且消融实验确认了全局-局部提取和多尺度融合的重要性。
### Conclusion
HiF-DTA在药物-靶点亲和力预测中表现出色，通过结合全局-局部特征和多尺度表征学习，显著提高了预测准确性，为药物发现提供了有效工具。
## 100. `cs.AI` - LLM在工作中的帮助能力：企业环境中的评估沙盒 [PDF](https://arxiv.org/pdf/2510.27287), [HTML](https://arxiv.org/abs/2510.27287)
### Authors
Harsh Vishwakarma,Ankush Agarwal,Ojas Patil,Chaitanya Devaguptapu,Mahesh Chandran
### Background
企业系统对于提高员工和客户的工作效率和决策能力至关重要。将基于LLM的系统集成到企业系统中可以实现智能化自动化、个性化体验和高效的信息检索，从而推动运营效率和战略增长。然而，开发和评估这种系统具有挑战性，因为企业环境中的数据分散在多个来源中，并受复杂的访问控制管理。本文提出了一个全面的基准测试，名为EnterpriseBench，它模拟了企业环境，覆盖了软件工程、人力资源、财务和行政管理等多个领域。该基准测试独特地捕捉了关键的企业特征，如数据源碎片化、访问控制层级结构和跨功能性的工作流程。此外，还提供了一个新的数据生成管道，从组织元数据中创建内部一致的企业任务。
### Innovation
文章提出了EnterpriseBench，这是一种模拟企业环境的基准测试，包含500种不同任务，覆盖了软件工程、人力资源、财务和行政管理等多个领域，捕捉了数据源碎片化、访问控制层级结构和跨功能性的工作流程等特点。同时，提供了一种新的数据生成管道，可以从组织元数据中创建内部一致的企业任务。实验表明，最先进的LLM代理只能完成41.8%的任务，强调了在企业关注的人工智能系统方面有巨大的改进空间。
### Conclusion
本文展示了EnterpriseBench的基准测试，发现最先进的LLM代理在企业环境中只能完成41.8%的任务，表明在企业环境中的AI系统还有很大的改进空间。研究结果表明，需要进一步研究和开发能够更好地适应复杂企业环境的AI系统。
## 101. `cs.AI` - FOCUS: 长视频理解中的高效关键帧选择 [PDF](https://arxiv.org/pdf/2510.27280), [HTML](https://arxiv.org/abs/2510.27280)
### Authors
Zirui Zhu,Hailun Xu,Yang Luo,Yong Liu,Kanchan Sarkar,Zhenheng Yang,Yang You
### Background
目前的多模态大型语言模型（MLLMs）将图像和视频帧表示为视觉标记。然而，从单个图像扩展到数小时的视频会极大地增加标记预算，超出实际限制。因此，常用的处理方法要么均匀地降采样，要么使用基于检索的评分进行关键帧选择，并使用较小的视觉-语言模型。这些关键帧选择方法仍然依赖于预筛选步骤以减少推理成本，但可能会错过最具信息性的时刻。当前方案尽管在一定程度上解决了数据量的问题，但是存在效率和信息获取完整性的不均等问题，无法有效处理长视频。因此，需要一种高效、准确的关键帧选择方法，以降低处理成本同时保证信息完整性和准确度的平衡。
### Innovation
本文提出了一种名为FOCUS（Frame-Optimistic Confidence Upper-bound Selection）的关键帧选择模块，该模块在不进行训练和与特定模型无关的情况下，能够在严格的标记预算内选择与查询相关的关键帧。该方法将时间短的连续片段视为arm，并利用经验平均值和Bernstein置信半径来定位信息丰富的区域，同时保持不确定性区域的探索。FOCUS采用两阶段探索利用策略，首先识别具有高价值的时间区域，然后选择每个区域得分最高的关键帧。通过这种方式，FOCUS在两个长视频问答基准上实现了显著的准确性提升，处理的视频帧不到2%，对于超过20分钟的长视频，FOCUS还在LongVideoBench上实现了11.9%的准确率提升，证明了其作为关键帧选择方法的有效性，并为大规模长视频理解提供了简单的一般解决方案。
### Conclusion
该研究表明，FOCUS能够高效地选择关键帧，大幅提升了长视频理解的准确性，在处理长视频时，只需要处理不到2%的帧，并且能够维持较高水平的信息完整性和准确性。此外，这种方法对于多模态大型语言模型的长视频理解问题具有普适性，是有效且可行的解决方案。
## 102. `cs.AI` - CASR-Net: 线性冠状动脉造影图像处理为重点的基于深度学习的冠状动脉分割和细化网络 [PDF](https://arxiv.org/pdf/2510.27315), [HTML](https://arxiv.org/abs/2510.27315)
### Authors
Alvee Hassan,Rusab Sarmun,Muhammad E. H. Chowdhury,M. Murugappan,Md. Sakib Abrar Hossain,Sakib Mahmud,Abdulrahman Alqahtani,Sohaib Bassam Zoghoul,Amith Khandakar,Susu M. Zughaier,Somaya Al-Maadeed,Anwarul Hasan
### Background
早期检测冠状动脉疾病(CAD)对降低死亡率和改善患者治疗计划至关重要。尽管X射线血管造影图像分析是一种常见且成本较低的方法，用于识别心脏异常，包括狭窄的冠状动脉，但图像质量差会显著妨碍临床诊断。
### Innovation
我们提出了冠状动脉分割和细化网络(CASR-Net)，这是一个包括图像预处理、分割和细化三层流水线。我们提出了一种新颖的多通道预处理策略，结合了CLAHE和改进后的Ben Graham方法，实现了分割性能的增量提升。其核心创新在于基于UNet的分割网络，具有DenseNet121编码器和基于Self-organized Operational Neural Network (Self-ONN)的解码器，该网络能够保持狭窄和狭窄血管分支的连续性。最终的轮廓细化模块进一步抑制了假阳性。
### Conclusion
CASR-Net在包含健康和狭窄动脉的两个公共数据集上的5折交叉验证中优于几种最先进的模型，实现了IoU为61.43%、Dice Score Coefficient (DSC)为76.10%和clDice为79.36%。这些结果突显了自动冠状动脉分割的稳健方法，并为支持临床诊断和治疗规划提供了有价值的工具。
## 103. `cs.AI` - 基于LoRA和Wan2.1 I2V的小数据视频生成器微调方法与电影场景合成：一种小数据管道 [PDF](https://arxiv.org/pdf/2510.27364), [HTML](https://arxiv.org/abs/2510.27364)
### Authors
Meftun Akarsu,Kerem Catay,Sedat Bin Vedat,Enes Kutay Yarkan,Ilke Senturk,Arda Sar,Dafne Eksioglu
### Background
文章介绍了一个实用的流水线，用于从少量数据中微调开源视频扩散变换器，以合成适用于电视和电影制作的电影场景。现有的方法通常需要大量的数据，但本文提出的方法可以使用小型数据集高效地进行微调。
### Innovation
提出了一个两阶段过程，将视觉风格学习与运动生成分离。第一阶段利用LoRA模块对Wan2.1 I2V-14B模型的交叉注意力层进行微调，使其能够使用来自Ay Yapim历史电视剧《El Turco》的短视频片段数据集快速适应视觉表示。第二阶段通过生成具有风格一致性、保留服装、光线和色彩校正的关键帧来实现这一点，然后通过模型的视频解码器将这些关键帧扩展为720p的连贯序列。此外，还应用了轻量级并行化和序列分割策略以加速推理，而不降低质量。
### Conclusion
定量和定性的评估结果表明，与基础模型相比，在视觉保真度和时间稳定性方面有明显的改进。该完整的训练和推理流水线被开源以支持可重复性和跨影视领域的适应。
## 104. `cs.AI` - 通过忠实性和冗余性衡量链式思维监控能力 [PDF](https://arxiv.org/pdf/2510.27378), [HTML](https://arxiv.org/abs/2510.27378)
### Authors
Austin Meek,Eitan Sprejer,Iván Arcuschin,Austin J. Brockmeier,Steven Basart
### Background
链式的思维输出（CoT）能够反映模型的逐步推理过程。任何长时间的、线性的推理过程都必须依赖这个文本痕迹，因此CoT的质量是直接反映模型所思考内容的窗口。这种透明性可以帮助我们识别模型潜在的不安全或不一致行为（监控能力），前提是CoT需要忠实于其内部推理过程（准确性）。研究人员经常关注模型在添加提示后改变答案的实例来衡量准确性，但这并不能全面反映所有推理过程。我们引入了一个新的概念：是否在CoT中列出了完成任务所需的所有因素（冗余性），将其与准确性结合起来，以评估模型作为外部‘工作记忆’的能力，这对基于CoT监控的许多安全方案至关重要。我们对指令调整和推理模型在BBH、GPQA和MMLU上的表现进行了评估。结果显示，即使模型看似忠实于其内在推理过程，但如果忽略了关键因素，仍难以进行监控，此外，不同模型家族之间的监控能力存在显著差异。我们还提供了一个开源的评估代码，使用Inspect库来支持未来研究的可重复性。
### Innovation
在传统的准确性基础上，引入冗余性的概念，组成一个新的监控能力评估标准。这个新的标准能够更全面地评估CoT作为模型外部‘工作记忆’的质量，这对基于CoT监控的各种安全方案至关重要。提供了可重复使用的评估代码，便于未来研究的进一步发展。
### Conclusion
模型可能在表面上显示得足够诚实，但如果忽略了完成任务所需的关键因素，则仍然难以监控。监控能力在不同的模型家族之间存在显著差异。已经提出了一种新的综合评估标准，将其发布为开源代码，以支持未来的可重复研究。
## 105. `cs.AI` - 无法归因性：从检索和语义相似性计算新颖性 [PDF](https://arxiv.org/pdf/2510.27313), [HTML](https://arxiv.org/abs/2510.27313)
### Authors
Philipp Davydov,Ameya Prabhu,Matthias Bethge,Elisa Nguyen,Seong Joon Oh
### Background
研究语言模型输出与预训练语料库的关系是理解模型行为的关键。大多数已有训练数据归因（TDA）方法关注的是哪些训练示例因果地影响了给定的输出，通常使用移除一个样本进行测试。本文则倒过来问：哪些输出不能被归因到任何预训练示例？这引出了未归因性作为一个操作性度量语义新颖性的概念：如果预训练语料中没有与之语义相似的上下文，那么输出就是新颖的。为此，作者提出了一个简单的两阶段检索管道：首先使用轻量级GIST嵌入索引语料库，然后检索最相关的候选者，并用ColBERTv2重新排名。如果最近的库项目在归因方面不如一个人工生成的文本参考，那么我们认为模型的输出是新颖的。作者在SmolLM和SmolLM2上进行了评估，报告了三条发现：（1）模型跨更长跨度使用预训练数据；（2）某些领域系统地促进了或抑制了新颖性；（3）指令微调不仅改变风格，还增加了新颖性。通过重新定义新颖性的评估框架为未归因性，这项工作使对大规模预训练进行高效分析成为可能。作者还发布了约20TB的语料库片段和索引文件以支持复制和大规模扩展分析工作。
### Innovation
本文提出了一个新的概念，即“未归因性”作为衡量语言模型输出语义新颖性的方法。通过构建一个简单的两阶段检索管道，结合轻量级GIST嵌入和ColBERTv2重新排名，作者提出了一个新颖的方式来评估语言模型的输出是否真正创新且不依赖于预训练数据。这种方法不仅能够理解模型如何利用预训练数据，还能揭示哪些领域更倾向于产生新颖的输出，并且揭示了指令微调如何不仅改变生成内容的风格还增加了其新颖性。这一工作对于理解大规模语料库训练的语言模型行为提供了新的视角，为其他研究提供了高效可靠的分析工具。
### Conclusion
本文通过重新定义新颖性的评估框架为未归因性，为大规模预训练模型的行为研究提供了新的工具和方法。通过对SmolLM和SmolLM2的数据分析，作者发现模型跨更长跨度使用预训练数据，有些领域系统地促进了或抑制了新颖性，指令微调不仅改变了生成内容的风格还增加了其新颖性。作者希望这些发现能推动对语言模型行为的研究，同时所发布的语料库片段和索引文件也为其他学者提供了方便。
## 106. `cs.AI` - 脉冲神经网络：脑启发计算的未来 [PDF](https://arxiv.org/pdf/2510.27379), [HTML](https://arxiv.org/abs/2510.27379)
### Authors
Sales G. Aribe Jr
### Background
脉冲神经网络（SNNs）代表了最新的神经计算技术，提供了一种基于大脑启发的替代传统人工神经网络（ANNs）的方法。与依赖连续信号的ANNs不同，SNNs通过单独的脉冲事件运行，使其更具有能量效率和时间动态性。本文对该领域的设计模型、训练算法以及多维度性能指标进行了全面分析，包括准确性、能耗、延迟、脉冲计数和收敛行为。研究深入探讨了Leaky Integrate-and-Fire（LIF）神经元模型和各种训练策略，如替代梯度下降、ANN到SNN的转换和突触定时依赖可塑性（STDP）。结果显示，经过替代梯度下降训练的SNNs与ANNs的准确性接近，收敛速度较快，延迟低至10毫秒。转换后的SNNs性能也具有竞争力，但需要更高的脉冲计数和更长的模拟窗口。基于STDP的SNNs虽然收敛速度较慢，但具有最低的脉冲计数和能耗，适合无监督和低功耗任务。这些发现表明，SNNs在能量限制、延迟敏感和自适应应用如机器人技术、神经形态视觉和边缘AI系统中的适用性。然而，硬件标准化和扩展性训练方面的挑战依然存在。
### Innovation
研究展示了SNNs的不同设计模型、训练算法及其多维度性能指标。特别是通过替代梯度下降训练的SNNs在准确性、能耗和收敛速度方面接近ANNs。STDP基的SNNs具有最低的能耗和脉冲计数，适合无监督和低功耗任务。此外，研究还详细探讨了LIF神经元模型和多种训练策略，如替代梯度下降、ANN到SNN的转换和STDP。这些工作为SNNs在机器人技术、神经形态视觉和边缘AI系统等应用领域中的进一步发展提供了依据，强调了SNNs在这些特定领域的潜力和优势。
### Conclusion
尽管SNNs在未来神经形态计算中具有巨大潜力，但在硬件标准化和扩展性训练方面仍存在挑战。未来，通过进一步改进，SNNs有望推动神经形态计算进入下一个发展阶段。
## 107. `cs.AI` - Atlas-Alignment：在语言模型间使可解释性可转移 [PDF](https://arxiv.org/pdf/2510.27413), [HTML](https://arxiv.org/abs/2510.27413)
### Authors
Bruno Puri,Jim Berend,Sebastian Lapuschkin,Wojciech Samek
### Background
构建安全、可靠和可控的语言模型时，可解释性至关重要，但现有可解释性管道仍然代价高昂且难以扩展。解释一种新模型通常需要对特定模型进行耗时的稀疏自编码器训练、手动或半自动标记SAE组件以及后续验证。这需要大量成本和复杂的工作。因此，提高模型可解释性的方法仍然是一个挑战。
### Innovation
引入Atlas-Alignment框架，通过将未知的潜在空间对齐到一个概念图谱（已标记，人类可解释的潜在空间）来实现模型间可解释性的转移，仅使用共享输入和轻量级表示对齐技术。这使得以前透明度不足的模型能够实现在具有人类可解释图谱概念的语义特征搜索与检索以及沿图谱概念引导生成的两个关键功能。研究表明，简单的表示对齐方法可以帮助实现稳健的语义检索和可引导生成，而无需标记的概念数据。这表明，通过投资于高质量的概念图谱，可以以最低的边际成本使许多新模型变得透明和可控。
### Conclusion
Atlas-Alignment框架通过一次高质量的概念图谱投资，使得许多新模型在极低成本下变得透明和可控，从而解决了现有可解释性管道的成本高和难以扩展的问题。
## 108. `cs.AI` - 谁会失败在您的算法中？MAMA-MIA数据集中年龄和族裔偏见的调查 [PDF](https://arxiv.org/pdf/2510.27421), [HTML](https://arxiv.org/abs/2510.27421)
### Authors
Aditya Parikh,Sneha Das,Aasa Feragen
### Background
深度学习模型旨在改进诊断工作流程，但在图像分割等分类之外的公平性评估方面仍然未得到充分探索。未解决的分割偏差可能导致某些人群在护理质量上的差异，这种差距可能在临床决策点上进一步扩大，并在迭代模型开发中被放大。我们审计了乳腺癌肿瘤分割数据集MAMA-MIA中自动分割标签的公平性，并评估了不同年龄、族裔和数据来源的自动分割质量。
### Innovation
研究揭示了年龄相关的内在偏见，即使在控制混杂因素（如数据来源）后仍存在。假定这种偏见与生理因素有关，这是我们分析的一个关键点。此外，研究表明，从多个数据源聚合数据会影响特定站点的族裔偏见，强调了需要在细粒度级别上调查数据的重要性。
### Conclusion
我们的研究突显了在细粒度层面上审查数据和检测数据集中的偏见的重要性，尤其是年龄和族裔方面的偏见。这些发现强调了对自动化医疗成像处理的公平性进行持续监测和改进的必要性。
## 109. `cs.AI` - 在部分相关视频检索中缓解语义塌陷 [PDF](https://arxiv.org/pdf/2510.27432), [HTML](https://arxiv.org/abs/2510.27432)
### Authors
WonJun Moon,MinSeok Jung,Gilhan Park,Tae-Young Kim,Cheol-Ho Cho,Woojin Jun,Jae-Pil Heo
### Background
现有的部分相关视频检索（PRVR）方法将每一对标注的文本-视频视为正样本，其余的视为负样本，这样的处理方式忽略了视频内部及不同视频之间的丰富语义变化。这导致不同事件的视频片段嵌入向量坍塌在一起，而来自不同视频但语义相似的查询和片段则被分离，从而限制了对包含多个多样事件的视频的检索性能。
### Innovation
本文提出了一种新的框架来解决这个问题，称为语义塌陷。首先引入了文本相关性保持学习，以保持基础模型中编码的语义关系。为了解决视频嵌入坍塌的问题，提出了跨分支视频对齐（CBVA）方法，这是一种对比对齐方法，可以解耦跨时间尺度的视频表示。此外，引入了有序标记合并和自适应CBVA，以增强对齐，从而生成内部一致但又互不相同的视频片段。
### Conclusion
大量的实验结果表明，本文提出的框架有效地防止了语义塌陷，并大幅提高了检索准确性。
## 110. `cs.AI` - CoMViT：低资源医学成像监督分类中的高效视觉主干 [PDF](https://arxiv.org/pdf/2510.27442), [HTML](https://arxiv.org/abs/2510.27442)
### Authors
Aon Safdar,Mohamed Saadeldin
### Background
视觉变换器（ViTs）在医学成像领域展现了强大的潜力；然而，它们的高计算需求和对小型数据集的过度拟合倾向限制了其在实际临床场景中的应用。在小型数据集上训练模型时，传统ViTs容易过拟合，且计算复杂度高，这限制了它们在资源受限的医学成像分析中的应用。
### Innovation
本文介绍了针对资源受限的医学图像分析优化设计的紧凑且通用的视觉变换器架构——CoMViT。CoMViT集成了卷积分词器、对角掩码、动态温度缩放和基于聚合的序列聚集，以提高性能和推广性。该模型在十二个MedMNIST数据集上实现了稳健的性能，同时保持了轻量设计，参数量约为4.5M。CoMViT的性能指标与更深层的CNN和ViT变种相当，且在某些情况下甚至更好，仅需不到5-20倍的参数数量即能达到或超越先前模式的准确性。定量和定性分析表明，尽管体积小，CoMViT也在临床相关的区域表现出了更高的关注点。
### Conclusion
CoMViT通过系统性架构优化，在低资源的医疗成像场景下达到了高效和可解释的模型表现。
## 111. `cs.AI` - VCORE: 基于方差控制的优化权重分配以增强链式推理监督 [PDF](https://arxiv.org/pdf/2510.27462), [HTML](https://arxiv.org/abs/2510.27462)
### Authors
Xuan Gong,Senmiao Wang,Hanbo Huang,Ruoyu Sun,Shiyu Liang
### Background
监督微调（SFT）在长链式推理（CoT）路径上的应用已成为提升大型语言模型（LLMs）推理能力的关键技术。然而，标准的交叉熵损失忽视了不同推理路径上不同词汇的异质性贡献，这种均一处理导致监督分配错误且泛化能力较弱，特别是在复杂的长形式推理任务中更为明显。
### Innovation
本文提出了基于方差控制的优化权重重分配（VCORE），这是一种原理性的框架，将CoT监督重新表述为一个制约优化问题。通过采用优化理论视角，VCORE实现了监督在不同词汇间的合理和自适应分配，从而更加接近稳健推理泛化的目标。实验证明，VCORE相比现有词汇重分配方法表现出更优异的效果。它在小样本数学和编程基准测试中实现了显著的性能提升，采用Qwen3系列（4B, 8B, 32B）和LLaMA-3.1-8B-Instruct模型。此外，VCORE还证明了它作为后续强化学习的有效初始化方法，为提升LLMs的推理能力奠定了更强的基础。
### Conclusion
VCORE通过改进CoT监督的权重分配，显著提高了语言模型的推理能力。它实现了个性化和自适应的监督分配，增强了模型在复杂推理任务中的泛化能力。该方法在多个基准测试中表现优异，为提升大语言模型的推理能力提供了新的途径。
## 112. `cs.AI` - 思维分支：解释大型语言模型推理需要抽样重采样 [PDF](https://arxiv.org/pdf/2510.27484), [HTML](https://arxiv.org/abs/2510.27484)
### Authors
Uzay Macar,Paul C. Bogdan,Senthooran Rajamanoharan,Neel Nanda
### Background
大多数研究仅关注单一推理链（CoT），而这些模型实际上定义了多种可能的CoT的分布。研究单一样本不足以理解因果影响和内部计算机制。虽然完全指定这一分布是不可行的，但可以通过抽样来理解。
### Innovation
本文提出通过抽样进行案例研究的方法，以调查模型决策。研究了原因是否真正导致行动（如自保句子对黑站点施的影响）、人工编辑的CoT是否足以引导推理、移除推理步骤对模型的影响、以及当CoT不忠实时的方法效果。研究表明，抽样方法能够进行可靠的因果分析，并提供模型推理的清晰叙事，同时提出针对CoT的有原则的干预方法。
### Conclusion
通过抽样分析分布可以进行可靠的因果分析，为模型推理提供清晰的叙事，并提出有原则的CoT干预方法。这项工作表明，抽样方法是研究和理解模型推理的有效手段。
## 113. `cs.AI` - FedAdamW：具有通信效率和泛化保证的联邦大型模型优化器 [PDF](https://arxiv.org/pdf/2510.27486), [HTML](https://arxiv.org/abs/2510.27486)
### Authors
Junkang Liu,Fanhua Shang,Kewen Zhu,Hongying Liu,Yuanyuan Liu,Jin Liu
### Background
AdamW已成为训练大规模模型最有效的优化器之一，并在联邦学习（FL）中也表现出有效性。然而，在联邦学习环境中直接应用AdamW存在显著挑战，包括由于数据异质性导致的第二矩估计高方差、局部过拟合引起的客户端脱靶，以及每次循环重新初始化动量估计使收敛速度变慢。
### Innovation
提出了首个联邦AdamW算法FedAdamW，通过局部校正机制和解耦权重衰减对局部过拟合进行缓解。FedAdamW通过聚合第二矩估计的均值并重新初始化这些估计值来降低它们的方差。理论研究证明，FedAdamW在无需异质性假设的情况下实现了一个线性加速收敛速率。此外，采用PAC-Bayesian泛化分析解释了解耦权重衰减在局部训练中的有效性。
### Conclusion
FedAdamW在语言和视觉Transformer模型上验证了其有效性，显著减少通信轮次并提高测试精度。
## 114. `cs.AI` - InertialAR：基于惯性帧的自回归3D分子生成 [PDF](https://arxiv.org/pdf/2510.27497), [HTML](https://arxiv.org/abs/2510.27497)
### Authors
Haorui Li,Weitao Du,Yuqiang Li,Hongyu Guo,Shengchao Liu
### Background
基于变压器的自回归模型已经在文本和图像等模态中形成了统一的范式，但在3D分子生成方面的扩展研究仍然相对不足。这是因为两个基本挑战：(1) 将分子原子化为一个不变于SE(3)变换和原子索引排列的标准化1D序列；(2) 设计一种能够表达混合原子基元的架构，结合离散原子类型与连续3D坐标。
### Innovation
引入了InertialAR模型，这是一种解决上述挑战的方法。InertialAR通过将分子沿惯性框架对齐并重新排序来实现原子不变性和SE(3)不变性。还通过几何旋转位置编码（GeoRoPE）增强了注意力机制的几何感知能力，并使用分层自回归框架预测下一个原子基元，先预测原子类型，然后通过扩散损失预测其3D坐标。实验表明，InertialAR在7个评估指标中达到最先进的性能，并在目标化学功能的可控生成上大幅优于强大基线，取得了所有评估指标的最先进结果。
### Conclusion
InertialAR在无条件分子生成（QM9、GEOM-Drugs和B3LYP）的7个评估指标中取得了最先进的性能，并在目标化学功能的可控生成上显著优于强基线，在所有评估指标上均达到了最先进结果。
## 115. `cs.AI` - 在差分隐私联邦学习中通过惩罚梯度模寻找全局平坦最小值的DP-FedPGN [PDF](https://arxiv.org/pdf/2510.27504), [HTML](https://arxiv.org/abs/2510.27504)
### Authors
Junkang Liu,Yuxuan Tian,Fanhua Shang,Yuanyuan Liu,Hongying Liu,Junchao Zhou,Daorui Ding
### Background
差分隐私联邦学习（CL-DPFL）在防止推理攻击和减少敏感信息泄露方面得到了广泛应用。然而，现有的CL-DPFL方法通常会导致更锋利的损失景观，从而在差分隐私保护后降低模型的泛化能力。通过Sharpness Aware Minimization（SAM）应用局部平坦最小值来缓解这一问题的当前方法，但局部平坦性可能不反映全局平坦性，在客户端级差分隐私联邦学习中，找到全局平坦最小值依然是一个挑战。
### Innovation
提出了一种新的CL-DPFL算法DP-FedPGN，在本地损失中引入全局梯度模惩罚来寻找全局平坦最小值。此外，通过全局梯度模惩罚，不仅找到了更平坦的全局最小值，还减少了局部更新的模，进一步减少了梯度裁剪的误差。从理论上分析了DP-FedPGN如何缓解由差分隐私导致的性能下降，同时提出DP-FedPGN算法消除了数据异质性的影响，实现了快速收敛，并通过Rényi DP提供了严格的隐私保证，进行了局部更新的敏感性分析。
### Conclusion
在ResNet和Transformer模型上进行有效性测试，与现有最先进的算法相比，取得了六个视觉和自然语言处理任务上的显著改进。
## 116. `cs.AI` - 借助视觉Mamba的上下文门控跨模态感知在PET-CT肺肿瘤分割中的应用 [PDF](https://arxiv.org/pdf/2510.27508), [HTML](https://arxiv.org/abs/2510.27508)
### Authors
Elena Mulero Ayllón,Linlin Shen,Pierangelo Veltri,Fabrizia Gelardi,Arturo Chiti,Paolo Soda,Matteo Tortora
### Background
准确的肺肿瘤分割对提高诊断和治疗规划至关重要，同时有效地结合PET和CT的解剖和功能信息仍是一个主要挑战。
### Innovation
提出了一种轻量级跨模态框架vMambaX，通过上下文门控跨模态感知模块(CGM)整合PET和CT扫描图像。该模型在PCLT20K数据集上的评估表明，相比基础模型，模型在保持较低计算复杂性的同时表现更优。这突显了自适应跨模态门控在多模态肿瘤分割中的有效性。
### Conclusion
vMambaX框架作为先进肺癌分析的高效且可扩展框架显示出潜力，代码已开源。
## 117. `cs.AI` - 生成语义编码在超低比特率视觉通信与分析中的应用 [PDF](https://arxiv.org/pdf/2510.27324), [HTML](https://arxiv.org/abs/2510.27324)
### Authors
Weiming Chen,Yijia Wang,Zhihan Zhu,Zhihai He
### Background
本文考虑了在深空探测、战场情报和复杂环境中机器人导航等挑战性场景中，超低比特率视觉通信的问题。面对远程视觉分析和人体交互性能的高要求，如何在极端低通信带宽的情况下准确重构视觉场景成为一个重要研究问题。现有的文本到图像生成模型虽然为超低比特率图像描述提供新方法，但仅能实现视觉场景的语义级近似，不足以满足视觉通信和远程视觉分析及人体交互的需求。
### Innovation
本文提出了一种将图像生成与深度图像压缩无缝结合的方法，利用联合文本和编码潜变量引导校正流模型精确生成视觉场景。语义文本描述和编码潜变量均以极低的比特率编码并传输至解码器，实验结果表明，该方法在保持与现有方法相同图像重建质量和视觉分析准确性的同时，使用了更少的带宽资源。
### Conclusion
本文提出的方法在保持现有方法的图像重建质量和视觉分析准确性的同时，使用了更少的带宽资源。实验结果证明了方法的有效性和优越性，代码将在论文被接受后开源。
## 118. `cs.AI` - 陈旧代码，现代裁判：低数据环境下的元验证 [PDF](https://arxiv.org/pdf/2510.27244), [HTML](https://arxiv.org/abs/2510.27244)
### Authors
Ora Nova Fandina,Gal Amram,Eitan Farchi,Shmulik Froimovich,Raviv Gal,Wesam Ibraheem,Rami Katan,Alice Podolsky,Orna Raz
### Background
在以COBOL、PL/I和REXX等过时语言为基础的应用现代化过程中，面临专家资源短缺和高质量的人工评价数据稀缺的问题。为了克服这些挑战，Large Language Models作为裁判（LaaJ）提供了一种可扩展的选择，但它们的可靠性需要验证才能在重要工作流程中获得信任。缺乏这样的验证会导致一个循环的评价循环，即未经验证的LaaJ被用来评估其他模型输出，这可能会加强不准确的判断，并影响下游部署决策。
### Innovation
本文介绍了一种名为SparseAlign的正式框架，用于在少量人类标注数据的情况下评估LaaJ与人类判断的一致性。SparseAlign结合了一个新颖的成对信任概念和一个评分敏感的对齐度量，能够捕捉排名一致性与评分接近性，即使在传统统计方法因标注示例有限而无效时，也可实现可靠的评估员选择。
### Conclusion
 SparseAlign已被内部应用于选择COBOL代码解释的LaaJ。排名最高的评估者被集成到评估工作流程中，指导模型发布决策。文章通过四个LaaJ的实际案例研究展示了SparseAlign在实际评价场景中的应用价值。
## 119. `cs.AI` - FedMuon: 使用矩阵正交化加速联邦学习 [PDF](https://arxiv.org/pdf/2510.27403), [HTML](https://arxiv.org/abs/2510.27403)
### Authors
Junkang Liu,Fanhua Shang,Junchao Zhou,Hongying Liu,Yuanyuan Liu,Jin Liu
### Background
联邦学习的核心瓶颈在于通信轮次。如何在本地更新时实现更有效的局部更新是减少通信轮次的关键。现有的联邦学习方法仍然主要依赖元素级别的局部优化器（Adam/SGD），忽略了权重矩阵的几何结构。这会导致在本地更新时放大权重中的病态方向，导致条件数恶化和收敛速度变慢。
### Innovation
引入了局部Muon优化器，用于优化矩阵结构化参数，通过矩阵正交化优化技术。在此基础上，提出了Federated Muon优化器（FedMuon），结合了（1）动量聚合技术，使客户端使用聚合动量进行局部初始化；（2）局部-全局对齐技术，将局部梯度与全局更新方向对齐，显著减少客户端漂移。FedMuon在理论上证明了无需异质性假设的情况下实现了线性加速的收敛速率。实验结果显示，FedMuon在客户端分布独立和不独立的情况下，显著减少了通信轮次，提高了测试准确率。
### Conclusion
实验结果表明，FedMuon在语言和视觉模型上有效，与多个基线相比，显著减少了通信轮次并提高了测试准确率。
## 120. `cs.AI` - 平衡知识更新：面向大语言模型统一模块编辑 [PDF](https://arxiv.org/pdf/2510.27400), [HTML](https://arxiv.org/abs/2510.27400)
### Authors
Jiahao Liu,Zijian Wang,Kuo Zhao,Dong Hu
### Background
知识编辑作为一种提高大型语言模型（LLMs）事实知识更新效率的方法已经出现。它通常涉及定位知识存储模块并修改其参数。然而，大多数现有方法主要关注多层感知机（MLP）模块的权重，而这些模块被广泛认为是事实信息的主要存储库。相比之下，注意（Attn）模块等其他组件在编辑过程中往往被忽略。这种不平衡可能导致残留的过时知识，从而限制编辑效果。
### Innovation
本文进行了全面的知识定位实验，发现注意（Attn）模块在事实知识的存储和检索中起到了重要甚至主要的作用，尤其是在早期层中。基于这些洞察，提出了一种称为IntAttn-Edit的方法，该方法扩展了联想记忆范式，同时联合更新MLP和Attn模块。该方法采用了一种知识平衡策略，根据各模块对知识存储的贡献量调整更新幅度。实验表明，IntAttn-Edit在编辑成功率、泛化能力和知识保存方面都优于现有方法。进一步的分析表明，这种平衡策略能够在各种情况下保持编辑性能在最优范围内。
### Conclusion
IntAttn-Edit通过平衡MLP和Attn模块的更新，提供了一种更有效的知识编辑方法，使得知识编辑不仅对于早期层而且在整个模型中都更加有效，进而有助于提升大语言模型的知识更新效果。
## 121. `cs.AI` - 运用通用时间序列基础模型进行EEG分类 [PDF](https://arxiv.org/pdf/2510.27522), [HTML](https://arxiv.org/abs/2510.27522)
### Authors
Théo Gnassounou,Yessin Moakher,Shifeng Xie,Vasilii Feofanov,Ievgen Redko
### Background
时间序列基础模型正在成为强大的通用基础架构，但在像脑电图（EEG）这样的特定医疗领域的潜力尚未被广泛探索。本文旨在研究一个最近提出的通用时序分类基础模型在不同EEG任务（如运动想象分类和睡眠阶段预测）上的适用性。
### Innovation
该研究对比了两种预训练策略的效果：一种是多领域的真实世界时间序列数据，另一种是纯合成数据，并发现两种策略均能获得良好性能，超越广为使用的卷积基础模型EEGNet和最新EEG专用基础模型CBraMod。这些结果表明，即使是在非神经领域数据或合成信号上预训练，通用时间序列基础模型也能够有效迁移到EEG上。研究强调了跨越领域预训练模型在脑信号分析中的潜力，暗示EEG可以从更广泛的时序文献进步中受益。
### Conclusion
研究发现显示，通用时间序列基础模型可以通过跨领域的预训练有效应用于EEG，强化了利用更广泛时序文献进步对EEG进行分析的前景。
## 122. `cs.AI` - TetraJet-v2: NVFP4培训方法实现大型语言模型的准确度提升及振荡抑制和异常值控制 [PDF](https://arxiv.org/pdf/2510.27527), [HTML](https://arxiv.org/abs/2510.27527)
### Authors
Yuxiang Chen,Xiaoming Xu,Pengle Zhang,Michael Beyer,Martin Rapp,Jun Zhu,Jianfei Chen
### Background
大型语言模型（LLMs）的训练过程成本高昂，促使了低精度全量化训练（FQT）的研究兴趣。尽管新颖的4位格式，例如NVFP4提供了显著的效率提升，但在如此低的精度下实现近乎无损训练依然具有挑战性。
### Innovation
我们引入了TetraJet-v2，一个端到端的4位FQT方法，利用NVFP4对所有线性层的激活、权重和梯度进行量化。针对低精度LLM训练中遇到的两个关键问题：权重振荡和异常值，提出了解决方法，包括一个未经偏差的双块量化方法，一个用于抑制权重振荡的OsciReset算法，和一个用于保持异常值准确性的OutControl算法。
### Conclusion
TetraJet-v2在不同规模的LLM预训练中表现优越，相比于之前的FP4训练方法，平均减少性能差距51.3%。
## 123. `cs.AI` - 使用主动探索学习软体机器人的动力学 [PDF](https://arxiv.org/pdf/2510.27428), [HTML](https://arxiv.org/abs/2510.27428)
### Authors
Hehui Zheng,Bhavya Sukhija,Chenhao Li,Klemens Iten,Andreas Krause,Robert K. Katzschmann
### Background
软体机器人在非结构化环境中展现出无与伦比的适应性和安全性，但由于其柔顺性、高维数和非线性动力学，对其进行建模以控制变得非常困难。现有的数据驱动方法常常无法泛化，受限于狭窄的任务演示或低效的随机探索。已有方法往往因为数据不足或效率低下而无法有效构建动态模型，影响控制效果和适应性。因此，建立一种能够自主学习泛化性强的动力学模型的框架显得尤为重要。
### Innovation
本文提出了一种不确定性感知的主动探索框架SoftAE，它不依靠特定任务的监督，能够主动学习软体机器人的任务无关和泛化性动态模型。SoftAE通过使用概率集成模型估计认识性不确定性，以主动引导探索，覆盖未出现的任务的空间区域，从而实现对多样化行为的有效覆盖，减少了特定任务的监督需求，提高了模型的准确性和鲁棒性。
### Conclusion
文章实验结果表明，SoftAE相比于随机探索和特定任务的模型驱动强化学习，能够产生更准确的动力学模型，实现更好的零样本控制，并在感知噪声、执行延迟和非线性材料效应下保持稳定性。这些结果表明，不确定性驱动的主动探索能够为不同的软体机器人形态产生可扩展且可重用的动力学模型，为软体机器人更自主、适应性和数据效率的控制开辟了道路。
## 124. `cs.AI` - 矢量化在线POMDP规划 [PDF](https://arxiv.org/pdf/2510.27191), [HTML](https://arxiv.org/abs/2510.27191)
### Authors
Marcus Hoerger,Muhammad Sudrajat,Hanna Kurniawati
### Background
在部分可观测性的条件下进行计划是自主机器人的一项基本能力。部分可观测的马尔科夫决策过程（POMDP）提供了一个强有力的框架来解决部分可观测性问题，它可以捕捉行动的随机效果以及通过嘈杂观测获得的有限信息。虽然现代硬件的并行化能显著提高POMDP解决方法的效率，但将POMDP求解器进行并行化处理仍然具有挑战性，因为需要交错进行行动数值优化与价值估计，这导致了并行过程之间的依赖性和同步瓶颈。
### Innovation
本文提出了一种新颖的在线并行求解器矢量化在线POMDP规划器（VOPP），它利用了最近提出的POMDP公式，该公式可以分析解决部分优化组件，仅将期望估计留给数值计算。VOPP将以张量形式表示所有与规划相关的数据结构，并将所有规划步骤作为在整个表示上完全矢量化计算实现。结果是具有大规模并行性和无并行计算依赖性和同步瓶颈的求解器。实验结果表明，与现有的最先进的在线并行求解器相比，VOPP在计算近最优解方面至少快20倍。
### Conclusion
实验结果显示，VOPP在计算近最优解方面至少比现有的最优在线并行求解器快20倍，显著提高了POMDP求解的效率。
## 125. `cs.AI` - 语言作为模态性：通过编码器注入实现跨语言对齐 [PDF](https://arxiv.org/pdf/2510.27254), [HTML](https://arxiv.org/abs/2510.27254)
### Authors
Rajan Agarwal,Aarush Gupta
### Background
大型语言模型(Large Language Models, LLMs)在低资源非拉丁语系任务上表现不佳，主要归因于分词器碎片化和跨语言联系薄弱。尽管指令微调可以提高LLMs的效果，但它们在非拉丁语系任务上的表现仍然受限。现有方法虽然取得了一定进展，但在多语言理解和跨语言对齐方面仍有不足，特别在数字准确性和低资源语言支持方面有待提高。因此，需要一种更高效且对跨语言对齐有价值的替代方案，特别是针对低资源非拉丁语系的任务。
### Innovation
研究提出了LLINK（Latent Language Injection for Non-English Knowledge）方法，这是一种计算效率较高的多语言模态性技术。该方法通过一个轻量级对比投影器将冻结的多语言编码器的句子嵌入对齐到解码器的潜在嵌入空间，并在保留位置引入K个软槽，使解码器在无需修改分词器和重新训练解码器的前提下接受信号。实验结果表明，LLINK在双语检索任务中显著提高了性能，并且在LLM评估的问答任务中优于基础模型和直接微调，尤其是在低数据任务方面的改进尤为明显。这种方法强调了低资源语言作为一种模态的重要性，并为轻量级LLMs中的跨语言对齐提供了新的途径。
### Conclusion
这种通过编码器注入实现在低资源非拉丁语系上的跨语言对齐方法，显著提升了LLM的多语言性能和泛化能力，特别是在保持语言一致性的同时，减小了分词增多带来的负面影响，并展示了在低资源语言学习上的前景。但在数值准确性和某些具体语言理解方面仍有待进一步优化。
## 126. `cs.AI` - 基于场景图的语言到动作：通过基础模型实现精确的长时距机器人操作 [PDF](https://arxiv.org/pdf/2510.27558), [HTML](https://arxiv.org/abs/2510.27558)
### Authors
Sushil Samuel Dinesh,Shinkyu Park
### Background
该论文的背景是目前机器人操作系统通常需要针对特定领域进行训练，这限制了其广泛应用。研究者们尝试利用预训练的基础模型来进行机器人操作，以减少领域的特定训练需求，提高通用性和灵活性。
### Innovation
论文的主要创新在于提出了一种框架，利用预训练的基础模型来进行通用的机器人操作，无需领域特定的训练。该框架结合了基础模型的多模态感知能力和一个通用推理模型，用于实现鲁棒的任务序列。框架内置动态维护的场景图提供空间感知，支持环境的一致性推理。
### Conclusion
论文通过一系列桌面机器人操作实验对该框架进行了评估，并表明其有潜力直接基于现成的基础模型构建机器人操作系统，展示了其在长时距机器人操作中的应用前景。
## 127. `cs.AI` - DialectalArabicMMLU: 测量阿拉伯语和多语言语言模型方言能力的基准 [PDF](https://arxiv.org/pdf/2510.27543), [HTML](https://arxiv.org/abs/2510.27543)
### Authors
Malik H. Altakrori,Nizar Habash,Abdelhakim Freihat,Younes Samih,Kirill Chirkunov,Muhammed AbuOdeh,Radu Florian,Teresa Lynn,Preslav Nakov,Alham Fikri Aji
### Background
尽管近期开发的阿拉伯语和多语言基准已经提升了现代标准阿拉伯语（MSA）的语言模型评估，但方言变体在日常交流中的普遍性并未得到反映，这导致了对模型在方言理解上的评估不足。为了填补这一空白，该研究提出了DialectalArabicMMLU基准评测框架，用于评估语言模型在阿拉伯语不同方言上的表现。该基准通过对3000个选择题-答案对进行手动翻译和适应，覆盖了五个主要阿拉伯语方言：叙利亚语、埃及语、阿联酋语、沙特语和摩洛哥语。共有15000个QA对涉及32个学术和专业领域（当包括英语和MSA时为22000个QA对）。这种基准测试使研究者能够系统地评估模型在MSA之外的推理和理解能力，支持任务分析和语言层面的评估。
### Innovation
DialectalArabicMMLU首创了一个统一的人工编制的资源，用于测量阿拉伯语中的方言理解能力，填补了现有阿拉伯语及其多语言模型评估方法的空白。这个基准为评估和未来模型开发提供了更包容的视角，揭示了在不同方言上存在持续的泛化差距，标志着语言模型在多语境环境下的进步。
### Conclusion
DialectalArabicMMLU为阿拉伯语和多语言语言模型的方言评估提供了一个系统化的资源，展示了模型在不同方言上表现的显著差异，为促进更加公平和包容的模型训练提供了重要工具，有助于未来模型的优化和发展。
## 128. `cs.AI` - CodeAlignBench: 评估开发者偏好代码调整的代码生成模型 [PDF](https://arxiv.org/pdf/2510.27565), [HTML](https://arxiv.org/abs/2510.27565)
### Authors
Forough Mehralian,Ryan Shar,James R. Rae,Alireza Hashemi
### Background
随着大规模语言模型在生成代码方面的能力不断增强，评估它们的性能仍然是一个复杂且不断演进的挑战。现有的基准测试主要集中在功能性正确性上，忽视了实际编码任务的多样性和开发者的期望。
### Innovation
该论文引入了一个多语言基准测试，评估大型语言模型的指令遵循能力，并可根据任意独立的编码问题集进行扩展。基准测试在两个关键方面评估指令遵循：一是遵循初始问题中预定义的约束，二是根据后续指令进行改进的能力。实验使用来自LiveBench的任务进行评估，并自动将Python代码翻译为Java和JavaScript代码。研究表明，模型在指令遵循的多个维度上表现出不同的性能。
### Conclusion
基准测试管道为代码生成模型提供了更为全面的评估，突显了它们在不同语言和生成目标方面的优点和局限性。
## 129. `cs.AI` -  Sybil-Resistant Service Discovery for Agent Economies [PDF](https://arxiv.org/pdf/2510.27554), [HTML](https://arxiv.org/abs/2510.27554)
### Authors
David Shi,Kevin Joo
### Background
本文探索了如何在代理经济体中进行服务发现，特别是在这些服务接受加密货币支付的情况下。随着代理越来越多地使用这些服务，如何确保这些服务的可靠性和安全性变得愈发重要，特别是在代理需要发现值得信任的交换接口和可靠的数据提供方时。传统的服务发现方法往往依赖于交易量，这容易受到Sybil攻击，即通过创建大量假账户来操纵排名，从而导致服务质量下降。
### Innovation
本文提出了TraceRank，这是一种基于声誉加权的排名算法，通过支付交易来验证声誉，以减轻Sybil攻击。该算法通过预计算的声誉凭证和交易价值以及时间相关性来传播声誉。该系统结合了语义搜索，能够用高质量的结果响应自然语言查询。这种方法优于仅仅依赖交易量或者语义方法，因为它能够避免基础设施偏见，并且通过将声誉传播应用于支付图，可以揭示高度声誉用户更喜欢的服务，而不是交易量大的服务。
### Conclusion
我们提出的方法旨在构建一个能够避免基础设施偏见且性能优于交易量或语义方法的x402启用服务的搜索方法。该方法通过将声誉传播应用于服务发现，确保了服务发现的可靠性，同时减轻了Sybil攻击的影响。
## 130. `cs.AI` - EBT-Policy: 能量解锁新兴的物理推理能力 [PDF](https://arxiv.org/pdf/2510.27545), [HTML](https://arxiv.org/abs/2510.27545)
### Authors
Travis Davies,Yiqi Huang,Alexi Gladstone,Yunxin Liu,Xiang Chen,Heng Ji,Huxian Liu,Luhui Hu
### Background
隐式政策（由生成模型参数化）已成为机器人领域政策学习和视觉-语言-动作（VLA）模型的标准方法。然而，这些方法通常面临高计算成本、曝光偏差和不稳定的推理动态等问题，导致在分布转移时出现发散现象。能量基模型（EBMs）通过端到端学习能量景观并建模平衡动态来解决这些问题，提供了改进的鲁棒性并减少了曝光偏差。但由EBM参数化的政策历史上在有效扩展方面遇到困难。最近关于能量基变换器（EBTs）的工作展示了EBMs在高维空间的可扩展性，但它们在解决物理身体模型核心挑战方面的潜力尚未充分探索。
### Innovation
我们引入了一种新的能量基架构——EBT-Policy，解决了机器人和现实世界环境中的核心问题。与基于扩散的策略相比，EBT-Policy在模拟和现实任务中表现出更优的表现，同时需要较少的训练和推理计算。值得注意的是，某些任务上它仅在两次推理步骤内收敛，对比扩散策略的100步，效率提高了50倍。此外，EBT-Policy展示了之前模型中未见的新颖能力，如通过行为克隆直接恢复失败动作序列的动力，无需显式重试培训。通过利用其标量能量进行不确定性感知推理和动态计算分配，EBT-Policy为在分布转移下实现稳健且通用的机器人行为提供了有前景的路径。
### Conclusion
EBT-Policy通过优化能源模型和推理动态，显著提高了物理机器人任务中的效率与鲁棒性，展示了在现实世界环境中的广泛应用潜力。
## 131. `cs.AI` - Spatial-SSRL: 通过自我监督强化学习增强空间理解 [PDF](https://arxiv.org/pdf/2510.27606), [HTML](https://arxiv.org/abs/2510.27606)
### Authors
Yuhong Liu,Beichen Zhang,Yuhang Zang,Yuhang Cao,Long Xing,Xiaoyi Dong,Haodong Duan,Dahua Lin,Jiaqi Wang
### Background
大型视觉-语言模型（LVLMs）在空间理解方面存在不足。现有的监督微调（SFT）和最近的基于可验证奖励的强化学习（RLVR）方法依赖于昂贵的监督、特殊工具或受限环境，限制了模型的规模。现有的方法主要通过人类或模型标注的数据进行监督，这增加了成本并限制了模型的规模和能力。因此，需要一种新的方法来增强LVLMs的空间理解能力，同时降低监督成本并提高模型的规模和通用性。
### Innovation
本文提出了Spatial-SSRL，一种自我监督的RL范式，从普通的RGB或RGB-D图像中直接推导出可验证的信号。Spatial-SSRL自动制定了五个预训练任务，这些任务捕捉了2D和3D空间结构，分别为打乱的块重新排序、翻转的块识别、裁剪的块图像填补、区域深度排序和相对三维位置预测。这些任务提供了易于验证且不需要人类或LVLM标注的正确答案。训练这些任务显著提高了空间推理能力，同时保留了模型的一般视觉能力。
### Conclusion
在七个空间理解基准测试中，无论是图像还是视频设置，Spatial-SSRL在Qwen2.5-VL基线上均实现了平均4.63%（3B）和3.89%（7B）的准确度增长。结果表明，简单的内在监督使大规模的RLVR成为可能，提供了一种实用的途径，以增强LVLMs的空间智能。
## 132. `cs.AI` - 开放权重生物基础模型的生物风险评估最佳实践 [PDF](https://arxiv.org/pdf/2510.27629), [HTML](https://arxiv.org/abs/2510.27629)
### Authors
Boyi Wei,Zora Che,Nathaniel Li,Udari Madhushani Sehwag,Jasper Götting,Samira Nedungadi,Julian Michael,Summer Yue,Dan Hendrycks,Peter Henderson,Zifan Wang,Seth Donoughe,Mantas Mazeika
### Background
开放权重生物基础模型具有加速科学研究和药物开发的潜力，但也很可能被不良分子用于开发更致命的生物武器。现有的应对策略集中在预训练阶段筛选生物危害数据，但这种方法的有效性存疑，特别是针对那些可能精调模型以进行恶意使用的有决心的分子。
### Innovation
本文提出了一种名为textbackslash eval的方法，一种评估旨在降低开放权重生物基础模型双重用途能力的程序稳定性的框架。textbackslash eval通过序列建模、突变效应预测和致病性预测三个视角来评估模型对病毒的理解。
### Conclusion
当前的数据过滤方法可能不够有效，被排除的知识可能通过微调迅速恢复，并且在序列建模中表现出更广泛的普适性。双重用途信号可能已经存在于预训练表示中，可以通过简单的线性探针被激发。这些发现突显了单纯依赖数据过滤作为独立措施的挑战，强调了需要进一步研究开放权重生物基础模型的安全和安全策略的重要性。
## 133. `cs.AI` - 迈向普适性视频检索：通过合成多模态金字塔课程实现视频嵌入泛化 [PDF](https://arxiv.org/pdf/2510.27571), [HTML](https://arxiv.org/abs/2510.27571)
### Authors
Zhuoning Guo,Mingxin Li,Yanzhao Zhang,Dingkun Long,Pengjun Xie,Xiaowen Chu
### Background
当前的视频检索范式结构上存在偏差，狭窄的基准测试会激励有限的数据集和单一任务的训练，这抑制了跨任务和领域的需求，即多维度的一般化能力。因此，缺乏诊断性评估机制，导致无法全面检测和要求多维度的通用能力。为打破这种循环，本文提出了一个从评估、数据和建模三方面的协同设计框架。首先，建立了普适视频检索基准（UVRB），包含16个数据集，用于不仅衡量性能，还诊断不同任务和领域的关键能力缺口。其次，根据UVRB提供的诊断信息，引入了可扩展的合成工作流程，生成一百多万个高质量的配对来填充所需的语义空间。最后，设计了模态金字塔，通过充分利用各种数据中的潜在联系，训练普适视频嵌入器（GVE）。实验结果表明，GVE 在UVRB上的零样本泛化能力达到领先水平。特别地，研究表明流行的基准测试不能很好地预测一般能力，并且部分相关的检索是普遍存在的但未被充分关注的情况。
### Innovation
本文提出了针对评估、数据和建模的协同设计框架，并建立了普适视频检索基准（UVRB），包含16个数据集，用于不仅衡量性能，还诊断不同任务和领域的关键能力缺口。在此基础上，引入了一种可扩展的合成工作流程来生成大量高质量配对，以填充所需的语义空间。同时，设计了模态金字塔课程，通过利用数据中的潜在联系，有效训练普適视频嵌入器（GVE），并在零样本泛化评估上取得了领先的结果。
### Conclusion
本文提出的设计框架为实现普适性视频检索提供了实际途径，打破了现有方法的局限性，并朝着真正的普适视频检索迈进。通过UVRB提供的诊断信息，它展示了目前流行的基准测试不能很好地预测一般能力，并且部分相关检索是普遍存在的但未被充分关注的情况。
## 134. `cs.AI` - 从草图到布局：基于草图的多模态布局生成 [PDF](https://arxiv.org/pdf/2510.27632), [HTML](https://arxiv.org/abs/2510.27632)
### Authors
Riccardo Brioschi,Aleksandr Alekseev,Emanuele Nevali,Berkay Döner,Omar El Malki,Blagoj Mitrevski,Leandro Kieliger,Mark Collier,Andrii Maksai,Jesse Berent,Claudiu Musat,Efi Kokiopoulou
### Background
图形布局生成是一个快速发展的研究领域，专注于从海报设计到文档的美观布局生成。虽然最近的研究探索了通过将用户约束引入布局生成过程来引导生成的方式，但用户需求有时需要复杂的规范，这降低了用户友好性。该论文的研究背景在于解决这一问题，并提出一种创新的方法，即利用用户提供的草图作为直观的约束来解决从草图到布局的问题，旨在减轻复杂规范带来的负担，且通过实验证明该方法的有效性。
### Innovation
该研究提出了一个采用Transformer的多模态解决方案，利用草图和内容资产作为输入生成高质量的布局。由于从人类注释者收集草图训练数据成本高昂，研究还介绍了大规模生成合成训练草图的新且高效的方法。该模型在三个公开数据集（PubLayNet，DocLayNet和SlidesVQA）上进行了训练和评估，展示了其优于现有的基于约束的方法，并提供了更直观的设计体验。此外，研究还发布了超过20万个合成生成的草图，以支持未来的研究。
### Conclusion
该研究通过从草图到布局的多模态生成方法，提升了布局生成的用户友好性，同时证明了该方向的潜力并展示了其优异性能。此方法为未来此类研究提供了强大的基础，并通过发布大量合成生成的草图促进了该领域的进一步研究。
## 135. `cs.AI` - 开放智能体系统中多智能体强化学习中的归因挑战 [PDF](https://arxiv.org/pdf/2510.27659), [HTML](https://arxiv.org/abs/2510.27659)
### Authors
Alireza Saleh Abadi,Leen-Kiat Soh
### Background
在迅速发展的多智能体强化学习（MARL）领域，理解开放系统的动力学至关重要。在这里，开放性指的是智能体群体、任务和智能体类型在系统中的动态特性。具体分为三种类型：代理开放性、任务开放性和类型开放性。传统的归因问题（CAP）方法假设智能体群体制固定、任务固定且类型稳定，这些假设在开放环境中不再成立，导致了传统方法的不足。
### Innovation
本文首先进行了概念分析，介绍了新的开放性子类别，详细说明了代理更替或任务取消如何打破现有CAP方法的前提假设，这些假设依赖于环境的稳定性和固定团队组合。然后，通过开放环境中的代表时间和结构算法进行实证研究，展示了开放性直接导致了归因错误，表现为不稳定的价格函数和显著的性能下降。
### Conclusion
研究结果表明，在开放环境中，传统的归因方法存在不足，开放性会直接导致归因错误。开放性机制使代理贡献难以准确评估，从而影响整体系统性能。
## 136. `cs.AI` - VessShape: 通过合成图像中的形状先验实现少量样本下的2D血液血管分割 [PDF](https://arxiv.org/pdf/2510.27646), [HTML](https://arxiv.org/abs/2510.27646)
### Authors
Cesar H. Comin,Wesley N. Galvão
### Background
医学图像分析中的血血管语义分割是一个重要的任务，但受到大型注释数据集稀缺性和不同成像模态之间的模型泛化能力差的阻碍。卷积神经网络（CNN）倾向于学习基于纹理的特征，限制了它们在视觉特性不同的新领域中的性能。为了克服这些挑战，本研究引入了VessShape方法，通过生成大规模的2D合成数据集来增强分割模型对形状的偏好，这些数据集包含程序生成的管状几何和各种背景纹理，以鼓励模型学习形状线索而非纹理特征。
### Innovation
本研究提出了VessShape方法，通过生成程序生成的2D合成数据集，其中包含管状几何和各种纹理，来增强分割模型对形状的偏好。这种方法可以在少量样本下实现强大的零样本和少量样本下的分割性能，有效解决了数据稀缺和模型泛化能力差的问题，为医学图像分析中血液血管分割提供了一种新的策略。
### Conclusion
实验结果表明，具有强烈形状偏置的预训练可以有效地克服数据稀缺性，并在血液血管分割中改善模型的泛化能力。本研究提出的方法可以在不同领域实现有效的零样本分割，仅需要少量的样本进行微调，展示了其在医学图像分析中的潜力。
## 137. `cs.AI` - 模型解释图上的社区检测以实现可解释人工智能 [PDF](https://arxiv.org/pdf/2510.27655), [HTML](https://arxiv.org/abs/2510.27655)
### Authors
Ehsan Moradi
### Background
特征归因方法（例如SHAP、LIME）可以解释个别预测，但对于更高级别的结构（即一组共同作用的特征集）却不够敏感。为了对此类问题提出解决方案，研究者们开发了一种名为MoI的框架，该框架能够构建基于实例的归因模型解释图、运用社区检测算法找到影响预测的特征模块，并量化这些模块与偏见、冗余和因果关系模式之间的关系。
### Innovation
研究人员提出了MoI框架，通过构建模型解释图和应用社区检测，发现对预测有共同影响的特征模块，并量化它们与偏见、冗余和因果关系模式之间的关系。此外，MoI还能够揭示相关特征组，并通过模块级的消除方法改进模型调试，还能定位偏见的具体模块。该研究还发布了稳定性与协同性的度量标准、参考实现和评估协议，用于对特征模块的发现进行基准测试。
### Conclusion
MoI框架在合成和真实数据集上提供了新的见解，改进了模型调试，并且通过定位特定的模块标记偏见。研究者还提供了稳定性与协同性的度量标准、参考实现以及评估协议来促进特征模块发现的基准测试。
## 138. `cs.AI` - 连续自回归语言模型 [PDF](https://arxiv.org/pdf/2510.27688), [HTML](https://arxiv.org/abs/2510.27688)
### Authors
Chenze Shao,Darren Li,Fandong Meng,Jie Zhou
### Background
大型语言模型（LLMs）的效率受限于它们逐个生成标记的过程。本文认为，必须通过增加每一步生成操作的语义带宽来突破这一瓶颈。因此，提出了连续自回归语言模型（CALM），从离散的下一个标记预测转变为连续的下一个向量预测，从而改进生成过程。
### Innovation
引入了连续自回归语言模型（CALM），通过高保真度自编码器将连续的K个标记压缩成单一的连续向量。这种方法使得语言能够被建模为连续向量序列，从而减少生成步骤的数量。此外，开发了一个全面的无似然框架，用于连续域的鲁棒训练、评估和可控制样。实验表明，CALM 以显著较低的计算成本实现了强大的离散基线的性能。
### Conclusion
这些发现表明，接下来的向量预测是通向下一代超高效语言模型的强大且可扩展的途径。
## 139. `cs.AI` - 全面过程导向的自动文本总结与LLM方法探索综述 [PDF](https://arxiv.org/pdf/2403.02901), [HTML](https://arxiv.org/abs/2403.02901)
### Authors
Yang Zhang,Hanlei Jin,Dan Meng,Jun Wang,Jinghua Tan
### Background
自动文本摘要（ATS）利用自然语言处理（NLP）算法，旨在创建简洁准确的摘要，从而显著减少处理大量文本所需的人工努力。尽管ATS受到了学术和工业界的广泛关注，但以前的研究常常缺乏实际应用性，因为它们通常是从理论角度对前人方法进行分类，而大型语言模型（LLMs）的出现改变了传统的ATS方法。
### Innovation
本文旨在1) 提供一种全面的过程导向的ATS综述，最符合实际应用；2) 完整地回顾最新的基于LLM的ATS工作；并3) 提供最新的ATS综述，填补文献中的两年空白。据我们所知，这是首次专门研究基于LLM的ATS方法的综述。
### Conclusion
本文全面地从过程导向的角度回顾了ATS，并深入探讨了基于LLM的ATS方法，填补了ATS研究中两年的空白，为未来的ATS研究提供了新的视角和方向。
## 140. `cs.AI` - PETAR: Localized Findings Generation with Mask-Aware Vision-Language Modeling for PET Automated Reporting [PDF](https://arxiv.org/pdf/2510.27680), [HTML](https://arxiv.org/abs/2510.27680)
### Authors
Danyal Maqbool,Changhee Lee,Zachary Huemann,Samuel D. Church,Matthew E. Larson,Scott B. Perlman,Tomas A. Romero,Joshua D. Warner,Meghan Lubner,Xin Tie,Jameson Merkow,Junjie Hu,Steve Y. Cho,Tyler J. Bradshaw
### Background
近期视觉-语言模型（VLMs）的发展使多模态推理变得令人印象深刻，但在医学应用方面仍主要局限于二维成像领域。本工作将视觉-语言模型扩展至正电子发射断层扫描与计算机断层扫描（PET/CT），这种领域包含大量的体积数据、分散的小病灶以及冗长的放射学报告。本研究构建了一个包含11000多个病灶级描述和超过5000个PET/CT影像的大型数据集，利用混合规则和大型语言模型进行提取。该数据集被用于构建PETAR-4B，这是一种能够融合PET、CT和病灶轮廓的3D掩码感知视觉-语言模型，以实现基于空间的报告生成。
### Innovation
该研究引入了一个规模庞大的数据集，用于训练多模态模型处理PET/CT数据。创新点在于提出了3D掩码感知的视觉-语言模型PETAR-4B，该模型能够结合PET、CT图像及病灶轮廓，生成具有临床相关性和定位性的报告。这种模型通过融合全局上下文理解和细致的病灶感知，提升了PET/CT影像报告的质量，促进了3D医学视觉-语言理解的进步。
### Conclusion
全面的自动化和人工评估表明，PETAR在PET/CT报告自动生成方面显著提升了报告质量。该研究为3D医学视觉-语言理解的深度解析提供了新的方法论，并有望加速医学影像自动化报告的发展。
## 141. `cs.AI` - VRoPE: Video Rotary Position Embedding for Video Large Language Models [PDF](https://arxiv.org/pdf/2502.11664), [HTML](https://arxiv.org/abs/2502.11664)
### Authors
Zikang Liu,Longteng Guo,Yepeng Tang,Tongtian Yue,Junxian Cai,Kai Ma,Qingbin Liu,Xi Chen,Jing Liu
### Background
Rotary Position Embedding (RoPE) 在基于文本的大语言模型(LLMs)中表现出强大的性能，但在将其扩展应用于视频时遇到挑战，因为视频帧具有复杂的时空结构。现有的尝试，如 RoPE-3D，分别编码空间和时间维度，但存在位置偏差和视频-文本过渡中断的问题。
### Innovation
提出了 Video Rotary Position Embedding (VRoPE)，一种新的适用于 Video-LLMs 的位置编码方法。具体来说，VRoPE 引入了更加平衡的编码策略，减轻了注意力偏差，确保了空间关注的均匀分布。此外，VRoPE 调整了位置索引，确保了视频和文本标记之间的平滑过渡。
### Conclusion
广泛的实验证明，VRoPE 一致地优于之前的 RoPE 变体，在视频理解、时间推理和检索任务中取得了显著的改进。
## 142. `cs.AI` - 信息论驱动的贪心分层训练方法在交通标志识别中的应用 [PDF](https://arxiv.org/pdf/2510.27651), [HTML](https://arxiv.org/abs/2510.27651)
### Authors
Shuyan Lyu,Zhanzimo Wu,Junliang Du
### Background
现代深层神经网络通常通过全局交叉熵损失在监督模式下从头到尾进行训练：神经元需要存储其传出权重；训练交替进行正向传播（计算）和反向传播（学习）过程，这在生物学上是不可实现的。另一种替代方案是逐层贪婪训练，通过避免计算中间梯度和存储中间输出，减少了内存使用并缓解了梯度消失或爆炸的问题。然而，大多数现有的逐层训练方法仅在较小的数据集和简单的深层架构上进行了评估。本文首先从信息论的角度系统分析常用卷积神经网络（CNN）由随机梯度下降（SGD）训练的训练动态。研究发现，网络从下到上逐层收敛，并遵循马尔可夫信息瓶颈原则。基于此观察，我们提出了一种新的基于最近开发的确定性信息瓶颈（DIB）和矩阵型Rényi’s $boldsymbol{boldsymbol{beta}}$-阶熵泛函的分层训练方法。每个分层联合训练了一个辅助分类器，直接连接到输出层，使学习最小相关的任务相关信息表示成为可能。我们通过CIFAR-10和CIFAR-100上现代深层CNN验证了该训练方法的有效性，并进一步证明其在实际的交通标志识别任务中的适用性。与现有方法相比，我们的方法不仅表现出色，还达到了与SGD相当的性能。
### Innovation
本文提出了一种新的信息论驱动的贪心分层训练方法，基于确定性信息瓶颈（DIB）和矩阵型Rényi’s $boldsymbol{boldsymbol{beta}}$-阶熵泛函。这种新方法通过每个分层联合训练一个直接连接到输出层的辅助分类器，使得网络能够学习最小相关的任务相关信息表示。这种方法不仅提高了训练效果，还减少了内存需求，并且在实际任务中表现出卓越的性能。
### Conclusion
本文提出的方法不仅在交通标志识别等实际任务中达到了与标准随机梯度下降法相当的性能，还在CIFAR-10和CIFAR-100数据集上的现代深层CNN上验证了其有效性和优越性。
## 143. `cs.AI` - 面向目标定向的动态随机场框架 [PDF](https://arxiv.org/pdf/2504.16115), [HTML](https://arxiv.org/abs/2504.16115)
### Authors
Yibo Jacky Zhang,Sanmi Koyejo
### Background
领域为描述由相互作用和动态组件组成的复杂系统提供了一种灵活的方法。特别是在某些动态和随机系统中，表现出旨在实现特定目标的智能行为。然而，由于这些系统的固有复杂性，开发这些系统的正式理论描述并将其有效转化为实际应用仍然具有挑战性。
### Innovation
提出三种基本原则来建立理解智能字段的理论框架：完整的配置、局部性以及目的性。此外，从人工智能应用的角度探索了设计这些字段的方法学。
### Conclusion
本初探旨在为未来智能目标驱动的动态随机场的理论发展和实际进步奠定基础。
## 144. `cs.AI` - 通过视觉语言模型实现强化学习的自动语义解释 [PDF](https://arxiv.org/pdf/2503.16724), [HTML](https://arxiv.org/abs/2503.16724)
### Authors
Zhaoxin Li,Zhang Xi-Jia,Batuhan Altundas,Letian Chen,Rohan Paleja,Matthew Gombolay
### Background
在强化学习（RL）中实现语义解释有助于增强决策的透明性和验证性。实现语义解释需要一个由人类可理解的概念组成的特征空间和一个可解释且可验证的策略。然而，构造这样的特征空间通常依赖于手动的、通常无法适应未知环境的人类指定。即使有了可解释的特征，大多数强化学习算法也采用黑盒模型作为策略，因此限制了透明度。
### Innovation
iTRACE是一种自动框架，利用预训练的视觉-语言模型（VLM）进行语义特征提取，并通过强化学习训练可解释的树状模型。研究人员提出通过视觉-语言模型自动进行树状强化学习以减轻对传统可解释模型中所需的人类注解的依赖，同时也解决了VLM单独使用时的一些关键限制。
### Conclusion
研究结果表明，iTRACE在多个领域中（如Atari游戏、网格导航和驾驶）优于其他可解释策略基准，并在相同的可解释特征空间上达到了与黑盒策略相当的性能。
## 145. `cs.AI` - 保留婴儿，不要倒掉洗澡水：为什么以及如何利用深度学习解决ARC [PDF](https://arxiv.org/pdf/2506.14276), [HTML](https://arxiv.org/abs/2506.14276)
### Authors
Jack Cole,Mohamed Osman
### Background
ARC-AGI 为 AI 系统提出了巨大挑战。尽管在 ARC 上的表现通常不佳，深度学习仍然是生成在视觉、语言等领域多样模式和任务上表现卓越的神经网络（NN）的最有效策略。通过训练使这些神经网络掌握所需的抽象思维能力。
### Innovation
本研究进一步依赖深度学习的能力来获取新的抽象思维，并在测试时进行即时 NN 训练。研究提出了在 ARC 上训练的全新方法，从预训练的大语言模型（LLMs）开始，并增强了它们的 ARC 推理。还提出了一种名为 Test-Time Fine-Tuning (TTFT) 和 Augment Inference Reverse-Augmentation and Vote (AIRV) 的有效测试时技术。首次显示深度学习可用于 ARC，并通过 AIRV 提高了高达 260% 的准确性，TTFT 进一步提高了 300% 的准确性。
### Conclusion
我们的发现强调了在新领域中建立稳健推理系统的关键要素，突显出改善广泛感知推理的核心机制。
## 146. `cs.AI` - 通过目标导向的常识推理解决可信AI的16+2项需求 [PDF](https://arxiv.org/pdf/2506.12667), [HTML](https://arxiv.org/abs/2506.12667)
### Authors
Alexis R. Tudor,Yankai Zeng,Huaduo Wang,Joaquin Arias,Gopal Gupta
### Background
当前AI和机器学习算法的进步凸显了确保其可信性的必要性，特别是出于法律、伦理和商业考虑。子象征机器学习算法，例如大型语言模型（LLMs），虽然能模拟推理过程，但会产生幻觉，且其决策难以解释或审计，这对可信性的要求至关重要。相比之下，基于规则的推理系统，如Cyc，能够提供推理链的详细步骤，但也极其复杂，需要大量推理机制。这篇论文旨在通过使用s(CASP)推理器（一种目标导向的基于约束的归纳集理论推理器），采用少量机制来模拟可靠且可解释的人类常见的常识推理，找到一个平衡点，以解决可信AI的问题。
### Innovation
提出了一种名为s(CASP)的推理器，通过少量机制实现可靠且可解释的人类风格的常识推理，同时满足Doug Lenat和Gary Marcus提出的16项可信AI的需求，以及额外增加了不一致性检测和对替代世界假设的支持。论文展示了s(CASP)在多种应用中的可行性和协同效应，包括会话聊天机器人和虚拟实体推理器。
### Conclusion
s(CASP)通过目标导向的推理方法支持了一项关于可信AI的16+2项需求，提供了一种实现可信AI的新方法，这种方法能够在保持解释性和可靠性的同时，简化推理过程。
## 147. `cs.AI` - 人工智能红队 [PDF](https://arxiv.org/pdf/2507.05538), [HTML](https://arxiv.org/abs/2507.05538)
### Authors
Subhabrata Majumdar,Brian Pendleton,Abhishek Gupta
### Background
红队的概念起源于军事应用，随着网络安全和人工智能的发展，逐渐成为一种广泛采用的方法。目前，在人工智能治理方面，红队活动备受关注，但其与最初作为批判性思维练习的目的之间存在差距，尤其是与生成型人工智能上下文中的模型级漏洞发现的狭隘焦点之间的差距。现有的人工智能红队活动主要集中在单个模型的漏洞上，而忽视了模型、用户和环境之间复杂交互产生的更广泛的社技系统和涌现行为。
### Innovation
本文提出了一种全面框架，将红队活动操作化到AI系统的两个层面：宏观层面的系统红队活动贯穿于整个AI开发生命周期，微观层面的模型红队活动。基于网络安全经验与系统理论，本文还提出了六项建议，强调有效的人工智能红队活动需要多功能团队审查新兴风险、系统漏洞以及技术与社会因素之间的相互作用。
### Conclusion
本文批判性地探讨了人工智能红队活动，提出了一个新的框架和建议，旨在弥补当前实践中的不足，提升人工智能红队活动的效果。
## 148. `cs.AI` - NaviAgent: 基于工具导航图的双层规划方法在大规模工具生态系统中的调度 [PDF](https://arxiv.org/pdf/2506.19500), [HTML](https://arxiv.org/abs/2506.19500)
### Authors
Yan Jiang,Hao Zhou,LiZhong GU,Ai Han,TianLong Li
### Background
大规模语言模型（LLMs）已经展示了通过调用外部工具来执行任务的能力，超越了它们的静态知识。然而，现有的代理通常是以逐步调用工具的方式进行，缺乏对任务结构的整体视角。工具之间相互依赖，这导致了错误积累，并且在扩展到数千个工具时缺乏可扩展性。
### Innovation
本文提出了NaviAgent，一种新颖的双层架构，通过基于图的工具生态系统建模来解耦任务规划与工具执行。在任务规划层面，基于语言模型的代理能够决定直接响应、澄清用户意图、调用工具链或执行工具输出，确保独立于工具间复杂性的广泛交互场景覆盖。在执行层面，一个持续进化的工具世界导航模型（TWNM）编码工具间的结构和行为关系，指导代理生成可扩展且稳健的调用序列。通过整合真实的工具交互反馈，NaviAgent支持规划和执行的闭环优化，从简单的工具调用迈向适应性导航大规模工具生态系统。
### Conclusion
实验证明，NaviAgent在多种模型和任务中实现了最高的任务成功率，结合TWNM模型在复杂任务上的性能进一步提高了17个百分点，突显了其在工具链协调中的关键作用。
## 149. `cs.AI` - 为什么关系学习并没有主导世界？ [PDF](https://arxiv.org/pdf/2507.13558), [HTML](https://arxiv.org/abs/2507.13558)
### Authors
David Poole
### Background
目前的人工智能系统主要通过像素、词汇和音素来建模世界。然而，作者认为世界是由实体（如物体、事物，包括事件）及其属性和相互关系组成的，而不是简单的感知或描述。作者推测，之所以大部分数据处理集中在文本和图像上，是因为这些领域提供了大量有价值的数据。但实际上，许多公司最重要的数据是以表格、数据库和其他关系格式存在的，而不是以像素或文本的形式。作者指出，现有的机器学习基础教育和研究主要关注的是这些数据格式的简化形式，但在公司中存储的重要数据则包含不能简单解释为数字的产品代码、学生代码、交易代码等标识符，这些都是关系学习所关注的数据类型。
### Innovation
文章解释了为什么关系学习没有普及，并指出需要改进的领域，以提高其重要性，使其在实际应用中得到更加广泛的应用。
### Conclusion
关系学习尚未成为主流，主要原因在于其应用范围有限，且需要进一步的研究和发展来弥补当前仅限于有限关系的学习系统的不足，从而提升其在数据处理和分析中的重要地位。
## 150. `cs.AI` - 强化学习与蒸馏：理解LLM推理中的准确性和能力 [PDF](https://arxiv.org/pdf/2505.14216), [HTML](https://arxiv.org/abs/2505.14216)
### Authors
Minwu Kim,Anubhav Shrestha,Safal Shrestha,Aadim Nepal,Keith Ross
### Background
最近的研究表明，带可验证奖励的强化学习（RLVR）提高了整体准确度（pass@1），但在推理任务中的能力（pass@k）提升方面效果不明显，而蒸馏能同时提高这两方面。本研究旨在探究这些现象背后的机制。首先，RLVR在提高较简单问题的准确度的基础上牺牲了最难问题的准确度，难以提高整体能力。其次，RLVR不仅增加了较简单问题的成功概率，还在小模型设置中产生了原输出分布中没有的质量更高的响应，这些响应特征上既没有变得更长，也不包含更多反思相关关键词，暗示了需要更可靠的响应质量指标。再次，通过实验发现，即使蒸馏教师的回答也能解决同类问题时，能力也未必得到提升。研究推测，仅通过蒸馏推理模式只能提高准确度而不提升能力，牺牲难以问题的性能，这与RLVR相似。这些发现为理解RLVR和蒸馏如何影响LLM的推理行为提供了更清晰的认识。
### Innovation
研究探究了RLVR和蒸馏机制背后的差异，指出即使在小模型设置中，RLVR也能生成以前不存在的质量更高的响应，但这些响应只是改进了最易问题的准确度，而未引入新的知识，因此与蒸馏教师的指示相比，仅提高了准确度而未能提升能力；研究提出，仅通过蒸馏推理模式不能提升能力，这与RLVR表现相似，突出了准确度与能力在LLM中的不同提升机制，需要更可靠地衡量响应质量的方法。
### Conclusion
研究结果表明，即使对于简单的推理问题，RLVR也能生成新的高质量回应，但无法在最难问题上提高内置知识，需要更有效的指标来评估响应质量。相比之下，蒸馏是对已有的知识进行提炼，仅能提高准确度而无法引入新知识，这可能导致在最难问题上的性能下降。对这两种方法的理解为进一步优化LLM在推理任务中的表现提供了新的视角和方向。
## 151. `cs.AI` - HiRA：深入搜索中分离计划与执行的分层推理框架 [PDF](https://arxiv.org/pdf/2507.02652), [HTML](https://arxiv.org/abs/2507.02652)
### Authors
Jiajie Jin,Xiaoxi Li,Guanting Dong,Yuyao Zhang,Yutao Zhu,Yang Zhao,Hongjin Qian,Zhicheng Dou
### Background
现实世界中的复杂信息需求需要对多样化的数据源进行深入的推理和知识综合，而传统的检索增强生成(RAG)流水线难以有效应对。现有的基于推理的方法存在一个根本性的局限：它们使用单一模型同时处理高级计划和详细执行，这导致推理效率低下，且扩展性有限。由于这一问题，这些方法在处理多步骤的信息搜寻任务时面临挑战，效果不尽人意。
### Innovation
本文提出了一种分层框架HiRA，该框架将战略规划与专业化执行分离。HiRA将复杂的搜索任务分解为专注于具体子任务，每个子任务分配给具有外部工具和推理能力的特定领域代理，并通过结构化的集成机制协调结果。这种分离方法避免了执行细节干扰高级推理，同时使系统能够利用不同类型的专门知识进行信息处理。实验结果表明，HiRA在四个复杂的、跨模态的深度搜索基准数据集上显著优于现有的RAG和基于代理的方法，在答案质量和系统效率方面都取得了提升，突显了分离规划和执行对于多步骤信息搜寻任务的有效性。
### Conclusion
实验结果显示，HiRA在四个复杂的、跨模态的深度搜索基准数据集上显著优于现有的RAG和基于代理的方法，分别在答案质量和系统效率方面都取得了提升，证明了分离规划和执行对于多步骤信息搜寻任务的有效性。
## 152. `cs.AI` - 社会和行为科学中的人工智能代理：历史和发展前景 [PDF](https://arxiv.org/pdf/2510.05743), [HTML](https://arxiv.org/abs/2510.05743)
### Authors
Petter Holme,Milena Tsvetkova
### Background
本文回顾了自20世纪50年代以来人工智能代理（代理型AI）在社会和行为科学中的历史发展和当前趋势。从最早的可编程计算机和社会模拟，到今天的大型语言模型实验。文章强调了AI在这个科学过程中的作用以及由技术进步和科学本身从1950年至今的发展所带来的变化。具体涵盖的主题包括：向一个不了解计算机的世界展示第一项社会模拟研究时所面临的挑战、社会系统科学的兴起、智能博弈论代理、大数据时代及其对知识体系的颠覆，以及目前对生成型AI应用的热烈追捧等诸多话题。贯穿始终的主题是我们与用于理解自己的技术之间的深厚联系。
### Innovation
文章通过对人工智能代理在社会和行为科学中的发展历程进行梳理，特别强调了技术进步对科学研究的影响以及科学发展过程中的重要变化。通过对不同阶段社会模拟研究、智能代理、大数据时代及其对知识体系影响的研究，文章创新性地展示了从早期计算机到当今AI技术应用的广泛影响和前景展望。
### Conclusion
文章总结了人工智能代理在社会和行为科学中的重要角色和深远影响，并展望了未来研究和发展方向。文章指出，技术发展深刻地影响着人类对自身的理解和认知，而未来的研究需要持续关注技术与社会之间的互动关系。
## 153. `cs.AI` - 超越像素：探索基于DOM降采样的LLM-web代理 [PDF](https://arxiv.org/pdf/2508.04412), [HTML](https://arxiv.org/abs/2508.04412)
### Authors
Thassilo M. Schiepanski,Nicholas Piël
### Background
前沿的语言模型仅最近才使自主网络代理成为可能。这些模型充当瞬时领域模型后端。在建议交互时，它们会被咨询网络任务以及相应的应用程序状态。关键问题在于应用状态的序列化，这被称为快照。最先进的网络代理依赖于物理窗口的快照，即带有视觉线索的屏幕截图。这些靠图像作为模型输入的相对便宜的方式。尽管语言模型的视觉功能仍然落后于代码解释能力，但DOM快照，具有结构类似HTML的特点，提供了一种替代方式。然而，由于模型输入的大量标记，到目前为止，DOM快照的可靠实现对网络代理来说仍不可行。
### Innovation
我们提出了一种名为D2Snap的首创DOM降采样算法，基于GPT-4o后端。我们对D2Snap在Online-Mind2Web数据集上进行任务评估。D2Snap降采样后的DOM快照（成功率67%）与基于物理窗口快照的基线（65%）相当，这在相同输入标记数量级（1e3）内达到。我们最佳评估配置在模型上下文窗口之上，但不超过的，在输入标记数量级上优于该基线8%。评估结果显示，DOM固有的层次结构对LLM而言是一种强大的UI特征。
### Conclusion
D2Snap算法能够在保持较高交互成功率的同时，提供一种可靠的VE（Visual Environment）输入方式，从而提升LLM在web代理中的应用效果。
## 154. `cs.AI` - BuildArena：物理学对齐的LLM工程建造交互式基准 [PDF](https://arxiv.org/pdf/2510.16559), [HTML](https://arxiv.org/abs/2510.16559)
### Authors
Tian Xia,Tianrun Gao,Wenhao Deng,Long Wei,Xiaowei Qian,Yixian Jiang,Chenglei Yu,Tailin Wu
### Background
工程建造自动化旨在将自然语言规范转化为物理上可行的结构，这要求在严格的物理限制下进行复杂的综合推理。虽然现代大型语言模型拥有广泛的知识和强大的推理能力，使其成为这一领域的有潜力的候选人，但它们在工程建造领域的应用能力尚未得到充分评估。因此，亟需一种能够评估并比较现代大型语言模型在语言驱动工程建造中的性能的基准工具。
### Innovation
BuildArena 是首个专门针对语言驱动工程建造设计的物理学对齐交互式基准。它包括四个创新点：（1）提供一个高度可定制的基准框架，以便深入比较和分析大型语言模型；（2）跨多个难度层级设计包括静力学和动力学的扩展性任务；（3）提供一个3D空间几何计算库，支持基于语言指令的建造；（4）设置一套基础性的工作流程，有助于评估不同模型在语言驱动和物理导向的建造自动化中的能力。在八种前沿的大型语言模型上，BuildArena 全面评估了它们在这方面的性能。
### Conclusion
BuildArena 对大型语言模型在语言驱动工程建造中的能力进行了首次全面评估，为该领域的发展提供了重要基准和工具。
## 155. `cs.AI` - 通过实现出现的认知趋同：反映四种心智理论的结构回路 [PDF](https://arxiv.org/pdf/2507.16184), [HTML](https://arxiv.org/abs/2507.16184)
### Authors
Myung Ho Kim
### Background
论文背景介绍了一个名为Agentic Flow的实用AI架构，其设计目的是解决大型语言模型（LLMs）的局限性。Agentic Flow由五个相互嵌套的模块组成：检索、认知、控制、记忆和行动。尽管最初的灵感仅来源于Minsky和Clark的心智理论，但后续分析发现其结构与Kahneman的双系统理论、Friston的预测加工理论以及Minsky的社会心智理论中的计算模式不谋而合。这表明理论上的趋同可以自然地从执行需求中产生，而不仅仅是出于刻意的综合。实验结果表明，结构化的代理在任务成功率为95.8%，远高于基线LLMs的62.3%，证明了其强大的约束能力和可重复推理能力。这些发现促使研究者提出一种更广泛的描述性元架构PEACE，强调重复的设计模式，如预测建模、关联回忆和误差敏感控制等。这些原则后来被综合为一种结构认知回路（SCL）框架，用作LLM基代理行为智能的理论基础。论文旨在展示认知形式的统一可能不是从抽象中产生的，而是由现实世界推理的需求而形成的。
### Innovation
Agentic Flow架构的设计结合了四种重要的心智理论（Kahneman的双系统理论、Friston的预测加工、Minsky的社会心智理论和Clark的扩展心智理论），形成了一个统一的结构模型。尽管最初设计仅受Minsky与Clark理论的启发，但分析揭示出它意外地融入了所有四种理论的计算模式。结构化代理在任务成功率上的显著改进证明了这种理论趋同的有效性。作者提出，智能架构可能通过实际限制自然地趋向于共享的结构模式，而非基于理论上的统一。结构认知回路（SCL）作为一种通用框架，进一步支持了基于LLM的代理的行为智能。
### Conclusion
本文提出了一种对四种心智理论趋同的解释。Agentic Flow架构和结构认知回路（SCL）展示了认知形式如何在实际推理需求而非抽象理论中统一。作者强调这种趋同是反思性的，旨在邀请进一步的理论和实验对话。该研究揭示了统一认知形态的实现可能来源于实际的约束而非抽象的概念，为未来的智能架构设计提供了新的视角。
## 156. `cs.AI` - RELATE：一种多模态关系图的无模式感知自注意力编码器 [PDF](https://arxiv.org/pdf/2510.19954), [HTML](https://arxiv.org/abs/2510.19954)
### Authors
Joe Meyer,Divyansha Lachi,Mahmoud Mohammadi,Roshan Reddy Upendra,Eva L. Dyer,Mark Li,Tom Palczewski
### Background
关系多表数据在电子商务、医疗健康和科学研究等多个领域中很常见，可以自然地表示为具有多模态节点属性的异构时间图。现有的图神经网络（GNNs）依赖于特定于模式的特征编码器，需要为每种节点类型和特征列创建单独的模块，这阻碍了可扩展性和参数共享能力。
### Innovation
RELATE（关系编码器）是一个无模式感知的即插即用特征编码器，可以与任何通用图神经网络一起使用。它采用了共享模态特定编码器来处理分类、数值、文本和时间属性，随后通过类似于Perceiver的交叉注意模块，将特征聚合为一个固定大小且对交换不变的节点表示。在RelBench基准上对RELATE进行评估，结果表明RELATE在性能上与特定于模式的编码器相差不到3%，同时参数数量降低了最多5倍。这种设计支持多种模式，并可实现通用图神经网络的多数据集预训练，为关系图数据领域奠定基础模型的基础。
### Conclusion
RELATE设计支持变化的模式，使得通用图神经网络能够进行多数据集预训练，为关系图数据领域提供了基础模型的发展之路。
## 157. `cs.AI` - 持续视觉语言导航 [PDF](https://arxiv.org/pdf/2403.15049), [HTML](https://arxiv.org/abs/2403.15049)
### Authors
Seongjun Jeong,Gi-Cheon Kang,Seongho Choi,Joochan Kim,Byoung-Tak Zhang
### Background
当前的视觉语言导航(VLN)代理通常采用一次性训练与部署的策略，这在实际应用中是不现实的，因为部署的代理不得不不断遇到新的环境。现有的持续学习方法在这类问题上表现不佳。
### Innovation
本文提出了持续视觉语言导航(CVLN)框架，该框架允许代理在一个或多个场景域中增量学习和适应。文章还引入了两种简单的辅助基准方法：困惑度重播(PerpR)和 episodic 自我重播(ESR)，这两种方法能够在训练过程中更好地利用回忆库。
### Conclusion
现有持续学习方法在 CVLN 上表现不佳，而 PerpR 和 ESR 能够通过高效地利用回忆库取得更好的性能。
## 158. `cs.AI` - AI科学家的研究现状 [PDF](https://arxiv.org/pdf/2510.23045), [HTML](https://arxiv.org/abs/2510.23045)
### Authors
Guiyao Tie,Pan Zhou,Lichao Sun
### Background
人工智能正处于从计算工具向自主创造科学知识的转变过程中。这种新兴的范式——AI科学家，旨在模拟完整的科学工作流程——从初始假设生成到最后可发表研究结果的综合，有望从根本上重塑发现的速度和规模。然而，这些系统的迅速和无序扩张导致了科研领域的碎片化，模糊了总体方法论原则和开发趋势。本文通过引入一个统一的六阶段方法论框架，系统地对AI科学家领域进行了综合分析，将整个科学过程分解为文献综述、想法生成、实验准备、实验执行、科学写作和论文生成等多个步骤。
### Innovation
本文提出了一个统一的、六阶段的方法论框架，将整个科学过程分解为六个步骤，分别为文献综述、想法生成、实验准备、实验执行、科学写作和论文生成。通过这个分析视角，作者绘制了该领域从早期基础模块(2022-2023)到集成闭环系统(2024)，再到当前规模、影响和人机协作前沿(2025至今)的演变轨迹。
### Conclusion
通过对这些发展的严格综合，本文不仅澄清了自主科学的现状，还为解决稳健性和治理方面的剩余挑战提供了关键的指导路径，最终引导下一代系统成为值得信赖且不可或缺的人类科学研究伙伴。
## 159. `cs.AI` - 理解机器人与人工智能中效용理论的应用：一项综述 [PDF](https://arxiv.org/pdf/2306.09445), [HTML](https://arxiv.org/abs/2306.09445)
### Authors
Qin Yang,Rui Liu
### Background
效用作为一种经济学、博弈论、运筹学以及机器人与人工智能领域的核心概念，被用来评估个体的需求、偏好和利益水平。尤其是在多智能体系统（MAS）或多机器人系统（MRS）的决策和学习中，适用的效用模型可以指导代理选择合理的策略来满足当前需求，并学习合作和组织行为，优化系统效用，建立稳定、可靠的关系，并确保每个团队成员的可持续发展，类似于人类社会。尽管这些系统的复杂、大规模和长期行为很大程度上受到基本关系特性的驱动，但在机器人和人工智能领域的理论机制和应用方面讨论较少，特别是系统行为的复杂性、规模和长期性对基本关系特性的强烈依赖性
### Innovation
本文引入了以效用为核心的需要范式，用于描述和评估智能体交互中的内和外关系。基于相关领域的现有文献，提出了几个有前景的研究方向，并指出了进一步调查所需解决的一些开放问题
### Conclusion
本文通过引入以效用为核心的需要范式，对机器人与人工智能中效用理论的应用进行了综述，总结了现有研究，提出了若干研究方向，并指出了需要进一步研究的开放问题，旨在推动该领域的发展
## 160. `cs.AI` - 迈向利用高级算法挖掘可解释模型的可信AI形式化 [PDF](https://arxiv.org/pdf/2510.20621), [HTML](https://arxiv.org/abs/2510.20621)
### Authors
Riccardo Guidotti,Martina Cinquini,Marta Marchiori Manerba,Mattia Setzu,Francesco Spinnato
### Background
可解释的自动化决策模型对于提高信任、问责制和安全应用至关重要。本文正式定义了MIMOSA框架，旨在生成在可解释性和性能之间达到平衡的预测模型，并嵌入关键伦理属性。该研究涵盖了各种决策任务和数据类型，如表格数据、时间序列、图像、文本、交易和轨迹。此外，该研究还界定了三大类可解释模型：特征重要性模型、规则模型和实例模型。对于每类模型，都分析了其可解释性维度、推理机制和复杂性。此外，该研究还正式界定了因果性、公平性和隐私性这三个关键伦理属性，并提供了相应的评估指标和验证程序。
### Innovation
正式化了一个名为MIMOSA的框架，该框架提供了一个全面的方法来生成在可解释性和性能之间达到平衡的预测模型，同时嵌入关键的伦理属性。该研究进一步界定了三种主要的可解释模型类别，并分析了它们的可解释性维度、推理机制和复杂性。此外，还提出了评估公平性、隐私性和因果性的正式定义、评估指标和验证程序，探讨了这些属性之间的内在权衡，并讨论了如何将隐私要求、公平约束和因果推理嵌入到可解释的管道中。
### Conclusion
通过在模型生成过程中评估伦理措施，该框架建立了开发不仅准确且可解释，而且公平、隐私保护和因果意识强的AI系统的理论基础，使其成为值得信赖的AI系统。
## 161. `cs.AI` - 大型语言模型中的规范推理：从逻辑和模态视角的比较基准 [PDF](https://arxiv.org/pdf/2510.26606), [HTML](https://arxiv.org/abs/2510.26606)
### Authors
Kentaro Ozeki,Risako Ando,Takanobu Morishita,Hirohiko Abe,Koji Mineshima,Mitsuhiro Okada
### Background
规范推理涉及规范或道义模态，例如义务和许可。尽管大型语言模型（LLMs）在各种推理任务中表现出色，但在处理规范推理方面的能力尚未得到充分探索。本研究从逻辑和模态的角度系统评估了LLMs在规范领域中的推理能力，通过将LLMs在规范模态上的推理与在认识论模态上的推理进行比较来考察其推理能力，后者拥有一个共同的形式结构。此外，还引入了一个新的数据集，涵盖了规范和认识论推理领域中的广泛形式推理模式，并结合了影响人类推理的非形式认知因素。研究结果显示，尽管LLMs通常遵循有效的推理模式，但在特定类型的规范推理中仍然表现出显著的不一致性和认知偏差，这与心理学研究中对人类推理的观察相似。这些发现揭示了在LLMs中的规范推理实现逻辑一致性的挑战，并提供了提高其可靠性的见解。
### Innovation
本研究首次从逻辑和模态视角系统评估了LLMs在规范推理中的能力，引入了一个覆盖规范和认识论推理广泛形式推理模式的新数据集，并结合了影响人类推理的非形式认知因素。通过将LLMs的规范模态推理与认识论模态推理进行对比分析，旨在评估其推理能力。研究结果揭示了LLMs在规范推理中的逻辑一致性和认知偏差，并提供了进一步提升其可靠性的见解。
### Conclusion
虽然LLMs通常遵循有效的推理模式，但在特定类型的规范推理中仍表现出显著的不一致性和认知偏差，这揭示了在LLMs中的规范推理实现逻辑一致性的挑战。研究提供了进一步提高LLMs在规范推理中可靠性的洞察，同时也建议进一步改善其逻辑推理的一致性。所有数据和代码已公开发布。
## 162. `cs.AI` - RepoMasterEval：通过真实仓库评估代码补全 [PDF](https://arxiv.org/pdf/2408.03519), [HTML](https://arxiv.org/abs/2408.03519)
### Authors
Qinyun Wu,Chao Peng,Pengfei Gao,Ruida Hu,Haoyu Gan,Bo Jiang,Jinhe Tang,Zhiwen Deng,Zhanming Guan,Cuiyun Gao,Xia Liu,Ping Yang
### Background
随着对自动化代码补全工具在软件开发中的依赖性增加，全面的评估基准变得尤为重要。现有的基准主要集中于函数和类级别的代码补全，依赖于文本描述来提示模型，但这种提示方式在实际开发中并不常见，代码补全可能发生在函数或代码块的任何地方。这些限制使得现有的评估基准与代码补全工具的实际应用场景不匹配。
### Innovation
本文提出了RepoMasterEval，这是一个基于真实世界仓库构建的新基准，用于评估代码补全模型。每个基准数据集通过从源代码文件中删除代码片段（基准事实）并使用现有测试套件生成。为了提高模型生成代码的测试准确性，采用变异测试评估测试用例的有效性，并针对低变异分数的手动制定新的测试用例。我们的实验结果表明，提供测试论据对于提高基准的准确性至关重要，RepoMasterEval能够反映模型在实际场景中的性能差异。此外，RepoMasterEval的应用还显示它对于提升模型训练过程中的反馈质量非常有用，其评分与模型的实际表现高度相关。
### Conclusion
我们的实验证明，测试质量对基准的准确性至关重要，RepoMasterEval能够在真实世界场景中有效评估代码补全模型的性能，并且其评估结果与实际模型表现高度相关，适用于指导模型训练过程。
## 163. `cs.AI` - 代表性的社会选择：从学习理论到AI对齐 [PDF](https://arxiv.org/pdf/2410.23953), [HTML](https://arxiv.org/abs/2410.23953)
### Authors
Tianyi Qiu
### Background
社会选择理论研究群体对偏好聚合的分析，应用于人类代理的机制设计以及语言模型的民主对齐。在这些情况下，当涉及的议题和个体数量庞大时，机制难以直接考虑所有偏好。这种大规模的偏好聚合在许多实际决策过程中都广泛存在，例如陪审团审判、立法、公司治理以及最近的语言模型对齐。在代表性的社会选择中，通过基于有限的个体-议题对样本进行社会选择决策。大多数关于代表性的社会选择最深的问题可以被定义为统计学习问题，并通过机器学习理论证明了社会选择机制的一般化性质。
### Innovation
提出了代表性的社会选择框架，将社会选择、学习理论和AI对齐领域相结合。该框架通过基于有限样本进行社会选择决策来解决大规模偏好聚合问题。此外，该研究将社会选择问题转化为统计学习问题，并利用机器学习理论证明了社会选择机制的一般化性质。该框架还引入了几类新的组合分析工具来证明阿罗不可能定理。
### Conclusion
该框架不仅为研究提供了新的视角，还为社会选择、机器学习和AI对齐交叉领域的未来研究打开了方向。
## 164. `cs.AI` - 时空图神经网络模型在时间序列预测和分类中的系统文献综述 [PDF](https://arxiv.org/pdf/2410.22377), [HTML](https://arxiv.org/abs/2410.22377)
### Authors
Flavio Corradini,Flavio Gerosa,Marco Gori,Carlo Lucheroni,Marco Piangerelli,Martina Zannotti
### Background
近年来，时空图神经网络（GNNs）在时间序列分析领域引起了广泛关注，由于其能够同时捕捉变量之间和时间点之间的依赖性。这篇综述文章旨在全面回顾时空GNNs在时间序列分类和预测中的各种建模方法和应用场景。为了实现这一目标，进行了数据库搜索，最终选出了366篇论文进行详细分析，以全面评估当前的技术前沿。这些分析旨在为读者提供一个全面的综述，包括模型、相关代码链接、可用数据集、基准模型以及拟合结果。所有这些信息都有助于研究者的研究工作。此前，这可能是第一个也是最全面的系统文献综述，详细比较了当前不同领域应用的时空GNN模型的结果。
### Innovation
这是第一个全面且广泛地系统文献综述，详细比较了应用到不同领域的当前时空GNN模型的结果。综述还讨论了时空GNN应用中的现有限制和挑战，如可比性、可重复性、可解释性、信息容量差和扩展性问题，并提供了GitHub仓库以提供进一步探索的研究工具。
### Conclusion
该综述文章提供了时空GNN在时间序列预测和分类中的当前研究状态，指出了研究中的现有挑战，并通过GitHub仓库提供了额外的交互工具，以进一步探索所呈现的结果。
## 165. `cs.AI` - MindSearch: 模拟人的思维揭示深层AI搜索引擎 [PDF](https://arxiv.org/pdf/2407.20183), [HTML](https://arxiv.org/abs/2407.20183)
### Authors
Zehui Chen,Kuikun Liu,Qiuchen Wang,Jiangning Liu,Wenwei Zhang,Kai Chen,Feng Zhao
### Background
信息搜索和整合是一个复杂的认知任务，耗时且费力。尽管大型语言模型取得了显著进展，但将这些模型与搜索引擎结合使用的方法仍然无法很好地解决这一问题，主要由于三个挑战：(1) 复杂请求无法被搜索引擎准确且完整地检索；(2) 需要整合的相关信息分布在多个网页中，并伴随大量噪声；(3) 大量包含长内容的网页会导致超过LLM的最大上下文长度限制。受人类解决这些挑战时的认知过程的启发，本文提出了MindSearch，旨在通过简单的基于LLM的多智能体框架来模仿人类在网页信息搜索和整合中的思维过程。
### Innovation
MindSearch 采用了多智能体设计，能够同时从大量网页中并行搜索和整合信息。它将用户查询分解为图中的原子子问题节点，并根据WebSearcher的搜索结果逐步扩展图，从而模拟了人类多步信息搜索的认知过程。每个子问题由WebSearcher执行分层次的信息检索，并收集信息供WebPlanner使用。这种方法显著提高了响应的质量，并证明了MindSearch对于封闭式和开放式问答问题的回答在深度和广度上都优于其他方法。
### Conclusion
MindSearch 在信息搜索和整合方面展示了显著改进，特别是在响应质量和效率方面。基于InternLM2.5-7B的MindSearch 的响应更受人类偏好，表明它已经可以提供与专有AI搜索引擎相当的解决方案。
## 166. `cs.AI` - LIBMoE: 一个用于大规模语言模型中混合专家综合基准测试的库 [PDF](https://arxiv.org/pdf/2411.00918), [HTML](https://arxiv.org/abs/2411.00918)
### Authors
Nam V. Nguyen,Thong T. Doan,Luong Tran,Van Nguyen,Quang Pham
### Background
混合专家（MoE）架构已成为扩展的重要基石，并且在许多大型语言模型（如GPT-OSS、DeepSeek-V3、Llama-4和Gemini-2.5）中是关键组件。然而，由于训练和评估的高昂计算成本，系统性的MoE研究受到了限制，这限制了大多数研究人员能够进行的大规模研究。
### Innovation
引入了LibMoE，这是一个统一框架，支持MoE的研究可重复性、高效性和可扩展性，适用于预训练和稀疏-上转换。除了统一实现之外，框架还提供了透明的分析工具，用于探测路由和专家动态。利用这一基础，进行了三个维度的全面分析：（一）路由动态，包括专家选择模式、路由稳定性和最优性，以及路由熵如何揭示任务专业化和专家多样性；（二）轻量级初始化对负载平衡的影响，展示细微改变路由器初始化如何影响早期专家的利用情况；（三）训练制度差异，揭示稀疏-上转换和全预训练表现出不同的路由模式和稳定性特征。LibMoE通过降低门槛和标准化评估，以及全面分析，拓宽了MoE研究的范围，建立了可靠的基准以指导未来创新。
### Conclusion
LibMoE 放宽了对 MoE 研究的访问，为未来的创新奠定了可靠基准，从而推动 MoE 领域的发展。
## 167. `cs.AI` - 面向以人为本研究的训练数据归属用户导向的可解释人工智能 [PDF](https://arxiv.org/pdf/2409.16978), [HTML](https://arxiv.org/abs/2409.16978)
### Authors
Elisa Nguyen,Johannes Bertram,Evgenii Kortukov,Jean Y. Song,Seong Joon Oh
### Background
可解释的人工智能(XAI)旨在使人工智能系统更加透明，然而许多实践过于注重数学严谨性而忽视了用户的实际需求。训练数据归属(TDA)是一个新兴的XAI领域，如果没有用户中心的方法，它可能重复其他子领域已知的解决方案模式。尽管如此，在TDA的早期阶段中，通过用户中心的方法进行方向塑造有着极大的价值。本研究直接与机器学习开发者通过需要发现访谈研究(N=6)和基于场景的互动用户研究(N=31)展开合作，以将解释与实际工作流程结合起来。
### Innovation
本研究提出了一种基于设计思维过程的方法来解决训练数据归属问题，这一方法能够在XAI领域尤其是TDA子领域中为研究者提供一种用户导向的新型任务，这将加强他们的研究实际相关性和人类影响。这种研究方法基于实际工作流程，发现了新的数据导向的解释任务，能够帮助开发者更好地理解模型行为。
### Conclusion
本研究建议TDA、XAI和HCI社区共同参与这些新任务的研究，通过这种方式可以增强他们的研究实际相关性和对人类的影响。
## 168. `cs.AI` - SparsePO：通过稀疏 token 面罩控制 LLM 的偏好对齐 [PDF](https://arxiv.org/pdf/2410.05102), [HTML](https://arxiv.org/abs/2410.05102)
### Authors
Fenia Christopoulou,Ronald Cardenas,Gerasimos Lampouras,Haitham Bou-Ammar,Jun Wang
### Background
直接对齐算法已被证明是将语言模型与人类期望的行为对齐的有效步骤。当前直接偏好优化目标的变体专注于一个严格的设置，即所有令牌都作为 KL 散度和奖励信号贡献到损失函数中。然而，人类的偏好并不受每个单词序列的均衡影响，而是通常依赖于特定的单词或短语，例如存在有毒术语会导致不受欢迎的响应。基于这一观察，本文认为在优化期间所有令牌不应被等权重对待，并提出了一种名为 SparsePO 的灵活目标，旨在自动学习在优化训练期间为每个令牌学习 KL 散度和奖励的权重。本研究提出了两种不同的权重面罩变体，可以从参考模型本身或在训练中实时学习得到。值得注意的是，我们的方法会诱导学习出稀疏的面罩，在学习如何在令牌级别平衡奖励和 KL 散度贡献方面，选择最佳水平的面罩稀疏度。并进行了详尽的实验以证明该方法在对齐偏好代理方面的有效性，包括情感控制、有用性和无害性，以及摘要质量。这一方法在摘要和对话场景中分别获得了 +10% 和 +3% 的胜利点数，没有损害模型推理或摘要响应的相关性和忠实度.
### Innovation
本文提出了一种称为 SparsePO 的灵活目标，旨在自动学习在优化训练期间为每个令牌学习 KL 散度和奖励的权重。本文还提出了两个不同的权重面罩变体，可以从参考模型本身或在训练中实时学习得到。研究表明，这种方法可以有效地对语言模型进行偏好对齐，特别是在情感控制、有用性和无害性，以及摘要质量方面表现出色，并且在摘要和对话场景中取得了 +10% 和 +3% 的胜利点数，没有损害模型推理或摘要响应的相关性和忠实度。
### Conclusion
本文提出的 SparsePO 方法通过学习自动调整每个令牌的权重，更加灵活地控制语言模型与人类期望的行为之间的偏好对齐。实验证明，SparsePO 可以提升多个方面的性能，且不会影响模型的核心性能。
## 169. `cs.AI` - 印度语言多语言状态空间模型在结构化问题回答中的应用 [PDF](https://arxiv.org/pdf/2502.01673), [HTML](https://arxiv.org/abs/2502.01673)
### Authors
Arpita Vats,Rahul Raja,Mrinal Mathur,Vinija Jain,Aman Chadha
### Background
印度语言的多样性和复杂性为自然语言处理（NLP）任务，尤其是问答任务（QA）带来了独特的挑战。现有的NLP技术在处理印度语言特有的丰富形态、复杂语法和语境细微之处时存在局限性。
### Innovation
本文探索了状态空间模型（SSMs）在印度语言问答系统中的应用。通过多个SSM架构在不同印度语言数据集上的评估，并进行性能比较，研究结果表明，这些模型在问题解释、语境对齐和答案生成方面具有显著优势。这是首次将SSMs应用于印度语言的问答任务，为这一领域的未来研究建立了基础基准。
### Conclusion
本文提出对现有SSM框架的改进，以优化其在低资源环境和多语言场景中的应用，为印度语言领域的进一步研究奠定了基础。
## 170. `cs.AI` - 使用线性结构化 f-散度正则化的鲁棒离线强化学习 [PDF](https://arxiv.org/pdf/2411.18612), [HTML](https://arxiv.org/abs/2411.18612)
### Authors
Cheng Tang,Zhishuai Liu,Pan Xu
### Background
现有方法主要使用无结构正则化，可能导致在假定的过渡动态下策略过于保守。文章针对这一局限性，提出了鲁棒正则化马尔可夫决策过程（$d$-RRMDP）框架，通过将正则化和过渡动态结构化，旨在学习在动态变化环境下鲁棒的策略。该研究集中在离线强化学习中，即学习者从名义环境中的预收集数据集中学习策略。文章开发了鲁棒正则悲观价值迭代（R2PVI）算法，使用线性函数逼近来学习 $d$-RRMDP中的鲁棒策略，并使用基于转移核的 $f$-散度正则化术语。
### Innovation
文章提出了 $d$-矩形线性 RRMDP 框架，将潜在的结构引入转移核和正则化项中。基于此，开发了鲁棒正则悲观价值迭代（R2PVI）算法，该算法使用线性函数逼近来进行在 $f$-散度正则化下的鲁棒策略学习，并提供了R2PVI策略的实例相关上界，表明这些上界受到数据集覆盖最优鲁棒策略下所访问的状态-动作空间的最佳稳健转移方式的影响。最后，通过信息论下的下界验证了算法的有效性，且数值实验表明R2PVI能够学习到鲁棒策略，相比基础方法展现出更高的计算效率。
### Conclusion
文章的结论是，通过引入 $d$-RRMDP和R2PVI算法，能够提高策略的鲁棒性，并且在计算效率方面具有优势。进一步的实验证明了这些方法的有效性和优越性。
## 171. `cs.AI` - SafeAgentBench: 一个保障实体LLM代理安全任务规划的基准 [PDF](https://arxiv.org/pdf/2412.13178), [HTML](https://arxiv.org/abs/2412.13178)
### Authors
Sheng Yin,Xianghe Pang,Yuanzhuo Ding,Menglan Chen,Yutong Bi,Yichen Xiong,Wenhao Huang,Zhen Xiang,Jing Shao,Siheng Chen
### Background
随着大型语言模型（LLMs）的融合，实体代理具有强大的理解与规划复杂自然语言指令的能力。然而，一个可预见的问题是这些实体代理可能完美地执行危险任务，这可能会在真实世界中造成损害。现有的基准测试主要忽视了关键的安全风险，仅关注计划性能，而少数则仅在非交互图像-文本数据上评估LLM的安全意识。因此，提出了SafeAgentBench——首个用于交互模拟环境中具有安全意识的实体LLM代理任务规划的全面基准，涵盖了显性和隐性危险。该基准包括：1. 750个多样化且高质量的任务集，严格编纂以涵盖10种潜在危害和3种任务类型；2. SafeAgentEnv，一个通用的实体环境，带有低级控制器，支持多agent执行，包含17种高级动作，适配9种最新的基线模型；3. 从执行和语义两个方面进行可靠评估的方法。实验结果表明，尽管不同设计框架的代理在任务成功率上存在显著差异，但在整体安全意识方面仍较弱。最安全的基线对详细的危险任务的拒绝率也仅为10%。此外，简单替换驱动代理的LLM并不会显著改善其安全意识。
### Innovation
SafeAgentBench 是首个针对交互模拟环境中安全意识的任务规划实体LLM代理的全面测试基准，涵盖了显性和隐性危险。该基准包括一个多样化且高质量的任务集、一个通用的实体环境和可靠的评估方法。它解决了现有基准测试忽视关键安全风险的问题。
### Conclusion
虽然不同设计框架的实体代理在任务成功率上存在显著差异，但它们的整体安全意识仍然较弱。最安全的基线对详细的危险任务的拒绝率也仅为10%。简单替换驱动作代理的LLM并不会显著改善安全意识。
## 172. `cs.AI` - 训练一个普遍好奇的智能体 [PDF](https://arxiv.org/pdf/2502.17543), [HTML](https://arxiv.org/abs/2502.17543)
### Authors
Fahim Tajwar,Yiding Jiang,Abitha Thankaraj,Sumaita Sadia Rahman,J Zico Kolter,Jeff Schneider,Ruslan Salakhutdinov
### Background
高效的探索对于智能系统与环境交互至关重要，但现有的语言模型在需要策略性信息收集的场景下往往表现不佳。
### Innovation
本文提出了Paprika，这是一种微调方法，使语言模型能够发展出不受特定环境限制的一般决策能力。通过在不同任务的合成交互数据上进行训练，这些任务要求不同的策略，Paprika教会模型根据环境反馈在新任务中探索并调整其行为，而无需更多的梯度更新。实验结果显示，使用Paprika微调的语言模型能够在不进行额外训练的情况下，有效地将所学的决策能力转移到全新的任务中。与传统的训练方法不同，我们方法的主要瓶颈在于使用有益的交互数据而不是模型更新。
### Conclusion
这些结果表明，朝着能够自主解决需要与外界交互的新型序列决策问题的AI系统，这种路径具有前景。
## 173. `cs.AI` - 大规模语言模型通过自信心实现可扩展的最佳-of-N 选择 [PDF](https://arxiv.org/pdf/2502.18581), [HTML](https://arxiv.org/abs/2502.18581)
### Authors
Zhewei Kang,Xuandong Zhao,Dawn Song
### Background
最佳-of-N 选择是一种通过增加测试时间计算来提高大型语言模型推断性能的关键技术。当前最先进的方法通常使用计算密集型奖励模型进行响应评估和选择。然而，无奖励替代方法如自我一致性或通用自我一致性，在处理开放生成任务方面能力有限，且难以有效扩展。
### Innovation
本文提出了自信心，这是一种利用大型语言模型输出固有的概率分布来估计响应质量的新颖且高效的指标。它不依赖于外部奖励模型，并且证明了与奖励模型相比，自信心可以在增加样本数量时有效扩展，同时保持性能。此外，自信心可以辅助思维链，超越贪婪解码提升推理性能，并且在传统自我一致性方法无法胜任的开放生成任务中表现良好。
### Conclusion
研究结果表明，自信心是提高大型语言模型推理能力的一个实用且高效的方法。代码已在GitHub上提供。
## 174. `cs.AI` - ChatGPT和Claude在伦理困境中决策偏见的比较研究 [PDF](https://arxiv.org/pdf/2501.10484), [HTML](https://arxiv.org/abs/2501.10484)
### Authors
Wentao Xu,Yile Yan,Yuqi Zhu
### Background
近年来，大语言模型（LLMs）的进步使得它们在各种任务中的响应接近人类表现，引发了对它们在伦理决策和潜在偏见方面能力的质疑。这项研究系统地评估了九种流行的LLMs（开源和闭源）在涉及受保护属性的伦理困境中的表现。研究覆盖了跨越单一和交叉属性组合的50,400次试验，在四个情境下（保护性 vs. 危害性），评估模型的伦理偏好、敏感性、稳定性及聚类模式。研究结果揭示了所有模型在受保护属性上的显著偏见，并且不同模型类型和情境下的偏好有所不同。此外，研究还发现在不同类型的伦理困境中，LLMs的伦理行为表现各异：保护性情境中模型表现出一致性模式，但在危害情境中则表现出更加多样化和认知要求高的决策。模型在交叉条件下的伦理倾向更加明显，表明复杂输入揭示了更深层次的偏见。这些发现强调了对LLMs伦理行为的多维度、情境感知评估的重要性，并提供了一种系统的方法来理解并解决LLMs决策中的公平性问题。
### Innovation
该研究首次系统性地评估了多种流行的LLMs在涉及受保护属性的伦理困境中的表现，揭示了不同模型类型的伦理偏好和差异性敏感性，特别是在保护性 vs. 危害性情境下。此外，研究还发现模型在交叉条件下的伦理倾向更加显著，这有助于理解复杂输入如何揭示更深层次的偏见。该研究提供了一种系统的方法来评估和理解LLMs在决策中的公平性，并提出了针对这些模型的公平性问题的理解和解决策略。
### Conclusion
研究结果表明，所有模型在受保护属性上都存在显著偏见，且不同模型类型和情境下的偏好有所不同。在保护性情境中，开源模型更倾向于支持边缘化群体并展示出更高的敏感性，而在危害情境下，闭源模型则更倾向于支持主流群体。研究表明，伦理行为在不同类型的情境中表现各异，模型在交叉条件下的伦理倾向比单一属性设置下更加显著，因此需要进行多维度、情境感知的评估来理解LLMs的伦理行为，以解决其决策中的公平性问题。
## 175. `cs.AI` - 单导联心电图参数的设备内计算用于实时远程心脏健康管理：一项真实世界验证研究 [PDF](https://arxiv.org/pdf/2502.17499), [HTML](https://arxiv.org/abs/2502.17499)
### Authors
Sumei Fan,Deyun Zhang,Yue Wang,Shijia Geng,Kun Lu,Meng Sang,Weilun Xu,Haixue Wang,Qinghao Zhao,Chuandong Cheng,Peng Wang,Shenda Hong
### Background
在院外实现准确且连续的心电图（ECG）参数测量对于实时心脏健康监测和远程医疗至关重要。边缘计算单导联ECG参数能够实现及时评估，无需依赖集中化数据处理，推动个性化和普及化的心脏护理，但这些系统的全面验证在异质实际人群中的工作仍然有限。本研究通过HeartVoice-ECG-lite和PTB-XL/PTB-XL+两个数据集对边缘计算算法FeatureDB进行了验证，具体数据集包括369名由两位医生标注了单导联ECG的人群和21,354名由医生进行诊断标注的12导联ECG患者。
### Innovation
研究通过两个大型数据集验证了单导联ECG参数的计算准确性和诊断性能，特别是对于一度房室传导阻滞（AVBI）和长QT综合征（LQT）。计算结果显示，该算法在多项标准上均达到或接近黄金标准水平，并且在识别这两种心脏异常方面优于开源算法Deli和商业系统。FeatureDB利用单导联设备能够提供与医生级别相当的参数准确度和与商业工具相匹敌的异常检测能力，支持扩展的远程医疗服务及心脏筛查。
### Conclusion
特征数据库能够提供医生级别的参数准确度和商业级别的异常检测能力，通过单导联设备支持可扩展的远程医疗服务、分散的心脏筛查以及社区和门诊连续监测。
## 176. `cs.AI` - 快速对抗性训练对抗稀疏攻击需要损失平滑 [PDF](https://arxiv.org/pdf/2502.21041), [HTML](https://arxiv.org/abs/2502.21041)
### Authors
Xuyang Zhong,Yixiao Huang,Chen Liu
### Background
该论文研究了在稀疏对抗性扰动（受限于$l_0$范数）下的快速对抗性训练。研究表明，使用单一步骤攻击（$1$-step攻击）在$c_0$受限扰动下的快速对抗性训练中性能下降，并且会发生灾难性过拟合（CO）。虽然$L_0$自动化对抗性训练的损失景观比$L_text{∞}$, $L_2$和$L_1$更崎岖，但是这种崎岖的损失景观会加重CO问题。因此，需要找到方法来解决这些问题，以提升对抗训练的稳定性与性能。
### Innovation
该论文提出了Fast-LS-$L_0$方法，该方法通过整合软标签和权衡损失函数来平滑对抗性损失景观。这使得方法能够在很大程度上克服灾难性过拟合问题，实现最先进的性能，并缩小单步骤和多步骤对抗性训练在稀疏攻击情况下的性能差距。
### Conclusion
综上，该研究证明了原始模型在对稀疏$1$-step攻击的应对中存在显著的挑战。通过引入一种新的方法（Fast-LS-$L_0$），有效解决了这些问题，从而在处理稀疏攻击时提高了模型的健壮性和性能。
## 177. `cs.AI` - 在面对面情境中建模情绪：眼动追踪、个性和时间动态的交互作用 [PDF](https://arxiv.org/pdf/2503.16532), [HTML](https://arxiv.org/abs/2503.16532)
### Authors
Meisam Jamshidi Seikavandi,Jostein Fimland,Maria Barrett,Paolo Burelli
### Background
准确的情绪识别对于细致和吸引人的计算机-人交互至关重要，但在动态、交谈-like 的环境中实现起来仍然具有挑战性。
### Innovation
本研究展示了如何通过整合眼动追踪数据、时间动态和个人特质来显著提高对感知和体验情绪的检测。将眼动记录信号（瞳孔大小、固定模式）、大五人格评估和自我报告的情绪状态等多模态输入结合到神经网络模型中，相较于现有最佳技术表现出显著的性能提升。
### Conclusion
这些结果突显了综合生理、个体和情境因素以应对情绪表达的主观性和复杂性所带来的好处。我们的研究不仅验证了用户特定数据在捕捉微妙内在状态方面的作用，还为未来的情感计算和人机系统的设计提供了指导，从而实现在实际交互中更具适应性和跨个体的情感智能。
## 178. `cs.AI` - 使用大型语言模型进行职业分类的带有税则引导推理的多阶段框架 [PDF](https://arxiv.org/pdf/2503.12989), [HTML](https://arxiv.org/abs/2503.12989)
### Authors
Palakorn Achananuparp,Ee-Peng Lim,Yao Lu
### Background
职业分类是指自动将就业数据中的标准化职业从分类目录中标注出来，这对于劳动力市场分析至关重要。然而，这一任务常常受到数据稀缺性和手动标注挑战的阻碍。大语言模型（LLMs）因其广泛的世界知识和基于上下文的学习能力而充满潜力，但其效果取决于对职业分类目录知识的掌握，这仍不清楚。
### Innovation
该研究提出了一种多阶段框架，包括推理、检索和重排序阶段，并结合了税则导向的推理示例，以增强性能并通过与分类知识对齐输出来弥补大语言模型的局限性，尤其是对于较小的模型。
### Conclusion
在大规模数据集上的评估显示，该框架不仅提升了职业和技能分类任务的效果，还提供了一种成本效益较高的替代方案，与前沿模型如GPT-4o相比，大大降低了计算成本同时保持了强大的性能。这种方法对于职业分类及相关任务来说是实用且可扩展的解决方案，适用于多种大语言模型。
## 179. `cs.AI` - More of the Same: Persistent Representational Harms Under Increased Representation [PDF](https://arxiv.org/pdf/2503.00333), [HTML](https://arxiv.org/abs/2503.00333)
### Authors
Jennifer Mickel,Maria De-Arteaga,Leqi Liu,Kevin Tian
### Background
为了识别和减轻生成AI系统的潜在危害，关键在于考虑不同社会群体是否以及如何被这些系统所代表。然而，仅直接衡量或提高谁被代表并不足以充分理解人们如何被代表。特别是在未经提示的情境下（即，群体未在生成系统的输入中明确指定时），这种直接的测量方法存在缺陷。因此，该研究开发了一种新的评价方法GAS(P)，以揭示生成文本中的分布级群体表征偏差，并通过分析先进的大型语言模型的职业性别表征，展现了即使在未经提示的情况下女性所占比例有所增加，表征偏差依然存在。研究揭示了不同性别在不同职业中的描述词选择存在显著差异，并证实这些差异与表征危害和刻板印象相关。这些研究结果表明，单纯增加未经提示的代表性可能无意中加剧表征偏差，而该评价方法则提供了一种系统和严谨的测量方法来应对这一问题。
### Innovation
GAS(P) 是一种新的评价方法，用于揭示生成文本中的分布级群体表征偏差，特别适用于未经提示的情境。该方法揭示了不同性别在不同职业中的描述词选择存在显著差异，并证实这些差异与表征危害和刻板印象相关。该评价方法能系统和严谨地测量这些问题，提供了一种新的视角和工具来评估和改进生成AI系统的表征问题。
### Conclusion
尽管未经提示的情况下女性所占比例有所增加，但表征偏差依然存在，不同性别在不同职业中的描述词选择存在显著差异，这些差异与表征危害和刻板印象相关联。单纯增加未经提示的代表性可能无意中加剧表征偏差，而该研究提出的评价方法GAS(P)能有效识别和量化这些问题，为改进生成AI系统的表征提供了系统和严谨的方法。
## 180. `cs.AI` - 使用深度学习进行面部欺骗检测 [PDF](https://arxiv.org/pdf/2503.19223), [HTML](https://arxiv.org/abs/2503.19223)
### Authors
Najeebullah,Maaz Salman,Zar Nawab Khan Swati
### Background
数字化图像欺骗已经成为生物特征认证系统中尤其是依赖面部识别的系统中的一个重要安全威胁。这项研究评估了三种视觉模型：MobileNetV2，ResNET50和Vision Transformer（ViT）在图像分类中对欺骗检测的性能，使用了一个包含150,986张图像的数据集，分为训练集140,002张、测试集10,984张和验证集39,574张。
### Innovation
该研究使用了不同的深度学习模型（MobileNetV2，ResNET50，ViT）对面部欺骗检测进行评估，并通过精度、召回率和F1分数等指标来比较这些模型的有效性。研究发现，MobileNetV2在测试集中的表现优于其他架构，特别是在准确性、精确度、召回率和F1分数等方面都超过了ViT。此外，MobileNetV2在训练过程中表现出更快的收敛速度并且具有更强的泛化能力，尽管两种模型都显示出过拟合的迹象。
### Conclusion
MobileNetV2因其平衡性能和鲁棒性，在新的未见过的数据上提供可靠的性能，因此是面部欺骗检测应用的理想选择。这项研究强调了在安全敏感的背景下进行模型选择的重要性，并建议MobileNetV2在实际部署中作为解决面部欺骗检测的可行性解决方案。
## 181. `cs.AI` - 关于深强化学习实现互换性假设的错误认识 [PDF](https://arxiv.org/pdf/2503.22575), [HTML](https://arxiv.org/abs/2503.22575)
### Authors
Rajdeep Singh Hundal,Yan Xiao,Xiaochun Cao,Jin Song Dong,Manuel Rigger
### Background
DRL是一种人工智能范式，其中代理使用神经网络来学习在给定环境中的行为。过去几年中，DRL因其在解决复杂环境方面的成功案例（如驾驶模拟器、3D机器人控制和多人在线战斗竞技场视频游戏）而受到关注。许多最新的算法，如深度Q网络（DQN）和近端策略优化（PPO），都有相应的实现。然而，现有研究错误地假设相同算法的不同实现是等同且可互换的。
### Innovation
通过差异测试视角，本研究揭示了一系列DRL实现的不一致性和这些不一致性对算法性能以及先前研究结论的影响。研究发现，看似相同的PPO实现之间存在显著差异，这些差异导致了一部分实现获得了超人表现，而另一部分则没有。进一步的代码分析揭示了代码层次的不一致是导致这些差异的主要原因。
### Conclusion
现有研究假设DRL实现的互换性是不正确的，这可能导致实验结果的不确定性。因此，需要改变对待实现的使用方式。
## 182. `cs.AI` - 语言模型如何追踪状态？ [PDF](https://arxiv.org/pdf/2503.02854), [HTML](https://arxiv.org/abs/2503.02854)
### Authors
Belinda Z. Li,Zifan Carl Guo,Jacob Andreas
### Background
本文探讨了语言模型（LMs）在执行特定任务时，如排列组合排序时，追踪未观察状态的方式。虽然这一问题具有简单的代数结构，但许多其他任务（如有限自动机的模拟和布尔表达式的评估）都可以归结为排列组合问题。这使得排列组合成为了研究语言模型一般状态跟踪机制的理想模型。先前的研究表明，语言模型在处理此类任务时，采用了两种相似但不同的状态跟踪机制，LCI和LC2，并揭示了这两种机制的区别及其应用场景。研究还表明，这两种机制之间存在选择偏好，适当设计的中间训练任务可以通过促进或抑制特定规则来引导模型趋向某一机制。此外，研究结果还表明，无论是预训练还是微调的语言模型都能学习实施高效且可解释的状态追踪机制，并能够预测和控制这些机制的出现。
### Innovation
本文创新地研究了在排列组合任务中语言模型如何学习状态跟踪机制，发现了两种状态跟踪机制LCI和LC2，并通过中间训练任务控制模型的选择偏好。研究表明，具备某些特征的语言模型在处理该任务时倾向于选择更高效的LCI机制，并且这种机制的掌握有助于更好地泛化与更快地收敛。这项工作揭示了如何预测和控制语言模型完成状态跟踪任务的能力，为理解和改进语言模型的表现提供了新的视角。
### Conclusion
本文研究发现，无论是预训练还是微调的语言模型，都能学习实施高效且可解释的状态追踪机制。通过对LCI和LC2的状态跟踪机制进行分析，研究结果表明，适当的设计可以使模型倾向于选择其中之一，并且这两种机制的应用场景可以被预见和控制。此外，该研究还揭示了这些机制在便携文本生成、代码生成等任务中的潜在应用价值。
## 183. `cs.AI` - RaanA: 一种快速、灵活且数据高效的后训练量化算法 [PDF](https://arxiv.org/pdf/2504.03717), [HTML](https://arxiv.org/abs/2504.03717)
### Authors
Yongyi Yang,Jianyang Gao,Wei Hu
### Background
后训练量化（PTQ）已成为提升大规模语言模型（LLMs）推理效率的一种广泛应用的技术。然而，现有的PTQ方法通常存在一些关键限制，例如需要大量校准数据和灵活选择目标比特位数的能力有限。
### Innovation
本文提出了一种名为RaanA的统一PTQ框架，通过引入两个新组件来克服上述挑战：1) RaBitQ-H，一种随机向量量化方法RaBitQ的变体，专为快速、准确且高效量化设计；2) AllocateBits，一种根据量化敏感度优化分配比特宽度的算法。RaanA在保持与最先进的量化方法相当的性能的同时，实现了极高的速度，需要最少的校准数据，并允许灵活分配比特位。
### Conclusion
广泛的实验证明RaanA在平衡效率和准确度方面表现出色。代码已公开，可供参考和使用。
## 184. `cs.AI` - DualOptim：使用双优化器提升机器遗忘的有效性和稳定性 [PDF](https://arxiv.org/pdf/2504.15827), [HTML](https://arxiv.org/abs/2504.15827)
### Authors
Xuyang Zhong,Haochen Luo,Chen Liu
### Background
现有机器遗忘（MU）方法对超参数表现出显著的敏感性，要求进行仔细调整，这限制了其实用部署。已有研究表明，不同的MU方法在不同场景下的表现不稳定且性能欠佳。
### Innovation
本文首次通过实验证明现有流行MU方法在不同场景下的不稳定性和表现不佳的问题，并提出了一个名为DualOptim的新方法，该方法结合了自适应学习率和解耦动量因素，实证和理论证据表明DualOptim能有效且稳定地实现遗忘。DualOptim已被广泛实验所验证，在图像分类、图像生成和大型语言模型等不同任务中显著提升MU的功效和稳定性，使其成为赋能现有MU算法的通用方法。
### Conclusion
通过大量实验，结果表明DualOptim可以在多种不同任务中显著提升MU的效力和稳定性，使它成为一种具有广泛应用潜力的MU方法。
## 185. `cs.AI` - Data Therapist: 使用大型语言模型从领域专家提取专业知识 [PDF](https://arxiv.org/pdf/2505.00455), [HTML](https://arxiv.org/abs/2505.00455)
### Authors
Sungbok Shin,Hyeon Jeon,Sanghyun Hong,Niklas Elmqvist
### Background
有效的数据可视化不仅需要技术熟练，还需要对数据所存域的深入理解，其中涉及的数据来源、质量及用途等知识往往是隐性的，未在数据集中明确体现。因此，有需求通过技术手段帮助领域专家明确这些隐性知识，并用于数据可视化的设计中。本文提出了一种名为数据治疗师的网页系统，该系统利用大型语言模型分析用户提供的数据集，提出针对性问题，并支持不同层次的注释，帮助领域专家外化隐性知识，形成结构化的知识库，以指导人类和自动化可视化设计。
### Innovation
该系统创新性地结合了迭代问答和交互注释的方法，通过大型语言模型自动化处理问题和注释，帮助领域专家理解和分享数据背后的知识，从而优化数据可视化设计。
### Conclusion
通过对会计、政治学和计算机安全领域的专家对数据的推理方式的研究，发现反复出现的模式，并指出人工智能支持在提升可视化设计中的机会。
## 186. `cs.AI` - GenSwarm：通过语言模型实现可扩展的多机器人代码策略生成与部署 [PDF](https://arxiv.org/pdf/2503.23875), [HTML](https://arxiv.org/abs/2503.23875)
### Authors
Wenkang Ji,Huaben Chen,Mingyang Chen,Guobin Zhu,Lufeng Xu,Roderich Groß,Rui Zhou,Ming Cao,Shiyu Zhao
### Background
多机器人系统的控制策略开发过程通常复杂且劳动密集，难以灵活适应动态任务。因此，研究者致力于开发能够自动创建控制策略的方法。然而，这些方法往往需要多次迭代地手工设计和优化目标函数，从而延长了开发周期。本文讨论了GenSwarm，一个利用大型语言模型根据简单的自然语言用户指令自动生成和部署多机器人任务控制策略的端到端系统。作为一个多语言智能代理系统，GenSwarm实现了零样本学习，能够迅速适应改变或未知的任务。由于其透明的代码策略，GenSwarm具有较强的可重复性和可解释性。通过可扩展的软件和硬件架构，GenSwarm能够在模拟和实际多机器人系统上实现高效的策略部署，实现从指令到执行的端到端功能，这对于机器人专家和非专家来说都非常有价值。
### Innovation
GenSwarm通过大型语言模型技术自动为多机器人任务生成和部署控制策略，无需多次迭代的手工设计和优化，从而实现快速适应变化或未知任务的零样本学习。其透明的代码策略保证了高度的可重复性和可解释性，并且具有可扩展的软件和硬件架构，可以在模拟和实际多机器人系统上实现高效的策略部署，实现从指令到执行的端到端功能。
### Conclusion
GenSwarm提供了一种新的方法，使得多机器人系统的控制策略开发更加高效和灵活。通过利用大型语言模型，它可以快速响应多变的任务需求，并保持高透明度和可解释性，从而支持机器人专家和非专家的应用。该系统的代码可在给定的链接中找到。
## 187. `cs.AI` - AVA: 通过 Vision Language Models 实现主动型视频分析 [PDF](https://arxiv.org/pdf/2505.00254), [HTML](https://arxiv.org/abs/2505.00254)
### Authors
Yuxuan Yan,Shiqi Jiang,Ting Cao,Yifan Yang,Qianqian Yang,Yuanchao Shu,Yuqing Yang,Lili Qiu
### Background
AI驱动的视频分析在多个领域变得越来越重要。然而，现有的系统通常受限于特定的预定义任务，不能在开放式的分析场景中很好地适应。最近，Vision Language Models (VLMs) 的出现为开放式的视频理解、推理和分析提供了潜在的可能性，但它们在处理超长视频内容时存在挑战，尤其是在现实世界应用中非常普遍的情况。为此，本文提出了一种名为AVA的系统，该系统利用VLMs进行开放式的高级视频分析。
### Innovation
AVA引入了两项创新：首先，它能够实现实时构建事件知识图谱（EKGs），用于长或连续视频流的高效索引。其次，它采用了一种代理检索-生成机制，利用EKGs来处理复杂和多样化的查询。
### Conclusion
在公共基准LVBench和VideoMME-Long上的全面评估显示，AVA实现了最先进的性能，准确率达到62.3%和64.1%，显著优于现有的VLM和视频检索增强生成（RAG）系统。为了在超长和开放世界视频场景中评估视频分析，本文还引入了一个新基准AVA-100，该基准包括8个超过10小时的视频，以及120个手动注释的多样化和复杂的问答对。在AVA-100上，AVA取得了顶级性能，准确率为75.8%。
## 188. `cs.AI` - 个体公平，群体受挫？审计匿名化对机器学习公平性的影响 [PDF](https://arxiv.org/pdf/2505.07985), [HTML](https://arxiv.org/abs/2505.07985)
### Authors
Héber H. Arcolezi,Mina Alishahi,Adda-Akram Bendoukha,Nesrine Kaaniche
### Background
机器学习算法高度依赖训练数据，这些数据可能包含敏感信息，从而对数据提供者构成隐私威胁。尽管去标识化技术已被广泛采用以保护隐私，但这些技术对机器学习公平性的影响仍不清楚，尤其是关于$k$-匿名性、$boldsymbol{beta}$多样化和$t$-邻近性等具体技术的影响。
### Innovation
本研究系统性地评估了各种匿名化技术对机器学习公平性的影响，包括个体和群体公平性的评价。研究显示，匿名化措施可能会使群体公平性指标下降四倍，但同时个体公平性指标在强匿名化措施下有所提升，主要是因为输入数据的同质性增加。这份研究在不同隐私设置和数据分布下的匿名化程度差异，揭示了公平性、隐私性和实用性之间的权衡，为负责任的人工智能开发提供了实用指导。
### Conclusion
本研究揭示了匿名化技术对机器学习公平性的影响，并指出个体和群体公平性之间的权衡。通过系统评估不同匿名化措施，研究为提高机器学习公平性的同时保护隐私提供了关键见解。
## 189. `cs.AI` - SageAttention3: 微缩 FP4 注意力加速推理及 8 位训练探索 [PDF](https://arxiv.org/pdf/2505.11594), [HTML](https://arxiv.org/abs/2505.11594)
### Authors
Jintao Zhang,Jia Wei,Pengle Zhang,Xiaoming Xu,Haofeng Huang,Haoxu Wang,Kai Jiang,Jun Zhu,Jianfei Chen
### Background
由于注意力机制的时间复杂度为二次时间复杂度，其效率成为一个重要的问题。现有的低比特注意力机制如FlashAttention3和SageAttention主要集中在推理阶段的加速，但对通过训练大大型模型的效率同样重要。因此，探讨低比特注意力能否应用于训练任务具有重要意义。
### Innovation
本研究通过以下两个关键贡献提升了注意力机制的效率：首先，利用Blackwell GPU中的新FP4张量核心加速注意力计算；其次，开发了适用于前向和反向传播的8位注意力机制，以探索其在训练任务中的应用并达到无损失的微调性能。
### Conclusion
实验结果表明，通过FP4注意力机制可以实现相对于RTX5090的FlashAttention5倍以上的速度提升，并且8位注意力机制在微调任务中可实现无损失性能，但在预训练任务中收敛速度较慢。
## 190. `cs.AI` - 不确定性意识的选择性预测的变分视觉问答 [PDF](https://arxiv.org/pdf/2505.09591), [HTML](https://arxiv.org/abs/2505.09591)
### Authors
Tobias Jan Wieczorek,Nathalie Daun,Mohammad Emtiyaz Khan,Marcus Rohrbach
### Background
尽管近年来取得了显著进展，视觉语言模型（VLMs）在视觉问答（VQA）和视觉推理等任务上仍然容易过度自信和产生幻觉。贝叶斯方法有可能通过帮助模型选择性地预测来提高可靠性，即模型只在足够自信时才回应。然而，贝叶斯方法常被认为对大型模型代价高且效果不佳，尤其是在多模态应用方面几乎没有实验证据。本文通过实验证明了变分贝叶斯方法在VQA中的有效性和竞争力，尤其是在低容错率（≤1%）的情况下，甚至优于通过AdamW训练的模型。这种方法提高了校准度，并在VQA和视觉推理中显著提高了选择性预测的表现。此外，还提出了一种新的风险厌恶选择器，其性能优于标准样本平均法，因为它考虑了预测的方差。
### Innovation
本文首次展示了变分贝叶斯方法在VQA中的有效性，并提出了一种新的风险厌恶选择器来实现选择性预测。变分VQA方法提高了校准度，并在低容错率下表现出显著的性能提升，甚至优于使用AdamW训练的模型。提出的风险厌恶选择器也显著优于标准样本平均法。
### Conclusion
本文提供了确凿的证据，表明变分学习是一种使大型VLMs更加安全和可信的有效选择。
## 191. `cs.AI` - 通过μP高效扩展扩散变换器 [PDF](https://arxiv.org/pdf/2505.15270), [HTML](https://arxiv.org/abs/2505.15270)
### Authors
Chenyu Zheng,Xinyu Zhang,Rongzhen Wang,Wei Huang,Zhi Tian,Weilin Huang,Jun Zhu,Chongxuan Li
### Background
扩散变换器已经成为了视觉生成模型的基础，但它们在大规模应用中受限于超参数（HP）调优的高成本。虽然通用变换器的最小子参数化（μP）可以稳定地从小型到大型语言模型转移HP并显著降低调优成本，但其在扩散变换器上的应用尚未得到验证，因为它们在架构和目标上存在差异。因此，本文探讨了μP在扩散变换器上的通用性，并通过大规模实验验证其有效性。
### Innovation
本文提出了将μP标准推广至扩散变换器，并系统展示了DiT-μP能够实现稳定的HP迁移。特别地，DiT-XL-2-μP在转移学习率的基础上实现了比原始DiT-XL-2快2.9倍的收敛速度。此外，通过将PixArt-α和MMDiT分别扩展到0.61B和18B参数，并在μP框架下实现了模型性能的提升，调优成本低至总训练量的5.5%和3%。这些发现为扩散变换器的大规模扩展提供了一个原则性和高效的框架。
### Conclusion
μP为扩散变换器的大规模扩展提供了一个合理且有效的解决方案，通过这一方法，模型不仅在性能上超越了各自的基线，而且调优成本极低。
## 192. `cs.AI` - R$^2$ec: 含有推理能力的大规模推荐模型 [PDF](https://arxiv.org/pdf/2505.16994), [HTML](https://arxiv.org/abs/2505.16994)
### Authors
Runyang You,Yongqi Li,Xinyu Lin,Xin Zhang,Wenjie Wang,Wenjie Li,Liqiang Nie
### Background
大型推荐模型通过编码或项目生成扩展了LLM的能力，成为强大的推荐器。最近在LLM推理方面的突破激发了在推荐中探索推理的研究。现有方法包括传统的推荐器、基于LLM的推荐器以及增强推荐推理的推荐器，但在推理方面的缺乏标记数据数据成为了挑战。为解决此问题，本文提出了具有内在推理能力的统一大型推荐模型R$^2$ec。
### Innovation
提出了R$^2$ec，一种统一的大规模推荐模型，具备内在的推理能力。R$^2$ec采用双头架构，支持单个模型中的推理链生成和高效的项目预测，显著减少了推理延迟。设计了RecPO，一种基于奖励机制的强化学习框架，用于同步优化推理与推荐。实验结果表明，R$^2$ec在多项任务上的表现优于传统、基于LLM和增强推理的推荐基准模型，且在面对多样化推荐场景时具有较强的适应能力。此外，还提供了代码和检查点的访问链接以方便验证结果的合理性。
### Conclusion
R$^2$ec在推荐系统中的推理能力方面取得了显著进展，通过引入双头架构和新型融合奖励机制提升了推荐效率和性能，并验证了其在多个数据集上的优越表现和对多样化推荐场景的适应性。
## 193. `cs.AI` - 进攻性网络安全代理的动态风险评估 [PDF](https://arxiv.org/pdf/2505.18384), [HTML](https://arxiv.org/abs/2505.18384)
### Authors
Boyi Wei,Benedikt Stroebl,Jiacen Xu,Joie Zhang,Zhou Li,Peter Henderson
### Background
基础模型正在变得越来越能够自主编程，这使得它们有可能自动化危险的进攻性网络操作。目前的前沿模型审查正在探索此类代理的网络安全风险，但大多数审查没有考虑到实际世界中对手拥有的自由度。特别是，在强大的验证者和经济激励措施存在的情况下，进攻性网络安全代理可以被有意图的对手通过迭代改进。因此，需要考虑在一个固定的计算预算下，对手在有状态和无状态环境中的不同自由度，来进行网络安全风险评估。
### Innovation
提出了一种评估进攻性网络安全代理风险的新方法，强调了在一个固定的计算预算下，对手在有状态和无状态环境中的不同自由度。该研究展示了即使在相对较小的计算预算（研究中使用8个H100 GPU小时）下，对手也能将代理的网络安全能力提高超过40%，并且无需外部协助。这凸显了需要以动态方式评估代理的网络安全风险，生成更具有代表性的风险图景。
### Conclusion
评估代理的网络安全风险应更加动态和全面，以更好地反映风险的真实情况。
## 194. `cs.AI` - GAIA：用于操作大气动力学的基本模型 [PDF](https://arxiv.org/pdf/2505.18179), [HTML](https://arxiv.org/abs/2505.18179)
### Authors
Ata Akbari Asanjan,Olivia Alexander,Tom Berg,Stephen Peng,Jad Makki,Clara Zhang,Matt Yang,Disha Shidham,Srija Chakraborty,William Bender,Cara Crawford,Arun Ravindran,Olivier Raiman,David Potere,David Bell
### Background
该研究介绍了一种名为GAIA（Geospatial Artificial Intelligence for Atmospheres）的地理空间人工智能结合模块，它将掩蔽自动编码器（MAE）与无标签自我精炼（DINO）结合，用于从全球静止轨道卫星图像生成语义丰富的表示。该模型基于2001年至2015年间的全球合并红外观测进行预训练，能够学习到复杂的分量结构和时间一致性，且能适应不同数据可用性情况，表现出强大的重构能力和填补实际数据空白的性能。
### Innovation
GAIA将掩蔽自动编码器（MAE）与无标签自我精炼（DINO）结合使用，无需标签即可生成语义丰富的表示。该模型能够学习到大气动态的专业表示，而非简单的日间模式。通过分析，表明GAIA的混合目标促进了学习空间一致、对象中心的特征分布在多个主成分中，而非集中在重建上，证明了结合互补的自我监督目标能够产生更适用于多样化大气建模任务的表示。
### Conclusion
GAIA在多个大气任务中表现出色，特别是在大气河流分割（F1: 0.58 vs 0.52）、热带气旋检测（风暴级召回：81% vs 75%，早期检测：29% vs 17%）和降水估计方面。这些结果表明GAIA能够生成更具迁移性、更适用于大气科学多样任务的表示，进一步证明了互补的自我监督目标结合的有效性。作者已提供了模型权重和代码。
## 195. `cs.AI` - 重新审视视频异常检测的度量标准和基准 [PDF](https://arxiv.org/pdf/2505.19022), [HTML](https://arxiv.org/abs/2505.19022)
### Authors
Zihao Liu,Xiaoyu Wu,Wenna Li,Linlin Yang,Shengjin Wang
### Background
视频异常检测（VAD）旨在发现与预期不符的异常现象，近年来吸引了越来越多的关注。现有的VAD研究主要集中在模型架构和训练策略上，但对评估指标和基准的关注不足。当前的评估方法存在三个主要问题：1) 存在显著的单注释偏差；2) 未能奖励异常早期检测；3) 可用基准不能评估强监督和弱监督算法的场景过拟合能力。因此，该领域需要新的评价方法来弥补这些不足之处。
### Innovation
本文提出了一种重新审视VAD评价方法方式，提出了三种新型评价方法：1) 通过利用多轮注释建立了概率AUC/AP（Prob-AUC/AP）指标，以减轻单注释偏差；2) 开发了一个基于延迟感知平均精度（LaAP）的指标，奖励早期和准确的异常检测；3) 引入了两种困难正常基准（UCF-HN, MSAD-HN），专用于评估场景过拟合。作者还使用这些新的评价方法对十种最先进的VAD方法进行了性能比较，提供了对未来VAD模型开发的新视角，并发布了相关数据和代码。
### Conclusion
本文提出了新的评价方法，比较了十种最先进的VAD方法，并通过公开数据和代码提供了对VAD开发的新见解。
## 196. `cs.AI` - 通过自适应并行解码加速扩散大语言模型 [PDF](https://arxiv.org/pdf/2506.00413), [HTML](https://arxiv.org/abs/2506.00413)
### Authors
Daniel Israel,Guy Van den Broeck,Aditya Grover
### Background
当前大语言模型（LLMs）的生成速度受到自回归解码的限制，因为每个token都是按顺序生成的。虽然扩散大语言模型（dLLMs）理论上允许并行生成token，但实践上却难以达到自回归模型的速度，同时质量也有所下降。因此，需要一种能够动态调整并行生成token数量的新方法来平衡吞吐量和质量。
### Innovation
本文介绍了一种新颖的方法——自适应并行解码（APD），通过定义dLLM边际概率与小辅助自回归模型下序列的联合概率之间的乘法混合，来实现动态调整并行生成token的数量。APD通过启用KV缓存和限制遮罩输入的大小来进一步优化，并提出三个可调节参数来灵活权衡吞吐量和质量。实验表明，APD在保持最小质量损失的情况下，能够显著提高下游基准模型的生成速度。
### Conclusion
该方法展示了在保留质量的同时，显著提高扩散大语言模型的生成速度，为大语言模型的高效生成提供了新的解决方案。
## 197. `cs.AI` - 长时间序列预测中增强的多模态视图大型视觉模型 [PDF](https://arxiv.org/pdf/2505.24003), [HTML](https://arxiv.org/abs/2505.24003)
### Authors
ChengAo Shen,Wenchao Yu,Ziming Zhao,Dongjin Song,Wei Cheng,Haifeng Chen,Jingchao Ni
### Background
时间序列，通常以数值序列的形式表示，也可以转换为图像和文本，提供相同基础信号的多模态视图（MMVs）。这些MMVs可以揭示互补模式，并允许使用强大的预先训练的大模型，如大型视觉模型（LVMs），进行长期时间序列预测（LTSF）。然而，正如我们在本文中指出的，最先进的LVM基于的预测器对“预测周期”存在诱导偏差，DMMV提出了一种新颖的基于分解的多模态视图框架，利用趋势-季节性分解和一种新颖的反向预测-残差基于的自适应分解策略，将MMVs整合到LTSF中。
### Innovation
提出了DMMV（基于分解的多模态视图），一种新颖的基于分解的多模态视图框架，利用趋势-季节性分解和一个新颖的反向预测-残差自适应分解策略，将MMVs整合到长时序预测中，克服了最先进的LVM预测器的“预测周期”偏见。DMMV在多个基准数据集上优于14个最先进的单一视图和现有的多模态基线模型，取得了6个数据集上最低的均方误差（MSE）
### Conclusion
DMMV在多种好奇心数据集上实现了最优的均方误差（MSE），并明显优于单一视图和现有的多模态基线模型，该方法将MMVs和LSTM-Ensemble结合，展示了出色的LTSF性能。
## 198. `cs.AI` - PoLAR: 洛北因分解释放低秩适配器表示 [PDF](https://arxiv.org/pdf/2506.03133), [HTML](https://arxiv.org/abs/2506.03133)
### Authors
Kai Lion,Liang Zhang,Bingcong Li,Niao He
### Background
研究表明，在大规模模型的低秩适配过程中，适配器所处的稳定秩较低，远低于子空间的线性代数秩，这影响了微调的性能。为了缓解分配空间的未充分利用问题，我们提出了一种基于极分解的参数化方法，这种方式将低秩更新因子化为两个受限于史蒂费尔流形的方向矩阵以及一个非约束的尺度矩阵。
### Innovation
我们提出的PoLAR方法通过将低秩更新的两方向矩阵限制在史蒂费尔流形上，及使用未约束的尺度矩阵，并受到极分解的启发，达到了在低秩适配问题上收敛速率指数级提升的效果。与里emann优化组合使用，PoLAR方法在三个基准测试（一般语言理解、常识推理和数学问题求解）上表现出了持续改进。
### Conclusion
我们证明了PoLAR方法在不同规模的预训练模型下，在一般语言理解、常识推理和数学问题求解上，能够有效地提升微调性能，并且在低秩适配问题上提供了指数级的更快收敛速率。
## 199. `cs.AI` - 基于人工智能的人类同情心：人工智能在心理健康中的应用 [PDF](https://arxiv.org/pdf/2506.00081), [HTML](https://arxiv.org/abs/2506.00081)
### Authors
Aditya Naik,Jovi Thomas,Teja Sree Mandava,Himavanth Reddy Vemula
### Background
许多人在生活中遭遇心理健康问题，但并非所有人都愿意寻求专业帮助或获得相应的心理健康服务。人工智能聊天机器人越来越成为人们的首选，无论是作为患有心理健康问题的人士，还是那些仅仅需要倾诉的人来说。本文通过调查已经使用过聊天机器人的参与者，并针对大型语言模型（LLM）聊天机器人进行了基于场景的测试。研究发现，聊天机器人主要被作为临时咨询或非评判性伴侣使用，参与者赞赏聊天机器人的匿名性和无评判性。然而，隐私和敏感信息的安全性问题引起了关注。场景测试还揭示了一些其他问题，如聊天机器人的语气不一致、偶尔给出不恰当的回答（例如随意或浪漫）、以及缺乏对危机的敏感性，特别是在识别预警词汇并恰当地升级响应方面存在不足。
### Innovation
本研究通过基于场景的测试，评估了大型语言模型（LLM）聊天机器人在心理健康领域的应用效果，不仅确认了其作为临时咨询工具的价值，同时也揭示了提高准确性和可靠性的关键问题，如语气的不一致性、不恰当的回应以及缺乏对危机情况的敏感性等。这些发现对技术和心理健康行业都有启示作用，有助于更好地利用人工智能聊天机器人支持面临情感困境的个体。
### Conclusion
研究结果表明，人工智能聊天机器人主要被用作临时咨询或非评判性伴侣。虽然它们提供了匿名性和无评判性的优势，但隐私和安全问题仍然存在。在对大型语言模型（LLM）的聊天机器人进行场景测试后，发现虽然有些机器人能够提供安抚和个性化的回应，但也存在语气不一致、不恰当回应和对危机情况缺乏敏感性的问题。这些发现可以用于指导技术及心理健康行业改进聊天机器人的功能，更好地支持经历情感挑战的个体。
## 200. `cs.AI` - SC-LoRA: Balancing Efficient Fine-tuning and Knowledge Preservation via Subspace-Constrained LoRA [PDF](https://arxiv.org/pdf/2505.23724), [HTML](https://arxiv.org/abs/2505.23724)
### Authors
Minrui Luo,Fuhang Kuang,Yu Wang,Zirui Liu,Tianxing He
### Background
参数高效的微调（PEFT）方法，特别是Low-Rank Adaptation (LoRA)，对于有效定制大型语言模型（LLMs）至关重要。但是，标准的LoRA在收敛速度方面存在问题，并且存在知识丢失的问题。最近的研究利用了精心设计的LoRA初始化方法来提升微调效率或保留预训练知识，然而这些研究无法同时解决这两个问题。针对此现状，我们引入了Subspace-Constrained LoRA (SC-LoRA)，一种工程化设计的LoRA初始化框架，旨在平衡高效微调和知识保留之间的权衡。SC-LoRA通过对可训练LoRA适配器的输出施加在低秩子空间中的约束条件，以平衡地保留微调数据中的上下文信息并最少地保留保存知识中的上下文信息。这种约束使得可训练权重主要专注于微调数据的主要特征，同时避免损害保存的知识特征。
### Innovation
我们通过构建一种新的LoRA初始化框架——Subspace-Constrained LoRA (SC-LoRA)，解决了高效微调和知识保留之间的权衡问题。SC-LoRA通过对可训练LoRA适配器的输出施加在低秩子空间中的约束条件，平衡地保留微调数据中的上下文信息并最少地保留保存知识中的上下文信息。这种方法不仅提高了微调性能，还显著减少了知识丢失，超过了现有的其他LoRA初始化方法。我们提供了对SC-LoRA的理论分析，并进行了涵盖安全保留和世界知识保留等各下游任务的广泛实验。实验结果表明，SC-LoRA在提升微调性能的同时，显著减少了知识遗忘。
### Conclusion
SC-LoRA成功地在高效微调和知识保留之间找到了平衡，其理论分析和实验结果都显示SC-LoRA在提升微调性能的同时显著减少了知识遗忘，超过了现有其他LoRA初始化方法。
## 201. `cs.AI` - UdonCare：基于层次剪枝的未知领域发现用于预测型医疗保健 [PDF](https://arxiv.org/pdf/2506.06977), [HTML](https://arxiv.org/abs/2506.06977)
### Authors
Pengfei Hu,Xiaoxue Han,Fei Wang,Yue Ning
### Background
医疗保健服务提供者常根据患者的临床因素（如病史）将患者群体分成具有相似特征的队列以提供个性化服务。在临床预测模型中，这一概念也得到了应用，但同时也带来了挑战：如何捕捉全局和特定队列的特征并使模型在未知领域中具有泛化能力。传统领域泛化（DG）方法在临床环境中通常难以应对，因为缺乏明确的领域标签和医学知识的局限性。
### Innovation
提出了一种名为UdonCare的新方法，该方法采用层级剪枝策略，通过逐步将患者分层为潜在领域，并从患者数据中分解领域不变（标签）信息来解决这一挑战。UdonCare通过剪枝医学概念层次结构（如ICD-9-CM层次结构）来识别患者领域。在MIMIC-III和MIMIC-IV两个公开数据集上，UdonCare在四个临床预测任务中展现出优于八个基线模型的效果，特别是在存在显著领域差距的情况下。
### Conclusion
UdonCare展示了医学知识在指导临床领域泛化问题方面的巨大潜力。
## 202. `cs.AI` - DeepVideo-R1: 视频强化微调通过感知难度的回归型GRPO [PDF](https://arxiv.org/pdf/2506.07464), [HTML](https://arxiv.org/abs/2506.07464)
### Authors
Jinyoung Park,Jeehye Na,Jinyoung Kim,Hyunwoo J. Kim
### Background
最近的研究表明，基于强化学习（RL）的后训练方法可以提高大型语言模型（LLMs）的推理能力。Group Relative Policy Optimization（GRPO）尤其通过使用类似于PPO的强化算法以及组归一化的奖励显示了显著的效果。尽管如此，GRPO在Video Large Language Models（VideoLLMs）中的有效性仍然较少被研究。
### Innovation
本文提出了一种新的方法DeepVideo-R1，使用感知难度的回归型GRPO（Reg-GRPO）和难度感知的数据增强策略。Reg-GRPO重新定义了GRPO的损失函数，将其转化为一个直接预测优势的回归任务，从而消除了需要诸如裁剪和最小值函数等保障措施的需求，直接指导模型选择更好的优势。难度感知的数据增强策略通过增强输入提示/视频来定位样本的难度，使其在可解决的难度级别上，从而提供多样化的奖励信号。
### Conclusion
我们的实验结果表明，我们的方法在多个基准测试中显著提高了视频推理性能。
## 203. `cs.AI` - 支持插入和删除的图扩散 [PDF](https://arxiv.org/pdf/2506.15725), [HTML](https://arxiv.org/abs/2506.15725)
### Authors
Matteo Ninniri,Marco Podda,Davide Bacciu
### Background
基于离散去噪扩散概率模型的图生成模型（DDPM）为分子生成提供了一种系统的方法，通过迭代原子和键调整逐步去除结构噪声。然而，现有的公式在扩散过程中无法适应图的大小（即原子数量），这对条件生成场景（如基于性质的分子设计）造成了很大的限制，因为目标性质通常与分子大小相关。
### Innovation
本文重新定义了去噪和去噪过程，以支持节点的单调插入和删除，从而开发了一种名为GrIDDD的新模型，该模型在生成过程中可以动态增长或缩小化学图。GrIDDD在分子性质目标方面达到了或超过了现有图扩散模型的表现，同时其训练问题更为困难。此外，在分子优化方面，GrIDDD表现出与专用优化模型相当的性能。这项工作为图扩散中的大小适应性分子生成铺平了道路。
### Conclusion
GrIDDD在分子性质目标方面表现出色，并为适应性分子生成提供了新的可能性。
## 204. `cs.AI` - 使用大型语言模型对设计结构矩阵进行组合优化 [PDF](https://arxiv.org/pdf/2506.09749), [HTML](https://arxiv.org/abs/2506.09749)
### Authors
Shuo Jiang,Min Xie,Jianxi Luo
### Background
在复杂的工程系统中，组件或开发活动之间的依赖关系通常通过设计结构矩阵（DSM）进行建模和分析。重组DSM中的元素以减少反馈回路并提高模块化或流程效率是一个具有挑战性的组合优化（CO）问题。随着问题规模的增加和依赖网络变得更加复杂，传统依赖数学启发式方法的优化方法往往无法捕捉到上下文细微差别，难以提供有效的解决方案。因此，有必要探索新的方法来解决这些CO问题。本文探讨了如何利用大型语言模型（LLMs）通过利用其高级推理和上下文理解能力来解决这些CO问题。
### Innovation
本文提出了一种基于LLM的新颖框架，该框架结合了网络拓扑和上下文领域知识，用于DSM顺序迭代优化。实验结果表明，该方法在收敛速度和解的质量上都优于传统的随机和确定性基线方法。此外，结合上下文领域知识显著提高了优化性能，不依赖于所选择的LLM基础结构。这些发现强调了LLMs组合语义和数学推理能力以解决复杂的工程CO问题的潜力，这为LLM在工程设计优化中的应用开辟了新的范式。
### Conclusion
本文研究使用大型语言模型解决设计结构矩阵的组合优化问题。提出了一种新颖的框架，该框架结合了网络拓扑和上下文领域知识来迭代优化DSM序列。结果表明，该方法在收敛速度和解的质量方面优于现有的基线方法，并且结合上下文领域知识显著提高了优化性能。最终这一发现强调了LLMs在解决复杂的工程组合优化问题上的潜力。
## 205. `cs.AI` - 基于深度学习的临床试验入组预测及不确定性估计 [PDF](https://arxiv.org/pdf/2507.23607), [HTML](https://arxiv.org/abs/2507.23607)
### Authors
Tien Huu Do,Antoine Masquelier,Nae Eoun Lee,Jonathan Crowther
### Background
临床试验是评估新药或治疗方法的安全性和有效性的一项系统工程，通常需要较大的资金投入和精细的规划。在规划阶段，准确预测患者入组情况是主要挑战之一。准确预测患者入组对于临床试验的成功至关重要，因此需要一种方法来解决这个问题。为此，本文提出了一种基于深度学习的新方法来解决这一关键挑战。该方法通过神经网络模型，结合预训练语言模型和编码的表格特征，利用注意机制，从而准确预测临床试验的患者入组情况，在实际临床试验数据上进行了实验，并展示了该方法在预测多站点临床试验入组情况方面的优越性，优于现有的基准模型。
### Innovation
提出了基于深度学习的方法，结合预训练语言模型和注意机制，通过编码的表格特征和Gamma分布的概率层，提高预测临床试验入组情况的准确性和对入组不确定性的估计能力，特别是在患者的入组预测中，假设站点级别患者入组遵循Poisson-Gamma过程。该方法在实际临床试验数据上的实验结果显示了其优越性。
### Conclusion
本文提出的方法能够有效地预测特定临床试验在多个站点的患者入组情况，效果优于现有的基准模型，表明该方法在临床试验规划和评估中具有重要的应用价值。
## 206. `cs.AI` - 基于不确定性平滑策略正则化的稀疏演示强化学习 [PDF](https://arxiv.org/pdf/2509.15981), [HTML](https://arxiv.org/abs/2509.15981)
### Authors
Yujie Zhu,Charles A. Hepburn,Matthew Thorpe,Giovanni Montana
### Background
在稀疏奖励的强化学习中，演示可以加速学习过程，但确定何时模仿演示仍然是一个挑战。SPReD框架旨在解决Agent何时模仿演示，何时遵循自身政策的基本问题。
### Innovation
SPReD提出了一种使用集成方法显式建模演示和策略行动的Q值分布的框架，量化不确定性进行比较。SPReD开发了两种互补的基于不确定性的方法：一种概率方法估计演示优势的可能性，一种基于优势的方法通过统计显著性缩放模仿。SPReD通过连续、与不确定性成比例的正则化权重应用，减少了训练中的梯度方差，其简单而高效，实验结果表明在八个机器人任务中表现优异，在复杂任务中相对于现有方法改进高达14倍，同时对演示质量和数量具有鲁棒性。
### Conclusion
SPReD框架在稀疏演示的强化学习中实现了显著的性能提升，尤其是在复杂任务上，比现有方法提高最多14倍，同时展示了对演示质量和数量的鲁棒性。
## 207. `cs.AI` - SafePLUG：为交通事故理解赋能的具有像素级洞察和时间定位的多模态LLM [PDF](https://arxiv.org/pdf/2508.06763), [HTML](https://arxiv.org/abs/2508.06763)
### Authors
Zihao Sheng,Zilin Huang,Yansong Qu,Jiancong Chen,Yuhao Luo,Yen-Jung Chen,Yue Leng,Sikai Chen
### Background
多模态大语言模型(MLLMs)已经在各种视觉语言任务中取得了显著进步，并展示了在交通事故理解方面的强大潜力。然而，现有的MLLMs主要集中在粗粒度的图像级别或视频级别的理解上，面对细粒度的视觉细节或局部场景组件时表现欠佳，限制了这些模型在复杂事故场景中的应用。
### Innovation
提出了一种名为SafePLUG的新框架，它增强了MLLMs的像素级理解和时间定位能力，适用于全面的交通事故分析。SafePLUG支持任意形状的视觉提示进行区域感知问答，基于语言指令进行像素级分割，并能在交通事故场景中识别时间锚定的事件。我们还构建了一个新数据集，包含多种事故场景的多模态问题-答案对，并进行了详细的像素级标注和时间事件边界定义。实验结果显示，SafePLUG在多种任务上表现出色，包括基于区域的问答、像素级分割、时间事件定位和事故事件理解，为交通场景的细致理解奠定了基石，有助于提高驾驶安全和智能交通系统的态势感知能力。数据集、代码和模型检查点将公开提供。
### Conclusion
SafePLUG框架提升了MLLMs在交通事故理解中的性能，展示了在复杂交通场景中的应用潜力，并为未来的多模态大语言模型的发展提供了基础。
## 208. `cs.AI` - 电商平台定价和广告算法性共谋 [PDF](https://arxiv.org/pdf/2508.08325), [HTML](https://arxiv.org/abs/2508.08325)
### Authors
Hangcheng Zhao,Ron Berman
### Background
当在线卖家使用AI学习算法自动在电子商务平台上竞争时，人们担心他们可能会竞相设定高于竞争的价格。然而，这种担忧主要集中在单一维度的价格竞争中。本文探讨了在定价和广告决策结合时，这种预测是否成立，即在两个维度上的决策竞争。使用大规模数据集提供实证证据，分析多代理强化学习中的竞争情况。
### Innovation
研究发现，在消费者搜索成本较高时，学习算法能够协调设定低于竞争的价格，对消费者、卖家和平台都有利。这发生在算法学习降低广告竞标成本，通过降低价格和增加平台需求来实现的情况之下。此外，研究结果表明，任何使用价格和广告投标探索的算法都能得到类似的结论。实证分析显示，价格水平在估计的消费者搜索成本和算法使用指数之间的互动是负向的。文章还分析了平台的战略反应，发现调整底价不会增加平台利润，而调整佣金可以使平台利润增加，并保持对卖家和消费者的好处。
### Conclusion
在消费者搜索成本较高时，学习算法可以协调设定低于竞争的价格，这将有利于消费者、卖家和平台。通过降低广告竞标成本降低价格，增加平台需求。平台通过调整佣金而非底价可以获得更好的利润，同时保持对买卖双方的好处。
## 209. `cs.AI` - PartnerMAS: 一种应用于高维度特征商业伙伴选择的大规模语言模型层次多智能体框架 [PDF](https://arxiv.org/pdf/2509.24046), [HTML](https://arxiv.org/abs/2509.24046)
### Authors
Lingyao Li,Haolun Wu,Zhenkun Li,Jiabei Hu,Yu Wang,Xiaoshan Huang,Wenyue Hua,Wenqian Wang
### Background
高维度决策任务，如业务伙伴选择，涉及评估具有异构数值、分类和文本特征的大量候选池。在这样的环境中，尽管大规模语言模型（LLMs）提供了强大的上下文推理能力，但单代理或辩论风格的系统常面临可扩展性和一致性的问题。.
### Innovation
本文提出了一种层次多代理框架——PartnerMAS，将评估分解为三个层次：规划代理设计策略、专业代理进行特定角色评估、监督代理整合输出。为了支持系统化评估，还引入了一个创投合作投资的精心筛选基准数据集，涵盖多样化的公司属性和真实的合作团体。PartnerMAS 在 140 个案例中均优于单代理和辩论式多代理基线，匹配率高出 10-15%。分析表明，规划者对领域导向的提示最敏感，专家代理提供互补的特征覆盖，监督代理在汇总中起重要作用。这种结构化的代理协作比单模型扩展产生更稳健的结果。
### Conclusion
我们的研究显示，结构化的LLM代理协作能产生比单一模型扩展更稳健的结果，突显了PartnerMAS在数据丰富的高维度决策领域的潜力。
## 210. `cs.AI` - PoseDiff: 一个统一的扩散模型在机器人姿态估计与视频到动作控制之间的桥梁 [PDF](https://arxiv.org/pdf/2509.24591), [HTML](https://arxiv.org/abs/2509.24591)
### Authors
Haozhuo Zhang,Michele Caprio,Jing Shao,Qiang Zhang,Jian Tang,Shanghang Zhang,Wei Pan
### Background
现有的机器人状态估计和控制通常需要多阶段的流程或辅助模态，以从视觉观察中提取结构化的机器人状态。这些方法通常效率低下，难以在实时应用中实现高质量的性能。随着扩散模型的兴起，研究者们开始探索如何在一个框架中实现这些任务，从而提高效率和准确性。
### Innovation
PoseDiff 是一种条件扩散模型，它在一个框架中统一了机器人的状态估计和控制。它能够单从 RGB 图像映射出结构化的机器人状态，如3D 关键点或关节角度，消除了多阶段管道或辅助模态的需求。此外，通过条件依赖于由世界模型生成的稀疏视频关键帧，PoseDiff 能够生成平滑且连续的长时间段动作序列，展示了扩散模型在机器人领域的强大潜力。
### Conclusion
PoseDiff 在 DREAM 数据集上的姿态估计达到了最先进的精度和实时性能。在 Libero-Object 操作任务中，它在严格的离线设置中也显著提升了动作精度，证明了它作为一个在物理智能体领域间具备可扩展性、准确性和效率的桥梁的有效性。
## 211. `cs.AI` - HTML中潜藏的攻击面解码：用于网页摘要的提示注入 [PDF](https://arxiv.org/pdf/2509.05831), [HTML](https://arxiv.org/abs/2509.05831)
### Authors
Ishaan Verma
### Background
大型语言模型（LLMs）已广泛集成到基于Web的系统中用于内容摘要，但它们对于提示注入攻击的脆弱性仍然是一个紧迫的问题。研究表明，不可见的HTML元素，如<meta>、aria-label和alt属性，可以被利用来嵌入恶意指令，而不改变网页的可见内容。
### Innovation
该研究引入了一个由280个静态网页构成的新数据集，其中一半是非恶意版本，另一半是含有恶意注入的版本，使用多种基于HTML的战略精心制作。这些页面通过自动化浏览器管道处理，提取原始HTML和渲染文本，模拟实际的LLM部署场景。此外，该研究评估了两个最先进的开源模型（Llama 4 Scout和Gemma 9B IT）对包含恶意注入内容的网页摘要能力的影响。
### Conclusion
研究表明，Llama 4 Scout中的29%被注入的样本导致了摘要结果的显著变化，而Gemma 9B IT也显示出15%的注入成功率。这揭示了在LLM驱动的网页管道中一个关键且被忽视的漏洞，即隐藏的恶意内容可以微妙地操纵模型输出。该研究提供了一个可复制的框架和基准，用于评估基于HTML的提示注入，并强调了在涉及Web内容的LLM应用中需要采取稳健的缓解策略的重要性。
## 212. `cs.AI` - BALR-SAM: Boundary-Aware Low-Rank Adaptation of SAM for Resource-Efficient Medical Image Segmentation [PDF](https://arxiv.org/pdf/2509.24204), [HTML](https://arxiv.org/abs/2509.24204)
### Authors
Zelin Liu,Sicheng Dong,Bocheng Li,Yixuan Yang,Jiacheng Ruan,Chenxu Zhou,Suncheng Xiang
### Background
视觉基础模型如Segment Anything Model (SAM)在大规模自然图像数据集上预训练，但往往在医学图像分割任务中表现不佳，因为缺乏针对特定领域的适应。在临床上，对于医学下游任务进行有效的细调以满足资源需求、保持高性能是非常具有挑战性的。
### Innovation
本文提出了一个边界感知的低秩适应框架BALR-SAM，用于医学成像资源高效分割。具体创新点包括：(1) 互补细节增强网络(CDEN)使用深度可分离卷积和多尺度融合来捕捉对准确分割至关重要的边界敏感特征；(2) 结合SAM的Vision Transformer块优化特征表示和同时显著减少参数空间的低秩适配器；(3) 在掩码解码器中引入低秩张量注意力机制，减少75%的内存使用并提升推理速度。实验表明，BALR-SAM无需提示也优于包括完全细调的MedSAM在内的多个最先进的方法，同时仅更新了其参数的1.8%（11.7M）。
### Conclusion
BALR-SAM在不使用提示的情况下，不仅在多个标准医学分割数据集上表现出色，而且只需要少量参数更新（1.8%），同时减少75%的内存使用并提高推理速度，解决了大规模自然图像数据预训练模型在医学图像分割中缺乏特异性适应的问题。
## 213. `cs.AI` - 源免费时间序列预测中的代理去噪不变特征解耦 [PDF](https://arxiv.org/pdf/2510.05589), [HTML](https://arxiv.org/abs/2510.05589)
### Authors
Kangjia Yan,Chenxi Liu,Hao Miao,Xinle Wu,Yan Zhao,Chenjuan Guo,Bin Yang
### Background
移动设备的普及产生了大量跨多领域的时序数据，有效的时序预测能够应用于各种现实生活场景。本文研究了一个新的源免费领域自适应问题，目标是在不使用源数据的情况下，通过预训练模型适应稀疏的目标时序数据领域，顺应数据保护法规的需求。
### Innovation
提出了TimePD框架，这是一个使用代理去噪的第一种源免费时间序列预测框架，通过大型语言模型（LLMs）的有效推广能力来实现。TimePD框架包含三个关键组件：（1）双重分支不变解耦特征学习，通过季节趋势分解确保表示和梯度上的不变性；（2）轻量级、无参数的代理去噪，动态校准LLMs的系统偏差；（3）知识蒸馏，双向对准去噪预测和原始目标预测。
### Conclusion
通过在真实数据集上的广泛实验，证明了TimePD的有效性，平均优于当前最先进的基线9.3%。
## 214. `cs.AI` - 通过强化学习探索解锁大语言模型的推理能力 [PDF](https://arxiv.org/pdf/2510.03865), [HTML](https://arxiv.org/abs/2510.03865)
### Authors
Wenhao Deng,Long Wei,Chenglei Yu,Tailin Wu
### Background
Reinforcement learning with verifiable rewards (RLVR) 近年来增强了大型语言模型 (LLMs) 的推理能力，特别是在数学问题解决方面。然而，随着采样预算的增加，RLVR 训练模型相对于其预训练基础模型的优势往往会减弱甚至消失，表明这些模型强烈依赖于基础模型的有限搜索空间。这一现象归因于逆Kullback-Leibler (KL) 发散正则化器的广泛应用，该正则化器的建模作用会将策略困在基础模型的支持区域内，阻碍广泛的探索。
### Innovation
本文提出了一种新的算法 RAPO（Rewards-Aware Policy Optimization），该算法通过利用前向KL惩罚替代逆KL惩罚来促进更广泛又集中的探索，以及重新加权参考策略以实现自适应的近分布探索。通过在 8K SimpleRL-Zero 数据集上对 Qwen2.5-3B 和 7B 模型进行 RAPO 训练(无需监督微调)，并在 AIME2024 和 AIME2025 上进行评估，结果表明 RAPO 一致地提高了问题解决性能。值得注意的是，RAPO 使模型能够超越基础模型的表现上限，并解决了 previously 无法解决的问题，从而推进了 RLVR 在具有挑战性的推理任务中应用的边界。
### Conclusion
RAPO 成功提升了 RLVR 训练模型的推理能力，特别是在具有挑战性的数学问题解决任务上，展示了作为更广泛探索的一种新策略的有效性。
## 215. `cs.AI` - 利用标识符替换的基于LLM的长代码翻译 [PDF](https://arxiv.org/pdf/2510.09045), [HTML](https://arxiv.org/abs/2510.09045)
### Authors
Manojit Chakraborty,Madhusudan Ghosh,Rishabh Gupta
### Background
在软件开发领域，LLM已被用于自动化代码翻译任务，即将一种编程语言的源代码翻译成另一种语言的同时保留其功能。然而，LLM在处理长代码时常常面临挑战，因为长代码往往超出了其上下文窗口的长度限制，导致翻译不准确。为了应对这一问题，本文提出了一个利用标识符替换的零样本代码翻译方法。通过在翻译过程中使用用户提供的长标识符替换为通用占位符，该方法使得LLM能够关注于代码的逻辑结构，通过减少token数量和内存使用，提高了长代码翻译的效率和成本效益。实验证明，该方法能够保持良好的语法和层次结构信息，并生成减少token数量的翻译结果。
### Innovation
提出了一个利用标识符替换的零样本代码翻译方法，通过在翻译过程中使用通用占位符替换长标识符，使得LLM能够更有效地处理长代码，提高翻译的准确性和效率。
### Conclusion
实验结果表明，该方法能够保持代码的语法和层次结构信息，并生成比原始方法更少token数量的翻译结果，证明了其在长代码翻译中的有效性。
## 216. `cs.AI` - 生成式AI与企业生产力：在线零售领域的现场实验 [PDF](https://arxiv.org/pdf/2510.12049), [HTML](https://arxiv.org/abs/2510.12049)
### Authors
Lu Fang,Zhe Yuan,Kaifu Zhang,Dante Donati,Miklos Sarvary
### Background
本文通过一系列大规模的随机现场实验，评估了生成式人工智能（GenAI）对一家领先跨境在线零售平台公司生产力的影响。实验涉及数百万名用户和产品，持续了2023-2024年的六个月，GenAI技术被整合到七个面向消费者的业务流程中。
### Innovation
研究采用大规模随机现场实验的方法，量化GenAI对生产力的具体影响，特别是在销售增长方面，根据GenAI的边际贡献不同，其效果范围从0%到16.3%。由于实验中保持了投入和价格的不变，这些收益直接转化为全要素生产力的提升。结果显示，对于四个具有正面效果的GenAI应用，其年度边际价值约为5美元，给零售商带来的经济影响具有重要意义。
### Conclusion
研究表明，GenAI的主要机制是提升转化率，这表明GenAI减少了市场中的摩擦并改善了消费者体验。此外，发现小企业和新手消费者受益更多。该研究为在线零售中GenAI的生产力效应提供了新颖的、大规模的因果证据，强调了其即时价值和更广泛的发展潜力。
## 217. `cs.AI` - SVTime：由大规模视觉模型预报器的‘物理法则’指导的轻量级时间序列预测模型 [PDF](https://arxiv.org/pdf/2510.09780), [HTML](https://arxiv.org/abs/2510.09780)
### Authors
ChengAo Shen,Ziming Zhao,Hanghang Tong,Dongjin Song,Dongsheng Luo,Qingsong Wen,Jingchao Ni
### Background
时间序列AI对于分析动态网页内容至关重要，推动了知识编码能力强、能在多种任务间迁移的大规模预训练模型的发展。然而，由于训练和推断时对大量计算资源和硬件的需求，这些大型模型作为通用解决方案可能会带来严重的碳足迹和可持续性问题。具体任务上，小而专业的高性能模型可能更为实用，尤其是对于资源有限的小型企业等用户而言。因此，构建具有与大型模型类似性能但成本更低的轻量级模型成为了一个关键问题。特别是在长时间序列预测（LTSF）任务上，最近的研究表明，大规模视觉模型（LVM）作为LTSF的工具展现了强有力的能力。
### Innovation
本文提出了一种新的轻量级模型SVTime，该模型受大规模视觉模型forecasters的启发，编码了相关的关键归纳偏置。SVTime设计了精心构建的线性层和约束函数来实现这些偏置，与10^3参数较少的LVM相比，性能接近大型模型，同时在资源受限环境下仍能实现高效的训练和推理。在21种基准模型中，SVTime超越了最先进的轻量级模型，并且与大规模模型相比，参数较少而性能相当。
### Conclusion
本文通过引入SVTime模型，提出了一种创新的方法，该方法在资源受限的环境下能够实现与大规模模型相媲美的高性能，同时降低了资源消耗和技术成本。这对于需要长期时间序列预测的实时应用程序和其他应用场景具有重要意义。
## 218. `cs.AI` - 通过模型合并导航对齐与校准的权衡：帕累托更优前沿 [PDF](https://arxiv.org/pdf/2510.17426), [HTML](https://arxiv.org/abs/2510.17426)
### Authors
Tiancheng Hu,Benjamin Minixhofer,Nigel Collier
### Background
通常认为后训练对齐会造成任务准确度下降，但本研究发现，这种对齐还会导致显著的校准损失，使模型变得更加自信但不可靠，且输出缺乏多样性。研究展示了通过简单的后处理干预，即在对齐前后的权重之间进行插值，可以有效应对这种权衡：发现了一致性的帕累托最优插值，即这些模型在提高准确性的同时显著恢复了对齐过程中丧失的校准。
### Innovation
研究通过简单的模型合并方法克服了对齐税的全面影响，提供了计算效率高的方法，提高了模型的能力和可靠性。这种方法揭示了帕累托更优的改进，即在保持模型优势的同时，显著恢复了对齐时损失的校准。
### Conclusion
研究表明，简单的模型合并方法可以为缓解对齐税提供一种有效的计算方法，从而产出更强大的、更可靠的模型。
## 219. `cs.AI` - I-RAVEN-X：大型语言和推理模型的类比和数学推理泛化和鲁棒性评估基准 [PDF](https://arxiv.org/pdf/2510.17496), [HTML](https://arxiv.org/abs/2510.17496)
### Authors
Giacomo Camposampiero,Michael Hersche,Roger Wattenhofer,Abu Sebastian,Abbas Rahimi
### Background
该论文引入了I-RAVEN-X，一个符号基准，旨在评估大型语言模型（LLMs）和大型推理模型（LRMs）在类比和数学推理中的泛化能力和鲁棒性。I-RAVEN-X 在 I-RAVEN 的基础上增加了操作符复杂性、属性范围，并引入了感知不确定性。与LLMs相比，实验结果显示，LRMs 在较长的推理关系和更宽的属性范围内实现了更好的生产力和系统性，但仍然在不确定性推理方面面临巨大挑战，无法有效探索多种概率性结果。
### Innovation
I-RAVEN-X 通过增加操作符复杂性、属性范围和引入感知不确定性扩展了 I-RAVEN。相较于LLMs，LRMs在处理较长的推理关系和更宽的属性范围方面表现出更好的生产力和系统性，但面对不确定性推理时表现不尽如人意。
### Conclusion
尽管LRMs在处理较长的推理关系和宽属性范围时优于LLMs，但它们在不确定性推理方面仍然面临巨大挑战，无法有效探索多种概率性结果。
## 220. `cs.AI` - DrivAerStar: 用于车辆气动优化的工业级CFD数据集 [PDF](https://arxiv.org/pdf/2510.16857), [HTML](https://arxiv.org/abs/2510.16857)
### Authors
Jiyan Qiu,Lyulin Kuang,Guan Wang,Yichen Xu,Leiyao Cui,Shaotong Fu,Yixin Zhu,Ruihua Zhang
### Background
随着汽车电动化的推进，车辆空气动力学优化变得越来越重要，其中阻力减少直接决定了电动汽车的续航能力和能源效率。传统方法面临计算成本高昂的CFD仿真，每次设计迭代需要数周时间，或者简化模型牺牲生产级精度的问题。虽然机器学习提供了潜力，但现有数据集存在根本限制，如不足的网格分辨率、缺失的车辆部件和验证错误率超过5%，无法在工业流程中部署。传统方法的瓶颈在于时间和成本，而现有数据集则因为精度不足而无法满足高级应用的需求。
### Innovation
DrivAerStar数据集包含12,000个使用STAR-CCM+生成的工业级汽车CFD仿真，通过Free Form Deformation (FFD)算法系统地探索了三种车辆配置，涵盖了完整的发动机舱和冷却系统，实现了与真实内部气流一致的仿真。DrivAerStar实现了低于1.04%的风洞验证精度，比现有数据集提高了五倍，通过精细的网格策略和严格的壁面 $y^+$ 控制实现。这种数据集首次将学术机器学习研究与工业CFD实践结合，为使用高保真物理仿真与人工智能的车辆开发提供了新的基准。
### Conclusion
DrivAerStar为车载动力优化提供了第一个高精度工业级CFD数据集，显著降低了计算成本并提高了模型的生产级精度。在汽车行业之外，DrivAerStar展示了在计算约束受限的工程学科中，如何将高保真物理仿真与人工智能集成进行创新的新范例。”lichtenberg符号或其他字符已替换为符合JSON规范的内容。
## 221. `cs.AI` - CARE: 对事件触发传感器流的日常生活活动识别的对比对齐方法 [PDF](https://arxiv.org/pdf/2510.16988), [HTML](https://arxiv.org/abs/2510.16988)
### Authors
Junhao Zhao,Zishuai Liu,Ruili Fang,Jin Lu,Linghan Zhang,Fei Dou
### Background
在辅助生活环境中，日常活动（ADLs）的识别是从事件触发的环境传感器中提取的重要任务。然而，现有的方法仍然受制于表示层面的限制。基于序列的方法保留了传感器激活的时间顺序，但对噪声敏感且缺乏空间感知；而基于图像的方法则捕捉全局模式和隐含的空间相关性，但压缩了细粒度的时间动态并失真了传感器布局。简单的融合方法（例如，特征连接）不能在序列和图像表征视图之间强制对齐，从而未能充分利用二者互补的优势。
### Innovation
我们提出了一种名为CARE的端到端框架，即对比对齐辅助日常生活活动识别，通过序列-图像对比对齐（SICA）和交叉熵分类优化表示学习，确保了跨表示对齐和任务特定可区分性。CARE整合了（i）具有时间感知和噪声鲁棒性的序列编码；（ii）具有空间信息和频率敏感性的图像表示；以及（iii）联合对比度-分类目标，用于端到端学习对齐和可区分嵌入。评估结果显示，CARE在米兰、开罗和京都7个数据集上的表现均达到最先进的性能（分别为89.8%、88.9%和73.3%），并且表现出对传感器故障和布局变化的鲁棒性，表明其在智能家庭中实现可靠ADL识别的潜力.
### Conclusion
CARE在三个CASAS数据集上的评估结果表明，它达到了最先进的性能，展示了对传感器故障和布局变化的稳健性，突显了其在智能家庭中实现可靠ADL识别的潜力。
## 222. `cs.AI` - ε-Seg: 非监督的显微镜数据语义分割 [PDF](https://arxiv.org/pdf/2510.18637), [HTML](https://arxiv.org/abs/2510.18637)
### Authors
Sheida Rahnamai Kordasiabi,Damian Dalle Nogare,Florian Jug
### Background
电子显微镜（EM）图像中的生物样本语义分割在生命科学中仍然是一项挑战。EM 数据捕捉生物结构的细节，有时过于复杂，即便是人类观察者也会感到困难重重。现有的方法在处理低密度训练标签时表现不佳，不足以准确区分所需的类别。因此，迫切需要开发新的方法来有效地进行非监督语义分割，特别是在训练标签稀少的情况下。
### Innovation
ε-Seg 引入了一种基于分层变分自动编码器（HVAEs）的方法，结合了中心-区域掩码、稀疏标签对比学习（CL）、高斯混合模型（GMM）先验以及无聚类的标签预测。通过中心-区域掩码和修复损失，鼓励模型在少量（甚至少至 0.05%）训练标签下学习稳健且具代表性的嵌入，从而区分所需的类别。同时，CL 和 GMM 先验有助于塑造 HVAE 的潜在空间，使得编码输入斑块按所需语义类别进行聚类。最终，ε-Seg 不依赖于聚类潜在嵌入进行语义分割，而是提出了一种直接从潜在嵌入预测类别标签的MLP语义分割头部。该方法在两个密集的生物组织 EM 数据集和荧光显微镜数据上显示出优越性和适用性。
### Conclusion
实验结果表明，即使只有少量的训练标签可用，ε-Seg 也能实现竞争性的稀疏监督分割结果，即使在复杂生物图像数据中也能达到良好的分割效果。
## 223. `cs.AI` - E2Rank：您的文本嵌入模型也可以成为有效的高效率列表级重排器 [PDF](https://arxiv.org/pdf/2510.22733), [HTML](https://arxiv.org/abs/2510.22733)
### Authors
Qi Liu,Yanzhao Zhang,Mingxin Li,Dingkun Long,Pengjun Xie,Jiaxin Mao
### Background
文本嵌入模型是现实世界搜索应用中的基本组件，通过将查询和文档映射到共享的嵌入空间，可以实现高效且具有竞争力的检索性能。然而，相对于专门的重排器，尤其是在最新的基于大语言模型的列表级重排器，它们在捕获细粒度的查询-文档和文档-文档交互方面仍然存在限制。
### Innovation
提出了一个简单有效的统一框架E2Rank，该框架通过在列表级排名目标下持续训练将单一文本嵌入模型扩展既能执行高质量检索又能进行列表级重排，从而在保持高效性和表示质量的同时显著提高其重排性能。
### Conclusion
E2Rank在BEIR重排基准测试中取得了最先进的结果，并在推理密集型BRIGHT基准测试中表现出竞争力的表现，同时具有极低的重排延迟。我们的研究结果表明，单一嵌入模型可以有效地统一检索和重排，提供计算效率和竞争力的排名准确性。
## 224. `cs.AI` - 医学中的变换器：提高医学图像标注中的视觉-语言对齐 [PDF](https://arxiv.org/pdf/2510.25164), [HTML](https://arxiv.org/abs/2510.25164)
### Authors
Yogesh Thakku Suresh,Vishwajeet Shivaji Hogale,Luca-Alexandru Zamfira,Anandavardhana Hegde
### Background
本文提出了一种基于变换器的多模态框架，用于生成与MRI扫描相关的临床相关描述。该系统结合了DEiT-Small视觉变换器作为图像编码器，MediCareBERT进行描述嵌入，并使用基于LSTM的自定义解码器。通过使用混合余弦-MSE损失和矢量相似性的对比推理，该架构旨在语义上对齐图像和文本嵌入。作者在MultiCaRe数据集上对系统进行了评估，与当前最先进的医学图像描述方法（如BLIP、R2GenGPT及近期的基于变换器的方法）进行了对比，实验结果表明关注专门领域数据可以提高描述准确性及语义对齐度。
### Innovation
引入了一种新颖的基于变换器的多模态框架，结合DEiT-Small视觉变换器、MediCareBERT和基于LSTM的自定义解码器，使用混合余弦-MSE损失及对比推理，提出了一种可扩展、可解释的自动化医学影像报告解决方案。
### Conclusion
通过专注于特定领域的数据，作者的框架能够提升基于不同MRI类型的描述准确性和语义对齐度。提出的方法为医学影像报告提供了一种可持续的、可解释的解决方案。
## 225. `cs.AI` - SmartMixed：一种用于神经网络自适应激活函数学习的两阶段训练策略 [PDF](https://arxiv.org/pdf/2510.22450), [HTML](https://arxiv.org/abs/2510.22450)
### Authors
Amin Omidvar
### Background
激活函数在神经网络中的选择至关重要，但大多数架构仍在使用固定、统一的激活函数。网络在不同神经元之间进行适配和优化激活函数的选择，以实现计算效率和功能多样性的平衡。
### Innovation
提出了SmartMixed，这是一种两阶段训练策略，允许网络学习最优的基于神经元的激活函数，同时保持推理阶段的计算效率。在第一阶段，神经元通过可微分的硬混合机制从一组候选激活函数（ReLU、Sigmoid、Tanh、Leaky ReLU、ELU、SELU）中选择。在第二阶段，每个神经元的激活函数固定为学习到的选择，从而生成一个计算高效的网络，并支持继续训练和优化的向量化操作。
### Conclusion
SmartMixed在MNIST数据集上使用不同深度的前馈神经网络进行评估，结果显示不同层的神经元对激活函数有明显不同的偏好，揭示了神经架构内的功能多样性。
## 226. `cs.AI` - MMEdge：通过流水线传感器和编码加速设备端多模态推理 [PDF](https://arxiv.org/pdf/2510.25327), [HTML](https://arxiv.org/abs/2510.25327)
### Authors
Runxi Huang,Mingxuan Yu,Mingyu Tsoi,Xiaomin Ouyang
### Background
实时多模态推理在诸如自动驾驶、人机交互和移动健康等应用中是必要的。然而，先前的工作往往忽视了传感动态与模型执行之间的紧密耦合，以及不同模态之间的复杂互动依赖关系。
### Innovation
本文提出了一种名为MMEdge的新型设备端多模态推理框架，基于流水线检测和编码。它将整个推理过程分解为一系列细粒度的检测和编码单元，允许随着数据到达逐步进行计算。MMEdge还引入了一个轻量且有效的时序聚合模块，以捕捉不同流水线单元中的丰富时序动态，从而保持准确性能。此外，MMEdge结合了适应性多模态配置优化器和跨模态推测性跳过机制，以适应资源和输入数据复杂性变化，提升系统性能。
### Conclusion
我们使用两个公开的多模态数据集在实际无人机（UAV）多模态测试床中对MMEdge进行评估。结果表明，MMEdge在保持高任务准确性的基础上，显著减少了端到端延迟。
## 227. `cs.AI` - DINO-YOLO: 自监督预训练在土木工程应用中高效目标检测 [PDF](https://arxiv.org/pdf/2510.25140), [HTML](https://arxiv.org/abs/2510.25140)
### Authors
Malaisree P,Youwai S,Kitkobsin T,Janrungautai S,Amorndechaphon D,Rojanavasu P
### Background
在土木工程应用中，目标检测受限于特定领域标注数据的不足。这限制了在这些领域中实现高效目标检测的能力。
### Innovation
DINO-YOLO通过结合YOLOv12与DINOv3自我监督的视觉变换器，提出了一种新的混合架构，用于数据高效的检测。DINOv3特征在输入预处理（P0）和中层主干增强（P3）两个位置进行了策略性集成，展示了显著的进步：在隧道段裂缝检测（648张图像）、建筑安全防护装备检测（1000张图像）和KITTI数据集的表现分别提高了12.4%、13.7%和88.6%，同时保持实时推理速度（30-47 FPS）。系统研究发现，中型架构在P0P3双集成下表现最佳，达到55.77%的mAP@0.5；小型架构则需要三集成，表现为53.63%。相对于8-16ms的基线，额外的2-4倍推理开销（21-33ms）在NVIDIA RTX 5090上仍可供野外部署使用。该研究为土木工程应用中的数据稀缺环境提供了高效的解决方案，同时保持了计算效率，为施工现场安全监控和基础设施检查提供了实用的辅助工具
### Conclusion
DINO-YOLO在数据量小于10K的土木工程数据集上达到了最先进的性能，同时保持了计算效率，为解决土木工程应用中的数据有限问题提供了切实可行的方法。
## 228. `cs.AI` - TempoPFN：线性RNN的合成预训练用于零样本时间序列预测 [PDF](https://arxiv.org/pdf/2510.25502), [HTML](https://arxiv.org/abs/2510.25502)
### Authors
Vladyslav Moroshan,Julien Siems,Arber Zela,Timur Carstensen,Frank Hutter
### Background
当前时间序列预测模型在长周期预测和重复性方面存在效率问题，现有的仅依赖合成数据的方法在挑战性基准测试中表现不佳。
### Innovation
提出了 TempoPFN，一种基于线性循环神经网络（RNN）的一元时间序列基础模型，该模型专门在合成数据上进行预训练。模型采用 GatedDeltaProduct 架构与状态编织技术，实现序列长度的完全并行化训练，无需窗口化或总结技术，同时保持强大的时间状态追踪能力。该模型通过综合多种生成器（包括随机微分方程、高斯过程和音频合成）的数据生成管道，并加入新颖的增强技术，实现了在Gift-Eval基准测试中的顶级竞争性能，优于所有现有的基于合成数据的方法，并且在效率方面优于现有基线。
### Conclusion
作者开源了其完整数据生成管道和训练代码，为未来研究提供了一个可重复的基础框架。
## 229. `cs.AI` - 基于过程挖掘的软件开发工作流分析与预测系统 [PDF](https://arxiv.org/pdf/2510.25935), [HTML](https://arxiv.org/abs/2510.25935)
### Authors
Antía Dorado,Iván Folgueira,Sofía Martín,Gonzalo Martín,Álvaro Porto,Alejandro Ramos,John Wallace
### Background
CodeSight 是一个全面的系统，旨在预测软件开发工作流中的截止时间遵守情况。它直接从 GitHub 捕获开发和部署数据，并将这些数据转化为过程挖掘日志进行详细分析。通过分析这些日志，系统生成经过结构化的指标和仪表板，提供有关 PR 活动模式和工作流效率的可操作见解。CodeSight 利用长短期记忆（LSTM）模型预测 PR 解决剩余时间，基于顺序活动轨迹和静态特征进行预测，有助于早期识别潜在的截止时间违反情况。
### Innovation
此系统的独特之处在于它结合了过程挖掘方法和机器学习技术，建立了基于 LSTM 的模型来预测 PR 的剩余解决时间。该系统能够根据软件项目中的具体活动轨迹和静态特征，预测剩余的完成时间，从而实现软件项目的主动管理。
### Conclusion
CodeSight 系统通过高精度和 F1 分数在预测截止时间合规方面的性能证明了过程挖掘与机器学习相结合的价值。这表明，这种系统可以为软件开发团队提供有价值的见解和预警，帮助他们在项目中实现更有效的管理。
## 230. `cs.AI` - 《Studies for》：一种基于实时多通道声音生成模型的人机共创声音艺术作品 [PDF](https://arxiv.org/pdf/2510.25228), [HTML](https://arxiv.org/abs/2510.25228)
### Authors
Chihiro Nagashima,Akira Takahashi,Zhi Zhong,Shusuke Takahashi,Yuki Mitsufuji
### Background
该研究探讨了将AI技术整合到艺术创作工作流程中的方法，通过与声音艺术家Evala合作创作的《Studies for》进行研究，《Studies for》是一个生成声音装置，使用了SpecMaskGIT模型实时生成和播放多通道声音，具有高度沉浸的声音体验。该作品基于“新形式的档案”理念，旨在保留艺术家艺术风格的同时，通过持续生成新的声音元素扩展艺术家的作品范围。
### Innovation
提出了一种人机共创框架，用于有效将声音生成AI模型融入声音艺术创作过程，建议利用艺术家过去作品的数据集进行训练，同时确保包括意想不到的新颖输出。该模型设计以反映艺术家的艺术身份为基础，生成新的、从未听过的声音，实现“新形式的档案”概念。
### Conclusion
该研究促进了声音艺术中人机共创的可能性，提出了一个整合声音生成AI模型的人机共创框架，并为延续和扩展艺术家的作品提供了新的方法。这种方法不仅有助于档案保存，还能激发新的艺术表达形式。
## 231. `cs.AI` - Aeolus: 多结构航班延误数据集 [PDF](https://arxiv.org/pdf/2510.26616), [HTML](https://arxiv.org/abs/2510.26616)
### Authors
Lin Xu,Xinyun Yuan,Yuxuan Liang,Suwan Yin,Yuankai Wu
### Background
现有的航班延误数据集通常局限于平面的表格结构，无法捕捉到延误传播过程中固有的时空动态。这限制了研究者们在预测航班延误和开发针对表格数据的基础模型方面的进展。
### Innovation
Aeolus 数据集通过提供三种对齐的模态来解决这一限制：（i）一个包含丰富运营、气象和机场层面特征的表格数据集，覆盖超过5000万个航班；（ii）一个航班链模块，模型沿顺序航班段的延误传播，捕捉上游和下游依赖性；（iii）一个航班网络图，编码共享飞机、机组和机场资源连接，允许跨航班关系推理。该数据集经过精心构建，分为时间分割，具有全面的特征和严格的泄漏预防，支持真实的和可复制的机器学习评估。
### Conclusion
Aeolus 数据集支持回归、分类、时间结构建模和图学习等多种任务，作为跨表格、序列和图模态的统一基准。我们发布基础实验和预处理工具来促进采用。Aeolus 充分填补了特定领域的建模和通用结构数据的关键空白。可以通过以下链接访问源码和数据：&lt;this https URL&gt;.
## 232. `cs.AI` - 真正的端到端语言模型：自动解码终结手动解码 [PDF](https://arxiv.org/pdf/2510.26697), [HTML](https://arxiv.org/abs/2510.26697)
### Authors
Zhichao Wang,Dongyang Ma,Xinting Huang,Deng Cai,Tian Lan,Jiahao Xu,Haitao Mi,Xiaoying Tang,Yan Wang
### Background
当前对大型语言模型（LLMs）的‘端到端’标签存在误导，实际上它们依赖于非可微分的解码过程，需要手动调整如温度、top-p等超参数。这限制了模型的灵活性和性能。
### Innovation
提出了AutoDeco，一种新架构，通过在每个步骤动态预测上下文特定的温度和top-p值来实现真正‘端到端’的生成。该方法将解码转换为参数化的、按token级的过程，使模型能够在一个前向通路中自我调节其采样策略。实验结果显示AutoDeco不仅显著优于默认解码策略，还实现了与‘破解测试集’调优基线相当的性能，揭示了基于指令的解码控制能力。
### Conclusion
AutoDeco不仅克服了传统解码策略的限制，还提供了一种新的可引导和互动的LLM解码范式。
## 233. `cs.AI` - 关于仅使用单一训练种子评估机器遗忘的局限性 [PDF](https://arxiv.org/pdf/2510.26714), [HTML](https://arxiv.org/abs/2510.26714)
### Authors
Jamie Lanyon,Axel Finke,Petros Andreou,Georgina Cosma
### Background
机器遗忘（MU）目标是在不需重新训练昂贵的情况下移除某些数据点对训练模型的影响。大多数实际的MU算法只能提供近似效果，其性能只能通过实验方法评估。因此，必须谨慎地进行实验比较以使其尽可能具代表性。一种常见做法是从相同的训练模型开始独立地多次运行MU算法。然而，研究表明，即使对于相同的架构和相同的数据集，某些MU方法对用于模型训练的随机数种子的选择也极为敏感，这可能导致实验结果严重缺乏代表性。
### Innovation
这项工作展示了仅使用单一训练种子进行实验评估机器遗忘方法可以导致高非代表性的结果。因此，作者建议在比较MU算法时，也应该反映不同模型训练种子的变异性。
### Conclusion
研究结果强调，在评估机器遗忘算法时应采用更全面的方法，通过反映不同的模型训练种子来提高实验结果的代表性。
## 234. `cs.CL` - MEDIQA-OE 2025年医疗订单提取共享任务概述 [PDF](https://arxiv.org/pdf/2510.26974), [HTML](https://arxiv.org/abs/2510.26974)
### Authors
Jean-Philippe Corbeil,Asma Ben Abacha,Jerome Tremblay,Phillip Swazinna,Akila Jeeson Daniel,Miguel Del-Agua,Francois Beaulieu
### Background
临床记录越来越多地使用自动语音识别和摘要，但将对话转化为用于电子健康记录的可操作医疗命令尚未得到探索。解决这个问题可以显著减轻医务人员的记录负担，并直接改善下游的患者护理。因此，需要一个专门的任务来应对这个问题。
### Innovation
介绍了MEDIQA-OE 2025共享任务，这是第一次针对从医生-患者咨询中提取医疗命令的挑战。六个团队参与了该任务，尝试了广泛的方法和技术，包括闭合和开放权重的大语言模型。
### Conclusion
本文描述了MEDIQA-OE任务、数据集、最终排行榜以及参与者的方法。
## 235. `cs.AI` - 通过高级采样实现忠实且快速的影响函数 [PDF](https://arxiv.org/pdf/2510.26776), [HTML](https://arxiv.org/abs/2510.26776)
### Authors
Jungyeon Koh,Hyeonsu Lyu,Jonggyu Jang,Hyun Jong Yang
### Background
影响函数（IFs）提供了一种后验解决方案，通过使用梯度和Hessian来解释训练数据对黑盒模型的影响。然而，计算整个数据集的Hessian矩阵在资源上是密集和昂贵的。因此，通常采用的方法是随机采样一小部分训练数据，但这种方法往往会导致IF估计值的高度不一致，因为样本配置具有高方差。
### Innovation
本文提出了一种新的方法，通过基于特征和logits的高级采样技术来选择一小部分具有代表性的数据集子集，从而增强IF估计的准确性。与基础方法相比，该方法计算时间减少了30.1%，内存使用减少了42.2%，或者提高了F1分数2.5%。
### Conclusion
本文通过特征或logits的随机分布选择一小部分数据集，提出了一种改进的影响函数方法。这种方法通过减少计算时间和内存使用，提高了影响函数的准确性，并通过类别移除实验验证了方法的有效性。
## 236. `cs.CL` - 理解并增强Mamba-Transformer 嵌合体以提升记忆召回和语言建模 [PDF](https://arxiv.org/pdf/2510.26912), [HTML](https://arxiv.org/abs/2510.26912)
### Authors
Hyunji Lee,Wenhao Yu,Hongming Zhang,Kaixin Ma,Jiyeon Kim,Dong Yu,Minjoon Seo
### Background
结合状态空间模型（SSMs）和注意力机制的混合模型已经在利用SSMs的高效性和注意力机制的高召回能力方面展示了强大的性能。然而，这些混合模型的架构设计选择仍然不够充分地被理解。
### Innovation
文章通过分析记忆利用率和整体性能来审视混合架构，并提出了一种补充方法来进一步增强其效果。首先，文章分析了SSM和注意力层的顺序集成与并行集成的区别。研究揭示了一些有趣的发现，包括顺序混合模型在较短上下文中表现更好，而并行混合模型在较长上下文中更有效。此外，文章还介绍了一种以数据为中心的方法，通过在增强的数据集上持续训练来进一步提高召回率，同时保持其他能力。这种方法在不同的基础模型上具有良好的泛化性，并优于旨在提升召回率的架构修改。
### Conclusion
研究结果为混合SSM-注意力模型提供了更深入的理解，并为根据各种应用场景设计架构提供了实际指导。
## 237. `cs.AI` - 非凸的空中异构联邦学习：偏差-方差权衡 [PDF](https://arxiv.org/pdf/2510.26722), [HTML](https://arxiv.org/abs/2510.26722)
### Authors
Muhammad Faraz Ul Abrar,Nicolò Michelusi
### Background
空中联邦学习（OTA-FL）被认为是利用无线多址信道中的波形叠加来在单次使用中聚合模型更新的一种可扩展范式。现有OTA-FL设计大多通过假定一致的无线条件（等路径损耗）或强制零偏差更新来保证收敛性，但在异构无线场景下，这些设计会受限于最弱设备并放大更新方差。此外，之前的偏移OTA-FL分析大多集中在凸目标函数上，而现代AI模型通常是非凸的。鉴于上述差距，研究了在无线异构环境中，使用随机梯度下降（SGD）的非凸OTA-FL。
### Innovation
开发了新型OTA-FL SGD更新，允许结构化的、时间不变的模型偏差，同时减少方差更新。推导了有限时间稳态界（期望的时间平均平方梯度范数），明确揭示了偏差与方差之间的权衡。提出了非凸的联合OTA功率控制设计，并开发了一种仅需基站具有统计CSIData的有效连续凸逼近算法。实验证明了该方法：基于SCA的设计通过优化偏差加速了收敛，提高了泛化能力超过先前的OTA-FL基线。
### Conclusion
通过优化偏差，SCA基于的设计加快了收敛并且优于之前的OTA-FL基线，在非凸的图像分类任务中提高了泛化能力。
## 238. `cs.CL` - 为高效语言模型的弹性架构搜索 [PDF](https://arxiv.org/pdf/2510.27037), [HTML](https://arxiv.org/abs/2510.27037)
### Authors
Shang Wang
### Background
随着大型预训练语言模型在自然语言理解（NLU）任务中的重要性不断增加，这些模型对计算能力和内存的需求也引发了经济和环境方面的重大担忧。
### Innovation
本文介绍了一种新颖的神经架构搜索（NAS）方法——弹性语言模型（ELM），该方法旨在优化紧凑型语言模型。ELM 通过引入灵活的搜索空间和高效的变压器块以及动态调整维度和头数的模块，扩展了现有的NAS方法。此外，ELM 还引入了新的知识蒸馏损失，以保留每个模块的独特特征，从而在搜索过程中增强对架构选择的区分能力。这些创新提高了搜索过程的效率和灵活性，有助于更深入和有效的模型架构探索。
### Conclusion
实验结果表明，通过ELM发现的模型显著优于现有方法，尤其是在掩码语言建模和因果语言建模任务中表现突出。
## 239. `cs.CL` - 框架语义模式在医疗保健领域识别可报告事件漏报中的应用：基于性别暴力的案例 [PDF](https://arxiv.org/pdf/2510.26969), [HTML](https://arxiv.org/abs/2510.26969)
### Authors
Lívia Dutra,Arthur Lorenzi,Laís Berno,Franciany Campos,Karoline Biscardi,Kenneth Brown,Marcelo Viridiano,Frederico Belcavello,Ely Matos,Olívia Guaranha,Erik Santos,Sofia Reinach,Tiago Timponi Torrent
### Background
本文提出了一种方法论，用于识别医疗领域中的可报告事件。该方法利用语义框架定义精细模式，并在非结构化数据（如电子病历中的开放式文本字段）中搜索这些模式。这一过程应用于识别电子病历中患者访问初级保健单位时性别暴力（GBV）漏报的问题。通过对2100万条巴西葡萄牙语句子的语料库进行分析，成功识别了八种模式，并通过语言学家的手工评估验证了精确度。研究结果表明该方法的有效性，具有较高的精确度（0.726），并确认其稳健性。这种方法可以适应其他健康监督领域，支持更广泛、道德和可解释的自然语言处理在公共卫生系统中的应用。
### Innovation
本文创新性地构建了一个基于语义框架的方法论，用于识别可报告事件并应用于性别暴力问题。该方法通过定义和搜索精确模式应用于电子病历的开放式文本字段。这种方法透明、高效、无碳足迹且语言无关，适合广泛的健康监督应用。
### Conclusion
该研究揭示了所提出方法在识别电子病历中的性别暴力报告的高精密度（0.726），并验证了该方法的有效性和稳健性。所提出的方法可以作为公共卫生系统中自然语言处理的应用支持工具，促进其更广泛的、道德的和可解释的使用。
## 240. `cs.CL` - Kad：一种基于背包近似舍弃的代理测试时对齐框架 [PDF](https://arxiv.org/pdf/2510.27017), [HTML](https://arxiv.org/abs/2510.27017)
### Authors
Ayoub Hammal,Pierre Zweigenbaum,Caio Corro
### Background
先前的研究指出，大型语言模型（LLM）的主要生成能力在预训练过程中获得，但LLM仍需进一步调整以满足下游任务需求和风格偏好等其他期望特性。随着LLM规模扩大，对齐过程的计算成本变得极其高昂。本文背景在于解决这一对齐难题。
### Innovation
本文提出了一种基于代理的测试时对齐方法（即使用较小对齐模型的指导），通过令牌特定级联方法并且将其令牌特定的推迟规则简化为0-1背包问题来实现。该方法通过导出原始和对偶近似来优化推迟决策，并展示了其在任务性能和推测性解码速度方面的优势。
### Conclusion
本文提出的方法在任务表现和推测性解码速度上均表现出色，提供了一种有效降低大规模语言模型对齐成本的新途径。
## 241. `cs.CL` - 提高会话AI服务隐私性的语义感知LLM代理 [PDF](https://arxiv.org/pdf/2510.27016), [HTML](https://arxiv.org/abs/2510.27016)
### Authors
Jayden Serenari,Stephen Lee
### Background
随着会话AI系统的使用增加，隐私泄露的问题也越来越受到关注，尤其是用户在与大规模语言模型（LLMs）交互时分享敏感个人信息时。这些对话可能包含个人可识别信息（PII），如果泄露，可能会导致安全漏洞或身份盗窃。为了应对这一挑战，本研究提出了LOPSIDED框架，这是一种语义感知的隐私代理，旨在在使用远程LLMs时保护敏感的PII数据。现有的许多方法往往会降低对话响应的质量，而LOPSIDED则通过动态用语义一致的假名替换用户提示中的敏感实体，以保持对话的语境完整性。
### Innovation
LOPSIDED框架是一种语义感知的隐私保护方法，它在保护用户隐私的同时，能够保持对话的语境完整性。不同于以往的方法可能会降低响应质量，该框架动态地用语义一致的假名替换用户提示中的敏感实体，确保用户接收到准确且隐私保护的输出。此外，LOPSIDED还能够自动去假名化，保证用户最终得到的响应准确无误。与基线技术相比，LOPSIDED将语义效用错误减少了5倍，并且提高了隐私保护效果。
### Conclusion
本研究提出了LOPSIDED框架，这是一种语义感知的隐私代理，能够在保护用户敏感信息的同时，保持对话的语境完整性。实验结果显示，相比于现有技术，LOPSIDED显著降低了语义效用错误，提高了隐私保护的效果。
## 242. `cs.CL` - 从数字人文视角看定量互文性：一项综述 [PDF](https://arxiv.org/pdf/2510.27045), [HTML](https://arxiv.org/abs/2510.27045)
### Authors
Siyu Duan
### Background
在文学理论中，文本间的联系被称为互文性，它已经成为许多数字人文研究中的重要理论基础。近年来，自然语言处理技术的进步推动了定量互文性研究的发展。基于先进方法的大规模互文性研究不断涌现。本论文提供了一条定量互文性研究的路线图，总结了相关数据、方法和应用，并涵盖了多种语言和话题的方法从统计学到深度学习的应用，同时介绍了这些方法在人文与社会科学中的应用及其相关的平台工具。随着计算机技术的进步，可以期待更精确、多样和大规模的互文本研究。互文性在跨学科研究中的应用前景良好，特别是与人工智能和人文科学的结合方面。
### Innovation
论文提供了一条定量互文性研究的路线图，总结了相关数据、方法和应用，并涵盖了多种语言和话题的方法从统计学到深度学习的应用，同时介绍了这些方法在人文与社会科学中的应用及其相关的平台工具。
### Conclusion
定量互文性研究有望在跨学科研究中得到更广泛的应用，特别是在人工智能与人文科学的结合方面。
## 243. `cs.CL` - 递归数词系统高度有序且易于处理 [PDF](https://arxiv.org/pdf/2510.27049), [HTML](https://arxiv.org/abs/2510.27049)
### Authors
Ponrawee Prasertsom,Andrea Silvi,Jennifer Culbertson,Moa Johansson,Devdatt Dubhashi,Kenny Smith
### Background
先前的研究认为，递归数词系统优化了词汇表大小与平均句法复杂度之间的权衡（Denić和Szymanik,2024）。然而，证明只有自然语言类型的系统能够最优地实现这一权衡是切实的，现有解决方案依赖于一些人为设定的约束条件来排除不自然的系统（Yang和Regier,2025）。这一问题的核心在于提出的权衡忽视了规律性，这是人类语言语法中一个至关重要的复杂性方面。
### Innovation
作者通过接纳最小描述长度（MDL）的方法，提出递归数词系统更应被视为在规律性和处理复杂性方面的高效系统。他们的MDL基方法更准确地捕捉了现实语言系统和可能但未被证实系统之间的关键差异，包括之前工作的“最优”递归数词系统，并且证明了之前文献中的人为约束条件自然地源于规律性。
### Conclusion
该方法强调在研究语言优化问题时需要涵盖形式集合中的规律性。
## 244. `cs.CL` - VISTA Score: Verification In Sequential Turn-based Assessment [PDF](https://arxiv.org/pdf/2510.27052), [HTML](https://arxiv.org/abs/2510.27052)
### Authors
Ashley Lewis,Andrew Perrault,Eric Fosler-Lussier,Michael White
### Background
对话AI系统在需要事实可靠性的环境中部署受到幻觉问题的重大阻碍，即生成未被现有证据或对话上下文支持或反驳的陈述。当前的评估指标要么仅评估孤立的响应，要么将无法验证的内容视为错误，这限制了它们在多轮对话中的应用。
### Innovation
VISTA（Verification In Sequential Turn-based Assessment）框架引入了一种基于断言级别的验证和顺序一致性跟踪的方法来评估对话事实性。它将每个助手的回合分解为独立的事实断言，对其进行可信来源和对话历史的验证，并将无法验证的陈述分类为主观、矛盾、缺乏证据或中立。
### Conclusion
VISTA在八个大型语言模型和四个对话事实性基准（AIS、BEGIN、FAITHDIAL和FADE）中显著改善了幻觉检测性能，与FACTSCORE和LLM-as-Judge基准相比。人类评估确认了VISTA的分解有助于增加标注者的共识，并揭示了现有基准中的不一致性。通过将事实性建模为对话的动态属性，VISTA为对话系统提供了更透明、与人类一致的真实度衡量标准。
## 245. `cs.CL` - 由硬注意力变压器计算的概率分布 [PDF](https://arxiv.org/pdf/2510.27118), [HTML](https://arxiv.org/abs/2510.27118)
### Authors
Andy Yang,Anej Svete,Jiaoda Li,Anthony Widjaja Lin,Jonathan Rawski,Ryan Cotterell,David Chiang
### Background
现有大多数关于变压器的表达性结果都将变压器视为语言识别器（接受或拒绝字符串），而不是实践中所使用的语言模型（自回归和概率地生成字符串）。
### Innovation
作者研究了变压器语言模型能够表达的概率分布，展示了将变压器语言识别器转换为自回归形式有时可以增强其表达性，并且使其概率化可以破坏非概率性情况下的等价性。
### Conclusion
整体贡献在于区分了作为语言模型使用的变压器能够表达的功能，明确了它们在最常见的应用场景下的特点。
## 246. `cs.CL` - 大规模语言模型中选择性拒绝偏见的特征化 [PDF](https://arxiv.org/pdf/2510.27087), [HTML](https://arxiv.org/abs/2510.27087)
### Authors
Adel Khorramrouz,Sharon Levy
### Background
在大规模语言模型（LLMs）中开发了安全护栏以防止恶意用户大规模生成有毒内容。然而，这些措施可能会无意中引入或反映新的偏见，因为LLMs可能会拒绝生成针对某些人口群体的有害内容，而不针对其他群体。
### Innovation
本文通过探讨被拒绝的目标个人和交叉人口群体的认知率、LLMs回复类型和生成拒绝的长度，研究了LLMs安全护栏中的选择性拒绝偏见，并发现了性别、性取向、国籍和宗教属性方面的选择性拒绝偏见。此外，通过针对此前被拒绝的群体进行间接攻击来研究其他安全影响。
### Conclusion
本文强调了在不同人口群体中需要更公平和稳健的安全护栏表现的需求。
## 247. `cs.CL` - Hausa性骚扰检测数据集创建及基线模型 [PDF](https://arxiv.org/pdf/2510.27038), [HTML](https://arxiv.org/abs/2510.27038)
### Authors
Fatima Adam Muhammad,Shamsuddeen Muhammad Hassan,Isa Inuwa-Dutse
### Background
性别歧视通过维持刻板印象、偏见和歧视性规范延续并加剧性别不平等和社会排斥。随着在线平台允许各种形式的性别歧视蓬勃发展，有效地检测和缓解性别歧视成为当务之急。尽管在资源丰富语言中，对于性别歧视的检测已经有了广泛应用，但在资源匮乏的语言中，由于有限的语言资源和文化差异，性别歧视的表达和认知方式也有所不同，进步相对有限。因此，这篇研究介绍了一个基于社区参与、定性编码和数据增强方法开发的豪萨语性别歧视检测数据集。开展了一项涉及六十六名本土讲豪萨语用户的两阶段用户研究，以探索日常话语中性别歧视的定义和表达方式。进一步实验了传统机器学习分类器和预训练多语言语言模型，评估在豪萨语中检测性别歧视的少样本学习效果。研究发现，捕捉文化细微差别具有挑战性，尤其是对于需要澄清和惯用表达的情况，许多情况容易出现误报。
### Innovation
该研究首次创建了豪萨语性别歧视检测数据集，开发过程中融入了社区参与、定性编码和数据增强方法。通过两阶段用户研究（涉及66名豪萨语母语者）探索性别歧视在日常对话中的定义和表达方式。该研究还实验了传统机器学习分类器与预训练多语言模型，探讨少样本学习在豪萨语中检测性别歧视的有效性。
### Conclusion
研究发现，文化细微差别在豪萨语中特别难以捉摸，尤其是对于需要澄清和惯用表达的情况，这导致了许多误报。尽管如此，研究为豪萨语性别歧视检测领域提供了基础数据和初步成果，这对于促进豪萨语相关的性别平等研究具有重要意义。
## 248. `cs.CL` - 侧重于LLM的RAVG方法，结合多粒度索引和置信约束 [PDF](https://arxiv.org/pdf/2510.27054), [HTML](https://arxiv.org/abs/2510.27054)
### Authors
Xiaofan Guo,Yaxuan Luan,Yue Kang,Xiangchen Song,Jinxu Guo
### Background
该论文关注在复杂知识环境中检索增强生成（RAG）所面临的问题，这些问题包括覆盖率不足、结果不稳定以及可靠性有限。现有的RAG方法在这种条件下表现不佳，难以建立检索与生成之间更为紧密的语义联系，同时难以保持信息的全面覆盖并有效抑制噪音和虚假内容.
### Innovation
该论文提出了一种新的置信控制方法，将多粒度记忆索引与不确定性估计相结合。该方法构建了一个分层的记忆结构，将知识表示划分为不同的粒度级别，并实现了从局部细节到全局语境的动态索引和检索，从而增强了检索与生成之间的语义联系。此外，引入了不确定性估计机制，以显式地约束和过滤生成过程中的低置信度路径，确保模型在全面覆盖信息的同时有效抑制噪音和虚假内容。整体优化目标包括生成损失、熵约束和方差正则化，形成了一个统一的置信控制框架。论文通过对超参数、环境条件和数据结构进行全面的敏感性测试和对比分析，验证了该方法在不同场景下的稳定性和鲁棒性.
### Conclusion
实验结果显示，该方法在问答精度、检索召回率、排名质量和事实一致性方面均优于现有模型，表明了将多粒度索引与置信控制相结合的有效性。该研究不仅为RAG提供了新的技术途径，还为复杂环境下大型模型的可靠性和可控性提供了实际证据.
## 249. `cs.CL` - 大型语言模型安全对齐和鲁棒优化的对比知识转移与鲁棒优化 [PDF](https://arxiv.org/pdf/2510.27077), [HTML](https://arxiv.org/abs/2510.27077)
### Authors
Jiasen Zheng,Huajun Zhang,Xu Yan,Ran Hao,Chong Peng
### Background
大型语言模型在安全对齐和鲁棒性方面存在局限性，本研究旨在通过结合对比蒸馏方法和噪声鲁棒训练来解决这些局限性。现有模型在大体量训练下难以保持安全和鲁棒性能，因此需要提出一种新的训练方法来改善这些模型在特定条件下的表现，如预测噪声和不确定性输入的稳定性。
### Innovation
提出了一种新的结合对比蒸馏与噪声鲁棒训练的方法。该方法固定骨干模型，并通过蒸馏将教师模型的知识边界转移到学生模型，从而提高语义一致性和对齐准确性。同时，引入了噪声扰动和鲁棒优化约束，确保模型在噪声和不确定输入下仍能保持稳定预测输出。整体框架包括蒸馏损失、鲁棒性损失和正则化项，形成了一个平衡对齐能力和抵御干扰的统一优化目标。
### Conclusion
该方法在知识转移、鲁棒性以及整体安全性方面明显优于现有基准，实现了多项关键指标的最优性能。本研究不仅丰富了参数高效微调的理论体系，还为构建更安全和值得信赖的对齐机制提供了新的解决方案。
## 250. `cs.CL` - Rating Roulette: 自然语言生成框架中LLM评判者的一致性问题 [PDF](https://arxiv.org/pdf/2510.27106), [HTML](https://arxiv.org/abs/2510.27106)
### Authors
Rajarshi Haldar,Julia Hockenmaier
### Background
随着自然语言生成（NLG）的广泛应用，对其评估变得越来越复杂。最近，使用大型语言模型（LLMs）进行评估变得流行，因为它们与人类偏好更接近，而非传统的n-gram或嵌入式度量标准。然而，在我们的实验中发现，LLM评判者在不同评估中的评分不一致，说明他们的评分存在较低的内在一致性和可靠性，这使得它们的判断结果变得不准确甚至几乎任意。这种不一致性影响了我们对其判断质量的衡量。研究通过不同NLG任务和基准，量化了这种不一致性的程度，并探讨了在适当使用LLM评判者情况下可能仍然对其有用性提供一定指导的可能性。
### Innovation
本研究通过实验证明了LLM评判者在不同评估中的一致性较差，其评分结果几乎变得任意，因而影响了评估质量的客观性。研究还进一步量化了不同NLG任务和基准中的这种不一致性程度，并探索了在改进使用LLM评判者的情况下可能仍然保持一定的有用性。
### Conclusion
本研究展示了在自然语言生成评估中自行不一致的问题，并为其针对适当使用LLM评判者提供了指导。尽管LLM评判者的一致性问题较为严重，但在遵循一定指导原则的情况下，它们仍能在一定程度上保持有用性。
## 251. `cs.CL` - 简单添加，显著收益：在URIEL+中扩展书写系统、语言和系族覆盖范围 [PDF](https://arxiv.org/pdf/2510.27183), [HTML](https://arxiv.org/abs/2510.27183)
### Authors
Mason Shipton,York Hay Ng,Aditya Khan,Phuong Hanh Hoang,Xiang Lu,A. Seza Doğruöz,En-Shiun Annie Lee
### Background
URIEL+语言知识库通过地理、语系和语类向量支持多种语言研究，但仍面临数据稀疏的问题，表现为缺乏特征类型、语言条目不完整以及基因学覆盖范围有限，这些问题限制了URIEL+在跨语言迁移中的实用性，尤其是对低资源语言的支持。
### Innovation
本文通过引入书写系统向量表示7,488种语言的书写系统属性，整合Glottolog增加18,710种额外语言，以及通过传播类型和书写系统特征扩大26,449种语言的系族填补，减少了书写系统向量14%的特征稀疏性，提升了多达19,015种语言（1007%）的语言覆盖范围，并改善了填充质量指标至至多33%。这些改进使得URIEL+在跨语言迁移任务（围绕低资源语言）中的表现有6%的提升。
### Conclusion
我们的研究增强了URIEL+在多语言研究中的完整性与包容性。
## 252. `cs.CL` - 在自然语言中识别信息的周期性 [PDF](https://arxiv.org/pdf/2510.27241), [HTML](https://arxiv.org/abs/2510.27241)
### Authors
Yulin Ou,Yu Wang,Yang Xu,Hendrik Buschmeier
### Background
最近在自然语言的信息密度理论方面取得了新的进展，这让研究者开始思考一个核心问题：自然语言在编码信息时是否表现出周期性的模式？本文通过引入一种新的方法—— surprisal 自动周期检测算法（AutoPeriod of Surprisal，APS）来探讨这一问题。
### Innovation
本文提出了一种创新的方法 APS，它能够识别单一文档-surprisal 序列中存在的任何显著周期。通过将这个算法应用于一系列语料库，研究者发现了一定比例的人类语言表现出强烈的信息周期模式，并且发现了新的周期，这些周期超出了文本中典型结构单元（如句子边界、基本话语单位等）的分布范围，进一步通过谐波回归模型得到了验证。
### Conclusion
研究结果表明，语言信息的周期性是由结构因素和其他远距离起作用的因素共同导致的结果。而且，本文介绍的周期性检测方法及其在LLM生成检测领域的潜在应用也进行了进一步讨论。
## 253. `cs.CL` - 百万词以上：LLMs的长期记忆基准测试与增强 [PDF](https://arxiv.org/pdf/2510.27246), [HTML](https://arxiv.org/abs/2510.27246)
### Authors
Mohammad Tavakoli,Alireza Salemi,Carrie Ye,Mohamed Abdalla,Hamed Zamani,J Ross Mitchell
### Background
现有的基准测试在评估大型语言模型（LLMs）在需要长期记忆和长上下文推理的任务上的能力时存在局限性，因为这些基准测试往往缺乏叙述连贯性，仅覆盖狭窄的领域，并仅测试简单的回忆任务。这导致在对话等场景中评估LLMs的能力变得困难。
### Innovation
本文提出了一个全面的解决方案，包括一个新颖的框架来自动生成长达100万词的连贯且主题多样的对话，并伴随一系列跨多种记忆能力的探针问题。基于此，构建了一个新的基准BEAM，包含100个对话和2000个验证问题。此外，提出了LIGHT框架，使LLMs配备长期事件记忆、短时工作记忆和积累重要事实的记事板，以增强模型性能。
### Conclusion
在BEAM上的实验表明，即便使用100万词上下文窗口的LLMs（带或不带检索增强），随对话变长而表现不佳。与基线模型相比，LIGHT框架能够跨多个模型有效提高表现，表现出3.5%-12.69%的平均改进。进一步的消融研究证实了每个记忆组件的贡献。
## 254. `cs.CL` - MemeArena: 自动化理解和评估多模态大型语言模型对有害内容理解的背景感知无偏评价 [PDF](https://arxiv.org/pdf/2510.27196), [HTML](https://arxiv.org/abs/2510.27196)
### Authors
Zixin Chen,Hongzhan Lin,Kaixin Li,Ziyang Luo,Yayue Deng,Jing Ma
### Background
社交媒体上短语传播的增加使得多模态大型语言模型（mLLMs）需要具备有效理解有害信息的能力。目前的评估方法主要集中在mLLMs对二分类任务的检测准确性，但对于不同上下文中的有害信息的解释细微差别反映不足。因此，本文提出MemeArena——一个基于代理的竞技场式评估框架，旨在提供一种考虑上下文和无偏见的方法，以评估mLLMs对多模态有害信息的理解能力。MemeArena通过模拟多样的解释上下文，并通过从不同视角出发构建评估任务来实现这一目标，从而促进公平、无偏见地比较mLLMs在解释多模态有害信息方面的表现能力。实验结果表明，MemeArena有效减少了评判代理的偏见，其评价结果与人类偏好高度一致，为多模态有害信息理解中mLLMs的可靠和全面评估提供了宝贵见解。
### Innovation
MemeArena是一个基于代理的竞技场式评估框架，旨在提供一种考虑上下文和无偏见的方法，以评估mLLMs对多模态有害信息的理解能力。该框架通过模拟多样的解释上下文，并通过从不同视角出发构建评估任务来实现这一目标。此外，MemeArena通过综合不同观点和专家评审的一致性，实现了公平和无偏见的比较。
### Conclusion
实验结果显示MemeArena有效减少了评判代理的偏见，其评价结果与人类偏好高度一致，为多模态有害信息理解中mLLMs的可靠和全面评估提供了宝贵的见解。MemeArena的代码和数据已公开可获取。
## 255. `cs.CL` - 为什么推理语言模型中会出现多语言推理差距？ [PDF](https://arxiv.org/pdf/2510.27269), [HTML](https://arxiv.org/abs/2510.27269)
### Authors
Deokhyung Kang,Seonjeong Hwang,Daehui Kim,Hyounghun Kim,Gary Geunbae Lee
### Background
推理语言模型（RLMs）在复杂推理任务中表现出色，但仍面临多语言推理差距问题，即在高资源语言上表现更好，而在低资源语言上表现较差。尽管最近的努力已经减少了这一差距，但其根本原因仍然不完全清楚。
### Innovation
本文展示了多语言推理差距主要源于语言理解失败——模型无法将多种语言输入的意义转换为其推理痕迹中的主导语言（即英语）。提出了Understanding Failures检测方法，发现可以识别这些失败，并提出了Selective Translation策略，仅在检测到理解失败时将多语言输入翻译成英语，实验表明Selective Translation能够弥合多语言推理差距，同时使用翻译的输入仅占大约20%。工作示理解失败是多语言推理差距的主要原因，可以通过检测和选择性缓解，从而深入了解其起源，提供实现更公平多语言推理的有希望路径。
### Conclusion
我们的工作证明了理解失败是多语言推理差距的主要原因，并能被检测和选择性地减轻，提供了有关其起源的关键见解和更公平多语言推理的潜在途径。代码和数据可在：this https URL. 上公开。
## 256. `cs.CL` - 语言即模态：通过编码器注入实现跨语言对齐 [PDF](https://arxiv.org/pdf/2510.27254), [HTML](https://arxiv.org/abs/2510.27254)
### Authors
Rajan Agarwal,Aarush Gupta
### Background
受过指令调优的大规模语言模型（LLMs）在低资源和非拉丁语系的场景中表现不佳，原因在于分词器碎片化以及跨语言耦合较弱。文章提出了一个名为LLINK（Latent Language Injection for Non-English Knowledge）的方法，该方法在不更改分词器和重新训练解码器的前提下，利用一个冻结的多语言编码器调整解码器的潜在嵌入空间，实现了对低资源和非拉丁语系的改进。
### Innovation
LLINK提出了一种计算高效的语言作为一种模态的方法。具体而言，它通过一个轻量级的对比投影，将冻结的多语言编码器的句子嵌入对准到解码器的潜在嵌入空间。接着，这个向量被扩展为K个软槽并进行小规模适配，使得冻结的解码器接收信号。LLINK在双语检索任务上显著提高了性能，并在LLM判断的问答评估中分别优于基础模型81.3%和直接调优63.6%。研究还发现，这些改进主要是由于减少了分词膨胀和增强了跨语言对齐，尽管该模型在数字准确性上仍存在一些弱点。
### Conclusion
将低资源语言视为一种模态提供了一条实现轻量级LLMs跨语言对齐的实用路径。
## 257. `cs.CL` - 大型语言模型判断背后的一致表示 [PDF](https://arxiv.org/pdf/2510.27328), [HTML](https://arxiv.org/abs/2510.27328)
### Authors
Yi-Long Lu,Jiajun Song,Wei Wang
### Background
生物和人工智能的核心问题之一是判断是否依赖于专门模块或通用资源。尽管大语言模型（LLMs）中可解码神经表示的发现暗示了一个模块化结构，但这些表示是否是真正独立的系统仍然是一个开放问题。本文通过对多种LLMs的研究，发现了一条主导维度，称为情感-赞同轴（VAA），它联合编码了主体的情感偏好和模型对事实陈述的认可度。该研究揭示了一种统一表示，表明VAA不仅作为控制信号引导生成过程以符合其评价状态，还可能牺牲事实准确性。这项机制引起了推理自上而下的从客观推理向目标导向辩护的转变，揭示了系统性偏见和幻觉的机制，并提供了忠实推理如何被具有连贯性判断的架构系统性削弱的解释。
### Innovation
本文提出了情感-赞同轴（VAA），这是一个主导的维度，联合编码了情感偏好和模型对事实陈述的认可度。通过直接干预展示了这种统一表示如何作为控制信号引导生成过程，并讨论了推理从客观推理向目标导向辩护的转变。这揭示了系统性偏见和幻觉的机制，并提供了忠实推理如何被具有连贯性判断的架构系统性削弱的解释。
### Conclusion
本文发现提供了一种机制，解释了系统性偏见和幻觉如何通过一个促进连贯判断的架构系统性削弱忠实推理。通过揭示VAA的控制信号作用，这项研究为理解大规模语言模型的判断机制提供了一个全新的视角。
## 258. `cs.CL` - ThoughtProbe：通过探测表示进行分类器引导的大语言模型思维空间探索 [PDF](https://arxiv.org/pdf/2510.27355), [HTML](https://arxiv.org/abs/2510.27355)
### Authors
Zijian Wang,Chang Xu
### Background
本文介绍了ThoughtProbe，这是一种新颖的推理时间框架，能够利用大型语言模型（LLMs）的隐藏推理特性来提升其推理性能。现有的研究主要通过操纵隐藏表示来引导LLM生成，但本文的方法是利用这些隐藏表示作为区分信号来指导基于树形结构的响应空间探索。这种方法在每个节点扩展阶段使用分类器作为评分和排名机制，优先分配计算资源给得分更高候选者的扩展。通过完成整个树形扩展，并收集所有分支的答案以形成候选答案池，本文提出了一种分支聚合方法，通过聚合所有支持分支的CoT评分来综合覆盖有效的推理链，从而从池中识别出最优答案。实验结果表明，这种框架不仅覆盖了有效的推理链，还有效地识别了它们，实现了在多个算术推理基准测试上的显著改进。
### Innovation
ThoughtProbe的核心创新在于其利用LGMs隐藏表示作为区分信号来指导树结构的响应空间探索的方法。与以往工作不同，这种方法不直接操纵隐藏表示来引导生成，而是让这些表示在节点扩展阶段作为评分机制来有效地分配计算资源，并后通过综合汇聚各分支的理由证明（CoT）分数来选择最优答案，这对于提升LLMs的推理性能具有重要意义。
### Conclusion
实验结果显示，ThoughtProbe在全面探索和识别有效推理链方面效果显著，达到了多个算术推理基准测试上的显著改进。
## 259. `cs.CL` - 从矿石地板到云端：电池全生命周期中先进NLP的系统审查 [PDF](https://arxiv.org/pdf/2510.27369), [HTML](https://arxiv.org/abs/2510.27369)
### Authors
Tosin Adewumi,Martin Karlsson,Marcus Liwicki,Mikael Sjödahl,Lama Alkhaled,Rihab Gargouri,Nudrat Habib,Franz Hennie
### Background
本文综述了自然语言处理（NLP）在整个电池生命周期的应用，而不仅仅是单一阶段或方法。作者遵循了系统评价和元分析的优选报告项目（PRISMA）方法，使用了包括Google Scholar、IEEE Xplore和Scopus在内的三个知名数据库或搜索引擎，对274篇科学论文进行了评估，并最终筛选出66篇相关论文进行关键审查。调研结果显示，在电池领域正出现新的NLP任务，有助于材料发现和其他生命周期阶段，但仍存在一些挑战，如缺乏标准化基准。作者还引进了一种新型的技术语言处理（TLP）框架，该框架结合了代理AI和优化提示，有助于应对这些挑战。
### Innovation
提出了一种新型的技术语言处理（TLP）框架，该框架结合了代理AI和优化提示，用于处理电池生命周期中的挑战。同时，作者还系统地综述了NLP在整个电池生命周期的应用，涵盖从矿石开采到云端的各种应用场景，填补了该领域的空白。
### Conclusion
研究表明，虽然NLP在电池领域的应用取得了显著进展，但仍面临许多挑战，尤其是缺乏标准化基准。所提出的TLP框架有望解决部分问题，进一步推动电池领域的发展。此外，作者公开提供了评审中的 artifacts，以便进行验证和可重复性研究。
## 260. `cs.CL` - 动态情感记忆管理在个性化大语言模型代理中的应用 [PDF](https://arxiv.org/pdf/2510.27418), [HTML](https://arxiv.org/abs/2510.27418)
### Authors
Junfeng Lu,Yueyan Li
### Background
大型语言模型的进步使得个性化的人工智能代理成为新的研究焦点。当前的主要代理系统依赖于个性化的外部记忆数据库来提供定制化的体验，但面临记忆冗余、记忆过时以及记忆与上下文整合不良的问题，这些问题主要归因于交互过程中缺乏有效的记忆更新机制。
### Innovation
该研究提出了一种新的记忆管理系统，专门用于情感情景。该方法采用受贝叶斯启发的记忆更新算法，并引入了记忆熵的概念，使代理能够自主地维护一个动态更新的记忆向量数据库，通过最小化全局熵来提供更个性化的服务。此外，研究还提出了DABench基准平台，专注于情感表达和对象的情感变化，以更好地评估系统的有效性。
### Conclusion
实验结果表明，该系统在个性化、逻辑连贯性和准确性方面表现出色。消融研究进一步验证了贝叶斯启发式更新机制在减轻记忆膨胀方面的有效性。这项工作为长期记忆系统的构建提供了新的见解。
## 261. `cs.CL` - Diffuse Thinking: Exploring Diffusion Language Models as Efficient Thought Proposers for Reasoning [PDF](https://arxiv.org/pdf/2510.27469), [HTML](https://arxiv.org/abs/2510.27469)
### Authors
Chenyang Shao,Sijian Ren,Fengli Xu,Yong Li
### Background
近年来，大型语言模型（LLMs）取得了显著的发展，特别是在推理能力方面通过测试时的扩展法则得到了持续提升。然而，LLMs的自回归生成范式导致了推理性能随测试时计算量的增加并不理想，通常需要大量的计算资源以提出多样化的想法，但这带来的性能提升却非常有限。
### Innovation
本文提出了一种高效的协作推理框架，利用扩散语言模型（DLMs）生成候选想法，并利用大型语言模型（LLMs）评估其质量。这种方法通过并行去噪单向前传播来高效产生多样化样本，从而缓解了自回归生成带来的计算负担，同时保持了高质量。
### Conclusion
该框架在多个基准测试中表现出色，特别是在复杂推理任务中表现出强大的性能，为未来的相关研究提供了一个有前途的方向。代码已开源。
## 262. `cs.CL` - VCORE: 基于方差控制的优化重新加权以优化链式思维监督 [PDF](https://arxiv.org/pdf/2510.27462), [HTML](https://arxiv.org/abs/2510.27462)
### Authors
Xuan Gong,Senmiao Wang,Hanbo Huang,Ruoyu Sun,Shiyu Liang
### Background
监督微调（SFT）在长链式思维（CoT）轨迹上已经作为增强大规模语言模型（LLMs）推理能力的关键技术。然而，常见的交叉熵损失将所有标记同等对待，忽视其在推理轨迹中的异质贡献，这种平等对待导致监督误分配和弱化泛化能力，尤其是在复杂的长形式推理任务中。论文旨在解决这一问题。
### Innovation
论文提出了基于方差控制的优化重新加权（VCORE），这是一种原则性的框架，将CoT监督重新表述为一个受限优化问题。通过基于优化理论视角，VCORE能够在标记之间实现原则性的自适应监督分配，从而更加紧密地将训练目标与稳健推理泛化的目标对齐。实证评估表明，VCORE 在各种背景下都优于现有标记重新加权方法，尤其是在数学和编码基准测试中的性能显著提升。此外，VCORE 还作为后续强化学习的有效初始化，为提高LLMs的推理能力提供了更好的基础。
### Conclusion
通过实验证明，VCORE 在各种基准测试中的性能都优于现有技术，尤其在数值和编程任务上取得了显著进步。该技术不仅改进了当前LLMs的推理能力，还为后续的强化学习提供了一个更坚实的基础。源代码将发布在这个链接：[此网址]，供进一步研究和应用。
## 263. `cs.CL` - 平衡知识更新：向着统一的模块化编辑在大型语言模型中 [PDF](https://arxiv.org/pdf/2510.27400), [HTML](https://arxiv.org/abs/2510.27400)
### Authors
Jiahao Liu,Zijian Wang,Kuo Zhao,Dong Hu
### Background
知识编辑作为一种高效的方法，用于更新大型语言模型（LLMs）中的事实性知识已逐渐浮现。现有的大多数方法主要集中在修改多层感知机（MLP）模块的权重上，而忽视了注意力（Attn）模块等其他组成部分。这导致了知识更新过程中存在残留的过时知识，限制了编辑的有效性。研究发现，在更先进的LLMs中，注意力模块在事实知识的存储和检索中扮演着重要角色，特别是在早期层中。
### Innovation
本文提出了IntAttn-Edit方法，该方法将联想记忆范式扩展到同时更新MLP和Attn模块。该方法采用一种知识平衡策略，在分配更新幅度时，根据各模块对知识存储的贡献程度进行分配。实验表明，IntAttn-Edit在标准基准测试上实现了更高的编辑成功率、更好的泛化能力和更强的知识保全能力。进一步的分析表明，平衡策略能够在多种设置下保持编辑性能在最优范围内。
### Conclusion
通过使用知识平衡策略，IntAttn-Edit在更新大型语言模型中的事实性知识时实现了更好的效果，并能够在多种不同情况下维持编辑的性能。
## 264. `cs.CL` - 低资源系统中域泛化技术的效果 [PDF](https://arxiv.org/pdf/2510.27512), [HTML](https://arxiv.org/abs/2510.27512)
### Authors
Mahi Aminu,Chisom Chibuike,Fatimo Adebanjo,Omokolade Awosanya,Samuel Oyeneye
### Background
机器学习模型通常假设训练数据和测试数据遵循相同的数据分布，但在实际应用中由于分布偏移，这一假设往往无法成立。这一问题在资源稀缺的情况下尤为明显，数据的稀缺性和有限的领域多样性会阻碍模型的鲁棒泛化能力。为此，领域泛化（Domain Generalization, DG）的方法应运而生，通过学习跨域不变特征来增强模型的鲁棒性，研究中具体通过因果机制来改进模型性能。
### Innovation
本研究探讨了两种独特的因果域泛化（DG）技术在低资源自然语言处理中的应用。一种是因果数据增强（CDA）方法，通过生成反事实样本来提高模型对伪相关因素的鲁棒性；另一种是基于因果表示学习方法（ICRL），使用DINER框架进行多语言情感分析的去偏见处理。此外，还对DINER框架进行多语言环境下的适应。
### Conclusion
两种方法均能增强模型对未知领域的鲁棒性：因果数据增强在情感分类任务中提供了跨域的准确率提升；使用DINER进行因果表示学习的方法在多语言情感分析中具有提高泛化性能的效果，但不同语言之间的增益效果有所不同。
## 265. `cs.CL` - SQLSpace：用于发现和减轻稳健性差距的文本到SQL的表示空间 [PDF](https://arxiv.org/pdf/2510.27532), [HTML](https://arxiv.org/abs/2510.27532)
### Authors
Neha Srikanth,Victor Bursztyn,Puneet Mathur,Ani Nenkova
### Background
介绍SQLSpace，这是一种人类可解释、可泛化的紧凑表示形式，基于最小的人工干预从文本到SQL示例中提取。展示这种表示形式在评估中的实用性，通过三种用例进行说明：(i) 仔细比较和对比流行文本到SQL基准中的组成，以识别基准中评估示例的独特维度，(ii) 通过超越总体准确度得分来了解模型性能的细粒度层面，(iii) 通过基于学习到的正确性估计进行有针对性的查询重写来提高模型性能。
### Innovation
SQLSpace提供了一种人类可解释、可泛化的紧凑表示形式，简化了文本到SQL问题的处理，并能精确比较不同基准的组成，揭示基于准确率的隐藏性能模式，支持查询成功的建模。
### Conclusion
SQLSpace使仅凭原始示例难以实现的分析成为可能：它揭示了基准之间的组合差异，暴露了准确性本身所掩盖的性能模式，并支持查询成功的建模，从而提高模型性能。
## 266. `cs.CL` - 复合词后的余波：探索复合词及其语义表示 [PDF](https://arxiv.org/pdf/2510.27477), [HTML](https://arxiv.org/abs/2510.27477)
### Authors
Swarang Joshi
### Background
本研究探讨了计算嵌入在处理英语复合词时与人类语义判断的契合度。研究对比了静态词向量（GloVe）和上下文嵌入（BERT）与来自心理语言学数据集的人类对词义主导性（LMD）和语义透明度（ST）的评级。通过关联强度（爱丁堡联想词典）、频率（BNC语料库）和预测性（LaDEC）的度量，计算了从嵌入数据派生的LMD和ST指标，并通过斯皮尔曼相关和回归分析评估了这些指标与人类判断的关系。研究表明，BERT嵌入比GloVe更好地捕获组构语义，并且预测性评分在人类和模型数据中都是语义透明度的强大预测因子。这些发现推进了计算心理语言学，明确了复合词处理的因素，并为基于嵌入的语义建模提供了见解。
### Innovation
本研究创新之处在于运用了BERT等上下文嵌入技术，对比了其与静态词向量（GloVe）在处理英语复合词时的语义建模效果。研究通过从心理语言学数据集中获取的人类对词义主导性和语义透明度的评级，运用多种评估指标（关联强度、频率、预测性）并采用斯皮尔曼相关和回归分析方法，探讨了嵌入式模型与人类判断的契合度。结果显示，BERT嵌入在捕捉复合词组构语义方面优于GloVe，且预测性评分是语义透明度的重要预测因素，无论在人类还是模型数据中均成立。
### Conclusion
这项研究表明，BERT嵌入比静态词向量（GloVe）更好地捕捉了复合词的组构语义，并且复合词的语义透明度可以通过其预测性评分来有效预测。该研究丰富了计算心理语言学领域的研究，明确了驱动复合词处理的因素，并为基于嵌入的语义建模提供了重要参考。
## 267. `cs.CL` - 基于患者为中心的AI临床总结框架：一种混合方法设计 [PDF](https://arxiv.org/pdf/2510.27535), [HTML](https://arxiv.org/abs/2510.27535)
### Authors
Maria Lizarazo Jimenez,Ana Gabriela Claros,Kieran Green,David Toro-Tobon,Felipe Larios,Sheena Asthana,Camila Wenczenovicz,Kerly Guevara Maldonado,Luis Vilatuna-Andrango,Cristina Proano-Velez,Satya Sai Sri Bandi,Shubhangi Bagewadi,Megan E. Branda,Misk Al Zahidy,Saturnino Luz,Mirella Lapata,Juan P. Brito,Oscar J. Ponce-Ponte
### Background
大型语言模型（LLMs）在生成来自患者-医生对话的临床摘要方面正逐渐达到人类水平的表现，但这些摘要往往侧重于患者的生物学而非偏好、价值观、意愿和关注点。为了实现以患者为中心的护理，作者提出了一个新的AI临床摘要标准：患者中心摘要（PCS），旨在开发一个框架来生成PCS，这些摘要应捕捉患者的价值观，并确保临床应用，同时评估当前开放源LLMs是否能在这一任务上达到人类水平的表现。
### Innovation
提出了新的标准——患者中心摘要（PCS），并在混合方法设计中评估了当前开放源LLMs是否能实现这一标准。研究采用混合方法，通过患者和公共参与小组访谈确定纳入临床摘要的个人和背景信息，八名临床医生根据这些发现创建了88例心房颤动咨询的金标准PCS。五个开源LLMs被用于生成摘要并进行评估，结果显示Mistral-8B和Llama-3.1-8B在零样本和少量样本提示下表现最佳。
### Conclusion
PCS框架已经建立并得到了初步验证，虽然开源LLMs在某些方面可以达到甚至超越人类表现，但在某些关键指标上仍然存在差距，尤其是在正确的和患者中心化的摘要生成方面。
## 268. `cs.CL` - DialectalArabicMMLU: 评估阿拉伯方言和多语言语言模型能力的标准 [PDF](https://arxiv.org/pdf/2510.27543), [HTML](https://arxiv.org/abs/2510.27543)
### Authors
Malik H. Altakrori,Nizar Habash,Abdelhakim Freihat,Younes Samih,Kirill Chirkunov,Muhammed AbuOdeh,Radu Florian,Teresa Lynn,Preslav Nakov,Alham Fikri Aji
### Background
尽管最近开发的阿拉伯语和多语言基准提高了现代标准阿拉伯语（MSA）的语言模型评估能力，但方言变体在日常交流中的普遍性导致其在这些基准中存在不足。因此，需要一个全面且细致的基准来评估语言模型在多种阿拉伯方言下的性能。
### Innovation
提出了DialectalArabicMMLU，这是一个新的基准，其中包含了手动翻译和适应了3000多个选择题-答案对，覆盖了五个主要方言（叙利亚、埃及、阿联酋、沙特阿拉伯和摩洛哥），总共包含15000个问答对，并支持32个学术和专业领域（加上英语和MSA时为22000个问答对）。这个基准不仅有助于系统地评估语言模型在MSA之外的推理和理解能力，还支持任务分析和语言分析。
### Conclusion
DialectalArabicMMLU提供了第一个统一的、由人类编纂的用于测量阿拉伯方言理解的标准资源，促进了更加包容的评估和未来模型的发展。这项基准展示了语言模型在不同阿拉伯方言上的性能差异，揭示了持续的变体现象，提升了对方言理解的研究和模型开发的关注。
## 269. `cs.CL` - BiSparse-AAS: Bilinear Sparse Attention and Adaptive Spans Framework for Scalable and Efficient Text Summarization [PDF](https://arxiv.org/pdf/2510.27516), [HTML](https://arxiv.org/abs/2510.27516)
### Authors
Desta Haileselassie Hagos,Legand L. Burge,Anietie Andy,Anis Yazidi,Vladimir Vlassov
### Background
尽管基于Transformer的架构在文本摘要任务中取得了显著进展，但它们的计算复杂度限制了在长文档上的可扩展性。目前的方法在面对长文档时效率低下，难以实现大规模应用和高性能。因此，如何提高文本摘要的效率和性能，特别是在处理长文档时，成为了一个重要的研究挑战。
### Innovation
本文提出了一种新颖的框架——BiSparse-AAS（Bilinear Sparse Attention with Adaptive Spans），它结合了稀疏注意力、自适应跨度和双线性注意力。稀疏注意力通过聚焦于输入中最相关的部分来减少计算成本；自适应跨度动态调整注意力范围；双线性注意力在这一优化过的上下文中建模复杂的令牌交互。与现有的最先进的基准相比，BiSparse-AAS 在提取性和抽象性的文本摘要任务中表现优异，分别在CNN/DailyMail和XSum数据集上获得了约68.1%和52.6%的ROUGE改进，并且在OpenWebText和Gigaword数据集上保持了较好的性能。通过解决效率、可扩展性和长序列建模的问题，BiSparse-AAS 提供了一个统一且实用的解决方案，适用于实际的文本摘要应用场景。
### Conclusion
BiSparse-AAS 提供了一个有效的方案来解决文本摘要任务中的效率和可扩展性问题，特别是在处理长文档时表现优异，为实际应用提供了可靠的解决方案。
## 270. `cs.CL` - 用于医疗任务的多语言BERT语言模型：基于领域特定适应性和跨语言能力的评估 [PDF](https://arxiv.org/pdf/2510.27552), [HTML](https://arxiv.org/abs/2510.27552)
### Authors
Yinghao Luo(1 and 2),Lang Zhou(1 and 2),Amrish Jhingoer(1 and 2),Klaske Vliegenthart Jongbloed(3 and 4),Carlijn Jordans(4),Ben Werkhoven(5),Tom Seinen(6),Erik van Mulligen(6),Casper Rokx(3 and 4),Yunlei Li(1) ((1) Department of Pathology &amp; Clinical Bioinformatics, Erasmus University Medical Center Rotterdam, (2) Department of Computer Science, Vrije Universiteit Amsterdam, (3) Department of Internal Medicine, Erasmus University Medical Center Rotterdam, (4) Department of Medical Microbiology and Infectious Diseases, Erasmus University Medical Center Rotterdam, (5) Department of Data and Analytics, Erasmus University Medical Center Rotterdam, (6) Department of Medical Informatics, Erasmus University Medical Center Rotterdam)
### Background
在多语言医疗应用程序中，特定领域的自然语言处理（NLP）工具可用性有限，特别是对于资源不足的语言。尽管多语言双向编码器表示来自变换器（BERT）提供了缓解语言差距的前景，医疗NLP任务在资源不足的语言中仍被低估。因此，这项研究探讨了在进一步预训练特定领域语料库如何影响医疗任务的模型性能，重点关注荷兰语、罗马尼亚语和西班牙语三种语言。进一步的预训练包括四大实验以构建医疗领域模型，并通过三种下游任务进行微调：在荷兰临床笔记中的自动化患者筛查，在罗马尼亚和西班牙临床笔记中的命名实体识别。结果显示，领域适应显著提升了任务性能。此外，领域分化（如临床与一般生物医学领域）导致了不同的性能表现。临床领域适应模型优于更一般的生物医学领域适应模型。此外，还观察到跨语言可转移性的证据。进一步研究还探讨了导致这些性能差异的可能原因，这些发现突出了医疗NLP领域适应和跨语言能力的可行性。在资源不足的语言环境下，这些发现可以为开发多语言医疗NLP系统提供有意义的指导，以缓解训练数据不足的问题，从而提高模型性能。
### Innovation
利用多语言BERT模型进一步预训练特定领域的语料库，进行了四项实验，构建了医疗领域的模型，并在不同任务中进行了微调。结果显示，领域适应显著提升了模型在医疗任务上的性能，并且发现在医疗和生物医学领域的差异性表现。此外，该研究还发现了跨语言转移能力的证据。通过这些实验，对多语言医疗NLP系统的开发提供了指导，以缓解数据不足的问题，并提高性能。
### Conclusion
领域适应和跨语言能力对于开发多语言医疗NLP系统至关重要。在资源不足的语言环境中的发现可以提供指导，通过领域特定的预训练和语言之间的转移能力，改善模型性能，从而解决训练数据不足的问题。
## 271. `cs.CL` - SpecAttn：推测稀疏注意 [PDF](https://arxiv.org/pdf/2510.27641), [HTML](https://arxiv.org/abs/2510.27641)
### Authors
Harsh Shah
### Background
大型语言模型（LLMs）在推理过程中受到自注意力机制的二次复杂度瓶颈影响，尤其是在上下文长度增加时。现有的方法无法有效缓解这一问题。
### Innovation
提出了一种名为SpecAttn的新型训练无需的方法，它能够无缝与现有的推测性解码技术集成，从而实现高效的稀疏注意力。SpecAttn的核心在于利用草稿模型在推测性解码过程中已计算的注意力权重来识别对目标模型重要的token，从而消除冗余计算，同时保持输出质量。该方法包括三种核心技术：基于KL散度的草稿和目标模型之间分层对齐、GPU优化的无排序的top-p token选择算法，以及由这些预测引导的动态键值缓存剪枝。
### Conclusion
SpecAttn通过利用标准推测性解码管道中已执行的计算工作，在不显著影响性能的情况下，实现了75%以上的键值缓存访问量减少，同时仅增加了15.29%的困惑度，显著优于现有的稀疏注意力方法。这表明，推测性执行可以被增强为提供近似验证而不显著降低性能。
## 272. `cs.CL` - MARAG-R1：通过强化学习多工具智能检索超越单一检索器 [PDF](https://arxiv.org/pdf/2510.27569), [HTML](https://arxiv.org/abs/2510.27569)
### Authors
Qi Luo,Xiaonan Li,Yuxin Wang,Tingshuo Fan,Yuan Li,Xinchi Chen,Xipeng Qiu
### Background
大型语言模型（LLMs）在推理和生成方面表现出色，但受到静态预训练数据的限制，导致事实准确性差和对新信息适应性弱。检索增强生成（RAG）通过将LLMs与外部知识相结合来解决这一问题，然而RAG的有效性很大程度上取决于模型能否充分获取相关信息。当前的RAG系统依赖单一固定top-k选择的检索器，这限制了对语料库的窄化和静态子集的访问，成为全面外部信息获取的主要瓶颈。特别是在需要语料库级推理的任务中更为明显。
### Innovation
我们提出了MARAG-R1，这是一种通过强化学习驱动的多工具RAG框架，允许模型动态协调多种检索机制以实现更广泛的和更精确的信息访问。MARAG-R1配备了四种检索工具：语义搜索、关键词搜索、筛选和聚合，并通过两阶段训练过程（监督微调随后是强化学习）来学习如何以及在何时使用这些工具。该设计使模型能够交错推理和检索，逐步收集足够的证据进行语料库级合成。实验表明，MARAG-R1在GlobalQA、HotpotQA和2WikiMultiHopQA等语料库级推理任务中显著优于强基线并达到了新的最先进水平。
### Conclusion
MARAG-R1在多工具智能检索框架中引入了强化学习，并通过监督微调和强化学习实现了卓越的性能。此框架显著改进了RAG的信息获取能力，在复杂的语料库级推理任务中取得了突破。
## 273. `cs.CL` - 连续自回归语言模型 [PDF](https://arxiv.org/pdf/2510.27688), [HTML](https://arxiv.org/abs/2510.27688)
### Authors
Chenze Shao,Darren Li,Fandong Meng,Jie Zhou
### Background
大型语言模型（LLMs）的效率受限于它们的串行、逐个标记生成过程。文章指出，克服这一瓶颈需要为LLM的扩展引入一个新的设计轴：增加每个生成步骤中的语义带宽。目前的模型以离散的标记预测为基础，这限制了生成步骤的数量。
### Innovation
作者提出了一种新的范式——连续自回归语言模型（CALM），它将连续向量预测作为新的预测方式，而不是传统的离散标记预测。CALM利用高保真度自编码器将K个标记压缩成一个连续向量，准确率超过99.9%。这种模型改变了语言被建模的方式，减少了生成步骤的数量。为此，作者还开发了一个全面的概率无损失框架，用于连续域中的鲁棒训练、评估和可控采样。实验结果表明，CALM在减少计算成本的同时显著提升了性能-计算权衡。
### Conclusion
这些发现确立了连续向量预测作为构建超高效语言模型的强大且可扩展的路径。
## 274. `cs.CL` - 文化制图学：绘制文化知识的版图 [PDF](https://arxiv.org/pdf/2510.27672), [HTML](https://arxiv.org/abs/2510.27672)
### Authors
Caleb Ziems,William Held,Jane Yu,Amir Goldberg,David Grusky,Diyi Yang
### Background
大型语言模型（LLMs）需要具备特定文化的知识才能更好地服务于全球用户。然而，在预训练阶段，这些模型可能无法获得此类知识。目前的主要解决方案是单一发起人的方式：研究人员定义挑战性的问题，用户被动回答（传统注解），或者用户主动生产数据，研究人员将其结构化为基准测试（知识提取）。这两种方法都需要进一步优化，通过混合发起人的方式，让用户指导过程以反映其文化，同时让模型引导问题设置以满足研究人员的目标。该研究提出了一种名为CultureCartography（文化制图学）的混合发起人方法，通过LLM提出其不确定答案的问题，促使人类填充知识空白并引导模型关注重要话题。
### Innovation
该研究提出了一种名为CultureCartography的混合发起人方法，并开发了一个名为CultureExplorer的工具。该工具让LLM提出其不确定答案的问题，以明确其知识缺口，使人类可以填补这些空白并直接引导模型关注重要话题。与基线方法相比，CultureExplorer可以更有效地产生现有模型如DeepSeek R1和GPT-4o所缺失的知识，即使使用网络搜索。基于此数据的微调提升了Llama-3.1-8B在相关文化基准测试中的准确性高达19.2%。
### Conclusion
文化制图学方法通过混合发起人的方式，提高了文化知识的采集和理解效率，特别是在提升模型的文化理解能力方面表现出色。该研究的CultureExplorer工具将有助于进一步增强LLMs的文化知识水平，提升其在跨文化交流中的有效性和生产力。
## 275. `cs.CL` - Broken-Token: Filtering Obfuscated Prompts by Counting Characters-Per-Token [PDF](https://arxiv.org/pdf/2510.26847), [HTML](https://arxiv.org/abs/2510.26847)
### Authors
Shaked Zychlinski,Yuval Kainan
### Background
大语言模型（LLMs）容易遭受监禁攻击，攻击者通过使用密码和字符级编码将恶意提示隐藏起来，绕过安全防护措施。这些防护措施往往无法解读编码内容，但底层模型仍然可以处理隐藏的有害指令。现有的防护方法在现代计算成本较高的情况下依赖于专有的大语言模型或其他模型。因此，需要一种既无额外成本又高效准确的防护技术来应对这一威胁。
### Innovation
我们提出了CPT-Filtering，这是一种新型的、适用于各种模型的方法，几乎不增加额外成本且准确性接近完美。该方法利用字节对编码（BPE）分词器的内在行为，通过计算文本中每个令牌的平均字符数（CPT），识别编码过的提示。这种方法基于这样一种原则：分词器在自然语言上训练时，会使用更多更短的令牌来表示分布外文本（如密码）。实验结果显示，简单的CPT阈值能准确地识别出编码文本，即使输入很短也能表现出高准确率。
### Conclusion
CPT-Filtering提供了一种实用的防护层，可以在实时文本过滤和离线数据整理中立即部署，有效地防御了此类攻击。
## 276. `cs.CL` - 评估跨模态检索中的视角偏差 [PDF](https://arxiv.org/pdf/2510.26861), [HTML](https://arxiv.org/abs/2510.26861)
### Authors
Teerapol Saengsukhiran,Peerawat Chomphooyod,Narabodee Rodjananant,Chompakorn Chaksangchaichot,Patawee Prakrankamanant,Witthawin Sripheanpol,Pak Lovichit,SarChaksaana Nutanong,Ekapol Chuangsuwanich
### Background
多模态检索系统期望能在语义空间中运作，不受查询语言或文化背景的影响。然而，实际检索结果往往是带有偏见的，表现为由语言盛行和文化关联性所塑造的偏差。研究中探讨了两种特定的偏见：第一，盛行偏差，指在图像到文本检索中偏好盛行语言的条目而非语义上忠实的内容；第二，关联偏差，在文本到图像检索中偏好与查询文化关联的图像而非语义上正确的图像。这些偏差表明，克服这些偏见需要超越简单数据扩展的专门策略，并指出文化关联性偏差可能是比语言盛行性偏差更难解决的问题。
### Innovation
提出了评估多模态检索中视角偏差的方法，并识别了两种关键偏见，即盛行偏差和关联偏差。研究显示，明确对齐是缓解盛行偏差的有效策略，但关联偏差依然是一个更具挑战性的难题。这让人们认识到，实现真正公平的多模态系统需要针对性的策略而不仅仅是简单的数据扩展，并提示文化关联性偏差可能比语言盛行性偏差更具挑战性。
### Conclusion
研究表明，克服多模态检索中的偏见需要针对性的策略，而不仅仅是简单数据扩展。明确对齐可以有效缓解盛行偏差，但文化关联性偏差则更为复杂且难以解决。因此，为了实现真正公平的多模态系统，需要开发和应用针对性的策略来应对文化关联性偏差。
## 277. `cs.CL` - CATArena：通过迭代锦标赛竞标赛评估大型语言模型代理 [PDF](https://arxiv.org/pdf/2510.26852), [HTML](https://arxiv.org/abs/2510.26852)
### Authors
Lingyue Fu,Xin Ding,Yaoming Zhu,Shao Zhang,Lin Qiu,Weiwen Liu,Weinan Zhang,Xuezhi Cao,Xunliang Cai,Jiaxin Ding,Yong Yu
### Background
大型语言模型（LLM）代理已经从基本的文本生成发展到能够通过与外部工具的交互独立完成复杂任务。然而，当前的评估基准主要是在固定场景中评估代理的端到端性能，这限制了评估范围，使得代理能力提升后存在评分饱和和对专家注释的依赖加剧的问题。本文强调学习能力，包括自我提高和互相学习，是代理达到人类水平智能的核心驱动力。为了应对当前基准评分饱和的问题，本文提出了一种迭代竞争性同伴学习框架，使代理能够通过重复交互和反馈来优化策略并系统地评估其学习能力。通过提供没有明确上限得分的任务，CATArena提供了一种持续的动态评价机制，以评估代理能力的快速提升。实验证明，CATArena能够为核心代理能力提供可靠、稳定和可扩展的基准测试，尤其是学习能力和策略编码能力。
### Innovation
提出了一种迭代竞争性同伴学习框架，并引入了CATArena，这是一个使用四款不同板卡游戏的锦标赛式评价平台，平台没有明确的得分上限，旨在为代理能力的动态提升提供持续评价，并解决当前基准评分饱和的问题，通过这种方式系统地评估代理的学习能力和策略编码能力。
### Conclusion
CATArena提供了一个可靠的、稳定的和可扩展的基准测试平台，特别是对于代理的学习能力和策略编码能力。
## 278. `cs.CL` - RepV: 安全分离的潜在空间用于可扩展的神经符号计划验证 [PDF](https://arxiv.org/pdf/2510.26935), [HTML](https://arxiv.org/abs/2510.26935)
### Authors
Yunhao Yang,Neel P. Bhatt,Pranay Samineni,Rohan Siva,Zhanyang Wang,Ufuk Topcu
### Background
随着AI系统进入安全性关键领域，验证其行动是否遵守预定义规则仍然是一个挑战。形式化方法可以提供可验证的保证，但需要手工制作时空逻辑规范，这限制了表达能力和易用性。深度学习方法能够评估计划是否符合自然语言约束，但其不透明的决策过程可能导致潜在严重的错误分类。
### Innovation
作者提出了RepV，这是一种神经符号验证器，通过学习一个潜在空间，将安全和不安全的计划线性可分。从一个基于现成模型检查器标注的基本种子集开始，RepV训练了一个轻量级的投影器，将每个计划和语言模型生成的解释嵌入到一个低维空间中；冻结的线性边界可以一次性前向传递来验证看不见的自然语言规则的合规性。RepV提供了基于在其潜在空间中的位置对验证正确性的概率保证。这种保证使规划器可以通过保证驱动的细化来改进规则合规性，不需要人类注释。实验证明，与基线方法相比，RepV在合规性预测准确性上提高了15%，同时增加的参数不到200万。此外，作者的细化框架在各种规划领域中优于普通的微调基线。
### Conclusion
这些结果表明，安全性可分的潜在空间提供了可扩展的、即插即用的神经符号计划验证的基本方法。代码和数据可在该网址获取: this https URL
## 279. `cs.CL` - The Denario项目：深度知识AI代理进行科学发现 [PDF](https://arxiv.org/pdf/2510.26887), [HTML](https://arxiv.org/abs/2510.26887)
### Authors
Francisco Villaescusa-Navarro,Boris Bolliet,Pablo Villanueva-Domingo,Adrian E. Bayer,Aidan Acquah,Chetana Amancharla,Almog Barzilay-Siegal,Pablo Bermejo,Camille Bilodeau,Pablo Cárdenas Ramírez,Miles Cranmer,Urbano L. França,ChangHoon Hahn,Yan-Fei Jiang,Raul Jimenez,Jun-Young Lee,Antonio Lerario,Osman Mamun,Thomas Meier,Anupam A. Ojha,Pavlos Protopapas,Shimanto Roy,David N. Spergel,Pedro Tarancón-Álvarez,Ujjwal Tiwari,Matteo Viel,Digvijay Wadekar,Chi Wang,Bonny Y. Wang,Licong Xu,Yossi Yovel,Shuwen Yue,Wen-Han Zhou,Qiyao Zhu,Jiajun Zou,Íñigo Zubeldia
### Background
本文介绍了Denario，一种多功能的人工智能多代理系统，旨在作为科学研究助手。它能够执行多种任务，包括生成想法、文献核查、制定研究计划、编写和执行代码、制作图表以及撰写和审查科学论文。该系统具有模块化的架构，可处理特定任务，例如生成想法或使用Cmbagent作为深度研究后端完成端到端的科学研究分析。文章详细描述了Denario及其模块，并通过在多个科学领域（如天文学、生物学、生物物理学、生物医学信息学、化学、材料科学、数学物理、医学、神经科学和行星科学）展示多个AI生成的论文，展示了其能力。此外，文章还展示了跨学科结合想法生成的论文，其中包括将量子物理和机器学习方法应用于天文学数据。
### Innovation
Denario创新之处在于其多代理系统的设计，能够进行多种复杂的科学研究任务。系统采用了模块化架构，允许专门处理特定任务，同时使用Cmbagent作为深度研究后端，实现端到端的科学研究分析。此外，Denario还展现了跨学科结合想法生成论文的能力，这在科学研究中具有重要意义。最后，系统还得到了领域专家的评估，提供了数值评分和评论性的反馈，这对于未来系统的改进具有指导意义。
### Conclusion
本研究通过Denario展示了一种新的科学研究方法，并对其工作进行了详细的描述。系统在多个科学领域展示了强大的能力，但也存在一定的局限性。最后，文章讨论了AI在科学发现中的伦理问题，并反思了这种技术与科学哲学的关系。系统和应用程序的代码公开发布，供公众下载和使用。
## 280. `cs.CL` - Glia：受人类启发的自动化系统设计与优化的人工智能 [PDF](https://arxiv.org/pdf/2510.27176), [HTML](https://arxiv.org/abs/2510.27176)
### Authors
Pouya Hamadanian,Pantea Karimi,Arash Nasr-Esfahany,Kimia Noorbakhsh,Joseph Chandler,Ali ParandehGheibi,Mohammad Alizadeh,Hari Balakrishnan
### Background
论文背景在于探讨是否能够通过人工智能自主设计出与人类专家同等创造性和推理能力的机制，特别是在计算机系统设计中。文章聚焦于如何利用大型语言模型（LLMs）构建一个类人类多代理的工作流程来解决这一问题。传统的方法是通过优化黑盒策略，而Glia创新之处在于用易解释的设计取代这些策略，并公开其推理过程。当Glia应用于分布式GPU集群的LLM推理时，展示了在显著缩短时间的情况下设计出可与人类专家水平媲美的请求路由、调度和自动扩展的新算法，并揭示了工作负载行为的新见解。整体来看，Glia的目的在于通过结合推理LLMs与结构化实验，生成复杂系统问题的创造性且易于理解的设计。
### Innovation
Glia的创新之处在于，它利用大型语言模型（LLMs）进行网络系统设计，并采用了受人类启发的多代理工作流程；每个代理专门负责推理、实验和分析，通过评价框架将抽象推理与实际反馈相结合。不同于以往优化黑盒策略的方法，Glia生成的是可解释的设计，并公开其推理过程。因此，Glia能够产生与人类专家相媲美的设计，并且能在较短的时间内做出决策，为复杂系统问题提供新的解决方案。
### Conclusion
通过将推理LLMs与结构化实验相结合，Glia能够在显著减少时间的情况下设计出具有创造性且易于理解的系统解决方案，这不仅提高了效率，也为研究复杂系统提供了新的见解。Glia的成功表明，结合特定领域的知识和人工智能技术，可以有效解决复杂的系统设计问题。
## 281. `cs.CL` - 基于语义帧聚合的变压器在实时视频评论生成中的应用 [PDF](https://arxiv.org/pdf/2510.26978), [HTML](https://arxiv.org/abs/2510.26978)
### Authors
Anam Fatima,Yi Yu,Janak Kapuriya,Julien Lalanne,Jainendra Shukla
### Background
实时视频流在Twitch等平台上的人气不断上升，通过动态互动增强了观众的参与度。然而，自动生成与当前观众互动相关的评论仍然是一个具有挑战性但也充满吸引力的任务。视频流包含大量数据和多余内容，现有方法往往忽视了优先处理与当前观众互动最相关的视频帧这一重要方面。这一优先处理对于生成与上下文相符的评论至关重要。为解决这一问题，本文提出了一种新颖的基于语义帧聚合的变压器（SFAT）模型用于实时视频评论生成。该方法不仅利用CLIP的视觉-文本多模态知识生成评论，还根据视频帧与其正在进行的观众对话的相关性为其分配权重。通过一种高效的加权帧总和技术，该方法强调信息性的帧，同时对不相关的帧关注较少。最后，带有跨注意力机制的评论解码器确保生成的评论从聊天和视频中反映出了上下文线索。此外，为克服现有数据集的局限性，这些数据集主要集中在中文内容且视频类别有限，我们构建了一个大规模、多模态的英语视频评论数据集，该数据集来源于Twitch，覆盖了11个视频类别，总时长438小时，包含320万条评论。
### Innovation
本文提出了基于语义帧聚合的变压器（SFAT）模型，用于实时视频评论生成。该模型不仅利用了CLIP的视觉-文本多模态知识生成评论，还根据视频帧的语义相关性为它们分配权重，强调了信息性的帧，同时忽略不相关的帧。此外，研究者还构建了一个大规模、多模态的英语视频评论数据集，该数据集主要来源于Twitch，覆盖了大量视频类别，提供了一个更为全面的数据集供进一步研究使用。
### Conclusion
本文通过比较现有方法，展示了基于语义帧聚合的变压器（SFAT）模型在实时视频评论生成方面的有效性。
## 282. `cs.CL` - 朝衡量算法相似性之方向 [PDF](https://arxiv.org/pdf/2510.27063), [HTML](https://arxiv.org/abs/2510.27063)
### Authors
Shairoz Sohail,Taher Ali
### Background
在面对同一问题的两个算法时，我们能否确定它们是否具有实质性差异？虽然在全般性的情况下这个问题无法通过计算得出答案，且由于相似性概念的竞争性使得问题在实际操作中变得更加模糊。但在多个应用场景（例如克隆检测或程序合成）下，有一个实用且一致的相似性度量标准是必要的。
### Innovation
我们回顾了现有的等价性和相似性概念，并引入了EMOC框架（Evaluation-Memory-Operations-Complexity），该框架将算法实现嵌入到适合下游任务的功能空间中。我们还编制了一个名为PACD的经过验证的Python实现集合，该集合涵盖了三个问题。利用EMOC特征，我们展示了如何进行算法类型的聚类和分类、进行近乎重复算法的检测、以及量化由大模型生成程序的多样性。此外，我们发布了计算EMOC嵌入的代码、数据和工具，以促进重现性和未来关于算法相似性的工作。
### Conclusion
EMOC框架能够支持算法类型的聚类和分类、近乎重复算法的检测，以及量化由大模型生成程序的多样性。我们还提供了EMOC嵌入的计算代码、数据和工具，以促进未来的研究。
## 283. `cs.CL` - MLLMs能否读懂社交场合？多模态多党诚信验证基准测试 [PDF](https://arxiv.org/pdf/2510.27195), [HTML](https://arxiv.org/abs/2510.27195)
### Authors
Caixin Kang,Yifei Huang,Liangyang Ouyang,Mingfang Zhang,Yoichi Sato
### Background
随着人工智能系统越来越多地融入人类生活，赋予它们强大的社交智能已成为一个关键的研究领域。一个重要的方面是区分事实与欺骗，这种在人类互动中普遍存在的元素通过言语和非言语视觉线索的复杂交互来传达。然而，在动态多党对话中自动检测欺骗仍然是一个重大挑战。近年来，强大的多模态大型语言模型（MLLMs）因其在视觉和文本理解方面的出色能力，成为进行这项任务的自然选择。然而，这些模型在这项关键领域的功能尚未得到充分量化。
### Innovation
本研究引入了新的任务——多模态交互真实性评估（MIVA），并基于狼人杀游戏创建了一个新的多模态数据集。该数据集提供了同步的视频和文本记录，以及每个陈述的真实标签。研究还建立了使用最先进的MLLMs的基准测试，揭示了即使是强大的模型如GPT-4o也不能可靠地区分事实与虚构。分析表明，这些模型难以将语言与视觉社会线索有效关联，且可能过于保守地进行对齐，这突显了急需新的方法来构建更敏感和可信的AI系统。
### Conclusion
研究发现，当前最先进的MLLMs在多党社会互动中介验事实与虚假的能力存在显著差距，这些模型难以有效将语言与视觉社会线索关联，且过度保守地对齐，亟需创新方法来提高AI系统的感知能力和可信度。
## 284. `cs.CL` - DRAMA: 将数据检索与分析统一起来以满足开放领域分析查询 [PDF](https://arxiv.org/pdf/2510.27238), [HTML](https://arxiv.org/abs/2510.27238)
### Authors
Chuxuan Hu,Maxwell Yang,James Weiland,Yeji Lim,Suhas Palawala,Daniel Kang
### Background
手动进行现实世界的数据分析工作量大且效率低。尽管尝试自动实现数据科学工作流程，但现有框架或系统均未能有效支持开放领域的数据收集、结构化数据转换和分析推理这三项关键能力。为此，研究提出了DRAMA，一种端到端的框架，能够在大规模开放领域数据上通过自然语言响应用户的分析查询。DRAMA统一了数据收集、转换和分析作为一个单一的流水线过程。为了评估DRAMA在典型任务上的性能，作者构建了一个基准DRAMA-Bench，包含声明验证和问答两类任务，每类各100个例子，这些任务来源于需要从开放领域获取和分析数据的热门现实应用。在此基础上，作者开发了遵循DRAMA框架的DRAMA-Bot多代理系统，包括数据检索器和数据分析器，分别负责收集、转化数据和结构化推理数据。DRAMA-Bot在DRAMA-Bench和五个最先进的基准代理上进行评估，准确率为86.5%，成本为0.05，超出所有基准代理多达6.9倍的准确率，且成本不到其六分之一。
### Innovation
DRAMA旨在一体化解决数据收集、结构化数据转换和分析推理，通过多代理系统（DRAMA-Bot）实现高效的自然语言数据分析查询处理。该系统在典型任务上的性能评估证明了其在准确性和成本效益上的显著优势。
### Conclusion
通过提出DRAMA和DRAMA-Bot，研究者展示了一个有效支持开放领域数据科学工作流程的新框架，能够在大规模数据环境中执行高效的自然语言分析查询。这一创新显著提高了数据处理的效率和准确性，同时显著降低了成本。
## 285. `cs.CL` - 高级线性注意力 [PDF](https://arxiv.org/pdf/2510.27258), [HTML](https://arxiv.org/abs/2510.27258)
### Authors
Yifan Zhang,Zhen Qin,Quanquan Gu
### Background
缩放自回归语言模型到长上下文的主要障碍在于标量点积注意力的成本是二次的。通过线性时间注意力和状态空间模型（SSMs）提供了可扩展的替代方案，但通常受到一阶或核基近似限制，这可能限制了表达能力。
### Innovation
本文引入了高级线性注意力（HLA），它是一种因果、流式机制，通过紧凑的前缀充分统计数据实现高级互动。在二阶情况下，HLA 维持常量大小的状态并在线性时间内计算每个标记的输出，而无需创建任何 n×n 矩阵。此外，还提出了用于高级和更高阶扩展的逐步流式身份、严格因果掩码变体以及基于关联扫描的批次并行训练方案，可精确重现级联递归的激活。
### Conclusion
总体而言，这些结果将 HLA 作为符合原理、可扩展的构建块定位，该构建块结合了注意力同数据依赖混合和现代递归架构的效率。
## 286. `cs.CL` - 通过忠实度和冗余度衡量链式思维监控能力 [PDF](https://arxiv.org/pdf/2510.27378), [HTML](https://arxiv.org/abs/2510.27378)
### Authors
Austin Meek,Eitan Sprejer,Iván Arcuschin,Austin J. Brockmeier,Steven Basart
### Background
链式思维（CoT）输出使得我们可以阅读模型的逐步推理过程。任何复杂的推理过程都必须通过这个文本痕迹体现，因此CoT的质量直接反映了模型的思维过程。然而，仅仅拥有透明的CoT并不足以让监控变得有效，还需要确保CoT的真实性和完整性。当前的方法主要是通过模型在输入添加提示后改变答案来评估CoT的忠实度，但这种方法对模型保持原答案的情况信息有限，也无法全面检验与提示无关的推理过程。为了更全面地评估监控能力，论文提出了一种新的评估方法：通过CoT列出所有解决任务所需因素的冗余度来衡量模型的整体监控能力。
### Innovation
提出了一个新的衡量链式思维监控能力的方法，结合了CoT的忠实度和冗余度。通过衡量CoT是否清晰完整地列出解决任务所需的所有因素，从而评估CoT作为模型外部‘工作记忆’的效果。这种方法提供了一个新的得分系统，可以有效地评估模型在任务解决过程中的可监控性。
### Conclusion
评估结果显示，即便是看似忠实的模型也可能因为忽略了关键因素而难以被监控。模型的各家族之间在监控能力上也表现出显著差异。研究结果为未来的可重现研究提供了支持，并通过Inspect库发布了评估代码。
## 287. `cs.CL` - Atlas-Alignment: 实现语言模型间解释性的可转移性 [PDF](https://arxiv.org/pdf/2510.27413), [HTML](https://arxiv.org/abs/2510.27413)
### Authors
Bruno Puri,Jim Berend,Sebastian Lapuschkin,Wojciech Samek
### Background
解释性对于构建安全、可靠和可控的语言模型至关重要，但现有的解释性流程仍然成本高昂且难以扩展。通常需要为新模型训练特定的稀疏自编码器、手动或半自动标记其组件以及后续验证，这过程昂贵且复杂。
### Innovation
本文介绍了一种名为Atlas-Alignment的框架，通过将未知的潜在空间与一个标记的人类可解释的潜在空间（概念图）对齐，利用共享输入和轻量级的表示对齐技术，实现解释性的转移。这种方法能够使以前不透明的模型具备两个关键功能：（1）语义特征搜索和检索，（2）基于人类可解释的概念图概念进行可控生成。研究显示简单的表示对齐方法可以在无需标记概念数据的情况下实现稳健的语义检索和可控生成。
### Conclusion
Atlas-Alignment框架通过投资于高质量的概念图（Concept Atlas），能够在大量的新模型中实现透明性和可控性，且边际成本极低。这降低了可解释AI和机理解释的成本。
## 288. `cs.CL` - 不可归因性：从检索与语义相似性计算新颖性 [PDF](https://arxiv.org/pdf/2510.27313), [HTML](https://arxiv.org/abs/2510.27313)
### Authors
Philipp Davydov,Ameya Prabhu,Matthias Bethge,Elisa Nguyen,Seong Joon Oh
### Background
理解语言模型输出与预训练语料库之间的关系是研究模型行为的核心。现有的大多数训练数据归因（TDA）方法关注的是哪些训练示例因果影响给定的输出。这项工作则将问题反转：哪些输出不能被归因到任何预训练的实例中？
### Innovation
本文引入了‘不可归因性’作为语义新颖性的操作性度量标准。此外，提出了一种简单的两步检索管道：使用轻量的GIST嵌入索引语料库，检索最相似的候选项，然后用ColBERTv2重新排名。通过对比语料库中最接近的项与人工生成的文本参考，来评估语言模型输出的新颖性。这项研究揭示了模型从预训练数据中汲取信息的范围远超之前报告的长度，并展示了不同领域如何系统地促进或抑制新颖性，同时发现指令微调不仅改变风格，也增加了新颖性。这种方法通过重新定义新颖性评估，使其更加高效地进行大规模分析，并公开了索引的语料库碎片以支持进一步的研究和复制实验。
### Conclusion
不可归因性的新方法和大规模语料库碎片的公开，使大规模语料库上的新颖性评估更加高效和可重复，还提供了关于预训练语言模型行为的新见解。
## 289. `cs.CL` - DeepCompress:一种动态探索和压缩推理链的双重奖励策略 [PDF](https://arxiv.org/pdf/2510.27419), [HTML](https://arxiv.org/abs/2510.27419)
### Authors
Tian Liang,Wenxiang Jiao,Zhiwei He,Jiahao Xu,Haitao Mi,Dong Yu
### Background
大型推理模型（LRMs）虽然表现出色，但在处理简单问题时容易走多条复杂路径（即过度思考），在处理复杂问题时则可能走简单路径（即思考不足），导致认知效率低下。现有通过监督微调（SFT）或利用token长度奖励的强化学习（RL）方法可以在一定程度上提升效率，但通常以牺牲准确率为代价。前人在面对这一问题时倾向于持续选择较短的推理路径，但该论文指出较长的响应可以包含更广泛正确解法的可能性。
### Innovation
提出了一种新颖的框架DeepCompress，旨在同时提升LRMs的准确性和效率。DeepCompress采用了一个自适应长度奖励机制，可以实时将问题分类为“简单”或“困难”，并据此调整推理路径的长短。对于简单的推理任务，鼓励更高效的简短推理；对于困难的任务，则促进更探索性的长推理链。这种方法使得模型可以根据演进能力自主调整其思维链（CoT）长度，从而优化不同类型问题的推理过程。实验结果表明，DeepCompress在解决难题的基准测试上表现优于基线方法，同时显著提高了token效率，达到了更高的准确率。
### Conclusion
实验结果显示，DeepCompress在具有挑战性的数学基准测试中表现优于基线方法，同时显著提高了token效率，实现了更高准确率。
## 290. `cs.CL` - 思想分枝：解释大模型推理需要重复采样 [PDF](https://arxiv.org/pdf/2510.27484), [HTML](https://arxiv.org/abs/2510.27484)
### Authors
Uzay Macar,Paul C. Bogdan,Senthooran Rajamanoharan,Neel Nanda
### Background
大多数研究推理模型的工作仅研究单一思维链（CoT），而模型实际上定义了许多可能思维链的分布。研究单一实例不足以理解因果影响和潜在的计算过程。尽管完全指定这种分布是不可行的，但通过采样可以对其有理解。本文探讨了通过重采样方法如何有效地研究模型决策。研究了具体句子的部分下游影响，评估人工编辑思维链的有效性和提出了一种鲁棒度度量，重采样以防止相似内容的重新出现。
### Innovation
通过重采样方法来研究模型决策思路，提出了对单一实例研究的替代方法。这包括特定句子的潜在因果影响，人工编辑机制的有效性，以及模型步骤更改对推理过程的影响。提出了鲁棒度度量，确保在重采样过程中防止相似内容重复出现。此外，还开发了一种方法，通过调整因果中介分析来了解未显式提及但在输出中具有因果影响的提示如何在思维链中产生微妙而累积的影响。
### Conclusion
通过重复采样研究分布，可以实现可靠的因果分析，提供模型推理的清晰叙述，并提出原则性强的推理链干预措施。该研究通过多角度分析揭示了新型的干预方法及其对模型推理的影响，为未来的推理模型研究提供了新的视角。
## 291. `cs.CL` - SIGMA：增强搜索的按需知识整合以实现自主数学推理 [PDF](https://arxiv.org/pdf/2510.27568), [HTML](https://arxiv.org/abs/2510.27568)
### Authors
Ali Asgarov,Umid Suleymanov,Aadyant Khatri
### Background
数学推理问题的解决不仅需要准确获取相关知识，还需要进行仔细、多步骤的思考。然而，当前的检索增强模型往往依赖单一视角，遵循僵化的搜索策略，并且难以有效地结合多个来源的信息。
### Innovation
作者提出了SIGMA框架，它协调专门的代理独立推理、进行有针对性的搜索并通过调解机制综合发现。每个代理生成假设段落以优化其分析视角的检索，确保知识整合既具上下文敏感性又具有计算效率。在MATH500、AIME和博士级别科学问答GPQA等具有挑战性的基准测试中，SIGMA超越了开源和封闭源系统，绝对性能提升7.4%。研究表明，多代理、按需知识整合大大提高了推理准确性和效率，为复杂、知识密集型问题解决提供了一种可扩展的方法。
### Conclusion
研究表明，多代理、按需知识整合在复杂、知识密集型问题解决中具有显著优势，增强了解决数学推理问题的能力，提高了准确性和效率。
## 292. `cs.CL` - 通用视频检索：通过合成多模态金字塔课程实现视频嵌入的泛化 [PDF](https://arxiv.org/pdf/2510.27571), [HTML](https://arxiv.org/abs/2510.27571)
### Authors
Zhuoning Guo,Mingxin Li,Yanzhao Zhang,Dingkun Long,Pengjun Xie,Xiaowen Chu
### Background
当前的视频检索范式存在结构性不匹配，狭窄的基准测试激励了相应有限的数据和单一任务训练，导致普遍能力受到抑制。缺乏定义和要求多维度泛化的诊断评估。因此，需要一种新的框架来打破这种循环，这种框架应综合考虑评估、数据和建模的设计。
### Innovation
提出了一种基于评估、数据和建模协同设计的框架。首先，建立了用于同时测量性能和诊断能力缺口的universal视频检索基准（UVRB），包括16个数据集。其次，通过UVRB的诊断指导，生成了155万个高质量配对来填充通用所需的语义空间。最后，设计了一个模态金字塔课程，通过显式利用数据中隐含的联系来训练通用视频嵌入（GVE）。实验表明，GVE在UVRB上实现了最先进的零样本泛化。研究表明，流行的基准测试是泛化能力的不良预测者，部分相关的检索是主导但未被忽视的场景。
### Conclusion
我们的协同设计框架提供了一条实用路径，使视频检索超越有限范围，并朝着真正通用的方向前进。
## 293. `cs.CL` - LIBMoE：大型语言模型中混合专家库的全面基准库 [PDF](https://arxiv.org/pdf/2411.00918), [HTML](https://arxiv.org/abs/2411.00918)
### Authors
Nam V. Nguyen,Thong T. Doan,Luong Tran,Van Nguyen,Quang Pham
### Background
Mixture of experts (MoE) 架构已成为扩展的关键组成部分，在大多数大型语言模型如GPT-OSS、DeepSeek-V3、Llama-4和Gemini-2.5中起到核心作用。然而，MoE的研究受到高昂的训练和评估计算成本限制，导致大多数研究人员无法进行大规模研究。
### Innovation
LibMoE引入了一个统一的框架，用于可重复、高效和扩展的MoE研究，支持预训练和稀疏增益两个阶段。该框架提供了透明的分析工具，用于探究路由动态，并通过降低进入门槛和标准化评估，以及全面分析，扩大了MoE研究的可访问性，并建立了未来的创新指导基准。
### Conclusion
通过LibMoE，研究者可以开展全面分析，从路由动态、轻量级初始化对负载均衡的影响，到训练制度差异，揭示不同的路由模式和稳定性特征。这有助于扩大MoE研究的可及性，建立可靠的基准指导未来的创新。
## 294. `cs.CL` - 通过对比触发学习在基于MLLM的实体决策中对视觉后门攻击的研究 [PDF](https://arxiv.org/pdf/2510.27623), [HTML](https://arxiv.org/abs/2510.27623)
### Authors
Qiusi Zhan,Hyeonjeong Ha,Rui Yang,Sirui Xu,Hanyang Chen,Liang-Yan Gui,Yu-Xiong Wang,Huan Zhang,Heng Ji,Daniel Kang
### Background
多模态大语言模型（MLLMs）通过让实体代理能够直接从视觉输入中进行感知、推理和规划任务导向的行为，已经显著提升了实体代理的能力。然而，这种以视觉驱动的实体代理也开辟了一个新的攻击面：视觉后门攻击。在这种攻击中，代理在标准行为下运行，直到场景中出现可视触发信号时，便会持续执行攻击者指定的多步骤策略。目前缺乏有效的框架来在MLLM驱动的实体代理中植入这种视觉后门。因此，BEAT框架应运而生，旨在利用环境中存在的对象作为触发信号植入视觉后门。然而，与文本触发相比，对象触发在视角和照明变化中表现出高度的变异性，这使得可靠地植入这些后门变得困难。BEAT通过构建包含多样场景、任务和触发位置的数据集，以及采用包含监督微调（SFT）和新颖对比触发学习（CTL）的两阶段训练方案，解决了这一挑战。CT学习将触发器的区分问题表述为带有和无触发器输入之间的偏好学习，从而明确边界以确保精准后门激活。
### Innovation
BEAT框架是首个利用环境中物体作为触发信号向基于MLLM的实体代理植入视觉后门的框架。框架通过（1）构建覆盖多样场景、任务及触发位置的数据集，增加触发信号变异性暴露；（2）采用两阶段训练方案，先进行监督微调（SFT），再引入新颖对比触发学习（CTL）。CT学习通过偏好学习，使判定边界更加明确，确保后门的精确激活。此外，与简单的监督微调相比，对比触发学习（CTL）在有限后门数据下提高了后门激活的准确性，最高可达39%。这些创新使得基于MLLM的实体代理面临的关键未被探索的安全风险得以揭露，强调了在实际部署前需要更为稳健的防御措施。
### Conclusion
在各种实体代理基准测试和MLLM模型中，BEAT实现了高达80%的攻击成功率，同时保持了强大的正常任务性能，并可靠地在未见过的触发位置进行泛化。这表明，基于MLLM的实体代理面临着严重的安全风险，需要采取相应的防御措施，以确保在实际部署前的安全性。
## 295. `cs.CL` - MindSearch: 模拟人类思维引发深层AI搜索器 [PDF](https://arxiv.org/pdf/2407.20183), [HTML](https://arxiv.org/abs/2407.20183)
### Authors
Zehui Chen,Kuikun Liu,Qiuchen Wang,Jiangning Liu,Wenwei Zhang,Kai Chen,Feng Zhao
### Background
信息检索和整合是一个复杂的认知任务，消耗大量的时间和精力。尽管大型语言模型（LLMs）取得了显著进展，通过将LLMs与搜索引擎相结合的方法仍未能取得令人满意的表现，主要由于以下三个挑战：首先，复杂的请求往往一次无法被搜索引擎准确和完整地检索；其次，需要整合的信息分布在多个网页中，且带有很多噪声；最后，大量含有长文本的网页可能超出LLMs的最大上下文长度限制。这些方法借鉴了人类解决类似问题的认知过程，提出了MindSearch，这是一种简单而有效的基于LLM的多智能体框架，用于模拟人类在网页信息检索和整合中的思维方式。
### Innovation
MindSearch引入了一种基于LLM的多智能体框架，将用户的多步骤信息检索过程建模为动态图构建：将用户查询分解为原子子问题作为图的节点，并逐步扩展基于WebSearcher的搜索结果。WebPlanner负责对每个子问题执行分层信息检索，收集有价值的信息，而WebSearcher则搜集这些信息。这种多智能体设计使框架能够在3分钟内（即人类3小时的工作量）并行地从300多个网页中检索和整合信息，实现了对封闭集和开放集问题的显著改进响应质量和深度广度。
### Conclusion
MindSearch在基于InternLM2.5-7B的实现中表现出了人类对ChatGPT-Web和相关应用的偏好，显示出其已经能够提供具有竞争力的解决方案，甚至超越了现有的专有AI搜索引擎。
## 296. `cs.CL` - SparsePO：通过稀疏トークンマスク控制LLMs的偏好对齐 [PDF](https://arxiv.org/pdf/2410.05102), [HTML](https://arxiv.org/abs/2410.05102)
### Authors
Fenia Christopoulou,Ronald Cardenas,Gerasimos Lampouras,Haitham Bou-Ammar,Jun Wang
### Background
直接对齐算法已被证明是将语言模型与人类期望的行为对齐的有效步骤。当前直接偏好优化目标的变体侧重于一种严格设置，即所有词元都对克隆分布的KL散度和奖励产生贡献信号。然而，人类的偏好并非由序列中的每个词同等影响，而是通常取决于特定的词或短语，例如，存在毒害术语会导致不受欢迎的回应。基于此观察，本文提出了一个新的观点：并非所有词元在偏好优化过程中都应该同等加权，并提出了一种名为SparsePO的灵活目标，旨在通过偏好优化训练自动学习为每个词元学习加权KL散度和奖励。还提出了两种不同的权重掩码变体，可以源自参考模型本身或实时学习。研究表明，这种方法在学习过程中引起了掩码的稀疏性，使模型能够学习如何在词元级别最佳地平衡奖励和KL散度贡献，从而学习到最优的掩码稀疏性水平。
### Innovation
本文提出了一种新的方法SparsePO，用于控制大规模语言模型的偏好对齐。虽然当前的直接偏好优化方法关注所有词元的加权，但SparsePO方法认为并不是所有词元都应同等加权，而是通过一种自动学习机制，动态调整每个词元的权重，特别是通过引入稀疏性和动态学习权重掩码，使模型能够更好地平衡奖励和KL散度的贡献。这种灵活的目标实现了在偏好优化训练中的自动加权学习，并通过实验展示了在情感控制、有用性和无害性以及总结质量方面的有效对齐效果。此外，这种方法在摘要和对话场景中分别获得了10%和3%的胜利点数，而不会损害模型推理或摘要响应的相关性和忠实性。
### Conclusion
鉴于SparsePO方法的成功应用，结论是它能够通过自动学习和调整词元级别的加权，显著提高语言模型行为与期望一致的程度，特别是在辅助性和无害性等关键方面表现出色，同时保持了高效的推理和响应真实性。
## 297. `cs.CL` - 多语言状态空间模型在印度语言结构化问答中的应用 [PDF](https://arxiv.org/pdf/2502.01673), [HTML](https://arxiv.org/abs/2502.01673)
### Authors
Arpita Vats,Rahul Raja,Mrinal Mathur,Vinija Jain,Aman Chadha
### Background
印度语言的多样性和复杂性为自然语言处理（NLP）任务，尤其是问答（QA）领域带来独特的挑战。为应对这些挑战，研究探索了状态空间模型（SSMs）的应用，旨在构建高效且上下文意识强烈的问答系统，专门适用于印度语言。SSMs适合此任务，因为它们能够建模序列数据中的长期和短期依赖关系，使得它们具备处理印度语言中丰富的形态、复杂的语法和上下文复杂性的能力。
### Innovation
研究评估了多种SSM架构，跨多个代表不同印度语言的多样数据集进行了比较分析，结果显示这些模型能有效捕捉语言细微之处，显著改善了问题解释、上下文对齐和答案生成。这是首次将SSMs应用于印度语言的问答任务，建立了未来研究领域的基础标准。提出对现有SSM框架进行增强，以优化其在资源匮乏和多语言情境下的适用性，这些情境在印度语言中很常见。
### Conclusion
这项工作代表了SSMs首次应用于印度语言的问答任务，为未来在此领域的研究奠定了基础，并提出了一系列增强SSM框架的建议，以适应低资源和多语言场景。
## 298. `cs.CL` - SMOL：115种未充分代表语言的专业平行数据 [PDF](https://arxiv.org/pdf/2502.12301), [HTML](https://arxiv.org/abs/2502.12301)
### Authors
Isaac Caswell,Elizabeth Nielsen,Jiaming Luo,Colin Cherry,Geza Kovacs,Hadar Shemtov,Partha Talukdar,Dinesh Tewari,Baba Mamadi Diane,Djibrila Diane,Solo Farabado Cissé,Koulako Moussa Doumbouya,Edoardo Ferrante,Alessandro Guasoni,Christopher Homan,Mamadou K. Keita,Sudhamoy DebBarma,Ali Kuzhuget,David Anugraha,Muhammad Ravi Shulthan Habibi,Genta Indra Winata,Anthony Munthali,Sina Ahmadi,Andrei Chemyshev,Mingfei Lau,Jonathan Eng
### Background
机器翻译一直面临低资源语言的挑战，因为这些语言的数据稀缺，限制了模型的训练效果。
### Innovation
SMOL是一个开源套件，包含124种（持续增长中）低资源语言的平行数据，共计610万翻译词元，特别注重稀缺语言的覆盖。它通过设计两个子集：SMOLSENT和SMOLDOC，以最大化对低资源语言的影响力。研究还展示了使用SMOL来提示或微调大规模语言模型可以显著提升chrF得分，并且提供了第一个用于这些语言的事实性数据集。
### Conclusion
SMOL及其提供的数据可以在促进低资源语言的机器翻译发展方面发挥重要作用，同时为这些语言提供了事实性信息的评估工具。
## 299. `cs.CL` - 大规模语言模型通过自我确定性实现可扩展的Best-of-N选择 [PDF](https://arxiv.org/pdf/2502.18581), [HTML](https://arxiv.org/abs/2502.18581)
### Authors
Zhewei Kang,Xuandong Zhao,Dawn Song
### Background
最佳N选择是通过增加测试阶段计算来提升大型语言模型（LLM）推理性能的关键技术。当前最先进的方法通常使用计算密集型的奖励模型来进行响应评估和选择。然而，不具备外部奖励模型的替代方案，如自我一致性或通用自我一致性，在处理开放生成任务或有效扩展方面存在局限性。
### Innovation
本文提出了一种新的高效度量——自我确定性，该度量利用了LLM输出固有的概率分布来估计响应质量，无需使用外部奖励模型。研究表明，自我确定性通过累积多个样本中的分布自我确定性，在增强生成输出准确性方面具有潜在优势，并在链式思考基础上进一步改进了推理性能，且适用于传统自我一致性方法难以处理的开放生成任务。
### Conclusion
我们的研究证明了自我确定性作为提高LLM推理能力的实用且高效的方法是可行的。研究表明自我确定性在样本数量增加时能有效扩展，类似于奖励模型但无需额外计算开销，并能够处理传统方法难以应对的开放生成任务。
## 300. `cs.CL` - （如何）语言模型跟踪状态？ [PDF](https://arxiv.org/pdf/2503.02854), [HTML](https://arxiv.org/abs/2503.02854)
### Authors
Belinda Z. Li,Zifan Carl Guo,Jacob Andreas
### Background
研究发现，变换器语言模型在故事创作、代码生成等任务中表现出似乎需要追踪不断变化的世界中的未观察状态的行为。本文研究了在排列组合任务中（即计算一系列交换后一组对象的顺序）训练或微调的语言模型如何进行状态追踪。
### Innovation
研究发现了两种状态追踪机制：一种类似于Liu等人（2023）和Merrill等人（2024）近期理论工作中所提出的“关联扫描”构造；另一种则利用一个易于计算的特征（排列符号）部分修剪输出空间，然后通过关联扫描进行细化。结果显示，学习前者的模型泛化能力更强、收敛更快，并展示了如何通过中间训练任务引导模型倾向于采取其中一种机制。
### Conclusion
证明了预训练的或微调的变换器语言模型能够学会实现高效且可解释的状态跟踪机制，而这些机制的出现可以被预测和控制。
## 301. `cs.CL` - 更多同一种类：在增加代表性下的持续代表性危害 [PDF](https://arxiv.org/pdf/2503.00333), [HTML](https://arxiv.org/abs/2503.00333)
### Authors
Jennifer Mickel,Maria De-Arteaga,Leqi Liu,Kevin Tian
### Background
生成型人工智能系统（Generative AI systems）可能会表现出不同程度的社会群体代表性偏见。当前在评估和提高这些系统的代表性时，往往忽略了人们在系统中如何被表现的问题。该研究旨在填补这一空白，探索在未指定提示的场景下，不同群体在生成文本中的代表性偏见和潜在危害。特别是针对性别在职业中的表达，该研究评估了顶级大型语言模型中未指定提示的情况下不同性别代表性的偏见及其相关危害。研究发现，即使通过特定提示增加了女性在职业中的代表性，不同性别的描述仍然存在显著差异，且这些差异与偏见和刻板印象有关。这表明简单地增加代表性可能无意中延续了诸如偏见和刻板印象等问题，强调需要严格的评估方法来识别和减轻这些问题。
### Innovation
提出了GAS(P)评估方法，用于揭示生成文本中未指定提示下的群体代表性偏差，并在顶级大型语言模型中研究性别在职业中的表达情况。该方法不仅证明了不同性别在未指定提示的情况下存在显著的词汇选择差异，还揭示了与代表性和偏见相关的问题。这对于系统评估和减少生成型AI系统中的代表性偏见具有开创性意义。
### Conclusion
该研究结果显示，增加代表性可能会无意中传播代表性偏见和刻板印象，强调需要严谨的评估方法来系统地测量和减轻这些危害。提出了GAS(P)评估方法是一种有效的工具，可用于评估和改进生成型AI系统中的偏见及代表性。
## 302. `cs.CL` - FUSE : 基于岭回归和随机森林的评价指标，用于评价土著语言中的机器翻译 [PDF](https://arxiv.org/pdf/2504.00021), [HTML](https://arxiv.org/abs/2504.00021)
### Authors
Rahul Raja,Arpita Vats
### Background
机器翻译（MT）应用于美洲的土著语言面临诸多挑战，如多合式语法、复杂的形态特征及非标准化的拼写，常规的自动评估指标如BLEU、TER和Chrf未能充分捕捉语义恰当性和流畅性这样的深层特征。
### Innovation
提出了一种Feature-Union Scorer (FUSE)评估方法，通过结合岭回归和梯度提升建模翻译质量。该方法利用了词汇、音韵、语义和模糊标记相似性，并借鉴了基于学习的方法来提高低资源语言和形态丰富的土著语言的翻译评估效果。
### Conclusion
FUSE方法在美洲NLP 2025共享任务3中取得了第一名，并且通过引入多语言句子嵌入和音系编码，展示了在低资源语境下，结合基于学习的方法更能与人类评价相匹配。evaluated held-out测试数据表明，FUSE方法在与人类判断的相关性指标（皮尔逊和斯皮尔曼相关性）中表现更优，提供了一种可靠且语言学导向的翻译评估解决方案。
## 303. `cs.CL` - 使用大型语言模型和基于分类指导推理的多阶段框架进行职业分类 [PDF](https://arxiv.org/pdf/2503.12989), [HTML](https://arxiv.org/abs/2503.12989)
### Authors
Palakorn Achananuparp,Ee-Peng Lim,Yao Lu
### Background
职业分类对于劳动力市场的分析至关重要，但在实际操作中常常受到数据稀缺性和手动标注挑战的影响。尽管大型语言模型（LLMs）因其广泛的世界知识和上下文学习能力而具有潜力，但它们在职业分类上的效果受制于其对职业分类法的理解能力。已有研究评估了LLMs生成精确分类实体的能力，结果表明，小型语言模型尤其受限。为了应对这些挑战，本研究提出了一种多阶段框架，包括推理、检索和再排序阶段，并结合了基于分类指导的推理示例，以通过将输出与分类知识对齐来提高性能。
### Innovation
该研究提出了一种结合了基于分类指导推理示例的多阶段框架，特别设计来解决小型大型语言模型在职业分类上的局限性。这种框架通过整合并结合分类指导的推理来增强性能，实现职业和技能分类任务的提升，并提供了一个成本效益较高的替代方案，优于类似GPT-4o的前沿模型，同时保持高性能。这种多阶段框架具有实际和可扩展性，适用于各种大型语言模型的职业分类任务及相关任务。
### Conclusion
所提出的框架不仅提高了职业和技能分类任务的表现，而且提供了一个成本效益较高的替代方案，优于类似GPT-4o的前沿模型，显著降低了计算成本，同时保持了强大的性能。这使其成为职业分类及相关任务在各种大型语言模型中的一个实用和可扩展的解决方案。
## 304. `cs.CL` - Cancer-Myth：在含有虚假前提的患者问题上评估大型语言模型 [PDF](https://arxiv.org/pdf/2504.11373), [HTML](https://arxiv.org/abs/2504.11373)
### Authors
Wang Bill Zhu,Tianqi Chen,Xinyan Velocity Yu,Ching Ying Lin,Jade Law,Mazen Jizzini,Jorge J. Nieva,Ruishan Liu,Robin Jia
### Background
随着癌症患者越来越多地依赖大型语言模型（LLMs）获取医疗信息，评估这些模型处理复杂个性化问题的能力变得至关重要。当前的医疗基准主要集中在医学考试或消费者搜索的问题上，忽略了对现场患者间题的评估，而这些问题是包含患者详细信息的真实问投。
### Innovation
提出了Cancer-Myth，这是一个专家验证的对抗数据集，包含585个含有虚假前提的癌症相关问题。该数据集用于评估无前沿的LLMs纠正虚假前提的能力，并提出了Cancer-Myth-NFP数据集，其中医生确认不存在虚假前提。研究发现，通常的缓解策略可以提高Cancer-Myth上的准确率至80%，但也会在Cancer-Myth-NFP问投中错误地识别前提，并在其他医疗基准测试中考相对下降10%。
### Conclusion
研究指出LLMs的可靠性存在关键缺口，单纯提示策略无法可靠解决虚假前提问题，强调了在医疗AI系统中需要更稳健的安全措施。
## 305. `cs.CL` - HELIOS：高效 LLM 推断服务的自适应模型和早期退出选择 [PDF](https://arxiv.org/pdf/2504.10724), [HTML](https://arxiv.org/abs/2504.10724)
### Authors
Avinash Kumar,Shashank Nag,Jason Clemons,Lizy John,Poulami Das
### Background
早期退出大语言模型（EE-LLMs）通过允许在中间层使代词提前来实现高吞吐量推理，但由于计算和内存节省有限，其吞吐量受到限制。现有的 EE-LLM 框架依赖单一模型，因此代词生成延迟受限于不提前退出且需要额外遍历多层的代词。此外，早期退出仅在运行时已知并取决于请求，因此这些框架即使在代词提前退出时仍加载所有模型层的权重，导致缺乏内存节省而不能扩展批量大小。
### Innovation
提出了名为 HELIOS 的框架，旨在同时提高代词生成延迟和批量大小以实现 EE-LLMs 的高吞吐量。HELIOS 利用了两个见解：一是早期退出在不同模型之间通常是互补的，而不会提前退出的代词在其他模型中可能会提前退出；二是即便因预测置信度低延迟退出，但代词通常仍会保持不变，此类代词可以贪婪地提前退出并仅加载最有可能被使用的层权重，从而节省内存。通过实时分析提前退出的分布，并监控代词实时切换模型，最大化性能效益，同时最小化贪婪模型加载和退出引起的性能下降。
### Conclusion
我们的评估显示，与现有的 EE-LLM 框架相比，HELIOS 实现了 1.48 倍的更高吞吐量和 15.14 倍的大批量处理能力。
## 306. `cs.CL` - 视频和文本的集成：多模态总结生成与评估的平衡方法 [PDF](https://arxiv.org/pdf/2505.06594), [HTML](https://arxiv.org/abs/2505.06594)
### Authors
Galann Pennec,Zhengyuan Liu,Nicholas Asher,Philippe Muller,Nancy F. Chen
### Background
视觉-语言模型（VLMs）在处理复杂多模态输入（如整集电视节目）时，难以平衡视觉和文本信息。现有的总结方法在自动生成剧本和命名角色时需要大量的预定义数据，并且现有的摘要评估指标往往不足以评估多模态信息的内容。
### Innovation
提出了一种零样本视频转文本总结的方法，能够自行构建剧本文本，综合视频中的关键时刻、对话和角色信息，并同时生成剧本和命名角色，仅需音频、视频和转录作为输入。此外，引入了一种新指标MFactSum，用于评估多模态摘要，针对视觉和文本模态进行评估，从而更好地评价多模态内容。
### Conclusion
使用MFactSum评估剧本文本摘要在SummScreen3D数据集中，证明了该方法优于最先进的VLMs（如Gemini 1.5），生成的摘要包含更多相关视觉信息（多20%）且需要更少的视频输入（减少75%）以生成这些信息。
## 307. `cs.CL` - Minitron-SSM: 通过组意识SSM剪枝实现高效混合语言模型压缩 [PDF](https://arxiv.org/pdf/2504.11409), [HTML](https://arxiv.org/abs/2504.11409)
### Authors
Ali Taghibakhshi,Sharath Turuvekere Sreenivas,Saurav Muralidharan,Marcin Chochowski,Yashaswi Karnati,Raviraj Joshi,Ameya Sunil Mahabaleshwarkar,Zijia Chen,Yoshi Suhara,Oluwatobi Olabiyi,Daniel Korzekwa,Mostofa Patwary,Mohammad Shoeybi,Jan Kautz,Bryan Catanzaro,Ashwath Aithal,Nima Tajbakhsh,Pavlo Molchanov
### Background
混合架构结合了注意力模型和状态空间模型（SSMs），展现了最先进的准确性和运行时性能。最近的研究表明，对仅使用注意力机制的模型进行压缩和蒸馏可以得到更小、更准确的模型，且训练成本更低。本文继承了这一趋势，探索混合架构的压缩效果。文中提出了一种新型的组意识剪枝策略，旨在保留SSM模块的结构完整性及其序列建模能力。研究还展示了Such SSM剪枝对于达到传统方法无法实现的更高准确性和推理速度的必要性。综上，研究结合了SSM、FFN、嵌入维度和层剪枝，并采用了基于知识蒸馏的重训练方法，最终将Nemotron-H 8B混合模型压缩到4B参数，训练样本数减少至原来的四十分之一。压缩后的模型不仅保持了与同等大小模型相同的准确度，还实现了两倍的推理速度，显著推进了帕累托边界。
### Innovation
本文引入了一种新型的组意识剪枝策略，该策略能够保留SSM模块的结构和序列建模能力，从而在压缩混合模型时提高准确度和推理速度。此外，研究还提出了一种全新的压缩配方，结合了SSM、FFN、嵌入维度和层剪枝技术，然后通过基于知识蒸馏的重训练来完成。最终，研究成功将大模型Nemotron-H 8B压缩到4B参数，同时达到了更高的准确性和更快的推理速度。
### Conclusion
本文通过引入组意识的SSM剪枝策略和技术，成功地将Nemotron-H 8B的混合架构压缩到4B参数，同时保持相同的准确度和两倍的推理速度。这显著推进了高性能语言模型的优化，对未来的模型压缩工作具有重要的参考价值。
## 308. `cs.CL` - VeriFastScore：加速长文事实性评估 [PDF](https://arxiv.org/pdf/2505.16973), [HTML](https://arxiv.org/abs/2505.16973)
### Authors
Rishanth Rajendhran,Amir Zadeh,Matthew Sarte,Chuan Li,Mohit Iyyer
### Background
现有的评价长段落事实性的度量标准（如FactScore和VeriScore），通过将输入回应分解为基本主张并逐一验证每个主张来工作。虽然有效且易于解释，但这些方法需要大量的LLM调用，评估单个回应可能需要100秒以上的时间，这限制了它们在大规模评估和训练场景中的实用性。
### Innovation
本文提出了VeriFastScore，一种利用合成数据微调Llama3.1 8B来同时从Google搜索证据中提取和验证所有可验证的主张的方法。这种方法不能通过少样本提示解决闭合LLM的问题，因为任务过于复杂，模型会接收平均约4K个标记的证据，并同时进行主张的分解、判断其可验证性和与噪音证据的验证。经过微调的VeriFastScore模型在示例级别与原始的VeriScore管道表现出0.80的相关性，在系统级别则表现出0.94的相关性，相比VeriScore总速度快6.6倍（排除证据检索情况下的9.9倍）
### Conclusion
为了促进未来事实性研究，本文公开发布了VeriFastScore模型和合成数据集。
## 309. `cs.CL` - 使用扩散语言模型强化横向思维链 [PDF](https://arxiv.org/pdf/2505.10446), [HTML](https://arxiv.org/abs/2505.10446)
### Authors
Zemin Huang,Zhiyang Chen,Zijun Wang,Tiancheng Li,Guo-Jun Qi
### Background
本文介绍了扩散语言模型（Diffusion Language Models, DLMs）的推理框架——扩散思维链（Diffusion Chain of Lateral Thought, DCoLT）。DLMs是通过反向扩散过程来生成文本的模型，而传统的思维链（CoT）方法则遵循线性的因果推理过程。DCoLT通过基于结果的强化学习（Outcome-based Reinforcement Learning, RL）优化整个推理过程，使其能够进行双向而非线性的非线性推理，而不严格要求中间步骤的语法正确性。本文在两个代表性DLMs上实现了DCoLT，分别是连续时间离散扩散模型SED和离散时间掩码扩散语言模型LLaDA。
### Innovation
本文提出的DCoLT框架创新之处在于它通过基于结果的RL优化整个扩散推理过程，允许进行双向而非线性的非线性推理。对于连续时间离散扩散模型SED，它利用具体的评分来最大化整个中间扩散步骤的RL奖励。对于离散时间掩码扩散语言模型LLaDA，引入了基于Plackett-Luce模型的排名解码策略模块（Unmasking Policy Module, UPM）来优化其RL行为。实验结果表明，使用DCoLT强化的DLMs在数学和代码生成任务中表现优异，比通过SFT或RL或两者结合训练的其他DLMs更胜一筹。
### Conclusion
使用DCoLT强化的DLMs在数学和代码生成任务中表现出色。实验使用公共数据和16个H800 GPU进行，并验证了DCoLT的质量。具体来说，在GSM8K、MATH、MBPP和HumanEval任务上，DCoLT强化的LLaDA分别提高了9.8%、5.7%、11.4%和19.5%的推理准确性。
## 310. `cs.CL` - Token Distillation: Attention-aware Input Embeddings For New Tokens [PDF](https://arxiv.org/pdf/2505.20133), [HTML](https://arxiv.org/abs/2505.20133)
### Authors
Konstantin Dobler,Desmond Elliott,Gerard de Melo
### Background
当前的语言模型依赖于在预训练时固定的词汇表，这对于在原始词汇表中代表性不足的领域来说会导致性能下降和计算成本增加。虽然可以通过添加新词汇来解决这个问题，但需要良好的新的嵌入初始化。然而，现有的嵌入初始化方法通常需要额外的训练或预训练，这既昂贵又费时。现有的方法不能很好地解决这一问题，需要进一步的训练或预训练过程来优化新词汇的嵌入。因此，需要一种新的方法，在不增加额外计算成本的前提下，能够快速学习高质量的输入嵌入。
### Innovation
本文提出了一种名为Token Distillation的技术，通过蒸馏使用原始分词获得的表示，可以迅速学习高质量的输入嵌入，从而为新词汇提供好的嵌入。实验结果表明，Token Distillation在多种开放模型中表现出色，甚至优于强大的基线方法。这种技术可以有效降低新词汇的融入成本，减少训练时间和计算资源的消耗。
### Conclusion
基于Token Distillation的技术，无需额外的训练或预训练过程，可快速学习高质量的新词汇嵌入。实验结果表明，Token Distillation在多种开放模型中表现优异，甚至优于强大的基线方法，证明了其在处理新词汇融入问题上的有效性。
## 311. `cs.CL` - AstroVisBench: 天文学中科学计算和可视化的代码基准 [PDF](https://arxiv.org/pdf/2505.20538), [HTML](https://arxiv.org/abs/2505.20538)
### Authors
Sebastian Antony Joseph,Syed Murtaza Husain,Stella S. R. Offner,Stéphanie Juneau,Paul Torrey,Adam S. Bolton,Juan P. Farias,Niall Gaffney,Greg Durrett,Junyi Jessy Li
### Background
大型语言模型（LLMs）在科学研究中的应用日益增多，包括文献综合、回答研究问题、生成研究思路甚至执行计算实验。科学发现往往来自数据分析和可视化，但评估由LLM驱动的工作流是否能产生正确的科学见解颇具挑战且已有研究尚未涉及。当前缺乏专门用于处理和分析天文学数据及结果可视化的基准评价工具。
### Innovation
本文提出AstroVisBench，这是首个天文学领域的科学计算和可视化基准。它评价语言模型处理数据的能力及生成复杂图表的能力。评估过程采用新颖的LLM作为裁判机制，通过五名专业天文学家的标注验证。该基准填补了天文学领域评价空白，帮助识别现有模型的不足，并促进基于可视化的工作流开发。
### Conclusion
使用AstroVisBench对当前最先进的语言模型进行了评估，结果显示这些模型在支持天文学研究方面还有显著差距，提供了一套从头到尾的评价方法，为AI科学家的发展路径提供了方向，特别适用于物理学和生物学等广泛的领域。
## 312. `cs.CL` - 通过自适应并行解码加速扩散大语言模型 [PDF](https://arxiv.org/pdf/2506.00413), [HTML](https://arxiv.org/abs/2506.00413)
### Authors
Daniel Israel,Guy Van den Broeck,Aditya Grover
### Background
现有的大型语言模型（LLMs）的生成速度受限于自回归解码过程，其中每一个令牌都要依次预测。虽然扩散大语言模型（dLLMs）理论上可以实现并行令牌生成，但在实践中难以达到自回归模型的速度，且会严重牺牲质量。
### Innovation
本文提出了一种名为自适应并行解码（APD）的新方法，它通过定义dLLM边缘概率与小型辅助自回归模型下序列的联合概率之间的乘性混合来动态调整并行采样的令牌数量。这种方法逆转了推测性解码的标准设定，并进一步通过启用KV缓存和限制遮罩输入的大小进行了优化。实验结果表明，APD在下游基准测试中能够显著提高吞吐量，且质量损失很小。
### Conclusion
本文提出了自适应并行解码（APD），这是一种能够灵活权衡吞吐量和质量的新方法，能够在保持质量的前提下大幅度提高扩散大语言模型的生成速度。
## 313. `cs.CL` - FastLongSpeech: 提升大型语言-语音模型在高效处理长语音方面的能力 [PDF](https://arxiv.org/pdf/2507.14815), [HTML](https://arxiv.org/abs/2507.14815)
### Authors
Shoutao Guo,Shaolei Zhang,Qingkai Fang,Zhengrui Ma,Min Zhang,Yang Feng
### Background
大型语言模型（LLMs）的快速发展推动了大型语音-语言模型（LSLMs）的进步，这些模型在语音理解和生成方面的能力得到了增强。尽管现有的LSLMs通常专注于增强语音生成或解决各种短语音任务，但处理长语音形式的有效性仍然是一个重要且未被充分探索的挑战。这主要是由于缺乏长语音训练数据集和长序列的高计算成本。
### Innovation
本文引入了FastLongSpeech框架，旨在在无需依赖专用长语音训练数据的情况下，扩展LSLMs的能力，以实现高效的长语音处理。FastLongSpeech采用迭代融合策略压缩过长的语音序列，使其变得容易处理。此外，该框架引入了一种动态压缩训练方法，通过对不同压缩比的短语音序列进行训练，使模型能够适应长语音任务。
### Conclusion
实验表明，我们的方法在长语音和短语音任务中都有很强的性能，并且极大地提高了推理效率。
## 314. `cs.CL` - 数学不是文化无感的：通过实体和情境扰动探究文化差异 [PDF](https://arxiv.org/pdf/2507.00883), [HTML](https://arxiv.org/abs/2507.00883)
### Authors
Aditya Tomar,Nihar Ranjan Sahoo,Ashish Mittal,Rudra Murthy,Pushpak Bhattacharyya
### Background
虽然数学常被认为是文化中立的，但数学问题的呈现方式仍可能隐含文化背景。现有的基准数据集如GSM8K主要基于西方规范，包括名字、货币和日常生活场景。本文研究了在非洲、印度、中国、韩国和日本创建的GSM8K测试集的文化适应版本，通过提示基转变和人工验证。评估了六种大型语言模型（LLMs），参数范围从8B到72B，以考察它们在数学问题呈现文化差异上的鲁棒性。研究发现，模型在原始以美国为中心的数据集上表现最好，而对文化适应版本的性能相对较差，但具备推理能力的模型更能应对这种变化，表明深层次的推理能更有效地弥合文化呈现差异.
### Innovation
创建了五大地区文化适应版本的GSM8K测试集，通过实体和情境扰动方法评估了六种大型语言模型在不同文化背景下对数学问题的鲁棒性，并揭示了模型性能与文化背景关系的新见解。
### Conclusion
研究发现，大型语言模型在原始文化背景的数学问题集上表现最佳，但在文化适应版本上表现相对较差，且具备推理能力的模型更能有效应对文化差异带来的挑战，表明深层推理能力有助于解决数学任务中的文化表现差异。
## 315. `cs.CL` - 大规模语言模型的多语言政治观点：识别与操控 [PDF](https://arxiv.org/pdf/2507.22623), [HTML](https://arxiv.org/abs/2507.22623)
### Authors
Daniil Gurgurov,Katharina Trinley,Ivan Vykopal,Josef van Genabith,Simon Ostermann,Roberto Zamparelli
### Background
大规模语言模型（LLMs）在日常生活工具和应用中被日益广泛应用，引发了对其潜在政治观点影响的担忧。尽管先前的研究展示了LLMs通常存在可测量的政治偏见，并倾向于自由或进步立场，但关于这些偏见在不同架构、规模和多语言环境中的普遍性，现有的研究仍存在不足。此外，很少有研究探讨这些偏见是否可以被主动控制。
### Innovation
本研究通过大规模研究现代开源指令调优的大规模语言模型的政治倾向，评估了包括LLaMA-3.1、Qwen-3和Aya-Expanse在内的七种模型，在14种语言上使用政治理想定位测验（Political Compass Test）和11种语义等价的改述来确保测量的稳健性。研究发现，较大的模型倾向于自由左翼立场，并展示了在多种语言中通过简单的方法干预可使模型响应转向不同意识形态的变化。研究结果表明这些偏见是可操控的。
### Conclusion
研究揭示了更大规模的LLMs更倾向于自由左翼立场，但不同语言和模型家族之间存在显著差异。通过简单的中心质量激活干预技术，模型响应可以被可靠地引导至不同意识形态立场。我们的代码已公开。
## 316. `cs.CL` - 准备好翻译，但不代表什么？跨语言家族和领域多语言LLM的偏见与性能差距 [PDF](https://arxiv.org/pdf/2510.07877), [HTML](https://arxiv.org/abs/2510.07877)
### Authors
Md. Faiyaz Abdullah Sayeedi,Md. Mahbub Alam,Subhey Sadi Rahman,Md. Adnanul Islam,Jannatul Ferdous Deepti,Tasnim Mohiuddin,Md Mofijul Islam,Swakkhar Shatabda
### Background
大语言模型（LLMs）的兴起重新定义了机器翻译（MT），使其能够在数百种语言和文本领域中实现上下文感知和流畅的翻译。尽管LLMs具有令人印象深刻的能力，但在不同语言家族和专业领域中的表现通常存在不均衡。此外，最近的研究发现这些模型在训练数据中存在的不同偏见得到了编码和放大，这引发了公平性方面的问题，特别是在低资源语言方面。
### Innovation
本文引入了Translation Tangles，这是一种统一的框架和数据集，用于评估开源LLMs的翻译质量和公平性。该方法使用不同的指标对24种双向语言对在多个领域的表现进行了基准测试。此外，提出了一种将基于规则的启发式、语义相似性和LLM验证集成的混合偏见检测管道。还基于1,439个翻译-参考对的人类评估，引入了一个高质量的偏见注释数据集。
### Conclusion
该研究基于Translation Tangles框架提供了一个实验结果和一个高注释质量的数据集，并且其代码和数据集可通过GitHub访问。该工作对于提高多语言LLMs的翻译质量和公平性具有重要意义。
## 317. `cs.CL` - 知识魔咒：复杂评估背景既有助于LLM法官又使其产生偏差 [PDF](https://arxiv.org/pdf/2509.03419), [HTML](https://arxiv.org/abs/2509.03419)
### Authors
Weiyuan Li,Xintao Wang,Siyu Yuan,Rui Xu,Jiangjie Chen,Qingqing Dong,Yanghua Xiao,Deqing Yang
### Background
随着大型语言模型（LLMs）的能力不断增强，它们面临的任务变得越来越多样化和复杂，这使得可靠的评估变得颇具挑战性。此前，LLMs作为一种可扩展解决方案的法官模型已崭露头角，但主要集中在简单情境中。然而，这些模型在面对复杂任务时的可靠性却鲜少受到研究，特别是涉及多方面评分标准、非结构化参考答案和细微评判标准的任务。本文旨在填补这一空白，通过构建ComplexEval挑战基准，系统探究和验证了6种未被探索的偏差，涵盖12个基础情境和3个高级情境，以揭示这些偏差对LLMs评估性能的影响.
### Innovation
本文主要创新在于构建了ComplexEval挑战基准，用于系统地揭露并量化由辅助信息引起的各种偏差。该基准涵盖了15个不同层级的情景，系统地调查并验证了6种已前所未见的偏差。此外，本文深入分析了这些偏差的影响，提供了解决评估信号准确性和可验证性问题的关键见解，为更通用和稳健的评估模型的开发奠定了基础.
### Conclusion
研究发现，所有评估模型都对这些偏差显示出显著的敏感性，且偏倚的强度随着任务复杂度的增加而增加。让人大感意外的是，大型推理模型（LRMs）在高复杂度任务中表现出反常的脆弱性。深入分析揭示了提高评估信号准确性和可验证性的关键洞察，推动了更通用和稳健评估模型的发展.
## 318. `cs.CL` - Prompt-MII: 用于大型语言模型的元学习指令归纳 [PDF](https://arxiv.org/pdf/2510.16932), [HTML](https://arxiv.org/abs/2510.16932)
### Authors
Emily Xiao,Yixiao Zeng,Ada Chen,Chin-Jou Li,Amanda Bertsch,Graham Neubig
### Background
一个流行的方法是利用上下文学习（ICL）将大型语言模型（LLMs）适应到新任务中，这种方法非常有效，但随着上下文长度的增长，会产生较高的推理成本。
### Innovation
本文提出了一种方法来进行指令归纳，该方法从训练示例中提炼出一个紧凑但描述性的提示，可以与ICL在完整训练集上达到相当的性能。具体而言，提出了一种基于强化学习（RL）的元学习框架PROMPT-MII，该框架用于元学习生成适用于任意新数据集的紧凑指令。通过在HuggingFace枢纽上超过3000个不同的分类数据集上进行训练，并在90个未见过的任务上进行评估，PROMPT-MII使下游模型质量提高了4-9个F1分数点（相当于10-20%的相对改进），同时只需要比ICL少3-13倍的令牌。
### Conclusion
PROMPT-MII在促进大型语言模型适应新任务的同时，显著降低了推理成本。
## 319. `cs.CL` - KAT-Coder技术报告 [PDF](https://arxiv.org/pdf/2510.18779), [HTML](https://arxiv.org/abs/2510.18779)
### Authors
Zizheng Zhan,Ken Deng,Jinghui Wang,Xiaojiang Zhang,Huaixi Tang,Minglei Zhang,Zhiyi Lai,Haoyang Huang,Wen Xiang,Kun Wu,Wenhao Zhuang,Shaojie Wang,Shangpeng Yan,Kepeng Lei,Zongxian Feng,Huiming Wang,Zheng Lin,Mengtong Li,Mengfei Xie,Yinghan Cui,Xuxing Chen,Chao Wang,Weihao Li,Wenqiang Zhu,Jiarong Zhang,Jingxuan Xu,Songwei Yu,Yifan Yao,Xinping Lei,C. Zhang,Han Li,Junqi Xiong,Zuchen Gao,Dailin Li,Haimo Li,Jiaheng Liu,Yuqun Zhang,Junyi Peng,Haotian Zhang,Bin Chen
### Background
大型语言模型（LLMs）的进步推动了自代理编码的发展，使模型能够在交互的软件开发工作流中自主推理、计划和执行。然而，静态文本训练与动态现实世界的自主执行之间的鸿沟依然是一个核心挑战。
### Innovation
提出了一个多阶段的KAT-Coder自代理代码模型，该模型通过中期训练、监督微调（SFT）、强化微调（RFT）和从强化到部署的适应性适应大规模的发展。各阶段包括通过真实软件工程数据和合成代理交互增强推理、计划和反思能力；构建一个平衡了二十种编程语言、十个开发环境和十种任务范式的百万样本数据集；提出了一种新颖的多真实情况奖励公式进行稳定的样本高效策略优化；以及使用错误屏蔽的SFT和基于树的轨迹训练，使模型适应生产级集成开发环境。
### Conclusion
这些阶段使KAT-Coder能够实现稳健的工具使用可靠性、指令对齐和长上下文推理，为现实中的智能编码代理提供了可部署的基础。KAT系列32B模型KAT-Dev已开源。
## 320. `cs.CL` - 通过模型合并导航对齐和校准之间的权衡：帕列托占优前沿 [PDF](https://arxiv.org/pdf/2510.17426), [HTML](https://arxiv.org/abs/2510.17426)
### Authors
Tiancheng Hu,Benjamin Minixhofer,Nigel Collier
### Background
通常认为模型对齐后的“对齐税”会表现为任务准确度的下降。本文指出，这种损失还包括了严重的校准损失，使得模型过度自信，降低了可靠性，并且模型输出不够多样化。研究者们展示了可以通过简单后处理手段—在模型对齐前后权重之间进行插值—有效地解决这一权衡。更重要的是，这一过程揭示了一种占优的平衡点—模型的准确度可以超过对齐后的模型和原本模型的准确度水平，同时还能显著恢复校准性的损失。研究发现，使用简单的模型合并方法可以提高模型的全面能力与可靠性，从而抵消对齐税的负面影响，并证明了这种方法的计算效率。
### Innovation
提出了一种简单有效的后处理干预手段，即在模型对齐前后权重之间进行插值。这种干预方法不仅仅能够有效减少校准损失和过度自信所带来的问题，还能够发现模型的帕列托最优解，使得模型的表现优于对齐后的模型和对齐前的模型，同时显著恢复了对齐过程中丢失的校准性。这证明了简单的模型合并方法可以有效地减少对齐税的全面影响，为模型提供更好的能力和可靠性。
### Conclusion
本文通过简单的模型合并方法，有效减少了模型对齐后的准确度损失和校准损失，证明了这种帕列托最优的插值方法可以在保留模型能力的同时提高其可靠性，从而提供了一种节省成本且有效的缓解对齐税的方法。
## 321. `cs.CL` - E2Rank: 文本嵌入模型也可以是高效可靠的列表级重排序器 [PDF](https://arxiv.org/pdf/2510.22733), [HTML](https://arxiv.org/abs/2510.22733)
### Authors
Qi Liu,Yanzhao Zhang,Mingxin Li,Dingkun Long,Pengjun Xie,Jiaxin Mao
### Background
文本嵌入模型作为现实搜索应用中的基本组件，通过将查询和文档映射到共享的嵌入空间，实现了高效率和竞争力的检索性能。然而，这些模型的排名准确性仍然不及专门的重排序器，尤其是在捕获细粒度的查询-文档和文档-文档交互方面，最新的基于LLM的列表级重排序器能力更强。
### Innovation
本文提出了一种简单而有效的统一框架E2Rank，即高效嵌入式排名（Embedding-to-Rank），它通过使用列表级排名目标在后续训练中扩展单一文本嵌入模型，以实现高质量检索和列表级重排序，并通过使用余弦相似性作为统一的排名函数，增强了查询以近似伪相关反馈（PRF）的方式提升了重排序性能。此外，E2Rank在BEIR重排序基准上的实验结果表明，其表现出色且具有很低的重排序延迟，特别是在推理密集的BRIGHT基准上，同时对MTEB基准上的嵌入性能也有显著提升。
### Conclusion
单个嵌入模型可以有效地统一检索和重排序，提供计算效率和竞争性的排名准确性。
## 322. `cs.CL` - DiffAdapt: 针对高效推理的难度自适应大模型推理 [PDF](https://arxiv.org/pdf/2510.19669), [HTML](https://arxiv.org/abs/2510.19669)
### Authors
Xiang Liu,Xuming Hu,Xiaowen Chu,Eunsol Choi
### Background
近期的大语言模型（LLMs）在解决问题的能力上表现出色，但经常会生成冗长的推理轨迹，这些轨迹的实用性尚不明确。本文旨在提高LLMs的效率，使其能够在不进行过度思考的情况下达到高绩效。研究者首先分析了推理轨迹中词元概率的熵，并在三个模型上观察到一致的U型熵模式：在简单问题上熵高但准确度高，在难度适中的问题上熵低，在困难问题上熵高，以反映不确定性。具体而言，从简单到中等难度区间，熵降低了22-25%，表明在简单实例上存在过度思考的现象。
### Innovation
本文引入了一种轻量级框架DiffAdapt，该框架根据问题的难度和推理轨迹的熵值选择易/平常/难推理策略。每个推理策略包括固定的提示、温度和最大词元长度。与现有方法不同，本文的方法是对基础LLM进行微调，而是对一个小探测器进行微调，该探测器分类LLM的最终隐藏状态，这使得适应更为经济。该方法在五个模型和八个基准上进行了全面评估，实现了与或优于现有方法的准确性并减少了高达22.4%的词元使用量，为计算高效推理提供了实用途径。
### Conclusion
本文介绍了一种高效推理方法DiffAdapt，该方法在保持或提高准确性的同时，有效减少了词元使用量，为未来计算高效的推理提供了实证方法，并为其在实际应用中的推广奠定了基础。
## 323. `cs.CL` - SynthWorlds: 受控并行世界用于分离语言模型中的推理与知识 [PDF](https://arxiv.org/pdf/2510.24427), [HTML](https://arxiv.org/abs/2510.24427)
### Authors
Ken Gu,Advait Bhat,Mike A Merrill,Robert West,Xin Liu,Daniel McDuff,Tim Althoff
### Background
评估语言模型（LMs）的推理能力受到其广泛的世界知识参数的影响，基准测试常常反映的是事实记忆而非真正的推理。现有的数据集和方法（如时间过滤、重写和对抗替换）无法清晰地分离这两者。
### Innovation
作者提出了SynthWorlds框架，该框架将任务推理复杂性从事实性知识中分离出来。该框架构建了两个拥有相同连通结构的平行语料庫：一个与现实世界对应，模型可以利用参数知识；另一个则是合成的，参数知识在这个世界无效。在此基础上设计了两个对称任务作为案例研究，用于评估语言模型在仅有参数知识和知识增强设置中的推理与记忆差距。这种方法使得无需人工干预即可自动进行大规模评估，从而提供一个受控环境来精确评估LMs的推理和记忆能力方面的对比。
### Conclusion
实验结果显示，在仅有参数知识和知识增强设置下，模型从记忆参数世界知识中获得持续的知识优势，知识获取和融合机制虽有所减少但未能消除这一差距，突出了系统改进的机会。SynthWorlds提供了一种新的方法，使得以前难以实现的环境下的LM评估变得可能，从而能够进行精确和可验证的推理和记忆能力比较。
## 324. `cs.CL` - DiagramEval: Via图形评估LLM生成的图表 [PDF](https://arxiv.org/pdf/2510.25761), [HTML](https://arxiv.org/abs/2510.25761)
### Authors
Chumeng Liang,Jiaxuan You
### Background
图表在科研论文中起着核心作用，用于传达想法，但由于其复杂性和制作的劳动密集型，通常非常难制作。尽管图表可以视为图像，但现有的图像生成模型在生成具有明确结构的清晰图表方面表现不佳。我们提出了一个有希望的方向：直接生成文本形式的示范图表作为SVG，利用大型语言模型（LLMs）的最新进展。然而，由于图表组件复杂性和多模态性，现有对LLM生成图表质量的评估仍缺乏足够的区分性和可解释性指标。本文提出了DiagramEval，这是一种新的评估指标，旨在评估由LLM生成的示范图表。该指标将图表视为图，文字元素作为节点，其连接作为有向边，并使用两种新的度量标准组：节点对齐和路径对齐来评估图表质量。
### Innovation
本文提出了名为DiagramEval的新评估指标，该指标将图表视为图，并采用节点对齐和路径对齐的新度量标准组来评估LLM生成图表的质量。这是首次对最先进的LLM生成的图表进行有效评估，量化证明了该指标的有效性。此外，该指标的增强可解释性提供了有关LLM生成图表特点的有价值见解。
### Conclusion
首次对最先进的LLM生成的图表进行有效评估，量化证明了我们指标的有效性。此外，我们展示了我们提出的指标的增强可解释性，提供了关于LLM生成图表特点的有价值见解。
## 325. `cs.CL` - 损失曲率谱中的记忆到推理 [PDF](https://arxiv.org/pdf/2510.24256), [HTML](https://arxiv.org/abs/2510.24256)
### Authors
Jack Merullo,Srihita Vatsavaya,Lucius Bushnaq,Owen Lewis
### Background
我们分析了变压器模型中记忆的表示，并展示了如何通过基于损失景观曲率的分解在语言模型（LMs）和视觉变压器（ViTs）的权重中分离记忆。研究表明，记忆化训练点的曲率要明显更尖锐，而非记忆化的曲率则较不明显，因此可以依据曲率将权重组件从高到低排序来揭示这一差异。这促使我们开发了一种权重编辑方法，这种方法相比于最近的去学习方法（BalancedSubnet），能够更有效地抑制未指定的记忆数据的再现出现，同时保持较低的困惑度。基于曲率的自然解释，在模型权重中共享结构，我们深入分析了编辑程序对下游任务的影响，并发现特定且一致地影响了事实检索和算术任务，尽管开放书事实检索和一般逻辑推理任务保持不变。这表明，这些任务依赖于权重空间中的专门方向而非通用机制，不管这些单独的数据点是否被记忆化。我们通过展示任务数据激活强度与我们编辑出的低曲率组件之间的对应关系，以及编辑后的任务性能下降来支持这一观点。我们的工作增强了对神经网络中记忆理解并具有实际应用价值，同时也提供了专门且狭窄使用的结构在解决数学和事实检索等任务中起作用的证据。
### Innovation
该研究提出了一种基于损失曲率分解的方法，通过权重编辑有效区分和抑制记忆内容，同时保持了模型的泛化性能。该方法使得未指定的记忆数据再现出现大幅减少，而困惑度较低。研究还发现了不同任务对权重空间中特定方向的依赖性，尤其是算术和事实检索任务，这些任务依赖于专门的权重方向而非通用机制。
### Conclusion
我们的研究加深了对神经网络中记忆机制的理解，并提出了一种实用的方法来消除记忆。此外，该研究还揭示了专门且狭窄使用的结构在解决特定任务，如数学和事实检索中的作用，这为理解复杂的推理任务提供了新的见解。
## 326. `cs.CL` - 从手动解码到真正意义上的端到端语言模型 [PDF](https://arxiv.org/pdf/2510.26697), [HTML](https://arxiv.org/abs/2510.26697)
### Authors
Zhichao Wang,Dongyang Ma,Xinting Huang,Deng Cai,Tian Lan,Jiahao Xu,Haitao Mi,Xiaoying Tang,Yan Wang
### Background
当前的大型语言模型（LLMs）的‘端到端’标签是个误解，实际上它们依赖于非可微分的解码过程，这需要手工调参，比如温度和top-p等超参数。这些调参过程复杂且耗时。因此，研究者们尝试找到一种能够真正实现端到端生成的模型，即能够自主控制解码策略的模型。已有研究大多依赖于静态方法或需要人工调参，这限制了模型的灵活性和自适应性。
### Innovation
本文提出了AutoDeco架构，这是一种新的模型能够自主学习控制自己的解码策略。该模型通过在标准变压器中加入轻量级头来动态预测上下文相关的温度和top-p值，将解码转换为一个可参数化的、基于token的过程。在八个基准测试上，AutoDeco不仅显著优于默认的解码策略，还实现了与通过‘破解测试集’得到的oracle调优基线相当的性能，证明了其强大的自适应能力。此外，研究还揭示出一种基于指令的解码控制能力：模型能够理解自然语言命令（如“生成低随机性内容”）并在逐token的基础上调整预测的温度和top-p值，这开启了可操控和交互的LLM解码的新范式。
### Conclusion
通过大量的实验，验证了AutoDeco在主要任务上的优越性，同时也证明了模型具备自适应和基于指令的解码控制能力，这标志着从手动解码向真正端到端的语言模型过渡的关键一步。
## 327. `cs.CL` - NeuronMM: 高性能矩阵乘法在AWS Trainium上的LLM推理 [PDF](https://arxiv.org/pdf/2510.25977), [HTML](https://arxiv.org/abs/2510.25977)
### Authors
Dinghong Song,Jierui Xu,Weichu Yang,Pengfei Su,Dong Li
### Background
AI加速器为特定的人工智能负载定制，提供了具有成本效益且高性能的训练和推理解决方案。亚马逊网络服务（AWS）开发的Trainium是一种异构架构的AI加速器，为大型语言模型（LLM）的训练和推理提供了吸引人的选项。然而，Trainium的结构和数据布局要求使得充分利用其高性能变得具有挑战性，特别是由于其基于阵列的结构。因此，需要设计特定于Trainium的高性能矩阵乘法（matmul）算法以优化其计算效率，从而加速LLM推理过程。研究者们评估了九个数据集和四个现代LLM模型，证明了所设计的系统在矩阵乘法内核以及端到端的LLM推理中实现了显著的性能提升。
### Innovation
研究团队设计了针对Trainium的高性能矩阵乘法算法，基于核融合和新颖的缓存策略减少软件管理内存层次结构中的数据移动，最大化SRAM带宽，并避免昂贵的矩阵转置。这些特定于Trainium的技术显著提高了LLM推理的计算速度，相比于AWS最新实现的矩阵乘法内核，平均加速1.35倍（最高2.22倍），端到端的LLM推理性能平均提高1.66倍（最高2.49倍）。
### Conclusion
该研究展示了针对Trainium设计的高性能矩阵乘法在LLM推理中的高效实现，并在多种现代LLM模型中验证了其显著的性能优势。该工作通过优化矩阵乘法（matmul）的计算向量，解决了Trainium架构的性能挑战，为LLM推理任务提供了有效的解决方案。
## 328. `cs.CL` - 代表性的社会选择：从学习理论到AI对齐 [PDF](https://arxiv.org/pdf/2410.23953), [HTML](https://arxiv.org/abs/2410.23953)
### Authors
Tianyi Qiu
### Background
社会选择理论研究一个群体的偏好聚合，既应用于机制设计中针对人类代理，也应用于语言模型的民主校准。在现实世界中，当问题数量和个体数量过多以至于无法直接考虑所有偏好时，需要一种新的社会选择框架来设计集体决策。这些场景常见于诸如陪审团审判、立法、公司治理等决策过程，以及最近的语言模型对齐领域。
### Innovation
本文提出了一种代表性的社会选择框架，通过有限的个体-问题样本进行社会选择决策，将代表性社会选择中的一些核心问题转化为统计学习问题，利用机器学习理论证明了社会选择机制的泛化特性。进一步提出了代表性的社会选择公理，并利用新的组合分析工具证明了类似阿罗的不可能定理。该框架将社会选择、学习理论和AI对齐结合起来，开启了一系列新的研究方向。
### Conclusion
通过代表性的社会选择框架，研究者将社会选择、学习理论和AI对齐之间的联系直接联系起来，拓宽了理论边界，并提供了新的方法论以应对大规模集体决策中的复杂性。
## 329. `cs.CL` - 训练一个普遍好奇的代理 [PDF](https://arxiv.org/pdf/2502.17543), [HTML](https://arxiv.org/abs/2502.17543)
### Authors
Fahim Tajwar,Yiding Jiang,Abitha Thankaraj,Sumaita Sadia Rahman,J Zico Kolter,Jeff Schneider,Ruslan Salakhutdinov
### Background
智能系统与环境互动时，有效的探索是必不可少的，但现有的语言模型在需要战略信息收集的场景中表现不足。Paprika是一种微调方法，使语言模型能够培养出不受特定环境限制的通用决策能力。通过在需要不同策略的合成互动数据上进行训练，Paprika教会模型在新任务中根据环境反馈来探索并调整其行为，而无需更多梯度更新。实验结果显示，使用Paprika微调的语言模型可以有效地将已学的决策能力应用于完全未见过的任务，而无需额外训练。与传统的训练方法相比，我们方法的主要瓶颈在于寻找有用的互动数据而不是模型更新.
### Innovation
Paprika通过合成互动数据的训练，使语言模型能够学习在新任务中根据环境反馈自我探索和调整行为的能力，而无需额外的梯度更新。此外，作者提出了一种基于课程学习策略来优先选择高学习潜力任务的轨迹采样策略，以提高样本效率。该方法旨在训练一个普遍好奇的代理，帮助AI系统解决需要与外部世界交互的新型序列决策问题.
### Conclusion
研究表明，Paprika方法为AI系统自主解决需要与外部世界互动的新型序列决策问题提供了有前途的途径。
## 330. `cs.CL` - 强化学习与知识蒸馏：理解大型语言模型推理中的准确性和能力 [PDF](https://arxiv.org/pdf/2505.14216), [HTML](https://arxiv.org/abs/2505.14216)
### Authors
Minwu Kim,Anubhav Shrestha,Safal Shrestha,Aadim Nepal,Keith Ross
### Background
近期研究显示，基于可验证奖励的强化学习（Reinforcement Learning with Verifiable Rewards，RLVR）能够提升整体准确性（pass@1），但往往无法改善逻辑推理任务中的能力（pass@k）；而知识蒸馏可以同时改善这两方面。本文旨在探讨这两种方法背后的原因。研究表明，RLVR在提高易题准确性的同时间接降低了难题的准确度。此外，RLVR还能生成高质量的回应，但这并不会让这些回应显著变长或包含更多内省关键词，表明需要更可靠的回应质量指标。进一步的实验发现，知识蒸馏并不总是能改进能力。这可能是因为仅通过蒸馏推理模式只能提升准确率，而不会引入新知识，从而牺牲难题上的性能。
### Innovation
本文通过实验证实并详细说明了RLVR的效果，展示了其在提高易题准确率的同时降低了难题的准确度；并通过知识蒸馏的实验结果推断，仅有蒸馏推理模式只能提升准确率，而不会真正提升能力。这项研究为进一步理解LLMs的推理行为提出了新的见解，强调了可靠指标的重要性。
### Conclusion
本文的研究结果表明，RLVR和知识蒸馏对LLMs推理能力的影响机制不同，RLVR主要通过牺牲难题的准确度来提升整体准确性，而知识蒸馏只能提高准确率而无法真正提升能力。这些发现为理解并改进LLMs的推理行为提供了新的视角。
## 331. `cs.CL` - R$^2$ec: 含有推理能力的大规模推荐模型 [PDF](https://arxiv.org/pdf/2505.16994), [HTML](https://arxiv.org/abs/2505.16994)
### Authors
Runyang You,Yongqi Li,Xinyu Lin,Xin Zhang,Wenjie Wang,Wenjie Li,Liqiang Nie
### Background
大型推荐模型已经通过编码或项目生成将LLM扩展为强大的推荐器。最近在LLM推理方面的突破促使推荐领域探索推理。因此，本文探讨了在推荐模型中嵌入推理能力的方法，以改善推荐效果并减少推理延迟。
### Innovation
本文提出了R$^2$ec，一种具有内在推理能力的统一推荐模型，引入了一种双头架构，支持推理链生成和高效的物品预测，同时设计了一个名为RecPO的强化学习框架，该框架使用新颖的融合奖励机制联合优化推理和推荐。研究结果表明R$^2$ec在多个数据集上优于传统、基于LLM和增强推理的推荐基线，并且在广泛推荐场景下的效率和适应性都很强。
### Conclusion
通过R$^2$ec，本文在推荐领域实现了推理能力，实验结果证明了其优于现有解决方案的效果和效率，并展示了对不同推荐场景的良好适应性。
## 332. `cs.CL` - RADAR：评估语言模型在不完美表格数据上的表现 [PDF](https://arxiv.org/pdf/2506.08249), [HTML](https://arxiv.org/abs/2506.08249)
### Authors
Ken Gu,Zhihan Zhang,Kate Lin,Yuwei Zhang,Akshay Paruchuri,Hong Yu,Mehran Kazemi,Kumar Ayush,A. Ali Heydari,Maxwell A. Xu,Girish Narayanswamy,Yun Liu,Ming-Zher Poh,Yuzhe Yang,Mark Malhotra,Shwetak Patel,Hamid Palangi,Xuhai Xu,Daniel McDuff,Tim Althoff,Xin Liu
### Background
语言模型越来越多地应用于自主数据分析，然而它们的数据意识——识别、推理和适当处理数据缺陷（如缺失值、异常值和逻辑不一致）的能力——尚未得到充分探索。这些缺陷在实际表结构数据中很常见，如果处理不当，会严重影响分析结论的有效性。RADAR 被设计用来系统地评估表格数据中的数据意识推理，通过编程方式模拟数据缺陷，以针对评估模型的行为。
### Innovation
RADAR 提出了一个框架来模拟数据缺陷，使其能够对模型在表格数据中的表现进行针对性评估。RADAR 包含 2980 个表格查询对，涵盖了 9 个领域和 5 种数据缺陷类型的真实数据，并且可以变化表格大小以系统地研究推理性能在表格大小增加时的表现。评估结果表明，尽管在没有数据缺陷的表格上表现良好，但最新的前沿模型在引入数据缺陷时性能显著下降，暴露了其在数据驱动分析中缺乏稳健性和数据意识的问题。RADAR 设计灵活且可扩展，支持不同类型的数据缺陷和可控制的表格大小，为其提供了有价值的发展资源。
### Conclusion
RADAR 为评估语言模型在不完美表格数据上的表现提供了一个系统的方法和基准。尽管现有的前沿模型在没有数据缺陷时表现良好，但在引入数据缺陷时性能显著下降，说明了它们在数据意识分析中存在关键的稳健性差距。RADAR 的设计灵活性使其可以扩展以适应不同的数据缺陷和表格大小，成为推动表格数据推理发展的重要资源。
## 333. `cs.CL` - NaviAgent: 基于工具导航图的两层规划在大规模编排中的应用 [PDF](https://arxiv.org/pdf/2506.19500), [HTML](https://arxiv.org/abs/2506.19500)
### Authors
Yan Jiang,Hao Zhou,LiZhong GU,Ai Han,TianLong Li
### Background
大语言模型（LLMs）最近展示了通过调用外部工具充当功能调用代理的能力，使其能够解决超出其静态知识的任务。然而，现有的代理通常一次只调用一个工具，缺乏对任务结构的全局视角。由于工具之间相互依赖，这导致了错误累积和可扩展性有限的问题，尤其是在扩展到数千个工具时更为明显。
### Innovation
我们提出了一种新颖的两层架构，NaviAgent，通过基于图的工具生态系统建模将任务规划与工具执行分离。在任务规划层面，基于LLM的代理决定直接回应、澄清用户意图、调用工具链或执行工具输出，确保独立于工具间复杂度的主要交互场景得到广泛覆盖。在执行层面，一个不断进化的工具世界导航模型（TWNM）编码了工具间的结构和行为关系，指导代理生成可扩展和稳健的调用序列。通过从实际工具交互中获取反馈，NaviAgent支持规划和执行的闭环优化，从中仅工具调用走向大规模工具生态系统的自适应导航。
### Conclusion
实验结果表明，NaviAgent在所有模型和任务上的任务成功率最高，集成TWNM在复杂任务上的性能提升高达17分，突显了其在工具链编排中的关键作用。
## 334. `cs.CL` - HiRA: 一种分层推理框架，用于深度搜索中的解耦规划和执行 [PDF](https://arxiv.org/pdf/2507.02652), [HTML](https://arxiv.org/abs/2507.02652)
### Authors
Jiajie Jin,Xiaoxi Li,Guanting Dong,Yuyao Zhang,Yutao Zhu,Yang Zhao,Hongjin Qian,Zhicheng Dou
### Background
在实际搜索场景中，复杂的检索需求需要在多种来源中进行深层次的推理和知识综合，而传统检索增强生成（RAG）管道在解决这些问题时表现出色。现有的基于推理的方法存在一个根本性的局限性：它们使用单一模型来同时处理高层次规划和详细执行，导致推理效率低下且可扩展性有限。
### Innovation
我们提出了一种分层框架HiRA，该框架将战略规划与特殊执行分离。该方法将复杂的搜索任务分解为特定领域中的子任务，并为每个子任务分配专用执行代理，这些代理配备了外部工具和推理能力。通过结构化整合机制协调结果。这种分离可以防止执行细节干扰高层次推理，同时让系统能够利用不同类型的专门化专业知识来处理不同类型的信息处理任务。
### Conclusion
我们在四个复杂的、跨模式的深度搜索基准测试中对HiRA进行了实验，结果显示HiRA显著优于最先进的RAG和基于代理系统。我们的结果表明，解耦规划和执行在多步信息检索任务中具有提高答案质量和系统效率的有效性。我们的代码可在以下网址获取：this https URL。
## 335. `cs.CL` - 基于深度学习的临床试验入组预测及其不确定性估计 [PDF](https://arxiv.org/pdf/2507.23607), [HTML](https://arxiv.org/abs/2507.23607)
### Authors
Tien Huu Do,Antoine Masquelier,Nae Eoun Lee,Jonathan Crowther
### Background
临床试验是一种系统性的努力，用于评估新药或治疗方法的安全性和有效性。这类试验通常需要大量的财务投入和细致的规划，这意味着准确预测试验结果变得至关重要。临床试验规划阶段的一个主要挑战是准确预测患者入组情况，这对于试验的成功至关重要。本文提出了一种基于深度学习的新方法，以应对这一关键挑战。该方法被实施为神经网络模型，并利用预训练的语言模型（PLMs）捕捉临床文档的复杂性和细微之处，将其转化为可表达的表示。这些表示随后通过注意机制与编码表格式特征结合。为了应对入组预测中的不确定性，我们通过基于Gamma分布的概率层增强了模型，从而实现范围估计。我们假设各个站点的入组遵循Poisson-Gamma过程，应用提出的方法对临床试验时长进行了预测。在实际临床试验数据上进行了大量实验，结果显示提出的模型可以有效预测给定临床试验中各个站点的入组患者数量，优于已有的基准模型。
### Innovation
本文提出了一种基于深度学习的新方法，利用预训练的语言模型捕捉临床文档的复杂性，通过注意机制与编码表格式特征结合，并通过基于Gamma分布的概率层增强模型以处理不确定性。该方法能够有效预测临床试验中各站点的患者入组数量，优于现有模型。
### Conclusion
在实际临床试验数据上进行了大量实验，结果显示本文提出的基于深度学习的方法在预测患者入组数量方面优于现有模型，能够准确考虑不确定性，并有效地应用于临床试验过程的规划和优化。
## 336. `cs.CL` - 超越像素：探索用于基于LLM的Web代理的DOM降采样 [PDF](https://arxiv.org/pdf/2508.04412), [HTML](https://arxiv.org/abs/2508.04412)
### Authors
Thassilo M. Schiepanski,Nicholas Piël
### Background
前端大语言模型（LLM）最近才使自主网络代理成为可能。这些模型充当即时领域模型后端。在需要建议互动时，与基于Web的任务和相应应用状态进行咨询。主要难题在于应用状态序列化，称为快照。最先进的网络代理是以地面用户界面（UI）快照为基础，即带有视觉线索的屏幕截图。这不仅为了模仿人类感知，而且因为图像是相对廉价的模型输入方式。LLM的视觉能力尚未跟上代码解释能力。文档对象模型（DOM）快照具有结构上类似于HTML的特点，提供了另一种备选方案。然而，巨大的模型输入标记大小至今为止使得可靠的实施具有挑战性。
### Innovation
提出了D2Snap，这是一种前所未有的DOM降采样算法，基于GPT-4o后端。通过对来自Online-Mind2Web数据集的任务进行评估，D2Snap-downsampled DOM快照的成功率（67%）与地面用户界面快照基线（65%）相当，输入标记数量级相同（1e3）。我们最佳的评估配置超出基线8%，达到了95%的成功率。此外，评估表明，DOM固有的层次结构对大语言模型构成了强大的UI功能。
### Conclusion
D2Snap不仅能在同等输入标记数量级上达到与地面用户界面快照相当的成功率，还在更少的输入标记下显示出更好的性能。这表明DOM层次结构对大语言模型构成了重要的UI特征，为进一步改进基于LLM的Web代理提供了新的可能性。
## 337. `cs.CL` - Mano 技术报告 [PDF](https://arxiv.org/pdf/2509.17336), [HTML](https://arxiv.org/abs/2509.17336)
### Authors
Tianyu Fu,Anyang Su,Chenxu Zhao,Hanning Wang,Minghui Wu,Zhe Yu,Fei Hu,Mingjia Shi,Wei Dong,Jiayao Wang,Yuyang Chen,Ruiyang Yu,Siran Peng,Menglin Li,Nan Huang,Haitian Wei,Jiawei Yu,Yi Xin,Xilin Zhao,Kai Gu,Ping Jiang,Sifan Zhou,Shuo Wang
### Background
图形用户界面（GUI）是人机交互的主要媒介，但自动化GUI交互因其复杂视觉元素、动态环境及多步骤推理需求而颇具挑战。现有的基于视觉语言模型（VLMs）的方法往往受限于低分辨率、领域不匹配和不足的序列决策能力。
### Innovation
我们提出了Mano，一个基于广泛网页和计算机系统数据预训练的多模态基础模型构建的鲁棒GUI代理。该方法结合了一个高保真度数据生成的新型模拟环境、三阶段训练管道（监督微调、离线强化学习和在线强化学习）以及一个用于错误恢复的验证模块。Mano在多个GUI基准测试中（如Mind2Web和OSWorld）表现出最先进的性能，并在成功率和操作准确性方面取得重大改进。
### Conclusion
我们的工作提供了强化学习与VLM的有效集成的新见解，特别是在实际GUI代理部署中的重要性。强调了特定领域数据、迭代训练和全面奖励设计的作用。
## 338. `cs.CL` - 通过强化学习探索提高大语言模型的推理能力 [PDF](https://arxiv.org/pdf/2510.03865), [HTML](https://arxiv.org/abs/2510.03865)
### Authors
Wenhao Deng,Long Wei,Chenglei Yu,Tailin Wu
### Background
最近，强化学习中的验证性奖励（RLVR）提高了大语言模型（LLMs）的推理能力，特别是对于数学问题的解决。然而，随着采样预算的增加，RLVR训练的模型相对于其预训练基础模型的优势往往会减弱或消失，显示出对基础模型限制搜索空间的强烈依赖。
### Innovation
本文提出了RAPO（奖励感知策略优化），一种促进更广泛且聚焦的探索的算法。RAPO采用正向KL惩罚来替代反向KL惩罚进行离分布的探索，并重权重参考策略以促进适应性在分布的探索。实验表明，使用RAPO训练的Qwen2.5-3B和7B模型在8K SimpleRL-Zero数据集上表现出增强的问题解决性能，并且能够克服基础模型的性能限制，解决之前难以解决的问题。
### Conclusion
RAPO算法在不同场景下的应用证明了其在提升LLMs解决难题方面的有效性，推动了RLVR在复杂推理任务中的前沿发展。
## 339. `cs.CL` - 大型语言模型中的规范性推理：从逻辑和模态视角的对比基准 [PDF](https://arxiv.org/pdf/2510.26606), [HTML](https://arxiv.org/abs/2510.26606)
### Authors
Kentaro Ozeki,Risako Ando,Takanobu Morishita,Hirohiko Abe,Koji Mineshima,Mitsuhiro Okada
### Background
规范性推理涉及规范或义务模态，如义务和许可。尽管大型语言模型（LLMs）在各种类型的推理任务中表现出色，但它们处理规范性推理的能力尚未得到充分探索。为了评估LLMs在规范性推理中的推理能力，本文从逻辑和模态两个角度系统地评估了LLMs在规范性领域的推理能力，通过将规范性模态的推理与存在相同形式结构的知识模态的推理进行比较来测试LLMs如何处理规范性模态的推理能力。研究人员还引入了一个新的数据集，涵盖了规范性领域和知识领域的广泛形式推理模式，同时考虑了影响人类推理的非形式认知因素。实验结果显示，尽管LLMs通常遵循有效的推理模式，但在某些类型的规范性推理中表现出明显的不一致，并且表现出类似于人类推理心理学研究中观察到的认知偏差。这些发现突显了在LLMs规范性推理中实现逻辑一致性的挑战，并为提高其可靠性提供了见解。
### Innovation
该研究创新性地将规范性模态推理与知识模态推理进行对比评估，引入了一个结合形式和非形式因素的新数据集，揭示了LLMs在特定类型规范性推理中的不一致性及其认知偏差，提供了增强其规范性推理可靠性的见解。
### Conclusion
尽管LLMs通常遵循有效的规范性推理模式，但在特定类型规范性推理中表现出明显不一致，并表现出类似人类推理的心理学研究中的认知偏差。这些发现突显了在LLMs规范性推理中实现逻辑一致性的挑战，并为提高其可靠性提供了见解。所有的数据和代码公开发布。
## 340. `cs.CV` - DC4GS: Directional Consistency-Driven Adaptive Density Control for 3D Gaussian Splatting [PDF](https://arxiv.org/pdf/2510.26921), [HTML](https://arxiv.org/abs/2510.26921)
### Authors
Moonsoo Jeong,Dongbeen Kim,Minseong Kim,Sungkil Lee
### Background
该论文背景是3D Gaussian Splatting在表示3D模型时需要控制密度，传统的方法通常是基于位置梯度的大小来决定分裂的基本单元，但这种方法在处理局部结构复杂性时可能会导致冗余的分裂。因此，本文提出了一个名为DC4GS的新方法，通过整合梯度的方向一致性来优化分裂过程，从而提高重建的准确性并减少基本单元的数量。
### Innovation
本文方法的主要创新点在于提出了一个基于方向一致性的自适应密度控制（DC-ADC）策略，具体而言，它首先通过方向一致性改进了传统的自适应密度控制方法（ADC），使得能够更好地捕捉局部结构的复杂性，减少冗余分裂；其次，在分裂时利用方向一致性来确定最优的分裂位置，使子基本单元更精确地对齐局部结构。
### Conclusion
实验结果表明，与现有方法相比，DC4GS方法能够显著减少基本单元的数量（实验中最多可减少30%），同时大大提高重建的真实性。
## 341. `cs.CV` - PF-DAformer: 双中心QCT的域自适应变压器进行近端股骨分割 [PDF](https://arxiv.org/pdf/2510.26903), [HTML](https://arxiv.org/abs/2510.26903)
### Authors
Rochak Dhakal,Chen Zhao,Zixin Shi,Joyce H. Keyak,Tadashi S. Kaneko,Kuan-Jui Su,Hui Shen,Hong-Wen Deng,Weihua Zhou
### Background
定量CT（QCT）在评估骨强度和骨折风险方面发挥着关键作用，通过分析近端股骨中骨密度的体积分布。然而，实际应用自动化分割模型仍然具有挑战性，因为不同数据集训练的深层网络在应用于其他数据集时往往会失败，这种失败源自于域偏移，具体表现为扫描器、重建设置和患者人口统计学的差异，导致预测不稳定，量化指标不可靠。克服这一障碍对于多中心骨质疏松症研究以及确保放射组学和结构 finite 元分析结果在不同地点的可重复性至关重要。
### Innovation
本文开发了一种针对多机构QCT的域自适应变压器分割框架。模型在迄今为止最大规模的髋部骨折相关的研究队列中进行了训练和验证，包含1,024张来自杜兰大学的QCT图像扫描和来自明尼苏达州罗切斯特市的384张扫描。为解决域偏移问题，采用3D TransUNet骨干网络内的两种互补策略：通过梯度反转层实现对抗对齐，从而抑制网络学习机构特定线索；以及通过最大均值偏差（MMD）实现统计对齐，明确减少机构之间的分布差异。这种双重机制在保持解剖细节的同时促进了扫描器无关特征的学习。
### Conclusion
该模型通过结合对抗对齐和统计对齐策略，实现了机构无关的关键特征学习，同时保留了解剖细节，提高了多机构QCT中的近端股骨分割的稳定性和准确性。
## 342. `cs.CV` - 数据感知 Curriculum 学习在 YOLOv11 软件稀疏肺结节检测中的应用 [PDF](https://arxiv.org/pdf/2510.26923), [HTML](https://arxiv.org/abs/2510.26923)
### Authors
Yi Luo,Yike Guo,Hamed Hooshangnejad,Kai Ding
### Background
肺部结节检测在胸部CT中的早期肺癌诊断中至关重要。然而，现有的深度学习方法在临床有限标注数据的环境中部署时遇到了挑战。虽然已经证明了 Curriculum 学习在提升模型训练效果上的潜力，但传统的静态 Curriculum 策略在数据匮乏的情况下效果不佳。
### Innovation
我们提出了一种新颖的训练策略 —— Scale Adaptive Curriculum Learning (SACL)，根据可用数据规模动态调整 Curriculum 设计。SACL 引入了三种机制：(1) 自适应 epoch 调度，(2) 难例注入，(3) 规模感知优化。我们使用 YOLOv11 作为基础检测器在 LUNA25 数据集上进行评估。实验结果显示，SACL 在 mAP50 与静态 Curriculum 学习的全数据集性能相当，在有限的数据条件下表现出显著的优势，在训练数据的 10%、20% 和 50% 分别提高了 4.6%、3.5% 和 2.0% 的性能。SACL 在不改变架构的情况下提供了在不同数据规模下进行稳健训练的解决方案，为医疗机构在有限标注资源下开发有效的肺结节检测系统提供了实用的解决方案。
### Conclusion
Scale Adaptive Curriculum Learning (SACL) 提供了一种实用的解决方案，可以在有限的标注数据资源下，实现不同数据规模下的稳健训练，对于开发有效的肺结节检测系统具有重要的意义。
## 343. `cs.CV` - 视觉-语言模型在视觉测量读取方面表现如何？MeasureBench基准测试 [PDF](https://arxiv.org/pdf/2510.26865), [HTML](https://arxiv.org/abs/2510.26865)
### Authors
Fenfen Lin,Yesheng Liu,Haiyu Xu,Chen Yue,Zheqi He,Mingxuan Zhao,Miguel Hu Chen,Jiakang Liu,JG Yao,Xi Yang
### Background
针对视觉-语言模型(VLMs)在读取测量仪器指示上的能力进行了初步评估，发现即使是最先进的VLMs在一般测量读取方面仍然表现不佳。这种任务对人类来说非常简单，但对当前的VLMs却具有挑战性。本文旨在通过介绍MeasureBench基准测试，涵盖各种类型的现实世界和合成图像中的测量读取，来解决这个问题。MeasureBench的合成管道可以根据需求生成具有可控视觉外观的特定类型的仪表盘，从而实现关键细节（如指针、刻度、字体、照明、杂乱）的大规模变化。评估结果指出，即使是领先的VLMs在一般测量读取方面也存在困难，尤其是在指针位置和对齐方面的指示器定位一致性失败。进一步的实验表明，对于现实世界的图像，强化学习在合成数据集上取得了一些令人鼓舞的结果，但对现实世界图像的表现则不太令人满意。这反映了当前VLMs在精细的空间定位上的基本局限性。
### Innovation
本文通过创建MeasureBench基准测试，为视觉-语言模型提供了一个测量读取的综合评估平台。这个基准测试涵盖多种真实和合成图像，并包含一个扩展的数据合成管道，该管道以程序化方式生成特定类型的测得仪，控制视觉外观的关键细节（如指针、刻度、字体、照明和杂乱）。除此之外，作者还使用强化学习进行了实验，发现对于合成数据集取得了一些有意义的结果，但在现实世界图像上的表现则不太理想。该研究揭示了当前VLMs在细粒度的空间定位方面的基本局限性，希望MeasureBench能够促进未来在视觉接地数值能力和精确的空间感知方面的发展，将识别数字与衡量世界的能力相结合，填补差距。
### Conclusion
视觉-语言模型在读取测量读取方面的表现令人失望，目前最先进的模型甚至在一般性和特定的测量读取操作方面也面临困难。特别是，在细粒度空间定位方面存在明显限制，如指示器定位。文章提出了MeasureBench作为基准测试，以促进未来在视觉接地数值和精确空间感知方面的进展。MeasureBench提供了一个平台，可以帮助在识别数字和衡量世界之间建立连接，利用合成数据进行初步实验得到了一些初步结果，但仍需要进一步的研究来解决实际世界的复杂性。
## 344. `cs.CV` - SYNAPSE-Net: 一种具备病变感知分层门控机制的统一框架，用于稳健分割异质性脑病变 [PDF](https://arxiv.org/pdf/2510.26961), [HTML](https://arxiv.org/abs/2510.26961)
### Authors
Md. Mehedi Hassan,Shafqat Alam,Shahriar Ahmed Seam,Maruf Ahmed
### Background
在临床神经影像学中，利用多模态MRI自动分割异质性脑病变仍然是一个关键性的挑战。目前的深度学习模型通常缺乏通用性和高性能的稳定性，限制了其在临床中的可靠性。
### Innovation
本文提出了统一路由多流SYNAPSE-Net，这是一种适应性框架，旨在提高通用性和稳健性。该架构集成了多流CNN编码器、基于Swin变换器的全局上下文、动态跨模态注意力融合机制(CMAF)以及分级门控解码器，用于高保真掩码重建。通过结合病理特异性数据增强和难度感知采样策略进行训练，以减少性能波动。实验结果表明该框架在多个脑病理学测试集中达到了最先进的性能，提供了一种稳健且临床可行的自动分割方案。
### Conclusion
本文提出了一个统一的适应性框架SYNAPSE-Net，该框架通过采用多层次门控机制提高了分割异质性脑病变的性能，并展示了在不同脑病变数据集上的优越表现，为临床实践提供了一种可靠的自动分割解决方案。
## 345. `cs.CL` - 通过情境学习检测语言模型中的数据污染 [PDF](https://arxiv.org/pdf/2510.27055), [HTML](https://arxiv.org/abs/2510.27055)
### Authors
Michał Zawalski,Meriem Boubdir,Klaudia Bałazy,Besmira Nushi,Pablo Ribalta
### Background
本文介绍了Contamination Detection via Context (CoDeC)，这是一种实用且精确的方法，用于检测和量化大型语言模型中的训练数据污染。CoDeC 通过测量上下文学习如何影响模型性能来区别在训练过程中记住了的数据和在训练分布之外的数据。实验证明，CoDeC 生成可解释的污染评分，能够清晰地区分已见过和未见过的数据集，并揭示了未披露训练语料库的开源权重模型中的强烈记忆证据。该方法简单、自动，适用于模型和数据集，易于集成到基准评估中。
### Innovation
CoDeC 的创新在于通过测量上下文学习如何影响模型性能来区分在训练过程中记住了的数据和未包含在训练分布中的数据，这种方法简单、自动化，对模型和数据集都不挑剔。同时，它能够清晰地揭示数据中的污染情况，并且提供可以解释的污染评分
### Conclusion
通过实验证明，CoDeC 能够生成可解释的污染评分，可以清晰地分离出已见过和未见过的数据集，并揭示了未披露训练语料库的开源权重模型中的强烈记忆证据。使用 CoDeC 可以简化数据污染检测过程，使其易于集成到基准评估中。
## 346. `cs.CL` - Awal — 由社区推动的柏柏尔语语言技术 [PDF](https://arxiv.org/pdf/2510.27407), [HTML](https://arxiv.org/abs/2510.27407)
### Authors
Alp Öktem,Farida Boudichat
### Background
该论文介绍了针对柏柏尔语语言技术资源开发的一项社区驱动的倡议Awal。论文回顾了柏柏尔语计算资源的最新进展，并探讨了社区驱动方法以应对持续的数据稀缺性。文章指出，尽管自2024年以来平台运营良好，但仍存在参与度低的问题，包括书面柏柏尔语的信心不足和持续的标准制定挑战。贡献者主要为语言学家和活动者，社区贡献规模相对较小，包括6,421对翻译和3小时的语音数据，这揭示了在复杂社会语言背景下应用标准众包方法的局限性。
### Innovation
该创新在于推出了一个由社区推动的平台Awal，旨在提升柏柏尔语在数字空间中的存在，通过协作平台鼓励柏柏尔语使用者贡献翻译和语音数据。该平台结合了用户生成的内容，同时使用收集的数据改进开源机器翻译模型。
### Conclusion
尽管 Awal 获得了广泛赞誉，但实际的数据贡献仍然集中在语言学家和活动者身上，社区贡献的规模较小。作者认为，需要解决的文化和语言认同问题仍然存在挑战，同时计划进一步改进开源机器翻译模型，以更好地适应柏柏尔语的独特需求。
## 347. `cs.CL` - TransAlign：机器翻译编码器同样也是强大的单词对齐器 [PDF](https://arxiv.org/pdf/2510.27337), [HTML](https://arxiv.org/abs/2510.27337)
### Authors
Benedikt Ebing,Christian Goldschmied,Goran Glavaš
### Background
由于大多数世界语言和NLP任务缺乏大量训练数据，基于翻译的策略，如‘翻译测试’（翻译目标语言数据为杂音源语言数据进行评价）和‘翻译训练’（利用杂音目标语言数据进行训练），已成为跨语言迁移（XLT）的竞争性方法。这些策略通常要求标签投影：将原始句子中的每个词性标签映射到翻译中的对应词性标签。传统的解决方案通常是使用从如mBERT或LaBSE等编码语言模型衍生的多语言词对齐器（WAs）。尽管机器翻译（MT）和WAs之间有明显关联，但利用MT模型提取对齐的研究大多集中在利用编码解码器架构中的跨注意力机制上，导致WAs性能不佳。
### Innovation
该工作提出了一种名为TransAlign的新颖单词对齐方法，利用大规模多语言机器翻译模型的编码器。TransAlign不仅实现了强大的WAs性能，还在基于机器翻译的跨语言迁移（XLT）中显著优于流行的WAs和最先进的无WAs基标签投影方法，特别是在词性分类任务中表现突出。
### Conclusion
TransAlign通过利用大规模多语言机器翻译模型的编码器部分，展示出在大规模多语言翻译任务中的卓越对齐性能。其对WAs性能的改进表明了利用机器翻译模型内部知识对于跨语言迁移学习的重要性。
## 348. `cs.CL` - 基于对比偏好优化的数据高效领域适应mt [PDF](https://arxiv.org/pdf/2510.27556), [HTML](https://arxiv.org/abs/2510.27556)
### Authors
Inacio Vieira,Antonio Castaldo,James O'Doherty,Sheila Castilho
### Background
大型语言模型（LLMs）通常需要适应特定领域的具体需求，但这种过程如果完全依赖于模型精细调优（SFT）将会非常昂贵。本文通过实验研究了如何利用对比偏好优化（CPO）来模拟后编辑流程，从而实现高效的数据驱动领域适应，特别是在机器翻译（MT）场景中。这种方法可以通过生成偏好匹配对，利用基模型的直接输出作为“被拒绝”的翻译，以及人类批准的翻译记忆条目作为“被选择”的翻译，来直接反馈模型的当前知识状态，从而引导模型与特定领域标准对齐。
### Innovation
本文的创新之处在于提出了一种新的方法——对比偏好优化（CPO），通过模拟人类后编辑流程来引导模型更好地适应特定领域，仅需较少的数据就取得了接近于通过大量样本精细调优的模型的表现，显著提高了数据效率。这种方法不仅在机器翻译中有效，还能够在其他生成任务中泛化应用，这些任务中模型的初始草稿可以作为对照信号与基准参考进行对比。
### Conclusion
实验结果表明，在英-巴西葡萄牙语和英-韩语场景中，仅使用14700个偏好匹配对，模型就能达到与SFT训练160000多个样本模型相媲美的性能，显示出显著的数据效率提升。虽然本文着重于MT的应用场景，但CPO方法可以自然地推广到其他领域，其中模型的初始草稿可以用作对照信号与黄金标准进行对比。
## 349. `cs.CL` - MedCalc-Eval和MedCalc-Env：提升大型语言模型的医学计算能力 [PDF](https://arxiv.org/pdf/2510.27267), [HTML](https://arxiv.org/abs/2510.27267)
### Authors
Kangkun Mao,Jinru Ding,Jiayuan Chen,Mouxiao Bian,Ruiyao Chen,Xinwei Peng,Sijie Ren,Linyang Li,Jie Xu
### Background
现有的医疗领域大型语言模型（LLMs）基准大多集中在问题回答和描述性推理方面，忽视了对临床决策至关重要的定量推理能力。现有的数据集如MedCalc-Bench涵盖的计算任务较少，无法反映真实的计算场景。为了填补这一空白，本文引入了MedCalc-Eval，这是一个评估LLMs医学计算能力的最大基准，包括700多个涵盖方程式基础（如Cockcroft-Gault、BMI、BSA）和基于规则的评分系统（如Apgar、Glasgow昏迷量表）的任务，覆盖内科学、外科、儿科和心脏病学等多个专科，提供了一个更广泛且更具挑战性的评估环境。
### Innovation
本文提出了MedCalc-Eval，这是目前最大的评估LLM医学计算能力的基准，包括700多个涵盖了方程式基础和基于规则的评分系统计算任务。此外，开发了一种名为MedCalc-Env的增强学习环境，基于InternBootcamp架构，支持多步骤的临床推理和规划。通过在该环境中微调Qwen2.5-32B模型，实现了在MedCalc-Eval上的最新成果，特别在数值敏感性、公式选择和推理稳健性方面取得显著进步。
### Conclusion
尽管在多个方面取得了显著进步，但仍然存在单位转换、多条件逻辑、上下文理解等方面的挑战。代码和数据集可以在相关链接下载。
## 350. `cs.CV` - MoME: Mixture of Visual Language Medical Experts for Medical Imaging Segmentation [PDF](https://arxiv.org/pdf/2510.26996), [HTML](https://arxiv.org/abs/2510.26996)
### Authors
Arghavan Rezvani,Xiangyi Yan,Anthony T. Wu,Kun Han,Pooya Khosravi,Xiaohui Xie
### Background
本研究背景集中在医学图像分割任务中，现有的模型通常难以充分利用医学图像的复杂性和多尺度视觉特征。通过利用大规模语言模型中的混合专家（MoE）架构，本文探索了将视觉-语言模型集成到医学图像分割中的新方法，以实现更准确和鲁棒的结果。
### Innovation
本文创新性地提出了MoME（Mixture of Visual Language Medical Experts），这是一种新的混合专家架构，能够在医学视觉-语言任务中动态选择专家，并有效利用多尺度视觉特征和文本嵌入。这项工作利用了10个数据集，涵盖了3,410份CT扫描，展示了在医学成像分割基准上的强劲表现，并且显示出利用基础模型实现医学图像分析的新架构。
### Conclusion
MoME 模型通过将视觉-语言模型结合到医学成像领域中，展示了在不同数据集上具有竞争力的精确度，并探索了一种新型的架构，用于实现医学图像分析中的稳健结果。它受益于MoE架构在提升模型性能方面的有效性，尤其是在引入文本信息方面。
## 351. `cs.CV` - 基于语义帧聚合的变换器模型用于实时视频评论生成 [PDF](https://arxiv.org/pdf/2510.26978), [HTML](https://arxiv.org/abs/2510.26978)
### Authors
Anam Fatima,Yi Yu,Janak Kapuriya,Julien Lalanne,Jainendra Shukla
### Background
实时视频流上的互动直播平台，如Twitch，通过动态交互增强观众多方面的参与度。然而，自动生成与当前互动相关的内容合适的评论仍然是一项具有挑战性的任务。现有方法倾向于忽视对视频帧优先级的关注，这些帧与当前观众的互动最为相关。这种优先级选择对于生成上下文合适的评论至关重要。鉴于此，本研究介绍了一种基于语义帧聚合的变换器模型（SFAT），该模型利用CLIP的跨模态知识生成评论，并根据视频帧与其当前观众对话的语义相关性分配权重。模型采用了一种有效的加权视频帧汇总技术来突出显示信息丰富的帧，同时较少关注无关帧。此外，为了应对现有数据集的限制，这些数据集主要侧重于中文内容且视频类别有限，本研究构建了一个大规模、多模态的英语视频评论数据集。该数据集源自Twitch，覆盖了11个视频类别，总计438小时和320万条评论。研究表明，SFAT模型生成的评论与现有的方法相比更为有效，特别是在从实时视频和持续对话上下文生成评论方面。
### Innovation
本研究提出了一种基于语义帧聚合的变换器模型（SFAT），能够根据视频帧与其当前观众对话的语义相关性分配权重，从而突出显示信息丰富的帧并生成与当前互动相关的内容。此外，研究还构建了一个多样化的多模态英语视频评论数据集，旨在解决现有数据集内容有限的问题。
### Conclusion
研究提出的基于语义帧聚合的变换器模型（SFAT）在实时视频评论生成方面显示出比现有方法更佳的效果。此外，通过构建一个大规模、多模态的英语视频评论数据集，研究也克服了现有数据集的限制。
## 352. `cs.CV` - 在不变关系表示学习下的逐步人-物体交互检测 [PDF](https://arxiv.org/pdf/2510.27020), [HTML](https://arxiv.org/abs/2510.27020)
### Authors
Yana Wei,Zeen Chi,Chongyu Wang,Yu Wu,Shipeng Yan,Yongfei Liu,Xuming He
### Background
在开放世界环境中，人-物体交互（HOIs）会持续演变，这给传统的封闭世界HOI检测模型带来了挑战。人类能够逐步获得知识的能力启发了我们探索逐步HOI检测（IHOID），以开发能够在动态环境中识别人-物体关系的智能体。这一设置不仅需要应对逐步学习中的灾难性遗忘问题，还需要解决交互漂移和零样本HOI组合检测的问题，尤其是这些组合是按顺序到达的。
### Innovation
提出了一种新颖的无样本逐步关系蒸馏（IRD）框架。IRD将物体与关系的学习分离，并引入了两种独特的蒸馏损失，以便在相同的关系下，能够学习不同HOI组合中的不变关系特征。该方法在HICO-DET和V-COCO数据集上的广泛实验表明，与最新的基线方法相比，该方法在减轻遗忘、增强对交互漂移的鲁棒性和零样本HOI泛化方面具有优势。
### Conclusion
该研究通过无样本逐步关系蒸馏框架，在减轻遗忘、增强对抗交互漂移的稳健性和零样本HOI泛化等方面展示了自身的优势。
## 353. `cs.CV` - VitalLens 2.0: 高保真面部视频中的心率变异性估算远程光电容积描记术 [PDF](https://arxiv.org/pdf/2510.27028), [HTML](https://arxiv.org/abs/2510.27028)
### Authors
Philipp V. Rouast
### Background
本文介绍了VitalLens 2.0，这是一种新的深度学习模型，用于从面部视频估计生理信号。前文提到，现有方法在远程光电容积描记术（rPPG）-心率（HR）和呼吸率（RR）的估计方面已经取得了一些进展，但对心率变异度（HRV）的估计还有待提高。本文通过引入新的模型架构和扩大训练数据规模，旨在提升rPPG的准确性，特别是心率变异度的估计精度。
### Innovation
通过使用新的模型架构和扩展训练数据集至1,413个独特个体，VitalLens 2.0在准确估计心率、呼吸率以及心率变异度方面取得了显著进展，平均绝对误差分别为1.57 bpm（心率），1.08 bpm（呼吸率），10.18 ms（HRV-SDNN），16.45 ms（HRV-RMSSD）。这些结果打破了现有技术的界限，并明显优于先前的方法。
### Conclusion
VitalLens 2.0已应用于由四个公开和私人数据集组成的各自包含422个独特个体的新测试集上，并表现出新的最先进的技术能力。此模型现已通过VitalLens API开放给开发者。
## 354. `cs.CV` - ZEBRA: Towards Zero-Shot Cross-Subject Generalization for Universal Brain Visual Decoding [PDF](https://arxiv.org/pdf/2510.27128), [HTML](https://arxiv.org/abs/2510.27128)
### Authors
Haonan Wang,Jingyu Lu,Hongrui Li,Xiaomeng Li
### Background
近期，神经解码技术取得了进展，能够从脑活动重建视觉体验，使得fMRI到图像的重建成为连接神经科学和计算机视觉之间的有希望的桥梁。然而，当前方法主要是基于特定个体的模型或需要特定个体的微调，限制了它们的规模化和实际应用。
### Innovation
提出了ZEBRA，一种零样本脑视觉解码框架，首次不需要特定个体的适配。ZEBRA的核心洞察是fMRI表示可以分解为与个体相关和语义相关的成分。通过利用对抗训练，我们的方法明确解耦这些成分，以分离出个体不变、语义特异的表示。这种分离使ZEBRA能够在无需额外fMRI数据或重训练的情况下泛化到未见过的个体。广泛的实验表明，ZEBRA在多个指标上显著优于零样本基线，性能与完全微调的模型相当。
### Conclusion
我们的工作代表了大规模和实用的向通用神经解码迈进的一步。代码和模型权重可在以下网址获取：this https URL。
## 355. `cs.CV` - 层级变换器用于无监督3D形状抽象 [PDF](https://arxiv.org/pdf/2510.27088), [HTML](https://arxiv.org/abs/2510.27088)
### Authors
Aditya Vora,Lily Goli,Andrea Tagliasacchi,Hao Zhang
### Background
本文介绍了一种新颖的层次神经场表示方法HiT，用于学习不同形状分类中自粗至细的一般层次结构，且在无监督设置下进行。不同以往的工作对任务施加固定层次结构的限制（例如二进制结构），HiT方法具有灵活性，可以直接从数据中推断出层次结构，超越了之前的复杂层次结构，训练时可捕捉到父节点和子节点之间有意义的包含关系，通过无监督的形状分割任务在所有55个ShapeNet分类中验证了其有效性和优越性
### Innovation
Introduces a hierarchical transformer（HiT）which learns parent-child relationships in a compressed codebook format. This enables the model to automatically identify common substructures across diverse shape categories without being constrained to a fixed hierarchical structure. Additionally, the model captures meaningful containment relationships between parent and child nodes when trained with a reconstruction loss.
### Conclusion
通过无监督的形状分割任务在所有55个ShapeNet分类中展示了模型的有效性，HiT能够成功对形状进行多层次的分割和抽象。
## 356. `cs.CV` - E-MMDiT：在有限资源下重新审视多模态扩散变换器设计以实现快速图像合成 [PDF](https://arxiv.org/pdf/2510.27135), [HTML](https://arxiv.org/abs/2510.27135)
### Authors
Tong Shen,Jingai Yu,Dong Zhou,Dong Li,Emad Barsoum
### Background
扩散模型在从文本提示生成高质量图片方面表现出了强大的能力，但这些模型往往需要大量的训练数据和计算资源，或者由于复杂的结构导致高延迟。
### Innovation
提出的Efficient Multimodal Diffusion Transformer (E-MMDiT)模型具有304M参数，仅需少量训练资源即可实现快速图像合成，采用高效的视觉词元化和多路径压缩模块，增强位置信息，引入交替子区域注意力机制和AdaLN-affine模块，以实现更低的计算成本。
### Conclusion
该模型在512px生成上，仅用25M公共数据在1.5天内于单节点8块AMD MI300X GPU上训练，达到GenEval 0.66，并可使用后训练技术提高到0.72。该工作为未来研究提供了一个强大且实用的基础，并有助于普及生成AI模型。
## 357. `cs.CV` - 改进交叉视角对象地理定位：基于交叉视角交互和多尺度空间特征的双注意力方法 [PDF](https://arxiv.org/pdf/2510.27139), [HTML](https://arxiv.org/abs/2510.27139)
### Authors
Xingtao Ling Yingying Zhu
### Background
交叉视角对象地理定位由于潜在应用逐渐受到关注，现有方法通过注意力机制捕捉不同视角之间查询对象的空域依赖关系，进而获得空域关系特征图并预测对象位置。然而，这些方法在信息跨视角传输和特征图进一步精炼方面存在不足，导致模型错误地关注与查询对象无关的边缘噪声，影响了定位性能。
### Innovation
该研究引入了一种名为Cross-view and Cross-attention Module (CVCAM) 的模块，该模块实现了两种视角之间的多轮交互，从而实现上下文信息的连续交换和学习。同时提出了Multi-head Spatial Attention Module (MHSAM)，利用不同尺寸的卷积核从包含隐式对应关系的特征图中提取多尺度空间特征，增强了查询对象的特征表示。此外，鉴于交叉视角对象地理定位数据集的稀缺性，该研究创建了名为G2D的新数据集，用于“地面到无人机”定位任务，丰富了现有的数据集并填补了“地面到无人机”定位任务的空白。
### Conclusion
在CVOGL和G2D数据集上的广泛实验表明，所提出的方法在定位精度上达到了高水平，超越了当前最先进的方法。
## 358. `cs.CV` - HiGS：多步关联语义空间组成中的分层生成场景框架 [PDF](https://arxiv.org/pdf/2510.27148), [HTML](https://arxiv.org/abs/2510.27148)
### Authors
Jiacheng Hong,Kunzhen Wu,Mingrui Yu,Yichao Gu,Shengze Xue,Shuangjiu Xiao,Deli Dong
### Background
三维场景生成在游戏、电影和虚拟现实领域具有显著潜力。然而，现有大多数方法采用单步生成过程，难以在保持场景复杂度的同时减少用户输入。受人类场景建模过程从全局到局部，关注关键元素并通过语义关联完成场景的启发，提出了一种多步关联语义空间构成的分层级生成框架HiGS。
### Innovation
HiGS是一种分层级生成框架，支持多步关联语义空间构成，通过逐步选择关键语义对象让用户能够迭代地扩展场景，细粒度地控制感兴趣区域的同时，自动完成周围的区域。Introduce PHiSSG，一种渐进式的分层级语义空间图，动态组织生成场景结构中的空间关系和语义依赖性，确保生成过程中的空间和几何一致性，通过保持图节点与生成对象之间的一对一映射，并支持递归布局优化。
### Conclusion
实验表明，HiGS在布局合理性、风格一致性和用户偏好方面优于单阶段方法，提供了一种可控制和可扩展的高效3D场景构建范例。
## 359. `cs.CV` - AD-SAM：为自主驾驶感知优化的分割任何视觉基础模型微调 [PDF](https://arxiv.org/pdf/2510.27047), [HTML](https://arxiv.org/abs/2510.27047)
### Authors
Mario Camarena,Het Patel,Fatemeh Nazari,Evangelos Papalexakis,Mohamadhossein Noruzoliaee,Jia Chen
### Background
本文介绍了自主驾驶段万物模型（AD-SAM），这是一种针对自主驾驶（AD）领域的语义分割微调视觉基础模型。AD-SAM 在 Segment Anything 模型（SAM）的基础上引入了双编码器和变形解码器，以适应道路场景的空间和几何复杂性。该模型通过结合预训练的视觉变换器（ViT-H）的全局语义上下文和可训练卷积深度学习骨干网（如 ResNet-50）的局部空间细节，生成多尺度融合表示。此外，它还使用变形融合模块对跨尺度和物体几何的不同特征进行对齐，并通过变形注意力进行逐阶段的多阶段细化。
### Innovation
AD-SAM 通过结合全局语义上下文和局部空间细节生成多尺度融合表示，并使用变形融合模块对齐不同尺度和物体几何的特征。同时，它采用了逐步多阶段细化和变形注意力，从而提高了语义类别平衡、边界精度和优化稳定性。训练过程中采用了由 Focal、Dice、Lovasz-Softmax 和 Surface 损失构成的混合损失函数，以改善性能。AD-SAM 在 Cityscapes 和 BDD100K 数据集上的语义分割准确性超过了其他模型（SAM、G-SAM 和 DeepLabV3），并展示了跨域泛化的强大能力，其保留得分为 0.87（比 SAM 的高），学习动态更快速、更稳定，且收敛速度快于基准模型。模型仅通过 1000 个样本就能维持 0.607 mIoU，表明其数据效率对于降低注释成本至关重要。这些都说明了针对基础模型进行目标架构和优化改进能够实现自主驾驶领域的可靠感知
### Conclusion
本研究通过引入 AD-SAM 模型，借助目标架构和优化改进增强基础模型的功能，在语义分割精度和泛化能力方面实现了显著提升。该模型在多种道路场景中表现出优异的性能，并且具有较快的学习动态。
## 360. `cs.CV` - WildfireX-SLAM：大规模低空RGB-D数据集及其在野火SLAM和更多应用中的应用 [PDF](https://arxiv.org/pdf/2510.27133), [HTML](https://arxiv.org/abs/2510.27133)
### Authors
Zhicong Sun,Jacqueline Lo,Jinxing Hu
### Background
3D高斯点云（3DGS）及其衍生版本在同步定位与建图（SLAM）方面取得了显著进展。尽管大多数基于3DGS的SLAM工作集中在小规模室内场景中，但对于大规模森林场景的SLAM方法的研究却具有巨大的潜力，尤其是在野火紧急响应和森林管理等领域。然而，由于缺乏全面和高质量的数据集，这种研究受到了阻碍。构建这样的数据集需要在实际场景中进行昂贵且技术上难以实现的采集工作。为此，本文构建了一个大规模、全面且高质量的合成数据集，用于森林野火环境下的SLAM研究。利用Unreal Engine 5 Electric Dreams Environment Sample Project，开发了一套采集空中和地面视角（含真实摄像机姿态和各种数据模态）的管线，并提供灵活的环境因素控制，如光照、天气和野火类型等，以满足各种任务需求，包括森林制图和野火紧急响应等。最终数据集WildfireX-SLAM包含5500张低空RGB-D的高空图像，总覆盖面积达16平方公里。
### Innovation
本文使用Unreal Engine 5 Electric Dreams Environment Sample Project开发了一套便于收集低空和地面视角数据的管线，并提供了灵活的环境因素控制，支持多种任务需求。由此构建的WildfireX-SLAM数据集提供了大规模、全面且高质量的图像资料，有助于揭示3DGS基SLAM在森林中的独特挑战，并为进一步研究指明了改进方向。此外，还进行了基准测试，不仅显示了3DGS基SLAM在森林野火环境中的独特挑战，还展示了未来工作的潜在改进点。数据集和源代码将公开提供，为研究和应用提供重要资源。
### Conclusion
本文构建了一个大规模低空RGB-D数据集WildfireX-SLAM，用于森林和野火环境下的SLAM研究，并评估了3DGS基SLAM方法的性能，在森林野火环境中发现并解决了新的挑战，提供了研究和应用的重要资源。
## 361. `cs.CV` - 为高分辨率图像生成准确详细的描述 [PDF](https://arxiv.org/pdf/2510.27164), [HTML](https://arxiv.org/abs/2510.27164)
### Authors
Hankyeol Lee,Gawon Seo,Kyounggyu Lee,Dogun Kim,Kyungwoo Song,Jiyoung Jung
### Background
视觉语言模型（VLMs）在为高分辨率图像生成准确和详细的描述时往往存在问题，因为它们通常是在低分辨率输入（如224x224或336x336像素）上进行预训练的。这可能导致在描述时丢失视觉细节和重要对象。
### Innovation
本文提出了一种新颖的流水线，结合了视觉语言模型、大型语言模型（LLMs）和物体检测系统，以提高描述质量。该流水线通过多阶段过程细化描述。通过视觉语言模型生成初稿描述，然后使用大型语言模型识别图像中的关键物体。大型语言模型预测与识别的关键物体共现的其他可能物体，并由物体检测系统验证这些预测。未在初稿描述中提及的新检测到的物体将进行聚焦的、区域特定的描述，以确保它们被纳入。这个过程丰富了描述的细节，减少了幻觉，即删除未检测到物体的参考。
### Conclusion
实验结果表明，该管道在高分辨率图像数据集上生成了更详细、可靠的图像描述，同时有效减少了幻觉。
## 362. `cs.CV` - AFM-Net: 高级融合分层次CNN视觉先验与全局序列建模以进行遥感图像场景分类 [PDF](https://arxiv.org/pdf/2510.27155), [HTML](https://arxiv.org/abs/2510.27155)
### Authors
Yuanhao Tang,Xuechao Zou,Zhengpei Hu,Junliang Xing,Chengkun Zhang,Jianqiang Huang
### Background
遥感图像场景分类仍然是一个具有挑战性的任务，主要由于地面对象的复杂空间结构和多尺度特性。现有的方法中，CNN擅长建模局部纹理，而Transformer则擅长捕捉全局上下文。但是，有效地整合这两种方法仍然受到Transformer高计算成本的瓶颈制约。
### Innovation
AFM-Net提出了一种高级层次融合框架，通过两种路径实现局部和全局的有效协同表示：CNN分支提取分层次的视觉先验，Mamba分支进行高效的全局序列建模。AFM-Net的核心创新在于其层次融合机制，该机制逐步从两个路径中聚合多尺度特征，实现动态跨层次特征交互和上下文重构，生成高判别力的表示。这些融合特征随后通过混合专家分类模块适配性路由，将它们分配给最适合的专家进行精细场景识别。这些实验在AID、NWPU-RESISC45和UC Merced数据集上展示了AFM-Net的优越性能。
### Conclusion
AFM-Net在AID、NWPU-RESISC45和UC Merced数据集上的实验结果显示，它的准确率分别为93.72%、95.54%和96.92%，超越了最先进的方法，在性能和效率上都取得了平衡。源代码可在 given URL 获取。
## 363. `cs.CV` - DANCER: 通过条件增强和渲染的扩散模型进行舞蹈动画 [PDF](https://arxiv.org/pdf/2510.27169), [HTML](https://arxiv.org/abs/2510.27169)
### Authors
Yucheng Xing,Jinxing Yin,Xiaodong Liu
### Background
近年来，扩散模型在视觉生成任务中表现出令人印象深刻的性能。除了静态图像之外，人们对生成真实视频的兴趣不断增加。视频生成不仅对质量有更高要求，而且还面临保持视频连续性的挑战。在所有视频生成任务中，包含人类参与的内容，如舞蹈，由于人类动作的高度自由度而更难生成。
### Innovation
本文提出了一种新颖的框架DANCER（通过条件增强和渲染的扩散模型进行舞蹈动画合成），基于最新的稳定视频扩散模型。为了充分利用参考图像和视频序列的引导作用，框架中引入了两个重要模块。设计了外观增强模块（AEM）以在生成过程中更加关注参考图像的细节，并通过姿势渲染模块（PRM）来扩展运动指导，以从额外领域捕获姿势条件。还收集了大量来自网络的视频数据，构建了一个新的数据集TikTok-3K，以增强模型的训练。
### Conclusion
所提出的模型通过广泛实验在实际数据集上进行了评估，其性能优于当前最先进的方法。所有数据和代码将在论文被接受后发布。
## 364. `cs.CV` - 我们有多接近？AI模型在Banff病灶评分中的局限与进展 [PDF](https://arxiv.org/pdf/2510.27158), [HTML](https://arxiv.org/abs/2510.27158)
### Authors
Yanfan Zhu,Juming Xiong,Ruining Deng,Yu Wang,Yaohong Wang,Shilin Zhao,Mengmeng Yin,Yuqing Liu,Haichun Yang,Yuankai Huo
### Background
Banff分类为评估肾脏移植活检提供了一个全球标准，但其半定量性质、复杂标准和观察者之间的差异障碍了计算复制。本研究探索使用现有深度学习模型通过模块化规则框架近似Banff病变评分的可行性，分解每个Banff指标（如肾小球炎、间质血管炎等），并评估当前分割和检测工具是否能够支持其计算。模型输出通过与专家指南对齐的经验性规则映射到Banff评分，并与专家标注的地面真实进行评估。虽然最终分数有时与专家标注一致，但中间表示的不一致性经常损害可解释性。
### Innovation
本研究采用模块化规则框架探索现有深度学习模型近似Banff病变评分的可行性，具体将每个Banff指标分解为构成的结构和炎症成分，并考察当前分割和检测工具是否支持它们的计算，用经验规则将模型输出映射到Banff评分，并与专家标注的地面真实进行评估。
### Conclusion
研究表明，尽管模型在某些方面取得了一定的成功，但在结构上的遗漏、虚构以及检测模糊等关键失败模式依然存在。即使最终评分与专家标注一致，中间表示的不一致性也常常损害了可解释性。这些结果揭示了当前人工智能管道在复制计算专家级评分方面的局限，并强调模块化评估和计算Banff评分标准的重要性，这将指导未来移植病理模型的发展。
## 365. `cs.CV` - H2-Cache: 一种用于生成扩散模型高性能加速的新型分层双阶段缓存 [PDF](https://arxiv.org/pdf/2510.27171), [HTML](https://arxiv.org/abs/2510.27171)
### Authors
Mingyu Sung,Il-Min Kim,Sangseok Yun,Jae-Mo Kang
### Background
扩散模型在图像生成中表现出色，但由于其迭代去噪过程的巨大计算成本，实际部署受到阻碍。现有的缓存技术可以加速推断，但也经常在速度和保真度之间造成困难的权衡，导致质量下降和高计算开销。
### Innovation
我们引入了H2-Cache，这是一种针对现代生成扩散模型架构的新颖层次缓存机制。H2-Cache通过将去噪过程的功能分离成结构定义阶段和细节精炼阶段，并使用独立的阈值来选择性地缓存每个阶段，实现了加速。为了确保双检查方法的效率，我们引入了聚合特征摘要（PFS），这是一种轻量级的相似性估计技术。实验表明，H2-Cache能够显著加速（最多5.08倍）同时保持图像质量几乎与基线相同，定量和定性上均优于现有缓存方法。
### Conclusion
我们的工作提供了一种稳健且实用的解决方案，有效地解决了速度-质量难题，显著降低了高保真扩散模型在实际应用中的门槛。
## 366. `cs.CV` - M^3Detection: 多帧多级特征融合的多模态3D目标检测方法，结合相机和4D成像雷达 [PDF](https://arxiv.org/pdf/2510.27166), [HTML](https://arxiv.org/abs/2510.27166)
### Authors
Xiaozhi Li,Huijun Di,Jian Li,Feng Liu,Wei Liang
### Background
最近的4D成像雷达技术使得在恶劣天气中实现稳健的感知成为可能，而相机传感器则提供了密集的语义信息。将这两种互补的传感器技术融合可以实现低成本的3D感知。然而，现有的相机-雷达融合方法通常仅限于单帧输入，这只能捕捉到场景的部分视图。不完整的信息，再加上图像退化和4D雷达稀疏性，降低了总体检测性能。相比之下，多帧融合提供了更加丰富的时空信息，但面临着两个挑战：实现跨帧和模态的鲁棒而有效的目标特征融合，以及缓解冗余特征提取导致的计算成本增加。
### Innovation
提出了一种名为M^3Detection的统一多帧3D对象检测框架，该框架在来自相机和4D成像雷达的多模态数据上执行多级特征融合。框架利用了基础检测器的中间特征，并通过追踪器生成参考轨迹，以提高计算效率并为第二阶段提供更丰富的信息。在第二阶段，设计了一个由雷达信息引导的全局级对象间特征聚合模块，以跨候选提案对齐全局特征，并设计了一个局部级网格间特征聚合模块，沿参考轨迹扩展局部特征以增强细粒度的对象表示。聚合后的特征通过一个轨迹级多帧时空推理模块进行处理，以编码跨帧交互并增强时间表示。
### Conclusion
在VoD和TJ4DRadSet数据集上的广泛实验表明，M^3Detection在3D检测性能上达到最先进的技术水平，并验证了它在相机-4D成像雷达融合的多帧检测中的有效性。
## 367. `cs.CV` - SilhouetteTell：利用模糊视频字幕录制进行实际视频识别 [PDF](https://arxiv.org/pdf/2510.27179), [HTML](https://arxiv.org/abs/2510.27179)
### Authors
Guanchong Huang,Song Fang
### Background
视频识别攻击对隐私构成了重大威胁，可用于揭示受害者观看的视频内容，进而暴露其爱好、宗教信仰、政治倾向、性取向和健康状况等。视频观看历史还可用于用户画像或广告目的，可能导致网络欺凌、歧视或敲诈。现有的广泛视频推断技术通常依赖于分析在线视频流产生的网络流量数据。然而，本文观察到字幕内容决定了其在屏幕上的轮廓显示，并通过识别每个字幕轮廓推导出连续字幕之间的时间差。本文提出了SilhouetteTell，一种新颖的视频识别攻击方法，结合了字幕轮廓的空域和时域信息，形成了一种时空特征。SilhouetteTell探索了视频录制的字幕轮廓与字幕文件之间的时空相关性，适用于在线和离线视频。实验结果表明，在各种情况下，SilhouetteTell在智能手机上具有很高的识别效果，包括从40米远的距离识别视频标题和片段。
### Innovation
SilhouetteTell 智能结合了字幕的空域和时域信息，形成了时空特征，突破了现有依赖网络流量分析的视频推断技术。它能够从模糊的字幕记录中有效地推断视频标题和片段，展现了更高的识别能力和广泛的适用性。
### Conclusion
SilhouetteTell 通过充分利用字幕轮廓的时空特性，可以在不同环境下有效推断视频内容，证明了其在实际应用中具有高效率和广泛的适用性。
## 368. `cs.CV` - Dual-level Progressive Hardness-Aware Reweighting for Cross-View Geo-Localization [PDF](https://arxiv.org/pdf/2510.27181), [HTML](https://arxiv.org/abs/2510.27181)
### Authors
Guozheng Zheng,Jian Guan,Mingjie Xie,Xuanjia Zhao,Congyi Fan,Shiheng Zhang,Pengming Feng
### Background
跨视角地理定位（CVGL）在无人机和卫星图像间仍具有挑战性，因为存在严重的视角差异以及难以区分的负面样本（在视觉上相似但地理上不匹配）。现有方法通常采用静态加权策略，这种策略容易受到分布变化的影响，并且在早期优化中过度强调困难样本，导致梯度噪音和不稳定收敛。
### Innovation
提出了一种双层渐进式硬度感知加权（DPHR）策略。在样本层面，引入了基于比率的难度感知（RDA）模块来评估相对难度并为负样本分配细致的权重。在批次层面，引入了渐进式自适应损失加权（PALW）机制，利用训练进程信号在早期优化阶段减弱噪音梯度，并随着训练的成熟逐步增强困难负样本挖掘。
### Conclusion
在University-1652和SUES-200基准上进行的实验表明，提出的DPHR策略在有效性和鲁棒性方面均优于现有最佳方法，实现了持续的增强效果。
## 369. `cs.CV` - 通过分层图神经网络进行传统村落空间形态多模态特征融合分析 [PDF](https://arxiv.org/pdf/2510.27208), [HTML](https://arxiv.org/abs/2510.27208)
### Authors
Jiaxin Zhang,Zehong Zhu,Junye Deng,Yunqin Li,and Bowen Wang
### Background
村庄在研究人地关系中具有重要地位，然而随着城市化的发展，空间特征逐渐消失，景观同质化问题突出。现有研究主要采用单一学科视角分析村庄空间形态及其影响因素，且依赖定性分析方法。这些研究受限于缺乏数字基础设施和数据不足。
### Innovation
本文提出了一种基于多源数据的分层图神经网络（HGNN）模型，加入了空间形态分类的关联池化机制和联合训练策略，通过图卷积网络（GCN）和图注意力网络（GAT）在两阶段特征更新机制下有效融合多模态特征，显著提高了多模态融合和分类任务的性能，并克服单一模型的限制。
### Conclusion
通过这种方法，我们提高了所有子类型的联合优化，将均值准确度/F1从0.71/0.83（独立模型）提升到0.82/0.90，提升了6%的parcel任务性能。该方法为探索村庄空间模式和生成逻辑提供了科学依据。
## 370. `cs.CV` - 隐私感知的多窗口胸部计算机断层扫描持续自我监督学习以实现领域偏移稳健性 [PDF](https://arxiv.org/pdf/2510.27213), [HTML](https://arxiv.org/abs/2510.27213)
### Authors
Ren Tasai,Guang Li,Ren Togo,Takahiro Ogawa,Kenji Hirata,Minghui Tang,Takaaki Yoshimura,Hiroyuki Sugimori,Noriko Nishioka,Yukie Shimizu,Kohsuke Kudo,Miki Haseyama
### Background
在医学图像诊断中，构建稳健且高度通用的模型极具挑战性，主要由于大规模精确注释数据的稀缺性以及动态医疗环境中固有的领域偏移。具体来说，在胸部CT中，这些领域偏移通常源于不同窗口设置之间的差异，这些设置是为了不同的临床目的而优化的。过去的持续自我监督学习(CSSL)框架往往通过重复使用过去的数据来缓解领域偏移，但由于隐私限制，这种做法通常是不实际的。此外，由于窗口设置的不同，不同医学成像窗口下的数据集会产生领域偏移，这对模型的持续学习构成了挑战，尤其是在确保数据隐私的情况下。
### Innovation
本文提出了一种新颖的持续自我监督学习(CSSL)框架，用于从多窗口获取的胸部CT图像中同时学习多样特征，并确保数据隐私。该方法通过持续预训练中的潜在线索回放机制有效地捕获先前学习知识与新信息之间的关系，同时缓解领域偏移带来的灾难性遗忘现象，同时确保数据隐私。此外，该方法还引入了一种特征蒸馏技术，结合了Wasserstein距离知识蒸馏(WKD)和批次知识聚合(BKE)，增强了模型学习稳健、领域迁移不变表示的能力。
### Conclusion
最后，通过多窗口获取的胸部CT图像验证了本方法，与现有方法相比，证明了其优越的性能。
## 371. `cs.CV` - 多模态大模型能读懂房间吗？一种多模态基准测试以验证多方社交互动中的真实性 [PDF](https://arxiv.org/pdf/2510.27195), [HTML](https://arxiv.org/abs/2510.27195)
### Authors
Caixin Kang,Yifei Huang,Liangyang Ouyang,Mingfang Zhang,Yoichi Sato
### Background
随着人工智能系统日益融入人类生活，赋予它们强大的社会智能已成为关键的方向之一。这种智能的一个重要方面是区分真伪的能力，这是人类互动中一个普遍存在的元素，通过口头语言和非口头视觉提示的复杂交互来传达。然而，在动态的多党对话中自动检测欺骗仍然是一个重大挑战。强大的多模态大型语言模型（MLLMs）最近的崛起，凭借其在视觉和文本理解方面的出色能力，它们成为这一任务的自然候选人。因此，它们在这一关键领域的表现大多未被量化。
### Innovation
为了应对这一差距，本文提出了一个新的任务，即多模态互动真实性评估（MIVA），并提出了一种从狼人杀游戏中派生出的新多模态数据集。该数据集提供了同步的视频和文本，每个陈述都有可验证的真实标签。我们建立了一个全面的基准测试以评估最新的MLLMs，结果显示存在显著的性能差距：即使像GPT-4o这样强大的模型，在可靠地区分真话和谎言方面也存在问题。我们对失败模式的分析表明，这些模型无法有效地将语言与视觉社会提示联系起来，并且可能在对齐方面过于保守，这强调了迫切需要开发新的方法以构建更具洞察力和值得信赖的AI系统。
### Conclusion
最新的MLLMs在多党社交互动中验证真实性方面存在显著的性能差距，尤其是在区分真伪方面。有效的多模态基准测试揭示了这些模型在语言与视觉社会提示之间的联系上存在不足，并且可能过于保守，强调了构建更具洞察力和值得信赖的AI系统的迫切需求。
## 372. `cs.CV` - 基于YOLOv11的Mask-to-Height架构：用于卫星图像中的联合建筑实例分割与高度分类 [PDF](https://arxiv.org/pdf/2510.27224), [HTML](https://arxiv.org/abs/2510.27224)
### Authors
Mahmoud El Hussieni,Bahadır K. Güntürk,Hasan F. Ateş,Oğuz Hanoğlu
### Background
精确的建筑实例分割和高度分类对于城市规划、三维城市建模和基础设施监测至关重要。本文分析了YOLOv11，这是YOLO系列最新发展的深度学习模型，针对其在卫星图像中联合提取建筑和离散高度分类的应用。结果显示，YOLOv11在复杂城市场景中表现出色，并且能够处理遮挡、复杂的建筑形状和类别不平衡等问题，尤其是对于稀有的高层建筑。
### Innovation
YOLOv11基于早期YOLO模型的优点，采用了更高效的架构，能够更有效地结合不同尺度的特征，提升物体定位精度并在复杂的城市环境中增强性能。研究显示，YOLOv11在检测准确性上优于早期的多任务框架，同时在推理速度上更具优势，适合用于实时大规模的城市制图。
### Conclusion
本文通过利用DFC2023数据集评估了YOLOv11，结果显示它的实例分割性能显著，同时高度分类准确性高。该研究展示了YOLOv11在实现语义城市重建方面的潜力，尤其是通过简化分类高度建模，为遥感和地理空间智能领域的未来发展提供了有价值的观点。
## 373. `cs.CV` - SpecAware: 一种用于多传感器统一学习的光谱-内容感知基础模型在高光谱遥感制图中的应用 [PDF](https://arxiv.org/pdf/2510.27219), [HTML](https://arxiv.org/abs/2510.27219)
### Authors
Renjie Ji,Xue Wang,Chao Niu,Wen Zhang,Yong Mei,Kun Tan
### Background
高光谱成像（HSI）是精细土地利用和土地覆盖（LULC）制图的重要工具。然而，HSI数据的内在异质性一直是通过联合训练开发通用模型的主要障碍。虽然HSI基础模型在不同的下游任务中展现出潜力，但现有的方法通常忽略了传感器元属性的关键指导作用，并且难以进行多传感器训练，从而限制了它们的可移植性。
### Innovation
我们提出了SpecAware，一种新的光谱-内容感知的HSI基础模型，用于统一多传感器学习。我们还构建了Hyper-400K数据集，这是新的大型高质量基准数据集，包含来自多种航空AVIRIS传感器的超过40万张图像块。SpecAware的核心是一个两步超网络驱动的编码过程。首先，设计了一个元内容感知模块，生成每个HSI块的唯一条件输入，为每个样本的每个光谱带融合传感器元属性和其自己的图像内容。其次，设计了HyperEmbedding模块，其中样本条件下的超网络动态生成通道级编码的一对矩阵因子，包括自适应空间模式提取和潜在语义特征重投影。因此，SpecAware可以感知和解释不同场景和传感器的空-光谱特征，从而能够适应处理不同数量的光谱通道，建立联合预训练的统一框架。
### Conclusion
在六个数据集上的广泛实验表明，SpecAware能够学习更优的特征表示，在土地覆盖语义分割、变化检测和场景分类方面表现出色。
## 374. `cs.CV` - MoRE: 3D视觉几何重建遇见混合专家 [PDF](https://arxiv.org/pdf/2510.27234), [HTML](https://arxiv.org/abs/2510.27234)
### Authors
Jingnan Gao,Zhe Wang,Xianze Fang,Xingyu Ren,Zhuo Chen,Shengqi Liu,Yuhao Cheng,Jiangjing Lyu,Xiaokang Yang,Yichao Yan
### Background
近期，语言和视觉方面的进展表明，扩展模型容量可以持续提升多样任务的表现。在3D视觉几何重建中，大规模训练也证明了其有效，有助于学习多样性的表示。然而，3D模型进一步扩展面临挑战，主要由于几何监督的复杂性和3D数据的多样性。
### Innovation
提出了一种名为MoRE的基于Mixture-of-Experts（MoE）架构的密集3D视觉基础模型，该模型能够动态地将特征按任务路由到特定专家，让他们在互补的数据方面进行专业化的学习。此外，MoRE结合了基于信心的深度细化模块和密集的语义特征，与全局对齐的3D主干表示一起用于高保真表面法线预测。MoRE还通过定制损失函数确保跨多样输入和多个几何任务的鲁棒学习。
### Conclusion
广泛的实验表明，MoRE在多个基准测试中达到了最先进的性能，并能够在没有额外计算的情况下支持有效的下游应用。
## 375. `cs.CV` - 基于对象一致性和网格变形的自监督图像重新尺寸方法：Object-IR [PDF](https://arxiv.org/pdf/2510.27236), [HTML](https://arxiv.org/abs/2510.27236)
### Authors
Tianli Liao,Ran Wang,Siqing Zhang,Lei Li,Guangen Liu,Chenyang Zhao,Heling Cao,Peng Li
### Background
在图像重新尺寸过程中消除重要区域的几何失真是一个难以解决的问题。现有方法难以同时保持视觉质量和几何精度。本文提出了Object-IR，一种自监督架构，将图像重新尺寸重新定义为基于学习的网格变形优化问题，该问题由对象外观一致性和几何保持约束指导。
### Innovation
Object-IR 通过自监督方式消除了需要手动标注的重新尺寸数据集，直接从输入的几何属性和语义属性中产生监督。该方法通过一个综合目标函数（包含对象一致损失、几何保持损失和边界损失）来减少几何失真，优化了输入图像的网格变形以保持重要对象的外观，同时限制重要网格的简单尺度变换，并强制输出为清洁的矩形。
### Conclusion
通过在RetargetMe基准上的大量评估，Object-IR 在定量指标和主观视觉质量评估方面均表现出最先进的性能。同时，该框架在任意输入分辨率下实现了高效处理（例如，1024x683分辨率的平均推理时间为0.009秒）并保持实时性能，在消费级 GPU 上运行。源代码即将在此httpsURL 查看。
## 376. `cs.CV` - 用于整个切片图像分析的异构病理基础模型融合 [PDF](https://arxiv.org/pdf/2510.27237), [HTML](https://arxiv.org/abs/2510.27237)
### Authors
Zhidong Yang,Xiuhui Shi,Wei Ba,Zhigang Song,Haijing Luan,Taiyuan Hu,Senlin Lin,Jiguang Wang,Shaohua Kevin Zhou,Rui Yan
### Background
全切片图像（WSI）分析已成为计算病理学中越来越重要的技术。最近在病理基础模型（FMs）方面的进展已经展示了从WSIs中提取有意义的区域级或切片级特征表示的显著优势。然而，当前的病理FMs由于不同的私人训练数据集和不同的网络架构展示出相当大的异质性。这种异质性在下游任务中使用来自不同FMs的提取特征时引入了性能变异性。为了充分利用多种FMs的优势，本研究提出了一种用于异构病理FMs融合的新框架，称为FuseCPath，从而获得具有优越集成性能的模型。
### Innovation
本文的主要创新贡献包括：（i）为了保证训练切片的代表性，提出了一种基于多视图聚类的方法，通过多种FMs的嵌入筛选出具有区分性的切片；（ii）为了有效融合异构的区域级FMs，设计了一种聚类级别的再嵌入策略，以实时捕获区域级局部特征；（iii）为了有效融合异构的切片级FMs，设计了一种协作式知识蒸馏策略，以探索切片级FMs之间的联系。广泛实验证明，所提出的FuseCPath方法在肺癌、膀胱癌和结肠直肠癌的数据集上，即使在公共数据集上也能够实现最佳性能。
### Conclusion
本研究提出的FuseCPath框架通过对异构病理基础模型的融合，展示了集成性能的优越性。该框架通过多视图聚类、区域级别再嵌入和协作知识蒸馏策略，有效提升了不同病理FMs在WSI分析中的表现。
## 377. `cs.CV` - Transformer-based Denoiser for Adversarial Defense with Spatial-Frequency Domain Representation [PDF](https://arxiv.org/pdf/2510.27245), [HTML](https://arxiv.org/abs/2510.27245)
### Authors
Alik Pramanick,Mayank Bansal,Utkarsh Srivastava,Suklav Ghosh,Arijit Sur
### Background
近年来，深度神经网络(DNNs)在各种应用中取得了显著的成功。然而，研究表明DNNs受到复杂的对抗性攻击，限制了它们在关键安全系统中的应用。对抗性攻击使得网络模型的性能受到损害，降低了其鲁棒性。因此，如何提高神经网络对对抗性攻击的抵抗力成为研究热点问题。本研究提出了一种双阶段训练方法，首先训练去噪网络，然后训练分类模型，以增强模型的鲁棒性。特别地，该研究结合了空间域和频率域的方法，利用离散小波变换(DWT)进行频域分析，并引入了结合空间图像特征和小波的Transformer层来构建去噪网络。
### Innovation
本文提出的双阶段训练方法在对抗性防御中引入了创新的去噪策略，结合了空间域和频率域的方法。首先，利用离散小波变换(DWT)分析攻击图像的频率特征，并设计一个去噪网络，将空间图像特征与小波结合，通过Transformer层实现去噪。其次，使用去噪后的图像重新训练分类模型，从而增强其对抗性攻击的鲁棒性。
### Conclusion
实验结果显示，本文提出的方法在MNIST、CIFAR-10和Fashion-MNIST数据集上显著提高了分类精度，远超仅使用去噪网络和对抗性训练方法的效果。该方法通过结合空间域和频率域的方法，利用小波变换和Transformer层实现图像去噪和提高模型鲁棒性，为对抗性防御提供了新的思路。源代码已发布。
## 378. `cs.CV` - T3: 在VLMs中进行零样本医学影像分析的测试时模型融合 [PDF](https://arxiv.org/pdf/2510.27265), [HTML](https://arxiv.org/abs/2510.27265)
### Authors
Raza Imam,Hu Wang,Dwarikanath Mahapatra,Mohammad Yaqub
### Background
在医学影像领域，视觉-语言模型面临两难的情况：预训练网络提供广泛的稳健性但缺少特定模态的细微特性，而微调的专家模型虽然在分布内准确性高，但在模态变化的情况下表现不佳。现有的模型合并技术，都是为自然图像基准设计的，它们虽然简单高效，但在不同医学模态中却难以提供一致的性能提升；这些静态插值方法在各种临床任务中可靠性较差。因此，亟需一种新的方法来解决这一问题。
### Innovation
本文介绍了一种名为Test-Time Task adaptive merging（T^3）的反向传播框架，该框架通过计算两个模型输出分布之间的Jensen-Shannon距离来确定每个样本的插值系数。T^3动态保留模型一致时的局部精度，并在出现模态漂移时依赖泛化稳健性。为了克服样本级合并的推理成本，提出了一种批级扩展T^3_B，它为一批样本计算合并系数，显著减少了计算瓶颈。并且提出了严格的跨评估协议，涵盖了不同医学模态内的性能、基础到新颖类别的性能以及抗毁性。
### Conclusion
实验结果表明，T^3在Top-1准确性和错误率减少方面设立了新的最佳基准，超过了强基准模型，同时保持高效性，为临床环境中自适应MVLM的部署开辟了道路。相关代码已开源。
## 379. `cs.CV` - RegionRAG: Region-level Retrieval-Augmented Generation for Visually-Rich Documents [PDF](https://arxiv.org/pdf/2510.27261), [HTML](https://arxiv.org/abs/2510.27261)
### Authors
Yinglu Li,Zhiying Lu,Zhihang Liu,Chuanbin Liu,Hongtao Xie
### Background
现有的多模态检索增强生成（RAG）方法通过利用候选视觉文档来增强大规模语言模型（LLMs），但在处理时通常以整个文档作为基本检索单位，这会引入大量的无关视觉内容：1) 相关文档中通常包含大量与查询无关的大区域，分散了对关键信息的注意力；2) 扩展检索文档数量以提高召回率，进一步引入了冗余和无关的文档。这些冗余信息会分散模型的注意力并进一步降低性能。
### Innovation
提出了RegionRAG，这是一种新的框架，将检索范式从文档层面转移到区域层面。训练时设计了一种混合监督策略，结合标记数据和未标记数据来标注相关片段。推理时提出了一种智能管道，能够将关键片段智能组合成完整的语义区域。通过将识别相关区域的任务委托给检索器，RegionRAG 允许生成器专注于与查询相关的简洁视觉内容，从而提高效率和准确性。
### Conclusion
在六个基准测试上，RegionRAG实现了最先进的性能。与前代方法相比，它在R@1上的检索准确率提高了10.02%，且在仅使用71.42%的视觉标记的情况下，问题回答准确率提高了3.56%。
## 380. `cs.CV` - HyperClick: 通过不确定性校准提升可靠GUI地基 [PDF](https://arxiv.org/pdf/2510.27266), [HTML](https://arxiv.org/abs/2510.27266)
### Authors
Shaojie Zhang,Pei Fu,Ruoceng Zhang,Jiahui Yang,Anan Du,Xiuwen Xi,Shaokang Wang,Ying Huang,Bin Qin,Zhenbo Luo,Jian Luan
### Background
自主图形用户界面（GUI）代理依赖于准确的GUI接地，将语言指令转换为屏幕坐标来执行用户命令。然而，当前通过监督微调（SFT）或强化微调（RFT）训练的模型缺乏对自身能力边界的自我意识，导致过度自信和不可靠的预测。研究表明，这种情况下准确性和信心之间的不匹配，在动态GUI自动化任务中尤为关键，因为单一错误可能导致任务失败。
### Innovation
提出了HyperClick，这是一个新颖的框架，通过不确定性校准增强可靠的GUI接地。HyperClick引入了一种双重奖励机制，结合了二进制奖励（正确操作）和基于截断正态分布的空间置信度建模，并采用Brier得分进行校准。该方法通过联合优化接地准确性与置信度可靠性共同优化，促进自我反省的批判性思考。
### Conclusion
在七个挑战基准上的广泛实验表明，HyperClick达到了最先进的性能，同时提供了具有良好校准的信心。通过显式地进行置信度校准和自我反省的批判性思考，HyperClick减少了过度自信，支持更可靠的GUI自动化。
## 381. `cs.CV` - 重新思考扩散模型中鲁棒的概念对抗擦除 [PDF](https://arxiv.org/pdf/2510.27285), [HTML](https://arxiv.org/abs/2510.27285)
### Authors
Qinghong Yin,Yu Tian,Yue Zhang
### Background
概念擦除旨在选择性地从扩散模型中删除不希望的内容，以降低敏感内容生成的风险。大部分现有方法使用对抗性训练来识别和抑制目标概念，从而减少生成有害输出的可能性。然而，这些方法往往忽略了扩散模型中对抗性训练的特殊性，导致仅部分缓解问题。本文从概念空间的视角探讨并量化了这一点，即对抗样本能否真正符合目标概念空间？研究表明，现有方法在生成对抗样本时忽视了概念语义的作用，导致对概念空间的有效拟合不足。这导致了两个主要问题：1）当对抗样本较少时，它们无法全面覆盖目标对象的概念；2）相反，它们会干扰其他目标概念空间。
### Innovation
本文引入了S-GRACE（基于语义的鲁棒对抗概念擦除），它充分利用概念空间中的语义指导生成对抗样本并进行擦除训练，解决了现有方法的不足。实验结果表明，S-GRACE显著提高了擦除性能26%，更好地保留了非目标概念，并将训练时间减少了90%。
### Conclusion
通过S-GRACE方法的验证，提出的方法在多种扩散模型归零场景中取得了显著的改进效果，能够更为准确地消除目标概念且保留其他概念，同时也大幅减少了训练时间。
## 382. `cs.CV` - FOCUS: 长视频理解中的高效关键帧选择 [PDF](https://arxiv.org/pdf/2510.27280), [HTML](https://arxiv.org/abs/2510.27280)
### Authors
Zirui Zhu,Hailun Xu,Yang Luo,Yong Liu,Kanchan Sarkar,Zhenheng Yang,Yang You
### Background
多模态大型语言模型（MLLMs）将图像和视频帧表示为视觉标记。然而，从单张图像扩展到一小时的视频，标记集超出了实际限制。流行的管道要么均匀下采样，要么使用较小的语言视觉模型的检索式评分进行关键帧选择。然而，这些关键帧选择方法依赖于预筛选，以减少推理成本，并可能错过最具信息性的时刻。
### Innovation
我们提出了FOCUS，一种无需训练且模型无关的关键帧选择模块，在严格的标记预算下选择查询相关的关键帧。FOCUS将关键帧选择形式化为多臂老虎机中的组合纯探索（CPE）问题：将短时间片段视为臂，并利用经验均值和伯努利信心半径，同时探索不确定区域来识别信息区域。FOCUS的探索-利用双重阶段减少关键帧选择为顺序策略，首先识别高价值的时间区域，然后在每个区域内选择得分最高的关键帧。在两个长视频问答基准上，FOCUS在处理不到2%的视频帧的情况下提供了显著的准确性改进，对于超过20分钟的视频，FOCUS在LongVideoBench上实现了11.9%的准确性增益，证明了其作为关键帧选择方法的有效性，同时也提供了一种解决长视频理解的简单且通用方法。
### Conclusion
FOCUS能够在严格的标记预算下，有效地选择关键帧，其方法适用于多模态大型语言模型的长效视频理解，实现显著的准确性增益，小于2%的视频帧处理率，尤其在长视频理解上表现突出。
## 383. `cs.CV` - 通过频率门控Mamba实现多功能且高效的医学图像超分辨率 [PDF](https://arxiv.org/pdf/2510.27296), [HTML](https://arxiv.org/abs/2510.27296)
### Authors
Wenfeng Huang,Xiangyun Liao,Wei Cao,Wenjing Jia,Weixin Si
### Background
医学图像超分辨率（SR）对于提高诊断精度、减少获取成本和扫描时间至关重要。然而，使用低计算开销同时建模长距离解剖结构和细粒度高频细节仍然是一个挑战。
### Innovation
提出了一种新的频率感知门控状态空间模型FGMamba，该模型将全局依赖性建模和细粒度细节增强统一到一个轻量级的结构中。该方法包含两个关键创新：一种增强的门控注意力状态空间模块（GASM），结合高效的状态空间建模与双分支空间和通道注意力；以及一个通过FFT引导融合的分层频率融合模块（PFFM）。
### Conclusion
在超声、OCT、MRI、CT和内窥镜等五种医学成像模态上进行广泛的评估表明，FGMamba在保持较小参数占用（<0.75M）的同时实现了更好的PSNR/SSIM，超越了基于CNN和Transformer的方法。结果验证了频率感知状态空间建模在医学图像增强中的有效性和可扩展性。
## 384. `cs.CV` - CASR-Net: 一种专注于图像处理的基于深度学习的冠状动脉分割和细化网络，用于X射线冠状动脉造影 [PDF](https://arxiv.org/pdf/2510.27315), [HTML](https://arxiv.org/abs/2510.27315)
### Authors
Alvee Hassan,Rusab Sarmun,Muhammad E. H. Chowdhury,M. Murugappan,Md. Sakib Abrar Hossain,Sakib Mahmud,Abdulrahman Alqahtani,Sohaib Bassam Zoghoul,Amith Khandakar,Susu M. Zughaier,Somaya Al-Maadeed,Anwarul Hasan
### Background
早期检测冠状动脉疾病(CAD)对于降低死亡率和改善患者治疗规划至关重要。尽管从X射线进行血管图像分析是识别心脏异常，包括狭窄的冠状动脉的一种常见且经济的方法，但图像质量差会显著妨碍临床诊断。
### Innovation
CASR-Net是一个由图像预处理、分割和细化三个阶段组成的管道。它的创新是一个基于UNet的分割网络，该网络使用DenseNet121编码器和基于自组织操作神经网络（Self-ONN）的解码器，这有助于保持狭窄和狭窄的冠状动脉分支的连续性。此外，引入了一种新颖的多通道预处理策略，结合了CLAHE和改进的Ben Graham方法。最后，引入了一种边缘细化模块来进一步抑制假阳性。
### Conclusion
CASR-Net在5折交叉验证下，使用两个公共数据集（包含健康和狭窄的动脉），比几个先进模型表现更好，实现了61.43%的IoU、76.10%的DSC和79.36%的clDice。这些结果表明，CASR-Net提供了一种可靠的自动冠状动脉分割方法，为临床诊断和治疗规划提供了有价值的工具。
## 385. `cs.CV` - SAGS: 自适应无混叠高斯点阵法在动态外科内窥镜重建中的应用 [PDF](https://arxiv.org/pdf/2510.27318), [HTML](https://arxiv.org/abs/2510.27318)
### Authors
Wenfeng Huang,Xiangyun Liao,Yinling Qian,Hao Liu,Yongming Yang,Wenjing Jia,Qiong Wang
### Background
在机器人辅助外科手术中，动态组织的外科重建技术至关重要。神经辐射场（NeRF）已极大地提高了可变形组织的重建效果，但端肟能见性中的混叠和伪影问题仍然导致了图像质量的下降。3D高斯点阵（3DGS）提高了重建效率，但现有方法常侧重于渲染速度，而忽视了这些关键问题。
### Innovation
我们提出了一种自适应无混叠高斯点阵（SAGS）框架，采用了注意驱动、动态加权的4D变形解码器，并通过3D平滑滤波器和2D斑片滤波器来减轻变形组织重建中的伪影，更好地捕捉组织运动的细节。
### Conclusion
我们的方法在PSNR、SSIM和LPIPS等所有指标上均优于现有方法，并且提供了更好的图像可视化效果。
## 386. `cs.CV` - 通过参数化提示克服增量目标检测中的提示池混乱 [PDF](https://arxiv.org/pdf/2510.27316), [HTML](https://arxiv.org/abs/2510.27316)
### Authors
Zijia An,Boyu Diao,Ruiqi Liu,Libo Huang,Chuanguang Yang,Fei Wang,Zhulin An,Yongjun Xu
### Background
近年来的研究表明，将可训练提示融入预训练模型可以实现有效的增量学习。然而，在增量对象检测(IOD)中应用提示还很少被探索。现有基于提示池的方法假定增量任务之间的类别集是相互独立的，这不适合IOD，因为它忽略了检测图像中的固有共现现象。在共现场景下，前一个任务中的未标记对象可能出现在当前任务的图像中，导致提示池中的混淆。
### Innovation
提出了一种参数化提示方法(P$^2$IOD)，该方法利用神经网络的全局进化特性，将网络作为可参数化的提示，以适应性地在任务之间积累知识。为了限制提示结构更新，P$^2$IOD进一步采用了一种参数化提示融合策略。
### Conclusion
在PASCAL VOC2007和MS COCO数据集上的详尽实验表明，P$^2$IOD在IOD中的有效性，并且其性能在现有基准模型中达到了最先进的水平。
## 387. `cs.CV` - 生成语义编码用于超低比特率视觉通信和分析 [PDF](https://arxiv.org/pdf/2510.27324), [HTML](https://arxiv.org/abs/2510.27324)
### Authors
Weiming Chen,Yijia Wang,Zhihan Zhu,Zhihai He
### Background
本文探讨了在深空探测、战场情报和复杂环境中机器人导航等极其有限通信带宽场景下的远程视觉分析、人机交互和控制问题。现有的文本到图像生成模型虽然能够在超低比特率下进行图像描述，但只能达到语义级别的视觉场景近似，无法满足视觉通信和远程视觉分析、人机交互的需求。
### Innovation
本文提出了一种将图像生成与深度图像压缩无缝集成的新方法，通过联合文本和编码潜变量引导校正流模型进行精细的视觉场景生成。语义文本描述和编码潜变量均以极小的比特率进行编码和传输。实验结果显示，该方法能够在使用更少带宽的同时，达到与现有方法相同的图像重建质量和视觉分析准确性。
### Conclusion
实验结果表明，该方法在使用更少带宽的情况下，能够达到与现有方法相同的图像重建质量和视觉分析准确性。论文已接受后，将会发布相关的源代码。
## 388. `cs.CV` - MeisenMeister：一种简单的两阶段MRI乳腺癌分类管道 [PDF](https://arxiv.org/pdf/2510.27326), [HTML](https://arxiv.org/abs/2510.27326)
### Authors
Benjamin Hamm,Yannick Kirchhoff,Maximilian Rokuss,Klaus Maier-Hein
### Background
乳腺癌筛查领域的一个关键问题是如何通过更高效和准确地解读乳腺MRI扫描来提高早期检测效率。尽管通用的全身病变分割方法和多时点分析已经存在，但乳腺癌的检测仍然极具挑战性，主要是由于高质量分割标签的稀缺。这使得开发稳健的分类方法对于早期乳腺癌检测至关重要，特别是在大规模筛查的应用中。
### Innovation
提出了一种简单的两阶段MRI乳腺癌分类管道。该方法通过迭代开发过程，经历了多次实验、评估和完善，最终形成了一个基于性能、鲁棒性和临床相关性的设计方案。这种两阶段的方法简化了复杂的技术过程，提高了分类的准确性和可靠性。
### Conclusion
研究团队发布了他们的完整实现代码，以供公众参考。这种两阶段的方法为MRI乳腺癌分类提供了一个简单而有效的解决方案，为未来的乳腺癌早期检测应用提供了新的可能性。
## 389. `cs.CV` - 通过大型语言模型推理理解隐含用户意图的图像编辑 [PDF](https://arxiv.org/pdf/2510.27335), [HTML](https://arxiv.org/abs/2510.27335)
### Authors
Yijia Wang,Yiqing Shen,Weiming Chen,Zhihai He
### Background
现有图像编辑方法在处理简单的编辑指令方面表现出色，但对于复杂的编辑指令则需要联合调优大型语言模型（LLMs）和扩散模型（DMs），这涉及极高的计算复杂性和训练成本。现有的方法无法有效地处理复杂的指令，导致性能限制和高昂的成本问题。因此，提出了新的复杂图像编辑方法即CIELR，该方法将复杂的用户指令转换为一系列简单的明确编辑动作，避免了LLMs和DMs的联合微调。这种方法通过使用基础模型构建输入图像的结构化语义表示，并通过迭代更新机制逐步精炼这一表示，获得精细的视觉表示，从而实现复杂的图像编辑任务。
### Innovation
提出了一种新的复杂图像编辑方法CIELR，该方法能够将复杂的用户指令转换为一系列简单的明确编辑动作，从而避免了大型语言模型和扩散模型的联合微调。通过使用基础模型构建输入图像的结构化语义表示，并引入迭代更新机制进一步细化表示，实现了精细的视觉表示，从而有效处理复杂的图像编辑任务。此外，还构建了一个名为CIEBench的基准数据集，包含86个图像样本及其特定的推理基于的编辑评价指标，CIELR在该基准数据集上也表现出色，超过了现有的方法。
### Conclusion
实验结果表明，使用CIELR方法在PSNR上超越了现有的先进技术9.955 dB，显示出在保持需要一致的区域方面具有更好的性能。同时，通过对复杂的图像编辑指令的理解和处理能力的提升，在公共复杂图像编辑大数据集资源有限的情况下，展示了该方法的有效性和优越性。
## 390. `cs.CV` - RzenEmbed: 向全面跨模态检索迈进 [PDF](https://arxiv.org/pdf/2510.27350), [HTML](https://arxiv.org/abs/2510.27350)
### Authors
Weijian Jian,Yajun Zhang,Dawei Liang,Chunyu Xie,Yixiao He,Dawei Leng,Yuhui Yin
### Background
随着多模态大语言模型（MLLMs）的快速发展，基于CLIP的框架已能够生成强大的、通用的嵌入用于检索任务。然而，现有的方法主要集中在自然图像上，对于其他重要的视觉模态，如视频和视觉文档，支持有限。鉴于此，本研究介绍了一种名为RzenEmbed的统一框架，它可以在文本、图像、视频和视觉文档等多种模态下学习嵌入。研究采用了创新的两阶段训练策略来学习区分性表示，第一阶段专注于基础的文本和多模态检索，而在第二阶段引入一种改进的InfoNCE损失，通过引入两个关键增强措施：一是采用难度加权机制，指导模型优先处理具有挑战性的样本；二是采用方法减少假阴性影响，减轻数据噪声。这种方法不仅增强了模型的区分能力，还提高了其遵循指令的能力。此外，通过学习温度参数和模型混合进一步提升了性能。RzenEmbed在MMEB基准测试中建立了一个新的最先进水平，不仅在整体得分上达到最佳，还在视频和视觉文档检索等挑战性任务上超越了所有先前的工作。
### Innovation
本研究提出了一种名为RzenEmbed的统一框架，可以适用于文本、图像、视频和视觉文档等多种模态。采用了创新的两阶段训练策略，包括难度加权机制和减少假阴性影响的方法来增强模型的区分能力和指令遵循能力，并且通过学习温度参数和模型混合进一步提升性能。
### Conclusion
RzenEmbed在MMEB基准测试中建立了新的最先进水平，不仅在整体得分上达到最佳，还特别在视频和视觉文档检索等挑战性任务上超越了所有之前的成果。模型已公开可供使用。
## 391. `cs.CV` - 异质双曲流形上基于树结构的模态对齐 [PDF](https://arxiv.org/pdf/2510.27391), [HTML](https://arxiv.org/abs/2510.27391)
### Authors
Wu Wei,Xiaomeng Fan,Yuwei Wu,Zhi Gao,Pengxiang Li,Yunde Jia,Mehrtash Harandi
### Background
模态对齐对于视觉语言模型（VLMs）整合跨模态信息至关重要。然而，现有的方法是从文本中提取层次特征，而用单个特征表示每张图像，这导致了对称性和优化性不足的对齐。
### Innovation
本文提出了基于树结构的模态对齐方法——Alignment across Trees（TAT），该方法构建并调整了图像和文本模态的树状层次特征。利用跨注意力机制从中间Transformer层的视觉类别标记中提取具有从粗到细语义的视觉特征，并嵌入具有不同曲率的双曲流形中以有效地建模层次结构。通过在不同曲率的异质流形上定义KL距离度量来实现流形对齐，并学习一个中间流形来最小化距离。论文证明了最优中间流形的存在性和唯一性。
### Conclusion
在多个图像数据集上的税onomic开放集分类任务实验表明，本文方法在少量样本和跨域设置下始终优于强有力的基线。
## 392. `cs.CV` - FPS: 基于前向传播的参数选择方法，用于高效的微调 [PDF](https://arxiv.org/pdf/2510.27359), [HTML](https://arxiv.org/abs/2510.27359)
### Authors
Kenneth Yang,Wen-Li Wei,Jen-Chun Lin
### Background
参数高效微调（PEFT）已经成为将大型预训练模型适应下游任务的关键策略，但现有方法存在显著局限性。添加基方法，如适配器，引入了推理延迟和工程复杂性；选择基方法，如基于梯度参数选择（GPS），需要完整的向后传递，导致内存使用量与全微调相同。这些缺点阻碍了实际高效微调的应用。
### Innovation
我们提出了基于前向传播的参数选择（FPS），这是一种无需梯度的方法，能够在单次前向传递中识别最优参数子集。FPS 根据参数幅度和相应输入激活的乘积进行参数排名，结合预训练知识和下游数据。在 FGVC 和 VTAB-1k 的 24 个视觉任务上，FPS 达到了与最先进的方法相当的效果，同时降低了近 9 倍的峰值内存使用量并加速参数选择约 2 倍，提供了一种真正高效且实用的大型预训练模型微调解决方案。
### Conclusion
FPS 提供了一种无梯度、单次前向传递的参数选择方法，有效解决了传统方法中的效果、内存和效率问题，为大型预训练模型的高效微调提供了实际可行性。
## 393. `cs.CV` - 使用LoRA和Wan2.1 I2V的小数据管道对开源视频扩散变压器进行微调以合成影视场景 [PDF](https://arxiv.org/pdf/2510.27364), [HTML](https://arxiv.org/abs/2510.27364)
### Authors
Meftun Akarsu,Kerem Catay,Sedat Bin Vedat,Enes Kutay Yarkan,Ilke Senturk,Arda Sar,Dafne Eksioglu
### Background
该研究提供了一个实用的流程，用于从少量数据集微调开源视频扩散变换器，以生成适用于电视和电影制作的电影级场景。该方法将视觉风格学习与运动生成解耦，旨在通过最小化数据集来提高生成场景的一致性和风格保真度，尤其是在高效率和高质量一致性方面.
### Innovation
提出的两阶段过程将视觉风格学习与运动生成分离。第一阶段使用低秩适应（LoRA）模块集成到Wan2.1 I2V-14B模型的交叉注意力层中，以便通过紧凑的含短片段的训练集以高效的方式在单个GPU上实现域适配。第二阶段利用微调后的模型产生风格一致性关键帧，并通过模型的视频解码器进行时间扩展，以生成连贯的720p序列。此外，研究还提出了轻量级并行和序列分割策略来加速推理过程而不降低成本。定量评估和定性评估表明，在保持优质用户研究的支持下，该方法在电影准确性及其时间稳定性方面优于基模型的具体优势.
### Conclusion
该完整训练和推理管道被发布以支持可重复性和跨影视领域的适应。结果表现为可测量的电影准确性和时间稳定性的提升，证明了该方法的有效性。
## 394. `cs.CV` - 谁会失败于你的算法？MAMA-MIA 数据集中的年龄与种族偏差调查 [PDF](https://arxiv.org/pdf/2510.27421), [HTML](https://arxiv.org/abs/2510.27421)
### Authors
Aditya Parikh,Sneha Das,Aasa Feragen
### Background
深度学习模型旨在改进诊断流程，但其公平性评估在超越分类任务（如图像分割）方面仍未得到充分探索。未解决的分割偏差可能导致某些人群医疗质量的差异，并可能在临床决策点累积，通过迭代模型开发进一步放大。为了评估自动化分割标签的公平性，本文审计了MAMA-MIA乳腺癌肿瘤分割数据集中的自动化分割质量，依据年龄、种族和数据源进行评估。分析发现了年轻人患者在分割中的内在年龄相关偏差，即使在控制混杂因素（如数据源）后该偏差仍然存在。研究表明，这种偏差可能与生理因素相关，这是对放射科医生和自动化系统的一个已知挑战。此外，将来自多个数据源的数据进行聚合可能会引发特定站点的种族偏差，强调了对数据进行细致调查的必要性。
### Innovation
本文通过审计MAMA-MIA乳腺癌肿瘤分割数据集的自动化分割标签公平性，首次对图像分割中年龄与种族偏差进行了系统性评估，揭示了自动化系统在分割中的内在偏差。此外，研究表明，多种数据源的聚合可能加剧特定站点的种族偏差，强调了对数据需进行细致的层面分析。这为后续研究和改进自动化医疗诊断系统的公平性提供了新的视角和方法。
### Conclusion
尽管在控制混杂因素后仍有年龄相关的偏差存在，但本文对分割标签公平性的审计揭示了自动化系统在处理年轻患者时的内在内在偏差。这种偏差可能与生理因素相关，单纯依赖图像数据进行分割可能会忽略此类因素的影响。将来自不同数据源的数据聚合后，特定站点的种族偏差可能会加剧，因此需要对多源数据进行全面细致的分析，以减少自动化医疗诊断系统的潜在不公平性。
## 395. `cs.CV` - 一种稳健的深度假信息检测的深度学习和取证混合方法 [PDF](https://arxiv.org/pdf/2510.27392), [HTML](https://arxiv.org/abs/2510.27392)
### Authors
Sales Aribe Jr
### Background
生成对抗网络（GANs）和扩散模型的迅速发展使得合成媒体越来越真实，引发了社会对信息误导、身份欺诈和数字信任问题的担忧。现有的深度造假检测方法或者依赖于深度学习，但该方法容易泛化差且对于畸变敏感；或者依赖于法医学分析，法医学分析方法具有可解释性，但对新型造假技术的检测能力有限。
### Innovation
这项研究提出了一种混合框架，将法医学特征（如噪声残差、JPEG压缩痕迹和频域描述符）与卷积神经网络（CNN）和视觉变换器（ViT）的深度学习表示相结合。该模型在基准数据集（FaceForensics++、Celeb-DF v2、DFDC）上的评估结果表明，相比于单一方法基线和现有的最先进的混合方法，该模型在F1分数上表现更优，分别为0.96、0.82和0.77。此外，该模型在压缩、对抗扰动和未见过的修改下的鲁棒性测试表现稳定。
### Conclusion
解释性分析表明，Grad-CAM和法医学热图在82%的情况下与真实修改区域重叠，提升了透明度和用户信任。这些结果证实，混合方法提供了一种平衡解决方案，结合了深度模型的适应性和法医学提示的可解释性，以开发出更加可靠和值得信赖的深度假信息检测系统。
## 396. `cs.CV` - DeblurSDI：使用自我扩散进行盲图像去模糊 [PDF](https://arxiv.org/pdf/2510.27439), [HTML](https://arxiv.org/abs/2510.27439)
### Authors
Yanlong Yang,Guanxiong Luo
### Background
盲图像去模糊是一个难题，由于未知的锐化图像和模糊核，这是一个病态的逆问题。传统方法依赖手工设计的先验知识，而现代深度学习方法通常需要大量的外部数据进行预训练，这限制了它们在现实场景中的适应性。
### Innovation
DeblurSDI 是一个零样本自监督框架，基于自我扩散机制。它不需要任何先验训练即可执行盲去模糊。该框架将盲去模糊过程表述为从纯噪声开始并逐渐细化解决方案的迭代反向自我扩散过程。关键创新在于噪声调度机制，该机制稳定了优化过程，并提供了对模糊核大小变化的显著鲁棒性，从而允许 DeblurSDI 动态地学习针对输入图像的特定先验。
### Conclusion
广泛的实验表明，DeblurSDI 在各种退化场景下始终能够获得优越的表现，即使在高度退化的条件下也能恢复锐化的图像和准确的模糊核。
## 397. `cs.CV` - CoMViT：低资源医学影像监督分类的高效视觉骨干 [PDF](https://arxiv.org/pdf/2510.27442), [HTML](https://arxiv.org/abs/2510.27442)
### Authors
Aon Safdar,Mohamed Saadeldin
### Background
Vision Transformers (ViTs) 在医学成像方面展现了强大的潜力，但由于其高计算需求和对小数据集的容易过拟合问题，实际临床场景中的应用受到限制。
### Innovation
本文介绍了CoMViT，一种专为资源受限医学图像分析优化的紧凑和可移植的Vision Transformer架构。CoMViT结合了卷积分词器、对角掩码、动态温度缩放和基于池化的序列聚合技术，以提高性能和泛化能力。通过系统性的架构优化，CoMViT在十二个MedMNIST数据集上取得了稳健的表现，同时保持了轻量级的设计（仅约4.5M参数），其性能甚至优于更深的CNN和ViT变体，参数减少了5-20倍而不损失准确性。质性的Grad-CAM分析显示，尽管体积小，但CoMViT仍然能够关注到临床相关的区域。
### Conclusion
CoMViT的设计和性能表明，有原则的ViT重新设计有可能开发出高效且可解释的模型，以适应资源有限的医学影像环境。
## 398. `cs.CV` - A Multi-tiered Human-in-the-loop Approach for Interactive School Mapping Using Earth Observation and Machine Learning [PDF](https://arxiv.org/pdf/2510.27460), [HTML](https://arxiv.org/abs/2510.27460)
### Authors
Casper Fibaek,Abi Riley,Kelsey Doerksen,Do-Hyung Kim,Rochelle Schneider
### Background
本研究提出了一个多层级的人工在环框架，用于交互式学校制图。该框架旨在提升教育设施记录的准确性和完整性，特别是在学校数据稀缺且更新不频繁的发展中国家。该框架采用多层次的方法，结合机器学习和地球观测技术进行分析。
### Innovation
创新点在于该研究提出了一种多层次的人工在环框架，利用机器学习和地球观测技术，通过多级筛选和验证过程，精确定位并生成学校的位置。关键在于后续层级使用中高分辨率卫星图像和深度学习模型进行精细匹配，确保结果的准确性和完整性。
### Conclusion
初步评估表明，多层次策略提供了一种可扩展且成本效益高的解决方案，支持教育基础设施的规划和资源分配。该研究强调了人工介入的重要性，确保在自动化分析结果中的准确性和可靠性。
## 399. `cs.CV` - 从像素到路径：基于多代理框架的可编辑科学插图 [PDF](https://arxiv.org/pdf/2510.27452), [HTML](https://arxiv.org/abs/2510.27452)
### Authors
Jianwen Sun,Fanrui Zhang,Yukang Feng,Chuanhao Li,Zizhen Li,Jiaxin Ai,Yifan Chang,Yu Dai,Kaipeng Zhang
### Background
科学插图需要高度的信息密度和后编辑能力。然而，当前的生成模型存在两个主要问题：第一，图像生成模型输出的是无语义结构的像素图像，无法访问、编辑或重新排列图像中的独立视觉组件；第二，基于代码的生成方法（如TikZ或SVG），虽然提供了元素级别的控制，但用户需经历“编写-编译-审查”的繁琐过程，且缺乏操作的直观性。这些方法都不能很好地满足科学创作中的效率、直观性以及迭代修改的需求。
### Innovation
提出了一种名为Vis Painter的多代理体系框架，结合模型上下文协议，通过协调三个专门模块——管理器、设计师和工具箱——来共同生成与标准向量图形软件兼容的图表。这种模块化、角色分工的设计允许每个元素被明确表示和操作，支持真正的元素级控制，并允许后期添加和修改元素。此外，还引入了一个名为VisBench的基准测试，使用七个维度的评估指标系统地评价科学插图的质量，包括内容、布局、视觉感知和交互成本。还进行了详细的消融实验，验证了架构的合理性和评估方法的可靠性。并对多种视觉语言模型进行了评估，提供公平且可信的模型排名，并详细比较了它们各自的性能。
### Conclusion
通过系统评估，研究人员发现Vis Painter能够有效提高科学插图的质量，其引入的多代理框架能够显著提升插图的可编辑性和效率。同时，还定量并量化了角色分工、步骤控制和描述对插图质量的影响。
## 400. `cs.CV` - Referee: 参考驱动的音视频Deepfake检测 [PDF](https://arxiv.org/pdf/2510.27475), [HTML](https://arxiv.org/abs/2510.27475)
### Authors
Hyemin Boo,Eunsang Lee,Jiyoung Lee
### Background
由于先进生成模型生成的Deepfakes迅速构成了严重威胁，现有的音频视频Deepfake检测方法难以泛化到未见过的伪造内容。
### Innovation
提出了一种新颖的参考驱动的音频视频Deepfake检测方法叫做Referee。该方法利用单一示例的讲者特定线索来检测超越时空特征的篡改。通过跨模态特征中的身份相关查询的匹配与对齐，Referee联合推理音频视频同步性和身份一致性。
### Conclusion
在FakeAVCeleb、FaceForensics++和KoDF上进行的实验表明，Referee在跨数据集和跨语言评估协议上达到最先进的性能。实验结果强调了跨模态身份验证在未来Deepfake检测中的重要性。代码可在该网址获取。
## 401. `cs.CV` - ThinkMorph: 具备涌现能力的多模态交替推理链式思维 [PDF](https://arxiv.org/pdf/2510.27492), [HTML](https://arxiv.org/abs/2510.27492)
### Authors
Jiawei Gu,Yunzhuo Hao,Huichen Will Wang,Linjie Li,Michael Qizhe Shieh,Yejin Choi,Ranjay Krishna,Yu Cheng
### Background
多模态推理需要在语言和视觉之间进行迭代协调，但尚未明确哪些构成有意义的交替推理链。过去研究认为，文本和图像思维应该是互补而非同构的模态，彼此促进推理过程。为了解决这一问题，作者提出了ThinkMorph模型，并在其上进行了24000个高质量交替推理痕迹的微调。该模型旨在生成逐步的文本-图像推理步骤，具体操作视觉内容，同时保持一致的口头逻辑。
### Innovation
ThinkMorph是一个统一模型，通过增强迭代语义推理和视觉内容编辑，有效解决了交替推理链中的非匹配和不连贯问题。它在视觉集中基准上取得了显著提升（平均提高34.7%），并能扩展到新领域任务，甚至超过大型专有视觉-语言模型。此外，ThinkMorph展示了多模态涌现智能，包括看不见的视觉操作技巧、不同推理模式的动态切换以及更好的测试时间扩展。
### Conclusion
研究结果表明，统一模型在多模态推理中的涌现能力具有明确的方向和潜力。未来的研究可以尝试进一步优化这种模型的训练策略和应用范围，以更好地理解和促进多模态推理的发展。
## 402. `cs.CV` - Context-Gated Cross-Modal Perception with Visual Mamba for PET-CT Lung Tumor Segmentation [PDF](https://arxiv.org/pdf/2510.27508), [HTML](https://arxiv.org/abs/2510.27508)
### Authors
Elena Mulero Ayllón,Linlin Shen,Pierangelo Veltri,Fabrizia Gelardi,Arturo Chiti,Paolo Soda,Matteo Tortora
### Background
准确的肺部肿瘤分割对于提高诊断和治疗规划至关重要，而有效结合来自PET和CT的解剖和功能信息仍然是一个主要挑战。
### Innovation
提出了一种名为vMambaX的轻量级多模态框架，通过Context-Gated Cross-Modal Perception Module (CGM) 有效融合PET和CT扫描图像。该模型能够自适应增强跨模态特征交互，强调信息区域并抑制噪声，同时具有较低的计算复杂性。
### Conclusion
该模型在PCLT20K数据集上的评估结果表明，自适应跨模态门控在多模态肿瘤分割中的有效性，并展示了vMambaX作为高效且具有扩展性的框架，在肺部癌症高级分析方面巨大的潜力。
## 403. `cs.CV` - NAUTILUS: 一种用于水下场景理解的大规模多模态模型 [PDF](https://arxiv.org/pdf/2510.27481), [HTML](https://arxiv.org/abs/2510.27481)
### Authors
Wei Xu,Cheng Wang,Dingkang Liang,Zongchuang Zhao,Xingyu Jiang,Peng Zhang,Xiang Bai
### Background
水下探索对于了解我们的星球和其在资源勘探、国家安全等方面更广泛的应用越来越受到关注。水下场景理解任务要求从多粒度进行多任务感知。然而，缺乏大规模的水下多任务指令调优数据集阻碍了这一研究的进步。NAUTILUS项目通过构建包含145万张图像-文本对的数据集NautData，支持八项水下场景理解任务，填补了这一空白。
### Innovation
NAUTILUS引入了从水下成像模型中派生的物理先验，并提出了一种插件视频特征增强（VFE）模块，以明确恢复清晰的水下信息，增强了水下场景理解的鲁棒性。将VFE模块整合到知名的baseline模型LLaVA-1.5和Qwen2.5-VL，并构建了水下多模态模型NAUTILUS。实验表明VFE模块在大多数支持的任务上均能提升baseline模型的性能，从而证明了NAUTILUS在水下场景理解领域的优越性。
### Conclusion
通过NautData数据集和VFE模块的开发，NAUTILUS在水下场景理解上展示出了显著的性能提升，证明了模型的优越性。
## 404. `cs.CV` - MapSAM2：将SAM2适应于历史地图图像和时间序列自动分割 [PDF](https://arxiv.org/pdf/2510.27547), [HTML](https://arxiv.org/abs/2510.27547)
### Authors
Xue Xia,Randall Balestriero,Tao Zhang,Yixin Zhou,Andrew Ding,Dev Saini,Lorenz Hurni
### Background
历史地图是独一无二且有价值的档案，它们记录了不同时间段的地理特征。然而，由于历史地图具有广泛的样式变化和标注训练数据稀缺，使用自动化方式进行历史地图图像分析仍是一个重大挑战。构建跨越历史地图时间系列的数据集更加耗时且劳力密集，因为这需要从多张地图上综合信息。此类数据集对于诸如建筑年代的确定、道路网络及聚落的发展分析、环境变化的研究等应用至关重要。
### Innovation
MapSAM2是一个统一框架，用于自动分割历史地图图像和时间序列。该框架基于视觉基础模型，通过少量的微调即可适应多种分割任务。其主要创新在于将历史地图图像和时间序列视为视频，对图像采用一组小块视作视频的方式处理，从而使记忆注意机制能够结合类似小块的上下文线索，提高几何精度，尤其是对于区域特征。对于时间序列，引入了有标注的Siegfried建筑时间系列数据集，并通过模拟常见的时间变换从单年的地图中生成虚拟时间序列以降低标注成本。
### Conclusion
实验结果显示，MapSAM2能有效地学习时间关联，并且能够在少量监督或使用虚拟视频的情况下准确分割和链接时间序列中的建筑物。作者将发布该数据集和代码以支持未来的研究。
## 405. `cs.CV` - 3D点云中鲁棒版权保护的深度神经水印 [PDF](https://arxiv.org/pdf/2510.27533), [HTML](https://arxiv.org/abs/2510.27533)
### Authors
Khandoker Ashik Uz Zaman,Mohammad Zahangir Alam,Mohammed N. M. Ali,Mahdi H. Miraz
### Background
由于数字媒体中三维内容的快速增长，知识产权保护变得至关重要。与传统的图像或视频不同，点云数据因其独特的几何和非几何攻击极易受到破坏或水印信号被移除，从而给版权保护带来挑战。
### Innovation
本文提出了一种基于深度神经网络的鲁棒水印框架，用于3D点云的版权保护和所有权验证。该框架使用谱分解（SVD）将二进制水印嵌入到点云块的奇异值中，并利用PointNet++神经网络架构的提取能力。网络训练后，即使在旋转、缩放、噪声、裁剪和信号失真等各种攻击下，也能可靠地提取水印。
### Conclusion
实验验证了该方法在可逆嵌入水印方面的有效性，在挑战条件下基于深度学习的提取方法显著优于传统SVD方法。深度学习方法在位准确度和IoU方面分别达到了0.83和0.80，而SVD方法在Crop（70%）攻击下位准确度为0.58和IoU为0.26。这表明本方法能够在严重失真下实现出色的水印恢复并保持高度保真度。
## 406. `cs.CV` - 向通用视频检索迈进：通过合成多模态金字塔课程进行视频嵌入的泛化 [PDF](https://arxiv.org/pdf/2510.27571), [HTML](https://arxiv.org/abs/2510.27571)
### Authors
Zhuoning Guo,Mingxin Li,Yanzhao Zhang,Dingkun Long,Pengjun Xie,Xiaowen Chu
### Background
当前视频检索范式存在结构上的错配问题，狭窄的基准测试激励了相应的有限数据和单任务训练。这导致了通用能力的抑制，因为缺乏一个定义并要求多维度泛化的诊断性评估。
### Innovation
该论文引入了一种基于评价、数据和建模协同设计的框架。首先，建立了通用视频检索基准（UVRB），包括16个数据集，不仅衡量性能，还诊断任务和领域中的关键能力差距。其次，通过UVRB的诊断引入了可扩展的合成工作流程，生成了155万高质量的数据对以填充所需的语义空间。最后，设计了模态金字塔，通过利用多样化数据中的隐含联系来训练通用视频嵌入器（GVE）。大量实验证明GVE在UVRB上实现了零样本泛化的新记录。
### Conclusion
我们的协同设计框架为超越现有局限性、迈向真正通用的视频检索提供了一条实用的道路。研究还揭示了流行的基准测试并不能很好地预测一般能力，并且部分相关检索是一个需要关注的重要但未被充分认知的场景。
## 407. `cs.CV` - Who Made This? Fake Detection and Source Attribution with Diffusion Features [PDF](https://arxiv.org/pdf/2510.27602), [HTML](https://arxiv.org/abs/2510.27602)
### Authors
Simone Bonechi,Paolo Andreini,Barbara Toniella Corradini
### Background
生成扩散模型的快速发展使得合成图像越来越难以与真实图像区分开来，引发了关于真实性、版权和误导信息的担忧。现有的监督式检测器通常难以在未见过的生成器上泛化，需要大量的标注数据和频繁的重新训练。
### Innovation
该论文提出了一种名为FRIDA（Fake-image Recognition and source Identification via Diffusion-features Analysis）的轻量级框架，利用预训练扩散模型的内部激活进行深fake检测和源生成器归属分析。通过应用k-最近邻分类器来识别扩散特征，无需微调即可实现跨生成器的最先进的性能，同时紧凑的神经模型可以实现精确的源头归属。结果显示扩散表示能够固有地编码生成器特定的模式，为合成图像取证提供了简洁且可解释的基础。
### Conclusion
这些结果表明，扩散表示法本身编码了生成器特有的模式，为合成图像的取证分析提供了一个简单且可解释的基础。该研究提出了一个轻量级的框架，通过扩散特征分析提升了深fake检测和源头归属的准确性，无需额外的训练即可达到最佳性能。
## 408. `cs.CV` - ANCHOR: 将对抗训练与硬采样监督对比学习集成用于鲁棒表征学习 [PDF](https://arxiv.org/pdf/2510.27599), [HTML](https://arxiv.org/abs/2510.27599)
### Authors
Samarup Bhattacharya,Anubhab Bhattacharya,Abir Chakraborty
### Background
神经网络改变了机器认知世界的方式。它们通过梯度学习，逐步调整参数以识别数据中的最具区分性的模式。然而，这一过程中的梯度也能被用来实施细微但不可感知的修改，这些修改可以导致模型做出完全不同的决策，这种现象被称为对抗攻击。对抗攻击通过在图像中添加极细微的变化，使其在人类视觉上保持不变，但也使模型作出错误预测。已有方法无法有效解决这一问题，导致模型的准确性和鲁棒性存在差距。
### Innovation
本文提出了一种名为Adversarially-trained Contrastive Hard-mining for Optimized Robustness (ANCHOR)的框架，该框架结合了监督对比学习和硬正样本挖掘。这种方法使得模型在嵌入空间中学习图形表示，这些表示会使同类图像、其增强版本和受损版本聚类在一起并与不同类的图像区分开来，有助于模型关注稳定、有意义的模式，而非脆弱的梯度线索。在CIFAR-10数据集上，我们的方法在针对PGD-20（ε=0.031）的干净和鲁棒准确性方面取得了令人印象深刻的结果，超过了标准的对抗训练方法。实验结果表明，结合对抗指导和硬挖掘的对比监督有助于模型learn更结构化和鲁棒的表示，缩小了准确性和鲁棒性之间的差距。
### Conclusion
我们的研究结果表明，结合对抗训练和硬挖掘的监督对比学习可通过引导模型学习更稳定和鲁棒的表示，从而提升模型的整体性能，并减少准确性和鲁棒性之间的不协调。
## 409. `cs.CV` - 基于基础模型时代的视图对齐编码的图像哈希 [PDF](https://arxiv.org/pdf/2510.27584), [HTML](https://arxiv.org/abs/2510.27584)
### Authors
Ilyass Moummad,Kawtar Zaher,Hervé Goëau,Alexis Joly
### Background
大规模检索需要紧凑且区分度高的表示。基础模型提供了强大的视觉和多模态嵌入，但在这些高维空间中进行最近邻搜索计算上代价高昂。哈希通过使用二进制代码实现快速汉明距离搜索提供了有效替代方案，但由于现有方案依赖于复杂的工作流、多目标对象设计、为单一学习范例专门化和长训练时间，它们通常很复杂。文章介绍了CroVCA（跨视图码对齐），这是一种简单而统一的原则，用于学习在语义对齐视图中保持一致的二进制代码。单个二元交叉熵损失强制这种对齐，而编码率最大化作为一种反塌陷正则化器，促进平衡和多样的代码。
### Innovation
CroVCA 提出了一种简单统一的原则，用于学习在语义对齐视图中保持一致的二进制代码。它通过单一的二元交叉熵损失强制对齐，并通过编码率最大化作为一种反塌陷正则化器促进平衡和多样化的代码。该方法通过设计一个带有最终批归一化层的轻量级MLP哈希网络HashCoder实现。HashCoder可以在冻结嵌入或通过LoRA微调来适应编码器时使用。
### Conclusion
CroVCA 在图像检索基准测试中取得了最新成果，仅需5个训练周期即可实现。在16位精度下，它特别高效，例如，COCO上的无监督哈希在单个GPU上不到2分钟即可完成，ImageNet100上的监督哈希则大约3分钟完成。这些结果凸显了CroVCA的效率、适应性和广泛适用性。
## 410. `cs.CV` - Spatial-SSRL: 通过自我监督强化学习提升空间理解 [PDF](https://arxiv.org/pdf/2510.27606), [HTML](https://arxiv.org/abs/2510.27606)
### Authors
Yuhong Liu,Beichen Zhang,Yuhang Zang,Yuhang Cao,Long Xing,Xiaoyi Dong,Haodong Duan,Dahua Lin,Jiaqi Wang
### Background
大型视觉-语言模型在空间理解方面仍然存在弱点。现有的监督微调（SFT）和最近的验证奖励强化学习（RLVR）方法依赖昂贵的监督、专业化工具或受限环境，限制了模型规模。这些方法需要大量的标注数据，增加了成本，并限制了模型应用的灵活性和广度。因此，需要一种新的方法来克服这些限制，同时提升模型的空间理解能力。
### Innovation
作者提出了一个新的自我监督的RL框架——Spatial-SSRL，可以从普通RGB或RGB-D图像中直接推导出可验证的信号。Spatial-SSRL制定了五个预训练任务来捕获2D和3D的空间结构，包括混洗块排序、翻转块识别、裁剪块填充、区域深度排序和相对3D位置预测。这些任务提供容易验证且不需要人类或LVLM标注的答案。通过训练， Spatial-SSRL能够显著提高空间推理能力，同时保持通用的视觉能力，这对于视觉-语言模型来说是非常重要的。
### Conclusion
在七个空间理解基准测试中，Spatial-SSRL在图像和视频设置下分别取得了3.89%和4.63%的准确率提升，超过了基于Qwen2.5-VL的基准模型。这意味着简单和内在的监督能够使RLVR在更大规模下实现，并为增强LVLM的空间智能提供了一个实用的路线。
## 411. `cs.CV` - 基于双流扩散的世界模型增强视觉-语言-动作模型 [PDF](https://arxiv.org/pdf/2510.27607), [HTML](https://arxiv.org/abs/2510.27607)
### Authors
John Won,Kyungmin Lee,Huiwon Jang,Dongyoung Kim,Jinwoo Shin
### Background
近期研究表明，将世界建模加入视觉-语言-动作模型（VLAs）可以提升机器人的策略学习表现，但是由于两种模态之间的固有差异，在联合预测下一状态观测和动作序列方面仍面临挑战。
### Innovation
本文提出了一种名为DUST（DUal-STream diffusion）的世界模型增强VLA框架，该框架通过一个明确维护分开模态流同时允许跨模态知识共享的多模态扩散变换器架构来解决模态冲突问题。此外，引入了每个模态独立的噪声扰动和解耦的流匹配损失，使得模型能够在不依赖统一潜在空间的情况下学习双方向联合分布。训练过程中引入的解耦模态联合采样方法还支持测试时的扩展，在不同速率下异步进化动作和视图标记。
### Conclusion
在RoboCasa和GR-1等模拟基准测试上，DUST相比基线方法实现了最高6%的提升，测试时扩展方法还额外提供了2-5%的增益。在具有Franka Research 3的真实世界任务中，DUST成功提升了13%的成功率，证实了其在模拟之外的有效性。此外，行动无视频的预训练在BridgeV2上显著提高了RoboCasa的表现，进一步突显了DUST在大规模VLA预训练的潜力。
## 412. `cs.CV` - Sketch-to-Layout: Sketch-Guided Multimodal Layout Generation [PDF](https://arxiv.org/pdf/2510.27632), [HTML](https://arxiv.org/abs/2510.27632)
### Authors
Riccardo Brioschi,Aleksandr Alekseev,Emanuele Nevali,Berkay Döner,Omar El Malki,Blagoj Mitrevski,Leandro Kieliger,Mark Collier,Andrii Maksai,Jesse Berent,Claudiu Musat,Efi Kokiopoulou
### Background
图形布局生成是一个不断发展中的研究领域，专注于从海报设计到文档等各种类型的美观布局生成。虽然近年来的研究探索了如何集成用户约束来指导布局生成，但这些约束往往需要复杂的规格说明，这降低了用户体验。为了克服这一问题，研究引入了一种新的方法，利用用户提供的素描作为直观的约束条件，从而证明了素描到布局问题是一个值得探索的研究方向。他们提出了一种基于多模态变换器的解决方案，使用素描和内容资产作为输入生成高质量布局。并且，研究介绍了一种新型且有效的方法来大规模生成训练素描，从而训练模型。研究在三个公开的数据集上训练和评估了模型，并展示了它在多种场景下优于最先进的基于约束的方法，提供了更直观的设计体验。为了促进未来的研究，研究还公开了20万个合成生成的素描。这些数据集可以通过提供的链接访问。
### Innovation
该研究提出了一种新的基于素描的多模态布局生成方法。这一方法利用用户提供的素描作为直观的约束条件。研究还开发了一种新的方法来大规模生成训练素描，从而解决了数据集构建成本高的问题。这种方法生成的模型在三个公开数据集上的表现优于现有的基于约束的方法，并提供了更直观的设计体验。研究还提出了大量合成的素描数据供未来研究使用，促进了该领域的进一步研究和发展。
### Conclusion
研究提出了一种创新的基于素描的多模态布局生成方法，有效地解决了现有布局生成方法中用户约束复杂性和数据集构建成本高的问题。通过大规模合成训练素描，研究构建了一个高质量的模型，该模型在多种场景下优于现有的基于约束的方法，提供了更直观的设计体验。该研究为未来的研究提供了大量的合成素描数据，促进了该领域的进一步研究和发展。
## 413. `cs.CV` - VessShape：利用合成图像中的形状先验实现少样本2D血管分割 [PDF](https://arxiv.org/pdf/2510.27646), [HTML](https://arxiv.org/abs/2510.27646)
### Authors
Cesar H. Comin,Wesley N. Galvão
### Background
血管分割在医学图像分析中是一项重要任务，但由于标注数据稀缺和模型在不同成像模态下的泛化能力差，其进展受到阻碍。卷积神经网络（CNN）倾向于学习纹理特征，这限制了它们在新领域中的性能，特别是这些新领域具有不同的视觉特征。
### Innovation
VessShape通过生成大规模的2D合成数据集，利用血管形状偏置在分割模型中灌输形状先验，从而鼓励模型学习形状线索而非纹理。这项方法引入了一个预训练模型，该模型仅需少量样本（四到十个）即可在不同领域中实现强大的少样本分割性能，并且在未见过的领域中具有显著的零样本分割能力。
### Conclusion
研究表明，带有强形状偏置的预训练可以有效地解决数据稀缺问题，并改善血管分割模型的泛化能力。
## 414. `cs.CV` - NegoCollab：一种用于异构协同感知的共同表示协商方法 [PDF](https://arxiv.org/pdf/2510.27647), [HTML](https://arxiv.org/abs/2510.27647)
### Authors
Congzhang Shao,Quan Yuan,Guiyang Luo,Yue Hu,Danni Wang,Yilin Liu,Rui Pan,Bo Chen,Jinglin Li
### Background
协作感知通过感知信息共享来扩展感知范围从而提高任务性能，然而，由于参与的代理可能采用不同的固定感知模型，导致在代理之间共享的中间特征存在领域差异，这些差异会降低协作性能。现有的方法试图通过将特征对齐到共同表示来消除这些差异，但它们通常设定共同表示为某个特定代理的表示，这使得具有显著领域差异的代理难以实现正确的对齐。因此，背景是解决这一挑战以改进异构协同感知性能的必要性。
### Innovation
该论文提出了NegoCollab，一种基于协商的共同表示方法。通过引入谈判者在训练过程中从每个模态代理的本地表示中推导出共同表示，这种方法能够有效减少特性之间的本领域差异，并引入结构对齐损失和实用对齐损失，以监督从本地表示到共同表示的知识转移，从而更好地对齐本地和共同表示，提供更多的多模态信息。
### Conclusion
NegoCollab通过协商过程中的共同表示，成功地解决了异构代理之间的固定感知模型所导致的领域差异问题，提高了协作感知的性能。通过引入特定的损失函数来优化训练过程，增强了多模态信息的融合和对齐性。
## 415. `cs.CV` - Vision Transformer for Robust Occluded Person Reidentification in Complex Surveillance Scenes [PDF](https://arxiv.org/pdf/2510.27677), [HTML](https://arxiv.org/abs/2510.27677)
### Authors
Bo Li,Duyuan Zheng,Xinyang Liu,Qingwen Li,Hong Li,Hongyan Cui,Ge Gao,Chen Liu
### Background
监视中的人再识别（ReID）因遮挡、视角畸变和低质量图像的挑战而受到影响。现有方法大多依赖于复杂的模块，或者仅在清晰的正面图像上表现良好。
### Innovation
提出了一种名为Sh-ViT（Shuffling Vision Transformer）的轻量级且鲁棒的模型，用于处理遮挡的人再识别，通过引入混合模块、适应场景的数据增强和基于DeiT的知识蒸馏来增强适应性，旨在改善监控场景下的人员再识别表现，特别是在遮挡和模糊的情况下更加鲁棒。
### Conclusion
实验结果表明，Sh-ViT在MyTT数据集上实现了83.2%的Rank-1和80.1%的mAP，超越了基线CNN和ViT模型；在Market1501数据集上达到了94.6%的Rank-1和87.5%的mAP，超过最先进的模型，表明Sh-ViT在监控场景中具有强大的再识别能力和实际适用性。
## 416. `cs.CV` - Gaussian Combined Distance: 一种泛化的对象检测度量 [PDF](https://arxiv.org/pdf/2510.27649), [HTML](https://arxiv.org/abs/2510.27649)
### Authors
Ziqian Guan,Xieyi Fu,Pengjun Huang,Hengyuan Zhang,Hubin Du,Yongtao Liu,Yinglin Wang,Qang Ma
### Background
在对象检测中，一个定义良好的相似性度量可以显著提升模型性能。目前，基于IoU的相似性度量是最常用的选择。然而，使用IoU的检测器在检测小对象时表现不佳，因为IoU对位置偏差高度敏感。为此，最近的研究提出了用 Wasserstein Distance 作为替代方案来衡量高斯分布的边界框之间的相似性。但是，我们观察到 Wasserstein Distance 缺乏尺度不变性，这影响了模型的泛化能力。此外，当用作损失函数时，它对中心属性的独立优化导致模型收敛缓慢且检测精度差。为了解决这些问题，我们引入了Gaussian Combined Distance (GCD)。通过分析GCD及其梯度，我们证明了GCD不仅具有尺度不变性，还促进了联合优化，从而提高了模型的定位性能。
### Innovation
我们提出了一种新的度量标准 Gaussian Combined Distance (GCD)，它不仅在梯度分析中被证明具有尺度不变性，还促进了优化过程的联合，从而提高了模型在小目标检测中的定位性能。此外，GCD 在多个数据集上取得了最先进的性能，包括 AI-TOD-v2、MS-COCO-2017 和 Visdrone-2019。
### Conclusion
我们在AI-TOD-v2数据集上的大量实验中展示了GCD作为边界框回归损失函数和标签分配度量的优越性能。此外，在MS-COCO-2017和Visdrone-2019数据集上验证了GCD的通用性，它在不同尺度的数据集上表现优于Wasserstein Distance。
## 417. `cs.CV` - 深度学习去噪解锁操作条件下材料显微镜定量见解 [PDF](https://arxiv.org/pdf/2510.27667), [HTML](https://arxiv.org/abs/2510.27667)
### Authors
Samuel Degnan-Morgenstern,Alexander E. Cohen,Rajeev Gopal,Megan Gober,George J. Nelson,Peng Bai,Martin Z. Bazant
### Background
操作条件下显微镜可以提供有关功能材料动态化学和物理过程的直接见解，但测量噪声限制了有效的分辨率并破坏了定量分析。目前，数值和实验结果中的噪声干扰了对复杂材料内部过程的理解。研究人员需要一种方法直接将无监督深度学习去噪整合到不同的显微镜工作流程中，以提高材料微观结构表征的准确性。
### Innovation
本文提出了一种通用框架，将基于无监督深度学习的去噪整合到不同模态和长度尺度的定量显微镜工作中。通过模拟数据，研究证明深度去噪能够保持物理保真度，引入最小偏差，并减少物理优化方程（PDE）约束优化中模式学习的不确定性。相关实验显示，深度去噪技术在扫描透射X射线显微镜（STXM）、光学显微镜颗粒分割和相分类以及中子成像中，能够减少高达百分之八十的噪声，从而揭示纳米尺度的化学和结构异质性，提高无噪声限制技术的有效性，提升了定量操作期显微成像的能力。
### Conclusion
研究表明，深度去噪是一种强大且模态通用的增强技术，能够推动定量操作期显微成像技术的发展，扩展以往受噪声限制的技术的应用范围。
## 418. `cs.CV` - PETAR：基于掩码感知的视觉语言建模以实现PET自动报告生成的局部发现生成 [PDF](https://arxiv.org/pdf/2510.27680), [HTML](https://arxiv.org/abs/2510.27680)
### Authors
Danyal Maqbool,Changhee Lee,Zachary Huemann,Samuel D. Church,Matthew E. Larson,Scott B. Perlman,Tomas A. Romero,Joshua D. Warner,Meghan Lubner,Xin Tie,Jameson Merkow,Junjie Hu,Steve Y. Cho,Tyler J. Bradshaw
### Background
近期，视觉语言模型（VLMs）取得了显著进展，实现了多模态推理，但大多数医学应用仍局限于二维成像。本文将VLMs扩展到3D正电子发射断层扫描和计算机断层扫描（PET/CT），这一领域特征为大量体积数据、小而分散的病变以及长时间的放射学报告。
### Innovation
本文提出了一种名为PETAR-4B的3D掩码感知视觉语言模型，集成了PET、CT和病变轮廓进行空间定位报告生成，弥合了全球上下文推理与细粒度病灶意识之间的鸿沟，生成临床连贯且局部化的发现。
### Conclusion
全面的自动化和人工评估表明，PETAR在PET/CT报告生成质量上取得了显著提升，促进了3D医疗视觉语言理解的进步。
## 419. `cs.CV` - 阶段性 DMD：区间内基于得分匹配的少量步骤分布匹配蒸馏 [PDF](https://arxiv.org/pdf/2510.27684), [HTML](https://arxiv.org/abs/2510.27684)
### Authors
Xiangyu Fan,Zesong Qiu,Zhuguanyu Wu,Fanzhou Wang,Zhiqian Lin,Tianxiang Ren,Dahua Lin,Ruihao Gong,Lei Yang
### Background
现有的 Distribution Matching Distillation (DMD) 方法能够将评分生成模型高效地转换为单步骤生成器，但其模型容量有限，不能很好地处理复杂的生成任务。直接扩展 DMD 成多步骤蒸馏会增加内存占用和计算深度，可能导致训练不稳定和效率下降。虽然先前工作提出了随机梯度截断作为可能的解决方案，但这种方法会显著减少多步骤蒸馏模型的生成多样性，使其降低到与单步骤模型相似的水平。为了克服这些局限性，提出了一种阶段性 DMD (Phased DMD) 框架，结合了阶段式蒸馏和混合专家 (MoE) 的思想，从而减轻学习难度并增强模型容量。
### Innovation
Phased DMD 引入了两个关键概念：阶段式分布匹配和区间的得分匹配。首先，模型将信噪比 (SNR) 范围划分为子区间，并逐步提高模型的 SNR 水平以更好地捕捉复杂的分布。其次，通过严格的数学推导确保每个子区间的训练目标精确合理。该方法通过蒸馏最先进的图像和视频生成模型，如 Qwen-Image (20B 参数) 和 Wan2.2 (28B 参数) 进行验证，实验结果显示，Phased DMD 保留了生成多样性更好，同时保持关键的生成能力。
### Conclusion
Phased DMD 通过阶段性分布匹配和区间的得分匹配，解决了单步骤和多步骤蒸馏模型中的多样性问题。该方法在图像和视频生成任务中取得了显著的性能提升，代码和模型将开源发布。
## 420. `cs.CV` - 在联合建模分离与消混响优化的复杂数字场景中的视听语音增强 [PDF](https://arxiv.org/pdf/2510.26825), [HTML](https://arxiv.org/abs/2510.26825)
### Authors
Jiarong Du,Zhan Jin,Peijun Yang,Juan Liu,Zhuo Li,Xin Liu,Ming Li
### Background
视听语音增强（AVSE）任务是利用视觉辅助信息从混响音频中提取目标讲话人的语音。在现实场景中，复杂的声学环境常常伴随着各种干扰声音和混响现象。大多数现有方法难以应对复杂条件，导致提取出的语音感知质量低。
### Innovation
本文提出了一种在复杂声学环境中表现良好的有效AVSE系统，具体设计了一种'分离之前进行消混响'的处理管道，该处理管道能够应用于其他AVSE网络。此外，该研究通过在第4届COGMHEAR视听语音增强挑战赛（AVSEC-4）中验证了系统的性能，并在三个客观指标上取得了优异结果，最终在人类主观听音测试中获得第一名。
### Conclusion
本文提出的AVSE系统能够在复杂数字场景中表现良好，特别是在联合建模分离与消混响方面有显著创新。系统的成功验证在比赛中取得了卓越成就，证明了其在复杂声学环境下的有效性和优越性。
## 421. `cs.CV` - 使用显著目标检测识别绕过GDPR的操纵性Cookie弹窗 [PDF](https://arxiv.org/pdf/2510.26967), [HTML](https://arxiv.org/abs/2510.26967)
### Authors
Riley Grossman,Michael Smith,Cristian Borcea,Yi Chen
### Background
本文研究遵循《通用数据保护条例》（GDPR）的Cookie弹窗中是否经常出现美学操纵现象，即设计手法以吸引用户关注可分享个人数据的按钮。作者还评估了这些弹窗是否符合GDPR和本地数据保护机构的建议。研究结果显示，尽管大多数网站的Cookie弹窗符合规定，但45%的合规弹窗中存在美学操纵现象。
### Innovation
研究采用了计算机视觉模型进行显著对象检测，以衡量每个弹窗元素的显著性（即注意力导向性），从而发现了新的美学操纵类型，并发现美学操纵现象更为普遍（38%对先前报道的27%）。研究还探讨了地理位置对Cookie弹窗设计的影响，发现来自欧盟的网站更可能使用美学操纵手段，并且更改设计响应隐私法规的比例更高。
### Conclusion
研究表明，欧盟地区的网站更有可能使用美学操纵手段，并在非欧盟网站中更为频繁地出现这种现象，这反映了它们在面对严格隐私法规时的创新性反应。
## 422. `cs.CV` - 改进电子背散射衍射中Kikuchi模式索引的生成扩散模型协议 [PDF](https://arxiv.org/pdf/2510.26907), [HTML](https://arxiv.org/abs/2510.26907)
### Authors
Meghraj Prajapat,Alankar Alankar
### Background
EBSD通常依赖于Hough变换和字典索引等方法来解释衍射图样并提取晶体取向。然而，在高扫描速度下，由于曝光时间过短，CCD相机的操作灵敏度降低，导致观察图样的信噪比下降，使图样变得嘈杂，从而降低了索引精度。因此，本研究旨在开发生成机器学习模型，用于处理或实时处理Kikuchi图样，以恢复在高扫描速度下获得的嘈杂EBSD图样，这些恢复的图样可用于晶体取向的确定，以提供可靠的索引结果。
### Innovation
研究开发了生成机器学习模型，专注于处理或实时处理Kikuchi图样，旨在在高扫描速度下恢复噪声EBSD图样，从而提高索引精度。值得注意的是，所提出的方法对数据的需求不高，不同于传统机器学习方法。
### Conclusion
通过生成模型提高在短曝光时间（高扫描速度）下捕获的图样的质量，验证了该方法的有效性，证明了其在提高EBSD索引准确性方面的潜力。
## 423. `cs.CV` - LifWavNet: 基于提升小波的网络用于从雷达信号重建非接触式心电图 [PDF](https://arxiv.org/pdf/2510.27692), [HTML](https://arxiv.org/abs/2510.27692)
### Authors
Soumitra Kundu,Gargi Panda,Saumik Bhattacharya,Aurobinda Routray,Rajlakshmi Guha
### Background
非接触式心电图（ECG）重建从雷达信号中提供了一种无干扰的心脏监测方法。现有模型往往依赖固定的波let变换方法，LifWavNet提出了一种基于多分辨分析与综合（MRAS）模型的提升小波网络，能够自适应地捕捉雷达信号特征并合成生理意义的心电图波形，从而提高重建的准确性。
### Innovation
LifWavNet采用了可学习的提升小波变换和逆提升单位，自适应地捕捉雷达信号特征并合成生理意义的心电图波形。此外，引入了多分辨短时傅里叶变换（STFT）损失，以确保心电图重建在时域和频域上的一致性。这些创新显著提高了心电图重建的准确度，并在下游生命体征估计（心率和心率变异性）中表现出色。
### Conclusion
对两个公开数据集的评估表明，LifWavNet在心电图重建和下游生命体征估计方面均优于现有的前沿方法。中间特征可视化结果进一步证明了多分辨分解和合成在雷达到心电图重建中的可解释性。这些结果表明，LifWavNet是一个稳健的雷达基非接触式ECG测量框架。
## 424. `cs.CV` - 从语音生成说话人：基于先验指导和区域精修构建高分辨率说话人脸 [PDF](https://arxiv.org/pdf/2510.26819), [HTML](https://arxiv.org/abs/2510.26819)
### Authors
Jinting Wang,Jun Wang,Hei Victor Cheng,Li Liu
### Background
现有的方法依赖于源图像作为外观参考，并使用源语音生成运动，而本文提出了一种新颖的方法，直接从语音中提取信息，解决了语音到说话人脸转换中的关键挑战。具体地，首先采用了语音到面部肖像生成阶段，使用了语音条件下的扩散模型结合统计面部先验和样本自适应加权模块，以实现高质量的肖像生成。随后，在语音驱动的说话人脸生成阶段，将表情动态（如嘴唇动作、面部表情和眼球运动）嵌入到扩散模型的潜在空间中，并进一步使用区域增强模块优化了唇部同步。为了生成高分辨率的输出，我们集成了一个预训练的基于Transformer的离散代码簿与图像渲染网络，以端到端的方式增强视频帧的细节。实验结果表明，我们的方法在HDTF、VoxCeleb和AVSpeech数据集上优于现有方法。值得注意的是，这是首次能够仅从单一语音输入生成高分辨率和高质量的说话人脸视频的方法。
### Innovation
本文提出了一种新颖的方法，直接从语音中提取信息，解决了语音到说话人脸转换中的关键挑战。首先采取语音到面部肖像生成阶段，使用了语音条件下的扩散模型结合统计面部先验和样本自适应加权模块。在后续的语音驱动的说话人脸生成阶段，嵌入了表情动态，并使用区域增强模块优化了唇部同步。为了生成高分辨率输出，集成了一个预训练的基于Transformer的离散代码簿与图像渲染网络，增强视频帧的细节。
### Conclusion
实验结果证明，我们的方法在HDTF、VoxCeleb和AVSpeech数据集上优于现有方法。此外，这是首次能够仅从单一语音输入生成高分辨率和高质量的说话人脸视频的方法。
## 425. `cs.CV` - 机器人领域的多模态神经符号方法在基于空间推理的视觉接地中的应用 [PDF](https://arxiv.org/pdf/2510.27033), [HTML](https://arxiv.org/abs/2510.27033)
### Authors
Simindokht Jahangard,Mehrzad Mohammadi,Abhinav Dhall,Hamid Rezatofighi
### Background
视觉推理，特别是空间推理，是一个具有挑战性的认知任务，要求理解物体间的关系及其在复杂环境中的交互，特别是在机器人领域。现有的视觉语言模型（VLMs）擅长感知任务，但在细粒度的空间推理方面表现不佳，因为它们依赖于隐式的、基于相关性的推理，并且仅依靠图像信息。
### Innovation
我们提出了一种新的神经符号框架，结合了全景图像和3D点云信息，将神经感知与符号推理相结合，显式地建模空间和逻辑关系。该框架包括一个感知模块用于检测实体并提取属性，以及一个推理模块用于构建结构化场景图，以支持精确和可解释的查询。
### Conclusion
在JRDB-Reasoning数据集上，我们的方法在拥挤的、人类构建的环境中表现出色且可靠，同时保持了轻量级设计，适用于机器人和嵌入式AI应用。
## 426. `cs.CV` - GUI-Rise: 基于结构化推理和历史总结的GUI导航 [PDF](https://arxiv.org/pdf/2510.27210), [HTML](https://arxiv.org/abs/2510.27210)
### Authors
Tao Liu,Chongyu Wang,Rongjie Li,Yingchen Yu,Xuming He,Bai Song
### Background
当前的多模态大型语言模型在GUI导航代理方面取得了进展，但存在跨域泛化能力和有效历史利用不足的问题。本文介绍了一个增强推理框架，系统地融合了结构化推理、动作预测和历史总结。该框架通过监督微调和Group Relative Policy Optimization (GRPO)算法强化学习训练了一个GUI代理GUI-Rise。实验在标准基准上展示了在相同训练数据条件下达到最先进的效果，特别是在跨域场景中的表现尤为突出。这些结果验证了该框架在各种GUI导航任务中维持稳健推理和泛化的能力。
### Innovation
提出了一个增强推理框架，结合了结构化推理、动作预测和历史总结，通过监督微调和GRPO算法训练了一个新的GUI代理GUI-Rise。该框架还采用了专门的奖励机制，直接将摘要质量与后续动作性能联系起来。
### Conclusion
该研究在标准基准上展示了该框架的优越性能，特别是在跨域场景下的表现。这证实了框架在各种GUI导航任务中维持稳健推理和泛化能力方面的能力。
## 427. `cs.CV` - 基于双四元数矩阵分解的脆弱零水印方法 [PDF](https://arxiv.org/pdf/2510.27307), [HTML](https://arxiv.org/abs/2510.27307)
### Authors
Mingcui Zhang,Zhigang Jia
### Background
医学图像在诊断、远程诊断和学术研究中发挥着重要作用，但由于传输和共享过程中的版权所有权风险和内容篡改风险，保护医学图像变得非常重要。现有的零水印技术通过对图像进行无损操作来保护其版权，因此提供了一种理想的方法来保护医学图像的版权和内容篡改检测。
### Innovation
该文提出了一种基于双四元数矩阵分解的脆弱零水印模型。该模型利用双四元数的实部分量与虚部分量之间的操作关系关联原始载体图像与水印图像，并基于双四元数矩阵分解的特性生成零水印信息，从而实现医学图像的版权保护和内容篡改检测。
### Conclusion
提出的基于双四元数矩阵分解的脆弱零水印方法能够有效地保护医学图像的版权并检测其内容篡改，是一种创新的方法。
## 428. `cs.CV` - 从虚假相关性视角看不平衡分类 [PDF](https://arxiv.org/pdf/2510.27650), [HTML](https://arxiv.org/abs/2510.27650)
### Authors
Jakob Hackstein,Sidney Bender
### Background
机器学习中的类别不平衡是一个基本挑战，常常导致分类性能不可靠。现有方法主要关注数据重采样或损失重权方案，未能充分关注类别不平衡对“聪慧汉斯”效应（CH 效应）的影响，即由于少数类的欠定义导致的表现不稳定问题。文章提出一种基于反事实解释的方法，利用可解释AI共同识别和消除不平衡下出现的CH效应，提供了一种新的研究视角.
### Innovation
文章提出了一种新的方法，利用可解释AI识别和消除不平衡数据下出现的“聪慧汉斯”效应，不同于以往主要基于数据重采样或损失重权的方法，文章通过反事实解释展示了这种效应如何在不平衡数据中发生，提供了一种新颖的研究视角.
### Conclusion
文章在三个数据集上实现了与现有方法相当甚至更好的分类性能，并展示了“聪慧汉斯”效应在不平衡数据下的发生机制，强调了从虚假相关性视角研究不平衡分类问题的重要性.
## 429. `cs.CV` - 任务感知的专家软路由方法用于收缩对称性表征学习 [PDF](https://arxiv.org/pdf/2510.27222), [HTML](https://arxiv.org/abs/2510.27222)
### Authors
Jaebyeong Jeon,Hyeonseo Jang,Jy-yong Sohn,Kibok Lee
### Background
传统的表征学习方法分为对称性和收缩性表征学习。对称性表征学习忽略输入变换来编码语义信息，而收缩性表征学习则在表征空间中捕捉变换导致的变异。最近的研究表明，同时学习这两种类型的表征往往对下游任务有益，通常通过使用单独的投影头来实现。然而，这种设计忽视了对称性和收缩性学习之间的共享信息，导致冗余特征学习和模型容量的低效使用。现有方法通过单独的投影头来学习这两种表征，虽然可以提高性能，但未能充分利用两者之间的共享信息。
### Innovation
本文提出了一种新的路由策略——Soft Task-Aware Routing (STAR)，通过将投影头建模为专家来实现任务感知。STAR能够让专家专门捕捉共享信息或任务特定信息，从而减少冗余特征学习。通过降低不变性和收缩性嵌入之间的典范相关性来验证这一效果。实验结果表明，在多种转移学习任务中均取得了持续改进。
### Conclusion
实验结果表明，STAR策略在各种转移学习任务中均显示出一致的改进效果。该方法能够降低模型冗余学习，更高效地利用模型容量，从而提升整体性能。相关的代码可以在指定网址获取。
## 430. `cs.CV` - 通过对比触发学习在基于MLLM的具身决策中针对视觉后门攻击 [PDF](https://arxiv.org/pdf/2510.27623), [HTML](https://arxiv.org/abs/2510.27623)
### Authors
Qiusi Zhan,Hyeonjeong Ha,Rui Yang,Sirui Xu,Hanyang Chen,Liang-Yan Gui,Yu-Xiong Wang,Huan Zhang,Heng Ji,Daniel Kang
### Background
多模态大语言模型(MLLMs)通过使具身代理能够直接从视觉输入中获取知觉、推理和规划任务导向行动，促进了具身代理的发展。然而，这种视觉驱动的具身代理打开了一个新的攻击面，即视觉后门攻击，攻击者在特定视觉触发出现时，使代理执行指定的多步骤政策。现有的研究对这种攻击的防范不足，尤其是在面对广泛变化的视觉触发时。为解决这一问题，本文提出了BEAT框架，能够将这种视觉后门注入基于MLLM的具身代理系统中，通过使用环境中的对象作为触发器，这种触发器在视角和光照方面表现出广泛的差异性，难以可靠地植入。
### Innovation
BEAT创新性地通过以下两个方面解决了嵌入感知不稳定的挑战：(1) 构建包含多种场景、任务和触发位置的训练集，使代理暴露于触发变化；(2) 引入了两阶段训练方案，首先进行有监督的微调(SFT)，然后是作者提出的新型对比触发学习(CTL)。CTL将触发物的区分视为具有触发和无触发输入之间偏好的学习过程，明确地优化决策边界的锐度以确保精确的后门激活。
### Conclusion
通过多个具身代理基准和MLLMs的实验表明，BEAT可获得高达80%的攻击成功率，同时保持良好的良性任务表现，并能够可靠地泛化到离分布的触发位置。此外，与简单的SFT相比，CTL在有限的后门数据下，可以将后门激活的准确性提高39%。这些发现揭示了基于MLLM的具身代理中一个至关重要的但未被探索的潜在安全风险，强调了在实际部署前需要构建更坚实的防御体系的重要性。
## 431. `cs.CV` - 暗场X射线成像显著提高基于深度学习的预临床模型中合成早期肺癌肿块检测 [PDF](https://arxiv.org/pdf/2510.27679), [HTML](https://arxiv.org/abs/2510.27679)
### Authors
Joyoni Dey,Hunter C. Meyer,Murtuza S. Taqi
### Background
低剂量计算机断层扫描（LDCT）是肺癌筛查的当前标准，但在许多地区其采用和可访问性有限。许多地方缺乏LDCT基础设施，即使在筛查中，早期肺癌的检测也会产生较高的假阳性率，如在国家肺癌筛查试验（NLST）中，其灵敏度为93.8%，假阳性率为26.6%。暗场X射线成像（DFI）作为一种对肺泡微结构的小角度散射敏感的方法，且较少受到器官阴影干扰，旨在通过与深度学习分割结合，提高早期肺癌检测的准确性。
### Innovation
研究提出了一种新的技术，即利用暗场X射线成像（DFI）与深度学习分割结合的方法，用于检测肺癌早期病变。具体创新点在于：1) DFI技术能有效探测微小结构的散射，减少器官阴影影响；2) 通过训练U-Net分割网络，实现对合成不规则边界和物理对比度的早期肺癌肿块的检测，显示出比传统衰减成像更高的灵敏性和准确性；3) 结合ATTN和DFI输入提高了检测的准确性和特异性。
### Conclusion
研究表明，单独使用DFI技术可以达到83.7%的真阳性检测率，而传统衰减成像仅为51%，且保持了相当的特异性（90.5% vs 92.9%）。结合ATTN和DFI输入则可实现79.6%的灵敏度和97.6%的特异性。总之，DFI技术显著改善了早期肺癌检测的可及性和准确性，且作为LDCT不可用情况下的低成本、低剂量替代方案具有潜力。
## 432. `cs.CV` - 连续视觉-语言导航 [PDF](https://arxiv.org/pdf/2403.15049), [HTML](https://arxiv.org/abs/2403.15049)
### Authors
Seongjun Jeong,Gi-Cheon Kang,Seongho Choi,Joochan Kim,Byoung-Tak Zhang
### Background
目前的视觉-语言导航（VLN）代理开发通常采用“训练一次、部署一次”的策略，但在实际应用中，部署的代理要持续遇到新的环境，这使得该策略不切实际。为了解决这个问题，作者提出了一种植入视觉-语言导航（CVLN）范式，重点在于代理能够在多个场景领域中逐步学习和适应。CVLN包括两种设置：基于初始指令的CVLN（用于指令跟随）和基于对话的CVLN（用于对话引导的导航）
### Innovation
提出了连续视觉-语言导航（CVLN）范式，并提供了两种简单的高效基线：困惑度回放（PerpR）和情景自我回放（ESR）。前者通过回放困难的导航示例，重新利用难以解决的问题场景；后者在训练过程中存储和回顾动作概率，以提升策略的性能。研究发现，现有的连续学习方法在CVLN场景中表现不佳，而PerpR和ESR则通过有效利用重放内存实现了更好的表现
### Conclusion
现有方法在面向连续学习的视觉-语言导航（CVLN）任务中表现不佳，而提出的困惑度回放（PerpR）和情景自我回放（ESR）基线方法则能够通过有效利用重放内存提高性能
## 433. `cs.CV` - EF-3DGS: 事件辅助自由轨迹3D高斯点 [PDF](https://arxiv.org/pdf/2410.15392), [HTML](https://arxiv.org/abs/2410.15392)
### Authors
Bohao Liao,Wei Zhai,Zengyu Wan,Zhixin Cheng,Wenfei Yang,Tianzhu Zhang,Yang Cao,Zheng-Jun Zha
### Background
场景重建在现实场景中有广泛应用。基于不同可微渲染技术的最新进展，一些方法尝试同时优化场景表示（如NeRF或3DGS）和摄像头姿态。尽管有所进步，但依赖传统摄像头输入的方法在高速（或等效低帧率）场景中容易失败。借鉴生物视觉原理，事件摄像头记录像素级别的强度变化，具有高时间分辨率，在盲帧间隔中提供有价值的场景和运动信息。因此，引入事件摄像头有助于首次从随意拍摄的视频中构建场景。
### Innovation
本文提出了事件辅助自由轨迹3D高斯点技术（EF-3DGS），通过三个关键组件整合事件摄像头的优势。第一，使用事件生成模型（EGM）融合事件和帧，监督通过事件流观察到的渲染视角。第二，采用对比最大化框架（CMax）来提取运动信息，从而校准估计的姿态。此外，基于线性事件生成模型（LEGM），IWE中的亮度信息也被用于在梯度域中约束3DGS。第三，为了缓解事件中缺少颜色信息的问题，引入透射光度捆绑调整（PBA）确保事件和帧之间的一致性。
### Conclusion
我们在公共Tanks and Temples基准和新收集的实世界数据集RealEv-DAVIS上评估了我们的方法。
## 434. `cs.CV` - GASP: Gaussian Splatting for Physic-Based Simulations [PDF](https://arxiv.org/pdf/2409.05819), [HTML](https://arxiv.org/abs/2409.05819)
### Authors
Piotr Borycki,Weronika Smolak,Joanna Waczyńska,Marcin Mazur,Sławomir Tadeja,Przemysław Spurek
### Background
物理模拟对于各种现实世界应用中的3D场景建模和利用至关重要。然而，将物理模拟与先进的3D场景渲染技术（如高斯点绘制（GS））集成仍然具有挑战性。现有的模型依赖于额外的网格机制，如三角形或四面体网格、行进立方体或笼模型。相比之下，我们可以通过修改基于物理的牛顿力学来与3D高斯成分对齐。当前模型通常采用变形图的近似方法，通过局部线性变换近似动力学。研究中提出的GASP（基于物理的高斯绘制）流水线使用参数化平面高斯分布，将使用物理引擎建模高斯成分的问题简化为处理3D点的问题。
### Innovation
GASP流水线通过使用参数化平面高斯分布，将物理引擎中建模高斯成分的问题简化为处理3D点的问题。它包括新的规则用于操作高斯分布，适应流水线以包含网格，控制模拟中的高斯尺寸，并提高模拟效率。核心创新点在于引入的高斯分组策略，实现了层次化结构化，使得模拟能够在选择的高斯上独立进行。该解决方案可以与任何作为黑盒形式的物理引擎集成。
### Conclusion
我们展示了所提出的流水线在一系列用于3D对象渲染的基准数据集上表现出优越性能。项目网页包括额外的可视化内容，可以帮助更直观地理解这一方法。
## 435. `cs.CV` - SRAGAN: 增强了基于显著性图像和注意机制的生成对抗网络用于中国水墨画风格转移 [PDF](https://arxiv.org/pdf/2404.15743), [HTML](https://arxiv.org/abs/2404.15743)
### Authors
Xiang Gao,Yuqi Zhang
### Background
最近的研究主要依赖生成对抗网络（GAN）进行跨域图像到图像（I2I）转换。问题的核心在于如何将目标领域的风格模式转移到源领域的内容图像上。本文讨论了一个特定的应用场景：将现实照片转化为传统的中国水墨画的风格转移问题。现存的许多I2I模型虽然能够处理该问题，但一个显著的挑战是，源图像的内容细节有可能因为水墨风格元素的转移而被抹去或破坏。因此，为了应对这一问题，作者提出将显著性检测纳入未配对的I2I框架中，以便规范化图像内容。在生成模型中引入显著性后，提出了显著性交并比（SIOU）损失来明确规范对象内容结构；并且提出了一种显著性自适应归一化（SANorm）机制，通过动态地将图像显著性信息注入生成器以指导风格化过程来隐式增强生成绘画中的对象结构完整性。此外，还提出了显著性注意力判别器，利用图像显著性来集中生成对抗网络的注意力于所绘制的对象上，有助于生成更生动细腻的笔触和水墨纹理。通过广泛的定性和定量实验，作者的这种方法在GAN范式和扩散模型范式中均优于相关先进的图像风格化方法。
### Innovation
1. 引入显著性检测机制，以显著性交并比（SIOU）损失约束对象内容结构；2. 提出显著性自适应归一化（SANorm）机制，动态注入图像显著性信息以指导风格生成过程；3. 引入显著性注意力判别器，增强了生成的图像细节和纹理的真实性。
### Conclusion
通过大量的实验，表明基于显著性增强的生成对抗网络（SRAGAN）在处理现实图像到中国水墨画风格转换的问题上有着显著的优势。这种方法不仅能够更好地保留内容细节，还能生成更精准、更细腻的艺术效果，比相关方法更为优越。
## 436. `cs.CV` - PROFIT: 专门为深度微调设计的专业优化器 [PDF](https://arxiv.org/pdf/2412.01930), [HTML](https://arxiv.org/abs/2412.01930)
### Authors
Anirudh S Chakravarthy,Shuai Kyle Zheng,Xin Huang,Sachithra Hemachandra,Xiao Zhang,Yuning Chai,Zhao Chen
### Background
预训练模型的微调已成为生成AI、计算机视觉和机器人技术中的普遍现象。虽然有不少研究致力于提高微调模型的效率，但对于专门为提升模型性能而设计的微调算法的研究较少。为填补这一空白，我们提出了PROFIT，一种专门设计用于增量微调已收敛模型的专业优化器。PROFIT 与传统的优化器（如SGD或Adam）不同，后者由于随机初始化而假设较少，PROFIT 则会考虑到已收敛模型的特性来调节优化过程，采用时间梯度正交化过程，PROFIT 在多种任务中表现出色，包括图像分类、多模态语言模型训练以及大规模运动预测。此外，PROFIT 是作为一个模块化的优化器封装的，使得它很容易直接集成到任何训练管道中，不需要过多的工程工作量。
### Innovation
1. 专门为提升模型性能而设计的微调算法。2. 首次将预收敛模型的特性明确纳入微调过程中。3. 采用时间梯度正交化过程进行微调。4. 提高了在各种任务中的性能表现。5. 作为一种模块化优化器，易于集成到任何训练管道中，无需大量工程努力。
### Conclusion
我们提出的PROFIT是一个专门用于增量微调已收敛模型的专业优化器。它通过结合考虑预收敛模型的特性，使得微调过程更为高效且性能更佳。这一优化器为提高各种机器学习任务（包括图像分类、多模态语言模型训练以及大规模运动预测）中的模型性能提供了新的途径。
## 437. `cs.CV` - MixedGaussianAvatar：通过混合2D-3D高斯模型实现逼真且几何上准确的头部avatar重建 [PDF](https://arxiv.org/pdf/2412.04955), [HTML](https://arxiv.org/abs/2412.04955)
### Authors
Peng Chen,Xiaobao Wei,Qingpo Wuwu,Xinyi Wang,Xingyu Xiao,Ming Lu
### Background
高保真3D头部头像在虚拟现实等多应用场景中至关重要。虽然神经辐射场（NeRF）可以生成逼真的头部头像，但其训练和渲染速度较慢。基于3D高斯体的最近方法（3DGS）大幅提高了训练和渲染效率，但其表面一致性导致几何精度不足。随后，基于2D高斯体的（2DGS）方法提升了几何精度，但牺牲了渲染保真度。本文以混合2D/3D高斯体模型为核心，旨在结合2DGS和3DGS的优势，提出一种新颖的方法MixedGaussianAvatar，以实现逼真且几何上准确的头部头像重建。
### Innovation
本文提出了一种名为MixedGaussianAvatar的新型方法，通过结合2D和3D高斯体模型，旨在平衡几何精度和渲染保真度。具体而言，MixedGaussianAvatar利用2D高斯体确保表面几何准确性，并将它们附着于FLAME模型的三角网格上。在渲染质量不足的地方附加3D高斯体，创建混合的2D-3D高斯表征。此外，所提方法采用逐步训练策略，首先训练2D高斯体，再对混合的2D-3D高斯体进行细化调整，统一使用混合的高斯表示方法整合二维图像模态和三维网格模态。
### Conclusion
全面的实验表明了MixedGaussianAvatar方法的优越性。所提出的MixedGaussianAvatar作为一种混合2D-3D高斯体方法，在几何精确度和渲染保真度方面都表现出优秀性能。最终，我们期望该方法在虚拟现实等领域中的应用将大大增强用户体验。该代码将在未来发布。
## 438. `cs.CV` - Semantic Alignment and Reinforcement for Data-Free Quantization of Vision Transformers [PDF](https://arxiv.org/pdf/2412.16553), [HTML](https://arxiv.org/abs/2412.16553)
### Authors
Yunshan Zhong,Yuyao Zhou,Yuxin Zhang,Wanchen Sui,Shen Li,Yong Li,Fei Chao,Rongrong Ji
### Background
DFQ能够在不访问真实数据的情况下进行模型量化，解决了数据安全和隐私问题。随着Vision Transformers (ViTs)的广泛应用，DFQ在ViTs中的应用受到了广泛关注。然而，现有的DFQ方法存在两个局限性：（1）语义失真，合成图像的语义与真实图像差异较大；（2）语义不足，合成图像包含大量内容有限和过度简化的纹理，导致量化性能不佳。
### Innovation
为了克服这些局限，本文提出了SARDFQ，一种新颖的Semantics Alignment and Reinforcement Data-Free Quantization方法用于ViTs。SARDFQ从三个方面进行改进：（1）通过引入Attention Priors Alignment (APA)，优化合成图像以遵循随机生成的结构注意力先验，解决了语义失真问题；（2）通过引入Multi-Semantic Reinforcement (MSR)，利用局部补丁优化增强合成图像中的语义丰富度，解决了语义不足问题；（3）通过Soft-Label Learning (SL)，适应多个语义目标以促进用MSR增强的多语义图像的训练。
### Conclusion
通过大量实验验证，SARDFQ展示了其优越性，显著超过了现有方法。例如，在ImageNet上，SARDFQ对于W4A4 ViT-B的top-1精度提升高达15.52%。完整的代码可从以下链接获取。
## 439. `cs.CV` - DPA: 一种用于分类数据集中测量偏见放大的一站式指标 [PDF](https://arxiv.org/pdf/2412.11060), [HTML](https://arxiv.org/abs/2412.11060)
### Authors
Bhanu Tokas,Rahul Nair,Hannah Kerner
### Background
大多数机器学习数据集存在偏见。在训练模型的过程中，这些偏见不仅会被学到，还可能被放大，这一现象称为偏见放大。目前存在多种基于共现的指标用于测量这类偏见放大，这些指标能够提供细粒度的偏见分析并确定偏见放大的方向，但也有局限性，表现完美的平衡数据集或负偏见放大无法被衡量。为了解决这些问题，最近提出了基于泄露的偏见放大度量（称为泄漏放大），尽管它在一定程度上解决了平衡和非平衡数据集的问题，无法识别偏见放大的方向。针对这一问题，本文提出了一个新的基于预测性的度量，称为方向性预测放大（DPA），DPA具有方向性，适用于平衡和非平衡数据集，并正确地识别正负偏见放大，而且可以一次性消除对模型在多个指标上的评估。DPA相对于之前的方法更加灵敏，能报告在一定范围内的分数，还考虑到数据集偏见通过衡量预测性的相对变化来体现。实验结果表明，DPA是测量分类问题中偏见放大的最可靠指标。
### Innovation
提出了一个新的基于预测性的度量，称为方向性预测放大（DPA），DPA具有方向性，适用于平衡和非平衡数据集，并正确地识别正负偏见放大，而且可以一次性消除对模型在多个指标上的评估。DPA相对于之前的方法更加灵敏，能报告在一定范围内的分数，还考虑到数据集偏见通过衡量预测性的相对变化来体现。
### Conclusion
实验结果表明，DPA是测量分类问题中偏见放大的最可靠指标。为了比较DPA与其他偏见放大度量指标，本文还提供了一个汇总主要偏见放大度量的一站式库。
## 440. `cs.CV` - 流形学习在高光谱图像中的应用 [PDF](https://arxiv.org/pdf/2503.15016), [HTML](https://arxiv.org/abs/2503.15016)
### Authors
Fethi Harkat(EDP, DT),Guillaume Gey(DT),Valérie Perrier(EDP),Kévin Polisano(SVH),Tiphaine Deuberet(DT)
### Background
传统的特征提取和投影技术，如主成分分析（PCA），在表示X射线传输多能源（XRT ME）图像时存在不足，限制了神经网络在决策过程中性能的提升。这主要是因为XRT ME图像中的非线性关系无法被传统方法准确捕捉。为了应对这个问题，提出了一种通过构建临近图来逼近数据流形的方法，该方法使用统一流形近似和投影（UMAP）技术。这种方法能够捕获数据中的非线性关系，显著提升机器学习算法的性能，特别适用于X射线传输光谱高光谱图像（HSI）的处理。这种方法不仅保留了数据的整体结构，还增强了特征的可分离性，从而提高了分类结果的准确性和鲁棒性。
### Innovation
提出了一种通过UMAP技术构建数据流形的方法。该方法能够捕获数据中的非线性关系，显著提升机器学习算法的性能，特别适用于处理X射线传输光谱高光谱图像（HSI），并与传统的特征提取和投影技术相比，该方法能够更好地表示XRT ME图像，提升神经网络在决策过程中性能的提升。
### Conclusion
该方法通过UMAP技术构建数据流形，不仅可以有效保留数据的整体结构，还可以提高特征的可分离性，从而提升机器学习算法在处理X射线传输光谱高光谱图像（HSI）中的分类准确性与鲁棒性。
## 441. `cs.CV` - 使用深度学习进行面部 spoofing 检测 [PDF](https://arxiv.org/pdf/2503.19223), [HTML](https://arxiv.org/abs/2503.19223)
### Authors
Najeebullah,Maaz Salman,Zar Nawab Khan Swati
### Background
数字图像 spoofing 已成为生物特征认证系统中的重大安全威胁，尤其是那些依赖于面部识别的系统。为了增强图像识别系统的安全性，研究人员评估了 MobileNetV2、ResNET50 和 Vision Transformer（ViT）三种基于视觉的模型在图像分类中的 spoof 检测性能，使用了一个包含150,986张图像的数据集，分为训练集（140,002）、测试集（10,984）和验证集（39,574）三部分。
### Innovation
该研究使用深度学习方法，特别是三种不同的模型（MobileNetV2、ResNET50 和 ViT），对面部 spoof 检测中的性能进行了评估。研究通过准确率、精确率、召回率和 F1 值等指标比较了不同模型的效果，结果显示 MobileNetV2 在测试集上表现出更好的性能和更稳定的泛化能力，即便在验证集上也显示了优秀的准确率。此外，研究还指出了 MobileNetV2 在处理新的未知数据时的优势和可靠性。
### Conclusion
MobileNetV2 在 spoof 检测任务中表现出较好的平衡性能和稳健性，特别是在处理新的数据时表现更佳，因此被推荐为可靠的 spoof 检测应用模型。研究强调了在安全敏感的情境下模型选择的重要性，并建议将 MobileNetV2 作为实际部署的实用解决方案。
## 442. `cs.CV` - D$^2$USt3R: 提升动态场景的3D重建效果 [PDF](https://arxiv.org/pdf/2504.06264), [HTML](https://arxiv.org/abs/2504.06264)
### Authors
Jisang Han,Honggyu An,Jaewoo Jung,Takuya Narihira,Junyoung Seo,Kazumi Fukuda,Chaehyun Kim,Sunghwan Hong,Yuki Mitsufuji,Seungryong Kim
### Background
在动态场景下进行3D重建的任务，对象的频繁移动导致了之前为静态3D场景设计的点云回归方法，例如DUSt3R，难以保持高质量重建。虽然这些方法在静态环境中能提供优雅且强大的解决方案，但当存在动态运动破坏基于相机姿态的对齐时，它们表现不佳。
### Innovation
我们提出了$D^2USt3R$，直接回归同时捕捉静态和动态3D场景几何的静态-动态对齐点图（SDAP），并明确结合空间和时间方面，模型成功涵盖了拟议点图的3D密集对应关系，从而提升下游任务的表现。
### Conclusion
通过广泛的实验评估，我们的方法在包含复杂运动的各种数据集上实现了3D重建性能的持续优势。
## 443. `cs.CV` - AMD-Hummingbird: 向高效文本转视频模型迈进 [PDF](https://arxiv.org/pdf/2503.18559), [HTML](https://arxiv.org/abs/2503.18559)
### Authors
Takashi Isobe,He Cui,Dong Zhou,Mengmeng Ge,Dong Li,Emad Barsoum
### Background
文本到视频(T2V)生成最近受到了广泛关注，因为它能够从文本描述合成逼真的视频。然而，现有的模型在实现计算效率和高视觉质量之间面临着挑战，特别是在有限资源的设备上，如iGPUs和移动电话。大多数先前的工作侧重于视觉保真度，而忽视了生成高效且更小模型的需求，这些模型适合实际部署。由于此挑战，本文提出了一种轻量级T2V框架Hummingbird，它通过视觉反馈学习剪枝现有的模型并改善视觉质量。这种方法将U-Net的规模从14亿参数减少到7亿，显著提高了效率同时保留了高质量的视频生成。另外，我们还引入了一种新型的数据处理流水线，利用大规模语言模型（LLMs）和视频质量评估（VQA）模型，增强了文本提示和视频数据的质量。为了支持用户驱动的训练和风格定制，我们公开发布了完整的训练代码，包括数据处理和模型训练。详尽的实验表明，相比同类领先方法，如VideoCrafter2，我们的方法在VBench上实现了31倍的速度提升，同时获得最高的总体得分。此外，我们的方法能够生成多达26帧的视频，解决了现有的基于U-Net的方法在长视频生成方面的局限性。值得注意的是，整个训练过程只需要四个GPU，就能够与现有的领先方法媲美。
### Innovation
我们提出的Hummingbird框架通过剪枝现有的模型，并利用视觉反馈学习来提高视觉质量，成功将U-Net的参数规模从14亿减少到7亿。同时，我们也引入了一种新型数据处理流水线，利用大语言模型（LLMs）和视频质量评估（VQA）模型，提升了文本提示和视频数据的质量。我们公开了完整的训练代码，包括数据处理和模型训练，以支持用户驱动的训练和风格定制。这种方法在速度和质量上都达到了与现有领先方法相当的水平，特别是在长视频生成方面表现优异。
### Conclusion
Hummingbird为T2V生成提供了一种实用且高效的解决方案，兼备高性能、可扩展性和灵活性，适用于实际应用。
## 444. `cs.CV` - NoisyRollout：通过数据增强强化视觉推理 [PDF](https://arxiv.org/pdf/2504.13055), [HTML](https://arxiv.org/abs/2504.13055)
### Authors
Xiangyan Liu,Jinjie Ni,Zijian Wu,Chao Du,Longxu Dou,Haonan Wang,Tianyu Pang,Michael Qizhe Shieh
### Background
强化学习（RL）的进步增强了视觉语言模型（VLMs）的推理能力，但关于如何改善策略探索以更好地扩展测试时计算能力的研究仍相对较少。同时，VLMs 在视觉感知不完美时仍然面临挑战，影响后续的推理过程。
### Innovation
提出了一种名为 NoisyRollout 的简单有效数据增强方法，通过混合干净图像和适量失真图像的训练轨迹，增加感知多样性，促进更好的策略探索和更加稳健的推理。还采用了一个噪声退火计划逐步减弱失真强度，早期有助于探索，后期确保稳定性。
### Conclusion
在两个不同的训练数据集上进行的大量实验表明，NoisyRollout 在5个开放源代码的RL调优模型在5种域外推理和感知基准测试中实现了最先进的性能。并验证了 NoisyRollout 在不同模型大小、数据规模和图像增强类型下的有效性和普遍适用性。
## 445. `cs.CV` - 通过语言驱动的描述属性增强时空零样本动作识别 [PDF](https://arxiv.org/pdf/2510.27255), [HTML](https://arxiv.org/abs/2510.27255)
### Authors
Yehna Kim andYoung-Eun Kim,Seong-Whan Lee
### Background
视觉-语言模型（VLMs）在零样本动作识别方面展示了令人印象深刻的能力，通过学习将视频嵌入与类别嵌入联系起来。然而，仅依赖动作类别提供语义上下文存在显著挑战，特别是由于多语义词的存在，这可能会引入对动作预期概念理解的歧义。
### Innovation
提出了一种创新方法，利用网络抓取的描述，借助大型语言模型提取相关关键词以减少对人工标注员的需求，并消除创建属性数据的繁琐手工过程。此外，引入了一种时空交互模块，专注于对象和动作单元，以实现描述属性与视频内容之间的对齐。
### Conclusion
在我们的零样本实验中，模型取得了显著结果，在UCF-101、HMDB-51和Kinetics-600上分别达到了81.0%、53.1%和68.9%的准确性，证明了模型在各种下游任务中的适应性和有效性。
## 446. `cs.CV` - Sparse Model Inversion: Efficient Inversion of Vision Transformers for Data-Free Applications [PDF](https://arxiv.org/pdf/2510.27186), [HTML](https://arxiv.org/abs/2510.27186)
### Authors
Zixuan Hu,Yongxian Wei,Li Shen,Zhenyi Wang,Lei Li,Chun Yuan,Dacheng Tao
### Background
模型反转旨在从预训练的判别模型中重建原始训练数据，当原始训练数据由于隐私、使用权限或大小限制而不可用时，这一技术特别有用。然而，现有的密集型模型反转方法试图重建整个图像区域，使得它们在反转大型Vision Transformers（视觉转换器）的高分辨率图像时极其低效。
### Innovation
本文识别了密集反转方法低效的两个根本原因：噪声背景的冗余反转以及潜在的虚假关联反转（我们将其称为模型反转中的“幻觉”现象）。为解决这些问题，作者提出了一种新颖的稀疏模型反转策略，这是一种即插即用的扩展方法，可以在不修改原始损失函数的情况下加快现有的密集反转方法。具体来说，该方法选择性地反转语义前景，停止对噪声背景和潜在虚假关联的反转。
### Conclusion
通过理论和实证研究，作者验证了该方法在实现显著的反转加速（最高达到3.79倍）的同时，还可以保持甚至增强下游的无数据模型量化和无数据知识转移的性能。
## 447. `cs.CV` - AVA: 以视觉语言模型实现自主视频分析 [PDF](https://arxiv.org/pdf/2505.00254), [HTML](https://arxiv.org/abs/2505.00254)
### Authors
Yuxuan Yan,Shiqi Jiang,Ting Cao,Yifan Yang,Qianqian Yang,Yuanchao Shu,Yuqing Yang,Lili Qiu
### Background
AI驱动的视频分析在各个领域变得越来越重要，但现有的系统通常受限于特定、预定义的任务，限制了在开放的分析场景中的适应性。最近，视觉语言模型（VLMs）的出现作为变革性技术提供了一个开放视频理解、推理和分析的潜力，然而，它们有限的上下文窗口在处理大量的实际应用场景中也带来了挑战。因此，有必要开发一种能够处理这些挑战并支持开放视频分析系统的解决方案。
### Innovation
提出了AVA，一种基于VLM的系统，设计用于开放的先进视频分析。该系统引入了两项关键创新：（1）事件知识图谱（EKGs）的近实时构建，用于高效地索引长或持续的视频流；（2）一种机构性检索生成机制，利用EKGs处理复杂的多样化查询。
### Conclusion
通过在公共基准（LVBench和VideoMME-Long）上的全面评估，以及新的基准（AVA-100）上达到了顶级表现，AV表现出了超越现有竞争系统（62.3%和64.1%的准确度，其中75.8%的准确度在AV-100上），证明了其在超长时间和开放世界视频场景中的视频分析能力。
## 448. `cs.CV` - 部分相关视频检索中的语义塌陷缓解 [PDF](https://arxiv.org/pdf/2510.27432), [HTML](https://arxiv.org/abs/2510.27432)
### Authors
WonJun Moon,MinSeok Jung,Gilhan Park,Tae-Young Kim,Cheol-Ho Cho,Woojin Jun,Jae-Pil Heo
### Background
现有的部分相关视频检索（PRVR）方法将每个标注的文字-视频对视为正样本，并将所有其他样本视为负样本，忽略了单个视频内部及不同视频之间的丰富语义变化。这种处理方式导致同一视频中不同事件的视频片段嵌入相互靠近，而语义相似但来自不同视频的查询和片段则被驱离，限制了当视频包含多个多样事件时的检索性能。
### Innovation
本文针对此问题，针对文本和视频嵌入空间中提出的语义塌陷问题，首先引入了文本相关性保持学习，该方法保持基础模型中编码的语义关系。为解决视频嵌入中的塌陷问题，提出了一种跨分支视频对齐方法（CBVA），通过对比式对齐方法，在时间尺度上解耦分层视频表示。此外，提出了保持顺序的标记合并和自适应CBVA，以通过产生内部一致但相互区别的视频片段来增强对齐效果。这在PRVR基准测试中显示了有效缓解语义塌陷并显著提高检索准确性的效果。
### Conclusion
我们的框架有效地缓解了语义塌陷，并在PRVR基准测试中大幅提高了检索准确性。
## 449. `cs.CV` - 全景域外分割在自动驾驶中的应用 [PDF](https://arxiv.org/pdf/2505.03539), [HTML](https://arxiv.org/abs/2505.03539)
### Authors
Mengfei Duan,Yuheng Zhang,Yihong Cao,Fei Teng,Kai Luo,Jiaming Zhang,Kailun Yang,Zhiyong Li
### Background
全景成像技术能够捕获超宽视野的360°图像，这对于自动驾驶和增强现实等应用至关重要。然而，现有的全景语义分割方法难以识别异常点，而基于针孔模型的域外分割（Out-of-distribution Segmentation, OoS）方法在全景域的表现并不理想，这主要是因为背景噪音和像素畸变的问题。
### Innovation
文章提出了一个名为全景域外分割（PanOoS）的新任务，并提出了一个名为POS（Panoramic Out-of-distribution Segmentation）的新解法。POS通过文本引导提示分布学习适应全景图像的特点，具体来说，POS将一种去混扰策略引入CLIP的跨域泛化能力，提出了提示驱动恢复注意力（PRA）优化语义解码，并通过语义原型监督来细化每个像素掩码嵌入的流形，提出了双层提示分布学习（BPDL）以提高分割精度。
### Conclusion
广泛实验表明，POS在DenseOoS基准上的AuPRC提高了34.25%，FPR95降低了21.42%，优于最先进的针孔OoS方法。POS还提高了封闭集语义分割的能力，促进了全景理解的进步。相关代码和数据集将公开发布。
## 450. `cs.CV` - C-LEAD：对比学习增强的对抗性防御 [PDF](https://arxiv.org/pdf/2510.27249), [HTML](https://arxiv.org/abs/2510.27249)
### Authors
Suklav Ghosh,Sonal Kumar,Arijit Sur
### Background
深度神经网络（DNNs）在计算机视觉任务如图像分类、分割和物体检测中取得了显著的成功。然而，它们容易受到对抗性攻击的影响，这些攻击可能导致在很小的输入图像扰动下产生错误的预测。因此，解决这一问题是部署 robust 的深度学习系统的关键。迄今为止，对抗性防御领域尚未充分利用对比学习的方法。本文提出了一种新颖的方法，利用对比学习提高对抗防御性能，通过使用干净的和对抗性扰动的图像来增强分类模型的鲁棒性。实验结果显示，该方法在模型对抗性扰动下的鲁棒性显著提高，验证了对比损失有助于提取更加有信息量且抗扰动性更强的特征，为深度学习中的对抗鲁棒性领域带来了新的成果。
### Innovation
本文提出了一种利用对比学习方法进行对抗防御的新颖方案（C-LEAD），该方法通过最大化干净数据和扰动数据之间的差异来优化模型参数。这种方法可以训练出更 robust 的表示，减少对抗性攻击的影响，相较于已有方法，实验表明该方法在对抗性鲁棒性方面更有效。
### Conclusion
我们的研究结果表明，对比损失有助于提取更有信息量且抗扰动性更强的特征，可以有效提高模型对各种类型的对抗性扰动的鲁棒性。这为在深度学习模型中增强对抗鲁棒性提供了新的途径，未来可以进一步探索对比学习在其他深度学习任务中的应用。
## 451. `cs.CV` - 不确定性意识的选择性视觉问答中的变异视觉问答 [PDF](https://arxiv.org/pdf/2505.09591), [HTML](https://arxiv.org/abs/2505.09591)
### Authors
Tobias Jan Wieczorek,Nathalie Daun,Mohammad Emtiyaz Khan,Marcus Rohrbach
### Background
尽管近年来视觉语言模型（VLMs）在视觉问答（VQA）和视觉推理等任务上取得了显著进展，但这些模型仍然容易表现出过度自信和幻觉的现象。贝叶斯方法有潜在的能力通过帮助模型有选择地预测来改善可靠性，即模型只有在足够自信时才进行反应。然而，贝叶斯方法常被视为对大型模型代价高昂且无效，目前关于其在多模态应用中的有效性的证据甚少。
### Innovation
本文创新地展示了变异贝叶斯方法在视觉问答任务中进行选择性预测的有效性和优越性。作者基于深度学习中的变异方法最新进展，提出了一种被称为“变异视觉问答”的方法，该方法提高了模型的校准，并在VQA和视觉推理任务中取得了显著的增益，尤其是在较低的容错率（≤1%）下。此外，作者还提出了一种新的风险规避选择器，该选择器通过考虑预测的方差，优于标准样本平均。
### Conclusion
本文提供了关于变异学习是一种有效的方案，以使大规模VLMs更加安全和可信的有力证明。
## 452. `cs.CV` - 关于条件特征对齐理论在无监督领域自适应计数中的研究 [PDF](https://arxiv.org/pdf/2506.17137), [HTML](https://arxiv.org/abs/2506.17137)
### Authors
Zhuonan Liang,Dongnan Liu,Jianan Fan,Yaxuan Song,Qiang Qu,Runnan Chen,Yu Yao,Peng Fu,Weidong Cai
### Background
现有的目标计数模型在跨领域应用时容易受到影响，因为不同领域的密度差异会导致任务相关信息的丢失，这违背了标准的领域适应假设，从而影响模型泛化能力。
### Innovation
文章提出了一种条件特征对齐的理论框架，并提供了一个简单的实现方法。通过理论分析，该框架能够有效提高不同密度分布领域间的跨域计数性能，特别是通过条件分布对齐提高了联合源目标决策误差边界。实验结果验证了该方法优于现有无监督领域适应方法的优越性.
### Conclusion
通过实验展示了所提出的方法在多个具有不同密度分布的数据集上的有效性，并通过理论分析和实验证明了条件特征对齐能够在不同密度领域的目标计数中取得更好的泛化性能。
## 453. `cs.CV` - 重新思考视频异常检测的评价标准与基准 [PDF](https://arxiv.org/pdf/2505.19022), [HTML](https://arxiv.org/abs/2505.19022)
### Authors
Zihao Liu,Xiaoyu Wu,Wenna Li,Linlin Yang,Shengjin Wang
### Background
视频异常检测（VAD）的目标是检测与预期不符的异常情况，近年来吸引了越来越多的关注。现有的VAD研究主要集中在模型架构和训练策略上，但对于评价指标和基准的重视不够。现有的评价方法存在三个方面的重要缺陷：1) 存在单标注偏差；2) 无法奖励早期异常检测；3) 当前的基准数据集无法评估监督不足算法在场景上的过拟合。
### Innovation
该论文通过全面分析重新思考了VAD的评价方法，提出了三种新的评价方法：1) 建立了利用多轮标注的基于概率的AUC/AP（Prob-AUC/AP）指标来减少单标注偏差；2) 开发了延迟感知平均精度（LaAP）指标，奖励早期和准确的异常检测；3) 引入了两个难负类别基准（UCF-HN, MSAD-HN），专门用于评估场景过拟合。十种先进的VAD方法在新提出的评价方法下的性能进行了比较，提供了对未来VAD模型发展的新视角。
### Conclusion
研究通过概率AUC/AP、LaAP评价方法和UCF-HN、MSAD-HN两个难负类别基准，重新定义了VAD的评价标准与基准，为后续VAD模型的发展提供了新的思路。研究成果已经发布在指定链接中。
## 454. `cs.CV` - StateSpaceDiffuser: 将长时上下文引入扩散世界模型 [PDF](https://arxiv.org/pdf/2505.22246), [HTML](https://arxiv.org/abs/2505.22246)
### Authors
Nedko Savov,Naser Kazemi,Deheng Zhang,Danda Pani Paudel,Xi Wang,Luc Van Gool
### Background
世界模型在复杂环境中基于动作的视觉预测中受到了广泛关注。然而，只依赖少数最近观察结果会导致它们失去长期上下文，在几步后生成的场景就会偏离先前的观察结果，从而损害时间连续性。这一局限在基于扩散的最先进的世界模型中普遍存在，原因是缺乏持久的环境状态。
### Innovation
我们提出了StateSpaceDiffuser，这是一种结合状态空间模型特征以使扩散模型能够执行长时间上下文任务的架构。这种设计恢复了长期记忆，同时保持了扩散模型的高保真合成能力。为严格测量时间一致性，我们开发了一个评估协议，测试模型将已见过的内容在长时间展开中重新实例化的能力。实验证明，StateSpaceDiffuser 显著优于仅基于扩散的强基准模型，可以更长时间地保持视觉上下文的一致性。该模型在2D迷宫导航和复杂3D环境上均能提供一致的视图。
### Conclusion
引入状态空间表示到扩散模型中可以显著提升表现，既展示视觉细节，又加强长期记忆力。实验结果表明，将状态空间表示引入扩散模型是提高扩散模型视觉预测能力的有效方法。
## 455. `cs.CV` - DeepVideo-R1: 通过难度自意识回归GRPO的视频强化微调 [PDF](https://arxiv.org/pdf/2506.07464), [HTML](https://arxiv.org/abs/2506.07464)
### Authors
Jinyoung Park,Jeehye Na,Jinyoung Kim,Hyunwoo J. Kim
### Background
最近的研究已经证明基于强化学习（RL）的后训练方法能提升大型语言模型（LLMs）的推理能力。尤其是Group Relative Policy Optimization (GRPO)方法使用了一种基于PPO的强化算法，并以群组规范化奖赏。然而，GRPO在视频大型语言模型（VideoLLMs）中的效果仍需进一步研究。特别是在视频推理的任务中，GRPO的有效性尚未被充分探索。
### Innovation
本文提出了DeepVideo-R1，一种使用回归GRPO (Reg-GRPO)和难度感知数据增强的视频大型语言模型训练方法。Reg-GRPO重新定义了GRPO的损失函数，转化为直接预测优势的回归任务，从而无需依赖剪辑和最小化等安全措施。此外，难度感知数据增强策略通过增强输入提示/视频来确定可解决难度水平的样本难度，提供各种奖励信号。这种方法显著提高了视频推理的表现。
### Conclusion
实验结果显示，本文的方法在多个基准测试中显著提高了视频推理的表现。
## 456. `cs.CV` - SafePLUG: Empowering Multimodal LLMs with Pixel-Level Insight and Temporal Grounding for Traffic Accident Understanding [PDF](https://arxiv.org/pdf/2508.06763), [HTML](https://arxiv.org/abs/2508.06763)
### Authors
Zihao Sheng,Zilin Huang,Yansong Qu,Jiancong Chen,Yuhao Luo,Yen-Jung Chen,Yue Leng,Sikai Chen
### Background
现有的多模态大型语言模型（MLLMs）在各种视觉-语言任务中取得了显著进展，展示了在交通事故理解方面强大的潜力。然而，这些模型主要关注粗粒度的图像级或视频级理解，对处理细粒度视觉细节或局部场景组件能力不足，限制了在复杂事故场景中的应用。
### Innovation
提出了SafePLUG，一种新的框架，使MLLMs具备像素级理解与时间定位的能力，以便进行全面的交通事故分析。SafePLUG支持任意形状的视觉提示进行区域感知的问题回答，并基于语言指令进行像素级分割，还能够识别交通事故场景中的时间锚定事件。为此，该研究还构建了一个新的多模态问题-答案数据集，包含详细的像素级注解和时间事件边界，用于训练模型。实验结果显示，在区域问题回答、像素级分割、时间事件定位和事故事件理解等多种任务中，SafePLUG表现出强大的性能。
### Conclusion
SafePLUG为复杂交通场景的细粒度理解奠定了基础，有望提高驾驶安全并在智能交通系统中增强情境意识。相关代码、数据集和模型检查点将在特定链接公开。
## 457. `cs.CV` - M^3VIR：一种面向图像恢复和内容创作的大规模多模态多视角合成基准数据集 [PDF](https://arxiv.org/pdf/2509.16873), [HTML](https://arxiv.org/abs/2509.16873)
### Authors
Yuanzhi Li,Lebin Zhou,Nam Ling,Zhenghao Chen,Wei Wang,Wei Jiang
### Background
随着游戏和娱乐行业快速发展，沉浸式体验和生成式AI（GAI）技术的融合日益增多。高效的模型训练需要能够捕捉游戏环境多样性和上下文的大规模数据集。然而，现有数据集往往局限于特定领域或依赖于人工降级，无法准确捕捉游戏内容的独特特征。另外，针对可控视频生成的基准测试仍然缺失。
### Innovation
为了解决这些问题，我们提出了M^3VIR，一种大规模、多模态、多视角的数据集，专门设计来克服现有资源的不足。M^3VIR 通过虚幻引擎5渲染提供了多样而高保真游戏内容，包含80个场景的8个类别，包括M^3VIR_MR用于超分辨率（SR）、新型视图合成（NVS）以及NVS+SR任务，以及M^3VIR_MS，这是第一个用于对象级基准测试的多风格数据集。此外，我们还基准测试了几种最先进的SR和NVS方法，建立了性能基准。
### Conclusion
通过发布此数据集，我们希望促进使用AI技术进行游戏和娱乐内容增强、压缩和可控生成的研究。
## 458. `cs.CV` - 单目失焦和运动模糊视频中的动态高斯散点图生成 [PDF](https://arxiv.org/pdf/2510.10691), [HTML](https://arxiv.org/abs/2510.10691)
### Authors
Xuankai Zhang,Junjin Xiao,Qing Zhang
### Background
现有的方法针对的是单一类型的模糊（要么是失焦模糊，要么是运动模糊），无法同时处理这两种类型的模糊。虽然两种模糊都可以通过采用核卷积的方式进行联合建模，但准确估计模糊核的难度限制了这一方向的进步。
### Innovation
提出了一种逐像素可靠估计模糊核的方法，使用一个利用了模糊相关场景和相机信息的模糊预测网络，并受模糊感知稀疏性约束。此外，引入了一种动态高斯稠密化策略，以缓解不完整区域中高斯的数量不足问题，并通过引入未见过视角的信息来约束场景优化，从而增强新颖视图生成的性能。
### Conclusion
大量实验表明，本方法在生成失焦和运动模糊单目视频的新颖视图合成方面优于最新方法，具有生成逼真图像的能力。
## 459. `cs.CV` - BALR-SAM: Boundary-Aware Low-Rank Adaptation of SAM for Resource-Efficient Medical Image Segmentation [PDF](https://arxiv.org/pdf/2509.24204), [HTML](https://arxiv.org/abs/2509.24204)
### Authors
Zelin Liu,Sicheng Dong,Bocheng Li,Yixuan Yang,Jiacheng Ruan,Chenxu Zhou,Suncheng Xiang
### Background
Vision基础模型如Segment Anything Model (SAM)在大规模自然图像数据集上预训练，但在医学图像分割中往往表现不佳，主要是由于缺乏针对特定领域的适应性。在临床实践中，高效地为医学下游任务微调这些模型并在资源有限的情况下保持高性能，具有挑战性。
### Innovation
提出了一个边界的感知低秩适应框架BALR-SAM，它增强了SAM以适应医学成像。该框架包含三个定制组件：(1) 补充细节增强网络(CDEN)，使用深度可分卷积和多尺度融合来捕捉对于精确分割至关重要的边界敏感特征；(2) 低秩适配器整合进SAM的视觉变压器块中，优化特征表示和注意力机制，同时还可以显着减少参数空间；(3) 在掩码解码器中使用低秩张量注意力机制，将内存使用量减少75%，并提高推理速度。实验表明，在标准医学分割数据集上，BALR-SAM无需提示即可超越包括完全微调的MedSAM在内的多种最新技术，仅更新了其1.8%（11.7M）的参数。
### Conclusion
实验结果表明，BALR-SAM在不需要提示的情况下，无需完全微调，就能比多个最先进的方法，包括MedSAM，展现出更好的性能，同时它仅更新了模型的1.8%参数，有效地减少了资源需求。
## 460. `cs.CV` - FantasyWorld：统一视频与三维预测的几何一致世界建模 [PDF](https://arxiv.org/pdf/2509.21657), [HTML](https://arxiv.org/abs/2509.21657)
### Authors
Yixiang Dai,Fan Jiang,Chiyu Wang,Mu Xu,Yonggang Qi
### Background
高质量的3D世界模型对嵌入式智能和通用人工智能（AGI）至关重要，支持如AR/VR内容创作和机器人导航等应用。现有视频基础模型缺乏明确的3D定位能力，导致在空间一致性和后续3D推理任务中的实用性受限。基于此背景，本文探讨了如何将几何信息融入视频生成模型中，以增强其三维理解和生成能力。
### Innovation
提出了一种名为FantasyWorld的几何增强框架，该框架通过可训练的几何分支，与视频隐含特征共同建模，并在单一前向传播中联合处理，引入跨分支监督机制，使几何线索指导视频生成，同时视频先验对3D预测起到正则化作用，从而获得一致且可泛化的3D感知视频表示。特别地，几何分支产生的隐含特征无需场景优化或微调，即可作为下游3D任务（如新视角合成和导航）的通用表示。实验结果表明，FantasyWorld能够有效地弥合视频想象与三维感知之间的差距，相比最近的几何一致性基线，在多视角连贯性和风格一致性方面表现更优。
### Conclusion
通过统一的模型结构和跨分支信息交流，FantasyWorld能够实现视频想象力与三维感知的有效结合，提升视频生成和三维推理任务的整体性能，并且无需针对每个场景进行优化或微调便能适用于下游的3D任务。
## 461. `cs.CV` - 基于人类不确定性的人选数据选择和自动标注在视觉问答中的应用 [PDF](https://arxiv.org/pdf/2510.11295), [HTML](https://arxiv.org/abs/2510.11295)
### Authors
Jian Lan,Zhicheng Liu,Udo Schlegel,Raoyuan Zhao,Yihong Liu,Hinrich Schütze,Michael A. Hedderich,Thomas Seidl
### Background
大型视觉语言模型在视觉问答任务中表现出色，但仍然依赖于大规模带标注数据集的监督微调，这导致了高昂的人工标注成本。现实世界的数据集中往往存在人类不确定性（HU），表现为不同注释者对同一任务的信心和不确定性不同。当前的监督微调方法在优化时倾向于那些出现频率较高的标签，而忽略人类不确定性分布。这引发了两个关键问题：人类不确定性是如何影响微调的？如何有效利用人类不确定性进行训练？
### Innovation
本文首先系统评估了在不同人类不确定性水平下视觉语言模型的表现，发现了高人类不确定性样本对模型性能影响小甚至可能是负面的，以及全量数据集合训练会导致模型欠校准和无法捕捉人类不确定性分布的现象。针对这些发现，作者提出了HaDola框架，一种结合人类不确定性的数据选择和自动标注方法，通过如下四阶段迭代流程：区分、自我标注、错误触发、训练，从少量种子数据开始逐步扩充数据集，并有效降低对昂贵的人类不确定性标注需求，提高模型的准确性和校准度。且实验表明在视觉问答和VizWiz数据集上HaDola框架能够比现有的基准模型提供更佳或相同的表现，即使使用更少的训练数据。
### Conclusion
本文通过明确建模人类不确定性，在监督微调中展现了其重要性，并建议更好的利用人类不确定性比仅仅增加数据集规模更能提高效果。
## 462. `cs.CV` - 如何评估单目深度估计？ [PDF](https://arxiv.org/pdf/2510.19814), [HTML](https://arxiv.org/abs/2510.19814)
### Authors
Siyang Wu,Jack Nugent,Willow Yang,Jia Deng
### Background
单目深度估计是一项重要的研究任务，正经历着快速的发展。然而，如何对其进行评估仍然面临挑战，这从现有文献中的标准不一以及多种评估指标的优缺点不明确中可以看出。现有指标对不同类型的地面真值扰动的敏感程度了解不足，尤其是对曲率变化不够敏感。
### Innovation
本文提出了一个新颖且量化的指标评估方法，按照各种类型扰动的敏感性对现有指标进行分析，并重点关注与人类判断的对比。引入了一种基于相对表面法线的新指标，以及更强符合人类判断的综合指标创建方法，并提供了新的深度可视化工具。该项研究提供了关于现有指标的新见解，包括对曲率变化扰动的敏感度增强。
### Conclusion
这项研究揭示了现有指标对曲率变化的不敏感，通过提出新的基于相对表面法线的指标改进了这一点，并开发了新的深度可视化工具和生成更好地与人类判断对齐的综合指标的方法。
## 463. `cs.CV` - ε-Seg：稀疏监督的显微镜数据语义分割 [PDF](https://arxiv.org/pdf/2510.18637), [HTML](https://arxiv.org/abs/2510.18637)
### Authors
Sheida Rahnamai Kordasiabi,Damian Dalle Nogare,Florian Jug
### Background
在生命科学中，电子显微镜（EM）图像的语义分割仍然是一个挑战。EM数据捕捉生物结构的细节，有时候这些细节如此复杂以至于即便是人类观察者也会感到压力重重。
### Innovation
ε-Seg方法是基于分层变分自动编码器（HVAEs）的一种方法，使用中心-区域遮罩、稀疏标签对比学习（CL）、高斯混合模型（GMM）先验以及无需聚类的标签预测。中心区遮罩和修复损失鼓励模型在标签稀疏的情况下学习稳健且具有代表性的嵌入，以辨别所需的类别。为了获得最佳性能，ε-Seg引入了CL和GMM先验来塑造HVAE的潜在空间，使编码输入片段倾向于按照我们希望区分开的语义类进行聚类。最后，ε-Seg提出了一种MLP语义分割头部，直接从潜在嵌入中预测类别标签，而不是聚类潜在嵌入进行语义分割。
### Conclusion
ε-Seg展示了在复杂的生物学图像数据中，即使只有有限数量的训练标签可用时，也能达到有竞争力的稀疏监督分割结果。我们的方法也在荧光显微镜数据上显示了其适用性。
## 464. `cs.CV` - CARE: Contrastive Alignment for ADL Recognition from Event-Triggered Sensor Streams [PDF](https://arxiv.org/pdf/2510.16988), [HTML](https://arxiv.org/abs/2510.16988)
### Authors
Junhao Zhao,Zishuai Liu,Ruili Fang,Jin Lu,Linghan Zhang,Fei Dou
### Background
活动识别（ADL）从事件触发的环境传感器中提取对于辅助生活至关重要，但现有方法受限于表示层次的限制。基于序列的方法保留传感器激活的时间顺序但对噪声敏感且缺乏空间意识，基于图像的方法可以捕获全局模式和隐式的空间关联性，但会压缩细粒度的时间动态和失真传感器布局。朴素融合（如特征拼接）无法结合序列和图像表示的优势，导致资源未能得到充分利用。因此，需要一种新的方法来解决混合使用序列和图像信息的问题，以实现可靠的家庭环境下的ADL识别.
### Innovation
提出了一种端到端框架，即对比对齐（CARE），通过序列-图像对比对齐（SICA）进行表示学习联合优化，通过交叉熵进行分类。CARE 结合了（i）具有时间感知且对噪声具有鲁棒性的序列编码和（ii）具备空间信息和频率敏感性的图像表示，并采用联合对比分类目标进行端到端的学习，得到对齐且具有判别能力的嵌入。这种方法有效地融合了序列和图像信息，提高了ADL识别的性能和鲁棒性.
### Conclusion
CARE 在三个 CASAS 数据集上表现优异（米兰数据集89.8%，开罗数据集88.9%，京都数据集73.3%），且展示了对传感器故障和布局变化的鲁棒性，体现了其在智能家庭中可靠识别ADL的潜力.
## 465. `cs.CV` - 自适应随机系数以加速扩散采样 [PDF](https://arxiv.org/pdf/2510.23285), [HTML](https://arxiv.org/abs/2510.23285)
### Authors
Ruoyu Wang,Beier Zhu,Junzhi Li,Liangyu Yuan,Chi Zhang
### Background
基于扩散的生成过程通常平衡计算速度与样本质量。通过对基于ODE和SDE的求解器的理论研究揭示，ODE求解器在确定性轨迹上积累不可约梯度误差，而SDE方法在步预算有限时受到放大离散误差的影响。
### Innovation
提出了一种名为AdaSDE的新型单步SDE求解器，旨在统一ODE的效率和SDE的抗误差能力。具体地，引入了一个每个步骤可学习的系数，通过轻量级蒸馏估计，动态调节错误修正强度以加速扩散采样。此外，我们的框架可以与现有的求解器集成以增强其能力。
### Conclusion
广泛的实验证明了AdaSDE具有出色性能：在5个NFE下，AdaSDE在CIFAR-10上的FID得分为4.18，在FFHQ上的得分为8.05，在LSUN Bedroom上的得分为6.96。代码可在以下链接获得：this https URL
## 466. `cs.CV` - IGGT: 基于实例的几何变换器用于语义3D重建 [PDF](https://arxiv.org/pdf/2510.22706), [HTML](https://arxiv.org/abs/2510.22706)
### Authors
Hao Li,Zhengyu Zou,Fangfu Liu,Xuanyang Zhang,Fangzhou Hong,Yukang Cao,Yushi Lan,Manyuan Zhang,Gang Yu,Dingwen Zhang,Ziwei Liu
### Background
人类自然地将三维世界的几何结构和语义内容视为交织的维度，这使得对复杂场景实现连贯且准确的理解成为可能。然而，大多数先前的方法专注于训练大规模几何模型进行低级3D重建，并将高级空间理解孤立对待，忽略了这两者之间至关重要的相互作用，从而限制了泛化能力和在下游3D理解任务中的表现。最近的尝试通过简单地将3D模型与特定的语言模型对齐来减轻这一问题，但这一方法限制了感知能力，并限制了对下游任务的适应性。
### Innovation
在这项研究中，我们提出了一种实例导向的几何变换器(IGGT)，这是一种端到端的大统一变压器，用于统一空间重构和实例级上下文理解的知识。具体而言，我们设计了一种3D一致性对比学习策略，该策略仅通过2D视觉输入指导IGGT生成同时包含几何结构和实例导向聚类的统一表示。这种表示支持将2D视觉输入统一提升到具有一致的实例分离物体的3D场景。
### Conclusion
为实现这一任务，我们进一步创建了InsScene-15K，这是一个具有高质量RGB图像、姿态、深度图和3D一致性实例级掩码注释的大规模数据集，其中包含新的数据策划流程。
## 467. `cs.CV` - MMEdge: 通过流水线感知和编码加速本地多模态推理 [PDF](https://arxiv.org/pdf/2510.25327), [HTML](https://arxiv.org/abs/2510.25327)
### Authors
Runxi Huang,Mingxuan Yu,Mingyu Tsoi,Xiaomin Ouyang
### Background
实时在边缘设备上进行多模态推理对于自动驾驶、人机交互和移动健康等应用至关重要。然而，以往的研究往往忽视了传感动态与模型执行之间紧密的耦合关系以及不同模态间的复杂依赖性。
### Innovation
本文提出了一种基于流水线感知和编码的新本地多模态推理框架—MMEdge。MMEdge将整个推理过程分解为一系列细粒度的感知和编码单元，使得计算可以随着数据的到达而逐步进行。MMEdge还引入了一个轻量级但有效的时域聚合模块，以捕捉不同流水线单元中的丰富时序动态，从而保持准确性。同时，MMEdge还提出了自适应多模态配置优化器，可以动态选择在延迟约束下的最优传感和模型配置，以及跨模态预测跳过机制，在早期预测达到足够置信度时跳过速度较慢的模态的后续单元。
### Conclusion
我们使用两个公开的多模态数据集评估了MMEdge，并将其部署到了基于无人机（UAV）的多模态测试平台上。结果表明，MMEdge在保持高任务准确率的同时，显著减少了端到端的延迟。
## 468. `cs.CV` - DINO-YOLO: 自监督预训练在土木工程应用中高效数据对象检测 [PDF](https://arxiv.org/pdf/2510.25140), [HTML](https://arxiv.org/abs/2510.25140)
### Authors
Malaisree P,Youwai S,Kitkobsin T,Janrungautai S,Amorndechaphon D,Rojanavasu P
### Background
在土木工程应用中，物体检测受限于专门领域内标注数据的不足。传统方法难以处理数据稀缺的问题，特别是在需要高精度检测的场景中.
### Innovation
提出了DINO-YOLO，它结合了YOLOv12和DINOv3半监督视觉变压器的混合架构，旨在提高数据效率的同时实现有效的物体检测。DINOv3特征战略地集成在输入预处理(P0)和中期骨干网络增强(P3)中。实验验证显示了显著改进: 隧道段裂缝检测(648张图像)提高了12.4%，建筑个人防护装备(1000张图像)提高了13.7%，KITTIA数据库(7000张图像)提高了88.6%，同时保持实时推理(每秒30-47帧)。系统分析了五个YOLO尺度和九种DINOv3变体，确定了中尺度架构和双重P0P3集成（55.77% mAP@0.5）的最佳性能，小尺度则需要三重集成（53.63%）。虽然2-4倍的推理开销（21-33ms对比8-16ms基线）是可以接受的，但对于英伟达RTX 5090的现场部署来说，依然是可接受的。DINO-YOLO在低于10000张图像的土木工程数据集上达到最好的性能，同时保持了计算效率，为数据受限环境下施工安全监控和基础设施检查提供解决方案.
### Conclusion
DINO-YOLO架构在土木工程数据集上取得了最先进的检测性能，同时保持了计算效率，为解决数据稀缺问题提供了实际解决方案。
## 469. `cs.CV` - 在扫描模式中增加Hausdorff维度促进基于Mamba的方法在低光照图像增强中的应用 [PDF](https://arxiv.org/pdf/2510.26001), [HTML](https://arxiv.org/abs/2510.26001)
### Authors
Xinhua Wang,Caibo Feng,Xiangjun Fu,Chunxiao Liu
### Background
本文基于Mamba框架，提出了一种创新性增强方法，通过引入新的希尔伯特选择扫描机制增加其扫描模式的Hausdorff维度。这一机制更有效地探索特征空间，捕获细节更加精细的局部信息，提升整体覆盖范围。从而减小信息不一致性和优化空间局部性，更好地捕获细微的本地交互，同时模型还能处理长距离依赖关系。
### Innovation
文章创新性地通过引入新的希尔伯特选择扫描机制，增加扫描模式的Hausdorff维度。该机制能更有效地探索特征空间，捕获细节更加精细的局部信息，提高整体覆盖范围，有助于减轻信息不一致性，优化空间局部性，更好地捕捉细微的本地交互，同时保持模型处理长距离依赖关系的能力。
### Conclusion
大量的实验在公开可获取的标准数据集上表明，我们的方法显著提高了现有的基于Mamba的低光图像增强方法的定量指标和视觉保真度，同时减少了计算资源的消耗和缩短了推理时间。我们认为，这种改进策略不仅推动了低光图像增强领域的技术进步，还为依赖Mamba技术的应用领域提供了更广泛的应用前景。
## 470. `cs.CV` - LV-UNet：一种用于医学图像分割的轻量级且基础模型 [PDF](https://arxiv.org/pdf/2408.16886), [HTML](https://arxiv.org/abs/2408.16886)
### Authors
Juntao Jiang,Mengmeng Wang,Huizhong Tian,Lingbo Cheng,Yong Liu
### Background
尽管大规模模型在计算机视觉领域取得了显著进展，但在医学图像分割中，诸如优化复杂性、Transformer架构的复杂性、计算约束以及实际应用需求等方面的问题强调了设计简单模型的重要性。特别是在移动医疗设备中，需要轻量级、可部署且具有实时性能的模型。然而，现有的轻量级模型往往在不同数据集上的鲁棒性较差，限制了它们的广泛应用。因此，有必要开发一种能够平衡性能和计算负载的轻量级模型，以克服上述挑战。
### Innovation
本文介绍了一种轻量级且基础的模型LV-UNet，该模型利用预训练的MobileNetv3-Large骨干网络，并引入了融合模块。进一步，LV-UNet采用强化的深度训练策略，并在推断过程中通过重新参数化切换到部署模式，从而显著降低了参数数量和计算开销。该模型在ISIC 2016、BUSI、CVC-ClinicDB、CVC-ColonDB和Kvair-SEG等数据集上的实验结果显示，其性能和计算负载之间的平衡优于现有轻量级模型。
### Conclusion
实验结果表明，LV-UNet模型在保持较高分割性能的同时，显著降低了计算负载，为临床医学中大规模部署和实时应用提供了解决方案。源代码将在https://github.com/lvunet发布。
## 471. `cs.CV` - 平衡视频与文本：一种多模态总结生成与评估的平衡方法 [PDF](https://arxiv.org/pdf/2505.06594), [HTML](https://arxiv.org/abs/2505.06594)
### Authors
Galann Pennec,Zhengyuan Liu,Nicholas Asher,Philippe Muller,Nancy F. Chen
### Background
Vision-Language模型在总结复杂的多媒体输入（如整个电视节目片段）时，难以平衡视觉和文本信息。现有的方法通常在生成总结时未能全面提升这两种模态之间的融合度，导致视觉与文本信息的不均衡。此外，现有的评估指标可能无法准确评估多模态总结的质量，无法充分衡量两种模态的信息综合情况。
### Innovation
该论文提出了一种零样本的视频到文本总结方法，能够生成自定义的电视剧剧本表示，将关键视频片段、对话和人物信息整合成一个统一的文档。这种方法同时生成剧本并命名人物，仅使用音频、视频和字幕作为输入。同时，论文引入了MFactSum，一种新的评价指标，能够综合评价视觉和文本两种模态的信息，从而更好地评估总结的质量。
### Conclusion
研究使用MFactSum评价其生成的剧本总结，结果显示该方法在生成包含更多相关视觉信息的总结时，只需输入视频的75%。该方法在SummScreen3D数据集上的表现优于最新的预训练模型（如Gemini 1.5），证明了其在多模态总结生成方面的优越性。
## 472. `cs.CV` - 基于增强现实的变形配准引导在头颈部肿瘤切除中的应用 [PDF](https://arxiv.org/pdf/2503.08802), [HTML](https://arxiv.org/abs/2503.08802)
### Authors
Qingyun Yang,Fangjie Li,Jiayi Xu,Zixuan Liu,Sindhura Sridhar,Whitney Jin,Jennifer Du,Jon Heiselman,Michael Miga,Michael Topf,Jie Ying Wu
### Background
头颈部鳞状细胞癌（HNSCC）在固体恶性肿瘤中复发率最高。通过提高阳性边缘定位能力可以减少复发率。冰冻切片分析（FSA）是术后标本中边缘评估的金标准，但由于标本复杂的3D解剖结构和显著的收缩，基于FSA结果将标本边缘准确重新定位至切除部位仍具挑战性。
### Innovation
提出了一种新的可变形注册框架，该框架结合了切除前和切除后的标本上表面及切除部位，将厚度信息纳入注册过程。这种方法显著提高了目标注册误差（TRE），尤其在舌标本中，相较于先前的可变形注册，TRE提高了33%。该方法展示了对较厚标本的增强适应性，并分析了不同标本的独特的变形行为，强调了定制变形策略的必要性。此外，还整合了增强现实（AR）基础的自动对齐系统，准确且自动地将变形的3D标本网格与阳性边缘标注叠加至切除部位。
### Conclusion
在两外科医生参与的试点研究中，整合系统将外科医生的平均目标重新定位误差从9.8厘米降至4.8厘米，表明该框架在头颈部肿瘤切除中的疗效显著。
## 473. `cs.CV` - 序贯风险控制下的 conformal 对象检测 [PDF](https://arxiv.org/pdf/2505.24038), [HTML](https://arxiv.org/abs/2505.24038)
### Authors
Léo andéol,Luca Mossina,Adrien Mazoyer,Sébastien Gerchinovitz
### Background
近年来，目标检测器的发展促成了其在工业领域的应用。然而，它们在安全关键应用中的部署受到神经网络可靠性的固有缺乏以及目标检测模型复杂结构的阻碍。
### Innovation
我们提出了正式定义序贯对象检测（COD）的问题，并引入了一种名为序贯风险控制（SeqCRC）的新方法。SeqCRC方法扩展了统计保证的范式，以适配两个包含两个参数的序列任务，这是在COD情况下所需要的。此外，我们还介绍了适用于不同场景的旧有和新型损失函数及预测集，以及一个用于我们的方法复现和进一步探索的 conformal 工具包。
### Conclusion
通过这个工具包，我们进行了详尽的实验，验证了我们的方法，并强调了权衡取舍和其他实际后果。
## 474. `cs.CV` - SageAttention3：面向推理的微量化FP4注意力及8位训练探索 [PDF](https://arxiv.org/pdf/2505.11594), [HTML](https://arxiv.org/abs/2505.11594)
### Authors
Jintao Zhang,Jia Wei,Pengle Zhang,Xiaoming Xu,Haofeng Huang,Haoxu Wang,Kai Jiang,Jun Zhu,Jianfei Chen
### Background
注意力机制的效率至关重要，因其存在二次时间复杂度。为提高注意力机制的效率，本文通过两个关键贡献实现了加速：首先，利用Blackwell GPU中的新型FP4张量核心加速注意力计算。其次，首次探索将低位注意力应用于训练任务，而不是仅限于推理。尽管FlashAttention3和SageAttention等现有低位注意力工作已经在推理上取得了一定成果，但训练大型模型的效率同样重要。本文旨在探索低位注意力在训练任务中的适用性，并设计了适用于正向和反向传播的高效8位注意力机制.
### Innovation
本文通过使用新的FP4张量核心和低位注意力开发出了SageAttention3模型。在推理上，SageAttention3实现了显著的加速效果。同时，作者设计了一种适用于训练任务的8位注意力机制，为训练任务的高效进行提供了新的可能性，尽管在某些预训练任务上显示出了较慢的收敛速度，但不影响其在微调任务上的零损失性能。
### Conclusion
通过使用新型FP4张量核心，SageAttention3在推理上相比FlashAttention3实现了5倍的速度提升。此外，提出并实现了8位注意力机制，初步显示了在微调任务上与全精度版本性能相当，但在预训练任务上收敛速度较慢，但这表明了低位注意力在训练任务中的潜在应用价值。
## 475. `cs.CV` - 通过μP高效扩展扩散变换器 [PDF](https://arxiv.org/pdf/2505.15270), [HTML](https://arxiv.org/abs/2505.15270)
### Authors
Chenyu Zheng,Xinyu Zhang,Rongzhen Wang,Wei Huang,Zhi Tian,Weilin Huang,Jun Zhu,Chongxuan Li
### Background
扩散变换器已成为用于视觉生成模型的基础，但它们的扩展性受限于大规模调超参数（HP）的高昂成本。尽管Vanilla Transformers有一个名为μP的超参数优化参数化方法已被提出，使小型到大型语言模型之间能够稳定地转移超参数，并大幅降低了调优成本，但其在扩散变换器中的应用效果尚不清楚，因为它们在架构和目标上有所不同。本文旨在将μP方法扩展到扩散变换器，并通过大规模实验验证其有效性。
### Innovation
本文将标准μP方法推广到了扩散变换器，并系统地展示了DiT-μP具有稳健的超参数转移性。还通过将PixArt-α放大至0.61B和MMDiT放大至18B验证了μP方法在文本转图像生成中的有效性。结果显示，μP下的模型在较小调优成本的前提下优于各自的基线模型，分别为PixArt-α的5.5%和MMDiT-18B的人类专家3%的消费成本。这些结果确立了μP方法作为通过μP高效扩展扩散变换器的一种原理和高效框架。
### Conclusion
通过μP方法能够解决扩散变换器扩展性问题，该方法不仅能够让超参数稳定地从小型模型转移到大型模型，而且在多个扩散变换器模型上证实了其有效性，并且能够以较低的调优成本实现模型性能提升。
## 476. `cs.CV` - C3Editor: 实现2D模型在3D编辑中的可控一致性 [PDF](https://arxiv.org/pdf/2510.04539), [HTML](https://arxiv.org/abs/2510.04539)
### Authors
Zeng Tao,Zheng Ding,Zeyuan Chen,Xiang Zhang,Leizhi Li,Zhuowen Tu
### Background
现有的基于2D提升的3D编辑方法往往面临着一致性问题，这主要是因为缺乏视图一致的2D编辑模型，以及在多个视图之间确保编辑一致性的难度。
### Innovation
提出了一种名为C3Editor的可控制且一致的基于2D提升的3D编辑框架。C3Editor通过控制选择一个参考视角（GT）及其对应的编辑图像作为优化目标，进行多视图一致性优化，引入单独的LoRA模块进行针对优化，从而实现多视图一致性。这种方法在定性和定量评估中都优于现有的基于2D提升的方法，提供了更一致和可控的2D和3D编辑结果。
### Conclusion
C3Editor在基于2D提升的3D编辑中实现了可控的一致性，通过多视图一致性优化和LoRA模块的引入，相比于现有方法提供了更好的编辑效果。
## 477. `cs.CV` - 低成本明场图像分割智能软件系统：基于算法的细胞自动分析实现 [PDF](https://arxiv.org/pdf/2509.11354), [HTML](https://arxiv.org/abs/2509.11354)
### Authors
Surajit Das,Pavel Zun
### Background
低成本实验室通常只能依赖成本效益高的微观测影技术，如明场显微镜，并搭配标准CPU计算资源。然而，明场图像固有的噪声高、对比度低以及动态形态变化等问题，加之缺乏GPU资源和复杂软件界面，制约了理想的研究产出。该文章概述了这种背景下，明场显微镜在低预算实验室中的局限性及其带来的挑战。
### Innovation
该论文提出了一种基于Python的新型细胞图像分析框架，专为配备标准CPU的低预算实验室设计。该框架无需标注训练数据，支持无需编程技能的用户界面以及为开发人员提供的脚本接口。其独特的模块化架构允许灵活集成和维护。经过多种类型未染色细胞的验证，该框架在精准度和再现性方面优于Cellpose和StarDist等当代工具，并在其基于CPU的平台上展示了竞争性的分割速度，凸显了其在基础研究及临床应用（如细胞移植和肌肉再生疗法）中的巨大潜力。
### Conclusion
该框架通过其模块化的端到端工作流程，实现了语义和实例分割、特征提取、分析、评估和报告自动化生成。它的设计满足了低预算实验室的需求，提供了高效的细胞图像分类和分析能力，显著提升了科研效率。
## 478. `cs.CV` - Mano技术报告 [PDF](https://arxiv.org/pdf/2509.17336), [HTML](https://arxiv.org/abs/2509.17336)
### Authors
Tianyu Fu,Anyang Su,Chenxu Zhao,Hanning Wang,Minghui Wu,Zhe Yu,Fei Hu,Mingjia Shi,Wei Dong,Jiayao Wang,Yuyang Chen,Ruiyang Yu,Siran Peng,Menglin Li,Nan Huang,Haitian Wei,Jiawei Yu,Yi Xin,Xilin Zhao,Kai Gu,Ping Jiang,Sifan Zhou,Shuo Wang
### Background
图形用户界面（GUIs）是人机交互的主要媒介，但自动化的GUI交互仍然具有挑战性，这主要是由于视觉元素的复杂性、动态环境以及多步推理的需求。现有的基于视觉语言模型（VLMs）的方法常受到图像分辨率有限、领域不匹配和序列决策能力不足等问题的困扰。
### Innovation
本文提出Mano，这是一种基于多模态预训练模型的GUI智能代理，该模型伫立于广泛的网页和计算机系统数据之上。Mano的核心创新包括一种新型模拟环境用于高保真数据生成、一个三阶段训练管道（监督微调、离线强化学习和在线强化学习）以及一个用于错误恢复的验证模块。这些创新解决了现有自动GUI交互方法中存在的问题。
### Conclusion
Mano在多个GUI基准测试中展现了最先进的性能，包括Mind2Web和OSWorld，其成功率和操作精度均达到了显著的提升。这项工作为强化学习与视觉语言模型的集成提供了新的见解，强调了领域特定数据、迭代训练和全面回报设计的重要作用。
## 479. `cs.CV` - Poisson Informed Retinex Network for Extreme Low-Light Image Enhancement [PDF](https://arxiv.org/pdf/2506.04470), [HTML](https://arxiv.org/abs/2506.04470)
### Authors
Isha Rao,Ratul Chakraborty,Sanjay Ghosh
### Background
低光照图像的去噪和增强具有挑战性，尤其是在传统噪声假设（如高斯噪声）不再有效的场景下。在许多实际场景中，尤其是低光照条件下，噪声是与信号相关的，并且更适合用泊松噪声来表示。本文解决了在极端低光照条件下被泊松噪声降级图像的去噪问题。
### Innovation
本文提出了一个基于轻量级深度学习的网络方法，该方法将Retinex基分解与泊松去噪结合到一个统一的编码-解码网络中。该模型通过引入泊松去噪损失来同时增强照明并抑制噪声，解决了与信号相关的噪声问题，无需预先知道反射率和照明，该网络学习一个有效的分解过程，同时确保反射率一致且照明平滑，不会引起任何颜色失真。实验结果表明，该方法在低光照条件下显著改善了可见性和亮度，同时在环境光照下保持了图像结构和颜色恒定性。
### Conclusion
实验结果证明了所提出的方法在低光照条件下的有效性和实用性。该方法在改善图像可见性与亮度的同时，有效地保持了图像的结构和颜色恒定性。
## 480. `cs.CV` - 通过单调包含模型的张量完成：广义低秩先验与深度去噪器的结合 [PDF](https://arxiv.org/pdf/2510.12425), [HTML](https://arxiv.org/abs/2510.12425)
### Authors
Peng Chen,Deliang Wei,Jiale Yao,Fang Li
### Background
多维度数据中的缺失值对下游分析构成了重大挑战，尤其是在多元应用中。这些数据通常以张量的形式存在，并且现有的一些填补方法结合了全局低秩先验和插件式纯净噪声去除器显示出很好的实验性能。然而，这些方法常常依赖于经验性的收敛性或者不现实的假设，比如深度去噪器作为隐式正则化器的 proximal 操作，这通常并不成立。
### Innovation
本文提出了一个新的基于单调包含原理的张量完成框架，其中将深度去噪器作为一般操作，相较于经典的基于优化的公式化起到了更为宽松的作用。另外，还将广义低秩先验与弱凸惩罚相结合，更好地捕捉整体结构。文章进一步基于 Davis-Yin 分解方案开发了一个新的算法 GTCTV DPC，并严格证明了其全局收敛性。实验结果表明，在多个质量指标上，GTCTV DPC 比现有方法表现出更好的性能，特别是在低采样率时。例如，在处理采样率为 0.05 的多维度图像完成任务时，GTCTV DPC 达到的平均峰值信噪比（MPSNR）比第二好方法高出 0.717 dB，多光谱图像和彩色视频的情况分别是 0.649 dB 和 0.649 dB.
### Conclusion
通过提出的 GTCTV DPC 算法，该研究不仅克服了现有方法的限制，还展示了在低采样率条件下对多维度数据和图像处理任务的优越性能。
## 481. `cs.CV` - 医学中的变压器：提高医学影像配图中的视觉-语言对齐 [PDF](https://arxiv.org/pdf/2510.25164), [HTML](https://arxiv.org/abs/2510.25164)
### Authors
Yogesh Thakku Suresh,Vishwajeet Shivaji Hogale,Luca-Alexandru Zamfira,Anandavardhana Hegde
### Background
该论文背景介绍了现有的医学影像配图方法，并指出当前的方法在处理特定医学影像数据时存在不足，特别是在语言和影像之间的语义对齐方面。因此，提出了一个基于变压器的多模态框架来生成具有临床相关性的MRI扫描配图，旨在提高配图的准确性与一致性，特别是针对特定领域数据时的效果更佳。同时，该工作借鉴了最新的医学图像配图方法，以进行对比研究和性能基准测试。
### Innovation
该工作的创新之处在于使用了一个DEiT-Small视觉变压器作为图像编码器，结合了MediCareBERT进行文本嵌入，并且通过自定义的LSTM解码器构建了一个框架。该框架利用了混合余弦-MSE损失和基于向量相似性的对比推理，从而在医学影像配图中实现了语义对齐。作者还设计了该模型专门针对医学影像数据进行优化，以进一步提高配图的准确性和语义对齐度。具体而言，与最先进的医学图像配图方法如BLIP、R2GenGPT以及基于变压器的 recent 方法相比，他们模型在特定领域数据上的表现更佳。
### Conclusion
该研究提出了一种可扩展且可解释的自动化医疗影像报告解决方案。通过实验证明，专注于特定领域数据集的模型能够显著提升配图的准确性和语义对齐。这不仅有助于提高医疗影像记录过程中的精确度，而且还能降低人力成本，提高工作效率。
## 482. `cs.LG` - 揭露真相：持续训练中毒引发信念偏移探究 [PDF](https://arxiv.org/pdf/2510.26829), [HTML](https://arxiv.org/abs/2510.26829)
### Authors
Svetlana Churina,Niranjan Chebrolu,Kokil Jaidka
### Background
大语言模型（LLMs）通过不断扩展的网络数据进行预训练，但这一适应过程也会使其暴露于细微的误导信息中。尽管之前的工作已经研究了静态预训练期间的数据污染，然而在持续预训练条件下这些操纵的影响依然很少被探索。鉴于虚假信息反复暴露会增强人们的信任度（似动真实效应），本研究探讨虚假但坚信的陈述是否能改变模型的认知表征。作者引入了一种针对性框架和数据集来验证这一假设，并通过注入受控量的污染数据，在不同检查点、模型规模及问题类型下进行探究，发现即使相对少量的暴露也能导致坚实事实的代表表征持续偏离，不同层次和模型规模的敏感性各异。这些结果揭示持续更新的LLMs存在类似人类的误导信息内化漏洞，强调了在模型更新过程中保持事实准确性的严格监控需求。
### Innovation
提出了一种框架和数据集（Layer of Truth）来探究持续训练期间信念的变化，特别是通过引入受控量的污染数据并监测中间表征的变化，量化了信念偏移的时机和方式。实验结果揭示了即使轻微的误导信息暴露也能导致坚实事实的代表表征持续偏离。
### Conclusion
持续训练的LLMs暴露于追随虚假信息的可能性，显示了它们与人类类似的认知脆弱性，因此需要对模型更新期间的事实完整性进行严格的监测和管理。
## 483. `cs.LG` - SmoothGuard: 通过噪声扰动和聚类聚合保护多模态大型语言模型 [PDF](https://arxiv.org/pdf/2510.26830), [HTML](https://arxiv.org/abs/2510.26830)
### Authors
Guangzhi Su,Shuchang Huang,Yutong Ke,Zhuohang Liu,Long Qian,Kaizhu Huang
### Background
多模态大型语言模型（MLLMs）通过联合处理文本和视觉输入在各种任务中取得了卓越的性能。然而，这些模型因对抗性操纵而表现出很高的脆弱性，这引发了对其部署时的安全性和可靠性的担忧。
### Innovation
作者首先在HuggingFace生态系统中生成对抗性图像，然后引入了SmoothGuard，这是一种轻量级且模型无感知的防御框架，通过随机噪声注入和基于聚类的预测聚合来增强MLLMs的鲁棒性。该方法使用高斯噪声扰动连续模态（如图像和音频），生成多个候选输出，并应用嵌入式聚类来过滤出受到对抗性影响的预测。最终答案从主要聚类中选择，以确保即使在恶意扰动下也能稳定响应。
### Conclusion
在POPE、LLaVA-Bench（野外环境）和MM-SafetyBench上的广泛实验表明，SmoothGuard在提高对抗攻击抗性的同时保持了竞争力。消融研究表明，噪声范围的最佳区间为0.1-0.2，以在鲁棒性和实用性之间取得平衡。
## 484. `cs.LG` - 准确的目标隐私保护联邦学习：平衡公平与效用 [PDF](https://arxiv.org/pdf/2510.26841), [HTML](https://arxiv.org/abs/2510.26841)
### Authors
Kangkang Sun,Jun Wu,Minyi Guo,Jianhua Li,Jianwei Huang
### Background
联邦学习（FL）允许参与者在不共享数据的情况下进行模型训练，但这种模式存在一个基本挑战，即如何同时确保不同人口群体的公平性，并保护敏感的客户端数据。现有方法难以在保护隐私的同时公平对待所有数据贡献者，这导致了一种公平性和隐私性之间的内在张力。
### Innovation
提出了一个新的差分隐私公平联邦学习算法（FedPF），通过将多目标优化转化为零和博弈来解决这一问题，其中公平性约束和隐私约束与模型性能相互竞争。理论分析揭示了隐私保护限制公平检测和纠正能力的一个反常关系，证明了适度的公平约束在初期会提高模型泛化能力，但在后期因公平性约束的增强会导致性能下降，这挑战了关于公平与效用权衡的传统观念。实验验证了该算法在三个数据集上可以减少42.9%的歧视现象，同时保持了竞争力性能。
### Conclusion
该项研究揭示了隐私保护与公平性之间的不可避免紧张关系，平衡两者需要精心协调而非单独优化。同时证明了FedPF算法可以在保护隐私的同时提升模型公平性和准确性。
## 485. `cs.CV` - 从空间和时间遗产调查图像中估算神经后验概率进行天文学图像目录构建 [PDF](https://arxiv.org/pdf/2510.15315), [HTML](https://arxiv.org/abs/2510.15315)
### Authors
Yicun Duan,Xinyue Li,Camille Avestruz,Jeffrey Regier
### Background
2026年，Vera C. Rubin天文台的_LSST_巡天项目将全面展开，产生前所未有的天文图像量。基于天文图像数据的多数科学工作流步骤需要构建天文目录，即由拍摄的恒星、星系及其属性构成的表格。传统的确定性目录构建方法缺乏统计一致性，而现有的概率方法则在计算效率、准确性或处理多波段叠加图像（这是LSST图像的主要输出格式）方面存在不足。因此，本文探讨了一种最近开发的贝叶斯推理方法——神经后验估计（NPE），作为一种目录构建的方法。NPE通过深度学习实现了计算效率和高精度的结合。在评估DC2模拟天空调查高逼真度合成数据集时，NPE在光源检测、亮度测量、恒星/星系分类以及星系形态测量方面系统地超过了标准的LSST管道。此外，NPE还提供了校准良好的后验近似。这些使用模拟数据获得的初步结果表明，在没有模型误设的情况下，NPE具有潜在优势。尽管在将NPE应用于实际的LSST图像时难以避免模型误设，但仍有许多策略可以减轻其影响。
### Innovation
提出了利用神经后验估计（NPE）方法进行天文目录构建，该方法结合了深度学习以实现高效的计算和高精度。NPE在光源检测、亮度测量、恒星/星系分类和星系形态测量方面表现优于标准LSST管道。此外，NPE还提供了校准良好的后验近似。
### Conclusion
尽管在将NPE应用于真实LSST图像时模型误设是不可避免的，但有多种策略可以减轻其影响，并且NPE在使用模拟数据进行测试时表现出潜在优势。
## 486. `cs.LG` - 通过少样本预测发现电动汽车充电站点类型：首个全国范围研究 [PDF](https://arxiv.org/pdf/2510.26910), [HTML](https://arxiv.org/abs/2510.26910)
### Authors
Kshitij Nikhal,Luke Ackerknecht,Benjamin S. Riggan,Phil Stahlfeld
### Background
交通运输的低碳化依赖于电动汽车（EV）的广泛应用，这要求对充电行为有准确的理解，以确保成本效益和电网弹性基础设施。现有的研究受限于小型数据集、基于简单临近关系的时间依赖性建模以及对操作历史有限的站点的弱泛化能力。这些问题限制了对大规模电动汽车充电需求的准确预测和有效的基础设施规划。
### Innovation
本文提出了一种将聚类与少样本预测结合的框架，利用新的大规模充电需求数据集来发现充电站点的典型模式。这项研究表明，针对典型模式的专家模型在对未见站点进行需求预测时表现优于全局基准。通过将预测性能作为基础设施分段的基础，我们为运营商提供了降低运营成本、优化能源和定价策略以及支持对气候目标至关重要的电网弹性提供了可操作的见解。
### Conclusion
通过建立基于预测性能的基础设施分段，我们生成了可操作的洞察，帮助运营者降低成本，优化能源和定价策略，并支持对抗气候变化至关重要的电网弹性。
## 487. `cs.LG` - 将本体与大型语言模型集成以增强化工领域的控制系统 [PDF](https://arxiv.org/pdf/2510.26898), [HTML](https://arxiv.org/abs/2510.26898)
### Authors
Crystal Su,Kuai Yu,Jingrui Zhang,Mingyuan Shao,Daniel Bauer
### Background
该工作提出了一种结合本体知识与生成推理的大规模语言模型（LLM）框架，用于化学工程。这种框架通过数据获取、语义预处理、信息提取和本体映射等一系列步骤，将结构化的领域知识与生成式推理相结合，生成模板化的问答对，用于微调模型。该框架还包含一个控制重点的解码阶段和引文闸门，通过约束输出到本体链接的术语，确保语法和事实的基础性。通过评价指标量化的语言质量和本体准确性进一步促进了系统的可解释性和可靠性。
### Innovation
该研究提出了一种新的框架，将本体知识与大规模语言模型相结合，通过一系列步骤整合结构化领域知识和生成推理。引入控制焦点的解码阶段和引文闸门，确保模型输出与本体链接的术语一致。引入反馈和未来扩展，包括语义检索和迭代验证，进一步增强系统的可解释性和可靠性。这种方法提供了一种透明且可审核的方法，将大型语言模型应用于过程控制、安全分析和其他关键工程领域。
### Conclusion
该集成框架结合了符号结构和神经生成，为应用大型语言模型到过程控制、安全分析和其他关键工程领域提供了一种透明且可审核的方法。未来的研究将继续改进系统，包括语义检索和迭代验证，进一步提高系统的可解释性和可靠性。
## 488. `cs.LG` - CAS-Spec: 级联自适应自投机解码方法在LLMs即时无损推理加速中的应用 [PDF](https://arxiv.org/pdf/2510.26843), [HTML](https://arxiv.org/abs/2510.26843)
### Authors
Zhiyuan Ning,Jiawei Shao,Ruge Xu,Xinfei Guo,Jun Zhang,Chi Zhang,Xuelong Li
### Background
投机解码已成为部署大规模语言模型（LLMs）时用于无损推理加速的有效技术。尽管即时自投机解码方法提供了无缝集成和广泛的适用性，但它们的加速效果通常不如依赖于专门训练的方法。级联多级草图模型可以进一步加速和提高灵活性，但多次训练模型的高成本限制了其实用应用。
### Innovation
作者提出了一种名为CAS-Spec的新方法，通过动态可切换的推理加速（DSIA）策略（如层稀疏性和激活量化）构建自投机草图模型。此外，传统的垂直和水平级联算法不适用于自投机解码方法。本文引入了一种动态树级联（DyTC）算法，基于接受率和延迟预测的启发式规则，自适应地路由多级草图模型并分配草图长度。CAS-Spec方法在各种LLM和数据集上实现了比现有即时自投机解码方法更先进的加速，平均加速比从1.1倍到2.3倍。DyTC分别在基于级联的基准算法和基于树的基准算法上提高了47%和48%的平均加速比。CAS-Spec可以轻松集成到大多数现有LLM中，并具有随着自投机解码技术的进步进一步加速的潜力。
### Conclusion
CAS-Spec方法实现了对现有即时自投机解码方法的最佳加速，结合DyTC算法进一步提高了加速效果，能够对大多数现有的LLM进行即时无损推理加速。
## 489. `cs.LG` - 机器可以高效思考吗？ [PDF](https://arxiv.org/pdf/2510.26954), [HTML](https://arxiv.org/abs/2510.26954)
### Authors
Adam Winchell
### Background
传统的图灵测试已不再适用于区分人类和机器智能，特别是在先进的人工智能系统已经通过原始图灵测试并引发严重道德和环境问题的情况下，急需更新测试标准。
### Innovation
本文扩展了原始的模仿游戏，引入了一个额外因素——答题过程中消耗的能量。通过增加能效限制，该新测试迫使我们从效率的角度评估智能，将抽象的思维问题与有限资源的具体现实联系起来。此外，这种新的测试设置了可供量化的结束点，而原始测试缺乏这一特点。
### Conclusion
通过增加能效限制，新测试促使社会权衡使用人工智能的时间节约与整体资源成本之间的关系。
## 490. `cs.LG` - 有限计算预算下的细粒度迭代对抗攻击 [PDF](https://arxiv.org/pdf/2510.26981), [HTML](https://arxiv.org/abs/2510.26981)
### Authors
Zhichao Hou,Weizhi Gao,Xiaorui Liu
### Background
在AI安全研究中，当计算资源有限时，如何在固定计算预算内最大化迭代对抗攻击的效果是一个关键挑战。粗略减少攻击迭代次数虽然可以降低成本，但会显著削弱攻击的有效性。
### Innovation
本文提出了一种细粒度控制机制，在迭代层和层内迭代水平上选择重新计算层激活，以在有限预算内实现可达到的攻击效果。该方法在同等成本下优于现有基准，并且当与对抗训练结合时，可以仅使用原始预算的30%就达到相当的性能。
### Conclusion
实验结果表明，本文提出的方法在同等成本下持续优于现有基准，并且在与对抗训练结合使用时，仅需原来预算的30%，即可达到类似的性能。
## 491. `cs.LG` - MM-OPERA: 用于大型视觉语言模型的开放式关联推理基准 [PDF](https://arxiv.org/pdf/2510.26937), [HTML](https://arxiv.org/abs/2510.26937)
### Authors
Zimeng Huang,Jinxin Ke,Xiaoxuan Fan,Yufeng Yang,Yang Liu,Liu Zhonghan,Zedi Wang,Junteng Dai,Haoyi Jiang,Yuyu Zhou,Keze Wang,Ziliang Chen
### Background
大型视觉语言模型（LVLMs）取得了显著的进步，但与人类智能相比，仍存在幻觉和浅显的模式匹配等缺陷。现有的基准测试多局限于封闭式任务，难以捕捉开放式关联推理的复杂性，这是实际应用中至关重要的能力。本工作旨在评估尚未充分探索的基本智能——关联，它是人类认知能力的核心，支撑着创造性和知识整合能力。
### Innovation
提出了一种系统性的基准测试MM-OPERA，包括11,497个实例，跨越两个开放式任务：远程项目关联（RIA）和上下文关联（ICA）。通过自由形式的回答和明确的推理路径，MM-OPERA挑战LVLMs模仿发散思维和收敛关联推理的精神。此外，部署了定制的LLM-as-a-Judge策略进行评估，并采用过程奖励导向的判断方法对推理进行精确解析。
### Conclusion
广泛的实证研究，包括任务实例的敏感性分析、LLM-as-a-Judge策略的有效性分析及能力、领域、语言、文化等方面的多样性分析，提供了对当前LVLMs在关联推理中局限性的全面而细致的理解，为开发更接近人类通用的人工智能铺平了道路。相关数据集和代码可在该链接获得：this https URL
## 492. `cs.LG` - 使用卫星和街景图像预测印度两座城市家庭用水量 [PDF](https://arxiv.org/pdf/2510.26957), [HTML](https://arxiv.org/abs/2510.26957)
### Authors
Qiao Wang,Joseph George
### Background
在快速城市化地区，监测家庭用水需要成本高昂且耗时的调查方法。本研究探索了使用公开可用的卫星图像碎片、谷歌街景（GSV）细分以及简单的地理空间协变量（夜光强度、人口密度）来预测印度Hubballi-Dharwad地区的家庭用水量的可能性。研究对比了几种方法：调查特征（基准）、卷积神经网络嵌入（卫星、GSV、结合）以及GSV语义地图结合辅助数据。
### Innovation
研究采用公开的遥感图像和街景图像，结合简单的地理空间协变量，提出了预测家庭用水量的新方法，尤其是在缺少传统调查数据的情况下，展示了Open-Access图像与少量地理空间数据结合的有效性，接近传统调查模型的准确度。同时，研究还对比了家庭用水量估计与主观收入估计之间的差异，揭示了视觉代理在中等消费群体中的混淆问题。
### Conclusion
研究表明，开源图像结合少量地理空间数据为在城市分析中获得可靠的家庭用水量估计提供了一种有前景的替代方法，这对需要准确家庭用水数据的城市规划和水资源管理至关重要。
## 493. `cs.LG` - 留意差距：审核并减少大规模移动预测中的群体不平等 [PDF](https://arxiv.org/pdf/2510.26940), [HTML](https://arxiv.org/abs/2510.26940)
### Authors
Ashwin Kumar,Hanyu Zhang,David A. Schweidel,William Yeoh
### Background
基于位置的下一个地点预测广泛应用于移动性、零售和公共卫生等领域，但其社会影响尚未得到充分研究。当前研究通过对大规模数据集训练的最先进的移动性预测模型进行审计，揭示基于用户人口统计学的隐藏差异。分析得出主流族裔用户组之间的预测性能差异，揭示数据集底层系统性差异导致的准确率差异。
### Innovation
提出了一种基于公平性的增量采样策略(FGIS)，能在增量数据收集场景中使用群体感知进行采样。为了在缺乏个体级人口统计标签的情况下进行分类，引入了适当的K均值聚类方法(SAKM)，该方法在潜在移动空间中将用户分组，并强制实现符合普查数据组的比例。该方法通过自动化标签为四个最大的群体(亚裔、非裔、西班牙裔和白人)生成代理种族标签。开发的采样算法优先考虑基于预计性能增益和当前组内代表性较低的用户，从而通过增量构建训练数据集，减少人口统计学性能差距同时保持总体准确性。方法在最先进的MetaPath2Vec模型和变压器编码器模型上评估，即使在资源有限的情况下也显示出公平意识策略的重要性。
### Conclusion
本研究揭示了移动预测管道中的结构性不平等问题，并展示了如何通过轻量级的数据驱动干预措施减少不公平性，尤其是对于数据量有限的应用场景。
## 494. `cs.LG` - BI-DCGAN：一种高效且多样性的GANs的理论基础贝叶斯框架 [PDF](https://arxiv.org/pdf/2510.26892), [HTML](https://arxiv.org/abs/2510.26892)
### Authors
Mahsa Valizadeh,Rui Tuo,James Caverlee
### Background
生成对抗网络 (GANs) 在生成合成数据方面非常擅长，但它们仍然受到模式崩溃的困扰，即生成器产生的输出范围狭窄，能够欺骗判别器，但却未能捕获数据的完整分布。这一点在多样性和对不确定性意识要求高的现实世界应用中尤其成为一个问题。因此，研究者引入了一种名为 BI-DCGAN 的方法，以通过对生成过程引入模型不确定性来解决这一问题，同时保持计算效率。BI-DCGAN 采用 Bayes by Backprop 来学习网络权重的分布，并使用均值场变分推断来有效地近似 GAN 训练过程中的后验分布。理论分析表明，贝叶斯建模能够提升样本多样性，虽然这两者对于现实应用而言是至关重要的，但传统 GAN (如 DCGAN) 仍未能很好地解决这些问题，特别是在训练效率上。现有的替代方案如扩散模型太过资源密集型，难以满足需求。因此，这需要一种高效的解决方案来应对多样性和不确定性的挑战
### Innovation
提出了一种名为 BI-DCGAN 的 GANs 扩展模型，通过引入贝叶斯不确定性来解决模式崩溃问题，并通过理论证明了该方法能够在生成对抗网络中提升样本的多样性。BI-DCGAN 使用 Bayes by Backprop 和均值场变分推断来在保持计算效率的同时实现这一目标，从而填补了现有 GANs 方法的空白，特别是在提高泛化能力和适应现实世界应用方面。该模型通过广泛的标准生成基准实验验证了其能力，表明其生成的输出更为多样且稳健，同时保持了训练效率
### Conclusion
BI-DCGAN 提供了一种在多样性和不确定性上相对平衡的解决方案，适用于那些需要高度多样性和较低资源需求的应用场景，在技术层面上为生成对抗网络的广泛应用铺平了道路。该项研究为现代 GANs 提供了理论依据，并在实际应用中取得了显著成果，显示了 BI-DCGAN 拥有良好的扩展性和及时性
## 495. `cs.LG` - HADSF：解释推荐中的方面意识语义控制 [PDF](https://arxiv.org/pdf/2510.26994), [HTML](https://arxiv.org/abs/2510.26994)
### Authors
Zheng Nie,Peijie Sun
### Background
近年来，大规模语言模型（LLMs）的进步为基于评论的推荐系统的信息提取提供了更有效的手段。然而，当前方法仍存在以下问题：（i）在没有范围控制的情况下挖掘自由文本评论，导致冗余和噪声表示；（ii）缺乏将LLM幻觉与下游效果关联起来的原理性度量标准；（iii）对不同模型规模的成本-质量权衡探索不足。
### Innovation
本文提出了Hyper-Adaptive Dual-Stage Semantic Framework (HADSF)框架，这是一种两阶段方法，首先通过自适应选择诱导一个紧凑的语料库级别方面词汇表，然后利用词汇引导的、明确约束的提取操作，提取结构化的方面-意见三元组。为了评估生成表示的准确性，引入了Aspect Drift Rate (ADR) 和 Opinion Fidelity Rate (OFR) 两个度量标准，并通过实验证明，HADSF可以减少预测误差，使较小的模型在代表性部署场景中实现与大型模型相当的表现。
### Conclusion
实验结果显示，在标准评分预测器中集成HADSF可以持续减少预测误差，并能使较小的模型在代表性部署场景中实现与大型模型相当的表现。本文还提供了代码、数据管道和度量实施，以支持对幻觉意识的LLM增强可解释推荐的可重复研究。
## 496. `cs.LG` - Mixture-of-Transformers 学习更快：对分类问题的理论研究 [PDF](https://arxiv.org/pdf/2510.27004), [HTML](https://arxiv.org/abs/2510.27004)
### Authors
Hongbo Li,Qinhang Wu,Sen Lin,Yingbin Liang,Ness B. Shroff
### Background
Mixture-of-Experts（MoE）模型能够提高变压器的效率，但在允许前向传播和注意层专业化的条件下缺乏统一的理论解释。研究人员探讨了Mixture-of-Transformers（MoT）模型，这是一种可计算的理论框架，其中每个变压器层作为由连续训练门控网络控制的专家。
### Innovation
研究开发了包含门控网络连续训练的三阶段训练算法，发现每个变压器专家都专精于不同的任务类别，并且门控网络能够准确地将数据样本路由到正确的专家。研究表明专家专业化减少了梯度冲突，并使得每个子任务变得强烈凸。通过大规模实证实验验证理论结论，证明了MoT的实际有效性。
### Conclusion
这些结果为大型模型的变压器层级专业化和学习动态提供了第一个统一的理论解释，提供了设计高效大型模型的实际指导。
## 497. `cs.LG` - Jasmine：一种简单、高性能且可扩展的JAX基_world模拟代码库 [PDF](https://arxiv.org/pdf/2510.27002), [HTML](https://arxiv.org/abs/2510.27002)
### Authors
Mihir Mahajan,Alfred Nguyen,Franz Srambical,Stefan Bauer
### Background
随着世界模型被越来越多地认为是解决机器人等领域的数据稀缺问题的途径，公开的训练基础设施对于世界建模仍然处于初级阶段。因此，开发一种高性能、可扩展的world modeling代码库具有重要意义。
### Innovation
Jasmine是一种基于JAX的世界建模代码库，能够在不进行大量代码更改的情况下，从单个主机扩展到数百个加速器，并且在CoinRun案例研究的复现速度上比先前的开源实现快了几个数量级。通过各种数据加载、训练和检查点的性能优化，Jasmine提高了复现性并支持多样化的分割配置。通过与精心挑选的大规模数据集结合使用，Jasmine为不同模型家族和架构消融的严格基准测试框架奠定了基础。
### Conclusion
Jasmine作为一个高效、可扩展且易于复现的世界建模代码库，为提高世界建模领域的实验效率和评估准确性提供了解决方案。
## 498. `cs.LG` - 一种公平评估变异感知bandit算法的框架 [PDF](https://arxiv.org/pdf/2510.27001), [HTML](https://arxiv.org/abs/2510.27001)
### Authors
Elise Wolf
### Background
多臂老虎机（MAB）问题作为更复杂的强化学习算法的基础构建块，但在评估和比较MAB算法时面临挑战，主要是缺乏标准化条件和可复制性，特别是在环境变化时。对于如UCB的经典方法的变异感知扩展而言，其性能高度依赖于底层环境，这导致直接比较变得困难。
### Innovation
本文提出了一种可重复的评估框架，系统比对了八种经典和变异感知的MAB算法。评估框架在Bandit Playground代码库中实现，具有明确的实验设置、多种性能指标（奖励、遗憾、奖励分布、尾风险和动作最优性）以及交互式评估界面，确保分析的持续性和透明度。结果显示，在不确定性高的环境中，变异感知算法可以提供优势；相比之下，在更可分的情景或经过大量调优时，经典算法可能具有相同或更好的表现。
### Conclusion
本文的贡献是提供一种系统评估MAB算法的框架，并揭示了变异感知方法超越其经典对应物的条件。
## 499. `cs.LG` - 梯度下降作为损失景观导航：一种推导学习规则的规范框架 [PDF](https://arxiv.org/pdf/2510.26997), [HTML](https://arxiv.org/abs/2510.26997)
### Authors
John J. Vastola,Samuel J. Gershman,Kanaka Rajan
### Background
学习规则的更新模型参数方法通常被假定而不是 derive 出来。不同学习规则为何效果不同以及在何种条件下哪种规则能被视作最优的机制仍不清楚。本文提出了一种理论框架，将学习规则视为在部分可观测损失景观中导航的策略，并确定最优规则为关联最优化控制问题的解。在不同假设下，这一框架自然地推导出一系列广为人知的学习规则，如从短期优化的角度出发的梯度下降，从长时规划角度的动量，考虑参数空间几何的自然梯度，部分可控性的非梯度规则，以及像 Adam 这样的自适应优化器。此外，文章指出持续学习策略如权重重置可以被理解为对任务不确定性做出的最佳响应。通过统一这些现象在单一目标下，本文框架澄清了学习的计算结构，并提出了设计自适应算法的指导原则。
### Innovation
提出了一种理论框架，将学习规则视为在部分可观测损失景观中导航的策略，并确定最优规则为关联最优化控制问题的解。这一框架自然地推导出一系列广为人知的学习规则，如从短期优化的角度出发的梯度下降，从长时规划角度的动量，考虑参数空间几何的自然梯度，部分可控性的非梯度规则，以及像 Adam 这样的自适应优化器。此外，本文提出了持续学习策略理解任务不确定性的重要性。
### Conclusion
通过统一这些现象在单一目标下，本文框架澄清了学习的计算结构，并提出了设计自适应算法的指导原则。
## 500. `cs.LG` - RLVR在数学推理中的泛化能力限制：两个案例研究 [PDF](https://arxiv.org/pdf/2510.27044), [HTML](https://arxiv.org/abs/2510.27044)
### Authors
Md Tanvirul Alam,Nidhi Rastogi
### Background
大语言模型在数学推理方面面临着重要挑战，不仅需要给出正确的答案，还需要具备可信的推理过程。虽然可验证奖励强化学习（RLVR）被证明是提升这一能力的有前途的方法，但其促进真正推理能力的潜力尚不清楚。
### Innovation
研究选择了两种具有完全可验证解的问题进行RLVR方法的实验：活动调度和最长递增子序列，并采用精心策划的数据集以独一无二的最优解为基础。多次奖励设计中，发现RLVR可以提升评估指标，但其往往通过强化表面的启发式方法而非掌握新的推理策略，从而揭示了RLVR泛化的局限。
### Conclusion
研究结果强调了RLVR泛化的限制，突出了分离真正数学推理和短视策略利用的重要性，并提供了进步的忠实度指标。
## 501. `cs.LG` - 长度正则化在变换器中的定量界限 [PDF](https://arxiv.org/pdf/2510.27015), [HTML](https://arxiv.org/abs/2510.27015)
### Authors
Zachary Izzo,Eshaan Nichani,Jason D. Lee
### Background
黄等人（2025）的研究表明，当训练序列长度超过某个有限阈值时，变换器最终能够实现长度正则化，但对所需的最小训练序列长度未给出具体答案。
### Innovation
本研究提供了长度正则化所需的训练序列长度的首个定量界限，分析了$bm{text{l_text{∞}}} bm{text{误差控制}}$ vs. 平均误差控制、无限精度 softmax 注意力 vs. 有限精度注意力、单层 vs. 双层变换器等不同问题情境下的长度正则化效果，证明了当变换器对更长序列的内部行为可以在以较短序列训练时的行为进行模拟时，长度正则化就会发生。
### Conclusion
研究结果深化了我们对变换器在长序列上外推机制的理论理解，并量化地说明了更复杂任务中所需训练数据的丰度对于正则化的重要性。
## 502. `cs.LG` - 使用组合融合提升情感分类 [PDF](https://arxiv.org/pdf/2510.27014), [HTML](https://arxiv.org/abs/2510.27014)
### Authors
Sean Patten,Pin-Yu Chen,Christina Schweikert,D. Frank Hsu
### Background
本文提出了一种新颖的情感分类方法，通过应用组合融合分析（CFA）来整合多种机器学习模型，从而在IMDB情感分析数据集上获得了97.07%的顶级准确率。CFA 利用认知多样性的概念，通过量化模式之间的差异性并将它们的预测策略性结合，实现模型之间多样性的有效利用和融合。文章中的方法将基于转换单元的RoBERTa架构模型与传统的机器学习模型（如随机森林、支持向量机和XGBoost）结合在一起。与传统单个模型规模扩展的方法相比，CFA 更加高效地利用计算资源。实验结果表明，CFA 在准确率方面超过了传统的集成方法，有效利用和计算了模型之间的多样性。
### Innovation
本文提出了一种新的情感分类方法，通过将组合融合分析（CFA）应用于多种机器学习模型的融合。CFA 利用认知多样性，通过量化模型之间的差异性并策略性地结合它们的预测，实现了多样性的有效利用和融合。相比于扩展单个模型规模的方法，CFA 更加高效地利用计算资源。此外，该方法结合了RoBERTa架构模型与传统的机器学习模型，增强了模型的多样性，从而提高了情感分类的准确率和效率。
### Conclusion
实验结果表明，通过组合融合分析（CFA）整合RoBERTa架构模型与传统机器学习模型，可以实现情感分类的高性能。相较于传统的集成方法，CFA 能够更有效地利用模型多样性，提高分类准确率。该方法展示了在情感分类任务中使用融合分析的有效性，并为未来的情感分析方法提供了一种创新思路。
## 503. `cs.LG` - 迈向算法相似性度量 [PDF](https://arxiv.org/pdf/2510.27063), [HTML](https://arxiv.org/abs/2510.27063)
### Authors
Shairoz Sohail,Taher Ali
### Background
在相同的问题上提供了两个算法时，我们能否确定它们是否在意义上有所不同？尽管在一个特定领域内完全确定算法的相似性是不现实的，并且由于不同的相似性概念的竞争使得实践中的判断更为复杂。但在许多应用中（如克隆检测或程序合成），需要一个实用的并且一致的相似性度量。现有的一些等价性和相似性概念被回顾，并引入了EMOC框架：一个评估-内存-运算复杂度框架，用于将算法实现嵌入到适合下游任务的功能空间中。从中展示了EMOC特征支持算法类型的聚类和分类、接近重复的检测以及对LLM生成程序的多样性量化。开源项目包括计算EMOC嵌入的代码、数据和技术工具，以促进结果的可重复性和未来的算法相似性研究工作。
### Innovation
EMOC框架将算法实现嵌入到一个适合下游任务的功能空间中。EMOC实现了对算法类型的聚类和分类，检测接近重复，并量化LLM生成程序的多样性。开源项目包括计算EMOC嵌入的代码、数据和技术工具，以促进结果的可重复性和未来的算法相似性研究工作。
### Conclusion
EMOC框架支持对算法类型的聚类和分类，检测接近重复，并量化LLM生成程序的多样性。开源项目促进了结果的可重复性和未来的工作。
## 504. `cs.LG` - 一致性训练有助于阻止奉承和逃逸 [PDF](https://arxiv.org/pdf/2510.27062), [HTML](https://arxiv.org/abs/2510.27062)
### Authors
Alex Irpan,Alexander Matt Turner,Mark Kurzeja,David K. Elson,Rohin Shah
### Background
大语言模型（LLM）可能因提示的简单更改而失去其事实性和拒绝能力，通常会接受用户信念（如趋承行为）或满足不当请求。研究者探索了一种叫做一致性训练的方法，这是一种自我监督的学习框架，旨在让模型对某些无关提示线索保持不变。这些方法教导模型在提示数据增强（如增加前导问题或逃逸文本）时表现一致，以减少LLM对无关提示信息的敏感性，提高其抗干扰能力。
### Innovation
该研究提出了一致性训练方法，通过两种方式——偏置增强一致性训练（Bias-augmented Consistency Training, BCT）和激活一致性训练（Activation Consistency Training, ACT）——来减少模型对无关提示信息的敏感性。BCT通过外部输出的一致性来实现，而ACT则通过内部激活的一致性来实现。相较于BCT和ACT在减少趋承行为方面表现相同，BCT在减少逃逸减少方面表现更好。此外，一致性训练使用模型自身的响应作为训练数据，避免了由过时数据引起的模型能力退化和响应准则陈旧化的问题。
### Conclusion
一致性训练能够减少模型对无关提示信息的敏感性，有助于解决LLM的趋承性和逃逸问题。尽管两种方法在减少趋承行为方面效率相仿，但BCT在减少逃逸行为方面更为有效。研究者认为一致性训练可以简化训练流程，减少对静态数据集的依赖，并且能够视某些对齐问题为一致性问题而非最佳响应问题来进行处理。
## 505. `cs.LG` - MLPerf Automotive [PDF](https://arxiv.org/pdf/2510.27065), [HTML](https://arxiv.org/abs/2510.27065)
### Authors
Radoyeh Shojaei,Predrag Djurdjevic,Mostafa El-Khamy,James Goel,Kasper Mecklenburg,John Owens,Pınar Muyan-Özçelik,Tom St. John,Jinho Suh,Arjun Suresh
### Background
现有的基准套件无法用于评估用于汽车系统AI加速的机器学习系统，因为汽车工作负载具有独特的安全性和实时处理约束，这些约束区分了之前引入基准所针对的领域。因此，需要标准化性能评估方法，以确保不同硬件平台和软件实现之间的一致性和可重现性性能比较。现有的基准套件无法满足这些独特需求，因此有必要创建专门服务于汽车机器学习系统的标准化公开基准。
### Innovation
MLPerf Automotive 是首个专门用于评估部署在汽车系统中的机器学习系统的标准化公开基准。它通过与 MLCommons 及自主车辆计算联盟的合作开发，提供延迟和准确性的评价指标，以及一致性重复性能比较的评估协议。此外，该基准框架特别涵盖了汽车感知任务中的2D物体检测、2D语义分割和3D物体检测。
### Conclusion
文章描述了基准设计方法，包括任务选择、参考模型以及提交规则。同时讨论了首次基准提交过程中遇到的挑战和数据集获取以及开发参考实现的工程努力。基准代码公开可用。
## 506. `cs.LG` - 理解LLM推理中的自玩游戏 [PDF](https://arxiv.org/pdf/2510.27072), [HTML](https://arxiv.org/abs/2510.27072)
### Authors
Justin Yang Chae,Md Tanvirul Alam,Nidhi Rastogi
### Background
大规模语言模型（LLM）的推理进步，尤其是借助可验证奖励的强化学习（RLVR），激发了训练后自我游戏的应用，这种方法通过生成和解决自身问题来进行自我提升。尽管自我游戏在领域内外都显示出强大的性能提升，但其背后的机制仍然不完全明了。这项研究通过分析绝对零推理器的训练动态，对比自我游戏、RLVR和监督微调（SFT），探究参数更新稀疏性、令牌分布的熵动态以及替代提议者奖励函数，最终通过pass@k评价连接这些动态与推理性能之间的关系，以清晰阐述自我游戏与其它训练后策略的不同之处，揭示其固有限制，并指明未来通过自我游戏改进LLM数学推理的方向
### Innovation
这项研究通过绝对零推理器分析自我游戏的训练动态，比较自我游戏与RLVR和SFT的差异，探讨参数更新稀疏性、令牌分布的熵动态以及探索不同的提议者奖励函数，通过pass@k评价来关联这些动态与推理能力，从而清晰展现自我游戏的独特之处，其固有限制及改进方向
### Conclusion
研究揭示了自我游戏与其它训练后策略之间的区别，指出了其内在限制，并为通过自我游戏改进LLM数学推理指明了未来的研究方向
## 507. `cs.LG` - QiNN-QJ：一种用于多模态情感分析的量子跃迁启发式神经网络 [PDF](https://arxiv.org/pdf/2510.27091), [HTML](https://arxiv.org/abs/2510.27091)
### Authors
Yiwei Chen,Kehuan Yan,Yu Pan,Daoyi Dong
### Background
量子理论提供了诸如叠加和纠缠等非经典原理，这些原理启发了在机器学习中的潜在范式。然而，现有的许多量子启发式融合模型仅依赖于幺正或幺正似然变换来生成量子纠缠。尽管在理论上表达能力强，但这种方法往往会导致训练稳定性差和泛化能力受限。文章背景在于当前多模态纠缠建模存在的问题，以及现有方法在复杂跨模态相关性建模上的不足。
### Innovation
本文提出了一个多模态纠缠建模的量子启发式神经网络（QiNN-QJ），其中每个模态都首先编码为量子纯状态，然后通过一个模拟量子跃迁操作符的不同模块来将分离的乘积状态转化为纠缠表示。通过联合学习哈密顿算子和林德施特算子，QiNN-QJ 生成了有可控性的跨模态纠缠，并通过耗散动力学来稳定训练和限制纠缠塑造。此外，QiNN-QJ 还可以通过冯·诺伊曼纠缠熵实现增强的后验可解释性。
### Conclusion
该工作建立了一个原则性的框架用于纠缠的多模态融合，并为进一步利用量子启发式方法建模复杂的跨模态相关铺平了道路。
## 508. `cs.LG` - 组敏感的离线上下文多臂老虎机 [PDF](https://arxiv.org/pdf/2510.27123), [HTML](https://arxiv.org/abs/2510.27123)
### Authors
Yihong Guo,Junjie Luo,Guodong Gao,Ritu Agarwal,Anqi Liu
### Background
离线上下文多臂老虎机允许用历史数据学习策略，而无需在线交互。然而，最大化总体预期奖励的离线策略优化可能会无意中放大不同群体间的奖励差距，某些群体可能因学习到的策略而受益更多，特别是在资源有限的情况下，这引发了公平性方面的关注。
### Innovation
本文研究了离线下文多臂老虎机中的群体敏感公平性约束，旨在降低在策略学习过程中可能产生的群体间奖励差距。提出了基于组间奖励差距约束的约束离线策略优化框架，并引入双重稳健估算器来改进训练过程中组间奖励差距的估计，同时提供了策略优化的收敛性保证。
### Conclusion
对合成和实际数据集的实验证明，本方法能有效减少奖励差距，同时保持竞争力的总体性能。
## 509. `cs.LG` - 人类月经周期中子宫内膜基因去卷积和功能分析的层序贝叶斯模型 [PDF](https://arxiv.org/pdf/2510.27097), [HTML](https://arxiv.org/abs/2510.27097)
### Authors
Crystal Su,Kuai Yu,Mingyuan Shao,Daniel Bauer
### Background
现有的bulk RNA测序方法会提供平均的转录表达谱，掩盖了不同细胞类型特异性的动态变化。本研究以此为背景，探讨了在月经周期中子宫内膜细胞类型比例和特定基因表达变化的动态变化。
### Innovation
研究提出了一种层序贝叶斯概率模型，能够将bulk RNA-seq数据分解为组成细胞类型表达谱和比例，通过高分辨率单细胞参考数据来实现。该模型在月经周期中的子宫内膜组织的应用展示出了周期阶段间的细胞类型比例动态变化，以及特定细胞类型相关的差异基因表达与子宫功能的关系。
### Conclusion
该研究模型通过模拟和与现有方法的比较验证了其性能，揭示了不同细胞类型在月经周期各阶段的动态变化，并讨论了该研究对生育和子宫疾病临床意义以及未来的研究方向，包括空间转录组学的整合。研究表明，贝叶斯方法对参考不匹配和噪音具有鲁棒性。
## 510. `cs.LG` - AI Agents in Drug Discovery [PDF](https://arxiv.org/pdf/2510.27130), [HTML](https://arxiv.org/abs/2510.27130)
### Authors
Srijit Seal,Dinh Long Huynh,Moudather Chelbi,Sara Khosravi,Ankur Kumar,Mattson Thieme,Isaac Wilks,Mark Davies,Jessica Mustali,Yannick Sun,Nick Edwards,Daniil Boiko,Andrei Tyrin,Douglas W. Selinger,Ayaan Parikh,Rahul Vijayan,Shoman Kasbekar,Dylan Reid,Andreas Bender,Ola Spjuth
### Background
人工智能（AI）代理正在成为药物发现领域的变革性工具，能够自主推理、行动和通过复杂的研发工作流程进行学习。这些具备感知、计算、行动和记忆工具的代理AI系统可以整合多元生物医学数据，执行任务，利用机器人平台进行实验，并通过闭环迭代改进假设。
### Innovation
本文综合介绍了代理AI架构，从ReAct和反思，到监督员和群系统，并展示了这些系统在药物发现关键阶段的应用，包括文献综合、毒性预测、自动化协议生成、小分子合成、药物再定位和端到端决策制定。本研究是首次全面展示在实际运营药物发现环境中部署的代理AI系统的实际实现和可量化影响的文章。初步实现显示了在速度、可复制性和可扩展性方面的显著提升，将原本需要数月的工作流程压缩到数小时，并保持科学追溯。
### Conclusion
当前面临的数据异质性、系统可靠性、隐私和基准测试挑战被视为需要重点关注的问题。未来方向将集中在技术支持科学和技术转化方面。
## 511. `cs.LG` - 功能嵌入使多区域SEEG记录在被试和会话之间聚集成为可能 [PDF](https://arxiv.org/pdf/2510.27090), [HTML](https://arxiv.org/abs/2510.27090)
### Authors
Sina Javadzadeh,Rahil Soroushmojdehi,S. Alireza Seyyed Mousavi,Mehrnaz Asadi,Sumiko Abe,Terence D. Sanger
### Background
跨被试聚集颅内记录具有挑战性，因为电极数量、位置和覆盖区域差异很大。MNI坐标等空间标准化方法提供了一个共同的解剖参考，但在精准定位不够的情况下难以捕捉真正的功能相似性；即使在匹配的解剖坐标下，个体之间的目标脑区和底层神经动态也可能有显著差异。
### Innovation
提出了一种可扩展的表征学习框架，该框架通过使用对比目标的双胞胎编码器从多个脑区的局部场电位中学习每个电极的被试无关的功能身份，诱导感知局部神经模式的嵌入几何结构；并且通过将这些嵌入进行分词来对变换器进行建模，该变换器使用可变数量的通道来建模跨区关系。该框架在包含基底神经节-丘脑区域的20名被试数据集上进行了评估，该数据集是在具有异质电极布局的灵活休息/运动记录会话中收集的。所学习的功能空间支持在单个被试内的准确区分，并形成清晰的、区域一致的聚类；该变换器可以在没有被试特定头部或监督的情况下直接处理功能标记，捕获跨区域依赖关系，并能重构被遮罩的通道，提供一种被试无关的基础结构，用于下游解码。
### Conclusion
这些结果表明，通向大规模跨境聚集和颅内神经数据预训练的道路，即使缺少严格的任务结构和统一的传感器布局。
## 512. `cs.LG` - 探索大型语言模型生成的解释在提升自动化作文评分中的用途 [PDF](https://arxiv.org/pdf/2510.27131), [HTML](https://arxiv.org/abs/2510.27131)
### Authors
Hong Jiao,Hanna Choi,Haowei Hua
### Background
本研究探讨了由GPT-4.1和GPT-5生成的解释在使用Prompt 6作文（来自2012年Kaggle ASAP数据集）进行自动化评分中的应用。研究对比了基于作文和基于解释的评分方法。
### Innovation
研究发现，基于作文的评分方法在总分上优于基于解释的评分方法，但在处理比例不平衡的情况下，基于解释的评分方法在分数为0的情况下表现更好。组合基于作文的评分模型提高了特定分数水平和总体评分水平上的评分准确性。综合考虑基于作文的评分和基于解释的评分的模型与单一模型相比，表现相似，但综合考虑所有基于作文和基于解释的评分则取得了最好的评分准确性，Quadratic Weighted Kappa (QWK)值达到了0.870，高于文献报道的0.848。
### Conclusion
组合基于作文的评分和基于解释的评分可实现更准确的自动化评分。
## 513. `cs.LG` - FairAD：基于代数距离的高效公平图聚类 [PDF](https://arxiv.org/pdf/2510.27136), [HTML](https://arxiv.org/abs/2510.27136)
### Authors
Minh Phu Vuong,Young-Ju Lee,Iván Ojeda-Ruiz,Chul-Ho Lee
### Background
由于人们对机器学习模型对某些人群不公正行为的关注不断增加，公平性已成为学术界关注的焦点，从而推动了图聚类中公平性研究的发展。传统图聚类旨在将图中的节点集划分为符合条件数量的互斥簇，但要将公平性约束整合到现有图聚类算法中特别困难，尤其是在处理大型图时。
### Innovation
本文提出了一种名为FairAD的高效公平图聚类方法。首先根据代数距离（algebraic distance）构建一种新的亲和度矩阵，并在此矩阵上执行图粗化过程以找到对应的簇中心节点，然后通过求解带有公平性约束的最小化问题来完成聚类过程。实验结果表明，与现有的公平图聚类算法相比，FairAD不仅可以实现公平聚类，而且性能提高了40倍。
### Conclusion
FairAD能够在保持公平性的同时，显著提高图聚类的效率。
## 514. `cs.LG` - 沿着山谷探索景观点以寻找更好的极小值 [PDF](https://arxiv.org/pdf/2510.27153), [HTML](https://arxiv.org/abs/2510.27153)
### Authors
Tong Zhao,Jiacheng Li,Yuanchang Zhou,Guangming Tan,Weile Jia
### Background
在深度学习中，找到较低且泛化效果更好的极小值至关重要。然而，大多数现有优化器在达到局部极小值后会停止搜索参数空间。由于损失景观复杂的几何性质，难以保证该点是全局最低点或提供最佳泛化效果。
### Innovation
论文提出了一种适应器'E'，用于基于梯度的优化器。该适应器优化器倾向于继续探索低且几乎相同的损失区域（即山谷），即使在达到局部极小值后也会继续搜索潜在更好的局部极小值。这种方式增加了找到较低且平坦的局部极小值的可能性，通常此类极小值与更好的泛化效果相关。此外，论文证明了适应器优化器在凸性和非凸场景下的收敛性。
### Conclusion
实验结果表明，适应器Lamb（ALTO）在大型批次训练等重要但极具挑战性的训练场景中，可以将当前最优优化器的测试准确率（泛化效果）平均提高2.5%。这项工作可能为优化算法的设计开辟了新的研究方向。
## 515. `cs.LG` - 专家软任务感知路由在共变代表学习中的应用 [PDF](https://arxiv.org/pdf/2510.27222), [HTML](https://arxiv.org/abs/2510.27222)
### Authors
Jaebyeong Jeon,Hyeonseo Jang,Jy-yong Sohn,Kibok Lee
### Background
共变代表学习旨在捕捉输入变换在代表空间中的变化，不变代表学习则通过忽略这些变换来编码语义信息。最近的研究表明，共同学习这两种类型的表示对于下游任务通常是有益的，通常通过使用分离的投影头来实现。然而，这种设计忽略了不变学习和共变学习之间共享的信息，导致冗余特征学习和模型容量的低效使用。
### Innovation
我们提出了一种称为Soft Task-Aware Routing (STAR)的投影头路由策略，将它们建模为专家。STAR使专家能专门化于捕获共享或任务特定的信息，从而减少冗余特征学习。通过观测不变和共变嵌入的标准相关性降低来验证这种效果。实验结果表明，STAR在多种迁移学习任务中表现出一致性改进。
### Conclusion
STAR策略通过有效利用共享信息减少了冗余特征学习，提高了多种迁移学习任务的表现，证明了联合学习不变和共变代表的有效性。
## 516. `cs.LG` - MDAS-GNN：用于城市交通风险预测的多维度时空图神经网络及其空间扩散机制 [PDF](https://arxiv.org/pdf/2510.27197), [HTML](https://arxiv.org/abs/2510.27197)
### Authors
Ziyuan Gao
### Background
交通事故是公共卫生的重大挑战，每年全球造成超过135万人死亡。传统的事故预测模型将道路段独立处理，未能捕捉城市交通网络中的复杂空间关系和时间依赖性。
### Innovation
该研究开发了MDAS-GNN，这是一种多维注意力空间扩散图神经网络，整合了交通安全性、基础设施和环境风险三个核心风险维度。该框架采用特征特定的空间扩散机制和多头时间注意力机制，来捕捉不同时间范围内的依赖关系。
### Conclusion
MDAS-GNN在英国运输部在中央伦敦、南曼彻斯特和伯明翰东南部的数据上表现优于现有基准方法。模型在短期、中期和长期预测中保持低预测误差，特别是在长期预测中表现出色。剔除分析表明，综合多维度特征优于单一特征方法，预测错误最多可减少40%。该框架为交通基础设施设计提供了高级预测能力，有助于基于数据的决策，用于道路网络优化、基础设施资源改进和城市开发项目的安全干预策略。
## 517. `cs.LG` - 基于亲和度评分的关系意识的DBMS配置的贝叶斯优化 [PDF](https://arxiv.org/pdf/2510.27145), [HTML](https://arxiv.org/abs/2510.27145)
### Authors
Sein Kwon,Seulgi Baek,Hyunseo Yang,Youngwan Jo,Sanghyun Park
### Background
数据库管理系统(DBMSs)是管理大规模和异构数据的基础，其性能受到配置参数的影响。有效的参数调整对于适应多样化的负载并最大化吞吐量、最小化延迟至关重要。现有的研究主要集中在使用机器学习的自动化配置优化上，但现有方法仍存在几个关键限制。大多数调优框架忽略了参数之间的依赖性，假设每个参数独立工作。这种简化使优化器无法利用参数间的相关效果，限制了其捕捉性能关键互作的能力。此外，为了简化高维搜索空间的复杂性，先前的工作通常只选择最 top 的几个参数进行优化，而忽略了那些对性能有实质性贡献的其他参数。最常用的自动调优方法贝叶斯优化(Bayesian Optimization, BO)也受到其对代理模型的依赖的限制，这可能导致不稳定的预测和探索效率低下。
### Innovation
提出了一种名为 RelTune 的新框架，该框架将参数依赖关系表示为 Relational Graph，并利用基于图形神经网络(GNN)的学习隐式嵌入来编码相关性能意义。RelTune 进一步引入了一种新的框架——Hybrid-Score-Guided Bayesian Optimization (HBO)，该框架结合了代理预测与衡量到先前高性能配置接近程度的亲和度评分。实验结果表明，RelTune 在多个 DBMS 和工作负载场景中的优化效率优于传统的基于 BO 的方法，实现了最先进的性能。
### Conclusion
我们的方法通过更好地捕捉参数间的依赖性和关联性，以及引入一种综合评分指导的贝叶斯优化方法，相比既有的基于 BO 的调优方法，展示出了更快的收敛速度和更高的优化效率。我们验证了 RelTune 在多个 DBMS 和工作负载场景下的卓越性能，将其与最先进的性能进行对比。
## 518. `cs.LG` - SERFLOW：一种针对SLO感知动态机器学习推理的跨服务成本优化框架 [PDF](https://arxiv.org/pdf/2510.27182), [HTML](https://arxiv.org/abs/2510.27182)
### Authors
Zongshun Zhang,Ibrahim Matta
### Background
动态将机器学习模型的各个部分卸载到不同的资源配置服务，如Function-as-a-Service (FaaS) 和 Infrastructure-as-a-Service (IaaS)，可以平衡处理和传输延迟，同时最小化自适应推断应用的成本。然而，先前的研究通常忽视了现实因素，例如虚拟机冷启动、长期尾部服务时间分布中的请求等。 SERFLOW通过利用基于FaaS的无服务器函数（容器）并根据不同阶段请求退出的比例进行特定阶段的资源配置解决了这些问题，从而实现在动态工作负载下低成本、高效率地适应性负载均衡。
### Innovation
SERFLOW通过考虑每个请求在不同阶段的退出率，区别化地为FaaS和IaaS资源配置。通过这种特定阶段资源分配的方式，可以有效减少早期请求导致的资源浪费，同时避免大型请求波高峰底波动导致的资源过度配置问题。整体上，SERFLOW能够降低超过23%的云成本，同时更为灵活地适应动态工作负载的变化。
### Conclusion
SERFLOW提供了一种通过跨服务的资源优化来降低成本的框架，特别是针对需要自适应推断的动态机器学习应用，通过基于请求数量的动态负载均衡，同时利用FaaS和IaaS的优势，实现了成本显著降低和高效的工作负载适应性。
## 519. `cs.LG` - Feature-Function Curvature Analysis: 一种用于解释可微模型的几何框架 [PDF](https://arxiv.org/pdf/2510.27207), [HTML](https://arxiv.org/abs/2510.27207)
### Authors
Hamed Najafi,Dongsheng Luo,Jason Liu
### Background
解释性人工智能(XAI)对于建立对复杂机器学习模型的信任至关重要。主流的归因方法通常只能提供模型最终状态的一个不完备、静态的画面。这种方法会因为不线性和交互性的问题而混淆特征的作用。为解决这些问题，介绍了Feature-Function Curvature Analysis (FFCA) 新型框架，该框架分析了模型学习函数的几何形状。FFCA为每个特征生成一个4维签名，量化其影响力、变化性、非线性和交互性。
### Innovation
这种方法扩展了FFCA框架，引入了Dynamic Archetype Analysis，它可以跟踪特征签名在整个训练过程中的演变。这种方法不仅解释了模型学到了什么，还揭示了模型是如何学习的。这项动态分析还为识别模型容量不足和预测过拟合提供了新的、实用的诊断工具。实验结果显示，FFCA通过其静态和动态部分提供了几何上下文，使其能够将模型解释从简单的量化转变成为整个学习过程提供细微、可信的分析。
### Conclusion
FFCA通过其静态和动态组成部分，提供了模型解释的关键几何背景，将模型解释从单一的量化分析提升到了整个学习过程的深入、可靠的分析。这种动态分析还揭示了模型学习的层次结构，显示了模型始终先学习简单的线性效应再学习复杂的交互效应，为模型解释提供了一种全新的视角。
## 520. `cs.LG` - 一种在较弱条件下改进后 regrets 边界的多项式时间在线稀疏线性回归算法 [PDF](https://arxiv.org/pdf/2510.27177), [HTML](https://arxiv.org/abs/2510.27177)
### Authors
Junfan Li,Shizhong Liao,Zenglin Xu,Liqiang Nie
### Background
本文研究了在线稀疏线性回归（OSLR）问题，在这种情况下，算法只能访问每个实例的 d 个属性中的 k 个来预测。这个问题已被证明是 NP 难问题。先前的工作假设数据矩阵满足特征的线性独立性、兼容条件或压缩近似性质，给出了多项式时间的算法。本文的新算法在兼容条件下证明了改进的效果，这一条件比其他两种假设更弱，从而显著改进了之前的 regrets 边界。
### Innovation
本文引入了一个新的多项式时间算法，该算法在兼容条件下表现出色，改进了之前的工作（Ito et al., 2017）的 regrets 边界。新算法利用了广泛研究的 Dantzig 选择器，并结合了几个新颖的技术：算法自适应的采样方案用于估计协方差矩阵，自适应的参数调整方案，以及批次在线牛顿步法和谨慎的初始化。此外，提供了新的和非平凡的分析，包括对 $boldsymbol{theta}$-范数误差的归纳方法，对非独立随机变量协方差的仔细分析，以及将 regrets 分解的方法。还有，算法进一步扩展到带有额外观测值的在线稀疏线性回归，照此改进了之前的 regrets 边界（Kale et al., 2017; Ito et al., 2017）。
### Conclusion
本文介绍了一个多项式时间算法，该算法在较弱的兼容条件下改进了 regrets 边界。算法使用了 Dantzig 选择器，并结合了几个新颖的技术，证明了算法在 OSLR 问题中的有效性。此外，给出了对新的和重要的分析，进一步扩展了算法，使其能够应对在线稀疏线性回归中的额外观测值。
## 521. `cs.LG` - 并非所有实例都具有相同的价值：迈向影响加权数据集蒸馏 [PDF](https://arxiv.org/pdf/2510.27253), [HTML](https://arxiv.org/abs/2510.27253)
### Authors
Qiyan Deng,Changqian Zheng,Lianpeng Qiao,Yuping Wang,Chengliang Chai,Lei Cao
### Background
数据集蒸馏是一种将大容量数据集压缩成合成子集的方法，可以在大幅减少存储和计算成本的同时，实现与使用完整数据集训练相当的性能。现有数据集蒸馏方法通常假定所有真实实例对过程的贡献相等，但在实际应用中，真实数据集同时包含有用和冗余或甚至有害的实例，直接将完整数据集进行蒸馏而不考虑数据质量可能导致模型性能下降。因此，引入了一个新的议题：在数据集蒸馏过程中显式考虑数据质量的重要性。
### Innovation
提出了影响加权蒸馏（IWD），一种基于影响函数的框架，能够为每个实例分配自适应权值，根据其对蒸馏目标的估计影响，在蒸馏过程中优先选择有益数据，同时减少不太有用或有害数据的权重。由于其模块化设计，IWD可以无缝集成到多种数据集蒸馏框架中。实验结果表明，集成IWD能够提高蒸馏后数据集的质量，提升模型性能，可获得高达7.8%的准确率增益。
### Conclusion
研究证明，IWD在数据集蒸馏过程中考虑数据质量的有效性，并能够显著提高模型性能。
## 522. `cs.LG` - FedSM: Robust Semantics-Guided Feature Mixup for Bias Reduction in Federated Learning with Long-Tail Data [PDF](https://arxiv.org/pdf/2510.27240), [HTML](https://arxiv.org/abs/2510.27240)
### Authors
Jingrui Zhang,Yimeng Xu,Shujie Li,Feng Liang,Haihan Duan,Yanjie Dong,Victor C. M. Leung,Xiping Hu
### Background
联邦学习（FL）允许跨去中心化的客户端协作训练模型而不共享私有数据。然而，FL会因非IID和长尾数据分布而产生有偏差的全局模型。需要改进FL中的偏差问题，特别是在数据极度不平衡的情况下。该论文提出了一种新颖的客户端中心框架FedSM，通过语义指导的特征混合和轻量级分类器重新训练来减少偏差。FedSM 利用预训练的图像-文本对齐模型计算类别级别的语义相关性，指导局部特征与全局原型的混合，生成类一致的伪特征。这些特征可以纠正分类器的偏差，特别是当数据极度偏斜时。为了避免预训练模型与数据之间潜在的领域偏移问题，该论文提出了概率类别选择，以增强特征多样性，有效减少偏差。所有计算在本地进行，需要少量的服务器开销。实验证明，FedSM 在长尾数据集上展现出比最先进的方法更高的准确性和鲁棒性，同时具有良好的计算效率。
### Innovation
FedSM框架通过语义指导的特征混合和轻量级分类器重新训练，针对长尾数据在联邦学习中减少偏差。特别是在数据极度不平衡的情况下，提出的概率类别选择方法进一步增强了特征多样性，有效减少了偏差。所有计算都在本地执行，以确保服务器开销最小。此外，FedSM 在长尾数据集上的实验结果表明，它在准确性和对领域偏移的鲁棒性方面优于现有方法，并且计算效率也很高。
### Conclusion
FedSM 在联邦学习中通过语义指导的特征混合和轻量级分类器重新训练有效减少了长尾数据的偏差问题。实验结果证明了 FedSM 在长尾数据集上的优越性能，并在准确性、对领域偏移的鲁棒性和计算效率方面优于现有的最先进的方法。
## 523. `cs.LG` - ECVL-ROUTER: 针对视觉-语言模型的场景感知路由 [PDF](https://arxiv.org/pdf/2510.27256), [HTML](https://arxiv.org/abs/2510.27256)
### Authors
Xin Tang,Youfang Han,Fangfei Gou,Wei Zhao,Xin Meng,Yang Yu,Jinguo Zhang,Yuanchun Shi,Yuntao Wang,Tengxiang Zhang
### Background
视觉-语言模型（VLMs）在多种多模态任务中表现优秀，但用户需求因场景不同而异，需求可以分为快速响应、高质量输出和低能耗三类。完全依赖于部署在云端的大模型来处理所有查询常常会导致高延迟和高能耗。相比之下，部署在边缘设备上的小模型能够处理更简单的任务，具有较低的延迟和能耗。基于此，需要一种方法来充分利用大模型和小模型的优势，因此提出了ECVL-ROUTER，第一个适用于VLMs的场景感知路由框架，使能够根据用户需求动态选择合适的模型进行查询处理，从而最大化整体效益
### Innovation
ECVL-ROUTER 是第一个场景感知路由框架，它引入了一种新的路由策略和评价指标，能够根据用户需求动态为每个查询选择合适的模型，最大化的提高整体的效益。该方法还构建了一个针对路由器训练的多模态响应质量数据集，并通过广泛的实验来验证其效果。实验结果表明，该方法能够将超过80%的查询成功路由到小模型，同时损失的问题解决概率不到10%。
### Conclusion
通过ECVL-ROUTER框架，实现了一种基于用户需求的视觉-语言模型的路由策略，提高整体模型的效率和响应速度，满足了不同场景下的用户需求。
## 524. `cs.LG` - Higher-order Linear Attention [PDF](https://arxiv.org/pdf/2510.27258), [HTML](https://arxiv.org/abs/2510.27258)
### Authors
Yifan Zhang,Zhen Qin,Quanquan Gu
### Background
自回归语言模型在处理长上下文时，缩放点积注意力的成本平方是一个核心障碍。线性时间注意力和状态空间模型（SSMs）提供了可扩展的替代方案，但通常受到第一或核近似限制，这可能限制其表达能力。现有方法在实现高阶交互时通常需要较大的状态大小或时间复杂度，不利于处理长序列的高效计算。
### Innovation
引入了高阶线性注意力（HLA），这是一种因果、流式机制，通过紧凑的前置充分统计量实现高阶交互。在二阶情况下，HLA可以在不使用$n times n$矩阵的情况下，以线性时间计算每个字的输出，且保持常数大小的状态。此外，还提供了闭式流式标识、一个严格的因果掩码变体及其基于关联扫描的并行训练方案，该方案能够精确再现经典的回环路径中的激活。
### Conclusion
HLA作为一个原理上合理的构建块，结合了注意力类似的数据依赖混合与现代递归架构的效率，它提供了处理长序列时的高效可扩展替代方案。进一步提出了HLA的三阶及其他更高阶扩展。
## 525. `cs.LG` - HiF-DTA: 层次特征学习网络在药物-靶点亲和性预测中的应用 [PDF](https://arxiv.org/pdf/2510.27281), [HTML](https://arxiv.org/abs/2510.27281)
### Authors
Minghui Li,Yuanhang Wang,Peijin Guo,Wei Wan,Shengshan Hu,Shengqing Hu
### Background
药物-靶点亲和性（Drug-Target Affinity, DTA）的准确预测对于减少实验成本和加速计算药物发现过程中的初步筛查至关重要。虽然基于序列的深度学习方法可以避免依赖昂贵的三维结构，但仍未能同时建模药物和蛋白质中的全局序列语义特征和局部拓扑结构特征，同时也未能将药物表示为具有原子级、亚结构级和分子级多尺度特征的复杂结构。
### Innovation
提出了一种名为HiF-DTA的层级网络，采用双路径策略从药物和蛋白质序列中提取全局序列语义和局部拓扑特征，并通过多尺度双线性注意力模块对药物进行多尺度建模以学习结合了原子、亚结构和分子表示的融合表示。
### Conclusion
在Davis、KIBA和Metz数据集上的实验表明，HiF-DTA在药物-靶点亲和性预测方面优于最先进的基线模型，消融实验验证了全局-局部提取和多尺度融合的重要性。
## 526. `cs.LG` - ODP-Bench: Out-of-Distribution Performance Prediction Benchmark [PDF](https://arxiv.org/pdf/2510.27263), [HTML](https://arxiv.org/abs/2510.27263)
### Authors
Han Yu,Kehan Li,Dongbai Li,Yue He,Xingxuan Zhang,Peng Cui
### Background
近年来，对离分布（OOD）性能预测的关注逐渐增加。其目标是在未标记的OOD测试数据集上预测训练模型的性能，以便在风险敏感场景中更好地利用和部署现成的训练模型。尽管在该领域已经取得了一些进展，但之前的文献评价协议不一致，大多数工作只涵盖了有限的真实世界OOD数据集和分布变化类型。因此，为了提供各种算法的便捷和公平比较，本文提出了离分布性能预测基准（ODP-Bench），这是一个综合基准，包含了最常用的OOD数据集和现有的实际性能预测算法。同时，我们还提供训练好的模型作为未来研究人员的测试基准，以确保比较的一致性并避免重复模型训练的负担。此外，我们还深入分析了实验，以更好地理解它们的能力边界。
### Innovation
提出了离分布性能预测基准（ODP-Bench），这个基准包括最常用的OOD数据集和现有的实际性能预测算法，旨在为各种算法提供便捷和公平的比较。我们还提供了训练好的模型作为未来研究人员的测试基准，以确保比较的一致性并避免重复模型训练的负担，同时深入分析实验以更好地理解算法的能力边界。
### Conclusion
ODP-Bench提供了一个综合基准，确保了比较的一致性和节省了重复训练模型的时间，同时通过深入实验分析了算法的能力边界，为未来的研究提供了重要的参考。
## 527. `cs.LG` - LLM们能在工作中帮助你吗？一个评估LLM代理在企业环境中的沙盒 [PDF](https://arxiv.org/pdf/2510.27287), [HTML](https://arxiv.org/abs/2510.27287)
### Authors
Harsh Vishwakarma,Ankush Agarwal,Ojas Patil,Chaitanya Devaguptapu,Mahesh Chandran
### Background
企业系统对企业员工和客户提高生产效率和决策至关重要。将基于LLM的系统集成到企业系统中可以实现智能自动化、个性化体验和高效的信息检索，从而推动运营效率和战略增长。然而，这类系统的开发和评估面临着复杂的企业环境所带来的挑战，因为数据分散在多个来源中，并受到复杂的访问控制约束。因此，需要一种模拟企业环境的基准，以评估和改进专门针对企业环境的AI系统的效果。现有的研究表明，最先进的LLM代理在任务完成方面只能达到41.8%的完成率，这显示了在企业环境中改进AI系统的重要机会。
### Innovation
本文提出了EnterpriseBench，这是一个全面的基准测试，用于模拟企业环境，涵盖了500项来自软件工程、人力资源、财务和行政等多个领域的任务。该基准的独特之处在于它可以捕捉到企业特性的关键方面，如数据源的碎片化、访问控制层级和跨职能的工作流程。此外，该研究还提供了一个新颖的数据生成管道，可以从前组织元数据中生成内部一致的商业任务。实验结果表明，最先进的LLM代理在任务完成方面的表现仅达到41.8%，这凸显了在企业环境中改进AI系统的潜在机会。
### Conclusion
本研究通过EnterpriseBench基准测试和数据生成管道，提供了一种评估LLM代理在真实企业环境中的有效性的方法。实验结果表明，当前最先进的LLM代理在企业环境中的任务完成率仍较低，需要进一步改进，以便更好地满足企业的实际需求。
## 528. `cs.LG` - 基于PPG的心率估计改进的时空心血管动力学 [PDF](https://arxiv.org/pdf/2510.27297), [HTML](https://arxiv.org/abs/2510.27297)
### Authors
Berken Utku Demirel,Christian Holz
### Background
人类的心率波动具有内在的复杂性和非线性特征，可以最好地通过数学混沌来描述。这些特征在日常生活中的心血管健康监测中带来了挑战。尽管传统方法可以应对这些复杂性，但仍存在不足之处。该研究关注非线性混沌行为并通过互信息进行研究，并提出了一种新颖的方法来增强在实际生活条件下的心率估计。这种方法不仅从数学角度解释和处理了非线性的时间复杂性，而且与现有的深度学习解决方案结合使用时，还能提高性能。为了验证该方法的有效性，研究者在四个不同场景的真实数据集上进行了验证，并与现有的算法进行了彻底的比较试验。研究结果表明，与传统方法和现有的机器学习技术相比，该方法在心率估计方面提高了20%到40%，同时减少了对多种传感模态的依赖，并消除了后处理步骤的需求。
### Innovation
该研究通过引入互信息来研究心率的非线性混沌行为，并提出了新颖的方法来增强实际生活条件下的心率估计。该方法不仅从数学角度解释并处理了非线性的时间复杂性，还可以与现有的深度学习解决方案结合使用，提高性能。实验结果表明，该方法在心率估计方面取得了显著改进，提高了20%到40%，并减少了对多种传感模态的依赖和后处理步骤的需要。
### Conclusion
该研究通过引入互信息和一种新颖方法，在实际生活中提高了基于PPG的心率估计的准确性，并且通过实验验证显示出显著的性能提升，同时简化了技术实现，提升了用户体验。
## 529. `cs.LG` - FedMuon: 使用矩阵正交化加速联邦学习 [PDF](https://arxiv.org/pdf/2510.27403), [HTML](https://arxiv.org/abs/2510.27403)
### Authors
Junkang Liu,Fanhua Shang,Junchao Zhou,Hongying Liu,Yuanyuan Liu,Jin Liu
### Background
联邦学习的核心瓶颈在于通信轮次。现有方法主要采用元素级的本地优化器（如Adam和SGD），忽视了权重矩阵的几何结构，在本地更新时导致路径依赖方向的放大，从而影响条件数并导致收敛缓慢。
### Innovation
提出了一种名为FedMuon的剪枝优化方法，结合了动量聚合和局部-全局方向对齐的技术，以解决非IID分布下矩阵正交化带来的客户端漂移问题，并在实验中证明了其在不同模型上的有效性，显著减少了通信轮次并提高了测试精度。
### Conclusion
理论上证明，FedMuon在没有异质性假设的情况下实现了线性加速收敛速率，其中S为每轮次参与客户端的数量，K为本地迭代次数，R为总通信轮次数。
## 530. `cs.LG` - 不可归因性：从检索与语义相似性计算新颖性 [PDF](https://arxiv.org/pdf/2510.27313), [HTML](https://arxiv.org/abs/2510.27313)
### Authors
Philipp Davydov,Ameya Prabhu,Matthias Bethge,Elisa Nguyen,Seong Joon Oh
### Background
理解语言模型输出与预训练语料库的关系是研究模型行为的关键。现有的大多数训练数据归因（TDA）方法试图确定哪些训练示例导致了给定的输出，通常使用排除法测试。该研究反转了这一问题，关注哪些输出无法归因于任何预训练示例。通过引入不可归因性作为语义新颖性的一个操作性衡量标准，研究找到了一种评估方法，即如果预训练语料库中没有相似的语境，输出被认为是新颖的。该研究使用了一个简单的两阶段检索管道来近似这一概念。
### Innovation
该研究提出了不可归因性作为计算新颖性的方法，并通过引入一个简单但高效的两阶段检索管道（利用轻量级GIST嵌入和ColBERTv2重新排名）来实现。这种方法能够评估哪些模型输出无法归因于预训练数据，并揭示了一些语境下模型新颖性被系统性地促进或抑制的现象。研究还发现指令调优不仅改变风格，还增加了新颖性。
### Conclusion
重新将新颖性评估框架围绕不可归因性，能够对大规模预训练数据进行高效分析。为了支持这一研究方法的可复制性和扩展，研究者发布了约20TB的语料库片段和索引工具，可在指定的网址下载。
## 531. `cs.LG` - 流式物联网流量概念漂移下的二元异常检测 [PDF](https://arxiv.org/pdf/2510.27304), [HTML](https://arxiv.org/abs/2510.27304)
### Authors
Rodrigo Matos Carnier,Laura Lahesoo,Kensuke Fukuda
### Background
随着物联网（IoT）网络流量的快速增长，基于机器学习（ML）的异常检测变得越来越重要。传统的批量学习模型面临高维护成本和对快速异常变化适应性差的挑战，尤其是面对概念漂移。相比之下，流式学习通过在线和增量学习方式，支持无缝更新和概念漂移检测，从而提高系统的鲁棒性。因此，本文旨在研究流式物联网流量的二元异常检测，并对比批量和流式学习方法，同时评估现有物联网流量数据集的局限性。通过模拟异构网络数据流，本文揭示了批量模型处理概念漂移的失败，并指出现有数据集由于流量异构性不足而导致的模型局限性。进一步探讨了树基机器学习算法在批量异常检测中的竞争力，并与非树基算法进行了比较，确认了树基模型的优势，并表明自适应随机森林在计算成本仅为批量版本三分之一的情况下，实现了0.990 ± 0.006的F1分数。霍夫丁自适应树达到了0.910 ± 0.007的F1分数，计算成本降低了四倍，尽管稳定性略有妥协，但仍是一个适合在线应用的选择。
### Innovation
本文提出了针对流式物联网流量的二元异常检测方法，并对比了批量和流式学习方法。通过模拟异构网络数据流，证明了树基机器学习算法（如自适应随机森林）相较于非树基算法在处理异构数据和减少计算成本方面具有明显优势。特别是自适应随机森林和霍夫丁自适应树在保持较高检测性能的同时，大幅降低了计算成本，展示了解决物联网中概念漂移问题的新策略。
### Conclusion
研究表明，自适应随机森林和霍夫丁自适应树在处理流式物联网流量中的概念漂移方面比批量模型更有效，能够在显著降低计算成本的同时获得较高的检测性能。未来工作可以进一步提高模型的稳定性，并探索更多适用于物联网环境的自适应学习算法。
## 532. `cs.LG` - MedM2T：一种用于电子健康记录和心电图数据的时间意识多模态框架 [PDF](https://arxiv.org/pdf/2510.27321), [HTML](https://arxiv.org/abs/2510.27321)
### Authors
Yu-Chen Kuo,Yi-Ju Tseng
### Background
医疗数据的固有多模态性和异质时间结构对建模提出了重大挑战。现有的模型难以处理这些复杂性，特别是在处理稀疏和不规则的时间序列以及不同模态之间的细微粒度差异方面。MedM2T框架旨在克服这些问题，提供一种时间意识的多模态建模方法，特别适用于电子健康记录（EHR）和心电图（ECG）数据。
### Innovation
MedM2T引入了具有以下创新点的新框架：(i) 稀疏时间序列编码器，灵活处理稀疏和不规则的时间序列；(ii) 分层时间意识融合，捕获来自多个密集时间序列（如ECGs）的微观和宏观时间模式；(iii) 双模态注意力机制，提取跨模态交互，可用于任意数量的模态。MedM2T通过使用模态特定预训练编码器并进行特征对齐解决了模态间的细微粒度差距。
### Conclusion
MedM2T在MIMIC-IV和MIMIC-IV-ECG数据集上对三种任务（90天心血管疾病预测、住院死亡率预测和ICU住院时间回归）进行了评估，并取得了优于现有模型的性能，展示了其在临床预测中的稳健性和广泛适用性。研究结果为MedM2T提供了实际应用的验证和支持，使其成为临床预测中的有力工具。
## 533. `cs.LG` - 利用贝叶斯数据调度器实现大型语言模型有害微调的自适应防御 [PDF](https://arxiv.org/pdf/2510.27172), [HTML](https://arxiv.org/abs/2510.27172)
### Authors
Zixuan Hu,Li Shen,Zhenyi Wang,Yongxian Wei,Dacheng Tao
### Background
有害微调对大型语言模型的服务安全构成了严重威胁。现有防御策略通过预先构建鲁棒性进行攻击模拟，但存在以下局限性：(i) 无法将攻击模拟扩展到超出界定的威胁模型，因为预测未知攻击本身具有困难性，(ii) 缺乏适应不同攻击设置的能力，因为模拟未能捕捉到它们的多样性和复杂性。
### Innovation
我们提出了贝叶斯数据调度器（BDS），这是一种无需进行攻击模拟的自适应微调阶段防御策略。BDS 将有害微调防御建模为贝叶斯推断问题，学习每个数据点安全属性的后验分布，受条件于微调和对齐数据集。通过使用贝叶斯推断的后验性质，后验条件于微调数据集，BDS 能够针对特定数据集调整其防御，从而实现自适应防御。此外，我们引入了基于公制贝叶斯学习的神经调度器，使其能够高效地在新数据上进行转移，无需重新训练。这些研究结果表明本方法具有业界最佳性能。
### Conclusion
我们的方法在多种攻击和防御设置下展示了行业领先的表现。
## 534. `cs.LG` - Atlas-Alignment: 实现语言模型间可解释性的转移 [PDF](https://arxiv.org/pdf/2510.27413), [HTML](https://arxiv.org/abs/2510.27413)
### Authors
Bruno Puri,Jim Berend,Sebastian Lapuschkin,Wojciech Samek
### Background
构建安全、可靠和可控的语言模型需要高可解释性，但现有的可解释性流程仍然成本高昂且难以扩展。解释一个新模型通常需要为特定模型训练稀疏自编码器，手动或半自动化标记自编码器组件，并进行后续验证。
### Innovation
我们提出了一种名为Atlas-Alignment的框架，通过将未知的潜在空间与概念图谱（包含标记的人类可解释的潜在空间）对齐，仅使用共享输入和轻量级的表征对齐技术，来在不同语言模型之间转移可解释性。这种方法使以前透明度不足的模型具备了两个关键能力：(1) 语义特征搜索和检索，(2) 沿着人类可解释的概念图谱进行定向生成。
### Conclusion
实验证明，简单的表征对齐方法能够在无需标记概念数据的情况下实现稳健的语义检索和可定向生成。因此，Atlas-Alignment 通过投资一个高质量的概念图谱，可以使许多新模型在极低的成本下具备透明性和可控性。
## 535. `cs.LG` - Thought Branches: Interpreting LLM Reasoning Requires Resampling [PDF](https://arxiv.org/pdf/2510.27484), [HTML](https://arxiv.org/abs/2510.27484)
### Authors
Uzay Macar,Paul C. Bogdan,Senthooran Rajamanoharan,Neel Nanda
### Background
大多数研究因果推理模型的文献仅关注单一的链式思考（CoT），但实际上，这些模型在多种可能的CoT中形成了不同的分布。这种单一样本的分析方法不足以全面理解因果影响及其背后的计算机制。
### Innovation
论文提出了通过重采样方法研究模型决策的新方法，以探究单一CoT是否真正导致了行动，人工编辑CoT是否能有效引导推理，移除推理步骤的影响以及未被明确提及的提示如何微妙地影响CoT。这些研究提供了对CoT分布进行可靠因果分析、清晰解释模型推理及实现原则性CoT干预的新途径。
### Conclusion
通过重采样方法研究CoT的分布可以进行可靠的因果分析，提供更清晰的模型推理叙述，并实现基于模型的因果干预。这种方法在
## 536. `cs.LG` - 光谱神经图稀疏化 [PDF](https://arxiv.org/pdf/2510.27474), [HTML](https://arxiv.org/abs/2510.27474)
### Authors
Angelica Liguori,Ettore Ritacco,Pietro Sabatino,Annalisa Socievole
### Background
图在社会网络、分子化学和神经科学等领域被广泛用作复杂系统的模型。虽然图神经网络（特别地是图卷积网络），已经成为图学习的标准工具，但它们仍然受限于对固定结构的依赖和过拟合的脆弱性。
### Innovation
提出了光谱保存网络（Spectral Preservation Network），这是一种新的图表示学习框架，通过生成具有代表性的子图来降低图的复杂性，以支持如社团检测、影响传播和信息扩散等任务并减少计算成本。该框架包含两个关键组件：联合图演化层和光谱一致性损失，前者允许结构和属性在层间自适应演化，克服静态邻域聚合的局限性，后者通过确保图的光谱属性和节点特征向量的一致性，对这些变化进行正则化约束。
### Conclusion
通过分析标准指标评估光谱保存网络进行节点级稀疏化的效果，并以最先进的方法为基准进行对比实验。实验结果表明我们的方法具有显着的优越性能和明显的优势。
## 537. `cs.LG` - 推理模型有时会输出不透明的推理链条 [PDF](https://arxiv.org/pdf/2510.27338), [HTML](https://arxiv.org/abs/2510.27338)
### Authors
Arun Jose
### Background
基于结果的强化学习（RL）训练的语言模型通过推理链条（CoT）进行推理时，其表现表现出色。监测这些模型的推理链条可以帮助我们了解其意图并检测潜在的恶意行为。然而，要实现这一点，要求推理链条必须是可读的和忠实的。本文研究了14种推理模型的可读性，发现RL经常使推理变得对人类和AI监控来说都是难以理解的，大多数模型（除Claude外）在生成可读的答案的同时，推理链条却是不可读的，这表明推理链条的透明度与模型性能之间的关系可能更为复杂，并且，随着问题难度的增加，推理链条的可读性会降低。
### Innovation
本文揭示了尽管模型能够给出正确的答案，但在必要时只使用可读推理部分会导致准确率下降53%，表明推理链条的透明度与模型性能之间没有直接的正相关关系。这可能暗示，结果导向的强化学习自然会产生越来越多难以理解的推理过程，这对于监控手段的有效性产生潜在的负面影响。研究还探讨了可能导致这些结果的一些假设，如隐写术、训练残迹和退化的代币。这些结果表明，在明确优化可读性的情况下，基于结果的RL反映出了出现更不透明推理过程的倾向，对于监控方法的有效性提出了挑战。
### Conclusion
研究发现，结果导向的强化学习自然会产生更加难以理解的推理过程，这可能会影响对于模型的监控策略的有效性。要改进这一点，未来的模型训练需要将对推理链条的透明性的优化作为重点考虑的内容之一。
## 538. `cs.LG` - InertialAR：基于惯性帧的自回归3D分子生成 [PDF](https://arxiv.org/pdf/2510.27497), [HTML](https://arxiv.org/abs/2510.27497)
### Authors
Haorui Li,Weitao Du,Yuqiang Li,Hongyu Guo,Shengchao Liu
### Background
基于Transformer的自回归模型在诸如文本和图像等模态中得到了统一的应用，但在3D分子生成方面还未得到充分发展。这一空白源于两个基本挑战：一是将分子转换为1D的、SE(3)变换和原子索引排列不变的标准序列的标记化方法；二是设计能够建模以离散原子类型与连续三维坐标耦合为基础的原子标记化架构。
### Innovation
InertialAR 创新地采用了惯性帧标记方法来确保3D分子生成的不变性和建模能量旋转和原子排列信息的几何位置编码（GeoRoPE）机制。它还采用分层自回归框架，首先预测原子类型，然后通过扩散损失预测其三维坐标。
### Conclusion
InertialAR 在轻气球、几何药物和B3LYP上的7个评估指标中达到了最佳性能，并在可控的化学功能生成中显著超过了强基线，在5个指标中达到了最佳效果。
## 539. `cs.LG` - 将单纯形映射到欧几里得空间的映射方法以实现类别流匹配 [PDF](https://arxiv.org/pdf/2510.27480), [HTML](https://arxiv.org/abs/2510.27480)
### Authors
Bernardo Williams,Victor M. Yeom-Song,Marcelo Hartmann,Arto Klami
### Background
当前的方法大多是在单纯形上使用黎曼几何或自定义噪声过程进行操作，这在密度建模时可能会有一定的局限性。本研究旨在提出一种方法，通过将开放单纯形映射到欧几里得空间，利用Aitchison几何来定义映射，支持通过Dirichlet插值将离散观测转化为连续观测，进而实现了在欧几里得空间中的密度建模，并能精确恢复原始的离散分布。
### Innovation
本研究提出了一种将单纯形映射到欧几里得空间的方法，通过使用光滑双射和Aitchison几何定义映射，利用Dirichlet插值将离散数据转化为连续数据。这种方法能够在保持Aitchison几何的基础上在欧几里得空间中实现密度建模，同时保持能精确恢复原始离散分布的能力，相较于传统的黎曼几何或自定义噪声过程的方法，具有竞争力的表现。
### Conclusion
通过本文提出的方法，在合成和真实世界数据集上均能实现与传统方法相当的性能，并且能够更加自然和高效地处理类别数据。这种方法为类别数据的建模和分析提供了一种新的视角和方法。
## 540. `cs.LG` - FedAdamW: 一种具有通信效率和收敛及泛化保证的联邦大规模模型优化器 [PDF](https://arxiv.org/pdf/2510.27486), [HTML](https://arxiv.org/abs/2510.27486)
### Authors
Junkang Liu,Fanhua Shang,Kewen Zhu,Hongying Liu,Yuanyuan Liu,Jin Liu
### Background
AdamW已成为训练大规模模型最有效的方法之一。尽管如此，在联邦学习（FL）场景中直接使用AdamW仍面临重大挑战，包括数据异质性导致的二阶矩估计$boldsymbol{v}$的高方差、局部过拟合引起的客户端漂移以及每次迭代重置动量估计导致的收敛速度变慢。该研究旨在解决这些问题。
### Innovation
研究提出了第一个面向联邦学习的AdamW算法，称为FedAdamW。FedAdamW采用了局部纠正机制和解耦的权重衰减来减少局部过拟合，并通过有效聚合二阶矩估计的均值来降低其方差并重新初始化它们。此外，研究还证明，FedAdamW在无需异质性假设的情况下实现了线性速度的收敛率，即$theta$。使用PAC-Bayesian泛化分析进一步解释了解耦权重衰减在局部训练中的有效性。实验结果表明，FedAdamW显著减少了通信轮数并提高了测试准确性。
### Conclusion
该研究通过证明FedAdamW在无需异质性假设的情况下实现了线性收敛速度并减少了通信轮次，展示了其在语言和视觉转换器模型上的有效性。
## 541. `cs.LG` - 利用通用时间序列基础模型进行EEG分类 [PDF](https://arxiv.org/pdf/2510.27522), [HTML](https://arxiv.org/abs/2510.27522)
### Authors
Théo Gnassounou,Yessin Moakher,Shifeng Xie,Vasilii Feofanov,Ievgen Redko
### Background
时间序列模型作为强大的通用基础架构正在逐渐崭露头角，但它们在生物医学信号如脑电图（EEG）特定领域的潜力尚未得到充分探索。
### Innovation
研究评估了一种近期提出的时间序列分类基础模型的适用性，应用于不同EEG任务，如运动想象分类和睡眠阶段预测。研究测试了两种预训练方案：一种是使用多领域的异质真实世界时间序列数据进行预训练，另一种是使用完全合成数据进行预训练。研究发现，这两种方法均表现出强大的性能，一致地优于广泛使用的卷积基线EEGNet和最新的EEG特定基础模型CBraMod。
### Conclusion
这些结果表明，即使预训练数据来自非神经领域或基于合成信号，通用时间序列基础模型也可以有效迁移到EEG。研究结果突显了利用跨域预训练模型进行脑信号分析的潜力，表明EEG可以受益于更广泛时间序列文献的发展。
## 542. `cs.LG` - 通过忠实度和详述度衡量链式思维监控能力 [PDF](https://arxiv.org/pdf/2510.27378), [HTML](https://arxiv.org/abs/2510.27378)
### Authors
Austin Meek,Eitan Sprejer,Iván Arcuschin,Austin J. Brockmeier,Steven Basart
### Background
链式思维（Chain-of-Thought，CoT）输出使我们能够阅读模型的逐步推理过程。任何长期的、串行的推理过程都必须通过这个文字痕迹，因此CoT的质量直接反映了模型的思维过程。透明的CoT可以帮助我们发现不安全或不对齐的行为（即监控能力），前提是CoT能够真实地反映其内部推理过程（即忠实度）。尽管评估忠实度很难，但研究人员通常关注在添加输入提示后模型改变答案的情况下评估CoT。虽然这种代理能够发现部分不忠实的情况，但它在模型维持原始答案时会丢失信息，并且不研究与提示无关的推理方面。为了扩展这些结果以更全面地评估监控能力，作者引入了详述度这个概念，即CoT是否列出了了解决任务所需的所有因素。作者将忠实度和详述度结合成单一的监控能力得分，该得分展示了CoT如何作为模型的外部‘工作记忆’表现，这是许多基于CoT监控的安全方案所依赖的特性。作者评估了指令调整和推理模型在BBH、GPQA和MMLU上的表现。结果显示，即便模型看起来是忠实的，但如果省略了关键因素，它们也可能难以监控，而且监控能力在不同模型家族之间存在显著差异。作者还发布了使用Inspect库的评估代码，以支持未来工作的可重复性研究。
### Innovation
研究引入了详述度的概念，即将CoT是否列出了解决任务所需的所有因素作为评估模型监控能力的一个新维度。将忠实度和详述度结合成单一的监控能力得分，以评估CoT如何作为模型的外部‘工作记忆’表现。提供了一种使用Inspect库来进行评估的代码，使后续研究可重复且支持透明化过程。创新点在于对模型的完整监测不仅要考虑忠实度，还要考虑详述度，从而更全面地评估模型的监控能力。
### Conclusion
研究结果表明，即便模型看起来忠实，但如果省略了解决任务所需的关键因素，它们也可能难以监控。不同类型的模型在监控能力方面存在着显著差异。为评估CoT的监控能力，作者提出了一个结合了忠实度和详述度的新得分体系，并发布了支持可重复研究的评估代码。
## 543. `cs.LG` - DP-FedPGN: 使用惩罚梯度范数来为差异隐私联邦学习寻找全局平坦极小值 [PDF](https://arxiv.org/pdf/2510.27504), [HTML](https://arxiv.org/abs/2510.27504)
### Authors
Junkang Liu,Yuxuan Tian,Fanhua Shang,Yuanyuan Liu,Hongying Liu,Junchao Zhou,Daorui Ding
### Background
在联邦学习（FL）中，为了防止推理攻击并减少敏感信息的泄露，通常使用客户级差异隐私联邦学习（CL-DPFL）。然而，现有的CL-DPFL方法通常会导致损失更尖锐的景观，从而在差异隐私保护后降低模型的泛化能力。现有方法使用Sharpness Aware Minimization（SAM）来寻找局部平坦极小值来缓解此问题，但这种方法可能无法反映全局平坦性。因此，本研究提出了一种新的CL-DPFL算法，DP-FedPGN，通过引入全局梯度范数惩罚到局部损失中寻找全局平坦极小值，从而寻找全局平坦的最小值，并进一步减少梯度裁剪的误差。从理论上分析了DP-FedPGN如何缓解由DP引起的性能下降，并展示了其对数据异质性的影响，实现了快速收敛。
### Innovation
本文提出了一种新的CL-DPFL算法—DP-FedPGN，该算法通过将全局梯度范数惩罚引入局部损失，来寻找全局平坦的极小值。这不仅找到了更平坦的全局极小值，还减少了局部更新的范数，进一步降低了梯度裁剪误差。此外，本文还使用Rényi DP提供严格的隐私保障，并对局部更新进行敏感性分析。
### Conclusion
本文采用DP-FedPGN算法在视觉和自然语言处理等六个任务中均实现了对现有先进算法的显著改进，实验证明该算法的有效性和优越性，且算法代码已开源。
## 544. `cs.LG` - GPU友好的学习稀疏近似逆预条件子方法应用于共轭梯度求解器 [PDF](https://arxiv.org/pdf/2510.27517), [HTML](https://arxiv.org/abs/2510.27517)
### Authors
Zherui Yang,Zhehao Li,Kangbo Lyu,Yixuan Li,Tao Du,Ligang Liu
### Background
共轭梯度求解器（CG）适用于求解对称正定线性系统 Ax=b，有效的预条件器对于加快收敛速度至关重要。传统预条件器依赖于预设算法提供严格的理论保证，但其限制了利用数据优化的能力。现有的基于学习的方法常常利用图神经网络（GNNs）来提升性能并加速构建过程。然而，这些方法依赖于不完全分解，在实际中阻碍了 GPU 并行化，并引入了难以建模的长期依赖关系。为解决这些问题，作者提出了一种基于学习的方法，生成 GPU 友好的预条件子，特别是利用 GNNs 构建稀疏近似逆（SPAI）预条件子，避免了三角解算，并需要在每个共轭梯度步骤中仅进行两次矩阵-向量乘法。
### Innovation
该方法利用 GNNs 构建稀疏近似逆预条件子（SPAI），避免了三角解算，仅需每次共轭梯度步骤中进行两次矩阵-向量乘法。此外，该方法引入了一种基于统计的无标度损失函数，该函数符合共轭梯度收敛速率依赖于条件数而不是 A 的绝对尺度的特性，从而提高了学习预条件子的性能。
### Conclusion
在三个 PDE 导出的数据集和一个合成数据集上的评估表明，该方法在 GPU 上比标准预条件子（对角线、IC 和传统 SP不在研究中）和先前的基于学习的预条件子具有更好的性能。我们减少了 GPU 上的求解时间 40%-53%（68%-113% 更快），同时具备更好的条件数和更强的泛化性能。
## 545. `cs.LG` - 不平衡分类透过伪相关性视角 [PDF](https://arxiv.org/pdf/2510.27650), [HTML](https://arxiv.org/abs/2510.27650)
### Authors
Jakob Hackstein,Sidney Bender
### Background
不均衡数据集构成了机器学习中的一个根本性挑战，常常导致不可靠的分类性能。以往的方法主要集中在数据或损失重权方案上，但本文认为不平衡是一种数据条件，这种条件会因为在少数类上的欠指定而导致Clever Hans（CH）效应被放大。
### Innovation
本文提出了一种基于反事实解释的方法，利用可解释人工智能联合识别和消除不平衡情况下的CH效应。该方法在三个数据集上实现了竞争力的分类性能，并展示了不平衡条件下CH效应的出现，这在现有方法中尚未得到重点研究。
### Conclusion
该方法不仅提升了分类性能，还在理论上丰富了对CH效应在不平衡数据集中的理解，为未来的研究提供了新的视角。
## 546. `cs.LG` - TetraJet-v2: NVFP4 训练法在大型语言模型中实现准确训练，同时抑制振荡和控制异常值 [PDF](https://arxiv.org/pdf/2510.27527), [HTML](https://arxiv.org/abs/2510.27527)
### Authors
Yuxiang Chen,Xiaoming Xu,Pengle Zhang,Michael Beyer,Martin Rapp,Jun Zhu,Jianfei Chen
### Background
大型语言模型（LLMs）的训练费用高昂，促使研究人员转向低精度全量化训练（FQT）。尽管新型4位格式如NVFP4提供了显著的效率提升，但在如此低精度下实现接近无损失的训练仍然颇具挑战。文章探讨了低精度LLMs训练中的两个关键问题：权重振荡和异常值，并提出相应的解决方案。
### Innovation
引入了TetraJet-v2，这是首个将NVFP4技术应用于激活、权重和梯度的端到端4位FQT方法。文中具体提出了以下创新点：1）基于NVFP4线性层的无偏双块量化方法，2）OsciReset算法，旨在抑制权重振荡，3）OutControl算法，确保保留异常值准确性。
### Conclusion
TetraJet-v2 在预训练LLMs方面表现出色，覆盖了从370M到200B不等的不同模型大小，与全精度训练相比，性能差距平均缩小了51.3%。
## 547. `cs.LG` - 结构健康监测中的主动迁移学习 [PDF](https://arxiv.org/pdf/2510.27525), [HTML](https://arxiv.org/abs/2510.27525)
### Authors
J. Poole,N. Dervilis,K. Worden,P. Gardner,V. Giglioni,R.S. Mills,A.J. Hughes
### Background
结构健康监测（SHM）系统的训练数据通常昂贵且难以获得，尤其是带有标签的数据。群体结构健康监测（PBSHM）通过利用多个结构的数据来缓解这个问题，但不同结构的数据遵循不同的分布，导致通过传统机器学习方法训练的模型泛化误差较大。为解决此问题，迁移学习中的域适应（DA）技术可用于对齐数据分布，但多数方法仅考虑了无监督的域适应方法，未考虑如何将这些技术整合到在线框架中，实时更新标签数据。已有研究中尚未提出结合主动学习提升无监督域适应效果的方法。
### Innovation
本文提出了一个贝叶斯域适应框架，能够在少量标签目标数据下改进无监督的域适应映射，并将此模型集成到主动采样策略中，指引检查以选择最具信息量的观测数据进行标签。该方法在实验桥的群体中进行评估，结果表明结合迁移学习和主动学习可以提高在标签稀缺场景下学习分类模型的数据效率。这为结构的信息化运维提供了新思路，暗示可减少结构运营生命周期中的检查次数，从而降低运营成本。
### Conclusion
结合迁移学习和主动学习可以提高在标签稀缺场景下结构健康监测中分类模型的学习效率。这种方法为未来结构健康监测领域提供了优化方案，尤其是在数据获取困难的情况下，如有效减少目检频次，降低运维成本。
## 548. `cs.LG` - 泛预测：任意下游任务和损失的最佳预测 [PDF](https://arxiv.org/pdf/2510.27638), [HTML](https://arxiv.org/abs/2510.27638)
### Authors
Sivaraman Balakrishnan,Nika Haghtalab,Daniel Hsu,Brian Lee,Eric Zhao
### Background
传统监督学习的目标是训练模型以最小化固定损失函数，并处理固定的任务。然而，新兴的框架将模型训练视为从数据中提取足够的信息，以便模型能够用于多种下游任务的许多损失函数的最小化。这一新框架被定义为泛预测，并且研究其统计复杂性。泛预测扩展了泛预测，并位于跨组学习之前，后者分别关注预测可以在许多下游损失上泛化或者在许多下游任务上泛化，但不兼得。
### Innovation
文章设计了用于学习确定性泛预测和随机化泛预测的算法，分别需要 $tilde{O}(1/?varepsilon^3)$ 和 $tilde{O}(1/?varepsilon^2)$ 的样本。结果显示，在温和的假设下，同时在无穷多个任务上优化无穷多个损失可以像在一个任务中优化一个损失一样统计上容易。同时，还细化了确定性泛预测的最佳已知样本复杂性保证，并匹配了其他已知的样本复杂性保证。关键的技术成分是一个几乎无损地将泛预测转换为一种统计上高效的校准概念——步进校准的减少方法。
### Conclusion
研究表明，在某些条件下，同时最小化无限多个下游任务的无限多个损失可以像最小化一个损失一样简单。通过改进和匹配先前的样本复杂性保证，强调了泛预测在统计效率上的优势，并通过步进校准概念展示了这个方法的有效性。
## 549. `cs.LG` - AstuteRAG-FQA：专为财务问答中专属数据挑战设计的任务感知检索增强生成框架 [PDF](https://arxiv.org/pdf/2510.27537), [HTML](https://arxiv.org/abs/2510.27537)
### Authors
Mohammad Zahangir Alam,Khandoker Ashik Uz Zaman,Mahdi H. Miraz
### Background
检索增强生成（RAG）在知识密集型任务中表现出显著的潜力，通过提高领域特定性、增强时间相关性和减少幻觉。然而，将其应用于金融领域会面临重要挑战，包括受限的专属数据集访问、检索精度有限、监管约束和敏感数据解释的挑战。
### Innovation
我们介绍了AstuteRAG-FQA，一个专为财务问答（FQA）优化的适应性RAG框架，利用任务感知提示工程来解决这些挑战。该框架使用混合检索策略，结合开源和专属金融数据，同时保持严格的安全协议和合规性。动态提示框架能够根据查询复杂性实时调整，提高精确度和上下文相关性。我们提出了四级任务分类：明确事实、隐含事实、可解释的推理性质和隐含的因果推理性质，并为每类确定关键挑战、数据集和检索与生成过程中的优化技术。框架整合了多层次的安全机制，包括差分隐私、数据匿名化和基于角色的访问控制，以保护敏感的财务信息。此外，AstuteRAG-FQA通过自动监管验证系统实施实时合规监控，验证响应是否符合行业标准和法律义务。我们评估了三种数据集成技术：上下文嵌入、小型模型增强和目标微调，并分析了它们在不同金融环境下的效率和可行性。
### Conclusion
我们通过一个多维度的方法系统地解决了财务查询中的各项挑战，提出了一种专为财务领域设计的RAG框架，保证了数据的合规性和安全性，并通过实证分析验证了其在不同金融场景下的有效性和可行性。
## 550. `cs.LG` - 基于W-PCA的无梯度代理方法：用于轻量级语言模型高效搜索 [PDF](https://arxiv.org/pdf/2504.15983), [HTML](https://arxiv.org/abs/2504.15983)
### Authors
Shang Wang
### Background
由于对高效自然语言处理（NLP）系统的需求不断增加，推动了轻量级语言模型的发展。以往的研究主要集中在手动设计或基于神经架构搜索（NAS）的方法上。最近，提出了零样本NAS方法，可以在无需训练的情况下评估语言模型。但现有零样本NAS方法常面临评价指标偏差和计算效率低下的问题。本文针对轻量级语言模型，提出了一种新的基于W-PCA的无梯度评价代理方法。
### Innovation
本文提出了W-PCA，一种针对轻量级语言模型的零样本NAS方法。该方法利用参数量和FFN层中累积贡献超过阈值的主成分数量两个评价代理，并通过消除梯度计算的需要来优化评价时间，从而提高轻量级语言模型设计和评价的效率。
### Conclusion
在GLUE和SQuAD数据集上的实验结果表明，本文方法能显著缩短训练时间，相对于一-shot NAS方法，在测试阶段得分更高；在从FlexiBERT搜索空间采样的数据集上进行的排名评价表明，本文方法在排名相关性和求解时间上优于其他需要梯度计算的零样本NAS方法。
## 551. `cs.LG` - 开放代理系统中多代理强化学习中的信用分配挑战 [PDF](https://arxiv.org/pdf/2510.27659), [HTML](https://arxiv.org/abs/2510.27659)
### Authors
Alireza Saleh Abadi,Leen-Kiat Soh
### Background
在快速演进的多智能体强化学习（MARL）领域，理解开放系统的动态特性至关重要。开放性包括代理动态进出系统、任务的新兴更替以及代理能力与行为的演变等三个方面。信用分配问题（CAP）涉及确定个体智能体对整体系统性能的贡献，开放环境使得这一任务复杂化。传统信用分配方法通常基于静止的智能体群体、固定的任务定义和稳定类型等假设，难以应对开放系统的新挑战。已有研究和报告中指出，智能体动态变化、任务更替等会打破现有CAP方法依赖的环境稳态和团体组成固定的前提条件。
### Innovation
本文通过概念分析引入了更多关于开放性的新子类别，详细阐述了代理轮换或任务取消等事件如何破坏现有CAP方法的前提假设，并通过开放环境中的代表性时间和结构算法进行了实证研究。实证研究表明开放性直接导致了信用误分配，通过不稳定的损失函数和显著的性能退化表现出来。
### Conclusion
开放性对信用分配问题的复杂性造成了显著影响。传统信用分配方法在开放系统中可能不再适用，需要开发新的方法以适应动态变化的环境。通过引入新的子类别和实证研究，本文提供了一个有价值的研究视角，为进一步研究开放性对信用分配的影响提供了参考。
## 552. `cs.LG` - 基于信息论的贪婪逐层训练方法在交通标志识别中的应用 [PDF](https://arxiv.org/pdf/2510.27651), [HTML](https://arxiv.org/abs/2510.27651)
### Authors
Shuyan Lyu,Zhanzimo Wu,Junliang Du
### Background
现代深度神经网络（DNNs）通常以监督端到端的方式通过全局交叉熵损失进行训练，这需要神经元存储其输出权重，并交替进行前向传播计算和自顶向下的反向传播学习，后者在生物上是不可实现的。另一种贪婪逐层训练方法通过避免计算中间梯度和存储中间输出，减少了内存使用，并有助于缓解梯度消失或爆炸的问题。然而，大多数现有的逐层训练方法仅在小型简单数据集上进行了评估。
### Innovation
本文通过信息论视角系统地分析了使用随机梯度下降（SGD）训练的流行卷积神经网络（CNNs）的训练动力学。研究发现，网络从下到上逐层收敛，并且信息流动遵循马尔可夫信息瓶颈原则。基于这些观察，提出了基于最近开发的确定性信息瓶颈（DIB）和矩阵形式的Rényi’s α阶熵泛函的新逐层训练方法。每个层与直接连接到输出层的辅助分类器共同训练，使得能够学习最小充分的任务相关表示。该方法在CIFAR-10和CIFAR-100上的实验验证了其有效性，并进一步展示了其在交通标志识别等实际任务中的适用性。
### Conclusion
本文提出的方法不仅优于现有的逐层训练基准，还实现了与随机梯度下降（SGD）相当的性能。
## 553. `cs.LG` - 基于ResNet架构的辅助评价指标神经架构搜索方法 [PDF](https://arxiv.org/pdf/2505.01313), [HTML](https://arxiv.org/abs/2505.01313)
### Authors
Shang Wang,Huanrong Tang,Jianquan Ouyang
### Background
该论文提出了一种使用ResNet作为框架的神经架构搜索空间，搜索目标包括卷积参数、池化、全连接层以及残差网络的连接性。除了识别精度外，该论文还使用验证集上的损失值作为优化的次要目标。研究结果表明，该论文提出的空间与优化方法可以在MNIST、Fashion-MNIST和CIFAR100数据集上找到具有竞争力的网络架构。
### Innovation
该论文的主要创新在于提出了一种使用ResNet架构的神经架构搜索方法，同时利用验证集上的损失值作为优化的次要目标，以提高网络架构的竞争力。这种方法可以在多个流行的图像数据集上找到表现良好的网络结构。
### Conclusion
该研究展示了基于ResNet架构的神经架构搜索空间与优化方法在多个数据集上的应用效果，证明了该方法能够找到具有竞争力的网络架构，特别是在MNIST、Fashion-MNIST和CIFAR100数据集上。
## 554. `cs.LG` - 基于Transformer的神经架构搜索方法 [PDF](https://arxiv.org/pdf/2505.01314), [HTML](https://arxiv.org/abs/2505.01314)
### Authors
Shang Wang,Huanrong Tang,Jianquan Ouyang
### Background
该领域目前存在多种神经网络结构，但无法确定哪种结构最适合特定任务。传统的搜索方法可能难以找到最佳结构。本文旨在通过引入变换器架构和多目标遗传算法，提出一种新的神经架构搜索方法，以寻找具有更好翻译结果的神经网络结构。
### Innovation
1. 基于Transformer架构，搜索不同编码器和解码器组合下的多头注意力机制计算方式。2. 除了BLEU分数外，还引入困惑度作为辅助评估指标，通过多目标遗传算法对种群中的每个神经网络进行迭代优化，提高其性能。
### Conclusion
实验结果表明，所提出的方法搜索到的神经网络结构优于所有基线模型，而引入辅助评估指标能够找到比仅考虑BLEU分数更好的模型。
## 555. `cs.LG` - 基于机器学习的缩短评估问卷框架以评估自闭症干预 [PDF](https://arxiv.org/pdf/2510.26808), [HTML](https://arxiv.org/abs/2510.26808)
### Authors
Audrey Dong,Claire Xu,Samuel R. Guo,Kevin Yang,Xue-Jun Kong
### Background
照顾自闭症患者的人通常认为77项自闭症治疗评估检查表(ATEC)复杂且耗时，限制了其在常规监控中的应用。本文探讨了利用纵向ATEC数据，通过特征选择和交叉验证技术识别最能预测纵向治疗跟踪和点时严重程度评估的项目，从而简化评估问卷，保持评估准确性。
### Innovation
本文提出了一种通用化的机器学习框架，该框架致力于缩短评估问卷长度，同时保持评估准确性。通过优化子集、模型可解释性和统计严谨性，该方法能够广泛应用于其他高维心理测量工具。
### Conclusion
构建的框架能够实现更便捷、更频繁且更具可扩展性的评估，并为神经发育和精神病学领域的AI支持干预提供数据驱动的方法。
## 556. `cs.LG` - 使用强化学习辅助糖尿病生活方式医学治疗 [PDF](https://arxiv.org/pdf/2510.26807), [HTML](https://arxiv.org/abs/2510.26807)
### Authors
Yuhan Tang
### Background
2型糖尿病的预防和治疗可以从个性化的生活方式建议中受益。然而，个性化的生活方式医学建议的提供受到专业人员短缺和医生技能差异的限制。本研究提出了一个基于离线上下文臂赛范畴的方法，该方法通过最小化Magni葡萄糖风险-收益函数，从119,555名参与者的NHANES综合资料中学习个性化的生活方式建议。研究将任务视为单步上下文臂赛范畴，旨在通过混合动作Soft Actor-Critic算法生成风险意识的生活方式医学建议，并验证这些建议与来自湘雅医院的三位认证医生提供的建议的相似性。
### Innovation
本研究提出了一个基于离线上下文臂赛范畴的方法，通过最小化Magni葡萄糖风险-收益函数，从NHANES综合资料中学习个性化的生活方式建议。该方法利用混合动作Soft Actor-Critic算法生成风险意识的生活方式医学建议，可以验证跨时段NHANES数据生成的风险意识生活方式医学建议的有效性，需要进一步的前瞻性临床验证。
### Conclusion
研究结果表明，离线混合动作Soft Actor-Critic算法可以从跨时段NHANES数据中生成风险意识的生活方式医学建议，这需要在前瞻性临床试验中进一步验证。
## 557. `cs.LG` - 使用高斯过程建模研究脑肿瘤儿童和年轻人放疗的长期影响 [PDF](https://arxiv.org/pdf/2510.26814), [HTML](https://arxiv.org/abs/2510.26814)
### Authors
Angela Davey,Arthur Leroy,Eliana Vasquez Osorio,Kate Vaughan,Peter Clayton,Marcel van Herk,Mauricio A Alvarez,Martin McCabe,Marianne Aznar
### Background
儿童癌症幸存者需要长期监测放疗的副作用，但现有的纵向监测数据往往样本频率低且不规则，准确性也存在问题。因此，通常会孤立地研究这些测量值，或者使用简单的线性关系来填补缺失的时间点。该研究旨在探索使用高斯过程（GP）建模方法，进行基于人口和个体的预测，以解决这些局限性。以血清胰岛素样生长因子1 (IGF-1) 测量值为例，研究了23名患者（中位数4次，范围1-16次）的训练数据，并将其与文献中报道的数值趋势进行比较。此外，通过8个测试案例进行了个体预测，两种方法的平均均方根误差分别为31.9（10.1 - 62.3）ng/ml 和 27.4（0.02 - 66.1）ng/ml。
### Innovation
研究采用高斯过程（GP）建模方法，用于基于人口和个体预测放疗的长期影响。这种方法克服了常规纵向数据的局限性，有助于分析放疗的长期效果。特别是在预测IGF-1测量值方面，研究获得了较小的误差范围，表明这种方法的有效性。
### Conclusion
高斯过程建模方法可以有效地预测儿童和年轻人脑肿瘤放疗的长期影响，提供了一种分析监测数据的新工具。这种方法的潜在应用可以广泛应用于长期监测和个体健康评估。
## 558. `cs.LG` - VISAT: 使用视觉属性在交通标志识别中对抗和分布偏移鲁棒性的基准测试 [PDF](https://arxiv.org/pdf/2510.26833), [HTML](https://arxiv.org/abs/2510.26833)
### Authors
Simon Yu,Peilin Yu,Hongbo Zheng,Huajie Shao,Han Zhao,Lui Sha
### Background
本文介绍了VISAT，一个用于评估交通标志识别任务中模型鲁棒性的新型开放数据集和基准测试套件，特别关注的是视觉属性的存在。该数据集建立在Mapillary交通标志数据集（MTSD）之上，引入了两个基准分别侧重于对抗性攻击和分布偏移的鲁棒性。此外，通过使用图像增强技术和合成颜色量化技术，评估了对抗性攻击和分布偏移对多任务学习（MTL）网络的影响。
### Innovation
提出VISAT数据集和基准测试框架，旨在评估模型在交通标志识别任务中的对抗和分布偏移鲁棒性。通过使用最先进的投影梯度下降（PGD）方法生成对抗输入，并通过ImageNet-C的数据污染技术和自然变异性进行评估，揭示了MTL任务中的虚假相关性。实验重点使用ResNet-152和ViT-B/32两大基础架构，并对比了基础模型和MTL模型之间的性能。
### Conclusion
VISAT数据集和基准测试框架有助于理解交通标志识别模型的鲁棒性，揭示了对抗性攻击和分布偏移带来的挑战。这项工作将促进更鲁棒模型的发展，以应对自动驾驶和网络物理系统等实际应用中的挑战。
## 559. `cs.LG` - The Denario项目：面向科学发现的深度知识人工智能代理 [PDF](https://arxiv.org/pdf/2510.26887), [HTML](https://arxiv.org/abs/2510.26887)
### Authors
Francisco Villaescusa-Navarro,Boris Bolliet,Pablo Villanueva-Domingo,Adrian E. Bayer,Aidan Acquah,Chetana Amancharla,Almog Barzilay-Siegal,Pablo Bermejo,Camille Bilodeau,Pablo Cárdenas Ramírez,Miles Cranmer,Urbano L. França,ChangHoon Hahn,Yan-Fei Jiang,Raul Jimenez,Jun-Young Lee,Antonio Lerario,Osman Mamun,Thomas Meier,Anupam A. Ojha,Pavlos Protopapas,Shimanto Roy,David N. Spergel,Pedro Tarancón-Álvarez,Ujjwal Tiwari,Matteo Viel,Digvijay Wadekar,Chi Wang,Bonny Y. Wang,Licong Xu,Yossi Yovel,Shuwen Yue,Wen-Han Zhou,Qiyao Zhu,Jiajun Zou,Íñigo Zubeldia
### Background
该论文介绍了Denary，这是一个多功能的AI多代理系统，旨在作为科研辅助工具。Denary可以执行多种任务，如产生研究想法、文献检查、制定研究计划、编写和执行代码、制作图表以及撰写和审阅科学论文。该系统具有模块化架构，能够处理特定任务，并且能够使用Cmbagent作为深度研究后端，在端到端科学研究中发挥作用。
### Innovation
Denary是一个高度多样性任务处理的多代理系统，拥有灵活的模块化设计。此外，该系统能够跨学科整合不同领域的研究方法并应用于具体的科学研究场景中。论文还详细描述了该系统及其模块，并通过多个AI生成的科学论文展示了其应用效果。
### Conclusion
作者总结了Denary系统的优点、缺点和限制。同时讨论了AI驱动科研的伦理问题，并反思了这种技术与科学哲学的关系。文章最后公开发布了代码，并提供了一个在线demo供用户直接运行。
## 560. `cs.LG` - 基于验证推理的逆向知识搜索：从长推理链知识库构建科学百科全书 [PDF](https://arxiv.org/pdf/2510.26854), [HTML](https://arxiv.org/abs/2510.26854)
### Authors
Yu Li,Yuan Huang,Tao Wang,Caiyu Fan,Xiansheng Cai,Sihan Hu,Xinzijian Liu,Cheng Shi,Mingjun Xu,Zhen Wang,Yan Wang,Xiangqi Jin,Tianhan Zhang,Linfeng Zhang,Lei Wang,Youjin Deng,Pan Zhang,Weijie Sun,Xingyu Li,Weinan E,Linfeng Zhang,Zhiyuan Yao,Kun Chen
### Background
大多数科学材料简略了推理过程，简述结论而忽略了证明这些结论的推导链。这种简略性限制了验证过程，因为它缺少明确、逐步的证明步骤，并且阻碍了跨领域的联系，因为推理过程中的逻辑和因果关系路径被压缩了。因此，需要一种框架来分解和验证科学推理，从而生成一个可验证的长推理链知识库，并进一步构建出科学百科全书SciencePedia。
### Innovation
该论文引入了一个可扩展的框架，用于分解科学推理并构建一个可验证的长推理链知识库，然后将其投影到新兴的百科全书中。框架运用自上而下的还原策略，通过基于约200门课程的Socratic代理生成大约300万个基本原则问题，并通过多重模型生成、提示清理和跨模型答案一致性筛选，确保推理链的可靠性。验证过的推理链数据集支持了一个头脑风暴搜索引擎，该搜索引擎可以检索汇聚至目标概念的多种基本原则推导。论文还利用可验证的推理链知识库构建了以推理为中心的方法，实现了大规模的跨学科科学综合，并为建立不断扩展的百科全书奠定了基础。
### Conclusion
这种基于验证推理的方法能够大规模实现可信的跨学科科学综合，并为构建不断扩展的科学百科全书奠定了基础。
## 561. `cs.LG` - LLMs are Overconfident: Evaluating Confidence Interval Calibration with FermiEval [PDF](https://arxiv.org/pdf/2510.26995), [HTML](https://arxiv.org/abs/2510.26995)
### Authors
Elliot L. Epstein,John Winnicki,Thanawat Sornwanee,Rajat Dwaraknath
### Background
大语言模型（LLMs）在数值估算方面表现出色，但在正确量化不确定性方面存在困难。研究发现，LLMs经常表现出过度自信。为了评估这一行为，论文引入了一种名为FermiEval的基准测试，专门针对费米估算问题，并提出了严格的置信区间覆盖和锐度评分规则。
### Innovation
该研究通过引入FermiEval基准测试来评估LLMs置信区间中的不确定性量化能力，并且发现即使名义上的99%置信区间平均也只覆盖真实答案的65%。进一步提出了一种基于可信性预测的方法来获得准确的99%覆盖区间，并且Winkler区间评分降低了54%。此外，提出直接概率引入和分位数调整方法以在高置信度水平上减少过度自信。
### Conclusion
研究开发了一种感知隧道理论来解释为什么LLMs表现出过度自信：当在不确定情况下进行推理时，它们似乎仅从其推断分布的截断区域进行采样，忽视了其尾部。
## 562. `cs.LG` - 在线体育粉丝社区是否变得更加冒犯？对r/PremierLeague主题、趋势和毒性的量化回顾 [PDF](https://arxiv.org/pdf/2510.27003), [HTML](https://arxiv.org/abs/2510.27003)
### Authors
Muhammad Zeeshan Mazhar,Tolga Buz,Yiran Su
### Background
在线体育粉丝社区，特别是Reddit上的r/PremierLeague，已成为英超球迷的聚集地，尤其是在美国市场取得了显著的增长。尽管英超联赛具有广泛的吸引力，但对其在线粉丝社区的理解仍有明显缺口。因此，本文通过对2013年至2022年间在r/PremierLeague上发布的超过110万条评论进行了分析，研究了这些讨论中的情感、话题和毒性，并追踪了这些趋势随时间的变化。
### Innovation
本文采用量化的方法对r/PremierLeague上的议题、趋势和毒性进行了研究，填补了对英超在线球迷社区缺乏了解的空白。
### Conclusion
尽管英超在线粉丝讨论的多元化显著增加，但负面情绪和毒性也出现了上升趋势。r/PremierLeague已经成为了用户表达对社会问题（如种族主义、COVID-19大流行和政治紧张）不满的讨论场所。
## 563. `cs.LG` - 用于水下生物声学降噪与识别的多表示关注框架 [PDF](https://arxiv.org/pdf/2510.26838), [HTML](https://arxiv.org/abs/2510.26838)
### Authors
Amine Razig,Youssef Soulaymani,Loubna Benabbou,Pierre Cauchy
### Background
在圣劳伦斯河口监测海洋哺乳动物面临巨大挑战，因为它们的叫声频率范围广泛，从低频呻吟到超声波点击声不等，且叫声常常重叠并且被不同程度的人类活动和环境噪声所掩盖。因此，需要一种多步骤、带有关注指导的框架，可以有效地分割声谱图，生成生物相关能量的软遮罩，然后将这些遮罩与原始输入融合以进行多频带去噪分类，从而提高信号识别能力，并在不同环境条件下和信噪比下建立可靠的海洋哺乳动物监测模式。
### Innovation
提出了一种多步、带有关注指导的框架，首先对声谱图进行分割以生成生物相关能量的软遮罩，然后将这些遮罩与原始输入融合进行多频带去噪分类。该框架通过中层融合将图像和掩码嵌入，使得模型能够专注于关键的声谱图区域，同时保留全局上下文。实验中使用加拿大萨格奈克圣劳伦斯海洋公园研究站的实际记录展示了该方法在提高信号识别、减少误报检测和生成可靠的表现方面优于基本模型。框架在不同的环境条件和信噪比下具有鲁棒性，即使在分布偏移的情况下，其性能也能保持稳定。
### Conclusion
该框架在所有实验设置中均优于基本架构，无论是在相同分布内还是在Out-of-distribution情况下，都显著提高了准确性。其鲁棒性表明MGC能够学习到可迁移的表示，而不是过度适应特定的变换，从而增强了其在大规模、实际环境中监测生物多样性的适用性。
## 564. `cs.LG` - 基于Missouri地区的区域框架实现精确土壤健康 [PDF](https://arxiv.org/pdf/2510.26815), [HTML](https://arxiv.org/abs/2510.26815)
### Authors
Dipal Shah(1),Jordon Wade(2),Timothy Haithcoat(3),Robert Myers(4),Kelly Wilson(1) ((1) School of Natural Resources, University of Missouri, Columbia, MO, USA, (2) Crop Protection Research &amp; Development, Syngenta Group, Basel, Switzerland, (3) Institute for Data Science and Informatics, University of Missouri, Columbia, MO, USA, (4) School of Plant Science &amp; Technology, University of Missouri, Columbia, MO, USA)
### Background
有效的土壤健康管理对维持农业、增强生态系统弹性和保持水质至关重要。然而，密苏里州复杂多样的地貌限制了广泛通用管理建议的有效性。现有的土壤分类系统缺乏分辨率，需要以数据驱动的方式提供特定地点的信息，以指导针对性的干预措施。因此，研究开发了一种区域性的土壤聚类框架，旨在支持整个州范围内的精准土壤健康管理策略。该方法利用高分辨率SSURGO数据集，侧重处理0至30厘米根区的土壤属性。通过使用变分自编码器和KMeans聚类的多元分析来对具有相似特性的土壤进行分组。通过统计指标如轮廓系数和现有分类单元的对照来验证聚类的有效性，以确保其在空间上的连贯性。通过这种方式，研究确定了有助于捕捉密苏里州不同农业生态地区独特纹理、水力和化学肥力特性的土壤组。地图识别出了十种不同的土壤健康管理区域。由于其足够大以捕捉继承的土壤模式，同时又容易在市场上实现，最终选择了十个聚类区作为最优选择。根深限制和饱和水力渗透性是驱动土壤差异的主要变量。每个管理区域由独特的高岭土、有机质、pH值和可用水容量组成。该框架将复杂的数据分析与针对性的实际建议相结合，帮助保护规划者和农学家优化管理实践，实现全省范围内的资源利用效率提高。
### Innovation
研究开发了一种基于高分辨率SSURGO数据集的区域土壤聚类框架，利用变分自编码器和KMeans聚类进行多元分析来分组具有相似特性的土壤。通过统计指标验证聚类的有效性。该方法能够识别独特的土壤属性，适用于密苏里州复杂多样的农业生态区域。最终确定了十个土壤健康管理区，为精确的土壤健康管理提供了可行的区域框架。
### Conclusion
该研究通过开发区域性的土壤聚类框架，成功识别出适用于密苏里州不同农业生态区域的十个土壤健康管理区。这种方法将复杂的数据分析与可行的、针对性的实际建议相结合，为保护规划者和农学家提供了优化管理实践和提高资源利用效率的途径。
## 565. `cs.LG` - 为异构LLM工作负载的类别感知语义缓存 [PDF](https://arxiv.org/pdf/2510.26835), [HTML](https://arxiv.org/abs/2510.26835)
### Authors
Chen Wang,Xunzhuo Liu,Yue Zhu,Alaa Youssef,Priya Nagpurkar,Huamin Chen
### Background
LLM服务系统处理异构查询负载，不同类别展示出不同的特性。代码查询在嵌入空间中聚类密集，而对话查询则分布稀疏。内容的陈旧度从分钟级（如股票数据）到月度级（如代码模式）不等。重复查询模式从幂律分布（代码）到均匀分布（对话），产生长尾缓存命中率分布：高重复类别可实现40-60%的命中率，而低重复或易变类别可实现5-15%的命中率。向量数据库必须排除长尾效应，因为远程搜索成本（30ms）要求至少15-20%的命中率才能收支平衡，从而留下20-30%的生产流量未被缓存。固定策略缓存进一步加剧了这一问题：固定的阈值在密集空间中导致误报，并在稀疏空间中错过有效的同义词；固定的TTL浪费内存或提供陈旧数据。
### Innovation
本文提出了类别感知的语义缓存，其中相似阈值、TTL和配额根据查询类别变异。介绍了一种混合架构，将内存中的HNSW搜索与外部文档存储分离，将错过成本从30ms降低到2ms。这使得低命中率类别在经济上可行（收支平衡在3-5%与15-20%之间），并使整个负载分布的缓存覆盖率成为可能。基于负载的自适应策略扩展了这一框架，根据下游模型负载动态调整阈值和TTL，理论预测这可将模型流量减少9-17%。
### Conclusion
类别感知的语义缓存架构减少错过成本，使低命中率类别在经济上成为可能，扩展了缓存覆盖范围至整个负载分布。自适应负载策略提供了进一步的优化，以减少超载模型的流量。
## 566. `cs.LG` - 在空间数据上采用因果掩蔽：学习空间数据的一元语言模型的信息论案例 [PDF](https://arxiv.org/pdf/2510.27009), [HTML](https://arxiv.org/abs/2510.27009)
### Authors
Jared Junkin,Samuel Nathanson
### Background
传统的语言模型通常是基于因果掩蔽设计的。但在具有空间或关系结构的领域中，因果掩蔽通常被认为不适当，因此更为常用的是顺序线性化。然而，关于因果掩蔽在非顺序数据中引入的信息损失是否可行，特别是在不损失表现力的情况下，这个问题鲜有直接研究。这是因为很少有领域同时提供空间和顺序表示的数据集。本文在象棋这一自然支持这两种表示法的领域中研究了这个问题。
### Innovation
该研究采用了一种新颖的方法，通过使用双向和因果自注意力机制训练语言模型，分别在基于棋盘的空间数据和基于移动序列的顺序数据上进行训练。实验结果表明，即使采用因果掩蔽方法训练的空间数据模型也能在棋艺表现上超过顺序数据模型。
### Conclusion
本研究表明，因果掩蔽可以应用于空间数据，在一些领域甚至优于顺序化。这种方法为训练在空间数据上的一元语言模型提供了可行的信息论依据，可能对未来语言模型的应用具有更广泛的指导意义。
## 567. `cs.LG` - 基于域分解架构和高斯-牛顿训练的物理信息神经网络 [PDF](https://arxiv.org/pdf/2510.27018), [HTML](https://arxiv.org/abs/2510.27018)
### Authors
Alexander Heinlein,Taniya Kapoor
### Background
通过神经网络逼近由偏微分方程支配的边值问题的解具有挑战性，主要原因是训练过程复杂。这种复杂性部分源于光谱偏置，即高频分量收敛较慢的现象。
### Innovation
将域分解与高斯-牛顿优化相结合，以加快收敛速度。相较于基于梯度的方法（如Adam），这种方法可以在每次迭代中解决病态线性系统，但可以减少迭代过程中的计算成本。
### Conclusion
结合局部化和高斯-牛顿优化对于基于神经网络的偏微分方程求解器具有潜在的前景。
## 568. `cs.LG` - 弹性架构搜索用于高效语言模型 [PDF](https://arxiv.org/pdf/2510.27037), [HTML](https://arxiv.org/abs/2510.27037)
### Authors
Shang Wang
### Background
随着大型预训练语言模型在自然语言理解任务中变得越来越关键，它们巨大的计算和内存要求引起了经济和环境方面的担忧。
### Innovation
本文介绍了一种名为Elastic Language Model (ELM)的创新神经架构搜索方法，它针对紧凑型语言模型进行了优化。ELM通过引入灵活的搜索空间和高效的变压器块以及动态模块来调整维度和头数，增强了搜索过程的效率和灵活性。此外，还引入了新的知识蒸馏损失，以改善搜索过程中每个模块的独特特征的保留，从而提高架构选择的区分性。
### Conclusion
在掩码语言建模和因果语言建模任务中的实验表明，通过ELM发现的模型显著优于现有方法。
## 569. `cs.LG` - 通过动力相匹配学习可泛化的视知觉策略 [PDF](https://arxiv.org/pdf/2510.27114), [HTML](https://arxiv.org/abs/2510.27114)
### Authors
Dohyeok Lee,Jung Min Lee,Munkyung Kim,Seokhun Ju,Jin Woo Koo,Kyungjae Lee,Dohyeong Kim,TaeHyun Cho,Jungwoo Lee
### Background
行为克隆方法在机器人学习中的泛化能力较差，因为它们的数据支持仅限于专家演示。最近利用视频预测模型的方法通过学习大数据集中的丰富的时空表示取得了令人鼓舞的结果。然而，这些模型学习的是通用的动力学，无法区分不同的控制输入，这限制了它们在精确操作任务中的实用性，需要大量的预训练数据集。
### Innovation
提出了一种动力相匹配流动匹配策略（DAP），将动力学预测整合到策略学习中。该方法引入了一种新颖的架构，其中策略模型和动力学模型在动作生成过程中相互提供纠正反馈，从而实现自我纠正并提高泛化性能。实验验证表明，与基线方法相比，该方法在实际操作任务中的泛化性能更优，特别是在传感器干扰和光照变化等OOD场景中表现出特别的鲁棒性。
### Conclusion
DAP方法在实际机器人操作任务中展示了优越的泛化性能，特别是在出了分布情况（OOD）下表现出了更强的鲁棒性。
## 570. `cs.LG` - 使用基于变压器的机器学习模型将行星大气辐射传输加速几个数量级 [PDF](https://arxiv.org/pdf/2510.27050), [HTML](https://arxiv.org/abs/2510.27050)
### Authors
Isaac Malsky,Tiffany Kataria,Natasha E. Batalha,Matthew Graham
### Background
辐射传输计算是行星大气建模中必不可少的组成部分。标准方法计算成本高昂，且会引入计算速度与准确性的权衡，这使得大尺度模型（如通用环流模型）在进行辐射传输计算时需要采用数值简化，从而影响模拟的精度。辐射传输过程本质上是从静止的大气剖面对应到结果辐射通量的已知物理映射，可以通过原理计算得到高保真数据进行训练，是机器学习仿真的理想候选对象。
### Innovation
我们开发了一个基于变压器神经网络架构的辐射传输模拟器，采用仅编码器结构，利用太阳组成热木星大气剖面数据集进行训练。该模拟器的测试集误差平均值约为传统方法的1%，在速度上实现了100倍的加速。机器学习仿真是加速和提高行星大气模型（如通用环流模型）内辐射传输计算速度和准确性的可能性。
### Conclusion
机器学习方法能够显著加速行星大气中的辐射传输计算过程，同时保持较高的准确性，为改进和优化行星大气模型提供了新的途径。
## 571. `cs.LG` - 过度指定混合判别分析：指数收敛、统计保证及其遥感应用 [PDF](https://arxiv.org/pdf/2510.27056), [HTML](https://arxiv.org/abs/2510.27056)
### Authors
Arman Bolatov,Alan Legg,Igor Melnykov,Amantay Nurlanuly,Maxat Tezekbayev,Zhenisbek Assylbekov
### Background
本文探讨了在混合组件数量超过实际数据分布中存在数量的场景下，混合判别分析（MDA）的分类错误问题，这种情况被称为过度指定。研究使用每个类别内部的两组成部分高斯混合模型拟合从单一高斯分布生成的数据，分析了期望最大化（EM）算法的收敛性和统计分类错误。
### Innovation
研究展示了在适当初始化的情况下，EM算法在总体层级上以指数速度收敛到贝叶斯风险。进一步地，在有限样本条件下，研究工作表明分类错误在 mild 条件下收敛到贝叶斯风险，收敛速率为 $n^{-1/2}$。为理解过度指定MDA在复杂数据设置下（如图像和文本分类）的性能提供了严格理论框架。
### Conclusion
研究通过实验验证了遥感数据集的结果，提供了过度指定MDA的指数收敛和统计保证，扩展了对其在实际应用场景中的理解与应用。
## 572. `cs.LG` - GeoPep：一种针对蛋白质-肽结合位点预测的几何感知掩码语言模型 [PDF](https://arxiv.org/pdf/2510.27040), [HTML](https://arxiv.org/abs/2510.27040)
### Authors
Dian Chen,Yunkai Chen,Tong Lin,Sijie Chen,Xiaolin Cheng
### Background
多模态方法在蛋白质-蛋白质界面预测方面取得了显著成果，结合了蛋白质的序列和结构信息。然而，当将这些方法扩展到蛋白质-肽相互作用时遇到了挑战，因为肽具有固有的构象灵活性，并且可供直接训练结构感知模型的结构数据有限。为了克服这些限制，该论文引入了一个新的框架—GeoPep，该框架利用了ESM3的多模态蛋白质基础模型，通过迁移学习来预测肽结合位点，特别地，在缺乏蛋白质-肽结合数据的情况下，对ESM3进行了微调以适应蛋白质-蛋白质结合数据。此外，该模型使用参数高效的神经网络架构，能够在稀疏数据中学习复杂模式，同时通过基于距离的损失函数利用3D结构信息来增强结合位点预测的准确性。
### Innovation
该研究提出了GeoPep框架，利用了ESM3的多模态蛋白质基础模型进行迁移学习，针对肽结合位点预测进行了微调。该框架整合了一种参数高效的神经网络架构，能够在稀疏数据中学习复杂模式，并且使用基于距离的损失函数结合3D结构信息，提升预测效果。
### Conclusion
全面的评估表明，GeoPep在蛋白质-肽结合位点预测上显著优于现有方法，能够有效捕捉稀疏和异质的结合模式。
## 573. `cs.LG` - SERVIMON: 由AI驱动的天文学观测站预测维护和实时监控 [PDF](https://arxiv.org/pdf/2510.27146), [HTML](https://arxiv.org/abs/2510.27146)
### Authors
Emilio Mastriani,Alessandro Costa,Federico Incardona,Kevin Munari,Sebastiano Spinello
### Background
为了监控分布式的天文学系统（如ASTRI迷你阵列），ServiMon被设计来提供一个可扩展且智能的数据收集和审计管道。该系统提高了望远镜操作的质量控制、预测性维护和实时异常检测的能力。
### Innovation
ServiMon整合了包括Prometheus、Grafana、Cassandra、Kafka和InfluxDB在内的云原生技术，用于遥测数据的收集和处理。它使用机器学习算法（如孤立森林）来检测Cassandra性能指标中的异常。关键指标如读写延迟、吞吐量和内存使用情况将被持续监控并作为时间序列数据存储，以进行特征工程。检测到的异常会被记录在InfluxDB v2中并通过Flux进行实时监控和可视化。
### Conclusion
ServiMon的可扩展框架证明了其对天文基础设施的预测性维护和实时监控的有效性。通过云和边缘计算，它可以适应未来的大型实验，优化性能和成本。结合机器学习和大数据分析，ServiMon成为现代和下一代观测天文学的稳健和灵活的解决方案。
## 574. `cs.LG` - 自适应数据飞轮：应用MAPE控制循环提升AI代理 [PDF](https://arxiv.org/pdf/2510.27051), [HTML](https://arxiv.org/abs/2510.27051)
### Authors
Aaditya Shukla,Sidney Knowles,Meenakshi Madugula,Dave Farris,Ryan Angilly,Santiago Pombo,Anbang Xu,Lu An,Abhinav Balasubramanian,Tan Yu,Jiaxiang Ren,Rama Akkiraju
### Background
企业AI代理必须持续适应以保持准确性、减少延迟并保持与用户需求的一致性。为此，我们介绍了NVInfo AI中NVIDIA Mixture-of-Experts (MoE)知识助理的实践实现，该助理为超过30,000名员工提供服务。通过实现基于MAPE的自适应数据飞轮，我们构建了一个闭环系统，可以系统地解决检索增强生成(RAG)管道中的故障，并实现持续学习。部署后的一个多月监控期内，我们收集了495个负反馈样本，并分析了两种主要故障模式：路由错误（5.25%）和查询重述错误（3.2%）.
### Innovation
我们通过使用NVIDIA NeMo微服务，在查询路由和查询重述方面实现了有针对性的改进，并通过微调实现了模型大小的显著缩小和延迟的显著降低。对于路由，我们用一个微调后的8B变体代替了Llama 3.1 70B模型，实现了96%的准确性，减少了十倍的模型大小，并使延迟降低了70%。对于查询重述，微调提高了3.7%的准确性并减少了40%的延迟。我们的方法展示了即使在有限的用户反馈下，通过在数据飞轮中结构化的HITL反馈如何将企业AI代理转化为自我改进系统。关键经验教训包括确保代理的鲁棒性、处理隐私限制以及在生产环境中执行分阶段部署的方法。这项工作提供了一种可重复的构建强大、适应性强的企业AI代理的蓝图，这些代理能够从大规模的实际使用中学习.
### Conclusion
我们的应用程序证明了在数据飞轮中以HITL反馈结构化时，企业AI代理可以成为自我改进的系统。关键经验教训包括确保代理的鲁棒性、处理隐私限制以及在生产环境中执行分阶段部署的方法。这项工作提供了一种可重复的构建强大、适应性强的企业AI代理的蓝图，这些代理能够从大规模的实际使用中学习。
## 575. `cs.LG` - Sparse Model Inversion: Efficient Inversion of Vision Transformers for Data-Free Applications [PDF](https://arxiv.org/pdf/2510.27186), [HTML](https://arxiv.org/abs/2510.27186)
### Authors
Zixuan Hu,Yongxian Wei,Li Shen,Zhenyi Wang,Lei Li,Chun Yuan,Dacheng Tao
### Background
模型反转旨在从预先训练的判别模型中重建原始训练数据，特别是在原始训练数据因隐私、使用权限或数据规模限制而不可用时非常有用。然而，现有的密集型模型反转方法试图重建整个图像区域，这使得它们在从大型Vision Transformers (ViTs) 反转高分辨率图像时变得非常低效。研究发现，这种低效性有两个根本原因：冗余地反转嘈杂的背景以及无意中反转虚假的相关性，我们将其在模型反转中称为“幻觉”。
### Innovation
我们提出了一种新颖的稀疏模型反转策略，作为一种即插即用的扩展，可以加速现有密集型模型反转方法，而无需修改它们的原始损失函数。具体而言，我们选择性地反转语义前景，同时停止对嘈杂的背景和潜在虚假相关性的反转。通过理论和实证研究，我们验证了该方法在实现显著加速的同时，能够在数据免费模型量化和数据免费知识转移中取得同等甚至更好的下游性能。
### Conclusion
我们的方法在加速模型反转方面取得了显著成效（最多提高3.79倍），同时保持了与之相当甚至改进的下游性能。代码已在GitHub上提供。
## 576. `cs.LG` - 为什么在推理语言模型中出现多语言推理差距？ [PDF](https://arxiv.org/pdf/2510.27269), [HTML](https://arxiv.org/abs/2510.27269)
### Authors
Deokhyung Kang,Seonjeong Hwang,Daehui Kim,Hyounghun Kim,Gary Geunbae Lee
### Background
推理语言模型（RLMs）在复杂推理任务中表现出色，但仍面临多语言推理差距的问题，即对高资源语言的性能优于低资源语言。尽管最近的研究努力减少了这一差距，其根本原因仍不明确。
### Innovation
该研究展示了多语言推理差距主要源于语言理解失败-模型无法将多语言输入的意义转化为其推理过程中的主导语言（即英语）。该研究通过监督方法检测理解失败，并提出仅在检测到理解失败时将多语言输入翻译成英语的策略（Selective Translation），成功缩小了多语言推理差距。
### Conclusion
该研究证明了理解失败是多语言推理差距的主要原因，可以通过检测和选择性缓解来解决。这为更公平的多语言推理提供了重要见解，并提出了潜在路径。
## 577. `cs.LG` - FMint-SDE: 基于误差纠正加速SDE数值模拟的一种多模态基础模型 [PDF](https://arxiv.org/pdf/2510.27173), [HTML](https://arxiv.org/abs/2510.27173)
### Authors
Jiaxin Yuan,Haizhao Yang,Maria Cameron
### Background
动力系统仿真的快速且准确的模拟是科学技术和工程领域中的基本挑战。传统的数值积分器常常在准确性和计算效率之间存在权衡，而现有的基于神经网络的方法通常需要为每种情况训练一个单独的模型。为此，我们提出了一种基于初始化的多模态基础模型，适用于大规模随机微分方程仿真：FMint-SDE（基于初始化的多模态基础模型）。该模型基于带上下文学习的解码器式变压器，利用数值和文本模态学习一个普遍性的误差校正方案，并通过由传统求解器生成的粗略解序列进行训练，从而实现对多样化系统的泛化能力。我们对包括分子动力学、机械系统、金融和生物等多个领域的挑战性SDE基准进行评估，实验结果表明，我们的方法在准确性和效率之间实现了优于传统求解器的平衡，证明了FMint-SDE作为动力系统仿真工具的通用潜力。
### Innovation
提出了基于初始化的多模态基础模型FMint-SDE，该模型结合了数值和文本模态来学习一个普遍性的误差校正方案。其创新之处在于：1）通过上下文学习的解码器式变压器结构，2）利用传统求解器生成的粗略解序列进行预训练，3）这种方法可以广泛应用于不同类型的动力系统，提供了一种更高效的解决方案，与传统求解器相比显著提高了准确性和计算效率。
### Conclusion
实验表明，与传统的求解器相比，FMint-SDE在各种动力系统仿真任务中表现出了显著的准确性和效率优势，证明了其作为通用动力系统仿真工具的巨大潜力。
## 578. `cs.LG` - 医疗知识图谱上的可追溯药物推荐 [PDF](https://arxiv.org/pdf/2510.27274), [HTML](https://arxiv.org/abs/2510.27274)
### Authors
Yu Lin,Zhen Jia,Philipp Christmann,Xu Zhang,Shengdong Du,Tianrui Li
### Background
现有的最先进的药物推荐(Drug recommendation, DR)系统利用深度学习技术来提高药物推荐的准确性，但是缺乏提供推荐过程的任何见解，这对高风险应用来说是一个重要的局限性。
### Innovation
提出了TraceDR，一种新型的医疗知识图谱(Medical Knowledge Graph, MKG)上的药物推荐系统，能够在多任务学习框架下同时预测药物推荐和相关证据，确保信息的规模和质量，从而提高药物推荐的可追溯性。此外，通过自动构建患者健康记录，覆盖了比现有工作更广泛的疾病和药物类型，发布了一个大规模的数据集，用于药物推荐系统的测试。
### Conclusion
TraceDR系统通过结合大规模临床数据和多任务学习框架，提高了药物推荐的透明度和可追溯性，为医疗领域的高风险决策提供了更可靠的信息支持。
## 579. `cs.LG` - 语言是模态：通过编码器注入实现跨语言对齐 [PDF](https://arxiv.org/pdf/2510.27254), [HTML](https://arxiv.org/abs/2510.27254)
### Authors
Rajan Agarwal,Aarush Gupta
### Background
大规模语言模型（LLMs）在低资源、非拉丁文脚本上表现欠佳，主要由于分词器碎片化和跨语言耦合薄弱。现有方法大多需要修改分词器或重新训练解码器，这提高了复杂性和成本。
### Innovation
提出了LLINK（潜藏语言注入非英语知识）方法，这是一种计算效率高的多语言模态方法，不改变分词器也能在不重新训练解码器的情况下条件化指令调优的解码器。首先，通过轻量级对比投影器将冻结的多语言编码器的句子嵌入对齐到解码器的潜藏嵌入空间的保留位置。其次，向量被扩展为K个软槽并用最小适配器训练，使冻结的解码器消耗信号。该方法在双语检索和LLM评估中，显著提高了问题回答表现，分别优于基础模型81.3%和直接微调63.6%。
### Conclusion
通过将低资源语言视为模态的方法，改善了跨语言对齐，尽管模型在数值准确性上仍存在弱点。这种方法为轻量级LLM实现更强的跨语言对齐提供了实际路径。
## 580. `cs.LG` - 隐私感知的多窗口胸部CT连续自我监督学习以增强领域转移鲁棒性 [PDF](https://arxiv.org/pdf/2510.27213), [HTML](https://arxiv.org/abs/2510.27213)
### Authors
Ren Tasai,Guang Li,Ren Togo,Takahiro Ogawa,Kenji Hirata,Minghui Tang,Takaaki Yoshimura,Hiroyuki Sugimori,Noriko Nishioka,Yukie Shimizu,Kohsuke Kudo,Miki Haseyama
### Background
在医学影像诊断中建立稳健且高度泛化的模型极具挑战性，主要因为数据稀缺和标注准确性不足，以及动态医疗环境中固有的领域偏移问题。特别是在胸部CT成像中，这些问题通常表现为窗口设置的不同，这些不同的窗口设置是为了满足不同的临床目的而优化的。传统的自我监督学习（SSL）框架常通过重用旧数据来缓解领域偏移问题，但这种做法由于隐私约束通常不实际。
### Innovation
本文提出了一种新颖的连续自我监督学习（CSSL）框架，旨在同时从多窗口获取的胸部CT图像中学习多种特征，并确保数据隐私。该方法通过连续预训练无标签图像，有效地捕获以前学习的知识与新信息之间的关系。特别地，该方法通过结合一个潜在重播机制，克服了在连续预训练过程中由于领域偏移导致的灾难性遗忘，同时保证了数据隐私。此外，该方法引入了一种特征蒸馏技术，该技术整合了 Wasserstein 距离为基础的知识蒸馏（WKD）和批次知识集束（BKE），增强了模型学习到有意义的、对领域偏移具有鲁棒性的表示能力。
### Conclusion
最后，该方法通过跨两种不同窗口设置获取的胸部CT图像进行验证，展示了与其他方法相比的优越性能。
## 581. `cs.LG` - T3: Test-Time Model Merging in VLMs for Zero-Shot Medical Imaging Analysis [PDF](https://arxiv.org/pdf/2510.27265), [HTML](https://arxiv.org/abs/2510.27265)
### Authors
Raza Imam,Hu Wang,Dwarikanath Mahapatra,Mohammad Yaqub
### Background
在医学成像中，视觉-语言模型面临一个关键两难：预训练网络提供广泛的鲁棒性，但缺乏特定模态的细微特征；而微调的专家模型在模态内的准确性高，但在模态切换时表现不佳。现有的为自然图像基准设计的模型合并技术简单高效，但在多种医学模态中未能实现一致的收益；这些固定插值的局限性影响了多种临床任务的可靠性。
### Innovation
我们引入了Test-Time Task adaptive merging (T^3)，这是一种无需反向传播的框架，通过计算两个模型输出分布的Jensen-Shannon距离来为每个样本确定插值系数。T^3动态地在模型一致时保持局部精度，在漂移时依赖于泛化专家的鲁棒性。为克服样本级别的合并带来的推理成本，我们进一步提出了一种批量级别的扩展T^3_B，该方法在批次样本上计算合并系数，显著减少了计算瓶颈。我们制定了一个严格的跨评估协议，涵盖不同模态下的领域内、基准到新颖以及干扰情况，从而为医学成像合并建立了标准化基准。
### Conclusion
实验证明，T^3在Top-1准确性上设立了新标准，有效降低了误差，优于强大的基线模型，且保持了高效性，为在临床环境中适应性部署多模态视觉-语言模型铺平了道路。我们的代码可在以下链接获取。
## 582. `cs.LG` - 当AI交易代理竞争时：基于强化学习的市场制作对元订单的不利选择 [PDF](https://arxiv.org/pdf/2510.27334), [HTML](https://arxiv.org/abs/2510.27334)
### Authors
Ali Raza Jafree,Konark Jain,Nick Firoozye
### Background
近年来，高频交易者通过利用低频交易者的不成熟策略来获取不公平的优势，即不利选择。这种现象在金融市场上日益普遍，特别是在竞争激烈的高频市场上。传统的交易模型通常基于外生价格影响假设，但现实市场的价格影响是内生的，因此需要新的模型来捕捉这些市场特性。本研究利用Hawkes型订单簿模型结合强化学习（RL）来模拟高频市场制作者的购销行为，进而研究不利选择现象。研究者发现，市场的高频AI代理可以通过学习来利用低频交易者的元订单执行策略中的价格偏移，从而获得收益，但这种做法并不会显著增加低频交易者的滑点成本。
### Innovation
基于Hawkes模型和激励控制强化学习框架来模拟高频市场制作者的行为，采用Proximal Policy Optimization (PPO) 和自模仿学习方法进行强化学习模拟。研究引入了基于AI代理的竞争视角，探索和量化了不利于低频交易者的不利选择现象，并通过实例展示了高频AI代理如何通过学习来利用既定的市场策略实现利润增长。研究创新性地使用了内生价格影响的市场模型和强化学习算法，以更真实地模拟市场动态和投资者行为。
### Conclusion
研究显示，随着高频交易代理利用强化学习技术进行竞争，以及不利选择的交易策略发展趋势，中低频交易者的滑点成本可能会上升。然而，高频市场制作AI代理的获利并未导致显著的滑点增加，表明这种现象并不一定直接加剧市场摩擦，但从长远来看，这种不公平的优势可能会改变市场整体的交易成本结构。未来研究可进一步探讨不同市场环境下的不利选择影响和对策。
## 583. `cs.LG` - FPS: 基于前向传播的参数选择用于高效的微调 [PDF](https://arxiv.org/pdf/2510.27359), [HTML](https://arxiv.org/abs/2510.27359)
### Authors
Kenneth Yang,Wen-Li Wei,Jen-Chun Lin
### Background
参数高效的微调（PEFT）已经成为适应大规模预训练模型到下游任务的关键策略，但现有方法面临明显限制。基于添加的方法（如适配器）增加推理延迟和工程复杂性；基于选择的方法（如梯度参数选择）则需要完整的反向传播，导致峰值内存使用量与完整微调相同。
### Innovation
我们提出了基于前向传播的参数选择（FPS），这是一种无梯度方法，可以在单次前向传播中识别出最优参数子集。FPS 通过参数的幅度与其输入激活的乘积对参数进行排序，利用预训练知识和下游数据。FPS 在多项视觉任务中实现了可媲美最新方法的性能，同时将峰值内存使用量减少了近 9 倍，参数选择加速了约 2 倍，提供了一个真正高效且实用的解决方案，用于大规模预训练模型的微调。
### Conclusion
FPS 在 24 项视觉任务中达到了与最新方法相当的性能，同时显著降低了内存使用量和加速了参数选择过程，提供了一种真正高效且实用的微调大型预训练模型的方法。
## 584. `cs.LG` - 基于成对和属性感知的决策树偏好获取方法在冷启动推荐中的应用 [PDF](https://arxiv.org/pdf/2510.27342), [HTML](https://arxiv.org/abs/2510.27342)
### Authors
Alireza Gharahighehi,Felipe Kenji Nakano,Xuehua Yang,Wenhan Cu,Celine Vens
### Background
推荐系统（RSs）通过分析用户的历史交互记录来推断用户的偏好，并据此推荐个性化内容。基于协同过滤的推荐系统能够在用户生成数据的基础上进行推荐，但对于刚加入平台的冷启动用户，则缺乏历史数据支持，难以提供个性化推荐。为解决这一问题，可以使用评分获取技术来收集用户的初始评分或偏好，这对于建立用户早期兴趣模型至关重要。传统的决策树评分获取方法适用于非个性化场景，但对于冷启动推荐而言，可以进一步优化，例如通过成对项目查询和考虑属性偏好来提高推荐效果和用户满意度。本文在音乐推荐的背景下，提出了一种改进的决策树评分获取方法，不仅获取项目评分，还获取项目属性偏好，同时使用项目对而非单个项目进行查询，提高了查询效率和推荐准确性。
### Innovation
本文提出了一种基于成对和属性感知的决策树评分获取方法，主要用于解决冷启动用户推荐问题。该方法不仅通过成对项目查询用户偏好，还获取了项目属性偏好以更好地聚类用户，提高了推荐系统的个性化水平和推荐性能，特别是在减少查询数量方面表现突出。这种方法提高了冷启动用户推荐的效果，同时也为音乐推荐提供了新的思路。
### Conclusion
实验结果表明，该方法能有效提高推荐系统的性能，并且减少了查询次数，特别是在使用成对项目查询和考虑属性偏好方面。这些改进在处理冷启动用户推荐时尤为显著，显示了该方法的潜在应用价值。
## 585. `cs.LG` - 随机森林模型感知的可解释反事实解释 [PDF](https://arxiv.org/pdf/2510.27397), [HTML](https://arxiv.org/abs/2510.27397)
### Authors
Joshua S. Harvey,Guanchao Feng,Sai Anusha Meesala,Tina Zhao,Dhagash Mehta
### Background
尽管机器学习模型具有强大的预测能力，但在金融等受监管的行业中，由于解释能力有限，它们往往不适合应用。虽然模型无拘束的方法如Shapley值提供了便利且受欢迎的选择，但它们通常不符合人们寻求的因果解释类型。反事实案例解释——告知个体其结果发生变化需要哪些不同情况，可能更为直观且实用。然而，找到适当的反事实案例以及解释哪些特征是结果变化的关键仍然是一个开放的挑战。
### Innovation
本文通过将反事实搜索和解释的构建问题表述为相似性学习，利用随机森林预测模型本身学习的表示来解决这一挑战。找到反事实后，通过原始实例到达反事实的决策树分区路径来计算解释的重要性。这种方法不仅在MNIST手写数字数据集和德国信用数据集上有效，而且生成的解释也比Shapley值更为精练且更实用。
### Conclusion
本文提出了一种利用随机森林预测模型的表示进行反事实解释的方法，这种方法能够提供更精练且更实用的解释，并且取得了良好的实验结果。
## 586. `cs.LG` - 最优输运问题与使用最优向量场的动作匹配的等价性 [PDF](https://arxiv.org/pdf/2510.27385), [HTML](https://arxiv.org/abs/2510.27385)
### Authors
Nikita Kornilov,Alexander Korotin
### Background
Flow Matching (FM) 方法在生成模型中通过构造概率分布之间的插值并学习定义插值的向量场来映射任意的概率分布。最近的研究表明，通过考虑特定的最优向量场，FM方法可以优化到任意初始插值下的二次代价函数。不过，这种方法仍然需要手动选择初始插值。在这篇论文中，作者提出了一个新的观点，认为直接学习最优向量场可以将最优输运问题和动作匹配（Action Matching, AM）联系起来，从而不需要手动选择初始插值，直接从给定的一系列分布中学习向量场，这样可以简化和优化该过程。
### Innovation
作者将最优输运问题与动作匹配方法联系起来，提出了一种新的方法，即动作匹配（AM），该方法通过直接学习最优向量场来定义一个连续的分布转变过程，从而简化了从分布到分布的变换过程。这种方法避免了手动选择初始插值，并且得到了最优输运问题的解，进而在理论上统一了生成模型中的几种不同方法。
### Conclusion
通过提出动作匹配（AM）方法，直接从给定的一系列分布中学习最优向量场，该方法不仅简化了从分布到分布的变换过程，还能够求解最优输运问题，证明了最优输运问题与动作匹配在某种特定条件下等价。
## 587. `cs.LG` - FOCUS：长视频理解高效关键帧选择 [PDF](https://arxiv.org/pdf/2510.27280), [HTML](https://arxiv.org/abs/2510.27280)
### Authors
Zirui Zhu,Hailun Xu,Yang Luo,Yong Liu,Kanchan Sarkar,Zhenheng Yang,Yang You
### Background
多模态大型语言模型（MLLMs）将图像和视频帧表示为视觉令牌。但是，从单张图像扩展到长达数小时的视频时，令牌预算急剧膨胀，远远超过实际限制。目前主流的方法要么均匀采样，要么利用检索式评分的小尺寸视觉-语言模型进行关键帧选择。然而，这些关键帧选择方法仍然需要在检索后进行筛选，以降低推理成本，但可能会漏掉最有信息的时刻。
### Innovation
本文提出了一种名为FOCUS的训练无监督、模型无关的关键帧选择模块，该模块在严格的令牌预算下选择查询相关的帧。FOCUS将关键帧选择问题转化为多臂老虎机中的组合完全探索问题（CPE），通过经验均值和伯恩斯坦置信半径识别信息区域，并保留不确定区域的探索。FOCUS通过一个两阶段探索-利用过程，首先识别高价值的时间区域，然后在每个区域选择最高评分的关键帧。针对长视频问答基准测试，FOCUS在处理不到2%的视频帧的情况下提供了显著的准确性提升，并在长视频基准（LongVideoBench）上，对于超过20分钟的视频，实现了11.9%的准确性增益。
### Conclusion
FOCUS作为一种关键帧选择方法，在长视频理解中取得了明显的效果，并提供了简化且通用的解决方案，实现了具有MLLMs的长视频理解的可扩展性。
## 588. `cs.LG` - 使用切片 Wasserstein 距离的最优两样本检验 [PDF](https://arxiv.org/pdf/2510.27498), [HTML](https://arxiv.org/abs/2510.27498)
### Authors
Binh Thuan Tran,Nicolas Schreuder
### Background
关于非参数两样本检验，现有的理论和实证研究显示切片 Wasserstein 距离在提供强大的统计保障和计算效率之间具有明显优势，然而，这种距离在假设检验的理论基础方面仍然存在局限性。本文研究了使用切片 Wasserstein 距离进行非参数两样本检验的问题，并探讨了其理论基础差距。
### Innovation
文章提出了基于替换的切片 Wasserstein 检验方法，并分析了其性能。该方法继承了替换原则下的有限样本第一类错误控制能力。进一步建立了非退化能量边界，并展示了该方法实现了 multinomial 和有界支持替代下的最小最大分离率 $n^{-1/2}$，与基于核函数的测试具有相同最优的保证，并基于 Wasserstein 距离的几何基础。此外，该分析还量化了投影数量与统计功效之间的权衡。
### Conclusion
数值实验表明，该测试兼具有限样本的有效性和竞争力及可扩展性，并且与其他需要精细核调优的基于核的测试相比，在我们考虑的所有场景中表现一致。
## 589. `cs.LG` - 在热带干森林中估算地上生物量：机载、无人和空间激光扫描的比较 [PDF](https://arxiv.org/pdf/2510.27408), [HTML](https://arxiv.org/abs/2510.27408)
### Authors
Nelson Mattié,Arturo Sanchez-Azofeifa,Pablo Crespo-Peremarch,Juan-Ygnacio López-Hernández
### Background
根据巴黎气候变化协定的要求，各国需每两年提交温室气体排放和吸收报告至2024年。森林在减碳方面起着关键作用，因此改善热带干森林地上生物量估算方法变得尤为重要。热带干森林被视为最不理解的热带森林环境之一，准确的碳池估算方法是必要的。目前，森林数据质量较高，尤其是在关键指标估算上的准确性提高变得迫切。
### Innovation
本研究采用了机载激光扫描（ALS）、无人激光扫描（ULS）和空间激光扫描（SLS）数据，并结合普通最小二乘法（OLS）和贝叶斯支持向量机（SVM）方法来获取森林指标，并通过机器学习方法进行了变量选择、SVM回归调优和交叉验证。研究结果确定了对Alsd和Ulds基于地上生物量估计的关键变量，并展示了不同激光扫描系统的误差，SLSF W表现出最低的误差。
### Conclusion
使用ALSD和ULSD的地上生物量估算是由六个关键变量决定的：树高、地表粗高度、地形高度、树冠高度、林隙指数和冠层覆盖。运用SVM回归的地上生物量估计值在十块永久热带干森林中范围内为26.02 Mg/ha到175.43 Mg/ha，并且使用SVM回归的激光扫描系统的误差为17.89，其中SLSF W表现最佳，误差为17.07，用于估算每块面积的总生物量。
## 590. `cs.LG` - pDANSE: 基于粒子的数据驱动非线性状态估计从非线性测量 [PDF](https://arxiv.org/pdf/2510.27503), [HTML](https://arxiv.org/abs/2510.27503)
### Authors
Anubhab Ghosh,Yonina C. Eldar,Saikat Chatterjee
### Background
文章讨论了在无模型（过程状态转移模型未知）的系统中，基于数据驱动的方法进行非线性状态估计的问题。现有方法通常要求测量系统为线性的，从而可以得到状态后验的闭解。但实际应用中，非线性测量系统的存在使得获得闭解变得不切实际。
### Innovation
文章提出了一种基于粒子的数据驱动非线性状态估计方法（pDANSE），它使用递归神经网络（RNN）来估计无模型过程的状态，并通过粒子采样技巧来克服非线性测量带来的问题，避免了计算密集的序列蒙特卡洛（SMC）和祖先采样方法，同时提供了半监督学习的方法转换到无监督学习，提高了训练效果和效率。
### Conclusion
通过使用随机洛伦兹-63系统作为实验基准，文章展示了pDANSE在不同非线性测量系统下的状态估计性能，表明其性能与对洛伦兹-63系统STM完全了解的粒子滤波器相媲美。
## 591. `cs.LG` - 在异构双曲流形上的树状模态对齐 [PDF](https://arxiv.org/pdf/2510.27391), [HTML](https://arxiv.org/abs/2510.27391)
### Authors
Wu Wei,Xiaomeng Fan,Yuwei Wu,Zhi Gao,Pengxiang Li,Yunde Jia,Mehrtash Harandi
### Background
视觉语言模型（VLMs）通过跨模态有效整合信息至关重要。但现有方法从文本中提取分层特征，却用单个特征表示每张图像，导致不对称且次优的对齐。
### Innovation
提出了一种称为'树状模态对齐'的方法，该方法构建并配对了图像和文本模态的树状分层特征。具体而言，引入了一种语义感知的视觉特征提取框架，利用交叉注意力机制从中间Transformer层的视觉类别标记中提取特征，并由文本线索引导，提取具有从粗到细语义的视觉特征。通过将两个模态的特征树嵌入具有不同曲率的双曲流形中，有效地建模它们的分层结构。通过定义异构流形上分布之间的KL距离度量，并通过最小化距离来学习中间流形，实现了不同曲率异构流形上的配对。
### Conclusion
在多个图像数据集上的分类任务中的实验表明，在少量样本和跨域设置下，该方法始终超越了强基线。
## 592. `cs.LG` - BiSparse-AAS: B线性稀疏注意力和自适应跨度框架实现可扩展和高效的文本摘要 [PDF](https://arxiv.org/pdf/2510.27516), [HTML](https://arxiv.org/abs/2510.27516)
### Authors
Desta Haileselassie Hagos,Legand L. Burge,Anietie Andy,Anis Yazidi,Vladimir Vlassov
### Background
基于Transformer的架构已经提高了文本摘要的效果，但其二次复杂度限制了其在长文档上的可扩展性。这限制了其在实际应用中的广泛使用，尤其是在需要处理大量信息和长文本的情况下。然而，现有的方法在处理长文档时遇到了效率和模型规模的挑战。因此，探讨一种既能提高效率又能保持高性能的方法变得尤为重要，这正是本文所讨论的内容。
### Innovation
本文提出了一种称为BiSparse-AAS（Bilinear Sparse Attention with Adaptive Spans）的新型框架，该框架将稀疏注意力、自适应跨度和线性二元注意力相结合，以解决上述限制。通过这种方式，BiSparse-AAS在计算成本上减少了对输入中最相关部分的计算负担，动态调整注意力范围，捕获复杂词汇之间的相互作用，并在长文本序列建模方面展示出了优异的能力。实验结果显示，BiSparse-AAS在抽性摘要和抽象性摘要任务上都优于现有的最佳基准，取得了显著的改进。
### Conclusion
BiSparse-AAS 通过提高效率、可扩展性和长序列建模能力，为实际文本文档摘要提供了统一且实用的解决方案，尤其是在处理大型语料库和长文档时做出的改进，使该方法在各种数据集上都表现出优异的性能，并且为未来的文本摘要提供了新的研究方向。
## 593. `cs.LG` - 基于场景图的预训练基础模型语言到动作长期精准机器人操作 [PDF](https://arxiv.org/pdf/2510.27558), [HTML](https://arxiv.org/abs/2510.27558)
### Authors
Sushil Samuel Dinesh,Shinkyu Park
### Background
该研究提出了一个框架，该框架利用预训练的基础模型进行机器人操作，无需特定领域的训练。框架整合了现成的模型，将基础模型的多模态感知与通用推理模型结合起来，以实现稳健的任务排序。场景图在框架内动态维护，提供空间意识并使环境推理保持一致。
### Innovation
该框架通过将多模态感知与通用推理模型结合，利用基础模型构建机器人操作系统，而无需特定领域的训练。框架使用场景图来提供空间意识和环境推理的一致性。
### Conclusion
该框架通过一系列桌面机器人操作实验进行评估，结果显示其在直接基于现成基础模型构建机器人操作系统方面的潜力巨大。
## 594. `cs.LG` - 广义分布下DDPM的最优收敛分析 [PDF](https://arxiv.org/pdf/2510.27562), [HTML](https://arxiv.org/abs/2510.27562)
### Authors
Yuchen Jiao,Yuchen Zhou,Gen Li
### Background
评分扩散模型在生成高质量目标数据分布样本方面取得了显著的实际成功。在这些模型中，去噪扩散概率模型（DDPM）是使用最广泛的采样方法之一，通过估计评分函数生成样本。尽管在实际应用中表现良好，但关于DDPM（尤其是其收敛性质）的理论理解仍显得有限。
### Innovation
本文为DDPM采样器提供了一种改进的收敛分析，并在一般分布假设下建立了接近最优的收敛速率。引入了一个参数化由常数$L$定义的松弛光滑条件，对于许多实际分布来说$L$很小（例如，高斯混合模型）。证明了当评分估计准确时，DDPM采样器的收敛速率为$?widetilde{O}?left(?frac{d?min?{d,L^2?}}{T^2}?right)$，其中$d$是数据维度，$T$是迭代次数，$?widetilde{O}$隐藏了$T$的多项式对数因子。这一结果在$L < √d$时，大大改善了现有的$d^2/T^2$速率。通过建立匹配的下界，展示了我们对DDPM的收敛分析在广泛的目标分布范围内是紧致的，揭示了DDPM和DDIM在$d$上的相同依赖关系。
### Conclusion
此外，这一结果揭示了DDPM和DDIM共享$d$的相同依赖关系，这引发了为什么DDIM通常在实际应用中看起来更快速的一个有趣问题。
## 595. `cs.LG` - Learned Static Function Data Structures [PDF](https://arxiv.org/pdf/2510.27588), [HTML](https://arxiv.org/abs/2510.27588)
### Authors
Stefan Hermann,Hans-Peter Lehmann,Giorgio Vinciguerra,Stefan Walzer
### Background
该研究任务是构建一个数据结构，用于将静态键集与值相关联，并允许对不属于该集的键进行查询时具有任意输出值。与哈希表相比，这些所谓的静态功能数据结构无需存储键集，因此占据更少的内存。已有多项技术被提出，压缩静态函数可以接近值序列的一阶经验熵。
### Innovation
本文引入了基于学习的静态函数，使用机器学习来捕捉键与值之间的关联。对于每个键，模型会预测一个值的概率分布，从中我们得出一个特定于键的前缀码以紧凑地编码真实值。生成的编码串被存储在经典静态函数数据结构中。这种设计使得基于学习的静态函数能够打破零阶熵的界限，同时仍支持点查询。实验结果显示存储量节省显著：在真实数据上，最多节省了1个数量级的空间；在合成数据上，最多节省了3个数量级的空间。
### Conclusion
本文提出了一种新的基于学习的静态函数数据结构，该结构利用机器学习来提高对键值关联的处理效率，同时保持了高效查询的能力，并通过实验验证了其显著的空间节省效果。
## 596. `cs.LG` - 在基础模型时代通过跨视图代码对齐进行图像哈希 [PDF](https://arxiv.org/pdf/2510.27584), [HTML](https://arxiv.org/abs/2510.27584)
### Authors
Ilyass Moummad,Kawtar Zaher,Hervé Goëau,Alexis Joly
### Background
大规模检索需要同时具备紧凑性和判别性的表示。基础模型提供了强大的视觉和多模态嵌入，但这些高维空间中的最近邻搜索计算成本高昂。哈希提供了一种高效的替代方案，通过使用二进制码进行快速汉明距离搜索，但现有方法往往依赖于复杂的管道、多目标、专为单一学习范式设计，并且训练时间较长。
### Innovation
作者提出了CroVCA（跨视图代码对齐），这是一种简单而统一的原则，用于学习在语义对齐视图中保持一致的二进制代码。单个二元交叉熵损失强制执行对齐，而编码率最大化作为抗塌陷正则化器促进平衡和多样化的代码。此外，设计了HashCoder，这是一种轻量级的MLP哈希网络，带有最终的批量归一化层以强制执行平衡的代码。HashCoder 可以在冻结的嵌入上作为探针头使用，也可以通过LoRA微调高效地调整编码器。
### Conclusion
CroVCA 在多个基准测试中仅用 5 个训练周期就达到了最先进的效果。例如，在单个 GPU 上，无监督哈希在 COCO 上完成不到 2 分钟，有监督哈希在 ImageNet100 上完成约 3 分钟。这些结果突出显示了 CroVCA 的效率、适应性和广泛的应用范围。
## 597. `cs.LG` - 迈向通用视频检索：通过合成多元模态金字塔课程实现视频嵌入泛化 [PDF](https://arxiv.org/pdf/2510.27571), [HTML](https://arxiv.org/abs/2510.27571)
### Authors
Zhuoning Guo,Mingxin Li,Yanzhao Zhang,Dingkun Long,Pengjun Xie,Xiaowen Chu
### Background
当前的视频检索范式存在结构性错位，狭窄的基准测试指标促使数据集和模型训练变得单一，这抑制了对多维度通用能力的需求。缺少诊断性评估会使得保持多维度泛化的指标和要求不足。
### Innovation
该研究提出了一种框架，通过评估、数据和建模的联合设计来打破这一循环。首先，引入了Universal Video Retrieval Benchmark (UVRB)，包含16个数据集，不仅衡量性能，还诊断任务和领域之间的关键能力差距。其次，基于UVRB的诊断结果，生成了1.55万个高质量嵌入对，填补了通用视频检索所需的整个语义空间。最后，设计了模态金字塔，利用多样化数据中的潜在联系对General Video Embedder (GVE)进行训练，实验结果表明GVE在UVRB上实现了最先进的零样本泛化效果。研究还揭示，流行基准未能准确预测泛化能力，并且部分相关检索是一个常见但被忽视的场景。
### Conclusion
我们的联合设计框架提供了一个实用的途径，能够超越当前的有限范围，朝着真正意义上的通用视频检索迈进。
## 598. `cs.LG` - 超密集LEO卫星网络中基于事件驱动的风险感知多Agent分组路由 [PDF](https://arxiv.org/pdf/2510.27506), [HTML](https://arxiv.org/abs/2510.27506)
### Authors
Ke He,Thang X. Vu,Le He,Lisheng Fan,Symeon Chatzinotas,Bjorn Ottersten
### Background
超密集的低地球轨道（LEO）星座在复杂和异步的网络环境中运行，由于其庞大的规模、动态的拓扑结构和显著的延迟。这种独有的复杂性要求一种适应性强的分组路由算法，该算法需要异步操作、风险感知，并且能够在去中心化的情况下平衡多种且往往相互冲突的服务质量（QoS）目标。然而，现有的方法未能满足这一需求，因为它们通常依赖于不切实际的同步决策和/或忽略风险的方法。因此，本文提出了PRIMAL，这是一种基于事件驱动的多Agent路由框架，旨在让每个卫星可以独立于其自身的时间表进行操作，通过原则性的原对偶方法管理最坏情况性能降级的风险。这使得代理能够了解所针对的QoS目标的完整成本分布，并限制尾端风险。通过在拥有1584颗卫星的LEO星座上进行大量的仿真实验，PRIMAL在优化时延和负载分配方面表现出了优势，相较于之前的一个忽略风险的方法，它减少了超过70%的排队延迟，而端到端延迟降低了接近12毫秒。这意味着PRIMAL能够在解决单纯最短路径查找和拥塞避免之间的核心冲突上做出贡献，显示出自主风险感知是实现鲁棒路由的关键。
### Innovation
提出了一个名为PRIMAL的事件驱动型多Agent路由框架，用于超密集LEO卫星网络。PRIMAL能够使每个卫星独立地在其特定的时间表上操作，并通过原对偶方法管理最坏情况下的性能降级风险，从而确保平衡性能和风险。该方法还引入了一种机制，即代理能够学习目标QoS的完整成本分布并控制尾部风险。与现有方法相比，PRIMAL显著提高了延迟优化和负载平衡的效果。
### Conclusion
PRIMAL作为一种新型的异步风险感知多Agent路由算法，在超密集LEO卫星网络中表现出色，能够有效优化延迟并平衡负载分配。相较于之前的设计，该算法能显著减少排队延迟，并在负荷条件下降低接近12毫秒的端到端延迟，凸显自主风险感知对于实现路由器鲁棒性的重要性。
## 599. `cs.LG` - 通过Implication-Realization与Temporal-Gestalt图表示古典音乐作品 [PDF](https://arxiv.org/pdf/2510.27530), [HTML](https://arxiv.org/abs/2510.27530)
### Authors
A. V. Bomediano,R. J. Conanan,L. D. Santuyo,A. Coronel
### Background
音乐理论与计算音乐学中理解音乐结构和认知基础仍然是一个关键挑战。传统方法主要集中在和声和节奏上，而认知模型，如Implication-Realization (I-R) 模型和Temporal Gestalt理论，可以提供对音乐感知与预测结构的洞察。本文将这些模型转化为基于图的计算方法，通过对旋律进行分段并标注I-R模式来实现。这些分段借助动态时间规整和k近邻图进行比较和网络化，从而建模分段间及分段内的关系。每个分段作为图中的一个节点，标注了音阶邻近度和音调反转的预期值，反映了听众对音乐紧张感和解决的理解，揭示了音乐结构与认知信息的关系。通过使用Weisfeiler-Lehman图核，研究结果显示出组内与组间结构的显著差异，多维标度分析也证实了图层面结构相似性与分段层面感知相似性的对应关系。通过Graph2vec嵌入和聚类进一步展现了这种表示形式能够捕捉到超出作曲家身份的风格和结构特性。
### Innovation
本文提出了一种基于图的计算方法，通过将Implication-Realization (I-R) 模型和Temporal Gestalt理论转化为分段标注，利用动态时间规整和k近邻图进行比较，以及通过Weisfeiler-Lehman图核和Graph2vec嵌入进行相似性度量。这种方法不仅编码了音乐结构信息，还体现了认知信息，可以在不同层次上允许对音乐篇章和风格特征的多维理解。
### Conclusion
研究结果表明，基于图的方法为计算音乐分析提供了一个结构化、符合认知的框架，能够通过听众感知的视角，提供对音乐结构和风格更为细腻的理解。这些发现揭示了这些方法在捕捉并再现古典音乐作品中的音乐及其认知过程的表达能力。
## 600. `cs.LG` - 增强软件产品线中的机器学习组件 [PDF](https://arxiv.org/pdf/2510.27640), [HTML](https://arxiv.org/abs/2510.27640)
### Authors
Luz-Viviana Cobaleda,Julián Carvajal,Paola Vallejo,Andrés López,Raúl Mazo
### Background
现代软件系统越来越多地整合机器学习（ML）功能，由于其进步和提升数据驱动决策的能力。然而，这种整合为软件工程带来了显著挑战，特别是在软件产品线（SPLs）中，随着包含ML组件，管理和重用的复杂性增加。尽管已有方法解决了SPL中的变异管理以及孤立系统中的ML组件集成问题，但鲜有方法兼顾这两个领域。特别是对于包含ML组件的SPLs，现有的模型支持管理和变异管理有限。为了弥合这一差距，本文提出了一个结构化的框架，旨在扩展软件产品线工程，促进ML组件的集成。该框架通过系统的变异和重用建模来支持SPLs的设计，具有ML功能的SPLs能够从中受益。该提议部分实现了VariaMos工具.
### Innovation
文章提出了一个结构化的框架，旨在扩展软件产品线工程，促进带有ML组件的SPLs的设计和建模。该框架能够系统地进行变异和重用建模，填补了该领域的空白。此外，该提议部分实现了一个名为VariaMos的工具来支持上述框架的应用和实施。
### Conclusion
本文提出并部分实现了结合了ML组件的SPLs的设计和建模框架，提供了系统的方法来管理和重用这些复杂的组件，并将为未来在此领域的进一步开发奠定基础。
## 601. `cs.LG` - SpecAttn: 推测稀疏注意机制 [PDF](https://arxiv.org/pdf/2510.27641), [HTML](https://arxiv.org/abs/2510.27641)
### Authors
Harsh Shah
### Background
大语言模型（LLMs）在推理过程中由于自注意力机制的复杂度呈二次增长，特别是在上下文长度增加时，面临显著的计算瓶颈。我们通过SpecAttn提出了一种无需训练的创新方法，无缝集成现有的推测解码技术，实现高效稀疏注意力。SpecAttn的关键是利用早期模型在推测解码中已计算的注意权重，识别目标模型的重要令牌，从而消减冗余计算，同时保持输出质量。
### Innovation
SpecAttn采用了三种核心技术：基于KL散度的中间模型与目标模型的层对齐，GPU优化的无排序顶级p值令牌选择算法，以及由这些预测指导的动态键值缓存修剪。通过利用标准推测解码管道中已完成的计算工作，SpecAttn实现了超过75%的关键值缓存访问减少，仅增加了15.29%的困惑度，显著优于现有稀疏注意力方法。
### Conclusion
我们的方法证明，推测执行可以增强为提供近似验证，而不会显著性能下降。
## 602. `cs.LG` - 网络上的贝叶斯优化 [PDF](https://arxiv.org/pdf/2510.27643), [HTML](https://arxiv.org/abs/2510.27643)
### Authors
Wenwen Li,Daniel Sanz-Alonso,Ruiyi Yang
### Background
本文研究在网络作为一个度量图建模的情况下优化问题。研究动机来自于目标函数昂贵且仅作为黑盒子的情况，需开发贝叶斯优化算法来次序更新目标函数的高斯过程代理模型，以此指导查询点的获取。为确保代理模型适应网络的几何特性，采用基于度量图上的随机偏微分方程定义的Whittle-Matérn高斯过程先验模型。研究还涵盖了目标函数光滑程度未知的实用情况，并分析了基于有限元表示Whittle-Matérn先验的情况。
### Innovation
开发了贝叶斯优化算法，这些算法次序更新目标函数的高斯过程代理模型，以指导查询点的获取。利用Whittle-Matérn高斯过程先验模型，针对度量图定义使用随机偏微分方程。该研究不仅为充分光滑的目标函数建立了后悔界限，还分析了目标函数光滑度未知的情况，以及使用有限元表示Whittle-Matérn先验的案例。并提供了在合成度量图和电信网络上的基准目标函数优化和贝叶斯反演的数值结果来验证算法的有效性。
### Conclusion
研究表明该算法在优化合成度量图上的基准目标函数以及通过最大后验估计在电信网络上的贝叶斯反演有效。
## 603. `cs.LG` - 从嘈杂和部分测量中仅在成像逆问题中进行贝叶斯模型选择和失拟测试 [PDF](https://arxiv.org/pdf/2510.27663), [HTML](https://arxiv.org/abs/2510.27663)
### Authors
Tom Sprunck,Marcelo Pereyra,Tobias Liaudat
### Background
现代成像技术依赖于贝叶斯统计模型来解决复杂的图像重建和恢复任务。当无法获得地面真相时，需要客观评估这些模型，重点在于模型选择和失拟诊断。现有的一些无监督模型评估方法由于计算成本高且与通过机器学习模型隐式定义的现代图像先验不兼容，不适应用于计算成像。
### Innovation
本文提出了一种基于贝叶斯交叉验证和随机测量分割技术（数据分裂）的通用无监督模型选择和失拟检测方法。该方法适用于任何贝叶斯成像采样器，包括扩散和即插即用采样器。
### Conclusion
通过不同评分规则和模型失拟类型的实验表明，该方法在计算成本低的情况下实现了优秀的选型和检测精度。
## 604. `cs.LG` - 基于选择少量示例的LLM代码漏洞检测 [PDF](https://arxiv.org/pdf/2510.27675), [HTML](https://arxiv.org/abs/2510.27675)
### Authors
Md Abdul Hannan,Ronghao Ni,Chi Zhang,Limin Jia,Ravi Mangal,Corina S. Pasareanu
### Background
大语言模型（LLMs）已经展示了在许多编码任务中的出色能力，包括摘要、翻译、完成和代码生成。然而，检测代码漏洞仍然是LLMs的一项挑战性任务。一种有效的方法是上下文学习（ICL），在为查询提供少量类似示例及其正确答案的基础上，可以帮助提高LLM生成正确解的能力。然而，正确选择这些少量示例对于提高模型性能至关重要。
### Innovation
本文探索了两种用于代码漏洞检测任务的ICL中选择少量示例的准则。第一种准则考虑了LLM是否在某个样例上犯错，基于样例上LLM的表现可以反映其作为少量示例的有用性。第二种准则基于给定样例与待查询程序的相似性，通过k-最近邻选择少量示例。实验证明了这两种准则的效果以及它们的组合效果。
### Conclusion
通过评估不同准则的效果及其组合，表明两种准则有助于提高LLM在代码漏洞检测任务中的表现，为后续研究提供了有价值的参考。
## 605. `cs.LG` - MolChord: 结构-序列对齐以蛋白质引导的药物设计 [PDF](https://arxiv.org/pdf/2510.27671), [HTML](https://arxiv.org/abs/2510.27671)
### Authors
Wei Zhang,Zekun Guo,Yingce Xia,Peiran Jin,Shufang Xie,Tao Qin,Xiang-Yang Li
### Background
结构导向的药物设计（SBDD），将目标蛋白与候选分子配体映射，是药物发现中的一个基础任务。有效地将蛋白质结构表示与分子表示对齐，并确保生成的药物与药理性质之间的对齐，依然是一个关键挑战。
### Innovation
我们提出了MolChord，该方法结合了两项关键技术：（1）利用NatureLM统一的自回归模型，结合文本、小分子和蛋白质，将其作为分子生成器，同时使用基于扩散的结构编码器，将蛋白质和分子结构与其文本描述和序列表示（如蛋白质的FASTA序列和分子的SMILES表示）对齐；（2）使用直接偏好优化（DPO）来指导分子向所需特性的方向移动，并整合偏好数据，提高对齐过程的准确性。
### Conclusion
在CrossDocked2020数据集上进行的实验表明，我们的方法在关键评估指标上达到了最先进的性能，突显了其作为SBDD实用工具的潜力。
## 606. `cs.LG` - 通过知识感知和多模态预测建模解读虚拟医疗的成功 [PDF](https://arxiv.org/pdf/2306.03833), [HTML](https://arxiv.org/abs/2306.03833)
### Authors
Shuang Geng,Wenli Zhang,Jiaheng Xie,Gemin Liang,Ben Niu,Sudha Ram
### Background
在线医疗咨询改变了患者寻求医疗建议的方式，提供了便利但同时也带来了一系列新的挑战，特别是在确保咨询成功方面。预测在线咨询的成功对于改善患者体验和保持平台竞争力至关重要。然而，由于患者护理旅程的碎片化以及虚拟和传统医疗保健系统的脱节，这种预测非常困难。此外，从在线平台上收集的数据，包括文本对话、互动序列和行为轨迹，往往是稀疏和不完整的。
### Innovation
本研究开发了一种融合多模态数据和动态构建的知识网络的预测建模方法，以捕捉患者、医生和咨询环境之间的潜在关系。通过整合异构信息源并揭示数字互动的演变结构，该模型提高了咨询成功预测的准确性和可解释性。
### Conclusion
研究结果提出了通过数据驱动智能设计结合在线和离线服务的混合医疗生态系统的重要意义。
## 607. `cs.LG` - PETAR: 通过 Aware 视觉语言建模实现 PET 自动报告的局部发现生成 [PDF](https://arxiv.org/pdf/2510.27680), [HTML](https://arxiv.org/abs/2510.27680)
### Authors
Danyal Maqbool,Changhee Lee,Zachary Huemann,Samuel D. Church,Matthew E. Larson,Scott B. Perlman,Tomas A. Romero,Joshua D. Warner,Meghan Lubner,Xin Tie,Jameson Merkow,Junjie Hu,Steve Y. Cho,Tyler J. Bradshaw
### Background
近期视觉语言模型(VLMs)的发展使多模态推理变得非常出色，但大多数医疗应用仍局限于二维成像。本文通过将 VLMs 扩展到 3D 正电子发射断层扫描和计算机断层扫描(PET/CT)领域，旨在解决这一限制。PET/CT 特别适用于具有大量体积数据、小而分散的病灶以及冗长的放射科报告的场景。研究人员创建了一个大规模数据集，包含超过 11,000 个病灶级描述与超过 5,000 次 PET/CT 成像的 3D 分割，以数据驱动方式验证方法的有效性。
### Innovation
研究人员提出了一种名为 PETAR-4B 的 3D 掩码感知视觉语言模型，它可以集成 PET、CT 和病灶轮廓，用于生成空间指导报告。PETAR 特别关注远处上下文推理与细致的病灶意识结合，能够产生临床上连贯且局部的发现。研究包括自动化和人工评估，证明 PETAR 显著提升了 PET/CT 报告的质量，促进了 3D 医学视觉语言理解的进步
### Conclusion
通过 PETAR-4B 可以实现 3D PET/CT 图像中局部病灶的准确报告生成，显著提高报告质量，推动了 3D 医学视觉语言理解的发展。
## 608. `cs.LG` - 在随机和对抗环境中介于随机加速在线凸优化 [PDF](https://arxiv.org/pdf/2303.03272), [HTML](https://arxiv.org/abs/2303.03272)
### Authors
Sarah Sachs,Hedi Hadiji,Tim van Erven,Cristobal Guzman
### Background
在线学习中，通常考虑随机和完全对抗的数据设置。然而，许多优化任务既不是独立同分布(i.i.d.)的，也不是完全对抗的，因此需要在随机和完全对抗这两种极端情况之间建立更好的理论理解。本文在不同介于随机与完全对抗环境之间的情况下，建立了在线凸优化的新遗憾界.
### Innovation
本文通过对预期损失的平滑性进行利用，将遗憾界中的最大梯度长度依赖替换为梯度方差依赖，这是之前仅对线性损失有效的方法。此外，通过允许例如对抗污染的轮次，这些边界放宽了i.i.d.假设，这种做法已在相关的专家和多臂老虎机问题中得到研究。在完全i.i.d.情况下，本文的遗憾界与随机加速结果中的预期速率一致，通过在线到批处理的转换还可以恢复最优的随机加速速率。在完全对抗的情况下，遗憾界优雅地恶化为匹配极小化遗憾的界。此外，还提供了关于损失梯度的随机波动和对抗波动在所有中间环境中的遗憾上界紧致性证明.
### Conclusion
本文建立了在线凸优化的新遗憾界，这些界在一定程度上介于随机和完全对抗环境中，并且在完全i.i.d.和完全对抗的情况下分别提供了匹配的最优速率和极小化遗憾界。
## 609. `cs.LG` - 混合分散优化：利用一阶和零阶优化器实现更快收敛 [PDF](https://arxiv.org/pdf/2210.07703), [HTML](https://arxiv.org/abs/2210.07703)
### Authors
Matin Ansaripour,Shayan Talaei,Giorgi Nadiradze,Dan Alistarh
### Background
分布式优化是加速机器学习训练的标准方法，大多数研究集中在分布式的一阶梯度方法。然而，在一些场景下，部分计算能力受限的节点可能无法进行一阶梯度优化，但仍可以参与联合优化任务。本文探讨了混合零阶和一阶优化能力的分布式系统中如何共同解决优化问题。研究表明，在合理参数设置下，这样的系统不仅可以承受噪声较大的零阶优化器，还可以从集成这些优化器中获益，而不是忽略它们提供的信息。文章的核心在于对包含噪声且可能带偏的梯度估计器的分布式优化的新分析，这一点可能具有独立的研究价值。该结果适用于凸函数和非凸函数目标。实验结果显示，混合一阶和零阶优化可以实现在训练深度神经网络时的快速收敛和实用性。
### Innovation
研究混合零阶和一阶优化能力的分布式系统，提出了一种新的关于噪声和可能偏斜的梯度估计器的分布式优化分析方法，显示了在合理参数设置下，系统可以集成零阶优化器并从其信息中获益，而不是忽略它们，该研究适用于凸函数和非凸函数的目标。
### Conclusion
研究表明，混合分布式一阶和零阶优化方法不仅能够处理噪声较大的零阶组件，甚至可以从这些组件中获益而非忽视它们的信息。该方法适用于凸和非凸目标函数，并且已在标准优化任务上进行了验证，证明了混合一阶零阶优化在训练深度神经网络时的实用性。
## 610. `cs.LG` - 连续自回归语言模型 [PDF](https://arxiv.org/pdf/2510.27688), [HTML](https://arxiv.org/abs/2510.27688)
### Authors
Chenze Shao,Darren Li,Fandong Meng,Jie Zhou
### Background
大语言模型（LLMs）的效率受到其按顺序逐个生成词元的过程限制。本文指出，克服这一瓶颈需要重新思考LLM的扩展方式，即增加每步生成过程中的语义带宽。传统的自回归语言模型依赖逐个词元的预测，而新的方法是连续的向量预测，这需要一个全新的体系结构来替代传统的基于词元的预测方法。通过使用高保真的自编码器将一串K个词元压缩为一个连续的向量，从而将语言表示为连续向量的序列，减少了生成步骤的数量。
### Innovation
提出了连续自回归语言模型（CALM），该模型从离散的下一个词预测转变为连续的下一个向量预测。CALM使用高保真的自编码器将一段K个词元压缩成一个连续向量，并且可以高精度地重建出原始的词元。这使得语言模型能够在连续的向量空间中建模，可以通过减少生成步骤的数量来提高效率，同时发展了一套完整的无需似然的框架，以保证在连续空间中的鲁棒训练、评估和可控采样。实验结果表明，CALM在较低的计算成本下实现了接近离散基线模型的性能。未来将连续向量预测视为一种强大且可扩展的途径，以构建超高效的语言模型。
### Conclusion
这些研究结果确立了连续向量预测作为构建超高效语言模型的强大且可扩展途径。通过代码和项目链接提供了详细的实现细节和实验结果，展示了CALM模型在性能和计算效率方面的显著提高。
## 611. `cs.LG` - X射线暗场成像显著提高基于深度学习的预临床模型中合成早期肺癌肿瘤检测 [PDF](https://arxiv.org/pdf/2510.27679), [HTML](https://arxiv.org/abs/2510.27679)
### Authors
Joyoni Dey,Hunter C. Meyer,Murtuza S. Taqi
### Background
低剂量计算机断层扫描（LDCT）是肺癌筛查的当前标准，但其普及和可及性仍然有限。许多地区缺乏LDCT基础设施，即便进行了筛选，早期肺癌检测也经常会产生假阳性结果。例如，在国家肺筛查试验（NLST）中，LDCT的灵敏度为93.8%，假阳性率高达26.6%。这项研究旨在探讨X射线暗场成像（DFI）放射照相技术在检测早期肺癌中的作用，该技术对肺泡微结构的小角度散射敏感，且对器官阴影的依赖性较小。通过结合深度学习分割技术，研究团队希望改进早期肺癌的检测效率
### Innovation
使用低剂量计算机断层扫描和X射线暗场成像放射照相图像，生成具有不规则边界和物理肺对比度一致的合成肿瘤。研究表明，仅使用DFI技术的模型实现了83.7%的真正阳性检测率，高于只使用衰减成像技术的51%，且同时保持相当的特异性（90.5% 对 92.9%）。结合衰减成像和DFI输入，模型的灵敏度为79.6%，特异性为97.6%。
### Conclusion
X射线暗场成像显著提高了预临床模型中合成早期肺癌肿瘤的可检测性，显示出作为LDCT不可用时的普及、低成本、低剂量筛查替代方案的潜力
## 612. `cs.LG` - 重新评估优化理论分析方法在深度学习中的应用 [PDF](https://arxiv.org/pdf/2407.01825), [HTML](https://arxiv.org/abs/2407.01825)
### Authors
Hoang Tran,Qinzi Zhang,Ashok Cutkosky
### Background
在深度学习中，我们对优化算法的理解与其实际性能之间存在显著的差距。理论发展大部分集中于在各种假设下证明收敛保证，而这些假设通常结合了对实践的直观理解以及分析的便利性。本文探讨了标准优化分析能力，通过开发新的实证指标来比较实际优化行为和理论预测行为。
### Innovation
本文的关键创新在于直接测量标准优化分析解释现代算法的能力，并引入了一种新的方法，通过实证指标将实际优化行为与理论预测行为进行比较。特别的是，本文发现基于光滑性的分析在大多数情况下在实践中都无法成立，但通常在凸优化分析中使用的关键恒等式在目标函数的全局非凸性情况下仍然实际有效，从而提高了对优化算法的理解。
### Conclusion
本文结果表明，基于光滑性的分析方法在大多数情况下无法充分解释现代优化算法的实际表现，而许多传统凸优化分析中的关键恒等式在实际问题中仍然有效，强调了在现代深度学习优化中对这些恒等式的关注。
## 613. `cs.LG` - 扩展实用概率电路的系统视角 [PDF](https://arxiv.org/pdf/2406.00766), [HTML](https://arxiv.org/abs/2406.00766)
### Authors
Anji Liu,Kareem Ahmed,Guy Van den Broeck
### Background
概率电路（PCs）是一种用于可计算深度生成模型的一般框架，支持在其学习分布上的精确和高效概率推理。虽然最近的建模和训练进步使PC能够在复杂的实际任务中得到应用，但现有的PC实现效率低下，阻碍了其进一步的扩展。
### Innovation
本文提出了PyJuice，一种通用的GPU实施设计，改进了先前的工作。尤其是，PyJuice相比现有系统（包括近期的）在大规模PC训练方面的速度提高了1-2个数量级，同时消耗的GPU内存减少了2-5倍，这使得能够训练更大的模型。PyJuice的核心是一个编译过程，该过程将PC转换成便于高效块并行化的紧凑表示，从而显著减少了I/O操作并充分利用现代GPU中的张量核。
### Conclusion
实验结果表明，PyJuice可以优化在图像（如ImageNet32）和语言（如WikiText，CommonGen）数据集上训练的最先进的PC。此外，他们还通过比较现有电路结构来建立新的基准，以大型模型和更多的训练周期为目标，希望激励未来的研究。源代码可在以下链接获得：this https URL
## 614. `cs.LG` - 连续时间随机梯度下降的收敛性及其在深度神经网络中的应用 [PDF](https://arxiv.org/pdf/2409.07401), [HTML](https://arxiv.org/abs/2409.07401)
### Authors
Gabor Lugosi,Eulalia Nualart
### Background
本文研究了用于最小化学习问题中总体期望损失的随机梯度下降过程的连续时间逼近。背景基于以往关于梯度下降的相关研究，特别是在非随机梯度下降方面的研究，如Chatterjee (2022)的研究成果。研究旨在扩展对于随机梯度下降过程的收敛性结果，并将其应用于过参数化神经网络的训练过程。
### Innovation
研究的主要成果是建立了一个泛化的充分条件来证明连续时间随机梯度下降方法的收敛性，这一成果扩展了Chatterjee (2022) 关于非随机梯度下降的结果。此外，该研究展示了其主要结果如何适用于过参数化神经网络的训练情况。
### Conclusion
本文通过对其细致的理论分析，证明了连续时间随机梯度下降方法的收敛性，为探索高效的机器学习算法提供了新的思路，并且该结论特别适用于过参数化神经网络场景下的训练优化。
## 615. `cs.LG` - Swing-by Dynamics in Concept Learning and Compositional Generalization [PDF](https://arxiv.org/pdf/2410.08309), [HTML](https://arxiv.org/abs/2410.08309)
### Authors
Yongyi Yang,Core Francisco Park,Ekdeep Singh Lubana,Maya Okawa,Wei Hu,Hidenori Tanaka
### Background
先前研究表明，基于文本的内容引导扩散模型能够学习和操控数据生成过程中最基本的概念，从而能够推广到全新的、未见过的组合。这些研究不仅在性能上进行评估，还详细探讨了学习动态的丰富现象学，展示了模型按照数据生成过程的层次结构逐步泛化。此外，数据中的概念中心结构显著影响了模型学习操控概念的速度。本研究旨在从理论层面更深入地探讨这些实证结果。
### Innovation
本文提出了一个结构性身份映射（SIM）任务，用于理论分析先前研究中关于概念学习和组合泛化的发现。通过对SIM任务训练的神经网络的学习动态进行数学分析，表明尽管SIM任务简单，但它捕捉并帮助解释了先前研究中关于扩散模型中概念学习能力和组合泛化的关键观察结果。本研究还提供了新的见解，例如在训练早期阶段测试损失的非单调学习动态机制。通过训练基于文本的扩散模型，将简化框架与复杂的生成模型相结合，验证了新的预测。
### Conclusion
本研究建立了SIM任务作为现代生成模型中概念学习动态的有意义的理论抽象。
## 616. `cs.LG` - AERO: 受熵导向框架的私密大语言模型推理 [PDF](https://arxiv.org/pdf/2410.13060), [HTML](https://arxiv.org/abs/2410.13060)
### Authors
Nandan Kumar Jha,Brandon Reagen
### Background
隐私保护计算允许语言模型直接在加密数据上进行推理，但面临着延迟和通信开销过大的问题，主要由于非线性函数的存在。去除非线性会导致两种失败模式：深层网络的熵坍塌，导致训练不稳定；早期网络的熵过载，导致注意力头利用率不足。
### Innovation
提出AERO，一种熵导向框架，旨在从Transformer架构中策略性地消除昂贵的非线性操作，通过头部层面的自适应校准和可学习的权重，使每个头部能够调整其熵水平，同时惩罚极端熵值并通过容差带促进功能多样性。
### Conclusion
实验证明，AERO可以在不牺牲性能的情况下节省3.4倍的通信和1.4倍的延迟。
## 617. `cs.LG` - 代表性的社会选择：从学习理论到AI对齐 [PDF](https://arxiv.org/pdf/2410.23953), [HTML](https://arxiv.org/abs/2410.23953)
### Authors
Tianyi Qiu
### Background
社会选择理论研究如何在整个人群中聚集偏好，并在人类代理的机制设计和语言模型的民主对齐中应用。在大规模的议题和个人信息中，难以直接考虑所有偏好。这些场景在现实世界中普遍存在，如陪审团审判、立法、公司治理以及最近的语言模型对齐。在代表性的社会选择中，通过基于有限的个体议题样本来代表人群，并据此做出社会选择决定。
### Innovation
通过将代表性的社会选择问题形式化为统计学习问题，并使用机器学习理论证明社会选择机制的泛化性质来证明其创新性。此外，提出了代表性的社会选择公理，并使用新的组合分析工具证明了类似于Arrow不可能性定理的结果。这标志着社会选择、学习理论和AI对齐研究之间的研究方向的新探索。
### Conclusion
该框架提出了代表性的社会选择方法，对社会选择、学习理论和AI对齐的研究进行了交叉研究，为该领域的进一步研究开辟了新的方向。
## 618. `cs.LG` - 时间序列预测与分类中的时空图神经网络模型系统的文献综述 [PDF](https://arxiv.org/pdf/2410.22377), [HTML](https://arxiv.org/abs/2410.22377)
### Authors
Flavio Corradini,Flavio Gerosa,Marco Gori,Carlo Lucheroni,Marco Piangerelli,Martina Zannotti
### Background
近年来，时空图神经网络（GNNs）在时间序列分析领域引起了广泛关注，这得益于它们能够同时捕捉变量之间的依赖性和不同时间点之间的依赖关系。本综述旨在提供时空GNN模型及其在时间序列分类和预测中的应用方法和应用场景的全面概述。通过对数据进行检索并选择366篇论文进行详细研究，旨在为读者提供拟议模型的全面回顾、与相关源代码的链接、可用数据集、基准模型和拟合结果的信息，以帮助研究人员进行研究。
### Innovation
这是首个和最广泛的系统性文献综述，详细比较了应用于不同领域当前时空GNN模型的结果。综述还讨论了时空GNN应用面临的当前限制和挑战，包括可比性、重现性、解释性差、信息容量不足和可扩展性问题。此外，还提供了一个GitHub存储库，增加了额外的交互工具，以进一步探索展示的研究成果。
### Conclusion
本综述为时间序列预测与分类中的时空GNN研究提供了全面的见解，并识别了未来研究的潜在挑战。
## 619. `cs.LG` - DeepOSets: 非自回归的在上下文学习具有置换不变性归纳偏置 [PDF](https://arxiv.org/pdf/2410.09298), [HTML](https://arxiv.org/abs/2410.09298)
### Authors
Shao-Ting Chiu,Junyuan Hong,Ulisses Braga-Neto
### Background
在计算模型中，尤其是在大型语言模型中，一些模型展示了从用户提供的示例中进行学习的能力，而无需更新模型参数，这被称为上下文学习（ICL）。长期以来，人们普遍认为这种能力源于自动回归变换器中的注意机制。然而，作者在本研究中，利用样式化的回归学习任务，展示了在具有硬编码的置换不变性归纳偏置的非自动回归神经网络架构中也可以出现ICL。研究者提出的新型架构DeepOSets结合了DeepSets架构的集学习属性和Deep Operator Networks（DeepONets）的操作学习能力。
### Innovation
研究者提出了一个名为DeepOSets的新架构，它结合了DeepSets和DeepONets的特点，并硬编码了置换不变性的归纳偏置以实现ICL。此外，研究者证明了DeepOSets是该类操作的通用逼近器，提供了置换不变性的回归学习操作的表示定理。在高维度条件下，通过使用Set Transformer替换DeepSets层，展示了在学习线性、多项式和浅神经网络回归时的准确性和速度，验证了模型的优越性。
### Conclusion
研究结果表明，DeepOSets比基于Transformer的相似模型在参数数量减少一数量级的情况下，能够提供准确且快速的结果。这表明，即使不依赖于自回归模型，模型仍然可以具备ICL能力，这对于处理高维度数据具有重要意义。
## 620. `cs.LG` - Transformer作为一种隐含状态估计器：在动力系统中的上下文学习 [PDF](https://arxiv.org/pdf/2410.16546), [HTML](https://arxiv.org/abs/2410.16546)
### Authors
Usman Akram,Haris Vikalo
### Background
从有噪声的过去输出预测动力系统的动态行为是一个在工程和技术领域广泛遇到的经典问题。对于具有高斯输入的线性系统，卡尔曼滤波器（最优的线性最小均方误差状态轨迹估计器）在贝叶斯意义上是最佳的。但对于非线性系统，通常采用诸如扩展卡尔曼滤波器(EKF)或粒子滤波(PF)之类的次优启发式方法。本研究探讨了在上下文学习(Conditional Learning)设置中使用变压器来隐含地推断隐藏状态，从而预测广泛的动力系统输出的方法。这种方法在测试阶段无需梯度更新，且不需要显式了解系统模型。
### Innovation
研究展示了变压器在上下文学习设置中，能够隐含推断隐藏状态以预测不同类型的动态系统输出。特别地，当给定一小段过去的输入-输出对时，冻结的变压器能够准确预测当前输出。其预测在高斯线性系统中近似卡尔曼滤波器的效果，在非线性系统中的表现接近外推卡尔曼滤波器（EKF）和粒子滤波（PF）。此外，当关键参数（如状态转换矩阵）缺失时，预测准确度平稳下降，展示了其鲁棒性和隐含参数推断能力。研究结果证明了变压器在动力系统中进行输出预测的灵活性和非参数化方法，基于隐含的潜伏状态估计。
### Conclusion
本研究提出，使用变压器进行上下文学习提供了一种灵活的、非参数化替代方案，用于动力系统的输出预测，这一方案基于隐含的潜伏状态估计，显示了其鲁棒性和参数推断能力。
## 621. `cs.LG` - 模型反转攻击：方法与对策综述 [PDF](https://arxiv.org/pdf/2411.10023), [HTML](https://arxiv.org/abs/2411.10023)
### Authors
Zhanke Zhou,Jianing Zhu,Fengfei Yu,Xuan Li,Xiong Peng,Tongliang Liu,Bo Han
### Background
深度神经网络的成功促使了从欧几里得数据到非欧几里得数据的研究和应用。然而，随着这些网络依赖于处理私有数据，越来越多地关注隐私泄露的问题。近期，一种新的隐私攻击--模型反转攻击（MIAs），旨在通过滥用对训练好的模型的访问来提取训练数据中的敏感特征。这些攻击在图像、文本和图等各个领域中证明了其有效性，凸显了神经网络的脆弱性，并引起了研究社区对数据隐私泄漏风险的关注。尽管MIAs的重要性，目前缺乏系统性的研究，提供了全面的概述和深入的见解，横跨不同领域。本综述旨在总结最新的MIAs攻击方法和防御手段，强调它们的贡献和局限性，基础建模原理，优化挑战以及未来方向。
### Innovation
本综述首次系统地总结了最新的MIAs攻击方法和防御手段，强调了它们的贡献、局限性、基础建模原理、优化挑战，并指出了未来的研究方向。本综述填补了文献中的空白，促进了该关键领域的未来研究。同时，还维护了一个数据存储库，以跟踪相关的研究信息：this https URL
### Conclusion
本综述旨在提供一个全面的MIAs方法和对策的概述，并强调了它们的研究贡献和局限性。此外，通过总结最新的研究成果，本综述更好地理解和应对MIAs攻击和防御方法，从而增加在神经网络中的数据保护措施。
## 622. `cs.LG` - 在使用基于树的模型处理不平衡数据时面临的挑战：流行率估计系统地依赖于超参数并且可以被高估 [PDF](https://arxiv.org/pdf/2412.16209), [HTML](https://arxiv.org/abs/2412.16209)
### Authors
Nathan Phelps,Daniel J. Lizotte,Douglas G. Woolford
### Background
在使用机器学习进行不平衡的二分类问题时，通常会通过对多数类进行下采样来创建一个（更）平衡的训练数据集。然而，这种方法会使得模型预测产生偏差，因为模型学习的数据生成过程与新数据不同。一种解决偏差的方法是通过采样率对结果的预测进行解析映射。研究发现，对于随机森林进行这种校准会产生负面后果，包括流行率估计取决于每次分裂时考虑的特征数量以及所使用的采样率。通过对后者的研究，研究者揭示了一个令人惊讶的事实：与广泛认为的决策树偏向多数类相反，它们实际上可以偏向少数类。
### Innovation
介绍了通过解析映射调整机器学习模型预测偏差的方法，并揭示了流行率估计依赖于决策树模型的超参数。特别是，发现决策树模型可以偏向少数类，与常见认识相反。
### Conclusion
研究指出了处理不平衡数据时基于树的模型的挑战，流行率估计系统地依赖于超参数，并且可以被高估。同时指出了决策树模型可能偏向少数类而非多数类的事实。
## 623. `cs.LG` - 训练一个普遍好奇的智能体 [PDF](https://arxiv.org/pdf/2502.17543), [HTML](https://arxiv.org/abs/2502.17543)
### Authors
Fahim Tajwar,Yiding Jiang,Abitha Thankaraj,Sumaita Sadia Rahman,J Zico Kolter,Jeff Schneider,Ruslan Salakhutdinov
### Background
高效探索对于智能系统与其环境互动至关重要，但现有的语言模型在需要策略性信息收集的场景中往往表现不佳。Paprika是一种微调方法，旨在使语言模型能够发展出不受特定环境限制的一般决策能力。通过训练基于不同需要多样策略的合成互动数据，Paprika教会模型根据环境反馈在新任务中探索和调整其行为，而无需更多梯度更新。实验结果显示，使用Paprika微调的语言模型可以有效地将学到的决策能力转移到完全未见过的任务中，而无需额外训练。这与传统的训练方法相比，我们的主要瓶颈在于采样有用的互动数据而不是模型更新。为了提高采样效率，我们提出了一种 curriculum学习策略，优先采样具有高学习潜力的任务的轨迹。
### Innovation
Paprika 方法使得语言模型能够发展出不受特定环境限制的一般决策能力，通过训练基于不同任务的不同策略的合成互动数据，微调后的语言模型可以有效地将学到的决策能力转移到全新的未知任务中。此外，提出了 curriculum 学习策略以提高训练效率，优先采样学习潜力高的任务的轨迹。
### Conclusion
实验结果表明，这种方法提供了一条有望实现能够自主解决需要与外部世界进行互动的新颖序列决策问题的AI系统的发展路径。
## 624. `cs.LG` - 使用线性结构化f-散度正则化的鲁棒离线强化学习 [PDF](https://arxiv.org/pdf/2411.18612), [HTML](https://arxiv.org/abs/2411.18612)
### Authors
Cheng Tang,Zhishuai Liu,Pan Xu
### Background
现有的强化学习方法大多使用无结构的正则化，这在不现实的转移过程中可能导致保守的政策。本文聚焦于离线强化学习，即代理从预先收集的数据集中学习策略，且环境为名义环境。面对系统动态转移发生偏移的情况，为学习到更加鲁棒的策略，该研究提出了一个名为$d$-矩形线性Robust Regularized Markov Decision Process ($d$-RRMDP) 的框架，引入了转移核和正则化中的潜在结构，还发展了Robust Regularized Pessimistic Value Iteration (R2PVI) 算法，用来在带有基于转移核的$f$-散度正则化项的$d$-RRMDPs中学习鲁棒策略。
### Innovation
该研究提出了一种基于线性结构化$f$-散度正则化的方法，以提高鲁棒性，改进了传统的无结构正则化，保证了在不现实的转移过程中的策略仍然具有实用性。开发出的R2PVI算法通过线性函数近似实现鲁棒策略学习，并给出了关于R2PVI策略子最优性的实例依赖上界，证实该算法的优越性。进一步，通过信息论的下界验证了算法的近最优性能。
### Conclusion
研究表明，R2PVI学习的策略不仅具有较高的鲁棒性，还显示出了比基线方法更优的计算效率。该研究提供的算法和理论分析为离线强化学习下的鲁棒策略学习提供了一种有效解法。
## 625. `cs.LG` - 资源适应性增量翻倍算法在高性能计算系统中对大规模数据集进行超参数优化 [PDF](https://arxiv.org/pdf/2412.02729), [HTML](https://arxiv.org/abs/2412.02729)
### Authors
Marcel Aach,Rakesh Sarma,Helmut Neukirchen,Morris Riedel,Andreas Lintermann
### Background
在高性能计算（HPC）系统中，可以并行评估多个超参数配置以加速超参数优化（HPO）过程。当前的先进HPO方法采用基于多臂老虎机的策略，并基于逐步缩减法，最终性能基于低于完全训练的度量估计，更有前途的组合会随着时间获得更多的资源。一般情况下，将迭代次数作为资源，使更有前途的组合训练时间更长。另一种选择是使用工作节点数量作为资源，并直接通过数据并行训练将更多工作节点分配给更有前途的配置。
### Innovation
本文提出了一种新的资源适应性增量翻倍算法（RASDA），结合了资源适应性增量翻倍方案与简单的异步增量缩减算法（ASHA）。这种方法在现代HPC系统中已通过高达1024个图形处理器（GPUs）进行了可扩展性验证。它应用于不同类型的人工神经网络（NN）并使用来自计算机视觉（CV）、计算流体动力学（CFD）和增材制造（AM）领域的大型数据集进行训练，通常只能进行一次完整的训练。实验证明，RASDA在运行时间方面优于ASHA最多1.9倍，并且通过RASDA这种隐式的批次大小调度，最终ASHA模型的解决方案质量通常保持不变或被超越。首次在文献中将系统HPO应用于千兆字节规模的科学数据集，从而在大规模科学数据上高效优化复杂模型。
### Conclusion
RASDA在文献中首次应用于千兆字节规模的科学数据集的系统HPO，实现在大规模科学数据上的复杂模型优化。RASDA的实现可以在以下链接找到：[提供的链接]。
## 626. `cs.LG` - 基准测试超低功耗μNPUs [PDF](https://arxiv.org/pdf/2503.22567), [HTML](https://arxiv.org/abs/2503.22567)
### Authors
Josh Millar,Yushan Huang,Sarab Sethi,Hamed Haddadi,Anil Madhavapeddy
### Background
在设备端进行神经网络（NN）推理能提供可预测的延迟、更好的隐私和可靠性以及较低的操作成本，相对于基于云的推理更加优越。这激发了微控制器规模的NN加速器（$?mu$NPUs）的发展，这些设备特别设计用于超低功耗应用。
### Innovation
研究人员开发了第一个针对多个商用$?mu$NPU平台的比较评估，并开发了一个开源的模型编译管道，支持跨不同微控制器硬件的量化模型的基准测试一致性。这项工作揭示了实际表现与硬件规格之间的差异，包括某些$?mu$NPUs在模型复杂度增加时显示出意外的性能缩放行为。
### Conclusion
这项研究为$?mu$NPU平台的持续评估提供了基础，同时也为硬件和软件开发人员提供了在这一快速发展的领域的实用见解。
## 627. `cs.LG` - 快速针对稀疏攻击的对抗训练需要损失平滑 [PDF](https://arxiv.org/pdf/2502.21041), [HTML](https://arxiv.org/abs/2502.21041)
### Authors
Xuyang Zhong,Yixiao Huang,Chen Liu
### Background
本文研究了稀疏对抗扰动（由$l_0$范数限制）下的快速对抗训练。分析了一步攻击方法在$l_0$约束扰动下的性能下降和灾难性过拟合（CO）问题，指出了一步攻击方法在$l_0$对抗训练中的最优点位不理想是造成CO的原因。理论和实证分析表明，$l_0$对抗训练的损失景观更为崎岖，并且这种崎岖会加剧CO现象。
### Innovation
提出了Fast-LS-$l_0$方法，结合了软标签和折中损失函数来平滑对抗损失景观，解决了上述问题，使方法能够克服灾难性过拟合，实现当前最先进的性能，并缩小了一步和多步对抗训练在对抗稀疏攻击时的性能差距。
### Conclusion
通过Fast-LS-$l_0$方法，可以有效解决$l_0$对抗训练中存在的性能下降和灾难性过拟合问题，实现更好的对抗训练效果，并且能够有效地应对一维攻击。
## 628. `cs.LG` - DualOptim: 使用双重优化器增强机器遗忘的有效性和稳定性 [PDF](https://arxiv.org/pdf/2504.15827), [HTML](https://arxiv.org/abs/2504.15827)
### Authors
Xuyang Zhong,Haochen Luo,Chen Liu
### Background
现有的机器遗忘(MU)方法对超参数非常敏感，需要精细调整，限制了其实用部署。本工作中，我们首先通过实验证明现有流行MU方法在不同场景下的表现不稳定且不尽如人意。
### Innovation
我们提出了双重优化器(DualOptim)，它包含自适应学习率和解耦动量因素，通过实证和理论证据证明了其在有效和稳定遗忘方面的作用。DualOptim 在不同的任务中显示出显著提升MU效果和稳定性，使它成为现有MU算法的一个通用增强方法。
### Conclusion
通过广泛的实验，我们展示了DualOptim在图像分类、图像生成任务以及大型语言模型中的广泛应用，证明了其在提高MU有效性和稳定性方面的能力。
## 629. `cs.LG` - 拜占庭鲁棒分布式多任务表示学习 [PDF](https://arxiv.org/pdf/2503.19209), [HTML](https://arxiv.org/abs/2503.19209)
### Authors
Tuan Le,Shana Moothedath
### Background
在异构联邦学习环境中，客户端可能包含故障或恶意代理，这对于学习个性化模型提出了挑战。当前的联邦学习方法通常不完全抵抗这些代理所带来的影响，尤其是当存在拜占庭行为时，这可能破坏整个学习过程的稳定性与准确性。本文旨在提出一种能够在面对这些挑战时保持鲁棒性的方法，特别是设计了一个称为BR-MTRL的拜占庭鲁棒多任务表示学习框架，该框架利用共享神经网络模型的表示学习机制，允许客户端共享固定层，并通过客户端特定的最终层实现个性化。
### Innovation
本文提出BR-MTRL框架，采用了一种交替梯度下降策略，其中每个客户端优化其本地模型，更新其最终层，并将共享表示的估计发送到中央服务器进行聚合。为了应对拜占庭代理，作者使用了Geometric Median和Krum两种稳健的聚合方法，确保了在存在故障或恶意代理的情况下仍能保持模型的学习性能和鲁棒性。此外，该方法不仅适用于已知客户端的数据学习，还能有效地转移到新客户端，即使该新客户端的数据量有限且存在拜占庭对手的情况。
### Conclusion
本文通过在亚马逊云服务平台上构建的分布式测试环境实现了提议算法，并与现有基准算法进行了性能对比，实验结果表明所提出的方法在现实世界的数据集如CIFAR-10和FEMNIST上具有有效性和稳健性，并能适应新的未见过的客户端，即使存在拜占庭对手。
## 630. `cs.LG` - RaanA: 一种快速、灵活且数据高效的后训练量化算法 [PDF](https://arxiv.org/pdf/2504.03717), [HTML](https://arxiv.org/abs/2504.03717)
### Authors
Yongyi Yang,Jianyang Gao,Wei Hu
### Background
后训练量化（PTQ）已成为提高大型语言模型（LLM）推理效率的广泛应用技术。然而，现有的PTQ方法通常存在重大限制，如对大量校准数据的需求和目标位数选择上的灵活性不足。
### Innovation
本文提出了一种名为RaanA的统一PTQ框架，通过引入两个新颖组件来克服这些挑战：1) RaBitQ-H，一种为快速、准确和高效量化设计的随机化向量量化方法的变体；2) AllocateBits，一种基于量化敏感度最优分配位宽的算法。RaanA能够以与最先进的量化方法相当的性能，同时具备极高的速度，最小化了校准数据需求，并允许灵活的位分配。广泛的实验展示了RaanA在效率和准确性之间取得平衡的能力。相关代码已公开发布。
### Conclusion
实验结果证明RaanA能够在效率和准确性之间取得良好的平衡，同时兼具速度快、数据需求少和灵活的位分配能力。
## 631. `cs.LG` - SageAttention3：针对推理的微缩FP4注意机制及8位训练探索 [PDF](https://arxiv.org/pdf/2505.11594), [HTML](https://arxiv.org/abs/2505.11594)
### Authors
Jintao Zhang,Jia Wei,Pengle Zhang,Xiaoming Xu,Haofeng Huang,Haoxu Wang,Kai Jiang,Jun Zhu,Jianfei Chen
### Background
由于注意力机制的时间复杂度为二次方，其效率显得尤为重要。现有低比特注意力机制如FlashAttention3和SageAttention主要关注推理任务而不是训练任务，这在训练大型模型时显得不够有效。
### Innovation
作者通过两个关键贡献提升了注意力机制的效率：首先利用Blackwell GPU上的新型FP4张量核心加速计算，相比最快的FlashAttention，RTX5090的推理速度提高5倍；其次，设计了适用于前向和反向传播的8位注意力机制，虽然在微调任务上的表现无损，但在预训练阶段收敛速度较慢。
### Conclusion
该研究通过微缩FP4注意力机制提升推理效率，并初步展示了8位注意力机制在训练中的应用前景。
## 632. `cs.LG` - Landscape of Thoughts: 反思景观：大型语言模型推理过程的可视化 [PDF](https://arxiv.org/pdf/2503.22165), [HTML](https://arxiv.org/abs/2503.22165)
### Authors
Zhanke Zhou,Zhaocheng Zhu,Xuan Li,Mikhail Galkin,Xiao Feng,Sanmi Koyejo,Jian Tang,Bo Han
### Background
大型语言模型（LLMs）在许多应用场景中依赖于其步步为营的推理能力。然而，这些模型的推理行为尚未得到充分的理解，这给研究、开发和安全性带来了挑战。为了解决这一问题，本文介绍了‘反思景观’（LoT），这是一个用于检查任何多选择数据集上特定推理方法的推理轨迹的可视化工具。该工具将文本状态沿轨迹表示为量化其与答案选项距离的数值特征，并使用t-SNE在二维图表中进行可视化。反思景观的质量和定量分析有效地区分了强弱模型、正确和错误的答案，以及不同类型的推理任务。此外，它还揭示了某些不良的推理模式，例如低一致性和高不确定性。用户还可以根据观察的属性调整LoT到一个轻量级验证器，该验证器评估轨迹的正确性。这一验证器实质上提升了推理准确性和测试时间扩展的效果。
### Innovation
本文首次提出了‘反思景观’（LoT），一种用于检验大型语言模型推理轨迹的可视化工具。该工具通过将文本状态沿轨迹表示为与答案选项距离的数值特征，并使用t-SNE进行可视化，从而有效地区分强弱模型、正确和错误的答案，以及不同的推理任务。此外，它还能揭示不良的推理模式，并可用于调整到一个轻量级验证器，评估轨迹的正确性。
### Conclusion
反思景观为理解大型语言模型的推理过程提供了一种新颖的方法。它不仅能够提升推理准确性和测试时间扩展的效果，还能帮助识别不良推理模式，对研究和应用都具有重要意义。
## 633. `cs.LG` - SC-LoRA: Balancing Efficient Fine-tuning and Knowledge Preservation via Subspace-Constrained LoRA [PDF](https://arxiv.org/pdf/2505.23724), [HTML](https://arxiv.org/abs/2505.23724)
### Authors
Minrui Luo,Fuhang Kuang,Yu Wang,Zirui Liu,Tianxing He
### Background
PEFT方法，特别是低秩适应（LoRA），对于高效定制大型语言模型（LLMs）至关重要。然而，LoRA的常用实现存在收敛速度慢和知识遗忘的问题。已有研究利用设计的LoRA初始化来提高微调效率或保存知识，但这些方法无法同时解决这两个问题。
### Innovation
介绍了SC-LoRA，一种新的LoRA初始化框架，旨在平衡高效微调和知识保存。通过在低秩子空间中约束可训练LoRA适配器的输出，以平衡保留细调数据的上下文信息和保留知识数据的上下文信息，从而使可训练权重主要关注细调数据的主要特征，同时避免损害保留的知识特征。该方法在理论上进行了分析，并在多种下游任务中进行了广泛的实验，包括安全性和世界知识的保存。
### Conclusion
在实验中，SC-LoRA 在提升微调性能的同时显著减少了知识遗忘，超越了当前的LoRA初始化方法。
## 634. `cs.LG` - 通过预评分高效注意力: Transformer中优先处理信息性键 [PDF](https://arxiv.org/pdf/2505.11040), [HTML](https://arxiv.org/abs/2505.11040)
### Authors
Zhexiang Li,Haoyu Wang,Yutong Bao,David Woodruff
### Background
近期，变压器架构在长时间语境语言建模方面取得了显著进步。HyperAttention通过结合基于LSH的一级聚类和均匀残差采样实现了较高的效率，但未能识别所有关键键，进而增加了整体困惑度。
### Innovation
本文提出了一种预评分机制，在应用HyperAttention之前优先处理重要键。引入了三种评分方法：$k$-means和核$k$-means聚类、$k$-median聚类以及基于LevAttention的杠杆得分排序，有效过滤键。此外，完全依赖预评分机制取代了HyperAttention的原始均匀残差采样。实验表明，在ChatGLM2（131k标记上下文）上减少了从12到8.3的困惑度，超过了标准HyperAttention。当在Vision-Transformer (ViT)上运行时，本文方法与LevAttention相似的准确性，并在特定参数下会超越LevAttention。尽管引入了一些计算开销，但与FlashAttention相比，其结合使用实现了最多20倍的速度提高，平衡了速度和建模准确性之间的关系。
### Conclusion
本文结果强调了将预评分集成到层次化注意力机制中的有效性，显着改善了变压器的效率。
## 635. `cs.LG` - 个人公平性受益于匿名化，群体公平性受损？匿名化对机器学习公平性影响审计 [PDF](https://arxiv.org/pdf/2505.07985), [HTML](https://arxiv.org/abs/2505.07985)
### Authors
Héber H. Arcolezi,Mina Alishahi,Adda-Akram Bendoukha,Nesrine Kaaniche
### Background
机器学习算法依赖于大量的训练数据，这些数据可能包含数据提供者的敏感信息。这引发了严重的隐私问题。匿名化技术通过泛化特征或屏蔽数据以提高准确识别个体的难度作为实践解决方案，得到了广泛应用。然而，尽管最近的研究表明，增强隐私的技术会影响机器学习在不同子群体中的预测，从而影响公平决策，但匿名化技术如K匿名、L多样性、T接近对于机器学习公平性的影响仍待深入探索。本文系统性地审计了匿名化技术对机器学习公平性的影响，评估了个体和群体公平性。定量研究揭示匿名化可能会将群体公平性指标降低四倍。此外，基于相似性的个体公平性指标在更高程度匿名的情况下有所改进，主要由于输入的同质性增加。通过分析不同隐私设定和数据分布下的匿名化级别，本研究提供了关于隐私、公平性和效用之间权衡的关键见解，并提出了以人为本的人工智能开发指南。相关代码已公开发布。
### Innovation
本文首次系统性地审计了不同匿名化技术（K匿名、L多样性、T接近性）对机器学习公平性，特别是对个体和群体公平性的影响。通过定量分析和不同隐私设定及数据分布下的实验，揭示了匿名化对机器学习公平性和效用之间的权衡关系。
### Conclusion
研究表明，匿名化可能会显著降低群体公平性指标，但可能提高基于相似性的个体公平性指标。本研究为平衡隐私保护、公平性和效用提供了实践指导，并强调了在人工智能发展中考虑这些权衡的重要性。相关代码已公开提供，以供进一步研究和实施使用。
## 636. `cs.LG` - 通过μP高效扩展扩散变换器 [PDF](https://arxiv.org/pdf/2505.15270), [HTML](https://arxiv.org/abs/2505.15270)
### Authors
Chenyu Zheng,Xinyu Zhang,Rongzhen Wang,Wei Huang,Zhi Tian,Weilin Huang,Jun Zhu,Chongxuan Li
### Background
扩散变换器作为视觉生成模型的基础，但其可扩展性受限于大规模调参的高成本。之前，$u$P参数化方法被提出应用于标准变换器，能够稳定地从小型到大型语言模型进行超参数转移，并显著降低调参成本。然而，尚不清楚$u$P是否同样适用于扩散变换器，因为它们在架构和目标上存在差异。
### Innovation
本研究将标准$u$P扩展至扩散变换器，并通过大规模实验验证其有效性。研究表明，主流的扩散变换器（如U-ViT、DiT、PixArt-$u$和MMDiT）的$u$P与标准变换器的$u$P一致，可以直接应用现有$u$P方法。利用这一结果，通过系统实验展示了DiT-$u$P的稳健超参数可转移性，并且DiT-XL-2-$u$在学习率转移后比原模型快2.9倍。此外，通过将PixArt-$u$和MMDiT模型分别扩大至0.61B和18B量级，进一步验证了$u$P的有效性，两个模型在保持训练成本低的情况下均优于各自的基线，并且只消耗了5.5%和3%的原有训练运行时间和人类专家使用的资源量。
### Conclusion
结果表明，$u$P是一个理论基础强且高效的框架，能够有效扩展扩散变换器。
## 637. `cs.LG` - 使用多模态视图增强的大视图模型进行长期时间序列预测 [PDF](https://arxiv.org/pdf/2505.24003), [HTML](https://arxiv.org/abs/2505.24003)
### Authors
ChengAo Shen,Wenchao Yu,Ziming Zhao,Dongjin Song,Wei Cheng,Haifeng Chen,Jingchao Ni
### Background
时间序列通常用数字序列表示，但也可转化为图像和文本，提供同一信号的多模态视图（MMVs）。MMVs揭示互补模式并允许使用强预训练大模型，如大规模视觉模型（LVMs）来进行长期时间序列预测（LTSF）。然而，研究发现最先进的LVM基预测器倾向于“预测时期”的归纳偏见，我们提出的DMMV框架利用趋势-季节分解和一种新颖的基于回溯残差的自适应分解结合MMVs来解决这一问题，提升LTSF效果。
### Innovation
本文提出了DMMV（分解基多模态视图），这是一种新颖的基于分解的多模态视图框架，利用趋势-季节分解和一种基于回溯残差的自适应分解技术将MMVs整合用于LTSF。与14个最新的模型在多个数据集上的对比表明，DMMV在6个基准数据集上达到了最低的均方误差（MSE），优于单视角和现有多模态基线模型。
### Conclusion
DMMV框架通过克服LVM预测器的归纳偏见，显著提升了LTSF的性能，并在多个数据集上取得了最佳结果。
## 638. `cs.LG` - 吸收并收敛：吸收离散扩散模型的可证明收敛性保证 [PDF](https://arxiv.org/pdf/2506.02318), [HTML](https://arxiv.org/abs/2506.02318)
### Authors
Yuchen Liang,Renxiang Huang,Lifeng Lai,Ness Shroff,Yingbin Liang
### Background
离散状态空间扩散模型在处理离散数据，如文本和图像生成时表现出显著优势。然而，这些模型的性能高度依赖于速率矩阵的选择，尤其是均匀和吸收类型的矩阵。虽然实证结果表明吸收型矩阵通常能产生更好的生成质量，但现有理论工作主要集中在均匀型矩阵的情况下。重要的是，对于吸收型扩散模型的收敛保证和误差分析仍然缺失。
### Innovation
本文首次为使用吸收型速率矩阵的离散扩散模型提供了有限时间误差界和收敛率分析。通过引入近似初始化分布来解决吸收平稳分布带来的KL散度未定义问题，证明了吸收型赤化跳跃和均匀化抽样的收敛保证，并表明与均匀型矩阵节点相比具有改进的收敛率。在适当假设下，还提供了无需提前停止的收敛保证。新的技术工具包括Jensen型论证、吸收评分函数的新技术以及接近初始化时得分的非发散上界，从而省去了提前停止的需要。
### Conclusion
本文的新理论工具解决了吸收型速率矩阵特有的挑战，为吸收型离散扩散模型提供了关键的可证明收敛保证和误差分析，改进了基于均匀型速率矩阵模型的收敛率。
## 639. `cs.LG` - GAIA：用于操作大气动力学的基座模型 [PDF](https://arxiv.org/pdf/2505.18179), [HTML](https://arxiv.org/abs/2505.18179)
### Authors
Ata Akbari Asanjan,Olivia Alexander,Tom Berg,Stephen Peng,Jad Makki,Clara Zhang,Matt Yang,Disha Shidham,Srija Chakraborty,William Bender,Cara Crawford,Arun Ravindran,Olivier Raiman,David Potere,David Bell
### Background
本文介绍了GAIA（地理空间人工智能）、一种将掩码自编码器（MAE）与无标签自我蒸馏（DINO）融合的混合自监督地理空间基础模型。该模型用于生成来自全球静止卫星图像的语义丰富的表示。GAIA经过15年全球合并红外观测数据训练（2001-2015年），通过分布式主成分结构和时间一致性分析显示出能捕捉大气动力学特征而非简单的日变化模式。
### Innovation
GAIA通过结合掩码自编码器和自我蒸馏，能在大量未标注的全球卫星数据上生成包含大气动力学特征的表示。相较于仅仅使用自编码器的方法，GAIA在对大气河流分割（F1得分提高）、热带气旋检测（召回率和早期检测时间提高）和降水估计性能方面表现出更优的效果。这种模型鼓励学习空间一致性且以对象为中心的特征，这些特征分散在多个主成分中。这项工作展示了结合互补的自监督目标可以为多样的大气建模任务提供更可转移的表示。
### Conclusion
GAIA在大气动力学任务上的表现表明，结合互补的自监督目标可以产生更适用于不同大气模型任务的可迁移表示。研究结果揭示了自编码器和自我蒸馏的结合如何促进了以空间一致性且以对象为中心的特征的学习，而这些特征分布在一个多种主成分中而不是集中于一个单一的重建焦点。这些发现为未来的自监督学习和大气科学模型开发提供了新的视角。
## 640. `cs.LG` - 一种具有自动阈值的稳健且非迭代的张量分解方法 [PDF](https://arxiv.org/pdf/2505.06203), [HTML](https://arxiv.org/abs/2505.06203)
### Authors
Hiroki Hasegawa,Yukihiko Okada
### Background
物联网和生物识别传感技术的最新进展导致了大量高维张量数据的生成，然而实现准确且高效的低秩近似仍然是一个主要挑战。现有的大多数张量分解方法需要预设的秩和迭代优化，这导致了较高的计算成本和对分析师专业知识的依赖。
### Innovation
本文提出了一种新颖的张量低秩近似方法，该方法无需预先指定秩和迭代优化。该方法通过在每个模式展开的矩阵上应用统计奇异值硬阈值来自动抽取统计上显著的成分，从而有效减少了噪声同时保持了固有的结构。理论上，每个模式的最佳阈值是从马尔琴科-帕斯图分布的渐进行为中推导出来的。
### Conclusion
模拟实验表明，本文提出的方法在估计准确性和计算效率方面均优于传统方法（HOSVD、HOOI和Tucker-L2E）。这表明，本文提出的方法提供了一种具有理论依据、全自动且非迭代的张量分解框架。
## 641. `cs.LG` - PoLAR：基于极分解的低秩适配器表示 [PDF](https://arxiv.org/pdf/2506.03133), [HTML](https://arxiv.org/abs/2506.03133)
### Authors
Kai Lion,Liang Zhang,Bingcong Li,Niao He
### Background
低秩适应大规模模型时会出现稳定秩偏低的问题，该稳定秩远低于子空间的线性代数秩，从而影响微调性能。为解决资源分配不足的问题，本文研究了低秩更新的表示方法，旨在提高模型的微调效果和学习效率.
### Innovation
提出了PoLAR（Parameterization inspired by the polar decomposition），该方法通过极分解启发式的参数化，将低秩更新向量分解为两个受Stiefel流形约束的方向矩阵和一个无约束的比例矩阵。理论研究表明，PoLAR方法在低秩适应问题上具有指数级的更快收敛速度，且与Riemannian优化方法结合后，能够在不同基础模型规模（从小到大的350M到27B）的三个测试基准中表现出一致的改进效果，涵盖通用语言理解、常识推理和数学问题解决.
### Conclusion
PoLAR通过有效利用分配给子空间的参数，提升了低阶更新向量的表示效率和适应性学习的收敛性，在多项任务上展示了显著的改进，证明了其在提升大规模模型适应性能方面的有效性.
## 642. `cs.LG` - 基于学习理论界值的核条件检验 [PDF](https://arxiv.org/pdf/2506.03898), [HTML](https://arxiv.org/abs/2506.03898)
### Authors
Pierre-François Massiani,Christian Fiedler,Lukas Haverbeck,Friedrich Solowjow,Sebastian Trimpe
### Background
本文提出了一种框架，用于假设检验条件概率分布，并用该框架构建了条件分布功能的统计检验。这些检验可以识别出功能在高概率下差异的输入，包括条件矩检验和两样本检验。关键思想是将学习方法的置信界转化为对条件期望的检验。本文将这一原则应用于高斯噪声下的核岭回归（KRR）。中间数据嵌入使通过核均值嵌入可以进行更广泛的检验——包括条件两样本检验。
### Innovation
1. 提出了一种将学习方法置信区间转化为条件期望检验的新框架。2. 将现有的KRR置信区间推广到无限维输出和非迹类核等先前难以访问但至关重要的情况，避免了需要独立数据的问题。3. 引入了基于理论中测试阈值的参数化形式的重新采样方案，使得测试方法更易于在实践中应用。
### Conclusion
本文从理论保证到算法实现建立了一个全面的条件测试基础，推进了向量值最小二乘估计置信区间的状态前沿。
## 643. `cs.LG` - 支持插入和删除的图扩散 [PDF](https://arxiv.org/pdf/2506.15725), [HTML](https://arxiv.org/abs/2506.15725)
### Authors
Matteo Ninniri,Marco Podda,Davide Bacciu
### Background
基于离散去噪扩散概率模型（DDPMs）的图生成模型提供了一种系统去除结构噪声的原理性方法，通过迭代的原子和键调整来生成分子结构。然而，现有的这些模型在扩散过程中无法适应图的大小（即原子的数量），这在条件生成场景（如根据性质进行分子设计）中限制了模型的有效性，因为目标性质通常与分子大小相关。
### Innovation
该论文改革了去噪和去噪过程，以支持节点的单调插入和删除，提出了名为GrIDDD的模型，在生成过程中可以动态地增长或缩小化学图。该模型在利用更困难的问题进行训练后，在分子性质靶向方面达到了或超过了现有图扩散模型的性能；在分子优化应用中，GrIDDD表现出了与专门优化模型相当的竞争性。
### Conclusion
这项工作为适应大小的分子生成打开了可能性，通过图扩散来实现自适应分子生成方法。
## 644. `cs.LG` - UdonCare：通过层次修剪发现未见领域在预测型医疗中的应用 [PDF](https://arxiv.org/pdf/2506.06977), [HTML](https://arxiv.org/abs/2506.06977)
### Authors
Pengfei Hu,Xiaoxue Han,Fei Wang,Yue Ning
### Background
医疗提供者常根据患者共同的临床因素（如病史）将患者群体划分为不同的组别，从而提供个性化医疗服务。在临床预测模型中，这一理念同样适用，并提出了一个至关重要的挑战：如何同时捕捉全局和特定组别的模式，同时使模型能够泛化到未见过的领域。这一挑战被列入了领域泛化（DG）的范畴。然而，传统的DG方法在临床环境中往往难以实现，主要是因其缺乏显式的领域标签和在医学知识上的先天不足。
### Innovation
我们提出了UdonCare，一种基于层次剪枝的方法，通过迭代地将患者划分为隐性领域，并从患者数据中分解出领域不变性（标签）信息。该方法通过修剪医学本体（例如ICD-9-CM层次结构）来识别患者领域。在两项公开数据集MIMIC-III和MIMIC-IV上，UdonCare在四个临床预测任务中比八个基线模型表现更优，突显了医学知识在指导临床领域泛化问题方面未被充分利用的潜力。
### Conclusion
UdonCare展示了通过层次修剪从医学本体中发现未见过领域的潜力，这对于解决临床领域的泛化问题具有重要意义，特别是对于临床预测模型而言，该方法能够有效地捕捉不同组别之间的模式，同时保持模型的泛化能力。
## 645. `cs.LG` - 几何感知边聚合在图神经网络中的应用 [PDF](https://arxiv.org/pdf/2506.11700), [HTML](https://arxiv.org/abs/2506.11700)
### Authors
Katharina Limbeck,Lydia Mezrag,Guy Wolf,Bastian Rieck
### Background
图神经网络（GNNs）在图相关任务中展现了显著的成功。由于现实世界应用场景中大量数据的普遍存在，池化层成为GNNs的重要组成部分，通过减少输入图的大小，池化可以加快训练速度并可能提升泛化能力。然而，现有的池化操作往往侧重于优化学习任务，代价是牺牲了基本的图结构，从而降低了可解释性，导致不同数据集类型、下游任务和池化比例下的表现不可靠。
### Innovation
本文提出了一种基于边坍缩的结构感知池化方法来应对这些挑战。该方法利用扩散几何，并通过迭代地减少图的大小来同时保持其度量结构和结构多样性。使用不变于等距变换的多样性度量（magnitude）来指导池化过程，以控制池化过程的保真度。同时使用度量空间的展开作为计算效率更高的替代方案，以确保计算效率。实验结果表明：(i) 其方法在多种不同类型图分类任务中性能最佳；(ii) 保留输入图的关键频谱属性；(iii) 能在不同池化比例下保持高准确度。
### Conclusion
本文提出了一种新颖的图池化层，通过边坍缩实现结构感知池化，利用扩散几何和不变于等距变换的多样性度量来控制池化过程的保真度。此外，使用度量空间的展开作为计算效率更高的替代方案，确保计算效率。通过实验验证了该方法在多个图分类任务上的优越性，并且能够保留输入图的关键频谱属性和较高的准确性，适用于不同池化比例的情况。
## 646. `cs.LG` - 动作分块和探索性数据收集在连续控制中的行为克隆中提供指数级改进 [PDF](https://arxiv.org/pdf/2507.09061), [HTML](https://arxiv.org/abs/2507.09061)
### Authors
Thomas T. Zhang,Daniel Pfrommer,Chaoyi Pan,Nikolai Matni,Max Simchowitz
### Background
本文基于现代机器人学习和连续控制中最具影响力的两种干预措施进行理论分析：动作分块（在开环中预测动作序列）和专家演示的探索性增强。尽管最近的研究表明，在连续环境中，从演示学习的技术性问题，如模仿学习（IL），可能会与任务持续时间成指数级地积累错误，但本文展示了在不同情境下动作分块和探索性数据收集能够规避这些指数级误差的问题。研究还强调了控制理论稳定性作为这些干预措施益处的关键机制。通过实验在流行的机器人学习基准上验证其预测，并通过理论分析，表明控制理论视角提供了对累积误差形成机制的精细洞察，从而在应用这些干预措施时，提供了比仅基于信息论考虑的先前技术更紧的统计保证。
### Innovation
本文提出了一种新的方法，通过动作分块和探索性数据收集来避免连续控制中模仿学习中积累的指数级错误。通过对比分析，发现控制理论稳定性是提高模仿学习效果的关键机制，并且通过实验验证了该理论的有效性。
### Conclusion
本文通过理论和实验验证，表明动作分块和探索性数据收集可以显著提升连续控制场景中的行为克隆性能，且结合控制理论分析提供了更可靠的统计保证。
## 647. `cs.LG` - 基于深度学习和不确定性估计的临床试验入组预测 [PDF](https://arxiv.org/pdf/2507.23607), [HTML](https://arxiv.org/abs/2507.23607)
### Authors
Tien Huu Do,Antoine Masquelier,Nae Eoun Lee,Jonathan Crowther
### Background
临床试验是评估新药或治疗方法的安全性和有效性的系统性努力。此类试验通常需要大量的资金投入和细致的计划，因此预测试验结果在计划阶段显得尤为关键。其中，准确预测患者入组情况是主要挑战之一。当前的模型尝试解决这一挑战，但论文提出一种基于深度学习的新方法，通过预训练语言模型捕捉临床文件的复杂性和细微之处，将其转换为有效的表示形式，进而结合编码的表格特征和注意力机制。此外，该模型还采用基于伽玛分布的概率层来考虑入组预测中的不确定性，并实现范围估计。
### Innovation
论文提出了一种基于深度学习的新方法，使用预训练语言模型捕捉临床文件的复杂性和细微之处，并通过编码表格特征和注意力机制进行融合。特别之处在于模型中加入了基于伽玛分布的概率层，以考虑入组预测中的不确定性，并实现范围估计。该模型用于预测临床试验的持续时间，并在特定临床试验数据集上进行了广泛的实验，表明所提方法可以有效预测给定临床试验中多个站点的患者入组情况，优于现有的基准模型。
### Conclusion
该研究提出的方法可以有效预测临床试验的患者入组情况，并在真实临床试验数据集上表现出更好的性能，优于现有的基准模型。这种方法能够为临床试验规划提供更准确的预测，有助于降低不确定性带来的成本和时间风险。
## 648. `cs.LG` - RTNinja: 一种用于纳米电子器件中随机脉冲噪声信号分析的通用机器学习框架 [PDF](https://arxiv.org/pdf/2507.08424), [HTML](https://arxiv.org/abs/2507.08424)
### Authors
Anirudh Varanasi,Robin Degraeve,Philippe Roussel,Clement Merckling
### Background
随机脉冲噪声是纳米电子器件中普遍存在的可变现象，源于缺陷位置的随机载流子交换，对器件可靠性和性能产生严重影响。传统的分析技术通常依赖于严格的假设或手动干预，限制了它们在复杂、嘈杂数据集中的应用。
### Innovation
我们提出了RTNinja，这是一种通用的全自动机器学习框架，用于无监督分析随机脉冲噪声信号。RTNinja能够分解复杂的信号，确定隐藏个体源的数量和特性，无需对系统有任何先验知识。该框架由两个模块组成：LevelsExtractor，使用贝叶斯推理和模型选择来去噪和离散信号；以及SourcesMapper，通过概率聚类和优化来推断源配置。我们使用蒙特卡洛模拟器生成了广泛信噪比和源复杂度的有标签数据集，在7000个这样的数据集中，RTNinja始终表现出高度准确的信号重建和源幅度及活动模式的提取。
### Conclusion
我们的结果表明，RTNinja提供了一种稳健、可扩展且设备无关的随机脉冲噪声表征工具，能够进行大规模统计基准测试、可靠性导向的技术验证、预测故障建模以及下一代纳米电子器件设备物理探索。
## 649. `cs.LG` - PPDiff: 在混合序列-结构空间中扩散进行蛋白质-蛋白质复合物设计 [PDF](https://arxiv.org/pdf/2506.11420), [HTML](https://arxiv.org/abs/2506.11420)
### Authors
Zhenqiao Song,Tiaoxiao Li,Lei Li,Martin Renqiang Min
### Background
在生物医学研究和生物技术中，设计与蛋白质具有高亲和力的蛋白质是至关重要的。尽管最近在特异性蛋白质领域取得了进展，但根据需求创建任意蛋白质目标的高亲和力结合子，而无需大量湿实验测试，依然是一个重大挑战。本文通过引入PPDiff模型，尝试解决这一问题。PPDiff利用Sequence Structure Interleaving Network with Causal attention layers（SSINC），结合了自注意力层捕捉全球氨基酸相关性、k近邻（kNN）等变图层建模三维局部相互作用、因果注意力层简化蛋白质序列间的复杂依赖关系，以非自回归的方式设计任意蛋白靶标的结合子的序列和结构。为了评估PPDiff，作者创建了PPBench数据集，包括来自蛋白质数据库(PDB)的706,360个蛋白质-蛋白质复合物，用于预训练和实际应用（靶蛋白-蛋白质迷你结合子设计及抗原-抗体复合物设计）的微调。结果显示，PPDiff在所有任务中都显著优于基准方法，取得接近预训练和两个下游应用的显著成功率。
### Innovation
PPDiff模型通过SSINC网络，在非自回归的方式下设计任意蛋白靶标的结合子的序列和结构，显著简化了蛋白质-蛋白质复合物的设计并提升了成功率。其独特之处在于模型结合了自注意力层捕捉全局相关性，k近邻（kNN）等变图层模型三维局部分子间作用关系，以及因果注意力层简化蛋白质序列间的复杂依赖关系，为非自回归序列结构设计提供了可行路径。
### Conclusion
PPDiff模型在多个生物信息学任务中表现出色，显著超越了现有的方法，为蛋白质-蛋白质复合物的设计提供了新的工具，为未来的生物医学研究和生物技术应用开辟了新的方向。
## 650. `cs.LG` - 数据流形上的点分类的图半监督学习 [PDF](https://arxiv.org/pdf/2506.12197), [HTML](https://arxiv.org/abs/2506.12197)
### Authors
Caio F. Deberaldini Netto,Zhiyang Wang,Luana Ruiz
### Background
该研究基于流形假设，将数据视为从低维流形$?mathcal{M} ?⊂ ?ℝ^F$中采样的点。通过使用变分自动编码器（VAE）无监督地近似流形，并将数据映射到表示其在$?mathcal{M}$中坐标的空间嵌入中，从而将点分类问题转换为基于图的半监督节点分类任务，该任务使用图神经网络（GNN）进行求解。研究的主要贡献在于从统计泛化性的角度分析了从数据到流形再到图的处理流程。通过对流形进行无监督近似以得到空间嵌入，并基于GNN解决节点分类问题，展示了使用这种方法进行半监督学习的效果。
### Innovation
本文提出了一种将点分类问题转化为图上的半监督节点分类任务的新方法，并通过构建具有高斯加权边的几何图来实现转换。这种方法的核心在于采用VAE进行无监督流形近似，并通过训练期间定期采样更大的图来进一步减少泛化差距，理论上证明了随着图的增大，泛化误差可以逐渐减小直至神经网络的训练误差，最终在图像分类基准上通过数值实验验证了这一方法的有效性。
### Conclusion
本文证明了对于基于图的半监督节点分类方法，在流形近似和GNN训练的框架下，图像分类任务中数据点分类的泛化误差随着图的规模增大而减小，并提供了训练期间定期采样更大图的方法来实现误差的进一步降低直至其渐近消失。这些实验结果表明本文方法在相关任务中具有优越的实用效果。
## 651. `cs.LG` - Multimodal LLM-assisted Evolutionary Search for Programmatic Control Policies [PDF](https://arxiv.org/pdf/2508.05433), [HTML](https://arxiv.org/abs/2508.05433)
### Authors
Qinglong Hu,Xialiang Tong,Mingxuan Yuan,Fei Liu,Zhichao Lu,Qingfu Zhang
### Background
深度强化学习在控制任务上取得了显著的成功，但其通过不透明的神经网络表示的策略难以供人类理解、验证和调试，这降低了信任度并阻碍了实际应用的部署。这一研究提出了通过引入一种新的程序控制策略发现方法——多模态大规模语言模型辅助进化搜索（MLES）来解决这一挑战。MLES 结合多模态大规模语言模型和进化搜索，自动化策略生成，并在策略生成过程中整合视觉反馈驱动的行为分析，以此识别失效模式并指导目标改进，从而提高策略发现效率并产生可适应、与人类对齐的策略。
### Innovation
引入了一种新的程序控制策略发现方法——MLES，结合多模态大规模语言模型和进化搜索，自动化策略生成。在控制任务的标准测试中，MLES 的性能与 Proximal Policy Optimization (PPO) 相当，同时提供了透明的控制逻辑和可溯的设计过程。这种方法克服了预定义领域特定语言的局限性，促进了知识的传递和再利用，并且在各种任务中都具有可扩展性，显示出透明可验证控制策略开发的新范式潜力。
### Conclusion
MLES 在保持性能的同时，提升了控制策略的透明度和可验证性，并且在各种任务中都展现出了可扩展性和发展潜力。
## 652. `cs.LG` - Khiops: 一种针对大量多表数据库的端到端、节俭型自动化机器学习和可解释性人工智能解决方案 [PDF](https://arxiv.org/pdf/2508.20519), [HTML](https://arxiv.org/abs/2508.20519)
### Authors
Marc Boullé,Nicolas Voisine,Bruno Guerraz,Carine Hue,Felipe Olmos,Vladimir Popescu,Stéphane Gouache,Stéphane Bouget,Alexis Bondu,Luc Aurelien Gauthier,Yassine Nair Benrekia,Fabrice Clérot,Vincent Lemaire
### Background
Khiops 作为一种开源的机器学习工具，旨在挖掘大规模多表数据库。它基于一种独特的贝叶斯方法，吸引了超过20篇学术论文的关注，涵盖了变量选择、分类、决策树和共聚类等主题。此工具通过数据离散化模型对数值数据进行变量重要性预测，并通过值聚类对分类数据进行重要性量化。
### Innovation
Khiops 引入了带有变量选择和权重学习的朴素贝叶斯分类/回归模型。特别是在处理多表数据库时，它能自动构建聚合并通过命题化转换提供预测。Khiops 能适应分析具有数百万个体、数万变量和数百亿记录的二次表的大规模数据库。
### Conclusion
Khiops 可在多种环境中使用，既可通过 Python 库也能通过用户界面访问。作为一个端到端的自动化机器学习和可解释性人工智能解决方案，Khiops 特别适合处理大型数据库。
## 653. `cs.LG` - 基于不确定性平滑策略正则化在稀疏示范强化学习中的应用 [PDF](https://arxiv.org/pdf/2509.15981), [HTML](https://arxiv.org/abs/2509.15981)
### Authors
Yujie Zhu,Charles A. Hepburn,Matthew Thorpe,Giovanni Montana
### Background
在强化学习中，稀疏奖励环境下，示范可以加速学习过程，但确定何时模仿这些示范仍然具有挑战性。本文提出的Smooth Policy Regularisation from Demonstrations (SPReD)框架旨在解决一个基本问题：智能体应该何时模仿示范，何时遵循其自身的策略？SPReD通过集成方法明确建模示范和策略行动的Q值分布，并量化不确定性以进行对比。
### Innovation
SPReD引入了两个互补的不确定性感知方法：一种概率方法估计示范优越性的可能性，和一种基于优势的统计显著性加权模仿方法。与现有的二元决策方法（如Q-filter）不同，SPReD使用连续的、与不确定性成比例的正则化权重，减少训练过程中的梯度方差。SPReD在八个机器人任务中表现出显著的性能提升，并且在复杂任务中比现有方法提高高达14倍，在示范质量和数量方面也保持了稳健性。
### Conclusion
通过应用SPReD，实验表明在多个机器人任务中取得了显著的性能提升，特别是在复杂任务中，相比现有方法，性能提升可高达14倍。该方法的优点还包括处理不确定性以及实现更稳健的学习过程。代码已公开。
## 654. `cs.LG` - 在代理噪声辅助下的源无处时间序列预测中不变特征解耦 [PDF](https://arxiv.org/pdf/2510.05589), [HTML](https://arxiv.org/abs/2510.05589)
### Authors
Kangjia Yan,Chenxi Liu,Hao Miao,Xinle Wu,Yan Zhao,Chenjuan Guo,Bin Yang
### Background
移动设备的普及产生了大量跨不同领域的时序数据，有效的时序预测能在许多现实应用中发挥作用。本研究关注的是一个新颖的源无处时间序列预测领域适应问题，在无法访问源数据的情况下，将预训练时序模型适应稀疏的目标时序领域，以遵守数据保护法规。
### Innovation
提出了一种名为TimePD的新型源无处时序预测框架，首次使用代理去噪方法。此框架利用大型语言模型的一般化能力，并包含三个关键组件：双分支不变解耦特征学习、无参数轻量级代理去噪以及双向知识蒸馏。
### Conclusion
实验证实在真实世界数据集上的表现远超最先进的基线方法，平均高出9.3%。
## 655. `cs.LG` - 离散扩散模型：新颖分析和新采样器保证 [PDF](https://arxiv.org/pdf/2509.16756), [HTML](https://arxiv.org/abs/2509.16756)
### Authors
Yuchen Liang,Yingbin Liang,Lifeng Lai,Ness Shroff
### Background
在涉及自然语言和图数据的应用中，离散扩散模型近年来获得了显著的关注。影响它们效果的关键因素之一是离散抽样器的效率。在这些模型中，τ跳跃抽样器因为其理论和经验上的成功而广受欢迎。然而，现有的 τ 跳跃抽样器的理论分析往往依赖于一些较为严格且难以验证的假设，并且其收敛性界限与词汇量大小存在二次依赖关系。
### Innovation
本文提出了一种新的分析方法，该方法可用于离散扩散模型，并消除了对这些假设的需要。对于标准的 τ 跳跃方法，我们建立了在 KL 散度下的收敛保证，与之前的二次依赖有所改进。此外，该方法还提供了对其他广泛使用的抽样器（包括欧拉方法和 Tweedie 跳跃方法）的第一种收敛保证。核心在于新提出的基于微分不等式的技巧，为其他随机过程的分析提供了更加灵活的选择。
### Conclusion
本工作提出了一种新的分析方法，该方法能够不需要任何假设地应用于离散扩散模型。对于标准的 τ 跳跃方法，我们的方法证明了在 KL 散度下的线性规模收敛保证，优于现有结果中的二次依赖。此外，该方法也是广泛适用的，提供了其他常用采样器的第一种收敛保证。
## 656. `cs.LG` - 从语言模型中提取隐秘知识 [PDF](https://arxiv.org/pdf/2510.01070), [HTML](https://arxiv.org/abs/2510.01070)
### Authors
Bartosz Cywiński,Emil Ryd,Rowan Wang,Senthooran Rajamanoharan,Neel Nanda,Arthur Conmy,Samuel Marks
### Background
本文研究隐秘知识的提取问题，即发现AI系统所掌握但未明确表述的知识。研究者通过训练大型语言模型（LLMs）使其拥有特定知识但否认这种知识，以此作为测试平台。这些LLMs在某些情况下表现一致，但在被直接询问时否认这些知识。研究者设计并评估了不同的秘密提取技术，测试它们能否帮助审计者猜出隐秘知识。这种方法能够揭示模型中的隐含知识，对于理解模型的内部运作具有重要价值。
### Innovation
本文最有效的技术是预填攻击（prefill attacks），这是一种黑盒技术，即在生成一个预先定义的前缀后，LLM会透露出隐秘知识。此外，基于logit镜头和稀疏自编码器（SAEs）的白盒技术也能提高提取成功率，但效果不如预填攻击明显。这些创新方法帮助研究者更有效地揭示LLMs中的隐秘知识，并提出了公共基准用于评估秘密提取方法的有效性。
### Conclusion
本文通过设计并评估多种秘密提取技术，证明了最有效的是预填攻击和基于logit镜头和稀疏自编码器的方法，建立了公共基准用于评估和改进秘密提取方法。
## 657. `cs.LG` - PRISM-Physics: 城市发展空间导向的因果DAG基过程评估 [PDF](https://arxiv.org/pdf/2510.03185), [HTML](https://arxiv.org/abs/2510.03185)
### Authors
Wanjia Zhao,Qinwei Ma,Jingzhe Shi,Shirley Wu,Jiaqi Han,Yijia Xiao,Si-Yuan Chen,Xiao Luo,Ludwig Schmidt,James Zou
### Background
竞争风格的基准已经在数学和编程领域中促进了评估的发展，但在物理学领域尚未得到足够的探索。目前大多数现有的物理基准仅评估最终答案，未能捕捉推理过程，而最近的按步骤的方法则依赖于启发式的人工智能作为评判者或线性假设评分，这限制了可靠性和诊断的有效性。
### Innovation
我们引入了PRISM-Physics，一个用于复杂物理推理问题的过程级评估框架和基准。解决方案表示为公式有向无环图（DAG），明确编码中间步骤之间的因果依赖关系，以实现细致、可解释且理论上支撑的评分。我们证明了DAG表示法及其相应的评分策略的最优性。结合我们开发的基于规则的方法进行符号公式等效匹配，以确保在不同表述形式下的一致验证，而无需启发式判断。实验结果表明我们的评估框架更符合人类专家的评分，而对最新一代语言模型的实验揭示了物理推理中的固有缺陷，步骤级评分提供了诊断洞察力和后续训练的丰富信号。通过结构严谨性、理论保证和符号验证组合，PRISM-Physics为过程级评估提供了理论基础，并引导了具有更深层次科学推理能力的模型的发展
### Conclusion
总的来说，PRISM-Physics通过结构严谨、理论保证和符号验证为过程级评估提供了原理基础，并引导了具有更深层次科学推理能力的模型的发展。
## 658. `cs.LG` - SVTime：受大型视觉模型预报器“物理”规律启发的小型时间序列预测模型 [PDF](https://arxiv.org/pdf/2510.09780), [HTML](https://arxiv.org/abs/2510.09780)
### Authors
ChengAo Shen,Ziming Zhao,Hanghang Tong,Dongjin Song,Dongsheng Luo,Qingsong Wen,Jingchao Ni
### Background
时间序列AI对于分析动态网络内容至关重要，导致了预训练大型模型的兴起，这些模型因其在各种任务中的强知识编码和迁移能力而受到青睐。然而，由于其能耗高、训练和推理硬件需求大，将大型模型作为一劳永逸的解决方案，可能会带来严重的碳排放和可持续性问题。对于特定任务而言，紧凑且专门化的高性能模型可能更加实用，特别是对于资源受限的用户，如小型企业。因此，本文提出了一个问题：是否可以构建出成本效益高、轻量级且在核心任务（如预测）上表现如同大型模型的小型模型？
### Innovation
本文提出了SVTime，这是一种新颖的小型时间序列预测模型，受到大型视觉模型（LVM）预报器的启发。论文定义了LVM预报器的关键归纳偏置，设计了紧凑且高效的小型模型，通过精心设计的线性层和约束函数来编码这些偏置，从而在低资源环境下实现高效的训练和推理，并在21种基准模型中表现出色。
### Conclusion
SVTime在8个基准数据集的21个基线模型中表现出色，不仅超越了最新的轻量级模型，还与参数量远少于LVMs的大型模型相媲美。同时，SVTime在低资源环境下的训练和推理也表现出高效性。
## 659. `cs.LG` - 通过强化学习探索解锁大语言模型的推理能力 [PDF](https://arxiv.org/pdf/2510.03865), [HTML](https://arxiv.org/abs/2510.03865)
### Authors
Wenhao Deng,Long Wei,Chenglei Yu,Tailin Wu
### Background
强化学习结合可验证奖励（RLVR）最近提升了大语言模型（LLMs）的推理能力，特别是在数学问题解决方面。然而，随着采样预算的增加，RLVR训练模型相较于其预训练基础模型的优势往往减弱甚至消失，这显示出RLVR模型对基础模型有限搜索空间的强烈依赖性。这一现象归因于广泛使用的逆Kullback-Leibler（KL）发散正则化器，其模式搜寻行为将策略困在基础模型的支持区域内，妨碍更广泛的探索。
### Innovation
本文提出了一种新的算法RAPO（Rewards-Aware Policy Optimization），旨在促进更广泛的但有选择性的探索。RAPO方法（i）利用前向KL惩罚替换逆KL惩罚以促进偏离分布的探索；（ii）重新加权参考策略以促进分布内的自适应探索。该方法在Qwen2.5-3B和7B模型上进行了训练，未采用监督微调，并在AIME2024和AIME2025上进行了评估。实验结果表明，RAPO能够持续提高解决问题的表现，并使模型超越基础模型的性能上限，解决了以前难以解决的问题，从而推进了RLVR在具有挑战性的推理任务中的应用前沿。
### Conclusion
RAPO算法能够使得具有挑战性的推理问题变得可解，并显著提升了模型的推理能力。这一方法解决了RLVR模型探索受限的问题，为大语言模型的强化学习研究提供了新的思路。
## 660. `cs.LG` - 当有所疑虑时，选择弃权：弃权对战略分类的影响 [PDF](https://arxiv.org/pdf/2510.13327), [HTML](https://arxiv.org/abs/2510.13327)
### Authors
Lina Alkarmi,Ziyuan Huang,Mingyan Liu
### Background
随着算法决策在各领域的广泛应用，其对战略操纵显得尤为脆弱。先前的研究表明，分类器的弃权策略（允许分类器在自信不足时拒绝做出决策）能够显著提升分类精度。本文将研究弃权策略在战略性分类中的影响，探索其如何影响战略性代理行为及其背后机制，并指导如何最优地利用弃权策略。
### Innovation
本文将弃权策略引入战略性分类环境中，将其视为Stackelberg博弈模型的一部分，这里的主导者（分类器）首先宣布策略，随后战略性代理者（作为追随者）尝试操控其可观察特征以获得期望结果。研究发现，最佳弃权策略能使主导者的收益（或损失）不低于无弃权策略环境，在战略性代理存在的情况下也成立。此外，研究还表明，弃权策略不仅能提高准确性，还可以提高操纵成本，尤其对于不合格的代理者，当操纵成本足够高时，弃权策略能有效抑制操作。
### Conclusion
研究结果强调了弃权策略作为减少算法决策框架中战略行为负面影响的重要工具的价值。
## 661. `cs.LG` - 发现和量化多模态EHR数据中潜在因果来源效果的教程 [PDF](https://arxiv.org/pdf/2510.16026), [HTML](https://arxiv.org/abs/2510.16026)
### Authors
Marco Barbero-Mota,Eric V. Strobl,John M. Still,William W. Stead,Thomas A. Lasko
### Background
当前，电子健康记录（EHR）提供了一种广泛的数据来源，但这些数据通常是多元化的且不完整，使得直接从这些数据中发现和量化潜在的因果关系具有挑战性。本研究旨在提供一个易于理解的、经过同行评审且可推广的因果推断机器学习管道，用于发现大规模EHR观察中的潜在因果因子，并量化这些因子对临床结果的影响。
### Innovation
该研究的创新之处在于提出了一种因果机器学习管道，该管道可以从不完美的多模态临床数据中发现潜在的因果来源，并将这些数据分解为概率独立的潜在因子，进而用于训练针对不同任务的因果模型。这些模型能够估计个体的因果影响，从而提供了在大规模医疗数据中发现和量化因果关系的新方法。
### Conclusion
本研究通过两个实际应用的总结展示了该方法的多样性和在大规模医疗发现中的实用价值。研究结果证明了该方法在解决许多临床问题上的潜力，强调了在多元和不完整的医疗数据中发现和量化潜在因果关系的重要性。
## 662. `cs.LG` - 解密MaskGIT采样器及其超越：Masked Diffusion中的自适应顺序选择 [PDF](https://arxiv.org/pdf/2510.04525), [HTML](https://arxiv.org/abs/2510.04525)
### Authors
Satoshi Hayakawa,Yuhta Takida,Masaaki Imaizumi,Hiromi Wakaki,Yuki Mitsufuji
### Background
掩码扩散模型已在多种领域中展现出生成高质量样本的良好性能，但其采样过程的加速仍相对未得到深入探索。研究有效采样器对于掩码扩散模型至关重要，因此有必要通过理论分析来揭示已有模型的功能和机制。MaskGIT作为一项用于图像建模的采样方法，本文对其进行了理论上分析，发现了其隐含的温度采样机制。通过这一分析，作者引入了一个名为“时刻采样器”的替代方案，它是MaskGIT的渐近等价替代品，更为适用和解释性强，通过“先选择后采样”的方式选取出掩码位置后再进行采样。这种方法改变了MaskGIT全维度采样的方式，将效率提升了一个新的层次，并促进了掩码扩散模型采样器的理论理解与实际应用的进步。本文还通过对Transformer采用部分缓存技术，以更低的计算成本逼近更长的时间历程，以及通过混合策略明确探索与利用权衡在自适应出掩中的应用，进一步提升了“先选择后采样”采样器的效率。实验结果验证了这些改进的有效性，且在图像和文本领域展现了优秀的实现效果，使得这一研究具有重大的理论与实践意义。
### Innovation
1. 通过引入“时刻采样器”，为MaskGIT提供了渐近等价但更实用和可解释的替代方案。2. 采用部分缓存技术优化了“先选择后采样”算法，显著提升了计算效率。3. 混合探索与利用策略在自适应出掩中形成明确的框架，增强了采样效率和模型的自适应性。4. 实现了对MaskGIT及其变体的理论分析，并证明了上述改进方法的有效性。
### Conclusion
本文通过理论分析揭示了MaskGIT的采样机制，并通过引入“时刻采样器”、优化部分缓存技术和采用混合策略，显著提升了MaskGIT及其变体的计算效率和自适应性。实验展示了这种方法的有效性和实用性，在图像和文本领域均有显著效果，从而推进了对掩码扩散模型采样器的理解和应用。
## 663. `cs.LG` - I-RAVEN-X：大规模语言模型和推理模型类比和数学推理泛化和鲁棒性评估基准 [PDF](https://arxiv.org/pdf/2510.17496), [HTML](https://arxiv.org/abs/2510.17496)
### Authors
Giacomo Camposampiero,Michael Hersche,Roger Wattenhofer,Abu Sebastian,Abbas Rahimi
### Background
该研究旨在评估大型语言模型（LLMs）和大型推理模型（LRMs）在类比和数学推理任务上的泛化能力和鲁棒性。I-RAVEN-X 是基于现有基准 I-RAVEN 扩展而来的新型符号基准工具，增加了操作复杂性、属性范围，并引入了感知不确定性。
### Innovation
I-RAVEN-X 通过提升操作复杂性、扩展属性范围并引入感知不确定性，对现有的类比和数学推理基准进行了改进。实验证明 LRMs 在处理更长的推理关系和更广泛属性范围时表现出较高的生产力和系统性，但仍难以应对不确定性推理与探索多概率结果的问题。
### Conclusion
尽管 LRMs 在某些方面的推理能力得到了改善，但其在处理不确定性推理任务时仍存在显著挑战，并且无法有效探索多概率结果。
## 664. `cs.LG` - DARTS-GT：具有可量化实例特定解释性分析的可微架构搜索的图变换器 [PDF](https://arxiv.org/pdf/2510.14336), [HTML](https://arxiv.org/abs/2510.14336)
### Authors
Shruti Sarika Chakraborty,Peter Minary
### Background
图变换器（GTs）作为处理图结构数据的强大架构已崭露头角，但其设计僵化，缺乏可量化的解释性。当前最先进GTs在整个层中采用固定类型的图神经网络（GNN），未能体现出深度特定组件选择的潜在好处，其复杂的架构使性能改进难以区分性能提升的真实模式和无效的相关性。
### Innovation
重新设计GT注意力通过不对称性，将结构编码和特征表示解耦：查询源自节点特征，而键和值来自GNN变换。在此基础上，使用可微架构搜索（DARTS）在每一层选择最优GNN操作符，从而使变换器注意本身具有深度内异质性（DARTS-GT）。为了理解发现的架构，首次为GTs开发了可量化解释性框架，通过因果消除。通过头偏差、专业化和焦点三个指标，识别哪些头和节点驱动预测，并支持模型比较。
### Conclusion
在八个基准测试中，DARTS-GT在四个数据集上取得了最先进的性能，同时在其他数据集上保持竞争力，发现的架构显示了数据集特定的模式。解释性分析揭示，视觉注意显著性和因果重要性并不总是相关，表明常用的可视化方法可能忽略了实际上重要的组件。重要的是，由DARTS-GT找到的异构架构比基线生成了更具解释性的模型，建立了图变换器不必在性能和解释性之间进行权衡的观点。
## 665. `cs.LG` - DrivAerStar：用于车辆气动优化的工业级CFD数据集 [PDF](https://arxiv.org/pdf/2510.16857), [HTML](https://arxiv.org/abs/2510.16857)
### Authors
Jiyan Qiu,Lyulin Kuang,Guan Wang,Yichen Xu,Leiyao Cui,Shaotong Fu,Yixin Zhu,Ruihua Zhang
### Background
随着汽车电气化进程加速，车辆气动力优化变得至关重要，减阻直接决定了电动汽车的续航里程和能效。传统方法面临计算量巨大的CFD仿真，每次设计迭代需要数周时间，或者简化模型牺牲生产级精度。虽然机器学习具有变革潜力，但现有数据集存在根本性限制，包括不足的网格分辨率、缺失的车辆部件和超过5%的验证误差，这在工业流程中无法部署。
### Innovation
作者引入了DrivAerStar数据集，包含12,000个使用STAR-CCM+软件生成的工业级汽车CFD仿真。这些仿真通过控制系统辅助变形（FFD）算法探讨了三种车辆配置的20个计算机辅助设计（CAD）参数，实现了完整的发动机舱和冷却系统，并带有现实的内部气流。DrivAerStar的数据集通过精细的网格策略和严格的壁面$y^+$控制，实现了风洞验证精度低于1.04%的效果，比现有数据集提高了五倍。基于此数据集训练的模型在生产级精度的同时将计算成本从数周缩短至几分钟。
### Conclusion
DrivAerStar是首个将学术机器学习研究与工业CFD实践相结合的数据集，为汽车开发中的数据驱动气动优化设立了新标准。此外，DrivAerStar展示了在计算限制当前限制创新的工程学科中，如何将高保真物理仿真与人工智能相结合的一个范例。
## 666. `cs.LG` - 汉克埃尔奇异值正则化用于高可压缩状态空间模型 [PDF](https://arxiv.org/pdf/2510.22951), [HTML](https://arxiv.org/abs/2510.22951)
### Authors
Paul Schwerdtner,Jules Berman,Benjamin Peherstorfer
### Background
深度神经网络使用状态空间模型作为层对于长序列任务非常适合，但在训练后压缩这些模型较为困难。文章探讨了通过正则化状态空间模型的汉克埃尔奇异值，使模型具有更快的奇异值衰减，从而实现压缩目的。
### Innovation
文章提出了一种通过利用特定块对角矩阵结构高效计算汉克埃尔奇异值的算法，以增强汉克埃尔奇异值正则化的可扩展性。实验结果表明，正则化状态空间层与标准状态空间层相比，压缩率最高可提升10倍，同时保持高准确率。
### Conclusion
论文证明了正则化的状态空间层在保持高准确率的同时，具有更高的可压缩性。通过开发的高效计算算法，该方法具有良好的可扩展性。
## 667. `cs.LG` - 关于对称函数的不确定性校准 [PDF](https://arxiv.org/pdf/2510.21691), [HTML](https://arxiv.org/abs/2510.21691)
### Authors
Edward Berman,Jacob Ginesin,Marco Pacini,Robin Walters
### Background
在机器人操作、分子物理学和星系形态分类等数据稀疏场景中，深度学习面临挑战。已有研究表明，通过对称网络可以在输入空间的欠采样部分提升建模能力，并且不确定性估计能够防止模型过于自信。然而，迄今为止，对称性和模型置信度以及更广泛意义上的对称性和模型校准之间的关系尚未被研究。本文通过分析对称性和不确定性校准错误（ECE和ENCE）之间的关系，旨在填补这一理论空白，揭示对称模型的一般化极限，并说明对称性不匹配如何导致分类和回归中的失校准问题。
### Innovation
本文通过证明在各种对称条件下不确定性校准错误（ECE和ENCE）的上下界，首次提出对称性与不确定性校准之间的理论关系。这种方法不仅可以揭示对称模型的一般化极限，还可以展示对称性不匹配如何导致分类和回归中的失校准问题。同时，作者通过数值实验进一步验证了对称性与不确定性之间的关系，从而为理解和改进深度学习算法提供了新的视角。
### Conclusion
本文揭示了对称性和不确定性校准之间的理论关系，并通过实验阐明了对称性失配、群大小以及 aleatoric 和 epistemic 不确定性与校准误差之间的关联。这种方法为对称模型的泛化能力和鲁棒性提供了有价值的指导。
## 668. `cs.LG` - SmartMixed：神经网络中自适应激活函数学习的两阶段训练策略 [PDF](https://arxiv.org/pdf/2510.22450), [HTML](https://arxiv.org/abs/2510.22450)
### Authors
Amin Omidvar
### Background
激活函数的选择对神经网络至关重要，但大多数架构仍然依赖于固定、统一的激活函数。研究表明，不同的神经元可能需要不同的激活函数来优化网络性能。为了解决这一问题，研究者提出了一种名为SmartMixed的两阶段训练策略，该策略能够使网络学习到最优的单个神经元激活函数，同时保持推理时的计算效率。该方法首先通过一种可微分的硬混合机制，使神经元从多种候选激活函数中适配性地选择；在第二阶段，根据第一阶段学习的选择，固定每个神经元的激活函数，从而生成一个在推理时计算高效的网络，支持优化的向量化操作。
### Innovation
SmartMixed提出了一种新的两阶段训练策略，允许网络在训练过程中学习到最优的单一神经元激活函数，从而提高网络性能并维持计算效率。这种方法通过一种可微分的硬混合机制从多种候选激活函数中选择，并在推理时固定这些选择，实现计算效率和性能优化。
### Conclusion
实验结果表明，不同层的神经元对激活函数有不同的偏好，这为理解神经架构的功能多样性提供了见解。使用不同深度的前馈神经网络在MNIST数据集上测试了SmartMixed，结果显示其在保持计算效率的同时，能够优化网络性能。
## 669. `cs.LG` - 使用强化学习生成辅助任务 [PDF](https://arxiv.org/pdf/2510.22940), [HTML](https://arxiv.org/abs/2510.22940)
### Authors
Judah Goldfeder,Matthew So,Hod Lipson
### Background
辅助学习（AL）是一种多任务学习形式，在这种形式中，模型通过对辅助任务的学习来提高主要目标的表现。虽然AL在诸如导航、图像分类和NLP等领域中改善了泛化性能，但它往往依赖于成本高昂且需要领域专业知识的人工标记辅助任务。元学习方法可以减轻这一问题，通过学习生成辅助任务，但通常需要基于梯度的两阶段优化，增加了大量计算和实现上的负担。
### Innovation
我们提出了RL-AUX，这是一种使用强化学习（RL）动态生成辅助任务的方法。通过为每个训练样例分配辅助标签，并奖励那些能够提高主要任务性能的样例选择，该方法能够自动生成有效的辅助任务。此外，我们还探索了学习针对每个样例的辅助损失权重的可能性。在CIFAR-100数据集上，该RL方法的表现优于人工标记的辅助任务，且与热门的基于梯度的两阶段优化基准具有同等效果。在其他分类数据集上的类似结果进一步验证了此方法的有效性。这项工作表明，使用RL生成有效辅助任务是一种可行的途径。
### Conclusion
我们的研究结果表明，使用RL生成辅助任务是一种可行的方法，能够在减少人工标注需求的同时保持或提高主要任务的性能，为解决多任务学习中的辅助任务设计问题提供了一种新的可能。
## 670. `cs.LG` - 通过解空间中的同源扰动加速非线性时变偏微分方程的数据生成 [PDF](https://arxiv.org/pdf/2510.21592), [HTML](https://arxiv.org/abs/2510.21592)
### Authors
Lei Liu,Zhenxin Huang,Hong Wang,huanshuo dong,Haiyang Xin,Hongwei Zhao,Bin Li
### Background
近年来，基于数据的深度学习方法，如神经运算符，在求解非线性时变偏微分方程（PDEs）方面取得了显著进展。然而，这些方法需要大量的解对——解函数和方程的右侧（RHS）。这些解对通常通过传统数值方法生成，这需要成千上万的时间步迭代，远远超过训练所需的几十个步骤。这样不仅增加了计算负担，还增加了时间复杂度。因此，需要一种新的数据生成算法来解决这些问题。
### Innovation
本文提出了一种新颖的数据生成算法，称为解空间中的同源扰动算法（HOPSS），它可以生成包含较少时间步长的训练数据集，而不像传统方法那样生成长时间步长的数据集。该算法能同时加速数据集生成并保持所需的精度。首先，通过可信解算器获得一组基础解函数，通常是经过成千上万时间步的计算，然后将其与训练数据集的时间步长对齐。之后，通过将两个解函数（其中一个作为主函数，另一个作为按小尺度系数缩放的同源扰动项）与随机噪声合并，高效地生成具有相似精度的PDE数据点。最后，利用这些数据点计算原始方程的右侧的变分，从而形成新的解对。理论和实验结果表明，HOPSS降低了时间复杂性，在例如纳维-斯托克斯方程的情况下，大约只需传统方法时间的10%，就能生成约10,000个样本，且具有相当的模型训练性能。 
### Conclusion
总之，HOPSS通过有效的数据生成技术，显著提高了模型训练效率，尤其是在解决非线性时变偏微分方程时。它在保留适当精度的同时，大大减少了所需的时间和计算量。
## 671. `cs.LG` - 向通用AI材料发现迈进：通过浸没冷却剂筛选的验证 [PDF](https://arxiv.org/pdf/2510.23371), [HTML](https://arxiv.org/abs/2510.23371)
### Authors
Hyunseung Kim(1),Dae-Woong Jeong(1),Changyoung Park(1),Won-Ji Lee(2),Ha-Eun Lee(2),Ji-Hye Lee(2),Rodrigo Hormazabal(1),Sung Moon Ko(1),Sumin Lee(1),Soorin Yim(1),Chanhui Lee(1),Sehui Han(1),Sang-Ho Cha(2),Woohyung Lim(1) ((1) LG AI Research, Republic of Korea, (2) Kyonggi University, Republic of Korea)
### Background
人工智能（AI）已成为材料发现的强大加速器，然而目前大多数现有的模型仍局限于特定问题，需要收集额外数据并重新训练才能用于检测新属性。
### Innovation
我们引入并验证了GATE（Geometrically Aligned Transfer Encoder）——一种通用AI框架，可以同时学习覆盖热学、电学、力学和光学等领域的34种物化性质。通过在共享几何空间中对这些性质进行对齐，GATE捕捉到跨性质的相关性，减少了多指标筛选中的孤立性质偏见现象。此外，GATE无需针对特定问题进行任何模型重构，便能够应用于数据中心的浸没冷却剂发现任务，筛选出92,861个可能用于实际部署的分子。
### Conclusion
这些结果确立了GATE作为适用于跨多种材料发现任务的通用AI平台的地位。
## 672. `cs.LG` - CDFlow: 使用循环矩阵和对角矩阵构建可逆层 [PDF](https://arxiv.org/pdf/2510.25323), [HTML](https://arxiv.org/abs/2510.25323)
### Authors
Xuchen Feng,Siyu Liao
### Background
规范流是一种允许通过可逆变换进行有效似然估计和采样的深度生成模型。关键挑战是如何设计具有增强表示能力的同时保持计算雅可比行列式和逆的成本效率的线性层。
### Innovation
该论文引入了一种新型的可逆线性层，基于循环矩阵和对角矩阵的乘积。这种分解将参数复杂度从O(n^2)降低到O(mn)，同时仍能近似一般的线性变换。利用快速傅里叶变换，该方法将矩阵求逆的时间复杂度从O(n^3)降低到O(mn log n)，并将计算对数行列式的复杂度从O(n^3)降低到O(mn)。
### Conclusion
CDFlow在自然图像数据集上实现了强大的密度估计，并有效建模具有固有的周期结构的数据。此外，CDFlow显著加速了规范流中的关键操作，为可扩展的生成建模提供了实际性的益处。
## 673. `cs.LG` - TempoPFN：线性RNN的合成预训练用于零样本时间序列预测 [PDF](https://arxiv.org/pdf/2510.25502), [HTML](https://arxiv.org/abs/2510.25502)
### Authors
Vladyslav Moroshan,Julien Siems,Arber Zela,Timur Carstensen,Frank Hutter
### Background
现有基于零样本的时序预测的模型在高效长时效预测和可重复性方面面临挑战，现有的仅使用合成数据的方法在挑战性基准测试中表现不佳。
### Innovation
提出了一种基于线性循环神经网络（RNN）的单变量时间序列基础模型TempoPFN，该模型使用带有状态交织的门控差异乘积架构，实现了通用心序列长度的全并行训练，避免了窗口化或摘要技术的使用，同时保持了稳健的时间状态跟踪。全面的合成数据管道结合了不同的生成器，包括随机微分方程、高斯过程和音频合成，并引入了新颖的增强方法。
### Conclusion
TempoPFN在Gift-Eval基准测试的零样本评估中表现出卓越的竞争性能，超越了所有现有仅使用合成数据的模型，并且在大多数基于真实数据训练的模型之上更具效率，同时提供了完全的数据生成管道和训练代码，以实现未来研究的可重复性。
## 674. `cs.LG` - 无数据神经操作符实现2D和3D纳维-斯托克斯方程的快速推断 [PDF](https://arxiv.org/pdf/2510.23936), [HTML](https://arxiv.org/abs/2510.23936)
### Authors
Junho Choi,Teng-Yuan Chang,Namjung Kim,Youngjoon Hong
### Background
高维度流体模型（如纳维-斯托克斯类型偏微分方程）的集合仿真在实时应用中计算成本高昂。神经算子可以实现快速推理，但受到成本高昂的数据需求和在3D流体中的弱泛化能力的限制。
### Innovation
该研究提出了一种无需数据的神经操作网络，用于纳维-斯托克斯方程，消除了配对解数据的需求，并在大型集合预报中实现了实时推理。该架构基于物理，接受初始条件、边界条件和forcing函数，能产生对高变异性及扰动具有鲁棒性的解。该方法在2D基准测试和3D测试案例中超越了之前的神经操作符，在精度上更优，并且对于集合相比传统的数值求解器更高效。它实现了对三维纳维-斯托克斯方程的准确解，这是之前数据免费神经操作符未能实现的。
### Conclusion
通过将基于数值的方法与机器学习的可扩展性相结合，这种方法为端到端的科学仿真和预测提供了一条实际的途径，建立了无数据的、高保真的偏微分方程代理模型。
## 675. `cs.LG` - Mixture-of-Experts Operator Transformer for Large-Scale PDE Pre-Training [PDF](https://arxiv.org/pdf/2510.25803), [HTML](https://arxiv.org/abs/2510.25803)
### Authors
Hong Wang,Haiyang Xin,Jie Wang,Xuanze Yang,Fei Zha,Huanshuo Dong,Yan Jiang
### Background
预训练在解决PDE问题时已显示出提高数据稀疏性和性能的有效性，但方程类型的异质性导致混合训练中的高误差问题。此外，通过增加网络宽度或深度来扩展参数的密集预训练模型会带来显著的推理成本。
### Innovation
提出了一种新颖的Mixture-of-Experts Pre-training Operator Transformer（MoE-POT），这是一种稀疏激活架构，能够高效地扩展参数并控制推理成本。MoE-POT模型通过分层路由器门控网络动态选择4个路由专家，从16个专家网络中，在推理过程中专注于特定方程特征。同时，引入了2个共享专家以捕捉PDE的共同性质并减少路由专家间的冗余。模型的最终输出是来自所有激活专家结果的加权平均值。通过在30M到0.5B参数范围内预训练于6个公开PDE数据集，我们的模型在零样本误差上比现有120M参数模型降低了多达40%。
### Conclusion
通过对模型进行解释性分析，结果表明数据集类型可以从路由器门控网络的决策中推断出来，这验证了MoE架构的合理性和有效性。
## 676. `cs.LG` - 仅使用单个训练种子评估机器遗忘的局限性 [PDF](https://arxiv.org/pdf/2510.26714), [HTML](https://arxiv.org/abs/2510.26714)
### Authors
Jamie Lanyon,Axel Finke,Petros Andreou,Georgina Cosma
### Background
机器遗忘（MU）旨在不执行昂贵的重新培训的情况下，从已训练的模型中移除某些数据点的影响。大多数实际的MU算法仅是近似的，其性能只能通过实验进行评估。因此，在进行对比实验时必须尽可能地保持代表性。通常的做法是从同一个训练模型开始，独立运行MU算法多次。然而，研究发现，即使在相同的架构和数据集下，某些MU方法对用于模型训练时的随机数种子的选择也非常敏感。
### Innovation
本文揭示了一个关键的局限性：仅使用单个训练种子评估MU算法的结果可能会非常代表性不足。研究者建议，在对比MU算法时，应反映不同训练种子对模型性能的影响，以保证结果的代表性。
### Conclusion
研究发现，使用单一训练种子评估MU算法可能会导致非代表性的结果。为了保证评估结果的代表性，推荐在对比不同MU算法时，反映不同模型训练种子的可变性。
## 677. `cs.LG` - Aeolus: 一个多模态飞行延误数据集 [PDF](https://arxiv.org/pdf/2510.26616), [HTML](https://arxiv.org/abs/2510.26616)
### Authors
Lin Xu,Xinyun Yuan,Yuxuan Liang,Suwan Yin,Yuankai Wu
### Background
现有的飞行延误数据集通常限于平坦的表格结构，无法捕捉飞行延误传播过程中的空间和时间动态。本文提出一个名为Aeolus的大规模多模态飞行延误数据集，旨在推动飞行延误预测的研究，并支持为表格数据开发基础模型。
### Innovation
Aeolus通过提供三个对齐的模态解决了上述限制：（i）包含丰富操作、气象和机场级别特征的表格数据集，涉及超过5000万次航班；（ii）飞行链模块，模拟沿序列飞行段的延误传播，捕捉上下游依赖关系；（iii）飞行网络图，编码共享飞机、机组人员和机场资源连接，支持跨航班关系推理。该数据集经过仔细构建，包含时间切分、全面特征和严格的泄漏预防，以支持现实和可重复的机器学习评估。
### Conclusion
Aeolus支持广泛的任务，包括回归、分类、时间结构建模和图学习，作为一个统一基准跨越表格、顺序和图模态。提供了基准实验和预处理工具以促进采用。Aeolus填补了领域特定建模和通用结构数据的关键空白，代码和数据可以从这里访问：https://github.com/Aeolus-dataset/Aeolus
## 678. `cs.LG` - 带有主动数据增强的离线偏好聚类学习 [PDF](https://arxiv.org/pdf/2510.26301), [HTML](https://arxiv.org/abs/2510.26301)
### Authors
Jingyuan Liu,Fatemeh Ghaffari,Xuchuang Wang,Xutong Liu,Mohammad Hajiesmaili,Carlee Joe-Wong
### Background
偏好学习从成对反馈中是一个广泛应用于强化学习带有人类反馈和推荐系统中的框架。然而，在很多实际应用场景中，用户交互是有限或昂贵的，因此需要离线偏好学习。此外，真实的偏好学习通常涉及具有不同偏好的用户群体，如来自不同背景的注释者可能对同一个回答有不同的排名。这带来了两个核心挑战：（1）在用户偏好不同且离线数据不平衡的情况下，有效地识别用户之间的相似性以聚合数据；（2）处理离线数据不平衡的情况，其中一些偏好维度代表性不足。
### Innovation
该论文提出了两个算法来解决离线偏好聚类学习中的两个核心挑战。首先提出了Off-C$^2$PL，应用于纯离线设置，依靠仅有的离线数据。随后提出A$^2$-Off-C$^2$PL，应用于包含主动数据增强的设置，允许学习者根据由Off-C$^2$PL学习到的聚类结构，选择为测试用户增加少量的主动数据，并更具针对性地选择不那么信息丰富的偏好维度的样本。
### Conclusion
我们的理论分析提供了子最优性边界，明确体现了样本噪声与偏差之间的权衡。我们还通过在合成数据集和真实世界数据集上进行的模拟验证了理论结果。最终，证明了主动收集的数据相比离线数据更有效。
## 679. `cs.LG` - 一种适用于All-Reduce的Top-K压缩器以实现通信高效的分布式学习 [PDF](https://arxiv.org/pdf/2510.26709), [HTML](https://arxiv.org/abs/2510.26709)
### Authors
Chuyan Chen,Chenyang Ma,Zhangxin Li,Yutong He,Yanjie Dong,Kun Yuan
### Background
在大规模分布式机器学习中，通信仍然是一个主要瓶颈。为了解决这个问题，已经提出了梯度稀疏化作为一种有前景的策略。然而，现有的梯度压缩器存在显著限制：Rand-$K$会丢弃结构性信息且在实践中性能较差，而Top-$K$虽然保留了有用的信息，但丢失了收缩性质，并需要昂贵的All-Gather操作。
### Innovation
本文提出了一种名为ARC-Top-$K$的All-Reduce兼容Top-$K$压缩器，在节点之间使用轻量级的梯度草图对稀疏模式进行对齐，从而实现索引无依赖的All-Reduce操作，同时保留全局显著信息。ARC-Top-$K$在与动量误差反馈（EF21M）结合使用时，能够证明具有收缩性，且在标准假设下，相比原始EF21M实现了线性加速和更快速的收敛速度。实验证明ARC-Top-$K$匹配Top-$K$的准确度，但能将训练时间减少高达60.7%，提供了一种既高效又可扩展的解决方案，结合了Rand-$K$的稳健性和Top-$K$的出色性能。
### Conclusion
ARC-Top-$K$结合了Rand-$K$的易用性和Top-$K$的性能优势，同时保持了收缩性质和高效的通信效率，为解决分布式学习中的通信瓶颈提供了一种有效的方法。
## 680. `cs.LG` - 高级采样法实现忠实且快速的影响函数 [PDF](https://arxiv.org/pdf/2510.26776), [HTML](https://arxiv.org/abs/2510.26776)
### Authors
Jungyeon Koh,Hyeonsu Lyu,Jonggyu Jang,Hyun Jong Yang
### Background
影响函数(IFs)通过使用梯度和Hessian提供了一种后验解决方案，以解释训练数据对黑盒模型的影响。然而，计算整个数据集的Hessian矩阵是一个资源密集型任务，通常需要找到一种可行的替代方案。一种常用的方法是随机抽取一小部分训练数据，但这种方法往往会导致IF估计结果差异性大且不一致，因为采样的配置具有高方差。因此，需要一种更精准且计算高效的采样方法来提高IF估计的准确性.
### Innovation
本文提出的创新之处在于提出了两种基于特征和预测值的高级采样技术。这两种技术通过考虑特征或预测值的随机分布来选择一小部分有代表性的数据，从而提高了IF估计的准确性。此外，该方法通过减少30.1%的计算时间和42.2%的内存使用，或在F1分数上提高了2.5%，相比基线方法实现了效率和准确性的双重提升.
### Conclusion
通过对删除类别的实验验证，本文方法有效地减少了模型忘记删除类别的同时保持了对剩余类别的推理一致性。实验结果表明，该方法在提高效率和准确性方面具有显著优势，可以作为一种有效提高IF估计准确性的实用方案。
## 681. `cs.LG` - ROBotic MAnipulation Network (ROMAN) -- Hybrid Hierarchical Learning for Solving Complex Sequential Tasks [PDF](https://arxiv.org/pdf/2307.00125), [HTML](https://arxiv.org/abs/2307.00125)
### Authors
Eleftherios Triantafyllidis,Fernando Acero,Zhaocheng Liu,Zhibin Li
### Background
在 embodied 人工智能中，解决长时间序列任务是一个显著的挑战。使机器人系统能够执行各种长时间序列任务并展现广泛的操控技能是当前研究的活跃领域。
### Innovation
提出了一个混合层次学习框架 Robotic Manipulation Network (ROMAN)，通过综合行为克隆、模仿学习和强化学习，ROMAN 生成正确的顺序动作序列，解决复杂的长期操控任务，同时展示了对各种感官噪声的鲁棒性。
### Conclusion
实验结果显示，通过协调和激活这些专门的操控专家，ROMAN 产生正确的顺序激活，完成复杂的操控任务序列，并展现出适应性行为，除了演示之外。这些结果表明 ROMAN 动态适应性的重要性和灵活性，及其在需要适应性运动技能的各种自主操控任务中的潜力。
## 682. `cs.LG` - ESTformer：基于时空依赖性的脑电图超分辨率方法 [PDF](https://arxiv.org/pdf/2312.10052), [HTML](https://arxiv.org/abs/2312.10052)
### Authors
Dongdong Li,Zhongliang Zeng,Zhe Wang,Hai Yang
### Background
轻量化脑电图（EEG）采集设备受到广泛关注，但是现有的EEG信道选择方法多依赖于具体的数据，缺乏一套统一有效的EEG采集设备标准。本文通过将EEG应用转化为超分辨率方式，尽管在计算成本、插值偏差、时空依赖性建模方面遇到瓶颈，但仍致力于改进。
### Innovation
提出了ESTformer，一种基于变压器的EEG超分辨率（SR）框架，它利用空间和时间维度的时空依赖性，使用位置编码方法和多头自注意力机制来捕捉空间结构关联和时间功能变化，并采用固定掩码策略和掩码标记以避免数学插值方法引起的扰动，从而提升低分辨率EEG数据的超分辨率。
### Conclusion
在两个EEG数据集上的实验表明，ESTformer在超分辨率任务上优于之前的最先进方法，证实了Transformer在EEG超分辨率任务中的通用性和优越性，特别是在基于脑电图的人体识别和情绪识别任务中，相较于低分辨率数据，得到了2%至38%的改进。
## 683. `cs.LG` - 朝着以人为本的解释性AI中训练数据归因用户导向研究 [PDF](https://arxiv.org/pdf/2409.16978), [HTML](https://arxiv.org/abs/2409.16978)
### Authors
Elisa Nguyen,Johannes Bertram,Evgenii Kortukov,Jean Y. Song,Seong Joon Oh
### Background
解释性AI（XAI）旨在提高AI系统的透明度，但许多实践过于强调数学严谨性而忽视了实用用户需求。在训练数据归因（TDA）这一新兴领域，存在重复其他子领域中解决方案主义模式的风险。TDA目前仍处于早期阶段，为通过用户中心实践塑造其发展方向提供了宝贵的机会。
### Innovation
本文通过设计思维过程提出了TDA的研究新方法，取代了模型中心的方法。为此，作者直接与机器学习开发者进行访谈研究（N=6）和基于场景的互动用户研究（N=31），使解释贴近实际工作流程。揭示了新型数据为中心的解释任务，如根据特定模型行为组合训练样本以及识别欠采样数据。
### Conclusion
本文邀请TDA、XAI和HCI社区参与到这些任务中，以加强其研究的实际相关性和人类影响。
## 684. `cs.LG` - 具有最优保证的对抗鲁棒聚类 [PDF](https://arxiv.org/pdf/2306.09977), [HTML](https://arxiv.org/abs/2306.09977)
### Authors
Soham Jana,Kun Yang,Sanjeev Kulkarni
### Background
本文考虑来自亚高斯混合的数据点的聚类问题。现有的能够证明达到最优分类错误率的方法，如Lloyd算法，通常对异常值敏感。然而，对于对抗性扰动具有鲁棒性的聚类方法，则无法满足最优统计保证。因此，文章讨论了在一个弱初始化条件下，对抗性异常值可能出现时，使用坐标中值为基础的简单鲁棒算法的优化错误率。在没有异常值的情况下，该算法在固定维度下的理论保证类似于Lloyd算法的理论保证。进行了广泛的仿真和公开数据集实验以支持该方法的理论保证。
### Innovation
提出了一种基于坐标中值的简单鲁棒算法，即使存在对抗性异常值，也能达到最优分类错误率。在满足弱初始化条件的情况下，算法在常数迭代内达到最优错误率。这种算法在没有异常值的情况下，在固定维度下，其理论保证类似于Lloyd算法。
### Conclusion
本文提出了一个具有对抗鲁棒性的简单聚类算法，即使在存在对抗性异常值的情况下也能达到最优分类错误率。在没有异常值的情况下，其理论保证与Lloyd算法相似。
## 685. `cs.LG` - 在再生核希尔伯特空间中的数据驱动随机最优控制 [PDF](https://arxiv.org/pdf/2407.16407), [HTML](https://arxiv.org/abs/2407.16407)
### Authors
Nicolas Hoischen,Petar Bevanda,Stefan Sosnowski,Sandra Hirche,Boris Houska
### Background
该论文提出了一个全数据驱动的方法来优化由随机扩散表示的非线性控制-仿射系统的控制。重点在于非线性动力学和阶段成本函数未知的场景，只提供控制惩罚函数和约束条件。通过将状态概率密度嵌入再生核希尔伯特空间（RKHS）来利用现代算子回归的进步，以此来识别与被控扩散过程相关的马尔可夫转移算子。这种算子学习方法与线性可扩展的算子理论哈密顿-雅可比-贝尔曼递归自然兼容，从而有效解决了一大类非线性最优控制问题。数值结果证明了该方法能够处理多种非线性控制任务，包括自主水下车辆的深度调节问题。
### Innovation
提出了一种全数据驱动的方法来优化非线性控制-仿射系统的控制。通过将状态概率密度嵌入再生核希尔伯特空间，结合算子回归的进步，并成功地与线性可扩展的算子理论哈密顿-雅可比-贝尔曼递归相结合，解决了非线性最优控制问题。这种方法能够在未知非线性动力学和阶段成本函数的情况下，仅提供控制惩罚函数和约束条件，有效处理复杂的控制任务。
### Conclusion
数值结果表明该方法能够处理广泛且复杂的非线性控制任务，展示了其在实际应用场景中的有效性，特别是对于自主水下车辆的深度调节任务。该方法不仅扩展了数据驱动控制理论的应用范围，同时也为解决更多的非线性控制问题提供了新思路。
## 686. `cs.LG` - 在空间转录组学数据中查询功能性与结构性微环境 [PDF](https://arxiv.org/pdf/2410.10652), [HTML](https://arxiv.org/abs/2410.10652)
### Authors
Mo Chen,Minsheng Hao,Xinquan Liu,Lin Deng,Chen Li,Dongfang Wang,Kui Hua,Xuegong Zhang,Lei Wei
### Background
多细胞生物中的细胞通过协调形成功能性和结构性的微环境。空间转录组学揭示了生理和病理过程中微环境作为一致且重出现的基本单元的重要性，这表明存在由保守的微环境模式编码的通用组织原则。因此，需要提出基于查询的微环境分析范式，超越现有的计算工具。
### Innovation
定义了Niche Query Task，即给定感兴趣的微环境（NOI），在空间转录组学样本中识别相似的微环境。进一步开发了QueST，这是一种专门方法用于解决此任务。QueST将每个微环境建模为子图，使用对比学习学习区分性的微环境嵌入，并通过对抗训练减轻批次效应。QueST在模拟和基准数据集中表现出色，准确捕获了异质环境中的微环境结构，并在不同的测序平台中展示了强大的泛化性。应用到肾癌和肺癌的三级淋巴样结构中，QueST揭示了与患者预后相关的功能性的差异微环境，并发现不同类型癌症中保守和变化的空间架构。
### Conclusion
QueST使系统、定量地分析样本中的空间微环境成为可能，为研究健康和疾病中的空间组织结构提供了一种强大的工具。
## 687. `cs.LG` - LIBMoE: 用于大规模语言模型中混合专家库的全面基准测试库 [PDF](https://arxiv.org/pdf/2411.00918), [HTML](https://arxiv.org/abs/2411.00918)
### Authors
Nam V. Nguyen,Thong T. Doan,Luong Tran,Van Nguyen,Quang Pham
### Background
混合专家（MoE）架构已成为扩展的关键基石，广泛应用于许多大型语言模型，如GPT-OSS、DeepSeek-V3、Llama-4和Gemini-2.5。然而，由于大规模训练和评估的高计算成本，限制了研究人员对MoE的深入研究。因此，需要一种统一的框架来简化MoE的研究，提供透明的分析工具，支持预训练和稀疏上层放大两种模式，并揭示路由动态和专家动力学的规律。
### Innovation
LibMoE是一个统一的研究框架，支持MoE的预训练和稀疏上层放大模式，提供透明的分析工具，降低进入门槛，标准化评估，实现全面的分析，包括路由动态、轻量级初始化对负载均衡的影响以及不同训练模式下的路由模式和稳定性分析。通过这些，LibMoE为MoE研究提供了更广泛的访问途径，并建立了一个可靠的基准来引导未来的创新。
### Conclusion
LibMoE不仅支持各种MoE架构的研究，也提供了深入分析路由动态、负载平衡与专家多样性的方式。它通过标准化评估和降低进入障碍，为研究人员提供了全面的基准测试环境，促进了未来MoE技术的发展。
## 688. `cs.LG` - SparsePO: 通过稀疏 token 标签控制 LLM 的偏好对齐 [PDF](https://arxiv.org/pdf/2410.05102), [HTML](https://arxiv.org/abs/2410.05102)
### Authors
Fenia Christopoulou,Ronald Cardenas,Gerasimos Lampouras,Haitham Bou-Ammar,Jun Wang
### Background
直接对齐算法已被证明是将语言模型与人的偏好行为对接的有效步骤。当前的直接偏好优化目标变体将重点放在所有 token 均等地为 KL 散度和奖励信号贡献的情形。然而，人的偏好常常不是由序列中的每个单词决定的，而是往往依赖于特定的单词或短语，例如存在毒性的术语会导致非偏好响应。基于这一观察，文章认为在偏好优化过程中并非所有 token 应当均等地被赋予权重，提出了一个称作 SparsePO 的灵活目标，旨在自动学习每个 token 对 KL 散度及奖励的加权在偏好优化训练中。
### Innovation
提出了一种称为 SparsePO 的新颖方法，该方法通过自动学习 token 的加权，在 preference 对齐过程中引入稀疏性，使得模型能够在 token 级别上学习如何平衡 KL 散度和奖励的贡献，优化加权的稀疏程度。SparsePO 方法提出了两种不同的权重掩码变体，这些掩码可以从参考模型推导而出或者在训练中实时学习。
### Conclusion
全面的实验证明，该方法在偏好表示中的对齐效果显著，特别是在情感控制、帮助性和无害性、以及总结质量方面。在总结和对话场景中，方法分别取得了 +10% 和 +3% 的 win rate 提升，同时不牺牲模型推理或总结响应的相关性和忠实性。
## 689. `cs.LG` - 监督二次特征分析：信息几何方法的降维 [PDF](https://arxiv.org/pdf/2502.00168), [HTML](https://arxiv.org/abs/2502.00168)
### Authors
Daniel Herrera-Esposito,Johannes Burge
### Background
监督维数约简将标记数据映射到低维特征空间，同时保留分类辨别性。传统方法通常通过最大化特征空间中类间统计度量的不相似性来实现。信息几何为度量类别不相似性提供了另一种框架，可能带来更好的洞察力和新颖的应用。信息几何基于黎曼几何，使用费舍尔信息度量，这是一种局部辨别度量，诱导费舍尔-罗氏距离。在高斯假设下，本文提出了一种监督线性维数约简方法——监督二次特征分析（SQFA），该方法通过最大化类条件分布之间的费舍尔-罗氏距离来实现，以此作为辨别度的良好代理。
### Innovation
本文提出了一种新的监督线性维数约简方法——监督二次特征分析（SQFA），该方法通过最大化类条件分布之间的费舍尔-罗氏距离来实现。此外，本文通过实验证明SQFA可以支持二次判别分析（QDA）的良好分类性能，并为信息几何在机器学习和神经科学中的应用提供了新的框架，为未来的研究奠定了基础。
### Conclusion
SQFA提供了一种新的监督维数约简框架，这种方法在三个真实数据集上支持良好的分类性能。未来研究应探索信息几何在机器学习和神经科学中的更多应用。
## 690. `cs.LG` - 非凸无线异构联邦学习：偏差-方差权衡 [PDF](https://arxiv.org/pdf/2510.26722), [HTML](https://arxiv.org/abs/2510.26722)
### Authors
Muhammad Faraz Ul Abrar,Nicolò Michelusi
### Background
空中（OTA）联邦学习（FL）已广泛被认为是一种利用无线多址信道波形叠加来在单次使用中聚合模型更新的可扩展的范式。现有的OTA-FL设计多通过假设同质性的无线环境（设备间的等路径损耗）或强制零偏移更新来确保收敛性。在异质性的无线环境中，这种设计受限于最弱的设备，并增加更新的方差。尽管先前对带有偏差的OTA-FL的分析主要针对凸目标，但现代人工智能模型通常是高度非凸的。
### Innovation
研究提出了针对无线异构环境的带有随机梯度下降（SGD）的一般光滑非凸OTA-FL更新方法。开发了新型的OTA-FL SGD更新，允许结构化的时间不变模型偏差，同时减少了更新的方差。导出了有限时间内的一致性误差上界，强调了偏差和方差之间的权衡关系。提出了非凸联合OTA功率控制设计，并开发了仅需基站统计CSI的高效相继凸逼近（SCA）算法。实验结果表明，这种基于SCA的设计通过优化偏差加速了收敛，并优于先前的OTA-FL基线，增强了通用性。
### Conclusion
该研究通过开发非凸OTA-FL的SGD更新，实现了偏差和方差之间的最优权衡，并通过实验验证了该方法的有效性，为异构无线环境下的OTA-FL提供了新的优化手段。
## 691. `cs.LG` - 核均值嵌入拓扑：随机核的弱强形式及其对模型学习的影响 [PDF](https://arxiv.org/pdf/2502.13486), [HTML](https://arxiv.org/abs/2502.13486)
### Authors
Naci Saldi,Serdar Yuksel
### Background
本文介绍了一种新型的拓扑结构，称为核均值嵌入拓扑（KME拓扑），适用于随机核函数，并在弱和强形式下进行了定义。这种拓扑在信号空间到概率度量空间（具有希尔伯特空间结构）的Bancher积分函数空间上定义，提供了多样的表述方式。研究了它在放松策略空间中的应用，并探讨了其与Young狭窄拓扑和Borkar（或星号弱）拓扑的关联，揭示了相应的性质。
### Innovation
本文提出了一种新的拓扑结构，既能在弱形式下为放松策略空间提供有用的工具，又能在强形式下为涉及随机核函数的空间提供适当的结构，这有助于理解和分析最优随机控制下的健壮性和学习理论性问题。
### Conclusion
本文展示了该拓扑在弱形式和强形式下均具有的若干性质，使得它适合于研究和模型学习中的最优性及近似性，以及强形式下的稳健性。
## 692. `cs.LG` - 大规模语言模型通过自我确定性进行可扩展的最优N选择 [PDF](https://arxiv.org/pdf/2502.18581), [HTML](https://arxiv.org/abs/2502.18581)
### Authors
Zhewei Kang,Xuandong Zhao,Dawn Song
### Background
最佳的N选择是一种通过增加测试时计算量来提高大型语言模型（LLMs）推理性能的关键技术。当前领先的方法通常使用计算密集型的奖励模型来进行响应评估和选择。然而，无需外部奖励模型的选择替代方法，如自我一致性或通用自我一致性，在处理开放生成任务或有效扩展方面存在局限性。
### Innovation
本文提出了一种新颖且高效的自我确定性度量方法，该方法利用LLM输出的内在概率分布来估计响应质量，而无需外部奖励模型。研究表明，自我确定性（1）与样本数量增加呈有效线性增长关系；（2）与链式思考相结合，可以改进推理性能；（3）可用于传统自我一致性方法无法胜任的开放生成任务。
### Conclusion
实验结果表明，自我确定性为提高LLM推理能力提供了一种实用且高效的途径。该方法在多种推理任务中进行了验证，并在开放生成任务中展示了其优越性，进而证明了其作为一种改进LLM推理能力方法的有效性。相关代码已公开发布于这个链接处。
## 693. `cs.LG` - 生成对抗网络在高维项目因数分析中的应用：一种深度对抗学习算法 [PDF](https://arxiv.org/pdf/2502.10650), [HTML](https://arxiv.org/abs/2502.10650)
### Authors
Nanyu Luo,Feng Ji
### Background
深度学习和表示学习的进步已经改变了项目反应理论（IRT）文献中的因数分析（IFA），使参数估计更高效且更准确。变分自编码器（VAEs）是该领域中模型高维潜在变量的一种非常有效的方法。然而，基于传统VAEs的推断模型限制性较强，仍会妨碍估计性能。为改进传统VAEs在IFA中的表现，AVB算法被引进该研究。通过结合VAEs和生成对抗网络（GANs）的优点，AVB算法引入了辅助判别网络，把估计过程重新定义为一种两玩家对抗博弈，移除了推断模型中受限的标准正态分布假设。
### Innovation
引入了Adversarial Variational Bayes（AVB）算法和Importance-weighted Adversarial Variational Bayes（IWAVB）算法，通过结合VAEs和GANs的优点，改进了潜在变量模型的灵活性和准确性。与传统的VAE相比，AVB和IWAVB能够移除标准正态分布的假设。在仿真数据和实际数据的实验中，IWAVB展现出了超越传统方法（如IWAE）的表现，特别是在处理多模态分布的潜在变量时。
### Conclusion
被提出的IWAVB算法在利用GANs的基础上，展示了扩展项目因数分析处理大规模数据的潜力，有助于潜在心理测量学和多模态数据分析的整合。
## 694. `cs.LG` - 针对实时远程心脏健康评估的单导联ECG参数在设备端计算：一项真实世界验证研究 [PDF](https://arxiv.org/pdf/2502.17499), [HTML](https://arxiv.org/abs/2502.17499)
### Authors
Sumei Fan,Deyun Zhang,Yue Wang,Shijia Geng,Kun Lu,Meng Sang,Weilun Xu,Haixue Wang,Qinghao Zhao,Chuandong Cheng,Peng Wang,Shenda Hong
### Background
在医院之外准确连续地测量心电图（ECG）参数对于实时心脏健康监控和远程医疗至关重要。设备端计算单导联ECG参数允许实时评估，无需依赖集中式数据处理，可以推进个性化和普遍的心脏护理，但仍缺乏广泛的验证工作。这项研究使用HeartVoice-ECG-lite和PTB-XL/PTB-XL+两个数据集来验证设备端算法FeatureDB，以证明其在真实世界中的有效性。
### Innovation
研究验证了设备端算法FeatureDB，通过HeartVoice-ECG-lite和PTB-XL/PTB-XL+两个数据集计算PR、QT和QTc间隔，通过与医生注释的均方绝对误差（MAE）、相关分析和Bland-Altman分析对比，展示了与商业设备相当的性能，特别是对于房室传导阻滞I度（AVBI）和长QT综合症（LQT）的诊断性能。研究证明了单导联设备可以达到医生级别的参数准确性和商业级别的心脏异常检测能力，支持可扩展的远程医疗和分散性心脏筛查，以及社区和门诊中的持续监测。
### Conclusion
FeatureDB通过单导联设备提供与医生级别的参数准确性和商业级别的异常检测能力，支持可扩展的远程医疗、分散性的心脏筛查以及社区和门诊中的持续监测。
## 695. `cs.LG` - DO-IQS: 动态感知的离线逆Q学习在未知收益函数的最优停止问题中 [PDF](https://arxiv.org/pdf/2503.03515), [HTML](https://arxiv.org/abs/2503.03515)
### Authors
Anna Kuchko
### Background
本文探讨了基于停止专家轨迹逆最优停止问题，旨在通过继续和停止收益函数逼近恢复最优停止区域。现有最先进的逆强化学习方法虽然可以恢复Q函数和相应的最优策略，但未能解决最优停止问题特有的挑战。这些挑战包括停止区域附近的稀疏数据、继续收益的非马尔可夫性质、边界条件的恰当处理、风险敏感应用中稳定离线方法的需求，以及缺乏评价指标。
### Innovation
提出了动态感知的离线逆Q学习（DO-IQS），通过近似累计继续收益的同时，结合世界动力学和Q函数，避免了对环境的查询。此外，还提出了基于置信的过采样方法来处理数据稀疏问题。
### Conclusion
在实际和人工数据上展示了我们模型的性能，包括对于关键事件的最佳干预。
## 696. `cs.LG` - Qini Curve Estimation under Clustered Network Interference [PDF](https://arxiv.org/pdf/2502.20097), [HTML](https://arxiv.org/abs/2502.20097)
### Authors
Rickard Karlsson,Bram van den Akker,Felipe Moraes,Hugo M. Proença,Jesse H. Krijthe
### Background
七尼曲线是一种广泛用于评估在分配约束下的治疗政策的有效工具，因为它可以可视化新治疗政策的增量收益与其实施成本之间的关系。标准的七尼曲线估计假设各单位之间没有相互影响，但在公共政策和营销等真实应用中，相互作用却很常见。忽略这些相互作用会导致系统性偏误的七尼曲线，从而高估或低估治疗政策的成本效益。本文即探讨在集群网络相互作用下七尼曲线的估计问题，提出一种形式化的描述和实验设计来解释集群网络相互作用。
### Innovation
本文提出了一种在存在集群网络相互作用的情况下估计七尼曲线的方法。首先，本文提供了一个形式化的框架来描述该问题，并设计了一个实验研究，从而能够处理集群网络相互作用。其次，本文描述了三种不同的估计策略，并提供了选择最合适的策略的指导，强调了固有的偏差-方差权衡。最后，本文引入了一个市场模拟器，可以在典型的电子商务环境中模拟集群网络相互作用，以便实际评估和比较提出的方法。
### Conclusion
本文提出了在存在集群网络相互作用的情况下估计七尼曲线的方法，提供了三个估计策略及其选择建议，并通过市场模拟器在典型的电子商务环境中实际评估了这些策略的有效性。
## 697. `cs.LG` - （如何）语言模型追踪状态？ [PDF](https://arxiv.org/pdf/2503.02854), [HTML](https://arxiv.org/abs/2503.02854)
### Authors
Belinda Z. Li,Zifan Carl Guo,Jacob Andreas
### Background
Transformer语言模型在生成故事和代码等任务中表现出需要跟踪随时间演化的世界中未观察到状态的行为。本文通过研究语言模型在组合排列（即计算一组对象在一系列换位后的顺序）任务中的状态跟踪能力来回答这个问题。排列组合的问题虽然结构简单，但许多其他任务（如有限自动机的仿真和布尔表达式的评估）都能被归约为排列组合的问题，这使得它可以作为一个一般状态跟踪的模型。
### Innovation
论文表明，语言模型在执行此任务时，学习了两种状态跟踪机制。其中一种机制类似于Liu et al.（2023）和Merrill et al.（2024）在近期理论工作中提出的“关联扫描”构造。另一种机制利用一个容易计算的特征（排列符号）部分减少了输出空间，然后通过关联扫描进一步完善。研究还展示了如何通过中间训练任务引导或抑制这些启发式算法使语言模型倾向学习其中一种机制。研究结果表明，无论是预训练还是微调的Transformer语言模型都可以学习实施高效且可解释的状态跟踪机制，并且这些机制的出现可以被预测和控制。
### Conclusion
Transformer语言模型，无论是预训练还是微调，都可以学习实现高效且可解释的状态跟踪机制。通过适当的中间训练任务，可以预测和控制这些机制的出现。这些发现揭示了语言模型在实施复杂任务时的潜在能力，提供了一种理解和控制语言模型行为的新视角。
## 698. `cs.LG` - 关于核偏差的实用介绍：MMD，HSIC & KSD [PDF](https://arxiv.org/pdf/2503.04820), [HTML](https://arxiv.org/abs/2503.04820)
### Authors
Antonin Schrab
### Background
本文提供了一种对核偏差的实际介绍，重点关注最大均值差异（MMD）、希尔伯特-施密特独立性判据（HSIC）和核斯坦差异（KSD）。文中介绍了各种偏差估计器，包括常见的V-统计量和U-统计量，以及更高效的不完全U-统计量形式。作者强调了核带宽选择的重要性，展示了其如何影响偏差估计的行为。
### Innovation
文中介绍了一些自适应估计器，这些估计器结合了使用不同核的多个估计器，以解决核选择的问题。这种方法为解决核选择难题提供了新的思路。
### Conclusion
本文简要回顾了核偏差估计器的主要类型及其特点，并讨论了核带宽选择的关键作用。同时，通过引入自适应估计器，解决了自动选择核的问题，为相关领域的研究提供了新的方法。
## 699. `cs.LG` - 流形学习在高光谱图像处理中的应用 [PDF](https://arxiv.org/pdf/2503.15016), [HTML](https://arxiv.org/abs/2503.15016)
### Authors
Fethi Harkat(EDP, DT),Guillaume Gey(DT),Valérie Perrier(EDP),Kévin Polisano(SVH),Tiphaine Deuberet(DT)
### Background
传统的特征提取和投影技术，如主成分分析，难以充分表示X射线传输多能量（XRT ME）图像，制约了神经网络在决策过程中的性能。高光谱图像（HSI）中的非线性关系使得这些问题更加复杂，传统的技术在捕捉这些复杂关系时存在局限性，进而影响了基于学习的算法的效果。
### Innovation
本文提出了一种基于流形学习的方法，通过使用均匀流形逼近和投影构造邻接图来近似数据集的拓扑结构。这种方法能够捕获数据中的非线性关系，显著提高了机器学习算法的性能，特别是在处理X射线传输光谱学中的高光谱图像时更为有效。该方法不仅保留了数据的整体结构，还增强了特征的可分性，从而提高了分类结果的准确性和鲁棒性。
### Conclusion
所提出的方法有效地提高了高光谱图像处理的性能，通过捕捉非线性关系，增强了特征的可分离性，从而实现了更准确和稳定的分类结果。
## 700. `cs.LG` - 有限的参与者多样性是否阻碍了基于EEG的机器学习？ [PDF](https://arxiv.org/pdf/2503.13497), [HTML](https://arxiv.org/abs/2503.13497)
### Authors
Philipp Bomatter,Henry Gouk
### Background
机器学习在脑电图（EEG）中的应用具有巨大的潜力，可以推进神经科学研究和临床应用的发展。然而，基于EEG的机器学习模型的普适性和鲁棒性通常依赖于训练数据的数量和多样性。EEG记录通常被分割成小段，以增加样本数量，从而提高模型性能。该研究认为这种分割是一种多层次的数据生成过程，并通过大规模实证研究调查了模型性能与总体样本大小和参与者多样性之间的关系。
### Innovation
该研究通过大规模实证研究，将EEG记录分割视为多层次数据生成过程，并探讨了模型性能随总体样本大小和参与者多样性的变化行为。此外，研究还使用相同的框架研究了不同机器学习策略的有效性，以应对有限数据问题，包括数据增强和自监督学习。研究发现，参与者分布的变化严重影响了模型性能的提升，并为此提供了数据收集和机器学习研究的行动指导。
### Conclusion
研究结果表明，模型性能随总体样本大小和参与者多样性变化的表现可能受到参与者分布变化的严重影响，并为此提供了改进数据收集和机器学习研究的策略。研究代码已经在网络上公开。
## 701. `cs.LG` - 目标驱动的动态随机场的框架 [PDF](https://arxiv.org/pdf/2504.16115), [HTML](https://arxiv.org/abs/2504.16115)
### Authors
Yibo Jacky Zhang,Sanmi Koyejo
### Background
场提供了一种描述由相互作用和动态组件组成的复杂系统的灵活方法。特别地，某些动态和随机系统可能表现出旨在实现特定目标的智能行为，我们称之为智能场。然而，由于它们的固有复杂性，目前仍难以对这些系统进行正式的理论描述，并有效将其描述转化为实际应用。
### Innovation
本文提出了三项基本原则，建立了理解智能场的理论框架：完整配置、局部性、目的性。此外，还探讨了从人工智能应用的角度设计此类场的方法。
### Conclusion
本初探旨在为将来在理解和利用此类目标驱动的动态随机场方面的理论发展和实际进步奠定基础。
## 702. `cs.LG` - 细胞作为标记：语言模型与细胞嵌入的高维几何 [PDF](https://arxiv.org/pdf/2503.20278), [HTML](https://arxiv.org/abs/2503.20278)
### Authors
William Gilpin
### Background
单细胞测序技术将细胞映射到一个高维空间，编码其内部活性。最近提出的虚拟细胞模型在此基础上进行了扩展，通过在大规模细胞图谱上进行预训练学习模式来丰富细胞的表示。这篇论文探讨了对自然语言嵌入结构的理解如何影响单细胞数据集的分析。两个领域都通过将数据集划分成嵌入高维向量空间的标记来处理非结构化数据。
### Innovation
本研究将细胞和语言模型进行类比，探讨上下文如何影响嵌入空间的几何结构，以及低维流形如何塑造其鲁棒性和可解释性。通过借鉴基础语言模型的新发展，如解释性探针和上下文内推理，以指导构建细胞图谱和训练虚拟细胞模型的努力。
### Conclusion
研究发现自然语言处理领域的进展为单细胞研究提供了新的方法和视角，特别是一些新的基础模型开发出的工具和概念，为理解细胞空间提供了新的途径。
## 703. `cs.LG` - 通过视觉语言模型实现强化学习中的自动化语义可解释性 [PDF](https://arxiv.org/pdf/2503.16724), [HTML](https://arxiv.org/abs/2503.16724)
### Authors
Zhaoxin Li,Zhang Xi-Jia,Batuhan Altundas,Letian Chen,Rohan Paleja,Matthew Gombolay
### Background
语义可解释性在强化学习（RL）中的应用能够提高决策的透明度和可验证性。实现语义可解释性的要求包括构建由人类可理解概念组成的特征空间以及训练可解释且可验证的策略。然而，通常依赖于手工指定特征空间，这难以在未知环境中泛化。即使可以获取可解释特征，大多数强化学习算法仍使用黑盒模型作为策略，从而阻碍了透明度。
### Innovation
提出了一种名为iTRACE的自动化框架，该框架利用预训练的视觉语言模型（VLM）进行语义特征提取，并通过强化学习训练一种可解释的树形模型。通过构建一个轻量级模型来解决VLM在RL环中的实际运行问题，iTRACE减轻了传统解释性模型对人工注释的依赖。该框架还解决了单独使用VLM的一些关键缺陷，例如其与动作空间的脱节以及无法直接优化策略。在三个领域（Atari游戏、网格世界导航和驾驶）上评估iTRACE的结果显示，iTRACE优于其他解释性策略基线，并在相同的可解释特征空间中达到与黑盒策略相当的性能。
### Conclusion
研究结果表明，iTRACE能够在保留透明性的同时提高强化学习模型的效果，并且在不同的应用场景中展现出了竞争力。
## 704. `cs.LG` - Token Distillation: Attention-aware Input Embeddings For New Tokens [PDF](https://arxiv.org/pdf/2505.20133), [HTML](https://arxiv.org/abs/2505.20133)
### Authors
Konstantin Dobler,Desmond Elliott,Gerard de Melo
### Background
当前的语言模型依赖于预训练时确定的静态词汇表，这可能导致在原词汇表下未被充分代表的领域中出现性能下降和计算成本增加的问题。为了解决这一问题，新词汇表项可以通过适当的初始化加入模型，但现有的嵌入初始化方法通常需要额外的昂贵训练或预训练。
### Innovation
本文提出了Token Distillation方法，通过蒸馏使用原始分词方法得到的表示，快速学习出高质量的新词汇嵌入。实验结果表明，在广泛的应用中，Token Distillation的表现甚至优于强大基线方法。
### Conclusion
实验结果表明，Token Distillation在广泛的应用中表现优越，即使面对强大的基线方法也能获得更好的效果。
## 705. `cs.LG` - DPA: 用于分类数据集测量偏差放大的一站式度量标准 [PDF](https://arxiv.org/pdf/2412.11060), [HTML](https://arxiv.org/abs/2412.11060)
### Authors
Bhanu Tokas,Rahul Nair,Hannah Kerner
### Background
现有的大多数机器学习数据集都存在偏差，当我们将模型训练在这些数据集上时，模型不仅会学习这些偏差，还可能放大这些偏差现象，称为偏差放大。已有的一些基于共现的度量标准被提出用于测量分类数据集中的偏差放大。这些度量标准通过识别保护属性（如性别）与任务（如烹饪）之间的关系来衡量偏差放大，并支持细微差别明显的偏差分析。然而，基于共现的度量标准存在一些局限性，部分度量标准在平衡数据集中无法衡量偏差放大，而其他度量标准无法衡量负面偏差放大。为解决这些问题，最近提出了一种基于预测性的度量标准被称为泄漏放大度量标准（LA），但它无法识别模型放大偏差的方向。因此，提出了一种称作方向预测放大（DPA）的新度量标准，它1. 是方向性的；2. 可以适用于平衡和不平衡的数据集；3. 正确地识别了正面和负面偏差放大。DPA简化了以前需要对模型进行多次评估以验证这三点的需求。此外，与之前的基于预测性的度量标准相比，如LA（泄漏放大度量标准），DPA对攻击者函数的选择更加不敏感，使用一个在有界范围内报告分数的方法，并通过衡量预测性变化来考虑数据集偏差。
### Innovation
提出了一种称作方向预测放大（DPA）的新度量标准，它是方向性的，适用于平衡和不平衡的数据集，并能正确地识别正面和负面偏差放大。DPA简化了以前需要对模型进行多次评估以验证这三点的需求。此外，与之前的基于预测性的度量标准相比，DPA在对攻击者函数选择的敏感性、报告分数范围和考虑数据集偏差方面有改善。
### Conclusion
我们通过知名的数据集如COMPAS（一个表格数据集）、COCO和ImSitu（图像数据集）的实验，展示了DPA是测量分类问题中偏差放大的最可靠度量标准。我们还推出了一站式库，包含主要的偏差放大度量标准进行DPA与其他现有偏差放大度量标准的比较。
## 706. `cs.LG` - HELIOS：高效LLM推理服务的自适应模型和早期退出选择 [PDF](https://arxiv.org/pdf/2504.10724), [HTML](https://arxiv.org/abs/2504.10724)
### Authors
Avinash Kumar,Shashank Nag,Jason Clemons,Lizy John,Poulami Das
### Background
早期退出大语言模型（EE-LLMs）能够通过允许令牌在中间层提前退出来实现高吞吐量推理。然而，这些模型的吞吐量受限于计算和内存节省。现有EE-LLM框架依赖单一模型，因此令牌生成延迟受限于不提前退出且需要 traversing 额外层的令牌。此外，早期退出仅在运行时已知并且依赖于请求。因此，这些框架在运行时加载所有模型层的权重，即使在令牌提前退出时大量权重未被使用。缺乏内存节省限制了批量大小的扩展。
### Innovation
提出了HELIOS框架，旨在提高EE-LLMs的令牌生成延迟和批量大小，从而提高高吞吐量。HELIOS借鉴了两个洞察点：1）不同模型之间的早期退出往往是互补的，一个模型中不提前退出的令牌经常会另一个模型中提前退出。HELIOS采用了多个模型并动态切换以共同最大化提前退出的令牌数量，从而最小化令牌生成延迟；2）即使由于置信度低预测的令牌没有提前退出，它在经过额外层遍历时通常也不会更改。HELIOS会贪婪地允许此类令牌提前退出，并仅加载最有可能被使用的层权重，从而节省内存并通过重新利用节省的内存空间增加批量大小。HELIOS采用了实时分析来准确确定早期退出分布，并通过实时跟踪令牌进行自适应模型切换，以最小化因贪婪模型加载和退出而导致的性能下降。
### Conclusion
我们的评估表明，HELIOS相较于现有EE-LLM框架实现了1.48倍更高的吞吐量和15.14倍更大的批量大小。
## 707. `cs.LG` - 顺序风险控制下的 conformal 对象检测 [PDF](https://arxiv.org/pdf/2505.24038), [HTML](https://arxiv.org/abs/2505.24038)
### Authors
Léo andéol,Luca Mossina,Adrien Mazoyer,Sébastien Gerchinovitz
### Background
近年，对象检测器取得了显著进展并被广泛应用，尤其是在工业领域。然而，它们在安全关键型应用中的部署受到了神经网络固有不可靠性及其模型复杂结构的影响。为此，本研究转向 Conformal Prediction，这是一种后检验的预测不确定性量化方法，能够提供统计上的有效保证，无需依赖于对模型或数据分布的任何先验知识。
### Innovation
该研究的创新之处在于正式定义了Conformal Object Detection (COD)问题，提出了一个新的方法——顺序风险控制定量（SeqCRC），扩展了Conformal Risk Control在两个具有两个参数的顺序任务中的统计保证。此外，该研究还介绍了适用于不同情境和验证需求的新旧损失函数和预测集。
### Conclusion
通过我们提供的工具包，我们进行了大量实验以验证我们的方法的有效性，并强调了权衡和其他实践后果。这些研究结果提醒我们，有序推进风险控制的方法可以在确保模型可靠性的同时提高对象检测的应用范围和安全性。
## 708. `cs.LG` - 通过自适应并行解码加速扩散大语言模型 [PDF](https://arxiv.org/pdf/2506.00413), [HTML](https://arxiv.org/abs/2506.00413)
### Authors
Daniel Israel,Guy Van den Broeck,Aditya Grover
### Background
当前，由于自回归解码要逐个预测标记，因此生成速度成为了大语言模型(LLMs)的一个瓶颈。扩散大语言模型（dLLMs）理论上允许并行预测标记，但是实际应用中很难在不显著牺牲预测质量的情况下达到自回归模型的速度。现有的推测性解码（speculative decoding）方法则旨在通过小型模型抽样来验证大型自回归模型，但这通常难以兼顾高效的生成速度与预测质量之间的平衡。
### Innovation
本文提出了一种新的方法自适应并行解码（APD），能够动态调整并行预测的标记数量。这种方法通过定义dLLM边缘概率与小型辅助自回归模型下的序列联合概率之间的乘法混合来实现，并进一步通过优化KV缓存和限定遮罩输入的大小来提高性能。这种方式提供了三个可调参数来灵活交换吞吐量和预测质量之间的平衡，从而显著提高了模型的生成速度并减少了质量损失。
### Conclusion
实验结果表明，自适应并行解码在下游基准测试中提供了显著更高的吞吐量，同时保持了接近于原始模型的质量水平。
## 709. `cs.LG` - AstroVisBench：天文学领域科学计算与可视化代码基准 [PDF](https://arxiv.org/pdf/2505.20538), [HTML](https://arxiv.org/abs/2505.20538)
### Authors
Sebastian Antony Joseph,Syed Murtaza Husain,Stella S. R. Offner,Stéphanie Juneau,Paul Torrey,Adam S. Bolton,Juan P. Farias,Niall Gaffney,Greg Durrett,Junyi Jessy Li
### Background
大型语言模型（LLMs）在科学领域的应用越来越广泛，包括文献综合、回答研究问题、生成研究想法，甚至进行计算实验。然而，对于这些模型在科学工作流程中生成的可视化结果是否传达了正确的科学见解进行评估仍然是一个挑战。在许多科学领域，通过处理和可视化数据来理解其模式常常能产生新的科学见解。然而，当前的研究并未对此类评估进行评估。本研究提出了AstroVisBench，一个专门用于天文学领域的科学计算和可视化基准。
### Innovation
研究引入了AstroVisBench，这是第一个用于天文学领域的科学计算与可视化基准。AstroVisBench 旨在评估语言模型在两个方面的表现：（1）创建特定于天文学的工作流来处理和分析数据；（2）通过复杂图表来可视化这些工作流的结果。该研究还提出了一种新的“语言模型作为评审员”的工作流程来评估可视化结果，并通过专业天文学家的注释进行了验证。研究结果显示，目前最先进的语言模型在天文学研究中的应用仍然存在显著差距。
### Conclusion
使用AstroVisBench，研究对最先进的语言模型进行了评估，并显示了它们在作为天文学研究助手的有效性方面存在显著差距。研究提供了一种端到端的评估方法，适用于AI科学家，并指出了开发基于可视化的科学工作流程的研究方向，这些工作流程在从物理学到生物学的多个领域中都非常重要。
## 710. `cs.LG` - 不要抛弃婴儿：为什么和如何在ARC中应用深度学习 [PDF](https://arxiv.org/pdf/2506.14276), [HTML](https://arxiv.org/abs/2506.14276)
### Authors
Jack Cole,Mohamed Osman
### Background
 ARC-AGI 挑战对AI系统构成了显著的挑战，尽管在ARC上的表现通常较低，但深度学习仍然是生成高性能（最先进的）神经网络的有效策略。深度学习能够训练出适用于多种模态和任务的技能型神经网络，并从中学习各种领域的抽象。本文强调了继续利用这一范式的必要性，并提出了一种结合在线训练的方法。
### Innovation
本文提出了一种训练方法，从预训练的语言模型开始，并增强其推理能力。具体提出的方法包括Test-Time Fine-Tuning (TTFT) 和Augment Inference Reverse-Augmentation and Vote (AIRV)。这些方法显示出显著的性能提升，AIRV 可提高准确率至多260%，TTFT 可进一步提高300%。早期版本在2023 ARCathon 挑战赛中获得第一名，而在最终版本中，得分达到现有最佳（58%）。通过实验证明了深度学习在ARC中的有效应用，并探讨了增强推理和抽象能力的关键要素。
### Conclusion
研究表明，全心全意利用深度学习的能力来获取新颖抽象可以实现ARC的最先进性能。这些发现强调了在不熟悉的领域构建稳健推理系统的关键成分，突显了提高广义知觉推理的中心机制。
## 711. `cs.LG` - 在线适应性飞行四旋翼在紧密编队中的应用 [PDF](https://arxiv.org/pdf/2506.17488), [HTML](https://arxiv.org/abs/2506.17488)
### Authors
Pei-An Hsieh,Kong Yao Chee,M. Ani Hsieh
### Background
四旋翼在进行紧密编队飞行任务时极具挑战性，因为复杂的气动尾流相互作用可能使个体成员及整个团队失稳。此外，这些气动效应高度非线性且快速变化，使得建模和预测变得困难。为了应对这些挑战，作者提出了一种基于混合专家学习的自适应控制框架L1 KNODE-DW MPC，该框架能够使个体四旋翼准确跟踪轨迹，并在编队飞行过程中适应时变气动相互作用。该研究在两种不同的三四旋翼编队中进行了评估，展示了其优于多种模型预测控制基准的方法。结果表明，该框架能够使三四旋翼团队在飞行过程中保持垂直对齐并保持近距离排列。研究发现，L1自适应模块与精确动力学模型相结合时，能最有效地补偿未建模的扰动。
### Innovation
提出了一种基于混合专家学习的自适应控制框架L1 KNODE-DW MPC，能够使四旋翼在紧密编队飞行中准确跟踪轨迹并适应时变气动相互作用。
### Conclusion
L1 KNODE-DW MPC控制框架在两种不同的三四旋翼编队实验中表现出色，能够使四旋翼团队在飞行过程中保持垂直对齐并保持近距离排列。L1自适应模块与精确动力学模型相结合时，最有效地补偿了未建模的扰动。
## 712. `cs.LG` - 为什么关系学习没有接管世界？ [PDF](https://arxiv.org/pdf/2507.13558), [HTML](https://arxiv.org/abs/2507.13558)
### Authors
David Poole
### Background
文章背景提到了人工智能正通过像素、词和音素建模来主导世界。但实际上，世界由具有属性和彼此关系的对象组成。文章指出，现有的模型集中在这些感知和描述上，而不是对象本身。此时，文本和图像数据占据了大量有价值的数据，但公司大多数重要的数据形式是诸如电子表格、数据库等关系型数据。这些数据未被传统机器学习方法充分研究，但它包含了不能简单解释为数字的产品编号、学生编号、交易编号和其他标识符。为此，一篇文章探讨了研究这类数据的领域，例如关系学习和统计关系AI等的方法及其现状和潜在的改进方向。
### Innovation
文章揭示了即便在涉及关系数据的学习中，尽管已经有一些基于关系学习的实际应用，但其在整个领域的影响力远远不足。文章强调了对关系学习研究的不足，并指出了加强关系学习研究的必要性和迫切性，以提升其在AI领域的地位。
### Conclusion
文章认为现有的一些案例是关系学习应用成功的突破，但在广泛领域内仍面临挑战，文章建议需要更多的研究和发展来提高关系学习的技术水平和应用范围。
## 713. `cs.LG` - NaviAgent: 工具导航图上的层级规划以实现大规模编排 [PDF](https://arxiv.org/pdf/2506.19500), [HTML](https://arxiv.org/abs/2506.19500)
### Authors
Yan Jiang,Hao Zhou,LiZhong GU,Ai Han,TianLong Li
### Background
大型语言模型（LLMs）最近展示了作为功能调用代理的能力，能够调用外部工具以解决超出其静态知识的任务。然而，现有的代理通常逐步调用工具而缺乏任务结构的全局视图，导致错误累积和扩展性限制，尤其是在涉及成千上万的工具时更为明显。
### Innovation
本文提出NaviAgent，这是一种新颖的层级架构，通过基于图的建模工具生态系统将任务规划与工具执行脱钩。NaviAgent在任务规划水平上使基于LLM的代理决定直接响应、澄清用户意图、调用工具链或执行工具输出，确保面对复杂的工具间关系仍然能广泛覆盖交互场景。在执行水平上，持续进化的Tool World Navigation Model（TWNM）编码工具间的结构和行为关系，指导代理生成可扩展且鲁棒的调用序列。通过反馈的实际工具交互，NaviAgent支持计划和执行的闭环优化，超越简单的工具调用转向大规模工具生态系统的适应导航。实验显示，NaviAgent在模型和任务中获得最高的任务成功率，整合TWNM进一步在复杂任务中提升表现高达17个百分点，突显了其在工具链编排中的关键作用。
### Conclusion
NaviAgent通过图建模工具生态系统，实现了任务规划与工具执行的分离，提升了工具调用的可扩展性和鲁棒性，同时通过闭环优化提高了大规模工具生态系统导航的能力。
## 714. `cs.LG` - 电子商务平台上定价与广告算法共谋的分析 [PDF](https://arxiv.org/pdf/2508.08325), [HTML](https://arxiv.org/abs/2508.08325)
### Authors
Hangcheng Zhao,Ron Berman
### Background
当在线卖家利用AI学习算法在电商平台上自动竞标时，担心这些算法会使卖家竞标出高于竞争的价格。这一担忧主要集中在单一维度的价格竞争上。因此，该研究进一步探讨了当卖家同时进行价格和广告决策（即二维决策）时，这种预测是否仍然成立。
### Innovation
研究分析了多代理强化学习中的竞争情况，并利用一个规模较大的数据集提供了实证证据。研究发现，当消费者搜寻成本高时，学习算法能够协调产生低于竞争价格的定价，从而实现消费者、卖家和平台的共赢。这种现象是因为算法学会了降低广告投标竞价，进而降低广告成本，导致价格降低及平台需求扩大。
### Conclusion
研究证明，任何利用价格和广告投标探索的算法都适用于上述结论。实证分析显示，价格水平与估计的消费者搜索成本和算法使用指数之间存在负相关关系。此外，平台的战略响应表明，调整保留价格不会增加平台利润，而调整佣金则可以在保持对卖家和消费者有利的情况下增加平台利润。
## 715. `cs.LG` - TokenBlowUp: 通过指标变换在大语言模型标记空间中解决表现异变 [PDF](https://arxiv.org/pdf/2507.19747), [HTML](https://arxiv.org/abs/2507.19747)
### Authors
Dongfang Zhao
### Background
最近的研究提供了有力的证据，挑战了大型语言模型（LLMs）标记嵌入空间的基础流形假设。这些发现揭示了多义标记周围存在几何奇异性，可能导致表示不稳定。现有方法假设数据流形是光滑的，无法解决这些固有的结构缺陷。本文通过图方案理论的正式化，提出了一种通过奇点的图方案破坏来解决问题的方法，从而实现新的几何景观，以解决这一问题，证明了这一新空间的几何正则化，并阐述了其架构影响，倡导从静态查找转向动态、几何化计算的范式变革。
### Innovation
本文通过引入图方案理论中的图方案破坏策略，为了解决大语言模型中标志嵌入空间的表示奇异性问题，提供了一种新的处理方法。这种方法能够将奇异点替换为其特殊的几何空间，实现表示的去奇性，并构建一个新的几何景观。同时，提出了通过局部几何变换解决此类问题的新方法，与现有方法形成对比，更为适应复杂的数据结构。
### Conclusion
本文构造了一种新的几何化空间，通过奇点的图方案破坏解决了术语嵌入空间中的表示奇异性问题，并通过几何正则化定理证明了该新空间的合理性。同时，阐述了该框架在架构设计上的重要性，推动计算从静态查找向动态几何底层计算转变。
## 716. `cs.LG` - Smooth Flow Matching [PDF](https://arxiv.org/pdf/2508.13831), [HTML](https://arxiv.org/abs/2508.13831)
### Authors
Jianbin Tan,Anru R. Zhang
### Background
功能数据，即在连续域上观测到的光滑随机函数，在生物医学研究、健康信息技术和流行病学等领域越来越常见。然而，功能数据的有效统计分析常常受限于隐私限制、稀疏和不规则采样、无限维以及非正态结构等挑战。
### Innovation
我们引入了一种名为Smooth Flow Matching (SFM)的新框架，该框架针对功能数据的生成建模，无需暴露敏感的原始数据即可实现统计分析。SFM基于流匹配思想，构建了一个半参数 copula 流来生成无限维的功能数据，摆脱了正态性和低秩假设，具有计算效率高、处理不规则观测以及保证生成函数光滑性等优点，为现有深度生成方法不适用的场景提供了实用和灵活的解决方案。通过广泛的模拟研究，我们展示了SFM在合成数据质量和计算效率方面的优势。我们还将SFM应用于从MIMIC-IV患者电子健康记录（EHR）纵向数据库生成临床轨迹数据。
### Conclusion
我们的研究表明，SFM能够产生高质量的替代数据，用于下游统计任务，突显了其在提升EHR数据临床应用价值方面的潜力。
## 717. `cs.LG` - 基于标识符替换的LLM长代码翻译 [PDF](https://arxiv.org/pdf/2510.09045), [HTML](https://arxiv.org/abs/2510.09045)
### Authors
Manojit Chakraborty,Madhusudan Ghosh,Rishabh Gupta
### Background
在软件开发领域，大型语言模型（LLMs）被用来自动化代码翻译任务，即将一种编程语言的源代码转换为另一种语言，同时保留其功能。然而，LLMs在处理长代码片段时经常面临问题，因为这些长代码超出了上下文窗口的限制，导致翻译不够准确。
### Innovation
为了解决这个问题，我们提出了一种新颖的零样本代码翻译方法，该方法结合了标识符替换。通过在翻译过程中使用用户提供的长标识符的通用占位符替代，我们的方法使得LLM能够关注代码的逻辑结构，从而减少标记计数和内存使用量，提高了长代码翻译的有效性和成本效益。
### Conclusion
我们的实验结果表明，我们的方法能够保留语法和层次信息，同时减少标记的数量，生成更准确的翻译结果。
## 718. `cs.LG` - 高效的分布式训练中的混合双向批次和循环渐进展开学习 [PDF](https://arxiv.org/pdf/2509.26092), [HTML](https://arxiv.org/abs/2509.26092)
### Authors
Kuan-Wei Lu,Ding-Yong Hong,Pangfeng Liu,Jan-Jan Wu
### Background
分布式机器学习对于在大型数据集上训练具有众多参数的深度学习模型至关重要。当前的研究主要侧重于利用额外的硬件资源和强大的计算单元来加速训练过程。因此，通常使用较大的批量大小来加快训练。然而，大批次训练可能导致较低的准确性，因为泛化能力较差。
### Innovation
提出了一种基于参数服务器框架的双批处理学习方案，该方法通过利用硬件支持的最大批量大小并结合较小的批量大小来增强模型的泛化能力。此外，为了减轻双批处理学习引起的训练时间延迟，提出了一种循环渐进展开学习方案，在训练过程中逐步增加图像分辨率，从而减少训练时间。结合循环渐进展开学习与双批处理学习，我们的混合方法同时提高了模型的泛化能力和训练效率。
### Conclusion
实验结果表明，与传统训练方法相比，使用ResNet-18，在CIFAR-100上我们的方法提高了3.3%的准确率，同时减少了10.1%的训练时间，并在ImageNet上实现了34.8%的训练时间减少。
## 719. `cs.LG` - 使用超图元学习的博弈论韧性推荐框架：用于协调网络物理微电网 [PDF](https://arxiv.org/pdf/2509.00528), [HTML](https://arxiv.org/abs/2509.00528)
### Authors
S Krishna Niketh,Prasanta K Panigrahi,V Vignesh,Mayukha Pal
### Background
本文介绍了针对辐射型微电网在协调网络物理攻击下的一种基于物理感知的网络韧性框架。背景涉及微电网在遭受网络攻击时的韧性问题，特别是在不同区域之间的能源交换和分布式能源资源调度中如何保持系统安全、降低成本和维持电压稳定性。
### Innovation
创新点在于提出了一种基于超图神经网络（HGNN）增强模型无厌恶元学习（MAML）的方法来快速适应不断变化的防御策略并预测高影响的异常状态。同时，通过一种双层Stackelberg博弈模型表示防御者，优化关键输电线路切换和分散能源资源的调度，进一步优化了负载分发、操作成本和电压稳定性。该方法能够确保所有防御后的系统状态满足网络物理约束。
### Conclusion
该方法首先在包含12个分布式能源资源、8个关键负载和5条输电线路的IEEE 69-节点配电系统上进行了验证，并进一步扩展到了IEEE 123-节点馈线和一个合成的300-节点配电系统。结果显示，对于90%的顶级攻击，提出的防御策略恢复了几乎全额服务，解决了电压异常问题，并确定了馈电2号线路为主要的脆弱通道。通过具体的输电线路预武装策略，该方法还提高了系统的整体韧性，并证明了该框架在更大系统上的可扩展性。
## 720. `cs.LG` - 通过模型融合导航对齐-校准权衡：PareTO-占优前沿 [PDF](https://arxiv.org/pdf/2510.17426), [HTML](https://arxiv.org/abs/2510.17426)
### Authors
Tiancheng Hu,Benjamin Minixhofer,Nigel Collier
### Background
研究背景通常认为，模型对齐后会引发任务准确性的下降，但本文指出，其实还涉及严重失校准，导致模型过于自信、不够可靠，且输出不够多样化。文章表明，这一权衡可以通过简单的后处理干预措施——插值模型对齐前后的权重来有效应对。
### Innovation
论文提出了一种通过模型融合的方法，达到在减少对齐税的同时，模型准确度提升且校准恢复的效果，具体包括：1) 插值插值对齐前后的模型权重，以减轻对齐税；2) 发现模型可以同时提高准确度并恢复校准，超越原始模型表现；3) 提供了一种计算高效的解决方法，使模型更加有能力且可靠。
### Conclusion
本文证明，简单的模型合并提供了一种计算上高效的缓解对齐税的方法，从而生成更加强大且可靠的模型。
## 721. `cs.LG` - ε-Seg: 稀疏监督显微镜数据语义分割 [PDF](https://arxiv.org/pdf/2510.18637), [HTML](https://arxiv.org/abs/2510.18637)
### Authors
Sheida Rahnamai Kordasiabi,Damian Dalle Nogare,Florian Jug
### Background
电子显微镜（EM）图像中的生物样本语义分割仍是生命科学领域的挑战。EM数据捕捉生物结构细节，有时会非常复杂，即使对于人类观察者而言也感到难以处理。现有的稀疏监督方法难以处理这种复杂度下的生物显微图像分割问题。
### Innovation
ε-Seg方法基于分层变分自编码器（HVAEs），使用中心区域掩蔽、稀疏标签对比学习（CL）、高斯混合模型（GMM）先验和无聚类标签预测。该方法通过中心区域掩蔽和填充损失促使模型学习区分目标类的稳健且具代表性的嵌入表示，即使标签稀疏（总图像数据的0.05%或更低）。此外，CL和GMM先验被用于塑造HVAE的潜在空间，使编码输入块倾向于根据我们想要区分的语义类别聚类。最终，ε-Seg方法直接从潜在嵌入中预测类别标签进行语义分割，避免了使用聚类。
### Conclusion
实验结果表明，ε-Seg在复杂的生物图像数据中实现了有竞争力的稀疏监督分割结果，即使只有有限的训练标签可用时也能表现良好，并且该方法也可应用于荧光显微镜数据。
## 722. `cs.LG` - 通过硬件遥测检测机器学习基础设施中的异常 [PDF](https://arxiv.org/pdf/2510.26008), [HTML](https://arxiv.org/abs/2510.26008)
### Authors
Ziji Chen,Steven W. D. Chien,Peng Qian,Noa Zilberman
### Background
现代机器学习（ML）已经发展成为紧密结合的全栈生态系统，结合了硬件、软件、网络和应用程序。许多用户依赖云提供商来获取弹性、隔离且成本效益高的资源。不幸的是，这些作为平台的服务使用虚拟化技术，这意味着操作员对于用户的负载几乎没有见解。这妨碍了操作员对资源进行优化，从而影响了成本效率并增加了执行时间。
### Innovation
本文提出Reveal，这是一种硬件为中心的方法，仅依赖硬件信号——这些信号完全由操作员可访问。通过从系统收集的低级信号，Reveal 通过一个无监督学习管道检测异常。该管道通过分析超过30个流行的ML模型来开发，适用于新兴负载和未知部署模式，以确保系统的适应性。
### Conclusion
使用Reveal，成功地识别了网络和系统配置问题，使DeepSeek模型加速了5.97%。
## 723. `cs.SE` - 量子优化在软件工程中的实证研究：一种系统分析 [PDF](https://arxiv.org/pdf/2510.27113), [HTML](https://arxiv.org/abs/2510.27113)
### Authors
Man Zhang,Yuechen Li,Tao Yue,Kai-Yuan Cai
### Background
最近几年，量子、量子启发式以及混合算法在解决软件工程优化问题方面展现出越来越大的潜力。然而，针对此类问题的最佳实践的实证研究方法尚不完善。
### Innovation
基于最新的系统文献综述发现的关于量子优化的首要研究，从实验设计、超参数设置、案例研究、基准、工具化和度量等方面进行了系统的分析。揭示了当前研究中的关键空白，如报告重复次数、量子脉冲数有限，噪音处理不充分，缺乏标准化评估协议，尤其是在使用量子特定度量方面。
### Conclusion
通过分析，为设计实证研究提供了见解，并强调了更多真实世界和开放案例研究的重要性，以评估和比较三种类型的算法：启发式、量子和混合算法在软件工程优化问题中的成本效益和实际实用性。本研究旨在为设计和开展评估和比较量子、量子启发式和混合算法的研究提供一个概述，并作为初步参考。
## 724. `cs.LG` - 从损失曲率谱系看记忆到推理的变化 [PDF](https://arxiv.org/pdf/2510.24256), [HTML](https://arxiv.org/abs/2510.24256)
### Authors
Jack Merullo,Srihita Vatsavaya,Lucius Bushnaq,Owen Lewis
### Background
在此之前的研究表明，已记忆的训练点的曲率比未记忆的要明显更尖锐，这意味着可以按照权重组件的曲率从高到低排序来揭示这种区分而无需显式的标签。基于这一理论和经验工作的前提，作者研究了如何在变压器模型中表示记忆，并展示了如何通过损失曲率分解来解构记忆。因此，作者提出了一种权重编辑方法，该方法比最近的去学习方法（BalancedSubnet）更有效地抑制未目标的记忆化数据的复述，同时保持较低的困惑度。
### Innovation
作者提出了一种基于损失曲率分解的方法，能够解构变压器模型中的记忆存储。通过抑制低曲率的权重组件，这种方法能够在不影响模型普遍推理能力的前提下更有效率地减少模型的记忆化。此外，作者通过实验证明了这种编辑方法对具体数学和事实检索任务的负面影响，同时保持开放书籍事实检索和一般逻辑推理能力不受影响，并发现了任务数据在低曲率权重组件上的激活强度与任务性能下降的关联性。
### Conclusion
这项工作的成果有助于理解神经网络中内存管理和去除内存的方法。通过分析权重编辑对下游任务的特定和一致的负面影响，作者发现解决数学和事实检索等任务需要在权重空间中利用特定的方向，无论这些单独的数据点是否已被记忆。此研究为消除任务中的特定结构提供了实证支持，这些结构可能正在狭隘地用于解决数学和事实检索等问题。
## 725. `cs.LG` - RELATE: Schema-不可知论Perceiver Encoder for Multimodal Relational Graphs [PDF](https://arxiv.org/pdf/2510.19954), [HTML](https://arxiv.org/abs/2510.19954)
### Authors
Joe Meyer,Divyansha Lachi,Mahmoud Mohammadi,Roshan Reddy Upendra,Eva L. Dyer,Mark Li,Tom Palczewski
### Background
在电子商务、医疗保健和科学研究等领域中，关系型多表数据很常见，这些数据可以自然地表示为具有多模态节点属性的异构时间图。现有的图神经网络（GNNs）依赖于特定模式的特征编码器，需要为每种节点类型和特征列分别设置模块，这限制了其可扩展性和参数共享能力。作为应对，作者引入了RELATE（关系编码器，用于类型化实体的潜编码聚合），这是一种适用于任何通用图神经网络的无模式感知特征编码器。RELATE使用共享的特定模态编码器来处理类别、数值、文本和时间属性，随后通过Perceiver风格的交叉注意模块，将特征聚合为固定大小、不变排列的节点表示。该方法在无模式感知编码器的性能范围内（差距不到3%），同时使参数数量最多减少5倍，支持不同模式下数据集的预训练，为通用图神经网络的相关图数据探索基础模型提供了可能性。
### Innovation
RELATE通过无模式感知的共享模态编码器和Perceiver风格的交叉注意模块，实现了多模态关系图的通用特征编码。该方法无需为每种节点类型和特征列分别设置模块，减少了参数数量，增强了可扩展性。此外，该设计支持不同的数据模式，并为通用图神经网络的多数据集预训练打开了大门，为相关图数据的基础模型铺平了道路。
### Conclusion
RELATE在RelBench基准上的评估结果表明，与特定模式的编码器相比，其性能仅低3%以内，但参数减少最多可达5倍，这表明RELATE能够有效处理多模式关系图，支持通用图神经网络的训练和应用。
## 726. `cs.SE` - MARIA：无ground truth的AI系统边际风险评估框架 [PDF](https://arxiv.org/pdf/2510.27163), [HTML](https://arxiv.org/abs/2510.27163)
### Authors
Jieshan Chen,Suyu Ma,Qinghua Lu,Sung Une Lee,Liming Zhu
### Background
在部署AI系统替代现有流程之前，必须对比新旧系统以确保安全性提升而无额外风险。传统的评估方法依赖于两个系统的绝对准确性，但在许多情况下，由于结果延迟、不可知性、高成本或数据不全等问题，的真实数据往往不可用，尤其是对于那些被传统认为安全的长期系统。因此，更实际的解决方法不是计算绝对风险，而是计算系统之间的差异。由此，研究人员 proposal 了一个边际风险评估框架，该框架避免了对真实数据的依赖或绝对风险的计算。
### Innovation
提出了一个边际风险评估框架（MARIA），该框架通过提供三种相对评估方法（可预测性、能力和交互主导性）来实现对真实数据的需求减少，帮助软件团队识别AI在哪种情况下能提高结果，引入哪些新风险，并负责任地采纳这些系统，从而实现从绝对评估到相对评估的转变，为软件团队提供了实际指导
### Conclusion
该研究通过提案的边际风险评估框架，能够为软件团队提供如何负责任地采纳AI系统的实际指导：识别AI改进之处、识别引入的新风险，并采取合适的策略。
## 727. `cs.LG` - MMEdge：通过分步传感器和编码加速设备上的多模态推理 [PDF](https://arxiv.org/pdf/2510.25327), [HTML](https://arxiv.org/abs/2510.25327)
### Authors
Runxi Huang,Mingxuan Yu,Mingyu Tsoi,Xiaomin Ouyang
### Background
实时的多模态推理对于诸如自动驾驶、人机交互和移动健康等应用程序至关重要。然而，先前的工作往往忽略了传感动态和模型执行之间的紧密耦合，以及复杂的跨模态依赖关系。
### Innovation
本文提出了一种基于分步传感和编码的新设备多模态推理框架MMEdge。MMEdge将整个推理过程分解为一系列细粒度的传感和编码单元，使计算能够随着数据的到达逐步进行。同时，MMEdge还引入了一个轻量级但有效的时序聚合模块，以捕获不同分步单元之间的丰富时序动态，从而保持准确性能。此外，该分步设计还为细粒度的跨模态优化和推理过程中的早期决策提供了便利。为了进一步在资源波动和输入数据复杂性下增强系统性能，MMEdge集成了一个自适应多模态配置优化器，该优化器根据延迟约束动态选择每个模态的最佳传感器和模型配置，以及一个跨模态推测性跳过机制，在早期预测达到足够信心时跳过更慢模态的未来单元。
### Conclusion
我们使用两个公开的多模态数据集评估了MMEdge，并将其部署在一个现实世界的基于无人机（UAV）的多模态测试台上。结果显示，MMEdge在端到端延迟显著减少的同时，仍能够在各种系统和数据动态下保持高任务准确性。
## 728. `cs.SE` - 通过低代码实现数据感知业务流程中的理论与实践结合 [PDF](https://arxiv.org/pdf/2510.27229), [HTML](https://arxiv.org/abs/2510.27229)
### Authors
Ali Nour Eldin,Benjamin Dalmas,Walid Gaaloul
### Background
近年来，对业务流程模型的验证越来越受到关注。尽管这些模型缺乏形式化描述，但它们在工业和学术界中被广泛采用。由于数据和过程是同一事物的两面，而数据对于执行业务过程模型至关重要，因此需要对业务流程建模语言的执行语义进行形式化。BPMN-ProX是一种低代码测试框架，显著提高了数据感知BPMN的验证能力。
### Innovation
BPMN-ProX 是一个低代码平台，它通过集成高级数据处理和先进的验证机制（通过最先进的模型检查器）来解决非技术专家与专业人士之间的鸿沟。该平台结合理论验证与实际建模，促进了更多灵活、可靠和用户中心的业务过程管理。
### Conclusion
BPMN-ProX 通过数据注入 BPMN，实现了低代码环境下的数据感知业务流程验证。它将先进的验证机制与用户友好的低代码平台相结合，增强了业务流程模型的验证性，使其更接近实际应用。
## 729. `cs.SE` - Agentic LLMs for REST API Test Amplification: A Comparative Study Across Cloud Applications [PDF](https://arxiv.org/pdf/2510.27417), [HTML](https://arxiv.org/abs/2510.27417)
### Authors
Jarne Besjes,Robbe Nooyens,Tolgahan Bardakci,Mutlu Beyazit,Serge Demeyer
### Background
Representational State Transfer (REST) APIs are essential in modern cloud native systems, and ensuring their reliability necessitates automated test suites covering various and boundary-level behaviors. However, designing such test cases is a challenging and resource-intensive task.
### Innovation
该研究扩展了基于大型语言模型（LLM）的测试放大前期工作，评估了单一代理和多代理配置在四个额外的云应用程序中的效果。这表明，具备智能的LLM系统能够跨越异构API架构有效地泛化，增加端点和参数覆盖范围，并揭示缺陷。同时，详细分析计算成本、运行时间和能源消耗，突显准确性、可扩展性和效率之间的权衡。
### Conclusion
这些发现强调了基于LLM驱动的测试放大的潜在价值，可以促进复杂云环境中REST API测试的自动化和可持续性。
## 730. `cs.SE` - 古老代码，现代法官：低数据情景下的元验证 [PDF](https://arxiv.org/pdf/2510.27244), [HTML](https://arxiv.org/abs/2510.27244)
### Authors
Ora Nova Fandina,Gal Amram,Eitan Farchi,Shmulik Froimovich,Raviv Gal,Wesam Ibraheem,Rami Katan,Alice Podolsky,Orna Raz
### Background
在使用COBOL、PL/I和REXX等遗产语言进行应用现代化的过程中，专家资源和高质量的人类评估数据都面临严重短缺。虽然大型语言模型作为法官（LaaJ）提供了一种可扩展的替代专家审核的方法，但它们的可靠性必须得到验证，才能在高风险的工作流程中被信任。没有原理性的验证，组织可能会陷入一个循环评估的陷阱，其中未经验证的LaaJ被用来评估模型输出，这可能会巩固不可靠的判断并影响下游部署决策。尽管已经提出了多种自动化的LaaJ验证方法，但与人类判断的对齐仍然是最常用和概念性较强的验证策略。在许多现实领域中，人类标记的评估数据极其有限，使得评估LaaJ与人类判断对齐的效果变得困难。
### Innovation
我们引入了一个名为SparseAlign的形式框架，专门用于通过稀疏的人类标记数据评估LaaJ的对齐情况。SparseAlign结合了一个新颖的成对置信度概念和一个得分敏感的对齐度量，该度量同时捕捉排名一致性和得分接近性，即使在传统统计方法因标注样本有限而无效的情况下，也能实现可靠的人类评审者选择。
### Conclusion
SparseAlign被应用于COBOL代码解释中，精选出的对齐评分最高的评审者被整合到评估工作流程中，指导模型的发布决策。我们通过一个实际案例研究了四个LaaJ，展示了SparseAlign在实际评估场景中的实用性。
## 731. `cs.SE` - 面向服务架构的跨平台功能高效集成 [PDF](https://arxiv.org/pdf/2510.27344), [HTML](https://arxiv.org/abs/2510.27344)
### Authors
Thomas Schulik,Viswanatha Reddy Batchu,Ramesh Kumar Dharmapuri,Saran Gundlapalli,Parthasarathy Nadarajan,Philipp Pelcz
### Background
汽车产业正经历从电子/电子（E/E）和软件架构的重大变革，主要是由于车辆内技术栈复杂性的增加。这种复杂性推动了软件定义汽车（SDVs）的发展，使汽车的E/E架构从分散配置的多个电子控制单元（ECUs）向更集成的配置转变，包含更少的ECUs、域控制器、网关和高性能计算机（HPCs）。这一转变以及其他原因导致了诸如AUTOSAR Classic、AUTOSAR Adaptive和RO S 2原型框架等异构软件平台的出现。因此，开发能够在不同硬件和平台/中间件上运行且保持开发和集成效率的应用程序变得至关重要。
### Innovation
本文提出了一种应用开发和集成概念，旨在支持软件作为产品（SaaP）的应用开发，同时确保其在多个软件架构平台上的高效集成。此概念强调应用的设计和接口标准的硬件及软件平台无关性，以及描述应用程序及相应的中间件以机器可读格式呈现，以辅助应用的集成。此外还开发了工具以支持开发和集成过程的部分自动化。
### Conclusion
通过一个实际应用在AUTOSAR Adaptive和RO S 2上的例子，证明了该方法的有效性。实验结果表明，该整体概念提高了应用开发和集成的效率。
## 732. `cs.SE` - 增强软件产品线中的机器学习组件 [PDF](https://arxiv.org/pdf/2510.27640), [HTML](https://arxiv.org/abs/2510.27640)
### Authors
Luz-Viviana Cobaleda,Julián Carvajal,Paola Vallejo,Andrés López,Raúl Mazo
### Background
现代软件系统越来越多地集成机器学习（ML），因为其在数据驱动决策方面的进步，但这种集成为软件工程带来了重大挑战，特别是在软件产品线（SPLs）中，由于包括了ML组件，这使得管理变异性与重用变得更加复杂。现有的方法虽然在处理SPL变异性管理和孤立系统中ML组件集成方面有所进展，但在两个领域的交集方面仍然缺乏探索。特别地，现有的技术对处理包含ML组件的SPLs的变异性建模和管理系统支持不足。
### Innovation
本文提出了一种结构化的框架，旨在扩展软件产品线工程，促进ML组件的集成。该框架通过使SPL能够系统地建模变异性与重用来促进ML功能的设计。这一框架部分通过VariaMos工具实现。
### Conclusion
通过引入一种新的框架，本文为处理包含ML组件的SPL的变异性与重用问题提供了解决方案，并通过半实现的VariaMos工具证明了这一点。
## 733. `cs.SE` - 针对基于大规模语言模型的代码漏洞检测选择少量示例的方法 [PDF](https://arxiv.org/pdf/2510.27675), [HTML](https://arxiv.org/abs/2510.27675)
### Authors
Md Abdul Hannan,Ronghao Ni,Chi Zhang,Limin Jia,Ravi Mangal,Corina S. Pasareanu
### Background
大规模语言模型（LLMs）在编程任务中展示了令人印象深刻的能力，包括总结、翻译、完成和代码生成。然而，检测代码漏洞仍然是一个具有挑战性的任务。一种有效的方式是通过在上下文学习（ICL）中提供与查询相似的少量示例及其正确答案，可以提高LLM生成正确解决方案的能力。但选择适当的少量示例对改进模型性能至关重要。
### Innovation
本文探讨了两种选择用于代码漏洞检测的ICL中少量示例的标准。第一种标准考虑LLM是否在样本上一贯出错，认为样本是LLM性能的指示，有助于判断其作为IHC示例的有用性。第二种标准则基于与待查询程序相似度高的邻居样本选择少量示例。通过在多个数据集上使用开源模型进行评估，研究了这些标准单独及组合使用的效果。
### Conclusion
通过实际评估表明，这两次标准可以单独或者结合使用来提升代码漏洞检测中的LLM表现。这种基于选择恰当示例的学习方法在代码漏洞检测任务中展示了巨大的潜力。
## 734. `cs.SE` - 向量衡量算法相似性 [PDF](https://arxiv.org/pdf/2510.27063), [HTML](https://arxiv.org/abs/2510.27063)
### Authors
Shairoz Sohail,Taher Ali
### Background
在面对同一个问题时，可能有多种不同的算法。尽管在全方面的理论上确定两个算法是否具有实质性差异是不可计算的，且在实验中由于相似性的不同定义而变得模糊，但在许多应用场景（如克隆检测或程序合成）中，需要一种实践性强且一致的相似性度量标准。因此，论文回顾了现有的算法等价性和相似性概念，并引入了EMOC框架，该框架将算法实现嵌入到适合下游任务的功能空间中。
### Innovation
论文提出了EMOC（Evaluation-Memory-Operations-Complexity）框架，该框架将算法实现嵌入到一个特征空间中，便于进行聚类、分类、近似重复检测以及计算程序多样性等下游任务的处理。更重要的是，作者推出了一个包含经验证的Python实现的PACD数据集，用于验证EMOC的有效性。
### Conclusion
论文通过EMOC框架支持了算法类型的聚类和分类，近似重复的检测以及量化LLM生成程序的多样性。EMOC框架、PACD数据集以及相关的计算工具的开源发布，旨在促进算法相似性领域的可重复性和未来研究工作。
## 735. `cs.SE` - CodeAlignBench：评估代码生成模型在开发人员首选代码调整方面的表现 [PDF](https://arxiv.org/pdf/2510.27565), [HTML](https://arxiv.org/abs/2510.27565)
### Authors
Forough Mehralian,Ryan Shar,James R. Rae,Alireza Hashemi
### Background
随着大型语言模型在生成代码方面的能力不断增强，评估其性能仍然是一项复杂且不断发展的挑战。现有的基准测试主要关注功能正确性，而忽略了真实世界编码任务的多样性和开发人员的期望。因此，本文引入了一个多语言基准测试，它评估LLM的指令遵循能力，并且可以针对任何独立的编码问题进行扩展。该基准测试在两个关键设置中评估指令遵循：一是遵循初始问题中预定义的约束，二是基于后续指令进行改进的能力。对于本文的分析，我们使用来自LiveBench的编程任务进行了实证测试，这些任务还自动从Python翻译到Java和JavaScript。自动化的基准测试揭示了模型在指令遵循多个维度上的不同表现水平。基准测试管道提供了一个更全面的代码生成模型评估，突显了它们在不同语言和生成目标下的优势和局限性。
### Innovation
本文提出的多语言基准测试CodeAlignBench，旨在评估大型语言模型在遵循开发者指令方面的表现。它特别关注实际编码任务中的多样性，以及模型在多语言环境下的代码生成能力。基准测试结合了预定义约束和基于后续指令的改进能力的评估。通过与LiveBench的任务进行对比分析，揭示了不同模型在不同编程语言和复杂任务上的表现差异。
### Conclusion
基准测试管道提供了一个更加全面的代码生成模型评估方法，突显了模型在不同语言和生成目标下的优势和局限性。CodeAlignBench有助于更好地理解现有的代码生成模型，并为未来的研究提供了更全面的评估框架。
## 736. `cs.SE` - RepoMasterEval：基于真实仓库评估代码补全 [PDF](https://arxiv.org/pdf/2408.03519), [HTML](https://arxiv.org/abs/2408.03519)
### Authors
Qinyun Wu,Chao Peng,Pengfei Gao,Ruida Hu,Haoyu Gan,Bo Jiang,Jinhe Tang,Zhiwen Deng,Zhanming Guan,Cuiyun Gao,Xia Liu,Ping Yang
### Background
随着软件开发对自动化代码补全工具的依赖日益增强，建立全面的评估基准变得至关重要。现有基准主要侧重于函数和类级别的代码补全，通过文本描述来提示模型。然而，在实际开发中，描述性提示较为罕见，代码补全可以在函数或代码块的中间发生，这使得现有评估基准与代码补全工具的实际应用场景严重脱节。
### Innovation
本文提出了RepoMasterEval，这是一种基于真实码库构建的新颖基准，用于评估代码完成模型。每一个基准数据都是通过从源码文件中遮盖一个代码片段（真实值）并结合现有的测试套件生成的。为了提高补全代码的测试准确性，作者采用突变测试来测量测试用例的效果，并对低突变评分的测试套件手工制作新的测试用例。
### Conclusion
针对10种最新模型的实证研究表明，测试论证对于提高基准的准确度至关重要，RepoMasterEval能够更好地反映模型在真实场景中的性能差异。repoMasterEval的部署还表明，该基准可以提供模型训练过程中准确的反馈，且得分与模型在实际中的表现高度相关。
## 737. `cs.SE` - 理解开源社区中的集体社会行为：协同编辑网络上的活动级联分析 [PDF](https://arxiv.org/pdf/2509.26173), [HTML](https://arxiv.org/abs/2509.26173)
### Authors
Lisi Qarkaxhija,Maximilian Capraro,Stefan Menzel,Bernhard Sendhoff,Ingo Scholtes
### Background
理解软件开发者的集体社会行为对于建模和预测开源软件（OSS）社区的长期动态和可持续性至关重要。因此，通过分析开发者的时间活动模式，揭示提交贡献的固有的‘突发性’性质。为了探究这一现象背后的社交机制，采用基于网络的建模框架捕捉开发者间的交互，通过协同编辑网络。
### Innovation
开发了一种方法，用大数据集分析50个主要的OSS社区中的活动级联，即开发者活动在底层协同编辑网络中的传播。结果显示，活动级联在超过一半的研究项目中是统计显著的现象。进一步展示了我们的见解可以用于开发一种简单实用的开发者流失预测方法。
### Conclusion
揭示了开源社区中集体社会动态的涌现机制，并强调了活动级联对理解开发者流失和保留的重要性。
## 738. `cs.SE` - 小变化，大麻烦：揭开PyPI生态系统中许可证变体不兼容检测的神秘面纱并进行解析 [PDF](https://arxiv.org/pdf/2507.14594), [HTML](https://arxiv.org/abs/2507.14594)
### Authors
Weiwei Xu,Hengzhi Ye,Kai Gao,Minghui Zhou
### Background
开源许可证为软件重用提供了法律基础，但许可证变体（包括修改的标准许可证和自创的替代品）引入了显著的合规复杂性。尽管这些变体很常见且影响重大，但它们在现代软件系统中的理解不足，现有工具未能考虑到它们的存在，导致在许可证分析的有效性和效率上带来巨大挑战。
### Innovation
基于研究发现，我们引入了LV-Parser，一种利用差异技术和大规模语言模型进行高效许可证变体分析的方法，以及LV-Compat，一种自动化检测软件依赖网络中许可证不兼容性的管道。评估结果表明，LV-Parser的准确率为0.936，降低了30%的计算成本，而LV-Compat能够比现有方法多识别5.2倍的不兼容包，精度为0.98。
### Conclusion
这项工作不仅提供了软件打包生态系统中许可证变体的第一个实证研究，也为开发者和组织提供了导航开源许可证复杂领域的实用工具。
## 739. `cs.SE` - 关于可互换深度强化学习实现的错误假设 [PDF](https://arxiv.org/pdf/2503.22575), [HTML](https://arxiv.org/abs/2503.22575)
### Authors
Rajdeep Singh Hundal,Yan Xiao,Xiaochun Cao,Jin Song Dong,Manuel Rigger
### Background
深度强化学习(DRL)是一种人工智能范式，其中代理使用神经网络学习在给定环境中采取何种行动。DRL最近因其能够解决诸如驾驶模拟器、3D机器人控制和多人线上战斗竞技场视频游戏等复杂环境而受到关注。尽管有许多最先进的算法如Deep Q-Network (DQN) 和Proximal Policy Optimization (PPO)的实现，现有研究通常假设相同算法的实现一致且互换。然而，这些研究忽略了不同实现可能存在的差异，可能导致错误的结论。因此，本文通过差异测试方法研究这些实现中的不一致性及其对性能和后续研究的影响，发现这些实现并非互换，而是存在显著差异。
### Innovation
通过差异测试方法研究深度强化学习实现的不一致性，发现这些算法的不同实现并非互换，表明它们之间存在显著差异。具体而言，本文测试了五个PPO实现，发现三中实现中仅有50%的试次实现了超人类性能，而另外两种实现仅在试次中实现了不到15%的超人类性能。通过对代码的细致分析，确定代码层面的不一致性是导致这些差异的主要原因。最后，复制前人的实验，证明这种实现互换性的假设可能影响实验结果。
### Conclusion
研究表明，深度强化学习中的实现并非互换，必须改变对实现使用的做法。
## 740. `cs.SE` - 你的构建脚本很臭:构建脚本中的代码异味状况 [PDF](https://arxiv.org/pdf/2506.17948), [HTML](https://arxiv.org/abs/2506.17948)
### Authors
Mahzabin Tamanna,Yash Chandrani,Matthew Burrows,Brandon Wroblewski,Laurie Williams,Dominik Wermke
### Background
构建脚本自动化了从源代码编译、依赖管理、测试运行到软件打包成可部署构件的过程。脚本在现代软件开发管道中被广泛应用，旨在简化测试和交付过程。尽管脚本开发过程中可能会无意中引入代码异味，即常见的不良编码实践模式，这可能导致构建失败或增加风险和技术债务。
### Innovation
该研究采用了混合方法，结合定性和定量分析，首先通过定量分析2000个GitHub问题来识别常见代码异味，并开发了一个名为Sniffer的静态分析工具，用于自动检测Maven、Gradle、CMake和Make文件中的代码异味。用户研究显示，Sniffer具有更高的精度、召回率和F分数。共识别出13类代码异味，其中最常见的是Maven中的不安全URL，以及Gradle和CMake中的硬编码路径/URL，而通配符使用是Makefile中最常见的异味。此外，硬编码路径/URL和重复，以及不一致的依赖管理与空或不完整标签之间存在紧密关联，这可能揭示构建脚本结构和维护实践中的潜在问题。
### Conclusion
该研究发现了构建脚本中的多种代码异味，并通过Sniffer工具提供了自动检测机制，该工具在准确性、召回率和F分数方面表现优越。未来工作可以进一步优化Sniffer工具的性能，以更好地支持构建脚本的质量提升。
## 741. `cs.SE` - LLM-Guided Scenario-based GUI Testing [PDF](https://arxiv.org/pdf/2506.05079), [HTML](https://arxiv.org/abs/2506.05079)
### Authors
Shengcheng Yu,Yuchen Ling,Chunrong Fang,Quan Zhou,Yi Zhao,Chunyang Chen,Shaomin Zhu,Zhenyu Chen
### Background
随着移动应用程序用户界面（GUI）在用户与应用程序交互中的重要作用凸显，自动化的GUI测试方法虽已发展多样，但仍存在显著的不足，主要表现为这些方法侧重于一般性的探索，而非完成特定的测试场景，从而忽略了关键功能的测试。鉴于此，研究者们借鉴了手动测试中以业务逻辑为驱动的场景为基础的做法，提出了利用大语言模型（LLM）理解GUI的语义和上下文相关性的方法，并基于此提出了名为ScenGen的多代理协作引导的基于场景的GUI测试框架，该框架旨在生成与业务逻辑高度相关的测试案例并改进自动化GUI测试的完整性。
### Innovation
该研究提出了ScenGen，一个由大语言模型引导的多代理协作的基于场景的GUI测试框架。ScenGen通过五个模块（观察者、决策者、执行者、监督者和记录者）模拟并自动化了手动测试的阶段。观察者负责解释和结构化GUI元素，决策者根据LLM的指导为完成特定目标确定目标元素和操作，执行者执行这些操作，监督者确保行动与预期目标一致，记录者跟踪GUI操作并将这些信息作为知识库用于后续决策和错误检测。ScenGen能够有效生成与业务逻辑相关的场景驱动的GUI测试案例，提高了自动化GUI测试的全面性。
### Conclusion
通过ScenGen框架，该研究成功地实现了LLM协作下的场景驱动的GUI测试案例生成，提高了测试案例与业务逻辑的相关性和自动GUI测试的完整性。这对于提高移动应用软件质量具有重要意义。
## 742. `cs.SE` - 利用标识符替换的基于LLM的长代码翻译 [PDF](https://arxiv.org/pdf/2510.09045), [HTML](https://arxiv.org/abs/2510.09045)
### Authors
Manojit Chakraborty,Madhusudan Ghosh,Rishabh Gupta
### Background
在软件开发领域，LLM（大型语言模型）被用来自动化代码翻译任务，即将一种编程语言的源代码转换为另一种语言，同时保持其功能。然而，这些模型在处理长代码时经常遇到问题，因为长代码往往超出上下文窗口的限制，导致翻译不准确。现有的解决方法对此类问题效果不佳，需要新的解决方案来提高长代码翻译的准确性和效率。
### Innovation
本文提出了一种新型的零样本代码翻译方法，该方法通过在翻译过程中用通用占位符替换用户指定的长标识符，减轻LLM处理长代码时的负担。这种方法显著降低了token计数和内存使用，使LLM能够更关注代码的逻辑结构，从而提高了长代码翻译的效率和成本效益。实验结果表明，该方法能够保留语法规则和层级结构信息，同时减少token数量，生成高质量的翻译结果。
### Conclusion
实验结果证明了本文方法的有效性，通过减少token数量和优化内存使用，解决了长代码翻译中的准确性问题，提高了LLM在代码翻译任务中的效率和成本效益。
## 743. `cs.SE` - 伪代码模拟语义翻译能否帮助LLM进行代码翻译？基于伪代码的一项研究 [PDF](https://arxiv.org/pdf/2510.00920), [HTML](https://arxiv.org/abs/2510.00920)
### Authors
Songqiang Chen,Congying Xu,Jingyi Chen,Jialun Cao,Jiarong Wu,Shing-Chi Cheung
### Background
大型语言模型（LLMs）在代码翻译方面显示出了巨大的潜力。然而，使用常见的直接代码到代码转换方法进行准确翻译仍然具有挑战性，这种方法将程序一次性转换为目标编程语言（PL）。受将中间步骤引入以指导LLMs解决困难任务的成功启发，本文探讨了基于伪代码的代码翻译方法。这种方法通过首先将程序的意图和逻辑解释为伪代码，然后再用目标PL实现，模仿了人类语义翻译的过程。尽管这种方法有助于翻译直接翻译困难的程序，但其有效性和局限性仍需进一步探索。
### Innovation
本文通过一项实证研究探讨基于伪代码的代码翻译方法的有效性，以增强直接翻译方法，揭示其有效用途，并识别阻碍其潜在好处的限制。研究在6种编程语言上的9,690个翻译任务中比较了直接翻译和基于伪代码的翻译方法，采用5个流行的大型语言模型，证明伪代码基于的翻译能有效补充直接翻译，尤其是在从灵活的语言翻译到严格的语言或处理低资源的Rust时。
### Conclusion
基于这些发现，本文建议采用结合两种方法互补优势的策略来提高代码翻译的准确性。伪代码基于的翻译也有助于拆分复杂程序的翻译并减轻对原程序详细实现的干扰，但也存在伪代码不正确、不完整或含糊不清的限制。
## 744. `cs.SE` - 隐私设计：一种需求工程方法实现GDPR与软件工程规范的协调 [PDF](https://arxiv.org/pdf/2510.21591), [HTML](https://arxiv.org/abs/2510.21591)
### Authors
Oleksandr Kosenkov,Ehsan Zabardast,Davide Fucci,Daniel Mendez,Michael Unterkalmsteiner
### Background
GDPR下的软件系统合规需要一致的规范和系统规范，确保实现隐私设计（PbD）。然而，现有方法未充分考虑GDPR在问题与解决方案空间之间的复杂交集。研究通过文献回顾和访谈了解从业者的视角，旨在探索联合需求和系统规范的需求，并提出应对需求的方法。
### Innovation
提出了基于原始法律概念建模GDPR内容的方法，以支持规范目标（如法律知识捕获、规范透明性和可追溯性）。该研究强调在软件工程生命周期的不同抽象层次上满足GDPR需求的重要性，确保隐私设计。同时也指出了方法未来有效实施的具体需求。
### Conclusion
GDPR下的需求需要在整个软件工程生命周期的不同抽象层次上解决，以实现隐私设计。根据GDPR条款中捕获的法律知识应该在规范中体现，以满足不同利益相关者的合规需求。尽管我们的方法证实了应对实践需求的适用性，但仍然需要解决未来有效实施的具体需求。
## 745. `cs.SE` - 从人类生成到AI生成：笔记竞赛中比较GenAI [PDF](https://arxiv.org/pdf/2510.18430), [HTML](https://arxiv.org/abs/2510.18430)
### Authors
Tasha Settewong,Youmei Fan,Raula Gaikovina Kula,Kenichi Matsumoto
### Background
计算笔记本已经成为数据科学家和从业者进行分析和分享结果的首选工具。笔记本结合了脚本和文档。随着生成式人工智能（GenAI）技术的出现，区分人类编写和GenAI编写的特点变得尤为重要，尤其是在竞争环境中。本文通过研究代码和文档的特点，对比了人类和GenAI在笔记中的编码和文档活动。我们首先分析了25个特征在人类获奖的Kaggle笔记本中的差异，发现了获奖者主要通过更长、更详细的文档进行区分。我们还分析了人类编写和GenAI笔记本之间的差异。结果显示，尽管GenAI笔记本在代码质量上得分更高（按代码臭味和技术债务等指标衡量），但人类编写笔记在结构多样性、复杂性和解决复杂问题的新颖方法上更具优势。
### Innovation
本研究通过三个案例分析，探索了在笔记中人类和GenAI的潜在优势，在代码质量方面GenAI表现出色，但在结构多样化、复杂度和创新性解决方案方面，人类编写的文章表现出色。
### Conclusion
这些发现为我们奠定了基础，明确了GenAI在笔记本中的潜在用途，强调了如何通过进一步研究最大化人类与AI协作的潜力。
## 746. `cs.SE` - 基于过程挖掘的软件开发工作流的分析与预测系统 [PDF](https://arxiv.org/pdf/2510.25935), [HTML](https://arxiv.org/abs/2510.25935)
### Authors
Antía Dorado,Iván Folgueira,Sofía Martín,Gonzalo Martín,Álvaro Porto,Alejandro Ramos,John Wallace
### Background
在软件开发流程中，确保按时完成开发任务是项目管理的重要一环。然而，由于开发过程的复杂性和不确定性，往往难以准确预测哪些开发任务可能会延误。本文介绍了一个名为CodeSight的系统，该系统通过直接从GitHub捕获开发和部署数据，将其转换为过程挖掘日志，以便进行详细分析。然后，系统生成了有关PR活动模式和工作流程效率的指标和仪表板，从而提供了可操作的见解。
### Innovation
CodeSight系统的关键创新在于它利用一个基于LSTM模型的预测机制，该模型可以基于序列活动轨迹和静态特征预测剩余的PR解决时间。这种预测机制使得在问题成为严重问题之前就能早期识别潜在的延误情况。
### Conclusion
实验结果显示，CodeSight系统在预测截止日期合规性方面具有高精度和F1评分，证明了将过程挖掘与机器学习相结合可以为项目管理提供一种前瞻性的方法。该系统促进了灵活和有效的软件项目管理。
## 747. `cs.SE` - 软件开发职业中多元化视角下的歧视问题 [PDF](https://arxiv.org/pdf/2510.22457), [HTML](https://arxiv.org/abs/2510.22457)
### Authors
Shalini Chakraborty,Sebastian Baltes
### Background
关于软件工程领域的多元性和包容性的对话通常侧重于性别和种族差异。然而，2025年开发者状态调查发现，其他形式的歧视同样普遍但受到的关注较少。这些包括基于年龄、政治观点、生理障碍或认知差异如神经多样性等问题。研究通过二次分析800份开放式问卷调查，来探讨感知到的歧视模式，相关的挑战和负面影响。研究覆盖了多个身份维度，包括年龄、性别、种族和残疾。研究表明，年龄和性别相关的歧视是工作场所问题中最常见的，而基于政治和宗教观点的歧视也是值得注意的新问题。女性参与者中，年龄、性别、种族、政治观点和性取向等因素的交叉影响提到得较多。护理责任相关的歧视报告出现在所有性别身份的参与者中。在工作场所问题的负面影响方面，许多参与者描述了为了应对性别偏见而修改外貌或行为。性别也影响更广泛的职业挑战，女性和非二元性别受访者报告在大多数工作场所问题上遇到的频率较高，尤其是歧视（35%）和心理健康问题（62%）方面更为突出。
### Innovation
研究强调了软件开发领域歧视问题的多样性，并呼吁研究者在设计软件工程研究时选择和评估年龄和性别之外的相关方面，提高研究社区对这一领域的认知。
### Conclusion
此项研究旨在提高研究界对软件开发行业多种类型的歧视问题的认识，并鼓励研究者在进行软件工程研究时考虑更多维度，如年龄、性别、种族和残疾等，而不仅仅是关注年龄和性别。
## 748. `cs.SE` - AI辅助科学编码的十个简单规则 [PDF](https://arxiv.org/pdf/2510.22254), [HTML](https://arxiv.org/abs/2510.22254)
### Authors
Eric W. Bridgeford,Iain Campbell,Zijao Chen,Zhicheng Lin,Harrison Ritz,Joachim Vandekerckhove,Russell A. Poldrack
### Background
尽管AI编程工具显示出加速软件开发的潜力，但在科学计算中的应用引发了关于代码质量和科学有效性的重要问题。论文提出了一种在保持科学和方法论严谨性的同时利用AI能力的策略，通过四个关键主题——问题准备与理解、管理上下文与交互、测试与验证、以及代码质量保证和迭代改进，来应对这些问题。这强调了在编码决策中保持人类代理的作用、建立有效的验证程序，以及保留领域专业知识的必要性，以确保方法论稳健的研究。
### Innovation
提出了十个在科学研究中使用AI辅助编程的原则，旨在战略地在开发周期中利用AI的能力，并在利用AI潜力加速软件开发的同时，确保代码达到可靠性、可再现性和科学有效性的要求，保证研究的道德规范。这些原则着重于保持人类在编码决策中的主导作用，建立严谨的验证程序，以及保留领域的专门知识至关重要。
### Conclusion
这些规则旨在帮助研究者利用AI的技术革新来加速软件开发的过程，同时确保代码符合研究的道德规范和标准，如可靠性、可再现性和科学有效性。
## 749. `cs.SE` - 内部脆弱性与外部威胁：面向企业的开源风险管理扎根框架 [PDF](https://arxiv.org/pdf/2510.25882), [HTML](https://arxiv.org/abs/2510.25882)
### Authors
Wenhao Yang,Minghui Zhou,Daniel Izquierdo Cortázar,Yehui Wang
### Background
企业的开源应用从单一的技术采用转变为深入的战略集成，这使得它们面临远超代码本身的复杂风险环境。传统的风险管理方法过于集中在技术工具上，而对于上游“无声的修复”、社区冲突或许可证突然变更等系统性威胁则缺乏有效的应对措施，造成治理上的盲点。为应对这一治理真空，研究基于15位专家的实地调研，旨在提出一种全面的风险治理框架，以从战术风险管理向整体风险治理转变，明确目标、识别外部威胁和内部脆弱性，并通过“目标→威胁→脆弱性→缓解”（OTVM）的逻辑链提供一个超越单纯技术清单的决策模型。
### Innovation
研究开发了一种全面的风险治理框架，重点在于明确战略目标矩阵，系统分类外部威胁和内部脆弱性，并提供一个可操作的缓解框架，它将能力建设与这些脆弱性联系起来。该框架通过逻辑链'目标→威胁→脆弱性→缓解'（OTVM）提供了超越纯技术清单的全面决策模型。风险管理通过专家验证，提供了一种创新的诊断视角和系统化的路径，使企业可以从被动的“灭火”转变为积极构建组织的“免疫系统”。
### Conclusion
这项研究为企业的开源风险管理提出现有的诊断工具和系统路径，帮助其从应对反应性问题转变为构建组织层面的防御机制。研究通过案例研究验证了框架的分析效用，提供了一个面向企业的原创框架，帮助企业更好地理解和管理开源风险。
## 750. `cs.SE` - 一个基于Chrysler Pacifica Hybrid车辆的实践驱动框架，用于从驱动-by-wire系统过渡到自动驾驶系统 [PDF](https://arxiv.org/pdf/2410.06492), [HTML](https://arxiv.org/abs/2410.06492)
### Authors
Dada Zhang,Md Ruman Islam,Pei-Chi Huang,Chun-Hsing Ho
### Background
从驱动-by-wire (DBW) 系统过渡到完全自动驾驶系统（ADS）涉及多个发展阶段，需要强大的定位和感知能力。这项研究提出了一个基于实践的框架，使用2022款克莱斯勒太平洋混合动力小型货车，配备有相机、LiDAR、GNSS和计算硬件（配置有Robot Operating System (ROS)），并在一个结构化的测试环境中展示了离线的自主运营，利用预记录的LiDAR和相机数据以及点云和矢量地图进行有效的定位和路径规划。研究解决了过渡过程中遇到的关键挑战，特别是与无线网络辅助感知和定位相关的问题，并提供了克服软件不兼容性、传感器同步问题和实时感知限制的实用解决方案。
### Innovation
该论文强调了通过传感、数据融合和自动化集成来支持自动驾驶系统在测绘、模拟和培训中的作用，特别强调传感器、数据融合和自动化的集成是支持自动驾驶系统的关键因素。它提出了实施离线自主操作的方法，使用预记录的数据，提供了一种实用的策略框架，帮助研究人员进行DBW到ADS的转换。
### Conclusion
这项工作旨在为寻求DBW到ADS转换的研究人员提供操作策略。它为整合实时感知、GNSS-LiDAR-相机集成以及完全用ADS装备的自动驾驶车辆的操作提供了方向，从而促进了可靠的自动驾驶技术的发展。
## 751. `cs.SE` - CI/CD流水线的环境影响 [PDF](https://arxiv.org/pdf/2510.26413), [HTML](https://arxiv.org/abs/2510.26413)
### Authors
Nuno Saavedra,Alexandra Mendes,João F. Ferreira
### Background
CI/CD流水线在软件开发中广泛应用，但其对环境的影响，尤其是碳足迹和水足迹（CWF），对开发者来说仍然未知。由于云服务提供商通常不公开此信息，对云计算日益增加的环境影响的理解变得越来越重要。这项研究探讨了使用GitHub Actions的CWF。该研究基于Cloud Carbon Footprint框架的方法论，并采用了迄今为止最大的工作流运行数据集，包括超过220万个工作流运行，来自超过18,000个开源仓库。
### Innovation
该研究利用GitHub Actions的大量数据，构建了CWF估计方法。通过分析，揭示了GitHub Actions生态系统的CWF显著性，并提供了在最可能情况下，碳足迹为456.9MTCO2e，水足迹为5,738.2千升的估计值。此外，该研究还提出了减少环境影响的战略，包括部署在环境影响较低的地区，实施更严格的预定运行禁用政策以及与区域能源混合更加环境友好的时间段对执行进行对齐。
### Conclusion
GitHub Actions生态系统的CWF是显著的，通过部署在环境影响较低的地区、实施更严格的预定运行禁用政策以及优化执行时间，可以减少这一影响。碳足迹的可能值相当于7,615棵城市树木一年吸收的碳量，而水足迹等同于一个普通美国家庭5,053年的用水量。
## 752. `cs.SE` - RepoMark：代码使用审计框架用于代码大型语言模型 [PDF](https://arxiv.org/pdf/2508.21432), [HTML](https://arxiv.org/abs/2508.21432)
### Authors
Wenjie Qu,Yuguang Zhou,Bo Wang,Yuexin Li,Lionel Z. Wang,Jinyuan Jia,Jiaheng Zhang
### Background
大规模语言模型（LLM）的发展极大地改变了软件开发，实现了前所未有的编码任务自动化。然而，这些模型在开源代码仓库（如GitHub）上的训练引发了重要的伦理和法律问题，尤其是关于数据授权和开源许可证合规的问题。开发人员越来越多地质疑模型训练者在使用代码仓库之前是否获得了适当的授权，尤其是在数据收集透明度不足的情况下。为了应对这些担忧，本文提出了一种名为RepoMark的新数据标记框架，以审计代码LLM的数据使用情况。该方法使代码仓库的所有者能够验证其代码是否被用于训练，同时确保语义保真度、不可感知性及理论假发现率（FDR）的保证。
### Innovation
针对现有审计方法效率低的问题，RepoMark通过生成多个语义等效的代码变体并将其引入代码文件中，进一步加入了数据标记。在检测过程中，RepoMark利用一种新颖的基于排名的假设检验来检测模型中的记忆。与先前的数据审计方法相比，RepoMark显著提高了样本效率，使得即使用户仓库中的代码文件数量很少也能进行有效的审计。实验表明，当在严格控制的FDR为5%的条件下，RepoMark在小型代码仓库上的检测成功率超过90%，这远远超过了其他现有数据标记技术在相同设置下的准确率，也低于55%。这进一步证明了RepoMark作为一种理论坚实且具有巨大前景的解决方案，能够增强代码LLM训练的透明度，保障代码仓库所有者的权益。
### Conclusion
RepoMark作为一种数据标记和审计框架，通过显著提高样本效率，实现了在少量代码文件中进行有效审计的能力。实验结果表明，RepoMark在严格的假发现率控制下实现了超过90%的检测成功率，远超其他现有方法。这意味着RepoMark是增强代码LLM训练透明度和保护代码仓库所有者权益的可靠解决方案。
