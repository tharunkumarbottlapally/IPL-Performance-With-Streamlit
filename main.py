import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.markdown("# IPL - Where Talent Meets Opportunity ")
st.sidebar.markdown("# IPL - Player Performance Dataset")


st.subheader('Content')
st.text(' The Indian Premier League (IPL) is a professional mens Twenty20 cricket league, contested by ten teams based out of ten Indian cities.\n The league was founded by the Board of Control for Cricket in India (BCCI) in 2007.\n \n It is usually held between March and May of every year and has an exclusive window in the ICC Future Tours Programme.\n The IPL is the most-attended cricket league in the world and in 2014 was ranked sixth by average attendance among all sports leagues.\n In 2010, the IPL became the first sporting event in the world to be broadcast live on YouTube.\n The brand value of the IPL in 2019 was ₹47,500 crores (6.3 billion US dollars), according to Duff & Phelps.\n According to BCCI, the 2015 IPL season contributed ₹1,150 crores (150 million US dollars) to the GDP of the Indian economy.\n \n The 2020 IPL season set a massive viewership record with 31.57 million average impressions and with an overall consumption increase of 23 percent from the 2019 season.\n There have been fourteen seasons of the IPL tournament.\n The current IPL title holders are the Chennai Super Kings, winning the 2021 season.\n \n The venue for the 2020 season was moved due to the COVID-19 pandemic and games were played in the United Arab Emirates.')

#bowlingtab,battingtab = st.tabs(['Bowling','Batting'])
page = st.sidebar.selectbox('Select Stats',
  ['Bowling','Batting'])



###### BestBowlingEconomy ###########

if page == 'Bowling':
    tab1, tab2,tab3,tab4,tab5 = st.tabs(['Best Bowling Economy','Best Bowling Strike',
                            'Most Dot Balls Inning','Most Runs Conceded Innings','Most Wickets',])
    with tab1:
        BestBowlingEconomy = pd.read_csv("IPLDataset2022/BestBowlingEconomyInnings2022.csv")
        st.write('## Best Bowling Economy Innings - 2022')
        st.write(BestBowlingEconomy)


        BarBestBowlingEconomy=alt.Chart(BestBowlingEconomy).mark_bar().encode(
            x='Econ',
            y='Player',
            color='Against',
            tooltip=['Econ','Against'],
        )
        st.altair_chart(BarBestBowlingEconomy,use_container_width=True)
    
    with tab2:
        ###### BestBowlingEconomy ###########
        BestBowlingStrike = pd.read_csv("IPLDataset2022/Best Bowling Strike Rate Innings - 2022.csv")
        st.write('## Best Bowling Strike Rate Innings - 2022')
        st.write(BestBowlingStrike)

        BarBestBowlingStrike=alt.Chart(BestBowlingStrike).mark_bar().encode(
            x='SR',
            y='Player',
            color='Against',
            tooltip=['SR','Against'],
        )
        st.altair_chart(BarBestBowlingStrike,use_container_width=True)


    with tab3:
        ###### Most Dot Balls Inning ###########
        MostDotBallsInning = pd.read_csv("IPLDataset2022/Most Dot Balls Innings - 2022.csv")
        st.write('## Most Dot Balls Innings - 2022')
        st.write(MostDotBallsInning)

        BarMostDotBallsInning=alt.Chart(MostDotBallsInning).mark_bar().encode(
            x='Dots',
            y='Player',
            color='Ov',
            tooltip=['Dots','Against'],
        )
        st.altair_chart(BarMostDotBallsInning,use_container_width=True)

    with tab4:
        ###### Most Runs Conceded Innings ###########
        MostRunsConcededInnings = pd.read_csv("IPLDataset2022/Most Runs Conceded Innings - 2022.csv")
        st.write('## Most Runs Conceded Innings - 2022')
        st.write(MostDotBallsInning)

        BarMostRunsConcededInnings=alt.Chart(MostRunsConcededInnings).mark_bar().encode(
            x='Runs',
            y='Player',
            color='Ov',
            tooltip=['Wkts','Against'],
        )
        st.altair_chart(BarMostRunsConcededInnings,use_container_width=True)        

    with tab5:
        ###### Most Runs Conceded Innings ###########
        MostWickets = pd.read_csv("IPLDataset2022/Most Wickets - 2022.csv")
        st.write('## Most Wickets - 2022')
        st.write(MostWickets)

        BarMostWickets=alt.Chart(MostWickets).mark_bar().encode(
                        x='Wkts',
                        y='Player',
                        tooltip=['Wkts'],
                        color='Mat',
                        order=alt.Order(
                         # Sort the segments of the bars by this field
                        'Wkts',
                        sort='ascending'
                        )
                        )
        st.altair_chart(BarMostWickets,use_container_width=True)     
####### BATTING ###########
if page == 'Batting':
    tab1,tab2=st.tabs(['Most Runs','Fastest Centuries'])
    with tab1:
                        ###### Most Runs ###########
                MostRuns = pd.read_csv("IPLDataset2022/Most Runs - 2022.csv")
                st.write('## Most Runs - 2022')
                st.write(MostRuns)

                BarMostRuns=alt.Chart(MostRuns).mark_bar().encode(
                                x='Runs',
                                y='Player',
                                tooltip=['Runs'],
                                color='Mat',
                                order=alt.Order(
                                # Sort the segments of the bars by this field
                                'Runs',
                                sort='ascending'
                                )
                                )
                st.altair_chart(BarMostRuns,use_container_width=True)
