# sample_job.py
from pyspark.sql import SparkSession

if __name__ == "__main__":
    # Initialize Spark session
    spark = SparkSession.builder.appName("SampleJob").getOrCreate()
    
    # Sample data
    data = [("Alice", 29), ("Bob", 35), ("Cathy", 23)]
    columns = ["Name", "Age"]
    
    # Create DataFrame
    df = spark.createDataFrame(data, columns)
    
    # Show DataFrame
    df.show()
    
    # Write to a table (optional)
    df.write.format("delta").mode("overwrite").saveAsTable("sample_table")
    
    print("Job completed successfully!")