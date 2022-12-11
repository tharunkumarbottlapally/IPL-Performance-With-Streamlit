import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.markdown("# IPL - Where Talent Meets Opportunity ")
st.sidebar.markdown("# IPL - Player Performance Dataset")


st.subheader('Content')
st.text(' The Indian Premier League (IPL) is a professional mens Twenty20 cricket league, contested by ten teams based out of ten Indian cities.\n The league was founded by the Board of Control for Cricket in India (BCCI) in 2007.\n \n It is usually held between March and May of every year and has an exclusive window in the ICC Future Tours Programme.\n The IPL is the most-attended cricket league in the world and in 2014 was ranked sixth by average attendance among all sports leagues.\n In 2010, the IPL became the first sporting event in the world to be broadcast live on YouTube.\n The brand value of the IPL in 2019 was ₹47,500 crores (6.3 billion US dollars), according to Duff & Phelps.\n According to BCCI, the 2015 IPL season contributed ₹1,150 crores (150 million US dollars) to the GDP of the Indian economy.\n \n The 2020 IPL season set a massive viewership record with 31.57 million average impressions and with an overall consumption increase of 23 percent from the 2019 season.\n There have been fourteen seasons of the IPL tournament.\n The current IPL title holders are the Chennai Super Kings, winning the 2021 season.\n \n The venue for the 2020 season was moved due to the COVID-19 pandemic and games were played in the United Arab Emirates.')

st.subheader('Recent Year Stats')
bowlingtab,battingtab = st.tabs(['Bowling','Batting'])

with bowlingtab:

    tab1, tab2,tab3,tab4,tab5 = st.tabs(['Best Bowling Economy','Best Bowling Strike',
                            'Most Dot Balls Inning','Most Runs Conceded Innings','Most Wickets',])
    with tab1:
        BestBowlingEconomy = pd.read_csv("IPLDataset2022/BestBowlingEconomyInnings2022.csv")
        st.write('## Best Bowling Economy Innings - 2022')
        st.write(BestBowlingEconomy)
        top20eco=BestBowlingEconomy.head(20)


        BarBestBowlingEconomy=alt.Chart(top20eco).mark_bar().encode(
            x='Econ',
            y=alt.Y('Player', sort='-x'),
            color='Against',
            tooltip=['Econ','Against'],
        )
        st.altair_chart(BarBestBowlingEconomy,use_container_width=True)
    
    with tab2:
        ###### BestBowlingEconomy ###########
        BestBowlingStrike = pd.read_csv("IPLDataset2022/Best Bowling Strike Rate Innings - 2022.csv")
        st.write('## Best Bowling Strike Rate Innings - 2022')
        st.write(BestBowlingStrike)
        top20Strike=BestBowlingStrike.head(20)

        BarBestBowlingStrike=alt.Chart(top20Strike).mark_bar().encode(
            x='SR',
            y=alt.Y('Player', sort='-x'),
            color='Against',
            tooltip=['SR','Against'],
        )
        st.altair_chart(BarBestBowlingStrike,use_container_width=True)


    with tab3:
        ###### Most Dot Balls Inning ###########
        MostDotBallsInning = pd.read_csv("IPLDataset2022/Most Dot Balls Innings - 2022.csv")
        st.write('## Most Dot Balls Innings - 2022')
        st.write(MostDotBallsInning)
        top20Dot=MostDotBallsInning.head(20)

        BarMostDotBallsInning=alt.Chart(top20Dot).mark_bar().encode(
            x='Dots',
            y=alt.Y('Player', sort='-x'),
            color='Ov',
            tooltip=['Dots','Against'],
        )
        st.altair_chart(BarMostDotBallsInning,use_container_width=True)

    with tab4:
        ###### Most Runs Conceded Innings ###########
        MostRunsConcededInnings = pd.read_csv("IPLDataset2022/Most Runs Conceded Innings - 2022.csv")
        st.write('## Most Runs Conceded Innings - 2022')
        st.write(MostRunsConcededInnings)
        top20Runs=MostRunsConcededInnings.head(20)

        BarMostRunsConcededInnings=alt.Chart(top20Runs).mark_bar().encode(
            x='Runs',
            y=alt.Y('Player', sort='-x'),
            color='Ov',
            tooltip=['Runs','Against'],
        )
        st.altair_chart(BarMostRunsConcededInnings,use_container_width=True)        

    with tab5:
        ###### Most Runs Conceded Innings ###########
        MostWickets = pd.read_csv("IPLDataset2022/Most Wickets - 2022.csv")
        st.write('## Most Wickets - 2022')
        st.write(MostWickets)
        top20Wickets=MostWickets.head(20)

        BarMostWickets=alt.Chart(top20Wickets).mark_bar().encode(
                        x='Wkts',
                        y=alt.Y('Player', sort='-x'),
                        tooltip=['Wkts'],
                        color='Mat',
                        order=alt.Order(
                         # Sort the segments of the bars by this field
                        'Wkts',
                        sort='descending'
                        )
                        )
        st.altair_chart(BarMostWickets,use_container_width=True)     
