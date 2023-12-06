package day01;

import java.util.List;
import java.util.Map;

import static java.lang.Character.isDigit;
import static utils.Utils.readFile;
import static utils.Utils.reverseString;

public class Main {
    private static final String DAY_FILE = "/Users/abreuj/dev/general/advent-of-code/2023/day01/input.txt";
    private static final Map<String, Integer> numbers = Map.of(
            "one", 1, "two", 2, "three", 3, "four", 4, "five", 5, "six", 6, "seven", 7, "eight", 8, "nine", 9
    );
    private static final Map<String, Integer> reversedNumbers = Map.of(
            "eno", 1, "owt", 2, "eerht", 3, "ruof", 4, "evif", 5, "xis", 6, "neves", 7, "thgie", 8, "enin", 9
    );

    // ---------------------------------------------------------------------------------------------------------

    public static int part1(List<String> data) {
        return data.stream()
                .map(line -> line.replaceAll("\\s*[a-z]\\s*", ""))
                .map(line -> line.charAt(0) + String.valueOf(line.charAt(line.length() - 1)))
                .mapToInt(Integer::parseInt)
                .sum();
    }

    // ---------------------------------------------------------------------------------------------------------
    public static String iterator(String line){
        int begin = 0;
        while (begin < line.length()) {
            for (int i = begin; i < line.length(); i++) {
                if(i == begin && isDigit(line.charAt(i))){
                    return String.valueOf(line.charAt(i));
                }

                String word = line.substring(begin, i + 1);
                if (numbers.containsKey(word)) {
                    return numbers.get(word).toString();
                }
                if (reversedNumbers.containsKey(word)) {
                    return reversedNumbers.get(word).toString();
                }
            }
            begin++;
        }
        return line;
    }

    public static String converter(String line) {
        String first = iterator(line);
        String second = iterator(reverseString(line));
        return first + second;
    }

    public static int part2(List<String> data) {
        return data.stream()
                .map(Main::converter)
                .map(line -> line.charAt(0) + String.valueOf(line.charAt(line.length() - 1)))
                .mapToInt(Integer::parseInt)
                .sum();
    }

    public static void main(String[] args) {
        List<String> data = readFile(DAY_FILE);
        System.out.println("Part 1: " + part1(data));
        System.out.println("Part 2: " + part2(data));
    }
}
