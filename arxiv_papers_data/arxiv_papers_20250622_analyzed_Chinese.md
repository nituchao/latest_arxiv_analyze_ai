# 1. `cs.AI` - CALM: 基于情境模态性的类比逻辑 [PDF](https://arxiv.org/pdf/2506.14936), [HTML](https://arxiv.org/abs/2506.14936)
## Authors
Maxwell J. Jacobson,Corey J. Maley,Yexiang Xue
## Background
经典二值逻辑系统无法捕捉人类决策的微妙之处。此外，人类需要在多模态环境中进行接地，这可能是临时的、僵硬的和脆弱的。神经网络擅长从多模态数据中提取丰富的上下文信息，但缺乏用于推理的可解释结构。
## Innovation
CALM 结合了符号推理与神经生成，使得系统能够基于真实世界多模态数据进行情境敏感的决策。它旨在弥合逻辑与神经感知之间的差距，创建一种可以在多模态输入上进行推理的类比逻辑。每个谓词通过领域树表示，并在实体的上下文确定过程中逐步细化其类比真值。通过神经网络预测迭代细化过程，并通过符号推理模块进行过滤以确保满足约束条件。实验显示，CALM 在填充任务中的准确率为 92.2%，超过传统的逻辑（86.3%）和大语言模型（LLM）基准（59.4%），并展示了符合逻辑约束和细腻人类偏好的空间热图生成能力。
## Conclusion
CALM 展示了在其多模态环境中进行逻辑推理并同时与偏好对齐的潜力。它为需要逻辑精确性和解释性的逻辑以及神经网络多模态信息处理的下一代 AI 系统奠定了基础。
# 2. `cs.AI` - MEAL: 一个用于持续多人增强学习的基准测试 [PDF](https://arxiv.org/pdf/2506.14990), [HTML](https://arxiv.org/abs/2506.14990)
## Authors
Tristan Tomilin,Luka van den Boogaard,Samuel Garcin,Bram Grooten,Meng Fang,Mykola Pechenizkiy
## Background
强化学习（RL）算法的发展和分析中，基准测试扮演着至关重要的角色，环境可用性对研究有着重要影响。特别是在合作多智能体持续学习（CL）方面，目前的研究还相对较少。现有的一些CL基准测试在CPU上运行环境，导致了计算瓶颈和任务序列长度的限制。
## Innovation
MEAL是首个针对持续多智能体强化学习（CMARL）设计的基准测试，利用JAX实现GPU加速，能够在几小时内对标准台式机PC上100个任务的序列进行持续学习。该基准测试揭示了现有方法在简单环境和复杂环境中的表现差异，特别是它们无法在需要持续协作和适应的复杂环境中形成良好表现。
## Conclusion
通过耗时较少的情况下完成较大任务序列的持续学习测试，MEAL帮助研究者识别出CMARL所必需的关键架构和算法特征。
# 3. `cs.AI` - 截断近端策略优化 [PDF](https://arxiv.org/pdf/2506.15050), [HTML](https://arxiv.org/abs/2506.15050)
## Authors
Tiantian Fan,Lingjun Liu,Yu Yue,Jiaze Chen,Chengyi Wang,Qiying Yu,Chi Zhang,Zhiqi Lin,Ruofei Zhu,Yufeng Yuan,Xiaochen Zuo,Bole Ma,Mofan Zhang,Gaohong Liu,Ru Zhang,Haotian Zhou,Cong Xie,Ruidong Zhu,Zhi Zhang,Xin Liu,Mingxuan Wang,Lin Yan,Yonghui Wu
## Background
近年来，在测试时间尺度上，大型语言模型（LLMs）通过生成长的推理链条（CoT）在科学和专业任务上表现出色，推理能力得到了极大的提升。尽管传统的近端策略优化（PPO）通过试错学习方法使得模型能够进行学习，但由于其固有的在线策略性质和响应长度的增加，PPO的训练耗时往往较长。特别是在长时间生成过程中，这种同步的完整流程会导致硬件资源利用率低下，常在等待完整回放期间处于闲置状态.
## Innovation
本文提出了截断近端策略优化（T-PPO），这是一种对PPO的创新扩展，通过简化策略更新和长度受限的响应生成来提高训练效率。T-PPO通过提出扩展的一般优势估计（EGAE）来估算不完整响应的优势，并保持策略学习的完整性。还设定了一个计算高效的机制，实现了策略和价值模型的独立优化，通过有选择地过滤提示和截断标记，减少了冗余计算并加速了训练过程，而不会牺牲收敛性能。实验证明T-PPO在AIME 2024竞赛中，使用一个32B基础模型的情况下，将推理LLM的训练效率提高了2.5倍，并且优于现有竞争对手.
## Conclusion
实验结果表明，T-PPO能够显著提高推理LLM的训练效率，并且比现有竞争对手表现更优。
# 4. `cs.AI` - HeurAgenix: 利用大语言模型解决复杂组合优化挑战 [PDF](https://arxiv.org/pdf/2506.15196), [HTML](https://arxiv.org/abs/2506.15196)
## Authors
Xianliang Yang,Ling Zhang,Haolong Qian,Lei Song,Jiang Bian
## Background
手工设计的启发式算法在解决组合优化问题方面起着至关重要的作用，但传统设计依赖于手动专业知识，难以在不同的实例上进行泛化。因此，需要一种新的方法来自动进化和选择启发式算法，以应对组合优化的复杂性。
## Innovation
HeurAgenix 通过两个阶段的超启发式框架利用大语言模型实现这一目标。在启发式进化阶段，它通过LLM来比较种子启发式解决方案与高质解决方案并通过提取可重用的进化策略来进化启发式算法。在问题求解阶段，它根据LLM的经验能力动态选择最有可能成功的启发式算法。此外，HeurAgenix 还采用双重奖励机制来微调轻量级选择器，以在嘈杂的注释下做出鲁棒的选择。
## Conclusion
HeurAgenix 不仅在多种基准测试上超过了现有的基于LLM的超启发式方法，而且还与专用求解器的性能相当或更优。
# 5. `cs.AI` - 使用多智能体强化学习进行自主多卫星地球观测：一个现实案例研究 [PDF](https://arxiv.org/pdf/2506.15207), [HTML](https://arxiv.org/abs/2506.15207)
## Authors
Mohamad A. Hady,Siyi Hu,Mahardhika Pratama,Jimmy Cao,Ryszard Kowalczyk
## Background
低地球轨道（LEO）卫星的数量呈指数增长，这极大地改变了地球观测（EO）任务，克服了诸如气候变化监测和灾害管理等领域的挑战。然而，多卫星系统中的自主协调仍是一个基本难题。传统的优化方法难以应对动态EO任务中的实时决策需求，因此需要利用强化学习（RL）和多智能体强化学习（MARL）来解决这个问题。传统方法难以应对动态EO任务中的实时决策需求，需要采用强化学习（RL）和多智能体强化学习（MARL）来应对这些挑战。本研究通过模拟单卫星操作并扩展到多卫星星座，运用MARL框架研究基于RL的自主EO任务规划。研究重点包括能源和数据存储限制、卫星观测中的不确定性以及在部分可观测的情况下分散协调的复杂性。利用接近现实的卫星仿真环境，评估了最新的MARL算法（包括PPO、IPPO、MAPPO和HAPPO）的训练稳定性和性能。结果表明，MARL在多卫星协调中可以平衡成像和资源管理，同时解决非平稳性和奖励相互依赖问题。研究获得了关于自主卫星操作的见解，为分zentralized EO任务中的策略学习提供了实用指南。
## Innovation
研究利用强化学习（RL）和多智能体强化学习（MARL）框架，提出了一种新的自主EO任务规划方法。通过一个近现实的卫星仿真环境，评估了最新的MARL算法的性能，针对多卫星协调中的非平稳性和奖励相互依赖问题提出了有效的解决方案。
## Conclusion
研究结果表明，MARL能够在多卫星协调中有效平衡成像和资源管理，提供了一种实用的方法来解决非平稳性和奖励相互依赖问题。这些发现为促进自主卫星操作提供了理论基础，并为分zentralized EO任务中的政策学习提供了实用准则。
