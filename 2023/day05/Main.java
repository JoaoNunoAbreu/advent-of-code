package day05;

import utils.Trio;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;

import static utils.Utils.readFile;

public class Main {
    private static final String DAY_FILE = System.getProperty("user.dir") + "/2023/day05/input.txt";

    // ---------------------------------------------------------------------------------------------------------

    private static double getMapping(Map<String, List<Trio<Double, Double, Double>>> map, String level, double val) {
        for (Trio<Double, Double, Double> trio : map.get(level)) {
            if (trio.getSecond() <= val && val < trio.getSecond() + trio.getThird()) {
                return trio.getFirst() + (val - trio.getSecond());
            }
        }
        return val;
    }

    private static String[] findOrder(Set<String> list) {
        String [] res = new String[list.size()];
        res[0] = "seed-to-soil";
        for (int i = 1; i < list.size(); i++) {
            for (String s : list) {
                if (s.startsWith(res[i - 1].split("-to-")[1])) {
                    res[i] = s;
                }
            }
        }
        return res;
    }

    private static Map<String, List<Trio<Double, Double, Double>>> process(List<String> data) {
        Map<String, List<Trio<Double, Double, Double>>> map = new HashMap<>();
        String mapName = "";
        for (String line : data) {
            if (line.contains("map")) {
                mapName = line.split(" map")[0];
            }
            if (Character.isDigit(line.charAt(0))) {
                String[] split = line.split(" ");
                double destination = Double.parseDouble(split[0]);
                double source = Double.parseDouble(split[1]);
                double range = Double.parseDouble(split[2]);
                map.computeIfAbsent(mapName, k -> new ArrayList<>()).add(new Trio<>(destination, source, range));
            }
        }
        return map;
    }

    private static double getMin(double[] seeds, String[] order, Map<String, List<Trio<Double, Double, Double>>> map) {
        double min = Double.MAX_VALUE;
        for (double seed : seeds) {
            double current = seed;
            for (String s : order) {
                current = getMapping(map, s, current);
            }
            min = Math.min(min, current);
        }
        return min;
    }

    public static double part1(List<String> data) {
        double[] seeds = Arrays.stream(data.get(0).split("seeds: ")[1].split(" "))
                .mapToDouble(Double::parseDouble)
                .toArray();
        Map<String, List<Trio<Double, Double, Double>>> map = process(data);
        String[] order = findOrder(map.keySet());
        return getMin(seeds, order, map);
    }

    // ---------------------------------------------------------------------------------------------------------

    public static int part2(List<String> data) {
        // this will be fun
        return 0;
    }

    // ---------------------------------------------------------------------------------------------------------

    public static void main(String[] args) {
        List<String> data = readFile(DAY_FILE).stream()
                .filter(line -> !line.isEmpty())
                .toList();
        System.out.printf("Part 1: %.0f\n", part1(data));
        System.out.println("Part 2: " + part2(data));
    }
}

