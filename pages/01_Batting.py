import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


alltime,seasons=st.tabs(['All Time Records','By Season Stats'])
with alltime:

        tabbat1,tabbat2,tabbat3,tabbat4,tabbat5,tabbat6=st.tabs(['Most Runs','Most Sixes Innings','Most Fours Innings','Fastest Centuries','Fastest Fifties','Most Runs Over'])
        with tabbat1:
                        ###### Most Runs ###########
                MostRuns = pd.read_csv("IPLDataset/AllSeasonsCombined/Most Runs All Seasons Combine.csv")
                MostRuns=MostRuns.sort_values(by=['Runs'],ascending=False)
                st.write('## Most Runs ')
                MostRuns=MostRuns.reset_index(drop=True)
                st.write(MostRuns)
                top20MostRuns=MostRuns.head(100)

                BarMostRuns=alt.Chart(top20MostRuns).mark_bar().encode(
                                x='Runs',
                                y=alt.Y('Player', sort='-x'),
                                tooltip=['Runs'],
                                color='Player',
                                order=alt.Order(
                                # Sort the segments of the bars by this field
                                'Player',
                                sort='ascending'
                                )
                                )
                st.altair_chart(BarMostRuns,use_container_width=True)

        with tabbat2:
                        ###### Most Sixes Innings ###########
                MostSixesInnings = pd.read_csv("IPLDataset/AllSeasonsCombined/Most Sixes Per Innings All Seasons Combine.csv")
                MostSixesInnings=MostSixesInnings.sort_values(by=['6s'],ascending=False)
                st.write('## Most Sixes Innings ')
                MostSixesInnings=MostSixesInnings.reset_index(drop=True)
                st.write(MostSixesInnings)
                top20MostSixesInnings=MostSixesInnings.style.hide_index()
                top20MostSixesInnings=MostSixesInnings.head(20)

                BarMostSixesInnings=alt.Chart(top20MostSixesInnings).mark_bar().encode(
                                x=alt.Y('6s'),
                                y=alt.Y('Player', sort='-x'),
                                tooltip=['6s'],
                                color='Against',
                                 order=alt.Order(
                                # Sort the segments of the bars by this field
                                'Player',
                                sort='descending'
                                )
                                
                                )
                st.altair_chart(BarMostSixesInnings,use_container_width=True)

        with tabbat3:
                        ###### Most Fours Innings ###########
                MostFoursInnings = pd.read_csv("IPLDataset/AllSeasonsCombined/Most Fours Per Innings All Seasons Combine.csv")
                MostFoursInnings=MostFoursInnings.sort_values(by=['4s'],ascending=False)
                st.write('## Most Fours Innings ')
                MostFoursInnings=MostFoursInnings.reset_index(drop=True)
                st.write(MostFoursInnings)
                top20MostFoursInnings=MostFoursInnings.head(50)

                BarMostFoursInnings=alt.Chart(top20MostFoursInnings).mark_bar().encode(
                                x='4s',
                                y=alt.Y('Player', sort='-x'),
                                tooltip=['4s'],
                                color='Against',order=alt.Order(
                                # Sort the segments of the bars by this field
                                'Player',
                                sort='descending'
                                )
                                
                                )
                st.altair_chart(BarMostFoursInnings,use_container_width=True)

        with tabbat4:
                        ###### Fastest Centuries ###########
                FastestCenturies = pd.read_csv("IPLDataset/AllSeasonsCombined/Fastest Centuries All Seasons Combine.csv")
                FastestCenturies=FastestCenturies.sort_values(by=['BF'],ascending=True)
                st.write('## Fastest Centuries')
                FastestCenturies=FastestCenturies.reset_index(drop=True)
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
                FastestFifties = pd.read_csv("IPLDataset/AllSeasonsCombined/Fastest Fifties All Seasons Combine.csv")
                FastestFifties=FastestFifties.sort_values(by=['BF'],ascending=True)
                st.write('## Fastest Centuries')
                FastestFifties=FastestFifties.reset_index(drop=True)
                st.write(FastestFifties)
                top20FastestFifties=FastestFifties.head(20)

                BarFastestFifties=alt.Chart(top20FastestFifties).mark_bar().encode(
                                x='Runs',
                                y=alt.Y('Player', sort='-x'),
                                tooltip=['BF'],
                                color='Against',
                                
                                )
                st.altair_chart(BarFastestFifties,use_container_width=True)
        with tabbat6:
                                ###### Most Runs over ###########
                        MostRunsover = pd.read_csv("IPLDataset/AllSeasonsCombined/Most Runs Per Over All Seasons Combine.csv")
                        MostRunsover=MostRunsover.sort_values(by=['Runs'],ascending=False)
                        st.write('## Most Runs over')
                        MostRunsover=MostRunsover.reset_index(drop=True)
                        st.write(MostRunsover)
                        top20MostRunsover=MostRunsover.head(20)

                        BarMostRunsover=alt.Chart(top20MostRunsover).mark_bar().encode(
                                        x='Runs',
                                        y=alt.Y('Player', sort='-x'),
                                        tooltip=['Runs','Match Date'],
                                        color='Against',
                                        
                                        )
                        st.altair_chart(BarMostRunsover,use_container_width=True)
