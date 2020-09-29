(
    activity_df
    .loc[lambda df: df['type'] == 'Ride']
    .assign(day_of_week=lambda df: df['start_date_local'].dt.dayofweek)
    .groupby('day_of_week')[['elapsed_time']].mean()
    .assign(hours=lambda df: df['elapsed_time'] / 3600)
)
