# 20251231
[![Subscribe_Visitors](https://visitor-badge.laobi.icu/badge?page_id=nituchao.latest_arxiv_analyze_ai_rss)](https://github.com/nituchao/latest_arxiv_analyze_ai)

## 1. `cs.AI` - 我们无法识别AI生成的图片 [PDF](https://arxiv.org/pdf/2512.22236), [HTML](https://arxiv.org/abs/2512.22236)
### Authors
Adrien Pavão
### Background
如今，AI生成的图像在网络上非常普遍，但许多人仍然相信他们能够很容易地将这些图像与真实的照片区分开来。为了验证这一假设，作者通过一项互动的网络实验，让参与者对20张图像进行分类，判断它们是真实的还是AI生成的。数据集中包含120个较难识别的案例，即从CC12M中选取的真实图像及其通过MidJourney仔细策划的AI生成对应图像。
### Innovation
实验表明，参与者的平均准确率为54%，仅略高于随机猜测，且在多次尝试中几乎没有任何改善。实验结果表明，即使在相对简单的肖像图像上，人类也很难可靠地识别AI生成的内容。这一发现揭示了随着合成媒体的不断改进，仅靠人类判断区分真实数据和虚假数据变得不足。
### Conclusion
研究结果指出，即便是在相对简单的图像上，人类依然难以可靠地识别AI生成的内容。随着合成媒体技术的提高，仅凭人类的判断已经不足以区分真正和伪造的数据。因此，当AI生成的媒体变得越来越难以区分时，提高公众对这一问题的认识和制定道德准则变得尤为重要。
## 2. `cs.AI` - 双向RAG：通过多阶段验证实现安全自我提升的检索增强生成 [PDF](https://arxiv.org/pdf/2512.22199), [HTML](https://arxiv.org/abs/2512.22199)
### Authors
Teja Chinthala
### Background
检索增强生成（RAG）系统通过将响应与外部知识库联系起来，增强了大型语言模型。然而，传统RAG架构依赖于静态的语料库，无法从用户交互中进化。因此，本文旨在介绍一种新的RAG架构——双向RAG，其可以通过验证的重写生成高质量响应来安全地扩充语料库。
### Innovation
本文提出了一种新的双向RAG架构，该架构通过多阶段验证机制提供了安全的语料库扩充。其采用多阶段接受层，结合了基础事实验证（基于前提推理、属性检查及新颖性检测），以防止幻觉污染同时促进知识积累。实验结果表明，与标准RAG相比，双向RAG在四个数据集上的平均覆盖率提高了约40.58%，而出于效率考虑，它所添加的文档数量仅为朴素重写的72%，即140比500。
### Conclusion
本文的工作表明，当受到严格验证机制的指导时，自我改进的RAG系统是可行且安全的，提供了一条实用的途径，可使RAG系统在部署时进行学习。
## 3. `cs.AI` - SciEvalKit: 开放源代码的科学通用智能评估工具 [PDF](https://arxiv.org/pdf/2512.22334), [HTML](https://arxiv.org/abs/2512.22334)
### Authors
Yiheng Wang,Yixin Chen,Shuo Li,Yifan Zhou,Bo Liu,Hengjian Gao,Jiakang Yuan,Jia Bu,Wanghan Xu,Yuhao Zhou,Xiangyu Zhao,Zhiwang Zhou,Fengxiang Wang,Haodong Duan,Songyang Zhang,Jun Yao,Han Deng,Yizhou Wang,Jiabei Xiao,Jiaqi Liu,Encheng Su,Yujie Liu,Weida Wang,Junchi Yao,Shenghe Zheng,Haoran Sun,Runmin Ma,Xiangchao Yan,Bo Zhang,Dongzhan Zhou,Shufei Zhang,Peng Ye,Xiaosong Wang,Shixiang Tang,Wenlong Zhang,Lei Bai
### Background
当前的AI模型评估平台多为通用型，缺乏专注于科学领域核心能力的统一评估工具。这导致在不同科学学科和任务复杂度上缺乏一致和具体的基准评估，阻碍了科学基础模型和智能代理的进一步发展。
### Innovation
SciEvalKit 是一个统一的基准评估工具包，专注于科学智能的核心能力，包括科学多模态感知、科学多模态推理、科学多模态理解、科学符号推理、科学代码生成、科学假设生成及科学知识理解。它支持涵盖物理学、化学、天文学和材料科学等六大领域的科学评估。SciEvalKit 通过使用来自真实世界、特定领域的数据集构建专家级科学基准，确保任务能够反映真实的科学挑战。此外，它还提供灵活可扩展的评估管道，支持批量模型和数据集评估，并且结果透明可重复。
### Conclusion
SciEvalKit 提供了一个标准化且可定制的基础设施来评估下一代科学基础模型和智能代理，同时通过开源和社区维护的方式促进了AI4Science领域的共同发展和进步。
## 4. `cs.AI` - 新兴劝说：大语言模型会在未被提示的情况下进行劝说吗？ [PDF](https://arxiv.org/pdf/2512.22201), [HTML](https://arxiv.org/abs/2512.22201)
### Authors
Vincent Chang,Thee Ho,Sunishchal Dev,Kevin Zhu,Shi Feng,Kellin Pelrine,Matthew Kowal
### Background
随着对话AI系统的广泛应用，AI现在能够对人类的看法和信念产生前所未有的影响。近期研究显示，许多大型语言模型（LLMs）在被要求使用户产生有害信念或行为时，能够遵循请求进行劝说，并且模型的劝说能力随模型规模的增大而增强。然而，现有的研究主要关注被恶意行为者利用产生的威胁（即坏行为者请求LLM进行劝说）。本研究则探讨在未被明确提示的情况下，模型是否会自发劝说，这将影响我们对这种潜在劝说风险的态度。
### Innovation
研究通过两种场景来探讨未被提示时模型的劝说行为：（i）通过内部分导实现角色特性导向；（ii）通过监督微调来展示相同的特性。研究发现，仅通过角色特性导向（无论是与劝说相关还是无关的特性）不能可靠地增加模型在未被提示情况下的劝说倾向，而监督微调确实能够增加这种倾向。此外，对一般包含仅良性话题的大规模说服数据集进行监督微调后的模型更倾向于在争议性和有害话题上表现劝说行为——这表明潜在的有害劝说行为可能产生并且需要进一步研究。
### Conclusion
研究结果表明，在未被显式提示的情况下，监督微调能够增加模型劝说的倾向，特别是在涉及争议性和有害话题时。这强调了对这种潜在的新兴劝说风险进行进一步研究的必要性。
## 5. `cs.AI` - Agent2World：通过自适应多代理反馈学习生成符号世界模型 [PDF](https://arxiv.org/pdf/2512.22336), [HTML](https://arxiv.org/abs/2512.22336)
### Authors
Mengkang Hu,Bowei Xia,Yuran Wu,Ailing Yu,Yude Zou,Qiguang Chen,Shijian Wang,Jiarui Jin,Kexin Li,Wenxiang Jiao,Yuan Lu,Ping Luo
### Background
符号世界模型（例如PDDL领域或可执行模拟器）在基于模型的规划中至关重要，但训练大语言模型生成此类世界模型受到大量可验证监督缺乏的限制。当前方法主要依赖于静态验证方法，这些方法无法捕捉到交互执行中产生的行为级错误。
### Innovation
本文提出了一种名为Agent2World的工具增强多代理框架，实现了强大的推理时世界模型生成，并作为监督微调的数据引擎。该框架通过多代理反馈的强制化生成多阶段流水线：(i) 深度研究员代理通过网络搜索解决规范缺口；(ii) 模型开发者代理实现可执行世界模型；(iii) 专门的测试团队进行自适应单元测试和基于模拟的验证。Agent2World在三个涵盖PDDL和可执行代码表示的基准测试中表现出优越的推理性能，实现了持续的领先成果。测试团队还作为模型开发者的互动环境，提供行为意识的自适应反馈，生成多轮训练路径。经过这些路径微调的模型显著提高了世界模型生成能力，平均相对增益为30.95%。
### Conclusion
Agent2World展示了在三个基准测试中的优越性能，特别是在PDDL和可执行代码表示中，同时作为模型开发者的互动环境，提供了行为认知的自适应反馈，显著提高了世界模型生成能力。
## 6. `cs.AI` - GamiBench: 通过折纸折叠任务评估MLLMs的空间推理和2D至3D规划能力 [PDF](https://arxiv.org/pdf/2512.22207), [HTML](https://arxiv.org/abs/2512.22207)
### Authors
Ryan Spencer,Roey Yaari,Ritvik Vemavarapu,Joyce Yang,Steven Ngo,Utkarsh Sharma
### Background
现有的多模态大语言模型（MLLMs）在感知和指令跟随方面表现良好，但在空间推理方面仍有不足，即难以在不同视角和时间维度上追踪和操作物体。空间推理是人类智能的关键组成部分，但目前大多数基准测试主要集中在静态图像或最终输出，未能考虑到该技能的顺序性和视角依赖性。因此，需要一种新的基准测试来评估MLLMs的空间推理和2D至3D规划能力。
### Innovation
提出了GamiBench，一种通过折纸启发的折叠任务来评估MLLMs的空间推理和2D至3D规划能力的基准测试。GamiBench包含186个常规和186个不可能的2D折痕模式及其对应的3D折叠形状，来自六种不同视角的三个视觉问答（VQA）任务。GamiBench采用了新的诊断指标，如视角一致性（VC）和不可能折痕选择率（IFSR），以衡量模型处理不同复杂度折痕的能力。实验结果显示，即便是领先的模型，如GPT-5和Gemini-2.5-Pro也在单一步骤的空间理解中表现欠佳。
### Conclusion
GamiBench为评估MLLMs的几何理解和空间推理提供了一个标准化框架。它通过引入新的任务和测量指标，全面评估了模型的空间推理过程，包括跨视角一致性、物理可行性以及对中间折叠步骤的理解水平。这些贡献为研究多模态大语言模型的空间推理能力提供了一个新的基准。
## 7. `cs.AI` - With Great Capabilities Come Great Responsibilities: Introducing the Agentic Risk & Capability Framework for Governing Agentic AI Systems [PDF](https://arxiv.org/pdf/2512.22211), [HTML](https://arxiv.org/abs/2512.22211)
### Authors
Shaun Khoo,Jessica Foo,Roy Ka-Wei Lee
### Background
随着自主行动能力的增强，代理型人工智能系统(Agentic AI)具备了执行代码、互联网交互和文件修改等任务的能力。这给组织的有效治理带来了重大挑战，特别是在全面识别、评估和减轻多样化和不断演变的风险方面。
### Innovation
本文提出的代理型风险与能力(ARC)框架，是一种技术治理框架，旨在帮助组织识别、评估和减轻由代理型AI系统带来的风险。该框架的核心贡献包括：(1) 开发了一种以能力为中心的新视角来分析广泛种类的代理型AI系统；(2) 提炼了三类内在风险源，分别是组件、设计和能力；(3) 建立了每个风险源与具体材料化风险及相应技术控制的明确联系；(4) 提供了一种结构化和实用的方法，帮助组织实施该框架。
### Conclusion
该框架提供了一种稳健且可适应的方法，帮助组织应对代理型AI系统的复杂性，从而实现快速有效的创新，并确保代理型AI系统的安全、可靠和负责任部署。该框架已开源并在[这里]可以访问。
## 8. `cs.AI` - 思考的形状：当分配比正确性更重要时在推理任务中的表现 [PDF](https://arxiv.org/pdf/2512.22255), [HTML](https://arxiv.org/abs/2512.22255)
### Authors
Abhranil Chandra,Ayush Agrawal,Arian Hosseini,Sebastian Fischmeister,Rishabh Agarwal,Navin Goyal,Aaron Courville
### Background
该研究揭示了一个令人惊讶的发现，即通过训练语言模型使用来自更强大模型的合成数据集（这些数据集包含推理路径或链式思考（CoT）的轨迹），即使这些轨迹最终导出错误的答案，也可以提高语言模型的推理能力。实验结果表明，这种训练方式可以在推理任务上优于使用人工注释数据集的训练效果。研究进一步推测，这是由于合成数据的分布与语言模型自身的分布更为接近，更容易学习，同时也因为这些错误轨迹中包含部分正确的推理步骤。为了验证这一推测，研究利用语言模型来重新表述人工注释的轨迹，使其分布更接近模型自身的分布，从而提升模型表现。
### Innovation
研究提出了一个创新的观点，即在推理任务中，模型的分布比最终的答案正确性更重要。通过训练使用来自更强大模型的合成数据集，这种训练方式可以提升模型的推理能力。研究还通过逐步引入越来越不完整且错误的推理路径，考察模型对这些错误的容忍度，展示了这一观点在数学、算法推理和代码生成等不同领域的适用性。
### Conclusion
研究证明，收集与模型分布更相似的数据集是提高模型推理性能的关键。此外，一个正确的最终答案并不总是反映真实的推理过程的一个可靠指标。该研究指出，在构建数据集时需要考虑模型的分布特征，同时强调正确性不能成为衡量模型推理过程的唯一标准。
## 9. `cs.AI` - 逻辑草图提示 (LSP): 一种确定性和可解释性的提示方法 [PDF](https://arxiv.org/pdf/2512.22258), [HTML](https://arxiv.org/abs/2512.22258)
### Authors
Satvik Tripathi
### Background
大型语言模型（LLMs）在自然语言推理方面表现出色，但在需要严格规则遵循、确定性和可审计性的任务上依然不可靠。现有的零样本提示、思维链提示和简洁提示等方法缺乏确定性和可解释性，无法满足临床、监管和安全关键决策支持系统的需求。
### Innovation
提出了一种轻量级提示框架逻辑草图提示 (LSP)，引入了类型变量、确定性条件评估器和基于规则的验证器，能够生成可追踪和可重复的输出。在两项药理逻辑合规任务中，LSP 在三个开源模型（Gemma 2、Mistral 和 Llama 3）上一致地呈现出最高的准确率和 F1 分数，显著优于其他提示方法。
### Conclusion
LSP 提高了确定性、可解释性和一致性，而未牺牲性能，支持其在临床、监管和安全关键决策支持系统中的应用。
## 10. `cs.AI` - 向更公平的恢复迈进：面向公平的人工智能框架在孟加拉国优先分配洪水后援助 [PDF](https://arxiv.org/pdf/2512.22210), [HTML](https://arxiv.org/abs/2512.22210)
### Authors
Farjana Yesmin,Romana Akter
### Background
发展中国家的灾后援助常常受到系统性偏见的影响，这些偏见使脆弱地区处于不利地位，加剧了历史上的不平等。本研究探讨了如何利用公平感知的人工智能框架优化孟加拉国洪水后的援助分配，孟加拉国是一个频繁遭受洪水灾害的国家。
### Innovation
开发了一种公平感知的人工智能框架，使用真实数据（2022年孟加拉国洪水影响720万人，损失4.055亿美元）训练一种对抗去偏导模型，该模型能预测洪水脆弱性并积极消除针对边缘化分区和农村地区的偏见。该方法采用源自医疗AI的公平感知表示学习技术，使用梯度反转层促使模型学习偏差不变的表示。
### Conclusion
实验结果表明，该框架减少了统计公平性差异41.6%，缩小了区域公平差距43.2%，同时保持了较高的预测准确性（R-squared=0.784 vs 基线0.811）。该模型生成了基于实际情况的优先级排序，确保援助资源真正分配给最脆弱的人群，而不是依赖于历史分配模式。该研究证明了算法公平技术如何有效应用于人道主义救援，为决策者提供了实施更公正的灾后恢复策略的工具。
## 11. `cs.AI` - 利用SMOTE-Tomek预处理技术提升需求分类 [PDF](https://arxiv.org/pdf/2501.06491), [HTML](https://arxiv.org/abs/2501.06491)
### Authors
Barak Or
### Background
本文研究了需求工程领域，特别是在PRoMES数据集中存在类别不平衡问题时的需求分类问题。PRoMES数据集包含969个需求，分为功能性和非功能性两类。
### Innovation
本文提出了一种新的处理策略，通过应用SMOTE-Tomek预处理技术结合分层K折交叉验证来解决类别不平衡问题。这种方法提高了少数类别的表示能力，同时保持验证折的完整性，显著提高了分类准确性。
### Conclusion
实验结果显示，使用逻辑回归方法达到了76.16％的准确率，远超过基线58.31％的精度。这表明机器学习模型作为一种可扩展和可解释的解决方案具有很高的应用价值与效率。
## 12. `cs.AI` - 通过信息论正则化实现机器卸载 [PDF](https://arxiv.org/pdf/2502.05684), [HTML](https://arxiv.org/abs/2502.05684)
### Authors
Shizhou Xu,Thomas Strohmer
### Background
本文探讨如何有效地从学习结果中去除或'遗忘'不必要的信息，如特定特征或单一数据点的影响，同时最大限度地减少功能损失并确保严格的技术保证。
### Innovation
文章引入了一个统一的数学框架，基于信息理论正则化，解决数据点遗忘和特征遗忘的问题。文章还提出了可审计和可证明的边缘遗忘原则，提供了一个基于该原则的边缘遗忘的正式信息理论定义，并且提供了边缘遗忘在现有近似遗忘定义中的充分性和必要性的可证明保证。此外，文章还展示了该框架可以自然地解决边缘遗忘问题，并且在深度学习中，该方法具有任意训练目标的灵活性，以及简单化的正则化设计，使其高度适应性和实用性强。从数学角度来看，文章提供了在多种信息论训练目标下的最优特征遗忘问题的统一解析解。
### Conclusion
本文的理论分析揭示了机器遗忘、信息论、最优传输以及极值sigma代数之间的有趣联系。数值模拟支持理论发现。
## 13. `cs.AI` - 在分散式数据上的任务无关联邦研究概貌与愿景 [PDF](https://arxiv.org/pdf/2503.03140), [HTML](https://arxiv.org/abs/2503.03140)
### Authors
Wentai Wu,Ligang He,Saiqin Long,Ahmed M. Abdelmoniem,Yingliang Wu,Rui Mao,Keqin Li
### Background
随着对私人和专有信息的立法和监管不断增加，分散式数据源产生的数据孤岛现象使数据孤岛成为新问题。联邦学习能够实现分散数据上的隐私保护协作，但这种模式在公平性、成本性和可再现性方面存在局限，因为它以学习为中心。因此，本研究探讨了从资源密集型学习转向任务无关合作的可能性，特别是在参与者没有共同目标兴趣的情况下。
### Innovation
提出了一个新的情景，称为任务无关联邦（TAF），并研究了几种技术构建块，直接或间接地采用了以数据为中心的方法，可以在任何学习任务之外独立运行。为此，该研究描述了任务无关联邦的系统架构和问题设定，并按协作数据扩展、协作数据精细化和集体数据协调化三个方面分类了近年来的研究，并指出了几个需要社区更多关注的挑战和开放问题。
### Conclusion
通过该研究，希望为不同动机的自主方如何在分散数据上超越学习的合作提供新的见解，呼吁社区在任务无关联邦的研究方面给予更多关注。
## 14. `cs.AI` - 原子思维：马尔可夫大语言模型推理过程 [PDF](https://arxiv.org/pdf/2502.12018), [HTML](https://arxiv.org/abs/2502.12018)
### Authors
Fengwei Teng,Quan Shi,Zhaoyang Yu,Jiayi Zhang,Yuyu Luo,Chenglin Wu,Zhijiang Guo
### Background
大语言模型（LLM）通过测试时缩放方法实现了显著的性能提升。然而，现有方法常常由于推理过程中历史依赖信息的累积而产生冗余计算。为了应对这一挑战，本文利用马尔可夫过程的记忆无相关性，减少对历史上下文的依赖，并提出了一种马尔可夫推理过程。该基础性的马尔可夫链结构能够无缝集成到各种测试时缩放方法中，从而提高其缩放效率。
### Innovation
通过与树搜索和技术反思性细化等技术相结合进一步放大马尔可夫推理链，本文揭示了一种新兴的原子推理结构，其中推理轨迹被分解成一系列自包含、低复杂度的原子单元。作者将该设计命名为“原子思维（textbf{Atom of Thoughts}）”。实验结果显示，在计算预算增加时，该方法始终优于现有基线。此外，该方法能够无缝集成到现有的推理框架及不同的大语言模型（无论是推理型还是非推理型）中，从而实现可扩展的高性能推理。
### Conclusion
大量的实验表明，textbf{Atom of Thoughts}在计算预算增加时始终优于现有基线。重要的是，textbf{Atom of Thoughts}能够无缝集成到现有的推理框架及不同大语言模型中，促进可扩展性和高性能推理。除了提交该论文，作者还计划公开发布代码，以促进可再现性和未来的研究。
## 15. `cs.AI` - Tiled Flash Linear Attention: 更高效的线性RNN和xLSTM内核 [PDF](https://arxiv.org/pdf/2503.14376), [HTML](https://arxiv.org/abs/2503.14376)
### Authors
Maximilian Beck,Korbinian Pöppel,Phillip Lippe,Sepp Hochreiter
### Background
线性RNN在语言建模中展现了与Transformer相当的表现。虽然线性RNN的计算复杂度与序列长度呈线性增长，理论上比Transformer具有运行时优势，但在实践中实现这些优势需要优化的定制内核。Flash Linear Attention (FLA) (Yang & Zhang, 2024) 通过在输入序列块上并行化来提高线性RNN内核的性能，但其块大小有限，导致中间状态占用大量GPU内存，产生低算术强度和高内存消耗及IO成本，尤其是在长上下文预训练中。
### Innovation
本文提出了Tiled Flash Linear Attention (TFLA)，这是一种用于线性RNN的新内核算法，它通过在每个块内引入额外的序列并行化层次，实现了任意大的块大小和高的算术强度。TFLA首先应用于具有矩阵内存的xLSTM，并提出了一种使用Sigmoid输入门的mLSTM变种，以获得更快的内核运行时间。实验表明，基于TFLA的新mLSTM内核性能优于高度优化的Flash Attention、Linear Attention和Mamba内核，建立了有效长上下文序列建模的新基准。
### Conclusion
我们的新mLSTM内核基于Tiled Flash Linear Attention，在保持语言建模性能的同时，比高度优化的Flash Attention、Linear Attention和Mamba内核更快，设定了一种新的高效长上下文序列建模基线。
## 16. `cs.AI` - 适应QoE变化的塑性意识混合专家在自适应视频流传输中的学习方法 [PDF](https://arxiv.org/pdf/2504.09906), [HTML](https://arxiv.org/abs/2504.09906)
### Authors
Zhiqiang He,Zhi Liu
### Background
自适应视频流传输系统旨在优化用户体验(QoE)，提高用户满意度。然而，不同用户特征和视频内容导致QoE因素权重不同，产生用户特定的QoE功能和变化的优化目标。这为神经网络带来了挑战，因为它们在适应变化的优化目标时会出现适应性退化现象，即塑性损失，导致模型难以适应新的优化目标。
### Innovation
提出了一种名为塑性意识混合专家(Plasticity-Aware Mixture of Experts, PA-MoE)的新学习框架，通过平衡记忆保留与有选择性遗忘来动态调节网络的适应性。PA-MoE利用噪声注入来促进遗忘过时知识，增强神经网络的适应能力，并通过理论分析明确了PA-MoE的学习性能。实验结果表明，PA-MoE在动态流传输环境中的QoE比竞争对手高出45.5%。此外，通过改变噪声注入的水平，该研究中的参数敏感性研究结果与理论预测高度一致。
### Conclusion
PA-MoE通过提高神经网络的适应性，有效地缓解了塑性损失，优化了神经元的利用，从而在动态流传输环境中实现了显著的QoE提升。
## 17. `cs.AI` - 字典学习：具反馈学习稀疏叠加特征的复杂性 [PDF](https://arxiv.org/pdf/2502.05407), [HTML](https://arxiv.org/abs/2502.05407)
### Authors
Akash Kumar
### Background
深度网络的成功主要归因于它们在表示空间中捕捉潜在特征的能力。本文探讨了模型的潜在学习特征是否可以通过代理（如大规模语言模型（LLM））提供的相对三元组比较反馈有效地检索出来。代理可以通过激活构建反馈，在稀疏环境下分析反馈学习特征矩阵的复杂性，并在代理反馈仅限于分布信息的情况下，验证稀疏场景中的强大上限。
### Innovation
提出了一种利用大规模语言模型进行相对三元组比较反馈来有效检索模型潜在学习特征的新方法。特别是在稀疏环境下的特征矩阵学习复杂性分析，并通过不同应用场景验证了理论发现。
### Conclusion
研究所确立的理论界限在代理能够构建激活时达到紧界，在代理反馈仅限于分布信息时，稀疏场景下呈现了强大的上限。通过两个不同应用案例（特征恢复和稀疏自动编码器提取大规模语言模型的字典）验证了理论发现的有效性。
## 18. `cs.AI` - HEART：实现车辆-边缘-云集成层次联邦学习的及时多模型训练 [PDF](https://arxiv.org/pdf/2501.09934), [HTML](https://arxiv.org/abs/2501.09934)
### Authors
Xiaohong Yang,Minghui Liwang,Xianbin Wang,Zhipeng Cheng,Seyyedali Hosseinalipour,Huaiyu Dai,Zhenzhen Jiao
### Background
随着AI增强的车联网（IoV）的迅速发展，高效的支持高车辆移动性和分散化数据的机器学习解决方案变得至关重要。这促使了车辆-边缘-云架构（VEC-HFL）层次联邦学习的出现。然而，在关于VEC-HFL的研究中，车辆执行多种机器学习任务并存的情况尚未受到充分探索。这种多模型训练环境引入了关键挑战，包括不当的聚合规则可能导致模型过时和训练时间延长，车辆移动性可能造成数据利用效率低下，并且资源分配不均衡严重影响协作训练的有效性。
### Innovation
本文提出了一个框架，旨在解决动态VEC-HFL中的多模型训练问题，目标是最大程度地减少全局训练延迟，同时确保在各种任务之间的平衡训练——这是一个证明是一个NP难问题。为实现及时模型训练，引入了一种混合同步-异步聚合规则。在此基础上，提出了一种名为HEART的新方法，通过结合改进的粒子群优化（PSO）和遗传算法（GA）的混合启发式方法进行任务调度，并通过低复杂度的贪婪算法确定已分配任务在车辆上的训练优先级。
### Conclusion
实验结果表明，HEART方法在实际数据集上优于现有方法。
## 19. `cs.AI` - The Heap：一种无污染的多语言代码数据集，用于评估大型语言模型 [PDF](https://arxiv.org/pdf/2501.09653), [HTML](https://arxiv.org/abs/2501.09653)
### Authors
Jonathan Katzy,Razvan Mihai Popescu,Arie van Deursen,Maliheh Izadi
### Background
近年来，大型语言模型的流行度上升推动了用于训练它们的大量代码数据集的发展。这导致可用于下游特定行为研究或大型语言模型评估的代码数据有限，并且容易受到数据污染的影响。
### Innovation
我们发布了《Heap》，这是一个涵盖了57种编程语言的大规模多语言代码数据集，经过与其他开源代码数据集的去重处理，使研究人员在不进行大量数据清理的情况下，能够公平地评估大型语言模型。
### Conclusion
通过使用Heap，研究人员可以在避免数据污染的同时进行公平的大型模型评估，无需承担显著的数据清理负担。
## 20. `cs.AI` - 通过组成提示引导的扩散模型实现鲁棒性息肉检测与诊断 [PDF](https://arxiv.org/pdf/2502.17951), [HTML](https://arxiv.org/abs/2502.17951)
### Authors
Jia Yu,Yan Zhu,Peiyao Fu,Tianyi Chen,Junbo Huang,Quanlin Li,Pinghong Zhou,Zhihua Wang,Fei Wu,Shuo Wang,Xian Yang
### Background
结肠癌（CRC）是全球重要的公共卫生问题，早期筛查在降低死亡率方面具有重要作用。虽然深度学习模型在提高息肉检测、分类和分割方面显示出潜力，但在多样化的临床环境中，特别是面对未遇分布（OOD）数据时，其泛化能力仍然是一个挑战。多中心的数据集如PolypGen被开发出来以应对这些问题，但这些数据集的收集成本高昂且耗时。传统的数据增强技术提供的变化有限，无法捕捉医学图像的复杂性。扩散模型作为一个生成合成息肉图像的有前途的解决方案已经出现，但当前模型生成图像的过程主要依赖分割掩码作为条件，限制了其在捕捉完整临床上下文方面的能力。
### Innovation
本文提出了渐进光谱扩散模型（PSDM），该模型通过将诸如分割掩码、边界框和结肠镜报告等多样化临床注解转化为组合提示，并根据这些提示分层组织成粗细两部分，以捕捉广泛的空冋结构和细节点，生成临床准确的合成图像。通过使用PSDM生成的样本增强训练数据，模型在息肉检测、分类和分割方面表现出显著的改进。例如，与PolypGen数据集相比，PSDM提升了F1分数2.12%和平均精度3.09%，在未见分布（OOD）场景中表现为具备优越性能和更强的泛化能力。
### Conclusion
通过使用PSDM生成的样本增强训练数据，我们的模型显著改善了息肉的检测、分类和分割。PSDM在PolypGen数据集上实现了F1分数2.12%和平均精度3.09%的提升，这种增强展示了其在未见分布（OOD）场景中的优越性能和更好的泛化能力。
## 21. `cs.LG` - 使用评分奖励训练AI合作者 [PDF](https://arxiv.org/pdf/2512.23707), [HTML](https://arxiv.org/abs/2512.23707)
### Authors
Shashwat Goel,Rishi Hazra,Dulhan Jayalath,Timon Willi,Parag Jain,William F. Shen,Ilias Leontiadis,Francesco Barbieri,Yoram Bachrach,Jonas Geiping,Chenxi Whitehouse
### Background
AI合作者正在成为辅助人类研究人员实现研究目标的工具。它们的关键特征是在给定目标和限制的情况下生成研究计划的能力。虽然现有的语言模型能够在一定程度上生成研究计划，但在遵守所有约束和隐性要求方面仍然表现不佳。
### Innovation
研究者开发了一个方法，利用大量已有的研究论文来训练能够生成更好研究计划的语言模型。通过自动提取研究目标和目标特定的评分规则，构建了一个可扩展且多样化的训练语料库。通过基于强化学习和自评分的方法训练模型，并通过冻结初始策略作为标记器，创建生成器验证器差距以进行改进，而无需外部的人类监督。此外，研究者还将该方法应用于来自不同领域的研究目标，展示了在不同领域中的泛化能力。
### Conclusion
基于评分奖励的方法有效提升了研究计划生成模型的表现，即使在医疗研究等执行反馈不可行的情况下，也能实现显著的交叉领域泛化。这些发现证明了一种可扩展的自动化训练方法对未来提升通用AI合作者的潜力。
## 22. `cs.LG` - ReCollab：用于合作即兴队友建模的检索增强大型语言模型 [PDF](https://arxiv.org/pdf/2512.22129), [HTML](https://arxiv.org/abs/2512.22129)
### Authors
Conor Wallace,Umer Siddique,Yongcan Cao
### Background
即兴团队工作（AHT）要求智能代理能够推断出之前未见过队友的行为，并相应地调整其策略。传统方法通常依赖于固定的概率模型或分类器，这些在部分可观测性和有限交互的情况下可能会表现出脆弱性。大型语言模型（LLMs）提供了一种灵活的替代方案：通过将行为痕迹映射到高层次的假设上，它们可以充当队友行为的世界模型。
### Innovation
我们提出了Collab，一种基于语言的框架，使用行为分类器将队友类型分类，该分类器是从轨迹特征中得出的行为标准。我们进一步将其扩展为ReCollab，该框架结合了检索增强生成（RAG）以通过典范轨迹稳定推理。在合作型的Overcooked环境中，Collab能够有效地区分队友类型，而ReCollab在各种布局上的一致性改进适应性，在分类准确性和阶段性回报之间实现了帕累托最优的权衡。
### Conclusion
这些发现证明了LLMs作为即兴团队工作行为世界模型的潜在价值，并强调了在挑战性的协调环境中检索基础的重要性。
## 23. `cs.LG` - 利用边缘闲置计算资源进行基础模型训练 [PDF](https://arxiv.org/pdf/2512.22142), [HTML](https://arxiv.org/abs/2512.22142)
### Authors
Leyang Xue,Meghana Madhyastha,Myungjin Lee,Amos Storkey,Randal Burns,Mahesh K. Marina
### Background
当前基础模型开发的生态系统具有高度集中性，仅限于大型云数据中心运营商。训练基础模型需要大量计算资源，成本高昂。现有的边缘设备训练方法在性能、可扩展性、内存限制和通信开销方面存在不足，难以应对设备异构性和动态性问题。
### Innovation
提出了一个新的范例——Cleave，通过一种新颖的选择性混合张量并行方法细粒度地划分训练操作，并结合以参数服务器为中心的训练框架，解决了设备内存限制和通信瓶颈问题，使得在大量设备上高效训练大规模模型与云计算性能相当。Cleave通过成本优化模型指导设备选择和训练任务分配，有效应对设备异构性和变化。
### Conclusion
实验结果显示，Cleave能够在支持更大规模模型和数千个设备的情况下高效扩展，比基线边缘训练方法多支持8倍的设备数。Cleave的方法在每批次训练时间上比最先进的边缘训练方法快10倍，并且能够有效处理设备故障，在恢复时间上比先前方法快至少100倍。
## 24. `cs.LG` - 使用Conformal Prediction的无分布过程监测 [PDF](https://arxiv.org/pdf/2512.23602), [HTML](https://arxiv.org/abs/2512.23602)
### Authors
Christopher Burger
### Background
传统统计过程控制（SPC）对于质量管理至关重要，但在现代复杂制造环境中，它受制于常常被违反的统计假设，导致监测结果不可靠。
### Innovation
本文介绍了一种结合Conformal Prediction的混合框架，以增强SPC。提出两种新颖的应用：一是Conformal-Enhanced Control Charts，用于可视化过程不确定性并发出如“不确定性高峰”等前瞻性的信号；二是Conformal-Enhanced Process Monitoring，重新将多变量控制问题视为形式化的异常检测问题，并使用直观的p值图来监控。
### Conclusion
本文框架提供了更稳健且统计上更严谨的过程质量控制方法，同时保持了经典方法的可解释性和易用性。
## 25. `cs.LG` - Le Cam Distortion: 一种基于决策理论的鲁棒迁移学习框架 [PDF](https://arxiv.org/pdf/2512.23617), [HTML](https://arxiv.org/abs/2512.23617)
### Authors
Deniz Akdemir
### Background
在实际机器学习中，领域转移是一个核心挑战。传统的无监督领域适应（UDA）方法通过最小化对称差异来使源和目标表示一致，要求严格不变性。然而，当源领域和目标领域信息量不均衡时，这种严格不变性会导致信息破坏，从而产生“消极转移”，尤其是在安全关键应用中可能造成灾难性后果。
### Innovation
本文提出了一个基于Le Cam统计实验理论的决策理论框架，通过构建近似方法替代对称不变性，引入了Le Cam扭曲度量Deficiency Distance，作为在可模拟条件下转移风险的严格上限。框架通过学习核函数来模拟目标从源领域，从而实现无源领域退化的迁移。
### Conclusion
Le Cam Distortion在五个实验（基因组学、视觉、强化学习）中取得了显著成果：1. 在HLA基因组学中实现了近乎完美的频率估计（相关性r=0.999），与经典方法匹配；2. 在CIFAR-10图像分类中保留了全部源领域实用性（准确率达81.2%），而CycleGAN导致34.7%的精度下降；3. 在强化学习控制中实现了安全策略迁移，而基于不变性方法则遭受了灾难性失败。Le Cam Distortion为不可接受消极转移的领域提供了第一个有原则的风险控制迁移学习框架，适用于医学影像、自主系统和精准医疗等领域。
## 26. `cs.LG` - 基于EEG的图引导领域自适应方法在稳健的跨会话情绪识别中的应用 [PDF](https://arxiv.org/pdf/2512.23526), [HTML](https://arxiv.org/abs/2512.23526)
### Authors
Maryam Mirzaei,Farzaneh Shayegh,Hamed Narimani
### Background
准确的人机交互需要对人类的情感状态进行准确识别。脑电图（EEG）由于其高时间分辨率和直接反映神经活动的特点，成为情绪识别的一个可靠来源。然而，记录会话之间的变化对模型泛化构成了重大挑战。
### Innovation
我们提出了EGDA框架，通过同时对全局（边际）和类特定（条件）分布进行联合对齐，减少了跨会话的差异性。该框架通过图形正则化保留了EEG数据的固有结构。
### Conclusion
EGDA在SEED-IV数据集上的实验结果表明，该方法在三个转移任务中的跨会话性能表现出稳健性，分别达到81.22%，80.15% 和83.27%的准确率，并且优于多个基线方法。进一步的分析还指出了γ频率带作为最具有鉴别性的频率带，以及中央顶叶和前额叶脑区对于可靠的情绪识别至关重要。
## 27. `cs.LG` - 长上下文的端到端测试时训练 [PDF](https://arxiv.org/pdf/2512.23675), [HTML](https://arxiv.org/abs/2512.23675)
### Authors
Arnuv Tandon,Karan Dalal,Xinhao Li,Daniel Koceja,Marcel Rød,Sam Buchanan,Xiaolong Wang,Jure Leskovec,Sanmi Koyejo,Tatsunori Hashimoto,Carlos Guestrin,Jed McCaleb,Yejin Choi,Yu Sun
### Background
当前的长上下文语言建模主要集中在架构设计上，而忽略了一个关键点：在测试阶段的持续学习。大多数方法依赖于复杂的架构设计来处理长上下文，这篇论文转而将长上下文语言建模问题重新定义为连续学习问题。
### Innovation
提出了一种名为Test-Time Training (TTT)的新方法，该方法通过在训练阶段采用元学习来改进测试阶段的学习初始化。这种方法将测试时间和训练时间都设计为端到端（E2E）展示，这是前代方法所不具备的。实验表明，该方法利用Transformer滑动窗口注意力机制，在128K上下文长度下比全注意力机制快2.7倍，同时保持了恒定的推理延迟。
### Conclusion
通过对比不同模型的扩展性实验，论文展示了其方法（TTT-E2E）在处理大量训练数据生成的大模型时的表现与全注意力机制类似，而在需要快速推理的应用场景中，TTT-E2E却能实现更快的速度，特别是在128K上下文长度下。
## 28. `cs.LG` - 随机控制微分方程 [PDF](https://arxiv.org/pdf/2512.23670), [HTML](https://arxiv.org/abs/2512.23670)
### Authors
Francesco Piatti,Thomas Cass,William F. Turner
### Background
研究介绍了结合随机特征与受控微分方程（CDEs）的时间序列学习训练框架。利用大型随机参数化CDEs作为连续时间的神经网络，将输入路径映射为丰富表示。仅训练一个线性读出层，从而构建出快速、可扩展且具有良好归纳偏置的时间序列模型。
### Innovation
提出了两种变体：(i) 随机Fourier CDEs (RF-CDEs)，通过随机Fourier特征将输入信号升维，提供无核近似RBF增强序列模型；(ii) 随机粗糙路径DEs (R-RDEs)，直接在粗糙路径输入上进行操作，采用对数常微分方程离散化，并使用对数标志捕捉更高阶时间交互，同时保持稳定性和效率。证明表明，在无限宽度极限下，这两种模型分别诱导RBF提升标志核和粗糙标志核，提供随机特征神经网络、连续时间深度架构以及路径标志理论的统一视角。
### Conclusion
两种模型在多种时间序列基准测试中表现出竞争或最先进的性能，为替代显式标志计算提供了实用可行的选择，保留其归纳偏置并受益于随机特征的高效性。
## 29. `cs.LG` - VL-RouterBench: 视觉-语言模型路由基准 [PDF](https://arxiv.org/pdf/2512.23562), [HTML](https://arxiv.org/abs/2512.23562)
### Authors
Zhehao Huang,Baijiong Lin,Jingyuan Zhang,Jingying Wang,Yuhang Liu,Ning Lu,Tao Li,Xiaolin Huang
### Background
多模型路由技术已经从工程技巧发展成为必要的基础设施，但现有的研究缺乏一套系统且可复现的基准来评估视觉-语言模型（VLM）的性能。
### Innovation
本文提出了VL-RouterBench基准，旨在系统地评估VLM路由系统的整体能力。它基于VLM的原始推理和评分日志构建质量与成本矩阵，涵盖14个数据集，总计30,540个样本，并包括15个开源模型和2个API模型，提供了519,180个样本-模型对。评估协议综合测量平均准确率、平均成本和吞吐量，并使用归一化成本和准确率的调和平均数构建排名分数，以跨不同的路由配置和成本预算进行比较。
### Conclusion
通过该基准评估了10种路由方法和基线，观察到显著的可路由性提升，但当前最佳路由器仍明显低于理想的Oracle基准，表明在通过更精细的视觉提示和文本结构建模改进路由器架构方面存在很大的改进空间。未来将公开此数据构建和评估工具链，以促进跨模态路由研究中的可比性、可复现性和实际部署。
## 30. `cs.LG` - BOAD：通过赌博机优化发现分级软件工程代理 [PDF](https://arxiv.org/pdf/2512.23631), [HTML](https://arxiv.org/abs/2512.23631)
### Authors
Iris Xu,Guangtao Zeng,Zexue He,Charles Jin,Aldo Pareja,Dan Gutfreund,Chuang Gan,Zhang-Wei Hong
### Background
大型语言模型（LLMs）在推理和编码方面表现出色，但在处理长周期和分布外的实际软件工程（SWE）问题时却难以实现泛化。现有系统通常依靠单一代理来处理整个工作流，包括解释问题、导航大型代码库和实现修复。这种单一模式的设计使模型被迫保持不必要的上下文，导致虚假的相关性和泛化效果不佳。受人类工程师如何分解复杂问题的启发，提出将软件工程代理结构化为协调专门子代理的协调者，每个子代理负责不同的子任务（例如定位、编辑和验证）。然而，自动构建有效的分级结构是一个挑战，随着子代理数量的增加，搜索空间变得组合化，难以在团队中为每个子代理归因贡献。
### Innovation
提出了通过赌博机优化（Bandit Optimization）发现分级软件工程代理的设计（BOAD）。将每个子代理视为手臂，评估与其他代理合作时的回报衡量其帮助性。这使BOAD能够在有限的评估预算下高效探索子代理的设计。当应用于SWE-bench-Verified时，BOAD优于单一代理系统和手工设计的多代理系统。在SWE-bench-Live版本中，对于更近和分布外的问题，36B系统的排名超过其他大型模型如GPT-4和Claude，证明了自动发现的分级多代理系统在处理具有挑战性的长期SWE任务时显著提高了泛化能力。
### Conclusion
自动发现的分级多代理系统在处理具有挑战性的长期软件工程任务时显著提高了泛化能力。该研究结果在其代码存储库中可获得。
