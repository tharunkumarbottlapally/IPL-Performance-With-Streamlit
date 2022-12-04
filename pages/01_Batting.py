import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.markdown("# Batting 🏏")
st.sidebar.markdown("# Batting 🏏")
tabbat1,tabbat2,tabbat3,tabbat4,tabbat5=st.tabs(['Most Runs','Most Sixes Innings','Most Fours Innings','Fastest Centuries','Fastest Fifties'])
with tabbat1:
                    ###### Most Runs ###########
            MostRuns = pd.read_csv("IPLDataset/AllSeasonsCombined/Most Runs All Seasons Combine.csv")
            MostRuns=MostRuns.sort_values(by=['Runs'],ascending=False)
            st.write('## Most Runs ')
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
            MostSixesInnings = pd.read_csv("IPLDataset/AllSeasonsCombined/Most Sixes Per Innings All Seasons Combine.csv")
            MostSixesInnings=MostSixesInnings.sort_values(by=['6s'],ascending=True)
            st.write('## Most Sixes Innings ')
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
            MostFoursInnings = pd.read_csv("IPLDataset/AllSeasonsCombined/Most Fours Per Innings All Seasons Combine.csv")
            MostFoursInnings=MostFoursInnings.sort_values(by=['4s'],ascending=True)
            st.write('## Most Fours Innings ')
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
            FastestCenturies = pd.read_csv("IPLDataset/AllSeasonsCombined/Fastest Centuries All Seasons Combine.csv")
            FastestCenturies=FastestCenturies.sort_values(by=['BF'],ascending=True)
            st.write('## Fastest Centuries')
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
            st.write(FastestFifties)
            top20FastestFifties=FastestFifties.head(20)

            BarFastestFifties=alt.Chart(top20FastestFifties).mark_bar().encode(
                            x='Runs',
                            y=alt.Y('Player', sort='-x'),
                            tooltip=['BF'],
                            color='Against',
                            
                            )
            st.altair_chart(BarFastestFifties,use_container_width=True)
