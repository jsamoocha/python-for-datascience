(
    activity_df
    .set_index('start_date_local')
    .sort_index()
    .assign(total_time_7days=lambda df: df.rolling('7d')['elapsed_time'].sum() / 3600)
    .sort_values('total_time_7days', ascending=False)
    .head(10)
)
