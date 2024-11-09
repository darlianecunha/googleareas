import streamlit as st
from scholarly import scholarly

def search_research_areas_google_scholar(researcher_name):
    try:
        # Search for the researcher's profile by name
        search_query = scholarly.search_author(researcher_name)
        author = next(search_query)  # Get the first result

        # Load the full profile of the author
        author = scholarly.fill(author)

        # Collect research areas
        research_areas = author.get("interests", [])
        
        return research_areas if research_areas else ["No research areas found."]
    except StopIteration:
        return ["Profile not found on Google Scholar."]
    except Exception as e:
        return [f"Error retrieving research areas: {e}"]

# Streamlit Interface
st.title("Researcher Interest Areas Search on Google Scholar")
st.markdown("<p style='color: navy;'>Developed by: Darliane Cunha</p>", unsafe_allow_html=True)
researcher_name = st.text_input("Enter the researcher's name on Google Scholar:")

if st.button("Search"):
    if researcher_name:
        with st.spinner("Searching..."):
            research_areas = search_research_areas_google_scholar(researcher_name)
        st.subheader("Found Research Areas:")
        for area in research_areas:
            st.write(f"- {area}")
    else:
        st.warning("Please enter the researcher's name.")
