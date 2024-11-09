import streamlit as st
from scholarly import scholarly
import time

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
st.markdown("<h1 style='color: navy;'>Busca de Áreas de Interesse dos Pesquisadores no Google Acadêmico</h1>", unsafe_allow_html=True)

# Entrada de múltiplos nomes de pesquisadores separados por vírgulas
nomes_pesquisadores = st.text_input("Digite os nomes dos pesquisadores no Google Acadêmico, separados por vírgulas:")

if st.button("Buscar"):
    if nomes_pesquisadores:
        with st.spinner("Buscando..."):
            # Divide a lista de nomes e remove espaços extras
            nomes_lista = [nome.strip() for nome in nomes_pesquisadores.split(",")]
            for nome in nomes_lista:
                st.subheader(f"Áreas de pesquisa para: {nome}")
                areas_de_pesquisa = buscar_areas_de_pesquisa_google_academico(nome)
                for area in areas_de_pesquisa:
                    st.write(f"- {area}")
                # Adiciona um intervalo de 2 segundos entre as buscas
                time.sleep(2)
    else:
        st.warning("Por favor, insira pelo menos um nome de pesquisador.")

# Adiciona a assinatura no final em azul-marinho
st.markdown("<p style='color: navy;'>Ferramenta desenvolvida por: Darliane Cunha</p>", unsafe_allow_html=True)

