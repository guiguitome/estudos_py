# Constantes:
# no python, já que o tipo da variável não é declarado, foi atribuido que var em caps lock é uma const

# Complexidade: no python, menos complexo -> melhor
# colocar muitas condicões no mesmo if -> ruim
# quanto mais identação -> ruim 

vel_carro = 40 #variável da velocidade do carro
local_carro = 90 #variável do km que o carro está

VEL_MAX = 60 #constante de velocidade maxima
LOCAL_1 = 100 # local do radar
RADAR_RANGE = 1 #distancia que o radar  cobre

carro_passou_vel = vel_carro > VEL_MAX
area_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

if carro_passou_vel:
    print("O carro passou da velocidade maxima")

# if local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) and \
#     vel_carro > RADAR_1:
#     print("carro multado em radar 1")

if area_radar_1 and carro_passou_vel: #se tiver dentro da area do radar e o carro ta acima da velocidade permitida
    print("carro multado em radar 1")