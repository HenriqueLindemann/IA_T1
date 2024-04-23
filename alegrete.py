import numpy as np


def compute_mse(b, w, data):
    """
    Calcula o erro quadratico medio
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :return: float - o erro quadratico medio
    """

    X = data[:, 0]
    Y = data[:, 1]

    Y_hat = np.dot(X, w) + b

    mse = np.mean(np.square(Y_hat - Y))

    return mse


def step_gradient(b, w, data, alpha):
    """
    Executa uma atualização por descida do gradiente  e retorna os valores atualizados de b e w.
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :return: float,float - os novos valores de b e w, respectivamente
    """

    X = data[:, 0]
    Y = data[:, 1]

    Y_hat = np.dot(X, w) + b

    b = b - (alpha * (np.mean(2 * (Y_hat - Y))))

    w = w - (alpha * (np.mean(np.dot((2 * X), (Y_hat - Y)))))

    return b, w


def fit(data, b, w, alpha, num_iterations):
    """
    Para cada época/iteração, executa uma atualização por descida de
    gradiente e registra os valores atualizados de b e w.
    Ao final, retorna duas listas, uma com os b e outra com os w
    obtidos ao longo da execução (o último valor das listas deve
    corresponder à última época/iteração).

    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :param num_iterations: int - numero de épocas/iterações para executar a descida de gradiente
    :return: list,list - uma lista com os b e outra com os w obtidos ao longo da execução
    """

    b_arr = [b]
    w_arr = [w]

    for iter in range(num_iterations):
      b_temp, w_temp = step_gradient(b_arr[iter], w_arr[iter], data, alpha)

      b_arr.append(b_temp)
      w_arr.append(w_temp)

    return b_arr, w_arr
