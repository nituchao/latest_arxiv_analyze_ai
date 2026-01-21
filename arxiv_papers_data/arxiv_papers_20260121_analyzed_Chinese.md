# 20260121
[![Subscribe_Visitors](https://visitor-badge.laobi.icu/badge?page_id=nituchao.latest_arxiv_analyze_ai_rss)](https://github.com/nituchao/latest_arxiv_analyze_ai)

## 1. `cs.AI` - 基于三值逻辑的趋势模型优化复杂产品创新过程 [PDF](https://arxiv.org/pdf/2601.10768), [HTML](https://arxiv.org/abs/2601.10768)
### Authors
Nina Bočková,Barbora Volná,Mirko Dohnal
### Background
本文探讨了复杂产品创新过程，并通过一组启发式方法建模。每个启发式方法均以简单趋势（增加、减少或保持不变）表达，作为最少信息密集性的量化指标，避免直接依赖具体的数值或粗集。
### Innovation
本文提出的创新是使用基于三值逻辑的趋势模型来表征产品的复杂创新过程。这种方法通过最小的信息密集性量化指标定义了趋势模型的解，即一系列可能场景及其间的转换，用过渡图来表示。
### Conclusion
这种方法能够表示研究系统的任何可能的过去或未来的行为，通过该图中的路径来展现。
## 2. `cs.AI` - 您信任我吗？大型语言模型中信任worthiness的认知情感标志 [PDF](https://arxiv.org/pdf/2601.10719), [HTML](https://arxiv.org/abs/2601.10719)
### Authors
Gerard Yeo,Svetlana Churina,Kokil Jaidka
### Background
用户的在线信息导航依赖于对信息的信任度感知，但尚不清楚越来越多嵌入搜索、推荐和对话系统的大型语言模型（LLMs）在心理方面是否以一致的方式体现这一构建。研究者使用PEACE-Reviews语料库（该数据库标注了认知评估、情绪和行为意图）分析了指令调整的LLMs（Llama 3.1 8B、Qwen 2.5 7B、Mistral 7B）如何在类似网页的叙事中编码信任度。结果显示，这些模型在网络叙事中区分高信任度和低信任度文本的系统层和头级激活差异，表明信任暗示在预训练过程中被隐含编码。进一步的探针分析显示，可以线性解码信任信号，并且微调效果能够细化这些表示而不是重新构建这些表示。
### Innovation
研究揭示了现代LLMs在没有显式监督的情况下内化了心理支持的信任信号，提供了具有可信赖性、透明性和信任的人工智能系统在网页生态系统中的表示基础。这是首次从认知和情感的角度系统研究大型语言模型中的信任度感知。
### Conclusion
研究表明，现代大型语言模型可以理解并体现类似于人类形成在线信任的心理机制和信任维度，而无需额外的监督。这对于设计可信的AI系统具有重要意义，尤其是在网状叙事环境中。
## 3. `cs.AI` - ORBITFLOW：细粒度KV缓存重构以实现长上下文LLM服务的SLO意识 [PDF](https://arxiv.org/pdf/2601.10729), [HTML](https://arxiv.org/abs/2601.10729)
### Authors
Xinyue Ma,Heelim Hong,Taegeon Um,Jongseop Lee,Seoyeong Choy,Woo-Yeon Lee,Myeongjae Jeon
### Background
长上下文LLM服务中直接响应请求长度和批处理组成的变化具有挑战性，这会导致内存占用在运行时显著波动。将KV缓存卸载到主机内存虽然限制了有效的内存使用，但现有的静态和预先确定的卸载策略无法适应长上下文服务中迅速变化的内存需求。这通常会导致超出预期的CPU到GPU的KV传输，进而导致延迟波动和频繁违反SLO目标。
### Innovation
ORBITFLOW引入了一种细粒度和自适应的KV缓存管理系统，能够在长上下文LLM服务中满足延迟SLO要求。ORBITFLOW使用轻量级ILP解决器，根据内存容量约束，在每次请求中决定要保留哪一层的KV缓存。它还基于运行时反馈不断优化KV放置。在负载过重时，ORBITFLOW会使用回退机制暂时保留当前正在处理的大型内存占用请求，以保持整体SLO的实现。
### Conclusion
我们的实验表明，ORBITFLOW将TPOT和TBT的SLO实现分别提高了66%和48%，将95th分位数的延迟降低了38%，并在吞吐量方面比现有卸载方法提高了3.3倍。
## 4. `cs.AI` - ARC Prize 2025: 技术报告 [PDF](https://arxiv.org/pdf/2601.10904), [HTML](https://arxiv.org/abs/2601.10904)
### Authors
François Chollet,Mike Knoop,Gregory Kamradt,Bryan Landers
### Background
ARC-AGI 挑战赛系列为评估新型任务的少量样本泛化能力提供了一个关键指标，这是智能的核心方面。ARC Prize 2025 全球竞赛针对新发布的 ARC-AGI-2 数据集，该数据集的复杂性比其前身更高。Kaggle 竞赛吸引了 1,455 支团队和 15,154 个参赛作品，最高分为 24%。提交论文的数量几乎翻了一番，达到 90 篇，反映出对流动智能和抽象推理的研究兴趣增长。2025 年的主题是情节细化循环——一种由反馈信号引导的任务迭代程序优化循环。此类循环主要有进化程序合成方法和商业 AI 系统的应用层细化。此外，零预训练的深度学习方法现在使用的小网络（7M 参数）也能取得竞争力的性能。
### Innovation
全球竞赛针对更新更复杂的 ARC-AGI-2 数据集，吸引了大量队伍和参赛作品，反映出研究兴趣的增长。重点讨论了情节细化循环在 AGI 进展中的作用，以及知识依赖性过拟合的问题。还预测了 ARC-AGI-3，引入了需要探索、规划、记忆、目标获取和对齐能力的互动推理挑战。
### Conclusion
当前前沿 AI 推理性能仍然受到知识覆盖范围的根本限制，产生了新的基准污染形式。本文总结了顶级方法，探讨了情节细化循环在 AGI 进展中的作用，讨论了知识依赖过拟合，以及展望了新的 ARC-AGI-3 挑战，包括互动推理挑战。
## 5. `cs.AI` - 构建改进陌生人求职推荐请求的AI代理 [PDF](https://arxiv.org/pdf/2601.10726), [HTML](https://arxiv.org/abs/2601.10726)
### Authors
Ross Chu,Yuting Huang
### Background
本文探讨了在专业的在线社区中，通过开发AI代理帮助求职者撰写有效的求职推荐请求。基本的工作流程包括一个改进代理，用于重写推荐请求，以及一个评估代理，使用已训练的模型来测量修订的质量，该模型可以预测从其他用户那里获得推荐的概率。
### Innovation
本文的创新在于使用了大型语言模型（LLM）的修订，结合检索增强生成（RAG）技术，提高了较弱请求的预测成功率14%，同时没有损害较强请求的表现。相较于标准的LLM修订，RAG防止了对较强请求的负面修订，并增强了对较弱请求的改进。
### Conclusion
虽然模型预测的成功率改善并不保证真实世界中更多推荐的获得，但使用LLM修订与RAG增强了这些预测的信号价值，为在用户进行高风险实验前提供了低成本的评估手段。
## 6. `cs.AI` - 多模态推理的数据整理中什么是重要的？DCVLR 挑战的见解 [PDF](https://arxiv.org/pdf/2601.10922), [HTML](https://arxiv.org/abs/2601.10922)
### Authors
Yosub Shin,Michael Buriek,Boris Sobolev,Pavel Bushuyeu,Vikas Kumar,Haoyang Xu,Samuel Watson,Igor Molybog
### Background
本文通过 NeurIPS 2025 视觉语言推理数据整理挑战（DCVLR）研究多模态推理的数据整理。该挑战通过固定模型和训练协议来隔离数据集选择。研究通过一个源自 Wal顿多模态冷启动的紧凑整理数据集进行实验，并展示了基于难度的选择对性能的显著影响。
### Innovation
通过在固定训练配方下分析不同数据集的性能，特别是探讨了难度为导向的选择方法如何显著提升性能；同时发现增加数据集规模并不能可靠地提高均值准确性，而主要减少多次运行之间的变异性；并且常用的数据多样性和合成增强策略在该挑战中并不能提供额外的好处，有时甚至会降低性能。这些结果使 DCVLR 成为了一个饱和评价标准，强调了对齐和难度在多模态推理中的核心作用。
### Conclusion
这些发现表明 DCVLR 是一个饱和评估环境，并突显了对其像难度和对齐等关键因素的重视。
## 7. `cs.AI` - 日本的人乳头瘤病毒疫苗智能代理系统：系统设计 [PDF](https://arxiv.org/pdf/2601.10718), [HTML](https://arxiv.org/abs/2601.10718)
### Authors
Junyu Liu,Siwen Yang,Dexiu Ma,Qian Niu,Zequn Zhang,Momoko Nagai-Tanima,Tomoki Aoyama
### Background
在2013年至2021年期间，日本因息发布了关于人乳头瘤病毒（HPV）疫苗接种的积极推荐建议，导致公众对HPV疫苗的犹豫不决，进而产生了信息缺口。社交媒体上的错误信息加剧了这一问题。传统的信息传递方式难以同时处理个人查询和监测人群层面的讨论。
### Innovation
该研究开发了一种双向AI代理系统，通过对话界面提供经过验证的HPV疫苗信息，同时基于用户互动和社交媒体生成分析报告。该系统结合向量数据库和采用ReAct代理架构的检索增强生成聊天机器人，以及自动化报告生成系统，包含新闻分析、研究综合、社交媒体情绪分析和用户互动模式识别模块。
### Conclusion
该研究证明了集成AI代理系统在双向HPV疫苗沟通方面的可行性。该体系结构使得经过验证的信息传递，并带有来源归属，同时还提供了系统性的公众讨论分析，具有适应其他医学背景的可转移框架。
## 8. `cs.AI` - AdaMARP: 一种通用沉浸式多智能体互动框架 [PDF](https://arxiv.org/pdf/2601.11007), [HTML](https://arxiv.org/abs/2601.11007)
### Authors
Zhenhua Xu,Dongsheng Chen,Shuo Wang,Jian Li,Chengjie Wang,Meng Han,Yabiao Wang
### Background
现有基于大语言模型的多智能体角色扮演系统在沉浸感和适应性方面存在局限，通常无法很好地建模动态环境信息，假设场景和角色相对静态，缺乏对多角色协同、场景转换和临时角色引入的支持。
### Innovation
提出了一个适应性多智能体角色扮演框架AdaMARP，包括一种沉浸式的消息格式，该格式交替呈现Thought、Action、Environment和Speech，以及明确的场景管理器，通过离散的动作（init_scene, pick_speaker, switch_scene, add_role, end）和理由来进行管理和决策。同时，构建了AdaRPSet用于演员模型的训练，以及AdaSMSet用于指导调度决策，并引入了AdaptiveBench用于轨迹级别的评估。
### Conclusion
通过在多个骨干网络和模型规模上进行实验，结果表明，AdaRPSet提高了角色一致性、环境连接性和叙事连贯性，8B的大语言模型优于几个商业系统，并且AdaSMSet使场景转换更加平滑、角色引入更加自然，仅用14B的LLM就优于Claude Sonnet 4.5。
## 9. `cs.AI` - CTHA：稳定多智能体LLM系统的约束时序层次架构 [PDF](https://arxiv.org/pdf/2601.10738), [HTML](https://arxiv.org/abs/2601.10738)
### Authors
Percy Jardine
### Background
近年来，多时间尺度代理架构扩展了普遍的单环范式，通过引入具有不同认知层次的时间层次结构。这虽然带来了显著的性能提升，但实质上损害了统一代理系统内部的协调稳定性，导致严重的跨层冲突、无限的错误传播以及受限的扩展性。
### Innovation
本文提出了约束时序层次架构（CTHA），这是一种通用框架，通过将跨层通信空间映射到结构化的流形上以恢复协调稳定性，并纳入了原则性的仲裁机制以确保一致的决策。具体而言，CTHA 实施了三大关键约束：（1）消息合同约束，通过类型化的摘要、计划和策略包来形式化层间的信 息流动；（2）权威流形约束，根据其时间范围限制每一层的决策空间；（3）仲裁解决约束，保证多层决策的无冲突组合。
### Conclusion
实验证明，CTHA 在复杂任务的大规模执行中是有效的，减少了 47% 的失败级联，样本效率提高了 2.3 倍，并且比不受约束的层次基准更具扩展性。我们预计，CTHA 作为时序层次的一种原则性扩展，将有助于对多智能体协调的更深入理解，并为鲁棒自主系统的进化指出有前景的方向。
## 10. `cs.AI` - 携长期记忆探索：基于多模态LLM的强化学习框架用于体态探索 [PDF](https://arxiv.org/pdf/2601.10744), [HTML](https://arxiv.org/abs/2601.10744)
### Authors
Sen Wang,Bangwei Liu,Zhenkun Gao,Lizhuang Ma,Xuhong Wang,Yuan Xie,Xin Tan
### Background
想象中的理想体态智能体应具备终生学习能力，能够处理长期和复杂任务，并在各种一般环境中持续运行。这不仅需要智能体准确执行给定的任务，还需要利用长期的事件记忆来优化决策。然而，当前主流的一次性体态任务主要关注任务完成的结果，而忽视了探索和记忆利用的过程。为解决这一问题，作者提出了长时记忆体态探索（LMEE），旨在统一智能体的探索性和决策行为，促进终生学习。为了进一步构建对应的基准数据集LMEE-Bench，该数据集含有多目标导航和基于记忆的问题回答，以全面评估体态探索的过程和结果。
### Innovation
提出了长时记忆体态探索（LMEE），方法包括：1）一个名为MemoryExplorer的新颖方法，通过基于强化学习的调优多模态大语言模型，促进主动的记忆查询；2）设计了一个包含动作预测、前沿选择和问题回答的多任务奖励函数，促使模型实现主动探索。通过与最新的体态探索模型的广泛实验，证明了该方法在长期任务中的显著优势。
### Conclusion
提出的LMEE方法和MemoryExplorer，在多目标导航和基于记忆的问题回答的基准数据集LMEE-Bench上进行评估，显著提高了体态智能体的记忆检索能力和主动探索能力。该方法为体态探索任务提供了一个有效的解决方案，尤其是在处理具有长期视角的任务时。
## 11. `cs.CL` - MADIAVE: 多代理论辩对隐含属性值提取 [PDF](https://arxiv.org/pdf/2510.05611), [HTML](https://arxiv.org/abs/2510.05611)
### Authors
Wei-Chieh Huang,Cornelia Caragea
### Background
在电子商务中，隐含属性值提取（AVE）是准确表示产品的关键，它能从多模态数据中推断出潜在属性。尽管在多模态大型语言模型（MLLM）方面取得了进展，但由于多维数据的复杂性和视觉-文本理解中的鸿沟，隐含AVE仍然具有挑战性。
### Innovation
本文提出了一个基于多代理机制的框架——MADIAVE，通过多个MLLM代理的迭代验证和更新，提高推断性能和鲁棒性。研究了不同配置的代理辩论回合对收敛动态的影响，展示了代理辩论策略在解决单一代理方法限制方面的潜力。
### Conclusion
实验表明，通过几轮辩论可以显著提高准确性，尤其是对于初始表现较低的属性，展示了多代理辩论策略在多模态电子商务中隐含AVE中的可扩展性解决方案。
## 12. `cs.CL` - LLMs在教育中的机遇与挑战：从NLP视角 [PDF](https://arxiv.org/pdf/2507.22753), [HTML](https://arxiv.org/abs/2507.22753)
### Authors
Sowmya Vajjala,Bashar Alhafni,Stefano Bannò,Kaushal Kumar Maurya,Ekaterina Kochmar
### Background
近年来，人们对大型语言模型（LLMs）在教育中的作用越来越感兴趣，考虑到它们在教学、学习和评估方面提供的新机遇。本文从自然语言处理（NLP）的角度，探讨了LLMs对教育中NLP的影响，并重点关注了‘辅助与评估’两大应用场景，通过对阅读、写作、口语和辅导四个维度的评估，来研究LLMs带来的新方向及其要解决的关键挑战。
### Innovation
本文提出了一个全面的视角，概述了LLMs在教育中的潜力，特别是对NLP研究人员和实践者在未来开发以语言为中心和NLP赋能的教育应用方面的重要性。
### Conclusion
本文认为这种全面的概述将有助于NLP研究人员和实践者探索LLMs在未来教育中的作用，并推进相关领域的研究和发展。
## 13. `cs.CL` - DecoupledESC: 通过策略-响应解耦的偏好优化提升情感支持生成 [PDF](https://arxiv.org/pdf/2505.16995), [HTML](https://arxiv.org/abs/2505.16995)
### Authors
Chao Zhang,Xin Shi,Xueqiao Zhang,Yifan Zhu,Yi Yang,Yawei Luo
### Background
近期的研究进展通过监督微调（SFT）大型语言模型（LLMs）来改进情感支持生成（ESC）。然而，常见的心理错误仍然存在。直接偏好优化（DPO）在减少这些错误方面显示出潜力，但其在ESC任务中的有效性受到两大挑战的限制：1. 缠结的数据结构：现有的ESC数据将心理策略和响应内容缠结在一起，使其难以构建高质量的偏好对；2. 最优化的不确定性：将传统的DPO应用于此类缠结的成对数据会导致训练目标模糊。
### Innovation
本文引入了推断偏好挖掘（IPM）来构建高质量的偏好数据，形成了IPM-PrefDial数据集。在此基础上，提出了一个基于格罗斯扩展情感调节过程模型的解耦ESC框架。该框架分解ESC任务为两个相继的子任务：策略规划和共情响应生成，每个子任务都通过SFT进行训练，并通过DPO进一步增强，以与心理偏好对齐。
### Conclusion
广泛的实验表明，我们的解耦ESC框架在偏好偏差和响应质量方面优于联合优化基线。
## 14. `cs.CL` - LLMs中成语比喻义与字面义之间的博弈 [PDF](https://arxiv.org/pdf/2506.01723), [HTML](https://arxiv.org/abs/2506.01723)
### Authors
Soyoung Oh,Xinting Huang,Mathis Pink,Michael Hahn,Vera Demberg
### Background
成语由于其非成分性的比喻解释方式，为语言模型带来了独特的挑战。这些比喻义与成语的字面意义往往相差甚远，给模型正确理解和使用成语增添了难度。
### Innovation
本文采用因果追踪方法系统分析预训练因原因自变换器如何处理成语的歧义性。研究发现了三种机制：早期子层和特定注意力头检索成语的比喻解释，抑制其字面解释；当先出场的背景信息有助于成语消歧，则从最早层抽取该信息，并在后续层对其进行精炼；接着，选择性、竞争路径携带两种解释：中间路径优先处理比喻解释，而并行直接路径则偏好字面意义，确保两种解释的可用性。
### Conclusion
研究提供了自动回归变换器中成语理解的机制性证据。
## 15. `cs.CL` - MIST：用于Theory of Mind的多维隐性偏见评估框架 [PDF](https://arxiv.org/pdf/2506.14161), [HTML](https://arxiv.org/abs/2506.14161)
### Authors
Yanlin Li,Hao Liu,Huimin Liu,Kun Wang,Yinwei Wei,Yupeng Hu
### Background
传统的直接查询方法在评估大型语言模型（LLM）的Theory of Mind（ToM，他人心理状态推理能力）时效果不佳，因为模型往往拒绝回答，且无法全面捕捉ToM能力的微妙和复杂性。
### Innovation
作者提出了一种名为MIST的方法，将刻板印象的内容模型重构为ToM的多维度失败，特别是在技能、社交和道德领域。MIST框架引入了两种间接任务：Word Association Bias Test (WABT)评估隐含的词汇关联，Affective Attribution Test (AAT)测量隐含的情感倾向，旨在避免模型逃避诊断。
### Conclusion
通过对八款最先进的LLM进行广泛的实验，框架展示了揭示复杂偏见结构和增强鲁棒性的能力。所有数据和代码将被公开共享。
## 16. `cs.CL` - 深度嵌入的表示：大型语言模型中文化偏见的机械研究 [PDF](https://arxiv.org/pdf/2508.08879), [HTML](https://arxiv.org/abs/2508.08879)
### Authors
Haeun Yu,Seogyeong Jeong,Siddhesh Pawar,Jisu Shin,Jiho Jin,Junho Myung,Alice Oh,Isabelle Augenstein
### Background
随着大型语言模型（LLMs）在不同文化背景下的广泛应用，了解这些模型对各种文化的表示变得越来越重要。以往的研究主要通过评估生成文本的文化意识来检查LLMs的文化敏感性，但这种评估忽视了模型内部存在的文化误表征源。因此，本研究旨在通过提出的Culturescope方法，这是第一个基于机理解释的方法，以探查LLMs中不同文化知识的内部表示。此外，研究还探讨了LLMs如何内化文化偏见，从而能够追踪西方主导偏见和文化扁平化等文化偏见是如何在LLMs中出现和发展起来的。
### Innovation
本研究提出了Culturescope方法，首次基于机理解释的方式探究LLMs中不同文化知识的内部表示。研究引入了一个文化扁平化得分，作为解码知识中的内在文化偏见的衡量标准。此外，研究还研究了LLMs如何内化文化偏见，从而能够追踪文化偏见是如何在LLMs中出现和发展的。
### Conclusion
研究发现，低资源文化较少受到文化偏见的影响，这可能是由于模型自身的参数知识有限。本研究为未来减少文化偏见和提升LLMs的文化理解提供了一个基础。
## 17. `cs.CL` - MedReflect：通过反思纠正教导医疗LLM自我提升 [PDF](https://arxiv.org/pdf/2510.03687), [HTML](https://arxiv.org/abs/2510.03687)
### Authors
Yue Huang,Yanyuan Chen,Dexuan Xu,Chenzhuo Zhao,Weihua Yue,Yu Huang
### Background
医学问题解决需要深厚的专业知识和复杂的推理。虽然大型语言模型（LLMs）的研究试图通过检索增强生成或通过训练于推理数据集来简化这一复杂性，但这些方法存在检索过程中的冗余和高标注成本问题，且高度依赖外部助手来达到有限的医疗性能。当前方法未能充分利用大型语言模型内在的能力。
### Innovation
本文介绍了一种名为MedReflect的一般框架，旨在启发LLMs具备医生式的反思思维模式。MedReflect生成单一通道的反思链，包含初始假设生成、自我质疑、自我回答和决策改进。这种自我验证和自我反思的特性使得大型语言模型在没有外部检索或大量标注的情况下也能应对医学问题解决。此外，MedReflect展示了高效低成本的医疗数据集构建方法，仅需少量随机采样的训练示例和轻量级微调即可实现显著的绝对准确率提升，大幅减少了标注需求。
### Conclusion
我们的研究结果表明，通过自我反思和自我改进，大型语言模型可以学会解决专门的医学问题，从而减少对外部监督和特定任务数据集的依赖。
## 18. `cs.CL` - SDialog：一种端到端代理构建、用户模拟、对话生成和评估的Python工具箱 [PDF](https://arxiv.org/pdf/2506.10622), [HTML](https://arxiv.org/abs/2506.10622)
### Authors
Sergio Burdisso,Séverin Baroudi,Yanis Labrak,David Grunert,Pawel Cyrta,Yiyang Chen,Srikanth Madikeri,Thomas Schaaf,Esaú Villatoro-Tello,Ahmed Hassoon,Ricard Marxer,Petr Motlicek
### Background
当前人工智能领域内，对话生成、评估和解释性工具的独立存在限制了研究者对对话系统的全面理解和系统性构建。SDialog旨在通过提供一个统一的端到端框架，整合对话生成、评价和机械解释性工具，来解决这些问题。
### Innovation
SDialog通过统一框架整合了对话生成、用户模拟、对话生成和评估功能，包括标准的对话表示、多代理模拟、功能齐全的评估工具以及机械解释性工具。此外，该工具箱还提供了音频生成功能，包括三维房间建模和麦克风效应模拟。它支持所有主要的大语言模型后端，使研究者能够进行混合后端实验。
### Conclusion
SDialog为研究人员提供了一个全面的平台，能够系统地构建、基准测试和理解基于LLM的对话系统。通过这种方式，研究者能够更有效地模拟和评估对话系统的性能和解释性。
## 19. `cs.CL` - LLM为中心的语音生成中好的语音标记器是什么？一项系统研究 [PDF](https://arxiv.org/pdf/2506.12537), [HTML](https://arxiv.org/abs/2506.12537)
### Authors
Xiaoran Fan,Zhichao Sun,Yangfan Gao,Jingfei Xiong,Hang Yan,Yifei Cao,Jiajun Sun,Shuo Li,Zhihao Zhang,Zhiheng Xi,Yuhao Zhou,Senjie Jin,Changhao Jiang,Junjie Ye,Ming Zhang,Rui Zheng,Zhenhua Han,Yunke Zhang,Demei Yan,Shaokang Dong,Tao Ji,Tao Gui
### Background
语音-语言模型（SLMs）提供了一条有希望的途径，用于统一语音和文本的理解和生成。然而，在实现有效的跨模态对齐和高质量语音生成方面仍存在挑战。这项工作中，研究者系统地探讨了在LLM为中心的SLMs中语音标记器设计的作用，这些模型被扩展了语音头部和说话人建模。在公平的SLM框架下，对比了耦合型、半解耦型和全解耦型语音标记器，并发现解耦标记显著提高了对齐和合成质量。
### Innovation
（1）引入了多令牌预测（MTP）到SLMs中，使每个隐藏状态能够解码多个语音令牌，导致解码速度提高了12倍并且词错率大幅度下降（从6.07降至3.01）；（2）提出了基于说话人的生成范式，并引入了具有多样说话人身份的大规模角色扮演知识问答基准（RoleTriviaQA）。
### Conclusion
实验证明，我们的方法增强了知识理解能力和说话人一致性。
## 20. `cs.CL` - Chandomitra: 从自然语言输入生成结构化梵文诗的方向 [PDF](https://arxiv.org/pdf/2506.00815), [HTML](https://arxiv.org/abs/2506.00815)
### Authors
Manoj Balaji Jagadeeshan,Samarth Bhatia,Pretam Ray,Harshul Raj Surana,Akhil Rajeev P,Priya Mishra,Annarao Kulkarni,Ganesh Ramakrishnan,Prathosh AP,Pawan Goyal
### Background
大型语言模型已经在文本生成方面取得了显著成果，特别是对于高资源语言，显示出强大的创造性生成能力。然而，如何利用这些大型语言模型进行低资源语言的诗结构化生成，特别是梵文，仍然具有挑战性。
### Innovation
本文提出了Chandomitra数据集，该数据集针对Anushtubh节拍规范，将其作为一种英语输入到结构化梵文诗转换的解决方案。此外，该研究还比较了不同开放和封闭模型，并采用了受限解码和指令微调等特定技术来解决该任务。这种方法在生成语法规则有效的梵文诗歌时达到了99.86%的语法准确性。最好微调模型在语义连贯性方面优于未微调模型，但语法规则准确性稍低。
### Conclusion
Chandomitra 数据集和基于此数据集的研究为使用大型语言模型生成结构化低资源语言的诗歌提供了重要的支持。通过受限解码和指令微调等技术，能够有效生成梵文诗，并可能更好地捕捉诗歌的文学特点。相关数据和代码可获取。
