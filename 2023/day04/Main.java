package day04;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static utils.Utils.readFile;

public class Main {
    private static final String DAY_FILE = System.getProperty("user.dir") + "/2023/day04/input2.txt";

    private static int calculateMultiplier(int cardNumber) {
        return (int) Math.pow(2, (double) cardNumber - 1);
    }

    private static List<List<List<Integer>>> process(List<String> data) {
        return data.stream()
                .map(s -> s.replaceAll("^.*?: ", "").trim())
                .map(s -> s.split(" \\| "))
                .map(listStr -> Arrays.stream(listStr)
                        .map(String::trim)
                        .map(s -> s.replace("  ", " "))
                        .map(s -> s.split(" "))
                        .map(s -> Arrays.stream(s)
                                .map(Integer::parseInt)
                                .toList())
                        .toList())
                .toList();
    }

    private static List<Integer> calculateMatching(List<List<List<Integer>>> list) {
        List<Integer> matching = new ArrayList<>();
        for (List<List<Integer>> game : list) {
            int sum = 0;
            List<Integer> winningNumbers = game.get(0);
            List<Integer> myNumbers = game.get(1);
            sum += winningNumbers.stream()
                    .filter(myNumbers::contains)
                    .toList()
                    .size();
            matching.add(sum);
        }
        return matching;
    }

    // ---------------------------------------------------------------------------------------------------------

    public static int part1(List<String> data) {
        List<List<List<Integer>>> list = process(data);
        List<Integer> result = calculateMatching(list);
        return result.stream().map(Main::calculateMultiplier).mapToInt(Integer::intValue).sum();
    }

    // ---------------------------------------------------------------------------------------------------------

    public static BigInteger part2(List<String> data) {
        List<List<List<Integer>>> list = process(data);
        List<Integer> result = calculateMatching(list);

        Map<Integer, BigInteger> mapper = new HashMap<>();
        for (int i = 0; i < result.size(); i++) {
            mapper.put(i+1, BigInteger.valueOf(1));
        }

        System.out.println(result);

        for (int i = 0; i < result.size(); i++) {
            int game = i + 1;
            int matchers = result.get(i);
            for (int j = 0; j < matchers; j++) {
                int nextGame = game + j + 1;
                int multiplier = calculateMultiplier(game);
                mapper.put(nextGame, mapper.get(nextGame).add(BigInteger.valueOf(multiplier)));
            }
        }
        System.out.println(mapper);
        BigInteger sum = new BigInteger("0");
        for (int i = 0; i < result.size(); i++) {
            sum = sum.add(mapper.get(i+1));
        }
        return sum;
    }

    // [X] 1500089387371

    // ---------------------------------------------------------------------------------------------------------

    public static void main(String[] args) {
        List<String> data = readFile(DAY_FILE);
        System.out.println("Part 1: " + part1(data));
        System.out.println("Part 2: " + part2(data));
    }
}

