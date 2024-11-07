import streamlit as st
from scholarly import scholarly

def buscar_areas_de_pesquisa_google_academico(nome_pesquisador):
    try:
        # Busca o perfil do pesquisador pelo nome
        search_query = scholarly.search_author(nome_pesquisador)
        autor = next(search_query)  # Pega o primeiro resultado

        # Carrega o perfil completo do autor
        autor = scholarly.fill(autor)

        # Coleta as áreas de pesquisa
        areas_de_pesquisa = autor.get("interests", [])
        
        return areas_de_pesquisa if areas_de_pesquisa else ["Nenhuma área de pesquisa encontrada."]
    except StopIteration:
        return ["Perfil não encontrado no Google Acadêmico."]
    except Exception as e:
        return [f"Erro ao buscar áreas de pesquisa: {e}"]

# Interface Streamlit
st.title("Busca de Áreas de Pesquisa no Google Acadêmico")
nome_pesquisador = st.text_input("Digite o nome do pesquisador no Google Acadêmico:")

if st.button("Buscar"):
    if nome_pesquisador:
        with st.spinner("Buscando..."):
            areas_de_pesquisa = buscar_areas_de_pesquisa_google_academico(nome_pesquisador)
        st.subheader("Áreas de pesquisa encontradas:")
        for area in areas_de_pesquisa:
            st.write(f"- {area}")
    else:
        st.warning("Por favor, insira o nome do pesquisador.")
