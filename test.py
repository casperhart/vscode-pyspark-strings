from pyspark.sql import SparkSession


def test():

    spark = SparkSession.builder.getOrCreate()
    spark.sql("select * from users")

    spark.sql("""select * from users""")

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
        """
    )

    # make sure multi-line doesn't break single-line
    spark.sql("select * from users")
    spark.sql("""select * from users""")
