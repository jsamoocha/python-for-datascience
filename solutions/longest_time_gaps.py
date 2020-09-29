(
    activity_df
    .sort_values('start_date_local')
    .assign(time_gap=lambda df: df['start_date_local'].diff())
    .sort_values('time_gap', ascending=False)
    .head(10)
)
