import java.io.File
import java.io.FileInputStream

fun readFromFile(fileName: String): String {
    val file = File(fileName)
    val size = file.length()
    val buffer = ByteArray(size.toInt())
    val fileInputStream = FileInputStream(file)
    fileInputStream.read(buffer)
    fileInputStream.close()
    return String(buffer)
}

fun part1(lines: List<Int>): Int {
    var count: Int = 0
    for (i in 1 until lines.size) {
        if(lines[i-1] < lines[i]) {
            count++
        }
    }
    return count
}

fun part2(lines: List<Int>): Int {
    var count: Int = 0
    for (i in 1 until lines.size-2) {
        if(lines[i-1] + lines[i] + lines[i+1] < lines[i] + lines[i+1] + lines[i+2]) {
            count++
        }
    }
    return count
}

fun main(){
    val fileName = System.getProperty("user.dir") + "/input.txt"
    val lines = readFromFile(fileName)

    val numbers = lines.split("\n").map { it.toInt() }
    val p1 = part1(numbers)
    println("Part 1: $p1")
    val p2 = part2(numbers)
    println("Part 2: $p2")

}