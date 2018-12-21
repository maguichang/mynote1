import org.apache.spark.{SparkConf,SparkContext}
import org.apache.spark.rdd.RDD
import org.apache.spark.mllib.fpm.{FPGrowth,FPGrowthModel}
object FPTree {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf().setMaster("local").setAppName("FPTree")
    val sc = new SparkContext(conf)
    val data = sc.textFile("C:\\Users\\dell\\Desktop\\NLP\\fp.txt")
    val exampleRDD = data.map(_.split(" ")).cache()
    val fpg = new FPGrowth().setMinSupport(0.7).run(exampleRDD)
//    val model = fpg.run(data)
//    data.foreach(println)
    println(s"Number of frequent itemsets: ${fpg.freqItemsets.count()}")
//    fpg.freqItemsets.collect().foreach { itemset =>
//      println(itemset.items.mkString("[", ",", "]") + ":" + itemset.freq)
//    }
    print("end...")

  }

}
