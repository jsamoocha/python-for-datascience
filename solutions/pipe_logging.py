def df_info(df):
    if df is not None:
        column_info = ','.join([f'{col} ({df[col].isnull().sum()} missing)' for col in df])
        return f'rows: {len(df)}, columns: {column_info}'
    else:
        return '<None>'

def pipe_logging(func):
    @wraps(func)
    def logging_wrapper(*args, **kwargs):
        in_df = args[0]
        logger.debug(f'Calling pipeline function {func.__name__} with input {df_info(in_df)}')
        start = time.time()
        out = func(*args, **kwargs)
        stop = time.time()
        logger.debug(f'Returning dataframe with {df_info(out)}')
        logger.debug(f'Took {stop - start:.4f}s')
        return out

    return logging_wrapper
