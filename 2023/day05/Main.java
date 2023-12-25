package day05;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static utils.Utils.readFile;

public class Main {
    private static final String DAY_FILE = System.getProperty("user.dir") + "/2023/day05/input.txt";

    // ---------------------------------------------------------------------------------------------------------

    private static Map<Double, Double> createMappings(String lineWithNumbers) {
        Map<Double, Double> map = new HashMap<>();
        String[] split = lineWithNumbers.split(" ");
        double destination = Double.parseDouble(split[0]);
        double source = Double.parseDouble(split[1]);
        double range = Double.parseDouble(split[2]);
        for (double i = 0; i < range; i++) {
            map.put(i + source, i + destination);
        }

        return map;
    }

    private static Map<String, Map<Double, Double>> process(List<String> data) {
        Map<String, Map<Double, Double>> map = new HashMap<>();
        String mapName = "";
        for (String line : data) {
            if (line.contains("map")) {
                mapName = line.split(" map")[0];
            }
            if (Character.isDigit(line.charAt(0))) {
                Map<Double, Double> mappings = createMappings(line);
                if (map.containsKey(mapName)) {
                    mappings.putAll(map.get(mapName));
                }
                map.put(mapName, mappings);
            }
        }
        return map;
    }

    private static double iterate(double i, Map<String, Map<Double, Double>> process) {
        double converted = process.get("seed-to-soil").getOrDefault(i, i);
        String firstWordConverter = "soil";
        boolean stop = false;
        boolean found = false;
        double res = 0;
        while (!stop) {
            String nextConverter;
            for(String converter : process.keySet()) {
                if (converter.startsWith(firstWordConverter)) {
                    firstWordConverter = converter.split("-to-")[1];
                    nextConverter = converter;
                    found = true;

                    converted = process.get(nextConverter).getOrDefault(converted, converted);
                    res = converted;

                    break;
                }
            }
            if (!found) {
                stop = true;
            }
            found = false;
        }
        return res;
    }

    public static double part1(List<String> data) {
        double[] seeds = Arrays.stream(data.get(0).split("seeds: ")[1].split(" "))
                .mapToDouble(Double::parseDouble)
                .toArray();
        Map<String, Map<Double, Double>> process = process(data);
        double min = Double.MAX_VALUE;
        for (double i : seeds) {
            min = Math.min(min, iterate(i, process));
        }
        return min;
    }

    // ---------------------------------------------------------------------------------------------------------

    public static int part2(List<String> data) {
        return 0;
    }

    // ---------------------------------------------------------------------------------------------------------

    public static void main(String[] args) {
        List<String> data = readFile(DAY_FILE).stream()
                .filter(line -> !line.isEmpty())
                .toList();
        System.out.println("Part 1: " + part1(data));
        System.out.println("Part 2: " + part2(data));
    }
}

