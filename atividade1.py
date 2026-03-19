# 1. Sistema de Rank com Penalidade
def rank_jogador(pontos, derrotas):
    pontos_finais = pontos - (derrotas * 10)
    
    if pontos_finais < 0:
        return "Banido"
    elif pontos_finais < 100:
        return "Bronze"
    elif pontos_finais < 300:
        return "Prata"
    elif pontos_finais < 600:
        return "Ouro"
    else:
        return "Diamante"


# 2. Sistema Bancário com Taxa
def saldo_final(saldo, saque):
    if saque > saldo:
        return "Saldo insuficiente"
    
    if saque > 1000:
        taxa = saque * 0.02
        saque_total = saque + taxa
    else:
        saque_total = saque
    
    return saldo - saque_total


# 3. Sistema de Magia com Combinação
def tipo_magia(fogo, agua):
    if fogo and agua:
        return "Vapor"
    elif fogo:
        return "Fogo"
    elif agua:
        return "Água"
    else:
        return "Sem magia"


# 4. Sistema de Pontuação com Bônus Oculto
def pontuacao_total(pontos, tempo):
    if tempo < 30:
        pontos += 50
    elif tempo > 100:
        pontos -= 20
    
    if pontos > 200:
        return "Recorde"
    
    return pontos


# 5. Sistema de Segurança com Múltiplas Condições
def verificar_acesso(usuario, senha, tentativas):
    if tentativas >= 3:
        return "Bloqueado"
    
    if usuario == "admin" and senha == "1234":
        return "Acesso total"
    elif usuario == "admin" and senha != "1234":
        return "Senha incorreta"
    else:
        return "Usuário inválido"


# 6. Missão Espacial – Lógica Composta
def lancar_foguete(combustivel, clima, sistema_ok):
    if combustivel < 100:
        return "Combustível insuficiente"
    elif clima != "bom":
        return "Clima desfavorável"
    elif not sistema_ok:
        return "Falha no sistema"
    else:
        return "Lançamento autorizado"