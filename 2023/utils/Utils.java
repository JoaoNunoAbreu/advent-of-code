package utils;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;

public class Utils {

    private Utils() {}

    public static List<String> readFile(String filename) {
        try {
            return Files.lines(Paths.get(filename)).collect(Collectors.toList());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public static String reverseString(String str) {
        return new StringBuilder(str).reverse().toString();
    }
}
