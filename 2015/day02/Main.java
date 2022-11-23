import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class Main {

    public static List<String> readFile(String filename) {
        try {
            List<String> content = Files.readAllLines(Paths.get(filename));
            return content;
        } catch (IOException e) {
            e.printStackTrace();
        }
        return List.of();
    }

    public static Integer part1(List<String> input) {
        String sequence = input.get(0);
        char[] chars = sequence.toCharArray();
        Integer floor = 0;
        for (char c : chars) {
            if (c == '(') {
                floor += 1;
            }
            else {
                floor -= 1;
            }
        }
        return floor;
    }

    public static Integer part2(List<String> input) {
        String sequence = input.get(0);
        char[] chars = sequence.toCharArray();
        Integer floor, index;
        floor = index = 0;
        for (char c : chars) {
            if (c == '(') {
                floor += 1;
            }
            else {
                floor -= 1;
            }
            if (floor == -1) {
                return index;
            }
            index += 1;
        }
        return floor;
    }

    public static void main(String[] args) {
        List<String> lines = readFile("input.txt");
        System.out.println("Part 1: " + part1(lines));
        System.out.println("Part 2: " + part2(lines));
    }
}