####### BATTING ###########
#if page == 'Batting':
with battingtab:
    tabbat1,tabbat2,tabbat3,tabbat4,tabbat5=st.tabs(['Most Runs','Most Sixes Innings','Most Fours Innings','Fastest Centuries','Fastest Fifties'])
    with tabbat1:
                        ###### Most Runs ###########
                MostRuns = pd.read_csv("IPLDataset2022/Most Runs - 2022.csv")
                st.write('## Most Runs - 2022')
                st.write(MostRuns)
                top20MostRuns=MostRuns.head(20)

                BarMostRuns=alt.Chart(top20MostRuns).mark_bar().encode(
                                x='Runs',
                                y=alt.Y('Player', sort='-x'),
                                tooltip=['Runs'],
                                color='Mat',
                                order=alt.Order(
                                # Sort the segments of the bars by this field
                                'Runs',
                                sort='descending'
                                )
                                )
                st.altair_chart(BarMostRuns,use_container_width=True)

    with tabbat2:
                        ###### Most Sixes Innings ###########
                MostSixesInnings = pd.read_csv("IPLDataset2022/Most Sixes Innings - 2022.csv")
                st.write('## Most Sixes Innings - 2022')
                st.write(MostSixesInnings)
                top20MostSixesInnings=MostSixesInnings.head(20)

                BarMostSixesInnings=alt.Chart(top20MostSixesInnings).mark_bar().encode(
                                x=alt.Y('6s', sort='-x'),
                                y=alt.Y('Player', sort='-x'),
                                tooltip=['6s'],
                                color='Against',
                              
                                )
                st.altair_chart(BarMostSixesInnings,use_container_width=True)

    with tabbat3:
                        ###### Most Fours Innings ###########
                MostFoursInnings = pd.read_csv("IPLDataset2022/Most Fours Innings - 2022.csv")
                st.write('## Most Fours Innings - 2022')
                st.write(MostFoursInnings)
                top20MostFoursInnings=MostFoursInnings.head(20)

                BarMostFoursInnings=alt.Chart(top20MostFoursInnings).mark_bar().encode(
                                x='4s',
                                y=alt.Y('Player', sort='-x'),
                                tooltip=['4s'],
                                color='Against',
                               
                                )
                st.altair_chart(BarMostFoursInnings,use_container_width=True)

    with tabbat4:
                        ###### Fastest Centuries ###########
                FastestCenturies = pd.read_csv("IPLDataset2022/Fastest Centuries - 2022.csv")
                st.write('## Fastest Centuries- 2022')
                st.write(FastestCenturies)
                top20FastestCenturies=FastestCenturies.head(20)

                BarFastestCenturies=alt.Chart(top20FastestCenturies).mark_bar().encode(
                                x='Runs',
                                y=alt.Y('Player', sort='-x'),
                                tooltip=['BF'],
                                color='Against',

                                )
                st.altair_chart(BarFastestCenturies,use_container_width=True)

    with tabbat5:
                        ###### Fastest Fifties ###########
                FastestFifties = pd.read_csv("IPLDataset2022/Fastest Fifties - 2022.csv")
                st.write('## Fastest Centuries- 2022')
                st.write(FastestFifties)
                top20FastestFifties=FastestFifties.head(20)

                BarFastestFifties=alt.Chart(top20FastestFifties).mark_bar().encode(
                                x='Runs',
                                y=alt.Y('Player', sort='-x'),
                                tooltip=['BF'],
                                color='Against',
                               
                                )
                st.altair_chart(BarFastestFifties,use_container_width=True)
