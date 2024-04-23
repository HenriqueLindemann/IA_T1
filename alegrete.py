import numpy as np

def compute_mse(b, w, data):
    total_error = 0.0
    # Calcula o total do erro quadrático
    for i in range(0, len(data)):
        x = data[i, 0]
        y = data[i, 1]
        # Diferença entre o valor observado (usando x, w e b) e o valor previsto (em data)
        error = (y - (w * x + b)) ** 2
        total_error += error
    # Calcula a média do erro quadrático
    mse = total_error / len(data)
    return mse

def step_gradient(b, w, data, alpha):
    b_gradient = 0
    w_gradient = 0
    N = float(len(data))
    
    # Loop através de cada ponto de dado no conjunto de dados
    for i in range(len(data)):
        x = data[i, 0]
        y = data[i, 1]
        
        # Calcula o gradiente do erro com relação a b 
        b_gradient += -(2/N) * (y - ((w * x) + b))
        
        # Calcula o gradiente do erro com relação a w 
        w_gradient += -(2/N) * x * (y - ((w * x) + b))
    
    # Atualiza b e w usando os gradientes e a taxa de aprendizado
    new_b = b - (alpha * b_gradient)
    new_w = w - (alpha * w_gradient)
    
    return new_b, new_w

def fit(data, b, w, alpha, num_iterations):
    b_new = b
    w_new = w
    # Inicializa listas para registrar a evolução dos parâmetros
    bs = []
    ws = []
    
    # Executa a descida do gradiente para um número definido de iterações
    for i in range(num_iterations):
        bs.append(b_new)
        ws.append(w_new)
        
        # Atualiza b e w executando um passo de descida do gradiente
        b_new, w_new = step_gradient(b_new, w_new, np.array(data), alpha)
    
    # Retorna as listas com os valores de b e w registrados a cada iteração
    return bs, ws