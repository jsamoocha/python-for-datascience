(
    activity_df
    .loc[lambda df: df['type'] == 'Run']
    .assign(year=lambda df: df['start_date_local'].dt.year)
    .groupby('year')['distance'].max()
)
