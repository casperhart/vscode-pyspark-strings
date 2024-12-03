from pyspark.sql import SparkSession


def test():
    """Test pyspark strings"""
    spark = SparkSession.builder.getOrCreate()
    # not highlighted in comments
    ## spark.sql("select * from users")

    # single line
    spark.sql("select * from users")  # comments still work

    # triple quotes
    spark.sql("""select * from users""")

    # testing strings still work (syntax above was closed)
    table = "users"
    spark.sql(f"select * from {table}")
    spark.sql(f"""select * from {table}""")

    # mutli-line
    spark.sql(
        f"""
        select 
            col1,
            col2
        from 
            users
        where
            col1 = 'value'
        """
    )

    # make sure multi-line doesn't break single-line
    spark.sql("select * from users")
    spark.sql("""select * from users""")
