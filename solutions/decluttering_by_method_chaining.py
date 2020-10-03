(
    activity_df
    .loc[lambda df: df['start_date_local'].dt.year == 2018]
    .groupby('type')['velocity_mean'].mean()
)
