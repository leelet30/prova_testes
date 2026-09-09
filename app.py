import streamlit as st
import database as db
import pandas as pd

db.criar_tabela()

st.title("𝓟𝓪𝓲𝓷𝓮𝓵 𝓭𝓮 𝓖𝓮𝓼𝓽𝓪̃𝓸 𝓭𝓮 𝓐𝓵𝓾𝓷𝓸𝓼", text_alignment="center")

# Cadastro de aluno
st.markdown("#### --- Cadastro Alunos ---", text_alignment="center")
with st.form("form_cadastro_aluno"):

    nome = st.text_input("Nome")
    idade = st.number_input("Idade", value=50)
    nota = st.number_input("Nota",value=0.0, step=0.5, min_value=0.0, max_value=10.0)

    btn_cadastro_aluno = st.form_submit_button("Cadastrar")

if btn_cadastro_aluno:
    msg = db.cadastro_aluno(nome, idade, nota)
    st.warning(msg)

# Exclusão de alunos
st.markdown("#### --- Exclusão Alunos ---", text_alignment="center")
with st.form("form_delete_aluno"):
    id_aluno = st.number_input("ID do aluno", value=0, step=1, min_value=0)

    btn_delete_aluno = st.form_submit_button("Deletar", 
    help="Ao clicar aqui você deleta um aluno")

if btn_delete_aluno:
    msg = db.delete_aluno(id_aluno)
    st.success(msg)

st.markdown("#### --- Alteração de cadastro de Alunos ---", text_alignment="center")
with st.form("form_update_aluno"):
    id_aluno = st.number_input("ID do aluno", value=0, step=1, min_value=0)
    idade = st.number_input("Idade", value=0)

    btn_update_aluno = st.form_submit_button("Alterar")

if btn_update_aluno:
    msg = db.update_idade_aluno(id_aluno, idade)

    if msg == 1:
        st.success("Aluno alterado com sucesso")
    else:
        st.error(msg)

st.markdown("#### --- Lista de alunos cadastrados ---", text_alignment="center")

listaAlunos = db.getAlunos()

if listaAlunos == None:
    st.warning("Não há alunos cadastrados")

else:
    # dataAlunos = [{"ID": aluno[0], "Nome": aluno[1], "Idade": aluno[2], 
    #                "Nota": aluno[3] } for aluno in listaAlunos]

    dataAlunos = pd.DataFrame(listaAlunos, columns=["ID", "Nome", "Idade", "Nota"])

    st.dataframe(dataAlunos, width="stretch", hide_index=True)
    st.table(dataAlunos, width="stretch")
    st.dataframe(listaAlunos, column_config={1: "ID", 2:"Nome", 3:"Idade", 4:"Nota"})

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://4kwallpapers.com/images/walls/thumbs_2t/20822.png");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

#else:

    #i = 0

    # for i in len(listaAlunos):

    #     dataAlunos = [{"ID": listaAlunos[i][0], "Nome": listaAlunos[i][1], "Idade": listaAlunos[i][2], 
    #                "Nota": listaAlunos[i][3]}]       
    #     i = i + 1

    #st.dataframe(listaAlunos, width="stretch")
    #st.table(listaAlunos, index=["ID","Nome","Idade","Nota"], width="stretch")
