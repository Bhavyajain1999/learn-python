import pandas as pd
import streamlit as st
import time
import matplotlib as plt
import matplotlib.pyplot as plt


st.set_page_config(layout='wide',page_title='StartUp Analysis')


df = pd.read_csv('D:\\Coding journey 2024\\datascience\\stremlit\\startup_cleaned.csv')

df['date'] = pd.to_datetime(df['date'],errors='coerce')
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

st.sidebar.title('startup funding analysis')

def load_overall_analysis():
    st.title('Overall Analysis')

    # total invested amount
    total = round(df['amount'].sum())
    # max amount infused in a startup
    max_funding = df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]
    # avg ticket size
    avg_funding = df.groupby('startup')['amount'].sum().mean()
    # total funded startups
    num_startups = df['startup'].nunique()

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        st.metric('Total',str(total) + ' Cr')
    with col2:
        st.metric('Max', str(max_funding) + ' Cr')

    with col3:
        st.metric('Avg',str(round(avg_funding)) + ' Cr')

    with col4:
        st.metric('Funded Startups',num_startups)

    st.header('MoM graph')
    selected_option = st.selectbox('Select Type',['Total','Count'])
    if selected_option == 'Total':
        temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()

    temp_df['x_axis'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')

    fig3, ax3 = plt.subplots()
    ax3.plot(temp_df['x_axis'], temp_df['amount'])

    st.pyplot(fig3)



def load_startup_details(startup):
    """Displays details about a specific startup."""

    st.title(startup)

    # Load relevant data for the startup
    startup_df = df[df['startup'].str.contains(startup)]

    # Ensure relevant columns exist before accessing them
    required_cols = ['date', 'city', 'round', 'investors']
    if not all(col in startup_df.columns for col in required_cols):
        missing_cols = ', '.join(set(required_cols) - set(startup_df.columns))
        st.write(f"Missing data columns: {missing_cols}")
        return  # Early exit if required columns are missing

    # Select relevant columns and filter for the startup (reorder to prioritize date)
    filtered_df = startup_df[required_cols]

    # Display data in a Streamlit table
    st.subheader('Investment Details')
    st.dataframe(filtered_df)
  
    show_similar_startups(startup)

def show_similar_startups(startup):
    required_cols = ['vertical', 'subvertical']
    if not all(col in df.columns for col in required_cols):
        st.write(f"Missing data columns: {', '.join(set(required_cols) - set(df.columns))}")
        return

    # Find similar startups (assuming a single vertical and subvertical per startup)
    vertical = df[df['startup'] == startup]['vertical'].values[0] if startup in df['startup'].tolist() else None
    subvertical = df[df['startup'] == startup]['subvertical'].values[0] if startup in df['startup'].tolist() else None
    if vertical is None or subvertical is None:
        st.write(f"Startup '{startup}' not found or missing vertical/subvertical data.")
        return

    similar_df = df[
        (df['vertical'] == vertical) & (df['subvertical'] == subvertical) & (df['startup'] != startup)
    ]

    # Display similar startups table (if any)
    if not similar_df.empty:
        st.subheader('Similar Startups in Same Vertical and Subvertical:')
        st.dataframe(similar_df[['startup', 'city', 'round']])  # Show relevant columns
    else:
        st.write("No similar startups found for this vertical and subvertical.")



  


def load_investor_details(investor): 
    st.title(investor)
    # load the recent 5 investments of the investor
    last5_df = df[df['investors'].str.contains(investor)].head()[['date', 'startup', 'vertical', 'city', 'round', 'amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last5_df)

    col1, col2 = st.columns(2)
    with col1:
        # biggest investments
        big_series = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
        st.subheader('Biggest Investments')
        fig, ax = plt.subplots()
        ax.bar(big_series.index,big_series.values)

        st.pyplot(fig)

    with col2:
        verical_series = df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()

        st.subheader('Sectors invested in')
        fig1, ax1 = plt.subplots()
        ax1.pie(verical_series,labels=verical_series.index,autopct="%0.01f%%")

        st.pyplot(fig1)
    print(df.info())
    col3, col4 = st.columns(2)
    with col3:
        verical_series3 = df[df['investors'].str.contains(investor)].groupby('round')['amount'].sum()

        st.subheader('invested in rounds')
        fig3, ax3 = plt.subplots()
        ax3.pie(verical_series3,labels=verical_series3.index,autopct="%0.01f%%")

        st.pyplot(fig3)

    with col4:
        verical_series4 = df[df['investors'].str.contains(investor)].groupby('city')['amount'].sum()

        st.subheader('city wise investment')
        fig4, ax4 = plt.subplots()
        ax4.pie(verical_series4,labels=verical_series4.index,autopct="%0.01f%%")

        st.pyplot(fig4)


    df['year'] = df['date'].dt.year
    year_series = df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()

    st.subheader('YoY Investment')
    fig2, ax2 = plt.subplots()
    ax2.plot(year_series.index,year_series.values)

    st.pyplot(fig2)
    show_similar_investors(investor)


def show_similar_investors(selected_investor):
    """Finds investors who have invested in the same verticals and subverticals as the selected investor."""

    # Ensure relevant columns exist before accessing them
    required_cols = ['vertical', 'subvertical', 'investors']
    if not all(col in df.columns for col in required_cols):
        st.write(f"Missing data columns: {', '.join(set(required_cols) - set(df.columns))}")
        return

    # Extract invested verticals and subverticals for the selected investor
    investor_info = df[df['investors'].str.contains(selected_investor)]
    if investor_info.empty:
        st.write(f"Investor '{selected_investor}' not found.")
        return
    invested_verticals = investor_info['vertical'].tolist()
    invested_subverticals = investor_info['subvertical'].tolist()

    # Find similar investors based on invested verticals and subverticals
    similar_investors = df[
        df['investors'].str.contains(selected_investor, na=False) &  # Exclude the selected investor
        df['vertical'].isin(invested_verticals) &
        df['subvertical'].isin(invested_subverticals)
    ]['investors'].unique()

    # Display results
    if len(similar_investors) > 0:
        st.subheader('Similar Investors based on category:')
        for investor in similar_investors:
            st.write(f'- {investor}')  # List investors with bullet points
    else:
        st.write("No similar investors found based on invested verticals and subverticals.")



option = st.sidebar.selectbox('selectone',['overall analysis','start up', 'investor'])

if option == 'overall analysis':
    load_overall_analysis()

    
elif option == 'start up':
    selected_start_up = st.sidebar.selectbox('select startup',sorted(df['startup'].unique().tolist()))
    
    btn1 = st.sidebar.button('Find StartUp Details')
   
    if btn1:
            load_startup_details(selected_start_up)
    

    
else:
    selected_investor = st.sidebar.selectbox('select investor',sorted(set(df['investors'].str.split(',').sum())))
   
    btn2 = st.sidebar.button('find investor details')
    
    if btn2:
            load_investor_details(selected_investor)
    
    