package day03;

import utils.Pair;

import java.util.*;

import static utils.Utils.readFile;

public class Main {
    private static final String DAY_FILE = System.getProperty("user.dir") + "/2023/day03/input.txt";
    private static int NUM_ROWS = 0;
    private static int NUM_COLS = 0;

    // ---------------------------------------------------------------------------------------------------------

    public static void printMatrix(Character[][] matrix) {

        for (int i = 0; i < NUM_COLS; i++) {
            if (i == 0) {
                System.out.print("    ");
            }
            System.out.print(i + " ");
        }
        System.out.println();

        for (int i = 0; i < NUM_ROWS; i++) {
            System.out.print(i + " | ");
            for (int j = 0; j < NUM_COLS; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static Character[][] process(List<String> data) {
        NUM_ROWS = data.size();
        int maxStringLength = 0;
        for (String str : data) {
            maxStringLength = Math.max(maxStringLength, str.length());
        }

        NUM_COLS = maxStringLength;
        Character[][] result = new Character[NUM_ROWS][NUM_COLS];

        for (int i = 0; i < NUM_ROWS; i++) {
            String str = data.get(i);
            for (int j = 0; j < str.length(); j++) {
                result[i][j] = str.charAt(j);
            }
        }

        return result;
    }

    public static boolean isNearSymbol(Character[][] matrix, int row, int column) {
        // left
        if (column > 0 && !Character.isDigit(matrix[row][column - 1]) && matrix[row][column - 1] != '.') {
            return true;
        }
        // right
        if (column < NUM_COLS - 1 && !Character.isDigit(matrix[row][column + 1]) && matrix[row][column + 1] != '.') {
            return true;
        }
        // up
        if (row > 0 && !Character.isDigit(matrix[row - 1][column]) && matrix[row - 1][column] != '.') {
            return true;
        }
        // down
        if (row < NUM_ROWS - 1 && !Character.isDigit(matrix[row + 1][column]) && matrix[row + 1][column] != '.') {
            return true;
        }
        // upper left diagonal
        if (row > 0 && column > 0 && !Character.isDigit(matrix[row - 1][column - 1]) && matrix[row - 1][column - 1] != '.') {
            return true;
        }
        // upper right diagonal
        if (row > 0 && column < NUM_COLS - 1 && !Character.isDigit(matrix[row - 1][column + 1]) && matrix[row - 1][column + 1] != '.') {
            return true;
        }
        // lower left diagonal
        if (row < NUM_ROWS - 1 && column > 0 && !Character.isDigit(matrix[row + 1][column - 1]) && matrix[row + 1][column - 1] != '.') {
            return true;
        }
        // lower right diagonal
        return row < NUM_ROWS - 1 && column < NUM_COLS - 1 && !Character.isDigit(matrix[row + 1][column + 1]) && matrix[row + 1][column + 1] != '.';
    }

    public static Pair<Integer, Integer> isNearAsterisk(Character[][] matrix, int row, int column) {
        // left
        if (column > 0 && matrix[row][column - 1] == '*') {
            return new Pair<>(row, column - 1);
        }
        // right
        if (column < NUM_COLS - 1 && matrix[row][column + 1] == '*') {
            return new Pair<>(row, column + 1);
        }
        // up
        if (row > 0 && matrix[row - 1][column] == '*') {
            return new Pair<>(row - 1, column);
        }
        // down
        if (row < NUM_ROWS - 1 && matrix[row + 1][column] == '*') {
            return new Pair<>(row + 1, column);
        }
        // upper left diagonal
        if (row > 0 && column > 0 && matrix[row - 1][column - 1] == '*') {
            return new Pair<>(row - 1, column - 1);
        }
        // upper right diagonal
        if (row > 0 && column < NUM_COLS - 1 && matrix[row - 1][column + 1] == '*') {
            return new Pair<>(row - 1, column + 1);
        }
        // lower left diagonal
        if (row < NUM_ROWS - 1 && column > 0 && matrix[row + 1][column - 1] == '*') {
            return new Pair<>(row + 1, column - 1);
        }
        // lower right diagonal
        if (row < NUM_ROWS - 1 && column < NUM_COLS - 1 && matrix[row + 1][column + 1] == '*') {
            return new Pair<>(row + 1, column + 1);
        }
        return null;
    }

    public static Map<Integer, List<List<Pair<Integer, Integer>>>> numbersAndPositions(Character[][] matrix) {
        Map<Integer, List<List<Pair<Integer, Integer>>>> res = new HashMap<>();
        for (int row = 0; row < NUM_ROWS; row++) {
            for (int col = 0; col < NUM_COLS; col++) {
                StringBuilder number = new StringBuilder();
                List<Pair<Integer, Integer>> coordinates = new ArrayList<>();
                if (Character.isDigit(matrix[row][col])) {
                    int i = col;
                    while (i < NUM_COLS && Character.isDigit(matrix[row][i])) {
                        if (Character.isDigit(matrix[row][i])) {
                            number.append(matrix[row][i]);
                            coordinates.add(new Pair<>(row, i));
                        }
                        i++;
                    }
                    if (res.containsKey(Integer.parseInt(number.toString()))) {
                        res.get(Integer.parseInt(number.toString())).add(coordinates);
                    } else {
                        res.put(Integer.parseInt(number.toString()), new ArrayList<>(Collections.singletonList(coordinates)));
                    }
                    col = i;
                }
            }
        }
        return res;
    }

    public static int part1(List<String> data) {
        Character[][] matrix = process(data);
        printMatrix(matrix);
        System.out.println(numbersAndPositions(matrix));

        Map<Integer, List<List<Pair<Integer, Integer>>>> numbersAndPositions = numbersAndPositions(matrix);
        List<Integer> nearSymbols = new ArrayList<>();
        for (Map.Entry<Integer, List<List<Pair<Integer, Integer>>>> entry : numbersAndPositions.entrySet()) {
            for (List<Pair<Integer, Integer>> list : entry.getValue()) {
                boolean isNear = false;
                for (Pair<Integer, Integer> pair : list) {
                    if (isNearSymbol(matrix, pair.getFirst(), pair.getSecond())) {
                        isNear = true;
                    }
                }
                if (isNear) {
                    nearSymbols.add(entry.getKey());
                }
            }
        }
        System.out.println(nearSymbols);
        return nearSymbols.stream().mapToInt(Integer::intValue).sum();
    }

    // ---------------------------------------------------------------------------------------------------------

    public static int part2(List<String> data) {
        Character[][] matrix = process(data);
        printMatrix(matrix);
        System.out.println(numbersAndPositions(matrix));

        Map<Integer, List<List<Pair<Integer, Integer>>>> numbersAndPositions = numbersAndPositions(matrix);
        Map<Pair<Integer, Integer>, List<List<Pair<Integer, Integer>>>> asterisksAndNearNumbers = new HashMap<>();

        for (Map.Entry<Integer, List<List<Pair<Integer, Integer>>>> entry : numbersAndPositions.entrySet()) {
            for (List<Pair<Integer, Integer>> list : entry.getValue()) {
                boolean isNear = false;
                Pair<Integer, Integer> asterisk = null;
                for (Pair<Integer, Integer> pair : list) {
                    Pair<Integer, Integer> asteriskLocal = isNearAsterisk(matrix, pair.getFirst(), pair.getSecond());
                    if (asteriskLocal != null) {
                        isNear = true;
                        asterisk = asteriskLocal;
                        break;
                    }
                }
                if (isNear) {
                    if (asterisksAndNearNumbers.containsKey(asterisk)) {
                        asterisksAndNearNumbers.get(asterisk).add(list);
                    } else {
                        asterisksAndNearNumbers.put(asterisk, new ArrayList<>(Collections.singletonList(list)));
                    }
                }
            }
        }
        return getSum(asterisksAndNearNumbers, matrix);
    }

    private static int getSum(Map<Pair<Integer, Integer>, List<List<Pair<Integer, Integer>>>> asterisksAndNearNumbers, Character[][] matrix) {
        int sum = 0;
        for (Map.Entry<Pair<Integer, Integer>, List<List<Pair<Integer, Integer>>>> entry : asterisksAndNearNumbers.entrySet()) {
            List<Integer> numbers = new ArrayList<>();
            for (List<Pair<Integer, Integer>> list : entry.getValue()) {
                StringBuilder str = new StringBuilder();
                for (Pair<Integer, Integer> pair : list) {
                    str.append(matrix[pair.getFirst()][pair.getSecond()]);
                }
                numbers.add(Integer.parseInt(str.toString()));
            }
            if (numbers.size() == 2) {
                sum += numbers.get(0) * numbers.get(1);
            }
        }
        return sum;
    }

    // ---------------------------------------------------------------------------------------------------------

    public static void main(String[] args) {
        List<String> data = readFile(DAY_FILE);
        System.out.println("Part 1: " + part1(data));
        System.out.println("Part 2: " + part2(data));
    }
}

