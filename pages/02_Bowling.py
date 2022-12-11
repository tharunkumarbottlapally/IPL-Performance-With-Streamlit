import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

alltime,seasons=st.tabs(['All Time Records','By Season Stats'])
with alltime:
    tab1, tab2,tab3,tab4,tab5 = st.tabs(['Best Bowling Economy','Best Bowling Strike',
                            'Most Dot Balls Inning','Most Runs Conceded Innings','Most Wickets',])
    with tab1:
        BestBowlingEconomy = pd.read_csv("IPLDataset/AllSeasonsCombined/Best Bowling Economy Per Innings All Seasons Combine.csv")
        BestBowlingEconomy=BestBowlingEconomy.sort_values(by=['Econ'],ascending=True)
        st.write('## Best Bowling Economy Innings')
        BestBowlingEconomy=BestBowlingEconomy.reset_index(drop=True)
        BestBowlingEconomy=BestBowlingEconomy.iloc[: , 1:]
        st.write(BestBowlingEconomy)
        top20eco=BestBowlingEconomy.head(20)


        BarBestBowlingEconomy=alt.Chart(top20eco).mark_bar().encode(
            x='Econ',
            y=alt.Y('Player', sort='-x'),
            color='Against',
            tooltip=['Econ','Against','Match Date'],
        )
        st.altair_chart(BarBestBowlingEconomy,use_container_width=True)
    with tab2:
        ###### BestBowlingEconomy ###########
        BestBowlingStrike = pd.read_csv("IPLDataset/AllSeasonsCombined/Best Bowling Strike Rate Per Innings All Seasons Combine.csv")
        BestBowlingStrike=BestBowlingStrike.sort_values(by=['SR'],ascending=False)
        st.write('## Best Bowling Strike Rate Innings')
        BestBowlingStrike=BestBowlingStrike.reset_index(drop=True)
        BestBowlingStrike=BestBowlingStrike.iloc[: , 1:]
        st.write(BestBowlingStrike)
        top20Strike=BestBowlingStrike.head(20)

        BarBestBowlingStrike=alt.Chart(top20Strike).mark_bar().encode(
            x='SR',
            y=alt.Y('Player', sort='-x'),
            color='Against',
            tooltip=['SR','Against','Match Date'],
        )
        st.altair_chart(BarBestBowlingStrike,use_container_width=True)


    with tab3:
        ###### Most Dot Balls Inning ###########
        MostDotBallsInning = pd.read_csv("IPLDataset/AllSeasonsCombined/Most Dot Balls Per Innings All Seasons Combine.csv")
        MostDotBallsInning=MostDotBallsInning.sort_values(by=['Dots'],ascending=False)
        st.write('## Most Dot Balls Innings ')
        MostDotBallsInning=MostDotBallsInning.reset_index(drop=True)
        MostDotBallsInning=MostDotBallsInning.iloc[: , 1:]
        st.write(MostDotBallsInning)
        top20Dot=MostDotBallsInning.head(20)

        BarMostDotBallsInning=alt.Chart(top20Dot).mark_bar().encode(
            x='Dots',
            y=alt.Y('Player', sort='-x'),
            color='Dots',
            tooltip=['Dots','Against','Match Date'],
        )
        st.altair_chart(BarMostDotBallsInning,use_container_width=True)

    with tab4:
        ###### Most Runs Conceded Innings ###########
        MostRunsConcededInnings = pd.read_csv("IPLDataset/AllSeasonsCombined/Most Runs Conceded Per Innings All Seasons Combine.csv")
        MostRunsConcededInnings=MostRunsConcededInnings.sort_values(by=['Runs'],ascending=False)
        st.write('## Most Runs Conceded Innings')
        MostRunsConcededInnings=MostRunsConcededInnings.reset_index(drop=True)
        MostRunsConcededInnings=MostRunsConcededInnings.iloc[: , 1:]
        st.write(MostRunsConcededInnings)
        top20Runs=MostRunsConcededInnings.head(20)

        BarMostRunsConcededInnings=alt.Chart(top20Runs).mark_bar().encode(
            x='Runs',
            y=alt.Y('Player', sort='-x'),
            color='Runs',
            tooltip=['Runs','Against','Match Date'],
        )
        st.altair_chart(BarMostRunsConcededInnings,use_container_width=True)        

    with tab5:
        ###### Most Runs Conceded Innings ###########
        MostWickets = pd.read_csv("IPLDataset/AllSeasonsCombined/Most Wickets All Seasons Combine.csv")
        MostWickets=MostWickets.sort_values(by=['Wkts'],ascending=False)
        st.write('## Most Wickets ')
        MostWickets=MostWickets.reset_index(drop=True)
        MostWickets=MostWickets.iloc[: , 1:]
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
    with seasons:
        
        options = st.selectbox(
        'Select Year',
        ["2008", '2009', '2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021',])
        if options ==options:
            tab1, tab2,tab3,tab4,tab5 = st.tabs(['Best Bowling Economy','Best Bowling Strike',
                            'Most Dot Balls Inning','Most Runs Conceded Innings','Most Wickets',])
            with tab1:
                BestBowlingEconomy = pd.read_csv("IPLDataset/BestBowlingEconomyInnings/Best Bowling Economy Innings - "+options+".csv")
                BestBowlingEconomy=BestBowlingEconomy.sort_values(by=['Econ'],ascending=True)
                st.write('## Best Bowling Economy Innings')
                BestBowlingEconomy=BestBowlingEconomy.iloc[: , 1:]
                st.write(BestBowlingEconomy)
                top20eco=BestBowlingEconomy.head(20)


                BarBestBowlingEconomy=alt.Chart(top20eco).mark_bar().encode(
                    x='Econ',
                    y=alt.Y('Player', sort='-x'),
                    color='Against',
                    tooltip=['Econ','Against','Match Date'],
                )
                st.altair_chart(BarBestBowlingEconomy,use_container_width=True)
            with tab2:
                ###### BestBowlingStrikeRateInnings ###########
                BestBowlingStrike = pd.read_csv("IPLDataset/BestBowlingStrikeRateInnings/Best Bowling Strike Rate Innings - "+options+".csv")
                BestBowlingStrike=BestBowlingStrike.sort_values(by=['SR'],ascending=False)
                st.write('## Best Bowling Strike Rate Innings')
                BestBowlingStrike=BestBowlingStrike.iloc[: , 1:]
                st.write(BestBowlingStrike)
                top20Strike=BestBowlingStrike.head(20)

                BarBestBowlingStrike=alt.Chart(top20Strike).mark_bar().encode(
                    x='SR',
                    y=alt.Y('Player', sort='-x'),
                    color='Against',
                    tooltip=['SR','Against','Match Date'],
                )
                st.altair_chart(BarBestBowlingStrike,use_container_width=True)


            with tab3:
                ###### Most Dot Balls Inning ###########
                MostDotBallsInning = pd.read_csv("IPLDataset/MostDotBallsInnings/Most Dot Balls Innings - "+options+".csv")
                MostDotBallsInning=MostDotBallsInning.sort_values(by=['Dots'],ascending=False)
                st.write('## Most Dot Balls Innings ')
                MostDotBallsInning=MostDotBallsInning.iloc[: , 1:]
                st.write(MostDotBallsInning)
                top20Dot=MostDotBallsInning.head(20)

                BarMostDotBallsInning=alt.Chart(top20Dot).mark_bar().encode(
                    x='Dots',
                    y=alt.Y('Player', sort='-x'),
                    color='Ov',
                    tooltip=['Dots','Against','Match Date'],
                )
                st.altair_chart(BarMostDotBallsInning,use_container_width=True)

            with tab4:
                ###### Most Runs Conceded Innings ###########
                MostRunsConcededInnings = pd.read_csv("IPLDataset/MostRunsConceded Innings/Most Runs Conceded Innings - "+options+".csv")
                MostRunsConcededInnings=MostRunsConcededInnings.sort_values(by=['Runs'],ascending=False)
                st.write('## Most Runs Conceded Innings')
                MostRunsConcededInnings=MostRunsConcededInnings.iloc[: , 1:]
                st.write(MostRunsConcededInnings)
                top20Runs=MostRunsConcededInnings.head(20)

                BarMostRunsConcededInnings=alt.Chart(top20Runs).mark_bar().encode(
                    x='Runs',
                    y=alt.Y('Player', sort='-x'),
                    color='Ov',
                    tooltip=['Runs','Against','Match Date'],
                )
                st.altair_chart(BarMostRunsConcededInnings,use_container_width=True)        

            with tab5:
                ###### MostWickets ###########
                MostWickets = pd.read_csv("IPLDataset/MostWickets/Most Wickets - "+options+".csv")
                MostWickets=MostWickets.sort_values(by=['Wkts'],ascending=False)
                st.write('## Most Wickets ')
                MostWickets=MostWickets.iloc[: , 1:]
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
                    
