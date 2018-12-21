import org.apache.spark.{SparkContext,SparkConf}

object CacheTest {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf().setAppName("MethodTest").setMaster("local")
    val sc = new SparkContext(conf)

    val arr = sc.parallelize(Array("abc","d","e","f")) //设定数据集
    println(arr)
    println("-----------------")
    //    提前计算的cache方法
    println(arr.cache())//cache用在spark lazy 模式，数据在编译和未使用时时不进行计算的
    println(arr.foreach(println))//迭代形式打印数据

    //    笛卡尔操作的cartesian方法
    val arr2 = sc.parallelize(Array(1,2,3,4,5,6))
    val arr3 = sc.parallelize(Array(6,5,4,3,2,1))

    val result = arr2.cartesian(arr3)//进行笛卡尔积运算
    println("-----------------")
    result.foreach(print)
    println("-----------------")

    //    分片存储的coalesce方法
    val arr4 = arr2.coalesce(2,true)//将数据重新分区
    val result2 = arr2.aggregate(0)(math.max(_,_),_+_)//计算数据值
    println("-----------------")
    println("result2",result2)
    println("-----------------")

    //    计算重新分区的数据值
    val result3 = arr4.aggregate(0)(math.max(_,_),_+_)//计算数据值
    println("-----------------")
    println("result3",result3)
    println("-----------------")

    //    以value计算的countByValue方法
    //    计算数据集中某个数据出现的个数，以map形式返回
    val result4 = arr2.countByValue()
    println("-----------------")
    result4.foreach(print)
    println("-----------------")

    //    以key计算的countByKey方法
    val arr5 = sc.parallelize(Array((1,"a"),(1,"c"),(2,"b"),(3,"f"),(2,"b")))
    val result5 = arr5.countByKey()
    println("countByKey-----------------")
    result5.foreach(print)
    println("-----------------")

    //    去重distinct
    val result6 = arr5.distinct()
    println("distinct-----------------")
    result6.foreach(println)
    println("-----------------")

    //    过滤的filter方法
    /*
    在fileter方法中，使用的方法是“_>=3”,下划线的作用是作为占位符标记所有的传过来的数据。
    在此方法中，数组的数据（1,2,3,4,5）依次传进来代替占位符
     */
    val result7 = arr2.filter(_>=3) //进行筛选
    println("filter-----------------")
    result7.foreach(println)
    println("-----------------")

    //    以行为单位操作数据的flatMap方法
    val result8 = arr2.flatMap(x => List(x+1)).collect()//进行数据集计算
    println("flatMap-----------------")
//    println("result8",result8)
    result8.foreach(println)
    println("-----------------")

//    以单个数据为目标操作的map方法
    val result9 = arr2.map(x => List(x+1)).collect()//进行单个数据计算
    println("map-----------------")
    result9.foreach(println)
    println("-----------------")

//    分组数据的groupBy方法,(打印的结果有问题)
    val result10 = arr2.groupBy(myFilter(_),1).collect()//设置第一个分组
    val result11 = arr2.groupBy(myFilter2(_),2).collect()//设置第二个分组
    println("groupBy-----------------")
    result10.foreach(print)
    result11.foreach(print)
    println("-----------------")

//    生成键值对的keyBy方法
    val str = sc.parallelize(Array("one","two","three","four"))
    val str2 = str.keyBy(word=>word.size)
    str2.foreach(println)

//    同时对两个数据进行处理的reduce方法
    val result12 = str.reduce(_+_)
    result12.foreach(print)

//    sortBy 方法
    var str3 = sc.parallelize(Array((5,"B"),(6,"A"),(3,"C")))
    val str4 = str3.sortBy(word=>word._1,true)
    val str5 = str3.sortBy(word=>word._2,true)
    str4.foreach(print)
    str5.foreach(print)

//    合并压缩的zip方法
    val s1 = Array(1,2,3)
    val s2 = Array('a','b','c')
    val s3 = Array('x','y','z')
    val s4 =s1.zip(s2).zip(s3)
    s4.foreach(print)
  }
  def myFilter(num: Int):Unit = {//自定义方法
    num >= 3 //条件
  }
  def myFilter2(num: Int):Unit = {
    num < 3
  }

}
