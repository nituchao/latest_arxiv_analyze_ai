# 20260125
[![Subscribe_Visitors](https://visitor-badge.laobi.icu/badge?page_id=nituchao.latest_arxiv_analyze_ai_rss)](https://github.com/nituchao/latest_arxiv_analyze_ai)

## 1. `cs.AI` - 知识图谱网络上的逻辑编程及其在医疗领域中的应用 [PDF](https://arxiv.org/pdf/2601.15347), [HTML](https://arxiv.org/abs/2601.15347)
### Authors
Chuanqing Wang,Zhenmin Zhao,Shanshan Du,Chaoqun Fei,Songmao Zhang,Ruqian Lu
### Background
知识图谱的发展促进了其在多个领域（如医学和健康领域）的应用。然而，有一些主要的信息处理技术在知识图谱中的应用还存在滞后，特别是在逻辑推理、高级人工智能技术、专用编程语言、现代概率与统计理论等方面的应用不足。此外，知识图谱之间的合作与竞争技术也尚未得到充分的研究关注。
### Innovation
本文发展了一种系统理论、技术和应用的概念‘知识图谱网络’及其在医疗和健康领域的应用。研究涵盖了不同条件下的定义、开发、推理、计算和应用，包括模糊性、不确定性、多模式、向量化、分布式、联邦等情况。每个方面都提供了实际数据的例子和实验结果。
### Conclusion
本研究提供了创新性的结论。
## 2. `cs.AI` - GeMM-GAN: 基于组织病理图像和临床描述的多模态生成模型用于基因表达谱生成 [PDF](https://arxiv.org/pdf/2601.15392), [HTML](https://arxiv.org/abs/2601.15392)
### Authors
Francesca Pia Panaccione,Carlo Sgaravatti,Pietro Pinoli
### Background
生物医学研究越来越依赖于整合多元数据模态，包括基因表达谱、医学图像和临床元数据。尽管医学图像和临床元数据在临床实践中常规采集，但基因表达数据由于严格的隐私法规和昂贵的实验室实验，限制了其广泛研究利用。为解决这些限制，我们提出了GeMM-GAN，这是一种以组织病理学组织切片和临床元数据为条件的生成对抗网络，用于合成真实的基因表达谱。GeMM-GAN结合了Transformer编码器处理图像块，并通过图像块与文本标记之间的交叉注意力机制生成条件向量，以此指导生成模型生成生物上连贯的基因表达谱。
### Innovation
GeMM-GAN是一种创新的多模态生成模型，其通过结合Transformer编码器和交叉注意力机制，以组织病理学图像和临床元数据为条件生成基因表达谱。该模型在TCGA数据集上的评估结果表明，与标准生成模型相比，GeMM-GAN生成的基因表达谱更真实且具有功能性意义，疾病类型预测准确性提高了超过11%。
### Conclusion
我们的研究成果表明，GeMM-GAN在合成基因表达谱方面具有显著优势，克服了传统生成模型在这一领域的不足，为生物医学研究提供了新的解决方案。
## 3. `cs.AI` - 超越提示：通过逻辑空间集成（LOGIC）实现高效稳健的语音大语言模型上下文偏倚 [PDF](https://arxiv.org/pdf/2601.15397), [HTML](https://arxiv.org/abs/2601.15397)
### Authors
Peidong Wang
### Background
新实体的快速涌现——由文化变革、演变的趋势和个人化用户数据驱动——对现有的语音大型语言模型（Speech LLMs）构成了重大挑战。虽然这些模型在通用对话任务中表现出色，但由于其静态训练知识的限制，它们难以识别特定领域的术语，如联系人姓名、播放列表或技术术语。现有解决方案主要依赖于提示，但这种方法在扩展性方面存在局限性，当实体列表增加时，容易遇到上下文窗口限制、推理延迟增加以及“中间丢失”的现象。一种替代方法是生成式错误修正（GEC），但这种方法常常导致过度修正，引入未说话实体的幻觉。
### Innovation
本文提出了一种高效的且稳健的框架LOGIC（Logit-Space Integration for Contextual Biasing），在解码层直接运行。与提示不同，LOGIC将上下文注入与输入处理脱钩，确保常数时间复杂度与提示长度无关。使用Phi-4-MM模型在11个不同语言环境中进行的广泛实验表明，LOGIC实现了9%的实体错误率相对减少，同时只在误报率上增加了0.30%。
### Conclusion
LOGIC框架在语音大语言模型中直接操作于解码层，确保了常数时间复杂度，并通过逻辑空间集成有效缓解了上下文偏倚问题，显著减少实体错误率，具有较好的扩展性和稳定性。
## 4. `cs.AI` - 通过代理变量揭示基于LLM的急诊分流中的潜在偏差 [PDF](https://arxiv.org/pdf/2601.15306), [HTML](https://arxiv.org/abs/2601.15306)
### Authors
Ethan Zhang
### Background
近年来，大型语言模型（LLMs）的进步使其能够整合到临床决策中，但是这些模型在处理患者时依然存在隐藏的偏见，这些偏见可能存在于种族、社会、经济和临床背景不同的患者中。本研究重点关注LLM在急诊分流中的应用，通过分析32个患者级别的代理变量及其配对的正负面描述符，评估这些变量对急诊分流的影响。研究指出，这些模型在处理输入时会表现出偏向行为，且这种偏向行为并不取决于输入中描述信息的正负面影响。
### Innovation
本研究通过使用代理变量量化了LLE在急诊分流中的潜在偏见，并发现LLE在输入具体词语时会调整对患者严重性的感知，这表明AI系统在受到非因果、噪声信息的训练时仍然存在缺陷，不能可靠地反映患者的真实紧急程度。这一研究提供了更深入理解LLE偏见形成机制的依据，促进了AI技术在临床应用中的优化。
### Conclusion
本研究揭示了在急诊分流中使用LLM时存在通过代理变量介导的歧视行为，以及LLE在面对特定输入时系统性地修改患者严重性的感知这一现象。这表明AI系统在训练过程中未能有效过滤出可靠反映患者真正紧急程度的影响因素。因此，需要更多努力来确保在临床环境中安全、负责任地部署AI技术。
## 5. `cs.AI` - The Paradigm Shift: A Comprehensive Survey on Large Vision Language Models for Multimodal Fake News Detection [PDF](https://arxiv.org/pdf/2601.15316), [HTML](https://arxiv.org/abs/2601.15316)
### Authors
Wei Ai,Yilong Tan,Yuntao Shou,Tao Meng,Haowen Chen,Zhixiong He,Keqin Li
### Background
近年来，大型视觉语言模型（LVLMs）的快速发展推动了多模态假新闻检测（MFND）范式的转变，从传统的特征工程方法转向统一的端到端多模态推理框架。早期方法主要依赖浅层融合技术来捕捉文本和图像之间的相关性，但难以进行高层次语义理解和复杂的跨模态交互。随着LVLMs的出现，这一格局发生了根本性变化，使得能够协同建模视觉和语言，从而增强对利用文本叙述和视觉内容的虚假信息的检测能力。
### Innovation
本文提供了一篇全面的关于通过LVLMs审视MFND的回顾性论文。通过历史视角，映射从传统的多模态检测管道到基于基础模型的范式演变。本文还建立了一个结构化的分类，涵盖了模型架构、数据集和性能基准。此外，分析了剩余的技术挑战，包括可解释性、时间推理和领域泛化。最后，概述了未来研究方向，以指导这一范式转变的下一阶段。到我们所知，这是首次系统记录和分析LVLMs在打击多模态假新闻中的变革性作用的综述。
### Conclusion
我们已经提供了一个全面的关于通过LVLMs审视MFND的回顾性陈述。本文首次系统记录和分析了LVLMs在打击多模态假新闻中的变革性作用，并指出了研究方向以指导这一范式的未来演变。
## 6. `cs.AI` - 可再现的金融代理: 工具使用LLM代理的确定性-忠实性保证框架 [PDF](https://arxiv.org/pdf/2601.15322), [HTML](https://arxiv.org/abs/2601.15322)
### Authors
Raffi Khatchadourian
### Background
LLM代理在应对监管审计重演时表现不佳，特别是在被要求重复处理被标记的交易决策时，大多数部署都无法获得一致的结果。研究者为此引入了一种框架——确定性-忠实性保证框架（DFAH）来衡量工具使用代理在金融服务中的轨迹确定性和证据条件下的忠实性。
### Innovation
研究提出了一种名为DFAH的新框架，用于评估工具使用代理在金融服务中的确定性和忠实性。该研究全面评估了74种配置下的多种规模模型的表现，发现较大规模的模型需要更多的验证样本才能达到与较小模型相同的统计可靠性。此外，研究揭示了确定性和忠实性之间存在正相关关系，即产生一致输出的模型也更倾向于证据对齐。
### Conclusion
在DFAH的评估条件下，使用模式优先架构的一级模型实现了符合审计回放要求的确定性水平。该研究提供了三个金融基准测试案例，并开放了压力测试框架，以验证和评估工具使用LLM代理的表现。
## 7. `cs.AI` - Aeon: 高性能神经符号记忆管理用于长时程LLM代理 [PDF](https://arxiv.org/pdf/2601.15311), [HTML](https://arxiv.org/abs/2601.15311)
### Authors
Mustafa Arslan
### Background
大型语言模型（LLMs）受到自我注意的二次计算成本和‘中间迷失’现象的限制，后者会导致随着上下文窗口的扩展，推理能力下降。现有的解决方案主要依赖于平坦的检索架构（Flat RAG），此类架构通过向量数据库处理记忆，但未能捕捉到长期交互中的层次结构和时间顺序，导致检索到的孤立事实缺乏情节连贯性。
### Innovation
我们提出了Aeon，一种神经符号认知操作系统，重新定义了记忆不仅是一个静态存储，而且是一个管理的OS资源。Aeon将记忆结构化为一个Memory Palace（通过Atlas实现了小世界图导航和B+树风格的磁盘本地性相结合的空间索引，用于最小化读取放大）和一个Trace（一种神经符号的 episodic 图）。我们引入了语义旁路缓存机制（SLB），这是一种利用对话局部性的预测性缓存机制，实现了亚毫秒级别的检索延迟。实验证明Aeon在对话工作负载中实现了亚毫秒级别的检索延迟，并通过零拷贝的C++/Python桥梁确保状态一致性，从而使自治代理能够拥有持久化和结构化的记忆。
### Conclusion
Aeon 通过这些创新性手段提供了高性能的神经符号内存管理，为长时程LLM代理提供了有效保障，使得这些代理能够保持状态的一致性，持久地拥有结构化记忆，从而增强其自主性。
## 8. `cs.AI` - Gated Sparse Attention: 结合计算效率与训练稳定性以提升长上下文语言模型 [PDF](https://arxiv.org/pdf/2601.15305), [HTML](https://arxiv.org/abs/2601.15305)
### Authors
Alfred Shen,Aaron Shen
### Background
长上下文语言模型中的注意力机制计算负担促使研究出两种主要独立的改进方式：稀疏注意机制和门控注意变体。前者通过关注选择的标记来降低复杂性，后者在缓解注意力陷阱现象的同时提高训练稳定性。
### Innovation
提出了门控稀疏注意（GSA）架构，结合稀疏注意机制的好处，并引入了门控闪电索引器、自适应稀疏控制器和双重门控机制。建立了该方法的理论基础，包括复杂性分析、表达能力结果和收敛保障。在1.7B参数、400B标记量训练的模型中，GSA实现了与稀疏注意机制同等的效率（128K上下文时12-16倍加速），同时达到门控注意机制带来的质量改进：困惑度从6.03降至5.70，RULER在128K上下文时几乎翻倍，注意力转移到首个标记大幅减少，且训练稳定性显著提高，损失峰值降低了98%。
### Conclusion
GSA提供了高效性和训练稳定性的双重优势，为长上下文语言模型提供了新的架构选择。
## 9. `cs.AI` - DeepSurvey-Bench: 评估自动生成科学问卷的学术价值 [PDF](https://arxiv.org/pdf/2601.15307), [HTML](https://arxiv.org/abs/2601.15307)
### Authors
Guo-Biao Zhang,Ding-Yuan Liu,Da-Yi Wu,Tian Lan,Heyan Huang,Zhijing Wu,Xian-Ling Mao
### Background
自动科学调查生成技术的迅速发展使得建立全面基准以评估生成调查的质量变得尤为重要。现有基准依赖存在缺陷的标准，如引用次数和结构连贯性，选择人类撰写的调查作为真实的调查数据集，然后使用表面度量如结构质量和参考相关性来评估生成的调查。现有基准存在两个关键问题：（1）真实的调查数据集不可靠，因为缺乏学术维度的标注；（2）评估指标仅关注调查的表面质量，如逻辑连贯性。这些问题导致现有基准无法评估生成调查的深入‘学术价值’，例如核心研究目标和对不同研究的批判性分析。
### Innovation
我们提出了DeepSurvey-Bench，一种新的基准，旨在全面评估生成调查的学术价值。我们的基准提出了一套全面的学术价值评估标准，涵盖信息价值、学术交流价值和研究指导价值三个维度。基于这一标准，我们构建了一个带有学术价值标注的可靠数据集，并评估生成调查的深刻学术价值。广泛的实验结果显示，我们的基准在评估生成调查的学术价值方面与人类表现高度一致。
### Conclusion
我们的基准可以有效解决当前基准存在的问题，为自动生成的科学调查提供了一个可靠的方法来评估他们的深入学术价值。这将有助于提高生成调查的质量，并推进自动科学调查这一领域的研究和发展。
## 10. `cs.AI` - Prometheus Mind: 重塑冻结语言模型的记忆 [PDF](https://arxiv.org/pdf/2601.15324), [HTML](https://arxiv.org/abs/2601.15324)
### Authors
Mark Wind
### Background
将预训练的语言模型添加记忆通常需要进行架构更改或权重修改。该论文介绍了一种名为Prometheus Mind的技术，能够在不改变架构或调整权重的情况下，通过11个模块化的适配器（530MB，约占7％的额外开销）将记忆添加到冻结的Qwen3-4B模型中，并且可以通过移除这些适配器完全逆向操作。
### Innovation
该创新在于开发了Contrastive Direction Discovery（CDD）方法，能够通过最小数据对找到语义方向；在训练上采用阶段训练方式；在注入方面，使用未训练的编码器成功地提供映射关系；在隐藏状态坍缩问题上，通过训练投影来恢复区分度。该技术能够在某些特定情况下实现高准确率的记忆检索，但在非正式输入如省略句、填充词或隐含主语的情况下表现较差。
### Conclusion
在PrometheusExtract-132（132个样本）上的表现上，系统在干净输入（n=54）上实现了94.4%的检索精度（置信区间：84.9%到98.1%），但在非正式输入（n=36）中准确率下降到19.4%。最突出的问题在于关系分类的准确率相对较低（47.3%），这也影响了整体提取的准确性。研究的主要挑战和改进包括稀疏特征的映射、阶段训练、未训练编码器的表现以及克服变压器的对称性问题来恢复词汇区分度。
## 11. `cs.CV` - FUGC：评估半监督学习方法用于宫颈分割的标准基准 [PDF](https://arxiv.org/pdf/2601.15572), [HTML](https://arxiv.org/abs/2601.15572)
### Authors
Jieyun Bai,Yitong Tang,Zihao Zhou,Mahdi Islam,Musarrat Tabassum,Enrique Almar-Munoz,Hongyu Liu,Hui Meng,Nianjiang Lv,Bo Deng,Yu Chen,Zilun Peng,Yusong Xiao,Li Xiao,Nam-Khanh Tran,Dac-Phu Phan-Le,Hai-Dang Nguyen,Xiao Liu,Jiale Hu,Mingxu Huang,Jitao Liang,Chaolu Feng,Xuezhi Zhang,Lyuyang Tong,Bo Du,Ha-Hieu Pham,Thanh-Huy Nguyen,Min Xu,Juntao Jiang,Jiangning Zhang,Yong Liu,Md. Kamrul Hasan,Jie Gan,Zhuonan Liang,Weidong Cai,Yuxin Huang,Gongning Luo,Mohammad Yaqub,Karim Lekadir
### Background
准确的TVS下宫颈结构分割对评估自发早产风险至关重要，然而标注数据的稀缺限制了监督学习方法的性能。
### Innovation
首次提出了Fetal Ultrasound Grand Challenge (FUGC)，作为ISBI 2025的第一个半监督学习的宫颈分割基准。FUGC提供了890张TVS图像，包括500张训练图像、90张验证图像和300张测试图像。挑战吸引了10支队伍的82名参与者提交了创新解决方案，展示了在有限标注数据的情况下半监督方法的有效性。
### Conclusion
FUGC为宫颈分割设立了标准化的基准，证明了半监督方法的有效性，并为AI辅助临床自发早产风险评估提供了基础。
## 12. `cs.CV` - PF-D2M：一种无需姿态的扩散模型用于通用舞蹈音乐生成 [PDF](https://arxiv.org/pdf/2601.15872), [HTML](https://arxiv.org/abs/2601.15872)
### Authors
Jaekwon Im,Natalia Polouliakh,Taketo Akama
### Background
舞蹈与音乐的同步生成旨在生成与舞蹈动作相匹配的音乐。现有方法通常依赖于单个舞者身体动作特征的提取，且受限于有限的舞蹈音乐数据集，这限制了其在多舞者及非人类舞者的现实场景中的性能和应用。
### Innovation
本文提出了一种名为PF-D2M的扩散基础的通用舞蹈音乐生成模型，该模型结合了从舞蹈视频中提取的视觉特征。PF-D2M采用逐步训练策略有效解决了数据稀缺和泛化难题。实验结果表明，PF-D2M在舞蹈音乐对齐和音乐质量方面实现了最先进的性能。
### Conclusion
PF-D2M在舞蹈音乐生成方面表现出色，提升了多舞者场景和非人类舞者的通用性，并通过逐步训练克服了数据不足的问题。
## 13. `cs.CV` - DextER: 语言驱动的带体体现推理的灵巧抓取生成 [PDF](https://arxiv.org/pdf/2601.16046), [HTML](https://arxiv.org/abs/2601.16046)
### Authors
Junha Lee,Eunha Park,Minsu Cho
### Background
语言驱动的灵巧抓取生成需要理解任务语义、3D几何形状以及复杂的手和物体之间的相互作用。现有的视觉-语言模型虽已应用于此问题，但这些方法直接将观察结果映射为抓取参数，缺乏对物理交互的中间推理过程。
### Innovation
介绍了一种基于接触的体体现推理方法，用于多指操作的灵巧抓取生成。DextER 自回归生成体体现接触令牌，指明哪只手指在物体表面何处接触，随后生成抓取令牌编码手部配置。
### Conclusion
在DexGYS数据集上，DextER 的成功率为67.14%，优于最先进的方法3.83%，意图对齐提升96.4%。还展示了部分接触指定下的可控生成，提供精细的抓取合成控制。
## 14. `cs.CV` - 基于机器视觉的初步皮肤病变评估方法 [PDF](https://arxiv.org/pdf/2601.15539), [HTML](https://arxiv.org/abs/2601.15539)
### Authors
Ali Khreis,Ro'Yah Radaideh,Quinn McGill
### Background
及时检测恶性皮肤病变是提高患有侵袭性、转移性皮肤癌症患者预后的关键。本研究评估了一种结合临床验证的皮肤镜下ABCD规则（分析非对称性、边界、颜色和皮肤镜特征）与机器学习分类的综合系统，用于初步皮肤病变评估。
### Innovation
该系统使用了一种自动化、基于规则的流程来为每个病变计算总皮肤镜评分（TDS）。该研究将基于手动构建的方法与各种机器学习解决方案（包括传统分类器以及深度学习模型）进行了对比。实验结果显示，虽然基于规则的系统具有临床可解释性，但在将复杂形态简化为五个数值特征时存在性能瓶颈。通过从零开始训练的自定义三层卷积神经网络（CNN）在中值滤波图像上取得了78.5%的准确率和86.5%的召回率，表明直接像素级学习能够捕捉到超越手动构建特征的诊断模式。
### Conclusion
该结果表明直接像素级学习能够捕捉到更深层次的诊断特征，而专门构建的轻量级架构在小而特定的医学数据集上可以优于大型预训练模型。
## 15. `cs.CV` - 通过深度隐式表示融合口内扫描和CBCT数据实现高保真3D牙齿重建 [PDF](https://arxiv.org/pdf/2601.15358), [HTML](https://arxiv.org/abs/2601.15358)
### Authors
Yi Zhu,Razmig Kechichian,Raphaël Richert,Satoshi Ikehata,Sébastien Valette
### Background
高保真3D牙齿模型对于数字牙科至关重要，但必须既捕捉到详细的冠部，又包括完整的根部。临床上的成像技术有限：锥形束计算机断层扫描（CBCT）能够捕捉到根部，但冠部的分辨率低且噪声较大，而口内扫描仪（IOS）则可以提供高保真冠部但不包含根部信息。简单的数据融合方法会生成不自然的接缝和伪影。
### Innovation
本文提出了一种全新的全自动融合管道，利用深度隐式表示将CBCT和IOS数据融合。该方法首先分割和稳健地注册牙齿实例，然后结合IOS冠部和CBCT根部生成混合代理网格。核心在于使用这个噪声代理来引导特定类别的DeepSDF网络，该优化过程将输入投影到理想的牙齿形状的已学习流形上，生成无缝、完全防水且在解剖学上连贯的模型。
### Conclusion
定性和定量评估表明，本方法独特地保留了IOS提供的高保真冠部和CBCT提供的患者特定根部形态，克服了各自的模态限制和简单的拼接方法的不足。
## 16. `cs.CV` - 从ImageNet转换学习实现基于MEG的想象言语解码 [PDF](https://arxiv.org/pdf/2601.15909), [HTML](https://arxiv.org/abs/2601.15909)
### Authors
Soufiane Jhilal,Stéphanie Martin,Anne-Lise Giraud
### Background
非侵入式解码想象中的言语仍然具有挑战性，主要是因为微弱且分布式的信号以及有限的带标签数据。该论文介绍了一种图像基础的方法，即将脑电信号（如脑磁信号，MEG）转换为与预训练的视觉模型兼容的时间-频率表示。
### Innovation
将MEG信号转化为适用于预训练视觉模型的时频表示，并通过可学习的传感器空间卷积将MEG数据投影到三个空间尺度混合，生成可用于预训练图像网络结构的图像型输入，从而提高了解码准确性。
### Conclusion
预训练视觉模型应用于基于图像的MEG表示，可以有效捕捉想象言语的非侵入性神经信号结构。通过跨受试者评估确认，预训练模型能够捕获共享的神经表示，并通过时间分析定位到想象锁定间隔中可区分的信息。
## 17. `cs.CV` - GeMM-GAN: 一种基于组织病理图像和临床描述的多模态生成模型用于基因表达谱生成 [PDF](https://arxiv.org/pdf/2601.15392), [HTML](https://arxiv.org/abs/2601.15392)
### Authors
Francesca Pia Panaccione,Carlo Sgaravatti,Pietro Pinoli
### Background
生物医学研究越来越多地依赖于整合多种数据模态，包括基因表达谱、医学影像和临床元数据。医学影像和临床元数据已在临床实践中常规收集，而基因表达数据由于严格的隐私规定和昂贵的实验室实验而难以广泛用于研究。为了克服这些限制，本文提出了一种名为GeMM-GAN的新颖生成对抗网络，该网络以组织病理图像和临床元数据为条件生成真实的基因表达谱。GeMM-GAN结合了Transformer编码器处理图像片段，并采用了片段与文本标记之间的交叉注意力机制，生成引导生成模型以产生生物上连贯的基因表达谱。
### Innovation
本文提出的GeMM-GAN是一种基于组织病理图像和临床元数据条件的多模态生成模型，旨在生成真实的基因表达谱。它使用Transformer编码器处理图像片段，并通过片段与文本标记之间的交叉注意力机制生成指导性向量，以引导生成模型生成生物上连贯的基因表达谱。通过TCGA数据集的评估显示，相比于当前最先进的生成模型，该框架生成了更真实且功能上更有意义的基因表达谱，下游疾病类型预测准确率提高了11%以上。
### Conclusion
我们的工作证明了GeMM-GAN的有效性，并表明该框架能够显著提高基因表达谱的生成质量，提供了更真实的基因表达谱，使得基于基因表达谱的生物医学研究更加接近实际应用。
## 18. `cs.CV` - 不确定性指导下的暗场X射线成像生成 [PDF](https://arxiv.org/pdf/2601.15859), [HTML](https://arxiv.org/abs/2601.15859)
### Authors
Lina Felsner,Henriette Bast,Tina Dorosti,Florian Schaff,Franz Pfeiffer,Daniela Pfeiffer,Julia Schnabel
### Background
X射线暗场成像能够通过小角度散射提供与常规衰减成像互补的诊断信息，但数据有限性带来挑战，阻碍了深度学习模型的发展。研究表明，使用不确定性指导的渐进生成对抗网络可以直接从标准衰减胸部X射线生成暗场图像，并通过结合先验不确定性和后验不确定性来提高可解释性和可靠性。
### Innovation
本文提出了第一个直接从标准衰减胸部X射线生成暗场图像的框架，采用不确定性指导下的渐进生成对抗网络。该模型结合了先验不确定性与后验不确定性，提高生成图像的结构精确性和定量指标的一致改进，且泛化性能良好，验证了该模型的可靠性。
### Conclusion
研究结果表明，不确定性指导下的生成模型能够实现真实的暗场图像合成，并为未来的临床应用提供了可靠基础。
## 19. `cs.CV` - SplatBus: 通过GPU进程间通信的高斯斑点视图框架 [PDF](https://arxiv.org/pdf/2601.15431), [HTML](https://arxiv.org/abs/2601.15431)
### Authors
Yinghan Xu,Théo Morales,John Dingliana
### Background
辐射场基渲染方法在计算机视觉和计算机图形学社区中引起了广泛关注。它们能够实现复杂的现实世界照明效果的高保真渲染，但这样做会带来高昂的渲染时间成本。为了实现实时渲染，3D Gaussian Splatting（3D高斯斑点渲染法）使用基于扫描仪的方法解决这一问题，使得其适用于自动驾驶、机器人技术、虚拟现实和扩展现实等应用。然而，当前的3D Gaussian Splatting 实现难以集成到传统的基于网格的渲染管道中，而在交互式应用和艺术探索中，基于网格的渲染管道是一个常见的需求。
### Innovation
该软件解决方案利用Nvidia的进程间通信（IPC）API来简化3D Gaussian Splatting 的集成过程，使其能够轻松地整合到传统基于网格的渲染管道中，并允许在Unity、Blender、Unreal Engine以及OpenGL视图中查看渲染结果。
### Conclusion
该研究成果提供了一种框架（SplatBus），并通过GPU进程间通信（GPU IPC）实现了3D高斯斑点渲染的视图。该成果为3D Gaussian Splatting 的广泛应用提供了新的可能，简化了其集成过程并提升了其使用灵活性。
## 20. `cs.CV` - CASL: 概念对齐稀疏潜在空间以解释扩散模型 [PDF](https://arxiv.org/pdf/2601.15441), [HTML](https://arxiv.org/abs/2601.15441)
### Authors
Zhenghao He,Guangzhi Xiong,Boyang Wang,Sanchit Sinha,Aidong Zhang
### Background
扩散模型内部激活包含了丰富的语义信息，但解读这些表示仍然是一个挑战。虽然稀疏自编码器（SAEs）显示了在分离潜在表示方面的潜力，现有的基于SAE的扩散模型理解方法依赖于无法将稀疏特征与人类可理解的概念对齐的无监督方法，这限制了它们在生成图像时提供语义控制的能力。
### Innovation
本研究引入了CASL（Concept-Aligned Sparse Latents），一个监督框架，其作用是将扩散模型的稀疏潜在维度与语义概念对齐。具体而言，CASL首先训练一个在冻结的Unet激活上的SAE以获取分离的潜在表示，然后学习一个轻量级的线性映射，将每个概念与相关的一组潜在维度相关联。为验证这些对齐维度的语义意义，提出CASL-Steer（一种可控的潜在干预方法），沿着学习的概念轴方向调整激活。此外，还引入了编辑精度比（EPR）指标，该指标同时衡量概念特异性与无关属性的保留情况。实验表明，与现有方法相比，该方法在编辑精准度和可解释性方面表现出色。
### Conclusion
据我们所知，这是首次在扩散模型中实现对潜在表示和语义概念的监督对齐的工作。
