package day01;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static List<String> readFile(String filename) {
        List<String> data = new ArrayList<>();
        try (Scanner myReader = new Scanner(new File(filename))) {
            while (myReader.hasNextLine()) {
                data.add(myReader.nextLine());
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        return data;
    }

    public static void main(String[] args) {
        String dayFile = System.getProperty("user.dir") + "/2023/day01/input.txt";
        List<String> data = readFile(dayFile);
        System.out.println(data);
    }
}
