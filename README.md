
((python3 -m venv .venv))
((source .venv/bin/activate))
((pip install -r requirements.txt))



Fernando Mello
00341727
Henrique Lindemann
00343234
Luca Fritscher
00343044

Turma B

Valores iniciais ótimos:
b: -0.1
w: 0.8
alpha: 0.000005
num_iterations: 100

Melhor erro quadrático médio: 10.55626756503405

Parte 2

características de cada dataset:

cifar10:
 - classes: 10
 - amostras: 60.000
 - imagens: 32x32x3

cifar100:
 - classes: 100
 - amostras: 60.000
 - imagens: 32x32x3

mnist:
 - classes: 10
 - amostras: 70.000  
 - imagens: 28x28

fmnist:
 - classes: 10
 - amostras: 70.000 
 - imagens: 28x28


1. Pelos testes, pode-se afirmar que os datasets MNIST e Fashion MNIST são mais fáceis de se lidar, visto que possuem apenas um canal de cor, e 10 classes. O data set MNIST acaba sendo menos complexo ainda, pois os números possuem um padrão de desenho mais bem definido do que as roupas que o Fashion MNIST apresenta. Agora, em relação ao CIFAR10 e CIFAR100, a complexidade aumenta, levando em conta que são imagens coloridas, três canais de cor, e com padrões menos definidos ainda. CIFAR100 é a mais desafiadora de todas, as 100 classes dificultam muito o trabalho da rede neural, pois além de serem muitas classes, ainda existe muita similaridade entre algumas delas, como a classe de “mouse” e “hamster”.

2. Em um primeiro momento, utilizando apenas os códigos já fornecidos em labs e no próprio arquivo, obtivemos os seguintes resultados:

'mnist': 'time': 44.93588185310364, 'acc': 93.55999827384949, 
'fashion_mnist': 'time': 83.41171026229858, 'acc': 76.70999765396118,
 'cifar10': 'time': 352.6680290699005, 'acc': 55.980002880096436, 
'cifar100': 'time': 362.82181429862976, 'acc': 0.9999999776482582

No segundo momento, adicionamos mais uma camada com o mesmo número de neurônios e os mesmos hiper parâmetros:

'mnist': 'time': 84.88157653808594, 'acc': 94.2799985408783,
 'fashion_mnist': 'time': 64.26329445838928, 'acc': 79.22000288963318, 
'cifar10': 'time': 349.6024606227875, 'acc': 56.30999803543091,
 'cifar100': 'time': 353.19315671920776, 'acc': 16.009999811649323

Observa-se que houve uma melhora geral, tendo uma melhora notável no conjunto CIFAR100, apesar de ter uma acurácia bem ruim ainda.

Em um terceiro teste, a partir do código inicial, dobramos o número de neurônios, a ideia aqui foi ver o que seria mais impactante nos conjuntos, o dobro de neurônios ou uma camada adicional.

'mnist': 'time': 83.5512306690216, 'acc': 94.56999897956848, 
'fashion_mnist': 'time': 83.52431845664978, 'acc': 74.73999857902527, 
'cifar10': 'time': 478.21955490112305, 'acc': 51.88000202178955, 
'cifar100': 'time': 509.30183935165405, 'acc': 0.9999999776482582

Agora, nota-se que não há muitas melhorias, havendo até certa piora nos conjuntos fashion_mnist e CIFAR10. Entende-se por isso que, para esses conjuntos de dados, é mais interessante adicionar camadas do que o aumento do número de neurônios em uma camada apenas.

Seguindo, decidimos juntar o segundo e terceiro teste, adicionar mais uma camada e dobrar os neurônios, resultando nas seguintes métricas: 

'mnist': 'time': 77.30388832092285, 'acc': 95.73000073432922,
 'fashion_mnist': 'time': 84.34335851669312, 'acc': 84.38000082969666, 
'cifar10': 'time': 509.158730506897, 'acc': 54.93000149726868, 
'cifar100': 'time': 509.4456367492676, 'acc': 19.110000133514404

Obtivemos uma melhora quase geral em relação aos demais testes, apenas no CIFAR10 que não. Nos demais data set`s, consegui-se os melhores números, em especial no fashion_mnist, com uma melhora de 5%.

Para uma quinta e última testagem, alteramos mais coisas. Aplicamos técnicas como normalização de batch e regularização (drop out), além do aumento de camadas e neurônios, a cada camada dobra-se o número de neurônios. 

'mnist': 'time': 673.9715433120728, 'acc': 98.94999861717224, 
'fashion_mnist': 'time': 688.3050405979156, 'acc': 90.86999893188477, 
'cifar10': 'time': 3829.2992136478424, 'acc': 82.9200029373169, 
'cifar100': 'time': 3766.0648794174194, 'acc': 49.16999936103821

Com esses resultados, atinge-se uma acurácia considerável em três data set`s, e tendo uma melhora considerável no CIFAR100, apesar de não estar satisfatória ainda. Conclui-se que, o aumento de camadas e neurônios, alinhadas com as técnicas usadas, foram fundamentais para as consideráveis melhorias obtidas. 
