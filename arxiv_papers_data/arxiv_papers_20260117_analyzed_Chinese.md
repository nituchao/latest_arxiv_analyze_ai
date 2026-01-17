# 20260117
[![Subscribe_Visitors](https://visitor-badge.laobi.icu/badge?page_id=nituchao.latest_arxiv_analyze_ai_rss)](https://github.com/nituchao/latest_arxiv_analyze_ai)

## 1. `cs.AI` - 通过注意力感知干预提高逻辑推理的链式思维 [PDF](https://arxiv.org/pdf/2601.09805), [HTML](https://arxiv.org/abs/2601.09805)
### Authors
Nguyen Minh Phuong,Dang Huu Tien,Naoya Inoue
### Background
现代逻辑推理主要依赖复杂的交互框架，通过将推理过程分解为子任务，并通过精心设计的提示或依赖外部资源（如符号求解器）来解决这些子任务。交互式方法增加了额外的开销，而混合方法则依赖于外部组件，这限制了它们的可扩展性。一种非交互式、端到端的推理框架可以在模型本身中促进推理，从而提高泛化能力，同时保持分析性，不需要任何外部资源。
### Innovation
该工作引入了一种非交互式、端到端的推理框架。通过在少量样本提示中引入结构信息，激活与逻辑推理操作模式相符的注意力头。在此基础上，提出了注意力感知干预（AAI），一种推理时干预方法，通过在选定的具有逻辑模式的头中重加权注意力分数来引导模型的推理，使其更有效地利用先验知识进行自我调节。
### Conclusion
广泛的实验表明，注意力感知干预（AAI）在多种基准测试和模型架构上提高了逻辑推理性能，同时几乎不受额外计算开销的影响。代码已在以下链接处提供：[此链接](https://example.com/code)。
## 2. `cs.AI` - 在人机交互中，认识论为互补性提供了未来 [PDF](https://arxiv.org/pdf/2601.09871), [HTML](https://arxiv.org/abs/2601.09871)
### Authors
Andrea Ferrario,Alessandro Facchini,Juan M. Durán
### Background
人类与AI的互补性是指人类在AI系统的支持下在决策过程中的表现可能优于单独工作。自引入人机交互文献以来，它通过推广依赖范式并提供一种更实用的替代‘信任AI’的概念而获得了认同。然而，互补性面临着一些关键的理论挑战，包括缺乏精确的理论支撑，仅作为事后指标来衡量相对预测准确性，以及未能解决其他人类与AI互动所需的条件。因此，互补性在实证研究中难以实现。
### Innovation
本文通过利用认识论（epistemology）来应对这些挑战，重新将互补性纳入可信性AI的讨论之中。基于计算可靠主义（computational reliabilism），作者认为历史上互补性的实例作为证据，证明了特定的个体与AI之间互动的可靠的认知过程。通过与其他可靠性指标（如人类与AI团队与认知标准和社会技术实践的对齐）结合使用，互补性有助于增强以生成预测的人类与AI团队的可靠性。这会支持那些受到这些输出影响的人的决策推理，如患者、管理者和监管者等。
### Conclusion
综上所述，本文的新颖之处在于，补充性的作用和价值不在于提供预测准确性的相对衡量标准，而在于帮助校准基于AI支持的过程可靠性进行决策，这些过程正在越来越多地塑造日常生活。
## 3. `cs.AI` - AI生存故事：对AI永续风险的一种分类分析 [PDF](https://arxiv.org/pdf/2601.09765), [HTML](https://arxiv.org/abs/2601.09765)
### Authors
Herman Cappelen,Simon Goldstein,John Hawthorne
### Background
近年来，随着ChatGPT等AI系统的发布，关于AI系统是否可能对人类构成生存风险的讨论变得频繁。文章发展了一个通用框架来分析AI系统的生存性风险。
### Innovation
文章提出了一个两前提论证框架，探讨AI系统带来的生存风险。通过构建不同的生存故事分类来分析两种前提中的每一种失效的可能性，从而推测人类被AI系统摧毁的概率。
### Conclusion
不同的生存故事揭示了不同的挑战，并引发了对AI威胁的不同响应。此外，通过分类分析，文章产生了关于P(doom)（人类被AI摧毁的概率）的大致估计。
## 4. `cs.AI` - 关于大型语言模型基于对话代理的人类拟人化现象的伦理视角综述 [PDF](https://arxiv.org/pdf/2601.09869), [HTML](https://arxiv.org/abs/2601.09869)
### Authors
Andrea Ferrario,Rasita Vinay,Matteo Casserini,Alessandro Facchini
### Background
随着基于大型语言模型（LLM）的对话代理（CAs）的兴起，人类拟人化——即赋予非人类实体人类品质的现象——变得越来越显著。与早期的聊天机器人相比，基于LLM的对话代理会常规地生成互动和语言提示，这些提示包括第一人称自我参照、关于知识和情感的表达，这些都已被实证研究证明能够增加用户的参与度。然而，人类拟人化也引发了诸如欺骗、过分依赖和剥削性关系界定等伦理问题。一些作者认为，人类拟人化的互动可能支持自主性、福祉和包容性。但现有的文献在对人类拟人化的定义、操作化和规范性评估方面仍然碎片化且存在显著差异。因此，需要对相关工作进行全面的综述。
### Innovation
本文开展了一项范围广泛的综述，涵盖了五个数据库和三个预印本存储库中有关基于LLM的对话代理人类拟人化的伦理视角的相关工作。研究综合总结了概念基础、伦理挑战与机遇以及方法论方法。通过这项综述，作者发现，尽管在属性基定义上存在共识，但在操作化方面存在显著分歧，并且大多数视角呈风险导向，缺乏将观察到的交互影响与可操作的治理指南进行联系的实证研究。这些综述结果为未来研究和伦理部署人类拟人化提示提供了参考。
### Conclusion
本文提出了一个研究议程和设计/治理建议，以指导伦理地使用人类拟人化提示在基于LLM的对话代理中的应用。
## 5. `cs.AI` - PCN-Rec: 自主证明携带谈判以实现可靠的任务治理限制推荐 [PDF](https://arxiv.org/pdf/2601.09771), [HTML](https://arxiv.org/abs/2601.09771)
### Authors
Aradhya Dixit,Shreem Dixit
### Background
现代基于大规模语言模型的推荐系统能够生成引人注目的推荐列表，但在可靠满足治理约束方面（如最小长尾曝光或多样性要求）存在困难。本研究通过提出PCN-Rec（一种证明携带谈判管道），阐述了解决上述问题的方法。
### Innovation
PCN-Rec 模型通过分离自然语言推理和确定性执行，将基础推荐器（如 MF/CF）生成的候选列表放入由用户倡导者（优化相关性）和政策代理（执行约束）进行谈判的过程。推荐结果通过一个中间 HPC（合谈判）大语言模型合成一个最佳顶级列表，并附带一个结构化证书，描述了所声称的约束满足情况。随后，使用确定性验证器从列表中重新计算所有约束并仅接受验证过的证书；若验证未通过，则使用确定性的约束条件下的贪婪修复方法生成符合用户需求的合规列表，从而提供可审计的痕迹。
### Conclusion
在 MovieLens-100K 数据集上进行的实验表明，PCN-Rec 在具备治理约束的用户（n = 551，候选窗口大小 W = 80）中实现了 98.55% 的通过率，相比一次性的缺乏验证和修复的单个 HPC 基准模型，对用户 Utility 的绝对下降仅为 0.021（NDCG@10 从 0.424 下降到 0.403），差异具有统计学意义 (p < 0.05)。此结果表明，PCN-Rec 在不显著牺牲用户体验的前提下，实现了高效可靠的治理约束推荐。
## 6. `cs.AI` - 超越基于规则的工作流：CORAL通过Agent-to-Agent通信的信息流协调多智能体范式 [PDF](https://arxiv.org/pdf/2601.09883), [HTML](https://arxiv.org/abs/2601.09883)
### Authors
Xinxing Ren,Quagmire Zang,Caelum Forder,Suman Deb,Ahsen Tahir,Roman J. Georgio,Peter Carroll,Zekun Guo
### Background
现有的大多数基于Large Language Model (LLM)的多智能体系统(MAS)依赖于预定义的工作流，其中人类工程师需要提前枚举任务状态，并相应地规定路由规则和上下文注入。这些基于工作流的设计本质上是基于规则的决策树，存在两大基本限制：需要大量手动努力来预测和编码可能的任务状态，并且不能彻底涵盖复杂现实任务的状态空间。
### Innovation
提出了一种基于CORAL的Agent-to-Agent (A2A)通信的信息流协调多智能体范式，即信息-流协调多智能体范式。”通过一个专门的信息流协调仲裁者，持续监控任务进度，并通过A2A工具包与其它智能体动态协调，无需依赖预定义的工作流。该方法在通用基准GAIA上进行评估，使用代表性的基于工作流的MAS（OWL）作为基线，同时控制智能体角色和基础模型。在pass@1设置下，该方法实现了63.64%的准确率，比OWL的55.15%高出8.49个百分点，且与OWL相比，在词汇消耗量相当的情况下性能更优。
### Conclusion
该范例使任务监控更具灵活性，并能够更好地处理边缘情况。实施代码已公开发布。
## 7. `cs.AI` - 大型语言模型用户中的反社会行为：实验证据 [PDF](https://arxiv.org/pdf/2601.09772), [HTML](https://arxiv.org/abs/2601.09772)
### Authors
Paweł Niszczota,Cassandra Grützner
### Background
大型语言模型（LLMs）的迅速普及引发了对其引起的社会反应的担忧。先前的研究记录了对AI用户持有负面态度的情况，但尚不清楚这种不满是否转化为实际行动。本文通过一项两阶段的在线实验来探讨这一问题。
### Innovation
通过一项两阶段的在线实验，研究受试者能否花费自己的部分财富减少使用过实证任务辅助的LLM或未使用LLM的同伴的收益。实验的结果显示，平均情况下，受试者抵消了完全依赖模型的人36%的收益，随着实际使用LLM的程度增加，惩罚也不断增加。披露LLM使用情况出现了信任缺口：声称未使用LLM的人受到比实际未使用更严厉的惩罚，表明“未使用”声明受到怀疑；而高程度使用时，实际依赖模型比自我报告依赖模型的人受到更严厉的惩罚。
### Conclusion
这些发现提供了首次行为证据，即LLM的效率收益可能伴随着社会制裁的成本。
## 8. `cs.AI` - 思考久远，但行动快捷：大型推理模型的稳定序列测试时间放大 [PDF](https://arxiv.org/pdf/2601.09855), [HTML](https://arxiv.org/abs/2601.09855)
### Authors
Michael R. Metel,Yufei Cui,Boxing Chen,Prasanna Parthasarathi
### Background
序列测试时间放大是一种无需训练即可提高大型推理模型准确性的有前景方法，但现有的实施方式显示出显著的局限性。延长模型的推理长度可以提高准确率，但进一步延长推理长度会导致准确率下降和模型不稳定。
### Innovation
本文提出了一种名为Min-Seek的新型序列测试时间放大方法，能够在广泛的诱导思考范围内显著提高模型准确性，稳定顺序放大准确率，消除推理长度调优的需求。该方法在推理过程中仅保留一个额外诱导思考的KV对，在具有定制的不存储位置嵌入的KV缓存中，通过在每次新生成的思考前动态连续编码它们，该方法可以合理地推理超出模型的最大上下文长度，并在较轻微的条件下具有线性计算复杂度。
### Conclusion
除了在各种推理任务上改善模型准确性外，该方法还具有内在的高效性，因仅在推理期间保留了一个额外诱导思考的KV对。通过这种定制的KV缓存，该方法可以使模型继续推理超出其最大上下文长度，并在较轻微的条件下具有线性计算复杂度。
## 9. `cs.AI` - 长视角LLM代理中的连续记忆架构 [PDF](https://arxiv.org/pdf/2601.09913), [HTML](https://arxiv.org/abs/2601.09913)
### Authors
Joe Logan
### Background
检索增强生成（RAG）已成为向大规模语言模型（LLM）代理提供上下文知识的默认策略。然而，RAG 将记忆视为无状态查找表：信息无限期持续，检索为只读，缺乏时间连续性。
### Innovation
定义了连续记忆架构（CMA），这是一种维护和更新交互之间内部状态的系统类别，通过持久存储、选择性保留、关联路由、时间链接和升维抽象化。CMA 强调了在任务中观察到的 RAG 的结构上无法积累、突变或消歧义记忆的一致行为优势。
### Conclusion
实验测试表明，CMA 是长视野代理必不可少的架构原语，同时指出了延迟、漂移和可解释性方面的开放挑战。
## 10. `cs.AI` - GUI-Eyes：GUI代理中的工具增强感知 [PDF](https://arxiv.org/pdf/2601.09770), [HTML](https://arxiv.org/abs/2601.09770)
### Authors
Chen Chen,Jiawei Shao,Dakuan Lu,Haoyi Hu,Xiangcheng Liu,Hantao Yao,Wu Liu
### Background
近年来，视觉语言模型（VLMs）和强化学习（RL）的发展促进了GUI自动化领域的进步。然而，现有的大多数方法依赖于静态的、一次性视觉输入以及被动感知，无法适应性地决定何时、是否以及如何观察界面。
### Innovation
本文提出了GUI-Eyes，一种用于GUI任务中的主动视觉感知的强化学习框架。该框架通过分阶段的推理过程和细粒度的策略来调控视觉工具的调用（例如裁剪或放大），进而获得更有信息量的观察。同时，引入了一种连续的空间奖励函数，以工具使用特征为中心，结合位置接近度和区域重叠度，从而提供密集监督并缓解GUI环境中常见的奖励稀疏问题。
### Conclusion
在ScreenSpot-Pro基准测试上，仅使用3000个标记样本，GUI-Eyes-3B实现了44.8%的定位准确率，显著优于监督学习和基于强化学习的基线方法。这些结果表明，分阶段策略推理和细粒度奖励反馈支持的工具感知是构建健壮且数据效率高的GUI代理的关键。
## 11. `cs.CL` - A.X K1 技术报告 [PDF](https://arxiv.org/pdf/2601.09200), [HTML](https://arxiv.org/abs/2601.09200)
### Authors
Sung Jun Cheon,Jaekyung Cho,Seongho Choi,Hyunjun Eun,Seokhwan Jo,Jaehyun Jun,Minsoo Kang,Jin Kim,Jiwon Kim,Minsang Kim,Sungwan Kim,Seungsik Kim,Tae Yoon Kim,Youngrang Kim,Hyeongmun Lee,Sangyeol Lee,Sungeun Lee,Youngsoon Lee,Yujin Lee,Seongmin Ok,Chanyong Park,Hyewoong Park,Junyoung Park,Hyunho Yang,Subin Yi,Soohyun Bae,Dhammiko Arya,Yongseok Choi,Sangho Choi,Dongyeon Cho,Seungmo Cho,Gyoungeun Han,Yong-jin Han,Seokyoung Hong,Hyeon Hwang,Wonbeom Jang,Minjeong Ju,Wonjin Jung,Keummin Ka,Sungil Kang,Dongnam Kim,Joonghoon Kim,Jonghwi Kim,SaeRom Kim,Sangjin Kim,Seongwon Kim,Youngjin Kim,Seojin Lee,Sunwoo Lee,Taehoon Lee,Chanwoo Park,Sohee Park,Sooyeon Park,Yohan Ra,Sereimony Sek,Seungyeon Seo,Gun Song,Sanghoon Woo,Janghan Yoon,Sungbin Yoon
### Background
本文介绍了一个从头开始训练的519B参数的Mixture-of-Experts (MoE)语言模型A.X K1。该模型的训练配置和词汇量大小通过利用缩放定律，在固定计算预算下进行了优化。A.X K1经过一个包含多阶段数据处理流程的10T标记规模的语料库预训练，旨在平衡推理能力和推理效率，支持用户可控的推理过程，以便在不同实际场景中实现可扩展部署。
### Innovation
本文提出了一个简单有效的Think-Fusion训练方案，允许单一模型内部用户控制切换思考和非思考模式。A.X K1在多个基准测试中的表现与领先开源模型相当，并且在韩语文本上的突出优势。
### Conclusion
A.X K1通过在固定计算预算下优化训练配置和词汇量大小，结合高效的Think-Fusion训练方案，在平衡推理能力和效率的同时，展现出与领先开源模型相当的性能，并且在韩语文本上有独特的优势。
## 12. `cs.CL` - Lil: 长解码阶段应用后训练稀疏注意算法时信息损失大于信息增益 [PDF](https://arxiv.org/pdf/2601.03043), [HTML](https://arxiv.org/abs/2601.03043)
### Authors
Junhao Hu,Fangze Li,Mingtao Xu,Feifan Meng,Shiju Zhao,Tiancheng Hu,Ting Peng,Anmin Liu,Wenrui Huang,Chenxu Liu,Ziyue Hua,Tao Xie
### Background
大型语言模型（LLMs）在各种复杂的任务中表现出强大的能力，并且越来越被大规模部署，这对推理效率提出了极大的需求。现有研究通常将推理过程分解为预填充和解码阶段，而解码阶段占总延迟的比例最大。为了减少解码阶段的时间和内存复杂度，有一项研究引入了稀疏注意算法。尽管这些算法在理论上能够减少计算复杂度，但本文通过实验证明，稀疏注意可能会增加端到端的复杂度：信息损失往往导致显著更长的序列长度，我们称之为“Less is Less”（Lil）问题。
### Innovation
本文提出了一个早期停止算法，该算法在稀疏解码过程中检测信息损失超过信息增益的阈值，从而缓解Lil问题。通过实验，该算法能够将token消费降低高达90%，同时仅带来小于2%的准确性下降。
### Conclusion
通过实验证明，稀疏注意算法虽然在理论上降低计算复杂性，但可能由于信息损失导致序列长度增加，引发Lil问题。提出的早期停止算法能够有效缓解这一问题，显著减少token消耗并保持较高的准确性。
## 13. `cs.CL` - 足够的多少个人类评估？人类偏好评估的可行性限制 [PDF](https://arxiv.org/pdf/2601.09084), [HTML](https://arxiv.org/abs/2601.09084)
### Authors
Wilson Y. Lee
### Background
人类偏好评估被广泛用于比较生成模型，但不清楚需要多少评价来可靠地检测小改进。当偏好信号在提示中是弥散的（即所有提示类型都具有同样信息量），等比例分配是最佳策略：没有分配策略能显著提高检测能力。大规模人类偏好数据集的实证分析显示，大多数比较都处于弥散的阶段，表现出小的偏好差距，需要比通常收集的更多的评价，即使是在充分采样的比较中也是如此。这些限制在不同的评估协议和模态中都存在，包括聊天、图像生成和带有执行反馈的代码生成。相比之下，精心策划的基准通过减少因提示引起的变异，系统地引起更大的差距，从而通过减少提示级变异的1.5倍增强检测能力。
### Innovation
研究发现，弥散的偏好信号导致了当前评估方法的有效性的界限。尤其是，当提示类型的偏好信号弥散时，无论采用何种分配策略，都不能显著提高检测能力。此外，通过减少提示引起的变异，精心策划的基准能系统性地增加检测能力。这表明，目前的人类评估结果可能是由于评估能力不足导致的，而并非模型等效。
### Conclusion
我们的结果表明，不明确或否定的人类评估结果通常反映了评估能力不足，而非模型等效。这强调了需要明确考虑效应大小、预算和协议设计的必要性。
## 14. `cs.CL` - 跨国差异：理解跨语言推理-答案不一致 [PDF](https://arxiv.org/pdf/2512.22712), [HTML](https://arxiv.org/abs/2512.22712)
### Authors
Anaelia Ovalle,Candace Ross,Sebastian Ruder,Adina Williams,Karen Ullrich,Mark Ibrahim,Levent Sagun
### Background
大型语言模型展示了通过链式思考提示的强大推理能力，但这种推理质量是否能够在不同语言中转移还尚未得到充分探索。本研究通过构建一个人工验证框架，对来自6种语言、6个前沿模型的65,000条推理痕迹进行分析，揭示了一个关键盲点：尽管模型在任务上的准确率很高，但其推理往往无法支持其结论。非拉丁字母语言中的推理与结论之间的不一致性至少是拉丁字母语言的两倍。
### Innovation
本研究开发了一个基于人工注释的错误分类框架，来表征这些推理错误的主要原因，发现主要来自证据错误（未支持的主张、模糊的事实）然后是不合逻辑的推理步骤。这项研究证实了当前多语言评估方法存在缺陷，需要推理意识更强的评估框架。
### Conclusion
当前的多语言评估实践未能完全反映模型的推理能力，指出需要推理意识更强的评估框架来填补这一空白。
## 15. `cs.CL` - Speech-LLM与端到端架构在多语言对话ASR中的差距桥梁：基于对比探索 [PDF](https://arxiv.org/pdf/2601.01461), [HTML](https://arxiv.org/abs/2601.01461)
### Authors
Yuxiang Mei,Dongxing Xu,Jiaen Liang,Yanhua Long
### Background
该研究背景是在INTERSPEECH 2025的MLC-SLM挑战赛中促进多语言对话ASR的发展。研究回顾了先前的SHNU-mASR系统，该系统使用了具备竞争力的并行语音编码器结构，结合了Whisper和mHuBERT，并配以LLM，但存在特征简单堆叠不能充分利用互补信息和LLM基于的ASR与端到端（E2E）编码解码ASR之间性能差距未能解决的问题。
### Innovation
该研究的创新之处在于提出了一种增强的基于LLM的ASR框架，该框架结合了微调的Whisper和mHuBERT编码器与LLM，以丰富语音表示。首先，研究对带有LoRA和全微调的E2E Whisper模型在MLC-SLM ASR任务上进行了评估，然后提出了基于交叉注意力机制的并行语音编码器融合机制。研究结果表明，在官方评估集上，系统达到了CER/WER为10.69%，与最佳的Track 1系统并驾齐驱，尽管其基础训练数据量仅为1500小时。
### Conclusion
尽管在该研究中微调的LLM-AER性能未达到最佳的E2E Whisper微调模型的水平，但此成果为未来的Speech-LLM设计提供了宝贵的经验指导。代码已公开发布。
## 16. `cs.CL` - Disco-RAG：具有 discourse 意识的检索增强生成 [PDF](https://arxiv.org/pdf/2601.04377), [HTML](https://arxiv.org/abs/2601.04377)
### Authors
Dongqi Liu,Hang Ding,Qiming Feng,Jian Li,Xurong Xie,Zhucun Xue,Chengjie Wang,Jiangning Zhang,Yabiao Wang
### Background
检索增强生成（RAG）已经成为增强大型语言模型（LLMs）在知识密集型任务中性能的重要手段。但是，目前大多数现有RAG策略以平铺且无结构的方式处理检索到的内容，这使得模型无法捕获结构线索，并限制了其从分散在多文档中的证据中综合知识的能力。
### Innovation
我们提出了DISCO-RAG，一种话语感知框架，明确将话语信号注入生成过程。该方法通过构建内片段话语树来捕捉局部层次结构，通过构建跨篇章论述图来建模篇章间的一致性。这些结构共同整合成一个规划蓝图，以条件生成过程。在问答和长文档摘要基准上的实验显示了该方法的有效性。DISCO-RAG 在这些基准上达到了最先进的效果，无需微调， 这些发现凸显了话语结构在推进RAG系统中的重要性。
### Conclusion
DISCO-RAG 的发现彰显了话语结构在促进RAG系统方面的重要作用。
## 17. `cs.CL` - TranslateGemma 技术报告 [PDF](https://arxiv.org/pdf/2601.09012), [HTML](https://arxiv.org/abs/2601.09012)
### Authors
Mara Finkelstein,Isaac Caswell,Tobias Domhan,Jan-Thorsten Peter,Juraj Juraska,Parker Riley,Daniel Deutsch,Cole Dilanni,Colin Cherry,Eleftheria Briakou,Elizabeth Nielsen,Jiaming Luo,Kat Black,Ryan Mullins,Sweta Agrawal,Wenda Xu,Erin Kats,Stephane Jaskiewicz,Markus Freitag,David Vilar
### Background
该研究基于Gemma 3基础模型，旨在增强其多语言翻译能力。通过使用两阶段微调过程，首先利用先进的合成平行数据和人工翻译数据进行监督微调，然后使用奖励模型进行强化学习优化，以提高翻译质量。
### Innovation
该研究提出了一种新的翻译套件——TranslateGemma，结合了监督微调和强化学习优化阶段。通过这种方法，TranslateGemma模型在WMT25和WMT24++基准测试中表现出色，特别是在小模型方面超越了基础模型。此外，该模型保持了优秀的跨模态能力，在Vistra图像翻译基准测试中表现更加出色。
### Conclusion
TranslateGemma模型展示了其在多语言翻译中的有效性，并释放了可适应性强的工具以供研究社区使用。这些模型在自动评估和人工评估中均显示出了显著的进步，且小型模型在性能上与大型模型相当，提供了更高的效率。
## 18. `cs.CL` - 受控自我演化算法对算法代码优化 [PDF](https://arxiv.org/pdf/2601.07348), [HTML](https://arxiv.org/abs/2601.07348)
### Authors
Tu Hu,Ronghao Chen,Shuo Zhang,Jianghao Yin,Mou Xiao Feng,Jingping Liu,Shaolei Zhang,Wenqi Jiang,Yuqi Fang,Sen Hu,Huacan Wang,Yi Xu
### Background
现有的自我演化方法通过迭代的“生成-验证-改进”循环增强了代码生成，但由于低探索效率的问题，往往无法在预算范围内找到具有更优复杂度的解决方案。这种低效主要来源于初始化偏差导致的进化被锁定在劣质解区、缺乏反馈指导的随机操作和任务间以及任务内经验利用不足。
### Innovation
本文提出了受控自我演化（CSE），包括三个关键技术组件：多样化的规划初始化、遗传演化的反馈指导机制以及层次化的进化记忆。CSE 的多样化的规划初始化能够生成结构上不同的算法策略，以覆盖广泛的解决方案空间；遗传进化用反馈指导的机制替换随机操作，实现有目标的突变和组合的杂交；层次化的进化记忆在跨任务和任务内层次上捕捉成功和失败的经验。
### Conclusion
在 EffiBench-X 上进行的实验表明，CSE 在各种 LLM 后端模型上始终优于所有基线方法，且从早期生成开始就有更高的效率，并在演化过程中保持连续改进。源代码已在该网址公开：this https URL
## 19. `cs.CL` - TeleMem：构建具有长期和多模态记忆的能动AI [PDF](https://arxiv.org/pdf/2601.06037), [HTML](https://arxiv.org/abs/2601.06037)
### Authors
Chunliang Chen,Ming Guan,Xiao Lin,Jiaxu Li,Luxi Lin,Qiyi Wang,Xiangyu Chen,Jixiang Luo,Changzhi Sun,Dell Zhang,Xuelong Li
### Background
大型语言模型（LLMs）在许多NLP任务中表现优异，但在长时间的对话中维持互动的能力有限，这主要是因为它们在处理扩展对话历史时的注意力限制。检索增强生成（RAG）可以部分缓解这一问题，但缺乏可靠机制来更新或改进存储的记忆，从而导致模式驱动的幻觉、低效的写入操作，以及对多模态支持不足。
### Innovation
本文提出了一种名为TeleMem的一体化的长期和多模态记忆系统。它通过叙事动态提取维持一致的用户档案，确保仅保留对话支持的信息。进一步引入了一个结构化写入管道，该管道批处理、检索、聚类和汇总记忆条目，显著提高了存储效率，减少了令牌使用，并加快了记忆操作。此外，结合了多模态记忆模块和ReAct风格的推理机制，使得系统能够在一个封闭环观察、思考和行动的过程中准确理解复杂的视频内容。
### Conclusion
实验结果显示，TeleMem在ZH-4O长期角色扮演游戏基准测试中超过了当前最先进的Mem0基线，准确率提高了19%，消耗的令牌减少了43%，并且速度提高了2.1倍。
## 20. `cs.CL` - 可扩展且可靠的AI知识检索系统评估：RIKER与一致的模拟宇宙 [PDF](https://arxiv.org/pdf/2601.08847), [HTML](https://arxiv.org/abs/2601.08847)
### Authors
JV Roig
### Background
当前的知识系统评估面临多重挑战：静态基准易受污染，基于LLM（大语言模型）的评判机构存在系统性偏差，真实的地面实况提取则需要昂贵的人工标注。为克服这些挑战，RIKER（检索智能与知识提取评级）提供了一种基于范式倒转的方法——从已知地面实况生成文档，而非从文档中提取地面实况。这种方法实现了无需人工标注或参考模型的确定性评分和可扩展评估，通过再生性语料库增强了抗污染能力。
### Innovation
RIKER是一个基准和可复制的方法论，采用基于范式倒转的技术——生成文档而不是从文档中提取地面实况，从而实现无需人工标注或参考模型的评分和大规模评估，以及再生性语料库提升抗污染能力。
### Conclusion
通过评估超过33个模型，使用超过210亿个令牌，发现语境长度声明经常超过可实用容量，超出32K令牌后表现显著下降；跨文档聚合比单文档提取更加困难；基底能力和幻觉抵抗是不同的能力——擅长发现存在事实的模型可能仍会虚构不存在的事实。RIKER方法还贡献了一种适用于生成从结构化地面实况到合成文档的可扩展和抗污染评估的跨领域方法论。
