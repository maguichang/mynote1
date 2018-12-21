
import org.apache.spark.{SparkContext,SparkConf}

//aggregate 方法
object testRDDMethod {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf()      //创建环境变量
      .setMaster("local")           //设置本地化处理
      .setAppName("testRDDMethod")
    val sc = new SparkContext(conf)
    val arr = sc.parallelize(Array(1,2,3,4,5,6))
    val result = arr.aggregate(0)(math.max(_, _), _+ _)
    println("---------")
    println("result:",result)
    println("---------")

    //    将数据分成两个节点进行存储
    val arr2 = sc.parallelize(Array(1,2,3,4,5,6),2)
    val result2 = arr2.aggregate(0)(math.max(_, _), _+ _)     //将两个节点上的最大值进行相加3+6=9
    println("---------")
    println("result2:",result2)
    println("---------")

    //    aggregate的字符串操作
    val arr3 = sc.parallelize(Array("abc","b","c","d","e","f"))
    val result3 = arr3.aggregate("")((value,word) => value+word,_+_)
    println("---------")
    println("result3:",result3)
    println("---------")

  }

}