with seasons:
        
        options = st.selectbox(
        'Select Year',
        ["2008", '2009', '2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021',])
        if options ==options:
                tabbat1,tabbat2,tabbat3,tabbat4,tabbat5,tabbat6=st.tabs(['Most Runs','Most Sixes Innings','Most Fours Innings','Fastest Centuries','Fastest Fifties','Most Runs Over'])
                with tabbat1:
                                ###### Most Runs ###########
                        MostRuns = pd.read_csv("IPLDataset/MostRuns/Most Runs - "+options+".csv")
                        MostRuns=MostRuns.sort_values(by=['Runs'],ascending=False)
                        st.write('## Most Runs ')
                        MostRuns=MostRuns.reset_index(drop=True)
                        st.write(MostRuns)
                        top20MostRuns=MostRuns.head(20)

                        BarMostRuns=alt.Chart(top20MostRuns).mark_bar().encode(
                                        x='Runs',
                                        y=alt.Y('Player', sort='-x'),
                                        tooltip=['Runs'],
                                        color='Player',
                                        order=alt.Order(
                                        # Sort the segments of the bars by this field
                                        'Runs',
                                        sort='descending'
                                        )
                                        )
                        st.altair_chart(BarMostRuns,use_container_width=True)

                with tabbat2:
                                ###### Most Sixes Innings ###########
                        MostSixesInnings = pd.read_csv("IPLDataset/MostSixesInnings/Most Sixes Innings - "+options+".csv")
                        MostSixesInnings=MostSixesInnings.sort_values(by=['6s'],ascending=False)
                        st.write('## Most Sixes Innings ')
                        MostSixesInnings=MostSixesInnings.reset_index(drop=True)
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
                        MostFoursInnings = pd.read_csv("IPLDataset/MostFoursInnings/Most Fours Innings - "+options+".csv")
                        MostFoursInnings=MostFoursInnings.sort_values(by=['4s'],ascending=False)
                        st.write('## Most Fours Innings ')
                        MostFoursInnings=MostFoursInnings.reset_index(drop=True)
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
                        FastestCenturies = pd.read_csv("IPLDataset/FastestCenturies/Fastest Centuries - "+options+".csv")
                        FastestCenturies=FastestCenturies.sort_values(by=['BF'],ascending=True)
                        st.write('## Fastest Centuries')
                        FastestCenturies=FastestCenturies.reset_index(drop=True)
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
                        FastestFifties = pd.read_csv("IPLDataset/FastestFifties/Fastest Fifties - "+options+".csv")
                        FastestFifties=FastestFifties.sort_values(by=['BF'],ascending=True)
                        st.write('## Fastest Centuries')
                        FastestFifties=FastestFifties.reset_index(drop=True)
                        st.write(FastestFifties)
                        top20FastestFifties=FastestFifties.head(20)

                        BarFastestFifties=alt.Chart(top20FastestFifties).mark_bar().encode(
                                        x='Runs',
                                        y=alt.Y('Player', sort='-x'),
                                        tooltip=['BF'],
                                        color='Against',
                                        
                                        )
                        st.altair_chart(BarFastestFifties,use_container_width=True)
                with tabbat6:
                                ###### Most Runs over ###########
                        MostRunsover = pd.read_csv("IPLDataset/MostRunsOver/Most Runs Over - "+options+".csv")
                        MostRunsover=MostRunsover.sort_values(by=['Runs'],ascending=False)
                        st.write('## Most Runs over')
                        MostRunsover=MostRunsover.reset_index(drop=True)
                        st.write(MostRunsover)
                        top20MostRunsover=MostRunsover.head(20)

                        BarMostRunsover=alt.Chart(top20MostRunsover).mark_bar().encode(
                                        x='Runs',
                                        y=alt.Y('Player', sort='-x'),
                                        tooltip=['Runs','Match Date'],
                                        color='Against',
                                        
                                        )
                        st.altair_chart(BarMostRunsover,use_container_width=True)


