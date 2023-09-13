import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objs as go
from PIL import Image



def page2():
    st.title('Analyse countries')
    df = pd.read_csv('dataset2.csv')

    search_query = st.text_input("Enter a search query:")

    if search_query:
        filtered_df = df[
            df.apply(lambda row: row.astype(str).str.contains(search_query, case=False, na=False).any(), axis=1)]

        if not filtered_df.empty:
            st.write(filtered_df)
        else:
            st.write("No results found.")
    else:
        st.write(df)

    continent_count = df['ContinentName'].value_counts().reset_index()
    continent_count.columns = ['Continent', 'Number of Countries']
    fig = px.bar(continent_count, x='Continent', y='Number of Countries',
                 title='Number of Countries per Continent')
    st.plotly_chart(fig)

    df['Density'] = pd.to_numeric(df['Density'], errors='coerce')

    # Population Density Plot
    fig = px.histogram(df, x='Density', title='Population Density Distribution')
    st.plotly_chart(fig)

    # Convert 'GDP' and 'Life expectancy' to numeric if they're not
    df['GDP'] = pd.to_numeric(df['GDP'], errors='coerce')
    df['Life expectancy'] = pd.to_numeric(df['Life expectancy'], errors='coerce')

    # Life Expectancy vs GDP Plot
    fig = px.scatter(df, x='GDP', y='Life expectancy', title='Life Expectancy vs GDP')
    st.plotly_chart(fig)


    # Convert 'Tax revenue (%)' to numeric if it's not
    df['Tax revenue (%)'] = pd.to_numeric(df['Tax revenue (%)'], errors='coerce')

    # GDP Plot
    top_gdp = df.sort_values('GDP', ascending=False).head(10)
    fig = px.bar(top_gdp, x='CountryName', y='GDP', title='Top 10 Countries by GDP')
    st.plotly_chart(fig)

    # Tax Revenue Plot
    top_tax_revenue = df.sort_values('Tax revenue (%)', ascending=False).head(10)
    fig = px.bar(top_tax_revenue, x='CountryName', y='Tax revenue (%)', title='Top 10 Countries by Tax Revenue (%)')
    st.plotly_chart(fig)


    # Convert 'Co2-Emissions' to numeric if it's not
    df['Co2-Emissions'] = pd.to_numeric(df['Co2-Emissions'], errors='coerce')

    # CO2 Emissions Plot
    top_co2 = df.sort_values('Co2-Emissions', ascending=False).head(10)
    fig = px.bar(top_co2, x='CountryName', y='Co2-Emissions', title='Top 10 Countries by CO2 Emissions')
    st.plotly_chart(fig)

    def display_treemap():
        df['Co2-Emissions'] = pd.to_numeric(df['Co2-Emissions'])
        fig = px.treemap(df, path=['ContinentName', 'CountryName'], values='Co2-Emissions',
                         title='CO2 Emissions by Country')
        fig.update_layout(height=800, width=1200)  # You can adjust these values as needed
        st.plotly_chart(fig)

    display_treemap()

    def display_treemappercapita():
        df['Co2-Emissions'] = pd.to_numeric(df['Co2-Emissions'])
        df['Co2-Emissions per capita'] = df['Co2-Emissions'] / df['Population']
        fig = px.treemap(df, path=['ContinentName', 'CountryName'], values='Co2-Emissions per capita',
                         title='CO2 Emissions per capita by Country')

        fig.update_layout(height=800, width=1200)  # You can adjust these values as needed
        st.plotly_chart(fig)

    display_treemappercapita()

    columns_to_drop = [
        'CapitalLatitude', 'CapitalLongitude', 'CapitalDescription',
        'Capital/Major City', 'Gross primary education enrollment (%)',
        'Gross tertiary education enrollment (%)', 'Maternal mortality ratio',
        'Minimum wage', 'Official language', 'Out of pocket health expenditure',
        'Tax revenue (%)'
    ]

    # Drop specified columns
    df.drop(columns=columns_to_drop, inplace=True, errors='ignore')

    # Filter the DataFrame for only Switzerland and New Zealand
    filtered_df = df[df['CountryName'].isin(['Switzerland', 'New Zealand'])]

    # Set 'CountryName' as the index of the DataFrame
    filtered_df.set_index('CountryName', inplace=True)
    st.write(filtered_df)


