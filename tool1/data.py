# python脚本生成调查问卷数据集
import pandas as pd
import random

# 配置总样本量
TOTAL_SAMPLES = 300

# 1. 基础画像权重配置
# 身份：准大学生10%，在校大学生72%，职场新人18%
identity_choices = ['A (准大学生)'] * 30 + ['B (在校大学生)'] * 216 + ['D (职场新人)'] * 54
# 性别：男48%，女52%
gender_choices = ['A (男)'] * 144 + ['B (女)'] * 156

random.shuffle(identity_choices)
random.shuffle(gender_choices)

# 备选数据字典
data_options = {
    'Q3': ['A', 'B', 'C', 'D', 'E'],
    'Q4': ['A', 'B', 'C', 'D', 'E'],
    'Q6': ['联想', '华为', '苹果', '其他品牌', '不考虑购买'],
    'Q7': ['A', 'B', 'C', 'D'],
    'Q8': ['1,2,3,4', '2,1,4,3', '3,1,4,2', '1,3,4,2', '2,4,1,3', '4,1,2,3'],
    'Q9': ['A', 'B', 'C', 'D'],
    'Q10': ['A', 'B', 'C', 'D'],
    'Q11': ['A', 'B', 'C', 'D', 'E'],
    'Q12': ['A', 'B', 'C', 'D', 'E', 'F'],
    'Q13': ['A', 'B', 'C', 'D'],
    'Q14_texts': [
        "帮我一键总结论文和文献", "离线运行大模型，保护隐私", "快速制作PPT并排版", 
        "断网时也能用AI翻译", "跑深度学习时风扇别太响", "帮我写代码和除错",
        "社团活动文案和海报一键生成", "开会自动记录并提炼待办事项", "不懂写提示词，希望AI能懂我"
    ]
}

data_rows = []

for i in range(TOTAL_SAMPLES):
    identity = identity_choices[i]
    gender = gender_choices[i]
    
    # Q3: 场景 (多选, 1-3项)
    q3 = ", ".join(random.sample(data_options['Q3'], random.randint(1, 3)))
    
    # Q4: 痛点
    q4 = random.choice(data_options['Q4'])
    
    # Q5: 认知 (根据报告，约82%听过，但仅18.6%完全懂。设定A:18%, B:63.4%, C/D:18.6%)
    q5_val = random.random()
    if q5_val < 0.18:
        q5 = 'A'
    elif q5_val < 0.814:
        q5 = 'B'
    else:
        q5 = random.choice(['C', 'D'])
        
    # Q6: 品牌偏好 (联想约占62%)
    if random.random() < 0.6:
        q6_list = ['联想']
        if random.random() < 0.2: q6_list.append(random.choice(['华为', '苹果']))
    else:
        q6_list = [random.choice(['华为', '苹果', '其他品牌'])]
    q6 = ", ".join(q6_list)
    
    # Q7, Q8
    q7 = random.choice(data_options['Q7'])
    q8 = random.choice(data_options['Q8'])
    
    # Q9: 反感AI特征 (76%反感浮夸和机械感 -> 高概率包含A/B)
    q9_list = []
    if random.random() < 0.76:
        q9_list.extend(random.sample(['A', 'B'], random.randint(1, 2)))
    else:
        q9_list.extend(random.sample(['C', 'D'], random.randint(1, 2)))
    if random.random() < 0.3 and len(q9_list) < 3:
        q9_list.append(random.choice(['C', 'D']))
    q9 = ", ".join(list(set(q9_list)))
    
    # 其他题目简单随机分配
    q10 = random.choice(data_options['Q10'])
    q11 = ", ".join(random.sample(data_options['Q11'], random.randint(1, 3)))
    q12 = ", ".join(random.sample(data_options['Q12'], 2)) # 选2项
    q13 = random.choice(data_options['Q13'])
    q14 = random.choice(data_options['Q14_texts'])
    
    data_rows.append([
        f"{i+1:03d}", identity, gender, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14
    ])

# 导出数据
columns = ['编号', 'Q1_身份', 'Q2_性别', 'Q3_常驻场景', 'Q4_痛点', 'Q5_AIPC认知', 'Q6_品牌考虑', 
           'Q7_触媒平台', 'Q8_种草元素', 'Q9_反感AI特征', 'Q10_搜索词', 'Q11_否决权', 'Q12_引流活动', 
           'Q13_未进店原因', 'Q14_开放题诉求']
df = pd.DataFrame(data_rows, columns=columns)
df.to_csv('survey_data_300.csv', index=False, encoding='utf-8-sig')
print("300份问卷数据已成功生成：survey_data_300.csv")
