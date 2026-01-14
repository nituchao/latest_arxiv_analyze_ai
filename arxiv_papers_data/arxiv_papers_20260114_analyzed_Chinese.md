# 20260114
[![Subscribe_Visitors](https://visitor-badge.laobi.icu/badge?page_id=nituchao.latest_arxiv_analyze_ai_rss)](https://github.com/nituchao/latest_arxiv_analyze_ai)

## 1. `cs.AI` - 利用因果图引导思考链自动生成启发式学习问题 [PDF](https://arxiv.org/pdf/2601.06098), [HTML](https://arxiv.org/abs/2601.06098)
### Authors
Nicholas X. Wang,Neel V. Parpia,Aaryan D. Parikh,Aggelos K. Katsaggelos
### Background
直观学习对于培养深入概念理解至关重要，特别是在STEM教育领域，学生常难以理解和掌握抽象且相互关联的概念。自动问题生成已成为个性化和自适应学习的有效策略，但大语言模型（LLMs）的幻觉问题是其效果的瓶颈，可能会生成事实错误、含义模糊或教学不一致的问题。
### Innovation
提出了一种结合因果图引导的思考链（CoT）推理与多代理LLM架构的新型框架，以确保生成准确、相关且符合课程的问题。因果图提供领域知识的显式表示，而思考链推理则支持相关概念的结构化、逐步推理。每个专门的LLM代理负责特定任务，如图路径查找、推理、验证和输出，所有工作均在领域约束内。双阶段验证机制在概念层和输出层显著减少了幻觉问题。
### Conclusion
实验结果表明，该方法相比参考方法的质量提高了70%以上，并在主观评估中取得了非常有利的结果。
## 2. `cs.AI` - 无限长度外推：一种统一方法 [PDF](https://arxiv.org/pdf/2601.06113), [HTML](https://arxiv.org/abs/2601.06113)
### Authors
Nitin Vetcha
### Background
大型语言模型（LLMs）革命性地改变了自然语言处理领域，但由于训练过程中上下文窗口大小的限制，它们处理长序列的能力本身是有限的。现有方法在长度外推时常会遇到性能下降或计算效率低效的问题。
### Innovation
本文提出了一种统一框架，解释位置编码方法为注意力分数的乘法变换和加性偏置的分解。基于这一框架，我们引入了自适应位置编码（APE），它通过自适应频率调制和精心设计的衰减偏置（包括线性、对数和平方根项）解决了这些不足。理论分析确定了无限上下文外推的条件，确保在无界序列上保持softmax归一化定义的同时保留长距离相关性、熵有界性和梯度位置敏感性。
### Conclusion
我们通过在TinyStories数据集和新的合成数据集'Long Tiny Stories'（包含最多32,000字的故事）上进行实验，验证了我们的主张，并提供了相关的代码、数据集和模型权重供大家使用。
## 3. `cs.AI` - 从RLHF到直接对齐：大型语言模型偏好学习的理论统一 [PDF](https://arxiv.org/pdf/2601.06108), [HTML](https://arxiv.org/abs/2601.06108)
### Authors
Tarun Raheja,Nilay Pochhi
### Background
随着大型语言模型（LLMs）与人类偏好的对齐成为确保AI安全和有益性的关键因素，尽管Reinforcement Learning from Human Feedback (RLHF)已经建立了主导范式，但出现了一系列替代方案，包括Direct Preference Optimization (DPO)、Identity Preference Optimization (IPO)、Kahneman-Tversky Optimization (KTO)、Simple Preference Optimization (SimPO)等，这让实践者在选择方法时缺乏明确的指导。
### Innovation
这篇论文提供了一种偏好学习方法的理论统一，揭示了表面的多样性实际上可以通过三个正交的轴进行理性选择：(I) preference model（目标的基础似然模型），(II) regularization mechanism（对参考策略偏差的控制机制），(III) data distribution（在线学习与离线学习及覆盖要求）。论文还提供了精确的定义和定理，包括在线与离线方法的覆盖分离、奖励过度优化的标度法则以及直接对齐方法失败的条件。此外，分析指出了特定设计选择组合导致的失败模式，如长度作弊、模式崩溃和似然位移。通过综合分析50多篇论文的结果，提供了实践者的决策指南。
### Conclusion
该框架将偏好学习从一种经验性艺术转变为一种基于理论的学科。
## 4. `cs.AI` - 结构感知的多样性追求作为AI安全策略对抗同质化 [PDF](https://arxiv.org/pdf/2601.06116), [HTML](https://arxiv.org/abs/2601.06116)
### Authors
Ian Rios-Sialer
### Background
生成式AI模型在训练数据中存在偏差，并且可以通过模式崩溃进一步放大这些偏差，导致有害的多样性减少，我们称之为同质化。研究者认为同质化应当是AI安全中的主要关注点。
### Innovation
提出了xeno-繁殖作为一种降低同质化的策略，并且为自回归的大语言模型（LLM）提出了结构感知的多样性追求形式化方法。
### Conclusion
研究为对抗同质化提供了基础性的贡献，旨在开启一条重要研究线路并邀请合作以推进多样性。
## 5. `cs.AI` - CBMAS: 通过激活导向进行的认知行为建模 [PDF](https://arxiv.org/pdf/2601.06109), [HTML](https://arxiv.org/abs/2601.06109)
### Authors
Ahmed H. Ismail,Anthony Kuang,Ayo Akinkugbe,Kevin Zhu,Sean O'Brien
### Background
大型语言模型（LLMs）在不同提示、层级和上下文中的认知行为表现出不可预测性，这使得诊断和控制变得困难。现有的分析框架通常侧重于离散的前后干预分析，并在一定程度上限制了理解和控制LLMs认知行为的能力。
### Innovation
本文提出了一种名为CBMAS的诊断框架，用于连续激活引导。该框架不仅扩展了认知偏差分析的应用范围，还将之前的离散干预分析转变为可解释的轨迹分析。通过结合引导向量构建、密集α扫描、逻辑镜像偏差曲线以及层级位置敏感性分析，该方法能够揭示细微干预如何改变模型行为，并展示从浅层到深层的引导效果变化，实现高级行为评估与低级表征动态之间的桥梁，提高LLMs的认知可解释性。
### Conclusion
综合来看，CBMAS为LLMs的认知可解释性提供了新的视角，并通过可解释的数字工具和数据集增强了LLMs的透明度。
## 6. `cs.AI` - 关于arXiv:2511.21731v1的评论：在人工智能语言中识别量子结构——人类和人工认知的进化趋同证据 [PDF](https://arxiv.org/pdf/2601.06104), [HTML](https://arxiv.org/abs/2601.06104)
### Authors
Krzysztof Sienicki
### Background
本文是对arXiv:2511.21731v1论文的技术评估，重点关注其对报道的CHSH/Bell型计算结果和玻色-爱因斯坦(BE)拟合的理解可能超出被描述程序的支持范围的部分，以及“能级间距”类比中的内部不一致性。文章旨在澄清观测结果对量子纠缠的含义，特别是在“能量”由排名定义的情况下。
### Innovation
作者指出论文在解释报告的CHSH/Bell型计算和玻色-爱因斯坦拟合时可能存在过度解读的问题，并指出了“能级间距”类比中的一个内部矛盾，旨在保持有趣的经验性观察，使读者能够清晰理解这些观察对量子纠缠的涵义。
### Conclusion
作者强调了该研究中的一些问题，并提出了如何澄清和重新解释结果的建议，以避免过度解读，同时保留其潜在的科学兴趣。
## 7. `cs.AI` - 动态智能天花板：衡量人工系统在长周期内规划和创造力的上限 [PDF](https://arxiv.org/pdf/2601.06102), [HTML](https://arxiv.org/abs/2601.06102)
### Authors
Truong Xuan Khanh,Truong Quynh Hoa
### Background
近年来，人工智能取得的进步使其在众多任务上表现出非凡的性能。然而，随着系统的性能不断达到新的高度，人们越来越关注它们在未来长期发展中的表现模式，很多系统表现出对重复解决方案的依赖，而非持续提升。我们提出，现代AI系统的瓶颈并非能力本身，而在于其过早固定了自己的表现边界。本文引入“动态智能天花板”（DIC）的概念，这是一个系统在特定资源、内部意图和结构配置下可达到的最高智能水平。
### Innovation
本文提出了衡量人工系统长周期规划和创造力上限的“动态智能天花板”理念，提出了一个基于轨迹的评价框架，该框架衡量智能作为一个可移动的边界而非静态截图。通过这种方式，引入了两个评估器：“渐进难度天花板”（PDC）和“天花板漂移率”（CDR），并使用程序生成的基准环境来评估长期规划和结构创造力。
### Conclusion
研究结果显示，系统在长周期中表现出的是深化现有解决方案的利用还是智能边界的持续扩展存在质的区分。本文并未设定无限制的智能，而是将限制重新定义为动态和轨迹依赖的，而非静态和提前固定的。
## 8. `cs.AI` - 以LLM为动力的社交数字双胞胎：一种模拟政策干预对人群行为响应的框架 [PDF](https://arxiv.org/pdf/2601.06111), [HTML](https://arxiv.org/abs/2601.06111)
### Authors
Aayush Gupta,Farahan Raza Sheikh
### Background
预测人口对政策干预的响应是计算社会科学和公共政策领域的基本挑战。传统的方法依赖于描述历史相关性的聚合统计模型，这些模型缺乏机制的可解释性，并且难以应对新的政策情景。
### Innovation
本文提出了一种通用框架——社交数字双胞胎，其中大语言模型（LLMs）作为个体代理的认知引擎。每个代理由人口统计和心理特征描述，并接收政策信号，输出多维度的行为概率向量。计算层将聚合的代理响应映射为可观测的群体级指标，用于与实际数据的验证和虚拟政策分析的部署。通过COVID-19案例研究，在一个保留的测试期内，经过校准的数字双胞胎在六个行为类别上的宏平均预测错误率上，比梯度提升基线提高了20.7%。反事实实验展示了在政策变动作出单调和有界响应，建立了行为的合理性。该框架是无领域的，相同的架构可以应用于交通政策、经济干预、环境法规等任何涉及政策对人群行为影响的领域。
### Conclusion
该框架对于政策模拟具有重要意义，同时讨论了该方法的局限性，并指出了超越疫情响应的LLM基数字双胞胎的未来研究方向。
## 9. `cs.AI` - 梦不仅是bug：一种荣格启发式的多智能体大模型伴侣梦层 [PDF](https://arxiv.org/pdf/2601.06115), [HTML](https://arxiv.org/abs/2601.06115)
### Authors
V. Cheung
### Background
作者受到了个人对于知识共享障碍在日常硬件项目中的梦想启发，旨在重新定义大语言模型（LLM）伴侣中的可控离线幻觉现象，将其视为学习和关系建设的资源而非仅仅是一个可靠性的缺陷。该研究受到了荣格集体无意识理论的启发，集体无意识被视为共享的原型库。作者在此基础上引入了一个“人工集体无意识（ACU）”的概念，即一种共享的梦境池，智能体在其中贡献匿名的、抽象的交互模板，这些模板之后会被重新实例化为个性化的梦境叙述。
### Innovation
该研究提出的荣格启发式的“梦层”概念，使而非单纯的缺陷，而是一项资源，它重新定义了线上无标记幻觉为缺陷，而线下的有界、标记且延迟的幻觉则成为合成情景和深化伴侣关系的宝库，为多智能体大模型伴侣的安全与灵活性提供了一个新的视角。
### Conclusion
实验结果显示，梦层实现了一个关键的解耦：代理在安全约束（如安全政策）上保持不变的同时，在叙事策略上变得灵活（如使用共享的原型隐喻来解决死锁），从而将幻想重新概念化，在线的无标记实例仍被视为缺陷，但在限定条件下的有效叙述则成为了合成场景的丰富来源和深化同伴关系的工具，这一方法在反过拟合的梦境机制方面与当代神经科学中提出的建议相呼应。
## 10. `cs.AI` - L2CU: 学习补充未见用户 [PDF](https://arxiv.org/pdf/2601.06119), [HTML](https://arxiv.org/abs/2601.06119)
### Authors
Dileepa Pitawela,Gustavo Carneiro,Hsiang-Ting Chen
### Background
最近的研究表明，机器学习模型有可能学习来补充人类的能力（L2C）。然而，将这种能力推广到未见用户仍然是一项重大挑战。现有L2C方法通过单一的全局用户模型简单化了人机交互，忽视了个体用户差异，导致合作性能不足。
### Innovation
本文介绍了L2CU，一种新的L2C框架，用于未见用户的人机合作分类。L2CU通过识别代表性的标注者模式来辨识不同的标签模式，通过将未见用户与这些模式匹配，使用模式特定模型来补充用户，并达成优于联合准确度。
### Conclusion
我们通过CIFAR-10N、CIFAR-10H、Fashion-MNIST-H、Chaoyang和AgNews等多个数据集评估了L2CU，证明了它在提高人机合作分类方面的有效性和模型无关性解决方案。
## 11. `cs.AI` - 通过K-V缓存对齐实现潜空间通信 [PDF](https://arxiv.org/pdf/2601.06123), [HTML](https://arxiv.org/abs/2601.06123)
### Authors
Lucio M. Dery,Zohar Yahav,Henry Prior,Qixuan Feng,Jiajun Shen,Arthur Szlam
### Background
随着复杂问题的不断增加，大型语言模型（LLMs）需要从单个模型过渡到多模型系统，这些系统能够有效地协作。虽然文本历来是模型间通信的媒介，但如果模型能够直接访问彼此的内部状态，则可以实现更丰富和高效的交互。
### Innovation
本文提出了一种学习共享表示空间的方法，该空间使多个模型的k-v缓存对齐，从而创建一个高带宽的合作通道，无需修改预训练参数。通过为每个模型添加适配器来将其状态翻译成和从共享空间转换，实现了模型之间的无缝通信，并且提高了个别模型的性能。共享空间还允许技能，如软提示，直接在不同模型之间转移。
### Conclusion
本文的工作代表了一个重要进步，旨在未来模型可以灵活地共享知识和能力。
## 12. `cs.AI` - GroupSegment-SHAP: Group-Segment Players for Shapley Value Explanations in Multivariate Time Series [PDF](https://arxiv.org/pdf/2601.06114), [HTML](https://arxiv.org/abs/2601.06114)
### Authors
Jinwoong Kim,Sangjin Park
### Background
多元时间序列模型在健康、工业、能源和金融等领域展现了强大的预测性能，但它们如何结合交叉变量交互与时间动态仍然不明确。SHAP（SHapley Additive exPlanations）被广泛用于解释，但现有时间序列变体通常将特征和时间轴独立处理，导致在特定时间区间内由多个变量形成的结构信号被分割。
### Innovation
提出了一种新的方法GroupSegment SHAP (GS-SHAP)，它基于变量间的依赖性和时间分布变化构建解释单元作为团队成员，并通过Shapley归因量化每个单元的贡献。GS-SHAP在四种实际应用场景中得到评估：人类活动识别、电力系统预测、医学信号分析和金融时间序列，并与KernelSHAP、TimeSHAP、SequenceSHAP、WindowSHAP和TSHAP进行了比较。与时间序列SHAP基线相比，GS-SHAP在基于删除的忠实性（DeltaAUC）上平均提高了约1.7倍，同时在匹配的扰动预算下平均将壁 Clock 运行时间减少了约40%。一项金融案例研究表明，在高波动时期，GS-SHAP可以识别出可观测的多变量时间交互作用。
### Conclusion
GS-SHAP通过结合变量间的依赖性和时间分布变化来解释多变量时间序列模型，有效地提高了模型解释的忠实性和效率，特别是在高波动时期能够识别出有意义的交互作用。
## 13. `cs.AI` - 如何评估人工智能素养：自我报告与客观评估之间的偏差 [PDF](https://arxiv.org/pdf/2601.06101), [HTML](https://arxiv.org/abs/2601.06101)
### Authors
Shan Zhang,Ruiwei Xiao,Anthony F. Botelho,Guanze Liao,Thomas K.F. Chiu,John Stamper,Kenneth R. Koedinger
### Background
在K-12教育中广泛采用人工智能（AI）技术，突显了需要经过心理测量验证的教师AI素养测验的重要性。现有的研究主要依赖自我报告或基于目标的评估方法，但较少将两者统一在一个框架中进行比较，或探讨先前的AI素养经验如何影响这种关系。这限制了学习分析的可扩展性和基于学习者特征的不同教学设计的发展。
### Innovation
本文开发并评估了教师AI素养的自我报告和基于目标的测量方法，并在概念、应用、评估和伦理的既有框架下进行了验证。证实性因子分析支持构建有效性，具有良好的可靠性和可接受的拟合度。结果显示自我报告和基于目标的因素之间存在较低的相关性。潜在类别分析识别了六个不同的群体，其中包括自我报告高于实际情况、自我报告低于实际情况、自我报告与实际情况一致以及未接触AI素养经验的低自我报告/低基于目标类别。
### Conclusion
本研究理论上扩展了现有的AI素养框架，验证了自我报告和基于目标的测量方法在相似维度上的有效性和可靠性。实际应用方面，这些工具可作为专业发展的诊断工具，支持基于人工智能的决策（例如，发展监测、需求分析），并使面向不同教师子群体的可扩展学习分析干预成为可能。
## 14. `cs.AI` - 大规模多模态基准模型测评器 [PDF](https://arxiv.org/pdf/2601.06106), [HTML](https://arxiv.org/abs/2601.06106)
### Authors
Min-Han Shih,Yu-Hsin Wu,Yu-Wei Chen
### Background
本文提出了一种专门的多模态测评模型，旨在为多样化的任务提供可靠且可解释的评估。基准涵盖了文本、音频、图像和视频等多种模态，通过精心选取公共数据集并固定种子以确保可复制性和减小训练测试泄露现象。该测评模型不仅进行简单的评分，还整合了多模态判断，分析模型输出的质量和推理一致性，并生成诊断反馈。
### Innovation
模型框架能够聚合多模态判断，分析模型输出质量及推理一致性，并生成诊断反馈，而非仅采用简单的评分方法。此外，作者通过比较测评模型的评估与人类注释者的评估结果，展示了测评模型在可扩展性和可解释性方面的潜力。
### Conclusion
测评模型与人类评分高度一致，表明其作为未来多模态AI研究中可扩展且可解释性高的评估管道的潜力。
## 15. `cs.AI` - 非洲教育中负责任生成AI使用的铆接工程：来自为期三天培训系列的报告 [PDF](https://arxiv.org/pdf/2601.06121), [HTML](https://arxiv.org/abs/2601.06121)
### Authors
Benjamin Quarshie,Vanessa Willemse,Macharious Nabang,Bismark Nyaaba Akanzire,Patrick Kyeremeh,Saeed Maigari,Dorcas Adomina,Ellen Kwarteng,Eric Kojo Majialuwe,Craig Gibbs,Jerry Etornam Kudaya,Sechaba Koma,Matthew Nyaaba Matthew Nyaaba
### Background
生成型人工智能（GenAI）工具在教育领域的应用越来越广泛，但许多教育者缺乏关于如何负责任地和情境敏感地进行提示工程的结构化指导，特别是在非洲和资源有限的地区。这导致了对该领域的关注，特别是在非洲需要定制化的培训和支持。
### Innovation
该论文报道了一项由GenAI for Education and Research in Africa（GenAI-ERA）组织的为期三天的在线专业发展项目，该项目旨在提升教育者和研究者在学术写作、教学和研究中对提示工程的伦理应用的能力。该项目成功地吸引了来自多个国家的468名参与者，并通过循序渐进的方式进行培训，包括基础提示设计和实际行动中的伦理策略。
### Conclusion
研究表明，参与者逐渐将提示工程视为一种需要伦理意识、情境敏感性和教育判断的AI素养，而不仅仅是技术技能。报告指出非洲地区在访问、本地相关培训材料和机构支持方面存在持续性的挑战，并建议持续的专业发展和将提示素养纳入课程，以支持非洲教育系统中负责任的GenAI使用。
## 16. `cs.AI` - 数据污染对后训练的影响 [PDF](https://arxiv.org/pdf/2601.06103), [HTML](https://arxiv.org/abs/2601.06103)
### Authors
Muhammed Yusuf Kocyigit,Caglar Yildirim
### Background
本文研究了数据集污染如何与大型语言模型训练管道中现在标准的后训练阶段相互作用。研究基于Qwen2.5（500M/1.5B）和Gemma3（1B/4B）的干净检查点，向一个250M增量预训练数据集的前20亿个令牌中注入GSM8K和MBPP测试项目五份副本，然后在经过两种常见后训练方法——监督微调（SFT）和基于组相对策略优化的强化学习（RL-GRPO）之后，对比受污染和未受污染模型的表现。
### Innovation
文章创新性地通过控制实验研究了数据集污染在模型训练与后训练阶段的交互影响，以及不同后训练方法（如SFT和RL-GRPO）如何处理这些污染数据，特别关注了污染数据对性能的影响模式，模型规模的变化如何影响这些现象。
### Conclusion
研究发现，污染会导致成绩短期内上升，但长期预训练可逐步消减这种影响；SFT和RL-GRPO都能恢复污染信息，但方法不同；模型规模的影响也不同，较大SFT模型更容易记住污染内容，而较大GRPO模型则将记忆转化为更为泛化的技能；因此，建议在后训练后进行数据污染的审计，并认为基于RL的后训练方法虽然不是完全免疫，但可以减轻污染相关的过度估计问题。
## 17. `cs.AI` - COVR: Collaborative Optimization of VLMs and RL Agent for Visual-Based Control [PDF](https://arxiv.org/pdf/2601.06122), [HTML](https://arxiv.org/abs/2601.06122)
### Authors
Canming Xia,Peixi Peng,Guang Tan,Zhan Su,Haoran Xu,Zhenxian Liu,Luntong Li
### Background
视觉强化学习（RL）在复杂任务中因高维度观测而表现出较差的样本效率。现有的工作展示了视觉-语言模型（VLMs）可以辅助RL，但往往集中在从VLM到RL的知识蒸馏上，忽视了RL生成的交互数据对VLM的潜在增强作用。
### Innovation
本文提出了COVR，一个协作优化框架，旨在实现VLM和RL策略的互相增强。COVR通过细调VLM并与RL生成的数据一起使用增强后的VLM进一步指导策略学习，引入了两个关键模块：探索驱动动态过滤模块和回报感知自适应损失权重模块，以及逐步调整策略来减少资源消耗。
### Conclusion
广泛的实验表明，COVR在各种具有挑战性的基于视觉的控制任务中表现出强大的性能。
## 18. `cs.AI` - AIS-CycleGen: 基于CycleGAN的高保真合成AIS数据生成与增强框架 [PDF](https://arxiv.org/pdf/2601.06127), [HTML](https://arxiv.org/abs/2601.06127)
### Authors
SM Ashfaq uz Zaman,Faizan Qamar,Masnizah Mohd,Nur Hanis Sabrina Suhaimi,Amith Khandakar
### Background
自动识别系统（AIS）数据对于海上态势感知至关重要，但这些数据往往遭受领域偏移、数据稀疏性和类别不平衡的困扰，从而影响预测模型的性能。
### Innovation
本文提出了一种基于循环一致生成对抗网络（CycleGAN）的鲁棒数据增强方法AISCycleGen，该方法专门为AIS数据集设计。AISCycleGen利用未配对领域转换生成高保真合成AIS数据序列，无需配对源-目标数据。该框架采用具有自适应噪声注入的一维卷积生成器，以保留AIS轨迹的时空结构，增强生成数据的多样性和真实性。
### Conclusion
实验结果表明，AISCycleGen在各类海上领域中优于当前基于GAN的增强技术，实现PSNR值为30.5和FID得分38.9，表明AISCycleGen具有作为有效的通用解决方案用于增强AIS数据集以提高下游模型在实际海事情报应用中的性能的潜力。
## 19. `cs.AI` - 基于语义事件图的长格式视频问答 [PDF](https://arxiv.org/pdf/2601.06097), [HTML](https://arxiv.org/abs/2601.06097)
### Authors
Aradhya Dixit,Tianxi Liang
### Background
现代的视觉-语言模型在处理长格式视频时仍面临挑战，尤其是在长时间跨度的视频片段推理方面，这往往超过了实际的子单位和计算预算。现有的系统通常通过下采样帧或向大上下文语言模型提供密集视觉嵌入来降低成本，但会牺牲时间覆盖范围。这些方法需要权衡时间覆盖范围与成本。
### Innovation
本文提出了语义事件图（SEG），这是一种轻量级的符号接口，用于在视频和语言之间进行交互。SEG将原始帧替换为紧凑的时间交互日志，通过检测和跟踪对象、转换接近模式为人类-对象事件并组织成时间场景图来实现目标。在推理时，查询感知的剪枝模块识别 anchor 实体和词义相关事件，返回的子图被口头化并通过 Gemini 2.5 Flash 生成答案。通过这种方法，SEG 将 300-500 个交互的五个 YouTube 视频和 120 个自动生成的长期问题的准确率提升至 65.0%，仅使用 3.47k 个子单位，几乎与使用完整日志的基线（准确率为 62.5%，使用 40.39k 个子单位）相当，同时减少了 91.4% 的子单位使用。
### Conclusion
本文展示了符号时间图作为一种高效且即插即用的内存层，可以用于现有的视觉-语言模型，既保持了长时间推理的能力，又显著提高了长格式视频问答的子单位使用效率和成本效率。相关代码、日志和事件提取工具将发布以实现可再现性。
## 20. `cs.CL` - 将对齐控制添加到语言模型 [PDF](https://arxiv.org/pdf/2503.04346), [HTML](https://arxiv.org/abs/2503.04346)
### Authors
Wenhong Zhu,Weinan Zhang,Rui Wang
### Background
在提升语言模型（LMs）的实用性方面，后训练对齐已成为关键因素。然而，不同用户对模型对齐的需求不同，造成了对齐强度的效果个性化。
### Innovation
本文提出了一种方法，即将对齐控制纳入单一模型（称为CLM）。该方法在初始层之前增加了一个身份层，并仅对该层进行偏好学习，将未对齐的输入词嵌入映射到对齐空间。实验结果显示，该方法的高效微调性能与全量微调相当。在推理过程中，输入嵌入会通过对齐层和未对齐层处理，然后通过插值系数合并。
### Conclusion
通过控制此参数，对齐表现出明显的插值和外推现象。
## 21. `cs.CL` - AdaSpec: 自适应的推测性解码以实现快速且符合SLO的大语言模型服务 [PDF](https://arxiv.org/pdf/2503.05096), [HTML](https://arxiv.org/abs/2503.05096)
### Authors
Kaiyu Huang,Hao Wu,Zhubo Shi,Han Zou,Minchen Yu,Qingjiang Shi
### Background
基于云的大语言模型（LLM）服务在应对动态请求模式时经常面临低推理延迟和满足服务水平目标（SLOs）的挑战。现有推测性解码方案难以适应波动的工作负载和动态系统环境，导致性能下降和SLO违约。
### Innovation
提出了一种名为AdaSpec的高效大语言模型推理系统，能够根据实时请求负载和系统配置动态调整推测策略。AdaSpec还提出了一种理论模型来分析和预测不同情境下推测策略的效率，并实现了智能的草稿和验证算法以最大化性能并确保高SLO达成。
### Conclusion
实验结果表明，AdaSpec能够一致地满足SLO并实现了显著的性能提升，相比最先进的推测性推理系统，性能提高了66%。源代码已公开并可以访问。
## 22. `cs.CL` - 最合适的指令调优数据是那些符合目标模型的数据 [PDF](https://arxiv.org/pdf/2502.04194), [HTML](https://arxiv.org/abs/2502.04194)
### Authors
Dylan Zhang,Qirun Dai,Hao Peng
### Background
高质量的监督微调（SFT）数据对于从预训练的大语言模型（LLMs）中激发强大的能力至关重要。通常，指令会配对多个响应，这些响应来自其他LLMs，但常常不符合目标模型的数据分布。这在大规模应用中可能导致效益递减甚至损害模型的性能和鲁棒性。
### Innovation
我们提出了GRAPE，一种新的SFT框架，能够考虑目标模型的独特特性。对于每条指令，它会从多种LLMs中收集响应，选择目标模型测度概率最高的响应，因为它与目标模型的预训练分布最接近。这种方法再进行标准的SFT训练。实验表明，相较于强大的基线，GRAPE显著提升了性能，绝对收益最高达13.8%，平均提升15.3%。实验结果也表明，即使在有限的数据和训练周期内，GRAPE也能使模型性能超越使用更多数据和训练周期的其他基线。
### Conclusion
GRAPE在实际应用场景中也表现出色，无论是在Tulu3和Olmo-2的微调数据中，还是在减少数据使用量和训练周期的情况下，GRAPE的表现都优于基线模型，显示出广泛的应用前景和竞争力。
## 23. `cs.CL` - KARMA: 利用多代理大语言模型进行自动知识图谱扩展 [PDF](https://arxiv.org/pdf/2502.06472), [HTML](https://arxiv.org/abs/2502.06472)
### Authors
Yuxing Lu,Wei Wu,Xukai Zhao,Rui Peng,Jinzhuo Wang
### Background
维护全面和最新的知识图谱对于现代AI系统至关重要，但手动标注难以应对科学文献的快速增长。现有的知识图谱维护方法面临难以扩展的问题。
### Innovation
提出了一种新的多代理大语言模型框架KARMA，用于通过结构化分析未结构化文本自动扩展知识图谱。KARMA包含了九个协作代理，涵盖实体发现、关系提取、模式对齐和冲突解决，能够迭代解析文档、验证提取的知识，并将其整合到现有的图结构中，同时遵循特定领域的模式。
### Conclusion
在1,200篇来自三个不同领域的PubMed文章的实验中，KARMA在知识图谱扩展方面表现出色，识别出多达38,230个新实体，LLM验证的正确率达到83.1%，并通过多层次评估减少了18.6%的冲突边。
## 24. `cs.CL` - 选择胜过问题 [PDF](https://arxiv.org/pdf/2502.18798), [HTML](https://arxiv.org/abs/2502.18798)
### Authors
Gyeongje Cho,Yeonkyoung So,Jaejin Lee
### Background
近期的研究结果引发了对大型语言模型通过多项选择题答题（MCQA）评估其理解能力的有效性的担忧。已有研究发现，模型在作答时更受选项影响而非真正理解问题，因此传统的评分方法可能不够可靠。
### Innovation
本文引入了一种新的评分方法，称为基于问题的归一化概率偏移（NPSQ），旨在隔离问题本身的影响，提供更可靠的理解评估。实验证明，传统的基于对数似然或其归一化长度变体的评分方法容易受到答案选项表面特征的影响，而NPSQ方法即使对答案选项进行修改后也保持稳定。
### Conclusion
研究表明，NPSQ评分方法可以更准确地评估大型语言模型的理解能力，不受选项表面特征的影响。
## 25. `cs.CL` - 使用持续预训练高效构建领域特定大型语言模型 [PDF](https://arxiv.org/pdf/2311.08545), [HTML](https://arxiv.org/abs/2311.08545)
### Authors
Yong Xie,Karan Aggarwal,Aitzaz Ahmad
### Background
大规模语言模型（LLMs）在开放域任务上表现出色。通常，针对某一领域的LLMs会完全基于该领域的数据集进行训练，以处理特定领域的任务。本文探索了一种替代策略，即持续预训练，作为一种方法来在现有的开放域LLM基础上开发领域特定的LLMs。
### Innovation
作者引入了基于金融领域持续适应性预训练的FinPythia-6.9B，并且探索了简单的、但有效的数据选择策略。这些策略仅使用数据集的10%，并在成本和数据量上都有显著优势，同时依然保持在开放域基准任务上的性能。
### Conclusion
本文提出了一种经济高效的解决方案，通过持续预训练构建领域特定的LLMs，表明该方法具有成本效益且在特定领域（如金融领域）表现出色。
## 26. `cs.CL` - 将LoRA初始化空间推向极致以保留预训练知识 [PDF](https://arxiv.org/pdf/2503.02659), [HTML](https://arxiv.org/abs/2503.02659)
### Authors
Pengwei Tang,Xiaolin Hu,Yong Liu,Lizhong Ding,Dongjie Zhang,Xing Wu,Debing Zhang
### Background
LoRA是大规模语言模型（LLMs）参数高效微调的主要方法，但目前仍然存在灾难性遗忘的问题。已有研究表明，专门的LoRA初始化可以缓解灾难性遗忘。现有的LoRA初始化方法主要集中在使残差权重接近预训练权重或确保LoRA初始化空间与预训练知识正交，但后者的重要性尚未充分认识到。该研究发现，LoRA初始化空间是保留预训练知识的关键，而不是残差权重。已有方法如MiLoRA提出使LoRA初始化空间与预训练权重正交，但MiLoRA使用了预训练权重的零空间。研究发现，输入激活的有效秩远小于预训练权重，因此激活的零空间比权重的零空间更准确且包含的预训练知识信息较少。
### Innovation
该研究提出了LoRA-Null方法，该方法在输入激活的零空间中初始化LoRA，以有效保存预训练大型语言模型的世界知识，同时也实现了良好的微调性能。相比MiLoRA方法采用预训练权重的零空间，输入激活的零空间考虑了所有前一层参数以及输入数据，从而更加准确。
### Conclusion
实验结果表明，LoRA-Null方法能有效保存预训练知识并实现良好的微调性能，代码可从指定网站获取。
## 27. `cs.CL` - 浏览与集注：通过先验大语言模型内容融合理解多模态内容 [PDF](https://arxiv.org/pdf/2402.12195), [HTML](https://arxiv.org/abs/2402.12195)
### Authors
Ziyue Wang,Chi Chen,Yiqi Zhu,Fuwen Luo,Peng Li,Ming Yan,Ji Zhang,Fei Huang,Maosong Sun,Yang Liu
### Background
随着大型语言模型（LLMs）的发展，结合预训练视觉模型的多模态大型语言模型（MLLMs）在视觉-语言任务中表现出色。然而，它们在理解涉及多张图片的上下文方面仍存在不足。主要原因是每张图片的视觉特征由冻结编码器单独编码，然后输入到LLM主干中，缺乏对其他图片和多模态指令的感知。
### Innovation
本文提出了一种两阶段范式——浏览-集注，以在将特征输入LLM之前先实现深入的多模态上下文融合。该范式首先浏览输入以获取关键见解，然后集注于关键细节，通过这些见解指导理解多模态输入。此外，本文还开发了特定的训练策略来增强对多张图片输入的理解。实验结果表明，该方法在7个多张图片场景中显著提升了表现，相对于3B和11B LLMs的强基线模型，平均准确率分别提高了2.13%和7.60%。
### Conclusion
本文提出了一种新颖的多模态上下文融合范式——浏览-集注，以改进多模态大型语言模型在多张图片场景下的理解和性能。通过实验验证了该方法的有效性，显著提升了模型在多模态任务中的表现。
## 28. `cs.CL` - 通过优化提示的大语言模型对分类命名自动标注方法的评估 [PDF](https://arxiv.org/pdf/2503.10662), [HTML](https://arxiv.org/abs/2503.10662)
### Authors
Keito Inoshita,Kota Nojiri,Haruto Sugeno,Takumi Taga
### Background
科学名称由属名和种 epithet 组成，其中种 epithet 经常反映形态、生态、分布和文化背景等方面。传统上，研究人员通过仔细检查分类描述来手动标记种名，这就需要大量时间和精力处理大量数据集。本研究评估了利用大型语言模型（LLM）的文本分类和语义提取能力，自动标记种名的可能性。
### Innovation
使用 Mammola 等人编写的蜘蛛名称数据集，该研究通过提示工程优化了基于 LLM 的标记结果，并将其与人类注释进行了比较。结果显示，基于 LLM 的分类在形态学、地理学和人群类别的准确性很高，但在生态与行为、现代与过去文化等类别中的准确性较低，显示了解读动物行为和文化背景的挑战。未来的研究将专注于通过优化少量标注学习和检索增强生成技术来提高准确性，并扩大 LLM 基本月标记的应用范围，涵盖多种生物种。
### Conclusion
通过优化提示的大语言模型能够实现对分类命名的自动标注，并在一些类别中达到了较高的准确性，但在动物行为和文化背景的解读方面仍存在挑战。未来需要进一步优化模型以提高准确性和应用范围。
## 29. `cs.CL` - 使用大规模语言模型在社交媒体上矫正错误信息 [PDF](https://arxiv.org/pdf/2403.11169), [HTML](https://arxiv.org/abs/2403.11169)
### Authors
Xinyi Zhou,Ashish Sharma,Amy X. Zhang,Tim Althoff
### Background
现实世界的信息通常是多模态的，但可能因事实错误、过时的声明、缺失的上下文、误解等原因而误导或具有潜在误导性。这类“错误信息”尚未被充分研究，难以解决且严重损害了许多社会领域，特别是在社交媒体上，它能够迅速传播。尽管手动纠正错误信息能够识别并解释其准确性和不准确之处，但这种方法难以扩大规模。尽管大规模语言模型可以生成人类类似的语言，以加速错误信息的纠正，但在处理过时信息、幻觉以及有限的多模态能力方面存在困难。
### Innovation
提出的MUSE是一种大规模语言模型，结合了视觉语言建模和网络检索功能，可以从相关且可信的来源中获取信息，生成判断哪些部分或哪些建议内容可能是错误信息或潜在误导性，并且给出基于事实的解释。进一步定义了一套全面的评估标准，涵盖了准确性、解释的可信度、相关性等层面。研究表明，MUSE在处理不同社交媒体内容方面表现优秀，包括之前未经过网络验证的内容。MUSE的表现优于GPT-4，比高质量的社交媒体用户回复也要出色，提升了37%和29%。
### Conclusion
这项工作提供了一个大规模纠正错误信息的通用方法论和评估框架。
## 30. `cs.LG` - 有限时间分析的同时双Q学习 [PDF](https://arxiv.org/pdf/2406.09946), [HTML](https://arxiv.org/abs/2406.09946)
### Authors
Hyunjun Na,Donghwan Lee
### Background
Q-学习是强化学习中最基本的算法之一，尽管它在各种应用中取得了广泛的成功，但在Q-学习更新过程中容易出现过度估计偏差。双Q学习通过使用两个独立的Q估计器并且在学习过程中随机选择和更新来应对这一问题。
### Innovation
本文提出了一种改进的双Q学习，命名为同时双Q学习（SDQ），并对其进行了有限时间分析。SDQ消除了两个Q估计器之间的随机选择的需要，并通过一个新的切换系统框架来促进高效的有限时间分析。
### Conclusion
实验研究表明，SDQ比双Q学习收敛速度更快，同时仍然能够减轻最大化偏差。我们还为SDQ推导出了有限时间的期望误差界。
## 31. `cs.LG` - Canopy: 属性驱动的学习在拥塞控制中的应用 [PDF](https://arxiv.org/pdf/2412.10915), [HTML](https://arxiv.org/abs/2412.10915)
### Authors
Chenxi Yang,Divyanshu Saxena,Rohit Dwivedula,Kshiteej Mahajan,Swarat Chaudhuri,Aditya Akella
### Background
基于学习的拥塞控制器相比传统启发式方法具有更好的适应性。然而，学习技术的不可靠性可能会导致基于学习的控制器表现不佳，因此需要提供形式上的保证。虽然现有方法可以形式化验证学习到的拥塞控制器，但这些方法只能提供二进制反馈，不能优化控制器以获得更好的行为。
### Innovation
Canopy 提出了一种新的属性驱动框架，将学习与正式推理集成到了学习循环中。Canopy 利用了新颖的定量认证和抽象解释器来指导训练过程，奖励模型并在最坏情况下评估模型的安全性和鲁棒性性能。与现有的最先进的学习控制器不同，Canopy 训练的控制器能够在各种网络条件下提供适应性和最坏情况下的可靠性。
### Conclusion
我们的评估表明，Canopy 训练的控制器不仅提供了适应性，还在各种网络条件下提供了最坏情况下的可靠性。
## 32. `cs.LG` - CFT-RAG：基于Cuckoo Filter的实体树检索增强生成算法 [PDF](https://arxiv.org/pdf/2501.15098), [HTML](https://arxiv.org/abs/2501.15098)
### Authors
Zihang Li,Yangdong Ruan,Wenjun Liu,Zhengyang Wang,Tong Yang
### Background
尽管检索增强生成(RAG)通过检索外部知识库并整合生成内容显著提高了生成质量，但在涉及层级结构的Tree-RAG知识检索任务中，面临着计算效率瓶颈。
### Innovation
提出了一种基于改进的Cuckoo Filter的Tree-RAG加速方法，在检索过程中优化实体定位，从而实现显著的性能提升。该方法通过引入层级树结构有效组织实体，并利用Cuckoo Filter作为高效数据结构，支持快速成员查询和动态更新。
### Conclusion
实验结果显示，本方法在保持较高生成质量的前提下，相比原始的Tree-RAG更快得多，在树的数目较大时，速度提高了数倍。本研究工作可在以下链接获取: this https URL
## 33. `cs.LG` - 批量化$Q^*$学习中的数据驱动知识转移 [PDF](https://arxiv.org/pdf/2404.15209), [HTML](https://arxiv.org/abs/2404.15209)
### Authors
Elynn Chen,Xi Chen,Wenbo Jing
### Background
在基于数据的营销、医疗和教育决策中，利用现有企业的大量数据导航高维特征空间和处理新企业中的数据稀缺问题变得尤为重要。本文通过集中精力研究批量稳态环境，利用马尔可夫决策过程（MDPs）框架正式定义任务差异，探讨在动态决策中的知识转移。
### Innovation
提出了Transferred Fitted $Q$-Iteration算法框架，该算法利用广义函数逼近，直接利用目标数据和源数据估算最优行为-状态函数$Q^*$。通过筛近似方法建立了统计性能与MDPs任务差异之间的关系，分析了源和目标样本大小及任务差异对知识转移有效性的影响。
### Conclusion
理论和实验结果表明，最终的$Q^*$函数的学习误差显著改善，证明了知识转移的有效性。
## 34. `cs.LG` - 统一理解与评估引导方法 [PDF](https://arxiv.org/pdf/2502.02716), [HTML](https://arxiv.org/abs/2502.02716)
### Authors
Shawn Im,Sharon Li
### Background
引导方法通过施加引导向量控制大语言模型，使输出朝着预期行为发展，同时避免重新训练。尽管这些方法的重要性日益增长，但领域内缺乏统一的理解和对不同任务和数据集的持续评估，这阻碍了进步。
### Innovation
该论文提出了一种统一框架来分析和评估引导方法，建立了其核心原则并提供了其效果的理论见解。通过在多项选择和开放式文本生成任务中的全面经验评估，验证了这些见解，确定了影响性能的关键因素，并展示了某些方法的优势。这项工作在理论和实践视角之间建立了桥梁，为推进引导方法的设计、优化和在大语言模型中的部署提供了可操作的指导。
### Conclusion
论文证明了引导方法的有效性，并提供了具体指导，有助于提升大语言模型中引导技术的设计、优化和部署。
## 35. `cs.LG` - FlowRL: 支持半结构化传感器数据的流动增强少样本强化学习 [PDF](https://arxiv.org/pdf/2409.14178), [HTML](https://arxiv.org/abs/2409.14178)
### Authors
Mohammad Pivezhandi,Abusayeed Saifullah
### Background
在传感器数据有限的情况下，强化学习（RL）在少样本场景中的应用具有挑战性，特别是在如动态电压和频率调优（DVFS）等应用中，传感器读数半结构化且具有内在相关性。现有的RL方法由于缺乏训练样本而难以有效训练。
### Innovation
提出了一种新颖的方法——流动增强强化学习（FlowRL），利用连续规范化流动生成高质量的合成数据，以提高少样本RL中的样本效率和策略鲁棒性。FlowRL 通过引入潜在空间自举来增强多样性，并通过特征加权流动匹配来保持关键数据相关性。
### Conclusion
FlowRL 在使用 NVIDIA Jetson TX2 的 DVFS 案例研究中，与基线相比，实现了高达 35% 的更高帧率和更快的 Q 值收敛，证明了在资源受限环境中其有效性。此外，FlowRL 还适用于其他半结构化领域，如机器人技术和智能电网，为数据稀缺的RL环境提供了可扩展的解决方案。
## 36. `cs.LG` - 信息匹配方法在最优实验设计和主动学习中的应用 [PDF](https://arxiv.org/pdf/2411.02740), [HTML](https://arxiv.org/abs/2411.02740)
### Authors
Yonatan Kurniawan(1),Tracianne B. Neilsen(1),Benjamin L. Francis(2),Alex M. Stankovic(3),Mingjian Wen(4),Ilia Nikiforov(5),Ellad B. Tadmor(5),Vasily V. Bulatov(6),Vincenzo Lordi(6),Mark K. Transtrum(1, 2, and 3) ((1) Brigham Young University, Provo, UT, USA, (2) Achilles Heel Technologies, Orem, UT, USA, (3) SLAC National Accelerator Laboratory, Menlo Park, CA, USA, (4) University of Electronic Science and Technology of China, Chengdu, China, (5) University of Minnesota, Minneapolis, MN, USA, (6) Lawrence Livermore National Laboratory)
### Background
数学模型的效果高度依赖于训练数据的质量，但收集足够的数据往往成本高且具有挑战性。许多建模应用需要通过推断参数来预测感兴趣的量（QoI）。由于模型中通常包含许多不可识别（灵活）的参数，QoI 常常取决于一小部分参数组合。因此，介绍了一种基于 Fishcer 信息矩阵的信息匹配标准，从候选数据池中选择最具有信息性的训练数据。
### Innovation
提出了一种基于 Fisher 信息矩阵的信息匹配准则，用于从候选数据池中选择最具有信息性的训练数据，确保选择的数据包含足够多的信息来学习需要约束下游 QoI 的参数。这种方法作为一种凸优化问题进行公式化，使其可以扩展到大型模型和数据集中。
### Conclusion
该方法在包括电力系统和水下声学等多个科学领域的建模问题中得到了证明，表明相对少量的最优训练数据可以提供精确预测所需的信息。这种方法在材料科学等应用中的主动学习环路中的应用展现了积极的结果，特别是在大型机器学习模型中的主动学习方面。
## 37. `cs.LG` - 当前正确之后错误：在偏好漂移下的非平稳直接偏好优化 [PDF](https://arxiv.org/pdf/2407.18676), [HTML](https://arxiv.org/abs/2407.18676)
### Authors
Seongho Son,William Bankes,Sayak Ray Chowdhury,Brooks Paige,Ilija Bogunovic
### Background
当前大语言模型（LLM）的偏好优化算法未考虑时间依赖的偏好漂移问题，这可能导致严重的对齐偏差。
### Innovation
提出了一种名为非平稳直接偏好优化（NS-DPO）的新方法，该方法通过引入动态Bradley-Terry模型来建模随时间变化的奖励函数。NS-DPO通过引入单一折扣参数在损失函数中，实现了指数加权并专注于更相关的数据点，从而提供了一种计算高效的解决方案。
### Conclusion
理论上分析了NS-DPO在偏好漂移的情况下的一般收敛性，并通过使用流行的LLM奖励模型和数据集展示了NS-DPO在具有漂移偏好的情况下对模型微调的效果，表明NS-DPO在非平稳情况下能保持鲁棒性，并且在没有忽略时间偏好变化的情况下显著优于基准算法。
## 38. `cs.LG` - skwdro：一个 Wasserstein 分布鲁棒机器学习库 [PDF](https://arxiv.org/pdf/2410.21231), [HTML](https://arxiv.org/abs/2410.21231)
### Authors
Florian Vincent,Waïss Azizian,Franck Iutzeler,Jérôme Malick
### Background
该论文背景在于使用 Wasserstein 距离进行分布鲁棒优化在最优运输和机器学习领域已得到广泛研究与应用。然而，对于普通用户来说，如何将这种方法应用到实际的机器学习模型训练中仍然有一定的难度。
### Innovation
论文的主要创新在于提出了一个名为 skwdro 的 Python 库，它基于 Wasserstein 距离实现分布鲁棒优化。该库提供了一个 PyTorch 模块的包装器，能够通过 minimal code changes 实现模型损失的鲁棒性优化，同时提供了一些 scikit-learn 兼容的估计器以支持多种优化目标。核心实现通过引入对原始鲁棒目标的对数光滑处理来保证最大程度的模型灵活性。
### Conclusion
该库现可以在该项目页面this https URL获取，并且相关文档在this https URL可以获得。这使得广大用户能更轻松地训练出鲁棒的机器学习模型。
## 39. `cs.LG` - EMP: 在数据修剪中增强记忆 [PDF](https://arxiv.org/pdf/2408.16031), [HTML](https://arxiv.org/abs/2408.16031)
### Authors
Jinying Xiao,Ping Li,Jie Nie,Bin Ji,Shasha Li,Xiaodong Liu,Jun Ma,Qingbo Wu,Jie Yu
### Background
近年来，大规模的语言和视觉模型显示出很强的表现能力，但由于预训练和微调成本高昂，研究方向转向了通过数据修剪加快训练速度。以往方法使用样本损失作为评估标准，目标是选择最难训练的样本进行训练。然而当剪裁率提高时，每个样本被训练的次数变得更加均衡，这导致许多关键或通用样本未能得到有效拟合，这被称为低频学习（Low-Frequency Learning，LFL）。LFL妨碍了模型记住大部分样本。
### Innovation
该工作分解了LFL的功能分数，提供了LFL效率低下的理论解释，并提出在功能分数中添加记忆项以增强模型的记忆能力，并给出了记忆项的近似值。同样地，还探讨了自我监督学习（SSL）中的记忆问题，标记了这是首次讨论SSL中的记忆。利用对比学习，对记忆项进行了理论和实验推导。最后提出了增强记忆力修剪（EMP），该方法通过增强数据的记忆能力解决高剪裁率下记忆不足的问题，从而提高性能。EMP在图像分类、自然语言理解和模型预训练等任务中进行了评估，结果显示在极端剪裁率下，EMP能够提高模型性能，例如，在CIFAR100-ResNet50预训练任务中，在70%的剪裁率下，EMP优于当前方法2.2%。
### Conclusion
在“极端剪裁率”下，增强记忆力修剪（EMP）能够通过改善模型对数据的记忆能力来提高模型性能。例如，在CIFAR100-ResNet50预训练任务中，使用70%的剪裁率，EMP比当前方法性能提高2.2%。
