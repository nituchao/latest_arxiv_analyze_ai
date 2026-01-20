# 20260120
[![Subscribe_Visitors](https://visitor-badge.laobi.icu/badge?page_id=nituchao.latest_arxiv_analyze_ai_rss)](https://github.com/nituchao/latest_arxiv_analyze_ai)

## 1. `cs.AI` - 长时记忆驱动的探索：基于多模态大语言模型的强化学习框架及其基准 [PDF](https://arxiv.org/pdf/2601.10744), [HTML](https://arxiv.org/abs/2601.10744)
### Authors
Sen Wang,Bangwei Liu,Zhenkun Gao,Lizhuang Ma,Xuhong Wang,Yuan Xie,Xin Tan
### Background
理想的实体代理应该具备终身学习能力，以处理长期和复杂的任务，从而在各种环境中保持连续运作。这不仅要求代理能够准确完成给定任务，还需要利用长期事件记忆优化决策。现有的主流单次学习实体任务主要关注任务完成的结果，忽视了探索和记忆利用的关键过程。因此，需要一种方法来统一代理的探索认知和决策行为，以促进终身学习。
### Innovation
提出了长时记忆驱动的探索（LMEE）框架，旨在统一代理的探索认知和决策行为，促进终身学习。进一步构建了一个相关的数据集和基准LMEE-Bench，涵盖多目标导航和基于记忆的问题解答，以全面评估实体探索过程和结果。还提出了一种名为MemoryExplorer的新方法，通过强化学习微调多模态大语言模型，鼓励积极的记忆查询，并通过包含动作预测、边界选择和问题解答的多任务奖励函数实现积极的探索。
### Conclusion
与最先进的实体探索模型的广泛实验表明，我们的方法在长期前景实体任务中实现了显著优势。
## 2. `cs.AI` - 您信任我吗？大型语言模型中的信任worthiness的认知-情感特征 [PDF](https://arxiv.org/pdf/2601.10719), [HTML](https://arxiv.org/abs/2601.10719)
### Authors
Gerard Yeo,Svetlana Churina,Kokil Jaidka
### Background
用户在在线环境中导航信息时，感知的信任度起着关键作用，但目前尚不清楚大型语言模型（LLMs）是否以心理上一致的方式表征这种构建。LLMs越来越被嵌入到搜索引擎、推荐系统和对话系统中，因此理解它们在心理上如何处理信任感至关重要。
### Innovation
本研究分析了指令调整的LLMs（如Llama 3.1 8B、Qwen 2.5 7B、Mistral 7B）如何在包含认知评价、情绪和行为意图的PEACE-Reviews数据集中的在线网络叙事中体现信任感。通过探针分析，研究揭示了线性可解的信任信号以及精细调整效果，这些影响使得模型能够更准确地理解信任概念，而不是重新构建它们的内部表示。研究发现在公平性、确定性和自我问责这一人类在线信任形成的中心维度上具有最强的相关性。
### Conclusion
研究表明，现代LLMs能够内化心理上一致的信任信号，而无需显式的监督。这些发现为设计在Web生态系统中具有可信赖性、透明性和信任感的AI系统提供了代表性的基础。相关代码和附录可在指定网址获得。
## 3. `cs.AI` - 基于三值逻辑的趋势模型优化复杂产品创新过程 [PDF](https://arxiv.org/pdf/2601.10768), [HTML](https://arxiv.org/abs/2601.10768)
### Authors
Nina Bočková,Barbora Volná,Mirko Dohnal
### Background
该论文旨在利用基于一组启发式方法的模型研究复杂的产品创新过程。每个启发式方法通过简单的趋势（增加、减少或不变）来表达，这种方式是一种最小信息密集度量化的手段，避免了对具体数值或粗糙集的依赖。
### Innovation
提出的创新在于将复杂的创新过程建模为趋势模型，并利用三值逻辑来定义趋势模型的解。具体表现为通过简单的趋势（增加、减少或不变）来表示启发式方法，以及将可能的场景及其转换通过过渡图表示，从而描绘出系统的任何过去或未来行为。
### Conclusion
任何有待研究系统未来的或过去的行旳为都能够通过该图中的路径来表示，从而为复杂的产品创新过程提供了一种新的优化方法和路径可视化方式。
## 4. `cs.AI` - 构建用于改善向陌生人寻求职位推荐的AI代理 [PDF](https://arxiv.org/pdf/2601.10726), [HTML](https://arxiv.org/abs/2601.10726)
### Authors
Ross Chu,Yuting Huang
### Background
本文介绍了帮助求职者在职业在线社区中撰写有效职位推荐请求的工作。基本工作流程包括一个改写请求的改进代理和一个评估代理，后者使用一个训练模型来测量改写质量，该模型可预测从其他用户那里收到职位推荐的可能性。
### Innovation
本文创新之处在于使用大型语言模型（LLM）及其增强版本（如检索增强生成RAG）来改进并向陌生人寻求职位推荐的请求。LLM改写的建议提高了较弱请求的成功率，而减少了较强请求的成功率。通过结合RAG，编辑不会恶化较强请求，同时可以放大较弱请求的改进。使用与RAG结合的LLM改写增加了较弱请求预测成功率为14%，而不影响较强请求的表现。
### Conclusion
尽管模型预测的成功改善并不保证在实际世界中会获得更多的推荐，但在真实用户上进行更高风险实验之前，它们为潜在的特征提供了低成本的信号。
## 5. `cs.AI` - 日本的人乳头瘤病毒疫苗AI代理系统：系统设计 [PDF](https://arxiv.org/pdf/2601.10718), [HTML](https://arxiv.org/abs/2601.10718)
### Authors
Junyu Liu,Siwen Yang,Dexiu Ma,Qian Niu,Zequn Zhang,Momoko Nagai-Tanima,Tomoki Aoyama
### Background
在2013年至2021年间，日本因为HPV疫苗接种建议主动暂停，导致了信息空白，同时社交媒体上的不实信息进一步加剧了这方面的疑惑。传统方法难以同时解决个体查询需求并监控公共层面的讨论。
### Innovation
该研究提出了一种双用途AI代理系统，通过对话界面提供验证过的HPV疫苗信息，并基于用户互动和社交媒体生成分析报告。系统集成了向量化数据库、检索增强生成聊天机器人以及自动报告生成系统，涵盖了新闻分析、研究综合、社交媒体情绪分析和用户互动模式识别等多个模块。
### Conclusion
该研究展示了整合AI代理系统在双向HPV疫苗沟通中的可行性。系统架构能在提供验证信息的同时记录来源，并进行系统化的公共讨论分析。这一框架具有转移性，适用于其他医疗领域。
## 6. `cs.AI` - ARC Prize 2025: 技术报告 [PDF](https://arxiv.org/pdf/2601.10904), [HTML](https://arxiv.org/abs/2601.10904)
### Authors
François Chollet,Mike Knoop,Gregory Kamradt,Bryan Landers
### Background
这篇论文背景在于介绍ARC-AGI基准系列，它是衡量新任务上少量示例泛化的关键指标，是智能的核心方面。2025年的ARCG-AGI-2数据集发布了，这比前一代更为复杂。Kaggle竞赛吸引了1455个团队和15154个参赛作品，最高得分为24%。论文投稿量几乎翻了一番，达到了90份，反映了对流体智能和抽象推理研究兴趣的增长。2025年的主要主题是‘细化循环’，这是一种由反馈信号引导的任务特定迭代程序优化循环。
### Innovation
新颖之处在于ARCG-AGI-2数据集的发布，比前一代更复杂。比赛吸引了大量参赛作品和团队，细化循环作为分析方法在智能进步中的角色得到强调。并讨论了数据集在知识依赖性过拟合方面的新形式基准污染。此外，还介绍了新的ARC-AGI-3基准，它引入了需要探索、规划、记忆、目标获取和对齐能力的交互式推理挑战。
### Conclusion
当前前沿的人工智能推理性能依然受到知识覆盖的限制，揭示了新的基准污染形式。论文总结了领先的方法，探讨了细化循环在AGI进展中的角色，讨论了知识型过拟合，并预览了即将发布的交互式推理挑战ARCG-AGI-3。
## 7. `cs.AI` - ORBITFLOW：细粒度KV缓存重新配置的SLO感知长上下文LLM服务 [PDF](https://arxiv.org/pdf/2601.10729), [HTML](https://arxiv.org/abs/2601.10729)
### Authors
Xinyue Ma,Heelim Hong,Taegeon Um,Jongseop Lee,Seoyeong Choy,Woo-Yeon Lee,Myeongjae Jeon
### Background
提供带有长上下文的LLM服务具有挑战性，因为请求长度和批次组成在标记生成过程中发生变化，导致内存占用在运行时显著波动。将KV缓存卸载到主机内存可以限制有效内存使用，但现有静态和预先决定的卸载策略无法适应长上下文服务中快速变化的内存需求。这通常会导致CPU到GPU的KV转移过多，导致延迟峰值和频繁违反服务水平目标（SLO）。
### Innovation
我们介绍了ORBITFLOW，这是一种细粒度且自适应的KV缓存管理系统，能够在长上下文LLM服务中满足延迟SLO。ORBITFLOW使用轻量级整数线性规划（ILP）求解器，在内存容量限制内，为每个请求决定哪些层级的KV缓存保留在GPU上。它根据运行时反馈持续优化KV的放置。在重负载下，ORBITFLOW会激活回退机制，以暂时推迟具有大内存占用的新传入请求，从而保持总体SLO的实现。
### Conclusion
我们的实验表明，与现有的卸载方法相比，ORBITFLOW将TPOT和TBT的SLO实现分别提高了66%和48%，将95百分位数延迟降低了38%，并实现了高达3.3倍的吞吐量提升。
## 8. `cs.AI` - AdaMARP: 一种通用沉浸式角色扮演的自适应多智能体交互框架 [PDF](https://arxiv.org/pdf/2601.11007), [HTML](https://arxiv.org/abs/2601.11007)
### Authors
Zhenhua Xu,Dongsheng Chen,Shuo Wang,Jian Li,Chengjie Wang,Meng Han,Yabiao Wang
### Background
现有的基于大语言模型（LLM）的角色扮演系统在沉浸感和适应性方面存在局限。这些系统通常无法很好地建模动态环境信息，假设场景和演员大量静态，因此在多角色协调、场景转换以及临时引入角色方面支持不足。
### Innovation
提出了一种自适应多智能体角色扮演框架AdaMARP，它采用一种沉浸的消息格式，嵌入了思考、行动、环境和对话，以及一个明确的场景管理器，通过离散的动作（初始化场景、选择说话者、切换场景、增加角色、结束）及其理由来管理角色扮演。
### Conclusion
在多个模型骨架和规模上的实验结果表明，AdaRPSet增强了角色的一致性、环境连贯性和叙事连贯性，与几款商用LLM相比，8B演员的表现更为出色；而AdaSMSet则使场景过渡更为平滑，角色介绍更自然，仅使用14B LLM就超越了Claude Sonnet 4.5。
## 9. `cs.AI` - 多模态推理数据整理中关键因素有哪些？来自DCVLR挑战赛的见解 [PDF](https://arxiv.org/pdf/2601.10922), [HTML](https://arxiv.org/abs/2601.10922)
### Authors
Yosub Shin,Michael Buriek,Boris Sobolev,Pavel Bushuyeu,Vikas Kumar,Haoyang Xu,Samuel Watson,Igor Molybog
### Background
该研究通过NeurIPS 2025多模态数据整理挑战（DCVLR）探讨了多模态推理的数据整理问题。挑战中固定了模型和训练协议，重点隔离了数据集的选择。研究者利用一个紧凑的整理后的数据集主要源自Walton多模态冷启动，提交取得了挑战的第一名。
### Innovation
通过竞赛后的消除性实验，研究者发现基于难度选择对齐的数据集上的样本是决定性能提升的主要因素。增加数据集的大小并不能可靠地提高平均准确性，而主要减少运行间差异。常用的多样性和合成增强策略没有额外的益处，有时甚至会降低性能。这项结果将DCVLR描述为效率极限评估，并强调了一致性和难度在数据有效多模态推理中的核心作用。
### Conclusion
这些结果表明，数据整理对于多模态推理至关重要。通过固定的训练配方，数据集的选择主要驱动性能的提升。挑战本身作为一种效率极限的评估，强调了保持数据对齐和控制数据难度的重要性。
## 10. `cs.AI` - CTHA: 受约束的时间递归架构以实现稳定的多智能体LLM系统 [PDF](https://arxiv.org/pdf/2601.10738), [HTML](https://arxiv.org/abs/2601.10738)
### Authors
Percy Jardine
### Background
近年来，多时间尺度代理架构通过引入具有不同认知层的时间层次结构扩展了普遍的单环范式。虽然这种多样化能够带来显著的性能提升，但客观上损害了统一代理系统内部固有的协调稳定性，从而导致层间冲突严重、错误传播不受限以及扩展性受限。
### Innovation
我们提出了一种名为Constrained Temporal Hierarchical Architecture (CTHA) 的通用框架，该框架通过将层间通信空间投影到结构化的流形上，以恢复协调稳定性，同时采用合理的仲裁机制以确保决策的一致性。CTHA 遵循三项关键约束条件：（1）消息契约约束，通过类型化的摘要、计划和策略包来规范各层之间的信息流动；（2）权力流形约束，根据每个层的时间范围限制其决策空间；（3）仲裁解决约束，保证多层决策的无冲突组合。实验证明，CTHA 对于大规模复杂任务执行非常有效，能够减少47%的失败传播链，提高样本效率2.3倍，并且在扩展性方面优于没有约束的多层基线。
### Conclusion
我们预计，CTHA 将作为时间递归层次结构的一个具有原则性的扩展，将为多智能体协调的深入研究做出贡献，并建议智能体系统未来发展的有前景的方向。
## 11. `cs.CV` - 使用结合全球上下文视觉变换器的无人机和街景影像评估建筑热韧性 [PDF](https://arxiv.org/pdf/2601.11357), [HTML](https://arxiv.org/abs/2601.11357)
### Authors
Steffen Knoblauch,Ram Kumar Muthusamy,Hao Li,Iddy Chazua,Benedcto Adamu,Innocent Maholi,Alexander Zipf
### Background
气候变暖加剧了城市热暴露，尤其是在全球南方密集建设的城市中心。低成本建材和高热质量表面进一步加重了这种风险。然而，评估与热相关的建筑属性的可扩展方法仍非常稀缺。
### Innovation
本文提出了一种结合无人机(UAV)和街景(SV)图像的机器学习框架，通过耦合全局上下文视觉变换器(CGCViT)来学习与热相关的城市结构的表示。利用HotSat-1的热红外(TIR)测量，量化了建筑属性与热相关健康风险之间的关系。该双模态跨视角学习方法超越了最好的单模态模型，最高可达9.3%的性能提升，证明了UAV和SV影像提供了有价值的信息，有助于理解和改善城市建筑结构的热韧性。
### Conclusion
该框架在坦桑尼亚达累斯萨拉姆市的部署显示，使用机器学习可以识别并解决房屋级别的热暴露不平等，这通常与社会经济劣势和建筑材料相关。我们的结果强调了局部驱动的风险评估对于制定公平的气候适应策略的重要性。
## 12. `cs.CV` - SUG-Occ: 显式语义和不确定性引导的稀疏学习框架，用于实现实时3D占用率预测 [PDF](https://arxiv.org/pdf/2601.11396), [HTML](https://arxiv.org/abs/2601.11396)
### Authors
Hanlin Wu,Pengfei Lin,Ehsan Javanmardi,Nanren Bao,Bo Qian,Hao Si,Manabu Tsukada
### Background
随着自动驾驶向全面场景理解发展，3D语义占有预测已成为一种关键的感知任务，能够提供超越传统检测和分割范式的体素级别语义信息。然而，这种详细的表示形式在场景理解中会带来巨大的计算和内存开销，极大地阻碍了其实际实时部署。现有方法难以平衡精度与实时性。
### Innovation
提出了一种显式语义和不确定性引导的稀疏学习框架SUG-Occ，利用3D场景的固有稀疏性来减少冗余计算，同时保持几何和语义完整性。通过使用语义和不确定性先验，在视图变换中抑制自由空间的投影，采用显式的无符号距离编码增强几何一致性，构建了一个结构一致的稀疏3D表示。此外，设计了一个级联稀疏完成模块（通过超交叉稀疏卷积和生成上采样），实现高效的粗到细推理。最后，通过基于对象上下文表示（OCR）的掩码解码器收集稀疏特征的全局语义上下文，并通过轻量级查询-上下文交互精化体素级预测，避免昂贵的体积特征注意力操作。
### Conclusion
在SemanticKITTI基准上的广泛实验表明，提出的框架优于基线方法，准确率提高了7.34%，效率提高了57.8%。
## 13. `cs.CV` - PRISM-CAFO: 基于先验条件的远程传感基础设施分割与地图绘制以识别CAFOs [PDF](https://arxiv.org/pdf/2601.11451), [HTML](https://arxiv.org/abs/2601.11451)
### Authors
Oishee Bintey Hoque,Nibir Chandra Mandal,Kyle Luong,Amanda Wilson,Samarth Swarup,Madhav Marathe,Abhijin Adiga
### Background
大规模畜禽养殖场对人类健康和环境构成了显著的风险，同时这些养殖场也面临着由传染病和极端天气事件等带来的威胁。随着此类养殖场的持续增加，准确且可扩展的映射变得尤为重要。
### Innovation
我们提出了一种以基础设施为中心、可解释的管道方法，用于从航空和卫星图像中识别和表征集约化畜禽饲养操作（CAFOs）。该方法包括使用领域调整后的YOLOv8检测器检测候选基础设施，然后从这些框中生成SAM2掩码并通过特定组件的标准进行筛选；提取结构描述符并使用轻量级的空间交叉注意力分类器与深度视觉特征进行融合；输出CAFO类型预测和链接决策与可见基础设施的掩码级解释。我们的方法在全面评估中达到了最先进的性能，与最佳基线相比，Swin-B+PRISM-CAFO的性能提高了15%。
### Conclusion
我们的研究表明，PRISM-CAFO在不同美国地区的预测性能都很强，并且系统地分析了梯度-激活以量化领域先验的影响。
## 14. `cs.CV` - 使用卫星图像时间序列和具有时间意识的分割一切模型从稀疏注释进行湿地映射 [PDF](https://arxiv.org/pdf/2601.11400), [HTML](https://arxiv.org/abs/2601.11400)
### Authors
Shuai Yuan,Tianwu Lin,Shuang Chen,Yu Xia,Peng Qin,Xiangyu Liu,Xiaoqing Xu,Nan Xu,Hongsheng Zhang,Jie Wang,Peng Gong
### Background
准确的湿地映射对于生态系统监测至关重要，但密集的像素级注释非常昂贵，实际应用通常依赖稀疏的点标签，在这种情况下，现有的深度学习模型表现不佳。由于强烈的季节性和年际动态变化，单日期图像不足以解决这一问题，导致显著的映射错误。尽管基础模型如SAM在点提示下表现出良好的泛化能力，但它们是为静态图像设计的，无法建模时间信息，导致湿地的不连续掩码。
### Innovation
我们提出了一种WetSAM框架，它基于SAM并整合卫星图像时间系列，通过双分支设计从稀疏点监督进行湿地映射。时间提示分支通过时间关联者和动态时间聚合将SAM扩展以分离湿地特征与相位变化，空间分支使用时间受限的区域生长策略生成可靠的密集伪标签。双向一致性正则化联合优化两个分支。
### Conclusion
在八个全球地区的广泛实验中，每个地区的面积约为5,000平方公里，WetSAM大幅超越了最先进的方法，平均F1分数达到了85.58%，实现了高精度、结构上一致的湿地分割，同时显著减少了标注工作量，突显了其强大的泛化能力和可扩展、低成本、高分辨率湿地映射的潜力。
## 15. `cs.CV` - Think-Clip-Sample: Slow-Fast Frame Selection for Video Understanding [PDF](https://arxiv.org/pdf/2601.11359), [HTML](https://arxiv.org/abs/2601.11359)
### Authors
Wenhui Tan,Ruihua Song,Jiaze Li,Jianzhong Ju,Zhenbo Luo
### Background
近期多模态大型语言模型（MLLMs）在视频理解方面取得了显著进展。然而，它们在长时间视频上的表现仍然受限于计算能力的限制和不理想的帧选择。
### Innovation
本文提出了一个无需训练的框架Think-Clip-Sample（TCS），通过两个关键组件增强长时间视频的理解：(i) 多查询推理，生成多个查询来捕捉问题和视频的互补方面；(ii) 剪辑级别慢速-快速采样，适应性平衡密集的局部细节和稀疏的全局上下文。
### Conclusion
广泛实验表明，TCS在不同MLLMs上的一致性改进，提升最高可达6.9%的精度，并且能够以50%更低的推理时间成本达到可比的准确性，突显了TCS在长时间视频理解上的高效与有效。
## 16. `cs.CV` - Map2Thought：通过度量认知地图进行显式3D空间推理 [PDF](https://arxiv.org/pdf/2601.11442), [HTML](https://arxiv.org/abs/2601.11442)
### Authors
Xiangjun Gao,Zhensong Zhang,Dave Zhenyu Chen,Songcen Xu,Long Quan,Eduardo Pérez-Pellitero,Youngkyoon Jang
### Background
当前的3D视觉语言模型（3D VLMs）在隐式的空间推理方面存在不足，缺乏透明性和可解释性。文章为了解决这一问题，提出了Map2Thought框架，旨在提升3D空间推理的能力。
### Innovation
Map2Thought引入了Metric Cognitive Map（度量认知地图）和Cognitive Chain-of-Thought（认知推理链）两个核心模块。Metric Cognitive Map实现了一种统一的空间表示，结合了离散网格和连续的度量尺度表示；Cognitive Chain-of-Thought则通过确定性操作进行显式的几何推理，生成可解释的推理轨迹。
### Conclusion
实验结果表明，Map2Thought框架显著提升了3D理解的可解释性，即使在较少的监督数据条件下也能达到与全监督训练相似的表现。在不同训练集大小的基准测试中，Map2Thought分别超出最先进的方法5.3%、4.8%和4.0%，证明了其在小样本学习中的优越性。
## 17. `cs.CV` - PubMed-OCR: PMC Open Access OCR Annotations [PDF](https://arxiv.org/pdf/2601.11425), [HTML](https://arxiv.org/abs/2601.11425)
### Authors
Hunter Heidenreich,Yosheb Getachew,Olivia Dinica,Ben Elliott
### Background
该研究基于PubMed Central (PMC) 公开访问PDF构建了一个针对光学字符识别(OCR)的科学文章语料库，其中每个页面的图像都经过Google Cloud Vision标注，并以紧凑的JSON模式发布，包含单词、行和段落级别的边界框。语料库包含了209,500篇文章，150万页，约13亿个词，支持基于布局的建模、坐标引导的问答和依赖OCR的管道评估。
### Innovation
该语料库通过使用Google Cloud Vision进行页面图像标注，并以紧凑的JSON模式发布，支持单词、行和段落级别的边界框，这为下游研究提供了方便，有助于推进OCR依赖管道的评估和基于布局的建模研究。
### Conclusion
作者分析了语料库的特征（例如期刊覆盖范围和检测到的布局功能），并讨论了其局限性，包括对单一OCR引擎的依赖和启发式行重建。同时，作者提供了数据和模式，以促进后续研究，并邀请进一步的扩展研究。
## 18. `cs.CV` - Heterogeneous Uncertainty-Guided Composed Image Retrieval with Fine-Grained Probabilistic Learning [PDF](https://arxiv.org/pdf/2601.11393), [HTML](https://arxiv.org/abs/2601.11393)
### Authors
Haomiao Tang,Jinpeng Wang,Minyi Zhao,Guanghao Meng,Ruisheng Luo,Long Chen,Shu-Tao Xia
### Background
Composed Image Retrieval (CIR)能够通过结合参考图像和修改文本进行图像搜索。然而，CIR三元组中的固有噪声会导致固有的不确定性，威胁模型的鲁棒性。现有的概率学习方法虽然在这方面有一些进展，但在处理CIR时存在不足，原因在于其实例级别的整体建模和查询与目标的同质化处理。
### Innovation
该论文提出了Heterogeneous Uncertainty-Guided (HUG)框架，以解决上述问题。HUG采用细粒度的概率学习框架，使用高斯嵌入表示查询和目标，捕捉详细概念和不确定性，进行了异质不确定性估计算法的定制。提出了一种证明动态加权机制来计算全面的查询不确定性，设计了不确定性引导目标，包括查询-目标整体对比和细粒度对比，采用全面的负样本策略来有效增强区分学习。
### Conclusion
在基准数据集上的实验结果显示HUG方法在性能上超越了现有的最先进的基线，深入的技术分析证实了其技术贡献的有效性。
## 19. `cs.CV` - 拓扑保证的图像分割：强制连接性、涵数和宽度约束 [PDF](https://arxiv.org/pdf/2601.11409), [HTML](https://arxiv.org/abs/2601.11409)
### Authors
Wenxiao Li,Xue-Cheng Tai,Jun Liu
### Background
现有的研究表明，拓扑先验在图像分割中起到关键作用，特别是保持重要结构的连通性和涵数等特性。然而，传统的拓扑结构定义缺乏宽度信息，限制了持久同调等方法全面满足实际分割需求。因此，需要一种新的数学框架，能够明确整合宽度信息来描述拓扑结构。
### Innovation
本文提出了一个新的数学框架，将宽度信息直接整合进拓扑结构的描述中。该方法结合了持久同调和偏微分方程的平滑概念，修改上层集的局部极值，从而使得生成的拓扑结构能够内在地包含宽度属性。此外，这种方法被融入到变分图像分割模型中，并设计出能够捕捉到所需拓扑和宽度属性的神经网络。
### Conclusion
通过变分约束相关的拓扑能量，该方法成功地保持了重要的拓扑不变量（如连通性和涵数计数）的同时，确保分割的结构保留关键的宽度属性（如线条的厚度和长度）。数值实验表明，该方法在保持拓扑保真度的同时，也明确地嵌入了宽度特性到分割后的图像结构中。
## 20. `cs.CV` - SME-YOLO: PCB表面微小缺陷的实时检测器 [PDF](https://arxiv.org/pdf/2601.11402), [HTML](https://arxiv.org/abs/2601.11402)
### Authors
Meng Han
### Background
印刷电路板（PCB）表面的缺陷直接影响产品的可靠性和安全性。然而，精确检测这些缺陷极具挑战，因为PCB缺陷通常具有极小的尺寸、高纹理相似性和不均匀的尺度分布。
### Innovation
本文提出了一种基于YOLOv11n的新型框架，命名为SME-YOLO（Small-target Multi-scale Enhanced YOLO）。通过引入归一化 Wasserstein 距离损失（NWDLoss）来减少交并比（IoU）对于小目标位置偏移的敏感性。同时，将原始上采样模块替换为高效的上采样卷积块（EUCB），利用多尺度卷积逐步恢复空间分辨率并增强细节点和纹理细节的保留。此外，提出了一种多尺度聚焦注意力（MSFA）模块，专为PCB缺陷的空间分布设计，以适应性的加强重要尺度区间内的感知，实现局部细粒度特征和全局上下文信息的有效融合。
### Conclusion
SME-YOLO在PKU-PCB数据集上实验结果表明其达到了最先进的性能。与基线YOLOv11n相比，SME-YOLO在mAP上提高了2.2%，精确度提高了4%，验证了该方法的有效性。
