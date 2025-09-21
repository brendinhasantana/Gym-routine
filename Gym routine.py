import random

# ==========================
# Dados do sistema
# ==========================
exercicios = []  # Cada exercício será um dicionário {nome, tempo, calorias, dia}


# ==========================
# Funções auxiliares
# ==========================
def calcular_imc(peso, altura):
    """Calcula o IMC dado peso e altura."""
    return peso / (altura ** 2)


def mostrar_frase_motivacional():
    """Exibe uma frase motivacional aleatória."""
    frases = [
        "Cada passo conta. Continue se movendo!",
        "Você é mais forte do que pensa!",
        "Não é sobre ser o melhor, é sobre ser melhor do que ontem.",
        "A disciplina é o caminho para o progresso.",
        "Desistir não é uma opção. Você consegue!",
        "Seu corpo pode suportar quase tudo. É sua mente que você precisa convencer.",
        "A dor que você sente hoje é a força que você sentirá amanhã.",
        "Transforme esforço em hábito e hábito em resultado.",
        "Não espere por motivação. Crie disciplina.",
        "Você não precisa ir rápido, só não pare."
    ]
    print(random.choice(frases))


def cadastrar_exercicio():
    """Cadastra um exercício com suas informações básicas."""
    nome = input("Digite o nome do Exercício realizado: ")
    tempo = float(input("Digite o tempo realizado (minutos): "))
    calorias = float(input("Digite a quantidade de calorias queimadas: "))
    dia = input("Digite o dia da semana: ")

    exercicio = {"nome": nome, "tempo": tempo, "calorias": calorias, "dia": dia}
    exercicios.append(exercicio)
    print("✅ Exercício cadastrado com sucesso!")


def relatorio_diario():
    """Mostra os exercícios e totais de um dia específico."""
    dia = input("Digite o dia da semana para o relatório: ")
    filtrados = [e for e in exercicios if e["dia"].lower() == dia.lower()]

    print("\n===== RELATÓRIO DIÁRIO =====")
    if not filtrados:
        print("Nenhum exercício encontrado para esse dia.")
    else:
        tempo_total = sum(e["tempo"] for e in filtrados)
        calorias_total = sum(e["calorias"] for e in filtrados)

        for e in filtrados:
            print(f"- {e['nome']} | Tempo: {e['tempo']} min | Calorias: {e['calorias']} kcal")

        print(f"Tempo total: {tempo_total} min")
        print(f"Calorias totais: {calorias_total} kcal")


def calcular_imc_usuario():
    """Solicita peso e altura e calcula o IMC do usuário."""
    peso = float(input("Digite o seu peso (kg): "))
    altura = float(input("Digite a sua altura (m): "))

    imc = calcular_imc(peso, altura)
    print(f"Seu IMC é: {imc:.2f}")

    if imc < 18.5:
        print("Você está abaixo do peso.")
    elif imc < 25:
        print("Você está no peso ideal.")
    elif imc < 30:
        print("Você está com sobrepeso.")
    else:
        print("Você está com obesidade.")


def verificar_meta_semanal():
    """Verifica se o usuário atingiu a meta semanal de calorias."""
    meta = float(input("Digite a meta semanal de calorias: "))
    total = sum(e["calorias"] for e in exercicios)

    print(f"Total de calorias queimadas: {total}")
    if total >= meta:
        print("🎉 Você atingiu a meta semanal!")
    else:
        print("⚠️ Você não atingiu a meta semanal.")


def media_calorias_por_exercicio():
    """Calcula a média de calorias gastas por exercício."""
    if not exercicios:
        print("Nenhum exercício cadastrado ainda.")
        return
    media = sum(e["calorias"] for e in exercicios) / len(exercicios)
    print(f"Média de calorias por exercício: {media:.2f} kcal")


def grafico_calorias():
    """Mostra um gráfico simples de calorias por exercício no terminal."""
    if not exercicios:
        print("Nenhum exercício cadastrado ainda.")
        return

    print("\n===== GRÁFICO DE CALORIAS =====")
    for e in exercicios:
        barras = "#" * int(e["calorias"] / 10)  # cada # representa 10 calorias
        print(f"{e['nome']}: {barras} ({e['calorias']} cal)")


# ==========================
# Menu principal
# ==========================
def menu():
    opcao = -1
    while opcao != 0:
        print("\n===== MENU =====")
        print("[1] Cadastrar exercício")
        print("[2] Relatório diário")
        print("[3] Calcular IMC")
        print("[4] Verificar meta semanal")
        print("[5] Mostrar frase motivacional")
        print("[6] Média de Calorias por Exercício")
        print("[7] Gráfico de Calorias no Terminal")
        print("[0] Sair")
        print("=================")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("⚠️ Entrada inválida! Digite um número.")
            continue

        if opcao == 1:
            cadastrar_exercicio()
        elif opcao == 2:
            relatorio_diario()
        elif opcao == 3:
            calcular_imc_usuario()
        elif opcao == 4:
            verificar_meta_semanal()
        elif opcao == 5:
            mostrar_frase_motivacional()
        elif opcao == 6:
            media_calorias_por_exercicio()
        elif opcao == 7:
            grafico_calorias()
        elif opcao == 0:
            print("Saindo do sistema... 👋")
        else:
            print("⚠️ Opção inválida. Tente novamente.")


# ==========================
# Execução
# ==========================
if __name__ == "__main__":
    menu()
