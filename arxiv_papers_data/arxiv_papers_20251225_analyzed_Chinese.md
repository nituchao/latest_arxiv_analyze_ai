# 20251225
[![Subscribe_Visitors](https://visitor-badge.laobi.icu/badge?page_id=nituchao.latest_arxiv_analyze_ai_rss)](https://github.com/nituchao/latest_arxiv_analyze_ai)

## 1. `cs.AI` - 插值解码：探索LLM中人格特质的光谱 [PDF](https://arxiv.org/pdf/2512.19937), [HTML](https://arxiv.org/abs/2512.19937)
### Authors
Eric Yeh,John Cadigan,Ran Chen,Dick Crouch,Melinda Gervasio,Dayne Freitag
### Background
最近的研究探索了使用非常大的语言模型（LLMs）作为人类在模拟、调查和研究中的代理。虽然LLMs没有人类的心理，但在适当条件下，它们能够很好地模拟人类行为，驱动模拟以测试人类行为假设，并且比行为经济学中常用的基于规则的代理展现出更高的细腻度和多样性。对人格对决策影响的兴趣是一个关键领域，但每种测试人格特征都需要一个提示的存在，这带来了实验负担并降低了可重复性。
### Innovation
本文通过采用插值解码技术，将每种人格维度表示为一对对立的提示，并使用插值参数模拟行为沿该维度的变化。研究展示了插值解码可以可靠地调节“大五人格”特质的评分，并且能够在经济游戏中使LLMs模拟人类决策行为，重现了人类心理学研究中的结果。此外，还展示了系统通过系统搜索在插值空间中找到能够复制人类玩家行为的点，以“克隆”个体玩家。
### Conclusion
插值解码技术为研究人格特质在LLM中的影响提供了新的方法，不仅减少了实验需求，提高了可重复性，还能够逼真地模拟人类在经济游戏中的决策行为，为行为经济学和人机交互研究提供了一种新的工具。
## 2. `cs.AI` - 一种快速且公平的最后一个环节救灾援助分配的分支定价算法 [PDF](https://arxiv.org/pdf/2512.19882), [HTML](https://arxiv.org/abs/2512.19882)
### Authors
Mahdi Mostajabdaveh,F. Sibel Salman,Walter J. Gutjahr
### Background
灾害后的救灾物资分配是人道主义物流的关键方面。在重大灾难中，预先储备的物资常常无法满足需求。本文旨在制定从配送中心到避难所的车辆路线规划，同时分配有限的救灾物资。为了平衡效率和公平性，本文提出了一个双目标问题：通过基于基尼系数的方法最小化未满足需求的不平等度，以及最小化总运输时间以确保及时交付。
### Innovation
提出了混合整数规划模型(HIP)，并使用ε约束方法处理双目标问题。通过推导最优解的数学性质，引入了有效的不等式，并设计了在可行车辆路线中实现最优配送分配的算法。开发了一种分支定价(B&P)算法来有效解决问题。计算结果显示，B&P算法显著优于商业MIP求解器。双目标方法在不影响效率的情况下减少了34%的援助分配不平等性。结果显示，当时间限制非常宽松或非常紧时，优先覆盖需求而忽略公平性的方式是有效的；在适度的时间限制下，平衡策略至关重要，以避免不公平的结果。
### Conclusion
分支定价(B&P)算法在解决救灾援助分配问题时具有显著优势。双目标方法在避免不公平的结果方面有效，并且在实际情况中能够显著减少援助分配的不平等性。
## 3. `cs.AI` - 零样本分割通过原型引导实现多标签植物物种识别 [PDF](https://arxiv.org/pdf/2512.19957), [HTML](https://arxiv.org/abs/2512.19957)
### Authors
Luciano Araujo Dourado Filho,Almir Moreira da Silva Neto,Rodrigo Pereira David,Rodrigo Tripodi Calumby
### Background
本文介绍了一种为解决PlantClef 2025挑战开发的方法。挑战涉及高分辨率图像上的细粒度多标签物种识别。该方法专注于使用从训练集获得的类原型作为代理指导，以训练分割ViT模型在测试集图像上的训练。
### Innovation
提出的解决方案通过提取训练数据集的特征，并通过K-Means聚类创建类原型，这些建立在预训练的DinoV2上的定制窄ViT模型用于重建训练集类原型，以指导分类过程。这种方法能够适应多类识别到多标签分类的领域适应。
### Conclusion
本文方法在PlantCLEF 2025挑战的私人排行榜上获得了第5名，F1分数为0.33331，且在绝对性能上比最高得分的提交仅低0.03，表明其在基准任务中取得了竞争力的性能。代码可从指定链接获取。
## 4. `cs.AI` - 通过流匹配发现李群 [PDF](https://arxiv.org/pdf/2512.20043), [HTML](https://arxiv.org/abs/2512.20043)
### Authors
Jung Yeon Park,Yuxuan Chen,Floor Eijkelboom,Jan-Willem van de Meent,Lawson L.S. Wong,Robin Walters
### Background
对称性在理解物理系统方面至关重要，同时在机器学习中可以提高性能和样本效率。要实现这一点，需要了解数据背后的各种对称性。现有的方法往往局限在特定类型的对称性，并且需要较多的假设。
### Innovation
提出了一种通过在李群上进行流匹配直接从数据中学习对称性的方法，称为?lieflow。这种方法可以在更多类型的数据中发现对称性，且所需的假设较少。实验表明，在2D和3D点云数据中成功地发现离散群，包括通过在复数域上进行流匹配发现反射。
### Conclusion
尽管基于流匹配的方法在发现对称性方面表现出色，但在具有对称排列的目标模式下可能会出现“最后一刻的收敛”问题，研究人员提出了一种新的插值方案来解决这一问题。
## 5. `cs.AI` - 为灾害响应生成位置意识：一种概率跨视角地理定位方法 [PDF](https://arxiv.org/pdf/2512.20056), [HTML](https://arxiv.org/abs/2512.20056)
### Authors
Hao Li,Fabian Deuser,Wenping Yin,Steffen Knoblauch,Wufan Zhao,Filip Biljecki,Yong Xue,Wei Huang
### Background
随着地球气候的变化，灾害和极端天气事件变得越来越频繁和强烈。应对灾害事件的快速和高效响应对于气候适应性和可持续性至关重要。然而，快速而准确地识别灾害地点以支持决策和资源分配是一项关键挑战。
### Innovation
本文提出了一个概率跨视角地理定位方法（简称ProbGLC），旨在通过生成的位置意识来加速灾害响应。该方法结合了概率和确定性地理定位模型，构建了一个综合框架，同时提高模型解释性（通过不确定性量化）并达到最先进的地理定位性能。
### Conclusion
通过对两种跨视角灾害数据集（即MultiIAN和SGAGAINDisaster）进行广泛的实验，验证了ProbGLC在地理位置准确性（@1公里准确度为0.86，@25公里准确度为0.97）和模型解释性（通过概率分布和位置可确定性分数）方面的优越性，表明了利用生成的跨视角方法提高位置意识以实现更快更好的灾害响应的巨大潜力。
## 6. `cs.AI` - 从无动作视频中学习技能 [PDF](https://arxiv.org/pdf/2512.20052), [HTML](https://arxiv.org/abs/2512.20052)
### Authors
Hung-Chieh Fang,Kuo-Han Hung,Chu-Rong Chen,Po-Jung Chou,Chun-Kai Yang,Po-Chen Ko,Yu-Chiang Wang,Yueh-Hua Wu,Min-Hung Chen,Shao-Hua Sun
### Background
通过学习视频中的丰富视觉和时间先验信息，向通用型机器人提供了有希望的发展路径。现有视频生成模型虽然能够生成令人印象深刻的视觉预测，但难以用于低级动作。相比之下，潜在动作模型能更好地将视频与动作对齐，但它们通常只能处理单一步骤，缺乏高级规划能力。
### Innovation
我们通过引入基于光流的潜在技能抽象 (SOF) 框架来弥合这一差距，该框架能够从大量无动作视频中学习潜在技能。我们的核心思想是通过基于光流的中间表示来构建技能的潜在空间，该表示可以捕捉与视频动态和机器人动作都对齐的运动信息。通过在这一基于流的潜在空间中学习技能，SOF 能够实现对视频导出技能的高级规划，并使得这些技能更易于翻译为动作。
### Conclusion
实验表明，我们的方法在多任务和长时序设置中都一致提高了表现，证明了能够直接从原始视觉数据中获取和组合技能的能力。
## 7. `cs.AI` - FGDCC: 细粒度深度聚类分类 -- 一种针对植物分类中类内变异性的框架 [PDF](https://arxiv.org/pdf/2512.19960), [HTML](https://arxiv.org/abs/2512.19960)
### Authors
Luciano Araujo Dourado Filho,Rodrigo Tripodi Calumby
### Background
在细粒度视觉分类（FGVC）任务中，类内变异性根据图像间差异的程度具有显著性。这种变异性有时会阻碍深度学习模型的学习过程，尤其是在类别也处于欠代表状态的情况下。这种情况在植物分类任务中极其常见。现有的方法需要探索如何缓解类内变异性问题，以便更好地学习细粒度视觉特征。
### Innovation
本文提出了一种新颖的方法，旨在通过学习基于类的聚类分配来进行细粒度特征分类，从而提高FGVC任务中的分类性能。该方法通过个体类别的聚类来发现伪标签，这些标签能够编码图象之间的潜在相似度。此类标签可用于分层分类过程，以学习更细粒度的视觉特征，从而缓解类内变异性问题。实验表明，尽管该方法的一些组件尚未完全优化，但仍能达到PlantNet300k数据集的最新技术水平。此代码已在此网页可用。http://www.example.com
### Conclusion
初步实验证明该方法有效缓解了类内变异性问题，但仍需要进一步研究以获得更多关于该方法有效性的明确证据。
## 8. `cs.AI` - PhysMaster: 构建自主AI物理学家进行理论和计算物理学研究 [PDF](https://arxiv.org/pdf/2512.19799), [HTML](https://arxiv.org/abs/2512.19799)
### Authors
Tingjia Miao(1 and 2 and 5),Jiawen Dai(2),Jingkun Liu(2),Jinxin Tan(2 and 3 and 4),Muhua Zhang(2 and 3 and 4),Wenkai Jin(1),Yuwen Du(1),Tian Jin(1),Xianghe Pang(1),Zexi Liu(1),Tu Guo(2 and 4),Zhengliang Zhang(2 and 4 and 5),Yunjie Huang(1),Shuo Chen(6),Rui Ye(1),Yuzhi Zhang(7),Linfeng Zhang(7),Kun Chen(6),Wei Wang(2 and 3 and 4),Weinan E(1),Siheng Chen(1) ((1) School of Artificial Intelligence, Shanghai Jiao Tong University, (2) School of Physics and Astronomy, Shanghai Jiao Tong University, (3) State Key Laboratory of Dark Matter Physics, Shanghai Jiao Tong University, (4) Tsung-Dao Lee Institute, Shanghai Jiao Tong University, (5) Zhiyuan College, Shanghai Jiao Tong University, (6) Institute of Theoretical Physics, Chinese Academy of Sciences, (7) DP Technology)
### Background
随着大模型的进步，已经生成了与人类科学家知识和操作能力相当的智能代理，表明此类系统有望协助、加速和自动化研究。然而，现有研究主要针对单一定义良好的基准或一般任务（如文献检索）进行评估，这限制了它们在开放科学研究场景中的端到端问题解决能力。特别是在物理学领域，该领域高度抽象、数学密集，并要求将分析推理与基于代码的计算结合起来。
### Innovation
本文提出PhysMaster，这是一种基于大模型的代理，具备自主理论物理学家和计算物理学家的功能。它将抽象推理与数值计算结合，并利用LANDAU（分层学术数据宇宙）来保存检索的文献、精心选择的先前知识以及验证的方法论痕迹，增强决策的可靠性和稳定性。此外，PhysMaster还采用了一种平衡效率和开放探索的自适应探索策略，使它在超长期任务中表现出稳健的性能。
### Conclusion
PhysMaster在高能物理学理论、凝聚态物理学理论和天体物理学问题上进行了评估，表明它可以加速研究、自动化假设驱动的循环以及自主探索开放性问题，实现了理论与计算物理学研究的自动化和加速。
## 9. `cs.AI` - 使用大语言模型扩展内容审核的强化学习 [PDF](https://arxiv.org/pdf/2512.20061), [HTML](https://arxiv.org/abs/2512.20061)
### Authors
Hamed Firooz,Rui Liu,Yuchen Lu,Zhenyu Hou,Fangzhou Xiong,Xiaoyang Zhang,Changshu Jian,Zhicheng Zhu,Jiayuan Ma,Jacob Tao,Chaitali Gupta,Xiaochang Peng,Shike Mei,Hang Cui,Yang Qin,Shuo Tang,Jason Gaedtke,Arpit Mittal
### Background
在当今互联网环境中，大规模的内容审核仍是一个巨大的挑战。每天都有大量用户和AI生成的内容需要不断评估，以防止政策违规。虽然最新的大型语言模型（LLMs）已经在政策导向的审核中显示出强大的潜力，但在实际场景中训练这些系统以达到专家级别的准确度，尤其是在标签稀疏、政策定义不断变化以及需要超越简单模式匹配的复杂推理的情况下，仍然存在未被充分探索的难题。
### Innovation
我们通过大规模的实证研究，系统评估了多种强化学习（RL）培训配方和奖励塑造策略，包括可验证奖励和大语言模型（LLM）作为法官的机制，来转化通用语言模型为专门的、政策对齐的分类器，涵盖三个实际内容审核任务。我们发现，RL在性能随着训练数据、模拟和优化步骤的增加而平滑提升并逐渐饱和的表现出Sigmoid特性。此外，我们证明了RL在需要复杂政策导向的推理任务中显著提高了性能，相比监督微调，数据效率提高高达100倍，使其特别适用于专家注解稀缺或成本高昂的领域。
### Conclusion
我们的研究结果为工业规模的审核系统提供了实际的见解，同时也展示了在内容审核中使用RL的潜力，有效地提高了系统性能和数据利用效率，特别是在缺乏或成本高昂的情况下。
## 10. `cs.AI` - S$^3$IT：虚拟空间社交智能测试基准 [PDF](https://arxiv.org/pdf/2512.19992), [HTML](https://arxiv.org/abs/2512.19992)
### Authors
Zhe Sun,Xueyuan Yang,Yujie Lu,Zhenliang Zhang
### Background
将具身代理融入人类环境需要具备具身的社会智能，这包括理解社交规范和物理约束。现有的评估方法要么局限于虚化的社交推理（例如，在文本中），要么只处理没有社交考虑的物理任务。这两种方式都无法评估代理在现实、具身环境中的综合和权衡物理及社会约束的能力。
### Innovation
我们提出了一个名为S$^3$IT的基准测试，旨在评估具身社交智能。该测试基于一个新颖且具有挑战性的座位排列任务，要求代理为一群具有多样身份、偏好和复杂人际关系的大语言模型驱动（LLM驱动）的NPC安排座位。我们的程序可扩展框架可以生成大量的可控制难度的场景，迫使代理通过主动对话来获取偏好，通过自主探索感知环境，并在复杂的约束网络中进行多目标优化。
### Conclusion
我们对当前最先进的LLM进行了S$^3$IT的评估，结果显示他们在解决此问题时仍然存在困难，与人类基准相比仍有明显差距。结果表明，LLM在空间智能方面存在不足，但同时展示了在带有明确文本线索的冲突解决中接近人类水平的能力。
## 11. `cs.CV` - 量子机器学习时代的机器遗忘: 实证研究 [PDF](https://arxiv.org/pdf/2512.19253), [HTML](https://arxiv.org/abs/2512.19253)
### Authors
Carla Crivoi,Radu Tudor Ionescu
### Background
尽管机器遗忘（MU）在经典深度学习中被广泛研究，但在变量子电路（VQCs）和量子增强架构中的行为尚未得到充分探索。本文首次进行了全面的实证研究，评估了量子模型的MU能力，并探讨了其在不同深度和结构下的表现。
### Innovation
本文提出了广泛适应量子环境的遗忘方法，包括基于梯度、基于蒸馏、基于正则化和认证技术，并引入了两种新的专门针对混合模型的遗忘策略。通过在Iris、MNIST和Fashion-MNIST数据集上的实验，研究了不同电路深度、纠缠结构和任务复杂性对量子模型MU的影响。
### Conclusion
研究表明，某些方法（如EU-k、LCA和认证遗忘），始终能提供在各项指标上最佳的平衡点。本文为量子机器遗忘提供了基本的实证洞察，并指出了需要具有量子意识的算法和理论保证的需求，随着量子机器学习系统规模和能力的扩大。
## 12. `cs.LG` - 针对频繁模型更新的轴向权重差异 [PDF](https://arxiv.org/pdf/2512.19720), [HTML](https://arxiv.org/abs/2512.19720)
### Authors
Stefan Kuyumdzhiev,Radostin Cholakov
### Background
由于微调的检查点大小庞大，导致加载这些特定任务的大型语言模型变体时存在冷启动延迟问题。尽管微调权重与基础模型相比相对较小且具有结构化的残差，但仍需要大量的存储空间来加载这些微调后的权重。
### Innovation
提出了一种简单的1位差值方案，该方案仅存储权重差异的符号，并结合轻量化的沿轴（行/列）FP16标度因子，这些标度因子是从少量校准集中学习而来。此设计保留了1位差值的紧凑性，同时更准确地捕捉权重维度的变化，提高了重建质量。从系统角度来看，该方法通过在每个模块中进行单一操作来传输打包的差值，从而减少了冷启动延迟和存储开销。
### Conclusion
该方法直接集成，所需校准数据量小，并能够保持推理效率，避免了密集重建。实验设置和源代码可在提供的链接中找到。
## 13. `cs.LG` - 热力学聚焦对推断时搜索：目标条件采样和提示推断的实用方法 [PDF](https://arxiv.org/pdf/2512.19717), [HTML](https://arxiv.org/abs/2512.19717)
### Authors
Zhan Zhang
### Background
在语言生成、规划和强化学习等领域中，寻找稀少但有用的目标解决方案是一个反复出现的实践挑战。在非常大的候选空间中，高效地找到这些目标解决方案是具有挑战性的。
### Innovation
本文提出了一种实用框架——逆因果聚焦算法（ICFA），将搜索视为条件导向的重权重过程。ICFA 通过利用现有的提案采样器和特定任务的相似性函数，形成聚焦的采样分布，同时通过自适应地控制聚焦强度以防止退化。文中提供了清晰的实现步骤，基于有效样本大小的稳定性诊断，还给出了一些简明的理论解释以及两个可复现的实验：受限语言生成和稀疏奖励导航。此外，文章还展示了结构化提示作为ICFA的一种近似语言级别形式的应用，并描述了一种结合提示推理与算法加权的混合架构。
### Conclusion
文章进一步表明结构化提示可以实现ICFA的语言级别近似，并描述了一种新的混合架构结合了提示推理与算法权重。
## 14. `cs.LG` - 锂离子电池剩余使用寿命预测的多尺度双路径特征聚合网络 [PDF](https://arxiv.org/pdf/2512.19719), [HTML](https://arxiv.org/abs/2512.19719)
### Authors
Zihao Lv,Siqi Ai,Yanbin Zhang
### Background
当前评估电池降级序列的局部和全局关联性的建模技术效率低下，难以满足实际应用需求。为此，本文提出了一个多尺度双路径特征聚合网络（MDFA-Net），用于预测剩余使用寿命（RUL）。
### Innovation
本文创新地提出了一种新的深度学习架构——多尺度双路径特征聚合网络（MDFA-Net），该网络由两条路径组成：第一路径是保持浅层信息并避免信息丢失的多尺度特征网络（MF-Net），第二路径是捕捉序列连续趋势并保留深层细节的编码网络（EC-Net）。有效地综合了深层次和浅层次的信息，能够同时捕捉局部和全局模式。
### Conclusion
在两个公开的锂离子电池数据集上的测试表明，本文的方法在剩余使用寿命预测中超过了现有的顶级方法，能够准确绘制容量衰退轨迹。
## 15. `cs.LG` - 使用多中心数据开发和外部验证重症患者多模态人工智能死亡率预测模型 [PDF](https://arxiv.org/pdf/2512.19716), [HTML](https://arxiv.org/abs/2512.19716)
### Authors
Behrooz Mamandipoor,Chun-Nan Hsu,Martin Krause,Ulrich H. Schmidt,Rodney A. Gabriel
### Background
在重症监护病房（ICU）中，早期预测住院死亡率对于优化治疗至关重要。该研究旨在利用结构化和非结构化临床数据开发一种跨模态深度学习模型，以预测重症患者在初始24小时ICU住院后住院期间的死亡风险。
### Innovation
研究开发了一种跨模态模型，融合了24小时内ICU入院的相关时序数据，并成功利用MIMIC-III、MIMIC-IV、eICU和HiRID等多中心数据集进行模型训练和验证。该模型不仅采用了时间不变变量、时间变量、临床病历和胸部X光图像作为输入，还能通过外部验证在不同的医疗中心得到验证，从而验证其泛化能力。
### Conclusion
研究发现，结合结构化数据点的模型在AUROC、AUPRC和Brier评分上的表现分别为0.92、0.53和0.19。将临床笔记和影像数据纳入模型后，这些评分进一步提升。该研究强调了整合多种患者信息源对于死亡率预测的重要性，并且通过多中心数据进行外部验证，进一步展示了该模型的泛化能力。
## 16. `cs.LG` - 面向EDA云作业资源和生命周期预测的大语言模型 [PDF](https://arxiv.org/pdf/2512.19701), [HTML](https://arxiv.org/abs/2512.19701)
### Authors
Yuxuan Yin,Shengke Zhou,Yunjie Zhang,Ajay Mohindra,Boxun Xu,Peng Li
### Background
电子设计自动化（EDA）行业中云 computing 的迅速发展，促使需要对资源和作业生命周期进行准确预测，以便实现最优调度。传统机器学习方法在处理EDA工作负载的复杂性和异构性方面表现不佳，需要大量的特征工程和领域专业知识。
### Innovation
提出了一种新的框架，通过文本到文本回归微调大型语言模型（LLMs）来应对这一挑战。引入了科学记数法和前缀填充来约束LLMs，显著提高了输出格式的可靠性。此外，发现全注意力微调和推理可以提高滑动窗口注意力LLMs的预测准确性。
### Conclusion
在实际云数据集上展示了所提框架的有效性，设定了EDA领域性能预测的新基准。
## 17. `cs.CV` - 范畴对称深度学习：范畴对称神经网络与普遍逼近定理 [PDF](https://arxiv.org/pdf/2511.18417), [HTML](https://arxiv.org/abs/2511.18417)
### Authors
Yoshihiro Maruyama
### Background
该论文基于对称神经网络的发展，统一了群/群胚对称网络、偏序集/格对称网络、图神经网络和层神经网络。
### Innovation
作者提出了一种范畴对称神经网络（CENNs）理论，将对称性形式化为拓扑范畴中带有拉东测度的自然性。此外，作者证明了在一般设置下对称通用逼近定理：有限深度CENNs在连续对称变换空间中稠密。
### Conclusion
该理论框架扩展了对称深度学习的边界，不仅包含了几何对称性，还涵盖了上下文和组合对称性，并为群/群胚、偏序集/格、图和细胞层提供了一种系统的方法来推导通用逼近定理。
## 18. `cs.CV` - LoGoPlanner：基于度量感知视觉几何的定位导向导航策略 [PDF](https://arxiv.org/pdf/2512.19629), [HTML](https://arxiv.org/abs/2512.19629)
### Authors
Jiaqi Peng,Wenzhe Cai,Yuqiang Yang,Tai Wang,Yuan Shen,Jiangmiao Pang
### Background
在非结构化环境中规划轨迹是移动机器人的一项基本且具有挑战性的能力。传统的模块化流程在感知、定位、制图和规划模块之间存在延迟和累积错误。最近的端到端学习方法直接将原始视觉观察映射到控制信号或轨迹，优化了开放世界环境中的性能和效率。然而，大多数端到端方法仍依赖于需要精准传感器外部校准的单独定位模块，从而限制了其在不同实体和环境中的一般化能力。
### Innovation
我们提出了LoGoPlanner，一种基于定位的端到端导航框架，通过：(1) 调整长时视觉几何骨干网络，使其进行绝对度量尺度下的预测，从而提供隐式状态估计，确保准确的定位；(2) 从历史观察中重构周围的场景几何，提供密集、细致的环境感知，以实现可靠的避障；(3) 在辅助任务启发的隐式几何上条件化策略，从而减少误差传播。这种设计在模拟和现实世界的评估中显示，累积误差减少，基于度量几何的记忆增强了规划的一致性和避障能力，性能大幅提升。
### Conclusion
在仿真实验和真实环境中，LoGoPlanner的全端到端设计减少了累积误差，度量感知几何记忆提高了规划稳定性和避障能力，与基于精准定位的基准相比，性能提高了27.3%以上。这种设计还显示了强大的跨实体和环境的一般化能力。相关代码和模型已公开发布。
## 19. `cs.LG` - 通过可穿戴设备减少人体活动识别中的标签依赖性：从监督学习到新颖的弱自监督方法 [PDF](https://arxiv.org/pdf/2512.19713), [HTML](https://arxiv.org/abs/2512.19713)
### Authors
Taoran Sheng,Manfred Huber
### Background
使用可穿戴传感器进行人体活动识别（HAR）已通过各种机器学习方法发展起来，每种方法都有其固有的性能和标记需求之间的权衡。尽管完全监督技术能够达到高精度，但它们需要成本高昂且耗时的大量标记数据集。相比之下，无监督方法无需标记但通常性能较差。本文对基于穿戴设备的HAR进行了全面的监督范围研究，特别关注那些能够最大限度地减少标记需求同时保持竞争力的新型方法。
### Innovation
本文开发并实证比较了六种方法：（1）传统的完全监督学习，（2）基本的无监督学习，（3）具有约束条件的弱监督学习方法，（4）具有知识共享的多任务学习方法，（5）基于领域专业知识的自我监督方法，以及（6）一种新颖的结合领域知识和少量标记数据的弱自我监督学习框架。实验结果表明：（1）我们的弱监督方法在显著减少监督需求的同时，性能可与完全监督方法媲美；（2）提出的一种多任务框架通过相关任务的知识共享来提高性能；（3）我们的弱自我监督方法仅使用10%的标记数据就能展现出了显著的效率。
### Conclusion
这些结果不仅强调了不同学习范式的互补优势，为基于标记数据的可用性定制HAR解决方案提供了有益的见解，还证实了我们提出的一种新颖的弱自我监督框架最适合于实际应用中的HAR，其中标记数据有限。
## 20. `cs.LG` - 合成数据蓝图（SDB）：一种用于合成表格数据的统计、结构和图基于评估的模块化框架 [PDF](https://arxiv.org/pdf/2512.19718), [HTML](https://arxiv.org/abs/2512.19718)
### Authors
Vasileios C. Pezoulas,Nikolaos S. Tachos,Eleni Georga,Kostas Marias,Manolis Tsiknakis,Dimitrios I. Fotiadis
### Background
在人工智能迅速发展的时代，合成数据被广泛用于加速创新，同时保护隐私并扩大数据的可用性。然而，合成数据的评估仍然分散在异构指标、临时脚本和不完整报告的实践中。
### Innovation
我们引入了合成数据蓝图（SDB），一种模块化的基于Python的库，用于定量和可视化评估合成表格数据的保真度。SDB支持自动生成特征类型检测、分布性和依赖性级别的保真度指标、基于图和嵌入的结构保存分数，以及丰富的数据可视化方案。
### Conclusion
为了展示SDB的广度、稳健性和领域无关的应用性，我们在三个实质上不同的实际应用场景中评估了框架，包括医疗诊断、社会经济和金融建模以及网络安全和网络流量分析。这些应用场景展示了SDB如何解决各种数据保真度评估挑战，既适用于混合类型临床变量，也适用于高基数分类属性和高维遥测信号，并且提供了一致、透明和可重复的基准评估，直接跨不同领域。
