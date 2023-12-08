

from funcoes_dupla_estrela import *

# Parâmetros da matriz de capacitores
n_col = 4
n_lin = 2
num_matrizes = 2 * 3 * 1
# Número total de capacitâncias
num_capacitancias = num_matrizes * n_col * n_lin
capacitancias_por_matriz = n_col * n_lin

# Ler capacitâncias e número de série correspondente
capacitancias_df = pd.read_excel("minhas_latas.xlsx").head(num_capacitancias)
capacitancias = np.array(capacitancias_df["uF"])
num_serie_cap = np.array(capacitancias_df["no_serie"])

# Criar as matrizes de capacitores e matrizes número de série
matrizes, numeros = criar_matrizes(num_capacitancias,
                                    capacitancias, num_serie_cap,
                                    capacitancias_por_matriz, n_lin, n_col)

# Encontrar melhor configuração
n_iteracoes = 10000
melhor_configuracao_value, melhor_configuracao_nrser = \
    otimizar_capacitancias(n_iteracoes, matrizes, numeros, n_lin, n_col,
                           calcular_capacitancia_equivalente)





exportar_matrizes_para_excel(melhor_configuracao_nrser, melhor_configuracao_value,
                             'melhor_configuracao_nrser.xlsx', 'melhor_configuracao_value.xlsx')

