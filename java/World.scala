object World {
  def main(args: Array[String]) {
    println("Hello, world!")
    def add(x:Int, y:Int):Int = {
      return x + y
    }
    import collection.mutable
    val mlist = mutable.MutableList("a", "b", "c")
    var list1 = List('a','b','c')
    val list2 = List(1,2,3)
    val list3 = list1 ++ list2
    list1 :+ 'd'
    mlist += "d"
    val x = 1
    println(x.map{1 => "a"})
  }
}
