package day02;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

import static utils.Utils.readFile;

public class Main {
    private static final String DAY_FILE = System.getProperty("user.dir") + "/2023/day02/input.txt";
    private static final Map<String, Integer> LIMITS = Map.of(
            "red", 12, "green", 13, "blue", 14
    );

    private static List<String[]> process(List<String> data) {
        return data.stream()
                .map(line -> line.replaceAll("Game \\d+: ", ""))
                .map(line -> line.split(";"))
                .map(line -> Arrays.stream(line).map(String::trim).toArray(String[]::new))
                .collect(Collectors.toList());
    }

    // ---------------------------------------------------------------------------------------------------------
    public static int part1(List<String> data) {
        List<String[]> processed = process(data);

        int i = 1;
        int res = 0;
        for (String[] lines : processed) {
            boolean invalid = false;
            for (String line : lines) {
                String[] pairs = line.split(", ");
                for (String pair : pairs) {
                    String[] singlePair = pair.split(" ");
                    int number = Integer.parseInt(singlePair[0]);
                    String color = singlePair[1];
                    if (number > LIMITS.get(color)) {
                        invalid = true;
                    }
                }
            }
            if (!invalid) {
                res += i;
            }
            i++;
        }
        return res;
    }

    // ---------------------------------------------------------------------------------------------------------
    public static int part2(List<String> data) {
        List<String[]> processed = process(data);

        int res = 0;
        for (String[] lines : processed) {
            Map<String, Integer> colors = new HashMap<>();
            for (String line : lines) {
                String[] pairs = line.split(", ");
                for (String pair : pairs) {
                    String[] singlePair = pair.split(" ");
                    int number = Integer.parseInt(singlePair[0]);
                    String color = singlePair[1];
                    colors.compute(color, (key, existingNumber) -> existingNumber == null
                            ? number
                            : Math.max(existingNumber, number)
                    );
                }
            }
            res += colors.values().stream().reduce(1, (a, b) -> a * b);
        }
        return res;
    }

    // ---------------------------------------------------------------------------------------------------------

    public static void main(String[] args) {
        List<String> data = readFile(DAY_FILE);
        System.out.println("Part 1: " + part1(data));
        System.out.println("Part 2: " + part2(data));
    }
}

