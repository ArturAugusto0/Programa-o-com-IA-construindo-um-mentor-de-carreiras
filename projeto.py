import os
from google import genai
from google.genai import types

# Certifique-se de configurar a variável de ambiente GEMINI_API_KEY
cliente = genai.Client()

INSTRUCAO_MENTOR = """
Você é um Mentor de Carreiras Sênior especializado em tecnologia.
Seu objetivo é:
1. Analisar o perfil e os objetivos do usuário com empatia e rigor técnico.
2. Identificar lacunas de habilidades (skill gaps) para a vaga desejada.
3. Propor planos de ação práticos e fazer perguntas de entrevista técnica quando solicitado.
Mantenha as respostas objetivas, organizadas em tópicos e sempre proponha um próximo passo claro.
"""

def iniciar_mentor():
    chat = cliente.chats.create(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=INSTRUCAO_MENTOR,
            temperature=0.7,
        )
    )

    print("=== Mentor de Carreiras IA iniciado ===")
    print("Digite 'sair' para encerrar a sessão.\n")

    # Primeira interação guiada para análise de perfil
    perfil = input("Descreva sua experiência atual e qual cargo você busca: ")
    resposta = chat.send_message(
        f"Analise meu perfil atual e trace um plano inicial de 4 semanas para meu objetivo: {perfil}"
    )
    print(f"\nMentor:\n{resposta.text}\n")

    # Loop contínuo de mentoria e simulação de entrevista
    while True:
        mensagem_usuario = input("Você: ")
        if mensagem_usuario.strip().lower() == "sair":
            print("Sessão encerrada. Bons estudos!")
            break

        resposta = chat.send_message(mensagem_usuario)
        print(f"\nMentor:\n{resposta.text}\n")

if __name__ == "__main__":
    iniciar_mentor()
