import streamlit as st
import datetime
import time

st.set_page_config(page_title="Nosso Treino ❤️", page_icon="💪", layout="centered")

if 'history_treinos' not in st.session_state:
    st.session_state.history_treinos = []
if 'history_refeicoes' not in st.session_state:
    st.session_state.history_refeicoes = []

st.title("💪 Nosso Treino & Dieta ❤️")
st.subheader("Conectados pelo foco, mesmo à distância!")

tab1, tab2, tab3, tab4 = st.tabs(["🏋️ Treinos", "🍎 Dieta & Calorias", "⏱️ Cronômetro", "📊 Histórico Compartilhado"])

with tab1:
    st.header("Personalize seu Treino")
    usuario = st.selectbox("Quem vai treinar?", ["Eu", "Meu Amor"], key="user_treino")
    tipo_treino = st.text_input("Nome do Treino (ex: Pernas, Cardio, Superior):")
    exercicios = st.text_area("Lista de Exercícios e Séries:")
    
    if st.button("Registrar Treino Concluído"):
        if tipo_treino and exercicios:
            data_atual = datetime.date.today().strftime("%d/%m/%Y")
            st.session_state.history_treinos.append({
                "Data": data_atual, "Quem": usuario, "Treino": tipo_treino, "Detalhes": exercicios
            })
            st.success(f"Boa! Treino de {usuario} registrado! 🎉")

with tab2:
    st.header("Contador de Calorias & Refeições")
    usuario_dieta = st.selectbox("Quem comeu?", ["Eu", "Meu Amor"], key="user_dieta")
    refeicao = st.text_input("Qual foi a refeição?")
    alimentos = st.text_area("O que comeu exatamente?")
    calorias = st.number_input("Total de Calorias Estimadas (kcal):", min_value=0, step=50)
    
    if st.button("Registrar Refeição"):
        if refeicao and calorias > 0:
            data_atual = datetime.date.today().strftime("%d/%m/%Y")
            st.session_state.history_refeicoes.append({
                "Data": data_atual, "Quem": usuario_dieta, "Refeicao": refeicao, "Alimentos": alimentos, "Calorias": calorias
            })
            st.success("Refeição guardada! 🍎")

with tab3:
    st.header("⏱️ Cronômetro de Descanso")
    tempo_segundos = st.number_input("Tempo de descanso (segundos):", min_value=5, max_value=300, value=60)
    
    if st.button("Iniciar Descanso"):
        progresso = st.progress(0)
        status_text = st.empty()
        for i in range(tempo_segundos):
            restante = tempo_segundos - i
            status_text.text(f"Descanse! Tempo restante: {restante}s")
            progresso.progress((i + 1) / tempo_segundos)
            time.sleep(1)
        status_text.text("⏱️ Fim do descanso! Próxima série! 🔥")
        st.balloons()

with tab4:
    st.header("📊 Nosso Painel de Evolução")
    st.subheader("🏋️ Últimos Treinos Concluídos")
    if st.session_state.history_treinos:
        for t in reversed(st.session_state.history_treinos):
            st.info(f"**{t['Data']}** - 👤 **{t['Quem']}** fez: **{t['Treino']}**\n\n*Exercícios:* {t['Detalhes']}")
    else:
        st.write("Nenhum treino registrado ainda.")
        
    st.subheader("🍎 Diário de Alimentação")
    if st.session_state.history_refeicoes:
        total_eu = sum(r['Calorias'] for r in st.session_state.history_refeicoes if r['Quem'] == 'Eu')
        total_amor = sum(r['Calorias'] for r in st.session_state.history_refeicoes if r['Quem'] == 'Meu Amor')
        col1, col2 = st.columns(2)
        col1.metric("Calorias (Eu)", f"{total_eu} kcal")
        col2.metric("Calorias (Amor)", f"{total_amor} kcal")

 
