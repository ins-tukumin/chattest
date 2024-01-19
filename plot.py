import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import japanize_matplotlib

def sigmoid(x):
    return 1/(1+np.exp(-x))

xs = np.linspace(1, 20, 1000)
alpha = 0.4
y_bias = sigmoid(alpha*(xs-15))
y_variance = sigmoid(-alpha*(xs-5))

fig, ax = plt.subplots(figsize=(8, 6))
sns.lineplot(x=xs, y=y_bias, ax=ax, label='バリアンス', linestyle='--')
sns.lineplot(x=xs, y=y_variance, ax=ax, label='バイアス', linestyle='--')
sns.lineplot(x=xs, y=y_bias+y_variance, ax=ax, label='汎化誤差')
ax.set_xlabel('入力の次元')
fig.savefig('bias_variance.png', dpi=300, transparent=False, facecolor='white')