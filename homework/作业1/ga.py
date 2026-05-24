"""
遗传算法求解f(x)=x^2最大值
-----------------------------------
1. 运作流程：
   init_population：随机生成初始种群
   fitness：计算每个个体的适应度
   selection：按适应度概率选择两个父代个体
   crossover：对父代基因进行单点交叉，生成子代
   mutation：随机翻转子代的一个基因位，引入变异
   主循环：迭代多代，不断选择、交叉、变异，记录最优个体
-----------------------------------
2. 重要变量说明：
     全局参数：pop_size（种群大小）、gene_length（基因位数）、generations（迭代次数）
     局部变量：
       population：当前种群
        fitness_scores：每个个体的适应度列表
       best_individual：当前找到的最优个体
        best_fitness_value：最优个体的适应度
       new_population：新一代种群
-----------------------------------
3. 函数依赖关系：
   - genetic_algorithm 依赖 init_population、fitness、selection、crossover、mutation
"""

import random


# 创建初始的随机群体
def init_population(pop_size, gene_length):
    # 设定群体里个体总数，每个个体用数字代表自身基因信息
    # 基因位数决定数字能取到的最大范围
    return [random.randint(0, 2 ** gene_length - 1) for _ in range(pop_size)]


# 计算个体好坏程度
def fitness(x):
    # 用数值平方评判优劣，目标是算出最大的结果
    return x ** 2


# 按照优劣挑选繁殖的父辈个体
def selection(population, fitness_scores):
    # 把所有个体的评分全部加起来
    total_fitness = sum(fitness_scores)

    # 换算出每个个体被选中的几率，表现越好选中概率越高
    prob = [f / total_fitness for f in fitness_scores]

    # 依靠概率随机选出两个用来繁衍的个体
    selected = random.choices(population, prob, k=2)

    # 返回挑选好的两个父辈
    return selected


# 两个个体之间交换基因片段
def crossover(parent1, parent2, crossover_rate=0.7, gene_length=5):
    # 按照设定概率判断是否进行基因交换
    if random.random() < crossover_rate:
        # 随便选定一个分割位置
        point = random.randint(1, gene_length - 1)

        # 制作截取基因用到的掩码
        mask = (1 << point) - 1
        # 组合双方基因，生成两个新个体
        child1 = (parent1 & mask) | (parent2 & ~mask)
        child2 = (parent2 & mask) | (parent1 & ~mask)

        # 限制数值大小，保证符合基因位数规则
        child1 = child1 % (2 ** gene_length)
        child2 = child2 % (2 ** gene_length)

        # 输出诞生的新个体
        return child1, child2
    else:
        # 不交换基因就直接保留原本个体
        return parent1, parent2


# 随机改动单个基因点位
def mutation(child, mutation_rate=0.01, gene_length=5):
    # 根据概率判断是否触发基因变动
    if random.random() < mutation_rate:
        # 随机挑选一个位置进行改动
        point = random.randint(0, gene_length - 1)

        # 翻转该位置的基因状态
        child ^= (1 << point)

        # 防止数值超出规定范围
        child = child % (2 ** gene_length)

    # 返回改动后的个体
    return child


# 整体算法运行流程
def genetic_algorithm(pop_size, gene_length, generations):
    # 最先生成一批初始个体
    population = init_population(pop_size, gene_length)

    # 记录全程表现最好的个体
    best_individual = None
    best_fitness_value = -1

    # 循环迭代指定次数不断优化群体
    for generation in range(generations):
        # 挨个算出每个个体的评分
        fitness_scores = [fitness(individual) for individual in population]

        # 找出当前这一批里分数最高的个体
        max_fitness = max(fitness_scores)
        max_fitness_index = fitness_scores.index(max_fitness)

        # 对比更新历史最优的个体数据
        if max_fitness > best_fitness_value:
            best_fitness_value = max_fitness
            best_individual = population[max_fitness_index]

        # 打印每一轮的最优结果信息
        print(f"Generation {generation}: Best individual = {best_individual}, Fitness = {best_fitness_value}")

        # 准备存放新一轮的个体
        new_population = []

        # 直接保留目前最优个体到下一代
        new_population.append(best_individual)

        # 不断繁育新个体，凑齐规定数量
        while len(new_population) < pop_size:
            # 选出两个父辈个体
            parent1, parent2 = selection(population, fitness_scores)

            # 父辈结合产生后代
            child1, child2 = crossover(parent1, parent2, gene_length=gene_length)

            # 后代有可能发生基因变异
            new_population.append(mutation(child1, gene_length=gene_length))

            # 控制群体总数不超标
            if len(new_population) < pop_size:
                new_population.append(mutation(child2, gene_length=gene_length))

        # 用新一批个体替换旧群体
        population = new_population

    # 最终返回找到的最佳结果
    return best_individual, best_fitness_value


# 自定义运行相关参数
pop_size = 100
gene_length = 5
generations = 50

# 启动算法程序
best_individual, best_fitness = genetic_algorithm(pop_size, gene_length, generations)

# 展示最后得到的最优答案
print(f"\nOptimal solution found: x = {best_individual}, f(x) = {best_fitness}")
