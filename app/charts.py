import matplotlib.pyplot as plt

def generate_bar_chart(name, values, labels):
    
    fig, ax = plt.subplots()
    ax.bar(labels,values)
    plt.savefig(f'./imgs/{name}.png')
    plt.close()

def generate_pie_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.savefig(f'./imgs/{name}.png')
    plt.close()

if __name__ == '__main__':
    generate_pie_chart(values, labels)